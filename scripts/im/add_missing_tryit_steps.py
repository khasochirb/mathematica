#!/usr/bin/env python3
"""One-time repair, 2026-08-02: reference every orphaned tryIt problem.

The lesson page renders ONLY `lesson.interactive.steps`, so a tryIt problem
that no step references is invisible — authored, sympy-verified, and never
shown. An audit found 60 such problems: every IM1 unit and IM2 unit 1
deliberately referenced only two of each lesson's three tryIts, and the
IM3 units 2–6 step-repair (add_im3_lesson_steps.py) only added steps for
t1 and t2, orphaning every t3.

This script edits the BUILDER sources (the source of truth — the JSON is
regenerated from them), inserting one `{"kind": "tryIt", ...}` step per
orphan next to its sibling tryIt steps, keeping t1 < t2 < t3 order. Run
the builders afterwards; `scripts/verify-genmath.py` now gates on full
reference coverage so the defect cannot ship again.

Run: python3 scripts/im/add_missing_tryit_steps.py
     for f in scripts/im/build_im*.py; do python3 "$f"; done
     npm run verify:genmath
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# pid -> on-screen step title. IM1/IM2 lessons use the "Your turn — ..."
# idiom of their existing tryIt steps; IM3 uses short noun-phrase titles.
TITLES = {
    # IM1 unit 1 — Quantities & Expressions
    "im1-u1-l1-t3": "Your turn — tiles to square metres",
    "im1-u1-l2-t2": "Your turn — read the taxi fare",
    "im1-u1-l3-t2": "Your turn — notebooks on a budget",
    "im1-u1-l4-t3": "Your turn — solve for b",
    # IM1 unit 2 — Linear Equations & Inequalities
    "im1-u2-l1-t3": "Your turn — x on both sides",
    "im1-u2-l2-t2": "Your turn — describe the solutions",
    "im1-u2-l3-t3": "Your turn — how many boxes?",
    "im1-u2-l4-t2": "Your turn — an absolute value",
    # IM1 unit 3 — Functions & Sequences
    "im1-u3-l1-t2": "Your turn — function or not?",
    "im1-u3-l2-t2": "Your turn — evaluate h",
    "im1-u3-l3-t2": "Your turn — the first negative term",
    "im1-u3-l4-t2": "Your turn — the third bounce",
    # IM1 unit 4 — Linear Functions
    "im1-u4-l1-t2": "Your turn — battery drain",
    "im1-u4-l2-t2": "Your turn — both intercepts",
    "im1-u4-l3-t3": "Your turn — to standard form",
    "im1-u4-l4-t2": "Your turn — the courier's charge",
    # IM1 unit 5 — Systems
    "im1-u5-l1-t2": "Your turn — classify the system",
    "im1-u5-l2-t2": "Your turn — solve by substitution",
    "im1-u5-l3-t3": "Your turn — solve by elimination",
    "im1-u5-l4-t2": "Your turn — shade the right side",
    # IM1 unit 6 — Exponential Functions
    "im1-u6-l1-t2": "Your turn — a fading drug",
    "im1-u6-l2-t3": "Your turn — which grows faster?",
    "im1-u6-l3-t2": "Your turn — classify the growth",
    "im1-u6-l4-t2": "Your turn — find the base",
    # IM1 unit 7 — Transformations & Congruence
    "im1-u7-l1-t3": "Your turn — a half turn",
    "im1-u7-l2-t3": "Your turn — reflect twice",
    "im1-u7-l3-t1": "Your turn — three sides equal",
    "im1-u7-l4-t2": "Your turn — the construction's proof",
    # IM1 unit 8 — Coordinate Geometry
    "im1-u8-l1-t2": "Your turn — a midpoint",
    "im1-u8-l2-t2": "Your turn — a parallel line",
    "im1-u8-l3-t3": "Your turn — three quarters along",
    "im1-u8-l4-t2": "Your turn — opposite sides parallel",
    # IM1 unit 9 — Data & Statistics
    "im1-u9-l1-t2": "Your turn — find the IQR",
    "im1-u9-l2-t3": "Your turn — pick the worker",
    "im1-u9-l3-t3": "Your turn — check the totals",
    "im1-u9-l4-t2": "Your turn — read a residual",
    # IM2 unit 1 — Rational Exponents & Radicals
    "im2-u1-l1-t3": "Your turn — a power of a power",
    "im2-u1-l2-t2": "Your turn — a cube root",
    "im2-u1-l3-t2": "Your turn — square the binomial",
    "im2-u1-l4-t2": "Your turn — rational or irrational?",
    # IM3 unit 2 — Rational & Radical Functions
    "im3-u2-l1-t3": "The horizontal asymptote",
    "im3-u2-l2-t3": "Divide and cancel",
    "im3-u2-l3-t3": "Two painters",
    "im3-u2-l4-t3": "Catch the extraneous root",
    # IM3 unit 3 — Exponential & Logarithmic Functions
    "im3-u3-l1-t3": "The domain of a log",
    "im3-u3-l2-t3": "An awkward base",
    "im3-u3-l3-t3": "Isolate, then take logs",
    "im3-u3-l4-t3": "Doubling to 4000",
    # IM3 unit 4 — Trigonometric Functions
    "im3-u4-l1-t3": "A coterminal angle",
    "im3-u4-l2-t3": "Tangent in quadrant III",
    "im3-u4-l3-t3": "Build the sine model",
    "im3-u4-l4-t3": "The identity in disguise",
    # IM3 unit 5 — Function Families & Inverses
    "im3-u5-l1-t3": "Name the transformation",
    "im3-u5-l2-t3": "Even, odd, or neither?",
    "im3-u5-l3-t3": "Decompose the cube",
    "im3-u5-l4-t3": "A point on the inverse",
    # IM3 unit 6 — Sequences, Series & the Binomial Theorem
    "im3-u6-l1-t3": "The pipe stack",
    "im3-u6-l2-t3": "The rumour's reach",
    "im3-u6-l3-t3": "Sum or no sum?",
    "im3-u6-l4-t3": "Three heads in six flips",
}

PID = re.compile(r"^(im\d)-u(\d+)-l\d+-t(\d)$")


def builder_path(pid):
    m = PID.match(pid)
    course = {"im1": "im1", "im2": "im2", "im3": "im3"}[m.group(1)]
    return os.path.join(HERE, f"build_{course}_unit{m.group(2)}.py")


def insert_step(lines, pid, title):
    """Insert the step line next to its sibling tryIt steps, in t-order."""
    prefix = pid.rsplit("-t", 1)[0]
    my_n = int(pid.rsplit("-t", 1)[1])
    sib = re.compile(
        r'^(\s*)\{"kind": "tryIt", .*"problemId": "'
        + re.escape(prefix) + r'-t(\d)"\},?\s*$'
    )
    siblings = []  # (line_index, indent, t_number)
    for i, line in enumerate(lines):
        m = sib.match(line)
        if m:
            siblings.append((i, m.group(1), int(m.group(2))))
    if not siblings:
        raise SystemExit(f"{pid}: no sibling tryIt step lines found")
    if any(n == my_n for _, _, n in siblings):
        return False  # already referenced (idempotent re-run)

    indent = siblings[0][1]
    new_line = (
        f'{indent}{{"kind": "tryIt", "title": {json.dumps(title)}, '
        f'"problemId": {json.dumps(pid)}}},\n'
    )
    later = [i for i, _, n in siblings if n > my_n]
    if later:
        at = min(later)          # before the first higher-numbered sibling
    else:
        at = max(i for i, _, n in siblings) + 1  # after the last lower one
    lines.insert(at, new_line)
    return True


def main():
    by_file = {}
    for pid in TITLES:
        by_file.setdefault(builder_path(pid), []).append(pid)

    total = 0
    for path, pids in sorted(by_file.items()):
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        added = 0
        for pid in sorted(pids):
            if insert_step(lines, pid, TITLES[pid]):
                added += 1
        if added:
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines(lines)
        print(f"{os.path.basename(path)}: +{added} tryIt step(s)")
        total += added
    print(f"inserted {total} steps — now re-run the builders and the gate")
    if total == 0:
        print("(nothing to do — already applied)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
