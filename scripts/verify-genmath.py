#!/usr/bin/env python3
"""
Courses content-integrity gate.

For every topic marked status == "published", asserts:
  - every lesson has a non-empty concreteComparison (hard content-bar requirement);
  - every problem (lesson.workedExamples, lesson.tryIt, topic.practice,
    topic.testYourself) has id / statement / solution and a NON-EMPTY `check`;
  - every interactive tapQuestion step has options / correctIndex / explanation
    and a NON-EMPTY `check`;
  - every `check` string sympifies to a boolean that is True.

No published answer (static or interactive) ships without a passing sympy
hard-assert. Exits non-zero on any failure. Placeholder topics are skipped.

Run: npm run verify:genmath
"""
import glob
import json
import os
import re
import sys

from sympy import sympify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_GLOB = os.path.join(ROOT, "data", "genmath", "**", "*.json")

failures = []
topics_checked = 0

# --- Render-safety (mirrors components/esh/MathText.tsx) -------------------
# Two defect classes are invisible to every other gate:
#   1. A **bold** run containing a complete $...$ pair. MathText's splitter is
#      leftmost-first, so the whole run matches AS BOLD and its content renders
#      as plain text — the math shows up as literal dollar signs. (A lone $ in
#      bold is a currency dollar and renders fine; only a full pair is a bug.)
#   2. A character KaTeX has no glyph for inside a math segment. It draws a
#      blank box with only a console warning — no katex-error node — so even
#      the render QA reports the file clean. ✓ has metrics and is fine;
#      Cyrillic inside \text{} falls back to a browser font and is fine.
# Checked for EVERY file, published or not, so no authoring route can skip it.
MATHTEXT_TOKEN = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)")
MATH_PAIR = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")
DOLLAR_SENTINEL = "\x00"
UNRENDERABLE_IN_MATH = "₮✗"

render_strings_checked = 0


def check_render_safety(label, node):
    global render_strings_checked
    if isinstance(node, str):
        render_strings_checked += 1
        protected = node.replace("\\$", DOLLAR_SENTINEL)
        for tok in MATHTEXT_TOKEN.findall(protected):
            shown = tok.replace(DOLLAR_SENTINEL, "\\$")[:80]
            if tok.startswith("**") and MATH_PAIR.search(tok[2:-2]):
                failures.append(f"{label}: bold run swallows inline math (renders literal $): {shown!r}")
            elif tok.startswith("$") and any(c in tok for c in UNRENDERABLE_IN_MATH):
                failures.append(f"{label}: character KaTeX cannot draw inside math: {shown!r}")
    elif isinstance(node, dict):
        for value in node.values():
            check_render_safety(label, value)
    elif isinstance(node, list):
        for value in node:
            check_render_safety(label, value)

# --- Widget-config contract (derived from lib/genmath-interactive.ts) ------
# A lesson page renders ONLY the interactive player, so a widget handed a
# config its component does not understand fails SILENTLY: React destructures
# the missing key to undefined and the widget draws a label reading
# "only undefined", or falls back to a default mode and plays the wrong
# animation. Nothing throws, nothing logs, and every other gate reports the
# file clean — five vennCounts steps shipped that way across three courses.
#
# The contract is the TypeScript source of truth, parsed rather than
# duplicated: the discriminated union at the bottom of genmath-interactive.ts
# maps each step kind to its <Kind>Config interface, and the interface says
# which keys are required (no `?`) and which take a fixed set of string
# literals. A per-builder allowlist would drift; this cannot.
IFACE_SRC = os.path.join(ROOT, "lib", "genmath-interactive.ts")
_KIND_TO_CONFIG = re.compile(
    r'\|\s*\{\s*kind:\s*"([A-Za-z0-9]+)";[^}]*?config:\s*(\w+Config)\s*\}'
)
_FIELD = re.compile(r"(\w+)(\?)?:\s*([^;]+);")
_STRING_UNION = re.compile(r'(\s*"[^"]+"\s*\|?)+')


def _drop_nested(body):
    """Erase brace-nested types so inline shapes ({ x: number; y: number }[])
    do not leak their inner fields into the top-level field list."""
    out, depth = [], 0
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            out.append("X")
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def load_widget_contract():
    """kind -> {field: (required, allowed_literals or None)}."""
    with open(IFACE_SRC, "r", encoding="utf-8") as fh:
        src = fh.read()
    contract = {}
    for kind, cfg_name in _KIND_TO_CONFIG.findall(src):
        m = re.search(r"export interface " + cfg_name + r"\s*\{\n(.*?)\n\}", src, re.S)
        if not m:
            failures.append(f"widget contract: no interface {cfg_name} for kind {kind!r}")
            continue
        body = _drop_nested(re.sub(r"//[^\n]*", "", m.group(1)))
        fields = {}
        for name, optional, ty in _FIELD.findall(body):
            ty = ty.strip()
            literals = re.findall(r'"([^"]+)"', ty)
            enum = literals if literals and _STRING_UNION.fullmatch(ty) else None
            fields[name] = (optional == "", enum)
        contract[kind] = fields
    return contract


WIDGET_CONTRACT = load_widget_contract()
widget_steps_checked = 0


def check_widget_config(topic_slug, lesson_slug, step):
    global widget_steps_checked
    kind = step.get("kind")
    fields = WIDGET_CONTRACT.get(kind)
    if fields is None:
        return  # not a config-carrying widget kind
    label = f"{topic_slug} / {lesson_slug} / {kind}"
    config = step.get("config")
    if not isinstance(config, dict):
        failures.append(f"{label}: widget step has no config object")
        return
    widget_steps_checked += 1
    for name, (required, enum) in fields.items():
        if required and name not in config:
            failures.append(f"{label}: config missing required key {name!r}")
        if enum and name in config and config[name] not in enum:
            failures.append(
                f"{label}: config[{name!r}] = {config[name]!r} is not one of {enum}"
            )
    for name in config:
        if name not in fields:
            failures.append(f"{label}: config has unknown key {name!r} (the component ignores it)")


problems_checked = 0
tapq_checked = 0
checks_run = 0


def run_checks(label, checks):
    global checks_run
    for expr in checks:
        checks_run += 1
        try:
            result = sympify(expr)
        except Exception as e:  # noqa: BLE001
            failures.append(f"{label}: check did not sympify: {expr!r} ({e})")
            continue
        try:
            ok = bool(result) is True
        except TypeError:
            ok = False
        if not ok:
            failures.append(f"{label}: check is NOT True: {expr!r} -> {result!r}")


def check_problem(topic_slug, where, problem):
    global problems_checked
    pid = problem.get("id", "<no-id>")
    label = f"{topic_slug} / {where} / {pid}"
    for field in ("id", "statement", "solution"):
        if not problem.get(field):
            failures.append(f"{label}: missing '{field}'")
    checks = problem.get("check")
    if not isinstance(checks, list) or len(checks) == 0:
        failures.append(f"{label}: missing non-empty 'check' (every published problem must be sympy-verified)")
        return
    problems_checked += 1
    run_checks(label, checks)


def check_tap_question(topic_slug, where, step):
    global tapq_checked
    label = f"{topic_slug} / {where} / tapQuestion"
    opts = step.get("options")
    ci = step.get("correctIndex")
    if not isinstance(opts, list) or len(opts) < 2:
        failures.append(f"{label}: needs at least 2 options")
    elif not isinstance(ci, int) or not (0 <= ci < len(opts)):
        failures.append(f"{label}: correctIndex {ci!r} out of range")
    if not step.get("prompt"):
        failures.append(f"{label}: missing prompt")
    if not step.get("explanation"):
        failures.append(f"{label}: missing explanation")
    checks = step.get("check")
    if not isinstance(checks, list) or len(checks) == 0:
        failures.append(f"{label}: missing non-empty 'check'")
        return
    tapq_checked += 1
    run_checks(label, checks)


def check_inline(topic_slug, where, item):
    # An inline worked-example or try-it problem (prompt + check, figure optional).
    global problems_checked
    label = f"{topic_slug} / {where}"
    if not item.get("prompt"):
        failures.append(f"{label}: missing prompt")
    checks = item.get("check")
    if not isinstance(checks, list) or len(checks) == 0:
        failures.append(f"{label}: missing non-empty 'check'")
        return
    problems_checked += 1
    run_checks(label, checks)


def main():
    global topics_checked
    files = sorted(glob.glob(DATA_GLOB, recursive=True))
    if not files:
        print("No genmath data files found.", file=sys.stderr)
        sys.exit(1)

    published = []
    for path in files:
        with open(path, "r", encoding="utf-8") as fh:
            topic = json.load(fh)
        check_render_safety(os.path.relpath(path, ROOT), topic)
        if topic.get("status") != "published":
            continue
        published.append(topic.get("slug", os.path.basename(path)))
        topics_checked += 1
        slug = topic.get("slug", "<no-slug>")

        # Titles are rendered as PLAIN TEXT — the course hub, the unit page's
        # lesson list and the catalog all interpolate them directly, never
        # through MathText. A title carrying $...$ therefore shows the student
        # literal dollar signs and a raw LaTeX macro. (Two shipped that way in
        # the IB AI SL course and were caught only by reading production HTML.)
        if "$" in topic.get("title", ""):
            failures.append(f"{slug}: unit title contains math delimiters — titles render as plain text: {topic['title']!r}")
        for lesson in topic.get("lessons", []):
            if "$" in lesson.get("title", ""):
                failures.append(
                    f"{slug} / {lesson.get('slug')}: lesson title contains math delimiters — "
                    f"titles render as plain text, not through MathText: {lesson['title']!r}"
                )

        for lesson in topic.get("lessons", []):
            lslug = lesson.get("slug", "<no-lesson-slug>")
            cc = lesson.get("concreteComparison", "")
            if not isinstance(cc, str) or cc.strip() == "":
                failures.append(f"{slug} / {lslug}: concreteComparison is required and must not be empty")
            for ex in lesson.get("workedExamples", []):
                check_problem(slug, f"{lslug}:worked", ex)
            for ex in lesson.get("tryIt", []):
                check_problem(slug, f"{lslug}:tryIt", ex)
            steps = (lesson.get("interactive") or {}).get("steps", [])
            for s in steps:
                k = s.get("kind")
                check_widget_config(slug, lslug, s)
                if k == "tapQuestion":
                    check_tap_question(slug, f"{lslug}:interactive", s)
                elif k == "workedSet":
                    for j, ex in enumerate(s.get("examples", [])):
                        check_inline(slug, f"{lslug}:workedSet[{j}]", ex)
                elif k == "tryItSet":
                    for j, p in enumerate(s.get("problems", [])):
                        check_tap_question(slug, f"{lslug}:tryItSet[{j}]", p)
            if steps:
                # A lesson page renders ONLY the interactive player, so a
                # player without teaching steps IS the lesson a student sees —
                # quiz-only step lists shipped as "courses" once (IM3 units
                # 2–6, caught by the owner 2026-08-01) and must never again.
                # Teaching = an instructional step kind, or a widget step
                # carrying `teach` prose. Quiz steps don't count.
                TEACHING_KINDS = {
                    "teach", "concept", "worked", "workedSet", "tryIt",
                    "tryItSet", "tip", "funFact", "recap", "notationToggle",
                }
                n_teaching = sum(
                    1 for s in steps
                    if s.get("kind") in TEACHING_KINDS or s.get("teach")
                )
                if n_teaching < 2:
                    failures.append(
                        f"{slug} / {lslug}: interactive player has {n_teaching} teaching step(s) "
                        f"(kinds: {[s.get('kind') for s in steps]}) — a lesson must teach, "
                        f"not just quiz; add teach/worked/tryIt/recap steps"
                    )
                # worked/tryIt steps reference problems by id; a broken
                # reference renders as a missing screen, invisibly.
                ids_w = {p.get("id") for p in lesson.get("workedExamples", [])}
                ids_t = {p.get("id") for p in lesson.get("tryIt", [])}
                for s in steps:
                    if s.get("kind") == "worked" and s.get("problemId") not in ids_w:
                        failures.append(f"{slug} / {lslug}: worked step references unknown problemId {s.get('problemId')!r}")
                    if s.get("kind") == "tryIt" and s.get("problemId") not in ids_t:
                        failures.append(f"{slug} / {lslug}: tryIt step references unknown problemId {s.get('problemId')!r}")
                # The mirror-image defect: the lesson page renders ONLY the
                # interactive steps, so an authored problem that no step
                # references is invisible content — written, verified, and
                # never shown (60 shipped that way until 2026-08-02). In the
                # reference idiom (worked/tryIt steps carrying problemIds)
                # every authored problem must be referenced. Lessons built in
                # the embedded-set idiom (workedSet/tryItSet carry their own
                # items) are a different design and are exempt.
                referenced = {
                    s.get("problemId") for s in steps
                    if s.get("kind") in ("worked", "tryIt")
                }
                if referenced:
                    for group, ids in (("workedExamples", ids_w), ("tryIt", ids_t)):
                        for pid in sorted(ids - referenced):
                            failures.append(
                                f"{slug} / {lslug}: {group} problem {pid!r} is never "
                                f"referenced by any step — it renders nowhere; add a "
                                f"worked/tryIt step for it (or delete the problem)"
                            )

        for ex in topic.get("practice", []):
            check_problem(slug, "practice", ex)
        for ex in topic.get("testYourself", []):
            check_problem(slug, "testYourself", ex)

    if topics_checked == 0:
        print("verify:genmath — no published topics found (nothing gated).")
        sys.exit(0)

    print(f"verify:genmath — published topics: {', '.join(published)}")
    print(
        f"  problems: {problems_checked}   tap-questions: {tapq_checked}   "
        f"sympy checks run: {checks_run}   render-safety strings: {render_strings_checked}   "
        f"widget configs: {widget_steps_checked}"
    )

    if failures:
        print(f"\nFAILED — {len(failures)} issue(s):", file=sys.stderr)
        for f in failures:
            print(f"  ✗ {f}", file=sys.stderr)
        sys.exit(1)

    print("  ✓ all checks passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
