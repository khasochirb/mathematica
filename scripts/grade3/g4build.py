# -*- coding: utf-8 -*-
"""Shared authoring helpers for the Grade 4 topic builders.

Re-exports the Grade 5 step/problem helpers (the grade idiom is identical)
with write_topic() retargeted at data/genmath/4, and adds FIGURE builders —
Grade 4 is the first primary grade authored with figures from day one.

Figure discipline (figures-creator): a figure's config is interpolated from
the SAME Python variables as the statement it illustrates, so text and
picture cannot disagree. Every helper asserts its config makes sense —
a broken figure fails the build, nothing ships.
"""
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "grade4"))

from g5build import (  # noqa: F401  (re-exported for topic builders)
    funfact, near, prob, recap, tapq, teach, th, tip, tp, tryitset,
    wex, workedset, _assert_checks,
)

ROOT = os.path.dirname(os.path.dirname(_HERE))
OUT = os.path.join(ROOT, "data", "genmath", "3")


def write_topic(topic, filename):
    """Assert every check in the topic, then write the JSON (grade-4 dir)."""
    os.makedirs(OUT, exist_ok=True)
    checks_run = _assert_checks(topic)
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(topic, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    n_steps = sum(len(l["interactive"]["steps"]) for l in topic["lessons"])
    n_figs = _count_figures(topic)
    print("wrote %s — %d lessons, %d steps, %d practice, %d test, %d sympy checks, %d figures"
          % (os.path.relpath(path, ROOT), len(topic["lessons"]), n_steps,
             len(topic["practice"]), len(topic["testYourself"]), checks_run, n_figs))


def _count_figures(obj):
    n = 0
    if isinstance(obj, dict):
        n += 1 if "figure" in obj else 0
        n += sum(_count_figures(v) for v in obj.values())
    elif isinstance(obj, list):
        n += sum(_count_figures(v) for v in obj)
    return n


# figures — the primary band's shared vocabulary (scripts/primary/figures.py).
# Re-exported so this grade's builders keep importing from g4build.
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "primary"))
from figures import (  # noqa: E402,F401
    C_ACCENT,
    C_GREEN,
    C_NEUTRAL,
    C_WARM,
    P,
    ang,
    fig_bar,
    fig_barchart,
    fig_clock,
    fig_geo,
    fig_linegraph,
    fig_groups,
    fig_numline,
    fig_pictograph,
    poly,
    seg,
    withfig,
    withprobfig,
)
