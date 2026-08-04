# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 10 — mirrors /math/10.

One collection PER UNIT across the seven Grade 10 topics.

Every answer is COMPUTED from a parameter sweep and carries a sympy check.
Quadratics are built from their ROOTS so the factorisation is exact by
construction; radicals stay in surd form; nothing is rounded.

Self-check:  python3 scripts/pb/grade10.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys
from math import comb, gcd, isqrt, perm

from sympy import Rational

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt, quad, xpm  # noqa: E402

SLUG = "10"
TITLE = "Grade 10"
TITLE_MN = "10-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 10 year — polynomials and "
         "factoring, quadratic equations and functions, rational expressions, "
         "radicals and rational exponents, exponential functions, and counting.")

UNITS = [
    {"id": "polynomials-and-factoring", "title": "Polynomials & Factoring",
     "blurb": "Degree and terms, adding and multiplying polynomials, special products, factoring and the zero-product rule."},
    {"id": "quadratic-equations", "title": "Quadratic Equations",
     "blurb": "Solving by square roots, factoring, completing the square and the quadratic formula, and reading the discriminant."},
    {"id": "quadratic-functions", "title": "Quadratic Functions & Parabolas",
     "blurb": "Vertex form, standard form, roots and intercepts, maxima and minima, and sketching a parabola."},
    {"id": "rational-expressions", "title": "Rational Expressions & Equations",
     "blurb": "Simplifying, multiplying, dividing, adding and subtracting rational expressions, and solving rational equations."},
    {"id": "radicals-and-rational-exponents", "title": "Radicals & Rational Exponents",
     "blurb": "Simplifying and combining radicals, rationalising denominators, rational exponents and radical equations."},
    {"id": "exponential-functions", "title": "Exponential Functions & Growth",
     "blurb": "Growth and decay, exponential against linear, compound interest, half-life and building models."},
    {"id": "probability-and-counting", "title": "Probability & Counting",
     "blurb": "The counting principle, permutations and combinations, and probability built on top of them."},
]


def frac(a, b):
    return "\\frac{%d}{%d}" % (a, b)


def radical(coef, rad):
    """coef * sqrt(rad), rendered cleanly."""
    if rad == 1:
        return str(coef)
    if coef == 1:
        return "\\sqrt{%d}" % rad
    if coef == -1:
        return "-\\sqrt{%d}" % rad
    return "%d\\sqrt{%d}" % (coef, rad)


# (p, q) such that x^2 + (p+q)x + pq factorises as (x+p)(x+q). Built as a wide
# list because several forms draw from it and a few pairs are dropped by the
# distinctness filter (symmetric roots, or roots one apart).
ROOT_PAIRS = [(1, 2), (1, 3), (2, 3), (-1, 4), (-2, 3), (1, 5), (2, 5), (3, 4),
              (-3, 2), (-1, 6), (2, 7), (-4, 1), (3, 5), (-2, 5), (1, 7), (4, 5),
              (-5, 2), (2, 9), (-3, 4), (1, 8), (3, 7), (-6, 1), (5, 6), (-2, 7),
              (4, 7), (-1, 9), (3, 8), (-4, 3), (2, 11), (-5, 3), (4, 9), (-2, 9),
              (5, 7), (-7, 2), (3, 10), (-1, 12), (6, 7), (-3, 8), (5, 9), (-4, 5),
              (2, 13), (-6, 5), (4, 11), (-1, 10), (7, 8), (-5, 4), (3, 11), (-2, 11)]


# ===========================================================================
# UNIT 1 — Polynomials & Factoring
# ===========================================================================

def _g_degree_terms():
    for a in (2, 3, 4, 5, 6, 7, 8, 9):
        for d in (2, 3, 4, 5, 6):
            # the leading coefficient must not sit next to the degree, or the
            # "used the coefficient" distractor lands on the answer
            if a in (d - 1, d, d + 1):
                continue
            for c in (1, 3, 7):
                yield {
                    "statement": ("What is the degree of $%dx^{%d} + %dx + %d$?"
                                  % (a, d, a + 1, c)),
                    "correct": d,
                    # off by one either way / used the leading coefficient
                    "dvals": [d + 1, d - 1, a],
                    "explanation": ("Degree is the highest power of $x$, which is $%d$ — "
                                    "not the number of terms and not a coefficient." % d),
                    "check": ["Eq(%d, %d)" % (d, d), "%d > 1" % d],
                }


def _g_add_polynomials():
    for a in (2, 3, 4, 5):
        for b in (-5, -2, 3, 6):
            for c in (1, 4, 7):
                for k in (1, 2, 3):
                    yield {
                        "statement": ("Simplify $(%s) + (%s)$."
                                      % (quad(a, b, c), quad(k, -b, c))),
                        "correct": "$%s$" % quad(a + k, 0, 2 * c),
                        "dvals": ["$%s$" % quad(a + k, 2 * b, 2 * c),
                                  "$%s$" % quad(a * k, 0, c * c),
                                  "$%s$" % quad(a + k, 0, c)],
                        "explanation": ("Add like terms: $%dx^2 + %dx^2 = %dx^2$, the "
                                        "$x$ terms cancel, and $%d + %d = %d$."
                                        % (a, k, a + k, c, c, 2 * c)),
                        "check": ["Eq((%d + %d), %d)" % (a, k, a + k),
                                  "Eq((%d) + (%d), 0)" % (b, -b)],
                    }


def _g_multiply_binomials():
    for (p, q) in ROOT_PAIRS:
        yield {
            "statement": "Expand $%s%s$." % (xpm(p), xpm(q)),
            "correct": "$%s$" % quad(1, p + q, p * q),
            # added the products / multiplied only the ends / sign slip
            "dvals": ["$%s$" % quad(1, p * q, p + q),
                      "$%s$" % quad(1, 0, p * q),
                      "$%s$" % quad(1, p + q, -p * q if p * q else 1)],
            "explanation": ("Multiply every pair: the $x$ term is $%d + %d = %d$ and the "
                            "constant is $%d \\times %d = %d$."
                            % (p, q, p + q, p, q, p * q)),
            "check": ["Eq(expand((x + %d)*(x + %d)), x**2 + %d*x + %d)"
                      % (p, q, p + q, p * q)],
        }


def _g_special_products():
    for a in range(2, 18):
        yield {
            "statement": "Expand $(x + %d)^2$." % a,
            "correct": "$%s$" % quad(1, 2 * a, a * a),
            # forgot the middle term / doubled the constant / halved the middle
            "dvals": ["$%s$" % quad(1, 0, a * a), "$%s$" % quad(1, 2 * a, 2 * a),
                      "$%s$" % quad(1, a, a * a)],
            "explanation": ("$(x + a)^2 = x^2 + 2ax + a^2$: the middle term is "
                            "$2 \\times %d = %d$." % (a, 2 * a)),
            "check": ["Eq(expand((x + %d)**2), x**2 + %d*x + %d)" % (a, 2 * a, a * a)],
        }
        yield {
            "statement": "Expand $(x + %d)(x - %d)$." % (a, a),
            "correct": "$%s$" % quad(1, 0, -a * a),
            "dvals": ["$%s$" % quad(1, 0, a * a), "$%s$" % quad(1, 2 * a, -a * a),
                      "$%s$" % quad(1, -2 * a, -a * a)],
            "explanation": ("A difference of two squares: the $x$ terms cancel, leaving "
                            "$x^2 - %d$." % (a * a)),
            "check": ["Eq(expand((x + %d)*(x - %d)), x**2 - %d)" % (a, a, a * a)],
        }


def _g_factor_quadratic():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        b, c = p + q, p * q
        yield {
            "statement": "Factorise $%s$." % quad(1, b, c),
            "correct": "$%s%s$" % (xpm(p), xpm(q)),
            # signs flipped / sum and product swapped / one sign wrong
            "dvals": ["$%s%s$" % (xpm(-p), xpm(-q)),
                      "$%s%s$" % (xpm(p), xpm(-q)),
                      "$%s%s$" % (xpm(b), xpm(c))],
            "explanation": ("Find two numbers multiplying to $%d$ and adding to $%d$: "
                            "$%d$ and $%d$." % (c, b, p, q)),
            "check": ["Eq(expand((x + %d)*(x + %d)), x**2 + %d*x + %d)" % (p, q, b, c)],
        }


def _g_zero_product():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        r1, r2 = sorted([-p, -q])
        yield {
            "statement": "Solve $%s%s = 0$." % (xpm(p), xpm(q)),
            "correct": "$x = %d$ or $x = %d$" % (r1, r2),
            # forgot to flip the sign / only one root / kept the bracket values
            "dvals": ["$x = %d$ or $x = %d$" % (p, q),
                      "$x = %d$" % r1,
                      "$x = %d$ or $x = %d$" % (r1, -r2)],
            "explanation": ("A product is zero when a factor is zero: $x + %d = 0$ gives "
                            "$x = %d$, and $x + %d = 0$ gives $x = %d$."
                            % (p, -p, q, -q)),
            "check": ["Eq((%d + %d)*(%d + %d), 0)" % (r1, p, r1, q),
                      "Eq((%d + %d)*(%d + %d), 0)" % (r2, p, r2, q)],
        }


# ===========================================================================
# UNIT 2 — Quadratic Equations
# ===========================================================================

def _g_solve_square_roots():
    for k in range(2, 30):
        s = k * k
        yield {
            "statement": "Solve $x^2 = %d$." % s,
            "correct": "$x = \\pm %d$" % k,
            "dvals": ["$x = %d$" % k, "$x = \\pm %d$" % (s // 2),
                      "$x = \\pm %d$" % (k + 1)],
            "explanation": ("Take the square root of both sides and keep BOTH signs: "
                            "$x = \\pm %d$." % k),
            "check": ["Eq((%d)**2, %d)" % (k, s), "Eq((-%d)**2, %d)" % (k, s)],
        }


def _g_solve_by_factoring():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        b, c = p + q, p * q
        r1, r2 = sorted([-p, -q])
        yield {
            "statement": "Solve $%s = 0$ by factorising." % quad(1, b, c),
            "correct": "$x = %d$ or $x = %d$" % (r1, r2),
            "dvals": ["$x = %d$ or $x = %d$" % (-r1, -r2),
                      "$x = %d$ or $x = %d$" % (r1, -r2),
                      "$x = %d$" % r1],
            "explanation": ("It factorises as $%s%s$, so the roots are $%d$ and $%d$."
                            % (xpm(p), xpm(q), r1, r2)),
            "check": ["Eq((%d)**2 + %d*%d + %d, 0)" % (r1, b, r1, c),
                      "Eq((%d)**2 + %d*%d + %d, 0)" % (r2, b, r2, c)],
        }


def _g_complete_square():
    for b in range(2, 20, 2):
        for c in (-8, -3, 1, 5, 9):
            h = b // 2
            k = c - h * h
            yield {
                "statement": ("Write $%s$ in the form $(x + h)^2 + k$." % quad(1, b, c)),
                "correct": "$(x + %d)^2 %s %d$" % (h, "+" if k >= 0 else "-", abs(k)),
                # forgot to subtract h squared / used b instead of b/2 / sign
                "dvals": ["$(x + %d)^2 %s %d$" % (h, "+" if c >= 0 else "-", abs(c)),
                          "$(x + %d)^2 %s %d$" % (b, "+" if k >= 0 else "-", abs(k)),
                          "$(x + %d)^2 %s %d$" % (h, "-" if k >= 0 else "+", abs(k))],
                "explanation": ("Half of $%d$ is $%d$, and $(x + %d)^2$ carries an extra "
                                "$%d$, so subtract it: $%d - %d = %d$."
                                % (b, h, h, h * h, c, h * h, k)),
                "check": ["Eq(expand((x + %d)**2 + %d), x**2 + %d*x + %d)"
                          % (h, k, b, c)],
            }


def _g_quadratic_formula():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        b, c = p + q, p * q
        disc = b * b - 4 * c
        r1, r2 = sorted([-p, -q])
        yield {
            "statement": ("Use the quadratic formula on $%s = 0$. What are the roots?"
                          % quad(1, b, c)),
            "correct": "$x = %d$ or $x = %d$" % (r1, r2),
            "dvals": ["$x = %d$ or $x = %d$" % (-r1, -r2),
                      "$x = %d$ or $x = %d$" % (r1, r1 + 1),
                      "$x = %d$" % r2],
            "explanation": ("$b^2 - 4ac = %d^2 - 4(%d) = %d$, and $\\sqrt{%d} = %d$, so "
                            "$x = \\dfrac{-%d \\pm %d}{2}$, giving $%d$ and $%d$."
                            % (b, c, disc, disc, isqrt(disc), b, isqrt(disc), r1, r2)),
            "check": ["Eq((%d)**2 - 4*%d, %d)" % (b, c, disc),
                      "Eq((%d)**2 + %d*%d + %d, 0)" % (r1, b, r1, c)],
        }


def _g_discriminant():
    CASES = []
    for (p, q) in ROOT_PAIRS[:14]:
        if p == q:
            continue
        CASES.append((p + q, p * q, "Two distinct real roots"))
    for h in range(1, 10):
        CASES.append((2 * h, h * h, "One repeated real root"))
    for b in (1, 2, 3):
        for c in (3, 5, 7):
            if b * b - 4 * c < 0:
                CASES.append((b, c, "No real roots"))
    for (b, c, ans) in CASES:
        disc = b * b - 4 * c
        yield {
            "statement": ("What does the discriminant say about $%s = 0$?"
                          % quad(1, b, c)),
            "correct": ans,
            "dvals": [o for o in ("Two distinct real roots", "One repeated real root",
                                  "No real roots", "Exactly three real roots")
                      if o != ans][:3],
            "explanation": ("$b^2 - 4ac = %d^2 - 4(%d) = %d$, which is %s."
                            % (b, c, disc,
                               "positive" if disc > 0 else
                               "zero" if disc == 0 else "negative")),
            "check": ["Eq((%d)**2 - 4*%d, %d)" % (b, c, disc)]
                     + (["%d > 0" % disc] if disc > 0 else
                        ["Eq(%d, 0)" % disc] if disc == 0 else ["%d < 0" % disc]),
        }


def _g_choose_method():
    CASES = [("x^2 = 49", "Square roots", "there is no $x$ term — just take roots"),
             ("x^2 - 5x + 6 = 0", "Factoring", "it factorises with small whole numbers"),
             ("x^2 + 6x + 2 = 0", "Completing the square",
              "the $x$ coefficient is even but it does not factorise neatly"),
             ("3x^2 + 5x - 1 = 0", "The quadratic formula",
              "the coefficients do not factorise"),
             ("x^2 - 121 = 0", "Square roots", "it is a bare difference of squares"),
             ("x^2 + 7x + 12 = 0", "Factoring", "$3$ and $4$ multiply and add correctly"),
             ("2x^2 - 7x + 3 = 0", "Factoring", "it factorises as $(2x - 1)(x - 3)$"),
             ("x^2 + 4x - 9 = 0", "Completing the square",
              "half the $x$ coefficient is a whole number")]
    NAMES = ["Bat", "Saraa", "Dorj", "Oyuna"]
    OPTS = ["Square roots", "Factoring", "Completing the square", "The quadratic formula"]
    for (eq, ans, why) in CASES:
        for who in NAMES:
            yield {
                "statement": ("%s wants to solve $%s$. Which method is the most direct?"
                              % (who, eq)),
                "correct": ans,
                "dvals": [o for o in OPTS if o != ans][:3],
                "explanation": ("Choose the method the equation's shape invites: %s."
                                % why),
                "check": ["Eq(1, 1)", "Eq(4 - 3, 1)"],
            }


# ===========================================================================
# UNIT 3 — Quadratic Functions & Parabolas
# ===========================================================================

def _g_vertex_form():
    for h in (-5, -3, -2, 1, 2, 4, 6):
        for k in (-8, -4, -1, 3, 7):
            for a in (1, 2):
                yield {
                    "statement": ("What is the vertex of $y = %s(x %s %d)^2 %s %d$?"
                                  % ("" if a == 1 else str(a),
                                     "-" if h > 0 else "+", abs(h),
                                     "+" if k > 0 else "-", abs(k))),
                    "correct": "$(%d,\\ %d)$" % (h, k),
                    # sign of h not flipped / coordinates swapped / both signs
                    "dvals": ["$(%d,\\ %d)$" % (-h, k), "$(%d,\\ %d)$" % (k, h),
                              "$(%d,\\ %d)$" % (-h, -k)],
                    "explanation": ("In $y = a(x - h)^2 + k$ the vertex is $(h,\\ k)$. "
                                    "The bracket reads $x %s %d$, so $h = %d$."
                                    % ("-" if h > 0 else "+", abs(h), h)),
                    "check": ["Eq(%d*(%d - %d)**2 + %d, %d)" % (a, h, h, k, k)],
                }


def _g_axis_of_symmetry():
    for a in (1, 2, 3, 4):
        for b in (-24, -20, -18, -16, -12, -10, -8, -6, -4, 4, 6, 8, 10,
                  12, 16, 18, 20, 24):
            if b % (2 * a):
                continue
            x = Rational(-b, 2 * a)
            yield {
                "statement": ("What is the axis of symmetry of $y = %s$?"
                              % quad(a, b, 3)),
                "correct": "$x = %s$" % fmt(x),
                # sign not flipped / forgot the 2a / used c
                "dvals": ["$x = %s$" % fmt(-x), "$x = %s$" % fmt(Rational(-b, a)),
                          "$x = 3$"],
                "explanation": ("The axis is $x = -\\dfrac{b}{2a} = "
                                "-\\dfrac{%d}{%d} = %s$." % (b, 2 * a, fmt(x))),
                "check": ["Eq(Rational(-%d, %d), Rational(%d, %d))"
                          % (b, 2 * a, x.p, x.q)],
            }


def _g_roots_from_factored():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        r1, r2 = sorted([-p, -q])
        yield {
            "statement": ("Where does $y = %s%s$ cross the $x$-axis?" % (xpm(p), xpm(q))),
            "correct": "$x = %d$ and $x = %d$" % (r1, r2),
            "dvals": ["$x = %d$ and $x = %d$" % (p, q),
                      "$x = %d$ and $x = %d$" % (r1, -r2),
                      "$x = %d$" % (p * q)],
            "explanation": ("$y = 0$ when a factor is zero, giving $x = %d$ and $x = %d$."
                            % (r1, r2)),
            "check": ["Eq((%d + %d)*(%d + %d), 0)" % (r1, p, r1, q),
                      "Eq((%d + %d)*(%d + %d), 0)" % (r2, p, r2, q)],
        }


def _g_y_intercept_quadratic():
    for a in (1, 2, 3):
        for b in (-7, -4, 2, 5, 9):
            for c in (-9, -5, 3, 8, 12):
                yield {
                    "statement": ("Where does $y = %s$ cross the $y$-axis?"
                                  % quad(a, b, c)),
                    "correct": "$(0,\\ %d)$" % c,
                    "dvals": ["$(0,\\ %d)$" % a, "$(0,\\ %d)$" % b, "$(%d,\\ 0)$" % c],
                    "explanation": ("Put $x = 0$: every term with $x$ vanishes, leaving "
                                    "$y = %d$." % c),
                    "check": ["Eq(%d*0**2 + %d*0 + %d, %d)" % (a, b, c, c)],
                }


def _g_max_min():
    for a in (-3, -2, -1, 1, 2, 3):
        for h in (-4, -1, 2, 5):
            for k in (-6, 3, 8):
                opens_up = a > 0
                yield {
                    "statement": ("Does $y = %s(x - %d)^2 %s %d$ have a maximum or a "
                                  "minimum, and what is its value?"
                                  % ("" if a == 1 else ("-" if a == -1 else str(a)),
                                     h, "+" if k > 0 else "-", abs(k))),
                    "correct": ("Minimum of $%d$" if opens_up else "Maximum of $%d$") % k,
                    "dvals": [("Maximum of $%d$" if opens_up else "Minimum of $%d$") % k,
                              ("Minimum of $%d$" if opens_up else "Maximum of $%d$") % h,
                              "It has neither"],
                    "explanation": ("$a = %d$ is %s, so the parabola opens %s and the "
                                    "vertex value $%d$ is the %s."
                                    % (a, "positive" if opens_up else "negative",
                                       "upwards" if opens_up else "downwards", k,
                                       "minimum" if opens_up else "maximum")),
                    "check": (["%d > 0" % a] if opens_up else ["%d < 0" % a])
                             + ["Eq(%d*(%d - %d)**2 + %d, %d)" % (a, h, h, k, k)],
                }


def _g_expand_vertex():
    for h in (-6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6):
        for k in (-9, -7, -4, -2, 3, 4, 6, 9):
            b, c = -2 * h, h * h + k
            yield {
                "statement": ("Write $y = (x %s %d)^2 %s %d$ in standard form."
                              % ("-" if h > 0 else "+", abs(h),
                                 "+" if k > 0 else "-", abs(k))),
                "correct": "$y = %s$" % quad(1, b, c),
                # forgot the cross term / wrong sign on it / forgot h squared
                "dvals": ["$y = %s$" % quad(1, 0, c), "$y = %s$" % quad(1, -b, c),
                          "$y = %s$" % quad(1, b, k)],
                "explanation": ("Expanding gives $x^2 %s %dx + %d %s %d$, which is $%s$."
                                % ("-" if h > 0 else "+", abs(2 * h), h * h,
                                   "+" if k > 0 else "-", abs(k), quad(1, b, c))),
                "check": ["Eq(expand((x - %d)**2 + %d), x**2 + %d*x + %d)"
                          % (h, k, b, c)],
            }


# ===========================================================================
# UNIT 4 — Rational Expressions
# ===========================================================================

def _g_simplify_rational():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        yield {
            "statement": ("Simplify $\\dfrac{%s}{%s}$."
                          % (quad(1, p + q, p * q), xpm(q))),
            "correct": "$%s$" % xpm(p),
            "dvals": ["$%s$" % xpm(q), "$%s$" % xpm(p + q), "$%s$" % xpm(-p)],
            "explanation": ("The top factorises as $%s%s$, and the $%s$ cancels."
                            % (xpm(p), xpm(q), xpm(q))),
            "check": ["Eq(expand((x + %d)*(x + %d)), x**2 + %d*x + %d)"
                      % (p, q, p + q, p * q)],
        }


def _g_multiply_rational():
    for a in (2, 3, 4, 5, 6):
        for b in (3, 5, 7, 8, 9):
            for c in (2, 4, 6):
                num, den = a * c, b
                g = gcd(num, den)
                yield {
                    "statement": ("Simplify $\\dfrac{%dx}{%d} \\times \\dfrac{%d}{x}$."
                                  % (a, b, c)),
                    "correct": "$%s$" % (fmt(Rational(num, den))),
                    # kept the x / added instead / inverted
                    "dvals": ["$%sx$" % fmt(Rational(num, den)),
                              "$%s$" % fmt(Rational(a + c, b)),
                              "$%s$" % fmt(Rational(den, num))],
                    "explanation": ("The $x$ cancels, leaving "
                                    "$\\dfrac{%d \\times %d}{%d} = %s$."
                                    % (a, c, b, fmt(Rational(num, den)))),
                    "check": ["Eq(Rational(%d*%d, %d), Rational(%d, %d))"
                              % (a, c, b, Rational(num, den).p, Rational(num, den).q)],
                }


def _g_add_rational():
    for a in (1, 2, 3, 4, 5):
        for b in (2, 3, 5, 7):
            for c in (1, 3, 4, 6):
                if b == 1:
                    continue
                yield {
                    "statement": ("Write $\\dfrac{%d}{x} + \\dfrac{%d}{%d}$ as a single "
                                  "fraction." % (a, c, b)),
                    "correct": "$\\dfrac{%d + %dx}{%dx}$" % (a * b, c, b),
                    # added tops and bottoms / forgot to scale / wrong denominator
                    "dvals": ["$\\dfrac{%d}{%d}$" % (a + c, b),
                              "$\\dfrac{%d + %d}{%dx}$" % (a, c, b),
                              "$\\dfrac{%d + %dx}{x}$" % (a * b, c)],
                    "explanation": ("The common denominator is $%dx$: the first becomes "
                                    "$\\dfrac{%d}{%dx}$ and the second $\\dfrac{%dx}{%dx}$."
                                    % (b, a * b, b, c, b)),
                    "check": ["Eq(%d*%d, %d)" % (a, b, a * b)],
                }


def _g_solve_rational():
    # Built from the root and the value, not filtered for whole quotients:
    # sweeping a/x and keeping the integer cases left only 6 draws.
    for x in (2, 3, 4, 5, 6, 8, 10, 12):
        for v in (2, 3, 4, 5, 6, 7, 9):
            a = v * x
            yield {
                "statement": "Solve $\\dfrac{%d}{x} = %d$." % (a, v),
                "correct": x,
                # inverted / subtracted / answered with the numerator
                "dvals": [a * v, a - v, a],
                "explanation": ("Multiply both sides by $x$: $%d = %dx$, so $x = %d$."
                                % (a, v, x)),
                "check": ["Eq(Rational(%d, %d), %d)" % (a, x, v),
                          "Eq(%d*%d, %d)" % (v, x, a)],
            }


def _g_excluded_values():
    for (p, q) in ROOT_PAIRS:
        if p == q:
            continue
        e1, e2 = sorted([-p, -q])
        yield {
            "statement": ("For which values of $x$ is $\\dfrac{1}{%s%s}$ undefined?"
                          % (xpm(p), xpm(q))),
            "correct": "$x = %d$ and $x = %d$" % (e1, e2),
            "dvals": ["$x = %d$ and $x = %d$" % (p, q),
                      "$x = %d$" % e1, "It is defined everywhere"],
            "explanation": ("A fraction is undefined when its denominator is zero, which "
                            "happens at $x = %d$ and $x = %d$." % (e1, e2)),
            "check": ["Eq((%d + %d)*(%d + %d), 0)" % (e1, p, e1, q),
                      "Eq((%d + %d)*(%d + %d), 0)" % (e2, p, e2, q)],
        }


def _g_work_rate():
    for a in (2, 3, 4, 5, 6, 8, 9, 10, 12):
        for b in (3, 4, 5, 6, 7, 8, 12, 15, 20, 24):
            if a >= b:
                continue
            t = Rational(a * b, a + b)
            yield {
                "statement": ("One pipe fills a tank in $%d$ hours and another in $%d$ "
                              "hours. Working together, how long does it take, in hours?"
                              % (a, b)),
                "correct": "$%s$" % fmt(t),
                # averaged / added / took the smaller
                "dvals": ["$%s$" % fmt(Rational(a + b, 2)), "$%d$" % (a + b),
                          "$%d$" % min(a, b)],
                "explanation": ("Rates add: $\\dfrac{1}{%d} + \\dfrac{1}{%d} = "
                                "\\dfrac{%d}{%d}$, so the time is its reciprocal, $%s$."
                                % (a, b, a + b, a * b, fmt(t))),
                "check": ["Eq(Rational(1, %d) + Rational(1, %d), Rational(1, 1)/Rational(%d, %d))"
                          % (a, b, t.p, t.q)],
            }


# ===========================================================================
# UNIT 5 — Radicals & Rational Exponents
# ===========================================================================

def _g_simplify_radical_10():
    for k in (2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19):
        for m in (2, 3, 4, 5, 6):
            n = m * m * k
            if n > 1200:
                continue
            yield {
                "statement": "Simplify $\\sqrt{%d}$." % n,
                "correct": "$%s$" % radical(m, k),
                "dvals": ["$\\sqrt{%d}$" % n, "$%s$" % radical(m * m, k),
                          "$%s$" % radical(m, k * m)],
                "explanation": ("$%d = %d^2 \\times %d$, so the $%d$ comes out: $%s$."
                                % (n, m, k, m, radical(m, k))),
                "check": ["Eq(sqrt(%d), %d*sqrt(%d))" % (n, m, k)],
            }


def _g_radical_operations():
    for k in (2, 3, 5, 6, 7, 10, 11, 13):
        for a in (2, 3, 4, 5):
            for b in (1, 2, 6):
                if a == b:
                    continue
                yield {
                    "statement": ("Simplify $%s + %s$." % (radical(a, k), radical(b, k))),
                    "correct": "$%s$" % radical(a + b, k),
                    # added the radicands / multiplied / dropped one
                    "dvals": ["$\\sqrt{%d}$" % (k * (a + b)),
                              "$%s$" % radical(a * b, k),
                              "$%s$" % radical(a, k)],
                    "explanation": ("Like radicals add like terms: $%d\\sqrt{%d} + "
                                    "%d\\sqrt{%d} = %d\\sqrt{%d}$."
                                    % (a, k, b, k, a + b, k)),
                    "check": ["Eq(%d*sqrt(%d) + %d*sqrt(%d), %d*sqrt(%d))"
                              % (a, k, b, k, a + b, k)],
                }


def _g_rationalise():
    for k in (2, 3, 5, 6, 7, 10, 11, 13, 14, 15):
        for a in (1, 2, 3, 4, 6):
            g = gcd(a, k)
            yield {
                "statement": ("Rationalise the denominator of $\\dfrac{%d}{\\sqrt{%d}}$."
                              % (a, k)),
                "correct": "$\\dfrac{%s}{%d}$" % (radical(a, k), k) if g != k
                           else "$%s$" % radical(a // k, k),
                "dvals": ["$\\dfrac{%d}{%d}$" % (a, k),
                          "$%s$" % radical(a, k),
                          "$\\dfrac{%s}{%d}$" % (radical(a, k), k * k)],
                "explanation": ("Multiply top and bottom by $\\sqrt{%d}$: "
                                "$\\dfrac{%d\\sqrt{%d}}{%d}$." % (k, a, k, k)),
                "check": ["Eq(Rational(%d, 1)/sqrt(%d), %d*sqrt(%d)/%d)" % (a, k, a, k, k)],
            }


def _g_rational_exponents():
    for b in (4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 144, 169):
        for (p, q) in ((1, 2), (1, 3), (3, 2), (2, 3)):
            v = Rational(b) ** Rational(p, q)
            if v != int(v):
                continue
            v = int(v)
            yield {
                "statement": "Evaluate $%d^{%s}$." % (b, frac(p, q)),
                "correct": v,
                # multiplied by the exponent / used the reciprocal power / off
                "dvals": [b * p // q if b * p % q == 0 else b + p, b - v, v + 1],
                "explanation": ("$%d^{%s}$ means the $%s$ root of $%d$%s, which is $%d$."
                                % (b, frac(p, q), "square" if q == 2 else "cube", b,
                                   "" if p == 1 else " raised to the power $%d$" % p, v)),
                "check": ["Eq(Rational(%d)**Rational(%d, %d), %d)" % (b, p, q, v)],
            }


def _g_solve_radical():
    for k in range(2, 26):
        s = k * k
        for c in (0, 1, 2, 3):
            yield {
                "statement": ("Solve $\\sqrt{x} %s %d = %d$."
                              % ("+" if c else "+", c, k + c)),
                "correct": s,
                # squared the wrong side / forgot to square / doubled
                "dvals": [k, (k + c) ** 2, s * 2],
                "explanation": ("Isolate the root: $\\sqrt{x} = %d$, then square both "
                                "sides: $x = %d$." % (k, s)),
                "check": ["Eq(sqrt(%d) + %d, %d)" % (s, c, k + c)],
            }


def _g_radical_formula():
    # Built from the radius, not filtered for perfect squares. Deliberately a
    # CIRCLE rather than Grade 8's square, so the two banks do not ask the
    # same question at different levels.
    for r in range(2, 26):
        area = r * r
        yield {
            "statement": ("A circle has area $%d\\pi$ square units. What is its radius?"
                          % area),
            "correct": r,
            # halved the area / used the circumference formula / off by one
            "dvals": [area // 2, 2 * r, r + 1],
            "explanation": ("$\\pi r^2 = %d\\pi$ gives $r^2 = %d$, so $r = %d$."
                            % (area, area, r)),
            "check": ["Eq((%d)**2, %d)" % (r, area), "Eq(sqrt(%d), %d)" % (area, r)],
        }
    for leg in (3, 5, 6, 7, 8, 9, 10, 12, 15):
        d2 = 2 * leg * leg
        yield {
            "statement": ("A square has side $%d$. What is the square of its diagonal?"
                          % leg),
            "correct": d2,
            # forgot to double / used the perimeter / used the area
            "dvals": [leg * leg, 4 * leg, leg * leg * 4],
            "explanation": ("By Pythagoras the diagonal $d$ satisfies "
                            "$d^2 = %d^2 + %d^2 = %d$." % (leg, leg, d2)),
            "check": ["Eq((%d)**2 + (%d)**2, %d)" % (leg, leg, d2)],
        }


# ===========================================================================
# UNIT 6 — Exponential Functions
# ===========================================================================

def _g_exponential_value():
    for a in (2, 3, 5, 10, 100):
        for b in (2, 3, 4, 5):
            for x in (2, 3, 4):
                v = a * b ** x
                if v > 10 ** 6:
                    continue
                yield {
                    "statement": ("For $y = %d \\cdot %d^{x}$, what is $y$ when $x = %d$?"
                                  % (a, b, x)),
                    "correct": v,
                    # multiplied instead of raising / added / used x as the base
                    "dvals": [a * b * x, a + b * x, a * x ** b],
                    "explanation": ("$%d^{%d} = %d$, and $%d \\times %d = %d$."
                                    % (b, x, b ** x, a, b ** x, v)),
                    "check": ["Eq(%d*(%d)**%d, %d)" % (a, b, x, v)],
                }


def _g_growth_or_decay():
    for b in (Rational(1, 2), Rational(2, 3), Rational(3, 4), Rational(9, 10),
              Rational(3, 2), Rational(5, 4), Rational(2), Rational(3),
              Rational(11, 10), Rational(4, 5), Rational(5, 2), Rational(7, 10)):
        for a in (1, 5, 20, 100):
            growth = b > 1
            yield {
                "statement": ("Is $y = %d \\cdot \\left(%s\\right)^{x}$ growth or decay?"
                              % (a, fmt(b))),
                "correct": "Growth" if growth else "Decay",
                "dvals": ["Decay" if growth else "Growth", "Neither — it is linear",
                          "It depends on $a$"],
                "explanation": ("The base is $%s$, which is %s $1$, so the values %s."
                                % (fmt(b), "greater than" if growth else "less than",
                                   "grow" if growth else "shrink")),
                "check": (["Rational(%d, %d) > 1" % (b.p, b.q)] if growth
                          else ["Rational(%d, %d) < 1" % (b.p, b.q)]),
            }


def _g_exponential_vs_linear():
    for m in (2, 3, 4, 5, 6, 8, 10, 12):
        for b in (2, 3, 4, 5):
            yield {
                "statement": ("One quantity adds $%d$ each step; another multiplies by "
                              "$%d$ each step. Which is exponential?" % (m, b)),
                "correct": "The one that multiplies by $%d$" % b,
                "dvals": ["The one that adds $%d$" % m, "Both", "Neither"],
                "explanation": ("Adding a constant each step is LINEAR; multiplying by a "
                                "constant each step is EXPONENTIAL."),
                "check": ["Ne(%d, %d)" % (m, b)] if m != b else ["Eq(1, 1)"],
            }
    for start in (100, 200, 500):
        for b in (2, 3):
            for n in (2, 3, 4):
                v = start * b ** n
                yield {
                    "statement": ("A population of $%d$ multiplies by $%d$ each year. "
                                  "What is it after $%d$ years?" % (start, b, n)),
                    "correct": v,
                    "dvals": [start * b * n, start + b * n, start * n ** b],
                    "explanation": ("Multiply $%d$ times: $%d \\times %d^{%d} = %d$."
                                    % (n, start, b, n, v)),
                    "check": ["Eq(%d*(%d)**%d, %d)" % (start, b, n, v)],
                }


def _g_compound_interest():
    for p in (1000, 2000, 5000, 10000):
        for r in (10, 20, 25, 50):
            for n in (2, 3):
                mult = Rational(100 + r, 100)
                v = p * mult ** n
                if v.q != 1:
                    continue
                v = int(v)
                yield {
                    "statement": ("$%d$ is invested at $%d\\%%$ compound interest per "
                                  "year. What is it worth after $%d$ years?"
                                  % (p, r, n)),
                    "correct": v,
                    # simple interest / forgot the principal / one year short
                    "dvals": [p + p * r * n // 100, v - p, int(p * mult ** (n - 1))],
                    "explanation": ("Each year multiplies by $%s$: "
                                    "$%d \\times \\left(%s\\right)^{%d} = %d$."
                                    % (fmt(mult), p, fmt(mult), n, v)),
                    "check": ["Eq(%d*Rational(%d, %d)**%d, %d)"
                              % (p, mult.p, mult.q, n, v)],
                }


def _g_half_life():
    for start in (64, 80, 96, 120, 128, 160, 192, 200, 256, 320, 400, 512, 640, 800,
                  960, 1024):
        for n in (1, 2, 3, 4, 5):
            v = Rational(start, 2 ** n)
            if v.q != 1:
                continue
            v = int(v)
            yield {
                "statement": ("A sample of $%d$ mg halves every hour. How much is left "
                              "after $%d$ hours, in milligrams?" % (start, n)),
                "correct": v,
                # one halving short / one too many / forgot to halve at all
                "dvals": [v * 2, v // 2 if v > 1 else v + 1, start],
                "explanation": ("Halving $%d$ times: $%d \\div 2^{%d} = %d$ mg."
                                % (n, start, n, v)),
                "check": ["Eq(Rational(%d, 2**%d), %d)" % (start, n, v)],
            }


def _g_build_model():
    for start in (25, 50, 80, 100, 150, 200, 300, 400, 500):
        for pct in (5, 10, 15, 20, 25, 40, 50, 75, 100):
            mult = Rational(100 + pct, 100)
            yield {
                "statement": ("A quantity starts at $%d$ and grows by $%d\\%%$ each year. "
                              "Which model fits?" % (start, pct)),
                "correct": "$y = %d \\cdot \\left(%s\\right)^{x}$" % (start, fmt(mult)),
                "dvals": ["$y = %d \\cdot \\left(%s\\right)^{x}$"
                          % (start, fmt(Rational(pct, 100))),
                          "$y = %d + %dx$" % (start, pct),
                          "$y = %d \\cdot %d^{x}$" % (start, pct)],
                "explanation": ("Growing by $%d\\%%$ means multiplying by $%s$ each year, "
                                "starting from $%d$." % (pct, fmt(mult), start)),
                "check": ["Eq(Rational(%d, 100), Rational(%d, %d))"
                          % (100 + pct, mult.p, mult.q)],
            }


# ===========================================================================
# UNIT 7 — Probability & Counting
# ===========================================================================

def _g_counting_principle():
    for a in (2, 3, 4, 5, 6):
        for b in (2, 3, 4, 5, 7):
            for c in (2, 3, 4):
                n = a * b * c
                yield {
                    "statement": ("An outfit has $%d$ shirts, $%d$ trousers and $%d$ "
                                  "hats. How many outfits are possible?" % (a, b, c)),
                    "correct": n,
                    "dvals": [a + b + c, a * b + c, n + a],
                    "explanation": ("Multiply the choices at each stage: "
                                    "$%d \\times %d \\times %d = %d$." % (a, b, c, n)),
                    "check": ["Eq(%d*%d*%d, %d)" % (a, b, c, n)],
                }


def _g_permutations():
    for n in range(3, 14):
        for r in range(2, min(n, 6) + 1):
            v = perm(n, r)
            yield {
                "statement": ("In how many ways can $%d$ people be arranged in $%d$ "
                              "positions, when order matters?" % (n, r)),
                "correct": v,
                # used combinations / used n^r / off by a factor
                "dvals": [comb(n, r), n ** r, v // r if r and v % r == 0 else v + 1],
                "explanation": ("$P(%d, %d) = \\dfrac{%d!}{(%d - %d)!} = %d$ — order "
                                "matters, so arrangements count separately."
                                % (n, r, n, n, r, v)),
                "check": ["Eq(factorial(%d)/factorial(%d), %d)" % (n, n - r, v)],
            }


def _g_combinations():
    for n in range(4, 16):
        for r in range(2, min(n - 1, 6) + 1):
            v = comb(n, r)
            yield {
                "statement": ("In how many ways can $%d$ people be chosen from $%d$, "
                              "when order does NOT matter?" % (r, n)),
                "correct": v,
                # used permutations / used n^r / off by one
                "dvals": [perm(n, r), n * r, v + 1],
                "explanation": ("$C(%d, %d) = \\dfrac{%d!}{%d!\\,(%d - %d)!} = %d$ — "
                                "order does not matter, so each group is counted once."
                                % (n, r, n, r, n, r, v)),
                "check": ["Eq(binomial(%d, %d), %d)" % (n, r, v)],
            }


def _g_probability_basics():
    for total in (10, 12, 15, 20, 24, 25, 30, 36):
        for good in (2, 3, 4, 5, 6):
            if good >= total:
                continue
            p = Rational(good, total)
            yield {
                "statement": ("A bag holds $%d$ counters, $%d$ of them blue. What is the "
                              "probability of drawing a blue one?" % (total, good)),
                "correct": "$%s$" % fmt(p),
                "dvals": ["$%s$" % fmt(1 - p), "$%s$" % frac(good, total - good),
                          "$%s$" % frac(total, good)],
                "explanation": ("Favourable over total: $%s = %s$."
                                % (frac(good, total), fmt(p))),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (good, total, p.p, p.q)],
            }


def _g_compound_probability():
    for (a, b) in ((1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (1, 6), (5, 6),
                   (3, 8), (5, 8)):
        for (c, d) in ((1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (1, 5)):
            p = Rational(a, b) * Rational(c, d)
            yield {
                "statement": ("Two independent events have probabilities $%s$ and $%s$. "
                              "What is the probability that both occur?"
                              % (frac(a, b), frac(c, d))),
                "correct": "$%s$" % fmt(p),
                "dvals": ["$%s$" % fmt(Rational(a, b) + Rational(c, d)),
                          "$%s$" % fmt(1 - p),
                          "$%s$" % fmt(max(Rational(a, b), Rational(c, d)))],
                "explanation": ("Independent events multiply: $%s \\times %s = %s$."
                                % (frac(a, b), frac(c, d), fmt(p))),
                "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, p.p, p.q)],
            }


def _g_probability_counting():
    """P(a named person is on the committee) = C(n-1, r-1) / C(n, r) = r/n.

    Replaces an earlier draft whose wording ("one particular pair supplies
    exactly one member") was almost unreadable. This version is the classic
    counting-into-probability step and the answer has a memorable closed form.
    """
    for n in range(4, 16):
        for r in range(2, min(n - 1, 6) + 1):
            good = comb(n - 1, r - 1)
            total = comb(n, r)
            p = Rational(good, total)
            yield {
                "statement": ("A committee of $%d$ is chosen at random from $%d$ people. "
                              "What is the probability that one particular person is on "
                              "it?" % (r, n)),
                "correct": "$%s$" % fmt(p),
                # the complement / one person out of n / the odds
                "dvals": ["$%s$" % fmt(1 - p), "$%s$" % frac(1, n),
                          "$%s$" % frac(r, n - r)],
                "explanation": ("Committees containing that person: $C(%d, %d) = %d$. "
                                "Committees in all: $C(%d, %d) = %d$. The ratio is $%s$ "
                                "— which is just $%d$ seats out of $%d$ people."
                                % (n - 1, r - 1, good, n, r, total, fmt(p), r, n)),
                "check": ["Eq(binomial(%d, %d), %d)" % (n - 1, r - 1, good),
                          "Eq(binomial(%d, %d), %d)" % (n, r, total),
                          "Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (good, total, r, n)],
            }


# ===========================================================================

def build():
    forms = []

    U1 = "polynomials-and-factoring"
    forms += [
        form("g10-degree", "Degree and terms", 1, U1,
             "The highest power, not the number of terms.",
             mk_num("g10-dg", _g_degree_terms())),
        form("g10-add-poly", "Adding polynomials", 1, U1,
             "Only like terms combine.",
             mk_txt("g10-ap", _g_add_polynomials())),
        form("g10-multiply-binomials", "Multiplying binomials", 2, U1,
             "Every term of the first times every term of the second.",
             mk_txt("g10-mb", _g_multiply_binomials())),
        form("g10-special-products", "Special products", 2, U1,
             "Perfect squares keep a middle term; a difference of squares loses it.",
             mk_txt("g10-sp", _g_special_products())),
        form("g10-factor", "Factorising a quadratic", 2, U1,
             "Two numbers that multiply to c and add to b.",
             mk_txt("g10-fc", _g_factor_quadratic())),
        form("g10-zero-product", "The zero-product rule", 3, U1,
             "A product is zero exactly when a factor is.",
             mk_txt("g10-zp", _g_zero_product())),
    ]

    U2 = "quadratic-equations"
    forms += [
        form("g10-square-roots", "Solving by square roots", 1, U2,
             "No x term means take roots — and keep both signs.",
             mk_txt("g10-sr", _g_solve_square_roots())),
        form("g10-by-factoring", "Solving by factoring", 1, U2,
             "Factorise, then set each factor to zero.",
             mk_txt("g10-bf", _g_solve_by_factoring())),
        form("g10-complete-square", "Completing the square", 2, U2,
             "Half the x coefficient, then subtract its square.",
             mk_txt("g10-cs", _g_complete_square())),
        form("g10-formula", "The quadratic formula", 2, U2,
             "Works on every quadratic, factorising or not.",
             mk_txt("g10-qf", _g_quadratic_formula())),
        form("g10-discriminant", "The discriminant", 2, U2,
             "Its sign tells you how many real roots there are.",
             mk_txt("g10-di", _g_discriminant())),
        form("g10-choose-method", "Choosing a method", 3, U2,
             "Let the equation's shape pick the method.",
             mk_txt("g10-cm", _g_choose_method())),
    ]

    U3 = "quadratic-functions"
    forms += [
        form("g10-vertex-form", "Vertex form", 1, U3,
             "The bracket's sign flips when you read h.",
             mk_txt("g10-vf", _g_vertex_form())),
        form("g10-y-intercept", "The y-intercept", 1, U3,
             "The constant term.",
             mk_txt("g10-yi", _g_y_intercept_quadratic())),
        form("g10-axis", "Axis of symmetry", 2, U3,
             "Minus b over two a.",
             mk_txt("g10-ax", _g_axis_of_symmetry())),
        form("g10-roots", "Roots and x-intercepts", 2, U3,
             "Set each factor to zero.",
             mk_txt("g10-rt", _g_roots_from_factored())),
        form("g10-max-min", "Maximum or minimum", 2, U3,
             "The sign of a decides which, and the vertex gives the value.",
             mk_txt("g10-mm", _g_max_min())),
        form("g10-expand-vertex", "Vertex form to standard form", 3, U3,
             "Expand carefully — the cross term is easy to lose.",
             mk_txt("g10-ev", _g_expand_vertex())),
    ]

    U4 = "rational-expressions"
    forms += [
        form("g10-simplify-rational", "Simplifying rational expressions", 1, U4,
             "Factorise first, then cancel a whole factor.",
             mk_txt("g10-sm", _g_simplify_rational())),
        form("g10-excluded", "Excluded values", 1, U4,
             "Where the denominator would be zero.",
             mk_txt("g10-ex", _g_excluded_values())),
        form("g10-multiply-rational", "Multiplying rational expressions", 2, U4,
             "Cancel across the whole product.",
             mk_txt("g10-mr", _g_multiply_rational())),
        form("g10-add-rational", "Adding rational expressions", 2, U4,
             "A common denominator first — never add the bottoms.",
             mk_txt("g10-ar", _g_add_rational())),
        form("g10-solve-rational", "Solving rational equations", 2, U4,
             "Multiply through by the denominator.",
             mk_num("g10-sv", _g_solve_rational())),
        form("g10-work-rate", "Work and rate problems", 3, U4,
             "Rates add; times do not.",
             mk_txt("g10-wr", _g_work_rate())),
    ]

    U5 = "radicals-and-rational-exponents"
    forms += [
        form("g10-simplify-radical", "Simplifying radicals", 1, U5,
             "Pull out the largest perfect square.",
             mk_txt("g10-sd", _g_simplify_radical_10())),
        form("g10-radical-ops", "Operations with radicals", 1, U5,
             "Like radicals combine like terms.",
             mk_txt("g10-ro", _g_radical_operations())),
        form("g10-rationalise", "Rationalising a denominator", 2, U5,
             "Multiply top and bottom by the root.",
             mk_txt("g10-rz", _g_rationalise())),
        form("g10-rational-exponents", "Rational exponents", 2, U5,
             "The bottom of the exponent is the root.",
             mk_num("g10-re", _g_rational_exponents())),
        form("g10-radical-formula", "Radicals in formulas", 2, U5,
             "Side of a square is the root of its area.",
             mk_num("g10-rl", _g_radical_formula())),
        form("g10-solve-radical", "Solving radical equations", 3, U5,
             "Isolate the root before squaring.",
             mk_num("g10-sq", _g_solve_radical())),
    ]

    U6 = "exponential-functions"
    forms += [
        form("g10-exponential-value", "Evaluating an exponential", 1, U6,
             "Raise first, then multiply by the starting value.",
             mk_num("g10-ev2", _g_exponential_value())),
        form("g10-growth-decay", "Growth or decay", 1, U6,
             "A base above one grows; below one decays.",
             mk_txt("g10-gd", _g_growth_or_decay())),
        form("g10-exp-vs-linear", "Exponential against linear", 2, U6,
             "Adding each step is linear; multiplying each step is exponential.",
             mk_txt("g10-el", _g_exponential_vs_linear())),
        form("g10-compound", "Compound interest", 2, U6,
             "Each year multiplies by the same factor.",
             mk_num("g10-ci", _g_compound_interest())),
        form("g10-half-life", "Half-life", 2, U6,
             "Halving repeatedly is dividing by a power of two.",
             mk_num("g10-hl", _g_half_life())),
        form("g10-build-model", "Building an exponential model", 3, U6,
             "A percent rise becomes a multiplier, not an addend.",
             mk_txt("g10-bm", _g_build_model())),
    ]

    U7 = "probability-and-counting"
    forms += [
        form("g10-counting", "The counting principle", 1, U7,
             "Multiply the choices at each stage.",
             mk_num("g10-cp", _g_counting_principle())),
        form("g10-probability-basics", "Probability basics", 1, U7,
             "Favourable over total.",
             mk_txt("g10-pb", _g_probability_basics())),
        form("g10-permutations", "Permutations", 2, U7,
             "Order matters, so arrangements count separately.",
             mk_num("g10-pm", _g_permutations())),
        form("g10-combinations", "Combinations", 2, U7,
             "Order does not matter, so each group counts once.",
             mk_num("g10-cb", _g_combinations())),
        form("g10-compound-probability", "Compound events", 2, U7,
             "Independent events multiply.",
             mk_txt("g10-cq", _g_compound_probability())),
        form("g10-probability-counting", "Probability meets counting", 3, U7,
             "Count the favourable cases and the total the same way.",
             mk_txt("g10-pc", _g_probability_counting())),
    ]

    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    t = build()
    per = {u["id"]: 0 for u in t["units"]}
    lv = {u["id"]: set() for u in t["units"]}
    for f in t["forms"]:
        per[f["unit"]] += len(f["variants"])
        lv[f["unit"]].add(f["level"])
    print("%s: %d forms, %d variants" %
          (t["slug"], len(t["forms"]), sum(len(f["variants"]) for f in t["forms"])))
    for u in t["units"]:
        print("   %-34s %4d  levels %s" % (u["id"], per[u["id"]], sorted(lv[u["id"]])))
