#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 11 (data/sat/sat-practice-11.json).

Built on scripts/test-builders/satbuild.py. Archetypes audited against
tests 1-10; new to the bank here:
  * interquartile range read off a BOX PLOT
  * a count read off a HISTOGRAM across several bins
  * a residual read off a scatterplot with its line of best fit
  * the slope of a line PERPENDICULAR to a given standard-form line
  * a negative rational exponent evaluated exactly
  * the 30-60-90 and 45-45-90 side ratios
  * successive percent change (a discount followed by a markup)
  * inverse variation, and direct variation from a single data point
  * an absolute-value INEQUALITY and its greatest integer solution
  * the sphere whose volume determines its surface area
  * the geometric sequence's common ratio from two terms
  * a two-solution acid mixture and a mi/h to ft/s unit conversion
  * a line tangent to a parabola (the double root of a system)

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
    assert _solve(Eq(3 * x - 8, 19), x) == [9]
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $3x - 8 = 19$, what is the value of $x$?",
        r"Add 8 to both sides, then divide by 3:"
        r" $$3x = 27 \;\Rightarrow\; x = 9.$$"
        r" Dropping the coefficient and solving $x - 8 = 19$ gives 27, and"
        r" stopping at $3x = 27$ gives 27 as well — the last step matters."
        r" The correct answer is **A**.",
        ["Eq(3*9 - 8, 19)", "Eq((19 + 8)/3, 9)"],
        9, {11: "solved $x - 8 = 19$ then subtracted",
            27: "stopped at $3x = 27$",
            81: "multiplied 27 by 3 instead of dividing"}))

    # Q2 E adv
    assert 2**2 * 2**5 == 2**7
    qs.append(mcq_listed(
        "SAT-P11-M1-Q02", M, 2, "advanced_math", "exponent_rules", "easy",
        r"Which of the following is equivalent to $x^2 \cdot x^5$?",
        {"A": r"$x^3$", "B": r"$x^7$", "C": r"$x^{10}$", "D": r"$2x^7$"},
        "B",
        r"Multiplying powers of the same base ADDS the exponents:"
        r" $$x^2 \cdot x^5 = x^{2 + 5} = x^7.$$"
        r" Testing at $x = 2$: $4 \times 32 = 128 = 2^7$. Multiplying the"
        r" exponents would give $x^{10}$ — that is the rule for a power of"
        r" a power, not for a product — and the base itself is never"
        r" doubled."
        r" The correct answer is **B**.",
        ["Eq(2**2 * 2**5, 128)", "Eq(2**7, 128)", "Eq(2 + 5, 7)"]))

    # Q3 E psda
    assert Rational(24, 3) * 10 == 80
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q03", M, 3, "psda", "ratios_rates_proportions", "easy",
        r"A printer prints 24 pages in 3 minutes. At this rate, how many"
        r" pages will it print in 10 minutes?",
        r"Find the rate first:"
        r" $$\frac{24 \text{ pages}}{3 \text{ minutes}}"
        r" = 8 \text{ pages per minute}.$$"
        r" Then multiply by the new time:"
        r" $$8 \times 10 = 80 \text{ pages}.$$"
        r" Scaling 24 by 10 without dividing by the 3 minutes first gives"
        r" 240 — a rate error, not an arithmetic one."
        r" The correct answer is **C**.",
        ["Eq(Rational(24, 3), 8)", "Eq(8*10, 80)"],
        80, {8: "reported the per-minute rate",
             34: "added 10 to 24",
             240: "multiplied 24 by 10 without using the rate"}))

    # Q4 E alg SPR
    assert 2 * 5 - 3 * 2 == 4
    qs.append(spr(
        "SAT-P11-M1-Q04", M, 4, "algebra", "evaluating_expressions", "easy",
        r"What is the value of $2x - 3y$ when $x = 5$ and $y = 2$?",
        ["4"],
        r"Substitute both values and follow the order of operations:"
        r" $$2(5) - 3(2) = 10 - 6 = 4.$$"
        r" Each coefficient multiplies its own variable — $2x$ is $2$"
        r" times $x$, not $2$ times $x$ and $y$ together.",
        ["Eq(2*5 - 3*2, 4)"]))

    # Q5 E geo
    assert 2 * 7 == 14
    qs.append(mcq_listed(
        "SAT-P11-M1-Q05", M, 5, "geometry_trig", "circle_basics", "easy",
        r"A circle has a diameter of 14. What is the circumference of the"
        r" circle?",
        {"A": r"$7\pi$", "B": r"$14\pi$", "C": r"$28\pi$", "D": r"$49\pi$"},
        "B",
        r"Circumference is $C = \pi d$, or equivalently $2\pi r$. With"
        r" $d = 14$ the radius is 7, so"
        r" $$C = 2\pi(7) = 14\pi.$$"
        r" Using the diameter where the radius belongs gives"
        r" $2\pi(14) = 28\pi$, and $\pi r^2 = 49\pi$ is the AREA, not the"
        r" circumference."
        r" The correct answer is **B**.",
        ["Eq(2*7, 14)", "Eq(7**2, 49)", "Eq(2*14, 28)"]))

    # Q6 E adv
    assert 5 - 2 * (-3) == 11
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q06", M, 6, "advanced_math", "function_notation", "easy",
        r"The function $f$ is defined by $f(x) = 5 - 2x$. What is the"
        r" value of $f(-3)$?",
        r"Substitute $x = -3$ and keep the double negative:"
        r" $$f(-3) = 5 - 2(-3) = 5 + 6 = 11.$$"
        r" Ignoring the sign of the input gives $5 - 6 = -1$, the most"
        r" common wrong answer here."
        r" The correct answer is **B**.",
        ["Eq(5 - 2*(-3), 11)", "Eq(5 - 2*3, -1)"],
        11, {-1: "used $x = 3$ instead of $x = -3$",
             16: "added 11 to 5",
             22: "doubled the correct result"}))

    # Q7 E alg
    assert Rational(18, 6) * 11 == 33
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q07", M, 7, "algebra", "direct_variation", "easy",
        r"The quantity $y$ is directly proportional to $x$, and $y = 18$"
        r" when $x = 6$. What is the value of $y$ when $x = 11$?",
        r"Direct proportion means $y = kx$ for a fixed constant $k$. From"
        r" the given pair,"
        r" $$k = \frac{18}{6} = 3.$$"
        r" So $y = 3x$, and at $x = 11$,"
        r" $$y = 3(11) = 33.$$"
        r" Adding the change in $x$ to $y$ — $18 + 5 = 23$ — treats a"
        r" proportional relationship as an additive one."
        r" The correct answer is **C**.",
        ["Eq(Rational(18, 6), 3)", "Eq(3*11, 33)"],
        33, {3: "reported the constant of proportionality",
             23: "added the change in $x$ to $y$",
             66: "doubled the correct value"}))

    # Q8 E geo
    assert 2 * 70 + 40 == 180
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q08", M, 8, "geometry_trig", "triangle_angles", "easy",
        r"In an isosceles triangle, the angle between the two congruent"
        r" sides measures $40^\circ$. What is the measure, in degrees, of"
        r" each of the other two angles?",
        r"The two angles opposite the congruent sides are equal. Call each"
        r" one $b$; the three angles sum to $180^\circ$:"
        r" $$40 + 2b = 180 \;\Rightarrow\; 2b = 140 \;\Rightarrow\; b = 70.$$"
        r" The value 140 is the COMBINED measure of the two base angles —"
        r" it still has to be split in half."
        r" The correct answer is **C**.",
        ["Eq(40 + 2*70, 180)", "Eq(180 - 40, 140)"],
        70, {20: "halved the given angle",
             40: "repeated the given angle",
             140: "gave the combined measure of both angles"}))

    # Q9 M adv SPR
    assert expand((x - 8) * (x + 3)) == x**2 - 5 * x - 24
    qs.append(spr(
        "SAT-P11-M1-Q09", M, 9, "advanced_math", "quadratic_equations",
        "medium",
        r"What is the positive solution of $x^2 - 5x - 24 = 0$?",
        ["8"],
        r"Look for two numbers whose product is $-24$ and whose sum is"
        r" $-5$: those are $-8$ and $3$. So"
        r" $$x^2 - 5x - 24 = (x - 8)(x + 3) = 0,$$"
        r" giving $x = 8$ or $x = -3$. The positive solution is"
        r" $$x = 8.$$"
        r" Checking: $64 - 40 - 24 = 0$.",
        ["Eq(expand((x - 8)*(x + 3)), x**2 - 5*x - 24)",
         "Eq(8**2 - 5*8 - 24, 0)"]))

    # Q10 M psda — box plot figure
    FIVE = (12, 20, 27, 38, 46)
    assert FIVE[3] - FIVE[1] == 18 and FIVE[4] - FIVE[0] == 34
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q10", M, 10, "psda", "center_spread", "medium",
        r"The box plot summarises the daily high temperatures, in degrees"
        r" Fahrenheit, recorded at a weather station. What is the"
        r" interquartile range of the data?",
        r"The interquartile range is the width of the BOX — the third"
        r" quartile minus the first quartile. Reading the plot,"
        r" $Q_1 = 20$ and $Q_3 = 38$, so"
        r" $$\text{IQR} = 38 - 20 = 18.$$"
        r" The line inside the box is the median, 27, and the whisker tips"
        r" give the range $46 - 12 = 34$ — both are different summaries of"
        r" the same picture."
        r" The correct answer is **B**.",
        ["Eq(38 - 20, 18)", "Eq(46 - 12, 34)", "Eq(27 - 20, 7)"],
        18, {7: "computed the median minus $Q_1$",
             27: "reported the median",
             34: "reported the full range"},
        fig=figure("sat-p11-m1-q10",
                   "Box plot with minimum 12, first quartile 20, median 27, "
                   "third quartile 38, and maximum 46")))

    # Q11 M alg — perpendicular slope
    assert _solve(Eq(3 * x + 4 * y, 8), y)[0] == -Rational(3, 4) * x + 2
    assert Rational(-3, 4) * Rational(4, 3) == -1
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q11", M, 11, "algebra", "parallel_perpendicular_lines",
        "medium",
        r"Line $\ell$ is given by $3x + 4y = 8$. What is the slope of a"
        r" line perpendicular to $\ell$?",
        r"Solve for $y$ to read off the slope of $\ell$:"
        r" $$4y = -3x + 8 \;\Rightarrow\; y = -\frac{3}{4}x + 2,$$"
        r" so $\ell$ has slope $-\frac{3}{4}$. A perpendicular line has"
        r" the NEGATIVE RECIPROCAL slope — flip the fraction and change"
        r" the sign:"
        r" $$m_\perp = \frac{4}{3}.$$"
        r" Check: $-\frac{3}{4} \cdot \frac{4}{3} = -1$, as required."
        r" Flipping without changing the sign gives $-\frac{4}{3}$, and"
        r" changing only the sign gives $\frac{3}{4}$."
        r" The correct answer is **D**.",
        ["Eq(Rational(-3,4)*Rational(4,3), -1)",
         "Eq(-3*2 + 4*Rational(7,2), 8)"],
        Rational(4, 3),
        {Rational(-4, 3): "flipped the fraction without changing the sign",
         Rational(-3, 4): "reported the slope of $\\ell$ itself",
         Rational(3, 4): "changed the sign without flipping"},
        fmt=frac))

    # Q12 M adv — negative rational exponent
    assert 16 ** Rational(-1, 2) == Rational(1, 4)
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q12", M, 12, "advanced_math", "exponent_rules", "medium",
        r"What is the value of $16^{-\frac{1}{2}}$?",
        r"A negative exponent means a reciprocal, and the exponent"
        r" $\frac{1}{2}$ means a square root:"
        r" $$16^{-1/2} = \frac{1}{16^{1/2}} = \frac{1}{\sqrt{16}}"
        r" = \frac{1}{4}.$$"
        r" A negative exponent never makes the value negative — that is"
        r" the trap in the two negative choices. Ignoring the minus sign"
        r" entirely gives 4."
        r" The correct answer is **C**.",
        ["Eq(16**Rational(-1,2), Rational(1,4))", "Eq(sqrt(16), 4)"],
        Rational(1, 4),
        {-4: "made the value negative instead of taking a reciprocal",
         Rational(-1, 4): "took the reciprocal AND the sign negative",
         4: "ignored the negative sign in the exponent"},
        fmt=frac))

    # Q13 M geo — 30-60-90
    assert 6**2 + (6 * sqrt(3)) ** 2 == 12**2
    qs.append(mcq_listed(
        "SAT-P11-M1-Q13", M, 13, "geometry_trig", "special_right_triangles",
        "medium",
        r"In a right triangle, one acute angle measures $30^\circ$ and the"
        r" hypotenuse has length 12. What is the length of the side"
        r" opposite the $60^\circ$ angle?",
        {"A": r"$6$", "B": r"$6\sqrt{2}$", "C": r"$6\sqrt{3}$",
         "D": r"$12\sqrt{3}$"},
        "C",
        r"A $30\text{-}60\text{-}90$ triangle has sides in the ratio"
        r" $1 : \sqrt{3} : 2$, where the shortest side faces the"
        r" $30^\circ$ angle and the hypotenuse is twice that side. With"
        r" hypotenuse 12,"
        r" $$\text{short leg} = \frac{12}{2} = 6,$$"
        r" $$\text{side opposite } 60^\circ = 6\sqrt{3}.$$"
        r" Check: $6^2 + (6\sqrt{3})^2 = 36 + 108 = 144 = 12^2$. The"
        r" answer 6 is the side opposite $30^\circ$, and $6\sqrt{2}$ would"
        r" belong to a $45\text{-}45\text{-}90$ triangle."
        r" The correct answer is **C**.",
        ["Eq(6**2 + (6*sqrt(3))**2, 144)", "Eq(sqrt(144), 12)",
         "Eq((6*sqrt(3))**2, 108)"]))

    # Q14 M psda SPR — histogram figure
    STARTS, COUNTS = [0, 10, 20, 30, 40], [3, 8, 11, 6, 2]
    assert sum(COUNTS) == 30 and sum(COUNTS[2:]) == 19
    qs.append(spr(
        "SAT-P11-M1-Q14", M, 14, "psda", "reading_graphs", "medium",
        r"The histogram shows the number of minutes 30 customers waited"
        r" in a queue. Each bar covers the interval from its left edge up"
        r" to but not including its right edge. How many of the customers"
        r" waited 20 minutes or more?",
        ["19"],
        r"Three bars cover waits of 20 minutes or more — the bars"
        r" beginning at 20, 30, and 40. Their heights are 11, 6, and 2,"
        r" so the count is"
        r" $$11 + 6 + 2 = 19.$$"
        r" As a check, the two bars below 20 minutes hold $3 + 8 = 11$"
        r" customers, and $19 + 11 = 30$, the full group.",
        ["Eq(11 + 6 + 2, 19)", "Eq(3 + 8, 11)", "Eq(19 + 11, 30)"],
        fig=figure("sat-p11-m1-q14",
                   "Histogram of waiting times in 10-minute intervals from "
                   "0 to 50 with frequencies 3, 8, 11, 6, and 2")))

    # Q15 M alg — successive percent change
    assert 80 * Rational(3, 4) * Rational(6, 5) == 72
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q15", M, 15, "algebra", "percentages", "medium",
        r"The price of a jacket is $\$80$. The price is first reduced by"
        r" $25\%$, and the reduced price is then increased by $20\%$."
        r" What is the final price of the jacket, in dollars?",
        r"Apply the changes one at a time, each to the price in force at"
        r" that moment. After the discount,"
        r" $$80 \times 0.75 = 60.$$"
        r" After the markup on that new price,"
        r" $$60 \times 1.20 = 72.$$"
        r" Percent changes do not simply add: combining them as"
        r" $-25\% + 20\% = -5\%$ would give $\$76$, which is wrong"
        r" because the $20\%$ is taken on $\$60$, not on $\$80$."
        r" The correct answer is **B**.",
        ["Eq(80*Rational(3,4), 60)", "Eq(60*Rational(6,5), 72)",
         "Eq(80*Rational(95,100), 76)"],
        72, {60: "stopped after the discount",
             76: "combined the two percents as a single $-5\\%$",
             96: "applied only the increase"}))

    # Q16 M adv — minimum from factored form
    assert expand((x + 1) * (x - 7)) == x**2 - 6 * x - 7
    assert (3 + 1) * (3 - 7) == -16
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q16", M, 16, "advanced_math", "quadratic_vertex_form",
        "medium",
        r"The function $f$ is defined by $f(x) = (x + 1)(x - 7)$. What is"
        r" the minimum value of $f$?",
        r"The zeros are $x = -1$ and $x = 7$. A parabola is symmetric"
        r" about its vertex, so the vertex sits midway between them:"
        r" $$x = \frac{-1 + 7}{2} = 3.$$"
        r" The minimum value is the OUTPUT there:"
        r" $$f(3) = (3 + 1)(3 - 7) = 4 \times (-4) = -16.$$"
        r" Answering 3 gives the $x$-coordinate of the vertex, not the"
        r" minimum value, and $-7$ is the constant term of the expanded"
        r" form."
        r" The correct answer is **A**.",
        ["Eq(expand((x + 1)*(x - 7)), x**2 - 6*x - 7)",
         "Eq((3 + 1)*(3 - 7), -16)", "Eq(Rational(-1 + 7, 2), 3)"],
        -16, {-7: "reported the constant term",
              3: "reported the $x$-coordinate of the vertex",
              7: "reported the larger zero"}))

    # Q17 M adv — inverse variation
    assert 12 * 3 == 36 and Rational(36, 9) == 4
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q17", M, 17, "advanced_math", "inverse_variation",
        "medium",
        r"The quantity $z$ varies inversely as $w$, and $z = 12$ when"
        r" $w = 3$. What is the value of $z$ when $w = 9$?",
        r"Inverse variation means the PRODUCT is constant: $zw = k$. From"
        r" the given pair,"
        r" $$k = 12 \times 3 = 36.$$"
        r" So when $w = 9$,"
        r" $$z = \frac{36}{9} = 4.$$"
        r" Tripling $w$ divides $z$ by 3. Treating the relationship as"
        r" direct instead would multiply $z$ by 3, giving 36."
        r" The correct answer is **A**.",
        ["Eq(12*3, 36)", "Eq(Rational(36, 9), 4)"],
        4, {6: "halved the original value of $z$",
            36: "treated the relationship as direct variation",
            108: "multiplied 12 by 9"}))

    # Q18 H alg SPR — absolute value inequality
    assert abs(3 * 4 - 4) < 11 and not abs(3 * 5 - 4) < 11
    qs.append(spr(
        "SAT-P11-M1-Q18", M, 18, "algebra", "absolute_value", "hard",
        r"What is the greatest integer value of $x$ that satisfies"
        r" $|3x - 4| < 11$?",
        ["4"],
        r"An absolute value less than 11 means the inside lies strictly"
        r" between $-11$ and $11$:"
        r" $$-11 < 3x - 4 < 11.$$"
        r" Add 4 throughout:"
        r" $$-7 < 3x < 15.$$"
        r" Divide by 3:"
        r" $$-\frac{7}{3} < x < 5.$$"
        r" The inequality is strict, so $x = 5$ is excluded and the"
        r" greatest integer that works is"
        r" $$x = 4.$$"
        r" Checking the two candidates: $|3(4) - 4| = 8 < 11$, but"
        r" $|3(5) - 4| = 11$, which is not less than 11.",
        ["Eq(Abs(3*4 - 4), 8)", "8 < 11", "Eq(Abs(3*5 - 4), 11)",
         "Eq(Rational(15, 3), 5)"]))

    # Q19 H psda — scatterplot figure, residual
    PTS = [(1, 8), (2, 8), (3, 12), (4, 12), (5, 16), (6, 20), (7, 18),
           (8, 22)]
    assert 2 * 6 + 5 == 17 and 20 - 17 == 3
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q19", M, 19, "psda", "linear_models_fit", "hard",
        r"The scatterplot shows eight data points and the line of best"
        r" fit $y = 2x + 5$. For the data point with $x = 6$, by how much"
        r" does the actual $y$-value exceed the value predicted by the"
        r" line?",
        r"Evaluate the model at $x = 6$:"
        r" $$y = 2(6) + 5 = 17.$$"
        r" The plotted point at $x = 6$ sits at $y = 20$, so the actual"
        r" value exceeds the prediction by"
        r" $$20 - 17 = 3.$$"
        r" That difference is called the residual. Answering 17 gives the"
        r" prediction itself rather than the gap, and 2 and 5 are the"
        r" slope and intercept of the model."
        r" The correct answer is **B**.",
        ["Eq(2*6 + 5, 17)", "Eq(20 - 17, 3)"],
        3, {2: "reported the slope of the model",
            5: "reported the $y$-intercept of the model",
            17: "reported the predicted value"},
        fig=figure("sat-p11-m1-q19",
                   "Scatterplot of eight points with the line of best fit "
                   "y = 2x + 5 drawn through them")))

    # Q20 H geo — sphere
    assert Rational(4, 3) * 3**3 == 36 and 4 * 3**2 == 36
    qs.append(mcq_listed(
        "SAT-P11-M1-Q20", M, 20, "geometry_trig", "solids_volume_surface",
        "hard",
        r"A sphere has a volume of $36\pi$ cubic centimetres. What is the"
        r" surface area, in square centimetres, of the sphere?",
        {"A": r"$9\pi$", "B": r"$12\pi$", "C": r"$27\pi$", "D": r"$36\pi$"},
        "D",
        r"Use the volume to recover the radius:"
        r" $$\frac{4}{3}\pi r^3 = 36\pi \;\Rightarrow\; r^3 = 27"
        r" \;\Rightarrow\; r = 3.$$"
        r" Then apply the surface-area formula:"
        r" $$S = 4\pi r^2 = 4\pi(9) = 36\pi.$$"
        r" The numerical coincidence — volume and surface area both"
        r" $36\pi$ — happens only at $r = 3$; the units differ, so it is"
        r" not a shortcut. Answering $9\pi$ uses $\pi r^2$, the area of a"
        r" flat circle."
        r" The correct answer is **D**.",
        ["Eq(Rational(4,3)*3**3, 36)", "Eq(4*3**2, 36)", "Eq(3**3, 27)"]))

    # Q21 H adv SPR — exponential growth
    assert 4000 * Rational(5, 4) ** 2 == 6250
    qs.append(spr(
        "SAT-P11-M1-Q21", M, 21, "advanced_math", "exponential_models",
        "hard",
        r"A town's population is 4,000 and increases by $25\%$ each"
        r" year. What will the population be after 2 years?",
        ["6250"],
        r"A $25\%$ annual increase multiplies the population by $1.25$"
        r" each year, so after 2 years"
        r" $$4000(1.25)^2 = 4000(1.5625) = 6250.$$"
        r" Step by step: after one year $4000 \times 1.25 = 5000$, and"
        r" after the second $5000 \times 1.25 = 6250$. Adding $25\%$ of"
        r" the ORIGINAL population twice would give only 6,000 — growth"
        r" compounds on the new total each year.",
        ["Eq(4000*Rational(5,4), 5000)", "Eq(5000*Rational(5,4), 6250)",
         "Eq(4000*Rational(5,4)**2, 6250)", "Ne(4000 + 2*1000, 6250)"]))

    # Q22 H alg — line tangent to a parabola
    assert expand((x - 2) ** 2) == x**2 - 4 * x + 4
    qs.append(mcq_numeric(
        "SAT-P11-M1-Q22", M, 22, "algebra", "systems_nonlinear", "hard",
        r"In the $xy$-plane, the graphs of $y = x^2 - 4x + 7$ and $y = 3$"
        r" intersect at exactly one point. What is the $x$-coordinate of"
        r" that point?",
        r"Set the two expressions equal and collect everything on one"
        r" side:"
        r" $$x^2 - 4x + 7 = 3 \;\Rightarrow\; x^2 - 4x + 4 = 0.$$"
        r" The left side is a perfect square:"
        r" $$(x - 2)^2 = 0 \;\Rightarrow\; x = 2.$$"
        r" The repeated root is exactly why there is only ONE intersection"
        r" point — the line is tangent to the parabola at the vertex."
        r" Adding 3 instead of subtracting gives $x^2 - 4x + 10 = 0$,"
        r" which has no real solution at all."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 2)**2), x**2 - 4*x + 4)",
         "Eq(2**2 - 4*2 + 7, 3)"],
        2, {4: "solved $x^2 = 4x$ and took the nonzero root",
            7: "reported the constant term",
            10: "added 3 to both sides instead of subtracting"}))

    return qs


# ─── Module 2, easier form (11E / 9M / 2H) ────────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg
    assert _solve(Eq(x - 8, 21), x) == [29]
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $x - 8 = 21$, what is the value of $x$?",
        r"Add 8 to both sides:"
        r" $$x = 21 + 8 = 29.$$"
        r" Subtracting 8 instead of adding gives 13 — always undo the"
        r" operation shown, not repeat it."
        r" The correct answer is **C**.",
        ["Eq(29 - 8, 21)", "Eq(21 + 8, 29)"],
        29, {8: "answered with the constant in the equation",
             13: "subtracted 8 instead of adding",
             168: "multiplied 21 by 8"}))

    # Q2 E adv
    assert expand((x + 3) ** 2) == x**2 + 6 * x + 9
    qs.append(mcq_listed(
        "SAT-P11-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $(x + 3)^2$?",
        {"A": r"$x^2 + 9$", "B": r"$x^2 + 3x + 9$",
         "C": r"$x^2 + 6x + 9$", "D": r"$x^2 + 9x + 9$"},
        "C",
        r"Squaring a binomial is not squaring each term. Expand it fully:"
        r" $$(x + 3)^2 = (x + 3)(x + 3) = x^2 + 3x + 3x + 9"
        r" = x^2 + 6x + 9.$$"
        r" The middle term is twice the product of the two terms,"
        r" $2 \cdot x \cdot 3 = 6x$. Dropping it entirely gives choice A,"
        r" the single most common algebra error on this pattern."
        r" The correct answer is **C**.",
        ["Eq(expand((x + 3)**2), x**2 + 6*x + 9)",
         "Eq((5 + 3)**2, 5**2 + 6*5 + 9)"]))

    # Q3 E psda SPR
    assert Rational(25, 100) * 60 == 15
    qs.append(spr(
        "SAT-P11-M2E-Q03", M, 3, "psda", "percentages", "easy",
        r"In a survey of 60 people, $25\%$ answered yes. How many of the"
        r" people surveyed answered yes?",
        ["15"],
        r"Twenty-five percent is one quarter:"
        r" $$0.25 \times 60 = \frac{60}{4} = 15.$$",
        ["Eq(Rational(25,100)*60, 15)", "Eq(Rational(60, 4), 15)"]))

    # Q4 E alg
    assert _solve(Eq(2 * (x + 5), 24), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q04", M, 4, "algebra", "linear_equations_one_var",
        "easy",
        r"If $2(x + 5) = 24$, what is the value of $x$?",
        r"Divide both sides by 2 first:"
        r" $$x + 5 = 12 \;\Rightarrow\; x = 7.$$"
        r" Stopping at $x + 5 = 12$ gives 12, and distributing the 2 to"
        r" only the $x$ produces $2x + 5 = 24$ and the answer $9.5$."
        r" The correct answer is **A**.",
        ["Eq(2*(7 + 5), 24)", "Eq(Rational(24, 2) - 5, 7)"],
        7, {Rational(19, 2): "distributed the 2 to only the $x$",
            12: "stopped at $x + 5 = 12$",
            19: "forgot to divide by 2"},
        fmt=smart))

    # Q5 E geo
    assert Rational(1, 2) * 10 * 6 == 30
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q05", M, 5, "geometry_trig", "area_perimeter", "easy",
        r"A triangle has a base of length 10 and a height of 6. What is"
        r" the area of the triangle?",
        r"The area of a triangle is half the base times the height:"
        r" $$A = \frac{1}{2}(10)(6) = 30.$$"
        r" Forgetting the factor of $\frac{1}{2}$ gives 60 — that is the"
        r" area of the rectangle the triangle fills half of."
        r" The correct answer is **D**.",
        ["Eq(Rational(1,2)*10*6, 30)", "Eq(10*6, 60)"],
        30, {8: "halved the sum of the base and the height",
             15: "halved the height instead of the product",
             16: "added the base and the height"}))

    # Q6 E adv
    assert 4 * 3 - 3**2 == 3
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q06", M, 6, "advanced_math", "function_notation",
        "easy",
        r"The function $f$ is defined by $f(x) = 4x - x^2$. What is the"
        r" value of $f(3)$?",
        r"Substitute $x = 3$, squaring before subtracting:"
        r" $$f(3) = 4(3) - 3^2 = 12 - 9 = 3.$$"
        r" Reversing the subtraction gives $-3$, and adding instead of"
        r" subtracting gives 21."
        r" The correct answer is **C**.",
        ["Eq(4*3 - 3**2, 3)", "Eq(4*3, 12)"],
        3, {-9: "evaluated only $-x^2$",
            -3: "reversed the order of the subtraction",
            21: "added the two terms instead of subtracting"}))

    # Q7 E alg SPR
    assert 5 * 8 + 12 == 52
    qs.append(spr(
        "SAT-P11-M2E-Q07", M, 7, "algebra", "linear_models", "easy",
        r"The equation $y = 5x + 12$ models the total cost $y$, in"
        r" dollars, of renting a kayak for $x$ hours. What is the total"
        r" cost, in dollars, of renting a kayak for 8 hours?",
        ["52"],
        r"Substitute $x = 8$:"
        r" $$y = 5(8) + 12 = 40 + 12 = 52.$$"
        r" The 5 is the hourly rate and the 12 is a one-time charge that"
        r" is added no matter how long the rental lasts.",
        ["Eq(5*8 + 12, 52)"]))

    # Q8 E adv
    assert sqrt(49 * 3**2) == 7 * 3
    qs.append(mcq_listed(
        "SAT-P11-M2E-Q08", M, 8, "advanced_math", "radicals", "easy",
        r"For $x > 0$, which of the following is equivalent to"
        r" $\sqrt{49x^2}$?",
        {"A": r"$7x$", "B": r"$7x^2$", "C": r"$14x$", "D": r"$49x$"},
        "A",
        r"A square root distributes over a product, so take the root of"
        r" each factor:"
        r" $$\sqrt{49x^2} = \sqrt{49}\cdot\sqrt{x^2} = 7x$$"
        r" (using $x > 0$ so that $\sqrt{x^2} = x$). Testing $x = 3$:"
        r" $\sqrt{49 \cdot 9} = \sqrt{441} = 21 = 7(3)$. Doubling 7"
        r" instead of taking the root of 49 gives $14x$."
        r" The correct answer is **A**.",
        ["Eq(sqrt(49*3**2), 21)", "Eq(7*3, 21)"]))

    # Q9 E alg
    assert 3 * 5 - 8 > 4 and not 3 * 4 - 8 > 4
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q09", M, 9, "algebra", "linear_inequalities", "easy",
        r"What is the smallest integer value of $x$ that satisfies"
        r" $3x - 8 > 4$?",
        r"Add 8 to both sides, then divide by 3:"
        r" $$3x > 12 \;\Rightarrow\; x > 4.$$"
        r" The inequality is strict, so $x = 4$ does not work"
        r" ($3(4) - 8 = 4$, which is not greater than 4). The smallest"
        r" integer that does work is"
        r" $$x = 5,$$"
        r" since $3(5) - 8 = 7 > 4$."
        r" The correct answer is **C**.",
        ["Eq(3*5 - 8, 7)", "7 > 4", "Eq(3*4 - 8, 4)",
         "Eq(Rational(12, 3), 4)"],
        5, {2: "solved $3x > 4$ and rounded up",
            4: "used the boundary value, which the strict sign excludes",
            12: "stopped at 3x > 12"}))

    # Q10 E geo
    assert 180 - 118 == 62
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q10", M, 10, "geometry_trig", "angle_relationships",
        "easy",
        r"Two angles are supplementary. One of the angles measures"
        r" $118^\circ$. What is the measure, in degrees, of the other"
        r" angle?",
        r"Supplementary angles sum to $180^\circ$:"
        r" $$180 - 118 = 62.$$"
        r" COMPLEMENTARY angles are the ones that sum to $90^\circ$;"
        r" using that rule here would give $-28$, and subtracting from a"
        r" full turn gives 242."
        r" The correct answer is **B**.",
        ["Eq(180 - 118, 62)", "Eq(360 - 118, 242)"],
        62, {28: "used the complementary rule instead",
             118: "repeated the given angle",
             242: "subtracted from $360^\\circ$"}))

    # Q11 E adv
    assert 2 * 4 + 1 == 9
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q11", M, 11, "advanced_math", "function_notation",
        "easy",
        r"The function $g$ is defined by $g(x) = 2x + 1$. If $g(a) = 9$,"
        r" what is the value of $a$?",
        r"Set the rule equal to the given output and solve:"
        r" $$2a + 1 = 9 \;\Rightarrow\; 2a = 8 \;\Rightarrow\; a = 4.$$"
        r" Adding 1 instead of subtracting gives 5, and evaluating"
        r" $g(9) = 19$ answers the wrong question entirely."
        r" The correct answer is **A**.",
        ["Eq(2*4 + 1, 9)", "Eq(Rational(9 - 1, 2), 4)"],
        4, {Rational(9, 2): "ignored the $+1$",
            5: "added 1 instead of subtracting",
            19: "computed $g(9)$"},
        fmt=smart))

    # Q12 M alg SPR
    assert Rational(11 - 3, 6 - 2) == 2 and 3 - 2 * 2 == -1
    qs.append(spr(
        "SAT-P11-M2E-Q12", M, 12, "algebra", "linear_functions_slope",
        "medium",
        r"A line in the $xy$-plane passes through the points $(2, 3)$ and"
        r" $(6, 11)$. What is the $y$-coordinate of the $y$-intercept of"
        r" the line?",
        ["-1"],
        r"Find the slope first:"
        r" $$m = \frac{11 - 3}{6 - 2} = \frac{8}{4} = 2.$$"
        r" Now substitute one point into $y = 2x + b$ using $(2, 3)$:"
        r" $$3 = 2(2) + b \;\Rightarrow\; b = -1.$$"
        r" Checking with the other point: $2(6) - 1 = 11$, as required.",
        ["Eq(Rational(11 - 3, 6 - 2), 2)", "Eq(2*2 + (-1), 3)",
         "Eq(2*6 + (-1), 11)"]))

    # Q13 M adv
    assert sum(_solve(Eq((x - 2) * (x + 5), 0), x)) == -3
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q13", M, 13, "advanced_math", "quadratic_equations",
        "medium",
        r"What is the sum of the solutions of $(x - 2)(x + 5) = 0$?",
        r"A product is zero exactly when one of its factors is zero:"
        r" $$x - 2 = 0 \;\Rightarrow\; x = 2, \qquad"
        r" x + 5 = 0 \;\Rightarrow\; x = -5.$$"
        r" Their sum is"
        r" $$2 + (-5) = -3.$$"
        r" Notice the solutions carry the OPPOSITE signs to the numbers"
        r" written in the factors; reading them off as $-2$ and $5$ gives"
        r" the sign-flipped answer 3."
        r" The correct answer is **C**.",
        ["Eq(expand((x - 2)*(x + 5)), x**2 + 3*x - 10)",
         "Eq(2 + (-5), -3)", "Eq(2*(-5), -10)"],
        -3, {-10: "gave the product of the solutions",
             -7: "gave the difference of the solutions",
             3: "read the signs straight out of the factors"}))

    # Q14 M psda
    assert 5 * 12 - (8 + 10 + 15 + 16) == 11
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q14", M, 14, "psda", "center_spread", "medium",
        r"The mean of five numbers is 12. Four of the numbers are 8, 10,"
        r" 15, and 16. What is the fifth number?",
        r"A mean of 12 across five numbers means they total"
        r" $$5 \times 12 = 60.$$"
        r" The four known numbers sum to"
        r" $$8 + 10 + 15 + 16 = 49.$$"
        r" The fifth number is what is left:"
        r" $$60 - 49 = 11.$$"
        r" It is not 12 — the missing value equals the mean only when the"
        r" other numbers already average exactly 12, and here they"
        r" average $12.25$."
        r" The correct answer is **A**.",
        ["Eq(5*12, 60)", "Eq(8 + 10 + 15 + 16, 49)", "Eq(60 - 49, 11)"],
        11, {12: "assumed the missing value equals the mean",
             49: "gave the sum of the four known numbers",
             60: "gave the total of all five numbers"}))

    # Q15 M alg SPR
    assert 500 - 12 * 20 == 260
    qs.append(spr(
        "SAT-P11-M2E-Q15", M, 15, "algebra", "linear_models", "medium",
        r"A tank holds 500 litres of water and drains at a constant rate"
        r" of 12 litres per minute. After how many minutes will the tank"
        r" hold 260 litres?",
        ["20"],
        r"The volume after $t$ minutes is $500 - 12t$. Set it equal to"
        r" 260:"
        r" $$500 - 12t = 260.$$"
        r" Subtract 500 and divide by $-12$, or equivalently work with the"
        r" amount drained:"
        r" $$12t = 500 - 260 = 240 \;\Rightarrow\; t = 20.$$",
        ["Eq(500 - 260, 240)", "Eq(Rational(240, 12), 20)",
         "Eq(500 - 12*20, 260)"]))

    # Q16 M adv
    assert 3 ** (2 * 2) == 81
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q16", M, 16, "advanced_math", "exponent_equations",
        "medium",
        r"If $3^{2x} = 81$, what is the value of $x$?",
        r"Write 81 as a power of 3:"
        r" $$81 = 3^4, \qquad\text{so}\qquad 3^{2x} = 3^4.$$"
        r" Equal bases force equal exponents:"
        r" $$2x = 4 \;\Rightarrow\; x = 2.$$"
        r" Stopping at $2x = 4$ and reporting 4 is the intended slip."
        r" The correct answer is **B**.",
        ["Eq(3**4, 81)", "Eq(3**(2*2), 81)"],
        2, {Rational(1, 2): "solved $2x = 1$",
            3: "took a cube root of 81",
            4: "reported $2x$ instead of $x$"},
        fmt=smart))

    # Q17 M geo
    assert 3**2 * 10 == 90
    qs.append(mcq_listed(
        "SAT-P11-M2E-Q17", M, 17, "geometry_trig", "solids_volume_surface",
        "medium",
        r"A right circular cylinder has a radius of 3 and a height of 10."
        r" What is the volume of the cylinder?",
        {"A": r"$9\pi$", "B": r"$30\pi$", "C": r"$60\pi$", "D": r"$90\pi$"},
        "D",
        r"The volume of a cylinder is the area of its circular base times"
        r" its height:"
        r" $$V = \pi r^2 h = \pi(3)^2(10) = 90\pi.$$"
        r" The base alone has area $9\pi$, and forgetting to square the"
        r" radius gives $\pi(3)(10) = 30\pi$."
        r" The correct answer is **D**.",
        ["Eq(3**2*10, 90)", "Eq(3**2, 9)", "Eq(3*10, 30)"]))

    # Q18 M alg
    _s18 = _solve([Eq(x + y, 14), Eq(x - y, 4)], [x, y], dict=True)[0]
    assert _s18[x] == 9 and _s18[y] == 5
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q18", M, 18, "algebra", "systems_two_variables",
        "medium",
        r"$$x + y = 14$$"
        r"$$x - y = 4$$"
        r"If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $x$?",
        r"Adding the two equations eliminates $y$:"
        r" $$2x = 18 \;\Rightarrow\; x = 9.$$"
        r" Substituting back gives $9 + y = 14$, so $y = 5$. The question"
        r" asks for $x$, so the answer is 9 — reporting $y = 5$ instead is"
        r" the intended trap."
        r" The correct answer is **C**.",
        ["Eq(9 + 5, 14)", "Eq(9 - 5, 4)", "Eq(Rational(14 + 4, 2), 9)"],
        9, {4: "read off the right side of the second equation",
            5: "reported $y$ instead of $x$",
            14: "read off the right side of the first equation"}))

    # Q19 M adv SPR
    assert (4**2 + 3 * 4) - (2**2 + 3 * 2) == 18
    qs.append(spr(
        "SAT-P11-M2E-Q19", M, 19, "advanced_math", "function_notation",
        "medium",
        r"The function $f$ is defined by $f(x) = x^2 + 3x$. What is the"
        r" value of $f(4) - f(2)$?",
        ["18"],
        r"Evaluate each output separately, then subtract:"
        r" $$f(4) = 4^2 + 3(4) = 16 + 12 = 28,$$"
        r" $$f(2) = 2^2 + 3(2) = 4 + 6 = 10,$$"
        r" $$f(4) - f(2) = 28 - 10 = 18.$$"
        r" Note that $f(4) - f(2)$ is not $f(4 - 2) = f(2) = 10$ —"
        r" function notation does not distribute over subtraction.",
        ["Eq(4**2 + 3*4, 28)", "Eq(2**2 + 3*2, 10)", "Eq(28 - 10, 18)"]))

    # Q20 M psda
    assert Rational(4, 10) * Rational(5, 10) == Rational(1, 5)
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q20", M, 20, "psda", "probability", "medium",
        r"Two events are independent. The probability that the first"
        r" occurs is $0.4$, and the probability that the second occurs is"
        r" $0.5$. What is the probability that both events occur?",
        r"For independent events the probability that both occur is the"
        r" PRODUCT of the individual probabilities:"
        r" $$0.4 \times 0.5 = 0.2 = \frac{1}{5}.$$"
        r" Adding them instead gives $0.9$, which would be the answer to"
        r" a different (and, for overlapping events, incorrect) question."
        r" The correct answer is **B**.",
        ["Eq(Rational(4,10)*Rational(5,10), Rational(1,5))",
         "Eq(Rational(4,10) + Rational(5,10), Rational(9,10))"],
        Rational(1, 5),
        {Rational(1, 10): "multiplied $0.4$ by $0.25$",
         Rational(2, 5): "reported only the first probability",
         Rational(9, 10): "added the two probabilities"},
        fmt=frac))

    # Q21 H adv — radical equation with an extraneous root
    assert sqrt(9 + 7) == 9 - 5
    qs.append(mcq_numeric(
        "SAT-P11-M2E-Q21", M, 21, "advanced_math", "radical_equations",
        "hard",
        r"What is the solution of $\sqrt{x + 7} = x - 5$?",
        r"Square both sides:"
        r" $$x + 7 = (x - 5)^2 = x^2 - 10x + 25.$$"
        r" Collect everything on one side:"
        r" $$x^2 - 11x + 18 = 0 \;\Rightarrow\; (x - 2)(x - 9) = 0,$$"
        r" so $x = 2$ or $x = 9$. Squaring can create false solutions, so"
        r" check both in the ORIGINAL equation. At $x = 2$:"
        r" $\sqrt{9} = 3$ but $2 - 5 = -3$, so $x = 2$ fails. At $x = 9$:"
        r" $\sqrt{16} = 4$ and $9 - 5 = 4$, so"
        r" $$x = 9$$"
        r" is the only solution."
        r" The correct answer is **C**.",
        ["Eq(expand((x - 2)*(x - 9)), x**2 - 11*x + 18)",
         "Eq(sqrt(9 + 7), 4)", "Eq(9 - 5, 4)", "Ne(sqrt(2 + 7), 2 - 5)"],
        9, {-2: "made a sign error when factoring",
            2: "kept the extraneous solution",
            11: "reported the sum of the two roots"}))

    # Q22 H alg SPR
    assert Rational(-4, 2) == -2
    qs.append(spr(
        "SAT-P11-M2E-Q22", M, 22, "algebra", "linear_functions_slope",
        "hard",
        r"In the equation $4x + by = 10$, $b$ is a nonzero constant. If"
        r" the graph of this equation in the $xy$-plane has a slope of"
        r" $-2$, what is the value of $b$?",
        ["2"],
        r"Solve for $y$ to expose the slope:"
        r" $$by = -4x + 10 \;\Rightarrow\; y = -\frac{4}{b}x"
        r" + \frac{10}{b}.$$"
        r" Set the slope equal to $-2$:"
        r" $$-\frac{4}{b} = -2 \;\Rightarrow\; 4 = 2b \;\Rightarrow\; b = 2.$$"
        r" Checking, $4x + 2y = 10$ becomes $y = -2x + 5$, whose slope is"
        r" indeed $-2$.",
        ["Eq(Rational(-4, 2), -2)", "Eq(-2*3 + 5, -1)",
         "Eq(4*3 + 2*(-1), 10)"]))

    return qs


# ─── Module 2, harder form (2E / 7M / 13H) ────────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg
    assert _solve(Eq(9 * x, 54), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $9x = 54$, what is the value of $\dfrac{x}{3}$?",
        r"Solve for $x$ first:"
        r" $$x = \frac{54}{9} = 6.$$"
        r" Then divide by 3, as the question asks:"
        r" $$\frac{6}{3} = 2.$$"
        r" Stopping at $x = 6$ answers a question that was not asked, and"
        r" multiplying by 3 instead of dividing gives 18."
        r" The correct answer is **A**.",
        ["Eq(9*6, 54)", "Eq(Rational(6, 3), 2)"],
        2, {6: "stopped at the value of $x$",
            18: "multiplied by 3 instead of dividing",
            54: "restated the right side of the equation"}))

    # Q2 E adv
    assert 3 * 2**2 * 4 * 2**5 == 12 * 2**7
    qs.append(mcq_listed(
        "SAT-P11-M2H-Q02", M, 2, "advanced_math", "exponent_rules", "easy",
        r"Which of the following is equivalent to $(3x^2)(4x^5)$?",
        {"A": r"$7x^7$", "B": r"$7x^{10}$", "C": r"$12x^7$",
         "D": r"$12x^{10}$"},
        "C",
        r"Multiply the coefficients and ADD the exponents:"
        r" $$3 \times 4 = 12, \qquad x^{2 + 5} = x^7,$$"
        r" giving $12x^7$. Adding the coefficients instead of multiplying"
        r" gives 7, and multiplying the exponents gives $x^{10}$ — that"
        r" rule belongs to a power raised to a power."
        r" The correct answer is **C**.",
        ["Eq(3*2**2 * 4*2**5, 1536)", "Eq(12*2**7, 1536)",
         "Eq(2 + 5, 7)"]))

    # Q3 M psda SPR
    assert Rational(2, 5) * 30 == 12
    qs.append(spr(
        "SAT-P11-M2H-Q03", M, 3, "psda", "ratios_rates_proportions",
        "medium",
        r"In a class of 30 students, the ratio of girls to boys is"
        r" $2 : 3$. How many of the students are girls?",
        ["12"],
        r"A ratio of $2 : 3$ splits the class into $2 + 3 = 5$ equal"
        r" parts, so each part holds"
        r" $$\frac{30}{5} = 6 \text{ students}.$$"
        r" Girls occupy 2 of those parts:"
        r" $$2 \times 6 = 12.$$"
        r" (The 18 boys make up the other three parts, and"
        r" $12 + 18 = 30$.) Answering 2 out of 3 rather than 2 out of 5 is"
        r" the classic ratio error.",
        ["Eq(Rational(30, 5), 6)", "Eq(2*6, 12)", "Eq(12 + 18, 30)",
         "Eq(Rational(12, 18), Rational(2,3))"]))

    # Q4 M alg
    _s4 = _solve([Eq(2 * x - 3 * y, 6), Eq(x, 2 * y)], [x, y], dict=True)[0]
    assert _s4[x] == 12 and _s4[y] == 6
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q04", M, 4, "algebra", "systems_two_variables",
        "medium",
        r"$$2x - 3y = 6$$"
        r"$$x = 2y$$"
        r"If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $x + y$?",
        r"Substitute $x = 2y$ into the first equation:"
        r" $$2(2y) - 3y = 6 \;\Rightarrow\; 4y - 3y = 6 \;\Rightarrow\; y = 6.$$"
        r" Then $x = 2(6) = 12$, and"
        r" $$x + y = 12 + 6 = 18.$$"
        r" Reporting $x$ or $y$ alone gives 12 or 6 — both are steps on"
        r" the way, not the answer."
        r" The correct answer is **C**.",
        ["Eq(2*12 - 3*6, 6)", "Eq(12, 2*6)", "Eq(12 + 6, 18)"],
        18, {6: "reported $y$ alone", 12: "reported $x$ alone",
             24: "doubled $x$ instead of adding $y$"}))

    # Q5 M geo
    assert 2 * (5 + 8) == 26 and 5 * 8 == 40
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q05", M, 5, "geometry_trig", "area_perimeter",
        "medium",
        r"The length of a rectangle is 3 more than its width, and the"
        r" perimeter of the rectangle is 26. What is the area of the"
        r" rectangle?",
        r"Let $w$ be the width, so the length is $w + 3$. The perimeter"
        r" gives"
        r" $$2\big(w + (w + 3)\big) = 26 \;\Rightarrow\; 2(2w + 3) = 26"
        r" \;\Rightarrow\; 2w + 3 = 13.$$"
        r" So $w = 5$ and the length is 8. The area is"
        r" $$5 \times 8 = 40.$$"
        r" The value 13 is half the perimeter — the sum of one length and"
        r" one width, not an area."
        r" The correct answer is **C**.",
        ["Eq(2*(5 + 8), 26)", "Eq(5 + 3, 8)", "Eq(5*8, 40)"],
        40, {13: "reported half the perimeter",
             26: "reported the perimeter",
             55: "used a length of 11 instead of 8"}))

    # Q6 M adv
    assert expand((x - 5) * (x + 3)) == x**2 - 2 * x - 15
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q06", M, 6, "advanced_math", "quadratic_equations",
        "medium",
        r"The function $f$ is defined by $f(x) = x^2 - 2x$. For what"
        r" positive value of $x$ does $f(x) = 15$?",
        r"Set the rule equal to 15 and move everything to one side:"
        r" $$x^2 - 2x - 15 = 0 \;\Rightarrow\; (x - 5)(x + 3) = 0,$$"
        r" so $x = 5$ or $x = -3$. The question asks for the positive"
        r" value, so"
        r" $$x = 5.$$"
        r" Checking: $25 - 10 = 15$."
        r" The correct answer is **D**.",
        ["Eq(expand((x - 5)*(x + 3)), x**2 - 2*x - 15)",
         "Eq(5**2 - 2*5, 15)"],
        5, {-5: "flipped the sign of the correct root",
            -3: "reported the negative solution",
            3: "flipped the sign of the negative solution"}))

    # Q7 M alg SPR
    assert Rational(13, 10) * 70 == 91
    qs.append(spr(
        "SAT-P11-M2H-Q07", M, 7, "algebra", "percentages", "medium",
        r"A number increased by $30\%$ is 91. What is the number?",
        ["70"],
        r"Increasing a number by $30\%$ multiplies it by $1.30$, so if"
        r" $n$ is the number,"
        r" $$1.30n = 91 \;\Rightarrow\; n = \frac{91}{1.30} = 70.$$"
        r" Checking: $30\%$ of 70 is 21, and $70 + 21 = 91$. Taking"
        r" $30\%$ OFF of 91 instead would give $63.7$, which is not the"
        r" reverse of a $30\%$ increase.",
        ["Eq(Rational(13,10)*70, 91)", "Eq(Rational(30,100)*70, 21)",
         "Eq(70 + 21, 91)"]))

    # Q8 M adv
    assert -2 * (3 - 3) ** 2 + 8 == 8
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q08", M, 8, "advanced_math", "quadratic_vertex_form",
        "medium",
        r"What is the maximum value of the function"
        r" $f(x) = -2(x - 3)^2 + 8$?",
        r"The squared term $(x - 3)^2$ is never negative, and it is"
        r" multiplied by $-2$, so $-2(x - 3)^2$ is never positive. The"
        r" function is therefore largest when the square is zero, at"
        r" $x = 3$:"
        r" $$f(3) = -2(0) + 8 = 8.$$"
        r" Answering 3 gives the $x$-coordinate where the maximum occurs,"
        r" not the maximum value itself."
        r" The correct answer is **D**.",
        ["Eq(-2*(3 - 3)**2 + 8, 8)", "Eq(-2*(5 - 3)**2 + 8, 0)"],
        8, {-8: "flipped the sign of the constant",
            -2: "reported the leading coefficient",
            3: "reported the $x$-coordinate of the vertex"}))

    # Q9 M geo — 45-45-90
    assert (10 * sqrt(2)) ** 2 == 10**2 + 10**2
    qs.append(mcq_listed(
        "SAT-P11-M2H-Q09", M, 9, "geometry_trig", "special_right_triangles",
        "medium",
        r"In an isosceles right triangle, the hypotenuse has length"
        r" $10\sqrt{2}$. What is the length of each leg?",
        {"A": r"$10$", "B": r"$10\sqrt{2}$", "C": r"$20$",
         "D": r"$20\sqrt{2}$"},
        "A",
        r"An isosceles right triangle is a"
        r" $45\text{-}45\text{-}90$ triangle, whose sides are in the ratio"
        r" $1 : 1 : \sqrt{2}$. The hypotenuse is $\sqrt{2}$ times a leg,"
        r" so"
        r" $$\text{leg} = \frac{10\sqrt{2}}{\sqrt{2}} = 10.$$"
        r" Check with the Pythagorean theorem:"
        r" $10^2 + 10^2 = 200 = (10\sqrt{2})^2$. Multiplying by"
        r" $\sqrt{2}$ instead of dividing gives 20."
        r" The correct answer is **A**.",
        ["Eq((10*sqrt(2))**2, 200)", "Eq(10**2 + 10**2, 200)"]))

    # Q10 H alg — proportion equation
    assert _solve(Eq(2 / (x - 3), 6 / (x + 5)), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q10", M, 10, "algebra", "rational_equations", "hard",
        r"If $\dfrac{2}{x - 3} = \dfrac{6}{x + 5}$, what is the value of"
        r" $x$?",
        r"Cross-multiply, then distribute carefully on both sides:"
        r" $$2(x + 5) = 6(x - 3) \;\Rightarrow\; 2x + 10 = 6x - 18.$$"
        r" Collect the $x$ terms:"
        r" $$28 = 4x \;\Rightarrow\; x = 7.$$"
        r" Checking, $\frac{2}{4} = \frac{6}{12}$, both equal"
        r" $\frac{1}{2}$. Writing $6(x - 3)$ as $6x + 18$ gives $-2$, and"
        r" cross-multiplying the other way round gives $-9$."
        r" The correct answer is **D**.",
        ["Eq(Rational(2, 7 - 3), Rational(6, 7 + 5))",
         "Eq(2*(7 + 5), 6*(7 - 3))"],
        7, {-9: "cross-multiplied in the wrong direction",
            -2: "expanded $6(x - 3)$ as $6x + 18$",
            Rational(23, 4): "distributed the 2 to only the $x$"},
        fmt=smart))

    # Q11 H adv — exponential through two points
    assert 5 * 3**2 == 45
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q11", M, 11, "advanced_math", "exponential_models",
        "hard",
        r"The function $f$ is defined by $f(x) = a \cdot b^x$, where $a$"
        r" and $b$ are positive constants. If $f(0) = 5$ and $f(2) = 45$,"
        r" what is the value of $b$?",
        r"Any base to the power 0 is 1, so the first condition pins down"
        r" $a$:"
        r" $$f(0) = a \cdot b^0 = a = 5.$$"
        r" Now use the second condition:"
        r" $$f(2) = 5b^2 = 45 \;\Rightarrow\; b^2 = 9 \;\Rightarrow\; b = 3,$$"
        r" taking the positive root because $b$ is positive. Answering 9"
        r" stops at $b^2$, and 5 is the value of $a$."
        r" The correct answer is **A**.",
        ["Eq(5*3**2, 45)", "Eq(5*3**0, 5)", "Eq(Rational(45, 5), 9)"],
        3, {5: "reported $a$ instead of $b$",
            9: "stopped at $b^2$",
            45: "restated the given output"}))

    # Q12 H alg SPR — perpendicular line through a point
    assert Rational(-1, 4) * 4 == -1
    qs.append(spr(
        "SAT-P11-M2H-Q12", M, 12, "algebra", "parallel_perpendicular_lines",
        "hard",
        r"Line $k$ is perpendicular to the line"
        r" $y = -\dfrac{1}{4}x + 3$ and passes through the point"
        r" $(0, -2)$. What is the $y$-coordinate of the point on line $k$"
        r" where $x = 2$?",
        ["6"],
        r"Perpendicular slopes are negative reciprocals, so line $k$ has"
        r" slope"
        r" $$m = -\frac{1}{-\frac{1}{4}} = 4.$$"
        r" (Check: $-\frac{1}{4}\cdot 4 = -1$.) The point $(0, -2)$ is"
        r" the $y$-intercept, so"
        r" $$y = 4x - 2.$$"
        r" At $x = 2$,"
        r" $$y = 4(2) - 2 = 6.$$",
        ["Eq(Rational(-1,4)*4, -1)", "Eq(4*0 - 2, -2)",
         "Eq(4*2 - 2, 6)"]))

    # Q13 H adv — factor theorem on a cubic
    assert 2 * 2**3 + (-3) * 2**2 - 5 * 2 + 6 == 0
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q13", M, 13, "advanced_math", "polynomial_factors",
        "hard",
        r"The polynomial $p(x) = 2x^3 + bx^2 - 5x + 6$ is divisible by"
        r" $x - 2$, where $b$ is a constant. What is the value of $b$?",
        r"Divisibility by $x - 2$ means $p(2) = 0$:"
        r" $$2(8) + b(4) - 5(2) + 6 = 16 + 4b - 10 + 6 = 4b + 12 = 0.$$"
        r" So"
        r" $$4b = -12 \;\Rightarrow\; b = -3.$$"
        r" Checking, $p(x) = 2x^3 - 3x^2 - 5x + 6$ gives"
        r" $16 - 12 - 10 + 6 = 0$. Substituting $x = -2$ instead of"
        r" $x = 2$ leads to a different equation and the value 3."
        r" The correct answer is **B**.",
        ["Eq(2*2**3 + (-3)*2**2 - 5*2 + 6, 0)", "Eq(16 - 10 + 6, 12)"],
        -3, {-6: "solved $4b = -24$", 3: "substituted $x = -2$",
             12: "stopped at $4b = -12$ and dropped the sign"}))

    # Q14 H psda — margin of error
    assert 54 - 4 == 50 and 54 + 4 == 58
    qs.append(mcq_listed(
        "SAT-P11-M2H-Q14", M, 14, "psda", "sample_stats_margin_error",
        "hard",
        r"In a random sample of 200 voters, $54\%$ said they support a"
        r" proposed measure. The margin of error for this estimate is 4"
        r" percentage points. Which of the following is the most"
        r" appropriate conclusion?",
        {"A": r"It is plausible that between $50\%$ and $58\%$ of all"
              r" voters support the measure.",
         "B": r"Exactly $54\%$ of all voters support the measure.",
         "C": r"At least $58\%$ of all voters support the measure.",
         "D": r"The sample says nothing about voters outside the 200"
              r" surveyed."},
        "A",
        r"A margin of error describes an INTERVAL of plausible values for"
        r" the population percentage, centred on the sample estimate:"
        r" $$54 - 4 = 50, \qquad 54 + 4 = 58.$$"
        r" So the data support the claim that the true percentage"
        r" plausibly lies between $50\%$ and $58\%$. Choice B claims"
        r" certainty a sample can never give; choice C reports the top of"
        r" the interval as a floor; and choice D denies the whole point of"
        r" random sampling, which is exactly what licenses generalising"
        r" beyond the 200 people surveyed."
        r" The correct answer is **A**.",
        ["Eq(54 - 4, 50)", "Eq(54 + 4, 58)", "200 > 0"]))

    # Q15 H alg SPR
    assert 2 * (8 + 16) == 48 and 8 * 16 == 128
    qs.append(spr(
        "SAT-P11-M2H-Q15", M, 15, "algebra", "area_perimeter_algebra",
        "hard",
        r"The perimeter of a rectangle is 48, and its length is twice its"
        r" width. What is the area of the rectangle?",
        ["128"],
        r"Let $w$ be the width, so the length is $2w$. The perimeter"
        r" gives"
        r" $$2(w + 2w) = 48 \;\Rightarrow\; 6w = 48 \;\Rightarrow\; w = 8.$$"
        r" The length is $2(8) = 16$, and the area is"
        r" $$8 \times 16 = 128.$$"
        r" (Check the perimeter: $2(8 + 16) = 48$.)",
        ["Eq(6*8, 48)", "Eq(2*(8 + 16), 48)", "Eq(8*16, 128)"]))

    # Q16 H adv — composition with a parameter
    assert (1 + 2) ** 2 + 2 == 11
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q16", M, 16, "advanced_math", "function_composition",
        "hard",
        r"The function $g$ is defined by $g(x) = x^2 + c$, where $c$ is a"
        r" positive constant. If $g(g(1)) = 11$, what is the value of"
        r" $c$?",
        r"Work outward one layer at a time. First,"
        r" $$g(1) = 1 + c.$$"
        r" Then"
        r" $$g(g(1)) = (1 + c)^2 + c = 11.$$"
        r" Expand and collect:"
        r" $$1 + 2c + c^2 + c = 11 \;\Rightarrow\; c^2 + 3c - 10 = 0.$$"
        r" Factoring gives $(c + 5)(c - 2) = 0$, so $c = -5$ or $c = 2$."
        r" Since $c$ is positive,"
        r" $$c = 2.$$"
        r" Checking: $g(1) = 3$ and $g(3) = 9 + 2 = 11$."
        r" The correct answer is **C**.",
        ["Eq((1 + 2)**2 + 2, 11)",
         "Eq(expand((1 + x)**2 + x - 11), x**2 + 3*x - 10)",
         "Eq(expand((x + 5)*(x - 2)), x**2 + 3*x - 10)"],
        2, {-5: "kept the negative root",
            1: "stopped at the inner input",
            3: "reported $g(1)$ instead of $c$"}))

    # Q17 H geo — cone height from volume
    assert Rational(1, 3) * 6**2 * 9 == 108
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q17", M, 17, "geometry_trig", "solids_volume_surface",
        "hard",
        r"A right circular cone has a radius of 6 and a volume of"
        r" $108\pi$. What is the height of the cone?",
        r"The volume of a cone is $V = \frac{1}{3}\pi r^2 h$. Substitute"
        r" the known values:"
        r" $$\frac{1}{3}\pi(6)^2 h = 108\pi \;\Rightarrow\; 12h = 108"
        r" \;\Rightarrow\; h = 9.$$"
        r" Dropping the factor $\frac{1}{3}$ turns the equation into"
        r" $36h = 108$ and gives 3, and using $r$ where $r^2$ belongs"
        r" gives 54."
        r" The correct answer is **B**.",
        ["Eq(Rational(1,3)*6**2*9, 108)", "Eq(Rational(1,3)*36, 12)",
         "Eq(Rational(108, 12), 9)"],
        9, {3: "omitted the factor of one third",
            27: "used $2r$ in place of $r^2$",
            54: "used $r$ in place of $r^2$"}))

    # Q18 H alg — mixture
    assert (Rational(2, 10) * 10 + Rational(5, 10) * 20
            == Rational(4, 10) * 30)
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q18", M, 18, "algebra", "linear_word_problems", "hard",
        r"A chemist combines a $20\%$ acid solution with a $50\%$ acid"
        r" solution to make 30 litres of a $40\%$ acid solution. How many"
        r" litres of the $20\%$ solution are used?",
        r"Let $x$ be the litres of $20\%$ solution; the rest,"
        r" $30 - x$ litres, is the $50\%$ solution. Count the ACID, not"
        r" the liquid:"
        r" $$0.20x + 0.50(30 - x) = 0.40(30) = 12.$$"
        r" Expand and solve:"
        r" $$0.20x + 15 - 0.50x = 12 \;\Rightarrow\; -0.30x = -3"
        r" \;\Rightarrow\; x = 10.$$"
        r" So 10 litres of the $20\%$ solution and 20 litres of the"
        r" $50\%$ solution are combined. Splitting the mixture evenly"
        r" would give a $35\%$ solution, not $40\%$."
        r" The correct answer is **A**.",
        ["Eq(Rational(2,10)*10 + Rational(5,10)*20, 12)",
         "Eq(Rational(4,10)*30, 12)", "Eq(10 + 20, 30)"],
        10, {12: "used the litres of acid as the volume",
             15: "split the 30 litres evenly",
             20: "gave the volume of the $50\\%$ solution"}))

    # Q19 H adv SPR — geometric sequence
    assert 5 * 3**3 == 135
    qs.append(spr(
        "SAT-P11-M2H-Q19", M, 19, "advanced_math", "sequences", "hard",
        r"The first term of a geometric sequence is 5, and the fourth"
        r" term is 135. What is the common ratio of the sequence?",
        ["3"],
        r"In a geometric sequence each term is the previous one times the"
        r" common ratio $r$, so the fourth term is the first times $r^3$"
        r" (three steps, not four):"
        r" $$5r^3 = 135 \;\Rightarrow\; r^3 = 27 \;\Rightarrow\; r = 3.$$"
        r" The sequence is $5,\ 15,\ 45,\ 135$, which confirms both the"
        r" ratio and the count of steps.",
        ["Eq(5*3**3, 135)", "Eq(Rational(135, 5), 27)",
         "Eq(5*3, 15)", "Eq(15*3, 45)"]))

    # Q20 H psda — same mean, different spread
    assert sum([10, 20, 30, 40, 50]) == sum([28, 29, 30, 31, 32]) == 150
    qs.append(mcq_listed(
        "SAT-P11-M2H-Q20", M, 20, "psda", "center_spread", "hard",
        r"Data set A consists of the values $10,\ 20,\ 30,\ 40,\ 50$, and"
        r" data set B consists of the values"
        r" $28,\ 29,\ 30,\ 31,\ 32$. Which of the following statements is"
        r" true?",
        {"A": r"The two data sets have the same mean, and data set A has"
              r" the greater standard deviation.",
         "B": r"The two data sets have the same mean, and data set B has"
              r" the greater standard deviation.",
         "C": r"Data set A has the greater mean, and the two data sets"
              r" have equal standard deviations.",
         "D": r"The two data sets have the same mean and the same"
              r" standard deviation."},
        "A",
        r"Both sets total 150 across 5 values, so both have mean"
        r" $$\frac{150}{5} = 30.$$"
        r" Standard deviation measures how far the values sit from that"
        r" shared mean. In set A the distances are $20, 10, 0, 10, 20$;"
        r" in set B they are only $2, 1, 0, 1, 2$. Set A is spread ten"
        r" times as far, so it has the greater standard deviation — the"
        r" means being equal says nothing about spread."
        r" The correct answer is **A**.",
        ["Eq(10 + 20 + 30 + 40 + 50, 150)",
         "Eq(28 + 29 + 30 + 31 + 32, 150)", "Eq(Rational(150, 5), 30)",
         "20 > 2"]))

    # Q21 H adv — rational exponent equation
    assert 27 ** Rational(2, 3) == 9
    qs.append(mcq_numeric(
        "SAT-P11-M2H-Q21", M, 21, "advanced_math", "exponent_equations",
        "hard",
        r"If $x^{\frac{2}{3}} = 9$ and $x > 0$, what is the value of $x$?",
        r"Undo a fractional exponent by raising both sides to its"
        r" reciprocal:"
        r" $$\left(x^{2/3}\right)^{3/2} = 9^{3/2}"
        r" \;\Rightarrow\; x = \left(\sqrt{9}\right)^3 = 3^3 = 27.$$"
        r" Checking: $27^{2/3} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9$."
        r" Taking the cube root of 9 gives roughly 2.08 and cubing 9"
        r" gives 729 — both apply the exponent in the wrong direction."
        r" The correct answer is **C**.",
        ["Eq(27**Rational(2,3), 9)", "Eq(9**Rational(3,2), 27)"],
        27, {3: "took the square root of 9",
             9: "restated the given value",
             729: "cubed 9 instead of using the reciprocal exponent"}))

    # Q22 H alg SPR — unit conversion
    assert Rational(60 * 5280, 3600) == 88
    qs.append(spr(
        "SAT-P11-M2H-Q22", M, 22, "algebra", "unit_conversion", "hard",
        r"A car travels at a constant speed of 60 miles per hour. What is"
        r" this speed in feet per second? (1 mile = 5,280 feet and"
        r" 1 hour = 3,600 seconds.)",
        ["88"],
        r"Convert both units in one chain, cancelling as you go:"
        r" $$\frac{60 \text{ mi}}{1 \text{ h}}"
        r" \times \frac{5280 \text{ ft}}{1 \text{ mi}}"
        r" \times \frac{1 \text{ h}}{3600 \text{ s}}"
        r" = \frac{60 \times 5280}{3600} \text{ ft/s}.$$"
        r" Evaluating,"
        r" $$\frac{316800}{3600} = 88 \text{ ft/s}.$$"
        r" Miles cancel against miles and hours against hours, which is"
        r" the check that the conversion factors were placed the right"
        r" way up.",
        ["Eq(60*5280, 316800)", "Eq(Rational(316800, 3600), 88)"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-11.json",
               {"testId": "sat-practice-11",
                "label": "SAT Math Practice Test 11",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
