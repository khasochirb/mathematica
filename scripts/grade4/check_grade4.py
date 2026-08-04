#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural + age-fit gate for the Grade 4 corpus.

verify-genmath.py already proves every sympy check is TRUE. This adds the
things it cannot know: the grade idiom (13-step arc in order), the answer
conventions (tapQuestion correct at index 0, 3 options per tryIt problem),
the grade CEILING (nothing above 10 000, no negatives, no decimals in
checks), figure sanity (every figure config well-formed, geo points
referenced exist, right-angle marks sit on true right angles), and the
authoring-debris sweep.

Run: python3 scripts/grade4/check_grade4.py
"""
import json
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "data", "genmath", "4")

ARC = ["teach", "workedSet", "tryItSet", "tapQuestion", "funFact",
       "teach", "workedSet", "tryItSet", "tapQuestion", "recap", "tip",
       "tryItSet", "funFact"]

# Self-talk left in shipped prose. "No — ..." at the START of a string is a
# legitimate answer option ("No — a quarter needs 4 equal parts"), so it only
# counts as debris mid-sentence.
# "actually"/"wait" are only debris as SELF-CORRECTION ("wait, no", "— actually"),
# not in ordinary prose ("the questions people actually ask").
DEBRIS = re.compile(r"\.\.\.|…|\bwait[,.]|\bwait\s+no\b|[—-]\s*actually\b|"
                    r"\bactually[,.]|\bhmm\b|careful:", re.I)
MID_SENTENCE_NO = re.compile(r"\S\s+no —", re.I)
# A number with a decimal point inside a sympy check string.
DECIMAL_IN_CHECK = re.compile(r"\d+\.\d+")
CEILING = 10000

failures = []
stats = {"topics": 0, "lessons": 0, "steps": 0, "problems": 0, "figures": 0, "checks": 0}


def fail(where, msg):
    failures.append("%s: %s" % (where, msg))


# Presentation fields that are not student-facing prose.
SKIP_KEYS = {"check", "color", "glyph", "id", "slug", "mode", "kind"}


def walk_strings(node, path, out):
    if isinstance(node, str):
        out.append((path, node))
    elif isinstance(node, dict):
        for k, v in node.items():
            if k not in SKIP_KEYS:
                walk_strings(v, "%s.%s" % (path, k), out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_strings(v, "%s[%d]" % (path, i), out)


# A number as a child reads it: plain digits, or KaTeX thin-space grouping
# (4\,350). Plain commas/spaces are NOT joined — "1, 2, 4" is three numbers.
NUMBER = re.compile(r"(?<![\d.\\])(\d{1,3}(?:\\,\d{3})+|\d+)(?![\d.])")


def check_numbers_in_text(where, text):
    """No value above the grade ceiling in student-facing prose."""
    for m in NUMBER.finditer(text):
        raw = m.group(1).replace("\\,", "")
        if not raw.isdigit():
            continue
        if int(raw) > CEILING:
            fail(where, "value %s exceeds the Grade 4 ceiling of %d" % (raw, CEILING))


def check_figure(where, fig):
    stats["figures"] += 1
    mode = fig.get("mode")
    if not mode:
        fail(where, "figure has no mode")
        return
    if mode == "fractionBar":
        f = fig.get("fraction") or {}
        num, den = f.get("num"), f.get("den")
        if not isinstance(num, int) or not isinstance(den, int):
            fail(where, "fractionBar num/den must be ints")
        elif not (0 < den <= 16 and 0 <= num <= den):
            fail(where, "fractionBar %r/%r out of range" % (num, den))
    elif mode == "groups":
        gs = fig.get("groups") or []
        if not gs:
            fail(where, "groups figure has no groups")
        for g in gs:
            # 0 is legal: an empty-but-standing column ("0 hundreds") is the
            # picture of a zero placeholder. Negative counts never are.
            if not isinstance(g.get("count"), int) or g["count"] < 0:
                fail(where, "group count must be a non-negative int, got %r" % (g.get("count"),))
            if not g.get("label"):
                fail(where, "group missing label")
    elif mode == "numberLine":
        nl = fig.get("numberLine") or {}
        pts = nl.get("points") or []
        if not pts:
            fail(where, "numberLine has no points")
        lo, hi = nl.get("min"), nl.get("max")
        if lo is not None and hi is not None:
            if lo >= hi:
                fail(where, "numberLine empty range")
            for p in pts:
                if not (lo <= p["value"] <= hi):
                    fail(where, "numberLine point %r outside [%r, %r]" % (p["value"], lo, hi))
        for p in pts:
            if p.get("value") is None or p.get("label") is None:
                fail(where, "numberLine point missing value/label")
    elif mode == "geo":
        g = fig.get("geo") or {}
        pts = {p["id"]: p for p in g.get("points", [])}
        if len(pts) != len(g.get("points", [])):
            fail(where, "geo has duplicate point ids")
        for o in g.get("objects", []):
            for key in ("from", "to", "at"):
                if key in o and o[key] not in pts:
                    fail(where, "geo object references unknown point %r" % (o[key],))
            # A right-angle mark must sit on a TRUE right angle.
            if o.get("kind") == "angle" and o.get("right"):
                try:
                    a, b, c = pts[o["at"]], pts[o["from"]], pts[o["to"]]
                except KeyError:
                    continue
                v1 = (b["x"] - a["x"], b["y"] - a["y"])
                v2 = (c["x"] - a["x"], c["y"] - a["y"])
                dot = v1[0] * v2[0] + v1[1] * v2[1]
                if abs(dot) > 1e-6:
                    fail(where, "right-angle mark at %s is not a right angle (dot=%g)"
                         % (o["at"], dot))
    else:
        fail(where, "unexpected figure mode %r for Grade 4" % (mode,))


def check_checks(where, checks):
    if not isinstance(checks, list) or not checks:
        fail(where, "missing check list")
        return
    for c in checks:
        stats["checks"] += 1
        if DECIMAL_IN_CHECK.search(c):
            fail(where, "decimal literal in check: %r" % (c,))
        if re.search(r"-\s*\d", c) and "Abs" not in c:
            # A minus sign is fine inside subtraction; flag only leading negatives.
            if re.search(r"[(,]\s*-\d", c):
                fail(where, "negative literal in check: %r" % (c,))
        # Trivially true checks teach nothing and hide errors.
        m = re.fullmatch(r"Eq\((\d+),\s*(\d+)\)", c.replace(" ", ""))
        if m and m.group(1) == m.group(2):
            fail(where, "trivial self-equal check: %r" % (c,))


def check_problem(where, p, n_options=None):
    stats["problems"] += 1
    check_checks(where, p.get("check"))
    if n_options is not None:
        opts = p.get("options") or []
        if len(opts) != n_options:
            fail(where, "expected %d options, got %d" % (n_options, len(opts)))
        if len(set(opts)) != len(opts):
            fail(where, "duplicate options")


def main():
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    if not files:
        print("no Grade 4 topics found")
        return 1
    for path in files:
        with open(path, encoding="utf-8") as fh:
            t = json.load(fh)
        slug = t.get("slug", os.path.basename(path))
        stats["topics"] += 1
        if t.get("grade") != 4:
            fail(slug, "grade is %r, expected 4" % (t.get("grade"),))
        if t.get("status") != "published":
            fail(slug, "status is %r, expected published" % (t.get("status"),))
        for field in ("slug", "title", "blurb"):
            if not t.get(field):
                fail(slug, "missing %s" % field)
        if len(t.get("lessons", [])) != 5:
            fail(slug, "expected 5 lessons, got %d" % len(t.get("lessons", [])))
        if len(t.get("practice", [])) != 8:
            fail(slug, "expected 8 practice problems, got %d" % len(t.get("practice", [])))
        if len(t.get("testYourself", [])) != 6:
            fail(slug, "expected 6 test problems, got %d" % len(t.get("testYourself", [])))

        for li, lesson in enumerate(t.get("lessons", [])):
            stats["lessons"] += 1
            lw = "%s/lessons[%d]" % (slug, li)
            for field in ("slug", "title", "concreteComparison", "objective", "keyIdea"):
                if not lesson.get(field):
                    fail(lw, "missing %s" % field)
            if len(lesson.get("concept", [])) != 3:
                fail(lw, "expected 3 concept beats, got %d" % len(lesson.get("concept", [])))
            if len(lesson.get("facts", [])) != 2:
                fail(lw, "expected 2 facts, got %d" % len(lesson.get("facts", [])))
            for cm in lesson.get("commonMistakes", []):
                if not cm.get("authored"):
                    fail(lw, "commonMistake missing authored flag")
            for wi, we in enumerate(lesson.get("workedExamples", [])):
                check_problem("%s.workedExamples[%d]" % (lw, wi), we)
            for ti, ti_p in enumerate(lesson.get("tryIt", [])):
                check_problem("%s.tryIt[%d]" % (lw, ti), ti_p)

            steps = lesson.get("interactive", {}).get("steps", [])
            kinds = [s.get("kind") for s in steps]
            if kinds != ARC:
                fail(lw, "step arc mismatch:\n     got %s\n     want %s" % (kinds, ARC))
            for si, step in enumerate(steps):
                stats["steps"] += 1
                sw = "%s.steps[%d](%s)" % (lw, si, step.get("kind"))
                if step.get("kind") == "tapQuestion":
                    if step.get("correctIndex") != 0:
                        fail(sw, "tapQuestion correctIndex is %r, must be 0"
                             % (step.get("correctIndex"),))
                    check_problem(sw, step, n_options=4)
                elif step.get("kind") == "tryItSet":
                    for pi, p in enumerate(step.get("problems", [])):
                        pw = "%s.problems[%d]" % (sw, pi)
                        check_problem(pw, p, n_options=3)
                        ci = p.get("correctIndex")
                        if not isinstance(ci, int) or not (0 <= ci < 3):
                            fail(pw, "correctIndex %r out of range" % (ci,))
                elif step.get("kind") == "workedSet":
                    for ei, e in enumerate(step.get("examples", [])):
                        check_problem("%s.examples[%d]" % (sw, ei), e)

        # Practice / test banks
        for bi, p in enumerate(t.get("practice", [])):
            check_problem("%s/practice[%d]" % (slug, bi), p)
        for bi, p in enumerate(t.get("testYourself", [])):
            check_problem("%s/testYourself[%d]" % (slug, bi), p)

        # Figures anywhere in the topic
        def find_figs(node, path):
            if isinstance(node, dict):
                if "figure" in node:
                    check_figure("%s%s.figure" % (slug, path), node["figure"])
                for k, v in node.items():
                    find_figs(v, "%s.%s" % (path, k))
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    find_figs(v, "%s[%d]" % (path, i))
        find_figs(t, "")

        # Prose sweep: debris and the grade ceiling
        strings = []
        walk_strings(t, slug, strings)
        for where, s in strings:
            if DEBRIS.search(s) or MID_SENTENCE_NO.search(s):
                fail(where, "authoring debris: %r" % (s[:90],))
            check_numbers_in_text(where, s)

    print("check:grade4 — topics: %d, lessons: %d, steps: %d, problems: %d, "
          "figures: %d, checks: %d" % (stats["topics"], stats["lessons"], stats["steps"],
                                       stats["problems"], stats["figures"], stats["checks"]))
    if failures:
        print("\n%d FAILURES:" % len(failures))
        for f in failures[:60]:
            print("  ✗ %s" % f)
        if len(failures) > 60:
            print("  ... and %d more" % (len(failures) - 60))
        return 1
    print("  ✓ all structural, age-fit and figure checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
