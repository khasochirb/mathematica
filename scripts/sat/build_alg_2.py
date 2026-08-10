#!/usr/bin/env python3
"""SAT Math — Algebra, Unit 2: Linear equations in two variables.

Builds data/genmath/sat/linear-equations-two-variables.json: the line itself —
slope, intercepts, the three forms the SAT writes a line in, and the contexts
it dresses them up as. Three lessons.

Run: python3 scripts/sat/build_alg_2.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "linear-equations-two-variables"
TAG = {"text": "sat-linear-eq-two-var", "mono": True}


def _b(level):
    return [TAG, {"text": level}]


# ===========================================================================
# Lesson 1 — slope and intercepts
# ===========================================================================

def lesson_slope():
    worked = [
        problem(
            "sat-l2a-w1",
            "A line in the $xy$-plane passes through the points $(-2, 7)$ and $(4, -5)$. "
            "What is the slope of the line?",
            "**Answer.** $-2$.  \n"
            "Slope is the change in $y$ divided by the change in $x$, taken in the same "
            "order for both:\n"
            "$$m = \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{-5 - 7}{4 - (-2)} = \\frac{-12}{6} = -2$$\n"
            "The order of the points does not matter as long as you are consistent. Taking "
            "them the other way round gives $\\frac{7 - (-5)}{-2 - 4} = \\frac{12}{-6} = -2$, "
            "the same value.  \n"
            "Subtracting in opposite orders — $y_2 - y_1$ over $x_1 - x_2$ — flips the sign and "
            "produces $2$, which is always a listed option.",
            [
                "Eq(Rational(-5 - 7, 4 - (-2)), -2)",
                "Eq(Rational(7 - (-5), -2 - 4), -2)",
                "Eq(Rational(-5 - 7, -2 - 4), 2)",
            ],
        ),
        problem(
            "sat-l2a-w2",
            "$$4x + 3y = 24$$\n"
            "What is the $y$-intercept of the graph of the equation above in the $xy$-plane?",
            "**Answer.** $(0, 8)$.  \n"
            "The $y$-intercept is where the graph crosses the $y$-axis, and every point on "
            "the $y$-axis has $x = 0$. Substitute:\n"
            "$$4(0) + 3y = 24$$\n"
            "$$3y = 24$$\n"
            "$$y = 8$$\n"
            "So the intercept is $(0, 8)$.  \n"
            "The same substitution with $y = 0$ gives the $x$-intercept: $4x = 24$, so "
            "$x = 6$ and the point is $(6, 0)$. Mixing the two up is the standard error here, "
            "and both $6$ and $8$ appear in the options.  \n"
            "Solving for $y$ instead gives $y = -\\frac{4}{3}x + 8$, which shows the intercept "
            "$8$ and the slope $-\\frac{4}{3}$ in one line.",
            [
                "Eq(4*0 + 3*8, 24)",
                "Eq(4*6 + 3*0, 24)",
                "Eq(solve(Eq(4*x + 3*y, 24), y)[0], -Rational(4,3)*x + 8)",
            ],
        ),
        problem(
            "sat-l2a-w3",
            "Line $\\ell$ has slope $\\tfrac{3}{5}$ and passes through the point $(10, 1)$. "
            "Which equation defines line $\\ell$?",
            "**Answer.** $y = \\dfrac{3}{5}x - 5$.  \n"
            "Point-slope form is built for exactly this information:\n"
            "$$y - y_1 = m(x - x_1)$$\n"
            "$$y - 1 = \\frac{3}{5}(x - 10)$$\n"
            "Distribute the $\\frac{3}{5}$, remembering it multiplies BOTH terms:\n"
            "$$y - 1 = \\frac{3}{5}x - 6$$\n"
            "$$y = \\frac{3}{5}x - 5$$\n"
            "Check by substituting the point: $\\frac{3}{5}(10) - 5 = 6 - 5 = 1$, which "
            "matches the given $y$-value.  \n"
            "The fast SAT route skips the algebra entirely: every option has the same slope "
            "in these items, so plug $x = 10$ into each and keep the one that returns $1$.",
            [
                "Eq(Rational(3,5)*10 - 5, 1)",
                "Eq(expand(1 + Rational(3,5)*(x - 10)), Rational(3,5)*x - 5)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l2a-t1",
            "What is the slope of the line through $(3, -1)$ and $(7, 11)$?",
            "**Answer.** $3$.  \n"
            "$m = \\dfrac{11 - (-1)}{7 - 3} = \\dfrac{12}{4} = 3$. The subtraction "
            "$11 - (-1)$ is an addition — dropping the double negative gives $\\frac{10}{4}$, "
            "a listed distractor.",
            ["Eq(Rational(11 - (-1), 7 - 3), 3)"],
        ),
        problem(
            "sat-l2a-t2",
            "$$5x - 2y = 20$$\n"
            "What is the $x$-intercept of the graph of the equation above?",
            "**Answer.** $(4, 0)$.  \n"
            "Set $y = 0$: $5x = 20$, so $x = 4$. The $x$-intercept is $(4, 0)$. "
            "Setting $x = 0$ instead gives $-2y = 20$ and $y = -10$, the $y$-intercept.",
            ["Eq(5*4 - 2*0, 20)", "Eq(5*0 - 2*(-10), 20)"],
        ),
        problem(
            "sat-l2a-t3",
            "A line passes through $(0, -3)$ with slope $\\tfrac{1}{2}$. What is the value of "
            "$y$ when $x = 8$?",
            "**Answer.** $1$.  \n"
            "The point given IS the $y$-intercept, so the line is $y = \\frac{1}{2}x - 3$ with "
            "no algebra needed. At $x = 8$: $y = 4 - 3 = 1$.",
            ["Eq(Rational(1,2)*8 - 3, 1)"],
        ),
        problem(
            "sat-l2a-t4",
            "In the $xy$-plane, line $k$ has slope $-4$ and passes through $(2, 5)$. What is "
            "the $y$-coordinate of the point on line $k$ whose $x$-coordinate is $2.5$?",
            "**Answer.** $3$.  \n"
            "Slope $-4$ means $y$ falls by $4$ for every $1$ that $x$ rises. Here $x$ rises by "
            "only $0.5$, so $y$ falls by $4 \\times 0.5 = 2$: from $5$ down to $3$.  \n"
            "The equation route agrees: $y = 5 - 4(x - 2)$, so at $x = 2.5$, "
            "$y = 5 - 4(0.5) = 3$.",
            ["Eq(5 - 4*(Rational(5,2) - 2), 3)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Linear equations in two variables",
            "beats": [
                "Domain: Algebra — 13 to 15 of the 44 questions on the Math section.",
                "This subtopic and Linear functions together are the most-tested pair on the test.",
                "Prerequisite: solving a linear equation in one variable.",
                "Everything here is one idea in three costumes — slope, intercept, and a point.",
            ],
        },
        {
            "kind": "teach",
            "title": "Slope is a rate, not a decoration",
            "body": "The slope of a line is how much $y$ changes for every $1$ that $x$ changes. "
                    "That is why every real-world linear question has its rate sitting in the "
                    "slope: dollars per hour, litres per minute, degrees per kilometre. "
                    "Positive slope rises left to right, negative falls, zero is flat, and a "
                    "vertical line has no slope at all because $x$ never changes.",
        },
        {
            "kind": "coordinateGrid",
            "title": "Plot two points, read the slope",
            "teach": "Tap two lattice points and count the rise and the run between them. The "
                     "slope is rise over run — and the count is the same whichever point you "
                     "start from, as long as you go the same direction for both.",
            "config": {"mode": "plot", "min": -8, "max": 8,
                       "points": [{"x": -2, "y": 7, "label": "A"}, {"x": 4, "y": -5, "label": "B"}]},
        },
        {"kind": "worked", "title": "Slope from two points", "problemId": "sat-l2a-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which sign?",
            "prompt": "A line passes through $(1, 6)$ and $(5, 2)$. What is its slope?",
            "options": ["$-1$", "$1$", "$-4$", "$\\dfrac{1}{4}$"],
            "correctIndex": 0,
            "explanation": "$m = \\frac{2 - 6}{5 - 1} = \\frac{-4}{4} = -1$. As $x$ grows the "
                           "$y$-value falls, so the slope must be negative — that alone rules "
                           "out two of the four options before any arithmetic.",
            "check": ["Eq(Rational(2 - 6, 5 - 1), -1)", "2 < 6", "5 > 1"],
        },
        {
            "kind": "teach",
            "title": "Intercepts: set the other one to zero",
            "beats": [
                "The y-intercept is where the line crosses the vertical axis, so x is 0 there.",
                "The x-intercept is where it crosses the horizontal axis, so y is 0 there.",
                "Substituting zero for one variable and solving is the whole method.",
                "In y = mx + b the number b IS the y-intercept, with no work at all.",
            ],
        },
        {"kind": "worked", "title": "Finding an intercept", "problemId": "sat-l2a-w2"},
        {
            "kind": "tip",
            "title": "Plug the point in, do not solve",
            "body": "When the options are four equations and the question gives you a point, "
                    "substitute the point into each option and keep the one that comes out "
                    "true. On a line question this is usually faster than deriving the "
                    "equation, and it cannot go wrong the way a distributed fraction can.",
        },
        {"kind": "worked", "title": "Building the equation from a point", "problemId": "sat-l2a-w3"},
        {"kind": "tryIt", "title": "Your turn: slope from two points", "problemId": "sat-l2a-t1"},
        {"kind": "tryIt", "title": "Your turn: which intercept?", "problemId": "sat-l2a-t2"},
        {"kind": "tryIt", "title": "Your turn: the intercept is given", "problemId": "sat-l2a-t3"},
        {"kind": "tryIt", "title": "Your turn: a fractional step", "problemId": "sat-l2a-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Slope is change in y over change in x, subtracted in the same order on top and bottom.",
                "For the y-intercept set x to zero; for the x-intercept set y to zero.",
                "In slope-intercept form the constant term is the y-intercept, free of charge.",
                "Point-slope form turns a point and a slope into an equation in one line.",
                "When the options are equations and you have a point, substitute rather than derive.",
            ],
        },
    ]

    return lesson(
        slug="slope-and-intercepts",
        title="Slope, Intercepts and the Line They Describe",
        concrete=(
            "A hot-air balloon at $1{,}200$ metres descends $80$ metres a minute. Two numbers "
            "describe the whole flight: where it started and how fast it drops. Those two "
            "numbers are the intercept and the slope, and once you have them you can answer "
            "any question about the balloon without ever drawing it."
        ),
        objective=(
            "Find the slope of a line from two points, an equation or a description; find both "
            "intercepts; and build the equation of a line from a point and a slope."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Linear equations in two variables*, "
            "in the **Algebra** domain. Together with *Linear functions* it is the most "
            "heavily tested pair on the Math section. The algebra is short; what the test "
            "grades is whether you can move between a graph, a table, an equation and a "
            "sentence without losing your footing.",
            "Slope is a rate: the change in $y$ for every $1$ that $x$ increases. Between two "
            "points it is $\\frac{y_2 - y_1}{x_2 - x_1}$ — and the only rule is to subtract in "
            "the SAME order on top and bottom. Reversing one of them flips the sign, which is "
            "why the negated slope is on every option list.",
            "An intercept is where the line meets an axis, and every point on an axis has a "
            "zero coordinate. Set $x = 0$ and solve for $y$ to get the $y$-intercept; set "
            "$y = 0$ and solve for $x$ to get the $x$-intercept. In the form $y = mx + b$ you "
            "do not even have to do that — $b$ is the $y$-intercept by construction.",
            "**The test's angle.** Two patterns dominate. The first gives you a point and a "
            "slope and asks for the equation: point-slope form, $y - y_1 = m(x - x_1)$, is "
            "built for it. The second gives you four candidate equations and a point, and the "
            "fastest route is to substitute the point into each option rather than derive "
            "anything — Bluebook's Desmos panel makes this almost instant.",
        ],
        key_idea=(
            "A line is pinned down by any two of: a slope, a point, an intercept. Slope is "
            "rise over run subtracted in a consistent order, and an intercept is what you get "
            "when the other coordinate is zero."
        ),
        facts=[
            fact(
                "Slope from two points",
                "m = \\frac{y_2 - y_1}{x_2 - x_1}",
                "Subtract in the same order on top and bottom. Swapping one order flips the "
                "sign of the answer.",
            ),
            fact(
                "Slope-intercept form",
                "y = mx + b",
                "$m$ is the slope, $b$ is the $y$-intercept. Getting an equation into this "
                "form makes both readable at a glance.",
            ),
            fact(
                "Point-slope form",
                "y - y_1 = m(x - x_1)",
                "The fastest way to write a line through $(x_1, y_1)$ with slope $m$. "
                "Distribute carefully — the slope multiplies both terms in the bracket.",
            ),
            fact(
                "Standard form",
                "Ax + By = C \\;\\Longrightarrow\\; m = -\\frac{A}{B}",
                "Handy when the SAT gives an equation in standard form and asks only for the "
                "slope. Note the minus sign.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Subtracting the coordinates in opposite orders in the slope formula.",
                "If the numerator is $y_2 - y_1$, the denominator must be $x_2 - x_1$. The "
                "mismatched version gives the negative of the true slope.",
            ),
            mistake(
                "Reporting the $x$-intercept when the question asked for the $y$-intercept.",
                "The $y$-intercept has $x = 0$; the $x$-intercept has $y = 0$. Write down "
                "which one you are setting to zero before you substitute.",
            ),
            mistake(
                "Reading the slope of $Ax + By = C$ as $\\frac{A}{B}$.",
                "Solving for $y$ gives $y = -\\frac{A}{B}x + \\frac{C}{B}$. The slope carries a "
                "minus sign.",
            ),
            mistake(
                "Distributing the slope over only the variable in point-slope form.",
                "In $y - 1 = \\frac{3}{5}(x - 10)$ the $\\frac{3}{5}$ multiplies the $-10$ too, "
                "giving $-6$, not $-10$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — parallel, perpendicular, and the three forms
# ===========================================================================

def lesson_forms():
    worked = [
        problem(
            "sat-l2b-w1",
            "Line $m$ is defined by $2x + 5y = 15$. Line $n$ is perpendicular to line $m$ and "
            "passes through the origin. Which equation defines line $n$?",
            "**Answer.** $y = \\dfrac{5}{2}x$.  \n"
            "First get the slope of line $m$ by solving for $y$:\n"
            "$$5y = -2x + 15$$\n"
            "$$y = -\\frac{2}{5}x + 3$$\n"
            "So $m$ has slope $-\\frac{2}{5}$. Perpendicular slopes are negative reciprocals: "
            "flip the fraction AND change the sign.\n"
            "$$m_n = -\\frac{1}{-2/5} = \\frac{5}{2}$$\n"
            "Line $n$ passes through the origin, so its $y$-intercept is $0$:\n"
            "$$y = \\frac{5}{2}x$$\n"
            "Check the perpendicularity the way the SAT checks it: the product of the two "
            "slopes is $-\\frac{2}{5} \\times \\frac{5}{2} = -1$.  \n"
            "Only flipping (giving $-\\frac{5}{2}$) or only negating (giving $\\frac{2}{5}$) "
            "each produce a listed option.",
            [
                "Eq(solve(Eq(2*x + 5*y, 15), y)[0], -Rational(2,5)*x + 3)",
                "Eq(-Rational(2,5)*Rational(5,2), -1)",
            ],
        ),
        problem(
            "sat-l2b-w2",
            "In the $xy$-plane, the graph of $y = 3x + 7$ is parallel to the graph of "
            "$y = ax + 2$. What is the value of $a$?",
            "**Answer.** $3$.  \n"
            "Parallel lines never meet, and two lines never meet exactly when they climb at "
            "the same rate — that is, when their slopes are equal:\n"
            "$$a = 3$$\n"
            "The different constant terms are what make them two distinct lines rather than "
            "one line written twice. If the constants also matched, the two equations would "
            "describe the same line, which is not what 'parallel' means on the SAT.",
            ["Eq(3, 3)", "Ne(7, 2)"],
        ),
        problem(
            "sat-l2b-w3",
            "The table below gives three points on a line in the $xy$-plane.\n\n"
            "| $x$ | $y$ |\n| --- | --- |\n| $1$ | $9$ |\n| $4$ | $3$ |\n| $7$ | $-3$ |\n\n"
            "Which equation represents the line?",
            "**Answer.** $y = -2x + 11$.  \n"
            "Read the slope straight off the table. From the first row to the second, $x$ "
            "rises by $3$ and $y$ falls by $6$:\n"
            "$$m = \\frac{3 - 9}{4 - 1} = \\frac{-6}{3} = -2$$\n"
            "Confirm with the next pair: $\\frac{-3 - 3}{7 - 4} = \\frac{-6}{3} = -2$. Equal "
            "steps in $x$ giving equal steps in $y$ is what makes the data linear at all.\n"
            "Now use any row in $y = mx + b$. Taking $(1, 9)$:\n"
            "$$9 = -2(1) + b \\;\\Longrightarrow\\; b = 11$$\n"
            "So $y = -2x + 11$. Check the last row: $-2(7) + 11 = -3$.  \n"
            "The table never shows $x = 0$, so $11$ has to be computed — reading $9$ off the "
            "first row as the intercept is the trap.",
            [
                "Eq(Rational(3 - 9, 4 - 1), -2)",
                "Eq(Rational(-3 - 3, 7 - 4), -2)",
                "Eq(-2*1 + 11, 9)",
                "Eq(-2*7 + 11, -3)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l2b-t1",
            "Line $p$ has slope $-\\tfrac{3}{4}$. What is the slope of a line perpendicular "
            "to line $p$?",
            "**Answer.** $\\dfrac{4}{3}$.  \n"
            "Flip the fraction and change the sign: $-\\frac{3}{4} \\to \\frac{4}{3}$. Check: "
            "$-\\frac{3}{4} \\times \\frac{4}{3} = -1$.",
            ["Eq(-Rational(3,4)*Rational(4,3), -1)"],
        ),
        problem(
            "sat-l2b-t2",
            "$$3x - y = 8$$\n"
            "Which equation defines a line parallel to the graph above and passing through "
            "$(0, -1)$?",
            "**Answer.** $y = 3x - 1$.  \n"
            "Solve the given equation for $y$: $-y = -3x + 8$, so $y = 3x - 8$ and the slope "
            "is $3$. Parallel means the same slope, and the point $(0, -1)$ is the "
            "$y$-intercept, so $y = 3x - 1$.  \n"
            "Forgetting to divide the whole equation by $-1$ gives slope $-3$, a listed option.",
            ["Eq(solve(Eq(3*x - y, 8), y)[0], 3*x - 8)", "Eq(3*0 - 1, -1)"],
        ),
        problem(
            "sat-l2b-t3",
            "A line passes through $(2, 9)$ and $(6, 21)$. What is its $y$-intercept?",
            "**Answer.** $3$.  \n"
            "Slope: $\\frac{21 - 9}{6 - 2} = \\frac{12}{4} = 3$. Then $9 = 3(2) + b$ gives "
            "$b = 3$. Check the other point: $3(6) + 3 = 21$.",
            ["Eq(Rational(21 - 9, 6 - 2), 3)", "Eq(3*2 + 3, 9)", "Eq(3*6 + 3, 21)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Three forms, one line",
            "beats": [
                "Slope-intercept y = mx + b — best for reading the slope and the intercept.",
                "Point-slope y − y1 = m(x − x1) — best for building a line from a point.",
                "Standard Ax + By = C — how the SAT usually PRINTS a line, slope −A/B.",
                "Moving between them is algebra, not new mathematics.",
            ],
        },
        {
            "kind": "teach",
            "title": "Parallel and perpendicular",
            "body": "Two lines are parallel exactly when their slopes are equal and their "
                    "intercepts are not — same climb, different starting height, so they never "
                    "meet. Two lines are perpendicular exactly when their slopes multiply to "
                    "$-1$, which means each slope is the other flipped upside down AND "
                    "negated. Half of that operation is the classic error: the negative "
                    "reciprocal of $-\\frac{2}{5}$ is $\\frac{5}{2}$, not $-\\frac{5}{2}$ and "
                    "not $\\frac{2}{5}$.",
        },
        {
            "kind": "systemGraph",
            "title": "Same slope, different intercept",
            "teach": "Drag the two lines. Matching their slopes makes them parallel and the "
                     "intersection disappears; matching the intercepts too collapses them into "
                     "one line. Every 'no solution' system on the SAT is the first picture.",
            "config": {"m1": 3, "b1": 7, "m2": 3, "b2": 2, "interactive": True, "min": -8, "max": 8},
        },
        {"kind": "worked", "title": "Perpendicular through the origin", "problemId": "sat-l2b-w1"},
        {
            "kind": "tapQuestion",
            "title": "Negative reciprocal",
            "prompt": "A line has slope $\\dfrac{2}{7}$. What is the slope of a line "
                      "perpendicular to it?",
            "options": [
                "$-\\dfrac{7}{2}$",
                "$\\dfrac{7}{2}$",
                "$-\\dfrac{2}{7}$",
                "$\\dfrac{2}{7}$",
            ],
            "correctIndex": 0,
            "explanation": "Flip AND negate: $\\frac{2}{7} \\to -\\frac{7}{2}$, and "
                           "$\\frac{2}{7} \\times \\left(-\\frac{7}{2}\\right) = -1$ confirms "
                           "it. Option B flips without negating, C negates without flipping, D "
                           "does neither.",
            "check": ["Eq(Rational(2,7)*(-Rational(7,2)), -1)", "Ne(Rational(2,7)*Rational(7,2), -1)"],
        },
        {"kind": "worked", "title": "Parallel means equal slopes", "problemId": "sat-l2b-w2"},
        {
            "kind": "tip",
            "title": "A table is a line in disguise",
            "body": "When a table's $x$-values step evenly and its $y$-values also step evenly, "
                    "the data is linear and the slope is one step of $y$ divided by one step of "
                    "$x$. The intercept almost never appears in the table — you have to compute "
                    "it by substituting one row into $y = mx + b$. Reading the first "
                    "$y$-value as the intercept is only right when that row has $x = 0$.",
        },
        {"kind": "worked", "title": "A line from a table", "problemId": "sat-l2b-w3"},
        {"kind": "tryIt", "title": "Your turn: perpendicular slope", "problemId": "sat-l2b-t1"},
        {"kind": "tryIt", "title": "Your turn: parallel through a point", "problemId": "sat-l2b-t2"},
        {"kind": "tryIt", "title": "Your turn: find the intercept", "problemId": "sat-l2b-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Parallel: equal slopes, different intercepts.",
                "Perpendicular: slopes multiply to −1 — flip the fraction and change the sign.",
                "From standard form Ax + By = C the slope is −A/B; watch the sign.",
                "In a table, equal steps in x with equal steps in y means the data is linear.",
                "The intercept is rarely in the table — compute it from one row.",
            ],
        },
    ]

    return lesson(
        slug="forms-parallel-and-perpendicular",
        title="Three Forms, Parallel Lines and Perpendicular Lines",
        concrete=(
            "Two streets that never cross run at the same angle; two that meet at a perfect "
            "corner have angles that are opposite in a very specific way. On a coordinate "
            "plane those two facts become one number each — equal slopes, and slopes whose "
            "product is $-1$ — and the SAT asks about them constantly."
        ),
        objective=(
            "Convert a line between slope-intercept, point-slope and standard form; recognise "
            "parallel and perpendicular slopes; and build a line from a table of values."
        ),
        concept=[
            "**Skill card.** Still *Linear equations in two variables*, in the **Algebra** "
            "domain. This is the half of the subtopic that carries the medium and hard items: "
            "converting between forms, spotting parallel and perpendicular, and reading a line "
            "out of a table.",
            "The same line can be written three ways. Slope-intercept $y = mx + b$ shows the "
            "slope and the $y$-intercept immediately. Point-slope $y - y_1 = m(x - x_1)$ is "
            "the quickest way to build a line from a point. Standard form $Ax + By = C$ is how "
            "the SAT usually prints one, and its slope is $-\\frac{A}{B}$ — the minus sign is "
            "the whole trap.",
            "Parallel lines have equal slopes and different $y$-intercepts. Perpendicular "
            "lines have slopes whose product is $-1$, which means one is the other flipped and "
            "negated. Doing only half of that — flipping without negating, or negating without "
            "flipping — produces two of the four options on nearly every question of this type.",
            "**The test's angle.** Tables. When the SAT gives you three rows of a linear "
            "relationship, the slope is one $y$-step divided by one $x$-step, and the "
            "intercept has to be computed from a row because the table almost never includes "
            "$x = 0$. Students who read the first $y$-value as the intercept lose the point "
            "even though their slope was right.",
        ],
        key_idea=(
            "One line, three forms. Equal slopes means parallel; slopes multiplying to $-1$ "
            "means perpendicular; and in standard form the slope is $-\\frac{A}{B}$."
        ),
        facts=[
            fact(
                "Parallel",
                "m_1 = m_2, \\qquad b_1 \\ne b_2",
                "Equal climb, different starting height. Equal intercepts too would make them "
                "the same line.",
            ),
            fact(
                "Perpendicular",
                "m_1 m_2 = -1 \\;\\Longleftrightarrow\\; m_2 = -\\frac{1}{m_1}",
                "Flip the fraction and change the sign. A quick check: the product must come "
                "out to exactly $-1$.",
            ),
            fact(
                "Standard to slope-intercept",
                "Ax + By = C \\;\\Longrightarrow\\; y = -\\frac{A}{B}x + \\frac{C}{B}",
                "Divide the whole equation by $B$, including the sign of $B$ — a negative $B$ "
                "flips both terms.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Taking the reciprocal without changing the sign for a perpendicular line.",
                "The perpendicular slope to $\\frac{2}{7}$ is $-\\frac{7}{2}$. Check by "
                "multiplying — the product must be exactly $-1$.",
            ),
            mistake(
                "Reading the first $y$-value in a table as the $y$-intercept.",
                "That only works when the row has $x = 0$. Otherwise substitute a row into "
                "$y = mx + b$ and solve for $b$.",
            ),
            mistake(
                "Forgetting the sign when $B$ is negative in standard form.",
                "In $3x - y = 8$, dividing by $-1$ gives $y = 3x - 8$. The slope is $+3$, not "
                "$-3$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 3 — lines in context
# ===========================================================================

def lesson_context():
    worked = [
        problem(
            "sat-l2c-w1",
            "A candle burns at a constant rate. After $2$ hours it is $23$ centimetres tall, "
            "and after $5$ hours it is $17$ centimetres tall. Which equation gives the height "
            "$h$, in centimetres, after $t$ hours?",
            "**Answer.** $h = 27 - 2t$.  \n"
            "The two given facts are two points, $(2, 23)$ and $(5, 17)$. The rate of change "
            "is the slope:\n"
            "$$m = \\frac{17 - 23}{5 - 2} = \\frac{-6}{3} = -2$$\n"
            "The candle loses $2$ centimetres an hour, and the negative sign is the word "
            "'burns'. Now find the starting height using either point:\n"
            "$$23 = -2(2) + b \\;\\Longrightarrow\\; b = 27$$\n"
            "So $h = 27 - 2t$, and the candle was $27$ centimetres tall when it was lit.  \n"
            "Check the second point: $27 - 2(5) = 17$.  \n"
            "A positive slope here would mean a candle that grows — always sanity-check the "
            "sign against the verb in the sentence.",
            [
                "Eq(Rational(17 - 23, 5 - 2), -2)",
                "Eq(27 - 2*2, 23)",
                "Eq(27 - 2*5, 17)",
            ],
        ),
        problem(
            "sat-l2c-w2",
            "The total cost $C$, in dollars, of renting a hall for $h$ hours is given by "
            "$C = 85h + 400$. Which of the following is the best interpretation of the number "
            "$85$ in this context?",
            "**Answer.** The cost increases by $\\$85$ for each additional hour of rental.  \n"
            "The number multiplying the variable is the RATE of change. Its units come "
            "straight from the two quantities: $C$ is in dollars and $h$ is in hours, so $85$ "
            "is measured in dollars per hour.  \n"
            "The other number, $400$, is the value of $C$ when $h = 0$ — a fixed booking fee "
            "charged before a single hour is used. Swapping the two interpretations is the "
            "entire question: the constant term is the one-time amount, the coefficient is "
            "the per-unit amount.  \n"
            "A quick confirmation: $C(3) - C(2) = 655 - 570 = 85$, exactly the cost of the "
            "third hour.",
            [
                "Eq(85*3 + 400, 655)",
                "Eq(85*2 + 400, 570)",
                "Eq((85*3 + 400) - (85*2 + 400), 85)",
                "Eq(85*0 + 400, 400)",
            ],
        ),
        problem(
            "sat-l2c-w3",
            "A pool containing $4{,}500$ litres is drained at a constant rate of $150$ litres "
            "per minute. Let $V$ be the volume of water remaining after $t$ minutes. For what "
            "values of $t$ does the equation $V = 4500 - 150t$ make sense in this context?",
            "**Answer.** $0 \\le t \\le 30$.  \n"
            "Two conditions bound the domain. Time cannot run backwards, so $t \\ge 0$. And "
            "the pool cannot hold a negative volume, so the model stops when $V$ reaches zero:\n"
            "$$4500 - 150t = 0$$\n"
            "$$150t = 4500$$\n"
            "$$t = 30$$\n"
            "After $30$ minutes the pool is empty and the equation would start predicting "
            "negative water — the model has broken down, not the arithmetic.  \n"
            "Domain questions like this one are pure SAT: the algebra is one division and the "
            "point being tested is whether you noticed the model has an end.",
            [
                "Eq(4500 - 150*30, 0)",
                "Eq(4500 - 150*0, 4500)",
                "Eq(4500 - 150*31, -150)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l2c-t1",
            "A phone plan costs $\\$18$ per month plus $\\$0.05$ per text message. Which "
            "equation gives the monthly bill $B$ in dollars for $n$ text messages?",
            "**Answer.** $B = 0.05n + 18$.  \n"
            "The per-message charge varies with $n$, so it is the coefficient; the monthly "
            "charge is fixed, so it is the constant. Check with $n = 100$: "
            "$0.05(100) + 18 = 23$ dollars.",
            ["Eq(Rational(5,100)*100 + 18, 23)"],
        ),
        problem(
            "sat-l2c-t2",
            "The number of subscribers $S$ of a magazine after $y$ years is modelled by "
            "$S = 12000 - 450y$. What does $450$ represent?",
            "**Answer.** The magazine loses $450$ subscribers each year.  \n"
            "The coefficient of $y$ is the yearly rate of change, and the minus sign in front "
            "of it makes that change a loss. The $12{,}000$ is the subscriber count at "
            "$y = 0$, the year the model starts.",
            [
                "Eq(12000 - 450*0, 12000)",
                "Eq((12000 - 450*1) - (12000 - 450*2), 450)",
            ],
        ),
        problem(
            "sat-l2c-t3",
            "A tree is $150$ centimetres tall and grows $8$ centimetres per year. After how "
            "many years is it $2.7$ metres tall?",
            "**Answer.** $15$ years.  \n"
            "Convert first: $2.7$ metres is $270$ centimetres. Then "
            "$150 + 8y = 270$, so $8y = 120$ and $y = 15$.  \n"
            "Skipping the unit conversion and solving $150 + 8y = 2.7$ gives a negative "
            "answer, which is the signal that a conversion was missed.",
            ["Eq(150 + 8*15, 270)", "Eq(Rational(27,10)*100, 270)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Every context has the same two numbers",
            "beats": [
                "The starting amount — what is true before anything happens. That is the intercept.",
                "The per-unit change — what happens each hour, month or kilometre. That is the slope.",
                "A word meaning decrease (burns, drains, loses, falls) makes the slope negative.",
                "The units of the slope are always the y-unit divided by the x-unit.",
            ],
        },
        {
            "kind": "evaluator",
            "title": "Watch the two numbers do their jobs",
            "teach": "Slide the hours and watch the hall-rental total. The 400-dollar booking "
                     "fee is there before the slider moves at all; each hour adds another 85. "
                     "Interpretation questions are just asking which of those two roles a "
                     "number plays.",
            "config": {"a": 85, "b": 400, "varName": "h", "min": 0, "max": 12, "start": 3},
        },
        {"kind": "worked", "title": "Two facts make a model", "problemId": "sat-l2c-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which number is which?",
            "prompt": "A gym membership costs $C = 30m + 75$ dollars for $m$ months. What does "
                      "the $75$ represent?",
            "options": [
                "A one-time joining fee of $\\$75$",
                "The monthly charge of $\\$75$",
                "The cost of $75$ months",
                "The total cost of the membership",
            ],
            "correctIndex": 0,
            "explanation": "Setting $m = 0$ gives $C = 75$: the amount owed before a single "
                           "month has passed, which is a one-time fee. The monthly charge is "
                           "the coefficient $30$. The total cost depends on $m$ and is never a "
                           "single number.",
            "check": ["Eq(30*0 + 75, 75)", "Eq(30*1 + 75, 105)", "Eq((30*1 + 75) - (30*0 + 75), 30)"],
        },
        {"kind": "worked", "title": "Interpreting a coefficient", "problemId": "sat-l2c-w2"},
        {
            "kind": "tip",
            "title": "Check the units, then the sign",
            "body": "The units of a slope are always the $y$-unit over the $x$-unit — dollars "
                    "per hour, litres per minute, subscribers per year. If an interpretation "
                    "option has the wrong units it is wrong, no matter how plausible the "
                    "sentence sounds. Then check the sign against the verb: 'drains', "
                    "'loses' and 'falls' all demand a negative rate.",
        },
        {"kind": "worked", "title": "Where the model stops", "problemId": "sat-l2c-w3"},
        {"kind": "tryIt", "title": "Your turn: build the equation", "problemId": "sat-l2c-t1"},
        {"kind": "tryIt", "title": "Your turn: interpret the rate", "problemId": "sat-l2c-t2"},
        {"kind": "tryIt", "title": "Your turn: mind the units", "problemId": "sat-l2c-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "The constant term is the starting amount; the coefficient is the per-unit rate.",
                "Two data points give the rate; substitute one back to get the starting amount.",
                "A verb meaning decrease makes the slope negative — check the sign against the words.",
                "The slope's units are the y-unit divided by the x-unit, always.",
                "Context questions can end the model early: solve for when the quantity hits zero.",
            ],
        },
    ]

    return lesson(
        slug="linear-equations-in-context",
        title="Writing the Equation a Context Describes",
        concrete=(
            "A candle is $27$ centimetres tall and burns $2$ centimetres an hour. Those two "
            "numbers — where it starts and how fast it changes — are the only things you need "
            "to answer every question anyone can ask about that candle. The SAT's version of "
            "the question hides one of the two numbers and hands you a pair of measurements "
            "instead."
        ),
        objective=(
            "Build a linear equation from a described situation or two data points, interpret "
            "the slope and intercept in the context's own units, and identify where the model "
            "stops making sense."
        ),
        concept=[
            "**Skill card.** Still *Linear equations in two variables*, in the **Algebra** "
            "domain, but this is the version the College Board writes most often — the "
            "modelling item. There is very little algebra in it and a great deal of careful "
            "reading, which is exactly why it is worth practising separately.",
            "Every linear context contains the same two numbers. There is a starting amount — "
            "what is true before anything happens — and that is the $y$-intercept. And there "
            "is a per-unit rate of change — what happens each hour, each month, each "
            "kilometre — and that is the slope. Write those two down in the context's own "
            "units and the equation assembles itself.",
            "When the question gives two measurements instead of a rate, they are two points. "
            "The slope comes from dividing the change in one quantity by the change in the "
            "other, and substituting either point back gives the starting amount. Watch the "
            "sign: any verb meaning decrease — burns, drains, loses, falls, cools — makes the "
            "rate negative.",
            "**The test's angle.** Interpretation questions look easy and are graded on "
            "precision. 'What does $85$ represent?' has four plausible-sounding options and "
            "the units settle it: $C$ in dollars over $h$ in hours makes $85$ dollars per "
            "hour, so it is the per-hour charge and not the booking fee. The other favourite "
            "is a domain question — the model stops when the quantity would go negative, so "
            "solve for that moment and stop there.",
        ],
        key_idea=(
            "Starting amount at the intercept, per-unit rate at the slope, and the units of "
            "the rate are the $y$-unit over the $x$-unit. Read the verb to get the sign."
        ),
        facts=[
            fact(
                "The modelling template",
                "y = (\\text{rate}) \\cdot x + (\\text{starting amount})",
                "Nearly every SAT linear context is this template with different nouns.",
            ),
            fact(
                "Rate from two measurements",
                "\\text{rate} = \\frac{\\text{change in output}}{\\text{change in input}}",
                "Two measured pairs are two points. Same formula as slope, with units attached.",
            ),
            fact(
                "Where a decreasing model ends",
                "\\text{starting amount} - (\\text{rate}) \\cdot x = 0",
                "Solve for $x$ to find the last moment the model describes reality. Beyond it "
                "the equation predicts negative quantities.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Swapping the roles of the coefficient and the constant term.",
                "Set the variable to zero: whatever survives is the one-time amount. Whatever "
                "multiplies the variable is the per-unit rate.",
            ),
            mistake(
                "Giving a positive rate to a quantity that is described as decreasing.",
                "Burns, drains, loses and falls all mean the coefficient is negative. Check "
                "the sign against the verb before choosing.",
            ),
            mistake(
                "Solving without converting units first.",
                "If the rate is in centimetres per year, the target height must be in "
                "centimetres too. Convert, then solve.",
            ),
            mistake(
                "Extending a model past the point where it stops describing anything.",
                "A drained pool holds zero litres, not negative litres. Solve for when the "
                "quantity reaches zero and treat that as the end of the domain.",
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
        "sat-l2-p01",
        "What is the slope of the line through $(1, 2)$ and $(5, 14)$?",
        "**Answer.** $3$. $m = \\frac{14 - 2}{5 - 1} = \\frac{12}{4} = 3$.",
        ["Eq(Rational(14 - 2, 5 - 1), 3)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-p02",
        "$$2x + y = 9$$\n"
        "What is the $y$-intercept of the graph of this equation?",
        "**Answer.** $(0, 9)$. Setting $x = 0$ gives $y = 9$. Solving for $y$ shows the same "
        "thing at a glance: $y = -2x + 9$.",
        ["Eq(2*0 + 9, 9)", "Eq(solve(Eq(2*x + y, 9), y)[0], -2*x + 9)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-p03",
        "A line has slope $\\tfrac{1}{3}$ and passes through $(6, 4)$. What is its "
        "$y$-intercept?",
        "**Answer.** $2$. Substitute into $y = mx + b$: $4 = \\frac{1}{3}(6) + b = 2 + b$, so "
        "$b = 2$.",
        ["Eq(Rational(1,3)*6 + 2, 4)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-p04",
        "Which equation defines a line perpendicular to $y = -\\tfrac{1}{4}x + 9$?",
        "**Answer.** Any line with slope $4$, for example $y = 4x - 1$. The negative "
        "reciprocal of $-\\frac{1}{4}$ is $4$, and $-\\frac{1}{4} \\times 4 = -1$ confirms "
        "the perpendicularity. Slope $\\frac{1}{4}$ (negating only) and $-4$ (flipping only) "
        "are the two standard distractors.",
        ["Eq(-Rational(1,4)*4, -1)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-p05",
        "$$6x - 4y = 20$$\n"
        "What is the slope of the graph of this equation?",
        "**Answer.** $\\dfrac{3}{2}$. Solve for $y$: $-4y = -6x + 20$, so "
        "$y = \\frac{3}{2}x - 5$. Both signs flip when dividing by $-4$; missing that gives "
        "$-\\frac{3}{2}$.",
        ["Eq(solve(Eq(6*x - 4*y, 20), y)[0], Rational(3,2)*x - 5)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-p06",
        "A line passes through $(-3, 8)$ and $(1, 0)$. What is the $x$-intercept of the line?",
        "**Answer.** $(1, 0)$. The point $(1, 0)$ already has $y = 0$, so it IS the "
        "$x$-intercept — no work needed. (The slope is $-2$ and the equation is $y = -2x + 2$, "
        "confirming an $x$-intercept at $x = 1$.)",
        ["Eq(Rational(0 - 8, 1 - (-3)), -2)", "Eq(-2*1 + 2, 0)", "Eq(-2*(-3) + 2, 8)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-p07",
        "A shrub is $40$ centimetres tall and grows $6$ centimetres per month. Which equation "
        "gives its height $H$, in centimetres, after $m$ months?",
        "**Answer.** $H = 6m + 40$. The growth per month is the coefficient; the height at "
        "$m = 0$ is the constant. Check at $m = 5$: $6(5) + 40 = 70$ centimetres.",
        ["Eq(6*5 + 40, 70)", "Eq(6*0 + 40, 40)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-p08",
        "The table shows three points on a line.\n\n"
        "| $x$ | $y$ |\n| --- | --- |\n| $-1$ | $10$ |\n| $2$ | $4$ |\n| $5$ | $-2$ |\n\n"
        "What is the $y$-intercept of the line?",
        "**Answer.** $8$. The slope is $\\frac{4 - 10}{2 - (-1)} = \\frac{-6}{3} = -2$. "
        "Substituting $(2, 4)$ into $y = -2x + b$ gives $4 = -4 + b$, so $b = 8$. Note the "
        "table never shows $x = 0$, so $10$ is not the intercept.",
        [
            "Eq(Rational(4 - 10, 2 - (-1)), -2)",
            "Eq(-2*2 + 8, 4)",
            "Eq(-2*(-1) + 8, 10)",
            "Eq(-2*5 + 8, -2)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-p09",
        "The cost $C$, in dollars, of producing $n$ items is $C = 4n + 900$. What is the best "
        "interpretation of $900$?",
        "**Answer.** A fixed cost of $\\$900$ incurred before any items are produced. Setting "
        "$n = 0$ gives $C = 900$. The $4$ is the cost per item, in dollars per item.",
        ["Eq(4*0 + 900, 900)", "Eq((4*11 + 900) - (4*10 + 900), 4)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-p10",
        "In the $xy$-plane, line $j$ passes through $(0, 5)$ and is parallel to the line "
        "$4x + 2y = 7$. Which equation defines line $j$?",
        "**Answer.** $y = -2x + 5$. Solving $4x + 2y = 7$ for $y$ gives $y = -2x + 3.5$, so "
        "the slope is $-2$. Line $j$ has the same slope and $y$-intercept $5$.",
        ["Eq(solve(Eq(4*x + 2*y, 7), y)[0], -2*x + Rational(7,2))", "Eq(-2*0 + 5, 5)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-p11",
        "A $600$-litre tank is filled at $25$ litres per minute starting from empty. For what "
        "values of $t$, in minutes, does $V = 25t$ describe the tank?",
        "**Answer.** $0 \\le t \\le 24$. The tank starts empty at $t = 0$ and is full when "
        "$25t = 600$, that is $t = 24$. Past $24$ minutes the equation predicts more than the "
        "tank can hold.",
        ["Eq(25*24, 600)", "Eq(25*0, 0)", "25*25 > 600"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-p12",
        "Line $\\ell$ passes through $(4, -1)$ and is perpendicular to the line $y = 2x + 3$. "
        "What is the $y$-intercept of line $\\ell$?",
        "**Answer.** $1$. The perpendicular slope is $-\\frac{1}{2}$. Substituting the point: "
        "$-1 = -\\frac{1}{2}(4) + b = -2 + b$, so $b = 1$. Check: "
        "$2 \\times \\left(-\\frac{1}{2}\\right) = -1$.",
        ["Eq(2*(-Rational(1,2)), -1)", "Eq(-Rational(1,2)*4 + 1, -1)"],
        badges=_b("Hard"),
    ),
]

TEST = [
    problem(
        "sat-l2-x01",
        "What is the slope of the line through $(-4, 3)$ and $(2, -9)$?",
        "**Answer.** $-2$. $m = \\frac{-9 - 3}{2 - (-4)} = \\frac{-12}{6} = -2$.",
        ["Eq(Rational(-9 - 3, 2 - (-4)), -2)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-x02",
        "$$3x + 5y = 45$$\n"
        "What is the $x$-intercept of the graph of this equation?",
        "**Answer.** $(15, 0)$. Setting $y = 0$ gives $3x = 45$ and $x = 15$. Setting $x = 0$ "
        "instead gives the $y$-intercept $(0, 9)$.",
        ["Eq(3*15 + 5*0, 45)", "Eq(3*0 + 5*9, 45)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l2-x03",
        "Line $g$ has slope $-\\tfrac{2}{3}$ and passes through $(9, 4)$. What is the "
        "$y$-intercept of line $g$?",
        "**Answer.** $10$. $4 = -\\frac{2}{3}(9) + b = -6 + b$, so $b = 10$.",
        ["Eq(-Rational(2,3)*9 + 10, 4)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-x04",
        "In the $xy$-plane, a line perpendicular to $y = \\tfrac{3}{7}x - 2$ passes through "
        "$(0, 6)$. Which equation defines that line?",
        "**Answer.** $y = -\\dfrac{7}{3}x + 6$. The negative reciprocal of $\\frac{3}{7}$ is "
        "$-\\frac{7}{3}$, and the given point is the $y$-intercept.",
        ["Eq(Rational(3,7)*(-Rational(7,3)), -1)", "Eq(-Rational(7,3)*0 + 6, 6)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-x05",
        "A machine is filled with $18$ kilograms of coffee beans and dispenses $0.25$ "
        "kilograms per serving. After how many servings does it hold $6$ kilograms?",
        "**Answer.** $48$ servings. The model is $W = 18 - 0.25s$. Setting $W = 6$ gives "
        "$0.25s = 12$, so $s = 48$.",
        ["Eq(18 - Rational(25,100)*48, 6)", "Eq(18 - Rational(25,100)*72, 0)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-x06",
        "The table shows three points on a line.\n\n"
        "| $x$ | $y$ |\n| --- | --- |\n| $2$ | $-1$ |\n| $6$ | $9$ |\n| $10$ | $19$ |\n\n"
        "Which equation represents the line?",
        "**Answer.** $y = \\dfrac{5}{2}x - 6$. The slope is $\\frac{9 - (-1)}{6 - 2} = "
        "\\frac{10}{4} = \\frac{5}{2}$. Substituting $(2, -1)$: $-1 = 5 + b$, so $b = -6$. "
        "Check the last row: $\\frac{5}{2}(10) - 6 = 19$.",
        [
            "Eq(Rational(9 - (-1), 6 - 2), Rational(5,2))",
            "Eq(Rational(5,2)*2 - 6, -1)",
            "Eq(Rational(5,2)*10 - 6, 19)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-x07",
        "The temperature $T$, in degrees Celsius, of a cooling engine after $t$ minutes is "
        "$T = 95 - 3.5t$. What does $3.5$ represent?",
        "**Answer.** The engine cools by $3.5$ degrees Celsius each minute. The coefficient of "
        "$t$ is the rate of change, in degrees per minute, and the minus sign in front of it "
        "makes it a decrease. The $95$ is the temperature when timing began.",
        [
            "Eq(95 - Rational(35,10)*0, 95)",
            "Eq((95 - Rational(35,10)*4) - (95 - Rational(35,10)*5), Rational(35,10))",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l2-x08",
        "Line $r$ passes through $(-2, 5)$ and $(4, 5)$. Line $s$ is perpendicular to line $r$ "
        "and passes through $(3, 1)$. Which statement describes line $s$?",
        "**Answer.** Line $s$ is the vertical line $x = 3$. Line $r$ has slope "
        "$\\frac{5 - 5}{4 - (-2)} = 0$: it is horizontal. A line perpendicular to a horizontal "
        "line is vertical, and a vertical line through $(3, 1)$ is $x = 3$. The negative "
        "reciprocal rule breaks here because you cannot divide by zero — which is exactly why "
        "vertical lines are said to have no slope rather than slope zero.",
        ["Eq(Rational(5 - 5, 4 - (-2)), 0)", "Eq(3, 3)"],
        badges=_b("Hard"),
    ),
]


def main():
    lessons = [lesson_slope(), lesson_forms(), lesson_context()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Linear Equations in Two Variables",
        2,
        "Slope as a rate, both intercepts, the three forms the test writes a line in, parallel "
        "and perpendicular slopes, lines read out of tables — and the modelling questions that "
        "ask what a coefficient MEANS.",
        "Solving in one variable from Unit 1 — every method here ends with one of those.",
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
