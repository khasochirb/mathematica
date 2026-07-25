#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 12 (data/sat/sat-practice-12.json).

Built on scripts/test-builders/satbuild.py. Archetypes audited against
tests 1-11; new to the bank here:
  * the area of a TRAPEZOID, read from a scale figure
  * a linear rule recovered from a table of values
  * "what percent of A is B" (the percent as the unknown)
  * the product of the roots of a quadratic with a leading coefficient
  * a vertical asymptote of a rational function
  * the area of a SECTOR (not the arc length)
  * the effect on the mean of shifting every value by a constant
  * average speed over two legs (a harmonic, not arithmetic, mean)
  * a combined work-rate problem
  * association versus causation, and correlation strength
  * the tangent-radius right angle at a point of tangency
  * the ratio of AREAS of similar triangles
  * projectile height returning to the ground, and a log of a multiple

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
    assert _solve(Eq(7 * x + 4, 39), x) == [5]
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $7x + 4 = 39$, what is the value of $x$?",
        r"Subtract 4 from both sides, then divide by 7:"
        r" $$7x = 35 \;\Rightarrow\; x = 5.$$"
        r" Stopping at $7x = 35$ gives 35, and adding 4 instead of"
        r" subtracting gives $43/7$."
        r" The correct answer is **A**.",
        ["Eq(7*5 + 4, 39)", "Eq((39 - 4)/7, 5)"],
        5, {Rational(43, 7): "added 4 instead of subtracting",
            11: "solved $x + 4 = 39$ then divided",
            35: "stopped at $7x = 35$"},
        fmt=smart))

    # Q2 E adv
    assert expand((x - 4) * (x + 4)) == x**2 - 16
    qs.append(mcq_listed(
        "SAT-P12-M1-Q02", M, 2, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $(x - 4)(x + 4)$?",
        {"A": r"$x^2 - 16$", "B": r"$x^2 - 8x - 16$",
         "C": r"$x^2 + 8x - 16$", "D": r"$x^2 + 16$"},
        "A",
        r"Multiply out and watch the middle terms cancel:"
        r" $$(x - 4)(x + 4) = x^2 + 4x - 4x - 16 = x^2 - 16.$$"
        r" This is the difference of two squares: a sum times a"
        r" difference of the same two terms always loses its middle term."
        r" Testing $x = 5$: $(1)(9) = 9 = 25 - 16$."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 4)*(x + 4)), x**2 - 16)",
         "Eq((5 - 4)*(5 + 4), 5**2 - 16)"]))

    # Q3 E psda
    assert Rational(28, 80) * 100 == 35
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q03", M, 3, "psda", "percentages", "easy",
        r"What percent of 80 is 28?",
        r"Write the question as an equation with the percent unknown:"
        r" $$\frac{p}{100}\cdot 80 = 28 \;\Rightarrow\; p"
        r" = \frac{28}{80}\cdot 100 = 35.$$"
        r" So 28 is $35\%$ of 80. Dividing the other way round asks"
        r" \"what percent of 28 is 80?\" and gives about $286\%$; taking"
        r" $28\%$ of 80 gives $22.4$, a count rather than a percent."
        r" The correct answer is **C**.",
        ["Eq(Rational(28, 80)*100, 35)",
         "Eq(Rational(35, 100)*80, 28)", "Eq(80 - 28, 52)"],
        35, {Rational(112, 5): "computed $28\\%$ of 80",
             28: "repeated the given part as a percent",
             52: "subtracted 28 from 80"},
        fmt=smart))

    # Q4 E alg SPR
    assert _solve(Eq(4 * (x - 2), 20), x) == [7]
    qs.append(spr(
        "SAT-P12-M1-Q04", M, 4, "algebra", "linear_equations_one_var",
        "easy",
        r"If $4(x - 2) = 20$, what is the value of $x$?",
        ["7"],
        r"Divide both sides by 4 first:"
        r" $$x - 2 = 5 \;\Rightarrow\; x = 7.$$"
        r" Checking: $4(7 - 2) = 4(5) = 20$.",
        ["Eq(4*(7 - 2), 20)", "Eq(Rational(20, 4) + 2, 7)"]))

    # Q5 E geo — trapezoid figure
    B1, B2, H = 10, 6, 5
    assert Rational(1, 2) * (B1 + B2) * H == 40
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q05", M, 5, "geometry_trig", "area_perimeter", "easy",
        r"The figure shows a trapezoid whose parallel sides have lengths"
        r" 10 and 6 and whose height is 5. What is the area of the"
        r" trapezoid?",
        r"The area of a trapezoid is the AVERAGE of the two parallel"
        r" sides times the height:"
        r" $$A = \frac{1}{2}(10 + 6)(5) = \frac{1}{2}(16)(5) = 40.$$"
        r" Forgetting the factor of $\frac{1}{2}$ gives 80, and"
        r" multiplying only the longer base by the height gives 50."
        r" The correct answer is **A**.",
        ["Eq(Rational(1,2)*(10 + 6)*5, 40)", "Eq((10 + 6)*5, 80)",
         "Eq(10*6*5, 300)"],
        40, {50: "used only the longer base",
             80: "omitted the factor of one half",
             300: "multiplied all three given lengths"},
        fig=figure("sat-p12-m1-q05",
                   "Trapezoid with parallel sides 10 and 6 and height 5")))

    # Q6 E adv
    assert 3 * (-2) ** 2 == 12
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q06", M, 6, "advanced_math", "function_notation", "easy",
        r"The function $f$ is defined by $f(x) = 3x^2$. What is the value"
        r" of $f(-2)$?",
        r"Square first, then multiply:"
        r" $$f(-2) = 3(-2)^2 = 3(4) = 12.$$"
        r" Squaring a negative gives a positive, so the answer is not"
        r" $-12$. Multiplying before squaring produces $(-6)^2 = 36$."
        r" The correct answer is **C**.",
        ["Eq(3*(-2)**2, 12)", "Eq((3*(-2))**2, 36)"],
        12, {-12: "kept the sign of the input after squaring",
             -6: "multiplied without squaring",
             36: "squared $3x$ instead of $x$"}))

    # Q7 E alg — rule from a table (figure)
    XS, YS = [1, 2, 3, 4], [7, 11, 15, 19]
    assert all(yy == 4 * xx + 3 for xx, yy in zip(XS, YS))
    qs.append(mcq_listed(
        "SAT-P12-M1-Q07", M, 7, "algebra", "linear_models", "easy",
        r"The table shows several values of $x$ and their corresponding"
        r" values of $y$ for a linear relationship. Which equation"
        r" describes this relationship?",
        {"A": r"$y = 3x + 4$", "B": r"$y = 4x + 3$",
         "C": r"$y = 4x + 7$", "D": r"$y = 7x$"},
        "B",
        r"Each time $x$ increases by 1, $y$ increases by 4, so the slope"
        r" is 4:"
        r" $$11 - 7 = 4, \qquad 15 - 11 = 4, \qquad 19 - 15 = 4.$$"
        r" To find the intercept, back up one step from $x = 1$:"
        r" $$y = 4x + b \;\Rightarrow\; 7 = 4(1) + b \;\Rightarrow\; b = 3.$$"
        r" So $y = 4x + 3$; checking $x = 4$ gives $16 + 3 = 19$."
        r" Swapping the slope and intercept gives choice A, and reading"
        r" the first $y$-value as the intercept gives choice C."
        r" The correct answer is **B**.",
        ["Eq(4*1 + 3, 7)", "Eq(4*2 + 3, 11)", "Eq(4*4 + 3, 19)",
         "Ne(3*1 + 4, 11)"],
        fig=figure("sat-p12-m1-q07",
                   "Table of x values 1, 2, 3, 4 with y values 7, 11, 15, "
                   "and 19")))

    # Q8 E geo
    assert 2 * (3 * 4 + 3 * 5 + 4 * 5) == 94
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q08", M, 8, "geometry_trig", "solids_volume_surface",
        "easy",
        r"A rectangular prism has edge lengths 3, 4, and 5. What is the"
        r" surface area of the prism?",
        r"A rectangular prism has three pairs of congruent faces, so add"
        r" the three distinct face areas and double:"
        r" $$2(3 \cdot 4 + 3 \cdot 5 + 4 \cdot 5) = 2(12 + 15 + 20)"
        r" = 2(47) = 94.$$"
        r" The product $3 \cdot 4 \cdot 5 = 60$ is the VOLUME, and 47 is"
        r" only half the surface — each face has a twin."
        r" The correct answer is **D**.",
        ["Eq(3*4 + 3*5 + 4*5, 47)", "Eq(2*47, 94)", "Eq(3*4*5, 60)"],
        94, {12: "found the area of one face",
             47: "forgot that each face has a matching opposite face",
             60: "computed the volume"}))

    # Q9 M adv SPR — product of the roots
    assert expand((2 * x + 3) * (x - 5)) == 2 * x**2 - 7 * x - 15
    assert Rational(3, -2) * 5 == Rational(-15, 2)
    qs.append(spr(
        "SAT-P12-M1-Q09", M, 9, "advanced_math", "quadratic_equations",
        "medium",
        r"What is the product of the two solutions of"
        r" $2x^2 - 7x - 15 = 0$?",
        ["-15/2", "-7.5"],
        r"Factor the quadratic. Two numbers multiplying to"
        r" $2 \times (-15) = -30$ and adding to $-7$ are $3$ and $-10$,"
        r" which regroup as"
        r" $$2x^2 - 7x - 15 = (2x + 3)(x - 5) = 0.$$"
        r" The solutions are $x = -\frac{3}{2}$ and $x = 5$, so their"
        r" product is"
        r" $$-\frac{3}{2}\times 5 = -\frac{15}{2} = -7.5.$$"
        r" The shortcut agrees: for $ax^2 + bx + c$ the product of the"
        r" roots is $\frac{c}{a} = \frac{-15}{2}$ — the leading"
        r" coefficient must not be ignored.",
        ["Eq(expand((2*x + 3)*(x - 5)), 2*x**2 - 7*x - 15)",
         "Eq(Rational(-3,2)*5, Rational(-15,2))",
         "Eq(2*Rational(-3,2)**2 - 7*Rational(-3,2) - 15, 0)"]))

    # Q10 M psda
    assert 1 - Rational(1, 4) == Rational(3, 4)
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q10", M, 10, "psda", "probability", "medium",
        r"A fair coin is flipped twice. What is the probability that at"
        r" least one flip lands heads?",
        r"The four equally likely outcomes are HH, HT, TH, TT. \"At least"
        r" one head\" rules out only TT, so it is easiest to use the"
        r" complement:"
        r" $$P(\text{at least one head}) = 1 - P(\text{no heads})"
        r" = 1 - \frac{1}{4} = \frac{3}{4}.$$"
        r" Answering $\frac{1}{2}$ treats the two flips as one, and"
        r" $\frac{1}{4}$ is the probability of TWO heads."
        r" The correct answer is **C**.",
        ["Eq(1 - Rational(1,4), Rational(3,4))",
         "Eq(Rational(1,2)*Rational(1,2), Rational(1,4))"],
        Rational(3, 4),
        {Rational(1, 4): "found the probability of two heads",
         Rational(1, 2): "answered as if a single flip",
         1: "assumed a head is certain"},
        fmt=frac))

    # Q11 M alg
    _s11 = _solve([Eq(5 * x + 2 * y, 26), Eq(3 * x - 2 * y, 6)], [x, y],
                  dict=True)[0]
    assert _s11[x] == 4 and _s11[y] == 3
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q11", M, 11, "algebra", "systems_two_variables",
        "medium",
        r"$$5x + 2y = 26$$"
        r"$$3x - 2y = 6$$"
        r"If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $x + y$?",
        r"The $y$ terms are already opposites, so add the equations:"
        r" $$8x = 32 \;\Rightarrow\; x = 4.$$"
        r" Substituting into the second equation gives"
        r" $$12 - 2y = 6 \;\Rightarrow\; y = 3.$$"
        r" The question asks for the sum:"
        r" $$x + y = 4 + 3 = 7.$$"
        r" Reporting $x = 4$ or $y = 3$ alone stops one step short."
        r" The correct answer is **C**.",
        ["Eq(5*4 + 2*3, 26)", "Eq(3*4 - 2*3, 6)", "Eq(4 + 3, 7)"],
        7, {1: "computed $x - y$", 3: "reported $y$ alone",
            4: "reported $x$ alone"}))

    # Q12 M adv — vertical asymptote
    assert 2 - 2 == 0
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q12", M, 12, "advanced_math", "rational_functions",
        "medium",
        r"The graph of $y = \dfrac{x + 4}{x - 2}$ in the $xy$-plane has a"
        r" vertical asymptote. At what value of $x$ does it occur?",
        r"A vertical asymptote sits where the DENOMINATOR is zero while"
        r" the numerator is not:"
        r" $$x - 2 = 0 \;\Rightarrow\; x = 2.$$"
        r" At $x = 2$ the numerator is $6 \ne 0$, so the function blows"
        r" up rather than forming a hole. Setting the NUMERATOR to zero"
        r" gives $x = -4$, which is the $x$-INTERCEPT, not an asymptote."
        r" The correct answer is **C**.",
        ["Eq(2 - 2, 0)", "Ne(2 + 4, 0)", "Eq(-4 + 4, 0)"],
        2, {-4: "set the numerator to zero", -2: "used the wrong sign",
            4: "read the constant from the numerator"}))

    # Q13 M geo — sector area
    assert Rational(72, 360) * 10**2 == 20
    qs.append(mcq_listed(
        "SAT-P12-M1-Q13", M, 13, "geometry_trig", "circle_arcs_sectors",
        "medium",
        r"A circle has radius 10. What is the area of a sector of this"
        r" circle whose central angle measures $72^\circ$?",
        {"A": r"$4\pi$", "B": r"$20\pi$", "C": r"$40\pi$",
         "D": r"$100\pi$"},
        "B",
        r"A sector's area is the same fraction of the circle's area that"
        r" its angle is of a full turn:"
        r" $$A = \frac{72}{360}\cdot \pi(10)^2 = \frac{1}{5}\cdot 100\pi"
        r" = 20\pi.$$"
        r" Using the CIRCUMFERENCE instead of the area gives"
        r" $\frac{1}{5}(20\pi) = 4\pi$, which is the arc length, not the"
        r" sector area — and $100\pi$ is the whole circle."
        r" The correct answer is **B**.",
        ["Eq(Rational(72,360), Rational(1,5))",
         "Eq(Rational(72,360)*10**2, 20)", "Eq(Rational(1,5)*2*10, 4)"]))

    # Q14 M psda SPR — shifting every value
    assert Rational(8 * 15 + 8 * 4, 8) == 19
    qs.append(spr(
        "SAT-P12-M1-Q14", M, 14, "psda", "center_spread", "medium",
        r"The mean of a list of 8 numbers is 15. If 4 is added to each of"
        r" the 8 numbers, what is the mean of the new list?",
        ["19"],
        r"The eight numbers originally total $8 \times 15 = 120$. Adding"
        r" 4 to each one adds $8 \times 4 = 32$ to the total:"
        r" $$120 + 32 = 152,$$"
        r" so the new mean is"
        r" $$\frac{152}{8} = 19.$$"
        r" More directly: shifting every value by the same amount shifts"
        r" the mean by exactly that amount, $15 + 4 = 19$. (The spread —"
        r" range and standard deviation — is unchanged.)",
        ["Eq(8*15, 120)", "Eq(8*4, 32)", "Eq(Rational(120 + 32, 8), 19)",
         "Eq(15 + 4, 19)"]))

    # Q15 M alg — average speed
    assert Rational(30, 15) + Rational(30, 10) == 5
    assert Rational(60, 5) == 12
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q15", M, 15, "algebra", "ratios_rates_proportions",
        "medium",
        r"A cyclist rides 30 kilometres at a constant speed of 30"
        r" kilometres per hour and then rides another 30 kilometres at a"
        r" constant speed of 20 kilometres per hour. What is the"
        r" cyclist's average speed, in kilometres per hour, for the"
        r" entire 60-kilometre ride?",
        r"Average speed is total distance over total TIME, so find the"
        r" time for each leg:"
        r" $$\frac{30}{30} = 1 \text{ hour}, \qquad"
        r" \frac{30}{20} = 1.5 \text{ hours}.$$"
        r" The whole ride takes $1 + 1.5 = 2.5$ hours, so"
        r" $$\text{average speed} = \frac{60}{2.5} = 24"
        r" \text{ km per hour}.$$"
        r" Averaging the two speeds gives 25, which is too high — the"
        r" cyclist spends MORE time at the slower speed, so it carries"
        r" more weight."
        r" The correct answer is **B**.",
        ["Eq(Rational(30, 30) + Rational(30, 20), Rational(5,2))",
         "Eq(Rational(60)/Rational(5,2), 24)",
         "Eq(Rational(30 + 20, 2), 25)"],
        24, {20: "reported the slower speed",
             25: "averaged the two speeds directly",
             50: "added the two speeds"}))

    # Q16 M adv — reading an exponential model
    assert Rational(108, 100) == 1 + Rational(8, 100)
    qs.append(mcq_listed(
        "SAT-P12-M1-Q16", M, 16, "advanced_math", "exponential_models",
        "medium",
        r"The number of subscribers to a service $t$ years after 2020 is"
        r" modelled by $P(t) = 250(1.08)^t$. Which of the following best"
        r" describes the model?",
        {"A": r"The number of subscribers increases by 8 each year.",
         "B": r"The number of subscribers increases by 250 each year.",
         "C": r"The number of subscribers increases by $8\%$ each year.",
         "D": r"The number of subscribers increases by $108\%$ each"
              r" year."},
        "C",
        r"In the model $P(t) = a\,b^t$, the constant $a = 250$ is the"
        r" starting value and $b = 1.08$ is the yearly growth FACTOR."
        r" Splitting the factor,"
        r" $$1.08 = 1 + 0.08,$$"
        r" the 1 preserves the current total and the $0.08$ adds $8\%$ of"
        r" it, so subscribers grow by $8\%$ per year. Reading $1.08$ as"
        r" $108\%$ growth would mean slightly more than doubling each"
        r" year, and a fixed increase of 8 or 250 per year would be"
        r" LINEAR growth, not exponential."
        r" The correct answer is **C**.",
        ["Eq(Rational(108,100), 1 + Rational(8,100))",
         "Eq(250*Rational(108,100), 270)"]))

    # Q17 M adv — composition
    assert 2 ** (1 + 3) == 16
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q17", M, 17, "advanced_math", "function_composition",
        "medium",
        r"The functions $f$ and $g$ are defined by $f(x) = 2^x$ and"
        r" $g(x) = x + 3$. What is the value of $f(g(1))$?",
        r"Evaluate the inner function first:"
        r" $$g(1) = 1 + 3 = 4.$$"
        r" Then apply $f$ to that output:"
        r" $$f(4) = 2^4 = 16.$$"
        r" Reversing the order gives $g(f(1)) = g(2) = 5$, and computing"
        r" $f(1) = 2$ alone stops at the first step."
        r" The correct answer is **D**.",
        ["Eq(2**(1 + 3), 16)", "Eq(2**1 + 3, 5)"],
        16, {2: "stopped at $f(1)$", 5: "computed $g(f(1))$ instead",
             8: "used $2^3$"}))

    # Q18 H alg SPR — combined work rate
    assert Rational(1, 6) + Rational(1, 3) == Rational(1, 2)
    qs.append(spr(
        "SAT-P12-M1-Q18", M, 18, "algebra", "rational_equations", "hard",
        r"Pump A can fill a tank in 6 hours, and pump B can fill the same"
        r" tank in 3 hours. Working together at these constant rates, how"
        r" many hours will the two pumps take to fill the tank?",
        ["2"],
        r"Add RATES, not times. Pump A fills $\frac{1}{6}$ of the tank"
        r" per hour and pump B fills $\frac{1}{3}$, so together"
        r" $$\frac{1}{6} + \frac{1}{3} = \frac{1}{6} + \frac{2}{6}"
        r" = \frac{3}{6} = \frac{1}{2}$$"
        r" of the tank per hour. Filling one whole tank at half a tank"
        r" per hour takes"
        r" $$t = \frac{1}{\frac{1}{2}} = 2 \text{ hours}.$$"
        r" Averaging the two times would give $4.5$ hours — longer than"
        r" pump B alone, which is impossible once help arrives.",
        ["Eq(Rational(1,6) + Rational(1,3), Rational(1,2))",
         "Eq(2*Rational(1,2), 1)", "Eq(Rational(1,6)*2 + Rational(1,3)*2, 1)"]))

    # Q19 H psda — association vs causation
    assert 400 > 0
    qs.append(mcq_listed(
        "SAT-P12-M1-Q19", M, 19, "psda", "evaluating_claims_experiments",
        "hard",
        r"A researcher surveyed 400 randomly selected students at a large"
        r" school and found that students who ate breakfast tended to"
        r" have higher test scores than students who did not. Which of"
        r" the following is the most appropriate conclusion?",
        {"A": r"Eating breakfast causes test scores at this school to"
              r" rise.",
         "B": r"At this school, eating breakfast is associated with"
              r" higher test scores.",
         "C": r"Every student at this school who eats breakfast scores"
              r" higher than every student who does not.",
         "D": r"Nothing can be concluded, because only 400 of the"
              r" students were surveyed."},
        "B",
        r"The study is OBSERVATIONAL: the researcher recorded what"
        r" students already do rather than assigning breakfast at random."
        r" Such a design can establish an association but not a cause,"
        r" because a third factor — sleep, household routine, study"
        r" habits — could drive both. So choice A overreaches. Choice C"
        r" misreads a group tendency as a claim about every individual."
        r" Choice D is wrong in the opposite direction: the sample of 400"
        r" was randomly selected from this school, which is exactly what"
        r" licenses generalising to the school. Only an experiment with"
        r" random ASSIGNMENT could support a causal claim."
        r" The correct answer is **B**.",
        ["Eq(400, 400)", "400 > 0"]))

    # Q20 H geo — tangent line figure
    assert 9**2 + 12**2 == 15**2
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q20", M, 20, "geometry_trig", "circle_tangents", "hard",
        r"In the figure, the line through $P$ and $Q$ is tangent to the"
        r" circle with centre $O$ at point $P$. The radius $OP$ is 9 and"
        r" $OQ = 15$. What is the length of $\overline{PQ}$?",
        r"A tangent line is perpendicular to the radius drawn to the"
        r" point of tangency, so triangle $OPQ$ has a right angle at"
        r" $P$. That makes $\overline{OQ}$ the hypotenuse and"
        r" $\overline{PQ}$ a leg:"
        r" $$9^2 + PQ^2 = 15^2 \;\Rightarrow\; PQ^2 = 225 - 81 = 144"
        r" \;\Rightarrow\; PQ = 12.$$"
        r" Treating $\overline{PQ}$ as the hypotenuse instead would give"
        r" $\sqrt{81 + 225} \approx 17.5$; subtracting the lengths"
        r" directly gives 6."
        r" The correct answer is **B**.",
        ["Eq(9**2 + 12**2, 15**2)", "Eq(225 - 81, 144)",
         "Eq(sqrt(144), 12)"],
        12, {6: "subtracted the radius from $OQ$",
             24: "added the radius to $OQ$",
             135: "multiplied the two given lengths"},
        fig=figure("sat-p12-m1-q20",
                   "Circle with centre O, radius OP of length 9 drawn to "
                   "the point of tangency P, and segment OQ of length 15 "
                   "to an external point Q on the tangent line")))

    # Q21 H adv SPR — recover a coefficient from a point
    assert 2**2 + (-4) * 2 + 7 == 3
    qs.append(spr(
        "SAT-P12-M1-Q21", M, 21, "advanced_math", "quadratic_equations",
        "hard",
        r"In the $xy$-plane, the graph of $y = x^2 + bx + 7$ passes"
        r" through the point $(2, 3)$, where $b$ is a constant. What is"
        r" the value of $b$?",
        ["-4"],
        r"A point on the graph satisfies the equation, so substitute"
        r" $x = 2$ and $y = 3$:"
        r" $$3 = 2^2 + 2b + 7 = 4 + 2b + 7 = 2b + 11.$$"
        r" Solve for $b$:"
        r" $$2b = 3 - 11 = -8 \;\Rightarrow\; b = -4.$$"
        r" Checking, $y = x^2 - 4x + 7$ gives $4 - 8 + 7 = 3$ at $x = 2$,"
        r" as required.",
        ["Eq(2**2 + (-4)*2 + 7, 3)", "Eq(Rational(3 - 11, 2), -4)"]))

    # Q22 H alg — ratio of areas of similar triangles
    assert Rational(10, 6) ** 2 * 27 == 75
    qs.append(mcq_numeric(
        "SAT-P12-M1-Q22", M, 22, "algebra", "similar_figures_ratios",
        "hard",
        r"Two similar triangles have corresponding sides of length 6 and"
        r" 10. The area of the smaller triangle is 27. What is the area"
        r" of the larger triangle?",
        r"In similar figures every length scales by the same factor $k$,"
        r" and every AREA scales by $k^2$. Here"
        r" $$k = \frac{10}{6} = \frac{5}{3},"
        r" \qquad k^2 = \frac{25}{9},$$"
        r" so the larger area is"
        r" $$27 \cdot \frac{25}{9} = 75.$$"
        r" Scaling by the linear ratio instead gives 45, and cubing the"
        r" ratio — the rule for volumes, not areas — gives 125."
        r" The correct answer is **C**.",
        ["Eq(Rational(10, 6), Rational(5,3))",
         "Eq(27*Rational(5,3)**2, 75)", "Eq(27*Rational(5,3), 45)",
         "Eq(27*Rational(5,3)**3, 125)"],
        75, {31: "added the difference of the side lengths",
             45: "scaled by the linear ratio",
             125: "cubed the ratio, as for volumes"}))

    return qs


# ─── Module 2, easier form (11E / 9M / 2H) ────────────────────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg
    assert _solve(Eq(8 * x, 56), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $8x = 56$, what is the value of $x$?",
        r"Divide both sides by 8:"
        r" $$x = \frac{56}{8} = 7.$$"
        r" Subtracting 8 instead of dividing gives 48, and multiplying"
        r" gives 448."
        r" The correct answer is **B**.",
        ["Eq(8*7, 56)", "Eq(Rational(56, 8), 7)"],
        7, {Rational(7, 8): "divided 7 by 8", 48: "subtracted 8 from 56",
            448: "multiplied 56 by 8"},
        fmt=smart))

    # Q2 E adv
    assert expand(3 * (x + 4)) == 3 * x + 12
    qs.append(mcq_listed(
        "SAT-P12-M2E-Q02", M, 2, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $3(x + 4)$?",
        {"A": r"$3x + 4$", "B": r"$3x + 7$", "C": r"$3x + 12$",
         "D": r"$3x + 43$"},
        "C",
        r"Distribute the 3 across BOTH terms inside the parentheses:"
        r" $$3(x + 4) = 3x + 3(4) = 3x + 12.$$"
        r" Multiplying only the $x$ leaves the 4 untouched (choice A),"
        r" and adding instead of multiplying gives $3 + 4 = 7$"
        r" (choice B)."
        r" The correct answer is **C**.",
        ["Eq(expand(3*(x + 4)), 3*x + 12)", "Eq(3*(5 + 4), 3*5 + 12)"]))

    # Q3 E psda SPR
    assert Rational(3, 8) * 24 == 9
    qs.append(spr(
        "SAT-P12-M2E-Q03", M, 3, "psda", "ratios_rates_proportions", "easy",
        r"In a class of 24 students, $\dfrac{3}{8}$ of the students play"
        r" a musical instrument. How many of the students play a musical"
        r" instrument?",
        ["9"],
        r"Take three eighths of 24. One eighth is $24 \div 8 = 3$, so"
        r" $$\frac{3}{8}\times 24 = 3 \times 3 = 9.$$",
        ["Eq(Rational(24, 8), 3)", "Eq(Rational(3,8)*24, 9)"]))

    # Q4 E alg
    assert _solve(Eq(2 * x - 7, 5), x) == [6]
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q04", M, 4, "algebra", "linear_functions_evaluate",
        "easy",
        r"If $y = 2x - 7$ and $y = 5$, what is the value of $x$?",
        r"Substitute 5 for $y$ and solve:"
        r" $$5 = 2x - 7 \;\Rightarrow\; 2x = 12 \;\Rightarrow\; x = 6.$$"
        r" Substituting 5 for $x$ instead computes $2(5) - 7 = 3$, which"
        r" answers a different question."
        r" The correct answer is **C**.",
        ["Eq(2*6 - 7, 5)", "Eq(Rational(5 + 7, 2), 6)"],
        6, {-1: "subtracted 7 from 5 then halved",
            3: "substituted 5 for $x$ instead of $y$",
            12: "stopped at $2x = 12$"}))

    # Q5 E geo
    assert 5**2 == 25
    qs.append(mcq_listed(
        "SAT-P12-M2E-Q05", M, 5, "geometry_trig", "circle_basics", "easy",
        r"A circle has a radius of 5. What is the area of the circle?",
        {"A": r"$5\pi$", "B": r"$10\pi$", "C": r"$25\pi$",
         "D": r"$100\pi$"},
        "C",
        r"The area of a circle is $A = \pi r^2$:"
        r" $$A = \pi(5)^2 = 25\pi.$$"
        r" The value $10\pi$ is the CIRCUMFERENCE $2\pi r$, and $100\pi$"
        r" would come from using the diameter 10 in place of the radius."
        r" The correct answer is **C**.",
        ["Eq(5**2, 25)", "Eq(2*5, 10)", "Eq(10**2, 100)"]))

    # Q6 E adv
    assert Rational(7 + 1, 2) == 4
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q06", M, 6, "advanced_math", "function_notation",
        "easy",
        r"The function $f$ is defined by $f(x) = \dfrac{x + 1}{2}$. What"
        r" is the value of $f(7)$?",
        r"Substitute $x = 7$, doing the addition before the division:"
        r" $$f(7) = \frac{7 + 1}{2} = \frac{8}{2} = 4.$$"
        r" Dividing before adding gives $3.5 + 1 = 4.5$."
        r" The correct answer is **B**.",
        ["Eq(Rational(7 + 1, 2), 4)"],
        4, {Rational(7, 2): "divided 7 by 2 and ignored the $+1$",
            Rational(9, 2): "divided before adding",
            8: "forgot to divide by 2"},
        fmt=smart))

    # Q7 E alg SPR
    assert _solve(Eq(5 * x - 12, 3 * x + 8), x) == [10]
    qs.append(spr(
        "SAT-P12-M2E-Q07", M, 7, "algebra", "linear_equations_one_var",
        "easy",
        r"If $5x - 12 = 3x + 8$, what is the value of $x$?",
        ["10"],
        r"Collect the variable terms on one side and the constants on the"
        r" other:"
        r" $$5x - 3x = 8 + 12 \;\Rightarrow\; 2x = 20 \;\Rightarrow\; x = 10.$$"
        r" Checking: $5(10) - 12 = 38$ and $3(10) + 8 = 38$.",
        ["Eq(5*10 - 12, 3*10 + 8)", "Eq(Rational(20, 2), 10)"]))

    # Q8 E adv
    assert sqrt(81) + sqrt(16) == 13
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q08", M, 8, "advanced_math", "radicals", "easy",
        r"What is the value of $\sqrt{81} + \sqrt{16}$?",
        r"Take each square root separately, then add:"
        r" $$\sqrt{81} + \sqrt{16} = 9 + 4 = 13.$$"
        r" A square root does NOT distribute over a sum:"
        r" $\sqrt{81 + 16} = \sqrt{97} \approx 9.85$, which is not 13."
        r" Multiplying the roots gives 36."
        r" The correct answer is **A**.",
        ["Eq(sqrt(81), 9)", "Eq(sqrt(16), 4)", "Eq(9 + 4, 13)",
         "Ne(sqrt(97), 13)"],
        13, {36: "multiplied the two roots instead of adding",
             49: "halved 98", 97: "added under a single radical"}))

    # Q9 E alg
    assert 3 * 2 - 2 == 4
    qs.append(mcq_listed(
        "SAT-P12-M2E-Q09", M, 9, "algebra", "linear_functions_evaluate",
        "easy",
        r"Which of the following points lies on the graph of"
        r" $y = 3x - 2$ in the $xy$-plane?",
        {"A": r"$(0, 2)$", "B": r"$(1, 2)$", "C": r"$(2, 5)$",
         "D": r"$(3, 7)$"},
        "D",
        r"A point lies on the graph when its coordinates satisfy the"
        r" equation. Test each one:"
        r" $$x = 0:\; 3(0) - 2 = -2 \ne 2, \qquad"
        r" x = 1:\; 3(1) - 2 = 1 \ne 2,$$"
        r" $$x = 2:\; 3(2) - 2 = 4 \ne 5, \qquad"
        r" x = 3:\; 3(3) - 2 = 7 \;\checkmark.$$"
        r" Only $(3, 7)$ works."
        r" The correct answer is **D**.",
        ["Eq(3*3 - 2, 7)", "Ne(3*0 - 2, 2)", "Ne(3*1 - 2, 2)",
         "Ne(3*2 - 2, 5)"]))

    # Q10 E geo
    assert Rational(36, 4) == 9 and 9**2 == 81
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q10", M, 10, "geometry_trig", "area_perimeter",
        "easy",
        r"A square has a perimeter of 36. What is the area of the"
        r" square?",
        r"All four sides of a square are equal, so"
        r" $$s = \frac{36}{4} = 9.$$"
        r" The area is the side squared:"
        r" $$A = 9^2 = 81.$$"
        r" Repeating the perimeter gives 36, and 18 is half the"
        r" perimeter, not a side."
        r" The correct answer is **D**.",
        ["Eq(Rational(36, 4), 9)", "Eq(9**2, 81)", "Eq(4*9, 36)"],
        81, {9: "reported the side length",
             18: "reported half the perimeter",
             36: "repeated the perimeter"}))

    # Q11 E adv
    assert expand((x + 3) * (x + 4)) == x**2 + 7 * x + 12
    qs.append(mcq_listed(
        "SAT-P12-M2E-Q11", M, 11, "advanced_math", "polynomial_factors",
        "easy",
        r"Which of the following is a factor of $x^2 + 7x + 12$?",
        {"A": r"$x - 4$", "B": r"$x - 3$", "C": r"$x + 3$",
         "D": r"$x + 12$"},
        "C",
        r"Look for two numbers whose product is 12 and whose sum is 7:"
        r" those are 3 and 4. So"
        r" $$x^2 + 7x + 12 = (x + 3)(x + 4),$$"
        r" and $x + 3$ is a factor. Both signs are positive because the"
        r" constant and the middle coefficient are both positive — the"
        r" negative choices would give $x^2 - 7x + 12$."
        r" The correct answer is **C**.",
        ["Eq(expand((x + 3)*(x + 4)), x**2 + 7*x + 12)",
         "Eq((-3)**2 + 7*(-3) + 12, 0)"]))

    # Q12 M alg SPR
    assert _solve(Eq(3 * x + 2 * 3, 18), x) == [4]
    qs.append(spr(
        "SAT-P12-M2E-Q12", M, 12, "algebra", "systems_two_variables",
        "medium",
        r"$$3x + 2y = 18$$"
        r"$$y = 3$$"
        r"If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $x$?",
        ["4"],
        r"The second equation hands you $y$ directly, so substitute it"
        r" into the first:"
        r" $$3x + 2(3) = 18 \;\Rightarrow\; 3x + 6 = 18.$$"
        r" Then"
        r" $$3x = 12 \;\Rightarrow\; x = 4.$$",
        ["Eq(3*4 + 2*3, 18)", "Eq(Rational(18 - 6, 3), 4)"]))

    # Q13 M adv
    assert sum(_solve(Eq(x**2, 49), x)) == 0
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q13", M, 13, "advanced_math", "quadratic_equations",
        "medium",
        r"What is the sum of all values of $x$ that satisfy $x^2 = 49$?",
        r"Taking a square root gives TWO values:"
        r" $$x = 7 \quad\text{or}\quad x = -7,$$"
        r" since $(-7)^2 = 49$ as well. Their sum is"
        r" $$7 + (-7) = 0.$$"
        r" Remembering only the positive root gives 7, and adding the"
        r" magnitudes rather than the signed values gives 14."
        r" The correct answer is **A**.",
        ["Eq((-7)**2, 49)", "Eq(7 + (-7), 0)"],
        0, {7: "kept only the positive root",
            14: "added the magnitudes instead of the signed values",
            49: "restated the right side"}))

    # Q14 M psda
    assert Rational(3, 8) * 320 == 120
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q14", M, 14, "psda", "ratios_rates_proportions",
        "medium",
        r"In a survey, 3 out of every 8 people said they prefer tea. If"
        r" 320 people were surveyed, how many said they prefer tea?",
        r"Set up the proportion and scale:"
        r" $$\frac{3}{8} = \frac{n}{320} \;\Rightarrow\; n"
        r" = \frac{3}{8}\times 320 = 3 \times 40 = 120.$$"
        r" The other 200 people did not choose tea; $120 + 200 = 320$"
        r" checks the split."
        r" The correct answer is **B**.",
        ["Eq(Rational(320, 8), 40)", "Eq(Rational(3,8)*320, 120)",
         "Eq(120 + 200, 320)"],
        120, {40: "found one eighth of the group",
              200: "found how many did NOT prefer tea",
              240: "used 3 out of 4 instead of 3 out of 8"}))

    # Q15 M alg SPR
    assert 8 * 50 + 150 == 550
    qs.append(spr(
        "SAT-P12-M2E-Q15", M, 15, "algebra", "linear_models", "medium",
        r"The total cost $C$, in dollars, of producing $n$ items is given"
        r" by $C = 8n + 150$. For how many items is the total cost"
        r" $\$550$?",
        ["50"],
        r"Set the model equal to 550:"
        r" $$8n + 150 = 550.$$"
        r" Subtract the fixed cost:"
        r" $$8n = 400 \;\Rightarrow\; n = 50.$$"
        r" Dividing 550 by 8 without removing the $\$150$ setup cost"
        r" first would give about 69 items.",
        ["Eq(550 - 150, 400)", "Eq(Rational(400, 8), 50)",
         "Eq(8*50 + 150, 550)"]))

    # Q16 M adv
    assert abs(2 - 6) + abs(10 - 6) == 8
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q16", M, 16, "advanced_math", "absolute_value",
        "medium",
        r"The function $f$ is defined by $f(x) = |x - 6|$. What is the"
        r" value of $f(2) + f(10)$?",
        r"Evaluate each output, taking the absolute value last:"
        r" $$f(2) = |2 - 6| = |-4| = 4,$$"
        r" $$f(10) = |10 - 6| = |4| = 4.$$"
        r" Their sum is"
        r" $$4 + 4 = 8.$$"
        r" Both inputs sit 4 units from 6, which is why the two outputs"
        r" match. Dropping the absolute value on the first term gives"
        r" $-4 + 4 = 0$."
        r" The correct answer is **C**.",
        ["Eq(Abs(2 - 6), 4)", "Eq(Abs(10 - 6), 4)", "Eq(4 + 4, 8)"],
        8, {0: "dropped the absolute value on the first term",
            4: "evaluated only one of the two outputs",
            12: "added the inputs instead of the outputs"}))

    # Q17 M geo
    assert 9**2 + 12**2 == 15**2
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q17", M, 17, "geometry_trig", "pythagorean_theorem",
        "medium",
        r"A right triangle has legs of length 9 and 12. What is the"
        r" perimeter of the triangle?",
        r"Find the hypotenuse first:"
        r" $$h = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15.$$"
        r" The perimeter adds all three sides:"
        r" $$9 + 12 + 15 = 36.$$"
        r" Adding only the two legs gives 21, and $\frac{1}{2}(9)(12)$ is"
        r" the AREA, 54."
        r" The correct answer is **B**.",
        ["Eq(9**2 + 12**2, 225)", "Eq(sqrt(225), 15)",
         "Eq(9 + 12 + 15, 36)"],
        36, {15: "reported only the hypotenuse",
             21: "added only the two legs",
             54: "computed the area"}))

    # Q18 M alg
    assert Rational(3, 10) * 70 == 21 and Rational(5, 10) * 70 == 35
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q18", M, 18, "algebra", "percentages", "medium",
        r"If $30\%$ of a number is 21, what is $50\%$ of that number?",
        r"Recover the number first:"
        r" $$0.30n = 21 \;\Rightarrow\; n = \frac{21}{0.30} = 70.$$"
        r" Half of it is"
        r" $$0.50 \times 70 = 35.$$"
        r" A shortcut: $50\%$ is $\frac{5}{3}$ of $30\%$, and"
        r" $21 \times \frac{5}{3} = 35$. Taking $50\%$ of 21 instead"
        r" gives $10.5$."
        r" The correct answer is **D**.",
        ["Eq(Rational(3,10)*70, 21)", "Eq(Rational(5,10)*70, 35)",
         "Eq(21*Rational(5,3), 35)", "Eq(Rational(1,10)*70, 7)"],
        35, {7: "found $10\\%$ of the number",
             Rational(21, 2): "took $50\\%$ of 21",
             21: "repeated the given amount"},
        fmt=smart))

    # Q19 M adv SPR
    assert (9 - 4) ** 2 == 25
    qs.append(spr(
        "SAT-P12-M2E-Q19", M, 19, "advanced_math", "quadratic_equations",
        "medium",
        r"If $(x - 4)^2 = 25$ and $x > 0$, what is the value of $x$?",
        ["9"],
        r"Take the square root of both sides, keeping BOTH signs:"
        r" $$x - 4 = 5 \quad\text{or}\quad x - 4 = -5,$$"
        r" so $x = 9$ or $x = -1$. The condition $x > 0$ selects"
        r" $$x = 9.$$"
        r" Checking: $(9 - 4)^2 = 25$.",
        ["Eq((9 - 4)**2, 25)", "Eq((-1 - 4)**2, 25)", "9 > 0"]))

    # Q20 M psda
    assert Rational(5 + 8, 2) == Rational(13, 2)
    assert Rational(3 + 5 + 5 + 8 + 9 + 12, 6) == 7
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q20", M, 20, "psda", "center_spread", "medium",
        r"What is the median of the data set"
        r" $3,\ 5,\ 5,\ 8,\ 9,\ 12$?",
        r"There are six values — an even count — so the median is the"
        r" average of the two middle ones. In order, the third and fourth"
        r" values are 5 and 8:"
        r" $$\text{median} = \frac{5 + 8}{2} = 6.5.$$"
        r" The mode is 5 and the mean is"
        r" $\frac{42}{6} = 7$; all three summaries differ here."
        r" The correct answer is **B**.",
        ["Eq(Rational(5 + 8, 2), Rational(13,2))",
         "Eq(Rational(3 + 5 + 5 + 8 + 9 + 12, 6), 7)"],
        Rational(13, 2),
        {5: "reported the mode", 7: "reported the mean",
         12: "reported the largest value"},
        fmt=smart))

    # Q21 H adv
    assert 2 ** Rational(1, 2) > 0 and (sqrt(2)) ** 3 - 2 * sqrt(2) == 0
    qs.append(mcq_numeric(
        "SAT-P12-M2E-Q21", M, 21, "advanced_math", "polynomial_roots",
        "hard",
        r"The function $f$ is defined by $f(x) = x^3 - 2x$. If $f(a) = 0$"
        r" and $a > 0$, what is the value of $a^2$?",
        r"Factor out the common $x$:"
        r" $$x^3 - 2x = x(x^2 - 2) = 0,$$"
        r" so $x = 0$ or $x^2 = 2$. The condition $a > 0$ rules out"
        r" $a = 0$, leaving $a = \sqrt{2}$, and therefore"
        r" $$a^2 = 2.$$"
        r" Notice the question asks for $a^2$, not $a$, so no radical"
        r" appears in the answer. Answering 0 keeps the root that the"
        r" condition excludes."
        r" The correct answer is **C**.",
        ["Eq(expand(x*(x**2 - 2)), x**3 - 2*x)",
         "Eq((sqrt(2))**3 - 2*sqrt(2), 0)", "Eq(sqrt(2)**2, 2)"],
        2, {0: "kept the excluded root $a = 0$",
            1: "assumed $a = 1$", 4: "squared 2 a second time"}))

    # Q22 H alg SPR
    assert Rational(14 - 5, 4 - 1) == 3 and 5 - 3 * 1 == 2
    qs.append(spr(
        "SAT-P12-M2E-Q22", M, 22, "algebra", "linear_functions_slope",
        "hard",
        r"The line $y = mx + b$ passes through the points $(1, 5)$ and"
        r" $(4, 14)$. What is the value of $m + b$?",
        ["5"],
        r"Find the slope from the two points:"
        r" $$m = \frac{14 - 5}{4 - 1} = \frac{9}{3} = 3.$$"
        r" Substitute $(1, 5)$ to find the intercept:"
        r" $$5 = 3(1) + b \;\Rightarrow\; b = 2.$$"
        r" The question asks for the sum:"
        r" $$m + b = 3 + 2 = 5.$$"
        r" (Checking the other point: $3(4) + 2 = 14$.)",
        ["Eq(Rational(14 - 5, 4 - 1), 3)", "Eq(3*1 + 2, 5)",
         "Eq(3*4 + 2, 14)", "Eq(3 + 2, 5)"]))

    return qs


# ─── Module 2, harder form (2E / 7M / 13H) ────────────────────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg
    assert _solve(Eq(2 * x + 6, 20), x) == [7]
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $2x + 6 = 20$, what is the value of $x - 1$?",
        r"Solve for $x$ first:"
        r" $$2x = 14 \;\Rightarrow\; x = 7.$$"
        r" The question asks for $x - 1$:"
        r" $$7 - 1 = 6.$$"
        r" Stopping at $x = 7$ is the trap, and stopping at $2x = 14$"
        r" gives 14."
        r" The correct answer is **A**.",
        ["Eq(2*7 + 6, 20)", "Eq(7 - 1, 6)"],
        6, {7: "stopped at the value of $x$",
            14: "stopped at $2x = 14$",
            20: "restated the right side of the equation"}))

    # Q2 E adv
    assert (2**4) ** 3 == 2**12
    qs.append(mcq_listed(
        "SAT-P12-M2H-Q02", M, 2, "advanced_math", "exponent_rules", "easy",
        r"Which of the following is equivalent to $\left(x^4\right)^3$?",
        {"A": r"$3x^4$", "B": r"$x^7$", "C": r"$x^{12}$", "D": r"$x^{64}$"},
        "C",
        r"A power raised to a power MULTIPLIES the exponents:"
        r" $$\left(x^4\right)^3 = x^{4 \times 3} = x^{12}.$$"
        r" Testing at $x = 2$: $(16)^3 = 4096 = 2^{12}$. Adding the"
        r" exponents gives $x^7$, which is the rule for a product of"
        r" powers, not a power of a power."
        r" The correct answer is **C**.",
        ["Eq((2**4)**3, 4096)", "Eq(2**12, 4096)", "Eq(4*3, 12)"]))

    # Q3 M psda SPR
    assert Rational(3, 5) == Rational(3, 5)
    qs.append(spr(
        "SAT-P12-M2H-Q03", M, 3, "psda", "probability", "medium",
        r"A spinner has 5 equal sections numbered 1 through 5. The"
        r" spinner is spun once. What is the probability that it lands on"
        r" an odd number?",
        ["3/5", "0.6", ".6"],
        r"The odd numbers among $1, 2, 3, 4, 5$ are 1, 3, and 5 — three"
        r" of the five sections. Because the sections are equal, each is"
        r" equally likely, so"
        r" $$P(\text{odd}) = \frac{3}{5} = 0.6.$$"
        r" The two even sections give the complement,"
        r" $\frac{2}{5}$, and $\frac{3}{5} + \frac{2}{5} = 1$.",
        ["Eq(Rational(3, 5) + Rational(2, 5), 1)",
         "Eq(Rational(3,5), Rational(6,10))"]))

    # Q4 M alg
    assert _solve(Eq(3 * (x - 2), 2 * (x + 5)), x) == [16]
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q04", M, 4, "algebra", "linear_equations_one_var",
        "medium",
        r"If $3(x - 2) = 2(x + 5)$, what is the value of $x$?",
        r"Distribute on both sides:"
        r" $$3x - 6 = 2x + 10.$$"
        r" Collect the $x$ terms on one side and the constants on the"
        r" other:"
        r" $$x = 16.$$"
        r" Checking: $3(14) = 42$ and $2(21) = 42$. Distributing to only"
        r" the first term on each side gives $3x - 2 = 2x + 5$ and the"
        r" answer 7."
        r" The correct answer is **D**.",
        ["Eq(3*(16 - 2), 2*(16 + 5))", "Eq(3*16 - 6, 2*16 + 10)"],
        16, {4: "solved $3x - 6 = 2x + 10$ as $x = 4$",
             7: "distributed to only the first term on each side",
             8: "halved the correct value"}))

    # Q5 M geo — regular polygon from an exterior angle
    assert Rational(360, 24) == 15
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q05", M, 5, "geometry_trig", "polygon_angles",
        "medium",
        r"Each exterior angle of a regular polygon measures $24^\circ$."
        r" How many sides does the polygon have?",
        r"The exterior angles of any convex polygon sum to $360^\circ$,"
        r" and in a REGULAR polygon they are all equal, so"
        r" $$n = \frac{360}{24} = 15.$$"
        r" Using $180$ in place of $360$ gives 7.5, which is not even a"
        r" whole number of sides — a sign the wrong total was used. The"
        r" interior angle here is $180 - 24 = 156^\circ$."
        r" The correct answer is **B**.",
        ["Eq(Rational(360, 24), 15)", "Eq(180 - 24, 156)",
         "Eq(15*24, 360)"],
        15, {8: "used a total of 180 degrees and rounded",
             24: "repeated the given angle",
             156: "reported the interior angle"}))

    # Q6 M adv
    assert 4 * 6 - 1 == 3 * 6 + 5
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q06", M, 6, "advanced_math", "function_notation",
        "medium",
        r"The function $f$ is defined by $f(x) = 4x - 1$. If"
        r" $f(a) = 3a + 5$, what is the value of $a$?",
        r"Write out $f(a)$ and set it equal to the given expression:"
        r" $$4a - 1 = 3a + 5.$$"
        r" Subtract $3a$ from both sides and add 1:"
        r" $$a = 6.$$"
        r" Checking: $f(6) = 23$ and $3(6) + 5 = 23$."
        r" The correct answer is **C**.",
        ["Eq(4*6 - 1, 23)", "Eq(3*6 + 5, 23)"],
        6, {Rational(4, 7): "combined the terms as $7a = 4$",
            4: "solved $4a = 3a + 1$",
            24: "multiplied the correct value by 4"},
        fmt=smart))

    # Q7 M alg SPR
    assert 26 + 14 == 40 and 26 - 14 == 12
    qs.append(spr(
        "SAT-P12-M2H-Q07", M, 7, "algebra", "systems_two_variables",
        "medium",
        r"The sum of two numbers is 40, and their difference is 12. What"
        r" is the larger of the two numbers?",
        ["26"],
        r"Call the numbers $a$ and $b$ with $a > b$:"
        r" $$a + b = 40, \qquad a - b = 12.$$"
        r" Adding the two equations eliminates $b$:"
        r" $$2a = 52 \;\Rightarrow\; a = 26.$$"
        r" Then $b = 40 - 26 = 14$, and indeed $26 - 14 = 12$. In"
        r" general the larger number is the average of the sum and the"
        r" difference: $\frac{40 + 12}{2} = 26$.",
        ["Eq(26 + 14, 40)", "Eq(26 - 14, 12)",
         "Eq(Rational(40 + 12, 2), 26)"]))

    # Q8 M adv
    assert 3**2 - 6 * 3 + 5 == -4
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q08", M, 8, "advanced_math", "quadratic_vertex_form",
        "medium",
        r"The vertex of the graph of $y = x^2 - 6x + 5$ is the point"
        r" $(h, k)$. What is the value of $h + k$?",
        r"Complete the square to expose the vertex:"
        r" $$y = (x^2 - 6x + 9) - 9 + 5 = (x - 3)^2 - 4,$$"
        r" so the vertex is $(3, -4)$, giving"
        r" $$h + k = 3 + (-4) = -1.$$"
        r" (You can also find $h = -\frac{b}{2a} = 3$ and then evaluate"
        r" $y$ there.) Adding the magnitudes gives 7, and reporting"
        r" $h$ alone gives 3."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 3)**2 - 4), x**2 - 6*x + 5)",
         "Eq(3**2 - 6*3 + 5, -4)", "Eq(3 + (-4), -1)"],
        -1, {-7: "added the two coordinates with the wrong sign on $h$",
             3: "reported $h$ alone",
             7: "added the magnitudes of the coordinates"}))

    # Q9 M geo
    assert Rational(96, 6) == 16 and sqrt(16) == 4 and 4**3 == 64
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q09", M, 9, "geometry_trig", "solids_volume_surface",
        "medium",
        r"A cube has a surface area of 96 square centimetres. What is the"
        r" volume, in cubic centimetres, of the cube?",
        r"A cube has 6 congruent square faces, so each face has area"
        r" $$\frac{96}{6} = 16,$$"
        r" and the edge length is $\sqrt{16} = 4$. The volume is"
        r" $$4^3 = 64.$$"
        r" Using 16 as the edge instead of the face area gives an"
        r" enormous volume, and 96 is the surface area itself."
        r" The correct answer is **B**.",
        ["Eq(Rational(96, 6), 16)", "Eq(sqrt(16), 4)", "Eq(4**3, 64)"],
        64, {16: "reported the area of one face",
             96: "repeated the surface area",
             512: "used an edge of 8"}))

    # Q10 H alg — ab from a sum and a sum of squares
    assert (9**2 - 53) == 2 * 14
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q10", M, 10, "algebra", "algebraic_identities", "hard",
        r"If $a + b = 9$ and $a^2 + b^2 = 53$, what is the value of"
        r" $ab$?",
        r"Square the first equation and expand:"
        r" $$(a + b)^2 = a^2 + 2ab + b^2 = 81.$$"
        r" Substitute the known sum of squares:"
        r" $$53 + 2ab = 81 \;\Rightarrow\; 2ab = 28 \;\Rightarrow\; ab = 14.$$"
        r" (The two numbers are 2 and 7, which do satisfy both"
        r" conditions.) Forgetting to halve gives 28, and subtracting"
        r" halving twice gives 7."
        r" The correct answer is **C**.",
        ["Eq(expand((x + y)**2), x**2 + 2*x*y + y**2)",
         "Eq(9**2 - 53, 28)", "Eq(Rational(28, 2), 14)",
         "Eq(2 + 7, 9)", "Eq(2**2 + 7**2, 53)"],
        14, {-14: "reversed the subtraction",
             7: "divided 28 by 4 instead of 2",
             28: "forgot to divide by 2"}))

    # Q11 H adv
    assert Rational(3 ** (2 + 2), 3**2) == 9
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q11", M, 11, "advanced_math", "exponent_rules", "hard",
        r"The function $f$ is defined by $f(x) = 3^x$. What is the value"
        r" of $\dfrac{f(x + 2)}{f(x)}$ for any value of $x$?",
        r"Write both pieces as powers of 3 and subtract the exponents:"
        r" $$\frac{3^{x + 2}}{3^{x}} = 3^{(x + 2) - x} = 3^2 = 9.$$"
        r" The $x$ cancels entirely, so the ratio is the same constant"
        r" for every input — that constant growth factor over a fixed"
        r" step is what makes the function exponential. Testing $x = 2$:"
        r" $\frac{81}{9} = 9$. Answering 6 multiplies the base by the"
        r" exponent instead of raising it."
        r" The correct answer is **C**.",
        ["Eq(Rational(3**(2 + 2), 3**2), 9)",
         "Eq(Rational(3**(5 + 2), 3**5), 9)", "Eq(3**2, 9)"],
        9, {3: "reported the base", 6: "multiplied the base by 2",
            27: "used an exponent of 3"}))

    # Q12 H alg SPR
    assert Rational(8 - 4, 5 - (-3)) == Rational(1, 2)
    qs.append(spr(
        "SAT-P12-M2H-Q12", M, 12, "algebra", "linear_functions_slope",
        "hard",
        r"In the $xy$-plane, the line through the points $(-3, 4)$ and"
        r" $(5, k)$ has a slope of $\dfrac{1}{2}$. What is the value of"
        r" $k$?",
        ["8"],
        r"Write the slope formula with $k$ as the unknown:"
        r" $$\frac{k - 4}{5 - (-3)} = \frac{k - 4}{8} = \frac{1}{2}.$$"
        r" Multiply both sides by 8:"
        r" $$k - 4 = 4 \;\Rightarrow\; k = 8.$$"
        r" The run is $5 - (-3) = 8$, not $5 - 3 = 2$ — the double"
        r" negative is the step most often lost here.",
        ["Eq(5 - (-3), 8)", "Eq(Rational(8 - 4, 8), Rational(1,2))"]))

    # Q13 H adv — recover p from integer roots
    assert expand((x - 3) * (x - 8)) == x**2 - 11 * x + 24
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q13", M, 13, "advanced_math", "quadratic_equations",
        "hard",
        r"The equation $x^2 + px + 24 = 0$ has two positive integer"
        r" solutions whose difference is 5, where $p$ is a constant. What"
        r" is the value of $p$?",
        r"For $x^2 + px + 24$, the two roots multiply to 24 and add to"
        r" $-p$. List the positive integer pairs with product 24 and pick"
        r" the one differing by 5:"
        r" $$1 \cdot 24,\quad 2 \cdot 12,\quad 3 \cdot 8,\quad 4 \cdot 6,$$"
        r" and only $3$ and $8$ differ by 5. Since the roots must be"
        r" positive, the factorisation is"
        r" $$(x - 3)(x - 8) = x^2 - 11x + 24,$$"
        r" so $p = -11$. Dropping the sign gives 11, and using the pair"
        r" $2$ and $12$ gives 14."
        r" The correct answer is **A**.",
        ["Eq(expand((x - 3)*(x - 8)), x**2 - 11*x + 24)",
         "Eq(8 - 3, 5)", "Eq(3*8, 24)", "Eq(3 + 8, 11)", "Eq(2 + 12, 14)"],
        -11, {5: "reported the difference of the roots",
              11: "dropped the negative sign",
              14: "used the pair 2 and 12 and dropped the sign"}))

    # Q14 H psda — correlation
    assert Rational(82, 100) > Rational(1, 2)
    qs.append(mcq_listed(
        "SAT-P12-M2H-Q14", M, 14, "psda", "evaluating_claims_experiments",
        "hard",
        r"A researcher recorded the weekly study hours and the test"
        r" scores of 50 students and found a correlation coefficient of"
        r" $r = 0.82$ between them. Which of the following conclusions is"
        r" best supported by this result?",
        {"A": r"Studying more hours causes a student's test score to"
              r" rise.",
         "B": r"There is a strong positive association between study"
              r" hours and test scores for these students.",
         "C": r"About $82\%$ of the students in the group studied every"
              r" week.",
         "D": r"There is no relationship between study hours and test"
              r" scores."},
        "B",
        r"A correlation coefficient measures the strength and direction"
        r" of a LINEAR association. Its sign is positive here, so the two"
        r" quantities tend to rise together, and its size, $0.82$, is"
        r" close to the maximum of 1, so the association is strong."
        r" That is exactly choice B. Choice A claims causation, which"
        r" observational data cannot establish. Choice C misreads $r$ as"
        r" a percentage of students — $r$ is a unitless measure of fit,"
        r" not a count. Choice D contradicts a value far from 0."
        r" The correct answer is **B**.",
        ["Eq(Rational(82,100), Rational(41,50))",
         "Rational(82,100) < 1", "Rational(82,100) > 0"]))

    # Q15 H alg SPR — projectile returns to the ground
    assert -16 * 4**2 + 64 * 4 == 0
    qs.append(spr(
        "SAT-P12-M2H-Q15", M, 15, "algebra", "quadratic_models", "hard",
        r"The height, in feet, of a ball $t$ seconds after it is thrown"
        r" upward from the ground is given by $h(t) = -16t^2 + 64t$. For"
        r" what positive value of $t$ does the ball return to the"
        r" ground?",
        ["4"],
        r"The ball is on the ground when its height is 0:"
        r" $$-16t^2 + 64t = 0 \;\Rightarrow\; -16t(t - 4) = 0.$$"
        r" So $t = 0$ or $t = 4$. The value $t = 0$ is the instant of the"
        r" throw, so the ball lands at"
        r" $$t = 4 \text{ seconds}.$$"
        r" (The peak comes halfway, at $t = 2$, where"
        r" $h(2) = 64$ feet.)",
        ["Eq(-16*4**2 + 64*4, 0)", "Eq(-16*0**2 + 64*0, 0)",
         "Eq(-16*2**2 + 64*2, 64)"]))

    # Q16 H adv — log of a multiple
    assert 2**5 == 32 and 8 * 32 == 2**8
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q16", M, 16, "advanced_math", "logarithms", "hard",
        r"If $\log_2 x = 5$, what is the value of $\log_2 (8x)$?",
        r"A logarithm of a product is the sum of the logarithms:"
        r" $$\log_2(8x) = \log_2 8 + \log_2 x = 3 + 5 = 8.$$"
        r" Directly: $\log_2 x = 5$ means $x = 32$, so $8x = 256 = 2^8$"
        r" and the logarithm is 8. Multiplying the logarithms instead of"
        r" adding gives 40, and adding the 8 itself gives 13."
        r" The correct answer is **A**.",
        ["Eq(2**5, 32)", "Eq(8*32, 256)", "Eq(2**8, 256)",
         "Eq(3 + 5, 8)"],
        8, {13: "added 8 instead of $\\log_2 8$",
            15: "multiplied 5 by 3", 40: "multiplied 5 by 8"}))

    # Q17 H geo — cylinder radius from volume
    assert 5**2 * 8 == 200
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q17", M, 17, "geometry_trig", "solids_volume_surface",
        "hard",
        r"A right circular cylinder has a volume of $200\pi$ cubic"
        r" centimetres and a height of 8 centimetres. What is the radius"
        r" of the cylinder, in centimetres?",
        r"Start from $V = \pi r^2 h$ and substitute:"
        r" $$\pi r^2 (8) = 200\pi \;\Rightarrow\; r^2 = 25"
        r" \;\Rightarrow\; r = 5.$$"
        r" Reporting 25 stops at $r^2$, and dividing 200 by 4 instead of"
        r" 8 gives 50 — neither is a length."
        r" The correct answer is **A**.",
        ["Eq(5**2*8, 200)", "Eq(Rational(200, 8), 25)", "Eq(sqrt(25), 5)"],
        5, {10: "used $r^2 = 100$", 25: "reported $r^2$",
            50: "divided 200 by 4"}))

    # Q18 H alg
    assert 2**3 * 5 == 40
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q18", M, 18, "algebra", "exponent_equations", "hard",
        r"If $2^{x} = 5$, what is the value of $2^{x + 3}$?",
        r"Split the exponent into the part you know and the part you"
        r" don't:"
        r" $$2^{x + 3} = 2^{x}\cdot 2^{3} = 5 \times 8 = 40.$$"
        r" You never need the actual value of $x$ (it is an irrational"
        r" number near $2.32$). Adding 3 to the output instead of the"
        r" exponent gives 8, and using $2^5$ as the factor gives 32."
        r" The correct answer is **D**.",
        ["Eq(2**3, 8)", "Eq(8*5, 40)", "Eq(2**5, 32)"],
        40, {8: "reported $2^3$ alone",
             20: "multiplied 5 by 4",
             32: "reported $2^5$ instead of $2^x \\cdot 2^3$"}))

    # Q19 H adv SPR — third zero of a cubic
    assert expand((x - 1) * (x - 2) * (x + 3)) == x**3 - 7 * x + 6
    qs.append(spr(
        "SAT-P12-M2H-Q19", M, 19, "advanced_math", "polynomial_roots",
        "hard",
        r"The polynomial $q(x) = x^3 - 7x + 6$ has zeros at $x = 1$,"
        r" $x = 2$, and $x = k$. What is the value of $k$?",
        ["-3"],
        r"For a cubic written as $x^3 + bx^2 + \dots$, the three zeros"
        r" sum to $-b$. Here the $x^2$ term is missing, so $b = 0$ and"
        r" the zeros sum to 0:"
        r" $$1 + 2 + k = 0 \;\Rightarrow\; k = -3.$$"
        r" Confirming by multiplication,"
        r" $$(x - 1)(x - 2)(x + 3) = x^3 - 7x + 6,$$"
        r" and $q(-3) = -27 + 21 + 6 = 0$.",
        ["Eq(expand((x - 1)*(x - 2)*(x + 3)), x**3 - 7*x + 6)",
         "Eq((-3)**3 - 7*(-3) + 6, 0)", "Eq(1 + 2 + (-3), 0)"]))

    # Q20 H psda — weighted mean of two groups
    assert Rational(5 * 20 + 15 * 28, 20) == 26
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q20", M, 20, "psda", "center_spread", "hard",
        r"Group A consists of 5 values with a mean of 20, and group B"
        r" consists of 15 values with a mean of 28. What is the mean of"
        r" all 20 values combined?",
        r"Convert each mean back into a total:"
        r" $$5 \times 20 = 100, \qquad 15 \times 28 = 420.$$"
        r" Combine and divide by the total count:"
        r" $$\frac{100 + 420}{20} = \frac{520}{20} = 26.$$"
        r" Averaging the two means as $\frac{20 + 28}{2} = 24$ ignores"
        r" that group B is three times as large, so the combined mean"
        r" must sit closer to 28 than to 20."
        r" The correct answer is **C**.",
        ["Eq(5*20, 100)", "Eq(15*28, 420)",
         "Eq(Rational(100 + 420, 20), 26)", "Eq(Rational(20 + 28, 2), 24)"],
        26, {22: "weighted the two groups the wrong way round",
             24: "averaged the two means directly",
             28: "reported the larger group's mean"}))

    # Q21 H adv — composition with a sign condition
    assert (-1 - 3) ** 2 == 16
    qs.append(mcq_numeric(
        "SAT-P12-M2H-Q21", M, 21, "advanced_math", "function_composition",
        "hard",
        r"The functions $f$ and $g$ are defined by $f(x) = x^2$ and"
        r" $g(x) = x - 3$. If $f(g(x)) = 16$ and $x < 0$, what is the"
        r" value of $x$?",
        r"Build the composition and set it equal to 16:"
        r" $$f(g(x)) = (x - 3)^2 = 16.$$"
        r" Take the square root of both sides, keeping both signs:"
        r" $$x - 3 = 4 \quad\text{or}\quad x - 3 = -4,$$"
        r" so $x = 7$ or $x = -1$. The condition $x < 0$ selects"
        r" $$x = -1.$$"
        r" Checking: $g(-1) = -4$ and $f(-4) = 16$. Keeping only the"
        r" positive square root gives 7 and misses the negative solution"
        r" entirely."
        r" The correct answer is **B**.",
        ["Eq((-1 - 3)**2, 16)", "Eq((7 - 3)**2, 16)", "-1 < 0"],
        -1, {-7: "made a sign error on the second branch",
             1: "dropped the sign of the correct solution",
             7: "kept only the positive square root"}))

    # Q22 H alg SPR — proportion with binomials
    assert 4 * (2 * Rational(17, 3) - 3) == 5 * (Rational(17, 3) + 1)
    qs.append(spr(
        "SAT-P12-M2H-Q22", M, 22, "algebra", "rational_equations", "hard",
        r"If $\dfrac{2x - 3}{x + 1} = \dfrac{5}{4}$ and $x \ne -1$, what"
        r" is the value of $x$?",
        ["17/3"],
        r"Cross-multiply, then distribute on both sides:"
        r" $$4(2x - 3) = 5(x + 1) \;\Rightarrow\; 8x - 12 = 5x + 5.$$"
        r" Collect terms:"
        r" $$3x = 17 \;\Rightarrow\; x = \frac{17}{3}.$$"
        r" Checking, $2x - 3 = \frac{25}{3}$ and $x + 1 = \frac{20}{3}$,"
        r" whose ratio is $\frac{25}{20} = \frac{5}{4}$ as required.",
        ["Eq(4*(2*Rational(17,3) - 3), 5*(Rational(17,3) + 1))",
         "Eq(2*Rational(17,3) - 3, Rational(25,3))",
         "Eq(Rational(17,3) + 1, Rational(20,3))"]))

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
    write_test(REPO / "data" / "sat" / "sat-practice-12.json",
               {"testId": "sat-practice-12",
                "label": "SAT Math Practice Test 12",
                "minutesPerModule": 35,
                "module2Threshold": 15},
               {"module1": m1, "module2Easy": m2e, "module2Hard": m2h})


if __name__ == "__main__":
    main()
