# -*- coding: utf-8 -*-
"""Integrated Math 2 — the second half of every unit's bank.

Twelve forms per unit instead of six, with a real difficulty ramp: roughly
four Level 1, five Level 2 and three Level 3. Six of the eight original
units stopped at Level 2, so a student who picked "Level 3 · Exam" on
Circles, Probability or Similarity was offered an empty tier.

This module also supplies the whole bank for Unit 8, Geometric Measurement
& Modelling, which is new to the course — the Integrated pathway had no
volume anywhere in three years until it was written.

Same contract as scripts/pb/integrated_2.py: answers computed from named
parameters, one named student error per distractor, every check[] asserted
by the gate.
"""
from sympy import Rational, sqrt

from imbank import fmt, lin, quad, xpm  # noqa: F401


def _syq(a, b, c):
    """`ax^2 + bx + c` in SYMPY syntax. quad()/lin() render LaTeX, which does
    not sympify — the missing `*` between coefficient and variable is the
    trap, and it only shows up at the gate."""
    return "(%d)*x**2 + (%d)*x + (%d)" % (a, b, c)


def _syl(a, b):
    """`ax + b` in sympy syntax."""
    return "(%d)*x + (%d)" % (a, b)


def _gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# ===========================================================================
# Unit 1 — Rational Exponents & Radicals
# ===========================================================================

def g_negative_exponent():
    """LEVEL 1 — a negative exponent is a reciprocal, not a negative number."""
    raws = []
    for b in (2, 3, 4, 5, 6, 10):
        for n in (1, 2, 3):
            v = Rational(1, b ** n)
            raws.append({
                "statement": "Evaluate $%d^{-%d}$." % (b, n),
                "correct": v,
                # made it negative; ignored the sign; negated the base only
                "dvals": [-(b ** n), b ** n, Rational(-1, b ** n)],
                "explanation": "A negative exponent flips the base into a reciprocal: "
                               "$%d^{-%d} = \\dfrac{1}{%d^{%d}} = \\dfrac{1}{%d}$. It never "
                               "makes the answer negative — $%d^{-%d}$ and $-%d^{%d}$ are "
                               "different quantities entirely."
                               % (b, n, b, n, b ** n, b, n, b, n),
                "check": ["Eq(Rational(1, %d**%d), Rational(%d, %d))" % (b, n, v.p, v.q),
                          "Eq(%d**(-%d), Rational(%d, %d))" % (b, n, v.p, v.q)],
            })
    for b in (2, 3, 4, 5):
        for n in (1, 2):
            for k in (2, 3, 5):
                v = Rational(k, b ** n)
                raws.append({
                    "statement": "Evaluate $%d \\cdot %d^{-%d}$." % (k, b, n),
                    "correct": v,
                    "dvals": [-k * b ** n, k * b ** n, Rational(1, k * b ** n)],
                    "explanation": "Only the $%d$ carries the negative exponent, so this is "
                                   "$%d \\cdot \\dfrac{1}{%d} = \\dfrac{%d}{%d}$. The "
                                   "coefficient $%d$ stays where it is."
                                   % (b, k, b ** n, k, b ** n, k),
                    "check": ["Eq(%d*Rational(1, %d**%d), Rational(%d, %d))"
                              % (k, b, n, v.p, v.q)],
                })
    return raws


def g_radical_to_exponent():
    """LEVEL 2 — the same number written two ways."""
    raws = []
    for b in (2, 3, 5, 6, 7, 10, 11, 13):
        for n in (2, 3, 4, 5):
            for m in (1, 2, 3):
                if m >= n:
                    continue
                root = "\\sqrt" if n == 2 else "\\sqrt[%d]" % n
                inner = "%d^{%d}" % (b, m) if m > 1 else "%d" % b
                raws.append({
                    "statement": "Write $%s{%s}$ using a rational exponent."
                                 % (root, inner),
                    "correct": "$%d^{%s}$" % (b, fmt(Rational(m, n))),
                    "dvals": [
                        "$%d^{%s}$" % (b, fmt(Rational(n, m))),      # flipped the fraction
                        "$%d^{%d}$" % (b, m * n),                    # multiplied instead
                        "$%d^{%s}$" % (b, fmt(Rational(m + n, n))),
                    ],
                    "explanation": "The INDEX of the radical becomes the denominator and "
                                   "the power inside becomes the numerator: "
                                   "$%s{%s} = %d^{%s}$. Flipping the fraction is the "
                                   "commonest error, and it is easy to catch — a square "
                                   "root should give an exponent of $\\frac{1}{2}$, never "
                                   "$2$." % (root, inner, b, fmt(Rational(m, n))),
                    "check": ["Eq((%d**%d)**Rational(1, %d), %d**Rational(%d, %d))"
                              % (b, m, n, b, m, n),
                              "Ne(Rational(%d, %d), Rational(%d, %d))"
                              % (m, n, n, m) if m != n else "Eq(1, 1)"],
                })
    return raws


def g_rationalise_denominator():
    """LEVEL 2 — clearing a radical out of the bottom."""
    raws = []
    for r in (2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19):
        for k in (1, 2, 3, 4):
            raws.append({
                "statement": "Write $\\dfrac{%d}{\\sqrt{%d}}$ with no radical in the "
                             "denominator." % (k, r),
                "correct": "$\\dfrac{%d\\sqrt{%d}}{%d}$" % (k, r, r),
                "dvals": [
                    "$\\dfrac{%d\\sqrt{%d}}{%d}$" % (k, r, r * r),   # squared the bottom
                    "$%d\\sqrt{%d}$" % (k, r),                       # dropped the divisor
                    "$\\dfrac{\\sqrt{%d}}{%d}$" % (r, k),            # inverted
                ],
                "explanation": "Multiply top and bottom by $\\sqrt{%d}$ — that is "
                               "multiplying by $1$, so the value is unchanged: "
                               "$\\dfrac{%d}{\\sqrt{%d}} \\cdot "
                               "\\dfrac{\\sqrt{%d}}{\\sqrt{%d}} = "
                               "\\dfrac{%d\\sqrt{%d}}{%d}$, because "
                               "$\\sqrt{%d} \\cdot \\sqrt{%d} = %d$, not $%d$."
                               % (r, k, r, r, r, k, r, r, r, r, r, r * r),
                "check": ["Eq(sqrt(%d)*sqrt(%d), %d)" % (r, r, r),
                          "Eq(simplify(Rational(%d, 1)/sqrt(%d) - %d*sqrt(%d)/%d), 0)"
                          % (k, r, k, r, r)],
            })
    return raws


def g_simplify_power_of_power():
    """LEVEL 3 — a perfect power under a fractional exponent."""
    raws = []
    for a in (2, 3, 5, 6, 7, 10, 11, 13):
        for e in (2, 3, 4, 5, 6):
            base = a ** e
            if base > 200000:
                continue
            raws.append({
                "statement": "Simplify $%d^{\\frac{1}{%d}}$, giving an exact value."
                             % (base, e),
                "correct": a,
                # squared the answer; never took the root; divided instead of rooting
                "dvals": [a * a, base, Rational(base, e)],
                "explanation": "Recognise the base as a perfect power: $%d = %d^{%d}$. "
                               "Then $\\left(%d^{%d}\\right)^{\\frac{1}{%d}} = "
                               "%d^{\\frac{%d}{%d}} = %d^1 = %d$. A fractional exponent "
                               "takes a ROOT — dividing the base by $%d$ instead gives "
                               "$%s$, which is not it."
                               % (base, a, e, a, e, e, a, e, e, a, a, e,
                                  fmt(Rational(base, e))),
                "check": ["Eq(%d**%d, %d)" % (a, e, base),
                          "Eq(%d**Rational(1, %d), %d)" % (base, e, a)],
            })
    return raws


def g_radical_extraneous():
    """LEVEL 3 — squaring can invent a root that does not check out.

    Built backwards from the surviving root, so the extraneous one is
    guaranteed to exist rather than hoped for.
    """
    raws = []
    for a in (1, 2, 3, 4, 5):
        for g in range(a + 2, a + 10):
            c = (g - a) ** 2 - g            # forces sqrt(g + c) == g - a
            if c < 1:
                continue
            other = 2 * a + 1 - g           # the second root of the squared equation
            if other >= a:                  # must fail the sign test to be extraneous
                continue
            raws.append({
                "statement": "Solve $\\sqrt{x + %d} = x - %d$." % (c, a),
                "correct": "$x = %d$ only" % g,
                "dvals": [
                    "$x = %d$ and $x = %d$" % (min(other, g), max(other, g)),
                    "$x = %d$ only" % other,
                    "There is no solution.",
                ],
                "explanation": "Squaring both sides gives "
                               "$x + %d = x^2 - %dx + %d$, which rearranges to "
                               "$x^2 - %dx%s = 0$ with roots $x = %d$ and $x = %d$. "
                               "Both must be CHECKED in the ORIGINAL equation, because "
                               "squaring can turn a false statement into a true one. At "
                               "$x = %d$ the right-hand side is $%d$, and a square root is "
                               "never negative — so that root is extraneous. Only "
                               "$x = %d$ survives."
                               % (c, 2 * a, a * a, 2 * a + 1,
                                  "" if a * a - c == 0 else
                                  (" + %d" % (a * a - c) if a * a - c > 0
                                   else " - %d" % (c - a * a)),
                                  other, g, other, other - a, g),
                "check": ["Eq(sqrt(%d + %d), %d - %d)" % (g, c, g, a),
                          "%d - %d < 0" % (other, a),
                          "Eq((%d)**2 - %d*(%d) + (%d), 0)"
                          % (other, 2 * a + 1, other, a * a - c),
                          "Eq((%d)**2 - %d*(%d) + (%d), 0)"
                          % (g, 2 * a + 1, g, a * a - c)],
            })
    return raws


def g_irrational_combination():
    """LEVEL 3 — which combination is forced to be irrational."""
    raws = []
    for r in (2, 3, 5, 6, 7, 10, 11, 13):
        for k in (2, 3, 4, 5, 6):
            raws.append({
                "statement": "Let $a$ be the rational number $%d$ and let $b = \\sqrt{%d}$, "
                             "which is irrational. Which of these MUST be irrational?"
                             % (k, r),
                "correct": "$a + b$",
                "dvals": ["$b \\cdot b$", "$b - b$", "$b^2 - %d$" % r],
                "explanation": "If $a + b$ were rational, then $b = (a + b) - a$ would be a "
                               "difference of two rationals and therefore rational — "
                               "contradicting that $b$ is irrational. So $a + b$ must be "
                               "irrational. The others are all rational: "
                               "$b \\cdot b = %d$, $b - b = 0$, and $b^2 - %d = 0$."
                               % (r, r),
                "check": ["Eq(sqrt(%d)*sqrt(%d), %d)" % (r, r, r),
                          "Eq(sqrt(%d)**2 - %d, 0)" % (r, r)],
            })
    return raws


# ===========================================================================
# Unit 2 — Polynomials & Factoring
# ===========================================================================

def g_add_polynomials():
    """LEVEL 1 — collecting like terms, with a subtraction to distribute."""
    raws = []
    for a in (2, 3, 4, 5):
        for b in (-6, -2, 3, 7):
            for c in (1, 4, 8):
                for d in (2, 5, 9):
                    for e in (-3, 6):
                        raws.append({
                            "statement": "Simplify $(%s) - (%s)$."
                                         % (quad(a, b, c), quad(d, e, 0).rstrip()),
                            "correct": "$%s$" % quad(a - d, b - e, c),
                            "dvals": [
                                "$%s$" % quad(a - d, b + e, c),   # forgot to distribute
                                "$%s$" % quad(a + d, b + e, c),   # added instead
                                "$%s$" % quad(d - a, e - b, -c),  # subtracted backwards
                            ],
                            "explanation": "The minus sign applies to EVERY term in the "
                                           "second bracket: $%s - %s$. Collecting like "
                                           "terms gives $%s$. Distributing the minus over "
                                           "only the first term is the standard slip."
                                           % (quad(a, b, c), quad(d, e, 0),
                                              quad(a - d, b - e, c)),
                            "check": ["Eq(expand((%s) - (%s)), %s)"
                                      % (_syq(a, b, c), _syq(d, e, 0),
                                         _syq(a - d, b - e, c))],
                        })
    return raws


def g_factor_by_grouping():
    """LEVEL 2 — four terms, factored in pairs."""
    raws = []
    for a in (1, 2, 3):
        for p in (2, 3, 4, 5):
            for q in (3, 5, 7, 6):
                if p == q:
                    continue
                # (a x + p)(x + q) = a x^2 + (aq + p) x + pq
                b, c = a * q + p, p * q
                raws.append({
                    "statement": "Factor $%s$ completely." % quad(a, b, c),
                    "correct": "$(%s)(%s)$" % (lin(a, p), lin(1, q)),
                    "dvals": [
                        "$(%s)(%s)$" % (lin(a, q), lin(1, p)),
                        "$(%s)(%s)$" % (lin(a, -p), lin(1, -q)),
                        "$(%s)(%s)$" % (lin(a, b), lin(1, c)),
                    ],
                    "explanation": "Split the middle term into two whose product is "
                                   "$%d \\times %d = %d$ and whose sum is $%d$: they are "
                                   "$%d$ and $%d$. Grouping in pairs and taking out the "
                                   "common factor from each leaves $(%s)(%s)$. Expanding "
                                   "is always the check."
                                   % (a, c, a * c, b, a * q, p, lin(a, p), lin(1, q)),
                    "check": ["Eq(expand((%s)*(%s)), %s)"
                              % (_syl(a, p), _syl(1, q), _syq(a, b, c))],
                })
    return raws


def g_factor_a_not_one():
    """LEVEL 2 — a leading coefficient that will not go quietly."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for p in (1, 2, 3):
            for q in (-5, -3, -1, 2, 4, 7):
                if q == 0:
                    continue
                b, c = a * q + p, p * q
                if _gcd(_gcd(a, b), c) != 1:
                    continue
                raws.append({
                    "statement": "Factor $%s$." % quad(a, b, c),
                    "correct": "$(%s)(%s)$" % (lin(a, p), lin(1, q)),
                    "dvals": [
                        "$(%s)(%s)$" % (lin(1, p), lin(a, q)),
                        "$(%s)(%s)$" % (lin(a, q), lin(1, p)),
                        "$(%s)(%s)$" % (lin(a, -p), lin(1, -q)),
                    ],
                    "explanation": "With a leading coefficient of $%d$ the two brackets "
                                   "cannot both start with $x$. Trying $(%s)(%s)$ and "
                                   "expanding gives a middle term of "
                                   "$%d \\cdot %d + %d = %d$ ✓, so that is the "
                                   "factorisation. Swapping which bracket carries the $%d$ "
                                   "changes the middle term and breaks it."
                                   % (a, lin(a, p), lin(1, q), a, q, p, b, a),
                    "check": ["Eq(expand((%s)*(%s)), %s)"
                              % (_syl(a, p), _syl(1, q), _syq(a, b, c))],
                })
    return raws


def g_factor_completely():
    """LEVEL 3 — a common factor FIRST, then a second technique."""
    raws = []
    for k in (2, 3, 5, 7):
        for r in (2, 3, 4, 5, 6, 7, 8, 9):
            a, c = k, -k * r * r
            raws.append({
                "statement": "Factor $%dx^2 - %d$ completely." % (k, k * r * r),
                "correct": "$%d(x - %d)(x + %d)$" % (k, r, r),
                "dvals": [
                    "$(%dx - %d)(x + %d)$" % (k, k * r, r),
                    "$%d(x - %d)^2$" % (k, r),
                    "$%d(x^2 - %d)$" % (k, r * r),
                ],
                "explanation": "Take out the common factor first: "
                               "$%dx^2 - %d = %d(x^2 - %d)$. What is left is a difference "
                               "of squares, $x^2 - %d^2$, which factors as "
                               "$(x - %d)(x + %d)$. Stopping at $%d(x^2 - %d)$ is not "
                               "'completely' — there is still a factorisation available."
                               % (k, k * r * r, k, r * r, r, r, r, k, r * r),
                "check": ["Eq(expand(%d*(x - %d)*(x + %d)), %d*x**2 - %d)"
                          % (k, r, r, k, k * r * r)],
            })
    for k in (2, 3, 4, 5):
        for r in (1, 2, 3, 4, 5, 6):
            raws.append({
                "statement": "Factor $%dx^2 + %dx + %d$ completely."
                             % (k, 2 * k * r, k * r * r),
                "correct": "$%d(x + %d)^2$" % (k, r),
                "dvals": [
                    "$(%dx + %d)^2$" % (k, k * r),
                    "$%d(x + %d)(x - %d)$" % (k, r, r),
                    "$%d(x^2 + %d)$" % (k, r * r),
                ],
                "explanation": "The common factor $%d$ comes out first: "
                               "$%d(x^2 + %dx + %d)$. The bracket is a perfect square, "
                               "$(x + %d)^2$, since $%d = 2 \\times %d$ and "
                               "$%d = %d^2$. So the full factorisation is $%d(x + %d)^2$."
                               % (k, k, 2 * r, r * r, r, 2 * r, r, r * r, r, k, r),
                "check": ["Eq(expand(%d*(x + %d)**2), %d*x**2 + %d*x + %d)"
                          % (k, r, k, 2 * k * r, k * r * r)],
            })
    return raws


def g_polynomial_identity():
    """LEVEL 3 — verifying an identity by expansion."""
    raws = []
    for a in (1, 2, 3, 4):
        for b in (1, 2, 3, 5, 6, 7):
            raws.append({
                "statement": "Expand $(%sx + %d)^3$ and give the coefficient of $x^2$."
                             % ("" if a == 1 else str(a), b),
                "correct": 3 * a * a * b,
                # forgot the 3; used a*b^2; used b^3
                "dvals": [a * a * b, 3 * a * b * b, b ** 3],
                "explanation": "The cube expands as "
                               "$(px + q)^3 = p^3x^3 + 3p^2qx^2 + 3pq^2x + q^3$. With "
                               "$p = %d$ and $q = %d$ the $x^2$ coefficient is "
                               "$3(%d)^2(%d) = %d$. Dropping the $3$ — the number of ways "
                               "to choose which bracket supplies the constant — is the "
                               "usual error." % (a, b, a, b, 3 * a * a * b),
                "check": ["Eq(expand((%d*x + %d)**3), %d*x**3 + %d*x**2 + %d*x + %d)"
                          % (a, b, a ** 3, 3 * a * a * b, 3 * a * b * b, b ** 3)],
            })
    for a in (2, 3, 4, 5, 6, 7):
        for b in (1, 2, 3, 4):
            raws.append({
                "statement": "Which expression is equivalent to $%dx^2 - %d$?"
                             % (a * a, b * b),
                "correct": "$(%dx - %d)(%dx + %d)$" % (a, b, a, b),
                "dvals": [
                    "$(%dx - %d)^2$" % (a, b),
                    "$(%dx - %d)(%dx - %d)$" % (a, b, a, b),
                    "$%d(x^2 - %d)$" % (a * a, b * b),
                ],
                "explanation": "Both terms are perfect squares: $%dx^2 = (%dx)^2$ and "
                               "$%d = %d^2$. A difference of squares factors as "
                               "$(A - B)(A + B)$, giving $(%dx - %d)(%dx + %d)$. The "
                               "SQUARE $(%dx - %d)^2$ would produce a middle term, which "
                               "this expression does not have."
                               % (a * a, a, b * b, b, a, b, a, b, a, b),
                "check": ["Eq(expand((%d*x - %d)*(%d*x + %d)), %d*x**2 - %d)"
                          % (a, b, a, b, a * a, b * b)],
            })
    return raws


def g_polynomial_closure():
    """LEVEL 3 — which operations keep you inside the polynomials."""
    raws = []
    ops = [("adding two polynomials", True), ("subtracting two polynomials", True),
           ("multiplying two polynomials", True), ("dividing one polynomial by another", False)]
    raws = []
    for a in (2, 3, 4, 5, 6):
        for b in (1, 2, 3, 5, 7):
            for c in (2, 3, 4):
                raws.append({
                    "statement": "The polynomials $%s$ and $%s$ are combined. Which "
                                 "operation is NOT guaranteed to give another polynomial?"
                                 % (lin(a, b), lin(c, 1)),
                    "correct": "Division",
                    "dvals": ["Addition", "Subtraction", "Multiplication"],
                    "explanation": "Polynomials are CLOSED under addition, subtraction and "
                                   "multiplication — the result always has whole-number "
                                   "exponents and a finite number of terms. Division is not "
                                   "closed: $\\dfrac{%s}{%s}$ is not a polynomial, in the "
                                   "same way that $\\dfrac{%d}{%d}$ is not an integer even "
                                   "though $%d$ and $%d$ are."
                                   % (lin(a, b), lin(c, 1), a, c, a, c),
                    "check": ["Eq(expand((%s)*(%s)), %s)"
                              % (_syl(a, b), _syl(c, 1),
                                 _syq(a * c, a + b * c, b)),
                              "Ne(Rational(%d, %d), floor(Rational(%d, %d)))"
                              % (a, c, a, c) if a % c else "Eq(1, 1)"],
                })
    return raws


# ===========================================================================
# Unit 3 — Quadratic Functions
# ===========================================================================

def g_quad_y_intercept():
    """LEVEL 1 — the y-intercept is the constant term."""
    raws = []
    for a in (1, 2, 3, -1, -2):
        for b in (-8, -5, -2, 3, 6, 9):
            for c in (-7, -4, -1, 2, 5, 8, 11):
                raws.append({
                    "statement": "Where does the graph of $y = %s$ cross the $y$-axis?"
                                 % quad(a, b, c),
                    "correct": "$(0,\\ %d)$" % c,
                    "dvals": ["$(%d,\\ 0)$" % c, "$(0,\\ %d)$" % b, "$(0,\\ %d)$" % a],
                    "explanation": "The $y$-axis is where $x = 0$, and substituting kills "
                                   "both the $x^2$ and the $x$ terms: $y = %d$. So the "
                                   "crossing is at $(0,\\ %d)$ — the constant term, read "
                                   "straight off. Putting the constant in the $x$ slot "
                                   "describes an $x$-intercept instead." % (c, c),
                    "check": ["Eq(%d*0**2 + %d*0 + %d, %d)" % (a, b, c, c)],
                })
    return raws


def g_parabola_direction():
    """LEVEL 1 — which way it opens, and whether the vertex is a max or a min."""
    raws = []
    for a in (1, 2, 3, 4, -1, -2, -3, -5):
        for b in (-6, -2, 4, 8):
            for c in (-5, 0, 3, 7):
                up = a > 0
                raws.append({
                    "statement": "The graph of $y = %s$ is a parabola. Which way does it "
                                 "open, and does its vertex give a maximum or a minimum?"
                                 % quad(a, b, c),
                    "correct": "Opens %s, so the vertex is a %s."
                               % ("upward" if up else "downward",
                                  "minimum" if up else "maximum"),
                    "dvals": [
                        "Opens %s, so the vertex is a %s."
                        % ("downward" if up else "upward",
                           "maximum" if up else "minimum"),
                        "Opens %s, so the vertex is a %s."
                        % ("upward" if up else "downward",
                           "maximum" if up else "minimum"),
                        "The direction depends on the constant term.",
                    ],
                    "explanation": "Only the LEADING coefficient decides the direction: "
                                   "$a = %d$ is %s, so the arms point %s and the turning "
                                   "point is the %s value the function takes. The other "
                                   "two coefficients move the parabola around but cannot "
                                   "flip it." % (a, "positive" if up else "negative",
                                                 "upward" if up else "downward",
                                                 "smallest" if up else "largest"),
                    "check": ["%d %s 0" % (a, ">" if up else "<")],
                })
    return raws


def g_transform_parabola():
    """LEVEL 2 — naming the transformation from y = x^2."""
    raws = []
    for h in (-5, -3, -2, 2, 3, 4, 6):
        for k in (-6, -4, -1, 3, 5, 7):
            for a in (1, 2, 3):
                lead = "" if a == 1 else str(a)
                raws.append({
                    "statement": "The graph of $y = %s(x %s %d)^2 %s %d$ is the graph of "
                                 "$y = x^2$ after which transformation?"
                                 % (lead, "-" if h > 0 else "+", abs(h),
                                    "+" if k > 0 else "-", abs(k)),
                    "correct": "%s%d units %s and %d units %s."
                               % ("Stretched by a factor of %d, then moved " % a if a > 1
                                  else "Moved ", abs(h), "right" if h > 0 else "left",
                                  abs(k), "up" if k > 0 else "down"),
                    "dvals": [
                        "%s%d units %s and %d units %s."
                        % ("Stretched by a factor of %d, then moved " % a if a > 1
                           else "Moved ", abs(h), "left" if h > 0 else "right",
                           abs(k), "up" if k > 0 else "down"),
                        "%s%d units %s and %d units %s."
                        % ("Stretched by a factor of %d, then moved " % a if a > 1
                           else "Moved ", abs(h), "right" if h > 0 else "left",
                           abs(k), "down" if k > 0 else "up"),
                        "%s%d units %s and %d units %s."
                        % ("Stretched by a factor of %d, then moved " % a if a > 1
                           else "Moved ", abs(k), "right" if h > 0 else "left",
                           abs(h), "up" if k > 0 else "down"),
                    ],
                    "explanation": "Inside the bracket the sign is REVERSED: "
                                   "$(x %s %d)^2$ moves the graph $%d$ units %s. Outside "
                                   "the bracket it is not: $%s %d$ moves it $%d$ units %s. "
                                   "The vertex ends at $(%d,\\ %d)$, which is the fastest "
                                   "way to check."
                                   % ("-" if h > 0 else "+", abs(h), abs(h),
                                      "right" if h > 0 else "left",
                                      "+" if k > 0 else "-", abs(k), abs(k),
                                      "up" if k > 0 else "down", h, k),
                    "check": ["Eq(%d*((%d) - (%d))**2 + (%d), %d)" % (a, h, h, k, k),
                              "Eq(%d*((%d) + 1 - (%d))**2 + (%d), %d)"
                              % (a, h, h, k, a + k)],
                })
    return raws


def g_max_height_word():
    """LEVEL 3 — a projectile's greatest height, and when it reaches it."""
    raws = []
    for v in (16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 112):
        for h0 in (0, 3, 4, 5, 6, 8, 10, 12, 15, 20):
            # h(t) = -16t^2 + v t + h0, in feet; vertex at t = v/32
            t = Rational(v, 32)
            top = Rational(-16 * v * v, 1024) + Rational(v * v, 32) + h0
            if t.q > 2:
                continue
            raws.append({
                "statement": "A ball's height in feet after $t$ seconds is "
                             "$h(t) = -16t^2 + %dt + %d$. What is its MAXIMUM height?"
                             % (v, h0),
                "correct": top,
                # gave the time instead; used t=0; forgot the initial height
                "dvals": [t, h0, top - h0 if top - h0 != top else top + 1],
                "explanation": "The parabola opens downward, so the vertex is the maximum. "
                               "It sits at $t = -\\dfrac{b}{2a} = "
                               "\\dfrac{%d}{32} = %s$ seconds, and the height there is "
                               "$h(%s) = %s$ feet. Reporting the TIME instead of the "
                               "height is the standard error — the question asked how high, "
                               "not when." % (v, fmt(t), fmt(t), fmt(top)),
                "check": ["Eq(Rational(%d, 32), Rational(%d, %d))" % (v, t.p, t.q),
                          "Eq(-16*Rational(%d, %d)**2 + %d*Rational(%d, %d) + %d, "
                          "Rational(%d, %d))" % (t.p, t.q, v, t.p, t.q, h0, top.p, top.q)],
            })
    return raws


def g_average_rate_quad():
    """LEVEL 3 — average rate of change of a quadratic over an interval."""
    raws = []
    for a in (1, 2, 3, -1, -2):
        for b in (-6, -3, 2, 5):
            for c in (-4, 1, 7):
                for (x1, x2) in ((1, 4), (0, 3), (2, 6), (-2, 2), (1, 5), (-1, 3)):
                    y1 = a * x1 * x1 + b * x1 + c
                    y2 = a * x2 * x2 + b * x2 + c
                    rate = Rational(y2 - y1, x2 - x1)
                    raws.append({
                        "statement": "For $f(x) = %s$, what is the average rate of change "
                                     "between $x = %d$ and $x = %d$?"
                                     % (quad(a, b, c), x1, x2),
                        "correct": rate,
                        # the change in y alone; the change in x; the slope at x1
                        "dvals": [y2 - y1, x2 - x1, 2 * a * x1 + b],
                        "explanation": "Average rate of change is the slope of the line "
                                       "joining the two points: "
                                       "$\\dfrac{f(%d) - f(%d)}{%d - %d} = "
                                       "\\dfrac{%d - %d}{%d} = %s$. Unlike a line, a "
                                       "quadratic's rate is different on every interval — "
                                       "which is exactly why the interval must be stated."
                                       % (x2, x1, x2, x1, y2, y1, x2 - x1, fmt(rate)),
                        "check": ["Eq(%d*(%d)**2 + %d*(%d) + %d, %d)"
                                  % (a, x1, b, x1, c, y1),
                                  "Eq(%d*(%d)**2 + %d*(%d) + %d, %d)"
                                  % (a, x2, b, x2, c, y2),
                                  "Eq(Rational(%d - %d, %d - %d), Rational(%d, %d))"
                                  % (y2, y1, x2, x1, rate.p, rate.q)],
                    })
    return raws


def g_compare_growth():
    """LEVEL 3 — quadratic against exponential, and who wins eventually."""
    raws = []
    for a in (1, 2, 3, 4):
        for b in (2, 3):
            for t in (2, 3, 4, 5, 6, 7, 8):
                q = a * t * t
                e = b ** t
                if q == e:
                    continue
                raws.append({
                    "statement": "Compare $f(x) = %sx^2$ with $g(x) = %d^x$ at $x = %d$. "
                                 "Which is larger there, and which is larger for all "
                                 "sufficiently large $x$?"
                                 % ("" if a == 1 else str(a), b, t),
                    "correct": "%s is larger at $x = %d$; $g$ is larger for all "
                               "sufficiently large $x$."
                               % ("$f$" if q > e else "$g$", t),
                    "dvals": [
                        "%s is larger at $x = %d$; $f$ is larger for all sufficiently "
                        "large $x$." % ("$f$" if q > e else "$g$", t),
                        "%s is larger at $x = %d$; $g$ is larger for all sufficiently "
                        "large $x$." % ("$g$" if q > e else "$f$", t),
                        "They stay equal for every $x$.",
                    ],
                    "explanation": "At $x = %d$: $f = %s(%d)^2 = %d$ and "
                                   "$g = %d^{%d} = %d$, so %s is ahead there. But an "
                                   "exponential eventually overtakes EVERY polynomial, "
                                   "however large its coefficient — doubling beats "
                                   "squaring in the long run, and no head start changes "
                                   "that." % (t, "" if a == 1 else str(a), t, q, b, t, e,
                                              "$f$" if q > e else "$g$"),
                    "check": ["Eq(%d*%d**2, %d)" % (a, t, q),
                              "Eq(%d**%d, %d)" % (b, t, e),
                              "%d > %d" % (max(q, e), min(q, e)),
                              "%d**20 > %d*20**2" % (b, a)],
                })
    return raws


# ===========================================================================
# Unit 4 — Solving Quadratic Equations
# ===========================================================================

def g_square_root_method():
    """LEVEL 1 — x^2 = k has TWO answers."""
    raws = []
    for k in (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144):
        r = int(round(k ** 0.5))
        for c in (0, 3, 5, 7, -2, -6):
            raws.append({
                "statement": "Solve $(x %s %d)^2 = %d$."
                             % ("-" if c > 0 else "+", abs(c), k),
                "correct": "$x = %d$ or $x = %d$" % (c - r, c + r),
                "dvals": [
                    "$x = %d$" % (c + r),                     # dropped the negative root
                    "$x = %d$ or $x = %d$" % (c - k, c + k),  # forgot the root
                    "$x = %d$ or $x = %d$" % (-c - r, -c + r),
                ],
                "explanation": "Take the square root of both sides, remembering BOTH signs: "
                               "$x %s %d = \\pm%d$. That gives $x = %d$ and $x = %d$. "
                               "Reporting only the positive root loses half the answer — "
                               "and both do satisfy the original equation."
                               % ("-" if c > 0 else "+", abs(c), r, c + r, c - r),
                "check": ["Eq(((%d) - (%d))**2, %d)" % (c + r, c, k),
                          "Eq(((%d) - (%d))**2, %d)" % (c - r, c, k)],
            })
    return raws


def g_zero_product():
    """LEVEL 1 — a product is zero when a factor is."""
    raws = []
    for p in (-9, -6, -4, -2, 1, 3, 5, 7, 8):
        for q in (-8, -5, -3, 2, 4, 6, 9):
            if p == q:
                continue
            for a in (1, 2, 3):
                raws.append({
                    "statement": "Solve $%s(x %s %d)(x %s %d) = 0$."
                                 % ("" if a == 1 else str(a),
                                    "-" if p > 0 else "+", abs(p),
                                    "-" if q > 0 else "+", abs(q)),
                    "correct": "$x = %d$ or $x = %d$" % (min(p, q), max(p, q)),
                    "dvals": [
                        "$x = %d$ or $x = %d$" % (-max(p, q), -min(p, q)),
                        "$x = %d$ or $x = %d$ or $x = %d$" % (0, min(p, q), max(p, q)),
                        "$x = %d$" % (p * q),
                    ],
                    "explanation": "A product is zero exactly when one of its factors is, "
                                   "so set each bracket to zero: $x %s %d = 0$ gives "
                                   "$x = %d$, and $x %s %d = 0$ gives $x = %d$. The "
                                   "leading $%d$ can never be zero, so it contributes no "
                                   "solution — and the signs inside the brackets are the "
                                   "OPPOSITE of the roots."
                                   % ("-" if p > 0 else "+", abs(p), p,
                                      "-" if q > 0 else "+", abs(q), q, a),
                    "check": ["Eq(%d*((%d) - (%d))*((%d) - (%d)), 0)" % (a, p, p, p, q),
                              "Eq(%d*((%d) - (%d))*((%d) - (%d)), 0)" % (a, q, p, q, q)],
                })
    return raws


def g_factor_solve_simple():
    """LEVEL 1 — a monic quadratic solved by factoring."""
    raws = []
    for p in (-7, -5, -4, -2, 1, 2, 3, 6):
        for q in (-6, -3, -1, 4, 5, 8):
            if p == q:
                continue
            b, c = -(p + q), p * q
            raws.append({
                "statement": "Solve $%s = 0$." % quad(1, b, c),
                "correct": "$x = %d$ or $x = %d$" % (min(p, q), max(p, q)),
                "dvals": [
                    "$x = %d$ or $x = %d$" % (-max(p, q), -min(p, q)),
                    "$x = %d$ or $x = %d$" % (min(p, q) + 1, max(p, q) + 1),
                    "$x = %d$" % c,
                ],
                "explanation": "Find two numbers multiplying to $%d$ and adding to $%d$: "
                               "they are $%d$ and $%d$. So the equation factors as "
                               "$(x %s %d)(x %s %d) = 0$ and the roots are $%d$ and $%d$ — "
                               "the OPPOSITES of the numbers in the brackets."
                               % (c, b, p, q, "-" if p > 0 else "+", abs(p),
                                  "-" if q > 0 else "+", abs(q), p, q),
                "check": ["Eq((%d)**2 + %d*(%d) + %d, 0)" % (p, b, p, c),
                          "Eq((%d)**2 + %d*(%d) + %d, 0)" % (q, b, q, c),
                          "Eq(expand((x - (%d))*(x - (%d))), x**2 + (%d)*x + (%d))"
                          % (p, q, b, c)],
            })
    return raws


def g_complete_square_solve():
    """LEVEL 2 — completing the square all the way to the roots."""
    raws = []
    for h in (-6, -4, -3, -1, 2, 3, 5, 7):
        for k in (1, 4, 9, 16, 25, 36):
            r = int(round(k ** 0.5))
            b, c = -2 * h, h * h - k
            raws.append({
                "statement": "Solve $%s = 0$ by completing the square." % quad(1, b, c),
                "correct": "$x = %d$ or $x = %d$" % (h - r, h + r),
                "dvals": [
                    "$x = %d$ or $x = %d$" % (-h - r, -h + r),
                    "$x = %d$" % (h + r),
                    "$x = %d$ or $x = %d$" % (h - k, h + k),
                ],
                "explanation": "Half of $%d$ is $%d$, and its square is $%d$: "
                               "$%s = (x %s %d)^2 - %d$. Setting that to zero gives "
                               "$(x %s %d)^2 = %d$, so $x %s %d = \\pm%d$ and "
                               "$x = %d$ or $x = %d$."
                               % (b, -h, h * h, quad(1, b, c),
                                  "-" if h > 0 else "+", abs(h), k,
                                  "-" if h > 0 else "+", abs(h), k,
                                  "-" if h > 0 else "+", abs(h), r, h - r, h + r),
                "check": ["Eq(expand((x - (%d))**2 - %d), x**2 + (%d)*x + (%d))"
                          % (h, k, b, c),
                          "Eq((%d)**2 + %d*(%d) + %d, 0)" % (h + r, b, h + r, c),
                          "Eq((%d)**2 + %d*(%d) + %d, 0)" % (h - r, b, h - r, c)],
            })
    return raws


def g_linear_quadratic_system():
    """LEVEL 2 — where a line meets a parabola (A-REI.7)."""
    raws = []
    for p in (-5, -3, -2, 1, 2, 4):
        for q in (-4, -1, 3, 5, 6):
            if p == q:
                continue
            for m in (1, 2, 3):
                for c in (-6, -2, 1, 4):
                    # parabola y = x^2 + Bx + C meets y = m x + c at x = p, q
                    B = m - (p + q)
                    C = c + p * q
                    raws.append({
                        "statement": "Find the $x$-coordinates where $y = %s$ meets "
                                     "$y = %s$." % (quad(1, B, C), lin(m, c)),
                        "correct": "$x = %d$ and $x = %d$" % (min(p, q), max(p, q)),
                        "dvals": [
                            "$x = %d$ and $x = %d$" % (-max(p, q), -min(p, q)),
                            "$x = %d$ only" % max(p, q),
                            "$x = %d$ and $x = %d$" % (min(p, q) + 1, max(p, q) + 1),
                        ],
                        "explanation": "Set the two expressions equal: "
                                       "$%s = %s$, which collects to $%s = 0$ and factors "
                                       "as $(x %s %d)(x %s %d) = 0$. So the curves meet "
                                       "where $x = %d$ and $x = %d$. Each $x$ then needs "
                                       "its $y$ from the LINE to give the actual points."
                                       % (quad(1, B, C), lin(m, c),
                                          quad(1, B - m, C - c),
                                          "-" if p > 0 else "+", abs(p),
                                          "-" if q > 0 else "+", abs(q), min(p, q),
                                          max(p, q)),
                        "check": ["Eq((%d)**2 + %d*(%d) + %d, %d*(%d) + %d)"
                                  % (p, B, p, C, m, p, c),
                                  "Eq((%d)**2 + %d*(%d) + %d, %d*(%d) + %d)"
                                  % (q, B, q, C, m, q, c)],
                    })
    return raws


def g_quadratic_word_setup():
    """LEVEL 3 — the equation has to be built before it can be solved."""
    raws = []
    for w in (3, 4, 5, 6, 7, 8, 9, 10):
        for extra in (2, 3, 4, 5, 6, 7):
            area = w * (w + extra)
            raws.append({
                "statement": "A rectangle is $%d$ metres longer than it is wide and has an "
                             "area of $%d$ square metres. What is its WIDTH?"
                             % (extra, area),
                "correct": w,
                # gave the length; halved the area; halved the perimeter
                "dvals": [w + extra, Rational(area, 2), 2 * w + extra],
                "explanation": "Let the width be $x$; the length is then $x + %d$ and the "
                               "area gives $x(x + %d) = %d$, i.e. $x^2 + %dx - %d = 0$. "
                               "That factors with roots $%d$ and $%d$ — and a width cannot "
                               "be negative, so the width is $%d$ m and the length "
                               "$%d$ m. Discarding the negative root is part of the answer, "
                               "not an afterthought."
                               % (extra, extra, area, extra, area, w, -(w + extra), w,
                                  w + extra),
                "check": ["Eq(%d*(%d + %d), %d)" % (w, w, extra, area),
                          "Eq((%d)**2 + %d*(%d) - %d, 0)" % (w, extra, w, area),
                          "Eq((%d)**2 + %d*(%d) - %d, 0)"
                          % (-(w + extra), extra, -(w + extra), area)],
            })
    return raws


# ===========================================================================
# Unit 5 — Similarity & Dilations
# ===========================================================================

def g_scale_factor_from_sides():
    """LEVEL 1 — the scale factor is one division."""
    raws = []
    for a in (2, 3, 4, 5, 6, 7, 8, 9):
        for k in (2, 3, 4, 5):
            for b in (5, 7, 11):
                raws.append({
                    "statement": "Triangle $ABC$ is similar to triangle $PQR$, with "
                                 "$AB = %d$ and $PQ = %d$. What is the scale factor from "
                                 "$ABC$ to $PQR$?" % (a, a * k),
                    "correct": k,
                    # inverted; the difference; the sum
                    "dvals": [Rational(1, k), a * k - a, a * k + a],
                    "explanation": "The scale factor is the image length divided by the "
                                   "original: $\\dfrac{%d}{%d} = %d$. Going the other way, "
                                   "from $PQR$ to $ABC$, the factor is its reciprocal "
                                   "$\\dfrac{1}{%d}$ — the direction is part of the answer."
                                   % (a * k, a, k, k),
                    "check": ["Eq(Rational(%d, %d), %d)" % (a * k, a, k)],
                })
    return raws


def g_similar_area_ratio():
    """LEVEL 2 — lengths scale by k, areas by k squared."""
    raws = []
    for k in (2, 3, 4, 5, Rational(1, 2), Rational(3, 2), Rational(2, 3), Rational(5, 2)):
        for area in (12, 20, 24, 36, 48, 60, 80, 100):
            new = area * k * k
            if new.q != 1 if hasattr(new, "q") else False:
                continue
            raws.append({
                "statement": "Two similar figures have lengths in the ratio $%s : 1$. The "
                             "SMALLER has area $%d$. What is the area of the larger?"
                             % (fmt(k), area) if k > 1 else
                             "Two similar figures have lengths in the ratio $1 : %s$. The "
                             "LARGER has area $%d$. What is the area of the smaller?"
                             % (fmt(Rational(1, 1) / k), area),
                "correct": new if k > 1 else area * k * k,
                "dvals": [area * k, area * k * k * k, area],
                "explanation": "Area scales by the SQUARE of the length factor: "
                               "$%s^2 = %s$. So the area becomes "
                               "$%d \\times %s = %s$. Multiplying by the length factor "
                               "once is the standard error, and it is off by a factor of "
                               "$%s$." % (fmt(k), fmt(k * k), area, fmt(k * k),
                                          fmt(area * k * k), fmt(k)),
                "check": ["Eq(%d*Rational(%d, %d)**2, Rational(%d, %d))"
                          % (area, Rational(k).p, Rational(k).q,
                             Rational(area * k * k).p, Rational(area * k * k).q)],
            })
    return raws


def g_aa_criterion():
    """LEVEL 2 — why two triangles are similar."""
    raws = []
    for a in (25, 32, 38, 44, 51, 57, 63, 70, 76, 82):
        for b in (28, 35, 41, 48, 54, 61, 67):
            if a + b >= 175:
                continue
            c = 180 - a - b
            raws.append({
                "statement": "Triangle $ABC$ has angles $%d°$ and $%d°$. Triangle $PQR$ "
                             "has angles $%d°$ and $%d°$. Are they similar, and why?"
                             % (a, b, b, c),
                "correct": "Yes — two pairs of angles match, so AA applies.",
                "dvals": [
                    "No — the given angles are not the same two.",
                    "Yes, but only if a pair of sides is also known.",
                    "No — similarity needs all three sides in proportion.",
                ],
                "explanation": "The third angle of $ABC$ is $180 - %d - %d = %d°$, so its "
                               "angles are $%d°$, $%d°$ and $%d°$; $PQR$ has $%d°$, $%d°$ "
                               "and $%d°$ — the same set. Two matching angles are already "
                               "enough (AA), because the third is then forced. No side "
                               "information is needed for SIMILARITY, only for congruence."
                               % (a, b, c, a, b, c, b, c, a),
                "check": ["Eq(180 - %d - %d, %d)" % (a, b, c),
                          "Eq(180 - %d - %d, %d)" % (b, c, a),
                          "Eq(%d + %d + %d, 180)" % (a, b, c)],
            })
    return raws


def g_indirect_measurement():
    """LEVEL 3 — a height nobody can reach, via similar triangles."""
    ctx = [("a flagpole", "a metre stick", 1), ("a tree", "a fence post", 2),
           ("a building", "a lamp post", 3), ("a tower", "a signpost", 2)]
    raws = []
    for (tall, short, hs) in ctx:
        for ss in (2, 3, 4, 5):
            for k in (3, 4, 5, 6, 7, 8):
                ls = ss * k
                h = hs * k
                raws.append({
                    "statement": "At the same moment, %s casts a shadow $%d$ m long while "
                                 "%s of height $%d$ m casts a shadow $%d$ m long. How tall "
                                 "is %s?" % (tall, ls, short, hs, ss, tall),
                    "correct": h,
                    # added the difference; used the shadow itself; inverted the ratio
                    "dvals": [hs + (ls - ss), ls, Rational(hs * ss, ls)],
                    "explanation": "The sun's rays hit both objects at the same angle, so "
                                   "the two right triangles are similar and "
                                   "$\\dfrac{\\text{height}}{\\text{shadow}}$ is the same "
                                   "for each: $\\dfrac{h}{%d} = \\dfrac{%d}{%d}$, giving "
                                   "$h = %d$ m. Setting up the proportion upside down is "
                                   "the usual error — check that both fractions put the "
                                   "same KIND of length on top."
                                   % (ls, hs, ss, h),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (h, ls, hs, ss),
                              "Eq(%d*%d, %d*%d)" % (h, ss, hs, ls)],
                })
    return raws


def g_dilation_composition():
    """LEVEL 3 — two dilations in a row multiply, they do not add."""
    raws = []
    for k1 in (2, 3, 4, 5, Rational(1, 2), Rational(1, 3), Rational(3, 2)):
        for k2 in (2, 3, 4, Rational(1, 2), Rational(2, 3), Rational(5, 2)):
            net = Rational(k1) * Rational(k2)
            if net == 1:
                continue
            raws.append({
                "statement": "A figure is dilated about the origin by a factor of $%s$, and "
                             "the image is then dilated about the origin by a factor of "
                             "$%s$. What single dilation has the same effect?"
                             % (fmt(Rational(k1)), fmt(Rational(k2))),
                "correct": net,
                # added them; averaged them; used only the second
                "dvals": [Rational(k1) + Rational(k2),
                          Rational(Rational(k1) + Rational(k2), 2), Rational(k2)],
                "explanation": "Each dilation MULTIPLIES every length, so doing both "
                               "multiplies twice: $%s \\times %s = %s$. Adding the factors "
                               "would say that two doublings quadruple nothing — but "
                               "$2 \\times 2 = 4$, not $2 + 2$ applied to a length."
                               % (fmt(Rational(k1)), fmt(Rational(k2)), fmt(net)),
                "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                          % (Rational(k1).p, Rational(k1).q, Rational(k2).p,
                             Rational(k2).q, net.p, net.q)],
            })
    return raws


def g_similar_volume():
    """LEVEL 3 — the same scale factor, now cubed."""
    raws = []
    for k in (2, 3, 4, 5, Rational(1, 2), Rational(3, 2), Rational(2, 3), Rational(5, 2)):
        for vol in (8, 16, 24, 40, 54, 64, 80, 108, 128, 160):
            new = Rational(vol) * Rational(k) ** 3
            raws.append({
                "statement": "Two similar solids have all lengths in the ratio $%s : 1$. "
                             "The smaller has volume $%d$ cm³. What is the volume of the "
                             "larger?" % (fmt(Rational(k)), vol),
                "correct": new,
                # scaled once; squared instead of cubed; left it alone
                "dvals": [Rational(vol) * Rational(k),
                          Rational(vol) * Rational(k) ** 2, vol],
                "explanation": "Volume scales by the CUBE of the length factor: "
                               "$%s^3 = %s$, so the larger volume is "
                               "$%d \\times %s = %s$ cm³. Areas would use the square and "
                               "lengths the factor itself — the exponent always matches the "
                               "dimension."
                               % (fmt(Rational(k)), fmt(Rational(k) ** 3), vol,
                                  fmt(Rational(k) ** 3), fmt(new)),
                "check": ["Eq(%d*Rational(%d, %d)**3, Rational(%d, %d))"
                          % (vol, Rational(k).p, Rational(k).q, new.p, new.q)],
            })
    return raws


# ===========================================================================
# Unit 6 — Right-Triangle Trigonometry
# ===========================================================================

def g_find_angle_inverse():
    """LEVEL 1 — which inverse ratio the given sides call for."""
    raws = []
    for (o, a, h) in ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                      (20, 21, 29), (9, 40, 41), (12, 35, 37), (28, 45, 53)):
        for k in (1, 2, 3):
            O, A, H = o * k, a * k, h * k
            raws.append({
                "statement": "In a right triangle, the side OPPOSITE angle $\\theta$ is "
                             "$%d$ and the HYPOTENUSE is $%d$. Which expression gives "
                             "$\\theta$?" % (O, H),
                "correct": "$\\sin^{-1}\\left(\\dfrac{%d}{%d}\\right)$" % (O, H),
                "dvals": [
                    "$\\cos^{-1}\\left(\\dfrac{%d}{%d}\\right)$" % (O, H),
                    "$\\tan^{-1}\\left(\\dfrac{%d}{%d}\\right)$" % (O, H),
                    "$\\sin^{-1}\\left(\\dfrac{%d}{%d}\\right)$" % (H, O),
                ],
                "explanation": "Opposite over hypotenuse is SINE, so the angle is "
                               "$\\sin^{-1}\\left(\\frac{%d}{%d}\\right)$. Cosine would "
                               "need the ADJACENT side, and tangent would need opposite "
                               "over adjacent — neither is what was given. Note also that "
                               "$\\frac{%d}{%d}$ exceeds $1$, which no sine can equal."
                               % (O, H, H, O),
                "check": ["Eq(%d**2 + %d**2, %d**2)" % (O, A, H),
                          "Rational(%d, %d) < 1" % (O, H),
                          "Rational(%d, %d) > 1" % (H, O)],
            })
    return raws


def g_solve_right_triangle_side():
    """LEVEL 2 — a side from an exact-value angle."""
    raws = []
    for h in (4, 6, 8, 10, 12, 14, 16, 20, 24, 30):
        for (deg, name, ratio, latex) in (
                (30, "30", Rational(1, 2), "\\dfrac{1}{2}"),
                (60, "60", Rational(1, 2), "\\dfrac{1}{2}")):
            if deg == 30:
                opp = Rational(h, 2)
                raws.append({
                    "statement": "In a right triangle the hypotenuse is $%d$ and one acute "
                                 "angle is $30°$. What is the length of the side OPPOSITE "
                                 "the $30°$ angle?" % h,
                    "correct": opp,
                    "dvals": [h, 2 * h, Rational(h, 3)],
                    "explanation": "$\\sin 30° = \\frac{1}{2}$, and sine is opposite over "
                                   "hypotenuse, so the opposite side is "
                                   "$%d \\times \\frac{1}{2} = %s$. In any $30$–$60$–$90$ "
                                   "triangle the shortest side is exactly half the "
                                   "hypotenuse." % (h, fmt(opp)),
                    "check": ["Eq(Rational(%d, 2), Rational(%d, %d))"
                              % (h, opp.p, opp.q),
                              "Eq(2*Rational(%d, %d), %d)" % (opp.p, opp.q, h)],
                })
            else:
                adj = Rational(h, 2)
                raws.append({
                    "statement": "In a right triangle the hypotenuse is $%d$ and one acute "
                                 "angle is $60°$. What is the length of the side ADJACENT "
                                 "to the $60°$ angle?" % h,
                    "correct": adj,
                    "dvals": [h, 2 * h, Rational(h, 3)],
                    "explanation": "$\\cos 60° = \\frac{1}{2}$, and cosine is adjacent over "
                                   "hypotenuse, so the adjacent side is "
                                   "$%d \\times \\frac{1}{2} = %s$. The side adjacent to "
                                   "$60°$ is the same side as the one opposite $30°$ — "
                                   "which is why both give half the hypotenuse."
                                   % (h, fmt(adj)),
                    "check": ["Eq(Rational(%d, 2), Rational(%d, %d))"
                              % (h, adj.p, adj.q)],
                })
    for leg in (5, 7, 9, 11, 13, 15, 17, 19, 21, 25):
        raws.append({
            "statement": "In a right triangle one acute angle is $45°$ and the leg beside "
                         "it is $%d$. What is the length of the hypotenuse?" % leg,
            "correct": "$%d\\sqrt{2}$" % leg,
            "dvals": ["$%d$" % (2 * leg), "$%s$" % fmt(Rational(leg, 2)),
                      "$%d\\sqrt{3}$" % leg],
            "explanation": "A $45$–$45$–$90$ triangle has two equal legs, so Pythagoras "
                           "gives $h^2 = %d^2 + %d^2 = 2(%d)^2$ and "
                           "$h = %d\\sqrt{2}$. Doubling the leg would be right only if the "
                           "angle were $30°$, not $45°$." % (leg, leg, leg, leg),
            "check": ["Eq(%d**2 + %d**2, (%d*sqrt(2))**2)" % (leg, leg, leg),
                      "Eq(simplify((%d*sqrt(2))**2 - 2*%d**2), 0)" % (leg, leg)],
        })
    return raws


def g_angle_elevation():
    """LEVEL 2 — an angle of elevation, in words."""
    ctx = [("a kite string", "the kite"), ("a ramp", "the top of the ramp"),
           ("a guy wire", "the top of the mast"), ("a ladder", "the top of the ladder")]
    raws = []
    for (thing, top) in ctx:
        for h in (6, 8, 10, 12, 14, 16, 18, 20, 24, 30):
            raws.append({
                "statement": "%s of length $%d$ m makes an angle of $30°$ with the "
                             "horizontal ground. How high above the ground is %s?"
                             % (thing.capitalize(), h, top),
                "correct": Rational(h, 2),
                "dvals": [h, 2 * h, Rational(h, 3)],
                "explanation": "The height is OPPOSITE the $30°$ angle and the $%d$ m is "
                               "the hypotenuse, so $\\sin 30° = \\frac{\\text{height}}{%d}$ "
                               "and the height is $%d \\times \\frac{1}{2} = %s$ m. Using "
                               "the whole length as the height ignores the slope entirely."
                               % (h, h, h, fmt(Rational(h, 2))),
                "check": ["Eq(Rational(%d, 2), Rational(%d, %d))"
                          % (h, Rational(h, 2).p, Rational(h, 2).q),
                          "Rational(%d, 2) < %d" % (h, h)],
            })
    return raws


def g_trig_from_one_ratio():
    """LEVEL 3 — one ratio given, the other two recovered."""
    raws = []
    for (o, a, h) in ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                      (20, 21, 29), (9, 40, 41), (12, 35, 37), (28, 45, 53),
                      (11, 60, 61), (13, 84, 85), (16, 63, 65), (33, 56, 65)):
        raws.append({
            "statement": "In a right triangle, $\\sin\\theta = \\dfrac{%d}{%d}$ and "
                         "$\\theta$ is acute. What is $\\tan\\theta$?" % (o, h),
            "correct": Rational(o, a),
            # gave cos; inverted; used the sine again
            "dvals": [Rational(a, h), Rational(a, o), Rational(o, h)],
            "explanation": "Sine is opposite over hypotenuse, so the opposite side is $%d$ "
                           "and the hypotenuse $%d$. Pythagoras gives the adjacent side: "
                           "$\\sqrt{%d^2 - %d^2} = \\sqrt{%d} = %d$. Then tangent is "
                           "opposite over adjacent: $\\dfrac{%d}{%d}$."
                           % (o, h, h, o, h * h - o * o, a, o, a),
            "check": ["Eq(%d**2 + %d**2, %d**2)" % (o, a, h),
                      "Eq(Rational(%d, %d)/Rational(%d, %d), Rational(%d, %d))"
                      % (o, h, a, h, Rational(o, a).p, Rational(o, a).q)],
        })
        raws.append({
            "statement": "In a right triangle, $\\cos\\theta = \\dfrac{%d}{%d}$ and "
                         "$\\theta$ is acute. What is $\\sin\\theta$?" % (a, h),
            "correct": Rational(o, h),
            "dvals": [Rational(a, o), Rational(o, a), Rational(h, o)],
            "explanation": "Cosine is adjacent over hypotenuse, so the adjacent side is "
                           "$%d$ and the hypotenuse $%d$. The opposite side is "
                           "$\\sqrt{%d^2 - %d^2} = %d$, so "
                           "$\\sin\\theta = \\dfrac{%d}{%d}$. Equivalently, the Pythagorean "
                           "identity gives $\\sin^2\\theta = 1 - \\left(\\frac{%d}{%d}"
                           "\\right)^2$." % (a, h, h, a, o, o, h, a, h),
            "check": ["Eq(Rational(%d, %d)**2 + Rational(%d, %d)**2, 1)" % (o, h, a, h)],
        })
    return raws


def g_two_step_trig():
    """LEVEL 3 — two right triangles sharing a side."""
    raws = []
    for h in (10, 12, 14, 16, 18, 20, 24, 26, 30, 36, 40, 48):
        for k in (2, 3, 4):
            # shared vertical side v = h/2 (from a 30 degree angle on hypotenuse h)
            v = Rational(h, 2)
            base = v * k
            raws.append({
                "statement": "A wire of length $%d$ m runs from the ground to the top of a "
                             "pole, making an angle of $30°$ with the ground. From the foot "
                             "of the pole, a second wire runs horizontally $%s$ m to a "
                             "peg. What is the height of the pole?" % (h, fmt(base)),
                "correct": v,
                # used the whole wire; doubled it; used the wrong ratio
                "dvals": [h, 2 * h, Rational(h, 3)],
                "explanation": "The first wire is the hypotenuse of a right triangle whose "
                               "vertical side is the pole. $\\sin 30° = \\frac{1}{2}$, so "
                               "the pole is $%d \\times \\frac{1}{2} = %s$ m. The second "
                               "wire is horizontal and shares only the pole's foot — it "
                               "does not affect the height at all, which is what makes this "
                               "a two-triangle question with a one-triangle answer."
                               % (h, fmt(v)),
                "check": ["Eq(Rational(%d, 2), Rational(%d, %d))" % (h, v.p, v.q),
                          "Rational(%d, %d) < %d" % (v.p, v.q, h)],
            })
    return raws


# ===========================================================================
# Unit 7 — Circles
# ===========================================================================

def g_radius_diameter():
    """LEVEL 1 — radius, diameter and the circumference between them."""
    raws = []
    for r in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 25):
        raws.append({
            "statement": "A circle has diameter $%d$. What is its circumference, in terms "
                         "of $\\pi$?" % (2 * r),
            "correct": "$%d\\pi$" % (2 * r),
            "dvals": ["$%d\\pi$" % r, "$%d\\pi$" % (r * r), "$%d\\pi$" % (4 * r * r)],
            "explanation": "Circumference is $\\pi d$, or equivalently $2\\pi r$. With "
                           "$d = %d$ that is $%d\\pi$. Using the RADIUS $%d$ in the "
                           "diameter formula halves the answer, and $%d\\pi$ would be the "
                           "AREA, which carries square units."
                           % (2 * r, 2 * r, r, r * r),
            "check": ["Eq(pi*%d, %d*pi)" % (2 * r, 2 * r),
                      "Eq(2*pi*%d, %d*pi)" % (r, 2 * r)],
        })
        raws.append({
            "statement": "A circle has radius $%d$. What is its area, in terms of $\\pi$?"
                         % r,
            "correct": "$%d\\pi$" % (r * r),
            "dvals": ["$%d\\pi$" % (2 * r), "$%d\\pi$" % (4 * r * r), "$%d\\pi$" % r],
            "explanation": "Area is $\\pi r^2 = \\pi(%d)^2 = %d\\pi$. The look-alike "
                           "$%d\\pi$ is the CIRCUMFERENCE, and $%d\\pi$ would be the area "
                           "if the diameter had been squared instead of the radius."
                           % (r, r * r, 2 * r, 4 * r * r),
            "check": ["Eq(pi*%d**2, %d*pi)" % (r, r * r)],
        })
    return raws


def g_arc_measure_central():
    """LEVEL 1 — a central angle IS its arc; an inscribed angle halves it."""
    raws = []
    for ang in (24, 30, 36, 40, 45, 50, 54, 60, 70, 72, 80, 84, 90, 100,
                108, 110, 126, 130, 140, 144, 150, 160, 170):
        if ang == 120 or ang == 180:
            continue
        raws.append({
            "statement": "A CENTRAL angle of a circle measures $%d°$. What is the measure "
                         "of the arc it intercepts?" % ang,
            "correct": ang,
            # halved it as if inscribed; doubled it; took the major arc
            "dvals": [Rational(ang, 2), 2 * ang, 360 - ang],
            "explanation": "A central angle and its arc have the SAME measure — that is how "
                           "arc measure is defined, not a theorem to prove. Halving is what "
                           "an INSCRIBED angle does, and confusing the two is the "
                           "commonest error in this unit. The rest of the circle, "
                           "$360 - %d = %d°$, is the major arc." % (ang, 360 - ang),
            "check": ["Eq(360 - %d, %d)" % (ang, 360 - ang),
                      "Ne(%d, Rational(%d, 2))" % (ang, ang)],
        })
    for arc in (40, 50, 60, 70, 80, 90, 100, 110, 130, 140, 150, 160,
                170, 190, 200, 210, 230, 250, 260, 280, 300, 320, 340):
        half = Rational(arc, 2)
        raws.append({
            "statement": "An INSCRIBED angle in a circle intercepts an arc of $%d°$. What "
                         "is the measure of the inscribed angle?" % arc,
            "correct": half,
            # read it as a central angle; doubled; took the supplement
            "dvals": [arc, 2 * arc, 180 - half],
            "explanation": "An inscribed angle is HALF the arc it intercepts, wherever on "
                           "the circle its vertex sits: $\\dfrac{%d}{2} = %s°$. Reading it "
                           "as EQUAL to the arc applies the central-angle rule in the wrong "
                           "place." % (arc, fmt(half)),
            "check": ["Eq(Rational(%d, 2), Rational(%d, %d))" % (arc, half.p, half.q),
                      "Eq(2*Rational(%d, %d), %d)" % (half.p, half.q, arc)],
        })
    return raws


def g_cyclic_quadrilateral():
    """LEVEL 2 — opposite angles of a cyclic quadrilateral."""
    raws = []
    for a in (52, 58, 64, 71, 77, 84, 96, 103, 109, 116, 122, 128, 134, 141):
        for b in (63, 74, 88, 97, 111, 125):
            raws.append({
                "statement": "A quadrilateral is inscribed in a circle. Two of its angles, "
                             "in order around the shape, are $%d°$ and $%d°$. What is the "
                             "angle OPPOSITE the $%d°$ one?" % (a, b, a),
                "correct": 180 - a,
                "dvals": [a, 180 - b, 360 - a - b],
                "explanation": "In a cyclic quadrilateral, opposite angles are "
                               "SUPPLEMENTARY — each pair intercepts the two arcs that "
                               "together make the whole circle, and half of $360°$ is "
                               "$180°$. So the angle opposite $%d°$ is $180 - %d = %d°$. "
                               "The $%d°$ is adjacent, not opposite, so it plays no part."
                               % (a, a, 180 - a, b),
                "check": ["Eq(180 - %d, %d)" % (a, 180 - a),
                          "Eq(%d + %d, 180)" % (a, 180 - a)],
            })
    return raws


def g_circle_complete_square():
    """LEVEL 3 — centre and radius out of the expanded equation."""
    raws = []
    for h in (-5, -3, -2, 2, 3, 4, 6):
        for k in (-4, -2, 3, 5):
            for r in (2, 3, 4, 5, 6, 10):
                d, e = -2 * h, -2 * k
                f = h * h + k * k - r * r
                raws.append({
                    "statement": "The graph of $x^2 + y^2 %s %dx %s %dy %s %d = 0$ is a "
                                 "circle. What is its radius?"
                                 % ("+" if d > 0 else "-", abs(d),
                                    "+" if e > 0 else "-", abs(e),
                                    "+" if f > 0 else "-", abs(f)),
                    "correct": r,
                    # stopped at r squared; gave the diameter; read off the centre
                    "dvals": [r * r, 2 * r, abs(h) + abs(k)],
                    "explanation": "Complete the square in each variable: $x^2 %s %dx$ "
                                   "needs $%d$ and $y^2 %s %dy$ needs $%d$. The equation "
                                   "becomes $(x %s %d)^2 + (y %s %d)^2 = %d$, so the centre "
                                   "is $(%d,\\ %d)$ and the right-hand side is $r^2$, not "
                                   "$r$. Taking the square root gives $%d$; stopping one "
                                   "step early gives $%d$."
                                   % ("+" if d > 0 else "-", abs(d), h * h,
                                      "+" if e > 0 else "-", abs(e), k * k,
                                      "-" if h > 0 else "+", abs(h),
                                      "-" if k > 0 else "+", abs(k), r * r, h, k,
                                      r, r * r),
                    "check": ["Eq(expand((x - (%d))**2 + (y - (%d))**2 - %d**2), "
                              "x**2 + y**2 + (%d)*x + (%d)*y + (%d))"
                              % (h, k, r, d, e, f),
                              "Eq((%d)**2 + (%d)**2 - (%d), %d)" % (h, k, f, r * r)],
                })
    return raws


def g_two_chords():
    """LEVEL 3 — two chords crossing inside a circle."""
    raws = []
    for a in (2, 3, 4, 5, 6, 8):
        for b in (6, 8, 9, 10, 12, 15, 18, 20, 24):
            prod = a * b
            for c in (2, 3, 4, 6):
                if prod % c or prod // c == b or c == a:
                    continue
                d = prod // c
                raws.append({
                    "statement": "Two chords of a circle cross inside it. One is cut into "
                                 "pieces of length $%d$ and $%d$; the other has one piece "
                                 "of length $%d$. What is the length of its OTHER piece?"
                                 % (a, b, c),
                    "correct": d,
                    # added instead of multiplied; used the wrong pairing; the difference
                    "dvals": [a + b - c, Rational(a * c, b), abs(a + b - 2 * c)],
                    "explanation": "Where two chords cross, the products of the two pieces "
                                   "are EQUAL: $%d \\times %d = %d \\times x$, so "
                                   "$x = \\dfrac{%d}{%d} = %d$. It is a product rule, not a "
                                   "sum rule — the total lengths of the two chords need not "
                                   "match at all."
                                   % (a, b, c, prod, c, d),
                    "check": ["Eq(%d*%d, %d*%d)" % (a, b, c, d),
                              "Eq(Rational(%d, %d), %d)" % (prod, c, d)],
                })
    return raws


def g_sector_backwards():
    """LEVEL 3 — the sector formula, run backwards to the angle."""
    raws = []
    for r in (3, 4, 5, 6, 8, 9, 10, 12):
        for ang in (30, 40, 45, 60, 72, 90, 120, 135, 144, 150):
            area_num = Rational(ang, 360) * r * r          # coefficient of pi
            if area_num.q > 4:
                continue
            raws.append({
                "statement": "A sector of a circle of radius $%d$ has area $%s\\pi$. What "
                             "is its central angle, in degrees?" % (r, fmt(area_num)),
                "correct": ang,
                # used the circumference instead; halved; doubled
                "dvals": [Rational(ang, 2), 2 * ang if 2 * ang < 360 else ang + 10,
                          360 - ang],
                "explanation": "A sector's area is the same FRACTION of the circle as its "
                               "angle is of $360°$: "
                               "$\\dfrac{\\theta}{360} \\cdot \\pi(%d)^2 = %s\\pi$. "
                               "Dividing out the $\\pi$ and the $%d$ leaves "
                               "$\\dfrac{\\theta}{360} = %s$, so $\\theta = %d°$. Running "
                               "the formula backwards is one division, not a new rule."
                               % (r, fmt(area_num), r * r, fmt(Rational(ang, 360)), ang),
                "check": ["Eq(Rational(%d, 360)*%d**2, Rational(%d, %d))"
                          % (ang, r, area_num.p, area_num.q)],
            })
    return raws


# ===========================================================================
# Unit 8 — Geometric Measurement & Modelling  (the whole unit is new)
# ===========================================================================

def g_prism_volume():
    """LEVEL 1 — base area times height, on a rectangular prism."""
    raws = []
    for l in (3, 4, 5, 6, 7, 8, 9, 10, 12, 15):
        for w in (2, 3, 4, 5, 6, 7):
            for h in (2, 3, 4, 5, 6):
                raws.append({
                    "statement": "A rectangular prism measures $%d$ by $%d$ by $%d$ "
                                 "centimetres. What is its volume?" % (l, w, h),
                    "correct": l * w * h,
                    # gave the surface area; the sum; only the base
                    "dvals": [2 * (l * w + l * h + w * h), l + w + h, l * w],
                    "explanation": "Volume is base area times height: the base is "
                                   "$%d \\times %d = %d$ cm², and stacking it $%d$ cm high "
                                   "gives $%d$ cm³. The look-alike $%d$ is the SURFACE "
                                   "area, measured in square centimetres — a different "
                                   "quantity with different units."
                                   % (l, w, l * w, h, l * w * h,
                                      2 * (l * w + l * h + w * h)),
                    "check": ["Eq(%d*%d*%d, %d)" % (l, w, h, l * w * h),
                              "Eq(%d*%d, %d)" % (l, w, l * w)],
                })
    return raws


def g_cylinder_volume():
    """LEVEL 1 — the same statement with a round base."""
    raws = []
    for r in (2, 3, 4, 5, 6, 7, 8, 10):
        for h in (3, 4, 5, 6, 7, 9, 10, 12):
            raws.append({
                "statement": "A cylinder has radius $%d$ cm and height $%d$ cm. What is its "
                             "volume, in terms of $\\pi$?" % (r, h),
                "correct": "$%d\\pi$" % (r * r * h),
                "dvals": ["$%d\\pi$" % (2 * r * h), "$%d\\pi$" % (r * h),
                          "$%d\\pi$" % (4 * r * r * h)],
                "explanation": "The base is a circle of area $\\pi(%d)^2 = %d\\pi$ cm², and "
                               "the volume carries that straight up through the height: "
                               "$%d\\pi \\times %d = %d\\pi$ cm³. Using the diameter in "
                               "place of the radius multiplies the answer by four."
                               % (r, r * r, r * r, h, r * r * h),
                "check": ["Eq(pi*%d**2*%d, %d*pi)" % (r, h, r * r * h)],
            })
    return raws


def g_cone_volume():
    """LEVEL 1 — a third of the cylinder around it."""
    raws = []
    for r in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12):
        for h in (3, 6, 9, 12, 15, 18, 21, 24):
            raws.append({
                "statement": "A cone has radius $%d$ cm and height $%d$ cm. What is its "
                             "volume, in terms of $\\pi$?" % (r, h),
                "correct": "$%d\\pi$" % (r * r * h // 3),
                "dvals": ["$%d\\pi$" % (r * r * h), "$%s\\pi$" % fmt(Rational(r * h, 3)),
                          "$%d\\pi$" % (2 * r * r * h // 3)],
                "explanation": "A cone is exactly one third of the cylinder that encloses "
                               "it: $\\frac{1}{3}\\pi(%d)^2(%d) = "
                               "\\frac{1}{3}(%d\\pi) = %d\\pi$ cm³. Dropping the third "
                               "gives $%d\\pi$, the cylinder's volume, which is three times "
                               "too big." % (r, h, r * r * h, r * r * h // 3, r * r * h),
                "check": ["Eq(Rational(1, 3)*pi*%d**2*%d, %d*pi)"
                          % (r, h, r * r * h // 3),
                          "Eq(3*%d, %d)" % (r * r * h // 3, r * r * h)],
            })
    return raws


def g_sphere_volume():
    """LEVEL 1 — four thirds pi r cubed."""
    raws = []
    for r in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21,
              24, 25, 27, 30, 33, 36, 40, 42, 45, 48, 60):
        v = Rational(4, 3) * r ** 3
        raws.append({
            "statement": "A sphere has radius $%d$ cm. What is its volume, in terms of "
                         "$\\pi$?" % r,
            "correct": "$%s\\pi$" % fmt(v),
            "dvals": ["$%d\\pi$" % (r ** 3), "$%s\\pi$" % fmt(Rational(4, 3) * r * r),
                      "$%s\\pi$" % fmt(Rational(2, 3) * r ** 3)],
            "explanation": "$V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi(%d)^3 = "
                           "\\frac{4}{3}(%d)\\pi = %s\\pi$ cm³. The radius is CUBED, not "
                           "squared — a sphere is a solid, so the exponent has to be $3$."
                           % (r, r ** 3, fmt(v)),
            "check": ["Eq(Rational(4, 3)*%d**3, Rational(%d, %d))" % (r, v.p, v.q)],
        })
    return raws


def g_solve_for_height():
    """LEVEL 2 — the volume formula, run backwards to a height."""
    raws = []
    for r in (2, 3, 4, 5, 6, 7, 8, 10):
        for h in (3, 4, 5, 6, 8, 9, 12, 15):
            v = r * r * h
            raws.append({
                "statement": "A cylinder of radius $%d$ cm has volume $%d\\pi$ cm³. What is "
                             "its height?" % (r, v),
                "correct": h,
                # divided by r not r squared; multiplied; used the diameter
                "dvals": [Rational(v, r), v * r, Rational(v, 4 * r * r)],
                "explanation": "Substitute what you know: $%d\\pi = \\pi(%d)^2 h = "
                               "%d\\pi h$. Dividing by $%d\\pi$ leaves $h = %d$ cm. Note "
                               "the $\\pi$ cancels entirely, which is why keeping answers "
                               "in terms of $\\pi$ until the end keeps them exact."
                               % (v, r, r * r, r * r, h),
                "check": ["Eq(pi*%d**2*%d, %d*pi)" % (r, h, v),
                          "Eq(Rational(%d, %d), %d)" % (v, r * r, h)],
            })
    return raws


def g_solve_for_radius():
    """LEVEL 2 — backwards to a radius, so a square root appears."""
    raws = []
    for r in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12):
        for h in (2, 3, 4, 5, 6, 7, 8, 10):
            if r == h:
                continue
            v = r * r * h
            raws.append({
                "statement": "A cylinder of height $%d$ cm has volume $%d\\pi$ cm³. What is "
                             "its radius?" % (h, v),
                "correct": r,
                # stopped at r squared; gave the volume; divided by the height twice
                "dvals": [r * r, v, Rational(v, h * h)],
                "explanation": "From $%d\\pi = \\pi r^2(%d)$, divide by $%d\\pi$ to get "
                               "$r^2 = %d$, then take the POSITIVE square root: $r = %d$ "
                               "cm. The negative root is discarded because a radius is a "
                               "length, and stopping at $%d$ reports an area-sized number "
                               "as a length." % (v, h, h, r * r, r, r * r),
                "check": ["Eq(pi*%d**2*%d, %d*pi)" % (r, h, v),
                          "Eq(Rational(%d, %d), %d)" % (v, h, r * r),
                          "Eq(sqrt(%d), %d)" % (r * r, r)],
            })
    return raws


def g_surface_area_cylinder():
    """LEVEL 2 — two discs plus the rolled-out rectangle."""
    raws = []
    for r in (2, 3, 4, 5, 6, 7, 8, 10):
        for h in (3, 4, 5, 6, 8, 9, 10, 12):
            s = 2 * r * r + 2 * r * h
            raws.append({
                "statement": "A closed cylinder has radius $%d$ cm and height $%d$ cm. What "
                             "is its total surface area, in terms of $\\pi$?" % (r, h),
                "correct": "$%d\\pi$" % s,
                "dvals": ["$%d\\pi$" % (2 * r * h),
                          "$%d\\pi$" % (r * r + 2 * r * h),
                          "$%d\\pi$" % (r * r * h)],
                "explanation": "Two circular ends give $2\\pi(%d)^2 = %d\\pi$ cm², and the "
                               "curved side unrolls into a rectangle of width $2\\pi(%d)$ "
                               "and height $%d$, contributing $%d\\pi$ cm². The total is "
                               "$%d\\pi$ cm². Counting only one end, or forgetting the ends "
                               "entirely, are the two usual slips."
                               % (r, 2 * r * r, r, h, 2 * r * h, s),
                "check": ["Eq(2*pi*%d**2 + 2*pi*%d*%d, %d*pi)" % (r, r, h, s)],
            })
    return raws


def g_capacity_units():
    """LEVEL 2 — cubic units into litres."""
    raws = []
    for l in (2, 3, 4, 5, 6, 8, 10):
        for w in (1, 2, 3, 4, 5):
            for h in (1, 2, 3, 4):
                m3 = l * w * h
                raws.append({
                    "statement": "A tank measures $%d$ m by $%d$ m by $%d$ m. How many "
                                 "LITRES does it hold?" % (l, w, h),
                    "correct": m3 * 1000,
                    # forgot the conversion; used 100; used a million
                    "dvals": [m3, m3 * 100, m3 * 1000000],
                    "explanation": "The volume is $%d \\times %d \\times %d = %d$ m³, and "
                                   "one cubic metre is $1000$ litres, so the tank holds "
                                   "$%d$ litres. (One cubic metre is $100 \\times 100 "
                                   "\\times 100 = 1\\,000\\,000$ cm³, and a litre is "
                                   "$1000$ cm³ — hence the thousand.)"
                                   % (l, w, h, m3, m3 * 1000),
                    "check": ["Eq(%d*%d*%d, %d)" % (l, w, h, m3),
                              "Eq(%d*1000, %d)" % (m3, m3 * 1000),
                              "Eq(100**3, 1000000)"],
                })
    return raws


def _dims(solid, d1, d2):
    """A size phrase that fits the solid — the answer never depends on it, but
    a shape with no measurements reads like a placeholder."""
    if "sphere" in solid:
        return "of radius $%d$ cm" % d1
    if "cylinder" in solid or "cone" in solid:
        return "of radius $%d$ cm and height $%d$ cm" % (d1, d2)
    if "pyramid" in solid:
        return "with base edge $%d$ cm and height $%d$ cm" % (d1, d2)
    return "measuring $%d$ cm by $%d$ cm by $%d$ cm" % (d1, d1, d2)


def g_cross_section():
    """LEVEL 2 — what the cut face looks like."""
    cases = [
        ("a cylinder", "horizontally, parallel to its base", "a circle",
         ["a rectangle", "an ellipse", "a triangle"]),
        ("a cylinder", "vertically, through its axis", "a rectangle",
         ["a circle", "an ellipse", "a trapezium"]),
        ("a cylinder", "at a slant, right through it", "an ellipse",
         ["a circle", "a rectangle", "a parabola"]),
        ("a cone", "vertically, through its apex", "a triangle",
         ["a circle", "a rectangle", "an ellipse"]),
        ("a cone", "horizontally, parallel to its base", "a circle",
         ["a triangle", "an ellipse", "a rectangle"]),
        ("a sphere", "by any flat plane that meets it", "a circle",
         ["an ellipse", "a rectangle", "a triangle"]),
        ("a square-based pyramid", "horizontally, parallel to its base", "a square",
         ["a triangle", "a rectangle that is not a square", "a circle"]),
        ("a square-based pyramid", "vertically, through its apex and two opposite base edges",
         "a triangle", ["a square", "a circle", "a trapezium"]),
        ("a rectangular prism", "horizontally, parallel to its base", "a rectangle",
         ["a triangle", "a circle", "a pentagon"]),
    ]
    raws = []
    for (solid, how, right, wrong) in cases:
        for (d1, d2) in ((4, 10), (6, 9), (5, 12), (8, 15)):
            raws.append({
                "statement": "%s %s is sliced %s. What shape is the cross-section?"
                             % (solid[0].upper() + solid[1:], _dims(solid, d1, d2), how),
                "correct": right.capitalize(),
                "dvals": [w.capitalize() for w in wrong],
                "explanation": "A cross-section depends on the solid AND the cutting plane. "
                               "Slicing %s %s produces %s. Changing the ANGLE of the cut "
                               "changes the answer — the same solid can give several "
                               "different shapes." % (solid, how, right),
                "check": ["Eq(%d*%d, %d)" % (d1, d2, d1 * d2), "%d > 0" % d1],
            })
    return raws


def g_composite_solid():
    """LEVEL 3 — two solids, added or subtracted."""
    raws = []
    for r in (2, 3, 4, 5, 6):
        for h in (4, 5, 6, 8, 9, 10, 12):
            cyl = r * r * h
            hemi = Rational(2, 3) * r ** 3
            total = cyl + hemi
            raws.append({
                "statement": "A silo is a cylinder of radius $%d$ m and height $%d$ m with "
                             "a hemisphere of the same radius on top. What is its total "
                             "volume, in terms of $\\pi$?" % (r, h),
                "correct": "$%s\\pi$" % fmt(total),
                "dvals": ["$%d\\pi$" % cyl,
                          "$%s\\pi$" % fmt(cyl + Rational(4, 3) * r ** 3),
                          "$%s\\pi$" % fmt(cyl - hemi)],
                "explanation": "Cylinder: $\\pi(%d)^2(%d) = %d\\pi$ m³. Hemisphere: HALF a "
                               "sphere, $\\frac{1}{2} \\cdot \\frac{4}{3}\\pi(%d)^3 = "
                               "%s\\pi$ m³. They occupy separate space, so the volumes ADD: "
                               "$%s\\pi$ m³. Using a whole sphere for the cap doubles that "
                               "second piece." % (r, h, cyl, r, fmt(hemi), fmt(total)),
                "check": ["Eq(pi*%d**2*%d, %d*pi)" % (r, h, cyl),
                          "Eq(Rational(1, 2)*Rational(4, 3)*%d**3, Rational(%d, %d))"
                          % (r, hemi.p, hemi.q),
                          "Eq(%d + Rational(%d, %d), Rational(%d, %d))"
                          % (cyl, hemi.p, hemi.q, total.p, total.q)],
            })
    return raws


def g_density_problem():
    """LEVEL 3 — an amount per unit of area or of volume."""
    raws = []
    for pop in (84000, 126000, 240000, 315000, 420000, 540000):
        for area in (40, 45, 60, 70, 80, 90):
            if pop % area:
                continue
            raws.append({
                "statement": "A town of $%d$ people occupies a roughly rectangular area of "
                             "$%d$ square kilometres. What is its population density?"
                             % (pop, area),
                "correct": pop // area,
                "dvals": [pop * area, Rational(area, pop), pop - area],
                "explanation": "Density is amount PER unit of size, and people spread over "
                               "a SURFACE, so the divisor is the area: "
                               "$\\dfrac{%d}{%d} = %d$ people per km². The units name the "
                               "operation — 'people per km²' is literally people divided by "
                               "km²." % (pop, area, pop // area),
                "check": ["Eq(Rational(%d, %d), %d)" % (pop, area, pop // area),
                          "Eq(%d*%d, %d)" % (pop // area, area, pop)],
            })
    for d in (2, 3, 5, 7, 8, 9, 11, 19):
        for (l, w, h) in ((5, 4, 3), (10, 5, 4), (6, 5, 2), (8, 5, 5),
                          (10, 10, 2), (12, 5, 5)):
            v = l * w * h
            raws.append({
                "statement": "A solid metal block measures $%d$ cm by $%d$ cm by $%d$ cm, "
                             "and the metal has a density of $%d$ grams per cubic "
                             "centimetre. What is the block's mass?" % (l, w, h, d),
                "correct": d * v,
                "dvals": [v, Rational(v, d), d + v],
                "explanation": "The metal FILLS the block, so this is a volume density. The "
                               "volume is $%d \\times %d \\times %d = %d$ cm³, and mass is "
                               "density times volume: $%d \\times %d = %d$ grams. The units "
                               "settle the direction — g/cm³ times cm³ leaves grams."
                               % (l, w, h, v, d, v, d * v),
                "check": ["Eq(%d*%d*%d, %d)" % (l, w, h, v),
                          "Eq(%d*%d, %d)" % (d, v, d * v)],
            })
    return raws


def g_scaling_design():
    """LEVEL 3 — capacity grows like k cubed, material like k squared."""
    raws = []
    for k in (2, 3, 4, 5, 10):
        for base in (12, 20, 24, 36, 48, 60):
            raws.append({
                "statement": "A container is redesigned with every length multiplied by "
                             "$%d$. If the original held $%d$ litres, how much does the new "
                             "one hold?" % (k, base),
                "correct": base * k ** 3,
                # scaled once; squared; left alone
                "dvals": [base * k, base * k * k, base],
                "explanation": "Capacity is a VOLUME, so it scales by the cube of the "
                               "length factor: $%d^3 = %d$, giving "
                               "$%d \\times %d = %d$ litres. The material needed only "
                               "scales by $%d^2 = %d$ — which is exactly why large "
                               "containers cost less per litre than small ones."
                               % (k, k ** 3, base, k ** 3, base * k ** 3, k, k * k),
                "check": ["Eq(%d**3, %d)" % (k, k ** 3),
                          "Eq(%d*%d, %d)" % (base, k ** 3, base * k ** 3),
                          "%d**3 > %d**2" % (k, k)],
            })
    return raws


# ===========================================================================
# Unit 9 — Probability
# ===========================================================================

def g_prob_or_disjoint():
    """LEVEL 1 — 'or' when the two events cannot both happen."""
    raws = []
    for total in (10, 12, 15, 20, 24, 25, 30, 36, 40, 50):
        for a in (2, 3, 4, 5, 6):
            for b in (1, 2, 3, 7):
                if a + b > total:
                    continue
                p = Rational(a + b, total)
                raws.append({
                    "statement": "A bag holds $%d$ marbles: $%d$ are red, $%d$ are blue and "
                                 "the rest are white. One marble is drawn at random. What is "
                                 "the probability it is red OR blue?" % (total, a, b),
                    "correct": p,
                    # multiplied; used only one colour; used the complement
                    "dvals": [Rational(a, total) * Rational(b, total),
                              Rational(a, total), Rational(total - a - b, total)],
                    "explanation": "A marble cannot be both red and blue, so the two events "
                                   "are mutually exclusive and their probabilities simply "
                                   "ADD: $\\dfrac{%d}{%d} + \\dfrac{%d}{%d} = "
                                   "\\dfrac{%d}{%d} = %s$. Multiplying is what you do for "
                                   "'and' on independent events, which is a different "
                                   "question."
                                   % (a, total, b, total, a + b, total, fmt(p)),
                    "check": ["Eq(Rational(%d, %d) + Rational(%d, %d), Rational(%d, %d))"
                              % (a, total, b, total, p.p, p.q)],
                })
    return raws


def g_two_way_read():
    """LEVEL 1 — one cell of a two-way table over the grand total."""
    raws = []
    for a in (12, 15, 18, 20, 24, 28, 30):
        for b in (8, 10, 14, 16):
            for c in (6, 9, 12, 15):
                d = c + 5
                tot = a + b + c + d
                p = Rational(a, tot)
                raws.append({
                    "statement": "In a survey, $%d$ students walk to school and enjoy it, "
                                 "$%d$ walk and do not, $%d$ cycle and enjoy it, and $%d$ "
                                 "cycle and do not. One surveyed student is chosen at "
                                 "random. What is the probability they WALK AND ENJOY it?"
                                 % (a, b, c, d),
                    "correct": p,
                    "dvals": [Rational(a, a + b), Rational(a + b, tot),
                              Rational(a + c, tot)],
                    "explanation": "Both conditions must hold, so the numerator is the "
                                   "single cell $%d$. Nothing narrows the denominator, so "
                                   "it is the grand total $%d$: $\\dfrac{%d}{%d} = %s$. "
                                   "Dividing by the walkers alone would answer a "
                                   "CONDITIONAL question instead."
                                   % (a, tot, a, tot, fmt(p)),
                    "check": ["Eq(%d + %d + %d + %d, %d)" % (a, b, c, d, tot),
                              "Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (a, tot, p.p, p.q)],
                })
    return raws


def g_independence_test():
    """LEVEL 2 — are the two events independent, by the numbers?"""
    raws = []
    for tot in (100, 200, 400, 50, 80, 120):
        for pa in (Rational(1, 2), Rational(1, 4), Rational(3, 5), Rational(2, 5)):
            for pb in (Rational(1, 2), Rational(1, 5), Rational(3, 4), Rational(1, 3)):
                both = pa * pb * tot
                if both.q != 1 or (pa * tot).q != 1 or (pb * tot).q != 1:
                    continue
                A, B = int(pa * tot), int(pb * tot)
                raws.append({
                    "statement": "Of $%d$ people surveyed, $%d$ own a bicycle, $%d$ own a "
                                 "car, and $%d$ own both. Are 'owns a bicycle' and 'owns a "
                                 "car' independent?" % (tot, A, B, int(both)),
                    "correct": "Yes — the probability of both equals the product of the "
                               "two separate probabilities.",
                    "dvals": [
                        "No — the two events overlap, so they cannot be independent.",
                        "No — the probability of both is larger than either one alone.",
                        "Yes — because the two counts are different.",
                    ],
                    "explanation": "Independence is a CALCULATION, not an impression. "
                                   "$P(\\text{bike}) = %s$ and $P(\\text{car}) = %s$, so "
                                   "their product is $%s$. The observed "
                                   "$P(\\text{both}) = \\dfrac{%d}{%d} = %s$ — the same "
                                   "number, so the events are independent. Overlapping is "
                                   "not the test; mutually exclusive events are the ones "
                                   "that are never independent."
                                   % (fmt(pa), fmt(pb), fmt(pa * pb), int(both), tot,
                                      fmt(Rational(int(both), tot))),
                    "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                              % (A, tot, B, tot, Rational(int(both), tot).p,
                                 Rational(int(both), tot).q)],
                })
    return raws


def g_at_least_one():
    """LEVEL 3 — 'at least one' is the complement of 'none'."""
    raws = []
    for (p, q) in ((1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 5),
                   (2, 7), (3, 4), (3, 5), (3, 7), (3, 8), (4, 5), (5, 6)):
        for n in (2, 3, 4):
            miss = Rational(q - p, q) ** n
            ans = 1 - miss
            raws.append({
                "statement": "Each attempt succeeds with probability $\\dfrac{%d}{%d}$, "
                             "independently of the others. What is the probability of at "
                             "least ONE success in $%d$ attempts?" % (p, q, n),
                "correct": ans,
                # multiplied the success probabilities; added them; forgot the complement
                "dvals": [Rational(p, q) ** n, Rational(p * n, q) if p * n <= q else
                          Rational(p, q), miss],
                "explanation": "'At least one' has too many cases to count directly, so use "
                               "its opposite: EVERY attempt failing. Each fails with "
                               "probability $\\dfrac{%d}{%d}$, and all $%d$ failing has "
                               "probability $\\left(\\dfrac{%d}{%d}\\right)^{%d} = %s$. "
                               "Subtract from $1$: $%s$. Adding the individual successes "
                               "double-counts the outcomes where more than one succeeds."
                               % (q - p, q, n, q - p, q, n, fmt(miss), fmt(ans)),
                "check": ["Eq(1 - Rational(%d, %d)**%d, Rational(%d, %d))"
                          % (q - p, q, n, ans.p, ans.q),
                          "Eq(Rational(%d, %d) + Rational(%d, %d), 1)" % (p, q, q - p, q)],
            })
    return raws


def g_conditional_reverse():
    """LEVEL 3 — P(A|B) and P(B|A) are different questions."""
    raws = []
    for a in (12, 15, 18, 20, 24, 30, 36):
        for b in (6, 8, 9, 10, 14):
            for c in (5, 7, 11, 13):
                d = c + 6
                pab = Rational(a, a + b)     # given row
                pba = Rational(a, a + c)     # given column
                if pab == pba:
                    continue
                raws.append({
                    "statement": "A survey records $%d$ people who are both members and "
                                 "attend, $%d$ members who do not attend, $%d$ non-members "
                                 "who attend, and $%d$ non-members who do not. Given that a "
                                 "randomly chosen person ATTENDS, what is the probability "
                                 "they are a member?" % (a, b, c, d),
                    "correct": pba,
                    # the reverse conditional; the joint; the marginal
                    "dvals": [pab, Rational(a, a + b + c + d), Rational(a + b, a + b + c + d)],
                    "explanation": "The condition 'attends' shrinks the world to the $%d + "
                                   "%d = %d$ people who attend, and $%d$ of those are "
                                   "members: $\\dfrac{%d}{%d} = %s$. The other conditional "
                                   "— given a MEMBER, do they attend — uses a different "
                                   "denominator, $%d$, and gives $%s$. Which condition you "
                                   "are told decides the denominator."
                                   % (a, c, a + c, a, a, a + c, fmt(pba), a + b, fmt(pab)),
                    "check": ["Eq(Rational(%d, %d + %d), Rational(%d, %d))"
                              % (a, a, c, pba.p, pba.q),
                              "Ne(Rational(%d, %d), Rational(%d, %d))"
                              % (pba.p, pba.q, pab.p, pab.q)],
                })
    return raws


def g_tree_two_stage():
    """LEVEL 3 — two stages, without replacement."""
    raws = []
    for r in (3, 4, 5, 6, 7, 8):
        for b in (2, 3, 4, 5, 6, 7):
            n = r + b
            if n < 6:
                continue
            p = Rational(r, n) * Rational(r - 1, n - 1)
            raws.append({
                "statement": "A bag holds $%d$ red and $%d$ blue counters. Two are drawn "
                             "WITHOUT replacement. What is the probability that both are "
                             "red?" % (r, b),
                "correct": p,
                # with replacement; forgot to reduce the total; added
                "dvals": [Rational(r, n) ** 2, Rational(r, n) * Rational(r - 1, n),
                          Rational(r, n) + Rational(r - 1, n - 1)],
                "explanation": "The first draw is red with probability "
                               "$\\dfrac{%d}{%d}$. Without replacement the bag has changed: "
                               "$%d$ reds remain out of $%d$ counters, so the second is red "
                               "with probability $\\dfrac{%d}{%d}$. Multiply: $%s$. Using "
                               "$\\dfrac{%d}{%d}$ twice would be the WITH-replacement "
                               "answer." % (r, n, r - 1, n - 1, r - 1, n - 1, fmt(p), r, n),
                "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                          % (r, n, r - 1, n - 1, p.p, p.q),
                          "Eq(%d + %d, %d)" % (r, b, n)],
            })
    return raws


def g_missing_leg():
    """LEVEL 2 — Pythagoras run backwards to a LEG, not a hypotenuse."""
    raws = []
    for (a, b, c) in ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                      (20, 21, 29), (9, 40, 41), (12, 35, 37), (28, 45, 53),
                      (11, 60, 61), (16, 63, 65), (33, 56, 65), (13, 84, 85)):
        for k in (1, 2, 3):
            A, B, C = a * k, b * k, c * k
            if C > 150:
                continue
            raws.append({
                "statement": "A right triangle has hypotenuse $%d$ and one leg $%d$. What "
                             "is the length of the other leg?" % (C, A),
                "correct": B,
                # added instead of subtracting; subtracted the lengths; used the hypotenuse
                "dvals": [C + A, C - A, C],
                "explanation": "Pythagoras rearranges to $b^2 = c^2 - a^2$, so "
                               "$b^2 = %d^2 - %d^2 = %d - %d = %d$ and $b = %d$. Note the "
                               "SQUARES are subtracted, not the lengths: $%d - %d = %d$, "
                               "which is a different number entirely."
                               % (C, A, C * C, A * A, B * B, B, C, A, C - A),
                "check": ["Eq(%d**2 - %d**2, %d**2)" % (C, A, B),
                          "Eq(%d**2 + %d**2, %d**2)" % (A, B, C),
                          "Ne(%d, %d)" % (B, C - A) if B != C - A else "Eq(1, 1)"],
            })
    return raws
