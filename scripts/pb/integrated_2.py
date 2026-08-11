# -*- coding: utf-8 -*-
"""Problem-bank subject: Integrated Math 2 — mirrors /math/integrated-2.

Same construction as integrated_1.py: library archetypes are REUSED where
they drill exactly what an IM2 unit teaches (re-identified with an `im2-`
prefix, since variant ids are globally unique across the bank), and the
IM2-specific material is authored fresh below.

Every generator sweeps a parameter grid wide enough to fill a form after
degenerate draws are discarded, and every value stays exact — sympy checks
are built from Rational, never from Python float division, and never from
fmt() output (which is LaTeX and will not sympify).

Self-check:  python3 scripts/pb/integrated_2.py
Regenerate:  python3 scripts/build_problembank.py
"""
import copy
import importlib.util
import os
import sys

from sympy import Integer, Rational, sqrt

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import (P, closed, figure, fmt, form, lin, mk_num, mk_txt,  # noqa: E402
                    on_circle, pt, quad, radical, seg, sgn, xpm)
import integrated_2_more as more  # noqa: E402

SLUG = "integrated-2"
TITLE = "Integrated Math 2"
TITLE_MN = "Нэгдсэн математик 2"
BLURB = ("Unit-by-unit practice for Integrated Math 2 — rational exponents "
         "and quadratics through similarity, right-triangle trigonometry, "
         "circles and probability.")

UNITS = [
    {"id": "rational-exponents-and-radicals", "title": "Rational Exponents & Radicals",
     "blurb": "Fractional powers forced by the exponent rules, simplifying radicals, and rational versus irrational sums."},
    {"id": "polynomials-and-factoring", "title": "Polynomials & Factoring",
     "blurb": "Polynomial arithmetic and closure, then every factoring technique from a common factor to the difference of squares."},
    {"id": "quadratic-functions", "title": "Quadratic Functions",
     "blurb": "The parabola and its vertex, the three forms and what each reveals, and quadratic against linear and exponential growth."},
    {"id": "solving-quadratic-equations", "title": "Solving Quadratic Equations",
     "blurb": "Factoring, square roots, completing the square and the formula; the discriminant; and the complex numbers it forces."},
    {"id": "similarity-and-dilations", "title": "Similarity & Dilations",
     "blurb": "Dilation as the one non-rigid transformation, the AA criterion, and the side-splitter and midsegment theorems."},
    {"id": "right-triangle-trigonometry", "title": "Right-Triangle Trigonometry",
     "blurb": "Sine, cosine and tangent as ratios similarity makes well defined, the special triangles, and complementary angles."},
    {"id": "circles", "title": "Circles",
     "blurb": "Central and inscribed angles, tangents and chords, arc length and sector area, and the equation of a circle."},
    {"id": "geometric-measurement-and-modelling",
     "title": "Geometric Measurement & Modelling",
     "blurb": "Volume and surface area of every solid on the reference sheet, running the "
              "formulas backwards, cross-sections and solids of revolution, and density "
              "and design problems."},
    {"id": "probability", "title": "Probability",
     "blurb": "Sample spaces, unions and intersections, conditional probability and independence, and two-way tables."},
]

REMAP = {
    "exponent-laws": "rational-exponents-and-radicals",
    "vertex-read": "quadratic-functions",
    "complete-square-min": "quadratic-functions",
    "factored-roots": "solving-quadratic-equations",
    "discriminant": "solving-quadratic-equations",
    "quadratic-inequality": "solving-quadratic-equations",
    "tangency-parameter": "solving-quadratic-equations",
    "similar-triangles": "similarity-and-dilations",
    "right-triangle-side": "right-triangle-trigonometry",
    "special-triangles": "right-triangle-trigonometry",
    "sin-to-cos-tan": "right-triangle-trigonometry",
    "circle-basics": "circles",
    "sector-area": "circles",
}

SOURCES = ["algebra", "functions", "geometry", "trigonometry"]


def _load(name):
    spec = importlib.util.spec_from_file_location(
        "pbsrc2_%s" % name, os.path.join(PB, "%s.py" % name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _remapped_forms():
    src = {}
    for name in SOURCES:
        for f in _load(name).build()["forms"]:
            src[f["id"]] = f
    out = []
    for fid, unit in REMAP.items():
        f = copy.deepcopy(src[fid])   # all subjects build in one process
        f["unit"] = unit
        f["id"] = "im2-%s" % fid
        for v in f["variants"]:
            v["id"] = "im2-%s" % v["id"]
        out.append(f)
    return out


# ===========================================================================
# Unit 1 — Rational Exponents & Radicals
# ===========================================================================

def _g_simplify_radical():
    raws = []
    for a in (2, 3, 4, 5, 6, 7, 10):
        for b in (2, 3, 5, 6, 7, 10, 11, 13):
            n = a * a * b
            if n > 900:
                continue
            raws.append({
                "statement": "Simplify $\\sqrt{%d}$ completely." % n,
                "correct": "$%s$" % radical(a, b),
                "dvals": ["$%s$" % radical(b, a), "$%s$" % radical(a * b, 1),
                          "$%s$" % radical(1, n)],
                "explanation": ("Pull out the largest square factor: $%d = %d^2 \\times %d$, so "
                                "$\\sqrt{%d} = %s$. Leaving it as $\\sqrt{%d}$ is not simplified, "
                                "and swapping which part comes out changes the value."
                                % (n, a, b, n, radical(a, b), n)),
                "check": ["Eq(sqrt(%d), %d*sqrt(%d))" % (n, a, b)],
            })
    return raws


def _g_rational_exponent():
    raws = []
    # Built FORWARD from the root r, so `base` is a perfect power by
    # construction — no float nth-root and no rounding to check.
    grid = []
    for r in (2, 3, 4, 5, 6, 7, 10):
        for root in (2, 3, 4, 5):
            base = r ** root
            if base > 1000:
                continue
            for power in (2, 3, 5):
                grid.append((base, root, power, r))
    for base, root, power, r in grid:
        val = Integer(r) ** power
        if val > 100000:
            continue
        raws.append({
            "statement": "Evaluate $%d^{%d/%d}$." % (base, power, root),
            "correct": val,
            # error models: multiplied instead of powering the root; took the
            # root only; applied the exponent to the base first then rooted wrong
            "dvals": [Integer(r) * power, Integer(r), Integer(base) * power],
            "explanation": ("The denominator is the ROOT and the numerator is the POWER: "
                            "$%d^{%d/%d} = \\left(\\sqrt[%d]{%d}\\right)^{%d} = %d^{%d} = %s$. "
                            "Taking the root and stopping ignores the numerator."
                            % (base, power, root, root, base, power, r, power, fmt(val))),
            "check": ["Eq(Integer(%d)**Rational(%d,%d), %s)" % (base, power, root, val)],
        })
    return raws


def _g_radical_arithmetic():
    raws = []
    for c1, c2, b in [(3, 5, 2), (7, 2, 3), (4, 9, 5), (6, 1, 7), (8, 3, 2), (5, 5, 6),
                      (2, 11, 3), (9, 4, 10), (6, 7, 5), (10, 3, 2), (4, 4, 11), (7, 6, 3)]:
        s = c1 + c2
        raws.append({
            "statement": "Simplify $%s + %s$." % (radical(c1, b), radical(c2, b)),
            "correct": "$%s$" % radical(s, b),
            "dvals": ["$%s$" % radical(s, b * 2), "$%s$" % radical(c1 * c2, b),
                      "$\\sqrt{%d}$" % ((c1 + c2) * b)],
            "explanation": ("Like radicals add like terms — the $\\sqrt{%d}$ is the 'unit': "
                            "$%d\\sqrt{%d} + %d\\sqrt{%d} = %d\\sqrt{%d}$. The radicand does "
                            "NOT change; adding it is the classic error."
                            % (b, c1, b, c2, b, s, b)),
            "check": ["Eq(%d*sqrt(%d) + %d*sqrt(%d), %d*sqrt(%d))" % (c1, b, c2, b, s, b)],
        })
    for a, b in [(2, 3), (3, 5), (5, 2), (7, 3), (2, 11), (3, 7), (5, 6), (6, 5),
                 (10, 3), (2, 13), (7, 2), (11, 3)]:
        raws.append({
            "statement": "Simplify $\\sqrt{%d} \\times \\sqrt{%d}$." % (a, b),
            "correct": "$\\sqrt{%d}$" % (a * b),
            "dvals": ["$\\sqrt{%d}$" % (a + b), "$%d\\sqrt{%d}$" % (a, b),
                      "$%d$" % (a * b)],
            "explanation": ("Radicals MULTIPLY under one root: "
                            "$\\sqrt{%d}\\sqrt{%d} = \\sqrt{%d \\times %d} = \\sqrt{%d}$. "
                            "Adding the radicands is the mirror-image of the addition error."
                            % (a, b, a, b, a * b)),
            "check": ["Eq(sqrt(%d)*sqrt(%d), sqrt(%d))" % (a, b, a * b)],
        })
    return raws


def _g_rational_irrational():
    raws = []
    for n, r in [(3, 2), (5, 3), (7, 5), (2, 7), (11, 6), (4, 10), (9, 3), (6, 11),
                 (8, 5), (12, 2), (10, 13), (1, 15)]:
        raws.append({
            "statement": ("Is $%d + \\sqrt{%d}$ rational or irrational, and why?" % (n, r)),
            "correct": "irrational — a rational plus an irrational is always irrational",
            "dvals": ["rational — the sum of two reals is rational",
                      "rational — $%d$ is rational so the sum is too" % n,
                      "it depends on the value of $\\sqrt{%d}$" % r],
            "explanation": ("$\\sqrt{%d}$ is irrational. If $%d + \\sqrt{%d}$ were rational, "
                            "subtracting the rational $%d$ would make $\\sqrt{%d}$ rational too "
                            "— a contradiction. So the sum must be irrational."
                            % (r, n, r, n, r)),
            "check": ["Eq(sqrt(%d)**2, %d)" % (r, r)],
        })
    for a, b in [(4, 9), (16, 25), (36, 49), (9, 64), (25, 81), (100, 4), (144, 9),
                 (49, 16), (121, 36), (169, 25), (196, 49), (225, 64)]:
        v = Integer(int(a ** 0.5)) + Integer(int(b ** 0.5))
        raws.append({
            "statement": ("Is $\\sqrt{%d} + \\sqrt{%d}$ rational or irrational?" % (a, b)),
            "correct": "rational — it equals $%s$" % fmt(v),
            "dvals": ["irrational — it contains square roots",
                      "irrational — a sum of roots is never rational",
                      "rational — it equals $\\sqrt{%d}$" % (a + b)],
            "explanation": ("Both are PERFECT squares: $\\sqrt{%d} = %d$ and $\\sqrt{%d} = %d$, "
                            "so the sum is $%s$ — rational. A radical sign does not by itself "
                            "make a number irrational, and roots do not add under one radical."
                            % (a, int(a ** 0.5), b, int(b ** 0.5), fmt(v))),
            "check": ["Eq(sqrt(%d) + sqrt(%d), %s)" % (a, b, v)],
        })
    return raws


# ===========================================================================
# Unit 2 — Polynomials & Factoring
# ===========================================================================

def _g_multiply_binomials():
    raws = []
    grid = [(p, q) for p in (2, 3, 4, 5, -2, -3, -4, 6, -5, 7)
            for q in (3, -4, 5, 7, -6, 2)]
    for p, q in grid:
        b, c = p + q, p * q
        raws.append({
            "statement": "Expand $%s%s$." % (xpm(p), xpm(q)),
            "correct": "$%s$" % quad(1, b, c),
            "dvals": ["$%s$" % quad(1, p * q, p + q), "$%s$" % quad(1, 0, c),
                      "$%s$" % quad(1, b, p * q + 1)],
            "explanation": ("Each term of the first bracket multiplies each of the second: "
                            "$x^2 %s %dx %s %dx %s %d$, and the middle terms combine to give "
                            "$%s$. The constant is the PRODUCT $%d$ and the middle coefficient "
                            "is the SUM $%d$ — swapping them is the usual slip."
                            % ("+" if p >= 0 else "-", abs(p), "+" if q >= 0 else "-", abs(q),
                               "+" if c >= 0 else "-", abs(c), quad(1, b, c), c, b)),
            "check": ["Eq(expand((x + (%d))*(x + (%d))), x**2 + (%d)*x + (%d))" % (p, q, b, c)],
        })
    return raws


def _g_factor_trinomial():
    raws = []
    grid = [(p, q) for p in (2, 3, 4, 5, -2, -3, -4, 6, -5, 7, -6, 8)
            for q in (3, -4, 5, 7, -6)]
    for p, q in grid:
        b, c = p + q, p * q
        raws.append({
            "statement": "Factor $%s$ completely." % quad(1, b, c),
            "correct": "$%s%s$" % (xpm(p), xpm(q)),
            "dvals": ["$%s%s$" % (xpm(-p), xpm(-q)), "$%s%s$" % (xpm(b), xpm(c)),
                      "$%s%s$" % (xpm(p), xpm(-q))],
            "explanation": ("Find two numbers multiplying to $%d$ and adding to $%d$: "
                            "$%d$ and $%d$. So the factorisation is $%s%s$. Check by "
                            "expanding — the signs must reproduce BOTH the middle term and "
                            "the constant." % (c, b, p, q, xpm(p), xpm(q))),
            "check": ["Eq(expand((x + (%d))*(x + (%d))), x**2 + (%d)*x + (%d))" % (p, q, b, c)],
        })
    return raws


def _g_difference_squares():
    raws = []
    for a in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        for b in (1, 2, 3, 4, 5, 6, 7):
            if a == b:
                continue
            raws.append({
                "statement": "Factor $%s$." % quad(a * a, 0, -(b * b)),
                "correct": "$(%dx - %d)(%dx + %d)$" % (a, b, a, b),
                "dvals": ["$(%dx - %d)^2$" % (a, b), "$(%dx + %d)^2$" % (a, b),
                          "$(%dx - %d)(%dx - %d)$" % (a, b, a, b)],
                "explanation": ("Both parts are squares: $%dx^2 = (%dx)^2$ and $%d = %d^2$. "
                                "A difference of squares factors as a SUM times a DIFFERENCE: "
                                "$(%dx - %d)(%dx + %d)$. A repeated bracket would give a middle "
                                "term, which this expression does not have."
                                % (a * a, a, b * b, b, a, b, a, b)),
                "check": ["Eq(expand((%d*x - %d)*(%d*x + %d)), %d*x**2 - %d)"
                          % (a, b, a, b, a * a, b * b)],
            })
    return raws


def _g_gcf_factor():
    raws = []
    for g in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12):
        for p, q in [(3, 5), (2, 7), (4, 9), (5, 3), (6, 11), (7, 2)]:
            raws.append({
                "statement": "Factor out the greatest common factor: $%dx^2 + %dx$."
                             % (g * p, g * q),
                "correct": "$%dx(%dx + %d)$" % (g, p, q),
                "dvals": ["$%d(%dx^2 + %dx)$" % (g, p, q), "$x(%dx + %d)$" % (g * p, g * q),
                          "$%dx(%dx + %d)$" % (g * p, 1, q)],
                "explanation": ("The numeric GCF of $%d$ and $%d$ is $%d$, and both terms carry "
                                "at least one $x$, so the full common factor is $%dx$: "
                                "$%dx(%dx + %d)$. Pulling out only the number leaves an $x$ "
                                "behind." % (g * p, g * q, g, g, g, p, q)),
                "check": ["Eq(expand(%d*x*(%d*x + %d)), %d*x**2 + %d*x)"
                          % (g, p, q, g * p, g * q)],
            })
    return raws


# ===========================================================================
# Unit 3 — Quadratic Functions
# ===========================================================================

def _g_axis_vertex():
    raws = []
    grid = [(a, b, c) for a in (1, 2, -1, 3, -2, 4, -3, 5)
            for b, c in ((-8, 3), (6, -5), (12, 7), (-4, 1), (10, -2), (-6, 4))]
    for a, b, c in grid:
        ax = Rational(-b, 2 * a)
        vy = a * ax * ax + b * ax + c
        raws.append({
            "statement": "Find the axis of symmetry of $y = %s$." % quad(a, b, c),
            "correct": ax,
            # error models: dropped the minus; halved b only; used c
            "dvals": [Rational(b, 2 * a), Rational(-b, 2), Rational(c, a)],
            "explanation": ("The axis is $x = -\\frac{b}{2a} = -\\frac{%d}{2(%d)} = %s$. The "
                            "MINUS is part of the formula — dropping it reflects the axis to "
                            "the wrong side of the $y$-axis." % (b, a, fmt(ax))),
            "check": ["Eq(Rational(-(%d), 2*(%d)), Rational(%d,%d))" % (b, a, ax.p, ax.q)],
        })
        raws.append({
            "statement": "Find the $y$-coordinate of the vertex of $y = %s$." % quad(a, b, c),
            "correct": vy,
            "dvals": [ax, Integer(c), vy + a],
            "explanation": ("The vertex sits at $x = %s$; substituting gives $y = %s$. The "
                            "$x$-coordinate $%s$ answers a different question, and $c = %d$ is "
                            "the $y$-INTERCEPT, not the vertex."
                            % (fmt(ax), fmt(vy), fmt(ax), c)),
            "check": ["Eq((%d)*Rational(%d,%d)**2 + (%d)*Rational(%d,%d) + (%d), Rational(%d,%d))"
                      % (a, ax.p, ax.q, b, ax.p, ax.q, c, Rational(vy).p, Rational(vy).q)],
        })
    return raws


def _g_which_form():
    raws = []
    setups = [
        ("standard form $y = ax^2 + bx + c$", "the $y$-intercept, read straight off as $c$",
         ["the roots, read straight off", "the vertex, read straight off",
          "the axis of symmetry, read straight off"]),
        ("factored form $y = a(x - p)(x - q)$", "the roots, read straight off as $p$ and $q$",
         ["the vertex, read straight off", "the $y$-intercept, read straight off",
          "the maximum value, read straight off"]),
        ("vertex form $y = a(x - h)^2 + k$", "the vertex, read straight off as $(h, k)$",
         ["the roots, read straight off", "the $y$-intercept, read straight off",
          "the leading coefficient's sign only"]),
    ]
    params = [(1, 2, 3), (2, -3, 5), (-1, 4, 1), (3, 1, -2), (-2, 5, 4), (4, -1, 6),
              (1, -5, 2), (2, 3, -4), (-3, 2, 7), (5, -2, 1), (1, 6, -3), (-4, 1, 2)]
    for a, u, v in params:
        for formname, ans, ds in setups:
            raws.append({
                "statement": ("A quadratic is written in %s, with $a = %d$. Which feature does "
                              "this form reveal WITHOUT any algebra?" % (formname, a)),
                "correct": ans,
                "dvals": ds,
                "explanation": ("Each form is chosen for what it exposes. %s Getting a different "
                                "feature out of this form always costs you some work — "
                                "expanding, factoring, or completing the square."
                                % ans.capitalize().replace(", read straight off", " is immediate")),
                "check": ["Eq(%d, %d)" % (a, a)],
            })
    return raws


# ===========================================================================
# Unit 4 — Solving Quadratic Equations
# ===========================================================================

def _g_quadratic_formula():
    raws = []
    # built backwards from integer roots so the arithmetic stays humane
    for r1 in (-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6):
        for a in (1, 2, 3):
            for r2 in (2, -3, 5):
                if r1 == r2:
                    continue
                b, c = -a * (r1 + r2), a * r1 * r2
                bigger = max(r1, r2)
                raws.append({
                    "statement": "Solve $%s = 0$. Give the LARGER root." % quad(a, b, c),
                    "correct": bigger,
                    "dvals": [min(r1, r2), -bigger, bigger + 1],
                    "explanation": ("The discriminant is $%d^2 - 4(%d)(%d) = %d$, so "
                                    "$x = \\frac{%d \\pm \\sqrt{%d}}{%d}$ gives roots $%d$ and "
                                    "$%d$. The larger is $%d$."
                                    % (b, a, c, b * b - 4 * a * c, -b, b * b - 4 * a * c,
                                       2 * a, min(r1, r2), max(r1, r2), bigger)),
                    "check": ["Eq(%d*(%d)**2 + (%d)*(%d) + (%d), 0)" % (a, bigger, b, bigger, c),
                              "Eq(%d*(%d)**2 + (%d)*(%d) + (%d), 0)"
                              % (a, min(r1, r2), b, min(r1, r2), c)],
                })
    return raws


def _g_complex_roots():
    raws = []
    # b^2 - 4ac < 0 forces a complex pair
    for a in (1, 2, 3, 4):
        for b in (2, 4, 6, -2, -4, -6):
            for c in (5, 7, 10, 13):
                disc = b * b - 4 * a * c
                if disc >= 0:
                    continue
                raws.append({
                    "statement": ("How many REAL solutions does $%s = 0$ have, and what does "
                                  "that mean for its graph?" % quad(a, b, c)),
                    "correct": "none — the parabola never crosses the $x$-axis",
                    "dvals": ["one — the parabola touches the $x$-axis",
                              "two — the parabola crosses twice",
                              "infinitely many"],
                    "explanation": ("The discriminant is $%d^2 - 4(%d)(%d) = %d < 0$, so there "
                                    "are no real roots — the solutions are a complex conjugate "
                                    "pair. Graphically the parabola sits entirely off the "
                                    "$x$-axis." % (b, a, c, disc)),
                    "check": ["%d < 0" % disc],
                })
    return raws


# ===========================================================================
# Unit 5 — Similarity & Dilations  (figure-bearing)
# ===========================================================================

def _g_dilation():
    raws = []
    grid = [(x, y, k) for x, y in [(2, 3), (-4, 2), (3, -5), (6, 1), (-2, -6), (5, 4)]
            for k in (2, 3, Rational(1, 2), 4, Rational(1, 3), Rational(3, 2))]
    for x, y, k in grid:
        k = Rational(k)
        ix, iy = Rational(x) * k, Rational(y) * k
        pts_ = [P("O", 0, 0, "O"), P("A", x, y, "A"), P("B", float(ix), float(iy), "A'")]
        fig = figure(pts_, [seg("O", "A"), seg("O", "B", dashed=True)])
        raws.append({
            "statement": ("Dilate $A%s$ about the origin with scale factor $%s$. Where does it "
                          "land?" % (pt(x, y), fmt(k))),
            "correct": "$%s$" % pt(ix, iy),
            "dvals": ["$%s$" % pt(Rational(x) + k, Rational(y) + k),
                      "$%s$" % pt(Rational(x) / k, Rational(y) / k),
                      "$%s$" % pt(ix, y)],
            "explanation": ("A dilation about the origin MULTIPLIES both coordinates by the "
                            "scale factor: $(%s \\cdot %s,\\ %s \\cdot %s) = %s$. Adding the "
                            "factor is a translation, and dividing shrinks when you meant to "
                            "grow." % (fmt(x), fmt(k), fmt(y), fmt(k), pt(ix, iy))),
            "check": ["Eq(%d*Rational(%d,%d), Rational(%d,%d))"
                      % (x, k.p, k.q, Rational(ix).p, Rational(ix).q),
                      "Eq(%d*Rational(%d,%d), Rational(%d,%d))"
                      % (y, k.p, k.q, Rational(iy).p, Rational(iy).q)],
            "geoFigure": fig,
        })
    return raws


def _g_scale_factor():
    raws = []
    grid = [(a, k) for a in (3, 4, 5, 6, 7, 8, 9, 10, 12, 15)
            for k in (2, 3, Rational(1, 2), Rational(3, 2), 4)]
    for a, k in grid:
        k = Rational(k)
        b = Rational(a) * k
        area_k = k * k
        raws.append({
            "statement": ("Two similar figures have corresponding sides $%s$ and $%s$. What is "
                          "the ratio of their AREAS?" % (fmt(a), fmt(b))),
            "correct": area_k,
            "dvals": [k, Rational(1) / k, k * 3],
            "explanation": ("Lengths scale by $%s$, so AREAS scale by the SQUARE of that: "
                            "$%s^2 = %s$. Using the length ratio for area is the single most "
                            "common similarity error." % (fmt(k), fmt(k), fmt(area_k))),
            "check": ["Eq(Rational(%d,%d)**2, Rational(%d,%d))"
                      % (k.p, k.q, area_k.p, area_k.q)],
        })
    return raws


def _g_side_splitter():
    raws = []
    grid = [(a, b, c) for a, b in [(3, 6), (4, 8), (5, 10), (6, 9), (2, 8), (7, 14),
                                   (4, 6), (5, 15), (3, 12), (8, 12)]
            for c in (4, 6, 10)]
    for a, b, c in grid:
        d = Rational(b * c, a)
        pts_ = [P("A", 0, 6, "A"), P("B", -4, 0, "B"), P("C", 4, 0, "C"),
                P("D", -2, 3, "D"), P("E", 2, 3, "E")]
        fig = figure(pts_, closed(["A", "B", "C"]) + [seg("D", "E")])
        raws.append({
            "statement": ("In $\\triangle ABC$, $DE \\parallel BC$ with $D$ on $AB$ and $E$ on "
                          "$AC$. If $AD = %d$, $DB = %d$ and $AE = %d$, find $EC$."
                          % (a, b, c)),
            "correct": d,
            "dvals": [Rational(a * c, b), Rational(b, a) + c, Rational(a + b + c)],
            "explanation": ("The side-splitter theorem gives $\\frac{AD}{DB} = \\frac{AE}{EC}$, "
                            "so $\\frac{%d}{%d} = \\frac{%d}{EC}$ and $EC = %s$. Inverting one "
                            "of the ratios is the usual slip." % (a, b, c, fmt(d))),
            "check": ["Eq(Rational(%d,%d), Rational(%d, %d)/Rational(%d,%d))"
                      % (a, b, c, 1, d.p, d.q)],
            "geoFigure": fig,
        })
    return raws


# ===========================================================================
# Unit 6 — Right-Triangle Trigonometry  (figure-bearing)
# ===========================================================================

_TRIP = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25),
         (12, 16, 20), (20, 21, 29), (10, 24, 26), (15, 20, 25), (9, 40, 41), (12, 35, 37)]


def _g_pick_ratio():
    raws = []
    for opp, adj, hyp in _TRIP:
        pts_ = [P("A", 0, 0, "A"), P("B", adj / 4.0, 0, "B"), P("C", adj / 4.0, opp / 4.0, "C")]
        fig = figure(pts_, closed(["A", "B", "C"]) + [
            {"kind": "angle", "at": "B", "from": "A", "to": "C", "right": True}])
        for name, val, why in [
            ("\\sin A", Rational(opp, hyp), "opposite over hypotenuse"),
            ("\\cos A", Rational(adj, hyp), "adjacent over hypotenuse"),
            ("\\tan A", Rational(opp, adj), "opposite over adjacent"),
        ]:
            others = [v for v in (Rational(opp, hyp), Rational(adj, hyp), Rational(opp, adj),
                                  Rational(hyp, opp)) if v != val]
            raws.append({
                "statement": ("In right triangle $ABC$ the right angle is at $B$, the side "
                              "opposite $A$ is $%d$, the side adjacent to $A$ is $%d$ and the "
                              "hypotenuse is $%d$. Find $%s$." % (opp, adj, hyp, name)),
                "correct": val,
                "dvals": others[:3],
                "explanation": ("$%s$ is %s: $\\frac{%s}{%s} = %s$. SOH-CAH-TOA — the wrong "
                                "options are the OTHER two ratios, so naming the sides before "
                                "dividing is what protects you."
                                % (name, why,
                                   fmt(val.p if val.q else 0) if False else str(val.p),
                                   str(val.q), fmt(val))),
                "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (val.p, val.q, val.p, val.q),
                          "Eq(%d**2 + %d**2, %d**2)" % (opp, adj, hyp)],
                "geoFigure": fig,
            })
    return raws


def _g_complementary():
    raws = []
    for ang in (10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80):
        comp = 90 - ang
        raws.append({
            "statement": ("Given $\\sin %d° = k$, which expression also equals $k$?" % ang),
            "correct": "$\\cos %d°$" % comp,
            "dvals": ["$\\cos %d°$" % ang, "$\\sin %d°$" % comp, "$\\tan %d°$" % ang],
            "explanation": ("Sine and cosine of COMPLEMENTARY angles are equal: "
                            "$\\sin \\theta = \\cos(90° - \\theta)$, so "
                            "$\\sin %d° = \\cos %d°$. This holds because the side opposite one "
                            "acute angle is adjacent to the other."
                            % (ang, comp)),
            "check": ["Eq(%d + %d, 90)" % (ang, comp)],
        })
    for ang in (10, 20, 25, 35, 40, 50, 55, 65, 70, 80):
        comp = 90 - ang
        raws.append({
            "statement": ("In a right triangle one acute angle is $%d°$. What is the other?" % ang),
            "correct": comp,
            "dvals": [ang, 180 - ang, 90 + ang],
            "explanation": ("The angles of a triangle sum to $180°$ and one is $90°$, so the two "
                            "acute angles sum to $90°$: the other is $90 - %d = %d°$."
                            % (ang, comp)),
            "check": ["Eq(90 + %d + %d, 180)" % (ang, comp)],
        })
    return raws


# ===========================================================================
# Unit 7 — Circles  (figure-bearing)
# ===========================================================================

def _g_inscribed_angle():
    raws = []
    for central in (20, 24, 30, 36, 40, 44, 50, 56, 60, 64, 70, 76, 80, 84, 90, 96,
                    100, 104, 110, 116, 120, 124, 130, 136, 140, 144, 150, 156, 160, 170):
        ins = Rational(central, 2)
        pts_ = [P("O", 0, 0, "O"), on_circle("A", 0, 0, 4, 200, "A"),
                on_circle("B", 0, 0, 4, 340, "B"), on_circle("C", 0, 0, 4, 90, "C")]
        fig = figure(pts_, [seg("O", "A"), seg("O", "B"), seg("C", "A"), seg("C", "B"),
                            {"kind": "angle", "at": "O", "from": "A", "to": "B",
                             "label": "%d°" % central}])
        raws.append({
            "statement": ("A central angle subtends arc $AB$ and measures $%d°$. What is the "
                          "measure of an inscribed angle subtending the SAME arc?" % central),
            "correct": ins,
            "dvals": [Integer(central), Integer(central) * 2, Integer(180 - central)],
            "explanation": ("An inscribed angle is HALF the central angle on the same arc: "
                            "$\\frac{%d}{2} = %s°$. Doubling instead of halving reverses the "
                            "theorem." % (central, fmt(ins))),
            "check": ["Eq(Rational(%d,2), Rational(%d,%d))" % (central, ins.p, ins.q)],
            "geoFigure": fig,
        })
    return raws


def _g_circle_equation():
    raws = []
    grid = [(h, k, r) for h, k in [(0, 0), (2, 3), (-1, 4), (5, -2), (-3, -5), (1, 6),
                                   (4, 1), (-2, 2), (3, -4), (-6, 3)]
            for r in (2, 3, 5, 7, 4, 6)]
    for h, k, r in grid:
        raws.append({
            "statement": ("Write the equation of the circle with centre $%s$ and radius $%d$."
                          % (pt(h, k), r)),
            "correct": "$%s^2 + %s^2 = %d$" % (xpm(-h), xpm(-k, "y"), r * r),
            "dvals": ["$%s^2 + %s^2 = %d$" % (xpm(h), xpm(k, "y"), r * r),
                      "$%s^2 + %s^2 = %d$" % (xpm(-h), xpm(-k, "y"), r),
                      "$%s^2 + %s^2 = %d$" % (xpm(-h), xpm(-k, "y"), 2 * r)],
            "explanation": ("The standard form is $(x - h)^2 + (y - k)^2 = r^2$. With centre "
                            "$%s$ the signs INVERT inside the brackets, and the right side is "
                            "$%d^2 = %d$ — the radius squared, not the radius."
                            % (pt(h, k), r, r * r)),
            "check": ["Eq((%d - (%d))**2 + (%d - (%d))**2, %d)"
                      % (h + r, h, k, k, r * r)],
        })
    return raws


def _g_arc_length():
    raws = []
    grid = [(r, deg) for r in (3, 4, 6, 9, 12, 5, 10, 8)
            for deg in (30, 45, 60, 90, 120, 180)]
    for r, deg in grid:
        arc = Rational(deg, 360) * 2 * r        # coefficient of pi
        raws.append({
            "statement": ("A circle has radius $%d$. Find the length of an arc subtending a "
                          "central angle of $%d°$, as a multiple of $\\pi$." % (r, deg)),
            "correct": arc,
            "dvals": [Rational(deg, 360) * r * r, Rational(deg, 360) * r, Rational(2 * r)],
            "explanation": ("Arc length is the fraction $\\frac{%d}{360}$ of the whole "
                            "circumference $2\\pi r = %d\\pi$: $%s\\pi$. Using $\\pi r^2$ there "
                            "would give a sector AREA instead."
                            % (deg, 2 * r, fmt(arc))),
            "check": ["Eq(Rational(%d,360)*2*%d, Rational(%d,%d))"
                      % (deg, r, arc.p, arc.q)],
        })
    return raws


def _g_tangent_radius():
    raws = []
    # both leg assignments: radius short/tangent long and the reverse. They are
    # genuinely different questions, not the same one relabelled.
    for a, b, c in _TRIP + [(b0, a0, c0) for a0, b0, c0 in _TRIP]:
        pts_ = [P("O", 0, 0, "O"), P("T", a / 2.0, 0, "T"), P("P", a / 2.0, b / 2.0, "P")]
        fig = figure(pts_, [seg("O", "T"), seg("T", "P"), seg("O", "P"),
                            {"kind": "angle", "at": "T", "from": "O", "to": "P", "right": True}])
        raws.append({
            "statement": ("$PT$ is tangent to a circle of centre $O$ at $T$. If the radius "
                          "$OT = %d$ and the tangent length $PT = %d$, find $OP$." % (a, b)),
            "correct": c,
            "dvals": [a + b, b - a, a * b],
            "explanation": ("A tangent meets the radius at the point of contact at $90°$, so "
                            "$\\triangle OTP$ is right-angled at $T$: "
                            "$OP = \\sqrt{%d^2 + %d^2} = %d$. That right angle is the whole "
                            "reason Pythagoras applies here." % (a, b, c)),
            "check": ["Eq(%d**2 + %d**2, %d**2)" % (a, b, c)],
            "geoFigure": fig,
        })
    return raws


# ===========================================================================
# Unit 8 — Probability
# ===========================================================================

def _g_basic_probability():
    raws = []
    for tot, fav in [(52, 13), (52, 4), (36, 6), (20, 5), (30, 12), (24, 8), (50, 15),
                     (40, 10), (60, 18), (25, 5), (48, 16), (100, 35)]:
        p = Rational(fav, tot)
        raws.append({
            "statement": ("A box holds $%d$ items, of which $%d$ are red. One is drawn at "
                          "random. Find $P(\\text{red})$." % (tot, fav)),
            "correct": p,
            "dvals": [Rational(tot, fav), Rational(fav, tot - fav), 1 - p],
            "explanation": ("Probability is favourable over total: $\\frac{%d}{%d} = %s$. "
                            "Dividing by the NON-red count gives odds, not probability, and "
                            "$%s$ is the complement." % (fav, tot, fmt(p), fmt(1 - p))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (fav, tot, p.p, p.q)],
        })
        raws.append({
            "statement": ("A box holds $%d$ items, of which $%d$ are red. Find "
                          "$P(\\text{not red})$." % (tot, fav)),
            "correct": 1 - p,
            "dvals": [p, Rational(tot, tot - fav), -p],
            "explanation": ("The complement rule: $P(\\text{not red}) = 1 - %s = %s$. "
                            "Equivalently $\\frac{%d}{%d}$ — the non-red count over the total."
                            % (fmt(p), fmt(1 - p), tot - fav, tot)),
            "check": ["Eq(1 - Rational(%d,%d), Rational(%d,%d))"
                      % (fav, tot, (1 - p).p, (1 - p).q)],
        })
    return raws


def _g_union_conditional():
    raws = []
    tables = [(30, 20, 10, 40), (25, 15, 35, 25), (18, 12, 22, 48), (40, 10, 20, 30),
              (16, 24, 32, 8), (45, 15, 25, 15), (12, 28, 36, 24), (50, 30, 10, 10),
              (21, 9, 27, 43), (14, 26, 30, 30), (36, 24, 12, 28), (20, 40, 25, 15)]
    for a, b, c, d in tables:
        tot = a + b + c + d
        pa = Rational(a + b, tot)        # P(group 1)
        pb = Rational(a + c, tot)        # P(yes)
        pab = Rational(a, tot)           # P(both)
        union = pa + pb - pab
        cond = Rational(a, a + c)        # P(group 1 | yes)
        tbl = ("In a survey — Group 1: $%d$ yes, $%d$ no; Group 2: $%d$ yes, $%d$ no."
               % (a, b, c, d))
        raws.append({
            "statement": "%s Find $P(\\text{Group 1 OR yes})$." % tbl,
            "correct": union,
            "dvals": [pa + pb, pab, pa * pb],
            "explanation": ("The addition rule subtracts the overlap so it is not counted "
                            "twice: $%s + %s - %s = %s$. Adding without subtracting "
                            "double-counts the $%d$ people who are both."
                            % (fmt(pa), fmt(pb), fmt(pab), fmt(union), a)),
            "check": ["Eq(Rational(%d,%d) + Rational(%d,%d) - Rational(%d,%d), Rational(%d,%d))"
                      % (pa.p, pa.q, pb.p, pb.q, pab.p, pab.q, union.p, union.q)],
        })
        raws.append({
            "statement": "%s Find $P(\\text{Group 1} \\mid \\text{yes})$." % tbl,
            "correct": cond,
            "dvals": [pab, Rational(a, a + b), pa],
            "explanation": ("Conditioning on 'yes' RESTRICTS the sample space to the $%d$ yes "
                            "answers, of which $%d$ are Group 1: $\\frac{%d}{%d} = %s$. Using "
                            "the grand total instead gives the joint probability $%s$."
                            % (a + c, a, a, a + c, fmt(cond), fmt(pab))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (a, a + c, cond.p, cond.q)],
        })
        indep = pab == pa * pb
        raws.append({
            "statement": "%s Are 'Group 1' and 'yes' independent?" % tbl,
            "correct": "yes — $P(A \\cap B) = P(A)P(B)$" if indep
                       else "no — $P(A \\cap B) \\ne P(A)P(B)$",
            "dvals": (["no — $P(A \\cap B) \\ne P(A)P(B)$",
                       "independence cannot be decided from a table",
                       "yes — because the groups are separate"] if indep else
                      ["yes — $P(A \\cap B) = P(A)P(B)$",
                       "independence cannot be decided from a table",
                       "no — because the groups are separate"]),
            "explanation": ("Test the definition: $P(A \\cap B) = %s$ while "
                            "$P(A)P(B) = %s \\times %s = %s$. They %s, so the events are %s."
                            % (fmt(pab), fmt(pa), fmt(pb), fmt(pa * pb),
                               "match" if indep else "differ",
                               "independent" if indep else "dependent")),
            "check": ["%s(Rational(%d,%d), Rational(%d,%d))"
                      % ("Eq" if indep else "Ne", pab.p, pab.q,
                         (pa * pb).p, (pa * pb).q)],
        })
    return raws


def _g_multiplication_rule():
    raws = []
    for tot, r in [(10, 4), (12, 5), (8, 3), (15, 6), (20, 8), (9, 4), (14, 6), (18, 7),
                   (11, 5), (16, 7), (13, 5), (25, 10)]:
        with_rep = Rational(r, tot) * Rational(r, tot)
        without = Rational(r, tot) * Rational(r - 1, tot - 1)
        raws.append({
            "statement": ("A bag has $%d$ balls, $%d$ red. Two are drawn WITH replacement. Find "
                          "$P(\\text{both red})$." % (tot, r)),
            "correct": with_rep,
            "dvals": [without, Rational(r, tot), Rational(2 * r, tot)],
            "explanation": ("Replacement leaves the bag unchanged, so the draws are independent "
                            "and the probabilities simply multiply: "
                            "$\\frac{%d}{%d} \\times \\frac{%d}{%d} = %s$."
                            % (r, tot, r, tot, fmt(with_rep))),
            "check": ["Eq(Rational(%d,%d)*Rational(%d,%d), Rational(%d,%d))"
                      % (r, tot, r, tot, with_rep.p, with_rep.q)],
        })
        raws.append({
            "statement": ("A bag has $%d$ balls, $%d$ red. Two are drawn WITHOUT replacement. "
                          "Find $P(\\text{both red})$." % (tot, r)),
            "correct": without,
            "dvals": [with_rep, Rational(r, tot), Rational(r - 1, tot - 1)],
            "explanation": ("The first draw removes a red ball AND shrinks the bag, so the "
                            "second probability is $\\frac{%d}{%d}$: "
                            "$\\frac{%d}{%d} \\times \\frac{%d}{%d} = %s$. Using $\\frac{%d}{%d}$ "
                            "twice would assume replacement."
                            % (r - 1, tot - 1, r, tot, r - 1, tot - 1, fmt(without), r, tot)),
            "check": ["Eq(Rational(%d,%d)*Rational(%d,%d), Rational(%d,%d))"
                      % (r, tot, r - 1, tot - 1, without.p, without.q)],
        })
    return raws


def _g_sample_space():
    raws = []
    # size of a compound sample space, and a probability read off it
    combos = [("a coin and a six-sided die", 2, 6), ("two six-sided dice", 6, 6),
              ("a coin and a spinner with $4$ equal sectors", 2, 4),
              ("a spinner with $3$ sectors and a six-sided die", 3, 6),
              ("two spinners with $5$ sectors each", 5, 5),
              ("a coin and a card drawn from $13$ hearts", 2, 13),
              ("a four-sided die and a six-sided die", 4, 6),
              ("three coins", 2, 4), ("a spinner with $8$ sectors and a coin", 8, 2),
              ("two four-sided dice", 4, 4), ("a six-sided die and a spinner with $10$ sectors", 6, 10),
              ("a spinner with $7$ sectors and a four-sided die", 7, 4),
              ("a coin and a spinner with $12$ sectors", 2, 12),
              ("a five-sided spinner and a six-sided die", 5, 6),
              ("two eight-sided dice", 8, 8),
              ("a three-sided spinner and a coin", 3, 2)]
    for desc, m, n in combos:
        tot = m * n
        raws.append({
            "statement": "How many equally likely outcomes are there when you use %s?" % desc,
            "correct": tot,
            "dvals": [m + n, tot + 1, max(m, n)],
            "explanation": ("Each of the $%d$ outcomes of the first can pair with each of the "
                            "$%d$ of the second, so the counting principle MULTIPLIES: "
                            "$%d \\times %d = %d$. Adding would count the two experiments as "
                            "alternatives rather than as a pair." % (m, n, m, n, tot)),
            "check": ["Eq(%d*%d, %d)" % (m, n, tot)],
        })
    # dice sums — a genuinely different question shape on the same unit
    for target, ways in [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6),
                         (8, 5), (9, 4), (10, 3), (11, 2), (12, 1)]:
        p = Rational(ways, 36)
        raws.append({
            "statement": ("Two fair six-sided dice are rolled. Find $P(\\text{sum} = %d)$." % target),
            "correct": p,
            # "all 11 sums equally likely"; off-by-one count; wrong denominator
            "dvals": [Rational(ways, 11), Rational(ways + 1, 36), Rational(ways, 6)],
            "explanation": ("There are $36$ equally likely ordered outcomes, and $%d$ of them "
                            "sum to $%d$, so $P = \\frac{%d}{36} = %s$. Treating the $11$ "
                            "possible sums as equally likely is the classic error — they are "
                            "not." % (ways, target, ways, fmt(p))),
            "check": ["Eq(Rational(%d,36), Rational(%d,%d))" % (ways, p.p, p.q)],
        })
    return raws


# ===========================================================================
# Batch 2 — the forms that take every Integrated 2 unit to six collections.
# ===========================================================================

def _g_radical_equation():
    raws = []
    for b in range(2, 10):
        for a in (-9, -4, -1, 0, 3, 7, 11):
            x = b * b - a
            if x <= 0:
                continue
            raws.append({
                "statement": ("Solve $\\sqrt{%s} = %d$."
                              % (lin(1, a), b)),
                "correct": x,
                "dvals": [b * b + a, b - a, 2 * b - a],
                "explanation": ("Square both sides to undo the root: "
                                "$%s = %d$, so $x = %d$. Check it: "
                                "$\\sqrt{%d} = %d$. Squaring can invent "
                                "solutions, so the check is part of the "
                                "method, not politeness."
                                % (lin(1, a), b * b, x, x + a, b)),
                "check": ["Eq(sqrt(%d + (%d)), %d)" % (x, a, b),
                          "Eq(%d - (%d), %d)" % (b * b, a, x)],
            })
    return raws


def _g_perfect_square_trinomial():
    raws = []
    for k in range(1, 13):
        for s in (1, -1):
            b = 2 * k * s
            raws.append({
                "statement": ("Factor completely: $%s$." % quad(1, b, k * k)),
                "correct": "$(%s)^2$" % lin(1, k * s),
                "dvals": ["$(%s)^2$" % lin(1, -k * s),
                          "$(%s)(%s)$" % (xpm(k * s), xpm(-k * s)),
                          "$(%s)(%s)$" % (xpm(k * s), xpm(2 * k * s))],
                "explanation": ("The constant $%d$ is $%d^2$ and the middle "
                                "coefficient $%d$ is $2 \\cdot %d$, which is "
                                "exactly the perfect-square pattern "
                                "$x^2 + 2kx + k^2 = (x + k)^2$. Here "
                                "$k = %d$. The difference-of-squares "
                                "factoring would leave no middle term at all."
                                % (k * k, k, b, k * s, k * s)),
                "check": ["Eq(expand((x + (%d))**2), x**2 + (%d)*x + %d)"
                          % (k * s, b, k * k)],
            })
    return raws


def _g_polynomial_degree():
    raws = []
    for m in range(1, 10):
        for n in range(1, 10):
            if m == n:
                continue
            raws.append({
                "statement": ("What is the degree of the product "
                              "$(3x^{%d} + 1)(2x^{%d} - 5)$?" % (m, n)),
                "correct": m + n,
                "dvals": [max(m, n), m * n, abs(m - n) + 1],
                "explanation": ("Multiplying powers of $x$ ADDS their "
                                "exponents, so the leading term is "
                                "$3 \\cdot 2 \\cdot x^{%d + %d} = 6x^{%d}$ "
                                "and the degree is $%d$. Taking the larger "
                                "degree is what happens when you ADD two "
                                "polynomials, not multiply them."
                                % (m, n, m + n, m + n)),
                "check": ["Eq(degree(expand((3*x**%d + 1)*(2*x**%d - 5)), x),"
                          " %d)" % (m, n, m + n)],
            })
    return raws


def _g_vertex_by_completing():
    raws = []
    for h in range(-6, 7):
        for k in (-8, -3, 2, 5, 9):
            if h == 0:
                continue
            b, c = -2 * h, h * h + k
            raws.append({
                "statement": ("Complete the square to find the vertex of "
                              "$y = %s$, and give the $y$-coordinate of "
                              "that vertex." % quad(1, b, c)),
                "correct": k,
                "dvals": [h, c, -k],
                "explanation": ("Half of $%d$ is $%d$, and $%d^2 = %d$, so "
                                "$y = (%s)^2 %s %d$. The vertex is "
                                "$(%d,\\ %d)$, so the $y$-coordinate asked "
                                "for is $%d$. The $x$-coordinate is $%d$ — "
                                "the two are easy to swap once the bracket "
                                "is written."
                                % (b, -h, -h, h * h, lin(1, -h),
                                   sgn(k), abs(k), h, k, k, h)),
                "check": ["Eq(expand((x - (%d))**2 + (%d)), x**2 + (%d)*x"
                          " + (%d))" % (h, k, b, c)],
            })
    return raws


def _g_quadratic_from_roots():
    raws = []
    for r in range(-6, 7):
        for s2 in range(-6, 7):
            if r >= s2:
                continue
            b, c = -(r + s2), r * s2
            raws.append({
                "statement": ("Write a monic quadratic whose roots are $%d$ "
                              "and $%d$." % (r, s2)),
                "correct": "$%s$" % quad(1, b, c),
                # -b is the sum itself, so "forgot the sign change" and
                # "wrote the sum where the product goes" must not both be
                # spelled quad(1, r + s2, c) — the second swaps the two.
                "dvals": ["$%s$" % quad(1, -b, c),
                          "$%s$" % quad(1, b, -c),
                          "$%s$" % quad(1, c, b)],
                "explanation": ("$(x - %d)(x - %d)$ expands to $%s$: the "
                                "coefficient of $x$ is MINUS the sum of the "
                                "roots and the constant is their product. "
                                "Copying the sum without the sign change is "
                                "the standard slip."
                                % (r, s2, quad(1, b, c))),
                "check": ["Eq(expand((x - (%d))*(x - (%d))), x**2 + (%d)*x"
                          " + (%d))" % (r, s2, b, c)],
            })
    return raws


def _g_similar_perimeter():
    raws = []
    for j in range(2, 8):
        for P in (12, 18, 24, 30, 36, 42, 48, 60):
            raws.append({
                "statement": ("Two similar polygons have corresponding sides "
                              "in the ratio $1 : %d$. The smaller has "
                              "perimeter $%d$. Find the perimeter of the "
                              "larger." % (j, P)),
                "correct": P * j,
                "dvals": [P * j * j, P + j, Rational(P, j)],
                "explanation": ("Perimeter is a LENGTH, so it scales by the "
                                "plain ratio, not its square: "
                                "$%d \\times %d = %d$. The $%d$ option "
                                "scales it like an area, which is what the "
                                "square of the ratio is for."
                                % (P, j, P * j, P * j * j)),
                "check": ["Eq(%d*%d, %d)" % (P, j, P * j)],
            })
    return raws


def _g_similar_side():
    raws = []
    for k in range(2, 7):
        for a in (3, 4, 5, 6, 7, 8, 9, 10):
            for b in (2, 5):
                raws.append({
                    "statement": ("$\\triangle ABC \\sim \\triangle DEF$ "
                                  "with $AB = %d$ and $DE = %d$. If "
                                  "$BC = %d$, find $EF$."
                                  % (a, a * k, b * k)),
                    "correct": b * k * k,
                    "dvals": [b * k, b + a * (k - 1), Rational(b, k)],
                    "explanation": ("One multiplier serves the whole "
                                    "triangle: $DE = %d$ is $%d$ times "
                                    "$AB = %d$, so every side scales by "
                                    "$%d$ and $EF = %d \\times %d = %d$. "
                                    "Adding the difference instead of "
                                    "multiplying by the ratio is the error "
                                    "similarity is built to expose."
                                    % (a * k, k, a, k, b * k, k, b * k * k)),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (a * k, a, b * k * k, b * k)],
                })
    return raws


def _g_trig_ratio_value():
    raws = []
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (7, 24, 25),
               (9, 12, 15), (20, 21, 29), (12, 16, 20), (10, 24, 26),
               (9, 40, 41), (15, 20, 25), (12, 35, 37)]
    for (o, a, h) in triples:
        for fn, val, why in (("sin", Rational(o, h), "opposite over "
                              "hypotenuse"),
                             ("cos", Rational(a, h), "adjacent over "
                              "hypotenuse"),
                             ("tan", Rational(o, a), "opposite over "
                              "adjacent")):
            raws.append({
                "statement": ("A right triangle has legs $%d$ and $%d$ and "
                              "hypotenuse $%d$. The angle $\\theta$ is "
                              "opposite the leg of length $%d$. Find "
                              "$\\%s\\theta$." % (o, a, h, o, fn)),
                "correct": val,
                "dvals": [Rational(a, o) if fn == "tan" else
                          Rational(h, o if fn == "sin" else a),
                          Rational(o, a) if fn != "tan" else Rational(o, h),
                          Rational(a, h) if fn != "cos" else Rational(o, h)],
                "explanation": ("$\\%s$ is %s. With $\\theta$ opposite the "
                                "leg $%d$, that is $\\frac{%d}{%d} = %s$. "
                                "Naming the sides RELATIVE TO THE ANGLE "
                                "before dividing is the whole discipline "
                                "here." % (fn, why, o,
                                           val.p, val.q, fmt(val))),
                "check": ["Eq(%d**2 + %d**2, %d**2)" % (o, a, h),
                          "Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (val.p, val.q, val.p, val.q)],
            })
    return raws


def _g_expected_value():
    raws = []
    for w in range(2, 10):
        for l in range(1, 9):
            for n in (4, 5, 6, 8, 10):
                p = Rational(1, n)
                ev = p * w - (1 - p) * l
                raws.append({
                    "statement": ("A game pays $%d$ with probability "
                                  "$\\frac{1}{%d}$ and costs you $%d$ "
                                  "otherwise. Find the expected gain per "
                                  "play." % (w, n, l)),
                    "correct": ev,
                    "dvals": [p * w + (1 - p) * l, w - l, p * (w - l)],
                    "explanation": ("Weight each outcome by its probability "
                                    "and add, with the loss counted as "
                                    "negative: $\\frac{1}{%d}(%d) - "
                                    "\\frac{%d}{%d}(%d) = %s$. Adding the "
                                    "loss instead of subtracting it turns a "
                                    "cost into a reward."
                                    % (n, w, n - 1, n, l, fmt(ev))),
                    "check": ["Eq(Rational(1,%d)*%d - Rational(%d,%d)*%d,"
                              " Rational(%d,%d))"
                              % (n, w, n - 1, n, l, ev.p, ev.q)],
                })
    return raws


def _g_perm_vs_comb():
    from math import comb as _comb, perm as _perm
    raws = []
    for n in range(4, 12):
        for r in range(2, min(n, 5) + 1):
            raws.append({
                "statement": ("From $%d$ people, how many different ORDERED "
                              "line-ups of $%d$ can be formed?" % (n, r)),
                "correct": _perm(n, r),
                "dvals": [_comb(n, r), n * r, n ** r],
                "explanation": ("Order matters, so this is a permutation: "
                                "$%d \\times %d \\times \\ldots$ down $%d$ "
                                "factors $= %d$. The unordered count is "
                                "$%d$ — smaller by exactly $%d!$, the number "
                                "of ways to shuffle each chosen group."
                                % (n, n - 1, r, _perm(n, r), _comb(n, r), r)),
                "check": ["Eq(factorial(%d)/factorial(%d), %d)"
                          % (n, n - r, _perm(n, r))],
            })
            raws.append({
                "statement": ("From $%d$ people, how many different "
                              "committees of $%d$ can be chosen, where order "
                              "does not matter?" % (n, r)),
                "correct": _comb(n, r),
                "dvals": [_perm(n, r), n * r, n - r],
                "explanation": ("Order does not matter, so divide the "
                                "$%d$ ordered line-ups by the $%d! = %d$ "
                                "orderings of each committee: $%d$. Using "
                                "the permutation count here counts the same "
                                "committee many times over."
                                % (_perm(n, r), r,
                                   _perm(n, r) // _comb(n, r),
                                   _comb(n, r))),
                "check": ["Eq(binomial(%d, %d), %d)" % (n, r, _comb(n, r))],
            })
    return raws


def build():
    forms = _remapped_forms()

    U1 = "rational-exponents-and-radicals"
    forms += [
        form("im2-simplify-radical", "Simplifying radicals", 1, U1,
             "Pull out the largest perfect-square factor — anything less is not simplified.",
             mk_txt("im2-rad", _g_simplify_radical())),
        form("im2-rational-exponent", "Evaluating rational exponents", 1, U1,
             "Denominator is the root, numerator is the power.",
             mk_num("im2-rex", _g_rational_exponent())),
        form("im2-radical-arithmetic", "Adding and multiplying radicals", 2, U1,
             "Like radicals add like terms; multiplication combines under one root.",
             mk_txt("im2-rar", _g_radical_arithmetic())),
        form("im2-radical-equation", "Solving a radical equation", 2, U1,
             "Square both sides, then CHECK — squaring can invent solutions.",
             mk_num("im2-req", _g_radical_equation())),
        form("im2-rational-irrational", "Rational or irrational?", 2, U1,
             "A rational plus an irrational is always irrational — but a radical is not automatically irrational.",
             mk_txt("im2-rir", _g_rational_irrational())),
    ]

    U2 = "polynomials-and-factoring"
    forms += [
        form("im2-multiply-binomials", "Multiplying binomials", 1, U2,
             "The constant is the product of the two numbers; the middle coefficient is their sum.",
             mk_txt("im2-mb", _g_multiply_binomials())),
        form("im2-gcf-factor", "Factoring out the greatest common factor", 1, U2,
             "Take the numeric GCF and every shared variable — always the FIRST factoring step.",
             mk_txt("im2-gcf", _g_gcf_factor())),
        form("im2-factor-trinomial", "Factoring trinomials", 2, U2,
             "Two numbers multiplying to c and adding to b — multiplication read backwards.",
             mk_txt("im2-ft", _g_factor_trinomial())),
        form("im2-difference-squares", "The difference of two squares", 2, U2,
             "a² - b² = (a - b)(a + b); a repeated bracket would create a middle term.",
             mk_txt("im2-ds", _g_difference_squares())),
        form("im2-perfect-square-trinomial", "Perfect-square trinomials", 2, U2,
             "Constant a perfect square and middle term twice its root — that is the pattern.",
             mk_txt("im2-pst", _g_perfect_square_trinomial())),
        form("im2-polynomial-degree", "The degree of a product", 1, U2,
             "Multiplying powers ADDS exponents; adding polynomials keeps the larger degree.",
             mk_num("im2-deg", _g_polynomial_degree())),
    ]

    U3 = "quadratic-functions"
    forms += [
        form("im2-axis-vertex", "The axis of symmetry and the vertex", 2, U3,
             "x = -b/2a, minus included; substitute back for the y-coordinate.",
             mk_num("im2-av", _g_axis_vertex())),
        form("im2-which-form", "Which form reveals which feature", 1, U3,
             "Standard shows the intercept, factored shows the roots, vertex form shows the vertex.",
             mk_txt("im2-wf", _g_which_form())),
        form("im2-vertex-by-completing", "Completing the square for the vertex", 2, U3,
             "Half the middle coefficient, squared — the leftover is the vertex height.",
             mk_num("im2-vcs", _g_vertex_by_completing())),
        form("im2-quadratic-from-roots", "Building a quadratic from its roots", 2, U3,
             "Minus the sum for the x-coefficient, the product for the constant.",
             mk_txt("im2-qfr", _g_quadratic_from_roots())),
    ]

    U4 = "solving-quadratic-equations"
    forms += [
        form("im2-quadratic-formula", "Solving with the quadratic formula", 2, U4,
             "Compute the discriminant first, then read both roots off the formula.",
             mk_num("im2-qf", _g_quadratic_formula())),
        form("im2-complex-roots", "When the discriminant goes negative", 3, U4,
             "b² - 4ac < 0 means no real roots — and a parabola that misses the axis entirely.",
             mk_txt("im2-cx", _g_complex_roots())),
    ]

    U5 = "similarity-and-dilations"
    forms += [
        form("im2-dilation", "Dilating a point about the origin", 1, U5,
             "Multiply both coordinates by the scale factor — adding it would be a translation.",
             mk_txt("im2-dil", _g_dilation())),
        form("im2-scale-factor", "Length ratio against area ratio", 2, U5,
             "Areas scale by the SQUARE of the length ratio.",
             mk_num("im2-sf", _g_scale_factor())),
        form("im2-side-splitter", "The side-splitter theorem", 2, U5,
             "A line parallel to one side cuts the other two proportionally.",
             mk_num("im2-ss", _g_side_splitter())),
        form("im2-similar-perimeter", "Perimeters of similar figures", 1, U5,
             "Perimeter is a length, so it scales by the plain ratio — never its square.",
             mk_num("im2-sper", _g_similar_perimeter())),
        form("im2-similar-side", "A missing side in similar triangles", 1, U5,
             "One multiplier serves the whole triangle.",
             mk_num("im2-sside", _g_similar_side())),
    ]

    U6 = "right-triangle-trigonometry"
    forms += [
        form("im2-pick-ratio", "Choosing the right trig ratio", 1, U6,
             "SOH-CAH-TOA: name the sides relative to the angle BEFORE dividing.",
             mk_num("im2-pr", _g_pick_ratio())),
        form("im2-complementary", "Complementary angles in a right triangle", 2, U6,
             "sin θ = cos(90° - θ), because one angle's opposite is the other's adjacent.",
             mk_txt("im2-comp", _g_complementary())),
        form("im2-trig-ratio-value", "Reading a trig ratio off the sides", 1, U6,
             "Name the sides relative to the angle, then divide.",
             mk_num("im2-trv", _g_trig_ratio_value())),
    ]

    U7 = "circles"
    forms += [
        form("im2-inscribed-angle", "Central and inscribed angles", 1, U7,
             "An inscribed angle is half the central angle on the same arc.",
             mk_num("im2-ia", _g_inscribed_angle())),
        form("im2-arc-length", "Arc length as a fraction of the circumference", 2, U7,
             "The angle's share of 360° times 2πr — not πr², which is area.",
             mk_num("im2-arc", _g_arc_length())),
        form("im2-tangent-radius", "Tangent meets radius at a right angle", 2, U7,
             "That right angle is what lets Pythagoras into a circle problem.",
             mk_num("im2-tan", _g_tangent_radius())),
        form("im2-circle-equation", "The equation of a circle", 2, U7,
             "(x - h)² + (y - k)² = r²: signs invert inside, and the right side is r SQUARED.",
             mk_txt("im2-ceq", _g_circle_equation())),
    ]

    U8 = "probability"
    forms += [
        form("im2-basic-probability", "Probability and its complement", 1, U8,
             "Favourable over total; the complement is 1 minus the probability.",
             mk_num("im2-bp", _g_basic_probability())),
        form("im2-union-conditional", "Unions, conditionals and independence", 2, U8,
             "Add and subtract the overlap; conditioning restricts the sample space.",
             mk_txt("im2-uc", _g_union_conditional())),
        form("im2-sample-space", "Counting the sample space", 1, U8,
             "The counting principle multiplies; not every visible total is equally likely.",
             mk_num("im2-ss2", _g_sample_space())),
        form("im2-multiplication-rule", "With and without replacement", 2, U8,
             "Without replacement, the second draw sees a smaller bag.",
             mk_num("im2-mr", _g_multiplication_rule())),
        form("im2-expected-value", "Expected gain per play", 2, U8,
             "Weight each outcome by its probability, counting a cost as negative.",
             mk_num("im2-ev", _g_expected_value())),
        form("im2-perm-vs-comb", "Ordered line-ups against committees", 2, U8,
             "Order matters or it does not — the factor between them is r!.",
             mk_num("im2-pvc", _g_perm_vs_comb())),
    ]

    # -----------------------------------------------------------------
    # Second half of every unit, plus the whole of Unit 8 (Geometric
    # Measurement & Modelling), which is new to the course. Six of the
    # eight original units stopped at Level 2, so the level filter on
    # the unit page offered a tier with nothing behind it.
    # Generators in scripts/pb/integrated_2_more.py.
    # -----------------------------------------------------------------
    U1 = "rational-exponents-and-radicals"
    U2 = "polynomials-and-factoring"
    U3 = "quadratic-functions"
    U4 = "solving-quadratic-equations"
    U5 = "similarity-and-dilations"
    U6 = "right-triangle-trigonometry"
    U7 = "circles"
    U8 = "geometric-measurement-and-modelling"
    U9 = "probability"
    forms += [
        # --- Unit 1: rational exponents & radicals --------------------
        form("im2-negative-exponent", "Negative exponents", 1, U1,
             "A negative exponent is a reciprocal, never a negative number.",
             mk_num("im2-nex", more.g_negative_exponent())),
        form("im2-radical-to-exponent", "Radical into rational exponent", 2, U1,
             "The index becomes the denominator; the inner power the numerator.",
             mk_txt("im2-r2e", more.g_radical_to_exponent())),
        form("im2-rationalise", "Clearing a radical from the bottom", 2, U1,
             "Multiply top and bottom by the radical — that is multiplying by 1.",
             mk_txt("im2-rat", more.g_rationalise_denominator())),
        form("im2-power-of-power", "A perfect power under a fractional exponent", 3, U1,
             "Rewrite the base as a power first; then the exponents cancel.",
             mk_num("im2-pop", more.g_simplify_power_of_power())),
        form("im2-extraneous-root", "The root that does not check out", 3, U1,
             "Squaring can make a false statement true — so every root gets tested.",
             mk_txt("im2-ext", more.g_radical_extraneous())),
        form("im2-irrational-combination", "Forced to be irrational", 3, U1,
             "Rational plus irrational cannot be rational — and the proof is one line.",
             mk_txt("im2-irc", more.g_irrational_combination())),

        # --- Unit 2: polynomials & factoring --------------------------
        form("im2-add-polynomials", "Adding and subtracting polynomials", 1, U2,
             "The minus sign distributes over EVERY term in the bracket.",
             mk_txt("im2-adp", more.g_add_polynomials())),
        form("im2-factor-grouping", "Factoring by grouping", 2, U2,
             "Split the middle term into two whose product is ac and sum is b.",
             mk_txt("im2-fgr", more.g_factor_by_grouping())),
        form("im2-factor-a-not-one", "A leading coefficient that will not go quietly", 2, U2,
             "Both brackets cannot start with x — decide which carries the coefficient.",
             mk_txt("im2-fa1", more.g_factor_a_not_one())),
        form("im2-factor-completely", "Common factor FIRST", 3, U2,
             "Take out the common factor, then look again — 'completely' means completely.",
             mk_txt("im2-fcm", more.g_factor_completely())),
        form("im2-polynomial-identity", "Identities and expansions", 3, U2,
             "The middle coefficients of a cube count the ways to choose a bracket.",
             mk_txt("im2-pid", more.g_polynomial_identity())),
        form("im2-polynomial-closure", "Which operation leaves the system", 3, U2,
             "Polynomials are closed under +, - and x, but not under division.",
             mk_txt("im2-pcl", more.g_polynomial_closure())),

        # --- Unit 3: quadratic functions ------------------------------
        form("im2-quad-y-intercept", "The y-intercept of a parabola", 1, U3,
             "Setting x = 0 leaves the constant term, and nothing else.",
             mk_txt("im2-qyi", more.g_quad_y_intercept())),
        form("im2-parabola-direction", "Which way it opens", 1, U3,
             "Only the leading coefficient decides up or down, maximum or minimum.",
             mk_txt("im2-pdi", more.g_parabola_direction())),
        form("im2-transform-parabola", "Naming the transformation", 2, U3,
             "The sign inside the bracket is reversed; the one outside is not.",
             mk_txt("im2-tpb", more.g_transform_parabola())),
        form("im2-max-height", "The greatest height", 3, U3,
             "The vertex is the maximum — and the question asks how high, not when.",
             mk_num("im2-mxh", more.g_max_height_word())),
        form("im2-average-rate", "Average rate of change", 3, U3,
             "The slope of the joining line — different on every interval.",
             mk_num("im2-avr", more.g_average_rate_quad())),
        form("im2-compare-growth", "Quadratic against exponential", 3, U3,
             "Exponential wins eventually, whatever head start the polynomial has.",
             mk_txt("im2-cgr", more.g_compare_growth())),

        # --- Unit 4: solving quadratic equations ----------------------
        form("im2-square-root-method", "Taking the square root", 1, U4,
             "Both signs, always — the plus-or-minus is half the answer.",
             mk_txt("im2-srm", more.g_square_root_method())),
        form("im2-zero-product", "The zero-product property", 1, U4,
             "A product is zero exactly when one factor is.",
             mk_txt("im2-zpr", more.g_zero_product())),
        form("im2-factor-solve", "Solving by factoring", 1, U4,
             "Two numbers multiplying to c and adding to b — then flip their signs.",
             mk_txt("im2-fsv", more.g_factor_solve_simple())),
        form("im2-complete-square-solve", "Completing the square to the roots", 2, U4,
             "Half the middle coefficient, squared — then un-square with both signs.",
             mk_txt("im2-css", more.g_complete_square_solve())),
        form("im2-linear-quadratic", "Where a line meets a parabola", 2, U4,
             "Substitute the line into the curve; one quadratic in x is left.",
             mk_txt("im2-lqs", more.g_linear_quadratic_system())),
        form("im2-quadratic-word", "Building the equation first", 3, U4,
             "Set up, solve, then throw away the root the situation forbids.",
             mk_num("im2-qwd", more.g_quadratic_word_setup())),

        # --- Unit 5: similarity & dilations ---------------------------
        form("im2-scale-from-sides", "The scale factor, in one division", 1, U5,
             "Image over original — and the direction is part of the answer.",
             mk_num("im2-sfs", more.g_scale_factor_from_sides())),
        form("im2-similar-area-ratio", "Areas of similar figures", 2, U5,
             "Lengths scale by k, areas by k squared.",
             mk_num("im2-sar", more.g_similar_area_ratio())),
        form("im2-aa-criterion", "Why they are similar", 2, U5,
             "Two matching angles is already enough — the third is forced.",
             mk_txt("im2-aac", more.g_aa_criterion())),
        form("im2-indirect-measurement", "Measuring what you cannot reach", 3, U5,
             "Same sun angle, similar triangles, one proportion.",
             mk_num("im2-idm", more.g_indirect_measurement())),
        form("im2-dilation-composition", "Two dilations in a row", 3, U5,
             "Scale factors MULTIPLY; they never add.",
             mk_num("im2-dcp", more.g_dilation_composition())),
        form("im2-similar-volume", "Volumes of similar solids", 3, U5,
             "The exponent matches the dimension: lengths k, areas k squared, volumes k cubed.",
             mk_num("im2-svl", more.g_similar_volume())),

        # --- Unit 6: right-triangle trigonometry ----------------------
        form("im2-find-angle-inverse", "Which inverse ratio", 1, U6,
             "Name the two sides you were given; that names the ratio.",
             mk_txt("im2-fai", more.g_find_angle_inverse())),
        form("im2-missing-leg", "Pythagoras, backwards to a leg", 2, U6,
             "The SQUARES subtract — never the lengths themselves.",
             mk_num("im2-mlg", more.g_missing_leg())),
        form("im2-exact-angle-side", "A side from an exact-value angle", 2, U6,
             "30, 45 and 60 degrees need no calculator at all.",
             mk_txt("im2-eas", more.g_solve_right_triangle_side())),
        form("im2-angle-elevation", "Angles of elevation", 2, U6,
             "The slope length is the hypotenuse; the height is opposite the angle.",
             mk_num("im2-ael", more.g_angle_elevation())),
        form("im2-trig-from-one", "One ratio gives the others", 3, U6,
             "Recover the third side with Pythagoras, then read off any ratio.",
             mk_num("im2-tfo", more.g_trig_from_one_ratio())),
        form("im2-two-step-trig", "Two triangles, one answer", 3, U6,
             "Find which triangle actually carries the quantity you were asked for.",
             mk_num("im2-tst", more.g_two_step_trig())),

        # --- Unit 7: circles ------------------------------------------
        form("im2-radius-diameter", "Circumference and area", 1, U7,
             "Circumference is linear in r; area is quadratic. Different units, different formulas.",
             mk_txt("im2-rdm", more.g_radius_diameter())),
        form("im2-arc-central", "Central against inscribed", 1, U7,
             "A central angle EQUALS its arc; an inscribed angle halves it.",
             mk_num("im2-arcm", more.g_arc_measure_central())),
        form("im2-cyclic-quad", "Cyclic quadrilaterals", 2, U7,
             "Opposite angles are supplementary, because the two arcs make a full circle.",
             mk_num("im2-cyq", more.g_cyclic_quadrilateral())),
        form("im2-circle-complete-square", "Completing the square twice", 3, U7,
             "Group x with x and y with y — and the right-hand side is r SQUARED.",
             mk_num("im2-ccs", more.g_circle_complete_square())),
        form("im2-two-chords", "Two chords crossing", 3, U7,
             "The PRODUCTS of the pieces are equal — it is not a sum rule.",
             mk_num("im2-2ch", more.g_two_chords())),
        form("im2-sector-backwards", "From sector area to angle", 3, U7,
             "The sector is the same fraction of the circle as the angle is of 360.",
             mk_num("im2-scb", more.g_sector_backwards())),

        # --- Unit 8: geometric measurement & modelling (all new) ------
        form("im2-prism-volume", "Volume of a prism", 1, U8,
             "Base area times height — and surface area is a different quantity.",
             mk_num("im2-pvl", more.g_prism_volume())),
        form("im2-cylinder-volume", "Volume of a cylinder", 1, U8,
             "The same statement as a prism, with a round base.",
             mk_txt("im2-cvl", more.g_cylinder_volume())),
        form("im2-cone-volume", "Volume of a cone", 1, U8,
             "Exactly one third of the cylinder that encloses it.",
             mk_txt("im2-kvl", more.g_cone_volume())),
        form("im2-sphere-volume", "Volume of a sphere", 1, U8,
             "Four thirds pi r CUBED — a solid, so the exponent is 3.",
             mk_txt("im2-svo", more.g_sphere_volume())),
        form("im2-solve-height", "Backwards to a height", 2, U8,
             "Knowing the volume turns the formula into an equation.",
             mk_num("im2-shg", more.g_solve_for_height())),
        form("im2-solve-radius", "Backwards to a radius", 2, U8,
             "A square root appears, and only the positive one is a length.",
             mk_num("im2-srd", more.g_solve_for_radius())),
        form("im2-surface-area-cylinder", "Surface area of a cylinder", 2, U8,
             "Two discs plus the side, unrolled into a rectangle.",
             mk_txt("im2-sac", more.g_surface_area_cylinder())),
        form("im2-capacity-units", "Cubic metres into litres", 2, U8,
             "One cubic metre is a thousand litres — the factor is not 100.",
             mk_num("im2-cpu", more.g_capacity_units())),
        form("im2-cross-section", "The shape of the cut face", 2, U8,
             "It depends on the cutting plane as much as on the solid.",
             mk_txt("im2-crs", more.g_cross_section())),
        form("im2-composite-solid", "Two solids joined", 3, U8,
             "Volumes add cleanly; decide add or subtract before reaching for a formula.",
             mk_txt("im2-cms", more.g_composite_solid())),
        form("im2-density", "Density, by area and by volume", 3, U8,
             "'Per' means divide, and the units say whether to use area or volume.",
             mk_num("im2-dns", more.g_density_problem())),
        form("im2-scaling-design", "Scaling a design up", 3, U8,
             "Capacity grows like k cubed while the material grows only like k squared.",
             mk_num("im2-scd", more.g_scaling_design())),

        # --- Unit 9: probability ---------------------------------------
        form("im2-prob-or-disjoint", "'Or' with no overlap", 1, U9,
             "Mutually exclusive events simply add.",
             mk_num("im2-por", more.g_prob_or_disjoint())),
        form("im2-two-way-read", "One cell of a two-way table", 1, U9,
             "Both conditions means one cell over the GRAND total.",
             mk_num("im2-twr", more.g_two_way_read())),
        form("im2-independence-test", "Testing independence", 2, U9,
             "Independence is a calculation: does P(both) equal the product?",
             mk_txt("im2-ind", more.g_independence_test())),
        form("im2-at-least-one", "At least one", 3, U9,
             "Count the opposite — every attempt failing — then subtract from 1.",
             mk_num("im2-alo", more.g_at_least_one())),
        form("im2-conditional-reverse", "Which condition names the denominator", 3, U9,
             "P(A given B) and P(B given A) are different questions with different answers.",
             mk_num("im2-cnr", more.g_conditional_reverse())),
        form("im2-tree-two-stage", "Two draws, without replacement", 3, U9,
             "The bag changes between draws, so both numbers move.",
             mk_num("im2-tts", more.g_tree_two_stage())),
    ]

    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    t = build()
    per = {u["id"]: 0 for u in t["units"]}
    for f in t["forms"]:
        per[f["unit"]] += len(f["variants"])
    print("%s: %d forms, %d variants" %
          (t["slug"], len(t["forms"]), sum(len(f["variants"]) for f in t["forms"])))
    for u in t["units"]:
        print("   %-40s %4d" % (u["id"], per[u["id"]]))
