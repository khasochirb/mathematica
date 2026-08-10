#!/usr/bin/env python3
"""SAT Math — Algebra, Unit 4: Systems of two linear equations in two variables.

Builds data/genmath/sat/systems-of-linear-equations.json. Three lessons:
solving one, counting its solutions, and finding one inside a word problem.

Run: python3 scripts/sat/build_alg_4.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "systems-of-linear-equations"
TAG = {"text": "sat-systems-linear", "mono": True}


def _b(level):
    return [TAG, {"text": level}]


# ===========================================================================
# Lesson 1 — substitution and elimination
# ===========================================================================

def lesson_solving():
    worked = [
        problem(
            "sat-l4a-w1",
            "$$3x + 2y = 19$$\n$$y = x - 3$$\n"
            "What is the solution $(x, y)$ to the system of equations above?",
            "**Answer.** $(5, 2)$.  \n"
            "The second equation already has $y$ alone, so substitution is free. Replace $y$ "
            "in the first equation by $x - 3$:\n"
            "$$3x + 2(x - 3) = 19$$\n"
            "$$3x + 2x - 6 = 19$$\n"
            "$$5x = 25$$\n"
            "$$x = 5$$\n"
            "Now go back to the SIMPLER equation for $y$:\n"
            "$$y = 5 - 3 = 2$$\n"
            "Check both equations, not just one: $3(5) + 2(2) = 19$ and $2 = 5 - 3$.  \n"
            "Stopping at $x = 5$ is the classic half-answer. A system in two variables has a "
            "two-number solution, and $5$ alone will be sitting in the options.",
            [
                "Eq(3*5 + 2*2, 19)",
                "Eq(2, 5 - 3)",
                "Eq(solve([Eq(3*x + 2*y, 19), Eq(y, x - 3)], [x, y])[x], 5)",
                "Eq(solve([Eq(3*x + 2*y, 19), Eq(y, x - 3)], [x, y])[y], 2)",
            ],
        ),
        problem(
            "sat-l4a-w2",
            "$$4x + 3y = 31$$\n$$4x - 5y = -1$$\n"
            "What is the value of $y$?",
            "**Answer.** $4$.  \n"
            "The $x$ terms are already identical, so subtracting one equation from the other "
            "eliminates $x$ in a single move:\n"
            "$$(4x + 3y) - (4x - 5y) = 31 - (-1)$$\n"
            "Distribute the subtraction across BOTH terms of the second bracket — this is "
            "where the sign error lives:\n"
            "$$8y = 32$$\n"
            "$$y = 4$$\n"
            "The question asks only for $y$, so you are done. (For the record $x = 4.75$, "
            "which is also on the option list.)  \n"
            "Check: $4(4.75) + 3(4) = 19 + 12 = 31$.",
            [
                "Eq(4*Rational(19,4) + 3*4, 31)",
                "Eq(4*Rational(19,4) - 5*4, -1)",
                "Eq(solve([Eq(4*x + 3*y, 31), Eq(4*x - 5*y, -1)], [x, y])[y], 4)",
            ],
        ),
        problem(
            "sat-l4a-w3",
            "$$2x + 3y = 12$$\n$$5x - 2y = 11$$\n"
            "What is the value of $x + y$?",
            "**Answer.** $5$.  \n"
            "Neither variable matches, so scale first. Multiply the first equation by $2$ and "
            "the second by $3$ to make the $y$ terms opposites:\n"
            "$$4x + 6y = 24$$\n"
            "$$15x - 6y = 33$$\n"
            "Now ADD them, because the $y$ terms cancel:\n"
            "$$19x = 57 \\;\\Longrightarrow\\; x = 3$$\n"
            "Substitute back into the simpler original:\n"
            "$$2(3) + 3y = 12 \\;\\Longrightarrow\\; 3y = 6 \\;\\Longrightarrow\\; y = 2$$\n"
            "So $x + y = 5$.  \n"
            "Check both: $2(3) + 3(2) = 12$ and $5(3) - 2(2) = 11$.  \n"
            "The SAT often asks for a COMBINATION like $x + y$ rather than either variable. "
            "Sometimes there is a shortcut — here adding the two originals gives "
            "$7x + y = 23$, which is not $x + y$, so the full solve was genuinely needed.",
            [
                "Eq(2*3 + 3*2, 12)",
                "Eq(5*3 - 2*2, 11)",
                "Eq(3 + 2, 5)",
                "Eq(solve([Eq(2*x + 3*y, 12), Eq(5*x - 2*y, 11)], [x, y])[x], 3)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l4a-t1",
            "$$y = 2x + 1$$\n$$3x + y = 16$$\n"
            "What is the value of $x$?",
            "**Answer.** $3$. Substitute: $3x + (2x + 1) = 16$, so $5x = 15$ and $x = 3$. Then "
            "$y = 7$, and $3(3) + 7 = 16$ checks out.",
            ["Eq(3*3 + (2*3 + 1), 16)", "Eq(2*3 + 1, 7)"],
        ),
        problem(
            "sat-l4a-t2",
            "$$x + y = 10$$\n$$x - y = 2$$\n"
            "What is the solution $(x, y)$?",
            "**Answer.** $(6, 4)$. Adding the two equations eliminates $y$: $2x = 12$, so "
            "$x = 6$, and then $y = 4$. Check: $6 + 4 = 10$ and $6 - 4 = 2$.",
            ["Eq(6 + 4, 10)", "Eq(6 - 4, 2)"],
        ),
        problem(
            "sat-l4a-t3",
            "$$3x + 4y = 26$$\n$$5x - 4y = 6$$\n"
            "What is the value of $x$?",
            "**Answer.** $4$. The $y$ terms are already opposites, so add: $8x = 32$ and "
            "$x = 4$. Then $4y = 26 - 12 = 14$, so $y = 3.5$.",
            ["Eq(3*4 + 4*Rational(7,2), 26)", "Eq(5*4 - 4*Rational(7,2), 6)"],
        ),
        problem(
            "sat-l4a-t4",
            "$$2x - y = 7$$\n$$3x + 2y = 21$$\n"
            "What is the value of $x - y$?",
            "**Answer.** $2$. Double the first equation to get $4x - 2y = 14$ and add it to "
            "the second: $7x = 35$, so $x = 5$. Then $y = 2(5) - 7 = 3$, and $x - y = 2$.  \n"
            "Check: $2(5) - 3 = 7$ and $3(5) + 2(3) = 21$.",
            ["Eq(2*5 - 3, 7)", "Eq(3*5 + 2*3, 21)", "Eq(5 - 3, 2)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Systems of two linear equations in two variables",
            "beats": [
                "Domain: Algebra — 13 to 15 of the 44 questions on the Math section.",
                "Expect 2 or 3 questions, spread across easy, medium and hard.",
                "Prerequisites: solving one linear equation, and slope from Unit 2.",
                "Bluebook's built-in Desmos graphs a system in seconds — always an option.",
            ],
        },
        {
            "kind": "teach",
            "title": "A solution satisfies BOTH equations",
            "body": "Two equations in two unknowns. A solution is a pair $(x, y)$ that makes "
                    "both true at once — geometrically, the point where the two lines cross. "
                    "That is why checking one equation is not enough: a pair can satisfy the "
                    "first and fail the second, and the SAT builds distractors from exactly "
                    "those pairs.",
        },
        {
            "kind": "systemGraph",
            "title": "Two lines, one crossing",
            "teach": "Drag either line and watch the intersection move. That single point is "
                     "the solution of the system — every algebraic method here is just a way "
                     "of computing its coordinates without drawing anything.",
            "config": {"m1": 1, "b1": -3, "m2": -1.5, "b2": 9.5, "interactive": True, "min": -6, "max": 10},
        },
        {
            "kind": "teach",
            "title": "Pick the method the system hands you",
            "beats": [
                "One equation already solved for a variable → substitution, no setup needed.",
                "Matching or opposite coefficients → elimination by adding or subtracting.",
                "Neither → scale one or both equations first, then eliminate.",
                "Ugly coefficients and MCQ options → graph both in Desmos and read the crossing.",
            ],
        },
        {"kind": "worked", "title": "Substitution when it is free", "problemId": "sat-l4a-w1"},
        {
            "kind": "tapQuestion",
            "title": "Add or subtract?",
            "prompt": "For the system $5x + 2y = 9$ and $5x - 2y = 11$, which single move "
                      "eliminates a variable?",
            "options": [
                "Add the two equations, eliminating $y$",
                "Subtract the second from the first, eliminating $y$",
                "Add the two equations, eliminating $x$",
                "Multiply the first by $2$, then subtract",
            ],
            "correctIndex": 0,
            "explanation": "The $y$ terms are $+2y$ and $-2y$: opposites, so ADDING cancels "
                           "them, giving $10x = 20$ and $x = 2$. Subtracting would cancel the "
                           "$x$ terms instead, not the $y$ terms. Opposites add; identical "
                           "terms subtract.",
            "check": [
                "Eq(5*2 + 2*Rational(-1,2), 9)",
                "Eq(5*2 - 2*Rational(-1,2), 11)",
                "Eq((5*x + 2*y) + (5*x - 2*y), 10*x)",
            ],
        },
        {"kind": "worked", "title": "Elimination when a term already matches", "problemId": "sat-l4a-w2"},
        {
            "kind": "tip",
            "title": "Read what the question wants",
            "body": "The SAT very often asks for something other than $x$: the value of $y$, of "
                    "$x + y$, of $2x - 3y$. Sometimes a combination falls out of the two "
                    "equations directly without solving — adding them, or subtracting them, "
                    "occasionally lands on exactly the expression asked for. Always check for "
                    "that before grinding through both variables.",
        },
        {"kind": "worked", "title": "Scaling before eliminating", "problemId": "sat-l4a-w3"},
        {"kind": "tryIt", "title": "Your turn: substitution", "problemId": "sat-l4a-t1"},
        {"kind": "tryIt", "title": "Your turn: add to eliminate", "problemId": "sat-l4a-t2"},
        {"kind": "tryIt", "title": "Your turn: opposites already", "problemId": "sat-l4a-t3"},
        {"kind": "tryIt", "title": "Your turn: scale, then add", "problemId": "sat-l4a-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "A solution must satisfy BOTH equations — always check both.",
                "Opposite coefficients add away; identical coefficients subtract away.",
                "Subtracting an equation flips the sign of every term in it, not just the first.",
                "After finding one variable, substitute into the simpler equation for the other.",
                "Check what is being asked: x, y, or a combination like x + y.",
            ],
        },
    ]

    return lesson(
        slug="solving-systems",
        title="Solving a System: Substitution and Elimination",
        concrete=(
            "Six coffees and two teas cost $\\$32$; three coffees and four teas cost $\\$28$. "
            "Neither receipt alone tells you the price of a coffee, but the two together pin "
            "both prices exactly. That is a system — two facts, two unknowns, one answer."
        ),
        objective=(
            "Solve a two-by-two linear system by substitution or elimination, choosing the "
            "method the system's own shape makes cheapest, and answer for whichever quantity "
            "is asked."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Systems of two linear equations in "
            "two variables*, in the **Algebra** domain. Expect two or three questions across "
            "the difficulty range. Bluebook's built-in Desmos will graph a system in seconds, "
            "so there is always a fallback — but the algebra is usually faster.",
            "A solution is a pair $(x, y)$ making BOTH equations true. Geometrically it is the "
            "point where the two lines cross. Checking only one equation is the classic "
            "mistake, because the test builds its distractors from pairs that satisfy one "
            "equation and fail the other.",
            "Substitution: when one equation already gives a variable alone, put that "
            "expression into the other equation. Elimination: when a variable's coefficients "
            "match, subtract the equations; when they are opposites, add them. When neither is "
            "true, multiply one or both equations by a constant until one of those cases "
            "appears. Subtracting is where signs get lost — the minus applies to every term in "
            "the bracket.",
            "**The test's angle.** The SAT rarely wants $x$. It asks for $y$, or $x + y$, or "
            "$3x - y$, precisely because a student who stops at the first variable has an "
            "answer that is listed and wrong. Sometimes a combination is reachable directly: "
            "adding $2x + 3y = 12$ to $5x - 2y = 11$ never gives $x + y$, but for other pairs "
            "it does, so it costs nothing to look before solving.",
        ],
        key_idea=(
            "One point satisfies both equations. Substitute when a variable is already alone; "
            "eliminate when coefficients match or oppose; scale first when they do not."
        ),
        facts=[
            fact(
                "Elimination",
                "\\begin{cases} ax + by = c \\\\ dx + by = e \\end{cases} \\;\\Longrightarrow\\; (a - d)x = c - e",
                "Identical $y$ terms disappear on subtraction. Opposite terms disappear on "
                "addition.",
            ),
            fact(
                "Substitution",
                "y = mx + k \\;\\Longrightarrow\\; ax + b(mx + k) = c",
                "Replace the variable, keeping the brackets so the coefficient reaches every "
                "term inside.",
            ),
            fact(
                "Scaling before eliminating",
                "p(ax + by) = pc \\text{ preserves the equation}",
                "Multiplying a whole equation by any non-zero number leaves the same line, so "
                "you may scale freely to make coefficients match.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Losing a sign when subtracting one equation from another.",
                "$(4x + 3y) - (4x - 5y)$ is $8y$, not $-2y$. The minus reaches every term in "
                "the second bracket.",
            ),
            mistake(
                "Answering with $x$ when the question asked for $y$ or for $x + y$.",
                "The other variable is always among the options. Re-read the final sentence "
                "before choosing.",
            ),
            mistake(
                "Checking the answer in only one of the two equations.",
                "A pair can satisfy one equation and fail the other. Substitute into both.",
            ),
            mistake(
                "Substituting the second variable back into the harder equation.",
                "Use the simpler one — usually the equation already solved for a variable. "
                "Less arithmetic means fewer slips.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — number of solutions
# ===========================================================================

def lesson_count():
    worked = [
        problem(
            "sat-l4b-w1",
            "$$2x + 6y = 14$$\n$$kx + 9y = 21$$\n"
            "In the system above, $k$ is a constant. If the system has infinitely many "
            "solutions, what is the value of $k$?",
            "**Answer.** $3$.  \n"
            "Infinitely many solutions means the two equations describe the SAME line, so one "
            "must be a constant multiple of the other. Compare the terms that are already "
            "known. The $y$ terms go from $6$ to $9$, and the constants from $14$ to $21$:\n"
            "$$\\frac{9}{6} = \\frac{3}{2}, \\qquad \\frac{21}{14} = \\frac{3}{2}$$\n"
            "Both scale by the same factor, which is what makes infinitely many solutions "
            "possible at all. The $x$ terms must scale by that factor too:\n"
            "$$k = \\frac{3}{2} \\times 2 = 3$$\n"
            "Check: multiplying the first equation by $\\frac{3}{2}$ gives exactly "
            "$3x + 9y = 21$.  \n"
            "Had the constants NOT scaled by the same factor, no value of $k$ would give "
            "infinitely many solutions — the best available would be parallel lines and no "
            "solution at all.",
            [
                "Eq(Rational(9,6), Rational(3,2))",
                "Eq(Rational(21,14), Rational(3,2))",
                "Eq(Rational(3,2)*2, 3)",
                "Eq(Rational(3,2)*(2*x + 6*y), 3*x + 9*y)",
            ],
        ),
        problem(
            "sat-l4b-w2",
            "$$y = 4x - 7$$\n$$2y = 8x + c$$\n"
            "In the system above, $c$ is a constant. For what value of $c$ does the system "
            "have NO solution?",
            "**Answer.** Any value other than $-14$.  \n"
            "Put the second equation into the same shape as the first by halving it:\n"
            "$$y = 4x + \\frac{c}{2}$$\n"
            "Both lines now have slope $4$, so they are parallel or identical whatever $c$ is. "
            "They are IDENTICAL — infinitely many solutions — exactly when the intercepts "
            "agree:\n"
            "$$\\frac{c}{2} = -7 \\;\\Longrightarrow\\; c = -14$$\n"
            "For every other $c$ the lines are parallel and distinct, so there is no solution. "
            "There is no value of $c$ producing exactly one solution, because the slopes can "
            "never differ.  \n"
            "On the real test this appears as 'which of the following CANNOT be the value of "
            "$c$?', and the answer is $-14$.",
            [
                "Eq(solve(Eq(2*y, 8*x - 14), y)[0], 4*x - 7)",
                "Ne(solve(Eq(2*y, 8*x + 6), y)[0], 4*x - 7)",
            ],
        ),
        problem(
            "sat-l4b-w3",
            "How many solutions does the system $3x - y = 5$ and $6x - 2y = 1$ have?",
            "**Answer.** None.  \n"
            "Compare the two equations by scaling. Doubling the first gives\n"
            "$$6x - 2y = 10$$\n"
            "The second equation says the same left-hand side equals $1$. One expression "
            "cannot equal both $10$ and $1$, so no pair $(x, y)$ can satisfy both — the system "
            "has no solution.  \n"
            "In slope form: $y = 3x - 5$ and $y = 3x - \\frac{1}{2}$. Equal slopes, different "
            "intercepts, parallel lines that never meet.  \n"
            "The test is checking whether you noticed the left sides were proportional before "
            "you started eliminating. Grinding elimination here produces $0 = 9$, which is the "
            "same conclusion reached the long way.",
            [
                "Eq(2*(3*x - y), 6*x - 2*y)",
                "Ne(10, 1)",
                "Eq(solve(Eq(3*x - y, 5), y)[0], 3*x - 5)",
                "Eq(solve(Eq(6*x - 2*y, 1), y)[0], 3*x - Rational(1,2))",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l4b-t1",
            "$$x + 3y = 8$$\n$$2x + my = 16$$\n"
            "For what value of $m$ does the system have infinitely many solutions?",
            "**Answer.** $6$. The second equation must be the first scaled by $2$, since the "
            "$x$ terms go from $1$ to $2$ and the constants from $8$ to $16$. So $m = 6$.",
            ["Eq(2*(x + 3*y), 2*x + 6*y)", "Eq(2*8, 16)"],
        ),
        problem(
            "sat-l4b-t2",
            "How many solutions does the system $y = 2x + 1$ and $y = 2x - 4$ have?",
            "**Answer.** None. Both lines have slope $2$ but different intercepts, so they are "
            "parallel and never meet. Setting the right sides equal gives $1 = -4$, which is "
            "false.",
            ["Ne(1, -4)", "Eq(2, 2)"],
        ),
        problem(
            "sat-l4b-t3",
            "$$5x - 2y = 9$$\n$$ax + 4y = 7$$\n"
            "For which value of $a$ does the system have NO solution?",
            "**Answer.** $-10$. No solution needs parallel lines: equal slopes, different "
            "intercepts. The second equation is the first scaled by $-2$ in its variable terms "
            "when $a = -10$, since $-2 \\times 5 = -10$ and $-2 \\times (-2) = 4$. The "
            "constants do not follow — $-2 \\times 9 = -18 \\ne 7$ — so the lines are parallel "
            "and distinct, which is exactly no solution.",
            [
                "Eq(-2*5, -10)",
                "Eq(-2*(-2), 4)",
                "Ne(-2*9, 7)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Three pictures, three answers",
            "beats": [
                "Lines that cross → exactly one solution. Different slopes.",
                "Parallel lines → no solution. Same slope, different intercept.",
                "One line drawn twice → infinitely many. Same slope AND same intercept.",
                "A two-by-two linear system can never have exactly two solutions.",
            ],
        },
        {
            "kind": "systemGraph",
            "title": "Slide the intercept, lose the crossing",
            "teach": "Set both slopes equal and the crossing disappears — that is 'no "
                     "solution'. Then match the intercepts too and the lines merge into one, "
                     "which is 'infinitely many'. Every counting question is one of these two "
                     "pictures.",
            "config": {"m1": 3, "b1": -5, "m2": 3, "b2": -0.5, "interactive": True, "min": -6, "max": 8},
        },
        {
            "kind": "teach",
            "title": "Compare the two equations, do not solve them",
            "body": "Write both equations in the same order, $ax + by = c$. Infinitely many "
                    "solutions means one equation is the other multiplied throughout by a "
                    "single constant — all three of $a$, $b$ and $c$ scale by the same factor. "
                    "No solution means $a$ and $b$ scale but $c$ does not. One solution means "
                    "$a$ and $b$ do not scale by a common factor at all. Finding that factor "
                    "is the entire method.",
        },
        {"kind": "worked", "title": "Infinitely many: everything scales", "problemId": "sat-l4b-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which picture?",
            "prompt": "The system $y = 5x + 2$ and $3y = 15x + 6$ has how many solutions?",
            "options": [
                "Infinitely many",
                "Exactly one",
                "None",
                "Exactly three",
            ],
            "correctIndex": 0,
            "explanation": "Dividing the second equation by $3$ gives $y = 5x + 2$, which is "
                           "the first equation exactly. One line drawn twice, so every point on "
                           "it is a solution. A linear system can never have exactly three.",
            "check": ["Eq(solve(Eq(3*y, 15*x + 6), y)[0], 5*x + 2)"],
        },
        {"kind": "worked", "title": "No solution: the constants disagree", "problemId": "sat-l4b-w2"},
        {
            "kind": "tip",
            "title": "Scale the whole equation, including the constant",
            "body": "When testing whether one equation is a multiple of another, the constant "
                    "term counts. In $2x + 6y = 14$ and $3x + 9y = 21$ every term scales by "
                    "$\\frac{3}{2}$ — same line. Change the $21$ to anything else and the "
                    "lines become parallel instead. Students who compare only the variable "
                    "terms answer 'infinitely many' to a system that has none.",
        },
        {"kind": "worked", "title": "Spotting parallel lines early", "problemId": "sat-l4b-w3"},
        {"kind": "tryIt", "title": "Your turn: find the scale factor", "problemId": "sat-l4b-t1"},
        {"kind": "tryIt", "title": "Your turn: count them", "problemId": "sat-l4b-t2"},
        {"kind": "tryIt", "title": "Your turn: force no solution", "problemId": "sat-l4b-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Different slopes: one solution. Same slope, different intercept: none.",
                "Same slope and same intercept: infinitely many — one line written twice.",
                "For infinitely many, EVERY term including the constant scales by one factor.",
                "For no solution, the variable terms scale but the constant does not.",
                "Never solve a counting question — compare the two equations term by term.",
            ],
        },
    ]

    return lesson(
        slug="number-of-solutions-of-a-system",
        title="One Solution, None, or Infinitely Many",
        concrete=(
            "Two roads on a map either cross once, run alongside each other forever, or turn "
            "out to be the same road with two names. There is no fourth option, and you can "
            "tell which case you are in by looking at the two equations without solving "
            "anything at all."
        ),
        objective=(
            "Decide how many solutions a two-by-two linear system has, and find the value of "
            "an unknown constant that forces no solution or infinitely many."
        ),
        concept=[
            "**Skill card.** Still *Systems of two linear equations in two variables*, in the "
            "**Algebra** domain — the harder half. These items look intimidating because of "
            "the unknown constant and take about twenty seconds once you know what to compare.",
            "Two lines can cross once, never, or everywhere. Crossing once means different "
            "slopes and one solution. Never meeting means equal slopes with different "
            "intercepts — parallel, no solution. Meeting everywhere means the two equations "
            "describe the same line — infinitely many solutions. There is no other case, and a "
            "linear system can never have exactly two solutions.",
            "The test is a comparison, not a calculation. Write both equations as "
            "$ax + by = c$. If one equation is the other multiplied throughout by a single "
            "constant — $a$, $b$ AND $c$ all scaling by the same factor — the system has "
            "infinitely many solutions. If $a$ and $b$ scale but $c$ does not, the lines are "
            "parallel and there is no solution. If $a$ and $b$ do not share a common factor at "
            "all, there is exactly one solution.",
            "**The test's angle.** The trap is comparing only the variable terms. In "
            "$2x + 6y = 14$ paired with $3x + 9y = 20$, the left sides scale perfectly by "
            "$\\frac{3}{2}$ — but $\\frac{3}{2} \\times 14 = 21$, not $20$, so the lines are "
            "parallel and the system has NO solutions rather than infinitely many. Always "
            "scale the constant too.",
        ],
        key_idea=(
            "Compare the two equations rather than solving them. All three terms scaling by "
            "one factor means infinitely many; the variable terms scaling but not the constant "
            "means none; no common factor means exactly one."
        ),
        facts=[
            fact(
                "The three cases",
                "\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2} \\;\\text{(one)}, \\quad \\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2} \\;\\text{(none)}, \\quad \\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} \\;\\text{(infinitely many)}",
                "Three ratios settle every counting question on this subtopic.",
            ),
            fact(
                "In slope form",
                "m_1 \\ne m_2 \\;\\text{(one)}, \\quad m_1 = m_2,\\, b_1 \\ne b_2 \\;\\text{(none)}, \\quad m_1 = m_2,\\, b_1 = b_2 \\;\\text{(infinitely many)}",
                "The same three cases seen as lines. Use whichever form the question is "
                "already written in.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Comparing only the variable terms when testing for infinitely many solutions.",
                "The constant must scale by the same factor. If it does not, the system has NO "
                "solution instead.",
            ),
            mistake(
                "Solving the system to find out how many solutions it has.",
                "Elimination on a degenerate system gives $0 = 0$ or $0 = 9$, which is the "
                "right answer the slow way. Comparing coefficients gets there in one line.",
            ),
            mistake(
                "Thinking 'no solution' means $x = 0$ and $y = 0$.",
                "$(0, 0)$ is a perfectly good solution when it satisfies both equations. No "
                "solution means no pair whatsoever works.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 3 — systems from word problems
# ===========================================================================

def lesson_words():
    worked = [
        problem(
            "sat-l4c-w1",
            "A theatre sells adult tickets for $\\$12$ and child tickets for $\\$7$. On one "
            "evening it sold $260$ tickets for a total of $\\$2{,}570$. How many adult tickets "
            "were sold?",
            "**Answer.** $150$.  \n"
            "Two unknowns need two equations, and the paragraph supplies exactly two facts. "
            "Let $a$ be adult tickets and $c$ child tickets.  \n"
            "The COUNT of tickets:\n"
            "$$a + c = 260$$\n"
            "The MONEY, which weights each ticket by its price:\n"
            "$$12a + 7c = 2570$$\n"
            "Substitute $c = 260 - a$ into the money equation:\n"
            "$$12a + 7(260 - a) = 2570$$\n"
            "$$12a + 1820 - 7a = 2570$$\n"
            "$$5a = 750$$\n"
            "$$a = 150$$\n"
            "So $110$ child tickets were sold. Check the money: "
            "$12(150) + 7(110) = 1800 + 770 = 2570$.  \n"
            "Nearly every SAT system word problem is this shape: one equation counting things, "
            "one equation weighting them by price, weight, or time.",
            [
                "Eq(150 + 110, 260)",
                "Eq(12*150 + 7*110, 2570)",
                "Eq(solve([Eq(a + c, 260), Eq(12*a + 7*c, 2570)], [a, c])[a], 150)",
            ],
        ),
        problem(
            "sat-l4c-w2",
            "A chemist mixes a $20\\%$ acid solution with a $50\\%$ acid solution to make "
            "$600$ millilitres of a $30\\%$ solution. How many millilitres of the $50\\%$ "
            "solution are used?",
            "**Answer.** $200$ millilitres.  \n"
            "Let $x$ be the millilitres of $20\\%$ solution and $y$ the millilitres of $50\\%$. "
            "The VOLUME equation:\n"
            "$$x + y = 600$$\n"
            "The ACID equation — each solution contributes its own percentage:\n"
            "$$0.20x + 0.50y = 0.30(600) = 180$$\n"
            "Substitute $x = 600 - y$:\n"
            "$$0.20(600 - y) + 0.50y = 180$$\n"
            "$$120 - 0.20y + 0.50y = 180$$\n"
            "$$0.30y = 60$$\n"
            "$$y = 200$$\n"
            "So $400$ mL of the weak solution and $200$ mL of the strong one. Check the acid: "
            "$0.20(400) + 0.50(200) = 80 + 100 = 180$, which is $30\\%$ of $600$.  \n"
            "Adding the percentages — treating $20\\% + 50\\%$ as meaningful — is the error "
            "the item is built on. Percentages of different amounts never add directly.",
            [
                "Eq(400 + 200, 600)",
                "Eq(Rational(20,100)*400 + Rational(50,100)*200, 180)",
                "Eq(Rational(30,100)*600, 180)",
            ],
        ),
        problem(
            "sat-l4c-w3",
            "At a market, $3$ kilograms of apples and $2$ kilograms of pears cost $\\$17$. Two "
            "kilograms of apples and $5$ kilograms of pears cost $\\$26$. What is the cost of "
            "one kilogram of apples?",
            "**Answer.** $\\$3$.  \n"
            "Let $a$ and $p$ be the per-kilogram prices in dollars:\n"
            "$$3a + 2p = 17$$\n"
            "$$2a + 5p = 26$$\n"
            "Neither variable matches, so scale to make the pear terms equal. Multiply the "
            "first by $5$ and the second by $2$:\n"
            "$$15a + 10p = 85$$\n"
            "$$4a + 10p = 52$$\n"
            "Subtract the second from the first, so the pear terms cancel:\n"
            "$$11a = 33$$\n"
            "$$a = 3$$\n"
            "Substitute back into the first original equation:\n"
            "$$9 + 2p = 17 \\;\\Longrightarrow\\; p = 4$$\n"
            "Check the second receipt, which was not used to find $a$: "
            "$2(3) + 5(4) = 6 + 20 = 26$.  \n"
            "Two receipts, two prices. Note that the question asks for apples — pears at "
            "$\\$4$ will be on the option list.",
            [
                "Eq(3*3 + 2*4, 17)",
                "Eq(2*3 + 5*4, 26)",
                "Eq(solve([Eq(3*a + 2*p, 17), Eq(2*a + 5*p, 26)], [a, p])[a], 3)",
                "Eq(solve([Eq(3*a + 2*p, 17), Eq(2*a + 5*p, 26)], [a, p])[p], 4)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l4c-t1",
            "A shop sells notebooks for $\\$4$ and pens for $\\$2$. A customer buys $9$ items "
            "for $\\$26$. How many notebooks did they buy?",
            "**Answer.** $4$. With $n$ notebooks and $p$ pens: $n + p = 9$ and $4n + 2p = 26$. "
            "Substituting $p = 9 - n$ gives $4n + 18 - 2n = 26$, so $2n = 8$ and $n = 4$. "
            "Check: $4(4) + 2(5) = 26$.",
            ["Eq(4 + 5, 9)", "Eq(4*4 + 2*5, 26)"],
        ),
        problem(
            "sat-l4c-t2",
            "Two numbers have a sum of $54$ and a difference of $16$. What is the larger "
            "number?",
            "**Answer.** $35$. With $x + y = 54$ and $x - y = 16$, adding gives $2x = 70$, so "
            "$x = 35$ and $y = 19$. Check: $35 + 19 = 54$ and $35 - 19 = 16$.",
            ["Eq(35 + 19, 54)", "Eq(35 - 19, 16)"],
        ),
        problem(
            "sat-l4c-t3",
            "A boat travels $60$ kilometres downstream in $3$ hours and the same $60$ "
            "kilometres upstream in $5$ hours. What is the speed of the current, in kilometres "
            "per hour?",
            "**Answer.** $4$. Let $b$ be the boat's speed in still water and $c$ the current. "
            "Downstream the speeds add, upstream they subtract:\n"
            "$$b + c = \\frac{60}{3} = 20, \\qquad b - c = \\frac{60}{5} = 12$$\n"
            "Subtracting gives $2c = 8$, so $c = 4$ and $b = 16$. Check: "
            "$60 \\div 20 = 3$ hours and $60 \\div 12 = 5$ hours.",
            [
                "Eq(Rational(60,3), 20)",
                "Eq(Rational(60,5), 12)",
                "Eq(16 + 4, 20)",
                "Eq(16 - 4, 12)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Two unknowns need two facts",
            "beats": [
                "Name both unknowns and write down what each letter means.",
                "One equation usually COUNTS things: tickets, items, litres.",
                "The other WEIGHTS them: by price, by percentage, by speed.",
                "Solve, then check which of the two quantities the question wanted.",
            ],
        },
        {
            "kind": "teach",
            "title": "The count-and-weight pattern",
            "body": "Almost every SAT system word problem has the same skeleton. Something is "
                    "being counted — tickets sold, items bought, millilitres poured — and that "
                    "gives an equation where every coefficient is $1$. Then the same things are "
                    "weighted by a per-unit amount — a price, a concentration, a mass — and "
                    "that gives the second equation. Spotting the skeleton means you can write "
                    "both equations before you have finished reading.",
        },
        {"kind": "worked", "title": "Tickets: count and money", "problemId": "sat-l4c-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which pair of equations?",
            "prompt": "A vending machine holds $40$ coins, all $50$-cent and $10$-cent pieces, "
                      "worth $\\$12$ in total. Which system models this?",
            "options": [
                "$f + t = 40$ and $0.5f + 0.1t = 12$",
                "$f + t = 12$ and $0.5f + 0.1t = 40$",
                "$f + t = 40$ and $f + t = 12$",
                "$0.5f + 0.1t = 40$ and $f + t = 12$",
            ],
            "correctIndex": 0,
            "explanation": "The first equation counts coins, so both coefficients are $1$ and "
                           "the total is $40$. The second weights each coin by its value, so "
                           "the total is the money, $12$. Swapping the two totals — option B — "
                           "is the error the question is testing. Solving gives $f = 20$ "
                           "and $t = 20$.",
            "check": [
                "Eq(20 + 20, 40)",
                "Eq(Rational(1,2)*20 + Rational(1,10)*20, 12)",
            ],
        },
        {"kind": "worked", "title": "Mixtures: volume and concentration", "problemId": "sat-l4c-w2"},
        {
            "kind": "tip",
            "title": "Percentages never add across different amounts",
            "body": "Mixing a $20\\%$ solution with a $50\\%$ solution does not give $70\\%$, "
                    "or $35\\%$, unless you happen to use equal volumes. Write the ACID "
                    "equation instead: each solution contributes its own percentage of its own "
                    "volume, and those amounts do add.",
        },
        {"kind": "worked", "title": "Two prices, two receipts", "problemId": "sat-l4c-w3"},
        {"kind": "tryIt", "title": "Your turn: count and price", "problemId": "sat-l4c-t1"},
        {"kind": "tryIt", "title": "Your turn: sum and difference", "problemId": "sat-l4c-t2"},
        {"kind": "tryIt", "title": "Your turn: speeds that add and subtract", "problemId": "sat-l4c-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Two unknowns need two equations — find the two facts in the paragraph.",
                "One equation counts, the other weights by price, percentage or speed.",
                "Percentages of different amounts never add; the AMOUNTS do.",
                "Downstream adds the current to the boat's speed; upstream subtracts it.",
                "Solve for both, then re-read to see which one was asked for.",
            ],
        },
    ]

    return lesson(
        slug="systems-from-word-problems",
        title="Systems Hidden in Word Problems",
        concrete=(
            "A theatre sells $260$ tickets and takes $\\$2{,}570$. Neither number alone tells "
            "you how many were adult tickets — but together they do, exactly. Two unknowns, "
            "two facts, one answer: that is a system, and the paragraph always hands you both "
            "facts if you know what shape to look for."
        ),
        objective=(
            "Turn a two-unknown word problem into a system of two linear equations, solve it, "
            "and answer for the quantity the question asked about."
        ),
        concept=[
            "**Skill card.** Still *Systems of two linear equations in two variables*, in the "
            "**Algebra** domain. This is the modelling version, and on the digital SAT it is "
            "at least as common as the bare algebra version.",
            "Two unknowns require two independent facts, and the paragraph always contains "
            "exactly two. Name both unknowns first and write down in words what each letter "
            "means — that one habit prevents most of the errors on this skill.",
            "The skeleton is nearly always the same. One equation COUNTS: tickets sold, items "
            "bought, millilitres poured — every coefficient is $1$ and the total is a count. "
            "The other WEIGHTS the same things by a per-unit amount: price per ticket, "
            "concentration per millilitre, distance per hour. Once you see which sentence is "
            "the count and which is the weight, both equations are written.",
            "**The test's angle.** Mixture problems are the ones students lose. Percentages of "
            "different amounts do not add — a $20\\%$ solution mixed with a $50\\%$ one is not "
            "$70\\%$ or $35\\%$. What adds is the AMOUNT of acid: $0.20x + 0.50y$. Rate "
            "problems have their own pattern: a boat going downstream travels at "
            "$b + c$ and upstream at $b - c$, which gives the sum-and-difference system "
            "directly.",
        ],
        key_idea=(
            "One equation counts the objects, the other weights them by price, concentration "
            "or speed. Name both unknowns in words before writing either equation."
        ),
        facts=[
            fact(
                "Count and weight",
                "\\begin{cases} x + y = N \\\\ p\\,x + q\\,y = T \\end{cases}",
                "$N$ is how many things; $T$ is the total value; $p$ and $q$ are the per-unit "
                "amounts. This models the majority of SAT system word problems.",
            ),
            fact(
                "Mixtures",
                "r_1 x + r_2 y = r_{\\text{mix}}(x + y)",
                "Each solution contributes its own concentration times its own volume. "
                "Concentrations never add directly.",
            ),
            fact(
                "Upstream and downstream",
                "\\text{downstream} = b + c, \\qquad \\text{upstream} = b - c",
                "Same idea for a plane with a tailwind or headwind. Divide distance by time to "
                "get each speed first.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Swapping the totals between the count equation and the value equation.",
                "The equation whose coefficients are all $1$ must equal the COUNT. The "
                "weighted equation equals the money, mass or distance.",
            ),
            mistake(
                "Adding or averaging percentages in a mixture problem.",
                "Write the amount of the substance: $0.20x + 0.50y$. Those amounts add; the "
                "percentages do not.",
            ),
            mistake(
                "Answering with the other unknown.",
                "You will have solved for both. Re-read the question — the unwanted one is "
                "always an option.",
            ),
            mistake(
                "Using speeds where the problem gives distances and times.",
                "Divide first. $60$ kilometres in $3$ hours is $20$ kilometres per hour, and "
                "the system is built from the speeds.",
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
        "sat-l4-p01",
        "$$y = 3x$$\n$$x + y = 20$$\n"
        "What is the value of $x$?",
        "**Answer.** $5$. Substitute: $x + 3x = 20$, so $4x = 20$ and $x = 5$; then $y = 15$.",
        ["Eq(5 + 3*5, 20)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l4-p02",
        "$$2x + y = 11$$\n$$2x - y = 5$$\n"
        "What is the value of $y$?",
        "**Answer.** $3$. Subtracting the second equation from the first gives $2y = 6$, so "
        "$y = 3$ and $x = 4$.",
        ["Eq(2*4 + 3, 11)", "Eq(2*4 - 3, 5)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l4-p03",
        "$$x + 2y = 14$$\n$$3x - 2y = 2$$\n"
        "What is the solution $(x, y)$?",
        "**Answer.** $(4, 5)$. The $y$ terms are opposites, so add: $4x = 16$ and $x = 4$; "
        "then $2y = 10$ and $y = 5$. Check both: $4 + 10 = 14$ and $12 - 10 = 2$.",
        ["Eq(4 + 2*5, 14)", "Eq(3*4 - 2*5, 2)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l4-p04",
        "$$5x + 3y = 29$$\n$$2x - 3y = 6$$\n"
        "What is the value of $x$?",
        "**Answer.** $5$. Adding eliminates $y$: $7x = 35$, so $x = 5$. Then "
        "$3y = 29 - 25 = 4$, giving $y = \\frac{4}{3}$.",
        [
            "Eq(5*5 + 3*Rational(4,3), 29)",
            "Eq(2*5 - 3*Rational(4,3), 6)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-p05",
        "$$3x + 4y = 10$$\n$$6x + 8y = k$$\n"
        "For what value of the constant $k$ does the system have infinitely many solutions?",
        "**Answer.** $20$. The second equation's variable terms are exactly twice the first's, "
        "so the constant must double too: $k = 2 \\times 10 = 20$. Any other $k$ gives "
        "parallel lines and no solution.",
        ["Eq(2*(3*x + 4*y), 6*x + 8*y)", "Eq(2*10, 20)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-p06",
        "How many solutions does the system $2x + 5y = 8$ and $4x + 10y = 15$ have?",
        "**Answer.** None. Doubling the first equation gives $4x + 10y = 16$, but the second "
        "says the same expression equals $15$. Parallel lines, no solution.",
        ["Eq(2*(2*x + 5*y), 4*x + 10*y)", "Ne(16, 15)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-p07",
        "A bakery sells muffins for $\\$3$ and scones for $\\$4$. It sold $50$ items for "
        "$\\$174$. How many scones were sold?",
        "**Answer.** $24$. With $m + s = 50$ and $3m + 4s = 174$: substituting $m = 50 - s$ "
        "gives $150 - 3s + 4s = 174$, so $s = 24$ and $m = 26$. Check: "
        "$3(26) + 4(24) = 78 + 96 = 174$.",
        ["Eq(26 + 24, 50)", "Eq(3*26 + 4*24, 174)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-p08",
        "$$4x - y = 9$$\n$$x + 2y = 9$$\n"
        "What is the value of $x + y$?",
        "**Answer.** $6$. Doubling the first equation gives $8x - 2y = 18$; adding the second "
        "gives $9x = 27$, so $x = 3$. Then $y = 4(3) - 9 = 3$, and $x + y = 6$. Check both "
        "originals: $4(3) - 3 = 9$ and $3 + 2(3) = 9$. Answering $3$ — the value of either "
        "variable — is the trap.",
        ["Eq(4*3 - 3, 9)", "Eq(3 + 2*3, 9)", "Eq(3 + 3, 6)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-p09",
        "$$7x + 2y = 24$$\n$$cx + 6y = 30$$\n"
        "For what value of $c$ does the system have no solution?",
        "**Answer.** $21$. Parallel lines need the variable terms to scale while the constant "
        "does not. The $y$ terms scale by $3$, so $c = 3 \\times 7 = 21$; and "
        "$3 \\times 24 = 72 \\ne 30$, so the constant does not follow and the lines are "
        "parallel and distinct.",
        ["Eq(3*7, 21)", "Eq(3*2, 6)", "Ne(3*24, 30)"],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l4-p10",
        "A jar holds $30$ coins worth $\\$4.20$ in total, made up of $10$-cent and $20$-cent "
        "pieces. How many $20$-cent pieces are there?",
        "**Answer.** $12$. With $a + b = 30$ and $0.10a + 0.20b = 4.20$: multiplying the "
        "second by $10$ gives $a + 2b = 42$, and subtracting the first gives $b = 12$, so "
        "$a = 18$. Check: $0.10(18) + 0.20(12) = 1.80 + 2.40 = 4.20$.",
        [
            "Eq(18 + 12, 30)",
            "Eq(Rational(1,10)*18 + Rational(2,10)*12, Rational(42,10))",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-p11",
        "A plane flies $2{,}400$ kilometres with a tailwind in $4$ hours and the same distance "
        "against it in $6$ hours. What is the wind speed, in kilometres per hour?",
        "**Answer.** $100$. The two ground speeds are $600$ and $400$ kilometres per hour. "
        "With $p$ the plane's own speed and $w$ the wind: $p + w = 600$ and $p - w = 400$. "
        "Subtracting gives $2w = 200$, so $w = 100$ and $p = 500$.",
        [
            "Eq(Rational(2400,4), 600)",
            "Eq(Rational(2400,6), 400)",
            "Eq(500 + 100, 600)",
            "Eq(500 - 100, 400)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l4-p12",
        "$$3x + y = 14$$\n$$x - 2y = -7$$\n"
        "What is the value of $y$?",
        "**Answer.** $5$. From the first equation $y = 14 - 3x$. Substituting: "
        "$x - 2(14 - 3x) = -7$, so $x - 28 + 6x = -7$, giving $7x = 21$ and $x = 3$. Then "
        "$y = 14 - 9 = 5$. Check: $3 - 10 = -7$.",
        ["Eq(3*3 + 5, 14)", "Eq(3 - 2*5, -7)"],
        badges=_b("Medium"),
    ),
]

TEST = [
    problem(
        "sat-l4-x01",
        "$$y = x + 4$$\n$$2x + y = 19$$\n"
        "What is the value of $x$?",
        "**Answer.** $5$. Substitute: $2x + x + 4 = 19$, so $3x = 15$ and $x = 5$; $y = 9$.",
        ["Eq(2*5 + (5 + 4), 19)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l4-x02",
        "$$3x + 2y = 16$$\n$$3x - 2y = 4$$\n"
        "What is the solution $(x, y)$?",
        "**Answer.** $\\left(\\dfrac{10}{3}, 3\\right)$. Adding gives $6x = 20$, so "
        "$x = \\frac{10}{3}$; subtracting gives $4y = 12$, so $y = 3$.",
        [
            "Eq(3*Rational(10,3) + 2*3, 16)",
            "Eq(3*Rational(10,3) - 2*3, 4)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-x03",
        "$$4x + 6y = 22$$\n$$2x + ky = 11$$\n"
        "For what value of $k$ does the system have infinitely many solutions?",
        "**Answer.** $3$. The second equation is the first halved: the $x$ terms go $4 \\to 2$ "
        "and the constants $22 \\to 11$, both scaling by $\\frac{1}{2}$. So "
        "$k = \\frac{1}{2} \\times 6 = 3$.",
        ["Eq(Rational(1,2)*(4*x + 6*y), 2*x + 3*y)", "Eq(Rational(1,2)*22, 11)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-x04",
        "How many solutions does the system $y = -2x + 5$ and $4x + 2y = 10$ have?",
        "**Answer.** Infinitely many. Rearranging the second equation: $2y = -4x + 10$, so "
        "$y = -2x + 5$ — identical to the first. One line written twice.",
        ["Eq(solve(Eq(4*x + 2*y, 10), y)[0], -2*x + 5)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-x05",
        "A cinema charges $\\$9$ for a student ticket and $\\$14$ for a full-price ticket. It "
        "sold $180$ tickets and took $\\$2{,}020$. How many full-price tickets were sold?",
        "**Answer.** $80$. With $s + f = 180$ and $9s + 14f = 2020$: substituting "
        "$s = 180 - f$ gives $1620 - 9f + 14f = 2020$, so $5f = 400$ and $f = 80$, leaving "
        "$s = 100$. Check: $9(100) + 14(80) = 900 + 1120 = 2020$.",
        ["Eq(100 + 80, 180)", "Eq(9*100 + 14*80, 2020)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l4-x06",
        "$$5x - 3y = 9$$\n$$2x + y = 8$$\n"
        "What is the value of $x + y$?",
        "**Answer.** $5$. Triple the second equation so the $y$ terms become opposites: "
        "$6x + 3y = 24$. Adding it to the first gives $11x = 33$, so $x = 3$, and then "
        "$y = 8 - 6 = 2$. So $x + y = 5$. Check both: $15 - 6 = 9$ and $6 + 2 = 8$.",
        [
            "Eq(5*3 - 3*2, 9)",
            "Eq(2*3 + 2, 8)",
            "Eq(3 + 2, 5)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l4-x07",
        "A $40\\%$ salt solution is mixed with a $10\\%$ salt solution to make $900$ "
        "millilitres of a $20\\%$ solution. How many millilitres of the $40\\%$ solution are "
        "used?",
        "**Answer.** $300$. With $x + y = 900$ and $0.40x + 0.10y = 0.20(900) = 180$: "
        "substituting $y = 900 - x$ gives $0.40x + 90 - 0.10x = 180$, so $0.30x = 90$ and "
        "$x = 300$. Check: $0.40(300) + 0.10(600) = 120 + 60 = 180$.",
        [
            "Eq(300 + 600, 900)",
            "Eq(Rational(40,100)*300 + Rational(10,100)*600, 180)",
            "Eq(Rational(20,100)*900, 180)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-l4-x08",
        "$$ax + 2y = 10$$\n$$6x + 4y = 20$$\n"
        "The system above has infinitely many solutions. What is the value of $a$?",
        "**Answer.** $3$. The second equation is the first doubled: the $y$ terms go "
        "$2 \\to 4$ and the constants $10 \\to 20$, both scaling by $2$. So $2a = 6$ and "
        "$a = 3$.",
        ["Eq(2*(3*x + 2*y), 6*x + 4*y)", "Eq(2*10, 20)"],
        badges=_b("Medium"),
    ),
]


def main():
    lessons = [lesson_solving(), lesson_count(), lesson_words()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Systems of Two Linear Equations in Two Variables",
        4,
        "Substitution and elimination and knowing which one the system is asking for; deciding "
        "whether two lines cross once, never, or everywhere; and the count-and-weight skeleton "
        "behind almost every system word problem on the test.",
        "Solving one linear equation (Unit 1) and the slope of a line (Unit 2).",
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
