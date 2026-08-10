#!/usr/bin/env python3
"""SAT Math — Geometry and Trigonometry, Units 3-4.

Builds:
  data/genmath/sat/right-triangles-and-trigonometry.json
  data/genmath/sat/circles.json

Run: python3 scripts/sat/build_geo_3_4.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
RT_TAG = {"text": "sat-right-triangle-trig", "mono": True}
CIR_TAG = {"text": "sat-circles", "mono": True}


def _b(tag, level):
    return [tag, {"text": level}]


# ===========================================================================
# UNIT 3 — Right triangles and trigonometry
# ===========================================================================

def lesson_pythagoras():
    worked = [
        problem(
            "sat-rt1-w1",
            "A right triangle has legs of length $9$ and $12$. What is the length of its "
            "hypotenuse?",
            "**Answer.** $15$.  \n"
            "Pythagoras relates the two legs to the hypotenuse:\n"
            "$$a^{2} + b^{2} = c^{2}$$\n"
            "$$9^{2} + 12^{2} = 81 + 144 = 225$$\n"
            "$$c = \\sqrt{225} = 15$$\n"
            "This is the $3$-$4$-$5$ triangle scaled by $3$, which is worth spotting: "
            "$9 = 3 \\times 3$, $12 = 3 \\times 4$, so the hypotenuse is $3 \\times 5 = 15$ "
            "with no squaring at all.  \n"
            "The letter $c$ is always the HYPOTENUSE — the side opposite the right angle, and "
            "the longest one. Putting a leg there is the single commonest Pythagoras error, "
            "and it produces an answer smaller than one of the given sides, which is a useful "
            "self-check: the hypotenuse must exceed both legs.",
            [
                "Eq(9**2 + 12**2, 225)",
                "Eq(sqrt(225), 15)",
                "Eq(3*3, 9)",
                "Eq(3*5, 15)",
                "15 > 12",
            ],
        ),
        problem(
            "sat-rt1-w2",
            "A right triangle has a hypotenuse of $26$ and one leg of $10$. What is the other "
            "leg?",
            "**Answer.** $24$.  \n"
            "The hypotenuse is given, so it goes in the $c$ position and the unknown leg is "
            "found by SUBTRACTING:\n"
            "$$10^{2} + b^{2} = 26^{2}$$\n"
            "$$100 + b^{2} = 676$$\n"
            "$$b^{2} = 576$$\n"
            "$$b = 24$$\n"
            "Check: $10^{2} + 24^{2} = 100 + 576 = 676 = 26^{2}$.  \n"
            "This is the $5$-$12$-$13$ triangle doubled. Knowing $3$-$4$-$5$, $5$-$12$-$13$ "
            "and $8$-$15$-$17$ and their multiples turns most SAT right-triangle questions "
            "into recognition rather than arithmetic.  \n"
            "Adding instead of subtracting gives $\\sqrt{776} \\approx 27.9$, which is longer "
            "than the hypotenuse — impossible, and again a self-check that catches the error.",
            [
                "Eq(26**2 - 10**2, 576)",
                "Eq(sqrt(576), 24)",
                "Eq(10**2 + 24**2, 26**2)",
                "Eq(2*13, 26)",
                "Eq(2*12, 24)",
            ],
        ),
        problem(
            "sat-rt1-w3",
            "In a $30$-$60$-$90$ triangle the shorter leg has length $7$. What are the other "
            "two sides?",
            "**Answer.** The longer leg is $7\\sqrt{3}$ and the hypotenuse is $14$.  \n"
            "The $30$-$60$-$90$ triangle always has sides in the ratio\n"
            "$$1 : \\sqrt{3} : 2$$\n"
            "with the shortest side opposite the $30^\\circ$ angle, the middle side opposite "
            "the $60^\\circ$, and the hypotenuse opposite the right angle. Multiplying the "
            "ratio through by $7$:\n"
            "$$7 : 7\\sqrt{3} : 14$$\n"
            "Check with Pythagoras: $7^{2} + (7\\sqrt{3})^{2} = 49 + 147 = 196 = 14^{2}$.  \n"
            "The ordering is what gets misremembered. The side opposite the SMALLEST angle is "
            "the shortest, so the $\\sqrt{3}$ side sits opposite $60^\\circ$, not opposite "
            "$30^\\circ$. Swapping them gives $\\frac{7}{\\sqrt{3}}$ and $\\frac{14}{\\sqrt{3}}$, "
            "both listed.  \n"
            "Both special triangles are printed on the SAT's reference sheet, so this is "
            "recognition rather than recall — but only if you read which angle faces which "
            "side.",
            [
                "Eq(7**2 + (7*sqrt(3))**2, 196)",
                "Eq(14**2, 196)",
                "Eq(simplify((7*sqrt(3))**2), 147)",
                "7*sqrt(3) > 7",
                "14 > 7*sqrt(3)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-rt1-t1",
            "A right triangle has legs $5$ and $12$. What is the hypotenuse?",
            "**Answer.** $13$. $25 + 144 = 169$, and $\\sqrt{169} = 13$ — the $5$-$12$-$13$ "
            "triangle.",
            ["Eq(5**2 + 12**2, 169)", "Eq(sqrt(169), 13)"],
        ),
        problem(
            "sat-rt1-t2",
            "A right triangle has hypotenuse $17$ and one leg $8$. What is the other leg?",
            "**Answer.** $15$. $289 - 64 = 225$, and $\\sqrt{225} = 15$ — the $8$-$15$-$17$ "
            "triangle.",
            ["Eq(17**2 - 8**2, 225)", "Eq(sqrt(225), 15)", "Eq(8**2 + 15**2, 17**2)"],
        ),
        problem(
            "sat-rt1-t3",
            "In a $45$-$45$-$90$ triangle each leg has length $6$. What is the hypotenuse?",
            "**Answer.** $6\\sqrt{2}$. The ratio is $1 : 1 : \\sqrt{2}$, so the hypotenuse is "
            "the leg times $\\sqrt{2}$. Check: $36 + 36 = 72 = (6\\sqrt{2})^{2}$.",
            ["Eq(6**2 + 6**2, 72)", "Eq(simplify((6*sqrt(2))**2), 72)"],
        ),
        problem(
            "sat-rt1-t4",
            "In a $30$-$60$-$90$ triangle the hypotenuse is $18$. What is the shorter leg?",
            "**Answer.** $9$. The hypotenuse is twice the shorter leg in this triangle, so the "
            "shorter leg is $\\frac{18}{2} = 9$, and the longer leg is $9\\sqrt{3}$.",
            [
                "Eq(Rational(18,2), 9)",
                "Eq(9**2 + (9*sqrt(3))**2, 18**2)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Right triangles and trigonometry",
            "beats": [
                "Domain: Geometry and Trigonometry — 5 to 7 of the 44 questions.",
                "Usually 1 or 2, and the special triangles are on the reference sheet.",
                "Prerequisites: squaring and square roots; similarity from Unit 2.",
                "Recognising a 3-4-5 or 5-12-13 turns arithmetic into recall.",
            ],
        },
        {
            "kind": "pythagoreanSquares",
            "title": "Why the squares add",
            "teach": "Squares built on the two legs, and a square built on the hypotenuse. "
                     "Drag the legs: the two smaller areas always total the larger one exactly. "
                     "That equality IS Pythagoras.",
            "config": {"a": 9, "b": 12},
        },
        {"kind": "worked", "title": "Finding a hypotenuse", "problemId": "sat-rt1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Add or subtract?",
            "prompt": "A right triangle has hypotenuse $25$ and one leg $7$. What is the other "
                      "leg?",
            "options": ["$24$", "$\\sqrt{674}$", "$32$", "$18$"],
            "correctIndex": 0,
            "explanation": "The hypotenuse is given, so subtract: $625 - 49 = 576$ and "
                           "$\\sqrt{576} = 24$. Option B adds the squares, which would make a "
                           "leg longer than the hypotenuse — impossible. Option D subtracts "
                           "the lengths themselves rather than their squares.",
            "check": [
                "Eq(25**2 - 7**2, 576)",
                "Eq(sqrt(576), 24)",
                "Eq(7**2 + 24**2, 25**2)",
                "sqrt(674) > 25",
            ],
        },
        {
            "kind": "teach",
            "title": "The triples worth recognising",
            "beats": [
                "3-4-5 and its multiples: 6-8-10, 9-12-15, 30-40-50.",
                "5-12-13 and its multiples: 10-24-26, 15-36-39.",
                "8-15-17 and 7-24-25 turn up too.",
                "Spotting one skips the squaring entirely.",
            ],
        },
        {"kind": "worked", "title": "Finding a missing leg", "problemId": "sat-rt1-w2"},
        {
            "kind": "specialTriangle",
            "title": "The two special triangles",
            "teach": "Slide the base length and watch every side scale together. The ratios "
                     "never change — that is what makes these two triangles worth knowing, and "
                     "why they sit on the reference sheet.",
            "config": {"type": "30-60-90", "start": 7},
        },
        {"kind": "worked", "title": "A 30-60-90 triangle", "problemId": "sat-rt1-w3"},
        {
            "kind": "tip",
            "title": "The hypotenuse is always the longest side",
            "body": "Before writing an answer down, check it against that fact. If your "
                    "hypotenuse came out shorter than a leg, or your missing leg came out "
                    "longer than the hypotenuse, you added where you should have subtracted. "
                    "It is a two-second check that catches the commonest error on this skill.",
        },
        {"kind": "tryIt", "title": "Your turn: a familiar triple", "problemId": "sat-rt1-t1"},
        {"kind": "tryIt", "title": "Your turn: subtract this time", "problemId": "sat-rt1-t2"},
        {"kind": "tryIt", "title": "Your turn: 45-45-90", "problemId": "sat-rt1-t3"},
        {"kind": "tryIt", "title": "Your turn: work backwards", "problemId": "sat-rt1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "The hypotenuse goes in the c position and is always the longest side.",
                "Given two legs, add the squares; given the hypotenuse, subtract.",
                "Recognise 3-4-5, 5-12-13, 8-15-17 and their multiples.",
                "45-45-90 has sides in the ratio 1 : 1 : root 2.",
                "30-60-90 has sides 1 : root 3 : 2, with root 3 opposite the 60-degree angle.",
            ],
        },
    ]

    return lesson(
        slug="pythagoras-and-special-triangles",
        title="Pythagoras and the Two Special Triangles",
        concrete=(
            "A ladder against a wall, a diagonal across a screen, the straight-line distance "
            "between two street corners: all the same question. Two sides at right angles are "
            "given and the third is wanted, and one relationship answers every version of it."
        ),
        objective=(
            "Use Pythagoras to find any side of a right triangle, recognise the common "
            "Pythagorean triples, and apply the $45$-$45$-$90$ and $30$-$60$-$90$ side ratios."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Right triangles and trigonometry*, "
            "in the **Geometry and Trigonometry** domain. It is one or two questions, and both "
            "special triangles are printed on the reference sheet — so this is recognition "
            "more than recall.",
            "Pythagoras says $a^{2} + b^{2} = c^{2}$, where $c$ is always the HYPOTENUSE: the "
            "side opposite the right angle, and the longest of the three. Given two legs you "
            "add the squares; given the hypotenuse and one leg you SUBTRACT. Putting a leg in "
            "the $c$ position is the commonest error, and it always produces an impossible "
            "triangle.",
            "Certain side lengths recur so often they are worth knowing on sight: $3$-$4$-$5$, "
            "$5$-$12$-$13$, $8$-$15$-$17$, $7$-$24$-$25$, and every multiple of each. "
            "Spotting that $9$, $12$ is $3$-$4$-$5$ tripled gives the hypotenuse $15$ with no "
            "squaring at all.",
            "**The test's angle.** The two special triangles. A $45$-$45$-$90$ has sides in "
            "the ratio $1 : 1 : \\sqrt{2}$; a $30$-$60$-$90$ has $1 : \\sqrt{3} : 2$. What "
            "gets misremembered is which side faces which angle: the side opposite the "
            "SMALLEST angle is the shortest, so in a $30$-$60$-$90$ the $\\sqrt{3}$ side sits "
            "opposite the $60^\\circ$ angle and the hypotenuse is exactly twice the shortest "
            "side.",
        ],
        key_idea=(
            "The hypotenuse is the longest side and sits alone on one side of the equation. "
            "Add the squares to find it, subtract to find a leg — and check the answer against "
            "'the hypotenuse is longest'."
        ),
        facts=[
            fact(
                "Pythagoras",
                "a^{2} + b^{2} = c^{2}",
                "$c$ is the hypotenuse, opposite the right angle and longest.",
            ),
            fact(
                "45-45-90",
                "x : x : x\\sqrt{2}",
                "An isosceles right triangle. The hypotenuse is a leg times $\\sqrt{2}$.",
            ),
            fact(
                "30-60-90",
                "x : x\\sqrt{3} : 2x",
                "The shortest side faces $30^\\circ$, the $\\sqrt{3}$ side faces $60^\\circ$, "
                "and the hypotenuse is twice the shortest.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Adding the squares when the hypotenuse was given.",
                "That produces a leg longer than the hypotenuse. Subtract instead.",
            ),
            mistake(
                "Subtracting the side lengths rather than their squares.",
                "$25 - 7 = 18$ is not a side of this triangle. Square first, subtract, then "
                "take the root.",
            ),
            mistake(
                "Putting the $\\sqrt{3}$ opposite the $30^\\circ$ angle.",
                "The shortest side faces the smallest angle. The $\\sqrt{3}$ side faces "
                "$60^\\circ$.",
            ),
            mistake(
                "Forgetting to take the square root at the end.",
                "$b^{2} = 576$ means $b = 24$. Reporting $576$ is a listed option.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_trig():
    worked = [
        problem(
            "sat-rt2-w1",
            "In right triangle $ABC$, the right angle is at $C$, $AB = 13$ and $BC = 5$. What "
            "is the value of $\\sin A$?",
            "**Answer.** $\\dfrac{5}{13}$.  \n"
            "SOH-CAH-TOA names the three ratios, and every one of them is measured FROM a "
            "particular angle:\n"
            "$$\\sin = \\frac{\\text{opposite}}{\\text{hypotenuse}}, \\quad \\cos = \\frac{\\text{adjacent}}{\\text{hypotenuse}}, \\quad \\tan = \\frac{\\text{opposite}}{\\text{adjacent}}$$\n"
            "The right angle is at $C$, so $AB$ is the hypotenuse: $13$. Working from angle "
            "$A$, the opposite side is the one not touching $A$, which is $BC = 5$.\n"
            "$$\\sin A = \\frac{5}{13}$$\n"
            "The third side is $AC = 12$, from the $5$-$12$-$13$ triple, so "
            "$\\cos A = \\frac{12}{13}$ and $\\tan A = \\frac{5}{12}$.  \n"
            "Everything depends on which angle you are standing at. From angle $B$ the same "
            "triangle gives $\\sin B = \\frac{12}{13}$ — the sides have not moved, but "
            "'opposite' now means something different.",
            [
                "Eq(13**2 - 5**2, 144)",
                "Eq(sqrt(144), 12)",
                "Eq(Rational(5,13), Rational(5,13))",
                "Eq(Rational(12,13) + 0, Rational(12,13))",
            ],
        ),
        problem(
            "sat-rt2-w2",
            "In a right triangle, $\\sin x^\\circ = \\dfrac{3}{5}$. What is $\\cos(90 - x)^\\circ$?",
            "**Answer.** $\\dfrac{3}{5}$.  \n"
            "The two non-right angles of a right triangle add to $90^\\circ$, so they are "
            "COMPLEMENTARY. And swapping between them swaps 'opposite' and 'adjacent' — which "
            "is exactly the difference between sine and cosine:\n"
            "$$\\sin \\theta = \\cos(90^\\circ - \\theta)$$\n"
            "So $\\cos(90 - x)^\\circ = \\sin x^\\circ = \\frac{3}{5}$.  \n"
            "Concretely: in a $3$-$4$-$5$ triangle with $\\sin x = \\frac{3}{5}$, the other "
            "acute angle is $90 - x$, and the side opposite $x$ is the side ADJACENT to "
            "$90 - x$. Same side, same hypotenuse, same ratio — different name.  \n"
            "This identity is tested directly on the SAT, usually in exactly this phrasing, "
            "and the answer is always just the given value.",
            [
                "Eq(Rational(3,5), Rational(3,5))",
                "Eq(3**2 + 4**2, 5**2)",
                "Eq(Rational(4,5)**2 + Rational(3,5)**2, 1)",
            ],
        ),
        problem(
            "sat-rt2-w3",
            "A ramp rises at an angle of $12^\\circ$ to the horizontal and is $30$ metres "
            "long. How high does it rise, to the nearest tenth of a metre?",
            "**Answer.** About $6.2$ metres.  \n"
            "Draw the right triangle: the ramp is the hypotenuse, the rise is the side "
            "opposite the $12^\\circ$ angle, and the horizontal distance is adjacent.  \n"
            "Opposite and hypotenuse means SINE:\n"
            "$$\\sin 12^\\circ = \\frac{h}{30}$$\n"
            "$$h = 30 \\sin 12^\\circ \\approx 30 \\times 0.2079 \\approx 6.24$$\n"
            "so the rise is about $6.2$ metres.  \n"
            "The choice of ratio is the whole question. Label the three sides relative to the "
            "given angle first — opposite, adjacent, hypotenuse — then pick the ratio that "
            "uses the one you know and the one you want. Using cosine here would give the "
            "horizontal distance, about $29.3$ metres, which is also a listed option.  \n"
            "Make sure the calculator is in DEGREE mode. In radians, $\\sin 12$ is about "
            "$-0.54$, which would give a negative height.",
            [
                "Abs(30*sin(pi*12/180) - 6.24) < 0.05",
                "Abs(30*cos(pi*12/180) - 29.3) < 0.05",
                "sin(pi*12/180) < cos(pi*12/180)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-rt2-t1",
            "In a right triangle the side opposite angle $\\theta$ is $8$ and the hypotenuse "
            "is $17$. What is $\\sin \\theta$?",
            "**Answer.** $\\dfrac{8}{17}$. Opposite over hypotenuse. The adjacent side is "
            "$15$, so $\\cos \\theta = \\frac{15}{17}$.",
            ["Eq(17**2 - 8**2, 225)", "Eq(sqrt(225), 15)", "Eq(8**2 + 15**2, 17**2)"],
        ),
        problem(
            "sat-rt2-t2",
            "In a right triangle the leg adjacent to angle $\\theta$ is $9$ and the opposite "
            "leg is $12$. What is $\\tan \\theta$?",
            "**Answer.** $\\dfrac{4}{3}$. Tangent is opposite over adjacent: "
            "$\\frac{12}{9} = \\frac{4}{3}$. Inverting gives $\\frac{3}{4}$, a listed option.",
            ["Eq(Rational(12,9), Rational(4,3))", "Eq(9**2 + 12**2, 15**2)"],
        ),
        problem(
            "sat-rt2-t3",
            "If $\\cos y^\\circ = \\dfrac{7}{25}$, what is $\\sin(90 - y)^\\circ$?",
            "**Answer.** $\\dfrac{7}{25}$. Sine and cosine swap under complementary angles, so "
            "the value is unchanged.",
            ["Eq(Rational(7,25), Rational(7,25))", "Eq(7**2 + 24**2, 25**2)"],
        ),
        problem(
            "sat-rt2-t4",
            "A kite string $40$ metres long makes an angle of $55^\\circ$ with the ground. How "
            "high is the kite, to the nearest metre?",
            "**Answer.** About $33$ metres. The height is opposite the angle and the string is "
            "the hypotenuse, so $h = 40 \\sin 55^\\circ \\approx 32.8$.",
            [
                "Abs(40*sin(pi*55/180) - 32.8) < 0.1",
                "Abs(40*cos(pi*55/180) - 22.9) < 0.1",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Three ratios, all measured from an angle",
            "body": "In a right triangle, sine is opposite over hypotenuse, cosine is adjacent "
                    "over hypotenuse, and tangent is opposite over adjacent — SOH-CAH-TOA. "
                    "Every one of those words is relative to the angle you are working from. "
                    "Move to the other acute angle and 'opposite' and 'adjacent' swap, so the "
                    "sine and cosine swap too.",
        },
        {
            "kind": "trigRatios",
            "title": "The ratios do not depend on size",
            "teach": "Change the angle and watch all three ratios move. Then note what does "
                     "NOT change them: scaling the triangle. Similar triangles have equal "
                     "ratios, which is exactly why these three numbers depend on the angle "
                     "alone — and why trigonometry exists at all.",
            "config": {"start": 35},
        },
        {"kind": "worked", "title": "Reading a ratio from a triangle", "problemId": "sat-rt2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which ratio?",
            "prompt": "You know an angle and the hypotenuse, and you want the side ADJACENT to "
                      "that angle. Which ratio do you use?",
            "options": ["Cosine", "Sine", "Tangent", "Pythagoras"],
            "correctIndex": 0,
            "explanation": "Cosine relates the adjacent side to the hypotenuse. Sine would "
                           "give the opposite side; tangent needs two legs and involves no "
                           "hypotenuse at all. Label the sides relative to the angle first, "
                           "then pick the ratio joining what you have to what you want.",
            "check": [
                "Abs(10*cos(pi*60/180) - 5) < 0.001",
                "Abs(10*sin(pi*60/180) - 8.66) < 0.01",
            ],
        },
        {
            "kind": "teach",
            "title": "The complementary-angle identity",
            "beats": [
                "The two acute angles of a right triangle add to 90 degrees.",
                "Moving between them swaps opposite and adjacent.",
                "So sin θ = cos(90 − θ), and cos θ = sin(90 − θ).",
                "The SAT tests this directly, and the answer is always the value you were given.",
            ],
        },
        {"kind": "worked", "title": "Sine and cosine swapping", "problemId": "sat-rt2-w2"},
        {
            "kind": "tip",
            "title": "Label the sides before choosing a ratio",
            "body": "Write 'opp', 'adj' and 'hyp' on the diagram relative to the GIVEN angle. "
                    "Then look at which side you know and which you want, and pick the ratio "
                    "that joins them. Choosing the ratio first and labelling afterwards is how "
                    "students end up computing the horizontal distance when the question asked "
                    "for the height — and both are on the option list.",
        },
        {"kind": "worked", "title": "A ramp, and degree mode", "problemId": "sat-rt2-w3"},
        {"kind": "tryIt", "title": "Your turn: read a sine", "problemId": "sat-rt2-t1"},
        {"kind": "tryIt", "title": "Your turn: a tangent", "problemId": "sat-rt2-t2"},
        {"kind": "tryIt", "title": "Your turn: complementary angles", "problemId": "sat-rt2-t3"},
        {"kind": "tryIt", "title": "Your turn: a kite string", "problemId": "sat-rt2-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "SOH-CAH-TOA — and every word in it is relative to the angle you are using.",
                "Label opp, adj and hyp on the diagram before choosing a ratio.",
                "sin θ = cos(90 − θ): the complementary identity is tested directly.",
                "The ratios depend on the angle alone, not on the triangle's size.",
                "Keep the calculator in degree mode unless the question uses radians.",
            ],
        },
    ]

    return lesson(
        slug="trigonometric-ratios",
        title="Sine, Cosine and Tangent in Right Triangles",
        concrete=(
            "Two right triangles with the same angles have different sizes but identical side "
            "RATIOS — that is what similarity guarantees. So a ratio depends only on the "
            "angle, which means it can be looked up. That single observation is the whole of "
            "trigonometry."
        ),
        objective=(
            "Compute sine, cosine and tangent from a right triangle, choose the right ratio to "
            "solve for a missing side, and apply the complementary-angle identity."
        ),
        concept=[
            "**Skill card.** Still *Right triangles and trigonometry*, in the **Geometry and "
            "Trigonometry** domain. Trigonometry on the SAT stays inside right triangles — "
            "there is no law of sines or cosines, and radians appear only in the circles "
            "subtopic.",
            "Three ratios, remembered as SOH-CAH-TOA: sine is opposite over hypotenuse, cosine "
            "is adjacent over hypotenuse, tangent is opposite over adjacent. Every one of "
            "those labels is relative to the angle you are working from — the side 'opposite' "
            "angle $A$ is 'adjacent' to angle $B$.",
            "Why the ratios are worth anything: similar right triangles have equal ratios, so "
            "the value depends on the ANGLE alone and not on the triangle's size. That is the "
            "connection back to Unit 2, and it is why a single table of values works for every "
            "right triangle in existence.",
            "**The test's angle.** The complementary identity. The two acute angles of a right "
            "triangle add to $90^\\circ$, and swapping between them exchanges 'opposite' and "
            "'adjacent' — so $\\sin \\theta = \\cos(90^\\circ - \\theta)$. The SAT asks this "
            "in almost exactly that form, and the answer is always the value you were handed. "
            "The other regular loss is choosing the wrong ratio and computing the horizontal "
            "distance when the height was wanted; labelling the diagram first prevents it.",
        ],
        key_idea=(
            "Sine, cosine and tangent are side ratios measured from a chosen angle, and they "
            "depend on the angle alone. Label opposite, adjacent and hypotenuse first, then "
            "pick the ratio joining what you know to what you want."
        ),
        facts=[
            fact(
                "The three ratios",
                "\\sin\\theta = \\frac{\\text{opp}}{\\text{hyp}}, \\quad \\cos\\theta = \\frac{\\text{adj}}{\\text{hyp}}, \\quad \\tan\\theta = \\frac{\\text{opp}}{\\text{adj}}",
                "All three are relative to the angle $\\theta$.",
            ),
            fact(
                "Complementary angles",
                "\\sin\\theta = \\cos(90^\\circ - \\theta)",
                "The two acute angles swap opposite and adjacent, so they swap sine and "
                "cosine.",
            ),
            fact(
                "Solving for a side",
                "\\text{opp} = \\text{hyp}\\,\\sin\\theta, \\qquad \\text{adj} = \\text{hyp}\\,\\cos\\theta",
                "Pick the ratio that contains the side you know and the side you want.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Using 'opposite' and 'adjacent' relative to the wrong angle.",
                "The labels move when the angle does. Mark them on the diagram for the angle "
                "the question names.",
            ),
            mistake(
                "Inverting a ratio.",
                "Tangent is opposite over adjacent. Writing adjacent over opposite gives the "
                "reciprocal, which is a listed option.",
            ),
            mistake(
                "Choosing the ratio before labelling the sides.",
                "That is how the horizontal distance gets computed when the height was asked "
                "for. Label first.",
            ),
            mistake(
                "Leaving the calculator in radian mode.",
                "$\\sin 12$ in radians is negative. Degree mode unless the question says "
                "otherwise.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


RT_PRACTICE = [
    problem(
        "sat-rt-p01",
        "A right triangle has legs $6$ and $8$. What is the hypotenuse?",
        "**Answer.** $10$. The $3$-$4$-$5$ triangle doubled.",
        ["Eq(6**2 + 8**2, 100)", "Eq(sqrt(100), 10)"],
        badges=_b(RT_TAG, "Easy"),
    ),
    problem(
        "sat-rt-p02",
        "A right triangle has hypotenuse $15$ and one leg $9$. What is the other leg?",
        "**Answer.** $12$. $225 - 81 = 144$, so the leg is $12$ — the $3$-$4$-$5$ triangle "
        "tripled.",
        ["Eq(15**2 - 9**2, 144)", "Eq(sqrt(144), 12)"],
        badges=_b(RT_TAG, "Easy"),
    ),
    problem(
        "sat-rt-p03",
        "In a right triangle, the side opposite $\\theta$ is $7$ and the hypotenuse is $25$. "
        "What is $\\sin\\theta$?",
        "**Answer.** $\\dfrac{7}{25}$. Opposite over hypotenuse.",
        ["Eq(25**2 - 7**2, 576)", "Eq(sqrt(576), 24)", "Eq(7**2 + 24**2, 25**2)"],
        badges=_b(RT_TAG, "Easy"),
    ),
    problem(
        "sat-rt-p04",
        "In a $45$-$45$-$90$ triangle the hypotenuse is $10\\sqrt{2}$. What is the length of "
        "each leg?",
        "**Answer.** $10$. The hypotenuse is a leg times $\\sqrt{2}$, so the leg is "
        "$\\frac{10\\sqrt{2}}{\\sqrt{2}} = 10$.",
        [
            "Eq(simplify(10*sqrt(2)/sqrt(2)), 10)",
            "Eq(10**2 + 10**2, simplify((10*sqrt(2))**2))",
        ],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-p05",
        "If $\\sin a^\\circ = \\dfrac{9}{41}$, what is $\\cos(90 - a)^\\circ$?",
        "**Answer.** $\\dfrac{9}{41}$. Complementary angles swap sine and cosine, leaving the "
        "value unchanged.",
        ["Eq(9**2 + 40**2, 41**2)", "Eq(Rational(9,41), Rational(9,41))"],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-p06",
        "A ladder $8$ metres long leans against a wall at $70^\\circ$ to the ground. How far "
        "up the wall does it reach, to the nearest tenth of a metre?",
        "**Answer.** About $7.5$ metres. The height is opposite the angle and the ladder is "
        "the hypotenuse: $8\\sin 70^\\circ \\approx 7.52$. Using cosine gives the distance "
        "from the wall, about $2.7$ metres.",
        [
            "Abs(8*sin(pi*70/180) - 7.52) < 0.02",
            "Abs(8*cos(pi*70/180) - 2.74) < 0.02",
        ],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-p07",
        "In a $30$-$60$-$90$ triangle the longer leg is $12\\sqrt{3}$. What is the hypotenuse?",
        "**Answer.** $24$. The longer leg is the shorter leg times $\\sqrt{3}$, so the shorter "
        "leg is $12$; the hypotenuse is twice that.",
        [
            "Eq(simplify(12*sqrt(3)/sqrt(3)), 12)",
            "Eq(2*12, 24)",
            "Eq(simplify(12**2 + (12*sqrt(3))**2), 576)",
            "Eq(24**2, 576)",
        ],
        badges=_b(RT_TAG, "Hard"),
    ),
    problem(
        "sat-rt-p08",
        "In right triangle $PQR$ with the right angle at $Q$, $\\tan P = \\dfrac{3}{4}$ and "
        "$PQ = 8$. What is $QR$?",
        "**Answer.** $6$. Tangent is opposite over adjacent, and from angle $P$ the adjacent "
        "leg is $PQ = 8$ while the opposite leg is $QR$. So $\\frac{QR}{8} = \\frac{3}{4}$, "
        "giving $QR = 6$. The hypotenuse is then $10$ — the $3$-$4$-$5$ triangle doubled.",
        [
            "Eq(Rational(6,8), Rational(3,4))",
            "Eq(6**2 + 8**2, 100)",
            "Eq(sqrt(100), 10)",
        ],
        badges=_b(RT_TAG, "Hard"),
    ),
]

RT_TEST = [
    problem(
        "sat-rt-x01",
        "A right triangle has legs $12$ and $16$. What is the hypotenuse?",
        "**Answer.** $20$. The $3$-$4$-$5$ triangle scaled by $4$.",
        ["Eq(12**2 + 16**2, 400)", "Eq(sqrt(400), 20)"],
        badges=_b(RT_TAG, "Easy"),
    ),
    problem(
        "sat-rt-x02",
        "In a right triangle the legs are $5$ and $5$. What is the hypotenuse?",
        "**Answer.** $5\\sqrt{2}$. Equal legs make a $45$-$45$-$90$ triangle, so the "
        "hypotenuse is a leg times $\\sqrt{2}$.",
        ["Eq(5**2 + 5**2, 50)", "Eq(simplify((5*sqrt(2))**2), 50)"],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-x03",
        "In a right triangle, the leg adjacent to $\\theta$ is $24$ and the hypotenuse is "
        "$26$. What is $\\cos\\theta$?",
        "**Answer.** $\\dfrac{12}{13}$. Adjacent over hypotenuse is $\\frac{24}{26}$, which "
        "reduces to $\\frac{12}{13}$.",
        ["Eq(Rational(24,26), Rational(12,13))", "Eq(26**2 - 24**2, 100)"],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-x04",
        "If $\\cos b^\\circ = 0.6$, what is $\\sin(90 - b)^\\circ$?",
        "**Answer.** $0.6$. The complementary identity leaves the value unchanged.",
        ["Eq(Rational(6,10), Rational(3,5))", "Eq(Rational(3,5)**2 + Rational(4,5)**2, 1)"],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-x05",
        "A guy wire runs from the top of a $24$-metre mast to a point on the ground $7$ metres "
        "from its base. How long is the wire?",
        "**Answer.** $25$ metres. The mast and the ground distance are the legs: "
        "$576 + 49 = 625$, and $\\sqrt{625} = 25$ — the $7$-$24$-$25$ triple.",
        ["Eq(24**2 + 7**2, 625)", "Eq(sqrt(625), 25)"],
        badges=_b(RT_TAG, "Medium"),
    ),
    problem(
        "sat-rt-x06",
        "A slide makes an angle of $38^\\circ$ with the ground and its top is $3$ metres above "
        "the ground. How long is the slide, to the nearest tenth of a metre?",
        "**Answer.** About $4.9$ metres. The height is opposite the angle and the slide is the "
        "hypotenuse, so $\\sin 38^\\circ = \\frac{3}{L}$ and "
        "$L = \\frac{3}{\\sin 38^\\circ} \\approx 4.87$. Multiplying instead of dividing gives "
        "$1.85$, which would be shorter than the height — impossible for a hypotenuse.",
        [
            "Abs(3/sin(pi*38/180) - 4.87) < 0.02",
            "3/sin(pi*38/180) > 3",
            "Abs(3*sin(pi*38/180) - 1.85) < 0.02",
        ],
        badges=_b(RT_TAG, "Hard"),
    ),
]


# ===========================================================================
# UNIT 4 — Circles
# ===========================================================================

def lesson_circle_equations():
    worked = [
        problem(
            "sat-ci1-w1",
            "What are the centre and radius of the circle $(x - 3)^{2} + (y + 5)^{2} = 49$?",
            "**Answer.** Centre $(3, -5)$, radius $7$.  \n"
            "The standard form of a circle is\n"
            "$$(x - h)^{2} + (y - k)^{2} = r^{2}$$\n"
            "with centre $(h, k)$ and radius $r$. Match it term by term.  \n"
            "The $x$ part is $(x - 3)^{2}$, so $h = 3$. The $y$ part is written $(y + 5)^{2}$, "
            "which is $(y - (-5))^{2}$, so $k = -5$: the sign FLIPS, exactly as it does in the "
            "vertex form of a parabola.  \n"
            "The right-hand side is $r^{2}$, not $r$. So $r^{2} = 49$ gives $r = 7$.  \n"
            "Two traps, both on every version of this question. Reading the centre as "
            "$(3, 5)$ misses the sign flip, and reporting the radius as $49$ forgets the "
            "square root.",
            [
                "Eq(expand((3 - 3)**2 + (-5 + 5)**2), 0)",
                "Eq(sqrt(49), 7)",
                "Eq((3 + 7 - 3)**2 + (-5 + 5)**2, 49)",
            ],
        ),
        problem(
            "sat-ci1-w2",
            "The equation of a circle is $x^{2} + y^{2} - 6x + 8y = 0$. What is its radius?",
            "**Answer.** $5$.  \n"
            "The equation is in expanded form, so complete the square in $x$ and in $y$ "
            "separately.  \n"
            "For $x$: half of $-6$ is $-3$, and $(-3)^{2} = 9$.  \n"
            "For $y$: half of $8$ is $4$, and $4^{2} = 16$.  \n"
            "Add both to each side:\n"
            "$$(x^{2} - 6x + 9) + (y^{2} + 8y + 16) = 0 + 9 + 16$$\n"
            "$$(x - 3)^{2} + (y + 4)^{2} = 25$$\n"
            "So the centre is $(3, -4)$ and the radius is $\\sqrt{25} = 5$.  \n"
            "Check that the centre is right: the origin satisfies the original equation, and "
            "its distance from $(3, -4)$ is $\\sqrt{9 + 16} = 5$, matching the radius exactly "
            "as it should.  \n"
            "The step people skip is adding the completing constants to the RIGHT side too. "
            "Adding $9$ and $16$ only on the left changes the circle.",
            [
                "Eq(expand((x - 3)**2 + (y + 4)**2 - 25), x**2 + y**2 - 6*x + 8*y)",
                "Eq(sqrt(25), 5)",
                "Eq(3**2 + (-4)**2, 25)",
            ],
        ),
        problem(
            "sat-ci1-w3",
            "A circle has centre $(2, -1)$ and passes through the point $(6, 2)$. What is its "
            "equation?",
            "**Answer.** $(x - 2)^{2} + (y + 1)^{2} = 25$.  \n"
            "The radius is the distance from the centre to any point on the circle:\n"
            "$$r = \\sqrt{(6 - 2)^{2} + (2 - (-1))^{2}} = \\sqrt{16 + 9} = \\sqrt{25} = 5$$\n"
            "Now substitute the centre and $r^{2} = 25$ into the standard form:\n"
            "$$(x - 2)^{2} + (y + 1)^{2} = 25$$\n"
            "Note that $r^{2}$, not $r$, goes on the right — and that the $-1$ in the centre "
            "becomes $+1$ in the equation.  \n"
            "Check: substituting $(6, 2)$ gives $16 + 9 = 25$, so the point does lie on the "
            "circle.  \n"
            "The distance formula here is Pythagoras in disguise: the horizontal and vertical "
            "gaps between the two points are the legs of a right triangle whose hypotenuse is "
            "the radius.",
            [
                "Eq((6 - 2)**2 + (2 + 1)**2, 25)",
                "Eq(sqrt(25), 5)",
                "Eq(4**2 + 3**2, 5**2)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ci1-t1",
            "What is the centre of the circle $(x + 4)^{2} + (y - 7)^{2} = 36$?",
            "**Answer.** $(-4, 7)$. Both signs flip relative to the equation, and the radius "
            "is $6$.",
            ["Eq((-4 + 4)**2 + (7 - 7)**2, 0)", "Eq(sqrt(36), 6)"],
        ),
        problem(
            "sat-ci1-t2",
            "What is the radius of the circle $(x - 1)^{2} + (y + 3)^{2} = 20$?",
            "**Answer.** $2\\sqrt{5}$. The radius is $\\sqrt{20}$, which simplifies to "
            "$2\\sqrt{5} \\approx 4.47$. Reporting $20$ forgets the square root.",
            ["Eq(simplify(sqrt(20) - 2*sqrt(5)), 0)", "Eq(simplify((2*sqrt(5))**2), 20)"],
        ),
        problem(
            "sat-ci1-t3",
            "A circle has centre $(0, 0)$ and passes through $(5, 12)$. What is its equation?",
            "**Answer.** $x^{2} + y^{2} = 169$. The radius is "
            "$\\sqrt{25 + 144} = 13$, and $r^{2} = 169$.",
            ["Eq(5**2 + 12**2, 169)", "Eq(sqrt(169), 13)"],
        ),
        problem(
            "sat-ci1-t4",
            "Find the centre of the circle $x^{2} + y^{2} + 10x - 4y = 7$.",
            "**Answer.** $(-5, 2)$. Completing the square gives "
            "$(x + 5)^{2} + (y - 2)^{2} = 7 + 25 + 4 = 36$, so the centre is $(-5, 2)$ and the "
            "radius is $6$.",
            [
                "Eq(expand((x + 5)**2 + (y - 2)**2 - 36), x**2 + y**2 + 10*x - 4*y - 7)",
                "Eq(sqrt(36), 6)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Circles",
            "beats": [
                "Domain: Geometry and Trigonometry — 5 to 7 of the 44 questions.",
                "Usually 1 question, split between coordinate circles and arcs and sectors.",
                "Prerequisites: completing the square, and Pythagoras.",
                "The equation of a circle IS the distance formula, rearranged.",
            ],
        },
        {
            "kind": "teach",
            "title": "Why the equation looks like that",
            "body": "A circle is every point at a fixed distance from a centre. The distance "
                    "from $(x, y)$ to $(h, k)$ is "
                    "$\\sqrt{(x-h)^{2} + (y-k)^{2}}$, so demanding that this equal $r$ and "
                    "squaring both sides gives $(x-h)^{2} + (y-k)^{2} = r^{2}$. The equation "
                    "is Pythagoras applied to the horizontal and vertical gaps.",
        },
        {
            "kind": "coordGeo",
            "title": "Centre, radius, equation",
            "teach": "Move the centre and change the radius, and watch the equation rewrite "
                     "itself. Notice the signs: a centre at negative four shows up as a plus "
                     "four in the bracket.",
            "config": {"mode": "circle", "center": {"x": 3, "y": -5}, "r": 7, "min": -8, "max": 12},
        },
        {"kind": "worked", "title": "Reading centre and radius", "problemId": "sat-ci1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Mind the signs and the square",
            "prompt": "What are the centre and radius of "
                      "$(x + 2)^{2} + (y - 6)^{2} = 16$?",
            "options": [
                "Centre $(-2, 6)$, radius $4$",
                "Centre $(2, -6)$, radius $4$",
                "Centre $(-2, 6)$, radius $16$",
                "Centre $(2, -6)$, radius $16$",
            ],
            "correctIndex": 0,
            "explanation": "The signs flip: $(x + 2)$ means $h = -2$, and $(y - 6)$ means "
                           "$k = 6$. The right-hand side is $r^{2}$, so $r = \\sqrt{16} = 4$. "
                           "Options C and D forget the square root; B and D miss the sign "
                           "flip.",
            "check": ["Eq((-2 + 2)**2 + (6 - 6)**2, 0)", "Eq(sqrt(16), 4)"],
        },
        {"kind": "worked", "title": "Completing the square", "problemId": "sat-ci1-w2"},
        {
            "kind": "tip",
            "title": "Add to both sides when completing the square",
            "body": "Completing the square in $x$ and in $y$ means adding two constants to the "
                    "left-hand side, and both must be added to the RIGHT as well. Skipping "
                    "that changes the circle and gives a wrong radius — usually a smaller one, "
                    "which is on the option list.",
        },
        {"kind": "worked", "title": "Building the equation from a point", "problemId": "sat-ci1-w3"},
        {"kind": "tryIt", "title": "Your turn: flip the signs", "problemId": "sat-ci1-t1"},
        {"kind": "tryIt", "title": "Your turn: an irrational radius", "problemId": "sat-ci1-t2"},
        {"kind": "tryIt", "title": "Your turn: from a point", "problemId": "sat-ci1-t3"},
        {"kind": "tryIt", "title": "Your turn: complete both squares", "problemId": "sat-ci1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Standard form is (x − h)² + (y − k)² = r², with centre (h, k).",
                "The signs in the brackets are the OPPOSITE of the centre's coordinates.",
                "The right-hand side is r squared — take the root for the radius.",
                "Expanded form needs completing the square, in x and in y separately.",
                "Whatever you add on the left to complete a square, add on the right too.",
            ],
        },
    ]

    return lesson(
        slug="circles-in-the-coordinate-plane",
        title="The Equation of a Circle",
        concrete=(
            "A radio mast reaches every house within twelve kilometres. That boundary is a "
            "circle, and writing it down is nothing more than Pythagoras: the horizontal and "
            "vertical distances from the mast are the legs of a right triangle whose "
            "hypotenuse is always twelve."
        ),
        objective=(
            "Read the centre and radius from a circle's equation, complete the square to get "
            "there from expanded form, and build the equation from a centre and a point."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Circles*, in the **Geometry and "
            "Trigonometry** domain. It is usually one question, split between coordinate "
            "circles and the arcs-and-sectors work in the next lesson.",
            "A circle is the set of points at a fixed distance from a centre. Since the "
            "distance from $(x, y)$ to $(h, k)$ is $\\sqrt{(x-h)^{2} + (y-k)^{2}}$, setting "
            "that equal to $r$ and squaring gives the standard form "
            "$(x-h)^{2} + (y-k)^{2} = r^{2}$. The equation is Pythagoras, applied to the "
            "horizontal and vertical gaps.",
            "Two signs to watch. The centre's coordinates are the OPPOSITE of the numbers in "
            "the brackets: $(x + 2)^{2}$ means $h = -2$. And the right-hand side is $r^{2}$, "
            "not $r$, so a $49$ there means a radius of $7$.",
            "**The test's angle.** Expanded form. When the equation arrives as "
            "$x^{2} + y^{2} - 6x + 8y = 0$, complete the square in $x$ and in $y$ separately "
            "— half the coefficient, squared, added to BOTH sides. Adding the constants only "
            "on the left is the standard error and produces a smaller radius, which is on the "
            "option list.",
        ],
        key_idea=(
            "$(x-h)^{2} + (y-k)^{2} = r^{2}$: centre $(h, k)$ with the signs flipped, and the "
            "right-hand side is the radius SQUARED."
        ),
        facts=[
            fact(
                "Standard form",
                "(x - h)^{2} + (y - k)^{2} = r^{2}",
                "Centre $(h, k)$, radius $r$. The bracket signs are opposite to the centre's "
                "coordinates.",
            ),
            fact(
                "Distance between two points",
                "d = \\sqrt{(x_2 - x_1)^{2} + (y_2 - y_1)^{2}}",
                "Pythagoras on the horizontal and vertical gaps. This is where the circle "
                "equation comes from.",
            ),
            fact(
                "Completing the square",
                "x^{2} + bx \\;\\longrightarrow\\; \\left(x + \\tfrac{b}{2}\\right)^{2}, \\text{ adding } \\tfrac{b^{2}}{4} \\text{ to both sides}",
                "Do it separately for $x$ and for $y$, and balance the right-hand side each "
                "time.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Reading the centre straight out of the brackets.",
                "$(x + 4)^{2}$ means the centre's $x$-coordinate is $-4$. The sign flips.",
            ),
            mistake(
                "Reporting the right-hand side as the radius.",
                "It is $r^{2}$. A $36$ there means a radius of $6$.",
            ),
            mistake(
                "Completing the square without balancing the other side.",
                "Every constant added on the left must be added on the right, or the circle "
                "changes.",
            ),
            mistake(
                "Leaving an irrational radius unsimplified.",
                "$\\sqrt{20}$ is $2\\sqrt{5}$, and the option list will use the simplified "
                "form.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_arcs():
    worked = [
        problem(
            "sat-ci2-w1",
            "A circle has radius $9$. A sector has a central angle of $80^\\circ$. What are "
            "the arc length and the sector area, in terms of $\\pi$?",
            "**Answer.** Arc $4\\pi$, area $18\\pi$.  \n"
            "A sector is a FRACTION of the whole circle, and the fraction is the same for both "
            "quantities:\n"
            "$$\\frac{80}{360} = \\frac{2}{9}$$\n"
            "The whole circumference is $2\\pi(9) = 18\\pi$, so the arc is\n"
            "$$\\frac{2}{9} \\times 18\\pi = 4\\pi$$\n"
            "The whole area is $\\pi(9)^{2} = 81\\pi$, so the sector is\n"
            "$$\\frac{2}{9} \\times 81\\pi = 18\\pi$$\n"
            "That is the entire method: work out what fraction of the circle you have, then "
            "take that fraction of whichever total the question wants.  \n"
            "Using the same total for both is the error to avoid — an arc is a LENGTH and "
            "comes from the circumference; a sector is an AREA and comes from the area.",
            [
                "Eq(Rational(80,360), Rational(2,9))",
                "Eq(2*9, 18)",
                "Eq(Rational(2,9)*18, 4)",
                "Eq(9**2, 81)",
                "Eq(Rational(2,9)*81, 18)",
            ],
        ),
        problem(
            "sat-ci2-w2",
            "In a circle, a central angle and an inscribed angle both intercept the same arc. "
            "The central angle measures $70^\\circ$. What does the inscribed angle measure?",
            "**Answer.** $35^\\circ$.  \n"
            "An inscribed angle — one whose vertex sits ON the circle — is always exactly HALF "
            "the central angle intercepting the same arc:\n"
            "$$\\frac{70^\\circ}{2} = 35^\\circ$$\n"
            "The central angle, with its vertex at the centre, equals the arc's measure. So "
            "the inscribed angle is half the arc too.  \n"
            "One consequence appears constantly on the SAT: an angle inscribed in a "
            "SEMICIRCLE — where the intercepted arc is $180^\\circ$ — measures $90^\\circ$. "
            "So any triangle drawn with one side as a diameter and its third vertex on the "
            "circle is right-angled, which quietly connects this subtopic to Pythagoras.  \n"
            "Doubling instead of halving gives $140^\\circ$, which is a listed option.",
            [
                "Eq(Rational(70,2), 35)",
                "Eq(Rational(180,2), 90)",
                "Eq(2*35, 70)",
            ],
        ),
        problem(
            "sat-ci2-w3",
            "A circle has radius $6$. An arc of the circle has length $4\\pi$. What is the "
            "central angle, in radians?",
            "**Answer.** $\\dfrac{2\\pi}{3}$.  \n"
            "In radians the arc-length relationship is as simple as it gets:\n"
            "$$s = r\\theta$$\n"
            "so\n"
            "$$4\\pi = 6\\theta \\;\\Longrightarrow\\; \\theta = \\frac{2\\pi}{3}$$\n"
            "That formula is the REASON radians exist: measuring an angle by the arc it cuts "
            "off, in units of the radius, removes every conversion factor.  \n"
            "In degrees the same angle is\n"
            "$$\\frac{2\\pi}{3} \\times \\frac{180}{\\pi} = 120^\\circ$$\n"
            "and the fraction check confirms it: $\\frac{120}{360} = \\frac{1}{3}$, and a "
            "third of the circumference $12\\pi$ is indeed $4\\pi$.  \n"
            "Converting between the two is one multiplication: $180^\\circ$ is $\\pi$ radians, "
            "so multiply by $\\frac{\\pi}{180}$ to go into radians and by $\\frac{180}{\\pi}$ "
            "to come back.",
            [
                "Eq(6*Rational(2,3)*pi, 4*pi)",
                "Eq(Rational(2,3)*pi*Rational(180,1)/pi, 120)",
                "Eq(Rational(120,360), Rational(1,3))",
                "Eq(Rational(1,3)*12, 4)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ci2-t1",
            "A circle has radius $10$. What is the length of an arc with central angle "
            "$36^\\circ$, in terms of $\\pi$?",
            "**Answer.** $2\\pi$. The fraction is $\\frac{36}{360} = \\frac{1}{10}$, and the "
            "circumference is $20\\pi$.",
            ["Eq(Rational(36,360), Rational(1,10))", "Eq(Rational(1,10)*20, 2)"],
        ),
        problem(
            "sat-ci2-t2",
            "A circle has radius $4$. What is the area of a sector with central angle "
            "$135^\\circ$, in terms of $\\pi$?",
            "**Answer.** $6\\pi$. The fraction is $\\frac{135}{360} = \\frac{3}{8}$, and the "
            "full area is $16\\pi$, so the sector is $\\frac{3}{8} \\times 16\\pi = 6\\pi$.",
            ["Eq(Rational(135,360), Rational(3,8))", "Eq(Rational(3,8)*16, 6)"],
        ),
        problem(
            "sat-ci2-t3",
            "An inscribed angle measures $48^\\circ$. What is the measure of the arc it "
            "intercepts?",
            "**Answer.** $96^\\circ$. The arc equals the central angle, which is twice the "
            "inscribed angle.",
            ["Eq(2*48, 96)"],
        ),
        problem(
            "sat-ci2-t4",
            "Convert $150^\\circ$ to radians.",
            "**Answer.** $\\dfrac{5\\pi}{6}$. Multiply by $\\frac{\\pi}{180}$: "
            "$150 \\times \\frac{\\pi}{180} = \\frac{5\\pi}{6}$.",
            ["Eq(150*pi/180, 5*pi/6)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "A sector is a fraction of the circle",
            "body": "Every arc-and-sector question is the same two steps. Find what fraction of "
                    "the full circle the central angle represents — that is the angle over "
                    "$360$ — then take that fraction of whichever total you need. An arc is a "
                    "fraction of the CIRCUMFERENCE; a sector is the same fraction of the AREA.",
        },
        {
            "kind": "arcSector",
            "title": "One fraction, two answers",
            "teach": "Sweep the central angle and watch both readouts move together. The "
                     "fraction of the circle is the same for the arc and for the sector — only "
                     "the total it multiplies changes.",
            "config": {"start": 80, "radius": 9},
        },
        {"kind": "worked", "title": "Arc and sector at once", "problemId": "sat-ci2-w1"},
        {
            "kind": "circleAngle",
            "title": "Central and inscribed",
            "teach": "Two angles standing on the same arc: one with its vertex at the centre, "
                     "one on the circle itself. Drag them and the inscribed angle stays "
                     "exactly half the central one, wherever on the circle its vertex sits.",
            "config": {"mode": "inscribed", "start": 70},
        },
        {
            "kind": "tapQuestion",
            "title": "Half or double?",
            "prompt": "A central angle intercepting an arc measures $100^\\circ$. What does an "
                      "inscribed angle on the same arc measure?",
            "options": ["$50^\\circ$", "$200^\\circ$", "$100^\\circ$", "$80^\\circ$"],
            "correctIndex": 0,
            "explanation": "An inscribed angle is half the central angle on the same arc, so "
                           "$\\frac{100}{2} = 50$. Option B doubles instead of halving — the "
                           "standard reversal — and C forgets the relationship entirely.",
            "check": ["Eq(Rational(100,2), 50)", "Eq(2*50, 100)"],
        },
        {"kind": "worked", "title": "Inscribed angles, and the semicircle", "problemId": "sat-ci2-w2"},
        {
            "kind": "teach",
            "title": "Radians, and why they simplify things",
            "beats": [
                "180 degrees is π radians — that one fact drives every conversion.",
                "Degrees to radians: multiply by π/180. Back again: multiply by 180/π.",
                "In radians, arc length is simply s = rθ.",
                "And sector area is A = ½r²θ — no 360 anywhere.",
            ],
        },
        {"kind": "worked", "title": "Working in radians", "problemId": "sat-ci2-w3"},
        {"kind": "tryIt", "title": "Your turn: an arc", "problemId": "sat-ci2-t1"},
        {"kind": "tryIt", "title": "Your turn: a sector", "problemId": "sat-ci2-t2"},
        {"kind": "tryIt", "title": "Your turn: inscribed to arc", "problemId": "sat-ci2-t3"},
        {"kind": "tryIt", "title": "Your turn: convert to radians", "problemId": "sat-ci2-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "The central angle over 360 gives the fraction of the circle you have.",
                "Arc length is that fraction of the circumference; sector area is that fraction of the area.",
                "An inscribed angle is HALF the central angle on the same arc.",
                "An angle inscribed in a semicircle is a right angle.",
                "180 degrees is π radians, and in radians arc length is just s = rθ.",
            ],
        },
    ]

    return lesson(
        slug="arcs-sectors-and-angles",
        title="Arcs, Sectors, Inscribed Angles and Radians",
        concrete=(
            "A slice of pizza is a sector. Its crust is an arc. Both are the same fraction of "
            "the whole pizza — the fraction the angle at the point represents — and knowing "
            "that fraction answers every question about either one."
        ),
        objective=(
            "Find arc lengths and sector areas from a central angle, use the inscribed-angle "
            "relationship, and convert between degrees and radians."
        ),
        concept=[
            "**Skill card.** Still *Circles*, in the **Geometry and Trigonometry** domain. "
            "This is where radians appear on the SAT — the only place they do.",
            "A sector is a fraction of the circle, and the fraction is the central angle over "
            "$360^\\circ$. Take that fraction of the CIRCUMFERENCE for an arc length, and the "
            "same fraction of the AREA for a sector's area. Using the wrong total is the main "
            "error: an arc is a length, a sector is an area.",
            "An inscribed angle — vertex on the circle — is exactly HALF the central angle "
            "intercepting the same arc. One case is worth memorising: an angle inscribed in a "
            "semicircle intercepts a $180^\\circ$ arc and is therefore a right angle, so any "
            "triangle with a diameter as one side and its third vertex on the circle is "
            "right-angled.",
            "**The test's angle.** Radians. $180^\\circ$ is $\\pi$ radians, so multiply by "
            "$\\frac{\\pi}{180}$ going in and $\\frac{180}{\\pi}$ coming back. Radians exist "
            "because they make the arc-length formula trivial: $s = r\\theta$, with no $360$ "
            "and no $\\pi$ conversion. Sector area is $\\frac{1}{2}r^{2}\\theta$ for the same "
            "reason.",
        ],
        key_idea=(
            "The central angle over $360^\\circ$ is the fraction of the circle. Multiply that "
            "fraction by the circumference for an arc and by the area for a sector — and an "
            "inscribed angle is half the central one."
        ),
        facts=[
            fact(
                "Arc and sector in degrees",
                "s = \\frac{\\theta}{360} \\cdot 2\\pi r, \\qquad A = \\frac{\\theta}{360} \\cdot \\pi r^{2}",
                "The same fraction, applied to the circumference and to the area.",
            ),
            fact(
                "Inscribed angle",
                "\\text{inscribed} = \\tfrac{1}{2} \\times \\text{central on the same arc}",
                "An angle inscribed in a semicircle is a right angle.",
            ),
            fact(
                "Radians",
                "180^\\circ = \\pi \\text{ rad}, \\qquad s = r\\theta, \\qquad A = \\tfrac{1}{2}r^{2}\\theta",
                "The last two hold only in radians, which is why radians are used at all.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Using the area when computing an arc length.",
                "An arc is a fraction of the CIRCUMFERENCE. The sector's area is a fraction of "
                "the area.",
            ),
            mistake(
                "Doubling instead of halving for an inscribed angle.",
                "The inscribed angle is half the central angle. Doubling gives a listed wrong "
                "option.",
            ),
            mistake(
                "Using $s = r\\theta$ with $\\theta$ in degrees.",
                "That formula requires radians. In degrees, use the fraction over $360$.",
            ),
            mistake(
                "Inverting the degree-radian conversion.",
                "Degrees to radians multiplies by $\\frac{\\pi}{180}$. Going the other way "
                "multiplies by $\\frac{180}{\\pi}$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


CIR_PRACTICE = [
    problem(
        "sat-ci-p01",
        "What is the radius of the circle $(x - 2)^{2} + (y - 5)^{2} = 64$?",
        "**Answer.** $8$. The right-hand side is $r^{2}$.",
        ["Eq(sqrt(64), 8)"],
        badges=_b(CIR_TAG, "Easy"),
    ),
    problem(
        "sat-ci-p02",
        "What is the centre of the circle $(x + 7)^{2} + (y - 1)^{2} = 9$?",
        "**Answer.** $(-7, 1)$. The signs in the brackets are opposite to the centre's "
        "coordinates.",
        ["Eq((-7 + 7)**2 + (1 - 1)**2, 0)", "Eq(sqrt(9), 3)"],
        badges=_b(CIR_TAG, "Easy"),
    ),
    problem(
        "sat-ci-p03",
        "A circle has radius $12$. What is the length of an arc with central angle "
        "$60^\\circ$, in terms of $\\pi$?",
        "**Answer.** $4\\pi$. The fraction is $\\frac{1}{6}$ and the circumference is "
        "$24\\pi$.",
        ["Eq(Rational(60,360), Rational(1,6))", "Eq(Rational(1,6)*24, 4)"],
        badges=_b(CIR_TAG, "Easy"),
    ),
    problem(
        "sat-ci-p04",
        "An inscribed angle intercepts an arc of $110^\\circ$. What is the inscribed angle?",
        "**Answer.** $55^\\circ$. The arc equals the central angle, and the inscribed angle is "
        "half of it.",
        ["Eq(Rational(110,2), 55)"],
        badges=_b(CIR_TAG, "Medium"),
    ),
    problem(
        "sat-ci-p05",
        "A circle has centre $(1, -2)$ and radius $\\sqrt{10}$. What is its equation?",
        "**Answer.** $(x - 1)^{2} + (y + 2)^{2} = 10$. The right-hand side is $r^{2} = 10$, "
        "not $\\sqrt{10}$.",
        ["Eq(simplify(sqrt(10)**2), 10)", "Eq((1 - 1)**2 + (-2 + 2)**2, 0)"],
        badges=_b(CIR_TAG, "Medium"),
    ),
    problem(
        "sat-ci-p06",
        "Convert $\\dfrac{3\\pi}{4}$ radians to degrees.",
        "**Answer.** $135^\\circ$. Multiply by $\\frac{180}{\\pi}$.",
        ["Eq(3*pi/4*180/pi, 135)"],
        badges=_b(CIR_TAG, "Medium"),
    ),
    problem(
        "sat-ci-p07",
        "Find the centre and radius of the circle $x^{2} + y^{2} - 4x + 6y - 12 = 0$.",
        "**Answer.** Centre $(2, -3)$, radius $5$. Completing both squares gives "
        "$(x - 2)^{2} + (y + 3)^{2} = 12 + 4 + 9 = 25$.",
        [
            "Eq(expand((x - 2)**2 + (y + 3)**2 - 25), x**2 + y**2 - 4*x + 6*y - 12)",
            "Eq(sqrt(25), 5)",
        ],
        badges=_b(CIR_TAG, "Hard"),
    ),
    problem(
        "sat-ci-p08",
        "A circle has radius $5$ and a sector has area $\\dfrac{25\\pi}{4}$. What is the "
        "central angle, in degrees?",
        "**Answer.** $90^\\circ$. The full area is $25\\pi$, so the sector is a quarter of the "
        "circle, and a quarter of $360^\\circ$ is $90^\\circ$.",
        [
            "Eq(5**2, 25)",
            "Eq(Rational(25,4)/25, Rational(1,4))",
            "Eq(Rational(1,4)*360, 90)",
        ],
        badges=_b(CIR_TAG, "Hard"),
    ),
]

CIR_TEST = [
    problem(
        "sat-ci-x01",
        "What is the centre of the circle $(x - 6)^{2} + (y + 3)^{2} = 100$?",
        "**Answer.** $(6, -3)$, with radius $10$.",
        ["Eq((6 - 6)**2 + (-3 + 3)**2, 0)", "Eq(sqrt(100), 10)"],
        badges=_b(CIR_TAG, "Easy"),
    ),
    problem(
        "sat-ci-x02",
        "A circle has radius $8$. What is the area of a sector with central angle "
        "$45^\\circ$, in terms of $\\pi$?",
        "**Answer.** $8\\pi$. The fraction is $\\frac{1}{8}$ and the full area is $64\\pi$.",
        ["Eq(Rational(45,360), Rational(1,8))", "Eq(Rational(1,8)*64, 8)"],
        badges=_b(CIR_TAG, "Medium"),
    ),
    problem(
        "sat-ci-x03",
        "A triangle is inscribed in a circle with one side as a diameter. What is the measure "
        "of the angle opposite that side?",
        "**Answer.** $90^\\circ$. The diameter cuts off a $180^\\circ$ arc, and the inscribed "
        "angle is half of it. Every triangle drawn this way is right-angled.",
        ["Eq(Rational(180,2), 90)"],
        badges=_b(CIR_TAG, "Medium"),
    ),
    problem(
        "sat-ci-x04",
        "A circle has centre $(-3, 4)$ and passes through the origin. What is its equation?",
        "**Answer.** $(x + 3)^{2} + (y - 4)^{2} = 25$. The radius is the distance from "
        "$(-3, 4)$ to $(0, 0)$, which is $\\sqrt{9 + 16} = 5$.",
        ["Eq((-3)**2 + 4**2, 25)", "Eq(sqrt(25), 5)", "Eq((0 + 3)**2 + (0 - 4)**2, 25)"],
        badges=_b(CIR_TAG, "Medium"),
    ),
    problem(
        "sat-ci-x05",
        "A circle has radius $7$ and an arc subtends a central angle of $\\dfrac{\\pi}{2}$ "
        "radians. What is the arc length?",
        "**Answer.** $\\dfrac{7\\pi}{2}$. In radians, $s = r\\theta = 7 \\times "
        "\\frac{\\pi}{2}$.",
        ["Eq(7*pi/2, 7*pi/2)", "Eq(pi/2*180/pi, 90)", "Eq(Rational(90,360)*14, Rational(7,2))"],
        badges=_b(CIR_TAG, "Hard"),
    ),
    problem(
        "sat-ci-x06",
        "Find the radius of the circle $x^{2} + y^{2} + 8x - 2y + 8 = 0$.",
        "**Answer.** $3$. Completing both squares gives "
        "$(x + 4)^{2} + (y - 1)^{2} = -8 + 16 + 1 = 9$, so the radius is $3$. Forgetting to "
        "move the $8$ across gives a different, wrong radius.",
        [
            "Eq(expand((x + 4)**2 + (y - 1)**2 - 9), x**2 + y**2 + 8*x - 2*y + 8)",
            "Eq(sqrt(9), 3)",
        ],
        badges=_b(CIR_TAG, "Hard"),
    ),
]


def main():
    write_unit(
        COURSE,
        "right-triangles-and-trigonometry",
        "Right Triangles and Trigonometry",
        3,
        "Pythagoras and the triples worth recognising, the two special triangles from the "
        "reference sheet, the three trigonometric ratios and how to pick one — and the "
        "complementary identity the test asks about directly.",
        "Similarity from Unit 2 — equal ratios in similar right triangles are exactly why "
        "trigonometry works.",
        [lesson_pythagoras(), lesson_trig()],
        RT_PRACTICE,
        RT_TEST,
    )
    write_unit(
        COURSE,
        "circles",
        "Circles",
        4,
        "The equation of a circle and the completing-the-square work to reach it, arcs and "
        "sectors as fractions of the whole, inscribed angles at half the central angle, and "
        "the radians that make arc length a single multiplication.",
        "Pythagoras from Unit 3 — the circle equation is the distance formula squared.",
        [lesson_circle_equations(), lesson_arcs()],
        CIR_PRACTICE,
        CIR_TEST,
    )


if __name__ == "__main__":
    main()
