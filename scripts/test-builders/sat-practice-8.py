#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 8 (data/sat/sat-practice-8.json).

Built on scripts/test-builders/satbuild.py — only stems, parameters,
computed answers, named distractor error models, verify[] strings, and
solutions live here.

Archetype freshness versus tests 1-7 (audited before authoring). New to
the bank in this test:
  * a linear model built from two context points, then extrapolated
  * a proportion with the unknown in a denominator
  * unit conversion chained through TWO rates (a dimensional-analysis item)
  * "which expression must be an integer" reasoning about parity
  * an inequality whose variable appears on both sides
  * a system where the question asks for a LINEAR COMBINATION (3x - y)
  * the second difference of a quadratic table
  * completing the square to read a MINIMUM off vertex form
  * a piecewise function evaluated on both branches
  * an exponential model compared against a linear one
  * probability of a COMPLEMENT, and "at least one" counting
  * a weighted average with an unknown weight
  * the midpoint of a segment, and an endpoint recovered from a midpoint
  * a triangle's third-side range (the triangle inequality)
  * a sector AREA (not arc length) and a circle from its diameter endpoints
  * the slant height of a cone via the Pythagorean theorem
  * the ratio of surface areas of similar solids

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
    return rf"$\${float(Fraction(v)):g}$"


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E algebra one_var
    assert _solve(Eq(9 - 2 * x, 1), x) == [4]
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $9 - 2x = 1$, what is the value of $x$?",
        r"Subtract 9 from both sides, then divide by $-2$:"
        r" $$-2x = -8 \;\Rightarrow\; x = 4.$$"
        r" Dropping the negative on the left gives $2x = -8$, or $-4$, and"
        r" $9 - 1 = 8$ without dividing gives 8."
        r" The correct answer is **C**.",
        ["Eq(9 - 2*4, 1)", "Eq((9 - 1)/2, 4)"],
        4, {-4: "dropped a negative sign when dividing",
            5: "subtracted 1 from 9 and divided by 2 incorrectly",
            8: "stopped at 2x = 8"}, fmt=smart))

    # Q2 E advanced equivalent_expressions — multiply a binomial by a monomial
    assert expand(4 * x * (2 * x - 7)) == 8 * x**2 - 28 * x
    qs.append(mcq_listed(
        "SAT-P8-M1-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $4x(2x - 7)$?",
        {"A": r"$6x^2 - 28x$", "B": r"$8x^2 - 7$", "C": r"$8x^2 - 28x$",
         "D": r"$8x^2 - 28$"}, "C",
        r"Distribute $4x$ across both terms, adding exponents on the first:"
        r" $$4x \cdot 2x = 8x^2, \qquad 4x \cdot (-7) = -28x.$$"
        r" So the product is $8x^2 - 28x$. Forgetting to multiply the second"
        r" term by $x$ gives $-28$, and adding the coefficients instead of"
        r" multiplying gives $6x^2$."
        r" The correct answer is **C**.",
        ["Eq(expand(4*x*(2*x - 7)), 8*x**2 - 28*x)",
         "Eq(expand(4*x*(2*x - 7)).subs(x, 1), -20)"]))

    # Q3 E psda ratios_rates_units — proportion with the unknown below
    assert _solve(Eq(Rational(5, 8), 15 / x), x) == [24]
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q03", M, 3, "algebra", "linear_equations_one_var", "easy",
        r"If $\dfrac{5}{8} = \dfrac{15}{x}$, what is the value of $x$?",
        r"Cross-multiply:"
        r" $$5x = 8 \cdot 15 = 120 \;\Rightarrow\; x = 24.$$"
        r" Notice $15 = 3 \times 5$, so $x = 3 \times 8 = 24$ — the same scale"
        r" factor applies to both parts of the ratio."
        r" Multiplying $8 \times 15$ without dividing gives 120, and adding"
        r" the difference $15 - 5 = 10$ to 8 gives 18."
        r" The correct answer is **C**.",
        ["Eq(5*24, 8*15)", "Eq(Rational(15,24), Rational(5,8))"],
        24, {18: "added the difference of the numerators to 8",
             40: "multiplied 8 by 5", 120: "did not divide by 5"}, fmt=smart))

    # Q4 SPR E algebra linear_functions — midpoint of a segment
    assert Rational(3 + 11, 2) == 7 and Rational(2 + 8, 2) == 5
    qs.append(spr(
        "SAT-P8-M1-Q04", M, 4, "algebra", "linear_equations_two_var", "easy",
        r"In the $xy$-plane, the midpoint of the segment joining $(3, 2)$ and"
        r" $(11, 8)$ is $(a, b)$. What is the value of $a$?",
        ["7"],
        r"Each coordinate of a midpoint is the average of the corresponding"
        r" coordinates:"
        r" $$a = \frac{3 + 11}{2} = 7, \qquad b = \frac{2 + 8}{2} = 5.$$"
        r" The question asks only for $a$, so the answer is 7."
        r" The correct answer is **7**.",
        ["Eq(Rational(3 + 11, 2), 7)", "Eq(Rational(2 + 8, 2), 5)"]))

    # Q5 E geometry area_volume — area of a parallelogram
    assert 13 * 6 == 78
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        r"A parallelogram has a base of length $13$ and a height of $6$ drawn"
        r" to that base. What is the area of the parallelogram?",
        r"The area of a parallelogram is base times height — no factor of"
        r" $\frac{1}{2}$, unlike a triangle:"
        r" $$A = 13 \times 6 = 78.$$"
        r" Halving as if it were a triangle gives 39, and adding the two"
        r" measurements gives 19."
        r" The correct answer is **D**.",
        ["Eq(13*6, 78)", "Eq(Rational(13*6, 2), 39)"],
        78, {19: "added the base and height",
             38: "computed the perimeter of a 13 by 6 rectangle",
             39: "halved the product as if it were a triangle"}, fmt=smart))

    # Q6 E advanced nonlinear_functions — piecewise evaluation
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = x^2 + 1$ for $x < 3$ and"
        r" $f(x) = 4x - 5$ for $x \ge 3$. What is the value of $f(5)$?",
        r"Choose the branch by testing the input against the condition. Since"
        r" $5 \ge 3$, use the SECOND rule:"
        r" $$f(5) = 4(5) - 5 = 15.$$"
        r" Using the first branch — which applies only when $x < 3$ — would"
        r" give $5^2 + 1 = 26$."
        r" The correct answer is **B**.",
        ["Eq(4*5 - 5, 15)", "Eq(5**2 + 1, 26)", "5 >= 3"],
        15, {10: "evaluated 4x - 5 at x = 3",
             26: "used the branch for x < 3",
             20: "omitted the constant term"}, fmt=smart))

    # Q7 E algebra linear_functions — build a model from two context points
    assert Rational(58 - 34, 8 - 2) == 4 and 34 - 4 * 2 == 26
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q07", M, 7, "algebra", "linear_functions", "easy",
        r"A candle burns at a constant rate. After $2$ hours it is $34$"
        r" centimeters tall, and after $8$ hours it is $58$ centimeters"
        r" tall — the candle is being MOLDED, not burned, and grows at a"
        r" constant rate. What was its height, in centimeters, at time $0$?",
        r"Constant rate means a linear model. The rate is"
        r" $$m = \frac{58 - 34}{8 - 2} = \frac{24}{6} = 4$$"
        r" centimeters per hour. Working back from the 2-hour reading:"
        r" $$h(0) = 34 - 4(2) = 26.$$"
        r" Check with the other point: $26 + 4(8) = 58$."
        r" Reporting the 2-hour reading itself gives 34, and adding the growth"
        r" instead of subtracting gives 90."
        r" The correct answer is **A**.",
        ["Eq(Rational(58 - 34, 8 - 2), 4)", "Eq(26 + 4*2, 34)",
         "Eq(26 + 4*8, 58)"],
        26, {30: "used a rate of 2 centimeters per hour",
             34: "reported the height at 2 hours",
             90: "added the growth instead of subtracting"}, fmt=smart))

    # Q8 E psda one_var_data — mode and range from a list
    DATA8 = [7, 9, 9, 12, 15, 15, 15, 20]
    assert max(DATA8) - min(DATA8) == 13
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q08", M, 8, "psda", "one_var_data", "easy",
        r"A data set consists of the values $7$, $9$, $9$, $12$, $15$, $15$,"
        r" $15$, $20$. What is the range of the data set?",
        r"The range is the largest value minus the smallest:"
        r" $$20 - 7 = 13.$$"
        r" The value 15 appears most often, so it is the MODE, not the range;"
        r" and the middle two values average to $\frac{12 + 15}{2} = 13.5$,"
        r" the median."
        r" The correct answer is **B**.",
        ["Eq(20 - 7, 13)", "Eq(Rational(12 + 15, 2), Rational(27,2))"],
        13, {8: "counted the number of values",
             15: "reported the mode",
             20: "reported the largest value"}, fmt=smart))

    # Q9 SPR M advanced nonlinear_equations_systems — second difference of a
    # quadratic table
    Q9X, Q9Y = [0, 1, 2, 3], [5, 8, 15, 26]
    _d1 = [Q9Y[i + 1] - Q9Y[i] for i in range(3)]
    _d2 = [_d1[i + 1] - _d1[i] for i in range(2)]
    assert _d1 == [3, 7, 11] and _d2 == [4, 4]
    assert all(2 * xx**2 + xx + 5 == yy for xx, yy in zip(Q9X, Q9Y))
    qs.append(spr(
        "SAT-P8-M1-Q09", M, 9, "advanced_math", "nonlinear_functions", "medium",
        r"The table shows four values of a quadratic function $g$. What is the"
        r" value of $g(4)$?",
        ["41"],
        r"For a quadratic sampled at equally spaced inputs, the SECOND"
        r" differences are constant. The first differences are"
        r" $$8 - 5 = 3, \quad 15 - 8 = 7, \quad 26 - 15 = 11,$$"
        r" and their differences are $7 - 3 = 4$ and $11 - 7 = 4$ — constant,"
        r" as expected. So the next first difference is $11 + 4 = 15$, giving"
        r" $$g(4) = 26 + 15 = 41.$$"
        r" (The function is $g(x) = 2x^2 + x + 5$, which confirms"
        r" $g(4) = 32 + 4 + 5 = 41$.) Continuing the FIRST differences as if"
        r" they were constant would wrongly give $26 + 11 = 37$."
        r" The correct answer is **41**.",
        ["Eq(2*4**2 + 4 + 5, 41)", "Eq(26 + 15, 41)",
         "Eq((15 - 8) - (8 - 5), 4)", "Eq((26 - 15) - (15 - 8), 4)"],
        fig=figure("sat-p8-m1-q09",
                   "Two-row table of x values 0, 1, 2, 3 against g(x) values "
                   "5, 8, 15, 26")))

    # Q10 M psda probability_conditional — probability of a COMPLEMENT
    assert Rational(9 + 6, 40) == Rational(3, 8)
    qs.append(mcq_listed(
        "SAT-P8-M1-Q10", M, 10, "psda", "probability_conditional", "medium",
        r"A box contains $40$ marbles: $9$ are red, $6$ are green, and the"
        r" rest are blue. If one marble is selected at random, what is the"
        r" probability that it is NOT blue?",
        {"A": r"$\dfrac{1}{4}$", "B": r"$\dfrac{3}{8}$", "C": r"$\dfrac{5}{8}$",
         "D": r"$\dfrac{3}{4}$"}, "B",
        r"''Not blue'' means red or green, so count those directly:"
        r" $$9 + 6 = 15, \qquad P = \frac{15}{40} = \frac{3}{8}.$$"
        r" Equivalently, use the complement: there are $40 - 15 = 25$ blue"
        r" marbles, so"
        r" $$P(\text{not blue}) = 1 - \frac{25}{40} = 1 - \frac{5}{8}"
        r" = \frac{3}{8}.$$"
        r" Answering $\frac{5}{8}$ gives the probability the marble IS blue —"
        r" the complement of what was asked."
        r" The correct answer is **B**.",
        ["Eq(9 + 6, 15)", "Eq(Rational(15,40), Rational(3,8))",
         "Eq(40 - 15, 25)", "Eq(1 - Rational(25,40), Rational(3,8))"]))

    # Q11 M algebra systems_two_linear — asks for a LINEAR COMBINATION
    _s = _solve([Eq(2 * x + y, 11), Eq(x - 2 * y, 3)], [x, y], dict=True)[0]
    assert _s[x] == 5 and _s[y] == 1 and 3 * 5 - 1 == 14
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q11", M, 11, "algebra", "systems_two_linear", "medium",
        r"$$2x + y = 11$$ $$x - 2y = 3$$"
        r" If $(x, y)$ is the solution to the system of equations above, what"
        r" is the value of $3x - y$?",
        r"Solve the system first. From the second equation $x = 2y + 3$;"
        r" substituting into the first gives"
        r" $$2(2y + 3) + y = 11 \;\Rightarrow\; 5y + 6 = 11"
        r" \;\Rightarrow\; y = 1,$$"
        r" and then $x = 5$. Both originals check:"
        r" $2(5) + 1 = 11$ and $5 - 2(1) = 3$. Now evaluate what was asked:"
        r" $$3x - y = 15 - 1 = 14.$$"
        r" Reporting $x$ alone gives 5, and $3x + y$ gives 16."
        r" The correct answer is **C**.",
        ["Eq(2*5 + 1, 11)", "Eq(5 - 2*1, 3)", "Eq(3*5 - 1, 14)"],
        14, {5: "reported x instead of 3x - y", 6: "computed x + y",
             16: "computed 3x + y"}, fmt=smart))

    # Q12 M advanced nonlinear_functions — completing the square for a minimum
    assert expand((x - 4) ** 2 - 3) == x**2 - 8 * x + 13
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q12", M, 12, "advanced_math", "equivalent_expressions",
        "medium",
        r"The expression $x^2 - 8x + 13$ can be written in the form"
        r" $(x - h)^2 + k$, where $h$ and $k$ are constants. What is the value"
        r" of $k$?",
        r"Complete the square. Half of $-8$ is $-4$, and $(-4)^2 = 16$:"
        r" $$x^2 - 8x + 13 = (x^2 - 8x + 16) - 16 + 13 = (x - 4)^2 - 3.$$"
        r" So $h = 4$ and $k = -3$. The question asks for $k$."
        r" Reporting $h$ gives 4, and forgetting to subtract the 16 back out"
        r" gives 13."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 4)**2 - 3), x**2 - 8*x + 13)", "Eq((-8/2)**2, 16)"],
        -3, {4: "reported h instead of k", 13: "forgot to subtract 16 back out",
             16: "reported the completing-the-square constant"}, fmt=smart))

    # Q13 M geometry lines_angles_triangles — triangle inequality range
    assert 12 - 5 < 8 < 12 + 5
    qs.append(mcq_listed(
        "SAT-P8-M1-Q13", M, 13, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"Two sides of a triangle have lengths $5$ and $12$. Which of the"
        r" following could be the length of the third side?",
        {"A": r"$5$", "B": r"$7$", "C": r"$8$", "D": r"$17$"}, "C",
        r"The third side must be longer than the difference of the other two"
        r" and shorter than their sum:"
        r" $$12 - 5 < s < 12 + 5, \qquad\text{so}\qquad 7 < s < 17.$$"
        r" Both endpoints are EXCLUDED — a third side of exactly 7 or exactly"
        r" 17 would flatten the triangle into a straight segment. Of the"
        r" choices only $8$ lies strictly between them; $5$ is too short."
        r" The correct answer is **C**.",
        ["Eq(12 - 5, 7)", "Eq(12 + 5, 17)", "(8 > 7) & (8 < 17)",
         "Not((5 > 7) & (5 < 17))"]))

    # Q14 SPR M psda percentages — weighted average with an unknown weight
    assert Rational(20 * 6 + 30 * 4, 6 + 4) == 24
    qs.append(spr(
        "SAT-P8-M1-Q14", M, 14, "psda", "one_var_data", "medium",
        r"A shop mixes $6$ kilograms of tea costing $\$20$ per kilogram with"
        r" $4$ kilograms of tea costing $\$30$ per kilogram. What is the cost,"
        r" in dollars per kilogram, of the mixture?",
        ["24"],
        r"Total the cost and divide by the total weight — not a plain average"
        r" of the two prices, because the amounts differ:"
        r" $$\frac{6(20) + 4(30)}{6 + 4} = \frac{120 + 120}{10}"
        r" = \frac{240}{10} = 24.$$"
        r" Averaging $20$ and $30$ directly gives 25, which is too high — the"
        r" cheaper tea makes up the larger share, so the mixture price must"
        r" sit closer to $20$."
        r" The correct answer is **24**.",
        ["Eq(6*20 + 4*30, 240)", "Eq(Rational(240,10), 24)",
         "24 < Rational(20 + 30, 2)"]))

    # Q15 M algebra linear_inequalities — variable on both sides
    qs.append(mcq_listed(
        "SAT-P8-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"Which of the following gives all solutions of $7 - 2x > 3x - 8$?",
        {"A": r"$x < -3$", "B": r"$x < 3$", "C": r"$x > -3$",
         "D": r"$x > 3$"}, "B",
        r"Collect the variable on the side that keeps its coefficient"
        r" positive. Adding $2x$ and $8$ to both sides:"
        r" $$15 > 5x \;\Rightarrow\; 3 > x,$$"
        r" which is $x < 3$. Because $5$ is positive, the inequality sign never"
        r" flips."
        r" Moving the $3x$ left instead gives $-5x > -15$, and dividing by the"
        r" NEGATIVE $-5$ requires flipping the sign — landing on the same"
        r" $x < 3$. Forgetting to flip there produces $x > 3$."
        r" The correct answer is **B**.",
        ["7 - 2*0 > 3*0 - 8", "Not(7 - 2*4 > 3*4 - 8)",
         "Eq(Rational(7 + 8, 2 + 3), 3)"]))

    # Q16 M advanced nonlinear_equations_systems — solve by substitution
    assert sorted(_solve([Eq(y, x**2), Eq(y, 6 * x - 8)], [x, y])) == \
        [(2, 4), (4, 16)]
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q16", M, 16, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"$$y = x^2$$ $$y = 6x - 8$$"
        r" The graphs of the equations above intersect at two points. What is"
        r" the sum of the $y$-coordinates of those two points?",
        r"Substitute the first equation into the second:"
        r" $$x^2 = 6x - 8 \;\Rightarrow\; x^2 - 6x + 8 = 0"
        r" \;\Rightarrow\; (x - 2)(x - 4) = 0.$$"
        r" So $x = 2$ and $x = 4$. The question asks for the $y$-values, which"
        r" come from $y = x^2$:"
        r" $$y = 4 \quad\text{and}\quad y = 16, \qquad 4 + 16 = 20.$$"
        r" Summing the $x$-coordinates instead gives $2 + 4 = 6$ — the most"
        r" common slip on this question."
        r" The correct answer is **D**.",
        ["Eq(expand((x - 2)*(x - 4)), x**2 - 6*x + 8)",
         "Eq(2**2, 6*2 - 8)", "Eq(4**2, 6*4 - 8)", "Eq(4 + 16, 20)"],
        20, {6: "summed the x-coordinates instead",
             12: "summed x and y of one point", 16: "gave only the larger y"},
        fmt=smart))

    # Q17 M geometry circles — sector AREA
    assert Rational(45, 360) * 12**2 == 18
    qs.append(mcq_listed(
        "SAT-P8-M1-Q17", M, 17, "geometry_trig", "circles", "medium",
        r"A circle has a radius of $12$. What is the area of a sector of this"
        r" circle with a central angle of $45^\circ$?",
        {"A": r"$3\pi$", "B": r"$6\pi$", "C": r"$18\pi$", "D": r"$36\pi$"},
        "C",
        r"A sector's area is the same fraction of the circle's area that its"
        r" central angle is of a full turn:"
        r" $$\frac{45}{360} = \frac{1}{8}.$$"
        r" The full area is $\pi r^2 = 144\pi$, so"
        r" $$\text{sector} = \frac{1}{8}(144\pi) = 18\pi.$$"
        r" Applying the fraction to the CIRCUMFERENCE $24\pi$ instead gives"
        r" $3\pi$ — that is the arc length, a different quantity."
        r" The correct answer is **C**.",
        ["Eq(Rational(45,360), Rational(1,8))", "Eq(12**2, 144)",
         "Eq(Rational(144,8), 18)", "Eq(Rational(2*12,8), 3)"]))

    # Q18 SPR H advanced nonlinear_functions — exponential vs linear crossing
    assert 3 * 2**5 == 96 and 5 * 5 + 60 == 85
    qs.append(spr(
        "SAT-P8-M1-Q18", M, 18, "advanced_math", "nonlinear_functions", "hard",
        r"Two populations are modeled by $A(t) = 3 \cdot 2^{\,t}$ and"
        r" $B(t) = 5t + 60$, where $t$ is the number of years. What is the"
        r" least integer value of $t$ for which $A(t) > B(t)$?",
        ["5"],
        r"Compare year by year — exponential growth starts behind and then"
        r" overtakes:"
        r" $$t = 4:\; A = 3 \cdot 16 = 48, \quad B = 80 \quad (A < B),$$"
        r" $$t = 5:\; A = 3 \cdot 32 = 96, \quad B = 85 \quad (A > B).$$"
        r" So the first integer year where $A$ exceeds $B$ is 5. Once an"
        r" exponential passes a linear model it never falls behind again, so"
        r" no later value needs checking."
        r" The correct answer is **5**.",
        ["Eq(3*2**4, 48)", "Eq(5*4 + 60, 80)", "3*2**4 < 5*4 + 60",
         "Eq(3*2**5, 96)", "Eq(5*5 + 60, 85)", "3*2**5 > 5*5 + 60"]))

    # Q19 H psda two_var_data_models — interpret a slope in context
    qs.append(mcq_listed(
        "SAT-P8-M1-Q19", M, 19, "psda", "two_var_data_models", "hard",
        r"A line of best fit for a data set relating the number of hours $x$"
        r" a plant is exposed to light and its growth $y$, in millimeters, is"
        r" $y = 1.8x + 4.5$. Which of the following is the best interpretation"
        r" of $1.8$ in this context?",
        {"A": r"The growth, in millimeters, of a plant exposed to no light.",
         "B": r"The predicted increase in growth, in millimeters, for each"
              r" additional hour of light exposure.",
         "C": r"The predicted number of additional hours of light needed for"
              r" each millimeter of growth.",
         "D": r"The total growth, in millimeters, of a plant exposed to"
              r" $1.8$ hours of light."}, "B",
        r"In a line of best fit $y = mx + b$, the slope $m$ is the predicted"
        r" CHANGE in $y$ for a one-unit increase in $x$. Here $x$ is measured"
        r" in hours and $y$ in millimeters, so $1.8$ carries units of"
        r" millimeters PER HOUR: each extra hour of light predicts $1.8$ more"
        r" millimeters of growth."
        r" The intercept $4.5$ — not the slope — is the prediction at zero"
        r" hours, and reading the rate upside down (hours per millimeter)"
        r" would describe $\frac{1}{1.8}$."
        r" The correct answer is **B**.",
        ["Eq(Rational(9,5)*(4 + 1) + Rational(9,2)"
         " - (Rational(9,5)*4 + Rational(9,2)), Rational(9,5))",
         "Eq(Rational(9,5)*0 + Rational(9,2), Rational(9,2))",
         "Eq(Rational(9,5), Rational(18,10))"]))

    # Q20 H geometry area_volume — slant height of a cone
    assert 9**2 + 12**2 == 15**2
    qs.append(mcq_numeric(
        "SAT-P8-M1-Q20", M, 20, "geometry_trig", "area_volume", "hard",
        r"A right circular cone has a base radius of $9$ and a height of $12$."
        r" What is the slant height of the cone?",
        r"The radius, the height, and the slant height form a right triangle"
        r" inside the cone, with the slant height as the HYPOTENUSE:"
        r" $$\ell^2 = 9^2 + 12^2 = 81 + 144 = 225,$$"
        r" so $\ell = 15$."
        r" Subtracting the squares would treat the slant height as a leg,"
        r" giving about $7.9$; adding the two measurements gives 21."
        r" The correct answer is **B**.",
        ["Eq(9**2 + 12**2, 225)", "Eq(sqrt(225), 15)"],
        15, {3: "subtracted the radius from the height",
             21: "added the radius and the height",
             108: "multiplied the radius by the height"}, fmt=smart,
        fig=figure("sat-p8-m1-q20",
                   "Right triangle with legs 9 and 12 representing the radius "
                   "and height of a cone, the hypotenuse being the slant "
                   "height")))

    # Q21 SPR H algebra linear_equations_two_var — endpoint from a midpoint
    assert 2 * 8 - 2 == 14 and 2 * 3 - (-1) == 7
    qs.append(spr(
        "SAT-P8-M1-Q21", M, 21, "algebra", "linear_equations_two_var", "hard",
        r"In the $xy$-plane, $M(8, 3)$ is the midpoint of the segment joining"
        r" $P(2, -1)$ and $Q$. What is the $x$-coordinate of $Q$?",
        ["14"],
        r"The midpoint is the average of the endpoints, so the endpoint"
        r" satisfies"
        r" $$\frac{2 + q_x}{2} = 8 \;\Rightarrow\; 2 + q_x = 16"
        r" \;\Rightarrow\; q_x = 14.$$"
        r" A faster way: the midpoint sits the same distance past $P$ as $P$"
        r" is from it. Going from $P$ to $M$ moves $+6$ in $x$, so going from"
        r" $M$ to $Q$ moves another $+6$: $8 + 6 = 14$."
        r" Answering 6 gives only the step, not the coordinate."
        r" The correct answer is **14**.",
        ["Eq(Rational(2 + 14, 2), 8)", "Eq(8 - 2, 6)", "Eq(8 + 6, 14)"]))

    # Q22 H advanced nonlinear_functions — parity reasoning
    qs.append(mcq_listed(
        "SAT-P8-M1-Q22", M, 22, "advanced_math", "equivalent_expressions",
        "hard",
        r"If $n$ is an integer, which of the following expressions must be an"
        r" EVEN integer?",
        {"A": r"$n + 2$", "B": r"$2n + 1$", "C": r"$n^2 + n$",
         "D": r"$n^2 + 1$"}, "C",
        r"Factor the third expression:"
        r" $$n^2 + n = n(n + 1).$$"
        r" That is the product of two CONSECUTIVE integers, so one of them is"
        r" always even — and an even factor makes the product even. This holds"
        r" for every integer $n$, positive, negative, or zero."
        r" The others fail for some $n$: $n + 2$ is odd whenever $n$ is odd;"
        r" $2n + 1$ is always ODD, never even; and $n^2 + 1$ is odd whenever"
        r" $n$ is even. Testing $n = 1$ and $n = 2$ eliminates all three"
        r" quickly."
        r" The correct answer is **C**.",
        ["Eq(1**2 + 1, 2)", "Eq(2**2 + 2, 6)", "Eq(3**2 + 3, 12)",
         "Eq(expand(x*(x + 1)), x**2 + x)"]))

    return qs


# ─── Module 2, easier variant (11E / 9M / 2H) ─────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E algebra one_var
    assert _solve(Eq(x + 14, 9), x) == [-5]
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $x + 14 = 9$, what is the value of $x$?",
        r"Subtract 14 from both sides:"
        r" $$x = 9 - 14 = -5.$$"
        r" Subtracting in the wrong order gives 5, and adding gives 23."
        r" The correct answer is **A**.",
        ["Eq(-5 + 14, 9)"],
        -5, {5: "subtracted 9 from 14 instead", 9: "left the constant alone",
             23: "added 14 instead of subtracting"}, fmt=smart))

    # Q2 E advanced equivalent_expressions — combine like terms
    assert expand(6 * x + 2 - (2 * x - 5)) == 4 * x + 7
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $(6x + 2) - (2x - 5)$?",
        {"A": r"$4x - 3$", "B": r"$4x + 7$", "C": r"$8x - 3$",
         "D": r"$8x + 7$"}, "B",
        r"Subtracting a group changes the sign of EVERY term inside it:"
        r" $$(6x + 2) - (2x - 5) = 6x + 2 - 2x + 5 = 4x + 7.$$"
        r" Leaving the $-5$ negative gives $4x - 3$, and adding the"
        r" $x$-coefficients instead of subtracting gives $8x$."
        r" The correct answer is **B**.",
        ["Eq(expand((6*x + 2) - (2*x - 5)), 4*x + 7)",
         "Eq(expand((6*x + 2) - (2*x - 5)).subs(x, 0), 7)"]))

    # Q3 SPR E algebra linear_functions
    qs.append(spr(
        "SAT-P8-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 7x - 12$. What is the value"
        r" of $f(4)$?",
        ["16"],
        r"Substitute $x = 4$:"
        r" $$f(4) = 7(4) - 12 = 28 - 12 = 16.$$"
        r" The correct answer is **16**.",
        ["Eq(7*4 - 12, 16)"]))

    # Q4 E psda percentages — percent increase
    assert Rational(63 - 45, 45) * 100 == 40
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q04", M, 4, "psda", "percentages", "easy",
        r"The number of members of a club increased from $45$ to $63$. What"
        r" was the percent increase?",
        r"Percent change compares the CHANGE to the ORIGINAL amount:"
        r" $$\frac{63 - 45}{45} = \frac{18}{45} = 0.4 = 40\%.$$"
        r" Dividing the change by the NEW value gives about $28.6\%$, and"
        r" reporting the raw change gives 18."
        r" The correct answer is **C**.",
        ["Eq(63 - 45, 18)", "Eq(Rational(18,45)*100, 40)"],
        40, {18: "reported the raw increase",
             29: "divided the change by the new value",
             63: "reported the new membership"}, fmt=smart))

    # Q5 E geometry lines_angles_triangles — supplementary angles
    assert _solve(Eq(5 * x + 25, 180), x) == [31]
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q05", M, 5, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"Two angles are supplementary. One measures $(5x)^\circ$ and the"
        r" other measures $25^\circ$. What is the value of $x$?",
        r"Supplementary angles sum to $180^\circ$:"
        r" $$5x + 25 = 180 \;\Rightarrow\; 5x = 155 \;\Rightarrow\; x = 31.$$"
        r" Using $90^\circ$ (complementary) instead gives 13, and reporting"
        r" the other angle's measure gives 155."
        r" The correct answer is **C**.",
        ["Eq(5*31 + 25, 180)", "Eq(Rational(180 - 25, 5), 31)"],
        31, {13: "used 90 degrees instead of 180",
             36: "divided 180 by 5", 155: "reported the other angle"},
        fmt=smart))

    # Q6 E advanced nonlinear_functions — evaluate a square root function
    assert sqrt(16) + 3 == 7
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $h$ is defined by $h(x) = \sqrt{x} + 3$. What is the"
        r" value of $h(16)$?",
        r"Take the square root first, then add:"
        r" $$h(16) = \sqrt{16} + 3 = 4 + 3 = 7.$$"
        r" Adding before taking the root gives $\sqrt{19} \approx 4.36$, and"
        r" halving 16 gives 8."
        r" The correct answer is **B**.",
        ["Eq(sqrt(16) + 3, 7)", "Eq(sqrt(16), 4)"],
        7, {4: "stopped at the square root", 8: "halved 16 instead",
            19: "added before taking the root"}, fmt=smart))

    # Q7 SPR E algebra linear_equations_two_var — slope from two points
    assert Rational(1 - 13, 9 - 3) == -2
    qs.append(spr(
        "SAT-P8-M2E-Q07", M, 7, "algebra", "linear_equations_two_var", "easy",
        r"A line in the $xy$-plane passes through $(3, 13)$ and $(9, 1)$. What"
        r" is the slope of the line?",
        ["-2"],
        r"Slope is the change in $y$ over the change in $x$, taken in the same"
        r" order for both:"
        r" $$m = \frac{1 - 13}{9 - 3} = \frac{-12}{6} = -2.$$"
        r" The line falls as $x$ increases, so a negative slope is expected."
        r" The correct answer is **-2**.",
        ["Eq(Rational(1 - 13, 9 - 3), -2)", "Eq(13 + (-2)*(9 - 3), 1)"]))

    # Q8 E advanced equivalent_expressions — power of a power
    assert simplify((x**5) ** 3 - x**15) == 0
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q08", M, 8, "advanced_math", "equivalent_expressions",
        "easy",
        r"For $x > 0$, which of the following is equivalent to"
        r" $\left(x^{5}\right)^{3}$?",
        {"A": r"$3x^{5}$", "B": r"$x^{8}$", "C": r"$x^{15}$",
         "D": r"$x^{125}$"}, "C",
        r"Raising a power to a power MULTIPLIES the exponents:"
        r" $$\left(x^{5}\right)^{3} = x^{5 \cdot 3} = x^{15}.$$"
        r" Adding them instead gives $x^{8}$, and multiplying the exponent by"
        r" the base as if it were a coefficient gives $3x^{5}$."
        r" Check with a small number: $\left(2^{5}\right)^{3} = 32^3 = 32768$"
        r" and $2^{15} = 32768$."
        r" The correct answer is **C**.",
        ["Eq(simplify((x**5)**3 - x**15), 0)", "Eq((2**5)**3, 2**15)",
         "Eq(2**15, 32768)"]))

    # Q9 E algebra linear_inequalities — translate at-least
    assert _solve(Eq(4 * x, 52), x) == [13]
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q09", M, 9, "algebra", "linear_inequalities", "easy",
        r"Which of the following is the smallest integer value of $x$ that"
        r" satisfies $4x \ge 52$?",
        r"Divide both sides by the positive number 4:"
        r" $$x \ge 13.$$"
        r" The smallest integer satisfying this is 13 itself, since the"
        r" inequality is inclusive ($\ge$, not $>$). Reading it as strict"
        r" would give 14."
        r" The correct answer is **B**.",
        ["Eq(4*13, 52)", "4*13 >= 52", "Not(4*12 >= 52)"],
        13, {12: "used the largest integer below the boundary",
             14: "treated the inequality as strict", 48: "multiplied 4 by 12"},
        fmt=smart))

    # Q10 E advanced nonlinear_functions — read the vertex from vertex form
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q10", M, 10, "advanced_math", "nonlinear_functions", "easy",
        r"The graph of $y = (x + 5)^2 - 2$ is a parabola in the $xy$-plane."
        r" What are the coordinates of its vertex?",
        {"A": r"$(-5, -2)$", "B": r"$(-5, 2)$", "C": r"$(5, -2)$",
         "D": r"$(5, 2)$"}, "A",
        r"In vertex form $y = (x - h)^2 + k$ the vertex is $(h, k)$. Matching"
        r" $(x + 5)^2 - 2$ against that pattern:"
        r" $$x + 5 = x - (-5) \;\Rightarrow\; h = -5, \qquad k = -2.$$"
        r" The $x$-coordinate takes the OPPOSITE sign of the number inside the"
        r" parentheses, while the constant outside keeps its own sign."
        r" The correct answer is **A**.",
        ["Eq(expand((x + 5)**2 - 2), x**2 + 10*x + 23)",
         "Eq(((-5) + 5)**2 - 2, -2)"]))

    # Q11 E psda one_var_data — median of an even-sized list
    D11 = [4, 6, 9, 11, 14, 18]
    assert Rational(9 + 11, 2) == 10
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q11", M, 11, "psda", "one_var_data", "easy",
        r"What is the median of the data set $4$, $6$, $9$, $11$, $14$, $18$?",
        r"The list is already in order and has an EVEN number of values, so"
        r" the median is the average of the two middle values, $9$ and $11$:"
        r" $$\frac{9 + 11}{2} = 10.$$"
        r" Picking a single middle value gives 9 or 11; the mean of all six is"
        r" $\frac{62}{6} \approx 10.3$, close but not the median."
        r" The correct answer is **B**.",
        ["Eq(Rational(9 + 11, 2), 10)", "Eq(4 + 6 + 9 + 11 + 14 + 18, 62)"],
        10, {9: "took the lower middle value", 11: "took the upper middle value",
             14: "counted from the wrong end"}, fmt=smart))

    # Q12 SPR M advanced nonlinear_equations_systems — difference of squares
    assert sorted(_solve(Eq(x**2 - 121, 0), x)) == [-11, 11]
    qs.append(spr(
        "SAT-P8-M2E-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What is the positive solution to $x^2 - 121 = 0$?",
        ["11"],
        r"Move the constant across and take both square roots:"
        r" $$x^2 = 121 \;\Rightarrow\; x = \pm 11.$$"
        r" Equivalently, factor the difference of squares:"
        r" $x^2 - 121 = (x - 11)(x + 11)$. The positive solution is 11."
        r" The correct answer is **11**.",
        ["Eq(11**2, 121)", "Eq(expand((x - 11)*(x + 11)), x**2 - 121)"]))

    # Q13 M algebra systems_two_linear — substitution word problem
    _t = _solve([Eq(x + y, 21), Eq(x, 2 * y + 3)], [x, y], dict=True)[0]
    assert _t[x] == 15 and _t[y] == 6
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q13", M, 13, "algebra", "systems_two_linear", "medium",
        r"Two numbers have a sum of $21$. The larger number is $3$ more than"
        r" twice the smaller. What is the larger number?",
        r"Let $L$ and $S$ be the larger and smaller numbers:"
        r" $$L + S = 21, \qquad L = 2S + 3.$$"
        r" Substitute the second into the first:"
        r" $$(2S + 3) + S = 21 \;\Rightarrow\; 3S = 18 \;\Rightarrow\; S = 6,$$"
        r" so $L = 2(6) + 3 = 15$. Check: $15 + 6 = 21$."
        r" Reporting the smaller number gives 6, and halving 21 gives $10.5$."
        r" The correct answer is **C**.",
        ["Eq(15 + 6, 21)", "Eq(15, 2*6 + 3)"],
        15, {6: "reported the smaller number",
             Rational(21, 2): "split the sum evenly",
             18: "stopped at 3S = 18"}, fmt=smart))

    # Q14 M advanced equivalent_expressions — divide out a common factor
    assert simplify((6 * x**2 + 9 * x) / (3 * x) - (2 * x + 3)) == 0
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "medium",
        r"For $x \ne 0$, which of the following is equivalent to"
        r" $\dfrac{6x^2 + 9x}{3x}$?",
        {"A": r"$2x$", "B": r"$2x + 3$", "C": r"$2x + 9$",
         "D": r"$6x^2 + 3$"}, "B",
        r"The denominator divides EVERY term of the numerator, so factor it"
        r" out first:"
        r" $$\frac{6x^2 + 9x}{3x} = \frac{3x(2x + 3)}{3x} = 2x + 3.$$"
        r" Cancelling $3x$ from only the first term leaves the $9x$ untouched"
        r" and produces $2x + 9x$; a quick check at $x = 1$ settles it — the"
        r" original is $\frac{15}{3} = 5$, and $2(1) + 3 = 5$."
        r" The correct answer is **B**.",
        ["Eq(simplify((6*x**2 + 9*x)/(3*x) - (2*x + 3)), 0)",
         "Eq(Rational(6 + 9, 3), 5)", "Eq(2*1 + 3, 5)"]))

    # Q15 SPR M psda ratios_rates_units — two chained rates
    assert Rational(3, 4) * 60 * 8 == 360
    qs.append(spr(
        "SAT-P8-M2E-Q15", M, 15, "psda", "ratios_rates_units", "medium",
        r"A printer prints $3$ pages every $4$ seconds. At this rate, how many"
        r" pages does it print in $8$ minutes?",
        ["360"],
        r"Chain the two rates so the units cancel. Eight minutes is"
        r" $8 \times 60 = 480$ seconds, and the printer does"
        r" $\frac{3}{4}$ of a page per second:"
        r" $$\frac{3 \text{ pages}}{4 \text{ s}} \times 480 \text{ s}"
        r" = 360 \text{ pages}.$$"
        r" Forgetting to convert minutes to seconds gives just 6 pages."
        r" The correct answer is **360**.",
        ["Eq(8*60, 480)", "Eq(Rational(3,4)*480, 360)"]))

    # Q16 M algebra linear_functions — solve for the input
    assert _solve(Eq(Rational(1, 2) * x + 9, 23), x) == [28]
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q16", M, 16, "algebra", "linear_functions", "medium",
        r"The function $f$ is defined by $f(x) = \dfrac{1}{2}x + 9$. For what"
        r" value of $x$ does $f(x) = 23$?",
        r"Set the rule equal to 23 and solve:"
        r" $$\frac{1}{2}x + 9 = 23 \;\Rightarrow\; \frac{1}{2}x = 14"
        r" \;\Rightarrow\; x = 28.$$"
        r" Multiplying by $\frac{1}{2}$ rather than by 2 gives 7, and"
        r" evaluating $f(23)$ instead of solving gives $20.5$."
        r" The correct answer is **D**.",
        ["Eq(Rational(1,2)*28 + 9, 23)", "Eq((23 - 9)*2, 28)"],
        28, {7: "multiplied by 1/2 instead of 2", 14: "stopped at x/2 = 14",
             Rational(41, 2): "evaluated f(23) instead of solving"},
        fmt=smart))

    # Q17 M advanced nonlinear_functions — factor to find zeros
    assert sorted(_solve(Eq(x**2 + 2 * x - 15, 0), x)) == [-5, 3]
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q17", M, 17, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What are all solutions to $x^2 + 2x - 15 = 0$?",
        {"A": r"$-5$ and $3$", "B": r"$-3$ and $5$", "C": r"$3$ and $5$",
         "D": r"$-15$ and $1$"}, "A",
        r"Find two numbers whose product is $-15$ and whose sum is $+2$:"
        r" those are $+5$ and $-3$, so"
        r" $$x^2 + 2x - 15 = (x + 5)(x - 3) = 0.$$"
        r" Setting each factor to zero gives $x = -5$ and $x = 3$ — each"
        r" solution has the OPPOSITE sign of the number in its factor, which"
        r" is exactly where choice B goes wrong."
        r" The correct answer is **A**.",
        ["Eq(expand((x + 5)*(x - 3)), x**2 + 2*x - 15)",
         "Eq((-5)**2 + 2*(-5) - 15, 0)", "Eq(3**2 + 2*3 - 15, 0)"]))

    # Q18 M geometry right_triangles_trig — sine ratio
    assert 8**2 + 15**2 == 17**2
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q18", M, 18, "geometry_trig", "right_triangles_trig",
        "medium",
        r"In a right triangle, the leg opposite angle $\theta$ has length $8$"
        r" and the hypotenuse has length $17$. What is the value of"
        r" $\sin\theta$?",
        {"A": r"$\dfrac{8}{17}$", "B": r"$\dfrac{8}{15}$",
         "C": r"$\dfrac{15}{17}$", "D": r"$\dfrac{17}{8}$"}, "A",
        r"Sine is the ratio of the opposite leg to the hypotenuse:"
        r" $$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}"
        r" = \frac{8}{17}.$$"
        r" No further work is needed. The other leg is"
        r" $\sqrt{17^2 - 8^2} = 15$, so $\frac{15}{17}$ is $\cos\theta$ and"
        r" $\frac{8}{15}$ is $\tan\theta$."
        r" The correct answer is **A**.",
        ["Eq(8**2 + 15**2, 17**2)",
         "Eq(Rational(8,17)**2 + Rational(15,17)**2, 1)"]))

    # Q19 SPR M algebra linear_equations_one_var — clear a decimal
    assert _solve(Eq(Rational(3, 10) * x + Rational(12, 10), 3), x) == [6]
    qs.append(spr(
        "SAT-P8-M2E-Q19", M, 19, "algebra", "linear_equations_one_var",
        "medium",
        r"$$0.3x + 1.2 = 3$$"
        r" What is the solution to the equation above?",
        ["6"],
        r"Multiply through by 10 to clear the decimals:"
        r" $$3x + 12 = 30 \;\Rightarrow\; 3x = 18 \;\Rightarrow\; x = 6.$$"
        r" Check: $0.3(6) + 1.2 = 1.8 + 1.2 = 3$."
        r" The correct answer is **6**.",
        ["Eq(Rational(3,10)*6 + Rational(12,10), 3)", "Eq(3*6 + 12, 30)"]))

    # Q20 M advanced nonlinear_functions — exponential from a table
    T20 = [(0, 7), (1, 21), (2, 63), (3, 189)]
    assert all(y2 == 3 * y1 for (_, y1), (_, y2) in zip(T20, T20[1:]))
    qs.append(mcq_numeric(
        "SAT-P8-M2E-Q20", M, 20, "advanced_math", "nonlinear_functions",
        "medium",
        r"The table shows four values of an exponential function $h$. By what"
        r" factor does $h(x)$ change each time $x$ increases by $1$?",
        r"For an exponential function successive outputs are multiplied by a"
        r" constant. Divide consecutive values:"
        r" $$\frac{21}{7} = 3, \qquad \frac{63}{21} = 3, \qquad"
        r" \frac{189}{63} = 3.$$"
        r" The factor is 3."
        r" Subtracting consecutive values instead gives $14$, $42$, $126$ —"
        r" not constant, which is exactly how an exponential differs from a"
        r" linear function."
        r" The correct answer is **A**.",
        ["Eq(Rational(21,7), 3)", "Eq(Rational(63,21), 3)",
         "Eq(Rational(189,63), 3)", "Eq(7*3**3, 189)"],
        3, {7: "reported the initial value", 14: "subtracted instead of dividing",
            21: "reported the second value"}, fmt=smart,
        fig=figure("sat-p8-m2e-q20",
                   "Two-row table of x values 0, 1, 2, 3 against h(x) values "
                   "7, 21, 63, 189")))

    # Q21 H geometry circles — circle from the endpoints of a diameter
    assert Rational(2 + 10, 2) == 6 and Rational(3 + 11, 2) == 7
    assert (10 - 2) ** 2 + (11 - 3) ** 2 == 128
    qs.append(mcq_listed(
        "SAT-P8-M2E-Q21", M, 21, "geometry_trig", "circles", "hard",
        r"In the $xy$-plane, a circle has a diameter whose endpoints are"
        r" $(2, 3)$ and $(10, 11)$. What are the coordinates of the center of"
        r" the circle?",
        {"A": r"$(4, 4)$", "B": r"$(6, 7)$", "C": r"$(8, 8)$",
         "D": r"$(12, 14)$"}, "B",
        r"The center of a circle is the MIDPOINT of any diameter, so average"
        r" the endpoints coordinate by coordinate:"
        r" $$\left(\frac{2 + 10}{2},\; \frac{3 + 11}{2}\right) = (6, 7).$$"
        r" Adding the coordinates without halving gives $(12, 14)$, and taking"
        r" their differences gives $(8, 8)$."
        r" The correct answer is **B**.",
        ["Eq(Rational(2 + 10, 2), 6)", "Eq(Rational(3 + 11, 2), 7)",
         "Eq((10 - 2)**2 + (11 - 3)**2, 128)"]))

    # Q22 SPR H algebra linear_equations_one_var — variable on both sides with
    # distribution
    assert _solve(Eq(5 * (x - 2), 2 * (x + 7)), x) == [8]
    qs.append(spr(
        "SAT-P8-M2E-Q22", M, 22, "algebra", "linear_equations_one_var", "hard",
        r"$$5(x - 2) = 2(x + 7)$$"
        r" What is the solution to the equation above?",
        ["8"],
        r"Distribute on both sides first:"
        r" $$5x - 10 = 2x + 14.$$"
        r" Then gather like terms:"
        r" $$3x = 24 \;\Rightarrow\; x = 8.$$"
        r" Check: $5(8 - 2) = 30$ and $2(8 + 7) = 30$."
        r" The correct answer is **8**.",
        ["Eq(5*(8 - 2), 2*(8 + 7))", "Eq(5*(8 - 2), 30)"]))

    return qs


# ─── Module 2, harder variant (2E / 7M / 13H) ─────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E algebra one_var
    assert _solve(Eq(6 * x - 11, 2 * x + 13), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $6x - 11 = 2x + 13$, what is the value of $x$?",
        r"Collect like terms on opposite sides:"
        r" $$4x = 24 \;\Rightarrow\; x = 6.$$"
        r" Subtracting the constants instead of adding gives $4x = 2$, and"
        r" stopping at $4x = 24$ gives 24."
        r" The correct answer is **C**.",
        ["Eq(6*6 - 11, 2*6 + 13)", "Eq((13 + 11)/(6 - 2), 6)"],
        6, {Rational(1, 2): "subtracted 11 from 13 instead of adding",
            3: "divided 24 by 8", 24: "stopped at 4x = 24"}, fmt=smart))

    # Q2 E advanced equivalent_expressions
    assert expand((x - 6) * (x + 6)) == x**2 - 36
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $(x - 6)(x + 6)$?",
        {"A": r"$x^2 - 36$", "B": r"$x^2 - 12x - 36$", "C": r"$x^2 + 36$",
         "D": r"$x^2 + 12x - 36$"}, "A",
        r"The middle terms cancel because the two constants are opposites:"
        r" $$(x - 6)(x + 6) = x^2 + 6x - 6x - 36 = x^2 - 36.$$"
        r" This is the difference-of-squares pattern"
        r" $(a - b)(a + b) = a^2 - b^2$, so no $x$-term survives."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 6)*(x + 6)), x**2 - 36)", "Eq(6 - 6, 0)"]))

    # Q3 SPR M algebra systems_two_linear — elimination
    _s = _solve([Eq(4 * x + 3 * y, 27), Eq(4 * x - y, 7)], [x, y], dict=True)[0]
    assert _s[x] == 3 and _s[y] == 5
    qs.append(spr(
        "SAT-P8-M2H-Q03", M, 3, "algebra", "systems_two_linear", "medium",
        r"$$4x + 3y = 27$$ $$4x - y = 7$$"
        r" If $(x, y)$ is the solution to the system above, what is the value"
        r" of $y$?",
        ["5"],
        r"The $x$-terms already match, so SUBTRACT the second equation from"
        r" the first — the $4x$ cancels without any scaling:"
        r" $$(4x + 3y) - (4x - y) = 27 - 7 \;\Rightarrow\; 4y = 20"
        r" \;\Rightarrow\; y = 5.$$"
        r" Substituting back gives $4x = 7 + 5 = 12$, so $x = 3$, and both"
        r" originals check: $4(3) + 3(5) = 27$ and $4(3) - 5 = 7$."
        r" The correct answer is **5**.",
        ["Eq(4*3 + 3*5, 27)", "Eq(4*3 - 5, 7)", "Eq(27 - 7, 20)",
         "Eq(Rational(20,4), 5)"]))

    # Q4 M geometry area_volume — surface areas of similar solids
    assert Rational(6, 2) == 3 and 3**2 == 9
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q04", M, 4, "geometry_trig", "area_volume", "medium",
        r"Two cubes have edge lengths of $2$ and $6$. The surface area of the"
        r" larger cube is how many times the surface area of the smaller cube?",
        r"Surface area is two-dimensional, so it scales by the SQUARE of the"
        r" linear ratio. The edges are in the ratio"
        r" $$k = \frac{6}{2} = 3,$$"
        r" so the surface areas are in the ratio $k^2 = 9$."
        r" Checking directly: $6(2)^2 = 24$ and $6(6)^2 = 216$, and"
        r" $\frac{216}{24} = 9$."
        r" Answering 3 uses the linear ratio, and 27 uses the cube — that is"
        r" the VOLUME ratio."
        r" The correct answer is **C**.",
        ["Eq(6*2**2, 24)", "Eq(6*6**2, 216)", "Eq(Rational(216,24), 9)",
         "Eq(3**3, 27)"],
        9, {3: "used the linear ratio", 6: "doubled the linear ratio",
            27: "used the cube, which is the volume ratio"}, fmt=smart))

    # Q5 M psda probability_conditional — "at least one" via the complement
    assert Rational(3, 5) * Rational(3, 5) == Rational(9, 25)
    assert 1 - Rational(9, 25) == Rational(16, 25)
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q05", M, 5, "psda", "probability_conditional", "medium",
        r"A spinner lands on a winning section with probability"
        r" $\dfrac{2}{5}$ on each spin, independently. If the spinner is spun"
        r" twice, what is the probability of winning AT LEAST once?",
        {"A": r"$\dfrac{4}{25}$", "B": r"$\dfrac{2}{5}$",
         "C": r"$\dfrac{16}{25}$", "D": r"$\dfrac{4}{5}$"}, "C",
        r"''At least once'' is easier to count through its complement —"
        r" losing BOTH spins. Each loss has probability"
        r" $1 - \frac{2}{5} = \frac{3}{5}$, and the spins are independent:"
        r" $$P(\text{both losses}) = \frac{3}{5} \cdot \frac{3}{5}"
        r" = \frac{9}{25}.$$"
        r" Therefore"
        r" $$P(\text{at least one win}) = 1 - \frac{9}{25} = \frac{16}{25}.$$"
        r" Simply adding the two win probabilities gives $\frac{4}{5}$, which"
        r" double-counts the outcome where BOTH spins win; and"
        r" $\frac{4}{25}$ is the probability that both win."
        r" The correct answer is **C**.",
        ["Eq(1 - Rational(2,5), Rational(3,5))",
         "Eq(Rational(3,5)*Rational(3,5), Rational(9,25))",
         "Eq(1 - Rational(9,25), Rational(16,25))",
         "Eq(Rational(2,5)*Rational(2,5), Rational(4,25))"]))

    # Q6 M advanced nonlinear_functions — average rate of change of a quadratic
    assert Rational((5**2 + 1) - (1**2 + 1), 5 - 1) == 6
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q06", M, 6, "advanced_math", "nonlinear_functions", "medium",
        r"The function $f$ is defined by $f(x) = x^2 + 1$. What is the average"
        r" rate of change of $f$ from $x = 1$ to $x = 5$?",
        r"Average rate of change is the slope of the line joining the two"
        r" points on the curve:"
        r" $$\frac{f(5) - f(1)}{5 - 1} = \frac{26 - 2}{4} = \frac{24}{4} = 6.$$"
        r" Note this is NOT the same as the function's value anywhere;"
        r" reporting $f(5) - f(1) = 24$ skips the division, and $f(3) = 10$ is"
        r" the value at the midpoint, not the rate."
        r" The correct answer is **B**.",
        ["Eq(5**2 + 1, 26)", "Eq(1**2 + 1, 2)", "Eq(Rational(26 - 2, 5 - 1), 6)"],
        6, {4: "divided by the wrong interval width",
            10: "reported f(3), the value at the midpoint",
            24: "did not divide by the change in x"}, fmt=smart))

    # Q7 SPR M advanced nonlinear_equations_systems — factor a cubic partially
    assert sorted(_solve(Eq(x**3 - 9 * x, 0), x)) == [-3, 0, 3]
    qs.append(spr(
        "SAT-P8-M2H-Q07", M, 7, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"How many distinct real solutions does $x^3 - 9x = 0$ have?",
        ["3"],
        r"Factor completely rather than dividing by $x$, which would lose a"
        r" solution:"
        r" $$x^3 - 9x = x(x^2 - 9) = x(x - 3)(x + 3) = 0.$$"
        r" Setting each factor to zero gives $x = 0$, $x = 3$, and $x = -3$ —"
        r" three distinct real solutions."
        r" The correct answer is **3**.",
        ["Eq(expand(x*(x - 3)*(x + 3)), x**3 - 9*x)",
         "Eq(0**3 - 9*0, 0)", "Eq(3**3 - 9*3, 0)", "Eq((-3)**3 - 9*(-3), 0)"]))

    # Q8 M algebra linear_functions — interpret a negative slope in context
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q08", M, 8, "algebra", "linear_functions", "medium",
        r"The number of liters of fuel in a generator is modeled by"
        r" $F(t) = 90 - 7.5t$, where $t$ is the number of hours the generator"
        r" has run. Which of the following is the best interpretation of"
        r" $7.5$ in this context?",
        {"A": r"The generator holds $7.5$ liters of fuel when full.",
         "B": r"The generator consumes $7.5$ liters of fuel each hour.",
         "C": r"The generator runs for $7.5$ hours before running out.",
         "D": r"The generator gains $7.5$ liters of fuel each hour."}, "B",
        r"The coefficient of $t$ is the rate of change per hour, and the minus"
        r" sign in $90 - 7.5t$ makes that change a DECREASE:"
        r" $$F(t + 1) - F(t) = -7.5.$$"
        r" So the generator loses — consumes — $7.5$ liters each hour."
        r" The constant $90$ is the full tank, and the generator actually runs"
        r" for $\frac{90}{7.5} = 12$ hours before emptying, not $7.5$."
        r" The correct answer is **B**.",
        ["Eq((90 - Rational(75,10)*(1 + 1)) - (90 - Rational(75,10)*1), -Rational(75,10))",
         "Eq(Rational(90*10, 75), 12)"]))

    # Q9 M geometry lines_angles_triangles — angle bisector in a triangle
    assert 180 - 2 * 35 == 110
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q09", M, 9, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In triangle $ABC$, $AB = AC$ and the angle at vertex $B$ measures"
        r" $35^\circ$. What is the measure, in degrees, of the angle at vertex"
        r" $A$?",
        r"Since $AB = AC$, the angles OPPOSITE those equal sides are equal —"
        r" and those are the angles at $C$ and $B$. So the angle at $C$ also"
        r" measures $35^\circ$, and"
        r" $$m\angle A = 180 - 35 - 35 = 110.$$"
        r" Assuming instead that $A$ equals $B$ gives 35, and halving the"
        r" remaining $110$ gives 55 — that would be right only if $A$ were one"
        r" of the two EQUAL angles."
        r" The correct answer is **D**.",
        ["Eq(180 - 35 - 35, 110)", "Eq(Rational(180 - 35, 2), Rational(145,2))"],
        110, {35: "assumed angle A equals angle B",
              55: "halved the remaining measure",
              145: "subtracted only one 35 degree angle"}, fmt=smart))

    # Q10 H algebra linear_inequalities — compound constraint on a budget
    assert 3 * 14 + 8 * 5 == 82
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q10", M, 10, "algebra", "linear_inequalities", "hard",
        r"A florist buys roses at $\$8$ each and lilies at $\$3$ each,"
        r" spending at most $\$82$ in total. If the florist buys exactly $5$"
        r" roses, what is the greatest number of lilies that can also be"
        r" bought?",
        r"The roses cost $5(8) = 40$ dollars, leaving the lilies to satisfy"
        r" $$40 + 3L \le 82 \;\Rightarrow\; 3L \le 42 \;\Rightarrow\; L \le 14.$$"
        r" Since 14 is a whole number and the constraint is inclusive, the"
        r" greatest count is 14, spending exactly $40 + 42 = 82$ dollars."
        r" Ignoring the roses gives $\frac{82}{3} \approx 27$, and swapping"
        r" the two prices gives a different budget entirely."
        r" The correct answer is **C**.",
        ["Eq(5*8, 40)", "Eq(40 + 3*14, 82)", "40 + 3*14 <= 82",
         "Not(40 + 3*15 <= 82)"],
        14, {5: "reported the number of roses",
             10: "used the rose price for the lilies",
             27: "ignored the cost of the roses"}, fmt=smart))

    # Q11 H advanced nonlinear_functions — inverse-style solve
    assert _solve(Eq((2 * x - 1) / 3, 5), x) == [8]
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q11", M, 11, "advanced_math", "nonlinear_functions", "hard",
        r"The function $f$ is defined by $f(x) = \dfrac{2x - 1}{3}$. If"
        r" $f(a) = 5$, what is the value of $f(a + 3)$?",
        r"First recover $a$:"
        r" $$\frac{2a - 1}{3} = 5 \;\Rightarrow\; 2a - 1 = 15"
        r" \;\Rightarrow\; a = 8.$$"
        r" Then evaluate at $a + 3 = 11$:"
        r" $$f(11) = \frac{2(11) - 1}{3} = \frac{21}{3} = 7.$$"
        r" A shortcut: $f$ is linear with slope $\frac{2}{3}$, so increasing"
        r" the input by 3 raises the output by $\frac{2}{3}(3) = 2$, giving"
        r" $5 + 2 = 7$ directly."
        r" Reporting $a$ itself gives 8, and adding 3 to the output gives 8"
        r" as well by a different error."
        r" The correct answer is **A**.",
        ["Eq(Rational(2*8 - 1, 3), 5)", "Eq(Rational(2*11 - 1, 3), 7)",
         "Eq(5 + Rational(2,3)*3, 7)"],
        7, {8: "reported a, or added 3 to the output",
            11: "reported the new input a + 3",
            15: "stopped at 2a - 1 = 15"}, fmt=smart))

    # Q12 SPR H advanced nonlinear_equations_systems — product of roots
    assert sorted(_solve(Eq(3 * x**2 - 5 * x - 12, 0), x)) == \
        [Rational(-4, 3), 3]
    qs.append(spr(
        "SAT-P8-M2H-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"The solutions to $3x^2 - 5x - 12 = 0$ are $p$ and $q$. What is the"
        r" value of $pq$?",
        ["-4"],
        r"For $ax^2 + bx + c = 0$ the product of the solutions is"
        r" $\frac{c}{a}$:"
        r" $$pq = \frac{-12}{3} = -4.$$"
        r" No factoring is required, though it confirms the result: the"
        r" equation factors as $(3x + 4)(x - 3) = 0$, giving"
        r" $p = -\frac{4}{3}$ and $q = 3$, whose product is"
        r" $-\frac{4}{3} \cdot 3 = -4$."
        r" Using $c$ alone, without dividing by $a$, would give $-12$."
        r" The correct answer is **-4**.",
        ["Eq(expand((3*x + 4)*(x - 3)), 3*x**2 - 5*x - 12)",
         "Eq(Rational(-4,3)*3, -4)", "Eq(Rational(-12,3), -4)"]))

    # Q13 H algebra linear_equations_two_var — parallel line through a point
    assert _solve(Eq(2 * 6 + 3 * (-1), x), x) == [9]
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q13", M, 13, "algebra", "linear_equations_two_var", "hard",
        r"In the $xy$-plane, line $m$ is parallel to the graph of"
        r" $2x + 3y = 18$ and passes through the point $(6, -1)$. Which"
        r" equation defines line $m$?",
        {"A": r"$2x + 3y = 9$", "B": r"$2x + 3y = 15$",
         "C": r"$3x - 2y = 20$", "D": r"$3x + 2y = 16$"}, "A",
        r"Parallel lines have the same slope, and two equations in standard"
        r" form are parallel exactly when their $x$- and $y$-coefficients"
        r" match. So line $m$ has the form"
        r" $$2x + 3y = c$$"
        r" for some constant $c$. Substitute the given point to find it:"
        r" $$2(6) + 3(-1) = 12 - 3 = 9.$$"
        r" So line $m$ is $2x + 3y = 9$. Choice C has the PERPENDICULAR"
        r" coefficient pattern, and choice B has the right slope but does not"
        r" pass through $(6, -1)$: $2(6) + 3(-1) = 9 \ne 15$."
        r" The correct answer is **A**.",
        ["Eq(2*6 + 3*(-1), 9)", "Ne(2*6 + 3*(-1), 15)",
         "Eq(Rational(-2,3)*Rational(3,2), -1)"]))

    # Q14 H advanced equivalent_expressions — expand a squared trinomial-ish
    assert expand((2 * x + 3) * (x - 1) * 2) == 4 * x**2 + 2 * x - 6
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "hard",
        r"Which of the following is equivalent to $2(2x + 3)(x - 1)$?",
        {"A": r"$4x^2 - 6$", "B": r"$4x^2 + 2x - 6$",
         "C": r"$4x^2 + 4x - 6$", "D": r"$4x^2 + 10x - 6$"}, "B",
        r"Multiply the two binomials first, then apply the factor of 2:"
        r" $$(2x + 3)(x - 1) = 2x^2 - 2x + 3x - 3 = 2x^2 + x - 3,$$"
        r" $$2(2x^2 + x - 3) = 4x^2 + 2x - 6.$$"
        r" Distributing the 2 into BOTH binomials first would double the"
        r" product twice over; and dropping the middle term entirely gives"
        r" $4x^2 - 6$. Checking at $x = 1$ settles it: the original is"
        r" $2(5)(0) = 0$, and $4 + 2 - 6 = 0$."
        r" The correct answer is **B**.",
        ["Eq(expand(2*(2*x + 3)*(x - 1)), 4*x**2 + 2*x - 6)",
         "Eq(2*(2*1 + 3)*(1 - 1), 0)", "Eq(4*1**2 + 2*1 - 6, 0)"]))

    # Q15 SPR H psda percentages — reverse a percent decrease
    assert Rational(85, 100) * 240 == 204
    qs.append(spr(
        "SAT-P8-M2H-Q15", M, 15, "psda", "percentages", "hard",
        r"After a $15\%$ decrease, the number of daily riders on a bus route"
        r" is $204$. How many daily riders were there before the decrease?",
        ["240"],
        r"A $15\%$ decrease leaves $85\%$ of the original, so if $r$ is the"
        r" original count,"
        r" $$0.85r = 204 \;\Rightarrow\; r = \frac{204}{0.85} = 240.$$"
        r" Check: $15\%$ of $240$ is $36$, and $240 - 36 = 204$."
        r" Adding $15\%$ to $204$ gives $234.6$, not $240$ — percent changes"
        r" are taken of DIFFERENT bases going forward and backward, so undoing"
        r" a decrease is division, not a matching increase."
        r" The correct answer is **240**.",
        ["Eq(Rational(85,100)*240, 204)", "Eq(240 - Rational(15,100)*240, 204)",
         "Ne(Rational(115,100)*204, 240)"]))

    # Q16 H algebra — inverse variation with a SQUARED variable
    assert 9 * 2**2 == 36 and Rational(36, 3**2) == 4
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q16", M, 16, "algebra", "linear_functions", "hard",
        r"The quantity $y$ varies inversely with the square of $x$. When"
        r" $x = 2$, $y = 9$. What is the value of $y$ when $x = 3$?",
        r"Inverse variation with the SQUARE means the product $y x^2$ is"
        r" constant. Find that constant from the given pair:"
        r" $$y x^2 = 9(2)^2 = 36.$$"
        r" Now solve at $x = 3$:"
        r" $$y(3)^2 = 36 \;\Rightarrow\; 9y = 36 \;\Rightarrow\; y = 4.$$"
        r" Tripling $x$ from 2 to 3 multiplies $x^2$ by $\frac{9}{4}$, so $y$"
        r" is divided by $\frac{9}{4}$ — it must DECREASE, which rules out"
        r" $13.5$ (that comes from treating the relationship as direct)."
        r" Using inverse variation in $x$ rather than $x^2$ gives"
        r" $9 \cdot \frac{2}{3} = 6$."
        r" The correct answer is **B**.",
        ["Eq(9*2**2, 36)", "Eq(Rational(36, 3**2), 4)",
         "Eq(9*Rational(2,3), 6)"],
        4, {3: "divided y by the new value of x",
            6: "used inverse variation in x rather than x squared",
            Rational(27, 2): "used direct variation"}, fmt=smart))

    # Q17 H advanced nonlinear_equations_systems — no-real-solution condition
    assert _solve(Eq(6**2 - 4 * 1 * x, 0), x) == [9]
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q17", M, 17, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"$$x^2 + 6x + c = 0$$"
        r" In the equation above, $c$ is a constant. For which of the"
        r" following values of $c$ does the equation have NO real solutions?",
        {"A": r"$5$", "B": r"$8$", "C": r"$9$", "D": r"$10$"}, "D",
        r"A quadratic has no real solutions exactly when its discriminant is"
        r" NEGATIVE:"
        r" $$b^2 - 4ac = 36 - 4c < 0 \;\Rightarrow\; c > 9.$$"
        r" Of the choices only $10$ exceeds 9. At $c = 9$ the discriminant is"
        r" exactly zero, which gives ONE real solution — a repeated root, not"
        r" zero solutions — so $9$ is the boundary case and does not qualify."
        r" Values below 9 give two real solutions."
        r" The correct answer is **D**.",
        ["Eq(6**2 - 4*9, 0)", "36 - 4*10 < 0", "36 - 4*9 >= 0",
         "36 - 4*8 > 0"]))

    # Q18 H psda two_var_data_models — extrapolate from a model, then compare
    assert 45 * 12 + 130 == 670
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q18", M, 18, "algebra", "linear_functions", "hard",
        r"A model predicts that a shop's monthly revenue, in dollars, is"
        r" $R(m) = 45m + 130$, where $m$ is the number of items sold. The shop"
        r" sold $12$ items in a month in which its ACTUAL revenue was $\$710$."
        r" By how many dollars did the actual revenue exceed the predicted"
        r" revenue?",
        r"Predict first:"
        r" $$R(12) = 45(12) + 130 = 540 + 130 = 670.$$"
        r" Then compare with the actual figure:"
        r" $$710 - 670 = 40.$$"
        r" Reporting the prediction gives 670, subtracting the fixed term from"
        r" the actual revenue gives $710 - 130 = 580$, and ignoring the fixed"
        r" term entirely gives $710 - 540 = 170$."
        r" The correct answer is **A**.",
        ["Eq(45*12 + 130, 670)", "Eq(710 - 670, 40)"],
        40, {170: "ignored the fixed term of the model",
             580: "subtracted only the fixed term",
             670: "reported the predicted revenue"}, fmt=smart))

    # Q19 SPR H algebra systems_two_linear — three-quantity setup
    _c = _solve([Eq(x + y, 18), Eq(25 * x + 10 * y, 315)], [x, y], dict=True)[0]
    assert _c[x] == 9 and _c[y] == 9
    qs.append(spr(
        "SAT-P8-M2H-Q19", M, 19, "algebra", "systems_two_linear", "hard",
        r"A coin jar holds only $25$-tögrög and $10$-tögrög coins. There are"
        r" $18$ coins worth $315$ tögrög in total. How many of the coins are"
        r" $25$-tögrög coins?",
        ["9"],
        r"Let $a$ be the number of $25$-tögrög coins and $b$ the number of"
        r" $10$-tögrög coins. Count and value give one equation each:"
        r" $$a + b = 18, \qquad 25a + 10b = 315.$$"
        r" Substitute $b = 18 - a$ into the value equation:"
        r" $$25a + 10(18 - a) = 315 \;\Rightarrow\; 15a + 180 = 315"
        r" \;\Rightarrow\; a = 9.$$"
        r" Check: 9 coins of each kind give $225 + 90 = 315$ tögrög."
        r" The correct answer is **9**.",
        ["Eq(9 + 9, 18)", "Eq(25*9 + 10*9, 315)"]))

    # Q20 H geometry circles — equation of a circle from center and a point
    assert (7 - 3) ** 2 + (1 - (-2)) ** 2 == 25
    qs.append(mcq_listed(
        "SAT-P8-M2H-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"In the $xy$-plane, a circle has its center at $(3, -2)$ and passes"
        r" through the point $(7, 1)$. Which of the following is an equation"
        r" of the circle?",
        {"A": r"$(x - 3)^2 + (y + 2)^2 = 5$",
         "B": r"$(x - 3)^2 + (y + 2)^2 = 25$",
         "C": r"$(x + 3)^2 + (y - 2)^2 = 5$",
         "D": r"$(x + 3)^2 + (y - 2)^2 = 25$"}, "B",
        r"The standard form is $(x - h)^2 + (y - k)^2 = r^2$ with center"
        r" $(h, k)$. With $h = 3$ and $k = -2$ the left side is"
        r" $$(x - 3)^2 + (y + 2)^2,$$"
        r" since subtracting $-2$ becomes adding 2. The radius is the distance"
        r" from the center to the given point:"
        r" $$r^2 = (7 - 3)^2 + (1 - (-2))^2 = 16 + 9 = 25.$$"
        r" The right side is $r^2$, not $r$, so it is $25$ — writing $5$ there"
        r" is the standard trap."
        r" The correct answer is **B**.",
        ["Eq((7 - 3)**2 + (1 + 2)**2, 25)", "Eq(sqrt(25), 5)",
         "Eq((7 - 3)**2 + (1 + 2)**2, 5**2)"]))

    # Q21 H advanced nonlinear_functions — compare two exponential expressions
    assert 2 ** 30 == 8 ** 10 and 4 ** 15 == 2 ** 30
    qs.append(mcq_numeric(
        "SAT-P8-M2H-Q21", M, 21, "advanced_math", "nonlinear_functions", "hard",
        r"If $8^{10} = 2^{\,n}$, what is the value of $n$?",
        r"Rewrite the base 8 as a power of 2 and multiply the exponents:"
        r" $$8^{10} = \left(2^3\right)^{10} = 2^{30}.$$"
        r" Matching exponents gives $n = 30$."
        r" Adding the exponents instead of multiplying gives 13, and using"
        r" $8 \times 10$ gives 80."
        r" The correct answer is **C**.",
        ["Eq(8**10, 2**30)", "Eq(3*10, 30)"],
        30, {13: "added the exponents instead of multiplying",
             24: "used a base of 4", 80: "multiplied the base by the exponent"},
        fmt=smart))

    # Q22 SPR H psda one_var_data — removing a value to move the mean
    assert 8 * 30 == 240 and 7 * 32 == 224 and 240 - 224 == 16
    qs.append(spr(
        "SAT-P8-M2H-Q22", M, 22, "psda", "one_var_data", "hard",
        r"The mean of a list of $8$ numbers is $30$. When one number is"
        r" removed, the mean of the remaining $7$ numbers is $32$. What number"
        r" was removed?",
        ["16"],
        r"Work with totals. The original list sums to"
        r" $$8 \times 30 = 240,$$"
        r" and the remaining seven sum to"
        r" $$7 \times 32 = 224.$$"
        r" The removed number is the difference:"
        r" $$240 - 224 = 16.$$"
        r" A sanity check: removing a number BELOW the old mean must pull the"
        r" mean up, and $16 < 30$, which matches the mean rising to 32."
        r" Subtracting the means, $32 - 30 = 2$, ignores that the total is"
        r" spread over a different count."
        r" The correct answer is **16**.",
        ["Eq(8*30, 240)", "Eq(7*32, 224)", "Eq(240 - 224, 16)", "16 < 30"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-8.json",
               {"testId": "sat-practice-8",
                "label": "SAT Math Practice Test 8",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
