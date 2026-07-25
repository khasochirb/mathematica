#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 10 (data/sat/sat-practice-10.json).

Built on scripts/test-builders/satbuild.py. Archetypes audited against
tests 1-9; new to the bank here:
  * a circle's centre read from the standard-form equation
  * a compound inequality solved as a single chain
  * the minimum value of a quadratic via completing the square
  * arc length from a central angle; the cone/cylinder volume ratio
  * similar SOLIDS (the cube of the linear ratio, not the square)
  * the factor theorem used to recover a missing coefficient
  * the value that makes a seventh data point move the mean by 1
  * the sum of the roots of a quadratic read off the coefficients
  * a system that has NO solution, solved for the parameter
  * a half-life model solved for the elapsed time
  * f(f(x)) composition, log-sum equations, and a two-power exponential
  * (x + y)^2 recovered from x^2 + y^2 and xy

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

from sympy import Eq, Rational, expand, simplify, sqrt, symbols
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
    fr = Fraction(v)
    if fr.denominator == 1:
        return f"${fr.numerator}$"
    if 10 % fr.denominator == 0 or 100 % fr.denominator == 0:
        return dec(v)
    return frac(v)


def money(v) -> str:
    return rf"$\${float(Fraction(v)):g}$"


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E alg
    assert _solve(Eq(5 * x + 3, 38), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $5x + 3 = 38$, what is the value of $x$?",
        r"Subtract 3 from both sides, then divide by 5:"
        r" $$5x = 35 \;\Rightarrow\; x = 7.$$"
        r" Adding 3 instead gives $41/5 = 8.2$, and stopping at $5x = 35$"
        r" gives 35."
        r" The correct answer is **A**.",
        ["Eq(5*7 + 3, 38)", "Eq((38 - 3)/5, 7)"],
        7, {Rational(41, 5): "added 3 instead of subtracting",
            35: "stopped at 5x = 35",
            Rational(38, 5): "divided 38 by 5, ignoring the 3"},
        fmt=smart))

    # Q2 E adv — rational exponent as a radical
    assert (4 ** Rational(3, 2)) == 8 and sqrt(4 ** 3) == 8
    qs.append(mcq_listed(
        "SAT-P10-M1-Q02", M, 2, "advanced_math", "exponent_rules", "easy",
        r"For $x > 0$, which of the following is equivalent to"
        r" $x^{\frac{3}{2}}$?",
        {"A": r"$\sqrt[3]{x^2}$", "B": r"$\sqrt{x^3}$",
         "C": r"$3\sqrt{x}$", "D": r"$\dfrac{1}{\sqrt{x^3}}$"},
        "B",
        r"A fractional exponent puts the denominator in the root and the"
        r" numerator in the power: $x^{m/n} = \sqrt[n]{x^m}$. With"
        r" $m = 3$ and $n = 2$ this is $\sqrt{x^3}$. Checking at $x = 4$:"
        r" $$4^{3/2} = 8 \quad\text{and}\quad \sqrt{4^3} = \sqrt{64} = 8.$$"
        r" Reading the fraction upside down gives $\sqrt[3]{x^2}$, and a"
        r" negative exponent would be needed for the reciprocal form."
        r" The correct answer is **B**.",
        ["Eq(4**Rational(3,2), 8)", "Eq(sqrt(4**3), 8)",
         "Eq(9**Rational(3,2), 27)", "Ne(9**Rational(2,3), 27)"]))

    # Q3 E psda
    assert Rational(15, 100) * 240 == 36
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q03", M, 3, "psda", "percentages", "easy",
        r"A shop has 240 bicycles in stock, and $15\%$ of them are"
        r" electric. How many of the bicycles are electric?",
        r"Fifteen percent of 240 is"
        r" $$0.15 \times 240 = 36.$$"
        r" The remaining $85\%$, or 204 bicycles, are not electric —"
        r" that is the trap in one of the other choices."
        r" The correct answer is **B**.",
        ["Eq(Rational(15,100)*240, 36)", "Eq(240 - 36, 204)"],
        36, {15: "reported the percent itself as a count",
             204: "found the number that are NOT electric",
             1600: "divided 240 by 0.15 instead of multiplying"}))

    # Q4 E alg SPR
    assert Rational(16 - 4, 5 - 1) == 3
    qs.append(spr(
        "SAT-P10-M1-Q04", M, 4, "algebra", "linear_functions_slope", "easy",
        r"A line in the $xy$-plane passes through the points $(1, 4)$ and"
        r" $(5, 16)$. What is the slope of the line?",
        ["3"],
        r"Slope is the change in $y$ over the change in $x$:"
        r" $$m = \frac{16 - 4}{5 - 1} = \frac{12}{4} = 3.$$"
        r" Subtracting the coordinates in a consistent order matters — as"
        r" long as both differences start with the same point, the sign"
        r" comes out right.",
        ["Eq(Rational(16 - 4, 5 - 1), 3)", "Eq(Rational(4 - 16, 1 - 5), 3)"]))

    # Q5 E geo
    assert 180 - 47 - 68 == 65
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q05", M, 5, "geometry_trig", "triangle_angles", "easy",
        r"Two angles of a triangle measure $47^\circ$ and $68^\circ$."
        r" What is the measure, in degrees, of the third angle?",
        r"The three angles of a triangle sum to $180^\circ$:"
        r" $$180 - 47 - 68 = 65.$$"
        r" Adding the two given angles gives 115, and subtracting only one"
        r" of them gives 133 or 112."
        r" The correct answer is **A**.",
        ["Eq(180 - 47 - 68, 65)", "Eq(47 + 68 + 65, 180)"],
        65, {112: "subtracted only the 68 degree angle",
             115: "added the two given angles",
             133: "subtracted only the 47 degree angle"}))

    # Q6 E adv
    assert (-2) ** 2 - 3 * (-2) == 10
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q06", M, 6, "advanced_math", "function_notation", "easy",
        r"The function $f$ is defined by $f(x) = x^2 - 3x$. What is the"
        r" value of $f(-2)$?",
        r"Substitute $x = -2$, keeping both signs:"
        r" $$f(-2) = (-2)^2 - 3(-2) = 4 + 6 = 10.$$"
        r" Squaring a negative gives a positive, and subtracting a"
        r" negative adds. Missing either sign gives $4 - 6 = -2$ or"
        r" $-4 + 6 = 2$."
        r" The correct answer is **D**.",
        ["Eq((-2)**2 - 3*(-2), 10)", "Eq((-2)**2, 4)"],
        10, {-10: "made both sign errors at once",
             -2: "treated $-3(-2)$ as $-6$",
             2: "treated the square of -2 as -4"}))

    # Q7 E alg
    assert _solve(Eq(50 + 25 * x, 300), x) == [10]
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q07", M, 7, "algebra", "linear_models", "easy",
        r"A gym charges a one-time fee of $\$50$ plus $\$25$ for each"
        r" month of membership. After how many months will a member have"
        r" paid a total of $\$300$?",
        r"With $m$ months the total is $50 + 25m$, so"
        r" $$50 + 25m = 300 \;\Rightarrow\; 25m = 250 \;\Rightarrow\; m = 10.$$"
        r" Dividing 300 by 25 without removing the fee first gives 12, and"
        r" adding the fee instead of subtracting gives 14."
        r" The correct answer is **B**.",
        ["Eq(50 + 25*10, 300)", "Eq((300 - 50)/25, 10)"],
        10, {6: "divided 300 by 50", 12: "ignored the one-time fee",
             14: "added the fee instead of subtracting it"}))

    # Q8 E geo — centre from standard form
    assert (8 - 3) ** 2 + (-4 + 4) ** 2 == 25
    qs.append(mcq_listed(
        "SAT-P10-M1-Q08", M, 8, "geometry_trig", "circle_equations", "easy",
        r"In the $xy$-plane, a circle has equation"
        r" $(x - 3)^2 + (y + 4)^2 = 25$. What are the coordinates of the"
        r" centre of the circle?",
        {"A": r"$(-3, -4)$", "B": r"$(-3, 4)$",
         "C": r"$(3, -4)$", "D": r"$(3, 4)$"},
        "C",
        r"The standard form is $(x - h)^2 + (y - k)^2 = r^2$ with centre"
        r" $(h, k)$. Matching term by term,"
        r" $$x - h = x - 3 \;\Rightarrow\; h = 3, \qquad"
        r" y - k = y + 4 \;\Rightarrow\; k = -4.$$"
        r" So the centre is $(3, -4)$; as a check, the point $(8, -4)$"
        r" gives $(8-3)^2 + 0 = 25$, exactly the radius squared. Copying"
        r" the signs straight out of the parentheses gives $(-3, 4)$."
        r" The correct answer is **C**.",
        ["Eq((8 - 3)**2 + (-4 + 4)**2, 25)", "Eq(sqrt(25), 5)"]))

    # Q9 M adv SPR — discriminant
    assert _solve(Eq(x**2 - 4 * 1 * 9, 0), x) == [-6, 6]
    qs.append(spr(
        "SAT-P10-M1-Q09", M, 9, "advanced_math", "quadratic_discriminant",
        "medium",
        r"In the equation $x^2 + kx + 9 = 0$, $k$ is a positive constant"
        r" and the equation has exactly one real solution. What is the"
        r" value of $k$?",
        ["6"],
        r"A quadratic has exactly one real solution when its discriminant"
        r" is zero:"
        r" $$b^2 - 4ac = k^2 - 4(1)(9) = k^2 - 36 = 0.$$"
        r" So $k^2 = 36$ and $k = \pm 6$. The problem says $k$ is"
        r" positive, so $k = 6$. (Indeed $x^2 + 6x + 9 = (x+3)^2$, whose"
        r" only root is $x = -3$.)",
        ["Eq(6**2 - 4*1*9, 0)", "Eq(expand((x + 3)**2), x**2 + 6*x + 9)"]))

    # Q10 M psda — bar chart figure
    TICKETS = [10, 14, 16, 24, 26]
    assert sum(TICKETS) == 90 and Rational(90, 5) == 18
    assert sorted(TICKETS)[2] == 16
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q10", M, 10, "psda", "center_spread", "medium",
        r"The bar chart shows the number of tickets a theatre sold on each"
        r" of five days. What is the mean number of tickets sold per day?",
        r"Add the five values and divide by 5:"
        r" $$\frac{10 + 14 + 16 + 24 + 26}{5} = \frac{90}{5} = 18.$$"
        r" The median — the middle value once the days are ordered — is"
        r" 16, which is a different number and a common wrong pick here."
        r" The correct answer is **B**.",
        ["Eq(Rational(10 + 14 + 16 + 24 + 26, 5), 18)",
         "Eq(10 + 14 + 16 + 24 + 26, 90)"],
        18, {16: "reported the median instead of the mean",
             26: "reported the largest value",
             90: "reported the total instead of the mean"},
        fig=figure("sat-p10-m1-q10",
                   "Bar chart of tickets sold on Monday through Friday: "
                   "10, 14, 16, 24, and 26")))

    # Q11 M alg — compound inequality
    assert Rational(-3 - 5, 2) == -4 and Rational(11 - 5, 2) == 3
    qs.append(mcq_listed(
        "SAT-P10-M1-Q11", M, 11, "algebra", "linear_inequalities", "medium",
        r"Which of the following describes all values of $x$ that satisfy"
        r" $-3 < 2x + 5 \le 11$?",
        {"A": r"$-4 < x \le 3$", "B": r"$-4 \le x < 3$",
         "C": r"$-1 < x \le 8$", "D": r"$1 < x \le 8$"},
        "A",
        r"Work on all three parts of the chain at once. Subtract 5:"
        r" $$-8 < 2x \le 6.$$"
        r" Then divide by 2, which is positive, so no inequality signs"
        r" flip:"
        r" $$-4 < x \le 3.$$"
        r" The strict sign stays on the left and the inclusive sign stays"
        r" on the right — swapping them gives choice B. Dividing before"
        r" subtracting produces the intervals in C and D."
        r" The correct answer is **A**.",
        ["Eq(Rational(-3 - 5, 2), -4)", "Eq(Rational(11 - 5, 2), 3)",
         "-3 < 2*0 + 5", "2*3 + 5 <= 11"]))

    # Q12 M adv — completing the square
    assert expand((x - 4) ** 2 - 5) == x**2 - 8 * x + 11
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q12", M, 12, "advanced_math", "quadratic_vertex_form",
        "medium",
        r"What is the minimum value of the function"
        r" $f(x) = x^2 - 8x + 11$?",
        r"Complete the square. Half of $-8$ is $-4$, and $(-4)^2 = 16$:"
        r" $$f(x) = (x^2 - 8x + 16) - 16 + 11 = (x - 4)^2 - 5.$$"
        r" A square is never negative, so $f(x)$ is smallest when"
        r" $(x-4)^2 = 0$, that is at $x = 4$, and the minimum value is"
        r" $-5$. Reporting the $x$-value 4 instead of the output, or"
        r" reading off the constant 11, are the two common slips."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 4)**2 - 5), x**2 - 8*x + 11)",
         "Eq(4**2 - 8*4 + 11, -5)"],
        -5, {-4: "reported the x-value of the vertex",
             5: "dropped the sign when completing the square",
             11: "read off the constant term"}))

    # Q13 M geo — arc length
    assert Rational(40, 360) * 2 * 9 == 2
    qs.append(mcq_listed(
        "SAT-P10-M1-Q13", M, 13, "geometry_trig", "circle_arcs_sectors",
        "medium",
        r"A circle has radius 9. What is the length of an arc of this"
        r" circle that is intercepted by a central angle of"
        r" $40^\circ$?",
        {"A": r"$\pi$", "B": r"$2\pi$", "C": r"$4\pi$", "D": r"$9\pi$"},
        "B",
        r"An arc is the same fraction of the circumference that its"
        r" central angle is of a full turn:"
        r" $$\text{arc} = \frac{40}{360}\cdot 2\pi(9)"
        r" = \frac{1}{9}\cdot 18\pi = 2\pi.$$"
        r" Using the radius instead of the circumference gives"
        r" $\frac{1}{9}(9\pi) = \pi$, choice A."
        r" The correct answer is **B**.",
        ["Eq(Rational(40,360)*2*9, 2)", "Eq(2*9, 18)",
         "Eq(Rational(40,360), Rational(1,9))"]))

    # Q14 M psda SPR — the seventh value that lifts the mean by 1
    assert 7 * 15 - 6 * 14 == 21
    qs.append(spr(
        "SAT-P10-M1-Q14", M, 14, "psda", "center_spread", "medium",
        r"The mean of a list of 6 numbers is 14. When a seventh number is"
        r" added to the list, the mean of the 7 numbers is 15. What is"
        r" the seventh number?",
        ["21"],
        r"A mean tells you the total. The first six numbers sum to"
        r" $$6 \times 14 = 84,$$"
        r" and all seven numbers sum to"
        r" $$7 \times 15 = 105.$$"
        r" The new number is the difference:"
        r" $$105 - 84 = 21.$$"
        r" Notice it is not 15 — to pull the mean up by 1 across seven"
        r" values, the new number must clear the old mean by 7.",
        ["Eq(6*14, 84)", "Eq(7*15, 105)", "Eq(105 - 84, 21)",
         "Eq(Rational(84 + 21, 7), 15)"]))

    # Q15 M alg — literal equation
    assert Rational(5, 9) * (212 - 32) == 100
    qs.append(mcq_listed(
        "SAT-P10-M1-Q15", M, 15, "algebra", "literal_equations", "medium",
        r"The formula $C = \dfrac{5}{9}(F - 32)$ converts a temperature"
        r" $F$ in degrees Fahrenheit to the temperature $C$ in degrees"
        r" Celsius. Which equation correctly gives $F$ in terms of $C$?",
        {"A": r"$F = \dfrac{9}{5}C + 32$", "B": r"$F = \dfrac{9}{5}(C + 32)$",
         "C": r"$F = \dfrac{5}{9}C + 32$",
         "D": r"$F = \dfrac{9C - 32}{5}$"},
        "A",
        r"Undo the operations in reverse order. Multiply both sides by"
        r" $\frac{9}{5}$:"
        r" $$\frac{9}{5}C = F - 32.$$"
        r" Then add 32 to both sides:"
        r" $$F = \frac{9}{5}C + 32.$$"
        r" Check with boiling water: $C = 100$ gives"
        r" $\frac{9}{5}(100) + 32 = 212$, which is correct. Multiplying"
        r" the 32 by $\frac{9}{5}$ as well produces choice B."
        r" The correct answer is **A**.",
        ["Eq(Rational(5,9)*(212 - 32), 100)",
         "Eq(Rational(9,5)*100 + 32, 212)",
         "Ne(Rational(9,5)*(100 + 32), 212)"]))

    # Q16 M adv — factor theorem
    assert 3**2 + 2 * 3 - 15 == 0
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q16", M, 16, "advanced_math", "polynomial_factors",
        "medium",
        r"In the polynomial $f(x) = x^2 + bx - 15$, $b$ is a constant. If"
        r" $x - 3$ is a factor of $f(x)$, what is the value of $b$?",
        r"If $x - 3$ is a factor, then $f(3) = 0$:"
        r" $$3^2 + 3b - 15 = 0 \;\Rightarrow\; 3b - 6 = 0 \;\Rightarrow\; b = 2.$$"
        r" Indeed $x^2 + 2x - 15 = (x - 3)(x + 5)$. Using the root"
        r" $x = -3$ by mistake gives $b = -2$, and forgetting to divide"
        r" the last step by 3 gives 6."
        r" The correct answer is **C**.",
        ["Eq(3**2 + 2*3 - 15, 0)",
         "Eq(expand((x - 3)*(x + 5)), x**2 + 2*x - 15)"],
        2, {-8: "kept the constant positive when substituting",
            -2: "substituted $x = -3$ instead of $x = 3$",
            6: "solved $3b = 6$ without dividing by 3"}))

    # Q17 M adv — rational equation
    assert _solve(Eq((x + 4) / (x - 2), 3), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q17", M, 17, "advanced_math", "rational_equations",
        "medium",
        r"If $\dfrac{x + 4}{x - 2} = 3$ and $x \ne 2$, what is the value"
        r" of $x$?",
        r"Multiply both sides by $x - 2$ and distribute the 3 across"
        r" BOTH terms:"
        r" $$x + 4 = 3(x - 2) = 3x - 6.$$"
        r" Collect the $x$ terms:"
        r" $$10 = 2x \;\Rightarrow\; x = 5.$$"
        r" Checking, $\frac{5 + 4}{5 - 2} = \frac{9}{3} = 3$."
        r" Distributing to only the first term gives $x + 4 = 3x - 2$ and"
        r" the answer 3."
        r" The correct answer is **D**.",
        ["Eq((5 + 4)/(5 - 2), 3)", "Eq(3*(5 - 2), 9)"],
        5, {-1: "wrote $3(x - 2)$ as $3x + 6$",
            2: "divided 4 by 2", 3: "distributed the 3 to only one term"}))

    # Q18 H alg SPR — parameter forcing NO solution
    assert Rational(-9, 3) == Rational(15, -5)
    qs.append(spr(
        "SAT-P10-M1-Q18", M, 18, "algebra", "systems_no_solution", "hard",
        r"$$3x - 5y = 8$$"
        r"$$kx + 15y = 4$$"
        r"In the system of equations above, $k$ is a constant. If the"
        r" system has no solution, what is the value of $k$?",
        ["-9"],
        r"Two lines fail to meet exactly when they are parallel but not"
        r" identical — the coefficients are proportional while the"
        r" constants are not. Set the coefficient ratios equal:"
        r" $$\frac{k}{3} = \frac{15}{-5} = -3 \;\Rightarrow\; k = -9.$$"
        r" Check: the second equation becomes $-9x + 15y = 4$, which is"
        r" $-3$ times the left side of the first equation. Multiplying the"
        r" first equation by $-3$ would give $-9x + 15y = -24$, and"
        r" $-24 \ne 4$, so the lines are parallel and distinct — no"
        r" solution, as required.",
        ["Eq(Rational(-9, 3), -3)", "Eq(Rational(15, -5), -3)",
         "Eq(-3*8, -24)", "Ne(-24, 4)"]))

    # Q19 H psda — two-way table figure, conditional probability
    CELLS = [[34, 26], [21, 39]]
    assert sum(sum(r) for r in CELLS) == 120
    assert CELLS[0][1] + CELLS[1][1] == 65
    assert Rational(39, 65) == Rational(3, 5)
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q19", M, 19, "psda", "two_way_tables", "hard",
        r"The table shows the responses of 120 students to a survey"
        r" question. If one of the students who answered No is selected"
        r" at random, what is the probability that the student is a"
        r" senior?",
        r"The condition — the student answered No — restricts attention to"
        r" the No COLUMN, whose total is"
        r" $$26 + 39 = 65.$$"
        r" Of those 65 students, 39 are seniors, so the probability is"
        r" $$\frac{39}{65} = \frac{3}{5}.$$"
        r" Dividing by the grand total 120 gives $\frac{13}{40}$, and"
        r" dividing by the senior ROW total of 60 gives $\frac{13}{20}$ —"
        r" both answer a different question."
        r" The correct answer is **C**.",
        ["Eq(26 + 39, 65)", "Eq(Rational(39, 65), Rational(3,5))",
         "Eq(34 + 26 + 21 + 39, 120)", "Eq(Rational(39, 120), Rational(13,40))",
         "Eq(Rational(39, 60), Rational(13,20))"],
        Rational(3, 5),
        {Rational(13, 40): "divided by the grand total of 120",
         Rational(13, 24): "found the probability of answering No",
         Rational(13, 20): "divided by the senior row total of 60"},
        fmt=frac,
        fig=figure("sat-p10-m1-q19",
                   "Two-way table of survey responses Yes and No by class, "
                   "juniors 34 and 26, seniors 21 and 39")))

    # Q20 H geo — similar solids
    assert Rational(3, 2) ** 3 * 24 == 81
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q20", M, 20, "geometry_trig", "similar_solids", "hard",
        r"Two similar cones have radii in the ratio $2 : 3$. The volume of"
        r" the smaller cone is $24$ cubic centimetres. What is the volume,"
        r" in cubic centimetres, of the larger cone?",
        r"For similar solids, every length scales by $k$, so every volume"
        r" scales by $k^3$. Here $k = \frac{3}{2}$, giving"
        r" $$V = 24 \cdot \left(\frac{3}{2}\right)^3"
        r" = 24 \cdot \frac{27}{8} = 81.$$"
        r" Scaling by the linear ratio $\frac{3}{2}$ gives 36 and scaling"
        r" by the area ratio $\frac{9}{4}$ gives 54 — those are the"
        r" surface-area and length rules, not the volume rule."
        r" The correct answer is **D**.",
        ["Eq(Rational(3,2)**3 * 24, 81)", "Eq(Rational(3,2)**2 * 24, 54)",
         "Eq(Rational(3,2) * 24, 36)"],
        81, {36: "scaled by the linear ratio",
             54: "scaled by the square of the ratio",
             72: "tripled the volume"}))

    # Q21 H adv SPR — half-life
    assert 800 * Rational(1, 2) ** Rational(36, 12) == 100
    qs.append(spr(
        "SAT-P10-M1-Q21", M, 21, "advanced_math", "exponential_models",
        "hard",
        r"A sample of a radioactive substance decays so that the amount"
        r" remaining after $t$ years is modelled by"
        r" $$A(t) = 800\left(\frac{1}{2}\right)^{\frac{t}{12}},$$"
        r" where $A(t)$ is measured in milligrams. After how many years"
        r" will 100 milligrams remain?",
        ["36"],
        r"Set the model equal to 100 and divide by the initial amount:"
        r" $$\left(\frac{1}{2}\right)^{t/12} = \frac{100}{800}"
        r" = \frac{1}{8}.$$"
        r" Since $\frac{1}{8} = \left(\frac{1}{2}\right)^3$, the exponents"
        r" must match:"
        r" $$\frac{t}{12} = 3 \;\Rightarrow\; t = 36.$$"
        r" In words: the exponent $t/12$ counts half-lives, the sample"
        r" must halve three times to fall from 800 to 100, and each"
        r" halving takes 12 years.",
        ["Eq(Rational(100, 800), Rational(1,8))",
         "Eq(Rational(1,2)**3, Rational(1,8))",
         "Eq(800*Rational(1,2)**Rational(36,12), 100)"]))

    # Q22 H alg — absolute value, sum of solutions
    assert abs(2 * 6 - 7) == 5 and abs(2 * 1 - 7) == 5
    qs.append(mcq_numeric(
        "SAT-P10-M1-Q22", M, 22, "algebra", "absolute_value", "hard",
        r"What is the sum of all values of $x$ that satisfy"
        r" $|2x - 7| = 5$?",
        r"An absolute value equals 5 when the inside is $5$ or $-5$, so"
        r" split into two cases:"
        r" $$2x - 7 = 5 \;\Rightarrow\; x = 6,$$"
        r" $$2x - 7 = -5 \;\Rightarrow\; x = 1.$$"
        r" Both check: $|12 - 7| = 5$ and $|2 - 7| = 5$. Their sum is"
        r" $$6 + 1 = 7.$$"
        r" Solving only the positive case gives 6, which is the most"
        r" common wrong answer here."
        r" The correct answer is **C**.",
        ["Eq(Abs(2*6 - 7), 5)", "Eq(Abs(2*1 - 7), 5)", "Eq(6 + 1, 7)"],
        7, {1: "reported only the smaller solution",
            6: "reported only the larger solution",
            12: "doubled the larger solution"}))

    return qs


# ─── Module 2, easier form (11E / 9M / 2H) ────────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg
    assert _solve(Eq(x / 4, 9), x) == [36]
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $\dfrac{x}{4} = 9$, what is the value of $x$?",
        r"Multiply both sides by 4:"
        r" $$x = 9 \times 4 = 36.$$"
        r" Dividing by 4 instead gives $2.25$, and treating the fraction"
        r" bar as a subtraction gives 13."
        r" The correct answer is **D**.",
        ["Eq(Rational(36, 4), 9)", "Eq(9*4, 36)"],
        36, {Rational(9, 4): "divided by 4 instead of multiplying",
             5: "subtracted 4 from 9", 13: "added 4 to 9"},
        fmt=smart))

    # Q2 E adv
    assert expand((x + 6) * (x - 2)) == x**2 + 4 * x - 12
    qs.append(mcq_listed(
        "SAT-P10-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $(x + 6)(x - 2)$?",
        {"A": r"$x^2 - 4x - 12$", "B": r"$x^2 + 4x - 12$",
         "C": r"$x^2 + 4x + 12$", "D": r"$x^2 + 8x - 12$"},
        "B",
        r"Multiply each term of the first factor by each term of the"
        r" second:"
        r" $$x \cdot x + x(-2) + 6x + 6(-2) = x^2 - 2x + 6x - 12.$$"
        r" Combining the middle terms gives"
        r" $$x^2 + 4x - 12.$$"
        r" The middle coefficient is $6 - 2 = 4$, not $6 + 2 = 8$, and the"
        r" constant is negative because the signs of 6 and $-2$ differ."
        r" The correct answer is **B**.",
        ["Eq(expand((x + 6)*(x - 2)), x**2 + 4*x - 12)",
         "Eq(6 + (-2), 4)", "Eq(6*(-2), -12)"]))

    # Q3 E psda SPR
    assert Rational(3, 12) * 28 == 7
    qs.append(spr(
        "SAT-P10-M2E-Q03", M, 3, "psda", "ratios_rates_proportions", "easy",
        r"A recipe uses 3 cups of flour to make 12 cookies. At this rate,"
        r" how many cups of flour are needed to make 28 cookies?",
        ["7"],
        r"Find the flour per cookie first:"
        r" $$\frac{3 \text{ cups}}{12 \text{ cookies}}"
        r" = \frac{1}{4}\text{ cup per cookie}.$$"
        r" Then scale up to 28 cookies:"
        r" $$28 \times \frac{1}{4} = 7 \text{ cups}.$$",
        ["Eq(Rational(3, 12), Rational(1,4))",
         "Eq(28*Rational(1,4), 7)"]))

    # Q4 E alg
    assert 3 * 4 - 5 == 7
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q04", M, 4, "algebra", "linear_functions_evaluate",
        "easy",
        r"If $y = 3x - 5$, what is the value of $y$ when $x = 4$?",
        r"Substitute $x = 4$:"
        r" $$y = 3(4) - 5 = 12 - 5 = 7.$$"
        r" Adding 5 instead of subtracting gives 17, and dropping the"
        r" $-5$ altogether gives 12."
        r" The correct answer is **B**.",
        ["Eq(3*4 - 5, 7)"],
        7, {-7: "computed $5 - 3x$", 12: "ignored the $-5$",
            17: "added 5 instead of subtracting"}))

    # Q5 E geo
    assert 12**2 + 5**2 == 13**2
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q05", M, 5, "geometry_trig", "pythagorean_theorem",
        "easy",
        r"A rectangle has length 12 and width 5. What is the length of a"
        r" diagonal of the rectangle?",
        r"A diagonal splits the rectangle into two right triangles whose"
        r" legs are the length and the width:"
        r" $$d^2 = 12^2 + 5^2 = 144 + 25 = 169 \;\Rightarrow\; d = 13.$$"
        r" Adding the sides gives 17, the perimeter is 34, and the area is"
        r" 60 — none of those is a length across the rectangle."
        r" The correct answer is **A**.",
        ["Eq(12**2 + 5**2, 169)", "Eq(sqrt(169), 13)"],
        13, {17: "added the two side lengths",
             34: "computed the perimeter", 60: "computed the area"}))

    # Q6 E adv
    assert 2 * 3**2 + 1 == 19
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q06", M, 6, "advanced_math", "function_notation",
        "easy",
        r"The function $f$ is defined by $f(x) = 2x^2 + 1$. What is the"
        r" value of $f(3)$?",
        r"Square first, then multiply, then add — that is the order of"
        r" operations:"
        r" $$f(3) = 2(3)^2 + 1 = 2(9) + 1 = 19.$$"
        r" Squaring $2x$ instead of just $x$ gives $6^2 + 1 = 37$, and"
        r" dropping the coefficient gives $9 + 1 = 10$."
        r" The correct answer is **C**.",
        ["Eq(2*3**2 + 1, 19)", "Eq((2*3)**2 + 1, 37)"],
        19, {7: "multiplied before squaring, as $2(3) + 1$",
             10: "dropped the coefficient 2",
             37: "squared $2x$ instead of $x$"}))

    # Q7 E alg SPR
    assert _solve(Eq(2 * x + 4, 10), x) == [3]
    qs.append(spr(
        "SAT-P10-M2E-Q07", M, 7, "algebra", "linear_functions_slope", "easy",
        r"The line $y = mx + 4$ passes through the point $(2, 10)$. What"
        r" is the value of $m$?",
        ["3"],
        r"A point on the line makes the equation true, so substitute"
        r" $x = 2$ and $y = 10$:"
        r" $$10 = m(2) + 4.$$"
        r" Subtract 4 and divide by 2:"
        r" $$2m = 6 \;\Rightarrow\; m = 3.$$",
        ["Eq(3*2 + 4, 10)", "Eq((10 - 4)/2, 3)"]))

    # Q8 E adv
    assert Rational(12 * 2**5, 3 * 2**2) == 4 * 2**3
    qs.append(mcq_listed(
        "SAT-P10-M2E-Q08", M, 8, "advanced_math", "exponent_rules", "easy",
        r"For $x \ne 0$, which of the following is equivalent to"
        r" $\dfrac{12x^5}{3x^2}$?",
        {"A": r"$4x^3$", "B": r"$4x^7$", "C": r"$9x^3$", "D": r"$36x^7$"},
        "A",
        r"Divide the coefficients and subtract the exponents:"
        r" $$\frac{12}{3} = 4, \qquad x^{5 - 2} = x^3,$$"
        r" so the quotient is $4x^3$. Testing $x = 2$ confirms it:"
        r" $\frac{12(32)}{3(4)} = \frac{384}{12} = 32 = 4(8)$. Adding the"
        r" exponents gives $x^7$, and subtracting the coefficients gives"
        r" 9."
        r" The correct answer is **A**.",
        ["Eq(Rational(12*2**5, 3*2**2), 32)", "Eq(4*2**3, 32)",
         "Eq(5 - 2, 3)"]))

    # Q9 E alg
    assert _solve(Eq(5 * (x - 3), 20), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q09", M, 9, "algebra", "linear_equations_one_var",
        "easy",
        r"If $5(x - 3) = 20$, what is the value of $x$?",
        r"Divide both sides by 5 first — it keeps the numbers small:"
        r" $$x - 3 = 4 \;\Rightarrow\; x = 7.$$"
        r" Distributing only to the $x$ gives $5x - 3 = 20$ and the answer"
        r" $4.6$; forgetting to divide by 5 at all gives 23."
        r" The correct answer is **C**.",
        ["Eq(5*(7 - 3), 20)", "Eq(Rational(20, 5) + 3, 7)"],
        7, {4: "ignored the $-3$",
            Rational(23, 5): "distributed the 5 only to $x$",
            23: "forgot to divide by 5"},
        fmt=smart))

    # Q10 E geo
    assert 5**3 == 125 and 6 * 5**2 == 150
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q10", M, 10, "geometry_trig", "solids_volume_surface",
        "easy",
        r"The volume of a cube is 125 cubic centimetres. What is the"
        r" surface area, in square centimetres, of the cube?",
        r"The edge length is the cube root of the volume:"
        r" $$s = \sqrt[3]{125} = 5.$$"
        r" A cube has 6 square faces, each of area $s^2$:"
        r" $$6(5)^2 = 6(25) = 150.$$"
        r" One face alone is 25, and multiplying the VOLUME by 6 gives"
        r" 750 — a units mismatch, since surface area is measured in"
        r" square centimetres."
        r" The correct answer is **C**.",
        ["Eq(5**3, 125)", "Eq(6*5**2, 150)"],
        150, {25: "found the area of a single face",
              30: "computed $6s$ instead of $6s^2$",
              750: "multiplied the volume by 6"}))

    # Q11 E adv — horizontal shift
    assert (3 - 3) ** 2 == 0 and (3 + 3) ** 2 != 0
    qs.append(mcq_listed(
        "SAT-P10-M2E-Q11", M, 11, "advanced_math", "function_transformations",
        "easy",
        r"The graph of $y = f(x)$ is shifted 3 units to the right in the"
        r" $xy$-plane. Which of the following is an equation of the graph"
        r" after the shift?",
        {"A": r"$y = f(x) - 3$", "B": r"$y = f(x) + 3$",
         "C": r"$y = f(x + 3)$", "D": r"$y = f(x - 3)$"},
        "D",
        r"Horizontal shifts act INSIDE the function and run opposite to"
        r" the sign: replacing $x$ by $x - 3$ moves the graph 3 units"
        r" right. To see why, take $f(x) = x^2$, whose lowest point is at"
        r" $x = 0$. For $y = f(x - 3) = (x-3)^2$ the lowest point is where"
        r" $$x - 3 = 0 \;\Rightarrow\; x = 3,$$"
        r" which is 3 units to the right. Adding 3 outside the function"
        r" would shift the graph up instead."
        r" The correct answer is **D**.",
        ["Eq((3 - 3)**2, 0)", "Ne((3 + 3)**2, 0)", "Eq((0 - 3)**2, 9)"]))

    # Q12 M alg SPR
    assert 26 + 28 + 30 == 84
    qs.append(spr(
        "SAT-P10-M2E-Q12", M, 12, "algebra", "linear_word_problems",
        "medium",
        r"The sum of three consecutive even integers is 84. What is the"
        r" largest of the three integers?",
        ["30"],
        r"Call the smallest integer $n$; the next two even integers are"
        r" $n + 2$ and $n + 4$. Then"
        r" $$n + (n + 2) + (n + 4) = 3n + 6 = 84.$$"
        r" So $3n = 78$ and $n = 26$, making the three integers 26, 28,"
        r" and 30. The largest is 30. (A quick check: their sum is"
        r" $26 + 28 + 30 = 84$.)",
        ["Eq(3*26 + 6, 84)", "Eq(26 + 28 + 30, 84)"]))

    # Q13 M adv
    assert 2**5 == 32 and 2**6 == 64
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q13", M, 13, "advanced_math", "exponential_models",
        "medium",
        r"The function $h$ is defined by $h(x) = 2^x$. If $h(a) = 32$,"
        r" what is the value of $h(a + 1)$?",
        r"Increasing the exponent by 1 multiplies the output by the base:"
        r" $$h(a + 1) = 2^{a + 1} = 2^a \cdot 2 = 32 \times 2 = 64.$$"
        r" You never need to find $a$ itself (though $a = 5$). Adding 1 to"
        r" the OUTPUT gives 33, and squaring gives 1024 — that would be"
        r" $h(2a)$."
        r" The correct answer is **B**.",
        ["Eq(2**5, 32)", "Eq(2**6, 64)", "Eq(32*2, 64)"],
        64, {33: "added 1 to the output instead of the exponent",
             128: "multiplied by 2 twice",
             1024: "squared the output"}))

    # Q14 M psda
    assert Rational(4 + 7 + 7 + 9 + 13, 5) == 8
    qs.append(mcq_listed(
        "SAT-P10-M2E-Q14", M, 14, "psda", "center_spread", "medium",
        r"Consider the data set $4,\ 7,\ 7,\ 9,\ 13$. Which of the"
        r" following statements about this data set is true?",
        {"A": r"The mean is less than the median.",
         "B": r"The mean is equal to the median.",
         "C": r"The mean is greater than the median.",
         "D": r"The mode is greater than the mean."},
        "C",
        r"The values are already in order, so the median is the middle"
        r" one:"
        r" $$\text{median} = 7.$$"
        r" The mean is the total divided by the count:"
        r" $$\frac{4 + 7 + 7 + 9 + 13}{5} = \frac{40}{5} = 8.$$"
        r" Since $8 > 7$, the mean exceeds the median — the single large"
        r" value 13 pulls the mean to the right while leaving the median"
        r" untouched. The mode is 7, which is less than the mean, so D is"
        r" false."
        r" The correct answer is **C**.",
        ["Eq(Rational(4 + 7 + 7 + 9 + 13, 5), 8)", "8 > 7",
         "Eq(4 + 7 + 7 + 9 + 13, 40)"]))

    # Q15 M alg SPR
    assert Rational(73 - 45, 1) / Rational(2, 10) == 140
    qs.append(spr(
        "SAT-P10-M2E-Q15", M, 15, "algebra", "linear_models", "medium",
        r"A car rental costs $\$45$ plus $\$0.20$ for each mile driven."
        r" A customer's total charge was $\$73$. How many miles did the"
        r" customer drive?",
        ["140"],
        r"Let $m$ be the number of miles. The total charge is"
        r" $$45 + 0.20m = 73.$$"
        r" Subtract the flat fee:"
        r" $$0.20m = 28.$$"
        r" Divide by $0.20$:"
        r" $$m = \frac{28}{0.20} = 140.$$"
        r" Dividing 73 by $0.20$ without removing the fee first would give"
        r" 365, far too many miles.",
        ["Eq(45 + Rational(2,10)*140, 73)",
         "Eq(Rational(28)/Rational(2,10), 140)"]))

    # Q16 M adv — sum of roots
    assert _solve(Eq(x**2 - 9 * x + 14, 0), x) == [2, 7]
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q16", M, 16, "advanced_math", "quadratic_equations",
        "medium",
        r"What is the sum of the solutions of $x^2 - 9x + 14 = 0$?",
        r"Factor: two numbers multiplying to 14 and adding to $-9$ are"
        r" $-2$ and $-7$, so"
        r" $$x^2 - 9x + 14 = (x - 2)(x - 7) = 0,$$"
        r" giving $x = 2$ and $x = 7$. Their sum is"
        r" $$2 + 7 = 9.$$"
        r" You can also read it straight off the coefficients: the sum of"
        r" the roots is $-b/a = 9$ and the product is $c/a = 14$, which is"
        r" the trap in the largest choice."
        r" The correct answer is **C**.",
        ["Eq(expand((x - 2)*(x - 7)), x**2 - 9*x + 14)", "Eq(2 + 7, 9)",
         "Eq(2*7, 14)"],
        9, {2: "gave only the smaller solution",
            7: "gave only the larger solution",
            14: "gave the product of the solutions"}))

    # Q17 M geo — right-triangle trig ratio
    assert 5**2 + 12**2 == 13**2
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q17", M, 17, "geometry_trig", "right_triangle_trig",
        "medium",
        r"In right triangle $ABC$, the right angle is at $C$, the"
        r" hypotenuse $AB$ has length 13, and side $BC$ has length 5."
        r" What is the value of $\sin A$?",
        r"The sine of an angle is the side opposite it over the"
        r" hypotenuse. The side opposite $A$ is $BC = 5$, and the"
        r" hypotenuse is $AB = 13$, so"
        r" $$\sin A = \frac{5}{13}.$$"
        r" The third side is $AC = \sqrt{169 - 25} = 12$, so"
        r" $\cos A = \frac{12}{13}$ and $\tan A = \frac{5}{12}$ — the two"
        r" ratios that are easiest to grab by mistake."
        r" The correct answer is **A**.",
        ["Eq(5**2 + 12**2, 13**2)", "Eq(sqrt(169 - 25), 12)"],
        Rational(5, 13),
        {Rational(5, 12): "used the tangent ratio",
         Rational(12, 13): "used the cosine ratio",
         Rational(13, 5): "inverted the ratio"},
        fmt=frac))

    # Q18 M alg
    assert 1 - (-2) * 3 == 7
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q18", M, 18, "algebra", "linear_functions_slope",
        "medium",
        r"A line in the $xy$-plane has slope $-2$ and passes through the"
        r" point $(3, 1)$. What is the $y$-coordinate of the"
        r" $y$-intercept of the line?",
        r"Start from $y = mx + b$ with $m = -2$ and substitute the point:"
        r" $$1 = -2(3) + b = -6 + b.$$"
        r" Add 6 to both sides:"
        r" $$b = 7.$$"
        r" So the line is $y = -2x + 7$, and its $y$-intercept is"
        r" $(0, 7)$. Using $+2$ for the slope gives $-5$, and swapping the"
        r" coordinates of the point gives 5."
        r" The correct answer is **D**.",
        ["Eq(1, -2*3 + 7)", "Eq(-2*0 + 7, 7)"],
        7, {-5: "used a slope of $+2$", -2: "reported the slope",
            5: "swapped the coordinates of the point"}))

    # Q19 M adv SPR
    assert 3 ** (2 + 2) == 81
    qs.append(spr(
        "SAT-P10-M2E-Q19", M, 19, "advanced_math", "exponent_equations",
        "medium",
        r"If $3^{x + 2} = 81$, what is the value of $x$?",
        ["2"],
        r"Write both sides as powers of the same base. Since"
        r" $81 = 3^4$,"
        r" $$3^{x + 2} = 3^4.$$"
        r" With equal bases the exponents must be equal:"
        r" $$x + 2 = 4 \;\Rightarrow\; x = 2.$$"
        r" Checking, $3^{2 + 2} = 3^4 = 81$.",
        ["Eq(3**4, 81)", "Eq(3**(2 + 2), 81)"]))

    # Q20 M psda
    assert Rational(5 + 4, 5 + 3 + 4) == Rational(3, 4)
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q20", M, 20, "psda", "probability", "medium",
        r"A bag contains 5 red marbles, 3 blue marbles, and 4 green"
        r" marbles. If one marble is selected at random, what is the"
        r" probability that it is NOT blue?",
        r"There are $5 + 3 + 4 = 12$ marbles in total, and $12 - 3 = 9$"
        r" of them are not blue, so"
        r" $$P(\text{not blue}) = \frac{9}{12} = \frac{3}{4}.$$"
        r" Equivalently, $1 - P(\text{blue}) = 1 - \frac{3}{12}"
        r" = \frac{3}{4}$. Answering with $P(\text{blue}) = \frac{1}{4}$"
        r" is the word-reversal trap."
        r" The correct answer is **D**.",
        ["Eq(5 + 3 + 4, 12)", "Eq(Rational(9, 12), Rational(3,4))",
         "Eq(1 - Rational(3,12), Rational(3,4))"],
        Rational(3, 4),
        {Rational(1, 4): "found the probability of blue",
         Rational(1, 3): "found the probability of green",
         Rational(5, 12): "found the probability of red"},
        fmt=frac))

    # Q21 H adv — composition with itself
    assert Rational(4 + 2, 4 - 1) == 2 and Rational(2 + 2, 2 - 1) == 4
    qs.append(mcq_numeric(
        "SAT-P10-M2E-Q21", M, 21, "advanced_math", "function_composition",
        "hard",
        r"The function $f$ is defined by $f(x) = \dfrac{x + 2}{x - 1}$ for"
        r" $x \ne 1$. What is the value of $f(f(4))$?",
        r"Work from the inside out. First,"
        r" $$f(4) = \frac{4 + 2}{4 - 1} = \frac{6}{3} = 2.$$"
        r" Then feed that result back in:"
        r" $$f(2) = \frac{2 + 2}{2 - 1} = \frac{4}{1} = 4.$$"
        r" So $f(f(4)) = 4$. Stopping after the first application gives 2,"
        r" and using only the numerator gives 6."
        r" The correct answer is **C**.",
        ["Eq(Rational(4 + 2, 4 - 1), 2)", "Eq(Rational(2 + 2, 2 - 1), 4)"],
        4, {2: "stopped after one application",
            3: "used the denominator of the first step",
            6: "used only the numerator of the first step"}))

    # Q22 H alg SPR — perfect square trinomial
    assert expand((x + 5) ** 2) == x**2 + 10 * x + 25
    qs.append(spr(
        "SAT-P10-M2E-Q22", M, 22, "algebra", "quadratic_discriminant",
        "hard",
        r"In the equation $x^2 + 10x + c = 0$, $c$ is a constant. If the"
        r" equation has exactly one real solution, what is the value of"
        r" $c$?",
        ["25"],
        r"Exactly one real solution means the discriminant is zero:"
        r" $$b^2 - 4ac = 10^2 - 4(1)c = 100 - 4c = 0.$$"
        r" So $4c = 100$ and $c = 25$. Equivalently, the left side must be"
        r" a perfect square, and"
        r" $$x^2 + 10x + 25 = (x + 5)^2,$$"
        r" whose only root is $x = -5$. Note $c$ is half of 10, then"
        r" squared — not half of 10.",
        ["Eq(10**2 - 4*1*25, 0)",
         "Eq(expand((x + 5)**2), x**2 + 10*x + 25)"]))

    return qs


# ─── Module 2, harder form (2E / 7M / 13H) ────────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg
    assert _solve(Eq(7 * x, 63), x) == [9]
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $7x = 63$, what is the value of $x + 5$?",
        r"First solve for $x$:"
        r" $$x = \frac{63}{7} = 9.$$"
        r" The question asks for $x + 5$, not $x$:"
        r" $$9 + 5 = 14.$$"
        r" Stopping at $x = 9$ is the trap; adding 5 to 63 before dividing"
        r" gives 68."
        r" The correct answer is **C**.",
        ["Eq(7*9, 63)", "Eq(9 + 5, 14)"],
        14, {4: "computed $x - 5$", 9: "stopped at the value of $x$",
             68: "added 5 to 63 instead of to $x$"}))

    # Q2 E adv
    assert (2 * 2**3) ** 2 == 4 * 2**6
    qs.append(mcq_listed(
        "SAT-P10-M2H-Q02", M, 2, "advanced_math", "exponent_rules", "easy",
        r"Which of the following is equivalent to $(2x^3)^2$?",
        {"A": r"$2x^5$", "B": r"$2x^6$", "C": r"$4x^5$", "D": r"$4x^6$"},
        "D",
        r"An outer exponent applies to EVERY factor inside the"
        r" parentheses:"
        r" $$(2x^3)^2 = 2^2 \cdot (x^3)^2 = 4x^6.$$"
        r" Powers of a power multiply, so $3 \times 2 = 6$, not"
        r" $3 + 2 = 5$; and the coefficient is squared too, so it is 4,"
        r" not 2. At $x = 2$: $(2 \cdot 8)^2 = 256 = 4(64)$."
        r" The correct answer is **D**.",
        ["Eq((2*2**3)**2, 256)", "Eq(4*2**6, 256)", "Eq(3*2, 6)"]))

    # Q3 M psda SPR — line of best fit prediction
    assert Rational(24, 10) * 25 + 15 == 75
    qs.append(spr(
        "SAT-P10-M2H-Q03", M, 3, "psda", "linear_models_fit", "medium",
        r"A scatterplot shows the relationship between the number of"
        r" hours $x$ a machine runs and the number of units $y$ it"
        r" produces. The line of best fit for the data is"
        r" $y = 2.4x + 15$. According to this model, how many units are"
        r" predicted when the machine runs for 25 hours?",
        ["75"],
        r"Substitute $x = 25$ into the model:"
        r" $$y = 2.4(25) + 15 = 60 + 15 = 75.$$"
        r" The slope $2.4$ is the predicted number of extra units per"
        r" additional hour, and the intercept 15 is the model's predicted"
        r" output at zero hours — both are needed here.",
        ["Eq(Rational(24,10)*25, 60)", "Eq(Rational(24,10)*25 + 15, 75)"]))

    # Q4 M alg
    _s4 = _solve([Eq(2 * x + y, 11), Eq(x - y, 4)], [x, y], dict=True)[0]
    assert _s4[x] == 5 and _s4[y] == 1
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q04", M, 4, "algebra", "systems_two_variables", "medium",
        r"$$2x + y = 11$$"
        r"$$x - y = 4$$"
        r"If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $x + 2y$?",
        r"Adding the two equations eliminates $y$ immediately:"
        r" $$3x = 15 \;\Rightarrow\; x = 5.$$"
        r" Substituting into the second equation gives"
        r" $$5 - y = 4 \;\Rightarrow\; y = 1.$$"
        r" The question asks for $x + 2y$, not for $x$ or $y$:"
        r" $$5 + 2(1) = 7.$$"
        r" Computing $x + y = 6$ instead is the intended slip."
        r" The correct answer is **C**.",
        ["Eq(2*5 + 1, 11)", "Eq(5 - 1, 4)", "Eq(5 + 2*1, 7)"],
        7, {4: "read off the right side of the second equation",
            6: "computed $x + y$",
            11: "read off the right side of the first equation"}))

    # Q5 M geo — similar triangles via perimeter
    assert Rational(27, 18) * 4 == 6
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q05", M, 5, "geometry_trig", "similar_triangles",
        "medium",
        r"Two similar triangles have perimeters 18 and 27. The shortest"
        r" side of the smaller triangle has length 4. What is the length"
        r" of the shortest side of the larger triangle?",
        r"In similar figures every length — including the perimeter —"
        r" scales by the same factor:"
        r" $$k = \frac{27}{18} = \frac{3}{2}.$$"
        r" So the corresponding shortest side is"
        r" $$4 \cdot \frac{3}{2} = 6.$$"
        r" Adding the perimeter difference $27 - 18 = 9$ to 4 gives 13,"
        r" which treats a proportional relationship as an additive one."
        r" The correct answer is **A**.",
        ["Eq(Rational(27, 18), Rational(3,2))",
         "Eq(4*Rational(3,2), 6)"],
        6, {9: "reported the perimeter difference",
            12: "tripled the side length",
            13: "added the perimeter difference to the side"}))

    # Q6 M adv
    assert 3**2 + (-5) == 4 and (-1) ** 2 + (-5) == -4
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q06", M, 6, "advanced_math", "function_notation",
        "medium",
        r"The function $f$ is defined by $f(x) = x^2 + k$, where $k$ is a"
        r" constant. If $f(3) = 4$, what is the value of $f(-1)$?",
        r"Use the given value to find $k$:"
        r" $$f(3) = 3^2 + k = 9 + k = 4 \;\Rightarrow\; k = -5.$$"
        r" So $f(x) = x^2 - 5$, and"
        r" $$f(-1) = (-1)^2 - 5 = 1 - 5 = -4.$$"
        r" Treating $(-1)^2$ as $-1$ gives $-6$, and solving $9 + k = 4$"
        r" as $k = 4 + 9$ gives 14."
        r" The correct answer is **B**.",
        ["Eq(3**2 + (-5), 4)", "Eq((-1)**2 + (-5), -4)"],
        -4, {-6: "treated $(-1)^2$ as $-1$",
             4: "assumed $f(-1) = f(3)$",
             14: "solved $9 + k = 4$ as $k = 13$"}))

    # Q7 M alg SPR
    assert 35 + Rational(1, 10) * (85 - 20) == Rational(415, 10)
    qs.append(spr(
        "SAT-P10-M2H-Q07", M, 7, "algebra", "linear_models", "medium",
        r"A phone plan costs $\$35$ per month plus $\$0.10$ for each"
        r" gigabyte of data used beyond the first 20 gigabytes. One"
        r" month a customer was charged $\$41.50$. How many gigabytes of"
        r" data did the customer use that month?",
        ["85"],
        r"Only the data beyond 20 GB is charged. Let $g$ be the total"
        r" gigabytes used, so the billed overage is $g - 20$:"
        r" $$35 + 0.10(g - 20) = 41.50.$$"
        r" Subtract the base charge:"
        r" $$0.10(g - 20) = 6.50.$$"
        r" Divide by $0.10$:"
        r" $$g - 20 = 65 \;\Rightarrow\; g = 85.$$"
        r" Answering 65 stops at the overage instead of the total usage.",
        ["Eq(Rational(415,10) - 35, Rational(65,10))",
         "Eq(Rational(65,10)/Rational(1,10), 65)",
         "Eq(35 + Rational(1,10)*(85 - 20), Rational(415,10))"]))

    # Q8 M adv
    assert Rational(5**2 - 9, 5 + 3) == 5 - 3
    qs.append(mcq_listed(
        "SAT-P10-M2H-Q08", M, 8, "advanced_math", "rational_expressions",
        "medium",
        r"For $x \ne -3$, which of the following is equivalent to"
        r" $\dfrac{x^2 - 9}{x + 3}$?",
        {"A": r"$x - 3$", "B": r"$x + 3$", "C": r"$x - 9$",
         "D": r"$x^2 - 3$"},
        "A",
        r"The numerator is a difference of two squares:"
        r" $$x^2 - 9 = (x - 3)(x + 3).$$"
        r" Cancelling the common factor $x + 3$ (legal because"
        r" $x \ne -3$) leaves"
        r" $$x - 3.$$"
        r" Testing $x = 5$ confirms it: $\frac{25 - 9}{8} = \frac{16}{8}"
        r" = 2 = 5 - 3$. Cancelling the 9 against the 3 term by term is"
        r" not allowed and produces choice C."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 3)*(x + 3)), x**2 - 9)",
         "Eq(Rational(5**2 - 9, 5 + 3), 2)"]))

    # Q9 M geo — figure: right triangle, cosine ratio
    assert 8**2 + 15**2 == 17**2
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q09", M, 9, "geometry_trig", "right_triangle_trig",
        "medium",
        r"The right triangle shown has legs of length 8 and 15. What is"
        r" the value of $\cos\theta$?",
        r"First find the hypotenuse:"
        r" $$h = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17.$$"
        r" Cosine is adjacent over hypotenuse. The leg of length 8 lies"
        r" along $\theta$, so"
        r" $$\cos\theta = \frac{8}{17}.$$"
        r" The leg of length 15 is opposite $\theta$, giving"
        r" $\sin\theta = \frac{15}{17}$ and"
        r" $\tan\theta = \frac{15}{8}$ — the two ratios most often"
        r" grabbed by mistake."
        r" The correct answer is **A**.",
        ["Eq(8**2 + 15**2, 289)", "Eq(sqrt(289), 17)"],
        Rational(8, 17),
        {Rational(8, 15): "used the leg ratio instead of the hypotenuse",
         Rational(15, 17): "used the sine ratio",
         Rational(17, 8): "inverted the ratio"},
        fmt=frac,
        fig=figure("sat-p10-m2h-q09",
                   "Right triangle with horizontal leg 8, vertical leg 15, "
                   "and the angle theta marked at the bottom-left vertex")))

    # Q10 H alg — (x+y)^2 from x^2+y^2 and xy
    assert 40 + 2 * 12 == 64
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q10", M, 10, "algebra", "algebraic_identities", "hard",
        r"If $x^2 + y^2 = 40$ and $xy = 12$, what is the value of"
        r" $(x + y)^2$?",
        r"Expand the square and recognise both given pieces:"
        r" $$(x + y)^2 = x^2 + 2xy + y^2 = (x^2 + y^2) + 2xy.$$"
        r" Substitute:"
        r" $$40 + 2(12) = 40 + 24 = 64.$$"
        r" The middle term is $2xy$, not $xy$ — adding 12 once gives 52,"
        r" and subtracting it gives $(x - y)^2 = 16$ instead."
        r" The correct answer is **C**.",
        ["Eq(expand((x + y)**2), x**2 + 2*x*y + y**2)",
         "Eq(40 + 2*12, 64)", "Eq(40 - 2*12, 16)"],
        64, {16: "computed $(x - y)^2$ by subtracting $2xy$",
             52: "added $xy$ once instead of twice",
             76: "added $3xy$"}))

    # Q11 H adv — remaining roots
    assert 3**3 - 4 * 3**2 + 3 + 6 == 0
    assert expand((x - 3) * (x - 2) * (x + 1)) == x**3 - 4 * x**2 + x + 6
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q11", M, 11, "advanced_math", "polynomial_roots",
        "hard",
        r"The polynomial $p(x) = x^3 - 4x^2 + x + 6$ has a zero at"
        r" $x = 3$. What is the sum of the other two zeros of $p$?",
        r"For a cubic $x^3 + bx^2 + \dots$, the three zeros sum to $-b$,"
        r" so here they sum to"
        r" $$-(-4) = 4.$$"
        r" One zero is 3, so the other two sum to"
        r" $$4 - 3 = 1.$$"
        r" (Dividing out the factor $x - 3$ gives"
        r" $x^2 - x - 2 = (x - 2)(x + 1)$, whose zeros are 2 and $-1$ —"
        r" and $2 + (-1) = 1$.) Answering 4 gives the sum of ALL three"
        r" zeros."
        r" The correct answer is **B**.",
        ["Eq(3**3 - 4*3**2 + 3 + 6, 0)",
         "Eq(expand((x - 3)*(x - 2)*(x + 1)), x**3 - 4*x**2 + x + 6)",
         "Eq(2 + (-1), 1)", "Eq(3 + 2 + (-1), 4)"],
        1, {-1: "gave only one of the remaining zeros",
            4: "gave the sum of all three zeros",
            6: "gave the constant term"}))

    # Q12 H alg SPR
    assert expand((2 * x - 3) * (x - 4)) == 2 * x**2 - 11 * x + 12
    qs.append(spr(
        "SAT-P10-M2H-Q12", M, 12, "algebra", "quadratic_equations", "hard",
        r"What is the smaller of the two solutions of"
        r" $2x^2 - 11x + 12 = 0$?",
        ["3/2", "1.5"],
        r"Factor the quadratic. Two numbers multiplying to"
        r" $2 \times 12 = 24$ and adding to $-11$ are $-3$ and $-8$, so"
        r" $$2x^2 - 11x + 12 = (2x - 3)(x - 4) = 0.$$"
        r" The two solutions are"
        r" $$2x - 3 = 0 \;\Rightarrow\; x = \frac{3}{2},"
        r" \qquad x - 4 = 0 \;\Rightarrow\; x = 4.$$"
        r" The smaller is $\frac{3}{2}$, or $1.5$. Note that the leading"
        r" coefficient 2 makes one root a fraction — ignoring it and"
        r" factoring as $(x-3)(x-4)$ would give the wrong pair.",
        ["Eq(expand((2*x - 3)*(x - 4)), 2*x**2 - 11*x + 12)",
         "Eq(2*Rational(3,2)**2 - 11*Rational(3,2) + 12, 0)",
         "Rational(3,2) < 4"]))

    # Q13 H adv — logarithms
    assert 8 * (8 - 6) == 16
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q13", M, 13, "advanced_math", "logarithms", "hard",
        r"If $\log_2 x + \log_2 (x - 6) = 4$, what is the value of $x$?",
        r"Combine the logarithms into one:"
        r" $$\log_2\big(x(x - 6)\big) = 4.$$"
        r" Rewrite in exponential form:"
        r" $$x(x - 6) = 2^4 = 16 \;\Rightarrow\; x^2 - 6x - 16 = 0.$$"
        r" Factoring gives $(x - 8)(x + 2) = 0$, so $x = 8$ or $x = -2$."
        r" The value $x = -2$ is extraneous — $\log_2(-2)$ is undefined —"
        r" so the only solution is"
        r" $$x = 8.$$"
        r" Checking: $\log_2 8 + \log_2 2 = 3 + 1 = 4$. Adding the"
        r" arguments instead of multiplying them gives $2x - 6 = 16$ and"
        r" the value 11."
        r" The correct answer is **B**.",
        ["Eq(8*(8 - 6), 16)", "Eq(expand((x - 8)*(x + 2)), x**2 - 6*x - 16)",
         "Eq(2**4, 16)"],
        8, {-2: "kept the extraneous negative solution",
            11: "added the arguments instead of multiplying",
            22: "set $x - 6$ equal to 16"}))

    # Q14 H psda — sampling and generalization
    assert Rational(40, 12400) == Rational(1, 310)
    qs.append(mcq_listed(
        "SAT-P10-M2H-Q14", M, 14, "psda", "evaluating_claims_experiments",
        "hard",
        r"A researcher wants to estimate the mean number of hours per week"
        r" that the 12,400 students at a university spend studying. She"
        r" will survey 40 students. Which of the following study designs"
        r" would best allow her conclusions to be generalised to all"
        r" 12,400 students?",
        {"A": r"Surveying 40 students chosen at random from the"
              r" university's full enrolment list.",
         "B": r"Surveying the first 40 students who enter the main"
              r" library on a Monday morning.",
         "C": r"Surveying 40 students who volunteer to respond after a"
              r" mathematics lecture.",
         "D": r"Surveying 40 students chosen at random from a single"
              r" residence hall."},
        "A",
        r"A result generalises to a population only when the sample was"
        r" selected at random from that ENTIRE population. The full"
        r" enrolment list is the population, so choice A gives every one"
        r" of the 12,400 students the same chance — a sampling fraction"
        r" of $\frac{40}{12400} = \frac{1}{310}$ — of being included."
        r" Choice B favours library users, choice C is a voluntary"
        r" response sample from one lecture, and choice D is random only"
        r" within one residence hall. Each of those three supports"
        r" conclusions about a narrower group, not about all students."
        r" The correct answer is **A**.",
        ["Eq(Rational(40, 12400), Rational(1,310))", "12400 > 40"]))

    # Q15 H alg SPR — average cost
    assert Rational(12 * 60 + 480, 60) == 20
    qs.append(spr(
        "SAT-P10-M2H-Q15", M, 15, "algebra", "rational_equations", "hard",
        r"A factory's total cost, in dollars, to produce $n$ units is"
        r" given by $C(n) = 12n + 480$. For what value of $n$ is the"
        r" average cost per unit equal to $\$20$?",
        ["60"],
        r"Average cost per unit is total cost divided by the number of"
        r" units:"
        r" $$\frac{12n + 480}{n} = 20.$$"
        r" Multiply both sides by $n$:"
        r" $$12n + 480 = 20n.$$"
        r" Collect the $n$ terms:"
        r" $$480 = 8n \;\Rightarrow\; n = 60.$$"
        r" Checking, $C(60) = 720 + 480 = 1200$, and"
        r" $1200 \div 60 = 20$. The fixed cost of $\$480$ is what makes"
        r" the average cost fall as $n$ grows.",
        ["Eq(12*60 + 480, 1200)", "Eq(Rational(1200, 60), 20)",
         "Eq(Rational(480, 20 - 12), 60)"]))

    # Q16 H adv — composition
    assert 3 * 2 - 2 == 4 and 4**2 + 1 == 17
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q16", M, 16, "advanced_math", "function_composition",
        "hard",
        r"The functions $f$ and $g$ are defined by $f(x) = 3x - 2$ and"
        r" $g(x) = x^2 + 1$. What is the value of $g(f(2))$?",
        r"In $g(f(2))$ the inner function runs first:"
        r" $$f(2) = 3(2) - 2 = 4.$$"
        r" Then apply $g$ to that output:"
        r" $$g(4) = 4^2 + 1 = 17.$$"
        r" Order matters — reversing it gives $f(g(2)) = f(5) = 13$, a"
        r" different number and the intended trap."
        r" The correct answer is **D**.",
        ["Eq(3*2 - 2, 4)", "Eq(4**2 + 1, 17)", "Eq(2**2 + 1, 5)",
         "Eq(3*5 - 2, 13)"],
        17, {4: "stopped at $f(2)$", 5: "computed $g(2)$",
             13: "computed $f(g(2))$ instead"}))

    # Q17 H geo — cone vs cylinder
    assert Rational(1, 3) * 96 == 32
    qs.append(mcq_listed(
        "SAT-P10-M2H-Q17", M, 17, "geometry_trig", "solids_volume_surface",
        "hard",
        r"A right circular cylinder and a right circular cone have the"
        r" same radius and the same height. The volume of the cylinder is"
        r" $96\pi$ cubic inches. What is the volume, in cubic inches, of"
        r" the cone?",
        {"A": r"$24\pi$", "B": r"$32\pi$", "C": r"$48\pi$",
         "D": r"$288\pi$"},
        "B",
        r"The two volume formulas differ by a single factor:"
        r" $$V_{\text{cyl}} = \pi r^2 h, \qquad"
        r" V_{\text{cone}} = \frac{1}{3}\pi r^2 h.$$"
        r" With the same $r$ and the same $h$, the cone holds exactly one"
        r" third as much:"
        r" $$\frac{1}{3}(96\pi) = 32\pi.$$"
        r" Halving instead of taking a third gives $48\pi$, and"
        r" multiplying by 3 gives $288\pi$."
        r" The correct answer is **B**.",
        ["Eq(Rational(1,3)*96, 32)", "Eq(Rational(1,2)*96, 48)",
         "Eq(3*96, 288)"]))

    # Q18 H alg — x-intercept from two points
    _m18 = Rational(-7 - 5, 4 - (-2))
    assert _m18 == -2
    assert _solve(Eq(-2 * x + 1, 0), x) == [Rational(1, 2)]
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q18", M, 18, "algebra", "linear_functions_slope",
        "hard",
        r"A line in the $xy$-plane passes through the points $(-2, 5)$ and"
        r" $(4, -7)$. What is the $x$-coordinate of the $x$-intercept of"
        r" the line?",
        r"Find the slope first:"
        r" $$m = \frac{-7 - 5}{4 - (-2)} = \frac{-12}{6} = -2.$$"
        r" Use the point $(-2, 5)$ in point-slope form:"
        r" $$y - 5 = -2(x + 2) \;\Rightarrow\; y = -2x + 1.$$"
        r" The $x$-intercept is where $y = 0$:"
        r" $$0 = -2x + 1 \;\Rightarrow\; x = \frac{1}{2} = 0.5.$$"
        r" Answering 1 gives the $y$-intercept instead, and $-2$ gives the"
        r" slope."
        r" The correct answer is **C**.",
        ["Eq(Rational(-7 - 5, 4 + 2), -2)", "Eq(-2*(-2) + 1, 5)",
         "Eq(-2*4 + 1, -7)", "Eq(-2*Rational(1,2) + 1, 0)"],
        Rational(1, 2),
        {-2: "reported the slope",
         Rational(-1, 2): "made a sign error solving $0 = -2x + 1$",
         1: "reported the $y$-intercept"},
        fmt=smart))

    # Q19 H adv SPR — reciprocal equation
    assert Rational(1, 10) + Rational(1, 15) == Rational(1, 6)
    qs.append(spr(
        "SAT-P10-M2H-Q19", M, 19, "advanced_math", "rational_equations",
        "hard",
        r"If $\dfrac{1}{a} + \dfrac{1}{b} = \dfrac{1}{6}$ and $a = 10$,"
        r" what is the value of $b$?",
        ["15"],
        r"Substitute $a = 10$ and isolate the remaining reciprocal:"
        r" $$\frac{1}{b} = \frac{1}{6} - \frac{1}{10}.$$"
        r" Use the common denominator 30:"
        r" $$\frac{1}{b} = \frac{5}{30} - \frac{3}{30} = \frac{2}{30}"
        r" = \frac{1}{15}.$$"
        r" Taking reciprocals of both sides gives"
        r" $$b = 15.$$"
        r" Subtracting the denominators directly, as $b = 10 - 6 = 4$,"
        r" is the classic error — reciprocals do not subtract that way.",
        ["Eq(Rational(1,6) - Rational(1,10), Rational(1,15))",
         "Eq(Rational(1,10) + Rational(1,15), Rational(1,6))"]))

    # Q20 H psda — mean after removing a subgroup
    assert 20 * 76 == 1520 and 4 * 44 == 176
    assert Rational(1520 - 176, 16) == 84
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q20", M, 20, "psda", "center_spread", "hard",
        r"The mean of 20 test scores is 76. Four of the scores, which"
        r" have a mean of 44, are removed from the list. What is the mean"
        r" of the remaining 16 scores?",
        r"Work in totals, not means. All 20 scores sum to"
        r" $$20 \times 76 = 1520,$$"
        r" and the four removed scores sum to"
        r" $$4 \times 44 = 176.$$"
        r" The remaining 16 scores therefore sum to"
        r" $$1520 - 176 = 1344,$$"
        r" and their mean is"
        r" $$\frac{1344}{16} = 84.$$"
        r" Means cannot be added or subtracted directly: $76 - 44 = 32$"
        r" and the midpoint $\frac{76 + 84}{2} = 80$ are both wrong here."
        r" The correct answer is **C**.",
        ["Eq(20*76, 1520)", "Eq(4*44, 176)", "Eq(1520 - 176, 1344)",
         "Eq(Rational(1344, 16), 84)"],
        84, {32: "subtracted the two means",
             80: "averaged the two means",
             120: "added the two means"}))

    # Q21 H adv — leading coefficient from vertex form
    assert 4 == 2 * (1 - 3) ** 2 - 4
    qs.append(mcq_numeric(
        "SAT-P10-M2H-Q21", M, 21, "advanced_math", "quadratic_vertex_form",
        "hard",
        r"In the $xy$-plane, the graph of $y = ax^2 + bx + c$ is a"
        r" parabola with vertex $(3, -4)$, and the graph passes through"
        r" the point $(1, 4)$. What is the value of $a$?",
        r"Write the parabola in vertex form, where the vertex appears"
        r" directly:"
        r" $$y = a(x - 3)^2 - 4.$$"
        r" Substitute the known point $(1, 4)$:"
        r" $$4 = a(1 - 3)^2 - 4 = 4a - 4.$$"
        r" Solve:"
        r" $$8 = 4a \;\Rightarrow\; a = 2.$$"
        r" Dropping the $-4$ before solving gives $a = 1$, and a sign slip"
        r" on $(1-3)^2$ gives $-2$."
        r" The correct answer is **C**.",
        ["Eq(2*(1 - 3)**2 - 4, 4)", "Eq((1 - 3)**2, 4)",
         "Eq(2*(3 - 3)**2 - 4, -4)"],
        2, {-2: "made a sign error on $(1 - 3)^2$",
            Rational(1, 2): "inverted the final division",
            4: "forgot to subtract 4 from both sides"},
        fmt=smart))

    # Q22 H alg SPR — two powers, one base
    assert 2 ** Rational(4, 3) * 4 ** (Rational(4, 3) + 1) == 64
    qs.append(spr(
        "SAT-P10-M2H-Q22", M, 22, "algebra", "exponent_equations", "hard",
        r"If $2^{x} \cdot 4^{x + 1} = 64$, what is the value of $x$?",
        ["4/3"],
        r"Write every term as a power of 2. Since $4 = 2^2$ and"
        r" $64 = 2^6$,"
        r" $$2^{x} \cdot \left(2^{2}\right)^{x + 1} = 2^{6}.$$"
        r" Multiply the exponents in the second factor, then add the"
        r" exponents of the product:"
        r" $$2^{x} \cdot 2^{2x + 2} = 2^{3x + 2} = 2^{6}.$$"
        r" Equal bases force equal exponents:"
        r" $$3x + 2 = 6 \;\Rightarrow\; x = \frac{4}{3}.$$"
        r" The step that is easy to miss is $(2^2)^{x+1} = 2^{2x + 2}$ —"
        r" the outer exponent multiplies BOTH terms of $x + 1$.",
        ["Eq(2**Rational(4,3) * 4**(Rational(4,3) + 1), 64)",
         "Eq(3*Rational(4,3) + 2, 6)", "Eq(2**6, 64)"]))

    return qs


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
    write_test(REPO / "data" / "sat" / "sat-practice-10.json",
               {"testId": "sat-practice-10",
                "label": "SAT Math Practice Test 10",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
