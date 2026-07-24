#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 6 (data/sat/sat-practice-6.json).

Built on scripts/test-builders/satbuild.py — only stems, parameters,
computed answers, named distractor error models, verify[] strings, and
solutions live here.

Archetype freshness versus tests 1-5 (audited question-by-question before
authoring). New to the bank in this test:
  * sample_stats_margin_error and evaluating_claims_experiments — two
    PSDA skills from the blueprint that had never appeared in tests 1-5.
  * residual (actual minus predicted) off a line of best fit
  * literal equations (solve a formula for one of its variables)
  * compound inequalities and a two-constraint feasibility ceiling
  * add-the-equations systems (asking for x + y, never x alone)
  * graph transformations y = f(x - h) + k
  * arithmetic sequence as a linear function
  * age-relationship system, mean-replacement, reverse percent chain
  * trapezoid area, sphere volume + volume scaling, vertical angles,
    parallelogram angles, tangent-radius perpendicularity, Thales
    right angle in a semicircle, 45-45-90 exact ratio
  * quadratic in disguise (x^4 - 13x^2 + 36 = 0), sum of rational
    expressions, composite equation f(g(a)) = k

Solution style: mcq_numeric distractor mentions describe the ERROR AND
ITS VALUE, never a choice letter — satbuild derives and rewrites the
closing letter line itself.

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

from sympy import Eq, Rational, expand, factor, simplify, sqrt, symbols
from sympy import solve as _solve

x, y = symbols("x y")


def frac(fr) -> str:
    fr = Fraction(fr)
    if fr.denominator == 1:
        return f"${fr.numerator}$"
    sign = "-" if fr.numerator < 0 else ""
    return rf"${sign}\dfrac{{{abs(fr.numerator)}}}{{{fr.denominator}}}$"


def dec(v) -> str:
    return f"${float(Fraction(v)):g}$"


def smart(v) -> str:
    """Integers and terminating decimals as decimals, everything else as a
    display fraction — so an option set never mixes 3.5 with 7/2."""
    fr = Fraction(v)
    if fr.denominator == 1:
        return f"${fr.numerator}$"
    if 10 % fr.denominator == 0 or 100 % fr.denominator == 0:
        return dec(v)
    return frac(v)


def money(v) -> str:
    f = float(Fraction(v))
    return rf"$\${f:g}$"


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E algebra linear_equations_one_var — variable on both sides
    assert _solve(Eq(5 * x + 12, 3 * x + 26), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $5x + 12 = 3x + 26$, what is the value of $x$?",
        r"Collect the variable terms on the left and the constants on the right:"
        r" $$5x - 3x = 26 - 12 \;\Rightarrow\; 2x = 14 \;\Rightarrow\; x = 7.$$"
        r" Adding $3x$ instead of subtracting it gives $8x = 14$, or $1.75$;"
        r" adding 12 to both sides gives $2x = 38$, or $19$; and stopping at"
        r" $2x = 14$ but multiplying gives 28."
        r" The correct answer is **B**.",
        ["Eq(5*7 + 12, 3*7 + 26)", "Eq((26 - 12)/(5 - 3), 7)"],
        7, {Rational(7, 4): "added 3x instead of subtracting it",
            19: "added 12 to both sides instead of subtracting",
            28: "multiplied by 2 instead of dividing"}, fmt=smart))

    # Q2 E advanced equivalent_expressions — product of two binomials
    assert expand((2 * x + 5) * (x - 3)) == 2 * x**2 - x - 15
    qs.append(mcq_listed(
        "SAT-P6-M1-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $(2x + 5)(x - 3)$?",
        {"A": r"$2x^2 - 11x - 15$", "B": r"$2x^2 - x - 15$",
         "C": r"$2x^2 - x + 15$", "D": r"$2x^2 + x - 15$"}, "B",
        r"Multiply each pair of terms:"
        r" $$(2x + 5)(x - 3) = 2x^2 - 6x + 5x - 15 = 2x^2 - x - 15.$$"
        r" Adding the inner and outer terms as $-6x - 5x$ gives $-11x$, and"
        r" mis-signing the last product gives $+15$."
        r" The correct answer is **B**.",
        ["Eq(expand((2*x + 5)*(x - 3)), 2*x**2 - x - 15)",
         "Eq(expand((2*x + 5)*(x - 3)) - (2*x**2 - 11*x - 15), 10*x)"]))

    # Q3 E psda ratios_rates_units — constant production rate
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q03", M, 3, "psda", "ratios_rates_units", "easy",
        r"A machine produces $18$ items every $4$ minutes at a constant rate."
        r" At this rate, how many items does the machine produce in $30$ minutes?",
        r"The rate is $\frac{18}{4} = 4.5$ items per minute, so in 30 minutes"
        r" the machine produces"
        r" $$4.5 \times 30 = 135 \text{ items}.$$"
        r" Multiplying $18 \times 30$ without dividing by the 4-minute interval"
        r" gives 540; $18 \times 4$ gives 72 (the count in 16 minutes); and"
        r" $30 \times 4$ gives 120."
        r" The correct answer is **C**.",
        ["Eq(Rational(18,4)*30, 135)", "Eq(135*4, 18*30)"],
        135, {540: "multiplied 18 by 30, ignoring the 4-minute interval",
              72: "multiplied 18 by 4", 120: "multiplied 30 by 4"}, fmt=smart))

    # Q4 SPR E algebra linear_functions — solve f(k) = value
    assert _solve(Eq(6 * x - 11, 25), x) == [6]
    qs.append(spr(
        "SAT-P6-M1-Q04", M, 4, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 6x - 11$. If $f(k) = 25$,"
        r" what is the value of $k$?",
        ["6"],
        r"Substitute and solve:"
        r" $$6k - 11 = 25 \;\Rightarrow\; 6k = 36 \;\Rightarrow\; k = 6.$$"
        r" The correct answer is **6**.",
        ["Eq(6*6 - 11, 25)"]))

    # Q5 E geometry area_volume — trapezoid area (fresh shape for the bank)
    B_BOT, B_TOP, TRAP_H = 14, 8, 6
    assert Rational(B_BOT + B_TOP, 2) * TRAP_H == 66
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        rf"The trapezoid shown has parallel sides of length ${B_TOP}$ and"
        rf" ${B_BOT}$ and a height of ${TRAP_H}$. What is the area of the"
        r" trapezoid?",
        rf"The area of a trapezoid is the average of the parallel sides times"
        rf" the height:"
        rf" $$A = \frac{{{B_TOP} + {B_BOT}}}{{2}} \cdot {TRAP_H}"
        rf" = 11 \cdot {TRAP_H} = 66.$$"
        r" Forgetting to halve the sum gives $22 \cdot 6 = 132$, and using only"
        r" one of the parallel sides gives $8 \cdot 6 = 48$ or $14 \cdot 6 = 84$."
        r" The correct answer is **B**.",
        [f"Eq(Rational({B_TOP} + {B_BOT}, 2)*{TRAP_H}, 66)",
         f"Eq(({B_TOP} + {B_BOT})*{TRAP_H}, 132)"],
        66, {48: "used only the shorter parallel side",
             84: "used only the longer parallel side",
             132: "forgot to halve the sum of the parallel sides"}, fmt=smart,
        fig=figure("sat-p6-m1-q05",
                   "Isosceles trapezoid with parallel sides 8 (top) and 14 "
                   "(bottom) and a dashed height segment of 6")))

    # Q6 E advanced nonlinear_functions — evaluate at a negative input
    assert (-3) ** 2 + 2 * (-3) - 4 == -1
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = x^2 + 2x - 4$."
        r" What is the value of $f(-3)$?",
        r"Substitute $x = -3$, squaring before multiplying:"
        r" $$f(-3) = (-3)^2 + 2(-3) - 4 = 9 - 6 - 4 = -1.$$"
        r" Treating $(-3)^2$ as $-9$ gives $-19$; using $x = 3$ gives"
        r" $9 + 6 - 4 = 11$; and combining $-9 + 6 - 4$ gives $-7$."
        r" The correct answer is **C**.",
        ["Eq((-3)**2 + 2*(-3) - 4, -1)", "Eq(3**2 + 2*3 - 4, 11)"],
        -1, {-19: "treated the square of -3 as -9",
             11: "substituted positive 3",
             -7: "made both a square and a sign slip"}, fmt=smart))

    # Q7 E algebra linear_equations_two_var — slope from two points
    assert Rational(21 - 9, 6 - 2) == 3
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q07", M, 7, "algebra", "linear_equations_two_var", "easy",
        r"Line $\ell$ passes through the points $(2, 9)$ and $(6, 21)$ in the"
        r" $xy$-plane. What is the slope of line $\ell$?",
        r"Slope is the change in $y$ over the change in $x$:"
        r" $$m = \frac{21 - 9}{6 - 2} = \frac{12}{4} = 3.$$"
        r" Inverting the ratio gives $\frac{1}{3}$, reversing the order in only"
        r" the numerator gives $-3$, and dividing the $y$-difference by 6 gives 2."
        r" The correct answer is **D**.",
        ["Eq(Rational(21 - 9, 6 - 2), 3)", "Eq(9 + 3*(6 - 2), 21)"],
        3, {Rational(1, 3): "inverted the ratio to run over rise",
            -3: "reversed the order in the numerator only",
            2: "divided the y-difference by 6"}, fmt=smart))

    # Q8 E geometry lines_angles_triangles — isosceles base angles
    assert Rational(180 - 44, 2) == 68
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q08", M, 8, "geometry_trig", "lines_angles_triangles", "easy",
        r"In isosceles triangle $ABC$ shown, $AB = AC$ and the angle at vertex"
        r" $A$ measures $44^\circ$. What is the measure, in degrees, of angle"
        r" $B$?",
        r"The angles opposite the two equal sides are equal, so angles $B$ and"
        r" $C$ have the same measure $b$. The three angles sum to $180^\circ$:"
        r" $$44 + 2b = 180 \;\Rightarrow\; 2b = 136 \;\Rightarrow\; b = 68.$$"
        r" Forgetting to halve gives 136, and taking the complement of"
        r" $44^\circ$ gives 46."
        r" The correct answer is **C**.",
        ["Eq(44 + 2*68, 180)", "Eq(Rational(180 - 44, 2), 68)"],
        68, {44: "assumed the base angles equal the vertex angle",
             46: "took the complement of the vertex angle",
             136: "forgot to divide the remaining measure by 2"}, fmt=smart,
        fig=figure("sat-p6-m1-q08",
                   "Isosceles triangle ABC with AB = AC and the angle at A "
                   "marked 44 degrees")))

    # Q9 SPR M advanced nonlinear_equations_systems — factor a quadratic
    assert sorted(_solve(Eq(x**2 - 11 * x + 28, 0), x)) == [4, 7]
    qs.append(spr(
        "SAT-P6-M1-Q09", M, 9, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What is the greater of the two solutions to $x^2 - 11x + 28 = 0$?",
        ["7"],
        r"Look for two numbers whose product is 28 and whose sum is $-11$:"
        r" those are $-4$ and $-7$, so"
        r" $$x^2 - 11x + 28 = (x - 4)(x - 7) = 0.$$"
        r" The solutions are $x = 4$ and $x = 7$, and the greater one is 7."
        r" The correct answer is **7**.",
        ["Eq(expand((x - 4)*(x - 7)), x**2 - 11*x + 28)",
         "Eq(7**2 - 11*7 + 28, 0)", "7 > 4"]))

    # Q10 M psda sample_stats_margin_error — read a margin of error as an
    # interval of plausible values for the POPULATION mean
    MOE_MEAN, MOE_E = Rational(24, 10), Rational(3, 10)
    assert MOE_MEAN - MOE_E == Rational(21, 10)
    assert MOE_MEAN + MOE_E == Rational(27, 10)
    qs.append(mcq_listed(
        "SAT-P6-M1-Q10", M, 10, "psda", "sample_stats_margin_error", "medium",
        r"A researcher surveyed $400$ households selected at random from a"
        r" city and found that the mean number of laptops per household was"
        r" $2.4$, with an associated margin of error of $0.3$. Which of the"
        r" following is the most appropriate conclusion?",
        {"A": r"Every household in the city owns between $2.1$ and $2.7$"
              r" laptops.",
         "B": r"It is plausible that the mean number of laptops per household"
              r" in the city is between $2.1$ and $2.7$.",
         "C": r"It is plausible that the mean number of laptops per household"
              r" in the city is between $2.4$ and $2.7$.",
         "D": r"The mean number of laptops per household in the city is"
              r" exactly $2.4$."}, "B",
        r"A margin of error extends the sample statistic in BOTH directions to"
        r" give an interval of plausible values for the POPULATION value:"
        r" $$2.4 - 0.3 = 2.1 \qquad\text{to}\qquad 2.4 + 0.3 = 2.7.$$"
        r" Two things must be right at once. The interval describes the"
        r" population MEAN, not each individual household — plenty of single"
        r" households will fall outside $2.1$ to $2.7$. And the sample mean of"
        r" $2.4$ is an estimate, so it does not pin the population mean to"
        r" exactly $2.4$; that is precisely what the margin of error exists to"
        r" express. Extending in only one direction gives the interval $2.4$ to"
        r" $2.7$."
        r" The correct answer is **B**.",
        ["Eq(Rational(24,10) - Rational(3,10), Rational(21,10))",
         "Eq(Rational(24,10) + Rational(3,10), Rational(27,10))"]))

    # Q11 M algebra systems_two_linear — add the equations, ask for x + y
    S1, S2 = Eq(3 * x + 5 * y, 29), Eq(5 * x + 3 * y, 35)
    _sol = _solve([S1, S2], [x, y], dict=True)[0]
    assert _sol[x] + _sol[y] == 8
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q11", M, 11, "algebra", "systems_two_linear", "medium",
        r"$$3x + 5y = 29$$ $$5x + 3y = 35$$"
        r" If $(x, y)$ is the solution to the system of equations above, what"
        r" is the value of $x + y$?",
        r"Adding the two equations pairs every $x$ with every $y$:"
        r" $$8x + 8y = 64.$$"
        r" Dividing by 8 gives the sum directly:"
        r" $$x + y = 8.$$"
        r" Stopping at $8x + 8y = 64$ gives 64 and halving it gives 32;"
        r" subtracting the equations instead produces $x - y = 3$."
        r" The correct answer is **B**.",
        ["Eq(3*Rational(11,2) + 5*Rational(5,2), 29)",
         "Eq(5*Rational(11,2) + 3*Rational(5,2), 35)",
         "Eq(Rational(11,2) + Rational(5,2), 8)"],
        8, {3: "subtracted the equations and found x - y",
            32: "divided 64 by 2 instead of 8",
            64: "stopped at 8x + 8y = 64"}, fmt=smart))

    # Q12 M advanced nonlinear_functions — graph transformation
    qs.append(mcq_listed(
        "SAT-P6-M1-Q12", M, 12, "advanced_math", "nonlinear_functions", "medium",
        r"The graph of $y = f(x)$ in the $xy$-plane has a maximum at the point"
        r" $(2, 5)$. The graph of $y = f(x - 3) + 4$ has a maximum at which"
        r" point?",
        {"A": r"$(-1, 1)$", "B": r"$(-1, 9)$", "C": r"$(5, 1)$",
         "D": r"$(5, 9)$"}, "D",
        r"Replacing $x$ by $x - 3$ shifts the graph 3 units to the RIGHT, and"
        r" adding 4 shifts it 4 units UP. The maximum point moves with the"
        r" graph:"
        r" $$(2, 5) \longrightarrow (2 + 3,\; 5 + 4) = (5, 9).$$"
        r" Reading $x - 3$ as a shift to the left gives an $x$-coordinate of"
        r" $-1$, and subtracting 4 instead of adding gives a $y$-coordinate of 1."
        r" The correct answer is **D**.",
        ["Eq(2 + 3, 5)", "Eq(5 + 4, 9)"]))

    # Q13 M geometry right_triangles_trig — 45-45-90 exact ratio
    LEG45 = 7
    assert simplify(sqrt(2) * LEG45**2 - LEG45 * sqrt(2) * LEG45) == 0
    qs.append(mcq_listed(
        "SAT-P6-M1-Q13", M, 13, "geometry_trig", "right_triangles_trig", "medium",
        rf"In the right triangle shown, both legs have length ${LEG45}$ and the"
        r" two acute angles each measure $45^\circ$. What is the length of the"
        r" hypotenuse?",
        {"A": r"$\dfrac{7\sqrt{2}}{2}$", "B": r"$7$", "C": r"$7\sqrt{2}$",
         "D": r"$14$"}, "C",
        rf"By the Pythagorean theorem with both legs equal to ${LEG45}$:"
        rf" $$h^2 = {LEG45}^2 + {LEG45}^2 = 2 \cdot 49 = 98"
        rf" \;\Rightarrow\; h = \sqrt{{98}} = 7\sqrt{{2}}.$$"
        r" This is the $45^\circ$-$45^\circ$-$90^\circ$ ratio"
        r" $1 : 1 : \sqrt{2}$ on the reference sheet. Doubling a leg gives 14,"
        r" and dividing by $\sqrt{2}$ instead of multiplying gives"
        r" $\frac{7\sqrt{2}}{2}$."
        r" The correct answer is **C**.",
        [f"Eq({LEG45}**2 + {LEG45}**2, 98)", "Eq(sqrt(98), 7*sqrt(2))",
         "Eq(simplify(7*sqrt(2)/2 * sqrt(2)), 7)"],
        fig=figure("sat-p6-m1-q13",
                   "Right triangle with two legs of length 7 and a 45 degree "
                   "angle marked at the bottom-left vertex")))

    # Q14 SPR M psda one_var_data — mean from a frequency table
    VALS, FREQ = [2, 3, 4, 5], [3, 5, 8, 4]
    assert sum(FREQ) == 20 and sum(v * f for v, f in zip(VALS, FREQ)) == 73
    assert Rational(73, 20) == Rational(365, 100)
    qs.append(spr(
        "SAT-P6-M1-Q14", M, 14, "psda", "one_var_data", "medium",
        r"The table shows the number of pets owned by each of the $20$ families"
        r" surveyed. What is the mean number of pets per family?",
        ["3.65", "73/20"],
        r"The mean is the total number of pets divided by the number of"
        r" families. Weight each value by how many families reported it:"
        r" $$2(3) + 3(5) + 4(8) + 5(4) = 6 + 15 + 32 + 20 = 73.$$"
        r" There are $3 + 5 + 8 + 4 = 20$ families, so"
        r" $$\text{mean} = \frac{73}{20} = 3.65.$$"
        r" Averaging just the four listed values, $\frac{2+3+4+5}{4} = 3.5$,"
        r" ignores how often each occurs."
        r" The correct answer is **3.65**.",
        ["Eq(2*3 + 3*5 + 4*8 + 5*4, 73)", "Eq(3 + 5 + 8 + 4, 20)",
         "Eq(Rational(73, 20), Rational(73, 20))",
         "Abs(Rational(73,20) - 3.65) < Rational(1,1000)"],
        fig=figure("sat-p6-m1-q14",
                   "Two-row table listing pets owned 2, 3, 4, 5 against number "
                   "of families 3, 5, 8, 4")))

    # Q15 M algebra linear_inequalities — compound inequality
    qs.append(mcq_listed(
        "SAT-P6-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"Which of the following gives all solutions of $-7 < 2x - 3 \le 9$?",
        {"A": r"$-5 < x \le 3$", "B": r"$-2 \le x < 6$",
         "C": r"$-2 < x \le 6$", "D": r"$2 < x \le 6$"}, "C",
        r"Work on all three parts at once. Add 3 throughout:"
        r" $$-4 < 2x \le 12.$$"
        r" Then divide throughout by 2, which is positive and so preserves both"
        r" inequality signs:"
        r" $$-2 < x \le 6.$$"
        r" The strict sign stays on the left and the inclusive sign on the"
        r" right; swapping them gives $-2 \le x < 6$. Subtracting 3 instead of"
        r" adding gives $-5 < x \le 3$."
        r" The correct answer is **C**.",
        ["Eq((-7 + 3)/2, -2)", "Eq((9 + 3)/2, 6)",
         "(2*0 - 3 > -7) & (2*0 - 3 <= 9)"]))

    # Q16 M advanced equivalent_expressions — difference of squares, factoring
    assert expand((4 * x - 7) * (4 * x + 7)) == 16 * x**2 - 49
    qs.append(mcq_listed(
        "SAT-P6-M1-Q16", M, 16, "advanced_math", "equivalent_expressions",
        "medium",
        r"Which of the following is equivalent to $16x^2 - 49$?",
        {"A": r"$(2x - 7)(8x + 7)$", "B": r"$(4x - 7)(4x + 7)$",
         "C": r"$(4x + 7)^2$", "D": r"$(4x - 49)(4x + 1)$"}, "B",
        r"Both terms are perfect squares: $16x^2 = (4x)^2$ and $49 = 7^2$."
        r" A difference of squares factors as"
        r" $$a^2 - b^2 = (a - b)(a + b),$$"
        r" so"
        r" $$16x^2 - 49 = (4x - 7)(4x + 7).$$"
        r" The expression is a DIFFERENCE, so it is not the perfect square"
        r" $(4x + 7)^2 = 16x^2 + 56x + 49$; and $(2x - 7)(8x + 7)$ expands to"
        r" $16x^2 - 42x - 49$, which has an unwanted $x$-term."
        r" The correct answer is **B**.",
        ["Eq(expand((4*x - 7)*(4*x + 7)), 16*x**2 - 49)",
         "Eq(expand((4*x + 7)**2), 16*x**2 + 56*x + 49)",
         "Eq(expand((2*x - 7)*(8*x + 7)), 16*x**2 - 42*x - 49)"]))

    # Q17 M algebra linear_equations_one_var — literal equation
    qs.append(mcq_listed(
        "SAT-P6-M1-Q17", M, 17, "algebra", "linear_equations_one_var", "medium",
        r"The formula $A = P(1 + rt)$ gives the value $A$ of an investment of"
        r" $P$ dollars earning simple interest at annual rate $r$ for $t$ years."
        r" Which of the following expresses $r$ in terms of $A$, $P$, and $t$?",
        {"A": r"$r = \dfrac{A - P}{t}$", "B": r"$r = \dfrac{A - Pt}{P}$",
         "C": r"$r = \dfrac{A}{Pt} - 1$", "D": r"$r = \dfrac{A - P}{Pt}$"},
        "D",
        r"Distribute $P$ so the term containing $r$ stands alone:"
        r" $$A = P + Prt.$$"
        r" Subtract $P$ from both sides:"
        r" $$A - P = Prt.$$"
        r" Then divide both sides by $Pt$, which is the entire coefficient of $r$:"
        r" $$r = \frac{A - P}{Pt}.$$"
        r" Dividing by only $t$ leaves the factor $P$ behind, and dividing"
        r" $A = P(1 + rt)$ by $Pt$ before subtracting produces"
        r" $\frac{A}{Pt} - \frac{1}{t}$, not $\frac{A}{Pt} - 1$."
        r" The correct answer is **D**.",
        ["Eq(simplify(100*(1 + Rational(1,20)*3)), 115)",
         "Eq(simplify((115 - 100)/(100*3)), Rational(1,20))"]))

    # Q18 SPR H advanced nonlinear_equations_systems — parabola meets a
    # horizontal line; sum of the x-coordinates
    assert sorted(_solve(Eq(x**2 - 5 * x + 9, 3), x)) == [2, 3]
    qs.append(spr(
        "SAT-P6-M1-Q18", M, 18, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"$$y = x^2 - 5x + 9$$ $$y = 3$$"
        r" The graphs of the equations above intersect at two points in the"
        r" $xy$-plane. What is the sum of the $x$-coordinates of those two"
        r" points?",
        ["5"],
        r"Set the expressions for $y$ equal and collect everything on one side:"
        r" $$x^2 - 5x + 9 = 3 \;\Rightarrow\; x^2 - 5x + 6 = 0.$$"
        r" Factoring gives $(x - 2)(x - 3) = 0$, so the intersection points have"
        r" $x = 2$ and $x = 3$, and"
        r" $$2 + 3 = 5.$$"
        r" Faster: for $x^2 + bx + c = 0$ the sum of the solutions is $-b$, and"
        r" here $-(-5) = 5$ — no factoring needed."
        r" The correct answer is **5**.",
        ["Eq(expand((x - 2)*(x - 3)), x**2 - 5*x + 6)",
         "Eq(2**2 - 5*2 + 9, 3)", "Eq(3**2 - 5*3 + 9, 3)", "Eq(2 + 3, 5)"]))

    # Q19 H psda two_var_data_models — residual off a line of best fit
    BF_M, BF_B, RES_X, RES_ACTUAL = 3, 12, 8, 40
    assert BF_M * RES_X + BF_B == 36 and RES_ACTUAL - 36 == 4
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q19", M, 19, "psda", "two_var_data_models", "hard",
        rf"The scatterplot shows the number of units $y$ assembled after $x$"
        rf" hours at a workshop, along with the line of best fit"
        rf" $y = {BF_M}x + {BF_B}$. For the data point at $x = {RES_X}$, the"
        rf" actual value of $y$ is ${RES_ACTUAL}$. By how much does the actual"
        rf" value exceed the value predicted by the line of best fit?",
        rf"Predict from the model first:"
        rf" $$y = {BF_M}({RES_X}) + {BF_B} = 24 + 12 = 36.$$"
        rf" The actual value is ${RES_ACTUAL}$, so the amount by which it"
        rf" exceeds the prediction — the residual — is"
        rf" $$40 - 36 = 4.$$"
        r" Reporting the prediction itself gives 36, subtracting the intercept"
        r" from the actual value gives $40 - 12 = 28$, and adding actual to"
        r" predicted gives 76."
        r" The correct answer is **A**.",
        [f"Eq({BF_M}*{RES_X} + {BF_B}, 36)", f"Eq({RES_ACTUAL} - 36, 4)"],
        4, {28: "subtracted the intercept from the actual value",
            36: "reported the predicted value itself",
            76: "added the actual and predicted values"}, fmt=smart,
        fig=figure("sat-p6-m1-q19",
                   "Scatterplot of units assembled versus hours with the line "
                   "of best fit y = 3x + 12 drawn through the points")))

    # Q20 H geometry circles — tangent is perpendicular to the radius
    TAN_R, TAN_OQ = 9, 15
    assert TAN_R**2 + 12**2 == TAN_OQ**2
    qs.append(mcq_numeric(
        "SAT-P6-M1-Q20", M, 20, "geometry_trig", "circles", "hard",
        rf"In the figure shown, the circle has center $O$ and radius ${TAN_R}$,"
        rf" and line $PQ$ is tangent to the circle at point $P$. If"
        rf" $OQ = {TAN_OQ}$, what is the length of $PQ$?",
        rf"A tangent line is perpendicular to the radius drawn to the point of"
        rf" tangency, so triangle $OPQ$ has a right angle at $P$. That makes"
        rf" $OQ$ the hypotenuse:"
        rf" $$PQ^2 = OQ^2 - OP^2 = {TAN_OQ}^2 - {TAN_R}^2 = 225 - 81 = 144,$$"
        rf" so $PQ = 12$."
        r" Treating the lengths as collinear gives $15 - 9 = 6$ or"
        r" $15 + 9 = 24$; adding the squares instead of subtracting treats $PQ$"
        r" as the hypotenuse, which the right angle at $P$ forbids."
        r" The correct answer is **B**.",
        [f"Eq({TAN_OQ}**2 - {TAN_R}**2, 144)", "Eq(sqrt(144), 12)",
         f"Eq({TAN_R}**2 + 12**2, {TAN_OQ}**2)"],
        12, {6: "subtracted the radius from OQ",
             18: "doubled the radius",
             24: "added the radius to OQ"}, fmt=smart,
        fig=figure("sat-p6-m1-q20",
                   "Circle with center O and radius 9, a tangent line touching "
                   "at P with a right-angle mark, and external point Q joined "
                   "to O by a segment of length 15")))

    # Q21 SPR H algebra systems_two_linear — parameter for NO solution
    assert Rational(6, 4) == Rational(9, 6) and Rational(21, 10) != Rational(6, 4)
    qs.append(spr(
        "SAT-P6-M1-Q21", M, 21, "algebra", "systems_two_linear", "hard",
        r"$$4x + 6y = 10$$ $$6x + ky = 21$$"
        r" In the system of equations above, $k$ is a constant. For what value"
        r" of $k$ does the system have no solution?",
        ["9"],
        r"A system of two linear equations has no solution exactly when the"
        r" lines are parallel but not identical — the coefficients are"
        r" proportional while the constants are not. Matching the $x$- and"
        r" $y$-coefficients:"
        r" $$\frac{6}{4} = \frac{k}{6} \;\Rightarrow\; k = 6 \cdot \frac{3}{2} = 9.$$"
        r" Check that the lines are not the same line: the constants give"
        r" $\frac{21}{10} = 2.1$, which does not equal $\frac{3}{2}$, so they"
        r" are parallel and distinct — no solution."
        r" The correct answer is **9**.",
        ["Eq(Rational(6,4), Rational(9,6))",
         "Rational(21,10) != Rational(6,4)",
         "Eq(simplify(Rational(3,2)*(4*x + 6*y)), 6*x + 9*y)"]))

    # Q22 H advanced nonlinear_functions — interpret an exponential base
    qs.append(mcq_listed(
        "SAT-P6-M1-Q22", M, 22, "advanced_math", "nonlinear_functions", "hard",
        r"The function $P(t) = 2400(0.94)^t$ models the number of trout in a"
        r" lake $t$ years after a survey began. Which of the following is the"
        r" best interpretation of $0.94$ in this context?",
        {"A": r"The number of trout is decreasing by $6\%$ each year.",
         "B": r"The number of trout is decreasing by $94\%$ each year.",
         "C": r"The number of trout is increasing by $6\%$ each year.",
         "D": r"The number of trout is increasing by $94\%$ each year."}, "A",
        r"In an exponential model $a \cdot b^t$, the base $b$ is the factor the"
        r" quantity is multiplied by each period. Write it as $1 + r$:"
        r" $$0.94 = 1 - 0.06,$$"
        r" so $r = -0.06$ — each year the population is $94\%$ of what it was,"
        r" which is a $6\%$ DECREASE. The base itself, $94\%$, is the fraction"
        r" that REMAINS, not the fraction lost; and because $0.94 < 1$ the model"
        r" cannot describe growth."
        r" The correct answer is **A**.",
        ["Eq(1 - Rational(94,100), Rational(6,100))",
         "Eq(2400*Rational(94,100), 2256)", "Rational(94,100) < 1"]))

    return qs


# ─── Module 2, easier variant (11E / 9M / 2H) ─────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E algebra one_var — distribute then solve
    assert _solve(Eq(4 * (x - 3), 20), x) == [8]
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $4(x - 3) = 20$, what is the value of $x$?",
        r"Divide both sides by 4 first, then undo the subtraction:"
        r" $$x - 3 = 5 \;\Rightarrow\; x = 8.$$"
        r" Stopping at $x - 3 = 5$ gives 5, adding 3 to 20 before dividing gives"
        r" 23, and subtracting 3 from 20 gives 17."
        r" The correct answer is **B**.",
        ["Eq(4*(8 - 3), 20)", "Eq(20/4 + 3, 8)"],
        8, {5: "stopped after dividing by 4", 17: "subtracted 3 from 20",
            23: "added 3 to 20 without dividing"}, fmt=smart))

    # Q2 E advanced equivalent_expressions — sum of two polynomials
    assert expand((5 * x**2 - 3 * x + 2) + (x**2 + 3 * x - 9)) == 6 * x**2 - 7
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to"
        r" $(5x^2 - 3x + 2) + (x^2 + 3x - 9)$?",
        {"A": r"$4x^2 - 7$", "B": r"$6x^2 - 6x - 7$", "C": r"$6x^2 - 7$",
         "D": r"$6x^2 + 11$"}, "C",
        r"Combine like terms:"
        r" $$(5x^2 + x^2) + (-3x + 3x) + (2 - 9) = 6x^2 + 0x - 7 = 6x^2 - 7.$$"
        r" The $x$-terms cancel exactly. Subtracting the second polynomial"
        r" instead of adding gives $4x^2 - 6x + 11$, and adding $-3x$ to $-3x$"
        r" leaves a spurious $-6x$."
        r" The correct answer is **C**.",
        ["Eq(expand((5*x**2 - 3*x + 2) + (x**2 + 3*x - 9)), 6*x**2 - 7)",
         "Eq(-3 + 3, 0)"]))

    # Q3 SPR E algebra linear_functions — evaluate
    qs.append(spr(
        "SAT-P6-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 3x + 7$. What is the value of"
        r" $f(5)$?",
        ["22"],
        r"Substitute $x = 5$:"
        r" $$f(5) = 3(5) + 7 = 15 + 7 = 22.$$"
        r" The correct answer is **22**.",
        ["Eq(3*5 + 7, 22)"]))

    # Q4 E psda percentages — part out of whole
    assert Rational(15, 25) * 100 == 60
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q04", M, 4, "psda", "percentages", "easy",
        r"In a class of $25$ students, $15$ are girls. What percent of the"
        r" students are girls?",
        r"Divide the part by the whole:"
        r" $$\frac{15}{25} = 0.6 = 60\%.$$"
        r" Reporting the count gives 15, and finding the percent who are NOT"
        r" girls gives $\frac{10}{25} = 40\%$."
        r" The correct answer is **C**.",
        ["Eq(Rational(15,25)*100, 60)", "Eq(Rational(10,25)*100, 40)"],
        60, {15: "reported the number of girls, not the percent",
             40: "found the percent who are not girls",
             75: "divided 15 by 20"}, fmt=smart))

    # Q5 E geometry area_volume — sphere volume
    SPH_R = 3
    assert Rational(4, 3) * SPH_R**3 == 36
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        rf"The sphere shown has a radius of ${SPH_R}$. What is the volume of"
        r" the sphere?",
        {"A": r"$12\pi$", "B": r"$27\pi$", "C": r"$36\pi$", "D": r"$108\pi$"},
        "C",
        rf"The reference sheet gives $V = \frac{{4}}{{3}}\pi r^3$. With"
        rf" $r = {SPH_R}$:"
        rf" $$V = \frac{{4}}{{3}}\pi ({SPH_R})^3 = \frac{{4}}{{3}}\pi (27)"
        rf" = 36\pi.$$"
        r" Omitting the $\frac{4}{3}$ gives $27\pi$, and using $4\pi r^3$"
        r" without the $\frac{1}{3}$ gives $108\pi$."
        r" The correct answer is **C**.",
        [f"Eq(Rational(4,3)*{SPH_R}**3, 36)", f"Eq(4*{SPH_R}**3, 108)"],
        fig=figure("sat-p6-m2e-q05",
                   "Sphere with a radius segment drawn from the center and "
                   "labeled 3")))

    # Q6 E advanced nonlinear_functions — evaluate a quadratic
    assert 6**2 - 4 * 6 == 12
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $g$ is defined by $g(x) = x^2 - 4x$. What is the value"
        r" of $g(6)$?",
        r"Substitute $x = 6$:"
        r" $$g(6) = 6^2 - 4(6) = 36 - 24 = 12.$$"
        r" Adding instead of subtracting gives 60, dropping the sign gives"
        r" $-12$, and evaluating only $4x$ gives 24."
        r" The correct answer is **B**.",
        ["Eq(6**2 - 4*6, 12)", "Eq(6**2 + 4*6, 60)"],
        12, {-12: "reversed the order of the subtraction",
             24: "evaluated only the 4x term",
             60: "added the two terms instead of subtracting"}, fmt=smart))

    # Q7 SPR E algebra linear_equations_two_var — x-intercept
    assert _solve(Eq(5 * x + 3 * 0, 45), x) == [9]
    qs.append(spr(
        "SAT-P6-M2E-Q07", M, 7, "algebra", "linear_equations_two_var", "easy",
        r"The graph of $5x + 3y = 45$ in the $xy$-plane crosses the $x$-axis at"
        r" the point $(a, 0)$. What is the value of $a$?",
        ["9"],
        r"Every point on the $x$-axis has $y = 0$. Substitute:"
        r" $$5x + 3(0) = 45 \;\Rightarrow\; 5x = 45 \;\Rightarrow\; x = 9.$$"
        r" Setting $x = 0$ instead would give the $y$-intercept, 15."
        r" The correct answer is **9**.",
        ["Eq(5*9 + 3*0, 45)", "Eq(45/5, 9)"]))

    # Q8 E geometry lines_angles_triangles — vertical angles
    assert _solve(Eq(4 * x, 68), x) == [17]
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q08", M, 8, "geometry_trig", "lines_angles_triangles", "easy",
        r"In the figure shown, two lines intersect. One angle measures"
        r" $(4x)^\circ$ and the angle vertically opposite it measures"
        r" $68^\circ$. What is the value of $x$?",
        r"Vertical angles — the pair formed on opposite sides of the"
        r" intersection — are equal, so"
        r" $$4x = 68 \;\Rightarrow\; x = 17.$$"
        r" Treating the two angles as supplementary instead gives"
        r" $4x = 112$, or 28; halving $68$ gives 34; and reporting the angle"
        r" itself gives 68."
        r" The correct answer is **A**.",
        ["Eq(4*17, 68)", "Eq(Rational(180 - 68, 4), 28)"],
        17, {28: "treated the angles as supplementary",
             34: "halved 68 instead of dividing by 4",
             68: "reported the angle measure rather than x"}, fmt=smart,
        fig=figure("sat-p6-m2e-q08",
                   "Two intersecting lines with one angle labeled 4x degrees "
                   "and the vertically opposite angle labeled 68 degrees")))

    # Q9 E algebra linear_functions — evaluate a cost model
    assert 45 + 28 * 5 == 185
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q09", M, 9, "algebra", "linear_functions", "easy",
        r"A plumber's charge, in dollars, for a job lasting $h$ hours is given"
        r" by $C(h) = 45 + 28h$. What is the charge for a job lasting $5$ hours?",
        r"Substitute $h = 5$:"
        r" $$C(5) = 45 + 28(5) = 45 + 140 = 185.$$"
        r" Forgetting the flat $\$45$ gives 140, using $h = 1$ gives 73, and"
        r" multiplying the whole expression by 5 gives 365."
        r" The correct answer is **C**.",
        ["Eq(45 + 28*5, 185)", "Eq(28*5, 140)"],
        185, {73: "evaluated the charge for 1 hour",
              140: "omitted the flat fee",
              365: "multiplied the flat fee by 5 as well"}, fmt=money))

    # Q10 E advanced nonlinear_functions — zeros from factored form
    assert sorted(_solve(Eq((x - 7) * (x + 2), 0), x)) == [-2, 7]
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q10", M, 10, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = (x - 7)(x + 2)$. What are the"
        r" zeros of $f$?",
        {"A": r"$-7$ and $2$", "B": r"$-7$ and $-2$", "C": r"$-2$ and $7$",
         "D": r"$2$ and $7$"}, "C",
        r"A product is zero exactly when one of its factors is zero:"
        r" $$x - 7 = 0 \;\Rightarrow\; x = 7, \qquad x + 2 = 0"
        r" \;\Rightarrow\; x = -2.$$"
        r" Each zero has the OPPOSITE sign of the number written inside its"
        r" factor — copying the signs straight across gives $7$ and $-2$"
        r" reversed."
        r" The correct answer is **C**.",
        ["Eq((7 - 7)*(7 + 2), 0)", "Eq((-2 - 7)*(-2 + 2), 0)"]))

    # Q11 E psda ratios_rates_units — rate scaled across time units
    assert Rational(15, 20) * 3600 == 2700
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q11", M, 11, "psda", "ratios_rates_units", "easy",
        r"A pump moves $15$ liters of water every $20$ seconds at a constant"
        r" rate. How many liters does the pump move in one hour?",
        r"Find the rate per second, then scale to the $3{,}600$ seconds in an"
        r" hour:"
        r" $$\frac{15}{20} = 0.75 \text{ liters per second},$$"
        r" $$0.75 \times 3600 = 2700 \text{ liters}.$$"
        r" Equivalently, 20 seconds goes into a minute 3 times, so the pump"
        r" moves $45$ liters per minute and $45 \times 60 = 2700$ per hour."
        r" Stopping at the per-minute figure gives 45, treating 15 as a"
        r" per-minute rate gives $15 \times 60 = 900$, and $15 \times 20$ gives"
        r" 300."
        r" The correct answer is **D**.",
        ["Eq(Rational(15,20)*3600, 2700)", "Eq(15*3, 45)", "Eq(45*60, 2700)"],
        2700, {45: "stopped at the per-minute rate",
               300: "multiplied 15 by 20",
               900: "treated 15 liters as a per-minute rate"}, fmt=smart))

    # Q12 SPR M advanced nonlinear_equations_systems — square-root both sides
    assert sorted(_solve(Eq((x - 4) ** 2, 49), x)) == [-3, 11]
    qs.append(spr(
        "SAT-P6-M2E-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"$$(x - 4)^2 = 49$$"
        r" What is the greatest value of $x$ that satisfies the equation above?",
        ["11"],
        r"Take the square root of both sides, keeping BOTH signs:"
        r" $$x - 4 = 7 \quad\text{or}\quad x - 4 = -7.$$"
        r" These give $x = 11$ and $x = -3$, so the greatest value is 11."
        r" Keeping only the positive root loses the solution $x = -3$; here that"
        r" happens not to change the answer, but on a question asking for the"
        r" least value it would."
        r" The correct answer is **11**.",
        ["Eq((11 - 4)**2, 49)", "Eq((-3 - 4)**2, 49)", "11 > -3"]))

    # Q13 M algebra linear_inequalities — solve and read the direction
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q13", M, 13, "algebra", "linear_inequalities", "medium",
        r"Which of the following gives all solutions of $3x + 5 \ge 23$?",
        {"A": r"$x \le 6$", "B": r"$x \ge 6$", "C": r"$x \ge 9$",
         "D": r"$x \ge \dfrac{28}{3}$"}, "B",
        r"Subtract 5 from both sides, then divide by 3:"
        r" $$3x \ge 18 \;\Rightarrow\; x \ge 6.$$"
        r" Dividing by a POSITIVE number leaves the inequality sign unchanged,"
        r" so the answer is $x \ge 6$, not $x \le 6$. Adding 5 instead of"
        r" subtracting gives $x \ge \frac{28}{3}$, and subtracting 5 from 23"
        r" but forgetting to divide gives $x \ge 18$."
        r" The correct answer is **B**.",
        ["Eq((23 - 5)/3, 6)", "3*6 + 5 >= 23", "3*5 + 5 < 23"]))

    # Q14 M advanced equivalent_expressions — negative exponents
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "medium",
        r"For $x \ne 0$, which of the following is equivalent to"
        r" $(2x^{-3})(6x^{5})$?",
        {"A": r"$8x^2$", "B": r"$12x^{-15}$", "C": r"$12x^2$",
         "D": r"$12x^{8}$"}, "C",
        r"Multiply the coefficients and ADD the exponents:"
        r" $$(2x^{-3})(6x^{5}) = (2 \cdot 6)\,x^{-3 + 5} = 12x^{2}.$$"
        r" Adding the coefficients gives $8$; multiplying the exponents gives"
        r" $x^{-15}$; and subtracting $-3$ instead of adding it gives $x^{8}$."
        r" The correct answer is **C**.",
        ["Eq(simplify(2*x**(-3) * 6*x**5 - 12*x**2), 0)", "Eq(-3 + 5, 2)"]))

    # Q15 SPR M advanced nonlinear_equations_systems — radical equation
    assert _solve(Eq(sqrt(x + 9), 5), x) == [16]
    qs.append(spr(
        "SAT-P6-M2E-Q15", M, 15, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"$$\sqrt{x + 9} = 5$$"
        r" What is the solution to the equation above?",
        ["16"],
        r"Square both sides to clear the radical:"
        r" $$x + 9 = 25 \;\Rightarrow\; x = 16.$$"
        r" Squaring can introduce extraneous solutions, so check:"
        r" $\sqrt{16 + 9} = \sqrt{25} = 5$. It works."
        r" The correct answer is **16**.",
        ["Eq(sqrt(16 + 9), 5)", "Eq(5**2 - 9, 16)"]))

    # Q16 M algebra systems_two_linear — two-priced-item word problem
    _c = _solve([Eq(x + y, 48), Eq(4 * x + 3 * y, 173)], [x, y], dict=True)[0]
    assert _c[x] == 29 and _c[y] == 19
    qs.append(mcq_numeric(
        "SAT-P6-M2E-Q16", M, 16, "algebra", "systems_two_linear", "medium",
        r"A café sold $48$ drinks one morning. Each coffee sold for $\$4$ and"
        r" each tea sold for $\$3$, and the total collected was $\$173$. How"
        r" many coffees did the café sell?",
        r"Let $c$ be the number of coffees and $t$ the number of teas:"
        r" $$c + t = 48, \qquad 4c + 3t = 173.$$"
        r" Substitute $t = 48 - c$ into the money equation:"
        r" $$4c + 3(48 - c) = 173 \;\Rightarrow\; c + 144 = 173"
        r" \;\Rightarrow\; c = 29.$$"
        r" Then $t = 19$, and the check holds:"
        r" $4(29) + 3(19) = 116 + 57 = 173$. Reporting the teas gives 19, and"
        r" the total drink count is 48."
        r" The correct answer is **B**.",
        ["Eq(29 + 19, 48)", "Eq(4*29 + 3*19, 173)"],
        29, {19: "reported the number of teas",
             44: "divided the total by 4 and rounded",
             48: "reported the total number of drinks"}, fmt=smart))

    # Q17 M advanced nonlinear_functions — x-intercepts from vertex form
    assert sorted(_solve(Eq((x - 3) ** 2 - 16, 0), x)) == [-1, 7]
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q17", M, 17, "advanced_math", "nonlinear_functions", "medium",
        r"The function $f$ is defined by $f(x) = (x - 3)^2 - 16$. At what values"
        r" of $x$ does the graph of $y = f(x)$ cross the $x$-axis?",
        {"A": r"$-1$ and $7$", "B": r"$-4$ and $4$", "C": r"$-7$ and $1$",
         "D": r"$3$ and $16$"}, "A",
        r"The graph crosses the $x$-axis where $f(x) = 0$:"
        r" $$(x - 3)^2 - 16 = 0 \;\Rightarrow\; (x - 3)^2 = 16"
        r" \;\Rightarrow\; x - 3 = \pm 4.$$"
        r" So $x = 3 + 4 = 7$ and $x = 3 - 4 = -1$. Solving only $(x-3)^2 = 16$"
        r" and stopping gives $\pm 4$; reading the constants straight off the"
        r" vertex form gives 3 and 16."
        r" The correct answer is **A**.",
        ["Eq((7 - 3)**2 - 16, 0)", "Eq((-1 - 3)**2 - 16, 0)"]))

    # Q18 M psda evaluating_claims_experiments — scope of a conclusion
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q18", M, 18, "psda", "evaluating_claims_experiments",
        "medium",
        r"A city planner selected $200$ residents of Darkhan at random and"
        r" surveyed them about a proposed bus route. Of those surveyed,"
        r" $62\%$ said they support the proposal. Which of the following is the"
        r" most appropriate conclusion?",
        {"A": r"The results cannot be generalized beyond the $200$ residents"
              r" surveyed.",
         "B": r"The results can be generalized to all residents of Darkhan.",
         "C": r"The results can be generalized to all residents of Mongolia.",
         "D": r"The proposed bus route caused residents to support public"
              r" transit."}, "B",
        r"A conclusion may be generalized to exactly the population the sample"
        r" was drawn from AT RANDOM. Here the random selection was made from"
        r" residents of Darkhan, so the results generalize to that city —"
        r" random selection is what makes the sample representative, and a"
        r" sample of 200 is ample."
        r" They do not extend to all of Mongolia, because residents of other"
        r" places had no chance of being selected. And a survey is an"
        r" OBSERVATIONAL study, not an experiment with random ASSIGNMENT to"
        r" treatment groups, so it cannot establish that anything was caused."
        r" The correct answer is **B**.",
        ["Eq(Rational(62,100)*200, 124)", "200 > 30"]))

    # Q19 SPR M algebra one_var — distribute on both sides
    assert _solve(Eq(4 * (2 * x - 1), 3 * x + 26), x) == [6]
    qs.append(spr(
        "SAT-P6-M2E-Q19", M, 19, "algebra", "linear_equations_one_var", "medium",
        r"$$4(2x - 1) = 3x + 26$$"
        r" What is the solution to the equation above?",
        ["6"],
        r"Distribute on the left, then gather like terms:"
        r" $$8x - 4 = 3x + 26 \;\Rightarrow\; 5x = 30 \;\Rightarrow\; x = 6.$$"
        r" Check: $4(2 \cdot 6 - 1) = 4(11) = 44$ and $3(6) + 26 = 44$."
        r" The correct answer is **6**.",
        ["Eq(4*(2*6 - 1), 3*6 + 26)", "Eq(4*(2*6 - 1), 44)"]))

    # Q20 H geometry circles — arc length from a given area
    assert Rational(60, 360) * 14 == Rational(7, 3)
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"A circle has an area of $49\pi$. In this circle, a central angle of"
        r" $60^\circ$ subtends an arc, as shown. What is the length of that arc?",
        {"A": r"$\dfrac{7\pi}{6}$", "B": r"$\dfrac{7\pi}{3}$",
         "C": r"$\dfrac{14\pi}{3}$", "D": r"$7\pi$"}, "B",
        r"Work back from the area to the radius:"
        r" $$\pi r^2 = 49\pi \;\Rightarrow\; r = 7.$$"
        r" The full circumference is $2\pi r = 14\pi$, and a $60^\circ$ angle"
        r" cuts off $\frac{60}{360} = \frac{1}{6}$ of it:"
        r" $$\text{arc} = \frac{1}{6}(14\pi) = \frac{7\pi}{3}.$$"
        r" Using the radius instead of the circumference gives"
        r" $\frac{7\pi}{6}$, and taking $\frac{1}{3}$ of the circumference"
        r" gives $\frac{14\pi}{3}$."
        r" The correct answer is **B**.",
        ["Eq(sqrt(49), 7)", "Eq(2*7, 14)",
         "Eq(Rational(60,360)*14, Rational(7,3))"],
        fig=figure("sat-p6-m2e-q20",
                   "Circle with center O, a radius labeled 7, and a central "
                   "angle of 60 degrees with its subtended arc drawn heavy")))

    # Q21 M advanced nonlinear_functions — choose the exponential model
    qs.append(mcq_listed(
        "SAT-P6-M2E-Q21", M, 21, "advanced_math", "nonlinear_functions", "medium",
        r"An investment of $\$5{,}000$ increases in value by $4\%$ each year."
        r" Which function gives the value, in dollars, of the investment after"
        r" $t$ years?",
        {"A": r"$V(t) = 5000(0.04)^t$", "B": r"$V(t) = 5000(1.04)^t$",
         "C": r"$V(t) = 5000(1.4)^t$", "D": r"$V(t) = 5000(4)^t$"}, "B",
        r"Growing by $4\%$ means each year's value is the previous value plus"
        r" $4\%$ of it — that is, multiplied by"
        r" $$1 + 0.04 = 1.04.$$"
        r" After $t$ years the factor has been applied $t$ times, giving"
        r" $V(t) = 5000(1.04)^t$. A base of $0.04$ would shrink the investment"
        r" to $4\%$ of its value each year, $1.4$ would mean $40\%$ growth, and"
        r" a base of 4 would quadruple it annually."
        r" The correct answer is **B**.",
        ["Eq(1 + Rational(4,100), Rational(104,100))",
         "Eq(5000*Rational(104,100), 5200)"]))

    # Q22 SPR H algebra systems_two_linear — parameter for INFINITELY MANY
    assert Rational(6, 2) == 3 and Rational(27, 9) == 3
    qs.append(spr(
        "SAT-P6-M2E-Q22", M, 22, "algebra", "systems_two_linear", "hard",
        r"$$2x + 5y = 9$$ $$6x + ay = 27$$"
        r" In the system of equations above, $a$ is a constant. For what value"
        r" of $a$ does the system have infinitely many solutions?",
        ["15"],
        r"A system has infinitely many solutions exactly when the two equations"
        r" describe the SAME line — every coefficient and the constant must"
        r" scale by one common factor. Comparing the $x$-coefficients gives the"
        r" factor:"
        r" $$\frac{6}{2} = 3.$$"
        r" Applying it to the $y$-coefficient gives $a = 3 \cdot 5 = 15$, and"
        r" the constants agree with it too: $3 \cdot 9 = 27$. So multiplying"
        r" the first equation by 3 reproduces the second exactly."
        r" The correct answer is **15**.",
        ["Eq(Rational(6,2), 3)", "Eq(3*5, 15)", "Eq(3*9, 27)",
         "Eq(simplify(3*(2*x + 5*y)), 6*x + 15*y)"]))

    return qs


# ─── Module 2, harder variant (2E / 7M / 13H) ─────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E algebra one_var
    assert _solve(Eq(9 * x - 4, 5 * x + 16), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $9x - 4 = 5x + 16$, what is the value of $x$?",
        r"Gather the variable terms and the constants on opposite sides:"
        r" $$9x - 5x = 16 + 4 \;\Rightarrow\; 4x = 20 \;\Rightarrow\; x = 5.$$"
        r" Subtracting the constants instead of adding gives $4x = 12$, or 3;"
        r" stopping at $4x = 20$ gives 20."
        r" The correct answer is **C**.",
        ["Eq(9*5 - 4, 5*5 + 16)", "Eq((16 + 4)/(9 - 5), 5)"],
        5, {1: "combined the constants and coefficients incorrectly",
            3: "subtracted 4 from 16 instead of adding",
            20: "stopped at 4x = 20"}, fmt=smart))

    # Q2 E advanced equivalent_expressions
    assert expand((x + 8) * (x - 3)) == x**2 + 5 * x - 24
    qs.append(mcq_listed(
        "SAT-P6-M2H-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $(x + 8)(x - 3)$?",
        {"A": r"$x^2 - 5x - 24$", "B": r"$x^2 + 5x - 24$",
         "C": r"$x^2 + 5x + 24$", "D": r"$x^2 + 11x - 24$"}, "B",
        r"Expand term by term:"
        r" $$(x + 8)(x - 3) = x^2 - 3x + 8x - 24 = x^2 + 5x - 24.$$"
        r" The middle coefficient is $8 - 3 = 5$; adding the two numbers gives"
        r" 11, and reversing their roles gives $-5$."
        r" The correct answer is **B**.",
        ["Eq(expand((x + 8)*(x - 3)), x**2 + 5*x - 24)", "Eq(8 - 3, 5)"]))

    # Q3 SPR M algebra linear_equations_two_var — y-intercept from two points
    assert Rational(16 - 4, 5 - 1) == 3 and 4 - 3 * 1 == 1
    qs.append(spr(
        "SAT-P6-M2H-Q03", M, 3, "algebra", "linear_equations_two_var", "medium",
        r"A line in the $xy$-plane passes through the points $(1, 4)$ and"
        r" $(5, 16)$. What is the $y$-coordinate of the point where the line"
        r" crosses the $y$-axis?",
        ["1"],
        r"Find the slope first:"
        r" $$m = \frac{16 - 4}{5 - 1} = \frac{12}{4} = 3.$$"
        r" Now use one point in $y = mx + b$:"
        r" $$4 = 3(1) + b \;\Rightarrow\; b = 1.$$"
        r" Check with the other point: $3(5) + 1 = 16$."
        r" The correct answer is **1**.",
        ["Eq(Rational(16 - 4, 5 - 1), 3)", "Eq(3*1 + 1, 4)",
         "Eq(3*5 + 1, 16)"]))

    # Q4 M geometry lines_angles_triangles — parallelogram adjacent angles
    assert _solve(Eq((3 * x + 10) + 2 * x, 180), x) == [34]
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q04", M, 4, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In the parallelogram shown, one interior angle measures"
        r" $(3x + 10)^\circ$ and an adjacent interior angle measures"
        r" $(2x)^\circ$. What is the value of $x$?",
        r"Adjacent angles of a parallelogram lie between the same pair of"
        r" parallel sides, so they are supplementary:"
        r" $$(3x + 10) + 2x = 180 \;\Rightarrow\; 5x + 10 = 180"
        r" \;\Rightarrow\; 5x = 170 \;\Rightarrow\; x = 34.$$"
        r" Treating the angles as EQUAL (true only for OPPOSITE angles of a"
        r" parallelogram) gives $3x + 10 = 2x$, or $x = -10$; adding 10 instead"
        r" of subtracting gives $5x = 190$, or 38; and doubling the answer"
        r" gives 68."
        r" The correct answer is **B**.",
        ["Eq(3*34 + 10 + 2*34, 180)", "Eq(Rational(180 - 10, 5), 34)"],
        34, {30: "solved 5x + 10 = 160",
             38: "added 10 to 180 instead of subtracting",
             68: "reported the measure of the second angle"}, fmt=smart,
        fig=figure("sat-p6-m2h-q04",
                   "Parallelogram with the bottom-left interior angle labeled "
                   "(3x + 10) degrees and the adjacent bottom-right interior "
                   "angle labeled (2x) degrees")))

    # Q5 M psda probability_conditional — two-way table, conditional
    TW = {"u30": [18, 12, 15], "o30": [10, 26, 9]}
    assert sum(TW["u30"]) == 45 and sum(TW["o30"]) == 45
    qs.append(mcq_listed(
        "SAT-P6-M2H-Q05", M, 5, "psda", "probability_conditional", "medium",
        r"The two-way table shows how $90$ surveyed commuters travel to work,"
        r" by age group. If one of the commuters who are $30$ or older is"
        r" selected at random, what is the probability that the person travels"
        r" by car?",
        {"A": r"$\dfrac{26}{90}$", "B": r"$\dfrac{38}{90}$",
         "C": r"$\dfrac{26}{45}$", "D": r"$\dfrac{26}{38}$"}, "C",
        r"The condition ''30 or older'' restricts the sample space to that ROW"
        r" only. That row totals"
        r" $$10 + 26 + 9 = 45$$"
        r" commuters, of whom 26 travel by car, so the probability is"
        r" $$\frac{26}{45}.$$"
        r" Dividing by the grand total 90 ignores the condition; dividing by"
        r" the car COLUMN total 38 answers the reversed question (given that a"
        r" commuter travels by car, the probability the person is 30 or older)."
        r" The correct answer is **C**.",
        ["Eq(10 + 26 + 9, 45)", "Eq(18 + 12 + 15, 45)",
         "Eq(12 + 26, 38)", "Rational(26,45) > Rational(26,90)"],
        fig=figure("sat-p6-m2h-q05",
                   "Two-way table of commuters by age group (under 30, 30 or "
                   "older) against travel method (bus, car, bicycle) with row "
                   "and column totals")))

    # Q6 M advanced nonlinear_functions — minimum of a quadratic
    assert 2 * (-2) ** 2 + 8 * (-2) + 1 == -7
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q06", M, 6, "advanced_math", "nonlinear_functions", "medium",
        r"What is the minimum value of the function"
        r" $f(x) = 2x^2 + 8x + 1$?",
        r"The parabola opens upward ($a = 2 > 0$), so its minimum occurs at the"
        r" vertex, where"
        r" $$x = -\frac{b}{2a} = -\frac{8}{2(2)} = -2.$$"
        r" Evaluate there:"
        r" $$f(-2) = 2(4) + 8(-2) + 1 = 8 - 16 + 1 = -7.$$"
        r" Reporting the $x$-coordinate of the vertex gives $-2$, and using"
        r" $f(0)$ gives 1 — the $y$-intercept, not the minimum."
        r" The correct answer is **A**.",
        ["Eq(-Rational(8, 2*2), -2)", "Eq(2*(-2)**2 + 8*(-2) + 1, -7)",
         "Eq(2*0**2 + 8*0 + 1, 1)"],
        -7, {-2: "reported the x-coordinate of the vertex",
             1: "evaluated f(0) instead of the vertex",
             9: "made a sign error evaluating the vertex"}, fmt=smart))

    # Q7 SPR M advanced nonlinear_equations_systems — absolute value
    # sympy cannot solve Abs(...) over a plain symbol, so check both branches
    # directly — the two cases ARE the definition of the absolute value.
    assert abs(2 * 7 - 9) == 5 and abs(2 * 2 - 9) == 5 and 7 + 2 == 9
    qs.append(spr(
        "SAT-P6-M2H-Q07", M, 7, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"$$|2x - 9| = 5$$"
        r" The equation above has two solutions. What is the sum of those"
        r" solutions?",
        ["9"],
        r"An absolute value equals 5 when the inside is $5$ or $-5$:"
        r" $$2x - 9 = 5 \;\Rightarrow\; x = 7, \qquad"
        r" 2x - 9 = -5 \;\Rightarrow\; x = 2.$$"
        r" Their sum is $7 + 2 = 9$. Solving only the positive case would miss"
        r" $x = 2$ entirely."
        r" The correct answer is **9**.",
        ["Eq(Abs(2*7 - 9), 5)", "Eq(Abs(2*2 - 9), 5)", "Eq(7 + 2, 9)"]))

    # Q8 M algebra linear_inequalities — point satisfying a SYSTEM
    for _px, _py, _ok in [(-1, -6, False), (1, 2, True), (4, 6, False),
                          (5, 0, False)]:
        assert ((_py > 2 * _px - 3) and (_py <= -_px + 6)) is _ok
    qs.append(mcq_listed(
        "SAT-P6-M2H-Q08", M, 8, "algebra", "linear_inequalities", "medium",
        r"$$y > 2x - 3$$ $$y \le -x + 6$$"
        r" Which of the following ordered pairs $(x, y)$ satisfies both"
        r" inequalities above?",
        {"A": r"$(-1, -6)$", "B": r"$(1, 2)$", "C": r"$(4, 6)$",
         "D": r"$(5, 0)$"}, "B",
        r"A point in the solution region must satisfy BOTH inequalities, so"
        r" test each pair in both."
        r" For $(1, 2)$: $2 > 2(1) - 3 = -1$ is true, and"
        r" $2 \le -(1) + 6 = 5$ is true — both hold."
        r" For $(-1, -6)$ the first fails, since $-6 > -5$ is false."
        r" For $(4, 6)$ the second fails, since $6 \le 2$ is false."
        r" For $(5, 0)$ the first fails, since $0 > 7$ is false."
        r" The correct answer is **B**.",
        ["(2 > 2*1 - 3) & (2 <= -1 + 6)", "Not(-6 > 2*(-1) - 3)",
         "Not(6 <= -4 + 6)", "Not(0 > 2*5 - 3)"]))

    # Q9 M geometry area_volume — volume scaling under a doubled radius
    assert Rational(4, 3) * 2**3 / Rational(4, 3) == 8
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q09", M, 9, "geometry_trig", "area_volume", "medium",
        r"The radius of a sphere is doubled. The volume of the new sphere is"
        r" how many times the volume of the original sphere?",
        r"Volume depends on the CUBE of the radius,"
        r" $V = \frac{4}{3}\pi r^3$, so replacing $r$ with $2r$ gives"
        r" $$\frac{4}{3}\pi (2r)^3 = \frac{4}{3}\pi \cdot 8r^3"
        r" = 8\left(\frac{4}{3}\pi r^3\right).$$"
        r" The volume is multiplied by $2^3 = 8$. Answering 2 uses the scale"
        r" factor itself, 4 squares it as if volume scaled like area, and 6"
        r" multiplies the factor by 3 instead of cubing it."
        r" The correct answer is **D**.",
        ["Eq(2**3, 8)", "Eq(Rational(4,3)*(2*3)**3, 8*Rational(4,3)*3**3)"],
        8, {2: "used the scale factor itself",
            4: "squared the scale factor as if scaling an area",
            6: "multiplied the scale factor by 3"}, fmt=smart))

    # Q10 H algebra systems_two_linear — age relationships
    _a = _solve([Eq(x - 5, 3 * (y - 5)), Eq(x + 4, 2 * (y + 4))],
                [x, y], dict=True)[0]
    assert _a[x] == 32 and _a[y] == 14
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q10", M, 10, "algebra", "systems_two_linear", "hard",
        r"Five years ago, Bat was three times as old as Saran. In four years,"
        r" Bat will be twice as old as Saran. How old is Bat now?",
        r"Let $b$ and $s$ be their current ages. Shift BOTH ages by the same"
        r" number of years in each sentence:"
        r" $$b - 5 = 3(s - 5), \qquad b + 4 = 2(s + 4).$$"
        r" The first gives $b = 3s - 10$. Substituting into the second:"
        r" $$3s - 10 + 4 = 2s + 8 \;\Rightarrow\; s = 14,$$"
        r" so $b = 3(14) - 10 = 32$."
        r" Check: five years ago $27 = 3 \cdot 9$, and in four years"
        r" $36 = 2 \cdot 18$. Reporting Saran's age gives 14, Bat's age five"
        r" years ago gives 27, and his age in four years gives 36."
        r" The correct answer is **C**.",
        ["Eq(32 - 5, 3*(14 - 5))", "Eq(32 + 4, 2*(14 + 4))"],
        32, {14: "reported Saran's current age",
             27: "reported Bat's age five years ago",
             36: "reported Bat's age in four years"}, fmt=smart))

    # Q11 H advanced nonlinear_functions — composition equation
    assert _solve(Eq(2 * (x**2 - 3) + 5, 19), x) == [-sqrt(10), sqrt(10)]
    qs.append(mcq_listed(
        "SAT-P6-M2H-Q11", M, 11, "advanced_math", "nonlinear_functions", "hard",
        r"The functions $f$ and $g$ are defined by $f(x) = 2x + 5$ and"
        r" $g(x) = x^2 - 3$. If $f(g(a)) = 19$, what are all possible values"
        r" of $a$?",
        {"A": r"$\pm\sqrt{7}$", "B": r"$\pm\sqrt{10}$", "C": r"$\pm\sqrt{13}$",
         "D": r"$\pm 10$"}, "B",
        r"Apply $f$ to the OUTPUT of $g$ — substitute $g(a)$ into $f$:"
        r" $$f(g(a)) = 2(a^2 - 3) + 5 = 2a^2 - 1.$$"
        r" Set that equal to 19:"
        r" $$2a^2 - 1 = 19 \;\Rightarrow\; 2a^2 = 20 \;\Rightarrow\; a^2 = 10,$$"
        r" so $a = \pm\sqrt{10}$. Both signs work because $a$ is squared."
        r" Forgetting to distribute the 2 over $-3$ gives $a^2 = 7$; composing"
        r" in the other order, $g(f(a))$, leads elsewhere entirely."
        r" The correct answer is **B**.",
        ["Eq(expand(2*(x**2 - 3) + 5), 2*x**2 - 1)",
         "Eq(2*(sqrt(10)**2 - 3) + 5, 19)",
         "Eq(2*((-sqrt(10))**2 - 3) + 5, 19)"]))

    # Q12 SPR H advanced nonlinear_equations_systems — discriminant condition
    assert _solve(Eq(12**2 - 4 * 2 * x, 0), x) == [18]
    qs.append(spr(
        "SAT-P6-M2H-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"$$2x^2 - 12x + k = 0$$"
        r" In the equation above, $k$ is a constant. If the equation has exactly"
        r" one real solution, what is the value of $k$?",
        ["18"],
        r"A quadratic $ax^2 + bx + c = 0$ has exactly one real solution when its"
        r" discriminant is zero. Here $a = 2$, $b = -12$, and $c = k$:"
        r" $$b^2 - 4ac = (-12)^2 - 4(2)(k) = 144 - 8k = 0,$$"
        r" so $k = 18$."
        r" Check by factoring: $2x^2 - 12x + 18 = 2(x - 3)^2$, which indeed has"
        r" the single (repeated) solution $x = 3$. Using $a = 1$ instead of 2"
        r" would give $k = 36$."
        r" The correct answer is **18**.",
        ["Eq((-12)**2 - 4*2*18, 0)",
         "Eq(expand(2*(x - 3)**2), 2*x**2 - 12*x + 18)"]))

    # Q13 H algebra linear_functions — arithmetic sequence as a linear model
    assert Rational(64 - 8, 14) == 4 and 8 + 29 * 4 == 124
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q13", M, 13, "algebra", "linear_functions", "hard",
        r"The first term of an arithmetic sequence is $8$, and the $15$th term"
        r" is $64$. What is the $30$th term of the sequence?",
        r"An arithmetic sequence is a linear function of the term number. Going"
        r" from term 1 to term 15 takes $15 - 1 = 14$ steps, so the common"
        r" difference is"
        r" $$d = \frac{64 - 8}{14} = 4.$$"
        r" Reaching term 30 from term 1 takes $30 - 1 = 29$ steps:"
        r" $$a_{30} = 8 + 29(4) = 8 + 116 = 124.$$"
        r" Counting 30 steps instead of 29 gives 128 — the classic off-by-one"
        r" here — and dividing by 15 rather than 14 mis-sizes $d$."
        r" The correct answer is **C**.",
        ["Eq(Rational(64 - 8, 15 - 1), 4)", "Eq(8 + (15 - 1)*4, 64)",
         "Eq(8 + (30 - 1)*4, 124)"],
        124, {68: "added one common difference to the 15th term",
              116: "forgot to add the first term",
              128: "used 30 steps instead of 29"}, fmt=smart))

    # Q14 H advanced equivalent_expressions — sum of two rational expressions
    assert simplify(1 / x + 1 / (x + 2) - (2 * x + 2) / (x * (x + 2))) == 0
    qs.append(mcq_listed(
        "SAT-P6-M2H-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "hard",
        r"For $x \ne 0$ and $x \ne -2$, which of the following is equivalent to"
        r" $\dfrac{1}{x} + \dfrac{1}{x + 2}$?",
        {"A": r"$\dfrac{1}{2x + 2}$", "B": r"$\dfrac{2}{2x + 2}$",
         "C": r"$\dfrac{2x + 2}{x(x + 2)}$", "D": r"$\dfrac{2x + 2}{x + 2}$"},
        "C",
        r"Fractions can only be added over a COMMON denominator; here that is"
        r" $x(x + 2)$. Rewrite each term:"
        r" $$\frac{1}{x} = \frac{x + 2}{x(x + 2)}, \qquad"
        r" \frac{1}{x + 2} = \frac{x}{x(x + 2)}.$$"
        r" Now add the numerators:"
        r" $$\frac{(x + 2) + x}{x(x + 2)} = \frac{2x + 2}{x(x + 2)}.$$"
        r" Adding the denominators instead — the most common error — would give"
        r" $\frac{1}{2x + 2}$, which fails even a quick check at $x = 1$:"
        r" the original is $1 + \frac{1}{3} = \frac{4}{3}$, while"
        r" $\frac{1}{2x+2} = \frac{1}{4}$."
        r" The correct answer is **C**.",
        ["Eq(simplify(1/x + 1/(x + 2) - (2*x + 2)/(x*(x + 2))), 0)",
         "Eq(1/Integer(1) + 1/Integer(3), Rational(4,3))",
         "Ne(Rational(4,3), Rational(1,4))"]))

    # Q15 SPR H psda one_var_data — replacing a value to move the mean
    assert 9 * 21 == 189 and 9 * 23 == 207 and 13 + (207 - 189) == 31
    qs.append(spr(
        "SAT-P6-M2H-Q15", M, 15, "psda", "one_var_data", "hard",
        r"The mean of a list of $9$ numbers is $21$. One of the numbers, $13$,"
        r" is replaced by a different number, and the mean of the new list of"
        r" $9$ numbers is $23$. What is the new number?",
        ["31"],
        r"Work with totals, since the mean is the total divided by the count."
        r" The original total is"
        r" $$9 \times 21 = 189,$$"
        r" and the new total is"
        r" $$9 \times 23 = 207.$$"
        r" Only one number changed, so the total rose by"
        r" $207 - 189 = 18$, and the new number is that much larger than the"
        r" one it replaced:"
        r" $$13 + 18 = 31.$$"
        r" Adding the change in the MEAN, $23 - 21 = 2$, to 13 gives 15 — that"
        r" ignores that one replacement must shift the whole total."
        r" The correct answer is **31**.",
        ["Eq(9*21, 189)", "Eq(9*23, 207)", "Eq(207 - 189, 18)",
         "Eq(13 + 18, 31)"]))

    # Q16 H algebra linear_inequalities — two constraints, which one binds
    assert (1500 - 25 * 30) / 20 == 37.5 and 60 - 25 == 35
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q16", M, 16, "algebra", "linear_inequalities", "hard",
        r"A shipping pallet can hold a total weight of at most $1{,}500$"
        r" kilograms and at most $60$ boxes. Each type A box weighs $30$"
        r" kilograms and each type B box weighs $20$ kilograms. If the pallet"
        r" already holds $25$ type A boxes, what is the greatest number of"
        r" type B boxes it can also hold?",
        r"Both limits must hold, so write an inequality for each. The 25 type A"
        r" boxes weigh $25(30) = 750$ kilograms, so the weight limit gives"
        r" $$750 + 20b \le 1500 \;\Rightarrow\; 20b \le 750"
        r" \;\Rightarrow\; b \le 37.5.$$"
        r" The box-count limit gives"
        r" $$25 + b \le 60 \;\Rightarrow\; b \le 35.$$"
        r" A value of $b$ must satisfy BOTH, so the binding limit is the"
        r" smaller one: $b \le 35$, and the greatest whole number of type B"
        r" boxes is 35."
        r" Using only the weight limit gives 37 after rounding down, and"
        r" ignoring the type A boxes already present gives 60."
        r" The correct answer is **A**.",
        ["Eq(25*30, 750)", "Eq(750 + 20*35, 1450)", "750 + 20*35 <= 1500",
         "Eq(25 + 35, 60)", "750 + 20*38 > 1500"],
        35, {37: "used only the weight limit",
             50: "divided 1500 by 30",
             60: "ignored the 25 type A boxes already on the pallet"},
        fmt=smart))

    # Q17 H advanced nonlinear_equations_systems — quadratic in disguise
    assert sorted(_solve(Eq(x**4 - 13 * x**2 + 36, 0), x)) == [-3, -2, 2, 3]
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q17", M, 17, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"What is the greatest solution to $x^4 - 13x^2 + 36 = 0$?",
        r"The equation is a quadratic in $x^2$. Writing $u = x^2$:"
        r" $$u^2 - 13u + 36 = 0 \;\Rightarrow\; (u - 4)(u - 9) = 0,$$"
        r" so $x^2 = 4$ or $x^2 = 9$. Each gives two values:"
        r" $$x = \pm 2, \qquad x = \pm 3,$$"
        r" and the greatest of the four is 3."
        r" Stopping at $u = 9$ and reporting it treats $x^2$ as $x$, giving 9;"
        r" reporting $u = 4$ the same way gives 4."
        r" The correct answer is **B**.",
        ["Eq(expand((x**2 - 4)*(x**2 - 9)), x**4 - 13*x**2 + 36)",
         "Eq(3**4 - 13*3**2 + 36, 0)", "Eq(2**4 - 13*2**2 + 36, 0)"],
        3, {2: "reported the smaller positive solution",
            4: "reported the value of x squared",
            9: "reported the larger value of x squared"}, fmt=smart))

    # Q18 H geometry circles — Thales: angle in a semicircle is right
    THA_D, THA_AC = 26, 10
    assert THA_AC**2 + 24**2 == THA_D**2
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q18", M, 18, "geometry_trig", "circles", "hard",
        rf"In the figure shown, points $A$, $B$, and $C$ lie on a circle, and"
        rf" $\overline{{AB}}$ is a diameter of length ${THA_D}$. If"
        rf" $AC = {THA_AC}$, what is the length of $\overline{{BC}}$?",
        rf"An angle inscribed in a semicircle is a right angle, so because"
        rf" $\overline{{AB}}$ is a diameter, the angle at $C$ measures"
        rf" $90^\circ$. Triangle $ABC$ is therefore a right triangle with"
        rf" hypotenuse $AB = {THA_D}$:"
        rf" $$BC^2 = {THA_D}^2 - {THA_AC}^2 = 676 - 100 = 576,$$"
        rf" so $BC = 24$."
        r" Subtracting the lengths directly gives 16, adding them gives 36,"
        r" and adding the squares treats $BC$ as the hypotenuse, which the"
        r" right angle at $C$ rules out."
        r" The correct answer is **B**.",
        [f"Eq({THA_D}**2 - {THA_AC}**2, 576)", "Eq(sqrt(576), 24)",
         f"Eq({THA_AC}**2 + 24**2, {THA_D}**2)"],
        24, {16: "subtracted the two given lengths",
             28: "added the squares instead of subtracting",
             36: "added the two given lengths"}, fmt=smart,
        fig=figure("sat-p6-m2h-q18",
                   "Circle with diameter AB of length 26, point C on the "
                   "circle, chord AC labeled 10, and a right-angle mark at C")))

    # Q19 SPR H advanced nonlinear_functions — exponential with unknown base
    assert 12 * 2**3 == 96 and 12 * 2**5 == 384
    qs.append(spr(
        "SAT-P6-M2H-Q19", M, 19, "advanced_math", "nonlinear_functions", "hard",
        r"The function $f$ is defined by $f(t) = a \cdot b^{\,t}$, where $a$ and"
        r" $b$ are positive constants. If $f(0) = 12$ and $f(3) = 96$, what is"
        r" the value of $f(5)$?",
        ["384"],
        r"At $t = 0$ the power is $b^0 = 1$, so $f(0) = a$ gives"
        r" $$a = 12.$$"
        r" Now use $f(3)$ to find the base:"
        r" $$12b^3 = 96 \;\Rightarrow\; b^3 = 8 \;\Rightarrow\; b = 2.$$"
        r" The model is $f(t) = 12 \cdot 2^{\,t}$, so"
        r" $$f(5) = 12 \cdot 2^5 = 12 \cdot 32 = 384.$$"
        r" Growth is multiplicative, not additive: adding the increase from"
        r" $f(0)$ to $f(3)$ twice more would wrongly suggest 264."
        r" The correct answer is **384**.",
        ["Eq(12*2**0, 12)", "Eq(12*2**3, 96)", "Eq(12*2**5, 384)"]))

    # Q20 H psda percentages — increase then decrease, working backwards
    assert Rational(125, 100) * Rational(80, 100) == 1
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q20", M, 20, "psda", "percentages", "hard",
        r"The price of a bicycle was increased by $25\%$, and the new price was"
        r" then decreased by $20\%$. If the final price is $\$60$, what was the"
        r" original price?",
        r"Percent changes multiply. Increasing by $25\%$ multiplies by $1.25$,"
        r" and decreasing by $20\%$ multiplies by $0.80$, so the overall factor"
        r" is"
        r" $$1.25 \times 0.80 = 1.$$"
        r" The two changes exactly undo each other, so the final price equals"
        r" the original price: $\$60$."
        r" This is the trap in the question — the percentages are taken of"
        r" DIFFERENT bases, and $-20\%$ of the larger new price cancels"
        r" $+25\%$ of the smaller original. Applying only one of the changes"
        r" gives $60 \times 0.8 = 48$ or $60 \times 1.25 = 75$."
        r" The correct answer is **B**.",
        ["Eq(Rational(125,100)*Rational(80,100), 1)",
         "Eq(60*Rational(125,100)*Rational(80,100), 60)"],
        60, {48: "applied only the 20 percent decrease",
             Rational(125, 2): "divided by 0.96 instead of by 1",
             75: "applied only the 25 percent increase"}, fmt=money))

    # Q21 H algebra linear_equations_two_var — perpendicular through the
    # x-intercept
    assert _solve(Eq(3 * x - 4 * 0, 24), x) == [8]
    assert Rational(-4, 3) * (0 - 8) == Rational(32, 3)
    qs.append(mcq_numeric(
        "SAT-P6-M2H-Q21", M, 21, "algebra", "linear_equations_two_var", "hard",
        r"Line $\ell$ has equation $3x - 4y = 24$. Line $m$ is perpendicular to"
        r" line $\ell$ and passes through the $x$-intercept of line $\ell$."
        r" What is the $y$-coordinate of the $y$-intercept of line $m$?",
        r"First find where $\ell$ crosses the $x$-axis by setting $y = 0$:"
        r" $$3x = 24 \;\Rightarrow\; x = 8,$$"
        r" so line $m$ passes through $(8, 0)$."
        r" Next, put $\ell$ in slope-intercept form:"
        r" $$-4y = -3x + 24 \;\Rightarrow\; y = \frac{3}{4}x - 6,$$"
        r" so $\ell$ has slope $\frac{3}{4}$ and $m$ has the negative reciprocal"
        r" slope $-\frac{4}{3}$. Using the point $(8, 0)$:"
        r" $$y = -\frac{4}{3}(x - 8),$$"
        r" and at $x = 0$ this gives $y = \frac{32}{3}$."
        r" Reporting $\ell$'s own $y$-intercept gives $-6$, and reusing $\ell$'s"
        r" slope instead of the perpendicular one gives $-6$ again by a"
        r" different route; the $x$-intercept itself is 8."
        r" The correct answer is **D**.",
        ["Eq(3*8 - 4*0, 24)", "Eq(Rational(3,4)*Rational(-4,3), -1)",
         "Eq(Rational(-4,3)*(0 - 8), Rational(32,3))"],
        Rational(32, 3), {-6: "reported the y-intercept of line l",
                          6: "dropped the sign of line l's y-intercept",
                          8: "reported the x-intercept"}, fmt=smart))

    # Q22 SPR H algebra systems_two_linear — parameter for infinitely many
    assert Rational(9, 3) == 3 and Rational(21, 7) == 3 and 3 * (-2) == -6
    qs.append(spr(
        "SAT-P6-M2H-Q22", M, 22, "algebra", "systems_two_linear", "hard",
        r"$$3x - 2y = 7$$ $$9x + by = 21$$"
        r" In the system of equations above, $b$ is a constant. For what value"
        r" of $b$ does the system have infinitely many solutions?",
        ["-6"],
        r"Infinitely many solutions means the two equations describe the same"
        r" line, so one is a constant multiple of the other. The"
        r" $x$-coefficients give the multiplier:"
        r" $$\frac{9}{3} = 3.$$"
        r" The constants confirm it: $\frac{21}{7} = 3$. Applying the same"
        r" factor to the $y$-coefficient:"
        r" $$b = 3(-2) = -6.$$"
        r" Multiplying the first equation by 3 does reproduce the second:"
        r" $9x - 6y = 21$. Dropping the minus sign gives $+6$, which would make"
        r" the lines intersect at a single point instead."
        r" The correct answer is **-6**.",
        ["Eq(Rational(9,3), 3)", "Eq(Rational(21,7), 3)", "Eq(3*(-2), -6)",
         "Eq(simplify(3*(3*x - 2*y)), 9*x - 6*y)"]))

    return qs


# ─── blueprint conformance + emit ─────────────────────────────────────

M1_SPEC = dict(diff_mix={"easy": 8, "medium": 9, "hard": 5},
               spr_slots={4, 9, 14, 18, 21},
               domains={"algebra": 7, "advanced_math": 7, "psda": 4,
                        "geometry_trig": 4})
M2_DOMAINS = {"algebra": 8, "advanced_math": 8, "psda": 3, "geometry_trig": 3}
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
    write_test(REPO / "data" / "sat" / "sat-practice-6.json",
               {"testId": "sat-practice-6",
                "label": "SAT Math Practice Test 6",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
