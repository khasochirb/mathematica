#!/usr/bin/env python3
"""Course-exam integrity gate.

For every exam in data/course-exams/*.json asserts:
  - meta has examId / course / label / minutes / totalQuestions, and the
    declared totals match the actual question list;
  - EVERY unit of the course spine appears — an exam that silently skips a
    unit reports a score the student cannot act on;
  - every question has a unique id, exactly 4 DISTINCT options, a valid
    correctIndex, a non-empty explanation and a NON-EMPTY check[];
  - every check sympifies to True;
  - the three exams of a course are pairwise DISJOINT, so a student can sit
    all of them without meeting a repeat;
  - render safety, same three classes the bank and genmath gates enforce.

Run: npm run verify:exams
"""
import glob
import json
import os
import re
import sys

from sympy import sympify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = sorted(glob.glob(os.path.join(ROOT, "data", "course-exams", "*.json")))
BANK = os.path.join(ROOT, "data", "problembank")

failures = []
exams = questions = checks_run = render_strings = 0

MATHTEXT_TOKEN = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)")
MATH_PAIR = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")
SENTINEL = "\x00"
UNRENDERABLE = "₮✗"


def check_render(label, node):
    global render_strings
    if isinstance(node, str):
        render_strings += 1
        protected = node.replace("\\$", SENTINEL)
        if protected.count("$") % 2 != 0:
            failures.append(f"{label}: odd number of $ delimiters: {node[:70]!r}")
        for tok in MATHTEXT_TOKEN.findall(protected):
            shown = tok.replace(SENTINEL, "\\$")[:70]
            if tok.startswith("**") and MATH_PAIR.search(tok[2:-2]):
                failures.append(f"{label}: bold run swallows inline math: {shown!r}")
            elif tok.startswith("$") and any(c in tok for c in UNRENDERABLE):
                failures.append(f"{label}: character KaTeX cannot draw in math: {shown!r}")
    elif isinstance(node, dict):
        for k, v in node.items():
            if k == "check":
                continue
            check_render(label, v)
    elif isinstance(node, list):
        for v in node:
            check_render(label, v)


def main():
    global exams, questions, checks_run
    if not FILES:
        print("No course-exam files found.", file=sys.stderr)
        sys.exit(1)

    by_course = {}
    for path in FILES:
        with open(path) as fh:
            ex = json.load(fh)
        exams += 1
        meta = ex.get("meta") or {}
        eid = meta.get("examId", os.path.basename(path))
        check_render(os.path.basename(path), ex)

        for field in ("examId", "course", "label", "minutes", "totalQuestions"):
            if not meta.get(field):
                failures.append(f"{eid}: missing meta field '{field}'")

        qs = ex.get("questions") or []
        if not qs:
            failures.append(f"{eid}: no questions")
            continue
        if meta.get("totalQuestions") != len(qs):
            failures.append(f"{eid}: meta.totalQuestions {meta.get('totalQuestions')} "
                            f"!= actual {len(qs)}")

        # Every unit of the course spine must be represented.
        course = meta.get("course")
        bank_path = os.path.join(BANK, "%s.json" % course)
        if os.path.exists(bank_path):
            with open(bank_path) as fh:
                spine = [u["id"] for u in json.load(fh)["units"]]
            covered = {q.get("unit") for q in qs}
            for uid in spine:
                if uid not in covered:
                    failures.append(f"{eid}: unit '{uid}' is not represented — an exam must "
                                    f"span the whole course")
        else:
            failures.append(f"{eid}: no bank found for course '{course}' to check coverage")

        seen = set()
        for q in qs:
            questions += 1
            qid = f"{eid}/{q.get('id', '<no-id>')}"
            if not q.get("id"):
                failures.append(f"{qid}: missing id")
            elif q["id"] in seen:
                failures.append(f"{qid}: duplicate question id WITHIN the exam")
            else:
                seen.add(q["id"])
            if not q.get("statement"):
                failures.append(f"{qid}: missing statement")
            if not q.get("unit"):
                failures.append(f"{qid}: missing unit tag — results could not name a weak unit")
            opts = q.get("options")
            if not isinstance(opts, list) or len(opts) != 4:
                failures.append(f"{qid}: needs exactly 4 options")
            elif len(set(opts)) != 4:
                failures.append(f"{qid}: options not distinct: {opts}")
            ci = q.get("correctIndex")
            if not isinstance(ci, int) or not (0 <= ci <= 3):
                failures.append(f"{qid}: bad correctIndex {ci!r}")
            if not q.get("explanation"):
                failures.append(f"{qid}: missing explanation")
            chks = q.get("check")
            if not isinstance(chks, list) or len(chks) == 0:
                failures.append(f"{qid}: empty check[] — every exam answer must be verified")
                continue
            for expr in chks:
                checks_run += 1
                try:
                    result = sympify(expr)
                except Exception as e:  # noqa: BLE001
                    failures.append(f"{qid}: check did not sympify: {expr!r} ({e})")
                    continue
                try:
                    ok = bool(result) is True
                except TypeError:
                    ok = False
                if not ok:
                    failures.append(f"{qid}: check is NOT True: {expr!r} -> {result!r}")

        by_course.setdefault(course, []).append((eid, seen))

    # The exams of one course must not share a question.
    for course, lst in by_course.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                overlap = lst[i][1] & lst[j][1]
                if overlap:
                    failures.append(f"{course}: {lst[i][0]} and {lst[j][0]} share "
                                    f"{len(overlap)} question(s) — exams must be disjoint")

    print(f"verify:exams — exams: {exams}, questions: {questions}, "
          f"sympy checks run: {checks_run}, render-safety strings: {render_strings}")
    if failures:
        for f in failures:
            print(f"  ✗ {f}")
        print(f"  {len(failures)} FAILURE(S)")
        sys.exit(1)
    print("  ✓ all checks passed")


if __name__ == "__main__":
    main()
