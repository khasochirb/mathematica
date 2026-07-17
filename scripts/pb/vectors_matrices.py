# -*- coding: utf-8 -*-
"""Problem-bank subject: Vectors & Matrices — mirrors the /math/vectors-matrices course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/vectors_matrices.py` to
self-check.
"""
import re

from sympy import Rational, simplify, sqrt, sympify

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
                      "skill": prefix, "unit": unit, "variants": variants})
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
