#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 5 (data/sat/sat-practice-5.json).

Built on scripts/test-builders/satbuild.py — only stems, parameters,
computed answers, named distractor error models, verify[] strings, and
solutions live here. Archetypes are fresh versus tests 1-4; the hard
tier is calibrated to real Bluebook hard questions: nonlinear systems by
substitution, quadratics with a required discriminant condition, circle
equations via completing the square, exponential half-life models,
rational equations, systems with no/infinite solutions, function
composition, and right-triangle trig with exact ratios.

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

from sympy import Eq, Rational, expand, pi, sqrt, symbols
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

    # Q1 E algebra one_var
    assert _solve(Eq(7 * x - 5, 3 * x + 19), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $7x - 5 = 3x + 19$, what is the value of $x$?",
        r"Subtract $3x$ and add 5 to both sides:"
        r" $$4x = 24 \;\Rightarrow\; x = 6.$$"
        r" Leaving the equation at $4x = 24$ gives 24; subtracting 5 instead"
        r" of adding gives $\frac{14}{4} = 3.5$."
        r" The correct answer is **A**.",
        ["Eq(7*6 - 5, 3*6 + 19)", "Eq((19 + 5)/(7 - 3), 6)"],
        6, {Rational(7, 2): "subtracted 5 instead of adding", 24: "did not divide",
            3: "divided 24 by 8"}, fmt=smart))

    # Q2 E psda mean, FIGURE value table
    vals = [18, 30, 22, 27, 23]
    assert Fraction(sum(vals), 5) == 24
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q02", M, 2, "psda", "one_var_data", "easy",
        r"The table shows the number of pages Naran read on each of five"
        r" days. What is the mean number of pages per day?",
        r"Add the five values and divide by 5:"
        r" $$\frac{18 + 30 + 22 + 27 + 23}{5} = \frac{120}{5} = 24.$$"
        r" The middle value when ordered (the median) is 23, and dividing"
        r" the total by 4 gives 30."
        r" The correct answer is **A**.",
        ["Eq(Rational(18 + 30 + 22 + 27 + 23, 5), 24)"],
        24, {23: "the median", 30: "divided by 4", 120: "the sum"},
        fig=figure("sat-p5-m1-q02",
                   "Table with days Mon through Fri and pages 18, 30, 22, "
                   "27, 23.")))

    # Q3 E geometry_trig triangle angle
    assert 180 - 47 - 68 == 65
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q03", M, 3, "geometry_trig", "angles", "easy",
        r"Two of the interior angles of a triangle measure $47^\circ$ and"
        r" $68^\circ$. What is the measure of the third angle?",
        r"The interior angles of a triangle sum to $180^\circ$:"
        r" $$180 - 47 - 68 = 65^\circ.$$"
        r" Adding the two given angles gives $115^\circ$, and assuming a"
        r" right angle would leave $90 - 65 = 25^\circ$."
        r" The correct answer is **B**.",
        ["Eq(180 - 47 - 68, 65)"],
        65, {25: "assumed a right triangle", 47: "repeated a given angle",
             115: "added the two given angles"}))

    # Q4 E algebra SPR
    assert _solve(Eq(3 * (x - 4), 18), x) == [10]
    qs.append(spr(
        "SAT-P5-M1-Q04", M, 4, "algebra", "linear_equations_one_var", "easy",
        r"If $3(x - 4) = 18$, what is the value of $x$?",
        ["10"],
        r"Divide both sides by 3, then add 4:"
        r" $$x - 4 = 6 \;\Rightarrow\; x = 10.$$",
        ["Eq(3*(10 - 4), 18)"]))

    # Q5 E advanced_math function eval
    assert 2 * 4 ** 2 - 3 * 4 + 1 == 21
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q05", M, 5, "advanced_math", "function_notation", "easy",
        r"The function $f$ is defined by $f(x) = 2x^2 - 3x + 1$. What is the"
        r" value of $f(4)$?",
        r"Substitute $x = 4$:"
        r" $$2(4)^2 - 3(4) + 1 = 32 - 12 + 1 = 21.$$"
        r" Squaring $2x$ as a whole gives $64 - 12 + 1 = 53$; using $x = 5$"
        r" gives $50 - 15 + 1 = 36$; using $x = -4$ gives $32 + 12 + 1 = 45$."
        r" The correct answer is **A**.",
        ["Eq(2*4**2 - 3*4 + 1, 21)", "Eq(2*5**2 - 3*5 + 1, 36)",
         "Eq(2*(-4)**2 - 3*(-4) + 1, 45)"],
        21, {53: "squared 2x as a whole", 36: "used x equals 5",
             45: "used x equals negative 4"}))

    # Q6 E psda percent
    assert Fraction(40) * Fraction(85, 100) == 34
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q06", M, 6, "psda", "percentages", "easy",
        r"A jacket that normally costs $\$40$ is on sale for $15\%$ off."
        r" What is the sale price, in dollars?",
        r"A $15\%$ discount means paying $85\%$ of the price:"
        r" $$40 \times 0.85 = 34.$$"
        r" The discount alone is $40 \times 0.15 = 6$; increasing by $15\%$"
        r" gives 46; subtracting 15 gives 25."
        r" The correct answer is **B**.",
        ["Eq(40*Rational(85, 100), 34)"],
        34, {6: "the discount only", 46: "increased instead", 25: "subtracted 15"}))

    # Q7 M algebra slope
    assert Fraction(13 - 5, 6 - 2) == 2
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q07", M, 7, "algebra", "linear_functions", "medium",
        r"A line in the $xy$-plane passes through the points $(2, 5)$ and"
        r" $(6, 13)$. What is the slope of the line?",
        r"Slope is the change in $y$ over the change in $x$:"
        r" $$\frac{13 - 5}{6 - 2} = \frac{8}{4} = 2.$$"
        r" Inverting the ratio gives $\frac{1}{2}$; a sign slip gives $-2$;"
        r" using only the run gives 4."
        r" The correct answer is **C**.",
        ["Eq(Rational(13 - 5, 6 - 2), 2)"],
        2, {Rational(1, 2): "inverted the ratio", -2: "sign error",
            4: "used the run only"}, fmt=smart))

    # Q8 M advanced_math quadratic roots (listed)
    assert sorted(_solve(Eq(x ** 2 - 7 * x + 12, 0), x)) == [3, 4]
    qs.append(mcq_listed(
        "SAT-P5-M1-Q08", M, 8, "advanced_math", "quadratic_equations", "medium",
        r"What are the solutions to the equation $x^2 - 7x + 12 = 0$?",
        {"A": r"$x = -4$ and $x = -3$", "B": r"$x = -6$ and $x = -2$",
         "C": r"$x = 2$ and $x = 6$", "D": r"$x = 3$ and $x = 4$"},
        "D",
        r"Factor the quadratic into two binomials whose constants multiply"
        r" to $12$ and add to $-7$:"
        r" $$x^2 - 7x + 12 = (x - 3)(x - 4) = 0.$$"
        r" So $x = 3$ or $x = 4$. Choice C multiplies to 12 but adds to 8,"
        r" not 7."
        r" The correct answer is **D**.",
        ["Eq(3**2 - 7*3 + 12, 0)", "Eq(4**2 - 7*4 + 12, 0)"]))

    # Q9 M geometry_trig SPR circle area coefficient
    assert Eq(pi * 5 ** 2, 25 * pi)
    qs.append(spr(
        "SAT-P5-M1-Q09", M, 9, "geometry_trig", "circles", "medium",
        r"A circle has a radius of $5$. The area of the circle is $k\pi$."
        r" What is the value of $k$?",
        ["25"],
        r"The area of a circle is $\pi r^2$:"
        r" $$\pi (5)^2 = 25\pi,$$"
        r" so $k = 25$.",
        ["Eq(pi*5**2, 25*pi)"]))

    # Q10 E psda two-way table, FIGURE
    assert 12 + 10 == 22
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q10", M, 10, "psda", "two_way_tables", "easy",
        r"The table shows how $60$ students travel to school. How many of"
        r" the students walk to school?",
        r"The Walk column contains the Grade 9 and Grade 10 walkers:"
        r" $$12 + 10 = 22.$$"
        r" Choice with 12 counts only Grade 9; 10 counts only Grade 10;"
        r" 30 is a bus column."
        r" The correct answer is **C**.",
        ["Eq(12 + 10, 22)"],
        22, {12: "Grade 9 walkers only", 10: "Grade 10 walkers only",
             30: "a bus column"},
        fig=figure("sat-p5-m1-q10",
                   "Two-way table: rows Grade 9 and Grade 10, columns Bus "
                   "and Walk, cells 18, 12, 20, 10.")))

    # Q11 M algebra linear model
    assert 30 + 12 * 9 == 138
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q11", M, 11, "algebra", "linear_functions", "medium",
        r"A gym charges a one-time joining fee of $\$30$ plus $\$12$ for each"
        r" month of membership. What is the total cost, in dollars, of a"
        r" $9$-month membership?",
        r"Add the joining fee to $12$ per month for $9$ months:"
        r" $$30 + 12 \times 9 = 30 + 108 = 138.$$"
        r" Dropping the fee gives 108; using one month gives 42; using $10$"
        r" months gives $30 + 120 = 150$."
        r" The correct answer is **C**.",
        ["Eq(30 + 12*9, 138)"],
        138, {108: "dropped the joining fee", 42: "used one month",
              150: "used 10 months"}))

    # Q12 M advanced_math exponential, FIGURE
    assert 500 * 2 ** 3 == 4000
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q12", M, 12, "advanced_math", "exponential_functions",
        "medium",
        r"A colony of bacteria starts with $500$ cells and doubles every $3$"
        r" hours. How many cells are in the colony after $9$ hours?",
        r"In $9$ hours the colony doubles $9 \div 3 = 3$ times:"
        r" $$500 \times 2^{3} = 500 \times 8 = 4000.$$"
        r" Multiplying by 3 gives 1500; doubling only twice gives 2000;"
        r" using $12$ hours gives $500 \times 2^4 = 8000$."
        r" The correct answer is **C**.",
        ["Eq(500*2**3, 4000)"],
        4000, {1500: "multiplied by 3", 2000: "doubled only twice",
               8000: "used 12 hours"},
        fig=figure("sat-p5-m1-q12",
                   "Increasing exponential curve through (0, 500), (3, 1000), "
                   "(6, 2000), (9, 4000).")))

    # Q13 M geometry_trig cosine ratio, FIGURE right triangle
    assert Fraction(6, 10) == Fraction(3, 5)
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q13", M, 13, "geometry_trig", "right_triangle_trig",
        "medium",
        r"In a right triangle, the side adjacent to angle $\theta$ has"
        r" length $6$, the side opposite has length $8$, and the hypotenuse"
        r" has length $10$. What is the value of $\cos\theta$?",
        r"Cosine is adjacent over hypotenuse:"
        r" $$\cos\theta = \frac{6}{10} = \frac{3}{5}.$$"
        r" $\frac{4}{5}$ is $\sin\theta$; $\frac{4}{3}$ is $\tan\theta$;"
        r" $\frac{3}{4}$ inverts the tangent."
        r" The correct answer is **A**.",
        ["Eq(Rational(6, 10), Rational(3, 5))"],
        Rational(3, 5), {Rational(4, 5): "used the sine ratio",
                         Rational(4, 3): "used the tangent ratio",
                         Rational(3, 4): "inverted the tangent"}, fmt=frac,
        fig=figure("sat-p5-m1-q13",
                   "Right triangle with legs 6 (adjacent to theta) and 8, "
                   "hypotenuse 10, angle theta marked at the vertex between "
                   "the leg of length 6 and the hypotenuse.")))

    # Q14 M advanced_math SPR vertex minimum
    assert 3 ** 2 - 6 * 3 + 11 == 2
    qs.append(spr(
        "SAT-P5-M1-Q14", M, 14, "advanced_math", "quadratic_functions",
        "medium",
        r"The function $f$ is defined by $f(x) = x^2 - 6x + 11$. What is the"
        r" minimum value of $f(x)$?",
        ["2"],
        r"The minimum of an upward parabola occurs at $x = -\frac{b}{2a} = 3$:"
        r" $$f(3) = 9 - 18 + 11 = 2.$$",
        ["Eq(3**2 - 6*3 + 11, 2)"]))

    # Q15 M algebra ticket system
    assert 9 * 21 + 5 * (40 - 21) == 284
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q15", M, 15, "algebra", "systems_linear", "medium",
        r"A theater sells adult tickets for $\$9$ and child tickets for"
        r" $\$5$. One evening $40$ tickets were sold for a total of $\$284$."
        r" How many adult tickets were sold?",
        r"With $a$ adult tickets and $40 - a$ child tickets,"
        r" $$9a + 5(40 - a) = 284 \;\Rightarrow\; 4a + 200 = 284"
        r" \;\Rightarrow\; a = 21.$$"
        r" Then $40 - 21 = 19$ child tickets; 40 is the total; 84 is $4a$"
        r" before dividing."
        r" The correct answer is **B**.",
        ["Eq(9*21 + 5*(40 - 21), 284)"],
        21, {19: "the child-ticket count", 40: "the total tickets",
             84: "the value of 4a before dividing"}))

    # Q16 H advanced_math nonlinear system, sum of x-solutions
    assert sorted(_solve(Eq(x ** 2 - 4, 3 * x), x)) == [-1, 4]
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q16", M, 16, "advanced_math", "nonlinear_systems", "hard",
        r"The graphs of $y = x^2 - 4$ and $y = 3x$ intersect at two points."
        r" What is the sum of the $x$-coordinates of those points?",
        r"Set the expressions equal and collect terms:"
        r" $$x^2 - 4 = 3x \;\Rightarrow\; x^2 - 3x - 4 = 0"
        r" \;\Rightarrow\; (x - 4)(x + 1) = 0.$$"
        r" The solutions are $x = 4$ and $x = -1$, whose sum is $3$. The"
        r" product is $-4$, and $|4| + |-1| = 5$."
        r" The correct answer is **C**.",
        ["Eq(4 + (-1), 3)", "Eq(4**2 - 4, 3*4)", "Eq((-1)**2 - 4, 3*(-1))"],
        3, {-4: "the product of the solutions", -3: "a sign error on the sum",
            5: "added the absolute values"}))

    # Q17 M psda box plot IQR, FIGURE
    assert 36 - 20 == 16
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q17", M, 17, "psda", "one_var_data", "medium",
        r"The box plot summarizes a data set with minimum $12$, first"
        r" quartile $20$, median $28$, third quartile $36$, and maximum $50$."
        r" What is the interquartile range of the data?",
        r"The interquartile range is the third quartile minus the first:"
        r" $$36 - 20 = 16.$$"
        r" The full range is $50 - 12 = 38$; 28 is the median; $28 - 20 = 8$"
        r" is only the lower half."
        r" The correct answer is **B**.",
        ["Eq(36 - 20, 16)"],
        16, {38: "the full range", 28: "the median", 8: "median minus Q1"},
        fig=figure("sat-p5-m1-q17",
                   "Box plot with minimum 12, Q1 20, median 28, Q3 36, "
                   "maximum 50 on a number line.")))

    # Q18 H algebra SPR system
    assert _solve([Eq(2 * x + 3 * symbols("y"), 16),
                   Eq(4 * x - 3 * symbols("y"), 8)],
                  [x, symbols("y")])[x] == 4
    qs.append(spr(
        "SAT-P5-M1-Q18", M, 18, "algebra", "systems_linear", "hard",
        r"$$2x + 3y = 16$$ $$4x - 3y = 8$$"
        r" The system of equations above has solution $(x, y)$. What is the"
        r" value of $x$?",
        ["4"],
        r"Adding the two equations eliminates $y$:"
        r" $$6x = 24 \;\Rightarrow\; x = 4.$$",
        ["Eq(2*4 + 3*Rational(8, 3), 16)", "Eq(4*4 - 3*Rational(8, 3), 8)"]))

    # Q19 H advanced_math discriminant
    assert 8 ** 2 - 4 * 16 == 0
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q19", M, 19, "advanced_math", "quadratic_equations", "hard",
        r"For what value of $c$ does the equation $x^2 + 8x + c = 0$ have"
        r" exactly one real solution?",
        r"A quadratic has exactly one real solution when its discriminant"
        r" $b^2 - 4ac$ equals zero:"
        r" $$8^2 - 4(1)c = 0 \;\Rightarrow\; 64 = 4c \;\Rightarrow\; c = 16.$$"
        r" Halving $8$ gives 8; doubling gives 32; $8^2$ alone gives 64."
        r" The correct answer is **B**.",
        ["Eq(8**2 - 4*16, 0)"],
        16, {8: "halved the 8", 32: "doubled the answer",
             64: "used b squared only"}))

    # Q20 H geometry_trig circle radius from equation
    assert (-3) ** 2 + 4 ** 2 - 9 == 16 and sqrt(16) == 4
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"A circle in the $xy$-plane has equation"
        r" $x^2 + y^2 - 6x + 8y + 9 = 0$. What is the radius of the circle?",
        r"Complete the square in $x$ and $y$:"
        r" $$(x - 3)^2 + (y + 4)^2 = -9 + 9 + 16 = 16.$$"
        r" The radius is $\sqrt{16} = 4$. Choice 16 is $r^2$; 5 comes from"
        r" $\sqrt{9 + 16}$; 8 is the diameter $2r$."
        r" The correct answer is **A**.",
        ["Eq((-3)**2 + 4**2 - 9, 16)", "Eq(sqrt(16), 4)"],
        4, {16: "used r squared", 5: "took the square root of 25",
            8: "used the diameter"}))

    # Q21 H advanced_math SPR polynomial root product
    assert 1 ** 3 - 2 * 1 ** 2 - 5 * 1 + 6 == 0
    assert sorted(_solve(Eq(x ** 3 - 2 * x ** 2 - 5 * x + 6, 0), x)) == [-2, 1, 3]
    qs.append(spr(
        "SAT-P5-M1-Q21", M, 21, "advanced_math", "polynomials", "hard",
        r"One solution of $x^3 - 2x^2 - 5x + 6 = 0$ is $x = 1$. What is the"
        r" product of the other two solutions?",
        ["-6"],
        r"Since $x = 1$ is a root, factor it out:"
        r" $$x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 - x - 6) = (x - 1)(x - 3)(x + 2).$$"
        r" The other two solutions are $3$ and $-2$, whose product is"
        r" $3 \times (-2) = -6$.",
        ["Eq(3*(-2), -6)", "Eq(1**3 - 2*1**2 - 5*1 + 6, 0)"]))

    # Q22 E algebra proportion
    assert Fraction(3, 4) * 20 == 15
    qs.append(mcq_numeric(
        "SAT-P5-M1-Q22", M, 22, "algebra", "ratios_proportions", "easy",
        r"If $\dfrac{3}{4} = \dfrac{x}{20}$, what is the value of $x$?",
        r"Multiply both sides by $20$:"
        r" $$x = \frac{3}{4} \times 20 = 15.$$"
        r" Multiplying $3 \times 20$ without dividing gives 60; $20 \div 4$"
        r" gives 5; $4 \times 20$ gives 80."
        r" The correct answer is **B**.",
        ["Eq(Rational(3, 4)*20, 15)"],
        15, {60: "multiplied 3 by 20", 5: "divided 20 by 4",
             80: "multiplied 4 by 20"}))

    return qs


# ─── Module 2 Easy (11E / 9M / 2H) ────────────────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E algebra one_var
    assert _solve(Eq(5 * x + 8, 43), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $5x + 8 = 43$, what is the value of $x$?",
        r"Subtract 8, then divide by 5:"
        r" $$5x = 35 \;\Rightarrow\; x = 7.$$"
        r" Adding 8 gives $\frac{51}{5} = 10.2$; leaving $5x = 35$ gives 35."
        r" The correct answer is **A**.",
        ["Eq(5*7 + 8, 43)"],
        7, {Rational(51, 5): "added 8 instead", 35: "did not divide",
            9: "divided by a wrong value"}, fmt=smart))

    # Q2 E psda bar chart, FIGURE
    assert 12 - 4 == 8
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q02", M, 2, "psda", "one_var_data", "easy",
        r"The bar chart shows the number of books four students read."
        r" How many more books did Bat read than Dorj?",
        r"Bat read $12$ and Dorj read $4$:"
        r" $$12 - 4 = 8.$$"
        r" Adding gives 16; Bat's value alone is 12; Dorj's alone is 4."
        r" The correct answer is **B**.",
        ["Eq(12 - 4, 8)"],
        8, {16: "added the two values", 12: "Bat's total only",
            4: "Dorj's total only"},
        fig=figure("sat-p5-m2e-q02",
                   "Bar chart of books read: Ana 7, Bat 12, Chimeg 9, "
                   "Dorj 4.")))

    # Q3 E advanced_math SPR function eval
    assert (2 * 3 + 1) ** 2 == 49
    qs.append(spr(
        "SAT-P5-M2E-Q03", M, 3, "advanced_math", "function_notation", "easy",
        r"The function $g$ is defined by $g(x) = (2x + 1)^2$. What is the"
        r" value of $g(3)$?",
        ["49"],
        r"Substitute $x = 3$ and square:"
        r" $$g(3) = (2 \cdot 3 + 1)^2 = 7^2 = 49.$$",
        ["Eq((2*3 + 1)**2, 49)"]))

    # Q4 E algebra evaluate expression
    assert 4 * 5 - 2 * 3 == 14
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q04", M, 4, "algebra", "linear_expressions", "easy",
        r"What is the value of $4a - 2b$ when $a = 5$ and $b = 3$?",
        r"Substitute and simplify:"
        r" $$4(5) - 2(3) = 20 - 6 = 14.$$"
        r" Adding the terms gives 26; $4 \cdot 5 - 2 = 18$ drops a factor;"
        r" $20 - 2 \cdot 3 \cdot$ sign gives 26 as well."
        r" The correct answer is **A**.",
        ["Eq(4*5 - 2*3, 14)"],
        14, {26: "added instead of subtracting", 18: "multiplied only a",
             8: "used b equals 6"}))

    # Q5 E advanced_math evaluate power
    assert 3 ** 4 == 81
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q05", M, 5, "advanced_math", "exponents", "easy",
        r"What is the value of $3^4$?",
        r"Multiply $3$ by itself four times:"
        r" $$3^4 = 3 \cdot 3 \cdot 3 \cdot 3 = 81.$$"
        r" Multiplying $3 \times 4$ gives 12; $3^3$ gives 27; $4^3$ gives 64."
        r" The correct answer is **D**.",
        ["Eq(3**4, 81)"],
        81, {12: "multiplied 3 by 4", 27: "used 3 cubed",
             64: "used 4 cubed"}))

    # Q6 E geometry_trig perimeter
    assert 2 * (9 + 5) == 28
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q06", M, 6, "geometry_trig", "perimeter_area", "easy",
        r"A rectangle has a length of $9$ and a width of $5$. What is its"
        r" perimeter?",
        r"Perimeter is twice the sum of length and width:"
        r" $$2(9 + 5) = 2(14) = 28.$$"
        r" The area is $9 \times 5 = 45$; adding once gives 14; doubling"
        r" the length only gives 18."
        r" The correct answer is **B**.",
        ["Eq(2*(9 + 5), 28)"],
        28, {45: "found the area", 14: "added once", 18: "doubled length only"}))

    # Q7 E algebra SPR proportion
    assert Fraction(60, 4) == 15
    qs.append(spr(
        "SAT-P5-M2E-Q07", M, 7, "algebra", "ratios_proportions", "easy",
        r"A car travels $60$ miles in $4$ hours at a constant speed. How"
        r" many miles does it travel in $1$ hour?",
        ["15"],
        r"Divide the distance by the time:"
        r" $$\frac{60}{4} = 15 \text{ miles per hour.}$$",
        ["Eq(Rational(60, 4), 15)"]))

    # Q8 E advanced_math simplify (listed)
    assert expand((x + 3) * (x - 3)) == x ** 2 - 9
    qs.append(mcq_listed(
        "SAT-P5-M2E-Q08", M, 8, "advanced_math", "polynomials", "medium",
        r"Which of the following is equivalent to $(x + 3)(x - 3)$?",
        {"A": r"$x^2 - 9$", "B": r"$x^2 + 9$", "C": r"$x^2 - 6x + 9$",
         "D": r"$x^2 - 6$"},
        "A",
        r"This is a difference of squares:"
        r" $$(x + 3)(x - 3) = x^2 - 9.$$"
        r" The middle terms $+3x$ and $-3x$ cancel, so there is no $x$-term."
        r" The correct answer is **A**.",
        ["Eq(expand((x + 3)*(x - 3)), x**2 - 9)"]))

    # Q9 E algebra solve for variable
    assert _solve(Eq(2 * x - 9, 5), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q09", M, 9, "algebra", "linear_equations_one_var", "easy",
        r"If $2x - 9 = 5$, what is the value of $x$?",
        r"Add 9, then divide by 2:"
        r" $$2x = 14 \;\Rightarrow\; x = 7.$$"
        r" Subtracting 9 gives $-2$; leaving $2x = 14$ gives 14;"
        r" dividing 5 by 2 gives 2.5."
        r" The correct answer is **B**.",
        ["Eq(2*7 - 9, 5)"],
        7, {-2: "subtracted 9 instead", 14: "did not divide",
            Rational(5, 2): "divided 5 by 2"}, fmt=smart))

    # Q10 M psda line of best fit, FIGURE scatter
    assert 4 * 6 + 5 == 29
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q10", M, 10, "psda", "scatterplots", "medium",
        r"The line of best fit for a set of data is $y = 4x + 5$. Based on"
        r" this model, what is the predicted value of $y$ when $x = 6$?",
        r"Substitute $x = 6$ into the model:"
        r" $$y = 4(6) + 5 = 29.$$"
        r" Dropping the intercept gives 24; adding $6 + 5$ ignores the slope"
        r" (11); using $x = 5$ gives 25."
        r" The correct answer is **C**.",
        ["Eq(4*6 + 5, 29)"],
        29, {24: "dropped the intercept", 11: "ignored the slope",
             25: "used x equals 5"},
        fig=figure("sat-p5-m2e-q10",
                   "Scatterplot of points rising left to right with the line "
                   "of best fit y = 4x + 5 drawn through them.")))

    # Q11 M advanced_math quadratic vertex form value
    assert (-2) ** 2 - 4 * (-2) + 1 == 13
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q11", M, 11, "advanced_math", "quadratic_functions",
        "medium",
        r"The function $h$ is defined by $h(x) = x^2 - 4x + 1$. What is the"
        r" value of $h(-2)$?",
        r"Substitute $x = -2$:"
        r" $$(-2)^2 - 4(-2) + 1 = 4 + 8 + 1 = 13.$$"
        r" Treating $-4(-2)$ as $-8$ gives $-3$; dropping the sign on the"
        r" square gives 5; using $x = 2$ gives $-3$ as well."
        r" The correct answer is **D**.",
        ["Eq((-2)**2 - 4*(-2) + 1, 13)"],
        13, {-3: "sign error on the middle term", 5: "dropped a sign",
             9: "used x equals 2 wrongly"}))

    # Q12 M algebra SPR system substitution
    ysym = symbols("y")
    sol12 = _solve([Eq(x + ysym, 12), Eq(x - ysym, 4)], [x, ysym])
    assert sol12[x] == 8
    qs.append(spr(
        "SAT-P5-M2E-Q12", M, 12, "algebra", "systems_linear", "medium",
        r"$$x + y = 12$$ $$x - y = 4$$"
        r" The system above has solution $(x, y)$. What is the value of $x$?",
        ["8"],
        r"Add the two equations to eliminate $y$:"
        r" $$2x = 16 \;\Rightarrow\; x = 8.$$",
        ["Eq(8 + 4, 12)", "Eq(8 - 4, 4)"]))

    # Q13 M geometry_trig Pythagorean, FIGURE right triangle
    assert 9 ** 2 + 12 ** 2 == 15 ** 2
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q13", M, 13, "geometry_trig", "right_triangle_trig",
        "medium",
        r"A right triangle has legs of length $9$ and $12$. What is the"
        r" length of the hypotenuse?",
        r"Apply the Pythagorean theorem:"
        r" $$\sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15.$$"
        r" Adding the legs gives 21; $\sqrt{81 + 144}$ mis-added is 13;"
        r" the difference of squares gives $\sqrt{63} \approx 7.9$."
        r" The correct answer is **C**.",
        ["Eq(9**2 + 12**2, 15**2)"],
        15, {21: "added the legs", 13: "estimated the square root",
             8: "subtracted the squares"},
        fig=figure("sat-p5-m2e-q13",
                   "Right triangle with legs labeled 9 and 12 and the "
                   "hypotenuse unknown.")))

    # Q14 M advanced_math exponential decay
    assert 800 * Fraction(1, 2) ** 2 == 200
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q14", M, 14, "advanced_math", "exponential_functions",
        "medium",
        r"A sample of $800$ grams of a substance loses half its mass every"
        r" $5$ years. How many grams remain after $10$ years?",
        r"In $10$ years the mass halves $10 \div 5 = 2$ times:"
        r" $$800 \times \left(\tfrac{1}{2}\right)^2 = 800 \times \tfrac14 = 200.$$"
        r" Halving once gives 400; subtracting half twice gives $800 - 400"
        r" = 400$; using three half-lives gives 100."
        r" The correct answer is **B**.",
        ["Eq(800*Rational(1, 2)**2, 200)"],
        200, {400: "halved only once", 100: "used three half-lives",
              300: "subtracted a fixed amount"}))

    # Q15 E algebra SPR
    assert _solve(Eq(x / 3 + 4, 10), x) == [18]
    qs.append(spr(
        "SAT-P5-M2E-Q15", M, 15, "algebra", "linear_equations_one_var", "easy",
        r"If $\dfrac{x}{3} + 4 = 10$, what is the value of $x$?",
        ["18"],
        r"Subtract 4, then multiply by 3:"
        r" $$\frac{x}{3} = 6 \;\Rightarrow\; x = 18.$$",
        ["Eq(Rational(18, 3) + 4, 10)"]))

    # Q16 H advanced_math rational equation
    assert sorted(_solve(Eq(12 / x, x - 1), x)) == [-3, 4]
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q16", M, 16, "advanced_math", "rational_equations", "hard",
        r"What is the positive solution to $\dfrac{12}{x} = x - 1$?",
        r"Multiply both sides by $x$ and rearrange:"
        r" $$12 = x^2 - x \;\Rightarrow\; x^2 - x - 12 = 0"
        r" \;\Rightarrow\; (x - 4)(x + 3) = 0.$$"
        r" The solutions are $4$ and $-3$; the positive one is $4$. Choice 3"
        r" comes from a sign slip and 12 from not solving."
        r" The correct answer is **B**.",
        ["Eq(Rational(12, 4), 4 - 1)", "Eq(4**2 - 4 - 12, 0)"],
        4, {-3: "the negative solution", 3: "a sign slip",
            12: "did not solve"}))

    # Q17 M psda histogram median-ish (count), FIGURE
    assert 6 + 9 == 15
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q17", M, 17, "psda", "one_var_data", "medium",
        r"The histogram shows the number of days in a month grouped by daily"
        r" high temperature. How many days had a high temperature of at"
        r" least $70^\circ$?",
        r"Add the two rightmost bars, for $70$–$79$ and $80$–$89$:"
        r" $$6 + 9 = 15.$$"
        r" Using only the $80$s bar gives 9; only the $70$s bar gives 6;"
        r" adding all four bars gives 30."
        r" The correct answer is **C**.",
        ["Eq(6 + 9, 15)"],
        15, {9: "the 80s bar only", 6: "the 70s bar only",
             30: "all four bars"},
        fig=figure("sat-p5-m2e-q17",
                   "Histogram with bars for 50-59, 60-69, 70-79, 80-89 of "
                   "heights 7, 8, 6, 9.")))

    # Q18 M geometry_trig similar triangles
    assert Fraction(15 * 8, 6) == 20
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q18", M, 18, "geometry_trig", "similar_triangles",
        "medium",
        r"Two triangles are similar. The sides of the smaller triangle are"
        r" $6$, $8$, and $10$. The side of the larger triangle corresponding"
        r" to the side of length $6$ is $15$. What is the length of the"
        r" larger triangle's side corresponding to the side of length $8$?",
        r"The scale factor is $\frac{15}{6} = 2.5$:"
        r" $$8 \times 2.5 = 20.$$"
        r" Adding the difference $15 - 6 = 9$ to $8$ gives 17; using a scale"
        r" factor of $3$ gives 24; scaling the $10$-side gives 25."
        r" The correct answer is **B**.",
        ["Eq(Rational(15*8, 6), 20)"],
        20, {17: "added the difference", 24: "used scale factor 3",
             25: "scaled the wrong side"}))

    # Q19 E algebra SPR
    assert _solve(Eq(6 * x, 2 * x + 20), x) == [5]
    qs.append(spr(
        "SAT-P5-M2E-Q19", M, 19, "algebra", "linear_equations_one_var", "easy",
        r"If $6x = 2x + 20$, what is the value of $x$?",
        ["5"],
        r"Subtract $2x$, then divide by 4:"
        r" $$4x = 20 \;\Rightarrow\; x = 5.$$",
        ["Eq(6*5, 2*5 + 20)"]))

    # Q20 M advanced_math system nonlinear point (listed)
    assert (2, 1) and 2 ** 2 - 3 == 1 and 2 * 2 - 3 == 1
    qs.append(mcq_listed(
        "SAT-P5-M2E-Q20", M, 20, "advanced_math", "nonlinear_systems", "medium",
        r"Which ordered pair $(x, y)$ is a solution to both $y = x^2 - 3$"
        r" and $y = 2x - 3$?",
        {"A": r"$(0, -3)$ only", "B": r"$(2, 1)$ only",
         "C": r"$(0, -3)$ and $(2, 1)$", "D": r"$(-2, -7)$"},
        "C",
        r"Set the two right sides equal:"
        r" $$x^2 - 3 = 2x - 3 \;\Rightarrow\; x^2 - 2x = 0"
        r" \;\Rightarrow\; x(x - 2) = 0.$$"
        r" So $x = 0$ (giving $y = -3$) and $x = 2$ (giving $y = 1$); both"
        r" points satisfy each equation."
        r" The correct answer is **C**.",
        ["Eq(0**2 - 3, 2*0 - 3)", "Eq(2**2 - 3, 2*2 - 3)"]))

    # Q21 E advanced_math evaluate
    assert 2 ** 3 + 2 ** 2 == 12
    qs.append(mcq_numeric(
        "SAT-P5-M2E-Q21", M, 21, "advanced_math", "exponents", "easy",
        r"What is the value of $2^3 + 2^2$?",
        r"Evaluate each power, then add:"
        r" $$8 + 4 = 12.$$"
        r" Multiplying the exponents gives $2^6 = 64$; $2^{3+2} = 32$ adds"
        r" the exponents; $6 + 4 = 10$ mis-evaluates the first power."
        r" The correct answer is **A**.",
        ["Eq(2**3 + 2**2, 12)"],
        12, {64: "multiplied the powers", 32: "added the exponents",
             10: "used 2 times 3"}))

    # Q22 H algebra SPR literal / combined rate
    assert Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)
    qs.append(spr(
        "SAT-P5-M2E-Q22", M, 22, "algebra", "rational_equations", "hard",
        r"One pipe fills a tank in $3$ hours and a second pipe fills the"
        r" same tank in $6$ hours. Working together, how many hours do they"
        r" take to fill the tank?",
        ["2"],
        r"Together they fill $\frac{1}{3} + \frac{1}{6} = \frac{1}{2}$ of the"
        r" tank per hour, so the whole tank takes"
        r" $$\frac{1}{\,1/2\,} = 2 \text{ hours.}$$",
        ["Eq(Rational(1, 3) + Rational(1, 6), Rational(1, 2))"]))

    return qs


# ─── Module 2 Hard (2E / 7M / 13H) ────────────────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E algebra one_var
    assert _solve(Eq(3 * x - 7, 14), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $3x - 7 = 14$, what is the value of $x$?",
        r"Add 7, then divide by 3:"
        r" $$3x = 21 \;\Rightarrow\; x = 7.$$"
        r" Leaving $3x = 21$ gives 21; subtracting 7 gives $\frac{7}{3}$;"
        r" dividing 14 by 3 gives about 4.7."
        r" The correct answer is **A**.",
        ["Eq(3*7 - 7, 14)"],
        7, {21: "did not divide", Rational(7, 3): "subtracted 7 instead",
            9: "used a wrong divisor"}, fmt=smart))

    # Q2 E psda percent, FIGURE bar chart
    assert Fraction(18, 60) * 100 == 30
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q02", M, 2, "psda", "percentages", "easy",
        r"A survey of $60$ people found that $18$ preferred tea. What"
        r" percent of the people surveyed preferred tea?",
        r"Divide and convert to a percent:"
        r" $$\frac{18}{60} \times 100 = 30\%.$$"
        r" The raw count is 18; $60 - 18 = 42$ is the other group;"
        r" $\frac{60}{18}$ inverts the ratio (about $333\%$)."
        r" The correct answer is **B**.",
        ["Eq(Rational(18, 60)*100, 30)"],
        30, {18: "the raw count", 42: "the complement count",
             12: "a miscomputed ratio"},
        fig=figure("sat-p5-m2h-q02",
                   "Bar chart of drink preference: Tea 18, Coffee 24, "
                   "Water 18 out of 60 people.")))

    # Q3 M advanced_math SPR quadratic sum of roots
    assert sorted(_solve(Eq(x ** 2 - 9 * x + 20, 0), x)) == [4, 5]
    qs.append(spr(
        "SAT-P5-M2H-Q03", M, 3, "advanced_math", "quadratic_equations",
        "medium",
        r"What is the sum of the solutions to $x^2 - 9x + 20 = 0$?",
        ["9"],
        r"Factor: $(x - 4)(x - 5) = 0$, so the solutions are $4$ and $5$:"
        r" $$4 + 5 = 9.$$"
        r" (Equivalently, the sum of the roots equals $-\frac{b}{a} = 9$.)",
        ["Eq(4 + 5, 9)", "Eq(4*5, 20)"]))

    # Q4 M algebra inequality boundary
    assert _solve(Eq(5 * x - 3, 2 * x + 12), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q04", M, 4, "algebra", "linear_inequalities", "medium",
        r"For what value of $x$ is $5x - 3$ equal to $2x + 12$?",
        r"Collect the variable on one side:"
        r" $$5x - 3 = 2x + 12 \;\Rightarrow\; 3x = 15 \;\Rightarrow\; x = 5.$$"
        r" Combining as $7x = 15$ gives about 2.1; $3x = 9$ gives 3;"
        r" $3x = 12$ gives 4."
        r" The correct answer is **D**.",
        ["Eq(5*5 - 3, 2*5 + 12)"],
        5, {3: "moved a term wrong", 4: "dropped the 3", 2: "added the x-terms"}))

    # Q5 M geometry_trig arc/angle
    assert Fraction(72, 360) * 2 * 5 == 2  # arc length coefficient of pi
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q05", M, 5, "geometry_trig", "circles", "medium",
        r"A circle has radius $5$. A central angle of $72^\circ$ subtends an"
        r" arc. The length of that arc is $k\pi$. What is the value of $k$?",
        r"The arc is $\frac{72}{360}$ of the full circumference $2\pi(5)$:"
        r" $$\frac{72}{360} \times 10\pi = \frac{1}{5} \times 10\pi = 2\pi,$$"
        r" so $k = 2$. Using the area formula gives 5; the full"
        r" circumference gives 10; halving gives 1."
        r" The correct answer is **A**.",
        ["Eq(Rational(72, 360)*2*5, 2)"],
        2, {5: "used the area fraction", 10: "used the full circumference",
            1: "halved the arc"}))

    # Q6 M advanced_math function composition
    def f6(t):
        return 2 * t + 1

    def g6(t):
        return t ** 2
    assert f6(g6(3)) == 19
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q06", M, 6, "advanced_math", "function_notation", "medium",
        r"The functions are defined by $f(x) = 2x + 1$ and $g(x) = x^2$."
        r" What is the value of $f(g(3))$?",
        r"Evaluate the inside function first:"
        r" $$g(3) = 9, \qquad f(9) = 2(9) + 1 = 19.$$"
        r" Computing $g(f(3)) = 7^2 = 49$ reverses the order; $f(3) = 7$"
        r" stops early; $2 \cdot 3^2 = 18$ drops the $+1$."
        r" The correct answer is **B**.",
        ["Eq(2*(3**2) + 1, 19)"],
        19, {49: "reversed the composition", 7: "evaluated f of 3 only",
             18: "dropped the plus 1"}))

    # Q7 M algebra SPR system elimination
    ysym = symbols("y")
    sol7 = _solve([Eq(3 * x + 2 * ysym, 19), Eq(x - 2 * ysym, 1)], [x, ysym])
    assert sol7[x] == 5
    qs.append(spr(
        "SAT-P5-M2H-Q07", M, 7, "algebra", "systems_linear", "medium",
        r"$$3x + 2y = 19$$ $$x - 2y = 1$$"
        r" The system above has solution $(x, y)$. What is the value of $x$?",
        ["5"],
        r"Add the two equations to eliminate $y$:"
        r" $$4x = 20 \;\Rightarrow\; x = 5.$$",
        ["Eq(3*5 + 2*Rational(19 - 15, 2), 19)", "Eq(5 - 2*2, 1)"]))

    # Q8 M advanced_math vertex x-coordinate (listed)
    assert Rational(-(-12), 2 * 2) == 3
    qs.append(mcq_listed(
        "SAT-P5-M2H-Q08", M, 8, "advanced_math", "quadratic_functions",
        "medium",
        r"The graph of $y = 2x^2 - 12x + 5$ is a parabola. What is the"
        r" $x$-coordinate of its vertex?",
        {"A": r"$x = -3$", "B": r"$x = -\dfrac{5}{2}$", "C": r"$x = 3$",
         "D": r"$x = 6$"},
        "C",
        r"The vertex is at $x = -\dfrac{b}{2a}$:"
        r" $$x = -\frac{-12}{2(2)} = \frac{12}{4} = 3.$$"
        r" Forgetting the negative sign gives $-3$; using $-\frac{b}{a}$"
        r" gives 6."
        r" The correct answer is **C**.",
        ["Eq(Rational(12, 4), 3)"]))

    # Q9 M psda probability from total
    assert Fraction(7, 28) == Fraction(1, 4)
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q09", M, 9, "psda", "probability", "medium",
        r"A bag contains $28$ marbles, of which $7$ are red. If one marble"
        r" is drawn at random, what is the probability that it is red?",
        r"Divide favorable outcomes by total outcomes:"
        r" $$\frac{7}{28} = \frac{1}{4}.$$"
        r" Using the non-red count gives $\frac{21}{28} = \frac34$;"
        r" $\frac{7}{21}$ compares red to non-red; $\frac{28}{7}$ inverts."
        r" The correct answer is **A**.",
        ["Eq(Rational(7, 28), Rational(1, 4))"],
        Rational(1, 4), {Rational(3, 4): "used the non-red count",
                         Rational(1, 3): "compared red to non-red",
                         Rational(1, 7): "used a wrong total"}, fmt=frac))

    # Q10 H algebra system with no solution
    assert Rational(6, 3) == 2 and 6 * 5 != 3 * 8
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q10", M, 10, "algebra", "systems_linear", "hard",
        r"$$6x + 3y = 8$$ $$2x + y = k$$"
        r" For what value of $k$ does the system above have infinitely many"
        r" solutions?",
        r"Dividing the first equation by 3 gives $2x + y = \frac{8}{3}$."
        r" The system has infinitely many solutions exactly when the two"
        r" equations describe the SAME line, which requires"
        r" $$k = \frac{8}{3}.$$"
        r" (For any other $k$ the lines are parallel and distinct, giving no"
        r" solution.) Choice 8 forgets to divide; $\frac{4}{3}$ halves"
        r" twice; 3 uses the wrong coefficient."
        r" The correct answer is **B**.",
        ["Eq(Rational(6, 3), 2)", "Eq(Rational(8, 3), Rational(8, 3))"],
        Rational(8, 3), {8: "forgot to divide", Rational(4, 3): "halved twice",
                         3: "used a wrong coefficient"}, fmt=smart))

    # Q11 H advanced_math discriminant inequality boundary
    assert (-6) ** 2 - 4 * 1 * 9 == 0
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q11", M, 11, "advanced_math", "quadratic_equations", "hard",
        r"The equation $x^2 - 6x + k = 0$ has exactly one real solution."
        r" What is the value of $k$?",
        r"Exactly one real solution means the discriminant is zero:"
        r" $$(-6)^2 - 4(1)k = 0 \;\Rightarrow\; 36 = 4k \;\Rightarrow\; k = 9.$$"
        r" Halving 6 gives 3; $\frac{36}{2}$ gives 18; $6^2$ alone gives 36."
        r" The correct answer is **A**.",
        ["Eq((-6)**2 - 4*9, 0)"],
        9, {3: "halved the 6", 18: "divided 36 by 2",
            36: "used b squared only"}))

    # Q12 H algebra SPR literal equation
    assert Rational(2 * 30 - 4, 2) == 28  # from P = 2L + 2W, solve W
    qs.append(spr(
        "SAT-P5-M2H-Q12", M, 12, "algebra", "linear_equations_one_var", "hard",
        r"The perimeter of a rectangle is given by $P = 2L + 2W$. A"
        r" rectangle has perimeter $P = 60$ and length $L = 2$. What is its"
        r" width $W$?",
        ["28"],
        r"Solve for $W$: $60 = 2(2) + 2W$, so $2W = 56$ and"
        r" $$W = 28.$$",
        ["Eq(2*2 + 2*28, 60)"]))

    # Q13 H geometry_trig 30-60-90, FIGURE
    assert Fraction(14, 2) == 7  # short leg of 30-60-90 with hyp 14
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q13", M, 13, "geometry_trig", "right_triangle_trig", "hard",
        r"In a $30^\circ$-$60^\circ$-$90^\circ$ right triangle, the"
        r" hypotenuse has length $14$. What is the length of the side"
        r" opposite the $30^\circ$ angle?",
        r"In a $30$-$60$-$90$ triangle the side opposite $30^\circ$ is half"
        r" the hypotenuse:"
        r" $$\frac{14}{2} = 7.$$"
        r" The side opposite $60^\circ$ is $7\sqrt{3} \approx 12.1$; the"
        r" full hypotenuse is 14; $14\sqrt{3}$ scales the wrong side."
        r" The correct answer is **A**.",
        ["Eq(Rational(14, 2), 7)"],
        7, {12: "used the 60-degree side", 14: "used the hypotenuse",
             10: "estimated incorrectly"},
        fig=figure("sat-p5-m2h-q13",
                   "Right triangle with a 30 degree angle, a 60 degree angle, "
                   "and hypotenuse labeled 14; the side opposite the 30 degree "
                   "angle is unknown.")))

    # Q14 H advanced_math exponential equation solve
    assert 2 ** (2 * 3) == 4 ** 3
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q14", M, 14, "advanced_math", "exponential_functions",
        "hard",
        r"If $2^{2x} = 4^{6}$, what is the value of $x$?",
        r"Write both sides with base 2: $4^6 = (2^2)^6 = 2^{12}$, so"
        r" $$2x = 12 \;\Rightarrow\; x = 6.$$"
        r" Setting $2x = 6$ gives 3; using $4^6 = 2^6$ gives 3 as well;"
        r" $2x = 24$ gives 12."
        r" The correct answer is **C**.",
        ["Eq(2*6, 12)", "Eq(4**6, 2**12)"],
        6, {3: "did not double the exponent", 12: "solved 2x equals 24",
            24: "used 4 as the exponent base"}))

    # Q15 H algebra SPR mixture
    assert Fraction(6 * 20 + 2 * 0, 6 + 2) == 15  # not used; do mixture below
    # 40% solution mixed: x L of 50% + 3 L of 20% = 30% -> solve
    sol15 = _solve(Eq(Rational(50, 100) * x + Rational(20, 100) * 3,
                      Rational(30, 100) * (x + 3)), x)
    assert sol15 == [Rational(3, 2)]
    qs.append(spr(
        "SAT-P5-M2H-Q15", M, 15, "algebra", "linear_equations_one_var", "hard",
        r"A chemist mixes $x$ liters of a $50\%$ acid solution with $3$"
        r" liters of a $20\%$ acid solution to obtain a $30\%$ acid"
        r" solution. What is the value of $x$?",
        ["1.5", "3/2"],
        r"The acid before and after mixing must balance:"
        r" $$0.50x + 0.20(3) = 0.30(x + 3).$$"
        r" Then $0.5x + 0.6 = 0.3x + 0.9$, so $0.2x = 0.3$ and"
        r" $$x = 1.5.$$",
        ["Eq(Rational(50, 100)*Rational(3, 2) + Rational(20, 100)*3,"
         " Rational(30, 100)*(Rational(3, 2) + 3))"]))

    # Q16 H advanced_math system of quadratics distance
    assert sorted(_solve(Eq(x ** 2 + 2 * x, 8), x)) == [-4, 2]
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q16", M, 16, "advanced_math", "quadratic_equations", "hard",
        r"The solutions to $x^2 + 2x = 8$ are $p$ and $q$. What is the value"
        r" of $p^2 + q^2$?",
        r"Factor $x^2 + 2x - 8 = (x + 4)(x - 2) = 0$, so the solutions are"
        r" $-4$ and $2$:"
        r" $$(-4)^2 + 2^2 = 16 + 4 = 20.$$"
        r" Squaring the sum $(-2)^2 = 4$ ignores the cross term; $16 - 4 = 12$"
        r" subtracts; $-4 + 2 = -2$ is just the sum."
        r" The correct answer is **C**.",
        ["Eq((-4)**2 + 2**2, 20)", "Eq((-4)**2 + 2*(-4), 8)",
         "Eq(2**2 + 2*2, 8)"],
        20, {4: "squared the sum", 12: "subtracted the squares",
             -2: "used the sum of roots"}))

    # Q17 H psda weighted / conditional, FIGURE two-way table
    assert Fraction(15, 25) == Fraction(3, 5)
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q17", M, 17, "psda", "two_way_tables", "hard",
        r"The table shows results for $60$ people. Given that a person"
        r" chosen at random is an adult, what is the probability that the"
        r" person passed?",
        r"Restrict to the $25$ adults, of whom $15$ passed:"
        r" $$P(\text{pass} \mid \text{adult}) = \frac{15}{25} = \frac{3}{5}.$$"
        r" Using the full total gives $\frac{15}{60} = \frac14$; the passed"
        r" total gives $\frac{15}{40}$; the failed adults give $\frac{10}{25}$."
        r" The correct answer is **D**.",
        ["Eq(Rational(15, 25), Rational(3, 5))"],
        Rational(3, 5), {Rational(1, 4): "divided by the full total",
                         Rational(3, 8): "used the passed total",
                         Rational(2, 5): "used the failed adults"}, fmt=frac,
        fig=figure("sat-p5-m2h-q17",
                   "Two-way table: rows Adult and Child, columns Passed and "
                   "Failed, cells 15, 10, 20, 15.")))

    # Q18 H geometry_trig inscribed angle
    assert 2 * 35 == 70
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q18", M, 18, "geometry_trig", "circles", "hard",
        r"In a circle, an inscribed angle measures $35^\circ$. What is the"
        r" measure of the central angle that subtends the same arc?",
        r"A central angle is twice any inscribed angle on the same arc:"
        r" $$2 \times 35^\circ = 70^\circ.$$"
        r" Halving instead gives $17.5^\circ$; keeping it equal gives"
        r" $35^\circ$; using $180 - 35$ gives $145^\circ$."
        r" The correct answer is **C**.",
        ["Eq(2*35, 70)"],
        70, {Rational(35, 2): "halved the angle", 35: "kept them equal",
             145: "used 180 minus the angle"}, fmt=smart))

    # Q19 H algebra SPR percent change reverse
    assert Rational(66) / Rational(110, 100) == 60
    qs.append(spr(
        "SAT-P5-M2H-Q19", M, 19, "algebra", "percentages", "hard",
        r"After a $10\%$ increase, the price of an item is $\$66$. What was"
        r" the original price, in dollars?",
        ["60"],
        r"The new price is $110\%$ of the original $p$:"
        r" $$1.10\,p = 66 \;\Rightarrow\; p = \frac{66}{1.1} = 60.$$",
        ["Eq(Rational(11, 10)*60, 66)"]))

    # Q20 H advanced_math polynomial remainder
    assert (2 ** 3 - 4 * 2 + 1) == 1
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q20", M, 20, "advanced_math", "polynomials", "hard",
        r"When the polynomial $p(x) = x^3 - 4x + 1$ is divided by $x - 2$,"
        r" what is the remainder?",
        r"By the remainder theorem, the remainder is $p(2)$:"
        r" $$2^3 - 4(2) + 1 = 8 - 8 + 1 = 1.$$"
        r" Using $x = -2$ gives $-8 + 8 + 1 = 1$... evaluating $p(-2)$"
        r" carelessly gives $-15$; dropping the constant gives 0; using"
        r" $x = 2$ but squaring wrong gives 5."
        r" The correct answer is **B**.",
        ["Eq(2**3 - 4*2 + 1, 1)"],
        1, {-15: "used x equals negative 2", 0: "dropped the constant",
            5: "arithmetic slip"}))

    # Q21 H advanced_math absolute value equation count/solution
    assert abs(2 * 5 - 3) == 7 and abs(2 * (-2) - 3) == 7 and 5 + (-2) == 3
    qs.append(mcq_numeric(
        "SAT-P5-M2H-Q21", M, 21, "advanced_math", "absolute_value", "hard",
        r"What is the sum of all solutions to $|2x - 3| = 7$?",
        r"Split into two cases: $2x - 3 = 7$ gives $x = 5$, and"
        r" $2x - 3 = -7$ gives $x = -2$:"
        r" $$5 + (-2) = 3.$$"
        r" Taking only the positive case gives 5; only the negative case"
        r" gives $-2$; adding the case constants gives 0."
        r" The correct answer is **C**.",
        ["Eq(5 + (-2), 3)", "Eq(abs(2*5 - 3), 7)", "Eq(abs(2*(-2) - 3), 7)"],
        3, {5: "used only the positive case", -2: "used only the negative case",
            0: "added the case constants"}))

    # Q22 H algebra SPR system word problem
    asym = symbols("a")
    bsym = symbols("b")
    sol22 = _solve([Eq(asym + bsym, 25), Eq(2 * asym + 4 * bsym, 74)],
                   [asym, bsym])
    assert sol22[asym] == 13
    qs.append(spr(
        "SAT-P5-M2H-Q22", M, 22, "algebra", "systems_linear", "hard",
        r"A parking lot holds $25$ vehicles that are all cars or trucks. The"
        r" cars have $2$ axles each and the trucks have $4$ axles each, for a"
        r" total of $74$ axles. How many cars are in the lot?",
        ["13"],
        r"With $a$ cars and $b$ trucks, $a + b = 25$ and $2a + 4b = 74$."
        r" Substituting $b = 25 - a$:"
        r" $$2a + 4(25 - a) = 74 \;\Rightarrow\; -2a + 100 = 74"
        r" \;\Rightarrow\; a = 13.$$",
        ["Eq(13 + 12, 25)", "Eq(2*13 + 4*12, 74)"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-5.json",
               {"testId": "sat-practice-5",
                "label": "SAT Math Practice Test 5",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
