#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 4 (data/sat/sat-practice-4.json).

Built on scripts/test-builders/satbuild.py — this file is ONLY stems,
parameters, computed answers, named distractor error models, verify[]
strings, and solutions. Archetypes are fresh versus tests 1-3, and the
hard tier is calibrated to real Bluebook hard questions: radical
equations with an extraneous root, no-solution / infinitely-many-solution
parameter systems, circle equations via completing the square, the
sine-cosine cofunction identity, combined percent change (reverse),
extending a quadratic model beyond its table, absolute-value equations
and inequalities, and d = rt closing-speed work.

Solution style rule (post letter-audit): mcq_numeric distractor mentions
describe the ERROR AND ITS VALUE, never a choice letter — satbuild
derives and rewrites the closing letter line itself.

Blueprint (asserted at the end):
  module1     alg 7 / adv 7 / psda 4 / geo 4 · 8E/9M/5H · SPR {4,9,14,18,21}
  module2*    alg 8 / adv 8 / psda 3 / geo 3 · SPR {3,7,12,15,19,22}
  module2Easy 11E/9M/2H · module2Hard 2E/7M/13H · threshold 15
"""

import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from satbuild import (REPO, check_module, figure, mcq_listed, mcq_numeric,
                      spr, write_test)

from sympy import Eq, Rational, expand, sqrt, symbols
from sympy import solve as _solve

x = symbols("x")


def frac(fr) -> str:
    fr = Fraction(fr)
    return rf"$\dfrac{{{fr.numerator}}}{{{fr.denominator}}}$"


def dec(v) -> str:
    return f"${float(Fraction(v)):g}$"


def smart(v) -> str:
    return dec(v) if Fraction(v).denominator == 1 else frac(v)


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E alg one_var — 4x + 7 = 31, x = 6
    assert _solve(Eq(4 * x + 7, 31), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $4x + 7 = 31$, what is the value of $x$?",
        r"Subtract 7 from both sides, then divide by 4:"
        r" $$4x = 24 \;\Rightarrow\; x = 6.$$"
        r" Adding 7 instead of subtracting gives $\frac{38}{4} = 9.5$, and"
        r" stopping at $4x = 24$ leaves 24."
        r" The correct answer is **A**.",
        ["Eq(4*6 + 7, 31)", "Eq((31 - 7)/4, 6)"],
        6, {7: "off by one", Rational(19, 2): "added 7", 24: "forgot divide"}))

    # Q2 E psda one_var_data — mean of five values, FIGURE (value table)
    laps = [12, 15, 9, 18, 16]
    mean = Fraction(sum(laps), 5)
    assert mean == 14
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q02", M, 2, "psda", "one_var_data", "easy",
        r"The table shows the number of laps Amara swam on each of five"
        r" days. What is the mean number of laps per day?",
        r"Add the five values and divide by 5:"
        r" $$\frac{12 + 15 + 9 + 18 + 16}{5} = \frac{70}{5} = 14.$$"
        r" The middle value when ordered (the median) is 15 — a different"
        r" statistic; dividing the total by 4 gives 17.5."
        r" The correct answer is **A**.",
        ["Eq(Rational(12 + 15 + 9 + 18 + 16, 5), 14)"],
        14, {15: "the median", Rational(35, 2): "divided by 4", 70: "the sum"},
        fig=figure("sat-p4-m1-q02",
                   "Table with days Mon through Fri and laps 12, 15, 9, 18, "
                   "16.")))

    # Q3 E alg linear model interpretation (listed)
    assert 25 + Fraction(1, 10) * 0 == 25
    qs.append(mcq_listed(
        "SAT-P4-M1-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The total monthly cost, in dollars, of a phone plan is"
        r" $C(m) = 25 + 0.10m$, where $m$ is the number of minutes of"
        r" calls made that month. What is the best interpretation of the"
        r" number 25 in this context?",
        {"A": r"The cost of each minute of calls, in cents.",
         "B": r"The number of free minutes included each month.",
         "C": r"The total monthly cost, in dollars, for 10 minutes of calls.",
         "D": r"The monthly cost, in dollars, if no calls are made."},
        "D",
        r"At $m = 0$ minutes, $C(0) = 25$ — the fixed monthly charge"
        r" before any calls. The per-minute cost is the coefficient"
        r" $0.10$ dollars (10 cents), not 25, and $C(10) = 26$, not 25."
        r" The correct answer is **D**.",
        ["Eq(25 + Rational(1, 10)*0, 25)", "Eq(25 + Rational(1, 10)*10, 26)"]))

    # Q4 E adv SPR — f(7) for f(x) = x^2 - 5x
    assert 7**2 - 5 * 7 == 14
    qs.append(spr(
        "SAT-P4-M1-Q04", M, 4, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = x^2 - 5x$. What is the"
        r" value of $f(7)$?",
        ["14"],
        r"Substitute $x = 7$:"
        r" $$f(7) = 7^2 - 5(7) = 49 - 35 = 14.$$"
        r" The correct answer is **14**.",
        ["Eq(7**2 - 5*7, 14)"]))

    # Q5 E geo complementary angles — x = 25
    assert 25 + (2 * 25 + 15) == 90
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q05", M, 5, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"Two angles are complementary. One measures $x°$ and the other"
        r" measures $(2x + 15)°$. What is the value of $x$?",
        r"Complementary angles sum to $90°$:"
        r" $$x + 2x + 15 = 90 \;\Rightarrow\; 3x = 75 \;\Rightarrow\;"
        r" x = 25.$$"
        r" Treating the pair as supplementary ($3x + 15 = 180$) gives 55;"
        r" solving $x + 15 = 90$ ignores the $2x$ and gives 75."
        r" The correct answer is **B**.",
        ["Eq(25 + 2*25 + 15, 90)", "Eq((90 - 15)/3, 25)"],
        25, {15: "solved 3x + 15 = 60", 55: "used 180", 75: "ignored 2x"}))

    # Q6 E alg parallel line (listed)
    qs.append(mcq_listed(
        "SAT-P4-M1-Q06", M, 6, "algebra", "linear_equations_two_var", "easy",
        r"Line $\ell$ has equation $y = 3x - 4$. Line $k$ is parallel to"
        r" line $\ell$ and passes through the point $(0, 5)$. Which"
        r" equation defines line $k$?",
        {"A": r"$y = -3x + 5$",
         "B": r"$y = -\tfrac{1}{3}x + 5$",
         "C": r"$y = 3x + 5$",
         "D": r"$y = 5x + 3$"},
        "C",
        r"Parallel lines have EQUAL slopes, so line $k$ keeps the slope 3,"
        r" and passing through $(0, 5)$ makes 5 the $y$-intercept:"
        r" $$y = 3x + 5.$$"
        r" A slope of $-\tfrac{1}{3}$ would be a PERPENDICULAR line, not a"
        r" parallel one."
        r" The correct answer is **C**.",
        ["Eq(3*0 + 5, 5)", "Eq(3*Rational(-1, 3), -1)"]))

    # Q7 E adv exponent product (listed)
    assert expand((2 * x**3) * (4 * x**5)) == 8 * x**8
    qs.append(mcq_listed(
        "SAT-P4-M1-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $(2x^3)(4x^5)$?",
        {"A": r"$6x^8$",
         "B": r"$6x^{15}$",
         "C": r"$8x^8$",
         "D": r"$8x^{15}$"},
        "C",
        r"Multiply the coefficients and ADD the exponents:"
        r" $$(2x^3)(4x^5) = (2 \cdot 4)\,x^{3+5} = 8x^8.$$"
        r" Adding the coefficients gives 6; multiplying the exponents"
        r" gives $x^{15}$ — both are the classic slips."
        r" The correct answer is **C**.",
        ["Eq(2*4, 8)", "Eq(3 + 5, 8)",
         "Eq(expand((2*x**3)*(4*x**5)), 8*x**8)"]))

    # Q8 E geo triangle angle sum — x = 80
    assert 35 + 65 + 80 == 180
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q08", M, 8, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"The measures of two angles of a triangle are $35°$ and $65°$."
        r" What is the measure, in degrees, of the third angle?",
        r"The angles of a triangle sum to $180°$:"
        r" $$x = 180 - 35 - 65 = 80.$$"
        r" Averaging the two given angles gives 50, and $180 - 80 = 100$ is"
        r" the supplement of the answer, not the angle itself."
        r" The correct answer is **B**.",
        ["Eq(180 - 35 - 65, 80)"],
        80, {50: "averaged the given pair", 65: "copied an angle",
             100: "the supplement"}))

    # Q9 M alg SPR — elimination system, y = 2
    yv = symbols("y")
    sol = _solve([Eq(3 * x + yv, 17), Eq(x - yv, 3)], [x, yv])
    assert sol[x] == 5 and sol[yv] == 2
    qs.append(spr(
        "SAT-P4-M1-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$3x + y = 17$$ $$x - y = 3$$"
        r" If $(x, y)$ is the solution to the system above, what is the"
        r" value of $y$?",
        ["2"],
        r"Add the equations to eliminate $y$:"
        r" $$4x = 20 \;\Rightarrow\; x = 5,$$"
        r" then $5 - y = 3$ gives $y = 2$. Check: $3(5) + 2 = 17$. ✓"
        r" The correct answer is **2**.",
        ["Eq(3*5 + 2, 17)", "Eq(5 - 2, 3)"]))

    # Q10 M psda conditional from two-way table, FIGURE
    walk_g11, g11_total = 10, 40
    p = Fraction(walk_g11, g11_total)
    assert p == Fraction(1, 4)
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q10", M, 10, "psda", "probability_conditional", "medium",
        r"The two-way table summarizes how 80 students travel to school."
        r" If one of the GRADE 11 students is selected at random, what is"
        r" the probability that the student walks to school?",
        r"The condition restricts the sample space to the 40 grade-11"
        r" students, of whom 10 walk:"
        r" $$P(\text{walk} \mid \text{grade 11}) = \frac{10}{40}"
        r" = \frac{1}{4}.$$"
        r" Dividing 10 by all 80 students ($\frac{1}{8}$) ignores the"
        r" condition; $\frac{13}{40}$ mixes in grade-10 walkers."
        r" The correct answer is **B**.",
        ["Eq(Rational(10, 40), Rational(1, 4))", "Eq(30 + 10, 40)",
         "Eq(24 + 16 + 30 + 10, 80)"],
        p, {Fraction(1, 8): "of all students", Fraction(13, 40): "mixed rows",
            Fraction(5, 13): "walkers overall ratio"},
        fmt=lambda v: frac(v),
        fig=figure("sat-p4-m1-q10",
                   "Two-way table of 80 students by grade (10, 11) and "
                   "travel mode (Bus, Walk): grade 10 has 24 bus and 16 "
                   "walk; grade 11 has 30 bus and 10 walk.")))

    # Q11 M alg linear model solve — 16 minutes to empty
    assert Fraction(240, 15) == 16
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q11", M, 11, "algebra", "linear_functions", "medium",
        r"The function $W(t) = 240 - 15t$ gives the number of liters of"
        r" water remaining in a tank $t$ minutes after it starts"
        r" draining. According to the model, after how many minutes will"
        r" the tank be empty?",
        r"The tank is empty when $W(t) = 0$:"
        r" $$240 - 15t = 0 \;\Rightarrow\; t = \frac{240}{15} = 16.$$"
        r" 15 is the drain RATE (liters per minute), and dividing 240 by 20"
        r" gives 12 — neither answers the question."
        r" The correct answer is **B**.",
        ["Eq(Rational(240, 15), 16)", "Eq(240 - 15*16, 0)"],
        16, {8: "halved", 12: "divided by 20", 15: "the rate"}))

    # Q12 M adv exponential decay read — V(2) = 4500, FIGURE
    assert 8000 * Fraction(3, 4)**2 == 4500
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q12", M, 12, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph shows the value $y$, in dollars, of a machine $x$"
        r" years after purchase; the value is multiplied by $0.75$ each"
        r" year from an initial \$8,000. What is the value of the"
        r" machine after 2 years?",
        r"Two years is two multiplications by 0.75:"
        r" $$8000 (0.75)^2 = 8000 \cdot 0.5625 = 4500.$$"
        r" Stopping after one year gives 6000; halving twice"
        r" ($8000 \cdot 0.25$) gives 2000 — the model multiplies by 0.75,"
        r" not 0.5."
        r" The correct answer is **C**.",
        ["Eq(8000*Rational(3, 4)**2, 4500)",
         "Eq(8000*Rational(3, 4), 6000)"],
        4500, {2000: "quartered", 4000: "halved", 6000: "one year"},
        fig=figure("sat-p4-m1-q12",
                   "Decreasing exponential curve through (0, 8000), "
                   "(1, 6000), and (2, 4500), flattening toward the "
                   "x-axis.")))

    # Q13 M adv transformation of a graphed point (listed)
    qs.append(mcq_listed(
        "SAT-P4-M1-Q13", M, 13, "advanced_math", "nonlinear_functions",
        "medium",
        r"The point $(3, 7)$ lies on the graph of $y = f(x)$ in the"
        r" $xy$-plane. The function $g$ is defined by $g(x) = f(x - 2)$."
        r" Which point must lie on the graph of $y = g(x)$?",
        {"A": r"$(1, 7)$",
         "B": r"$(3, 5)$",
         "C": r"$(5, 7)$",
         "D": r"$(3, 9)$"},
        "C",
        r"$g(5) = f(5 - 2) = f(3) = 7$, so $(5, 7)$ is on the graph of"
        r" $g$: replacing $x$ with $x - 2$ shifts the graph 2 units to"
        r" the RIGHT, opposite to the sign inside. Shifting left instead"
        r" gives $(1, 7)$; the $\pm 2$ never touches the $y$-value."
        r" The correct answer is **C**.",
        ["Eq(5 - 2, 3)"]))

    # Q14 M adv SPR — radical with extraneous root, x = 9
    roots = _solve(Eq(x**2 - 11 * x + 18, 0), x)
    assert set(roots) == {2, 9}
    assert sqrt(9 + 7) == 9 - 5          # 4 = 4 ✓
    assert sqrt(2 + 7) != 2 - 5          # 3 ≠ -3: extraneous
    qs.append(spr(
        "SAT-P4-M1-Q14", M, 14, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"$$\sqrt{x + 7} = x - 5$$"
        r" What is the solution to the equation above?",
        ["9"],
        r"Square both sides and solve the quadratic:"
        r" $$x + 7 = (x - 5)^2 \;\Rightarrow\; x^2 - 11x + 18 = 0"
        r" \;\Rightarrow\; (x - 2)(x - 9) = 0.$$"
        r" Check BOTH candidates in the original equation: $x = 9$ gives"
        r" $\sqrt{16} = 4$ ✓, but $x = 2$ gives $\sqrt{9} = 3 \ne -3$ —"
        r" extraneous. Only $x = 9$ survives."
        r" The correct answer is **9**.",
        ["Eq(expand((x - 2)*(x - 9)), x**2 - 11*x + 18)",
         "Eq(sqrt(9 + 7), 9 - 5)", "Ne(sqrt(2 + 7), 2 - 5)"]))

    # Q15 M alg inequality word — max whole 8
    assert 45 + 12 * 8 <= 150 < 45 + 12 * 9
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"A repair shop charges a \$45 diagnostic fee plus \$12 for each"
        r" half hour of labor. Mele can spend at most \$150. What is the"
        r" greatest number of half hours of labor she can afford?",
        r"With $h$ half hours, $45 + 12h \le 150$, so"
        r" $$12h \le 105 \;\Rightarrow\; h \le 8.75.$$"
        r" The greatest WHOLE number of half hours is 8. Rounding 8.75 up"
        r" to 9 breaks the budget ($45 + 108 = 153 > 150$)."
        r" The correct answer is **B**.",
        ["Eq(Rational(150 - 45, 12), Rational(35, 4))",
         "45 + 12*8 <= 150", "45 + 12*9 > 150"],
        8, {7: "over-cautious", Rational(35, 4): "the boundary",
            9: "rounded up"},
        fmt=lambda v: dec(v)))

    # Q16 M geo similar triangles — corresponding side 15
    scale = Fraction(10, 6)
    assert scale * 9 == 15
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q16", M, 16, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"Triangle $PQR$ is similar to triangle $XYZ$, with $P$, $Q$, and"
        r" $R$ corresponding to $X$, $Y$, and $Z$. In triangle $PQR$,"
        r" $PQ = 6$ and $QR = 9$. If $XY = 10$, what is the length of"
        r" $YZ$?",
        r"Corresponding sides of similar triangles are proportional:"
        r" $$\frac{YZ}{QR} = \frac{XY}{PQ} = \frac{10}{6}"
        r" \;\Rightarrow\; YZ = 9 \cdot \frac{10}{6} = 15.$$"
        r" Adding the same amount to each side ($9 + 4 = 13$) is the"
        r" classic similarity error — sides scale by a FACTOR, not a"
        r" difference; $\frac{9 \cdot 9}{6} = 13.5$ pairs the wrong"
        r" sides."
        r" The correct answer is **D**.",
        ["Eq(9*Rational(10, 6), 15)", "Eq(Rational(15, 9), Rational(10, 6))"],
        15, {12: "scaled by 2 then added", 13: "added the difference",
             Rational(27, 2): "paired wrong sides"},
        fmt=lambda v: smart(v)))

    # Q17 M psda box plot percent, FIGURE
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q17", M, 17, "psda", "one_var_data", "medium",
        r"The box plot summarizes the distribution of 80 delivery times."
        r" Approximately what percent of the delivery times are greater"
        r" than the first quartile (30 minutes)?",
        r"By definition, one quarter of the data lies at or below the"
        r" first quartile, so about"
        r" $$100 - 25 = 75\%$$"
        r" of the times are above it. 25\% is the share BELOW $Q_1$, and"
        r" 50\% is the share above the MEDIAN — a different landmark."
        r" The correct answer is **D**.",
        ["Eq(100 - 25, 75)"],
        75, {25: "below Q1 share", 30: "the Q1 value itself",
             50: "above the median"},
        fig=figure("sat-p4-m1-q17",
                   "Box plot of delivery times over a number line: minimum "
                   "20, first quartile 30, median 40, third quartile 55, "
                   "maximum 70 minutes.")))

    # Q18 H alg SPR — no-solution parameter, a = 6
    # 3x - 5y = 8 and ax - 10y = 21: parallel iff a/3 = -10/-5 = 2 → a = 6
    assert Fraction(-10, -5) * 3 == 6 and Fraction(21, 8) != 2
    qs.append(spr(
        "SAT-P4-M1-Q18", M, 18, "algebra", "systems_two_linear", "hard",
        r"$$3x - 5y = 8$$ $$ax - 10y = 21$$"
        r" In the system of equations above, $a$ is a constant. If the"
        r" system has NO solution, what is the value of $a$?",
        ["6"],
        r"No solution means the lines are parallel: the left-hand sides"
        r" must be proportional while the right-hand sides are not."
        r" Doubling the first equation's coefficients gives"
        r" $6x - 10y$, so"
        r" $$a = 6,$$"
        r" and indeed $2 \times 8 = 16 \ne 21$, so the lines never meet."
        r" The correct answer is **6**.",
        ["Eq(2*3, 6)", "Eq(2*(-5), -10)", "Ne(2*8, 21)"]))

    # Q19 H adv vertex-form parameter — a = 2
    assert 2 * (1 - 3)**2 + 5 == 13
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q19", M, 19, "advanced_math", "nonlinear_functions",
        "hard",
        r"The graph of $y = a(x - 3)^2 + 5$ in the $xy$-plane passes"
        r" through the point $(1, 13)$, where $a$ is a constant. What is"
        r" the value of $a$?",
        r"Substitute the point:"
        r" $$13 = a(1 - 3)^2 + 5 = 4a + 5 \;\Rightarrow\; 4a = 8"
        r" \;\Rightarrow\; a = 2.$$"
        r" Dividing $13 - 5 = 8$ by 2 instead of by $(-2)^2 = 4$ gives 4;"
        r" forgetting to square entirely leaves 8."
        r" The correct answer is **B**.",
        ["Eq(2*(1 - 3)**2 + 5, 13)", "Eq((13 - 5)/4, 2)"],
        2, {-2: "sign error", 4: "divided by 2", 8: "did not square"}))

    # Q20 H geo circle equation (listed)
    assert expand((x - 3)**2 - 9) + 0 == expand(x**2 - 6 * x)
    qs.append(mcq_listed(
        "SAT-P4-M1-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"$$x^2 + y^2 - 6x + 4y - 12 = 0$$"
        r" The graph of the equation above in the $xy$-plane is a circle."
        r" What are the center and the radius of the circle?",
        {"A": r"center $(-3, 2)$, radius $5$",
         "B": r"center $(3, -2)$, radius $5$",
         "C": r"center $(3, -2)$, radius $25$",
         "D": r"center $(6, -4)$, radius $12$"},
        "B",
        r"Complete the square in both variables:"
        r" $$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$$"
        r" $$(x - 3)^2 + (y + 2)^2 = 25.$$"
        r" The center is $(3, -2)$ — signs OPPOSITE to those inside the"
        r" parentheses — and the radius is $\sqrt{25} = 5$, not 25 (that"
        r" is $r^2$)."
        r" The correct answer is **B**.",
        ["Eq(12 + 9 + 4, 25)", "Eq(sqrt(25), 5)",
         "Eq(expand((x - 3)**2), x**2 - 6*x + 9)"]))

    # Q21 H adv SPR — exponential equation, x = 2
    assert 5**(2 * 2 - 1) == 125
    qs.append(spr(
        "SAT-P4-M1-Q21", M, 21, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$5^{\,2x - 1} = 125$$"
        r" What is the solution to the equation above?",
        ["2"],
        r"Write both sides as powers of 5 and equate exponents:"
        r" $$5^{2x - 1} = 5^3 \;\Rightarrow\; 2x - 1 = 3 \;\Rightarrow\;"
        r" x = 2.$$"
        r" The correct answer is **2**.",
        ["Eq(5**3, 125)", "Eq(2*2 - 1, 3)"]))

    # Q22 H psda reverse combined percent — original 50
    net = Fraction(120, 100) * Fraction(75, 100)
    assert net == Fraction(9, 10) and Fraction(45, 1) / net == 50
    qs.append(mcq_numeric(
        "SAT-P4-M1-Q22", M, 22, "psda", "percentages", "hard",
        r"The price of a jacket was increased by 20\%, and the new price"
        r" was later decreased by 25\%. The final price was \$45. What"
        r" was the original price of the jacket, in dollars?",
        r"The two changes multiply: $1.20 \times 0.75 = 0.90$, so the"
        r" final price is 90\% of the original $p$:"
        r" $$0.90\,p = 45 \;\Rightarrow\; p = 50.$$"
        r" Undoing only the increase ($45 \times 1.2$) gives 54; treating"
        r" the cut as a 25\% raise on 45 gives 56.25, and undoing only"
        r" the decrease ($45 \div 0.75$) gives 60."
        r" The correct answer is **B**.",
        ["Eq(Rational(120, 100)*Rational(75, 100), Rational(9, 10))",
         "Eq(Rational(45)/Rational(9, 10), 50)"],
        50, {54: "undid increase only", Rational(225, 4): "treated cut as +25%",
             60: "undid decrease only"}))

    return qs


# ─── Module 2 Easy (11E / 9M / 2H) ────────────────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg one_var — 2(x + 5) = 26, x = 8
    assert _solve(Eq(2 * (x + 5), 26), x) == [8]
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $2(x + 5) = 26$, what is the value of $x$?",
        r"Divide both sides by 2, then subtract 5:"
        r" $$x + 5 = 13 \;\Rightarrow\; x = 8.$$"
        r" Subtracting 5 before dividing correctly gives"
        r" $\frac{26 - 10}{2} = 8$ as well — but subtracting only 5 from"
        r" 26 and then halving gives 10.5, and distributing to"
        r" $2x + 5 = 26$ gives 10.5 too; forgetting to divide leaves 16."
        r" The correct answer is **B**.",
        ["Eq(2*(8 + 5), 26)", "Eq(Rational(26, 2) - 5, 8)"],
        8, {3: "divided then subtracted 10", Rational(21, 2): "2x + 5 = 26",
            16: "26 - 10, no divide"}))

    # Q2 E psda bar chart total, FIGURE
    books = [7, 12, 9, 4]
    assert sum(books) == 32
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q02", M, 2, "psda", "one_var_data", "easy",
        r"The bar chart shows the number of books read by four students."
        r" What is the total number of books the four students read?",
        r"Add the four bars:"
        r" $$7 + 12 + 9 + 4 = 32.$$"
        r" Leaving out the shortest bar (4) gives 28; leaving out the"
        r" first bar gives 25."
        r" The correct answer is **C**.",
        ["Eq(7 + 12 + 9 + 4, 32)"],
        32, {25: "dropped the 7", 28: "dropped the 4", 30: "mis-added"},
        fig=figure("sat-p4-m2e-q02",
                   "Bar chart of books read: Ana 7, Bat 12, Chimeg 9, "
                   "Dorj 4.")))

    # Q3 E geo SPR — rectangle perimeter 26
    assert 2 * (9 + 4) == 26
    qs.append(spr(
        "SAT-P4-M2E-Q03", M, 3, "geometry_trig", "area_volume", "easy",
        r"A rectangle has a length of 9 and a width of 4. What is the"
        r" perimeter of the rectangle?",
        ["26"],
        r"Perimeter is twice the sum of length and width:"
        r" $$P = 2(9 + 4) = 26.$$"
        r" The correct answer is **26**.",
        ["Eq(2*(9 + 4), 26)"]))

    # Q4 E alg slope from graph, FIGURE
    assert Fraction(2 - (-2), 2 - 0) == 2
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q04", M, 4, "algebra", "linear_functions", "easy",
        r"The graph of a line in the $xy$-plane is shown. What is the"
        r" slope of the line?",
        r"The line rises from $(0, -2)$ to $(2, 2)$:"
        r" $$m = \frac{2 - (-2)}{2 - 0} = \frac{4}{2} = 2.$$"
        r" Inverting rise over run gives $\frac{1}{2}$; $-2$ is the"
        r" $y$-intercept, not the slope, and 4 is only the rise."
        r" The correct answer is **C**.",
        ["Eq(Rational(2 - (-2), 2 - 0), 2)"],
        2, {-2: "the intercept", Fraction(1, 2): "inverted", 4: "rise only"},
        fmt=lambda v: smart(v),
        fig=figure("sat-p4-m2e-q04",
                   "Coordinate grid with a single line rising through "
                   "(0, -2) and (2, 2).")))

    # Q5 E adv evaluate — g(4) = 28
    assert 4**2 + 3 * 4 == 28
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q05", M, 5, "advanced_math", "nonlinear_functions",
        "easy",
        r"The function $g$ is defined by $g(x) = x^2 + 3x$. What is the"
        r" value of $g(4)$?",
        r"Substitute $x = 4$:"
        r" $$g(4) = 4^2 + 3(4) = 16 + 12 = 28.$$"
        r" Adding 3 instead of $3x$ gives 19; squaring the sum"
        r" ($(4 + 3)^2$) gives 49."
        r" The correct answer is **C**.",
        ["Eq(4**2 + 3*4, 28)"],
        28, {16: "dropped 3x", 19: "added 3 not 3x", 49: "squared the sum"}))

    # Q6 E alg inequality point test (listed)
    assert 3 > 2 * 1 - 1
    qs.append(mcq_listed(
        "SAT-P4-M2E-Q06", M, 6, "algebra", "linear_inequalities", "easy",
        r"Which of the following points in the $xy$-plane is a solution"
        r" to the inequality $y > 2x - 1$?",
        {"A": r"$(0, -1)$",
         "B": r"$(1, 3)$",
         "C": r"$(2, 1)$",
         "D": r"$(3, 4)$"},
        "B",
        r"Test each point. At $(1, 3)$: $3 > 2(1) - 1 = 1$. ✓"
        r" At $(2, 1)$: $1 > 3$ is false; at $(3, 4)$: $4 > 5$ is false;"
        r" and at $(0, -1)$: $-1 > -1$ is false — the boundary itself is"
        r" NOT included in a strict inequality."
        r" The correct answer is **B**.",
        ["3 > 2*1 - 1", "Eq(2*0 - 1, -1)"]))

    # Q7 E adv SPR — coefficient b = 5
    assert expand((7 * x**2 - 3 * x) + (2 * x**2 + 8 * x)) == 9 * x**2 + 5 * x
    qs.append(spr(
        "SAT-P4-M2E-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "easy",
        r"$$(7x^2 - 3x) + (2x^2 + 8x) = ax^2 + bx$$"
        r" The equation above is true for all $x$, where $a$ and $b$ are"
        r" constants. What is the value of $b$?",
        ["5"],
        r"Add like terms: the $x$-terms give $-3 + 8 = 5$ (and the"
        r" $x^2$-terms give $a = 9$):"
        r" $$9x^2 + 5x.$$"
        r" The correct answer is **5**.",
        ["Eq(-3 + 8, 5)",
         "Eq(expand((7*x**2 - 3*x) + (2*x**2 + 8*x)), 9*x**2 + 5*x)"]))

    # Q8 E psda map scale — 52.5 km
    km = Fraction(15, 2) * 7
    assert km == Fraction(105, 2)
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q08", M, 8, "psda", "ratios_rates_units", "easy",
        r"On a map, 2 centimeters represent 15 kilometers. Two towns are"
        r" 7 centimeters apart on the map. What is the actual distance"
        r" between the towns, in kilometers?",
        r"Each centimeter represents $15 \div 2 = 7.5$ km, so"
        r" $$7 \times 7.5 = 52.5 \text{ km}.$$"
        r" Multiplying $15 \times 2$ gives 30 (two map-steps, not"
        r" seven); $15 \times 4 = 60$ rounds the scale the wrong way."
        r" The correct answer is **C**.",
        ["Eq(Rational(15, 2)*7, Rational(105, 2))"],
        km, {30: "two steps", 49: "squared 7", 60: "rounded scale up"},
        fmt=lambda v: smart(v)))

    # Q9 M alg tickets system — adults 55
    a, c = symbols("a c")
    sol = _solve([Eq(a + c, 150), Eq(5 * a + 3 * c, 560)], [a, c])
    assert sol[a] == 55 and sol[c] == 95
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"A theater sold 150 tickets for a total of \$560. Adult tickets"
        r" cost \$5 each and child tickets cost \$3 each. How many ADULT"
        r" tickets were sold?",
        r"With $a + c = 150$ and $5a + 3c = 560$, substitute"
        r" $c = 150 - a$:"
        r" $$5a + 3(150 - a) = 560 \;\Rightarrow\; 2a + 450 = 560"
        r" \;\Rightarrow\; a = 55.$$"
        r" Check: $5(55) + 3(95) = 275 + 285 = 560$. ✓ The 95 is the"
        r" number of CHILD tickets; 110 is $2a$ before halving."
        r" The correct answer is **A**.",
        ["Eq(55 + 95, 150)", "Eq(5*55 + 3*95, 560)"],
        55, {75: "half of 150", 95: "child tickets", 110: "2a"}))

    # Q10 E adv growth factor from table, FIGURE
    vals = [5, 10, 20, 40]
    assert all(b == 2 * a for a, b in zip(vals, vals[1:]))
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "easy",
        r"The table shows values of an exponential function $h$ at"
        r" $x = 0, 1, 2, 3$. By what factor does $h(x)$ increase each"
        r" time $x$ increases by 1?",
        r"Each output is double the one before:"
        r" $$\frac{10}{5} = \frac{20}{10} = \frac{40}{20} = 2.$$"
        r" 5 is the INITIAL value, not the factor; $\frac{1}{2}$ would"
        r" describe decay."
        r" The correct answer is **B**.",
        ["Eq(Rational(10, 5), 2)", "Eq(Rational(40, 20), 2)"],
        2, {Fraction(1, 2): "decay direction", 5: "initial value",
            10: "second output"},
        fmt=lambda v: smart(v),
        fig=figure("sat-p4-m2e-q10",
                   "Table with x values 0, 1, 2, 3 and h(x) values 5, 10, "
                   "20, 40.")))

    # Q11 M adv zeros from factored form (listed)
    assert expand((x - 2) * (x + 5)) == x**2 + 3 * x - 10
    qs.append(mcq_listed(
        "SAT-P4-M2E-Q11", M, 11, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"$$y = (x - 2)(x + 5)$$"
        r" The graph of the equation above in the $xy$-plane crosses the"
        r" $x$-axis at which two values of $x$?",
        {"A": r"$x = -2$ and $x = 5$",
         "B": r"$x = 2$ and $x = 5$",
         "C": r"$x = -2$ and $x = -5$",
         "D": r"$x = 2$ and $x = -5$"},
        "D",
        r"The graph crosses the $x$-axis where $y = 0$, i.e. where a"
        r" factor is zero: $x - 2 = 0$ gives $x = 2$ and $x + 5 = 0$"
        r" gives $x = -5$ — each zero has the OPPOSITE sign of the"
        r" number in its factor."
        r" The correct answer is **D**.",
        ["Eq((2 - 2)*(2 + 5), 0)", "Eq((-5 - 2)*(-5 + 5), 0)"]))

    # Q12 M psda SPR — fourth test score 100
    assert 4 * 85 - 240 == 100
    qs.append(spr(
        "SAT-P4-M2E-Q12", M, 12, "psda", "one_var_data", "medium",
        r"The mean of Nara's four test scores is 85. The sum of her first"
        r" three scores is 240. What is her fourth test score?",
        ["100"],
        r"A mean of 85 over four tests means the total is"
        r" $4 \times 85 = 340$, so the fourth score is"
        r" $$340 - 240 = 100.$$"
        r" The correct answer is **100**.",
        ["Eq(4*85, 340)", "Eq(340 - 240, 100)"]))

    # Q13 M alg inequality from number line (listed), FIGURE
    qs.append(mcq_listed(
        "SAT-P4-M2E-Q13", M, 13, "algebra", "linear_inequalities", "medium",
        r"The number line shows the solution set of an inequality: a"
        r" filled circle at 3 with shading to the right. Which inequality"
        r" has this solution set?",
        {"A": r"$x \ge 3$",
         "B": r"$x > 3$",
         "C": r"$x < 3$",
         "D": r"$x \le 3$"},
        "A",
        r"The ray points right (numbers GREATER than 3) and the FILLED"
        r" circle includes 3 itself: $x \ge 3$. An open circle would make"
        r" it strict; shading left would flip the direction."
        r" The correct answer is **A**.",
        ["4 >= 3", "Eq(3, 3)"],
        fig=figure("sat-p4-m2e-q13",
                   "Number line from -2 to 8 with a filled circle at 3 and "
                   "an arrow shading all numbers to the right.")))

    # Q14 M adv completed-square minimum — -18
    assert expand((x - 5)**2 - 18) == x**2 - 10 * x + 7
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "medium",
        r"What is the minimum value of the function"
        r" $f(x) = x^2 - 10x + 7$?",
        r"Complete the square: half of $-10$ is $-5$ and $(-5)^2 = 25$:"
        r" $$f(x) = (x - 5)^2 - 25 + 7 = (x - 5)^2 - 18.$$"
        r" The square is never negative, so the minimum VALUE is $-18$"
        r" (at $x = 5$). $-25$ forgets to add back the 7, and 5 is the"
        r" INPUT where the minimum occurs, not the minimum."
        r" The correct answer is **B**.",
        ["Eq(expand((x - 5)**2 - 18), x**2 - 10*x + 7)",
         "Eq(-25 + 7, -18)"],
        -18, {-25: "forgot the +7", 5: "x of the minimum", 7: "f(0)"}))

    # Q15 M geo SPR — Pythagorean hypotenuse 15
    assert 9**2 + 12**2 == 15**2
    qs.append(spr(
        "SAT-P4-M2E-Q15", M, 15, "geometry_trig", "right_triangles_trig",
        "medium",
        r"The legs of a right triangle have lengths 9 and 12. What is the"
        r" length of the hypotenuse?",
        ["15"],
        r"Apply the Pythagorean theorem:"
        r" $$c = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15.$$"
        r" (This is the 3-4-5 triple scaled by 3.)"
        r" The correct answer is **15**.",
        ["Eq(9**2 + 12**2, 225)", "Eq(sqrt(225), 15)"]))

    # Q16 E alg proportionality constant — k = 3.5
    assert Fraction(21, 6) == Fraction(7, 2)
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q16", M, 16, "algebra", "linear_functions", "easy",
        r"The quantity $y$ is directly proportional to $x$. When $x = 6$,"
        r" $y = 21$. What is the constant of proportionality?",
        r"Direct proportion means $y = kx$:"
        r" $$k = \frac{21}{6} = 3.5.$$"
        r" Inverting the ratio gives $\frac{6}{21} = \frac{2}{7}$;"
        r" subtracting gives $21 - 6 = 15$ — proportion is a RATIO, not a"
        r" difference."
        r" The correct answer is **B**.",
        ["Eq(Rational(21, 6), Rational(7, 2))"],
        Fraction(7, 2), {Fraction(2, 7): "inverted", 3: "21 divided by 7", 15: "subtracted"},
        fmt=lambda v: smart(v)))

    # Q17 M geo cylinder volume (listed), FIGURE
    assert 3**2 * 5 == 45
    qs.append(mcq_listed(
        "SAT-P4-M2E-Q17", M, 17, "geometry_trig", "area_volume", "medium",
        r"The right circular cylinder shown has a base radius of 3 and a"
        r" height of 5. What is the volume of the cylinder?",
        {"A": r"$15\pi$",
         "B": r"$30\pi$",
         "C": r"$45\pi$",
         "D": r"$180\pi$"},
        "C",
        r"Volume is base area times height:"
        r" $$V = \pi r^2 h = \pi(3^2)(5) = 45\pi.$$"
        r" $15\pi$ forgets to square the radius; $30\pi$ is the lateral"
        r" area $2\pi rh$; $180\pi$ squares the diameter."
        r" The correct answer is **C**.",
        ["Eq(pi*3**2*5, 45*pi)", "Eq(2*pi*3*5, 30*pi)",
         "Eq(pi*6**2*5, 180*pi)"],
        fig=figure("sat-p4-m2e-q17",
                   "Right circular cylinder with base radius labeled 3 and "
                   "height labeled 5.")))

    # Q18 M adv growth percent — 6%
    assert Fraction(106, 100) - 1 == Fraction(6, 100)
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q18", M, 18, "advanced_math", "nonlinear_functions",
        "medium",
        r"An account balance is modeled by $A(t) = 300(1.06)^t$ dollars,"
        r" where $t$ is the number of years after the account is opened."
        r" By what percent does the balance increase each year?",
        r"Each year the balance is multiplied by $1.06 = 1 + 0.06$, an"
        r" increase of"
        r" $$0.06 = 6\%.$$"
        r" Reading the whole factor as the increase gives 106\%;"
        r" misplacing the decimal gives 0.6\%."
        r" The correct answer is **B**.",
        ["Eq(Rational(106, 100) - 1, Rational(6, 100))"],
        6, {Fraction(3, 5): "decimal slip", 60: "decimal slip x10",
            106: "read the factor"},
        fmt=lambda v: f"${float(Fraction(v)):g}\\%$"))

    # Q19 E alg SPR — x-intercept 5
    assert 2 * 5 - 10 == 0
    qs.append(spr(
        "SAT-P4-M2E-Q19", M, 19, "algebra", "linear_equations_two_var",
        "easy",
        r"The graph of $y = 2x - 10$ in the $xy$-plane crosses the"
        r" $x$-axis at the point $(a, 0)$. What is the value of $a$?",
        ["5"],
        r"On the $x$-axis, $y = 0$:"
        r" $$0 = 2a - 10 \;\Rightarrow\; a = 5.$$"
        r" The correct answer is **5**.",
        ["Eq(2*5 - 10, 0)"]))

    # Q20 M adv composition — f(g(2)) = 11
    g2 = 2 * 2**2
    fg2 = g2 + 3
    assert (g2, fg2) == (8, 11)
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q20", M, 20, "advanced_math", "nonlinear_functions",
        "medium",
        r"The functions $f$ and $g$ are defined by $f(x) = x + 3$ and"
        r" $g(x) = 2x^2$. What is the value of $f(g(2))$?",
        r"Inside first: $g(2) = 2(4) = 8$, then"
        r" $$f(8) = 8 + 3 = 11.$$"
        r" Stopping at $g(2)$ leaves 8; composing in the reverse order"
        r" gives $g(f(2)) = g(5) = 50$."
        r" The correct answer is **B**.",
        ["Eq(2*2**2, 8)", "Eq(8 + 3, 11)", "Eq(2*(2 + 3)**2, 50)"],
        11, {8: "stopped at g(2)", 13: "2^2 + 3^2", 50: "reversed order"}))

    # Q21 H alg break-even minutes — 300
    assert 20 + Fraction(5, 100) * 300 == 35
    qs.append(mcq_numeric(
        "SAT-P4-M2E-Q21", M, 21, "algebra", "linear_equations_one_var",
        "hard",
        r"Phone plan A costs \$20 per month plus \$0.05 per minute of"
        r" calls. Plan B costs a flat \$35 per month. For how many"
        r" minutes of calls in a month do the two plans cost the same?",
        r"Set the costs equal:"
        r" $$20 + 0.05m = 35 \;\Rightarrow\; 0.05m = 15 \;\Rightarrow\;"
        r" m = 300.$$"
        r" Dividing the full \$35 by 0.05 gives 700 (ignores the \$20"
        r" base); $15 \div 5 = 3$ misplaces the decimal."
        r" The correct answer is **C**.",
        ["Eq(20 + Rational(5, 100)*300, 35)",
         "Eq(Rational(35 - 20, 1)/Rational(5, 100), 300)"],
        300, {3: "decimal slip", 55: "added the prices", 700: "ignored base fee"}))

    # Q22 H adv SPR — factor theorem k = 5
    assert 1**3 + 5 * 1 - 6 == 0
    qs.append(spr(
        "SAT-P4-M2E-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$p(x) = x^3 + kx - 6$$"
        r" In the polynomial above, $k$ is a constant. If $x - 1$ is a"
        r" factor of $p(x)$, what is the value of $k$?",
        ["5"],
        r"By the factor theorem, $x - 1$ is a factor exactly when"
        r" $p(1) = 0$:"
        r" $$1 + k - 6 = 0 \;\Rightarrow\; k = 5.$$"
        r" The correct answer is **5**.",
        ["Eq(1**3 + 5*1 - 6, 0)"]))

    return qs


# ─── Module 2 Hard (2E / 7M / 13H) ────────────────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg one_var — 5x - 3 = 2x + 18, x = 7
    assert _solve(Eq(5 * x - 3, 2 * x + 18), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $5x - 3 = 2x + 18$, what is the value of $x$?",
        r"Collect the $x$-terms and the constants:"
        r" $$3x = 21 \;\Rightarrow\; x = 7.$$"
        r" Computing $(18 - 3)/3$ gives 5, and dividing only the 18 by 3"
        r" gives 6 — both skip a step."
        r" The correct answer is **B**.",
        ["Eq(5*7 - 3, 2*7 + 18)"],
        7, {5: "(18-3)/3", 6: "18/3", 21: "forgot divide"}))

    # Q2 E geo angles on a line, FIGURE — x = 44
    assert 3 * 44 + 48 == 180
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q02", M, 2, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure, two angles measuring $(3x)°$ and $48°$ together"
        r" form a straight line. What is the value of $x$?",
        r"Angles on a straight line sum to $180°$:"
        r" $$3x + 48 = 180 \;\Rightarrow\; 3x = 132 \;\Rightarrow\;"
        r" x = 44.$$"
        r" Using $90°$ for the line gives 14; dividing 48 by 3 gives 16;"
        r" stopping at $3x = 132$ leaves 132."
        r" The correct answer is **C**.",
        ["Eq((180 - 48)/3, 44)"],
        44, {14: "used 90", 16: "48/3", 132: "forgot /3"},
        fig=figure("sat-p4-m2h-q02",
                   "A straight line with a ray from a point on it forming "
                   "two angles labeled (3x) degrees and 48 degrees.")))

    # Q3 M alg SPR — 3(2x - 1) = 4x + 9, x = 6
    assert _solve(Eq(3 * (2 * x - 1), 4 * x + 9), x) == [6]
    qs.append(spr(
        "SAT-P4-M2H-Q03", M, 3, "algebra", "linear_equations_one_var",
        "medium",
        r"$$3(2x - 1) = 4x + 9$$"
        r" What is the solution to the equation above?",
        ["6"],
        r"Distribute, then collect terms:"
        r" $$6x - 3 = 4x + 9 \;\Rightarrow\; 2x = 12 \;\Rightarrow\;"
        r" x = 6.$$"
        r" Check: $3(11) = 33$ and $24 + 9 = 33$. ✓"
        r" The correct answer is **6**.",
        ["Eq(3*(2*6 - 1), 4*6 + 9)"]))

    # Q4 M psda histogram median interval (listed), FIGURE
    counts = {0: 3, 10: 5, 20: 7, 30: 4, 40: 1}
    assert sum(counts.values()) == 20 and 3 + 5 < 10.5 <= 3 + 5 + 7
    qs.append(mcq_listed(
        "SAT-P4-M2H-Q04", M, 4, "psda", "one_var_data", "medium",
        r"The histogram shows the wait times of 20 customers, in"
        r" ten-minute intervals. In which interval does the MEDIAN wait"
        r" time lie?",
        {"A": r"10 to 20 minutes",
         "B": r"20 to 30 minutes",
         "C": r"30 to 40 minutes",
         "D": r"40 to 50 minutes"},
        "B",
        r"With 20 values, the median is the average of the 10th and 11th"
        r" ordered values. The first two bars hold $3 + 5 = 8$ values,"
        r" and the third bar (20 to 30) carries values 9 through 15 — so"
        r" both the 10th and 11th values lie in the 20-to-30 interval."
        r" The correct answer is **B**.",
        ["Eq(3 + 5, 8)", "Eq(3 + 5 + 7, 15)", "8 < 10", "11 <= 15"],
        fig=figure("sat-p4-m2h-q04",
                   "Histogram of wait times: 3 customers in 0 to 10 "
                   "minutes, 5 in 10 to 20, 7 in 20 to 30, 4 in 30 to 40, "
                   "and 1 in 40 to 50.")))

    # Q5 M adv absolute value equation — sum of solutions 5
    r1, r2 = _solve(Eq(abs(2 * x - 5), 11), x) if False else (8, -3)
    assert abs(2 * 8 - 5) == 11 and abs(2 * (-3) - 5) == 11 and 8 + (-3) == 5
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q05", M, 5, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"What is the sum of the solutions to the equation"
        r" $|2x - 5| = 11$?",
        r"Split into the two cases:"
        r" $$2x - 5 = 11 \Rightarrow x = 8, \qquad 2x - 5 = -11"
        r" \Rightarrow x = -3.$$"
        r" The sum is $8 + (-3) = 5$. Reporting a single root gives 8 or"
        r" $-3$; 11 is just the right-hand side."
        r" The correct answer is **B**.",
        ["Eq(Abs(2*8 - 5), 11)", "Eq(Abs(2*(-3) - 5), 11)", "Eq(8 - 3, 5)"],
        5, {-3: "negative root only", 8: "positive root only",
            11: "the right side"}))

    # Q6 M alg perpendicular through point — y-intercept 5
    assert 1 == -2 * 2 + 5
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q06", M, 6, "algebra", "linear_functions", "medium",
        r"Line $k$ is perpendicular to the line $y = \tfrac{1}{2}x + 3$"
        r" and passes through the point $(2, 1)$. What is the"
        r" $y$-coordinate of the point where line $k$ crosses the"
        r" $y$-axis?",
        r"The perpendicular slope is the negative reciprocal of"
        r" $\tfrac{1}{2}$, which is $-2$. Through $(2, 1)$:"
        r" $$y - 1 = -2(x - 2) \;\Rightarrow\; y = -2x + 5,$$"
        r" so the $y$-intercept is 5. Keeping the slope $\tfrac{1}{2}$"
        r" gives $1 - 1 = 0$; using slope $-\tfrac{1}{2}$ gives 2, and"
        r" slope $+2$ gives $-3$."
        r" The correct answer is **D**.",
        ["Eq(Rational(1, 2)*(-2), -1)", "Eq(-2*2 + 5, 1)"],
        5, {-3: "slope +2", 0: "kept slope 1/2", 2: "slope -1/2"}))

    # Q7 M adv SPR — rational equation, x = 5
    assert Fraction(5 + 4, 5 - 2) == 3
    qs.append(spr(
        "SAT-P4-M2H-Q07", M, 7, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"$$\frac{x + 4}{x - 2} = 3$$"
        r" What is the solution to the equation above?",
        ["5"],
        r"Multiply both sides by $x - 2$:"
        r" $$x + 4 = 3x - 6 \;\Rightarrow\; 10 = 2x \;\Rightarrow\;"
        r" x = 5.$$"
        r" Check: $\frac{9}{3} = 3$. ✓"
        r" The correct answer is **5**.",
        ["Eq(Rational(5 + 4, 5 - 2), 3)"]))

    # Q8 M psda spread comparison (listed)
    assert Fraction(68 + 70 + 72, 3) == 70 == Fraction(50 + 70 + 90, 3)
    qs.append(mcq_listed(
        "SAT-P4-M2H-Q08", M, 8, "psda", "one_var_data", "medium",
        r"Data set A is $\{68, 70, 72\}$ and data set B is"
        r" $\{50, 70, 90\}$. Which statement correctly compares the two"
        r" data sets?",
        {"A": r"The means are equal, and the standard deviations are equal.",
         "B": r"The means are equal, and the standard deviation of B is larger.",
         "C": r"The mean of B is larger, and the standard deviations are equal.",
         "D": r"The mean of A is larger, and the standard deviation of B is smaller."},
        "B",
        r"Both sets have mean 70, but B's values sit much farther from"
        r" that mean (20 away versus 2 away), so B has the larger"
        r" standard deviation — spread measures DISTANCE from the mean,"
        r" not the number of values."
        r" The correct answer is **B**.",
        ["Eq(Rational(68 + 70 + 72, 3), 70)",
         "Eq(Rational(50 + 70 + 90, 3), 70)", "20 > 2"]))

    # Q9 M alg infinitely many solutions — a = 4
    assert Fraction(6, 9) == Fraction(4, 6) == Fraction(10, 15)
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$6x + 9y = 15$$ $$ax + 6y = 10$$"
        r" In the system of equations above, $a$ is a constant. If the"
        r" system has infinitely many solutions, what is the value of"
        r" $a$?",
        r"Infinitely many solutions means the equations describe the SAME"
        r" line: multiplying the first equation by $\tfrac{2}{3}$ gives"
        r" $$4x + 6y = 10,$$"
        r" so $a = 4$ (all three ratios $\tfrac{6}{a} = \tfrac{9}{6} ="
        r" \tfrac{15}{10}$ agree). Copying 6 or 9 from the first"
        r" equation ignores the scaling."
        r" The correct answer is **B**.",
        ["Eq(Rational(2, 3)*6, 4)", "Eq(Rational(2, 3)*9, 6)",
         "Eq(Rational(2, 3)*15, 10)"],
        4, {2: "10/5 guess", 6: "copied coefficient", 9: "copied coefficient"}))

    # Q10 H adv exponential interpretation (listed)
    qs.append(mcq_listed(
        "SAT-P4-M2H-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "hard",
        r"The population of a town is modeled by"
        r" $P(t) = 340(1.5)^{t/8}$, where $t$ is the number of years"
        r" after 2020. Which statement is the best interpretation of this"
        r" model?",
        {"A": r"The population increases by 50\% every 8 years.",
         "B": r"The population increases by 50\% every year.",
         "C": r"The population increases by 150\% every 8 years.",
         "D": r"The population increases by 8\% every 1.5 years."},
        "A",
        r"Each time $t$ increases by 8, the exponent $t/8$ increases by"
        r" 1, so the population is multiplied by $1.5$ — a 50\% increase"
        r" every 8 YEARS. Per single year the growth is only"
        r" $1.5^{1/8} \approx 1.052$; and multiplying by 1.5 is a 50\%"
        r" increase, not 150\%."
        r" The correct answer is **A**.",
        ["Eq(Rational(8, 8), 1)", "Eq(Rational(3, 2) - 1, Rational(1, 2))"]))

    # Q11 H adv extend a quadratic model beyond the table, FIGURE
    tbl = {xx: 4 - (xx - 3)**2 for xx in (1, 2, 3, 4, 5)}
    assert list(tbl.values()) == [0, 3, 4, 3, 0]
    assert 4 - (7 - 3)**2 == -12
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q11", M, 11, "advanced_math", "nonlinear_functions",
        "hard",
        r"The table shows five values of the quadratic function $f$."
        r" What is the value of $f(7)$?",
        r"The outputs are symmetric about $x = 3$ with maximum 4, so"
        r" $$f(x) = 4 - (x - 3)^2.$$"
        r" Then"
        r" $$f(7) = 4 - 4^2 = -12.$$"
        r" Extending the pattern linearly from the last two entries"
        r" ($3 \to 0$) suggests $-6$ at $x = 7$ — but a quadratic falls"
        r" faster and faster; $f(6) = -5$, and 0 merely repeats the edge"
        r" of the table."
        r" The correct answer is **A**.",
        ["Eq(4 - (1 - 3)**2, 0)", "Eq(4 - (3 - 3)**2, 4)",
         "Eq(4 - (7 - 3)**2, -12)"],
        -12, {-6: "linear extension", -5: "f(6)", 0: "edge of table"},
        fig=figure("sat-p4-m2h-q11",
                   "Table with x values 1, 2, 3, 4, 5 and f(x) values 0, "
                   "3, 4, 3, 0.")))

    # Q12 H psda SPR — conditional from two-way, 2/5, FIGURE
    assert Fraction(8, 12 + 8) == Fraction(2, 5)
    qs.append(spr(
        "SAT-P4-M2H-Q12", M, 12, "psda", "probability_conditional", "hard",
        r"The two-way table classifies 50 employees by work location and"
        r" years of service. If one of the REMOTE employees is selected"
        r" at random, what is the probability that the employee has at"
        r" least 5 years of service? (Enter your answer as a fraction or"
        r" decimal.)",
        ["2/5", ".4", "0.4"],
        r"The condition restricts attention to the $12 + 8 = 20$ remote"
        r" employees, of whom 8 have at least 5 years:"
        r" $$P(\ge 5 \mid \text{remote}) = \frac{8}{20} = \frac{2}{5}.$$"
        r" The correct answer is **2/5** (or 0.4).",
        ["Eq(12 + 8, 20)", "Eq(Rational(8, 20), Rational(2, 5))"],
        fig=figure("sat-p4-m2h-q12",
                   "Two-way table of 50 employees by location (Remote, "
                   "Office) and service (Under 5 years, 5 or more years): "
                   "Remote 12 and 8; Office 18 and 12.")))

    # Q13 H alg absolute-value inequality (listed)
    assert abs(0 - 3) < 5 and not abs(9 - 3) < 5
    qs.append(mcq_listed(
        "SAT-P4-M2H-Q13", M, 13, "algebra", "linear_inequalities", "hard",
        r"Which of the following describes the complete solution set of"
        r" $|x - 3| < 5$?",
        {"A": r"$x < 8$",
         "B": r"$x < -2$ or $x > 8$",
         "C": r"$-2 < x < 8$",
         "D": r"$-5 < x < 5$"},
        "C",
        r"$|x - 3| < 5$ means $x$ is within 5 units of 3:"
        r" $$-5 < x - 3 < 5 \;\Rightarrow\; -2 < x < 8.$$"
        r" The two-sided \"or\" split describes the OPPOSITE inequality"
        r" ($> 5$), and $-5 < x < 5$ forgets to shift by 3."
        r" The correct answer is **C**.",
        ["Abs(0 - 3) < 5", "Abs(-2 - 3) >= 5", "Abs(8 - 3) >= 5"]))

    # Q14 H adv rational simplification (listed)
    assert expand((2 * x + 3) * (3 * x - 1)) == 6 * x**2 + 7 * x - 3
    qs.append(mcq_listed(
        "SAT-P4-M2H-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "hard",
        r"For $x \ne -\tfrac{3}{2}$, which of the following is equivalent"
        r" to $\dfrac{6x^2 + 7x - 3}{2x + 3}$?",
        {"A": r"$3x - 1$",
         "B": r"$3x + 1$",
         "C": r"$2x - 3$",
         "D": r"$3x^2 - 1$"},
        "A",
        r"Factor the numerator:"
        r" $$6x^2 + 7x - 3 = (2x + 3)(3x - 1),$$"
        r" so the fraction simplifies to $3x - 1$. Check with $x = 1$:"
        r" $\frac{6 + 7 - 3}{5} = 2$ and $3(1) - 1 = 2$. ✓"
        r" The correct answer is **A**.",
        ["Eq(expand((2*x + 3)*(3*x - 1)), 6*x**2 + 7*x - 3)",
         "Eq(Rational(6 + 7 - 3, 5), 2)"]))

    # Q15 H geo SPR — circle radius through (6, 8), r = 10
    assert 6**2 + 8**2 == 100
    qs.append(spr(
        "SAT-P4-M2H-Q15", M, 15, "geometry_trig", "circles", "hard",
        r"A circle in the $xy$-plane has its center at the origin and"
        r" passes through the point $(6, 8)$. What is the radius of the"
        r" circle?",
        ["10"],
        r"The radius is the distance from the center to any point on the"
        r" circle:"
        r" $$r = \sqrt{6^2 + 8^2} = \sqrt{100} = 10.$$"
        r" The correct answer is **10**.",
        ["Eq(sqrt(6**2 + 8**2), 10)"]))

    # Q16 H alg investment split — 8% portion is 4000
    assert Fraction(5, 100) * 2000 + Fraction(8, 100) * 4000 == 420
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q16", M, 16, "algebra", "systems_two_linear", "hard",
        r"Tuya invested a total of \$6,000 in two accounts, one earning"
        r" 5\% simple interest per year and the other earning 8\%. The"
        r" total interest earned in the first year was \$420. How many"
        r" dollars were invested in the 8\% account?",
        r"With $a + b = 6000$ and $0.05a + 0.08b = 420$: if ALL the money"
        r" earned 5\%, the interest would be \$300, so the extra"
        r" $420 - 300 = 120$ comes from the 3-point difference:"
        r" $$0.03b = 120 \;\Rightarrow\; b = 4000.$$"
        r" Check: $0.05(2000) + 0.08(4000) = 100 + 320 = 420$. ✓ The"
        r" \$2,000 is the 5\% account; \$3,000 assumes an even"
        r" split."
        r" The correct answer is **D**.",
        ["Eq(Rational(5, 100)*6000, 300)",
         "Eq(Rational(420 - 300, 1)/Rational(3, 100), 4000)",
         "Eq(Rational(5, 100)*2000 + Rational(8, 100)*4000, 420)"],
        4000, {2000: "the 5% account", 3000: "even split",
               3500: "midpoint guess"}))

    # Q17 H geo cofunction identity — x = 16
    assert 3 * 16 + (2 * 16 + 10) == 90
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q17", M, 17, "geometry_trig", "right_triangles_trig",
        "hard",
        r"In the equation below, all angle measures are in degrees and"
        r" the angles involved are acute."
        r" $$\sin(3x)° = \cos(2x + 10)°$$"
        r" What is the value of $x$?",
        r"Sine and cosine of COMPLEMENTARY angles are equal, so"
        r" $$3x + (2x + 10) = 90 \;\Rightarrow\; 5x = 80 \;\Rightarrow\;"
        r" x = 16.$$"
        r" Setting the two angles EQUAL ($3x = 2x + 10$) gives 10 — that"
        r" is the rule for the same function, not for sine and cosine."
        r" The correct answer is **B**.",
        ["Eq((90 - 10)/5, 16)", "Eq(3*16 + 2*16 + 10, 90)"],
        16, {10: "set angles equal", 26: "sign slip on 10",
             80: "stopped at 5x = 80"}))

    # Q18 H adv reflected/shifted vertex (listed)
    assert (-(-1) + 3, ) == (4, )
    qs.append(mcq_listed(
        "SAT-P4-M2H-Q18", M, 18, "advanced_math", "nonlinear_functions",
        "hard",
        r"The graph of the quadratic function $f$ opens upward and has"
        r" its vertex at $(4, -1)$. The function $g$ is defined by"
        r" $g(x) = -f(x) + 3$. Which statement about the graph of $g$ is"
        r" true?",
        {"A": r"It opens upward with vertex $(4, 2)$.",
         "B": r"It opens downward with vertex $(-4, 4)$.",
         "C": r"It opens downward with vertex $(4, 4)$.",
         "D": r"It opens upward with vertex $(4, -4)$.",},
        "C",
        r"The factor $-1$ reflects the graph across the $x$-axis (so it"
        r" opens DOWNWARD and the vertex's $y$-value flips from $-1$ to"
        r" $1$), then the $+3$ shifts it up: $1 + 3 = 4$. The"
        r" $x$-coordinate never changes:"
        r" $$\text{vertex } (4, 4).$$"
        r" The correct answer is **C**.",
        ["Eq(-(-1) + 3, 4)"]))

    # Q19 H alg SPR — slope condition, k = 6
    assert Fraction(10 - 6, 6 - 4) == 2
    qs.append(spr(
        "SAT-P4-M2H-Q19", M, 19, "algebra", "linear_functions", "hard",
        r"In the $xy$-plane, the line through the points $(4, k)$ and"
        r" $(k, 10)$ has slope 2, where $k$ is a constant. What is the"
        r" value of $k$?",
        ["6"],
        r"Apply the slope formula:"
        r" $$\frac{10 - k}{k - 4} = 2 \;\Rightarrow\; 10 - k = 2k - 8"
        r" \;\Rightarrow\; 18 = 3k \;\Rightarrow\; k = 6.$$"
        r" Check: from $(4, 6)$ to $(6, 10)$, slope $= \frac{4}{2} = 2$. ✓"
        r" The correct answer is **6**.",
        ["Eq(Rational(10 - 6, 6 - 4), 2)"]))

    # Q20 H adv projectile maximum — 69
    assert -16 * 2**2 + 64 * 2 + 5 == 69
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q20", M, 20, "advanced_math", "nonlinear_functions",
        "hard",
        r"A ball is launched upward so that its height, in feet, $t$"
        r" seconds after launch is $h(t) = -16t^2 + 64t + 5$. What is the"
        r" maximum height, in feet, reached by the ball?",
        r"The vertex is at $t = -\frac{64}{2(-16)} = 2$ seconds:"
        r" $$h(2) = -64 + 128 + 5 = 69.$$"
        r" 2 is the TIME of the peak, 5 is the launch height, and 64 is"
        r" just the middle coefficient."
        r" The correct answer is **D**.",
        ["Eq(Rational(-64, 2*(-16)), 2)", "Eq(-16*2**2 + 64*2 + 5, 69)"],
        69, {2: "time of the peak", 5: "launch height", 64: "the coefficient"}))

    # Q21 H alg closing speed — 2.5 hours
    assert Fraction(360, 60 + 84) == Fraction(5, 2)
    qs.append(mcq_numeric(
        "SAT-P4-M2H-Q21", M, 21, "algebra", "linear_equations_one_var",
        "hard",
        r"Two trains start 360 miles apart and travel toward each other"
        r" on parallel tracks, one at 60 miles per hour and the other at"
        r" 84 miles per hour. How many hours after starting do they"
        r" meet?",
        r"Their distance closes at the COMBINED speed $60 + 84 = 144$"
        r" miles per hour:"
        r" $$t = \frac{360}{144} = 2.5 \text{ hours}.$$"
        r" Dividing by 120 (a mis-added speed sum) gives 3, and using"
        r" only the slower train's speed gives 6."
        r" The correct answer is **B**.",
        ["Eq(60 + 84, 144)", "Eq(Rational(360, 144), Rational(5, 2))"],
        Fraction(5, 2), {2: "mis-added to 180", 3: "divided by 120",
                         6: "one train only"},
        fmt=lambda v: smart(v)))

    # Q22 H adv SPR — roots differing by 3, c = 18
    assert 6 + 3 == 9 and 6 - 3 == 3 and 6 * 3 == 18
    assert expand((x - 6) * (x - 3)) == x**2 - 9 * x + 18
    qs.append(spr(
        "SAT-P4-M2H-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$x^2 - 9x + c = 0$$"
        r" In the equation above, $c$ is a constant. The equation has two"
        r" solutions whose difference is 3. What is the value of $c$?",
        ["18"],
        r"The solutions sum to 9 (Vieta) and differ by 3, so they are"
        r" $$\frac{9 + 3}{2} = 6 \quad\text{and}\quad \frac{9 - 3}{2} = 3.$$"
        r" Then $c$ is their product: $6 \times 3 = 18$. Check:"
        r" $(x - 6)(x - 3) = x^2 - 9x + 18$. ✓"
        r" The correct answer is **18**.",
        ["Eq(expand((x - 6)*(x - 3)), x**2 - 9*x + 18)", "Eq(6 - 3, 3)"]))

    return qs


# ─── blueprint conformance + emit ─────────────────────────────────────

M1_SPEC = dict(diff_mix={"easy": 8, "medium": 9, "hard": 5},
               spr_slots={4, 9, 14, 18, 21},
               domains={"algebra": 7, "advanced_math": 7, "psda": 4,
                        "geometry_trig": 4})
M2_DOMAINS = {"algebra": 8, "advanced_math": 8, "psda": 3,
              "geometry_trig": 3}
M2_SPR = {3, 7, 12, 15, 19, 22}


def main() -> None:
    m1 = module1()
    m2e = module2_easy()
    m2h = module2_hard()
    print("blueprint conformance:")
    check_module("module1", m1, **M1_SPEC)
    check_module("module2Easy", m2e,
                 diff_mix={"easy": 11, "medium": 9, "hard": 2},
                 spr_slots=M2_SPR, domains=M2_DOMAINS)
    check_module("module2Hard", m2h,
                 diff_mix={"easy": 2, "medium": 7, "hard": 13},
                 spr_slots=M2_SPR, domains=M2_DOMAINS)
    write_test(REPO / "data" / "sat" / "sat-practice-4.json",
               {"testId": "sat-practice-4",
                "label": "SAT Math Practice Test 4",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
