# -*- coding: utf-8 -*-
"""Shared authoring helpers for the Grade 5 topic builders.

Extracted from build_place_value.py so every primary-band topic builds the
same way: GRADE-idiom steps (teach beats, embedded workedSet/tryItSet,
tapQuestion, funFact, recap, tip), and a write_topic() that asserts every
sympy check in the whole structure BEFORE writing the JSON — fail = crash,
nothing written.
"""
import json
import os
import sys

from sympy import sympify

# The primary band's shared figure vocabulary. Until 2026-08-13 this module
# had none, and the year built on it shipped forty lessons without a single
# figure — the audit's worst finding. Importing it here is what lets a
# grade-4 builder reach for a picture at all.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "primary"))
from figures import (  # noqa: E402,F401
    C_ACCENT, C_GREEN, C_NEUTRAL, C_WARM, P, ang, fig_bar, fig_barchart,
    fig_clock, fig_geo, fig_groups, fig_linegraph, fig_numline,
    fig_pictograph, poly, seg, withfig, withprobfig,
)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "4")


def _assert_checks(obj, path="topic"):
    """Walk the structure; every `check` list must sympify to True."""
    count = 0
    if isinstance(obj, dict):
        for expr in obj.get("check", []):
            # sympify returns BooleanTrue (not Python True); bool() converts,
            # and an undecidable relational raises on bool() — both are fails.
            try:
                ok = bool(sympify(expr)) is True
            except Exception as e:  # noqa: BLE001
                raise SystemExit("%s: check does not sympify: %r (%s)" % (path, expr, e))
            if not ok:
                raise SystemExit("%s: check not True: %r" % (path, expr))
            count += 1
        for k, v in obj.items():
            if k != "check":
                count += _assert_checks(v, "%s.%s" % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            count += _assert_checks(v, "%s[%d]" % (path, i))
    return count


def th(n):
    """Thin-space thousands separator for KaTeX: 4708215 -> 4\\,708\\,215."""
    s = "{:,}".format(n)
    return s.replace(",", "\\,")


def near(n, target, rival):
    """Check string asserting `target` is the nearer multiple than `rival`."""
    return "Abs(%d - %d) < Abs(%d - %d)" % (n, target, n, rival)


# --------------------------------------------------------------------------
# step helpers (grade idiom)
# --------------------------------------------------------------------------

def teach(eyebrow, title, beats):
    return {"kind": "teach", "eyebrow": eyebrow, "title": title, "beats": beats}


def workedset(title, intro, examples):
    return {"kind": "workedSet", "eyebrow": "Worked examples", "title": title,
            "intro": intro, "examples": examples}


def wex(prompt, steps, answer, check):
    return {"prompt": prompt, "steps": steps, "answer": answer, "check": check}


def tryitset(title, intro, problems, eyebrow="Try it yourself"):
    return {"kind": "tryItSet", "eyebrow": eyebrow, "title": title,
            "intro": intro, "problems": problems}


def tp(prompt, options, explanation, check, correct=0):
    assert len(set(options)) == len(options), "duplicate options: %r" % prompt
    return {"prompt": prompt, "options": options, "correctIndex": correct,
            "explanation": explanation, "check": check}


def tapq(title, prompt, options, explanation, check):
    assert len(set(options)) == len(options), "duplicate options: %r" % prompt
    return {"kind": "tapQuestion", "eyebrow": "Quick check", "title": title,
            "prompt": prompt, "options": options, "correctIndex": 0,
            "explanation": explanation, "check": check}


def funfact(title, body, eyebrow="Fun fact"):
    return {"kind": "funFact", "eyebrow": eyebrow, "title": title, "body": body}


def recap(points):
    return {"kind": "recap", "eyebrow": "Recap", "title": "What you learned",
            "points": points}


def tip(body):
    return {"kind": "tip", "eyebrow": "Practice", "title": "Time to practice",
            "body": body}


def prob(id_, statement, solution, check):
    return {"id": id_, "statement": statement, "solution": solution, "check": check}


def write_topic(topic, filename):
    """Assert every check in the topic, then write the JSON."""
    os.makedirs(OUT, exist_ok=True)
    checks_run = _assert_checks(topic)
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(topic, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    n_steps = sum(len(l["interactive"]["steps"]) for l in topic["lessons"])
    print("wrote %s — %d lessons, %d steps, %d practice, %d test, %d sympy checks"
          % (os.path.relpath(path, ROOT), len(topic["lessons"]), n_steps,
             len(topic["practice"]), len(topic["testYourself"]), checks_run))
