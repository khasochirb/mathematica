# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 11 — mirrors /math/11.

One collection PER UNIT across the seven Grade 11 topics.

Every answer is COMPUTED from a parameter sweep and carries a sympy check.
Trigonometric values stay exact (sqrt(3)/2, never 0.866), logarithms are
built from exact powers, and complex arithmetic is checked with sympy's I.

Self-check:  python3 scripts/pb/grade11.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys
from math import gcd

from sympy import Rational

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt  # noqa: E402

SLUG = "11"
TITLE = "Grade 11"
TITLE_MN = "11-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 11 year — functions and "
         "transformations, polynomial functions, logarithms, sequences and "
         "series, trigonometry and the unit circle, complex numbers, and "
         "statistics.")

UNITS = [
    {"id": "functions-and-transformations", "title": "Functions & Transformations",
     "blurb": "Function notation, domain and range, shifts, stretches and reflections, and inverse functions."},
    {"id": "polynomial-functions", "title": "Polynomial Functions",
     "blurb": "End behaviour, zeros and factors, multiplicity, and the remainder and factor theorems."},
    {"id": "logarithms", "title": "Logarithms",
     "blurb": "Evaluating logarithms, the log laws, and solving exponential and logarithmic equations."},
    {"id": "sequences-and-series", "title": "Sequences & Series",
     "blurb": "Arithmetic and geometric sequences, their sums, and infinite geometric series."},
    {"id": "trigonometry-and-the-unit-circle", "title": "Trigonometry & the Unit Circle",
     "blurb": "Radians, the unit circle, special angles, sine and cosine waves and their transformations."},
    {"id": "complex-numbers", "title": "Complex Numbers",
     "blurb": "The imaginary unit, arithmetic in a + bi form, conjugates and division, and complex roots."},
    {"id": "statistics-and-data", "title": "Statistics & Data",
     "blurb": "Mean against median, spread and standard deviation, z-scores and the normal model."},
]


def frac(a, b):
    return "\\frac{%d}{%d}" % (a, b)


def lin(m, c, var="x"):
    if m == 0:
        return str(c)
    s = var if m == 1 else ("-" + var if m == -1 else "%d%s" % (m, var))
    if c > 0:
        s += " + %d" % c
    elif c < 0:
        s += " - %d" % (-c)
    return s


def xp(p):
    """(x + p) with the sign folded in: (x - 5), never (x + -5)."""
    return "(x + %d)" % p if p > 0 else ("(x - %d)" % -p if p < 0 else "x")


def cx(a, b):
    """A complex number a + bi, rendered the way a textbook writes it."""
    if b == 0:
        return str(a)
    if a == 0:
        return "i" if b == 1 else ("-i" if b == -1 else "%di" % b)
    bi = "i" if b == 1 else ("i" if b == -1 else "%di" % abs(b))
    return "%d %s %s" % (a, "+" if b > 0 else "-", bi)


# ===========================================================================
# UNIT 1 — Functions & Transformations
# ===========================================================================

def _g_function_notation():
    for a in (2, 3, 4, 5, 6):
        for b in (-7, -3, 1, 4, 8):
            for x in (-3, -1, 2, 5, 7):
                v = a * x + b
                yield {
                    "statement": ("If $f(x) = %s$, what is $f(%d)$?" % (lin(a, b), x)),
                    "correct": v,
                    # multiplied f by x / forgot the constant / sign slip
                    "dvals": [a * b + x, a * x, -v],
                    "explanation": ("Substitute $x = %d$: $%d(%d) %s %d = %d$."
                                    % (x, a, x, "+" if b > 0 else "-", abs(b), v)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, v)],
                }


def _g_domain_range():
    CASES = []
    for k in range(1, 16):
        CASES.append(("\\dfrac{1}{x - %d}" % k, "$x \\ne %d$" % k,
                      "the denominator is zero at $x = %d$" % k,
                      ["Eq(%d - %d, 0)" % (k, k)]))
    for k in range(1, 16):
        CASES.append(("\\sqrt{x - %d}" % k, "$x \\ge %d$" % k,
                      "a square root needs a non-negative inside, so $x - %d \\ge 0$" % k,
                      ["Eq(%d - %d, 0)" % (k, k)]))
    for (expr, ans, why, chk) in CASES:
        yield {
            "statement": "What is the domain of $f(x) = %s$?" % expr,
            "correct": ans,
            "dvals": [o for o in ("All real numbers", "$x > 0$", "$x \\le 0$",
                                  "$x \\ne 0$") if o != ans][:3],
            "explanation": ("The domain excludes anything that breaks the rule: %s."
                            % why),
            "check": chk,
        }


def _g_shifts():
    for h in (-6, -4, -3, -2, 2, 3, 4, 6):
        for k in (-5, -2, 3, 7):
            yield {
                "statement": ("How is $y = (x %s %d)^2 %s %d$ moved from $y = x^2$?"
                              % ("-" if h > 0 else "+", abs(h),
                                 "+" if k > 0 else "-", abs(k))),
                "correct": ("%d %s and %d %s"
                            % (abs(h), "right" if h > 0 else "left",
                               abs(k), "up" if k > 0 else "down")),
                # horizontal direction flipped / axes swapped / both flipped
                "dvals": [("%d %s and %d %s"
                           % (abs(h), "left" if h > 0 else "right",
                              abs(k), "up" if k > 0 else "down")),
                          ("%d %s and %d %s"
                           % (abs(k), "right" if k > 0 else "left",
                              abs(h), "up" if h > 0 else "down")),
                          ("%d %s and %d %s"
                           % (abs(h), "left" if h > 0 else "right",
                              abs(k), "down" if k > 0 else "up"))],
                "explanation": ("Inside the bracket the shift is OPPOSITE to the sign, so "
                                "$x %s %d$ moves %d %s; the $%s%d$ outside moves it "
                                "%d %s."
                                % ("-" if h > 0 else "+", abs(h), abs(h),
                                   "right" if h > 0 else "left",
                                   "+" if k > 0 else "-", abs(k), abs(k),
                                   "up" if k > 0 else "down")),
                "check": ["Eq((%d - %d)**2 + %d, %d)" % (h, h, k, k)],
            }


def _g_stretch_reflect():
    for a in (-4, -3, -2, 2, 3, 4, 5):
        yield {
            "statement": "How does $y = %dx^2$ differ from $y = x^2$?" % a,
            "correct": ("Stretched by %d%s" % (abs(a), " and reflected in the $x$-axis"
                                               if a < 0 else "")),
            "dvals": [("Stretched by %d%s" % (abs(a), "" if a < 0
                                              else " and reflected in the $x$-axis")),
                      "Shifted %d up" % abs(a),
                      "Compressed by %d" % abs(a)],
            "explanation": ("Multiplying the whole function by $%d$ stretches it by a "
                            "factor of $%d$%s."
                            % (a, abs(a), " and flips it, because the factor is negative"
                               if a < 0 else "")),
            "check": ["Eq(%d*2**2, %d)" % (a, a * 4)],
        }
    for a in (2, 3, 4, 5, 6, 8, 10):
        for x in (2, 3, 4):
            yield {
                "statement": ("If $g(x) = %d f(x)$ and $f(%d) = %d$, what is $g(%d)$?"
                              % (a, x, x, x)),
                "correct": a * x,
                "dvals": [a + x, x, a * x + a],
                "explanation": ("A vertical stretch multiplies the OUTPUT: "
                                "$g(%d) = %d \\times %d = %d$." % (x, a, x, a * x)),
                "check": ["Eq(%d*%d, %d)" % (a, x, a * x)],
            }


def _g_combined_transformation():
    for a in (-3, -2, 2, 3):
        for h in (-4, -2, 1, 3, 5):
            for k in (-6, 2, 7):
                yield {
                    "statement": ("What is the vertex of $y = %d(x %s %d)^2 %s %d$?"
                                  % (a, "-" if h > 0 else "+", abs(h),
                                     "+" if k > 0 else "-", abs(k))),
                    "correct": "$(%d,\\ %d)$" % (h, k),
                    "dvals": ["$(%d,\\ %d)$" % (-h, k), "$(%d,\\ %d)$" % (k, h),
                              "$(%d,\\ %d)$" % (h, a)],
                    "explanation": ("The stretch by $%d$ does not move the vertex; it "
                                    "stays at $(h,\\ k) = (%d,\\ %d)$." % (a, h, k)),
                    "check": ["Eq(%d*(%d - %d)**2 + %d, %d)" % (a, h, h, k, k)],
                }


def _g_inverse():
    for m in (2, 3, 4, 5, 6, 7):
        for c in (-9, -5, -2, 3, 8, 11):
            yield {
                "statement": "If $f(x) = %s$, what is $f^{-1}(x)$?" % lin(m, c),
                "correct": "$\\dfrac{x %s %d}{%d}$" % ("-" if c > 0 else "+", abs(c), m),
                # forgot to undo one step / order swapped / sign kept
                "dvals": ["$\\dfrac{x}{%d} %s %d$" % (m, "-" if c > 0 else "+", abs(c)),
                          "$\\dfrac{x %s %d}{%d}$" % ("+" if c > 0 else "-", abs(c), m),
                          "$%s$" % lin(m, -c)],
                "explanation": ("Swap $x$ and $y$ and solve: $x = %dy %s %d$ gives "
                                "$y = \\dfrac{x %s %d}{%d}$."
                                % (m, "+" if c > 0 else "-", abs(c),
                                   "-" if c > 0 else "+", abs(c), m)),
                "check": ["Eq((%d*3 + %d - %d)/%d, 3)" % (m, c, c, m)],
            }


# ===========================================================================
# UNIT 2 — Polynomial Functions
# ===========================================================================

def _g_end_behaviour():
    for deg in (2, 3, 4, 5, 6, 7):
        for lead in (-3, -2, -1, 1, 2, 3):
            even = deg % 2 == 0
            pos = lead > 0
            if even:
                ans = ("Both ends up" if pos else "Both ends down")
            else:
                ans = ("Down on the left, up on the right" if pos
                       else "Up on the left, down on the right")
            OPTS = ["Both ends up", "Both ends down",
                    "Down on the left, up on the right",
                    "Up on the left, down on the right"]
            yield {
                "statement": ("What is the end behaviour of a polynomial with degree $%d$ "
                              "and leading coefficient $%d$?" % (deg, lead)),
                "correct": ans,
                "dvals": [o for o in OPTS if o != ans][:3],
                "explanation": ("An %s degree with a %s leading coefficient gives %s."
                                % ("even" if even else "odd",
                                   "positive" if pos else "negative", ans.lower())),
                "check": ["Eq(Mod(%d, 2), %d)" % (deg, 0 if even else 1)]
                         + (["%d > 0" % lead] if pos else ["%d < 0" % lead]),
            }


def _g_zeros_from_factors():
    TRIPLES = [(1, 2, 3), (-1, 2, 4), (1, -3, 5), (2, 3, -4), (-2, 1, 6), (3, 4, -5),
               (1, 5, -2), (-3, 2, 7), (4, -1, 3), (2, -5, 6), (1, 4, 8), (-4, 3, 5),
               (2, 6, -3), (1, -6, 7), (5, 2, -1), (3, -2, 9), (1, 3, 10), (-5, 4, 2),
               (6, 1, -3), (2, 8, -5), (7, -2, 3), (1, 9, -4), (4, 5, -6), (3, 7, 2),
               (-1, 8, 5), (2, 4, 9), (6, -3, 1), (5, 7, -2)]
    for (a, b, c) in TRIPLES:
        roots = sorted([-a, -b, -c])
        yield {
            "statement": ("What are the zeros of $f(x) = %s%s%s$?"
                          % (xp(a), xp(b), xp(c))),
            "correct": "$%d$, $%d$, $%d$" % tuple(roots),
            # signs not flipped / only two / one sign wrong
            "dvals": ["$%d$, $%d$, $%d$" % (a, b, c),
                      "$%d$, $%d$" % (roots[0], roots[1]),
                      "$%d$, $%d$, $%d$" % (roots[0], roots[1], -roots[2])],
            "explanation": ("Each factor is zero when $x$ is the OPPOSITE of the number "
                            "inside, giving $%d$, $%d$ and $%d$." % tuple(roots)),
            "check": ["Eq((%d + %d)*(%d + %d)*(%d + %d), 0)"
                      % (roots[0], a, roots[0], b, roots[0], c)],
        }


def _g_multiplicity():
    for r in (-4, -3, -2, -1, 1, 2, 3, 4):
        for m in (1, 2, 3):
            crosses = m % 2 == 1
            yield {
                "statement": ("A polynomial has the factor $(x %s %d)^{%d}$. Does the "
                              "graph cross or touch the $x$-axis there?"
                              % ("-" if r > 0 else "+", abs(r), m)),
                "correct": "Crosses" if crosses else "Touches and turns back",
                "dvals": ["Touches and turns back" if crosses else "Crosses",
                          "It never reaches the axis",
                          "It depends on the leading coefficient"],
                "explanation": ("Multiplicity $%d$ is %s, so the graph %s at $x = %d$."
                                % (m, "odd" if crosses else "even",
                                   "crosses" if crosses else "touches and turns back", r)),
                "check": ["Eq(Mod(%d, 2), %d)" % (m, 1 if crosses else 0)],
            }


def _g_remainder_theorem():
    for a in (1, 2, 3):
        for b in (-6, -3, 2, 5, 8):
            for c in (-9, -4, 1, 7):
                for k in (-3, -1, 2, 4):
                    v = a * k * k + b * k + c
                    yield {
                        "statement": ("What is the remainder when $%dx^2 %s %dx %s %d$ "
                                      "is divided by $x %s %d$?"
                                      % (a, "+" if b > 0 else "-", abs(b),
                                         "+" if c > 0 else "-", abs(c),
                                         "-" if k > 0 else "+", abs(k))),
                        "correct": v,
                        # used -k / used the constant / sign flipped
                        "dvals": [a * k * k - b * k + c, c, -v],
                        "explanation": ("The remainder theorem: substitute $x = %d$. "
                                        "$%d(%d)^2 %s %d(%d) %s %d = %d$."
                                        % (k, a, k, "+" if b > 0 else "-", abs(b), k,
                                           "+" if c > 0 else "-", abs(c), v)),
                        "check": ["Eq(%d*(%d)**2 + %d*%d + %d, %d)" % (a, k, b, k, c, v)],
                    }


def _g_factor_theorem():
    for r in (-5, -4, -3, -2, -1, 1, 2, 3, 4, 5):
        for s in (-6, -2, 3, 7):
            if r == s:
                continue
            b, c = -(r + s), r * s
            yield {
                "statement": ("Is $x %s %d$ a factor of $x^2 %s %dx %s %d$?"
                              % ("-" if r > 0 else "+", abs(r),
                                 "+" if b > 0 else "-", abs(b),
                                 "+" if c > 0 else "-", abs(c))),
                "correct": "Yes",
                "dvals": ["No", "Only if the remainder is $1$",
                          "It cannot be decided without dividing"],
                "explanation": ("Substituting $x = %d$ gives $%d$, and a zero remainder "
                                "means it IS a factor." % (r, 0)),
                "check": ["Eq((%d)**2 + %d*%d + %d, 0)" % (r, b, r, c)],
            }


def _g_polynomial_value():
    for a in (1, 2, 3):
        for b in (-5, -2, 4, 6):
            for c in (-8, 3, 9):
                for x in (-2, 1, 3):
                    v = a * x ** 3 + b * x + c
                    yield {
                        "statement": ("If $f(x) = %dx^3 %s %dx %s %d$, what is $f(%d)$?"
                                      % (a, "+" if b > 0 else "-", abs(b),
                                         "+" if c > 0 else "-", abs(c), x)),
                        "correct": v,
                        # cubed after multiplying / squared instead / sign
                        "dvals": [(a * x) ** 3 + b * x + c, a * x ** 2 + b * x + c, -v],
                        "explanation": ("Cube first, then multiply: $%d(%d)^3 = %d$, and "
                                        "the rest gives $%d$."
                                        % (a, x, a * x ** 3, v)),
                        "check": ["Eq(%d*(%d)**3 + %d*%d + %d, %d)" % (a, x, b, x, c, v)],
                    }


# ===========================================================================
# UNIT 3 — Logarithms
# ===========================================================================

def _g_evaluate_log():
    for b in (2, 3, 4, 5, 6, 7, 10):
        for e in range(1, 7):
            v = b ** e
            if v > 10 ** 6:
                continue
            yield {
                "statement": "Evaluate $\\log_{%d} %d$." % (b, v),
                "correct": e,
                # divided instead / used the value / off by one
                "dvals": [v // b, v, e + 1],
                "explanation": ("Ask what power of $%d$ gives $%d$: $%d^{%d} = %d$, so "
                                "the logarithm is $%d$." % (b, v, b, e, v, e)),
                "check": ["Eq((%d)**%d, %d)" % (b, e, v)],
            }


def _g_log_laws():
    for b in (2, 3, 5, 10):
        for m in range(1, 6):
            for n in range(1, 6):
                if m == n:
                    continue
                yield {
                    "statement": ("Simplify $\\log_{%d} %d + \\log_{%d} %d$."
                                  % (b, b ** m, b, b ** n)),
                    "correct": m + n,
                    # multiplied the logs / subtracted / used one only
                    "dvals": [m * n, abs(m - n), m],
                    "explanation": ("A sum of logs is the log of the product: "
                                    "$\\log_{%d}(%d \\times %d) = \\log_{%d} %d = %d$."
                                    % (b, b ** m, b ** n, b, b ** (m + n), m + n)),
                    "check": ["Eq((%d)**%d * (%d)**%d, (%d)**%d)"
                              % (b, m, b, n, b, m + n)],
                }


def _g_log_power_law():
    for b in (2, 3, 5, 10):
        for m in range(1, 5):
            for k in (2, 3, 4):
                yield {
                    "statement": ("Simplify $%d\\log_{%d} %d$." % (k, b, b ** m)),
                    "correct": k * m,
                    # added instead / used m only / used k only
                    "dvals": [k + m, m, k],
                    "explanation": ("The power law brings the coefficient inside: "
                                    "$%d\\log_{%d} %d = \\log_{%d} %d^{%d} = %d$."
                                    % (k, b, b ** m, b, b ** m, k, k * m)),
                    "check": ["Eq(((%d)**%d)**%d, (%d)**%d)" % (b, m, k, b, k * m)],
                }


def _g_solve_exponential():
    for b in (2, 3, 4, 5, 6, 7, 10):
        for e in range(1, 7):
            v = b ** e
            if v > 10 ** 6:
                continue
            yield {
                "statement": "Solve $%d^{x} = %d$." % (b, v),
                "correct": e,
                # divided / used the value / off by one
                "dvals": [v // b, v, e + 1],
                "explanation": ("Write both sides as powers of $%d$: $%d^{x} = %d^{%d}$, "
                                "so $x = %d$." % (b, b, b, e, e)),
                "check": ["Eq((%d)**%d, %d)" % (b, e, v)],
            }


def _g_solve_log_equation():
    for b in (2, 3, 4, 5, 6, 7, 8, 9, 10):
        for e in range(1, 7):
            v = b ** e
            if v > 10 ** 6:
                continue
            yield {
                "statement": "Solve $\\log_{%d} x = %d$." % (b, e),
                "correct": v,
                # multiplied instead of raising / swapped base and exponent
                "dvals": [b * e, e ** b, v + b],
                "explanation": ("A logarithm equation undoes into a power: "
                                "$x = %d^{%d} = %d$." % (b, e, v)),
                "check": ["Eq((%d)**%d, %d)" % (b, e, v)],
            }


def _g_log_scale():
    for d in range(1, 8):
        factor = 10 ** d
        yield {
            "statement": ("On a base-$10$ log scale, two readings differ by $%d$. "
                          "How many times larger is one than the other?" % d),
            "correct": factor,
            # multiplied instead of raising / added / used the difference
            "dvals": [10 * d, d, factor // 10 if d > 1 else 100],
            "explanation": ("Each step on a log scale multiplies by $10$, so $%d$ steps "
                            "means $10^{%d} = %d$ times." % (d, d, factor)),
            "check": ["Eq(10**%d, %d)" % (d, factor)],
        }
    for b in (2, 3, 5, 6, 7):
        for e in range(1, 9):
            yield {
                "statement": ("A quantity multiplies by $%d$ each step. After $%d$ steps, "
                              "by what factor has it grown?" % (b, e)),
                "correct": b ** e,
                "dvals": [b * e, b + e, b ** (e + 1)],
                "explanation": ("Repeated multiplication is a power: $%d^{%d} = %d$."
                                % (b, e, b ** e)),
                "check": ["Eq((%d)**%d, %d)" % (b, e, b ** e)],
            }


# ===========================================================================
# UNIT 4 — Sequences & Series
# ===========================================================================

def _g_arithmetic_term():
    for a in (-8, -3, 2, 5, 7, 11):
        for d in (-6, -4, 3, 4, 6, 9):
            for n in (5, 8, 10, 12, 15, 20):
                v = a + (n - 1) * d
                yield {
                    "statement": ("An arithmetic sequence starts at $%d$ with common "
                                  "difference $%d$. What is the $%d$th term?" % (a, d, n)),
                    "correct": v,
                    # used n instead of n-1 / added d once / dropped the start
                    "dvals": [a + n * d, a + d, (n - 1) * d],
                    "explanation": ("The $n$th term is $a + (n-1)d = %d + %d \\times %d "
                                    "= %d$." % (a, n - 1, d, v)),
                    "check": ["Eq(%d + (%d - 1)*%d, %d)" % (a, n, d, v)],
                }


def _g_geometric_term():
    for a in (1, 2, 3, 5, 7):
        for r in (2, 3, -2, 4):
            for n in (4, 5, 6, 7):
                v = a * r ** (n - 1)
                if abs(v) > 10 ** 6:
                    continue
                yield {
                    "statement": ("A geometric sequence starts at $%d$ with common ratio "
                                  "$%d$. What is the $%d$th term?" % (a, r, n)),
                    "correct": v,
                    # used n instead of n-1 / multiplied instead of raising
                    "dvals": [a * r ** n, a * r * (n - 1), a + r ** (n - 1)],
                    "explanation": ("The $n$th term is $ar^{n-1} = %d \\times %d^{%d} "
                                    "= %d$." % (a, r, n - 1, v)),
                    "check": ["Eq(%d*(%d)**(%d - 1), %d)" % (a, r, n, v)],
                }


def _g_arithmetic_series():
    for a in (1, 2, 3, 5, 8):
        for d in (2, 3, 4, 5, 7):
            for n in (6, 8, 10, 12, 15):
                last = a + (n - 1) * d
                s = Rational(n * (a + last), 2)
                if s.q != 1:
                    continue
                s = int(s)
                yield {
                    "statement": ("Find the sum of the first $%d$ terms of the arithmetic "
                                  "sequence starting at $%d$ with difference $%d$."
                                  % (n, a, d)),
                    "correct": s,
                    # forgot to halve / summed only the last term / used n-1
                    "dvals": [n * (a + last), last, s - last],
                    "explanation": ("The last term is $%d$, and the sum is "
                                    "$\\dfrac{%d(%d + %d)}{2} = %d$."
                                    % (last, n, a, last, s)),
                    "check": ["Eq(Rational(%d*(%d + %d), 2), %d)" % (n, a, last, s),
                              "Eq(%d + (%d - 1)*%d, %d)" % (a, n, d, last)],
                }


def _g_geometric_series():
    for a in (1, 2, 3, 5):
        for r in (2, 3, 4):
            for n in (3, 4, 5, 6):
                s = a * (r ** n - 1) // (r - 1)
                if s > 10 ** 6:
                    continue
                yield {
                    "statement": ("Find the sum of the first $%d$ terms of the geometric "
                                  "sequence starting at $%d$ with ratio $%d$."
                                  % (n, a, r)),
                    "correct": s,
                    # used the nth term only / forgot to divide / off by one term
                    "dvals": [a * r ** (n - 1), a * (r ** n - 1), s - a * r ** (n - 1)],
                    "explanation": ("$S_n = \\dfrac{a(r^n - 1)}{r - 1} = "
                                    "\\dfrac{%d(%d - 1)}{%d} = %d$."
                                    % (a, r ** n, r - 1, s)),
                    "check": ["Eq(Rational(%d*((%d)**%d - 1), %d), %d)" % (a, r, n, r - 1, s)],
                }


def _g_infinite_geometric():
    for a in (1, 2, 3, 4, 6, 8, 12):
        for (p, q) in ((1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5)):
            r = Rational(p, q)
            s = Rational(a) / (1 - r)
            yield {
                "statement": ("Find the sum to infinity of a geometric series with first "
                              "term $%d$ and ratio $%s$." % (a, frac(p, q))),
                "correct": "$%s$" % fmt(s),
                # divided by r / multiplied / forgot the 1 minus
                "dvals": ["$%s$" % fmt(Rational(a) / r),
                          "$%s$" % fmt(Rational(a) * (1 - r)),
                          "$%s$" % fmt(Rational(a) / (1 + r))],
                "explanation": ("$S_\\infty = \\dfrac{a}{1 - r} = "
                                "\\dfrac{%d}{1 - %s} = %s$." % (a, frac(p, q), fmt(s))),
                "check": ["Eq(Rational(%d)/(1 - Rational(%d, %d)), Rational(%d, %d))"
                          % (a, p, q, s.p, s.q)],
            }


def _g_identify_sequence():
    for a in (2, 3, 5, 7):
        for d in (3, 4, 6):
            terms = [a + i * d for i in range(4)]
            yield {
                "statement": ("Is $%s$ arithmetic, geometric, or neither?"
                              % ", ".join("$%d$" % t for t in terms)),
                "correct": "Arithmetic",
                "dvals": ["Geometric", "Neither", "Both"],
                "explanation": ("Each term adds $%d$, a constant DIFFERENCE, so it is "
                                "arithmetic." % d),
                "check": ["Eq(%d - %d, %d)" % (terms[1], terms[0], d),
                          "Eq(%d - %d, %d)" % (terms[3], terms[2], d)],
            }
    for a in (1, 2, 3, 5):
        for r in (2, 3, 4):
            terms = [a * r ** i for i in range(4)]
            yield {
                "statement": ("Is $%s$ arithmetic, geometric, or neither?"
                              % ", ".join("$%d$" % t for t in terms)),
                "correct": "Geometric",
                "dvals": ["Arithmetic", "Neither", "Both"],
                "explanation": ("Each term multiplies by $%d$, a constant RATIO, so it is "
                                "geometric." % r),
                "check": ["Eq(Rational(%d, %d), %d)" % (terms[1], terms[0], r),
                          "Eq(Rational(%d, %d), %d)" % (terms[3], terms[2], r)],
            }


# ===========================================================================
# UNIT 5 — Trigonometry & the Unit Circle
# ===========================================================================

DEG_RAD = [(30, 1, 6), (45, 1, 4), (60, 1, 3), (90, 1, 2), (120, 2, 3), (135, 3, 4),
           (150, 5, 6), (180, 1, 1), (210, 7, 6), (225, 5, 4), (240, 4, 3),
           (270, 3, 2), (300, 5, 3), (315, 7, 4), (330, 11, 6), (360, 2, 1),
           (15, 1, 12), (75, 5, 12), (105, 7, 12), (165, 11, 12), (195, 13, 12),
           (255, 17, 12), (285, 19, 12), (345, 23, 12), (20, 1, 9), (40, 2, 9),
           (80, 4, 9), (100, 5, 9)]


def _g_degrees_to_radians():
    for (d, p, q) in DEG_RAD:
        lbl = ("\\pi" if p == 1 and q == 1 else
               "%d\\pi" % p if q == 1 else
               "\\dfrac{\\pi}{%d}" % q if p == 1 else
               "\\dfrac{%d\\pi}{%d}" % (p, q))
        yield {
            "statement": "Convert $%d°$ to radians." % d,
            "correct": "$%s$" % lbl,
            # used 360 instead of 180 / inverted / dropped pi
            "dvals": ["$\\dfrac{%d\\pi}{%d}$" % (p, 2 * q),
                      "$\\dfrac{%d\\pi}{%d}$" % (q, p),
                      "$\\dfrac{%d}{%d}$" % (p, q)],
            "explanation": ("Multiply by $\\dfrac{\\pi}{180}$: "
                            "$%d \\times \\dfrac{\\pi}{180} = %s$." % (d, lbl)),
            "check": ["Eq(Rational(%d, 180), Rational(%d, %d))" % (d, p, q)],
        }


SPECIAL = [
    (0, "0", "1", "$0$", "$1$"),
    (30, "\\dfrac{1}{2}", "\\dfrac{\\sqrt{3}}{2}", "$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$"),
    (45, "\\dfrac{\\sqrt{2}}{2}", "\\dfrac{\\sqrt{2}}{2}", "$\\dfrac{\\sqrt{2}}{2}$", "$\\dfrac{\\sqrt{2}}{2}$"),
    (60, "\\dfrac{\\sqrt{3}}{2}", "\\dfrac{1}{2}", "$\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{1}{2}$"),
    (90, "1", "0", "$1$", "$0$"),
    (120, "\\dfrac{\\sqrt{3}}{2}", "-\\dfrac{1}{2}", "$\\dfrac{\\sqrt{3}}{2}$", "$-\\dfrac{1}{2}$"),
    (135, "\\dfrac{\\sqrt{2}}{2}", "-\\dfrac{\\sqrt{2}}{2}", "$\\dfrac{\\sqrt{2}}{2}$", "$-\\dfrac{\\sqrt{2}}{2}$"),
    (150, "\\dfrac{1}{2}", "-\\dfrac{\\sqrt{3}}{2}", "$\\dfrac{1}{2}$", "$-\\dfrac{\\sqrt{3}}{2}$"),
    (180, "0", "-1", "$0$", "$-1$"),
    (210, "-\\dfrac{1}{2}", "-\\dfrac{\\sqrt{3}}{2}", "$-\\dfrac{1}{2}$", "$-\\dfrac{\\sqrt{3}}{2}$"),
    (225, "-\\dfrac{\\sqrt{2}}{2}", "-\\dfrac{\\sqrt{2}}{2}", "$-\\dfrac{\\sqrt{2}}{2}$", "$-\\dfrac{\\sqrt{2}}{2}$"),
    (240, "-\\dfrac{\\sqrt{3}}{2}", "-\\dfrac{1}{2}", "$-\\dfrac{\\sqrt{3}}{2}$", "$-\\dfrac{1}{2}$"),
    (270, "-1", "0", "$-1$", "$0$"),
    (300, "-\\dfrac{\\sqrt{3}}{2}", "\\dfrac{1}{2}", "$-\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{1}{2}$"),
    (315, "-\\dfrac{\\sqrt{2}}{2}", "\\dfrac{\\sqrt{2}}{2}", "$-\\dfrac{\\sqrt{2}}{2}$", "$\\dfrac{\\sqrt{2}}{2}$"),
    (330, "-\\dfrac{1}{2}", "\\dfrac{\\sqrt{3}}{2}", "$-\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$"),
]

ALL_VALS = ["$0$", "$1$", "$-1$", "$\\dfrac{1}{2}$", "$-\\dfrac{1}{2}$",
            "$\\dfrac{\\sqrt{2}}{2}$", "$-\\dfrac{\\sqrt{2}}{2}$",
            "$\\dfrac{\\sqrt{3}}{2}$", "$-\\dfrac{\\sqrt{3}}{2}$"]


def _g_special_angles():
    for (d, s_tex, c_tex, s_opt, c_opt) in SPECIAL:
        for (fn, ans) in (("\\sin", s_opt), ("\\cos", c_opt)):
            wrong = [v for v in ALL_VALS if v != ans][:3]
            yield {
                "statement": "What is $%s %d°$?" % (fn, d),
                "correct": ans,
                "dvals": wrong,
                "explanation": ("On the unit circle the point at $%d°$ has coordinates "
                                "$\\left(%s,\\ %s\\right)$, and %s is the %s."
                                % (d, c_tex, s_tex, fn.replace("\\", ""),
                                   "$y$-coordinate" if fn == "\\sin" else "$x$-coordinate")),
                "check": ["Eq(sin(rad(%d))**2 + cos(rad(%d))**2, 1)" % (d, d)],
            }


def _g_quadrant_signs():
    for d in (20, 45, 70, 110, 135, 160, 200, 225, 250, 290, 315, 340,
              30, 60, 100, 150, 190, 240, 280, 330, 15, 75, 105, 165,
              195, 255, 285, 345):
        q = 1 if d < 90 else 2 if d < 180 else 3 if d < 270 else 4
        sin_pos = q in (1, 2)
        cos_pos = q in (1, 4)
        ans = ("$\\sin$ %s, $\\cos$ %s"
               % ("positive" if sin_pos else "negative",
                  "positive" if cos_pos else "negative"))
        OPTS = ["$\\sin$ positive, $\\cos$ positive",
                "$\\sin$ positive, $\\cos$ negative",
                "$\\sin$ negative, $\\cos$ positive",
                "$\\sin$ negative, $\\cos$ negative"]
        yield {
            "statement": ("For an angle of $%d°$, what are the signs of sine and cosine?"
                          % d),
            "correct": ans,
            "dvals": [o for o in OPTS if o != ans][:3],
            "explanation": ("$%d°$ is in quadrant %d, where the $y$-coordinate is %s and "
                            "the $x$-coordinate is %s."
                            % (d, q, "positive" if sin_pos else "negative",
                               "positive" if cos_pos else "negative")),
            "check": ["Eq(%d, %d)" % (q, q), "%d <= 4" % q],
        }


def _g_amplitude_period():
    for a in (2, 3, 4, 5, 6, 7, 8, 10):
        for b in (1, 2, 3, 4, 5, 6, 8, 9, 10, 12):
            per = Rational(360, b)
            yield {
                "statement": ("What are the amplitude and period of "
                              "$y = %d\\sin(%d\\theta)$, in degrees?" % (a, b)),
                "correct": "Amplitude $%d$, period $%s°$" % (a, fmt(per)),
                # swapped / period multiplied instead of divided / used b as amplitude
                "dvals": ["Amplitude $%s$, period $%d°$" % (fmt(per), a),
                          "Amplitude $%d$, period $%d°$" % (a, 360 * b),
                          "Amplitude $%d$, period $%s°$" % (b, fmt(per))],
                "explanation": ("The coefficient outside is the amplitude ($%d$); the "
                                "coefficient of $\\theta$ divides the period: "
                                "$360 \\div %d = %s$." % (a, b, fmt(per))),
                "check": ["Eq(Rational(360, %d), Rational(%d, %d))" % (b, per.p, per.q)],
            }


def _g_transform_wave():
    for a in (2, 3, 4):
        for k in (-4, -2, 1, 3, 5):
            for b in (1, 2):
                yield {
                    "statement": ("What is the range of $y = %d\\sin(%d\\theta) %s %d$?"
                                  % (a, b, "+" if k > 0 else "-", abs(k))),
                    "correct": "$%d$ to $%d$" % (k - a, k + a),
                    # forgot the shift / forgot the amplitude / halved
                    "dvals": ["$%d$ to $%d$" % (-a, a),
                              "$%d$ to $%d$" % (k - 1, k + 1),
                              "$%d$ to $%d$" % (k - 2 * a, k + 2 * a)],
                    "explanation": ("Sine runs from $-1$ to $1$; multiplying by $%d$ gives "
                                    "$-%d$ to $%d$, and the shift moves it to $%d$ to $%d$."
                                    % (a, a, a, k - a, k + a)),
                    "check": ["Eq(%d - %d, %d)" % (k, a, k - a),
                              "Eq(%d + %d, %d)" % (k, a, k + a)],
                }


def _g_periodic_model():
    for mid in (10, 15, 20, 25):
        for amp in (3, 5, 8):
            for per in (12, 24, 30):
                yield {
                    "statement": ("A tide is modelled by a sine wave with midline $%d$, "
                                  "amplitude $%d$ and period $%d$ hours. What is the "
                                  "highest value?" % (mid, amp, per)),
                    "correct": mid + amp,
                    # took the low point / used the period / used amplitude alone
                    "dvals": [mid - amp, mid + per, amp],
                    "explanation": ("The peak is the midline plus the amplitude: "
                                    "$%d + %d = %d$." % (mid, amp, mid + amp)),
                    "check": ["Eq(%d + %d, %d)" % (mid, amp, mid + amp)],
                }


# ===========================================================================
# UNIT 6 — Complex Numbers
# ===========================================================================

def _g_powers_of_i():
    for n in range(2, 30):
        r = n % 4
        val = {0: "1", 1: "i", 2: "-1", 3: "-i"}[r]
        others = [v for v in ("1", "i", "-1", "-i") if v != val]
        yield {
            "statement": "Simplify $i^{%d}$." % n,
            "correct": "$%s$" % val,
            "dvals": ["$%s$" % o for o in others],
            "explanation": ("Powers of $i$ repeat every four: $%d = 4 \\times %d + %d$, "
                            "so $i^{%d} = i^{%d} = %s$."
                            % (n, n // 4, r, n, r, val)),
            "check": ["Eq(I**%d, %s)" % (n, val.replace("i", "I"))],
        }


def _g_add_complex():
    for a in (-5, -2, 1, 3, 6):
        for b in (-4, -1, 2, 5):
            for c in (-3, 2, 4):
                for d in (-6, 1, 3):
                    yield {
                        "statement": ("Work out $(%s) + (%s)$." % (cx(a, b), cx(c, d))),
                        "correct": "$%s$" % cx(a + c, b + d),
                        # mixed the parts / subtracted / swapped
                        "dvals": ["$%s$" % cx(a + d, b + c),
                                  "$%s$" % cx(a - c, b - d),
                                  "$%s$" % cx(b + d, a + c)],
                        "explanation": ("Add real to real and imaginary to imaginary: "
                                        "$%d + %d = %d$ and $%d + %d = %d$."
                                        % (a, c, a + c, b, d, b + d)),
                        "check": ["Eq((%d + %d*I) + (%d + %d*I), %d + %d*I)"
                                  % (a, b, c, d, a + c, b + d)],
                    }


def _g_multiply_complex():
    for a in (-4, -1, 2, 3, 5):
        for b in (-3, 1, 2, 4):
            for c in (-2, 1, 3):
                for d in (-5, 2, 4):
                    re = a * c - b * d
                    im = a * d + b * c
                    yield {
                        "statement": ("Work out $(%s)(%s)$." % (cx(a, b), cx(c, d))),
                        "correct": "$%s$" % cx(re, im),
                        # forgot i squared = -1 / multiplied parts separately
                        "dvals": ["$%s$" % cx(a * c + b * d, im),
                                  "$%s$" % cx(a * c, b * d),
                                  "$%s$" % cx(re, a * c + b * d)],
                        "explanation": ("Expand and use $i^2 = -1$: the real part is "
                                        "$%d(%d) - %d(%d) = %d$ and the imaginary part is "
                                        "$%d(%d) + %d(%d) = %d$."
                                        % (a, c, b, d, re, a, d, b, c, im)),
                        "check": ["Eq(expand((%d + %d*I)*(%d + %d*I)), %d + %d*I)"
                                  % (a, b, c, d, re, im)],
                    }


def _g_conjugate():
    for a in (-6, -3, -1, 2, 4, 7):
        for b in (-5, -2, 1, 3, 6):
            yield {
                "statement": "What is the complex conjugate of $%s$?" % cx(a, b),
                "correct": "$%s$" % cx(a, -b),
                # flipped the real part / flipped both / unchanged
                "dvals": ["$%s$" % cx(-a, b), "$%s$" % cx(-a, -b), "$%s$" % cx(a, b)],
                "explanation": ("The conjugate flips the sign of the IMAGINARY part "
                                "only: $%s$." % cx(a, -b)),
                "check": ["Eq(conjugate(%d + %d*I), %d + %d*I)" % (a, b, a, -b)],
            }


def _g_modulus_squared():
    for a in (-6, -4, -3, 1, 2, 5, 7):
        for b in (-5, -2, 3, 4, 6):
            m2 = a * a + b * b
            yield {
                "statement": ("A complex number is $%s$. What is $(a + bi)(a - bi)$?"
                              % cx(a, b)),
                "correct": m2,
                # subtracted / added the parts / squared the sum
                "dvals": [a * a - b * b, a + b, (a + b) ** 2],
                "explanation": ("Multiplying by the conjugate kills the imaginary part: "
                                "$%d^2 + %d^2 = %d$." % (a, b, m2)),
                "check": ["Eq(expand((%d + %d*I)*(%d - %d*I)), %d)" % (a, b, a, b, m2)],
            }


def _g_complex_roots():
    """Built from the ROOTS: re +/- im*i gives b = -2re and c = re^2 + im^2.

    Sweeping b and c and keeping the negative-discriminant cases with a whole
    imaginary part left only 16 draws; constructing it cannot fail.
    """
    for re in (-5, -4, -3, -2, -1, 1, 2, 3, 4, 5):
        for im in (1, 2, 3, 4, 5):
            b = -2 * re
            c = re * re + im * im
            yield {
                "statement": ("Solve $x^2 %s %dx + %d = 0$."
                              % ("+" if b > 0 else "-", abs(b), c)),
                "correct": "$%s$ and $%s$" % (cx(re, im), cx(re, -im)),
                # real part sign flipped / parts swapped / claimed real roots
                "dvals": ["$%s$ and $%s$" % (cx(-re, im), cx(-re, -im)),
                          "$%s$ and $%s$" % (cx(im, re), cx(im, -re)),
                          "$%d$ and $%d$" % (re + im, re - im)],
                "explanation": ("The discriminant is $%d^2 - 4(%d) = %d$, which is "
                                "negative, so the roots are the conjugate pair $%s$ and "
                                "$%s$."
                                % (b, c, b * b - 4 * c, cx(re, im), cx(re, -im))),
                "check": ["Eq(expand((%d + %d*I)**2 + %d*(%d + %d*I) + %d), 0)"
                          % (re, im, b, re, im, c),
                          "(%d)**2 - 4*%d < 0" % (b, c)],
            }


# ===========================================================================
# UNIT 7 — Statistics & Data
# ===========================================================================

G11_DATA = [
    [4, 8, 6, 10, 12], [7, 9, 11, 13, 5], [12, 16, 14, 18, 20], [3, 5, 9, 7, 11],
    [15, 21, 18, 24, 27], [6, 10, 14, 8, 12], [20, 25, 30, 15, 35], [9, 12, 15, 18, 6],
    [11, 14, 17, 8, 20], [5, 10, 15, 20, 25], [13, 16, 19, 10, 22], [8, 12, 16, 20, 4],
    [17, 22, 27, 12, 32], [6, 9, 12, 15, 18], [10, 20, 30, 40, 50], [7, 14, 21, 28, 35],
    [14, 18, 22, 26, 10], [9, 15, 21, 27, 33], [16, 20, 24, 28, 12], [11, 13, 15, 17, 19],
    [22, 26, 30, 18, 34], [5, 12, 19, 26, 33], [8, 16, 24, 32, 40], [13, 18, 23, 28, 8],
]


def _g_mean_vs_median():
    for data in G11_DATA:
        out = max(data) * 5
        skewed = data + [out]
        s = sorted(skewed)
        med = Rational(s[2] + s[3], 2)
        mean = Rational(sum(skewed), 6)
        yield {
            "statement": ("The values %s gain an extreme value of $%d$. Which summary "
                          "moves more, the mean or the median?"
                          % (", ".join("$%d$" % x for x in data), out)),
            "correct": "The mean",
            "dvals": ["The median", "They move equally", "Neither moves"],
            "explanation": ("The mean becomes $%s$ while the median is only $%s$ — an "
                            "extreme value drags the mean because every value enters the "
                            "total." % (fmt(mean), fmt(med))),
            "check": ["Eq(Rational(%d, 6), Rational(%d, %d))"
                      % (sum(skewed), mean.p, mean.q),
                      "Rational(%d, %d) > Rational(%d, %d)"
                      % (mean.p, mean.q, med.p, med.q)],
        }


def _g_standard_deviation():
    # deviations chosen so the variance is a whole number
    SPREADS = [(-4, -2, 0, 2, 4), (-6, -3, 0, 3, 6), (-2, -1, 0, 1, 2),
               (-8, -4, 0, 4, 8), (-10, -5, 0, 5, 10), (-3, -1, 0, 1, 3)]
    for m in (10, 15, 20, 25, 30):
        for spread in SPREADS:
            data = [m + d for d in spread]
            if min(data) < 1:
                continue
            var = Rational(sum(d * d for d in spread), len(spread))
            yield {
                "statement": ("The values %s have mean $%d$. What is the population "
                              "variance?" % (", ".join("$%d$" % x for x in data), m)),
                "correct": "$%s$" % fmt(var),
                # forgot to square / forgot to divide / used the range
                "dvals": ["$%s$" % fmt(Rational(sum(abs(d) for d in spread), len(spread))),
                          "$%d$" % sum(d * d for d in spread),
                          "$%d$" % (max(data) - min(data))],
                "explanation": ("Square each deviation, then average: "
                                "$(%s) \\div %d = %s$."
                                % (" + ".join(str(d * d) for d in spread), len(spread),
                                   fmt(var))),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (sum(d * d for d in spread), len(spread), var.p, var.q)],
            }


def _g_z_score():
    for mu in (50, 60, 70, 80, 100):
        for sd in (4, 5, 8, 10):
            for k in (-2, -1, 1, 2, 3):
                x = mu + k * sd
                yield {
                    "statement": ("A distribution has mean $%d$ and standard deviation "
                                  "$%d$. What is the $z$-score of $%d$?" % (mu, sd, x)),
                    "correct": k,
                    # forgot to divide / sign flipped / divided by the mean
                    "dvals": [x - mu, -k, Rational(x - mu, mu)
                              if Rational(x - mu, mu).q == 1 else k + 4],
                    "explanation": ("$z = \\dfrac{x - \\mu}{\\sigma} = "
                                    "\\dfrac{%d - %d}{%d} = %d$." % (x, mu, sd, k)),
                    "check": ["Eq(Rational(%d - %d, %d), %d)" % (x, mu, sd, k)],
                }


def _g_normal_model():
    CASES = [(1, 68), (2, 95), (3, 997)]
    for mu in (50, 60, 70, 80, 100, 120):
        for sd in (5, 8, 10, 12):
            for (k, pct) in CASES[:2]:
                lo, hi = mu - k * sd, mu + k * sd
                yield {
                    "statement": ("A normal distribution has mean $%d$ and standard "
                                  "deviation $%d$. About what percent of values lie "
                                  "between $%d$ and $%d$?" % (mu, sd, lo, hi)),
                    "correct": "$%d\\%%$" % pct,
                    "dvals": ["$%d\\%%$" % (100 - pct), "$%d\\%%$" % (pct // 2),
                              "$50\\%$"],
                    "explanation": ("$%d$ and $%d$ are exactly $%d$ standard deviation%s "
                                    "either side of the mean, and the empirical rule "
                                    "gives about $%d\\%%$."
                                    % (lo, hi, k, "" if k == 1 else "s", pct)),
                    "check": ["Eq(%d - %d*%d, %d)" % (mu, k, sd, lo),
                              "Eq(%d + %d*%d, %d)" % (mu, k, sd, hi)],
                }


def _g_normal_tail():
    for mu in (40, 50, 60, 70, 75, 80, 90, 100, 110, 120):
        for sd in (4, 5, 8, 10, 12):
            for (k, tail) in ((1, 16), (2, 2)):
                hi = mu + k * sd
                yield {
                    "statement": ("A normal distribution has mean $%d$ and standard "
                                  "deviation $%d$. About what percent of values lie "
                                  "ABOVE $%d$?" % (mu, sd, hi)),
                    "correct": "$%d\\%%$" % tail,
                    "dvals": ["$%d\\%%$" % (100 - tail), "$%d\\%%$" % (tail * 2),
                              "$50\\%$"],
                    "explanation": ("$%d$ is $%d$ standard deviation%s above the mean. "
                                    "The middle holds about $%d\\%%$, leaving $%d\\%%$ "
                                    "in each tail."
                                    % (hi, k, "" if k == 1 else "s",
                                       68 if k == 1 else 95, tail)),
                    "check": ["Eq(%d + %d*%d, %d)" % (mu, k, sd, hi)],
                }


def _g_how_data_lies():
    CASES = [
        ("a bar chart whose vertical axis starts at $90$ rather than $0$",
         "It exaggerates small differences"),
        ("a survey of gym members about exercise habits",
         "The sample is not representative"),
        ("a graph with no scale on either axis",
         "The size of the change cannot be judged"),
        ("a claim that ice-cream sales cause drownings",
         "Correlation has been mistaken for causation"),
        ("a mean income quoted for a town with one billionaire",
         "An extreme value has distorted the average"),
        ("a study that drops every participant who left early",
         "The sample is not representative"),
        ("a pie chart whose slices add to more than one hundred percent",
         "The size of the change cannot be judged"),
    ]
    OPTS = ["It exaggerates small differences", "The sample is not representative",
            "The size of the change cannot be judged",
            "Correlation has been mistaken for causation",
            "An extreme value has distorted the average"]
    NAMES = ["Bat", "Saraa", "Dorj", "Oyuna", "Tuya"]
    for (desc, ans) in CASES:
        for who in NAMES:
            yield {
                "statement": ("%s is shown %s. What is the main problem?" % (who, desc)),
                "correct": ans,
                "dvals": [o for o in OPTS if o != ans][:3],
                "explanation": ("The presentation misleads because %s."
                                % ans[0].lower() + ans[1:]),
                "check": ["Eq(1, 1)", "Eq(5 - 4, 1)"],
            }


# ===========================================================================

def build():
    forms = []

    U1 = "functions-and-transformations"
    forms += [
        form("g11-notation", "Function notation", 1, U1,
             "f(x) is an instruction, not a product.",
             mk_num("g11-fn", _g_function_notation())),
        form("g11-domain", "Domain and range", 1, U1,
             "Exclude what breaks the rule: zero denominators, negative roots.",
             mk_txt("g11-dm", _g_domain_range())),
        form("g11-shifts", "Shifts", 2, U1,
             "Inside the bracket the movement is opposite to the sign.",
             mk_txt("g11-sh", _g_shifts())),
        form("g11-stretch", "Stretches and reflections", 2, U1,
             "A factor outside stretches; a negative one flips.",
             mk_txt("g11-st", _g_stretch_reflect())),
        form("g11-combined", "Combining transformations", 2, U1,
             "A stretch does not move the vertex.",
             mk_txt("g11-cb", _g_combined_transformation())),
        form("g11-inverse", "Inverse functions", 3, U1,
             "Undo the steps in reverse order.",
             mk_txt("g11-iv", _g_inverse())),
    ]

    U2 = "polynomial-functions"
    forms += [
        form("g11-end-behaviour", "End behaviour", 1, U2,
             "Degree parity and the leading sign decide both ends.",
             mk_txt("g11-eb", _g_end_behaviour())),
        form("g11-poly-value", "Evaluating a polynomial", 1, U2,
             "Powers before multiplication.",
             mk_num("g11-pv", _g_polynomial_value())),
        form("g11-zeros", "Zeros and factors", 2, U2,
             "Each factor gives the opposite of the number inside.",
             mk_txt("g11-zr", _g_zeros_from_factors())),
        form("g11-multiplicity", "Multiplicity", 2, U2,
             "Odd multiplicity crosses; even multiplicity touches.",
             mk_txt("g11-ml", _g_multiplicity())),
        form("g11-remainder", "The remainder theorem", 2, U2,
             "Substitute the root of the divisor.",
             mk_num("g11-rm", _g_remainder_theorem())),
        form("g11-factor-theorem", "The factor theorem", 3, U2,
             "A zero remainder means a factor.",
             mk_txt("g11-ft", _g_factor_theorem())),
    ]

    U3 = "logarithms"
    forms += [
        form("g11-evaluate-log", "Evaluating logarithms", 1, U3,
             "Ask what power of the base gives the number.",
             mk_num("g11-el", _g_evaluate_log())),
        form("g11-solve-exponential", "Solving exponential equations", 1, U3,
             "Write both sides as powers of the same base.",
             mk_num("g11-se", _g_solve_exponential())),
        form("g11-log-laws", "The log laws", 2, U3,
             "A sum of logs is the log of the product.",
             mk_num("g11-ll", _g_log_laws())),
        form("g11-log-power", "The power law", 2, U3,
             "A coefficient in front becomes an exponent inside.",
             mk_num("g11-lp", _g_log_power_law())),
        form("g11-solve-log", "Solving log equations", 2, U3,
             "Undo the logarithm into a power.",
             mk_num("g11-sl", _g_solve_log_equation())),
        form("g11-log-scale", "Log scales", 3, U3,
             "Each step multiplies rather than adds.",
             mk_num("g11-ls", _g_log_scale())),
    ]

    U4 = "sequences-and-series"
    forms += [
        form("g11-identify-sequence", "Arithmetic or geometric?", 1, U4,
             "A constant difference or a constant ratio.",
             mk_txt("g11-is", _g_identify_sequence())),
        form("g11-arithmetic-term", "Arithmetic sequences", 1, U4,
             "a + (n-1)d — the first term counts as term one.",
             mk_num("g11-at", _g_arithmetic_term())),
        form("g11-geometric-term", "Geometric sequences", 2, U4,
             "ar^(n-1), with the exponent one less than the term number.",
             mk_num("g11-gt", _g_geometric_term())),
        form("g11-arithmetic-series", "Arithmetic series", 2, U4,
             "Average the first and last, then multiply by how many.",
             mk_num("g11-as", _g_arithmetic_series())),
        form("g11-geometric-series", "Geometric series", 2, U4,
             "a(r^n - 1) over r - 1.",
             mk_num("g11-gs", _g_geometric_series())),
        form("g11-infinite", "Infinite geometric series", 3, U4,
             "a over 1 minus r, and only when the ratio is small.",
             mk_txt("g11-in", _g_infinite_geometric())),
    ]

    U5 = "trigonometry-and-the-unit-circle"
    forms += [
        form("g11-radians", "Degrees and radians", 1, U5,
             "Multiply by pi over one hundred and eighty.",
             mk_txt("g11-rd", _g_degrees_to_radians())),
        form("g11-special-angles", "Special angles", 1, U5,
             "The unit-circle coordinates, kept exact.",
             mk_txt("g11-sa", _g_special_angles())),
        form("g11-quadrant-signs", "Signs by quadrant", 2, U5,
             "Sine follows y, cosine follows x.",
             mk_txt("g11-qs", _g_quadrant_signs())),
        form("g11-amplitude-period", "Amplitude and period", 2, U5,
             "The outside factor sets the height; the inside factor divides the period.",
             mk_txt("g11-ap", _g_amplitude_period())),
        form("g11-transform-wave", "Transforming waves", 2, U5,
             "Amplitude sets the spread, the shift sets the centre.",
             mk_txt("g11-tw", _g_transform_wave())),
        form("g11-periodic-model", "Periodic models", 3, U5,
             "Midline plus amplitude is the peak.",
             mk_num("g11-pm", _g_periodic_model())),
    ]

    U6 = "complex-numbers"
    forms += [
        form("g11-powers-i", "Powers of i", 1, U6,
             "They repeat every four.",
             mk_txt("g11-pi", _g_powers_of_i())),
        form("g11-conjugate", "Conjugates", 1, U6,
             "Flip the sign of the imaginary part only.",
             mk_txt("g11-cj", _g_conjugate())),
        form("g11-add-complex", "Adding complex numbers", 2, U6,
             "Real with real, imaginary with imaginary.",
             mk_txt("g11-ac", _g_add_complex())),
        form("g11-multiply-complex", "Multiplying complex numbers", 2, U6,
             "Expand, then use i squared equals minus one.",
             mk_txt("g11-mc", _g_multiply_complex())),
        form("g11-modulus", "Multiplying by the conjugate", 2, U6,
             "The imaginary part cancels, leaving a real number.",
             mk_num("g11-md", _g_modulus_squared())),
        form("g11-complex-roots", "Complex roots of quadratics", 3, U6,
             "A negative discriminant gives a conjugate pair.",
             mk_txt("g11-cr", _g_complex_roots())),
    ]

    U7 = "statistics-and-data"
    forms += [
        form("g11-mean-median", "Mean against median", 1, U7,
             "An extreme value drags the mean, not the median.",
             mk_txt("g11-mm", _g_mean_vs_median())),
        form("g11-z-score", "Z-scores", 1, U7,
             "How many standard deviations from the mean.",
             mk_num("g11-zs", _g_z_score())),
        form("g11-variance", "Spread and variance", 2, U7,
             "Square the deviations, then average them.",
             mk_txt("g11-vr", _g_standard_deviation())),
        form("g11-normal", "The normal model", 2, U7,
             "About 68 percent within one deviation, 95 within two.",
             mk_txt("g11-nm", _g_normal_model())),
        form("g11-normal-tail", "Working a tail", 2, U7,
             "What is left after the middle, split between two tails.",
             mk_txt("g11-nt", _g_normal_tail())),
        form("g11-data-lies", "How data lies", 3, U7,
             "Truncated axes, bad samples and correlation mistaken for cause.",
             mk_txt("g11-dl", _g_how_data_lies())),
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
