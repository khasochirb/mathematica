#!/usr/bin/env python3
"""
Practice-test verification gate (ЭЕШ / SAT / IB).

Companion to the authoring skills in .claude/skills/practice-test-authoring/
(core manual) + esh-practice-test / sat-practice-test / ib-practice-test.
Run this on every test JSON before commit:

    python3 scripts/verify-practice-test.py data/questions/2026a.json \
        data/questions/2026a-section2.json --strict
    python3 scripts/verify-practice-test.py --hub sat data/sat/sat-practice-1.json
    python3 scripts/verify-practice-test.py --all-esh          # sweep existing bank
    python3 scripts/verify-practice-test.py --strip <file>     # blind copy for
                                                               # adversarial re-solve

Hub is auto-detected from the file path/shape; override with --hub esh|sat|ib.

Default mode: structural errors fail; blueprint/style deviations warn
(the pre-existing bank must keep passing). --strict promotes the
new-test requirements to errors: verify[] present on every question,
positional difficulty, exact option letters, answer-key balance.
Every check mirrors a rule in the skill docs — if you change a rule
there, change it here.
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PUBLIC = REPO / "public"

ERRORS: list[str] = []
WARNINGS: list[str] = []

# Real defects in shipped legacy data that must NOT be patched without
# textbook verification (memory/practice-test-audit.md). Downgraded to
# warnings so the bank sweep stays green; remove entries once fixed.
KNOWN_ISSUES = {
    # Audit open item: "Test-3B-Q20 (option D) — NOT YET verified against
    # textbook". Options C and D are identical in the JSON.
    "test3b.json[Test-3B-Q20]: duplicate option text",
}


def err(msg: str) -> None:
    if msg in KNOWN_ISSUES:
        WARNINGS.append(f"(known issue) {msg}")
    else:
        ERRORS.append(msg)


def warn(msg: str, strict: bool = False) -> None:
    (ERRORS if strict else WARNINGS).append(msg)


# ─── shared text checks ────────────────────────────────────────────────

# Exact replica of the splitter in components/esh/MathText.tsx. After the
# split, matched math/bold groups sit at odd indices; any $ or ** left in
# an even-index (plain text) segment is a delimiter the renderer would
# print literally — i.e. unclosed or empty math.
MATH_SPLIT = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)")


def check_math_text(label: str, text: str) -> None:
    """Delimiter sanity per components/esh/MathText.tsx."""
    if not isinstance(text, str):
        err(f"{label}: not a string")
        return
    stripped = text.replace("\\$", "")  # literal-dollar escape
    parts = MATH_SPLIT.split(stripped)
    for i, part in enumerate(parts):
        if i % 2 == 1:
            continue
        if "$" in part:
            err(f"{label}: stray/unmatched $ would render literally: "
                f"…{part.strip()[:60]!r}…")
        if "**" in part:
            err(f"{label}: stray/unmatched ** would render literally: "
                f"…{part.strip()[:60]!r}…")


def check_figure(label: str, fig: dict, mn_required: bool = True) -> None:
    for k in ("src", "width", "height"):
        if k not in fig:
            err(f"{label}: figure missing {k!r}")
            return
    src = fig["src"]
    if not src.startswith("/"):
        err(f"{label}: figure.src must be public-root-relative: {src!r}")
    elif not (PUBLIC / src.lstrip("/")).is_file():
        err(f"{label}: figure file not on disk: public{src}")
    if not (isinstance(fig["width"], int) and fig["width"] > 0
            and isinstance(fig["height"], int) and fig["height"] > 0):
        err(f"{label}: figure width/height must be positive ints")
    if mn_required and not fig.get("alt_mn"):
        err(f"{label}: figure.alt_mn missing/empty")
    if not fig.get("alt_en"):
        err(f"{label}: figure.alt_en missing/empty")


def check_verify(label: str, entries, strict: bool) -> None:
    if not entries:
        if strict:
            err(f"{label}: verify[] missing/empty (required with --strict)")
        return
    try:
        from sympy import sympify  # deferred: sweep mode may not need it
    except ImportError:
        warn(f"{label}: sympy unavailable — verify[] not evaluated", strict)
        return
    for expr in entries:
        try:
            result = sympify(expr)
        except Exception as e:  # noqa: BLE001
            err(f"{label}: verify does not sympify: {expr!r} ({e})")
            continue
        # sympify returns sympy's BooleanTrue (not the Python singleton)
        # for auto-evaluated relations like Eq(4 - 1, 3).
        if result is not True and result != True:  # noqa: E712
            err(f"{label}: verify not True: {expr!r} -> {result}")


def letter_balance(label: str, answers: list[str], letters: str, strict: bool) -> None:
    n = len(answers)
    if n < 20:
        return
    hist = Counter(answers)
    lo, hi = n // len(letters) - 3, n // len(letters) + 4
    for letter in letters:
        c = hist.get(letter, 0)
        if not lo <= c <= hi:
            warn(f"{label}: answer letter {letter} appears {c}× of {n} "
                 f"(expected {lo}–{hi})", strict)
    run = 1
    for a, b in zip(answers, answers[1:]):
        run = run + 1 if a == b else 1
        if run == 4:
            warn(f"{label}: run of 4+ consecutive answer letter {b!r}", strict)


# ─── ЭЕШ Section 1 ─────────────────────────────────────────────────────

# Hard fields break the product if absent; soft fields are metadata some
# legacy files miss (warn by default, error with --strict).
ESH_S1_HARD = ("source", "questionNumber", "body", "options", "answer",
               "solution")
ESH_S1_SOFT = ("testNumber", "testVariant", "type", "topic", "subtopic",
               "difficulty")


def positional_difficulty(qnum: int) -> int:
    return 1 if qnum <= 12 else 2 if qnum <= 24 else 3


def check_esh_s1(path: Path, data, strict: bool) -> None:
    if not isinstance(data, list):
        err(f"{path.name}: expected a JSON array of questions")
        return
    name = path.name
    answers: list[str] = []
    sources = Counter()
    for i, q in enumerate(data):
        label = f"{name}[{q.get('source', i)}]"
        for k in ESH_S1_HARD:
            if k not in q or q[k] in ("", None):
                err(f"{label}: missing/empty {k!r}")
        for k in ESH_S1_SOFT:
            if k not in q or q[k] in ("", None):
                warn(f"{label}: missing/empty {k!r}", strict)
        opts = q.get("options") or {}
        if not isinstance(opts, dict) or not opts:
            err(f"{label}: options must be a non-empty object")
            opts = {}
        bad_keys = [k for k in opts if k not in "ABCDE"]
        if bad_keys:
            err(f"{label}: non-A–E option keys {bad_keys}")
        if strict and sorted(opts) != list("ABCDE"):
            err(f"{label}: options must be exactly A–E (got {sorted(opts)})")
        vals = list(opts.values())
        if len(set(vals)) != len(vals):
            err(f"{label}: duplicate option text")
        ans = q.get("answer")
        if ans not in opts:
            err(f"{label}: answer {ans!r} not an option key")
        else:
            answers.append(ans)
        for field in ("body", "solution"):
            if isinstance(q.get(field), str):
                check_math_text(f"{label}.{field}", q[field])
        for k, v in opts.items():
            check_math_text(f"{label}.options.{k}", v)
        qnum = q.get("questionNumber")
        if isinstance(qnum, int) and q.get("difficulty") != positional_difficulty(qnum):
            warn(f"{label}: difficulty {q.get('difficulty')} breaks the "
                 f"positional convention (Q{qnum} → {positional_difficulty(qnum)})",
                 strict)
        tier = q.get("difficulty_tier")
        tier_map = {1: "easy", 2: "medium", 3: "hard"}
        if tier and q.get("difficulty") in tier_map and tier != tier_map[q["difficulty"]]:
            err(f"{label}: difficulty_tier {tier!r} ≠ map({q['difficulty']})")
        if q.get("figure"):
            check_figure(label, q["figure"])
        check_verify(label, q.get("verify"), strict)
        if q.get("source"):
            sources[q["source"]] += 1
    for src, c in sources.items():
        if c > 1:
            err(f"{name}: duplicate source {src!r} ×{c}")
    if strict and len(data) != 36:
        err(f"{name}: Section 1 must have 36 questions (got {len(data)})")
    letter_balance(name, answers, "ABCDE", strict)


# ─── ЭЕШ Section 2 ─────────────────────────────────────────────────────

ESH_S2_REQUIRED = ("source", "test", "section", "problem", "subproblem",
                   "type", "context", "instruction", "slots", "points",
                   "solution")
SLOT_RE = re.compile(r"^(\d*)([A-Za-z]+)$")
PLACEHOLDER_RE = re.compile(r"\[([A-Za-z0-9]+)\]")


def check_esh_s2(path: Path, data, strict: bool) -> None:
    if not isinstance(data, list):
        err(f"{path.name}: expected a JSON array of Section 2 items")
        return
    name = path.name
    by_problem: dict[str, list[dict]] = defaultdict(list)
    for i, item in enumerate(data):
        label = f"{name}[{item.get('source', i)}]"
        for k in ESH_S2_REQUIRED:
            if k not in item or item[k] in ("", None):
                err(f"{label}: missing/empty {k!r}")
        if item.get("section") != 2:
            err(f"{label}: section must be 2")
        if item.get("problem") not in ("2.1", "2.2", "2.3", "2.4"):
            err(f"{label}: bad problem id {item.get('problem')!r}")
        slots = item.get("slots") or []
        seen_letters: set[str] = set()
        for s in slots:
            slabel = s.get("label", "")
            m = SLOT_RE.match(slabel)
            if not m:
                err(f"{label}: slot label {slabel!r} breaks ^digits+letters$ grammar")
                continue
            prefix, var = m.group(1), m.group(2)
            ansv = str(s.get("answer", ""))
            if not ansv.isdigit():
                err(f"{label}: slot {slabel!r} answer {ansv!r} must be a "
                    f"non-negative digit string")
            elif len(ansv) != len(prefix) + len(var):
                err(f"{label}: slot {slabel!r} answer {ansv!r} length ≠ "
                    f"prefix+letters ({len(prefix)}+{len(var)})")
            elif prefix and not ansv.startswith(prefix):
                err(f"{label}: slot {slabel!r} answer {ansv!r} does not start "
                    f"with literal prefix {prefix!r}")
            if s.get("type") not in ("digit", "integer"):
                err(f"{label}: slot {slabel!r} type must be digit|integer")
            dup = seen_letters & set(var)
            if dup:
                err(f"{label}: letters {sorted(dup)} reused across slots")
            seen_letters |= set(var)
        # Every slot must be enterable: its label appears as an [x]
        # placeholder in the instruction. The reverse is NOT required —
        # shipped papers repeat placeholders and re-reference labels
        # answered in an earlier subproblem.
        placeholders = set(PLACEHOLDER_RE.findall(item.get("instruction", "")))
        for s in slots:
            if s.get("label") and s["label"] not in placeholders:
                err(f"{label}: slot {s['label']!r} has no [{s['label']}] "
                    f"placeholder in the instruction")
        for field in ("context", "instruction", "solution"):
            if isinstance(item.get(field), str):
                check_math_text(f"{label}.{field}", item[field])
        if item.get("figure"):
            check_figure(label, item["figure"])
            if item.get("subproblem") != 1:
                warn(f"{label}: figure on subproblem {item.get('subproblem')} "
                     f"(convention: subproblem 1 only)")
        check_verify(label, item.get("verify"), strict)
        if isinstance(item.get("problem"), str):
            by_problem[item["problem"]].append(item)

    total = 0
    for prob, items in sorted(by_problem.items()):
        items.sort(key=lambda x: x.get("subproblem", 0))
        subs = [x.get("subproblem") for x in items]
        if subs != list(range(1, len(items) + 1)):
            err(f"{name} {prob}: subproblems not consecutive from 1: {subs}")
        pts = sum(x.get("points", 0) for x in items)
        total += pts
        if pts != 7:
            err(f"{name} {prob}: points sum {pts} ≠ 7")
        contexts = {x.get("context") for x in items}
        if len(contexts) > 1:
            warn(f"{name} {prob}: context differs across subproblems", strict)
        topics = {x.get("topic") for x in items}
        if len(topics) > 1:
            err(f"{name} {prob}: topic differs across subproblems")
    if len(by_problem) != 4:
        err(f"{name}: expected problems 2.1–2.4 (got {sorted(by_problem)})")
    elif total != 28:
        err(f"{name}: Section 2 total {total} ≠ 28")


# ─── SAT ───────────────────────────────────────────────────────────────

SAT_DOMAINS = {"algebra", "advanced_math", "psda", "geometry_trig"}
SAT_DIFF = {"easy", "medium", "hard"}


def check_sat_question(name: str, q: dict, module_key: str, strict: bool) -> str | None:
    label = f"{name}.{module_key}[{q.get('source', '?')}]"
    for k in ("source", "questionNumber", "format", "domain", "skill_tag",
              "difficulty", "body", "solution"):
        if k not in q or q[k] in ("", None):
            err(f"{label}: missing/empty {k!r}")
    if q.get("domain") not in SAT_DOMAINS:
        err(f"{label}: domain {q.get('domain')!r} not in {sorted(SAT_DOMAINS)}")
    if q.get("difficulty") not in SAT_DIFF:
        err(f"{label}: difficulty must be easy|medium|hard")
    fmt = q.get("format")
    answer_letter = None
    if fmt == "mcq":
        opts = q.get("options") or {}
        if sorted(opts) != list("ABCD"):
            err(f"{label}: MCQ options must be exactly A–D (got {sorted(opts)})")
        if len(set(opts.values())) != len(opts):
            err(f"{label}: duplicate option text")
        if q.get("answer") not in opts:
            err(f"{label}: answer {q.get('answer')!r} not an option key")
        else:
            answer_letter = q["answer"]
        nums = []
        for v in opts.values():
            m = re.fullmatch(r"\$?(-?\d+(?:\.\d+)?)\$?", str(v).strip())
            if not m:
                nums = None
                break
            nums.append(float(m.group(1)))
        if nums and nums != sorted(nums):
            warn(f"{label}: numeric options not in ascending order", strict)
        for k, v in opts.items():
            check_math_text(f"{label}.options.{k}", v)
    elif fmt == "spr":
        acc = q.get("acceptedAnswers")
        if not acc or not isinstance(acc, list):
            err(f"{label}: SPR needs non-empty acceptedAnswers[]")
        else:
            for a in acc:
                a = str(a)
                limit = 6 if a.startswith("-") else 5
                if len(a) > limit:
                    err(f"{label}: SPR answer {a!r} exceeds {limit} chars")
                if not re.fullmatch(r"-?(\d+(\.\d*)?|\.\d+|\d+/\d+)", a):
                    err(f"{label}: SPR answer {a!r} not digit/decimal/fraction")
    else:
        err(f"{label}: format must be mcq|spr")
    for field in ("body", "solution"):
        if isinstance(q.get(field), str):
            check_math_text(f"{label}.{field}", q[field])
    if q.get("figure"):
        check_figure(label, q["figure"], mn_required=False)
    check_verify(label, q.get("verify"), strict)
    return answer_letter


def check_sat(path: Path, data, strict: bool) -> None:
    name = path.name
    if not isinstance(data, dict) or "meta" not in data:
        err(f"{name}: SAT test must be an object with meta + modules")
        return
    meta = data["meta"]
    for k in ("testId", "label", "minutesPerModule", "module2Threshold"):
        if k not in meta:
            err(f"{name}: meta missing {k!r}")
    for module_key in ("module1", "module2Easy", "module2Hard"):
        qs = data.get(module_key)
        if not isinstance(qs, list):
            err(f"{name}: missing module {module_key!r}")
            continue
        if len(qs) != 22:
            err(f"{name}.{module_key}: must have 22 questions (got {len(qs)})")
        answers = [a for q in qs
                   if (a := check_sat_question(name, q, module_key, strict))]
        letter_balance(f"{name}.{module_key}", answers, "ABCD", strict)
        spr = sum(1 for q in qs if q.get("format") == "spr")
        if not 4 <= spr <= 7:
            warn(f"{name}.{module_key}: {spr} SPR questions (expect 5–6)", strict)
        dom = Counter(q.get("domain") for q in qs)
        for d, (lo, hi) in {"algebra": (6, 8), "advanced_math": (6, 8),
                            "psda": (2, 4), "geometry_trig": (2, 4)}.items():
            if not lo <= dom.get(d, 0) <= hi:
                warn(f"{name}.{module_key}: domain {d} count {dom.get(d, 0)} "
                     f"outside {lo}–{hi}", strict)


# ─── IB ────────────────────────────────────────────────────────────────

IB_TOPICS = {"number_algebra", "functions", "geometry_trig",
             "stats_probability", "calculus"}
IB_MARK_RE = re.compile(r"^\(?(M\d|A\d|R\d|AG|FT)\)?$")
IB_PAPER_TOTALS = {("sl", 1): 80, ("sl", 2): 80,
                   ("hl", 1): 110, ("hl", 2): 110, ("hl", 3): 55}


def check_ib(path: Path, data, strict: bool) -> None:
    name = path.name
    if not isinstance(data, dict) or "meta" not in data or "questions" not in data:
        err(f"{name}: IB paper must be an object with meta + questions")
        return
    meta = data["meta"]
    for k in ("course", "level", "paper", "testId", "label", "timeMinutes",
              "totalMarks", "calculator"):
        if k not in meta:
            err(f"{name}: meta missing {k!r}")
    expected = IB_PAPER_TOTALS.get((meta.get("level"), meta.get("paper")))
    if expected and meta.get("totalMarks") != expected:
        err(f"{name}: totalMarks {meta.get('totalMarks')} ≠ {expected} for "
            f"{meta.get('level')} paper {meta.get('paper')}")
    if meta.get("course") == "aa" and meta.get("paper") == 1 and meta.get("calculator"):
        err(f"{name}: AA Paper 1 must be calculator: false")
    grand = 0
    for q in data.get("questions", []):
        qlabel = f"{name}[Q{q.get('number', '?')}]"
        if q.get("topic") not in IB_TOPICS:
            err(f"{qlabel}: topic {q.get('topic')!r} not in {sorted(IB_TOPICS)}")
        parts = q.get("parts") or []
        if not parts:
            err(f"{qlabel}: no parts")
            continue
        part_sum = 0
        for p in parts:
            plabel = f"{qlabel}({p.get('label', '?')})"
            for k in ("label", "body", "marks", "markscheme", "answer", "solution"):
                if k not in p or p[k] in ("", None):
                    err(f"{plabel}: missing/empty {k!r}")
            marks = p.get("marks", 0)
            part_sum += marks
            ms = p.get("markscheme") or []
            if len(ms) != marks:
                err(f"{plabel}: markscheme has {len(ms)} marks, part is [{marks}]")
            for entry in ms:
                if not IB_MARK_RE.match(str(entry.get("mark", ""))):
                    err(f"{plabel}: illegal mark code {entry.get('mark')!r}")
            body = p.get("body", "")
            if isinstance(body, str):
                check_math_text(f"{plabel}.body", body)
                if re.search(r"\bshow that\b", body, re.I):
                    if not ms or ms[-1].get("mark") != "AG":
                        err(f"{plabel}: 'Show that' part must end its "
                            f"markscheme with AG")
            if isinstance(p.get("solution"), str):
                check_math_text(f"{plabel}.solution", p["solution"])
            check_verify(plabel, p.get("verify"), strict)
        if part_sum != q.get("maximumMark"):
            err(f"{qlabel}: parts sum {part_sum} ≠ maximumMark "
                f"{q.get('maximumMark')}")
        grand += q.get("maximumMark", 0)
        if q.get("figure"):
            check_figure(qlabel, q["figure"], mn_required=False)
    if meta.get("totalMarks") and grand != meta["totalMarks"]:
        err(f"{name}: question marks sum {grand} ≠ meta.totalMarks "
            f"{meta['totalMarks']}")


# ─── strip mode (adversarial re-solve input) ──────────────────────────

def strip_file(path: Path) -> None:
    data = json.loads(path.read_text())
    hub = detect_hub(path, data)
    if hub == "esh-s1":
        out = [{k: q[k] for k in ("source", "questionNumber", "body", "options")
                if k in q} | ({"figure": q["figure"]} if q.get("figure") else {})
               for q in data]
    elif hub == "esh-s2":
        out = [{k: it[k] for k in ("source", "problem", "subproblem", "context",
                                   "instruction") if k in it}
               | {"slots": [{"label": s["label"], "type": s["type"]}
                            for s in it.get("slots", [])]}
               for it in data]
    elif hub == "sat":
        def strip_q(q):
            keep = {k: q[k] for k in ("source", "questionNumber", "format",
                                      "body", "options") if k in q}
            if q.get("figure"):
                keep["figure"] = q["figure"]
            return keep
        out = {m: [strip_q(q) for q in data.get(m, [])]
               for m in ("module1", "module2Easy", "module2Hard")}
    else:  # ib
        out = {"meta": data.get("meta"), "questions": [
            {"number": q.get("number"), "maximumMark": q.get("maximumMark"),
             "contextIntro": q.get("contextIntro"),
             "parts": [{"label": p.get("label"), "body": p.get("body"),
                        "marks": p.get("marks")} for p in q.get("parts", [])]}
            for q in data.get("questions", [])]}
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()


# ─── dispatch ──────────────────────────────────────────────────────────

def detect_hub(path: Path, data) -> str:
    p = str(path)
    if "/data/sat/" in p or "sat" in path.stem.lower() and isinstance(data, dict) and "module1" in data:
        return "sat"
    if "/data/ib/" in p or (isinstance(data, dict) and
                            isinstance(data.get("meta"), dict) and
                            "paper" in data["meta"]):
        return "ib"
    if "section2" in path.name:
        return "esh-s2"
    return "esh-s1"


def check_file(path: Path, strict: bool, hub_override: str | None) -> None:
    try:
        data = json.loads(path.read_text())
    except Exception as e:  # noqa: BLE001
        err(f"{path.name}: JSON parse failed: {e}")
        return
    hub = hub_override or detect_hub(path, data)
    if hub == "sat":
        check_sat(path, data, strict)
    elif hub == "ib":
        check_ib(path, data, strict)
    elif hub == "esh-s2" or (hub == "esh" and "section2" in path.name):
        check_esh_s2(path, data, strict)
    else:
        check_esh_s1(path, data, strict)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--hub", choices=["esh", "sat", "ib"])
    ap.add_argument("--strict", action="store_true",
                    help="promote new-test requirements to errors")
    ap.add_argument("--all-esh", action="store_true",
                    help="sweep every file in data/questions/")
    ap.add_argument("--strip", action="store_true",
                    help="emit a blind copy (no answers/solutions) to stdout")
    args = ap.parse_args()

    files = list(args.files)
    if args.all_esh:
        files += sorted((REPO / "data" / "questions").glob("*.json"))
    if not files:
        ap.error("no files given (or use --all-esh)")

    if args.strip:
        for f in files:
            strip_file(f)
        return

    for f in files:
        check_file(f, args.strict, args.hub)

    for w in WARNINGS:
        print(f"WARN  {w}")
    for e in ERRORS:
        print(f"ERROR {e}")
    print(f"\n{len(files)} file(s): {len(ERRORS)} error(s), "
          f"{len(WARNINGS)} warning(s)")
    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
