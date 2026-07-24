"""AA SL Practice Paper 2 (ib-practice-4) — 90 min, 80 marks, GDC required.

Blueprint (topic x marks):
    Section A (40): Q1 functions 6 | Q2 stats_probability 6
                    Q3 geometry_trig 6 | Q4 number_algebra 6
                    Q5 functions 8 | Q6 calculus 8
    Section B (40): Q7 functions 13 | Q8 stats_probability 12
                    Q9 calculus 15
    Paper totals: functions 27 | stats_probability 18 | geometry_trig 6 |
                  number_algebra 6 | calculus 23 = 80.

Fresh archetypes versus practice 1-3: exponential equation solved with
logs, binomial B(8, 0.35), cosine-rule triangle + area, compound interest
with a "least whole years" search, cubic stationary points via GDC and a
horizontal-line intersection count, area under a parabola, a sinusoidal
temperature model, a two-percentile normal distribution N(mu, sigma^2)
recovered from data, and rectilinear kinematics with displacement vs
TOTAL distance. Figures: Q3 (triangle), Q7 (temperature curve) generated
by scripts/test-figures/ib-aa-sl-practice-4.py from the SAME parameters.
"""
import os
import sys
from math import floor, log10

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, N, erf, erfinv, log, sin, cos,  # noqa: F401,E402
                   asin, rad, integrate, diff, expand, solve, simplify,
                   binomial, symbols)

x, t = symbols("x t")


def sf3(v):
    """Round to 3 significant figures; return (printed_string, tolerance)."""
    v = float(v)
    assert v != 0
    d = 2 - floor(log10(abs(v)))
    r = round(v, d)
    printed = str(int(r)) if d <= 0 else f"{r:.{d}f}"
    assert abs(v - r) < 0.499 * 10 ** (-d), f"ambiguous 3sf rounding for {v}"
    return printed, 0.51 * 10 ** (-d)


def sig(v, n=6):
    v = float(v)
    d = (n - 1) - floor(log10(abs(v)))
    return f"{round(v, d):.{max(d, 0)}f}"


def Phi(z):
    return (1 + erf(z / sqrt(2))) / 2


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [6] functions: exponential equation ───────────────────────────────
assert 3 * 2 ** 0 == 3
assert 3 * 2 ** 4 == 48
x1 = log(Rational(100, 3)) / log(2)
x1_p, x1_tol = sf3(N(x1, 12))
assert x1_p == "5.06"
QS.append(question(
    "IB-AASL-P2-T4-Q1", 1, "A", "functions", "exponential_functions",
    contextIntro=("The function $f$ is defined by $f(x) = 3 \\times 2^{x}$."),
    parts=[
        part("a", "Write down the value of $f(0)$.", 1,
             [A1("$f(0) = 3$")],
             answer="$f(0) = 3$",
             solution=("$$f(0) = 3 \\times 2^{0} = 3.$$"),
             verify=["Eq(3*2**0, 3)"]),
        part("b", "Find the value of $x$ for which $f(x) = 48$.", 2,
             [M1("$2^{x} = 16$"),
              A1("$x = 4$")],
             answer="$x = 4$",
             solution=("$$3 \\times 2^{x} = 48 \\Rightarrow 2^{x} = 16 = 2^4"
                       " \\Rightarrow x = 4.$$"),
             verify=["Eq(3*2**4, 48)"]),
        part("c", "Solve $f(x) = 100$, giving your answer to three"
             " significant figures.", 3,
             [M1("$2^{x} = \\dfrac{100}{3}$"),
              M1("take logarithms: $x = \\dfrac{\\ln(100/3)}{\\ln 2}$"),
              A1(f"$x = {x1_p}$ $({sig(N(x1, 12))}\\ldots)$")],
             answer=f"$x = {x1_p}$",
             solution=("$$3 \\times 2^{x} = 100 \\Rightarrow 2^{x} = "
                       "\\frac{100}{3}$$"
                       f"$$x = \\frac{{\\ln(100/3)}}{{\\ln 2}} = "
                       f"{sig(N(x1, 12))} \\approx {x1_p}.$$"),
             verify=[f"Abs(log(Rational(100, 3))/log(2) - {x1_p}) < {x1_tol}"]),
    ]))

# ── Q2 [6] stats_probability: binomial B(8, 0.35) ────────────────────────
p = Rational(35, 100)
pX3 = binomial(8, 3) * p ** 3 * (1 - p) ** 5
pX3_p, pX3_tol = sf3(N(pX3, 15))
assert pX3_p == "0.279"
pLe2 = sum(binomial(8, k) * p ** k * (1 - p) ** (8 - k) for k in range(3))
pLe2_p, pLe2_tol = sf3(N(pLe2, 15))
assert pLe2_p == "0.428"
assert 8 * p == Rational(14, 5)
QS.append(question(
    "IB-AASL-P2-T4-Q2", 2, "A", "stats_probability", "binomial_distribution",
    contextIntro=("A biased coin lands on heads with probability $0.35$. The"
                  " coin is tossed $8$ times. Let $X$ be the number of heads,"
                  " so $X \\sim B(8,\\, 0.35)$."),
    parts=[
        part("a", "Find $P(X = 3)$.", 2,
             [M1("binomial pdf $\\binom{8}{3}(0.35)^3(0.65)^5$ (or GDC)"),
              A1(f"$P(X = 3) = {pX3_p}$ $({sig(N(pX3, 12))}\\ldots)$")],
             answer=f"${pX3_p}$",
             solution=("$$P(X = 3) = \\binom{8}{3}(0.35)^3(0.65)^5 = "
                       f"{sig(N(pX3, 12))} \\approx {pX3_p}.$$"),
             verify=[f"Abs(binomial(8, 3)*Rational(35,100)**3"
                     f"*Rational(65,100)**5 - {pX3_p}) < {pX3_tol}"]),
        part("b", "Find $P(X \\le 2)$.", 2,
             [M1("binomial cdf up to $2$ (or sum $k = 0, 1, 2$)"),
              A1(f"$P(X \\le 2) = {pLe2_p}$ $({sig(N(pLe2, 12))}\\ldots)$")],
             answer=f"${pLe2_p}$",
             solution=("$$P(X \\le 2) = \\sum_{k=0}^{2}\\binom{8}{k}"
                       "(0.35)^k(0.65)^{8-k} = "
                       f"{sig(N(pLe2, 12))} \\approx {pLe2_p}.$$"),
             verify=[f"Abs((Rational(65,100)**8 "
                     f"+ 8*Rational(35,100)*Rational(65,100)**7 "
                     f"+ 28*Rational(35,100)**2*Rational(65,100)**6) "
                     f"- {pLe2_p}) < {pLe2_tol}"]),
        part("c", "Write down $E(X)$.", 2,
             [M1("use $E(X) = np$"),
              A1("$E(X) = 2.8$")],
             answer="$E(X) = 2.8$",
             solution=("$$E(X) = np = 8 \\times 0.35 = 2.8.$$"),
             verify=["Eq(8*Rational(35,100), Rational(14,5))"]),
    ]))

# ── Q3 [6] geometry_trig: cosine rule + area, FIGURE ─────────────────────
bAC, cAB, Adeg = 9, 7, 52
BC2 = cAB ** 2 + bAC ** 2 - 2 * cAB * bAC * cos(rad(Adeg))
BC = sqrt(BC2)
BC_p, BC_tol = sf3(N(BC, 12))
assert BC_p == "7.24"
area3 = Rational(1, 2) * cAB * bAC * sin(rad(Adeg))
area3_p, area3_tol = sf3(N(area3, 12))
assert area3_p == "24.8"
QS.append(question(
    "IB-AASL-P2-T4-Q3", 3, "A", "geometry_trig", "non_right_triangles",
    contextIntro=("In triangle $ABC$, $AB = 7$ cm, $AC = 9$ cm and"
                  " $B\\hat{A}C = 52^{\\circ}$."),
    figure=png("ib-aasl-p2-t4-q3.png",
               "Triangle ABC with AB = 7 cm along the base, AC = 9 cm, and "
               "the 52 degree angle at A marked with an arc."),
    parts=[
        part("a", "Find the length of $BC$.", 3,
             [M1("cosine rule $BC^2 = 7^2 + 9^2 - 2(7)(9)\\cos 52^{\\circ}$"),
              A1(f"$BC^2 = {sig(N(BC2, 12))}$"),
              A1(f"$BC = {BC_p}$ cm")],
             answer=f"$BC = {BC_p}$ cm",
             solution=("$$BC^2 = 7^2 + 9^2 - 2(7)(9)\\cos 52^{\\circ} = "
                       f"{sig(N(BC2, 12))}$$"
                       f"$$BC = {sig(N(BC, 12))} \\approx {BC_p} "
                       "\\text{ cm}.$$"),
             verify=[f"Abs(sqrt(7**2 + 9**2 - 126*cos(rad(52))) - {BC_p}) "
                     f"< {BC_tol}"]),
        part("b", "Find the area of triangle $ABC$.", 3,
             [M1("area $= \\tfrac12 (7)(9)\\sin 52^{\\circ}$"),
              A1(f"$= {sig(N(area3, 12))}\\ldots$"),
              A1(f"area $= {area3_p}$ cm$^2$")],
             answer=f"${area3_p}$ cm$^2$",
             solution=("$$\\text{Area} = \\tfrac12 (7)(9)\\sin 52^{\\circ} "
                       f"= {sig(N(area3, 12))} \\approx {area3_p} "
                       "\\text{ cm}^2.$$"),
             verify=[f"Abs(Rational(1,2)*63*sin(rad(52)) - {area3_p}) "
                     f"< {area3_tol}"]),
    ]))

# ── Q4 [6] number_algebra: compound interest ─────────────────────────────
V5 = 2000 * Rational(104, 100) ** 5
V5_p = f"{float(N(V5, 15)):.2f}"
assert V5_p == "2433.31"
assert 2000 * Rational(104, 100) ** 10 < 3000
assert 2000 * Rational(104, 100) ** 11 > 3000
QS.append(question(
    "IB-AASL-P2-T4-Q4", 4, "A", "number_algebra", "financial_math",
    contextIntro=("Bold invests \\$2000 in an account paying $4\\%$ interest"
                  " per year, compounded annually."),
    parts=[
        part("a", "Find the value of the investment after $5$ years, giving"
             " your answer to two decimal places.", 2,
             [M1("$V = 2000(1.04)^5$"),
              A1(f"$V = \\${V5_p}$")],
             answer=f"$\\${V5_p}$",
             solution=("$$V = 2000(1.04)^5 = " f"{V5_p}.$$"),
             verify=[f"Abs(2000*Rational(104,100)**5 - {V5_p}) < 0.005"]),
        part("b", "Find the least number of complete years for the"
             " investment to exceed \\$3000.", 4,
             [M1("solve $2000(1.04)^n > 3000$, i.e. $(1.04)^n > 1.5$"),
              A1("$n > \\dfrac{\\ln 1.5}{\\ln 1.04} = 10.3\\ldots$"),
              M1("test whole years: $2000(1.04)^{10} = \\$2960.49 < 3000$"),
              A1("least $n = 11$ years")],
             answer="$11$ years",
             solution=("$$2000(1.04)^n > 3000 \\Rightarrow (1.04)^n > 1.5 "
                       "\\Rightarrow n > \\frac{\\ln 1.5}{\\ln 1.04} = "
                       "10.33\\ldots$$"
                       "After $10$ years the value is \\$2960.49 $< 3000$;"
                       " after $11$ years it is \\$3078.91 $> 3000$. The"
                       " least number of complete years is $11$."),
             verify=["2000*Rational(104,100)**10 < 3000",
                     "2000*Rational(104,100)**11 > 3000",
                     "Abs(log(Rational(3,2))/log(Rational(104,100)) - 10.33)"
                     " < 0.05"]),
    ]))

# ── Q5 [8] functions: cubic stationary points via GDC ────────────────────
g5 = x ** 3 - 6 * x ** 2 + 9 * x + 2
assert expand(diff(g5, x)) == 3 * x ** 2 - 12 * x + 9
assert sorted(solve(Eq(diff(g5, x), 0), x)) == [1, 3]
assert g5.subs(x, 1) == 6 and g5.subs(x, 3) == 2
QS.append(question(
    "IB-AASL-P2-T4-Q5", 5, "A", "functions", "cubic_functions",
    contextIntro=("The function $g$ is defined by "
                  "$g(x) = x^3 - 6x^2 + 9x + 2$."),
    parts=[
        part("a", "Find the coordinates of the two stationary points of the"
             " graph of $g$.", 4,
             [M1("$g'(x) = 3x^2 - 12x + 9 = 0$ (GDC or factor)"),
              A1("$x = 1$ and $x = 3$"),
              A1("$(1, 6)$"),
              A1("$(3, 2)$")],
             answer="$(1, 6)$ and $(3, 2)$",
             solution=("$$g'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 "
                       "\\Rightarrow x = 1, 3.$$"
                       "$$g(1) = 6, \\qquad g(3) = 2.$$"),
             verify=["Eq(expand(diff(x**3 - 6*x**2 + 9*x + 2, x)),"
                     " 3*x**2 - 12*x + 9)",
                     "Eq((x**3 - 6*x**2 + 9*x + 2).subs(x, 1), 6)",
                     "Eq((x**3 - 6*x**2 + 9*x + 2).subs(x, 3), 2)"]),
        part("b", "State the nature of each stationary point.", 2,
             [A1("$(1, 6)$ is a local maximum"),
              A1("$(3, 2)$ is a local minimum")],
             answer="$(1, 6)$ maximum; $(3, 2)$ minimum",
             solution=("The cubic has a positive leading coefficient, so the"
                       " first stationary point $(1, 6)$ is a local maximum"
                       " and $(3, 2)$ is a local minimum."),
             verify=["Eq((x**3 - 6*x**2 + 9*x + 2).subs(x, 1)"
                     " - (x**3 - 6*x**2 + 9*x + 2).subs(x, 3), 4)"]),
        part("c", "Hence state the number of solutions of the equation"
             " $g(x) = 4$.", 2,
             [M1("the line $y = 4$ lies between the minimum $2$ and the"
                 " maximum $6$"),
              A1("$3$ solutions")],
             answer="$3$",
             solution=("Since $2 < 4 < 6$, the horizontal line $y = 4$ cuts"
                       " the curve three times, so $g(x) = 4$ has $3$"
                       " solutions."),
             verify=["2 < 4", "4 < 6"]),
    ]))

# ── Q6 [8] calculus: area under a parabola ───────────────────────────────
f6 = 4 * x - x ** 2
assert sorted(solve(Eq(f6, 0), x)) == [0, 4]
area6 = integrate(f6, (x, 0, 4))
assert area6 == Rational(32, 3)
QS.append(question(
    "IB-AASL-P2-T4-Q6", 6, "A", "calculus", "integration_area",
    contextIntro=("The curve $y = 4x - x^2$ encloses a region with the"
                  " $x$-axis."),
    parts=[
        part("a", "Find the $x$-coordinates of the points where the curve"
             " meets the $x$-axis.", 3,
             [M1("set $4x - x^2 = 0$"),
              A1("$x(4 - x) = 0$"),
              A1("$x = 0$ and $x = 4$")],
             answer="$x = 0$ and $x = 4$",
             solution=("$$4x - x^2 = x(4 - x) = 0 \\Rightarrow x = 0 "
                       "\\text{ or } x = 4.$$"),
             verify=["Eq(4*0 - 0**2, 0)", "Eq(4*4 - 4**2, 0)"]),
        part("b", "Find the area of the region enclosed between the curve"
             " and the $x$-axis.", 5,
             [M1("area $= \\displaystyle\\int_0^4 (4x - x^2)\\,dx$"),
              A1("antiderivative $2x^2 - \\tfrac{x^3}{3}$"),
              M1("evaluate between $0$ and $4$"),
              A1("$32 - \\tfrac{64}{3}$"),
              A1("area $= \\dfrac{32}{3}$")],
             answer="area $= \\dfrac{32}{3}$",
             solution=("The curve is above the axis on $[0, 4]$:"
                       "$$\\int_0^4 (4x - x^2)\\,dx = \\left[2x^2 - "
                       "\\frac{x^3}{3}\\right]_0^4 = 32 - \\frac{64}{3} = "
                       "\\frac{32}{3}.$$"),
             verify=["Eq(integrate(4*x - x**2, (x, 0, 4)), Rational(32, 3))"]),
    ]))

# ── Q7 [13] functions (Section B): sinusoidal model, FIGURE ──────────────
def Tmodel(tt):
    return 8 * sin(pi / 6 * (tt - 3)) + 15
assert Tmodel(6) == 23
assert Tmodel(0) == 8 * sin(-pi / 2) + 15 == 7
period7 = 2 * pi / (pi / 6)
assert period7 == 12
# T = 20 -> sin(pi/6 (t-3)) = 5/8
a58 = float(N(asin(Rational(5, 8)), 15))
pival = float(N(pi, 15))
t_first = 3 + 6 / pival * a58
t1_p, t1_tol = sf3(t_first)
assert t1_p == "4.29"
t_second = 3 + 6 / pival * (pival - a58)
t2_p, t2_tol = sf3(t_second)
assert t2_p == "7.71"
dur7 = t_second - t_first
dur_p, dur_tol = sf3(dur7)
assert dur_p == "3.42"
QS.append(question(
    "IB-AASL-P2-T4-Q7", 7, "B", "functions", "trigonometric_models",
    contextIntro=("The temperature $T$, in $^{\\circ}$C, in a greenhouse $t$"
                  " hours after midnight is modelled by"
                  " $T(t) = 8\\sin\\!\\left(\\dfrac{\\pi}{6}(t - 3)\\right)"
                  " + 15$ for $0 \\le t \\le 24$."),
    figure=png("ib-aasl-p2-t4-q7.png",
               "One-and-a-half cycles of the temperature curve T against t "
               "from 0 to 24 hours, oscillating between 7 and 23 with "
               "midline 15."),
    parts=[
        part("a", "Write down the maximum and minimum temperatures predicted"
             " by the model.", 2,
             [A1("maximum $= 15 + 8 = 23\\,^{\\circ}$C"),
              A1("minimum $= 15 - 8 = 7\\,^{\\circ}$C")],
             answer="maximum $23\\,^{\\circ}$C, minimum $7\\,^{\\circ}$C",
             solution=("The amplitude is $8$ about the midline $15$, so"
                       "$$T_{\\max} = 23\\,^{\\circ}\\text{C}, \\qquad "
                       "T_{\\min} = 7\\,^{\\circ}\\text{C}.$$"),
             verify=["Eq(15 + 8, 23)", "Eq(15 - 8, 7)"]),
        part("b", "Find the period of the model.", 2,
             [M1("period $= \\dfrac{2\\pi}{\\pi/6}$"),
              A1("$12$ hours")],
             answer="$12$ hours",
             solution=("$$\\text{period} = \\frac{2\\pi}{\\pi/6} = 12 "
                       "\\text{ hours}.$$"),
             verify=["Eq(2*pi/(pi/6), 12)"]),
        part("c", "Find the maximum temperature and the time at which it"
             " first occurs.", 3,
             [M1("the maximum occurs when $\\dfrac{\\pi}{6}(t - 3) = "
                 "\\dfrac{\\pi}{2}$"),
              A1("$t - 3 = 3$"),
              A1("$T = 23\\,^{\\circ}$C at $t = 6$ (06:00)")],
             answer="$23\\,^{\\circ}$C at $t = 6$",
             solution=("The sine reaches $1$ when $\\dfrac{\\pi}{6}(t-3) = "
                       "\\dfrac{\\pi}{2}$, giving $t = 6$, and then"
                       "$$T(6) = 8(1) + 15 = 23\\,^{\\circ}\\text{C}.$$"),
             verify=["Eq(8*sin(pi/6*(6 - 3)) + 15, 23)"]),
        part("d", "Find the two times during the first $12$ hours at which"
             " the temperature is $20\\,^{\\circ}$C.", 3,
             [M1("$\\sin\\!\\left(\\tfrac{\\pi}{6}(t-3)\\right) = "
                 "\\tfrac{5}{8}$ (GDC)"),
              A1(f"$t = {t1_p}$"),
              A1(f"$t = {t2_p}$")],
             answer=f"$t = {t1_p}$ and $t = {t2_p}$ hours",
             solution=("$$8\\sin\\!\\left(\\tfrac{\\pi}{6}(t-3)\\right) + 15 "
                       "= 20 \\Rightarrow \\sin\\!\\left(\\tfrac{\\pi}{6}"
                       "(t-3)\\right) = \\tfrac{5}{8}.$$"
                       f" Solving with the GDC on $0 \\le t \\le 12$ gives"
                       f" $t = {t1_p}$ and $t = {t2_p}$ hours."),
             verify=[f"Abs(8*sin(pi/6*({t1_p} - 3)) + 15 - 20) < 0.02",
                     f"Abs(8*sin(pi/6*({t2_p} - 3)) + 15 - 20) < 0.02"]),
        part("e", "Hence find the length of time during the first $12$ hours"
             " for which the temperature is at least $20\\,^{\\circ}$C.", 3,
             [M1("the temperature is $\\ge 20$ between the two times in (d)"),
              A1(f"${t2_p} - {t1_p}$"),
              A1(f"$= {dur_p}$ hours")],
             answer=f"${dur_p}$ hours",
             solution=("Between the two solutions the curve is above $20$:"
                       f"$$ {t2_p} - {t1_p} = {dur_p} \\text{{ hours}}.$$"),
             verify=[f"Abs(({t2_p} - {t1_p}) - {dur_p}) < 0.02"]),
    ]))

# ── Q8 [12] stats_probability (Section B): two-percentile normal ─────────
z1 = sqrt(2) * erfinv(2 * Rational(10, 100) - 1)      # P(M<200)=0.10
z2 = sqrt(2) * erfinv(2 * Rational(95, 100) - 1)      # P(M>260)=0.05 -> 0.95
# 200 - mu = z1 * sigma ; 260 - mu = z2 * sigma
sigma8 = (260 - 200) / (z2 - z1)
mu8 = 200 - z1 * sigma8
sig8_p, sig8_tol = sf3(N(sigma8, 15))
mu8_p, mu8_tol = sf3(N(mu8, 15))
assert sig8_p == "20.5"
assert mu8_p == "226"
p_mid = Phi((240 - mu8) / sigma8) - Phi((210 - mu8) / sigma8)
pmid_p, pmid_tol = sf3(N(p_mid, 15))
assert pmid_p == "0.535"
perc99 = mu8 + sigma8 * sqrt(2) * erfinv(2 * Rational(99, 100) - 1)
p99_p, p99_tol = sf3(N(perc99, 15))
assert p99_p == "274"
QS.append(question(
    "IB-AASL-P2-T4-Q8", 8, "B", "stats_probability", "normal_distribution",
    contextIntro=("The mass $M$, in grams, of an apple from an orchard is"
                  " normally distributed with mean $\\mu$ and standard"
                  " deviation $\\sigma$. It is known that $P(M < 200) = 0.10$"
                  " and $P(M > 260) = 0.05$."),
    parts=[
        part("a", "Find the value of $\\mu$ and the value of $\\sigma$.", 6,
             [M1("standardise the first condition: "
                 "$\\dfrac{200 - \\mu}{\\sigma} = z_{0.10}$"),
              A1("$z_{0.10} = -1.2816\\ldots$"),
              M1("standardise the second: $\\dfrac{260 - \\mu}{\\sigma} = "
                 "z_{0.95} = 1.6449\\ldots$"),
              M1("subtract to eliminate $\\mu$: $60 = (z_{0.95} - z_{0.10})"
                 "\\sigma$"),
              A1(f"$\\sigma = {sig8_p}$"),
              A1(f"$\\mu = {mu8_p}$")],
             answer=f"$\\mu = {mu8_p}$, $\\sigma = {sig8_p}$",
             solution=("Standardising, $\\dfrac{200 - \\mu}{\\sigma} = "
                       "-1.28155$ and $\\dfrac{260 - \\mu}{\\sigma} = "
                       "1.64485$. Subtracting the first from the second:"
                       f"$$60 = (1.64485 + 1.28155)\\sigma \\Rightarrow "
                       f"\\sigma = {sig(N(sigma8, 12))} \\approx {sig8_p}.$$"
                       f"$$\\mu = 200 + 1.28155\\sigma = "
                       f"{sig(N(mu8, 12))} \\approx {mu8_p}.$$"),
             verify=[f"Abs((260 - 200)/(sqrt(2)*erfinv(Rational(9,10)) "
                     f"- sqrt(2)*erfinv(Rational(-8,10))) - {sig8_p}) "
                     f"< {sig8_tol}"]),
        part("b", "Find $P(210 < M < 240)$.", 3,
             [M1("standardise both bounds with the unrounded $\\mu, \\sigma$"),
              M1("normal cdf between the two $z$-values (GDC)"),
              A1(f"$P(210 < M < 240) = {pmid_p}$ "
                 f"$({sig(N(p_mid, 12))}\\ldots)$")],
             answer=f"${pmid_p}$",
             solution=("Using the unrounded $\\mu = 226.28$ and $\\sigma = "
                       "20.50$,"
                       f"$$P(210 < M < 240) = {sig(N(p_mid, 12))} \\approx "
                       f"{pmid_p}.$$"),
             verify=["Abs(((1 + erf(0.66936/sqrt(2)))/2"
                     " - (1 + erf(-0.79383/sqrt(2)))/2) - 0.535) < 0.01"]),
        part("c", "Find the mass that is exceeded by only $1\\%$ of the"
             " apples.", 3,
             [M1("solve $P(M > m) = 0.01$, i.e. the $99$th percentile"),
              A1("$m = \\mu + 2.3263\\ldots\\,\\sigma$"),
              A1(f"$m = {p99_p}$ g $({sig(N(perc99, 12))}\\ldots)$")],
             answer=f"$m = {p99_p}$ g",
             solution=("The $99$th percentile satisfies $P(M > m) = 0.01$:"
                       f"$$m = \\mu + 2.32635\\,\\sigma = "
                       f"{sig(N(perc99, 12))} \\approx {p99_p} \\text{{ g}}."
                       "$$"),
             verify=["Abs(226.276 + 20.5033*sqrt(2)*erfinv(Rational(98, 100))"
                     f" - {p99_p}) < {p99_tol}"]),
    ]))

# ── Q9 [15] calculus (Section B): kinematics, displacement vs distance ───
v9 = t ** 2 - 4 * t + 3
assert sorted(solve(Eq(v9, 0), t)) == [1, 3]
a9 = diff(v9, t)
assert a9 == 2 * t - 4 and solve(Eq(a9, 0), t) == [2]
disp9 = integrate(v9, (t, 0, 4))
assert disp9 == Rational(4, 3)
d01 = integrate(v9, (t, 0, 1))
d13 = integrate(v9, (t, 1, 3))
d34 = integrate(v9, (t, 3, 4))
assert d01 == Rational(4, 3) and d13 == Rational(-4, 3) and d34 == Rational(4, 3)
total9 = abs(d01) + abs(d13) + abs(d34)
assert total9 == 4
assert v9.subs(t, 0) == 3 and v9.subs(t, 4) == 3
QS.append(question(
    "IB-AASL-P2-T4-Q9", 9, "B", "calculus", "kinematics",
    contextIntro=("A particle $P$ moves in a straight line. Its velocity, in"
                  " m s$^{-1}$, at time $t$ seconds is given by "
                  "$v(t) = t^2 - 4t + 3$ for $0 \\le t \\le 4$."),
    parts=[
        part("a", "Find the times at which $P$ is at rest.", 2,
             [M1("solve $v(t) = 0$: $(t - 1)(t - 3) = 0$"),
              A1("$t = 1$ and $t = 3$")],
             answer="$t = 1$ and $t = 3$ seconds",
             solution=("$$v(t) = t^2 - 4t + 3 = (t - 1)(t - 3) = 0 "
                       "\\Rightarrow t = 1, 3.$$"),
             verify=["Eq(1**2 - 4*1 + 3, 0)", "Eq(3**2 - 4*3 + 3, 0)"]),
        part("b", "Find the acceleration of $P$ when $t = 2$, and state what"
             " this tells you about the motion at that instant.", 3,
             [M1("$a(t) = v'(t) = 2t - 4$"),
              A1("$a(2) = 0$"),
              R1("the velocity is a minimum (speed greatest in that phase)"
                 " when $a = 0$")],
             answer="$a(2) = 0$",
             solution=("$$a(t) = v'(t) = 2t - 4 \\Rightarrow a(2) = 0.$$"
                       " At $t = 2$ the acceleration is zero, so the velocity"
                       " is momentarily neither increasing nor decreasing"
                       " (a turning point of $v$)."),
             verify=["Eq(diff(t**2 - 4*t + 3, t).subs(t, 2), 0)"]),
        part("c", "Find the displacement of $P$ from its starting point over"
             " the interval $0 \\le t \\le 4$.", 3,
             [M1("displacement $= \\displaystyle\\int_0^4 v(t)\\,dt$"),
              A1("antiderivative $\\tfrac{t^3}{3} - 2t^2 + 3t$"),
              A1("$\\dfrac{4}{3}$ m")],
             answer="$\\dfrac{4}{3}$ m",
             solution=("$$\\int_0^4 (t^2 - 4t + 3)\\,dt = "
                       "\\left[\\frac{t^3}{3} - 2t^2 + 3t\\right]_0^4 = "
                       "\\frac{64}{3} - 32 + 12 = \\frac{4}{3} \\text{ m}.$$"),
             verify=["Eq(integrate(t**2 - 4*t + 3, (t, 0, 4)),"
                     " Rational(4, 3))"]),
        part("d", "Find the total distance travelled by $P$ over the"
             " interval $0 \\le t \\le 4$.", 4,
             [M1("the velocity changes sign at $t = 1$ and $t = 3$"),
              M1("integrate over each interval and take absolute values"),
              A1("$\\tfrac43 + \\tfrac43 + \\tfrac43$"),
              A1("total distance $= 4$ m")],
             answer="$4$ m",
             solution=("$v > 0$ on $(0, 1)$ and $(3, 4)$ and $v < 0$ on"
                       " $(1, 3)$:"
                       "$$\\int_0^1 v = \\frac43, \\quad \\int_1^3 v = "
                       "-\\frac43, \\quad \\int_3^4 v = \\frac43,$$"
                       "$$\\text{distance} = \\frac43 + \\frac43 + \\frac43 "
                       "= 4 \\text{ m}.$$"),
             verify=["Eq(integrate(t**2 - 4*t + 3, (t, 0, 1)), Rational(4,3))",
                     "Eq(integrate(t**2 - 4*t + 3, (t, 1, 3)),"
                     " Rational(-4,3))",
                     "Eq(integrate(t**2 - 4*t + 3, (t, 3, 4)), Rational(4,3))"]),
        part("e", "Find the maximum speed of $P$ over the interval"
             " $0 \\le t \\le 4$.", 3,
             [M1("check the velocity at the endpoints and the turning"
                 " point"),
              A1("$v(0) = 3$, $v(2) = -1$, $v(4) = 3$"),
              A1("maximum speed $= 3$ m s$^{-1}$")],
             answer="$3$ m s$^{-1}$",
             solution=("Speed is $|v|$. The interior turning point gives"
                       " $v(2) = -1$ (speed $1$), while the endpoints give"
                       " $v(0) = v(4) = 3$:"
                       "$$\\text{maximum speed} = 3 \\text{ m s}^{-1}.$$"),
             verify=["Eq((t**2 - 4*t + 3).subs(t, 0), 3)",
                     "Eq((t**2 - 4*t + 3).subs(t, 2), -1)",
                     "Eq((t**2 - 4*t + 3).subs(t, 4), 3)"]),
    ]))

META = {"course": "aa", "level": "sl", "paper": 2, "testId": "ib-practice-4",
        "label": "AA SL Practice Paper 2", "timeMinutes": 90,
        "totalMarks": 80, "calculator": True}

if __name__ == "__main__":
    write_paper(META, QS, "data/ib/aa-sl/ib-practice-4/paper2.json")
