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
