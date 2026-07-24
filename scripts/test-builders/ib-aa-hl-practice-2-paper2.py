"""AA HL Practice Paper 2 (ib-hl-practice-2) — 120 min, 110 marks, GDC required.

Blueprint (topic x marks):
    Section A (52): Q1 geometry_trig 7 | Q2 stats_probability 7
                    Q3 number_algebra 7 | Q4 functions 7
                    Q5 calculus 8       | Q6 functions 8
                    Q7 number_algebra 8
    Section B (58): Q8 stats_probability 19 | Q9 calculus 21
                    Q10 geometry_trig 18
    Paper totals: number_algebra 15 | functions 15 | geometry_trig 25 |
                  stats_probability 26 | calculus 29 = 110.

Fresh HL archetypes versus Set 1: cosine-rule triangle with an altitude,
binomial B(20, 0.3), a 3x3 linear system, a transcendental equation
e^x = 3x with two roots, area between two curves, x ln x optimisation,
complex powers via De Moivre, an expected-value die game feeding a
binomial, cylindrical-can optimisation with a second-derivative test,
and a two-leg bearings navigation problem. GDC conventions: exact or
3 s.f. Figures: Q1 (triangle), Q9 (can), Q10 (bearings).
"""
import os
import sys
from math import floor, log10

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, N, erf, exp, log, sin, cos,  # noqa: F401,E402
                   acos, asin, rad, deg, atan, integrate, diff, expand,
                   solve, simplify, binomial, symbols, Abs, cbrt, ln)

x, r = symbols("x r")


def sf3(v):
    v = float(v)
    assert v != 0
    d = 2 - floor(log10(abs(v)))
    rr = round(v, d)
    printed = str(int(rr)) if d <= 0 else f"{rr:.{d}f}"
    assert abs(v - rr) < 0.499 * 10 ** (-d), f"ambiguous 3sf rounding for {v}"
    return printed, 0.51 * 10 ** (-d)


def sig(v, n=6):
    v = float(v)
    d = (n - 1) - floor(log10(abs(v)))
    return f"{round(v, d):.{max(d, 0)}f}"


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [7] geometry_trig: cosine rule + area + altitude, FIGURE ──────────
# sides a=8, b=11, c=15; largest angle C opposite 15
cosC = Rational(8 ** 2 + 11 ** 2 - 15 ** 2, 2 * 8 * 11)
assert cosC == Rational(-40, 176)
angC = acos(cosC)
angC_p, angC_tol = sf3(N(deg(angC), 12))
assert angC_p == "103"
area1 = Rational(1, 2) * 8 * 11 * sin(angC)
area1_p, area1_tol = sf3(N(area1, 12))
assert area1_p == "42.8"
alt1 = 2 * area1 / 15
alt1_p, alt1_tol = sf3(N(alt1, 12))
assert alt1_p == "5.71"
QS.append(question(
    "IB-AAHL-P2-T2-Q1", 1, "A", "geometry_trig", "non_right_trig",
    contextIntro=("In triangle $ABC$, $AB = 15$, $BC = 8$ and $AC = 11$."),
    figure=png("ib-aahl-p2-t2-q1.png",
               "Triangle ABC with the longest side AB = 15 as the base, "
               "AC = 11 and BC = 8."),
    parts=[
        part("a", "Find the size of the largest angle of the triangle.", 3,
             [M1("the largest angle is opposite the longest side; cosine"
                 " rule $\\cos C = \\dfrac{8^2 + 11^2 - 15^2}{2(8)(11)}$"),
              A1("$\\cos C = -\\dfrac{40}{176}$"),
              A1(f"$C = {angC_p}^\\circ$ $({sig(N(deg(angC), 12))}\\ldots)$")],
             answer=f"$C = {angC_p}^\\circ$",
             solution=("$$\\cos C = \\frac{8^2 + 11^2 - 15^2}{2(8)(11)} = "
                       f"-\\frac{{40}}{{176}} \\Rightarrow C = "
                       f"{sig(N(deg(angC), 12))} \\approx {angC_p}^\\circ.$$"),
             verify=[f"Abs(deg(acos(Rational(-40, 176))) - {angC_p}) "
                     f"< {angC_tol}"]),
        part("b", "Find the area of the triangle.", 2,
             [M1("area $= \\tfrac12(8)(11)\\sin C$"),
              A1(f"area $= {area1_p}$ $({sig(N(area1, 12))}\\ldots)$")],
             answer=f"${area1_p}$",
             solution=("$$\\text{Area} = \\tfrac12(8)(11)\\sin C = "
                       f"{sig(N(area1, 12))} \\approx {area1_p}.$$"),
             verify=[f"Abs(Rational(1,2)*88*sin(acos(Rational(-40,176)))"
                     f" - {area1_p}) < {area1_tol}"]),
        part("c", "Find the shortest distance from $C$ to the side"
             " $[AB]$.", 2,
             [M1("area $= \\tfrac12 \\times AB \\times h$, so "
                 "$h = \\dfrac{2 \\times \\text{area}}{15}$"),
              A1(f"$h = {alt1_p}$")],
             answer=f"$h = {alt1_p}$",
             solution=("The shortest distance is the altitude to $[AB]$:"
                       f"$$h = \\frac{{2 \\times {sig(N(area1, 12))}}}{{15}} "
                       f"= {sig(N(alt1, 12))} \\approx {alt1_p}.$$"),
             verify=[f"Abs(2*Rational(1,2)*88*sin(acos(Rational(-40,176)))/15"
                     f" - {alt1_p}) < {alt1_tol}"]),
    ]))

# ── Q2 [7] stats_probability: binomial B(20, 0.3) ────────────────────────
p2 = Rational(3, 10)
pX6 = binomial(20, 6) * p2 ** 6 * (1 - p2) ** 14
pX6_p, pX6_tol = sf3(N(pX6, 15))
assert pX6_p == "0.192"
pGe8 = 1 - sum(binomial(20, k) * p2 ** k * (1 - p2) ** (20 - k) for k in range(8))
pGe8_p, pGe8_tol = sf3(N(pGe8, 15))
assert pGe8_p == "0.228"
# explicit (generator-free) sum string for the gate's verify re-check
CDF8 = " + ".join(f"binomial(20, {k})*Rational(3,10)**{k}"
                  f"*Rational(7,10)**{20 - k}" for k in range(8))
assert 20 * p2 == 6
assert 20 * p2 * (1 - p2) == Rational(21, 5)
QS.append(question(
    "IB-AAHL-P2-T2-Q2", 2, "A", "stats_probability", "binomial_distribution",
    contextIntro=("A factory produces components, $30\\%$ of which are"
                  " painted red. A random sample of $20$ components is taken."
                  " Let $X$ be the number that are red, so "
                  "$X \\sim B(20,\\, 0.3)$."),
    parts=[
        part("a", "Find $P(X = 6)$.", 2,
             [M1("binomial pdf (GDC)"),
              A1(f"$P(X = 6) = {pX6_p}$ $({sig(N(pX6, 12))}\\ldots)$")],
             answer=f"${pX6_p}$",
             solution=("$$P(X = 6) = \\binom{20}{6}(0.3)^6(0.7)^{14} = "
                       f"{sig(N(pX6, 12))} \\approx {pX6_p}.$$"),
             verify=[f"Abs(binomial(20, 6)*Rational(3,10)**6"
                     f"*Rational(7,10)**14 - {pX6_p}) < {pX6_tol}"]),
        part("b", "Find $P(X \\ge 8)$.", 3,
             [M1("use the complement $1 - P(X \\le 7)$ (GDC binomial cdf)"),
              A1("$P(X \\le 7) = 0.772\\ldots$"),
              A1(f"$P(X \\ge 8) = {pGe8_p}$ $({sig(N(pGe8, 12))}\\ldots)$")],
             answer=f"${pGe8_p}$",
             solution=("$$P(X \\ge 8) = 1 - P(X \\le 7) = "
                       f"{sig(N(pGe8, 12))} \\approx {pGe8_p}.$$"),
             verify=[f"Abs((1 - ({CDF8})) - {pGe8_p}) < {pGe8_tol}"]),
        part("c", "Find $E(X)$ and $\\operatorname{Var}(X)$.", 2,
             [A1("$E(X) = np = 6$"),
              A1("$\\operatorname{Var}(X) = np(1-p) = 4.2$")],
             answer="$E(X) = 6$, $\\operatorname{Var}(X) = 4.2$",
             solution=("$$E(X) = 20(0.3) = 6, \\qquad \\operatorname{Var}(X)"
                       " = 20(0.3)(0.7) = 4.2.$$"),
             verify=["Eq(20*Rational(3, 10), 6)",
                     "Eq(20*Rational(3, 10)*Rational(7, 10), Rational(21, 5))"]),
    ]))

# ── Q3 [7] number_algebra: 3x3 linear system (word problem) ──────────────
a, b, c = symbols("a b c")
sol3 = solve([Eq(a + b + c, 4), Eq(a - b + 2 * c, 9), Eq(2 * a + b - c, 0)],
             [a, b, c])
assert sol3[a] == 2 and sol3[b] == -1 and sol3[c] == 3
QS.append(question(
    "IB-AAHL-P2-T2-Q3", 3, "A", "number_algebra", "systems_equations",
    contextIntro=("The variables $x$, $y$ and $z$ satisfy the system"
                  " $$x + y + z = 4$$ $$x - y + 2z = 9$$ $$2x + y - z = 0.$$"),
    parts=[
        part("a", "Use technology to solve the system.", 5,
             [M1("enter the coefficient matrix and constants into the GDC"),
              A1("$x = 2$"),
              A1("$y = -1$"),
              A1("$z = 3$"),
              R1("verify in an equation, e.g. $2 + (-1) + 3 = 4$")],
             answer="$x = 2$, $y = -1$, $z = 3$",
             solution=("Solving with the GDC gives"
                       "$$x = 2, \\quad y = -1, \\quad z = 3.$$"
                       " Check: $2 - (-1) + 2(3) = 9$ and "
                       "$2(2) + (-1) - 3 = 0$."),
             verify=["Eq(2 + (-1) + 3, 4)", "Eq(2 - (-1) + 2*3, 9)",
                     "Eq(2*2 + (-1) - 3, 0)"]),
        part("b", "Hence write down the value of $x + 2y + 3z$.", 2,
             [M1("substitute the solution"),
              A1("$2 + 2(-1) + 3(3) = 9$")],
             answer="$9$",
             solution=("$$x + 2y + 3z = 2 + 2(-1) + 3(3) = 2 - 2 + 9 = 9.$$"),
             verify=["Eq(2 + 2*(-1) + 3*3, 9)"]),
    ]))

# ── Q4 [7] functions: transcendental equation e^x = 3x ───────────────────
r4a, r4b = 0.619061, 1.512135
r4a_p, r4a_tol = sf3(r4a)
r4b_p, r4b_tol = sf3(r4b)
assert r4a_p == "0.619" and r4b_p == "1.51"
assert exp(0) - 3 * 0 == 1 and float(N(exp(1) - 3 * 1)) < 0
QS.append(question(
    "IB-AAHL-P2-T2-Q4", 4, "A", "functions", "graphical_solutions",
    contextIntro=("Consider the equation $e^{x} = 3x$."),
    parts=[
        part("a", "By considering $f(x) = e^{x} - 3x$ at $x = 0$ and"
             " $x = 1$, explain why the equation has a solution between $0$"
             " and $1$.", 2,
             [M1("$f(0) = 1 > 0$ and $f(1) = e - 3 < 0$"),
              R1("$f$ is continuous and changes sign, so by the intermediate"
                 " value theorem there is a root in $(0, 1)$")],
             answer="sign change of $f$ on $(0, 1)$",
             solution=("$f(0) = e^0 - 0 = 1 > 0$ and $f(1) = e - 3 \\approx "
                       "-0.28 < 0$. As $f$ is continuous and changes sign,"
                       " there is a root between $0$ and $1$."),
             verify=["Eq(exp(0) - 3*0, 1)", "(exp(1) - 3) < 0"]),
        part("b", "State the number of real solutions of $e^{x} = 3x$.", 2,
             [M1("sketch $y = e^x$ and $y = 3x$ (GDC) — they cross twice"),
              A1("$2$ solutions")],
             answer="$2$",
             solution=("The line $y = 3x$ meets the curve $y = e^x$ at two"
                       " points, so there are $2$ real solutions."),
             verify=["(exp(0) - 3*0) > 0", "(exp(1) - 3*1) < 0",
                     "(exp(2) - 3*2) > 0"]),
        part("c", "Find both solutions, giving your answers to three"
             " significant figures.", 3,
             [M1("solve $e^x = 3x$ with the GDC"),
              A1(f"$x = {r4a_p}$"),
              A1(f"$x = {r4b_p}$")],
             answer=f"$x = {r4a_p}$ and $x = {r4b_p}$",
             solution=("Using the GDC to intersect $y = e^x$ and $y = 3x$:"
                       f"$$x = {r4a_p} \\text{{ and }} x = {r4b_p}.$$"),
             verify=[f"Abs(exp({r4a_p}) - 3*{r4a_p}) < 0.02",
                     f"Abs(exp({r4b_p}) - 3*{r4b_p}) < 0.02"]),
    ]))

# ── Q5 [8] calculus: area between two curves ─────────────────────────────
inter5 = sorted(solve(Eq(x - (x ** 2 - 2), 0), x))
assert inter5 == [-1, 2]
area5 = integrate((x) - (x ** 2 - 2), (x, -1, 2))
assert area5 == Rational(9, 2)
QS.append(question(
    "IB-AAHL-P2-T2-Q5", 5, "A", "calculus", "area_between_curves",
    contextIntro=("The curves $y = x$ and $y = x^2 - 2$ enclose a region"
                  " $R$."),
    parts=[
        part("a", "Find the $x$-coordinates of the points of intersection of"
             " the two curves.", 3,
             [M1("set $x = x^2 - 2$"),
              A1("$x^2 - x - 2 = (x - 2)(x + 1) = 0$"),
              A1("$x = -1$ and $x = 2$")],
             answer="$x = -1$ and $x = 2$",
             solution=("$$x = x^2 - 2 \\Rightarrow x^2 - x - 2 = 0 "
                       "\\Rightarrow (x - 2)(x + 1) = 0,$$ so $x = -1, 2$."),
             verify=["Eq(-1 - ((-1)**2 - 2), 0)", "Eq(2 - (2**2 - 2), 0)"]),
        part("b", "Find the area of $R$.", 5,
             [M1("area $= \\displaystyle\\int_{-1}^{2}\\big(x - (x^2 - 2)"
                 "\\big)\\,dx$ (line is above the parabola)"),
              A1("integrand $= -x^2 + x + 2$"),
              M1("antiderivative $-\\tfrac{x^3}{3} + \\tfrac{x^2}{2} + 2x$"),
              A1("evaluate between $-1$ and $2$"),
              A1("area $= \\dfrac{9}{2}$")],
             answer="area $= \\dfrac{9}{2}$",
             solution=("On $[-1, 2]$ the line lies above the parabola:"
                       "$$\\int_{-1}^{2}\\big(x - (x^2 - 2)\\big)\\,dx = "
                       "\\int_{-1}^{2}(-x^2 + x + 2)\\,dx = \\frac{9}{2}.$$"),
             verify=["Eq(integrate(x - (x**2 - 2), (x, -1, 2)),"
                     " Rational(9, 2))"]),
    ]))

# ── Q6 [8] functions: x ln x optimisation + tangent ──────────────────────
f6 = x * ln(x)
assert simplify(diff(f6, x) - (ln(x) + 1)) == 0
assert solve(Eq(ln(x) + 1, 0), x) == [exp(-1)]
assert simplify(f6.subs(x, exp(-1)) - (-exp(-1))) == 0
assert f6.subs(x, 1) == 0 and diff(f6, x).subs(x, 1) == 1
QS.append(question(
    "IB-AAHL-P2-T2-Q6", 6, "A", "functions", "logarithmic_functions",
    contextIntro=("The function $f$ is defined by $f(x) = x\\ln x$ for"
                  " $x > 0$."),
    parts=[
        part("a", "Find $f'(x)$.", 2,
             [M1("product rule on $x$ and $\\ln x$"),
              A1("$f'(x) = \\ln x + 1$")],
             answer="$f'(x) = \\ln x + 1$",
             solution=("$$f'(x) = 1\\cdot\\ln x + x\\cdot\\frac1x = "
                       "\\ln x + 1.$$"),
             verify=["Eq(simplify(diff(x*log(x), x) - (log(x) + 1)), 0)"]),
        part("b", "Find the coordinates of the minimum point of the graph of"
             " $f$, giving your answer in exact form.", 3,
             [M1("solve $f'(x) = 0$: $\\ln x = -1$"),
              A1("$x = e^{-1}$"),
              A1("minimum point $\\left(e^{-1},\\, -e^{-1}\\right)$")],
             answer="$\\left(e^{-1}, -e^{-1}\\right)$",
             solution=("$f'(x) = 0 \\Rightarrow \\ln x = -1 \\Rightarrow x "
                       "= e^{-1}$, and"
                       "$$f(e^{-1}) = e^{-1}\\ln(e^{-1}) = -e^{-1}.$$"
                       " Since $f'$ changes from negative to positive, this"
                       " is a minimum."),
             verify=["Eq(solve(Eq(log(x) + 1, 0), x)[0], exp(-1))",
                     "Eq(simplify((x*log(x)).subs(x, exp(-1)) + exp(-1)), 0)"]),
        part("c", "Find the equation of the tangent to the graph of $f$ at"
             " the point where $x = 1$.", 3,
             [M1("$f(1) = 0$ and $f'(1) = 1$"),
              A1("gradient $1$, point $(1, 0)$"),
              A1("$y = x - 1$")],
             answer="$y = x - 1$",
             solution=("At $x = 1$: $f(1) = 0$ and $f'(1) = \\ln 1 + 1 = 1$,"
                       " so"
                       "$$y - 0 = 1(x - 1) \\Rightarrow y = x - 1.$$"),
             verify=["Eq((x*log(x)).subs(x, 1), 0)",
                     "Eq(diff(x*log(x), x).subs(x, 1), 1)"]),
    ]))

# ── Q7 [8] number_algebra: complex powers via De Moivre ──────────────────
z7 = 1 + __import__("sympy").I
assert Abs(z7) == sqrt(2)
assert __import__("sympy").arg(z7) == pi / 4
assert simplify(z7 ** 8) == 16
assert simplify((1 + __import__("sympy").I) ** 4) == -4
QS.append(question(
    "IB-AAHL-P2-T2-Q7", 7, "A", "number_algebra", "complex_numbers",
    contextIntro=("Let $z = 1 + i$."),
    parts=[
        part("a", "Write down $|z|$ and $\\arg z$.", 2,
             [A1("$|z| = \\sqrt2$"),
              A1("$\\arg z = \\dfrac{\\pi}{4}$")],
             answer="$|z| = \\sqrt2$, $\\arg z = \\dfrac{\\pi}{4}$",
             solution=("$$|z| = \\sqrt{1^2 + 1^2} = \\sqrt2, \\qquad "
                       "\\arg z = \\frac{\\pi}{4}.$$"),
             verify=["Eq(Abs(1 + I), sqrt(2))", "Eq(arg(1 + I), pi/4)"]),
        part("b", "Use de Moivre's theorem to find $z^{8}$.", 3,
             [M1("$z^8 = (\\sqrt2)^8\\operatorname{cis}\\!\\left(8\\cdot"
                 "\\tfrac{\\pi}{4}\\right)$"),
              A1("$= 16\\operatorname{cis}(2\\pi)$"),
              A1("$z^8 = 16$")],
             answer="$z^8 = 16$",
             solution=("$$z^8 = (\\sqrt2)^8\\operatorname{cis}(2\\pi) = "
                       "16(1 + 0i) = 16.$$"),
             verify=["Eq(simplify((1 + I)**8), 16)"]),
        part("c", "Find the smallest positive integer $n$ such that $z^{n}$"
             " is a real number.", 3,
             [M1("$z^n$ is real when $\\arg(z^n) = \\dfrac{n\\pi}{4}$ is a"
                 " multiple of $\\pi$"),
              A1("$n$ must be a multiple of $4$"),
              A1("$n = 4$ (and $z^4 = -4$)")],
             answer="$n = 4$",
             solution=("$\\arg(z^n) = \\dfrac{n\\pi}{4}$ is a multiple of"
                       " $\\pi$ exactly when $4 \\mid n$; the smallest"
                       " positive such $n$ is $4$, and indeed $z^4 = "
                       "(1+i)^4 = -4$ is real."),
             verify=["Eq(simplify((1 + I)**4), -4)"]),
    ]))

# ── Q8 [19] stats_probability (Section B): expected-value game + binomial ─
# Die: even (2,4,6) win that many $, odd (1,3,5) lose $2
EW = Rational(1, 6) * (2 + 4 + 6) + Rational(1, 2) * (-2)
assert EW == 1
EW2 = Rational(1, 6) * (4 + 16 + 36) + Rational(1, 2) * 4
assert EW2 == Rational(34, 3)
VarW = EW2 - EW ** 2
assert VarW == Rational(31, 3)
sd_total = sqrt(20 * VarW)
sd_p, sd_tol = sf3(N(sd_total, 12))
assert sd_p == "14.4"
pYge12 = 1 - sum(binomial(20, k) * Rational(1, 2) ** 20 for k in range(12))
pY_p, pY_tol = sf3(N(pYge12, 15))
assert pY_p == "0.252"
CDF12 = " + ".join(f"binomial(20, {k})*Rational(1,2)**20" for k in range(12))
QS.append(question(
    "IB-AAHL-P2-T2-Q8", 8, "B", "stats_probability", "expectation_binomial",
    contextIntro=("In a game a fair six-sided die is rolled once. If the"
                  " result is even the player wins that many dollars; if the"
                  " result is odd the player loses \\$2. Let $W$ be the"
                  " player's winnings, in dollars, from one roll."),
    parts=[
        part("a", "Complete the probability distribution of $W$: the values"
             " are $-2$, $2$, $4$ and $6$. Write down each probability.", 3,
             [A1("$P(W = -2) = \\tfrac12$ (odd)"),
              A1("$P(W = 2) = P(W = 4) = P(W = 6) = \\tfrac16$"),
              R1("the four probabilities sum to $1$")],
             answer="$P(W=-2)=\\tfrac12$; $P(W=2)=P(W=4)=P(W=6)=\\tfrac16$",
             solution=("An odd result ($1, 3, 5$) has probability $\\tfrac36"
                       " = \\tfrac12$ and gives $W = -2$; each even result"
                       " has probability $\\tfrac16$ and gives $W = 2, 4, 6$"
                       " respectively. These sum to $1$."),
             verify=["Eq(Rational(1,2) + 3*Rational(1,6), 1)"]),
        part("b", "Find $E(W)$.", 3,
             [M1("$E(W) = \\sum w\\,P(W = w)$"),
              A1("$\\tfrac16(2 + 4 + 6) + \\tfrac12(-2) = 2 - 1$"),
              A1("$E(W) = 1$")],
             answer="$E(W) = \\$1$",
             solution=("$$E(W) = \\frac16(2 + 4 + 6) + \\frac12(-2) = 2 - 1 "
                       "= 1.$$"),
             verify=["Eq(Rational(1,6)*(2 + 4 + 6) + Rational(1,2)*(-2), 1)"]),
        part("c", "Find $\\operatorname{Var}(W)$.", 3,
             [M1("$E(W^2) = \\tfrac16(4 + 16 + 36) + \\tfrac12(4) = "
                 "\\tfrac{34}{3}$"),
              M1("$\\operatorname{Var}(W) = E(W^2) - [E(W)]^2$"),
              A1("$\\operatorname{Var}(W) = \\dfrac{31}{3}$")],
             answer="$\\operatorname{Var}(W) = \\dfrac{31}{3}$",
             solution=("$$E(W^2) = \\frac16(4 + 16 + 36) + \\frac12(4) = "
                       "\\frac{34}{3},$$"
                       "$$\\operatorname{Var}(W) = \\frac{34}{3} - 1^2 = "
                       "\\frac{31}{3}.$$"),
             verify=["Eq(Rational(1,6)*(4 + 16 + 36) + Rational(1,2)*4,"
                     " Rational(34, 3))",
                     "Eq(Rational(34, 3) - 1, Rational(31, 3))"]),
        part("d", "The game is played $20$ times. Find the expected total"
             " winnings and the standard deviation of the total.", 4,
             [M1("total expectation $= 20\\,E(W)$"),
              A1("expected total $= \\$20$"),
              M1("total variance $= 20\\operatorname{Var}(W)$ (independent"
                 " rolls)"),
              A1(f"standard deviation $= \\sqrt{{20 \\cdot \\tfrac{{31}}{{3}}}}"
                 f" = {sd_p}$")],
             answer=f"expected \\$20; standard deviation ${sd_p}$",
             solution=("$$E(\\text{total}) = 20(1) = \\$20.$$"
                       " Because the rolls are independent, variances add:"
                       f"$$\\operatorname{{sd}} = \\sqrt{{20\\cdot\\tfrac{{31}}"
                       f"{{3}}}} = {sig(N(sd_total, 12))} \\approx {sd_p}.$$"),
             verify=[f"Abs(sqrt(20*Rational(31, 3)) - {sd_p}) < {sd_tol}"]),
        part("e", "Let $Y$ be the number of the $20$ games that are wins"
             " (i.e. $W > 0$). Find $P(Y \\ge 12)$ and write down the most"
             " likely number of wins.", 6,
             [M1("$P(W > 0) = P(\\text{even}) = \\tfrac12$, so "
                 "$Y \\sim B(20, \\tfrac12)$"),
              M1("$P(Y \\ge 12) = 1 - P(Y \\le 11)$ (GDC)"),
              A1(f"$P(Y \\ge 12) = {pY_p}$ $({sig(N(pYge12, 12))}\\ldots)$"),
              A1("the distribution is symmetric about its mean"),
              A1("mean $= 20\\cdot\\tfrac12 = 10$"),
              A1("most likely number of wins $= 10$")],
             answer=f"$P(Y \\ge 12) = {pY_p}$; mode $= 10$",
             solution=("A win occurs on an even roll, with probability"
                       " $\\tfrac12$, so $Y \\sim B(20, \\tfrac12)$:"
                       f"$$P(Y \\ge 12) = 1 - P(Y \\le 11) = "
                       f"{sig(N(pYge12, 12))} \\approx {pY_p}.$$"
                       " The binomial with $p = \\tfrac12$ is symmetric, so"
                       " the most likely value is the mean $np = 10$."),
             verify=[f"Abs((1 - ({CDF12})) - {pY_p}) < {pY_tol}",
                     "Eq(20*Rational(1, 2), 10)"]),
    ]))

# ── Q9 [21] calculus (Section B): can optimisation, FIGURE ───────────────
# V = 330 -> h = 330/(pi r^2); A = 2 pi r^2 + 660/r
Ar = 2 * pi * r ** 2 + 660 / r
assert simplify(2 * pi * r ** 2 + 2 * pi * r * (330 / (pi * r ** 2)) - Ar) == 0
Apr = diff(Ar, r)
assert simplify(Apr - (4 * pi * r - 660 / r ** 2)) == 0
r_star = (Rational(165) / pi) ** Rational(1, 3)
assert simplify(Apr.subs(r, r_star)) == 0
rstar_p, rstar_tol = sf3(N(r_star, 12))
assert rstar_p == "3.74"
Amin = Ar.subs(r, r_star)
Amin_p, Amin_tol = sf3(N(Amin, 12))
assert Amin_p == "264"
hstar = 330 / (pi * r_star ** 2)
hstar_p, hstar_tol = sf3(N(hstar, 12))
assert hstar_p == "7.49"
Appr = diff(Ar, r, 2)
assert simplify(Appr - (4 * pi + 1320 / r ** 3)) == 0
# doubled volume 660 -> A2 = 2 pi r^2 + 1320/r
r2 = (Rational(330) / pi) ** Rational(1, 3)
A2min = (2 * pi * r ** 2 + 1320 / r).subs(r, r2)
A2_p, A2_tol = sf3(N(A2min, 12))
assert A2_p == "420"
QS.append(question(
    "IB-AAHL-P2-T2-Q9", 9, "B", "calculus", "optimisation",
    contextIntro=("A closed cylindrical can has radius $r$ cm and height $h$"
                  " cm, and a fixed volume of $330$ cm$^3$. The surface area"
                  " of the can is $A$ cm$^2$."),
    figure=png("ib-aahl-p2-t2-q9.png",
               "Closed cylinder of radius r and height h with r marked on the "
               "top circle and h marked on the side."),
    parts=[
        part("a", "Show that $A = 2\\pi r^2 + \\dfrac{660}{r}$.", 3,
             [M1("from $V = \\pi r^2 h = 330$, $h = \\dfrac{330}{\\pi r^2}$"),
              M1("$A = 2\\pi r^2 + 2\\pi r h$"),
              AG("$= 2\\pi r^2 + \\dfrac{660}{r}$")],
             answer="$A = 2\\pi r^2 + \\dfrac{660}{r}$",
             solution=("From $\\pi r^2 h = 330$, $h = \\dfrac{330}{\\pi r^2}$."
                       " The surface area of a closed cylinder is"
                       "$$A = 2\\pi r^2 + 2\\pi r h = 2\\pi r^2 + 2\\pi r "
                       "\\cdot\\frac{330}{\\pi r^2} = 2\\pi r^2 + "
                       "\\frac{660}{r}.$$"),
             verify=["Eq(simplify(2*pi*r**2 + 2*pi*r*(330/(pi*r**2))"
                     " - (2*pi*r**2 + 660/r)), 0)"]),
        part("b", "Find $\\dfrac{dA}{dr}$.", 3,
             [M1("differentiate term by term"),
              A1("$4\\pi r$ from the first term"),
              A1("$\\dfrac{dA}{dr} = 4\\pi r - \\dfrac{660}{r^2}$")],
             answer="$\\dfrac{dA}{dr} = 4\\pi r - \\dfrac{660}{r^2}$",
             solution=("$$\\frac{dA}{dr} = 4\\pi r - \\frac{660}{r^2}.$$"),
             verify=["Eq(simplify(diff(2*pi*r**2 + 660/r, r)"
                     " - (4*pi*r - 660/r**2)), 0)"]),
        part("c", "Find the value of $r$ that minimises $A$, giving your"
             " answer to three significant figures.", 4,
             [M1("set $\\dfrac{dA}{dr} = 0$: $4\\pi r = \\dfrac{660}{r^2}$"),
              A1("$r^3 = \\dfrac{165}{\\pi}$"),
              M1("solve (GDC or cube root)"),
              A1(f"$r = {rstar_p}$ $({sig(N(r_star, 12))}\\ldots)$")],
             answer=f"$r = {rstar_p}$",
             solution=("$$4\\pi r - \\frac{660}{r^2} = 0 \\Rightarrow r^3 = "
                       "\\frac{660}{4\\pi} = \\frac{165}{\\pi} \\Rightarrow r"
                       f" = {sig(N(r_star, 12))} \\approx {rstar_p}.$$"),
             verify=[f"Abs((Rational(165)/pi)**Rational(1,3) - {rstar_p}) "
                     f"< {rstar_tol}"]),
        part("d", "Find the minimum surface area.", 3,
             [M1("substitute $r$ into $A$"),
              A1("$A = 2\\pi r^2 + \\dfrac{660}{r}$ at the optimal $r$"),
              A1(f"$A_{{\\min}} = {Amin_p}$ cm$^2$ "
                 f"$({sig(N(Amin, 12))}\\ldots)$")],
             answer=f"$A_{{\\min}} = {Amin_p}$ cm$^2$",
             solution=("$$A_{\\min} = 2\\pi(3.744)^2 + \\frac{660}{3.744} = "
                       f"{sig(N(Amin, 12))} \\approx {Amin_p} \\text{{ cm}}"
                       "^2.$$"),
             verify=[f"Abs((2*pi*r**2 + 660/r).subs(r,"
                     f" (Rational(165)/pi)**Rational(1,3)) - {Amin_p}) "
                     f"< {Amin_tol}"]),
        part("e", "By considering the second derivative, justify that this"
             " value of $r$ gives a minimum, and find the corresponding"
             " height $h$.", 4,
             [M1("$\\dfrac{d^2A}{dr^2} = 4\\pi + \\dfrac{1320}{r^3}$"),
              R1("this is positive for all $r > 0$, so $A$ is a minimum"),
              M1("$h = \\dfrac{330}{\\pi r^2}$"),
              A1(f"$h = {hstar_p}$ cm (note $h = 2r$)")],
             answer=f"minimum confirmed; $h = {hstar_p}$ cm",
             solution=("$$\\frac{d^2A}{dr^2} = 4\\pi + \\frac{1320}{r^3} > 0"
                       "\\text{ for all } r > 0,$$ so the stationary point is"
                       " a minimum. The height is"
                       f"$$h = \\frac{{330}}{{\\pi r^2}} = "
                       f"{sig(N(hstar, 12))} \\approx {hstar_p} \\text{{ cm}},"
                       "$$ which equals $2r$."),
             verify=["Eq(simplify(diff(2*pi*r**2 + 660/r, r, 2)"
                     " - (4*pi + 1320/r**3)), 0)",
                     f"Abs((330/(pi*r**2)).subs(r,"
                     f" (Rational(165)/pi)**Rational(1,3)) - {hstar_p}) "
                     f"< {hstar_tol}"]),
        part("f", "The volume is now doubled to $660$ cm$^3$. Find the new"
             " minimum surface area.", 4,
             [M1("now $A = 2\\pi r^2 + \\dfrac{1320}{r}$"),
              M1("minimise: $r^3 = \\dfrac{330}{\\pi}$"),
              A1("optimal $r \\approx 4.72$"),
              A1(f"$A_{{\\min}} = {A2_p}$ cm$^2$ $({sig(N(A2min, 12))}"
                 "\\ldots)$")],
             answer=f"$A_{{\\min}} = {A2_p}$ cm$^2$",
             solution=("Doubling the volume gives $A = 2\\pi r^2 + "
                       "\\dfrac{1320}{r}$, minimised when $r^3 = "
                       "\\dfrac{330}{\\pi}$, i.e. $r \\approx 4.72$:"
                       f"$$A_{{\\min}} = {sig(N(A2min, 12))} \\approx "
                       f"{A2_p} \\text{{ cm}}^2.$$"),
             verify=[f"Abs((2*pi*r**2 + 1320/r).subs(r,"
                     f" (Rational(330)/pi)**Rational(1,3)) - {A2_p}) "
                     f"< {A2_tol}"]),
    ]))

# ── Q10 [18] geometry_trig (Section B): bearings navigation, FIGURE ──────
angPQR = 110      # 240 (back-bearing) - 130
PR2 = 20 ** 2 + 15 ** 2 - 2 * 20 * 15 * cos(rad(angPQR))
PR = sqrt(PR2)
PR_p, PR_tol = sf3(N(PR, 12))
assert PR_p == "28.8"
# angle QPR via sine rule
sinQPR = 15 * sin(rad(angPQR)) / PR
QPR = asin(sinQPR)
bearingR = 60 + deg(QPR)
bearR_p, bearR_tol = sf3(N(bearingR, 12))
assert bearR_p == "89.3"
area10 = Rational(1, 2) * 20 * 15 * sin(rad(angPQR))
distQ = 2 * area10 / PR
distQ_p, distQ_tol = sf3(N(distQ, 12))
assert distQ_p == "9.78"
returnBearing = bearingR + 180
retB_p, retB_tol = sf3(N(returnBearing, 12))
assert retB_p == "269"
QS.append(question(
    "IB-AAHL-P2-T2-Q10", 10, "B", "geometry_trig", "bearings",
    contextIntro=("A ship sails from port $P$ on a bearing of $060^\\circ$"
                  " for $20$ km to a point $Q$, then changes course and"
                  " sails on a bearing of $130^\\circ$ for $15$ km to a point"
                  " $R$."),
    figure=png("ib-aahl-p2-t2-q10.png",
               "Navigation diagram: from P a leg of 20 km on bearing 060 to "
               "Q, then a leg of 15 km on bearing 130 to R, with North "
               "arrows at P and Q and the direct line PR dashed."),
    parts=[
        part("a", "Show that the angle $P\\hat{Q}R = 110^\\circ$.", 3,
             [M1("the back-bearing of $Q$ from the first leg is $240^\\circ$"),
              A1("angle $= 240^\\circ - 130^\\circ$"),
              AG("$P\\hat{Q}R = 110^\\circ$")],
             answer="$P\\hat{Q}R = 110^\\circ$",
             solution=("Arriving at $Q$ the ship faces $060^\\circ$, so the"
                       " direction back to $P$ is $060 + 180 = 240^\\circ$."
                       " The next leg is on $130^\\circ$, so"
                       "$$P\\hat{Q}R = 240^\\circ - 130^\\circ = "
                       "110^\\circ.$$"),
             verify=["Eq(240 - 130, 110)"]),
        part("b", "Find the distance $PR$.", 4,
             [M1("cosine rule $PR^2 = 20^2 + 15^2 - 2(20)(15)\\cos "
                 "110^\\circ$"),
              A1(f"$PR^2 = {sig(N(PR2, 12))}$"),
              M1("take the positive square root"),
              A1(f"$PR = {PR_p}$ km")],
             answer=f"$PR = {PR_p}$ km",
             solution=("$$PR^2 = 20^2 + 15^2 - 2(20)(15)\\cos 110^\\circ = "
                       f"{sig(N(PR2, 12))}$$"
                       f"$$PR = {sig(N(PR, 12))} \\approx {PR_p} \\text{{ km}}"
                       ".$$"),
             verify=[f"Abs(sqrt(20**2 + 15**2 - 600*cos(rad(110))) - {PR_p})"
                     f" < {PR_tol}"]),
        part("c", "Find the bearing of $R$ from $P$.", 4,
             [M1("sine rule for angle $Q\\hat{P}R$: "
                 "$\\dfrac{\\sin Q\\hat{P}R}{15} = \\dfrac{\\sin 110^\\circ}"
                 "{PR}$"),
              A1("$Q\\hat{P}R = 29.3^\\circ$"),
              M1("add to the first bearing: $060^\\circ + Q\\hat{P}R$"),
              A1(f"bearing $= {bearR_p}^\\circ$")],
             answer=f"$ {bearR_p}^\\circ$",
             solution=("By the sine rule, $\\sin Q\\hat{P}R = \\dfrac{15\\sin"
                       " 110^\\circ}{PR}$, giving $Q\\hat{P}R = "
                       "29.3^\\circ$. The bearing of $R$ from $P$ is"
                       f"$$060^\\circ + 29.3^\\circ = "
                       f"{bearR_p}^\\circ.$$"),
             verify=[f"Abs(60 + deg(asin(15*sin(rad(110))"
                     f"/sqrt(20**2 + 15**2 - 600*cos(rad(110))))) - {bearR_p})"
                     f" < {bearR_tol}"]),
        part("d", "Find the shortest distance from $Q$ to the line $[PR]$.", 3,
             [M1("area of triangle $= \\tfrac12(20)(15)\\sin 110^\\circ$,"
                 " and area $= \\tfrac12 \\times PR \\times d$"),
              A1(f"$d = \\dfrac{{2 \\times \\text{{area}}}}{{PR}}$"),
              A1(f"$d = {distQ_p}$ km")],
             answer=f"$ {distQ_p}$ km",
             solution=("The area of triangle $PQR$ is $\\tfrac12(20)(15)\\sin"
                       " 110^\\circ$. Equating to $\\tfrac12\\,PR\\,d$:"
                       f"$$d = \\frac{{2\\times\\tfrac12(20)(15)\\sin "
                       f"110^\\circ}}{{PR}} = {sig(N(distQ, 12))} \\approx "
                       f"{distQ_p} \\text{{ km}}.$$"),
             verify=[f"Abs(2*Rational(1,2)*300*sin(rad(110))"
                     f"/sqrt(20**2 + 15**2 - 600*cos(rad(110))) - {distQ_p})"
                     f" < {distQ_tol}"]),
        part("e", "Find the bearing on which the ship must sail to return"
             " directly from $R$ to $P$.", 4,
             [M1("the return bearing is the reverse of the bearing of $R$"
                 " from $P$"),
              A1("add $180^\\circ$ to the bearing found in (c)"),
              A1(f"${bearR_p}^\\circ + 180^\\circ$"),
              A1(f"bearing $= {retB_p}^\\circ$")],
             answer=f"$ {retB_p}^\\circ$",
             solution=("The bearing of $P$ from $R$ is the back-bearing of"
                       " the bearing of $R$ from $P$:"
                       f"$${bearR_p}^\\circ + 180^\\circ = "
                       f"{retB_p}^\\circ.$$"),
             verify=[f"Abs((60 + deg(asin(15*sin(rad(110))"
                     f"/sqrt(20**2 + 15**2 - 600*cos(rad(110))))) + 180)"
                     f" - {retB_p}) < {retB_tol}"]),
    ]))

META = {"course": "aa", "level": "hl", "paper": 2, "testId": "ib-hl-practice-2",
        "label": "AA HL Practice Paper 2", "timeMinutes": 120,
        "totalMarks": 110, "calculator": True}

if __name__ == "__main__":
    write_paper(META, QS, "data/ib/aa-hl/ib-hl-practice-2/paper2.json")
