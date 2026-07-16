# -*- coding: utf-8 -*-
"""Problem-bank subject: Geometry — mirrors the /math/geometry course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/geometry_course.py` for the self-check.
"""
import importlib.util
import os
import re
from math import cos, radians, sin

from sympy import Rational, simplify, sqrt, sympify

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "geometry"
TITLE = "Geometry"
TITLE_MN = "Геометр"
BLURB = ("Unit-by-unit practice for the Geometry course — from points and angles to circles, area, and coordinates.")

UNITS = [
    {"id": "foundations", "title": "Foundations: Points, Lines & Angles",
     "blurb": "Points, lines, rays, segments and planes; measuring segments and angles; angle types, angle pairs, and bisectors."},
    {"id": "reasoning-and-proof", "title": "Reasoning & Proof",
     "blurb": "From noticing patterns to proving facts: conjectures, if-then statements, and your first two-column proofs."},
    {"id": "parallel-and-perpendicular", "title": "Parallel & Perpendicular Lines",
     "blurb": "Transversals and the angle pairs they create — which are congruent, which are supplementary — and proving lines parallel."},
    {"id": "triangles-and-congruence", "title": "Triangles & Congruence",
     "blurb": "Triangle types, the angle sum, the triangle inequality, and the congruence shortcuts SSS · SAS · ASA · AAS · HL."},
    {"id": "relationships-in-triangles", "title": "Relationships in Triangles",
     "blurb": "Bisectors, medians, altitudes, the midsegment theorem, and inequalities inside a triangle."},
    {"id": "quadrilaterals-and-polygons", "title": "Quadrilaterals & Polygons",
     "blurb": "Angle sums for any polygon; parallelograms, rectangles, rhombi, squares, trapezoids, and kites — with proofs."},
    {"id": "similarity", "title": "Similarity",
     "blurb": "Ratio and proportion, similar polygons, the AA · SSS · SAS similarity shortcuts, and the side-splitter theorem."},
    {"id": "right-triangles-and-trig", "title": "Right Triangles & Trigonometry",
     "blurb": "The Pythagorean theorem, special right triangles, and sine · cosine · tangent with elevation and depression."},
    {"id": "circles", "title": "Circles",
     "blurb": "Radius, chord, tangent, secant; central and inscribed angles; arcs; and the circle relationships."},
    {"id": "area-and-perimeter", "title": "Area & Perimeter",
     "blurb": "Areas of triangles, quadrilaterals and regular polygons; circumference, circle area, sectors, and composite figures."},
    {"id": "surface-area-and-volume", "title": "Surface Area & Volume",
     "blurb": "Prisms, cylinders, pyramids, cones, and spheres — wrapping and filling 3-D solids."},
    {"id": "transformations", "title": "Transformations",
     "blurb": "Translations, reflections, rotations, and dilations; symmetry; congruence and similarity re-seen through motion."},
    {"id": "coordinate-geometry", "title": "Coordinate Geometry",
     "blurb": "Distance, midpoint, and slope; equations of lines and circles; proofs with coordinates — the course capstone."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "similar-triangles": "similarity",
    "pythagoras": "right-triangles-and-trig",
    "special-triangles": "right-triangles-and-trig",
    "circle-basics": "circles",
    "sector-area": "circles",
    "triangle-area": "area-and-perimeter",
    "solid-volumes": "surface-area-and-volume",
}

SOURCES = ['geometry']

# Independent re-solvers for the NEW forms below: form id -> fn(statement) ->
# ("num", sympy-comparable) | ("opt", exact option string) | ("assert", bool)
RESOLVERS = {}


def _load(name):
    spec = importlib.util.spec_from_file_location(
        "pbsrc_%s" % name, os.path.join(PB, "%s.py" % name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _remapped_forms():
    src = {}
    for name in SOURCES:
        for f in _load(name).build()["forms"]:
            src[f["id"]] = f
    forms = []
    for fid, unit in REMAP.items():
        f = dict(src[fid])
        f["unit"] = unit
        forms.append(f)
    return forms


# ---------------------------------------------------------------------------
# formatting + option-assembly helpers (house style copied from geometry.py)
# ---------------------------------------------------------------------------

def intL(v):
    return str(int(v))


def L(v):
    """LaTeX for an integer/rational value (no surrounding $)."""
    v = sympify(v)
    if getattr(v, "q", 1) == 1:
        return str(v.p if hasattr(v, "p") else int(v))
    if v < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def degL(v):
    return "%d°" % int(v)


def build_latex_options(correct, cands, pos, latex_of=None):
    """correct = (latex, value); cands = list of (latex, value).

    Returns (options[4] wrapped in $...$, correctIndex=pos). Guarantees the
    three chosen distractors are numerically distinct from the correct answer
    and from each other, and have distinct latex. Crashes on collision.
    """
    clat, cval = correct[0], sympify(correct[1])
    chosen = []  # list of (latex, value)
    for lat, val in cands:
        v = sympify(val)
        if simplify(v - cval) == 0:
            continue
        if lat == clat or any(lat == l for l, _ in chosen):
            continue
        if any(simplify(v - cv) == 0 for _, cv in chosen):
            continue
        chosen.append((lat, v))
        if len(chosen) == 3:
            break
    k = 1
    while len(chosen) < 3 and latex_of is not None:
        for cand in (cval + k, cval - k):
            lat = latex_of(cand)
            if simplify(cand - cval) == 0:
                continue
            if lat == clat or any(lat == l for l, _ in chosen):
                continue
            if any(simplify(cand - cv) == 0 for _, cv in chosen):
                continue
            chosen.append((lat, cand))
            if len(chosen) == 3:
                break
        k += 1
        if k > 60:
            break
    assert len(chosen) == 3, "could not build 3 distractors for %s" % clat
    final = [l for l, _ in chosen]
    final.insert(pos, clat)
    opts = ["$" + s + "$" for s in final]
    assert len(set(opts)) == 4, "option collision for %s" % clat
    return opts, pos


def _pt(pid, x, y, label=""):
    return {"id": pid, "x": round(x, 4), "y": round(y, 4), "label": label}


def _pair_str(x, y):
    return "$(%d; %d)$" % (x, y)


def _pair_opts(hint, correct, cands, pos):
    """4 distinct '(x; y)' options; crash on collision."""
    cs = _pair_str(*correct)
    opts = []
    for c in cands:
        s = _pair_str(*c)
        if s != cs and s not in opts:
            opts.append(s)
    assert len(opts) >= 3, "%s: cannot build 3 distinct pair distractors" % hint
    opts = opts[:3]
    opts.insert(pos, cs)
    assert len(set(opts)) == 4, "%s: option collision" % hint
    return opts, pos


# ---------------------------------------------------------------------------
# per-form generators (each returns exactly 36 variant dicts without ids)
# ---------------------------------------------------------------------------

def gen_segadd():
    fwd = [(2, 7), (3, 5), (4, 9), (5, 3), (6, 8), (7, 4), (8, 11), (9, 6),
           (10, 5), (11, 7), (12, 9), (13, 4), (14, 3), (4, 13), (5, 12),
           (6, 15), (3, 11), (8, 7)]
    rev = [(9, 4), (11, 5), (12, 7), (13, 6), (15, 8), (14, 9), (16, 7),
           (17, 5), (18, 11), (19, 8), (20, 13), (10, 3), (21, 9), (22, 15),
           (13, 4), (17, 12), (19, 6), (23, 16)]
    out = []
    idx = 0

    def bar_fig(a, whole, part_b_label, bar_label):
        t = whole
        return {
            "points": [
                _pt("A", 0, 0, "A"), _pt("B", a, 0, "B"), _pt("C", t, 0, "C"),
                _pt("A2", 0, -1.4), _pt("C2", t, -1.4),
            ],
            "hidePoints": ["A2", "C2"],
            "objects": [
                {"kind": "segment", "from": "A", "to": "B", "label": str(a)},
                {"kind": "segment", "from": "B", "to": "C",
                 "label": part_b_label,
                 **({"color": "accent"} if part_b_label == "?" else {})},
                {"kind": "segment", "from": "A2", "to": "C2", "dashed": True,
                 "label": bar_label,
                 **({"color": "accent"} if bar_label == "?" else {"color": "blue"})},
            ],
        }

    for a, b in fwd:
        s = a + b
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(s), s),
            [(intL(abs(a - b)), abs(a - b)), (intL(b), b), (intL(a), a),
             (intL(s + 2), s + 2)],
            pos, latex_of=intL)
        out.append({
            "statement": "$B$ lies on segment $AC$ with $AB = %d$ and "
                         "$BC = %d$. Find $AC$." % (a, b),
            "options": opts, "correctIndex": ci,
            "explanation": "Since $B$ is between $A$ and $C$, the whole is the "
                           "sum of the parts: $AC = %d + %d = %d$. Subtracting "
                           "to get $%d$ is the classic slip — subtraction is "
                           "only for finding a missing part."
                           % (a, b, s, abs(a - b)),
            "check": ["%d + %d == %d" % (a, b, s)],
            "geoFigure": bar_fig(a, s, str(b), "?"),
        })
        idx += 1
    for t, a in rev:
        ans = t - a
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(ans), ans),
            [(intL(t + a), t + a), (intL(t), t), (intL(a), a),
             (intL(ans + 2), ans + 2)],
            pos, latex_of=intL)
        out.append({
            "statement": "$B$ lies on segment $AC$ with $AC = %d$ and "
                         "$AB = %d$. Find $BC$." % (t, a),
            "options": opts, "correctIndex": ci,
            "explanation": "A part is the whole minus the other part: "
                           "$BC = AC - AB = %d - %d = %d$. Adding to get $%d$ "
                           "treats the whole $AC$ as if it were another part."
                           % (t, a, ans, t + a),
            "check": ["%d - %d == %d" % (t, a, ans)],
            "geoFigure": bar_fig(a, t, "?", str(t)),
        })
        idx += 1
    return out


def gen_angpair():
    comp_a = [5, 10, 15, 20, 25, 30, 35, 40, 50, 55, 60, 65, 70, 75, 80, 85,
              12, 38]
    supp_a = [10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140, 150,
              160, 170, 45, 155]
    out = []
    idx = 0
    for kind, alist in (("comp", comp_a), ("supp", supp_a)):
        for a in alist:
            full = 90 if kind == "comp" else 180
            ans = full - a
            pos = idx % 4
            if kind == "comp":
                cands = [(degL(180 - a), 180 - a), (degL(a), a),
                         (degL(90 + a), 90 + a), (degL(180 + a), 180 + a)]
                st = ("Two angles are complementary. One of them measures "
                      "$%d°$. Find the other angle." % a)
                ex = ("Complementary angles add to $90°$, so the other is "
                      "$90° - %d° = %d°$. Subtracting from $180°$ "
                      "(supplementary) is the classic mix-up, giving $%d°$."
                      % (a, ans, 180 - a))
                chk = "90 - %d == %d" % (a, ans)
                third = (0.0, 6.0)
            else:
                slip = 90 - a if a < 90 else a - 90
                cands = [(degL(slip), slip), (degL(a), a),
                         (degL(360 - a), 360 - a), (degL(180 + a), 180 + a)]
                st = ("Two angles are supplementary. One of them measures "
                      "$%d°$. Find the other angle." % a)
                ex = ("Supplementary angles add to $180°$, so the other is "
                      "$180° - %d° = %d°$. Using $90°$ (complementary) is the "
                      "classic mix-up." % (a, ans))
                chk = "180 - %d == %d" % (a, ans)
                third = (-6.0, 0.0)
            opts, ci = build_latex_options((degL(ans), ans), cands, pos,
                                           latex_of=degL)
            ar = radians(a)
            fig = {
                "points": [
                    _pt("O", 0, 0), _pt("X", 6, 0),
                    _pt("M", 6 * cos(ar), 6 * sin(ar)),
                    _pt("T", third[0], third[1]),
                ],
                "hidePoints": ["O", "X", "M", "T"],
                "objects": [
                    {"kind": "ray", "from": "O", "to": "X"},
                    {"kind": "ray", "from": "O", "to": "M"},
                    {"kind": "ray", "from": "O", "to": "T"},
                    {"kind": "angle", "at": "O", "from": "X", "to": "M",
                     "label": "%d°" % a},
                    {"kind": "angle", "at": "O", "from": "M", "to": "T",
                     "label": "?", "color": "accent"},
                ],
            }
            out.append({"statement": st, "options": opts, "correctIndex": ci,
                        "explanation": ex, "check": [chk], "geoFigure": fig})
            idx += 1
    return out


def gen_vert():
    vals = [v for v in range(20, 161, 5) if v != 90]  # 28 values
    out = []
    idx = 0
    for kind, alist in (("vert", vals[:18]), ("lin", vals[10:])):
        for a in alist:
            pos = idx % 4
            slip = 90 - a if a < 90 else a - 90
            if kind == "vert":
                ans = a
                cands = [(degL(180 - a), 180 - a), (degL(slip), slip),
                         (degL(360 - a), 360 - a)]
                st = ("Two lines intersect. One of the angles formed measures "
                      "$%d°$. Find the measure of its vertical angle." % a)
                ex = ("Vertical angles are congruent, so it also measures "
                      "$%d°$. Subtracting from $180°$ gives $%d°$ — that is "
                      "the linear pair, not the vertical angle."
                      % (a, 180 - a))
                chk = "180 - (180 - %d) == %d" % (a, ans)
            else:
                ans = 180 - a
                cands = [(degL(a), a), (degL(slip), slip),
                         (degL(360 - a), 360 - a)]
                st = ("Two lines intersect. One of the angles formed measures "
                      "$%d°$. Find the measure of the angle that forms a "
                      "linear pair with it." % a)
                ex = ("A linear pair is supplementary: $180° - %d° = %d°$. "
                      "Answering $%d°$ unchanged is the vertical-angle slip."
                      % (a, ans, a))
                chk = "180 - %d == %d" % (a, ans)
            opts, ci = build_latex_options((degL(ans), ans), cands, pos,
                                           latex_of=degL)
            ar = radians(a)
            ux, uy = 6 * cos(ar), 6 * sin(ar)
            ask = ({"kind": "angle", "at": "O", "from": "W", "to": "D",
                    "label": "?", "color": "accent"} if kind == "vert" else
                   {"kind": "angle", "at": "O", "from": "U", "to": "W",
                    "label": "?", "color": "accent"})
            fig = {
                "points": [
                    _pt("O", 0, 0), _pt("E", 6, 0), _pt("W", -6, 0),
                    _pt("U", ux, uy), _pt("D", -ux, -uy),
                ],
                "hidePoints": ["O", "E", "W", "U", "D"],
                "objects": [
                    {"kind": "line", "from": "W", "to": "E"},
                    {"kind": "line", "from": "D", "to": "U"},
                    {"kind": "angle", "at": "O", "from": "E", "to": "U",
                     "label": "%d°" % a},
                    ask,
                ],
            }
            out.append({"statement": st, "options": opts, "correctIndex": ci,
                        "explanation": ex, "check": [chk], "geoFigure": fig})
            idx += 1
    return out


def gen_trans():
    avals = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 100, 105, 110, 115, 120,
             125, 130, 135, 140, 145]
    out = []
    idx = 0
    for kind, alist in (("corr", avals[0:12]), ("alt", avals[4:16]),
                        ("coint", avals[8:20])):
        for a in alist:
            pos = idx % 4
            slip = 90 - a if a < 90 else a - 90
            if kind == "corr":
                ans = a
                st = ("Two parallel lines are cut by a transversal. One angle "
                      "measures $%d°$. Find the measure of its corresponding "
                      "angle at the other intersection." % a)
                ex = ("Corresponding angles on parallel lines are congruent, "
                      "so it is $%d°$ again. Subtracting from $180°$ is only "
                      "correct for co-interior angles." % a)
                cands = [(degL(180 - a), 180 - a), (degL(slip), slip),
                         (degL(360 - a), 360 - a)]
                chk = "180 - (180 - %d) == %d" % (a, ans)
                ask = {"kind": "angle", "at": "Q2", "from": "B2", "to": "T2",
                       "label": "?", "color": "accent"}
            elif kind == "alt":
                ans = a
                st = ("Two parallel lines are cut by a transversal. An "
                      "interior angle measures $%d°$. Find the measure of the "
                      "alternate interior angle at the other intersection."
                      % a)
                ex = ("Alternate interior angles between parallel lines are "
                      "congruent, so it is $%d°$ again. Making them "
                      "supplementary ($%d°$) is the co-interior rule, not "
                      "this one." % (a, 180 - a))
                cands = [(degL(180 - a), 180 - a), (degL(slip), slip),
                         (degL(360 - a), 360 - a)]
                chk = "180 - (180 - %d) == %d" % (a, ans)
                ask = {"kind": "angle", "at": "Q2", "from": "B1", "to": "Q1",
                       "label": "?", "color": "accent"}
            else:
                ans = 180 - a
                st = ("Two parallel lines are cut by a transversal. An "
                      "interior angle measures $%d°$. Find the measure of the "
                      "co-interior angle on the same side of the transversal."
                      % a)
                ex = ("Co-interior (same-side interior) angles are "
                      "supplementary: $180° - %d° = %d°$. Calling them "
                      "congruent is the classic wrong move." % (a, ans))
                cands = [(degL(a), a), (degL(slip), slip),
                         (degL(360 - a), 360 - a)]
                chk = "180 - %d == %d" % (a, ans)
                ask = {"kind": "angle", "at": "Q2", "from": "B2", "to": "Q1",
                       "label": "?", "color": "accent"}
            opts, ci = build_latex_options((degL(ans), ans), cands, pos,
                                           latex_of=degL)
            ar = radians(a)
            q2x = 3 * cos(ar) / sin(ar)
            fig = {
                "points": [
                    _pt("A1", -5, 0), _pt("A2", 7, 0),
                    _pt("B1", -5, 3), _pt("B2", 7, 3),
                    _pt("Q1", 0, 0), _pt("Q2", q2x, 3),
                    _pt("T1", -2 * cos(ar), -2 * sin(ar)),
                    _pt("T2", q2x + 2 * cos(ar), 3 + 2 * sin(ar)),
                ],
                "hidePoints": ["A1", "A2", "B1", "B2", "Q1", "Q2", "T1", "T2"],
                "objects": [
                    {"kind": "line", "from": "A1", "to": "A2"},
                    {"kind": "line", "from": "B1", "to": "B2"},
                    {"kind": "line", "from": "T1", "to": "T2"},
                    {"kind": "angle", "at": "Q1", "from": "A2", "to": "Q2",
                     "label": "%d°" % a},
                    ask,
                ],
            }
            out.append({"statement": st, "options": opts, "correctIndex": ci,
                        "explanation": ex, "check": [chk], "geoFigure": fig})
            idx += 1
    return out


def gen_transx():
    coint = [(10, 24), (14, 30), (8, 42), (22, 36), (12, 48), (16, 54),
             (26, 40), (18, 62), (34, 52), (15, 29), (21, 37), (11, 45),
             (25, 41), (13, 57), (27, 49), (19, 63), (31, 55), (23, 69)]
    alt = [(7, 22), (11, 30), (9, 35), (13, 26), (5, 41), (17, 20), (3, 28),
           (8, 23), (12, 31), (6, 19), (10, 27), (14, 33), (4, 37), (15, 32),
           (18, 25), (2, 39), (16, 29), (1, 34)]
    out = []
    idx = 0
    for c, d in coint:
        assert (c + d) % 2 == 0 and c != d
        x = (180 - c - d) // 2
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(x), x),
            [(intL(180 - c - d), 180 - c - d), (intL(x + c), x + c),
             (intL(x + d), x + d)],
            pos, latex_of=intL)
        out.append({
            "statement": "Two parallel lines are cut by a transversal. The "
                         "co-interior angles measure $(x + %d)°$ and "
                         "$(x + %d)°$. Find $x$." % (c, d),
            "options": opts, "correctIndex": ci,
            "explanation": "Co-interior angles are supplementary: "
                           "$(x + %d) + (x + %d) = 180$, so $2x = %d$ and "
                           "$x = %d$. Forgetting to halve gives the classic "
                           "wrong answer $%d$."
                           % (c, d, 180 - c - d, x, 180 - c - d),
            "check": ["Rational(180 - %d - %d, 2) == %d" % (c, d, x)],
        })
        idx += 1
    for c, d in alt:
        x = c + d
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(x), x),
            [(intL(c + 2 * d), c + 2 * d), (intL(d - c), d - c),
             (intL(180 - c - d), 180 - c - d)],
            pos, latex_of=intL)
        out.append({
            "statement": "Two parallel lines are cut by a transversal. The "
                         "alternate interior angles measure $(2x - %d)°$ and "
                         "$(x + %d)°$. Find $x$." % (c, d),
            "options": opts, "correctIndex": ci,
            "explanation": "Alternate interior angles are equal: "
                           "$2x - %d = x + %d$, so $x = %d$. Setting the pair "
                           "supplementary instead of equal is the classic "
                           "wrong move." % (c, d, x),
            "check": ["2*%d - %d == %d + %d" % (x, c, x, d)],
        })
        idx += 1
    return out


def _tri_fig(a_deg, beta_deg, arcs, label_c="C"):
    """Triangle A(0,0)-B(6,0)-C true to the given interior angles at A and B.

    beta_deg is the interior angle at B; C is the ray intersection. `arcs` is
    a list of extra angle objects appended after the sides.
    """
    ar, br = radians(a_deg), radians(beta_deg)
    t = 6 * sin(ar) / sin(ar + br)
    cx, cy = 6 - t * cos(br), t * sin(br)
    pts = [_pt("A", 0, 0, "A"), _pt("B", 6, 0, "B"), _pt("C", cx, cy, label_c)]
    objs = [
        {"kind": "segment", "from": "A", "to": "B"},
        {"kind": "segment", "from": "A", "to": "C"},
        {"kind": "segment", "from": "B", "to": "C"},
    ]
    return pts, objs


def gen_angsum():
    pool = []
    for a in range(25, 115, 5):
        for b in range(30, 91, 6):
            if a != b and 25 <= 180 - a - b <= 115:
                pool.append((a, b))
    step = max(1, len(pool) // 36)
    picked = []
    for j in range(0, len(pool), step):
        picked.append(pool[j])
        if len(picked) == 36:
            break
    for p in pool:
        if len(picked) == 36:
            break
        if p not in picked:
            picked.append(p)

    out = []
    for i, (a, b) in enumerate(picked[:36]):
        ans = 180 - a - b
        pos = i % 4
        opts, ci = build_latex_options(
            (degL(ans), ans),
            [(degL(a + b), a + b), (degL(360 - a - b), 360 - a - b),
             (degL(180 - a), 180 - a), (degL(180 - b), 180 - b)],
            pos, latex_of=degL)
        pts, objs = _tri_fig(a, b, [])
        objs += [
            {"kind": "angle", "at": "A", "from": "B", "to": "C",
             "label": "%d°" % a},
            {"kind": "angle", "at": "B", "from": "A", "to": "C",
             "label": "%d°" % b},
            {"kind": "angle", "at": "C", "from": "A", "to": "B",
             "label": "?", "color": "accent"},
        ]
        out.append({
            "statement": "A triangle has angles $%d°$ and $%d°$. Find the "
                         "third angle." % (a, b),
            "options": opts, "correctIndex": ci,
            "explanation": "The angles of a triangle sum to $180°$: "
                           "$180° - %d° - %d° = %d°$. Adding the two givens "
                           "($%d°$) answers a different question."
                           % (a, b, ans, a + b),
            "check": ["180 - %d - %d == %d" % (a, b, ans)],
            "geoFigure": {"points": pts, "objects": objs},
        })
    return out


def gen_ext():
    fwd = [(30, 45), (35, 60), (40, 55), (45, 70), (50, 65), (55, 80),
           (60, 35), (65, 50), (70, 45), (75, 40), (80, 55), (85, 30),
           (28, 64), (32, 78), (46, 58), (52, 74), (66, 42), (74, 68)]
    rev = [(70, 30), (80, 35), (90, 40), (100, 45), (110, 50), (120, 55),
           (130, 60), (140, 65), (150, 70), (75, 28), (85, 32), (95, 52),
           (105, 64), (115, 42), (125, 58), (135, 72), (145, 88), (65, 26)]
    out = []
    idx = 0
    for a, b in fwd:
        ans = a + b
        assert ans < 180
        pos = idx % 4
        opts, ci = build_latex_options(
            (degL(ans), ans),
            [(degL(180 - a - b), 180 - a - b), (degL(360 - a - b), 360 - a - b),
             (degL(180 - a), 180 - a), (degL(180 - b), 180 - b)],
            pos, latex_of=degL)
        pts, objs = _tri_fig(a, 180 - a - b, [])
        pts.append(_pt("X", 9, 0))
        objs += [
            {"kind": "ray", "from": "B", "to": "X"},
            {"kind": "angle", "at": "A", "from": "B", "to": "C",
             "label": "%d°" % a},
            {"kind": "angle", "at": "C", "from": "A", "to": "B",
             "label": "%d°" % b},
            {"kind": "angle", "at": "B", "from": "X", "to": "C",
             "label": "?", "color": "accent"},
        ]
        out.append({
            "statement": "In a triangle, the two remote interior angles "
                         "measure $%d°$ and $%d°$. Find the exterior angle at "
                         "the third vertex." % (a, b),
            "options": opts, "correctIndex": ci,
            "explanation": "The exterior angle equals the sum of the two "
                           "remote interior angles: $%d° + %d° = %d°$. "
                           "Subtracting from $180°$ gives the interior angle "
                           "at that vertex instead." % (a, b, ans),
            "check": ["%d + %d == %d" % (a, b, ans)],
            "geoFigure": {"points": pts, "objects": objs,
                          "hidePoints": ["X"]},
        })
        idx += 1
    for e, a in rev:
        ans = e - a
        assert 0 < ans and e < 180 and a < e
        pos = idx % 4
        cands = [(degL(180 - e), 180 - e), (degL(180 - a), 180 - a)]
        if e + a < 180:
            cands.append((degL(e + a), e + a))
        opts, ci = build_latex_options((degL(ans), ans), cands, pos,
                                       latex_of=degL)
        pts, objs = _tri_fig(a, 180 - e, [])
        pts.append(_pt("X", 9, 0))
        objs += [
            {"kind": "ray", "from": "B", "to": "X"},
            {"kind": "angle", "at": "A", "from": "B", "to": "C",
             "label": "%d°" % a},
            {"kind": "angle", "at": "B", "from": "X", "to": "C",
             "label": "%d°" % e},
            {"kind": "angle", "at": "C", "from": "A", "to": "B",
             "label": "?", "color": "accent"},
        ]
        out.append({
            "statement": "An exterior angle of a triangle measures $%d°$, and "
                         "one remote interior angle measures $%d°$. Find the "
                         "other remote interior angle." % (e, a),
            "options": opts, "correctIndex": ci,
            "explanation": "The exterior angle is the sum of the two remote "
                           "interior angles, so the missing one is "
                           "$%d° - %d° = %d°$. Subtracting from $180°$ "
                           "instead gives the adjacent interior angle."
                           % (e, a, ans),
            "check": ["%d - %d == %d" % (e, a, ans)],
            "geoFigure": {"points": pts, "objects": objs,
                          "hidePoints": ["X"]},
        })
        idx += 1
    return out


def _mid_fig(K, mn_label, bc_label):
    ax, ay = 0.35 * K, 0.7 * K
    mx, my = ax / 2, ay / 2
    nx, ny = (ax + K) / 2, ay / 2
    mn = {"kind": "segment", "from": "M", "to": "N", "dashed": True,
          "label": mn_label}
    bc = {"kind": "segment", "from": "B", "to": "C", "label": bc_label}
    if mn_label == "?":
        mn["color"] = "accent"
    else:
        mn["color"] = "blue"
    if bc_label == "?":
        bc["color"] = "accent"
    return {
        "points": [
            _pt("B", 0, 0, "B"), _pt("C", K, 0, "C"), _pt("A", ax, ay, "A"),
            _pt("M", mx, my, "M"), _pt("N", nx, ny, "N"),
        ],
        "objects": [
            {"kind": "segment", "from": "B", "to": "M", "ticks": 1},
            {"kind": "segment", "from": "M", "to": "A", "ticks": 1},
            {"kind": "segment", "from": "A", "to": "N", "ticks": 2},
            {"kind": "segment", "from": "N", "to": "C", "ticks": 2},
            bc, mn,
        ],
    }


def gen_mid():
    out = []
    idx = 0
    for k in range(6, 41, 2):  # 18 even values
        ans = k // 2
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(ans), ans),
            [(intL(2 * k), 2 * k), (intL(k), k), (intL(ans + 2), ans + 2)],
            pos, latex_of=intL)
        out.append({
            "statement": "In triangle $ABC$, points $M$ and $N$ are the "
                         "midpoints of sides $AB$ and $AC$, and $BC = %d$. "
                         "Find the length of the midsegment $MN$." % k,
            "options": opts, "correctIndex": ci,
            "explanation": "A midsegment is parallel to the third side and "
                           "half as long: $MN = %d / 2 = %d$. Doubling to "
                           "$%d$ goes the wrong way." % (k, ans, 2 * k),
            "check": ["Rational(%d, 2) == %d" % (k, ans)],
            "geoFigure": _mid_fig(k, "?", str(k)),
        })
        idx += 1
    for m in range(4, 39, 2):  # 18 even values
        ans = 2 * m
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(ans), ans),
            [(intL(m // 2), m // 2), (intL(m), m), (intL(3 * m), 3 * m)],
            pos, latex_of=intL)
        out.append({
            "statement": "In triangle $ABC$, points $M$ and $N$ are the "
                         "midpoints of sides $AB$ and $AC$, and the midsegment "
                         "$MN = %d$. Find $BC$." % m,
            "options": opts, "correctIndex": ci,
            "explanation": "The third side is twice the midsegment: "
                           "$BC = 2 \\cdot %d = %d$. Halving again to get "
                           "$%d$ is the classic reversal." % (m, ans, m // 2),
            "check": ["2*%d == %d" % (m, ans)],
            "geoFigure": _mid_fig(2 * m, str(m), "?"),
        })
        idx += 1
    return out


def gen_trineq():
    pairs, seen, t = [], set(), 0
    while len(pairs) < 36 and t < 2000:
        a = 3 + (t % 11)
        b = a + 1 + ((t * 7) % 16)
        if b <= 29 and (a, b) not in seen:
            seen.add((a, b))
            pairs.append((a, b))
        t += 1
    assert len(pairs) == 36
    out = []
    for i, (a, b) in enumerate(pairs):
        lo, hi = b - a, a + b
        dvals = [lo + 1, b, hi - 1]
        assert len({hi, *dvals}) == 4, "trineq option collision %r" % ((a, b),)
        for d in dvals:
            assert lo < d < hi
        pos = i % 4
        opts = ["$%d$" % d for d in dvals]
        opts.insert(pos, "$%d$" % hi)
        assert len(set(opts)) == 4
        checks = ["%d + %d == %d" % (a, b, hi)]
        for d in dvals:
            checks.append("%d < %d + %d" % (d, a, b))
            checks.append("%d > %d - %d" % (d, b, a))
        out.append({
            "statement": "A triangle has sides $%d$ and $%d$. Which of these "
                         "CANNOT be the length of the third side?" % (a, b),
            "options": opts, "correctIndex": pos,
            "explanation": "The third side must be strictly between "
                           "$%d - %d = %d$ and $%d + %d = %d$. Exactly $%d$ "
                           "flattens the triangle into a segment — the "
                           "classic slip is allowing equality in the "
                           "triangle inequality." % (b, a, lo, a, b, hi, hi),
            "check": checks,
        })
    return out


def gen_poly():
    regular = [5, 6, 8, 9, 10, 12, 15, 18, 20]
    out = []
    idx = 0
    for n in range(5, 23):  # 18 sums
        ans = (n - 2) * 180
        pos = idx % 4
        opts, ci = build_latex_options(
            (degL(ans), ans),
            [(degL(n * 180), n * 180), (degL((n - 1) * 180), (n - 1) * 180),
             (degL((n - 3) * 180), (n - 3) * 180)],
            pos, latex_of=degL)
        out.append({
            "statement": "Find the sum of the interior angles of a convex "
                         "$%d$-gon." % n,
            "options": opts, "correctIndex": ci,
            "explanation": "An $n$-gon splits into $n - 2$ triangles, so the "
                           "sum is $(%d - 2) \\cdot 180° = %d°$. Using "
                           "$n \\cdot 180°$ forgets the $-2$." % (n, ans),
            "check": ["(%d - 2)*180 == %d" % (n, ans)],
        })
        idx += 1
    for n in regular:  # 9 each-interior
        ans = (n - 2) * 180 // n
        assert (n - 2) * 180 % n == 0
        pos = idx % 4
        opts, ci = build_latex_options(
            (degL(ans), ans),
            [(degL(360 // n), 360 // n), (degL((n - 2) * 180), (n - 2) * 180),
             (degL(180), 180)],
            pos, latex_of=degL)
        out.append({
            "statement": "Find the measure of each interior angle of a "
                         "regular $%d$-gon." % n,
            "options": opts, "correctIndex": ci,
            "explanation": "Each interior angle is "
                           "$\\frac{(%d - 2) \\cdot 180°}{%d} = %d°$. "
                           "$%d°$ is the exterior angle — the classic swap."
                           % (n, n, ans, 360 // n),
            "check": ["Rational((%d - 2)*180, %d) == %d" % (n, n, ans)],
        })
        idx += 1
    for n in regular:  # 9 each-exterior
        ans = 360 // n
        assert 360 % n == 0
        pos = idx % 4
        opts, ci = build_latex_options(
            (degL(ans), ans),
            [(degL((n - 2) * 180 // n), (n - 2) * 180 // n),
             (degL(360), 360), (degL(180 // n if 180 % n == 0 else n), 180 // n if 180 % n == 0 else n)],
            pos, latex_of=degL)
        out.append({
            "statement": "Find the measure of each exterior angle of a "
                         "regular $%d$-gon." % n,
            "options": opts, "correctIndex": ci,
            "explanation": "Exterior angles of any convex polygon sum to "
                           "$360°$, so each is $\\frac{360°}{%d} = %d°$. "
                           "$%d°$ is the interior angle — the classic swap."
                           % (n, ans, (n - 2) * 180 // n),
            "check": ["Rational(360, %d) == %d" % (n, ans)],
        })
        idx += 1
    return out


def _para_fig(a, ask_at):
    ar = radians(a)
    dx, dy = 3.2 * cos(ar), 3.2 * sin(ar)
    ask = ({"kind": "angle", "at": "B", "from": "A", "to": "C",
            "label": "?", "color": "accent"} if ask_at == "B" else
           {"kind": "angle", "at": "C", "from": "B", "to": "D",
            "label": "?", "color": "accent"})
    return {
        "points": [
            _pt("A", 0, 0, "A"), _pt("B", 6, 0, "B"),
            _pt("C", 6 + dx, dy, "C"), _pt("D", dx, dy, "D"),
        ],
        "objects": [
            {"kind": "segment", "from": "A", "to": "B"},
            {"kind": "segment", "from": "B", "to": "C"},
            {"kind": "segment", "from": "C", "to": "D"},
            {"kind": "segment", "from": "D", "to": "A"},
            {"kind": "angle", "at": "A", "from": "B", "to": "D",
             "label": "%d°" % a},
            ask,
        ],
    }


def gen_para():
    a_vals = [35, 40, 50, 55, 65, 70, 75, 80, 95, 100, 110, 115]
    b_vals = [38, 44, 52, 58, 64, 76, 84, 98, 104, 116, 124, 132]
    k_vals = [3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17]
    out = []
    idx = 0
    for a in a_vals:
        ans = 180 - a
        pos = idx % 4
        opts, ci = build_latex_options(
            (degL(ans), ans),
            [(degL(a), a), (degL(90), 90), (degL(360 - a), 360 - a)],
            pos, latex_of=degL)
        out.append({
            "statement": "In parallelogram $ABCD$, $\\angle A = %d°$. Find "
                         "$\\angle B$." % a,
            "options": opts, "correctIndex": ci,
            "explanation": "Consecutive angles of a parallelogram are "
                           "supplementary: $\\angle B = 180° - %d° = %d°$. "
                           "Equal angles ($%d°$) are the opposite ones, like "
                           "$\\angle C$." % (a, ans, a),
            "check": ["180 - %d == %d" % (a, ans)],
            "geoFigure": _para_fig(a, "B"),
        })
        idx += 1
    for a in b_vals:
        pos = idx % 4
        opts, ci = build_latex_options(
            (degL(a), a),
            [(degL(180 - a), 180 - a), (degL(90), 90),
             (degL(360 - a), 360 - a)],
            pos, latex_of=degL)
        out.append({
            "statement": "In parallelogram $ABCD$, $\\angle A = %d°$. Find "
                         "$\\angle C$." % a,
            "options": opts, "correctIndex": ci,
            "explanation": "Opposite angles of a parallelogram are equal, so "
                           "$\\angle C = %d°$. Subtracting from $180°$ gives "
                           "the consecutive angle $\\angle B$ instead."
                           % a,
            "check": ["180 - (180 - %d) == %d" % (a, a)],
            "geoFigure": _para_fig(a, "C"),
        })
        idx += 1
    for k in k_vals:
        ans = 2 * k
        pos = idx % 4
        opts, ci = build_latex_options(
            (intL(ans), ans),
            [(intL(k), k), (intL(3 * k), 3 * k), (intL(4 * k), 4 * k)],
            pos, latex_of=intL)
        out.append({
            "statement": "In parallelogram $ABCD$, the diagonals intersect at "
                         "$O$ and $AO = %d$. Find the diagonal $AC$." % k,
            "options": opts, "correctIndex": ci,
            "explanation": "The diagonals of a parallelogram bisect each "
                           "other, so $O$ is the midpoint of $AC$ and "
                           "$AC = 2 \\cdot %d = %d$. Answering $%d$ forgets "
                           "that $AO$ is only half the diagonal."
                           % (k, ans, k),
            "check": ["2*%d == %d" % (k, ans)],
        })
        idx += 1
    return out


def gen_simarea():
    ratios = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5), (4, 5),
              (1, 5), (2, 7), (5, 6), (1, 6)]
    out = []
    idx = 0
    for i, (j, k) in enumerate(ratios):
        for m in (i % 4 + 2, i % 4 + 6):
            S = j * j * m
            A2 = k * k * m
            pos = idx % 4
            opts, ci = build_latex_options(
                (intL(A2), A2),
                [(intL(j * k * m), j * k * m),
                 (intL(S * (k - j) ** 2), S * (k - j) ** 2),
                 (intL(S + k * k), S + k * k)],
                pos, latex_of=intL)
            out.append({
                "statement": "Two similar triangles have similarity ratio "
                             "$%d : %d$ (smaller to larger). The smaller "
                             "triangle has area $%d$. Find the area of the "
                             "larger triangle." % (j, k, S),
                "options": opts, "correctIndex": ci,
                "explanation": "Areas of similar figures scale by the "
                               "SQUARE of the ratio: "
                               "$%d \\cdot \\left(\\frac{%d}{%d}\\right)^2 = "
                               "%d$. Multiplying by just $\\frac{%d}{%d}$ — "
                               "the classic slip — treats area like a length "
                               "and gives $%d$."
                               % (S, k, j, A2, k, j, j * k * m),
                "check": ["Rational(%d**2, %d**2)*%d == %d" % (k, j, S, A2)],
            })
            idx += 1
    for i, (j, k) in enumerate(ratios):
        m = i % 3 + 2
        A1, A2 = j * j * m, k * k * m
        ratio = Rational(k, j)
        pos = idx % 4
        opts, ci = build_latex_options(
            (L(ratio), ratio),
            [(L(Rational(k * k, j * j)), Rational(k * k, j * j)),
             (L(Rational(k * k - j * j, j * j)), Rational(k * k - j * j, j * j)),
             (L(Rational(k + j, j)), Rational(k + j, j))],
            pos, latex_of=L)
        out.append({
            "statement": "Two similar triangles have areas $%d$ and $%d$. "
                         "Find their similarity ratio, larger to smaller."
                         % (A1, A2),
            "options": opts, "correctIndex": ci,
            "explanation": "The similarity ratio is the square ROOT of the "
                           "area ratio: $\\sqrt{\\frac{%d}{%d}} = %s$. "
                           "Quoting the raw area ratio $%s$ skips the square "
                           "root." % (A2, A1, L(ratio),
                                      L(Rational(k * k, j * j))),
            "check": ["sqrt(Rational(%d, %d)) == Rational(%d, %d)"
                      % (A2, A1, k, j)],
        })
        idx += 1
    return out


def gen_trap():
    pool = []
    for a in range(8, 21):
        for b in range(3, a - 2):
            for h in range(3, 11):
                if (a + b) * h % 2 == 0:
                    pool.append((a, b, h))
    step = max(1, len(pool) // 36)
    picked = []
    for j in range(0, len(pool), step):
        picked.append(pool[j])
        if len(picked) == 36:
            break
    for p in pool:
        if len(picked) == 36:
            break
        if p not in picked:
            picked.append(p)

    out = []
    for i, (a, b, h) in enumerate(picked[:36]):
        ans = (a + b) * h // 2
        pos = i % 4
        opts, ci = build_latex_options(
            (intL(ans), ans),
            [(intL((a + b) * h), (a + b) * h), (intL(a * h), a * h),
             (intL((a - b) * h // 2), (a - b) * h // 2)],
            pos, latex_of=intL)
        x0 = 0.4 * (a - b)
        fx = x0 + 0.45 * b
        fig = {
            "points": [
                _pt("P", 0, 0), _pt("Q", a, 0), _pt("R", x0 + b, h),
                _pt("S", x0, h), _pt("F", fx, 0), _pt("H", fx, h),
            ],
            "hidePoints": ["P", "Q", "R", "S", "F", "H"],
            "objects": [
                {"kind": "segment", "from": "P", "to": "Q", "label": str(a)},
                {"kind": "segment", "from": "S", "to": "R", "label": str(b)},
                {"kind": "segment", "from": "P", "to": "S"},
                {"kind": "segment", "from": "Q", "to": "R"},
                {"kind": "segment", "from": "F", "to": "H", "label": str(h),
                 "color": "blue", "dashed": True},
                {"kind": "angle", "at": "F", "from": "Q", "to": "H",
                 "right": True},
            ],
        }
        out.append({
            "statement": "A trapezoid has parallel sides $%d$ and $%d$ and "
                         "height $%d$. Find its area." % (a, b, h),
            "options": opts, "correctIndex": ci,
            "explanation": "Average the parallel sides, then multiply by the "
                           "height: $\\frac{%d + %d}{2} \\cdot %d = %d$. "
                           "Forgetting the $\\tfrac12$ gives $%d$."
                           % (a, b, h, ans, (a + b) * h),
            "check": ["Rational(%d + %d, 2)*%d == %d" % (a, b, h, ans)],
            "geoFigure": fig,
        })
    return out


def gen_tpoint():
    trans_data = [(3, -4, 2, 5), (1, 6, 4, -3), (-2, 5, 3, 4), (4, -1, -5, 2),
                  (-3, -6, 7, 4), (5, 2, -3, 6), (-4, 7, 2, -5),
                  (6, -3, -4, -2), (2, 8, 5, -7), (-5, -2, 6, 3),
                  (7, 1, -2, 4), (-1, -7, 3, 5), (8, -5, -6, 2),
                  (-6, 4, 5, -3), (3, 7, -4, -6)]
    refl_x = [(3, -4), (-2, 5), (6, 1), (-7, -3), (4, 9), (-5, 8), (2, -7)]
    refl_y = [(1, 4), (-3, 7), (5, -2), (-6, -8), (7, 3), (-8, 2), (4, -5)]
    refl_o = [(2, 5), (-4, 1), (3, -8), (-6, 7), (8, -3), (-1, -6), (5, 4)]
    out = []
    idx = 0
    for x, y, dx, dy in trans_data:
        nx, ny = x + dx, y + dy
        pos = idx % 4
        opts, ci = _pair_opts(
            "tpoint-trans", (nx, ny),
            [(x - dx, y - dy), (x + dy, y + dx), (x + dx, y - dy),
             (x - dx, y + dy)], pos)
        out.append({
            "statement": "The point $(%d; %d)$ is translated by the vector "
                         "$(%d; %d)$. Find the image." % (x, y, dx, dy),
            "options": opts, "correctIndex": ci,
            "explanation": "Add the vector to each coordinate: "
                           "$(%d + %d; %d + %d) = (%d; %d)$. Subtracting the "
                           "vector moves the point the wrong way."
                           % (x, dx, y, dy, nx, ny),
            "check": ["(%d) + (%d) == (%d)" % (x, dx, nx),
                      "(%d) + (%d) == (%d)" % (y, dy, ny)],
        })
        idx += 1
    for kind, data in (("x", refl_x), ("y", refl_y), ("o", refl_o)):
        for x, y in data:
            pos = idx % 4
            if kind == "x":
                nxy = (x, -y)
                cands = [(-x, y), (-x, -y), (y, x)]
                st = ("The point $(%d; %d)$ is reflected over the $x$-axis. "
                      "Find the image." % (x, y))
                ex = ("Reflecting over the $x$-axis keeps $x$ and flips the "
                      "sign of $y$: $(%d; %d)$. Flipping $x$ instead "
                      "reflects over the $y$-axis." % nxy)
                chk = ["(%d) == (%d)" % (x, x), "-(%d) == (%d)" % (y, -y)]
            elif kind == "y":
                nxy = (-x, y)
                cands = [(x, -y), (-x, -y), (y, x)]
                st = ("The point $(%d; %d)$ is reflected over the $y$-axis. "
                      "Find the image." % (x, y))
                ex = ("Reflecting over the $y$-axis flips the sign of $x$ and "
                      "keeps $y$: $(%d; %d)$. Flipping $y$ instead reflects "
                      "over the $x$-axis." % nxy)
                chk = ["-(%d) == (%d)" % (x, -x), "(%d) == (%d)" % (y, y)]
            else:
                nxy = (-x, -y)
                cands = [(x, -y), (-x, y), (y, x)]
                st = ("The point $(%d; %d)$ is reflected through the origin. "
                      "Find the image." % (x, y))
                ex = ("Reflecting through the origin flips BOTH signs: "
                      "$(%d; %d)$. Flipping only one sign is an axis "
                      "reflection, not a point reflection." % nxy)
                chk = ["-(%d) == (%d)" % (x, -x), "-(%d) == (%d)" % (y, -y)]
            opts, ci = _pair_opts("tpoint-" + kind, nxy, cands, pos)
            out.append({"statement": st, "options": opts, "correctIndex": ci,
                        "explanation": ex, "check": chk})
            idx += 1
    return out


def gen_trot():
    rpts = [(3, -5), (2, 7), (-4, 1), (-6, -3), (5, 2), (-7, 4), (1, -8),
            (8, 3), (-2, -9), (6, -1), (-5, 8), (4, -7)]
    out = []
    idx = 0
    for ang in (90, 180, 270):
        for x, y in rpts:
            if ang == 90:
                nxy = (-y, x)
                cands = [(-x, -y), (y, -x), (-y, -x)]
                rule = "(-y;\\ x)"
                slip = (y, -x)
            elif ang == 180:
                nxy = (-x, -y)
                cands = [(-y, x), (y, -x), (x, -y)]
                rule = "(-x;\\ -y)"
                slip = (x, -y)
            else:
                nxy = (y, -x)
                cands = [(-y, x), (-x, -y), (-y, -x)]
                rule = "(y;\\ -x)"
                slip = (-y, x)
            pos = idx % 4
            opts, ci = _pair_opts("trot-%d" % ang, nxy, cands, pos)
            if ang == 180:
                ex = ("A $180°$ rotation flips both signs: $(x; y) \\to "
                      "%s$, so the image is $(%d; %d)$. Flipping only one "
                      "coordinate, like $(%d; %d)$, is a reflection, not a "
                      "rotation." % (rule, nxy[0], nxy[1], slip[0], slip[1]))
            else:
                ex = ("A $%d°$ counterclockwise rotation sends $(x; y) \\to "
                      "%s$, so the image is $(%d; %d)$. Rotating clockwise "
                      "by mistake gives $(%d; %d)$."
                      % (ang, rule, nxy[0], nxy[1], slip[0], slip[1]))
            out.append({
                "statement": "The point $(%d; %d)$ is rotated $%d°$ "
                             "counterclockwise about the origin. Find the "
                             "image." % (x, y, ang),
                "options": opts, "correctIndex": ci,
                "explanation": ex,
                "check": ["cos(rad(%d))*(%d) - sin(rad(%d))*(%d) == (%d)"
                          % (ang, x, ang, y, nxy[0]),
                          "sin(rad(%d))*(%d) + cos(rad(%d))*(%d) == (%d)"
                          % (ang, x, ang, y, nxy[1])],
            })
            idx += 1
    return out


def gen_midp():
    combos, seen, t = [], set(), 0
    while len(combos) < 36 and t < 20000:
        x1 = ((t * 5) % 17) - 8
        y1 = ((t * 7) % 15) - 7
        x2 = x1 + 2 * (((t * 3) % 9) - 4)
        y2 = y1 + 2 * (((t * 11) % 9) - 4)
        t += 1
        if (x1, y1) == (x2, y2) or abs(x2) > 9 or abs(y2) > 9:
            continue
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        if (mx, my) == (0, 0) or mx == my:
            continue
        d1 = ((x2 - x1) // 2, (y2 - y1) // 2)
        d2 = (x1 + x2, y1 + y2)
        d3 = (my, mx)
        if len({(mx, my), d1, d2, d3}) < 4:
            continue
        key = (x1, y1, x2, y2)
        if key in seen:
            continue
        seen.add(key)
        combos.append((x1, y1, x2, y2, mx, my, d1, d2, d3))
    assert len(combos) == 36
    out = []
    for i, (x1, y1, x2, y2, mx, my, d1, d2, d3) in enumerate(combos):
        pos = i % 4
        opts, ci = _pair_opts("midp", (mx, my), [d1, d2, d3], pos)
        out.append({
            "statement": "Find the midpoint of the segment from $(%d; %d)$ "
                         "to $(%d; %d)$." % (x1, y1, x2, y2),
            "options": opts, "correctIndex": ci,
            "explanation": "Average the endpoints: $\\left(\\frac{%d + %d}"
                           "{2}; \\frac{%d + %d}{2}\\right) = (%d; %d)$. "
                           "Adding without halving gives $(%d; %d)$."
                           % (x1, x2, y1, y2, mx, my, d2[0], d2[1]),
            "check": ["Rational((%d) + (%d), 2) == (%d)" % (x1, x2, mx),
                      "Rational((%d) + (%d), 2) == (%d)" % (y1, y2, my)],
        })
    return out


def gen_dist():
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17),
               (12, 16, 20), (7, 24, 25), (20, 21, 29), (10, 24, 26),
               (15, 20, 25), (18, 24, 30), (16, 30, 34)]
    out = []
    idx = 0
    for i, (a, b, c) in enumerate(triples):
        for cfg in range(3):
            x1 = (i % 5) - 2 + cfg
            y1 = ((i * 2) % 7) - 3 - cfg
            sx = 1 if (i + cfg) % 2 == 0 else -1
            sy = 1 if cfg % 2 == 0 else -1
            dx, dy = (a, b) if cfg != 1 else (b, a)
            x2, y2 = x1 + sx * dx, y1 + sy * dy
            pos = idx % 4
            opts, ci = build_latex_options(
                (intL(c), c),
                [(intL(a + b), a + b), (intL(c + 1), c + 1),
                 (intL(c - 1), c - 1)],
                pos, latex_of=intL)
            out.append({
                "statement": "Find the distance between the points "
                             "$(%d; %d)$ and $(%d; %d)$." % (x1, y1, x2, y2),
                "options": opts, "correctIndex": ci,
                "explanation": "Distance formula: $\\sqrt{(%d)^2 + (%d)^2} = "
                               "\\sqrt{%d} = %d$ — the %d-%d-%d triple. "
                               "Adding the legs to get $%d$ skips the "
                               "squaring." % (sx * dx, sy * dy, c * c, c,
                                              a, b, c, a + b),
                "check": ["sqrt(((%d) - (%d))**2 + ((%d) - (%d))**2) == %d"
                          % (x2, x1, y2, y1, c)],
            })
            idx += 1
    return out


# ---------------------------------------------------------------------------
# assembly of the new forms
# ---------------------------------------------------------------------------

NEW_FORMS_META = [
    ("segment-addition", "Segment addition", 1, "GEO-segadd",
     "foundations", gen_segadd),
    ("angle-pairs", "Complementary & supplementary angles", 1, "GEO-angpair",
     "foundations", gen_angpair),
    ("vertical-linear-angles", "Vertical angles & linear pairs", 2,
     "GEO-vert", "reasoning-and-proof", gen_vert),
    ("transversal-angles", "Angles with parallel lines", 1, "GEO-trans",
     "parallel-and-perpendicular", gen_trans),
    ("transversal-solve", "Solving with transversal angles", 2, "GEO-transx",
     "parallel-and-perpendicular", gen_transx),
    ("triangle-angle-sum", "The triangle angle sum", 1, "GEO-angsum",
     "triangles-and-congruence", gen_angsum),
    ("exterior-angle", "The exterior angle theorem", 2, "GEO-ext",
     "triangles-and-congruence", gen_ext),
    ("midsegment", "The midsegment theorem", 2, "GEO-mid",
     "relationships-in-triangles", gen_mid),
    ("triangle-inequality", "The triangle inequality", 2, "GEO-trineq",
     "relationships-in-triangles", gen_trineq),
    ("polygon-angles", "Polygon angle measures", 1, "GEO-poly",
     "quadrilaterals-and-polygons", gen_poly),
    ("parallelogram-solve", "Parallelogram properties", 2, "GEO-para",
     "quadrilaterals-and-polygons", gen_para),
    ("similar-area-ratio", "Areas of similar figures", 3, "GEO-simarea",
     "similarity", gen_simarea),
    ("trapezoid-area", "Trapezoid area", 2, "GEO-trap",
     "area-and-perimeter", gen_trap),
    ("transform-point", "Translations & reflections", 1, "GEO-tpoint",
     "transformations", gen_tpoint),
    ("rotate-point", "Rotations about the origin", 2, "GEO-trot",
     "transformations", gen_trot),
    ("midpoint", "The midpoint formula", 1, "GEO-midp",
     "coordinate-geometry", gen_midp),
    ("distance-points", "The distance formula", 2, "GEO-dist",
     "coordinate-geometry", gen_dist),
]


def new_forms():
    """Unit-specific forms authored for this subject (appended by unit)."""
    forms = []
    for form_id, title, level, skill, unit, gen in NEW_FORMS_META:
        raw = gen()
        assert len(raw) >= 34, "%s: only %d variants" % (form_id, len(raw))
        variants = []
        for i, v in enumerate(raw):
            vd = {"id": "%s-v%02d" % (skill, i + 1)}
            vd.update(v)
            variants.append(vd)
        forms.append({"id": form_id, "title": title, "level": level,
                      "skill": skill, "unit": unit, "variants": variants})
    return forms


# ---------------------------------------------------------------------------
# independent re-solvers (regex the statement, recompute from scratch)
# ---------------------------------------------------------------------------

def _r_segadd(s):
    a = int(re.search(r"AB = (\d+)", s).group(1))
    if "Find $AC$" in s:
        b = int(re.search(r"BC = (\d+)", s).group(1))
        return ("num", a + b)
    t = int(re.search(r"AC = (\d+)", s).group(1))
    return ("num", t - a)


def _r_angpair(s):
    a = int(re.search(r"measures \$(\d+)°\$", s).group(1))
    return ("num", (90 if "complementary" in s else 180) - a)


def _r_vert(s):
    a = int(re.search(r"measures \$(\d+)°\$", s).group(1))
    return ("num", a if "vertical" in s else 180 - a)


def _r_trans(s):
    a = int(re.search(r"measures \$(\d+)°\$", s).group(1))
    return ("num", 180 - a if "co-interior" in s else a)


def _r_transx(s):
    if "co-interior" in s:
        c, d = [int(x) for x in re.findall(r"\(x \+ (\d+)\)°", s)]
        return ("num", Rational(180 - c - d, 2))
    c = int(re.search(r"\(2x - (\d+)\)°", s).group(1))
    d = int(re.search(r"\(x \+ (\d+)\)°", s).group(1))
    return ("num", c + d)


def _r_angsum(s):
    a, b = [int(x) for x in re.findall(r"\$(\d+)°\$", s)]
    return ("num", 180 - a - b)


def _r_ext(s):
    nums = [int(x) for x in re.findall(r"\$(\d+)°\$", s)]
    if "Find the exterior angle" in s:
        return ("num", nums[0] + nums[1])
    return ("num", nums[0] - nums[1])


def _r_mid(s):
    m = re.search(r"MN = (\d+)", s)
    if m:
        return ("num", 2 * int(m.group(1)))
    k = int(re.search(r"BC = (\d+)", s).group(1))
    return ("num", Rational(k, 2))


def _r_trineq(s):
    a, b = [int(x) for x in re.findall(r"\$(\d+)\$", s)[:2]]
    return ("opt", "$%d$" % (a + b))


def _r_poly(s):
    n = int(re.search(r"\$(\d+)\$-gon", s).group(1))
    if "sum of the interior" in s:
        return ("num", (n - 2) * 180)
    if "each interior" in s:
        return ("num", Rational((n - 2) * 180, n))
    return ("num", Rational(360, n))


def _r_para(s):
    m = re.search(r"AO = (\d+)", s)
    if m:
        return ("num", 2 * int(m.group(1)))
    a = int(re.search(r"angle A = (\d+)°", s).group(1))
    if "Find $\\angle B$" in s:
        return ("num", 180 - a)
    return ("num", a)


def _r_simarea(s):
    m = re.search(r"similarity ratio \$(\d+) : (\d+)\$", s)
    if m:
        j, k = int(m.group(1)), int(m.group(2))
        S = int(re.search(r"has area \$(\d+)\$", s).group(1))
        return ("num", Rational(k * k, j * j) * S)
    a1, a2 = [int(x) for x in
              re.search(r"areas \$(\d+)\$ and \$(\d+)\$", s).groups()]
    return ("num", sqrt(Rational(a2, a1)))


def _r_trap(s):
    a, b = [int(x) for x in
            re.search(r"parallel sides \$(\d+)\$ and \$(\d+)\$", s).groups()]
    h = int(re.search(r"height \$(\d+)\$", s).group(1))
    return ("num", Rational((a + b) * h, 2))


def _r_tpoint(s):
    pairs = [(int(x), int(y)) for x, y in
             re.findall(r"\((-?\d+); (-?\d+)\)", s)]
    x, y = pairs[0]
    if "translated" in s:
        dx, dy = pairs[1]
        return ("opt", _pair_str(x + dx, y + dy))
    if "$x$-axis" in s:
        return ("opt", _pair_str(x, -y))
    if "$y$-axis" in s:
        return ("opt", _pair_str(-x, y))
    return ("opt", _pair_str(-x, -y))


def _r_trot(s):
    x, y = [int(v) for v in
            re.search(r"\((-?\d+); (-?\d+)\)", s).groups()]
    ang = int(re.search(r"rotated \$(\d+)°\$", s).group(1))
    if ang == 90:
        return ("opt", _pair_str(-y, x))
    if ang == 180:
        return ("opt", _pair_str(-x, -y))
    return ("opt", _pair_str(y, -x))


def _r_midp(s):
    (x1, y1), (x2, y2) = [(int(x), int(y)) for x, y in
                          re.findall(r"\((-?\d+); (-?\d+)\)", s)]
    return ("opt", _pair_str((x1 + x2) // 2, (y1 + y2) // 2))


def _r_dist(s):
    (x1, y1), (x2, y2) = [(int(x), int(y)) for x, y in
                          re.findall(r"\((-?\d+); (-?\d+)\)", s)]
    return ("num", sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


RESOLVERS.update({
    "segment-addition": _r_segadd,
    "angle-pairs": _r_angpair,
    "vertical-linear-angles": _r_vert,
    "transversal-angles": _r_trans,
    "transversal-solve": _r_transx,
    "triangle-angle-sum": _r_angsum,
    "exterior-angle": _r_ext,
    "midsegment": _r_mid,
    "triangle-inequality": _r_trineq,
    "polygon-angles": _r_poly,
    "parallelogram-solve": _r_para,
    "similar-area-ratio": _r_simarea,
    "trapezoid-area": _r_trap,
    "transform-point": _r_tpoint,
    "rotate-point": _r_trot,
    "midpoint": _r_midp,
    "distance-points": _r_dist,
})


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = _remapped_forms() + new_forms()
    for f in forms:
        assert f["unit"] in unit_order, "%s: unknown unit %r" % (f["id"], f["unit"])
    forms.sort(key=lambda f: (unit_order[f["unit"]], f["level"], f["id"]))
    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    data = build()
    total = sum(len(f["variants"]) for f in data["forms"])
    per_unit = {u["id"]: 0 for u in UNITS}
    for f in data["forms"]:
        per_unit[f["unit"]] += len(f["variants"])
    ids = [v["id"] for f in data["forms"] for v in f["variants"]]
    assert len(ids) == len(set(ids)), "variant ids not unique"
    empty = [u for u, n in per_unit.items() if n == 0]
    print("SELFCHECK OK  forms=%d  total=%d  units=%d  empty_units=%s"
          % (len(data["forms"]), total, len(UNITS), ",".join(empty) or "none"))
