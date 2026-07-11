#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 2 (data/sat/sat-practice-2.json).

Built on the shared framework in satbuild.py — this file is ONLY stems,
parameters, computed answers, named distractor error models, verify[]
strings, and solutions. Every archetype here is deliberately different
from Practice Test 1 (proportion equations, elimination systems, reverse
percent, inscribed angles, composition, factor theorem, Vieta, function
transformations, half-life decay, mixtures, combined means) and the
figures exercise the satfigs tool library: bar chart, value table,
angles-on-a-line, composite area, association scatter, decay curve,
inscribed circle, lines-on-a-grid, transversal, histogram, box plot,
absolute-value curves, number lines, cylinders, and trig triangles.

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


def pi_mult(n: int) -> str:
    return rf"${n}\pi$"


# ─── Module 1 (8E / 9M / 5H) ──────────────────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E alg one_var — fraction equation, x = 25 (D)
    x_val = 8 * 2 + 9
    assert Fraction(x_val - 9, 2) == 8
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $\dfrac{x - 9}{2} = 8$, what is the value of $x$?",
        r"Multiply both sides by 2, then add 9:"
        r" $$x - 9 = 16 \;\Rightarrow\; x = 25.$$"
        r" Choice B stops at $16 - 9 = 7$, subtracting instead of adding"
        r" after the multiplication; choice C computes $8 + 9$ without"
        r" ever multiplying by 2."
        r" The correct answer is **D**.",
        ["Eq((25 - 9)/2, 8)", "Eq(8*2 + 9, 25)"],
        x_val, {-1: "8 - 9", 16 - 9: "subtracted 9", 8 + 9: "forgot x2"},
        expect_letter="D"))

    # Q2 E psda one_var_data — bar chart difference, 15 (A), FIGURE
    sold = {"Mon": 30, "Tue": 25, "Wed": 40, "Thu": 55, "Fri": 45}
    correct = sold["Thu"] - sold["Wed"]
    assert correct == 15
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q02", M, 2, "psda", "one_var_data", "easy",
        r"The bar chart shows the number of books a store sold on each of"
        r" five days. How many more books were sold on Thursday than on"
        r" Wednesday?",
        r"Read the two bars: Thursday is 55 and Wednesday is 40, so the"
        r" difference is $$55 - 40 = 15.$$"
        r" Choice B compares Thursday with Tuesday (25) instead of"
        r" Wednesday, and choice C is Thursday's own bar."
        r" The correct answer is **A**.",
        ["Eq(55 - 40, 15)", "Eq(55 - 25, 30)"],
        correct, {30: "used Tuesday", 55: "Thursday alone", 95: "added"},
        fig=figure("sat-p2-m1-q02",
                   "Bar chart of books sold: Monday 30, Tuesday 25, "
                   "Wednesday 40, Thursday 55, Friday 45."),
        expect_letter="A"))

    # Q3 E alg linear_functions — equation from table (B), FIGURE
    xs_t, ys_t = [0, 1, 2, 3], [5, 8, 11, 14]
    assert all(3 * a + 5 == b for a, b in zip(xs_t, ys_t))
    qs.append(mcq_listed(
        "SAT-P2-M1-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The table shows four values of the linear function $f$. Which"
        r" equation defines $f$?",
        {"A": r"$f(x) = x + 5$",
         "B": r"$f(x) = 3x + 5$",
         "C": r"$f(x) = 5x + 3$",
         "D": r"$f(x) = 8x$"},
        "B",
        r"The outputs rise by 3 each time $x$ rises by 1, so the slope is"
        r" 3, and $f(0) = 5$ gives the starting value:"
        r" $$f(x) = 3x + 5.$$"
        r" Check a second row: $f(2) = 11$. ✓ Choice C swaps the slope"
        r" and the constant — it fails at $x = 1$ ($5 + 3 = 8$ works, but"
        r" $f(2) = 13 \ne 11$)."
        r" The correct answer is **B**.",
        ["Eq(3*0 + 5, 5)", "Eq(3*1 + 5, 8)", "Eq(3*2 + 5, 11)",
         "Eq(3*3 + 5, 14)", "Ne(5*2 + 3, 11)"],
        fig=figure("sat-p2-m1-q03",
                   "Table with x values 0, 1, 2, 3 and f(x) values 5, 8, "
                   "11, 14.")))

    # Q4 E adv nonlinear_functions — g(3) = 7, SPR
    assert 3**3 - 20 == 7
    qs.append(spr(
        "SAT-P2-M1-Q04", M, 4, "advanced_math", "nonlinear_functions",
        "easy",
        r"The function $g$ is defined by $g(x) = x^3 - 20$. What is the"
        r" value of $g(3)$?",
        ["7"],
        r"Substitute $x = 3$:"
        r" $$g(3) = 3^3 - 20 = 27 - 20 = 7.$$"
        r" The correct answer is **7**.",
        ["Eq(3**3 - 20, 7)"]))

    # Q5 E geo lines_angles — angles on a line, x = 73 (C), FIGURE
    x_val = Fraction(180 - 34, 2)
    assert x_val == 73
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q05", M, 5, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure, two angles measuring $(2x)°$ and $34°$ together"
        r" form a straight line. What is the value of $x$?",
        r"Angles on a straight line sum to $180°$:"
        r" $$2x + 34 = 180 \;\Rightarrow\; 2x = 146 \;\Rightarrow\;"
        r" x = 73.$$"
        r" Choice D stops at $2x = 146$; choice A uses $90°$ instead of"
        r" $180°$ for the straight line."
        r" The correct answer is **C**.",
        ["Eq((180 - 34)/2, 73)", "Eq(2*73 + 34, 180)"],
        int(x_val), {28: "used 90", 34: "thought equal", 146: "forgot /2"},
        fig=figure("sat-p2-m1-q05",
                   "A straight line with a ray from a point on it, "
                   "forming two angles labeled (2x) degrees and 34 "
                   "degrees."),
        expect_letter="C"))

    # Q6 E psda ratios_rates_units — 120 pages (C)
    rate = Fraction(45, 3)
    correct = int(rate * 8)
    assert correct == 120
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q06", M, 6, "psda", "ratios_rates_units", "easy",
        r"A printer prints 45 pages every 3 minutes at a constant rate."
        r" How many pages does it print in 8 minutes?",
        r"The unit rate is $45 \div 3 = 15$ pages per minute, so in 8"
        r" minutes: $$15 \times 8 = 120.$$"
        r" Choice A is the per-minute rate itself; choice D multiplies"
        r" $45 \times 8$ without dividing by the 3 minutes."
        r" The correct answer is **C**.",
        ["Eq(Rational(45, 3), 15)", "Eq(15*8, 120)"],
        correct, {15: "unit rate only", 105: "added rate for 4 min",
                  360: "forgot /3"},
        expect_letter="C"))

    # Q7 E adv equivalent_expressions — exponent rules, x^6 (A)
    qs.append(mcq_listed(
        "SAT-P2-M1-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to"
        r" $\dfrac{x^5 \cdot x^3}{x^2}$ for $x \ne 0$?",
        {"A": r"$x^6$",
         "B": r"$x^8$",
         "C": r"$x^{10}$",
         "D": r"$x^{13}$"},
        "A",
        r"Multiply by adding exponents, divide by subtracting:"
        r" $$\frac{x^5 \cdot x^3}{x^2} = \frac{x^8}{x^2} = x^6.$$"
        r" Choice B forgets the division; choice D multiplies"
        r" $5 \cdot 3$ instead of adding."
        r" The correct answer is **A**.",
        ["Eq((2**5 * 2**3)/2**2, 2**6)", "Eq(5 + 3 - 2, 6)"]))

    # Q8 E geo area_volume — composite area 80 (C), FIGURE
    rw, rh, th = 10, 6, 4
    area = rw * rh + Fraction(rw * th, 2)
    assert area == 80
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q08", M, 8, "geometry_trig", "area_volume", "easy",
        r"The figure shows a rectangle with a width of 10 and a height of"
        r" 6, with a right triangle of height 4 on top whose base is the"
        r" top side of the rectangle. What is the total area of the"
        r" figure?",
        r"Add the two areas:"
        r" $$A = 10 \cdot 6 + \frac{1}{2} \cdot 10 \cdot 4 = 60 + 20"
        r" = 80.$$"
        r" Choice B is the rectangle alone; choice D forgets the"
        r" $\frac{1}{2}$ in the triangle's area."
        r" The correct answer is **C**.",
        ["Eq(10*6, 60)", "Eq(Rational(1,2)*10*4, 20)", "Eq(60 + 20, 80)"],
        int(area), {40: "triangle as rectangle", 60: "rectangle only",
                    100: "forgot 1/2"},
        fig=figure("sat-p2-m1-q08",
                   "A rectangle 10 wide and 6 tall with a right triangle "
                   "of height 4 on its top side; the right angle of the "
                   "triangle is at the top-right corner."),
        expect_letter="C"))

    # Q9 M alg systems — elimination, y = 3, SPR
    y_val = Fraction(17 - 11, 2)
    x_val = Fraction(17 - 5 * 3, 2)
    assert (x_val, y_val) == (1, 3)
    qs.append(spr(
        "SAT-P2-M1-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$2x + 5y = 17$$ $$2x + 3y = 11$$"
        r" If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $y$?",
        ["3"],
        r"The $x$-terms match, so subtract the second equation from the"
        r" first:"
        r" $$(2x + 5y) - (2x + 3y) = 17 - 11 \;\Rightarrow\; 2y = 6"
        r" \;\Rightarrow\; y = 3.$$"
        r" (Then $x = 1$, and $2(1) + 5(3) = 17$ checks.)"
        r" The correct answer is **3**.",
        ["Eq(2*1 + 5*3, 17)", "Eq(2*1 + 3*3, 11)", "Eq((17 - 11)/2, 3)"]))

    # Q10 M psda two_var_data — association type (B), FIGURE
    qs.append(mcq_listed(
        "SAT-P2-M1-Q10", M, 10, "psda", "two_var_data_models", "medium",
        r"The scatterplot shows 10 measurements of two variables $x$ and"
        r" $y$. Which statement best describes the association between"
        r" $x$ and $y$?",
        {"A": r"A strong positive linear association",
         "B": r"A strong negative linear association",
         "C": r"A nonlinear association",
         "D": r"No association"},
        "B",
        r"As $x$ increases, $y$ decreases at a roughly constant rate, and"
        r" the points cluster tightly around a straight line — a strong"
        r" NEGATIVE linear association. Positive (choice A) would rise to"
        r" the right; \"no association\" (choice D) would show no"
        r" pattern at all."
        r" The correct answer is **B**.",
        ["Eq((38 - 10)/(1 - 8) + 4, 0)"],
        fig=figure("sat-p2-m1-q10",
                   "Scatterplot of 10 points falling steadily from "
                   "upper left, near (1, 38), to lower right, near "
                   "(10, 5), close to a straight line.")))

    # Q11 M alg linear_functions — interpretation of the rate (C)
    assert 280 - 8 * 35 == 0
    qs.append(mcq_listed(
        "SAT-P2-M1-Q11", M, 11, "algebra", "linear_functions", "medium",
        r"A pump drains a water tank. The function $W(t) = 280 - 8t$"
        r" gives the number of liters of water in the tank $t$ minutes"
        r" after the pump starts. What is the best interpretation of the"
        r" number 8 in this context?",
        {"A": r"The number of liters in the tank when the pump starts.",
         "B": r"The number of minutes the pump runs until the tank is empty.",
         "C": r"The number of liters drained from the tank each minute.",
         "D": r"The total number of liters the pump drains."},
        "C",
        r"In $W(t) = 280 - 8t$ the coefficient of $t$ is the rate of"
        r" change: each minute, the water decreases by"
        r" $$W(t) - W(t+1) = 8 \text{ liters}.$$"
        r" Choice A describes 280; choice B is $280 \div 8 = 35$ minutes,"
        r" a number that is in neither slot of the formula."
        r" The correct answer is **C**.",
        ["Eq((280 - 8*0) - (280 - 8*1), 8)", "Eq(Rational(280, 8), 35)"]))

    # Q12 M adv nonlinear_functions — decay curve, mass 40 at t=30 (A), FIG
    m0 = 320
    vals = {t: m0 // 2**(t // 10) for t in (0, 10, 20, 30)}
    assert vals == {0: 320, 10: 160, 20: 80, 30: 40}
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q12", M, 12, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph shows the mass $y$, in grams, of a radioactive sample"
        r" $x$ days after it was measured; the mass halves every 10 days"
        r" from an initial 320 grams. What is the mass of the sample at"
        r" $x = 30$?",
        r"Thirty days is three halving periods:"
        r" $$320 \to 160 \to 80 \to 40.$$"
        r" Equivalently, $320 \cdot \left(\frac{1}{2}\right)^{30/10}"
        r" = 320 \cdot \frac{1}{8} = 40$. Choice B stops after two"
        r" halvings (day 20)."
        r" The correct answer is **A**.",
        ["Eq(320*Rational(1,2)**3, 40)", "Eq(320*Rational(1,2)**2, 80)"],
        40, {80: "stopped at day 20", 160: "one halving", 320: "initial"},
        fig=figure("sat-p2-m1-q12",
                   "Decreasing exponential curve from (0, 320) through "
                   "(10, 160), (20, 80), and (30, 40), flattening toward "
                   "the x-axis."),
        expect_letter="A"))

    # Q13 M adv equivalent_expressions — x^(2/3) as a radical (B)
    qs.append(mcq_listed(
        "SAT-P2-M1-Q13", M, 13, "advanced_math", "equivalent_expressions",
        "medium",
        r"For $x > 0$, which of the following is equivalent to"
        r" $x^{2/3}$?",
        {"A": r"$\dfrac{1}{\sqrt[3]{x^2}}$",
         "B": r"$\sqrt[3]{x^2}$",
         "C": r"$\sqrt{x^3}$",
         "D": r"$\dfrac{x^2}{3}$"},
        "B",
        r"A fractional exponent's DENOMINATOR is the root and its"
        r" numerator is the power:"
        r" $$x^{2/3} = \sqrt[3]{x^2}.$$"
        r" Choice C swaps them ($x^{3/2}$), and choice A is $x^{-2/3}$."
        r" Check with $x = 8$: $8^{2/3} = 4$ and $\sqrt[3]{64} = 4$. ✓"
        r" The correct answer is **B**.",
        ["Eq(8**Rational(2, 3), 4)", "Eq((8**2)**Rational(1, 3), 4)",
         "Ne(8**Rational(3, 2), 4)"]))

    # Q14 M adv nonlinear_equations_systems — rational equation, x = 4, SPR
    assert Fraction(24, 4 + 2) == 4
    qs.append(spr(
        "SAT-P2-M1-Q14", M, 14, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"$$\frac{24}{x + 2} = 4$$"
        r" What is the solution to the equation above?",
        ["4"],
        r"Multiply both sides by $x + 2$:"
        r" $$24 = 4(x + 2) \;\Rightarrow\; 6 = x + 2 \;\Rightarrow\;"
        r" x = 4.$$"
        r" Check: $\frac{24}{6} = 4$. ✓"
        r" The correct answer is **4**.",
        ["Eq(Rational(24, 4 + 2), 4)", "Eq(Rational(24, 4), 6)"]))

    # Q15 M alg linear_inequalities — max rides 6 (B)
    t_max = (110 - 20) // 15
    assert t_max == 6 and 15 * 6 + 20 <= 110 < 15 * 7 + 20
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"Admission to a fair costs \$20, and each ride costs \$15."
        r" Deshawn can spend at most \$110 at the fair. What is the"
        r" greatest number of rides he can go on?",
        r"With $r$ rides, the total cost is $15r + 20$, so"
        r" $$15r + 20 \le 110 \;\Rightarrow\; 15r \le 90 \;\Rightarrow\;"
        r" r \le 6.$$"
        r" The greatest whole number of rides is 6. Choice C ignores the"
        r" \$20 admission ($110 / 15 = 7.33$, then rounds down to 7)."
        r" The correct answer is **B**.",
        ["Eq((110 - 20)/15, 6)", "15*6 + 20 <= 110", "15*7 + 20 > 110"],
        t_max, {4: "subtracted fee twice", 7: "ignored fee",
                8: "added fee to budget"},
        expect_letter="B"))

    # Q16 M geo circles — inscribed angle 40 (A), FIGURE
    central = 80
    inscribed = central // 2
    assert inscribed == 40
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q16", M, 16, "geometry_trig", "circles", "medium",
        r"In the circle shown with center $O$, points $A$, $B$, and $C$"
        r" lie on the circle. The central angle $AOB$ measures $80°$,"
        r" and the inscribed angle $ACB$ intercepts the same arc $AB$."
        r" What is the value of $x$, the measure in degrees of angle"
        r" $ACB$?",
        r"An inscribed angle measures HALF the central angle that"
        r" intercepts the same arc:"
        r" $$x = \frac{80}{2} = 40.$$"
        r" Choice B treats the two angles as equal; choice D doubles"
        r" instead of halving."
        r" The correct answer is **A**.",
        ["Eq(Rational(80, 2), 40)"],
        inscribed, {80: "equal to central", 100: "supplement",
                    160: "doubled"},
        fig=figure("sat-p2-m1-q16",
                   "Circle with center O; radii OA and OB form a central "
                   "angle of 80 degrees, and chords from A and B meet at "
                   "point C on the far side of the circle, forming an "
                   "inscribed angle labeled x degrees."),
        expect_letter="A"))

    # Q17 M alg systems — read solution from graph (D), FIGURE
    # y = x - 1 and y = -x + 5 meet at (3, 2)
    assert 3 - 1 == 2 and -3 + 5 == 2
    qs.append(mcq_listed(
        "SAT-P2-M1-Q17", M, 17, "algebra", "systems_two_linear", "medium",
        r"The graph shows the two lines of a system of linear equations."
        r" What is the solution $(x, y)$ to the system?",
        {"A": r"$(-3, 2)$",
         "B": r"$(2, 3)$",
         "C": r"$(3, -2)$",
         "D": r"$(3, 2)$"},
        "D",
        r"The solution of a system is the intersection point of its"
        r" graphs. The lines cross 3 units right of the origin and 2"
        r" units up: $(3, 2)$. Choice B swaps the coordinates — always"
        r" read $x$ (horizontal) first."
        r" The correct answer is **D**.",
        ["Eq(3 - 1, 2)", "Eq(-3 + 5, 2)"],
        fig=figure("sat-p2-m1-q17",
                   "Coordinate grid with two lines: one rising through "
                   "(0, -1) with slope 1, one falling through (0, 5) "
                   "with slope -1; they intersect at the marked point "
                   "(3, 2).")))

    # Q18 H alg one_var — fraction answer 7/2, SPR
    sol = _solve(Eq(6*x - 5, 2*x + 9), x)
    assert sol == [Rational(7, 2)]
    qs.append(spr(
        "SAT-P2-M1-Q18", M, 18, "algebra", "linear_equations_one_var",
        "hard",
        r"$$6x - 5 = 2x + 9$$"
        r" What is the solution to the equation above?",
        ["7/2", "3.5"],
        r"Collect the $x$-terms on one side and constants on the other:"
        r" $$6x - 2x = 9 + 5 \;\Rightarrow\; 4x = 14 \;\Rightarrow\;"
        r" x = \frac{14}{4} = \frac{7}{2}.$$"
        r" Check: $6(3.5) - 5 = 16$ and $2(3.5) + 9 = 16$. ✓"
        r" The correct answer is **7/2** (or 3.5).",
        ["Eq(6*Rational(7,2) - 5, 2*Rational(7,2) + 9)",
         "Eq(Rational(14, 4), Rational(7, 2))"]))

    # Q19 H adv nonlinear_functions — transformed vertex (D)
    # f(x) = (x-1)^2 - 4; g(x) = f(x - 3) + 2 has vertex (4, -2)
    gx = expand((x - 3 - 1)**2 - 4 + 2)
    assert gx == expand((x - 4)**2 - 2)
    qs.append(mcq_listed(
        "SAT-P2-M1-Q19", M, 19, "advanced_math", "nonlinear_functions",
        "hard",
        r"The graph of the quadratic function $f$ has its vertex at"
        r" $(1, -4)$. The function $g$ is defined by"
        r" $g(x) = f(x - 3) + 2$. What are the coordinates of the vertex"
        r" of the graph of $g$?",
        {"A": r"$(-2, -6)$",
         "B": r"$(-2, -2)$",
         "C": r"$(4, -6)$",
         "D": r"$(4, -2)$"},
        "D",
        r"Replacing $x$ with $x - 3$ shifts the graph 3 units to the"
        r" RIGHT (the inside change works opposite to its sign), and the"
        r" $+2$ outside shifts it 2 units UP:"
        r" $$(1, -4) \to (1 + 3, -4 + 2) = (4, -2).$$"
        r" Choice A shifts left and down — both directions reversed."
        r" The correct answer is **D**.",
        ["Eq(1 + 3, 4)", "Eq(-4 + 2, -2)",
         "Eq(expand((x - 4)**2 - 2), expand(((x - 3) - 1)**2 - 4 + 2))"]))

    # Q20 H psda probability_conditional — 5/12 (C)
    red, blue, green = 5, 7, 8
    not_green = red + blue
    correct = Fraction(red, not_green)
    assert correct == Fraction(5, 12)
    qs.append(mcq_numeric(
        "SAT-P2-M1-Q20", M, 20, "psda", "probability_conditional", "hard",
        r"A bag contains 5 red, 7 blue, and 8 green marbles. A marble is"
        r" selected at random, and it is NOT green. What is the"
        r" probability that the selected marble is red?",
        r"Knowing the marble is not green shrinks the sample space to"
        r" the $5 + 7 = 12$ non-green marbles:"
        r" $$P(\text{red} \mid \text{not green}) = \frac{5}{12}.$$"
        r" Choice A divides by all 20 marbles, ignoring the condition;"
        r" choice D is the probability of the CONDITION itself"
        r" ($\frac{12}{20}$)."
        r" The correct answer is **C**.",
        ["Eq(5 + 7, 12)", "Eq(5 + 7 + 8, 20)",
         "Rational(5, 20) < Rational(5, 15)",
         "Rational(5, 15) < Rational(5, 12)"],
        correct, {Fraction(5, 20): "of all marbles",
                  Fraction(5, 15): "wrong complement",
                  Fraction(12, 20): "P(not green)"},
        fmt=lambda v: frac(v),
        expect_letter="C"))

    # Q21 H geo right_triangles_trig — adjacent leg 48, SPR
    adj = 52 * Fraction(12, 13)
    assert adj == 48
    qs.append(spr(
        "SAT-P2-M1-Q21", M, 21, "geometry_trig", "right_triangles_trig",
        "hard",
        r"In right triangle $ABC$, the measure of angle $C$ is $90°$ and"
        r" $\cos B = \dfrac{12}{13}$. If the length of hypotenuse $AB$"
        r" is 52, what is the length of side $BC$?",
        ["48"],
        r"$\cos B$ is the ratio of the leg ADJACENT to angle $B$ to the"
        r" hypotenuse. Side $BC$ is adjacent to $B$, so"
        r" $$\frac{BC}{52} = \frac{12}{13} \;\Rightarrow\;"
        r" BC = 52 \cdot \frac{12}{13} = 48.$$"
        r" The correct answer is **48**.",
        ["Eq(52*Rational(12, 13), 48)", "Eq(Rational(48, 52), Rational(12, 13))"]))

    # Q22 H adv nonlinear_equations_systems — k > 2 (B)
    # x^2 + 3 = 2x + k → x^2 - 2x + (3 - k) = 0, disc > 0 ⟺ k > 2
    qs.append(mcq_listed(
        "SAT-P2-M1-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$y = x^2 + 3$$ $$y = 2x + k$$"
        r" In the system of equations above, $k$ is a constant. For which"
        r" values of $k$ does the system have exactly two solutions?",
        {"A": r"$k > -2$",
         "B": r"$k > 2$",
         "C": r"$k < 2$",
         "D": r"$k = 2$"},
        "B",
        r"Setting the right-hand sides equal gives"
        r" $x^2 - 2x + (3 - k) = 0$. Two solutions require a positive"
        r" discriminant:"
        r" $$(-2)^2 - 4(3 - k) > 0 \;\Rightarrow\; 4k - 8 > 0"
        r" \;\Rightarrow\; k > 2.$$"
        r" At $k = 2$ (choice D) the line is tangent — exactly ONE"
        r" solution. Desmos check: graph with $k = 3$ (two crossings)"
        r" and $k = 1$ (no crossing)."
        r" The correct answer is **B**.",
        ["Eq(2**2 - 4*(3 - 2), 0)", "2**2 - 4*(3 - 3) > 0",
         "2**2 - 4*(3 - 1) < 0"]))

    return qs


# ─── Module 2 shared slot notes ───────────────────────────────────────
# Anchor: alg Q1,3,6,9,13,16,19,21 · adv Q5,7,11,14,15,18,20,22 ·
# psda Q4,10,12 · geo Q2,8,17. SPR {3,7,12,15,19,22}. Variants share the
# slot's domain/skill/format; only difficulty and parameters differ.


def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg one_var — x = 3 (A)
    sol = _solve(Eq(4*x + 9, 2*x + 15), x)
    assert sol == [3]
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $4x + 9 = 2x + 15$, what is the value of $x$?",
        r"Subtract $2x$ and 9 from both sides:"
        r" $$2x = 6 \;\Rightarrow\; x = 3.$$"
        r" Check: $4(3) + 9 = 21$ and $2(3) + 15 = 21$. ✓ Choice B comes"
        r" from ADDING the $x$-terms ($6x = 24$); choice C is $15 - 9$"
        r" without dividing by 2."
        r" The correct answer is **A**.",
        ["Eq(4*3 + 9, 2*3 + 15)", "Eq((15 - 9)/2, 3)"],
        3, {4: "6x = 24", 6: "15 - 9", 12: "(15+9)/2"},
        expect_letter="A"))

    # Q2 E geo transversal — co-interior with 110°, x = 70 (C), FIGURE
    assert 110 + 70 == 180
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q02", M, 2, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure, lines $\ell$ and $m$ are parallel and are cut by"
        r" a transversal. One same-side interior angle measures $110°$"
        r" and the other measures $x°$. What is the value of $x$?",
        r"Same-side interior angles between parallel lines are"
        r" SUPPLEMENTARY:"
        r" $$x + 110 = 180 \;\Rightarrow\; x = 70.$$"
        r" Choice D treats them as equal (that is the rule for alternate"
        r" interior or corresponding angles, not same-side)."
        r" The correct answer is **C**.",
        ["Eq(180 - 110, 70)"],
        70, {20: "used 110 - 90", 55: "halved 110", 110: "thought equal"},
        fig=figure("sat-p2-m2e-q02",
                   "Two parallel horizontal lines l and m cut by a "
                   "transversal; the same-side interior angle at line l "
                   "is labeled 110 degrees and the one at line m is "
                   "labeled x degrees."),
        expect_letter="C"))

    # Q3 E alg linear_functions — f(6) = 17, SPR
    assert 4 * 6 - 7 == 17
    qs.append(spr(
        "SAT-P2-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 4x - 7$. What is the"
        r" value of $f(6)$?",
        ["17"],
        r"Substitute $x = 6$:"
        r" $$f(6) = 4(6) - 7 = 24 - 7 = 17.$$"
        r" The correct answer is **17**.",
        ["Eq(4*6 - 7, 17)"]))

    # Q4 E psda one_var_data — histogram, at least 40: 8 (B), FIGURE
    counts = {10: 2, 20: 4, 30: 6, 40: 5, 50: 3}
    correct = counts[40] + counts[50]
    assert correct == 8 and sum(counts.values()) == 20
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q04", M, 4, "psda", "one_var_data", "easy",
        r"The histogram shows the ages of the 20 members of a club, in"
        r" ten-year groups. How many members are at least 40 years old?",
        r"\"At least 40\" covers the last two bars:"
        r" $$5 + 3 = 8.$$"
        r" Choice A is only the 40-to-50 bar; choice C adds the bars"
        r" BELOW 40 instead."
        r" The correct answer is **B**.",
        ["Eq(5 + 3, 8)", "Eq(2 + 4 + 6, 12)", "Eq(2 + 4 + 6 + 5 + 3, 20)"],
        correct, {5: "one bar only", 12: "wrong side", 20: "total"},
        fig=figure("sat-p2-m2e-q04",
                   "Histogram of member ages: 2 members aged 10 to 20, "
                   "4 aged 20 to 30, 6 aged 30 to 40, 5 aged 40 to 50, "
                   "and 3 aged 50 to 60."),
        expect_letter="B"))

    # Q5 E adv nonlinear_functions — V-graph minimum at x = 3 (D), FIGURE
    assert abs(3 - 3) - 2 == -2
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q05", M, 5, "advanced_math", "nonlinear_functions",
        "easy",
        r"The graph of $y = |x - 3| - 2$ is shown. For what value of $x$"
        r" does $y$ reach its minimum?",
        r"An absolute value is smallest when the expression inside is"
        r" zero: $x - 3 = 0$ at $x = 3$, where $y = -2$. The question"
        r" asks for the $x$-VALUE of the minimum, not the minimum $y$"
        r" (choice B)."
        r" The correct answer is **D**.",
        ["Eq(Abs(3 - 3) - 2, -2)", "Eq(Abs(1 - 3) - 2, 0)"],
        3, {-3: "sign of shift", -2: "the minimum y", 2: "sign slip"},
        fig=figure("sat-p2-m2e-q05",
                   "V-shaped graph of an absolute value function with "
                   "vertex at (3, -2), rising with slope 1 on each side "
                   "and crossing the x-axis at 1 and 5."),
        expect_letter="D"))

    # Q6 E alg two_var — which point on y = 5x − 8 (D)
    assert 5 * 2 - 8 == 2
    qs.append(mcq_listed(
        "SAT-P2-M2E-Q06", M, 6, "algebra", "linear_equations_two_var",
        "easy",
        r"Which of the following points lies on the graph of"
        r" $y = 5x - 8$ in the $xy$-plane?",
        {"A": r"$(0, 8)$",
         "B": r"$(1, 3)$",
         "C": r"$(2, -2)$",
         "D": r"$(2, 2)$"},
        "D",
        r"Test each point in the equation. At $x = 2$:"
        r" $$y = 5(2) - 8 = 2,$$"
        r" so $(2, 2)$ lies on the line. Choice A flips the sign of the"
        r" intercept ($y(0) = -8$, not 8), and choice B forgets the sign"
        r" of $-8$ at $x = 1$ ($y = -3$, not 3)."
        r" The correct answer is **D**.",
        ["Eq(5*2 - 8, 2)", "Ne(5*0 - 8, 8)", "Ne(5*1 - 8, 3)",
         "Ne(5*2 - 8, -2)"]))

    # Q7 E adv equivalent_expressions — coefficient a = 2, SPR
    diff = expand((5*x**2 - 2*x + 1) - (3*x**2 - 2*x + 7))
    assert diff == 2*x**2 - 6
    qs.append(spr(
        "SAT-P2-M2E-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "easy",
        r"$$(5x^2 - 2x + 1) - (3x^2 - 2x + 7) = ax^2 + b$$"
        r" The equation above is true for all values of $x$, where $a$"
        r" and $b$ are constants. What is the value of $a$?",
        ["2"],
        r"Subtract like terms: the $x^2$-terms give $5 - 3 = 2$, the"
        r" $x$-terms cancel ($-2x + 2x = 0$), and the constants give"
        r" $1 - 7 = -6$:"
        r" $$2x^2 - 6.$$"
        r" So $a = 2$ (and $b = -6$)."
        r" The correct answer is **2**.",
        ["Eq(expand((5*x**2 - 2*x + 1) - (3*x**2 - 2*x + 7)), 2*x**2 - 6)",
         "Eq(5 - 3, 2)"]))

    # Q8 E geo area_volume — cylinder volume 80π (C), FIGURE
    r_, h_ = 4, 5
    assert r_**2 * h_ == 80
    qs.append(mcq_listed(
        "SAT-P2-M2E-Q08", M, 8, "geometry_trig", "area_volume", "easy",
        r"The right circular cylinder shown has a base radius of 4 and a"
        r" height of 5. What is the volume of the cylinder?",
        {"A": r"$20\pi$",
         "B": r"$40\pi$",
         "C": r"$80\pi$",
         "D": r"$320\pi$"},
        "C",
        r"The volume of a cylinder is the base area times the height:"
        r" $$V = \pi r^2 h = \pi (4^2)(5) = 80\pi.$$"
        r" Choice A forgets to square the radius ($\pi \cdot 4 \cdot 5$);"
        r" choice B is the lateral surface area $2\pi r h$."
        r" The correct answer is **C**.",
        ["Eq(pi*4**2*5, 80*pi)", "Eq(2*pi*4*5, 40*pi)"],
        fig=figure("sat-p2-m2e-q08",
                   "Right circular cylinder with base radius labeled 4 "
                   "and height labeled 5.")))

    # Q9 M alg systems — tickets, adults 5 (B)
    a_val = Fraction(80 - 5 * 12, 4)
    assert a_val == 5 and 9 * 5 + 5 * 7 == 80
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"A theater sold 12 tickets for a total of \$80. Adult tickets"
        r" cost \$9 each and child tickets cost \$5 each. How many adult"
        r" tickets were sold?",
        r"With $a$ adult and $c$ child tickets: $a + c = 12$ and"
        r" $9a + 5c = 80$. Substitute $c = 12 - a$:"
        r" $$9a + 5(12 - a) = 80 \;\Rightarrow\; 4a + 60 = 80"
        r" \;\Rightarrow\; a = 5.$$"
        r" Check: $9(5) + 5(7) = 80$. ✓ Choice C is the number of CHILD"
        r" tickets."
        r" The correct answer is **B**.",
        ["Eq((80 - 5*12)/4, 5)", "Eq(9*5 + 5*7, 80)", "Eq(5 + 7, 12)"],
        int(a_val), {4: "coefficient echo", 7: "child tickets",
                     12: "total tickets"},
        expect_letter="B"))

    # Q10 E psda percentages — 15% of 40 = 6 (A)
    assert Fraction(15, 100) * 40 == 6
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q10", M, 10, "psda", "percentages", "easy",
        r"A server received a 15\% tip on a \$40 bill. How many dollars"
        r" was the tip?",
        r"Convert the percent and multiply:"
        r" $$0.15 \times 40 = 6.$$"
        r" Choice D misplaces the decimal point ($1.5 \times 40$);"
        r" choice B subtracts $40 - 15$."
        r" The correct answer is **A**.",
        ["Eq(Rational(15, 100)*40, 6)"],
        6, {25: "subtracted", 55: "added", 60: "decimal slip"},
        expect_letter="A"))

    # Q11 M adv nonlinear_functions — min from table −1 (A), FIGURE
    tbl = {xx: (xx - 2)**2 - 1 for xx in (-1, 0, 1, 2, 3)}
    assert list(tbl.values()) == [8, 3, 0, -1, 0]
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q11", M, 11, "advanced_math", "nonlinear_functions",
        "medium",
        r"The table shows five values of the quadratic function $g$."
        r" What is the minimum value of $g$?",
        r"The outputs fall and then rise again — the turn happens at"
        r" $x = 2$, where $g(2) = -1$; the equal outputs at $x = 1$ and"
        r" $x = 3$ confirm the symmetry around $x = 2$. The minimum"
        r" VALUE is the output $-1$, not the input 2 (choice C)."
        r" The correct answer is **A**.",
        ["Eq((2 - 2)**2 - 1, -1)", "Eq((1 - 2)**2 - 1, (3 - 2)**2 - 1)"],
        -1, {0: "nearby output", 2: "x of the minimum", 3: "g(0)"},
        fig=figure("sat-p2-m2e-q11",
                   "Table with x values -1, 0, 1, 2, 3 and g(x) values "
                   "8, 3, 0, -1, 0."),
        expect_letter="A"))

    # Q12 M psda one_var_data — combined mean 86.8, SPR
    combined = Fraction(10 * 82 + 15 * 90, 25)
    assert combined == Fraction(434, 5)
    qs.append(spr(
        "SAT-P2-M2E-Q12", M, 12, "psda", "one_var_data", "medium",
        r"In a school, 10 students in Class A have a mean test score of"
        r" 82, and 15 students in Class B have a mean test score of 90."
        r" What is the mean score of all 25 students?",
        ["86.8", "434/5"],
        r"Work with totals: Class A contributes $10 \times 82 = 820$"
        r" points and Class B contributes $15 \times 90 = 1350$, so"
        r" $$\text{mean} = \frac{820 + 1350}{25} = \frac{2170}{25}"
        r" = 86.8.$$"
        r" (Averaging 82 and 90 to get 86 is wrong because the classes"
        r" have different sizes.)"
        r" The correct answer is **86.8**.",
        ["Eq(10*82, 820)", "Eq(15*90, 1350)",
         "Eq(Rational(820 + 1350, 25), Rational(434, 5))",
         "Ne(Rational(82 + 90, 2), Rational(434, 5))"]))

    # Q13 M alg linear_inequalities — graph reads x ≥ −1 (A), FIGURE
    qs.append(mcq_listed(
        "SAT-P2-M2E-Q13", M, 13, "algebra", "linear_inequalities", "medium",
        r"The number line shows the solution set of an inequality: a"
        r" filled circle at $-1$ with shading to the right. Which"
        r" inequality has this solution set?",
        {"A": r"$x \ge -1$",
         "B": r"$x > -1$",
         "C": r"$x \le -1$",
         "D": r"$x \ge 1$"},
        "A",
        r"The ray points right, so the solutions are numbers GREATER"
        r" than the endpoint, and the FILLED circle means $-1$ itself is"
        r" included: $x \ge -1$. Choice B would need an open circle;"
        r" choice C shades the wrong direction."
        r" The correct answer is **A**.",
        ["0 >= -1", "Eq(-1, -1)"],
        fig=figure("sat-p2-m2e-q13",
                   "Number line from -5 to 5 with a filled circle at -1 "
                   "and an arrow shading all numbers to the right.")))

    # Q14 M adv equivalent_expressions — vertex-revealing form (B)
    assert expand((x - 3)**2 - 1) == expand((x - 2)*(x - 4)) == x**2 - 6*x + 8
    qs.append(mcq_listed(
        "SAT-P2-M2E-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "medium",
        r"The graph of $y = x^2 - 6x + 8$ is a parabola in the"
        r" $xy$-plane. Which equivalent form of the equation displays the"
        r" coordinates of the vertex of the parabola as constants or"
        r" coefficients?",
        {"A": r"$y = (x - 2)(x - 4)$",
         "B": r"$y = (x - 3)^2 - 1$",
         "C": r"$y = x(x - 6) + 8$",
         "D": r"$y = x^2 - 6x + 8$"},
        "B",
        r"Vertex form $y = (x - h)^2 + k$ shows the vertex $(h, k)$"
        r" directly: $$y = (x - 3)^2 - 1$$ displays the vertex $(3, -1)$."
        r" Both forms expand to $x^2 - 6x + 8$, but choice A displays the"
        r" $x$-INTERCEPTS (2 and 4), not the vertex."
        r" The correct answer is **B**.",
        ["Eq(expand((x - 3)**2 - 1), x**2 - 6*x + 8)",
         "Eq(expand((x - 2)*(x - 4)), x**2 - 6*x + 8)",
         "Eq((2 + 4)/2, 3)", "Eq((3 - 3)**2 - 1, -1)"]))

    # Q15 M adv nonlinear_equations_systems — positive root 3, SPR
    roots = _solve(Eq(x**2 + 5*x - 24, 0), x)
    assert set(roots) == {-8, 3}
    qs.append(spr(
        "SAT-P2-M2E-Q15", M, 15, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"What is the positive solution to the equation"
        r" $x^2 + 5x - 24 = 0$?",
        ["3"],
        r"Look for two numbers with product $-24$ and sum $5$: they are"
        r" $8$ and $-3$:"
        r" $$x^2 + 5x - 24 = (x + 8)(x - 3) = 0,$$"
        r" so $x = -8$ or $x = 3$; the positive solution is 3."
        r" The correct answer is **3**.",
        ["Eq(expand((x + 8)*(x - 3)), x**2 + 5*x - 24)",
         "Eq(3**2 + 5*3 - 24, 0)"]))

    # Q16 E alg linear_functions — proportional k = 2.5 (B)
    k_val = Fraction(10, 4)
    assert k_val == Fraction(5, 2)
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q16", M, 16, "algebra", "linear_functions", "easy",
        r"The line $y = kx$, where $k$ is a constant, passes through the"
        r" point $(4, 10)$ in the $xy$-plane. What is the value of $k$?",
        r"Substitute the point:"
        r" $$10 = 4k \;\Rightarrow\; k = \frac{10}{4} = 2.5.$$"
        r" Choice A inverts the ratio ($4/10$); choice C subtracts the"
        r" coordinates."
        r" The correct answer is **B**.",
        ["Eq(Rational(10, 4), Rational(5, 2))",
         "Eq(Rational(5, 2)*4, 10)"],
        k_val, {Fraction(2, 5): "inverted ratio", 6: "subtracted",
                40: "multiplied"},
        fmt=lambda v: f"${float(Fraction(v)):g}$",
        expect_letter="B"))

    # Q17 M geo right_triangles_trig — cos θ = 12/13 (C), FIGURE
    assert 5**2 + 12**2 == 13**2
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q17", M, 17, "geometry_trig", "right_triangles_trig",
        "medium",
        r"In the right triangle shown, the angle $\theta$ is between the"
        r" side of length 12 and the hypotenuse of length 13; the side"
        r" opposite $\theta$ has length 5. What is the value of"
        r" $\cos \theta$?",
        r"Cosine is adjacent over hypotenuse. The side of length 12 is"
        r" adjacent to $\theta$:"
        r" $$\cos \theta = \frac{12}{13}.$$"
        r" Choice A is $\sin \theta$ (opposite over hypotenuse), and"
        r" choice B is $\tan \theta$."
        r" The correct answer is **C**.",
        ["Eq(5**2 + 12**2, 13**2)",
         "Rational(5, 13) < Rational(5, 12)",
         "Rational(5, 12) < Rational(12, 13)"],
        Fraction(12, 13), {Fraction(5, 13): "sine",
                           Fraction(5, 12): "tangent",
                           Fraction(13, 12): "inverted"},
        fmt=lambda v: frac(v),
        fig=figure("sat-p2-m2e-q17",
                   "Right triangle with horizontal leg 12, vertical leg "
                   "5, hypotenuse 13, right angle where the legs meet, "
                   "and angle theta marked between the leg of length 12 "
                   "and the hypotenuse."),
        expect_letter="C"))

    # Q18 M adv nonlinear_functions — 18% decrease (B)
    assert Fraction(100, 100) - Fraction(82, 100) == Fraction(18, 100)
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q18", M, 18, "advanced_math", "nonlinear_functions",
        "medium",
        r"The value of a car $t$ years after purchase is modeled by"
        r" $V(t) = 12{,}000(0.82)^t$ dollars. By what percent does the"
        r" value of the car decrease each year?",
        r"Each year the value is MULTIPLIED by 0.82, which means it"
        r" keeps 82\% of its value and loses the rest:"
        r" $$1 - 0.82 = 0.18 = 18\%.$$"
        r" Choice C reads 0.82 itself as the loss; choice A misplaces"
        r" the decimal."
        r" The correct answer is **B**.",
        ["Eq(1 - Rational(82, 100), Rational(18, 100))"],
        18, {Fraction(41, 5): "decimal slip", 82: "kept share",
             118: "added"},
        fmt=lambda v: f"${float(Fraction(v)):g}\\%$",
        expect_letter="B"))

    # Q19 E alg two_var — x-intercept 7, SPR
    assert Fraction(21, 3) == 7
    qs.append(spr(
        "SAT-P2-M2E-Q19", M, 19, "algebra", "linear_equations_two_var",
        "easy",
        r"The graph of $3x + 4y = 21$ in the $xy$-plane crosses the"
        r" $x$-axis at the point $(a, 0)$. What is the value of $a$?",
        ["7"],
        r"On the $x$-axis, $y = 0$:"
        r" $$3a + 4(0) = 21 \;\Rightarrow\; a = 7.$$"
        r" The correct answer is **7**.",
        ["Eq(3*7 + 4*0, 21)"]))

    # Q20 M adv nonlinear_functions — composition f(g(3)) = 19 (C)
    g3 = 3**2
    fg3 = 2 * g3 + 1
    assert (g3, fg3) == (9, 19)
    qs.append(mcq_numeric(
        "SAT-P2-M2E-Q20", M, 20, "advanced_math", "nonlinear_functions",
        "medium",
        r"The functions $f$ and $g$ are defined by $f(x) = 2x + 1$ and"
        r" $g(x) = x^2$. What is the value of $f(g(3))$?",
        r"Work inside out: $g(3) = 9$ first, then"
        r" $$f(9) = 2(9) + 1 = 19.$$"
        r" Choice D composes in the wrong order —"
        r" $g(f(3)) = g(7) = 49$; choice B stops at $g(3)$."
        r" The correct answer is **C**.",
        ["Eq(3**2, 9)", "Eq(2*9 + 1, 19)", "Eq((2*3 + 1)**2, 49)"],
        fg3, {7: "f(3) first, stopped", 9: "stopped at g(3)",
              49: "reversed order"},
        expect_letter="C"))

    # Q21 H alg systems — which system models it (A)
    # the modeled system's actual solution: a = 95 adults, s = 165 students
    assert 95 + 165 == 260 and 11 * 95 + 7 * 165 == 2200
    qs.append(mcq_listed(
        "SAT-P2-M2E-Q21", M, 21, "algebra", "systems_two_linear", "hard",
        r"A cinema sold 260 tickets one evening for a total of \$2{,}200."
        r" Adult tickets cost \$11 each and student tickets cost \$7"
        r" each. If $a$ is the number of adult tickets and $s$ is the"
        r" number of student tickets, which system of equations models"
        r" this situation?",
        {"A": r"$a + s = 260$ and $11a + 7s = 2200$",
         "B": r"$a + s = 2200$ and $11a + 7s = 260$",
         "C": r"$a + s = 260$ and $7a + 11s = 2200$",
         "D": r"$11a + 7s = 260$ and $18(a + s) = 2200$"},
        "A",
        r"Counts add to the ticket total: $a + s = 260$. Money adds to"
        r" the revenue, each ticket weighted by ITS price:"
        r" $$11a + 7s = 2200.$$"
        r" Choice B swaps the two totals; choice C attaches each price"
        r" to the wrong ticket type."
        r" The correct answer is **A**.",
        ["Eq(95 + 165, 260)", "Eq(11*95 + 7*165, 2200)"]))

    # Q22 H adv nonlinear_equations_systems — factor theorem c = 6, SPR
    c_val = -(2**3 - 4 * 2**2 + 2)
    assert c_val == 6 and 2**3 - 4*2**2 + 2 + 6 == 0
    qs.append(spr(
        "SAT-P2-M2E-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$p(x) = x^3 - 4x^2 + x + c$$"
        r" In the polynomial above, $c$ is a constant. If $x - 2$ is a"
        r" factor of $p(x)$, what is the value of $c$?",
        ["6"],
        r"By the factor theorem, $x - 2$ is a factor exactly when"
        r" $p(2) = 0$:"
        r" $$2^3 - 4(2^2) + 2 + c = 8 - 16 + 2 + c = c - 6 = 0,$$"
        r" so $c = 6$."
        r" The correct answer is **6**.",
        ["Eq(2**3 - 4*2**2 + 2 + 6, 0)", "Eq(8 - 16 + 2, -6)"]))

    return qs


def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg one_var — 7x + 3 = 31 (D)
    x_val = Fraction(24 + 4, 7)
    assert x_val == 4 and 7 * 4 + 3 == 31
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $7x - 4 = 24$, what is the value of $7x + 3$?",
        r"No need to solve for $x$: the left side just grows by 7,"
        r" since $(7x + 3) - (7x - 4) = 7$:"
        r" $$7x + 3 = 24 + 7 = 31.$$"
        r" (Directly: $7x = 28$, so $7x + 3 = 31$.) Choice A solves for"
        r" $x = 4$ and stops; choice C stops at $7x = 28$."
        r" The correct answer is **D**.",
        ["Eq((24 + 4)/7, 4)", "Eq(7*4 + 3, 31)", "Eq(24 + 7, 31)"],
        31, {4: "solved for x", 21: "24 - 3", 28: "stopped at 7x"},
        expect_letter="D"))

    # Q2 M geo transversal with algebra — x = 25 (C), FIGURE
    x_val = Fraction(180 - 30, 6)
    assert x_val == 25 and 4*25 + (2*25 + 30) == 180
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q02", M, 2, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In the figure, lines $\ell$ and $m$ are parallel and are cut by"
        r" a transversal. The two same-side interior angles measure"
        r" $(4x)°$ and $(2x + 30)°$. What is the value of $x$?",
        r"Same-side interior angles are supplementary:"
        r" $$4x + (2x + 30) = 180 \;\Rightarrow\; 6x = 150"
        r" \;\Rightarrow\; x = 25.$$"
        r" Check: the angles are $100°$ and $80°$, which do sum to"
        r" $180°$. Choice B (15) comes from setting the angles EQUAL —"
        r" the rule for alternate interior angles, not same-side."
        r" The correct answer is **C**.",
        ["Eq((180 - 30)/6, 25)", "Eq(4*25 + 2*25 + 30, 180)",
         "Eq((30 - 0)/2, 15)"],
        int(x_val), {10: "used 90", 15: "set angles equal",
                     35: "sign slip on 30"},
        fig=figure("sat-p2-m2h-q02",
                   "Two parallel horizontal lines l and m cut by a "
                   "transversal; the same-side interior angle at line l "
                   "is labeled (4x) degrees and the one at line m is "
                   "labeled (2x + 30) degrees."),
        expect_letter="C"))

    # Q3 E alg linear_functions — f(−2) = 11, SPR
    assert -3 * (-2) + 5 == 11
    qs.append(spr(
        "SAT-P2-M2H-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = -3x + 5$. What is the"
        r" value of $f(-2)$?",
        ["11"],
        r"Substitute carefully — a negative times a negative:"
        r" $$f(-2) = -3(-2) + 5 = 6 + 5 = 11.$$"
        r" The correct answer is **11**.",
        ["Eq(-3*(-2) + 5, 11)"]))

    # Q4 H psda one_var_data — IQR from box plot 18 (B), FIGURE
    mn, q1, med, q3, mx = 12, 20, 28, 38, 50
    iqr = q3 - q1
    assert iqr == 18
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q04", M, 4, "psda", "one_var_data", "hard",
        r"The box plot summarizes the distribution of the number of"
        r" minutes 40 students spent on homework. What is the"
        r" interquartile range (IQR) of the distribution?",
        r"The IQR is the width of the BOX — the third quartile minus the"
        r" first quartile:"
        r" $$\text{IQR} = 38 - 20 = 18.$$"
        r" Choice D is the full range ($50 - 12$), whisker to whisker;"
        r" choice C is the median, the line inside the box."
        r" The correct answer is **B**.",
        ["Eq(38 - 20, 18)", "Eq(50 - 12, 38)"],
        iqr, {12: "min echo", 28: "median", 38: "range"},
        fig=figure("sat-p2-m2h-q04",
                   "Box plot over a number line from 10 to 50: whiskers "
                   "at 12 and 50, box from 20 to 38, median line at 28. "
                   "Axis labeled minutes."),
        expect_letter="B"))

    # Q5 M adv nonlinear_functions — x-intercepts of 2|x−1|−6 (C), FIGURE
    assert 2 * abs(4 - 1) - 6 == 0 and 2 * abs(-2 - 1) - 6 == 0
    qs.append(mcq_listed(
        "SAT-P2-M2H-Q05", M, 5, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph of $y = 2|x - 1| - 6$ is shown. What are the"
        r" $x$-intercepts of the graph?",
        {"A": r"$x = -5$ and $x = 7$",
         "B": r"$x = -4$ and $x = 2$",
         "C": r"$x = -2$ and $x = 4$",
         "D": r"$x = 1$ and $x = -6$"},
        "C",
        r"Set $y = 0$ and isolate the absolute value:"
        r" $$2|x - 1| = 6 \;\Rightarrow\; |x - 1| = 3 \;\Rightarrow\;"
        r" x - 1 = \pm 3,$$"
        r" so $x = 4$ or $x = -2$. Choice A forgets to divide by 2"
        r" ($|x-1| = 6$); choice D just reads the vertex $(1, -6)$."
        r" The correct answer is **C**.",
        ["Eq(2*Abs(4 - 1) - 6, 0)", "Eq(2*Abs(-2 - 1) - 6, 0)",
         "Ne(2*Abs(7 - 1) - 6, 0)"],
        fig=figure("sat-p2-m2h-q05",
                   "V-shaped absolute value graph with vertex at "
                   "(1, -6), rising with slope 2 on each side and "
                   "crossing the x-axis at -2 and 4.")))

    # Q6 M alg two_var — y-intercept 3 (B)
    slope = Fraction(-5 - 7, 4 - (-2))
    b_val = 7 - slope * (-2)
    assert (slope, b_val) == (-2, 3)
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q06", M, 6, "algebra", "linear_equations_two_var",
        "medium",
        r"A line in the $xy$-plane passes through the points $(-2, 7)$"
        r" and $(4, -5)$. What is the $y$-coordinate of the line's"
        r" $y$-intercept?",
        r"The slope is"
        r" $$\frac{-5 - 7}{4 - (-2)} = \frac{-12}{6} = -2.$$"
        r" Then from $(-2, 7)$: $y = -2x + b$ gives"
        r" $7 = -2(-2) + b = 4 + b$, so $b = 3$. Choice A is the slope"
        r" itself; choice D reuses the given $y$-value 7; choice C uses"
        r" slope $+2$ ($7 = 2(-2) + b \Rightarrow b = 11$)."
        r" The correct answer is **B**.",
        ["Eq(Rational(-5 - 7, 4 + 2), -2)", "Eq(-2*(-2) + 3, 7)",
         "Eq(-2*4 + 3, -5)"],
        int(b_val), {-2: "the slope", 7: "echoed y-value",
                     11: "sign-slipped slope"},
        expect_letter="B"))

    # Q7 H adv equivalent_expressions — b = 16, SPR
    assert expand((x + 8)**2) == x**2 + 16*x + 64
    qs.append(spr(
        "SAT-P2-M2H-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "hard",
        r"$$(x + a)^2 = x^2 + bx + 64$$"
        r" In the equation above, $a$ and $b$ are positive constants. If"
        r" the equation is true for all values of $x$, what is the value"
        r" of $b$?",
        ["16"],
        r"Expanding, $(x + a)^2 = x^2 + 2ax + a^2$. Matching constants:"
        r" $a^2 = 64$, and $a$ is positive, so $a = 8$. Matching the"
        r" $x$-coefficients:"
        r" $$b = 2a = 16.$$"
        r" The correct answer is **16**.",
        ["Eq(expand((x + 8)**2), x**2 + 16*x + 64)", "Eq(8**2, 64)",
         "Eq(2*8, 16)"]))

    # Q8 H geo area_volume — volume from circumference 360π (C), FIGURE
    r_ = Fraction(12, 2)          # circumference 12π → r = 6
    vol_over_pi = r_**2 * 10
    assert vol_over_pi == 360
    qs.append(mcq_listed(
        "SAT-P2-M2H-Q08", M, 8, "geometry_trig", "area_volume", "hard",
        r"The circumference of the base of the right circular cylinder"
        r" shown is $12\pi$, and the height of the cylinder is 10. What"
        r" is the volume of the cylinder?",
        {"A": r"$60\pi$",
         "B": r"$120\pi$",
         "C": r"$360\pi$",
         "D": r"$1440\pi$"},
        "C",
        r"Recover the radius from the circumference first:"
        r" $$2\pi r = 12\pi \;\Rightarrow\; r = 6,$$"
        r" then $V = \pi r^2 h = \pi(36)(10) = 360\pi$. Choice B"
        r" multiplies the circumference by the height (that is the"
        r" LATERAL AREA, $12\pi \cdot 10$); choice D squares the 12"
        r" as if it were the radius."
        r" The correct answer is **C**.",
        ["Eq(Rational(12, 2), 6)", "Eq(6**2*10, 360)", "Eq(12*10, 120)",
         "Eq(12**2*10, 1440)"],
        fig=figure("sat-p2-m2h-q08",
                   "Right circular cylinder with height labeled 10; the "
                   "caption under the base reads circumference 12 pi.")))

    # Q9 H alg systems — decimals, y = 12 (C)
    x_val = Fraction(7 - Fraction(1, 4) * 20, Fraction(1, 4))
    y_val = 20 - x_val
    assert (x_val, y_val) == (8, 12)
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q09", M, 9, "algebra", "systems_two_linear", "hard",
        r"$$0.5x + 0.25y = 7$$ $$x + y = 20$$"
        r" If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $y$?",
        r"Substitute $y = 20 - x$ into the first equation:"
        r" $$0.5x + 0.25(20 - x) = 7 \;\Rightarrow\; 0.25x + 5 = 7"
        r" \;\Rightarrow\; x = 8,$$"
        r" so $y = 20 - 8 = 12$. Check: $0.5(8) + 0.25(12) = 4 + 3 = 7$."
        r" ✓ Choice B is the value of $x$. (Desmos: graph both and read"
        r" the intersection.)"
        r" The correct answer is **C**.",
        ["Eq(Rational(1,2)*8 + Rational(1,4)*12, 7)", "Eq(8 + 12, 20)",
         "Eq(Rational(2, Rational(1,4)), 8)"],
        int(y_val), {4: "0.25x value x2", 8: "the value of x",
                     20: "the total"},
        expect_letter="C"))

    # Q10 M psda percentages — up 20% then down 20% (B)
    net = Fraction(120, 100) * Fraction(80, 100)
    assert net == Fraction(24, 25)
    qs.append(mcq_listed(
        "SAT-P2-M2H-Q10", M, 10, "psda", "percentages", "medium",
        r"The price of a stock increased by 20\% in one month and then"
        r" decreased by 20\% the next month. Compared with the original"
        r" price, the final price is",
        {"A": r"40\% lower",
         "B": r"4\% lower",
         "C": r"exactly the same",
         "D": r"4\% higher"},
        "B",
        r"Percent changes MULTIPLY, they don't cancel:"
        r" $$1.20 \times 0.80 = 0.96,$$"
        r" which is 96\% of the original — a 4\% decrease. The second"
        r" change is 20\% of a LARGER number, so it removes more than"
        r" the first change added. Choice C is the classic trap."
        r" The correct answer is **B**.",
        ["Eq(Rational(120, 100)*Rational(80, 100), Rational(96, 100))",
         "Eq(1 - Rational(96, 100), Rational(4, 100))"]))

    # Q11 H adv nonlinear_functions — h(10) = 17 from table (C), FIGURE
    def h(v):
        return Fraction(1, 2) * (v - 4)**2 - 1
    assert [h(v) for v in (0, 2, 4, 6, 8)] == [7, 1, -1, 1, 7]
    assert h(10) == 17
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q11", M, 11, "advanced_math", "nonlinear_functions",
        "hard",
        r"The table shows five values of the quadratic function $h$."
        r" What is the value of $h(10)$?",
        r"The equal outputs at $x = 2, 6$ and at $x = 0, 8$ show the"
        r" axis of symmetry is $x = 4$, so"
        r" $h(x) = a(x - 4)^2 - 1$. From $h(0) = 7$:"
        r" $$16a - 1 = 7 \;\Rightarrow\; a = \tfrac{1}{2}.$$"
        r" Then $$h(10) = \tfrac{1}{2}(36) - 1 = 17.$$"
        r" Choice B continues the last visible step linearly"
        r" ($1 \to 7$ suggests $+6$ per 2 units → 13) — but a quadratic"
        r" accelerates; choice D uses $a = 1$."
        r" The correct answer is **C**.",
        ["Eq(Rational(1,2)*(0 - 4)**2 - 1, 7)",
         "Eq(Rational(1,2)*(2 - 4)**2 - 1, 1)",
         "Eq(Rational(1,2)*(10 - 4)**2 - 1, 17)"],
        17, {7: "symmetry misread", 13: "linear extension",
             35: "used a = 1"},
        fig=figure("sat-p2-m2h-q11",
                   "Table with x values 0, 2, 4, 6, 8 and h(x) values "
                   "7, 1, -1, 1, 7."),
        expect_letter="C"))

    # Q12 H psda one_var_data — x = 19.5, SPR
    x_val = Fraction(7 * 18 - 5 * 16 - 7, 2)
    assert x_val == Fraction(39, 2)
    qs.append(spr(
        "SAT-P2-M2H-Q12", M, 12, "psda", "one_var_data", "hard",
        r"The mean of a list of 5 numbers is 16. When two more numbers,"
        r" $x$ and $x + 7$, are added to the list, the mean of the"
        r" resulting 7 numbers is 18. What is the value of $x$?",
        ["19.5", "39/2"],
        r"Totals again: the 5 numbers sum to $5 \cdot 16 = 80$, and the"
        r" 7 numbers must sum to $7 \cdot 18 = 126$. So"
        r" $$x + (x + 7) = 126 - 80 = 46 \;\Rightarrow\; 2x = 39"
        r" \;\Rightarrow\; x = 19.5.$$"
        r" The correct answer is **19.5** (or 39/2).",
        ["Eq(5*16, 80)", "Eq(7*18, 126)",
         "Eq(Rational(126 - 80 - 7, 2), Rational(39, 2))"]))

    # Q13 M alg linear_inequalities — open dot at 2, ray left (A), FIGURE
    assert Fraction(-2 - 4, -3) == 2
    qs.append(mcq_listed(
        "SAT-P2-M2H-Q13", M, 13, "algebra", "linear_inequalities", "medium",
        r"The number line shows the solution set of an inequality: an"
        r" open circle at $2$ with shading to the left. Which inequality"
        r" has this solution set?",
        {"A": r"$-3x + 4 > -2$",
         "B": r"$-3x + 4 < -2$",
         "C": r"$-3x + 4 \ge -2$",
         "D": r"$3x + 4 > -2$"},
        "A",
        r"The graph says $x < 2$, strictly (open circle). Solve choice"
        r" A: $-3x > -6$, and dividing by $-3$ flips the sign:"
        r" $$x < 2. ✓$$"
        r" Choice C gives $x \le 2$ — a CLOSED circle; choice D gives"
        r" $x > -2$."
        r" The correct answer is **A**.",
        ["Eq(Rational(-6, -3), 2)", "-3*1 + 4 > -2", "-3*3 + 4 < -2"],
        fig=figure("sat-p2-m2h-q13",
                   "Number line from -3 to 6 with an open circle at 2 "
                   "and an arrow shading all numbers to the left.")))

    # Q14 H adv equivalent_expressions — minimum −6 (A)
    e = expand(2*(x + 4)**2 - 6)
    assert e == 2*x**2 + 16*x + 26
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "hard",
        r"$$y = 2x^2 + 16x + 26$$"
        r" The equation above can be rewritten in the form"
        r" $y = a(x + h)^2 + k$. What is the minimum value of $y$?",
        r"Complete the square, factoring the 2 out of the $x$-terms"
        r" first:"
        r" $$y = 2(x^2 + 8x) + 26 = 2\big[(x + 4)^2 - 16\big] + 26"
        r" = 2(x + 4)^2 - 6.$$"
        r" The square is at least 0, so the minimum is $-6$ (at"
        r" $x = -4$). Choice B is the $x$-coordinate of the vertex;"
        r" choice D is the $y$-intercept."
        r" The correct answer is **A**.",
        ["Eq(expand(2*(x + 4)**2 - 6), 2*x**2 + 16*x + 26)",
         "Eq(2*(-4)**2 + 16*(-4) + 26, -6)"],
        -6, {-4: "x of vertex", 6: "sign slip", 26: "y-intercept"},
        expect_letter="A"))

    # Q15 H adv nonlinear_equations_systems — Vieta c = 18, SPR
    # roots r = 2s with r + s = 9 → s = 3, r = 6, c = rs
    s_v = Fraction(9, 3)
    c_val = 2 * s_v * s_v
    assert c_val == 18 and expand((x - 3)*(x - 6)) == x**2 - 9*x + 18
    qs.append(spr(
        "SAT-P2-M2H-Q15", M, 15, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$x^2 - 9x + c = 0$$"
        r" In the equation above, $c$ is a constant. The equation has two"
        r" solutions, and one solution is twice the other. What is the"
        r" value of $c$?",
        ["18"],
        r"Call the solutions $s$ and $2s$. Their SUM is the negative of"
        r" the $x$-coefficient: $s + 2s = 9$, so $s = 3$ and the"
        r" solutions are 3 and 6. Their PRODUCT is the constant:"
        r" $$c = 3 \cdot 6 = 18.$$"
        r" Check: $x^2 - 9x + 18 = (x - 3)(x - 6)$. ✓"
        r" The correct answer is **18**.",
        ["Eq(Rational(9, 3), 3)", "Eq(3*6, 18)",
         "Eq(expand((x - 3)*(x - 6)), x**2 - 9*x + 18)"]))

    # Q16 M alg linear_functions — slope 3 (A)
    assert Fraction(9, 3) == 3
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q16", M, 16, "algebra", "linear_functions", "medium",
        r"For the linear function $f$, $f(4) - f(1) = 9$. What is the"
        r" slope of the graph of $f$ in the $xy$-plane?",
        r"The slope is the change in output over the change in input:"
        r" $$m = \frac{f(4) - f(1)}{4 - 1} = \frac{9}{3} = 3.$$"
        r" Choice B is the raw difference 9 without dividing by the run;"
        r" the function's intercept cannot be determined, but the slope"
        r" can."
        r" The correct answer is **A**.",
        ["Eq(Rational(9, 4 - 1), 3)"],
        3, {9: "forgot the run", 27: "multiplied by 3",
            36: "multiplied by 4"},
        expect_letter="A"))

    # Q17 H geo right_triangles_trig — tan θ = 3/4 (B), FIGURE
    assert 15**2 + 20**2 == 25**2
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q17", M, 17, "geometry_trig", "right_triangles_trig",
        "hard",
        r"In the right triangle shown, the hypotenuse has length 25 and"
        r" the side opposite angle $\theta$ has length 15. What is the"
        r" value of $\tan \theta$?",
        r"First find the missing adjacent side with the Pythagorean"
        r" theorem:"
        r" $$\sqrt{25^2 - 15^2} = \sqrt{625 - 225} = \sqrt{400} = 20.$$"
        r" Then $$\tan \theta = \frac{\text{opposite}}{\text{adjacent}}"
        r" = \frac{15}{20} = \frac{3}{4}.$$"
        r" Choice A is $\sin \theta = \frac{15}{25}$; choice C is"
        r" $\cos \theta = \frac{20}{25}$."
        r" The correct answer is **B**.",
        ["Eq(sqrt(25**2 - 15**2), 20)",
         "Eq(Rational(15, 20), Rational(3, 4))",
         "Rational(3, 5) < Rational(3, 4)"],
        Fraction(3, 4), {Fraction(3, 5): "sine",
                         Fraction(4, 5): "cosine",
                         Fraction(4, 3): "inverted"},
        fmt=lambda v: frac(v),
        fig=figure("sat-p2-m2h-q17",
                   "Right triangle with hypotenuse labeled 25 and "
                   "vertical leg labeled 15 opposite the marked angle "
                   "theta; the horizontal leg is unlabeled."),
        expect_letter="B"))

    # Q18 H adv nonlinear_functions — 5% every 3 months (B)
    assert Fraction(105, 100)**1 == Fraction(105, 100)
    qs.append(mcq_listed(
        "SAT-P2-M2H-Q18", M, 18, "advanced_math", "nonlinear_functions",
        "hard",
        r"A savings account balance is modeled by"
        r" $B(t) = 8{,}000(1.05)^{4t}$ dollars, where $t$ is the time in"
        r" YEARS. Which statement best describes the growth of the"
        r" balance?",
        {"A": r"It increases by 5\% once each year.",
         "B": r"It increases by 5\% every 3 months.",
         "C": r"It increases by 5\% every 4 years.",
         "D": r"It increases by 20\% once each year."},
        "B",
        r"Write the exponent as a count of periods: $4t$ reaches 1 when"
        r" $t = \frac{1}{4}$ year — every 3 months the balance is"
        r" multiplied by 1.05, a 5\% increase. Choice D adds the four"
        r" quarterly increases as if percents were additive; the true"
        r" yearly factor is $(1.05)^4 \approx 1.216$, about 21.6\%."
        r" The correct answer is **B**.",
        ["Eq(Rational(105, 100)**(4*Rational(1, 4)), Rational(105, 100))",
         "Rational(105, 100)**4 > Rational(120, 100)"]))

    # Q19 M alg two_var — y-intercept −2, SPR (negative answer)
    assert Fraction(10, -5) == -2
    qs.append(spr(
        "SAT-P2-M2H-Q19", M, 19, "algebra", "linear_equations_two_var",
        "medium",
        r"The graph of $2x - 5y = 10$ in the $xy$-plane crosses the"
        r" $y$-axis at the point $(0, b)$. What is the value of $b$?",
        ["-2"],
        r"On the $y$-axis, $x = 0$:"
        r" $$2(0) - 5b = 10 \;\Rightarrow\; b = \frac{10}{-5} = -2.$$"
        r" (Watch the sign — the $-5y$ makes the intercept negative.)"
        r" The correct answer is **-2**.",
        ["Eq(2*0 - 5*(-2), 10)"]))

    # Q20 H adv nonlinear_functions — nested constant b = 2 (B)
    b_sym = symbols("b")
    sol_b = _solve(Eq(3*(3*2 - b_sym) - b_sym, 10), b_sym)
    assert sol_b == [2]
    qs.append(mcq_numeric(
        "SAT-P2-M2H-Q20", M, 20, "advanced_math", "nonlinear_functions",
        "hard",
        r"The function $f$ is defined by $f(x) = 3x - b$, where $b$ is a"
        r" constant. If $f(f(2)) = 10$, what is the value of $b$?",
        r"Build the composition from the inside:"
        r" $f(2) = 6 - b$, so"
        r" $$f(f(2)) = 3(6 - b) - b = 18 - 4b = 10 \;\Rightarrow\;"
        r" 4b = 8 \;\Rightarrow\; b = 2.$$"
        r" Check: $f(2) = 4$ and $f(4) = 10$. ✓ Choice D stops at"
        r" $4b = 8$ and reports 8."
        r" The correct answer is **B**.",
        ["Eq(3*(3*2 - 2) - 2, 10)", "Eq(3*2 - 2, 4)", "Eq(3*4 - 2, 10)"],
        2, {-2: "sign slip", 6: "f(2) with b = 0", 8: "stopped at 4b"},
        expect_letter="B"))

    # Q21 H alg systems — mixture setup (A)
    # the modeled mixture system's actual solution: x = 12, y = 8
    assert Fraction(30, 100)*12 + Fraction(55, 100)*8 == 8
    qs.append(mcq_listed(
        "SAT-P2-M2H-Q21", M, 21, "algebra", "systems_two_linear", "hard",
        r"A chemist mixes $x$ liters of a 30\% acid solution with $y$"
        r" liters of a 55\% acid solution to produce 20 liters of a 40\%"
        r" acid solution. Which system of equations models this"
        r" situation?",
        {"A": r"$x + y = 20$ and $0.30x + 0.55y = 0.40(20)$",
         "B": r"$x + y = 20$ and $0.30x + 0.55y = 0.40$",
         "C": r"$x + y = 0.40(20)$ and $0.30x + 0.55y = 20$",
         "D": r"$x + y = 20$ and $0.55x + 0.30y = 0.40(20)$"},
        "A",
        r"Volumes add: $x + y = 20$. Pure acid also adds: the first"
        r" solution contributes $0.30x$ liters of acid, the second"
        r" $0.55y$, and the mixture contains $0.40 \times 20 = 8$"
        r" liters:"
        r" $$0.30x + 0.55y = 8.$$"
        r" Choice B equates liters of acid with a unitless 0.40; choice"
        r" D attaches each concentration to the wrong solution."
        r" The correct answer is **A**.",
        ["Eq(Rational(40, 100)*20, 8)",
         "Eq(Rational(30,100)*12 + Rational(55,100)*8, 8)",
         "Eq(12 + 8, 20)"]))

    # Q22 H adv nonlinear_equations_systems — factor theorem c = 1, SPR
    c_sym = symbols("c")
    sol_c = _solve(Eq(2*(-2)**3 + c_sym*(-2)**2 - 5*(-2) + 2, 0), c_sym)
    assert sol_c == [1]
    qs.append(spr(
        "SAT-P2-M2H-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$p(x) = 2x^3 + cx^2 - 5x + 2$$"
        r" In the polynomial above, $c$ is a constant. If $x + 2$ is a"
        r" factor of $p(x)$, what is the value of $c$?",
        ["1"],
        r"$x + 2$ is a factor exactly when $p(-2) = 0$ — note the"
        r" opposite sign:"
        r" $$2(-8) + 4c + 10 + 2 = 4c - 4 = 0 \;\Rightarrow\; c = 1.$$"
        r" The correct answer is **1**.",
        ["Eq(2*(-2)**3 + 1*(-2)**2 - 5*(-2) + 2, 0)",
         "Eq(-16 + 4 + 10 + 2, 0)"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-2.json",
               {"testId": "sat-practice-2",
                "label": "SAT Math Practice Test 2",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
