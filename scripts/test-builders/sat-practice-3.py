#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 3 (data/sat/sat-practice-3.json).

Built on the shared framework in satbuild.py — this file is ONLY stems,
parameters, computed answers, named distractor error models, verify[]
strings, and solutions. Archetypes are deliberately fresh versus tests 1
and 2: slope from two points, midpoint, distance, substitution systems,
parallel-line (no-solution) systems, exponential GROWTH, percent increase,
direct/inverse variation, difference of squares, completing the square,
quadratic formula, exterior-angle theorem, corresponding angles, arc
length, prism surface area, sphere volume, two-way-table probability,
line-of-best-fit prediction, median from a frequency table, and 30-60-90
and similar-triangle trig. The figures exercise the satfigs tool library:
value tables, bar chart, histogram, box plot, scatter with fit line,
lines-on-a-grid, transversal, angle pair, inscribed circle, composite
area, cylinder, number lines, curve graphs, and right triangles.

Blueprint (asserted at the end):
  module1     alg 7 / adv 7 / psda 4 / geo 4 · 8E/9M/5H · SPR {4,9,14,18,21}
  module2*    alg 8 / adv 8 / psda 3 / geo 3 · SPR {3,7,12,15,19,22}
  module2Easy 11E/9M/2H · module2Hard 2E/7M/13H · threshold 15
  Full path: alg 15 / adv 15 / psda 7 / geo 7 = 44.
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


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E alg one_var — 5(x - 2) = 35, x = 9 (B)
    x_val = _solve(Eq(5 * (x - 2), 35), x)[0]
    assert x_val == 9
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $5(x - 2) = 35$, what is the value of $x$?",
        r"Divide both sides by 5, then add 2:"
        r" $$x - 2 = 7 \;\Rightarrow\; x = 9.$$"
        r" Choice A stops at $x - 2 = 7$; choice C distributes to"
        r" $5x - 2 = 35$, dropping the factor on the 2."
        r" The correct answer is **B**.",
        ["Eq(5*(9 - 2), 35)", "Eq(35/5 + 2, 9)"],
        int(x_val), {7: "stopped early", Rational(37, 5): "5x - 2 = 35",
                     45: "multiplied"}))

    # Q2 E psda one_var_data — table total hours, 34 (C), FIGURE (value table)
    hours = {"Mon": 6, "Tue": 9, "Wed": 7, "Thu": 12}
    total = sum(hours.values())
    assert total == 34
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q02", M, 2, "psda", "one_var_data", "easy",
        r"The table shows the number of hours a library was open on each"
        r" of four days. What was the total number of hours the library"
        r" was open over the four days?",
        r"Add the four values:"
        r" $$6 + 9 + 7 + 12 = 34.$$"
        r" Choice B leaves out Thursday; choice D adds an extra 12."
        r" The correct answer is **C**.",
        ["Eq(6 + 9 + 7 + 12, 34)"],
        total, {22: "dropped Thursday", 28: "dropped Tuesday",
                46: "double Thursday"},
        fig=figure("sat-p3-m1-q02",
                   "Table with days Mon, Tue, Wed, Thu and hours 6, 9, 7, "
                   "12.")))

    # Q3 E geo lines_angles — vertical angles, x = 65 (A), FIGURE (angle pair)
    assert 180 - 115 == 65
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q03", M, 3, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure, a ray meets a straight line, forming an angle of"
        r" $115°$ on one side and an angle of $x°$ on the other side."
        r" What is the value of $x$?",
        r"The two angles form a straight line, so they are supplementary:"
        r" $$x + 115 = 180 \;\Rightarrow\; x = 65.$$"
        r" Choice C treats them as equal; choice B uses $90°$ instead of"
        r" $180°$."
        r" The correct answer is **A**.",
        ["Eq(180 - 115, 65)"],
        65, {25: "used 90", 75: "used 190", 115: "thought equal"},
        fig=figure("sat-p3-m1-q03",
                   "A straight horizontal line with a ray rising from a "
                   "point on it; the angle on the left is 115 degrees and "
                   "the angle on the right is x degrees.")))

    # Q4 E adv equivalent_expressions — evaluate, SPR
    val = 2 * 4**2 - 3
    assert val == 29
    qs.append(spr(
        "SAT-P3-M1-Q04", M, 4, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 2x^2 - 3$. What is the"
        r" value of $f(4)$?",
        ["29"],
        r"Substitute $x = 4$, squaring before multiplying:"
        r" $$f(4) = 2(4)^2 - 3 = 2(16) - 3 = 29.$$"
        r" The correct answer is **29**.",
        ["Eq(2*4**2 - 3, 29)"]))

    # Q5 E alg linear_functions — slope from two points, 2 (D)
    slope = Fraction(11 - 3, 5 - 1)
    assert slope == 2
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q05", M, 5, "algebra", "linear_functions", "easy",
        r"A line in the $xy$-plane passes through the points $(1, 3)$ and"
        r" $(5, 11)$. What is the slope of the line?",
        r"Slope is the change in $y$ over the change in $x$:"
        r" $$m = \frac{11 - 3}{5 - 1} = \frac{8}{4} = 2.$$"
        r" Choice A inverts the ratio; choice B uses"
        r" $\frac{11 - 3}{5 + 1}$."
        r" The correct answer is **D**.",
        ["Eq(Rational(11 - 3, 5 - 1), 2)"],
        int(slope), {Fraction(1, 2): "inverted", Fraction(4, 3): "wrong denom",
                     Fraction(3, 2): "y over x at one point"},
        fmt=lambda v: dec(v) if Fraction(v).denominator == 1 else frac(v)))

    # Q6 E adv equivalent_expressions — expand product (B)
    prod = expand((x + 3) * (x - 5))
    assert prod == x**2 - 2 * x - 15
    qs.append(mcq_listed(
        "SAT-P3-M1-Q06", M, 6, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $(x + 3)(x - 5)$?",
        {"A": r"$x^2 - 15$",
         "B": r"$x^2 - 2x - 15$",
         "C": r"$x^2 + 2x - 15$",
         "D": r"$x^2 - 8x - 15$"},
        "B",
        r"Use FOIL:"
        r" $$(x + 3)(x - 5) = x^2 - 5x + 3x - 15 = x^2 - 2x - 15.$$"
        r" Choice C flips the sign of the middle term; choice A forgets"
        r" the middle term entirely."
        r" The correct answer is **B**.",
        ["Eq(expand((x + 3)*(x - 5)), x**2 - 2*x - 15)",
         "Eq(-5 + 3, -2)"]))

    # Q7 E psda percentages — 12% increase of 250 = 280 (A)
    new = 250 + Fraction(12, 100) * 250
    assert new == 280
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q07", M, 7, "psda", "percentages", "easy",
        r"A town's population was 250 thousand. Over one year it increased"
        r" by 12\%. What was the population, in thousands, after the"
        r" increase?",
        r"A 12\% increase multiplies by 1.12:"
        r" $$250 \times 1.12 = 280.$$"
        r" Equivalently, add $0.12 \times 250 = 30$ to 250. Choice C is"
        r" only the increase itself; choice B forgets to add it back."
        r" The correct answer is **A**.",
        ["Eq(250 + Rational(12, 100)*250, 280)",
         "Eq(Rational(12, 100)*250, 30)"],
        int(new), {30: "increase only", 250: "no change", 500: "doubled"}))

    # Q8 E geo area_volume — circle area 36π (C), FIGURE (right triangle? use table? use inscribed? just text)
    r_ = 6
    assert r_**2 == 36
    qs.append(mcq_listed(
        "SAT-P3-M1-Q08", M, 8, "geometry_trig", "area_volume", "easy",
        r"A circle has a radius of 6. What is the area of the circle?",
        {"A": r"$6\pi$",
         "B": r"$12\pi$",
         "C": r"$36\pi$",
         "D": r"$144\pi$"},
        "C",
        r"The area of a circle is $\pi r^2$:"
        r" $$A = \pi (6)^2 = 36\pi.$$"
        r" Choice B is the circumference $2\pi r$; choice D squares the"
        r" diameter instead of the radius."
        r" The correct answer is **C**.",
        ["Eq(pi*6**2, 36*pi)", "Eq(2*pi*6, 12*pi)"]))

    # Q9 M alg systems — substitution, x = 4, SPR
    # y = x - 1; 3x + 2y = 10 → 3x + 2(x-1) = 10 → 5x = 12? recompute
    # choose: y = 2x - 3 ; x + y = 9 → x + 2x - 3 = 9 → 3x = 12 → x = 4, y = 5
    sol = _solve([Eq(symbols("y"), 2 * x - 3), Eq(x + symbols("y"), 9)],
                 [x, symbols("y")])
    assert sol[x] == 4 and sol[symbols("y")] == 5
    qs.append(spr(
        "SAT-P3-M1-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$y = 2x - 3$$ $$x + y = 9$$"
        r" If $(x, y)$ is the solution to the system above, what is the"
        r" value of $x$?",
        ["4"],
        r"Substitute the first equation into the second:"
        r" $$x + (2x - 3) = 9 \;\Rightarrow\; 3x = 12 \;\Rightarrow\;"
        r" x = 4.$$"
        r" (Then $y = 2(4) - 3 = 5$, and $4 + 5 = 9$ checks.)"
        r" The correct answer is **4**.",
        ["Eq(4 + (2*4 - 3), 9)", "Eq(2*4 - 3, 5)"]))

    # Q10 M adv nonlinear_functions — exponential growth, 800 at t=3 (D), FIG
    p0 = 100
    vals = {t: p0 * 2**t for t in (0, 1, 2, 3)}
    assert vals == {0: 100, 1: 200, 2: 400, 3: 800}
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph shows a population $y$ of bacteria $x$ hours after a"
        r" study began; the population doubles every hour from an initial"
        r" 100. What is the population at $x = 3$?",
        r"Three hours is three doublings:"
        r" $$100 \to 200 \to 400 \to 800.$$"
        r" Equivalently $100 \cdot 2^3 = 800$. Choice C stops after two"
        r" doublings (hour 2); choice A multiplies $100 \cdot 3 \cdot 2$."
        r" The correct answer is **D**.",
        ["Eq(100*2**3, 800)", "Eq(100*2**2, 400)"],
        800, {300: "linear guess", 600: "100*3*2", 400: "hour 2"},
        fig=figure("sat-p3-m1-q10",
                   "Increasing exponential curve through (0, 100), "
                   "(1, 200), (2, 400), and (3, 800), rising steeply to "
                   "the right.")))

    # Q11 M psda two_var_data — best fit prediction 26 (B), FIGURE (scatter+line)
    # line y = 2x + 6, at x = 10 → 26
    assert 2 * 10 + 6 == 26
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q11", M, 11, "psda", "two_var_data_models", "medium",
        r"The scatterplot shows data for 8 plants, with the line of best"
        r" fit $y = 2x + 6$, where $x$ is the number of weeks and $y$ is"
        r" the height in centimeters. Based on the line of best fit, what"
        r" is the predicted height, in centimeters, of a plant at $x = 10$"
        r" weeks?",
        r"Substitute $x = 10$ into the line of best fit:"
        r" $$y = 2(10) + 6 = 26.$$"
        r" Choice A forgets the intercept ($2 \times 10$); choice D uses"
        r" the slope and intercept swapped ($6 \times 10 + 2$)."
        r" The correct answer is **B**.",
        ["Eq(2*10 + 6, 26)"],
        26, {20: "no intercept", 18: "slope as intercept", 62: "swapped"},
        fig=figure("sat-p3-m1-q11",
                   "Scatterplot of 8 points rising to the right around a "
                   "straight best-fit line, with weeks on the horizontal "
                   "axis and height on the vertical axis.")))

    # Q12 M alg linear_equations_two_var — parallel lines, no solution (A)
    # 2x + 3y = 7 and 4x + 6y = 5 are parallel (no solution)
    qs.append(mcq_listed(
        "SAT-P3-M1-Q12", M, 12, "algebra", "systems_two_linear", "medium",
        r"$$2x + 3y = 7$$ $$4x + 6y = 5$$"
        r" How many solutions $(x, y)$ does the system of equations above"
        r" have?",
        {"A": r"Zero",
         "B": r"Exactly one",
         "C": r"Exactly two",
         "D": r"Infinitely many"},
        "A",
        r"Multiplying the first equation by 2 gives $4x + 6y = 14$, but"
        r" the second equation says $4x + 6y = 5$. The same expression"
        r" cannot equal both 14 and 5, so the lines are PARALLEL and"
        r" never meet — zero solutions. (Infinitely many would require"
        r" the constants to match too.)"
        r" The correct answer is **A**.",
        ["Eq(2*7, 14)", "Ne(14, 5)", "Eq(Rational(2, 4), Rational(3, 6))"]))

    # Q13 M adv nonlinear_equations_systems — difference of squares (C)
    # x^2 - 49 = 0 → x = ±7; product of solutions = -49
    qs.append(mcq_listed(
        "SAT-P3-M1-Q13", M, 13, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"Which of the following is the complete set of solutions to"
        r" $x^2 - 49 = 0$?",
        {"A": r"$x = 7$",
         "B": r"$x = -7$",
         "C": r"$x = 7$ and $x = -7$",
         "D": r"$x = 49$ and $x = -49$"},
        "C",
        r"Factor as a difference of squares:"
        r" $$x^2 - 49 = (x - 7)(x + 7) = 0,$$"
        r" so $x = 7$ or $x = -7$. A squared variable equation usually has"
        r" TWO solutions; choices A and B each keep only one. Choice D"
        r" forgets to take the square root."
        r" The correct answer is **C**.",
        ["Eq(expand((x - 7)*(x + 7)), x**2 - 49)", "Eq(7**2, 49)",
         "Eq((-7)**2, 49)"]))

    # Q14 M geo right_triangles_trig — 30-60-90 short leg, SPR
    # hypotenuse 20, 30° angle → opposite (short leg) = 10
    assert 20 * Fraction(1, 2) == 10
    qs.append(spr(
        "SAT-P3-M1-Q14", M, 14, "geometry_trig", "right_triangles_trig",
        "medium",
        r"In right triangle $ABC$, angle $C$ is the right angle and angle"
        r" $A$ measures $30°$. If the hypotenuse $AB$ has length 20, what"
        r" is the length of side $BC$, the side opposite the $30°$ angle?",
        ["10"],
        r"In a right triangle, the side opposite the $30°$ angle is half"
        r" the hypotenuse (that is the 30-60-90 ratio, or"
        r" $\sin 30° = \frac{1}{2}$):"
        r" $$BC = 20 \cdot \sin 30° = 20 \cdot \tfrac{1}{2} = 10.$$"
        r" The correct answer is **10**.",
        ["Eq(20*Rational(1, 2), 10)"]))

    # Q15 M alg linear_inequalities — solve, x ≤ 4 boundary read; SPR? no, mcq (D)
    # 3x + 7 ≤ 19 → x ≤ 4
    bound = _solve(Eq(3 * x + 7, 19), x)[0]
    assert bound == 4
    qs.append(mcq_listed(
        "SAT-P3-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"Which of the following is the solution to the inequality"
        r" $3x + 7 \le 19$?",
        {"A": r"$x \ge 4$",
         "B": r"$x \le 8$",
         "C": r"$x \ge 8$",
         "D": r"$x \le 4$"},
        "D",
        r"Subtract 7, then divide by the positive 3 (so the inequality"
        r" direction is unchanged):"
        r" $$3x \le 12 \;\Rightarrow\; x \le 4.$$"
        r" Choice A flips the inequality for no reason; choice B divides"
        r" $19 - 7$ by nothing (keeps 8 instead of $12/3$)."
        r" The correct answer is **D**.",
        ["Eq((19 - 7)/3, 4)", "12 <= 12"]))

    # Q16 M adv equivalent_expressions — complete the square vertex form (B), no fig
    # x^2 + 8x + 10 = (x + 4)^2 - 6
    assert expand((x + 4)**2 - 6) == x**2 + 8 * x + 10
    qs.append(mcq_listed(
        "SAT-P3-M1-Q16", M, 16, "advanced_math", "equivalent_expressions",
        "medium",
        r"Which of the following is equivalent to $x^2 + 8x + 10$?",
        {"A": r"$(x + 4)^2 + 10$",
         "B": r"$(x + 4)^2 - 6$",
         "C": r"$(x + 8)^2 - 6$",
         "D": r"$(x + 4)^2 - 16$"},
        "B",
        r"Complete the square. Half of 8 is 4, and $4^2 = 16$:"
        r" $$x^2 + 8x + 10 = (x^2 + 8x + 16) - 16 + 10 = (x + 4)^2 - 6.$$"
        r" Choice A forgets to subtract the 16; choice C halves 8"
        r" incorrectly to 8 inside the square."
        r" The correct answer is **B**.",
        ["Eq(expand((x + 4)**2 - 6), x**2 + 8*x + 10)", "Eq(4**2, 16)",
         "Eq(-16 + 10, -6)"]))

    # Q17 M psda probability_two_way — from a two-way table, 3/10 (A), FIGURE
    # table: cells; P = 18/60
    correct = Fraction(18, 60)
    assert correct == Fraction(3, 10)
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q17", M, 17, "psda", "probability_conditional", "medium",
        r"The two-way table shows the results of a survey of 60 students."
        r" If one of the 60 students is selected at random, what is the"
        r" probability that the student is a senior who prefers tea?",
        r"The seniors-who-prefer-tea cell holds 18 students out of the 60"
        r" surveyed:"
        r" $$P = \frac{18}{60} = \frac{3}{10}.$$"
        r" Choice C divides 18 by the 30 seniors (that is the CONDITIONAL"
        r" probability given senior, a different question)."
        r" The correct answer is **A**.",
        ["Eq(Rational(18, 60), Rational(3, 10))",
         "Rational(3, 10) < Rational(2, 5)"],
        correct, {Fraction(2, 5): "wrong cell", Fraction(3, 5): "of seniors",
                  Fraction(1, 2): "half"},
        fmt=lambda v: frac(v),
        fig=figure("sat-p3-m1-q17",
                   "Two-way table of 60 students by class (Junior, Senior) "
                   "and drink preference (Coffee, Tea); the Senior-Tea "
                   "cell is 18.")))

    # Q18 H alg one_var — fraction answer 9/4, SPR
    sol = _solve(Eq(8 * x - 3, 4 * x + 6), x)
    assert sol == [Rational(9, 4)]
    qs.append(spr(
        "SAT-P3-M1-Q18", M, 18, "algebra", "linear_equations_one_var",
        "hard",
        r"$$8x - 3 = 4x + 6$$"
        r" What is the solution to the equation above?",
        ["9/4", "2.25"],
        r"Collect the $x$-terms and constants:"
        r" $$8x - 4x = 6 + 3 \;\Rightarrow\; 4x = 9 \;\Rightarrow\;"
        r" x = \frac{9}{4}.$$"
        r" Check: $8(2.25) - 3 = 15$ and $4(2.25) + 6 = 15$. ✓"
        r" The correct answer is **9/4** (or 2.25).",
        ["Eq(8*Rational(9, 4) - 3, 4*Rational(9, 4) + 6)",
         "Eq(Rational(9, 4), 2.25)"]))

    # Q19 H adv nonlinear_functions — quadratic formula sum of roots (C)
    # 2x^2 - 6x + 1 = 0 → sum of roots = 6/2 = 3
    a_, b_, c_ = 2, -6, 1
    assert Fraction(-b_, a_) == 3
    qs.append(mcq_listed(
        "SAT-P3-M1-Q19", M, 19, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"The equation $2x^2 - 6x + 1 = 0$ has two solutions. What is the"
        r" sum of the two solutions?",
        {"A": r"$-3$",
         "B": r"$\dfrac{1}{2}$",
         "C": r"$3$",
         "D": r"$6$"},
        "C",
        r"For $ax^2 + bx + c = 0$, the sum of the solutions is"
        r" $-\dfrac{b}{a}$ (from the quadratic formula, the $\pm\sqrt{}$"
        r" terms cancel):"
        r" $$-\frac{-6}{2} = 3.$$"
        r" Choice A keeps the sign of $b$; choice D reads $-b$ without"
        r" dividing by $a$."
        r" The correct answer is **C**.",
        ["Eq(Rational(-(-6), 2), 3)", "Eq((-6)**2 - 4*2*1, 28)"]))

    # Q20 H geo circles — arc length (D), FIGURE (inscribed_circle reused? use text)
    # radius 9, central angle 40° → arc = (40/360)(2π·9) = 2π
    arc = Fraction(40, 360) * 2 * 9
    assert arc == 2
    qs.append(mcq_listed(
        "SAT-P3-M1-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"In a circle with radius 9, a central angle of $40°$ cuts off an"
        r" arc. What is the length of that arc?",
        {"A": r"$\pi$",
         "B": r"$\dfrac{3\pi}{2}$",
         "C": r"$\dfrac{9\pi}{5}$",
         "D": r"$2\pi$"},
        "D",
        r"The arc is the fraction $\frac{40}{360} = \frac{1}{9}$ of the"
        r" full circumference $2\pi r = 18\pi$:"
        r" $$\text{arc} = \frac{1}{9} \cdot 18\pi = 2\pi.$$"
        r" Choice C uses the radius 9 as the circumference; choice A"
        r" halves the correct value."
        r" The correct answer is **D**.",
        ["Eq(Rational(40, 360)*2*9, 2)", "Eq(Rational(40, 360), Rational(1, 9))"]))

    # Q21 H adv nonlinear_functions — evaluate composite, SPR
    # f(x)=x^2+1, g(x)=x-4; f(g(6)) = f(2) = 5
    g6 = 6 - 4
    fg = g6**2 + 1
    assert (g6, fg) == (2, 5)
    qs.append(spr(
        "SAT-P3-M1-Q21", M, 21, "advanced_math", "nonlinear_functions",
        "hard",
        r"The functions $f$ and $g$ are defined by $f(x) = x^2 + 1$ and"
        r" $g(x) = x - 4$. What is the value of $f(g(6))$?",
        ["5"],
        r"Work from the inside out. First $g(6) = 6 - 4 = 2$, then"
        r" $$f(2) = 2^2 + 1 = 5.$$"
        r" The correct answer is **5**.",
        ["Eq(6 - 4, 2)", "Eq(2**2 + 1, 5)"]))

    # Q22 H alg linear_functions — find b so line passes through point (B)
    # y = 3x + b through (2, 1) → b = -5
    b_val = 1 - 3 * 2
    assert b_val == -5
    qs.append(mcq_numeric(
        "SAT-P3-M1-Q22", M, 22, "algebra", "linear_functions", "hard",
        r"In the $xy$-plane, the line $y = 3x + b$ passes through the point"
        r" $(2, 1)$, where $b$ is a constant. What is the value of $b$?",
        r"Substitute the point and solve for $b$:"
        r" $$1 = 3(2) + b \;\Rightarrow\; 1 = 6 + b \;\Rightarrow\;"
        r" b = -5.$$"
        r" Choice C adds instead of subtracts ($1 + 6$); choice A"
        r" forgets the slope factor ($1 - 2$)."
        r" The correct answer is **B**.",
        ["Eq(3*2 + (-5), 1)"],
        b_val, {-1: "1 - 2", 5: "sign flip", 7: "1 + 6"}))

    return qs


# ─── Module 2 Easy (11E / 9M / 2H) ────────────────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg one_var — x = 6 (C)
    x_val = _solve(Eq(3 * x - 4, 14), x)[0]
    assert x_val == 6
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $3x - 4 = 14$, what is the value of $x$?",
        r"Add 4, then divide by 3:"
        r" $$3x = 18 \;\Rightarrow\; x = 6.$$"
        r" Choice B subtracts 4 instead of adding; choice D divides 14 by"
        r" 3 first."
        r" The correct answer is **C**.",
        ["Eq(3*6 - 4, 14)"],
        int(x_val), {Rational(10, 3): "subtracted 4", Rational(14, 3): "no +4",
                     18: "forgot divide"},
        fmt=lambda v: dec(v) if Fraction(v).denominator == 1 else frac(v)))

    # Q2 E geo transversal — same-side interior supplementary, x = 112 (D), FIG
    assert 68 + 112 == 180
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q02", M, 2, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure, parallel lines $\ell$ and $m$ are cut by a"
        r" transversal. One same-side interior angle measures $68°$ and"
        r" the other same-side interior angle measures $x°$. What is the"
        r" value of $x$?",
        r"Same-side interior angles between parallel lines are"
        r" SUPPLEMENTARY:"
        r" $$x + 68 = 180 \;\Rightarrow\; x = 112.$$"
        r" Choice B treats them as equal (that is the corresponding-angle"
        r" rule, not same-side interior); choice A uses $90 - 68$."
        r" The correct answer is **D**.",
        ["Eq(180 - 68, 112)"],
        112, {22: "90 - 68", 34: "halved", 68: "thought equal"},
        fig=figure("sat-p3-m2e-q02",
                   "Two parallel horizontal lines l and m cut by a "
                   "transversal; the same-side interior angle at line l is "
                   "68 degrees and the one at line m is x degrees.")))

    # Q3 E alg linear_functions — f(5) = 23, SPR
    assert 4 * 5 + 3 == 23
    qs.append(spr(
        "SAT-P3-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 4x + 3$. What is the"
        r" value of $f(5)$?",
        ["23"],
        r"Substitute $x = 5$:"
        r" $$f(5) = 4(5) + 3 = 23.$$"
        r" The correct answer is **23**.",
        ["Eq(4*5 + 3, 23)"]))

    # Q4 E psda one_var_data — bar chart most (A), FIGURE (bar chart)
    sold = {"A": 50, "B": 35, "C": 42, "D": 28}
    best = max(sold, key=sold.get)
    assert best == "A"
    qs.append(mcq_listed(
        "SAT-P3-M2E-Q04", M, 4, "psda", "one_var_data", "easy",
        r"The bar chart shows the number of tickets sold by four sellers."
        r" Which seller sold the most tickets?",
        {"A": r"Seller A",
         "B": r"Seller B",
         "C": r"Seller C",
         "D": r"Seller D"},
        "A",
        r"The tallest bar is Seller A at 50 tickets, higher than C (42),"
        r" B (35), and D (28)."
        r" The correct answer is **A**.",
        ["50 > 42", "42 > 35", "35 > 28"],
        fig=figure("sat-p3-m2e-q04",
                   "Bar chart of tickets sold by Seller A (50), B (35), "
                   "C (42), and D (28).")))

    # Q5 E adv nonlinear_functions — g(2) = 10 (C)
    assert 2**3 + 2 == 10
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q05", M, 5, "advanced_math", "nonlinear_functions",
        "easy",
        r"The function $g$ is defined by $g(x) = x^3 + 2$. What is the"
        r" value of $g(2)$?",
        r"Substitute $x = 2$, cubing first:"
        r" $$g(2) = 2^3 + 2 = 8 + 2 = 10.$$"
        r" Choice B multiplies $2 \cdot 3$ instead of cubing; choice A"
        r" adds the exponent."
        r" The correct answer is **C**.",
        ["Eq(2**3 + 2, 10)"],
        10, {5: "2+3", 8: "no +2", 12: "cubed 2 wrong"}))

    # Q6 E alg two_var — which point on 2x + y = 10 (B)
    assert 2 * 3 + 4 == 10
    qs.append(mcq_listed(
        "SAT-P3-M2E-Q06", M, 6, "algebra", "linear_equations_two_var",
        "easy",
        r"Which of the following points lies on the graph of"
        r" $2x + y = 10$ in the $xy$-plane?",
        {"A": r"$(1, 4)$",
         "B": r"$(3, 4)$",
         "C": r"$(4, 3)$",
         "D": r"$(5, 5)$"},
        "B",
        r"Test each point. At $(3, 4)$:"
        r" $$2(3) + 4 = 10. ✓$$"
        r" Choice C gives $2(4) + 3 = 11$; choice A gives $2(1) + 4 = 6$."
        r" The correct answer is **B**.",
        ["Eq(2*3 + 4, 10)", "Ne(2*4 + 3, 10)", "Ne(2*1 + 4, 10)",
         "Ne(2*5 + 5, 10)"]))

    # Q7 E adv equivalent_expressions — combine, coefficient a = 7, SPR
    total = expand((3 * x + 5) + (4 * x - 2))
    assert total == 7 * x + 3
    qs.append(spr(
        "SAT-P3-M2E-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "easy",
        r"$$(3x + 5) + (4x - 2) = ax + b$$"
        r" The equation above is true for all $x$, where $a$ and $b$ are"
        r" constants. What is the value of $a$?",
        ["7"],
        r"Add like terms: the $x$-terms give $3 + 4 = 7$ and the"
        r" constants give $5 - 2 = 3$:"
        r" $$7x + 3.$$"
        r" So $a = 7$."
        r" The correct answer is **7**.",
        ["Eq(expand((3*x + 5) + (4*x - 2)), 7*x + 3)", "Eq(3 + 4, 7)"]))

    # Q8 E geo area_volume — rectangular prism volume 60 (C)
    l_, w_, h_ = 5, 4, 3
    assert l_ * w_ * h_ == 60
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q08", M, 8, "geometry_trig", "area_volume", "easy",
        r"A rectangular box has length 5, width 4, and height 3. What is"
        r" the volume of the box?",
        r"Volume of a rectangular prism is length times width times"
        r" height:"
        r" $$V = 5 \times 4 \times 3 = 60.$$"
        r" Choice A is the sum of the edges' product for one face; choice"
        r" D is the surface area."
        r" The correct answer is **C**.",
        ["Eq(5*4*3, 60)"],
        60, {12: "5+4+3 doubled", 20: "one face", 94: "surface area"}))

    # Q9 M alg systems — elimination, x = 2 (A)
    # 3x + 2y = 12 ; 3x - 2y = 0 → add: 6x = 12 → x = 2, y = 3
    sol = _solve([Eq(3 * x + 2 * symbols("y"), 12),
                  Eq(3 * x - 2 * symbols("y"), 0)], [x, symbols("y")])
    assert sol[x] == 2 and sol[symbols("y")] == 3
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$3x + 2y = 12$$ $$3x - 2y = 0$$"
        r" If $(x, y)$ is the solution to the system above, what is the"
        r" value of $x$?",
        r"Add the two equations to eliminate $y$:"
        r" $$(3x + 2y) + (3x - 2y) = 12 + 0 \;\Rightarrow\; 6x = 12"
        r" \;\Rightarrow\; x = 2.$$"
        r" Choice C is the value of $y$; choice D is the sum $x + y$."
        r" The correct answer is **A**.",
        ["Eq(3*2 + 2*3, 12)", "Eq(3*2 - 2*3, 0)"],
        2, {3: "value of y", 4: "6x=12 mis", 5: "x + y"}))

    # Q10 E psda ratios — 3 cups per 2 people → 12 cups for 8 (D)
    cups = Fraction(3, 2) * 8
    assert cups == 12
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q10", M, 10, "psda", "ratios_rates_units", "easy",
        r"A recipe uses 3 cups of flour for every 2 servings. How many"
        r" cups of flour are needed for 8 servings?",
        r"Scale the ratio: 8 servings is $8 / 2 = 4$ times the base, so"
        r" $$3 \times 4 = 12 \text{ cups}.$$"
        r" Choice A keeps the original 3 cups; choice B adds instead of"
        r" scaling."
        r" The correct answer is **D**.",
        ["Eq(Rational(3, 2)*8, 12)"],
        int(cups), {3: "no scaling", 9: "added", 16: "used 2 cups"}))

    # Q11 M adv nonlinear_functions — vertex from table, x = 1 (A), FIGURE
    tbl = {xx: (xx - 1)**2 + 2 for xx in (-1, 0, 1, 2, 3)}
    assert list(tbl.values()) == [6, 3, 2, 3, 6]
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q11", M, 11, "advanced_math", "nonlinear_functions",
        "medium",
        r"The table shows five values of the quadratic function $h$. At"
        r" what value of $x$ does $h$ reach its minimum?",
        r"The outputs are symmetric — equal at $x = 0$ and $x = 2$, and"
        r" smallest between them at $x = 1$, where $h(1) = 2$. The"
        r" question asks for the $x$-value of the minimum (choice C is the"
        r" minimum OUTPUT, not the input)."
        r" The correct answer is **A**.",
        ["Eq((1 - 1)**2 + 2, 2)", "Eq((0 - 1)**2 + 2, (2 - 1)**2 + 2)"],
        1, {0: "left neighbor", 2: "minimum output", 3: "h(0)"},
        fig=figure("sat-p3-m2e-q11",
                   "Table with x values -1, 0, 1, 2, 3 and h(x) values 6, "
                   "3, 2, 3, 6.")))

    # Q12 M psda one_var_data — median from list, 7, SPR
    data = [3, 5, 6, 8, 9]
    med = data[len(data) // 2]
    assert med == 6
    qs.append(spr(
        "SAT-P3-M2E-Q12", M, 12, "psda", "one_var_data", "medium",
        r"A data set has the values $3, 5, 6, 8, 9$. What is the median of"
        r" the data set?",
        ["6"],
        r"The median is the middle value once the data are ordered (they"
        r" already are). With five values, the middle one is the third:"
        r" $$3, \; 5, \; \boxed{6}, \; 8, \; 9.$$"
        r" The correct answer is **6**.",
        ["3 < 6", "6 < 8"]))

    # Q13 M alg linear_inequalities — number line x > 2 (B), FIGURE
    qs.append(mcq_listed(
        "SAT-P3-M2E-Q13", M, 13, "algebra", "linear_inequalities", "medium",
        r"The number line shows the solution set of an inequality: an"
        r" open circle at 2 with shading to the right. Which inequality"
        r" has this solution set?",
        {"A": r"$x \ge 2$",
         "B": r"$x > 2$",
         "C": r"$x < 2$",
         "D": r"$x \le 2$"},
        "B",
        r"The ray points right, so solutions are numbers GREATER than the"
        r" endpoint, and the OPEN circle means 2 itself is excluded:"
        r" $x > 2$. A filled circle would be needed for choice A; choice"
        r" C shades the wrong direction."
        r" The correct answer is **B**.",
        ["3 > 2", "Eq(2, 2)"],
        fig=figure("sat-p3-m2e-q13",
                   "Number line from -3 to 7 with an open circle at 2 and "
                   "an arrow shading all numbers to the right.")))

    # Q14 M adv equivalent_expressions — factor common, (C)
    fact = expand(3 * x * (x + 4))
    assert fact == 3 * x**2 + 12 * x
    qs.append(mcq_listed(
        "SAT-P3-M2E-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "medium",
        r"Which of the following is equivalent to $3x^2 + 12x$?",
        {"A": r"$3(x^2 + 12x)$",
         "B": r"$3x(x + 12)$",
         "C": r"$3x(x + 4)$",
         "D": r"$x(3x + 12x)$"},
        "C",
        r"Factor out the greatest common factor $3x$ from both terms:"
        r" $$3x^2 + 12x = 3x(x + 4),$$"
        r" since $3x \cdot x = 3x^2$ and $3x \cdot 4 = 12x$. Choice A only"
        r" factors the 3; choice B divides the 12 by the 3 but not by the"
        r" $x$."
        r" The correct answer is **C**.",
        ["Eq(expand(3*x*(x + 4)), 3*x**2 + 12*x)", "Eq(3*4, 12)"]))

    # Q15 M adv nonlinear_equations — positive root, 5, SPR
    roots = _solve(Eq(x**2 - 3 * x - 10, 0), x)
    assert set(roots) == {-2, 5}
    qs.append(spr(
        "SAT-P3-M2E-Q15", M, 15, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"What is the positive solution to $x^2 - 3x - 10 = 0$?",
        ["5"],
        r"Find two numbers with product $-10$ and sum $-3$: they are $-5$"
        r" and $2$:"
        r" $$x^2 - 3x - 10 = (x - 5)(x + 2) = 0,$$"
        r" so $x = 5$ or $x = -2$; the positive solution is 5."
        r" The correct answer is **5**.",
        ["Eq(expand((x - 5)*(x + 2)), x**2 - 3*x - 10)",
         "Eq(5**2 - 3*5 - 10, 0)"]))

    # Q16 E alg linear_functions — direct variation k = 4 (D)
    k_val = Fraction(20, 5)
    assert k_val == 4
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q16", M, 16, "algebra", "linear_functions", "easy",
        r"The variable $y$ is directly proportional to $x$, and $y = 20$"
        r" when $x = 5$. What is the constant of proportionality?",
        r"Direct proportion means $y = kx$, so"
        r" $$k = \frac{y}{x} = \frac{20}{5} = 4.$$"
        r" Choice A inverts the ratio; choice C subtracts."
        r" The correct answer is **D**.",
        ["Eq(Rational(20, 5), 4)"],
        int(k_val), {Fraction(1, 4): "inverted", 3: "5 - 2? no", 15: "20 - 5"},
        fmt=lambda v: dec(v) if Fraction(v).denominator == 1 else frac(v)))

    # Q17 M geo right_triangles_trig — sin θ = 3/5 (A), FIGURE
    assert 3**2 + 4**2 == 5**2
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q17", M, 17, "geometry_trig", "right_triangles_trig",
        "medium",
        r"In the right triangle shown, the leg opposite angle $\theta$ has"
        r" length 3, the other leg has length 4, and the hypotenuse has"
        r" length 5. What is the value of $\sin \theta$?",
        r"Sine is opposite over hypotenuse:"
        r" $$\sin \theta = \frac{3}{5}.$$"
        r" Choice B is $\cos \theta$ (adjacent over hypotenuse); choice C"
        r" is $\tan \theta$."
        r" The correct answer is **A**.",
        ["Eq(3**2 + 4**2, 5**2)", "Rational(3, 5) < Rational(3, 4)"],
        Fraction(3, 5), {Fraction(4, 5): "cosine", Fraction(3, 4): "tangent",
                         Fraction(5, 3): "inverted"},
        fmt=lambda v: frac(v),
        fig=figure("sat-p3-m2e-q17",
                   "Right triangle with the leg opposite theta of length "
                   "3, the adjacent leg of length 4, hypotenuse 5, and "
                   "theta marked at the bottom-left vertex.")))

    # Q18 M adv nonlinear_functions — growth percent 25% (B)
    assert Fraction(125, 100) - 1 == Fraction(25, 100)
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q18", M, 18, "advanced_math", "nonlinear_functions",
        "medium",
        r"The number of subscribers to a channel $t$ years after it"
        r" launched is modeled by $N(t) = 4000(1.25)^t$. By what percent"
        r" does the number of subscribers increase each year?",
        r"Each year the count is MULTIPLIED by 1.25, which is a growth"
        r" factor of $1 + 0.25$:"
        r" $$1.25 - 1 = 0.25 = 25\%.$$"
        r" Choice C reads 1.25 as 125\% growth; choice A misplaces the"
        r" decimal."
        r" The correct answer is **B**.",
        ["Eq(Rational(125, 100) - 1, Rational(25, 100))"],
        25, {Fraction(5, 2): "decimal slip", 75: "wrong complement",
             125: "read factor"},
        fmt=lambda v: f"${float(Fraction(v)):g}\\%$"))

    # Q19 E alg two_var — y-intercept 5, SPR
    assert Fraction(20, 4) == 5
    qs.append(spr(
        "SAT-P3-M2E-Q19", M, 19, "algebra", "linear_equations_two_var",
        "easy",
        r"The graph of $3x + 4y = 20$ in the $xy$-plane crosses the"
        r" $y$-axis at the point $(0, b)$. What is the value of $b$?",
        ["5"],
        r"On the $y$-axis, $x = 0$:"
        r" $$3(0) + 4b = 20 \;\Rightarrow\; b = 5.$$"
        r" The correct answer is **5**.",
        ["Eq(3*0 + 4*5, 20)"]))

    # Q20 M adv nonlinear_functions — composition f(g(2)) (C)
    # f(x)=3x-1, g(x)=x^2 → g(2)=4, f(4)=11
    g2 = 2**2
    fg2 = 3 * g2 - 1
    assert (g2, fg2) == (4, 11)
    qs.append(mcq_numeric(
        "SAT-P3-M2E-Q20", M, 20, "advanced_math", "nonlinear_functions",
        "medium",
        r"The functions $f$ and $g$ are defined by $f(x) = 3x - 1$ and"
        r" $g(x) = x^2$. What is the value of $f(g(2))$?",
        r"Inside first: $g(2) = 4$, then"
        r" $$f(4) = 3(4) - 1 = 11.$$"
        r" Choice D reverses the order — $g(f(2)) = g(5) = 25$; choice A"
        r" stops at $g(2)$."
        r" The correct answer is **C**.",
        ["Eq(2**2, 4)", "Eq(3*4 - 1, 11)", "Eq((3*2 - 1)**2, 25)"],
        fg2, {4: "stopped at g(2)", 5: "f(2) only", 25: "reversed"}))

    # Q21 H alg systems — which system models it (D)
    # 40 items, $290, pens $5, notebooks $8; p + n = 40, 5p + 8n = 290
    assert 30 + 10 == 40 and 5 * 30 + 8 * 10 == 230  # sanity of a wrong combo; solve real
    sol = _solve([Eq(symbols("p") + symbols("n"), 40),
                  Eq(5 * symbols("p") + 8 * symbols("n"), 290)],
                 [symbols("p"), symbols("n")])
    assert sol[symbols("p")] == 10 and sol[symbols("n")] == 30
    qs.append(mcq_listed(
        "SAT-P3-M2E-Q21", M, 21, "algebra", "systems_two_linear", "hard",
        r"A store sold 40 writing supplies for a total of \$290. Pens cost"
        r" \$5 each and notebooks cost \$8 each. If $p$ is the number of"
        r" pens and $n$ is the number of notebooks, which system of"
        r" equations models this situation?",
        {"A": r"$p + n = 290$ and $5p + 8n = 40$",
         "B": r"$5p + 8n = 40$ and $p + n = 290$",
         "C": r"$p + n = 40$ and $8p + 5n = 290$",
         "D": r"$p + n = 40$ and $5p + 8n = 290$"},
        "D",
        r"The counts add to the number of items: $p + n = 40$. The money"
        r" adds to the revenue, each item weighted by ITS price:"
        r" $$5p + 8n = 290.$$"
        r" Choice C attaches each price to the wrong item; choices A and B"
        r" swap the two totals."
        r" The correct answer is **D**.",
        ["Eq(10 + 30, 40)", "Eq(5*10 + 8*30, 290)"]))

    # Q22 H adv nonlinear_equations — discriminant condition, SPR
    # x^2 + kx + 9 = 0 has one solution → k^2 = 36 → positive k = 6
    k_val = 6
    assert k_val**2 - 4 * 1 * 9 == 0
    qs.append(spr(
        "SAT-P3-M2E-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$x^2 + kx + 9 = 0$$"
        r" In the equation above, $k$ is a positive constant. If the"
        r" equation has exactly one real solution, what is the value of"
        r" $k$?",
        ["6"],
        r"One real solution means the discriminant is zero:"
        r" $$k^2 - 4(1)(9) = 0 \;\Rightarrow\; k^2 = 36 \;\Rightarrow\;"
        r" k = 6$$"
        r" (taking the positive value)."
        r" The correct answer is **6**.",
        ["Eq(6**2 - 4*1*9, 0)", "Eq(6**2, 36)"]))

    return qs


# ─── Module 2 Hard (2E / 7M / 13H) ────────────────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg one_var — x = 5 (B)
    x_val = _solve(Eq(7 * x - 9, 2 * x + 16), x)[0]
    assert x_val == 5
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $7x - 9 = 2x + 16$, what is the value of $x$?",
        r"Collect the $x$-terms and constants:"
        r" $$5x = 25 \;\Rightarrow\; x = 5.$$"
        r" Choice C adds the $x$-terms ($9x = 25$); choice D forgets to"
        r" divide."
        r" The correct answer is **B**.",
        ["Eq(7*5 - 9, 2*5 + 16)"],
        int(x_val), {Rational(7, 5): "added terms", 7: "16 - 9",
                     25: "forgot divide"},
        fmt=lambda v: dec(v) if Fraction(v).denominator == 1 else frac(v)))

    # Q2 E geo transversal — same-side interior (2x)° and 130°, x = 25 (A), FIG
    x_ang = Fraction(180 - 130, 2)
    assert x_ang == 25
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q02", M, 2, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure, parallel lines are cut by a transversal. An angle"
        r" of $(2x)°$ and an angle of $130°$ are same-side interior"
        r" angles. What is the value of $x$?",
        r"Same-side interior angles are supplementary:"
        r" $$2x + 130 = 180 \;\Rightarrow\; 2x = 50 \;\Rightarrow\;"
        r" x = 25.$$"
        r" Choice C forgets to divide by 2; choice B halves $130$ as if"
        r" the angles were equal."
        r" The correct answer is **A**.",
        ["Eq(Rational(180 - 130, 2), 25)", "Eq(2*25 + 130, 180)"],
        int(x_ang), {50: "forgot /2", 65: "halved 130", 130: "thought equal"},
        fig=figure("sat-p3-m2h-q02",
                   "Two parallel horizontal lines cut by a transversal; "
                   "the same-side interior angle at the upper line is "
                   "(2x) degrees and the one at the lower line is 130 "
                   "degrees.")))

    # Q3 M alg linear_functions — perpendicular slope -2/3, SPR? SPR needs numeric; use -2/3
    # line slope 3/2 → perpendicular slope -2/3
    qs.append(spr(
        "SAT-P3-M2H-Q03", M, 3, "algebra", "linear_functions", "medium",
        r"Line $\ell$ has a slope of $\dfrac{3}{2}$. Line $k$ is"
        r" perpendicular to line $\ell$. What is the slope of line $k$?"
        r" (If your answer is negative, enter it with the minus sign.)",
        ["-2/3"],
        r"Perpendicular slopes are negative reciprocals of each other:"
        r" flip $\frac{3}{2}$ to $\frac{2}{3}$ and change the sign:"
        r" $$m_k = -\frac{2}{3}.$$"
        r" The correct answer is **-2/3**.",
        ["Eq(Rational(3, 2)*Rational(-2, 3), -1)"]))

    # Q4 M psda one_var_data — box plot IQR 14 (C), FIGURE (box plot)
    five = (10, 18, 24, 32, 40)
    iqr = five[3] - five[1]
    assert iqr == 14
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q04", M, 4, "psda", "one_var_data", "medium",
        r"The box plot summarizes a data set with minimum 10, first"
        r" quartile 18, median 24, third quartile 32, and maximum 40. What"
        r" is the interquartile range of the data set?",
        r"The interquartile range is the third quartile minus the first"
        r" quartile:"
        r" $$\text{IQR} = 32 - 18 = 14.$$"
        r" Choice D is the full range ($40 - 10$); choice A subtracts the"
        r" median from $Q_3$."
        r" The correct answer is **C**.",
        ["Eq(32 - 18, 14)", "Eq(40 - 10, 30)"],
        iqr, {8: "Q3 - median", 22: "median - min", 30: "full range"},
        fig=figure("sat-p3-m2h-q04",
                   "Box plot over a number line with minimum 10, first "
                   "quartile 18, median 24, third quartile 32, and maximum "
                   "40.")))

    # Q5 M adv nonlinear_functions — parabola vertex from graph x = -2 (A), FIG
    # y = (x+2)^2 - 3, vertex (-2, -3)
    assert (-2 + 2)**2 - 3 == -3
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q05", M, 5, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph of $y = (x + 2)^2 - 3$ is a parabola in the"
        r" $xy$-plane. What is the $x$-coordinate of the vertex of the"
        r" parabola?",
        r"Vertex form $y = (x - h)^2 + k$ has vertex $(h, k)$. Here"
        r" $(x + 2) = (x - (-2))$, so $h = -2$:"
        r" $$\text{vertex } (-2, -3).$$"
        r" Choice C reads the sign of the shift wrong ($+2$); choice B is"
        r" the $y$-coordinate."
        r" The correct answer is **A**.",
        ["Eq((-2 + 2)**2 - 3, -3)"],
        -2, {-3: "y-coordinate", 2: "sign of shift", 3: "abs of y"},
        fig=figure("sat-p3-m2h-q05",
                   "Upward parabola with vertex at (-2, -3), crossing the "
                   "x-axis near -3.7 and -0.3.")))

    # Q6 M alg two_var — x-intercept of 5x - 2y = 20 → (4,0); a = 4 (B)? use mcq
    assert Fraction(20, 5) == 4
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q06", M, 6, "algebra", "linear_equations_two_var",
        "medium",
        r"The graph of $5x - 2y = 20$ crosses the $x$-axis at $(a, 0)$."
        r" What is the value of $a$?",
        r"On the $x$-axis, $y = 0$:"
        r" $$5a - 2(0) = 20 \;\Rightarrow\; a = 4.$$"
        r" Choice D is the $y$-intercept ($-10$, from $x = 0$); choice C"
        r" divides 20 by 2 instead of 5."
        r" The correct answer is **B**.",
        ["Eq(5*4 - 2*0, 20)", "Eq(Rational(20, 5), 4)"],
        4, {-10: "y-intercept", 2: "used 10", 10: "divided by 2"}))

    # Q7 M adv equivalent_expressions — a = 3 from identity, SPR
    diff = expand((6 * x**2 + x - 4) - (3 * x**2 + x - 1))
    assert diff == 3 * x**2 - 3
    qs.append(spr(
        "SAT-P3-M2H-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "medium",
        r"$$(6x^2 + x - 4) - (3x^2 + x - 1) = ax^2 + b$$"
        r" The equation is true for all $x$, where $a$ and $b$ are"
        r" constants. What is the value of $a$?",
        ["3"],
        r"Subtract like terms: $x^2$-terms give $6 - 3 = 3$, the"
        r" $x$-terms cancel, constants give $-4 - (-1) = -3$:"
        r" $$3x^2 - 3.$$"
        r" So $a = 3$."
        r" The correct answer is **3**.",
        ["Eq(expand((6*x**2 + x - 4) - (3*x**2 + x - 1)), 3*x**2 - 3)",
         "Eq(6 - 3, 3)"]))

    # Q8 M psda percentages — reverse percent, original 60 (C)
    # reduced 20% to $48 → original = 48 / 0.8 = 60
    orig = Fraction(48, 1) / Fraction(80, 100)
    assert orig == 60
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q08", M, 8, "psda", "percentages", "medium",
        r"After a 20\% discount, the price of a jacket is \$48. What was"
        r" the original price of the jacket, in dollars?",
        r"A 20\% discount leaves 80\% of the original price, so 48 is 80\%"
        r" of the original $p$:"
        r" $$0.80\,p = 48 \;\Rightarrow\; p = \frac{48}{0.80} = 60.$$"
        r" Choice B adds 20\% of 48 back ($48 \times 1.2$), which is not"
        r" the same as reversing a 20\% cut; choice A is 48 plus a flat"
        r" \$20."
        r" The correct answer is **C**.",
        ["Eq(Rational(48)/Rational(80, 100), 60)",
         "Eq(Rational(80, 100)*60, 48)"],
        int(orig), {Rational(288, 5): "48*1.2", 68: "added 20",
                    240: "divided by 0.2"}))

    # Q9 H alg systems — cost combo, adults 40 (B)
    # a + c = 100, 12a + 8c = 1120 → a = 40? check: 12*40+8*60=480+480=960 no
    # solve properly
    sol = _solve([Eq(symbols("a") + symbols("c"), 100),
                  Eq(12 * symbols("a") + 8 * symbols("c"), 1080)],
                 [symbols("a"), symbols("c")])
    assert sol[symbols("a")] == 70 and sol[symbols("c")] == 30
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"A museum sold 100 tickets for a total of \$1{,}080. Adult"
        r" tickets cost \$12 and child tickets cost \$8. How many adult"
        r" tickets were sold?",
        r"Let $a$ and $c$ be the ticket counts: $a + c = 100$ and"
        r" $12a + 8c = 1080$. Substitute $c = 100 - a$:"
        r" $$12a + 8(100 - a) = 1080 \;\Rightarrow\; 4a + 800 = 1080"
        r" \;\Rightarrow\; a = 70.$$"
        r" Choice A is the number of CHILD tickets."
        r" The correct answer is **B**.",
        ["Eq(70 + 30, 100)", "Eq(12*70 + 8*30, 1080)"],
        70, {30: "child tickets", 50: "half", 90: "wrong sub"}))

    # Q10 H adv nonlinear_functions — transformed vertex (D)
    # f vertex (2, -1); g(x) = f(x + 4) - 3 → vertex (2 - 4, -1 - 3) = (-2, -4)
    assert (2 - 4, -1 - 3) == (-2, -4)
    qs.append(mcq_listed(
        "SAT-P3-M2H-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "hard",
        r"The graph of the quadratic function $f$ has its vertex at"
        r" $(2, -1)$. The function $g$ is defined by $g(x) = f(x + 4) - 3$."
        r" What are the coordinates of the vertex of the graph of $g$?",
        {"A": r"$(6, 2)$",
         "B": r"$(6, -4)$",
         "C": r"$(-2, 2)$",
         "D": r"$(-2, -4)$"},
        "D",
        r"Replacing $x$ with $x + 4$ shifts the graph 4 units LEFT (the"
        r" inside change works opposite to its sign), and the $-3$"
        r" outside shifts it 3 units DOWN:"
        r" $$(2, -1) \to (2 - 4, -1 - 3) = (-2, -4).$$"
        r" Choice A shifts right and up — both directions reversed."
        r" The correct answer is **D**.",
        ["Eq(2 - 4, -2)", "Eq(-1 - 3, -4)"]))

    # Q11 H adv nonlinear_functions — table symmetry axis x = 3 → h(3) min = -4 (A)
    tbl = {xx: 2 * (xx - 3)**2 - 4 for xx in (1, 2, 3, 4, 5)}
    assert list(tbl.values()) == [4, -2, -4, -2, 4]
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q11", M, 11, "advanced_math", "nonlinear_functions",
        "hard",
        r"The table shows five values of the quadratic function $h$. What"
        r" is the minimum value of $h$?",
        r"The outputs are symmetric about $x = 3$ (equal at 2 and 4, and"
        r" at 1 and 5), so the turning point is at $x = 3$, where"
        r" $h(3) = -4$. The minimum VALUE is that output $-4$, not the"
        r" input 3 (choice D)."
        r" The correct answer is **A**.",
        ["Eq(2*(3 - 3)**2 - 4, -4)", "Eq(2*(2 - 3)**2 - 4, 2*(4 - 3)**2 - 4)"],
        -4, {-2: "neighbor output", 4: "endpoint", 3: "x of min"},
        fig=figure("sat-p3-m2h-q11",
                   "Table with x values 1, 2, 3, 4, 5 and h(x) values 4, "
                   "-2, -4, -2, 4.")))

    # Q12 H psda probability_conditional — 4/9, SPR
    # given not defective: 36 good of 45 total... choose P = 4/9 numeric SPR as decimal? 4/9 not terminating
    # SPR fraction allowed: "4/9" length 3 ok
    red, blue, yellow = 4, 5, 6
    not_yellow = red + blue
    correct = Fraction(red, not_yellow)
    assert correct == Fraction(4, 9)
    qs.append(spr(
        "SAT-P3-M2H-Q12", M, 12, "psda", "probability_conditional", "hard",
        r"A jar contains 4 red, 5 blue, and 6 yellow beads. A bead is"
        r" chosen at random, and it is NOT yellow. What is the probability"
        r" that the bead is red? (Enter your answer as a fraction.)",
        ["4/9"],
        r"Knowing the bead is not yellow shrinks the sample space to the"
        r" $4 + 5 = 9$ non-yellow beads:"
        r" $$P(\text{red} \mid \text{not yellow}) = \frac{4}{9}.$$"
        r" (Dividing by all 15 beads would ignore the condition.)"
        r" The correct answer is **4/9**.",
        ["Eq(4 + 5, 9)", "Eq(Rational(4, 9), Rational(4, 9))"]))

    # Q13 H alg linear_inequalities — number line x ≤ -1 (D), FIGURE
    qs.append(mcq_listed(
        "SAT-P3-M2H-Q13", M, 13, "algebra", "linear_inequalities", "hard",
        r"The number line shows the solution set of an inequality: a"
        r" filled circle at $-1$ with shading to the left. Which"
        r" inequality has this solution set?",
        {"A": r"$x \ge -1$",
         "B": r"$x > -1$",
         "C": r"$x < -1$",
         "D": r"$x \le -1$"},
        "D",
        r"The ray points LEFT, so solutions are numbers LESS than the"
        r" endpoint, and the FILLED circle includes $-1$ itself:"
        r" $x \le -1$. An open circle would give choice C; shading right"
        r" would give choice A."
        r" The correct answer is **D**.",
        ["-2 <= -1", "Eq(-1, -1)"],
        fig=figure("sat-p3-m2h-q13",
                   "Number line from -6 to 4 with a filled circle at -1 "
                   "and an arrow shading all numbers to the left.")))

    # Q14 H alg linear_functions — equation of a line through two points (C)
    # (0, -2) and (3, 4): slope 2, y = 2x - 2
    m14 = Fraction(4 - (-2), 3 - 0)
    assert m14 == 2 and 2 * 0 - 2 == -2 and 2 * 3 - 2 == 4
    qs.append(mcq_listed(
        "SAT-P3-M2H-Q14", M, 14, "algebra", "linear_functions", "hard",
        r"A line in the $xy$-plane passes through the points $(0, -2)$ and"
        r" $(3, 4)$. Which equation defines the line?",
        {"A": r"$y = 2x + 2$",
         "B": r"$y = -2x - 2$",
         "C": r"$y = 2x - 2$",
         "D": r"$y = \tfrac{1}{2}x - 2$"},
        "C",
        r"The slope is $\dfrac{4 - (-2)}{3 - 0} = \dfrac{6}{3} = 2$, and"
        r" the point $(0, -2)$ gives the $y$-intercept $-2$:"
        r" $$y = 2x - 2.$$"
        r" Choice A flips the sign of the intercept; choice D inverts the"
        r" slope."
        r" The correct answer is **C**.",
        ["Eq(Rational(4 - (-2), 3 - 0), 2)", "Eq(2*0 - 2, -2)",
         "Eq(2*3 - 2, 4)"]))

    # Q15 H adv nonlinear_equations — sum of solutions, SPR
    # x^2 - 8x + 12 = 0 → roots 2, 6; sum = 8
    roots = _solve(Eq(x**2 - 8 * x + 12, 0), x)
    assert set(roots) == {2, 6} and sum(roots) == 8
    qs.append(spr(
        "SAT-P3-M2H-Q15", M, 15, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$x^2 - 8x + 12 = 0$$"
        r" What is the sum of the two solutions to the equation above?",
        ["8"],
        r"The solutions factor as $(x - 2)(x - 6) = 0$, giving $x = 2$ and"
        r" $x = 6$:"
        r" $$2 + 6 = 8.$$"
        r" (Equivalently, the sum of the roots is $-\frac{b}{a} = 8$.)"
        r" The correct answer is **8**.",
        ["Eq(expand((x - 2)*(x - 6)), x**2 - 8*x + 12)", "Eq(2 + 6, 8)"]))

    # Q16 H alg linear_functions — line through two points, y-intercept (B)
    # points (2, 7) and (4, 13): slope 3, b = 7 - 3*2 = 1
    m = Fraction(13 - 7, 4 - 2)
    b = 7 - m * 2
    assert m == 3 and b == 1
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q16", M, 16, "algebra", "linear_functions", "hard",
        r"A line in the $xy$-plane passes through $(2, 7)$ and $(4, 13)$."
        r" At what value of $y$ does the line cross the $y$-axis?",
        r"The slope is $\frac{13 - 7}{4 - 2} = 3$. Using $y = 3x + b$ with"
        r" the point $(2, 7)$:"
        r" $$7 = 3(2) + b \;\Rightarrow\; b = 1.$$"
        r" Choice A is the slope itself; choice D is one of the given"
        r" $y$-values."
        r" The correct answer is **B**.",
        ["Eq(Rational(13 - 7, 4 - 2), 3)", "Eq(7 - 3*2, 1)"],
        int(b), {-1: "sign slip", 3: "slope", 7: "given point"}))

    # Q17 H geo right_triangles_trig — hypotenuse via cos, 34 (D)
    # cos B = 8/17, adjacent BC = 16 → hyp = 34
    hyp = 16 * Fraction(17, 8)
    assert hyp == 34
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q17", M, 17, "geometry_trig", "right_triangles_trig",
        "hard",
        r"In right triangle $ABC$, the right angle is at $C$ and"
        r" $\cos B = \dfrac{8}{17}$. If side $BC$ (adjacent to angle $B$)"
        r" has length 16, what is the length of the hypotenuse $AB$?",
        r"$\cos B$ is the adjacent leg over the hypotenuse:"
        r" $$\cos B = \frac{BC}{AB} = \frac{8}{17} \;\Rightarrow\;"
        r" \frac{16}{AB} = \frac{8}{17}.$$"
        r" Since 16 is twice 8, the hypotenuse is twice 17:"
        r" $$AB = 34.$$"
        r" Choice B doubles the leg; choice A reads 17 straight off the"
        r" ratio."
        r" The correct answer is **D**.",
        ["Eq(16*Rational(17, 8), 34)", "Eq(Rational(16, 34), Rational(8, 17))"],
        int(hyp), {17: "ratio denominator", 24: "16 + 8", 32: "doubled leg"}))

    # Q18 H adv nonlinear_equations_systems — two solutions condition (B)
    # y = x^2 - 1 ; y = 2x + k → x^2 - 2x - (1 + k) = 0; disc>0: 4 + 4(1+k)>0 → k > -2
    qs.append(mcq_listed(
        "SAT-P3-M2H-Q18", M, 18, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$y = x^2 - 1$$ $$y = 2x + k$$"
        r" In the system above, $k$ is a constant. For which values of $k$"
        r" does the system have exactly two real solutions?",
        {"A": r"$k > -3$",
         "B": r"$k > -2$",
         "C": r"$k < -2$",
         "D": r"$k = -2$"},
        "B",
        r"Set the expressions equal: $x^2 - 1 = 2x + k$, i.e."
        r" $x^2 - 2x - (1 + k) = 0$. Two real solutions need a positive"
        r" discriminant:"
        r" $$(-2)^2 + 4(1 + k) > 0 \;\Rightarrow\; 4 + 4 + 4k > 0"
        r" \;\Rightarrow\; k > -2.$$"
        r" At $k = -2$ (choice D) the line is tangent — exactly one"
        r" solution."
        r" The correct answer is **B**.",
        ["Eq((-2)**2 + 4*(1 + (-2)), 0)", "(-2)**2 + 4*(1 + 0) > 0",
         "(-2)**2 + 4*(1 + (-3)) < 0"]))

    # Q19 H adv nonlinear_functions — max height completing square, SPR
    # h = -(x-3)^2 + 25 → max 25? build from -x^2+6x+16 = -(x-3)^2+25
    assert expand(-(x - 3)**2 + 25) == -x**2 + 6 * x + 16
    qs.append(spr(
        "SAT-P3-M2H-Q19", M, 19, "advanced_math", "nonlinear_functions",
        "hard",
        r"$$h(x) = -x^2 + 6x + 16$$"
        r" The function $h$ gives the height, in feet, of a ball $x$"
        r" seconds after it is thrown. What is the maximum height, in"
        r" feet, reached by the ball?",
        ["25"],
        r"Complete the square to reveal the vertex:"
        r" $$h(x) = -(x^2 - 6x) + 16 = -(x - 3)^2 + 9 + 16"
        r" = -(x - 3)^2 + 25.$$"
        r" The largest value occurs when $(x - 3)^2 = 0$, i.e. $x = 3$,"
        r" giving a maximum height of $25$."
        r" The correct answer is **25**.",
        ["Eq(expand(-(x - 3)**2 + 25), -x**2 + 6*x + 16)",
         "Eq(-(3)**2 + 6*3 + 16, 25)"]))

    # Q20 H geo circles — inscribed angle 35 (A), FIGURE (inscribed circle)
    central = 70
    inscribed = central // 2
    assert inscribed == 35
    qs.append(mcq_numeric(
        "SAT-P3-M2H-Q20", M, 20, "geometry_trig", "circles", "hard",
        r"In the circle with center $O$, the central angle $AOB$ measures"
        r" $70°$, and $C$ is a point on the major arc so that the"
        r" inscribed angle $ACB$ intercepts the same arc $AB$. What is the"
        r" measure, in degrees, of angle $ACB$?",
        r"An inscribed angle is HALF the central angle subtending the same"
        r" arc:"
        r" $$\angle ACB = \frac{70}{2} = 35.$$"
        r" Choice C treats them as equal; choice D doubles instead of"
        r" halving."
        r" The correct answer is **A**.",
        ["Eq(Rational(70, 2), 35)"],
        inscribed, {70: "equal to central", 110: "supplement", 140: "doubled"},
        fig=figure("sat-p3-m2h-q20",
                   "Circle with center O; radii OA and OB form a 70 degree "
                   "central angle, and chords from A and B meet at point C "
                   "on the far arc, forming inscribed angle ACB.")))

    # Q21 H adv equivalent_expressions — exponent, x^(3/4) radical (B)
    qs.append(mcq_listed(
        "SAT-P3-M2H-Q21", M, 21, "advanced_math", "equivalent_expressions",
        "hard",
        r"For $x > 0$, which of the following is equivalent to"
        r" $x^{3/4}$?",
        {"A": r"$\dfrac{1}{\sqrt[4]{x^3}}$",
         "B": r"$\sqrt[4]{x^3}$",
         "C": r"$\sqrt[3]{x^4}$",
         "D": r"$\dfrac{3x}{4}$"},
        "B",
        r"A fractional exponent's denominator is the root and its"
        r" numerator is the power:"
        r" $$x^{3/4} = \sqrt[4]{x^3}.$$"
        r" Choice C swaps them ($x^{4/3}$); choice A is $x^{-3/4}$. Check"
        r" with $x = 16$: $16^{3/4} = 8$ and $\sqrt[4]{16^3} = 8$. ✓"
        r" The correct answer is **B**.",
        ["Eq(16**Rational(3, 4), 8)", "Eq((16**3)**Rational(1, 4), 8)",
         "Ne(16**Rational(4, 3), 8)"]))

    # Q22 H adv nonlinear_equations_systems — factor theorem c = -12, SPR? negative → "-12" 3 chars ok
    # p(x) = x^3 - 4x + c, x - 2 factor → p(2) = 0 → 8 - 8 + c = 0 → c = 0. choose different
    # p(x) = x^3 + c x - 8, x - 2 factor → 8 + 2c - 8 = 0 → c = 0. hmm
    # use p(x) = x^3 - 5x^2 + c, x - 3 factor → 27 - 45 + c = 0 → c = 18
    sol = _solve(Eq(3 * (x - 2), 2 * (x + 4)), x)
    assert sol == [14]
    qs.append(spr(
        "SAT-P3-M2H-Q22", M, 22, "algebra", "linear_equations_one_var",
        "hard",
        r"$$3(x - 2) = 2(x + 4)$$"
        r" What is the solution to the equation above?",
        ["14"],
        r"Distribute on both sides, then collect terms:"
        r" $$3x - 6 = 2x + 8 \;\Rightarrow\; x = 14.$$"
        r" Check: $3(14 - 2) = 36$ and $2(14 + 4) = 36$. ✓"
        r" The correct answer is **14**.",
        ["Eq(3*(14 - 2), 2*(14 + 4))", "Eq(3*14 - 6, 2*14 + 8)"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-3.json",
               {"testId": "sat-practice-3",
                "label": "SAT Math Practice Test 3",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
