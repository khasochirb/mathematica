# -*- coding: utf-8 -*-
"""Shared authoring helpers for the Grade 3 topic builders.

Grade 3 is the third primary-band year, authored one rung BELOW Grade 4.
The machinery is deliberately identical to Grade 4's — same step idiom,
same figure builders, same assert-before-write discipline — because the
two years are read by the same components and gated by the same rules.
Only two things change: write_topic() targets data/genmath/3, and the
grade ceiling drops from 10 000 to 1000 (enforced by check_grade3.py, not
here, so that a builder cannot quietly opt out of it).

Everything is re-exported rather than re-implemented. A Grade 3 builder
importing `teach` gets the SAME function a Grade 4 builder gets, so the
two corpora cannot drift into different shapes.
"""
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_SCRIPTS, "grade4"))
sys.path.insert(0, os.path.join(_SCRIPTS, "grade5"))

from g5build import (  # noqa: F401,E402  (re-exported for topic builders)
    funfact, near, prob, recap, tapq, teach, th, tip, tp, tryitset,
    wex, workedset, _assert_checks,
)
from g4build import (  # noqa: F401,E402  (figures — same builders as Grade 4)
    withfig, withprobfig, fig_bar, fig_groups, fig_numline, fig_geo,
    P, seg, ang, poly,
    C_ACCENT, C_WARM, C_GREEN, C_NEUTRAL, _count_figures,
)

ROOT = os.path.dirname(_SCRIPTS)
OUT = os.path.join(ROOT, "data", "genmath", "3")

# The Grade 3 number ceiling. Stated here so a builder can assert against it
# while choosing values; check_grade3.py enforces it on the written JSON.
CEILING = 1000


def write_topic(topic, filename):
    """Assert every check in the topic, then write the JSON (grade-3 dir)."""
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


def clock(hour, minute):
    """A clock face as a geo figure: a twelve-sided rim through the hour
    marks, the 12/3/6/9 numerals, and the two hands at the EXACT angles
    for `hour`:`minute`.

    Generalised from the one-off face in Grade 4's measurement topic so
    that Grade 3 — which reads the clock to five minutes, a finer grain
    than Grade 4's quarter hours — can draw any legal time without
    re-deriving trigonometry per lesson.

    The hands are honest. The hour hand advances half a degree per minute,
    so at half past four it sits BETWEEN the 4 and the 5 exactly as a real
    clock does; a child reading the picture gets the same time the
    statement says, because both come from this one (hour, minute) pair.

    Diagram units are y-UP (GeoDiagram flips for the screen), so angles
    measured clockwise from 12 give (sin, cos) directly.
    """
    import math
    assert 1 <= hour <= 12, "clock: hour %r out of range" % (hour,)
    assert 0 <= minute < 60, "clock: minute %r out of range" % (minute,)
    assert minute % 5 == 0, "clock: minute %r is not a five-minute mark" % (minute,)

    cx = cy = 5.0
    rim_r = 4.2
    numerals = {12: "12", 3: "3", 6: "6", 9: "9"}

    def at(deg_from_12, radius):
        rad = math.radians(deg_from_12)
        return (cx + radius * math.sin(rad), cy + radius * math.cos(rad))

    pts, rim = [], []
    for k in range(1, 13):
        x, y = at(30 * k, rim_r)
        pts.append(P("h%d" % k, x, y, numerals.get(k, "")))
        rim.append(seg("h%d" % k, "h%d" % (k % 12 + 1), color=C_NEUTRAL))

    hx, hy = at((hour % 12) * 30 + minute * 0.5, rim_r * 0.52)
    mx, my = at(minute * 6, rim_r * 0.86)
    pts += [P("C", cx, cy, ""), P("H", hx, hy, ""), P("M", mx, my, "")]
    hands = [seg("C", "M", color=C_ACCENT), seg("C", "H", color=C_WARM)]
    return fig_geo(pts, rim + hands, height=220)


def coins(*denoms):
    """Mongolian tögrög notes laid out as counting groups: each entry is
    (value, how_many). Renders one labelled group per denomination, so a
    child counts the notes in the picture and reaches the same total the
    statement asks for."""
    assert denoms, "coins: nothing to draw"
    groups = []
    palette = [C_ACCENT, C_WARM, C_GREEN, C_NEUTRAL]
    for i, (value, count) in enumerate(denoms):
        assert value in (1, 5, 10, 20, 50, 100, 500), "coins: %r is not a note we use" % (value,)
        groups.append((count, "%d togrog" % value, palette[i % len(palette)]))
    return fig_groups(*groups)
