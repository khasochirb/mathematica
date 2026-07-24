"""AA HL Practice Paper 1 (ib-hl-practice-2) — 120 min, 110 marks, NO calculator.

Blueprint (topic x marks):
    Section A (51): Q1 number_algebra 5 | Q2 stats_probability 6
                    Q3 functions 9      | Q4 number_algebra 6
                    Q5 geometry_trig 8  | Q6 calculus 8
                    Q7 stats_probability 9
    Section B (59): Q8 geometry_trig 21 | Q9 calculus 20
                    Q10 number_algebra 18
    Paper totals: number_algebra 29 | functions 9 | geometry_trig 29 |
                  stats_probability 15 | calculus 28 = 110.

HL-only content, fresh versus HL Set 1: selections/combinations, a
rational function with no stationary points, complex numbers in Cartesian
and modulus-argument form, a trig equation reduced to a quadratic in
cos, related rates of change, exact binomial B(4, 1/3), skew lines in 3D
(angle, shortest distance, common perpendicular), integration by
substitution + volume of revolution, and TWO proofs by induction
(a summation formula and a divisibility result). Everything exact.
Figure: Q9 (region under x / sqrt(x^2 + 4)).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, I, Matrix, simplify, solve,  # noqa: F401,E402
                   expand, factor, diff, integrate, atan, sin, cos, tan,
                   binomial, factorial, symbols, im, re, arg, Abs, log)

x, k, n, m = symbols("x k n m")


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [5] number_algebra: selections / combinations ─────────────────────
assert binomial(11, 4) == 330
assert binomial(6, 2) * binomial(5, 2) == 150
QS.append(question(
    "IB-AAHL-P1-T2-Q1", 1, "A", "number_algebra", "counting",
    contextIntro=("A committee of $4$ people is to be chosen from a group of"
                  " $6$ men and $5$ women."),
    parts=[
        part("a", "Find the number of different committees that can be"
             " formed.", 2,
             [M1("choose $4$ from $11$: $\\binom{11}{4}$"),
              A1("$330$")],
             answer="$330$",
             solution=("$$\\binom{11}{4} = \\frac{11!}{4!\\,7!} = 330.$$"),
             verify=["Eq(binomial(11, 4), 330)"]),
        part("b", "Find the number of committees that contain exactly $2$ men"
             " and $2$ women.", 3,
             [M1("multiply independent choices $\\binom{6}{2}$ and "
                 "$\\binom{5}{2}$"),
              A1("$15 \\times 10$"),
              A1("$150$")],
             answer="$150$",
             solution=("$$\\binom{6}{2}\\binom{5}{2} = 15 \\times 10 = 150.$$"),
             verify=["Eq(binomial(6, 2)*binomial(5, 2), 150)"]),
    ]))

# ── Q2 [6] stats_probability: selection without replacement ──────────────
assert binomial(5, 2) / binomial(8, 2) == Rational(5, 14)
assert (5 * 3) / binomial(8, 2) == Rational(15, 28)
QS.append(question(
    "IB-AAHL-P1-T2-Q2", 2, "A", "stats_probability", "probability_basics",
    contextIntro=("A bag contains $5$ red counters and $3$ blue counters."
                  " Two counters are drawn at random, without replacement."),
    parts=[
        part("a", "Find the probability that both counters are red.", 3,
             [M1("$\\dfrac{\\binom{5}{2}}{\\binom{8}{2}}$ (or "
                 "$\\tfrac58 \\cdot \\tfrac47$)"),
              A1("$\\dfrac{10}{28}$"),
              A1("$\\dfrac{5}{14}$")],
             answer="$\\dfrac{5}{14}$",
             solution=("$$P(RR) = \\frac{\\binom{5}{2}}{\\binom{8}{2}} "
                       "= \\frac{10}{28} = \\frac{5}{14}.$$"),
             verify=["Eq(binomial(5, 2)/binomial(8, 2), Rational(5, 14))"]),
        part("b", "Find the probability that exactly one counter is red.", 3,
             [M1("one red and one blue: $\\dfrac{\\binom{5}{1}\\binom{3}{1}}"
                 "{\\binom{8}{2}}$"),
              A1("$\\dfrac{15}{28}$"),
              A1("accept equivalent working $2 \\cdot \\tfrac58 \\cdot "
                 "\\tfrac37$")],
             answer="$\\dfrac{15}{28}$",
             solution=("$$P(\\text{one red}) = \\frac{\\binom{5}{1}"
                       "\\binom{3}{1}}{\\binom{8}{2}} = \\frac{15}{28}.$$"),
             verify=["Eq((5*3)/binomial(8, 2), Rational(15, 28))"]),
    ]))

# ── Q3 [9] functions: rational function, asymptotes, no stationary point ─
f3 = (x ** 2 - 4) / (x - 1)
# oblique asymptote: x + 1 with remainder -3/(x-1)
assert simplify(f3 - (x + 1 - 3 / (x - 1))) == 0
fp3 = simplify(diff(f3, x))              # (x^2 - 2x + 4)/(x-1)^2
assert simplify(fp3 - (x ** 2 - 2 * x + 4) / (x - 1) ** 2) == 0
assert (-2) ** 2 - 4 * 1 * 4 == -12      # discriminant of numerator < 0
QS.append(question(
    "IB-AAHL-P1-T2-Q3", 3, "A", "functions", "rational_functions",
    contextIntro=("The function $f$ is defined by "
                  "$f(x) = \\dfrac{x^2 - 4}{x - 1}$, $x \\ne 1$."),
    parts=[
        part("a", "Write down the equation of the vertical asymptote, and"
             " find the equation of the oblique (slant) asymptote.", 3,
             [A1("vertical asymptote $x = 1$"),
              M1("divide: $\\dfrac{x^2 - 4}{x - 1} = x + 1 - "
                 "\\dfrac{3}{x - 1}$"),
              A1("oblique asymptote $y = x + 1$")],
             answer="$x = 1$ and $y = x + 1$",
             solution=("Polynomial division gives"
                       "$$f(x) = x + 1 - \\frac{3}{x - 1},$$"
                       " so the vertical asymptote is $x = 1$ and the oblique"
                       " asymptote is $y = x + 1$."),
             verify=["Eq(simplify((x**2 - 4)/(x - 1) - (x + 1 - 3/(x - 1))),"
                     " 0)"]),
        part("b", "Find the coordinates of the points where the graph of $f$"
             " meets the axes.", 2,
             [A1("$x$-intercepts $(2, 0)$ and $(-2, 0)$"),
              A1("$y$-intercept $(0, 4)$")],
             answer="$(2, 0)$, $(-2, 0)$, $(0, 4)$",
             solution=("$f(x) = 0$ when $x^2 - 4 = 0$, i.e. $x = \\pm 2$;"
                       " and $f(0) = \\dfrac{-4}{-1} = 4$."),
             verify=["Eq((2**2 - 4), 0)", "Eq(((-2)**2 - 4), 0)",
                     "Eq((0**2 - 4)/(0 - 1), 4)"]),
        part("c", "Show that $f$ has no stationary points.", 4,
             [M1("use the quotient rule"),
              A1("$f'(x) = \\dfrac{x^2 - 2x + 4}{(x - 1)^2}$"),
              M1("stationary points need the numerator $= 0$"),
              AG("the discriminant $(-2)^2 - 4(4) = -12 < 0$, so there are"
                 " no real solutions")],
             answer="no stationary points (numerator has no real zeros)",
             solution=("By the quotient rule,"
                       "$$f'(x) = \\frac{2x(x - 1) - (x^2 - 4)}{(x - 1)^2} "
                       "= \\frac{x^2 - 2x + 4}{(x - 1)^2}.$$"
                       " A stationary point needs $x^2 - 2x + 4 = 0$, but its"
                       " discriminant is $(-2)^2 - 4(1)(4) = -12 < 0$, so"
                       " there are no real solutions and hence no stationary"
                       " points."),
             verify=["Eq(simplify(diff((x**2 - 4)/(x - 1), x)"
                     " - (x**2 - 2*x + 4)/(x - 1)**2), 0)",
                     "Eq((-2)**2 - 4*4, -12)"]),
    ]))

# ── Q4 [6] number_algebra: complex numbers (Cartesian + polar) ───────────
z4 = 2 - 2 * I
assert Abs(z4) == 2 * sqrt(2)
assert arg(z4) == -pi / 4
assert expand(z4 ** 2) == -8 * I
QS.append(question(
    "IB-AAHL-P1-T2-Q4", 4, "A", "number_algebra", "complex_numbers",
    contextIntro=("Let $z = 2 - 2i$."),
    parts=[
        part("a", "Find $|z|$ and $\\arg z$.", 3,
             [A1("$|z| = \\sqrt{2^2 + 2^2} = 2\\sqrt{2}$"),
              M1("$z$ lies in the fourth quadrant, $\\tan(\\arg z) = -1$"),
              A1("$\\arg z = -\\dfrac{\\pi}{4}$")],
             answer="$|z| = 2\\sqrt{2}$, $\\arg z = -\\dfrac{\\pi}{4}$",
             solution=("$$|z| = \\sqrt{2^2 + (-2)^2} = \\sqrt{8} = 2\\sqrt{2},"
                       "\\qquad \\arg z = -\\frac{\\pi}{4}.$$"),
             verify=["Eq(Abs(2 - 2*I), 2*sqrt(2))",
                     "Eq(arg(2 - 2*I), -pi/4)"]),
        part("b", "Write $z$ in the form $r\\,\\text{cis}\\,\\theta$.", 1,
             [A1("$z = 2\\sqrt{2}\\,\\operatorname{cis}\\!\\left("
                 "-\\dfrac{\\pi}{4}\\right)$")],
             answer="$z = 2\\sqrt{2}\\,\\operatorname{cis}\\!\\left("
                    "-\\dfrac{\\pi}{4}\\right)$",
             solution=("$$z = 2\\sqrt{2}\\left(\\cos\\!\\left(-\\tfrac{\\pi}"
                       "{4}\\right) + i\\sin\\!\\left(-\\tfrac{\\pi}{4}"
                       "\\right)\\right).$$"),
             verify=["Eq(2*sqrt(2)*cos(-pi/4), 2)",
                     "Eq(2*sqrt(2)*sin(-pi/4), -2)"]),
        part("c", "Find $z^2$, giving your answer in the form $a + bi$.", 2,
             [M1("expand $(2 - 2i)^2$"),
              A1("$z^2 = -8i$")],
             answer="$z^2 = -8i$",
             solution=("$$z^2 = (2 - 2i)^2 = 4 - 8i + 4i^2 = 4 - 8i - 4 "
                       "= -8i.$$"),
             verify=["Eq(expand((2 - 2*I)**2), -8*I)"]),
    ]))

# ── Q5 [8] geometry_trig: trig equation reduced to a quadratic in cos ────
# 2 sin^2 x - 3 cos x = 0  ->  2 cos^2 x + 3 cos x - 2 = 0
assert expand(2 * (1 - cos(x) ** 2) - 3 * cos(x)) == \
    expand(-(2 * cos(x) ** 2 + 3 * cos(x) - 2))
assert solve(Eq(2 * k ** 2 + 3 * k - 2, 0), k) == [-2, Rational(1, 2)]
assert simplify(2 * sin(pi / 3) ** 2 - 3 * cos(pi / 3)) == 0
assert simplify(2 * sin(5 * pi / 3) ** 2 - 3 * cos(5 * pi / 3)) == 0
QS.append(question(
    "IB-AAHL-P1-T2-Q5", 5, "A", "geometry_trig", "trig_equations",
    contextIntro=("Consider the equation $2\\sin^2 x - 3\\cos x = 0$ for"
                  " $0 \\le x \\le 2\\pi$."),
    parts=[
        part("a", "Show that the equation can be written as"
             " $2\\cos^2 x + 3\\cos x - 2 = 0$.", 2,
             [M1("replace $\\sin^2 x$ with $1 - \\cos^2 x$"),
              AG("$2(1 - \\cos^2 x) - 3\\cos x = 0 \\Rightarrow "
                 "2\\cos^2 x + 3\\cos x - 2 = 0$")],
             answer="$2\\cos^2 x + 3\\cos x - 2 = 0$",
             solution=("$$2(1 - \\cos^2 x) - 3\\cos x = 0 \\Rightarrow "
                       "-2\\cos^2 x - 3\\cos x + 2 = 0 \\Rightarrow "
                       "2\\cos^2 x + 3\\cos x - 2 = 0.$$"),
             verify=["Eq(expand(2*(1 - cos(x)**2) - 3*cos(x)),"
                     " expand(-(2*cos(x)**2 + 3*cos(x) - 2)))"]),
        part("b", "Hence solve $2\\cos^2 x + 3\\cos x - 2 = 0$ for"
             " $\\cos x$.", 3,
             [M1("factor: $(2\\cos x - 1)(\\cos x + 2) = 0$"),
              A1("$\\cos x = \\dfrac{1}{2}$ or $\\cos x = -2$"),
              R1("reject $\\cos x = -2$ (outside $[-1, 1]$)")],
             answer="$\\cos x = \\dfrac{1}{2}$",
             solution=("$$(2\\cos x - 1)(\\cos x + 2) = 0 \\Rightarrow "
                       "\\cos x = \\tfrac12 \\text{ or } \\cos x = -2.$$"
                       " Since $-1 \\le \\cos x \\le 1$, only $\\cos x = "
                       "\\tfrac12$ is valid."),
             verify=["Eq(expand((2*k - 1)*(k + 2)), 2*k**2 + 3*k - 2)",
                     "Eq(2*Rational(1, 2)**2 + 3*Rational(1, 2) - 2, 0)"]),
        part("c", "Find all solutions of the original equation in"
             " $0 \\le x \\le 2\\pi$.", 3,
             [M1("$\\cos x = \\tfrac12$ in $[0, 2\\pi]$"),
              A1("$x = \\dfrac{\\pi}{3}$"),
              A1("$x = \\dfrac{5\\pi}{3}$")],
             answer="$x = \\dfrac{\\pi}{3}$ and $x = \\dfrac{5\\pi}{3}$",
             solution=("$$\\cos x = \\frac12 \\Rightarrow x = \\frac{\\pi}{3}"
                       " \\text{ or } x = 2\\pi - \\frac{\\pi}{3} = "
                       "\\frac{5\\pi}{3}.$$"),
             verify=["Eq(simplify(2*sin(pi/3)**2 - 3*cos(pi/3)), 0)",
                     "Eq(simplify(2*sin(5*pi/3)**2 - 3*cos(5*pi/3)), 0)"]),
    ]))

# ── Q6 [8] calculus: related rates (sphere) ──────────────────────────────
# dV/dt = 100 cm^3/s ; V = 4/3 pi r^3 ; A = 4 pi r^2
assert diff(Rational(4, 3) * pi * x ** 3, x) == 4 * pi * x ** 2
assert simplify(100 / (4 * pi * 25) - 1 / pi) == 0
assert diff(4 * pi * x ** 2, x).subs(x, 5) * (1 / pi) == 40
QS.append(question(
    "IB-AAHL-P1-T2-Q6", 6, "A", "calculus", "related_rates",
    contextIntro=("A spherical balloon is being inflated so that its volume"
                  " increases at a constant rate of $100$ cm$^3$ s$^{-1}$."
                  " The volume is $V = \\tfrac{4}{3}\\pi r^3$ and the surface"
                  " area is $A = 4\\pi r^2$, where $r$ is the radius in cm."),
    parts=[
        part("a", "Find $\\dfrac{dV}{dr}$.", 2,
             [M1("differentiate $V$ with respect to $r$"),
              A1("$\\dfrac{dV}{dr} = 4\\pi r^2$")],
             answer="$\\dfrac{dV}{dr} = 4\\pi r^2$",
             solution=("$$\\frac{dV}{dr} = 4\\pi r^2.$$"),
             verify=["Eq(diff(Rational(4, 3)*pi*x**3, x), 4*pi*x**2)"]),
        part("b", "Find the rate at which the radius is increasing at the"
             " instant when $r = 5$.", 3,
             [M1("chain rule: $\\dfrac{dr}{dt} = \\dfrac{dV/dt}{dV/dr}$"),
              A1("$\\dfrac{100}{4\\pi(25)}$"),
              A1("$\\dfrac{dr}{dt} = \\dfrac{1}{\\pi}$ cm s$^{-1}$")],
             answer="$\\dfrac{1}{\\pi}$ cm s$^{-1}$",
             solution=("$$\\frac{dr}{dt} = \\frac{dV/dt}{dV/dr} = "
                       "\\frac{100}{4\\pi(5)^2} = \\frac{100}{100\\pi} = "
                       "\\frac{1}{\\pi}.$$"),
             verify=["Eq(100/(4*pi*25), 1/pi)"]),
        part("c", "Find the rate at which the surface area is increasing at"
             " the instant when $r = 5$.", 3,
             [M1("$\\dfrac{dA}{dt} = \\dfrac{dA}{dr}\\cdot\\dfrac{dr}{dt}$"
                 " with $\\dfrac{dA}{dr} = 8\\pi r$"),
              A1("$8\\pi(5)\\cdot\\dfrac{1}{\\pi}$"),
              A1("$\\dfrac{dA}{dt} = 40$ cm$^2$ s$^{-1}$")],
             answer="$40$ cm$^2$ s$^{-1}$",
             solution=("$$\\frac{dA}{dr} = 8\\pi r, \\qquad \\frac{dA}{dt} "
                       "= 8\\pi(5)\\cdot\\frac{1}{\\pi} = 40 \\text{ cm}^2"
                       "\\text{ s}^{-1}.$$"),
             verify=["Eq(diff(4*pi*x**2, x).subs(x, 5)*(1/pi), 40)"]),
    ]))

# ── Q7 [9] stats_probability: exact binomial B(4, 1/3) ───────────────────
p7 = Rational(1, 3)
assert binomial(4, 2) * p7 ** 2 * (1 - p7) ** 2 == Rational(8, 27)
assert 1 - (1 - p7) ** 4 == Rational(65, 81)
assert 4 * p7 == Rational(4, 3)
assert 4 * p7 * (1 - p7) == Rational(8, 9)
QS.append(question(
    "IB-AAHL-P1-T2-Q7", 7, "A", "stats_probability", "binomial_distribution",
    contextIntro=("A spinner lands on green with probability $\\dfrac{1}{3}$"
                  " on each spin, independently. The spinner is spun $4$"
                  " times, and $X$ is the number of greens, so "
                  "$X \\sim B\\!\\left(4, \\tfrac13\\right)$."),
    parts=[
        part("a", "Find $P(X = 2)$.", 2,
             [M1("$\\binom{4}{2}\\left(\\tfrac13\\right)^2"
                 "\\left(\\tfrac23\\right)^2$"),
              A1("$P(X = 2) = \\dfrac{8}{27}$")],
             answer="$\\dfrac{8}{27}$",
             solution=("$$P(X = 2) = \\binom{4}{2}\\left(\\frac13\\right)^2"
                       "\\left(\\frac23\\right)^2 = 6\\cdot\\frac19\\cdot"
                       "\\frac49 = \\frac{8}{27}.$$"),
             verify=["Eq(binomial(4, 2)*Rational(1, 3)**2*Rational(2, 3)**2,"
                     " Rational(8, 27))"]),
        part("b", "Find $P(X \\ge 1)$.", 3,
             [M1("use the complement $1 - P(X = 0)$"),
              A1("$P(X = 0) = \\left(\\tfrac23\\right)^4 = \\tfrac{16}{81}$"),
              A1("$P(X \\ge 1) = \\dfrac{65}{81}$")],
             answer="$\\dfrac{65}{81}$",
             solution=("$$P(X \\ge 1) = 1 - \\left(\\frac23\\right)^4 = "
                       "1 - \\frac{16}{81} = \\frac{65}{81}.$$"),
             verify=["Eq(1 - Rational(2, 3)**4, Rational(65, 81))"]),
        part("c", "Find $E(X)$.", 2,
             [M1("use $E(X) = np$"),
              A1("$E(X) = \\dfrac{4}{3}$")],
             answer="$\\dfrac{4}{3}$",
             solution=("$$E(X) = np = 4\\cdot\\frac13 = \\frac43.$$"),
             verify=["Eq(4*Rational(1, 3), Rational(4, 3))"]),
        part("d", "Find $\\operatorname{Var}(X)$.", 2,
             [M1("use $\\operatorname{Var}(X) = np(1 - p)$"),
              A1("$\\operatorname{Var}(X) = \\dfrac{8}{9}$")],
             answer="$\\dfrac{8}{9}$",
             solution=("$$\\operatorname{Var}(X) = np(1 - p) = "
                       "4\\cdot\\frac13\\cdot\\frac23 = \\frac89.$$"),
             verify=["Eq(4*Rational(1, 3)*Rational(2, 3), Rational(8, 9))"]),
    ]))

# ── Q8 [21] geometry_trig (Section B): skew lines in 3D ──────────────────
d1 = Matrix([1, 0, 1])
d2 = Matrix([0, 1, 1])
a1 = Matrix([1, 0, 2])
a2 = Matrix([0, 1, 0])
assert d1.dot(d2) == 1
assert d1.norm() == sqrt(2) and d2.norm() == sqrt(2)
cross = d1.cross(d2)
assert list(cross) == [-1, -1, 1]
assert cross.norm() == sqrt(3)
sepdot = (a2 - a1).dot(cross)
assert sepdot == -2
# common perpendicular feet
lam, mu = symbols("lam mu")
P8 = a1 + lam * d1
Q8 = a2 + mu * d2
solPQ = solve([(Q8 - P8).dot(d1), (Q8 - P8).dot(d2)], [lam, mu])
assert solPQ[lam] == Rational(-5, 3) and solPQ[mu] == Rational(-1, 3)
Pcoord = a1 + solPQ[lam] * d1
Qcoord = a2 + solPQ[mu] * d2
assert list(Pcoord) == [Rational(-2, 3), 0, Rational(1, 3)]
assert list(Qcoord) == [0, Rational(2, 3), Rational(-1, 3)]
QS.append(question(
    "IB-AAHL-P1-T2-Q8", 8, "B", "geometry_trig", "vectors_lines",
    contextIntro=("Two lines are given by "
                  "$L_1: \\mathbf{r} = \\begin{pmatrix}1\\\\0\\\\2"
                  "\\end{pmatrix} + \\lambda\\begin{pmatrix}1\\\\0\\\\1"
                  "\\end{pmatrix}$ and "
                  "$L_2: \\mathbf{r} = \\begin{pmatrix}0\\\\1\\\\0"
                  "\\end{pmatrix} + \\mu\\begin{pmatrix}0\\\\1\\\\1"
                  "\\end{pmatrix}$."),
    parts=[
        part("a", "Find the acute angle between the two lines.", 3,
             [M1("$\\cos\\theta = \\dfrac{|\\mathbf{d}_1\\cdot\\mathbf{d}_2|}"
                 "{|\\mathbf{d}_1||\\mathbf{d}_2|}$"),
              A1("$\\mathbf{d}_1\\cdot\\mathbf{d}_2 = 1$, "
                 "$|\\mathbf{d}_1| = |\\mathbf{d}_2| = \\sqrt2$"),
              A1("$\\cos\\theta = \\dfrac12 \\Rightarrow \\theta = 60^\\circ$")],
             answer="$60^\\circ$",
             solution=("$$\\cos\\theta = \\frac{|(1)(0)+(0)(1)+(1)(1)|}"
                       "{\\sqrt2\\,\\sqrt2} = \\frac12 \\Rightarrow \\theta "
                       "= 60^\\circ.$$"),
             verify=["Eq(Matrix([1,0,1]).dot(Matrix([0,1,1])), 1)",
                     "Eq(Matrix([1,0,1]).norm(), sqrt(2))"]),
        part("b", "Show that $L_1$ and $L_2$ do not intersect, and hence"
             " that they are skew.", 4,
             [M1("equate components: $1 + \\lambda = 0$, $0 = 1 + \\mu$,"
                 " $2 + \\lambda = \\mu$"),
              A1("first two give $\\lambda = -1$, $\\mu = -1$"),
              M1("test in the third equation: $2 + (-1) = 1 \\ne -1$"),
              AG("no consistent $(\\lambda, \\mu)$, and the directions are"
                 " not parallel, so the lines are skew")],
             answer="the lines are skew",
             solution=("Equating components: $1+\\lambda = 0$ gives "
                       "$\\lambda = -1$; $0 = 1+\\mu$ gives $\\mu = -1$. The"
                       " third equation would need $2 + (-1) = -1$, i.e. "
                       "$1 = -1$, which is false. The directions "
                       "$(1,0,1)$ and $(0,1,1)$ are not parallel, so the"
                       " lines neither intersect nor are parallel: they are"
                       " skew."),
             verify=["Eq(1 + (-1), 0)", "Eq(2 + (-1), 1)", "1 != -1"]),
        part("c", "Find $\\mathbf{d}_1 \\times \\mathbf{d}_2$.", 3,
             [M1("evaluate the vector-product determinant"),
              A1("components $(0\\cdot1 - 1\\cdot1,\\; 1\\cdot0 - 1\\cdot1,"
                 "\\; 1\\cdot1 - 0\\cdot0)$"),
              A1("$\\mathbf{d}_1\\times\\mathbf{d}_2 = "
                 "\\begin{pmatrix}-1\\\\-1\\\\1\\end{pmatrix}$")],
             answer="$(-1, -1, 1)$",
             solution=("$$\\mathbf{d}_1\\times\\mathbf{d}_2 = "
                       "\\begin{vmatrix}\\mathbf{i}&\\mathbf{j}&\\mathbf{k}"
                       "\\\\1&0&1\\\\0&1&1\\end{vmatrix} = (-1, -1, 1).$$"),
             verify=["Eq(0*1 - 1*1, -1)", "Eq(1*0 - 1*1, -1)",
                     "Eq(1*1 - 0*0, 1)"]),
        part("d", "Hence find the shortest distance between $L_1$ and"
             " $L_2$.", 4,
             [M1("$\\text{dist} = \\dfrac{|(\\mathbf{a}_2 - \\mathbf{a}_1)"
                 "\\cdot(\\mathbf{d}_1\\times\\mathbf{d}_2)|}"
                 "{|\\mathbf{d}_1\\times\\mathbf{d}_2|}$"),
              A1("$\\mathbf{a}_2 - \\mathbf{a}_1 = (-1, 1, -2)$, dot "
                 "$= -2$"),
              A1("$|\\mathbf{d}_1\\times\\mathbf{d}_2| = \\sqrt3$"),
              A1("$\\text{dist} = \\dfrac{2}{\\sqrt3} = "
                 "\\dfrac{2\\sqrt3}{3}$")],
             answer="$\\dfrac{2\\sqrt3}{3}$",
             solution=("With $\\mathbf{a}_2 - \\mathbf{a}_1 = (-1, 1, -2)$,"
                       "$$\\text{dist} = \\frac{|(-1,1,-2)\\cdot(-1,-1,1)|}"
                       "{\\sqrt3} = \\frac{|-2|}{\\sqrt3} = \\frac{2}"
                       "{\\sqrt3} = \\frac{2\\sqrt3}{3}.$$"),
             verify=["Eq(Matrix([-1,1,-2]).dot(Matrix([-1,-1,1])), -2)",
                     "Eq(Matrix([-1,-1,1]).norm(), sqrt(3))"]),
        part("e", "Find the coordinates of the points $P$ on $L_1$ and $Q$"
             " on $L_2$ such that $[PQ]$ is perpendicular to both lines.", 7,
             [M1("write $P = (1+\\lambda,\\,0,\\,2+\\lambda)$ and "
                 "$Q = (0,\\,1+\\mu,\\,\\mu)$"),
              M1("set $\\vec{PQ}\\cdot\\mathbf{d}_1 = 0$ and "
                 "$\\vec{PQ}\\cdot\\mathbf{d}_2 = 0$"),
              A1("$\\lambda = -\\dfrac53$"),
              A1("$\\mu = -\\dfrac13$"),
              A1("$P = \\left(-\\dfrac23,\\,0,\\,\\dfrac13\\right)$"),
              A1("$Q = \\left(0,\\,\\dfrac23,\\,-\\dfrac13\\right)$"),
              R1("check: $|\\vec{PQ}| = \\dfrac{2\\sqrt3}{3}$ matches part"
                 " (d)")],
             answer="$P\\left(-\\tfrac23, 0, \\tfrac13\\right)$,"
                    " $Q\\left(0, \\tfrac23, -\\tfrac13\\right)$",
             solution=("Let $\\vec{PQ} = Q - P$. Imposing "
                       "$\\vec{PQ}\\cdot\\mathbf{d}_1 = 0$ and "
                       "$\\vec{PQ}\\cdot\\mathbf{d}_2 = 0$ gives "
                       "$\\lambda = -\\tfrac53$, $\\mu = -\\tfrac13$, so"
                       "$$P = \\left(-\\tfrac23,\\,0,\\,\\tfrac13\\right),"
                       "\\qquad Q = \\left(0,\\,\\tfrac23,\\,-\\tfrac13"
                       "\\right).$$"
                       " Then $\\vec{PQ} = \\left(\\tfrac23, \\tfrac23, "
                       "-\\tfrac23\\right)$ with $|\\vec{PQ}| = \\tfrac{2}"
                       "{\\sqrt3}$, confirming part (d)."),
             verify=["Eq(Matrix([1, 0, 2]) + Rational(-5, 3)*Matrix([1,0,1])"
                     " - Matrix([Rational(-2,3), 0, Rational(1,3)]),"
                     " Matrix([0, 0, 0]))",
                     "Eq(Matrix([0, 1, 0]) + Rational(-1, 3)*Matrix([0,1,1])"
                     " - Matrix([0, Rational(2,3), Rational(-1,3)]),"
                     " Matrix([0, 0, 0]))"]),
    ]))

# ── Q9 [20] calculus (Section B): substitution + volume of revolution ────
g9 = x / sqrt(x ** 2 + 4)
anti9 = sqrt(x ** 2 + 4)
assert simplify(diff(anti9, x) - g9) == 0
xhi = 2 * sqrt(3)
area9 = integrate(g9, (x, 0, xhi))
assert simplify(area9 - 2) == 0
assert simplify(x ** 2 / (x ** 2 + 4) - (1 - 4 / (x ** 2 + 4))) == 0
anti9b = x - 2 * atan(x / 2)
assert simplify(diff(anti9b, x) - x ** 2 / (x ** 2 + 4)) == 0
vol9 = pi * integrate(x ** 2 / (x ** 2 + 4), (x, 0, xhi))
assert simplify(vol9 - pi * (2 * sqrt(3) - 2 * pi / 3)) == 0
QS.append(question(
    "IB-AAHL-P1-T2-Q9", 9, "B", "calculus", "integration_substitution",
    contextIntro=("The curve $C$ has equation $y = \\dfrac{x}"
                  "{\\sqrt{x^2 + 4}}$ for $x \\ge 0$. The diagram shows the"
                  " region $R$ bounded by $C$, the $x$-axis and the line"
                  " $x = 2\\sqrt{3}$."),
    figure=png("ib-aahl-p1-t2-q9.png",
               "Curve y = x / sqrt(x^2 + 4) rising from the origin toward its "
               "horizontal asymptote y = 1; the region R between the curve, "
               "the x-axis and the vertical line x = 2 sqrt 3 is shaded."),
    parts=[
        part("a", "Using the substitution $u = x^2 + 4$, find "
             "$\\displaystyle\\int \\frac{x}{\\sqrt{x^2 + 4}}\\,dx$.", 3,
             [M1("$u = x^2 + 4 \\Rightarrow du = 2x\\,dx$"),
              A1("$\\tfrac12\\displaystyle\\int u^{-1/2}\\,du = u^{1/2}$"),
              A1("$\\sqrt{x^2 + 4} + C$")],
             answer="$\\sqrt{x^2 + 4} + C$",
             solution=("With $u = x^2 + 4$, $du = 2x\\,dx$:"
                       "$$\\int \\frac{x}{\\sqrt{x^2+4}}\\,dx = \\frac12"
                       "\\int u^{-1/2}\\,du = u^{1/2} + C = \\sqrt{x^2 + 4}"
                       " + C.$$"),
             verify=["Eq(simplify(diff(sqrt(x**2 + 4), x)"
                     " - x/sqrt(x**2 + 4)), 0)"]),
        part("b", "Hence find the area of the region $R$.", 3,
             [M1("area $= \\Big[\\sqrt{x^2 + 4}\\Big]_0^{2\\sqrt3}$"),
              A1("$\\sqrt{16} - \\sqrt{4} = 4 - 2$"),
              A1("area $= 2$")],
             answer="area $= 2$",
             solution=("$$\\int_0^{2\\sqrt3}\\frac{x}{\\sqrt{x^2+4}}\\,dx = "
                       "\\Big[\\sqrt{x^2+4}\\Big]_0^{2\\sqrt3} = \\sqrt{16} "
                       "- \\sqrt{4} = 4 - 2 = 2.$$"),
             verify=["Eq(simplify(integrate(x/sqrt(x**2 + 4),"
                     " (x, 0, 2*sqrt(3)))), 2)"]),
        part("c", "Show that $\\dfrac{x^2}{x^2 + 4} = 1 - \\dfrac{4}"
             "{x^2 + 4}$.", 4,
             [M1("write $x^2 = (x^2 + 4) - 4$"),
              A1("$\\dfrac{(x^2 + 4) - 4}{x^2 + 4}$"),
              M1("split the fraction"),
              AG("$1 - \\dfrac{4}{x^2 + 4}$")],
             answer="$1 - \\dfrac{4}{x^2 + 4}$",
             solution=("$$\\frac{x^2}{x^2 + 4} = \\frac{(x^2 + 4) - 4}"
                       "{x^2 + 4} = 1 - \\frac{4}{x^2 + 4}.$$"),
             verify=["Eq(simplify(x**2/(x**2 + 4)"
                     " - (1 - 4/(x**2 + 4))), 0)"]),
        part("d", "Hence find $\\displaystyle\\int \\frac{x^2}{x^2 + 4}"
             "\\,dx$.", 4,
             [M1("integrate $1 - \\dfrac{4}{x^2 + 4}$ term by term"),
              A1("$\\displaystyle\\int\\frac{4}{x^2 + 4}\\,dx = "
                 "2\\arctan\\frac{x}{2}$"),
              A1("combine the two integrals"),
              A1("$x - 2\\arctan\\dfrac{x}{2} + C$")],
             answer="$x - 2\\arctan\\dfrac{x}{2} + C$",
             solution=("Using part (c) and the standard result "
                       "$\\int\\frac{1}{x^2 + a^2}dx = \\frac1a\\arctan"
                       "\\frac xa$ with $a = 2$:"
                       "$$\\int\\frac{x^2}{x^2+4}\\,dx = \\int\\left(1 - "
                       "\\frac{4}{x^2+4}\\right)dx = x - 2\\arctan\\frac{x}"
                       "{2} + C.$$"),
             verify=["Eq(simplify(diff(x - 2*atan(x/2), x)"
                     " - x**2/(x**2 + 4)), 0)"]),
        part("e", "Find the exact volume of the solid formed when $R$ is"
             " rotated through $2\\pi$ about the $x$-axis.", 6,
             [M1("volume $= \\pi\\displaystyle\\int_0^{2\\sqrt3} y^2\\,dx$"),
              A1("$y^2 = \\dfrac{x^2}{x^2 + 4}$"),
              M1("use part (d): $\\pi\\Big[x - 2\\arctan\\tfrac{x}{2}"
                 "\\Big]_0^{2\\sqrt3}$"),
              A1("$\\arctan\\sqrt3 = \\dfrac{\\pi}{3}$"),
              A1("$\\pi\\left(2\\sqrt3 - 2\\cdot\\tfrac{\\pi}{3}\\right)$"),
              A1("volume $= \\pi\\left(2\\sqrt3 - \\dfrac{2\\pi}{3}\\right)$")],
             answer="$\\pi\\left(2\\sqrt3 - \\dfrac{2\\pi}{3}\\right)$",
             solution=("$$V = \\pi\\int_0^{2\\sqrt3}\\frac{x^2}{x^2+4}\\,dx "
                       "= \\pi\\Big[x - 2\\arctan\\tfrac{x}{2}\\Big]_0"
                       "^{2\\sqrt3}.$$"
                       " Since $\\arctan\\sqrt3 = \\tfrac{\\pi}{3}$,"
                       "$$V = \\pi\\left(2\\sqrt3 - 2\\cdot\\frac{\\pi}{3}"
                       "\\right) = \\pi\\left(2\\sqrt3 - \\frac{2\\pi}{3}"
                       "\\right).$$"),
             verify=["Eq(simplify(pi*integrate(x**2/(x**2 + 4),"
                     " (x, 0, 2*sqrt(3))) - pi*(2*sqrt(3) - 2*pi/3)), 0)",
                     "Eq(atan(sqrt(3)), pi/3)"]),
    ]))

# ── Q10 [18] number_algebra (Section B): two proofs by induction ─────────
assert sum(r ** 2 for r in range(1, 6)) == Rational(5 * 6 * 11, 6)
assert sum(r ** 2 for r in range(11, 21)) == 2485
assert (6 ** 1 + 4) % 5 == 0
QS.append(question(
    "IB-AAHL-P1-T2-Q10", 10, "B", "number_algebra", "proof",
    parts=[
        part("a", "Prove by mathematical induction that "
             "$\\displaystyle\\sum_{r=1}^{n} r^2 = \\frac{n(n + 1)(2n + 1)}"
             "{6}$ for all $n \\in \\mathbb{Z}^{+}$.", 8,
             [R1("base case $n = 1$: LHS $= 1$, RHS $= \\tfrac{1\\cdot2\\cdot3}"
                 "{6} = 1$ — true"),
              M1("assume true for $n = k$: $\\sum_{r=1}^{k} r^2 = "
                 "\\tfrac{k(k+1)(2k+1)}{6}$"),
              M1("consider $n = k + 1$: add $(k + 1)^2$"),
              A1("$\\tfrac{k(k+1)(2k+1)}{6} + (k+1)^2$"),
              M1("factor out $\\tfrac{k+1}{6}$"),
              A1("$\\tfrac{(k+1)\\big[k(2k+1) + 6(k+1)\\big]}{6} = "
                 "\\tfrac{(k+1)(2k^2 + 7k + 6)}{6}$"),
              A1("$= \\tfrac{(k+1)(k+2)(2k+3)}{6}$, the statement for "
                 "$n = k+1$"),
              R1("true for $n = 1$ and $k \\Rightarrow k+1$, so true for all"
                 " $n \\in \\mathbb{Z}^{+}$ by induction")],
             answer="proof by induction (see solution)",
             solution=("**Base case** $n = 1$: LHS $= 1^2 = 1$ and RHS $= "
                       "\\dfrac{1\\cdot2\\cdot3}{6} = 1$."
                       "**Inductive step**: assume $\\sum_{r=1}^{k} r^2 = "
                       "\\dfrac{k(k+1)(2k+1)}{6}$. Then"
                       "$$\\sum_{r=1}^{k+1} r^2 = \\frac{k(k+1)(2k+1)}{6} + "
                       "(k+1)^2 = \\frac{(k+1)\\big[k(2k+1)+6(k+1)\\big]}{6}$$"
                       "$$= \\frac{(k+1)(2k^2 + 7k + 6)}{6} = "
                       "\\frac{(k+1)(k+2)(2k+3)}{6},$$"
                       " which is the formula with $n = k+1$. By induction it"
                       " holds for all positive integers $n$."),
             verify=["Eq(expand((k + 1)*(2*k**2 + 7*k + 6)),"
                     " expand((k + 1)*(k + 2)*(2*k + 3)))",
                     "Eq(expand(k*(2*k + 1) + 6*(k + 1)), 2*k**2 + 7*k + 6)"]),
        part("b", "Hence find $\\displaystyle\\sum_{r=11}^{20} r^2$.", 3,
             [M1("$\\sum_{11}^{20} = \\sum_{1}^{20} - \\sum_{1}^{10}$"),
              A1("$\\tfrac{20\\cdot21\\cdot41}{6} - \\tfrac{10\\cdot11\\cdot21}"
                 "{6} = 2870 - 385$"),
              A1("$2485$")],
             answer="$2485$",
             solution=("$$\\sum_{r=11}^{20} r^2 = \\sum_{r=1}^{20} r^2 - "
                       "\\sum_{r=1}^{10} r^2 = \\frac{20\\cdot21\\cdot41}{6}"
                       " - \\frac{10\\cdot11\\cdot21}{6} = 2870 - 385 = "
                       "2485.$$"),
             verify=["Eq(Rational(20*21*41, 6) - Rational(10*11*21, 6),"
                     " 2485)"]),
        part("c", "Prove by mathematical induction that $6^{n} + 4$ is"
             " divisible by $5$ for all $n \\in \\mathbb{Z}^{+}$.", 7,
             [R1("base case $n = 1$: $6^1 + 4 = 10 = 5\\times 2$ — divisible"),
              M1("assume $6^{k} + 4 = 5m$ for some integer $m$"),
              M1("consider $6^{k+1} + 4 = 6\\cdot 6^{k} + 4$"),
              A1("$= 6(6^{k} + 4) - 20$"),
              A1("$= 6(5m) - 20 = 5(6m - 4)$"),
              R1("this is a multiple of $5$"),
              R1("true for $n = 1$ and $k \\Rightarrow k+1$, so true for all"
                 " $n \\in \\mathbb{Z}^{+}$ by induction")],
             answer="proof by induction (see solution)",
             solution=("**Base case** $n = 1$: $6^1 + 4 = 10$, divisible by"
                       " $5$."
                       "**Inductive step**: assume $6^{k} + 4 = 5m$ for some"
                       " integer $m$. Then"
                       "$$6^{k+1} + 4 = 6\\cdot 6^{k} + 4 = 6(6^{k} + 4) - "
                       "20 = 6(5m) - 20 = 5(6m - 4),$$"
                       " which is divisible by $5$. By induction $6^{n} + 4$"
                       " is divisible by $5$ for all positive integers $n$."),
             verify=["Eq((6**1 + 4) % 5, 0)", "Eq((6**2 + 4) % 5, 0)",
                     "Eq(6*(5*m) - 20, 5*(6*m - 4))"]),
    ]))

META = {"course": "aa", "level": "hl", "paper": 1, "testId": "ib-hl-practice-2",
        "label": "AA HL Practice Paper 1", "timeMinutes": 120,
        "totalMarks": 110, "calculator": False}

if __name__ == "__main__":
    write_paper(META, QS, "data/ib/aa-hl/ib-hl-practice-2/paper1.json")
