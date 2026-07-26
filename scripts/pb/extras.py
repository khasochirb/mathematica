# -*- coding: utf-8 -*-
"""Extra dense forms for the thin problem-bank subjects.

Calculus, Vectors & Matrices, Precalculus and Prob-Stats were authored before
the ~36-variants-per-form standard and sit at ~12, so their unit pages are
noticeably shallower than Algebra 1's or Geometry's. Rather than perform
surgery on 167 existing generators, this module ADDS new archetypes to those
subjects through a single integration point in build_problembank.py.

Each form here sweeps a parameter grid through the shared imbank assemblers,
so it lands at the same depth as the IM banks and inherits the same guards:
a draw whose distractors collide with the answer AS VALUES is discarded, and
a form that ends up under the floor fails the build rather than shipping thin.

Add to a subject by appending to EXTRA_FORMS[slug].
"""
import os
import sys

from sympy import Integer, Rational, binomial, factorial

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt, pt, quad  # noqa: E402


# ===========================================================================
# Calculus
# ===========================================================================

def _g_power_rule():
    raws = []
    for a in (2, 3, 4, 5, 6, 7, 8, 10, 12):
        for n in (2, 3, 4, 5, 6):
            for c in (1, -3, 7):
                raws.append({
                    "statement": "Differentiate $f(x) = %dx^{%d} + %d$." % (a, n, c),
                    "correct": Integer(a * n),
                    "dvals": [Integer(a * n - a), Integer(a), Integer(a * n + c)],
                    "explanation": (
                        "The power rule multiplies by the exponent and drops it by one: "
                        "$\\frac{d}{dx}\\left(%dx^{%d}\\right) = %dx^{%d}$, and the constant "
                        "$%d$ differentiates to zero. The COEFFICIENT of the derivative is "
                        "$%d \\times %d = %d$." % (a, n, a * n, n - 1, c, a, n, a * n)),
                    "check": ["Eq(diff(%d*x**%d + (%d), x), %d*x**%d)"
                              % (a, n, c, a * n, n - 1)],
                })
    return raws


def _g_product_rule():
    raws = []
    for a in (2, 3, 4, 5):
        for b in (1, -2, 3, -4, 5):
            for c in (2, 3, -1, 4):
                # d/dx[(ax + b)(x + c)] = 2ax + (ac + b)
                raws.append({
                    "statement": ("Differentiate $f(x) = (%s)(x %s %d)$ and give the "
                                  "coefficient of $x$."
                                  % (("%dx + %d" % (a, b)) if b >= 0 else ("%dx - %d" % (a, -b)),
                                     "+" if c >= 0 else "-", abs(c))),
                    "correct": Integer(2 * a),
                    "dvals": [Integer(a), Integer(a * c + b), Integer(a + 1)],
                    "explanation": (
                        "Expanding first is legitimate: $(%dx %s %d)(x %s %d) = %dx^2 + %dx %s "
                        "%d$, whose derivative is $%dx + %d$. The coefficient of $x$ is $%d$ — "
                        "twice the leading coefficient, because the $x^2$ term dominates the "
                        "differentiation."
                        % (a, "+" if b >= 0 else "-", abs(b), "+" if c >= 0 else "-", abs(c),
                           a, a * c + b, "+" if b * c >= 0 else "-", abs(b * c),
                           2 * a, a * c + b, 2 * a)),
                    "check": ["Eq(expand(diff((%d*x + (%d))*(x + (%d)), x)), %d*x + (%d))"
                              % (a, b, c, 2 * a, a * c + b)],
                })
    return raws


def _g_definite_integral():
    raws = []
    for a in (1, 2, 3, 4, 6):
        for n in (1, 2, 3):
            for b in (1, 2, 3, 4, 5):
                # ∫₀^b a x^n dx = a b^(n+1)/(n+1)
                val = Rational(a * b ** (n + 1), n + 1)
                raws.append({
                    "statement": ("Evaluate $\\displaystyle\\int_0^{%d} %dx^{%d}\\,dx$."
                                  % (b, a, n)),
                    "correct": val,
                    # error models: forgot to divide; differentiated instead; wrong power
                    "dvals": [Integer(a * b ** (n + 1)), Integer(a * n * b),
                              Rational(a * b ** n, n + 1)],
                    "explanation": (
                        "Antidifferentiate then evaluate: $\\int %dx^{%d}dx = "
                        "\\frac{%d}{%d}x^{%d}$, and at $x = %d$ this is "
                        "$\\frac{%d \\cdot %d}{%d} = %s$ (the lower limit contributes $0$). "
                        "Forgetting to divide by the new exponent is the usual slip."
                        % (a, n, a, n + 1, n + 1, b, a, b ** (n + 1), n + 1, fmt(val))),
                    "check": ["Eq(integrate(%d*x**%d, (x, 0, %d)), Rational(%d,%d))"
                              % (a, n, b, val.p, val.q)],
                })
    return raws


def _g_tangent_line():
    raws = []
    for a in (1, 2, 3):
        for b in (-4, -2, 1, 3, 5):
            for x0 in (1, 2, 3, -1, -2):
                # f(x) = a x^2 + b x ; f'(x0) = 2 a x0 + b
                slope = 2 * a * x0 + b
                y0 = a * x0 * x0 + b * x0
                raws.append({
                    "statement": ("Find the slope of the tangent to $f(x) = %s$ at $x = %d$."
                                  % (quad(a, b, 0), x0)),
                    "correct": Integer(slope),
                    # error models: used f(x0); forgot the b; halved
                    "dvals": [Integer(y0), Integer(2 * a * x0), Integer(a * x0 + b)],
                    "explanation": (
                        "The slope of the tangent IS the derivative: $f'(x) = %dx %s %d$, so "
                        "$f'(%d) = %d$. The value $f(%d) = %d$ is the HEIGHT of the curve "
                        "there, not its steepness — that is the confusion this question tests."
                        % (2 * a, "+" if b >= 0 else "-", abs(b), x0, slope, x0, y0)),
                    "check": ["Eq(diff(%d*x**2 + (%d)*x, x).subs(x, %d), %d)"
                              % (a, b, x0, slope)],
                })
    return raws


# ===========================================================================
# Vectors & Matrices
# ===========================================================================

def _g_vector_magnitude():
    raws = []
    trip = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25),
            (12, 16, 20), (20, 21, 29), (10, 24, 26), (15, 20, 25), (9, 40, 41),
            (12, 35, 37), (16, 30, 34), (18, 24, 30)]
    for a, b, c in trip:
        for sa, sb in ((1, 1), (-1, 1), (1, -1)):
            x, y = sa * a, sb * b
            raws.append({
                "statement": "Find the magnitude of the vector $\\langle %d,\\ %d \\rangle$."
                             % (x, y),
                "correct": Integer(c),
                # error models: added components; used one only; forgot the root
                "dvals": [Integer(abs(x) + abs(y)), Integer(max(abs(x), abs(y))),
                          Integer(c * c)],
                "explanation": (
                    "Magnitude is $\\sqrt{x^2 + y^2} = \\sqrt{%d + %d} = \\sqrt{%d} = %d$. "
                    "Signs vanish under the squares, so $\\langle %d,\\ %d \\rangle$ is exactly "
                    "as long as $\\langle %d,\\ %d \\rangle$ — adding the components instead "
                    "measures the path along the axes."
                    % (x * x, y * y, c * c, c, x, y, abs(x), abs(y))),
                "check": ["Eq((%d)**2 + (%d)**2, %d**2)" % (x, y, c)],
            })
    return raws


def _g_dot_product():
    raws = []
    grid = [(a, b, c, d) for a, b in ((3, 4), (2, 5), (-1, 6), (7, -2), (4, 4), (-3, -5))
            for c, d in ((1, 2), (5, -3), (-2, 4), (6, 1), (0, 7), (3, -6))]
    for a, b, c, d in grid:
        val = a * c + b * d
        raws.append({
            "statement": ("Find $\\langle %d,\\ %d \\rangle \\cdot \\langle %d,\\ %d \\rangle$."
                          % (a, b, c, d)),
            "correct": Integer(val),
            # error models: cross-multiplied; subtracted; added all four
            "dvals": [Integer(a * d + b * c), Integer(a * c - b * d), Integer(a + b + c + d)],
            "explanation": (
                "The dot product multiplies MATCHING components and adds: "
                "$(%d)(%d) + (%d)(%d) = %d + %d = %d$. Pairing across ($ad + bc$) is the "
                "determinant-style pattern, not the dot product."
                % (a, c, b, d, a * c, b * d, val)),
            "check": ["Eq(%d*%d + %d*%d, %d)" % (a, c, b, d, val)],
        })
    return raws


def _g_determinant_2x2():
    raws = []
    grid = [(a, b, c, d) for a, b in ((3, 4), (2, 5), (1, 6), (7, 2), (4, 3), (5, 1), (6, 7))
            for c, d in ((1, 2), (5, 3), (2, 4), (6, 1), (3, 7))]
    for a, b, c, d in grid:
        det = a * d - b * c
        raws.append({
            "statement": ("Find the determinant of $\\begin{pmatrix} %d & %d \\\\ %d & %d "
                          "\\end{pmatrix}$." % (a, b, c, d)),
            "correct": Integer(det),
            # error models: added instead of subtracted; wrong diagonal; summed entries
            "dvals": [Integer(a * d + b * c), Integer(b * c - a * d), Integer(a + b + c + d)],
            "explanation": (
                "For a $2 \\times 2$ matrix the determinant is $ad - bc$: "
                "$(%d)(%d) - (%d)(%d) = %d - %d = %d$. The MAIN diagonal product comes first "
                "and the anti-diagonal is subtracted — reversing them flips the sign."
                % (a, d, b, c, a * d, b * c, det)),
            "check": ["Eq(%d*%d - %d*%d, %d)" % (a, d, b, c, det)],
        })
    return raws


def _g_vector_add():
    raws = []
    grid = [(a, b, c, d, k) for a, b in ((3, 4), (2, 5), (-1, 6), (7, -2), (4, 4))
            for c, d in ((1, 2), (5, -3), (-2, 4), (6, 1))
            for k in (2, 3, -1)]
    for a, b, c, d, k in grid:
        rx = a + k * c
        raws.append({
            "statement": ("If $\\vec{u} = \\langle %d,\\ %d \\rangle$ and $\\vec{v} = "
                          "\\langle %d,\\ %d \\rangle$, find the $x$-component of "
                          "$\\vec{u} + %d\\vec{v}$." % (a, b, c, d, k)),
            "correct": Integer(rx),
            # error models: scaled u instead; added without scaling; used the y-component
            "dvals": [Integer(k * a + c), Integer(a + c), Integer(b + k * d)],
            "explanation": (
                "Scalar multiplication scales EVERY component, then addition is "
                "componentwise: the $x$-component is $%d + %d(%d) = %d$. The scalar attaches "
                "to $\\vec{v}$, not to $\\vec{u}$."
                % (a, k, c, rx)),
            "check": ["Eq(%d + %d*%d, %d)" % (a, k, c, rx)],
        })
    return raws


# ===========================================================================
# Precalculus
# ===========================================================================

def _g_function_composition():
    raws = []
    grid = [(a, b, c, d, x0) for a, b in ((2, 3), (3, -1), (4, 5), (-2, 7), (5, 2))
            for c, d in ((1, 4), (2, -3), (3, 1))
            for x0 in (1, 2, -1, 3)]
    for a, b, c, d, x0 in grid:
        inner = c * x0 + d
        val = a * inner + b
        raws.append({
            "statement": ("If $f(x) = %s$ and $g(x) = %s$, find $f(g(%d))$."
                          % (quad(0, a, b), quad(0, c, d), x0)),
            "correct": Integer(val),
            # error models: composed the other way; multiplied the outputs; added them
            "dvals": [Integer(c * (a * x0 + b) + d), Integer((a * x0 + b) * inner),
                      Integer((a * x0 + b) + inner)],
            "explanation": (
                "Work from the INSIDE out: $g(%d) = %d$, then $f(%d) = %d$. Composing the "
                "other way, $g(f(%d))$, gives $%d$ — composition is not commutative, which is "
                "exactly what this tests."
                % (x0, inner, inner, val, x0, c * (a * x0 + b) + d)),
            "check": ["Eq((%d*(%d*%d + %d) + %d), %d)" % (a, c, x0, d, b, val)],
        })
    return raws


def _g_log_evaluate():
    raws = []
    for base in (2, 3, 5, 10, 4, 6, 7):
        for n in (1, 2, 3, 4, 5):
            val = base ** n
            if val > 100000:
                continue
            raws.append({
                "statement": "Evaluate $\\log_{%d} %d$." % (base, val),
                "correct": Integer(n),
                # error models: gave the argument; gave base*n; gave the base
                "dvals": [Integer(val), Integer(base * n), Integer(base)],
                "explanation": (
                    "$\\log_{%d} %d$ asks: to what power must $%d$ be raised to give $%d$? "
                    "Since $%d^{%d} = %d$, the answer is $%d$. A logarithm returns the "
                    "EXPONENT, never the number itself."
                    % (base, val, base, val, base, n, val, n)),
                "check": ["Eq(log(%d, %d), %d)" % (val, base, n)],
            })
    return raws


def _g_exp_log_solve():
    raws = []
    for base in (2, 3, 5, 10):
        for n in (2, 3, 4, 5):
            for k in (1, 2, 3, -1, -2):
                # base^(x - k) = base^n  ->  x = n + k
                val = base ** n
                raws.append({
                    "statement": ("Solve $%d^{\\,x %s %d} = %d$."
                                  % (base, "-" if k >= 0 else "+", abs(k), val)),
                    "correct": Integer(n + k),
                    "dvals": [Integer(n), Integer(n - k), Integer(val)],
                    "explanation": (
                        "Both sides are powers of $%d$, and $%d = %d^{%d}$, so the exponents "
                        "must match: $x %s %d = %d$, giving $x = %d$. Equating the exponents "
                        "is legal precisely because $y = %d^x$ is one-to-one."
                        % (base, val, base, n, "-" if k >= 0 else "+", abs(k), n, n + k, base)),
                    "check": ["Eq(%d**((%d) - (%d)), %d)" % (base, n + k, k, val)],
                })
    return raws


# LaTeX exact value -> sympy literal. The check asserts that the STATED value
# really equals the trig function, so a wrong table entry fails the build.
# Without this map the check could only compare sin(x) to sin(x) — a check
# that can never fail is not a check.
_SY = {
    "0": "0",
    "1": "1",
    "-1": "-1",
    "\\frac{1}{2}": "Rational(1,2)",
    "-\\frac{1}{2}": "-Rational(1,2)",
    "\\frac{\\sqrt{2}}{2}": "sqrt(2)/2",
    "-\\frac{\\sqrt{2}}{2}": "-sqrt(2)/2",
    "\\frac{\\sqrt{3}}{2}": "sqrt(3)/2",
    "-\\frac{\\sqrt{3}}{2}": "-sqrt(3)/2",
}


def _g_unit_circle_exact():
    raws = []
    # (degrees, sin, cos) with exact values written as latex
    # (deg, sin latex, cos latex, sin sympy, cos sympy) — the sympy column
    # exists so the check asserts the STATED value rather than a tautology.
    table = [
        (0, "0", "1"), (30, "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"),
        (45, "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}"),
        (60, "\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}"), (90, "1", "0"),
        (120, "\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2}"),
        (135, "\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}"),
        (150, "\\frac{1}{2}", "-\\frac{\\sqrt{3}}{2}"), (180, "0", "-1"),
        (210, "-\\frac{1}{2}", "-\\frac{\\sqrt{3}}{2}"),
        (225, "-\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}"),
        (240, "-\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2}"), (270, "-1", "0"),
        (300, "-\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}"),
        (315, "-\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}"),
        (330, "-\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"),
    ]
    allvals = ["0", "1", "-1", "\\frac{1}{2}", "-\\frac{1}{2}",
               "\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}",
               "\\frac{\\sqrt{3}}{2}", "-\\frac{\\sqrt{3}}{2}"]
    for deg, s, c in table:
        for name, val in (("\\sin", s), ("\\cos", c)):
            ds = [v for v in allvals if v != val][:3]
            raws.append({
                "statement": "Give the exact value of $%s %d°$." % (name, deg),
                "correct": "$%s$" % val,
                "dvals": ["$%s$" % d for d in ds],
                "explanation": (
                    "On the unit circle the point at $%d°$ has coordinates "
                    "$(\\cos %d°,\\ \\sin %d°) = (%s,\\ %s)$, so $%s %d° = %s$. The sign "
                    "follows the quadrant and the magnitude follows the reference angle."
                    % (deg, deg, deg, c, s, name, deg, val)),
                "check": ["Eq(simplify(%s(Rational(%d,180)*pi) - (%s)), 0)"
                          % ("sin" if name == "\\sin" else "cos", deg, _SY[val])],
            })
    return raws


# ===========================================================================
# Prob-Stats
# ===========================================================================

def _g_permutations_combinations():
    raws = []
    for n in (5, 6, 7, 8, 9, 10, 12):
        for r in (2, 3, 4):
            if r >= n:
                continue
            nPr = Integer(factorial(n) / factorial(n - r))
            nCr = Integer(binomial(n, r))
            raws.append({
                "statement": ("From $%d$ distinct items, how many ORDERED arrangements of $%d$ "
                              "are there?" % (n, r)),
                "correct": nPr,
                "dvals": [nCr, Integer(n ** r), Integer(n * r)],
                "explanation": (
                    "Order matters, so this is a permutation: $P(%d,%d) = \\frac{%d!}{(%d-%d)!} "
                    "= %s$. The combination $C(%d,%d) = %s$ counts the same selections while "
                    "IGNORING order, which is why it is $%d!$ times smaller."
                    % (n, r, n, n, r, fmt(nPr), n, r, fmt(nCr), r)),
                "check": ["Eq(factorial(%d)/factorial(%d - %d), %s)" % (n, n, r, nPr)],
            })
            raws.append({
                "statement": ("From $%d$ distinct items, how many UNORDERED selections of $%d$ "
                              "are there?" % (n, r)),
                "correct": nCr,
                "dvals": [nPr, Integer(n ** r), Integer(n * r)],
                "explanation": (
                    "Order does not matter, so this is a combination: $C(%d,%d) = %s$. Each "
                    "unordered selection could be arranged in $%d! = %s$ ways, which is exactly "
                    "the factor separating it from $P(%d,%d) = %s$."
                    % (n, r, fmt(nCr), r, fmt(Integer(factorial(r))), n, r, fmt(nPr))),
                "check": ["Eq(binomial(%d, %d), %s)" % (n, r, nCr)],
            })
    return raws


def _g_binomial_probability():
    raws = []
    for n in (3, 4, 5, 6):
        for k in (1, 2, 3):
            if k > n:
                continue
            for num, den in ((1, 2), (1, 3), (2, 3), (1, 4)):
                p = Rational(num, den)
                val = binomial(n, k) * p ** k * (1 - p) ** (n - k)
                raws.append({
                    "statement": ("A trial succeeds with probability $%s$. In $%d$ independent "
                                  "trials, find $P(\\text{exactly } %d \\text{ successes})$."
                                  % (fmt(p), n, k)),
                    "correct": val,
                    # error models: dropped the binomial coefficient; ignored the failures;
                    # used the wrong count
                    "dvals": [p ** k * (1 - p) ** (n - k), binomial(n, k) * p ** k,
                              p ** k],
                    "explanation": (
                        "The binomial formula is $\\binom{n}{k}p^k(1-p)^{n-k}$: "
                        "$\\binom{%d}{%d} = %s$ ways to choose WHICH trials succeed, times "
                        "$%s^{%d}$ for those successes, times $%s^{%d}$ for the failures, "
                        "giving $%s$. Dropping the coefficient counts only one specific "
                        "ordering."
                        % (n, k, fmt(Integer(binomial(n, k))), fmt(p), k, fmt(1 - p), n - k,
                           fmt(val))),
                    "check": ["Eq(binomial(%d,%d)*Rational(%d,%d)**%d*(1 - Rational(%d,%d))**%d, "
                              "Rational(%d,%d))"
                              % (n, k, num, den, k, num, den, n - k,
                                 Rational(val).p, Rational(val).q)],
                })
    return raws


def _g_expected_value():
    raws = []
    grid = [(a, b, pa, pb) for a, b in ((10, 20), (5, 15), (0, 100), (3, 9), (25, 50), (8, 12))
            for pa, pb in ((Rational(1, 2), Rational(1, 2)),
                           (Rational(1, 4), Rational(3, 4)),
                           (Rational(1, 3), Rational(2, 3)),
                           (Rational(1, 5), Rational(4, 5)),
                           (Rational(2, 5), Rational(3, 5)))]
    for a, b, pa, pb in grid:
        ev = pa * a + pb * b
        raws.append({
            "statement": ("A random variable takes the value $%d$ with probability $%s$ and "
                          "$%d$ with probability $%s$. Find its expected value."
                          % (a, fmt(pa), b, fmt(pb))),
            "correct": ev,
            # error models: unweighted mean; summed the values; used the wrong weights
            "dvals": [Rational(a + b, 2), Integer(a + b), pb * a + pa * b],
            "explanation": (
                "Expected value weights each outcome by its probability: "
                "$%s(%d) + %s(%d) = %s$. The plain average $%s$ would be right only if the "
                "two outcomes were equally likely."
                % (fmt(pa), a, fmt(pb), b, fmt(ev), fmt(Rational(a + b, 2)))),
            "check": ["Eq(Rational(%d,%d)*%d + Rational(%d,%d)*%d, Rational(%d,%d))"
                      % (pa.p, pa.q, a, pb.p, pb.q, b, Rational(ev).p, Rational(ev).q)],
        })
    return raws


def _g_zscore():
    raws = []
    grid = [(mu, sd, x) for mu, sd in ((100, 15), (50, 10), (80, 5), (200, 20), (60, 8),
                                       (75, 12), (500, 100))
            for x in (-2, -1, 1, 2, 3)]
    for mu, sd, xk in grid:
        val = mu + xk * sd
        raws.append({
            "statement": ("A distribution has mean $%d$ and standard deviation $%d$. Find the "
                          "$z$-score of the value $%d$." % (mu, sd, val)),
            "correct": Integer(xk),
            # error models: subtracted the other way; forgot to divide; divided by the mean
            "dvals": [Integer(-xk), Integer(xk * sd), Rational(xk * sd, mu)],
            "explanation": (
                "A $z$-score counts standard deviations from the mean: "
                "$z = \\frac{%d - %d}{%d} = \\frac{%d}{%d} = %d$. The sign says which side of "
                "the mean the value sits on, so reversing the subtraction reverses the meaning."
                % (val, mu, sd, xk * sd, sd, xk)),
            "check": ["Eq(Rational(%d - %d, %d), %d)" % (val, mu, sd, xk)],
        })
    return raws


# ===========================================================================
# Registry — one entry per subject slug
# ===========================================================================

def extra_forms(slug):
    """New forms to append to the given subject, or [] if it has none."""
    if slug == "calculus":
        return [
            form("cal-power-rule", "The power rule", 1, "the-derivative",
                 "Multiply by the exponent, drop it by one; constants vanish.",
                 mk_num("CALX-pow", _g_power_rule())),
            form("cal-tangent-slope", "Slope of a tangent line", 2, "applications-of-derivatives",
                 "The derivative IS the slope — not the height of the curve.",
                 mk_num("CALX-tan", _g_tangent_line())),
            form("cal-product-expand", "Differentiating a product", 2,
                 "differentiation-techniques",
                 "Expand or apply the product rule — both must give the same coefficient.",
                 mk_num("CALX-prod", _g_product_rule())),
            form("cal-definite-integral", "Definite integrals of powers", 2, "integrals",
                 "Raise the exponent, divide by the new one, then evaluate at the limits.",
                 mk_num("CALX-int", _g_definite_integral())),
        ]
    if slug == "vectors-matrices":
        return [
            form("vm-magnitude", "Magnitude of a vector", 1, "vectors-and-coordinates",
                 "√(x² + y²) — signs disappear under the squares.",
                 mk_num("VMX-mag", _g_vector_magnitude())),
            form("vm-linear-combination", "Adding and scaling vectors", 1, "vector-arithmetic",
                 "The scalar attaches to its own vector, then components add.",
                 mk_num("VMX-add", _g_vector_add())),
            form("vm-dot-product", "The dot product", 2, "the-dot-product",
                 "Multiply MATCHING components and add; pairing across is a different operation.",
                 mk_num("VMX-dot", _g_dot_product())),
            form("vm-determinant", "Determinant of a 2x2 matrix", 2, "determinants-and-inverses",
                 "ad - bc, main diagonal first — reversing the order flips the sign.",
                 mk_num("VMX-det", _g_determinant_2x2())),
        ]
    if slug == "precalculus":
        return [
            form("pc-composition", "Composing functions", 2, "functions-and-their-graphs",
                 "Work inside out; f(g(x)) and g(f(x)) are generally different.",
                 mk_num("PCX-comp", _g_function_composition())),
            form("pc-log-evaluate", "Evaluating logarithms", 1, "exponentials-and-logarithms",
                 "A logarithm returns the EXPONENT, never the number itself.",
                 mk_num("PCX-log", _g_log_evaluate())),
            form("pc-exp-equation", "Exponential equations with a matched base", 2,
                 "exponentials-and-logarithms",
                 "Write both sides as powers of one base, then equate the exponents.",
                 mk_num("PCX-exp", _g_exp_log_solve())),
            form("pc-unit-circle", "Exact values on the unit circle", 1, "the-unit-circle",
                 "Quadrant fixes the sign; the reference angle fixes the magnitude.",
                 mk_txt("PCX-uc", _g_unit_circle_exact())),
        ]
    if slug == "prob-stats":
        return [
            form("ps-perm-comb", "Permutations against combinations", 2, "combinations",
                 "Order matters or it does not — the factor between them is r!.",
                 mk_num("PSX-pc", _g_permutations_combinations())),
            form("ps-binomial", "The binomial distribution", 2, "binomial-distribution",
                 "Choose WHICH trials succeed, then weight successes and failures.",
                 mk_num("PSX-bin", _g_binomial_probability())),
            form("ps-expected-value", "Expected value", 2, "random-variables",
                 "Weight each outcome by its probability — not a plain average.",
                 mk_num("PSX-ev", _g_expected_value())),
            form("ps-zscore", "z-scores", 2, "distributions-and-position",
                 "How many standard deviations from the mean, with the sign kept.",
                 mk_num("PSX-z", _g_zscore())),
        ]
    return []
