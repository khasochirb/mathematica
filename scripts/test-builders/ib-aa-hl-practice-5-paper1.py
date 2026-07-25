"""AA HL Practice Paper 1 (ib-hl-practice-5) — 120 min, 110 marks, NO calculator.

Blueprint (topic x marks):
    Section A (52): Q1 number_algebra 6  | Q2 functions 8
                    Q3 geometry_trig 8   | Q4 stats_probability 7
                    Q5 calculus 7        | Q6 number_algebra 8
                    Q7 calculus 8
    Section B (58): Q8 geometry_trig 20  | Q9 calculus 20
                    Q10 stats_probability 18
    Paper totals: number_algebra 14 | functions 8 | geometry_trig 28 |
                  stats_probability 25 | calculus 35 = 110.

HL-only content, fresh versus HL Sets 1-4: an arithmetic series pinned by
two of its terms, a quadratic's range from its completed square, the
double-angle route from tan to sin and cos, a probability tree WITHOUT
replacement, the quotient rule, a proof by CONTRADICTION that sqrt(3) is
irrational, integration by parts on x cos x, the vector equation of a
plane through THREE points together with the angle between two planes,
the curve y = x sqrt(4 - x^2) taken through the full calculus cycle, and
a discrete random variable defined by a two-parameter table.
Everything exact.
Figure: Q9 (region under x sqrt(4 - x^2) from 0 to 2).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, I, Matrix, simplify, solve,  # noqa: F401,E402
                   expand, factor, diff, integrate, atan, sin, cos, tan,
                   binomial, factorial, symbols, Abs, log, exp, E, oo, limit)

x, y, t, k, n, m, a, b, d = symbols("x y t k n m a b d")


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [6] number_algebra: an arithmetic series from two terms ──────────
_s1 = solve([Eq(a + 3 * d, 17), Eq(a + 8 * d, 37)], [a, d], dict=True)[0]
assert _s1[a] == 5 and _s1[d] == 4
assert sum(5 + 4 * i for i in range(0, 20)) == 860
QS.append(question(
    "IB-AAHL-P1-T5-Q1", 1, "A", "number_algebra", "arithmetic_sequences",
    contextIntro=("In an arithmetic sequence the fourth term is $17$ and"
                  " the ninth term is $37$."),
    parts=[
        part("a", "Find the first term and the common difference.", 3,
             [M1("write both terms as $u_1 + (n-1)d$ and subtract"),
              A1("$5d = 20$, so $d = 4$"),
              A1("$u_1 = 5$")],
             answer="$u_1 = 5$, $d = 4$",
             solution=("Write each given term with the general formula"
                       " $u_n = u_1 + (n - 1)d$:"
                       "$$u_4 = u_1 + 3d = 17, \\qquad u_9 = u_1 + 8d"
                       " = 37.$$"
                       " Subtracting the first from the second removes"
                       " $u_1$:"
                       "$$5d = 20 \\;\\Rightarrow\\; d = 4,$$"
                       " and then $u_1 = 17 - 3(4) = 5$. Check:"
                       " $u_9 = 5 + 8(4) = 37$."),
             verify=["Eq(5 + 3*4, 17)", "Eq(5 + 8*4, 37)",
                     "Eq(37 - 17, 20)"]),
        part("b", "Find the sum of the first $20$ terms.", 3,
             [M1("$S_{20} = \\dfrac{20}{2}\\left(2u_1 + 19d\\right)$"),
              A1("$10(10 + 76)$"),
              A1("$860$")],
             answer="$860$",
             solution=("Use the sum formula for an arithmetic series:"
                       "$$S_{20} = \\frac{20}{2}\\left(2u_1 + 19d\\right)"
                       " = 10\\left(2(5) + 19(4)\\right) = 10(10 + 76).$$"
                       " That gives $S_{20} = 10(86) = 860$."
                       " (Equivalently, $u_{20} = 5 + 19(4) = 81$ and"
                       " $S_{20} = \\tfrac{20}{2}(5 + 81) = 860$.)"),
             verify=["Eq(Rational(20,2)*(2*5 + 19*4), 860)",
                     "Eq(5 + 19*4, 81)",
                     "Eq(Rational(20,2)*(5 + 81), 860)"]),
    ]))

# ── Q2 [8] functions: a quadratic's range and its inverse branch ────────
assert expand((x - 3) ** 2 - 4) == x**2 - 6 * x + 5
QS.append(question(
    "IB-AAHL-P1-T5-Q2", 2, "A", "functions", "quadratic_functions",
    contextIntro=("The function $f$ is defined by"
                  " $f(x) = x^{2} - 6x + 5$ for $x \\in \\mathbb{R}$."),
    parts=[
        part("a", "Write $f(x)$ in the form $(x - h)^{2} + k$.", 3,
             [M1("complete the square: half of $-6$ is $-3$"),
              A1("$(x - 3)^{2} - 9 + 5$"),
              A1("$(x - 3)^{2} - 4$")],
             answer="$f(x) = (x - 3)^{2} - 4$",
             solution=("Half the coefficient of $x$ is $-3$, and"
                       " $(-3)^{2} = 9$, so"
                       "$$x^{2} - 6x + 5 = \\left(x^{2} - 6x + 9\\right)"
                       " - 9 + 5 = (x - 3)^{2} - 4.$$"
                       " Expanding back confirms it."),
             verify=["Eq(expand((x - 3)**2 - 4), x**2 - 6*x + 5)",
                     "Eq((-3)**2, 9)"]),
        part("b", "Hence write down the range of $f$.", 2,
             [R1("a square is never negative, so"
                 " $(x - 3)^{2} \\ge 0$"),
              A1("$f(x) \\ge -4$")],
             answer="$f(x) \\ge -4$",
             solution=("From part (a), $f(x) = (x - 3)^{2} - 4$. The"
                       " square term is at least $0$ for every real $x$"
                       " and equals $0$ only at $x = 3$, so"
                       "$$f(x) \\ge -4,$$"
                       " with the minimum $-4$ attained at $x = 3$. The"
                       " range is $[-4, \\infty)$."),
             verify=["Eq((3 - 3)**2 - 4, -4)", "(0 - 3)**2 - 4 > -4",
                     "(6 - 3)**2 - 4 > -4"]),
        part("c", "The domain of $f$ is now restricted to $x \\ge 3$. Find"
             " an expression for $f^{-1}(x)$ on this restricted domain, and"
             " state its domain.", 3,
             [M1("set $y = (x - 3)^{2} - 4$ and solve for $x$"),
              A1("$f^{-1}(x) = 3 + \\sqrt{x + 4}$"),
              A1("domain $x \\ge -4$")],
             answer="$f^{-1}(x) = 3 + \\sqrt{x + 4}$, for $x \\ge -4$",
             solution=("Restricting to $x \\ge 3$ makes $f$ one-to-one, so"
                       " an inverse exists. Starting from"
                       " $y = (x - 3)^{2} - 4$,"
                       "$$(x - 3)^{2} = y + 4 \\;\\Rightarrow\\;"
                       " x - 3 = \\pm\\sqrt{y + 4}.$$"
                       " The restriction $x \\ge 3$ forces the POSITIVE"
                       " root, so"
                       "$$f^{-1}(x) = 3 + \\sqrt{x + 4}.$$"
                       " Its domain is the range of $f$ found in part (b),"
                       " namely $x \\ge -4$ — which is also exactly where"
                       " the square root is defined."),
             verify=["Eq(simplify(((3 + sqrt(x + 4)) - 3)**2 - 4 - x), 0)",
                     "Eq(3 + sqrt(-4 + 4), 3)",
                     "Eq((5 - 3)**2 - 4, 0)", "Eq(3 + sqrt(0 + 4), 5)"]),
    ]))

# ── Q3 [8] geometry_trig: from tan to the double angles ────────────────
assert simplify(sin(atan(Rational(3, 4))) - Rational(3, 5)) == 0
assert 2 * Rational(3, 5) * Rational(4, 5) == Rational(24, 25)
assert 1 - 2 * Rational(3, 5) ** 2 == Rational(7, 25)
QS.append(question(
    "IB-AAHL-P1-T5-Q3", 3, "A", "geometry_trig", "double_angle_formulas",
    contextIntro=("The angle $\\theta$ satisfies"
                  " $\\tan\\theta = \\dfrac{3}{4}$ and"
                  " $0 < \\theta < \\dfrac{\\pi}{2}$."),
    parts=[
        part("a", "Find the exact values of $\\sin\\theta$ and"
             " $\\cos\\theta$.", 3,
             [M1("build a right triangle with opposite $3$, adjacent $4$"),
              A1("hypotenuse $5$"),
              A1("$\\sin\\theta = \\dfrac{3}{5}$,"
                 " $\\cos\\theta = \\dfrac{4}{5}$")],
             answer="$\\sin\\theta = \\dfrac{3}{5}$,"
                    " $\\cos\\theta = \\dfrac{4}{5}$",
             solution=("Since $\\tan\\theta$ is opposite over adjacent,"
                       " sketch a right triangle with legs $3$ and $4$."
                       " Its hypotenuse is"
                       "$$\\sqrt{3^{2} + 4^{2}} = 5.$$"
                       " Because $\\theta$ is in the first quadrant both"
                       " ratios are positive:"
                       "$$\\sin\\theta = \\frac{3}{5}, \\qquad"
                       " \\cos\\theta = \\frac{4}{5}.$$"
                       " (Check: $\\left(\\tfrac35\\right)^{2}"
                       " + \\left(\\tfrac45\\right)^{2} = 1$.)"),
             verify=["Eq(3**2 + 4**2, 5**2)",
                     "Eq(Rational(3,5)**2 + Rational(4,5)**2, 1)",
                     "Eq(Rational(3,5)/Rational(4,5), Rational(3,4))"]),
        part("b", "Hence find the exact values of $\\sin 2\\theta$ and"
             " $\\cos 2\\theta$.", 5,
             [M1("$\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$"),
              A1("$\\dfrac{24}{25}$"),
              M1("$\\cos 2\\theta = 1 - 2\\sin^{2}\\theta$"),
              A1("$1 - \\dfrac{18}{25}$"),
              A1("$\\dfrac{7}{25}$")],
             answer="$\\sin 2\\theta = \\dfrac{24}{25}$,"
                    " $\\cos 2\\theta = \\dfrac{7}{25}$",
             solution=("Use the double-angle formulas with the values from"
                       " part (a):"
                       "$$\\sin 2\\theta = 2\\sin\\theta\\cos\\theta"
                       " = 2\\cdot\\frac{3}{5}\\cdot\\frac{4}{5}"
                       " = \\frac{24}{25},$$"
                       "$$\\cos 2\\theta = 1 - 2\\sin^{2}\\theta"
                       " = 1 - 2\\cdot\\frac{9}{25} = 1 - \\frac{18}{25}"
                       " = \\frac{7}{25}.$$"
                       " Any of the three forms of $\\cos 2\\theta$ gives"
                       " the same value; for instance"
                       " $\\cos^{2}\\theta - \\sin^{2}\\theta"
                       " = \\tfrac{16}{25} - \\tfrac{9}{25}"
                       " = \\tfrac{7}{25}$. As a check,"
                       " $\\left(\\tfrac{24}{25}\\right)^{2}"
                       " + \\left(\\tfrac{7}{25}\\right)^{2} = 1$."),
             verify=["Eq(2*Rational(3,5)*Rational(4,5), Rational(24,25))",
                     "Eq(1 - 2*Rational(3,5)**2, Rational(7,25))",
                     "Eq(Rational(4,5)**2 - Rational(3,5)**2,"
                     " Rational(7,25))",
                     "Eq(Rational(24,25)**2 + Rational(7,25)**2, 1)"]),
    ]))

# ── Q4 [7] stats_probability: drawing without replacement ──────────────
assert Rational(7, 12) * Rational(6, 11) == Rational(7, 22)
assert (Rational(7, 12) * Rational(5, 11)
        + Rational(5, 12) * Rational(7, 11)) == Rational(35, 66)
QS.append(question(
    "IB-AAHL-P1-T5-Q4", 4, "A", "stats_probability", "probability_basics",
    contextIntro=("A box contains $7$ green marbles and $5$ yellow"
                  " marbles. Two marbles are drawn at random, one after the"
                  " other, WITHOUT replacement."),
    parts=[
        part("a", "Find the probability that both marbles are green.", 3,
             [M1("multiply along the branch, reducing the pool"),
              A1("$\\dfrac{7}{12}\\times\\dfrac{6}{11}$"),
              A1("$\\dfrac{7}{22}$")],
             answer="$\\dfrac{7}{22}$",
             solution=("The first marble is green with probability"
                       " $\\dfrac{7}{12}$. If it was green, only $6$ green"
                       " marbles remain among $11$, so"
                       "$$P(\\text{both green}) = \\frac{7}{12}\\times"
                       "\\frac{6}{11} = \\frac{42}{132}"
                       " = \\frac{7}{22}.$$"
                       " The second fraction has smaller numerator AND"
                       " denominator — that is what \"without replacement\""
                       " changes."),
             verify=["Eq(Rational(7,12)*Rational(6,11), Rational(7,22))",
                     "Eq(Rational(42,132), Rational(7,22))"]),
        part("b", "Find the probability that the two marbles are of"
             " different colours.", 4,
             [M1("two branches: green-then-yellow or"
                 " yellow-then-green"),
              A1("$\\dfrac{7}{12}\\times\\dfrac{5}{11}"
                 " = \\dfrac{35}{132}$"),
              A1("$\\dfrac{5}{12}\\times\\dfrac{7}{11}"
                 " = \\dfrac{35}{132}$"),
              A1("$\\dfrac{35}{66}$")],
             answer="$\\dfrac{35}{66}$",
             solution=("Different colours happens two ways, and they are"
                       " mutually exclusive so their probabilities add:"
                       "$$P(GY) = \\frac{7}{12}\\times\\frac{5}{11}"
                       " = \\frac{35}{132}, \\qquad"
                       " P(YG) = \\frac{5}{12}\\times\\frac{7}{11}"
                       " = \\frac{35}{132}.$$"
                       " Hence"
                       "$$P(\\text{different}) = \\frac{35}{132}"
                       " + \\frac{35}{132} = \\frac{70}{132}"
                       " = \\frac{35}{66}.$$"
                       " Check with the complement: both green is"
                       " $\\tfrac{7}{22} = \\tfrac{21}{66}$ and both"
                       " yellow is $\\tfrac{5}{12}\\cdot\\tfrac{4}{11}"
                       " = \\tfrac{10}{66}$, and"
                       " $\\tfrac{21 + 10 + 35}{66} = 1$."),
             verify=["Eq(Rational(7,12)*Rational(5,11), Rational(35,132))",
                     "Eq(2*Rational(35,132), Rational(35,66))",
                     "Eq(Rational(7,22) + Rational(5,12)*Rational(4,11)"
                     " + Rational(35,66), 1)"]),
    ]))

# ── Q5 [7] calculus: the quotient rule ─────────────────────────────────
assert simplify(diff((2 * x + 1) / (x**2 + 3), x)
                - (-2 * x**2 - 2 * x + 6) / (x**2 + 3) ** 2) == 0
assert simplify(diff((2 * x + 1) / (x**2 + 3), x).subs(x, 1)) == Rational(1, 8)
QS.append(question(
    "IB-AAHL-P1-T5-Q5", 5, "A", "calculus", "quotient_rule",
    contextIntro=("The function $f$ is defined by"
                  " $f(x) = \\dfrac{2x + 1}{x^{2} + 3}$."),
    parts=[
        part("a", "Find $f'(x)$, simplifying your answer.", 4,
             [M1("quotient rule with $u = 2x + 1$, $v = x^{2} + 3$"),
              A1("$\\dfrac{2\\left(x^{2} + 3\\right)"
                 " - (2x + 1)(2x)}{\\left(x^{2} + 3\\right)^{2}}$"),
              M1("expand the numerator"),
              A1("$f'(x) = \\dfrac{-2x^{2} - 2x + 6}"
                 "{\\left(x^{2} + 3\\right)^{2}}$")],
             answer="$f'(x) = \\dfrac{-2x^{2} - 2x + 6}"
                    "{\\left(x^{2} + 3\\right)^{2}}$",
             solution=("With $u = 2x + 1$ and $v = x^{2} + 3$ we have"
                       " $u' = 2$ and $v' = 2x$, so"
                       "$$f'(x) = \\frac{vu' - uv'}{v^{2}}"
                       " = \\frac{2\\left(x^{2} + 3\\right)"
                       " - (2x + 1)(2x)}{\\left(x^{2} + 3\\right)^{2}}.$$"
                       " Expanding the numerator,"
                       "$$2x^{2} + 6 - \\left(4x^{2} + 2x\\right)"
                       " = -2x^{2} - 2x + 6,$$"
                       " so"
                       "$$f'(x) = \\frac{-2x^{2} - 2x + 6}"
                       "{\\left(x^{2} + 3\\right)^{2}}.$$"
                       " The order $vu' - uv'$ matters — reversing it flips"
                       " every sign."),
             verify=["Eq(simplify(diff((2*x + 1)/(x**2 + 3), x)"
                     " - (-2*x**2 - 2*x + 6)/(x**2 + 3)**2), 0)",
                     "Eq(expand(2*(x**2 + 3) - (2*x + 1)*(2*x)),"
                     " -2*x**2 - 2*x + 6)"]),
        part("b", "Find the gradient of the curve $y = f(x)$ at the point"
             " where $x = 1$.", 3,
             [M1("substitute $x = 1$"),
              A1("$\\dfrac{-2 - 2 + 6}{16}$"),
              A1("$\\dfrac{1}{8}$")],
             answer="$\\dfrac{1}{8}$",
             solution=("Substitute $x = 1$ into the derivative:"
                       "$$f'(1) = \\frac{-2(1) - 2(1) + 6}"
                       "{\\left(1 + 3\\right)^{2}} = \\frac{2}{16}"
                       " = \\frac{1}{8}.$$"
                       " The gradient is positive, so the curve is rising"
                       " at that point."),
             verify=["Eq(Rational(-2 - 2 + 6, (1 + 3)**2), Rational(1,8))",
                     "Eq(simplify(diff((2*x + 1)/(x**2 + 3), x).subs(x, 1)),"
                     " Rational(1,8))"]),
    ]))

# ── Q6 [8] number_algebra: proof by contradiction ──────────────────────
assert 3 * 1**2 != 2**2 and 3 * 2**2 != 3**2
assert simplify(sqrt(3) ** 2) == 3
QS.append(question(
    "IB-AAHL-P1-T5-Q6", 6, "A", "number_algebra", "proof_methods",
    parts=[
        part("a", "Show that if $p$ is an integer and $p^{2}$ is divisible"
             " by $3$, then $p$ is divisible by $3$.", 3,
             [M1("consider the cases $p = 3q$, $p = 3q + 1$,"
                 " $p = 3q + 2$"),
              A1("$(3q+1)^{2} = 3(3q^{2} + 2q) + 1$ and"
                 " $(3q+2)^{2} = 3(3q^{2} + 4q + 1) + 1$"),
              AG()],
             answer="only $p = 3q$ gives $p^{2}$ divisible by $3$"
                    " (given)",
             solution=("Every integer is exactly one of $3q$, $3q + 1$ or"
                       " $3q + 2$ for some integer $q$. Squaring each:"
                       "$$(3q)^{2} = 3\\left(3q^{2}\\right),$$"
                       "$$(3q + 1)^{2} = 9q^{2} + 6q + 1"
                       " = 3\\left(3q^{2} + 2q\\right) + 1,$$"
                       "$$(3q + 2)^{2} = 9q^{2} + 12q + 4"
                       " = 3\\left(3q^{2} + 4q + 1\\right) + 1.$$"
                       " The last two leave remainder $1$ on division by"
                       " $3$, so $p^{2}$ is divisible by $3$ only in the"
                       " first case — that is, only when $p$ itself is a"
                       " multiple of $3$."),
             verify=["Eq(expand((3*k + 1)**2), 9*k**2 + 6*k + 1)",
                     "Eq(expand((3*k + 2)**2), 9*k**2 + 12*k + 4)",
                     "Eq((4**2) % 3, 1)", "Eq((5**2) % 3, 1)",
                     "Eq((6**2) % 3, 0)"]),
        part("b", "Hence prove by contradiction that $\\sqrt{3}$ is"
             " irrational.", 5,
             [M1("assume $\\sqrt{3} = \\dfrac{p}{q}$ in lowest terms with"
                 " $q \\neq 0$"),
              A1("$p^{2} = 3q^{2}$, so $p^{2}$ is divisible by $3$"),
              M1("by part (a), $p = 3r$, so $9r^{2} = 3q^{2}$"),
              A1("$q^{2} = 3r^{2}$, so $q$ is also divisible by $3$"),
              R1("that contradicts \"lowest terms\", so $\\sqrt{3}$ is"
                 " irrational")],
             answer="proof by contradiction (see solution)",
             solution=("**Assume the opposite**: suppose $\\sqrt{3}$ is"
                       " rational, so"
                       "$$\\sqrt{3} = \\frac{p}{q}$$"
                       " for integers $p$ and $q \\neq 0$ with no common"
                       " factor — the fraction is in lowest terms."
                       "Squaring and clearing the denominator,"
                       "$$p^{2} = 3q^{2}.$$"
                       " So $p^{2}$ is divisible by $3$, and by part (a)"
                       " $p$ itself is divisible by $3$. Write $p = 3r$:"
                       "$$9r^{2} = 3q^{2} \\;\\Rightarrow\\;"
                       " q^{2} = 3r^{2}.$$"
                       " Now $q^{2}$ is divisible by $3$, so by part (a)"
                       " again $q$ is divisible by $3$."
                       "But then $p$ and $q$ share the factor $3$,"
                       " contradicting the assumption that the fraction"
                       " was in lowest terms. The assumption must be"
                       " false, so $\\sqrt{3}$ is irrational."),
             verify=["Eq(simplify(sqrt(3)**2), 3)",
                     "Eq(expand((3*k)**2), 3*(3*k**2))",
                     "Eq(simplify(9*k**2 - 3*(3*k**2)), 0)"]),
    ]))

# ── Q7 [8] calculus: integration by parts on x cos x ───────────────────
assert simplify(diff(x * sin(x) + cos(x), x) - x * cos(x)) == 0
assert simplify(integrate(x * cos(x), (x, 0, pi / 2)) - (pi / 2 - 1)) == 0
QS.append(question(
    "IB-AAHL-P1-T5-Q7", 7, "A", "calculus", "integration_by_parts",
    parts=[
        part("a", "Use integration by parts to show that"
             " $\\displaystyle\\int x\\cos x\\,dx"
             " = x\\sin x + \\cos x + c$.", 4,
             [M1("choose $u = x$,"
                 " $\\dfrac{dv}{dx} = \\cos x$"),
              A1("$x\\sin x - \\displaystyle\\int \\sin x\\,dx$"),
              A1("$= x\\sin x + \\cos x + c$"),
              AG()],
             answer="$x\\sin x + \\cos x + c$ (given)",
             solution=("Take $u = x$ and $\\dfrac{dv}{dx} = \\cos x$, so"
                       " $\\dfrac{du}{dx} = 1$ and $v = \\sin x$."
                       " (Choosing $u$ to be the polynomial is what makes"
                       " the remaining integral simpler.) Then"
                       "$$\\int x\\cos x\\,dx = x\\sin x"
                       " - \\int \\sin x\\,dx = x\\sin x + \\cos x + c.$$"
                       " Differentiating the result checks it:"
                       " $\\sin x + x\\cos x - \\sin x = x\\cos x$."),
             verify=["Eq(simplify(diff(x*sin(x) + cos(x), x) - x*cos(x)),"
                     " 0)",
                     "Eq(diff(sin(x), x), cos(x))"]),
        part("b", "Hence find the exact value of"
             " $\\displaystyle\\int_{0}^{\\frac{\\pi}{2}} x\\cos x\\,dx$.",
             4,
             [M1("substitute the limits into"
                 " $x\\sin x + \\cos x$"),
              A1("at $\\dfrac{\\pi}{2}$: $\\dfrac{\\pi}{2}(1) + 0$"),
              A1("at $0$: $0 + 1$"),
              A1("$\\dfrac{\\pi}{2} - 1$")],
             answer="$\\dfrac{\\pi}{2} - 1$",
             solution=("Evaluate the antiderivative at the two limits,"
                       " remembering $\\sin\\dfrac{\\pi}{2} = 1$ and"
                       " $\\cos\\dfrac{\\pi}{2} = 0$:"
                       "$$\\left[x\\sin x + \\cos x\\right]_{0}^{\\pi/2}"
                       " = \\left(\\frac{\\pi}{2}\\cdot 1 + 0\\right)"
                       " - \\left(0 + 1\\right).$$"
                       " Hence the integral equals"
                       "$$\\frac{\\pi}{2} - 1 \\approx 0.571,$$"
                       " which is positive, as it must be since"
                       " $x\\cos x \\ge 0$ throughout"
                       " $\\left[0, \\tfrac{\\pi}{2}\\right]$."),
             verify=["Eq(sin(pi/2), 1)", "Eq(cos(pi/2), 0)",
                     "Eq(simplify(integrate(x*cos(x), (x, 0, pi/2))),"
                     " pi/2 - 1)",
                     "pi/2 - 1 > 0"]),
    ]))

# ── Q8 [20] geometry_trig: a plane through three points, two planes ────
_P, _Q, _R = Matrix([1, 0, 2]), Matrix([3, 1, 1]), Matrix([2, -1, 4])
_n8 = (_Q - _P).cross(_R - _P)
assert _n8 == Matrix([1, -5, -3])
assert _n8.dot(_P) == _n8.dot(_Q) == _n8.dot(_R) == -5
_m8 = Matrix([2, -1, 2])
assert _n8.dot(_m8) == 1
assert simplify(_n8.norm()) == sqrt(35)
assert simplify(Abs(_n8.dot(Matrix([4, 2, 1])) + 5) / _n8.norm()) \
    == 4 * sqrt(35) / 35
QS.append(question(
    "IB-AAHL-P1-T5-Q8", 8, "B", "geometry_trig", "vectors_planes",
    contextIntro=("The points $P(1, 0, 2)$, $Q(3, 1, 1)$ and"
                  " $R(2, -1, 4)$ lie in the plane $\\Pi_1$. The plane"
                  " $\\Pi_2$ has equation $2x - y + 2z = 5$."),
    parts=[
        part("a", "Find $\\overrightarrow{PQ}$ and"
             " $\\overrightarrow{PR}$.", 3,
             [M1("subtract position vectors"),
              A1("$\\overrightarrow{PQ} = \\begin{pmatrix} 2 \\\\ 1 \\\\"
                 " -1 \\end{pmatrix}$"),
              A1("$\\overrightarrow{PR} = \\begin{pmatrix} 1 \\\\ -1 \\\\"
                 " 2 \\end{pmatrix}$")],
             answer="$\\overrightarrow{PQ} = \\begin{pmatrix} 2 \\\\ 1"
                    " \\\\ -1 \\end{pmatrix}$,"
                    " $\\overrightarrow{PR} = \\begin{pmatrix} 1 \\\\ -1"
                    " \\\\ 2 \\end{pmatrix}$",
             solution=("Subtract the position vector of the start point"
                       " from that of the end point:"
                       "$$\\overrightarrow{PQ} = \\begin{pmatrix} 3 \\\\ 1"
                       " \\\\ 1 \\end{pmatrix} - \\begin{pmatrix} 1 \\\\ 0"
                       " \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ 1"
                       " \\\\ -1 \\end{pmatrix},$$"
                       "$$\\overrightarrow{PR} = \\begin{pmatrix} 2 \\\\"
                       " -1 \\\\ 4 \\end{pmatrix} - \\begin{pmatrix} 1"
                       " \\\\ 0 \\\\ 2 \\end{pmatrix}"
                       " = \\begin{pmatrix} 1 \\\\ -1 \\\\ 2"
                       " \\end{pmatrix}.$$"),
             verify=["Eq(Matrix([3,1,1]) - Matrix([1,0,2]),"
                     " Matrix([2,1,-1]))",
                     "Eq(Matrix([2,-1,4]) - Matrix([1,0,2]),"
                     " Matrix([1,-1,2]))"]),
        part("b", "Find a Cartesian equation of the plane $\\Pi_1$.", 5,
             [M1("a normal is"
                 " $\\overrightarrow{PQ} \\times \\overrightarrow{PR}$"),
              M1("evaluate the cross product"),
              A1("$\\mathbf{n} = \\begin{pmatrix} 1 \\\\ -5 \\\\ -3"
                 " \\end{pmatrix}$"),
              M1("use $\\mathbf{n}\\cdot\\mathbf{r}"
                 " = \\mathbf{n}\\cdot\\overrightarrow{OP}$"),
              A1("$x - 5y - 3z = -5$")],
             answer="$x - 5y - 3z = -5$",
             solution=("Two independent vectors lying in the plane give a"
                       " normal through their cross product:"
                       "$$\\mathbf{n} = \\overrightarrow{PQ} \\times"
                       " \\overrightarrow{PR} = \\begin{pmatrix}"
                       " (1)(2) - (-1)(-1) \\\\ (-1)(1) - (2)(2) \\\\"
                       " (2)(-1) - (1)(1) \\end{pmatrix}"
                       " = \\begin{pmatrix} 1 \\\\ -5 \\\\ -3"
                       " \\end{pmatrix}.$$"
                       " Substituting the point $P(1, 0, 2)$ fixes the"
                       " constant:"
                       "$$\\mathbf{n}\\cdot\\overrightarrow{OP}"
                       " = 1(1) - 5(0) - 3(2) = -5,$$"
                       " so the plane is"
                       "$$x - 5y - 3z = -5.$$"
                       " Check the other two points: for $Q$,"
                       " $3 - 5 - 3 = -5$; for $R$, $2 + 5 - 12 = -5$."
                       " Both lie on it, as they must."),
             verify=["Eq(Matrix([2,1,-1]).cross(Matrix([1,-1,2])),"
                     " Matrix([1,-5,-3]))",
                     "Eq(Matrix([1,-5,-3]).dot(Matrix([1,0,2])), -5)",
                     "Eq(Matrix([1,-5,-3]).dot(Matrix([3,1,1])), -5)",
                     "Eq(Matrix([1,-5,-3]).dot(Matrix([2,-1,4])), -5)"]),
        part("c", "Find the exact value of $\\cos\\phi$, where $\\phi$ is"
             " the acute angle between the planes $\\Pi_1$ and"
             " $\\Pi_2$.", 5,
             [M1("the angle between planes is the angle between their"
                 " normals"),
              A1("$\\mathbf{n}_1\\cdot\\mathbf{n}_2 = 2 + 5 - 6 = 1$"),
              A1("$|\\mathbf{n}_1| = \\sqrt{35}$"),
              A1("$|\\mathbf{n}_2| = 3$"),
              A1("$\\cos\\phi = \\dfrac{\\sqrt{35}}{105}$")],
             answer="$\\cos\\phi = \\dfrac{\\sqrt{35}}{105}$",
             solution=("Two planes meet at the same angle their normals"
                       " do, so"
                       "$$\\cos\\phi = \\frac{|\\mathbf{n}_1\\cdot"
                       "\\mathbf{n}_2|}{|\\mathbf{n}_1||\\mathbf{n}_2|}.$$"
                       " With $\\mathbf{n}_1 = \\begin{pmatrix} 1 \\\\ -5"
                       " \\\\ -3 \\end{pmatrix}$ and $\\mathbf{n}_2"
                       " = \\begin{pmatrix} 2 \\\\ -1 \\\\ 2"
                       " \\end{pmatrix}$,"
                       "$$\\mathbf{n}_1\\cdot\\mathbf{n}_2"
                       " = 1(2) + (-5)(-1) + (-3)(2) = 2 + 5 - 6 = 1,$$"
                       "$$|\\mathbf{n}_1| = \\sqrt{1 + 25 + 9}"
                       " = \\sqrt{35}, \\qquad |\\mathbf{n}_2|"
                       " = \\sqrt{4 + 1 + 4} = 3.$$"
                       " Therefore"
                       "$$\\cos\\phi = \\frac{1}{3\\sqrt{35}}"
                       " = \\frac{\\sqrt{35}}{105}.$$"
                       " The absolute value is taken so that the ACUTE"
                       " angle is returned whichever way the normals"
                       " happen to point."),
             verify=["Eq(Matrix([1,-5,-3]).dot(Matrix([2,-1,2])), 1)",
                     "Eq(simplify(sqrt(1 + 25 + 9)), sqrt(35))",
                     "Eq(sqrt(4 + 1 + 4), 3)",
                     "Eq(simplify(1/(3*sqrt(35))), sqrt(35)/105)"]),
        part("d", "Find the exact perpendicular distance from the point"
             " $S(4, 2, 1)$ to the plane $\\Pi_1$.", 4,
             [M1("use"
                 " $\\dfrac{|\\mathbf{n}\\cdot\\mathbf{s} + 5|}"
                 "{|\\mathbf{n}|}$"),
              A1("$\\mathbf{n}\\cdot\\mathbf{s} = 4 - 10 - 3 = -9$"),
              A1("numerator $|-9 - (-5)| = 4$"),
              A1("$\\dfrac{4\\sqrt{35}}{35}$")],
             answer="$\\dfrac{4\\sqrt{35}}{35}$",
             solution=("For the plane written as"
                       " $\\mathbf{n}\\cdot\\mathbf{r} = d$, the distance"
                       " from a point with position vector $\\mathbf{s}$"
                       " is"
                       "$$\\frac{|\\mathbf{n}\\cdot\\mathbf{s} - d|}"
                       "{|\\mathbf{n}|}.$$"
                       " Here $d = -5$ and"
                       "$$\\mathbf{n}\\cdot\\mathbf{s} = 1(4) - 5(2)"
                       " - 3(1) = -9,$$"
                       " so the numerator is $|-9 + 5| = 4$ and"
                       "$$\\text{distance} = \\frac{4}{\\sqrt{35}}"
                       " = \\frac{4\\sqrt{35}}{35}.$$"),
             verify=["Eq(Matrix([1,-5,-3]).dot(Matrix([4,2,1])), -9)",
                     "Eq(Abs(-9 + 5), 4)",
                     "Eq(simplify(4/sqrt(35)), 4*sqrt(35)/35)"]),
        part("e", "Find the exact area of triangle $PQR$.", 3,
             [M1("area"
                 " $= \\tfrac{1}{2}\\left|\\overrightarrow{PQ} \\times"
                 " \\overrightarrow{PR}\\right|$"),
              A1("magnitude $\\sqrt{35}$"),
              A1("$\\dfrac{\\sqrt{35}}{2}$")],
             answer="$\\dfrac{\\sqrt{35}}{2}$",
             solution=("The cross product computed in part (b) already"
                       " carries the area: its magnitude equals twice the"
                       " area of the triangle spanned by the two vectors."
                       " Since"
                       "$$\\left|\\overrightarrow{PQ} \\times"
                       " \\overrightarrow{PR}\\right|"
                       " = \\sqrt{1^{2} + (-5)^{2} + (-3)^{2}}"
                       " = \\sqrt{35},$$"
                       " the area of triangle $PQR$ is"
                       "$$\\frac{\\sqrt{35}}{2}.$$"),
             verify=["Eq(simplify(Matrix([1,-5,-3]).norm()), sqrt(35))",
                     "Eq(1 + 25 + 9, 35)"]),
    ]))

# ── Q9 [20] calculus: y = x sqrt(4 - x^2) ─────────────────────────────
assert simplify(diff(x * sqrt(4 - x**2), x)
                - (4 - 2 * x**2) / sqrt(4 - x**2)) == 0
assert simplify((sqrt(2)) * sqrt(4 - 2)) == 2
assert simplify(integrate(x * sqrt(4 - x**2), (x, 0, 2))) == Rational(8, 3)
assert simplify(pi * integrate(x**2 * (4 - x**2), (x, 0, 2))) \
    == Rational(64, 15) * pi
QS.append(question(
    "IB-AAHL-P1-T5-Q9", 9, "B", "calculus", "differentiation_applications",
    contextIntro=("The function $f$ is defined by"
                  " $f(x) = x\\sqrt{4 - x^{2}}$ for"
                  " $0 \\le x \\le 2$. The diagram shows the region $R$"
                  " bounded by the curve $y = f(x)$ and the $x$-axis."),
    figure=None,
    parts=[
        part("a", "State the domain of $f$ as given, and explain why the"
             " curve meets the $x$-axis at both ends of it.", 3,
             [R1("the square root needs $4 - x^{2} \\ge 0$"),
              A1("$0 \\le x \\le 2$"),
              R1("$f(0) = 0$ and $f(2) = 2\\sqrt{0} = 0$")],
             answer="$0 \\le x \\le 2$; $f(0) = f(2) = 0$",
             solution=("The square root requires"
                       " $4 - x^{2} \\ge 0$, that is"
                       " $-2 \\le x \\le 2$; combined with the stated"
                       " restriction the domain is $0 \\le x \\le 2$."
                       " At the two ends,"
                       "$$f(0) = 0 \\cdot \\sqrt{4} = 0, \\qquad"
                       " f(2) = 2 \\cdot \\sqrt{0} = 0,$$"
                       " so the curve starts and finishes on the"
                       " $x$-axis — the first because the factor $x$"
                       " vanishes, the second because the root does."),
             verify=["Eq(0*sqrt(4 - 0**2), 0)", "Eq(2*sqrt(4 - 2**2), 0)",
                     "4 - 2**2 >= 0", "4 - 3**2 < 0"]),
        part("b", "Show that $f'(x) = \\dfrac{4 - 2x^{2}}"
             "{\\sqrt{4 - x^{2}}}$ for $0 < x < 2$.", 4,
             [M1("product rule on $x$ and"
                 " $\\left(4 - x^{2}\\right)^{1/2}$"),
              A1("$\\sqrt{4 - x^{2}} + x\\cdot\\dfrac{-x}"
                 "{\\sqrt{4 - x^{2}}}$"),
              A1("common denominator"
                 " $\\dfrac{\\left(4 - x^{2}\\right) - x^{2}}"
                 "{\\sqrt{4 - x^{2}}}$"),
              AG()],
             answer="$f'(x) = \\dfrac{4 - 2x^{2}}{\\sqrt{4 - x^{2}}}$"
                    " (given)",
             solution=("Use the product rule with the chain rule on the"
                       " root:"
                       "$$f'(x) = 1\\cdot\\sqrt{4 - x^{2}}"
                       " + x\\cdot\\frac{-2x}{2\\sqrt{4 - x^{2}}}"
                       " = \\sqrt{4 - x^{2}} - \\frac{x^{2}}"
                       "{\\sqrt{4 - x^{2}}}.$$"
                       " Putting both terms over the common denominator"
                       " $\\sqrt{4 - x^{2}}$,"
                       "$$f'(x) = \\frac{\\left(4 - x^{2}\\right)"
                       " - x^{2}}{\\sqrt{4 - x^{2}}}"
                       " = \\frac{4 - 2x^{2}}{\\sqrt{4 - x^{2}}}.$$"),
             verify=["Eq(simplify(diff(x*sqrt(4 - x**2), x)"
                     " - (4 - 2*x**2)/sqrt(4 - x**2)), 0)",
                     "Eq(simplify(diff(sqrt(4 - x**2), x)"
                     " + x/sqrt(4 - x**2)), 0)"]),
        part("c", "Find the exact coordinates of the maximum point of the"
             " curve.", 4,
             [M1("set the numerator $4 - 2x^{2}$ to zero"),
              A1("$x = \\sqrt{2}$ (taking the positive root)"),
              M1("evaluate $f$ there"),
              A1("$\\left(\\sqrt{2},\\ 2\\right)$")],
             answer="$\\left(\\sqrt{2},\\ 2\\right)$",
             solution=("A fraction vanishes when its numerator does, so"
                       "$$4 - 2x^{2} = 0 \\;\\Rightarrow\\; x^{2} = 2"
                       " \\;\\Rightarrow\\; x = \\sqrt{2},$$"
                       " taking the positive root because the domain is"
                       " $0 < x < 2$. There"
                       "$$f\\!\\left(\\sqrt{2}\\right)"
                       " = \\sqrt{2}\\cdot\\sqrt{4 - 2}"
                       " = \\sqrt{2}\\cdot\\sqrt{2} = 2.$$"
                       " It is a maximum because $f' > 0$ for"
                       " $x < \\sqrt{2}$ and $f' < 0$ for"
                       " $x > \\sqrt{2}$ — the numerator changes sign"
                       " while the denominator stays positive. So the"
                       " maximum point is"
                       " $\\left(\\sqrt{2},\\ 2\\right)$."),
             verify=["Eq(4 - 2*(sqrt(2))**2, 0)",
                     "Eq(simplify(sqrt(2)*sqrt(4 - 2)), 2)",
                     "4 - 2*1**2 > 0",
                     "4 - 2*Rational(3,2)**2 < 0"]),
        part("d", "Find the exact area of the region $R$.", 5,
             [M1("substitute $u = 4 - x^{2}$, so"
                 " $x\\,dx = -\\tfrac{1}{2}du$"),
              A1("$-\\tfrac{1}{2}\\displaystyle\\int u^{1/2}du"
                 " = -\\tfrac{1}{3}u^{3/2}$"),
              M1("evaluate between $x = 0$ and $x = 2$"),
              A1("$0 - \\left(-\\tfrac{1}{3}(8)\\right)$"),
              A1("area $= \\dfrac{8}{3}$")],
             answer="$\\dfrac{8}{3}$",
             solution=("The factor $x$ outside is exactly what a"
                       " substitution needs. With $u = 4 - x^{2}$ we get"
                       " $du = -2x\\,dx$, so"
                       " $x\\,dx = -\\tfrac{1}{2}du$ and"
                       "$$\\int x\\sqrt{4 - x^{2}}\\,dx"
                       " = -\\frac{1}{2}\\int u^{1/2}du"
                       " = -\\frac{1}{3}u^{3/2} + c"
                       " = -\\frac{1}{3}\\left(4 - x^{2}\\right)^{3/2}"
                       " + c.$$"
                       " Evaluating from $0$ to $2$,"
                       "$$A = \\left[-\\frac{1}{3}\\left(4 - x^{2}"
                       "\\right)^{3/2}\\right]_{0}^{2}"
                       " = 0 - \\left(-\\frac{1}{3}\\cdot 8\\right)"
                       " = \\frac{8}{3}.$$"),
             verify=["Eq(simplify(diff(-Rational(1,3)*(4 - x**2)"
                     "**Rational(3,2), x) - x*sqrt(4 - x**2)), 0)",
                     "Eq(simplify(integrate(x*sqrt(4 - x**2), (x, 0, 2))),"
                     " Rational(8,3))",
                     "Eq(4**Rational(3,2), 8)"]),
        part("e", "The region $R$ is rotated through $2\\pi$ about the"
             " $x$-axis. Find the exact volume of the solid formed.", 4,
             [M1("$V = \\pi\\displaystyle\\int_{0}^{2}"
                 " x^{2}\\left(4 - x^{2}\\right)dx$"),
              A1("$\\pi\\left[\\dfrac{4x^{3}}{3} - \\dfrac{x^{5}}{5}"
                 "\\right]_{0}^{2}$"),
              A1("$\\dfrac{32}{3} - \\dfrac{32}{5}$"),
              A1("$V = \\dfrac{64\\pi}{15}$")],
             answer="$V = \\dfrac{64\\pi}{15}$",
             solution=("Squaring the function removes the root entirely,"
                       " which is what makes this volume elementary:"
                       "$$V = \\pi\\int_{0}^{2}\\left(x\\sqrt{4 - x^{2}}"
                       "\\right)^{2}dx"
                       " = \\pi\\int_{0}^{2}\\left(4x^{2} - x^{4}"
                       "\\right)dx.$$"
                       " Antidifferentiating,"
                       "$$V = \\pi\\left[\\frac{4x^{3}}{3}"
                       " - \\frac{x^{5}}{5}\\right]_{0}^{2}"
                       " = \\pi\\left(\\frac{32}{3} - \\frac{32}{5}"
                       "\\right).$$"
                       " Over the common denominator $15$,"
                       "$$V = \\pi\\cdot\\frac{160 - 96}{15}"
                       " = \\frac{64\\pi}{15}.$$"),
             verify=["Eq(simplify(integrate(4*x**2 - x**4, (x, 0, 2))),"
                     " Rational(64,15))",
                     "Eq(Rational(32,3) - Rational(32,5), Rational(64,15))"]),
    ]))

# ── Q10 [18] stats_probability: a two-parameter discrete table ─────────
_sol10 = solve([Eq(Rational(1, 5) + a + b + Rational(1, 10), 1),
                Eq(1 * Rational(1, 5) + 2 * a + 3 * b + 4 * Rational(1, 10),
                   Rational(23, 10))], [a, b], dict=True)[0]
assert _sol10[a] == Rational(2, 5) and _sol10[b] == Rational(3, 10)
_EX = Rational(23, 10)
_EX2 = (1 * Rational(1, 5) + 4 * Rational(2, 5) + 9 * Rational(3, 10)
        + 16 * Rational(1, 10))
assert _EX2 == Rational(61, 10)
assert _EX2 - _EX**2 == Rational(81, 100)
QS.append(question(
    "IB-AAHL-P1-T5-Q10", 10, "B", "stats_probability",
    "discrete_random_variables",
    contextIntro=("A discrete random variable $X$ has the probability"
                  " distribution shown below, where $a$ and $b$ are"
                  " constants."
                  "$$\\begin{array}{c|cccc}"
                  " x & 1 & 2 & 3 & 4 \\\\ \\hline"
                  " P(X = x) & \\dfrac{1}{5} & a & b & \\dfrac{1}{10}"
                  " \\end{array}$$"
                  "It is given that $\\mathrm{E}(X) = 2.3$."),
    parts=[
        part("a", "Write down two equations in $a$ and $b$.", 3,
             [M1("the probabilities sum to $1$"),
              A1("$a + b = \\dfrac{7}{10}$"),
              A1("$2a + 3b = \\dfrac{17}{10}$")],
             answer="$a + b = \\dfrac{7}{10}$ and"
                    " $2a + 3b = \\dfrac{17}{10}$",
             solution=("Every distribution sums to $1$:"
                       "$$\\frac{1}{5} + a + b + \\frac{1}{10} = 1"
                       " \\;\\Rightarrow\\; a + b = \\frac{7}{10}.$$"
                       " The expectation gives a second equation:"
                       "$$1\\left(\\frac{1}{5}\\right) + 2a + 3b"
                       " + 4\\left(\\frac{1}{10}\\right) = 2.3"
                       " \\;\\Rightarrow\\; 2a + 3b = 2.3 - 0.6"
                       " = \\frac{17}{10}.$$"),
             verify=["Eq(1 - Rational(1,5) - Rational(1,10),"
                     " Rational(7,10))",
                     "Eq(Rational(23,10) - Rational(1,5)"
                     " - 4*Rational(1,10), Rational(17,10))"]),
        part("b", "Hence find the values of $a$ and $b$.", 4,
             [M1("eliminate $a$ by subtracting twice the first equation"),
              A1("$b = \\dfrac{3}{10}$"),
              M1("substitute back"),
              A1("$a = \\dfrac{2}{5}$")],
             answer="$a = \\dfrac{2}{5}$, $b = \\dfrac{3}{10}$",
             solution=("From $a + b = \\dfrac{7}{10}$, multiply by $2$:"
                       "$$2a + 2b = \\frac{14}{10}.$$"
                       " Subtracting this from"
                       " $2a + 3b = \\dfrac{17}{10}$ leaves"
                       "$$b = \\frac{3}{10}.$$"
                       " Then $a = \\dfrac{7}{10} - \\dfrac{3}{10}"
                       " = \\dfrac{4}{10} = \\dfrac{2}{5}$."
                       " Both values lie in $[0, 1]$ and the four"
                       " probabilities sum to $1$, as required."),
             verify=["Eq(Rational(2,5) + Rational(3,10), Rational(7,10))",
                     "Eq(2*Rational(2,5) + 3*Rational(3,10),"
                     " Rational(17,10))",
                     "Eq(Rational(1,5) + Rational(2,5) + Rational(3,10)"
                     " + Rational(1,10), 1)"]),
        part("c", "Find $\\mathrm{Var}(X)$.", 5,
             [M1("$\\mathrm{E}(X^{2}) = \\sum x^{2}P(X = x)$"),
              A1("$\\dfrac{1}{5} + \\dfrac{8}{5} + \\dfrac{27}{10}"
                 " + \\dfrac{8}{5}$"),
              A1("$\\mathrm{E}(X^{2}) = \\dfrac{61}{10}$"),
              M1("$\\mathrm{Var}(X) = \\mathrm{E}(X^{2})"
                 " - \\left(\\mathrm{E}(X)\\right)^{2}$"),
              A1("$\\dfrac{81}{100} = 0.81$")],
             answer="$\\mathrm{Var}(X) = \\dfrac{81}{100} = 0.81$",
             solution=("First the second moment, weighting each SQUARED"
                       " value by its probability:"
                       "$$\\mathrm{E}(X^{2}) = 1\\left(\\frac{1}{5}"
                       "\\right) + 4\\left(\\frac{2}{5}\\right)"
                       " + 9\\left(\\frac{3}{10}\\right)"
                       " + 16\\left(\\frac{1}{10}\\right).$$"
                       " Over the denominator $10$ this is"
                       " $\\dfrac{2 + 16 + 27 + 16}{10}"
                       " = \\dfrac{61}{10}$. Then"
                       "$$\\mathrm{Var}(X) = \\mathrm{E}(X^{2})"
                       " - \\left(\\mathrm{E}(X)\\right)^{2}"
                       " = \\frac{61}{10} - \\left(\\frac{23}{10}"
                       "\\right)^{2} = \\frac{610 - 529}{100}"
                       " = \\frac{81}{100}.$$"
                       " So $\\mathrm{Var}(X) = 0.81$, and the standard"
                       " deviation is exactly $0.9$."),
             verify=["Eq(Rational(1,5) + 4*Rational(2,5) + 9*Rational(3,10)"
                     " + 16*Rational(1,10), Rational(61,10))",
                     "Eq(Rational(61,10) - Rational(23,10)**2,"
                     " Rational(81,100))",
                     "Eq(sqrt(Rational(81,100)), Rational(9,10))"]),
        part("d", "Two independent observations of $X$ are made. Find the"
             " probability that their sum is $7$.", 6,
             [M1("list the ordered pairs summing to $7$"),
              A1("$(3, 4)$ and $(4, 3)$"),
              M1("multiply within each pair, then add"),
              A1("$\\dfrac{3}{10}\\times\\dfrac{1}{10}"
                 " = \\dfrac{3}{100}$"),
              A1("doubled for the two orders"),
              A1("$\\dfrac{3}{50}$")],
             answer="$\\dfrac{3}{50} = 0.06$",
             solution=("Since $X$ takes only the values $1$ to $4$, a sum"
                       " of $7$ can arise only from the ordered pairs"
                       " $(3, 4)$ and $(4, 3)$. The observations are"
                       " independent, so multiply within each pair:"
                       "$$P(3 \\text{ then } 4) = \\frac{3}{10}\\times"
                       "\\frac{1}{10} = \\frac{3}{100},$$"
                       "$$P(4 \\text{ then } 3) = \\frac{1}{10}\\times"
                       "\\frac{3}{10} = \\frac{3}{100}.$$"
                       " These outcomes are mutually exclusive, so add:"
                       "$$P(\\text{sum} = 7) = \\frac{6}{100}"
                       " = \\frac{3}{50} = 0.06.$$"
                       " Forgetting that the two orders are DIFFERENT"
                       " outcomes halves the answer — the single most"
                       " common slip here."),
             verify=["Eq(Rational(3,10)*Rational(1,10), Rational(3,100))",
                     "Eq(2*Rational(3,100), Rational(3,50))",
                     "Eq(Rational(3,50), Rational(6,100))"]),
    ]))

META = {"course": "aa", "level": "hl", "paper": 1, "testId": "ib-hl-practice-5",
        "label": "AA HL Practice Paper 1", "timeMinutes": 120,
        "totalMarks": 110, "calculator": False}

if __name__ == "__main__":
    QS[8]["figure"] = png("ib-aahl-p1-t5-q9.png",
                          "Region R bounded by the curve y = x times the "
                          "square root of (4 minus x squared) and the "
                          "x-axis, from x = 0 to x = 2")
    write_paper(META, QS, "data/ib/aa-hl/ib-hl-practice-5/paper1.json")
