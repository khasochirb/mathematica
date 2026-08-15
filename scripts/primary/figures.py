# -*- coding: utf-8 -*-
"""The primary band's FIGURE VOCABULARY — one definition, every grade.

Extracted from scripts/grade3/g4build.py on 2026-08-13. It lived inside one
grade's helper module, which is exactly why the 2026-08-13 audit found the
top primary year shipping FORTY lessons with no figure at all: the author of
that year had no vocabulary to reach for. Every primary builder now imports
from here, so a figure a child needs is never a grade away.

Each helper asserts what its picture must satisfy before it can be built —
no bar past its axis, no pictograph value a symbol row cannot draw, no geo
object pointing at a point that does not exist. A figure that would mislead
a seven-year-old fails the build instead of shipping.

The configs mirror FigureSpec in lib/genmath-interactive.ts and render
through components/genmath/interactive/RatioFigure.tsx.
"""

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


def fig_barchart(categories, step=1, unit=None, max_=None, highlight=None):
    """A real bar chart: [(label, value, color?)...]. Values must be exact
    multiples the axis can carry; the assert keeps a chart readable for a
    child — no bar past the axis, no zero-category chart."""
    assert categories, "fig_barchart: no categories"
    cats = []
    for c in categories:
        label, value = c[0], c[1]
        assert isinstance(value, int) and 0 <= value <= 60, "fig_barchart: value %r" % (value,)
        d = {"label": label, "value": value}
        if len(c) > 2 and c[2]:
            d["color"] = c[2]
        cats.append(d)
    top = max(c["value"] for c in cats)
    if max_ is not None:
        assert max_ >= top, "fig_barchart: max below tallest bar"
    fig = {"mode": "barChart", "barChart": {"categories": cats, "step": step}}
    if unit: fig["barChart"]["unit"] = unit
    if max_ is not None: fig["barChart"]["max"] = max_
    if highlight is not None:
        assert 0 <= highlight < len(cats), "fig_barchart: highlight out of range"
        fig["barChart"]["highlight"] = highlight
    return fig


def fig_pictograph(rows, key, symbol=None, color=None):
    """A pictograph with a key: rows [(label, value)...], one symbol = key.
    Every value must be a whole- or half-multiple of the key, because that
    is the only thing a symbol row can SHOW — a value the picture cannot
    draw is a lying figure and fails the build."""
    assert rows and key >= 1, "fig_pictograph: bad rows/key"
    for label, value in rows:
        doubled = (2 * value) % key
        assert doubled == 0,             "fig_pictograph: %r=%r not a half-multiple of key %r" % (label, value, key)
        assert value // key <= 12, "fig_pictograph: row %r too long to read" % (label,)
    fig = {"mode": "pictograph",
           "pictograph": {"rows": [{"label": l, "value": v} for l, v in rows], "key": key}}
    if symbol: fig["pictograph"]["symbol"] = symbol
    if color: fig["pictograph"]["color"] = color
    return fig


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


def fig_linegraph(points, step=1, unit=None, max_=None, color=None):
    """A plotted line over labelled readings: [(label, value)...].

    Exists because the line-graph lesson used to give a child a list of
    numbers and ask questions about "the graph" — the reading skill was
    never on the page. Values are asserted small and whole so the axis a
    child counts stays countable."""
    assert len(points) >= 2, "fig_linegraph: a line needs at least two readings"
    pts = []
    for label, value in points:
        assert isinstance(value, int) and 0 <= value <= 200, \
            "fig_linegraph: value %r out of a primary-readable range" % (value,)
        pts.append({"label": label, "value": value})
    top = max(p["value"] for p in pts)
    if max_ is not None:
        assert max_ >= top, "fig_linegraph: max below the tallest reading"
    lg = {"points": pts, "step": step}
    if unit: lg["unit"] = unit
    if max_ is not None: lg["max"] = max_
    if color: lg["color"] = color
    return {"mode": "lineGraph", "lineGraph": lg}


def fig_clock(hour, minute, until=None, label=None, until_label=None):
    """An analogue clock at h:mm — two faces when `until` is given, which is
    the shape an elapsed-time question wants.

    The hour is asserted 1..12 (a clock face has no 0 and no 13) and the
    minute 0..59, because a face cannot draw what those would mean."""
    def ok(h, m):
        assert 1 <= h <= 12, "fig_clock: hour %r is not on a clock face" % (h,)
        assert 0 <= m <= 59, "fig_clock: minute %r out of range" % (m,)
    ok(hour, minute)
    cf = {"hour": int(hour), "minute": int(minute)}
    if until is not None:
        ok(until[0], until[1])
        cf["until"] = {"hour": int(until[0]), "minute": int(until[1])}
    if label: cf["label"] = label
    if until_label: cf["untilLabel"] = until_label
    return {"mode": "clockFace", "clockFace": cf}
