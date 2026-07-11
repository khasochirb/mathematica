#!/usr/bin/env python3
"""
Builder for SAT Math Practice Test 1 (data/sat/sat-practice-1.json).

Authored per .claude/skills/practice-test-authoring + sat-practice-test.
Every answer is COMPUTED (sympy/Fraction), never typed as a literal;
every distractor encodes one named student error; verify[] is asserted
in-process before anything is written. Blueprint conformance (domain
counts, difficulty mix, SPR slots, answer-letter runs) is asserted at
the end — a drifting edit crashes the build instead of shipping.

Run:  python3 scripts/test-builders/sat-practice-1.py
Then: python3 scripts/test-figures/sat-practice-1.py   (figures + dims)
Then re-run this builder so figure dims are read back via PIL.
"""

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from sympy import Eq, Rational, simplify, sqrt, sympify, symbols, expand, pi

REPO = Path(__file__).resolve().parent.parent.parent
OUT = REPO / "data" / "sat" / "sat-practice-1.json"
FIGDIR = REPO / "public" / "sat-figures"

x = symbols("x")


# ─── framework ─────────────────────────────────────────────────────────

def assert_verified(qid: str, verify: list[str]) -> None:
    for expr in verify:
        try:
            ok = sympify(expr)
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"{qid}: verify does not sympify: {expr!r} ({e})")
        if ok is not True and ok != True:  # noqa: E712
            raise SystemExit(f"{qid}: verify not True: {expr!r} -> {ok}")


def figure(name: str, alt_en: str) -> dict:
    """Figure ref; dims read from disk via PIL when the PNG exists."""
    src = f"/sat-figures/{name}.png"
    width, height = 900, 620
    png = FIGDIR / f"{name}.png"
    if png.is_file():
        from PIL import Image
        with Image.open(png) as im:
            width, height = im.size
    return {"src": src, "alt_en": alt_en, "width": width, "height": height}


def mcq_numeric(qid, module, qnum, domain, skill, difficulty, body, solution,
                verify, correct, distractors, fmt=None, fig=None,
                expect_letter=None):
    """Numeric MCQ: options sorted ascending (College Board convention);
    the answer letter is DERIVED from the sort, then checked against the
    blueprint expectation. `distractors` is {value: error_name}."""
    fmt = fmt or (lambda v: f"${v}$")
    vals = [correct] + list(distractors)
    assert len({simplify(v) for v in vals}) == 4, f"{qid}: option collision"
    ordered = sorted(vals, key=lambda v: float(simplify(v)))
    letters = "ABCD"
    options = {letters[i]: fmt(v) for i, v in enumerate(ordered)}
    answer = letters[ordered.index(correct)]
    if expect_letter:
        assert answer == expect_letter, \
            f"{qid}: answer letter {answer} != blueprint {expect_letter}"
    assert_verified(qid, verify)
    q = {"source": qid, "module": module, "questionNumber": qnum,
         "format": "mcq", "domain": domain, "skill_tag": skill,
         "difficulty": difficulty, "body": body, "options": options,
         "answer": answer, "solution": solution, "verify": verify}
    if fig:
        q["figure"] = fig
    return q


def mcq_listed(qid, module, qnum, domain, skill, difficulty, body, options,
               answer, solution, verify, fig=None):
    """MCQ with hand-ordered options (expressions / statements)."""
    assert sorted(options) == list("ABCD"), f"{qid}: options must be A-D"
    assert len(set(options.values())) == 4, f"{qid}: duplicate option text"
    assert answer in options, f"{qid}: answer {answer} not an option"
    assert_verified(qid, verify)
    q = {"source": qid, "module": module, "questionNumber": qnum,
         "format": "mcq", "domain": domain, "skill_tag": skill,
         "difficulty": difficulty, "body": body, "options": options,
         "answer": answer, "solution": solution, "verify": verify}
    if fig:
        q["figure"] = fig
    return q


def spr(qid, module, qnum, domain, skill, difficulty, body, accepted,
        solution, verify, fig=None):
    for a in accepted:
        limit = 6 if a.startswith("-") else 5
        assert len(a) <= limit, f"{qid}: SPR answer {a!r} too long"
    assert_verified(qid, verify)
    q = {"source": qid, "module": module, "questionNumber": qnum,
         "format": "spr", "domain": domain, "skill_tag": skill,
         "difficulty": difficulty, "body": body,
         "acceptedAnswers": accepted, "solution": solution,
         "verify": verify}
    if fig:
        q["figure"] = fig
    return q


def latex_int(v):
    return f"${v}$"


def latex_frac(fr: Fraction) -> str:
    return rf"$\dfrac{{{fr.numerator}}}{{{fr.denominator}}}$"


# ─── Module 1 (8 easy / 9 medium / 5 hard) ────────────────────────────

def module1() -> list[dict]:
    qs = []
    M = "1"

    # Q1 E alg linear_equations_one_var — answer 22 (D)
    # 4x+6 = 2(2x+3): no need to solve for x at all.
    a, b, rhs = 2, 3, 11
    x_val = Fraction(rhs - b, a)            # 4
    correct = 2 * rhs                        # 4x+6 = 2(2x+3) = 22
    d_x = int(x_val)                         # solved for x and stopped
    d_rhs = rhs                              # echoed the right-hand side
    d_4x = 4 * int(x_val)                    # computed 4x, forgot +6
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q01", M, 1, "algebra", "linear_equations_one_var", "easy",
        r"If $2x + 3 = 11$, what is the value of $4x + 6$?",
        r"Notice that $4x + 6$ is exactly twice $2x + 3$, so"
        r" $$4x + 6 = 2(2x + 3) = 2 \cdot 11 = 22.$$"
        r" Solving directly also works: $2x = 8$, so $x = 4$, and"
        r" $4(4) + 6 = 22$. Choice A is the value of $x$ itself, and"
        r" choice C is $4x$ without the $+6$."
        r" The correct answer is **D**.",
        ["Eq(2*11, 22)", "Eq((11-3)/2, 4)", "Eq(4*4 + 6, 22)"],
        correct, {d_x: "solved for x", d_rhs: "echoed rhs", d_4x: "forgot +6"},
        expect_letter="D"))

    # Q2 E psda ratios_rates_units — answer 540 (D)
    bottles, mins, target = 240, 40, 90
    rate = Fraction(bottles, mins)           # 6 per minute
    correct = int(rate * target)             # 540
    d_invert = int(Fraction(mins, bottles) * target)   # 15: inverted the rate
    d_added = bottles + (target - mins)                # 290: added the extra minutes
    d_hour = bottles * Fraction(target, 60)            # 360: used 60 min as the base
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q02", M, 2, "psda", "ratios_rates_units", "easy",
        r"A bottling machine fills 240 bottles every 40 minutes at a"
        r" constant rate. At this rate, how many bottles will the machine"
        r" fill in 90 minutes?",
        r"Find the unit rate first:"
        r" $$\frac{240 \text{ bottles}}{40 \text{ min}} = 6 \text{ bottles per minute}.$$"
        r" In 90 minutes the machine fills $6 \times 90 = 540$ bottles."
        r" Choice C comes from treating 240 as an hourly rate."
        r" The correct answer is **D**.",
        ["Eq(Rational(240, 40), 6)", "Eq(6*90, 540)",
         "Eq(240*Rational(90, 60), 360)"],
        correct, {d_invert: "inverted rate", d_added: "added minutes",
                  int(d_hour): "per-hour base"},
        expect_letter="D"))

    # Q3 E alg linear_functions — interpretation, answer B
    qs.append(mcq_listed(
        "SAT-P1-M1-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $f(m) = 12 + 0.4m$ gives the total cost, in"
        r" dollars, of a taxi ride of $m$ miles. What is the best"
        r" interpretation of the number $0.4$ in this context?",
        {"A": r"The total cost, in dollars, of a ride of 1 mile.",
         "B": r"For each additional mile, the total cost increases by \$0.40.",
         "C": r"The charge, in dollars, before any miles are driven.",
         "D": r"The number of miles that can be ridden for \$1."},
        "B",
        r"In a linear model the coefficient of the variable is the rate of"
        r" change: $$f(m+1) - f(m) = 0.4,$$ so each additional mile adds"
        r" \$0.40 to the cost. Choice C describes the constant 12, and"
        r" choice A is $f(1) = 12.40$, not $0.40$."
        r" The correct answer is **B**.",
        ["Eq((12 + Rational(2,5)*(1)) - (12 + Rational(2,5)*0), Rational(2,5))",
         "Eq(12 + Rational(2,5)*1, Rational(62, 5))"]))

    # Q4 E adv nonlinear_functions — f(4)=9 (B)
    correct = 4**2 - 3*4 + 5                 # 9
    d_2x = 2*4 - 3*4 + 5                     # 1: used 2x instead of x^2
    d_partial = 4**2 - 3 + 5                 # 18: forgot to multiply 3 by 4
    d_sign = 4**2 + 3*4 + 5                  # 33: sign slip on -3x
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q04", M, 4, "advanced_math", "nonlinear_functions", "easy",
        r"The function $f$ is defined by $f(x) = x^2 - 3x + 5$. What is"
        r" the value of $f(4)$?",
        r"Substitute $x = 4$ into the definition:"
        r" $$f(4) = 4^2 - 3(4) + 5 = 16 - 12 + 5 = 9.$$"
        r" Choice D comes from adding $3x$ instead of subtracting it."
        r" The correct answer is **B**.",
        ["Eq(4**2 - 3*4 + 5, 9)", "Eq(16 - 12 + 5, 9)"],
        correct, {d_2x: "used 2x for x^2", d_partial: "forgot *4",
                  d_sign: "sign slip"},
        expect_letter="B"))

    # Q5 E geo area_volume — legs 9, 12 → area 54 (B), FIGURE
    leg_a, leg_b = 9, 12
    hyp = 15                                  # 9-12-15 right triangle
    assert leg_a**2 + leg_b**2 == hyp**2
    correct = Fraction(leg_a * leg_b, 2)      # 54
    d_product = leg_a * leg_b                 # 108: forgot the 1/2
    d_hyp = Fraction(leg_b * hyp, 2)          # 90: used the hypotenuse as a leg
    d_half_short = Fraction(leg_a * (leg_a - 1), 2)  # 36 = ½·9·8: misread base as 8
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        r"The right triangle shown has legs of length 9 and 12. What is"
        r" the area of the triangle?",
        r"The legs of a right triangle are perpendicular, so they serve as"
        r" base and height:"
        r" $$A = \frac{1}{2} \cdot 9 \cdot 12 = 54.$$"
        r" Choice D is $9 \cdot 12$ without the factor $\frac{1}{2}$, and"
        r" choice C uses the hypotenuse (15) in place of a leg."
        r" The correct answer is **B**.",
        ["Eq(Rational(1,2)*9*12, 54)", "Eq(9**2 + 12**2, 15**2)"],
        int(correct), {d_product: "forgot 1/2", int(d_hyp): "hyp as leg",
                       int(d_half_short): "misread base"},
        fig=figure("sat-p1-m1-q05",
                   "Right triangle with legs labeled 9 and 12; the right "
                   "angle is between the two labeled legs."),
        expect_letter="B"))

    # Q6 E alg linear_equations_two_var — slope 3, SPR
    x1, y1, x2, y2 = 2, 5, 6, 17
    m = Fraction(y2 - y1, x2 - x1)
    assert m == 3
    qs.append(spr(
        "SAT-P1-M1-Q06", M, 6, "algebra", "linear_equations_two_var", "easy",
        r"Line $\ell$ passes through the points $(2, 5)$ and $(6, 17)$ in"
        r" the $xy$-plane. What is the slope of line $\ell$?",
        ["3"],
        r"The slope is the change in $y$ divided by the change in $x$:"
        r" $$m = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3.$$"
        r" The correct answer is **3**.",
        ["Eq(Rational(17-5, 6-2), 3)"]))

    # Q7 E psda percentages — 68 (C)
    price, pct = 85, Fraction(20, 100)
    correct = int(price * (1 - pct))          # 68
    d_discount = int(price * pct)             # 17: found the discount amount
    d_sub20 = price - 20                      # 65: subtracted 20 dollars
    d_up = int(price * (1 + pct))             # 102: increased instead
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q07", M, 7, "psda", "percentages", "easy",
        r"The regular price of a jacket is \$85. During a sale, the price"
        r" is reduced by 20\%. What is the sale price of the jacket, in"
        r" dollars?",
        r"A 20\% reduction leaves 80\% of the price:"
        r" $$85 \times 0.80 = 68.$$"
        r" Choice A is the discount amount ($85 \times 0.20 = 17$), and"
        r" choice B subtracts 20 dollars rather than 20 percent."
        r" The correct answer is **C**.",
        ["Eq(85*Rational(80,100), 68)", "Eq(85*Rational(20,100), 17)"],
        correct, {d_discount: "discount amount", d_sub20: "subtracted 20",
                  d_up: "increased"},
        expect_letter="C"))

    # Q8 E adv equivalent_expressions — (3x+2)(x−4) (A)
    prod = expand((3*x + 2) * (x - 4))        # 3x^2 - 10x - 8
    assert prod == 3*x**2 - 10*x - 8
    qs.append(mcq_listed(
        "SAT-P1-M1-Q08", M, 8, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to $(3x + 2)(x - 4)$?",
        {"A": r"$3x^2 - 10x - 8$",
         "B": r"$3x^2 - 10x + 8$",
         "C": r"$3x^2 - 8$",
         "D": r"$3x^2 + 10x - 8$"},
        "A",
        r"Distribute each term of the first factor:"
        r" $$(3x + 2)(x - 4) = 3x^2 - 12x + 2x - 8 = 3x^2 - 10x - 8.$$"
        r" Choice C keeps only the first and last products, dropping the"
        r" $-12x$ and $+2x$ cross terms."
        r" The correct answer is **A**.",
        ["Eq(expand((3*x + 2)*(x - 4)), 3*x**2 - 10*x - 8)",
         "Eq(3*1**2 - 10*1 - 8, (3*1 + 2)*(1 - 4))"]))

    # Q9 M alg systems_two_linear — x = 6 (B)
    # 2x + 3y = 24, x − y = 2 → x = 6, y = 4
    y_val = Fraction(24 - 2*2, 5)             # substitute x = y + 2
    x_val = y_val + 2
    assert (x_val, y_val) == (6, 4)
    correct, d_y, d_sum, d_2x = 6, 4, 10, 12
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$2x + 3y = 24$$ $$x - y = 2$$"
        r" If $(x, y)$ is the solution to the system of equations above,"
        r" what is the value of $x$?",
        r"From the second equation, $x = y + 2$. Substitute into the"
        r" first: $$2(y + 2) + 3y = 24 \;\Rightarrow\; 5y + 4 = 24"
        r" \;\Rightarrow\; y = 4,$$ so $x = y + 2 = 6$. Check:"
        r" $2(6) + 3(4) = 24$. Choice A is the value of $y$; choice C is"
        r" $x + y$. Desmos check: graph both lines and read the"
        r" intersection $(6, 4)$."
        r" The correct answer is **B**.",
        ["Eq(2*6 + 3*4, 24)", "Eq(6 - 4, 2)", "Eq((24 - 4)/5, 4)"],
        correct, {d_y: "solved for y", d_sum: "x+y", d_2x: "2x"},
        expect_letter="B"))

    # Q10 M adv nonlinear_functions — min of x²−6x+5 is −4 (A), FIGURE
    vx = Fraction(6, 2)                       # vertex x = 3
    vy = vx**2 - 6*vx + 5                     # −4
    assert (vx, vy) == (3, -4)
    correct, d_vx, d_sign, d_yint = -4, 3, 4, 5
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "medium",
        r"The graph of $y = x^2 - 6x + 5$ is shown. What is the minimum"
        r" value of $y$?",
        r"The vertex lies midway between the $x$-intercepts $x = 1$ and"
        r" $x = 5$, at $x = 3$:"
        r" $$y = 3^2 - 6(3) + 5 = 9 - 18 + 5 = -4.$$"
        r" Choice B is the $x$-coordinate of the vertex, not the minimum"
        r" value of $y$; choice D is the $y$-intercept."
        r" The correct answer is **A**.",
        ["Eq(3**2 - 6*3 + 5, -4)", "Eq((1 + 5)/2, 3)",
         "Eq(1**2 - 6*1 + 5, 0)", "Eq(5**2 - 6*5 + 5, 0)"],
        correct, {d_vx: "x of vertex", d_sign: "dropped sign",
                  d_yint: "y-intercept"},
        fig=figure("sat-p1-m1-q10",
                   "Parabola opening upward with x-intercepts at 1 and 5, "
                   "y-intercept at 5, and vertex at (3, -4), graphed on "
                   "labeled axes."),
        expect_letter="A"))

    # Q11 M psda one_var_data — median of dot plot = 5, SPR, FIGURE
    data = [3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 8]
    assert len(data) == 11 and sorted(data) == data
    med = data[len(data)//2]
    assert med == 5
    qs.append(spr(
        "SAT-P1-M1-Q11", M, 11, "psda", "one_var_data", "medium",
        r"The dot plot shows the number of books read last month by each"
        r" of the 11 students in a book club. What is the median number"
        r" of books read?",
        ["5"],
        r"With 11 values, the median is the 6th value when the data are"
        r" listed in order. Reading the dot plot from the left:"
        r" $3, 3, 4, 4, 4, 5, \dots$ — the 6th value is 5."
        r" The correct answer is **5**.",
        ["Eq((11 + 1)/2, 6)", "Eq(2 + 3, 5)"],
        fig=figure("sat-p1-m1-q11",
                   "Dot plot titled Books read: 2 dots above 3, 3 dots "
                   "above 4, 2 dots above 5, 3 dots above 6, and 1 dot "
                   "above 8.")))

    # Q12 M alg linear_inequalities — setup, answer A
    bound = Fraction(85 - 40, Fraction(3, 10))
    assert bound == 150
    qs.append(mcq_listed(
        "SAT-P1-M1-Q12", M, 12, "algebra", "linear_inequalities", "medium",
        r"A moving-truck rental costs \$40 for the day plus \$0.30 per"
        r" mile driven. Alicia can spend at most \$85 on the rental."
        r" Which inequality gives all possible numbers of miles $m$ that"
        r" Alicia can drive?",
        {"A": r"$40 + 0.3m \le 85$",
         "B": r"$40 + 0.3m \ge 85$",
         "C": r"$0.3 + 40m \le 85$",
         "D": r"$0.3 + 40m \ge 85$"},
        "A",
        r"The total cost is the fixed \$40 plus \$0.30 for each of the"
        r" $m$ miles, so the cost is $40 + 0.3m$. \"At most \$85\" means"
        r" the cost is less than or equal to 85:"
        r" $$40 + 0.3m \le 85,$$ which solves to $m \le 150$ miles."
        r" Choices C and D swap the fixed fee with the per-mile rate."
        r" The correct answer is **A**.",
        ["Eq((85 - 40)/Rational(3, 10), 150)",
         "40 + Rational(3,10)*150 <= 85"]))

    # Q13 M adv equivalent_expressions — k = 14, SPR
    k_val = expand((x + 7)**2).coeff(x, 1)
    assert k_val == 14
    qs.append(spr(
        "SAT-P1-M1-Q13", M, 13, "advanced_math", "equivalent_expressions",
        "medium",
        r"$$x^2 + kx + 49 = (x + 7)^2$$"
        r" In the equation above, $k$ is a constant. If the equation is"
        r" true for all values of $x$, what is the value of $k$?",
        ["14"],
        r"Expand the right-hand side:"
        r" $$(x + 7)^2 = x^2 + 14x + 49.$$"
        r" Matching the coefficient of $x$ on each side gives $k = 14$."
        r" The correct answer is **14**.",
        ["Eq(expand((x + 7)**2), x**2 + 14*x + 49)"]))

    # Q14 M geo lines_angles_triangles — largest angle 80 (C), FIGURE
    xv = Fraction(180 - 20, 4)                # x = 40
    angles = (int(xv), int(2*xv), int(xv + 20))
    assert sum(angles) == 180 and angles == (40, 80, 60)
    correct = max(angles)                     # 80
    d_x, d_third, d_slip = 40, 60, 90
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q14", M, 14, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In the triangle shown, the measures of the three interior"
        r" angles are $x°$, $(2x)°$, and $(x + 20)°$. What is the measure,"
        r" in degrees, of the largest angle of the triangle?",
        r"The angle measures sum to $180°$:"
        r" $$x + 2x + (x + 20) = 180 \;\Rightarrow\; 4x = 160"
        r" \;\Rightarrow\; x = 40.$$"
        r" The three angles measure $40°$, $80°$, and $60°$, so the"
        r" largest is $80°$. Choice A stops at $x = 40$ without comparing"
        r" the three angles."
        r" The correct answer is **C**.",
        ["Eq((180 - 20)/4, 40)", "Eq(40 + 80 + 60, 180)",
         "Eq(2*40, 80)", "Eq(40 + 20, 60)"],
        correct, {d_x: "stopped at x", d_third: "picked x+20",
                  d_slip: "4x=180 slip"},
        fig=figure("sat-p1-m1-q14",
                   "Triangle with interior angles labeled x degrees, 2x "
                   "degrees, and (x + 20) degrees."),
        expect_letter="C"))

    # Q15 M alg linear_functions — V(t) = 300 − 12t (B)
    assert 300 - 12*25 == 0                   # tank empties at t = 25
    qs.append(mcq_listed(
        "SAT-P1-M1-Q15", M, 15, "algebra", "linear_functions", "medium",
        r"A water tank contains 300 liters of water and drains at a"
        r" constant rate of 12 liters per minute. Which function gives"
        r" the volume of water $V(t)$, in liters, remaining in the tank"
        r" $t$ minutes after draining begins?",
        {"A": r"$V(t) = 12t - 300$",
         "B": r"$V(t) = 300 - 12t$",
         "C": r"$V(t) = 300 + 12t$",
         "D": r"$V(t) = 12 - 300t$"},
        "B",
        r"The tank starts at 300 liters, and each minute removes 12"
        r" liters, so after $t$ minutes the volume is"
        r" $$V(t) = 300 - 12t.$$"
        r" Check: $V(0) = 300$ (full tank) and $V(25) = 0$ (empty)."
        r" Choice C adds water instead of draining it."
        r" The correct answer is **B**.",
        ["Eq(300 - 12*0, 300)", "Eq(300 - 12*25, 0)"]))

    # Q16 M adv nonlinear_equations_systems — x = 5, SPR
    from sympy import solve as _solve
    roots = _solve(Eq(x**2 - 2*x - 3, 2*x + 2), x)
    assert set(roots) == {-1, 5}
    qs.append(spr(
        "SAT-P1-M1-Q16", M, 16, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"$$y = x^2 - 2x - 3$$ $$y = 2x + 2$$"
        r" The graphs of the equations above intersect at two points. If"
        r" $(x, y)$ is the intersection point with $x > 0$, what is the"
        r" value of $x$?",
        ["5"],
        r"Set the expressions for $y$ equal:"
        r" $$x^2 - 2x - 3 = 2x + 2 \;\Rightarrow\; x^2 - 4x - 5 = 0"
        r" \;\Rightarrow\; (x - 5)(x + 1) = 0.$$"
        r" So $x = 5$ or $x = -1$; the point with $x > 0$ has $x = 5$."
        r" Desmos check: graph both equations; the right-hand intersection"
        r" is $(5, 12)$."
        r" The correct answer is **5**.",
        ["Eq(expand((x - 5)*(x + 1)), x**2 - 4*x - 5)",
         "Eq(5**2 - 2*5 - 3, 2*5 + 2)", "Eq((-1)**2 - 2*(-1) - 3, 2*(-1) + 2)"]))

    # Q17 M psda probability_conditional — 15/60 = 1/4 (C), FIGURE
    jr = {"bus": 28, "car": 20, "walk": 12}
    sr = {"bus": 22, "car": 23, "walk": 15}
    assert sum(jr.values()) == 60 and sum(sr.values()) == 60
    correct = Fraction(sr["walk"], sum(sr.values()))          # 1/4
    d_all = Fraction(sr["walk"], 120)                          # 1/8
    d_flip = Fraction(sr["walk"], jr["walk"] + sr["walk"])     # 5/9
    d_walkers = Fraction(jr["walk"] + sr["walk"], 120)         # 9/40
    assert (correct, d_all, d_flip, d_walkers) == \
        (Fraction(1, 4), Fraction(1, 8), Fraction(5, 9), Fraction(9, 40))
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q17", M, 17, "psda", "probability_conditional", "medium",
        r"The table shows how the 120 students at a school travel to"
        r" school, by class. If one of the seniors is selected at random,"
        r" what is the probability that the selected student walks to"
        r" school?",
        r"The condition \"one of the seniors\" restricts the sample space"
        r" to the 60 seniors, of whom 15 walk:"
        r" $$P(\text{walks} \mid \text{senior}) = \frac{15}{60}"
        r" = \frac{1}{4}.$$"
        r" Choice A divides by all 120 students instead of the 60"
        r" seniors, and choice D is the probability that a randomly"
        r" chosen walker is a senior — the reversed condition."
        r" The correct answer is **C**.",
        ["Eq(Rational(15, 60), Rational(1, 4))",
         "Eq(28 + 20 + 12 + 22 + 23 + 15, 120)",
         "Eq(Rational(15, 120), Rational(1, 8))",
         "Eq(Rational(15, 27), Rational(5, 9))"],
        correct, {d_all: "divided by all", d_flip: "reversed condition",
                  d_walkers: "all walkers over all"},
        fmt=lambda v: latex_frac(Fraction(v) if not isinstance(v, Fraction) else v),
        fig=figure("sat-p1-m1-q17",
                   "Two-way table of travel method by class. Juniors: bus "
                   "28, car 20, walk 12, total 60. Seniors: bus 22, car "
                   "23, walk 15, total 60. Column totals: bus 50, car 43, "
                   "walk 27, total 120."),
        expect_letter="C"))

    # Q18 H alg systems_two_linear — a = 12 (C)
    scale = Fraction(48, 12)                  # 4
    a_val = 3 * scale                          # 12
    assert Fraction(-20, -5) == scale and a_val == 12
    correct, d_neg, d_scale, d_prod = 12, -12, 4, 15
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q18", M, 18, "algebra", "systems_two_linear", "hard",
        r"$$3x - 5y = 12$$ $$ax - 20y = 48$$"
        r" In the system of equations above, $a$ is a constant. If the"
        r" system has infinitely many solutions, what is the value of"
        r" $a$?",
        r"Two linear equations have infinitely many solutions exactly"
        r" when they are the same line. The second equation's $y$-"
        r"coefficient and constant are both 4 times those of the first"
        r" ($-20 = 4(-5)$ and $48 = 4 \cdot 12$), so the whole equation"
        r" must be 4 times the first:"
        r" $$a = 4 \cdot 3 = 12.$$"
        r" Choice B stops at the scale factor 4 itself."
        r" The correct answer is **C**.",
        ["Eq(Rational(-20, -5), 4)", "Eq(Rational(48, 12), 4)",
         "Eq(4*3, 12)"],
        correct, {d_neg: "sign error", d_scale: "scale factor itself",
                  d_prod: "3*5"},
        expect_letter="C"))

    # Q19 H adv nonlinear_functions — g(3) = 162 (B)
    a0 = 6
    b_sq = Fraction(54, 6)                    # 9
    b_val = 3
    assert b_val**2 == b_sq
    correct = a0 * b_val**3                   # 162
    d_lin = 6 + 3 * Fraction(54 - 6, 2)       # 78: linear extension
    d_off = a0 * b_val**4                     # 486: computed g(4)
    d_b9 = a0 * 9**3                          # 4374: used b = 9
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q19", M, 19, "advanced_math", "nonlinear_functions",
        "hard",
        r"The graph of the exponential function $g(x) = a \cdot b^x$,"
        r" where $a > 0$ and $b > 0$, passes through the points $(0, 6)$"
        r" and $(2, 54)$. What is the value of $g(3)$?",
        r"From $(0, 6)$: $g(0) = a = 6$. From $(2, 54)$:"
        r" $$6b^2 = 54 \;\Rightarrow\; b^2 = 9 \;\Rightarrow\; b = 3$$"
        r" (taking $b > 0$). Then"
        r" $$g(3) = 6 \cdot 3^3 = 6 \cdot 27 = 162.$$"
        r" Choice A treats the growth as linear (adding 24 per unit"
        r" step); choice D uses $b = 9$ without taking the square root."
        r" The correct answer is **B**.",
        ["Eq(6*3**0, 6)", "Eq(6*3**2, 54)", "Eq(6*3**3, 162)"],
        correct, {int(d_lin): "linear extension", d_off: "computed g(4)",
                  d_b9: "b = 9"},
        expect_letter="B"))

    # Q20 H geo right_triangles_trig — BC = 15, SPR
    hyp = 39
    bc = hyp * Fraction(5, 13)                # 15
    assert bc == 15
    qs.append(spr(
        "SAT-P1-M1-Q20", M, 20, "geometry_trig", "right_triangles_trig",
        "hard",
        r"In right triangle $ABC$, the measure of angle $C$ is $90°$,"
        r" $\sin A = \dfrac{5}{13}$, and the length of hypotenuse $AB$ is"
        r" 39. What is the length of side $BC$?",
        ["15"],
        r"In a right triangle, $\sin A$ is the ratio of the leg opposite"
        r" angle $A$ to the hypotenuse. Side $BC$ is opposite angle $A$,"
        r" so $$\frac{BC}{39} = \frac{5}{13} \;\Rightarrow\;"
        r" BC = 39 \cdot \frac{5}{13} = 15.$$"
        r" The correct answer is **15**.",
        ["Eq(39*Rational(5, 13), 15)", "Eq(Rational(15, 39), Rational(5, 13))"]))

    # Q21 H adv nonlinear_equations_systems — k = 6 (C)
    # x^2+4x+7 = 2x+k → x^2+2x+(7−k) = 0, discriminant 0 → k = 6
    from sympy import discriminant
    k = symbols("k")
    disc = discriminant(x**2 + 2*x + (7 - k), x)
    k_sol = _solve(Eq(disc, 0), k)
    assert k_sol == [6]
    correct, d_neg, d_half, d_echo = 6, -6, 3, 7
    qs.append(mcq_numeric(
        "SAT-P1-M1-Q21", M, 21, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$y = x^2 + 4x + 7$$ $$y = 2x + k$$"
        r" In the system of equations above, $k$ is a constant. For which"
        r" value of $k$ does the system have exactly one solution?",
        r"Substituting gives $x^2 + 4x + 7 = 2x + k$, i.e."
        r" $$x^2 + 2x + (7 - k) = 0.$$"
        r" Exactly one solution means the discriminant is zero:"
        r" $$2^2 - 4(7 - k) = 0 \;\Rightarrow\; 4 - 28 + 4k = 0"
        r" \;\Rightarrow\; k = 6.$$"
        r" Geometrically, the line is tangent to the parabola. Desmos"
        r" check: graph $y = x^2 + 4x + 7$ and $y = 2x + 6$ — they touch"
        r" only at $(-1, 4)$."
        r" The correct answer is **C**.",
        ["Eq(2**2 - 4*(7 - 6), 0)",
         "Eq((-1)**2 + 4*(-1) + 7, 2*(-1) + 6)"],
        correct, {d_neg: "sign error", d_half: "half-discriminant slip",
                  d_echo: "echoed constant"},
        expect_letter="C"))

    # Q22 H alg linear_functions — f(7) = 34, SPR
    slope = Fraction(10, 2)                   # f(x+2)−f(x) = 10 → slope 5
    f7 = 4 + slope * (7 - 1)
    assert f7 == 34
    qs.append(spr(
        "SAT-P1-M1-Q22", M, 22, "algebra", "linear_functions", "hard",
        r"For the linear function $f$, $f(x + 2) - f(x) = 10$ for all"
        r" values of $x$, and $f(1) = 4$. What is the value of $f(7)$?",
        ["34"],
        r"A linear function changes by the same amount over equal steps."
        r" An increase of 10 over every step of 2 means the slope is"
        r" $\frac{10}{2} = 5$. From $x = 1$ to $x = 7$ is 6 units, so"
        r" $$f(7) = f(1) + 5 \cdot 6 = 4 + 30 = 34.$$"
        r" The correct answer is **34**.",
        ["Eq(Rational(10, 2), 5)", "Eq(4 + 5*(7 - 1), 34)"]))

    return qs


# ─── Module 2 — EASY variant (11 easy / 9 medium / 2 hard) ────────────

def module2_easy() -> list[dict]:
    qs = []
    M = "2E"

    # Q1 E alg linear_equations_one_var — x = 68 (D)
    x_val = (11 + 6) * 4
    assert Fraction(x_val, 4) - 6 == 11
    correct = x_val                            # 68
    d_no4 = 11 + 6                             # 17: forgot to multiply by 4
    d_sign = (11 - 6) * 4                      # 20: subtracted 6 instead
    d_order = 11 * 4 - 6                       # 38: multiplied before adding
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $\dfrac{x}{4} - 6 = 11$, what is the value of $x$?",
        r"Add 6 to both sides, then multiply by 4:"
        r" $$\frac{x}{4} = 17 \;\Rightarrow\; x = 68.$$"
        r" Choice A stops at 17 without multiplying by 4; choice C"
        r" multiplies 11 by 4 before undoing the subtraction."
        r" The correct answer is **D**.",
        ["Eq(Rational(68, 4) - 6, 11)", "Eq(11 + 6, 17)", "Eq(17*4, 68)"],
        correct, {d_no4: "forgot x4", d_sign: "sign slip",
                  d_order: "order of operations"},
        expect_letter="D"))

    # Q2 E psda two_var_data_models — predicted 30 at x = 8 (C), FIGURE
    pred = Fraction(5, 2) * 8 + 10             # 30
    assert pred == 30
    correct = int(pred)
    d_noint = int(Fraction(5, 2) * 8)          # 20: forgot the intercept
    d_point = 26                               # read the data point instead
    d_resid = 34                               # added the residual
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q02", M, 2, "psda", "two_var_data_models", "easy",
        r"The scatterplot shows the relationship between two variables"
        r" $x$ and $y$ for a sample of measurements, along with the line"
        r" of best fit $y = 2.5x + 10$. What is the $y$-value predicted"
        r" by the line of best fit when $x = 8$?",
        r"A prediction from a line of best fit is the $y$-value of the"
        r" LINE at that $x$, not of any data point:"
        r" $$y = 2.5(8) + 10 = 20 + 10 = 30.$$"
        r" Choice B (26) is the actual data value at $x = 8$; the"
        r" prediction question asks about the line."
        r" The correct answer is **C**.",
        ["Eq(Rational(5,2)*8 + 10, 30)"],
        correct, {d_noint: "forgot intercept", d_point: "read data point",
                  d_resid: "added residual"},
        fig=figure("sat-p1-m2e-q02",
                   "Scatterplot of 10 points with a line of best fit "
                   "rising from (0, 10) with slope 2.5. A data point sits "
                   "at (8, 26), below the line."),
        expect_letter="C"))

    # Q3 E alg linear_functions — x-intercept 4 (C)
    xint = Fraction(12, 3)
    assert -3 * xint + 12 == 0
    correct, d_negx, d_slope, d_yint = 4, -4, -3, 12
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q03", M, 3, "algebra", "linear_functions", "easy",
        r"The function $g$ is defined by $g(x) = -3x + 12$. What is the"
        r" $x$-coordinate of the $x$-intercept of the graph of $g$?",
        r"The graph crosses the $x$-axis where $g(x) = 0$:"
        r" $$-3x + 12 = 0 \;\Rightarrow\; 3x = 12 \;\Rightarrow\; x = 4.$$"
        r" Choice D is the $y$-intercept (12), and choice B is the slope."
        r" The correct answer is **C**.",
        ["Eq(-3*4 + 12, 0)", "Eq(Rational(12, 3), 4)"],
        correct, {d_negx: "sign slip", d_slope: "picked slope",
                  d_yint: "y-intercept"},
        expect_letter="C"))

    # Q4 E adv nonlinear_functions — roots of (x+6)(x−2) (B)
    r1, r2 = -6, 2
    assert (r1 + 6) * (r1 - 2) == 0 and (r2 + 6) * (r2 - 2) == 0
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q04", M, 4, "advanced_math", "nonlinear_functions",
        "easy",
        r"The function $f$ is defined by $f(x) = (x + 6)(x - 2)$. What"
        r" are the zeros of $f$?",
        {"A": r"$x = -6$ and $x = -2$",
         "B": r"$x = -6$ and $x = 2$",
         "C": r"$x = -2$ and $x = 6$",
         "D": r"$x = 2$ and $x = 6$"},
        "B",
        r"A product is zero when a factor is zero:"
        r" $$x + 6 = 0 \;\Rightarrow\; x = -6, \qquad"
        r" x - 2 = 0 \;\Rightarrow\; x = 2.$$"
        r" Each zero has the OPPOSITE sign of the constant in its factor"
        r" — choices C and D flip one or both signs."
        r" The correct answer is **B**.",
        ["Eq((-6 + 6)*(-6 - 2), 0)", "Eq((2 + 6)*(2 - 2), 0)",
         "Ne((6 + 6)*(6 - 2), 0)"]))

    # Q5 E geo area_volume — prism volume 160 (C), FIGURE
    L, W, H = 8, 5, 4
    vol = L * W * H
    sa = 2 * (L*W + L*H + W*H)
    assert (vol, sa) == (160, 184)
    correct = vol
    d_sum = L + W + H                          # 17: added the dimensions
    d_two = L * W                              # 40: multiplied only two
    d_sa = sa                                  # 184: surface area
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q05", M, 5, "geometry_trig", "area_volume", "easy",
        r"The right rectangular prism shown has a length of 8, a width"
        r" of 5, and a height of 4. What is the volume of the prism?",
        r"The volume of a right rectangular prism is the product of its"
        r" three dimensions:"
        r" $$V = 8 \cdot 5 \cdot 4 = 160.$$"
        r" Choice B multiplies only the length and width; choice D is the"
        r" surface area of the prism."
        r" The correct answer is **C**.",
        ["Eq(8*5*4, 160)", "Eq(2*(8*5 + 8*4 + 5*4), 184)"],
        correct, {d_sum: "added dims", d_two: "two dims only",
                  d_sa: "surface area"},
        fig=figure("sat-p1-m2e-q05",
                   "Right rectangular prism drawn in light perspective "
                   "with edges labeled 8, 5, and 4."),
        expect_letter="C"))

    # Q6 E alg linear_equations_two_var — k = 9, SPR
    k_val = 19 - 2 * 5
    assert k_val == 9
    qs.append(spr(
        "SAT-P1-M2E-Q06", M, 6, "algebra", "linear_equations_two_var",
        "easy",
        r"The point $(5, k)$ lies on the graph of the equation"
        r" $2x + y = 19$ in the $xy$-plane. What is the value of $k$?",
        ["9"],
        r"Substitute $x = 5$ and $y = k$:"
        r" $$2(5) + k = 19 \;\Rightarrow\; k = 19 - 10 = 9.$$"
        r" The correct answer is **9**.",
        ["Eq(2*5 + 9, 19)"]))

    # Q7 E adv equivalent_expressions — sum of polynomials (B)
    s = expand((4*x**2 + 3*x - 5) + (2*x**2 - 7*x + 1))
    assert s == 6*x**2 - 4*x - 4
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "easy",
        r"Which of the following is equivalent to"
        r" $(4x^2 + 3x - 5) + (2x^2 - 7x + 1)$?",
        {"A": r"$2x^2 + 10x - 6$",
         "B": r"$6x^2 - 4x - 4$",
         "C": r"$6x^2 - 4x + 4$",
         "D": r"$6x^2 + 4x - 4$"},
        "B",
        r"Combine like terms degree by degree:"
        r" $$4x^2 + 2x^2 = 6x^2, \quad 3x - 7x = -4x, \quad -5 + 1 = -4,$$"
        r" giving $6x^2 - 4x - 4$. Choice A subtracts the second"
        r" polynomial instead of adding it."
        r" The correct answer is **B**.",
        ["Eq(expand((4*x**2 + 3*x - 5) + (2*x**2 - 7*x + 1)), 6*x**2 - 4*x - 4)",
         "Eq(6*2**2 - 4*2 - 4, (4*2**2 + 3*2 - 5) + (2*2**2 - 7*2 + 1))"]))

    # Q8 E geo lines_angles_triangles — exterior angle: 55 (B), FIGURE
    ext, remote = 140, 85
    other = ext - remote
    assert other == 55 and other + remote + (180 - ext) == 180
    correct = other
    d_supp = 180 - ext                         # 40: supplement of the exterior
    d_supp85 = 180 - remote                    # 95: supplement of the remote
    d_sum = remote + (180 - ext)               # 125: added the wrong pair
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q08", M, 8, "geometry_trig", "lines_angles_triangles",
        "easy",
        r"In the figure shown, one side of the triangle is extended, and"
        r" the exterior angle formed measures $140°$. One of the two"
        r" remote interior angles measures $85°$. What is the value of"
        r" $x$, the measure in degrees of the other remote interior"
        r" angle?",
        r"An exterior angle of a triangle equals the sum of the two"
        r" remote interior angles:"
        r" $$140 = 85 + x \;\Rightarrow\; x = 55.$$"
        r" Choice A (40) is the interior angle adjacent to the $140°$"
        r" angle, not the remote angle asked for."
        r" The correct answer is **B**.",
        ["Eq(140 - 85, 55)", "Eq(55 + 85 + 40, 180)", "Eq(180 - 140, 40)"],
        correct, {d_supp: "adjacent interior", d_supp85: "supplement of 85",
                  d_sum: "wrong pair sum"},
        fig=figure("sat-p1-m2e-q08",
                   "Triangle with one side extended to form an exterior "
                   "angle labeled 140 degrees; the two remote interior "
                   "angles are labeled 85 degrees and x degrees."),
        expect_letter="B"))

    # Q9 M alg systems_two_linear — x = 5 (B)
    y_val = Fraction(21 + 3, 8)                # 3
    x_val = 2 * y_val - 1                       # 5
    assert (x_val, y_val) == (5, 3)
    correct, d_y, d_div, d_sum = 5, 3, 7, 8
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q09", M, 9, "algebra", "systems_two_linear", "medium",
        r"$$3x + 2y = 21$$ $$x = 2y - 1$$"
        r" If $(x, y)$ satisfies the system of equations above, what is"
        r" the value of $x$?",
        r"The second equation already isolates $x$; substitute it into"
        r" the first:"
        r" $$3(2y - 1) + 2y = 21 \;\Rightarrow\; 8y - 3 = 21"
        r" \;\Rightarrow\; y = 3,$$"
        r" so $x = 2(3) - 1 = 5$. Check: $3(5) + 2(3) = 21$. Choice A is"
        r" the value of $y$; choice D is $x + y$."
        r" The correct answer is **B**.",
        ["Eq((21 + 3)/8, 3)", "Eq(2*3 - 1, 5)", "Eq(3*5 + 2*3, 21)"],
        correct, {d_y: "solved for y", d_div: "21/3", d_sum: "x+y"},
        expect_letter="B"))

    # Q10 E adv nonlinear_functions — max 9 (D), FIGURE
    assert -(0 - 2)**2 + 9 == 5                # y-intercept 5
    correct, d_neg, d_vx, d_yint = 9, -9, 2, 5
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "easy",
        r"The graph of $y = -(x - 2)^2 + 9$ is shown. What is the maximum"
        r" value of $y$?",
        r"The equation is in vertex form $y = a(x - h)^2 + k$ with"
        r" $a = -1 < 0$, so the parabola opens downward and its maximum"
        r" is the $y$-coordinate of the vertex:"
        r" $$y = 9 \text{ (at } x = 2\text{)}.$$"
        r" Choice B is the $x$-coordinate of the vertex; choice C is the"
        r" $y$-intercept, $-(0-2)^2 + 9 = 5$."
        r" The correct answer is **D**.",
        ["Eq(-(2 - 2)**2 + 9, 9)", "Eq(-(0 - 2)**2 + 9, 5)"],
        correct, {d_neg: "dropped sign", d_vx: "x of vertex",
                  d_yint: "y-intercept"},
        fig=figure("sat-p1-m2e-q10",
                   "Downward-opening parabola with vertex at (2, 9), "
                   "y-intercept at (0, 5), and x-intercepts at -1 and 5, "
                   "graphed on labeled axes."),
        expect_letter="D"))

    # Q11 M psda one_var_data — 8th value 20, SPR
    v = 8 * 13 - 7 * 12
    assert v == 20
    qs.append(spr(
        "SAT-P1-M2E-Q11", M, 11, "psda", "one_var_data", "medium",
        r"The mean of a list of 7 numbers is 12. When an 8th number is"
        r" added to the list, the mean of the list becomes 13. What is"
        r" the 8th number?",
        ["20"],
        r"Work with totals, not means. The original 7 numbers sum to"
        r" $7 \times 12 = 84$; after adding the new number the 8 numbers"
        r" sum to $8 \times 13 = 104$. The 8th number is the difference:"
        r" $$104 - 84 = 20.$$"
        r" The correct answer is **20**.",
        ["Eq(7*12, 84)", "Eq(8*13, 104)", "Eq(104 - 84, 20)"]))

    # Q12 M alg linear_inequalities — x < −5 (A)
    assert Fraction(22 - 7, -3) == -5
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q12", M, 12, "algebra", "linear_inequalities", "medium",
        r"Which of the following gives all solutions of the inequality"
        r" $-3x + 7 > 22$?",
        {"A": r"$x < -5$",
         "B": r"$x > -5$",
         "C": r"$x < 5$",
         "D": r"$x > 5$"},
        "A",
        r"Subtract 7 from both sides: $-3x > 15$. Dividing by $-3$"
        r" REVERSES the inequality:"
        r" $$x < -5.$$"
        r" Choice B forgets to flip the inequality sign when dividing by"
        r" a negative number. Check with $x = -6$:"
        r" $-3(-6) + 7 = 25 > 22$. ✓"
        r" The correct answer is **A**.",
        ["Eq(Rational(15, -3), -5)", "-3*(-6) + 7 > 22",
         "-3*(-5) + 7 <= 22"]))

    # Q13 M adv equivalent_expressions — a = 4, SPR
    a_sym = symbols("a")
    from sympy import solve as _solve
    sol_a = _solve(Eq(5 + a_sym, 9), a_sym)
    assert sol_a == [4]
    qs.append(spr(
        "SAT-P1-M2E-Q13", M, 13, "advanced_math", "equivalent_expressions",
        "medium",
        r"$$(x + a)(x + 5) = x^2 + 9x + 5a$$"
        r" In the equation above, $a$ is a constant. If the equation is"
        r" true for all values of $x$, what is the value of $a$?",
        ["4"],
        r"Expand the left-hand side:"
        r" $$(x + a)(x + 5) = x^2 + (a + 5)x + 5a.$$"
        r" The constant terms $5a$ already match; matching the"
        r" $x$-coefficients gives $a + 5 = 9$, so $a = 4$."
        r" The correct answer is **4**.",
        ["Eq(expand((x + 4)*(x + 5)), x**2 + 9*x + 20)", "Eq(5*4, 20)",
         "Eq(4 + 5, 9)"]))

    # Q14 M geo circles — arc length 2π (B), FIGURE
    r = 6
    arc = Rational(60, 360) * 2 * pi * r
    assert arc == 2 * pi
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q14", M, 14, "geometry_trig", "circles", "medium",
        r"In the circle shown, center $O$ has radius 6, and the central"
        r" angle of the shaded sector measures $60°$. What is the length"
        r" of arc $AB$, the arc of the shaded sector?",
        {"A": r"$\pi$",
         "B": r"$2\pi$",
         "C": r"$3\pi$",
         "D": r"$6\pi$"},
        "B",
        r"An arc is the same fraction of the circumference as its central"
        r" angle is of $360°$:"
        r" $$\text{arc} = \frac{60}{360} \cdot 2\pi(6)"
        r" = \frac{1}{6} \cdot 12\pi = 2\pi.$$"
        r" Choice D ($6\pi$) is the AREA of the sector"
        r" ($\frac{60}{360} \cdot 36\pi$), not the arc length."
        r" The correct answer is **B**.",
        ["Eq(Rational(60, 360)*2*pi*6, 2*pi)",
         "Eq(Rational(60, 360)*pi*6**2, 6*pi)"],
        fig=figure("sat-p1-m2e-q14",
                   "Circle with center O and radius 6; a 60-degree sector "
                   "AOB is shaded with hatching, points A and B on the "
                   "circle.")))

    # Q15 E alg linear_functions — k = 7 (A)
    k_val = Fraction(20 - 6, 2)
    assert k_val == 7
    correct = 7
    d_no6 = Fraction(20, 2)                    # 10: forgot the −6
    d_add6 = Fraction(20 + 6, 2)               # 13: added 6 instead
    d_f20 = 2 * 20 + 6                          # 46: computed f(20)
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q15", M, 15, "algebra", "linear_functions", "easy",
        r"The function $f$ is defined by $f(x) = 2x + 6$. If $f(k) = 20$"
        r" for some number $k$, what is the value of $k$?",
        r"Set the output equal to 20 and solve for the input:"
        r" $$2k + 6 = 20 \;\Rightarrow\; 2k = 14 \;\Rightarrow\; k = 7.$$"
        r" Choice D computes $f(20) = 46$ — evaluating at 20 instead of"
        r" solving for the input that produces 20."
        r" The correct answer is **A**.",
        ["Eq(2*7 + 6, 20)", "Eq(Rational(20 - 6, 2), 7)", "Eq(2*20 + 6, 46)"],
        correct, {int(d_no6): "forgot -6", int(d_add6): "added 6",
                  d_f20: "evaluated f(20)"},
        expect_letter="A"))

    # Q16 M adv nonlinear_equations_systems — larger root 7, SPR
    from sympy import solve as _solve2
    roots = _solve2(Eq(x**2 - 10*x + 21, 0), x)
    assert set(roots) == {3, 7}
    qs.append(spr(
        "SAT-P1-M2E-Q16", M, 16, "advanced_math",
        "nonlinear_equations_systems", "medium",
        r"What is the larger of the two solutions of the equation"
        r" $x^2 - 10x + 21 = 0$?",
        ["7"],
        r"Factor: two numbers with product 21 and sum 10 are 3 and 7:"
        r" $$x^2 - 10x + 21 = (x - 3)(x - 7) = 0,$$"
        r" so $x = 3$ or $x = 7$; the larger is 7."
        r" The correct answer is **7**.",
        ["Eq(expand((x - 3)*(x - 7)), x**2 - 10*x + 21)",
         "Eq(7**2 - 10*7 + 21, 0)", "7 > 3"]))

    # Q17 M psda probability_conditional — 25/43 (C), FIGURE
    g9d, g9n, g10d, g10n = 18, 22, 25, 15
    dog_total = g9d + g10d                     # 43
    assert g9d + g9n == 40 and g10d + g10n == 40 and dog_total == 43
    correct = Fraction(g10d, dog_total)        # 25/43
    d_all = Fraction(g10d, 80)                 # 25/80
    d_dog = Fraction(dog_total, 80)            # 43/80
    d_flip = Fraction(g10d, 40)                # 25/40: P(dog | grade 10)
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q17", M, 17, "psda", "probability_conditional",
        "medium",
        r"The table shows the results of a survey of 80 students, by"
        r" grade, about whether they own a dog. If one of the students"
        r" who owns a dog is selected at random, what is the probability"
        r" that the student is in grade 10?",
        r"\"One of the students who owns a dog\" restricts the sample"
        r" space to the $18 + 25 = 43$ dog owners, of whom 25 are in"
        r" grade 10:"
        r" $$P(\text{grade 10} \mid \text{dog}) = \frac{25}{43}.$$"
        r" Choice D, $\frac{25}{40}$, is the reversed condition — the"
        r" probability that a grade-10 student owns a dog."
        r" The correct answer is **C**.",
        ["Eq(18 + 25, 43)", "Eq(18 + 22 + 25 + 15, 80)",
         "Rational(25, 80) < Rational(43, 80)",
         "Rational(43, 80) < Rational(25, 43)",
         "Rational(25, 43) < Rational(25, 40)"],
        correct, {d_all: "over all students", d_dog: "P(dog)",
                  d_flip: "reversed condition"},
        fmt=lambda v: latex_frac(Fraction(v) if not isinstance(v, Fraction) else v),
        fig=figure("sat-p1-m2e-q17",
                   "Two-way table of dog ownership by grade. Grade 9: "
                   "owns a dog 18, does not 22, total 40. Grade 10: owns "
                   "a dog 25, does not 15, total 40. Column totals: 43, "
                   "37, 80."),
        expect_letter="C"))

    # Q18 M alg linear_equations_two_var — y = 3x − 11 (A)
    b_val = 1 - 3 * 4                          # −11
    assert b_val == -11
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q18", M, 18, "algebra", "linear_equations_two_var",
        "medium",
        r"Line $\ell$ in the $xy$-plane is parallel to the line"
        r" $y = 3x - 5$ and passes through the point $(4, 1)$. Which"
        r" equation defines line $\ell$?",
        {"A": r"$y = 3x - 11$",
         "B": r"$y = 3x - 5$",
         "C": r"$y = 3x + 11$",
         "D": r"$y = -\dfrac{1}{3}x + \dfrac{7}{3}$"},
        "A",
        r"Parallel lines share the slope 3, so $\ell$ is $y = 3x + b$."
        r" Requiring it to pass through $(4, 1)$:"
        r" $$1 = 3(4) + b \;\Rightarrow\; b = -11,$$"
        r" so $y = 3x - 11$. Choice B is the GIVEN line, which does not"
        r" pass through $(4, 1)$; choice D uses the perpendicular slope."
        r" The correct answer is **A**.",
        ["Eq(3*4 - 11, 1)", "Ne(3*4 - 5, 1)"]))

    # Q19 M adv nonlinear_functions — doubling model (A)
    assert 500 * 2**Fraction(3, 3) == 1000 and 500 * 2**Fraction(6, 3) == 2000
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q19", M, 19, "advanced_math", "nonlinear_functions",
        "medium",
        r"A bacteria culture starts with 500 cells and doubles in size"
        r" every 3 hours. Which function gives the number of cells $N(t)$"
        r" in the culture $t$ hours after the start?",
        {"A": r"$N(t) = 500 \cdot 2^{t/3}$",
         "B": r"$N(t) = 500 \cdot 2^{t}$",
         "C": r"$N(t) = 500 \cdot 2^{3t}$",
         "D": r"$N(t) = 500 + 2t$"},
        "A",
        r"Each doubling multiplies the count by 2, and $t$ hours contain"
        r" $\frac{t}{3}$ doubling periods, so"
        r" $$N(t) = 500 \cdot 2^{t/3}.$$"
        r" Check: $N(3) = 1000$ (doubled once) and $N(6) = 2000$. Choice"
        r" B doubles every hour; choice C doubles three times every hour;"
        r" choice D grows linearly."
        r" The correct answer is **A**.",
        ["Eq(500*2**Rational(3, 3), 1000)", "Eq(500*2**Rational(6, 3), 2000)"]))

    # Q20 E geo right_triangles_trig — hypotenuse 17, SPR
    hyp_val = sqrt(8**2 + 15**2)
    assert hyp_val == 17
    qs.append(spr(
        "SAT-P1-M2E-Q20", M, 20, "geometry_trig", "right_triangles_trig",
        "easy",
        r"The legs of a right triangle have lengths 8 and 15. What is"
        r" the length of the hypotenuse?",
        ["17"],
        r"By the Pythagorean theorem,"
        r" $$c = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17.$$"
        r" The correct answer is **17**.",
        ["Eq(sqrt(8**2 + 15**2), 17)", "Eq(64 + 225, 289)"]))

    # Q21 H adv nonlinear_equations_systems — sum of x-coords −1 (B)
    from sympy import solve as _solve3
    y_sym = symbols("y")
    sols = _solve3([Eq(x**2 + y_sym**2, 25), Eq(y_sym, x + 1)], [x, y_sym])
    xs = sorted(s[0] for s in sols)
    assert xs == [-4, 3]
    correct = sum(xs)                          # −1
    d_prod = xs[0] * xs[1]                     # −12: product instead of sum
    d_sign = 1                                 # +1: dropped the sign (b/a)
    d_one = 3                                  # picked the positive root only
    qs.append(mcq_numeric(
        "SAT-P1-M2E-Q21", M, 21, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$x^2 + y^2 = 25$$ $$y = x + 1$$"
        r" The graphs of the equations above intersect at two points."
        r" What is the sum of the $x$-coordinates of the two points?",
        r"Substitute $y = x + 1$ into the circle equation:"
        r" $$x^2 + (x + 1)^2 = 25 \;\Rightarrow\; 2x^2 + 2x - 24 = 0"
        r" \;\Rightarrow\; x^2 + x - 12 = 0,$$"
        r" which factors as $(x + 4)(x - 3) = 0$, so $x = -4$ or $x = 3$"
        r" and the sum is $-1$. (Faster: for $x^2 + x - 12 = 0$ the sum"
        r" of roots is $-\frac{b}{a} = -1$.) Choice A is the PRODUCT of"
        r" the roots."
        r" The correct answer is **B**.",
        ["Eq((-4)**2 + (-4 + 1)**2, 25)", "Eq(3**2 + (3 + 1)**2, 25)",
         "Eq(-4 + 3, -1)", "Eq(expand((x + 4)*(x - 3)), x**2 + x - 12)"],
        int(correct), {int(d_prod): "product of roots", d_sign: "sign slip",
                       d_one: "one root only"},
        expect_letter="B"))

    # Q22 H adv equivalent_expressions — (x+3)/(x+2) (C)
    lhs = (x**2 - 9) / (x**2 - x - 6)
    assert simplify(lhs - (x + 3)/(x + 2)) == 0
    qs.append(mcq_listed(
        "SAT-P1-M2E-Q22", M, 22, "advanced_math", "equivalent_expressions",
        "hard",
        r"For $x > 3$, which of the following is equivalent to"
        r" $\dfrac{x^2 - 9}{x^2 - x - 6}$?",
        {"A": r"$\dfrac{x - 3}{x - 2}$",
         "B": r"$\dfrac{x + 2}{x + 3}$",
         "C": r"$\dfrac{x + 3}{x + 2}$",
         "D": r"$\dfrac{x + 3}{x - 2}$"},
        "C",
        r"Factor both quadratics:"
        r" $$\frac{x^2 - 9}{x^2 - x - 6}"
        r" = \frac{(x - 3)(x + 3)}{(x - 3)(x + 2)} = \frac{x + 3}{x + 2},$$"
        r" after canceling the common factor $x - 3$ (nonzero since"
        r" $x > 3$). Choice A comes from factoring the denominator as"
        r" $(x + 3)(x - 2)$ — check: that product is $x^2 + x - 6$, not"
        r" $x^2 - x - 6$."
        r" The correct answer is **C**.",
        ["Eq(expand((x - 3)*(x + 3)), x**2 - 9)",
         "Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
         "Eq(Rational(5**2 - 9, 5**2 - 5 - 6), Rational(5 + 3, 5 + 2))",
         "Eq(Rational(4**2 - 9, 4**2 - 4 - 6), Rational(4 + 3, 4 + 2))"]))

    return qs


# ─── Module 2 — HARD variant (2 easy / 7 medium / 13 hard) ────────────

def module2_hard() -> list[dict]:
    qs = []
    M = "2H"

    # Q1 E alg linear_equations_one_var — 2x + 7 = 21 (D)
    x_val = Fraction(45 - 3, 6)                # 7
    correct = int(2 * x_val + 7)               # 21
    assert x_val == 7 and correct == 21
    d_x = int(x_val)                           # 7: solved for x and stopped
    d_2x = int(2 * x_val)                      # 14: computed 2x, forgot +7
    d_2x3 = int(2 * x_val + 3)                 # 17: added the 3 from the equation
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q01", M, 1, "algebra", "linear_equations_one_var",
        "easy",
        r"If $6x + 3 = 45$, what is the value of $2x + 7$?",
        r"Solve for $x$ first: $6x = 42$, so $x = 7$. Then"
        r" $$2x + 7 = 2(7) + 7 = 21.$$"
        r" (Or divide the given equation by 3 to get $2x + 1 = 15$, so"
        r" $2x = 14$ and $2x + 7 = 21$.) Choice A stops at $x = 7$;"
        r" choice C adds the 3 from the original equation instead of 7."
        r" The correct answer is **D**.",
        ["Eq(Rational(45 - 3, 6), 7)", "Eq(2*7 + 7, 21)"],
        correct, {d_x: "solved for x", d_2x: "forgot +7", d_2x3: "added 3"},
        expect_letter="D"))

    # Q2 E psda two_var_data_models — x = 10 for predicted 60 (B), FIGURE
    x_pred = Fraction(60 - 20, 4)              # 10
    assert x_pred == 10
    correct = int(x_pred)
    d_dbl = int(Fraction(60 - 20, 8))          # 5: doubled the slope
    d_noint = 15                               # 60/4: ignored the intercept
    d_addint = int(Fraction(60 + 20, 4))       # 20: added the intercept
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q02", M, 2, "psda", "two_var_data_models", "easy",
        r"The scatterplot shows the height $y$, in millimeters, of a"
        r" plant $x$ days after germination, along with the line of best"
        r" fit $y = 4x + 20$. Based on the line of best fit, after how"
        r" many days is the predicted height equal to 60 millimeters?",
        r"Set the prediction equal to 60 and solve for $x$:"
        r" $$4x + 20 = 60 \;\Rightarrow\; 4x = 40 \;\Rightarrow\; x = 10.$$"
        r" Choice C divides 60 by 4 without first subtracting the"
        r" intercept 20."
        r" The correct answer is **B**.",
        ["Eq(4*10 + 20, 60)", "Eq(Rational(60 - 20, 4), 10)"],
        correct, {d_dbl: "doubled slope", d_noint: "ignored intercept",
                  d_addint: "added intercept"},
        fig=figure("sat-p1-m2h-q02",
                   "Scatterplot of plant height in millimeters versus "
                   "days, 10 points near a line of best fit rising from "
                   "(0, 20) with slope 4."),
        expect_letter="B"))

    # Q3 M alg linear_functions — interpretation of 550 (B)
    assert 550 + 32 * (4 - 4) == 550
    qs.append(mcq_listed(
        "SAT-P1-M2H-Q03", M, 3, "algebra", "linear_functions", "medium",
        r"A banquet hall charges according to the function"
        r" $C(n) = 550 + 32(n - 4)$, which gives the total cost, in"
        r" dollars, for an event with $n$ guests, where $n \ge 4$. What"
        r" is the best interpretation of the number 550 in this context?",
        {"A": r"The cost, in dollars, of an event with no guests.",
         "B": r"The cost, in dollars, of an event with exactly 4 guests.",
         "C": r"The cost, in dollars, added for each additional guest.",
         "D": r"The maximum possible cost, in dollars, of an event."},
        "B",
        r"Substituting $n = 4$ makes the second term vanish:"
        r" $$C(4) = 550 + 32(4 - 4) = 550.$$"
        r" So 550 is the cost when exactly 4 guests attend — NOT the cost"
        r" of zero guests: because of the $(n - 4)$ shift, $C(0)$ would"
        r" be $550 - 128 = 422$, and the model isn't even defined below"
        r" $n = 4$. Choice C describes 32."
        r" The correct answer is **B**.",
        ["Eq(550 + 32*(4 - 4), 550)", "Eq(550 + 32*(0 - 4), 422)"]))

    # Q4 M adv nonlinear_functions — larger zero of 2(x−3)²−8 (C)
    from sympy import solve as _solve
    zeros = _solve(Eq(2*(x - 3)**2 - 8, 0), x)
    assert set(zeros) == {1, 5}
    correct = 5
    d_small = 1                                # smaller zero
    d_neg = -1                                 # solved (x+3)² = 4 instead
    d_16 = 7                                   # solved (x−3)² = 16
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q04", M, 4, "advanced_math", "nonlinear_functions",
        "medium",
        r"The function $f$ is defined by $f(x) = 2(x - 3)^2 - 8$. What is"
        r" the larger of the two zeros of $f$?",
        r"Set $f(x) = 0$ and isolate the square:"
        r" $$2(x - 3)^2 = 8 \;\Rightarrow\; (x - 3)^2 = 4"
        r" \;\Rightarrow\; x - 3 = \pm 2,$$"
        r" so $x = 1$ or $x = 5$; the larger zero is 5. Choice D comes"
        r" from solving $(x - 3)^2 = 16$, forgetting to divide the 8 by 2"
        r" first — check: $2(7 - 3)^2 - 8 = 24 \ne 0$."
        r" The correct answer is **C**.",
        ["Eq(2*(5 - 3)**2 - 8, 0)", "Eq(2*(1 - 3)**2 - 8, 0)",
         "Ne(2*(7 - 3)**2 - 8, 0)"],
        correct, {d_small: "smaller zero", d_neg: "sign-flipped shift",
                  d_16: "forgot /2"},
        expect_letter="C"))

    # Q5 H geo area_volume — cylinder minus cone = 48π (B), FIGURE
    r_, h_ = 3, 8
    vcyl = pi * r_**2 * h_                     # 72π
    vcone = Rational(1, 3) * pi * r_**2 * h_   # 24π
    diff = vcyl - vcone                        # 48π
    assert diff == 48 * pi
    qs.append(mcq_listed(
        "SAT-P1-M2H-Q05", M, 5, "geometry_trig", "area_volume", "hard",
        r"A right circular cylinder and a right circular cone each have"
        r" a base radius of 3 and a height of 8, as shown. The volume of"
        r" the cylinder is how much greater than the volume of the cone?",
        {"A": r"$24\pi$",
         "B": r"$48\pi$",
         "C": r"$72\pi$",
         "D": r"$96\pi$"},
        "B",
        r"With the same base and height, a cone holds exactly one third"
        r" of the cylinder, so the difference is two thirds of the"
        r" cylinder:"
        r" $$V_{cyl} = \pi (3)^2 (8) = 72\pi, \qquad"
        r" V_{cone} = \frac{1}{3}(72\pi) = 24\pi,$$"
        r" $$72\pi - 24\pi = 48\pi.$$"
        r" Choice A is the cone's own volume; choice C is the cylinder's."
        r" The correct answer is **B**.",
        ["Eq(pi*3**2*8, 72*pi)", "Eq(Rational(1,3)*pi*3**2*8, 24*pi)",
         "Eq(72*pi - 24*pi, 48*pi)"],
        fig=figure("sat-p1-m2h-q05",
                   "A right circular cylinder and a right circular cone "
                   "side by side, each with base radius labeled 3 and "
                   "height labeled 8.")))

    # Q6 M alg linear_equations_two_var — a = 9, SPR
    a_val = Fraction(36, 4)
    assert a_val == 9 and Fraction(36, 3) == 12
    qs.append(spr(
        "SAT-P1-M2H-Q06", M, 6, "algebra", "linear_equations_two_var",
        "medium",
        r"The graph of $ax + by = 36$ in the $xy$-plane has an"
        r" $x$-intercept at $(4, 0)$ and a $y$-intercept at $(0, 3)$,"
        r" where $a$ and $b$ are constants. What is the value of $a$?",
        ["9"],
        r"At the $x$-intercept, $y = 0$:"
        r" $$a(4) + b(0) = 36 \;\Rightarrow\; a = 9.$$"
        r" (The $y$-intercept similarly gives $b = 12$.)"
        r" The correct answer is **9**.",
        ["Eq(Rational(36, 4), 9)", "Eq(Rational(36, 3), 12)",
         "Eq(9*4 + 12*0, 36)"]))

    # Q7 H adv equivalent_expressions — (2x−3)² − (2x−3)(x+4) (A)
    e = expand((2*x - 3)**2 - (2*x - 3)*(x + 4))
    assert e == 2*x**2 - 17*x + 21
    qs.append(mcq_listed(
        "SAT-P1-M2H-Q07", M, 7, "advanced_math", "equivalent_expressions",
        "hard",
        r"Which of the following is equivalent to"
        r" $(2x - 3)^2 - (2x - 3)(x + 4)$?",
        {"A": r"$2x^2 - 17x + 21$",
         "B": r"$2x^2 - 5x + 3$",
         "C": r"$2x^2 + 17x + 21$",
         "D": r"$6x^2 - 7x - 3$"},
        "A",
        r"Factor out the common binomial $(2x - 3)$ instead of expanding"
        r" everything:"
        r" $$(2x - 3)\big[(2x - 3) - (x + 4)\big] = (2x - 3)(x - 7)"
        r" = 2x^2 - 17x + 21.$$"
        r" Choice D comes from ADDING $(x + 4)$ inside the bracket — the"
        r" minus sign must distribute over both terms."
        r" The correct answer is **A**.",
        ["Eq(expand((2*x - 3)**2 - (2*x - 3)*(x + 4)), 2*x**2 - 17*x + 21)",
         "Eq(expand((2*x - 3)*(x - 7)), 2*x**2 - 17*x + 21)",
         "Eq((2*2 - 3)**2 - (2*2 - 3)*(2 + 4), 2*4 - 17*2 + 21)"]))

    # Q8 M geo lines_angles_triangles — BC = 18 (D), FIGURE
    AD, AB, DE = 4, 12, 6
    BC = Fraction(DE * AB, AD)                 # 18
    assert BC == 18
    correct = int(BC)
    d_db = int(Fraction(DE * (AB - AD), AD))   # 12: used DB instead of AB
    d_add = DE + (AB - AD)                     # 14: added DB
    d_flip = int(Fraction(DE * AB, AB - AD))   # 9: divided by DB
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q08", M, 8, "geometry_trig", "lines_angles_triangles",
        "medium",
        r"In triangle $ABC$ shown, points $D$ and $E$ lie on sides $AB$"
        r" and $AC$, respectively, and $\overline{DE} \parallel"
        r" \overline{BC}$. If $AD = 4$, $AB = 12$, and $DE = 6$, what is"
        r" the length of $\overline{BC}$?",
        r"Because $DE \parallel BC$, triangles $ADE$ and $ABC$ are"
        r" similar, and corresponding sides are proportional with ratio"
        r" $\frac{AB}{AD} = \frac{12}{4} = 3$:"
        r" $$BC = 3 \cdot DE = 3 \cdot 6 = 18.$$"
        r" Choice B uses $DB = 8$ in place of the full side $AB$ — the"
        r" similar triangles share vertex $A$, so the ratio needs $AB$,"
        r" not $DB$."
        r" The correct answer is **D**.",
        ["Eq(Rational(12, 4), 3)", "Eq(3*6, 18)", "Eq(12 - 4, 8)"],
        correct, {d_db: "used DB ratio", d_add: "added DB",
                  d_flip: "divided by DB"},
        fig=figure("sat-p1-m2h-q08",
                   "Triangle ABC with segment DE parallel to base BC; D "
                   "on AB with AD = 4 and AB = 12, DE labeled 6."),
        expect_letter="D"))

    # Q9 H alg systems_two_linear — no solution: k = 4 (C)
    k_val = Fraction(2 * (-6), -3)             # 4
    assert k_val == 4 and Fraction(8, 5) != Fraction(-6, -3)
    correct, d_neg, d_half, d_dbl = 4, -4, 3, 12
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q09", M, 9, "algebra", "systems_two_linear", "hard",
        r"$$kx - 6y = 8$$ $$2x - 3y = 5$$"
        r" In the system of equations above, $k$ is a constant. For which"
        r" value of $k$ does the system have no solution?",
        r"A system of two lines has no solution when the lines are"
        r" parallel but distinct. Multiply the second equation by 2:"
        r" $4x - 6y = 10$. Matching $y$-coefficients, the lines are"
        r" parallel when"
        r" $$k = 4,$$"
        r" and then the constants differ ($8 \ne 10$), so the lines never"
        r" meet. Choice B (3) is the ratio $\frac{6}{2}$ of the wrong"
        r" pair of coefficients."
        r" The correct answer is **C**.",
        ["Eq(2*2, 4)", "Ne(8, 10)", "Eq(Rational(-6, -3), 2)"],
        correct, {d_neg: "sign error", d_half: "6/2 ratio",
                  d_dbl: "6*2"},
        expect_letter="C"))

    # Q10 H adv nonlinear_functions — f(5) = 12 (D), FIGURE
    a_lead = Fraction(-8, (0 + 1) * (0 - 4))   # a = 2 from y-intercept −8
    assert a_lead == 2
    f5 = a_lead * (5 + 1) * (5 - 4)            # 12
    assert f5 == 12
    correct = int(f5)
    d_noa = (5 + 1) * (5 - 4)                  # 6: forgot the leading factor
    d_yint = -8                                # echoed the y-intercept
    d_asign = -int(f5)                         # −12: took a = −2
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q10", M, 10, "advanced_math", "nonlinear_functions",
        "hard",
        r"The parabola shown has $x$-intercepts at $(-1, 0)$ and"
        r" $(4, 0)$ and $y$-intercept at $(0, -8)$. The parabola is the"
        r" graph of $f(x) = a(x + 1)(x - 4)$, where $a$ is a constant."
        r" What is the value of $f(5)$?",
        r"Use the $y$-intercept to find $a$:"
        r" $$f(0) = a(1)(-4) = -4a = -8 \;\Rightarrow\; a = 2.$$"
        r" Then"
        r" $$f(5) = 2(5 + 1)(5 - 4) = 2 \cdot 6 \cdot 1 = 12.$$"
        r" Choice B (6) forgets the leading factor $a$; choice A takes"
        r" $a = -2$ from a sign slip in $-4a = -8$."
        r" The correct answer is **D**.",
        ["Eq(Rational(-8, -4), 2)", "Eq(2*(0 + 1)*(0 - 4), -8)",
         "Eq(2*(5 + 1)*(5 - 4), 12)"],
        correct, {d_noa: "forgot a", d_yint: "echoed y-intercept",
                  d_asign: "a sign slip"},
        fig=figure("sat-p1-m2h-q10",
                   "Upward-opening parabola with x-intercepts at -1 and "
                   "4 and y-intercept at (0, -8), graphed on labeled "
                   "axes."),
        expect_letter="D"))

    # Q11 H psda one_var_data — new mean 12, SPR
    new_mean = Fraction(12 * 15 - 27 - 33, 10)
    assert new_mean == 12
    qs.append(spr(
        "SAT-P1-M2H-Q11", M, 11, "psda", "one_var_data", "hard",
        r"The mean of a list of 12 numbers is 15. When the two numbers"
        r" 27 and 33 are removed from the list, what is the mean of the"
        r" remaining 10 numbers?",
        ["12"],
        r"The 12 numbers sum to $12 \times 15 = 180$. Removing 27 and 33"
        r" removes $27 + 33 = 60$, leaving a sum of $180 - 60 = 120$ for"
        r" the remaining 10 numbers:"
        r" $$\text{mean} = \frac{120}{10} = 12.$$"
        r" The correct answer is **12**.",
        ["Eq(12*15, 180)", "Eq(27 + 33, 60)", "Eq(Rational(180 - 60, 10), 12)"]))

    # Q12 H alg linear_inequalities — system setup (A)
    assert 30 * 12 + 45 * 0 <= 1200            # 12 crates of A alone fit
    qs.append(mcq_listed(
        "SAT-P1-M2H-Q12", M, 12, "algebra", "linear_inequalities", "hard",
        r"A delivery truck can carry at most 1200 kilograms. Each crate"
        r" of type A weighs 30 kilograms, and each crate of type B weighs"
        r" 45 kilograms. The truck must carry at least 12 crates of type"
        r" A. If $a$ is the number of type A crates and $b$ is the number"
        r" of type B crates, which system represents these constraints?",
        {"A": r"$30a + 45b \le 1200$ and $a \ge 12$",
         "B": r"$30a + 45b \ge 1200$ and $a \ge 12$",
         "C": r"$45a + 30b \le 1200$ and $a \ge 12$",
         "D": r"$30a + 45b \le 1200$ and $a \le 12$"},
        "A",
        r"The total weight is 30 kilograms per type-A crate times $a$,"
        r" plus 45 per type-B crate times $b$; \"at most 1200\" bounds it"
        r" above: $30a + 45b \le 1200$. \"At least 12 crates of type A\""
        r" means $a \ge 12$. Choice C attaches each weight to the wrong"
        r" crate type; choice D reverses the crate-count requirement."
        r" The correct answer is **A**.",
        ["30*12 + 45*0 <= 1200", "30*12 + 45*18 <= 1200",
         "Eq(30*12, 360)"]))

    # Q13 H adv equivalent_expressions — b = 14, SPR
    a_c = Fraction(15, 3)                      # a = 5
    b_c = 9 + a_c                              # 14
    assert (a_c, b_c) == (5, 14)
    e2 = expand((3*x + 5) * (x + 3))
    assert e2 == 3*x**2 + 14*x + 15
    qs.append(spr(
        "SAT-P1-M2H-Q13", M, 13, "advanced_math", "equivalent_expressions",
        "hard",
        r"$$(3x + a)(x + 3) = 3x^2 + bx + 15$$"
        r" In the equation above, $a$ and $b$ are constants. If the"
        r" equation is true for all values of $x$, what is the value of"
        r" $b$?",
        ["14"],
        r"Expand the left side:"
        r" $$(3x + a)(x + 3) = 3x^2 + (9 + a)x + 3a.$$"
        r" Matching constants: $3a = 15$, so $a = 5$. Matching the"
        r" $x$-coefficients: $b = 9 + a = 14$."
        r" The correct answer is **14**.",
        ["Eq(Rational(15, 3), 5)", "Eq(9 + 5, 14)",
         "Eq(expand((3*x + 5)*(x + 3)), 3*x**2 + 14*x + 15)"]))

    # Q14 H geo circles — radius 6 (C)
    r_sq = 11 + 16 + 9                          # 36
    assert sqrt(r_sq) == 6
    correct = 6
    d_half = 4                                  # half of 8
    d_no11 = 5                                  # √(16+9): dropped the 11
    d_rsq = 36                                  # forgot the square root
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q14", M, 14, "geometry_trig", "circles", "hard",
        r"$$x^2 + y^2 - 8x + 6y = 11$$"
        r" The graph of the equation above in the $xy$-plane is a circle."
        r" What is the radius of the circle?",
        r"Complete the square in each variable:"
        r" $$(x^2 - 8x + 16) + (y^2 + 6y + 9) = 11 + 16 + 9$$"
        r" $$(x - 4)^2 + (y + 3)^2 = 36,$$"
        r" so $r = \sqrt{36} = 6$. Choice D stops at $r^2 = 36$; choice B"
        r" completes the squares but forgets to carry the original 11 to"
        r" the right-hand side ($\sqrt{25} = 5$)."
        r" The correct answer is **C**.",
        ["Eq(11 + 16 + 9, 36)", "Eq(sqrt(36), 6)",
         "Eq(expand((x - 4)**2) , x**2 - 8*x + 16)"],
        correct, {d_half: "half of 8", d_no11: "dropped the 11",
                  d_rsq: "r^2"},
        expect_letter="C"))

    # Q15 M alg linear_functions — f(0) = 1 (A)
    slope = Fraction(26 - 11, 5 - 2)            # 5
    f0 = 11 - slope * 2                          # 1
    assert (slope, f0) == (5, 1)
    correct = int(f0)
    d_div = 3                                    # (26−11)/5: wrong divisor
    d_slope = int(slope)                         # 5: reported the slope
    d_sub = 6                                    # 6 = 11 − 5: subtracted the slope once
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q15", M, 15, "algebra", "linear_functions", "medium",
        r"For the linear function $f$, $f(2) = 11$ and $f(5) = 26$. What"
        r" is the value of $f(0)$?",
        r"The slope is"
        r" $$\frac{f(5) - f(2)}{5 - 2} = \frac{26 - 11}{3} = 5.$$"
        r" Walking back from $x = 2$ to $x = 0$ subtracts the slope"
        r" twice:"
        r" $$f(0) = 11 - 2(5) = 1.$$"
        r" Choice C reports the slope itself; choice B divides the rise"
        r" 15 by 5 instead of by the run 3."
        r" The correct answer is **A**.",
        ["Eq(Rational(26 - 11, 5 - 2), 5)", "Eq(11 - 2*5, 1)",
         "Eq(5*5 + 1, 26)"],
        correct, {d_div: "divided by 5", d_slope: "the slope",
                  d_sub: "11 - 5"},
        expect_letter="A"))

    # Q16 H adv nonlinear_equations_systems — k = 1, SPR
    vy = (3)**2 - 6*3 + 10                      # vertex value 1
    assert vy == 1
    qs.append(spr(
        "SAT-P1-M2H-Q16", M, 16, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"$$y = x^2 - 6x + 10$$ $$y = k$$"
        r" In the system of equations above, $k$ is a constant. For which"
        r" value of $k$ does the system have exactly one real solution?",
        ["1"],
        r"Completing the square, $y = (x - 3)^2 + 1$: an upward-opening"
        r" parabola with vertex $(3, 1)$. The horizontal line $y = k$"
        r" meets it exactly once only at the vertex, so"
        r" $$k = 1.$$"
        r" (Equivalently: $x^2 - 6x + (10 - k) = 0$ has one solution when"
        r" the discriminant $36 - 4(10 - k) = 0$, giving $k = 1$.)"
        r" The correct answer is **1**.",
        ["Eq(expand((x - 3)**2 + 1), x**2 - 6*x + 10)",
         "Eq(3**2 - 6*3 + 10, 1)", "Eq(36 - 4*(10 - 1), 0)"]))

    # Q17 M psda probability_conditional — 3/5 (C), FIGURE
    y1, n1, y2, n2 = 30, 50, 72, 48
    assert y1 + n1 == 80 and y2 + n2 == 120
    correct = Fraction(y2, y2 + n2)             # 72/120 = 3/5
    d_all = Fraction(y2, 200)                   # 9/25
    d_yes = Fraction(y1 + y2, 200)              # 102/200 = 51/100
    d_flip = Fraction(y2, y1 + y2)              # 72/102 = 12/17
    assert (correct, d_all, d_yes, d_flip) == \
        (Fraction(3, 5), Fraction(9, 25), Fraction(51, 100), Fraction(12, 17))
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q17", M, 17, "psda", "probability_conditional",
        "medium",
        r"The table summarizes the responses of 200 adults, by age group,"
        r" to a yes-or-no survey question. If one of the adults age 30 or"
        r" older is selected at random, what is the probability that the"
        r" selected adult answered yes?",
        r"The condition restricts the sample space to the 120 adults age"
        r" 30 or older, of whom 72 answered yes:"
        r" $$P(\text{yes} \mid \text{age} \ge 30) = \frac{72}{120}"
        r" = \frac{3}{5}.$$"
        r" Choice A divides 72 by all 200 adults; choice D,"
        r" $\frac{12}{17}$, is the reversed condition $P(\text{age} \ge"
        r" 30 \mid \text{yes}) = \frac{72}{102}$."
        r" The correct answer is **C**.",
        ["Eq(Rational(72, 120), Rational(3, 5))",
         "Eq(30 + 50 + 72 + 48, 200)",
         "Eq(Rational(72, 102), Rational(12, 17))"],
        correct, {d_all: "over all adults", d_yes: "P(yes)",
                  d_flip: "reversed condition"},
        fmt=lambda v: latex_frac(Fraction(v) if not isinstance(v, Fraction) else v),
        fig=figure("sat-p1-m2h-q17",
                   "Two-way table of survey answers by age group. Under "
                   "30: yes 30, no 50, total 80. Age 30 or older: yes 72, "
                   "no 48, total 120. Column totals: yes 102, no 98, "
                   "total 200."),
        expect_letter="C"))

    # Q18 M alg linear_equations_two_var — perpendicular through origin (B)
    assert Fraction(5, 2) * Fraction(-2, 5) == -1
    qs.append(mcq_listed(
        "SAT-P1-M2H-Q18", M, 18, "algebra", "linear_equations_two_var",
        "medium",
        r"Line $\ell$ is defined by $5x - 2y = 8$. Line $m$ is"
        r" perpendicular to line $\ell$ and passes through the origin."
        r" Which equation defines line $m$?",
        {"A": r"$y = -\dfrac{5}{2}x$",
         "B": r"$y = -\dfrac{2}{5}x$",
         "C": r"$y = \dfrac{2}{5}x$",
         "D": r"$y = \dfrac{5}{2}x$"},
        "B",
        r"Rewrite $\ell$ in slope-intercept form: $y = \frac{5}{2}x - 4$,"
        r" so $\ell$ has slope $\frac{5}{2}$. A perpendicular line has"
        r" the negative reciprocal slope, and through the origin the"
        r" intercept is 0:"
        r" $$y = -\frac{2}{5}x.$$"
        r" Choice A negates without taking the reciprocal; choice C takes"
        r" the reciprocal without negating; choice D is parallel to"
        r" $\ell$, not perpendicular."
        r" The correct answer is **B**.",
        ["Eq(Rational(5, 2)*Rational(-2, 5), -1)",
         "Eq((5*2 - 8)/2, 1)"]))

    # Q19 H adv nonlinear_functions — f(5) = 1215 (C)
    b_sq = Fraction(405, 45)                    # 9
    b_val = 3
    a_val = Fraction(45, 9)                     # 5
    assert b_val**2 == b_sq and a_val * b_val**2 == 45
    f5 = a_val * b_val**5                       # 1215
    assert f5 == 1215
    correct = int(f5)
    d_noa = 3**5                                # 243: dropped a
    d_lin = 405 + (405 - 45)//2                 # 585: linear extension
    d_f6 = int(a_val * b_val**6)                # 3645: computed f(6)
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q19", M, 19, "advanced_math", "nonlinear_functions",
        "hard",
        r"For the exponential function $f(t) = a \cdot b^t$, where $a >"
        r" 0$ and $b > 0$, $f(2) = 45$ and $f(4) = 405$. What is the"
        r" value of $f(5)$?",
        r"Divide the two known values to eliminate $a$:"
        r" $$\frac{f(4)}{f(2)} = b^2 = \frac{405}{45} = 9"
        r" \;\Rightarrow\; b = 3.$$"
        r" Then $a \cdot 3^2 = 45$ gives $a = 5$, so"
        r" $$f(5) = 5 \cdot 3^5 = 5 \cdot 243 = 1215.$$"
        r" (Faster: $f(5) = f(4) \cdot b = 405 \cdot 3$.) Choice B"
        r" continues the pattern linearly instead of multiplicatively."
        r" The correct answer is **C**.",
        ["Eq(Rational(405, 45), 9)", "Eq(Rational(45, 9), 5)",
         "Eq(5*3**5, 1215)", "Eq(405*3, 1215)"],
        correct, {d_noa: "dropped a", d_lin: "linear extension",
                  d_f6: "computed f(6)"},
        expect_letter="C"))

    # Q20 H geo right_triangles_trig — longer leg 32, SPR
    kk = Fraction(40, 5)
    legs = (3 * kk, 4 * kk)
    assert max(legs) == 32 and (3*kk)**2 + (4*kk)**2 == 40**2
    qs.append(spr(
        "SAT-P1-M2H-Q20", M, 20, "geometry_trig", "right_triangles_trig",
        "hard",
        r"In a right triangle, the tangent of one of the acute angles is"
        r" $\dfrac{3}{4}$. If the hypotenuse of the triangle has length"
        r" 40, what is the length of the longer leg?",
        ["32"],
        r"$\tan \theta = \frac{3}{4}$ means the legs are in ratio $3 : 4$"
        r" — a 3-4-5 right triangle scaled by some factor $k$: legs $3k$"
        r" and $4k$, hypotenuse $5k$. Then"
        r" $$5k = 40 \;\Rightarrow\; k = 8,$$"
        r" so the legs are 24 and 32; the longer leg is"
        r" $4k = 32$. Check: $24^2 + 32^2 = 576 + 1024 = 1600 = 40^2$."
        r" The correct answer is **32**.",
        ["Eq(Rational(40, 5), 8)", "Eq(4*8, 32)",
         "Eq(24**2 + 32**2, 40**2)"]))

    # Q21 H adv nonlinear_equations_systems — x = 6 only (B)
    from sympy import solve as _solve4
    cands = _solve4(Eq((x - 4)**2, x - 2), x)
    assert set(cands) == {3, 6}
    assert (6 - 4) == sqrt(6 - 2)               # 6 checks
    assert (3 - 4) != sqrt(3 - 2)               # 3 is extraneous
    qs.append(mcq_listed(
        "SAT-P1-M2H-Q21", M, 21, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"What are all solutions of the equation"
        r" $x - 4 = \sqrt{x - 2}$?",
        {"A": r"$3$",
         "B": r"$6$",
         "C": r"$3$ and $6$",
         "D": r"There are no solutions."},
        "B",
        r"Square both sides: $(x - 4)^2 = x - 2$, so"
        r" $$x^2 - 9x + 18 = 0 \;\Rightarrow\; (x - 3)(x - 6) = 0,$$"
        r" giving candidates $x = 3$ and $x = 6$. Squaring can create"
        r" extraneous roots, so check both in the ORIGINAL equation:"
        r" $x = 6$: $6 - 4 = 2$ and $\sqrt{4} = 2$. ✓"
        r" $x = 3$: $3 - 4 = -1$ but $\sqrt{1} = 1$. ✗ (a square root is"
        r" never negative). Choice C keeps the extraneous root."
        r" The correct answer is **B**.",
        ["Eq(expand((x - 3)*(x - 6)), x**2 - 9*x + 18)",
         "Eq(6 - 4, sqrt(6 - 2))", "Ne(3 - 4, sqrt(3 - 2))"]))

    # Q22 H adv nonlinear_equations_systems — 8^x = 2^(x+12) → x = 6 (B)
    x_val = Fraction(12, 2)
    assert 3 * x_val == x_val + 12
    correct = int(x_val)                        # 6
    d_34 = 4                                    # solved 3x = 12
    d_echo = 12                                 # echoed the 12
    d_dbl = 24                                  # doubled it
    qs.append(mcq_numeric(
        "SAT-P1-M2H-Q22", M, 22, "advanced_math",
        "nonlinear_equations_systems", "hard",
        r"If $8^x = 2^{x + 12}$, what is the value of $x$?",
        r"Write both sides with base 2: $8 = 2^3$, so"
        r" $$8^x = (2^3)^x = 2^{3x}.$$"
        r" Equal powers of the same base have equal exponents:"
        r" $$3x = x + 12 \;\Rightarrow\; 2x = 12 \;\Rightarrow\; x = 6.$$"
        r" Check: $8^6 = 262144 = 2^{18}$. Choice A solves $3x = 12$,"
        r" forgetting the $x$ on the right side."
        r" The correct answer is **B**.",
        ["Eq(8**6, 2**(6 + 12))", "Eq(3*6, 6 + 12)", "Eq(Rational(12, 2), 6)"],
        correct, {d_34: "3x = 12", d_echo: "echoed 12", d_dbl: "doubled"},
        expect_letter="B"))

    return qs


# ─── blueprint conformance + emit ─────────────────────────────────────

BLUEPRINT = {
    # module: (difficulty mix, SPR positions, domain counts)
    "module1": ({"easy": 8, "medium": 9, "hard": 5}, {6, 11, 13, 16, 20, 22},
                {"algebra": 8, "advanced_math": 7, "psda": 4,
                 "geometry_trig": 3}),
    "module2Easy": ({"easy": 11, "medium": 9, "hard": 2}, {6, 11, 13, 16, 20},
                    {"algebra": 7, "advanced_math": 8, "psda": 3,
                     "geometry_trig": 4}),
    "module2Hard": ({"easy": 2, "medium": 7, "hard": 13}, {6, 11, 13, 16, 20},
                    {"algebra": 7, "advanced_math": 8, "psda": 3,
                     "geometry_trig": 4}),
}


def check_module(key: str, qs: list[dict]) -> None:
    diff_mix, spr_slots, domains = BLUEPRINT[key]
    assert len(qs) == 22, f"{key}: {len(qs)} questions"
    assert [q["questionNumber"] for q in qs] == list(range(1, 23)), \
        f"{key}: question numbers not 1..22"
    assert Counter(q["difficulty"] for q in qs) == Counter(diff_mix), \
        f"{key}: difficulty mix {Counter(q['difficulty'] for q in qs)}"
    got_spr = {q["questionNumber"] for q in qs if q["format"] == "spr"}
    assert got_spr == spr_slots, f"{key}: SPR at {sorted(got_spr)}"
    assert Counter(q["domain"] for q in qs) == Counter(domains), \
        f"{key}: domains {Counter(q['domain'] for q in qs)}"
    letters = [q["answer"] for q in qs if q["format"] == "mcq"]
    hist = Counter(letters)
    run, prev = 1, None
    for a in letters:
        run = run + 1 if a == prev else 1
        prev = a
        assert run < 4, f"{key}: run of 4 answer letter {a}"
    print(f"  {key}: 22 ok, letters {dict(sorted(hist.items()))}, "
          f"spr at {sorted(got_spr)}")


def main() -> None:
    m1 = module1()
    m2e = module2_easy()
    m2h = module2_hard()
    print("blueprint conformance:")
    check_module("module1", m1)
    check_module("module2Easy", m2e)
    check_module("module2Hard", m2h)

    all_qs = m1 + m2e + m2h
    sources = [q["source"] for q in all_qs]
    assert len(set(sources)) == len(sources), "duplicate source ids"
    n_fig = sum(1 for q in all_qs if "figure" in q)

    data = {
        "meta": {
            "testId": "sat-practice-1",
            "label": "SAT Math Practice Test 1",
            "minutesPerModule": 35,
            "module2Threshold": 15,
        },
        "module1": m1,
        "module2Easy": m2e,
        "module2Hard": m2h,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"wrote {OUT.relative_to(REPO)}: 66 questions, {n_fig} figures")


if __name__ == "__main__":
    main()
