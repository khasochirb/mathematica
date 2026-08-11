# -*- coding: utf-8 -*-
"""Integrated Math 3 — bringing every unit's bank to twelve forms.

IM3 already had a Level 3 in every unit, but the unit sizes were uneven —
four units sat at 120–170 problems while others held 250+. This module adds
41 forms so every unit carries twelve, with roughly four Level 1, five
Level 2 and three Level 3.

Unit 4 also picks up the Law of Sines and Law of Cosines, added to the
course in the same batch: general triangles were the last piece of the
CCSS integrated pathway with no lesson anywhere in three years.

Same contract as scripts/pb/integrated_3.py: answers computed from named
parameters, one named student error per distractor, every check[] asserted
by the gate.
"""
from sympy import Rational, sqrt

from imbank import fmt, lin, quad, xpm  # noqa: F401


def _syq(a, b, c):
    """`ax^2 + bx + c` in SYMPY syntax — quad() renders LaTeX, which does not
    sympify (the missing `*` between coefficient and variable is the trap)."""
    return "(%d)*x**2 + (%d)*x + (%d)" % (a, b, c)


def _gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# ===========================================================================
# Unit 1 — Polynomial Functions
# ===========================================================================

def g_poly_evaluate():
    """LEVEL 1 — one substitution into a cubic."""
    raws = []
    for a in (1, 2, 3, -1, -2):
        for b in (-5, -2, 3, 6):
            for c in (-8, -3, 4, 7):
                for k in (-2, -1, 2, 3):
                    v = a * k ** 3 + b * k + c
                    raws.append({
                        "statement": "If $p(x) = %sx^3 %s %dx %s %d$, what is $p(%d)$?"
                                     % ("" if a == 1 else ("-" if a == -1 else str(a)),
                                        "+" if b > 0 else "-", abs(b),
                                        "+" if c > 0 else "-", abs(c), k),
                        "correct": v,
                        # cubed after multiplying; used k^2; dropped the constant
                        "dvals": [(a * k) ** 3 + b * k + c, a * k ** 2 + b * k + c,
                                  a * k ** 3 + b * k],
                        "explanation": "Substitute $%d$ everywhere: "
                                       "$%d(%d)^3 + %d(%d) + %d = %d + %d + %d = %d$. The "
                                       "exponent applies to $x$ ALONE, so cube first and "
                                       "multiply by $%d$ afterwards — doing it the other "
                                       "way round gives $%d$."
                                       % (k, a, k, b, k, c, a * k ** 3, b * k, c, v, a,
                                          (a * k) ** 3 + b * k + c),
                        "check": ["Eq(%d*(%d)**3 + %d*(%d) + %d, %d)"
                                  % (a, k, b, k, c, v)],
                    })
    return raws


def g_poly_from_zeros():
    """LEVEL 2 — building a polynomial from what it is meant to vanish at."""
    raws = []
    for p in (-4, -3, -2, -1, 1, 2, 3, 5):
        for q in (-5, -2, 1, 3, 4, 6):
            if p == q or p + q == 0:
                continue
            for a in (1, 2, 3):
                b, c = -a * (p + q), a * p * q
                raws.append({
                    "statement": "A quadratic has zeros $%d$ and $%d$ and a leading "
                                 "coefficient of $%d$. What is it, in expanded form?"
                                 % (p, q, a),
                    "correct": "$%s$" % quad(a, b, c),
                    "dvals": [
                        "$%s$" % quad(a, -b, c),      # zeros read straight in, sign unflipped
                        "$%s$" % quad(a, b, -c),      # sign slip on the constant
                        "$%s$" % quad(a, b + a, c),   # arithmetic slip in the middle term
                    ],
                    "explanation": "A zero at $%d$ means a factor of $(x %s %d)$ — the "
                                   "SIGN flips. So the polynomial is "
                                   "$%d(x %s %d)(x %s %d)$, which expands to $%s$. Reading "
                                   "the zeros straight into the brackets without flipping "
                                   "gives the wrong middle term."
                                   % (p, "-" if p > 0 else "+", abs(p), a,
                                      "-" if p > 0 else "+", abs(p),
                                      "-" if q > 0 else "+", abs(q), quad(a, b, c)),
                    "check": ["Eq(expand(%d*(x - (%d))*(x - (%d))), %s)"
                              % (a, p, q, _syq(a, b, c)),
                              "Eq(%d*(%d)**2 + %d*(%d) + %d, 0)" % (a, p, b, p, c),
                              "Eq(%d*(%d)**2 + %d*(%d) + %d, 0)" % (a, q, b, q, c)],
                })
    return raws


def g_vieta_cubic():
    """LEVEL 2 — the sum and product of a cubic's roots, without solving."""
    raws = []
    for r1 in (-4, -2, 1, 2, 3):
        for r2 in (-3, -1, 2, 4, 5):
            for r3 in (-5, 1, 3, 6):
                if len({r1, r2, r3}) < 3:
                    continue
                s = r1 + r2 + r3
                pr = r1 * r2 * r3
                b = -s
                d = -pr
                cc = r1 * r2 + r1 * r3 + r2 * r3
                raws.append({
                    "statement": "The equation $x^3 %s %dx^2 %s %dx %s %d = 0$ has three "
                                 "real roots. What is their SUM?"
                                 % ("+" if b > 0 else "-", abs(b),
                                    "+" if cc > 0 else "-", abs(cc),
                                    "+" if d > 0 else "-", abs(d)),
                    "correct": s,
                    # sign not flipped; gave the product; gave the middle coefficient
                    "dvals": [b, pr, cc],
                    "explanation": "For $x^3 + bx^2 + cx + d = 0$ the roots sum to $-b$ — "
                                   "expanding $(x - r_1)(x - r_2)(x - r_3)$ puts "
                                   "$-(r_1 + r_2 + r_3)$ in the $x^2$ slot. Here $b = %d$, "
                                   "so the sum is $%d$. No solving is needed, and the "
                                   "product $%d$ answers a different question."
                                   % (b, s, pr),
                    "check": ["Eq(expand((x - (%d))*(x - (%d))*(x - (%d))), "
                              "x**3 + (%d)*x**2 + (%d)*x + (%d))"
                              % (r1, r2, r3, b, cc, d),
                              "Eq((%d) + (%d) + (%d), %d)" % (r1, r2, r3, s)],
                })
    return raws


def g_factor_theorem_k():
    """LEVEL 2 — choose the constant that makes a given binomial a factor."""
    raws = []
    for a in (1, 2, 3):
        for r in (-4, -3, -2, -1, 1, 2, 3, 4):
            for b in (-6, -2, 5, 9):
                # p(x) = a x^3 + b x + k, want p(r) = 0
                k = -(a * r ** 3 + b * r)
                if k == 0:
                    continue
                raws.append({
                    "statement": "For what value of $k$ is $(x %s %d)$ a factor of "
                                 "$%sx^3 %s %dx + k$?"
                                 % ("-" if r > 0 else "+", abs(r),
                                    "" if a == 1 else str(a),
                                    "+" if b > 0 else "-", abs(b)),
                    "correct": k,
                    # sign flipped; substituted into the cubic term only; into the
                    # linear term only
                    "dvals": [-k, -(a * r ** 3), -(b * r)],
                    "explanation": "The factor theorem: $(x %s %d)$ divides $p(x)$ exactly "
                                   "when $p(%d) = 0$. So "
                                   "$%d(%d)^3 + %d(%d) + k = 0$, giving "
                                   "$%d + k = 0$ and $k = %d$. Note the factor "
                                   "$(x %s %d)$ tests the value $%d$ — the OPPOSITE sign "
                                   "to the one in the bracket."
                                   % ("-" if r > 0 else "+", abs(r), r, a, r, b, r,
                                      -k, k, "-" if r > 0 else "+", abs(r), r),
                    "check": ["Eq(%d*(%d)**3 + %d*(%d) + (%d), 0)" % (a, r, b, r, k)],
                })
    return raws


def g_poly_sign():
    """LEVEL 3 — where a factored polynomial is positive."""
    raws = []
    for p in (-5, -4, -3, -2, -1):
        for q in (0, 1, 2, 3):
            for r in (4, 5, 6, 7):
                if len({p, q, r}) < 3:
                    continue
                raws.append({
                    "statement": "For $f(x) = %s%s%s$, on which interval is $f(x)$ "
                                 "POSITIVE?" % (xpm(-p), xpm(-q), xpm(-r)),
                    "correct": "$%d < x < %d$" % (p, q),
                    "dvals": [
                        "$x < %d$" % p,
                        "$%d < x < %d$" % (q, r),
                        "$%d < x < %d$" % (p, r),
                    ],
                    "explanation": "The zeros $%d$, $%d$ and $%d$ cut the line into four "
                                   "pieces, and the sign flips at each (every factor is "
                                   "simple). To the right of $%d$ all three factors are "
                                   "positive, so $f > 0$ there; walking left, the sign "
                                   "alternates $+,\\ -,\\ +,\\ -$. The interval "
                                   "$%d < x < %d$ is the second positive stretch — testing "
                                   "one point in each piece is the reliable method."
                                   % (p, q, r, r, p, q),
                    "check": ["(Rational(%d, %d) - (%d))*(Rational(%d, %d) - (%d))*"
                              "(Rational(%d, %d) - (%d)) > 0"
                              % (p + q, 2, p, p + q, 2, q, p + q, 2, r),
                              "(%d - (%d))*(%d - (%d))*(%d - (%d)) > 0"
                              % (r + 1, p, r + 1, q, r + 1, r)],
                })
    return raws


def g_equate_coefficients():
    """LEVEL 3 — two expressions are identical, so their coefficients match."""
    raws = []
    for a in (1, 2, 3, 4):
        for p in (-5, -3, -1, 2, 4, 6):
            for q in (-4, -2, 1, 3, 5, 7):
                if p == q:
                    continue
                b, c = a * (p + q), a * p * q
                raws.append({
                    "statement": "For all $x$, $%s = %d(x + A)(x + B)$ where $A$ and $B$ "
                                 "are constants. What is $A + B$?" % (quad(a, b, c), a),
                    "correct": p + q,
                    # gave the product; the middle coefficient; the constant
                    "dvals": [p * q, b, c],
                    "explanation": "Expanding the right side gives "
                                   "$%dx^2 + %d(A + B)x + %dAB$. Two expressions equal for "
                                   "ALL $x$ must match coefficient by coefficient, so "
                                   "$%d(A + B) = %d$ and $A + B = %d$. Nothing has to be "
                                   "solved for $A$ and $B$ individually."
                                   % (a, a, a, a, b, p + q),
                    "check": ["Eq(expand(%d*(x + (%d))*(x + (%d))), %s)"
                              % (a, p, q, _syq(a, b, c)),
                              "Eq(%d*((%d) + (%d)), %d)" % (a, p, q, b)],
                })
    return raws


# ===========================================================================
# Unit 2 — Rational & Radical Functions
# ===========================================================================

def g_rational_domain():
    """LEVEL 1 — the values the denominator forbids."""
    raws = []
    for p in (-6, -4, -3, -1, 2, 3, 5, 7):
        for q in (-5, -2, 1, 4, 6, 8):
            if p == q:
                continue
            raws.append({
                "statement": "What values must be excluded from the domain of "
                             "$f(x) = \\dfrac{x + 1}{(x %s %d)(x %s %d)}$?"
                             % ("-" if p > 0 else "+", abs(p),
                                "-" if q > 0 else "+", abs(q)),
                "correct": "$x = %d$ and $x = %d$" % (min(p, q), max(p, q)),
                "dvals": [
                    "$x = %d$ and $x = %d$" % (-max(p, q), -min(p, q)),
                    "$x = -1$",
                    "$x = %d$, $x = %d$ and $x = -1$" % (min(p, q), max(p, q)),
                ],
                "explanation": "Division by zero is undefined, so the excluded values are "
                               "exactly where the DENOMINATOR vanishes: $x = %d$ and "
                               "$x = %d$. The numerator's zero at $x = -1$ makes the "
                               "function zero, not undefined — a completely different "
                               "thing." % (p, q),
                "check": ["Eq(((%d) - (%d))*((%d) - (%d)), 0)" % (p, p, p, q),
                          "Eq(((%d) - (%d))*((%d) - (%d)), 0)" % (q, p, q, q)],
            })
    return raws


def g_multiply_rational():
    """LEVEL 1 — multiply two rational expressions and cancel."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for b in (3, 5, 7, 8, 9):
            for m in (1, 2, 3):
                for n in (2, 3, 4):
                    if _gcd(a * m, b * n) != 1 and a * m != b * n:
                        pass
                    num, den = a * m, b * n
                    g = _gcd(num, den)
                    raws.append({
                        "statement": "Simplify $\\dfrac{%dx}{%d} \\cdot "
                                     "\\dfrac{%d}{%dx^2}$ for $x \\ne 0$."
                                     % (a, b, m, n),
                        "correct": "$\\dfrac{%d}{%dx}$" % (num // g, den // g),
                        "dvals": [
                            "$\\dfrac{%dx}{%d}$" % (num // g, den // g),
                            "$\\dfrac{%d}{%dx^2}$" % (num // g, den // g),
                            "$\\dfrac{%d}{%dx}$" % (den // g, num // g),
                        ],
                        "explanation": "Multiply straight across: "
                                       "$\\dfrac{%dx \\cdot %d}{%d \\cdot %dx^2} = "
                                       "\\dfrac{%dx}{%dx^2}$. One power of $x$ cancels, "
                                       "leaving $\\dfrac{%d}{%dx}$ after dividing the "
                                       "numbers by $%d$. The $x$ ends up DOWNSTAIRS "
                                       "because the denominator carried the higher power."
                                       % (a, m, b, n, num, den, num // g, den // g, g),
                        "check": ["Eq(simplify(Rational(%d,%d)*x*Rational(%d,%d)/x**2 - "
                                  "Rational(%d,%d)/x), 0)"
                                  % (a, b, m, n, num // g, den // g)],
                    })
    return raws


def g_radical_domain():
    """LEVEL 1 — a square root needs a non-negative inside."""
    raws = []
    for a in (1, 2, 3, 4, 5):
        for b in (-12, -9, -6, -3, 2, 5, 8, 11):
            lo = Rational(-b, a)
            raws.append({
                "statement": "What is the domain of $f(x) = \\sqrt{%s}$?" % lin(a, b),
                "correct": "$x \\ge %s$" % fmt(lo),
                "dvals": [
                    "$x \\le %s$" % fmt(lo),
                    "$x \\ge %s$" % fmt(-lo),
                    "all real numbers",
                ],
                "explanation": "A square root is only defined when what is inside is at "
                               "least zero: $%s \\ge 0$, so $%dx \\ge %d$ and "
                               "$x \\ge %s$. Because $%d$ is positive the inequality sign "
                               "does not turn round."
                               % (lin(a, b), a, -b, fmt(lo), a),
                "check": ["Eq(%d*Rational(%d, %d) + (%d), 0)" % (a, lo.p, lo.q, b),
                          "%d*(Rational(%d, %d) + 1) + (%d) > 0" % (a, lo.p, lo.q, b)],
            })
    return raws


def g_add_rational():
    """LEVEL 2 — unlike denominators, combined."""
    raws = []
    for a in (1, 2, 3, 4, 5):
        for b in (2, 3, 4, 6, 7):
            for p in (-5, -3, 2, 4):
                for q in (-4, 1, 3, 6):
                    if p == q:
                        continue
                    num = a * q + b * p          # a(x+q) + b(x+p) constant part
                    raws.append({
                        "statement": "Write $\\dfrac{%d}{x %s %d} + \\dfrac{%d}{x %s %d}$ "
                                     "as a single fraction."
                                     % (a, "+" if p > 0 else "-", abs(p),
                                        b, "+" if q > 0 else "-", abs(q)),
                        "correct": "$\\dfrac{%s}{(x %s %d)(x %s %d)}$"
                                   % (lin(a + b, num), "+" if p > 0 else "-", abs(p),
                                      "+" if q > 0 else "-", abs(q)),
                        "dvals": [
                            "$\\dfrac{%d}{(x %s %d)(x %s %d)}$"
                            % (a + b, "+" if p > 0 else "-", abs(p),
                               "+" if q > 0 else "-", abs(q)),
                            "$\\dfrac{%d}{x %s %d}$"
                            % (a + b, "+" if p + q > 0 else "-", abs(p + q)),
                            "$\\dfrac{%s}{(x %s %d) + (x %s %d)}$"
                            % (lin(a + b, num), "+" if p > 0 else "-", abs(p),
                               "+" if q > 0 else "-", abs(q)),
                        ],
                        "explanation": "The common denominator is the PRODUCT of the two "
                                       "brackets. Rewriting each fraction over it gives "
                                       "$\\dfrac{%d(x %s %d) + %d(x %s %d)}"
                                       "{(x %s %d)(x %s %d)}$, and the numerator collects "
                                       "to $%s$. Adding the numerators without rewriting — "
                                       "or adding the denominators — are the two standard "
                                       "errors."
                                       % (a, "+" if q > 0 else "-", abs(q),
                                          b, "+" if p > 0 else "-", abs(p),
                                          "+" if p > 0 else "-", abs(p),
                                          "+" if q > 0 else "-", abs(q),
                                          lin(a + b, num)),
                        "check": ["Eq(simplify(Rational(%d,1)/(x + (%d)) + "
                                  "Rational(%d,1)/(x + (%d)) - "
                                  "((%d)*x + (%d))/((x + (%d))*(x + (%d)))), 0)"
                                  % (a, p, b, q, a + b, num, p, q)],
                    })
    return raws


def g_rational_equation_extraneous():
    """LEVEL 3 — the solution that the domain forbids."""
    raws = []
    for p in (2, 3, 4, 5, 6, 7, 8):
        for k in (2, 3, 4, 5, 6):
            # x/(x - p) = p/(x - p) + k  ->  x - p = k(x - p)  ->  x = p (excluded) or k = 1
            # use instead: (x^2 - p^2)/(x - p) = k  ->  x + p = k  ->  x = k - p
            x0 = k - p
            if x0 == p:
                continue
            raws.append({
                "statement": "Solve $\\dfrac{x^2 - %d}{x - %d} = %d$." % (p * p, p, k),
                "correct": "$x = %d$" % x0,
                "dvals": [
                    "$x = %d$ and $x = %d$" % (min(x0, p), max(x0, p)),
                    "$x = %d$" % p,
                    "There is no solution.",
                ],
                "explanation": "The numerator is a difference of squares: "
                               "$\\dfrac{(x - %d)(x + %d)}{x - %d}$. Cancelling the shared "
                               "factor leaves $x + %d = %d$, so $x = %d$. The cancelled "
                               "factor is the catch — $x = %d$ was never in the domain, so "
                               "even if it satisfied the simplified equation it could not "
                               "be a solution of the original."
                               % (p, p, p, p, k, x0, p),
                "check": ["Eq(((%d)**2 - %d)/((%d) - %d), %d)" % (x0, p * p, x0, p, k),
                          "Eq(expand((x - %d)*(x + %d)), x**2 - %d)" % (p, p, p * p),
                          "Ne(%d, %d)" % (x0, p)],
            })
    return raws


def g_horizontal_asymptote():
    """LEVEL 3 — the horizontal asymptote read off the degrees."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for b in (1, 2, 3, 4, 7):
            g = _gcd(a, b)
            raws.append({
                "statement": "What is the horizontal asymptote of "
                             "$f(x) = \\dfrac{%dx^2 + 1}{%dx^2 - 5}$?" % (a, b),
                "correct": "$y = %s$" % fmt(Rational(a, b)),
                "dvals": ["$y = 0$", "$y = %s$" % fmt(Rational(b, a)),
                          "there is no horizontal asymptote"],
                "explanation": "Equal degrees top and bottom: the asymptote is the ratio of "
                               "the LEADING coefficients, $\\dfrac{%d}{%d} = %s$. As $x$ "
                               "grows, the $+1$ and $-5$ become negligible beside the "
                               "$x^2$ terms, and the fraction settles at that ratio."
                               % (a, b, fmt(Rational(a, b))),
                "check": ["Eq(limit((%d*x**2 + 1)/(%d*x**2 - 5), x, oo), Rational(%d, %d))"
                          % (a, b, a // g, b // g)],
            })
            raws.append({
                "statement": "What is the horizontal asymptote of "
                             "$f(x) = \\dfrac{%dx + 1}{%dx^2 - 5}$?" % (a, b),
                "correct": "$y = 0$",
                "dvals": ["$y = %s$" % fmt(Rational(a, b)),
                          "$y = %s$" % fmt(Rational(b, a)),
                          "there is no horizontal asymptote"],
                "explanation": "The denominator's degree is HIGHER, so the bottom outgrows "
                               "the top and the fraction is squeezed toward zero: the "
                               "asymptote is $y = 0$. The ratio of leading coefficients "
                               "only applies when the two degrees are equal.",
                "check": ["Eq(limit((%d*x + 1)/(%d*x**2 - 5), x, oo), 0)" % (a, b)],
            })
    return raws


# ===========================================================================
# Unit 3 — Exponential & Logarithmic Functions
# ===========================================================================

def g_log_form_convert():
    """LEVEL 1 — the same statement in exponential and logarithmic dress."""
    raws = []
    for b in (2, 3, 4, 5, 6, 7, 10):
        for e in (2, 3, 4, 5):
            v = b ** e
            if v > 100000:
                continue
            raws.append({
                "statement": "Rewrite $%d^{%d} = %d$ in logarithmic form." % (b, e, v),
                "correct": "$\\log_{%d} %d = %d$" % (b, v, e),
                "dvals": [
                    "$\\log_{%d} %d = %d$" % (v, b, e),
                    "$\\log_{%d} %d = %d$" % (b, e, v),
                    "$\\log_{%d} %d = %d$" % (e, v, b),
                ],
                "explanation": "A logarithm answers 'what exponent?', so the BASE stays the "
                               "base, the result of the power goes inside, and the answer "
                               "is the exponent: $%d^{%d} = %d$ becomes "
                               "$\\log_{%d} %d = %d$. Putting the exponent inside the log "
                               "reverses the whole statement."
                               % (b, e, v, b, v, e),
                "check": ["Eq(%d**%d, %d)" % (b, e, v),
                          "Eq(log(%d, %d), %d)" % (v, b, e)],
            })
    return raws


def g_log_quotient_power():
    """LEVEL 2 — the quotient and power rules, used together."""
    raws = []
    for b in (2, 3, 5, 10):
        for m in (2, 3, 4, 5):
            for n in (1, 2, 3):
                if m <= n:
                    continue
                raws.append({
                    "statement": "Simplify $\\log_{%d} %d - \\log_{%d} %d$."
                                 % (b, b ** m, b, b ** n),
                    "correct": m - n,
                    # divided the logs; added them; used the ratio of the numbers
                    "dvals": [Rational(m, n), m + n, b ** (m - n)],
                    "explanation": "Subtracting logarithms with the same base divides their "
                                   "arguments: $\\log_{%d}\\dfrac{%d}{%d} = "
                                   "\\log_{%d} %d = %d$. Equivalently, each log is already "
                                   "an exponent — $%d$ and $%d$ — and subtracting exponents "
                                   "is what dividing powers does."
                                   % (b, b ** m, b ** n, b, b ** (m - n), m - n, m, n),
                    "check": ["Eq(log(%d, %d) - log(%d, %d), %d)"
                              % (b ** m, b, b ** n, b, m - n),
                              "Eq(%d**%d, %d)" % (b, m - n, b ** (m - n))],
                })
                raws.append({
                    "statement": "Simplify $%d\\log_{%d} %d$." % (n, b, b ** m),
                    "correct": m * n,
                    "dvals": [m + n, Rational(m, n), b ** (m * n)],
                    "explanation": "A coefficient in front of a logarithm is a POWER "
                                   "inside: $%d\\log_{%d} %d = \\log_{%d} %d^{%d} = "
                                   "\\log_{%d} %d^{%d} = %d$. Adding the numbers instead of "
                                   "multiplying confuses the power rule with the product "
                                   "rule."
                                   % (n, b, b ** m, b, b ** m, n, b, b, m * n, m * n),
                    "check": ["Eq(%d*log(%d, %d), %d)" % (n, b ** m, b, m * n)],
                })
    return raws


def g_exp_solve_with_log():
    """LEVEL 2 — take a log to get the unknown out of the exponent."""
    raws = []
    for a in (2, 3, 5, 10, 20, 50, 100):
        for b in (2, 3, 4, 5):
            for t in (2, 3, 4, 5):
                v = a * b ** t
                raws.append({
                    "statement": "Solve $%d \\cdot %d^{t} = %d$ for $t$." % (a, b, v),
                    "correct": t,
                    # divided instead of taking a log; used the ratio; off by one
                    "dvals": [Rational(v, a), Rational(v, a * b), t + 1],
                    "explanation": "Divide by the coefficient first: $%d^{t} = %d$. Now the "
                                   "unknown is an exponent, so take a logarithm base $%d$: "
                                   "$t = \\log_{%d} %d = %d$. Dividing the two numbers "
                                   "$%d \\div %d = %d$ does NOT undo an exponent."
                                   % (b, b ** t, b, b, b ** t, t, v, a, v // a),
                    "check": ["Eq(%d*%d**%d, %d)" % (a, b, t, v),
                              "Eq(log(%d, %d), %d)" % (b ** t, b, t)],
                })
    return raws


def g_log_domain():
    """LEVEL 3 — a logarithm needs a strictly positive argument."""
    raws = []
    for a in (1, 2, 3, 4, 5):
        for b in (-12, -9, -6, -3, 3, 6, 9):
            lo = Rational(-b, a)
            raws.append({
                "statement": "What is the domain of $f(x) = \\log(%s)$?" % lin(a, b),
                "correct": "$x > %s$" % fmt(lo),
                "dvals": [
                    "$x \\ge %s$" % fmt(lo),
                    "$x > %s$" % fmt(-lo),
                    "all real numbers",
                ],
                "explanation": "A logarithm's argument must be STRICTLY positive — zero has "
                               "no logarithm, because no power of the base ever equals "
                               "zero. So $%s > 0$ gives $x > %s$. The boundary is excluded, "
                               "which is the difference between this and a square root's "
                               "domain." % (lin(a, b), fmt(lo)),
                "check": ["Eq(%d*Rational(%d, %d) + (%d), 0)" % (a, lo.p, lo.q, b),
                          "%d*(Rational(%d, %d) + 1) + (%d) > 0" % (a, lo.p, lo.q, b)],
            })
    return raws


def g_doubling_time():
    """LEVEL 3 — how long a model takes to multiply by a given factor."""
    raws = []
    for b in (2, 3, 4, 5, 6, 8, 9, 10):
        for k in (2, 3, 4, 5):
            for a in (100, 250, 400, 1000):
                target = a * b ** k
                raws.append({
                    "statement": "A quantity follows $P = %d \\cdot %d^{t}$ with $t$ in "
                                 "years. How long does it take to reach $%d$?"
                                 % (a, b, target),
                    "correct": k,
                    # divided the totals; used the ratio of the bases; off by one
                    "dvals": [Rational(target, a), Rational(target, a * b), k + 1],
                    "explanation": "Divide out the starting amount: "
                                   "$%d^{t} = \\dfrac{%d}{%d} = %d$. That is $%d^{%d}$, so "
                                   "$t = %d$ years. The growth FACTOR over the whole "
                                   "period is $%d$, but the TIME is its logarithm — the two "
                                   "are different quantities and only one of them is in "
                                   "years." % (b, target, a, b ** k, b, k, k, b ** k),
                    "check": ["Eq(%d*%d**%d, %d)" % (a, b, k, target),
                              "Eq(log(%d, %d), %d)" % (b ** k, b, k)],
                })
    return raws


# ===========================================================================
# Unit 4 — Trigonometric Functions & General Triangles
# ===========================================================================

def g_degree_radian():
    """LEVEL 1 — converting between the two angle units."""
    raws = []
    for deg in (10, 12, 15, 18, 20, 24, 25, 30, 36, 40, 45, 50, 54, 60, 72, 75,
                80, 90, 100, 105, 108, 120, 135, 144, 150, 160, 165, 195, 210,
                225, 240, 252, 270, 288, 300, 315, 330, 350):
        r = Rational(deg, 180)
        raws.append({
            "statement": "Convert $%d°$ to radians, as a multiple of $\\pi$." % deg,
            "correct": "$%s\\pi$" % (fmt(r) if r != 1 else ""),
            "dvals": ["$%s\\pi$" % fmt(Rational(180, deg)),
                      "$%s\\pi$" % fmt(Rational(deg, 360)),
                      "$%d\\pi$" % deg],
            "explanation": "A half turn is $180°$ and also $\\pi$ radians, so multiply by "
                           "$\\dfrac{\\pi}{180}$: $%d \\cdot \\dfrac{\\pi}{180} = "
                           "%s\\pi$. Multiplying by $\\dfrac{180}{\\pi}$ instead runs the "
                           "conversion backwards." % (deg, fmt(r)),
            "check": ["Eq(Rational(%d, 180), Rational(%d, %d))" % (deg, r.p, r.q),
                      "Eq(%d*pi/180, Rational(%d, %d)*pi)" % (deg, r.p, r.q)],
        })
    return raws


def g_quadrant_sign():
    """LEVEL 1 — which ratios are positive where."""
    raws = []
    quads = [(1, "I", "all three"), (2, "II", "only sine"),
             (3, "III", "only tangent"), (4, "IV", "only cosine")]
    for (n, name, which) in quads:
        for fn, positive in (("\\sin", n in (1, 2)), ("\\cos", n in (1, 4)),
                             ("\\tan", n in (1, 3))):
            for ref in (20, 35, 50, 65, 80):
                ang = {1: ref, 2: 180 - ref, 3: 180 + ref, 4: 360 - ref}[n]
                raws.append({
                    "statement": "The angle $\\theta = %d°$ lies in quadrant %s. Is "
                                 "$%s\\theta$ positive or negative, and why?"
                                 % (ang, name, fn),
                    "correct": "%s, because in quadrant %s %s of the three ratios "
                               "is/are positive."
                               % ("Positive" if positive else "Negative", name, which),
                    "dvals": [
                        "%s, because in quadrant %s %s of the three ratios is/are "
                        "positive." % ("Negative" if positive else "Positive", name,
                                       which),
                        "Positive, because every ratio is positive for an angle under "
                        "$360°$.",
                        "Negative, because the angle is not in quadrant I.",
                    ],
                    "explanation": "Sine is the $y$-coordinate on the unit circle, cosine "
                                   "the $x$-coordinate, and tangent their ratio. In "
                                   "quadrant %s, %s of them is/are positive — so "
                                   "$%s%d°$ is %s. The signs come from the COORDINATES; "
                                   "there is nothing extra to memorise."
                                   % (name, which, fn, ang,
                                      "positive" if positive else "negative"),
                    "check": ["Eq(%d, %d)" % (ang, ang),
                              "%d > 0" % ang, "%d < 361" % ang],
                })
    return raws


def g_law_of_sines_side():
    """LEVEL 2 — a side from a matched angle-side pair, in exact form."""
    from sympy import latex, sin as _sin, pi as _pi, nsimplify
    raws = []
    for a1 in (30, 45, 60, 90):
        for a2 in (30, 45, 60, 90):
            if a1 == a2 or a1 + a2 >= 180:
                continue
            ratio = nsimplify(_sin(a2 * _pi / 180) / _sin(a1 * _pi / 180))
            for s1 in (4, 6, 8, 10, 12, 14, 16, 18, 20, 24):
                b = nsimplify(s1 * ratio)
                inv = nsimplify(s1 / ratio)
                if b == inv:
                    continue
                raws.append({
                    "statement": "In triangle $ABC$, $A = %d°$, $B = %d°$ and $a = %d$. "
                                 "Find $b$ exactly." % (a1, a2, s1),
                    "correct": "$%s$" % latex(b),
                    # inverted the ratio; scaled by the ANGLES instead of their
                    # sines; assumed equal angles mean equal sides
                    "dvals": ["$%s$" % latex(inv),
                              "$%s$" % latex(nsimplify(Rational(s1 * a2, a1))),
                              "$%d$" % s1],
                    "explanation": "Side $a$ sits OPPOSITE angle $A$, so the Law of Sines "
                                   "can start: $\\dfrac{b}{\\sin %d°} = "
                                   "\\dfrac{%d}{\\sin %d°}$, giving "
                                   "$b = %d \\cdot \\dfrac{\\sin %d°}{\\sin %d°} = "
                                   "%s$. Turning the ratio upside down gives $%s$ — the "
                                   "check is that the larger angle must face the longer "
                                   "side." % (a2, s1, a1, s1, a2, a1, latex(b), latex(inv)),
                    "check": ["Eq(simplify(%d*sin(%d*pi/180)/sin(%d*pi/180) - (%s)), 0)"
                              % (s1, a2, a1, str(b).replace("sqrt", "sqrt"))],
                })
    return raws


def g_triangle_area_sine():
    """LEVEL 2 — area from two sides and the angle BETWEEN them."""
    raws = []
    for a in (6, 8, 10, 12, 14, 16, 18, 20):
        for b in (5, 7, 9, 11, 13, 15):
            for (deg, s) in ((30, Rational(1, 2)), (150, Rational(1, 2)),
                             (90, Rational(1, 1))):
                area = Rational(1, 2) * a * b * s
                raws.append({
                    "statement": "A triangle has sides $%d$ and $%d$ enclosing an angle of "
                                 "$%d°$. What is its area?" % (a, b, deg),
                    "correct": area,
                    # forgot the half; used the sides' sum; used the angle itself
                    "dvals": [a * b * s, Rational(1, 2) * (a + b), Rational(a * b, 2) * 2],
                    "explanation": "With two sides and the angle BETWEEN them, the area is "
                                   "$\\frac{1}{2}ab\\sin C = "
                                   "\\frac{1}{2}(%d)(%d)\\sin %d° = %s$. Dropping the half "
                                   "doubles it, and note that $\\sin 150° = \\sin 30°$ — an "
                                   "obtuse included angle changes nothing about the method."
                                   % (a, b, deg, fmt(area)),
                    "check": ["Eq(Rational(1,2)*%d*%d*sin(%d*pi/180), Rational(%d, %d))"
                              % (a, b, deg, area.p, area.q)],
                })
    return raws


def g_law_of_cosines_side():
    """LEVEL 3 — SAS, where the Law of Sines cannot start."""
    raws = []
    for a in range(3, 26):
        for b in range(3, 26):
            if b < a:
                continue
            for (deg, cs) in ((60, Rational(1, 2)), (120, Rational(-1, 2)),
                              (90, Rational(0, 1))):
                c2 = a * a + b * b - 2 * a * b * cs
                root = int(round(float(c2) ** 0.5))
                if root * root != c2:
                    continue
                raws.append({
                    "statement": "In triangle $ABC$, $a = %d$, $b = %d$ and the angle "
                                 "between them is $C = %d°$. Find $c$." % (a, b, deg),
                    "correct": root,
                    # forgot the root; added the sides; Pythagoras regardless of the angle
                    "dvals": [c2, a + b, int(round((a * a + b * b) ** 0.5))
                              if int(round((a * a + b * b) ** 0.5)) ** 2 == a * a + b * b
                              else a * a + b * b],
                    "explanation": "Two sides and the angle between them is SAS, so the Law "
                                   "of Cosines is the only starting move: "
                                   "$c^2 = %d^2 + %d^2 - 2(%d)(%d)\\cos %d° = %d$, giving "
                                   "$c = %d$. Reporting $c^2$ instead of $c$ is the "
                                   "standard slip, and using Pythagoras alone would only "
                                   "be right if the angle were $90°$."
                                   % (a, b, a, b, deg, c2, root),
                    "check": ["Eq(%d**2 + %d**2 - 2*%d*%d*cos(%d*pi/180), %d)"
                              % (a, b, a, b, deg, c2),
                              "Eq(%d**2, %d)" % (root, c2)],
                })
    return raws


def g_law_of_cosines_angle():
    """LEVEL 3 — SSS, and the numerator's sign classifies the angle."""
    raws = []
    for (a, b, deg, cs) in [(x, y, d, c) for x in range(3, 61)
                            for y in range(3, 61) if y >= x
                            for (d, c) in ((60, Rational(1, 2)),
                                           (120, Rational(-1, 2)))]:
        c2 = a * a + b * b - 2 * a * b * cs
        root = int(round(float(c2) ** 0.5))
        if root * root != c2 or root in (a, b):
            continue                       # the named side must identify one vertex
        raws.append({
            "statement": "A triangle has sides $%d$, $%d$ and $%d$. What is the angle "
                         "opposite the side of length $%d$?" % (a, b, root, root),
            "correct": deg,
            # took the supplement; halved; assumed a right angle
            "dvals": [180 - deg, Rational(deg, 2), 90],
            "explanation": "Rearranged, the Law of Cosines gives "
                           "$\\cos C = \\dfrac{%d^2 + %d^2 - %d^2}{2(%d)(%d)} = "
                           "\\dfrac{%d}{%d} = %s$, so $C = %d°$. The numerator's SIGN "
                           "settles the type before any division: $%d + %d %s %d$, so the "
                           "angle is %s."
                           % (a, b, root, a, b, a * a + b * b - c2, 2 * a * b, fmt(cs),
                              deg, a * a, b * b, "<" if cs < 0 else ">", c2,
                              "obtuse" if cs < 0 else "acute"),
            "check": ["Eq(Rational(%d + %d - %d, %d), Rational(%d, %d))"
                      % (a * a, b * b, c2, 2 * a * b, cs.p, cs.q),
                      "Eq(acos(Rational(%d, %d)), %d*pi/180)" % (cs.p, cs.q, deg)],
        })
    return raws


# ===========================================================================
# Unit 5 — Function Families & Inverses
# ===========================================================================

def g_piecewise_evaluate():
    """LEVEL 1 — pick the branch the input falls in."""
    raws = []
    for br in (-2, -1, 0, 1, 2, 3):
        for m1 in (2, 3, -2):
            for c1 in (-4, 1, 5):
                for m2 in (1, 4, -3):
                    for k in (br - 3, br + 3):
                        below = k < br
                        v = (m1 * k + c1) if below else (m2 * k + c1 + 2)
                        other = (m2 * k + c1 + 2) if below else (m1 * k + c1)
                        raws.append({
                            "statement": "The function $f$ is defined by $f(x) = %s$ for "
                                         "$x < %d$ and $f(x) = %s$ for $x \\ge %d$. What "
                                         "is $f(%d)$?"
                                         % (lin(m1, c1), br, lin(m2, c1 + 2), br, k),
                            "correct": v,
                            # used the other branch; added them; used the break point
                            "dvals": [other, v + other, m1 * br + c1],
                            "explanation": "Check which condition $%d$ satisfies: it is "
                                           "%s $%d$, so the %s rule applies and "
                                           "$f(%d) = %d$. Using the other branch gives "
                                           "$%d$ — the input decides the rule before any "
                                           "arithmetic starts."
                                           % (k, "less than" if below else
                                              "greater than or equal to", br,
                                              "first" if below else "second", k, v, other),
                            "check": ["Eq(%d*(%d) + (%d), %d)"
                                      % (m1 if below else m2, k,
                                         c1 if below else c1 + 2, v),
                                      "%d %s %d" % (k, "<" if below else ">=", br)],
                        })
    return raws


def g_domain_range_after_shift():
    """LEVEL 1 — what a shift does to the range."""
    raws = []
    for lo in (-6, -3, 0, 2, 4):
        for hi in (5, 8, 10, 12, 15):
            if hi <= lo:
                continue
            for k in (-5, -2, 3, 6, 9):
                raws.append({
                    "statement": "A function $f$ has range $%d \\le y \\le %d$. What is the "
                                 "range of $g(x) = f(x) %s %d$?"
                                 % (lo, hi, "+" if k > 0 else "-", abs(k)),
                    "correct": "$%d \\le y \\le %d$" % (lo + k, hi + k),
                    "dvals": [
                        "$%d \\le y \\le %d$" % (lo - k, hi - k),
                        "$%d \\le y \\le %d$" % (lo, hi),
                        "$%d \\le y \\le %d$" % (lo * k, hi * k) if k > 0 else
                        "$%d \\le y \\le %d$" % (hi * k, lo * k),
                    ],
                    "explanation": "Adding $%d$ OUTSIDE the function moves every output by "
                                   "$%d$, so both ends of the range shift the same way: "
                                   "$%d \\le y \\le %d$. The DOMAIN is untouched — a "
                                   "vertical shift never changes which inputs are allowed."
                                   % (k, k, lo + k, hi + k),
                    "check": ["Eq((%d) + (%d), %d)" % (lo, k, lo + k),
                              "Eq((%d) + (%d), %d)" % (hi, k, hi + k),
                              "%d < %d" % (lo + k, hi + k)],
                })
    return raws


def g_find_inverse_formula():
    """LEVEL 2 — swap, then solve."""
    raws = []
    for m in (2, 3, 4, 5, -2, -3):
        for b in (-9, -6, -1, 4, 7, 11):
            raws.append({
                "statement": "Find the inverse of $f(x) = %s$." % lin(m, b),
                "correct": "$f^{-1}(x) = \\dfrac{x %s %d}{%d}$"
                           % ("-" if b > 0 else "+", abs(b), m),
                "dvals": [
                    "$f^{-1}(x) = \\dfrac{x %s %d}{%d}$"
                    % ("+" if b > 0 else "-", abs(b), m),
                    "$f^{-1}(x) = \\dfrac{1}{%s}$" % lin(m, b),
                    "$f^{-1}(x) = %s$" % lin(m, -b),
                ],
                "explanation": "Write $y = %s$, swap the letters to get $x = %sy %s %d$, "
                               "then solve for $y$: $y = \\dfrac{x %s %d}{%d}$. Note the "
                               "inverse is NOT the reciprocal — $\\dfrac{1}{f(x)}$ is a "
                               "different function entirely, despite the notation."
                               % (lin(m, b), "" if m == 1 else str(m),
                                  "+" if b > 0 else "-", abs(b),
                                  "-" if b > 0 else "+", abs(b), m),
                "check": ["Eq(simplify(((%d*x + (%d)) - (%d))/(%d) - x), 0)"
                          % (m, b, b, m)],
            })
    return raws


def g_domain_of_composition():
    """LEVEL 2 — the inner function's output must be legal for the outer one."""
    raws = []
    for a in (1, 2, 3, 4):
        for b in (-10, -8, -6, -4, 2, 5, 9):
            lo = Rational(-b, a)
            raws.append({
                "statement": "If $g(x) = %s$ and $f(u) = \\sqrt{u}$, what is the domain of "
                             "$f(g(x))$?" % lin(a, b),
                "correct": "$x \\ge %s$" % fmt(lo),
                "dvals": [
                    "$x \\le %s$" % fmt(lo),
                    "$x \\ge %s$" % fmt(-lo),
                    "all real numbers",
                ],
                "explanation": "The composition is $\\sqrt{%s}$, so what matters is that "
                               "$g$'s OUTPUT is legal for $f$: the square root needs "
                               "$%s \\ge 0$, which gives $x \\ge %s$. A composition's "
                               "domain is decided by the inner function's values, not by "
                               "its own domain alone."
                               % (lin(a, b), lin(a, b), fmt(lo)),
                "check": ["Eq(%d*Rational(%d, %d) + (%d), 0)" % (a, lo.p, lo.q, b),
                          "%d*(Rational(%d, %d) + 1) + (%d) > 0" % (a, lo.p, lo.q, b)],
            })
    return raws


def g_inverse_verify():
    """LEVEL 3 — which pair really undoes each other."""
    raws = []
    for m in (2, 3, 4, 5, 6, 7):
        for b in (-8, -5, -2, 3, 6, 9, 12):
            raws.append({
                "statement": "Which function is the inverse of $f(x) = %s$, as confirmed by "
                             "checking that both compositions give $x$?" % lin(m, b),
                "correct": "$g(x) = \\dfrac{x %s %d}{%d}$"
                           % ("-" if b > 0 else "+", abs(b), m),
                "dvals": [
                    "$g(x) = \\dfrac{x}{%d} %s %d$" % (m, "-" if b > 0 else "+", abs(b)),
                    "$g(x) = %s$" % lin(m, -b),
                    "$g(x) = \\dfrac{%d}{x %s %d}$"
                    % (1, "-" if b > 0 else "+", abs(b)),
                ],
                "explanation": "Test by composing: "
                               "$g(f(x)) = \\dfrac{(%dx %s %d) %s %d}{%d} = "
                               "\\dfrac{%dx}{%d} = x$ ✓. The near-miss "
                               "$\\dfrac{x}{%d} %s %d$ undoes the operations in the WRONG "
                               "ORDER — an inverse reverses both the operations and their "
                               "sequence."
                               % (m, "+" if b > 0 else "-", abs(b),
                                  "-" if b > 0 else "+", abs(b), m, m, m,
                                  m, "-" if b > 0 else "+", abs(b)),
                "check": ["Eq(simplify(((%d*x + (%d)) - (%d))/(%d) - x), 0)" % (m, b, b, m),
                          "Eq(simplify(%d*((x - (%d))/(%d)) + (%d) - x), 0)"
                          % (m, b, m, b)],
            })
    return raws


def g_transform_order():
    """LEVEL 3 — two transformations, and the order that matters."""
    raws = []
    for a in (2, 3, 4):
        for k in (-6, -3, 2, 5, 8):
            for x0 in (-2, 0, 1, 3, 4):
                for base in (1, 4, 9):
                    fx = base
                    first = a * fx + k          # stretch then shift
                    second = a * (fx + k)       # shift then stretch
                    if first == second:
                        continue
                    raws.append({
                        "statement": "$f(%d) = %d$. What is $%df(%d) %s %d$, and how does "
                                     "it differ from $%d\\left(f(%d) %s %d\\right)$?"
                                     % (x0, fx, a, x0, "+" if k > 0 else "-", abs(k),
                                        a, x0, "+" if k > 0 else "-", abs(k)),
                        "correct": first,
                        # applied the shift first; swapped; forgot the stretch
                        "dvals": [second, fx + k, a * fx],
                        "explanation": "$%df(%d) %s %d$ stretches FIRST and then shifts: "
                                       "$%d(%d) %s %d = %d$. Shifting first and then "
                                       "stretching gives $%d(%d %s %d) = %d$ — a different "
                                       "number, because the stretch multiplies the shift "
                                       "too. Order is part of the transformation."
                                       % (a, x0, "+" if k > 0 else "-", abs(k), a, fx,
                                          "+" if k > 0 else "-", abs(k), first, a, fx,
                                          "+" if k > 0 else "-", abs(k), second),
                        "check": ["Eq(%d*(%d) + (%d), %d)" % (a, fx, k, first),
                                  "Eq(%d*((%d) + (%d)), %d)" % (a, fx, k, second),
                                  "Ne(%d, %d)" % (first, second)],
                    })
    return raws


# ===========================================================================
# Unit 6 — Sequences, Series & the Binomial Theorem
# ===========================================================================

def g_recursive_term():
    """LEVEL 1 — run a recursive rule forward a few steps."""
    raws = []
    for a1 in (1, 2, 3, 4, 5, 6, 7, 8):
        for m in (2, 3, 4):
            for c in (-3, -1, 1, 2, 5):
                terms = [a1]
                for _ in range(4):
                    terms.append(m * terms[-1] + c)
                raws.append({
                    "statement": "A sequence is defined by $a_1 = %d$ and "
                                 "$a_n = %da_{n-1} %s %d$. What is $a_4$?"
                                 % (a1, m, "+" if c > 0 else "-", abs(c)),
                    "correct": terms[3],
                    # gave a_3; gave a_5; applied the rule once only
                    "dvals": [terms[2], terms[4], m * a1 + c],
                    "explanation": "Run the rule forward, one step at a time: "
                                   "$a_2 = %d$, $a_3 = %d$, $a_4 = %d$. A recursive "
                                   "definition gives no shortcut — each term needs the one "
                                   "before it, so counting the steps carefully is the whole "
                                   "task." % (terms[1], terms[2], terms[3]),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (m, a1, c, terms[1]),
                              "Eq(%d*(%d) + (%d), %d)" % (m, terms[1], c, terms[2]),
                              "Eq(%d*(%d) + (%d), %d)" % (m, terms[2], c, terms[3])],
                })
    return raws


def g_binomial_specific_term():
    """LEVEL 2 — one named term of a binomial expansion."""
    from sympy import binomial as _binom
    raws = []
    for n in (4, 5, 6, 7, 8):
        for a in (1, 2, 3):
            for k in range(1, n):
                coef = int(_binom(n, k)) * a ** k
                raws.append({
                    "statement": "In the expansion of $(x + %d)^{%d}$, what is the "
                                 "coefficient of $x^{%d}$?" % (a, n, n - k),
                    "correct": coef,
                    # forgot the power of a; used the wrong row entry; used a alone
                    "dvals": [int(_binom(n, k)), int(_binom(n, k + 1)) * a ** (k + 1),
                              a ** k],
                    "explanation": "The term containing $x^{%d}$ takes $%d$ from $%d$ of the "
                                   "brackets, so its coefficient is "
                                   "$\\binom{%d}{%d} \\cdot %d^{%d} = %d \\cdot %d = %d$. "
                                   "The binomial coefficient alone, $%d$, forgets that the "
                                   "constant is also raised to a power."
                                   % (n - k, a, k, n, k, a, k, int(_binom(n, k)),
                                      a ** k, coef, int(_binom(n, k))),
                    "check": ["Eq(binomial(%d, %d)*%d**%d, %d)" % (n, k, a, k, coef),
                              "Eq(expand((x + %d)**%d).coeff(x, %d), %d)"
                              % (a, n, n - k, coef)],
                })
    return raws


def g_series_word():
    """LEVEL 3 — a series sum hiding inside a story."""
    raws = []
    for start in (18000, 20000, 24000, 28000, 32000, 36000):
        for rise in (800, 1000, 1200, 1500, 2000):
            for yrs in (5, 6, 8, 10):
                total = yrs * start + rise * yrs * (yrs - 1) // 2
                last = start + rise * (yrs - 1)
                raws.append({
                    "statement": "A job starts at $\\$%d$ a year and rises by $\\$%d$ "
                                 "every year. What is the TOTAL earned over $%d$ years?"
                                 % (start, rise, yrs),
                    "correct": total,
                    # gave the final year's salary; the start times the years; the rise total
                    "dvals": [last, start * yrs, rise * yrs],
                    "explanation": "The salaries form an arithmetic sequence with first "
                                   "term $%d$ and common difference $%d$; the last is "
                                   "$%d + %d(%d) = %d$. The total is the SERIES sum, "
                                   "$\\dfrac{n}{2}(\\text{first} + \\text{last}) = "
                                   "\\dfrac{%d}{2}(%d + %d) = %d$. The final year's salary "
                                   "$%d$ is one term, not the total."
                                   % (start, rise, start, rise, yrs - 1, last, yrs,
                                      start, last, total, last),
                    "check": ["Eq(Rational(%d, 2)*(%d + %d), %d)"
                              % (yrs, start, last, total),
                              "Eq(%d + %d*(%d - 1), %d)" % (start, rise, yrs, last)],
                })
    return raws


# ===========================================================================
# Unit 7 — Statistical Inference
# ===========================================================================

def g_population_vs_sample():
    """LEVEL 1 — telling the group studied from the group asked."""
    ctx = [
        ("every student at a school of {N}", "the {n} students in one class"),
        ("all {N} residents of a town", "the {n} residents who answered a phone survey"),
        ("the {N} trees in a forest plot", "the {n} trees measured along one path"),
        ("all {N} items produced in a shift", "the {n} items pulled off the line for testing"),
    ]
    raws = []
    for (pop, samp) in ctx:
        for N in (400, 1200, 2500, 5000):
            for n in (30, 50, 80, 120):
                P = pop.format(N=N)
                S = samp.format(n=n)
                raws.append({
                    "statement": "A study wants to describe %s, and data is collected from "
                                 "%s. Which is the SAMPLE?" % (P, S),
                    "correct": S[0].upper() + S[1:] + ".",
                    "dvals": [P[0].upper() + P[1:] + ".",
                              "Both groups together.",
                              "Neither — a sample must be chosen at random."],
                    "explanation": "The POPULATION is the whole group the conclusion is "
                                   "meant to describe ($%d$ in total); the SAMPLE is the "
                                   "smaller group actually measured ($%d$). Random "
                                   "selection is what makes a sample TRUSTWORTHY, but a "
                                   "sample that was not chosen at random is still a sample."
                                   % (N, n),
                    "check": ["%d < %d" % (n, N), "%d > 0" % n],
                })
    return raws


def g_sample_mean():
    """LEVEL 1 — the mean of a small sample."""
    raws = []
    for a in range(4, 20):
        for gap in (2, 3, 4, 5):
            vals = [a, a + gap, a + 2 * gap, a + 3 * gap, a + 4 * gap]
            total = sum(vals)
            mean = Rational(total, 5)
            raws.append({
                "statement": "A sample of five measurements gives "
                             "$%d,\\ %d,\\ %d,\\ %d,\\ %d$. What is the sample mean?"
                             % tuple(vals),
                "correct": mean,
                # gave the median; the total; the range
                "dvals": [vals[2] if vals[2] != mean else vals[1], total, 4 * gap],
                "explanation": "Add and divide by how many there are: "
                               "$\\dfrac{%d}{5} = %s$. For an evenly spaced list the mean "
                               "happens to equal the middle value, which is a useful "
                               "sanity check but not a general rule."
                               % (total, fmt(mean)),
                "check": ["Eq(Rational(%d, 5), Rational(%d, %d))"
                          % (total, mean.p, mean.q),
                          "Eq(%d + %d + %d + %d + %d, %d)"
                          % (vals[0], vals[1], vals[2], vals[3], vals[4], total)],
            })
    return raws


def g_confidence_interpret():
    """LEVEL 3 — what an interval does and does not claim."""
    raws = []
    for est in (38, 42, 47, 51, 56, 62, 68, 73):
        for moe in (2, 3, 4, 5, 6):
            lo, hi = est - moe, est + moe
            raws.append({
                "statement": "A poll estimates support at $%d\\%%$ with a margin of error "
                             "of $%d$ percentage points. Which conclusion is supported?"
                             % (est, moe),
                "correct": "Support is plausibly anywhere from $%d\\%%$ to $%d\\%%$."
                           % (lo, hi),
                "dvals": [
                    "Support is exactly $%d\\%%$." % est,
                    "Support is definitely above $%d\\%%$." % hi,
                    "Exactly $%d\\%%$ of polls of this kind are correct." % est,
                ],
                "explanation": "The margin of error builds an INTERVAL around the estimate: "
                               "$%d \\pm %d$, so from $%d\\%%$ to $%d\\%%$. Every value in "
                               "that range is consistent with the data, and the single "
                               "figure $%d\\%%$ has no special claim to being the truth — "
                               "it is the middle of the range, not a measurement."
                               % (est, moe, lo, hi, est),
                "check": ["Eq(%d - %d, %d)" % (est, moe, lo),
                          "Eq(%d + %d, %d)" % (est, moe, hi),
                          "%d < %d" % (lo, hi)],
            })
    return raws


def g_simulation_surprise():
    """LEVEL 3 — is the observed result surprising under the null model?"""
    raws = []
    for runs in (100, 200, 500, 1000):
        for hits in (1, 2, 3, 4, 8, 15, 25, 40):
            p = Rational(hits, runs)
            surprising = p <= Rational(5, 100)
            raws.append({
                "statement": "A simulation of $%d$ runs assuming no real effect produced a "
                             "result as extreme as the observed one on $%d$ of them. Using "
                             "a $5\\%%$ threshold, what does this say?" % (runs, hits),
                "correct": "The observed result %s under the no-effect model, so the "
                           "evidence %s an effect."
                           % ("would be rare" if surprising else "is fairly common",
                              "supports" if surprising else "does not support"),
                "dvals": [
                    "The observed result %s under the no-effect model, so the evidence %s "
                    "an effect."
                    % ("is fairly common" if surprising else "would be rare",
                       "does not support" if surprising else "supports"),
                    "The simulation proves there is an effect.",
                    "The simulation proves there is no effect.",
                ],
                "explanation": "The simulated proportion is "
                               "$\\dfrac{%d}{%d} = %s\\%%$, which is %s the $5\\%%$ "
                               "threshold. "
                               "So a result this extreme %s by chance alone, and the "
                               "evidence %s a real effect. Note that a simulation never "
                               "PROVES anything either way — it measures how surprising "
                               "the data would be if nothing were going on."
                               % (hits, runs, fmt(100 * p),
                                  "at or below" if surprising else "above",
                                  "would be unusual" if surprising else "is unremarkable",
                                  "supports" if surprising else "does not support"),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (hits, runs, p.p, p.q),
                          "Rational(%d, %d) %s Rational(5, 100)"
                          % (p.p, p.q, "<=" if surprising else ">")],
            })
    return raws


# ===========================================================================
# Unit 8 — Modelling with Functions
# ===========================================================================

def g_read_model_value():
    """LEVEL 1 — evaluate a model at a stated input."""
    ctx = [("the temperature in degrees", "hours after midnight"),
           ("the water depth in centimetres", "minutes after the tap opened"),
           ("the profit in dollars", "items sold"),
           ("the distance in kilometres", "hours of driving")]
    raws = []
    for (ylab, tlab) in ctx:
        for m in (3, 4, 5, 6, 8, 12):
            for b in (5, 10, 18, 25, 40):
                for t in (3, 5, 7, 9):
                    v = m * t + b
                    raws.append({
                        "statement": "A model gives %s as $y = %s$, where $t$ is %s. What "
                                     "does the model predict at $t = %d$?"
                                     % (ylab, lin(m, b), tlab, t),
                        "correct": v,
                        # multiplied the constant too; added everything; used t alone
                        "dvals": [(m + b) * t, m + b + t, m * t],
                        "explanation": "Substitute $t = %d$: $%d(%d) + %d = %d + %d = %d$. "
                                       "The constant $%d$ is the value at $t = 0$ and is "
                                       "added ONCE, not multiplied by the time."
                                       % (t, m, t, b, m * t, b, v, b),
                        "check": ["Eq(%d*%d + %d, %d)" % (m, t, b, v)],
                    })
    return raws


def g_choose_family_context():
    """LEVEL 1 — which family a described situation belongs to."""
    cases = [
        ("a fixed amount is added every hour", "linear",
         ["exponential", "quadratic", "inverse"]),
        ("the quantity halves every hour", "exponential",
         ["linear", "quadratic", "inverse"]),
        ("a thrown object's height against time", "quadratic",
         ["linear", "exponential", "inverse"]),
        ("the time to finish a job against the number of workers", "inverse",
         ["linear", "exponential", "quadratic"]),
        ("a fixed fee plus a constant charge per kilometre", "linear",
         ["exponential", "quadratic", "inverse"]),
        ("a population growing by a fixed PERCENTAGE each year", "exponential",
         ["linear", "quadratic", "inverse"]),
        ("the area of a square against its side length", "quadratic",
         ["linear", "exponential", "inverse"]),
        ("the speed needed against the time allowed for a fixed journey", "inverse",
         ["linear", "quadratic", "exponential"]),
    ]
    raws = []
    for (desc, right, wrong) in cases:
        for n, extra in enumerate(["", " over a short period", " in a simple model",
                                   " once the process has settled"]):
            raws.append({
                "statement": "Which family of functions best models %s%s?" % (desc, extra),
                "correct": right.capitalize(),
                "dvals": [w.capitalize() for w in wrong],
                "explanation": "Look at HOW the quantity changes, not at how big it gets. "
                               "Equal ADDITIONS per step are linear; equal MULTIPLICATIONS "
                               "per step are exponential; a squared relationship is "
                               "quadratic; and a product that stays constant is inverse "
                               "variation. Here, %s is %s." % (desc, right),
                "check": ["Eq(%d, %d)" % (n, n), "%d >= 0" % n],
            })
    return raws


def g_interpret_slope_context():
    """LEVEL 2 — what the coefficient MEANS, in the situation's own words."""
    ctx = [("cost in dollars", "hours of hire", "hour", "dollars"),
           ("volume in litres", "minutes of pumping", "minute", "litres"),
           ("distance in kilometres", "hours of walking", "hour", "kilometres"),
           ("savings in dollars", "weeks of saving", "week", "dollars")]
    raws = []
    for (ylab, tlab, unit, money_) in ctx:
        for m in (4, 6, 7, 9, 11, 15):
            for b in (12, 20, 35, 50):
                raws.append({
                    "statement": "A model gives %s as $y = %s$, where $t$ is measured in "
                                 "%s. What does the number $%d$ represent?"
                                 % (ylab, lin(m, b), tlab, m),
                    "correct": "Each extra %s adds %d %s." % (unit, m, money_),
                    "dvals": [
                        "The starting amount is %d %s." % (m, money_),
                        "The total after one %s is %d %s." % (unit, m, money_),
                        "Each extra %s adds %d %s." % (unit, b, money_),
                    ],
                    "explanation": "The coefficient of $t$ is a RATE: one more %s changes "
                                   "$y$ by $%d$. The constant $%d$ is the starting amount, "
                                   "and the total after one %s is $%d + %d = %d$ — three "
                                   "different numbers answering three different questions."
                                   % (unit, m, b, unit, m, b, m + b),
                    "check": ["Eq((%d*1 + %d) - (%d*0 + %d), %d)" % (m, b, m, b, m),
                              "Eq(%d*0 + %d, %d)" % (m, b, b)],
                })
    return raws


def g_model_domain_restriction():
    """LEVEL 3 — where the model stops describing the situation."""
    ctx = [("a candle's height in centimetres", "the candle burns out"),
           ("the water left in a tank, in litres", "the tank empties"),
           ("a battery's charge as a percentage", "the battery dies"),
           ("the ice remaining in a cooler, in grams", "the ice has all melted")]
    raws = []
    for (ylab, end) in ctx:
        for b in (20, 24, 30, 36, 45, 48, 60):
            for m in (2, 3, 4, 5, 6):
                if b % m:
                    continue
                t = b // m
                raws.append({
                    "statement": "%s is modelled by $y = %s$, with $t$ in hours. Over what "
                                 "values of $t$ does the model describe the situation?"
                                 % (ylab[0].upper() + ylab[1:], lin(-m, b)),
                    "correct": "$0 \\le t \\le %d$" % t,
                    "dvals": [
                        "$t \\ge 0$, with no upper limit",
                        "$0 \\le t \\le %d$" % b,
                        "$0 \\le t \\le %d$" % m,
                    ],
                    "explanation": "The model starts at $t = 0$ and reaches zero when "
                                   "$%s = 0$, i.e. $t = %d$. Past that it predicts a "
                                   "NEGATIVE quantity, which is where %s and the model "
                                   "stops meaning anything. Stating the domain is part of "
                                   "building the model, not an optional extra."
                                   % (lin(-m, b), t, end),
                    "check": ["Eq(-%d*%d + %d, 0)" % (m, t, b),
                              "-%d*%d + %d < 0" % (m, t + 1, b)],
                })
    return raws


def g_compare_model_fit():
    """LEVEL 3 — which model fits better, judged by the residuals."""
    raws = []
    for e1 in (1, 2, 3):
        for e2 in (5, 6, 8, 9):
            for base in (10, 20, 30, 40, 50):
                for n in (3, 4, 5):
                    s1, s2 = e1 * n, e2 * n
                    raws.append({
                        "statement": "Two models are fitted to the same $%d$ data points. "
                                     "Model P's residuals have a total absolute size of "
                                     "$%d$; model Q's total is $%d$. Both pass near the "
                                     "point $(%d,\\ %d)$. Which model fits better, and "
                                     "why?" % (n, s1, s2, n, base),
                        "correct": "Model P — smaller residuals mean the predictions sit "
                                   "closer to the data.",
                        "dvals": [
                            "Model Q — larger residuals mean it covers more of the data.",
                            "Neither — residuals say nothing about fit.",
                            "Model Q — it must be the more complicated model.",
                        ],
                        "explanation": "A residual is how far a point sits from the model's "
                                       "prediction, so SMALLER total residuals mean a "
                                       "closer fit: $%d < %d$, and model P wins. Passing "
                                       "near one shared point tells you nothing — fit is "
                                       "judged across ALL the points, which is exactly what "
                                       "the residual total measures." % (s1, s2),
                        "check": ["%d < %d" % (s1, s2),
                                  "Eq(%d*%d, %d)" % (e1, n, s1),
                                  "Eq(%d*%d, %d)" % (e2, n, s2)],
                    })
    return raws
