#!/usr/bin/env python3
"""Shared authoring helpers for the Integrated Mathematics courses (IM1-IM3).

Every unit builder imports these so the schema, the sympy gate and the JSON
writing behave identically across the three courses. Nothing here is
course-specific: the builders supply the mathematics, this file supplies the
scaffolding and refuses to write a file whose checks do not hold.

The contract mirrors scripts/verify-genmath.py: every workedExample, tryIt,
practice, testYourself and tapQuestion carries a non-empty `check` list, and
every entry must sympify to True. Asserting here as well as in the gate means
a broken problem crashes at authoring time, before it can reach a JSON file.
"""
import json
import os
import re
import sys

from sympy import sympify  # noqa: F401  (re-exported for builders)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The exact splitter from components/esh/MathText.tsx. The alternation is
# leftmost-first, so a **bold** run that contains inline math is matched AS
# BOLD and the math inside it never reaches KaTeX — it renders as literal
# dollar signs in production. The pattern is copied verbatim rather than
# approximated, because an approximation would flag different strings than the
# renderer actually breaks on.
MATHTEXT_SPLIT = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)")


# MathText protects escaped dollars (\$) with a sentinel before splitting, and
# renders bold content as plain text. So a LONE currency $ inside bold renders
# fine; the defect is a bold run containing a COMPLETE $...$ pair, whose math
# then shows up as literal dollar signs.
DOLLAR_SENTINEL = "\x00"
MATH_PAIR = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")


def find_math_in_bold(text):
    """Bold runs swallowing a full math pair — they render as literal dollars."""
    protected = text.replace("\\$", DOLLAR_SENTINEL)
    return [
        t.replace(DOLLAR_SENTINEL, "\\$")
        for t in MATHTEXT_SPLIT.findall(protected)
        if t.startswith("**") and MATH_PAIR.search(t[2:-2])
    ]


# Characters KaTeX has no glyph for. Inside math they produce a warning and a
# blank box rather than an error node, so the render gate reports the file
# clean and the defect ships. The tugrik sign and the ballot cross are the two
# that occur in practice; the check mark ✓ HAS KaTeX metrics and renders fine,
# so it is deliberately not listed.
UNRENDERABLE_IN_MATH = "₮✗"


def find_unrenderable_math(text):
    """Math segments containing a character KaTeX cannot draw."""
    bad = []
    for token in MATHTEXT_SPLIT.findall(text):
        if token.startswith("$") and any(c in token for c in UNRENDERABLE_IN_MATH):
            bad.append(token)
    return bad


# The interactive-widget config contract lives in scripts/widget_contract.py,
# DERIVED by parsing lib/genmath-interactive.ts rather than transcribed here.
# A widget whose config is missing a required key still type-checks (the JSON
# is imported and cast, so tsc never sees it) and still renders — it just
# silently falls back to a default and shows the wrong thing. That failure mode
# is invisible to every other gate in the chain, which is why it is checked at
# build time as well as at gate time.
#
# This used to be a hand-written allowlist, and it had drifted: it rejected
# `coef` on balanceScale (declared on the interface since the component was
# written) and knew nothing of about half the widget kinds, which meant an
# author reaching for a new widget hit a spurious "unknown widget kind" error.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from widget_contract import config_problems, load_widget_contract  # noqa: E402

WIDGET_CONTRACT = load_widget_contract()

# Step kinds that carry no `config` at all — prose, problem references and
# tapQuestion (which carries its options inline, not in a config object).
WIDGET_EXEMPT_KINDS = {"teach", "tip", "funFact", "recap", "worked", "tryIt", "tapQuestion"}

# Every config-carrying kind the components know about, straight from the
# discriminated union. A kind that is neither exempt nor here is a typo.
KNOWN_WIDGET_KINDS = set(WIDGET_CONTRACT) | WIDGET_EXEMPT_KINDS | {
    "concept", "workedSet", "tryItSet",
}


def check_widget_configs(lessons):
    """Every widget-config defect in the unit, reported in one pass."""
    problems = []
    for les in lessons:
        for i, step in enumerate(les["interactive"]["steps"]):
            kind = step["kind"]
            where = f"{les['slug']}.steps[{i}]"
            if kind not in KNOWN_WIDGET_KINDS:
                problems.append(
                    f"{where}: unknown step kind {kind!r} — check the discriminated "
                    f"union at the bottom of lib/genmath-interactive.ts"
                )
                continue
            for msg in config_problems(WIDGET_CONTRACT, kind, step.get("config")):
                problems.append(f"{where} ({kind}): {msg}")
    return problems


def _walk_strings(node, path, visit):
    if isinstance(node, str):
        visit(path, node)
    elif isinstance(node, dict):
        for key, value in node.items():
            _walk_strings(value, f"{path}.{key}", visit)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            _walk_strings(value, f"{path}[{i}]", visit)


def out_path(course, unit_slug):
    """data/genmath/<course>/<unit>.json — e.g. ("integrated-1", "quantities")."""
    return os.path.join(ROOT, "data", "genmath", course, f"{unit_slug}.json")


def assert_checks(where, checks):
    """Every check must sympify to True. Anything else stops the build."""
    if not checks:
        raise SystemExit(f"{where}: empty check list")
    for expr in checks:
        try:
            value = sympify(expr)
        except Exception as exc:  # noqa: BLE001 — surface the raw sympy error
            raise SystemExit(f"{where}: check does not sympify: {expr!r} ({exc})")
        # Mirror scripts/verify-genmath.py exactly: sympy returns BooleanTrue,
        # not Python True, and an undecidable relational raises on bool().
        #
        # The result must BE a boolean, not merely be truthy. A stray trailing
        # comma turns "Eq(1, 2)," into the 1-tuple (False,), which is truthy
        # and would otherwise sail through — a check that verifies nothing.
        if isinstance(value, (tuple, list, set, dict, str)):
            raise SystemExit(
                f"{where}: check is a {type(value).__name__}, not a true/false "
                f"claim (a stray comma does this): {expr!r} -> {value!r}"
            )
        try:
            ok = bool(value) is True
        except TypeError:
            ok = False
        if not ok:
            raise SystemExit(f"{where}: check is not True: {expr!r} -> {value!r}")


def problem(pid, statement, solution, check, **extra):
    """A worked example / practice / test problem, verified on construction."""
    assert_checks(pid, check)
    return {"id": pid, "statement": statement, "solution": solution, "check": check, **extra}


def tap(title, prompt, options, correct_index, explanation, check, **extra):
    """A tapQuestion step. The correct option is verified, not asserted."""
    if not 0 <= correct_index < len(options):
        raise SystemExit(f"{title}: correctIndex {correct_index} out of range")
    if len(set(options)) != len(options):
        raise SystemExit(f"{title}: duplicate option text")
    assert_checks(title, check)
    return {
        "kind": "tapQuestion",
        "title": title,
        "prompt": prompt,
        "options": options,
        "correctIndex": correct_index,
        "explanation": explanation,
        "check": check,
        **extra,
    }


def lesson(slug, title, concrete, objective, concept, key_idea, facts, worked, mistakes, try_it, steps):
    """Assemble a lesson, checking the pieces the gate will later re-check."""
    if not concrete.strip():
        raise SystemExit(f"{slug}: concreteComparison is required")
    if not worked:
        raise SystemExit(f"{slug}: at least one worked example is required")
    if not try_it:
        raise SystemExit(f"{slug}: at least one tryIt is required")
    return {
        "slug": slug,
        "title": title,
        "concreteComparison": concrete,
        "objective": objective,
        "concept": concept,
        "keyIdea": key_idea,
        "facts": facts,
        "workedExamples": worked,
        "commonMistakes": mistakes,
        "tryIt": try_it,
        "interactive": {"steps": steps},
    }


def mistake(text, correction):
    return {"text": text, "correction": correction, "authored": True}


def fact(title, latex, explanation):
    return {"title": title, "latex": latex, "explanation": explanation}


def write_unit(course, slug, title, unit_number, blurb, builds_on, lessons, practice, test):
    """Write the unit JSON, after a final sweep over every check in the file."""
    for p in practice:
        assert_checks(p["id"], p.get("check"))
    for p in test:
        assert_checks(p["id"], p.get("check"))

    widget_problems = check_widget_configs(lessons)
    if widget_problems:
        lines = "\n".join(f"  {p}" for p in widget_problems)
        raise SystemExit(
            f"{len(widget_problems)} interactive step(s) have an invalid config. These "
            f"render silently wrong rather than failing, so they are caught here:\n{lines}"
        )

    n_checks = 0
    for les in lessons:
        for group in ("workedExamples", "tryIt"):
            for p in les[group]:
                n_checks += len(p["check"])
        for step in les["interactive"]["steps"]:
            if step["kind"] == "tapQuestion":
                n_checks += len(step["check"])
    n_checks += sum(len(p["check"]) for p in practice)
    n_checks += sum(len(p["check"]) for p in test)

    data = {
        "slug": slug,
        "title": title,
        "unit": unit_number,
        "status": "published",
        "blurb": blurb,
        "buildsOn": builds_on,
        "lessons": lessons,
        "practice": practice,
        "testYourself": test,
    }

    # Every rendered string in the file, checked before it is written. All
    # violations are reported together — fixing them one crash at a time is
    # needlessly slow when a lesson has a dozen.
    bold_math = []
    bad_glyphs = []

    def collect(path, text):
        for token in find_math_in_bold(text):
            bold_math.append((path, token))
        for token in find_unrenderable_math(text):
            bad_glyphs.append((path, token))

    _walk_strings(data, slug, collect)
    if bold_math:
        lines = "\n".join(f"  {path}: {token!r}" for path, token in bold_math)
        raise SystemExit(
            f"{len(bold_math)} bold run(s) contain inline math, which MathText "
            f"renders as literal dollar signs. Rewrite the bold text without "
            f"math:\n{lines}"
        )
    if bad_glyphs:
        lines = "\n".join(f"  {path}: {token!r}" for path, token in bad_glyphs)
        raise SystemExit(
            f"{len(bad_glyphs)} math segment(s) contain a character KaTeX cannot "
            f"render. Move it into the surrounding prose:\n{lines}"
        )

    path = out_path(course, slug)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(
        f"wrote {os.path.relpath(path, ROOT)} — {len(lessons)} lessons, "
        f"{len(practice)} practice, {len(test)} test, {n_checks} sympy checks"
    )
