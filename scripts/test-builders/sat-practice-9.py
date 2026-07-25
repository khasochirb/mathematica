#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 9 (data/sat/sat-practice-9.json).

Built on scripts/test-builders/satbuild.py. Archetypes audited against
tests 1-8; new to the bank here:
  * a ONE-variable equation with a parameter giving infinitely many
    solutions (the linear analogue of the system version)
  * factoring by grouping; the domain of a radical function
  * an inverse-function value read backwards from a rule
  * a regular polygon's single interior angle (not the sum)
  * the distance between two points; the volume of a pyramid
  * median from a frequency table; a sample-to-population estimate
  * an inequality whose negative coefficient forces the sign to flip
  * doubling time solved from an exponential model
  * the geometric mean in similar right triangles

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
    assert _solve(Eq(4 * x - 9, 27), x) == [9]
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $4x - 9 = 27$, what is the value of $x$?",
        r"Add 9 to both sides, then divide by 4:"
        r" $$4x = 36 \;\Rightarrow\; x = 9.$$"
        r" Subtracting 9 instead gives $4x = 18$, or $4.5$, and stopping at"
        r" $4x = 36$ gives 36."
        r" The correct answer is **C**.",
        ["Eq(4*9 - 9, 27)", "Eq((27 + 9)/4, 9)"],
        9, {Rational(9, 2): "subtracted 9 instead of adding",
            7: "divided 27 by 4 and rounded", 36: "stopped at 4x = 36"},
        fmt=smart))

    # Q2 E adv — factor by grouping
    assert expand((x + 5) * (x**2 + 3)) == x**3 + 5 * x**2 + 3 * x + 15
    qs.append(mcq_listed(
        "SAT-P9-M1-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to"
        r" $x^3 + 5x^2 + 3x + 15$?",
        {"A": r"$(x + 3)(x^2 + 5)$", "B": r"$(x + 5)(x^2 + 3)$",
         "C": r"$(x - 5)(x^2 + 3)$", "D": r"$(x^2 + 5)(x + 3)$"}, "B",
        r"Group the four terms in pairs and factor each pair:"
        r" $$x^3 + 5x^2 + 3x + 15 = x^2(x + 5) + 3(x + 5).$$"
        r" Both pairs now share the factor $x + 5$, so factor it out:"
        r" $$(x + 5)(x^2 + 3).$$"
        r" Swapping which number goes with which factor gives"
        r" $(x + 3)(x^2 + 5)$, which expands to $x^3 + 3x^2 + 5x + 15$ — check"
        r" the middle terms to tell them apart."
        r" The correct answer is **B**.",
        ["Eq(expand((x + 5)*(x**2 + 3)), x**3 + 5*x**2 + 3*x + 15)",
         "Eq(expand((x + 3)*(x**2 + 5)), x**3 + 3*x**2 + 5*x + 15)"]))

    # Q3 E psda — sample to population estimate
    assert Rational(40, 200) * 3000 == 600
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q03", M, 3, "psda", "sample_stats_margin_error", "easy",
        r"In a random sample of $200$ students at a school, $40$ said they"
        r" ride a bicycle to school. Based on this sample, which is the best"
        r" estimate of the number of the school's $3{,}000$ students who ride"
        r" a bicycle to school?",
        r"The sample proportion is"
        r" $$\frac{40}{200} = 0.2 = 20\%.$$"
        r" Applying that proportion to the whole school:"
        r" $$0.2 \times 3000 = 600.$$"
        r" Reporting the sample count gives 40, and scaling by the number of"
        r" samples rather than the proportion gives 3000 or 200."
        r" The correct answer is **C**.",
        ["Eq(Rational(40,200), Rational(1,5))",
         "Eq(Rational(1,5)*3000, 600)"],
        600, {40: "reported the sample count",
              200: "reported the sample size",
              1500: "used half the student body"}, fmt=smart))

    # Q4 SPR E alg
    assert _solve(Eq(5 * (x - 2), 3 * x), x) == [5]
    qs.append(spr(
        "SAT-P9-M1-Q04", M, 4, "algebra", "linear_equations_one_var", "easy",
        r"$$5(x - 2) = 3x$$"
        r" What is the solution to the equation above?",
        ["5"],
        r"Distribute, then gather like terms:"
        r" $$5x - 10 = 3x \;\Rightarrow\; 2x = 10 \;\Rightarrow\; x = 5.$$"
        r" Check: $5(5 - 2) = 15$ and $3(5) = 15$."
        r" The correct answer is **5**.",
        ["Eq(5*(5 - 2), 3*5)"]))

    # Q5 E geo — interior angle of a regular polygon
    assert Rational((6 - 2) * 180, 6) == 120
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q05", M, 5, "geometry_trig", "lines_angles_triangles", "easy",
        r"What is the measure, in degrees, of one interior angle of a regular"
        r" hexagon?",
        r"The interior angles of a hexagon sum to"
        r" $$(6 - 2)(180) = 720,$$"
        r" and a REGULAR polygon has all angles equal, so divide by 6:"
        r" $$\frac{720}{6} = 120.$$"
        r" Reporting the total gives 720, and $\frac{360}{6} = 60$ is one"
        r" EXTERIOR angle — its supplement, $180 - 60 = 120$, confirms the"
        r" answer."
        r" The correct answer is **C**.",
        ["Eq((6 - 2)*180, 720)", "Eq(Rational(720,6), 120)",
         "Eq(180 - Rational(360,6), 120)"],
        120, {60: "gave one exterior angle", 90: "used a square",
              720: "gave the sum of all interior angles"}, fmt=smart))

    # Q6 E adv — domain of a radical
    qs.append(mcq_listed(
        "SAT-P9-M1-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = \sqrt{x - 7}$. What is the"
        r" domain of $f$?",
        {"A": r"$x \le 7$", "B": r"$x \ge -7$", "C": r"$x \ge 0$",
         "D": r"$x \ge 7$"}, "D",
        r"A square root is defined only when what is inside it is not"
        r" negative:"
        r" $$x - 7 \ge 0 \;\Rightarrow\; x \ge 7.$$"
        r" Testing confirms it: $f(7) = \sqrt{0} = 0$ is fine, while"
        r" $f(3) = \sqrt{-4}$ is not a real number. Solving the inequality"
        r" backwards gives $x \le 7$, and moving 7 the wrong way gives"
        r" $x \ge -7$."
        r" The correct answer is **D**.",
        ["Eq(sqrt(7 - 7), 0)", "Eq(sqrt(16 - 7), 3)", "16 - 7 >= 0",
         "Not(3 - 7 >= 0)"]))

    # Q7 E alg — direct variation constant
    assert Rational(42, 7) == 6
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q07", M, 7, "algebra", "linear_functions", "easy",
        r"The quantity $y$ is directly proportional to $x$, and $y = 42$ when"
        r" $x = 7$. What is the value of $y$ when $x = 11$?",
        r"Direct proportion means $y = kx$ for a constant $k$:"
        r" $$42 = k(7) \;\Rightarrow\; k = 6.$$"
        r" Then at $x = 11$:"
        r" $$y = 6(11) = 66.$$"
        r" Adding the change in $x$ to $y$ instead — $42 + 4 = 46$ — treats the"
        r" relationship as a constant DIFFERENCE rather than a constant ratio."
        r" The correct answer is **D**.",
        ["Eq(Rational(42,7), 6)", "Eq(6*11, 66)"],
        66, {6: "reported the constant of proportionality",
             46: "added the change in x instead of scaling",
             53: "added 11 to 42"}, fmt=smart))

    # Q8 E adv — evaluate a composite of simple rules
    assert 3 * (2 * 4 - 1) == 21
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q08", M, 8, "advanced_math", "nonlinear_functions", "easy",
        r"The functions $f$ and $g$ are defined by $f(x) = 2x - 1$ and"
        r" $g(x) = 3x$. What is the value of $g(f(4))$?",
        r"Work from the inside out:"
        r" $$f(4) = 2(4) - 1 = 7, \qquad g(7) = 3(7) = 21.$$"
        r" Composing in the other order gives $f(g(4)) = f(12) = 23$, a"
        r" different value — the order of composition matters."
        r" The correct answer is **C**.",
        ["Eq(2*4 - 1, 7)", "Eq(3*7, 21)", "Eq(2*(3*4) - 1, 23)"],
        21, {11: "computed f(4) + g(4) incorrectly", 12: "computed g(4) only",
             23: "composed in the reverse order"}, fmt=smart))

    # Q9 SPR M adv — doubling time from an exponential model
    assert 500 * 2**3 == 4000
    qs.append(spr(
        "SAT-P9-M1-Q09", M, 9, "advanced_math", "nonlinear_functions", "medium",
        r"A population is modeled by $P(t) = 500 \cdot 2^{\,t/4}$, where $t$ is"
        r" measured in years. After how many years does the population first"
        r" reach $4{,}000$?",
        ["12"],
        r"Divide both sides by the starting value to isolate the power:"
        r" $$2^{\,t/4} = \frac{4000}{500} = 8 = 2^3.$$"
        r" With equal bases the exponents match:"
        r" $$\frac{t}{4} = 3 \;\Rightarrow\; t = 12.$$"
        r" The model doubles every 4 years, and reaching 8 times the start"
        r" takes three doublings — $4 \times 3 = 12$ years. Answering 3 gives"
        r" the number of doublings, not the years."
        r" The correct answer is **12**.",
        ["Eq(Rational(4000,500), 8)", "Eq(2**3, 8)",
         "Eq(500*2**Rational(12,4), 4000)"]))

    # Q10 M psda — median from a frequency table
    VALS, FREQ = [1, 2, 3, 4], [5, 9, 7, 4]
    assert sum(FREQ) == 25
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q10", M, 10, "psda", "one_var_data", "medium",
        r"The table shows the number of siblings reported by each of $25$"
        r" students. What is the median number of siblings?",
        r"With 25 values the median is the $13$th when they are listed in"
        r" order. Accumulate the frequencies from the smallest value:"
        r" $$5, \quad 5 + 9 = 14, \quad 14 + 7 = 21, \quad 21 + 4 = 25.$$"
        r" The running total first reaches 13 in the second row, so the $13$th"
        r" student reported 2 siblings."
        r" The value 2 also has the largest frequency here, but that makes it"
        r" the MODE; the running total is what identifies the median. The mean"
        r" is $\frac{60}{25} = 2.4$, a third distinct measure."
        r" The correct answer is **B**.",
        ["Eq(5 + 9 + 7 + 4, 25)", "Eq(5 + 9, 14)", "5 < 13", "14 >= 13",
         "Eq(1*5 + 2*9 + 3*7 + 4*4, 60)"],
        2, {1: "took the smallest value",
            Rational(12, 5): "reported the mean", 3: "took the middle value"},
        fmt=smart,
        fig=figure("sat-p9-m1-q10",
                   "Two-row table of siblings 1, 2, 3, 4 against number of "
                   "students 5, 9, 7, 4")))

    # Q11 M alg — parameter for infinitely many solutions in ONE variable
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q11", M, 11, "algebra", "linear_equations_one_var", "medium",
        r"$$ax + 12 = 4x + 12$$"
        r" In the equation above, $a$ is a constant. If the equation has"
        r" infinitely many solutions, what is the value of $a$?",
        r"An equation in one variable has infinitely many solutions only when"
        r" the two sides are IDENTICAL — every $x$ must work. The constants"
        r" already agree, so the coefficients of $x$ must agree too:"
        r" $$a = 4.$$"
        r" Any other value of $a$ gives $(a - 4)x = 0$, which has the single"
        r" solution $x = 0$ — one solution, not infinitely many. That is the"
        r" distinction the question tests."
        r" The correct answer is **B**.",
        ["Eq(4*7 + 12, 4*7 + 12)", "Eq(4*(-3) + 12, 4*(-3) + 12)",
         "Eq(expand((5 - 4)*x), x)"],
        4, {0: "set the coefficient to zero", 12: "used the constant term",
            -4: "matched the coefficients with the wrong sign"}, fmt=smart))

    # Q12 M adv — inverse value read backwards
    assert _solve(Eq(3 * x + 8, 23), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q12", M, 12, "advanced_math", "nonlinear_functions", "medium",
        r"The function $f$ is defined by $f(x) = 3x + 8$. If $f^{-1}$ is the"
        r" inverse of $f$, what is the value of $f^{-1}(23)$?",
        r"$f^{-1}(23)$ asks: which input to $f$ PRODUCES 23? Solve"
        r" $$3x + 8 = 23 \;\Rightarrow\; 3x = 15 \;\Rightarrow\; x = 5.$$"
        r" No formula for the inverse is needed — reading the definition"
        r" backwards is enough. Evaluating $f(23) = 77$ answers the forward"
        r" question instead, and $\frac{1}{f(23)}$ confuses the inverse"
        r" FUNCTION with a reciprocal."
        r" The correct answer is **A**.",
        ["Eq(3*5 + 8, 23)", "Eq(3*23 + 8, 77)"],
        5, {15: "stopped at 3x = 15", 31: "added 8 instead of subtracting",
            77: "evaluated f(23) instead"}, fmt=smart))

    # Q13 M geo — distance between two points
    assert (9 - 3) ** 2 + (13 - 5) ** 2 == 100
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q13", M, 13, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In the $xy$-plane, what is the distance between the points $(3, 5)$"
        r" and $(9, 13)$?",
        r"The horizontal and vertical gaps are the legs of a right triangle,"
        r" and the distance is its hypotenuse:"
        r" $$d = \sqrt{(9 - 3)^2 + (13 - 5)^2} = \sqrt{36 + 64}"
        r" = \sqrt{100} = 10.$$"
        r" Adding the gaps without squaring gives $6 + 8 = 14$, and taking"
        r" only one gap gives 6 or 8."
        r" The correct answer is **C**.",
        ["Eq((9 - 3)**2 + (13 - 5)**2, 100)", "Eq(sqrt(100), 10)"],
        10, {8: "used only the vertical gap",
             14: "added the gaps without squaring",
             100: "stopped at the sum of squares"}, fmt=smart))

    # Q14 SPR M psda — percent of a total from counts
    assert Rational(63, 180) * 100 == 35
    qs.append(spr(
        "SAT-P9-M1-Q14", M, 14, "psda", "percentages", "medium",
        r"Of the $180$ tickets sold for a concert, $63$ were student tickets."
        r" What percent of the tickets sold were student tickets? (Disregard"
        r" the percent sign when entering your answer.)",
        ["35"],
        r"Divide the part by the whole and convert:"
        r" $$\frac{63}{180} = 0.35 = 35\%.$$"
        r" The remaining $117$ tickets are $65\%$, and $35 + 65 = 100$ as a"
        r" check."
        r" The correct answer is **35**.",
        ["Eq(Rational(63,180)*100, 35)", "Eq(180 - 63, 117)",
         "Eq(Rational(117,180)*100, 65)"]))

    # Q15 M alg — inequality with a negative coefficient
    qs.append(mcq_listed(
        "SAT-P9-M1-Q15", M, 15, "algebra", "linear_inequalities", "medium",
        r"Which of the following gives all solutions of $11 - 4x \ge 31$?",
        {"A": r"$x \le -5$", "B": r"$x \le 5$", "C": r"$x \ge -5$",
         "D": r"$x \ge 5$"}, "A",
        r"Subtract 11 from both sides:"
        r" $$-4x \ge 20.$$"
        r" Now divide by $-4$. Dividing an inequality by a NEGATIVE number"
        r" reverses the direction of the sign:"
        r" $$x \le -5.$$"
        r" Forgetting to flip gives $x \ge -5$, the exact opposite set. Check"
        r" with $x = -6$: $11 - 4(-6) = 35 \ge 31$ — true, and $-6 \le -5$, so"
        r" the direction is right."
        r" The correct answer is **A**.",
        ["11 - 4*(-6) >= 31", "Not(11 - 4*0 >= 31)",
         "Eq(Rational(20,-4), -5)"]))

    # Q16 M adv — quadratic with a leading coefficient, larger root
    assert sorted(_solve(Eq(2 * x**2 - 11 * x + 12, 0), x)) == \
        [Rational(3, 2), 4]
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q16", M, 16, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What is the greater of the two solutions to $2x^2 - 11x + 12 = 0$?",
        r"Split the middle term using two numbers whose product is"
        r" $2 \cdot 12 = 24$ and whose sum is $-11$: those are $-3$ and $-8$."
        r" $$2x^2 - 8x - 3x + 12 = 2x(x - 4) - 3(x - 4) = (2x - 3)(x - 4) = 0.$$"
        r" The solutions are $x = \frac{3}{2}$ and $x = 4$, and the greater is"
        r" 4. Reporting the smaller gives $1.5$."
        r" The correct answer is **D**.",
        ["Eq(expand((2*x - 3)*(x - 4)), 2*x**2 - 11*x + 12)",
         "Eq(2*4**2 - 11*4 + 12, 0)",
         "Eq(2*Rational(3,2)**2 - 11*Rational(3,2) + 12, 0)"],
        4, {Rational(3, 2): "reported the smaller solution",
            2: "divided the middle coefficient by the leading one",
            3: "used the split value 3 as a solution"}, fmt=smart))

    # Q17 M geo — volume of a pyramid
    assert Rational(1, 3) * 9 * 9 * 10 == 270
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q17", M, 17, "geometry_trig", "area_volume", "medium",
        r"A right pyramid has a square base with sides of length $9$ and a"
        r" height of $10$. What is the volume of the pyramid?",
        r"The reference sheet gives $V = \frac{1}{3}Bh$, where $B$ is the area"
        r" of the base:"
        r" $$B = 9^2 = 81, \qquad V = \frac{1}{3}(81)(10) = 270.$$"
        r" Omitting the $\frac{1}{3}$ gives 810 — that is the volume of the"
        r" PRISM with the same base and height, exactly three times as large."
        r" The correct answer is **B**.",
        ["Eq(9**2, 81)", "Eq(Rational(1,3)*81*10, 270)", "Eq(81*10, 810)"],
        270, {90: "multiplied the side by the height",
              810: "omitted the one-third factor",
              243: "used the height as a third side"}, fmt=smart))

    # Q18 SPR H adv — system of a line and a parabola, sum of x
    assert sorted(_solve(Eq(x**2 + 2 * x - 5, 3 * x + 1), x)) == [-2, 3]
    qs.append(spr(
        "SAT-P9-M1-Q18", M, 18, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"$$y = x^2 + 2x - 5$$ $$y = 3x + 1$$"
        r" The graphs of the equations above intersect at two points in the"
        r" $xy$-plane. What is the sum of the $x$-coordinates of those points?",
        ["1"],
        r"Set the expressions equal and collect on one side:"
        r" $$x^2 + 2x - 5 = 3x + 1 \;\Rightarrow\; x^2 - x - 6 = 0.$$"
        r" Factoring gives $(x - 3)(x + 2) = 0$, so $x = 3$ and $x = -2$, and"
        r" $$3 + (-2) = 1.$$"
        r" Faster: for $x^2 + bx + c = 0$ the solutions sum to $-b$, and here"
        r" $-(-1) = 1$."
        r" The correct answer is **1**.",
        ["Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
         "Eq(3**2 + 2*3 - 5, 3*3 + 1)",
         "Eq((-2)**2 + 2*(-2) - 5, 3*(-2) + 1)", "Eq(3 + (-2), 1)"]))

    # Q19 H psda — two-way table, conditional
    T19 = {"a": [22, 18], "b": [31, 9]}
    assert sum(T19["a"]) + sum(T19["b"]) == 80
    qs.append(mcq_listed(
        "SAT-P9-M1-Q19", M, 19, "psda", "probability_conditional", "hard",
        r"The two-way table shows how $80$ people responded to a survey, by"
        r" age group. If one of the people who answered NO is selected at"
        r" random, what is the probability that the person is under $40$?",
        {"A": r"$\dfrac{18}{80}$", "B": r"$\dfrac{18}{40}$",
         "C": r"$\dfrac{18}{27}$", "D": r"$\dfrac{27}{80}$"}, "C",
        r"The condition selects the NO group, so the denominator is that"
        r" COLUMN's total:"
        r" $$18 + 9 = 27.$$"
        r" Of those 27, the 18 who are under 40 give"
        r" $$\frac{18}{27}.$$"
        r" Dividing by the under-40 ROW total 40 answers the reversed"
        r" question, and dividing by 80 ignores the condition entirely."
        r" Identifying which total the condition selects is the whole task."
        r" The correct answer is **C**.",
        ["Eq(22 + 18 + 31 + 9, 80)", "Eq(18 + 9, 27)", "Eq(22 + 18, 40)",
         "Rational(18,27) != Rational(18,40)"],
        fig=figure("sat-p9-m1-q19",
                   "Two-way table of age group (under 40, 40 or older) "
                   "against response (yes, no) with row and column totals")))

    # Q20 H geo — geometric mean in similar right triangles
    assert 4 * 9 == 36 and 6**2 == 36
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q20", M, 20, "geometry_trig", "right_triangles_trig", "hard",
        r"In right triangle $ABC$, the right angle is at $C$, and the altitude"
        r" from $C$ meets the hypotenuse $AB$ at $D$. If $AD = 4$ and"
        r" $DB = 9$, what is the length of the altitude $CD$?",
        r"The altitude to the hypotenuse splits a right triangle into two"
        r" triangles SIMILAR to the original and to each other. Matching"
        r" corresponding sides in the two small triangles gives"
        r" $$\frac{AD}{CD} = \frac{CD}{DB} \;\Rightarrow\; CD^2 = AD \cdot DB.$$"
        r" So"
        r" $$CD^2 = 4 \times 9 = 36 \;\Rightarrow\; CD = 6.$$"
        r" The altitude is the GEOMETRIC mean of the two pieces, not the"
        r" arithmetic one — averaging gives $6.5$, and the full hypotenuse is"
        r" $4 + 9 = 13$."
        r" The correct answer is **B**.",
        ["Eq(4*9, 36)", "Eq(sqrt(36), 6)", "Eq(4 + 9, 13)",
         "Ne(Rational(4 + 9, 2), 6)"],
        6, {5: "took half the difference",
            Rational(13, 2): "averaged the two pieces",
            13: "reported the whole hypotenuse"}, fmt=smart))

    # Q21 SPR H alg — literal equation solved for a nested variable
    assert _solve(Eq(2 * (x + 3 * 5), 46), x) == [8]
    qs.append(spr(
        "SAT-P9-M1-Q21", M, 21, "algebra", "linear_equations_one_var", "hard",
        r"The perimeter of a rectangle is given by $P = 2(L + W)$. A rectangle"
        r" has perimeter $46$ and width $W = 15$. What is its length $L$?",
        ["8"],
        r"Substitute the known values and undo the operations from the outside"
        r" in:"
        r" $$46 = 2(L + 15) \;\Rightarrow\; 23 = L + 15 \;\Rightarrow\; L = 8.$$"
        r" Check: $2(8 + 15) = 2(23) = 46$. Subtracting 15 from 46 before"
        r" halving gives $15.5$ — the division by 2 must come first because"
        r" the 2 multiplies the WHOLE sum."
        r" The correct answer is **8**.",
        ["Eq(2*(8 + 15), 46)", "Eq(Rational(46,2) - 15, 8)"]))

    # Q22 H alg — system with fractional coefficients
    _s = _solve([Eq(Rational(1, 2) * x + Rational(1, 3) * y, 8),
                 Eq(x - y, 6)], [x, y], dict=True)[0]
    assert _s[x] == 12 and _s[y] == 6
    assert Rational(1, 2) * 12 + Rational(1, 3) * 6 == 8
    qs.append(mcq_numeric(
        "SAT-P9-M1-Q22", M, 22, "algebra", "systems_two_linear", "hard",
        r"$$\frac{1}{2}x + \frac{1}{3}y = 8$$ $$x - y = 6$$"
        r" If $(x, y)$ is the solution to the system above, what is the value"
        r" of $x$?",
        r"Clear the fractions first by multiplying the first equation by 6,"
        r" the least common denominator of 2 and 3:"
        r" $$3x + 2y = 48.$$"
        r" The second equation gives $y = x - 6$. Substitute:"
        r" $$3x + 2(x - 6) = 48 \;\Rightarrow\; 5x - 12 = 48"
        r" \;\Rightarrow\; 5x = 60 \;\Rightarrow\; x = 12.$$"
        r" Then $y = 6$, and the original first equation checks out:"
        r" $\frac{1}{2}(12) + \frac{1}{3}(6) = 6 + 2 = 8$."
        r" Reporting $y$ gives 6, and multiplying the first equation by 2"
        r" instead of 6 leaves the $y$-term fractional."
        r" The correct answer is **C**.",
        ["Eq(Rational(1,2)*12 + Rational(1,3)*6, 8)", "Eq(12 - 6, 6)",
         "Eq(3*12 + 2*6, 48)"],
        12, {6: "reported the value of y",
             10: "cleared the fractions with the wrong multiplier",
             14: "added the two right-hand sides"}, fmt=smart))

    return qs


# ─── Module 2, easier variant (11E / 9M / 2H) ─────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    assert _solve(Eq(x + 9, 4), x) == [-5]
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $x + 9 = 4$, what is the value of $x$?",
        r"Subtract 9 from both sides:"
        r" $$x = 4 - 9 = -5.$$"
        r" Reversing the subtraction gives 5, and adding gives 13."
        r" The correct answer is **A**.",
        ["Eq(-5 + 9, 4)"],
        -5, {5: "subtracted 4 from 9 instead", 4: "left the constant alone",
             13: "added 9 instead of subtracting"}, fmt=smart))

    assert expand(2 * (3 * x + 4)) == 6 * x + 8
    qs.append(mcq_listed(
        "SAT-P9-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $2(3x + 4)$?",
        {"A": r"$5x + 6$", "B": r"$6x + 4$", "C": r"$6x + 8$",
         "D": r"$6x + 42$"}, "C",
        r"Distribute the 2 across BOTH terms:"
        r" $$2 \cdot 3x = 6x, \qquad 2 \cdot 4 = 8.$$"
        r" So the result is $6x + 8$. Multiplying only the first term leaves"
        r" $6x + 4$."
        r" The correct answer is **C**.",
        ["Eq(expand(2*(3*x + 4)), 6*x + 8)", "Eq(2*(3*1 + 4), 14)"]))

    qs.append(spr(
        "SAT-P9-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 5x + 2$. What is the value of"
        r" $f(6)$?",
        ["32"],
        r"Substitute $x = 6$:"
        r" $$f(6) = 5(6) + 2 = 30 + 2 = 32.$$"
        r" The correct answer is **32**.",
        ["Eq(5*6 + 2, 32)"]))

    assert Rational(9, 36) * 100 == 25
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q04", M, 4, "psda", "percentages", "easy",
        r"A basket holds $36$ pieces of fruit, of which $9$ are pears. What"
        r" percent of the fruit are pears?",
        r"Divide the part by the whole:"
        r" $$\frac{9}{36} = 0.25 = 25\%.$$"
        r" Reporting the count gives 9, and the percent that are NOT pears is"
        r" $75\%$."
        r" The correct answer is **B**.",
        ["Eq(Rational(9,36)*100, 25)", "Eq(Rational(27,36)*100, 75)"],
        25, {9: "reported the number of pears", 27: "reported the other fruit",
             75: "found the percent that are not pears"}, fmt=smart))

    assert 2 * (7 + 5) == 24
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        r"A rectangle has a length of $7$ and a width of $5$. What is the"
        r" perimeter of the rectangle?",
        r"Perimeter adds all four sides, which is twice the sum of the length"
        r" and width:"
        r" $$P = 2(7 + 5) = 24.$$"
        r" Multiplying instead gives the AREA, 35, and adding the two"
        r" dimensions once gives 12."
        r" The correct answer is **C**.",
        ["Eq(2*(7 + 5), 24)", "Eq(7*5, 35)"],
        24, {12: "added the length and width once",
             35: "computed the area instead", 70: "doubled the area"},
        fmt=smart))

    assert (-1) ** 2 - 5 * (-1) == 6
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q06", M, 6, "advanced_math", "nonlinear_functions", "easy",
        r"The function $g$ is defined by $g(x) = x^2 - 5x$. What is the value"
        r" of $g(-1)$?",
        r"Substitute $x = -1$, squaring first:"
        r" $$g(-1) = (-1)^2 - 5(-1) = 1 + 5 = 6.$$"
        r" Subtracting rather than recognising the double negative gives"
        r" $1 - 5 = -4$."
        r" The correct answer is **D**.",
        ["Eq((-1)**2 - 5*(-1), 6)", "Eq((-1)**2, 1)"],
        6, {-6: "made both a sign and a square error",
            -4: "treated -5(-1) as -5", 4: "squared -1 as -1"}, fmt=smart))

    assert _solve(Eq(2 * x + 3 * 4, 20), x) == [4]
    qs.append(spr(
        "SAT-P9-M2E-Q07", M, 7, "algebra", "linear_equations_two_var", "easy",
        r"The point $(k, 4)$ lies on the graph of $2x + 3y = 20$ in the"
        r" $xy$-plane. What is the value of $k$?",
        ["4"],
        r"A point on the graph satisfies the equation. Substitute $y = 4$:"
        r" $$2k + 12 = 20 \;\Rightarrow\; 2k = 8 \;\Rightarrow\; k = 4.$$"
        r" The correct answer is **4**.",
        ["Eq(2*4 + 3*4, 20)"]))

    assert sorted(_solve(Eq((x - 6) * (x + 1), 0), x)) == [-1, 6]
    qs.append(mcq_listed(
        "SAT-P9-M2E-Q08", M, 8, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = (x - 6)(x + 1)$. What are the"
        r" zeros of $f$?",
        {"A": r"$-6$ and $1$", "B": r"$-6$ and $-1$", "C": r"$-1$ and $6$",
         "D": r"$1$ and $6$"}, "C",
        r"A product equals zero when one of its factors does:"
        r" $$x - 6 = 0 \;\Rightarrow\; x = 6, \qquad x + 1 = 0"
        r" \;\Rightarrow\; x = -1.$$"
        r" Each zero has the OPPOSITE sign of the number written in its"
        r" factor."
        r" The correct answer is **C**.",
        ["Eq((6 - 6)*(6 + 1), 0)", "Eq((-1 - 6)*(-1 + 1), 0)"]))

    assert 30 + 12 * 4 == 78
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q09", M, 9, "algebra", "linear_functions", "easy",
        r"A gym charges a $\$30$ joining fee plus $\$12$ for each month of"
        r" membership. What is the total cost for $4$ months?",
        r"The joining fee is paid once; the monthly charge scales with the"
        r" months:"
        r" $$30 + 12(4) = 30 + 48 = 78.$$"
        r" Omitting the joining fee gives 48, and charging the fee monthly"
        r" gives $4(30 + 12) = 168$."
        r" The correct answer is **C**.",
        ["Eq(30 + 12*4, 78)", "Eq(4*(30 + 12), 168)"],
        78, {42: "added the fee and the monthly rate once",
             48: "omitted the joining fee",
             168: "charged the joining fee every month"}, fmt=money))

    qs.append(mcq_listed(
        "SAT-P9-M2E-Q10", M, 10, "advanced_math", "equivalent_expressions",
        "easy",
        r"For $x \ne 0$, which of the following is equivalent to"
        r" $\dfrac{x^{9}}{x^{4}}$?",
        {"A": r"$x^{2}$", "B": r"$x^{5}$", "C": r"$x^{13}$",
         "D": r"$x^{36}$"}, "B",
        r"Dividing powers with the same base SUBTRACTS the exponents:"
        r" $$\frac{x^{9}}{x^{4}} = x^{9 - 4} = x^{5}.$$"
        r" Adding them gives $x^{13}$ and multiplying gives $x^{36}$ — those"
        r" are the rules for multiplying and for a power of a power."
        r" The correct answer is **B**.",
        ["Eq(simplify(x**9/x**4 - x**5), 0)", "Eq(2**9/2**4, 2**5)"]))

    D11 = [3, 7, 7, 10, 13]
    assert sum(D11) == 40
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q11", M, 11, "psda", "one_var_data", "easy",
        r"What is the mean of the data set $3$, $7$, $7$, $10$, $13$?",
        r"Add the values and divide by how many there are:"
        r" $$\frac{3 + 7 + 7 + 10 + 13}{5} = \frac{40}{5} = 8.$$"
        r" The MEDIAN — the middle value in order — is 7, and the MODE is also"
        r" 7; the mean is pulled up by the 13."
        r" The correct answer is **B**.",
        ["Eq(3 + 7 + 7 + 10 + 13, 40)", "Eq(Rational(40,5), 8)"],
        8, {7: "reported the median or mode", 10: "took the middle of the range",
            40: "reported the total"}, fmt=smart))

    assert sorted(_solve(Eq(x**2 - 6 * x + 5, 0), x)) == [1, 5]
    qs.append(spr(
        "SAT-P9-M2E-Q12", M, 12, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"What is the greater of the two solutions to $x^2 - 6x + 5 = 0$?",
        ["5"],
        r"Two numbers with product 5 and sum $-6$ are $-1$ and $-5$:"
        r" $$x^2 - 6x + 5 = (x - 1)(x - 5) = 0.$$"
        r" The solutions are 1 and 5, and the greater is 5."
        r" The correct answer is **5**.",
        ["Eq(expand((x - 1)*(x - 5)), x**2 - 6*x + 5)",
         "Eq(5**2 - 6*5 + 5, 0)"]))

    _s = _solve([Eq(x + y, 30), Eq(x - y, 8)], [x, y], dict=True)[0]
    assert _s[x] == 19 and _s[y] == 11
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q13", M, 13, "algebra", "systems_two_linear", "medium",
        r"$$x + y = 30$$ $$x - y = 8$$"
        r" If $(x, y)$ is the solution to the system above, what is the value"
        r" of $x$?",
        r"Adding the two equations eliminates $y$ at once:"
        r" $$2x = 38 \;\Rightarrow\; x = 19.$$"
        r" Then $y = 11$, and both originals check. Subtracting instead gives"
        r" $2y = 22$, or $y = 11$ — the other variable."
        r" The correct answer is **C**.",
        ["Eq(19 + 11, 30)", "Eq(19 - 11, 8)", "Eq(30 + 8, 38)"],
        19, {11: "reported the value of y", 15: "halved 30",
             38: "stopped at 2x = 38"}, fmt=smart))

    qs.append(mcq_listed(
        "SAT-P9-M2E-Q14", M, 14, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph of $y = x^2$ is shifted $4$ units DOWN to produce the graph"
        r" of $y = g(x)$. Which equation defines $g$?",
        {"A": r"$g(x) = (x - 4)^2$", "B": r"$g(x) = (x + 4)^2$",
         "C": r"$g(x) = x^2 - 4$", "D": r"$g(x) = x^2 + 4$"}, "C",
        r"A VERTICAL shift changes the output, so it is applied outside the"
        r" squaring — subtract 4 from the whole expression:"
        r" $$g(x) = x^2 - 4.$$"
        r" Putting the 4 inside the parentheses, as in $(x - 4)^2$, shifts the"
        r" graph HORIZONTALLY instead. Checking one point settles it: the"
        r" vertex $(0, 0)$ must move to $(0, -4)$, and only $x^2 - 4$ does"
        r" that."
        r" The correct answer is **C**.",
        ["Eq(0**2 - 4, -4)", "Eq((0 - 4)**2, 16)"]))

    assert _solve(Eq(Rational(x, 4) + 3, 11), x) == [32] if False else True
    assert _solve(Eq(x / 4 + 3, 11), x) == [32]
    qs.append(spr(
        "SAT-P9-M2E-Q15", M, 15, "algebra", "linear_equations_one_var",
        "medium",
        r"$$\frac{x}{4} + 3 = 11$$"
        r" What is the solution to the equation above?",
        ["32"],
        r"Subtract 3, then multiply by 4:"
        r" $$\frac{x}{4} = 8 \;\Rightarrow\; x = 32.$$"
        r" Check: $\frac{32}{4} + 3 = 8 + 3 = 11$."
        r" The correct answer is **32**.",
        ["Eq(Rational(32,4) + 3, 11)", "Eq((11 - 3)*4, 32)"]))

    assert Rational(56, 8) == 7
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q16", M, 16, "psda", "ratios_rates_units", "medium",
        r"A car uses $8$ liters of fuel to travel $56$ kilometers. At this"
        r" rate, how many liters are needed to travel $189$ kilometers?",
        r"Find the distance per liter, then divide:"
        r" $$\frac{56}{8} = 7 \text{ km per liter}, \qquad"
        r" \frac{189}{7} = 27 \text{ liters}.$$"
        r" Multiplying by 7 instead of dividing gives $1323$, and using 8"
        r" liters per 189 km gives about 24."
        r" The correct answer is **C**.",
        ["Eq(Rational(56,8), 7)", "Eq(Rational(189,7), 27)"],
        27, {7: "reported the kilometers per liter",
             24: "divided 189 by 8", 32: "added the numbers"}, fmt=smart))

    qs.append(mcq_listed(
        "SAT-P9-M2E-Q17", M, 17, "advanced_math", "nonlinear_functions",
        "medium",
        r"A quantity begins at $800$ and decreases by $15\%$ each year. Which"
        r" function gives the quantity after $t$ years?",
        {"A": r"$q(t) = 800(0.15)^t$", "B": r"$q(t) = 800(0.85)^t$",
         "C": r"$q(t) = 800(1.15)^t$", "D": r"$q(t) = 800 - 15t$"}, "B",
        r"Decreasing by $15\%$ leaves $85\%$ of the previous amount, so each"
        r" year multiplies by"
        r" $$1 - 0.15 = 0.85.$$"
        r" After $t$ years the factor applies $t$ times, giving"
        r" $q(t) = 800(0.85)^t$. A base of $0.15$ would keep only $15\%$ each"
        r" year, and $800 - 15t$ is LINEAR — it subtracts a fixed 15, not"
        r" $15\%$ of a shrinking amount."
        r" The correct answer is **B**.",
        ["Eq(1 - Rational(15,100), Rational(85,100))",
         "Eq(800*Rational(85,100), 680)"]))

    assert 5**2 + 12**2 == 13**2
    qs.append(mcq_numeric(
        "SAT-P9-M2E-Q18", M, 18, "geometry_trig", "right_triangles_trig",
        "medium",
        r"A right triangle has legs of length $5$ and $12$. What is the length"
        r" of the hypotenuse?",
        r"By the Pythagorean theorem:"
        r" $$h^2 = 5^2 + 12^2 = 25 + 144 = 169 \;\Rightarrow\; h = 13.$$"
        r" Adding the legs gives 17, which would be the perimeter contribution"
        r" of the two legs, not the hypotenuse."
        r" The correct answer is **C**.",
        ["Eq(5**2 + 12**2, 169)", "Eq(sqrt(169), 13)"],
        13, {6: "halved the longer leg", 7: "subtracted the legs",
             17: "added the legs"}, fmt=smart))

    assert Rational(19 - 7, 5 - 1) == 3
    qs.append(spr(
        "SAT-P9-M2E-Q19", M, 19, "algebra", "linear_equations_two_var",
        "medium",
        r"A line in the $xy$-plane passes through $(1, 7)$ and $(5, 19)$. What"
        r" is the slope of the line?",
        ["3"],
        r"Slope is the change in $y$ over the change in $x$:"
        r" $$m = \frac{19 - 7}{5 - 1} = \frac{12}{4} = 3.$$"
        r" The correct answer is **3**.",
        ["Eq(Rational(19 - 7, 5 - 1), 3)", "Eq(7 + 3*(5 - 1), 19)"]))

    assert simplify(sqrt(50) - 5 * sqrt(2)) == 0
    qs.append(mcq_listed(
        "SAT-P9-M2E-Q20", M, 20, "advanced_math", "equivalent_expressions",
        "medium",
        r"Which of the following is equivalent to $\sqrt{50}$?",
        {"A": r"$2\sqrt{5}$", "B": r"$5\sqrt{2}$", "C": r"$10\sqrt{5}$",
         "D": r"$25\sqrt{2}$"}, "B",
        r"Pull out the largest perfect-square factor of 50:"
        r" $$\sqrt{50} = \sqrt{25 \cdot 2} = \sqrt{25}\sqrt{2} = 5\sqrt{2}.$$"
        r" A quick check: $5\sqrt{2} \approx 7.07$ and"
        r" $\sqrt{50} \approx 7.07$, while $2\sqrt{5} \approx 4.47$."
        r" The correct answer is **B**.",
        ["Eq(simplify(sqrt(50)), 5*sqrt(2))",
         "Eq(simplify((5*sqrt(2))**2), 50)"]))

    assert Rational(72, 360) * 10 == 2
    qs.append(mcq_listed(
        "SAT-P9-M2E-Q21", M, 21, "geometry_trig", "circles", "hard",
        r"A circle has a radius of $5$. What is the length of an arc"
        r" intercepted by a central angle of $72^\circ$?",
        {"A": r"$\pi$", "B": r"$2\pi$", "C": r"$5\pi$", "D": r"$10\pi$"},
        "B",
        r"An arc is the same fraction of the circumference that its central"
        r" angle is of a full turn:"
        r" $$\frac{72}{360} = \frac{1}{5}.$$"
        r" The circumference is $2\pi(5) = 10\pi$, so"
        r" $$\text{arc} = \frac{1}{5}(10\pi) = 2\pi.$$"
        r" Applying the fraction to the AREA $25\pi$ instead gives $5\pi$, a"
        r" different quantity with different units."
        r" The correct answer is **B**.",
        ["Eq(Rational(72,360), Rational(1,5))", "Eq(2*5, 10)",
         "Eq(Rational(10,5), 2)"]))

    assert _solve(Eq(3 * (x - 4), 2 * x + 1), x) == [13]
    qs.append(spr(
        "SAT-P9-M2E-Q22", M, 22, "algebra", "linear_equations_one_var", "hard",
        r"$$3(x - 4) = 2x + 1$$"
        r" What is the solution to the equation above?",
        ["13"],
        r"Distribute, then gather like terms:"
        r" $$3x - 12 = 2x + 1 \;\Rightarrow\; x = 13.$$"
        r" Check: $3(13 - 4) = 27$ and $2(13) + 1 = 27$."
        r" The correct answer is **13**.",
        ["Eq(3*(13 - 4), 2*13 + 1)", "Eq(3*(13 - 4), 27)"]))

    return qs


# ─── Module 2, harder variant (2E / 7M / 13H) ─────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    assert _solve(Eq(7 * x + 3, 3 * x + 27), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $7x + 3 = 3x + 27$, what is the value of $x$?",
        r"Gather like terms:"
        r" $$4x = 24 \;\Rightarrow\; x = 6.$$"
        r" Stopping at $4x = 24$ gives 24."
        r" The correct answer is **B**.",
        ["Eq(7*6 + 3, 3*6 + 27)", "Eq((27 - 3)/(7 - 3), 6)"],
        6, {Rational(15, 2): "added the constants instead of subtracting",
            10: "divided 30 by 3", 24: "stopped at 4x = 24"}, fmt=smart))

    assert expand((2 * x + 1) * (2 * x - 1)) == 4 * x**2 - 1
    qs.append(mcq_listed(
        "SAT-P9-M2H-Q02", M, 2, "advanced_math", "equivalent_expressions", "easy",
        r"Which of the following is equivalent to $(2x + 1)(2x - 1)$?",
        {"A": r"$4x^2 - 1$", "B": r"$4x^2 + 1$", "C": r"$4x^2 - 4x - 1$",
         "D": r"$4x^2 + 4x - 1$"}, "A",
        r"The two middle products cancel because the constants are opposites:"
        r" $$(2x + 1)(2x - 1) = 4x^2 - 2x + 2x - 1 = 4x^2 - 1.$$"
        r" This is the difference-of-squares pattern, so no $x$-term survives."
        r" The correct answer is **A**.",
        ["Eq(expand((2*x + 1)*(2*x - 1)), 4*x**2 - 1)"]))

    _s = _solve([Eq(3 * x + y, 22), Eq(x + y, 10)], [x, y], dict=True)[0]
    assert _s[x] == 6 and _s[y] == 4
    qs.append(spr(
        "SAT-P9-M2H-Q03", M, 3, "algebra", "systems_two_linear", "medium",
        r"$$3x + y = 22$$ $$x + y = 10$$"
        r" If $(x, y)$ is the solution to the system above, what is the value"
        r" of $x$?",
        ["6"],
        r"The $y$-terms already match, so subtract the second equation from"
        r" the first:"
        r" $$2x = 12 \;\Rightarrow\; x = 6.$$"
        r" Then $y = 4$, and both originals check: $3(6) + 4 = 22$ and"
        r" $6 + 4 = 10$."
        r" The correct answer is **6**.",
        ["Eq(3*6 + 4, 22)", "Eq(6 + 4, 10)", "Eq(22 - 10, 12)"]))

    assert Rational(1, 2) * 8 * 15 == 60
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q04", M, 4, "geometry_trig", "area_volume", "medium",
        r"A right triangle has legs of length $8$ and $15$. What is the area"
        r" of the triangle?",
        r"In a right triangle the two legs are perpendicular, so they serve as"
        r" base and height:"
        r" $$A = \frac{1}{2}(8)(15) = 60.$$"
        r" Omitting the $\frac{1}{2}$ gives 120, and 17 is the HYPOTENUSE"
        r" (from the $8$-$15$-$17$ triple), not the area."
        r" The correct answer is **C**.",
        ["Eq(Rational(1,2)*8*15, 60)", "Eq(8**2 + 15**2, 17**2)"],
        60, {17: "reported the hypotenuse", 23: "added the legs",
             120: "omitted the one-half factor"}, fmt=smart))

    assert Rational(14, 50) * 100 == 28
    qs.append(mcq_listed(
        "SAT-P9-M2H-Q05", M, 5, "psda", "probability_conditional", "medium",
        r"A bag holds $50$ tokens: $14$ are gold and the rest are silver. Two"
        r" tokens are drawn at random WITHOUT replacement. What is the"
        r" probability that both are gold?",
        {"A": r"$\dfrac{14}{50} \cdot \dfrac{14}{50}$",
         "B": r"$\dfrac{14}{50} \cdot \dfrac{13}{49}$",
         "C": r"$\dfrac{14}{50} + \dfrac{13}{49}$",
         "D": r"$\dfrac{14}{50} \cdot \dfrac{13}{50}$"}, "B",
        r"The first draw is gold with probability $\frac{14}{50}$. Because the"
        r" token is NOT replaced, both counts drop for the second draw: 13"
        r" gold remain out of 49 tokens. Multiply, since both must happen:"
        r" $$\frac{14}{50} \cdot \frac{13}{49}.$$"
        r" Choice A treats the draws as independent — that would be correct"
        r" WITH replacement. Choice D reduces the numerator but forgets the"
        r" denominator, and adding probabilities answers an ''or'' question."
        r" The correct answer is **B**.",
        ["Eq(50 - 14, 36)", "Eq(Rational(14,50)*Rational(13,49), Rational(13,175))",
         "Ne(Rational(14,50)*Rational(13,49), Rational(14,50)*Rational(14,50))"]))

    assert 2 * (-3) ** 2 - 4 * (-3) + 1 == 31
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q06", M, 6, "advanced_math", "nonlinear_functions", "medium",
        r"The function $f$ is defined by $f(x) = 2x^2 - 4x + 1$. What is the"
        r" value of $f(-3)$?",
        r"Substitute $x = -3$, squaring before multiplying:"
        r" $$f(-3) = 2(9) - 4(-3) + 1 = 18 + 12 + 1 = 31.$$"
        r" Treating $-4(-3)$ as $-12$ gives $18 - 12 + 1 = 7$, and squaring"
        r" $-3$ as $-9$ gives $-18 + 12 + 1 = -5$."
        r" The correct answer is **D**.",
        ["Eq(2*(-3)**2 - 4*(-3) + 1, 31)", "Eq((-3)**2, 9)"],
        31, {-5: "treated the square of -3 as -9",
             7: "made a sign error on the linear term",
             19: "omitted the constant"}, fmt=smart))

    assert sorted(_solve(Eq(x**2 + 4 * x - 21, 0), x)) == [-7, 3]
    qs.append(spr(
        "SAT-P9-M2H-Q07", M, 7, "advanced_math", "nonlinear_equations_systems",
        "medium",
        r"The solutions to $x^2 + 4x - 21 = 0$ are $p$ and $q$. What is the"
        r" value of $|p - q|$?",
        ["10"],
        r"Factor with two numbers whose product is $-21$ and sum is $+4$:"
        r" those are $+7$ and $-3$."
        r" $$x^2 + 4x - 21 = (x + 7)(x - 3) = 0,$$"
        r" so the solutions are $-7$ and $3$. Their positive difference is"
        r" $$|{-7} - 3| = 10.$$"
        r" The SUM of the solutions is $-4$ — a different quantity, and the"
        r" one the coefficient $b$ gives directly."
        r" The correct answer is **10**.",
        ["Eq(expand((x + 7)*(x - 3)), x**2 + 4*x - 21)",
         "Eq(Abs(-7 - 3), 10)", "Eq(-7 + 3, -4)"]))

    assert _solve(Eq(6 * x - 5, 2 * x + 19), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q08", M, 8, "algebra", "linear_inequalities", "medium",
        r"What is the least integer value of $x$ that satisfies"
        r" $6x - 5 > 2x + 19$?",
        r"Collect terms:"
        r" $$4x > 24 \;\Rightarrow\; x > 6.$$"
        r" The inequality is STRICT, so $x = 6$ does not satisfy it —"
        r" $6(6) - 5 = 31$ and $2(6) + 19 = 31$ are equal, not greater. The"
        r" least integer strictly above 6 is 7."
        r" The correct answer is **C**.",
        ["Eq(6*6 - 5, 2*6 + 19)", "6*7 - 5 > 2*7 + 19",
         "Not(6*6 - 5 > 2*6 + 19)"],
        7, {5: "used the wrong side of the boundary",
            6: "included the boundary despite the strict inequality",
            24: "stopped at 4x = 24"}, fmt=smart))

    assert 180 - 118 == 62
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q09", M, 9, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In the figure, parallel lines $\ell$ and $m$ are cut by a"
        r" transversal. One interior angle on the same side of the"
        r" transversal measures $118^\circ$. What is the measure, in degrees,"
        r" of the other same-side interior angle?",
        r"Same-side interior angles between parallel lines are SUPPLEMENTARY,"
        r" not equal:"
        r" $$180 - 118 = 62.$$"
        r" Alternate interior angles and corresponding angles would be equal"
        r" to $118^\circ$ — recognising which pair the figure shows is the"
        r" whole task. Halving gives 59."
        r" The correct answer is **B**.",
        ["Eq(180 - 118, 62)", "Eq(118 + 62, 180)"],
        62, {59: "halved the given angle", 118: "assumed the angles are equal",
             242: "added instead of subtracting"}, fmt=smart,
        fig=figure("sat-p9-m2h-q09",
                   "Two parallel lines cut by a transversal with one "
                   "same-side interior angle labeled 118 degrees and the "
                   "other labeled x degrees")))

    _a = _solve([Eq(x + y, 26), Eq(4 * x + 2 * y, 76)], [x, y], dict=True)[0]
    assert _a[x] == 12 and _a[y] == 14
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q10", M, 10, "algebra", "systems_two_linear", "hard",
        r"A farm has only chickens and sheep, $26$ animals in all. Together"
        r" they have $76$ legs. How many sheep are there?",
        r"Let $s$ be the sheep (4 legs each) and $c$ the chickens (2 legs"
        r" each):"
        r" $$s + c = 26, \qquad 4s + 2c = 76.$$"
        r" Substitute $c = 26 - s$:"
        r" $$4s + 2(26 - s) = 76 \;\Rightarrow\; 2s + 52 = 76"
        r" \;\Rightarrow\; s = 12.$$"
        r" So there are 12 sheep and 14 chickens; the check holds:"
        r" $4(12) + 2(14) = 48 + 28 = 76$. Reporting the chickens gives 14."
        r" The correct answer is **B**.",
        ["Eq(12 + 14, 26)", "Eq(4*12 + 2*14, 76)"],
        12, {13: "split the animals evenly", 14: "reported the chickens",
             19: "divided the legs by 4"}, fmt=smart))

    assert _solve(Eq(x**2 - 4 * x + 4, 0), x) == [2]
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q11", M, 11, "advanced_math", "nonlinear_equations_systems",
        "hard",
        r"How many distinct real solutions does $x^2 - 4x + 4 = 0$ have?",
        r"The discriminant decides:"
        r" $$b^2 - 4ac = 16 - 16 = 0,$$"
        r" and a zero discriminant means exactly ONE distinct real solution."
        r" Factoring confirms it: $x^2 - 4x + 4 = (x - 2)^2$, whose only root"
        r" is $x = 2$ — a repeated root, but a single distinct value."
        r" Answering 2 counts the repeated root twice."
        r" The correct answer is **B**.",
        ["Eq((-4)**2 - 4*1*4, 0)", "Eq(expand((x - 2)**2), x**2 - 4*x + 4)",
         "Eq(2**2 - 4*2 + 4, 0)"],
        1, {0: "read a zero discriminant as no solutions",
            2: "counted the repeated root twice",
            4: "reported the constant term"}, fmt=smart))

    assert 3 * 2**4 == 48
    qs.append(spr(
        "SAT-P9-M2H-Q12", M, 12, "advanced_math", "nonlinear_functions", "hard",
        r"The function $h$ is defined by $h(x) = a \cdot 2^{\,x}$, where $a$ is"
        r" a constant. If $h(1) = 6$, what is the value of $h(4)$?",
        ["48"],
        r"Use the given value to find $a$:"
        r" $$a \cdot 2^1 = 6 \;\Rightarrow\; a = 3.$$"
        r" Then"
        r" $$h(4) = 3 \cdot 2^4 = 3 \cdot 16 = 48.$$"
        r" Shortcut: from $x = 1$ to $x = 4$ is three steps, and each step"
        r" doubles, so $6 \cdot 2^3 = 48$. Adding instead of doubling would"
        r" wrongly give 24."
        r" The correct answer is **48**.",
        ["Eq(3*2**1, 6)", "Eq(3*2**4, 48)", "Eq(6*2**3, 48)"]))

    assert _solve(Eq(2 * (x - 1) + 3 * (x + 2), 29), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q13", M, 13, "algebra", "linear_equations_one_var", "hard",
        r"$$2(x - 1) + 3(x + 2) = 29$$"
        r" What is the solution to the equation above?",
        r"Distribute both products, then combine:"
        r" $$2x - 2 + 3x + 6 = 29 \;\Rightarrow\; 5x + 4 = 29"
        r" \;\Rightarrow\; 5x = 25 \;\Rightarrow\; x = 5.$$"
        r" Check: $2(4) + 3(7) = 8 + 21 = 29$. Mis-signing the $-2$ gives"
        r" $5x + 8 = 29$, or $4.2$."
        r" The correct answer is **B**.",
        ["Eq(2*(5 - 1) + 3*(5 + 2), 29)", "Eq(2*4 + 3*7, 29)"],
        5, {Rational(21, 5): "mis-signed the first product",
            Rational(29, 5): "ignored the constants",
            9: "combined the coefficients incorrectly"}, fmt=smart))

    assert simplify((x**2 - 25) / (x + 5) - (x - 5)) == 0
    qs.append(mcq_listed(
        "SAT-P9-M2H-Q14", M, 14, "advanced_math", "equivalent_expressions",
        "hard",
        r"For $x \ne -5$, which of the following is equivalent to"
        r" $\dfrac{x^2 - 25}{x + 5}$?",
        {"A": r"$x - 5$", "B": r"$x + 5$", "C": r"$x - 25$",
         "D": r"$\dfrac{x - 25}{5}$"}, "A",
        r"The numerator is a difference of squares:"
        r" $$\frac{x^2 - 25}{x + 5} = \frac{(x - 5)(x + 5)}{x + 5} = x - 5,$$"
        r" cancelling the common factor $x + 5$, which is nonzero by the"
        r" stated restriction."
        r" Cancelling the 25 against the 5 — a common but invalid move, since"
        r" they are terms, not factors — would give $x - 5$ by accident here"
        r" but fails in general. Check at $x = 0$: the original is"
        r" $\frac{-25}{5} = -5$, and $x - 5 = -5$."
        r" The correct answer is **A**.",
        ["Eq(simplify((x**2 - 25)/(x + 5) - (x - 5)), 0)",
         "Eq(expand((x - 5)*(x + 5)), x**2 - 25)",
         "Eq(Rational(0 - 25, 0 + 5), -5)"]))

    assert Rational(6 * 82 + 4 * 92, 10) == 86
    qs.append(spr(
        "SAT-P9-M2H-Q15", M, 15, "psda", "one_var_data", "hard",
        r"On a test, $6$ students scored a mean of $82$ and $4$ students"
        r" scored a mean of $92$. What is the mean score of all $10$ students?",
        ["86"],
        r"Combine totals rather than averaging the two means, since the groups"
        r" differ in size:"
        r" $$6(82) = 492, \qquad 4(92) = 368,$$"
        r" $$\text{mean} = \frac{492 + 368}{10} = \frac{860}{10} = 86.$$"
        r" Averaging $82$ and $92$ gives 87, which is too high — the larger"
        r" group scored lower, so the combined mean must sit closer to 82."
        r" The correct answer is **86**.",
        ["Eq(6*82, 492)", "Eq(4*92, 368)", "Eq(Rational(860,10), 86)",
         "86 < Rational(82 + 92, 2)"]))

    assert _solve(Eq(Rational(3, 5) * x, 42), x) == [70]
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q16", M, 16, "algebra", "linear_equations_one_var", "hard",
        r"Three-fifths of a number is $42$. What is one-half of that number?",
        r"Recover the number first:"
        r" $$\frac{3}{5}n = 42 \;\Rightarrow\; n = 42 \cdot \frac{5}{3} = 70.$$"
        r" Then take half:"
        r" $$\frac{70}{2} = 35.$$"
        r" Reporting the number itself gives 70, and halving 42 directly gives"
        r" 21 — that skips recovering $n$."
        r" The correct answer is **C**.",
        ["Eq(Rational(3,5)*70, 42)", "Eq(Rational(70,2), 35)"],
        35, {21: "halved 42 without recovering the number",
             25: "used two-fifths", 70: "reported the number itself"},
        fmt=smart))

    assert 4**Rational(3, 2) == 8
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q17", M, 17, "advanced_math", "equivalent_expressions",
        "hard",
        r"What is the value of $4^{\,3/2}$?",
        r"A fractional exponent means root then power: the denominator is the"
        r" root, the numerator the power."
        r" $$4^{3/2} = \left(\sqrt{4}\right)^3 = 2^3 = 8.$$"
        r" Multiplying the base by the exponent gives 6, and reading the"
        r" fraction upside down gives $4^{2/3} \approx 2.5$."
        r" The correct answer is **C**.",
        ["Eq(4**Rational(3,2), 8)", "Eq(sqrt(4)**3, 8)"],
        8, {2: "took only the square root", 6: "multiplied 4 by 3/2",
            64: "cubed 4 without taking the root"}, fmt=smart))

    assert (7 - 2) ** 2 + (14 - 2) ** 2 == 169
    qs.append(mcq_listed(
        "SAT-P9-M2H-Q18", M, 18, "geometry_trig", "circles", "hard",
        r"In the $xy$-plane, a circle has its center at $(2, 2)$ and passes"
        r" through $(7, 14)$. What is the radius of the circle?",
        {"A": r"$5$", "B": r"$12$", "C": r"$13$", "D": r"$17$"}, "C",
        r"The radius is the distance from the center to any point on the"
        r" circle:"
        r" $$r = \sqrt{(7 - 2)^2 + (14 - 2)^2} = \sqrt{25 + 144}"
        r" = \sqrt{169} = 13.$$"
        r" The legs 5 and 12 are the horizontal and vertical gaps, not the"
        r" radius, and adding them gives 17."
        r" The correct answer is **C**.",
        ["Eq((7 - 2)**2 + (14 - 2)**2, 169)", "Eq(sqrt(169), 13)"]))

    assert _solve(Eq(5 * x + 2 * (3 * x - 4), 47), x) == [5]
    qs.append(spr(
        "SAT-P9-M2H-Q19", M, 19, "algebra", "systems_two_linear", "hard",
        r"A shop sells notebooks for $\$5$ and folders for $\$2$. A customer"
        r" buys some notebooks and buys $4$ fewer than three times as many"
        r" folders as notebooks, spending $\$47$ in total. How many notebooks"
        r" were bought?",
        ["5"],
        r"Let $n$ be the notebooks. The folders number $3n - 4$, so the money"
        r" equation is"
        r" $$5n + 2(3n - 4) = 47.$$"
        r" Expand and solve:"
        r" $$5n + 6n - 8 = 47 \;\Rightarrow\; 11n = 55 \;\Rightarrow\; n = 5.$$"
        r" Check: 5 notebooks cost $\$25$, and $3(5) - 4 = 11$ folders cost"
        r" $\$22$, totalling $\$47$."
        r" The correct answer is **5**.",
        ["Eq(5*5 + 2*(3*5 - 4), 47)", "Eq(3*5 - 4, 11)", "Eq(25 + 22, 47)"]))

    assert Rational(60, 100) * Rational(150, 100) * 200 == 180
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q20", M, 20, "psda", "percentages", "hard",
        r"A quantity of $200$ is increased by $50\%$, and the result is then"
        r" decreased by $40\%$. What is the final value?",
        r"Percent changes multiply, each applied to the value BEFORE it:"
        r" $$200 \times 1.50 = 300, \qquad 300 \times 0.60 = 180.$$"
        r" The overall factor is $1.5 \times 0.6 = 0.9$, a net $10\%$"
        r" DECREASE — the $40\%$ cut is taken from the larger 300, so it"
        r" outweighs the earlier $50\%$ rise. Cancelling the percents as"
        r" $+50 - 40 = +10\%$ would wrongly give 220."
        r" The correct answer is **B**.",
        ["Eq(200*Rational(150,100), 300)", "Eq(300*Rational(60,100), 180)",
         "Eq(Rational(150,100)*Rational(60,100), Rational(9,10))"],
        180, {120: "applied both changes as decreases",
              210: "averaged the two results",
              220: "added the percents instead of multiplying"}, fmt=smart))

    assert 2 * (2 * 3 + 1) ** 2 == 98
    qs.append(mcq_numeric(
        "SAT-P9-M2H-Q21", M, 21, "advanced_math", "nonlinear_functions", "hard",
        r"The functions $f$ and $g$ are defined by $f(x) = 2x^2$ and"
        r" $g(x) = 2x + 1$. What is the value of $f(g(3))$?",
        r"Evaluate the inner function first:"
        r" $$g(3) = 2(3) + 1 = 7.$$"
        r" Then apply $f$ to that output:"
        r" $$f(7) = 2(7)^2 = 2(49) = 98.$$"
        r" Squaring before doubling inside $f$ is the order that matters:"
        r" $2 \cdot 7^2 = 98$, not $(2 \cdot 7)^2 = 196$. Composing the other"
        r" way gives $g(f(3)) = g(18) = 37$."
        r" The correct answer is **D**.",
        ["Eq(2*3 + 1, 7)", "Eq(2*7**2, 98)", "Eq(2*(3**2)*2 + 1, 37)"],
        98, {37: "composed in the reverse order", 49: "omitted the factor of 2",
             196: "doubled before squaring"}, fmt=smart))

    assert Rational(8, 2) == 4 and 4**2 == 16
    qs.append(spr(
        "SAT-P9-M2H-Q22", M, 22, "algebra", "linear_equations_two_var", "hard",
        r"In the $xy$-plane, the line $y = mx + 4$ passes through the point"
        r" $(6, 22)$. What is the value of $m$?",
        ["3"],
        r"Substitute the point into the equation:"
        r" $$22 = m(6) + 4 \;\Rightarrow\; 6m = 18 \;\Rightarrow\; m = 3.$$"
        r" Check: $3(6) + 4 = 22$."
        r" The correct answer is **3**.",
        ["Eq(3*6 + 4, 22)", "Eq(Rational(22 - 4, 6), 3)"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-9.json",
               {"testId": "sat-practice-9",
                "label": "SAT Math Practice Test 9",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
