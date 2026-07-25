"""AA HL Practice Paper 1 (ib-hl-practice-4) — 120 min, 110 marks, NO calculator.

Blueprint (topic x marks):
    Section A (52): Q1 number_algebra 5  | Q2 functions 9
                    Q3 geometry_trig 8   | Q4 stats_probability 7
                    Q5 calculus 7        | Q6 number_algebra 8
                    Q7 calculus 8
    Section B (58): Q8 geometry_trig 20  | Q9 calculus 21
                    Q10 stats_probability 17
    Paper totals: number_algebra 13 | functions 9 | geometry_trig 28 |
                  stats_probability 24 | calculus 36 = 110.

HL-only content, fresh versus HL Sets 1-3: binomial-theorem coefficients
from (2 + x)^7, a log/exp pair shown to be mutual inverses, the
product-to-sum identity cos(A-B) - cos(A+B) = 2 sin A sin B used as a
"hence" lever, independence feeding a conditional probability, the chain
rule with a tangent, simultaneous logarithmic equations, integration by
substitution, TWO INTERSECTING lines in 3D with the plane that contains
them and a point-to-line distance, ln(x)/x through the full calculus
cycle, and a CONTINUOUS random variable with its mean, variance and an
interval probability. Everything exact.
Figure: Q9 (region under ln(x)/x from 1 to e).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, I, Matrix, simplify, solve,  # noqa: F401,E402
                   expand, factor, diff, integrate, atan, sin, cos, tan,
                   binomial, factorial, symbols, Abs, log, exp, E, oo, limit)

x, y, t, s, k, n, m = symbols("x y t s k n m")


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [5] number_algebra: binomial-theorem coefficients ────────────────
assert binomial(7, 3) * 2**4 == 560
assert binomial(7, 5) * 2**2 == 84
QS.append(question(
    "IB-AAHL-P1-T4-Q1", 1, "A", "number_algebra", "binomial_theorem",
    contextIntro=("Consider the expansion of $(2 + x)^{7}$."),
    parts=[
        part("a", "Find the coefficient of $x^{3}$.", 3,
             [M1("general term $\\binom{7}{r}2^{7-r}x^{r}$ with $r = 3$"),
              A1("$\\binom{7}{3}2^{4} = 35 \\times 16$"),
              A1("$560$")],
             answer="$560$",
             solution=("The general term of $(2 + x)^{7}$ is"
                       "$$\\binom{7}{r}2^{\\,7-r}x^{r}.$$"
                       " For $x^{3}$ take $r = 3$, so the coefficient is"
                       "$$\\binom{7}{3}2^{4} = 35 \\times 16 = 560.$$"
                       " Note the power of $2$ is $7 - r$, not $r$ — that"
                       " swap is the usual slip."),
             verify=["Eq(binomial(7, 3), 35)", "Eq(35*2**4, 560)",
                     "Eq(expand((2 + x)**7).coeff(x, 3), 560)"]),
        part("b", "Find the coefficient of $x^{5}$.", 2,
             [M1("$\\binom{7}{5}2^{2}$"),
              A1("$84$")],
             answer="$84$",
             solution=("Now $r = 5$, so the coefficient is"
                       "$$\\binom{7}{5}2^{2} = 21 \\times 4 = 84.$$"),
             verify=["Eq(binomial(7, 5), 21)", "Eq(21*2**2, 84)",
                     "Eq(expand((2 + x)**7).coeff(x, 5), 84)"]),
    ]))

# ── Q2 [9] functions: a log/exp pair that are mutual inverses ───────────
assert simplify(log(exp(2) + 1 - 1)) == 2
assert simplify(exp(log(5 - 1)) + 1) == 5
QS.append(question(
    "IB-AAHL-P1-T4-Q2", 2, "A", "functions", "inverse_functions",
    contextIntro=("The functions $f$ and $g$ are defined by"
                  " $f(x) = \\ln(x - 1)$ and"
                  " $g(x) = \\mathrm{e}^{x} + 1$."),
    parts=[
        part("a", "State the domain of $f$.", 2,
             [R1("the argument of a logarithm must be positive"),
              A1("$x > 1$")],
             answer="$x > 1$",
             solution=("A logarithm is defined only for a positive"
                       " argument, so we need"
                       "$$x - 1 > 0 \\;\\Rightarrow\\; x > 1.$$"
                       " The domain of $f$ is $\\{x \\in \\mathbb{R} :"
                       " x > 1\\}$."),
             verify=["Eq(2 - 1, 1)", "2 - 1 > 0", "Eq(log(1), 0)"]),
        part("b", "Show that $(f \\circ g)(x) = x$ for all"
             " $x \\in \\mathbb{R}$.", 3,
             [M1("substitute $g$ into $f$:"
                 " $f(g(x)) = \\ln\\!\\left(\\mathrm{e}^{x} + 1 - 1\\right)$"),
              A1("$= \\ln\\!\\left(\\mathrm{e}^{x}\\right)$"),
              AG()],
             answer="$(f \\circ g)(x) = x$ (given)",
             solution=("Feed $g$ into $f$:"
                       "$$f(g(x)) = \\ln\\!\\left(g(x) - 1\\right)"
                       " = \\ln\\!\\left(\\mathrm{e}^{x} + 1 - 1\\right)"
                       " = \\ln\\!\\left(\\mathrm{e}^{x}\\right) = x.$$"
                       " The composition is defined for every real $x$"
                       " because $\\mathrm{e}^{x} + 1 > 1$ always, so"
                       " $g(x)$ always lands inside the domain of $f$."),
             verify=["Eq(simplify(log(exp(2) + 1 - 1)), 2)",
                     "Eq(simplify(log(exp(-3) + 1 - 1)), -3)",
                     "exp(0) + 1 > 1"]),
        part("c", "State the range of $f$.", 2,
             [R1("$\\ln u$ takes every real value as $u$ ranges over"
                 " $(0, \\infty)$"),
              A1("$f(x) \\in \\mathbb{R}$")],
             answer="all real numbers, $f(x) \\in \\mathbb{R}$",
             solution=("As $x$ runs over the domain $(1, \\infty)$, the"
                       " argument $x - 1$ runs over $(0, \\infty)$, and"
                       " $\\ln u$ takes every real value on that interval:"
                       "$$\\ln u \\to -\\infty \\text{ as } u \\to 0^{+},"
                       " \\qquad \\ln u \\to \\infty \\text{ as } u \\to"
                       " \\infty.$$"
                       " So the range of $f$ is $\\mathbb{R}$."),
             verify=["Eq(limit(log(x), x, oo), oo)",
                     "Eq(log(exp(-5)), -5)", "Eq(log(exp(5)), 5)"]),
        part("d", "State what part (b), together with the domain and range"
             " found above, shows about the relationship between $f$ and"
             " $g$.", 2,
             [R1("the composition returns the input, and the domain of one"
                 " is the range of the other"),
              A1("$g = f^{-1}$ (equivalently $f = g^{-1}$)")],
             answer="$f$ and $g$ are inverses of each other:"
                    " $g = f^{-1}$",
             solution=("Part (b) shows that applying $g$ and then $f$"
                       " returns the original input. Moreover the range of"
                       " $g$ is $(1, \\infty)$, which is exactly the domain"
                       " of $f$, and the range of $f$ is $\\mathbb{R}$,"
                       " which is exactly the domain of $g$. Those two"
                       " facts together mean the functions undo each other"
                       " in both directions, so"
                       "$$g = f^{-1} \\quad\\text{and}\\quad f = g^{-1}.$$"
                       " As a check the other way round:"
                       " $g(f(x)) = \\mathrm{e}^{\\ln(x-1)} + 1"
                       " = (x - 1) + 1 = x$ for $x > 1$."),
             verify=["Eq(simplify(exp(log(5 - 1)) + 1), 5)",
                     "Eq(simplify(log(exp(2) + 1 - 1)), 2)"]),
    ]))

# ── Q3 [8] geometry_trig: product-to-sum, then a "hence" solve ──────────
assert simplify(cos(x - y) - cos(x + y) - 2 * sin(x) * sin(y)) == 0
assert simplify(cos(pi / 6 - pi / 6) - cos(pi / 6 + pi / 6)) == Rational(1, 2)
QS.append(question(
    "IB-AAHL-P1-T4-Q3", 3, "A", "geometry_trig", "trig_identities",
    parts=[
        part("a", "Show that $\\cos(A - B) - \\cos(A + B)"
             " = 2\\sin A \\sin B$.", 3,
             [M1("expand both compound angles"),
              A1("$(\\cos A\\cos B + \\sin A\\sin B)"
                 " - (\\cos A\\cos B - \\sin A\\sin B)$"),
              AG()],
             answer="identity (given)",
             solution=("Expand each compound angle with the standard"
                       " formulas:"
                       "$$\\cos(A - B) = \\cos A\\cos B"
                       " + \\sin A\\sin B,$$"
                       "$$\\cos(A + B) = \\cos A\\cos B"
                       " - \\sin A\\sin B.$$"
                       " Subtracting, the $\\cos A\\cos B$ terms cancel and"
                       " the two sine products add:"
                       "$$\\cos(A - B) - \\cos(A + B)"
                       " = 2\\sin A\\sin B.$$"),
             verify=["Eq(simplify(cos(x - y) - cos(x + y)"
                     " - 2*sin(x)*sin(y)), 0)",
                     "Eq(simplify(cos(pi/3 - pi/4) - cos(pi/3 + pi/4)"
                     " - 2*sin(pi/3)*sin(pi/4)), 0)"]),
        part("b", "Hence solve"
             " $\\cos\\!\\left(x - \\dfrac{\\pi}{6}\\right)"
             " - \\cos\\!\\left(x + \\dfrac{\\pi}{6}\\right)"
             " = \\dfrac{1}{2}$ for $0 \\le x < 2\\pi$.", 5,
             [M1("apply part (a) with $A = x$, $B = \\dfrac{\\pi}{6}$"),
              A1("$2\\sin x \\sin\\dfrac{\\pi}{6} = \\sin x$"),
              A1("$\\sin x = \\dfrac{1}{2}$"),
              A1("$x = \\dfrac{\\pi}{6}$"),
              A1("$x = \\dfrac{5\\pi}{6}$")],
             answer="$x = \\dfrac{\\pi}{6}$ or $x = \\dfrac{5\\pi}{6}$",
             solution=("Apply the identity from part (a) with $A = x$ and"
                       " $B = \\dfrac{\\pi}{6}$:"
                       "$$\\cos\\!\\left(x - \\frac{\\pi}{6}\\right)"
                       " - \\cos\\!\\left(x + \\frac{\\pi}{6}\\right)"
                       " = 2\\sin x \\sin\\frac{\\pi}{6}"
                       " = 2\\sin x \\cdot \\frac{1}{2} = \\sin x.$$"
                       " The equation therefore collapses to"
                       "$$\\sin x = \\frac{1}{2}.$$"
                       " On $[0, 2\\pi)$ the sine equals $\\tfrac12$ in the"
                       " first and second quadrants:"
                       "$$x = \\frac{\\pi}{6} \\quad\\text{or}\\quad"
                       " x = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}.$$"),
             verify=["Eq(sin(pi/6), Rational(1,2))",
                     "Eq(sin(5*pi/6), Rational(1,2))",
                     "Eq(simplify(cos(pi/6 - pi/6) - cos(pi/6 + pi/6)),"
                     " Rational(1,2))",
                     "Eq(simplify(cos(5*pi/6 - pi/6) - cos(5*pi/6 + pi/6)),"
                     " Rational(1,2))"]),
    ]))

# ── Q4 [7] stats_probability: independence into a conditional ───────────
assert Rational(4, 10) + Rational(5, 10) - Rational(2, 10) == Rational(7, 10)
assert Rational(4, 10) / Rational(7, 10) == Rational(4, 7)
QS.append(question(
    "IB-AAHL-P1-T4-Q4", 4, "A", "stats_probability", "probability_rules",
    contextIntro=("$A$ and $B$ are independent events with"
                  " $P(A) = 0.4$ and $P(B) = 0.5$."),
    parts=[
        part("a", "Find $P(A \\cup B)$.", 3,
             [M1("independence gives"
                 " $P(A \\cap B) = P(A)P(B) = 0.2$"),
              M1("addition rule"
                 " $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$"),
              A1("$\\dfrac{7}{10}$")],
             answer="$P(A \\cup B) = \\dfrac{7}{10} = 0.7$",
             solution=("Independence lets us multiply for the"
                       " intersection:"
                       "$$P(A \\cap B) = P(A)P(B) = 0.4 \\times 0.5"
                       " = 0.2.$$"
                       " Then the addition rule gives"
                       "$$P(A \\cup B) = 0.4 + 0.5 - 0.2 = 0.7"
                       " = \\frac{7}{10}.$$"
                       " Subtracting the overlap matters — simply adding"
                       " would double-count the $0.2$."),
             verify=["Eq(Rational(4,10)*Rational(5,10), Rational(2,10))",
                     "Eq(Rational(4,10) + Rational(5,10) - Rational(2,10),"
                     " Rational(7,10))"]),
        part("b", "Find $P(A \\mid A \\cup B)$.", 4,
             [M1("$P(A \\mid A \\cup B)"
                 " = \\dfrac{P(A \\cap (A \\cup B))}{P(A \\cup B)}$"),
              R1("$A \\subseteq A \\cup B$, so the numerator is $P(A)$"),
              A1("$\\dfrac{0.4}{0.7}$"),
              A1("$\\dfrac{4}{7}$")],
             answer="$\\dfrac{4}{7}$",
             solution=("Use the definition of conditional probability:"
                       "$$P(A \\mid A \\cup B)"
                       " = \\frac{P\\big(A \\cap (A \\cup B)\\big)}"
                       "{P(A \\cup B)}.$$"
                       " Every outcome in $A$ is already in $A \\cup B$, so"
                       " $A \\cap (A \\cup B) = A$ and the numerator is"
                       " simply $P(A) = 0.4$. Hence"
                       "$$P(A \\mid A \\cup B) = \\frac{0.4}{0.7}"
                       " = \\frac{4}{7}.$$"
                       " This exceeds $P(A) = 0.4$, as it must: knowing"
                       " that at least one event occurred makes $A$ more"
                       " likely."),
             verify=["Eq(Rational(4,10)/Rational(7,10), Rational(4,7))",
                     "Rational(4,7) > Rational(4,10)"]),
    ]))

# ── Q5 [7] calculus: chain rule and a tangent ──────────────────────────
assert simplify(diff((3 * x**2 - 1) ** 4, x) - 24 * x * (3 * x**2 - 1) ** 3) == 0
assert (3 * 1**2 - 1) ** 4 == 16 and 24 * 1 * (3 * 1**2 - 1) ** 3 == 192
QS.append(question(
    "IB-AAHL-P1-T4-Q5", 5, "A", "calculus", "chain_rule",
    contextIntro=("A curve has equation $y = \\left(3x^{2} - 1\\right)^{4}$."),
    parts=[
        part("a", "Find $\\dfrac{dy}{dx}$.", 4,
             [M1("chain rule: differentiate the outer power"),
              A1("$4\\left(3x^{2} - 1\\right)^{3}$"),
              M1("multiply by the derivative of the inside, $6x$"),
              A1("$\\dfrac{dy}{dx}"
                 " = 24x\\left(3x^{2} - 1\\right)^{3}$")],
             answer="$\\dfrac{dy}{dx} = 24x\\left(3x^{2} - 1\\right)^{3}$",
             solution=("Differentiate the outer fourth power first, then"
                       " multiply by the derivative of the inside:"
                       "$$\\frac{dy}{dx}"
                       " = 4\\left(3x^{2} - 1\\right)^{3} \\cdot 6x"
                       " = 24x\\left(3x^{2} - 1\\right)^{3}.$$"
                       " Forgetting the inner derivative $6x$ is the"
                       " classic chain-rule omission."),
             verify=["Eq(simplify(diff((3*x**2 - 1)**4, x)"
                     " - 24*x*(3*x**2 - 1)**3), 0)",
                     "Eq(diff(3*x**2 - 1, x), 6*x)"]),
        part("b", "Find the equation of the tangent to the curve at the"
             " point where $x = 1$, giving your answer in the form"
             " $y = mx + c$.", 3,
             [M1("evaluate the derivative at $x = 1$"),
              A1("gradient $= 192$, and $y = 16$ there"),
              A1("$y = 192x - 176$")],
             answer="$y = 192x - 176$",
             solution=("At $x = 1$ the inside is $3 - 1 = 2$, so the point"
                       " on the curve is"
                       "$$y = 2^{4} = 16,$$"
                       " and the gradient is"
                       "$$\\left.\\frac{dy}{dx}\\right|_{x=1}"
                       " = 24(1)(2)^{3} = 192.$$"
                       " The tangent through $(1, 16)$ with gradient $192$"
                       " is"
                       "$$y - 16 = 192(x - 1) \\;\\Rightarrow\\;"
                       " y = 192x - 176.$$"),
             verify=["Eq((3*1**2 - 1)**4, 16)",
                     "Eq(24*1*(3*1**2 - 1)**3, 192)",
                     "Eq(192*1 - 176, 16)"]),
    ]))

# ── Q6 [8] number_algebra: simultaneous and quadratic logarithms ────────
assert log(8, 2) == 3 and log(4, 2) == 2
assert 3 * (3 - 2) == 3
QS.append(question(
    "IB-AAHL-P1-T4-Q6", 6, "A", "number_algebra", "logarithms",
    parts=[
        part("a", "Solve the simultaneous equations"
             " $\\log_2 x + \\log_2 y = 5$ and"
             " $\\log_2 x - \\log_2 y = 1$.", 4,
             [M1("add the two equations to eliminate $\\log_2 y$"),
              A1("$\\log_2 x = 3$, so $x = 8$"),
              M1("substitute back"),
              A1("$\\log_2 y = 2$, so $y = 4$")],
             answer="$x = 8$, $y = 4$",
             solution=("Treat $\\log_2 x$ and $\\log_2 y$ as the two"
                       " unknowns. Adding the equations,"
                       "$$2\\log_2 x = 6 \\;\\Rightarrow\\;"
                       " \\log_2 x = 3 \\;\\Rightarrow\\; x = 2^{3} = 8.$$"
                       " Subtracting them instead,"
                       "$$2\\log_2 y = 4 \\;\\Rightarrow\\;"
                       " \\log_2 y = 2 \\;\\Rightarrow\\; y = 4.$$"
                       " Check: $\\log_2 8 + \\log_2 4 = 3 + 2 = 5$ and"
                       " $3 - 2 = 1$. Both values are positive, so both"
                       " logarithms are defined."),
             verify=["Eq(log(8, 2) + log(4, 2), 5)",
                     "Eq(log(8, 2) - log(4, 2), 1)",
                     "Eq(2**3, 8)", "Eq(2**2, 4)"]),
        part("b", "Solve $\\log_3 x + \\log_3 (x - 2) = 1$.", 4,
             [M1("combine into a single logarithm:"
                 " $\\log_3\\big(x(x - 2)\\big) = 1$"),
              A1("$x^{2} - 2x - 3 = 0$"),
              A1("$x = 3$ or $x = -1$"),
              R1("$x = -1$ is rejected because $\\log_3(-1)$ is undefined,"
                 " so $x = 3$")],
             answer="$x = 3$",
             solution=("Combine the logarithms with"
                       " $\\log a + \\log b = \\log(ab)$:"
                       "$$\\log_3\\big(x(x - 2)\\big) = 1"
                       " \\;\\Rightarrow\\; x(x - 2) = 3^{1} = 3.$$"
                       " Rearranging,"
                       "$$x^{2} - 2x - 3 = 0 \\;\\Rightarrow\\;"
                       " (x - 3)(x + 1) = 0,$$"
                       " so $x = 3$ or $x = -1$. The value $x = -1$ makes"
                       " both original logarithms undefined, so it is"
                       " extraneous and"
                       "$$x = 3$$"
                       " is the only solution. Checking:"
                       " $\\log_3 3 + \\log_3 1 = 1 + 0 = 1$."),
             verify=["Eq(3*(3 - 2), 3)",
                     "Eq(expand((x - 3)*(x + 1)), x**2 - 2*x - 3)",
                     "Eq(log(3, 3) + log(1, 3), 1)"]),
    ]))

# ── Q7 [8] calculus: integration by substitution ────────────────────────
assert simplify(diff(Rational(1, 8) * (x**2 + 1) ** 4, x)
                - x * (x**2 + 1) ** 3) == 0
assert integrate(x * (x**2 + 1) ** 3, (x, 0, 1)) == Rational(15, 8)
QS.append(question(
    "IB-AAHL-P1-T4-Q7", 7, "A", "calculus", "integration_substitution",
    parts=[
        part("a", "Use the substitution $u = x^{2} + 1$ to show that"
             " $\\displaystyle\\int x\\left(x^{2} + 1\\right)^{3}dx"
             " = \\frac{1}{8}\\left(x^{2} + 1\\right)^{4} + c$.", 4,
             [M1("$\\dfrac{du}{dx} = 2x$, so"
                 " $x\\,dx = \\tfrac{1}{2}du$"),
              A1("integral becomes"
                 " $\\tfrac{1}{2}\\displaystyle\\int u^{3}\\,du$"),
              A1("$= \\tfrac{1}{8}u^{4} + c$"),
              AG()],
             answer="$\\dfrac{1}{8}\\left(x^{2} + 1\\right)^{4} + c$"
                    " (given)",
             solution=("With $u = x^{2} + 1$ we get"
                       " $\\dfrac{du}{dx} = 2x$, so"
                       " $x\\,dx = \\tfrac{1}{2}\\,du$ and the integral"
                       " becomes"
                       "$$\\int x\\left(x^{2} + 1\\right)^{3}dx"
                       " = \\frac{1}{2}\\int u^{3}\\,du"
                       " = \\frac{1}{2}\\cdot\\frac{u^{4}}{4} + c"
                       " = \\frac{u^{4}}{8} + c.$$"
                       " Substituting back,"
                       "$$= \\frac{1}{8}\\left(x^{2} + 1\\right)^{4} + c.$$"
                       " Differentiating this result returns"
                       " $\\tfrac{1}{8}\\cdot4\\left(x^{2}+1\\right)^{3}"
                       "\\cdot 2x = x\\left(x^{2}+1\\right)^{3}$, which"
                       " confirms it."),
             verify=["Eq(simplify(diff(Rational(1,8)*(x**2 + 1)**4, x)"
                     " - x*(x**2 + 1)**3), 0)",
                     "Eq(diff(x**2 + 1, x), 2*x)"]),
        part("b", "Hence evaluate"
             " $\\displaystyle\\int_{0}^{1} x\\left(x^{2} + 1\\right)^{3}"
             "dx$.", 4,
             [M1("substitute the limits into"
                 " $\\tfrac{1}{8}\\left(x^{2} + 1\\right)^{4}$"),
              A1("$\\tfrac{1}{8}(2)^{4} = 2$"),
              A1("$\\tfrac{1}{8}(1)^{4} = \\tfrac{1}{8}$"),
              A1("$\\dfrac{15}{8}$")],
             answer="$\\dfrac{15}{8}$",
             solution=("Evaluate the antiderivative at the two limits:"
                       "$$\\left[\\frac{1}{8}\\left(x^{2} + 1\\right)^{4}"
                       "\\right]_{0}^{1}"
                       " = \\frac{1}{8}(2)^{4} - \\frac{1}{8}(1)^{4}"
                       " = 2 - \\frac{1}{8} = \\frac{15}{8}.$$"
                       " (Working in $u$ instead, the limits become"
                       " $u = 1$ and $u = 2$, giving the same"
                       " $\\tfrac{1}{8}\\left[u^{4}\\right]_{1}^{2}$ —"
                       " remember to change the limits if you do not"
                       " substitute back.)"),
             verify=["Eq(Rational(1,8)*2**4, 2)",
                     "Eq(2 - Rational(1,8), Rational(15,8))",
                     "Eq(integrate(x*(x**2 + 1)**3, (x, 0, 1)),"
                     " Rational(15,8))"]),
    ]))

# ── Q8 [20] geometry_trig: two INTERSECTING lines and their plane ───────
_A8 = Matrix([1, 2, 3])
_d1 = Matrix([2, -1, 1])
_B8 = Matrix([3, 1, 4])
_d2 = Matrix([1, 2, 2])
assert _A8 + 1 * _d1 == _B8 + 0 * _d2 == Matrix([3, 1, 4])
assert _d1.dot(_d2) == 2
assert _d1.cross(_d2) == Matrix([-4, -3, 5])
assert 4 * 3 + 3 * 1 - 5 * 4 + 5 == 0
_AD = Matrix([2, 0, 1]) - _A8
assert _AD.cross(_d1) == Matrix([-4, -5, 3])
assert simplify(sqrt(50) / sqrt(6)) == 5 * sqrt(3) / 3
QS.append(question(
    "IB-AAHL-P1-T4-Q8", 8, "B", "geometry_trig", "vectors_3d",
    contextIntro=("Two lines are given by"
                  " $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3"
                  " \\end{pmatrix} + s\\begin{pmatrix} 2 \\\\ -1 \\\\ 1"
                  " \\end{pmatrix}$ and"
                  " $L_2: \\mathbf{r} = \\begin{pmatrix} 3 \\\\ 1 \\\\ 4"
                  " \\end{pmatrix} + t\\begin{pmatrix} 1 \\\\ 2 \\\\ 2"
                  " \\end{pmatrix}$, where $s, t \\in \\mathbb{R}$."),
    parts=[
        part("a", "Show that $L_1$ and $L_2$ intersect, and find the"
             " coordinates of the point of intersection.", 5,
             [M1("equate the three coordinates"),
              A1("$1 + 2s = 3 + t$ and $2 - s = 1 + 2t$"),
              M1("solve the first two equations"),
              A1("$s = 1$, $t = 0$"),
              AG("both satisfy the third equation $3 + s = 4 + 2t$, so the"
                 " lines meet at $(3, 1, 4)$")],
             answer="the lines meet at $(3, 1, 4)$",
             solution=("Set the two position vectors equal, coordinate by"
                       " coordinate:"
                       "$$1 + 2s = 3 + t, \\qquad 2 - s = 1 + 2t,"
                       " \\qquad 3 + s = 4 + 2t.$$"
                       " From the first equation $t = 2s - 2$."
                       " Substituting into the second,"
                       "$$2 - s = 1 + 2(2s - 2) = 4s - 3"
                       " \\;\\Rightarrow\\; 5 = 5s \\;\\Rightarrow\\;"
                       " s = 1,$$"
                       " and then $t = 0$."
                       " The THIRD equation must now be checked, since two"
                       " equations can always be solved but three need not"
                       " agree: $3 + 1 = 4$ and $4 + 2(0) = 4$, so it"
                       " holds. The lines therefore intersect, at"
                       "$$\\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}"
                       " + 1\\begin{pmatrix} 2 \\\\ -1 \\\\ 1"
                       " \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 1 \\\\ 4"
                       " \\end{pmatrix},$$"
                       " that is at the point $(3, 1, 4)$."),
             verify=["Eq(Matrix([1,2,3]) + Matrix([2,-1,1]),"
                     " Matrix([3,1,4]))",
                     "Eq(Matrix([3,1,4]) + 0*Matrix([1,2,2]),"
                     " Matrix([3,1,4]))",
                     "Eq(3 + 1, 4 + 2*0)"]),
        part("b", "Find the exact value of $\\cos\\theta$, where $\\theta$"
             " is the acute angle between the two lines.", 4,
             [M1("$\\cos\\theta = \\dfrac{|\\mathbf{d}_1 \\cdot"
                 " \\mathbf{d}_2|}{|\\mathbf{d}_1||\\mathbf{d}_2|}$"),
              A1("$\\mathbf{d}_1 \\cdot \\mathbf{d}_2 = 2$"),
              A1("$|\\mathbf{d}_1| = \\sqrt{6}$,"
                 " $|\\mathbf{d}_2| = 3$"),
              A1("$\\cos\\theta = \\dfrac{\\sqrt{6}}{9}$")],
             answer="$\\cos\\theta = \\dfrac{\\sqrt{6}}{9}$",
             solution=("The angle between two lines is the angle between"
                       " their direction vectors, taken acute:"
                       "$$\\cos\\theta = \\frac{|\\mathbf{d}_1 \\cdot"
                       " \\mathbf{d}_2|}{|\\mathbf{d}_1|\\,"
                       "|\\mathbf{d}_2|}.$$"
                       " Here"
                       "$$\\mathbf{d}_1 \\cdot \\mathbf{d}_2"
                       " = 2(1) + (-1)(2) + 1(2) = 2,$$"
                       "$$|\\mathbf{d}_1| = \\sqrt{4 + 1 + 1}"
                       " = \\sqrt{6}, \\qquad |\\mathbf{d}_2|"
                       " = \\sqrt{1 + 4 + 4} = 3.$$"
                       " Hence"
                       "$$\\cos\\theta = \\frac{2}{3\\sqrt{6}}"
                       " = \\frac{2\\sqrt{6}}{18}"
                       " = \\frac{\\sqrt{6}}{9}.$$"),
             verify=["Eq(Matrix([2,-1,1]).dot(Matrix([1,2,2])), 2)",
                     "Eq(sqrt(4 + 1 + 1), sqrt(6))",
                     "Eq(sqrt(1 + 4 + 4), 3)",
                     "Eq(simplify(2/(3*sqrt(6))), sqrt(6)/9)"]),
        part("c", "Find a Cartesian equation of the plane that contains"
             " both lines.", 5,
             [M1("a normal is"
                 " $\\mathbf{d}_1 \\times \\mathbf{d}_2$"),
              M1("evaluate the cross product"),
              A1("$\\begin{pmatrix} -4 \\\\ -3 \\\\ 5 \\end{pmatrix}$"),
              M1("use a point on the plane, e.g. $(1, 2, 3)$"),
              A1("$4x + 3y - 5z + 5 = 0$")],
             answer="$4x + 3y - 5z + 5 = 0$",
             solution=("Because the lines intersect, they span a unique"
                       " plane, and a normal to that plane is perpendicular"
                       " to both directions:"
                       "$$\\mathbf{n} = \\mathbf{d}_1 \\times"
                       " \\mathbf{d}_2 = \\begin{pmatrix}"
                       " (-1)(2) - (1)(2) \\\\ (1)(1) - (2)(2) \\\\"
                       " (2)(2) - (-1)(1) \\end{pmatrix}"
                       " = \\begin{pmatrix} -4 \\\\ -3 \\\\ 5"
                       " \\end{pmatrix}.$$"
                       " Using the point $(1, 2, 3)$ from $L_1$,"
                       "$$-4(x - 1) - 3(y - 2) + 5(z - 3) = 0.$$"
                       " Expanding and multiplying by $-1$,"
                       "$$4x + 3y - 5z + 5 = 0.$$"
                       " Check with the intersection point $(3, 1, 4)$:"
                       " $12 + 3 - 20 + 5 = 0$."),
             verify=["Eq(Matrix([2,-1,1]).cross(Matrix([1,2,2])),"
                     " Matrix([-4,-3,5]))",
                     "Eq(4*1 + 3*2 - 5*3 + 5, 0)",
                     "Eq(4*3 + 3*1 - 5*4 + 5, 0)"]),
        part("d", "Find the exact perpendicular distance from the point"
             " $D(2, 0, 1)$ to the line $L_1$.", 6,
             [M1("use $\\dfrac{\\left|\\overrightarrow{AD} \\times"
                 " \\mathbf{d}_1\\right|}{|\\mathbf{d}_1|}$ with"
                 " $A(1, 2, 3)$"),
              A1("$\\overrightarrow{AD} = \\begin{pmatrix} 1 \\\\ -2"
                 " \\\\ -2 \\end{pmatrix}$"),
              M1("evaluate the cross product"),
              A1("$\\begin{pmatrix} -4 \\\\ -5 \\\\ 3 \\end{pmatrix}$"),
              A1("magnitude $5\\sqrt{2}$"),
              A1("$\\dfrac{5\\sqrt{3}}{3}$")],
             answer="$\\dfrac{5\\sqrt{3}}{3}$",
             solution=("Take the known point $A(1, 2, 3)$ on $L_1$. The"
                       " perpendicular distance from $D$ to the line is"
                       "$$\\frac{\\left|\\overrightarrow{AD} \\times"
                       " \\mathbf{d}_1\\right|}{|\\mathbf{d}_1|},$$"
                       " which measures the component of"
                       " $\\overrightarrow{AD}$ across the line rather than"
                       " along it. Here"
                       "$$\\overrightarrow{AD} = \\begin{pmatrix} 2 \\\\ 0"
                       " \\\\ 1 \\end{pmatrix} - \\begin{pmatrix} 1 \\\\ 2"
                       " \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\"
                       " -2 \\\\ -2 \\end{pmatrix},$$"
                       "$$\\overrightarrow{AD} \\times \\mathbf{d}_1"
                       " = \\begin{pmatrix} (-2)(1) - (-2)(-1) \\\\"
                       " (-2)(2) - (1)(1) \\\\ (1)(-1) - (-2)(2)"
                       " \\end{pmatrix} = \\begin{pmatrix} -4 \\\\ -5"
                       " \\\\ 3 \\end{pmatrix}.$$"
                       " Its magnitude is"
                       " $\\sqrt{16 + 25 + 9} = \\sqrt{50} = 5\\sqrt{2}$,"
                       " so the distance is"
                       "$$\\frac{5\\sqrt{2}}{\\sqrt{6}}"
                       " = \\frac{5}{\\sqrt{3}} = \\frac{5\\sqrt{3}}{3}.$$"),
             verify=["Eq(Matrix([2,0,1]) - Matrix([1,2,3]),"
                     " Matrix([1,-2,-2]))",
                     "Eq(Matrix([1,-2,-2]).cross(Matrix([2,-1,1])),"
                     " Matrix([-4,-5,3]))",
                     "Eq(simplify(sqrt(16 + 25 + 9)), 5*sqrt(2))",
                     "Eq(simplify(5*sqrt(2)/sqrt(6)), 5*sqrt(3)/3)"]),
    ]))

# ── Q9 [21] calculus: the full cycle on f(x) = ln(x)/x ─────────────────
assert simplify(diff(log(x) / x, x) - (1 - log(x)) / x**2) == 0
assert simplify(diff(log(x) / x, x, 2) - (2 * log(x) - 3) / x**3) == 0
assert simplify(integrate(log(x) / x, (x, 1, E)) - Rational(1, 2)) == 0
assert simplify(integrate((log(x) / x) ** 2, (x, 1, E)) - (2 - 5 * exp(-1))) == 0
QS.append(question(
    "IB-AAHL-P1-T4-Q9", 9, "B", "calculus", "differentiation_applications",
    contextIntro=("The function $f$ is defined by"
                  " $f(x) = \\dfrac{\\ln x}{x}$ for $x > 0$. The diagram"
                  " shows the region $R$ bounded by the curve $y = f(x)$,"
                  " the $x$-axis and the line $x = \\mathrm{e}$."),
    figure=None,
    parts=[
        part("a", "Show that $f'(x) = \\dfrac{1 - \\ln x}{x^{2}}$.", 3,
             [M1("quotient rule with $u = \\ln x$, $v = x$"),
              A1("$\\dfrac{x\\cdot\\frac{1}{x} - \\ln x \\cdot 1}"
                 "{x^{2}}$"),
              AG()],
             answer="$f'(x) = \\dfrac{1 - \\ln x}{x^{2}}$ (given)",
             solution=("Apply the quotient rule with $u = \\ln x$ and"
                       " $v = x$, so $u' = \\dfrac{1}{x}$ and $v' = 1$:"
                       "$$f'(x) = \\frac{v u' - u v'}{v^{2}}"
                       " = \\frac{x \\cdot \\frac{1}{x} - \\ln x \\cdot 1}"
                       "{x^{2}} = \\frac{1 - \\ln x}{x^{2}}.$$"),
             verify=["Eq(simplify(diff(log(x)/x, x)"
                     " - (1 - log(x))/x**2), 0)",
                     "Eq(diff(log(x), x), 1/x)"]),
        part("b", "Find the coordinates of the stationary point of the"
             " curve and justify that it is a maximum.", 4,
             [M1("set $f'(x) = 0$, so $\\ln x = 1$"),
              A1("$\\left(\\mathrm{e}, \\dfrac{1}{\\mathrm{e}}\\right)$"),
              M1("find"
                 " $f''(x) = \\dfrac{2\\ln x - 3}{x^{3}}$"),
              R1("$f''(\\mathrm{e}) = -\\dfrac{1}{\\mathrm{e}^{3}} < 0$,"
                 " so it is a maximum")],
             answer="$\\left(\\mathrm{e}, \\dfrac{1}{\\mathrm{e}}\\right)$,"
                    " a local maximum",
             solution=("A fraction is zero when its numerator is zero, so"
                       "$$1 - \\ln x = 0 \\;\\Rightarrow\\; \\ln x = 1"
                       " \\;\\Rightarrow\\; x = \\mathrm{e},$$"
                       " and there"
                       "$$f(\\mathrm{e}) = \\frac{\\ln \\mathrm{e}}"
                       "{\\mathrm{e}} = \\frac{1}{\\mathrm{e}}.$$"
                       " Differentiating again,"
                       "$$f''(x) = \\frac{2\\ln x - 3}{x^{3}},$$"
                       " so"
                       "$$f''(\\mathrm{e}) = \\frac{2 - 3}"
                       "{\\mathrm{e}^{3}} = -\\frac{1}{\\mathrm{e}^{3}}"
                       " < 0.$$"
                       " The curve is concave down there, so"
                       " $\\left(\\mathrm{e}, \\dfrac{1}{\\mathrm{e}}"
                       "\\right)$ is a local maximum."),
             verify=["Eq(simplify((1 - log(E))/E**2), 0)",
                     "Eq(simplify(log(E)/E), 1/E)",
                     "Eq(simplify(diff(log(x)/x, x, 2)"
                     " - (2*log(x) - 3)/x**3), 0)",
                     "(2 - 3)/E**3 < 0"]),
        part("c", "Find the exact coordinates of the point of inflexion of"
             " the curve.", 4,
             [M1("set $f''(x) = 0$: $2\\ln x = 3$"),
              A1("$x = \\mathrm{e}^{3/2}$"),
              R1("$f''$ changes sign there"),
              A1("$\\left(\\mathrm{e}^{3/2},"
                 " \\dfrac{3}{2\\mathrm{e}^{3/2}}\\right)$")],
             answer="$\\left(\\mathrm{e}^{3/2},"
                    " \\dfrac{3}{2\\mathrm{e}^{3/2}}\\right)$",
             solution=("Set the second derivative to zero:"
                       "$$2\\ln x - 3 = 0 \\;\\Rightarrow\\;"
                       " \\ln x = \\frac{3}{2} \\;\\Rightarrow\\;"
                       " x = \\mathrm{e}^{3/2}.$$"
                       " Because $x^{3} > 0$, the sign of $f''$ is the sign"
                       " of $2\\ln x - 3$, which is negative for"
                       " $x < \\mathrm{e}^{3/2}$ and positive after — a"
                       " genuine change of concavity. The $y$-coordinate is"
                       "$$f\\!\\left(\\mathrm{e}^{3/2}\\right)"
                       " = \\frac{3/2}{\\mathrm{e}^{3/2}}"
                       " = \\frac{3}{2\\mathrm{e}^{3/2}}.$$"),
             verify=["Eq(simplify(2*log(E**Rational(3,2)) - 3), 0)",
                     "Eq(simplify(log(E**Rational(3,2))"
                     "/E**Rational(3,2) - Rational(3,2)"
                     "/E**Rational(3,2)), 0)"]),
        part("d", "Find the exact area of the region $R$.", 5,
             [M1("recognise the form"
                 " $\\displaystyle\\int \\frac{\\ln x}{x}dx$ with"
                 " $u = \\ln x$"),
              A1("$= \\dfrac{(\\ln x)^{2}}{2} + c$"),
              M1("evaluate between $1$ and $\\mathrm{e}$"),
              A1("$\\dfrac{1}{2} - 0$"),
              A1("area $= \\dfrac{1}{2}$")],
             answer="$\\dfrac{1}{2}$",
             solution=("The integrand is a derivative times a function of"
                       " itself: with $u = \\ln x$ we get"
                       " $du = \\dfrac{1}{x}dx$, so"
                       "$$\\int \\frac{\\ln x}{x}\\,dx"
                       " = \\int u\\,du = \\frac{u^{2}}{2} + c"
                       " = \\frac{(\\ln x)^{2}}{2} + c.$$"
                       " The curve crosses the $x$-axis at $x = 1$ (where"
                       " $\\ln 1 = 0$), so the region runs from $1$ to"
                       " $\\mathrm{e}$:"
                       "$$A = \\left[\\frac{(\\ln x)^{2}}{2}"
                       "\\right]_{1}^{\\mathrm{e}}"
                       " = \\frac{1}{2} - 0 = \\frac{1}{2}.$$"),
             verify=["Eq(simplify(diff(log(x)**2/2, x) - log(x)/x), 0)",
                     "Eq(simplify(integrate(log(x)/x, (x, 1, E))),"
                     " Rational(1,2))",
                     "Eq(log(1), 0)"]),
        part("e", "The region $R$ is rotated through $2\\pi$ about the"
             " $x$-axis. Find the exact volume of the solid formed.", 5,
             [M1("$V = \\pi\\displaystyle\\int_{1}^{\\mathrm{e}}"
                 " \\frac{(\\ln x)^{2}}{x^{2}}dx$"),
              M1("integrate by parts twice"),
              A1("antiderivative"
                 " $-\\dfrac{(\\ln x)^{2} + 2\\ln x + 2}{x}$"),
              A1("definite value"
                 " $2 - \\dfrac{5}{\\mathrm{e}}$"),
              A1("$V = \\pi\\left(2"
                 " - \\dfrac{5}{\\mathrm{e}}\\right)$")],
             answer="$V = \\pi\\left(2"
                    " - \\dfrac{5}{\\mathrm{e}}\\right)$",
             solution=("Rotating about the $x$-axis,"
                       "$$V = \\pi\\int_{1}^{\\mathrm{e}}"
                       "\\left(\\frac{\\ln x}{x}\\right)^{2}dx"
                       " = \\pi\\int_{1}^{\\mathrm{e}}"
                       " (\\ln x)^{2}x^{-2}\\,dx.$$"
                       " Integrating by parts with $u = (\\ln x)^{2}$ and"
                       " $dv = x^{-2}dx$, then by parts once more on the"
                       " remaining $\\int \\ln x \\cdot x^{-2}dx$, gives"
                       "$$\\int (\\ln x)^{2}x^{-2}dx"
                       " = -\\frac{(\\ln x)^{2} + 2\\ln x + 2}{x} + c.$$"
                       " At $x = \\mathrm{e}$ the bracket is"
                       " $1 + 2 + 2 = 5$ and at $x = 1$ it is $2$, so"
                       "$$\\int_{1}^{\\mathrm{e}} (\\ln x)^{2}x^{-2}dx"
                       " = -\\frac{5}{\\mathrm{e}} + 2.$$"
                       " Therefore"
                       "$$V = \\pi\\left(2 - \\frac{5}{\\mathrm{e}}"
                       "\\right).$$"
                       " Since $\\mathrm{e} > 2.5$ this is positive, as a"
                       " volume must be."),
             verify=["Eq(simplify(diff(-(log(x)**2 + 2*log(x) + 2)/x, x)"
                     " - log(x)**2/x**2), 0)",
                     "Eq(simplify(integrate((log(x)/x)**2, (x, 1, E))"
                     " - (2 - 5/E)), 0)",
                     "2 - 5/E > 0"]),
    ]))

# ── Q10 [17] stats_probability: a continuous random variable ────────────
assert integrate(x * (4 - x), (x, 0, 4)) == Rational(32, 3)
assert Rational(3, 32) * integrate(x**2 * (4 - x), (x, 0, 4)) == 2
assert (Rational(3, 32) * integrate(x**3 * (4 - x), (x, 0, 4))
        - 2**2) == Rational(4, 5)
assert Rational(3, 32) * integrate(x * (4 - x), (x, 1, 3)) == Rational(11, 16)
QS.append(question(
    "IB-AAHL-P1-T4-Q10", 10, "B", "stats_probability",
    "continuous_random_variables",
    contextIntro=("A continuous random variable $X$ has probability"
                  " density function"
                  " $f(x) = kx(4 - x)$ for $0 \\le x \\le 4$, and"
                  " $f(x) = 0$ otherwise, where $k$ is a constant."),
    parts=[
        part("a", "Show that $k = \\dfrac{3}{32}$.", 4,
             [M1("a density integrates to $1$ over its support"),
              A1("$\\displaystyle\\int_{0}^{4} x(4 - x)\\,dx"
                 " = \\left[2x^{2} - \\frac{x^{3}}{3}\\right]_{0}^{4}$"),
              A1("$= \\dfrac{32}{3}$"),
              AG()],
             answer="$k = \\dfrac{3}{32}$ (given)",
             solution=("Every probability density integrates to $1$ over"
                       " its support:"
                       "$$\\int_{0}^{4} kx(4 - x)\\,dx = 1.$$"
                       " Compute the integral first:"
                       "$$\\int_{0}^{4}\\left(4x - x^{2}\\right)dx"
                       " = \\left[2x^{2} - \\frac{x^{3}}{3}"
                       "\\right]_{0}^{4} = 32 - \\frac{64}{3}"
                       " = \\frac{32}{3}.$$"
                       " Hence $k \\cdot \\dfrac{32}{3} = 1$, giving"
                       " $k = \\dfrac{3}{32}$. Note $f(x) \\ge 0$ on"
                       " $[0, 4]$, as a density must be."),
             verify=["Eq(integrate(x*(4 - x), (x, 0, 4)), Rational(32,3))",
                     "Eq(Rational(3,32)*Rational(32,3), 1)"]),
        part("b", "Find $\\mathrm{E}(X)$.", 4,
             [M1("$\\mathrm{E}(X)"
                 " = \\displaystyle\\int_{0}^{4} x f(x)\\,dx$"),
              A1("$\\dfrac{3}{32}\\displaystyle\\int_{0}^{4}"
                 "\\left(4x^{2} - x^{3}\\right)dx$"),
              A1("$\\dfrac{3}{32} \\cdot \\dfrac{64}{3}$"),
              A1("$\\mathrm{E}(X) = 2$")],
             answer="$\\mathrm{E}(X) = 2$",
             solution=("The mean of a continuous variable is"
                       "$$\\mathrm{E}(X) = \\int_{0}^{4} x f(x)\\,dx"
                       " = \\frac{3}{32}\\int_{0}^{4}"
                       "\\left(4x^{2} - x^{3}\\right)dx.$$"
                       " Evaluating,"
                       "$$\\int_{0}^{4}\\left(4x^{2} - x^{3}\\right)dx"
                       " = \\left[\\frac{4x^{3}}{3} - \\frac{x^{4}}{4}"
                       "\\right]_{0}^{4} = \\frac{256}{3} - 64"
                       " = \\frac{64}{3},$$"
                       " so"
                       "$$\\mathrm{E}(X) = \\frac{3}{32}\\cdot"
                       "\\frac{64}{3} = 2.$$"
                       " This is no surprise: the density is symmetric"
                       " about $x = 2$."),
             verify=["Eq(integrate(4*x**2 - x**3, (x, 0, 4)),"
                     " Rational(64,3))",
                     "Eq(Rational(3,32)*Rational(64,3), 2)"]),
        part("c", "Find $\\mathrm{Var}(X)$.", 5,
             [M1("$\\mathrm{Var}(X) = \\mathrm{E}(X^{2})"
                 " - \\left(\\mathrm{E}(X)\\right)^{2}$"),
              M1("$\\mathrm{E}(X^{2})"
                 " = \\dfrac{3}{32}\\displaystyle\\int_{0}^{4}"
                 "\\left(4x^{3} - x^{4}\\right)dx$"),
              A1("$\\displaystyle\\int_{0}^{4}\\left(4x^{3} - x^{4}"
                 "\\right)dx = \\dfrac{256}{5}$"),
              A1("$\\mathrm{E}(X^{2}) = \\dfrac{24}{5}$"),
              A1("$\\mathrm{Var}(X) = \\dfrac{4}{5}$")],
             answer="$\\mathrm{Var}(X) = \\dfrac{4}{5}$",
             solution=("First find the second moment:"
                       "$$\\mathrm{E}(X^{2}) = \\frac{3}{32}"
                       "\\int_{0}^{4}\\left(4x^{3} - x^{4}\\right)dx"
                       " = \\frac{3}{32}\\left[x^{4} - \\frac{x^{5}}{5}"
                       "\\right]_{0}^{4}.$$"
                       " The bracket is $256 - \\dfrac{1024}{5}"
                       " = \\dfrac{256}{5}$, so"
                       "$$\\mathrm{E}(X^{2}) = \\frac{3}{32}\\cdot"
                       "\\frac{256}{5} = \\frac{24}{5}.$$"
                       " Then"
                       "$$\\mathrm{Var}(X) = \\mathrm{E}(X^{2})"
                       " - \\left(\\mathrm{E}(X)\\right)^{2}"
                       " = \\frac{24}{5} - 4 = \\frac{4}{5}.$$"),
             verify=["Eq(integrate(4*x**3 - x**4, (x, 0, 4)),"
                     " Rational(256,5))",
                     "Eq(Rational(3,32)*Rational(256,5), Rational(24,5))",
                     "Eq(Rational(24,5) - 4, Rational(4,5))"]),
        part("d", "Find $P(1 \\le X \\le 3)$.", 4,
             [M1("integrate the density between $1$ and $3$"),
              A1("$\\dfrac{3}{32}\\left[2x^{2} - \\dfrac{x^{3}}{3}"
                 "\\right]_{1}^{3}$"),
              A1("$\\dfrac{3}{32} \\cdot \\dfrac{22}{3}$"),
              A1("$\\dfrac{11}{16}$")],
             answer="$\\dfrac{11}{16}$",
             solution=("A probability over an interval is the area under"
                       " the density there:"
                       "$$P(1 \\le X \\le 3) = \\frac{3}{32}"
                       "\\int_{1}^{3}\\left(4x - x^{2}\\right)dx"
                       " = \\frac{3}{32}\\left[2x^{2} - \\frac{x^{3}}{3}"
                       "\\right]_{1}^{3}.$$"
                       " At $x = 3$ the bracket is $18 - 9 = 9$; at"
                       " $x = 1$ it is $2 - \\dfrac{1}{3}"
                       " = \\dfrac{5}{3}$. The difference is"
                       " $\\dfrac{22}{3}$, so"
                       "$$P(1 \\le X \\le 3) = \\frac{3}{32}\\cdot"
                       "\\frac{22}{3} = \\frac{22}{32}"
                       " = \\frac{11}{16}.$$"
                       " Just over two thirds of the distribution lies in"
                       " the middle half of the range, which fits the"
                       " density's hump at $x = 2$."),
             verify=["Eq(integrate(4*x - x**2, (x, 1, 3)),"
                     " Rational(22,3))",
                     "Eq(Rational(3,32)*Rational(22,3), Rational(11,16))"]),
    ]))

META = {"course": "aa", "level": "hl", "paper": 1, "testId": "ib-hl-practice-4",
        "label": "AA HL Practice Paper 1", "timeMinutes": 120,
        "totalMarks": 110, "calculator": False}

if __name__ == "__main__":
    QS[8]["figure"] = png("ib-aahl-p1-t4-q9.png",
                          "Region R bounded by the curve y = ln(x)/x, the "
                          "x-axis and the line x = e")
    write_paper(META, QS, "data/ib/aa-hl/ib-hl-practice-4/paper1.json")
