#!/usr/bin/env python3
"""SAT Math — Advanced Math, Unit 3: Systems of equations in two variables.

Builds data/genmath/sat/systems-nonlinear-two-variables.json. The nonlinear
systems subtopic: a line meeting a curve. Two lessons — solving one, and
counting the intersections without solving.

Deliberately the shortest unit in the domain. The College Board's subtopic is
narrow, and padding it would misrepresent how much of the test it carries.

Run: python3 scripts/sat/build_adv_3.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "systems-nonlinear-two-variables"
TAG = {"text": "sat-nonlinear-systems", "mono": True}


def _b(level):
    return [TAG, {"text": level}]


# ===========================================================================
# Lesson 1 — solving a nonlinear system
# ===========================================================================

def lesson_solving():
    worked = [
        problem(
            "sat-ns1-w1",
            "$$y = x^{2} - 2x - 3$$\n$$y = 2x - 3$$\n"
            "What are the solutions $(x, y)$ to the system above?",
            "**Answer.** $(0, -3)$ and $(4, 5)$.  \n"
            "Both equations already give $y$ alone, so set the two right-hand sides equal — "
            "at an intersection the two $y$-values are the same number:\n"
            "$$x^{2} - 2x - 3 = 2x - 3$$\n"
            "Move everything to one side. Do NOT divide by $x$; that would destroy a "
            "solution:\n"
            "$$x^{2} - 4x = 0$$\n"
            "$$x(x - 4) = 0$$\n"
            "$$x = 0 \\quad \\text{or} \\quad x = 4$$\n"
            "Now find each $y$ from the SIMPLER equation, the line:\n"
            "$$x = 0: \\; y = -3 \\qquad x = 4: \\; y = 5$$\n"
            "Check the parabola too: $0 - 0 - 3 = -3$ and $16 - 8 - 3 = 5$. Both points sit "
            "on both curves.  \n"
            "Dividing both sides by $x$ at the second line would have given $x - 4 = 0$ and "
            "lost the solution $x = 0$ entirely. Factor instead — dividing by something that "
            "might be zero is never safe.",
            [
                "Eq(0**2 - 2*0 - 3, 2*0 - 3)",
                "Eq(4**2 - 2*4 - 3, 2*4 - 3)",
                "Eq(4**2 - 2*4 - 3, 5)",
                "Eq(expand(x*(x - 4)), x**2 - 4*x)",
            ],
        ),
        problem(
            "sat-ns1-w2",
            "$$x^{2} + y^{2} = 25$$\n$$y = x + 1$$\n"
            "What is the sum of the $x$-coordinates of the solutions?",
            "**Answer.** $-1$.  \n"
            "The first equation is a circle of radius $5$ centred at the origin; the second is "
            "a line. Substitute the line into the circle:\n"
            "$$x^{2} + (x + 1)^{2} = 25$$\n"
            "Expand the square as a whole — $(x+1)^{2}$ is $x^{2} + 2x + 1$, not "
            "$x^{2} + 1$:\n"
            "$$x^{2} + x^{2} + 2x + 1 = 25$$\n"
            "$$2x^{2} + 2x - 24 = 0$$\n"
            "$$x^{2} + x - 12 = 0$$\n"
            "$$(x + 4)(x - 3) = 0$$\n"
            "so $x = -4$ or $x = 3$, and the sum is $-1$.  \n"
            "That sum was available without factoring: for $x^{2} + x - 12 = 0$ the solutions "
            "sum to $-\\frac{b}{a} = -1$.  \n"
            "Check: $(-4, -3)$ gives $16 + 9 = 25$, and $(3, 4)$ gives $9 + 16 = 25$. Both are "
            "on the circle and on the line.",
            [
                "Eq((-4)**2 + (-3)**2, 25)",
                "Eq(3**2 + 4**2, 25)",
                "Eq(-3, -4 + 1)",
                "Eq(4, 3 + 1)",
                "Eq(-4 + 3, -1)",
            ],
        ),
        problem(
            "sat-ns1-w3",
            "$$y = x^{2} + 4x + 7$$\n$$y = 3$$\n"
            "How many solutions $(x, y)$ does the system have?",
            "**Answer.** Exactly one.  \n"
            "Set the two expressions for $y$ equal:\n"
            "$$x^{2} + 4x + 7 = 3$$\n"
            "$$x^{2} + 4x + 4 = 0$$\n"
            "$$(x + 2)^{2} = 0$$\n"
            "so $x = -2$ is the only solution, giving the single point $(-2, 3)$.  \n"
            "The discriminant says the same thing without factoring: "
            "$b^{2} - 4ac = 16 - 16 = 0$, and a zero discriminant means exactly one "
            "solution.  \n"
            "Geometrically the horizontal line $y = 3$ just touches the parabola at its "
            "vertex — it is TANGENT. That is what a repeated root looks like on a graph, and "
            "'the line is tangent to the curve' is the SAT's usual phrasing for 'the "
            "discriminant is zero'.",
            [
                "Eq(4**2 - 4*1*4, 0)",
                "Eq(expand((x + 2)**2), x**2 + 4*x + 4)",
                "Eq((-2)**2 + 4*(-2) + 7, 3)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ns1-t1",
            "$$y = x^{2}$$\n$$y = 5x - 6$$\n"
            "What are the $x$-coordinates of the solutions?",
            "**Answer.** $x = 2$ and $x = 3$. Setting them equal gives "
            "$x^{2} - 5x + 6 = 0$, which factors as $(x - 2)(x - 3) = 0$. Check: at $x = 2$ "
            "both give $4$; at $x = 3$ both give $9$.",
            [
                "Eq(2**2, 5*2 - 6)",
                "Eq(3**2, 5*3 - 6)",
                "Eq(expand((x - 2)*(x - 3)), x**2 - 5*x + 6)",
            ],
        ),
        problem(
            "sat-ns1-t2",
            "$$y = x^{2} - 4$$\n$$y = 3x$$\n"
            "What is the product of the $x$-coordinates of the solutions?",
            "**Answer.** $-4$. Setting them equal gives $x^{2} - 3x - 4 = 0$, so the product "
            "of the roots is $\\frac{c}{a} = -4$. Factoring confirms it: $(x - 4)(x + 1) = 0$ "
            "gives $x = 4$ and $x = -1$.",
            [
                "Eq(expand((x - 4)*(x + 1)), x**2 - 3*x - 4)",
                "Eq(4*(-1), -4)",
                "Eq(4**2 - 4, 3*4)",
                "Eq((-1)**2 - 4, 3*(-1))",
            ],
        ),
        problem(
            "sat-ns1-t3",
            "$$x^{2} + y^{2} = 10$$\n$$y = 3x$$\n"
            "What are the possible values of $x$?",
            "**Answer.** $x = 1$ and $x = -1$. Substituting gives $x^{2} + 9x^{2} = 10$, so "
            "$10x^{2} = 10$ and $x^{2} = 1$. Both signs count: the line through the origin "
            "cuts the circle twice, once on each side.",
            ["Eq(1**2 + (3*1)**2, 10)", "Eq((-1)**2 + (3*(-1))**2, 10)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Systems of equations in two variables",
            "beats": [
                "Domain: Advanced Math — 13 to 15 of the 44 questions on the Math section.",
                "Usually 1 question a test, and usually in the harder module.",
                "Prerequisites: solving quadratics, and systems of linear equations.",
                "The whole subtopic is a line meeting a curve.",
            ],
        },
        {
            "kind": "teach",
            "title": "Substitute the line into the curve",
            "body": "A solution is a point on BOTH graphs. So take the equation that gives one "
                    "variable alone — that is nearly always the line — and substitute it into "
                    "the other. What comes out is a quadratic in one variable, which you "
                    "already know how to solve. Every root gives an $x$, and each $x$ gives a "
                    "$y$ from the line.",
        },
        {
            "kind": "parabolaGraph",
            "title": "Where a line meets a parabola",
            "teach": "Move the parabola and watch how a horizontal line cuts it: twice, once "
                     "at the vertex, or not at all. Those three cases are exactly the three "
                     "signs of the discriminant.",
            "config": {"mode": "vertex", "a": 1, "h": 1, "k": -4, "interactive": True, "min": -6, "max": 8},
        },
        {"kind": "worked", "title": "A line and a parabola", "problemId": "sat-ns1-w1"},
        {
            "kind": "tapQuestion",
            "title": "What goes wrong here?",
            "prompt": "Solving $x^{2} - 4x = 0$, a student divides both sides by $x$ and "
                      "concludes $x = 4$. What is wrong?",
            "options": [
                "Dividing by $x$ discards the solution $x = 0$",
                "Nothing — $x = 4$ is the only solution",
                "The equation has no solutions",
                "Dividing by $x$ changes the sign",
            ],
            "correctIndex": 0,
            "explanation": "Dividing by $x$ silently assumes $x \\ne 0$ — but $x = 0$ does "
                           "satisfy the equation, since $0 - 0 = 0$. Factoring to "
                           "$x(x - 4) = 0$ keeps both roots. Never divide an equation by "
                           "something that could be zero.",
            "check": ["Eq(0**2 - 4*0, 0)", "Eq(4**2 - 4*4, 0)", "Eq(expand(x*(x - 4)), x**2 - 4*x)"],
        },
        {
            "kind": "teach",
            "title": "The circle, and squaring a binomial",
            "beats": [
                "x² + y² = r² is the circle of radius r centred at the origin.",
                "Substituting y = mx + c into it gives a quadratic in x.",
                "Expand (x + 1)² as x² + 2x + 1 — squaring term by term loses the middle.",
                "A line through the origin always cuts a circle twice, once on each side.",
            ],
        },
        {"kind": "worked", "title": "A line and a circle", "problemId": "sat-ns1-w2"},
        {
            "kind": "tip",
            "title": "Answer what is asked, not the whole system",
            "body": "These questions often want a SUM or a PRODUCT of the $x$-coordinates, or "
                    "just the number of solutions. All three are readable off the quadratic "
                    "without solving it: the sum is $-\\frac{b}{a}$, the product is "
                    "$\\frac{c}{a}$, and the count is the sign of the discriminant. Getting "
                    "the quadratic is often the whole job.",
        },
        {"kind": "worked", "title": "A tangent line", "problemId": "sat-ns1-w3"},
        {"kind": "tryIt", "title": "Your turn: line meets parabola", "problemId": "sat-ns1-t1"},
        {"kind": "tryIt", "title": "Your turn: product of the roots", "problemId": "sat-ns1-t2"},
        {"kind": "tryIt", "title": "Your turn: line meets circle", "problemId": "sat-ns1-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Substitute the equation that gives a variable alone into the other one.",
                "What results is a quadratic — solve it, then get each y from the line.",
                "Never divide both sides by a variable; factor instead, or you lose a root.",
                "Expand (x + c)² fully; squaring term by term loses the middle term.",
                "Sum, product and count are all readable off the quadratic without solving.",
            ],
        },
    ]

    return lesson(
        slug="solving-nonlinear-systems",
        title="When a Line Meets a Curve",
        concrete=(
            "A ball's flight is a parabola; a fence is a straight line. Asking whether the "
            "ball clears the fence — and where it crosses — is asking for the intersection of "
            "a curve and a line. There can be two such points, one, or none, and the algebra "
            "tells you which before you draw anything."
        ),
        objective=(
            "Solve a system of one linear and one quadratic equation by substitution, "
            "including circles, and answer for the coordinates, their sum, their product or "
            "their count."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Systems of equations in two "
            "variables*, in the **Advanced Math** domain. It is usually one question a test, "
            "and usually in the harder module — but it is a short skill, because it always "
            "reduces to a quadratic you already know how to solve.",
            "A solution is a point lying on BOTH graphs. Take the equation that gives one "
            "variable alone — almost always the line — and substitute it into the other. What "
            "comes out is a quadratic in a single variable. Each root is an $x$-coordinate, "
            "and each $x$ goes back into the LINE (the easier equation) for its $y$.",
            "Circles turn up as $x^{2} + y^{2} = r^{2}$, centred at the origin with radius "
            "$r$. Substituting $y = mx + c$ into that produces a quadratic in the same way — "
            "the only extra care needed is expanding $(mx + c)^{2}$ as a whole, since squaring "
            "term by term loses the middle term and quietly changes the problem.",
            "**The test's angle.** Two traps. First, never divide both sides by a variable: "
            "$x^{2} - 4x = 0$ becomes $x = 4$ if you divide by $x$, silently losing the "
            "solution $x = 0$. Factor instead. Second, the question often wants the SUM or "
            "PRODUCT of the $x$-coordinates, or just how many solutions there are — and all "
            "three come straight off the quadratic's coefficients, so getting the quadratic is "
            "usually the entire job.",
        ],
        key_idea=(
            "Substitute the line into the curve and you get a quadratic. Its roots are the "
            "$x$-coordinates, its coefficients give their sum and product, and its "
            "discriminant counts them."
        ),
        facts=[
            fact(
                "Circle centred at the origin",
                "x^{2} + y^{2} = r^{2}",
                "Radius $r$, centre $(0,0)$. Substituting a line gives a quadratic in $x$.",
            ),
            fact(
                "Never divide by a variable",
                "x^{2} = 4x \\;\\Longrightarrow\\; x^{2} - 4x = 0 \\;\\Longrightarrow\\; x(x - 4) = 0",
                "Dividing by $x$ assumes $x \\ne 0$ and discards a genuine solution.",
            ),
            fact(
                "Squaring a binomial",
                "(mx + c)^{2} = m^{2}x^{2} + 2mcx + c^{2}",
                "The middle term is real. Squaring term by term is the commonest slip in a "
                "line-meets-circle substitution.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Dividing both sides by $x$ to simplify.",
                "That assumes $x \\ne 0$ and throws away the root $x = 0$. Move everything to "
                "one side and factor.",
            ),
            mistake(
                "Expanding $(x + 1)^{2}$ as $x^{2} + 1$.",
                "It is $x^{2} + 2x + 1$. Losing the middle term changes the whole quadratic.",
            ),
            mistake(
                "Giving only the $x$-coordinates when the question asks for points.",
                "Each $x$ needs its $y$, from the line. A solution to a two-variable system is "
                "a pair.",
            ),
            mistake(
                "Substituting the $x$-values back into the harder equation.",
                "Use the line. It has less to go wrong, and any solution of the system "
                "satisfies both anyway.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — counting intersections
# ===========================================================================

def lesson_counting():
    worked = [
        problem(
            "sat-ns2-w1",
            "$$y = x^{2} + 3x + 5$$\n$$y = x + c$$\n"
            "In the system above, $c$ is a constant. For what value of $c$ is the line tangent "
            "to the parabola?",
            "**Answer.** $c = 4$.  \n"
            "Tangent means the line touches the curve at exactly one point, which means the "
            "resulting quadratic has exactly one solution — a zero discriminant.  \n"
            "Set the two expressions equal and collect on one side:\n"
            "$$x^{2} + 3x + 5 = x + c$$\n"
            "$$x^{2} + 2x + (5 - c) = 0$$\n"
            "Here $a = 1$, $b = 2$ and the constant is $5 - c$. Set the discriminant to zero:\n"
            "$$2^{2} - 4(1)(5 - c) = 0$$\n"
            "$$4 - 20 + 4c = 0$$\n"
            "$$4c = 16 \\;\\Longrightarrow\\; c = 4$$\n"
            "Check: with $c = 4$ the quadratic is $x^{2} + 2x + 1 = (x + 1)^{2} = 0$, whose "
            "only root is $x = -1$. The single touching point is $(-1, 3)$.  \n"
            "The sign of $-4ac$ is where this is lost. With the constant $5 - c$, "
            "$-4(1)(5 - c)$ is $-20 + 4c$, not $-20 - 4c$.",
            [
                "Eq(2**2 - 4*1*(5 - 4), 0)",
                "Eq(expand((x + 1)**2), x**2 + 2*x + 1)",
                "Eq((-1)**2 + 3*(-1) + 5, 3)",
                "Eq(-1 + 4, 3)",
            ],
        ),
        problem(
            "sat-ns2-w2",
            "$$y = x^{2} - 6x + 11$$\n$$y = 1$$\n"
            "How many solutions does the system above have?",
            "**Answer.** None.  \n"
            "Set the expressions equal:\n"
            "$$x^{2} - 6x + 11 = 1$$\n"
            "$$x^{2} - 6x + 10 = 0$$\n"
            "The discriminant is\n"
            "$$(-6)^{2} - 4(1)(10) = 36 - 40 = -4$$\n"
            "which is negative, so there are no real solutions — the horizontal line "
            "$y = 1$ never meets the parabola.  \n"
            "A sanity check without the discriminant: completing the square gives "
            "$y = (x - 3)^{2} + 2$, so the parabola's lowest point is at height $2$. A line at "
            "height $1$ passes underneath it and cannot touch. Both routes agree, and the "
            "second one is often faster when the numbers are friendly.",
            [
                "Eq((-6)**2 - 4*1*10, -4)",
                "-4 < 0",
                "Eq(expand((x - 3)**2 + 2), x**2 - 6*x + 11)",
                "2 > 1",
            ],
        ),
        problem(
            "sat-ns2-w3",
            "$$y = 2x^{2} - 8x + k$$\n$$y = -x + 2$$\n"
            "For what values of the constant $k$ does the system have two distinct real "
            "solutions?",
            "**Answer.** $k < \\dfrac{57}{8}$.  \n"
            "Two distinct solutions means a POSITIVE discriminant. Set the expressions equal "
            "and collect:\n"
            "$$2x^{2} - 8x + k = -x + 2$$\n"
            "$$2x^{2} - 7x + (k - 2) = 0$$\n"
            "With $a = 2$, $b = -7$ and constant $k - 2$:\n"
            "$$(-7)^{2} - 4(2)(k - 2) > 0$$\n"
            "$$49 - 8k + 16 > 0$$\n"
            "$$65 > 8k$$\n"
            "$$k < \\frac{65}{8}$$\n"
            "Re-reading the expansion: $-4 \\cdot 2 \\cdot (k - 2) = -8k + 16$, so the "
            "discriminant is $49 - 8k + 16 = 65 - 8k$, giving $k < \\frac{65}{8} = 8.125$.  \n"
            "Check with $k = 0$, comfortably below the threshold: the quadratic is "
            "$2x^{2} - 7x - 2 = 0$ with discriminant $49 + 16 = 65 > 0$, so two solutions. "
            "Check with $k = 10$, above it: $2x^{2} - 7x + 8 = 0$ has discriminant "
            "$49 - 64 = -15 < 0$, so none.",
            [
                "Eq((-7)**2 - 4*2*(0 - 2), 65)",
                "65 > 0",
                "Eq((-7)**2 - 4*2*(10 - 2), -15)",
                "-15 < 0",
                "Eq(Rational(65,8), Rational(65,8))",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ns2-t1",
            "$$y = x^{2} + 2x + 6$$\n$$y = 5$$\n"
            "How many real solutions does the system have?",
            "**Answer.** Exactly one. Setting them equal gives $x^{2} + 2x + 1 = 0$, whose "
            "discriminant is $4 - 4 = 0$ — a repeated root at $x = -1$. The parabola's vertex "
            "is $(-1, 5)$, exactly the height of the line, so the line is tangent there and "
            "touches at the single point $(-1, 5)$.",
            [
                "Eq(2**2 - 4*1*1, 0)",
                "Eq((-1)**2 + 2*(-1) + 6, 5)",
            ],
        ),
        problem(
            "sat-ns2-t2",
            "$$y = x^{2} + 4$$\n$$y = mx$$\n"
            "For what positive value of $m$ is the line tangent to the parabola?",
            "**Answer.** $m = 4$. Setting them equal gives $x^{2} - mx + 4 = 0$, and tangency "
            "needs a zero discriminant: $m^{2} - 16 = 0$, so $m = \\pm 4$ and the positive "
            "value is $4$. Then $x^{2} - 4x + 4 = (x - 2)^{2} = 0$ touches at $(2, 8)$.",
            [
                "Eq(4**2 - 4*1*4, 0)",
                "Eq(expand((x - 2)**2), x**2 - 4*x + 4)",
                "Eq(2**2 + 4, 4*2)",
            ],
        ),
        problem(
            "sat-ns2-t3",
            "$$x^{2} + y^{2} = 9$$\n$$y = 4$$\n"
            "How many solutions does the system have?",
            "**Answer.** None. The circle has radius $3$, so every point on it has "
            "$|y| \\le 3$. The horizontal line $y = 4$ lies entirely outside it. "
            "Algebraically: $x^{2} + 16 = 9$ gives $x^{2} = -7$, which no real $x$ satisfies.",
            ["Eq(9 - 16, -7)", "-7 < 0", "3 < 4"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "You do not have to solve to count",
            "body": "Substituting the line into the curve gives a quadratic, and the number of "
                    "intersections is the number of real roots that quadratic has. The "
                    "discriminant $b^{2} - 4ac$ counts them: positive means two crossings, "
                    "zero means one — the line is TANGENT — and negative means the line misses "
                    "the curve entirely.",
        },
        {
            "kind": "teach",
            "title": "The SAT's vocabulary for each case",
            "beats": [
                "'Exactly one solution' and 'tangent to' both mean a zero discriminant.",
                "'Two distinct real solutions' means a positive discriminant.",
                "'No real solutions' and 'the graphs do not intersect' mean a negative one.",
                "Each phrasing turns into an equation or inequality in the unknown constant.",
            ],
        },
        {"kind": "worked", "title": "Finding the tangent constant", "problemId": "sat-ns2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which condition?",
            "prompt": "A line is tangent to a parabola. What does that say about the "
                      "discriminant of the quadratic you get by substituting?",
            "options": [
                "It equals zero",
                "It is positive",
                "It is negative",
                "It equals the slope of the line",
            ],
            "correctIndex": 0,
            "explanation": "Tangent means the two graphs touch at exactly one point, so the "
                           "quadratic has exactly one root — a repeated root — which happens "
                           "precisely when $b^{2} - 4ac = 0$. A positive discriminant would "
                           "mean the line cuts through at two points.",
            "check": ["Eq(4**2 - 4*1*4, 0)", "Eq(expand((x - 2)**2), x**2 - 4*x + 4)"],
        },
        {"kind": "worked", "title": "A line that misses entirely", "problemId": "sat-ns2-w2"},
        {
            "kind": "tip",
            "title": "Watch the sign inside the discriminant",
            "body": "When the constant term is an expression like $5 - c$ or $k - 2$, the "
                    "$-4ac$ term distributes over it. $-4(1)(5 - c)$ is $-20 + 4c$, and "
                    "$-4(2)(k - 2)$ is $-8k + 16$. Getting that sign wrong flips the "
                    "inequality and produces exactly the option the item was built around.",
        },
        {"kind": "worked", "title": "A range of constants", "problemId": "sat-ns2-w3"},
        {"kind": "tryIt", "title": "Your turn: count them", "problemId": "sat-ns2-t1"},
        {"kind": "tryIt", "title": "Your turn: find the tangent slope", "problemId": "sat-ns2-t2"},
        {"kind": "tryIt", "title": "Your turn: a line and a circle", "problemId": "sat-ns2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Substitute, collect into a quadratic, then read the discriminant.",
                "Positive: two intersections. Zero: tangent, one. Negative: none.",
                "'Tangent to' is the SAT's phrase for a zero discriminant.",
                "Distribute −4ac over an expression constant, and watch the sign.",
                "Completing the square gives the vertex, which often settles the count faster.",
            ],
        },
    ]

    return lesson(
        slug="counting-intersections",
        title="Counting Intersections with the Discriminant",
        concrete=(
            "A plane's descent path is a straight line and a hillside is a curve. Whether they "
            "meet twice, just graze once, or never touch is not a question about where — it is "
            "a question about how many, and one number answers it."
        ),
        objective=(
            "Use the discriminant to count the intersections of a line and a curve, and find "
            "the value or range of a constant that makes a line tangent, secant, or missing "
            "entirely."
        ),
        concept=[
            "**Skill card.** Still *Systems of equations in two variables*, in the **Advanced "
            "Math** domain. This is the harder half of the subtopic and it appears almost "
            "exclusively in the second module.",
            "Substituting the line into the curve produces a quadratic, and the number of "
            "intersections is the number of real roots that quadratic has. So you never have "
            "to solve anything: the discriminant $b^{2} - 4ac$ counts them. Positive gives two "
            "crossings, zero gives one, negative gives none.",
            "The SAT has a fixed vocabulary for the three cases. 'Exactly one solution' and "
            "'is tangent to' both mean a zero discriminant. 'Two distinct real solutions' means "
            "a positive one. 'No real solutions' and 'the graphs do not intersect' mean a "
            "negative one. Each phrasing becomes an equation or an inequality in the unknown "
            "constant.",
            "**The test's angle.** The sign inside the discriminant. When the constant term is "
            "itself an expression — $5 - c$, or $k - 2$ — the $-4ac$ distributes over it: "
            "$-4(1)(5 - c) = -20 + 4c$. Getting that wrong flips the inequality and lands "
            "exactly on the distractor. There is also often a faster route: completing the "
            "square gives the parabola's vertex, and comparing that height to a horizontal "
            "line settles the count in one glance.",
        ],
        key_idea=(
            "The discriminant of the substituted quadratic counts the intersections. Tangent "
            "means zero, two crossings mean positive, and no meeting means negative."
        ),
        facts=[
            fact(
                "Counting intersections",
                "b^{2} - 4ac > 0 \\;(\\text{two}), \\quad = 0 \\;(\\text{tangent}), \\quad < 0 \\;(\\text{none})",
                "Applied to the quadratic left after substituting the line into the curve.",
            ),
            fact(
                "Vertex form",
                "y = a(x - h)^{2} + k \\;\\Longrightarrow\\; \\text{vertex } (h, k)",
                "Completing the square often settles a count against a horizontal line faster "
                "than the discriminant does.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Mis-signing $-4ac$ when $c$ is an expression.",
                "$-4(1)(5 - c) = -20 + 4c$, not $-20 - 4c$. Distribute before simplifying.",
            ),
            mistake(
                "Reading 'tangent' as a positive discriminant.",
                "Tangent means the graphs TOUCH at exactly one point, which is a repeated "
                "root: discriminant zero.",
            ),
            mistake(
                "Forgetting to collect everything onto one side before reading $a$, $b$ and "
                "$c$.",
                "The discriminant is only meaningful for a quadratic written as "
                "$ax^{2} + bx + c = 0$.",
            ),
            mistake(
                "Solving for the intersections when only the count was asked for.",
                "The discriminant answers 'how many' in one line. Solving is slower and gives "
                "more chances to slip.",
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
        "sat-ns-p01",
        "$$y = x^{2}$$\n$$y = 4x$$\n"
        "What are the $x$-coordinates of the solutions?",
        "**Answer.** $x = 0$ and $x = 4$. Setting them equal gives $x^{2} - 4x = 0$, which "
        "factors as $x(x - 4) = 0$. Dividing by $x$ instead would lose the solution $x = 0$.",
        ["Eq(0**2, 4*0)", "Eq(4**2, 4*4)", "Eq(expand(x*(x - 4)), x**2 - 4*x)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ns-p02",
        "$$y = x^{2} - 1$$\n$$y = 3$$\n"
        "How many solutions does the system have?",
        "**Answer.** Two. Setting them equal gives $x^{2} = 4$, so $x = 2$ and $x = -2$; the "
        "points are $(2, 3)$ and $(-2, 3)$.",
        ["Eq(2**2 - 1, 3)", "Eq((-2)**2 - 1, 3)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ns-p03",
        "$$x^{2} + y^{2} = 20$$\n$$y = 2x$$\n"
        "What are the possible values of $x$?",
        "**Answer.** $x = 2$ and $x = -2$. Substituting gives $x^{2} + 4x^{2} = 20$, so "
        "$5x^{2} = 20$ and $x^{2} = 4$.",
        ["Eq(2**2 + (2*2)**2, 20)", "Eq((-2)**2 + (2*(-2))**2, 20)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-p04",
        "$$y = x^{2} + 5x + 9$$\n$$y = x + c$$\n"
        "For what value of the constant $c$ is the line tangent to the parabola?",
        "**Answer.** $5$. Setting them equal gives $x^{2} + 4x + (9 - c) = 0$, and tangency "
        "needs $16 - 4(9 - c) = 0$, so $16 - 36 + 4c = 0$ and $c = 5$. Then "
        "$x^{2} + 4x + 4 = (x + 2)^{2} = 0$ touches at $x = -2$.",
        [
            "Eq(4**2 - 4*1*(9 - 5), 0)",
            "Eq(expand((x + 2)**2), x**2 + 4*x + 4)",
            "Eq((-2)**2 + 5*(-2) + 9, -2 + 5)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ns-p05",
        "$$y = x^{2} - 2x + 6$$\n$$y = 2$$\n"
        "How many real solutions does the system have?",
        "**Answer.** None. Setting them equal gives $x^{2} - 2x + 4 = 0$ with discriminant "
        "$4 - 16 = -12 < 0$. Equivalently, the vertex is $(1, 5)$, so the parabola never "
        "drops to height $2$.",
        [
            "Eq((-2)**2 - 4*1*4, -12)",
            "-12 < 0",
            "Eq(expand((x - 1)**2 + 5), x**2 - 2*x + 6)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-p06",
        "$$y = x^{2} + x - 6$$\n$$y = 2x$$\n"
        "What is the sum of the $x$-coordinates of the solutions?",
        "**Answer.** $1$. Setting them equal gives $x^{2} - x - 6 = 0$, whose roots sum to "
        "$-\\frac{b}{a} = 1$. Factoring confirms it: $(x - 3)(x + 2) = 0$ gives $3$ and $-2$.",
        [
            "Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
            "Eq(3 + (-2), 1)",
            "Eq(3**2 + 3 - 6, 2*3)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-p07",
        "$$y = 3x^{2}$$\n$$y = 6x - 3$$\n"
        "How many solutions does the system have?",
        "**Answer.** Exactly one. Setting them equal gives $3x^{2} - 6x + 3 = 0$, or "
        "$3(x - 1)^{2} = 0$, whose only root is $x = 1$. The line is tangent at $(1, 3)$.",
        [
            "Eq((-6)**2 - 4*3*3, 0)",
            "Eq(3*1**2, 6*1 - 3)",
            "Eq(expand(3*(x - 1)**2), 3*x**2 - 6*x + 3)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-p08",
        "$$x^{2} + y^{2} = 25$$\n$$x = 3$$\n"
        "What are the solutions $(x, y)$?",
        "**Answer.** $(3, 4)$ and $(3, -4)$. Substituting gives $9 + y^{2} = 25$, so "
        "$y^{2} = 16$ and $y = \\pm 4$. Taking only the positive root loses one of the two "
        "points — a vertical line cuts a circle twice.",
        ["Eq(3**2 + 4**2, 25)", "Eq(3**2 + (-4)**2, 25)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-p09",
        "$$y = x^{2} + 8$$\n$$y = mx$$\n"
        "For what positive value of $m$ is the line tangent to the parabola?",
        "**Answer.** $m = 4\\sqrt{2}$. Setting them equal gives $x^{2} - mx + 8 = 0$, and "
        "tangency needs $m^{2} - 32 = 0$, so $m = \\pm 4\\sqrt{2}$ and the positive value is "
        "$4\\sqrt{2} \\approx 5.66$.",
        [
            "Eq((4*sqrt(2))**2 - 4*1*8, 0)",
            "Eq(simplify(sqrt(32) - 4*sqrt(2)), 0)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ns-p10",
        "$$y = -x^{2} + 4x$$\n$$y = x$$\n"
        "What is the product of the $x$-coordinates of the solutions?",
        "**Answer.** $0$. Setting them equal gives $-x^{2} + 3x = 0$, so $x(3 - x) = 0$ and "
        "the roots are $0$ and $3$, whose product is $0$. Dividing by $x$ would have lost the "
        "root that makes the product zero.",
        [
            "Eq(-(0**2) + 4*0, 0)",
            "Eq(-(3**2) + 4*3, 3)",
            "Eq(0*3, 0)",
        ],
        badges=_b("Medium"),
    ),
]

TEST = [
    problem(
        "sat-ns-x01",
        "$$y = x^{2} - 3$$\n$$y = 2x$$\n"
        "What are the $x$-coordinates of the solutions?",
        "**Answer.** $x = 3$ and $x = -1$. Setting them equal gives $x^{2} - 2x - 3 = 0$, "
        "which factors as $(x - 3)(x + 1) = 0$.",
        [
            "Eq(3**2 - 3, 2*3)",
            "Eq((-1)**2 - 3, 2*(-1))",
            "Eq(expand((x - 3)*(x + 1)), x**2 - 2*x - 3)",
        ],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ns-x02",
        "$$x^{2} + y^{2} = 13$$\n$$y = x + 1$$\n"
        "What is the sum of the $x$-coordinates of the solutions?",
        "**Answer.** $-1$. Substituting gives $x^{2} + x^{2} + 2x + 1 = 13$, so "
        "$2x^{2} + 2x - 12 = 0$ and $x^{2} + x - 6 = 0$. The roots sum to $-1$; factoring "
        "gives $x = 2$ and $x = -3$.",
        [
            "Eq(2**2 + 3**2, 13)",
            "Eq((-3)**2 + (-2)**2, 13)",
            "Eq(2 + (-3), -1)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-x03",
        "$$y = x^{2} + 6x + 13$$\n$$y = 4$$\n"
        "How many real solutions does the system have?",
        "**Answer.** Exactly one. Setting them equal gives $x^{2} + 6x + 9 = 0$, whose "
        "discriminant is $36 - 36 = 0$ — a repeated root at $x = -3$. Completing the square "
        "shows why: the parabola is $y = (x + 3)^{2} + 4$, with vertex $(-3, 4)$, and the "
        "line $y = 4$ passes exactly through that vertex.",
        [
            "Eq(6**2 - 4*1*9, 0)",
            "Eq((-3)**2 + 6*(-3) + 13, 4)",
            "Eq(expand((x + 3)**2 + 4), x**2 + 6*x + 13)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-x04",
        "$$y = 2x^{2} + 3$$\n$$y = 4x + k$$\n"
        "For what value of the constant $k$ is the line tangent to the parabola?",
        "**Answer.** $k = 1$. Setting them equal gives $2x^{2} - 4x + (3 - k) = 0$, and "
        "tangency needs $16 - 8(3 - k) = 0$, so $16 - 24 + 8k = 0$ and $k = 1$. Then "
        "$2x^{2} - 4x + 2 = 2(x - 1)^{2} = 0$ touches at $(1, 5)$.",
        [
            "Eq((-4)**2 - 4*2*(3 - 1), 0)",
            "Eq(2*1**2 + 3, 4*1 + 1)",
            "Eq(expand(2*(x - 1)**2), 2*x**2 - 4*x + 2)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ns-x05",
        "$$y = x^{2} + 2x$$\n$$y = 3x + 6$$\n"
        "What is the product of the $x$-coordinates of the solutions?",
        "**Answer.** $-6$. Setting them equal gives $x^{2} - x - 6 = 0$, whose roots multiply "
        "to $\\frac{c}{a} = -6$. Factoring gives $x = 3$ and $x = -2$.",
        [
            "Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
            "Eq(3*(-2), -6)",
            "Eq(3**2 + 2*3, 3*3 + 6)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-x06",
        "$$x^{2} + y^{2} = 4$$\n$$y = 5$$\n"
        "How many solutions does the system have?",
        "**Answer.** None. The circle has radius $2$, so no point on it reaches height $5$. "
        "Algebraically, $x^{2} = 4 - 25 = -21$, which no real $x$ satisfies.",
        ["Eq(4 - 25, -21)", "-21 < 0", "2 < 5"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ns-x07",
        "$$y = x^{2} - 4x + c$$\n$$y = -2x + 1$$\n"
        "For what values of $c$ does the system have two distinct real solutions?",
        "**Answer.** $c < 2$. Setting them equal gives $x^{2} - 2x + (c - 1) = 0$, and two "
        "distinct solutions need a positive discriminant: $4 - 4(c - 1) > 0$, so "
        "$4 - 4c + 4 > 0$ and $c < 2$. Check with $c = 0$: the discriminant is $4 + 4 = 8 > 0$; "
        "with $c = 5$ it is $4 - 16 = -12 < 0$.",
        [
            "Eq((-2)**2 - 4*1*(0 - 1), 8)",
            "8 > 0",
            "Eq((-2)**2 - 4*1*(5 - 1), -12)",
            "-12 < 0",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ns-x08",
        "$$y = x^{2}$$\n$$y = 6x - 9$$\n"
        "What is the solution $(x, y)$?",
        "**Answer.** $(3, 9)$. Setting them equal gives $x^{2} - 6x + 9 = 0$, or "
        "$(x - 3)^{2} = 0$, a repeated root at $x = 3$. The line is tangent to the parabola "
        "at the single point $(3, 9)$.",
        [
            "Eq(3**2, 6*3 - 9)",
            "Eq((-6)**2 - 4*1*9, 0)",
            "Eq(expand((x - 3)**2), x**2 - 6*x + 9)",
        ],
        badges=_b("Medium"),
    ),
]


def main():
    lessons = [lesson_solving(), lesson_counting()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Systems of Equations in Two Variables",
        3,
        "A line meeting a parabola or a circle: substituting into the curve, solving the "
        "quadratic that results, and using the discriminant to count the intersections — or to "
        "find the constant that makes the line tangent.",
        "Quadratics from Unit 2, and linear systems from the Algebra course.",
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
