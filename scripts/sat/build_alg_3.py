#!/usr/bin/env python3
"""SAT Math — Algebra, Unit 3: Linear functions.

Builds data/genmath/sat/linear-functions.json. Unit 2 taught the LINE; this
unit teaches the FUNCTION — notation, evaluation, reading one out of a graph
or a table, and comparing two of them. Three lessons.

Run: python3 scripts/sat/build_alg_3.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "linear-functions"
TAG = {"text": "sat-linear-functions", "mono": True}


def _b(level):
    return [TAG, {"text": level}]


# ===========================================================================
# Lesson 1 — function notation
# ===========================================================================

def lesson_notation():
    worked = [
        problem(
            "sat-l3a-w1",
            "The function $f$ is defined by $f(x) = 7 - 4x$. What is the value of $f(-3)$?",
            "**Answer.** $19$.  \n"
            "Function notation is an instruction: replace every $x$ in the rule with the "
            "number in the brackets, then compute.\n"
            "$$f(-3) = 7 - 4(-3)$$\n"
            "$$= 7 + 12$$\n"
            "$$= 19$$\n"
            "The double negative is the whole difficulty. Subtracting a negative adds, so "
            "$-4(-3) = +12$ — writing $-12$ instead gives $-5$, a listed option.  \n"
            "Note what $f(-3)$ is NOT: it is not $f$ multiplied by $-3$. The brackets are not "
            "multiplication anywhere in function notation.",
            ["Eq(7 - 4*(-3), 19)", "Ne(7 - 12, 19)"],
        ),
        problem(
            "sat-l3a-w2",
            "The function $g$ is defined by $g(x) = 5x + 2$. If $g(a) = 37$, what is the "
            "value of $a$?",
            "**Answer.** $7$.  \n"
            "This is the machine run backwards: you are told the OUTPUT and asked for the "
            "input. Set the rule equal to the given output:\n"
            "$$5a + 2 = 37$$\n"
            "$$5a = 35$$\n"
            "$$a = 7$$\n"
            "Check by running it forwards: $g(7) = 5(7) + 2 = 37$.  \n"
            "The commonest error is evaluating instead of solving — computing $g(37) = 187$ "
            "answers a different question.",
            ["Eq(5*7 + 2, 37)", "Eq(solve(Eq(5*a + 2, 37), a)[0], 7)"],
        ),
        problem(
            "sat-l3a-w3",
            "For the linear function $h$, the table below gives some values of $x$ and "
            "$h(x)$.\n\n"
            "| $x$ | $h(x)$ |\n| --- | --- |\n| $0$ | $-4$ |\n| $3$ | $5$ |\n| $6$ | $14$ |\n\n"
            "What is the value of $h(10)$?",
            "**Answer.** $26$.  \n"
            "The $x$-values step by $3$ and the outputs step by $9$ each time, so the function "
            "is linear with rate\n"
            "$$m = \\frac{9}{3} = 3$$\n"
            "The row $x = 0$ is handed to you, so $h(0) = -4$ is the $y$-intercept directly:\n"
            "$$h(x) = 3x - 4$$\n"
            "$$h(10) = 30 - 4 = 26$$\n"
            "Check the table: $h(3) = 5$ and $h(6) = 14$, both correct.  \n"
            "When the table has no $x = 0$ row you must compute the intercept from a row "
            "instead — but here the test gave it away.",
            [
                "Eq(Rational(5 - (-4), 3 - 0), 3)",
                "Eq(3*0 - 4, -4)",
                "Eq(3*6 - 4, 14)",
                "Eq(3*10 - 4, 26)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l3a-t1",
            "The function $f$ is defined by $f(x) = 2x - 9$. What is $f(4)$?",
            "**Answer.** $-1$. Substitute: $f(4) = 2(4) - 9 = 8 - 9 = -1$.",
            ["Eq(2*4 - 9, -1)"],
        ),
        problem(
            "sat-l3a-t2",
            "The function $p$ is defined by $p(x) = -3x + 11$. For what value of $x$ is "
            "$p(x) = 2$?",
            "**Answer.** $3$. Set the rule equal to $2$: $-3x + 11 = 2$, so $-3x = -9$ and "
            "$x = 3$. Check: $p(3) = -9 + 11 = 2$.",
            ["Eq(-3*3 + 11, 2)", "Eq(solve(Eq(-3*x + 11, 2), x)[0], 3)"],
        ),
        problem(
            "sat-l3a-t3",
            "If $f(x) = 6x + 1$, what is the value of $f(5) - f(2)$?",
            "**Answer.** $18$. $f(5) = 31$ and $f(2) = 13$, so the difference is $18$.  \n"
            "Faster: for a linear function the difference in outputs is the slope times the "
            "difference in inputs, $6 \\times 3 = 18$ — the constant term cancels.",
            ["Eq((6*5 + 1) - (6*2 + 1), 18)", "Eq(6*(5 - 2), 18)"],
        ),
        problem(
            "sat-l3a-t4",
            "The function $f$ is defined by $f(x) = kx - 5$, and $f(3) = 4$. What is the value "
            "of $k$?",
            "**Answer.** $3$. Substitute both the input and the output: $k(3) - 5 = 4$, so "
            "$3k = 9$ and $k = 3$. Check: $f(3) = 3(3) - 5 = 4$.",
            ["Eq(3*3 - 5, 4)", "Eq(solve(Eq(k*3 - 5, 4), k)[0], 3)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Linear functions",
            "beats": [
                "Domain: Algebra — 13 to 15 of the 44 questions on the Math section.",
                "Roughly 3 questions per test carry function notation somewhere in them.",
                "Prerequisite: slope and intercepts from Unit 2.",
                "The notation is the hurdle, not the algebra — the algebra is one substitution.",
            ],
        },
        {
            "kind": "teach",
            "title": "f(x) is an instruction, not a product",
            "body": "$f(x)$ is read 'f of x' and it names the OUTPUT of the function $f$ when "
                    "the input is $x$. The brackets are not multiplication: $f(3)$ never means "
                    "$f$ times $3$. To evaluate, replace every $x$ in the rule with what is "
                    "inside the brackets and compute. The letter naming the function is "
                    "arbitrary — $f$, $g$, $h$, $C$, $P$ all behave identically.",
        },
        {
            "kind": "evaluator",
            "title": "The function as a machine",
            "teach": "Slide the input and watch the output. Each step of 1 in the input changes "
                     "the output by the same fixed amount — that fixed amount is the slope, and "
                     "it is what makes the function LINEAR.",
            "config": {"a": 5, "b": 2, "varName": "x", "min": -5, "max": 10, "start": 3},
        },
        {"kind": "worked", "title": "Evaluating with a negative input", "problemId": "sat-l3a-w1"},
        {
            "kind": "tapQuestion",
            "title": "Forwards or backwards?",
            "prompt": "If $f(x) = 4x - 1$, which question is asking you to SOLVE rather than to "
                      "evaluate?",
            "options": [
                "For what $x$ is $f(x) = 11$?",
                "What is $f(11)$?",
                "What is $f(0)$?",
                "What is $f(-2)$?",
            ],
            "correctIndex": 0,
            "explanation": "Option A gives the output and asks for the input, so you set "
                           "$4x - 1 = 11$ and solve, getting $x = 3$. The other three give an "
                           "input and ask for the output, which is a substitution.",
            "check": ["Eq(solve(Eq(4*x - 1, 11), x)[0], 3)", "Eq(4*11 - 1, 43)"],
        },
        {"kind": "worked", "title": "Running the machine backwards", "problemId": "sat-l3a-w2"},
        {
            "kind": "tip",
            "title": "Substitute the whole thing",
            "body": "When the input is an expression rather than a number — $f(2a)$, $f(x + 3)$ "
                    "— replace every $x$ with the WHOLE expression, brackets and all. For "
                    "$f(x) = 5x + 2$, $f(x + 3) = 5(x + 3) + 2 = 5x + 17$. Dropping the "
                    "brackets and writing $5x + 3 + 2$ is the classic slip.",
        },
        {"kind": "worked", "title": "A function given by a table", "problemId": "sat-l3a-w3"},
        {"kind": "tryIt", "title": "Your turn: evaluate", "problemId": "sat-l3a-t1"},
        {"kind": "tryIt", "title": "Your turn: solve for the input", "problemId": "sat-l3a-t2"},
        {"kind": "tryIt", "title": "Your turn: a difference of outputs", "problemId": "sat-l3a-t3"},
        {"kind": "tryIt", "title": "Your turn: find the constant", "problemId": "sat-l3a-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "f(x) is the output for input x — the brackets never mean multiplication.",
                "Given the input, substitute. Given the output, set the rule equal to it and solve.",
                "Replace x with the WHOLE input expression, keeping its brackets.",
                "For a linear function, a difference of outputs equals the slope times the difference of inputs.",
                "If the rule contains an unknown constant, one input-output pair pins it down.",
            ],
        },
    ]

    return lesson(
        slug="function-notation",
        title="Function Notation and Evaluating",
        concrete=(
            "A vending machine takes a code and returns a snack. Press B4 and you get exactly "
            "one thing, every time. A function is that machine written down: $f(\\text{B4})$ "
            "names what comes out, and the whole of function notation is deciding whether the "
            "question hands you the button or the snack."
        ),
        objective=(
            "Evaluate a linear function at a number or an expression, solve for the input when "
            "the output is given, and read a linear function out of a table of values."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Linear functions*, in the "
            "**Algebra** domain. It is the notation layer over everything Unit 2 taught: same "
            "lines, same slopes, new vocabulary. Roughly three questions a test involve "
            "function notation somewhere, and losing them is almost always a notation problem "
            "rather than an algebra problem.",
            "$f(x)$ names the output of the function $f$ for the input $x$. The brackets are "
            "not multiplication — $f(3)$ is never $f$ times $3$. Evaluating means replacing "
            "every $x$ in the rule with what sits inside the brackets. If the input is an "
            "expression, replace $x$ with the whole expression and keep its brackets: for "
            "$f(x) = 5x + 2$, $f(x + 3) = 5(x + 3) + 2$.",
            "There are exactly two directions. Given the input, substitute and compute. Given "
            "the OUTPUT — 'if $g(a) = 37$' — set the rule equal to that output and solve. The "
            "same rule serves both; only the direction changes.",
            "**The test's angle.** Linear functions are the ones whose outputs change by a "
            "constant amount for each constant step in the input, so a table with evenly "
            "spaced $x$-values and evenly spaced outputs is announcing that it is linear. From "
            "there the rate is one output step over one input step, and the constant term is "
            "$f(0)$ — often handed to you as a table row.",
        ],
        key_idea=(
            "$f(x)$ is the output for the input $x$. Input given means substitute; output "
            "given means solve. A linear function changes its output by the same amount for "
            "every equal step in the input."
        ),
        facts=[
            fact(
                "Function notation",
                "f(x) = mx + b \\;\\Longrightarrow\\; f(c) = mc + b",
                "Replace every $x$ by $c$. The brackets never mean multiplication.",
            ),
            fact(
                "Difference of outputs",
                "f(x_2) - f(x_1) = m\\,(x_2 - x_1)",
                "For a linear function the constant term cancels, so a difference of outputs "
                "is the slope times the difference of inputs.",
            ),
            fact(
                "The constant term is the output at zero",
                "f(0) = b",
                "If a table contains an $x = 0$ row, the intercept is read straight off it.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Reading $f(3)$ as $f$ multiplied by $3$.",
                "The brackets in function notation hold the input. Nothing is being multiplied.",
            ),
            mistake(
                "Evaluating when the question gives the output.",
                "'If $g(a) = 37$' means $37$ came OUT. Set the rule equal to $37$ and solve for "
                "$a$; computing $g(37)$ answers a question nobody asked.",
            ),
            mistake(
                "Dropping the brackets when the input is an expression.",
                "For $f(x) = 5x + 2$, $f(x + 3)$ is $5(x + 3) + 2$, not $5x + 3 + 2$. The "
                "coefficient multiplies the whole input.",
            ),
            mistake(
                "Losing a sign when the input is negative.",
                "In $f(x) = 7 - 4x$, $f(-3) = 7 - 4(-3) = 7 + 12$. A negative times a negative "
                "is positive.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — reading a linear function from a graph
# ===========================================================================

def lesson_graphs():
    worked = [
        problem(
            "sat-l3b-w1",
            "The graph of the linear function $f$ in the $xy$-plane passes through $(0, 12)$ "
            "and $(8, 0)$. Which equation defines $f$?",
            "**Answer.** $f(x) = -\\dfrac{3}{2}x + 12$.  \n"
            "The two points given are the two intercepts, which is the friendliest case there "
            "is. The $y$-intercept is $12$, so the constant term is $12$ with no work. The "
            "slope comes from the two points:\n"
            "$$m = \\frac{0 - 12}{8 - 0} = \\frac{-12}{8} = -\\frac{3}{2}$$\n"
            "So $f(x) = -\\frac{3}{2}x + 12$.  \n"
            "Check the second point: $-\\frac{3}{2}(8) + 12 = -12 + 12 = 0$.  \n"
            "A line falling from left to right must have a negative slope — that alone kills "
            "half the option list before you compute anything.",
            [
                "Eq(Rational(0 - 12, 8 - 0), -Rational(3,2))",
                "Eq(-Rational(3,2)*8 + 12, 0)",
                "Eq(-Rational(3,2)*0 + 12, 12)",
            ],
        ),
        problem(
            "sat-l3b-w2",
            "The graph of $y = f(x)$ is a line with $x$-intercept $(-5, 0)$ and "
            "$y$-intercept $(0, 4)$. What is the value of $f(5)$?",
            "**Answer.** $8$.  \n"
            "Build the function from the two intercepts. The $y$-intercept gives the constant "
            "term $4$, and the slope is\n"
            "$$m = \\frac{4 - 0}{0 - (-5)} = \\frac{4}{5}$$\n"
            "$$f(x) = \\frac{4}{5}x + 4$$\n"
            "$$f(5) = 4 + 4 = 8$$\n"
            "There is a faster route on the graph itself: from $x = -5$ to $x = 0$ the output "
            "rises by $4$, so from $x = 0$ to $x = 5$ — the same run — it rises by $4$ again, "
            "landing on $8$. Equal runs give equal rises, which is what 'linear' means.",
            [
                "Eq(Rational(4 - 0, 0 - (-5)), Rational(4,5))",
                "Eq(Rational(4,5)*5 + 4, 8)",
                "Eq(Rational(4,5)*(-5) + 4, 0)",
            ],
        ),
        problem(
            "sat-l3b-w3",
            "The function $f$ is linear, $f(2) = 11$ and $f(6) = 3$. What is the value of "
            "$f(0)$?",
            "**Answer.** $15$.  \n"
            "Two input-output pairs are two points, $(2, 11)$ and $(6, 3)$:\n"
            "$$m = \\frac{3 - 11}{6 - 2} = \\frac{-8}{4} = -2$$\n"
            "Now use either pair in $f(x) = -2x + b$. Taking $(2, 11)$:\n"
            "$$11 = -4 + b \\;\\Longrightarrow\\; b = 15$$\n"
            "And $f(0) = b = 15$.  \n"
            "The step-back shortcut: from $x = 2$ down to $x = 0$ is a run of $-2$, and with "
            "slope $-2$ that raises the output by $4$, from $11$ to $15$. Same answer, no "
            "equation written.",
            [
                "Eq(Rational(3 - 11, 6 - 2), -2)",
                "Eq(-2*2 + 15, 11)",
                "Eq(-2*6 + 15, 3)",
                "Eq(-2*0 + 15, 15)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l3b-t1",
            "A line passes through $(0, -6)$ and $(4, 2)$. Which function does it define?",
            "**Answer.** $f(x) = 2x - 6$. The $y$-intercept is $-6$ and the slope is "
            "$\\frac{2 - (-6)}{4 - 0} = \\frac{8}{4} = 2$.",
            ["Eq(Rational(2 - (-6), 4 - 0), 2)", "Eq(2*4 - 6, 2)"],
        ),
        problem(
            "sat-l3b-t2",
            "The linear function $g$ satisfies $g(1) = 7$ and $g(4) = 16$. What is $g(0)$?",
            "**Answer.** $4$. The slope is $\\frac{16 - 7}{4 - 1} = 3$, so $g(x) = 3x + b$ and "
            "$7 = 3 + b$ gives $b = 4$. Then $g(0) = 4$.",
            ["Eq(Rational(16 - 7, 4 - 1), 3)", "Eq(3*1 + 4, 7)", "Eq(3*4 + 4, 16)"],
        ),
        problem(
            "sat-l3b-t3",
            "The graph of a linear function has $x$-intercept $(3, 0)$ and passes through "
            "$(0, -9)$. What is the slope?",
            "**Answer.** $3$. $m = \\frac{0 - (-9)}{3 - 0} = \\frac{9}{3} = 3$. A line "
            "crossing below the origin and rising to cross the $x$-axis to the right must "
            "climb, so a negative answer would be impossible.",
            ["Eq(Rational(0 - (-9), 3 - 0), 3)", "Eq(3*3 - 9, 0)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "A graph carries the same two numbers",
            "beats": [
                "Where the line crosses the vertical axis is f(0) — the constant term.",
                "How steeply it climbs between any two lattice points is the slope.",
                "Both intercepts given is the friendliest case: one IS the constant term.",
                "Falling left to right means a negative slope, before any arithmetic.",
            ],
        },
        {
            "kind": "coordinateGrid",
            "title": "Two intercepts pin a line",
            "teach": "The points shown are the two intercepts of one line. Read the constant "
                     "term straight off the vertical axis, then count the rise and run between "
                     "the two points for the slope.",
            "config": {"mode": "plot", "min": -8, "max": 14,
                       "points": [{"x": 0, "y": 12, "label": "y-int"}, {"x": 8, "y": 0, "label": "x-int"}]},
        },
        {"kind": "worked", "title": "A function from its two intercepts", "problemId": "sat-l3b-w1"},
        {
            "kind": "tapQuestion",
            "title": "Sanity-check the sign",
            "prompt": "A line passes through $(0, 5)$ and $(10, 1)$. Without computing, what "
                      "must be true of its slope?",
            "options": [
                "It is negative, because the output falls as $x$ grows",
                "It is positive, because both coordinates are positive",
                "It is zero, because the line is nearly flat",
                "It cannot be determined from two points",
            ],
            "correctIndex": 0,
            "explanation": "Going from $x = 0$ to $x = 10$ the output drops from $5$ to $1$, so "
                           "the slope is negative — it is $\\frac{1 - 5}{10 - 0} = -0.4$. Two "
                           "distinct points always determine a slope, and 'nearly flat' is "
                           "still not flat.",
            "check": ["Eq(Rational(1 - 5, 10 - 0), -Rational(2,5))", "-Rational(2,5) < 0"],
        },
        {"kind": "worked", "title": "Evaluating from a graph", "problemId": "sat-l3b-w2"},
        {
            "kind": "tip",
            "title": "Step along the line instead of solving",
            "body": "Because a linear function changes by the same amount over equal runs, you "
                    "can often walk to the answer. If $f(2) = 11$ and the slope is $-2$, then "
                    "$f(1) = 13$ and $f(0) = 15$ — two steps, no equation. On a hard item this "
                    "is faster than finding $b$, and it is much harder to get wrong.",
        },
        {"kind": "worked", "title": "Two values pin the function", "problemId": "sat-l3b-w3"},
        {"kind": "tryIt", "title": "Your turn: from two points", "problemId": "sat-l3b-t1"},
        {"kind": "tryIt", "title": "Your turn: find the constant term", "problemId": "sat-l3b-t2"},
        {"kind": "tryIt", "title": "Your turn: slope from intercepts", "problemId": "sat-l3b-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "The y-intercept of a graph IS the constant term of the function.",
                "Two input-output pairs are two points: slope first, then substitute for the constant.",
                "Equal runs give equal rises — step along the line instead of solving when you can.",
                "A falling line has a negative slope; use that to eliminate options first.",
                "A horizontal line has slope zero; a vertical line is not a function at all.",
            ],
        },
    ]

    return lesson(
        slug="linear-functions-from-graphs-and-tables",
        title="Reading a Linear Function from a Graph or a Table",
        concrete=(
            "A delivery drone's altitude readout shows $12$ metres at launch and zero after "
            "eight seconds. You never see the equation, but those two readings contain it "
            "entirely — and any question about second three, or second seven, is already "
            "answered by the picture."
        ),
        objective=(
            "Build the equation of a linear function from a graph, a pair of intercepts, or "
            "two input-output pairs, and evaluate it anywhere."
        ),
        concept=[
            "**Skill card.** Still *Linear functions*, in the **Algebra** domain. This is the "
            "version that arrives as a picture or a table rather than as a formula, and it is "
            "where the SAT tests whether you can move between representations without losing "
            "anything.",
            "A graph carries exactly the same two numbers a formula does. The height at which "
            "the line crosses the vertical axis is $f(0)$, which is the constant term. The "
            "steepness between any two points on the line is the slope. Get both and the "
            "equation writes itself.",
            "Two intercepts is the friendliest case, because one of them is the constant term "
            "already. Two arbitrary input-output pairs need one extra step: find the slope "
            "from the pair, then substitute either pair back to find the constant.",
            "**The test's angle.** Because equal runs produce equal rises, you can often WALK "
            "to the answer rather than solve for anything. If $f(2) = 11$ and the slope is "
            "$-2$, then stepping back two units of $x$ raises the output by $4$, so "
            "$f(0) = 15$. On a timed test that is both faster and safer than solving for the "
            "constant. And before any of it: a line that falls left to right has a negative "
            "slope, which usually eliminates two options for free.",
        ],
        key_idea=(
            "Every representation of a linear function — graph, table, formula, sentence — "
            "carries the same two numbers. Find the rate and the starting value and you can "
            "convert between all four."
        ),
        facts=[
            fact(
                "The intercept is the constant term",
                "f(0) = b",
                "Whatever height the graph crosses the vertical axis at is the constant term "
                "of the formula.",
            ),
            fact(
                "Equal runs, equal rises",
                "f(x + d) - f(x) = md \\text{ for every } x",
                "This is what makes a function linear, and it is what lets you step along the "
                "line to a value instead of solving.",
            ),
            fact(
                "From two input-output pairs",
                "m = \\frac{f(x_2) - f(x_1)}{x_2 - x_1}",
                "Two pairs are two points. Same slope formula, function notation on top.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Using the $x$-intercept as the constant term.",
                "The constant term is the value at $x = 0$, which is the $y$-intercept. The "
                "$x$-intercept is where the output is zero.",
            ),
            mistake(
                "Giving a positive slope to a line that falls from left to right.",
                "Check the direction before computing. A falling line has a negative slope, "
                "full stop.",
            ),
            mistake(
                "Assuming a table's first output is $f(0)$.",
                "Only when that row's input is $0$. Otherwise the constant term has to be "
                "computed from a row.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 3 — comparing linear functions
# ===========================================================================

def lesson_comparing():
    worked = [
        problem(
            "sat-l3c-w1",
            "Company A charges $\\$60$ plus $\\$8$ per hour. Company B charges $\\$20$ plus "
            "$\\$12$ per hour. After how many hours do the two companies charge the same "
            "amount?",
            "**Answer.** $10$ hours.  \n"
            "Write both as functions of the hours $h$:\n"
            "$$A(h) = 8h + 60, \\qquad B(h) = 12h + 20$$\n"
            "'Charge the same amount' means the two outputs are equal:\n"
            "$$8h + 60 = 12h + 20$$\n"
            "$$40 = 4h$$\n"
            "$$h = 10$$\n"
            "Both charge $8(10) + 60 = 140$ dollars at that point, and $12(10) + 20 = 140$ "
            "confirms it.  \n"
            "Company B starts cheaper but climbs faster, so it is cheaper before ten hours and "
            "dearer after — the steeper line always wins eventually. That crossover reasoning "
            "is what the follow-up question usually asks about.",
            [
                "Eq(8*10 + 60, 12*10 + 20)",
                "Eq(8*10 + 60, 140)",
                "Eq(solve(Eq(8*h + 60, 12*h + 20), h)[0], 10)",
                "12*5 + 20 < 8*5 + 60",
                "12*15 + 20 > 8*15 + 60",
            ],
        ),
        problem(
            "sat-l3c-w2",
            "The function $f$ is defined by $f(x) = 3x - 5$. The function $g$ is defined by "
            "$g(x) = f(x) + 7$. What is the $y$-intercept of the graph of $g$?",
            "**Answer.** $(0, 2)$.  \n"
            "Adding a constant to a function shifts its whole graph up by that amount:\n"
            "$$g(x) = (3x - 5) + 7 = 3x + 2$$\n"
            "The slope is untouched — the two lines are parallel — and the intercept moves "
            "from $-5$ up to $2$.  \n"
            "Check directly: $g(0) = f(0) + 7 = -5 + 7 = 2$.  \n"
            "Adding INSIDE the brackets is a different transformation entirely: "
            "$f(x + 7) = 3(x + 7) - 5 = 3x + 16$, a shift LEFT rather than up, and it gives a "
            "different intercept. The SAT tests this contrast directly.",
            [
                "Eq(3*0 - 5 + 7, 2)",
                "Eq(expand(3*(x + 7) - 5), 3*x + 16)",
                "Ne(3*0 + 16, 2)",
            ],
        ),
        problem(
            "sat-l3c-w3",
            "The table shows values of two linear functions.\n\n"
            "| $x$ | $f(x)$ | $g(x)$ |\n| --- | --- | --- |\n"
            "| $0$ | $2$ | $17$ |\n| $4$ | $14$ | $13$ |\n| $8$ | $26$ | $9$ |\n\n"
            "For what value of $x$ does $f(x) = g(x)$?",
            "**Answer.** $3.75$.  \n"
            "Read both rates off the table. Over each step of $4$ in $x$, $f$ gains $12$ and "
            "$g$ loses $4$:\n"
            "$$m_f = \\frac{12}{4} = 3, \\qquad m_g = \\frac{-4}{4} = -1$$\n"
            "Both constant terms come free from the $x = 0$ row, so\n"
            "$$f(x) = 3x + 2, \\qquad g(x) = -x + 17$$\n"
            "Set them equal:\n"
            "$$3x + 2 = -x + 17$$\n"
            "$$4x = 15$$\n"
            "$$x = \\frac{15}{4} = 3.75$$\n"
            "Both functions equal $13.25$ there.  \n"
            "Notice where that falls. The table jumps from $x = 0$, where $g$ leads $17$ to "
            "$2$, straight to $x = 4$, where $f$ already leads $14$ to $13$. The crossing "
            "happened BETWEEN two rows, and no row shows it. Answering $4$ because that is "
            "the first row where $f$ is ahead is exactly the trap this item is built around.",
            [
                "Eq(Rational(14 - 2, 4 - 0), 3)",
                "Eq(Rational(13 - 17, 4 - 0), -1)",
                "Eq(solve(Eq(3*x + 2, -x + 17), x)[0], Rational(15,4))",
                "Eq(3*Rational(15,4) + 2, Rational(53,4))",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-l3c-t1",
            "Plan X costs $\\$25$ plus $\\$3$ per gigabyte. Plan Y costs $\\$10$ plus $\\$5$ "
            "per gigabyte. At how many gigabytes do they cost the same?",
            "**Answer.** $7.5$ gigabytes. Set $3g + 25 = 5g + 10$, so $15 = 2g$ and "
            "$g = 7.5$. Both cost $\\$47.50$ there.",
            [
                "Eq(solve(Eq(3*g + 25, 5*g + 10), g)[0], Rational(15,2))",
                "Eq(3*Rational(15,2) + 25, Rational(95,2))",
                "Eq(5*Rational(15,2) + 10, Rational(95,2))",
            ],
        ),
        problem(
            "sat-l3c-t2",
            "If $f(x) = 2x + 1$ and $h(x) = f(x) - 6$, what is $h(3)$?",
            "**Answer.** $1$. $h(x) = 2x + 1 - 6 = 2x - 5$, so $h(3) = 6 - 5 = 1$.  \n"
            "Or directly: $h(3) = f(3) - 6 = 7 - 6 = 1$.",
            ["Eq(2*3 + 1 - 6, 1)"],
        ),
        problem(
            "sat-l3c-t3",
            "Two linear functions satisfy $f(0) = 20$, $f(5) = 5$, $g(0) = 2$, and "
            "$g(5) = 12$. For what value of $x$ is $f(x) = g(x)$?",
            "**Answer.** $\\dfrac{18}{5}$, that is $3.6$. The rates are "
            "$\\frac{5 - 20}{5} = -3$ and $\\frac{12 - 2}{5} = 2$, so $f(x) = -3x + 20$ and "
            "$g(x) = 2x + 2$. Setting them equal: $18 = 5x$, so $x = 3.6$, where both equal "
            "$9.2$.",
            [
                "Eq(Rational(5 - 20, 5), -3)",
                "Eq(Rational(12 - 2, 5), 2)",
                "Eq(solve(Eq(-3*x + 20, 2*x + 2), x)[0], Rational(18,5))",
                "Eq(-3*Rational(18,5) + 20, Rational(46,5))",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Two functions, one question",
            "body": "When the SAT gives you two linear functions, it asks one of three "
                    "questions. When are they equal? That is setting the two rules equal and "
                    "solving. Which is bigger at a given input? That is evaluating both. Which "
                    "is bigger EVENTUALLY? That is comparing the two rates — the steeper "
                    "function always overtakes, no matter how far behind it starts.",
        },
        {
            "kind": "systemGraph",
            "title": "The crossover point",
            "teach": "Two costs, drawn as two lines. The cheaper option before the crossing is "
                     "the one that starts lower; the cheaper option after it is the one that "
                     "climbs more slowly. Drag them and watch the crossing move.",
            "config": {"m1": 8, "b1": 60, "m2": 12, "b2": 20, "interactive": True, "min": -2, "max": 20},
        },
        {"kind": "worked", "title": "When do two plans cost the same?", "problemId": "sat-l3c-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which one wins in the end?",
            "prompt": "Function $f$ has slope $2$ and starts at $100$. Function $g$ has slope "
                      "$9$ and starts at $10$. Which is larger for very large $x$?",
            "options": [
                "$g$, because its rate of change is larger",
                "$f$, because it starts far ahead",
                "They stay equal once they cross",
                "It depends on the value of $x$ chosen",
            ],
            "correctIndex": 0,
            "explanation": "A head start is a fixed amount; a bigger rate compounds with every "
                           "step. Here $2x + 100 = 9x + 10$ at $x = \\frac{90}{7}$, and beyond "
                           "that $g$ is permanently ahead. The steeper line always wins "
                           "eventually.",
            "check": [
                "Eq(solve(Eq(2*x + 100, 9*x + 10), x)[0], Rational(90,7))",
                "9*20 + 10 > 2*20 + 100",
                "9*5 + 10 < 2*5 + 100",
            ],
        },
        {
            "kind": "teach",
            "title": "Outside the brackets moves it up",
            "beats": [
                "g(x) = f(x) + 7 shifts the graph UP by 7 — the slope is unchanged.",
                "g(x) = f(x + 7) shifts the graph LEFT by 7 — also unchanged slope, different intercept.",
                "g(x) = 3f(x) multiplies every output by 3, tripling the slope AND the intercept.",
                "Outside the brackets acts on the output; inside acts on the input.",
            ],
        },
        {"kind": "worked", "title": "Shifting a linear function", "problemId": "sat-l3c-w2"},
        {
            "kind": "tip",
            "title": "Do not read a crossing off a table",
            "body": "A table only shows a few inputs, and two functions almost never cross "
                    "exactly at one of them. Use the table to get both RULES, then set the "
                    "rules equal and solve. The crossing usually lands between two rows, and "
                    "picking the nearest row is the trap the item is built around.",
        },
        {"kind": "worked", "title": "Two functions in one table", "problemId": "sat-l3c-w3"},
        {"kind": "tryIt", "title": "Your turn: equal cost", "problemId": "sat-l3c-t1"},
        {"kind": "tryIt", "title": "Your turn: a shifted function", "problemId": "sat-l3c-t2"},
        {"kind": "tryIt", "title": "Your turn: crossing from four values", "problemId": "sat-l3c-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "'Equal' means set the two rules equal and solve for the input.",
                "The function with the larger rate always overtakes, however far behind it starts.",
                "Adding outside the brackets shifts the output; adding inside shifts the input.",
                "Get both rules from a table before comparing — never read a crossing off the rows.",
                "Check the crossing by evaluating both functions there; they must agree.",
            ],
        },
    ]

    return lesson(
        slug="comparing-linear-functions",
        title="Comparing Two Linear Functions",
        concrete=(
            "Two removal firms quote for the same job. One asks $\\$60$ up front and $\\$8$ an "
            "hour; the other asks $\\$20$ up front and $\\$12$ an hour. Which is cheaper is "
            "not a fixed answer — it depends entirely on how long the job takes, and there is "
            "exactly one duration where it makes no difference at all."
        ),
        objective=(
            "Find where two linear functions are equal, decide which is greater on either side "
            "of that point, and handle functions defined in terms of another function."
        ),
        concept=[
            "**Skill card.** Still *Linear functions*, in the **Algebra** domain. Comparison "
            "items are common in the harder module and they reward structure over "
            "computation — the crossover, and which side of it you are on, is usually the "
            "whole question.",
            "Two linear functions are equal where their rules are equal, so set them equal and "
            "solve. That single input is the crossover. On one side of it one function is "
            "larger; on the other side the other one is. Which is which is decided by the "
            "rates: the function with the larger rate is behind before the crossover and "
            "ahead after it, however big the other one's head start.",
            "Functions defined from other functions come in two flavours and the SAT tests the "
            "contrast. $g(x) = f(x) + 7$ adds to the OUTPUT — the graph shifts up seven and "
            "the slope is untouched. $g(x) = f(x + 7)$ changes the INPUT before $f$ ever sees "
            "it — the graph shifts left seven, and for a line that lands on a different "
            "intercept. Outside the brackets acts on the output; inside acts on the input.",
            "**The test's angle.** When two functions arrive as a table, do NOT read the "
            "crossing off the rows. A table samples a handful of inputs and the crossing "
            "almost always falls between two of them. Extract both rules from the table — the "
            "rate from the steps, the constant from the $x = 0$ row — and then solve. Picking "
            "the nearest row is the error the item was written to catch.",
        ],
        key_idea=(
            "Set the rules equal to find where two linear functions cross. Before and after "
            "that point, the one with the larger rate is behind and then ahead — a head start "
            "is finite, a rate is not."
        ),
        facts=[
            fact(
                "The crossover",
                "m_1x + b_1 = m_2x + b_2 \\;\\Longrightarrow\\; x = \\frac{b_2 - b_1}{m_1 - m_2}",
                "One equation, one solution — unless the rates are equal, in which case the "
                "two functions never meet.",
            ),
            fact(
                "Vertical shift",
                "g(x) = f(x) + k \\;\\Longrightarrow\\; \\text{same slope, intercept } b + k",
                "Adding outside the brackets moves the whole graph up by $k$.",
            ),
            fact(
                "Horizontal shift",
                "g(x) = f(x + k) \\;\\Longrightarrow\\; \\text{same slope, intercept } b + mk",
                "Adding inside the brackets moves the graph LEFT by $k$. For a line that also "
                "changes the intercept, but by $mk$, not by $k$.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Reading the crossover off a table instead of solving for it.",
                "A table shows a few inputs; the crossing usually falls between two rows. "
                "Get both rules, then set them equal.",
            ),
            mistake(
                "Assuming the function that starts higher stays higher.",
                "A head start is a fixed amount. The function with the larger rate always "
                "overtakes it eventually.",
            ),
            mistake(
                "Treating $f(x) + 7$ and $f(x + 7)$ as the same thing.",
                "The first shifts the graph up by $7$; the second shifts it left by $7$. For "
                "$f(x) = 3x - 5$ they give intercepts $2$ and $16$ respectively.",
            ),
            mistake(
                "Answering with the equal VALUE when the question asked for the input.",
                "'After how many hours' wants the input; 'what is the cost' wants the output. "
                "Both numbers are on the option list.",
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
        "sat-l3-p01",
        "The function $f$ is defined by $f(x) = 8 - 3x$. What is $f(5)$?",
        "**Answer.** $-7$. $f(5) = 8 - 15 = -7$.",
        ["Eq(8 - 3*5, -7)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l3-p02",
        "The function $g$ is defined by $g(x) = 4x + 3$. For what value of $x$ is $g(x) = 23$?",
        "**Answer.** $5$. Set $4x + 3 = 23$, so $4x = 20$ and $x = 5$.",
        ["Eq(4*5 + 3, 23)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l3-p03",
        "If $f(x) = -2x + 9$, what is $f(-4)$?",
        "**Answer.** $17$. $f(-4) = -2(-4) + 9 = 8 + 9 = 17$. Losing the double negative "
        "gives $1$, a listed option.",
        ["Eq(-2*(-4) + 9, 17)", "Ne(-2*4 + 9, 17)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l3-p04",
        "The linear function $h$ satisfies $h(0) = 7$ and $h(4) = 19$. What is $h(9)$?",
        "**Answer.** $34$. The rate is $\\frac{19 - 7}{4} = 3$, so $h(x) = 3x + 7$ and "
        "$h(9) = 27 + 7 = 34$.",
        ["Eq(Rational(19 - 7, 4), 3)", "Eq(3*9 + 7, 34)", "Eq(3*4 + 7, 19)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p05",
        "If $f(x) = 5x - 2$, what is $f(x + 1) - f(x)$?",
        "**Answer.** $5$. $f(x + 1) = 5(x + 1) - 2 = 5x + 3$, so the difference is "
        "$(5x + 3) - (5x - 2) = 5$. For any linear function this difference is just the "
        "slope, independent of $x$ — which is the definition of linear.",
        ["Eq(expand((5*(x + 1) - 2) - (5*x - 2)), 5)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p06",
        "The graph of the linear function $f$ passes through $(0, -3)$ and $(6, 9)$. What is "
        "$f(2)$?",
        "**Answer.** $1$. The slope is $\\frac{9 - (-3)}{6} = 2$ and the intercept is $-3$, so "
        "$f(x) = 2x - 3$ and $f(2) = 1$.",
        ["Eq(Rational(9 - (-3), 6 - 0), 2)", "Eq(2*2 - 3, 1)", "Eq(2*6 - 3, 9)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p07",
        "The function $f$ is defined by $f(x) = mx + 4$ and $f(6) = 22$. What is the value of "
        "$m$?",
        "**Answer.** $3$. Substitute: $6m + 4 = 22$, so $6m = 18$ and $m = 3$.",
        ["Eq(3*6 + 4, 22)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l3-p08",
        "If $f(x) = 4x - 7$ and $g(x) = f(x) + 10$, what is the $y$-intercept of $g$?",
        "**Answer.** $3$. $g(x) = 4x - 7 + 10 = 4x + 3$, so the intercept is $3$. The slope "
        "is unchanged because adding outside the brackets only moves the graph up.",
        ["Eq(4*0 - 7 + 10, 3)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p09",
        "Two rental services are compared. Service A charges $C_A(d) = 30d + 45$ and Service "
        "B charges $C_B(d) = 45d$, where $d$ is the number of days. For how many days do they "
        "cost the same?",
        "**Answer.** $3$ days. Set $30d + 45 = 45d$, so $45 = 15d$ and $d = 3$. Both cost "
        "$\\$135$. Beyond three days B is dearer, because it climbs faster.",
        [
            "Eq(30*3 + 45, 45*3)",
            "Eq(45*3, 135)",
            "45*5 > 30*5 + 45",
            "45*2 < 30*2 + 45",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p10",
        "The table gives values of the linear function $f$.\n\n"
        "| $x$ | $f(x)$ |\n| --- | --- |\n| $-2$ | $13$ |\n| $1$ | $4$ |\n| $4$ | $-5$ |\n\n"
        "What is the value of $f(0)$?",
        "**Answer.** $7$. The rate is $\\frac{4 - 13}{1 - (-2)} = \\frac{-9}{3} = -3$. "
        "Substituting $(1, 4)$: $4 = -3 + b$, so $b = 7$ and $f(0) = 7$. The table has no "
        "$x = 0$ row, so this had to be computed.",
        [
            "Eq(Rational(4 - 13, 1 - (-2)), -3)",
            "Eq(-3*1 + 7, 4)",
            "Eq(-3*(-2) + 7, 13)",
            "Eq(-3*4 + 7, -5)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p11",
        "If $f(x) = 2x + 5$, what is $f(3a)$?",
        "**Answer.** $6a + 5$. Replace every $x$ with the whole input $3a$: "
        "$f(3a) = 2(3a) + 5 = 6a + 5$. Writing $2x + 5$ times $3a$, or $6a + 15$, are the two "
        "standard errors.",
        ["Eq(expand(2*(3*a) + 5), 6*a + 5)", "Ne(6*a + 15, 6*a + 5)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-p12",
        "The linear functions $f$ and $g$ satisfy $f(x) = 4x - 1$ and $g(x) = -2x + 17$. For "
        "what value of $x$ is $f(x) = g(x)$, and what is that common value?",
        "**Answer.** $x = 3$, and both equal $11$. Setting $4x - 1 = -2x + 17$ gives $6x = 18$ "
        "and $x = 3$; then $f(3) = 11$ and $g(3) = 11$ agree. Reporting $3$ when the question "
        "wanted $11$ — or the reverse — is the trap.",
        ["Eq(solve(Eq(4*x - 1, -2*x + 17), x)[0], 3)", "Eq(4*3 - 1, 11)", "Eq(-2*3 + 17, 11)"],
        badges=_b("Hard"),
    ),
]

TEST = [
    problem(
        "sat-l3-x01",
        "The function $f$ is defined by $f(x) = 9 - 2x$. What is $f(-1)$?",
        "**Answer.** $11$. $f(-1) = 9 - 2(-1) = 9 + 2 = 11$.",
        ["Eq(9 - 2*(-1), 11)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l3-x02",
        "The function $g$ is defined by $g(x) = 7x - 12$. If $g(c) = 30$, what is $c$?",
        "**Answer.** $6$. $7c = 42$, so $c = 6$. Check: $7(6) - 12 = 30$.",
        ["Eq(7*6 - 12, 30)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-l3-x03",
        "The linear function $f$ satisfies $f(3) = 1$ and $f(7) = 13$. What is $f(0)$?",
        "**Answer.** $-8$. The rate is $\\frac{13 - 1}{7 - 3} = 3$, and $1 = 3(3) + b$ gives "
        "$b = -8$. Stepping back from $f(3) = 1$ by three units of $x$ lowers the output by "
        "$9$, reaching $-8$ — same answer, no equation.",
        ["Eq(Rational(13 - 1, 7 - 3), 3)", "Eq(3*3 - 8, 1)", "Eq(3*7 - 8, 13)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-x04",
        "If $f(x) = 3x + 2$, what is $f(x - 4)$?",
        "**Answer.** $3x - 10$. Replace $x$ by the whole expression: "
        "$f(x - 4) = 3(x - 4) + 2 = 3x - 12 + 2 = 3x - 10$. Distributing over only the $x$ "
        "gives $3x - 4 + 2$, which is wrong by $8$.",
        ["Eq(expand(3*(x - 4) + 2), 3*x - 10)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-x05",
        "A pool is drained by function $V(t) = 900 - 45t$ litres after $t$ minutes. What does "
        "$V(0) - V(10)$ represent, and what is its value?",
        "**Answer.** The litres drained in the first ten minutes, which is $450$. "
        "$V(0) = 900$ and $V(10) = 450$, so the difference is $450$. Equivalently the rate "
        "times the elapsed time: $45 \\times 10 = 450$.",
        [
            "Eq(900 - 45*0, 900)",
            "Eq(900 - 45*10, 450)",
            "Eq((900 - 45*0) - (900 - 45*10), 450)",
            "Eq(45*10, 450)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-x06",
        "The graph of the linear function $f$ has $x$-intercept $(4, 0)$ and $y$-intercept "
        "$(0, -10)$. What is $f(6)$?",
        "**Answer.** $5$. The slope is $\\frac{0 - (-10)}{4 - 0} = \\frac{10}{4} = 2.5$, so "
        "$f(x) = 2.5x - 10$ and $f(6) = 15 - 10 = 5$.",
        [
            "Eq(Rational(0 - (-10), 4 - 0), Rational(5,2))",
            "Eq(Rational(5,2)*4 - 10, 0)",
            "Eq(Rational(5,2)*6 - 10, 5)",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-x07",
        "Machine P has produced $80$ parts and makes $12$ more per hour. Machine Q has "
        "produced $200$ parts and makes $4$ more per hour. After how many hours have they "
        "produced the same number of parts?",
        "**Answer.** $15$ hours. Set $12h + 80 = 4h + 200$, so $8h = 120$ and $h = 15$; both "
        "have made $260$ parts. Machine P starts behind but is three times faster, so it "
        "always catches up eventually.",
        [
            "Eq(12*15 + 80, 4*15 + 200)",
            "Eq(12*15 + 80, 260)",
            "12*20 + 80 > 4*20 + 200",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-l3-x08",
        "The function $f$ is linear and $f(x + 2) = f(x) + 6$ for every $x$. If $f(1) = 4$, "
        "what is $f(7)$?",
        "**Answer.** $22$. The given relation says every step of $2$ in the input raises the "
        "output by $6$, so the slope is $\\frac{6}{2} = 3$. Going from $x = 1$ to $x = 7$ is a "
        "run of $6$, which raises the output by $18$: $4 + 18 = 22$.  \n"
        "Written out, $f(x) = 3x + 1$, and $f(7) = 22$ confirms it.",
        [
            "Eq(Rational(6,2), 3)",
            "Eq(3*1 + 1, 4)",
            "Eq(3*7 + 1, 22)",
            "Eq(expand((3*(x + 2) + 1) - (3*x + 1)), 6)",
        ],
        badges=_b("Hard"),
    ),
]


def main():
    lessons = [lesson_notation(), lesson_graphs(), lesson_comparing()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Linear Functions",
        3,
        "Function notation and what it is really asking, linear functions read out of graphs "
        "and tables, and the comparison questions where two plans, machines or prices meet at "
        "exactly one crossover point.",
        "Slope and intercepts from Unit 2 — this is the same line wearing function notation.",
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
