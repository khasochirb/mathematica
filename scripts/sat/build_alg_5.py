#!/usr/bin/env python3
"""SAT Math — Algebra, Unit 5: Linear inequalities in one or two variables.

Builds data/genmath/sat/linear-inequalities.json. Three lessons: solving in
one variable (and the flip), the half-plane picture in two variables, and the
constraint systems the test builds word problems from.

Run: python3 scripts/sat/build_alg_5.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "linear-inequalities"
TAG = {"text": "sat-linear-inequalities", "mono": True}


def _b(level):
    return [TAG, {"text": level}]


# ===========================================================================
# Lesson 1 — solving in one variable
# ===========================================================================

def lesson_solving():
    worked = [
        problem(
            "sat-l5a-w1",
            "What is the greatest integer $x$ that satisfies $7 - 3x > -8$?",
            "**Answer.** $4$.  \n"
            "Solve the inequality exactly as you would an equation, until the moment you "
            "divide by a negative number.\n"
            "$$7 - 3x > -8$$\n"
            "Subtract $7$ from both sides — adding and subtracting never affect the direction:\n"
            "$$-3x > -15$$\n"
            "Now divide by $-3$. Dividing by a negative REVERSES the inequality sign:\n"
            "$$x < 5$$\n"
            "The greatest integer strictly less than $5$ is $4$.  \n"
            "Check the boundary carefully: at $x = 4$, $7 - 12 = -5$, and $-5 > -8$ is true. "
            "At $x = 5$, $7 - 15 = -8$, and $-8 > -8$ is FALSE because the inequality is "
            "strict. That is why the answer is $4$ and not $5$.  \n"
            "Forgetting to flip gives $x > 5$ and the answer 'no greatest integer exists' — "
            "which is why the flip is the single most important rule in this unit.",
            [
                "7 - 3*4 > -8",
                "Eq(7 - 3*5, -8)",
                "Not(7 - 3*5 > -8)",
                "Eq(solve(7 - 3*x > -8, x).as_set().sup, 5)",
            ],
        ),
        problem(
            "sat-l5a-w2",
            "$$4(x - 2) \\le 6x + 10$$\n"
            "Which of the following describes all solutions to the inequality above?",
            "**Answer.** $x \\ge -9$.  \n"
            "Distribute first:\n"
            "$$4x - 8 \\le 6x + 10$$\n"
            "Collect the variable on the side that keeps its coefficient positive — subtract "
            "$4x$ from both sides rather than $6x$:\n"
            "$$-8 \\le 2x + 10$$\n"
            "$$-18 \\le 2x$$\n"
            "$$-9 \\le x$$\n"
            "which reads $x \\ge -9$. Because the coefficient stayed positive, no flip was "
            "ever needed.  \n"
            "Check a value on each side. At $x = 0$: $4(-2) = -8$ and $6(0) + 10 = 10$, and "
            "$-8 \\le 10$ is true. At $x = -10$: $4(-12) = -48$ and $-60 + 10 = -50$, and "
            "$-48 \\le -50$ is false. The boundary is where it should be.  \n"
            "Collecting on the other side works too but forces a division by $-2$ and a flip. "
            "Choosing the side that avoids the flip is free insurance.",
            [
                "4*(0 - 2) <= 6*0 + 10",
                "Not(4*(-10 - 2) <= 6*(-10) + 10)",
                "Eq(4*(-9 - 2), 6*(-9) + 10)",
            ],
        ),
        problem(
            "sat-l5a-w3",
            "A delivery van can carry at most $1{,}200$ kilograms. It is already loaded with "
            "$340$ kilograms of equipment, and each crate weighs $26$ kilograms. What is the "
            "greatest number of crates the van can carry?",
            "**Answer.** $33$.  \n"
            "'At most' is the phrase that makes this an inequality rather than an equation. "
            "With $c$ crates:\n"
            "$$340 + 26c \\le 1200$$\n"
            "$$26c \\le 860$$\n"
            "$$c \\le 33.07\\ldots$$\n"
            "A crate cannot be split, so $c$ must be a whole number, and the greatest whole "
            "number satisfying this is $33$.  \n"
            "Check: $33$ crates weigh $858$ kilograms, giving a total of $1{,}198$ — just "
            "under the limit. $34$ crates weigh $884$, a total of $1{,}224$, which is over.  \n"
            "This is the SAT's favourite inequality context, and its favourite trap is "
            "ROUNDING UP. The algebra gives $33.07$, but rounding to $34$ overloads the van. "
            "For an 'at most' question you always round DOWN, no matter what the decimal is.",
            [
                "340 + 26*33 <= 1200",
                "Not(340 + 26*34 <= 1200)",
                "Eq(340 + 26*33, 1198)",
                "Eq(340 + 26*34, 1224)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l5a-t1",
            "What is the least integer $x$ satisfying $5x + 3 > 18$?",
            "**Answer.** $4$. Subtract $3$: $5x > 15$, so $x > 3$. Dividing by a POSITIVE "
            "number keeps the direction. The least integer strictly greater than $3$ is $4$; "
            "$x = 3$ fails because $18 > 18$ is false.",
            ["5*4 + 3 > 18", "Not(5*3 + 3 > 18)"],
        ),
        problem(
            "sat-l5a-t2",
            "Solve $-2x + 9 \\ge 1$.",
            "**Answer.** $x \\le 4$. Subtract $9$: $-2x \\ge -8$. Divide by $-2$ and FLIP: "
            "$x \\le 4$. Check: at $x = 4$, $-8 + 9 = 1$ and $1 \\ge 1$ is true; at $x = 5$, "
            "$-10 + 9 = -1$, which is not $\\ge 1$.",
            ["-2*4 + 9 >= 1", "Not(-2*5 + 9 >= 1)"],
        ),
        problem(
            "sat-l5a-t3",
            "$$\\frac{x}{3} - 4 < 2$$\n"
            "What is the greatest integer value of $x$ that satisfies the inequality?",
            "**Answer.** $17$. Add $4$: $\\frac{x}{3} < 6$. Multiply by $3$, which is "
            "positive, so no flip: $x < 18$. The greatest integer below $18$ is $17$; $x = 18$ "
            "fails because the inequality is strict.",
            ["Rational(17,3) - 4 < 2", "Not(Rational(18,3) - 4 < 2)"],
        ),
        problem(
            "sat-l5a-t4",
            "A student has $\\$60$ and buys a $\\$16$ notebook plus pens costing $\\$3.50$ "
            "each. What is the greatest number of pens they can buy?",
            "**Answer.** $12$. The constraint is $16 + 3.50p \\le 60$, so $3.50p \\le 44$ and "
            "$p \\le 12.57\\ldots$. Round DOWN: $12$ pens cost $\\$42$, total $\\$58$; $13$ "
            "pens would cost $\\$45.50$, total $\\$61.50$, which is over budget.",
            [
                "16 + Rational(35,10)*12 <= 60",
                "Not(16 + Rational(35,10)*13 <= 60)",
                "Eq(16 + Rational(35,10)*12, 58)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Linear inequalities in one or two variables",
            "beats": [
                "Domain: Algebra — 13 to 15 of the 44 questions on the Math section.",
                "Expect 1 or 2 questions, and at least one dressed as a budget or capacity limit.",
                "Prerequisite: solving a linear equation in one variable.",
                "One extra rule over equations — and it is the rule the whole subtopic tests.",
            ],
        },
        {
            "kind": "teach",
            "title": "Everything works, except one move",
            "body": "Solve an inequality exactly like an equation: clear fractions, distribute, "
                    "collect, divide. Adding and subtracting the same thing on both sides never "
                    "changes the direction of the sign, and neither does multiplying or "
                    "dividing by a POSITIVE number. Multiplying or dividing by a NEGATIVE "
                    "number reverses it. That single exception is what the SAT is testing.",
        },
        {
            "kind": "integerLine",
            "title": "Why the sign flips",
            "teach": "Look at where numbers sit. Three is to the left of five, so 3 is less "
                     "than 5. Multiply both by −1 and they swap places: −3 now sits to the "
                     "RIGHT of −5. Negating reflects the whole line, and reflection reverses "
                     "every comparison on it.",
            "config": {"min": -8, "max": 8, "start": 3},
        },
        {"kind": "worked", "title": "Dividing by a negative", "problemId": "sat-l5a-w1"},
        {
            "kind": "tapQuestion",
            "title": "Does the sign flip?",
            "prompt": "Solving $-4x < 20$, what is the solution set?",
            "options": ["$x > -5$", "$x < -5$", "$x > 5$", "$x < 5$"],
            "correctIndex": 0,
            "explanation": "Dividing both sides by $-4$ reverses the inequality, giving "
                           "$x > -5$. Test it: $x = 0$ gives $0 < 20$, true, and $0$ is indeed "
                           "greater than $-5$. Option B is the same arithmetic without the "
                           "flip, and $x = 0$ disproves it immediately.",
            "check": ["-4*0 < 20", "0 > -5", "Not(0 < -5)"],
        },
        {
            "kind": "tip",
            "title": "Collect on the side that stays positive",
            "body": "You get to choose which side the variable ends up on. Move the variable "
                    "terms toward the side with the LARGER coefficient and the final "
                    "coefficient is positive, so no flip is ever needed. In "
                    "$4x - 8 \\le 6x + 10$, subtracting $4x$ leaves $2x$ on the right and the "
                    "flip never comes up.",
        },
        {"kind": "worked", "title": "Avoiding the flip entirely", "problemId": "sat-l5a-w2"},
        {
            "kind": "teach",
            "title": "At most, at least, and rounding",
            "beats": [
                "'At most', 'no more than', 'a maximum of' → the sign is ≤.",
                "'At least', 'no fewer than', 'a minimum of' → the sign is ≥.",
                "'More than' and 'less than' are STRICT — the boundary value itself fails.",
                "Counting whole objects under an 'at most' limit means rounding DOWN, always.",
            ],
        },
        {"kind": "worked", "title": "A capacity limit", "problemId": "sat-l5a-w3"},
        {"kind": "tryIt", "title": "Your turn: least integer", "problemId": "sat-l5a-t1"},
        {"kind": "tryIt", "title": "Your turn: flip it", "problemId": "sat-l5a-t2"},
        {"kind": "tryIt", "title": "Your turn: clear the fraction", "problemId": "sat-l5a-t3"},
        {"kind": "tryIt", "title": "Your turn: a budget", "problemId": "sat-l5a-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Multiplying or dividing by a negative reverses the inequality sign.",
                "Adding, subtracting, and scaling by a positive never change the direction.",
                "Collect the variable on the side that keeps its coefficient positive.",
                "Strict signs exclude the boundary; the 'or equal to' versions include it.",
                "Counting whole objects under an 'at most' budget always rounds DOWN.",
            ],
        },
    ]

    return lesson(
        slug="solving-linear-inequalities",
        title="Solving Inequalities and the One Move That Flips Them",
        concrete=(
            "A van rated for $1{,}200$ kilograms does not care whether you load exactly that "
            "much — it cares that you do not load more. 'At most' is a different kind of "
            "statement from 'equals', and it needs a different kind of answer: not a number, "
            "but a range of numbers."
        ),
        objective=(
            "Solve a linear inequality in one variable, apply the sign-flip rule correctly, "
            "translate 'at most' and 'at least' into symbols, and round a whole-object answer "
            "the right way."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Linear inequalities in one or two "
            "variables*, in the **Algebra** domain. Expect one or two questions, and at least "
            "one of them will be a budget or capacity limit rather than bare algebra.",
            "Every move that works on an equation works on an inequality — clear fractions, "
            "distribute, collect, divide — with exactly one exception. Multiplying or dividing "
            "both sides by a NEGATIVE number reverses the direction of the sign. The reason is "
            "visible on a number line: $3 < 5$, but multiplying both by $-1$ gives $-3$ and "
            "$-5$, and now $-3 > -5$. Negating reflects the line, and a reflection reverses "
            "every comparison on it.",
            "You can often avoid the flip altogether. Collect the variable terms on whichever "
            "side leaves a positive coefficient, and the dangerous division never happens. It "
            "costs nothing and removes the only rule you can get wrong.",
            "**The test's angle.** The wording carries the sign. 'At most' and 'no more than' "
            "are $\\le$; 'at least' and 'no fewer than' are $\\ge$; 'more than' and 'fewer "
            "than' are strict, so the boundary value itself does not qualify. And when the "
            "answer counts whole objects — crates, pens, tickets — an 'at most' constraint "
            "always rounds DOWN, however close the decimal is to the next integer. Rounding "
            "$33.07$ up to $34$ overloads the van, and $34$ is always an option.",
        ],
        key_idea=(
            "Solve it like an equation, but reverse the sign whenever you multiply or divide "
            "by a negative. Under an 'at most' limit, a count of whole objects rounds down."
        ),
        facts=[
            fact(
                "The flip rule",
                "a < b \\;\\Longrightarrow\\; -a > -b, \\qquad a < b \\text{ and } c < 0 \\;\\Longrightarrow\\; ac > bc",
                "Only multiplication and division by a negative reverse the sign. Addition "
                "never does.",
            ),
            fact(
                "The words and their signs",
                "\\text{at most} \\;\\to\\; \\le, \\qquad \\text{at least} \\;\\to\\; \\ge, \\qquad \\text{more than} \\;\\to\\; >",
                "The 'or equal to' versions include the boundary; the strict versions exclude "
                "it. Checking the boundary value settles which you have.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Forgetting to reverse the sign after dividing by a negative.",
                "Test your answer with a single value. If $x = 0$ satisfies the original and "
                "your solution set excludes it, the sign is backwards.",
            ),
            mistake(
                "Rounding up when a whole-object answer is capped from above.",
                "$c \\le 33.07$ means $33$ crates. The van cannot carry $34$; that answer is "
                "on the option list precisely because rounding up is the instinct.",
            ),
            mistake(
                "Treating 'more than' as including the boundary.",
                "$7 - 3x > -8$ excludes $x = 5$, because $-8 > -8$ is false. Test the boundary "
                "whenever the answer is the greatest or least integer.",
            ),
            mistake(
                "Flipping the sign when adding or subtracting a negative number.",
                "Only multiplication and division by a negative flip it. Subtracting $7$ from "
                "both sides never does.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — inequalities in two variables
# ===========================================================================

def lesson_two_vars():
    worked = [
        problem(
            "sat-l5b-w1",
            "Which of the following points is a solution to the inequality "
            "$y > 2x - 3$?  \n"
            "Consider $(0, 0)$, $(2, 1)$, $(3, 3)$ and $(1, -5)$.",
            "**Answer.** $(0, 0)$.  \n"
            "Testing a point in a two-variable inequality is pure substitution — there is "
            "nothing to solve.\n"
            "At $(0, 0)$: is $0 > 2(0) - 3 = -3$? Yes.  \n"
            "At $(2, 1)$: is $1 > 2(2) - 3 = 1$? No — the inequality is strict, so equality "
            "fails. This point is ON the boundary line, not above it.  \n"
            "At $(3, 3)$: is $3 > 2(3) - 3 = 3$? No, same reason.  \n"
            "At $(1, -5)$: is $-5 > 2(1) - 3 = -1$? No.  \n"
            "Only $(0, 0)$ works.  \n"
            "The picture behind the arithmetic: $y > 2x - 3$ shades everything ABOVE the line "
            "$y = 2x - 3$, with the line itself dashed and excluded. Two of the four points "
            "sit exactly on that dashed line, which is the trap.",
            [
                "0 > 2*0 - 3",
                "Not(1 > 2*2 - 3)",
                "Not(3 > 2*3 - 3)",
                "Not(-5 > 2*1 - 3)",
            ],
        ),
        problem(
            "sat-l5b-w2",
            "A graph in the $xy$-plane shows a solid line through $(0, 4)$ and $(2, 0)$, with "
            "the region BELOW the line shaded. Which inequality does the graph represent?",
            "**Answer.** $y \\le -2x + 4$.  \n"
            "Build the boundary line first. Through $(0, 4)$ and $(2, 0)$ the slope is\n"
            "$$m = \\frac{0 - 4}{2 - 0} = -2$$\n"
            "and the $y$-intercept is $4$, so the boundary is $y = -2x + 4$.  \n"
            "Now the two decisions. The line is SOLID, so the boundary is included and the "
            "sign carries an 'or equal to'. The shading is BELOW, so the inequality is "
            "$y \\le$.  \n"
            "$$y \\le -2x + 4$$\n"
            "Confirm with a test point in the shaded region. The origin sits below the line: "
            "is $0 \\le -2(0) + 4 = 4$? Yes, so the origin is a solution and the shading is on "
            "the right side.  \n"
            "A dashed line would have meant $<$ instead. Solid means included, dashed means "
            "excluded — the same distinction as $\\le$ against $<$.",
            [
                "Eq(Rational(0 - 4, 2 - 0), -2)",
                "Eq(-2*0 + 4, 4)",
                "Eq(-2*2 + 4, 0)",
                "0 <= -2*0 + 4",
            ],
        ),
        problem(
            "sat-l5b-w3",
            "Which of the following is NOT a solution to $3x + 4y \\ge 24$?  \n"
            "Consider $(8, 0)$, $(0, 6)$, $(4, 3)$ and $(2, 4)$.",
            "**Answer.** $(2, 4)$.  \n"
            "Substitute each point into the left side and compare with $24$:\n"
            "$$(8, 0): \\; 3(8) + 4(0) = 24 \\ge 24 \\;\\checkmark$$\n"
            "$$(0, 6): \\; 3(0) + 4(6) = 24 \\ge 24 \\;\\checkmark$$\n"
            "$$(4, 3): \\; 3(4) + 4(3) = 24 \\ge 24 \\;\\checkmark$$\n"
            "$$(2, 4): \\; 3(2) + 4(4) = 22 \\ge 24 \\;\\times$$\n"
            "So $(2, 4)$ is the one that fails.  \n"
            "Notice the structure: the first three points all land exactly ON the boundary "
            "line $3x + 4y = 24$, and because the sign includes equality they all qualify. "
            "Had the inequality been strict, all three would have failed and the question "
            "would have had no single answer — which is a useful check that you read the sign "
            "correctly.",
            [
                "3*8 + 4*0 >= 24",
                "3*0 + 4*6 >= 24",
                "3*4 + 4*3 >= 24",
                "Not(3*2 + 4*4 >= 24)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l5b-t1",
            "Is $(1, 5)$ a solution to $y < 3x + 2$?",
            "**Answer.** No. Substituting gives $5 < 3(1) + 2 = 5$, and $5 < 5$ is false. The "
            "point lies exactly on the boundary line, which a strict inequality excludes.",
            ["Not(5 < 3*1 + 2)", "Eq(3*1 + 2, 5)"],
        ),
        problem(
            "sat-l5b-t2",
            "A dashed line passes through $(0, -1)$ with slope $3$, and the region above it is "
            "shaded. Which inequality does this represent?",
            "**Answer.** $y > 3x - 1$. The boundary is $y = 3x - 1$; dashed means the sign is "
            "strict, and shading above means $y$ is greater. Test $(0, 0)$, which is above the "
            "line: $0 > -1$ is true.",
            ["0 > 3*0 - 1", "Not(-2 > 3*0 - 1)"],
        ),
        problem(
            "sat-l5b-t3",
            "Which point satisfies $2x - y \\le 6$: $(5, 1)$, $(1, -5)$ or $(2, 1)$?",
            "**Answer.** $(2, 1)$. Substitute each into the left side and compare with $6$. "
            "$(5, 1)$ gives $2(5) - 1 = 9$, which is not $\\le 6$. $(1, -5)$ gives "
            "$2(1) - (-5) = 7$ — the double negative ADDS, which is what makes this one fail. "
            "$(2, 1)$ gives $2(2) - 1 = 3 \\le 6$, so it is the solution.",
            ["Not(2*5 - 1 <= 6)", "Not(2*1 - (-5) <= 6)", "2*2 - 1 <= 6"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "An inequality in two variables shades a region",
            "body": "An EQUATION in two variables draws a line — the points where the two sides "
                    "are equal. An INEQUALITY keeps that line as a boundary and then claims one "
                    "whole side of it. The solution set is not a handful of points; it is half "
                    "the plane, infinitely many points, and any single one of them is a "
                    "solution.",
        },
        {
            "kind": "teach",
            "title": "Two decisions make the picture",
            "beats": [
                "Solid or dashed: ≤ and ≥ include the boundary (solid); < and > exclude it (dashed).",
                "Which side: solve for y, then 'greater' shades above and 'less' shades below.",
                "Safer than remembering: test one point, usually the origin.",
                "If the test point satisfies the inequality, shade its side. If not, shade the other.",
            ],
        },
        {
            "kind": "coordinateGrid",
            "title": "On the line, or off it",
            "teach": "Three of these points sit exactly on the line y = 2x − 3 and one does "
                     "not. A strict inequality excludes everything on the boundary, so points "
                     "that look like solutions on a graph can fail on substitution. Tap them "
                     "and check.",
            "config": {"mode": "plot", "min": -8, "max": 8,
                       "points": [{"x": 0, "y": 0, "label": "A"}, {"x": 2, "y": 1, "label": "B"},
                                  {"x": 3, "y": 3, "label": "C"}, {"x": 1, "y": -5, "label": "D"}]},
        },
        {"kind": "worked", "title": "Testing points by substitution", "problemId": "sat-l5b-w1"},
        {
            "kind": "tapQuestion",
            "title": "Solid or dashed?",
            "prompt": "The graph of $y \\ge -x + 2$ has what kind of boundary line, and which "
                      "side is shaded?",
            "options": [
                "Solid, shaded above",
                "Dashed, shaded above",
                "Solid, shaded below",
                "Dashed, shaded below",
            ],
            "correctIndex": 0,
            "explanation": "The 'or equal to' includes the boundary, so the line is solid, and "
                           "'$y$ greater' shades above. Check with the origin: is "
                           "$0 \\ge -0 + 2 = 2$? No — so the origin is NOT in the region, and "
                           "the origin does lie below this line, confirming that the shading "
                           "is above.",
            "check": ["Not(0 >= -0 + 2)", "3 >= -0 + 2"],
        },
        {"kind": "worked", "title": "Reading an inequality off a graph", "problemId": "sat-l5b-w2"},
        {
            "kind": "tip",
            "title": "Test the origin whenever you can",
            "body": "The origin is the easiest point in the plane to substitute — every "
                    "variable term becomes zero. If $(0, 0)$ satisfies the inequality, the "
                    "shaded region is the side containing the origin; if not, it is the other "
                    "side. The only time this fails is when the boundary passes through the "
                    "origin, in which case pick any other convenient point.",
        },
        {"kind": "worked", "title": "Finding the point that fails", "problemId": "sat-l5b-w3"},
        {"kind": "tryIt", "title": "Your turn: on the boundary", "problemId": "sat-l5b-t1"},
        {"kind": "tryIt", "title": "Your turn: from a description", "problemId": "sat-l5b-t2"},
        {"kind": "tryIt", "title": "Your turn: substitute, do not guess", "problemId": "sat-l5b-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "A two-variable inequality shades half the plane, bounded by a line.",
                "Solid line means the boundary is included; dashed means it is excluded.",
                "Solve for y: greater shades above, less shades below.",
                "Testing a point beats remembering which way to shade — use the origin when you can.",
                "A point exactly on the boundary satisfies ≤ and ≥ but never < or >.",
            ],
        },
    ]

    return lesson(
        slug="inequalities-in-two-variables",
        title="Inequalities in Two Variables and the Region They Shade",
        concrete=(
            "A budget of $\\$24$ buys apples at $\\$3$ and bread at $\\$4$. There is no single "
            "correct purchase — there is a whole region of affordable combinations, bounded by "
            "the line where you spend exactly $\\$24$. Two-variable inequalities are how that "
            "region gets written down."
        ),
        objective=(
            "Decide whether a point satisfies a two-variable linear inequality, read an "
            "inequality off a shaded graph, and know when the boundary itself counts."
        ),
        concept=[
            "**Skill card.** Still *Linear inequalities in one or two variables*, in the "
            "**Algebra** domain. These items are usually quick: substitution, or reading a "
            "graph. What makes them cost points is the boundary — whether it is included.",
            "An equation in two variables draws a line. An inequality keeps that line as a "
            "BOUNDARY and claims one entire side of it. The solution set is half the plane, so "
            "checking a proposed point is pure substitution — put both coordinates in and see "
            "whether the resulting numerical claim is true.",
            "Two decisions turn an inequality into a picture. First, is the boundary included? "
            "$\\le$ and $\\ge$ include it and the line is drawn SOLID; $<$ and $>$ exclude it "
            "and the line is DASHED. Second, which side? Solve for $y$: 'greater' shades "
            "above, 'less' shades below. Safer than memorising: test the origin. If $(0, 0)$ "
            "satisfies the inequality, shade the side containing it.",
            "**The test's angle.** Boundary points. The SAT lists points that sit exactly ON "
            "the line, knowing that a student who thinks visually will accept them. With "
            "$3x + 4y \\ge 24$, all of $(8, 0)$, $(0, 6)$ and $(4, 3)$ give exactly $24$ and "
            "all three qualify — but under $>$ every one of them would fail. Read the sign "
            "before you read the points.",
        ],
        key_idea=(
            "A two-variable inequality shades half the plane. Solid boundary means included, "
            "dashed means excluded, and substituting a test point beats remembering which way "
            "to shade."
        ),
        facts=[
            fact(
                "Above and below",
                "y > mx + b \\;\\text{shades above}, \\qquad y < mx + b \\;\\text{shades below}",
                "Solve for $y$ first. If you multiplied by a negative to get there, the sign "
                "flipped and so does the side.",
            ),
            fact(
                "Solid or dashed",
                "\\le, \\ge \\;\\to\\; \\text{solid}, \\qquad <, > \\;\\to\\; \\text{dashed}",
                "The line style says whether points on the boundary are solutions.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Accepting a boundary point under a strict inequality.",
                "$(2, 1)$ gives $1 > 1$, which is false. Under $<$ or $>$ nothing on the line "
                "is a solution.",
            ),
            mistake(
                "Shading the wrong side after rearranging.",
                "If you multiplied both sides by a negative while solving for $y$, the sign "
                "flipped — and so did the side that gets shaded. Test a point to confirm.",
            ),
            mistake(
                "Reading a dashed line as if it were solid.",
                "Dashed means the boundary is excluded, so the answer uses $<$ or $>$, never "
                "$\\le$ or $\\ge$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 3 — systems of inequalities
# ===========================================================================

def lesson_systems():
    worked = [
        problem(
            "sat-l5c-w1",
            "$$y \\ge 2x - 1$$\n$$y \\le -x + 8$$\n"
            "Which of the following points is a solution to the system above: $(0, 9)$, "
            "$(4, 2)$, $(2, 3)$ or $(5, 5)$?",
            "**Answer.** $(2, 3)$.  \n"
            "A solution to a SYSTEM of inequalities must satisfy every inequality at once, so "
            "each point gets tested against both.\n"
            "$(0, 9)$: is $9 \\ge 2(0) - 1 = -1$? Yes. Is $9 \\le -0 + 8 = 8$? No — it "
            "fails the second.  \n"
            "$(4, 2)$: is $2 \\ge 2(4) - 1 = 7$? No — it fails the first.  \n"
            "$(2, 3)$: is $3 \\ge 2(2) - 1 = 3$? Yes, with equality, and $\\ge$ admits it. "
            "Is $3 \\le -2 + 8 = 6$? Yes. Both hold.  \n"
            "$(5, 5)$: is $5 \\ge 2(5) - 1 = 9$? No.  \n"
            "So only $(2, 3)$ qualifies, and it does so with the first inequality holding "
            "EXACTLY — a point sitting on the edge of the region, which the 'or equal to' "
            "lets in. Under a strict $>$ it would have failed.  \n"
            "Geometrically the solution set is the overlap of two half-planes: a wedge. Every "
            "point inside that wedge, and on its solid edges, is a solution.",
            [
                "3 >= 2*2 - 1",
                "3 <= -2 + 8",
                "Not(2 >= 2*4 - 1)",
                "Not(5 >= 2*5 - 1)",
                "Not(9 <= -0 + 8)",
            ],
        ),
        problem(
            "sat-l5c-w2",
            "A student has at most $\\$50$ to spend on notebooks costing $\\$4$ each and pens "
            "costing $\\$2$ each, and needs at least $12$ items in total. Which system of "
            "inequalities models this, where $n$ is notebooks and $p$ is pens?",
            "**Answer.** $4n + 2p \\le 50$ and $n + p \\ge 12$.  \n"
            "Two constraints, two inequalities, and the signs come from the wording.  \n"
            "'At most $\\$50$' caps the MONEY, and the money is $4n + 2p$ because each item is "
            "weighted by its price:\n"
            "$$4n + 2p \\le 50$$\n"
            "'At least $12$ items' sets a floor on the COUNT, and a count weights nothing — "
            "every coefficient is $1$:\n"
            "$$n + p \\ge 12$$\n"
            "The two signs point in opposite directions, which is the whole point: one "
            "constraint is a ceiling, the other a floor, and the solutions live between them.  \n"
            "Check a candidate: $n = 5$, $p = 10$ costs $20 + 20 = 40 \\le 50$ and gives "
            "$15 \\ge 12$ items. Both hold.  \n"
            "Swapping which total goes with which inequality is the standard distractor, and "
            "so is putting the prices on the count equation.",
            [
                "4*5 + 2*10 <= 50",
                "5 + 10 >= 12",
                "Not(4*10 + 2*10 <= 50)",
                "Eq(4*5 + 2*10, 40)",
            ],
        ),
        problem(
            "sat-l5c-w3",
            "$$y < 3x + 2$$\n$$y > 3x - 4$$\n"
            "Describe the solution set of the system above.",
            "**Answer.** The strip strictly between two parallel lines — it is non-empty, and "
            "it contains no boundary points.  \n"
            "Both boundaries have slope $3$, so they are parallel. The first inequality claims "
            "everything BELOW $y = 3x + 2$; the second claims everything ABOVE $y = 3x - 4$. "
            "The overlap is the band between them.  \n"
            "It is non-empty because the lower boundary really is below the upper one: at "
            "$x = 0$ they sit at $-4$ and $2$, so the whole vertical gap between them "
            "qualifies. The origin is in it: $0 < 2$ and $0 > -4$ are both true.  \n"
            "Both signs are strict, so both boundary lines are dashed and no point on either "
            "line is a solution.  \n"
            "Reverse the two constants — below $y = 3x - 4$ and above $y = 3x + 2$ — and the "
            "regions would not overlap at all, giving a system with NO solutions. Parallel "
            "boundaries make that possible, which is why the SAT likes this configuration.",
            [
                "0 < 3*0 + 2",
                "0 > 3*0 - 4",
                "3*0 - 4 < 3*0 + 2",
                "Not(0 < 3*0 - 4)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l5c-t1",
            "Is $(1, 4)$ a solution to the system $y \\ge x + 2$ and $y \\le 2x + 5$?",
            "**Answer.** Yes. Check both: $4 \\ge 1 + 2 = 3$ is true, and "
            "$4 \\le 2(1) + 5 = 7$ is true. Both hold, so the point is in the overlap.",
            ["4 >= 1 + 2", "4 <= 2*1 + 5"],
        ),
        problem(
            "sat-l5c-t2",
            "A van carries crates weighing $30$ kilograms and boxes weighing $12$ kilograms, "
            "with a load limit of $900$ kilograms, and must carry at least $20$ items. Write "
            "the system, using $c$ for crates and $b$ for boxes.",
            "**Answer.** $30c + 12b \\le 900$ and $c + b \\ge 20$. The weight is capped, so "
            "that inequality is $\\le$ and each item is weighted by its mass; the count has a "
            "floor, so that inequality is $\\ge$ with coefficients of $1$. Check $c = 10$, "
            "$b = 20$: the load is $300 + 240 = 540 \\le 900$ and the count is $30 \\ge 20$.",
            ["30*10 + 12*20 <= 900", "10 + 20 >= 20", "Eq(30*10 + 12*20, 540)"],
        ),
        problem(
            "sat-l5c-t3",
            "How many solutions does the system $y > x + 5$ and $y < x + 1$ have?",
            "**Answer.** None. Both boundaries have slope $1$, so they are parallel. The first "
            "claims everything above $y = x + 5$ and the second everything below $y = x + 1$ — "
            "but $x + 1$ is always BELOW $x + 5$, so the two regions never overlap. A point "
            "would need $y$ to exceed $x + 5$ and fall short of $x + 1$ at the same time, "
            "which is impossible.",
            [
                "Eq(simplify((x + 5) - (x + 1)), 4)",
                "Not(0 > 0 + 5)",
                "Eq(4 > 0, True)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "A system means every condition at once",
            "body": "A point solves a system of inequalities only if it satisfies ALL of them. "
                    "Each inequality claims half the plane, so the solution set is the overlap "
                    "of those halves — usually a wedge or a polygon, sometimes a strip, and "
                    "occasionally nothing at all. Testing a candidate point means substituting "
                    "into every inequality, not just the first one that looks relevant.",
        },
        {
            "kind": "systemGraph",
            "title": "Where two half-planes overlap",
            "teach": "The two lines are the boundaries. Each inequality keeps one side; the "
                     "solution set is where the kept sides overlap. Drag the lines until they "
                     "are parallel and watch the overlap become a strip — or vanish entirely.",
            "config": {"m1": 2, "b1": -1, "m2": -1, "b2": 8, "interactive": True, "min": -6, "max": 10},
        },
        {"kind": "worked", "title": "Testing a point against both", "problemId": "sat-l5c-w1"},
        {
            "kind": "teach",
            "title": "Ceilings and floors",
            "beats": [
                "A budget, a weight limit or a capacity is a CEILING — the sign is ≤.",
                "A quota, a minimum order or a required total is a FLOOR — the sign is ≥.",
                "Money and weight equations weight each item by its price or mass.",
                "Count equations weight nothing — every coefficient is 1.",
            ],
        },
        {
            "kind": "tapQuestion",
            "title": "Which sign goes where?",
            "prompt": "A caterer must prepare at least $80$ meals and can spend no more than "
                      "$\\$600$, with meat meals costing $\\$9$ and vegetarian $\\$6$. Which "
                      "pair models it?",
            "options": [
                "$m + v \\ge 80$ and $9m + 6v \\le 600$",
                "$m + v \\le 80$ and $9m + 6v \\ge 600$",
                "$9m + 6v \\ge 80$ and $m + v \\le 600$",
                "$m + v \\ge 80$ and $9m + 6v \\ge 600$",
            ],
            "correctIndex": 0,
            "explanation": "'At least $80$ meals' is a floor on the COUNT, so coefficients of "
                           "$1$ and a $\\ge$. 'No more than $\\$600$' is a ceiling on the "
                           "MONEY, so each meal is weighted by its price and the sign is "
                           "$\\le$. Check $m = 40$, $v = 40$: $80 \\ge 80$ and "
                           "$360 + 240 = 600 \\le 600$, both exactly on the boundary.",
            "check": ["40 + 40 >= 80", "9*40 + 6*40 <= 600", "Eq(9*40 + 6*40, 600)"],
        },
        {"kind": "worked", "title": "Building a constraint system", "problemId": "sat-l5c-w2"},
        {
            "kind": "tip",
            "title": "Parallel boundaries are the interesting case",
            "body": "When the two boundary lines have the same slope, the overlap is either an "
                    "infinite strip between them or nothing at all — and which one depends "
                    "entirely on the order of the constants. Check by testing the origin, or "
                    "by asking whether the lower boundary really is below the upper one at any "
                    "single value of $x$.",
        },
        {"kind": "worked", "title": "A strip between parallel lines", "problemId": "sat-l5c-w3"},
        {"kind": "tryIt", "title": "Your turn: check both", "problemId": "sat-l5c-t1"},
        {"kind": "tryIt", "title": "Your turn: write the system", "problemId": "sat-l5c-t2"},
        {"kind": "tryIt", "title": "Your turn: an empty overlap", "problemId": "sat-l5c-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "A solution must satisfy EVERY inequality in the system — test all of them.",
                "The solution set is the overlap of the half-planes, and it can be empty.",
                "A budget or capacity gives ≤; a quota or minimum gives ≥.",
                "Money and weight constraints weight each item; count constraints do not.",
                "Parallel boundaries give either an infinite strip or no solutions at all.",
            ],
        },
    ]

    return lesson(
        slug="systems-of-inequalities",
        title="Systems of Inequalities and Real Constraints",
        concrete=(
            "A caterer must make at least $80$ meals and cannot spend more than $\\$600$. "
            "Neither rule alone decides the menu; together they carve out a region of workable "
            "plans, and everything inside that region is a valid answer."
        ),
        objective=(
            "Test a point against a system of linear inequalities, translate a pair of "
            "real-world constraints into a system, and recognise when the solution region is "
            "empty."
        ),
        concept=[
            "**Skill card.** Still *Linear inequalities in one or two variables*, in the "
            "**Algebra** domain. Constraint-system items are common on the digital SAT because "
            "they test modelling and sign choice in one question, with almost no computation.",
            "A point solves a system only if it satisfies EVERY inequality. Each inequality "
            "keeps half the plane, so the solution set is the overlap of those halves — "
            "usually a wedge or a polygon, sometimes an infinite strip, and occasionally "
            "nothing at all. Testing a candidate means substituting into all of them, not just "
            "the first.",
            "The modelling questions follow the same count-and-weight skeleton as systems of "
            "equations, with signs attached. A budget, a weight limit or a capacity is a "
            "CEILING and gives $\\le$; a quota, a minimum order or a required total is a FLOOR "
            "and gives $\\ge$. Money and weight constraints weight each item by its price or "
            "mass; count constraints weight nothing, so every coefficient is $1$.",
            "**The test's angle.** Parallel boundaries. When both inequalities have the same "
            "slope, the overlap is either an infinite strip between the two lines or the empty "
            "set, depending only on which constant is larger. $y < 3x + 2$ with $y > 3x - 4$ "
            "gives a band; reverse the constants and no point can satisfy both. Testing the "
            "origin settles it in one substitution.",
        ],
        key_idea=(
            "The solution set of a system of inequalities is the overlap of half-planes. "
            "Ceilings give $\\le$, floors give $\\ge$, and parallel boundaries mean the "
            "overlap is a strip or nothing."
        ),
        facts=[
            fact(
                "The constraint pair",
                "\\begin{cases} p\\,x + q\\,y \\le B \\\\ x + y \\ge N \\end{cases}",
                "A budget $B$ weighting each item by its price, and a minimum count $N$ "
                "weighting nothing. This models most SAT constraint questions.",
            ),
            fact(
                "Parallel boundaries",
                "y < mx + b_1 \\;\\text{and}\\; y > mx + b_2 \\;\\text{is non-empty} \\iff b_2 < b_1",
                "Same slope means a strip or nothing, decided entirely by the order of the two "
                "constants.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Checking a candidate point against only one of the inequalities.",
                "Every inequality must hold. The SAT's distractors are points that satisfy one "
                "and fail another.",
            ),
            mistake(
                "Attaching the prices to the count constraint.",
                "The count inequality has coefficients of $1$; the money inequality carries the "
                "prices. Swapping them is the standard modelling distractor.",
            ),
            mistake(
                "Assuming a system of inequalities always has solutions.",
                "Parallel boundaries pointing away from each other give an empty solution set. "
                "Test the origin to check.",
            ),
            mistake(
                "Using $<$ where the words say 'at most'.",
                "'At most' includes the boundary, so it is $\\le$. 'Fewer than' excludes it.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Unit assembly
# ===========================================================================

PRACTICE = [
    problem(
        "sat-l5-p01",
        "What is the greatest integer satisfying $2x + 5 < 17$?",
        "**Answer.** $5$. Subtract $5$: $2x < 12$, so $x < 6$. The greatest integer strictly "
        "below $6$ is $5$.",
        ["2*5 + 5 < 17", "Not(2*6 + 5 < 17)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l5-p02",
        "Solve $-5x \\ge 35$.",
        "**Answer.** $x \\le -7$. Dividing by $-5$ reverses the sign. Check: $x = -7$ gives "
        "$35 \\ge 35$, true; $x = -6$ gives $30 \\ge 35$, false.",
        ["-5*(-7) >= 35", "Not(-5*(-6) >= 35)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l5-p03",
        "Which of these is a solution to $y \\le 4x - 2$: $(0, 0)$ or $(3, 5)$?",
        "**Answer.** $(3, 5)$. At $(3, 5)$: $5 \\le 4(3) - 2 = 10$, true. At $(0, 0)$: "
        "$0 \\le -2$, false.",
        ["5 <= 4*3 - 2", "Not(0 <= 4*0 - 2)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l5-p04",
        "$$3(x + 4) > 5x - 2$$\n"
        "What is the greatest integer value of $x$ that satisfies the inequality?",
        "**Answer.** $6$. Distribute: $3x + 12 > 5x - 2$. Subtract $3x$: $12 > 2x - 2$, so "
        "$14 > 2x$ and $x < 7$. The greatest integer below $7$ is $6$; at $x = 7$ both sides "
        "equal $33$, and the inequality is strict.",
        ["3*(6 + 4) > 5*6 - 2", "Eq(3*(7 + 4), 5*7 - 2)", "Not(3*(7 + 4) > 5*7 - 2)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-p05",
        "A lift can carry at most $680$ kilograms. Six people weighing a total of $410$ "
        "kilograms are inside, and boxes weigh $18$ kilograms each. What is the greatest "
        "number of boxes that can be added?",
        "**Answer.** $15$. The constraint is $410 + 18b \\le 680$, so $18b \\le 270$ and "
        "$b \\le 15$ exactly. Fifteen boxes bring the total to exactly $680$, which 'at most' "
        "permits; sixteen would give $698$.",
        ["410 + 18*15 <= 680", "Eq(410 + 18*15, 680)", "Not(410 + 18*16 <= 680)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-p06",
        "A solid line passes through $(0, -2)$ and $(4, 6)$, with the region below it shaded. "
        "Which inequality does the graph show?",
        "**Answer.** $y \\le 2x - 2$. The slope is $\\frac{6 - (-2)}{4} = 2$ and the intercept "
        "is $-2$. Solid means the boundary is included, and shading below means $y$ is less "
        "than or equal to the boundary value. Pick a test point that is genuinely in the "
        "shaded region — $(0, -5)$ sits well below the line — and check: $-5 \\le -2$, true. "
        "The origin is a poor choice here because it lies ABOVE this line, and testing it "
        "gives $0 \\le -2$, false, which correctly reports that the origin is outside the "
        "region.",
        [
            "Eq(Rational(6 - (-2), 4 - 0), 2)",
            "-5 <= 2*0 - 2",
            "Not(0 <= 2*0 - 2)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-p07",
        "$$y > -2x + 6$$\n$$y > x - 3$$\n"
        "Is $(4, 4)$ a solution to the system?",
        "**Answer.** Yes. Check both: $4 > -8 + 6 = -2$ is true, and $4 > 4 - 3 = 1$ is true. "
        "Both strict inequalities hold, so the point lies strictly inside the overlap.",
        ["4 > -2*4 + 6", "4 > 4 - 3"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-p08",
        "A shop must sell at least $150$ items and wants revenue of no more than $\\$1{,}000$ "
        "in a promotion, with mugs at $\\$8$ and keyrings at $\\$3$. Which system models this?",
        "**Answer.** $m + k \\ge 150$ and $8m + 3k \\le 1000$. The count has a floor, so "
        "coefficients of $1$ and a $\\ge$; the money has a ceiling, so prices as coefficients "
        "and a $\\le$. Check $m = 50$, $k = 150$: $200 \\ge 150$ and "
        "$400 + 450 = 850 \\le 1000$.",
        ["50 + 150 >= 150", "8*50 + 3*150 <= 1000", "Eq(8*50 + 3*150, 850)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-p09",
        "$$\\frac{2x - 1}{5} \\ge 3$$\n"
        "What is the least integer value of $x$ satisfying the inequality?",
        "**Answer.** $8$. Multiply both sides by $5$, which is positive so no flip: "
        "$2x - 1 \\ge 15$. Then $2x \\ge 16$ and $x \\ge 8$. At $x = 8$ the left side is "
        "exactly $3$, which the $\\ge$ admits.",
        ["Rational(2*8 - 1, 5) >= 3", "Not(Rational(2*7 - 1, 5) >= 3)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-p10",
        "How many solutions does the system $y \\le 2x - 5$ and $y \\ge 2x + 1$ have?",
        "**Answer.** None. Both boundaries have slope $2$, but $2x - 5$ is always below "
        "$2x + 1$. A point would have to be at or below the lower line and at or above the "
        "upper one simultaneously, which is impossible.",
        ["2*0 - 5 < 2*0 + 1", "Not(And(0 <= 2*0 - 5, 0 >= 2*0 + 1))"],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l5-p11",
        "A tank holds at least $200$ litres and at most $350$ litres. It currently holds $80$ "
        "litres and is filled at $15$ litres per minute. For what whole numbers of minutes $t$ "
        "is the volume within the allowed range?",
        "**Answer.** $8 \\le t \\le 18$. The volume is $80 + 15t$. The lower bound gives "
        "$80 + 15t \\ge 200$, so $t \\ge 8$; the upper gives $80 + 15t \\le 350$, so "
        "$t \\le 18$. At $t = 8$ the volume is exactly $200$ and at $t = 18$ exactly $350$, "
        "both allowed.",
        [
            "Eq(80 + 15*8, 200)",
            "Eq(80 + 15*18, 350)",
            "Not(80 + 15*7 >= 200)",
            "Not(80 + 15*19 <= 350)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l5-p12",
        "If $-3 < 2x + 1 \\le 9$, what is the range of $x$?",
        "**Answer.** $-2 < x \\le 4$. Work on all three parts at once. Subtract $1$: "
        "$-4 < 2x \\le 8$. Divide by $2$, which is positive so nothing flips: "
        "$-2 < x \\le 4$. The left end stays strict and the right end stays inclusive — each "
        "sign keeps its own character.",
        [
            "-3 < 2*4 + 1",
            "2*4 + 1 <= 9",
            "Not(2*(-2) + 1 > -3)",
        ],
        badges=_b("Hard"),
    ),
]

TEST = [
    problem(
        "sat-l5-x01",
        "What is the greatest integer satisfying $4x - 7 < 21$?",
        "**Answer.** $6$. Add $7$: $4x < 28$, so $x < 7$, and the greatest integer below $7$ "
        "is $6$.",
        ["4*6 - 7 < 21", "Not(4*7 - 7 < 21)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l5-x02",
        "Solve $8 - 2x \\le 14$.",
        "**Answer.** $x \\ge -3$. Subtract $8$: $-2x \\le 6$. Divide by $-2$ and flip: "
        "$x \\ge -3$. Check $x = -3$: $8 + 6 = 14 \\le 14$, true; $x = -4$ gives $16$, false.",
        ["8 - 2*(-3) <= 14", "Not(8 - 2*(-4) <= 14)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l5-x03",
        "Which point satisfies $2x + 3y < 12$: $(3, 2)$ or $(0, 4)$?",
        "**Answer.** Neither. $(3, 2)$ gives $6 + 6 = 12$, and $12 < 12$ is false. $(0, 4)$ "
        "gives $0 + 12 = 12$, also false. Both lie exactly on the boundary line, which a "
        "strict inequality excludes. A point such as $(1, 1)$, giving $5 < 12$, does satisfy "
        "it.",
        ["Not(2*3 + 3*2 < 12)", "Not(2*0 + 3*4 < 12)", "2*1 + 3*1 < 12"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-x04",
        "A caterer has $\\$450$ and buys trays costing $\\$28$ each. A fixed delivery fee of "
        "$\\$60$ applies. What is the greatest number of trays they can buy?",
        "**Answer.** $13$. The constraint is $60 + 28t \\le 450$, so $28t \\le 390$ and "
        "$t \\le 13.9\\ldots$. Round DOWN: $13$ trays cost $364$, a total of $424$; $14$ trays "
        "would total $452$, over budget.",
        ["60 + 28*13 <= 450", "Not(60 + 28*14 <= 450)", "Eq(60 + 28*13, 424)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-x05",
        "$$y \\ge x + 1$$\n$$y \\le 3x - 3$$\n"
        "Is $(3, 5)$ a solution to the system?",
        "**Answer.** Yes. Check both: $5 \\ge 3 + 1 = 4$ is true, and $5 \\le 9 - 3 = 6$ is "
        "true. Both hold, so the point is in the overlap.",
        ["5 >= 3 + 1", "5 <= 3*3 - 3"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-x06",
        "A dashed line passes through $(0, 5)$ with slope $-1$, and the region below it is "
        "shaded. Which inequality does the graph represent?",
        "**Answer.** $y < -x + 5$. The boundary is $y = -x + 5$; dashed means strict, and "
        "shading below means $y$ is less. Test the origin, which lies below: $0 < 5$ is true.",
        ["0 < -0 + 5", "Not(6 < -0 + 5)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l5-x07",
        "A factory must produce at least $500$ units and its machines can run no more than "
        "$40$ hours in total. Machine A makes $20$ units per hour and machine B makes $15$. "
        "Which system models this, with $a$ and $b$ the hours each machine runs?",
        "**Answer.** $20a + 15b \\ge 500$ and $a + b \\le 40$. The output has a floor, so it "
        "is $\\ge$ and each hour is weighted by that machine's rate. The hours have a ceiling, "
        "so it is $\\le$ with coefficients of $1$. Check $a = 20$, $b = 10$: "
        "$400 + 150 = 550 \\ge 500$ and $30 \\le 40$.",
        ["20*20 + 15*10 >= 500", "20 + 10 <= 40", "Eq(20*20 + 15*10, 550)"],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l5-x08",
        "If $5 \\le 3x - 4 < 14$, what is the range of $x$?",
        "**Answer.** $3 \\le x < 6$. Add $4$ throughout: $9 \\le 3x < 18$. Divide by $3$: "
        "$3 \\le x < 6$. Each end keeps its own sign — the left stays inclusive, the right "
        "stays strict — so $x = 3$ qualifies and $x = 6$ does not.",
        ["5 <= 3*3 - 4", "3*3 - 4 < 14", "Not(3*6 - 4 < 14)"],
        badges=_b("Hard"),
    ),
]


def main():
    lessons = [lesson_solving(), lesson_two_vars(), lesson_systems()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Linear Inequalities in One or Two Variables",
        5,
        "The one rule that separates inequalities from equations, the half-plane a two-variable "
        "inequality shades, and the budget-and-quota systems the test builds its constraint "
        "questions from — including when to round down.",
        "Solving equations (Unit 1) and graphing lines (Unit 2) — an inequality is a line plus "
        "a side.",
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
