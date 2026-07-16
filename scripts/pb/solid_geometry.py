# -*- coding: utf-8 -*-
"""Problem-bank subject: Solid Geometry — mirrors the /math/solid-geometry course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/solid_geometry.py` for the self-check.
"""
import importlib.util
import os
import re
from math import factorial, gcd

from sympy import Rational, pi, simplify, sqrt, sympify

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "solid-geometry"
TITLE = "Solid Geometry"
TITLE_MN = "Огторгуйн геометр"
BLURB = ("Unit-by-unit practice for the Solid Geometry course — lines and planes in space through spheres and similar solids.")

UNITS = [
    {"id": "lines-and-planes-in-space", "title": "Lines & Planes in Space",
     "blurb": "The rules of 3D: what determines a plane, skew lines, perpendicularity, and the two angles every exam measures."},
    {"id": "prisms-and-the-cube", "title": "Prisms & the Cube",
     "blurb": "The box family: prism anatomy, the cube's √2 and √3 diagonals, and surface & volume you can see face by face."},
    {"id": "pyramids", "title": "Pyramids",
     "blurb": "Height, apothem, slant, edge — the two Pythagorean triangles inside every pyramid, the ⅓ in the volume, and the frustum."},
    {"id": "cylinders-and-cones", "title": "Cylinders & Cones",
     "blurb": "The round solids you can unroll: the cylinder's rectangle label, the cone's pie-slice development, and both volumes."},
    {"id": "spheres", "title": "Spheres",
     "blurb": "Every slice a circle (r² = R² − d²), the surface of exactly four great circles, and Archimedes' tombstone 2:3."},
    {"id": "cross-sections-and-similar-solids", "title": "Cross-Sections & Similar Solids",
     "blurb": "Predict any cut, scale with k / k² / k³, glue and drill combined solids — and the five-triangle exam strategy."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "space-diagonal": "prisms-and-the-cube",
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
# formatting helpers (house style — copied from scripts/pb/geometry.py)
# ---------------------------------------------------------------------------

def L(v):
    """LaTeX for an integer/rational value (no surrounding $)."""
    v = sympify(v)
    if getattr(v, "q", 1) == 1:
        return str(v.p if hasattr(v, "p") else int(v))
    if v < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def intL(v):
    return str(int(v))


def piL(k):
    """LaTeX for k*pi."""
    k = sympify(k)
    if k == 0:
        return "0"
    if k == 1:
        return "\\pi"
    if k == -1:
        return "-\\pi"
    return L(k) + "\\pi"


def surd(coef, base):
    """LaTeX for coef*sqrt(base) with integer coef>=1."""
    coef = int(coef)
    if coef == 1:
        return "\\sqrt{%d}" % base
    return "%d\\sqrt{%d}" % (coef, base)


def build_latex_options(correct, cands, pos, latex_of=None):
    """correct = (latex, value); cands = list of (latex, value).

    Returns (options[4] wrapped in $...$, correctIndex=pos). Guarantees the
    three chosen distractors are numerically distinct from the correct answer
    and from each other, and have distinct latex. Crashes on collision
    shortage.
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
    return ["$" + s + "$" for s in final], pos


def _pi_buffer(k):
    """Always-valid filler distractors around k*pi, so pi-valued forms never
    reach the integer +/- fallback (which cannot latex a pi multiple)."""
    return [(piL(k + d), (k + d) * pi) for d in (1, 2, 3)]


def _pick_spread(items, want=36):
    """Spread-pick `want` items across the list (geometry.py house pattern)."""
    step = max(1, len(items) // want)
    picked = list(items[::step][:want])
    for it in items:
        if len(picked) >= want:
            break
        if it not in picked:
            picked.append(it)
    return picked[:want]


def _rt_fig(w, h, wl, hl):
    """Extracted right triangle, true to scale: right angle at the origin,
    horizontal leg w (labeled wl), vertical leg h (labeled hl, blue),
    hypotenuse '?' in the accent color."""
    return {
        "points": [
            {"id": "A", "x": 0, "y": 0, "label": ""},
            {"id": "B", "x": w, "y": 0, "label": ""},
            {"id": "C", "x": 0, "y": h, "label": ""},
        ],
        "objects": [
            {"kind": "segment", "from": "A", "to": "B", "label": wl},
            {"kind": "segment", "from": "A", "to": "C", "label": hl,
             "color": "blue"},
            {"kind": "segment", "from": "B", "to": "C", "label": "?",
             "color": "accent"},
            {"kind": "angle", "at": "A", "from": "B", "to": "C",
             "right": True},
        ],
    }


def _triples_both(want=36):
    """Pythagorean triples (p, q, c) in BOTH leg orders, smallest first."""
    seen = set()
    out = []
    for m in range(2, 11):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a0, b0, c0 = m * m - n * n, 2 * m * n, m * m + n * n
                for mult in (1, 2, 3):
                    for p, q in ((a0 * mult, b0 * mult),
                                 (b0 * mult, a0 * mult)):
                        if (p, q) in seen:
                            continue
                        seen.add((p, q))
                        out.append((p, q, c0 * mult))
    out.sort(key=lambda t: (t[2], t[0]))
    return out[:want]


# ---------------------------------------------------------------------------
# unit: lines-and-planes-in-space
# ---------------------------------------------------------------------------

CUBE_EDGES = ["AB", "BC", "CD", "DA",
              "A_1B_1", "B_1C_1", "C_1D_1", "D_1A_1",
              "AA_1", "BB_1", "CC_1", "DD_1"]


def gen_cube_edges():
    # For any edge of a cube: 3 parallel, 4 intersecting (2 at each endpoint),
    # and 12 - 1 - 3 - 4 = 4 skew.
    out = []
    idx = 0
    for e in CUBE_EDGES:
        for q in ("parallel", "intersect", "skew"):
            pos = idx % 4
            if q == "parallel":
                st = ("In the cube $ABCDA_1B_1C_1D_1$, how many edges are "
                      "parallel to edge $%s$?" % e)
                ans = 3
                cands = [(intL(4), 4), (intL(6), 6), (intL(2), 2)]
                ex = ("The cube's 12 edges split into 3 directions of 4 "
                      "parallel edges each; besides $%s$ itself that leaves "
                      "$4 - 1 = 3$. Counting $%s$ itself gives the classic "
                      "wrong answer 4." % (e, e))
                chk = "4 - 1 == 3"
            elif q == "intersect":
                st = ("In the cube $ABCDA_1B_1C_1D_1$, how many edges "
                      "intersect edge $%s$?" % e)
                ans = 4
                cands = [(intL(3), 3), (intL(6), 6), (intL(8), 8)]
                ex = ("Each endpoint of $%s$ is a vertex where 2 more edges "
                      "meet, so $2 + 2 = 4$ edges intersect it. Skew edges "
                      "never touch it, so they must not be counted."
                      % e)
                chk = "2 + 2 == 4"
            else:
                st = ("In the cube $ABCDA_1B_1C_1D_1$, how many edges are "
                      "skew to edge $%s$?" % e)
                ans = 4
                cands = [(intL(3), 3), (intL(6), 6), (intL(8), 8)]
                ex = ("Of the other $11$ edges, $3$ are parallel to $%s$ and "
                      "$4$ intersect it, so $11 - 3 - 4 = 4$ are skew. The "
                      "classic miscount forgets that skew edges must be "
                      "neither parallel nor intersecting." % e)
                chk = "12 - 1 - 3 - 4 == 4"
            opts, ci = build_latex_options((intL(ans), ans), cands, pos,
                                           latex_of=intL)
            out.append({"statement": st, "options": opts, "correctIndex": ci,
                        "explanation": ex, "check": [chk]})
            idx += 1
    return out


COUNT_LINE_TS = [
    "In space, $%d$ points are in general position (no three on a line). "
    "How many distinct lines pass through pairs of these points?",
    "How many distinct lines are determined by $%d$ points in space in "
    "general position (no three on a line)?",
    "$%d$ points in space are in general position (no three on a line). "
    "How many distinct lines can be drawn through pairs of these points?",
]
COUNT_PLANE_TS = [
    "In space, $%d$ points are in general position (no four in one plane). "
    "How many distinct planes pass through triples of these points?",
    "How many distinct planes are determined by $%d$ points in space in "
    "general position (no four in one plane)?",
    "$%d$ points in space are in general position (no four in one plane). "
    "How many distinct planes can be drawn through triples of these points?",
]


def gen_counting_in_space():
    items = []
    for t in range(3):
        for n in range(4, 11):
            items.append(("line", t, n))
            items.append(("plane", t, n))
    out = []
    for idx, (kind, t, n) in enumerate(items[:36]):
        pos = idx % 4
        if kind == "line":
            ans = n * (n - 1) // 2
            st = COUNT_LINE_TS[t] % n
            cands = [(intL(n * (n - 1) * (n - 2) // 6),
                      n * (n - 1) * (n - 2) // 6),
                     (intL(factorial(n)), factorial(n)),
                     (intL(n * (n - 1)), n * (n - 1)),
                     (intL(n * n), n * n)]
            ex = ("Each pair of points determines exactly one line: "
                  "$\\binom{%d}{2} = \\frac{%d\\cdot %d}{2} = %d$. The "
                  "ordered count $%d\\cdot %d = %d$ counts every line twice."
                  % (n, n, n - 1, ans, n, n - 1, n * (n - 1)))
            chk = "binomial(%d,2) == %d" % (n, ans)
        else:
            ans = n * (n - 1) * (n - 2) // 6
            st = COUNT_PLANE_TS[t] % n
            cands = [(intL(n * (n - 1) // 2), n * (n - 1) // 2),
                     (intL(factorial(n)), factorial(n)),
                     (intL(n * (n - 1)), n * (n - 1)),
                     (intL(n * (n - 1) * (n - 2)), n * (n - 1) * (n - 2))]
            ex = ("Each triple of points determines one plane: "
                  "$\\binom{%d}{3} = %d$. Ordered counts like "
                  "$%d\\cdot %d = %d$ overcount — the order of the points "
                  "never matters." % (n, ans, n, n - 1, n * (n - 1)))
            chk = "binomial(%d,3) == %d" % (n, ans)
        opts, ci = build_latex_options((intL(ans), ans), cands, pos,
                                       latex_of=intL)
        out.append({"statement": st, "options": opts, "correctIndex": ci,
                    "explanation": ex, "check": [chk]})
    return out


# ---------------------------------------------------------------------------
# unit: prisms-and-the-cube
# ---------------------------------------------------------------------------

def gen_cube_diagonals():
    out = []
    idx = 0
    for a in range(2, 14):
        for kind in ("face", "space", "rev"):
            pos = idx % 4
            if kind == "face":
                st = ("A cube has edge $%d$. Find the length of a face "
                      "diagonal." % a)
                correct = (surd(a, 2), a * sqrt(2))
                cands = [(surd(a, 3), a * sqrt(3)), (intL(2 * a), 2 * a),
                         (intL(a), a)]
                ex = ("A face diagonal is the hypotenuse of a $%d$–$%d$ "
                      "right triangle: $\\sqrt{2\\cdot %d^2} = %s$. "
                      "$%s$ is the space diagonal — the classic mix-up."
                      % (a, a, a, surd(a, 2), surd(a, 3)))
                chk = "sqrt(2*%d**2) == %d*sqrt(2)" % (a, a)
            elif kind == "space":
                st = ("A cube has edge $%d$. Find the length of its space "
                      "diagonal." % a)
                correct = (surd(a, 3), a * sqrt(3))
                cands = [(surd(a, 2), a * sqrt(2)), (intL(2 * a), 2 * a),
                         (intL(a), a)]
                ex = ("$d = \\sqrt{%d^2 + %d^2 + %d^2} = \\sqrt{3\\cdot %d^2}"
                      " = %s$; $%s$ is only the face diagonal."
                      % (a, a, a, a, surd(a, 3), surd(a, 2)))
                chk = "sqrt(3*%d**2) == %d*sqrt(3)" % (a, a)
            else:
                st = ("The face diagonal of a cube is $%d\\sqrt{2}$. Find "
                      "the edge length." % a)
                correct = (intL(a), a)
                cands = [(intL(2 * a), 2 * a), (surd(a, 2), a * sqrt(2)),
                         (surd(a, 3), a * sqrt(3))]
                ex = ("Divide by $\\sqrt{2}$: edge $= \\frac{%d\\sqrt{2}}"
                      "{\\sqrt{2}} = %d$. Multiplying by $\\sqrt{2}$ instead "
                      "gives $%d$ — the classic wrong direction."
                      % (a, a, 2 * a))
                chk = "%d*sqrt(2)/sqrt(2) == %d" % (a, a)
            opts, ci = build_latex_options(correct, cands, pos)
            out.append({"statement": st, "options": opts, "correctIndex": ci,
                        "explanation": ex, "check": [chk]})
            idx += 1
    return out


PRISM_RECT = [(2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5), (2, 5, 6),
              (3, 4, 6), (2, 3, 7), (3, 5, 6), (4, 5, 6), (2, 4, 7),
              (3, 4, 7), (2, 5, 7), (4, 5, 7), (3, 6, 7), (2, 4, 9),
              (5, 6, 7), (3, 5, 8), (4, 6, 7)]
PRISM_TRI = [(3, 4, 5), (4, 5, 3), (6, 3, 4), (4, 6, 5), (5, 4, 7),
             (8, 3, 5), (6, 5, 7), (3, 8, 6), (10, 4, 3), (6, 7, 4),
             (12, 5, 2), (8, 5, 6), (4, 9, 5), (10, 6, 5), (7, 6, 8),
             (12, 4, 5), (9, 8, 3), (10, 8, 4)]


def gen_prism_volume():
    out = []
    idx = 0
    for (l, w, h), (p, q, H) in zip(PRISM_RECT, PRISM_TRI):
        # (a) rectangular prism
        pos = idx % 4
        V = l * w * h
        SA = 2 * (l * w + l * h + w * h)
        cands = [(intL(SA), SA), (intL(l + w + h), l + w + h),
                 (intL(4 * (l + w + h)), 4 * (l + w + h))]
        opts, ci = build_latex_options((intL(V), V), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A rectangular prism measures $%d \\times %d "
                         "\\times %d$. Find its volume." % (l, w, h),
            "options": opts, "correctIndex": ci,
            "explanation": "$V = lwh = %d\\cdot %d\\cdot %d = %d$. $%d$ is "
                           "the surface area $2(lw+lh+wh)$ — the classic "
                           "surface/volume mix-up." % (l, w, h, V, SA),
            "check": ["%d*%d*%d == %d" % (l, w, h, V)],
        })
        idx += 1
        # (b) right-triangle-based prism (p*q even)
        pos = idx % 4
        assert (p * q) % 2 == 0
        B = p * q // 2
        V = B * H
        cands = [(intL(p * q * H), p * q * H),
                 (intL((p + q) * H), (p + q) * H),
                 (intL(p + q + H), p + q + H)]
        opts, ci = build_latex_options((intL(V), V), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "The base of a right prism is a right triangle "
                         "with legs $%d$ and $%d$; the prism has height "
                         "$%d$. Find its volume." % (p, q, H),
            "options": opts, "correctIndex": ci,
            "explanation": "Base area $= \\tfrac12\\cdot %d\\cdot %d = %d$, "
                           "so $V = %d\\cdot %d = %d$. Forgetting the "
                           "$\\tfrac12$ gives $%d$."
                           % (p, q, B, B, H, V, p * q * H),
            "check": ["Rational(1,2)*%d*%d*%d == %d" % (p, q, H, V)],
        })
        idx += 1
    return out


# ---------------------------------------------------------------------------
# unit: pyramids
# ---------------------------------------------------------------------------

def gen_pyramid_volume():
    pairs = [(a, h) for a in range(2, 14) for h in range(2, 13)
             if (a * a * h) % 3 == 0]
    out = []
    for idx, (a, h) in enumerate(_pick_spread(pairs, 36)):
        pos = idx % 4
        V = a * a * h // 3
        cands = [(intL(a * a * h), a * a * h),
                 (L(Rational(a * a * h, 2)), Rational(a * a * h, 2)),
                 (L(Rational(a * h, 3)), Rational(a * h, 3))]
        opts, ci = build_latex_options((intL(V), V), cands, pos, latex_of=L)
        out.append({
            "statement": "A pyramid has a square base with side $%d$ and "
                         "height $%d$. Find its volume." % (a, h),
            "options": opts, "correctIndex": ci,
            "explanation": "$V = \\tfrac13 a^2 h = \\tfrac13\\cdot %d\\cdot "
                           "%d = %d$. Forgetting the $\\tfrac13$ gives the "
                           "prism volume $%d$." % (a * a, h, V, a * a * h),
            "check": ["Rational(1,3)*%d**2*%d == %d" % (a, h, V)],
        })
    return out


def gen_pyramid_slant():
    out = []
    for idx, (x, h, m) in enumerate(_triples_both(36)):
        pos = idx % 4
        a = 2 * x  # even base side; (a/2, h, m) is a Pythagorean triple
        cands = [("\\sqrt{%d}" % (a * a + h * h), sqrt(a * a + h * h)),
                 (intL(h + x), h + x),
                 (intL(abs(h - x)), abs(h - x))]
        opts, ci = build_latex_options((intL(m), m), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A regular square pyramid has base side $%d$ and "
                         "height $%d$. Find the slant height from the apex "
                         "to the midpoint of a base edge." % (a, h),
            "options": opts, "correctIndex": ci,
            "explanation": "The slant height closes a right triangle with "
                           "legs $h = %d$ and half the base, "
                           "$\\tfrac{%d}{2} = %d$: $\\sqrt{%d^2 + %d^2} = "
                           "%d$. Using the full side $%d$ instead of half "
                           "is the classic slip." % (h, a, x, h, x, m, a),
            "check": ["sqrt(%d**2 + Rational(%d,2)**2) == %d" % (h, a, m)],
            "geoFigure": _rt_fig(x, h, str(x), str(h)),
        })
    return out


# ---------------------------------------------------------------------------
# unit: cylinders-and-cones
# ---------------------------------------------------------------------------

CYL_PAIRS = [(2, 3), (2, 5), (2, 7), (2, 9), (3, 2), (3, 4), (3, 5), (3, 8),
             (4, 3), (4, 5), (4, 7), (5, 2), (5, 4), (5, 6), (6, 5), (6, 7),
             (7, 3), (7, 4)]


def gen_cylinder_surface():
    out = []
    idx = 0
    for r, h in CYL_PAIRS:
        # lateral surface
        pos = idx % 4
        k = 2 * r * h
        kt = 2 * r * (r + h)
        cands = [(piL(kt), kt * pi), (piL(r * r * h), r * r * h * pi),
                 (piL(r * h), r * h * pi)] + _pi_buffer(k)
        opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
        out.append({
            "statement": "A cylinder has base radius $%d$ and height $%d$. "
                         "Find its lateral surface area, exactly." % (r, h),
            "options": opts, "correctIndex": ci,
            "explanation": "Unrolled, the lateral surface is a rectangle "
                           "$2\\pi r \\times h$: $2\\pi\\cdot %d\\cdot %d = "
                           "%s$. $%s$ is the total surface — it also counts "
                           "the two disks." % (r, h, piL(k), piL(kt)),
            "check": ["2*pi*%d*%d == %d*pi" % (r, h, k)],
        })
        idx += 1
        # total surface
        pos = idx % 4
        cands = [(piL(k), k * pi), (piL(r * r * h), r * r * h * pi),
                 (piL(r * (r + h)), r * (r + h) * pi)] + _pi_buffer(kt)
        opts, ci = build_latex_options((piL(kt), kt * pi), cands, pos)
        out.append({
            "statement": "A cylinder has base radius $%d$ and height $%d$. "
                         "Find its total surface area, exactly." % (r, h),
            "options": opts, "correctIndex": ci,
            "explanation": "Total surface $= 2\\pi rh + 2\\pi r^2 = "
                           "2\\pi r(r+h) = 2\\pi\\cdot %d\\cdot %d = %s$. "
                           "Stopping at the lateral rectangle $%s$ forgets "
                           "the two disks." % (r, r + h, piL(kt), piL(k)),
            "check": ["2*pi*%d*(%d + %d) == %d*pi" % (r, r, h, kt)],
        })
        idx += 1
    return out


def gen_cone_slant_lateral():
    out = []
    for idx, (r, h, l) in enumerate(_triples_both(36)):
        pos = idx % 4
        if idx % 2 == 0:
            # slant height
            cands = [(intL(r + h), r + h), (intL(abs(h - r)), abs(h - r)),
                     (intL(l + 2), l + 2)]
            opts, ci = build_latex_options((intL(l), l), cands, pos,
                                           latex_of=intL)
            out.append({
                "statement": "A cone has base radius $%d$ and height $%d$. "
                             "Find its slant height." % (r, h),
                "options": opts, "correctIndex": ci,
                "explanation": "$\\ell = \\sqrt{%d^2 + %d^2} = \\sqrt{%d} = "
                               "%d$ — the %d-%d-%d triple. Adding "
                               "$%d + %d = %d$ skips Pythagoras entirely."
                               % (r, h, l * l, l, r, h, l, r, h, r + h),
                "check": ["sqrt(%d**2 + %d**2) == %d" % (r, h, l)],
                "geoFigure": _rt_fig(r, h, str(r), str(h)),
            })
        else:
            # lateral surface
            k = r * l
            cands = [(piL(r * h), r * h * pi),
                     (piL(r * (r + l)), r * (r + l) * pi),
                     (piL(2 * r * l), 2 * r * l * pi)] + _pi_buffer(k)
            opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
            out.append({
                "statement": "A cone has base radius $%d$ and height $%d$. "
                             "Find its lateral surface area, exactly."
                             % (r, h),
                "options": opts, "correctIndex": ci,
                "explanation": "First $\\ell = \\sqrt{%d^2 + %d^2} = %d$; "
                               "then $S_{\\text{lat}} = \\pi r \\ell = "
                               "\\pi\\cdot %d\\cdot %d = %s$. Using the "
                               "height instead of the slant gives $%s$."
                               % (r, h, l, r, l, piL(k), piL(r * h)),
                "check": ["pi*%d*sqrt(%d**2 + %d**2) == %d*pi"
                          % (r, r, h, k)],
            })
    return out


# ---------------------------------------------------------------------------
# unit: spheres
# ---------------------------------------------------------------------------

def gen_sphere_surface():
    out = []
    idx = 0
    for R in range(2, 14):
        for kind in ("surface", "great", "rev"):
            pos = idx % 4
            if kind == "surface":
                k = 4 * R * R
                cands = [(piL(R * R), R * R * pi),
                         (piL(Rational(4 * R ** 3, 3)),
                          Rational(4 * R ** 3, 3) * pi),
                         (piL(2 * R), 2 * R * pi),
                         (piL(R ** 3), R ** 3 * pi)] + _pi_buffer(k)
                opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
                out.append({
                    "statement": "A sphere has radius $%d$. Find its "
                                 "surface area, exactly." % R,
                    "options": opts, "correctIndex": ci,
                    "explanation": "$S = 4\\pi R^2 = 4\\pi\\cdot %d = %s$ — "
                                   "exactly four great circles. $%s$ is "
                                   "just one great circle."
                                   % (R * R, piL(k), piL(R * R)),
                    "check": ["4*pi*%d**2 == %d*pi" % (R, k)],
                })
            elif kind == "great":
                k = R * R
                cands = [(piL(4 * R * R), 4 * R * R * pi),
                         (piL(2 * R), 2 * R * pi),
                         (piL(Rational(4 * R ** 3, 3)),
                          Rational(4 * R ** 3, 3) * pi),
                         (piL(R ** 3), R ** 3 * pi)] + _pi_buffer(k)
                opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
                out.append({
                    "statement": "A sphere has radius $%d$. Find the area "
                                 "of its great circle, exactly." % R,
                    "options": opts, "correctIndex": ci,
                    "explanation": "A great circle is a circle with the "
                                   "sphere's own radius, so $A = \\pi R^2 = "
                                   "%s$. $%s$ is the full surface area — "
                                   "four times too big."
                                   % (piL(k), piL(4 * R * R)),
                    "check": ["pi*%d**2 == %d*pi" % (R, k)],
                })
            else:
                k = 4 * R * R
                cands = [(intL(2 * R), 2 * R), (intL(R * R), R * R),
                         (intL(4 * R), 4 * R)]
                opts, ci = build_latex_options((intL(R), R), cands, pos,
                                               latex_of=intL)
                out.append({
                    "statement": "A sphere has surface area $%s$. Find its "
                                 "radius." % piL(k),
                    "options": opts, "correctIndex": ci,
                    "explanation": "$4\\pi R^2 = %s$ gives $R^2 = %d$, so "
                                   "$R = %d$. Taking $\\sqrt{%d}$ without "
                                   "first dividing by $4$ gives $%d$."
                                   % (piL(k), R * R, R, k, 2 * R),
                    "check": ["sqrt(Rational(%d,4)) == %d" % (k, R)],
                })
            idx += 1
    return out


# ---------------------------------------------------------------------------
# unit: cross-sections-and-similar-solids
# ---------------------------------------------------------------------------

SIM_VOL = [(1, 2, 3), (1, 2, 5), (2, 3, 1), (2, 3, 2), (1, 3, 2), (3, 4, 1),
           (1, 4, 3), (2, 5, 1), (3, 5, 1), (4, 5, 1), (1, 5, 2), (5, 6, 1)]
SIM_AREA = [(1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 3, 3), (3, 4, 1), (1, 4, 3),
            (2, 5, 1), (3, 5, 1), (4, 5, 1), (1, 5, 3), (5, 6, 1), (1, 2, 7)]
SIM_REV = [(1, 2), (2, 3), (1, 3), (3, 4), (2, 5), (3, 5), (4, 5), (1, 4),
           (5, 6), (1, 5), (2, 7), (3, 7)]


def gen_similar_solids():
    out = []
    idx = 0
    for i in range(12):
        # (a) volume forward: V * (k/j)^3
        j, k, t = SIM_VOL[i]
        pos = idx % 4
        V = t * j ** 3
        ans = t * k ** 3
        cands = [(intL(t * j * j * k), t * j * j * k),      # linear slip
                 (intL(t * j * k * k), t * j * k * k),      # squared slip
                 (intL(ans - V), ans - V)]                  # difference slip
        opts, ci = build_latex_options((intL(ans), ans), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "Two similar solids have similarity ratio "
                         "$%d : %d$ (smaller to larger). The smaller solid "
                         "has volume $%d$. Find the volume of the larger "
                         "solid." % (j, k, V),
            "options": opts, "correctIndex": ci,
            "explanation": "Volumes scale with the cube of the ratio: "
                           "$%d\\cdot\\left(\\tfrac{%d}{%d}\\right)^3 = "
                           "%d$. Multiplying by just $\\tfrac{%d}{%d}$ — "
                           "the length scale — gives $%d$."
                           % (V, k, j, ans, k, j, t * j * j * k),
            "check": ["%d*Rational(%d,%d)**3 == %d" % (V, k, j, ans)],
        })
        idx += 1
        # (b) surface-area forward: S * (k/j)^2
        j, k, u = SIM_AREA[i]
        pos = idx % 4
        S = u * j ** 3
        ans = u * j * k * k
        cands = [(intL(u * j * j * k), u * j * j * k),      # linear slip
                 (intL(u * k ** 3), u * k ** 3),            # cubed-for-area
                 (intL(ans - S), ans - S),                  # difference slip
                 (intL(u * j * j * k * k), u * j * j * k * k)]
        opts, ci = build_latex_options((intL(ans), ans), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "Two similar solids have similarity ratio "
                         "$%d : %d$ (smaller to larger). The smaller solid "
                         "has surface area $%d$. Find the surface area of "
                         "the larger solid." % (j, k, S),
            "options": opts, "correctIndex": ci,
            "explanation": "Areas scale with the square of the ratio: "
                           "$%d\\cdot\\left(\\tfrac{%d}{%d}\\right)^2 = "
                           "%d$. Cubing the ratio — the volume rule — "
                           "gives $%d$." % (S, k, j, ans, u * k ** 3),
            "check": ["%d*Rational(%d,%d)**2 == %d" % (S, k, j, ans)],
        })
        idx += 1
        # (c) reverse: volumes j^3, k^3 -> similarity ratio j : k
        j, k = SIM_REV[i]
        pos = idx % 4
        v1, v2 = j ** 3, k ** 3
        correct = "$%d : %d$" % (j, k)
        dists = ["$%d : %d$" % (v1, v2),          # volume ratio repeated
                 "$%d : %d$" % (j * j, k * k),    # area (squared) rule
                 "$%d : %d$" % (k, j)]            # inverted ratio
        vals = {Rational(j, k), Rational(v1, v2), Rational(j * j, k * k),
                Rational(k, j)}
        assert len(vals) == 4, "similar-solids ratio collision %d:%d" % (j, k)
        opts = list(dists)
        opts.insert(pos, correct)
        assert len(set(opts)) == 4
        out.append({
            "statement": "Two similar solids have volumes $%d$ and $%d$. "
                         "Find their similarity ratio (smaller to larger)."
                         % (v1, v2),
            "options": opts, "correctIndex": pos,
            "explanation": "The length ratio is the cube root of the "
                           "volume ratio: $\\sqrt[3]{\\tfrac{%d}{%d}} = "
                           "\\tfrac{%d}{%d}$, i.e. $%d : %d$. Answering "
                           "$%d : %d$ just repeats the volume ratio."
                           % (v1, v2, j, k, j, k, v1, v2),
            "check": ["Rational(%d,%d)**3 == Rational(%d,%d)"
                      % (j, k, v1, v2)],
        })
        idx += 1
    return out


# ---------------------------------------------------------------------------
# assembly of the new forms
# ---------------------------------------------------------------------------

NEW_FORMS_META = [
    ("cube-edge-relations", "Edges of the cube: parallel, intersecting, skew",
     1, "SOLID-edges", "lines-and-planes-in-space", "edges", gen_cube_edges),
    ("counting-in-space", "Counting lines & planes through points", 2,
     "SOLID-planes", "lines-and-planes-in-space", "planes",
     gen_counting_in_space),
    ("cube-diagonals", "Cube diagonals: the √2 and √3 rules", 1,
     "SOLID-cdiag", "prisms-and-the-cube", "cdiag", gen_cube_diagonals),
    ("prism-volume", "Prism volume", 2, "SOLID-pvol", "prisms-and-the-cube",
     "pvol", gen_prism_volume),
    ("pyramid-volume", "Pyramid volume", 1, "SOLID-pyrv", "pyramids", "pyrv",
     gen_pyramid_volume),
    ("pyramid-slant", "Slant height of a regular pyramid", 2, "SOLID-slant",
     "pyramids", "slant", gen_pyramid_slant),
    ("cylinder-surface", "Cylinder surface area", 2, "SOLID-cyls",
     "cylinders-and-cones", "cyls", gen_cylinder_surface),
    ("cone-slant-lateral", "Cone: slant height & lateral surface", 2,
     "SOLID-cone", "cylinders-and-cones", "cone", gen_cone_slant_lateral),
    ("sphere-surface", "Sphere surface area & the great circle", 1,
     "SOLID-sph", "spheres", "sph", gen_sphere_surface),
    ("similar-solids", "Similar solids: k, k², k³", 3, "SOLID-simsol",
     "cross-sections-and-similar-solids", "simsol", gen_similar_solids),
]


def new_forms():
    """Unit-specific forms authored for this subject (appended by unit)."""
    forms = []
    for fid, title, level, skill, unit, ab, gen in NEW_FORMS_META:
        raw = gen()
        assert len(raw) >= 34, "%s: only %d variants" % (fid, len(raw))
        variants = []
        for i, v in enumerate(raw):
            vd = {"id": "SOLID-%s-v%02d" % (ab, i + 1)}
            vd.update(v)
            variants.append(vd)
        forms.append({"id": fid, "title": title, "level": level,
                      "skill": skill, "unit": unit, "variants": variants})
    forms.extend(_extra_new_forms())  # appended drill forms (defined below)
    return forms


# ---------------------------------------------------------------------------
# independent re-solvers (blind: regex-parse the statement, recompute)
# ---------------------------------------------------------------------------

def _r_cube_edges(s):
    if "parallel" in s:
        return ("num", 3)
    if "skew" in s:
        return ("num", 4)
    assert "intersect" in s
    return ("num", 4)


def _r_counting(s):
    n = int(re.search(r"\$(\d+)\$", s).group(1))
    if "plane" in s:
        return ("num", Rational(n * (n - 1) * (n - 2), 6))
    return ("num", Rational(n * (n - 1), 2))


def _r_cube_diagonals(s):
    m = re.search(r"face diagonal of a cube is \$(\d+)\\sqrt\{2\}\$", s)
    if m:
        return ("num", int(m.group(1)))
    a = int(re.search(r"edge \$(\d+)\$", s).group(1))
    if "space diagonal" in s:
        return ("num", a * sqrt(3))
    return ("num", a * sqrt(2))


def _r_prism_volume(s):
    if "rectangular" in s:
        l, w, h = [int(x) for x in re.findall(r"\d+", s)][:3]
        return ("num", l * w * h)
    m = re.search(r"legs \$(\d+)\$ and \$(\d+)\$; the prism has height "
                  r"\$(\d+)\$", s)
    p, q, H = (int(x) for x in m.groups())
    return ("num", Rational(p * q * H, 2))


def _r_pyramid_volume(s):
    m = re.search(r"side \$(\d+)\$ and height \$(\d+)\$", s)
    a, h = int(m.group(1)), int(m.group(2))
    return ("num", Rational(a * a * h, 3))


def _r_pyramid_slant(s):
    m = re.search(r"base side \$(\d+)\$ and height \$(\d+)\$", s)
    a, h = int(m.group(1)), int(m.group(2))
    return ("num", sqrt(h ** 2 + Rational(a, 2) ** 2))


def _r_cylinder_surface(s):
    m = re.search(r"radius \$(\d+)\$ and height \$(\d+)\$", s)
    r, h = int(m.group(1)), int(m.group(2))
    if "lateral" in s:
        return ("num", 2 * pi * r * h)
    return ("num", 2 * pi * r * (r + h))


def _r_cone(s):
    m = re.search(r"radius \$(\d+)\$ and height \$(\d+)\$", s)
    r, h = int(m.group(1)), int(m.group(2))
    ell = sqrt(r * r + h * h)
    if "lateral" in s:
        return ("num", pi * r * ell)
    return ("num", ell)


def _r_sphere(s):
    m = re.search(r"surface area \$(\d+)\\pi\$", s)
    if m:
        return ("num", sqrt(Rational(int(m.group(1)), 4)))
    R = int(re.search(r"radius \$(\d+)\$", s).group(1))
    if "great circle" in s:
        return ("num", pi * R * R)
    return ("num", 4 * pi * R * R)


def _r_similar_solids(s):
    m = re.search(r"similarity ratio \$(\d+) : (\d+)\$", s)
    if m:
        j, k = int(m.group(1)), int(m.group(2))
        ms = re.search(r"surface area \$(\d+)\$", s)
        if ms:
            return ("num", Rational(int(ms.group(1)) * k * k, j * j))
        V = int(re.search(r"volume \$(\d+)\$", s).group(1))
        return ("num", Rational(V * k ** 3, j ** 3))
    m = re.search(r"volumes \$(\d+)\$ and \$(\d+)\$", s)
    v1, v2 = int(m.group(1)), int(m.group(2))
    j, k = round(v1 ** (1.0 / 3)), round(v2 ** (1.0 / 3))
    assert j ** 3 == v1 and k ** 3 == v2, "volumes are not perfect cubes"
    g = gcd(j, k)
    return ("opt", "$%d : %d$" % (j // g, k // g))


RESOLVERS.update({
    "cube-edge-relations": _r_cube_edges,
    "counting-in-space": _r_counting,
    "cube-diagonals": _r_cube_diagonals,
    "prism-volume": _r_prism_volume,
    "pyramid-volume": _r_pyramid_volume,
    "pyramid-slant": _r_pyramid_slant,
    "cylinder-surface": _r_cylinder_surface,
    "cone-slant-lateral": _r_cone,
    "sphere-surface": _r_sphere,
    "similar-solids": _r_similar_solids,
})


# ---------------------------------------------------------------------------
# appended drill forms — extra distinct problem types per unit
# (12 variants each; assembled by _extra_new_forms(), floor 10)
# ---------------------------------------------------------------------------

def _sqrtL(n):
    """LaTeX for sqrt(n), simplified: 164 -> 2\\sqrt{41}, 144 -> 12."""
    s = sqrt(n)
    if s.is_Integer:
        return intL(s)
    c, rest = s.as_coeff_Mul()
    return surd(int(c), int(rest ** 2))


# --- lines-and-planes-in-space: classify a pair of cube edges ---------------

CUBE_VERT_XY = {"A": (0, 0), "B": (1, 0), "C": (1, 1), "D": (0, 1)}


def _edge_endpoints(edge):
    """Vertices of a cube edge name like 'A_1B_1' as 3D coordinates:
    A(0,0,0) B(1,0,0) C(1,1,0) D(0,1,0), subscript-1 vertices at z = 1."""
    pts = []
    for v in re.findall(r"[A-D](?:_1)?", edge):
        x, y = CUBE_VERT_XY[v[0]]
        pts.append((x, y, 1 if v.endswith("_1") else 0))
    assert len(pts) == 2, edge
    return pts


def _edge_relation(e1, e2):
    """Classify two cube edges by coordinates. Returns (class, cross, triple)
    where cross = d1 x d2 and triple = (d1 x d2) . (p2 - p1)."""
    (p1, q1), (p2, q2) = _edge_endpoints(e1), _edge_endpoints(e2)
    d1 = tuple(q1[i] - p1[i] for i in range(3))
    d2 = tuple(q2[i] - p2[i] for i in range(3))
    cross = (d1[1] * d2[2] - d1[2] * d2[1],
             d1[2] * d2[0] - d1[0] * d2[2],
             d1[0] * d2[1] - d1[1] * d2[0])
    w = tuple(p2[i] - p1[i] for i in range(3))
    triple = cross[0] * w[0] + cross[1] * w[1] + cross[2] * w[2]
    if cross == (0, 0, 0):
        return "parallel", cross, triple
    return ("intersecting" if triple == 0 else "skew"), cross, triple


CLSF_PAIRS = [
    ("AB", "C_1D_1", "parallel"),
    ("AB", "BC", "intersecting"),
    ("AB", "CC_1", "skew"),
    ("BC", "A_1D_1", "parallel"),
    ("AB", "AA_1", "intersecting"),
    ("AB", "B_1C_1", "skew"),
    ("AA_1", "CC_1", "parallel"),
    ("B_1C_1", "CC_1", "intersecting"),
    ("AA_1", "BC", "skew"),
    ("CD", "A_1B_1", "parallel"),
    ("DA", "DD_1", "intersecting"),
    ("CD", "BB_1", "skew"),
]


def gen_classify_edge_pair():
    out = []
    for idx, (e1, e2, cls) in enumerate(CLSF_PAIRS):
        pos = idx % 4
        got, cross, triple = _edge_relation(e1, e2)
        assert got == cls, (e1, e2, cls, got)
        cs2 = "(%d)**2 + (%d)**2 + (%d)**2" % cross
        if cls == "parallel":
            others = ["intersecting", "skew", "equal and intersecting"]
            ex = ("The direction vectors of $%s$ and $%s$ are proportional, "
                  "so the lines are parallel. Calling them skew just because "
                  "they lie in different faces is the classic slip."
                  % (e1, e2))
            chk = ["Eq(%s, 0)" % cs2]
        elif cls == "intersecting":
            shared = sorted(set(re.findall(r"[A-D](?:_1)?", e1))
                            & set(re.findall(r"[A-D](?:_1)?", e2)))[0]
            others = ["parallel", "skew", "coincident"]
            ex = ("$%s$ and $%s$ share the vertex $%s$, so the lines meet at "
                  "a point. Answering 'skew' because the edges point in "
                  "different directions is the classic slip — skew lines "
                  "must have no common point." % (e1, e2, shared))
            chk = ["Eq(%d, 0)" % triple, "Ne(%s, 0)" % cs2]
        else:
            others = ["parallel", "intersecting", "equal and intersecting"]
            ex = ("$%s$ and $%s$ are not parallel and share no vertex, so no "
                  "plane contains both: they are skew. Trusting the flat "
                  "drawing, where they appear to cross, is the classic "
                  "mistake." % (e1, e2))
            chk = ["Ne(%d, 0)" % triple]
        opts = list(others)
        opts.insert(pos, cls)
        assert len(set(opts)) == 4
        out.append({
            "statement": "In the cube $ABCDA_1B_1C_1D_1$, how are the lines "
                         "containing edges $%s$ and $%s$ positioned relative "
                         "to each other?" % (e1, e2),
            "options": opts, "correctIndex": pos,
            "explanation": ex, "check": chk,
        })
    return out


# --- lines-and-planes-in-space: a slanted segment & its projection ----------

PROJ_FWD = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15),
            (20, 21, 29)]
PROJ_REV = [(4, 3, 5), (8, 6, 10), (12, 5, 13), (15, 8, 17), (12, 9, 15),
            (24, 7, 25)]


def _proj_fig(p, h, wl, hl, dl):
    """True-scale extracted right triangle: foot of the perpendicular at the
    origin, projection horizontal (label wl), height vertical (label hl,
    blue), slanted segment as the hypotenuse (label dl, accent)."""
    return {
        "points": [
            {"id": "F", "x": 0, "y": 0, "label": ""},
            {"id": "Q", "x": p, "y": 0, "label": ""},
            {"id": "T", "x": 0, "y": h, "label": ""},
        ],
        "objects": [
            {"kind": "segment", "from": "F", "to": "Q", "label": wl},
            {"kind": "segment", "from": "F", "to": "T", "label": hl,
             "color": "blue"},
            {"kind": "segment", "from": "Q", "to": "T", "label": dl,
             "color": "accent"},
            {"kind": "angle", "at": "F", "from": "Q", "to": "T",
             "right": True},
        ],
    }


def gen_diagonal_projection():
    out = []
    idx = 0
    for fwd, rev in zip(PROJ_FWD, PROJ_REV):
        # forward: segment + height -> projection
        p, h, d = fwd
        pos = idx % 4
        cands = [(_sqrtL(d * d + h * h), sqrt(d * d + h * h)),
                 (intL(d - h), d - h), (intL(d + h), d + h)]
        opts, ci = build_latex_options((intL(p), p), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A segment of length $%d$ joins a point at height "
                         "$%d$ above a plane to a point in the plane. Find "
                         "the length of the segment's projection on the "
                         "plane." % (d, h),
            "options": opts, "correctIndex": ci,
            "explanation": "Segment, height and projection form a right "
                           "triangle with the segment as hypotenuse: "
                           "$\\sqrt{%d^2 - %d^2} = %d$. Adding the squares "
                           "instead, $%s$, treats the projection as the "
                           "hypotenuse — the classic slip."
                           % (d, h, p, _sqrtL(d * d + h * h)),
            "check": ["sqrt(%d**2 - %d**2) == %d" % (d, h, p)],
            "geoFigure": _proj_fig(p, h, "?", str(h), str(d)),
        })
        idx += 1
        # reverse: projection + height -> segment
        p, h, d = rev
        pos = idx % 4
        cands = [(_sqrtL(p * p - h * h), sqrt(p * p - h * h)),
                 (intL(p + h), p + h), (intL(p - h), p - h)]
        opts, ci = build_latex_options((intL(d), d), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A segment joins a point at height $%d$ above a "
                         "plane to a point in the plane; its projection on "
                         "the plane has length $%d$. Find the length of the "
                         "segment." % (h, p),
            "options": opts, "correctIndex": ci,
            "explanation": "The segment is the hypotenuse over the legs "
                           "$%d$ (projection) and $%d$ (height): "
                           "$\\sqrt{%d^2 + %d^2} = %d$. Adding the legs, "
                           "$%d + %d = %d$, skips Pythagoras — the classic "
                           "slip." % (p, h, p, h, d, p, h, p + h),
            "check": ["sqrt(%d**2 + %d**2) == %d" % (p, h, d)],
            "geoFigure": _proj_fig(p, h, str(p), str(h), "?"),
        })
        idx += 1
    return out


# --- prisms-and-the-cube: cube surface area & volume ------------------------

CSV_SURF = (2, 3, 4, 5)
CSV_VOL = (7, 8, 9, 10)
CSV_REV = (6, 11, 12, 13)


def gen_cube_surface_volume():
    out = []
    idx = 0
    for a_s, a_v, a_r in zip(CSV_SURF, CSV_VOL, CSV_REV):
        # (a) surface area from edge
        pos = idx % 4
        S = 6 * a_s * a_s
        cands = [(intL(a_s ** 3), a_s ** 3),
                 (intL(4 * a_s * a_s), 4 * a_s * a_s),
                 (intL(a_s * a_s), a_s * a_s),
                 (intL(12 * a_s), 12 * a_s)]
        opts, ci = build_latex_options((intL(S), S), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A cube has edge $%d$. Find its surface area."
                         % a_s,
            "options": opts, "correctIndex": ci,
            "explanation": "All $6$ faces are $%d \\times %d$ squares: "
                           "$S = 6a^2 = 6\\cdot %d = %d$. Counting only the "
                           "$4$ side faces gives $%d$."
                           % (a_s, a_s, a_s * a_s, S, 4 * a_s * a_s),
            "check": ["6*%d**2 == %d" % (a_s, S)],
        })
        idx += 1
        # (b) volume from edge
        pos = idx % 4
        V = a_v ** 3
        cands = [(intL(6 * a_v * a_v), 6 * a_v * a_v),
                 (intL(a_v * a_v), a_v * a_v),
                 (intL(12 * a_v), 12 * a_v)]
        opts, ci = build_latex_options((intL(V), V), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A cube has edge $%d$. Find its volume." % a_v,
            "options": opts, "correctIndex": ci,
            "explanation": "$V = a^3 = %d^3 = %d$. $%d$ is the surface area "
                           "$6a^2$ — the classic surface/volume mix-up."
                           % (a_v, V, 6 * a_v * a_v),
            "check": ["%d**3 == %d" % (a_v, V)],
        })
        idx += 1
        # (c) edge back from surface area (engineered integer)
        pos = idx % 4
        S = 6 * a_r * a_r
        cands = [(intL(a_r * a_r), a_r * a_r),
                 (surd(a_r, 6), a_r * sqrt(6)),
                 (intL(2 * a_r), 2 * a_r)]
        opts, ci = build_latex_options((intL(a_r), a_r), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A cube has surface area $%d$. Find its edge "
                         "length." % S,
            "options": opts, "correctIndex": ci,
            "explanation": "$6a^2 = %d$ gives $a^2 = %d$, so $a = %d$. "
                           "Dividing by $6$ but forgetting the square root "
                           "leaves $%d$." % (S, a_r * a_r, a_r, a_r * a_r),
            "check": ["sqrt(Rational(%d,6)) == %d" % (S, a_r)],
        })
        idx += 1
    return out


# --- prisms-and-the-cube: lateral surface of a right prism ------------------

PLAT_PAIRS = [(10, 3), (12, 5), (14, 4), (16, 7), (18, 5), (20, 6),
              (22, 3), (24, 5), (26, 4), (28, 6), (30, 7), (32, 5)]


def gen_prism_lateral():
    out = []
    for idx, (P, h) in enumerate(PLAT_PAIRS):
        pos = idx % 4
        S = P * h
        cands = [(intL(S // 2), S // 2), (intL(P + h), P + h),
                 (intL(2 * S), 2 * S)]
        opts, ci = build_latex_options((intL(S), S), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A right prism has base perimeter $%d$ and height "
                         "$%d$. Find its lateral surface area." % (P, h),
            "options": opts, "correctIndex": ci,
            "explanation": "Unrolled, the lateral surface is one rectangle "
                           "$P \\times h$: $%d\\cdot %d = %d$. Halving it "
                           "to $%d$ borrows the pyramid's $\\tfrac12$ — a "
                           "prism has none." % (P, h, S, S // 2),
            "check": ["%d*%d == %d" % (P, h, S)],
        })
    return out


# --- pyramids: lateral surface of a regular square pyramid ------------------

PYL_PAIRS = [(3, 5), (4, 5), (5, 6), (6, 5), (4, 7), (6, 7), (5, 8), (8, 5),
             (7, 6), (6, 9), (8, 7), (9, 4)]


def gen_pyramid_lateral():
    out = []
    for idx, (a, m) in enumerate(PYL_PAIRS):
        pos = idx % 4
        S = 2 * a * m
        cands = [(intL(4 * a * m), 4 * a * m), (intL(a * m), a * m),
                 (intL(a * a + 2 * a * m), a * a + 2 * a * m)]
        opts, ci = build_latex_options((intL(S), S), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A regular square pyramid has base side $%d$ and "
                         "slant height $%d$. Find its lateral surface area."
                         % (a, m),
            "options": opts, "correctIndex": ci,
            "explanation": "Four triangular faces of area $\\tfrac12 am$ "
                           "each: $S = \\tfrac12\\cdot 4\\cdot %d\\cdot %d "
                           "= %d$. Forgetting the $\\tfrac12$ gives $%d$."
                           % (a, m, S, 4 * a * m),
            "check": ["Rational(1,2)*4*%d*%d == %d" % (a, m, S)],
        })
    return out


# --- pyramids: base side back from the volume --------------------------------

PBV_PAIRS = [(2, 3), (4, 3), (3, 4), (5, 3), (6, 4), (3, 5), (6, 5), (9, 2),
             (3, 7), (12, 4), (6, 7), (9, 5)]


def gen_pyramid_base_side():
    out = []
    for idx, (a, h) in enumerate(PBV_PAIRS):
        pos = idx % 4
        assert (a * a * h) % 3 == 0
        V = a * a * h // 3
        cands = [(intL(a * a), a * a),
                 ("\\sqrt{" + L(Rational(V, h)) + "}", sqrt(Rational(V, h))),
                 (_sqrtL(3 * V), sqrt(3 * V))]
        opts, ci = build_latex_options((intL(a), a), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A pyramid with a square base has volume $%d$ and "
                         "height $%d$. Find its base side." % (V, h),
            "options": opts, "correctIndex": ci,
            "explanation": "From $V = \\tfrac13 a^2 h$: $a^2 = \\frac{3V}"
                           "{h} = \\frac{3\\cdot %d}{%d} = %d$, so "
                           "$a = %d$. Stopping at $a^2 = %d$ without the "
                           "square root is the classic slip."
                           % (V, h, a * a, a, a * a),
            "check": ["sqrt(Rational(3*%d,%d)) == %d" % (V, h, a)],
        })
    return out


# --- cylinders-and-cones: cone volume ----------------------------------------

CVOL_PAIRS = [(3, 4), (2, 3), (3, 5), (4, 3), (5, 3), (2, 6), (3, 7),
              (6, 4), (4, 6), (3, 8), (6, 5), (5, 6)]


def gen_cone_volume():
    out = []
    for idx, (r, h) in enumerate(CVOL_PAIRS):
        pos = idx % 4
        assert (r * r * h) % 3 == 0
        k = r * r * h // 3
        cands = [(piL(r * r * h), r * r * h * pi),
                 (piL(r * h), r * h * pi),
                 (piL(Rational(r * r * h, 2)),
                  Rational(r * r * h, 2) * pi)] + _pi_buffer(k)
        opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
        out.append({
            "statement": "A cone has base radius $%d$ and height $%d$. Find "
                         "its volume, exactly." % (r, h),
            "options": opts, "correctIndex": ci,
            "explanation": "$V = \\tfrac13\\pi r^2 h = \\tfrac13\\pi\\cdot "
                           "%d\\cdot %d = %s$. Forgetting the $\\tfrac13$ "
                           "gives the cylinder volume $%s$."
                           % (r * r, h, piL(k), piL(r * r * h)),
            "check": ["Rational(1,3)*pi*%d**2*%d == %d*pi" % (r, h, k)],
        })
    return out


# --- cylinders-and-cones: axial sections --------------------------------------

AXIAL_CYL = [(2, 5), (3, 4), (4, 3), (5, 6), (3, 7), (6, 5)]
AXIAL_CONE = [(3, 4), (4, 5), (5, 4), (6, 7), (2, 9), (5, 8)]


def gen_axial_section():
    out = []
    idx = 0
    for (r, h), (rc, hc) in zip(AXIAL_CYL, AXIAL_CONE):
        # cylinder: rectangle 2r x h
        pos = idx % 4
        S = 2 * r * h
        cands = [(intL(r * h), r * h), (piL(r * r * h), r * r * h * pi),
                 (intL(2 * r + h), 2 * r + h)]
        opts, ci = build_latex_options((intL(S), S), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A cylinder has base radius $%d$ and height $%d$. "
                         "Find the area of its axial section." % (r, h),
            "options": opts, "correctIndex": ci,
            "explanation": "The axial section of a cylinder is a rectangle "
                           "with sides $2r = %d$ and $h = %d$: area $%d$. "
                           "Using the radius instead of the diameter gives "
                           "$%d$." % (2 * r, h, S, r * h),
            "check": ["2*%d*%d == %d" % (r, h, S)],
        })
        idx += 1
        # cone: isosceles triangle, base 2r, height h
        pos = idx % 4
        S = rc * hc
        cands = [(intL(2 * rc * hc), 2 * rc * hc),
                 (piL(rc * hc), rc * hc * pi),
                 (intL(rc + hc), rc + hc)]
        opts, ci = build_latex_options((intL(S), S), cands, pos,
                                       latex_of=intL)
        out.append({
            "statement": "A cone has base radius $%d$ and height $%d$. Find "
                         "the area of its axial section." % (rc, hc),
            "options": opts, "correctIndex": ci,
            "explanation": "The axial section of a cone is a triangle with "
                           "base $2r = %d$ and height $%d$: $\\tfrac12\\cdot "
                           "%d\\cdot %d = %d$. Forgetting the $\\tfrac12$ "
                           "(treating it as a rectangle) gives $%d$."
                           % (2 * rc, hc, 2 * rc, hc, S, 2 * rc * hc),
            "check": ["Rational(1,2)*2*%d*%d == %d" % (rc, hc, S)],
        })
        idx += 1
    return out


# --- spheres: exact sphere volume ---------------------------------------------

def gen_sphere_volume():
    out = []
    for idx, R in enumerate(range(2, 14)):
        pos = idx % 4
        k = Rational(4 * R ** 3, 3)
        cands = [(piL(4 * R * R), 4 * R * R * pi),
                 (piL(R ** 3), R ** 3 * pi),
                 (piL(4 * R ** 3), 4 * R ** 3 * pi)] + _pi_buffer(k)
        opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
        out.append({
            "statement": "A sphere has radius $%d$. Find its volume, "
                         "exactly." % R,
            "options": opts, "correctIndex": ci,
            "explanation": "$V = \\tfrac43\\pi R^3 = \\tfrac43\\pi\\cdot %d "
                           "= %s$. The classic mix-up reaches for the "
                           "surface-area formula $4\\pi R^2$ instead of the "
                           "volume." % (R ** 3, piL(k)),
            "check": ["Rational(4,3)*pi*%d**3 == Rational(%d,3)*pi"
                      % (R, 4 * R ** 3)],
        })
    return out


# --- spheres: hemisphere total surface & volume --------------------------------

HEMI_SURF = (2, 3, 4, 5, 6, 7)
HEMI_VOL = (3, 6, 2, 4, 5, 9)


def gen_hemisphere():
    out = []
    idx = 0
    for R_s, R_v in zip(HEMI_SURF, HEMI_VOL):
        # total surface = curved 2*pi*R^2 + flat disk pi*R^2
        pos = idx % 4
        k = 3 * R_s * R_s
        cands = [(piL(2 * R_s * R_s), 2 * R_s * R_s * pi),
                 (piL(4 * R_s * R_s), 4 * R_s * R_s * pi),
                 (piL(R_s * R_s), R_s * R_s * pi)] + _pi_buffer(k)
        opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
        out.append({
            "statement": "A hemisphere has radius $%d$. Find its total "
                         "surface area (curved surface plus the flat base "
                         "disk), exactly." % R_s,
            "options": opts, "correctIndex": ci,
            "explanation": "Half the sphere's surface plus the base disk: "
                           "$2\\pi R^2 + \\pi R^2 = 3\\pi R^2 = %s$. "
                           "Stopping at the curved part $%s$ forgets the "
                           "disk." % (piL(k), piL(2 * R_s * R_s)),
            "check": ["2*pi*%d**2 + pi*%d**2 == %d*pi" % (R_s, R_s, k)],
        })
        idx += 1
        # volume = half of 4/3*pi*R^3
        pos = idx % 4
        k = Rational(2 * R_v ** 3, 3)
        cands = [(piL(Rational(4 * R_v ** 3, 3)),
                  Rational(4 * R_v ** 3, 3) * pi),
                 (piL(2 * R_v ** 3), 2 * R_v ** 3 * pi),
                 (piL(R_v ** 3), R_v ** 3 * pi)] + _pi_buffer(k)
        opts, ci = build_latex_options((piL(k), k * pi), cands, pos)
        out.append({
            "statement": "A hemisphere has radius $%d$. Find its volume, "
                         "exactly." % R_v,
            "options": opts, "correctIndex": ci,
            "explanation": "Half the sphere's volume: $\\tfrac12\\cdot"
                           "\\tfrac43\\pi R^3 = \\tfrac23\\pi\\cdot %d = "
                           "%s$. Taking the full $\\tfrac43\\pi R^3 = %s$ "
                           "forgets the halving."
                           % (R_v ** 3, piL(k),
                              piL(Rational(4 * R_v ** 3, 3))),
            "check": ["Rational(2,3)*pi*%d**3 == Rational(%d,3)*pi"
                      % (R_v, 2 * R_v ** 3)],
        })
        idx += 1
    return out


EXTRA_FORMS_META = [
    ("classify-edge-pair", "Cube edges: parallel, intersecting or skew?", 1,
     "SOLID-clsf", "lines-and-planes-in-space", "clsf",
     gen_classify_edge_pair),
    ("diagonal-projection", "A slanted segment & its projection", 2,
     "SOLID-proj", "lines-and-planes-in-space", "proj",
     gen_diagonal_projection),
    ("cube-surface-volume", "Cube surface area & volume", 1, "SOLID-csv",
     "prisms-and-the-cube", "csv", gen_cube_surface_volume),
    ("prism-lateral", "Lateral surface of a right prism", 2, "SOLID-plat",
     "prisms-and-the-cube", "plat", gen_prism_lateral),
    ("pyramid-lateral", "Lateral surface of a regular pyramid", 2,
     "SOLID-pyl", "pyramids", "pyl", gen_pyramid_lateral),
    ("pyramid-base-from-volume", "Base side of a pyramid from its volume", 3,
     "SOLID-pbv", "pyramids", "pbv", gen_pyramid_base_side),
    ("cone-volume", "Cone volume", 1, "SOLID-cvol", "cylinders-and-cones",
     "cvol", gen_cone_volume),
    ("axial-section", "Axial sections of a cylinder and a cone", 2,
     "SOLID-axial", "cylinders-and-cones", "axial", gen_axial_section),
    ("sphere-volume-exact", "Sphere volume", 1, "SOLID-svol", "spheres",
     "svol", gen_sphere_volume),
    ("hemisphere", "Hemisphere: total surface & volume", 2, "SOLID-hemi",
     "spheres", "hemi", gen_hemisphere),
]


def _extra_new_forms():
    """Appended drill forms (12-variant target, floor 10)."""
    forms = []
    for fid, title, level, skill, unit, ab, gen in EXTRA_FORMS_META:
        raw = gen()
        assert len(raw) >= 10, "%s: only %d variants" % (fid, len(raw))
        variants = []
        for i, v in enumerate(raw):
            vd = {"id": "SOLID-%s-v%02d" % (ab, i + 1)}
            vd.update(v)
            variants.append(vd)
        forms.append({"id": fid, "title": title, "level": level,
                      "skill": skill, "unit": unit, "variants": variants})
    return forms


# --- blind re-solvers for the appended drill forms ---------------------------

def _r_classify_edge_pair(s):
    m = re.search(r"edges \$([A-D](?:_1)?[A-D](?:_1)?)\$ and "
                  r"\$([A-D](?:_1)?[A-D](?:_1)?)\$", s)
    cls, _, _ = _edge_relation(m.group(1), m.group(2))
    return ("opt", cls)


def _r_diagonal_projection(s):
    h = int(re.search(r"height \$(\d+)\$", s).group(1))
    m = re.search(r"projection on the plane has length \$(\d+)\$", s)
    if m:
        p = int(m.group(1))
        return ("num", sqrt(p * p + h * h))
    d = int(re.search(r"segment of length \$(\d+)\$", s).group(1))
    return ("num", sqrt(d * d - h * h))


def _r_cube_surface_volume(s):
    m = re.search(r"surface area \$(\d+)\$", s)
    if m:
        return ("num", sqrt(Rational(int(m.group(1)), 6)))
    a = int(re.search(r"edge \$(\d+)\$", s).group(1))
    if "volume" in s:
        return ("num", a ** 3)
    return ("num", 6 * a * a)


def _r_prism_lateral(s):
    m = re.search(r"perimeter \$(\d+)\$ and height \$(\d+)\$", s)
    return ("num", int(m.group(1)) * int(m.group(2)))


def _r_pyramid_lateral(s):
    m = re.search(r"base side \$(\d+)\$ and slant height \$(\d+)\$", s)
    return ("num", 2 * int(m.group(1)) * int(m.group(2)))


def _r_pyramid_base_side(s):
    m = re.search(r"volume \$(\d+)\$ and height \$(\d+)\$", s)
    V, h = int(m.group(1)), int(m.group(2))
    return ("num", sqrt(Rational(3 * V, h)))


def _r_cone_volume(s):
    m = re.search(r"radius \$(\d+)\$ and height \$(\d+)\$", s)
    r, h = int(m.group(1)), int(m.group(2))
    return ("num", Rational(1, 3) * pi * r * r * h)


def _r_axial_section(s):
    m = re.search(r"radius \$(\d+)\$ and height \$(\d+)\$", s)
    r, h = int(m.group(1)), int(m.group(2))
    if "cylinder" in s:
        return ("num", 2 * r * h)
    return ("num", r * h)


def _r_sphere_volume(s):
    R = int(re.search(r"radius \$(\d+)\$", s).group(1))
    return ("num", Rational(4, 3) * pi * R ** 3)


def _r_hemisphere(s):
    R = int(re.search(r"radius \$(\d+)\$", s).group(1))
    if "volume" in s:
        return ("num", Rational(2, 3) * pi * R ** 3)
    return ("num", 3 * pi * R * R)


RESOLVERS.update({
    "classify-edge-pair": _r_classify_edge_pair,
    "diagonal-projection": _r_diagonal_projection,
    "cube-surface-volume": _r_cube_surface_volume,
    "prism-lateral": _r_prism_lateral,
    "pyramid-lateral": _r_pyramid_lateral,
    "pyramid-base-from-volume": _r_pyramid_base_side,
    "cone-volume": _r_cone_volume,
    "axial-section": _r_axial_section,
    "sphere-volume-exact": _r_sphere_volume,
    "hemisphere": _r_hemisphere,
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
