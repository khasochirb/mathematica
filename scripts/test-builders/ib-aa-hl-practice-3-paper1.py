"""AA HL Practice Paper 1 (ib-hl-practice-3) — 120 min, 110 marks, NO calculator.

Blueprint (topic x marks):
    Section A (51): Q1 number_algebra 5  | Q2 functions 8
                    Q3 geometry_trig 8   | Q4 stats_probability 6
                    Q5 calculus 7        | Q6 stats_probability 9
                    Q7 functions 8
    Section B (59): Q8 geometry_trig 20  | Q9 calculus 21
                    Q10 number_algebra 18
    Paper totals: number_algebra 23 | functions 16 | geometry_trig 28 |
                  stats_probability 15 | calculus 28 = 110.

HL-only content, fresh versus HL Sets 1 and 2: a geometric series pinned
by its sum to infinity, a Mobius-type rational function inverted with its
domain, the identity sin 2t / (1 + cos 2t) = tan t used as a "hence"
lever, Bayes from a two-machine production line, implicit differentiation
with a tangent, an exact discrete distribution P(X = x) = kx, a cubic
factorised and its sign set solved, a line meeting a PLANE (angle via the
normal, perpendicular distance, triangle area from a cross product),
x e^(-x) taken through the full calculus cycle including a volume of
revolution, and complex numbers in modulus-argument form with the cube
roots of 8i plus a proof by induction. Everything exact.
Figure: Q9 (region under x e^(-x) from 0 to 1).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, I, Matrix, simplify, solve,  # noqa: F401,E402
                   expand, factor, diff, integrate, atan, sin, cos, tan,
                   binomial, factorial, symbols, im, re, arg, Abs, log, exp,
                   E, together, cancel, Sum, oo, limit)

x, y, t, k, n, m, r = symbols("x y t k n m r")


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [5] number_algebra: geometric series from its sum to infinity ─────
assert solve(Eq(12 / (1 - x), 20), x) == [Rational(2, 5)]
assert 12 + Rational(24, 5) + Rational(48, 25) == Rational(468, 25)
QS.append(question(
    "IB-AAHL-P1-T3-Q1", 1, "A", "number_algebra", "geometric_sequences",
    contextIntro=("The first term of an infinite geometric sequence is $12$,"
                  " and the sum of all the terms of the sequence is $20$."),
    parts=[
        part("a", "Show that the common ratio of the sequence is"
             " $\\dfrac{2}{5}$.", 3,
             [M1("use $S_\\infty = \\dfrac{u_1}{1 - r}$: $\\dfrac{12}{1 - r}"
                 " = 20$"),
              A1("$1 - r = \\dfrac{12}{20} = \\dfrac{3}{5}$"),
              AG()],
             answer="$r = \\dfrac{2}{5}$ (given)",
             solution=("An infinite geometric series converges to"
                       " $S_\\infty = \\dfrac{u_1}{1 - r}$, so"
                       "$$\\frac{12}{1 - r} = 20 \\;\\Rightarrow\\;"
                       " 1 - r = \\frac{12}{20} = \\frac{3}{5}.$$"
                       " Hence $r = 1 - \\dfrac{3}{5} = \\dfrac{2}{5}$."
                       " Note $|r| < 1$, which is exactly the condition"
                       " that makes the infinite sum exist."),
             verify=["Eq(12/(1 - Rational(2,5)), 20)",
                     "Eq(1 - Rational(3,5), Rational(2,5))",
                     "Abs(Rational(2,5)) < 1"]),
        part("b", "Find the sum of the first three terms of the sequence,"
             " giving your answer as a fraction in its lowest terms.", 2,
             [M1("$12 + 12\\left(\\tfrac{2}{5}\\right) +"
                 " 12\\left(\\tfrac{2}{5}\\right)^2$"),
              A1("$\\dfrac{468}{25}$")],
             answer="$\\dfrac{468}{25}$",
             solution=("The first three terms are $12$, $\\dfrac{24}{5}$ and"
                       " $\\dfrac{48}{25}$. Writing them over the common"
                       " denominator $25$,"
                       "$$S_3 = \\frac{300 + 120 + 48}{25}"
                       " = \\frac{468}{25}.$$"
                       " (Equivalently $S_3 = 20\\left(1 -"
                       " \\left(\\tfrac{2}{5}\\right)^3\\right)"
                       " = 20 \\cdot \\tfrac{117}{125}$.)"),
             verify=["Eq(12 + Rational(24,5) + Rational(48,25),"
                     " Rational(468,25))",
                     "Eq(20*(1 - Rational(2,5)**3), Rational(468,25))"]),
    ]))

# ── Q2 [8] functions: rational function, inverse and its domain ──────────
assert simplify(((2 * x - 3) / (x + 1)).subs(x, (x + 3) / (2 - x)) - x) == 0
QS.append(question(
    "IB-AAHL-P1-T3-Q2", 2, "A", "functions", "inverse_functions",
    contextIntro=("The function $f$ is defined by"
                  " $f(x) = \\dfrac{2x - 3}{x + 1}$, for $x \\in \\mathbb{R}"
                  ",\\ x \\neq -1$."),
    parts=[
        part("a", "Write down the equations of the vertical and the"
             " horizontal asymptote of the graph of $f$.", 2,
             [A1("$x = -1$"), A1("$y = 2$")],
             answer="$x = -1$ and $y = 2$",
             solution=("The vertical asymptote occurs where the denominator"
                       " vanishes: $x + 1 = 0$, so $x = -1$."
                       " For the horizontal asymptote, divide numerator and"
                       " denominator by $x$:"
                       "$$f(x) = \\frac{2 - \\frac{3}{x}}"
                       "{1 + \\frac{1}{x}} \\to \\frac{2}{1} = 2$$"
                       " as $x \\to \\pm\\infty$, so $y = 2$."),
             verify=["Eq(-1 + 1, 0)",
                     "Eq(limit((2*x - 3)/(x + 1), x, oo), 2)"]),
        part("b", "Find an expression for $f^{-1}(x)$.", 4,
             [M1("write $y = \\dfrac{2x - 3}{x + 1}$ and clear the"
                 " denominator"),
              A1("$xy + y = 2x - 3$"),
              M1("collect the $x$ terms: $x(y - 2) = -y - 3$"),
              A1("$f^{-1}(x) = \\dfrac{x + 3}{2 - x}$")],
             answer="$f^{-1}(x) = \\dfrac{x + 3}{2 - x}$",
             solution=("Set $y = \\dfrac{2x - 3}{x + 1}$ and multiply"
                       " through by $x + 1$:"
                       "$$y(x + 1) = 2x - 3 \\;\\Rightarrow\\;"
                       " xy + y = 2x - 3.$$"
                       " Gather every $x$ on one side:"
                       "$$xy - 2x = -3 - y \\;\\Rightarrow\\;"
                       " x(y - 2) = -(y + 3).$$"
                       " Dividing and swapping the roles of the letters,"
                       "$$f^{-1}(x) = \\frac{-(x + 3)}{x - 2}"
                       " = \\frac{x + 3}{2 - x}.$$"
                       " A quick check: $f(0) = -3$ and"
                       " $f^{-1}(-3) = \\dfrac{0}{5} = 0$."),
             verify=["Eq(simplify(((2*x - 3)/(x + 1)).subs(x, (x + 3)/(2 - x))"
                     " - x), 0)",
                     "Eq((2*0 - 3)/(0 + 1), -3)",
                     "Eq((-3 + 3)/(2 - (-3)), 0)"]),
        part("c", "State the domain of $f^{-1}$.", 2,
             [R1("the domain of $f^{-1}$ is the range of $f$"),
              A1("$x \\in \\mathbb{R},\\ x \\neq 2$")],
             answer="$x \\in \\mathbb{R},\\ x \\neq 2$",
             solution=("The domain of an inverse is the range of the"
                       " original function. Because $y = 2$ is a horizontal"
                       " asymptote of $f$ and the value $2$ is never"
                       " attained, the range of $f$ is"
                       " $\\mathbb{R} \\setminus \\{2\\}$."
                       " This matches the formula: $f^{-1}(x) ="
                       " \\dfrac{x + 3}{2 - x}$ is undefined exactly at"
                       " $x = 2$."),
             verify=["Eq(2 - 2, 0)",
                     "Ne(-3, 2)",
                     "Eq(limit((2*x - 3)/(x + 1), x, oo), 2)"]),
    ]))

# ── Q3 [8] geometry_trig: a double-angle identity used as a lever ────────
assert simplify(sin(2 * t) / (1 + cos(2 * t)) - tan(t)) == 0
assert solve(Eq(tan(t), sqrt(3)), t)[0] == pi / 3
QS.append(question(
    "IB-AAHL-P1-T3-Q3", 3, "A", "geometry_trig", "trig_identities",
    parts=[
        part("a", "Show that $\\dfrac{\\sin 2\\theta}{1 + \\cos 2\\theta}"
             " = \\tan\\theta$ for all $\\theta$ for which both sides are"
             " defined.", 3,
             [M1("use $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$ and"
                 " $\\cos 2\\theta = 2\\cos^2\\theta - 1$"),
              A1("$\\dfrac{2\\sin\\theta\\cos\\theta}{2\\cos^2\\theta}$"),
              AG()],
             answer="identity (given)",
             solution=("Replace both double angles. Using"
                       " $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$ and the"
                       " form $\\cos 2\\theta = 2\\cos^2\\theta - 1$,"
                       "$$\\frac{\\sin 2\\theta}{1 + \\cos 2\\theta}"
                       " = \\frac{2\\sin\\theta\\cos\\theta}"
                       "{1 + 2\\cos^2\\theta - 1}"
                       " = \\frac{2\\sin\\theta\\cos\\theta}"
                       "{2\\cos^2\\theta}.$$"
                       " Cancelling the factor $2\\cos\\theta$ (valid"
                       " wherever $\\cos\\theta \\neq 0$, which is exactly"
                       " where the left side is defined) leaves"
                       " $\\dfrac{\\sin\\theta}{\\cos\\theta}"
                       " = \\tan\\theta$."),
             verify=["Eq(simplify(sin(2*t)/(1 + cos(2*t)) - tan(t)), 0)",
                     "Eq(simplify(cos(2*t) - (2*cos(t)**2 - 1)), 0)"]),
        part("b", "Hence solve $\\dfrac{\\sin 2\\theta}{1 + \\cos 2\\theta}"
             " = \\sqrt{3}$ for $0 \\le \\theta < 2\\pi$.", 5,
             [M1("use part (a) to reduce the equation to"
                 " $\\tan\\theta = \\sqrt{3}$"),
              A1("$\\theta = \\dfrac{\\pi}{3}$"),
              M1("tangent has period $\\pi$, so add $\\pi$"),
              A1("$\\theta = \\dfrac{4\\pi}{3}$"),
              R1("both values satisfy $\\cos\\theta \\neq 0$, so neither is"
                 " excluded")],
             answer="$\\theta = \\dfrac{\\pi}{3}$ or"
                    " $\\theta = \\dfrac{4\\pi}{3}$",
             solution=("By part (a) the equation becomes"
                       "$$\\tan\\theta = \\sqrt{3}.$$"
                       " The first-quadrant solution is"
                       " $\\theta = \\dfrac{\\pi}{3}$, and since the tangent"
                       " function has period $\\pi$ the next solution in"
                       " range is"
                       "$$\\theta = \\frac{\\pi}{3} + \\pi"
                       " = \\frac{4\\pi}{3}.$$"
                       " Both values have $\\cos\\theta \\neq 0$, so the"
                       " original quotient is defined at each, and no"
                       " further solutions lie in $[0, 2\\pi)$."),
             verify=["Eq(tan(pi/3), sqrt(3))",
                     "Eq(tan(4*pi/3), sqrt(3))",
                     "Ne(cos(pi/3), 0)", "Ne(cos(4*pi/3), 0)",
                     "Eq(simplify(sin(2*pi/3)/(1 + cos(2*pi/3))), sqrt(3))"]),
    ]))

# ── Q4 [6] stats_probability: Bayes on a two-machine line ────────────────
assert (Rational(6, 10) * Rational(3, 100)
        + Rational(4, 10) * Rational(5, 100)) == Rational(19, 500)
assert (Rational(6, 10) * Rational(3, 100)) / Rational(19, 500) == Rational(9, 19)
QS.append(question(
    "IB-AAHL-P1-T3-Q4", 4, "A", "stats_probability", "conditional_probability",
    contextIntro=("A factory uses two machines to make the same component."
                  " Machine $A$ makes $60\\%$ of the components and"
                  " machine $B$ makes the rest. Of the components made by"
                  " machine $A$, $3\\%$ are defective; of those made by"
                  " machine $B$, $5\\%$ are defective. A component is chosen"
                  " at random from the factory's output."),
    parts=[
        part("a", "Find the probability that the component is defective.", 3,
             [M1("total probability: $0.6 \\times 0.03 + 0.4 \\times 0.05$"),
              A1("$0.018 + 0.020$"),
              A1("$\\dfrac{19}{500}$")],
             answer="$\\dfrac{19}{500} = 0.038$",
             solution=("Split by which machine made the component:"
                       "$$P(D) = P(A)P(D \\mid A) + P(B)P(D \\mid B)"
                       " = \\frac{6}{10}\\cdot\\frac{3}{100}"
                       " + \\frac{4}{10}\\cdot\\frac{5}{100}.$$"
                       " That is $0.018 + 0.020 = 0.038"
                       " = \\dfrac{19}{500}$."),
             verify=["Eq(Rational(6,10)*Rational(3,100)"
                     " + Rational(4,10)*Rational(5,100), Rational(19,500))",
                     "Eq(Rational(19,500), Rational(38,1000))"]),
        part("b", "Given that the chosen component is defective, find the"
             " probability that it was made by machine $A$.", 3,
             [M1("conditional probability"
                 " $P(A \\mid D) = \\dfrac{P(A \\cap D)}{P(D)}$"),
              A1("$\\dfrac{0.018}{0.038}$"),
              A1("$\\dfrac{9}{19}$")],
             answer="$\\dfrac{9}{19}$",
             solution=("Condition on the defective components only:"
                       "$$P(A \\mid D) = \\frac{P(A \\cap D)}{P(D)}"
                       " = \\frac{0.018}{0.038} = \\frac{18}{38}"
                       " = \\frac{9}{19}.$$"
                       " Notice this is less than $P(A) = 0.6$: learning"
                       " that the component is defective shifts suspicion"
                       " towards the machine with the higher defect rate."),
             verify=["Eq(Rational(18,1000)/Rational(19,500), Rational(9,19))",
                     "Rational(9,19) < Rational(6,10)"]),
    ]))

# ── Q5 [7] calculus: implicit differentiation and a tangent ──────────────
assert 1**2 + 1 * 2 + 2**2 == 7
assert Rational(-(2 * 1 + 2), 1 + 2 * 2) == Rational(-4, 5)
QS.append(question(
    "IB-AAHL-P1-T3-Q5", 5, "A", "calculus", "implicit_differentiation",
    contextIntro=("A curve is defined by the equation"
                  " $x^2 + xy + y^2 = 7$."),
    parts=[
        part("a", "Find an expression for $\\dfrac{dy}{dx}$ in terms of $x$"
             " and $y$.", 4,
             [M1("differentiate term by term with respect to $x$, using the"
                 " product rule on $xy$"),
              A1("$2x + y + x\\dfrac{dy}{dx} + 2y\\dfrac{dy}{dx} = 0$"),
              M1("collect the $\\dfrac{dy}{dx}$ terms"),
              A1("$\\dfrac{dy}{dx} = -\\dfrac{2x + y}{x + 2y}$")],
             answer="$\\dfrac{dy}{dx} = -\\dfrac{2x + y}{x + 2y}$",
             solution=("Differentiate both sides with respect to $x$,"
                       " treating $y$ as a function of $x$. The middle term"
                       " needs the product rule:"
                       "$$2x + \\left(y + x\\frac{dy}{dx}\\right)"
                       " + 2y\\frac{dy}{dx} = 0.$$"
                       " Collect the derivative terms:"
                       "$$(x + 2y)\\frac{dy}{dx} = -(2x + y),$$"
                       " so"
                       "$$\\frac{dy}{dx} = -\\frac{2x + y}{x + 2y}.$$"),
             verify=["Eq(diff(x**2 + x*y + y**2, x), 2*x + y)",
                     "Eq(diff(x**2 + x*y + y**2, y), x + 2*y)"]),
        part("b", "Find the equation of the tangent to the curve at the"
             " point $(1, 2)$, giving your answer in the form"
             " $ax + by = c$ where $a$, $b$ and $c$ are integers.", 3,
             [M1("substitute $x = 1$, $y = 2$ into the derivative"),
              A1("gradient $= -\\dfrac{4}{5}$"),
              A1("$4x + 5y = 14$")],
             answer="$4x + 5y = 14$",
             solution=("First confirm the point is on the curve:"
                       " $1 + 2 + 4 = 7$. Now substitute into the"
                       " derivative:"
                       "$$\\left.\\frac{dy}{dx}\\right|_{(1,2)}"
                       " = -\\frac{2(1) + 2}{1 + 2(2)} = -\\frac{4}{5}.$$"
                       " The tangent through $(1, 2)$ is"
                       "$$y - 2 = -\\frac{4}{5}(x - 1).$$"
                       " Multiplying by $5$ and rearranging,"
                       "$$5y - 10 = -4x + 4 \\;\\Rightarrow\\;"
                       " 4x + 5y = 14.$$"),
             verify=["Eq(1**2 + 1*2 + 2**2, 7)",
                     "Eq(Rational(-(2*1 + 2), 1 + 2*2), Rational(-4,5))",
                     "Eq(4*1 + 5*2, 14)"]),
    ]))

# ── Q6 [9] stats_probability: an exact discrete distribution ─────────────
assert Rational(1, 10) * (1 + 2 + 3 + 4) == 1
assert Rational(1 + 4 + 9 + 16, 10) == 3
assert Rational(1 + 8 + 27 + 64, 10) - 3**2 == 1
QS.append(question(
    "IB-AAHL-P1-T3-Q6", 6, "A", "stats_probability", "discrete_random_variables",
    contextIntro=("A discrete random variable $X$ has probability"
                  " distribution given by $P(X = x) = kx$ for"
                  " $x = 1, 2, 3, 4$, where $k$ is a constant."),
    parts=[
        part("a", "Show that $k = \\dfrac{1}{10}$.", 3,
             [M1("the probabilities sum to $1$:"
                 " $k(1 + 2 + 3 + 4) = 1$"),
              A1("$10k = 1$"),
              AG()],
             answer="$k = \\dfrac{1}{10}$ (given)",
             solution=("Every probability distribution sums to $1$:"
                       "$$\\sum_{x=1}^{4} kx = k(1 + 2 + 3 + 4) = 10k = 1.$$"
                       " Hence $k = \\dfrac{1}{10}$, and the four"
                       " probabilities are $0.1,\\ 0.2,\\ 0.3,\\ 0.4$, all"
                       " of which lie in $[0, 1]$ as required."),
             verify=["Eq(Rational(1,10)*(1 + 2 + 3 + 4), 1)",
                     "Eq(Rational(1,10) + Rational(2,10) + Rational(3,10)"
                     " + Rational(4,10), 1)"]),
        part("b", "Find $\\mathrm{E}(X)$.", 3,
             [M1("$\\mathrm{E}(X) = \\sum x\\,P(X = x)$"),
              A1("$\\dfrac{1 + 4 + 9 + 16}{10}$"),
              A1("$3$")],
             answer="$\\mathrm{E}(X) = 3$",
             solution=("The expectation weights each value by its"
                       " probability:"
                       "$$\\mathrm{E}(X) = \\sum_{x=1}^{4} x \\cdot"
                       " \\frac{x}{10} = \\frac{1 + 4 + 9 + 16}{10}"
                       " = \\frac{30}{10} = 3.$$"),
             verify=["Eq(Rational(1 + 4 + 9 + 16, 10), 3)"]),
        part("c", "Find $\\mathrm{Var}(X)$.", 3,
             [M1("$\\mathrm{Var}(X) = \\mathrm{E}(X^2)"
                 " - \\left(\\mathrm{E}(X)\\right)^2$"),
              A1("$\\mathrm{E}(X^2) = \\dfrac{100}{10} = 10$"),
              A1("$1$")],
             answer="$\\mathrm{Var}(X) = 1$",
             solution=("First find $\\mathrm{E}(X^2)$:"
                       "$$\\mathrm{E}(X^2) = \\sum_{x=1}^{4} x^2 \\cdot"
                       " \\frac{x}{10} = \\frac{1 + 8 + 27 + 64}{10}"
                       " = \\frac{100}{10} = 10.$$"
                       " Then"
                       "$$\\mathrm{Var}(X) = \\mathrm{E}(X^2)"
                       " - \\left(\\mathrm{E}(X)\\right)^2"
                       " = 10 - 3^2 = 1.$$"),
             verify=["Eq(Rational(1 + 8 + 27 + 64, 10), 10)",
                     "Eq(10 - 3**2, 1)"]),
    ]))

# ── Q7 [8] functions: cubic factorised, then a cubic inequality ──────────
assert 3**3 - 4 * 3**2 + 3 + 6 == 0
assert expand((x - 3) * (x - 2) * (x + 1)) == x**3 - 4 * x**2 + x + 6
QS.append(question(
    "IB-AAHL-P1-T3-Q7", 7, "A", "functions", "polynomial_functions",
    contextIntro=("The polynomial function $p$ is defined by"
                  " $p(x) = x^3 - 4x^2 + x + 6$."),
    parts=[
        part("a", "Show that $(x - 3)$ is a factor of $p(x)$.", 3,
             [M1("apply the factor theorem: evaluate $p(3)$"),
              A1("$27 - 36 + 3 + 6 = 0$"),
              AG()],
             answer="$p(3) = 0$, so $(x - 3)$ is a factor (given)",
             solution=("By the factor theorem, $(x - a)$ divides $p(x)$"
                       " exactly when $p(a) = 0$. Here"
                       "$$p(3) = 27 - 4(9) + 3 + 6 = 27 - 36 + 9 = 0,$$"
                       " so $(x - 3)$ is a factor of $p(x)$."),
             verify=["Eq(3**3 - 4*3**2 + 3 + 6, 0)",
                     "Eq(4*3**2, 36)"]),
        part("b", "Hence factorise $p(x)$ completely.", 3,
             [M1("divide $p(x)$ by $x - 3$"),
              A1("quotient $x^2 - x - 2$"),
              A1("$p(x) = (x - 3)(x - 2)(x + 1)$")],
             answer="$p(x) = (x - 3)(x - 2)(x + 1)$",
             solution=("Dividing $p(x)$ by $x - 3$ (long division or"
                       " synthetic division) gives"
                       "$$p(x) = (x - 3)(x^2 - x - 2).$$"
                       " The quadratic factor splits further, since $-2$ and"
                       " $1$ multiply to $-2$ and add to $-1$:"
                       "$$x^2 - x - 2 = (x - 2)(x + 1).$$"
                       " Hence $p(x) = (x - 3)(x - 2)(x + 1)$, with zeros"
                       " $-1$, $2$ and $3$."),
             verify=["Eq(expand((x - 3)*(x**2 - x - 2)),"
                     " x**3 - 4*x**2 + x + 6)",
                     "Eq(expand((x - 2)*(x + 1)), x**2 - x - 2)"]),
        part("c", "Hence solve the inequality $p(x) < 0$.", 2,
             [M1("consider the sign of the product across the zeros"
                 " $-1$, $2$, $3$"),
              A1("$x < -1$ or $2 < x < 3$")],
             answer="$x < -1$ or $2 < x < 3$",
             solution=("The zeros $-1$, $2$, $3$ cut the number line into"
                       " four intervals, and because each factor is linear"
                       " the sign of $p$ alternates across them. The leading"
                       " coefficient is positive, so $p(x) > 0$ on the"
                       " rightmost interval $x > 3$; the signs then"
                       " alternate leftwards:"
                       "$$x < -1:\\ p < 0, \\quad -1 < x < 2:\\ p > 0,"
                       " \\quad 2 < x < 3:\\ p < 0, \\quad x > 3:\\ p > 0.$$"
                       " Hence $p(x) < 0$ for $x < -1$ or $2 < x < 3$."
                       " Spot checks confirm it: $p(-2) = -20 < 0$,"
                       " $p(0) = 6 > 0$, $p(2.5) = -0.375 < 0$ and"
                       " $p(4) = 10 > 0$."),
             verify=["(-2)**3 - 4*(-2)**2 + (-2) + 6 < 0",
                     "0**3 - 4*0**2 + 0 + 6 > 0",
                     "Rational(5,2)**3 - 4*Rational(5,2)**2 + Rational(5,2)"
                     " + 6 < 0",
                     "4**3 - 4*4**2 + 4 + 6 > 0"]),
    ]))

# ── Q8 [20] geometry_trig: a line meeting a plane in 3D ──────────────────
assert 2 * 6 + 3 + (-1) == 14                       # C on the plane
assert Matrix([1, 1, -1]).dot(Matrix([2, 1, 1])) == 2
assert simplify(sqrt(3) * sqrt(6)) == 3 * sqrt(2)
assert Matrix([2, 2, -2]).cross(Matrix([-2, 4, -1])) == Matrix([6, 6, 12])
assert simplify(sqrt(6**2 + 6**2 + 12**2)) == 6 * sqrt(6)
QS.append(question(
    "IB-AAHL-P1-T3-Q8", 8, "B", "geometry_trig", "vectors_3d",
    contextIntro=("Relative to an origin $O$, the points $A$ and $B$ have"
                  " position vectors"
                  " $\\overrightarrow{OA} = \\begin{pmatrix} 2 \\\\ -1 \\\\"
                  " 3 \\end{pmatrix}$ and"
                  " $\\overrightarrow{OB} = \\begin{pmatrix} 4 \\\\ 1 \\\\"
                  " 1 \\end{pmatrix}$. The plane $\\Pi$ has equation"
                  " $2x + y + z = 14$."),
    parts=[
        part("a", "Find a vector equation of the line $L$ passing through"
             " $A$ and $B$.", 3,
             [M1("direction vector"
                 " $\\overrightarrow{AB} = \\overrightarrow{OB}"
                 " - \\overrightarrow{OA}$"),
              A1("$\\begin{pmatrix} 2 \\\\ 2 \\\\ -2 \\end{pmatrix}$, or"
                 " $\\begin{pmatrix} 1 \\\\ 1 \\\\ -1 \\end{pmatrix}$"),
              A1("$\\mathbf{r} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 3"
                 " \\end{pmatrix} + t\\begin{pmatrix} 1 \\\\ 1 \\\\ -1"
                 " \\end{pmatrix}$")],
             answer="$\\mathbf{r} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 3"
                    " \\end{pmatrix} + t\\begin{pmatrix} 1 \\\\ 1 \\\\ -1"
                    " \\end{pmatrix}$",
             solution=("The direction of the line is"
                       "$$\\overrightarrow{AB} = \\begin{pmatrix} 4 \\\\ 1"
                       " \\\\ 1 \\end{pmatrix} - \\begin{pmatrix} 2 \\\\ -1"
                       " \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ 2"
                       " \\\\ -2 \\end{pmatrix},$$"
                       " which is parallel to the simpler vector"
                       " $\\begin{pmatrix} 1 \\\\ 1 \\\\ -1"
                       " \\end{pmatrix}$. Taking $A$ as the position vector,"
                       "$$\\mathbf{r} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 3"
                       " \\end{pmatrix} + t\\begin{pmatrix} 1 \\\\ 1 \\\\"
                       " -1 \\end{pmatrix}, \\quad t \\in \\mathbb{R}.$$"
                       " (At $t = 2$ this gives $B$, as a check.)"),
             verify=["Eq(Matrix([4,1,1]) - Matrix([2,-1,3]),"
                     " Matrix([2,2,-2]))",
                     "Eq(Matrix([2,-1,3]) + 2*Matrix([1,1,-1]),"
                     " Matrix([4,1,1]))"]),
        part("b", "Find the coordinates of the point $C$ where $L$ meets the"
             " plane $\\Pi$.", 4,
             [M1("substitute the parametric coordinates into"
                 " $2x + y + z = 14$"),
              A1("$2(2 + t) + (-1 + t) + (3 - t) = 6 + 2t$"),
              A1("$t = 4$"),
              A1("$C(6, 3, -1)$")],
             answer="$C(6, 3, -1)$",
             solution=("A general point of $L$ is"
                       " $(2 + t,\\ -1 + t,\\ 3 - t)$. Substituting into"
                       " the plane equation,"
                       "$$2(2 + t) + (-1 + t) + (3 - t)"
                       " = 4 + 2t - 1 + t + 3 - t = 6 + 2t = 14.$$"
                       " Hence $t = 4$, and"
                       "$$C = (2 + 4,\\ -1 + 4,\\ 3 - 4) = (6, 3, -1).$$"
                       " Check: $2(6) + 3 + (-1) = 14$."),
             verify=["Eq(2*(2 + 4) + (-1 + 4) + (3 - 4), 14)",
                     "Eq(2*6 + 3 + (-1), 14)",
                     "Eq(6 + 2*4, 14)"]),
        part("c", "Find the exact value of $\\sin\\theta$, where $\\theta$ is"
             " the acute angle between $L$ and the plane $\\Pi$.", 4,
             [M1("use the normal"
                 " $\\mathbf{n} = \\begin{pmatrix} 2 \\\\ 1 \\\\ 1"
                 " \\end{pmatrix}$ and"
                 " $\\sin\\theta = \\dfrac{|\\mathbf{d}\\cdot\\mathbf{n}|}"
                 "{|\\mathbf{d}||\\mathbf{n}|}$"),
              A1("$\\mathbf{d}\\cdot\\mathbf{n} = 2$"),
              A1("$|\\mathbf{d}| = \\sqrt{3}$,"
                 " $|\\mathbf{n}| = \\sqrt{6}$"),
              A1("$\\sin\\theta = \\dfrac{\\sqrt{2}}{3}$")],
             answer="$\\sin\\theta = \\dfrac{\\sqrt{2}}{3}$",
             solution=("The angle between a line and a plane is the"
                       " COMPLEMENT of the angle between the line's"
                       " direction and the plane's normal, which turns the"
                       " usual cosine formula into a sine:"
                       "$$\\sin\\theta = \\frac{|\\mathbf{d}\\cdot"
                       "\\mathbf{n}|}{|\\mathbf{d}|\\,|\\mathbf{n}|}.$$"
                       " With $\\mathbf{d} = \\begin{pmatrix} 1 \\\\ 1 \\\\"
                       " -1 \\end{pmatrix}$ and $\\mathbf{n} ="
                       " \\begin{pmatrix} 2 \\\\ 1 \\\\ 1 \\end{pmatrix}$,"
                       "$$\\mathbf{d}\\cdot\\mathbf{n} = 2 + 1 - 1 = 2,"
                       " \\quad |\\mathbf{d}| = \\sqrt{3}, \\quad"
                       " |\\mathbf{n}| = \\sqrt{6}.$$"
                       " Therefore"
                       "$$\\sin\\theta = \\frac{2}{\\sqrt{18}}"
                       " = \\frac{2}{3\\sqrt{2}} = \\frac{\\sqrt{2}}{3}.$$"),
             verify=["Eq(Matrix([1,1,-1]).dot(Matrix([2,1,1])), 2)",
                     "Eq(sqrt(1**2 + 1**2 + 1**2), sqrt(3))",
                     "Eq(sqrt(2**2 + 1**2 + 1**2), sqrt(6))",
                     "Eq(simplify(2/(sqrt(3)*sqrt(6))), sqrt(2)/3)"]),
        part("d", "Find the exact perpendicular distance from the point"
             " $D(1, 0, 5)$ to the plane $\\Pi$.", 4,
             [M1("use $\\dfrac{|2x_0 + y_0 + z_0 - 14|}{|\\mathbf{n}|}$"),
              A1("numerator $|2 + 0 + 5 - 14| = 7$"),
              A1("denominator $\\sqrt{6}$"),
              A1("$\\dfrac{7\\sqrt{6}}{6}$")],
             answer="$\\dfrac{7\\sqrt{6}}{6}$",
             solution=("For a plane written as"
                       " $\\mathbf{n}\\cdot\\mathbf{r} = d$, the"
                       " perpendicular distance from a point"
                       " $(x_0, y_0, z_0)$ is"
                       "$$\\frac{|\\mathbf{n}\\cdot\\mathbf{r}_0 - d|}"
                       "{|\\mathbf{n}|}.$$"
                       " Here"
                       "$$\\mathbf{n}\\cdot\\mathbf{r}_0 - d"
                       " = 2(1) + 0 + 5 - 14 = -7,$$"
                       " so the distance is"
                       "$$\\frac{7}{\\sqrt{6}} = \\frac{7\\sqrt{6}}{6}.$$"),
             verify=["Eq(2*1 + 0 + 5 - 14, -7)",
                     "Eq(simplify(7/sqrt(6)), 7*sqrt(6)/6)"]),
        part("e", "The point $E$ has position vector"
             " $\\begin{pmatrix} 0 \\\\ 3 \\\\ 2 \\end{pmatrix}$. Find the"
             " exact area of triangle $ABE$.", 5,
             [M1("area"
                 " $= \\tfrac{1}{2}\\left|\\overrightarrow{AB} \\times"
                 " \\overrightarrow{AE}\\right|$"),
              A1("$\\overrightarrow{AE} = \\begin{pmatrix} -2 \\\\ 4 \\\\"
                 " -1 \\end{pmatrix}$"),
              M1("evaluate the cross product"),
              A1("$\\begin{pmatrix} 6 \\\\ 6 \\\\ 12 \\end{pmatrix}$,"
                 " magnitude $6\\sqrt{6}$"),
              A1("area $= 3\\sqrt{6}$")],
             answer="$3\\sqrt{6}$",
             solution=("The area of a triangle spanned by two vectors is"
                       " half the magnitude of their cross product. With"
                       "$$\\overrightarrow{AB} = \\begin{pmatrix} 2 \\\\ 2"
                       " \\\\ -2 \\end{pmatrix}, \\qquad"
                       " \\overrightarrow{AE} = \\begin{pmatrix} 0 \\\\ 3"
                       " \\\\ 2 \\end{pmatrix} - \\begin{pmatrix} 2 \\\\ -1"
                       " \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} -2 \\\\ 4"
                       " \\\\ -1 \\end{pmatrix},$$"
                       " the cross product is"
                       "$$\\overrightarrow{AB} \\times \\overrightarrow{AE}"
                       " = \\begin{pmatrix} 2(-1) - (-2)(4) \\\\ (-2)(-2)"
                       " - 2(-1) \\\\ 2(4) - 2(-2) \\end{pmatrix}"
                       " = \\begin{pmatrix} 6 \\\\ 6 \\\\ 12"
                       " \\end{pmatrix}.$$"
                       " Its magnitude is"
                       " $\\sqrt{36 + 36 + 144} = \\sqrt{216} = 6\\sqrt{6}$,"
                       " so the area is"
                       "$$\\tfrac{1}{2}\\left(6\\sqrt{6}\\right)"
                       " = 3\\sqrt{6}.$$"),
             verify=["Eq(Matrix([0,3,2]) - Matrix([2,-1,3]),"
                     " Matrix([-2,4,-1]))",
                     "Eq(Matrix([2,2,-2]).cross(Matrix([-2,4,-1])),"
                     " Matrix([6,6,12]))",
                     "Eq(simplify(sqrt(6**2 + 6**2 + 12**2)), 6*sqrt(6))",
                     "Eq(simplify(6*sqrt(6)/2), 3*sqrt(6))"]),
    ]))

# ── Q9 [21] calculus: the full cycle on f(x) = x e^(-x) ──────────────────
assert simplify(diff(x * exp(-x), x) - exp(-x) * (1 - x)) == 0
assert simplify(diff(x * exp(-x), x, 2) - exp(-x) * (x - 2)) == 0
assert simplify(integrate(x * exp(-x), (x, 0, 1)) - (1 - 2 * exp(-1))) == 0
assert simplify(integrate(x**2 * exp(-2 * x), (x, 0, 1))
                - (1 - 5 * exp(-2)) / 4) == 0
QS.append(question(
    "IB-AAHL-P1-T3-Q9", 9, "B", "calculus", "differentiation_applications",
    contextIntro=("The function $f$ is defined by $f(x) = x\\mathrm{e}^{-x}$"
                  " for $x \\ge 0$. The diagram shows the region $R$ bounded"
                  " by the curve $y = f(x)$, the $x$-axis and the line"
                  " $x = 1$."),
    figure=None,
    parts=[
        part("a", "Show that $f'(x) = (1 - x)\\mathrm{e}^{-x}$.", 2,
             [M1("product rule:"
                 " $f'(x) = 1\\cdot\\mathrm{e}^{-x} + x\\cdot"
                 " (-\\mathrm{e}^{-x})$"),
              AG("$f'(x) = (1 - x)\\mathrm{e}^{-x}$")],
             answer="$f'(x) = (1 - x)\\mathrm{e}^{-x}$ (given)",
             solution=("Apply the product rule to $x \\cdot"
                       " \\mathrm{e}^{-x}$, with $u = x$ and"
                       " $v = \\mathrm{e}^{-x}$ so that $u' = 1$ and"
                       " $v' = -\\mathrm{e}^{-x}$:"
                       "$$f'(x) = (1)\\mathrm{e}^{-x}"
                       " + x\\left(-\\mathrm{e}^{-x}\\right)"
                       " = \\mathrm{e}^{-x} - x\\mathrm{e}^{-x}"
                       " = (1 - x)\\mathrm{e}^{-x}.$$"),
             verify=["Eq(simplify(diff(x*exp(-x), x) - (1 - x)*exp(-x)), 0)",
                     "Eq(simplify(diff(exp(-x), x) + exp(-x)), 0)"]),
        part("b", "Find the coordinates of the stationary point of the"
             " curve.", 2,
             [M1("set $f'(x) = 0$; $\\mathrm{e}^{-x} \\neq 0$ so $x = 1$"),
              A1("$\\left(1, \\dfrac{1}{\\mathrm{e}}\\right)$")],
             answer="$\\left(1, \\dfrac{1}{\\mathrm{e}}\\right)$",
             solution=("Since $\\mathrm{e}^{-x} > 0$ for every $x$, the"
                       " derivative $(1 - x)\\mathrm{e}^{-x}$ vanishes only"
                       " when $1 - x = 0$, that is at $x = 1$. Then"
                       "$$f(1) = 1 \\cdot \\mathrm{e}^{-1}"
                       " = \\frac{1}{\\mathrm{e}},$$"
                       " so the stationary point is"
                       " $\\left(1, \\dfrac{1}{\\mathrm{e}}\\right)$."),
             verify=["Eq((1 - 1)*exp(-1), 0)", "exp(-1) > 0",
                     "Eq(1*exp(-1), exp(-1))"]),
        part("c", "Justify that this stationary point is a local maximum.", 3,
             [M1("find $f''(x) = (x - 2)\\mathrm{e}^{-x}$"),
              A1("$f''(1) = -\\mathrm{e}^{-1}$"),
              R1("$f''(1) < 0$, so the stationary point is a local maximum")],
             answer="$f''(1) = -\\dfrac{1}{\\mathrm{e}} < 0$, so it is a"
                    " local maximum",
             solution=("Differentiate $f'(x) = (1 - x)\\mathrm{e}^{-x}$"
                       " again, using the product rule once more:"
                       "$$f''(x) = (-1)\\mathrm{e}^{-x}"
                       " + (1 - x)\\left(-\\mathrm{e}^{-x}\\right)"
                       " = (x - 2)\\mathrm{e}^{-x}.$$"
                       " At the stationary point,"
                       "$$f''(1) = (1 - 2)\\mathrm{e}^{-1}"
                       " = -\\frac{1}{\\mathrm{e}} < 0,$$"
                       " so the curve is concave down there and the"
                       " stationary point is a local maximum."),
             verify=["Eq(simplify(diff(x*exp(-x), x, 2) - (x - 2)*exp(-x)),"
                     " 0)",
                     "(1 - 2)*exp(-1) < 0"]),
        part("d", "Find the coordinates of the point of inflexion of the"
             " curve.", 4,
             [M1("set $f''(x) = 0$"),
              A1("$x = 2$"),
              R1("$f''$ changes sign at $x = 2$ (negative before, positive"
                 " after)"),
              A1("$\\left(2, \\dfrac{2}{\\mathrm{e}^{2}}\\right)$")],
             answer="$\\left(2, \\dfrac{2}{\\mathrm{e}^{2}}\\right)$",
             solution=("A point of inflexion needs $f''(x) = 0$ together"
                       " with a change of sign. From"
                       " $f''(x) = (x - 2)\\mathrm{e}^{-x}$ and"
                       " $\\mathrm{e}^{-x} > 0$, the only zero is $x = 2$,"
                       " and $f''$ changes from negative (for $x < 2$) to"
                       " positive (for $x > 2$) there — a genuine change of"
                       " concavity. The $y$-coordinate is"
                       "$$f(2) = 2\\mathrm{e}^{-2}"
                       " = \\frac{2}{\\mathrm{e}^{2}},$$"
                       " so the point of inflexion is"
                       " $\\left(2, \\dfrac{2}{\\mathrm{e}^{2}}\\right)$."),
             verify=["Eq((2 - 2)*exp(-2), 0)",
                     "(1 - 2)*exp(-1) < 0", "(3 - 2)*exp(-3) > 0"]),
        part("e", "Find the exact area of the region $R$.", 5,
             [M1("integrate by parts with $u = x$,"
                 " $\\dfrac{dv}{dx} = \\mathrm{e}^{-x}$"),
              A1("$\\int x\\mathrm{e}^{-x}\\,dx"
                 " = -x\\mathrm{e}^{-x} - \\mathrm{e}^{-x} + c$"),
              M1("evaluate between $0$ and $1$"),
              A1("$\\left[-(x + 1)\\mathrm{e}^{-x}\\right]_0^1"
                 " = -2\\mathrm{e}^{-1} + 1$"),
              A1("$1 - \\dfrac{2}{\\mathrm{e}}$")],
             answer="$1 - \\dfrac{2}{\\mathrm{e}}$",
             solution=("Integrate by parts with $u = x$ and"
                       " $\\dfrac{dv}{dx} = \\mathrm{e}^{-x}$, so"
                       " $\\dfrac{du}{dx} = 1$ and"
                       " $v = -\\mathrm{e}^{-x}$:"
                       "$$\\int x\\mathrm{e}^{-x}\\,dx"
                       " = -x\\mathrm{e}^{-x} + \\int \\mathrm{e}^{-x}\\,dx"
                       " = -x\\mathrm{e}^{-x} - \\mathrm{e}^{-x} + c"
                       " = -(x + 1)\\mathrm{e}^{-x} + c.$$"
                       " Evaluating between $0$ and $1$,"
                       "$$\\left[-(x + 1)\\mathrm{e}^{-x}\\right]_{0}^{1}"
                       " = -2\\mathrm{e}^{-1} - \\left(-1\\right)"
                       " = 1 - \\frac{2}{\\mathrm{e}}.$$"
                       " Since $\\mathrm{e} > 2$, this value is positive, as"
                       " an area must be."),
             verify=["Eq(simplify(integrate(x*exp(-x), (x, 0, 1))"
                     " - (1 - 2*exp(-1))), 0)",
                     "Eq(simplify(diff(-(x + 1)*exp(-x), x) - x*exp(-x)), 0)"]),
        part("f", "The region $R$ is rotated through $2\\pi$ about the"
             " $x$-axis. Find the exact volume of the solid formed.", 5,
             [M1("$V = \\pi\\displaystyle\\int_{0}^{1} x^2"
                 "\\mathrm{e}^{-2x}\\,dx$"),
              M1("integrate by parts twice"),
              A1("$\\int x^2\\mathrm{e}^{-2x}\\,dx"
                 " = -\\left(\\tfrac{x^2}{2} + \\tfrac{x}{2}"
                 " + \\tfrac{1}{4}\\right)\\mathrm{e}^{-2x} + c$"),
              A1("definite value"
                 " $\\dfrac{1}{4} - \\dfrac{5}{4\\mathrm{e}^{2}}$"),
              A1("$V = \\dfrac{\\pi\\left(1 - 5\\mathrm{e}^{-2}\\right)}"
                 "{4}$")],
             answer="$V = \\dfrac{\\pi\\left(1"
                    " - 5\\mathrm{e}^{-2}\\right)}{4}$",
             solution=("Rotating about the $x$-axis gives"
                       "$$V = \\pi\\int_{0}^{1}\\left(x\\mathrm{e}^{-x}"
                       "\\right)^{2}dx"
                       " = \\pi\\int_{0}^{1} x^{2}\\mathrm{e}^{-2x}\\,dx.$$"
                       " Integrating by parts twice (first with $u = x^2$,"
                       " then with $u = x$) gives the antiderivative"
                       "$$\\int x^{2}\\mathrm{e}^{-2x}\\,dx"
                       " = -\\left(\\frac{x^{2}}{2} + \\frac{x}{2}"
                       " + \\frac{1}{4}\\right)\\mathrm{e}^{-2x} + c.$$"
                       " At $x = 1$ the bracket is"
                       " $\\tfrac{1}{2} + \\tfrac{1}{2} + \\tfrac{1}{4}"
                       " = \\tfrac{5}{4}$, and at $x = 0$ it is"
                       " $\\tfrac{1}{4}$, so"
                       "$$\\int_{0}^{1} x^{2}\\mathrm{e}^{-2x}\\,dx"
                       " = -\\frac{5}{4}\\mathrm{e}^{-2} + \\frac{1}{4}"
                       " = \\frac{1 - 5\\mathrm{e}^{-2}}{4}.$$"
                       " Therefore"
                       "$$V = \\frac{\\pi\\left(1"
                       " - 5\\mathrm{e}^{-2}\\right)}{4}.$$"),
             verify=["Eq(simplify(integrate(x**2*exp(-2*x), (x, 0, 1))"
                     " - (1 - 5*exp(-2))/4), 0)",
                     "Eq(simplify(diff(-(x**2/2 + x/2 + Rational(1,4))"
                     "*exp(-2*x), x) - x**2*exp(-2*x)), 0)"]),
    ]))

# ── Q10 [18] number_algebra: complex numbers and induction ───────────────
assert Abs(1 + sqrt(3) * I) == 2
assert arg(1 + sqrt(3) * I) == pi / 3
assert simplify((1 + sqrt(3) * I) ** 6) == 64
assert simplify((2 * (cos(pi / 6) + I * sin(pi / 6))) ** 3 - 8 * I) == 0
QS.append(question(
    "IB-AAHL-P1-T3-Q10", 10, "B", "number_algebra", "complex_numbers",
    parts=[
        part("a", "Let $z = 1 + \\sqrt{3}\\,\\mathrm{i}$. Find $|z|$ and"
             " $\\arg z$, and hence write $z$ in modulus-argument form.", 4,
             [M1("$|z| = \\sqrt{1^2 + (\\sqrt{3})^2}$"),
              A1("$|z| = 2$"),
              A1("$\\arg z = \\dfrac{\\pi}{3}$"),
              A1("$z = 2\\left(\\cos\\tfrac{\\pi}{3}"
                 " + \\mathrm{i}\\sin\\tfrac{\\pi}{3}\\right)$")],
             answer="$|z| = 2$, $\\arg z = \\dfrac{\\pi}{3}$,"
                    " $z = 2\\operatorname{cis}\\dfrac{\\pi}{3}$",
             solution=("The modulus is"
                       "$$|z| = \\sqrt{1^{2} + \\left(\\sqrt{3}\\right)^{2}}"
                       " = \\sqrt{4} = 2.$$"
                       " The point $\\left(1, \\sqrt{3}\\right)$ lies in the"
                       " first quadrant, so"
                       "$$\\arg z = \\arctan\\!\\left(\\frac{\\sqrt{3}}{1}"
                       "\\right) = \\frac{\\pi}{3}.$$"
                       " Hence"
                       "$$z = 2\\left(\\cos\\frac{\\pi}{3}"
                       " + \\mathrm{i}\\sin\\frac{\\pi}{3}\\right).$$"),
             verify=["Eq(Abs(1 + sqrt(3)*I), 2)",
                     "Eq(arg(1 + sqrt(3)*I), pi/3)",
                     "Eq(simplify(2*(cos(pi/3) + I*sin(pi/3))),"
                     " 1 + sqrt(3)*I)"]),
        part("b", "Hence find $z^{6}$, giving your answer in Cartesian"
             " form.", 4,
             [M1("apply De Moivre's theorem"),
              A1("$z^{6} = 2^{6}\\left(\\cos 2\\pi"
                 " + \\mathrm{i}\\sin 2\\pi\\right)$"),
              A1("$= 64(1 + 0\\mathrm{i})$"),
              A1("$z^{6} = 64$")],
             answer="$z^{6} = 64$",
             solution=("De Moivre's theorem raises the modulus to the power"
                       " and multiplies the argument:"
                       "$$z^{6} = 2^{6}\\left(\\cos\\frac{6\\pi}{3}"
                       " + \\mathrm{i}\\sin\\frac{6\\pi}{3}\\right)"
                       " = 64\\left(\\cos 2\\pi"
                       " + \\mathrm{i}\\sin 2\\pi\\right).$$"
                       " Since $\\cos 2\\pi = 1$ and $\\sin 2\\pi = 0$,"
                       "$$z^{6} = 64.$$"
                       " The result is real because the argument"
                       " $\\dfrac{\\pi}{3}$ multiplied by $6$ lands exactly"
                       " on a full turn."),
             verify=["Eq(simplify((1 + sqrt(3)*I)**6), 64)",
                     "Eq(2**6, 64)", "Eq(cos(2*pi), 1)", "Eq(sin(2*pi), 0)"]),
        part("c", "Find the three cube roots of $8\\mathrm{i}$, giving your"
             " answers in modulus-argument form with arguments in"
             " $[0, 2\\pi)$.", 4,
             [M1("write $8\\mathrm{i} = 8\\operatorname{cis}"
                 "\\dfrac{\\pi}{2}$ and take cube roots"),
              A1("$2\\operatorname{cis}\\dfrac{\\pi}{6}$"),
              A1("$2\\operatorname{cis}\\dfrac{5\\pi}{6}$"),
              A1("$2\\operatorname{cis}\\dfrac{3\\pi}{2}$")],
             answer="$2\\operatorname{cis}\\dfrac{\\pi}{6}$,"
                    " $2\\operatorname{cis}\\dfrac{5\\pi}{6}$,"
                    " $2\\operatorname{cis}\\dfrac{3\\pi}{2}$",
             solution=("First write the number in modulus-argument form:"
                       " $8\\mathrm{i}$ has modulus $8$ and argument"
                       " $\\dfrac{\\pi}{2}$, so"
                       "$$8\\mathrm{i} = 8\\operatorname{cis}"
                       "\\left(\\frac{\\pi}{2} + 2k\\pi\\right).$$"
                       " Taking cube roots divides the argument by $3$ and"
                       " the modulus becomes $\\sqrt[3]{8} = 2$:"
                       "$$w_k = 2\\operatorname{cis}"
                       "\\left(\\frac{\\pi}{6} + \\frac{2k\\pi}{3}\\right),"
                       " \\quad k = 0, 1, 2.$$"
                       " This gives"
                       " $2\\operatorname{cis}\\dfrac{\\pi}{6}$,"
                       " $2\\operatorname{cis}\\dfrac{5\\pi}{6}$ and"
                       " $2\\operatorname{cis}\\dfrac{3\\pi}{2}$ — three"
                       " points equally spaced by $\\dfrac{2\\pi}{3}$ around"
                       " a circle of radius $2$."),
             verify=["Eq(simplify((2*(cos(pi/6) + I*sin(pi/6)))**3), 8*I)",
                     "Eq(simplify((2*(cos(5*pi/6) + I*sin(5*pi/6)))**3),"
                     " 8*I)",
                     "Eq(simplify((2*(cos(3*pi/2) + I*sin(3*pi/2)))**3),"
                     " 8*I)",
                     "Eq(pi/6 + 2*pi/3, 5*pi/6)"]),
        part("d", "Prove by mathematical induction that"
             " $\\displaystyle\\sum_{r=1}^{n} r(r + 1)"
             " = \\frac{n(n + 1)(n + 2)}{3}$ for all"
             " $n \\in \\mathbb{Z}^{+}$.", 6,
             [R1("base case $n = 1$: left side $= 2$, right side"
                 " $= \\dfrac{1\\cdot2\\cdot3}{3} = 2$ — true"),
              M1("assume the result holds for $n = k$"),
              M1("consider the sum to $k + 1$:"
                 " $\\dfrac{k(k+1)(k+2)}{3} + (k+1)(k+2)$"),
              A1("$= \\dfrac{(k+1)(k+2)\\left(k + 3\\right)}{3}$"),
              R1("this is the formula with $n = k + 1$"),
              R1("true for $n = 1$ and $k \\Rightarrow k + 1$, so true for"
                 " all $n \\in \\mathbb{Z}^{+}$ by induction")],
             answer="proof by induction (see solution)",
             solution=("**Base case** $n = 1$: the left side is"
                       " $1 \\times 2 = 2$ and the right side is"
                       " $\\dfrac{1 \\cdot 2 \\cdot 3}{3} = 2$, so the"
                       " statement holds."
                       "**Inductive step**: assume that for some"
                       " $k \\in \\mathbb{Z}^{+}$"
                       "$$\\sum_{r=1}^{k} r(r + 1)"
                       " = \\frac{k(k + 1)(k + 2)}{3}.$$"
                       " Adding the next term $(k + 1)(k + 2)$,"
                       "$$\\sum_{r=1}^{k+1} r(r + 1)"
                       " = \\frac{k(k + 1)(k + 2)}{3} + (k + 1)(k + 2)"
                       " = (k + 1)(k + 2)\\left(\\frac{k}{3} + 1\\right).$$"
                       " Writing the bracket over $3$,"
                       "$$= \\frac{(k + 1)(k + 2)(k + 3)}{3},$$"
                       " which is exactly the formula with $n = k + 1$."
                       "Since the statement is true for $n = 1$ and its"
                       " truth for $n = k$ implies its truth for"
                       " $n = k + 1$, it holds for all positive integers"
                       " $n$ by mathematical induction."),
             verify=["Eq(1*2, Rational(1*2*3, 3))",
                     "Eq(1*2 + 2*3, Rational(2*3*4, 3))",
                     "Eq(1*2 + 2*3 + 3*4, Rational(3*4*5, 3))",
                     "Eq(simplify(Rational(1,3)*k*(k + 1)*(k + 2)"
                     " + (k + 1)*(k + 2)"
                     " - Rational(1,3)*(k + 1)*(k + 2)*(k + 3)), 0)"]),
    ]))

META = {"course": "aa", "level": "hl", "paper": 1, "testId": "ib-hl-practice-3",
        "label": "AA HL Practice Paper 1", "timeMinutes": 120,
        "totalMarks": 110, "calculator": False}

if __name__ == "__main__":
    QS[8]["figure"] = png("ib-aahl-p1-t3-q9.png",
                          "Region R bounded by the curve y = x e^(-x), the "
                          "x-axis and the line x = 1")
    write_paper(META, QS, "data/ib/aa-hl/ib-hl-practice-3/paper1.json")
