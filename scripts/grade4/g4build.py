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
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "grade5"))

from g5build import (  # noqa: F401  (re-exported for topic builders)
    funfact, near, prob, recap, tapq, teach, th, tip, tp, tryitset,
    wex, workedset, _assert_checks,
)

ROOT = os.path.dirname(os.path.dirname(_HERE))
OUT = os.path.join(ROOT, "data", "genmath", "4")


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


# --------------------------------------------------------------------------
# figures — configs for components/genmath/interactive (FigureSpec)
# --------------------------------------------------------------------------

# The warm palette existing figure-bearing topics use.
C_ACCENT = "#3b82f6"
C_WARM = "#d97706"
C_GREEN = "#059669"
C_NEUTRAL = "#94a3b8"


def withfig(item, figure):
    """Attach a figure to a TEACH step, a TAPQUESTION, a worked-example item
    or a tryIt option-problem — the four places whose renderers read
    `figure`.

    NOT for practice/testYourself bank problems: those render through
    RevealProblemCard, whose `figure` field is the ЭЕШ hub's image type.
    Use withprobfig() there. check_grade3/4 fails the build either way, so
    a figure can never again be authored somewhere nothing draws it."""
    assert isinstance(item, dict) and figure, "withfig: bad arguments"
    return {**item, "figure": figure}


def withprobfig(problem, figure):
    """Attach a figure to a practice/testYourself bank problem.

    Writes `courseFigure`, which RevealProblemCard renders with RatioFigure.
    The plain `figure` key is the ЭЕШ image shape (src/width/height) and a
    genmath spec placed there draws nothing at all."""
    assert isinstance(problem, dict) and figure, "withprobfig: bad arguments"
    assert "statement" in problem, "withprobfig: not a bank problem"
    return {**problem, "courseFigure": figure}


def fig_bar(num, den, label=None):
    """A fraction bar: `den` equal pieces, `num` shaded."""
    assert 0 < den <= 16 and 0 <= num <= den, "fig_bar: %r/%r out of range" % (num, den)
    f = {"num": int(num), "den": int(den)}
    if label:
        f["label"] = label
    return {"mode": "fractionBar", "fraction": f}


def fig_groups(*groups):
    """Glyph groups: each group is (count, label) or (count, label, color, glyph).
    Draws equal groups / pictograph rows / part collections.

    A count of 0 is legal and deliberate: it renders an EMPTY group still
    captioned with its label ("0 hundreds"), which is how a place-value
    figure shows a column that is empty but still standing."""
    assert groups, "fig_groups: no groups"
    out = []
    palette = [C_ACCENT, C_WARM, C_GREEN, C_NEUTRAL]
    for i, g in enumerate(groups):
        count, label = g[0], g[1]
        color = g[2] if len(g) > 2 else palette[i % len(palette)]
        assert 0 <= count <= 24, "fig_groups: count %r out of range" % (count,)
        item = {"count": int(count), "color": color, "label": label}
        if len(g) > 3:
            item["glyph"] = g[3]
        out.append(item)
    return {"mode": "groups", "groups": out}


def fig_numline(points, lo=None, hi=None):
    """A number line with labelled points: [(value, label), ...] or
    [(value, label, color), ...]. Bounds default to the component's 0..1
    unless given."""
    assert points, "fig_numline: no points"
    pts = []
    for p in points:
        d = {"value": p[0], "label": p[1]}
        if len(p) > 2:
            d["color"] = p[2]
        pts.append(d)
    nl = {"points": pts}
    if lo is not None:
        nl["min"] = lo
    if hi is not None:
        nl["max"] = hi
    if lo is not None and hi is not None:
        assert lo < hi, "fig_numline: empty range"
        for p in pts:
            assert lo <= p["value"] <= hi, "fig_numline: point %r outside [%r, %r]" % (p["value"], lo, hi)
    return {"mode": "numberLine", "numberLine": nl}


def P(pid, x, y, label=None):
    """A named point for geo diagrams. Label defaults to the id; pass
    label="" for an unlabelled construction point."""
    p = {"id": pid, "x": round(float(x), 3), "y": round(float(y), 3)}
    p["label"] = pid if label is None else label
    return p


def seg(a, b, label=None, dashed=False, color=None):
    o = {"kind": "segment", "from": a, "to": b}
    if label:
        o["label"] = label
    if dashed:
        o["dashed"] = True
    if color:
        o["color"] = color
    return o


def ang(at, frm, to, label=None, right=False):
    """Angle arc at vertex `at` between rays toward `frm` and `to`;
    right=True draws the square right-angle mark."""
    o = {"kind": "angle", "at": at, "from": frm, "to": to}
    if label:
        o["label"] = label
    if right:
        o["right"] = True
    return o


def fig_geo(points, objects, height=None):
    """A static geometry diagram. Asserts every referenced point exists."""
    ids = {p["id"] for p in points}
    assert len(ids) == len(points), "fig_geo: duplicate point ids"
    for o in objects:
        for key in ("from", "to", "at"):
            if key in o:
                assert o[key] in ids, "fig_geo: object references unknown point %r" % (o[key],)
    g = {"points": points, "objects": objects}
    if height:
        g["height"] = height
    return {"mode": "geo", "geo": g}


def poly(points_ids, color=None):
    """Segments closing a polygon through the given point ids, in order."""
    out = []
    n = len(points_ids)
    assert n >= 3, "poly: need at least 3 points"
    for i in range(n):
        out.append(seg(points_ids[i], points_ids[(i + 1) % n], color=color))
    return out
