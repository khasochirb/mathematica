# -*- coding: utf-8 -*-
"""Problem-bank subject: Vectors & Matrices — mirrors the /math/vectors-matrices course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/vectors_matrices.py` to
self-check.
"""
import os
import re
import sys

from sympy import Rational, simplify, sqrt, sympify

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

import vecmat_more  # noqa: E402 — the units 7-8 forms

SLUG = "vectors-matrices"
TITLE = "Vectors & Matrices"
TITLE_MN = "Вектор ба матриц"
BLURB = ("Unit-by-unit practice for the Vectors & Matrices course — components and magnitudes to determinants and systems.")

UNITS = [
    {"id": "vectors-and-coordinates", "title": "Vectors & Coordinates",
     "blurb": "What a vector is, components and magnitude, equal/opposite/parallel vectors, and unit vectors."},
    {"id": "vector-arithmetic", "title": "Vector Arithmetic",
     "blurb": "Tip-to-tail addition, scaling, subtraction, vectors inside figures, and the section formula."},
    {"id": "the-dot-product", "title": "The Dot Product",
     "blurb": "u·v two ways, angles from the sign, perpendicularity tests, and the |u+v|² toolbox."},
    {"id": "vectors-in-space", "title": "Vectors in Space",
     "blurb": "The third coordinate: 3D magnitudes and dot products, the box diagonal, and normal vectors of planes."},
    {"id": "matrices-and-operations", "title": "Matrices & Operations",
     "blurb": "Grids with an address system: entrywise arithmetic, row-times-column multiplication, identity and powers."},
    {"id": "determinants-and-inverses", "title": "Determinants, Inverses & Systems",
     "blurb": "ad − bc, the 2×2 inverse, Cramer's rule, and matrices as transformations — the capstone."},
    {"id": "transformation-matrices", "title": "Transformation Matrices",
     "blurb": "Reflections, rotations, enlargements and translations as matrices, then composing and naming them."},
    {"id": "systems-in-three-unknowns", "title": "Systems in Three Unknowns",
     "blurb": "Augmented matrices and row operations, Gauss's method, 3×3 determinants and inverses, and Cramer's rule."},
]

# No legacy forms: this subject is authored fresh.
REMAP = {}
SOURCES = []

# form id -> fn(statement) -> ("num", sympy value) | ("opt", exact option str)
RESOLVERS = {}


# ---------------------------------------------------------------------------
# formatting helpers (house style)
# ---------------------------------------------------------------------------

def L(v):
    """LaTeX for an integer/rational value (no surrounding $)."""
    v = sympify(v)
    if getattr(v, "q", 1) == 1:
        return str(int(v))
    if v < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def numO(v):
    """A numeric option string."""
    return "$" + L(v) + "$"


def pair(x, y):
    """A coordinate-pair option string, semicolon house style."""
    return "$(%s; %s)$" % (L(x), L(y))


def trip(x, y, z):
    return "$(%s; %s; %s)$" % (L(x), L(y), L(z))


def vec2(name, x, y):
    """Inline latex (no $) for \\vec{name} = (x; y)."""
    return "\\vec{%s} = (%s; %s)" % (name, L(x), L(y))


def vec3(name, x, y, z):
    return "\\vec{%s} = (%s; %s; %s)" % (name, L(x), L(y), L(z))


def pm(a, b, c, d):
    """Inline latex for a 2x2 pmatrix."""
    return ("\\begin{pmatrix} %d & %d \\\\ %d & %d \\end{pmatrix}"
            % (a, b, c, d))


def place(correct, cands, pos):
    """Insert `correct` at index pos among the first 3 candidate strings that
    are distinct from it and from each other. Crashes on shortage."""
    picked = []
    for c in cands:
        if c == correct or c in picked:
            continue
        picked.append(c)
        if len(picked) == 3:
            break
    assert len(picked) == 3, "distractor shortage for %s from %r" % (
        correct, cands)
    opts = list(picked)
    opts.insert(pos, correct)
    assert len(set(opts)) == 4
    return opts


def _rt_fig(w, h):
    """True-scale extracted right triangle: right angle at the origin,
    horizontal leg w, vertical leg h, hypotenuse '?' in the accent color."""
    return {
        "points": [
            {"id": "A", "x": 0, "y": 0, "label": ""},
            {"id": "B", "x": w, "y": 0, "label": ""},
            {"id": "C", "x": 0, "y": h, "label": ""},
        ],
        "objects": [
            {"kind": "segment", "from": "A", "to": "B", "label": str(w)},
            {"kind": "segment", "from": "A", "to": "C", "label": str(h),
             "color": "blue"},
            {"kind": "segment", "from": "B", "to": "C", "label": "?",
             "color": "accent"},
            {"kind": "angle", "at": "A", "from": "B", "to": "C",
             "right": True},
        ],
    }


PAIR_RE = r"\((-?\d+); (-?\d+)\)"
TRIP_RE = r"\((-?\d+); (-?\d+); (-?\d+)\)"


def _pair_after(s, prefix):
    m = re.search(prefix + " = " + PAIR_RE, s)
    return int(m.group(1)), int(m.group(2))


def _trip_after(s, prefix):
    m = re.search(prefix + " = " + TRIP_RE, s)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


# ---------------------------------------------------------------------------
# unit: vectors-and-coordinates
# ---------------------------------------------------------------------------

FROM_PTS = [
    (2, 3, 5, -1), (1, 2, 4, 7), (-3, 4, 2, 1), (5, -2, 1, 3),
    (4, 1, -2, 5), (-1, -3, 4, 3), (3, 7, 9, 2), (-2, 5, 3, -4),
    (6, 0, 2, 7), (-5, -1, -2, 3), (7, 2, 3, -3), (0, -4, 6, 1),
]


def gen_vector_from_points():
    out = []
    for i, (x1, y1, x2, y2) in enumerate(FROM_PTS):
        dx, dy = x2 - x1, y2 - y1
        assert dx != dy and dx != -dy, (x1, y1, x2, y2)
        pos = i % 4
        correct = pair(dx, dy)
        cands = [pair(-dx, -dy), pair(x1 + x2, y1 + y2), pair(dy, dx),
                 pair(dx + 1, dy)]
        out.append({
            "statement": "The points $A = (%d; %d)$ and $B = (%d; %d)$ are "
                         "given. Find the coordinates of $\\vec{AB}$."
                         % (x1, y1, x2, y2),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Tip minus tail: $\\vec{AB} = (x_B - x_A; "
                           "y_B - y_A) = (%d; %d)$. Computing $A - B$ "
                           "instead flips both signs to $(%d; %d)$ — the "
                           "classic direction slip." % (dx, dy, -dx, -dy),
            "check": ["(%d) - (%d) == %d" % (x2, x1, dx),
                      "(%d) - (%d) == %d" % (y2, y1, dy)],
        })
    return out


def _r_vector_from_points(s):
    x1, y1 = _pair_after(s, "A")
    x2, y2 = _pair_after(s, "B")
    return ("opt", pair(x2 - x1, y2 - y1))


MAG_PAIRS = [
    (3, 4, 5), (-6, 8, 10), (5, -12, 13), (-8, -15, 17), (9, 12, 15),
    (-7, 24, 25), (20, -21, 29), (-12, 5, 13), (6, -8, 10), (8, 15, 17),
    (-20, 15, 25), (12, -16, 20),
]


def gen_vector_magnitude():
    out = []
    for i, (a, b, c) in enumerate(MAG_PAIRS):
        assert a * a + b * b == c * c
        pos = i % 4
        correct = numO(c)
        cands = [numO(abs(a) + abs(b)), numO(a + b), numO(c * c),
                 numO(c + 1), numO(c - 1)]
        out.append({
            "statement": "Find the magnitude $|\\vec{a}|$ of the vector "
                         "$%s$." % vec2("a", a, b),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$|\\vec{a}| = \\sqrt{(%d)^2 + (%d)^2} = "
                           "\\sqrt{%d} = %d$. Adding the components' "
                           "absolute values, $%d + %d = %d$, skips "
                           "Pythagoras — the classic slip."
                           % (a, b, c * c, c, abs(a), abs(b),
                              abs(a) + abs(b)),
            "check": ["sqrt((%d)**2 + (%d)**2) == %d" % (a, b, c)],
            "geoFigure": _rt_fig(abs(a), abs(b)),
        })
    return out


def _r_vector_magnitude(s):
    a, b = _pair_after(s, r"\\vec\{a\}")
    return ("num", sqrt(a * a + b * b))


# ---------------------------------------------------------------------------
# unit: vector-arithmetic
# ---------------------------------------------------------------------------

COMB_DATA = [
    (2, 3, 2, -1, 3, 4), (1, -2, 3, 5, 1, 2), (3, 1, -1, 2, 4, -3),
    (-1, 2, 5, 3, 2, -2), (2, -3, 1, 4, -2, 1), (3, 2, 2, 0, -1, 5),
    (1, 3, -4, 2, 2, 3), (-2, 1, 3, -2, 5, 4), (2, 1, 4, 3, -3, 2),
    (3, -1, 1, -2, 2, -5), (1, 2, 6, -3, -2, 4), (-3, 2, -1, 1, 3, 2),
]


def _comb_latex(m, n):
    if m == 1:
        am = "\\vec{a}"
    elif m == -1:
        am = "-\\vec{a}"
    else:
        am = "%d\\vec{a}" % m
    sign = "+" if n > 0 else "-"
    bn = "\\vec{b}" if abs(n) == 1 else "%d\\vec{b}" % abs(n)
    return "%s %s %s" % (am, sign, bn)


def gen_vector_combine():
    out = []
    for i, (m, n, a1, a2, b1, b2) in enumerate(COMB_DATA):
        assert m != n
        pos = i % 4
        rx, ry = m * a1 + n * b1, m * a2 + n * b2
        correct = pair(rx, ry)
        cands = [pair(n * a1 + m * b1, n * a2 + m * b2),      # m/n swapped
                 pair(m * a1 - n * b1, m * a2 - n * b2),      # subtracted
                 pair(a1 + b1, a2 + b2),                       # scalars lost
                 pair(rx + 1, ry)]
        out.append({
            "statement": "Given $%s$ and $%s$, find $%s$."
                         % (vec2("a", a1, a2), vec2("b", b1, b2),
                            _comb_latex(m, n)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Scale each vector first, then add matching "
                           "components: $(%d; %d)$. Adding "
                           "$\\vec{a} + \\vec{b}$ and forgetting the "
                           "scalars gives $(%d; %d)$ — the classic slip."
                           % (rx, ry, a1 + b1, a2 + b2),
            "check": ["(%d)*(%d) + (%d)*(%d) == %d" % (m, a1, n, b1, rx),
                      "(%d)*(%d) + (%d)*(%d) == %d" % (m, a2, n, b2, ry)],
        })
    return out


def _r_vector_combine(s):
    a1, a2 = _pair_after(s, r"\\vec\{a\}")
    b1, b2 = _pair_after(s, r"\\vec\{b\}")
    m = re.search(r"find \$(-?)(\d*)\\vec\{a\} ([+-]) (\d*)\\vec\{b\}\$", s)
    mm = int(m.group(2) or "1") * (-1 if m.group(1) == "-" else 1)
    nn = int(m.group(4) or "1") * (1 if m.group(3) == "+" else -1)
    return ("opt", pair(mm * a1 + nn * b1, mm * a2 + nn * b2))


TIP_DATA = [
    (1, 3, 2, 1), (2, 2, 4, 6), (1, 5, 4, 7), (5, 2, 3, 4),
    (7, 1, 5, 4), (4, 5, 5, 7), (3, 6, 5, 9), (9, 10, 11, 11),
    (3, 11, 4, 13), (8, 3, 7, 5), (1, 2, 3, 1), (6, 4, 6, 5),
]


def _tip_fig(a1, a2, sx, sy):
    return {
        "points": [
            {"id": "O", "x": 0, "y": 0, "label": ""},
            {"id": "P", "x": a1, "y": a2, "label": ""},
            {"id": "Q", "x": sx, "y": sy, "label": ""},
        ],
        "objects": [
            {"kind": "segment", "from": "O", "to": "P", "label": "a"},
            {"kind": "segment", "from": "P", "to": "Q", "label": "b",
             "color": "blue"},
            {"kind": "segment", "from": "O", "to": "Q", "label": "?",
             "color": "accent", "dashed": True},
        ],
    }


def gen_tip_to_tail():
    out = []
    for i, (a1, a2, b1, b2) in enumerate(TIP_DATA):
        sx, sy = a1 + b1, a2 + b2
        c = int(sqrt(sx * sx + sy * sy))
        assert sx * sx + sy * sy == c * c, (a1, a2, b1, b2)
        pos = i % 4
        correct = numO(c)
        cands = [numO(sx + sy), numO(c * c), numO(c + 2), numO(c - 1)]
        out.append({
            "statement": "Let $%s$ and $%s$. Find $|\\vec{a} + \\vec{b}|$."
                         % (vec2("a", a1, a2), vec2("b", b1, b2)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "First add tip-to-tail: $\\vec{a} + \\vec{b} = "
                           "(%d; %d)$; then $\\sqrt{%d^2 + %d^2} = %d$. "
                           "Adding the coordinates, $%d + %d = %d$, skips "
                           "Pythagoras — the classic slip."
                           % (sx, sy, sx, sy, c, sx, sy, sx + sy),
            "check": ["sqrt(((%d) + (%d))**2 + ((%d) + (%d))**2) == %d"
                      % (a1, b1, a2, b2, c)],
            "geoFigure": _tip_fig(a1, a2, sx, sy),
        })
    return out


def _r_tip_to_tail(s):
    a1, a2 = _pair_after(s, r"\\vec\{a\}")
    b1, b2 = _pair_after(s, r"\\vec\{b\}")
    return ("num", sqrt((a1 + b1) ** 2 + (a2 + b2) ** 2))


PAR_DATA = [
    (2, 3, 4), (3, 5, 6), (4, -3, 8), (5, 2, -10), (2, -7, 6), (3, 4, -9),
    (6, 4, 3), (4, 6, 2), (5, -3, 10), (2, 5, -8), (7, 2, 14), (3, -8, 6),
]


def gen_parallel_scalar():
    out = []
    for i, (p, q, r) in enumerate(PAR_DATA):
        k = Rational(q * r, p)
        assert k.q == 1, (p, q, r)
        k = int(k)
        pos = i % 4
        correct = numO(k)
        cands = [numO(Rational(p * q, r)), numO(r - p + q), numO(-k),
                 numO(k + 1)]
        out.append({
            "statement": "The vectors $%s$ and $\\vec{b} = (%d; k)$ are "
                         "parallel. Find $k$." % (vec2("a", p, q), r),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Parallel vectors have proportional coordinates: "
                           "$\\frac{k}{%d} = \\frac{%d}{%d}$, so $k = "
                           "\\frac{%d \\cdot %d}{%d} = %d$. Matching the "
                           "wrong pair gives $\\frac{p\\,q}{r} = %s$ — the "
                           "classic cross-multiplication slip."
                           % (r, q, p, q, r, p, k, L(Rational(p * q, r))),
            "check": ["((%d)*(%d))/(%d) == %d" % (q, r, p, k),
                      "(%d)*(%d) - (%d)*(%d) == 0" % (p, k, q, r)],
        })
    return out


def _r_parallel_scalar(s):
    p, q = _pair_after(s, r"\\vec\{a\}")
    r = int(re.search(r"\\vec\{b\} = \((-?\d+); k\)", s).group(1))
    return ("num", Rational(q * r, p))


# ---------------------------------------------------------------------------
# unit: the-dot-product
# ---------------------------------------------------------------------------

DOT_DATA = [
    (2, 3, 4, 1), (3, -2, 5, 4), (-1, 4, 3, 2), (5, 2, -3, 4),
    (2, -5, -4, 3), (4, 1, 2, 7), (-3, 2, 4, 5), (6, -1, 2, 5),
    (1, 7, 3, -2), (-2, -3, 5, 1), (3, 4, 1, -6), (7, 2, -1, 4),
]


def gen_dot_value():
    out = []
    for i, (a, b, c, d) in enumerate(DOT_DATA):
        D = a * c + b * d
        cross = a * d + b * c
        pos = i % 4
        correct = numO(D)
        cands = [numO(cross), numO((a + c) * (b + d)), numO(a + b + c + d),
                 numO(D + 1), numO(D - 1)]
        out.append({
            "statement": "Compute the dot product $\\vec{a} \\cdot "
                         "\\vec{b}$ for $%s$ and $%s$."
                         % (vec2("a", a, b), vec2("b", c, d)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Multiply matching components and add: "
                           "$(%d)(%d) + (%d)(%d) = %d$. Crossing the "
                           "components, $a_1 b_2 + a_2 b_1 = %d$, is the "
                           "classic slip." % (a, c, b, d, D, cross),
            "check": ["(%d)*(%d) + (%d)*(%d) == %d" % (a, c, b, d, D)],
        })
    return out


def _r_dot_value(s):
    a, b = _pair_after(s, r"\\vec\{a\}")
    c, d = _pair_after(s, r"\\vec\{b\}")
    return ("num", a * c + b * d)


PERP_DATA = [
    (2, 3, 4), (3, 2, 6), (2, -5, 4), (5, 4, -10), (3, -7, 6), (4, 3, -8),
    (2, 9, -4), (6, -4, 3), (7, 2, -7), (2, -3, -8), (5, 10, 2), (3, -2, 9),
]


def gen_perpendicular_k():
    out = []
    for i, (p, q, r) in enumerate(PERP_DATA):
        k = Rational(-q * r, p)
        assert k.q == 1 and k != 0, (p, q, r)
        k = int(k)
        pos = i % 4
        correct = numO(k)
        cands = [numO(-k), numO(r - q), numO(p + q + r), numO(k + 1),
                 numO(k - 1)]
        out.append({
            "statement": "The vectors $%s$ and $\\vec{b} = (k; %d)$ are "
                         "perpendicular. Find $k$." % (vec2("a", p, q), r),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Perpendicular means zero dot product: "
                           "$%d k + (%d)(%d) = 0$, so $k = %d$. Dropping "
                           "the minus sign when solving gives $%d$ — the "
                           "classic slip." % (p, q, r, k, -k),
            "check": ["(%d)*(%d) + (%d)*(%d) == 0" % (p, k, q, r)],
        })
    return out


def _r_perpendicular_k(s):
    p, q = _pair_after(s, r"\\vec\{a\}")
    r = int(re.search(r"\\vec\{b\} = \(k; (-?\d+)\)", s).group(1))
    return ("num", Rational(-q * r, p))


ANG_DATA = [
    (2, 0, 3, 3, 45), (4, 0, 1, 1, 45), (5, 0, 2, 2, 45),
    (3, 0, 0, 5, 90), (2, 3, -3, 2, 90), (1, 4, -4, 1, 90),
    (1, 2, 2, 4, 0), (3, 1, 6, 2, 0),
    (2, 1, -4, -2, 180), (1, 3, -2, -6, 180),
    (3, 0, -2, 2, 135), (1, 0, -5, 5, 135),
]

ANG_DIST = {45: (135, 60, 90), 90: (0, 45, 180), 0: (90, 180, 45),
            180: (0, 90, 135), 135: (45, 60, 90)}
ANG_COS = {0: "1", 45: "\\frac{\\sqrt{2}}{2}", 90: "0",
           135: "-\\frac{\\sqrt{2}}{2}", 180: "-1"}


def gen_vector_angle():
    out = []
    for i, (a1, a2, b1, b2, deg) in enumerate(ANG_DATA):
        pos = i % 4
        dot = a1 * b1 + a2 * b2
        na, nb = a1 * a1 + a2 * a2, b1 * b1 + b2 * b2
        correct = "$%d°$" % deg
        cands = ["$%d°$" % d for d in ANG_DIST[deg]]
        if deg in (45, 135):
            wrong = ("Reading off the supplement $%d°$ (wrong sign of the "
                     "cosine) is the classic slip." % (180 - deg))
        elif deg == 90:
            wrong = ("A zero dot product means perpendicular — answering "
                     "$0°$ (parallel) is the classic confusion.")
        elif deg == 0:
            wrong = ("Answering $180°$ ignores that the scale factor is "
                     "positive — the classic direction slip.")
        else:
            wrong = ("Answering $0°$ ignores the negative scale factor — "
                     "the classic direction slip.")
        out.append({
            "statement": "Find the angle between $%s$ and $%s$."
                         % (vec2("a", a1, a2), vec2("b", b1, b2)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$\\cos\\theta = \\frac{\\vec{a}\\cdot\\vec{b}}"
                           "{|\\vec{a}||\\vec{b}|} = %s$, so $\\theta = "
                           "%d°$. %s" % (ANG_COS[deg], deg, wrong),
            "check": ["cos(pi*%d/180) == (%d)/(sqrt(%d)*sqrt(%d))"
                      % (deg, dot, na, nb)],
        })
    return out


def _r_vector_angle(s):
    a1, a2 = _pair_after(s, r"\\vec\{a\}")
    b1, b2 = _pair_after(s, r"\\vec\{b\}")
    cosv = (a1 * b1 + a2 * b2) / (sqrt(a1 * a1 + a2 * a2)
                                  * sqrt(b1 * b1 + b2 * b2))
    for deg, target in ((0, sympify(1)), (45, sqrt(2) / 2), (90, sympify(0)),
                        (135, -sqrt(2) / 2), (180, sympify(-1))):
        if simplify(cosv - target) == 0:
            return ("opt", "$%d°$" % deg)
    raise AssertionError("non-special cosine %s" % cosv)


# ---------------------------------------------------------------------------
# unit: vectors-in-space
# ---------------------------------------------------------------------------

M3D_DATA = [
    (1, 2, 2, 3), (2, -3, 6, 7), (-1, 4, 8, 9), (4, -4, 7, 9),
    (2, 6, -9, 11), (-6, 6, 7, 11), (2, -2, 1, 3), (6, -2, -3, 7),
    (8, 1, -4, 9), (-7, 4, 4, 9), (9, -2, 6, 11), (-6, 7, 6, 11),
]


def gen_magnitude_3d():
    out = []
    for i, (a, b, c, d) in enumerate(M3D_DATA):
        assert a * a + b * b + c * c == d * d
        pos = i % 4
        sabs = abs(a) + abs(b) + abs(c)
        correct = numO(d)
        cands = [numO(sabs), numO(d * d), numO(d + 1), numO(d - 1)]
        out.append({
            "statement": "Find the magnitude $|\\vec{a}|$ of the space "
                         "vector $%s$." % vec3("a", a, b, c),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$|\\vec{a}| = \\sqrt{(%d)^2 + (%d)^2 + (%d)^2} "
                           "= \\sqrt{%d} = %d$. Adding the components' "
                           "absolute values gives $%d$ — the classic "
                           "no-Pythagoras slip." % (a, b, c, d * d, d, sabs),
            "check": ["sqrt((%d)**2 + (%d)**2 + (%d)**2) == %d"
                      % (a, b, c, d)],
        })
    return out


def _r_magnitude_3d(s):
    a, b, c = _trip_after(s, r"\\vec\{a\}")
    return ("num", sqrt(a * a + b * b + c * c))


MID3_DATA = [
    (2, 4, 6, 4, 0, 2), (1, 3, 5, 3, 7, 1), (-2, 4, 0, 6, -2, 8),
    (5, -1, 3, -1, 5, 7), (0, 2, -4, 6, 4, 2), (4, 4, 2, -2, 0, 6),
    (-3, 1, 5, 7, 3, -1), (6, -2, 4, 2, 8, 0), (1, -5, 3, 5, 1, -7),
    (-4, 2, 6, 0, 6, -2), (3, 3, -5, 7, -1, 1), (2, 0, 8, 6, 4, -2),
]


def gen_midpoint_3d():
    out = []
    for i, (ax, ay, az, bx, by, bz) in enumerate(MID3_DATA):
        assert (ax + bx) % 2 == 0 and (ay + by) % 2 == 0 and (az + bz) % 2 == 0
        mx, my, mz = (ax + bx) // 2, (ay + by) // 2, (az + bz) // 2
        assert ax != mx
        pos = i % 4
        correct = trip(mx, my, mz)
        cands = [trip(Rational(bx - ax, 2), Rational(by - ay, 2),
                      Rational(bz - az, 2)),
                 trip(ax + bx, ay + by, az + bz),
                 trip(ax, my, mz),
                 trip(mx + 1, my, mz)]
        out.append({
            "statement": "Find the midpoint of the segment with endpoints "
                         "$A = (%d; %d; %d)$ and $B = (%d; %d; %d)$."
                         % (ax, ay, az, bx, by, bz),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Average each coordinate: $\\left(\\frac{%d+%d}"
                           "{2}; \\frac{%d+%d}{2}; \\frac{%d+%d}{2}\\right)"
                           " = (%d; %d; %d)$. Halving the difference "
                           "$B - A$ gives half of $\\vec{AB}$, not the "
                           "midpoint — the classic mix-up."
                           % (ax, bx, ay, by, az, bz, mx, my, mz),
            "check": ["((%d) + (%d))/2 == %d" % (ax, bx, mx),
                      "((%d) + (%d))/2 == %d" % (ay, by, my),
                      "((%d) + (%d))/2 == %d" % (az, bz, mz)],
        })
    return out


def _r_midpoint_3d(s):
    ax, ay, az = _trip_after(s, "A")
    bx, by, bz = _trip_after(s, "B")
    return ("opt", trip(Rational(ax + bx, 2), Rational(ay + by, 2),
                        Rational(az + bz, 2)))


DOT3_DATA = [
    (1, 2, 3, 4, -1, 2), (2, -3, 1, 3, 2, 5), (-1, 4, 2, 5, 1, -3),
    (3, 0, -2, 1, 6, 4), (2, 5, -1, -2, 3, 6), (4, -2, 3, 2, 1, -2),
]
DOT3_PERP = [
    (1, 2, 2, 4, 3), (2, -1, 3, 3, 0), (3, 2, -4, 2, 5),
    (1, -3, 2, 5, 1), (2, 2, 5, -3, -2), (4, -1, -3, 2, 5),
]


def gen_dot_3d():
    out = []
    idx = 0
    for (a1, a2, a3, b1, b2, b3), (p1, p2, p3, q1, q2) in zip(DOT3_DATA,
                                                              DOT3_PERP):
        # (a) plain 3D dot product
        pos = idx % 4
        D = a1 * b1 + a2 * b2 + a3 * b3
        dropz = a1 * b1 + a2 * b2
        slip = D - 2 * a3 * b3
        correct = numO(D)
        cands = [numO(dropz), numO(slip), numO(a1 + a2 + a3 + b1 + b2 + b3),
                 numO(D + 1), numO(D - 1)]
        out.append({
            "statement": "Compute $\\vec{a} \\cdot \\vec{b}$ for $%s$ and "
                         "$%s$." % (vec3("a", a1, a2, a3),
                                    vec3("b", b1, b2, b3)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Sum all three products: $(%d)(%d) + (%d)(%d) + "
                           "(%d)(%d) = %d$. Dropping the $z$-term out of "
                           "2D habit gives $%d$ — the classic slip."
                           % (a1, b1, a2, b2, a3, b3, D, dropz),
            "check": ["(%d)*(%d) + (%d)*(%d) + (%d)*(%d) == %d"
                      % (a1, b1, a2, b2, a3, b3, D)],
        })
        idx += 1
        # (b) engineered perpendicularity: solve for k
        pos = idx % 4
        part = p1 * q1 + p2 * q2
        k = Rational(-part, p3)
        assert k.q == 1 and k != 0, (p1, p2, p3, q1, q2)
        k = int(k)
        correct = numO(k)
        cands = [numO(-k), numO(part), numO(-part), numO(k + 1)]
        out.append({
            "statement": "Find $k$ so that $%s$ and $\\vec{b} = "
                         "(%d; %d; k)$ are perpendicular."
                         % (vec3("a", p1, p2, p3), q1, q2),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Set the dot product to zero: $(%d)(%d) + "
                           "(%d)(%d) + %d k = 0$, so $k = %d$. Flipping "
                           "the sign when isolating $k$ gives $%d$ — the "
                           "classic slip." % (p1, q1, p2, q2, p3, k, -k),
            "check": ["(%d)*(%d) + (%d)*(%d) + (%d)*(%d) == 0"
                      % (p1, q1, p2, q2, p3, k)],
        })
        idx += 1
    return out


def _r_dot_3d(s):
    if "perpendicular" in s:
        a1, a2, a3 = _trip_after(s, r"\\vec\{a\}")
        m = re.search(r"\\vec\{b\} = \((-?\d+); (-?\d+); k\)", s)
        b1, b2 = int(m.group(1)), int(m.group(2))
        return ("num", Rational(-(a1 * b1 + a2 * b2), a3))
    a1, a2, a3 = _trip_after(s, r"\\vec\{a\}")
    b1, b2, b3 = _trip_after(s, r"\\vec\{b\}")
    return ("num", a1 * b1 + a2 * b2 + a3 * b3)


# ---------------------------------------------------------------------------
# unit: matrices-and-operations
# ---------------------------------------------------------------------------

MENT_DATA = [
    # (A: a b c d), (B: e f g h), m — answer is b + m*f
    ((2, 1, 4, 3), (5, 3, 2, 6), 2), ((1, 4, 2, 5), (3, -2, 6, 1), 3),
    ((3, -2, 1, 4), (2, 5, -3, 1), 2), ((5, 2, 3, 1), (1, 4, 2, -2), 3),
    ((2, 6, -1, 3), (4, 1, 5, 2), 2), ((1, -3, 2, 6), (2, 4, 1, 3), 2),
    ((4, 5, 1, 2), (3, -1, 6, 4), 3), ((2, 3, 5, -1), (1, 6, 3, 4), 2),
    ((3, 1, 2, 5), ((-2), 3, 4, 1), 3), ((6, -4, 3, 2), (2, 2, -1, 5), 2),
    ((1, 2, 4, 3), (5, -3, 2, 6), 3), ((2, 7, 1, 4), (3, 3, 4, -2), 2),
]


def gen_matrix_entry():
    out = []
    for i, (A, B, m) in enumerate(MENT_DATA):
        a, b, c, d = A
        e, f, g, h = B
        ans = b + m * f
        pos = i % 4
        correct = numO(ans)
        cands = [numO(c + m * g), numO(b + f), numO(b - m * f),
                 numO(ans + 1)]
        out.append({
            "statement": "Let $C = A + %dB$ for the $2\\times 2$ matrices "
                         "$A = %s$ and $B = %s$. Find the entry $c_{12}$ "
                         "(row 1, column 2)."
                         % (m, pm(a, b, c, d), pm(e, f, g, h)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Work entrywise at address $(1, 2)$: $c_{12} = "
                           "%d + %d\\cdot(%d) = %d$. Reading $c_{21}$ (row "
                           "2, column 1) instead gives $%d$ — the classic "
                           "index swap." % (b, m, f, ans, c + m * g),
            "check": ["(%d) + (%d)*(%d) == %d" % (b, m, f, ans)],
        })
    return out


PM_RE = re.compile(r"\\begin\{pmatrix\} (-?\d+) & (-?\d+) \\\\ "
                   r"(-?\d+) & (-?\d+) \\end\{pmatrix\}")


def _r_matrix_entry(s):
    m = int(re.search(r"C = A \+ (\d+)B", s).group(1))
    mats = PM_RE.findall(s)
    (a, b, c, d), (e, f, g, h) = [tuple(int(x) for x in t) for t in mats]
    return ("num", b + m * f)


MPROD_DATA = [
    ((2, 3, 1, 4), (5, 1, 2, 6)), ((1, 2, 3, 5), (4, 2, 1, 3)),
    ((3, -1, 2, 4), (2, 5, 3, 1)), ((2, 4, 1, 3), (-1, 2, 5, 3)),
    ((5, 2, 3, 1), (1, 4, 2, 6)), ((1, 3, 2, -2), (6, 1, 4, 5)),
    ((4, 1, 5, 2), (2, 3, 1, 7)), ((2, -3, 4, 1), (3, 2, 1, 5)),
    ((3, 2, 1, 6), (4, -1, 2, 3)), ((1, 5, 2, 3), (2, 4, 3, 1)),
    ((6, 2, 3, 4), (1, 3, 5, 2)), ((2, 3, 5, 1), (3, 6, 2, 4)),
]


def gen_matrix_product_entry():
    out = []
    for i, (A, B) in enumerate(MPROD_DATA):
        a11, a12, a21, a22 = A
        b11, b12, b21, b22 = B
        ans = a11 * b11 + a12 * b21
        pos = i % 4
        correct = numO(ans)
        cands = [numO(a11 * b11),                       # single product
                 numO(a11 * b11 + a12 * b12),           # row·row slip
                 numO(a21 * b12 + a22 * b22),           # c22 instead
                 numO(ans + 1)]
        out.append({
            "statement": "Let $C = AB$ for $A = %s$ and $B = %s$. Find the "
                         "entry $c_{11}$ (row 1, column 1)."
                         % (pm(*A), pm(*B)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$c_{11}$ is row 1 of $A$ times column 1 of "
                           "$B$: $%d\\cdot%d + %d\\cdot%d = %d$. Stopping "
                           "after the first product gives $%d$ — the "
                           "classic slip."
                           % (a11, b11, a12, b21, ans, a11 * b11),
            "check": ["(%d)*(%d) + (%d)*(%d) == %d"
                      % (a11, b11, a12, b21, ans)],
        })
    return out


def _r_matrix_product_entry(s):
    mats = PM_RE.findall(s)
    A, B = [tuple(int(x) for x in t) for t in mats]
    return ("num", A[0] * B[0] + A[1] * B[2])


# ---------------------------------------------------------------------------
# unit: determinants-and-inverses
# ---------------------------------------------------------------------------

DET_DATA = [
    (2, 3, 1, 4), (3, 1, 2, 5), (4, 2, 3, 5), (1, -2, 3, 4),
    (5, 3, 2, 4), (2, -1, 4, 3), (3, 4, 1, 2), (6, 2, 5, 1),
    (2, 5, 3, 7), (4, -3, 2, 1), (1, 6, 2, 3), (7, 2, 4, 3),
]


def gen_det_2x2():
    out = []
    for i, (a, b, c, d) in enumerate(DET_DATA):
        det = a * d - b * c
        assert det != 0 and b * c != 0
        pos = i % 4
        correct = numO(det)
        cands = [numO(a * d + b * c), numO(a * c - b * d), numO(-det),
                 numO(det + 1)]
        out.append({
            "statement": "Compute the determinant $\\det%s$."
                         % pm(a, b, c, d),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$\\det = ad - bc = %d\\cdot%d - (%d)\\cdot(%d) "
                           "= %d$. Adding the two diagonal products "
                           "instead gives $%d$ — the classic sign slip."
                           % (a, d, b, c, det, a * d + b * c),
            "check": ["(%d)*(%d) - (%d)*(%d) == %d" % (a, d, b, c, det)],
        })
    return out


def _r_det_2x2(s):
    a, b, c, d = (int(x) for x in PM_RE.search(s).groups())
    return ("num", a * d - b * c)


CRAM_DATA = [
    # (a, b, c, d, x0, y0): system a x + b y = e, c x + d y = f
    (3, 2, 5, -4, 2, 1), (2, 1, 1, 3, 3, -1), (1, 2, 3, -1, 4, 2),
    (4, -3, 2, 5, 1, 2), (2, 3, 4, 1, -2, 3), (5, 2, 3, 4, 2, -3),
    (1, 4, 2, 3, 5, 1), (3, -2, 1, 4, 4, 3), (2, 5, 3, 2, 1, 4),
    (6, 1, 2, -3, 2, 5), (1, 3, 4, 2, -3, 4), (4, 3, 2, 7, 3, 2),
]


def _lin_eq(a, b, e):
    """Latex for a x + b y = e with a > 0, b != 0."""
    ax = "x" if a == 1 else "%dx" % a
    sign = "+" if b > 0 else "-"
    by = "y" if abs(b) == 1 else "%dy" % abs(b)
    return "%s %s %s = %d" % (ax, sign, by, e)


def gen_cramer():
    out = []
    for i, (a, b, c, d, x0, y0) in enumerate(CRAM_DATA):
        e, f = a * x0 + b * y0, c * x0 + d * y0
        det = a * d - b * c
        assert det != 0 and x0 != 0 and x0 != y0
        assert Rational(e * d - b * f, det) == x0
        pos = i % 4
        correct = numO(x0)
        cands = [numO(y0), numO(det), numO(-x0), numO(x0 + 1), numO(x0 - 1)]
        out.append({
            "statement": "Solve the system by Cramer's rule: $%s$, $%s$. "
                         "Find $x$." % (_lin_eq(a, b, e), _lin_eq(c, d, f)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$x = \\frac{\\Delta_x}{\\Delta} = "
                           "\\frac{e d - b f}{a d - b c} = \\frac{%d}{%d} "
                           "= %d$. Swapping in the $y$-column determinant "
                           "returns $y = %d$ — the classic Cramer column "
                           "mix-up." % (e * d - b * f, det, x0, y0),
            "check": ["((%d)*(%d) - (%d)*(%d))/((%d)*(%d) - (%d)*(%d)) "
                      "== %d" % (e, d, b, f, a, d, b, c, x0),
                      "(%d)*(%d) + (%d)*(%d) == %d" % (a, x0, b, y0, e)],
        })
    return out


EQ_RE = re.compile(r"\$(-?\d*)x\s*([+-])\s*(\d*)y\s*=\s*(-?\d+)\$")


def _r_cramer(s):
    eqs = EQ_RE.findall(s)
    assert len(eqs) == 2, s
    (a_, s1, b_, e), (c_, s2, d_, f) = eqs
    a = int(a_ or "1")
    b = int(b_ or "1") * (1 if s1 == "+" else -1)
    c = int(c_ or "1")
    d = int(d_ or "1") * (1 if s2 == "+" else -1)
    e, f = int(e), int(f)
    return ("num", Rational(e * d - b * f, a * d - b * c))


# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------

NEW_FORMS_META = [
    ("vector-from-points", "Vector between two points", 1, "VM-from",
     "vectors-and-coordinates", gen_vector_from_points),
    ("vector-magnitude", "Magnitude of a vector", 2, "VM-mag",
     "vectors-and-coordinates", gen_vector_magnitude),
    ("vector-combine", "Linear combinations m·a + n·b", 1,
     "VM-comb", "vector-arithmetic", gen_vector_combine),
    ("tip-to-tail", "Tip-to-tail: magnitude of a sum", 2, "VM-tip",
     "vector-arithmetic", gen_tip_to_tail),
    ("parallel-scalar", "Parallel vectors: find k", 2, "VM-par",
     "vector-arithmetic", gen_parallel_scalar),
    ("dot-value", "Computing the dot product", 1, "VM-dot",
     "the-dot-product", gen_dot_value),
    ("perpendicular-k", "Perpendicular vectors: find k", 2, "VM-perp",
     "the-dot-product", gen_perpendicular_k),
    ("vector-angle-special", "Angle between vectors", 3, "VM-ang",
     "the-dot-product", gen_vector_angle),
    ("magnitude-3d", "Magnitude in 3D", 2, "VM-m3d", "vectors-in-space",
     gen_magnitude_3d),
    ("midpoint-3d", "Midpoint in 3D", 1, "VM-mid3", "vectors-in-space",
     gen_midpoint_3d),
    ("dot-3d", "Dot product in space", 3, "VM-dot3", "vectors-in-space",
     gen_dot_3d),
    ("matrix-entry", "Entry of A + mB", 1, "VM-ment",
     "matrices-and-operations", gen_matrix_entry),
    ("matrix-product-entry", "Entry of a matrix product", 2, "VM-mprod",
     "matrices-and-operations", gen_matrix_product_entry),
    ("det-2x2", "The 2×2 determinant", 1, "VM-det",
     "determinants-and-inverses", gen_det_2x2),
    ("cramer-2x2", "Cramer's rule for 2×2 systems", 3, "VM-cram",
     "determinants-and-inverses", gen_cramer),
]


# form id -> the one-line "what this drills" line. It is SHOWN TO STUDENTS,
# under the answer in the browser and under each form title in the runner's
# summary (components/bank/BankBrowser.tsx, BankRunner.tsx). Both assemblers
# below used to pass the variant-id PREFIX here, so every form in this subject
# shipped a debug code — "VM-from" — where a sentence belongs.
SKILLS = {
    "vector-from-points": "Tip minus tail gives the vector between two points.",
    "vector-relation": "Compare two vectors: equal, opposite, parallel or none of these.",
    "scaled-magnitude": "Scaling a vector multiplies its magnitude by |k|.",
    "unit-vector": "Divide a vector by its own magnitude to get length 1.",
    "vector-magnitude": "Pythagoras on the components.",
    "vector-combine": "Combine vectors componentwise with scalar weights.",
    "vector-subtract": "Subtract componentwise — order decides the direction.",
    "parallel-scalar": "Parallel vectors are multiples: match the ratios.",
    "tip-to-tail": "Add tip to tail, then take the magnitude of the sum.",
    "section-point": "The section formula splits a segment in a given ratio.",
    "dot-sign": "The sign of the dot product classifies the angle.",
    "dot-value": "Multiply matching components and add.",
    "perpendicular-k": "Perpendicular means the dot product is zero — solve for k.",
    "sum-square": "Expand |u + v|² with the dot product.",
    "vector-angle-special": "Find the angle from the dot product and the two magnitudes.",
    "midpoint-3d": "Average each of the three coordinates.",
    "vector-from-points-3d": "Tip minus tail, one coordinate at a time, in space.",
    "magnitude-3d": "Pythagoras with a third term.",
    "parallel-3d": "Parallel vectors in space share one scale factor across all three components.",
    "dot-3d": "Multiply matching components and add — now three of them.",
    "perpendicular-3d": "Set the 3D dot product to zero and solve.",
    "matrix-dimensions": "The product exists when the inner sizes match; the outer sizes survive.",
    "matrix-entry": "Add and scale matrices entry by entry.",
    "scalar-matrix": "Multiply every entry by the scalar.",
    "transpose": "Rows become columns.",
    "matrix-product-entry": "Row of the first times column of the second.",
    "matrix-square": "Multiply a matrix by itself and read one entry.",
    "det-2x2": "The determinant is ad − bc.",
    "inverse-2x2": "Swap the diagonal, negate the off-diagonal, divide by the determinant.",
    "singular-k": "A matrix is singular exactly when its determinant is zero.",
    "cramer-2x2": "Replace a column with the constants and divide by the determinant.",
    "unique-solution": "One solution exactly when the coefficient determinant is non-zero.",
}


def skill_of(fid):
    """The student-facing skill line, or a loud failure if one is missing."""
    line = SKILLS.get(fid)
    assert line, "%s: no student-facing skill line (see SKILLS)" % fid
    return line


def new_forms():
    """Unit-specific forms authored for this subject."""
    forms = []
    for fid, title, level, prefix, unit, gen in NEW_FORMS_META:
        raw = gen()
        assert len(raw) >= 10, "%s: only %d variants" % (fid, len(raw))
        variants = []
        for i, v in enumerate(raw):
            vd = {"id": "%s-v%02d" % (prefix, i + 1)}
            vd.update(v)
            variants.append(vd)
        forms.append({"id": fid, "title": title, "level": level,
                      "skill": skill_of(fid), "unit": unit,
                      "variants": variants})
    return forms


RESOLVERS.update({
    "vector-from-points": _r_vector_from_points,
    "vector-magnitude": _r_vector_magnitude,
    "vector-combine": _r_vector_combine,
    "tip-to-tail": _r_tip_to_tail,
    "parallel-scalar": _r_parallel_scalar,
    "dot-value": _r_dot_value,
    "perpendicular-k": _r_perpendicular_k,
    "vector-angle-special": _r_vector_angle,
    "magnitude-3d": _r_magnitude_3d,
    "midpoint-3d": _r_midpoint_3d,
    "dot-3d": _r_dot_3d,
    "matrix-entry": _r_matrix_entry,
    "matrix-product-entry": _r_matrix_product_entry,
    "det-2x2": _r_det_2x2,
    "cramer-2x2": _r_cramer,
})


# ===========================================================================
# Batch 2 — the forms that take every Vectors & Matrices unit to six.
#
# Matrices & Operations shipped with two collections and three other units
# with three. Each form below drills something its unit did not already ask.
# ===========================================================================

# --- vectors-and-coordinates ----------------------------------------------
UNITV_DATA = [(3, 4), (6, 8), (5, 12), (8, 15), (-3, 4), (7, 24),
              (9, 12), (-5, 12), (20, 21), (12, 16), (-8, 15), (10, 24)]


def gen_unit_vector():
    out = []
    for i, (x, y) in enumerate(UNITV_DATA):
        n2 = x * x + y * y
        n = int(sqrt(n2))
        assert n * n == n2, "unit vector: magnitude %d not exact" % n2
        pos = i % 4
        correct = pair(Rational(x, n), Rational(y, n))
        cands = [pair(Rational(y, n), Rational(x, n)),
                 pair(Rational(x, n2), Rational(y, n2)),
                 pair(Rational(n, x) if x else Rational(1),
                      Rational(n, y) if y else Rational(1)),
                 pair(Rational(-x, n), Rational(-y, n))]
        out.append({
            "statement": "Find the unit vector in the direction of $%s$."
                         % vec2("u", x, y),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Divide by the magnitude: $|\\vec{u}| = "
                           "\\sqrt{%d + %d} = %d$, so the unit vector is "
                           "$\\left(\\frac{%d}{%d}; \\frac{%d}{%d}\\right)$. "
                           "Dividing by $|\\vec{u}|^2 = %d$ instead shrinks "
                           "it too far — the result would not have length "
                           "$1$." % (x * x, y * y, n, x, n, y, n, n2),
            "check": ["sqrt((%d)**2 + (%d)**2) == %d" % (x, y, n),
                      "Rational(%d, %d)**2 + Rational(%d, %d)**2 == 1"
                      % (x, n, y, n)],
        })
    return out


def _r_unit_vector(s):
    x, y = _pair_after(s, r"\\vec\{u\}")
    n = int(sqrt(x * x + y * y))
    return ("opt", pair(Rational(x, n), Rational(y, n)))


RELATION_DATA = [
    ((2, 5), (2, 5), "equal"), ((3, -1), (-3, 1), "opposite"),
    ((1, 4), (3, 12), "parallel but not equal"),
    ((2, 3), (5, 1), "none of these"),
    ((-4, 6), (-4, 6), "equal"), ((7, 2), (-7, -2), "opposite"),
    ((2, -5), (6, -15), "parallel but not equal"),
    ((3, 4), (4, 3), "none of these"),
    ((-1, -8), (-1, -8), "equal"), ((5, -3), (-5, 3), "opposite"),
    ((4, 1), (12, 3), "parallel but not equal"),
    ((6, -2), (2, 6), "none of these"),
]


def gen_vector_relation():
    pool = ["equal", "opposite", "parallel but not equal", "none of these"]
    out = []
    for i, ((a, b), (c, d), kind) in enumerate(RELATION_DATA):
        pos = i % 4
        cands = [k for k in pool if k != kind]
        cross = a * d - b * c
        out.append({
            "statement": "How are $%s$ and $%s$ related?"
                         % (vec2("u", a, b), vec2("v", c, d)),
            "options": place(kind, cands, pos), "correctIndex": pos,
            "explanation": "Two vectors are parallel exactly when "
                           "$u_1 v_2 - u_2 v_1 = 0$; here that is "
                           "$(%d)(%d) - (%d)(%d) = %d. $ %s Equal means the "
                           "same multiplier $1$, opposite means $-1$, and "
                           "any other non-zero multiplier leaves them "
                           "parallel without being either."
                           % (a, d, b, c, cross,
                              "So they are parallel."
                              if cross == 0 else
                              "So they are not parallel at all."),
            "check": ["(%d)*(%d) - (%d)*(%d) %s 0"
                      % (a, d, b, c, "==" if cross == 0 else "!=")],
        })
    return out


def _r_vector_relation(s):
    a, b = _pair_after(s, r"\\vec\{u\}")
    c, d = _pair_after(s, r"\\vec\{v\}")
    if a * d - b * c != 0:
        return ("opt", "none of these")
    if (a, b) == (c, d):
        return ("opt", "equal")
    if (a, b) == (-c, -d):
        return ("opt", "opposite")
    return ("opt", "parallel but not equal")


SCALEMAG_DATA = [(3, 4, 2), (6, 8, 3), (5, 12, 2), (8, 15, 4), (3, 4, 5),
                 (7, 24, 2), (9, 12, 3), (5, 12, 6), (20, 21, 2),
                 (12, 16, 5), (8, 15, 3), (10, 24, 4)]


def gen_scaled_magnitude():
    out = []
    for i, (x, y, k) in enumerate(SCALEMAG_DATA):
        n = int(sqrt(x * x + y * y))
        assert n * n == x * x + y * y
        ans = k * n
        pos = i % 4
        correct = numO(ans)
        cands = [numO(n), numO(k * k * n), numO(n + k), numO(k * (x + y)),
                 numO(ans + 1), numO(ans - 1)]
        out.append({
            "statement": "For $%s$, find $|%d\\vec{u}|$." % (vec2("u", x, y),
                                                             k),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Scaling a vector by $%d$ scales its length by "
                           "$%d$ too: $|\\vec{u}| = %d$, so "
                           "$|%d\\vec{u}| = %d \\cdot %d = %d$. The squares "
                           "in the magnitude formula do NOT square the "
                           "scalar — it comes back out of the root."
                           % (k, k, n, k, k, n, ans),
            "check": ["sqrt((%d*%d)**2 + (%d*%d)**2) == %d"
                      % (k, x, k, y, ans)],
        })
    return out


def _r_scaled_magnitude(s):
    x, y = _pair_after(s, r"\\vec\{u\}")
    k = int(re.search(r"\|(\d+)\\vec\{u\}\|", s).group(1))
    return ("num", k * sqrt(x * x + y * y))


# --- vector-arithmetic ----------------------------------------------------
SUBTRACT_DATA = [((5, 2), (1, 7)), ((3, -4), (6, 2)), ((-2, 5), (4, 1)),
                 ((7, 3), (2, -6)), ((1, 8), (-5, 4)), ((6, -1), (3, 9)),
                 ((-3, 2), (5, -7)), ((4, 6), (9, 2)), ((8, -5), (1, 3)),
                 ((2, 9), (-4, 6)), ((-6, 1), (2, 8)), ((5, -3), (7, 4))]


def gen_vector_subtract():
    out = []
    for i, ((a, b), (c, d)) in enumerate(SUBTRACT_DATA):
        ax, ay = a - c, b - d
        pos = i % 4
        correct = pair(ax, ay)
        cands = [pair(c - a, d - b), pair(a + c, b + d),
                 pair(a - c, d - b), pair(c - a, b - d)]
        out.append({
            "statement": "Find $\\vec{u} - \\vec{v}$ for $%s$ and $%s$."
                         % (vec2("u", a, b), vec2("v", c, d)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Subtract componentwise, keeping the order: "
                           "$(%d - %d;\\ %d - %d) = (%d; %d)$. Reversing the "
                           "order gives $(%d; %d)$, which points the "
                           "opposite way — $\\vec{u} - \\vec{v}$ runs from "
                           "the tip of $\\vec{v}$ to the tip of $\\vec{u}$."
                           % (a, c, b, d, ax, ay, c - a, d - b),
            "check": ["(%d) - (%d) == %d" % (a, c, ax),
                      "(%d) - (%d) == %d" % (b, d, ay)],
        })
    return out


def _r_vector_subtract(s):
    a, b = _pair_after(s, r"\\vec\{u\}")
    c, d = _pair_after(s, r"\\vec\{v\}")
    return ("opt", pair(a - c, b - d))


# A 1 : 1 ratio is deliberately absent: at equal weights the section point
# IS the midpoint, and the two error models this form teaches — weighting
# each endpoint by its own part, and reaching for the midpoint — collapse
# onto the correct answer.
SECTION_DATA = [((0, 0), (6, 9), 1, 2), ((2, 1), (8, 7), 1, 2),
                ((-3, 2), (9, 10), 1, 3), ((4, -2), (10, 4), 2, 1),
                ((1, 5), (13, -7), 1, 2), ((-6, 0), (6, 12), 3, 1),
                ((5, 3), (5, 15), 1, 5), ((0, -4), (12, 8), 1, 2),
                ((7, 1), (-5, 13), 1, 3), ((2, 8), (14, -4), 1, 3),
                ((-1, -1), (11, 11), 1, 2), ((9, 6), (-3, 18), 2, 4)]


def gen_section_point():
    out = []
    for i, ((ax, ay), (bx, by), m, n) in enumerate(SECTION_DATA):
        px = Rational(n * ax + m * bx, m + n)
        py = Rational(n * ay + m * by, m + n)
        assert px.q == 1 and py.q == 1, "section: %r not a lattice point" % (
            (ax, ay, bx, by, m, n),)
        pos = i % 4
        correct = pair(px, py)
        cands = [pair(Rational(m * ax + n * bx, m + n),
                      Rational(m * ay + n * by, m + n)),
                 pair(Rational(ax + bx, 2), Rational(ay + by, 2)),
                 pair(bx - ax, by - ay), pair(ax + m, ay + n)]
        out.append({
            "statement": "$P$ divides $AB$ so that $AP : PB = %d : %d$, with "
                         "$A = (%d; %d)$ and $B = (%d; %d)$. Find $P$."
                         % (m, n, ax, ay, bx, by),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The section formula weights each endpoint by the "
                           "OPPOSITE part of the ratio: "
                           "$P = \\dfrac{%d \\cdot A + %d \\cdot B}{%d} = "
                           "(%s; %s)$. Weighting $A$ by its own part instead "
                           "pulls the point to the wrong side."
                           % (n, m, m + n, L(px), L(py)),
            "check": ["Rational(%d*(%d) + %d*(%d), %d) == %d"
                      % (n, ax, m, bx, m + n, px),
                      "Rational(%d*(%d) + %d*(%d), %d) == %d"
                      % (n, ay, m, by, m + n, py)],
        })
    return out


def _r_section_point(s):
    m, n = [int(x) for x in
            re.search(r"AP : PB = (\d+) : (\d+)", s).groups()]
    ax, ay = _pair_after(s, "A")
    bx, by = _pair_after(s, "B")
    return ("opt", pair(Rational(n * ax + m * bx, m + n),
                        Rational(n * ay + m * by, m + n)))


# --- the-dot-product ------------------------------------------------------
DOTSIGN_DATA = [((3, 1), (2, 4)), ((2, 3), (-3, 2)), ((-1, 5), (4, -2)),
                ((6, 2), (1, 3)), ((4, -1), (1, 4)), ((-2, -3), (5, 1)),
                ((7, 3), (2, 5)), ((1, 6), (6, -1)), ((-4, 2), (3, 1)),
                ((5, 5), (2, 1)), ((3, -2), (2, 3)), ((-3, 4), (2, -5))]


def gen_dot_sign():
    pool = ["acute", "right", "obtuse"]
    out = []
    for i, ((a, b), (c, d)) in enumerate(DOTSIGN_DATA):
        D = a * c + b * d
        kind = "acute" if D > 0 else ("right" if D == 0 else "obtuse")
        cands = [k for k in pool if k != kind] + ["straight"]
        pos = i % 4
        out.append({
            "statement": "Without computing the angle, decide whether the "
                         "angle between $%s$ and $%s$ is acute, right or "
                         "obtuse." % (vec2("u", a, b), vec2("v", c, d)),
            "options": place(kind, cands, pos), "correctIndex": pos,
            "explanation": "$\\vec{u} \\cdot \\vec{v} = |\\vec{u}||\\vec{v}|"
                           "\\cos\\theta$, and the two magnitudes are always "
                           "positive — so the SIGN of the dot product is the "
                           "sign of $\\cos\\theta$. Here "
                           "$(%d)(%d) + (%d)(%d) = %d$, which is %s, so the "
                           "angle is %s."
                           % (a, c, b, d, D,
                              "positive" if D > 0 else
                              ("zero" if D == 0 else "negative"), kind),
            "check": ["(%d)*(%d) + (%d)*(%d) %s 0"
                      % (a, c, b, d, ">" if D > 0 else
                         ("==" if D == 0 else "<"))],
        })
    return out


def _r_dot_sign(s):
    a, b = _pair_after(s, r"\\vec\{u\}")
    c, d = _pair_after(s, r"\\vec\{v\}")
    D = a * c + b * d
    return ("opt", "acute" if D > 0 else ("right" if D == 0 else "obtuse"))


SUMSQ_DATA = [(3, 4, 5), (5, 12, 20), (2, 6, 7), (8, 15, -30), (4, 3, 6),
              (7, 24, 40), (6, 8, -10), (9, 12, 15), (1, 5, 3),
              (10, 10, -25), (2, 9, 8), (11, 6, 12)]


def gen_sum_square():
    out = []
    for i, (mu, mv, dot) in enumerate(SUMSQ_DATA):
        ans = mu * mu + 2 * dot + mv * mv
        assert ans > 0, "sum-square: %r gives a negative square" % (
            (mu, mv, dot),)
        pos = i % 4
        correct = numO(ans)
        cands = [numO(mu * mu + mv * mv), numO((mu + mv) ** 2),
                 numO(mu * mu + dot + mv * mv),
                 numO(mu * mu - 2 * dot + mv * mv), numO(ans + 1),
                 numO(ans - 1)]
        out.append({
            "statement": "$|\\vec{u}| = %d$, $|\\vec{v}| = %d$ and "
                         "$\\vec{u} \\cdot \\vec{v} = %d$. Find "
                         "$|\\vec{u} + \\vec{v}|^2$." % (mu, mv, dot),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Expand the dot product with itself: "
                           "$|\\vec{u} + \\vec{v}|^2 = |\\vec{u}|^2 + "
                           "2\\vec{u}\\cdot\\vec{v} + |\\vec{v}|^2 = "
                           "%d + 2(%d) + %d = %d$. Dropping the middle term "
                           "assumes the vectors are perpendicular, which is "
                           "only true when the dot product is zero."
                           % (mu * mu, dot, mv * mv, ans),
            "check": ["%d**2 + 2*(%d) + %d**2 == %d" % (mu, dot, mv, ans)],
        })
    return out


def _r_sum_square(s):
    mu = int(re.search(r"\|\\vec\{u\}\| = (\d+)", s).group(1))
    mv = int(re.search(r"\|\\vec\{v\}\| = (\d+)", s).group(1))
    dot = int(re.search(r"\\cdot \\vec\{v\} = (-?\d+)", s).group(1))
    return ("num", mu * mu + 2 * dot + mv * mv)


# --- vectors-in-space -----------------------------------------------------
FROM3_DATA = [((1, 2, 3), (4, 6, 8)), ((0, -1, 5), (3, 2, 1)),
              ((2, 4, -2), (7, 1, 3)), ((-3, 0, 6), (2, 5, -1)),
              ((5, 3, 1), (0, 7, 4)), ((-1, -4, 2), (6, 2, 9)),
              ((8, 1, -3), (2, 6, 5)), ((3, 9, 0), (-4, 3, 7)),
              ((6, -2, 4), (1, 8, -6)), ((-5, 5, 2), (4, 0, 3)),
              ((7, 2, 8), (3, -3, 1)), ((0, 6, -4), (9, 1, 2))]


def gen_vector_from_points_3d():
    out = []
    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(FROM3_DATA):
        dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
        pos = i % 4
        correct = trip(dx, dy, dz)
        cands = [trip(-dx, -dy, -dz), trip(x1 + x2, y1 + y2, z1 + z2),
                 trip(dx, dy, -dz), trip(dy, dx, dz)]
        out.append({
            "statement": "Find $\\vec{AB}$ for $A = (%d; %d; %d)$ and "
                         "$B = (%d; %d; %d)$." % (x1, y1, z1, x2, y2, z2),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Head minus tail, one coordinate at a time: "
                           "$(%d - %d;\\ %d - %d;\\ %d - %d) = (%d; %d; %d)$. "
                           "Doing it the other way round gives $\\vec{BA}$, "
                           "which is the same arrow reversed."
                           % (x2, x1, y2, y1, z2, z1, dx, dy, dz),
            "check": ["(%d) - (%d) == %d" % (x2, x1, dx),
                      "(%d) - (%d) == %d" % (y2, y1, dy),
                      "(%d) - (%d) == %d" % (z2, z1, dz)],
        })
    return out


def _r_vector_from_points_3d(s):
    x1, y1, z1 = _trip_after(s, "A")
    x2, y2, z2 = _trip_after(s, "B")
    return ("opt", trip(x2 - x1, y2 - y1, z2 - z1))


PAR3_DATA = [((2, 3, 4), 3), ((1, -2, 5), 4), ((3, 1, -2), 2), ((4, 5, 1), 3),
             ((-1, 3, 2), 5), ((2, -4, 6), 2), ((5, 2, 3), 4), ((1, 6, -3), 3),
             ((-2, 1, 4), 6), ((3, -5, 2), 2), ((6, 1, 5), 3), ((2, 7, -1), 4)]


def gen_parallel_3d():
    out = []
    for i, ((a, b, c), k) in enumerate(PAR3_DATA):
        # v = k*u, and the missing third component is k*c
        ans = k * c
        pos = i % 4
        correct = numO(ans)
        cands = [numO(c + k), numO(c), numO(k), numO(c * c),
                 numO(ans - 1), numO(ans + 1), numO(2 * ans)]
        out.append({
            "statement": "$\\vec{u} = (%d; %d; %d)$ and "
                         "$\\vec{v} = (%d; %d; t)$ are parallel. Find $t$."
                         % (a, b, c, k * a, k * b),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Parallel means one vector is a single multiple "
                           "of the other. Comparing the first components, "
                           "$\\frac{%d}{%d} = %d$, and the second agrees, so "
                           "the SAME multiplier must apply to the third: "
                           "$t = %d \\cdot %d = %d$. A multiplier that works "
                           "for only one coordinate is not parallelism."
                           % (k * a, a, k, k, c, ans),
            "check": ["Rational(%d, %d) == %d" % (k * a, a, k),
                      "Rational(%d, %d) == %d" % (k * b, b, k),
                      "%d * (%d) == %d" % (k, c, ans)],
        })
    return out


def _r_parallel_3d(s):
    a, b, c = _trip_after(s, r"\\vec\{u\}")
    m = re.search(r"\\vec\{v\} = \((-?\d+); (-?\d+); t\)", s)
    return ("num", Rational(int(m.group(1)), a) * c)


PERP3_DATA = [((2, 3, 1), (4, -1, 5)), ((1, 2, 4), (3, 5, -2)),
              ((5, -2, 3), (1, 4, 2)), ((2, 6, -1), (3, 1, 7)),
              ((4, 1, 2), (2, -3, 5)), ((-1, 3, 6), (4, 2, 1)),
              ((3, 5, 2), (1, -2, 4)), ((6, -1, 1), (2, 3, 5)),
              ((1, 4, 7), (5, 2, -3)), ((2, -5, 4), (6, 1, 3)),
              ((7, 2, -2), (1, 5, 4)), ((3, 3, 5), (4, -6, 2))]


def gen_perpendicular_3d():
    out = []
    for i, ((a, b, c), (d, e, f)) in enumerate(PERP3_DATA):
        assert f != 0
        # a*d + b*e + c*(f + t) = 0  ->  we instead solve for the third
        # component of v: find t with a*d + b*e + c*t = 0
        num = -(a * d + b * e)
        ans = Rational(num, c)
        pos = i % 4
        correct = numO(ans)
        cands = [numO(-ans), numO(Rational(num, a) if a else ans + 3),
                 numO(ans + 1), numO(ans - 1), numO(2 * ans)]
        out.append({
            "statement": "$\\vec{u} = (%d; %d; %d)$ and "
                         "$\\vec{v} = (%d; %d; t)$ are perpendicular. Find "
                         "$t$." % (a, b, c, d, e),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Perpendicular means the dot product vanishes: "
                           "$(%d)(%d) + (%d)(%d) + (%d)t = 0$, so "
                           "$%dt = %d$ and $t = %s$. Note it is the "
                           "component of $\\vec{u}$ that multiplies $t$ — "
                           "matching the wrong pair is the usual slip."
                           % (a, d, b, e, c, c, num, L(ans)),
            "check": ["(%d)*(%d) + (%d)*(%d) + (%d)*Rational(%d, %d) == 0"
                      % (a, d, b, e, c, ans.p, ans.q)],
        })
    return out


def _r_perpendicular_3d(s):
    a, b, c = _trip_after(s, r"\\vec\{u\}")
    m = re.search(r"\\vec\{v\} = \((-?\d+); (-?\d+); t\)", s)
    d, e = int(m.group(1)), int(m.group(2))
    return ("num", Rational(-(a * d + b * e), c))

# --- matrices-and-operations ----------------------------------------------
SCALARM_DATA = [((2, 3, 1, 4), 3), ((5, -1, 2, 6), 2), ((1, 4, -3, 2), 5),
                ((6, 2, 4, -5), 3), ((-2, 7, 1, 3), 4), ((3, 1, 5, 2), 6),
                ((4, -6, 2, 1), 2), ((1, 5, 3, -4), 7), ((7, 2, -1, 6), 3),
                ((2, 8, 4, 3), 5), ((-5, 1, 6, 2), 2), ((3, 4, 1, 9), 4)]


def gen_scalar_matrix():
    out = []
    for i, ((a, b, c, d), k) in enumerate(SCALARM_DATA):
        ans = k * c
        pos = i % 4
        correct = numO(ans)
        cands = [numO(k * b), numO(c + k), numO(k * a), numO(k * d),
                 numO(ans + 1), numO(ans - 1)]
        out.append({
            "statement": "Let $M = %dA$ for $A = %s$. Find the entry "
                         "$m_{21}$ (row 2, column 1)."
                         % (k, pm(a, b, c, d)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "A scalar multiplies EVERY entry, so the entry at "
                           "address $(2, 1)$ is $%d \\cdot %d = %d$. Reading "
                           "$m_{12}$ instead — row 1, column 2 — gives $%d$; "
                           "the row index always comes first."
                           % (k, c, ans, k * b),
            "check": ["(%d)*(%d) == %d" % (k, c, ans)],
        })
    return out


def _r_scalar_matrix(s):
    k = int(re.search(r"M = (\d+)A", s).group(1))
    a, b, c, d = [int(x) for x in PM_RE.search(s).groups()]
    return ("num", k * c)


TRANSPOSE_DATA = [(2, 3, 1, 4), (5, -1, 2, 6), (1, 4, -3, 2), (6, 2, 4, -5),
                  (-2, 7, 1, 3), (3, 1, 5, 2), (4, -6, 2, 1), (1, 5, 3, -4),
                  (7, 2, -1, 6), (2, 8, 4, 3), (-5, 1, 6, 2), (3, 4, 1, 9)]


def gen_transpose():
    out = []
    for i, (a, b, c, d) in enumerate(TRANSPOSE_DATA):
        assert b != c, "transpose: symmetric matrix hides the swap"
        pos = i % 4
        correct = "$" + pm(a, c, b, d) + "$"
        cands = ["$" + pm(a, b, c, d) + "$", "$" + pm(d, b, c, a) + "$",
                 "$" + pm(d, c, b, a) + "$", "$" + pm(c, a, d, b) + "$"]
        out.append({
            "statement": "Find $A^{T}$ for $A = %s$." % pm(a, b, c, d),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Transposing reflects the matrix across its main "
                           "diagonal, so the two off-diagonal entries trade "
                           "places while $%d$ and $%d$ stay put: the result "
                           "is $%s$. Swapping the DIAGONAL entries instead "
                           "is what the adjugate does, not the transpose."
                           % (a, d, pm(a, c, b, d)),
            "check": ["(%d) == (%d)" % (b, b), "(%d) == (%d)" % (c, c)],
        })
    return out


def _r_transpose(s):
    a, b, c, d = [int(x) for x in PM_RE.search(s).groups()]
    return ("opt", "$" + pm(a, c, b, d) + "$")


SQUARE_DATA = [(2, 1, 3, 4), (1, 2, 0, 3), (3, -1, 2, 1), (4, 2, 1, 5),
               (2, 3, -1, 2), (5, 1, 2, 3), (1, 4, 2, -2), (3, 2, 4, 1),
               (-1, 3, 5, 2), (2, 5, 1, 4), (6, 1, -2, 3), (1, 1, 4, 2)]


def gen_matrix_square():
    out = []
    for i, (a, b, c, d) in enumerate(SQUARE_DATA):
        ans = a * a + b * c        # entry (1, 1) of A squared
        pos = i % 4
        correct = numO(ans)
        cands = [numO(a * a), numO(a * a + b * b), numO((a + b) * (a + c)),
                 numO(a * a + c * c), numO(ans + 1), numO(ans - 1),
                 numO(2 * ans)]
        out.append({
            "statement": "For $A = %s$, find the entry in row 1, column 1 of "
                         "$A^{2}$." % pm(a, b, c, d),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "$A^2$ means $A$ times $A$, so the $(1,1)$ entry "
                           "is row 1 of $A$ dotted with column 1 of $A$: "
                           "$(%d)(%d) + (%d)(%d) = %d$. Squaring each entry "
                           "separately would give $%d$ — matrix "
                           "multiplication is not entrywise."
                           % (a, a, b, c, ans, a * a),
            "check": ["(%d)*(%d) + (%d)*(%d) == %d" % (a, a, b, c, ans)],
        })
    return out


def _r_matrix_square(s):
    a, b, c, d = [int(x) for x in PM_RE.search(s).groups()]
    return ("num", a * a + b * c)


DIM_DATA = [(2, 3, 3, 4), (3, 2, 2, 5), (4, 1, 1, 3), (2, 3, 3, 6),
            (5, 3, 3, 2), (1, 4, 4, 4), (3, 5, 5, 1), (6, 2, 2, 3),
            (2, 4, 4, 7), (4, 3, 3, 3), (5, 1, 1, 6), (3, 6, 6, 2)]


def gen_matrix_dimensions():
    out = []
    for i, (m, n, p, q) in enumerate(DIM_DATA):
        assert n == p, "dimensions: inner sizes must agree"
        pos = i % 4
        correct = "$%d \\times %d$" % (m, q)
        cands = ["$%d \\times %d$" % (q, m), "$%d \\times %d$" % (m, n),
                 "$%d \\times %d$" % (n, q), "$%d \\times %d$" % (m, m),
                 "$%d \\times %d$" % (q, q), "$%d \\times %d$" % (n, n)]
        out.append({
            "statement": "$A$ is $%d \\times %d$ and $B$ is $%d \\times %d$. "
                         "What size is $AB$?" % (m, n, p, q),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The inner sizes must match — here both are $%d$, "
                           "so the product exists — and the OUTER sizes "
                           "survive: $AB$ is $%d \\times %d$. Rows come from "
                           "the left factor and columns from the right, "
                           "which is why $AB$ and $BA$ usually differ in "
                           "shape as well as value." % (n, m, q),
            "check": ["%d == %d" % (n, p)],
        })
    return out


def _r_matrix_dimensions(s):
    m, n, p, q = [int(x) for x in
                  re.search(r"\$(\d+) \\times (\d+)\$ and \$B\$ is "
                            r"\$(\d+) \\times (\d+)\$", s).groups()]
    return ("opt", "$%d \\times %d$" % (m, q))


# --- determinants-and-inverses --------------------------------------------
INV_DATA = [(2, 1, 3, 2), (3, 1, 5, 2), (1, 2, 1, 3), (4, 3, 5, 4),
            (2, 3, 1, 2), (5, 2, 7, 3), (3, 2, 4, 3), (1, 1, 2, 3),
            (6, 5, 5, 4), (2, 5, 1, 3), (4, 1, 7, 2), (3, 4, 2, 3)]


def gen_inverse_2x2():
    out = []
    for i, (a, b, c, d) in enumerate(INV_DATA):
        det = a * d - b * c
        assert det in (1, -1), "inverse: det %d is not a unit" % det
        ia, ib, ic, id_ = d // det, -b // det, -c // det, a // det
        pos = i % 4
        correct = "$" + pm(ia, ib, ic, id_) + "$"
        cands = ["$" + pm(d, b, c, a) + "$",       # swapped, forgot to negate
                 "$" + pm(a, -b, -c, d) + "$",     # negated, forgot to swap
                 "$" + pm(d, -b, -c, a) + "$",     # right shape, no division
                 "$" + pm(-ia, -ib, -ic, -id_) + "$",
                 "$" + pm(a, b, c, d) + "$",
                 "$" + pm(ia, ic, ib, id_) + "$"]
        out.append({
            "statement": "Find $A^{-1}$ for $A = %s$." % pm(a, b, c, d),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The determinant is $(%d)(%d) - (%d)(%d) = %d$. "
                           "The inverse swaps the main diagonal, negates the "
                           "other two entries, and divides by the "
                           "determinant: $%s$. Forgetting to negate the "
                           "off-diagonal pair is the usual slip — the result "
                           "will not multiply back to the identity."
                           % (a, d, b, c, det, pm(ia, ib, ic, id_)),
            "check": ["(%d)*(%d) + (%d)*(%d) == 1" % (a, ia, b, ic),
                      "(%d)*(%d) + (%d)*(%d) == 0" % (a, ib, b, id_),
                      "(%d)*(%d) - (%d)*(%d) == %d" % (a, d, b, c, det)],
        })
    return out


def _r_inverse_2x2(s):
    a, b, c, d = [int(x) for x in PM_RE.search(s).groups()]
    det = a * d - b * c
    return ("opt", "$" + pm(d // det, -b // det, -c // det, a // det) + "$")


SING_DATA = [(2, 3, 4), (5, 2, 10), (3, 4, 6), (7, 1, 14), (2, 5, 8),
             (4, 3, 12), (6, 2, 9), (5, 4, 15), (3, 7, 6), (8, 1, 16),
             (2, 9, 10), (9, 2, 18)]


def gen_singular_k():
    out = []
    for i, (a, b, c) in enumerate(SING_DATA):
        # A = [[a, b], [c, k]] is singular when a*k - b*c = 0
        ans = Rational(b * c, a)
        pos = i % 4
        correct = numO(ans)
        cands = [numO(-ans), numO(Rational(a * c, b)), numO(Rational(a, b * c)
                                                            if b * c else
                                                            ans + 2),
                 numO(ans + 1), numO(b + c - a)]
        out.append({
            "statement": "For which value of $k$ does "
                         "$\\begin{pmatrix} %d & %d \\\\ %d & k "
                         "\\end{pmatrix}$ have no inverse?" % (a, b, c),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "A matrix has no inverse exactly when its "
                           "determinant is zero: $%dk - (%d)(%d) = 0$, so "
                           "$k = \\frac{%d}{%d} = %s$. At that value the two "
                           "rows are multiples of each other, which is the "
                           "same fact wearing different clothes."
                           % (a, b, c, b * c, a, L(ans)),
            "check": ["(%d)*Rational(%d, %d) - (%d)*(%d) == 0"
                      % (a, ans.p, ans.q, b, c)],
        })
    return out


def _r_singular_k(s):
    m = re.search(r"\\begin\{pmatrix\} (-?\d+) & (-?\d+) \\\\ (-?\d+) & k",
                  s)
    a, b, c = [int(x) for x in m.groups()]
    return ("num", Rational(b * c, a))


UNIQUE_DATA = [(2, 3, 4, 6, False), (1, 2, 3, 4, True), (5, 1, 10, 2, False),
               (3, 2, 1, 4, True), (4, 6, 2, 3, False), (2, 5, 3, 1, True),
               (6, 4, 3, 2, False), (1, 3, 2, 5, True), (7, 2, 14, 4, False),
               (4, 1, 3, 2, True), (2, 8, 1, 4, False), (5, 3, 2, 4, True)]


def gen_unique_solution():
    out = []
    for i, (a, b, c, d, unique) in enumerate(UNIQUE_DATA):
        det = a * d - b * c
        assert (det != 0) == unique, (a, b, c, d)
        correct = ("exactly one solution" if unique
                   else "no unique solution — the determinant is zero")
        cands = [("no unique solution — the determinant is zero" if unique
                  else "exactly one solution"),
                 "exactly two solutions",
                 "a unique solution only when the right-hand sides are zero"]
        pos = i % 4
        out.append({
            "statement": "How many solutions does the system "
                         "$%dx + %dy = 7$, $%dx + %dy = 11$ have?"
                         % (a, b, c, d),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The coefficient determinant is "
                           "$(%d)(%d) - (%d)(%d) = %d$. A non-zero "
                           "determinant means the two lines have different "
                           "slopes and cross exactly once; a zero "
                           "determinant means they are parallel, so there is "
                           "either no solution or a whole line of them — "
                           "never exactly two."
                           % (a, d, b, c, det),
            "check": ["(%d)*(%d) - (%d)*(%d) %s 0"
                      % (a, d, b, c, "!=" if unique else "==")],
        })
    return out


def _r_unique_solution(s):
    a, b, c, d = [int(x) for x in
                  re.search(r"\$(-?\d+)x \+ (-?\d+)y = 7\$, "
                            r"\$(-?\d+)x \+ (-?\d+)y = 11\$", s).groups()]
    return ("opt", "exactly one solution" if a * d - b * c != 0
            else "no unique solution — the determinant is zero")


NEW_FORMS_META_2 = [
    ("unit-vector", "The unit vector in a direction", 2, "VM-unit",
     "vectors-and-coordinates", gen_unit_vector, _r_unit_vector),
    ("vector-relation", "Equal, opposite, parallel or neither", 1, "VM-rel",
     "vectors-and-coordinates", gen_vector_relation, _r_vector_relation),
    ("scaled-magnitude", "Magnitude after scaling", 2, "VM-smag",
     "vectors-and-coordinates", gen_scaled_magnitude, _r_scaled_magnitude),
    ("vector-subtract", "Subtracting vectors", 1, "VM-sub",
     "vector-arithmetic", gen_vector_subtract, _r_vector_subtract),
    ("section-point", "The section formula", 3, "VM-sect",
     "vector-arithmetic", gen_section_point, _r_section_point),
    ("dot-sign", "The angle from the sign of the dot product", 1, "VM-dsign",
     "the-dot-product", gen_dot_sign, _r_dot_sign),
    ("sum-square", "Expanding the square of a sum", 3, "VM-ssq",
     "the-dot-product", gen_sum_square, _r_sum_square),
    ("vector-from-points-3d", "A vector between two points in space", 1,
     "VM-f3d", "vectors-in-space", gen_vector_from_points_3d,
     _r_vector_from_points_3d),
    ("parallel-3d", "Parallel vectors in space", 2, "VM-p3d",
     "vectors-in-space", gen_parallel_3d, _r_parallel_3d),
    ("perpendicular-3d", "Perpendicular vectors in space", 3, "VM-x3d",
     "vectors-in-space", gen_perpendicular_3d, _r_perpendicular_3d),
    ("scalar-matrix", "Scaling a matrix", 1, "VM-scal",
     "matrices-and-operations", gen_scalar_matrix, _r_scalar_matrix),
    ("transpose", "The transpose", 1, "VM-trn", "matrices-and-operations",
     gen_transpose, _r_transpose),
    ("matrix-square", "An entry of A squared", 2, "VM-sqr",
     "matrices-and-operations", gen_matrix_square, _r_matrix_square),
    ("matrix-dimensions", "The size of a product", 1, "VM-dim",
     "matrices-and-operations", gen_matrix_dimensions, _r_matrix_dimensions),
    ("inverse-2x2", "The inverse of a 2×2 matrix", 2, "VM-inv",
     "determinants-and-inverses", gen_inverse_2x2, _r_inverse_2x2),
    ("singular-k", "Making a matrix singular", 2, "VM-sing",
     "determinants-and-inverses", gen_singular_k, _r_singular_k),
    ("unique-solution", "When a 2×2 system has one solution", 3, "VM-uniq",
     "determinants-and-inverses", gen_unique_solution, _r_unique_solution),
]


def _batch2_forms():
    forms = []
    for fid, title, level, prefix, unit, gen, _rz in NEW_FORMS_META_2:
        raw = gen()
        assert len(raw) >= 12, "%s: only %d variants" % (fid, len(raw))
        variants = []
        for i, v in enumerate(raw):
            vd = {"id": "%s-v%02d" % (prefix, i + 1)}
            vd.update(v)
            variants.append(vd)
        forms.append({"id": fid, "title": title, "level": level,
                      "skill": skill_of(fid), "unit": unit,
                      "variants": variants})
    return forms


_BATCH1_FORMS = new_forms


def new_forms():  # noqa: F811 — appends batch 2 to the original set
    """All unit-specific forms: the original set, batch 2, and units 7-8."""
    return _BATCH1_FORMS() + _batch2_forms() + vecmat_more.forms()


RESOLVERS.update({fid: rz for fid, _t, _l, _p, _u, _g, rz
                  in NEW_FORMS_META_2})


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = new_forms()
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
