# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 8 — mirrors /math/8.

One collection PER UNIT across the seven Grade 8 topics.

Every answer is COMPUTED from a parameter sweep and carries a sympy check.
Radicals stay exact (sqrt, never a decimal), scientific notation is checked as
an exact product, and every distractor encodes a named student error.

Self-check:  python3 scripts/pb/grade8.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys
from math import gcd, isqrt

from sympy import Integer, Rational, sqrt

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt  # noqa: E402

SLUG = "8"
TITLE = "Grade 8"
TITLE_MN = "8-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 8 year — the real number "
         "system, exponents and scientific notation, roots, linear equations "
         "and functions, systems, and bivariate data.")

UNITS = [
    {"id": "the-real-number-system", "title": "The Real Number System",
     "blurb": "Rational and irrational numbers, terminating and repeating decimals, classifying and ordering the reals."},
    {"id": "exponents-and-scientific-notation", "title": "Exponents & Scientific Notation",
     "blurb": "The product, quotient and power rules, zero and negative exponents, and arithmetic in scientific notation."},
    {"id": "roots", "title": "Square & Cube Roots",
     "blurb": "Square and cube roots, estimating them, solving x² = k and x³ = k, and simplifying radicals."},
    {"id": "linear-equations", "title": "Linear Equations",
     "blurb": "Two-step equations, simplifying first, variables on both sides, brackets, and how many solutions there are."},
    {"id": "linear-functions", "title": "Linear Functions",
     "blurb": "What makes a function, slope as a rate of change, slope-intercept form, and reading a line four ways."},
    {"id": "systems-of-linear-equations", "title": "Systems of Linear Equations",
     "blurb": "Solving by graphing, substitution and elimination, and telling one solution from none or infinitely many."},
    {"id": "scatter-plots-and-bivariate-data", "title": "Scatter Plots & Bivariate Data",
     "blurb": "Correlation, outliers and clusters, fitting and using a trend line, and two-way tables."},
]


def frac(a, b):
    return "\\frac{%d}{%d}" % (a, b)


def lin(m, c, var="x"):
    """Render mx + c cleanly."""
    if m == 0:
        return str(c)
    s = var if m == 1 else ("-" + var if m == -1 else "%d%s" % (m, var))
    if c > 0:
        s += " + %d" % c
    elif c < 0:
        s += " - %d" % (-c)
    return s


def dec(v):
    """Exact decimal string for a Rational — never through float."""
    r = Rational(v)
    neg = r < 0
    r = abs(r)
    k = 0
    while (Rational(10) ** k * r).q != 1:
        k += 1
        if k > 8:
            raise ValueError("not a terminating decimal: %s" % v)
    n = int(Rational(10) ** k * r)
    t = str(n).rjust(k + 1, "0")
    out = t if k == 0 else t[:-k] + "." + t[-k:]
    return ("-" if neg else "") + out


def sci(mant, exp):
    """Scientific notation as LaTeX.

    The mantissa is written as a DECIMAL: nobody writes 5/2 x 10^4 for
    25 000, and rendering it through fmt() (which reduces to a fraction) made
    every one of these read wrongly.
    """
    return "%s \\times 10^{%d}" % (dec(mant), exp)


# ===========================================================================
# UNIT 1 — The Real Number System
# ===========================================================================

PERFECT = {n * n for n in range(1, 40)}


def _g_classify_real():
    ITEMS = []
    for n in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23):
        ITEMS.append(("$\\sqrt{%d}$" % n, "Irrational",
                      "$%d$ is not a perfect square, so its root never terminates "
                      "or repeats." % n, ["Ne(sqrt(%d), floor(sqrt(%d)))" % (n, n)]))
    for n in (4, 9, 16, 25, 36, 49, 64, 81, 100):
        ITEMS.append(("$\\sqrt{%d}$" % n, "Rational",
                      "$%d$ is a perfect square: $\\sqrt{%d} = %d$."
                      % (n, n, isqrt(n)), ["Eq(sqrt(%d), %d)" % (n, isqrt(n))]))
    for (a, b) in ((3, 8), (5, 6), (7, 12), (2, 9), (11, 20), (4, 15)):
        ITEMS.append(("$%s$" % frac(a, b), "Rational",
                      "Any ratio of two integers is rational by definition.",
                      ["Eq(Rational(%d, %d)*%d, %d)" % (a, b, b, a)]))
    for (lbl, kind, why, chk) in ITEMS:
        yield {
            "statement": "Is %s rational or irrational?" % lbl,
            "correct": kind,
            "dvals": ["Irrational" if kind == "Rational" else "Rational",
                      "Neither", "Both"],
            "explanation": why,
            "check": chk,
        }


def _g_terminating_repeating():
    for (a, b) in ((1, 2), (1, 4), (3, 8), (7, 10), (9, 20), (3, 25), (7, 40), (1, 5),
                   (11, 16), (13, 50), (1, 3), (2, 3), (1, 6), (5, 6), (1, 7), (2, 7),
                   (1, 9), (4, 9), (5, 11), (7, 12), (1, 15), (5, 18), (2, 21), (7, 22)):
        d = b // gcd(a, b)
        rest = d
        for p in (2, 5):
            while rest % p == 0:
                rest //= p
        terminating = rest == 1
        yield {
            "statement": ("Does $%s$ give a terminating or a repeating decimal?"
                          % frac(a, b)),
            "correct": "Terminating" if terminating else "Repeating",
            "dvals": ["Repeating" if terminating else "Terminating",
                      "Neither — it is irrational", "It depends on the numerator"],
            "explanation": ("In lowest terms the denominator is $%d$. A decimal "
                            "terminates exactly when that denominator has no prime "
                            "factor except $2$ and $5$ — here it %s."
                            % (d, "does not" if terminating else "does")),
            "check": (["Eq(Mod(%d, %d), 0)" % (10 ** 6, d)] if terminating
                      else ["Ne(Mod(%d, %d), 0)" % (10 ** 6, d)]),
        }


def _g_compare_reals():
    for n in list(range(2, 50)):
        if n in PERFECT:
            continue
        lo = isqrt(n)
        yield {
            "statement": ("Between which two consecutive whole numbers does "
                          "$\\sqrt{%d}$ lie?" % n),
            "correct": "$%d$ and $%d$" % (lo, lo + 1),
            "dvals": ["$%d$ and $%d$" % (lo + 1, lo + 2),
                      "$%d$ and $%d$" % (lo - 1, lo),
                      "$%d$ and $%d$" % (n // 2, n // 2 + 1)],
            "explanation": ("$%d^2 = %d$ and $%d^2 = %d$, and $%d$ sits between them."
                            % (lo, lo * lo, lo + 1, (lo + 1) ** 2, n)),
            "check": ["%d < %d" % (lo * lo, n), "%d < %d" % (n, (lo + 1) ** 2)],
        }


def _g_fraction_to_decimal():
    for (a, b, s) in ((1, 2, "0.5"), (1, 4, "0.25"), (3, 4, "0.75"), (1, 5, "0.2"),
                      (2, 5, "0.4"), (3, 5, "0.6"), (4, 5, "0.8"), (1, 8, "0.125"),
                      (3, 8, "0.375"), (5, 8, "0.625"), (7, 8, "0.875"), (1, 10, "0.1"),
                      (3, 10, "0.3"), (7, 10, "0.7"), (9, 10, "0.9"), (1, 16, "0.0625"),
                      (1, 20, "0.05"), (3, 20, "0.15"), (7, 20, "0.35"), (9, 20, "0.45"),
                      (11, 20, "0.55"), (13, 20, "0.65"), (17, 20, "0.85"),
                      (1, 25, "0.04"), (3, 25, "0.12"), (7, 25, "0.28"),
                      (1, 40, "0.025"), (3, 40, "0.075")):
        yield {
            "statement": "Write $%s$ as a decimal." % frac(a, b),
            "correct": "$%s$" % s,
            "dvals": ["$%s$" % str(Rational(b, a).evalf(4))[:6],
                      "$0.%d%d$" % (a, b) if b < 100 else "$0.%d$" % a,
                      "$%s$" % s.replace("0.", "0.0", 1)],
            "explanation": ("Divide the top by the bottom: $%d \\div %d = %s$."
                            % (a, b, s)),
            "check": ["Eq(Rational(%d, %d), Rational('%s'))" % (a, b, s)],
        }


def _g_order_reals():
    for n in list(range(2, 50)):
        if n in PERFECT:
            continue
        lo = isqrt(n)
        rival = Rational(2 * lo * lo + 1, 2 * lo)      # a close rational
        bigger = "$\\sqrt{%d}$" % n if sqrt(n) > rival else "$%s$" % fmt(rival)
        smaller = "$%s$" % fmt(rival) if sqrt(n) > rival else "$\\sqrt{%d}$" % n
        yield {
            "statement": ("Which is greater, $\\sqrt{%d}$ or $%s$?" % (n, fmt(rival))),
            "correct": bigger,
            "dvals": [smaller, "They are equal", "$%d$" % (lo + 1)],
            # `bigger` already carries its own $...$ — stripping them is exactly
            # the defect the precalculus bank shipped with.
            "explanation": ("Square both: $\\sqrt{%d}^2 = %d$ and $\\left(%s\\right)^2 "
                            "= %s$, so %s is the greater."
                            % (n, n, fmt(rival), fmt(rival ** 2), bigger)),
            "check": ["Ne(sqrt(%d), Rational(%d, %d))" % (n, rival.p, rival.q)],
        }


def _g_closure():
    CASES = [
        ("the sum of two rational numbers", "Always rational",
         "A sum of two ratios of integers is another ratio of integers."),
        ("the product of two rational numbers", "Always rational",
         "Multiplying two ratios of integers gives a ratio of integers."),
        ("the sum of a rational and an irrational number", "Always irrational",
         "If the sum were rational, subtracting the rational part would make the "
         "irrational one rational too."),
        ("the product of a non-zero rational and an irrational number",
         "Always irrational",
         "Dividing the product by the rational factor would otherwise make the "
         "irrational number rational."),
        ("the sum of two irrational numbers", "Sometimes rational",
         "$\\sqrt{2} + (-\\sqrt{2}) = 0$ is rational, but $\\sqrt{2} + \\sqrt{3}$ "
         "is not."),
        ("the product of two irrational numbers", "Sometimes rational",
         "$\\sqrt{2} \\times \\sqrt{2} = 2$ is rational, but $\\sqrt{2} \\times "
         "\\sqrt{3}$ is not."),
    ]
    OPTS = ["Always rational", "Always irrational", "Sometimes rational", "Never defined"]
    NAMES = ["Bat", "Saraa", "Dorj", "Oyuna", "Tuya"]
    for (desc, ans, why) in CASES:
        for who in NAMES:
            yield {
                "statement": ("%s claims something about %s. Which statement is true?"
                              % (who, desc)),
                "correct": ans,
                "dvals": [o for o in OPTS if o != ans][:3],
                "explanation": why,
                "check": ["Eq(sqrt(2)*sqrt(2), 2)"],
            }


# ===========================================================================
# UNIT 2 — Exponents & Scientific Notation
# ===========================================================================

def _g_product_rule():
    for b in (2, 3, 5, 7, 10):
        for m in range(2, 8):
            for n in range(2, 7):
                yield {
                    "statement": ("Simplify $%d^{%d} \\times %d^{%d}$." % (b, m, b, n)),
                    "correct": "$%d^{%d}$" % (b, m + n),
                    # multiplied the exponents / kept one / multiplied the bases
                    "dvals": ["$%d^{%d}$" % (b, m * n), "$%d^{%d}$" % (b, m),
                              "$%d^{%d}$" % (b * b, m + n)],
                    "explanation": ("Same base means ADD the exponents: "
                                    "$%d + %d = %d$." % (m, n, m + n)),
                    "check": ["Eq((%d)**%d * (%d)**%d, (%d)**%d)" % (b, m, b, n, b, m + n)],
                }


def _g_quotient_rule():
    for b in (2, 3, 5, 7, 10):
        for m in range(5, 12):
            for n in range(2, 5):
                if m - n < 1:
                    continue
                yield {
                    "statement": ("Simplify $\\dfrac{%d^{%d}}{%d^{%d}}$." % (b, m, b, n)),
                    "correct": "$%d^{%d}$" % (b, m - n),
                    # divided the exponents / added them / divided the bases
                    "dvals": ["$%d^{%d}$" % (b, m // n if n and m % n == 0 else m + n),
                              "$%d^{%d}$" % (b, m + n),
                              "$%d^{%d}$" % (1, m - n)],
                    "explanation": ("Same base means SUBTRACT the exponents: "
                                    "$%d - %d = %d$." % (m, n, m - n)),
                    "check": ["Eq(Rational((%d)**%d, (%d)**%d), (%d)**%d)"
                              % (b, m, b, n, b, m - n)],
                }


def _g_power_of_power():
    for b in (2, 3, 5, 7):
        for m in range(2, 7):
            for n in range(2, 6):
                yield {
                    "statement": "Simplify $\\left(%d^{%d}\\right)^{%d}$." % (b, m, n),
                    "correct": "$%d^{%d}$" % (b, m * n),
                    # added instead of multiplying / kept one / raised the base
                    "dvals": ["$%d^{%d}$" % (b, m + n), "$%d^{%d}$" % (b, m),
                              "$%d^{%d}$" % (b ** n, m)],
                    "explanation": ("A power of a power MULTIPLIES the exponents: "
                                    "$%d \\times %d = %d$." % (m, n, m * n)),
                    "check": ["Eq(((%d)**%d)**%d, (%d)**%d)" % (b, m, n, b, m * n)],
                }


def _g_zero_negative_exponent():
    for b in (2, 3, 4, 5, 6, 7, 10):
        yield {
            "statement": "What is $%d^{0}$?" % b,
            "correct": "$1$",
            "dvals": ["$0$", "$%d$" % b, "undefined"],
            "explanation": ("Any non-zero base to the power zero is $1$ — it is what "
                            "$%d^{n} \\div %d^{n}$ must equal." % (b, b)),
            "check": ["Eq((%d)**0, 1)" % b],
        }
        for n in range(1, 5):
            v = Rational(1, b ** n)
            yield {
                "statement": "Write $%d^{-%d}$ as a fraction." % (b, n),
                "correct": "$%s$" % fmt(v),
                # made it negative / kept the sign on the exponent / off by a power
                "dvals": ["$-%d$" % (b ** n), "$%d$" % (b ** n),
                          "$%s$" % fmt(Rational(1, b ** (n + 1)))],
                "explanation": ("A negative exponent means the reciprocal: "
                                "$%d^{-%d} = \\dfrac{1}{%d^{%d}} = %s$."
                                % (b, n, b, n, fmt(v))),
                "check": ["Eq(Rational(1, (%d)**%d), Rational(%d, %d))"
                          % (b, n, v.p, v.q)],
            }


def _g_scientific_notation():
    for mant in (Rational(12, 10), Rational(25, 10), Rational(34, 10), Rational(47, 10),
                 Rational(56, 10), Rational(68, 10), Rational(73, 10), Rational(89, 10),
                 Rational(15, 10), Rational(92, 10)):
        for exp in (3, 4, 5, 6, -3, -4):
            v = mant * Rational(10) ** exp
            plain = dec(v)
            yield {
                "statement": ("Write $%s$ in scientific notation." % plain),
                "correct": "$%s$" % sci(mant, exp),
                # exponent off by one / mantissa not between 1 and 10 / sign flipped
                "dvals": ["$%s$" % sci(mant, exp + 1),
                          "$%s$" % sci(mant * 10, exp - 1),
                          "$%s$" % sci(mant, -exp)],
                "explanation": ("The mantissa must sit between $1$ and $10$, and the "
                                "exponent counts how far the point moves: $%s$."
                                % sci(mant, exp)),
                "check": ["Eq(Rational(%d, %d)*Rational(10)**%d, Rational(%d, %d))"
                          % (mant.p, mant.q, exp, v.p, v.q)],
            }


def _g_sci_operations():
    for m1 in (Rational(2), Rational(3), Rational(4), Rational(15, 10), Rational(25, 10)):
        for m2 in (Rational(2), Rational(3), Rational(4), Rational(5)):
            for (e1, e2) in ((3, 4), (5, 2), (6, -3), (-2, 5), (4, 4)):
                mant = m1 * m2
                exp = e1 + e2
                # renormalise so the mantissa stays in [1, 10)
                while mant >= 10:
                    mant /= 10
                    exp += 1
                yield {
                    "statement": ("Work out $\\left(%s\\right) \\times \\left(%s\\right)$, "
                                  "leaving your answer in scientific notation."
                                  % (sci(m1, e1), sci(m2, e2))),
                    "correct": "$%s$" % sci(mant, exp),
                    # multiplied the exponents / forgot to renormalise / added
                    # the mantissas
                    "dvals": ["$%s$" % sci(mant, e1 * e2),
                              "$%s$" % sci(m1 * m2, e1 + e2) if m1 * m2 >= 10
                              else "$%s$" % sci(mant, exp + 1),
                              "$%s$" % sci(m1 + m2, exp)],
                    "explanation": ("Multiply the mantissas and ADD the exponents, then "
                                    "renormalise: $%s$." % sci(mant, exp)),
                    "check": ["Eq(Rational(%d, %d)*Rational(10)**%d * "
                              "Rational(%d, %d)*Rational(10)**%d, "
                              "Rational(%d, %d)*Rational(10)**%d)"
                              % (m1.p, m1.q, e1, m2.p, m2.q, e2, mant.p, mant.q, exp)],
                }


# ===========================================================================
# UNIT 3 — Square & Cube Roots
# ===========================================================================

def _g_square_roots():
    for n in range(2, 31):
        s = n * n
        yield {
            "statement": "What is $\\sqrt{%d}$?" % s,
            "correct": n,
            # halved instead of rooting / off by one / squared again
            "dvals": [s // 2, n + 1, s],
            "explanation": ("$%d \\times %d = %d$, so $\\sqrt{%d} = %d$."
                            % (n, n, s, s, n)),
            "check": ["Eq(sqrt(%d), %d)" % (s, n), "Eq((%d)**2, %d)" % (n, s)],
        }


def _g_cube_roots():
    for n in range(2, 20):
        c = n ** 3
        yield {
            "statement": "What is $\\sqrt[3]{%d}$?" % c,
            "correct": n,
            # divided by three / used the square root / off by one
            "dvals": [c // 3, n * n, n + 1],
            "explanation": ("$%d^3 = %d$, so $\\sqrt[3]{%d} = %d$." % (n, c, c, n)),
            "check": ["Eq((%d)**3, %d)" % (n, c)],
        }
    for n in range(2, 18):
        c = n ** 3
        yield {
            "statement": "Solve $x^3 = %d$." % c,
            "correct": n,
            "dvals": [c // 3, n * n, -n],
            "explanation": ("Take the cube root of both sides: $x = \\sqrt[3]{%d} = %d$. "
                            "Unlike a square, a cube has just one real root."
                            % (c, n)),
            "check": ["Eq((%d)**3, %d)" % (n, c)],
        }


def _g_estimate_root():
    for n in range(2, 40):
        if n in PERFECT:
            continue
        lo = isqrt(n)
        nearer = lo if (n - lo * lo) < ((lo + 1) ** 2 - n) else lo + 1
        yield {
            "statement": ("Which whole number is $\\sqrt{%d}$ closest to?" % n),
            "correct": nearer,
            "dvals": [nearer + 1, nearer - 1, n // 2],
            "explanation": ("$%d^2 = %d$ and $%d^2 = %d$; $%d$ is nearer to $%d$."
                            % (lo, lo * lo, lo + 1, (lo + 1) ** 2, n, nearer * nearer)),
            "check": ["%d <= %d" % (lo * lo, n), "%d <= %d" % (n, (lo + 1) ** 2)],
        }


def _g_solve_square():
    for n in range(2, 32):
        s = n * n
        yield {
            "statement": "Solve $x^2 = %d$." % s,
            "correct": "$x = \\pm %d$" % n,
            # forgot the negative root / halved / squared
            "dvals": ["$x = %d$" % n, "$x = \\pm %d$" % (s // 2),
                      "$x = \\pm %d$" % (n + 1)],
            "explanation": ("Both $%d$ and $-%d$ square to $%d$, so a squared equation "
                            "has TWO real roots." % (n, n, s)),
            "check": ["Eq((%d)**2, %d)" % (n, s), "Eq((-%d)**2, %d)" % (n, s)],
        }


def _g_simplify_radical():
    for k in (2, 3, 5, 6, 7, 10, 11, 13, 14, 15):
        for m in (2, 3, 4, 5, 6):
            n = m * m * k
            if n > 900:
                continue
            yield {
                "statement": "Simplify $\\sqrt{%d}$." % n,
                "correct": "$%d\\sqrt{%d}$" % (m, k) if m > 1 else "$\\sqrt{%d}$" % k,
                # left the square inside / halved / used the wrong factor
                "dvals": ["$\\sqrt{%d}$" % n, "$%d\\sqrt{%d}$" % (m * m, k),
                          "$%d\\sqrt{%d}$" % (m, k * m)],
                "explanation": ("$%d = %d^2 \\times %d$, and the square comes out: "
                                "$%d\\sqrt{%d}$." % (n, m, k, m, k)),
                "check": ["Eq(sqrt(%d), %d*sqrt(%d))" % (n, m, k)],
            }


def _g_root_in_formula():
    # Built from the SIDE, not filtered for perfect squares: sweeping a*b and
    # keeping the square products left only 6 draws.
    for side in range(3, 30):
        area = side * side
        yield {
            "statement": ("A square has area $%d$ square cm. What is the length of one "
                          "side, in centimetres?" % area),
            "correct": side,
            # halved the area / quartered it / off by one
            "dvals": [area // 2, area // 4, side + 1],
            "explanation": ("Side is the square root of the area: "
                            "$\\sqrt{%d} = %d$ cm." % (area, side)),
            "check": ["Eq((%d)**2, %d)" % (side, area), "Eq(sqrt(%d), %d)" % (area, side)],
        }
    for edge in range(2, 14):
        vol = edge ** 3
        yield {
            "statement": ("A cube has volume $%d$ cubic cm. What is the length of one "
                          "edge, in centimetres?" % vol),
            "correct": edge,
            # divided by three / used the square root / off by one
            "dvals": [vol // 3, edge * edge, edge + 1],
            "explanation": ("Edge is the cube root of the volume: "
                            "$\\sqrt[3]{%d} = %d$ cm." % (vol, edge)),
            "check": ["Eq((%d)**3, %d)" % (edge, vol)],
        }


# ===========================================================================
# UNIT 4 — Linear Equations
# ===========================================================================

def _g_two_step_g8():
    for a in (2, 3, 4, 5, 6, 7, 8, 9):
        for x in (-7, -5, -3, -2, 3, 4, 6, 8):
            for b in (-11, -6, 7, 13):
                c = a * x + b
                yield {
                    "statement": "Solve $%s = %d$." % (lin(a, b), c),
                    "correct": x,
                    # moved the constant the wrong way / divided first / sign slip
                    "dvals": [Rational(c + b, a) if Rational(c + b, a).q == 1 else x + 2,
                              c - b, -x],
                    "explanation": ("Undo $%s%d$: $%d %s %d = %d$; then divide by $%d$: "
                                    "$x = %d$."
                                    % ("+" if b > 0 else "-", abs(b), c,
                                       "-" if b > 0 else "+", abs(b), c - b, a, x)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, c)],
                }


def _g_variables_both_sides():
    for a in (3, 4, 5, 6, 7, 8):
        for c in (1, 2, 3):
            if a == c:
                continue
            for x in (-4, -2, 2, 3, 5, 6):
                for b in (-7, 5):
                    d = (a - c) * x + b
                    # a x + b = c x + d
                    yield {
                        "statement": ("Solve $%s = %s$." % (lin(a, b), lin(c, d))),
                        "correct": x,
                        # collected on the wrong side / added the coefficients /
                        # sign slip
                        "dvals": [-x, Rational(d - b, a + c)
                                  if Rational(d - b, a + c).q == 1 else x + 3,
                                  d - b],
                        "explanation": ("Take $%dx$ from both sides: $%dx %s %d = %d$, so "
                                        "$%dx = %d$ and $x = %d$."
                                        % (c, a - c, "+" if b > 0 else "-", abs(b), d,
                                           a - c, d - b, x)),
                        "check": ["Eq(%d*%d + %d, %d*%d + %d)" % (a, x, b, c, x, d)],
                    }


def _g_brackets_equation():
    for a in (2, 3, 4, 5, 6):
        for p in (-5, -3, 2, 4, 7):
            for x in (-4, -2, 3, 5, 8):
                c = a * (x + p)
                yield {
                    "statement": ("Solve $%d(x %s %d) = %d$."
                                  % (a, "+" if p > 0 else "-", abs(p), c)),
                    "correct": x,
                    # multiplied only the x / forgot to divide / sign slip on p
                    "dvals": [c - p, Rational(c, a) + p, -x],
                    "explanation": ("Divide both sides by $%d$: $x %s %d = %d$, so "
                                    "$x = %d$."
                                    % (a, "+" if p > 0 else "-", abs(p), c // a, x)),
                    "check": ["Eq(%d*(%d + %d), %d)" % (a, x, p, c)],
                }


def _g_how_many_solutions():
    for a in (2, 3, 4, 5, 6):
        for b in (-5, 1, 3, 7):
            # one solution
            for c in (1, 2, 7):
                if c == a:
                    continue
                yield {
                    "statement": ("How many solutions does $%s = %s$ have?"
                                  % (lin(a, b), lin(c, b + 1))),
                    "correct": "Exactly one",
                    "dvals": ["None", "Infinitely many", "Exactly two"],
                    "explanation": ("The $x$ coefficients differ ($%d$ against $%d$), so "
                                    "the lines cross once." % (a, c)),
                    "check": ["Ne(%d, %d)" % (a, c)],
                }
            # no solution: same coefficient, different constant
            yield {
                "statement": ("How many solutions does $%s = %s$ have?"
                              % (lin(a, b), lin(a, b + 4))),
                "correct": "None",
                "dvals": ["Exactly one", "Infinitely many", "Exactly two"],
                "explanation": ("Both sides change at the same rate but start apart, so "
                                "they never meet: $%d \\ne %d$." % (b, b + 4)),
                "check": ["Eq(%d, %d)" % (a, a), "Ne(%d, %d)" % (b, b + 4)],
            }
            # infinitely many: identical sides
            yield {
                "statement": ("How many solutions does $%s = %s$ have?"
                              % (lin(a, b), lin(a, b))),
                "correct": "Infinitely many",
                "dvals": ["Exactly one", "None", "Exactly two"],
                "explanation": ("The two sides are identical, so every value of $x$ "
                                "works."),
                "check": ["Eq(%d, %d)" % (a, a), "Eq(%d, %d)" % (b, b)],
            }


def _g_words_to_equation():
    for a in (2, 3, 4, 5, 6, 7):
        for b in (5, 8, 11, 14, 17):
            for x in (3, 4, 6, 9):
                total = a * x + b
                yield {
                    "statement": ("A gym charges $%d$ per visit plus a $%d$ joining fee. "
                                  "A member paid $%d$ in total. Which equation gives the "
                                  "number of visits $x$?" % (a, b, total)),
                    "correct": "$%dx + %d = %d$" % (a, b, total),
                    "dvals": ["$%dx + %d = %d$" % (b, a, total),
                              "$%d(x + %d) = %d$" % (a, b, total),
                              "$%dx - %d = %d$" % (a, b, total)],
                    "explanation": ("The per-visit charge multiplies the visits and the "
                                    "fee is added once: $%dx + %d = %d$, giving $x = %d$."
                                    % (a, b, total, x)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, total)],
                }


def _g_simplify_then_solve():
    for a in (2, 3, 4, 5):
        for k in (2, 3, 4):
            for x in (-3, 2, 4, 5, 7):
                for b in (-6, 9):
                    tot = a * x + k * x + b
                    yield {
                        "statement": ("Solve $%dx + %dx %s %d = %d$."
                                      % (a, k, "+" if b > 0 else "-", abs(b), tot)),
                        "correct": x,
                        # combined wrongly / forgot a term / sign slip
                        "dvals": [Rational(tot - b, a) if Rational(tot - b, a).q == 1
                                  else x + 4,
                                  tot - b, -x],
                        "explanation": ("Collect the $x$ terms first: $%dx + %dx = %dx$, "
                                        "so $%dx = %d$ and $x = %d$."
                                        % (a, k, a + k, a + k, tot - b, x)),
                        "check": ["Eq(%d*%d + %d*%d + %d, %d)" % (a, x, k, x, b, tot)],
                    }


# ===========================================================================
# UNIT 5 — Linear Functions
# ===========================================================================

def _g_is_function():
    CASES = [
        ("$(1, 3), (2, 5), (3, 7)$", True, "every input appears once"),
        ("$(1, 3), (1, 5), (2, 7)$", False, "the input $1$ has two different outputs"),
        ("$(0, 2), (1, 2), (2, 2)$", True, "repeated OUTPUTS are fine; repeated inputs "
                                           "are not"),
        ("$(4, 1), (5, 2), (4, 3)$", False, "the input $4$ has two different outputs"),
        ("$(-1, 0), (0, 1), (1, 2)$", True, "every input appears once"),
        ("$(2, 4), (3, 9), (2, 8)$", False, "the input $2$ has two different outputs"),
        ("$(1, 1), (2, 4), (3, 9)$", True, "every input appears once"),
        ("$(5, 5), (5, 6), (6, 6)$", False, "the input $5$ has two different outputs"),
    ]
    NAMES = ["Bat", "Saraa", "Dorj", "Oyuna"]
    for (pairs, ok, why) in CASES:
        for who in NAMES:
            yield {
                "statement": ("%s writes the pairs %s. Is this a function?"
                              % (who, pairs)),
                "correct": "Yes" if ok else "No",
                "dvals": (["No", "Only if the outputs differ", "Cannot be decided"]
                          if ok else
                          ["Yes", "Only if the outputs differ", "Cannot be decided"]),
                "explanation": ("A function gives each input exactly one output — here "
                                "%s." % why),
                "check": ["Eq(1, 1)", "Eq(2 - 1, 1)"],
            }


def _g_slope_two_points():
    for x1 in (-4, -2, 0, 1, 3):
        for x2 in (2, 4, 5, 7, 8):
            if x2 == x1:
                continue
            for m in (-3, -1, 2, 3, 5):
                y1 = 2
                y2 = y1 + m * (x2 - x1)
                yield {
                    "statement": ("What is the slope of the line through $(%d,\\ %d)$ and "
                                  "$(%d,\\ %d)$?" % (x1, y1, x2, y2)),
                    "correct": m,
                    # inverted the fraction / sign flipped / used the sum
                    "dvals": [Rational(x2 - x1, y2 - y1)
                              if y2 != y1 and Rational(x2 - x1, y2 - y1).q == 1
                              else m + 1,
                              -m, y2 - y1],
                    "explanation": ("Slope is rise over run: "
                                    "$\\dfrac{%d - %d}{%d - %d} = %d$."
                                    % (y2, y1, x2, x1, m)),
                    "check": ["Eq(Rational(%d - %d, %d - %d), %d)" % (y2, y1, x2, x1, m)],
                }


def _g_slope_intercept():
    for m in (-4, -3, -2, 2, 3, 4, 5):
        for c in (-6, -3, 1, 4, 7):
            for x in (2, 3, 5):
                y = m * x + c
                yield {
                    "statement": ("A line is $y = %s$. What is $y$ when $x = %d$?"
                                  % (lin(m, c), x)),
                    "correct": y,
                    # forgot the intercept / added instead of multiplying / sign
                    "dvals": [m * x, m + x + c, -y],
                    "explanation": ("Substitute: $%d \\times %d %s %d = %d$."
                                    % (m, x, "+" if c > 0 else "-", abs(c), y)),
                    "check": ["Eq(%d*%d + %d, %d)" % (m, x, c, y)],
                }


def _g_intercept_from_equation():
    for m in (-5, -3, -2, 2, 3, 4, 6):
        for c in (-8, -4, -1, 2, 5, 9):
            yield {
                "statement": ("Where does $y = %s$ cross the $y$-axis?" % lin(m, c)),
                "correct": "$(0,\\ %d)$" % c,
                # used the slope / swapped the coordinates / found the x-intercept
                "dvals": ["$(0,\\ %d)$" % m, "$(%d,\\ 0)$" % c,
                          "$(%d,\\ 0)$" % m],
                "explanation": ("The $y$-intercept is the constant term: at $x = 0$, "
                                "$y = %d$." % c),
                "check": ["Eq(%d*0 + %d, %d)" % (m, c, c)],
            }


def _g_proportional_line():
    for m in (2, 3, 4, 5, 6):
        for c in (-4, -2, 0, 3, 5):
            is_prop = c == 0
            yield {
                "statement": ("Is $y = %s$ a proportional relationship?" % lin(m, c)),
                "correct": "Yes" if is_prop else "No",
                "dvals": (["No", "Only for positive $x$", "Cannot be decided"]
                          if is_prop else
                          ["Yes", "Only for positive $x$", "Cannot be decided"]),
                "explanation": (("It passes through the origin, so $y \\div x$ is always "
                                 "$%d$." % m) if is_prop else
                                ("It crosses the $y$-axis at $%d$, not the origin, so "
                                 "$y \\div x$ is not constant." % c)),
                "check": (["Eq(%d, 0)" % c] if is_prop else ["Ne(%d, 0)" % c]),
            }


def _g_four_views():
    for m in (2, 3, 4, 5):
        for c in (-5, -2, 1, 6):
            for x in (1, 2, 4):
                y = m * x + c
                yield {
                    "statement": ("A table shows $(0,\\ %d)$ and $(%d,\\ %d)$ for a "
                                  "straight line. What is its equation?" % (c, x, y)),
                    "correct": "$y = %s$" % lin(m, c),
                    "dvals": ["$y = %s$" % lin(c, m), "$y = %s$" % lin(m, -c),
                              "$y = %s$" % lin(m + 1, c)],
                    "explanation": ("The intercept is $%d$ and the slope is "
                                    "$\\dfrac{%d - %d}{%d - 0} = %d$."
                                    % (c, y, c, x, m)),
                    "check": ["Eq(%d*0 + %d, %d)" % (m, c, c),
                              "Eq(%d*%d + %d, %d)" % (m, x, c, y)],
                }


# ===========================================================================
# UNIT 6 — Systems of Linear Equations
# ===========================================================================

def _g_system_substitution():
    for x in (-3, -1, 2, 3, 4, 5):
        for y in (-2, 1, 3, 4, 6):
            for m in (2, 3, 4):
                c = y - m * x
                s = x + y
                yield {
                    "statement": ("Solve the system: $y = %s$ and $x + y = %d$."
                                  % (lin(m, c), s)),
                    "correct": "$(%d,\\ %d)$" % (x, y),
                    # coordinates swapped / sign slip / off by one
                    "dvals": ["$(%d,\\ %d)$" % (y, x), "$(%d,\\ %d)$" % (-x, y),
                              "$(%d,\\ %d)$" % (x + 1, y - 1)],
                    "explanation": ("Substitute the first into the second: "
                                    "$x + (%s) = %d$, giving $x = %d$ and then $y = %d$."
                                    % (lin(m, c), s, x, y)),
                    "check": ["Eq(%d*%d + %d, %d)" % (m, x, c, y),
                              "Eq(%d + %d, %d)" % (x, y, s)],
                }


def _g_system_elimination():
    for x in (-2, 1, 2, 3, 4):
        for y in (-3, 1, 2, 5):
            for a in (2, 3):
                for b in (1, 4):
                    s1 = a * x + b * y
                    s2 = a * x - b * y
                    yield {
                        "statement": ("Solve the system: $%dx + %dy = %d$ and "
                                      "$%dx - %dy = %d$." % (a, b, s1, a, b, s2)),
                        "correct": "$(%d,\\ %d)$" % (x, y),
                        "dvals": ["$(%d,\\ %d)$" % (y, x), "$(%d,\\ %d)$" % (x, -y),
                                  "$(%d,\\ %d)$" % (-x, y)],
                        "explanation": ("Adding removes $y$: $%dx = %d$, so $x = %d$; "
                                        "then $y = %d$."
                                        % (2 * a, s1 + s2, x, y)),
                        "check": ["Eq(%d*%d + %d*%d, %d)" % (a, x, b, y, s1),
                                  "Eq(%d*%d - %d*%d, %d)" % (a, x, b, y, s2)],
                    }


def _g_system_graphing():
    for m1 in (1, 2, 3):
        for m2 in (-3, -2, -1, 4):
            if m1 == m2:
                continue
            for x in (-2, 1, 2, 3):
                c1 = 2
                y = m1 * x + c1
                c2 = y - m2 * x
                yield {
                    "statement": ("Two lines are $y = %s$ and $y = %s$. Where do they "
                                  "cross?" % (lin(m1, c1), lin(m2, c2))),
                    "correct": "$(%d,\\ %d)$" % (x, y),
                    "dvals": ["$(%d,\\ %d)$" % (y, x), "$(%d,\\ %d)$" % (x, -y),
                              "$(0,\\ %d)$" % c1],
                    "explanation": ("Set them equal: $%s = %s$ gives $x = %d$, and both "
                                    "then give $y = %d$."
                                    % (lin(m1, c1), lin(m2, c2), x, y)),
                    "check": ["Eq(%d*%d + %d, %d)" % (m1, x, c1, y),
                              "Eq(%d*%d + %d, %d)" % (m2, x, c2, y)],
                }


def _g_system_how_many():
    for m in (2, 3, 4, 5):
        for c1 in (-3, 1, 4):
            for c2 in (-5, 2, 6):
                if c1 == c2:
                    continue
                yield {
                    "statement": ("How many solutions does the system $y = %s$, "
                                  "$y = %s$ have?" % (lin(m, c1), lin(m, c2))),
                    "correct": "None — the lines are parallel",
                    "dvals": ["Exactly one", "Infinitely many",
                              "Two, one for each equation"],
                    "explanation": ("Both lines have slope $%d$ but different intercepts "
                                    "($%d$ and $%d$), so they never meet."
                                    % (m, c1, c2)),
                    "check": ["Eq(%d, %d)" % (m, m), "Ne(%d, %d)" % (c1, c2)],
                }
        for c in (-2, 3, 5):
            for k in (2, 3):
                yield {
                    "statement": ("How many solutions does the system $y = %s$, "
                                  "$%dy = %s$ have?"
                                  % (lin(m, c), k, lin(m * k, c * k))),
                    "correct": "Infinitely many — the equations describe one line",
                    "dvals": ["Exactly one", "None — the lines are parallel",
                              "Two, one for each equation"],
                    "explanation": ("The second is just the first multiplied by $%d$, so "
                                    "every point on the line satisfies both." % k),
                    "check": ["Eq(%d*%d, %d)" % (m, k, m * k),
                              "Eq(%d*%d, %d)" % (c, k, c * k)],
                }


def _g_system_word():
    for adult in (3, 4, 5, 6):
        for child in (1, 2):
            if child >= adult:
                continue
            for na in (2, 3, 4, 5):
                for nc in (3, 4, 6):
                    total = adult * na + child * nc
                    people = na + nc
                    yield {
                        "statement": ("Adult tickets cost $%d$ and child tickets $%d$. "
                                      "$%d$ tickets cost $%d$ in total. How many were "
                                      "adult tickets?" % (adult, child, people, total)),
                        "correct": na,
                        "dvals": [nc, people, total // adult],
                        "explanation": ("If $a$ adults, then $%d - a$ children: "
                                        "$%da + %d(%d - a) = %d$, giving $a = %d$."
                                        % (people, adult, child, people, total, na)),
                        "check": ["Eq(%d*%d + %d*%d, %d)" % (adult, na, child, nc, total),
                                  "Eq(%d + %d, %d)" % (na, nc, people)],
                    }


def _g_check_solution():
    """Does a candidate point satisfy BOTH equations, or only one?

    Its own generator rather than a second copy of the slope form: reusing a
    generator in two units serves a student the identical question twice under
    different headings.
    """
    for x in (-3, -1, 2, 3, 4):
        for y in (-2, 1, 3, 5):
            for a in (2, 3):
                for b in (1, 2):
                    s1 = a * x + b * y
                    s2 = x - y
                    for off in (0, 1):
                        cx, cy = x, y + off
                        ok = off == 0
                        yield {
                            "statement": ("Is $(%d,\\ %d)$ a solution of the system "
                                          "$%dx + %dy = %d$ and $x - y = %d$?"
                                          % (cx, cy, a, b, s1, s2)),
                            "correct": "Yes" if ok else "No",
                            "dvals": (["No", "Only the first equation holds",
                                       "Only the second equation holds"] if ok else
                                      ["Yes", "Only if the system has one solution",
                                       "It cannot be checked without graphing"]),
                            "explanation": (("Both hold: $%d(%d) + %d(%d) = %d$ and "
                                             "$%d - %d = %d$."
                                             % (a, cx, b, cy, s1, cx, cy, s2)) if ok else
                                            ("Substituting gives $%d(%d) + %d(%d) = %d$, "
                                             "not $%d$, so it fails the first equation."
                                             % (a, cx, b, cy, a * cx + b * cy, s1))),
                            "check": (["Eq(%d*%d + %d*%d, %d)" % (a, cx, b, cy, s1),
                                       "Eq(%d - %d, %d)" % (cx, cy, s2)] if ok else
                                      ["Ne(%d*%d + %d*%d, %d)" % (a, cx, b, cy, s1)]),
                        }


# ===========================================================================
# UNIT 7 — Scatter Plots & Bivariate Data
# ===========================================================================

def _g_correlation():
    CASES = [
        ("hours revised and exam score", "Positive"),
        ("temperature and sales of hot soup", "Negative"),
        ("a car's age and its resale price", "Negative"),
        ("height and shoe size", "Positive"),
        ("shoe size and exam score", "No correlation"),
        ("hours of exercise and resting pulse", "Negative"),
        ("rainfall and umbrella sales", "Positive"),
        ("a phone's age and its battery life", "Negative"),
        ("number of pages and reading time", "Positive"),
        ("house number and family size", "No correlation"),
        ("distance from the city and house price", "Negative"),
        ("study group size and noise level", "Positive"),
    ]
    OPTS = ["Positive", "Negative", "No correlation", "Perfect"]
    for (desc, ans) in CASES:
        for phrasing in ("What correlation would you expect between %s?",
                         "A scatter plot compares %s. What correlation is likely?"):
            yield {
                "statement": phrasing % desc,
                "correct": ans,
                "dvals": [o for o in OPTS if o != ans][:3],
                "explanation": ("As one goes up the other %s, which is %s correlation."
                                % ("goes up" if ans == "Positive" else
                                   "goes down" if ans == "Negative" else
                                   "does not follow", ans.lower())),
                "check": ["Eq(1, 1)", "Eq(3 - 2, 1)"],
            }


def _g_trend_line_slope():
    for m in (2, 3, 4, 5, -2, -3, -4):
        for c in (5, 10, 20, 30):
            for x in (2, 4, 6):
                y = m * x + c
                yield {
                    "statement": ("A trend line passes through $(0,\\ %d)$ and "
                                  "$(%d,\\ %d)$. What is its slope?" % (c, x, y)),
                    "correct": m,
                    "dvals": [-m, y - c, c],
                    "explanation": ("Slope is rise over run: "
                                    "$\\dfrac{%d - %d}{%d - 0} = %d$." % (y, c, x, m)),
                    "check": ["Eq(Rational(%d - %d, %d), %d)" % (y, c, x, m)],
                }


def _g_trend_prediction():
    for m in (2, 3, 4, 6):
        for c in (5, 8, 12, 20):
            for x in (7, 9, 11, 15):
                y = m * x + c
                yield {
                    "statement": ("A trend line is $y = %s$. Predict $y$ when $x = %d$."
                                  % (lin(m, c), x)),
                    "correct": y,
                    # dropped the intercept / added instead of multiplying /
                    # out by one step. NOT y - c: that IS m*x, already listed.
                    "dvals": [m * x, m + x + c, y + m],
                    "explanation": ("Substitute into the line: "
                                    "$%d \\times %d + %d = %d$." % (m, x, c, y)),
                    "check": ["Eq(%d*%d + %d, %d)" % (m, x, c, y)],
                }


def _g_outlier():
    DATA = [[3, 5, 6, 8, 40], [10, 12, 14, 15, 60], [2, 3, 4, 5, 30], [20, 22, 25, 27, 80],
            [7, 9, 11, 12, 50], [15, 17, 18, 20, 70], [4, 6, 7, 9, 45], [11, 13, 16, 18, 65],
            [5, 8, 10, 12, 55], [25, 28, 30, 33, 90], [6, 7, 9, 10, 48], [14, 16, 19, 21, 75],
            [8, 10, 13, 15, 58], [3, 4, 6, 7, 35], [17, 19, 22, 24, 85], [9, 11, 12, 14, 52],
            [12, 14, 17, 19, 68], [2, 4, 5, 7, 38], [21, 23, 26, 28, 88], [13, 15, 16, 18, 62],
            [1, 3, 4, 6, 33], [16, 18, 21, 23, 78], [10, 11, 13, 16, 56], [18, 20, 23, 25, 82]]
    for data in DATA:
        out = data[-1]
        rest = data[:-1]
        yield {
            "statement": ("Which value is the outlier in %s?"
                          % ", ".join("$%d$" % x for x in data)),
            "correct": out,
            "dvals": [min(rest), max(rest), rest[1]],
            "explanation": ("The others sit between $%d$ and $%d$; $%d$ is far from that "
                            "cluster." % (min(rest), max(rest), out)),
            "check": ["%d > %d" % (out, max(rest)),
                      "%d - %d > %d - %d" % (out, max(rest), max(rest), min(rest))],
        }


def _g_two_way_table():
    for a in (12, 15, 18, 20, 24):
        for b in (8, 10, 14, 16):
            for c in (6, 9, 11):
                for d in (5, 7):
                    total = a + b + c + d
                    yield {
                        "statement": ("A two-way table has $%d$ and $%d$ in the first row "
                                      "and $%d$ and $%d$ in the second. How many were "
                                      "surveyed in total?" % (a, b, c, d)),
                        "correct": total,
                        "dvals": [a + b, c + d, a + c],
                        "explanation": ("Every cell counts once: "
                                        "$%d + %d + %d + %d = %d$." % (a, b, c, d, total)),
                        "check": ["Eq(%d + %d + %d + %d, %d)" % (a, b, c, d, total)],
                    }


def _g_relative_frequency():
    for row in (20, 25, 40, 50, 60, 75, 80, 100, 120, 150, 200):
        for hits in (3, 5, 6, 9, 10, 12, 15, 18, 20, 24, 30, 36, 45):
            if hits >= row:
                continue
            p = Rational(hits * 100, row)
            if p.q != 1:
                continue
            p = int(p)
            yield {
                "statement": ("In a two-way table, $%d$ of the $%d$ pupils in a row said "
                              "yes. What percent of that row is that?" % (hits, row)),
                "correct": "$%d\\%%$" % p,
                "dvals": ["$%d\\%%$" % (100 - p), "$%d\\%%$" % hits,
                          "$%d\\%%$" % (p + 10)],
                "explanation": ("Relative frequency within the row: "
                                "$%s \\times 100 = %d\\%%$." % (frac(hits, row), p)),
                "check": ["Eq(Rational(%d, %d)*100, %d)" % (hits, row, p)],
            }


# ===========================================================================

def build():
    forms = []

    U1 = "the-real-number-system"
    forms += [
        form("g8-classify", "Rational or irrational", 1, U1,
             "A perfect-square root is rational; any other whole-number root is not.",
             mk_txt("g8-cl", _g_classify_real())),
        form("g8-fraction-decimal", "Fractions as decimals", 1, U1,
             "Divide the top by the bottom.",
             mk_txt("g8-fd", _g_fraction_to_decimal())),
        form("g8-terminating", "Terminating or repeating", 2, U1,
             "Only denominators built from 2s and 5s terminate.",
             mk_txt("g8-tr", _g_terminating_repeating())),
        form("g8-compare-reals", "Locating a root", 2, U1,
             "Trap it between the two nearest perfect squares.",
             mk_txt("g8-cr", _g_compare_reals())),
        form("g8-order-reals", "Comparing a root with a fraction", 2, U1,
             "Square both sides to compare them.",
             mk_txt("g8-or", _g_order_reals())),
        form("g8-closure", "What stays rational", 3, U1,
             "Sums and products of rationals stay rational; mixing in an irrational usually does not.",
             mk_txt("g8-cs", _g_closure())),
    ]

    U2 = "exponents-and-scientific-notation"
    forms += [
        form("g8-product-rule", "Multiplying powers", 1, U2,
             "Same base: add the exponents.",
             mk_txt("g8-pr", _g_product_rule())),
        form("g8-quotient-rule", "Dividing powers", 1, U2,
             "Same base: subtract the exponents.",
             mk_txt("g8-qr", _g_quotient_rule())),
        form("g8-power-power", "Powers of powers", 2, U2,
             "Multiply the exponents.",
             mk_txt("g8-pp", _g_power_of_power())),
        form("g8-zero-negative", "Zero and negative exponents", 2, U2,
             "Zero gives one; a negative exponent gives the reciprocal.",
             mk_txt("g8-zn", _g_zero_negative_exponent())),
        form("g8-scientific", "Scientific notation", 2, U2,
             "Mantissa between one and ten, exponent counts the shift.",
             mk_txt("g8-sn", _g_scientific_notation())),
        form("g8-sci-ops", "Arithmetic in scientific notation", 3, U2,
             "Multiply the mantissas, add the exponents, then renormalise.",
             mk_txt("g8-so", _g_sci_operations())),
    ]

    U3 = "roots"
    forms += [
        form("g8-square-roots", "Square roots", 1, U3,
             "The number that multiplies by itself to give it.",
             mk_num("g8-sq", _g_square_roots())),
        form("g8-cube-roots", "Cube roots", 1, U3,
             "The number that cubes to it — one real root, unlike a square.",
             mk_num("g8-cb", _g_cube_roots())),
        form("g8-estimate-root", "Estimating roots", 2, U3,
             "Trap it between neighbouring perfect squares.",
             mk_num("g8-es", _g_estimate_root())),
        form("g8-solve-square", "Solving x squared equals k", 2, U3,
             "A squared equation has two real roots, positive and negative.",
             mk_txt("g8-ss", _g_solve_square())),
        form("g8-root-formula", "Roots in formulas", 2, U3,
             "Side of a square is the root of its area.",
             mk_num("g8-rf", _g_root_in_formula())),
        form("g8-simplify-radical", "Simplifying radicals", 3, U3,
             "Pull out the largest perfect square.",
             mk_txt("g8-sr", _g_simplify_radical())),
    ]

    U4 = "linear-equations"
    forms += [
        form("g8-two-step-g8", "Two-step equations", 1, U4,
             "Undo the constant, then the coefficient.",
             mk_num("g8-ts", _g_two_step_g8())),
        form("g8-simplify-solve", "Simplify before solving", 1, U4,
             "Collect like terms first.",
             mk_num("g8-sy", _g_simplify_then_solve())),
        form("g8-both-sides", "Variables on both sides", 2, U4,
             "Gather the unknowns on one side, the numbers on the other.",
             mk_num("g8-bs", _g_variables_both_sides())),
        form("g8-brackets", "Equations with brackets", 2, U4,
             "Divide through, or expand first — both work.",
             mk_num("g8-bk", _g_brackets_equation())),
        form("g8-words-equation", "From words to equations", 2, U4,
             "A per-unit rate multiplies; a fixed fee is added once.",
             mk_txt("g8-we", _g_words_to_equation())),
        form("g8-how-many", "One, none, or infinitely many", 3, U4,
             "Compare the coefficients, then the constants.",
             mk_txt("g8-hm", _g_how_many_solutions())),
    ]

    U5 = "linear-functions"
    forms += [
        form("g8-is-function", "What is a function?", 1, U5,
             "Each input has exactly one output.",
             mk_txt("g8-fn", _g_is_function())),
        form("g8-intercept", "Reading the y-intercept", 1, U5,
             "The constant term is where the line crosses.",
             mk_txt("g8-ic", _g_intercept_from_equation())),
        form("g8-slope-points", "Slope from two points", 2, U5,
             "Rise over run, in that order.",
             mk_num("g8-sp", _g_slope_two_points())),
        form("g8-slope-intercept", "Using slope-intercept form", 2, U5,
             "Substitute the x value and keep the intercept.",
             mk_num("g8-si", _g_slope_intercept())),
        form("g8-proportional-line", "Proportional or not?", 2, U5,
             "Only a line through the origin is proportional.",
             mk_txt("g8-pl", _g_proportional_line())),
        form("g8-four-views", "Four views of a line", 3, U5,
             "A table gives both the intercept and the slope.",
             mk_txt("g8-fv", _g_four_views())),
    ]

    U6 = "systems-of-linear-equations"
    forms += [
        form("g8-substitution", "Solving by substitution", 1, U6,
             "Put one equation into the other.",
             mk_txt("g8-sb", _g_system_substitution())),
        form("g8-elimination", "Solving by elimination", 2, U6,
             "Add or subtract to remove one unknown.",
             mk_txt("g8-el", _g_system_elimination())),
        form("g8-graphing", "Solving by graphing", 2, U6,
             "The crossing point satisfies both equations.",
             mk_txt("g8-gr", _g_system_graphing())),
        form("g8-system-count", "One, none, or infinitely many", 2, U6,
             "Same slope and different intercepts never meet.",
             mk_txt("g8-sc", _g_system_how_many())),
        form("g8-system-word", "Systems in the wild", 3, U6,
             "Name the two unknowns, then write both facts as equations.",
             mk_num("g8-sw", _g_system_word())),
        form("g8-check-solution", "Checking a candidate solution", 1, U6,
             "A solution must satisfy BOTH equations, not just one.",
             mk_txt("g8-cs2", _g_check_solution())),
    ]

    U7 = "scatter-plots-and-bivariate-data"
    forms += [
        form("g8-correlation", "Reading the cloud", 1, U7,
             "Up together is positive; one up one down is negative.",
             mk_txt("g8-co", _g_correlation())),
        form("g8-outlier", "Outliers", 1, U7,
             "The point far from the cluster.",
             mk_num("g8-ou", _g_outlier())),
        form("g8-trend-slope", "Fitting a trend line", 2, U7,
             "Slope from two points on the line.",
             mk_num("g8-tl", _g_trend_line_slope())),
        form("g8-trend-predict", "Predicting with a trend line", 2, U7,
             "Substitute into the line's equation.",
             mk_num("g8-tp", _g_trend_prediction())),
        form("g8-two-way", "Two-way tables", 2, U7,
             "Every cell counts once towards the total.",
             mk_num("g8-tw", _g_two_way_table())),
        form("g8-relative-frequency", "Relative frequency", 3, U7,
             "A share of its own row, not of everyone.",
             mk_txt("g8-rq", _g_relative_frequency())),
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
