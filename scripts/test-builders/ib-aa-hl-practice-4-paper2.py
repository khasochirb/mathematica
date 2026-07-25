"""AA HL Practice Paper 2 (ib-hl-practice-4) — 120 min, 110 marks, GDC required.

Blueprint (topic x marks):
    Section A (52): Q1 number_algebra 7  | Q2 functions 7
                    Q3 geometry_trig 8   | Q4 stats_probability 7
                    Q5 calculus 8        | Q6 functions 7
                    Q7 number_algebra 8
    Section B (58): Q8 calculus 20 | Q9 geometry_trig 20
                    Q10 stats_probability 18
    Paper totals: number_algebra 15 | functions 14 | geometry_trig 28 |
                  stats_probability 25 | calculus 28 = 110.

Fresh HL archetypes versus Sets 1-3: an arithmetic seating plan, a cubic
whose roots and turning points come from the GDC, a cuboid's space
diagonal and its angle with the base, a binomial B(15, 0.35), open-box
optimisation, an absolute-value equation and the matching inequality, a
bouncing-ball geometric series, kinematics on v = 4 sin t - t (rest
times, maximum speed, displacement versus total distance), a triangle
with an ANGLE BISECTOR (cosine rule, sine rule, area, bisector theorem),
and bivariate statistics (correlation, least-squares regression,
interpretation, and the limits of extrapolation). GDC conventions: exact
where possible, otherwise 3 significant figures.
Figures: Q8 (velocity graph), Q9 (triangle with the bisector).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ibbuild import ROOT, A1, AG, M1, R1, part, question, write_paper  # noqa: E402

from sympy import (Rational, sqrt, pi, Eq, N, exp, log, sin, cos, asin,  # noqa: F401,E402
                   acos, atan, integrate, diff, expand, solve, simplify,
                   binomial, symbols, Abs, nsolve, rad, deg, Integer, Sum)

x, t, n = symbols("x t n")


def png(name, alt_en):
    from PIL import Image
    p = os.path.join(ROOT, "public", "ib-figures", name)
    assert os.path.isfile(p), f"figure missing on disk: {p} — run the figure script first"
    with Image.open(p) as im_:
        w, h = im_.size
    return {"src": f"/ib-figures/{name}", "width": w, "height": h, "alt_en": alt_en}


QS = []

# ── Q1 [7] number_algebra: an arithmetic seating plan ───────────────────
assert 24 + 19 * 3 == 81
assert Rational(20, 2) * (24 + 81) == 1050
assert 24 + 3 * (13 - 1) == 60 and 24 + 3 * (12 - 1) == 57
QS.append(question(
    "IB-AAHL-P2-T4-Q1", 1, "A", "number_algebra", "arithmetic_sequences",
    contextIntro=("A theatre has $20$ rows of seats. The first row has"
                  " $24$ seats, and each row after the first has $3$ more"
                  " seats than the row in front of it."),
    parts=[
        part("a", "Find the number of seats in the last row.", 2,
             [M1("$u_{20} = 24 + 19(3)$"),
              A1("$81$")],
             answer="$81$ seats",
             solution=("The rows form an arithmetic sequence with"
                       " $u_1 = 24$ and $d = 3$. The twentieth term is"
                       "$$u_{20} = 24 + (20 - 1)(3) = 24 + 57 = 81.$$"
                       " Note the multiplier is $19$, not $20$ — there are"
                       " nineteen steps between the first and twentieth"
                       " rows."),
             verify=["Eq(24 + 19*3, 81)", "Eq(20 - 1, 19)"]),
        part("b", "Find the total number of seats in the theatre.", 3,
             [M1("$S_{20} = \\dfrac{20}{2}(u_1 + u_{20})$"),
              A1("$10(24 + 81)$"),
              A1("$1050$")],
             answer="$1050$ seats",
             solution=("Use the sum of an arithmetic series in the"
                       " first-and-last form:"
                       "$$S_{20} = \\frac{20}{2}\\left(u_1 + u_{20}\\right)"
                       " = 10(24 + 81) = 10(105) = 1050.$$"
                       " (The equivalent form"
                       " $\\tfrac{20}{2}\\left(2(24) + 19(3)\\right)$ gives"
                       " the same total.)"),
             verify=["Eq(Rational(20, 2)*(24 + 81), 1050)",
                     "Eq(Rational(20, 2)*(2*24 + 19*3), 1050)"]),
        part("c", "Find the number of the first row that has at least $60$"
             " seats.", 2,
             [M1("solve $24 + 3(n - 1) \\ge 60$"),
              A1("row $13$")],
             answer="row $13$",
             solution=("Set up the inequality"
                       "$$24 + 3(n - 1) \\ge 60 \\;\\Rightarrow\\;"
                       " 3(n - 1) \\ge 36 \\;\\Rightarrow\\; n \\ge 13.$$"
                       " Since $n$ counts rows it is an integer, so the"
                       " first such row is row $13$. Checking: row $12$"
                       " has $57$ seats and row $13$ has $60$."),
             verify=["Eq(24 + 3*(13 - 1), 60)", "Eq(24 + 3*(12 - 1), 57)",
                     "57 < 60"]),
    ]))

# ── Q2 [7] functions: a cubic explored on the GDC ──────────────────────
from sympy import real_roots  # noqa: E402
_r2 = sorted(float(r.evalf()) for r in real_roots(x**3 - 4 * x + 1))
assert abs(_r2[0] + 2.114908) < 1e-5 and abs(_r2[1] - 0.254102) < 1e-5
assert abs(_r2[2] - 1.860806) < 1e-5
QS.append(question(
    "IB-AAHL-P2-T4-Q2", 2, "A", "functions", "polynomial_functions",
    contextIntro=("The function $f$ is defined by"
                  " $f(x) = x^{3} - 4x + 1$ for $x \\in \\mathbb{R}$."),
    parts=[
        part("a", "Find all real zeros of $f$, giving your answers correct"
             " to three significant figures.", 3,
             [M1("sketch or solve on the GDC"),
              A1("$-2.11$ and $0.254$"),
              A1("$1.86$")],
             answer="$x = -2.11$, $x = 0.254$, $x = 1.86$",
             solution=("A cubic with a positive leading coefficient and"
                       " two turning points can cross the axis three"
                       " times, and this one does. Reading the three"
                       " intersections with $y = 0$ from the GDC,"
                       "$$x = -2.114907\\ldots, \\quad x = 0.25410\\ldots,"
                       " \\quad x = 1.86081\\ldots$$"
                       " To three significant figures the zeros are"
                       " $-2.11$, $0.254$ and $1.86$. (Note the middle"
                       " root needs three significant FIGURES, not three"
                       " decimal places.)"),
             verify=["Abs((Rational(-2114908,1000000))**3"
                     " - 4*Rational(-2114908,1000000) + 1) < Rational(1,1000)",
                     "Abs((Rational(254102,1000000))**3"
                     " - 4*Rational(254102,1000000) + 1) < Rational(1,1000)",
                     "Abs((Rational(1860806,1000000))**3"
                     " - 4*Rational(1860806,1000000) + 1) < Rational(1,1000)"]),
        part("b", "Find the coordinates of the local maximum and the local"
             " minimum of the graph of $f$, giving your answers correct to"
             " three significant figures.", 4,
             [M1("solve $f'(x) = 3x^{2} - 4 = 0$"),
              A1("$x = \\pm\\dfrac{2}{\\sqrt{3}}"
                 " = \\pm 1.1547\\ldots$"),
              A1("local maximum $(-1.15,\\ 4.08)$"),
              A1("local minimum $(1.15,\\ -2.08)$")],
             answer="maximum $(-1.15,\\ 4.08)$; minimum"
                    " $(1.15,\\ -2.08)$",
             solution=("Differentiate and set to zero:"
                       "$$f'(x) = 3x^{2} - 4 = 0 \\;\\Rightarrow\\;"
                       " x = \\pm\\frac{2}{\\sqrt{3}}"
                       " = \\pm 1.15470\\ldots$$"
                       " Since $f'' (x) = 6x$, the negative root gives"
                       " $f'' < 0$ (a maximum) and the positive root gives"
                       " $f'' > 0$ (a minimum). Evaluating,"
                       "$$f(-1.1547\\ldots) = 4.07920\\ldots, \\qquad"
                       " f(1.1547\\ldots) = -2.07920\\ldots$$"
                       " So the local maximum is $(-1.15,\\ 4.08)$ and the"
                       " local minimum is $(1.15,\\ -2.08)$."),
             verify=["Eq(diff(x**3 - 4*x + 1, x), 3*x**2 - 4)",
                     "Eq(solve(Eq(3*x**2 - 4, 0), x)[1], 2*sqrt(3)/3)",
                     "Abs((-2*sqrt(3)/3)**3 - 4*(-2*sqrt(3)/3) + 1"
                     " - Rational(408,100)) < Rational(1,100)",
                     "Abs((2*sqrt(3)/3)**3 - 4*(2*sqrt(3)/3) + 1"
                     " + Rational(208,100)) < Rational(1,100)"]),
    ]))

# ── Q3 [8] geometry_trig: a cuboid's space diagonal ────────────────────
assert 5**2 + 12**2 == 13**2
assert 5**2 + 12**2 + 9**2 == 250
assert abs(float(deg(atan(Rational(9, 13)))) - 34.695) < 0.01
QS.append(question(
    "IB-AAHL-P2-T4-Q3", 3, "A", "geometry_trig", "3d_geometry",
    contextIntro=("A cuboid has a rectangular base measuring $5$ cm by"
                  " $12$ cm and a height of $9$ cm."),
    parts=[
        part("a", "Find the exact length of a space diagonal of the"
             " cuboid.", 3,
             [M1("base diagonal $\\sqrt{5^{2} + 12^{2}} = 13$"),
              M1("space diagonal $\\sqrt{13^{2} + 9^{2}}$"),
              A1("$5\\sqrt{10}$ cm")],
             answer="$5\\sqrt{10}$ cm $\\approx 15.8$ cm",
             solution=("Work in two steps. The diagonal of the base is"
                       "$$\\sqrt{5^{2} + 12^{2}} = \\sqrt{169} = 13"
                       "\\ \\text{cm}.$$"
                       " That base diagonal and the vertical height form a"
                       " right triangle whose hypotenuse is the space"
                       " diagonal:"
                       "$$d = \\sqrt{13^{2} + 9^{2}} = \\sqrt{250}"
                       " = 5\\sqrt{10} \\approx 15.8\\ \\text{cm}.$$"
                       " Equivalently $d = \\sqrt{5^2 + 12^2 + 9^2}$ in one"
                       " step."),
             verify=["Eq(sqrt(5**2 + 12**2), 13)",
                     "Eq(simplify(sqrt(13**2 + 9**2)), 5*sqrt(10))",
                     "Eq(5**2 + 12**2 + 9**2, 250)"]),
        part("b", "Find the angle that this space diagonal makes with the"
             " base of the cuboid, correct to three significant figures.",
             5,
             [M1("the angle sits in the right triangle formed by the base"
                 " diagonal and the height"),
              A1("$\\tan\\theta = \\dfrac{9}{13}$"),
              M1("$\\theta = \\arctan\\dfrac{9}{13}$"),
              A1("$34.6947\\ldots^\\circ$"),
              A1("$34.7^\\circ$")],
             answer="$34.7^\\circ$",
             solution=("Drop the space diagonal onto the base: its shadow"
                       " is the base diagonal of length $13$, and the"
                       " vertical rise is the height $9$. The angle"
                       " $\\theta$ between the diagonal and the base"
                       " therefore satisfies"
                       "$$\\tan\\theta = \\frac{\\text{height}}"
                       "{\\text{base diagonal}} = \\frac{9}{13},$$"
                       " so"
                       "$$\\theta = \\arctan\\frac{9}{13}"
                       " = 34.6947\\ldots^\\circ \\approx 34.7^\\circ.$$"
                       " Using $\\tan\\theta = \\tfrac{9}{12}$ or"
                       " $\\tfrac{9}{5}$ — an edge rather than the base"
                       " DIAGONAL — is the usual error here."),
             verify=["Abs(deg(atan(Rational(9,13))) - Rational(347,10))"
                     " < Rational(1,10)",
                     "Abs(sin(atan(Rational(9,13))) - Rational(9,1)"
                     "/(5*sqrt(10))) < Rational(1,1000)"]),
    ]))

# ── Q4 [7] stats_probability: a binomial B(15, 0.35) ───────────────────
_p4 = Rational(35, 100)
_pmf = lambda kk: binomial(15, kk) * _p4**kk * (1 - _p4) ** (15 - kk)
assert abs(float(_pmf(5)) - 0.2123) < 0.0005
assert 15 * _p4 == Rational(21, 4)
_ge7 = 1 - sum(_pmf(i) for i in range(0, 7))
assert abs(float(_ge7) - 0.245158) < 0.00001
QS.append(question(
    "IB-AAHL-P2-T4-Q4", 4, "A", "stats_probability", "binomial_distribution",
    contextIntro=("A random variable $X$ follows a binomial distribution"
                  " with $n = 15$ trials and probability of success"
                  " $p = 0.35$ on each trial."),
    parts=[
        part("a", "Find $P(X = 5)$, correct to three significant figures.",
             3,
             [M1("$\\binom{15}{5}(0.35)^{5}(0.65)^{10}$"),
              A1("$3003 \\times 0.0052522\\ldots \\times"
                 " 0.0134627\\ldots$"),
              A1("$0.212$")],
             answer="$0.212$ (3 s.f.)",
             solution=("Use the binomial probability formula:"
                       "$$P(X = 5) = \\binom{15}{5}(0.35)^{5}"
                       "(0.65)^{10}.$$"
                       " Here $\\binom{15}{5} = 3003$, and evaluating"
                       " gives"
                       "$$P(X = 5) = 0.21234\\ldots \\approx 0.212.$$"),
             verify=["Eq(binomial(15, 5), 3003)",
                     "Abs(binomial(15,5)*Rational(35,100)**5"
                     "*Rational(65,100)**10 - Rational(212,1000))"
                     " < Rational(1,1000)"]),
        part("b", "Find $\\mathrm{E}(X)$.", 2,
             [M1("$\\mathrm{E}(X) = np$"),
              A1("$5.25$")],
             answer="$\\mathrm{E}(X) = 5.25$",
             solution=("For a binomial distribution the mean is"
                       "$$\\mathrm{E}(X) = np = 15 \\times 0.35 = 5.25.$$"
                       " An expected value need not be a whole number even"
                       " though $X$ only takes whole values."),
             verify=["Eq(15*Rational(35,100), Rational(21,4))",
                     "Eq(Rational(21,4), Rational(525,100))"]),
        part("c", "Find $P(X \\ge 7)$, correct to three significant"
             " figures.", 2,
             [M1("$1 - P(X \\le 6)$"),
              A1("$0.245$")],
             answer="$0.245$ (3 s.f.)",
             solution=("Cumulative binomial tables and calculators give"
                       " $P(X \\le k)$, so use the complement:"
                       "$$P(X \\ge 7) = 1 - P(X \\le 6)"
                       " = 1 - 0.754842\\ldots = 0.245158\\ldots$$"
                       " To three significant figures this is $0.245$."
                       " Note the boundary: $X \\ge 7$ excludes $X = 6$,"
                       " so the complement stops at $6$, not $7$."),
             verify=["Abs(1 - Sum(binomial(15, n)*Rational(35,100)**n"
                     "*Rational(65,100)**(15 - n), (n, 0, 6)).doit()"
                     " - Rational(245,1000)) < Rational(1,1000)"]),
    ]))

# ── Q5 [8] calculus: open-box optimisation ─────────────────────────────
assert expand(x * (20 - 2 * x) * (30 - 2 * x)) == 4 * x**3 - 100 * x**2 + 600 * x
_xopt = [r for r in solve(Eq(12 * x**2 - 200 * x + 600, 0), x)
         if 0 < float(r) < 10][0]
assert abs(float(_xopt) - 3.9237) < 0.001
assert abs(float(_xopt * (20 - 2 * _xopt) * (30 - 2 * _xopt)) - 1056.3) < 0.5
QS.append(question(
    "IB-AAHL-P2-T4-Q5", 5, "A", "calculus", "optimisation",
    contextIntro=("An open box is made from a rectangular sheet of card"
                  " measuring $20$ cm by $30$ cm by cutting a square of"
                  " side $x$ cm from each corner and folding up the sides."),
    parts=[
        part("a", "Show that the volume $V$, in cubic centimetres, is given"
             " by $V = 4x^{3} - 100x^{2} + 600x$.", 3,
             [M1("base measures $(20 - 2x)$ by $(30 - 2x)$, height $x$"),
              A1("$V = x(20 - 2x)(30 - 2x)$"),
              AG()],
             answer="$V = 4x^{3} - 100x^{2} + 600x$ (given)",
             solution=("Cutting a square of side $x$ from each corner"
                       " removes $x$ from BOTH ends of each dimension, so"
                       " the folded base measures $(20 - 2x)$ by"
                       " $(30 - 2x)$ and the height is $x$:"
                       "$$V = x(20 - 2x)(30 - 2x).$$"
                       " Expanding the two brackets first,"
                       " $(20 - 2x)(30 - 2x) = 600 - 100x + 4x^{2}$, so"
                       "$$V = x\\left(4x^{2} - 100x + 600\\right)"
                       " = 4x^{3} - 100x^{2} + 600x.$$"),
             verify=["Eq(expand(x*(20 - 2*x)*(30 - 2*x)),"
                     " 4*x**3 - 100*x**2 + 600*x)",
                     "Eq(expand((20 - 2*x)*(30 - 2*x)),"
                     " 4*x**2 - 100*x + 600)"]),
        part("b", "Find the value of $x$ that maximises $V$, and the"
             " maximum volume, each correct to three significant figures.",
             5,
             [M1("$\\dfrac{dV}{dx} = 12x^{2} - 200x + 600$"),
              M1("solve $\\dfrac{dV}{dx} = 0$"),
              A1("roots $3.9237\\ldots$ and $12.74\\ldots$"),
              R1("only $x = 3.92$ lies in the valid range $0 < x < 10$"),
              A1("$V_{\\max} = 1060$ cm$^{3}$ (3 s.f.)")],
             answer="$x = 3.92$ cm, giving $V_{\\max} = 1060$ cm$^{3}$"
                    " (3 s.f.)",
             solution=("Differentiate and set to zero:"
                       "$$\\frac{dV}{dx} = 12x^{2} - 200x + 600 = 0"
                       " \\;\\Rightarrow\\; 3x^{2} - 50x + 150 = 0.$$"
                       " The quadratic formula gives"
                       "$$x = \\frac{50 \\pm \\sqrt{2500 - 1800}}{6}"
                       " = \\frac{50 \\pm \\sqrt{700}}{6},$$"
                       " that is $x = 3.92374\\ldots$ or"
                       " $x = 12.7429\\ldots$"
                       " The physical constraint is $0 < x < 10$ — the"
                       " shorter side is only $20$ cm, so cutting $x$ from"
                       " both ends needs $2x < 20$. Hence"
                       " $x = 3.92$ cm, and"
                       "$$V = 3.92374(20 - 7.84748)(30 - 7.84748)"
                       " = 1056.3\\ldots$$"
                       " so $V_{\\max} = 1060$ cm$^{3}$ to three"
                       " significant figures."),
             verify=["Eq(diff(4*x**3 - 100*x**2 + 600*x, x),"
                     " 12*x**2 - 200*x + 600)",
                     "Abs(12*Rational(392374,100000)**2"
                     " - 200*Rational(392374,100000) + 600) < Rational(1,100)",
                     "Abs(Rational(392374,100000)"
                     "*(20 - 2*Rational(392374,100000))"
                     "*(30 - 2*Rational(392374,100000)) - 1056) < 1",
                     "2*Rational(392374,100000) < 20"]),
    ]))

# ── Q6 [7] functions: an absolute-value equation and inequality ────────
assert Abs(2 * 6 - 5) == 6 + 1
assert Abs(2 * Rational(4, 3) - 5) == Rational(4, 3) + 1
QS.append(question(
    "IB-AAHL-P2-T4-Q6", 6, "A", "functions", "absolute_value",
    parts=[
        part("a", "Solve $|2x - 5| = x + 1$.", 4,
             [M1("split into the two cases"
                 " $2x - 5 = \\pm(x + 1)$"),
              A1("$x = 6$"),
              A1("$x = \\dfrac{4}{3}$"),
              R1("both satisfy $x + 1 \\ge 0$, so both are valid")],
             answer="$x = \\dfrac{4}{3}$ or $x = 6$",
             solution=("An absolute value equals $x + 1$ when the inside"
                       " is $x + 1$ or $-(x + 1)$:"
                       "$$2x - 5 = x + 1 \\;\\Rightarrow\\; x = 6,$$"
                       "$$2x - 5 = -(x + 1) \\;\\Rightarrow\\; 3x = 4"
                       " \\;\\Rightarrow\\; x = \\frac{4}{3}.$$"
                       " Squaring introduces false roots whenever the"
                       " right side is negative, so check both: at $x = 6$"
                       " the two sides are $|7| = 7$; at"
                       " $x = \\tfrac{4}{3}$ they are"
                       " $\\left|-\\tfrac{7}{3}\\right| = \\tfrac{7}{3}$."
                       " Both are genuine solutions."),
             verify=["Eq(Abs(2*6 - 5), 6 + 1)",
                     "Eq(Abs(2*Rational(4,3) - 5), Rational(4,3) + 1)",
                     "Eq(Rational(4,3) + 1, Rational(7,3))"]),
        part("b", "Hence solve $|2x - 5| < x + 1$.", 3,
             [M1("the two sides are equal at"
                 " $x = \\dfrac{4}{3}$ and $x = 6$"),
              M1("test a value between them, e.g. $x = 3$:"
                 " $|1| < 4$"),
              A1("$\\dfrac{4}{3} < x < 6$")],
             answer="$\\dfrac{4}{3} < x < 6$",
             solution=("The two graphs $y = |2x - 5|$ and $y = x + 1$ can"
                       " only swap over at the points where they meet,"
                       " which part (a) found at $x = \\tfrac{4}{3}$ and"
                       " $x = 6$. Testing one point in each region settles"
                       " the direction:"
                       "$$x = 0:\\ |{-5}| = 5 \\not< 1, \\qquad"
                       " x = 3:\\ |1| = 1 < 4, \\qquad"
                       " x = 8:\\ |11| = 11 \\not< 9.$$"
                       " So the V-shaped graph dips below the line exactly"
                       " between the crossings:"
                       "$$\\frac{4}{3} < x < 6.$$"),
             verify=["Abs(2*3 - 5) < 3 + 1", "Abs(2*0 - 5) > 0 + 1",
                     "Abs(2*8 - 5) > 8 + 1"]),
    ]))

# ── Q7 [8] number_algebra: a bouncing ball (geometric) ─────────────────
assert 2 * Rational(8, 10) ** 5 == Rational(16384, 25000)
assert abs(float(2 * Rational(8, 10) ** 5) - 0.65536) < 1e-9
assert 2 + 4 * (Rational(8, 10) / (1 - Rational(8, 10))) == 18
QS.append(question(
    "IB-AAHL-P2-T4-Q7", 7, "A", "number_algebra", "geometric_sequences",
    contextIntro=("A ball is dropped from a height of $2$ metres. After"
                  " each bounce it rises to $80\\%$ of the height it fell"
                  " from."),
    parts=[
        part("a", "Find the height the ball rises to after the fifth"
             " bounce, correct to three significant figures.", 3,
             [M1("geometric with $r = 0.8$"),
              A1("$2(0.8)^{5}$"),
              A1("$0.655$ metres")],
             answer="$0.655$ metres (3 s.f.)",
             solution=("Each bounce multiplies the peak height by $0.8$,"
                       " so after five bounces the ball rises to"
                       "$$2(0.8)^{5} = 2(0.32768) = 0.65536"
                       "\\ \\text{m},$$"
                       " which is $0.655$ m to three significant"
                       " figures."),
             verify=["Eq(2*Rational(8,10)**5, Rational(16384,25000))",
                     "Abs(2*Rational(8,10)**5 - Rational(655,1000))"
                     " < Rational(1,1000)"]),
        part("b", "Find the total vertical distance travelled by the ball"
             " before it comes to rest.", 5,
             [M1("the first drop is $2$ m, and every later stage is"
                 " counted twice (up and down)"),
              A1("total $= 2 + 2\\displaystyle\\sum_{n=1}^{\\infty}"
                 " 2(0.8)^{n}$"),
              M1("sum to infinity"
                 " $\\dfrac{u_1}{1 - r}$ with $u_1 = 1.6$, $r = 0.8$"),
              A1("$\\dfrac{1.6}{0.2} = 8$, doubled gives $16$"),
              A1("$18$ metres")],
             answer="$18$ metres",
             solution=("The ball first falls $2$ m. After that, each"
                       " bounce contributes its rise AND the equal fall"
                       " that follows, so every later height is counted"
                       " twice:"
                       "$$D = 2 + 2\\left[2(0.8) + 2(0.8)^{2}"
                       " + 2(0.8)^{3} + \\cdots\\right].$$"
                       " The bracket is an infinite geometric series with"
                       " first term $1.6$ and ratio $0.8$, and since"
                       " $|r| < 1$ it converges:"
                       "$$\\sum = \\frac{1.6}{1 - 0.8} = \\frac{1.6}{0.2}"
                       " = 8.$$"
                       " Therefore"
                       "$$D = 2 + 2(8) = 18\\ \\text{metres}.$$"
                       " Forgetting to double the post-bounce heights"
                       " gives $10$ m, which is the single most common"
                       " error on this classic."),
             verify=["Eq(Rational(16,10)/(1 - Rational(8,10)), 8)",
                     "Eq(2 + 2*8, 18)",
                     "Abs(Rational(8,10)) < 1"]),
    ]))

# ── Q8 [20] calculus: kinematics on v(t) = 4 sin t - t ────────────────
_v = 4 * sin(t) - t
_trest = nsolve(Eq(_v, 0), t, 2.5)
assert abs(float(_trest) - 2.47458) < 0.001
_tmax = nsolve(Eq(diff(_v, t), 0), t, 1.3)
assert abs(float(_tmax) - 1.31812) < 0.001
assert abs(float(_v.subs(t, _tmax)) - 2.55487) < 0.001
assert abs(float(integrate(_v, (t, 0, 4))) + 1.38539) < 0.001
_d1 = float(integrate(_v, (t, 0, _trest)))
_d2 = float(integrate(_v, (t, _trest, 4)))
assert abs(_d1 - abs(_d2) - (4.08329 - 5.46868)) < 0.01
assert abs((_d1 + abs(_d2)) - 9.55197) < 0.01
QS.append(question(
    "IB-AAHL-P2-T4-Q8", 8, "B", "calculus", "kinematics",
    contextIntro=("A particle moves in a straight line. Its velocity, in"
                  " metres per second, is given by"
                  " $v(t) = 4\\sin t - t$ for $0 \\le t \\le 4$, where $t$"
                  " is in seconds and the sine is in radians. The diagram"
                  " shows the graph of $v$ against $t$."),
    figure=None,
    parts=[
        part("a", "Find the time in $0 < t \\le 4$ at which the particle is"
             " momentarily at rest, correct to three significant figures.",
             3,
             [M1("solve $4\\sin t - t = 0$ on the GDC"),
              A1("$t = 2.47458\\ldots$"),
              A1("$t = 2.47$ seconds")],
             answer="$t = 2.47$ seconds",
             solution=("The particle is at rest when $v(t) = 0$, that is"
                       " where"
                       "$$4\\sin t = t.$$"
                       " Besides the trivial $t = 0$ at which the motion"
                       " starts, the graph crosses the axis once more in"
                       " the given interval. Solving on the GDC,"
                       "$$t = 2.47458\\ldots \\approx 2.47"
                       "\\ \\text{seconds}.$$"
                       " (For $t > \\pi$ the sine is negative while $t$ is"
                       " positive, so there is no further crossing before"
                       " $t = 4$.)"),
             verify=["Abs(4*sin(Rational(247458,100000))"
                     " - Rational(247458,100000)) < Rational(1,1000)",
                     "4*sin(2) - 2 > 0", "4*sin(3) - 3 < 0"]),
        part("b", "Find the maximum velocity of the particle, correct to"
             " three significant figures.", 4,
             [M1("solve $v'(t) = 4\\cos t - 1 = 0$"),
              A1("$t = 1.31812\\ldots$"),
              M1("substitute back into $v$"),
              A1("$2.55$ m s$^{-1}$")],
             answer="$2.55$ metres per second",
             solution=("Velocity is greatest where its own derivative"
                       " vanishes:"
                       "$$v'(t) = 4\\cos t - 1 = 0 \\;\\Rightarrow\\;"
                       " \\cos t = \\frac{1}{4},$$"
                       " so $t = 1.31812\\ldots$ within the interval."
                       " Substituting back,"
                       "$$v(1.31812\\ldots)"
                       " = 4\\sin(1.31812\\ldots) - 1.31812\\ldots"
                       " = 2.55487\\ldots$$"
                       " The maximum velocity is $2.55$ m s$^{-1}$."
                       " (This is a maximum because"
                       " $v''(t) = -4\\sin t < 0$ there.)"),
             verify=["Abs(4*cos(Rational(131812,100000)) - 1)"
                     " < Rational(1,1000)",
                     "Abs(4*sin(Rational(131812,100000))"
                     " - Rational(131812,100000) - Rational(255,100))"
                     " < Rational(1,100)"]),
        part("c", "Find the displacement of the particle from its starting"
             " point after $4$ seconds, correct to three significant"
             " figures.", 4,
             [M1("displacement"
                 " $= \\displaystyle\\int_{0}^{4} v(t)\\,dt$"),
              A1("$\\left[-4\\cos t - \\dfrac{t^{2}}{2}\\right]_{0}^{4}$"),
              A1("$-1.38539\\ldots$"),
              A1("$-1.39$ metres")],
             answer="$-1.39$ metres (that is, $1.39$ m behind the start)",
             solution=("Displacement is the SIGNED integral of velocity:"
                       "$$s = \\int_{0}^{4}\\left(4\\sin t - t\\right)dt"
                       " = \\left[-4\\cos t - \\frac{t^{2}}{2}"
                       "\\right]_{0}^{4}.$$"
                       " Evaluating,"
                       "$$= \\left(-4\\cos 4 - 8\\right)"
                       " - \\left(-4\\right) = -1.38539\\ldots$$"
                       " So the particle finishes $1.39$ metres on the"
                       " negative side of where it started."),
             verify=["Abs(integrate(4*sin(t) - t, (t, 0, 4))"
                     " + Rational(139,100)) < Rational(1,100)",
                     "Eq(diff(-4*cos(t) - t**2/2, t), 4*sin(t) - t)"]),
        part("d", "Find the total distance travelled by the particle during"
             " the first $4$ seconds, correct to three significant"
             " figures.", 4,
             [M1("split the integral where $v$ changes sign, at"
                 " $t = 2.47458\\ldots$"),
              A1("$\\displaystyle\\int_{0}^{2.4746} v\\,dt"
                 " = 4.08329\\ldots$"),
              A1("$\\displaystyle\\int_{2.4746}^{4} v\\,dt"
                 " = -5.46868\\ldots$"),
              A1("total distance $= 9.55$ metres")],
             answer="$9.55$ metres",
             solution=("Distance ignores direction, so integrate the"
                       " MAGNITUDE of the velocity — in practice, split at"
                       " the sign change found in part (a) and add the"
                       " absolute values:"
                       "$$\\int_{0}^{2.4746} v\\,dt = 4.08329\\ldots,"
                       " \\qquad \\int_{2.4746}^{4} v\\,dt"
                       " = -5.46868\\ldots$$"
                       " Hence"
                       "$$\\text{distance} = 4.08329 + 5.46868"
                       " = 9.55197\\ldots \\approx 9.55\\ \\text{m}.$$"
                       " Compare with part (c): the displacement is only"
                       " $-1.39$ m, because the particle travels forwards"
                       " and then further back."),
             verify=["Abs(integrate(4*sin(t) - t,"
                     " (t, 0, Rational(247458,100000)))"
                     " - Rational(408,100)) < Rational(1,50)",
                     "Abs(integrate(4*sin(t) - t,"
                     " (t, Rational(247458,100000), 4))"
                     " + Rational(547,100)) < Rational(1,50)",
                     "Abs(Rational(408,100) + Rational(547,100)"
                     " - Rational(955,100)) < Rational(1,50)"]),
        part("e", "Find the acceleration of the particle at the instant it"
             " is momentarily at rest, correct to three significant"
             " figures, and state what it tells you about the motion.", 5,
             [M1("$a(t) = v'(t) = 4\\cos t - 1$"),
              M1("substitute $t = 2.47458\\ldots$"),
              A1("$4\\cos(2.47458\\ldots) = -3.14347\\ldots$"),
              A1("$a = -4.14$ m s$^{-2}$"),
              R1("the acceleration is negative while the velocity is zero,"
                 " so the particle is reversing direction there")],
             answer="$a = -4.14$ m s$^{-2}$; the particle is turning"
                    " round",
             solution=("Acceleration is the derivative of velocity:"
                       "$$a(t) = 4\\cos t - 1.$$"
                       " At the rest instant $t = 2.47458\\ldots$,"
                       "$$a = 4\\cos(2.47458\\ldots) - 1"
                       " = -3.14347\\ldots - 1 = -4.14347\\ldots,$$"
                       " so $a = -4.14$ m s$^{-2}$ to three significant"
                       " figures."
                       " Interpretation: the velocity is momentarily zero"
                       " but the acceleration is clearly negative, so the"
                       " particle does not stay at rest — it is changing"
                       " direction, having moved forwards up to this"
                       " instant and moving backwards afterwards. That"
                       " matches the split in part (d)."),
             verify=["Abs(4*cos(Rational(247458,100000)) - 1"
                     " + Rational(414,100)) < Rational(1,100)",
                     "4*cos(Rational(247458,100000)) - 1 < 0"]),
    ]))

# ── Q9 [20] geometry_trig: triangle with an angle bisector ─────────────
_A9 = rad(70)
_BC = sqrt(9**2 + 12**2 - 2 * 9 * 12 * cos(_A9))
assert abs(float(_BC) - 12.2933) < 0.001
_B9 = asin(12 * sin(_A9) / _BC)
assert abs(float(deg(_B9)) - 66.53129) < 0.001
assert abs(float(Rational(1, 2) * 9 * 12 * sin(_A9)) - 50.7434) < 0.001
assert abs(float(Rational(9, 21) * _BC) - 5.268530) < 0.0001
QS.append(question(
    "IB-AAHL-P2-T4-Q9", 9, "B", "geometry_trig", "triangle_trigonometry",
    contextIntro=("In triangle $ABC$, $AB = 9$ cm, $AC = 12$ cm and"
                  " $A\\hat{B}C$ is the angle at $B$. The angle"
                  " $B\\hat{A}C$ measures $70^\\circ$. The point $D$ lies"
                  " on $BC$ so that $AD$ bisects the angle at $A$, as shown"
                  " in the diagram."),
    figure=None,
    parts=[
        part("a", "Find the length of $BC$, correct to three significant"
             " figures.", 3,
             [M1("cosine rule"
                 " $BC^{2} = 9^{2} + 12^{2} - 2(9)(12)\\cos 70^\\circ$"),
              A1("$BC^{2} = 151.12\\ldots$"),
              A1("$BC = 12.3$ cm")],
             answer="$BC = 12.3$ cm",
             solution=("Two sides and the included angle are known, so use"
                       " the cosine rule:"
                       "$$BC^{2} = 9^{2} + 12^{2} - 2(9)(12)"
                       "\\cos 70^\\circ = 225 - 216(0.34202\\ldots).$$"
                       " That gives $BC^{2} = 151.124\\ldots$, so"
                       "$$BC = 12.2933\\ldots \\approx 12.3\\ \\text{cm}.$$"),
             verify=["Abs(sqrt(9**2 + 12**2 - 2*9*12*cos(rad(70)))"
                     " - Rational(123,10)) < Rational(1,10)",
                     "Eq(9**2 + 12**2, 225)"]),
        part("b", "Find the size of the angle at $B$, correct to three"
             " significant figures.", 4,
             [M1("sine rule"
                 " $\\dfrac{\\sin B}{12} = \\dfrac{\\sin 70^\\circ}{BC}$"),
              A1("$\\sin B = 0.917277\\ldots$"),
              R1("the angle opposite the shorter of $AC$ and $BC$ must be"
                 " acute, so take the acute value"),
              A1("$66.5^\\circ$")],
             answer="$66.5^\\circ$",
             solution=("Apply the sine rule, pairing each side with the"
                       " angle opposite it:"
                       "$$\\frac{\\sin B}{AC} = \\frac{\\sin A}{BC}"
                       " \\;\\Rightarrow\\; \\sin B"
                       " = \\frac{12\\sin 70^\\circ}{12.2933\\ldots}"
                       " = 0.917277\\ldots$$"
                       " The inverse sine gives $66.5313\\ldots^\\circ$;"
                       " the obtuse alternative $113.47^\\circ$ is"
                       " impossible here because $70^\\circ + 113.47^\\circ"
                       " > 180^\\circ$. So the angle at $B$ is"
                       " $66.5^\\circ$, and the remaining angle at $C$ is"
                       " about $43.5^\\circ$."),
             verify=["Abs(deg(asin(12*sin(rad(70))"
                     "/sqrt(9**2 + 12**2 - 2*9*12*cos(rad(70)))))"
                     " - Rational(665,10)) < Rational(1,10)",
                     "70 + 113 > 180"]),
        part("c", "Find the area of triangle $ABC$, correct to three"
             " significant figures.", 3,
             [M1("$\\tfrac{1}{2}ab\\sin C$ with the INCLUDED angle"),
              A1("$\\tfrac{1}{2}(9)(12)\\sin 70^\\circ$"),
              A1("$50.7$ cm$^{2}$")],
             answer="$50.7$ cm$^{2}$",
             solution=("The area formula needs two sides and the angle"
                       " BETWEEN them, which is exactly what is given:"
                       "$$\\text{Area} = \\tfrac{1}{2}(AB)(AC)\\sin A"
                       " = \\tfrac{1}{2}(9)(12)\\sin 70^\\circ"
                       " = 54(0.93969\\ldots).$$"
                       " So the area is $50.7434\\ldots \\approx 50.7$"
                       " cm$^{2}$."),
             verify=["Abs(Rational(1,2)*9*12*sin(rad(70))"
                     " - Rational(507,10)) < Rational(1,10)",
                     "Eq(Rational(1,2)*9*12, 54)"]),
        part("d", "Find the length of $BD$, correct to three significant"
             " figures.", 5,
             [M1("the angle bisector divides $BC$ in the ratio of the"
                 " adjacent sides"),
              A1("$\\dfrac{BD}{DC} = \\dfrac{AB}{AC} = \\dfrac{9}{12}"
                 " = \\dfrac{3}{4}$"),
              M1("so $BD = \\dfrac{3}{7}BC$"),
              A1("$\\dfrac{3}{7}(12.2933\\ldots)$"),
              A1("$BD = 5.27$ cm")],
             answer="$BD = 5.27$ cm",
             solution=("The angle-bisector theorem says the bisector from"
                       " $A$ cuts the opposite side in the ratio of the"
                       " two sides that meet at $A$:"
                       "$$\\frac{BD}{DC} = \\frac{AB}{AC}"
                       " = \\frac{9}{12} = \\frac{3}{4}.$$"
                       " So $BD$ is three of the seven equal parts of"
                       " $BC$:"
                       "$$BD = \\frac{3}{7}(12.2933\\ldots)"
                       " = 5.26857\\ldots \\approx 5.27\\ \\text{cm}.$$"
                       " (As a check, $DC = \\tfrac{4}{7}BC = 7.02$ cm and"
                       " $BD + DC = BC$.)"),
             verify=["Eq(Rational(9, 12), Rational(3,4))",
                     "Abs(Rational(3,7)"
                     "*sqrt(9**2 + 12**2 - 2*9*12*cos(rad(70)))"
                     " - Rational(527,100)) < Rational(1,100)",
                     "Eq(Rational(3,7) + Rational(4,7), 1)"]),
        part("e", "Find the length of $AD$, correct to three significant"
             " figures.", 5,
             [M1("in triangle $ABD$ the angle at $A$ is $35^\\circ$"),
              A1("angle $A\\hat{D}B = 180 - 35 - 66.5313"
                 " = 78.4687\\ldots^\\circ$"),
              M1("sine rule"
                 " $\\dfrac{AD}{\\sin B} = \\dfrac{AB}{\\sin A\\hat{D}B}$"),
              A1("$AD = \\dfrac{9\\sin 66.5313^\\circ}"
                 "{\\sin 78.4687^\\circ}$"),
              A1("$AD = 8.43$ cm")],
             answer="$AD = 8.43$ cm",
             solution=("Work inside triangle $ABD$. The bisector halves"
                       " the $70^\\circ$ angle, so $B\\hat{A}D"
                       " = 35^\\circ$, and from part (b) the angle at $B$"
                       " is $66.5313\\ldots^\\circ$. The third angle is"
                       "$$A\\hat{D}B = 180^\\circ - 35^\\circ"
                       " - 66.5313^\\circ = 78.4687\\ldots^\\circ.$$"
                       " Now the sine rule in that triangle gives"
                       "$$AD = \\frac{AB\\sin B}{\\sin A\\hat{D}B}"
                       " = \\frac{9(0.917277\\ldots)}{0.979637\\ldots}"
                       " = 8.42556\\ldots$$"
                       " So $AD = 8.43$ cm. It is shorter than both $AB$"
                       " and $AC$, as a cevian to the opposite side must"
                       " be here."),
             verify=["Eq(70/2, 35)",
                     "Abs(180 - 35 - deg(asin(12*sin(rad(70))"
                     "/sqrt(9**2 + 12**2 - 2*9*12*cos(rad(70)))))"
                     " - Rational(7847,100)) < Rational(1,10)",
                     "Abs(9*sin(rad(Rational(665313,10000)))"
                     "/sin(rad(Rational(784687,10000)))"
                     " - Rational(843,100)) < Rational(1,50)"]),
    ]))

# ── Q10 [18] stats_probability: bivariate statistics ───────────────────
XS = [2, 3, 5, 6, 7, 8, 9, 10]
YS = [42, 50, 63, 72, 78, 85, 91, 100]
_n = len(XS)
_sxy = sum(a * b for a, b in zip(XS, YS)) - Rational(sum(XS) * sum(YS), _n)
_sxx = sum(a * a for a in XS) - Rational(sum(XS) ** 2, _n)
_syy = sum(b * b for b in YS) - Rational(sum(YS) ** 2, _n)
assert _sxy == Rational(1579, 4) and _sxx == Rational(111, 2)
assert abs(float(_sxy / _sxx) - 7.11261) < 0.0001
assert abs(float(Rational(sum(YS), _n) - (_sxy / _sxx) * Rational(sum(XS), _n))
           - 28.1712) < 0.001
assert abs(float(_sxy / sqrt(_sxx * _syy)) - 0.999259) < 0.00001
QS.append(question(
    "IB-AAHL-P2-T4-Q10", 10, "B", "stats_probability", "bivariate_statistics",
    contextIntro=("An ice-cream stall records the number of hours of"
                  " sunshine $x$ and the number of ice creams sold $y$ on"
                  " eight days."
                  "$$\\begin{array}{c|cccccccc}"
                  " x & 2 & 3 & 5 & 6 & 7 & 8 & 9 & 10 \\\\ \\hline"
                  " y & 42 & 50 & 63 & 72 & 78 & 85 & 91 & 100"
                  " \\end{array}$$"),
    parts=[
        part("a", "Find the Pearson product-moment correlation coefficient"
             " $r$, correct to three significant figures.", 3,
             [M1("enter the paired data on the GDC"),
              A1("$r = 0.99925\\ldots$"),
              A1("$r = 0.999$")],
             answer="$r = 0.999$ (3 s.f.)",
             solution=("Entering the eight pairs into the two-variable"
                       " statistics mode of the GDC gives"
                       "$$r = 0.999259\\ldots \\approx 0.999.$$"
                       " Equivalently"
                       " $r = \\dfrac{S_{xy}}{\\sqrt{S_{xx}S_{yy}}}$ with"
                       " $S_{xy} = 394.75$, $S_{xx} = 55.5$ and"
                       " $S_{yy} = 2811.875$."),
             verify=["Eq(Rational(1579, 4), Rational(157900,400))",
                     "Abs(Rational(1579,4)/sqrt(Rational(111,2)"
                     "*Rational(22495,8)) - Rational(999,1000))"
                     " < Rational(1,1000)"]),
        part("b", "Find the equation of the regression line of $y$ on $x$,"
             " giving the coefficients correct to three significant"
             " figures.", 4,
             [M1("least-squares regression on the GDC"),
              A1("gradient $7.11261\\ldots$"),
              A1("intercept $28.1712\\ldots$"),
              A1("$y = 7.11x + 28.2$")],
             answer="$y = 7.11x + 28.2$",
             solution=("The least-squares line of $y$ on $x$ has gradient"
                       "$$b = \\frac{S_{xy}}{S_{xx}} = \\frac{394.75}"
                       "{55.5} = 7.11261\\ldots$$"
                       " and passes through the mean point"
                       " $\\left(\\bar{x}, \\bar{y}\\right)"
                       " = (6.25,\\ 72.625)$, so"
                       "$$a = 72.625 - 7.11261(6.25) = 28.1712\\ldots$$"
                       " The regression line is therefore"
                       "$$y = 7.11x + 28.2.$$"),
             verify=["Abs(Rational(1579,4)/Rational(111,2)"
                     " - Rational(711,100)) < Rational(1,100)",
                     "Abs(Rational(581,8) - (Rational(1579,4)"
                     "/Rational(111,2))*Rational(50,8)"
                     " - Rational(282,10)) < Rational(1,10)"]),
        part("c", "Interpret the gradient of the regression line in"
             " context.", 3,
             [M1("the gradient is a rate of change of $y$ per unit of"
                 " $x$"),
              A1("about $7.11$ extra ice creams"),
              R1("for each additional hour of sunshine, within the range of"
                 " the data")],
             answer="each extra hour of sunshine is associated with about"
                    " $7.11$ more ice creams sold",
             solution=("The gradient measures how much the predicted"
                       " $y$ changes per one-unit increase in $x$. Here"
                       " each additional hour of sunshine is associated"
                       " with about $7.11$ more ice creams sold."
                       " The wording matters: the data are observational,"
                       " so this is an ASSOCIATION, not proof that"
                       " sunshine causes the sales — and the statement is"
                       " only supported over the observed range of $2$ to"
                       " $10$ hours."),
             verify=["Abs(Rational(1579,4)/Rational(111,2)"
                     " - Rational(711,100)) < Rational(1,100)",
                     "Eq(10 - 2, 8)"]),
        part("d", "Use your regression line to predict the number of ice"
             " creams sold on a day with $4$ hours of sunshine.", 4,
             [M1("substitute $x = 4$"),
              A1("$7.11261(4) + 28.1712$"),
              A1("$56.62\\ldots$"),
              A1("about $57$ ice creams")],
             answer="about $57$ ice creams",
             solution=("Substitute $x = 4$ into the regression line:"
                       "$$y = 7.11261(4) + 28.1712 = 28.4504 + 28.1712"
                       " = 56.6216\\ldots$$"
                       " Ice creams come in whole numbers, so the"
                       " prediction is about $57$. This is an"
                       " INTERPOLATION — $x = 4$ sits inside the observed"
                       " range $2 \\le x \\le 10$ — so the prediction is"
                       " reasonable."),
             verify=["Abs((Rational(1579,4)/Rational(111,2))*4"
                     " + Rational(2817,100) - Rational(566,10))"
                     " < Rational(1,5)",
                     "2 < 4", "4 < 10"]),
        part("e", "A colleague uses the same line to predict sales on a day"
             " with $15$ hours of sunshine. Comment on the reliability of"
             " that prediction.", 4,
             [M1("compare $x = 15$ with the range of the data"),
              A1("$15$ lies outside $2 \\le x \\le 10$"),
              R1("this is extrapolation, so the linear pattern is not"
                 " known to continue"),
              R1("the prediction is unreliable — sales are also limited by"
                 " stock and opening hours")],
             answer="unreliable: $x = 15$ is extrapolation beyond the"
                    " data",
             solution=("The data cover only $2 \\le x \\le 10$ hours of"
                       " sunshine, so $x = 15$ lies well outside the"
                       " observed range. Using the model there is"
                       " EXTRAPOLATION: the strong linear fit"
                       " ($r = 0.999$) is evidence about the pattern"
                       " between $2$ and $10$ hours only, and nothing in"
                       " the data says the straight line continues."
                       " In context there are good reasons to doubt it"
                       " would — sales are capped by stock, staffing and"
                       " opening hours, so growth must flatten eventually."
                       " The prediction of about $135$ ice creams should"
                       " therefore be treated as unreliable."),
             verify=["15 > 10",
                     "Abs((Rational(1579,4)/Rational(111,2))*15"
                     " + Rational(2817,100) - 135) < 1"]),
    ]))

META = {"course": "aa", "level": "hl", "paper": 2, "testId": "ib-hl-practice-4",
        "label": "AA HL Practice Paper 2", "timeMinutes": 120,
        "totalMarks": 110, "calculator": True}

if __name__ == "__main__":
    QS[7]["figure"] = png("ib-aahl-p2-t4-q8.png",
                          "Graph of velocity v = 4 sin t minus t against "
                          "time t from 0 to 4 seconds, rising to a peak "
                          "then crossing the axis near t = 2.5")
    QS[8]["figure"] = png("ib-aahl-p2-t4-q9.png",
                          "Triangle ABC with AB = 9, AC = 12, angle A = 70 "
                          "degrees, and the bisector AD drawn to the point "
                          "D on BC")
    write_paper(META, QS, "data/ib/aa-hl/ib-hl-practice-4/paper2.json")
