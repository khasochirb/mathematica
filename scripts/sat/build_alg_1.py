#!/usr/bin/env python3
"""SAT Math — Algebra, Unit 1: Linear equations in one variable.

One of the four official College Board domains, cut into the official
subtopics rather than into units borrowed from the school catalog: this file
builds data/genmath/sat/linear-equations-one-variable.json.

Algebra carries 13-15 of the 44 questions on the Math section and this is the
skill the rest of the domain stands on, so the unit is deliberately the
longest-drilled of the five.

Run: python3 scripts/sat/build_alg_1.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "linear-equations-one-variable"


# ===========================================================================
# Lesson 1 — solving a linear equation
# ===========================================================================

def lesson_solving():
    worked = [
        problem(
            "sat-le1-w1",
            "If $5(x - 3) = 2x + 9$, what is the value of $x$?",
            "**Answer.** $x = 8$.  \n"
            "Distribute the $5$ across both terms in the parentheses:\n"
            "$$5x - 15 = 2x + 9$$\n"
            "Subtract $2x$ from both sides to collect the variable on the left:\n"
            "$$3x - 15 = 9$$\n"
            "Add $15$ to both sides:\n"
            "$$3x = 24$$\n"
            "Divide both sides by $3$:\n"
            "$$x = 8$$\n"
            "Check by substitution: $5(8 - 3) = 25$ and $2(8) + 9 = 25$. They agree, so $x = 8$.  \n"
            "**Desmos route.** Type both sides as two functions and read the intersection. "
            "That is slower here than the algebra, but it is a free safety net when the "
            "coefficients get ugly.",
            [
                "Eq(5*(8 - 3), 2*8 + 9)",
                "Eq(solve(Eq(5*(x - 3), 2*x + 9), x)[0], 8)",
            ],
        ),
        problem(
            "sat-le1-w2",
            "$$\\frac{x}{2} + \\frac{x - 2}{3} = 6$$\n"
            "What value of $x$ satisfies the equation above?",
            "**Answer.** $x = 8$.  \n"
            "The denominators are $2$ and $3$, so multiply EVERY term by $6$ — the least "
            "common denominator — to clear both fractions in one move:\n"
            "$$6 \\cdot \\frac{x}{2} + 6 \\cdot \\frac{x - 2}{3} = 6 \\cdot 6$$\n"
            "$$3x + 2(x - 2) = 36$$\n"
            "Distribute the $2$ across both terms in the bracket:\n"
            "$$3x + 2x - 4 = 36$$\n"
            "Collect like terms:\n"
            "$$5x - 4 = 36$$\n"
            "$$5x = 40$$\n"
            "$$x = 8$$\n"
            "Check: $\\frac{8}{2} + \\frac{6}{3} = 4 + 2 = 6$.  \n"
            "Note the $6$ on the right also gets multiplied. Multiplying only the two "
            "fractions is the single commonest error on this pattern.",
            [
                "Eq(Rational(8,2) + Rational(8 - 2, 3), 6)",
                "Eq(solve(Eq(x/2 + (x - 2)/3, 6), x)[0], 8)",
            ],
        ),
        problem(
            "sat-le1-w3",
            "If $3(2x + 7) = 33$, what is the value of $2x + 7$?",
            "**Answer.** $11$.  \n"
            "The question asks for $2x + 7$, not for $x$ — and $2x + 7$ is already sitting "
            "in the equation as a single block. Treat it as one object:\n"
            "$$3 \\cdot (\\text{block}) = 33 \\;\\Longrightarrow\\; \\text{block} = 11$$\n"
            "So $2x + 7 = 11$ and you are done in one division.  \n"
            "The long way still works: distribute to get $6x + 21 = 33$, so $6x = 12$ and "
            "$x = 2$, then $2(2) + 7 = 11$. Same answer, four times the work — and $x = 2$ "
            "is exactly the trap answer the test puts in the options.",
            [
                "Eq(3*(2*2 + 7), 33)",
                "Eq(2*2 + 7, 11)",
                "Eq(solve(Eq(3*(2*x + 7), 33), x)[0], 2)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-le1-t1",
            "If $4(x + 2) = 3x + 15$, what is the value of $x$?",
            "**Answer.** $x = 7$.  \n"
            "Distribute: $4x + 8 = 3x + 15$. Subtract $3x$: $x + 8 = 15$. Subtract $8$: $x = 7$.  \n"
            "Check: $4(7 + 2) = 36$ and $3(7) + 15 = 36$.",
            ["Eq(4*(7 + 2), 3*7 + 15)", "Eq(solve(Eq(4*(x + 2), 3*x + 15), x)[0], 7)"],
        ),
        problem(
            "sat-le1-t2",
            "$$0.4x + 1.2 = 0.1x + 3$$\n"
            "What value of $x$ satisfies the equation above?",
            "**Answer.** $x = 6$.  \n"
            "Multiply every term by $10$ to clear the decimals: $4x + 12 = x + 30$. "
            "Subtract $x$: $3x + 12 = 30$. Subtract $12$: $3x = 18$, so $x = 6$.  \n"
            "Check: $0.4(6) + 1.2 = 3.6$ and $0.1(6) + 3 = 3.6$.",
            [
                "Eq(Rational(4,10)*6 + Rational(12,10), Rational(1,10)*6 + 3)",
                "Eq(solve(Eq(Rational(4,10)*x + Rational(12,10), Rational(1,10)*x + 3), x)[0], 6)",
            ],
        ),
        problem(
            "sat-le1-t3",
            "If $\\dfrac{2x - 5}{3} = 7$, what is the value of $2x - 5$?",
            "**Answer.** $21$.  \n"
            "The numerator $2x - 5$ is the block the question wants. Multiply both sides by "
            "$3$: $2x - 5 = 21$. Done — no need to find $x$ at all.  \n"
            "If you did solve on: $2x = 26$, so $x = 13$. The option list will certainly "
            "contain $13$.",
            ["Eq((2*13 - 5)/3, 7)", "Eq(2*13 - 5, 21)"],
        ),
        problem(
            "sat-le1-t4",
            "If $7 - 2(3 - x) = 4x + 5$, what is the value of $x$?",
            "**Answer.** $x = -2$.  \n"
            "Distribute the $-2$ across BOTH terms — this is where the sign error lives:\n"
            "$$7 - 6 + 2x = 4x + 5$$\n"
            "$$1 + 2x = 4x + 5$$\n"
            "Subtract $2x$: $1 = 2x + 5$. Subtract $5$: $-4 = 2x$, so $x = -2$.  \n"
            "Check: $7 - 2(3 - (-2)) = 7 - 10 = -3$ and $4(-2) + 5 = -3$.",
            [
                "Eq(7 - 2*(3 - (-2)), 4*(-2) + 5)",
                "Eq(solve(Eq(7 - 2*(3 - x), 4*x + 5), x)[0], -2)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Linear equations in one variable",
            "beats": [
                "Domain: Algebra — 13 to 15 of the 44 questions on the Math section.",
                "Expect 2 or 3 questions on this skill alone, mostly easy and medium.",
                "Every other Algebra skill is built on it, so an error here costs points twice.",
                "No prerequisites beyond arithmetic with negatives and fractions.",
            ],
        },
        {
            "kind": "teach",
            "title": "One variable, one answer",
            "body": "An equation claims two expressions are equal. Solving means finding the "
                    "value that makes the claim true. You may do anything to both sides — add, "
                    "subtract, multiply, divide — with one exception: never divide by zero. "
                    "Every legal move keeps the balance, and the goal is to move everything "
                    "except the variable off to the other side.",
        },
        {
            "kind": "balanceScale",
            "title": "Both sides, always",
            "teach": "Three x-boxes balance eighteen weights. Split each pan into three equal "
                     "groups and one box balances six. Dividing both sides by 3 is exactly that "
                     "move, written down.",
            "config": {"mode": "mul", "coef": 3, "rhs": 18},
        },
        {
            "kind": "teach",
            "title": "The order that never gets stuck",
            "beats": [
                "1. Clear fractions and decimals — multiply every term by the common denominator or a power of ten.",
                "2. Distribute across every parenthesis.",
                "3. Collect variable terms on one side, constants on the other.",
                "4. Divide by the coefficient.",
                "Do them in that order and the equation unwinds itself.",
            ],
        },
        {"kind": "worked", "title": "Distribute, collect, divide", "problemId": "sat-le1-w1"},
        {
            "kind": "algebraTiles",
            "title": "Collecting like terms",
            "teach": "Drag tiles to build an expression, then collect them. Three x-tiles and "
                     "two more x-tiles are five x-tiles; an x-tile and a unit tile never combine. "
                     "That is the whole rule behind step 3.",
            "config": {"x": 3, "units": 5, "mode": "collect"},
        },
        {
            "kind": "tapQuestion",
            "title": "Spot the first move",
            "prompt": "Which first move clears the fractions in $\\dfrac{x}{6} - \\dfrac{x}{4} = 1$ in a single step?",
            "options": [
                "Multiply every term by $12$",
                "Multiply every term by $24$",
                "Multiply every term by $10$",
                "Subtract $\\dfrac{x}{4}$ from both sides",
            ],
            "correctIndex": 0,
            "explanation": "The least common denominator of $6$ and $4$ is $12$, giving "
                           "$2x - 3x = 12$, so $x = -12$. Multiplying by $24$ also works but "
                           "leaves bigger numbers; $10$ clears nothing; subtracting leaves both "
                           "fractions in place.",
            "check": [
                "Eq(solve(Eq(x/6 - x/4, 1), x)[0], -12)",
                "Eq(lcm(6, 4), 12)",
                "Eq(12*Rational(1,6) - 12*Rational(1,4), 2 - 3)",
            ],
        },
        {"kind": "worked", "title": "Clearing fractions", "problemId": "sat-le1-w2"},
        {
            "kind": "tip",
            "title": "Read the last line first",
            "body": "The SAT often asks for an expression, not for the variable: 'what is the "
                    "value of $2x + 7$?' If that expression already appears as a block in the "
                    "equation, you are one step from the answer and the value of $x$ is a trap "
                    "option. Read what is being asked BEFORE you start moving terms.",
        },
        {"kind": "worked", "title": "Answer the question asked", "problemId": "sat-le1-w3"},
        {"kind": "tryIt", "title": "Your turn: distribute and collect", "problemId": "sat-le1-t1"},
        {"kind": "tryIt", "title": "Your turn: clear the decimals", "problemId": "sat-le1-t2"},
        {"kind": "tryIt", "title": "Your turn: the block again", "problemId": "sat-le1-t3"},
        {"kind": "tryIt", "title": "Your turn: mind the sign", "problemId": "sat-le1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Clear fractions first, distribute second, collect third, divide last.",
                "Distributing a negative changes the sign of every term inside.",
                "If the question asks for an expression, look for it as a block before solving.",
                "Substituting your answer back takes ten seconds and catches almost every slip.",
                "Grid-in answers may be fractions or decimals — a non-integer is not a red flag.",
            ],
        },
    ]

    return lesson(
        slug="solving-linear-equations",
        title="Solving a Linear Equation",
        concrete=(
            "A phone plan charges $\\$35$ a month plus $\\$0.12$ a minute, and the bill came "
            "to $\\$59$. Exactly one number of minutes produces that bill, and finding it is "
            "one equation: $35 + 0.12m = 59$. The SAT dresses this in a dozen costumes — "
            "wages, mixtures, membership fees, distances — and every costume comes off the "
            "same way."
        ),
        objective=(
            "Solve any linear equation in one variable — clearing fractions and decimals, "
            "distributing, collecting and dividing — and recognise when the question wants an "
            "expression rather than the variable itself."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Linear equations in one variable*, "
            "in the **Algebra** domain. Algebra is 13 to 15 of the 44 questions on the Math "
            "section, and this skill sits underneath every other one in the domain. Expect two "
            "or three questions on it directly, and at least one dressed as a word problem.",
            "An equation is a claim that two expressions are equal. Solving it means finding "
            "the value of the variable that makes the claim true. You may add, subtract, "
            "multiply or divide BOTH sides by the same thing — the only illegal move is "
            "dividing by zero. Each legal move keeps the equation balanced while stripping "
            "away everything that is not the variable.",
            "The order that never gets stuck: clear fractions and decimals first (multiply "
            "every term by the least common denominator, or by a power of ten), then "
            "distribute, then collect variable terms on one side and constants on the other, "
            "then divide by the coefficient. Fractions are the single biggest source of lost "
            "points here, and clearing them at the start means you never meet one again.",
            "**The test's angle.** The SAT rarely stops at $x$. It asks for $2x$, or for "
            "$x + 5$, or for the value of an expression built from $x$ — because a fast solver "
            "notices the requested quantity is already visible. In $3(2x + 7) = 33$ the block "
            "$2x + 7$ equals $11$ after one division; grinding out $x = 2$ first is four times "
            "the work AND lands on the trap option. Read the question's last line before you "
            "touch the equation.",
        ],
        key_idea=(
            "Whatever you do to one side, do to the other. Clear fractions, distribute, "
            "collect, divide — in that order — and then read the question again to check "
            "which quantity it actually wanted."
        ),
        facts=[
            fact(
                "The two legal moves",
                "a = b \\;\\Longrightarrow\\; a + c = b + c, \\qquad a = b \\;\\Longrightarrow\\; ac = bc \\;\\;(c \\ne 0)",
                "Adding and multiplying both sides by the same thing preserve equality. These "
                "two moves, run backwards and forwards, are the entire toolkit.",
            ),
            fact(
                "Clearing fractions",
                "\\frac{x}{4} + \\frac{x}{3} = 7 \\;\\Longrightarrow\\; 3x + 4x = 84",
                "Multiply EVERY term — including the ones already whole — by the least common "
                "denominator. Missing one term is the classic error.",
            ),
            fact(
                "Distributing a negative",
                "-2(3 - x) = -6 + 2x",
                "The sign attaches to both terms inside. Writing $-6 - 2x$ here is the most "
                "common single mistake on this skill.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Distributing only over the first term: reading $-2(3 - x)$ as $-6 - x$.",
                "The multiplier hits every term inside the parentheses, and a negative "
                "multiplier flips every sign: $-2(3 - x) = -6 + 2x$.",
            ),
            mistake(
                "Multiplying only the fraction terms when clearing denominators.",
                "Every term on both sides gets multiplied, including whole numbers. In "
                "$\\frac{x}{4} + 1 = 5$, multiplying by $4$ gives $x + 4 = 20$, not $x + 1 = 20$.",
            ),
            mistake(
                "Solving for $x$ when the question asked for $3x$ or $x + 2$.",
                "The value of $x$ is almost always one of the wrong options in that situation. "
                "Re-read the final sentence before choosing.",
            ),
            mistake(
                "Assuming a grid-in answer has to be a whole number, and 'fixing' a fraction.",
                "Grid-ins accept fractions and decimals. If the algebra gives $\\frac{68}{7}$, "
                "enter $68/7$ — rounding to $10$ scores zero.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — no solution, one solution, infinitely many
# ===========================================================================

def lesson_how_many():
    worked = [
        problem(
            "sat-le2-w1",
            "$$4(x + 3) = ax + 12$$\n"
            "In the equation above, $a$ is a constant. If the equation has infinitely many "
            "solutions, what is the value of $a$?",
            "**Answer.** $a = 4$.  \n"
            "Infinitely many solutions means the two sides are the SAME expression — identical "
            "coefficient, identical constant. Distribute the left side:\n"
            "$$4x + 12 = ax + 12$$\n"
            "The constants already match ($12 = 12$). For the variable terms to match as well, "
            "$$a = 4$$\n"
            "Any other value of $a$ gives exactly one solution, because then $4x$ and $ax$ "
            "differ and the $x$ terms cannot cancel.",
            ["Eq(4*(x + 3) - (4*x + 12), 0)", "Eq(solve(Eq(4, a), a)[0], 4)"],
        ),
        problem(
            "sat-le2-w2",
            "$$6x - 5 = 2(3x + k)$$\n"
            "In the equation above, $k$ is a constant. For what value of $k$ does the equation "
            "have infinitely many solutions?",
            "**Answer.** $k = -\\dfrac{5}{2}$.  \n"
            "Distribute the right side:\n"
            "$$6x - 5 = 6x + 2k$$\n"
            "Subtract $6x$ from both sides. The variable vanishes entirely:\n"
            "$$-5 = 2k$$\n"
            "Solving for $k$ gives $k = -\\frac{5}{2}$, and with that value the equation reads "
            "$-5 = -5$: a true statement with no $x$ left in it, so EVERY real number is a "
            "solution.  \n"
            "The same line answers the companion question. For any OTHER value of $k$ the "
            "equation reduces to a false statement such as $-5 = 2$, which no $x$ can rescue — "
            "so every $k$ except $-\\frac{5}{2}$ gives no solution, and no value of $k$ "
            "gives exactly one.",
            [
                "Eq(6*x - 5 - 2*(3*x + Rational(-5,2)), 0)",
                "Eq(solve(Eq(2*k, -5), k)[0], Rational(-5, 2))",
                "Ne(6*x - 5 - 2*(3*x + 1), 0)",
            ],
        ),
        problem(
            "sat-le2-w3",
            "How many solutions does the equation $3(x - 2) + 4 = 3x - 2$ have?",
            "**Answer.** infinitely many.  \n"
            "Simplify the left side:\n"
            "$$3x - 6 + 4 = 3x - 2$$\n"
            "$$3x - 2 = 3x - 2$$\n"
            "The two sides are identical, so every real number satisfies the equation.  \n"
            "The tell: when you subtract $3x$ from both sides you get $-2 = -2$, a true "
            "statement with no variable left. True statement means every $x$ works; a false "
            "statement like $-2 = 5$ would mean no $x$ works.",
            ["Eq(simplify(3*(x - 2) + 4 - (3*x - 2)), 0)"],
        ),
    ]

    try_it = [
        problem(
            "sat-le2-t1",
            "$$5(2x - 3) = cx - 15$$\n"
            "In the equation above, $c$ is a constant. If the equation has infinitely many "
            "solutions, what is the value of $c$?",
            "**Answer.** $c = 10$.  \n"
            "Distribute: $10x - 15 = cx - 15$. The constants match, so the coefficients must "
            "too: $c = 10$.",
            ["Eq(5*(2*x - 3) - (10*x - 15), 0)"],
        ),
        problem(
            "sat-le2-t2",
            "How many solutions does $2(x + 4) = 2x + 5$ have?",
            "**Answer.** none.  \n"
            "Distribute: $2x + 8 = 2x + 5$. Subtract $2x$: $8 = 5$, which is false. No value "
            "of $x$ can make it true, so the equation has no solution.",
            ["Ne(2*(x + 4), 2*x + 5)", "Ne(8, 5)"],
        ),
        problem(
            "sat-le2-t3",
            "$$ax + 9 = 4x + b$$\n"
            "In the equation above, $a$ and $b$ are constants. If the equation has exactly one "
            "solution, which statement must be true?",
            "**Answer.** $a \\ne 4$.  \n"
            "Rewrite as $(a - 4)x = b - 9$. If $a \\ne 4$ you may divide by $a - 4$ and get "
            "exactly one solution, whatever $b$ is. If $a = 4$ the left side collapses to $0$, "
            "and then the equation has infinitely many solutions when $b = 9$ and none "
            "otherwise. So the single condition that guarantees exactly one solution is "
            "$a \\ne 4$; $b$ is unconstrained.",
            ["Eq(solve(Eq(5*x + 9, 4*x + 2), x)[0], -7)", "Ne(5, 4)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Three possible endings",
            "beats": [
                "One solution — the variable survives and lands on a number.",
                "No solution — the variable cancels and leaves something false, like 8 = 5.",
                "Infinitely many — the variable cancels and leaves something true, like 5 = 5.",
                "The endings are decided by the coefficients, not by how hard the algebra looks.",
            ],
        },
        {
            "kind": "teach",
            "title": "Read it off the coefficients",
            "body": "Push every equation into the shape $px + q = rx + s$. If $p \\ne r$ there "
                    "is exactly one solution. If $p = r$ and $q = s$ the two sides are the same "
                    "expression — infinitely many solutions. If $p = r$ but $q \\ne s$ the "
                    "equation is a contradiction — no solution. That is the whole skill, and "
                    "it lets you answer without solving anything.",
        },
        {
            "kind": "systemGraph",
            "title": "Two lines that never meet",
            "teach": "Each side of a linear equation is a line. One solution is the point where "
                     "two crossing lines meet. Equal coefficients make the lines PARALLEL — "
                     "drag them and they never touch, which is exactly what 'no solution' looks "
                     "like. Make the intercepts equal too and the two lines land on top of each "
                     "other: infinitely many solutions.",
            "config": {"m1": 2, "b1": 1, "m2": 2, "b2": 4, "interactive": True, "min": -6, "max": 6},
        },
        {"kind": "worked", "title": "Infinitely many: match everything", "problemId": "sat-le2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which ending?",
            "prompt": "How many solutions does $3(2x - 1) = 6x - 3$ have?",
            "options": ["Infinitely many", "Exactly one", "None", "Exactly two"],
            "correctIndex": 0,
            "explanation": "Distributing gives $6x - 3 = 6x - 3$: the two sides are identical, "
                           "so every real number is a solution. A linear equation can never "
                           "have exactly two solutions.",
            "check": ["Eq(simplify(3*(2*x - 1) - (6*x - 3)), 0)"],
        },
        {"kind": "worked", "title": "No solution: the constant decides", "problemId": "sat-le2-w2"},
        {
            "kind": "tip",
            "title": "The 60-second check",
            "body": "When a question hands you a constant like $a$ or $k$ and asks about the "
                    "number of solutions, do NOT solve for $x$. Distribute both sides, line the "
                    "two sides up, and compare the coefficient of $x$ and the constant. The "
                    "answer falls out of the comparison in one line.",
        },
        {"kind": "worked", "title": "Reading the ending off a simplification", "problemId": "sat-le2-w3"},
        {"kind": "tryIt", "title": "Your turn: match the coefficients", "problemId": "sat-le2-t1"},
        {"kind": "tryIt", "title": "Your turn: name the ending", "problemId": "sat-le2-t2"},
        {"kind": "tryIt", "title": "Your turn: the condition for one solution", "problemId": "sat-le2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Shape every such equation into px + q = rx + s and compare p with r.",
                "p different from r: exactly one solution, whatever the constants are.",
                "p equal to r and q equal to s: infinitely many solutions.",
                "p equal to r but q different from s: no solution.",
                "A linear equation in one variable can never have exactly two solutions.",
            ],
        },
    ]

    return lesson(
        slug="no-solution-or-infinitely-many",
        title="No Solution, One Solution, Every Solution",
        concrete=(
            "Two runners set off down the same road. If they run at different speeds, there is "
            "exactly one moment they are level. If they run at the same speed from the same "
            "start, they are level forever. If they run at the same speed from different "
            "starts, they are never level at all. Every linear equation is one of those three "
            "races, and the coefficients tell you which before you solve anything."
        ),
        objective=(
            "Decide whether a linear equation has one solution, no solution, or infinitely "
            "many by comparing coefficients, and find the value of an unknown constant that "
            "forces a given outcome."
        ),
        concept=[
            "**Skill card.** Still *Linear equations in one variable*, in the **Algebra** "
            "domain — but this is the version the College Board reserves for the harder half "
            "of the module. It shows up as 'the equation has no solution, what is the value of "
            "$a$?' and it is worth knowing cold, because the intended method takes about "
            "twenty seconds and the brute-force method takes two minutes.",
            "Push any linear equation into the shape $px + q = rx + s$. Subtract $rx$ from both "
            "sides and you get $(p - r)x = s - q$. Everything follows from whether $p - r$ is "
            "zero.",
            "If $p \\ne r$, you divide by $p - r$ and land on a single number: exactly one "
            "solution, no matter what the constants are. If $p = r$, the variable disappears "
            "and you are left with a bare claim about numbers. If that claim is TRUE "
            "($q = s$), every real number was a solution all along — infinitely many. If it is "
            "FALSE ($q \\ne s$), nothing can rescue it — no solution.",
            "**The test's angle.** These questions almost always hide a constant. 'For what "
            "value of $a$ does the equation have infinitely many solutions?' means: make both "
            "sides identical. 'For what value has it no solution?' means: make the $x$ terms "
            "match while the constants do not. You never solve for $x$ — you match two "
            "expressions, coefficient against coefficient.",
        ],
        key_idea=(
            "The variable's coefficients decide everything. Different coefficients means one "
            "solution. Same coefficients means the constants decide: matching constants give "
            "infinitely many solutions, mismatched constants give none."
        ),
        facts=[
            fact(
                "The classification",
                "px + q = rx + s \\;\\Longrightarrow\\; (p - r)x = s - q",
                "One solution when $p \\ne r$. When $p = r$: infinitely many if $q = s$, none "
                "otherwise.",
            ),
            fact(
                "Infinitely many means identical",
                "ax + b = cx + d \\text{ for all } x \\iff a = c \\text{ and } b = d",
                "Two linear expressions agree everywhere only when they are the same "
                "expression. This is the fact the constant-finding questions test.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Reading 'no solution' as 'the answer is zero'.",
                "$x = 0$ IS a solution — the value happens to be zero. No solution means the "
                "equation is false for every $x$ and there is nothing to write down.",
            ),
            mistake(
                "Matching only the variable terms when asked for infinitely many solutions.",
                "Infinitely many requires BOTH the coefficients and the constants to match. If "
                "the constants disagree, matching the coefficients produces no solution instead.",
            ),
            mistake(
                "Trying to solve for $x$ when the question asks for the constant.",
                "Solving for $x$ in terms of $a$ works but is slow and error-prone. Distribute "
                "both sides and compare them term by term.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 3 — the equation hidden in a paragraph
# ===========================================================================

def lesson_word_problems():
    worked = [
        problem(
            "sat-le3-w1",
            "A gym charges a one-time joining fee of $\\$40$ plus $\\$25$ per month. A member "
            "has paid a total of $\\$290$. For how many months has the member belonged to the "
            "gym?",
            "**Answer.** $10$ months.  \n"
            "Name the unknown: let $m$ be the number of months. The total is the one-time fee "
            "plus the monthly charge times the number of months:\n"
            "$$40 + 25m = 290$$\n"
            "Subtract the joining fee — it is paid once, so it comes off once:\n"
            "$$25m = 250$$\n"
            "$$m = 10$$\n"
            "Check: $40 + 25(10) = 290$.  \n"
            "The trap option is $11.6$, which is $290 \\div 25$ — what you get by forgetting "
            "the joining fee entirely.",
            ["Eq(40 + 25*10, 290)", "Eq(solve(Eq(40 + 25*m, 290), m)[0], 10)"],
        ),
        problem(
            "sat-le3-w2",
            "A number is $8$ more than $3$ times a second number. The sum of the two numbers "
            "is $52$. What is the value of the smaller number?",
            "**Answer.** $11$.  \n"
            "Name the SECOND number $n$, because the first is described in terms of it:\n"
            "$$\\text{first} = 3n + 8, \\qquad \\text{second} = n$$\n"
            "Their sum is $52$:\n"
            "$$(3n + 8) + n = 52$$\n"
            "$$4n + 8 = 52$$\n"
            "$$4n = 44$$\n"
            "$$n = 11$$\n"
            "The other number is $3(11) + 8 = 41$, and $11 + 41 = 52$ confirms it. The "
            "question asks for the SMALLER, which is $11$ — $41$ is on the option list.  \n"
            "The naming choice matters: calling the FIRST number $n$ forces "
            "$\\frac{n-8}{3}$ into the equation and triples the algebra.",
            ["Eq((3*11 + 8) + 11, 52)", "Eq(solve(Eq((3*n + 8) + n, 52), n)[0], 11)", "11 < 41"],
        ),
        problem(
            "sat-le3-w3",
            "A chemist has $200$ millilitres of a solution that is $10\\%$ acid. She adds "
            "pure water until the mixture is $8\\%$ acid. How many millilitres of water did "
            "she add?",
            "**Answer.** $50$ millilitres.  \n"
            "The quantity that does not change is the ACID. Adding water changes the total "
            "volume, never the acid:\n"
            "$$\\text{acid} = 0.10 \\times 200 = 20 \\text{ mL}$$\n"
            "Let $w$ be the millilitres of water added. The new total volume is $200 + w$, and "
            "the same $20$ mL of acid is now $8\\%$ of it:\n"
            "$$0.08(200 + w) = 20$$\n"
            "$$200 + w = 250$$\n"
            "$$w = 50$$\n"
            "Check: $250$ mL containing $20$ mL of acid is $20/250 = 8\\%$.  \n"
            "$250$ is the trap answer — it is the new TOTAL, not the water added.",
            [
                "Eq(Rational(8,100)*(200 + 50), Rational(10,100)*200)",
                "Eq(Rational(20,250), Rational(8,100))",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-le3-t1",
            "A taxi charges a flat $\\$3.50$ plus $\\$1.75$ per kilometre. A ride cost "
            "$\\$24.50$. How many kilometres was the ride?",
            "**Answer.** $12$ kilometres.  \n"
            "Let $k$ be the kilometres travelled:\n"
            "$$3.50 + 1.75k = 24.50$$\n"
            "Subtract the flat fee, which is charged once:\n"
            "$$1.75k = 21$$\n"
            "$$k = 12$$\n"
            "Check: $3.50 + 1.75(12) = 3.50 + 21 = 24.50$.  \n"
            "Dividing $24.50$ by $1.75$ without removing the flat fee gives $14$ — a listed "
            "option on every version of this question.",
            [
                "Eq(Rational(350,100) + Rational(175,100)*12, Rational(2450,100))",
                "Eq(solve(Eq(Rational(350,100) + Rational(175,100)*k, Rational(2450,100)), k)[0], 12)",
                "Eq(Rational(2450,100)/Rational(175,100), 14)",
            ],
        ),
        problem(
            "sat-le3-t2",
            "The sum of three consecutive integers is $84$. What is the largest of the three?",
            "**Answer.** $29$.  \n"
            "Let the MIDDLE integer be $n$; the three are $n - 1$, $n$, $n + 1$ and their sum "
            "collapses beautifully:\n"
            "$$(n - 1) + n + (n + 1) = 3n = 84$$\n"
            "so $n = 28$ and the three integers are $27$, $28$, $29$. The largest is $29$.  \n"
            "Naming the middle one is the trick: naming the smallest gives $3n + 3 = 84$, "
            "which works but adds a step.",
            ["Eq(27 + 28 + 29, 84)", "Eq(solve(Eq(3*n, 84), n)[0], 28)"],
        ),
        problem(
            "sat-le3-t3",
            "A store marks up every item by $40\\%$ of its wholesale cost. A jacket sells for "
            "$\\$91$. What was the wholesale cost, in dollars?",
            "**Answer.** $\\$65$.  \n"
            "Let $c$ be the wholesale cost. The selling price is the cost plus $40\\%$ of the "
            "cost, which is $1.4c$:\n"
            "$$1.4c = 91$$\n"
            "$$c = 65$$\n"
            "Check: $40\\%$ of $65$ is $26$, and $65 + 26 = 91$.  \n"
            "The trap is subtracting $40\\%$ from the selling price: $91 - 36.40 = 54.60$, "
            "which is wrong because the markup is a percentage of the COST, not of the price.",
            [
                "Eq(Rational(14,10)*65, 91)",
                "Eq(65 + Rational(40,100)*65, 91)",
                "Ne(91 - Rational(40,100)*91, 65)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Four moves, every time",
            "beats": [
                "1. Name the unknown with a letter and write down what the letter means.",
                "2. Find the quantity the paragraph says stays fixed — a total, a cost, an amount of acid.",
                "3. Write that fixed quantity two ways and set them equal.",
                "4. Solve, then re-read the question to see which number it asked for.",
            ],
        },
        {
            "kind": "teach",
            "title": "Name the right unknown",
            "body": "When one quantity is described in terms of another — 'eight more than three "
                    "times the second number' — name the one being described FROM, not the one "
                    "being described. Naming the second number $n$ makes the first $3n + 8$; "
                    "naming the first number $n$ makes the second $\\frac{n - 8}{3}$ and triples "
                    "the work. The right name is usually the noun that appears at the END of "
                    "the sentence.",
        },
        {
            "kind": "evaluator",
            "title": "Flat fee plus a rate",
            "teach": "The commonest SAT setup: something charged once, plus something charged "
                     "per unit. Slide the number of months and watch the gym total climb by "
                     "the same 25 dollars each time, starting from the 40-dollar joining fee. "
                     "The question runs this machine backwards: given the total, find the slider.",
            "config": {"a": 25, "b": 40, "varName": "m", "min": 0, "max": 14, "start": 6},
        },
        {"kind": "worked", "title": "One-time fee plus a monthly rate", "problemId": "sat-le3-w1"},
        {
            "kind": "tapQuestion",
            "title": "Translate the sentence",
            "prompt": "'Five less than twice a number is $17$.' Which equation says that?",
            "options": [
                "$2n - 5 = 17$",
                "$5 - 2n = 17$",
                "$2(n - 5) = 17$",
                "$2n + 5 = 17$",
            ],
            "correctIndex": 0,
            "explanation": "'Twice a number' is $2n$; 'five less than' that subtracts $5$ FROM "
                           "it, giving $2n - 5 = 17$ and $n = 11$. Option B reverses the "
                           "subtraction, C subtracts before doubling, D adds instead of "
                           "subtracting. 'Less than' always reverses the order you read it in.",
            "check": ["Eq(solve(Eq(2*n - 5, 17), n)[0], 11)", "Eq(2*11 - 5, 17)"],
        },
        {"kind": "worked", "title": "Two numbers, one relationship", "problemId": "sat-le3-w2"},
        {
            "kind": "tip",
            "title": "Find what does not change",
            "body": "Mixture, dilution and 'how much must be added' problems all turn on a "
                    "quantity that survives the change. Adding water changes the volume but "
                    "not the acid. Adding a solvent-free ingredient changes the total but not "
                    "the other ingredient. Write that invariant quantity twice — before and "
                    "after — and set the two expressions equal.",
        },
        {"kind": "worked", "title": "The quantity that stays fixed", "problemId": "sat-le3-w3"},
        {"kind": "tryIt", "title": "Your turn: flat fee plus rate", "problemId": "sat-le3-t1"},
        {"kind": "tryIt", "title": "Your turn: consecutive integers", "problemId": "sat-le3-t2"},
        {"kind": "tryIt", "title": "Your turn: percent of what?", "problemId": "sat-le3-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Write down what your letter means before you write the equation.",
                "'Less than' and 'subtracted from' reverse the order the words appear in.",
                "A percent increase is a percentage of the ORIGINAL, so selling price is 1.4 times cost.",
                "In mixture problems, the ingredient that is not added is the one that stays fixed.",
                "After solving, re-read the last sentence: the smaller number, the total, the water added.",
            ],
        },
    ]

    return lesson(
        slug="equations-from-word-problems",
        title="Finding the Equation Inside the Words",
        concrete=(
            "A gym bill of $\\$290$, a joining fee of $\\$40$, dues of $\\$25$ a month. The "
            "paragraph looks nothing like algebra until you notice that $\\$290$ can be "
            "written a second way — $40 + 25m$ — and that writing one quantity two different "
            "ways IS the equation. Every SAT word problem is that same trick."
        ),
        objective=(
            "Turn an SAT word problem into a linear equation in one variable: name the "
            "unknown, find the quantity that is expressed twice, and answer the question the "
            "paragraph actually asked."
        ),
        concept=[
            "**Skill card.** Still *Linear equations in one variable*, in the **Algebra** "
            "domain — but this is the dressed version, and it is where most of the lost points "
            "on this skill live. The algebra is easy; the translation is what the test is "
            "grading.",
            "The method is always the same four moves. Name the unknown and write down in "
            "words what the letter stands for. Find the quantity the paragraph pins down — a "
            "total paid, a distance covered, the amount of acid in a beaker. Write that "
            "quantity a second way, using your letter. Set the two ways equal and solve.",
            "Naming matters more than it looks. When one quantity is described in terms of "
            "another, name the one being described FROM. 'A number is eight more than three "
            "times a second number' — name the second number $n$, and the first is $3n + 8$. "
            "Name the first number $n$ instead and the second becomes $\\frac{n - 8}{3}$, "
            "which is correct and three times the work.",
            "**The test's angle.** Two traps appear on nearly every word problem. The first is "
            "the unfinished answer: the equation gives $n$, the question asks for the smaller "
            "of the two numbers, or the total, or how much was added — and the value of $n$ is "
            "sitting right there in the options. The second is percent direction: a $40\\%$ "
            "markup means the price is $1.4$ times the COST, and you cannot recover the cost "
            "by taking $40\\%$ off the price.",
        ],
        key_idea=(
            "One quantity, written two ways, is an equation. Name the unknown, find the "
            "quantity the paragraph fixes, express it twice, and then check which number the "
            "final sentence asked for."
        ),
        facts=[
            fact(
                "Fee plus rate",
                "\\text{total} = \\text{one-time fee} + (\\text{rate}) \\times (\\text{number of units})",
                "The single most common SAT context. The fee is the constant term; the rate is "
                "the coefficient.",
            ),
            fact(
                "Percent increase and decrease",
                "\\text{new} = (1 + r)\\,\\text{old}, \\qquad \\text{new} = (1 - r)\\,\\text{old}",
                "A $40\\%$ markup multiplies by $1.4$; a $40\\%$ discount multiplies by $0.6$. "
                "Reversing them means dividing, never subtracting the same percent back.",
            ),
            fact(
                "Consecutive integers",
                "n - 1,\\; n,\\; n + 1 \\;\\Longrightarrow\\; \\text{sum} = 3n",
                "Naming the MIDDLE integer makes the sum collapse. For consecutive even or odd "
                "integers use $n - 2,\\, n,\\, n + 2$.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Answering with the letter you solved for instead of the quantity asked about.",
                "Underline the last sentence of the question before you start. The value you "
                "solved for is almost always one of the wrong options.",
            ),
            mistake(
                "Undoing a percent increase by subtracting the same percent.",
                "A $40\\%$ markup means price $= 1.4 \\times$ cost, so cost $=$ price $\\div 1.4$. "
                "Taking $40\\%$ off the price gives a different, wrong number.",
            ),
            mistake(
                "Dividing the total by the rate and ignoring the one-time fee.",
                "Subtract the fee FIRST, then divide. $290 \\div 25$ answers a question nobody asked.",
            ),
            mistake(
                "In a dilution problem, treating the concentration as the thing that stays fixed.",
                "Adding water changes the concentration — that is the point of the question. "
                "The amount of the dissolved substance is what stays fixed.",
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
        "sat-le-p01",
        "If $2(x - 6) = 8$, what is the value of $x$?",
        "**Answer.** $x = 10$. Divide both sides by $2$ first: $x - 6 = 4$, so $x = 10$. "
        "Distributing first also works: $2x - 12 = 8$, $2x = 20$, $x = 10$.",
        ["Eq(2*(10 - 6), 8)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Easy"}],
    ),
    problem(
        "sat-le-p02",
        "If $\\dfrac{3x}{5} = 12$, what is the value of $x$?",
        "**Answer.** $x = 20$. Multiply both sides by $5$: $3x = 60$. Divide by $3$: $x = 20$.",
        ["Eq(Rational(3*20, 5), 12)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Easy"}],
    ),
    problem(
        "sat-le-p03",
        "If $6 - 3(x + 1) = 0$, what is the value of $x$?",
        "**Answer.** $x = 1$. Distribute the $-3$: $6 - 3x - 3 = 0$, so $3 - 3x = 0$ and "
        "$x = 1$. Writing $6 - 3x + 3$ — forgetting that the $-3$ hits the $+1$ — gives "
        "$x = 3$, a listed option.",
        ["Eq(6 - 3*(1 + 1), 0)", "Ne(6 - 3*(3 + 1), 0)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Easy"}],
    ),
    problem(
        "sat-le-p04",
        "If $\\dfrac{x + 1}{2} - \\dfrac{x - 1}{5} = 4$, what is the value of $x$?",
        "**Answer.** $x = 11$. Multiply every term by $10$: $5(x + 1) - 2(x - 1) = 40$. "
        "Distribute, watching the negative: $5x + 5 - 2x + 2 = 40$, so $3x + 7 = 40$, "
        "$3x = 33$ and $x = 11$. Check: $\\frac{12}{2} - \\frac{10}{5} = 6 - 2 = 4$.",
        [
            "Eq((11 + 1)/2 - (11 - 1)/5, 4)",
            "Eq(solve(Eq((x + 1)/2 - (x - 1)/5, 4), x)[0], 11)",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-p05",
        "If $4x - 9 = 23$, what is the value of $4x - 3$?",
        "**Answer.** $29$. The two expressions differ by $6$: $4x - 3 = (4x - 9) + 6 = "
        "23 + 6 = 29$. No need to find $x$ at all. (For the record, $x = 8$ — a listed trap.)",
        ["Eq(4*8 - 9, 23)", "Eq(4*8 - 3, 29)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-p06",
        "$$7x + 3 = kx - 5$$\n"
        "In the equation above, $k$ is a constant. If the equation has no solution, what is "
        "the value of $k$?",
        "**Answer.** $k = 7$. No solution needs the $x$ terms to cancel while the constants "
        "disagree. Setting $k = 7$ gives $7x + 3 = 7x - 5$, and subtracting $7x$ leaves "
        "$3 = -5$, which is false for every $x$. The constants already disagree, so $k = 7$ "
        "is exactly the value that produces no solution.",
        ["Ne(3, -5)", "Eq(7*x + 3 - (7*x - 5), 8)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-p07",
        "$$a(x + 3) = 5x + b$$\n"
        "In the equation above, $a$ and $b$ are constants. If the equation has infinitely "
        "many solutions, what is the value of $b$?",
        "**Answer.** $b = 15$. Distribute: $ax + 3a = 5x + b$. Matching the $x$ terms gives "
        "$a = 5$; matching the constants then gives $b = 3a = 15$. Both must match — matching "
        "only the coefficients would give no solution instead.",
        ["Eq(5*(x + 3) - (5*x + 15), 0)", "Eq(3*5, 15)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Hard"}],
    ),
    problem(
        "sat-le-p08",
        "A printer produces $18$ pages per minute after a fixed warm-up of $40$ seconds. A "
        "job finished $4$ minutes after the print button was pressed. How many pages were "
        "printed?",
        "**Answer.** $60$ pages. The warm-up eats $40$ seconds, leaving "
        "$4 - \\frac{40}{60} = \\frac{10}{3}$ minutes of printing. At $18$ pages per minute "
        "that is $18 \\times \\frac{10}{3} = 60$ pages. Ignoring the warm-up gives $72$, the "
        "trap option.",
        [
            "Eq(4 - Rational(40,60), Rational(10,3))",
            "Eq(18*Rational(10,3), 60)",
            "Ne(18*4, 60)",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-p09",
        "The perimeter of a rectangle is $54$ centimetres. The length is $3$ centimetres more "
        "than twice the width. What is the width, in centimetres?",
        "**Answer.** $8$ centimetres. Let $w$ be the width; the length is $2w + 3$. Perimeter "
        "is twice the sum of the sides:\n"
        "$$2\\left(w + (2w + 3)\\right) = 54$$\n"
        "$$2(3w + 3) = 54$$\n"
        "$$6w + 6 = 54$$\n"
        "$$w = 8$$\n"
        "The length is $19$, and $2(8 + 19) = 54$ confirms it. The trap option is $19$.",
        ["Eq(2*(8 + (2*8 + 3)), 54)", "Eq(2*8 + 3, 19)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-p10",
        "A solution of $300$ millilitres is $12\\%$ salt. How many millilitres of pure salt "
        "must be added so that the mixture is $20\\%$ salt?",
        "**Answer.** $30$ millilitres. The solution starts with $0.12 \\times 300 = 36$ mL of "
        "salt. Adding $s$ mL of salt raises BOTH the salt and the total:\n"
        "$$\\frac{36 + s}{300 + s} = 0.20$$\n"
        "$$36 + s = 60 + 0.2s$$\n"
        "$$0.8s = 24$$\n"
        "$$s = 30$$\n"
        "Check: $66$ mL of salt in $330$ mL is exactly $20\\%$. The common error is holding "
        "the total at $300$, which gives $24$.",
        [
            "Eq(Rational(36 + 30, 300 + 30), Rational(20, 100))",
            "Eq(Rational(12,100)*300, 36)",
            "Ne(Rational(36 + 24, 300 + 24), Rational(20,100))",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Hard"}],
    ),
    problem(
        "sat-le-p11",
        "If $\\dfrac{2}{3}(9x - 6) = 6x + c$ for all values of $x$, what is the value of $c$?",
        "**Answer.** $c = -4$. Distribute the $\\frac{2}{3}$ across both terms: "
        "$\\frac{2}{3}(9x) = 6x$ and $\\frac{2}{3}(-6) = -4$, so the left side is $6x - 4$. "
        "'For all values of $x$' means the two sides are the same expression, so the $x$ terms "
        "match automatically and $c = -4$. Distributing over the $9x$ only — a very common "
        "slip — leaves $6x - 6$ and the wrong answer $-6$.",
        ["Eq(Rational(2,3)*(9*x - 6), 6*x - 4)", "Eq(Rational(2,3)*(-6), -4)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Hard"}],
    ),
    problem(
        "sat-le-p12",
        "Jamal is $4$ years older than his sister. In $6$ years the sum of their ages will be "
        "$40$. How old is Jamal now?",
        "**Answer.** $16$. Let $s$ be the sister's age now; Jamal is $s + 4$. In six years "
        "they are $s + 6$ and $s + 10$:\n"
        "$$(s + 6) + (s + 10) = 40$$\n"
        "$$2s + 16 = 40$$\n"
        "$$s = 12$$\n"
        "So the sister is $12$ and Jamal is $s + 4 = 16$. Check: in six years they are $18$ "
        "and $22$, which sum to $40$. The trap is answering $12$ — the sister's age, not "
        "Jamal's.",
        ["Eq((12 + 6) + (12 + 4 + 6), 40)", "Eq(12 + 4, 16)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
]

TEST = [
    problem(
        "sat-le-x01",
        "If $3(x + 4) = 2(x - 1)$, what is the value of $x$?",
        "**Answer.** $x = -14$. Distribute both sides: $3x + 12 = 2x - 2$. Subtract $2x$: "
        "$x + 12 = -2$. Subtract $12$: $x = -14$. Check: $3(-10) = -30$ and $2(-15) = -30$.",
        ["Eq(3*(-14 + 4), 2*(-14 - 1))"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Easy"}],
    ),
    problem(
        "sat-le-x02",
        "If $5x - 2 = 18$, what is the value of $10x - 4$?",
        "**Answer.** $36$. $10x - 4$ is exactly twice $5x - 2$, so it is $2 \\times 18 = 36$. "
        "Solving gives $x = 4$, which is a listed distractor.",
        ["Eq(5*4 - 2, 18)", "Eq(10*4 - 4, 36)", "Eq(2*18, 36)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-x03",
        "$$8x + m = 4(2x + 3)$$\n"
        "In the equation above, $m$ is a constant. If the equation has infinitely many "
        "solutions, what is the value of $m$?",
        "**Answer.** $m = 12$. Distribute the right side: $8x + m = 8x + 12$. The $x$ terms "
        "already match, so infinitely many solutions requires the constants to match too: "
        "$m = 12$. Any other value gives no solution — there is no value of $m$ producing "
        "exactly one solution here.",
        ["Eq(8*x + 12 - 4*(2*x + 3), 0)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-x04",
        "A car rental costs $\\$45$ per day plus $\\$0.30$ per kilometre. A two-day rental "
        "cost $\\$132$. How many kilometres were driven?",
        "**Answer.** $140$ kilometres. Two days cost $2 \\times 45 = 90$, so the distance "
        "charge was $132 - 90 = 42$ dollars. At $\\$0.30$ per kilometre that is "
        "$42 \\div 0.30 = 140$ kilometres. Forgetting to double the daily rate gives "
        "$290$ kilometres.",
        [
            "Eq(2*45 + Rational(30,100)*140, 132)",
            "Eq(Rational(132 - 90, 1)/Rational(30,100), 140)",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-x05",
        "If $\\dfrac{x}{2} + \\dfrac{x}{3} + \\dfrac{x}{6} = 12$, what is the value of $x$?",
        "**Answer.** $x = 12$. Multiply every term by $6$: $3x + 2x + x = 72$, so $6x = 72$ "
        "and $x = 12$. The three fractions sum to exactly one whole $x$, which is the "
        "structural shortcut: $\\frac12 + \\frac13 + \\frac16 = 1$.",
        [
            "Eq(Rational(1,2) + Rational(1,3) + Rational(1,6), 1)",
            "Eq(Rational(12,2) + Rational(12,3) + Rational(12,6), 12)",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
    problem(
        "sat-le-x06",
        "The price of a coat after a $25\\%$ discount is $\\$96$. What was the price before "
        "the discount, in dollars?",
        "**Answer.** $\\$128$. A $25\\%$ discount multiplies by $0.75$, so $0.75p = 96$ and "
        "$p = 128$. Check: $25\\%$ of $128$ is $32$, and $128 - 32 = 96$. Adding $25\\%$ to "
        "$96$ gives $120$, which is the trap — a percentage of the smaller number is a "
        "smaller amount.",
        [
            "Eq(Rational(75,100)*128, 96)",
            "Eq(128 - Rational(25,100)*128, 96)",
            "Ne(96 + Rational(25,100)*96, 128)",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Hard"}],
    ),
    problem(
        "sat-le-x07",
        "$$3(2x + 1) = 6x + c$$\n"
        "In the equation above, $c$ is a constant. The equation has no solution. Which value "
        "can $c$ NOT have?",
        "**Answer.** $c = 3$. Distribute the left side: $6x + 3 = 6x + c$. The $x$ terms are "
        "identical, so subtracting $6x$ leaves $3 = c$ — a statement with no variable in it. "
        "When $c = 3$ that statement is true and every real number is a solution; for every "
        "other $c$ it is false and there is no solution. So 'no solution' rules out exactly "
        "one value, $c = 3$.",
        ["Eq(3*(2*x + 1) - (6*x + 3), 0)", "Ne(3*(2*x + 1), 6*x + 5)"],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Hard"}],
    ),
    problem(
        "sat-le-x08",
        "A tank holds $600$ litres. It is $\\tfrac{1}{4}$ full and a hose adds $15$ litres "
        "per minute. After how many minutes is the tank $\\tfrac{3}{4}$ full?",
        "**Answer.** $20$ minutes. The tank starts with $150$ litres and needs to reach $450$ "
        "litres — a gain of $300$ litres. At $15$ litres per minute that takes "
        "$300 \\div 15 = 20$ minutes. Using $450 \\div 15 = 30$ ignores the water already "
        "there.",
        [
            "Eq(Rational(1,4)*600 + 15*20, Rational(3,4)*600)",
            "Eq(Rational(3,4)*600 - Rational(1,4)*600, 300)",
        ],
        badges=[{"text": "sat-linear-eq-one-var", "mono": True}, {"text": "Medium"}],
    ),
]


def main():
    lessons = [lesson_solving(), lesson_how_many(), lesson_word_problems()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Linear Equations in One Variable",
        1,
        "The skill every other Algebra question stands on: clearing fractions and decimals, "
        "distributing without losing a sign, deciding whether an equation has one solution, "
        "none, or every number at once — and finding the equation hiding inside a paragraph.",
        None,
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
