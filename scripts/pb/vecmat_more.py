# -*- coding: utf-8 -*-
"""Bank forms for Vectors & Matrices units 7 and 8.

Unit 7 (Transformation Matrices) and unit 8 (Systems in Three Unknowns) were
added on 2026-08-12 to close the last core gaps against the ministry standard
А/492 — section 10.11 and objective 11.2г. A course unit with no bank unit is
half a unit: the lesson page offers practice, but the unit's bank page would
be empty and scripts/verify-problembank.py refuses a unit with fewer than 24
problems. These are the twelve forms that fill it.

The house style of scripts/pb/vectors_matrices.py is followed exactly (raw
dicts with `place`-rotated options and a sympy `check` list per variant), with
the handful of small renderers duplicated here rather than imported, because
vectors_matrices.py imports THIS module and a cycle would break the build.

Run `python3 scripts/pb/vecmat_more.py` to self-check.
"""
from sympy import Matrix, Rational, sympify

# ---------------------------------------------------------------------------
# renderers (mirrors of the ones in vectors_matrices.py)
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
    return "$" + L(v) + "$"


def pair(x, y):
    return "$(%s; %s)$" % (L(x), L(y))


def pm(a, b, c, d):
    """Inline latex for a 2x2 pmatrix (no surrounding $)."""
    return ("\\begin{pmatrix} %s & %s \\\\ %s & %s \\end{pmatrix}"
            % (L(a), L(b), L(c), L(d)))


def pmO(a, b, c, d):
    return "$" + pm(a, b, c, d) + "$"


def m3(rows):
    body = " \\\\ ".join(" & ".join(L(x) for x in r) for r in rows)
    return "\\begin{pmatrix} %s \\end{pmatrix}" % body


def row(a, b, c, d):
    """An augmented-matrix row as a rendered option."""
    return "$%s \\;\\; %s \\;\\; %s \\mid %s$" % (L(a), L(b), L(c), L(d))


def sys3(rows):
    return "\\begin{cases} %s \\end{cases}" % (" \\\\ ".join(rows))


def eqn(a, b, c, d):
    """`ax + by + cz = d` with zero terms dropped and signs folded."""
    parts = []
    for coef, var in ((a, "x"), (b, "y"), (c, "z")):
        if coef == 0:
            continue
        if not parts:
            head = var if coef == 1 else ("-" + var if coef == -1 else "%d%s" % (coef, var))
            parts.append(head)
        else:
            mag = var if abs(coef) == 1 else "%d%s" % (abs(coef), var)
            parts.append("%s %s" % ("+" if coef > 0 else "-", mag))
    return "%s = %d" % (" ".join(parts), d)


def place(correct, cands, pos):
    """Insert `correct` at index pos among the first 3 distinct candidates."""
    picked = []
    for c in cands:
        if c == correct or c in picked:
            continue
        picked.append(c)
        if len(picked) == 3:
            break
    assert len(picked) == 3, "distractor shortage for %s from %r" % (correct, cands)
    opts = list(picked)
    opts.insert(pos, correct)
    assert len(set(opts)) == 4
    return opts


def n(v):
    """A signed factor for prose: -3 renders as (-3), so a product never
    reads `4 \\cdot -2` or, worse, `- -1(`."""
    return str(int(v)) if v >= 0 else "(%d)" % int(v)


def sy(v):
    """A sympy-syntax literal. L() renders LaTeX, which does NOT sympify —
    `\\frac{1}{2}` reaches parse_expr as a line-continuation and blows up."""
    v = sympify(v)
    if getattr(v, "q", 1) == 1:
        return "(%d)" % int(v)
    return "Rational(%d, %d)" % (v.p, v.q)


def det3_check(rows, value):
    """A cofactor-expansion check string for a 3x3 determinant."""
    (a, b, c), (d, e, f), (g, h, i) = rows
    return ("(%d)*((%d)*(%d) - (%d)*(%d)) - (%d)*((%d)*(%d) - (%d)*(%d)) "
            "+ (%d)*((%d)*(%d) - (%d)*(%d)) == %d"
            % (a, e, i, f, h, b, d, i, f, g, c, d, h, e, g, value))


# ===========================================================================
# unit: transformation-matrices
# ===========================================================================

RULE_MATRICES = [
    (3, -1, 2, 4), (5, 2, -1, 3), (1, 4, 2, -3), (-2, 5, 3, 1), (4, 0, -1, 2),
    (2, 7, 0, 5), (6, -3, 1, 2), (-1, 2, 4, 5), (3, 5, -2, 1), (7, 1, 3, -4),
    (2, -5, 6, 3), (1, 3, -4, 2), (5, -2, 3, 6), (-3, 1, 2, 7),
]


def gen_matrix_from_rules():
    out = []
    for i, (a, b, c, d) in enumerate(RULE_MATRICES):
        assert b != c and (a, b) != (c, d)
        pos = i % 4
        correct = pmO(a, b, c, d)
        cands = [pmO(a, c, b, d), pmO(c, d, a, b), pmO(a, -b, c, -d), pmO(b, a, d, c)]
        out.append({
            "statement": "A transformation of the plane is given by $x' = %s$ and "
                         "$y' = %s$. Which matrix carries this transformation?"
                         % (eqn2(a, b), eqn2(c, d)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Row one holds the coefficients of the $x'$ rule and row two "
                           "those of the $y'$ rule, so the matrix is $%s$. Reading the "
                           "coefficients DOWN the columns instead gives the transpose "
                           "$%s$ — the most common slip in this topic."
                           % (pm(a, b, c, d), pm(a, c, b, d)),
            "check": ["(%d)*1 + (%d)*0 == %d" % (a, b, a),
                      "(%d)*0 + (%d)*1 == %d" % (c, d, d)],
        })
    return out


def eqn2(a, b):
    """`ax + by` with zero terms dropped, for a transformation rule."""
    parts = []
    for coef, var in ((a, "x"), (b, "y")):
        if coef == 0:
            continue
        if not parts:
            parts.append(var if coef == 1 else
                         ("-" + var if coef == -1 else "%d%s" % (coef, var)))
        else:
            mag = var if abs(coef) == 1 else "%d%s" % (abs(coef), var)
            parts.append("%s %s" % ("+" if coef > 0 else "-", mag))
    return " ".join(parts) if parts else "0"


IMAGE_CASES = [
    (3, -1, 2, 4, 2, -1), (1, 2, 0, 1, 3, 2), (0, -1, 1, 0, 5, 2),
    (2, 0, 0, 3, -4, 1), (1, 3, -2, 1, 2, 4), (4, 1, 2, -3, 1, 5),
    (-1, 2, 3, 1, 4, -2), (5, -2, 1, 3, 2, 3), (2, 4, -1, 0, 3, 1),
    (0, 2, -3, 1, 1, 4), (3, 1, 1, 2, -2, 5), (1, -4, 2, 3, 6, 1),
    (6, 2, -1, 4, 1, 2), (2, -3, 5, 1, 3, -1),
]


def gen_image_of_point():
    out = []
    for i, (a, b, c, d, x, y) in enumerate(IMAGE_CASES):
        u, v = a * x + b * y, c * x + d * y
        pos = i % 4
        correct = pair(u, v)
        cands = [pair(a * x + c * y, b * x + d * y), pair(v, u),
                 pair(a * y + b * x, c * y + d * x), pair(a * x, d * y),
                 pair(a * x - b * y, c * x - d * y), pair(u + 1, v),
                 pair(u, v - 1)]
        out.append({
            "statement": "Find the image of the point $(%d; %d)$ under the transformation "
                         "with matrix $%s$." % (x, y, pm(a, b, c, d)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Row times column: $x' = %s \\cdot %s + %s \\cdot %s = %d$ and "
                           "$y' = %s \\cdot %s + %s \\cdot %s = %d$, so the image is "
                           "$(%d; %d)$." % (n(a), n(x), n(b), n(y), u,
                                            n(c), n(x), n(d), n(y), v, u, v),
            "check": ["(%d)*(%d) + (%d)*(%d) == %d" % (a, x, b, y, u),
                      "(%d)*(%d) + (%d)*(%d) == %d" % (c, x, d, y, v)],
        })
    return out


# name -> (matrix, a one-line justification)
STANDARD = [
    ("a reflection in the $x$-axis", (1, 0, 0, -1),
     "$(1; 0)$ stays put and $(0; 1) \\to (0; -1)$"),
    ("a reflection in the $y$-axis", (-1, 0, 0, 1),
     "$(1; 0) \\to (-1; 0)$ and $(0; 1)$ stays put"),
    ("a reflection in the line $y = x$", (0, 1, 1, 0),
     "the reflection swaps the two coordinates"),
    ("a reflection in the line $y = -x$", (0, -1, -1, 0),
     "the coordinates swap and both change sign"),
    ("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0),
     "$(1; 0) \\to (0; 1)$ and $(0; 1) \\to (-1; 0)$"),
    ("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0),
     "$(1; 0) \\to (0; -1)$ — a quarter turn clockwise"),
    ("a rotation of $180°$ about the origin", (-1, 0, 0, -1),
     "both coordinates change sign"),
    ("a reflection in the origin", (-1, 0, 0, -1),
     "point symmetry sends $(x; y)$ to $(-x; -y)$"),
    ("an enlargement with centre the origin and ratio $2$", (2, 0, 0, 2),
     "both coordinates are multiplied by $2$"),
    ("an enlargement with centre the origin and ratio $3$", (3, 0, 0, 3),
     "both coordinates are multiplied by $3$"),
    ("an enlargement with centre the origin and ratio $5$", (5, 0, 0, 5),
     "both coordinates are multiplied by $5$"),
    ("an enlargement with centre the origin and ratio $-2$", (-2, 0, 0, -2),
     "the ratio is negative, so the figure also turns through $180°$"),
    ("an enlargement with centre the origin and ratio $-4$", (-4, 0, 0, -4),
     "the ratio is negative, so the figure also turns through $180°$"),
    ("an enlargement with centre the origin and ratio $\\tfrac{1}{2}$",
     (Rational(1, 2), 0, 0, Rational(1, 2)),
     "both coordinates are halved"),
]

POOL = [(1, 0, 0, -1), (-1, 0, 0, 1), (0, 1, 1, 0), (0, -1, -1, 0),
        (0, -1, 1, 0), (0, 1, -1, 0), (-1, 0, 0, -1), (2, 0, 0, 2),
        (3, 0, 0, 3), (1, 0, 0, 1)]


def gen_standard_matrix():
    out = []
    for i, (name, mat, why) in enumerate(STANDARD):
        a, b, c, d = mat
        pos = i % 4
        correct = pmO(a, b, c, d)
        cands = [pmO(*p) for p in POOL] + [pmO(b, a, d, c), pmO(-a, b, c, -d)]
        out.append({
            "statement": "Which matrix performs %s?" % name,
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Build it from the two unit points: %s, and those two "
                           "destinations stand up as the columns of $%s$."
                           % (why, pm(a, b, c, d)),
            "check": ["Eq(%s*1 + %s*0, %s)" % (sy(a), sy(b), sy(a)),
                      "Eq(%s*0 + %s*1, %s)" % (sy(c), sy(d), sy(d))],
        })
    return out


IDENTIFY = [
    ((1, 0, 0, -1), "a reflection in the $x$-axis"),
    ((-1, 0, 0, 1), "a reflection in the $y$-axis"),
    ((0, 1, 1, 0), "a reflection in the line $y = x$"),
    ((0, -1, -1, 0), "a reflection in the line $y = -x$"),
    ((0, -1, 1, 0), "a rotation of $90°$ counter-clockwise about the origin"),
    ((0, 1, -1, 0), "a rotation of $270°$ counter-clockwise about the origin"),
    ((2, 0, 0, 2), "an enlargement with centre the origin and ratio $2$"),
    ((3, 0, 0, 3), "an enlargement with centre the origin and ratio $3$"),
    ((4, 0, 0, 4), "an enlargement with centre the origin and ratio $4$"),
    ((6, 0, 0, 6), "an enlargement with centre the origin and ratio $6$"),
    ((-3, 0, 0, -3), "an enlargement with centre the origin and ratio $-3$"),
    ((-5, 0, 0, -5), "an enlargement with centre the origin and ratio $-5$"),
    ((Rational(1, 3), 0, 0, Rational(1, 3)),
     "an enlargement with centre the origin and ratio $\\tfrac{1}{3}$"),
    ((Rational(1, 4), 0, 0, Rational(1, 4)),
     "an enlargement with centre the origin and ratio $\\tfrac{1}{4}$"),
]

NAMES = [n for _m, n in IDENTIFY] + [
    "a translation by $(1; 1)$",
    "a rotation of $45°$ counter-clockwise about the origin",
]


def gen_identify_transformation():
    out = []
    for i, (mat, name) in enumerate(IDENTIFY):
        a, b, c, d = mat
        det = a * d - b * c
        pos = i % 4
        cands = [n for n in NAMES if n != name]
        out.append({
            "statement": "Which transformation does the matrix $%s$ perform?" % pm(a, b, c, d),
            "options": place(name, cands, pos), "correctIndex": pos,
            "explanation": "Its determinant is $%s$, and multiplying by $(1; 0)$ gives "
                           "$(%s; %s)$ — that pins the transformation down as %s."
                           % (L(det), L(a), L(c), name),
            "check": ["Eq(%s*%s - %s*%s, %s)" % (sy(a), sy(d), sy(b), sy(c), sy(det)),
                      "Eq(%s*1 + %s*0, %s)" % (sy(a), sy(b), sy(a))],
        })
    return out


AREA_CASES = [
    ((3, 1, 2, 4), 2), ((1, 2, 0, 1), 5), ((2, 0, 0, 3), 4), ((5, 2, 1, 3), 3),
    ((4, 1, 1, 2), 6), ((0, -2, 3, 0), 2), ((1, 4, 2, 3), 10), ((6, 1, 2, 2), 3),
    ((2, 5, 1, 4), 7), ((3, 0, 4, 2), 5), ((1, -3, 2, 1), 4), ((5, 1, 3, 2), 8),
    ((2, 3, 4, 1), 6), ((7, 2, 3, 1), 2),
]


def gen_area_factor():
    out = []
    for i, ((a, b, c, d), area) in enumerate(AREA_CASES):
        det = a * d - b * c
        new = abs(det) * area
        assert det != 0
        pos = i % 4
        correct = numO(new)
        cands = [numO(abs(det)), numO(area * abs(a * d + b * c)), numO(area + abs(det)),
                 numO(area * abs(a + d)), numO(2 * new)]
        out.append({
            "statement": "A figure of area $%d$ is transformed by the matrix $%s$. Find the "
                         "area of the image." % (area, pm(a, b, c, d)),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The determinant is $%s \\cdot %s - %s \\cdot %s = %d$, and areas "
                           "are multiplied by its absolute value: $%d \\cdot %d = %d$."
                           % (n(a), n(d), n(b), n(c), det, area, abs(det), new),
            "check": ["(%d)*(%d) - (%d)*(%d) == %d" % (a, d, b, c, det),
                      "Abs(%d)*%d == %d" % (det, area, new)],
        })
    return out


# (first transformation, second transformation) — reflections and rotations
# chosen so that BA and AB genuinely differ, which is what the form drills.
COMPOSE_PAIRS = [
    (("a reflection in the $x$-axis", (1, 0, 0, -1)),
     ("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0))),
    (("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0)),
     ("a reflection in the $x$-axis", (1, 0, 0, -1))),
    (("a reflection in the $y$-axis", (-1, 0, 0, 1)),
     ("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0))),
    (("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0)),
     ("a reflection in the $y$-axis", (-1, 0, 0, 1))),
    (("a reflection in the line $y = x$", (0, 1, 1, 0)),
     ("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0))),
    (("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0)),
     ("a reflection in the line $y = x$", (0, 1, 1, 0))),
    (("a reflection in the $x$-axis", (1, 0, 0, -1)),
     ("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0))),
    (("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0)),
     ("a reflection in the $x$-axis", (1, 0, 0, -1))),
    (("a reflection in the line $y = -x$", (0, -1, -1, 0)),
     ("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0))),
    (("a rotation of $90°$ counter-clockwise about the origin", (0, -1, 1, 0)),
     ("a reflection in the line $y = -x$", (0, -1, -1, 0))),
    (("a reflection in the $y$-axis", (-1, 0, 0, 1)),
     ("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0))),
    (("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0)),
     ("a reflection in the $y$-axis", (-1, 0, 0, 1))),
    (("a reflection in the line $y = x$", (0, 1, 1, 0)),
     ("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0))),
    (("a rotation of $270°$ counter-clockwise about the origin", (0, 1, -1, 0)),
     ("a reflection in the line $y = x$", (0, 1, 1, 0))),
]


def gen_compose():
    out = []
    for i, ((n1, m1), (n2, m2)) in enumerate(COMPOSE_PAIRS):
        A, B = Matrix(2, 2, list(m1)), Matrix(2, 2, list(m2))
        BA, AB = B * A, A * B
        assert BA != AB
        pos = i % 4
        correct = pmO(BA[0, 0], BA[0, 1], BA[1, 0], BA[1, 1])
        cands = [pmO(AB[0, 0], AB[0, 1], AB[1, 0], AB[1, 1]),
                 pmO(*[m1[k] + m2[k] for k in range(4)]),
                 pmO(m1[0], m1[1], m1[2], m1[3]),
                 pmO(m2[0], m2[1], m2[2], m2[3])]
        out.append({
            "statement": "A figure undergoes %s, and then %s. Which single matrix performs "
                         "the combined transformation?" % (n1, n2),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The first transformation stands nearest the point, so the product "
                           "is $%s \\cdot %s = %s$. Multiplying in reading order instead gives "
                           "$%s$ — a different transformation, because matrix multiplication "
                           "does not commute."
                           % (pm(*m2), pm(*m1),
                              pm(BA[0, 0], BA[0, 1], BA[1, 0], BA[1, 1]),
                              pm(AB[0, 0], AB[0, 1], AB[1, 0], AB[1, 1])),
            "check": ["(%d)*(%d) + (%d)*(%d) == %d"
                      % (m2[0], m1[0], m2[1], m1[2], BA[0, 0]),
                      "(%d)*(%d) + (%d)*(%d) == %d"
                      % (m2[2], m1[1], m2[3], m1[3], BA[1, 1])],
        })
    return out


# ===========================================================================
# unit: systems-in-three-unknowns
# ===========================================================================

ROW_EQUATIONS = [
    (4, 0, -1, 9), (3, -1, 0, 5), (1, 0, 5, 4), (0, 2, -3, 7), (2, 5, 0, 1),
    (-1, 3, 0, 6), (5, 0, 2, -3), (1, -4, 0, 8), (0, 1, 6, 2), (7, 2, 0, 4),
    (2, 0, 3, -5), (0, -3, 4, 1), (6, 0, -2, 3), (1, 1, 0, 10),
]


def gen_equation_to_row():
    out = []
    for i, (a, b, c, d) in enumerate(ROW_EQUATIONS):
        assert [a, b, c].count(0) == 1, "exactly one missing unknown per draw"
        pos = i % 4
        correct = row(a, b, c, d)
        # the classic slips: dropping the zero and sliding everything left,
        # putting the constant in the coefficient block, and a sign flip.
        slid = [v for v in (a, b, c) if v != 0] + [d]
        cands = [row(slid[0], slid[1], slid[2], 0) if len(slid) == 3 else row(a, c, b, d),
                 row(a, b, d, c), row(-a, -b, -c, d), row(d, a, b, c),
                 row(a, c, b, d), row(a, b, c, -d)]
        out.append({
            "statement": "Which row of an augmented matrix represents the equation $%s$?"
                         % eqn(a, b, c, d),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The columns hold the coefficients of $x$, $y$ and $z$ in that "
                           "order, and a missing unknown contributes a $0$; the constant "
                           "$%d$ goes past the bar. Dropping the zero shifts every later "
                           "column and solves a different system." % d,
            "check": ["(%d)*1 + (%d)*0 + (%d)*0 == %d" % (a, b, c, a),
                      "(%d)*0 + (%d)*1 + (%d)*0 == %d" % (a, b, c, b)],
        })
    return out


ROW_OPS = [
    ((1, -2, 4, 2), (3, 1, -5, 7), 3), ((1, 2, -1, 3), (2, 5, 1, 8), 2),
    ((1, 0, 2, 5), (4, 1, 3, 1), 4), ((1, 3, 1, -2), (5, 2, 4, 6), 5),
    ((1, -1, 3, 4), (2, 6, 1, 0), 2), ((1, 4, -2, 1), (3, 3, 3, 9), 3),
    ((1, 1, 1, 6), (2, -1, 3, 9), 2), ((1, -3, 2, 0), (6, 1, 5, 4), 6),
    ((1, 2, 5, 7), (3, -2, 1, 2), 3), ((1, 5, -1, 3), (4, 0, 2, 8), 4),
    ((1, -2, 1, 5), (2, 3, 7, 1), 2), ((1, 6, 3, -4), (5, 1, 0, 2), 5),
    ((1, 0, -3, 8), (7, 2, 1, 5), 7), ((1, 2, 2, 1), (3, 5, 8, 3), 3),
]


def gen_row_operation():
    out = []
    for i, (r1, r2, k) in enumerate(ROW_OPS):
        new = tuple(r2[j] - k * r1[j] for j in range(4))
        assert new[0] == 0
        pos = i % 4
        correct = row(*new)
        cands = [row(*[r2[j] + k * r1[j] for j in range(4)]),
                 row(new[0], new[1], new[2], r2[3]),
                 row(*[r1[j] - k * r2[j] for j in range(4)]),
                 row(*[r2[j] - r1[j] for j in range(4)])]
        out.append({
            "statement": "An augmented matrix has $R_1 = %s$ and $R_2 = %s$. What is the "
                         "new $R_2$ after the operation $R_2 - %dR_1$?"
                         % (row(*r1)[1:-1], row(*r2)[1:-1], k),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Subtract entry by entry, INCLUDING the constant past the bar: "
                           "$%s - %s \\cdot %s = %d$, and likewise across the row, giving "
                           "$%s$. Leaving the constant untouched is the classic error."
                           % (n(r2[3]), n(k), n(r1[3]), new[3], row(*new)[1:-1]),
            "check": ["(%d) - (%d)*(%d) == %d" % (r2[0], k, r1[0], new[0]),
                      "(%d) - (%d)*(%d) == %d" % (r2[1], k, r1[1], new[1]),
                      "(%d) - (%d)*(%d) == %d" % (r2[3], k, r1[3], new[3])],
        })
    return out


# (a1, b1, c1), (b2, c2), c3 with an integer solution (x, y, z)
BACK_SUB = [
    ((1, 1, 1), (1, 2), 3, (0, -1, 3)), ((1, 2, -1), (1, 1), 2, (1, 3, 4)),
    ((1, -1, 2), (2, 1), 5, (2, 1, 5)), ((1, 3, 1), (1, -2), 4, (-1, 5, 1)),
    ((1, 1, -2), (3, 1), 2, (4, 2, 3)), ((1, -2, 1), (1, 3), 6, (3, -2, 1)),
    ((1, 2, 2), (2, -1), 3, (2, 4, 6)), ((1, 1, 3), (1, 1), 4, (5, 1, 4)),
    ((1, -1, 1), (2, 3), 5, (1, 2, 5)), ((1, 4, -1), (1, 2), 3, (0, 3, 1)),
    ((1, 2, 1), (3, -2), 2, (6, 1, 2)), ((1, -3, 2), (1, 4), 7, (2, 5, 3)),
    ((1, 1, 4), (2, 2), 6, (3, 2, 1)), ((1, 5, 1), (1, -1), 4, (-2, 4, 2)),
]


def gen_back_substitution():
    out = []
    for i, ((a1, b1, c1), (b2, c2), c3, (x, y, z)) in enumerate(BACK_SUB):
        d1, d2, d3 = a1 * x + b1 * y + c1 * z, b2 * y + c2 * z, c3 * z
        assert x != y and y != z and x != z
        pos = i % 4
        correct = numO(x)
        cands = [numO(y), numO(z), numO(d1), numO(x + 1), numO(-x)]
        rows = [eqn(a1, b1, c1, d1), eqn(0, b2, c2, d2), eqn(0, 0, c3, d3)]
        out.append({
            "statement": "Solve $%s$ for $x$." % sys3(rows),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The system is already triangular. The last equation gives "
                           "$z = %d$, the second then gives $y = %d$, and substituting both "
                           "into the first gives $x = %d$." % (z, y, x),
            "check": ["Eq(Rational(%d, %d), %d)" % (d3, c3, z),
                      "Eq(Rational(%d - (%d)*(%d), %d), %d)" % (d2, c2, z, b2, y),
                      "Eq((%d)*(%d) + (%d)*(%d) + (%d)*(%d), %d)"
                      % (a1, x, b1, y, c1, z, d1)],
        })
    return out


DET3 = [
    [[2, -1, 3], [0, 4, 1], [5, 2, -2]], [[1, 2, 0], [3, -1, 4], [2, 0, 5]],
    [[3, 0, 0], [7, -2, 5], [1, 6, 4]], [[1, 0, 2], [2, -1, 3], [4, 1, 8]],
    [[2, 1, 0], [1, 3, -1], [0, 2, 4]], [[4, -2, 1], [3, 0, 5], [-1, 2, 2]],
    [[1, 1, 2], [2, -1, 1], [1, 2, -1]], [[5, 0, 1], [2, 3, 0], [1, 1, 2]],
    [[2, 2, 1], [0, 1, 3], [4, 0, 1]], [[1, -1, 0], [2, 3, 1], [0, 4, 2]],
    [[3, 1, 2], [1, 0, 4], [2, 5, 1]], [[1, 3, 0], [4, 1, 2], [0, 2, 5]],
    [[2, 0, 3], [1, 4, 1], [3, 1, 0]], [[6, 1, 0], [2, 2, 3], [1, 0, 4]],
]


def gen_determinant_3x3():
    out = []
    for i, rows in enumerate(DET3):
        (a, b, c), (d, e, f), (g, h, k) = rows
        det = int(Matrix(rows).det())
        pos = i % 4
        # the named error models: dropping the middle minus sign, and adding
        # the three "diagonal" products without the corrections.
        no_minus = a * (e * k - f * h) + b * (d * k - f * g) + c * (d * h - e * g)
        diag = a * e * k + b * f * g + c * d * h
        correct = numO(det)
        cands = [numO(no_minus), numO(diag), numO(-det), numO(a * e * k),
                 numO(det + 1)]
        out.append({
            "statement": "Compute $\\det %s$." % m3(rows),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "Expand along the first row with the signs $+, -, +$: "
                           "$%s(%s \\cdot %s - %s \\cdot %s) - %s(%s \\cdot %s - %s \\cdot "
                           "%s) + %s(%s \\cdot %s - %s \\cdot %s) = %d$. Forgetting the "
                           "middle minus sign is the usual error."
                           % (n(a), n(e), n(k), n(f), n(h), n(b), n(d), n(k), n(f), n(g),
                              n(c), n(d), n(h), n(e), n(g), det),
            "check": [det3_check(rows, det)],
        })
    return out


# (rows after elimination, outcome key)
CLASSIFY = [
    ([(1, 2, -1, 3), (0, 1, 4, 5), (0, 0, 0, 7)], "none"),
    ([(1, 1, 1, 6), (0, 3, 2, 4), (0, 0, 0, 0)], "inf"),
    ([(1, -1, 2, 4), (0, 2, 1, 3), (0, 0, 5, 10)], "one"),
    ([(1, 3, 0, 2), (0, 1, -2, 1), (0, 0, 0, -4)], "none"),
    ([(1, 0, 4, 7), (0, 1, 1, 2), (0, 0, 3, 9)], "one"),
    ([(1, 2, 2, 5), (0, -1, 3, 1), (0, 0, 0, 0)], "inf"),
    ([(1, 1, -3, 0), (0, 4, 1, 8), (0, 0, 2, 6)], "one"),
    ([(1, -2, 1, 9), (0, 1, 5, 3), (0, 0, 0, 2)], "none"),
    ([(1, 5, 1, 1), (0, 2, -1, 4), (0, 0, 0, 0)], "inf"),
    ([(1, 1, 2, 8), (0, 3, 3, 6), (0, 0, 1, 4)], "one"),
    ([(1, -1, 0, 5), (0, 1, 2, 7), (0, 0, 0, -1)], "none"),
    ([(1, 4, -1, 3), (0, 1, 1, 5), (0, 0, 0, 0)], "inf"),
    ([(1, 2, 3, 6), (0, 5, 2, 1), (0, 0, 4, 8)], "one"),
    ([(1, 0, -2, 2), (0, 2, 1, 3), (0, 0, 0, 5)], "none"),
]

OUTCOMES = {
    "none": "no solution",
    "one": "exactly one solution",
    "inf": "infinitely many solutions",
}
ALL_OUTCOMES = ["no solution", "exactly one solution", "infinitely many solutions",
                "exactly two solutions"]


def gen_classify_solutions():
    out = []
    for i, (rows, key) in enumerate(CLASSIFY):
        pos = i % 4
        correct = OUTCOMES[key]
        cands = [o for o in ALL_OUTCOMES if o != correct]
        last = rows[2]
        if key == "none":
            why = ("The last row reads $0 = %d$, which nothing can satisfy." % last[3])
            check = ["Ne(0, %d)" % last[3]]
        elif key == "inf":
            why = ("The last row reads $0 = 0$: one equation carried no new information, "
                   "so a free unknown remains and the solutions form a line.")
            check = ["Eq(0*1 + 0*2 + 0*3, 0)"]
        else:
            why = ("The last row gives $z = %s$ on its own, and back-substitution then "
                   "pins down $y$ and $x$ uniquely." % L(Rational(last[3], last[2])))
            check = ["Ne(%d, 0)" % last[2],
                     "Eq(Rational(%d, %d), %s)" % (last[3], last[2],
                                                   L(Rational(last[3], last[2])))]
        out.append({
            "statement": "Gaussian elimination reduces a system in $x$, $y$, $z$ to the rows "
                         "%s, %s and %s. How many solutions does the system have?"
                         % (row(*rows[0]), row(*rows[1]), row(*rows[2])),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": why,
            "check": check,
        })
    return out


# coefficient matrix + the integer solution it is built around
CRAMER = [
    ([[2, 1, -1], [1, -1, 2], [3, 2, 1]], (2, 3, 4)),
    ([[1, 1, 1], [2, -1, 1], [1, 2, -1]], (1, 2, 3)),
    ([[2, 1, 1], [1, 2, 1], [1, 1, 2]], (1, 2, 3)),
    ([[1, 2, 1], [2, -1, 1], [1, 1, 3]], (3, 1, 2)),
    ([[1, 1, 2], [2, 1, 1], [1, 2, 1]], (2, 3, 1)),
    ([[3, 1, 1], [1, 2, 1], [1, 1, 4]], (1, 3, 2)),
    ([[1, -1, 1], [2, 1, 1], [1, 1, 2]], (4, 1, 2)),
    ([[2, 1, 3], [1, 2, 1], [3, 1, 1]], (1, 2, 4)),
    ([[1, 2, -1], [2, 1, 1], [1, 3, 2]], (2, 1, 3)),
    ([[4, 1, 1], [1, 3, 1], [1, 1, 2]], (2, 1, 3)),
    ([[1, 1, 3], [2, 3, 1], [1, 2, 2]], (3, 2, 1)),
    ([[2, 3, 1], [1, 1, 2], [3, 1, 1]], (1, 4, 2)),
    ([[1, 4, 1], [2, 1, 3], [1, 1, 1]], (2, 1, 3)),
    ([[3, 2, 1], [1, 1, 3], [2, 3, 1]], (1, 2, 4)),
]


def gen_cramer_3x3():
    out = []
    for i, (rows, (x, y, z)) in enumerate(CRAMER):
        A = Matrix(rows)
        D = int(A.det())
        assert D != 0
        assert len({x, y, z}) == 3
        consts = [rows[r][0] * x + rows[r][1] * y + rows[r][2] * z for r in range(3)]
        Ax = A.copy()
        Ax[:, 0] = Matrix(consts)
        Dx = int(Ax.det())
        assert Rational(Dx, D) == x
        pos = i % 4
        correct = numO(x)
        cands = [numO(y), numO(z), numO(Dx), numO(D), numO(x + 1)]
        eqs = [eqn(rows[r][0], rows[r][1], rows[r][2], consts[r]) for r in range(3)]
        out.append({
            "statement": "Use Cramer's rule to find $x$ for the system $%s$." % sys3(eqs),
            "options": place(correct, cands, pos), "correctIndex": pos,
            "explanation": "The coefficient determinant is $D = %d$. Replacing the FIRST "
                           "column by the constants $(%d; %d; %d)$ gives $D_x = %d$, so "
                           "$x = \\dfrac{%d}{%d} = %d$."
                           % (D, consts[0], consts[1], consts[2], Dx, Dx, D, x),
            "check": [det3_check(rows, D),
                      det3_check([[consts[0], rows[0][1], rows[0][2]],
                                  [consts[1], rows[1][1], rows[1][2]],
                                  [consts[2], rows[2][1], rows[2][2]]], Dx),
                      "Eq(Rational(%d, %d), %d)" % (Dx, D, x)],
        })
    return out


# ---------------------------------------------------------------------------
# form metadata: (id, title, level, variant-id prefix, unit, generator)
# ---------------------------------------------------------------------------

FORMS_META = [
    ("tm-matrix-from-rules", "The matrix of a coordinate rule", 1, "VM-tmr",
     "transformation-matrices", gen_matrix_from_rules,
     "Stack the two coordinate rules into a matrix, rows first."),
    ("tm-image-of-point", "The image of a point", 1, "VM-tmi",
     "transformation-matrices", gen_image_of_point,
     "Multiply a matrix by a point written as a column."),
    ("tm-standard-matrix", "The matrix of a named transformation", 2, "VM-tms",
     "transformation-matrices", gen_standard_matrix,
     "Build reflections, rotations and enlargements from the two unit points."),
    ("tm-identify", "Naming a transformation from its matrix", 2, "VM-tmn",
     "transformation-matrices", gen_identify_transformation,
     "Read the determinant and the columns, then name the map."),
    ("tm-area-factor", "Area under a transformation", 2, "VM-tma",
     "transformation-matrices", gen_area_factor,
     "Areas are multiplied by the absolute value of the determinant."),
    ("tm-compose", "Composing two transformations", 3, "VM-tmc",
     "transformation-matrices", gen_compose,
     "The first transformation is the right-hand factor of the product."),
    ("su-equation-to-row", "An equation as a matrix row", 1, "VM-sur",
     "systems-in-three-unknowns", gen_equation_to_row,
     "Write a zero for every missing unknown, constant past the bar."),
    ("su-row-operation", "One row operation", 1, "VM-suo",
     "systems-in-three-unknowns", gen_row_operation,
     "Apply R2 - kR1 across all four entries, constant included."),
    ("su-back-substitution", "Back-substitution", 2, "VM-suz",
     "systems-in-three-unknowns", gen_back_substitution,
     "Read a triangular system from the bottom row upward."),
    ("su-determinant-3x3", "A 3x3 determinant", 2, "VM-sud",
     "systems-in-three-unknowns", gen_determinant_3x3,
     "Expand into three 2x2 minors with the signs plus, minus, plus."),
    ("su-classify", "How many solutions?", 2, "VM-suc",
     "systems-in-three-unknowns", gen_classify_solutions,
     "Read the final row: a contradiction, a free unknown, or a unique answer."),
    ("su-cramer-3x3", "Cramer's rule for three unknowns", 3, "VM-sux",
     "systems-in-three-unknowns", gen_cramer_3x3,
     "Replace the unknown's column with the constants and divide by D."),
]


def forms():
    """The twelve forms for units 7 and 8, ready to append to the subject."""
    out = []
    for fid, title, level, prefix, unit, gen, skill in FORMS_META:
        raw = gen()
        assert len(raw) >= 12, "%s: only %d variants" % (fid, len(raw))
        variants = []
        for i, v in enumerate(raw):
            vd = {"id": "%s-v%02d" % (prefix, i + 1)}
            vd.update(v)
            variants.append(vd)
        out.append({"id": fid, "title": title, "level": level, "skill": skill,
                    "unit": unit, "variants": variants})
    return out


if __name__ == "__main__":
    fs = forms()
    total = sum(len(f["variants"]) for f in fs)
    ids = [v["id"] for f in fs for v in f["variants"]]
    assert len(ids) == len(set(ids)), "variant ids not unique"
    n_checks = 0
    for f in fs:
        for v in f["variants"]:
            assert len(v["options"]) == 4 and len(set(v["options"])) == 4, v["id"]
            assert v["options"][v["correctIndex"]]
            assert v["check"], v["id"]
            for expr in v["check"]:
                value = sympify(expr)
                assert value is not None and bool(value) is True, (v["id"], expr, value)
                n_checks += 1
    print("SELFCHECK OK  forms=%d  variants=%d  checks=%d" % (len(fs), total, n_checks))
