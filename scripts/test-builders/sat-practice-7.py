#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 7 (data/sat/sat-practice-7.json).

Built on scripts/test-builders/satbuild.py — only stems, parameters,
computed answers, named distractor error models, verify[] strings, and
solutions live here.

Archetype freshness versus tests 1-6 (audited before authoring). New to
the bank in this test:
  * two-way table read for a JOINT (not conditional) probability, and a
    conditional stated in the reversed direction
  * percent-of-a-percent and "what number is p% of q" phrasings
  * an inequality whose solution must be reported as a COUNT of integers
  * a system solved by scaling BOTH equations before elimination
  * proportional reasoning with a unit-price comparison ("better buy")
  * function tables: reading f(g(x)) values off two tables at once
  * a quadratic given by its factored form asked for the VERTEX
  * exponential decay expressed with a fractional exponent (half-life)
  * slope from a table, and a line through the origin (direct variation)
  * interior-angle sum of a polygon; the exterior-angle total
  * similar triangles with an AREA ratio (square of the scale factor)
  * arc measure vs inscribed angle; a chord bisected by a radius
  * a cube's space diagonal; surface area to volume
  * standard deviation compared between two data sets
  * a boxplot IQR read, and a histogram median-interval read

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
    f = float(Fraction(v))
    return rf"$\${f:g}$"


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E algebra one_var — fraction coefficient
    assert _solve(Eq(Rational(2, 3) * x + 5, 17), x) == [18]
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $\dfrac{2}{3}x + 5 = 17$, what is the value of $x$?",
        r"Subtract 5, then multiply by the reciprocal of $\frac{2}{3}$:"
        r" $$\frac{2}{3}x = 12 \;\Rightarrow\; x = 12 \cdot \frac{3}{2} = 18.$$"
        r" Multiplying by $\frac{2}{3}$ instead of its reciprocal gives 8, and"
        r" forgetting to subtract 5 first gives $17 \cdot \frac{3}{2} = 25.5$."
        r" The correct answer is **C**.",
        ["Eq(Rational(2,3)*18 + 5, 17)", "Eq(12*Rational(3,2), 18)"],
        18, {8: "multiplied by 2/3 instead of its reciprocal",
             Rational(51, 2): "did not subtract 5 first",
             12: "stopped after subtracting 5"}, fmt=smart))

    # Q2 E advanced equivalent_expressions — distribute a negative
    assert expand(3 * (2 * x - 5) - 2 * (x - 4)) == 4 * x - 7
    qs.append(mcq_listed(
        "SAT-P7-M1-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $3(2x - 5) - 2(x - 4)$?",
        {"A": r"$4x - 23$", "B": r"$4x - 7$", "C": r"$4x + 1$",
         "D": r"$8x - 7$"}, "B",
        r"Distribute both products, watching the sign on the second:"
        r" $$3(2x - 5) = 6x - 15, \qquad -2(x - 4) = -2x + 8.$$"
        r" Now combine:"
        r" $$6x - 15 - 2x + 8 = 4x - 7.$$"
        r" Distributing $-2$ over $-4$ as $-8$ gives $4x - 23$ — the most"
        r" common slip here."
        r" The correct answer is **B**.",
        ["Eq(expand(3*(2*x - 5) - 2*(x - 4)), 4*x - 7)",
         "Eq(expand(-2*(x - 4)), -2*x + 8)"]))

    # Q3 E psda ratios_rates_units — unit price comparison ("better buy")
    assert Rational(20, 5) == 4 and Rational(24, 8) == 3 and 3 < 4
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q03", M, 3, "psda", "ratios_rates_units", "easy",
        r"A store sells rice in two sizes: a $5$-kilogram bag for $\$20$ and"
        r" an $8$-kilogram bag for $\$24$. In dollars per kilogram, what is"
        r" the unit price of the CHEAPER option?",
        r"Divide each price by its size to compare like with like:"
        r" $$\frac{20}{5} = 4, \qquad \frac{24}{8} = 3.$$"
        r" The 8-kilogram bag costs less per kilogram, so the cheaper unit"
        r" price is $\$3$ per kilogram — note that it is the bag with the"
        r" LARGER sticker price. Reporting the other unit price gives 4,"
        r" dividing the larger cost by the smaller size gives $4.8$, and"
        r" adding the sticker prices gives 44."
        r" The correct answer is **A**.",
        ["Eq(Rational(20,5), 4)", "Eq(Rational(24,8), 3)", "3 < 4"],
        3, {4: "reported the more expensive unit price",
            Rational(24, 5): "divided the larger cost by the smaller size",
            44: "added the two sticker prices"}, fmt=smart))

    # Q4 SPR E algebra linear_functions — slope read from a table
    TBL_X, TBL_Y = [1, 3, 5, 7], [9, 17, 25, 33]
    assert all(Rational(TBL_Y[i + 1] - TBL_Y[i], TBL_X[i + 1] - TBL_X[i]) == 4
               for i in range(3))
    qs.append(spr(
        "SAT-P7-M1-Q04", M, 4, "algebra", "linear_functions", "easy",
        r"The table shows four values of the linear function $f$. What is the"
        r" slope of the graph of $y = f(x)$ in the $xy$-plane?",
        ["4"],
        r"For a linear function the slope is the same between any two rows."
        r" Using the first two:"
        r" $$m = \frac{17 - 9}{3 - 1} = \frac{8}{2} = 4.$$"
        r" Note that $x$ steps by 2 each row, not by 1 — dividing the"
        r" $y$-differences by 1 would wrongly give 8."
        r" The correct answer is **4**.",
        ["Eq(Rational(17 - 9, 3 - 1), 4)", "Eq(Rational(33 - 25, 7 - 5), 4)",
         "Eq(9 + 4*(7 - 1), 33)"],
        fig=figure("sat-p7-m1-q04",
                   "Two-row table of x values 1, 3, 5, 7 against f(x) values "
                   "9, 17, 25, 33")))

    # Q5 E geometry lines_angles_triangles — polygon interior-angle sum
    assert (7 - 2) * 180 == 900
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q05", M, 5, "geometry_trig", "lines_angles_triangles", "easy",
        r"What is the sum of the measures of the interior angles of a"
        r" heptagon (a polygon with $7$ sides)?",
        r"A polygon with $n$ sides splits into $n - 2$ triangles from one"
        r" vertex, and each triangle contributes $180^\circ$:"
        r" $$(7 - 2)(180) = 5 \cdot 180 = 900.$$"
        r" Using $n$ instead of $n - 2$ gives $1260$; using $n - 1$ gives"
        r" $1080$; and $360$ is the sum of the EXTERIOR angles, which is the"
        r" same for every polygon."
        r" The correct answer is **B**.",
        ["Eq((7 - 2)*180, 900)", "Eq(7*180, 1260)"],
        900, {360: "gave the exterior-angle sum",
              1080: "used n - 1 triangles",
              1260: "used n triangles"}, fmt=smart))

    # Q6 E advanced nonlinear_functions — evaluate a rational function
    assert Rational(2 * 5 + 3, 5 - 1) == Rational(13, 4)
    qs.append(mcq_listed(
        "SAT-P7-M1-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $g$ is defined by $g(x) = \dfrac{2x + 3}{x - 1}$ for"
        r" $x \ne 1$. What is the value of $g(5)$?",
        {"A": r"$\dfrac{7}{4}$", "B": r"$\dfrac{13}{6}$",
         "C": r"$\dfrac{13}{4}$", "D": r"$\dfrac{13}{2}$"}, "C",
        r"Substitute $x = 5$ into the numerator and the denominator"
        r" separately:"
        r" $$g(5) = \frac{2(5) + 3}{5 - 1} = \frac{13}{4}.$$"
        r" Adding 1 to 5 in the denominator gives $\frac{13}{6}$, and"
        r" dividing only the $2x$ term by $x - 1$ gives $\frac{7}{4}$."
        r" The correct answer is **C**.",
        ["Eq(Rational(2*5 + 3, 5 - 1), Rational(13,4))",
         "Eq(Rational(2*5 + 3, 5 + 1), Rational(13,6))"]))

    # Q7 E algebra linear_equations_two_var — direct variation through origin
    assert Rational(45, 9) == 5
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q07", M, 7, "algebra", "linear_equations_two_var", "easy",
        r"In the $xy$-plane, the line $y = kx$, where $k$ is a constant,"
        r" passes through the point $(9, 45)$. What is the value of $k$?",
        r"A line of the form $y = kx$ passes through the origin, so $k$ is"
        r" simply the ratio of the coordinates:"
        r" $$45 = k(9) \;\Rightarrow\; k = \frac{45}{9} = 5.$$"
        r" Inverting the ratio gives $\frac{1}{5}$, subtracting gives 36, and"
        r" adding gives 54."
        r" The correct answer is **B**.",
        ["Eq(45, 5*9)", "Eq(Rational(45,9), 5)"],
        5, {Rational(1, 5): "inverted the ratio",
            36: "subtracted the coordinates",
            54: "added the coordinates"}, fmt=smart))

    # Q8 E algebra linear_equations_one_var — consecutive integers
    assert _solve(Eq(x + (x + 1) + (x + 2), 72), x) == [23]
    assert 23 + 24 + 25 == 72
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q08", M, 8, "algebra", "linear_equations_one_var", "easy",
        r"The sum of three consecutive integers is $72$. What is the LEAST of"
        r" the three integers?",
        r"Name the least one $n$; the next two are $n + 1$ and $n + 2$:"
        r" $$n + (n + 1) + (n + 2) = 72 \;\Rightarrow\; 3n + 3 = 72"
        r" \;\Rightarrow\; n = 23.$$"
        r" The three integers are $23$, $24$, $25$, and they do sum to 72."
        r" Dividing 72 by 3 gives 24 — that is the MIDDLE integer, because the"
        r" three are evenly spaced about it — and 25 is the greatest."
        r" The correct answer is **B**.",
        ["Eq(23 + 24 + 25, 72)", "Eq(Rational(72 - 3, 3), 23)",
         "Eq(Rational(72,3), 24)"],
        23, {21: "subtracted 3 after dividing by 3",
             24: "reported the middle integer",
             25: "reported the greatest integer"}, fmt=smart))

    # Q9 SPR M advanced nonlinear_equations_systems — factor out first
    assert sorted(_solve(Eq(3 * x**2 - 12 * x, 0), x)) == [0, 4]
    qs.append(spr(
        "SAT-P7-M1-Q09", M, 9, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What is the greatest solution to $3x^2 - 12x = 0$?",
        ["4"],
        r"Factor rather than divide — dividing by $x$ would destroy the"
        r" solution $x = 0$:"
        r" $$3x(x - 4) = 0.$$"
        r" So $x = 0$ or $x = 4$, and the greatest is 4."
        r" The correct answer is **4**.",
        ["Eq(expand(3*x*(x - 4)), 3*x**2 - 12*x)",
         "Eq(3*4**2 - 12*4, 0)", "Eq(3*0**2 - 12*0, 0)", "4 > 0"]))

    # Q10 M psda probability_conditional — JOINT probability off a table
    JT = {"tenth": [21, 14], "eleventh": [18, 27]}   # [yes, no]
    assert sum(JT["tenth"]) + sum(JT["eleventh"]) == 80
    qs.append(mcq_listed(
        "SAT-P7-M1-Q10", M, 10, "psda", "probability_conditional", "medium",
        r"The two-way table shows the responses of $80$ students to a survey"
        r" about a new schedule. If one of the $80$ students is selected at"
        r" random, what is the probability that the student is in the eleventh"
        r" grade AND answered yes?",
        {"A": r"$\dfrac{18}{80}$", "B": r"$\dfrac{18}{45}$",
         "C": r"$\dfrac{18}{39}$", "D": r"$\dfrac{39}{80}$"}, "A",
        r"The student is selected from ALL $80$ students, so the denominator"
        r" is the grand total — no condition narrows it. The cell that is both"
        r" eleventh grade and yes holds 18 students:"
        r" $$P = \frac{18}{80}.$$"
        r" Dividing by the eleventh-grade row total 45 would answer ''given"
        r" that the student is in eleventh grade''; dividing by the yes-column"
        r" total 39 would answer ''given that the student answered yes''."
        r" Both are CONDITIONAL probabilities, and this question asks for"
        r" neither."
        r" The correct answer is **A**.",
        ["Eq(21 + 14 + 18 + 27, 80)", "Eq(18 + 27, 45)", "Eq(21 + 18, 39)"],
        fig=figure("sat-p7-m1-q10",
                   "Two-way table of grade (tenth, eleventh) against survey "
                   "response (yes, no) with row and column totals")))

    # Q11 M algebra systems_two_linear — scale BOTH equations to eliminate
    _s = _solve([Eq(3 * x + 4 * y, 26), Eq(5 * x - 3 * y, 24)], [x, y], dict=True)[0]
    assert _s[x] == 6 and _s[y] == 2
    assert 9 * 6 + 12 * 2 == 78 and 20 * 6 - 12 * 2 == 96 and 29 * 6 == 174
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q11", M, 11, "algebra", "systems_two_linear", "medium",
        r"$$3x + 4y = 26$$ $$5x - 3y = 24$$"
        r" If $(x, y)$ is the solution to the system of equations above, what"
        r" is the value of $x$?",
        r"Neither variable cancels as written, so scale BOTH equations. The"
        r" $y$-coefficients are 4 and $-3$, whose least common multiple is 12:"
        r" multiply the first equation by 3 and the second by 4."
        r" $$9x + 12y = 78, \qquad 20x - 12y = 96.$$"
        r" Now adding eliminates $y$:"
        r" $$29x = 174 \;\Rightarrow\; x = 6.$$"
        r" Substituting back gives $y = 2$, and both originals check:"
        r" $3(6) + 4(2) = 26$ and $5(6) - 3(2) = 24$."
        r" Reporting $y$ gives 2, and scaling only one equation leaves the"
        r" $y$-terms uncancelled."
        r" The correct answer is **C**.",
        ["Eq(3*6 + 4*2, 26)", "Eq(5*6 - 3*2, 24)",
         "Eq(3*(3*6 + 4*2), 78)", "Eq(4*(5*6 - 3*2), 96)",
         "Eq(78 + 96, 174)", "Eq(Rational(174, 29), 6)"],
        6, {2: "reported the value of y",
            4: "made a sign error when adding the scaled equations",
            10: "added the two right-hand sides without scaling"}, fmt=smart))

    # Q12 M advanced nonlinear_functions — vertex from factored form
    assert sorted(_solve(Eq((x - 1) * (x - 9), 0), x)) == [1, 9]
    assert (1 + 9) / 2 == 5 and (5 - 1) * (5 - 9) == -16
    qs.append(mcq_listed(
        "SAT-P7-M1-Q12", M, 12, "advanced_math", "nonlinear_functions", "medium",
        r"The function $f$ is defined by $f(x) = (x - 1)(x - 9)$. What is the"
        r" vertex of the graph of $y = f(x)$ in the $xy$-plane?",
        {"A": r"$(1, 9)$", "B": r"$(5, -16)$", "C": r"$(5, 16)$",
         "D": r"$(9, 1)$"}, "B",
        r"The factored form gives the $x$-intercepts directly: $x = 1$ and"
        r" $x = 9$. A parabola is symmetric about its vertex, so the vertex"
        r" sits exactly halfway between them:"
        r" $$x = \frac{1 + 9}{2} = 5.$$"
        r" Evaluate there for the $y$-coordinate:"
        r" $$f(5) = (5 - 1)(5 - 9) = (4)(-4) = -16.$$"
        r" Since the parabola opens upward, the vertex is a MINIMUM and its"
        r" $y$-coordinate must be negative — $(5, 16)$ has the sign wrong, and"
        r" $(1, 9)$ just copies the two intercepts."
        r" The correct answer is **B**.",
        ["Eq(Rational(1 + 9, 2), 5)", "Eq((5 - 1)*(5 - 9), -16)",
         "Eq(expand((x - 1)*(x - 9)), x**2 - 10*x + 9)"]))

    # Q13 M geometry area_volume — cube space diagonal
    assert 6**2 * 3 == 108 and simplify(sqrt(108) - 6 * sqrt(3)) == 0
    qs.append(mcq_listed(
        "SAT-P7-M1-Q13", M, 13, "geometry_trig", "area_volume", "medium",
        r"A cube has edges of length $6$. What is the length of a diagonal"
        r" connecting two opposite vertices of the cube?",
        {"A": r"$6$", "B": r"$6\sqrt{2}$", "C": r"$6\sqrt{3}$", "D": r"$18$"},
        "C",
        r"Apply the Pythagorean theorem twice. A diagonal of one face has"
        r" length"
        r" $$\sqrt{6^2 + 6^2} = 6\sqrt{2}.$$"
        r" That face diagonal and the perpendicular edge form a second right"
        r" triangle whose hypotenuse is the space diagonal:"
        r" $$\sqrt{(6\sqrt{2})^2 + 6^2} = \sqrt{72 + 36} = \sqrt{108}"
        r" = 6\sqrt{3}.$$"
        r" Stopping at the face diagonal gives $6\sqrt{2}$, and adding three"
        r" edges gives 18."
        r" The correct answer is **C**.",
        ["Eq(6**2 + 6**2, 72)", "Eq(72 + 36, 108)",
         "Eq(simplify(sqrt(108)), 6*sqrt(3))"]))

    # Q14 SPR M psda one_var_data — interquartile range from a box plot
    FIVE = [12, 20, 27, 38, 51]
    assert FIVE[3] - FIVE[1] == 18
    qs.append(spr(
        "SAT-P7-M1-Q14", M, 14, "psda", "one_var_data", "medium",
        r"The box plot summarizes a data set. What is the interquartile range"
        r" of the data set?",
        ["18"],
        r"The interquartile range is the third quartile minus the first —"
        r" the width of the BOX, not of the whole plot:"
        r" $$38 - 20 = 18.$$"
        r" The full range, $51 - 12 = 39$, spans the whiskers as well, and"
        r" the median 27 is the line inside the box."
        r" The correct answer is **18**.",
        ["Eq(38 - 20, 18)", "Eq(51 - 12, 39)"],
        fig=figure("sat-p7-m1-q14",
                   "Box plot with minimum 12, first quartile 20, median 27, "
                   "third quartile 38, and maximum 51")))

    # Q15 M algebra linear_inequalities — count the integer solutions
    assert [n for n in range(-20, 20) if 4 * n - 7 < 21 and n >= 2] == \
        list(range(2, 7))
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"How many integers $n$ satisfy both $n \ge 2$ and $4n - 7 < 21$?",
        r"Solve the second inequality:"
        r" $$4n < 28 \;\Rightarrow\; n < 7.$$"
        r" Combined with $n \ge 2$, the integers allowed are"
        r" $$2,\; 3,\; 4,\; 5,\; 6,$$"
        r" which is 5 values. Note $7$ is EXCLUDED because the inequality is"
        r" strict; counting it gives 6, and computing $7 - 2 = 5$ works here"
        r" only by coincidence of the endpoints — the reliable method is to"
        r" list them."
        r" The correct answer is **B**.",
        ["Eq(4*6 - 7, 17)", "4*6 - 7 < 21", "Not(4*7 - 7 < 21)"],
        5, {4: "excluded both endpoints",
            6: "included n = 7 despite the strict inequality",
            7: "counted from 1 through 7"}, fmt=smart))

    # Q16 M advanced equivalent_expressions — rationalize a radical quotient
    assert simplify(12 / sqrt(3) - 4 * sqrt(3)) == 0
    qs.append(mcq_listed(
        "SAT-P7-M1-Q16", M, 16, "advanced_math", "equivalent_expressions",
        "medium",
        r"Which of the following is equivalent to $\dfrac{12}{\sqrt{3}}$?",
        {"A": r"$\sqrt{3}$", "B": r"$4\sqrt{3}$", "C": r"$6\sqrt{3}$",
         "D": r"$12\sqrt{3}$"}, "B",
        r"Multiply numerator and denominator by $\sqrt{3}$ to clear the"
        r" radical from the denominator:"
        r" $$\frac{12}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}}"
        r" = \frac{12\sqrt{3}}{3} = 4\sqrt{3}.$$"
        r" Forgetting to divide by 3 afterwards gives $12\sqrt{3}$."
        r" A quick check: $4\sqrt{3} \approx 6.93$ and"
        r" $\frac{12}{\sqrt{3}} \approx \frac{12}{1.732} \approx 6.93$."
        r" The correct answer is **B**.",
        ["Eq(simplify(12/sqrt(3)), 4*sqrt(3))",
         "Eq(simplify((4*sqrt(3))**2), 48)",
         "Eq(simplify((12/sqrt(3))**2), 48)"]))

    # Q17 M geometry right_triangles_trig — complementary-angle identity
    qs.append(mcq_listed(
        "SAT-P7-M1-Q17", M, 17, "geometry_trig", "right_triangles_trig",
        "medium",
        r"In right triangle $ABC$, the right angle is at $C$ and"
        r" $\sin A = \dfrac{5}{13}$. What is the value of $\cos B$?",
        {"A": r"$\dfrac{5}{13}$", "B": r"$\dfrac{12}{13}$",
         "C": r"$\dfrac{13}{12}$", "D": r"$\dfrac{13}{5}$"}, "A",
        r"Because the right angle is at $C$, angles $A$ and $B$ are"
        r" complementary: $A + B = 90^\circ$. For complementary angles the"
        r" sine of one equals the cosine of the other, since they swap which"
        r" leg is ''opposite'':"
        r" $$\cos B = \cos(90^\circ - A) = \sin A = \frac{5}{13}.$$"
        r" No side lengths are needed. Computing $\cos A$ instead gives"
        r" $\frac{12}{13}$, and inverting the ratio gives $\frac{13}{5}$."
        r" The correct answer is **A**.",
        ["Eq(5**2 + 12**2, 13**2)",
         "Eq(Rational(5,13)**2 + Rational(12,13)**2, 1)"]))

    # Q18 SPR H advanced nonlinear_functions — half-life with a fractional
    # exponent
    assert 640 * Rational(1, 2) ** Rational(18, 6) == 80
    qs.append(spr(
        "SAT-P7-M1-Q18", M, 18, "advanced_math", "nonlinear_functions", "hard",
        r"The mass, in grams, of a sample of a radioactive isotope $t$ hours"
        r" after it is measured is given by"
        r" $M(t) = 640\left(\dfrac{1}{2}\right)^{t/6}$. What is the mass, in"
        r" grams, of the sample $18$ hours after it is measured?",
        ["80"],
        r"The exponent $\frac{t}{6}$ counts how many 6-hour half-lives have"
        r" passed. At $t = 18$ that is"
        r" $$\frac{18}{6} = 3$$"
        r" half-lives, so"
        r" $$M(18) = 640\left(\frac{1}{2}\right)^{3} = \frac{640}{8} = 80.$$"
        r" Reading the exponent as $18$ rather than $\frac{18}{6}$ would give"
        r" a mass far below a gram; halving only once gives 320."
        r" The correct answer is **80**.",
        ["Eq(640*Rational(1,2)**3, 80)", "Eq(Rational(18,6), 3)"]))

    # Q19 H psda one_var_data — comparing standard deviations
    A_SET, B_SET = [40, 50, 60], [10, 50, 90]
    assert sum(A_SET) / 3 == sum(B_SET) / 3 == 50
    qs.append(mcq_listed(
        "SAT-P7-M1-Q19", M, 19, "psda", "one_var_data", "hard",
        r"Data set A consists of the values $40$, $50$, $60$ and data set B"
        r" consists of the values $10$, $50$, $90$. Which of the following"
        r" statements is true?",
        {"A": r"The mean of A is less than the mean of B, and the standard"
              r" deviations are equal.",
         "B": r"The mean of A is greater than the mean of B, and the standard"
              r" deviations are equal.",
         "C": r"The means are equal and the standard deviation of A is greater"
              r" than that of B.",
         "D": r"The means are equal and the standard deviation of A is less"
              r" than that of B."}, "D",
        r"Both sets have the same mean:"
        r" $$\frac{40 + 50 + 60}{3} = 50, \qquad"
        r" \frac{10 + 50 + 90}{3} = 50.$$"
        r" Standard deviation measures typical distance FROM the mean. In A"
        r" the distances are $10$, $0$, $10$; in B they are $40$, $0$, $40$."
        r" B's values are spread much further from the same center, so A has"
        r" the smaller standard deviation. Equal means never imply equal"
        r" spread — that is exactly the distinction this question tests."
        r" The correct answer is **D**.",
        ["Eq(Rational(40 + 50 + 60, 3), 50)",
         "Eq(Rational(10 + 50 + 90, 3), 50)",
         "Eq((40-50)**2 + (50-50)**2 + (60-50)**2, 200)",
         "Eq((10-50)**2 + (50-50)**2 + (90-50)**2, 3200)",
         "200 < 3200"]))

    # Q20 H geometry circles — inscribed angle from an arc measure
    assert Rational(140, 2) == 70
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"In a circle, points $A$, $B$, and $C$ lie on the circle and the arc"
        r" $AB$ that does NOT contain $C$ has measure $140^\circ$. What is the"
        r" measure, in degrees, of the inscribed angle $ACB$?",
        r"An inscribed angle is half the measure of the arc it intercepts."
        r" Angle $ACB$ has its vertex at $C$ and intercepts the arc $AB$ that"
        r" does not contain $C$, so"
        r" $$m\angle ACB = \frac{140}{2} = 70.$$"
        r" Using the arc measure itself gives 140 — that is the CENTRAL angle,"
        r" not the inscribed one; using the other arc, $360 - 140 = 220$, and"
        r" halving it gives 110."
        r" The correct answer is **A**.",
        ["Eq(Rational(140,2), 70)", "Eq(360 - 140, 220)",
         "Eq(Rational(220,2), 110)"],
        70, {110: "halved the other arc instead",
             140: "reported the arc measure (the central angle)",
             220: "reported the other arc"}, fmt=smart))

    # Q21 SPR H algebra linear_functions — solve for a parameter from a
    # function value
    assert _solve(Eq(3 * (2 * 4 + x) - 5, 22), x) == [1]
    qs.append(spr(
        "SAT-P7-M1-Q21", M, 21, "algebra", "linear_functions", "hard",
        r"The function $f$ is defined by $f(x) = 3(2x + c) - 5$, where $c$ is"
        r" a constant. If $f(4) = 22$, what is the value of $c$?",
        ["1"],
        r"Substitute $x = 4$ and keep $c$ symbolic:"
        r" $$f(4) = 3(8 + c) - 5 = 24 + 3c - 5 = 19 + 3c.$$"
        r" Set that equal to 22:"
        r" $$19 + 3c = 22 \;\Rightarrow\; 3c = 3 \;\Rightarrow\; c = 1.$$"
        r" Check: $f(4) = 3(8 + 1) - 5 = 27 - 5 = 22$."
        r" The correct answer is **1**.",
        ["Eq(3*(2*4 + 1) - 5, 22)", "Eq(3*(8 + 1) - 5, 22)"]))

    # Q22 H advanced nonlinear_equations_systems — line tangent to a parabola
    assert _solve(Eq((-6) ** 2 - 4 * 1 * x, 0), x) == [9]
    qs.append(mcq_numeric(
        "SAT-P7-M1-Q22", M, 22, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"$$y = x^2 - 2x + c$$ $$y = 4x - 5$$"
        r" In the system of equations above, $c$ is a constant. If the graphs"
        r" intersect at exactly one point in the $xy$-plane, what is the value"
        r" of $c$?",
        r"Set the two expressions for $y$ equal and collect on one side:"
        r" $$x^2 - 2x + c = 4x - 5 \;\Rightarrow\; x^2 - 6x + (c + 5) = 0.$$"
        r" Exactly one intersection point means this quadratic has exactly one"
        r" real solution, so its discriminant is zero:"
        r" $$(-6)^2 - 4(1)(c + 5) = 0 \;\Rightarrow\; 36 = 4(c + 5)"
        r" \;\Rightarrow\; c + 5 = 9,$$"
        r" giving $c = 4$. Forgetting to move the $-5$ across gives $c = 9$,"
        r" and dropping the factor of 4 in the discriminant gives $c = 31$."
        r" The correct answer is **A**.",
        ["Eq((-6)**2 - 4*(9), 0)", "Eq(9 - 5, 4)",
         "Eq(expand((x - 3)**2), x**2 - 6*x + 9)"],
        4, {9: "forgot to move the constant -5 across",
            14: "added 5 instead of subtracting",
            31: "dropped the factor of 4 in the discriminant"}, fmt=smart))

    return qs


# ─── Module 2, easier variant (11E / 9M / 2H) ─────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E algebra one_var
    assert _solve(Eq(x - 7, 12), x) == [19]
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $x - 7 = 12$, what is the value of $x + 3$?",
        r"Solve for $x$ first:"
        r" $$x = 12 + 7 = 19,$$"
        r" then evaluate what is asked:"
        r" $$x + 3 = 22.$$"
        r" Reporting $x$ itself gives 19, and subtracting 7 from 12 gives 5."
        r" The correct answer is **D**.",
        ["Eq(19 - 7, 12)", "Eq(19 + 3, 22)"],
        22, {5: "subtracted 7 from 12", 15: "added 3 to 12",
             19: "reported x instead of x + 3"}, fmt=smart))

    # Q2 E advanced equivalent_expressions — factor out a common factor
    assert expand(5 * x * (x + 3)) == 5 * x**2 + 15 * x
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $5x^2 + 15x$?",
        {"A": r"$5(x^2 + 15x)$", "B": r"$5x(x + 3)$", "C": r"$5x(x + 15)$",
         "D": r"$15x(x + 1)$"}, "B",
        r"The greatest common factor of $5x^2$ and $15x$ is $5x$:"
        r" $$5x^2 + 15x = 5x(x) + 5x(3) = 5x(x + 3).$$"
        r" Check by expanding: $5x(x + 3) = 5x^2 + 15x$. Factoring out only 5"
        r" leaves an $x$ behind in the second term."
        r" The correct answer is **B**.",
        ["Eq(expand(5*x*(x + 3)), 5*x**2 + 15*x)",
         "Eq(expand(5*(x**2 + 15*x)), 5*x**2 + 75*x)"]))

    # Q3 SPR E algebra linear_functions
    qs.append(spr(
        "SAT-P7-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 9 - 2x$. What is the value of"
        r" $f(-3)$?",
        ["15"],
        r"Substitute $x = -3$, keeping track of the double negative:"
        r" $$f(-3) = 9 - 2(-3) = 9 + 6 = 15.$$"
        r" The correct answer is **15**.",
        ["Eq(9 - 2*(-3), 15)"]))

    # Q4 E psda ratios_rates_units — scale on a recipe
    assert Rational(3, 4) * 12 == 9
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q04", M, 4, "psda", "ratios_rates_units", "easy",
        r"A recipe uses $3$ cups of flour for every $4$ servings. How many"
        r" cups of flour are needed for $12$ servings?",
        r"Twelve servings is $\frac{12}{4} = 3$ times the recipe, so the flour"
        r" scales by the same factor:"
        r" $$3 \times 3 = 9 \text{ cups}.$$"
        r" Equivalently $\frac{3}{4} \cdot 12 = 9$. Adding 8 servings' worth to"
        r" the original 3 cups without scaling gives 11, and $\frac{4}{3}$ of"
        r" 12 gives 16."
        r" The correct answer is **B**.",
        ["Eq(Rational(3,4)*12, 9)", "Eq(Rational(12,4), 3)"],
        9, {11: "added 8 servings' worth instead of scaling",
            12: "reported the number of servings",
            16: "inverted the ratio"}, fmt=smart))

    # Q5 E geometry area_volume — circumference from diameter
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        r"A circle has a diameter of $10$. What is the circumference of the"
        r" circle?",
        {"A": r"$5\pi$", "B": r"$10\pi$", "C": r"$25\pi$", "D": r"$100\pi$"},
        "B",
        r"Circumference is $C = \pi d$, or equivalently $2\pi r$. With"
        r" $d = 10$:"
        r" $$C = 10\pi.$$"
        r" Using the radius $5$ in $\pi d$ gives $5\pi$, and $\pi r^2 = 25\pi$"
        r" is the AREA, not the circumference."
        r" The correct answer is **B**.",
        ["Eq(2*5, 10)", "Eq(5**2, 25)"]))

    # Q6 E advanced nonlinear_functions — read a value off a graph description
    assert (-2) ** 3 + 4 == -4
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $h$ is defined by $h(x) = x^3 + 4$. What is the value"
        r" of $h(-2)$?",
        r"Cube first, then add:"
        r" $$h(-2) = (-2)^3 + 4 = -8 + 4 = -4.$$"
        r" An odd power keeps the negative sign, so $(-2)^3 = -8$, not $8$ —"
        r" that slip gives 12. Multiplying by 3 instead of cubing gives $-2$."
        r" The correct answer is **B**.",
        ["Eq((-2)**3 + 4, -4)", "Eq((-2)**3, -8)"],
        -4, {-12: "cubed then subtracted", -2: "multiplied by 3 instead of cubing",
             12: "treated the cube of -2 as +8"}, fmt=smart))

    # Q7 SPR E algebra linear_equations_two_var — substitute a point
    assert _solve(Eq(4 * 3 + 2 * x, 26), x) == [7]
    qs.append(spr(
        "SAT-P7-M2E-Q07", M, 7, "algebra", "linear_equations_two_var", "easy",
        r"The point $(3, k)$ lies on the graph of $4x + 2y = 26$ in the"
        r" $xy$-plane. What is the value of $k$?",
        ["7"],
        r"A point lies on a graph exactly when its coordinates satisfy the"
        r" equation. Substitute $x = 3$ and $y = k$:"
        r" $$4(3) + 2k = 26 \;\Rightarrow\; 12 + 2k = 26"
        r" \;\Rightarrow\; 2k = 14 \;\Rightarrow\; k = 7.$$"
        r" The correct answer is **7**.",
        ["Eq(4*3 + 2*7, 26)"]))

    # Q8 E geometry lines_angles_triangles — exterior angle of a triangle
    assert 55 + 68 == 123
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q08", M, 8, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In a triangle, two of the interior angles measure $55^\circ$ and"
        r" $68^\circ$. What is the measure, in degrees, of the exterior angle"
        r" at the third vertex?",
        r"An exterior angle equals the sum of the two NON-adjacent interior"
        r" angles:"
        r" $$55 + 68 = 123.$$"
        r" Equivalently, the third interior angle is"
        r" $180 - 123 = 57$, and its exterior angle is $180 - 57 = 123$."
        r" Reporting the third INTERIOR angle gives 57, and $180 - 68 = 112$"
        r" uses only one of the given angles."
        r" The correct answer is **D**.",
        ["Eq(55 + 68, 123)", "Eq(180 - 123, 57)", "Eq(180 - 57, 123)"],
        123, {57: "reported the third interior angle",
              112: "subtracted only one given angle from 180",
              125: "used 180 minus 55"}, fmt=smart))

    # Q9 E algebra linear_functions — interpret the intercept in context
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q09", M, 9, "algebra", "linear_functions", "easy",
        r"The total cost, in dollars, of renting a bicycle for $h$ hours is"
        r" given by $C(h) = 8h + 15$. What is the best interpretation of $15$"
        r" in this context?",
        {"A": r"The cost, in dollars, of renting the bicycle for one hour.",
         "B": r"The fixed fee, in dollars, charged regardless of the number of"
              r" hours.",
         "C": r"The cost, in dollars, of renting the bicycle for $15$ hours.",
         "D": r"The number of hours the bicycle is rented."}, "B",
        r"In a linear model $C(h) = mh + b$, the constant $b$ is the value"
        r" when $h = 0$:"
        r" $$C(0) = 8(0) + 15 = 15.$$"
        r" That is the amount charged before any hours accrue — a fixed fee."
        r" The $8$ is the hourly rate, so one hour costs $8 + 15 = 23$, not"
        r" $15$."
        r" The correct answer is **B**.",
        ["Eq(8*0 + 15, 15)", "Eq(8*1 + 15, 23)"]))

    # Q10 E advanced nonlinear_functions — solve a simple square equation
    assert sorted(_solve(Eq(x**2, 81), x)) == [-9, 9]
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q10", M, 10, "advanced_math", "nonlinear_functions", "easy",
        r"What are all solutions to $x^2 = 81$?",
        {"A": r"$-9$ only", "B": r"$9$ only", "C": r"$-9$ and $9$",
         "D": r"$-81$ and $81$"}, "C",
        r"Both a positive and a negative number square to 81:"
        r" $$9^2 = 81 \qquad\text{and}\qquad (-9)^2 = 81.$$"
        r" So the complete solution set is $x = \pm 9$. Reporting only the"
        r" principal square root, $9$, misses half the solutions."
        r" The correct answer is **C**.",
        ["Eq(9**2, 81)", "Eq((-9)**2, 81)"]))

    # Q11 E psda percentages — simple discount
    assert 60 - Rational(25, 100) * 60 == 45
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q11", M, 11, "psda", "percentages", "easy",
        r"A shirt regularly priced at $\$60$ is on sale for $25\%$ off. What"
        r" is the sale price?",
        r"A $25\%$ discount leaves $75\%$ of the price:"
        r" $$0.75 \times 60 = 45.$$"
        r" Equivalently, the discount is $0.25 \times 60 = 15$ and"
        r" $60 - 15 = 45$. Reporting the discount itself gives 15, and adding"
        r" it instead gives 75."
        r" The correct answer is **B**.",
        ["Eq(Rational(75,100)*60, 45)", "Eq(60 - Rational(25,100)*60, 45)"],
        45, {15: "reported the discount rather than the sale price",
             35: "subtracted 25 from 60",
             75: "added the discount instead of subtracting"}, fmt=money))

    # Q12 SPR M advanced nonlinear_equations_systems — quadratic with a
    # leading coefficient
    assert sorted(_solve(Eq(2 * x**2 - 5 * x - 3, 0), x)) == [Rational(-1, 2), 3]
    qs.append(spr(
        "SAT-P7-M2E-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What is the positive solution to $2x^2 - 5x - 3 = 0$?",
        ["3"],
        r"Factor by splitting the middle term, using $-6$ and $+1$ (product"
        r" $-6 = 2 \cdot (-3)$, sum $-5$):"
        r" $$2x^2 - 6x + x - 3 = 2x(x - 3) + 1(x - 3) = (2x + 1)(x - 3) = 0.$$"
        r" The solutions are $x = -\frac{1}{2}$ and $x = 3$, so the positive"
        r" one is 3."
        r" The correct answer is **3**.",
        ["Eq(expand((2*x + 1)*(x - 3)), 2*x**2 - 5*x - 3)",
         "Eq(2*3**2 - 5*3 - 3, 0)"]))

    # Q13 M algebra systems_two_linear — read the solution off a graph
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q13", M, 13, "algebra", "systems_two_linear", "medium",
        r"The graph shows the two lines of a system of linear equations. What"
        r" is the solution $(x, y)$ to the system?",
        {"A": r"$(-2, 4)$", "B": r"$(2, -4)$", "C": r"$(2, 4)$",
         "D": r"$(4, 2)$"}, "C",
        r"The solution to a system of two linear equations is the point where"
        r" the graphs INTERSECT — the one ordered pair that satisfies both"
        r" equations at once. The lines shown cross at"
        r" $$(2, 4).$$"
        r" Reversing the coordinates gives $(4, 2)$, a different point"
        r" entirely; always read across for $x$ first, then up for $y$."
        r" The correct answer is **C**.",
        ["Eq(2*2, 4)", "Eq(-2 + 6, 4)"],
        fig=figure("sat-p7-m2e-q13",
                   "Two lines on a coordinate grid intersecting at the point "
                   "(2, 4)")))

    # Q14 M advanced equivalent_expressions — fractional exponent to a radical
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "medium",
        r"For $x > 0$, which of the following is equivalent to"
        r" $\sqrt[3]{x^{5}}$?",
        {"A": r"$x^{3/5}$", "B": r"$x^{5/3}$", "C": r"$x^{8}$",
         "D": r"$x^{15}$"}, "B",
        r"A radical converts to a fractional exponent with the ROOT as the"
        r" denominator and the power as the numerator:"
        r" $$\sqrt[n]{x^{m}} = x^{m/n}, \qquad\text{so}\qquad"
        r" \sqrt[3]{x^{5}} = x^{5/3}.$$"
        r" Swapping them gives $x^{3/5}$, and multiplying the two numbers"
        r" gives $x^{15}$."
        r" The correct answer is **B**.",
        ["Eq(simplify((8**Rational(5,3))), 32)",
         "Eq(simplify((2**5)**Rational(1,3)), 2**Rational(5,3))"]))

    # Q15 SPR M advanced nonlinear_functions — find a coefficient from a root
    assert _solve(Eq(2**2 + x * 2 + 12, 0), x) == [-8]
    assert sorted(_solve(Eq(x**2 - 8 * x + 12, 0), x)) == [2, 6]
    qs.append(spr(
        "SAT-P7-M2E-Q15", M, 15, "advanced_math", "nonlinear_functions",
        "medium",
        r"The function $g$ is defined by $g(x) = x^2 + kx + 12$, where $k$ is"
        r" a constant. If $g(2) = 0$, what is the value of $k$?",
        ["-8"],
        r"Saying $g(2) = 0$ means $x = 2$ is a zero of the function, so"
        r" substitute it in and solve for $k$:"
        r" $$2^2 + k(2) + 12 = 0 \;\Rightarrow\; 2k + 16 = 0"
        r" \;\Rightarrow\; k = -8.$$"
        r" Check: $g(x) = x^2 - 8x + 12 = (x - 2)(x - 6)$, which does vanish"
        r" at $x = 2$ (and at $x = 6$)."
        r" The correct answer is **-8**.",
        ["Eq(2**2 + (-8)*2 + 12, 0)",
         "Eq(expand((x - 2)*(x - 6)), x**2 - 8*x + 12)"]))

    # Q16 M algebra linear_inequalities — translate and solve
    assert _solve(Eq(12 + 3 * x, 45), x) == [11]
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q16", M, 16, "algebra", "linear_inequalities", "medium",
        r"A student has already read $12$ pages of a book and reads $3$ more"
        r" pages each day. What is the greatest number of days the student can"
        r" read and still have read at most $45$ pages in total?",
        r"Let $d$ be the number of days. The total read is $12 + 3d$, and it"
        r" must satisfy"
        r" $$12 + 3d \le 45 \;\Rightarrow\; 3d \le 33 \;\Rightarrow\; d \le 11.$$"
        r" The greatest whole number of days is 11. Dividing 45 by 3 without"
        r" removing the 12 pages already read gives 15, and $45 - 12 = 33$ is"
        r" the number of PAGES still allowed, not the number of days."
        r" The correct answer is **B**.",
        ["Eq(12 + 3*11, 45)", "12 + 3*11 <= 45", "Not(12 + 3*12 <= 45)"],
        11, {9: "subtracted before dividing incorrectly",
             15: "divided 45 by 3 without removing the 12 pages",
             33: "reported the pages remaining rather than the days"},
        fmt=smart))

    # Q17 M advanced nonlinear_functions — composition read off two tables
    F_TBL = {1: 4, 2: 6, 3: 1, 4: 5}
    G_TBL = {1: 3, 2: 1, 3: 2, 4: 4}
    assert F_TBL[G_TBL[4]] == 5
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q17", M, 17, "advanced_math", "nonlinear_functions",
        "medium",
        r"The tables show several values of the functions $f$ and $g$. What is"
        r" the value of $f(g(4))$?",
        r"Work from the INSIDE out. First read $g(4)$ from the second table:"
        r" $$g(4) = 4.$$"
        r" Now feed that into $f$, using the first table:"
        r" $$f(g(4)) = f(4) = 5.$$"
        r" Composing in the other order gives $g(f(4)) = g(5)$, which the"
        r" tables do not even list; reading $f(4)$ then $g$ of it gives 4."
        r" The correct answer is **C**.",
        ["Eq(4, 4)", "Eq(5, 5)"],
        5, {1: "read g(3) by mistake", 4: "stopped at the inner value g(4)",
            6: "read f(2) by mistake"}, fmt=smart,
        fig=figure("sat-p7-m2e-q17",
                   "Two two-row tables: x versus f(x) with values 4, 6, 1, 5 "
                   "and x versus g(x) with values 3, 1, 2, 4")))

    # Q18 M psda one_var_data — median interval from a histogram
    HIST = [4, 7, 6, 3]     # counts in the four intervals
    assert sum(HIST) == 20 and HIST[0] + HIST[1] >= 10
    qs.append(mcq_listed(
        "SAT-P7-M2E-Q18", M, 18, "psda", "one_var_data", "medium",
        r"The histogram shows the commute times, in minutes, of $20$ people."
        r" Which interval contains the median commute time?",
        {"A": r"$0$ to $10$", "B": r"$10$ to $20$", "C": r"$20$ to $30$",
         "D": r"$30$ to $40$"}, "B",
        r"With $20$ values, the median is the average of the $10$th and $11$th"
        r" values in order. Accumulate the bars from the left:"
        r" $$4, \quad 4 + 7 = 11, \quad 11 + 6 = 17, \quad 17 + 3 = 20.$$"
        r" The count first reaches 10 in the second interval, so both the"
        r" $10$th and $11$th values fall in $10$ to $20$."
        r" The TALLEST bar also happens to be that interval here, but height"
        r" alone identifies the mode, not the median — the running total is"
        r" what settles it."
        r" The correct answer is **B**.",
        ["Eq(4 + 7 + 6 + 3, 20)", "Eq(4 + 7, 11)", "4 < 10", "11 >= 11"],
        fig=figure("sat-p7-m2e-q18",
                   "Histogram of commute times in four ten-minute intervals "
                   "with frequencies 4, 7, 6, 3")))

    # Q19 SPR M algebra linear_equations_two_var — parallel line's slope
    assert Rational(6, 3) == 2
    qs.append(spr(
        "SAT-P7-M2E-Q19", M, 19, "algebra", "linear_equations_two_var",
        "medium",
        r"Line $\ell$ is defined by $6x - 3y = 15$. Line $m$ is parallel to"
        r" line $\ell$. What is the slope of line $m$?",
        ["2"],
        r"Put line $\ell$ in slope-intercept form:"
        r" $$-3y = -6x + 15 \;\Rightarrow\; y = 2x - 5.$$"
        r" Its slope is 2, and parallel lines have EQUAL slopes, so line $m$"
        r" also has slope 2. (The perpendicular slope would be"
        r" $-\frac{1}{2}$.)"
        r" The correct answer is **2**.",
        ["Eq(Rational(-6,-3), 2)", "Eq(6*0 - 3*(-5), 15)"]))

    # Q20 M geometry right_triangles_trig — Pythagorean triple scaled
    assert 21**2 + 28**2 == 35**2
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q20", M, 20, "geometry_trig", "right_triangles_trig",
        "medium",
        r"A right triangle has a hypotenuse of length $35$ and one leg of"
        r" length $21$. What is the length of the other leg?",
        r"The hypotenuse is the longest side, so subtract:"
        r" $$\text{leg}^2 = 35^2 - 21^2 = 1225 - 441 = 784,$$"
        r" giving $\sqrt{784} = 28$. (This is the $3$-$4$-$5$ triple scaled by"
        r" 7.) ADDING the squares would treat the missing side as the"
        r" hypotenuse, which it is not; that gives about $40.8$."
        r" The correct answer is **C**.",
        ["Eq(35**2 - 21**2, 784)", "Eq(sqrt(784), 28)",
         "Eq(21**2 + 28**2, 35**2)"],
        28, {14: "subtracted the side lengths directly",
             24: "used the wrong triple",
             56: "added the side lengths"}, fmt=smart))

    # Q21 M advanced nonlinear_functions — exponential doubling model
    assert 300 * 2**4 == 4800
    qs.append(mcq_numeric(
        "SAT-P7-M2E-Q21", M, 21, "advanced_math", "nonlinear_functions",
        "hard",
        r"A population of $300$ bacteria doubles every $3$ hours. How many"
        r" bacteria are there after $12$ hours?",
        r"In 12 hours the population doubles"
        r" $$\frac{12}{3} = 4$$"
        r" times, so multiply by $2^4 = 16$:"
        r" $$300 \times 16 = 4800.$$"
        r" Doubling 12 times instead of 4 gives an enormous number;"
        r" multiplying by 4 rather than $2^4$ gives 1200, and doubling only"
        r" once gives 600."
        r" The correct answer is **D**.",
        ["Eq(Rational(12,3), 4)", "Eq(300*2**4, 4800)"],
        4800, {600: "doubled only once",
               1200: "multiplied by 4 instead of 2 to the 4th",
               2400: "used three doublings"}, fmt=smart))

    # Q22 SPR H algebra linear_equations_one_var — clear the fractions
    assert _solve(Eq((x + 5)/3, (x - 1)/2), x) == [13]
    qs.append(spr(
        "SAT-P7-M2E-Q22", M, 22, "algebra", "linear_equations_one_var", "hard",
        r"$$\frac{x + 5}{3} = \frac{x - 1}{2}$$"
        r" What is the solution to the equation above?",
        ["13"],
        r"Cross-multiply to clear both denominators:"
        r" $$2(x + 5) = 3(x - 1).$$"
        r" Distribute and solve:"
        r" $$2x + 10 = 3x - 3 \;\Rightarrow\; 13 = x.$$"
        r" Check: $\frac{13 + 5}{3} = 6$ and $\frac{13 - 1}{2} = 6$."
        r" The correct answer is **13**.",
        ["Eq(2*(13 + 5), 3*(13 - 1))", "Eq(Rational(13 + 5, 3), 6)",
         "Eq(Rational(13 - 1, 2), 6)"]))

    return qs


# ─── Module 2, harder variant (2E / 7M / 13H) ─────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E algebra one_var
    assert _solve(Eq(8 * x + 5, 3 * x + 40), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $8x + 5 = 3x + 40$, what is the value of $x$?",
        r"Gather like terms on opposite sides:"
        r" $$5x = 35 \;\Rightarrow\; x = 7.$$"
        r" Adding $3x$ rather than subtracting gives $11x = 35$; stopping at"
        r" $5x = 35$ gives 35."
        r" The correct answer is **B**.",
        ["Eq(8*7 + 5, 3*7 + 40)", "Eq((40 - 5)/(8 - 3), 7)"],
        7, {5: "divided 35 by 7 instead of 5", 9: "used 45 in the numerator",
            35: "stopped at 5x = 35"}, fmt=smart))

    # Q2 E advanced equivalent_expressions
    assert expand((3 * x - 2) ** 2) == 9 * x**2 - 12 * x + 4
    qs.append(mcq_listed(
        "SAT-P7-M2H-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $(3x - 2)^2$?",
        {"A": r"$9x^2 - 12x + 4$", "B": r"$9x^2 - 6x + 4$",
         "C": r"$9x^2 + 4$", "D": r"$9x^2 - 12x - 4$"}, "A",
        r"Squaring a binomial produces THREE terms, not two:"
        r" $$(3x - 2)^2 = (3x)^2 - 2(3x)(2) + 2^2 = 9x^2 - 12x + 4.$$"
        r" Squaring each term separately gives $9x^2 + 4$ and loses the middle"
        r" term entirely; using $-2(3x)(1)$ gives $-6x$."
        r" The correct answer is **A**.",
        ["Eq(expand((3*x - 2)**2), 9*x**2 - 12*x + 4)",
         "Eq(expand((3*x - 2)**2).subs(x, 1), 1)"]))

    # Q3 SPR M algebra linear_functions — average rate of change
    assert Rational(38 - 14, 9 - 3) == 4
    qs.append(spr(
        "SAT-P7-M2H-Q03", M, 3, "algebra", "linear_functions", "medium",
        r"For the linear function $f$, $f(3) = 14$ and $f(9) = 38$. What is"
        r" the value of $f(5)$?",
        ["22"],
        r"A linear function changes at a constant rate:"
        r" $$m = \frac{38 - 14}{9 - 3} = \frac{24}{6} = 4.$$"
        r" From $x = 3$ to $x = 5$ is 2 steps, so"
        r" $$f(5) = 14 + 2(4) = 22.$$"
        r" The correct answer is **22**.",
        ["Eq(Rational(38 - 14, 9 - 3), 4)", "Eq(14 + 2*4, 22)",
         "Eq(14 + 6*4, 38)"]))

    # Q4 M geometry area_volume — similar triangles, AREA ratio
    assert Rational(15, 5) == 3 and 3**2 == 9 and 9 * 8 == 72
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q04", M, 4, "geometry_trig", "area_volume", "medium",
        r"Triangle $DEF$ is similar to triangle $ABC$, with corresponding"
        r" sides in the ratio $15$ to $5$. If the area of triangle $ABC$ is"
        r" $8$, what is the area of triangle $DEF$?",
        r"For similar figures, areas scale by the SQUARE of the side ratio."
        r" The scale factor is"
        r" $$k = \frac{15}{5} = 3,$$"
        r" so the area factor is $k^2 = 9$:"
        r" $$\text{area of } DEF = 9 \times 8 = 72.$$"
        r" Scaling the area by 3 instead of 9 — the single most common error"
        r" on this question type — gives 24; cubing the factor as if it were a"
        r" volume gives 216."
        r" The correct answer is **C**.",
        ["Eq(Rational(15,5), 3)", "Eq(3**2*8, 72)", "Eq(3*8, 24)"],
        72, {24: "scaled the area by 3 instead of 3 squared",
             40: "multiplied the area by the side length ratio 5",
             216: "cubed the scale factor as if scaling a volume"}, fmt=smart))

    # Q5 M psda probability_conditional — conditional stated in reverse
    RV = {"morning": [24, 16], "evening": [9, 31]}   # [pass, fail]
    assert sum(RV["morning"]) + sum(RV["evening"]) == 80
    qs.append(mcq_listed(
        "SAT-P7-M2H-Q05", M, 5, "psda", "probability_conditional", "medium",
        r"The two-way table shows the results of a driving test for $80$"
        r" candidates, by session. If one of the candidates who PASSED is"
        r" selected at random, what is the probability that the candidate took"
        r" the morning session?",
        {"A": r"$\dfrac{24}{80}$", "B": r"$\dfrac{24}{40}$",
         "C": r"$\dfrac{24}{33}$", "D": r"$\dfrac{33}{80}$"}, "C",
        r"The condition names the PASSED group, so the denominator is the"
        r" pass COLUMN total, not a row total:"
        r" $$24 + 9 = 33.$$"
        r" Of those 33, the 24 who took the morning session give"
        r" $$\frac{24}{33}.$$"
        r" Dividing by the morning row total 40 answers the REVERSED question"
        r" — given that a candidate took the morning session, the probability"
        r" that the candidate passed. Reading which total the condition"
        r" selects is the whole task here."
        r" The correct answer is **C**.",
        ["Eq(24 + 16 + 9 + 31, 80)", "Eq(24 + 9, 33)", "Eq(24 + 16, 40)",
         "Rational(24,33) != Rational(24,40)"],
        fig=figure("sat-p7-m2h-q05",
                   "Two-way table of session (morning, evening) against result "
                   "(passed, failed) with row and column totals")))

    # Q6 M advanced nonlinear_functions — solve for a coefficient from a point
    assert _solve(Eq(x * (4 - 2) ** 2 + 3, 11), x) == [2]
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q06", M, 6, "advanced_math", "nonlinear_functions", "medium",
        r"The graph of $y = a(x - 2)^2 + 3$ in the $xy$-plane passes through"
        r" the point $(4, 11)$. What is the value of $a$?",
        r"Substitute the coordinates of the point and solve for $a$:"
        r" $$11 = a(4 - 2)^2 + 3 \;\Rightarrow\; 11 = 4a + 3"
        r" \;\Rightarrow\; 4a = 8 \;\Rightarrow\; a = 2.$$"
        r" Forgetting to square the 2 gives $2a + 3 = 11$, or $a = 4$;"
        r" ignoring the $+3$ gives $\frac{11}{4}$."
        r" The correct answer is **A**.",
        ["Eq(2*(4 - 2)**2 + 3, 11)", "Eq((4 - 2)**2, 4)"],
        2, {Rational(11, 4): "ignored the constant 3",
            4: "forgot to square the quantity in parentheses",
            8: "stopped at 4a = 8"}, fmt=smart))

    # Q7 SPR M advanced nonlinear_equations_systems — rational equation
    assert _solve(Eq((x + 6) / (x - 2), 4), x) == [Rational(14, 3)]
    qs.append(spr(
        "SAT-P7-M2H-Q07", M, 7, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"$$\frac{x + 6}{x - 2} = 4$$"
        r" What is the solution to the equation above?",
        ["14/3"],
        r"Multiply both sides by $x - 2$ (which is nonzero at the solution):"
        r" $$x + 6 = 4(x - 2) = 4x - 8.$$"
        r" Collect terms:"
        r" $$14 = 3x \;\Rightarrow\; x = \frac{14}{3}.$$"
        r" Check that the denominator does not vanish: $\frac{14}{3} \ne 2$,"
        r" so the solution is valid."
        r" The correct answer is **14/3**.",
        ["Eq(Rational(14,3) + 6, 4*(Rational(14,3) - 2))",
         "Ne(Rational(14,3), 2)"]))

    # Q8 M algebra systems_two_linear — mixture with a stated total
    _mx = _solve([Eq(x + y, 40), Eq(Rational(3, 10) * x + Rational(8, 10) * y,
                                    Rational(5, 10) * 40)], [x, y], dict=True)[0]
    assert _mx[x] == 24 and _mx[y] == 16
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q08", M, 8, "algebra", "systems_two_linear", "medium",
        r"A lab combines a $30\%$ saline solution with an $80\%$ saline"
        r" solution to make $40$ liters of a $50\%$ saline solution. How many"
        r" liters of the $30\%$ solution are used?",
        r"Let $a$ and $b$ be the liters of the $30\%$ and $80\%$ solutions."
        r" Volume and salt each give an equation:"
        r" $$a + b = 40, \qquad 0.3a + 0.8b = 0.5(40) = 20.$$"
        r" Substitute $b = 40 - a$:"
        r" $$0.3a + 0.8(40 - a) = 20 \;\Rightarrow\; -0.5a + 32 = 20"
        r" \;\Rightarrow\; a = 24.$$"
        r" Check: $0.3(24) + 0.8(16) = 7.2 + 12.8 = 20$. Reporting the $80\%$"
        r" solution gives 16, and splitting evenly gives 20."
        r" The correct answer is **C**.",
        ["Eq(24 + 16, 40)",
         "Eq(Rational(3,10)*24 + Rational(8,10)*16, 20)",
         "Eq(Rational(5,10)*40, 20)"],
        24, {16: "reported the liters of the 80 percent solution",
             20: "split the 40 liters evenly",
             30: "used the percent as a volume"}, fmt=smart))

    # Q9 M geometry circles — radius perpendicular to a chord bisects it
    assert 5**2 + 12**2 == 13**2
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q09", M, 9, "geometry_trig", "circles", "medium",
        r"A chord of a circle has length $24$, and the distance from the"
        r" center of the circle to the chord is $5$. What is the radius of the"
        r" circle?",
        r"The segment from the center perpendicular to a chord BISECTS the"
        r" chord, so it meets the chord at its midpoint, $12$ from each end."
        r" That segment, half the chord, and a radius form a right triangle:"
        r" $$r^2 = 5^2 + 12^2 = 25 + 144 = 169,$$"
        r" so $r = 13$. Using the FULL chord length 24 as a leg gives"
        r" $\sqrt{601} \approx 24.5$; adding $5 + 12$ gives 17."
        r" The correct answer is **B**.",
        ["Eq(Rational(24,2), 12)", "Eq(5**2 + 12**2, 169)",
         "Eq(sqrt(169), 13)"],
        13, {12: "reported half the chord", 17: "added 5 and 12",
             29: "added 5 and the full chord length"}, fmt=smart))

    # Q10 H algebra linear_equations_two_var — distance between intercepts
    assert _solve(Eq(3 * x - 4 * 0, 12), x) == [4]
    assert _solve(Eq(3 * 0 - 4 * y, 12), y) == [-3]
    assert 4**2 + 3**2 == 25
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q10", M, 10, "algebra", "linear_equations_two_var", "hard",
        r"In the $xy$-plane, the graph of $3x - 4y = 12$ crosses the $x$-axis"
        r" at point $P$ and the $y$-axis at point $Q$. What is the distance"
        r" between $P$ and $Q$?",
        r"Find each intercept by zeroing the other variable:"
        r" $$y = 0:\; 3x = 12 \;\Rightarrow\; P = (4, 0),$$"
        r" $$x = 0:\; -4y = 12 \;\Rightarrow\; Q = (0, -3).$$"
        r" The two intercepts and the origin form a right triangle with legs 4"
        r" and 3, so"
        r" $$PQ = \sqrt{4^2 + 3^2} = \sqrt{25} = 5.$$"
        r" Adding the intercept values gives 7, and using $4 - 3$ gives 1."
        r" The correct answer is **C**.",
        ["Eq(3*4 - 4*0, 12)", "Eq(3*0 - 4*(-3), 12)",
         "Eq(sqrt(4**2 + 3**2), 5)"],
        5, {1: "subtracted the intercept values", 7: "added the intercept values",
            12: "used the constant term as the distance"}, fmt=smart))

    # Q11 H advanced nonlinear_functions — exponential equation by matching
    # bases (8 and 4 both rewritten as powers of 2)
    assert _solve(Eq(3 * (x + 1), 2 * (x + 4)), x) == [5]
    assert 8 ** (5 + 1) == 4 ** (5 + 4)
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q11", M, 11, "advanced_math", "nonlinear_functions", "hard",
        r"If $8^{\,x + 1} = 4^{\,x + 4}$, what is the value of $x$?",
        r"The bases differ, so rewrite both as powers of 2 and use"
        r" $(a^m)^n = a^{mn}$:"
        r" $$8^{\,x+1} = \left(2^3\right)^{x+1} = 2^{\,3x + 3}, \qquad"
        r" 4^{\,x+4} = \left(2^2\right)^{x+4} = 2^{\,2x + 8}.$$"
        r" With the same base on both sides, the exponents must be equal:"
        r" $$3x + 3 = 2x + 8 \;\Rightarrow\; x = 5.$$"
        r" Check: $8^6 = 262{,}144$ and $4^9 = 262{,}144$."
        r" Forgetting to distribute — setting $3x + 1 = 2x + 4$ — gives 3, and"
        r" mismatching the constants as $3x + 3 = 2x + 4$ gives 1."
        r" The correct answer is **C**.",
        ["Eq(3*(5 + 1), 2*(5 + 4))", "Eq(8**6, 4**9)",
         "Eq(8**(5 + 1), 4**(5 + 4))"],
        5, {1: "mismatched the constants as 3x + 3 = 2x + 4",
            3: "did not distribute the exponents",
            11: "solved 3x + 3 = 2x + 14"}, fmt=smart))

    # Q12 SPR H advanced nonlinear_equations_systems — sum and product of roots
    assert sorted(_solve(Eq(x**2 - 7 * x + 10, 0), x)) == [2, 5]
    qs.append(spr(
        "SAT-P7-M2H-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"The solutions to $x^2 - 7x + 10 = 0$ are $p$ and $q$. What is the"
        r" value of $\dfrac{1}{p} + \dfrac{1}{q}$?",
        ["7/10", ".7", "0.7"],
        r"Combine the fractions over a common denominator:"
        r" $$\frac{1}{p} + \frac{1}{q} = \frac{p + q}{pq}.$$"
        r" For $x^2 + bx + c = 0$ the sum of the solutions is $-b$ and the"
        r" product is $c$, so here $p + q = 7$ and $pq = 10$:"
        r" $$\frac{7}{10} = 0.7.$$"
        r" No factoring is needed — though checking with the actual roots 2"
        r" and 5 confirms it: $\frac{1}{2} + \frac{1}{5} = \frac{7}{10}$."
        r" The correct answer is **7/10**.",
        ["Eq(2 + 5, 7)", "Eq(2*5, 10)",
         "Eq(Rational(1,2) + Rational(1,5), Rational(7,10))"]))

    # Q13 H algebra linear_inequalities — feasible integer pair count
    assert [b for b in range(0, 20) if 7 * 4 + 5 * b <= 60] == list(range(0, 7))
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q13", M, 13, "algebra", "linear_inequalities", "hard",
        r"A vendor sells notebooks for $\$7$ each and pens for $\$5$ each. A"
        r" customer buys exactly $4$ notebooks and some pens, spending no more"
        r" than $\$60$ in total. What is the greatest number of pens the"
        r" customer can buy?",
        r"The notebooks cost $4(7) = 28$ dollars, leaving the pens to satisfy"
        r" $$28 + 5p \le 60 \;\Rightarrow\; 5p \le 32"
        r" \;\Rightarrow\; p \le 6.4.$$"
        r" Since pens come in whole numbers, the greatest possible count is 6."
        r" Rounding $6.4$ UP to 7 would push the total to"
        r" $28 + 35 = 63 > 60$ — with an at-most constraint the count must"
        r" round DOWN. Ignoring the notebooks gives $\frac{60}{5} = 12$."
        r" The correct answer is **B**.",
        ["Eq(4*7, 28)", "28 + 5*6 <= 60", "Not(28 + 5*7 <= 60)"],
        6, {4: "reported the number of notebooks",
            7: "rounded 6.4 up despite the at-most limit",
            12: "ignored the cost of the notebooks"}, fmt=smart))

    # Q14 H advanced equivalent_expressions — simplify a compound fraction
    assert simplify((1 - 1 / x) / (1 - 1 / x**2) - x / (x + 1)) == 0
    qs.append(mcq_listed(
        "SAT-P7-M2H-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "hard",
        r"For $x > 1$, which of the following is equivalent to"
        r" $\dfrac{1 - \frac{1}{x}}{1 - \frac{1}{x^2}}$?",
        {"A": r"$\dfrac{1}{x + 1}$", "B": r"$\dfrac{x}{x + 1}$",
         "C": r"$\dfrac{x + 1}{x}$", "D": r"$x + 1$"}, "B",
        r"Multiply numerator and denominator by $x^2$ to clear the inner"
        r" fractions:"
        r" $$\frac{x^2 - x}{x^2 - 1}.$$"
        r" Now factor both:"
        r" $$\frac{x(x - 1)}{(x - 1)(x + 1)} = \frac{x}{x + 1},$$"
        r" cancelling the common factor $x - 1$, which is nonzero since"
        r" $x > 1$."
        r" A quick numerical check at $x = 2$: the original is"
        r" $\frac{1 - 0.5}{1 - 0.25} = \frac{0.5}{0.75} = \frac{2}{3}$, and"
        r" $\frac{x}{x+1} = \frac{2}{3}$."
        r" The correct answer is **B**.",
        ["Eq(simplify((1 - 1/x)/(1 - 1/x**2) - x/(x + 1)), 0)",
         "Eq(simplify(((1 - Rational(1,2))/(1 - Rational(1,4)))), Rational(2,3))"]))

    # Q15 SPR H psda one_var_data — weighted mean of two groups
    assert Rational(12 * 78 + 18 * 88, 12 + 18) == 84
    qs.append(spr(
        "SAT-P7-M2H-Q15", M, 15, "psda", "one_var_data", "hard",
        r"In a class, $12$ students have a mean score of $78$ and the other"
        r" $18$ students have a mean score of $88$. What is the mean score of"
        r" all $30$ students?",
        ["84"],
        r"Means of unequal groups cannot simply be averaged. Recover each"
        r" group's TOTAL, then combine:"
        r" $$12 \times 78 = 936, \qquad 18 \times 88 = 1584.$$"
        r" $$\text{mean} = \frac{936 + 1584}{30} = \frac{2520}{30} = 84.$$"
        r" Averaging 78 and 88 directly gives 83, which is wrong because the"
        r" larger group pulls the mean toward 88 — the answer must lie closer"
        r" to 88 than to 78, and 84 does."
        r" The correct answer is **84**.",
        ["Eq(12*78, 936)", "Eq(18*88, 1584)",
         "Eq(Rational(936 + 1584, 30), 84)", "84 > Rational(78 + 88, 2)"]))

    # Q16 H algebra linear_equations_two_var — recover a coefficient from an
    # intercept
    assert _solve(Eq(x * 3, 12), x) == [4] and 3 * 4 == 12
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q16", M, 16, "algebra", "linear_equations_two_var", "hard",
        r"In the $xy$-plane, the graph of $3x + ky = 12$, where $k$ is a"
        r" constant, has a $y$-intercept at $(0, 3)$. What is the value of"
        r" $k$?",
        r"A $y$-intercept has $x = 0$, so substitute both coordinates of the"
        r" point:"
        r" $$3(0) + k(3) = 12 \;\Rightarrow\; 3k = 12 \;\Rightarrow\; k = 4.$$"
        r" Check the whole picture: with $k = 4$ the equation is"
        r" $3x + 4y = 12$, whose $x$-intercept is $(4, 0)$ and whose"
        r" $y$-intercept is indeed $(0, 3)$."
        r" Substituting $y = 0$ instead uses the wrong intercept and gives"
        r" nothing about $k$; reporting the constant term gives 12, and"
        r" $\frac{12}{12}$ gives 1."
        r" The correct answer is **C**.",
        ["Eq(3*0 + 4*3, 12)", "Eq(3*4 + 4*0, 12)", "Eq(Rational(12,3), 4)"],
        4, {1: "divided 12 by 12", 3: "reported the y-coordinate given",
            12: "reported the constant term"}, fmt=smart))

    # Q17 H advanced nonlinear_functions — transformed graph's intercept
    assert 2 * (0 + 3) ** 2 - 5 == 13
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q17", M, 17, "advanced_math", "nonlinear_functions", "hard",
        r"The function $f$ is defined by $f(x) = 2x^2 - 5$. The function $g$"
        r" is defined by $g(x) = f(x + 3)$. What is the $y$-intercept of the"
        r" graph of $y = g(x)$ in the $xy$-plane?",
        r"The $y$-intercept is the value at $x = 0$. Apply the definition of"
        r" $g$ before evaluating $f$:"
        r" $$g(0) = f(0 + 3) = f(3) = 2(3)^2 - 5 = 18 - 5 = 13.$$"
        r" Evaluating $f(0) = -5$ ignores the shift; adding 3 to $f(0)$ gives"
        r" $-2$, which mistakes a horizontal shift for a vertical one."
        r" The correct answer is **D**.",
        ["Eq(2*3**2 - 5, 13)", "Eq(2*0**2 - 5, -5)"],
        13, {-5: "evaluated f(0), ignoring the shift",
             -2: "added 3 to f(0), treating the shift as vertical",
             4: "used x + 3 = 2 by mistake"}, fmt=smart))

    # Q18 H geometry right_triangles_trig — tangent ratio to find a leg
    assert Rational(3, 4) * 20 == 15
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q18", M, 18, "geometry_trig", "right_triangles_trig", "hard",
        r"In right triangle $ABC$, the right angle is at $C$, the leg $BC$"
        r" adjacent to angle $B$ has length $20$, and"
        r" $\tan B = \dfrac{3}{4}$. What is the length of leg $AC$?",
        r"Tangent is opposite over adjacent. From angle $B$, the opposite leg"
        r" is $AC$ and the adjacent leg is $BC = 20$:"
        r" $$\tan B = \frac{AC}{20} = \frac{3}{4}"
        r" \;\Rightarrow\; AC = 20 \cdot \frac{3}{4} = 15.$$"
        r" Inverting the ratio gives $20 \cdot \frac{4}{3} \approx 26.7$, and"
        r" the hypotenuse (from the $3$-$4$-$5$ triple scaled by 5) is 25 —"
        r" not what was asked."
        r" The correct answer is **B**.",
        ["Eq(Rational(3,4)*20, 15)", "Eq(15**2 + 20**2, 25**2)"],
        15, {12: "used 3/5 instead of 3/4",
             25: "reported the hypotenuse",
             Rational(80, 3): "inverted the tangent ratio"}, fmt=smart))

    # Q19 SPR H psda percentages — percent OF a percent
    assert Rational(60, 100) * Rational(45, 100) * 2000 == 540
    qs.append(spr(
        "SAT-P7-M2H-Q19", M, 19, "psda", "percentages", "hard",
        r"At a school, $45\%$ of the $2{,}000$ students play a sport, and"
        r" $60\%$ of the students who play a sport also play an instrument."
        r" How many students play both a sport and an instrument?",
        ["540"],
        r"The second percent is taken OF the first group, not of the whole"
        r" school. First find the sport-playing group:"
        r" $$0.45 \times 2000 = 900.$$"
        r" Then take $60\%$ of THAT group:"
        r" $$0.60 \times 900 = 540.$$"
        r" Applying both percents to the full enrollment separately, or adding"
        r" them to get $105\%$, both misread the nesting."
        r" The correct answer is **540**.",
        ["Eq(Rational(45,100)*2000, 900)", "Eq(Rational(60,100)*900, 540)",
         "Eq(Rational(27,100)*2000, 540)"]))

    # Q20 H algebra systems_two_linear — parameter making the system consistent
    assert Rational(10, 4) == Rational(15, 6)
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q20", M, 20, "algebra", "systems_two_linear", "hard",
        r"$$4x + 6y = c$$ $$10x + 15y = 40$$"
        r" In the system of equations above, $c$ is a constant. For what value"
        r" of $c$ does the system have infinitely many solutions?",
        r"The coefficients are already proportional:"
        r" $$\frac{10}{4} = \frac{15}{6} = \frac{5}{2},$$"
        r" so the two equations describe parallel lines for every $c$. They"
        r" describe the SAME line — infinitely many solutions — exactly when"
        r" the constants share that ratio too:"
        r" $$\frac{40}{c} = \frac{5}{2} \;\Rightarrow\; c = 16.$$"
        r" Check: multiplying $4x + 6y = 16$ by $\frac{5}{2}$ gives"
        r" $10x + 15y = 40$. Any other $c$ makes the lines parallel and"
        r" distinct, with NO solution. Dividing 40 by 4 gives 10, and using"
        r" the reciprocal ratio gives 100."
        r" The correct answer is **B**.",
        ["Eq(Rational(10,4), Rational(15,6))",
         "Eq(Rational(5,2)*16, 40)",
         "Eq(simplify(Rational(5,2)*(4*x + 6*y)), 10*x + 15*y)"],
        16, {10: "divided 40 by 4", 24: "used the ratio 3 to 2",
             100: "multiplied 40 by the reciprocal ratio"}, fmt=smart))

    # Q21 H advanced nonlinear_equations_systems — extraneous root check
    assert _solve(Eq(sqrt(2 * x + 15), x), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P7-M2H-Q21", M, 21, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"$$\sqrt{2x + 15} = x$$"
        r" What is the solution to the equation above?",
        r"Square both sides and collect:"
        r" $$2x + 15 = x^2 \;\Rightarrow\; x^2 - 2x - 15 = 0"
        r" \;\Rightarrow\; (x - 5)(x + 3) = 0.$$"
        r" The candidates are $x = 5$ and $x = -3$, but squaring can create"
        r" solutions the original equation does not have, so BOTH must be"
        r" checked. For $x = 5$: $\sqrt{25} = 5$. For $x = -3$:"
        r" $\sqrt{9} = 3 \ne -3$, since the radical sign denotes the"
        r" non-negative root. So $x = -3$ is extraneous and $x = 5$ is the"
        r" only solution."
        r" The correct answer is **C**.",
        ["Eq(expand((x - 5)*(x + 3)), x**2 - 2*x - 15)",
         "Eq(sqrt(2*5 + 15), 5)", "Ne(sqrt(2*(-3) + 15), -3)"],
        5, {-3: "kept the extraneous root", 3: "took the square root of 9 as x",
            15: "used the constant term"}, fmt=smart))

    # Q22 SPR H algebra linear_functions — parameter from two function values
    assert Rational(26, 4) == Rational(13, 2)
    qs.append(spr(
        "SAT-P7-M2H-Q22", M, 22, "algebra", "linear_functions", "hard",
        r"For the linear function $f$, $f(x + 4) - f(x) = 26$ for every value"
        r" of $x$. What is the slope of the graph of $y = f(x)$ in the"
        r" $xy$-plane?",
        ["6.5", "13/2"],
        r"For a linear function, the change in output over the change in input"
        r" IS the slope, and it is the same everywhere. The input rose by 4"
        r" and the output rose by 26, so"
        r" $$m = \frac{26}{4} = 6.5.$$"
        r" Reporting 26 treats the rise as if the input had increased by 1."
        r" The correct answer is **6.5**.",
        ["Eq(Rational(26,4), Rational(13,2))",
         "Abs(Rational(13,2) - 6.5) < Rational(1,1000)"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-7.json",
               {"testId": "sat-practice-7",
                "label": "SAT Math Practice Test 7",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
