#!/usr/bin/env python3
"""IB Mathematics: Applications & Interpretation SL — Unit 2 (Topic 2: Functions).

Builds data/genmath/ib-ai-sl/functions.json: six lessons, one per official
subtopic code AI SL 2.1-2.6, same anatomy as Unit 1 (syllabus cards, booklet
flags, M/A/R markscheme + narrative solutions, interactive widgets, sympy
check[] everywhere). Banks tagged ib-ai-sl-2.x.

Functions carry ~26% of the AI SL assessment — the largest single topic, and
the one whose final two codes (2.5 modelling with named families, 2.6 the
modelling process itself) have no counterpart in Analysis & Approaches. AA
asks you to manipulate a function; AI asks you to CHOOSE one, fit it, and say
where it stops being true.

Run: python3 scripts/ib/build_ai_sl_unit2.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-ai-sl", "functions.json")


# ===========================================================================
# Lesson 1 — AI SL 2.1: straight lines
# ===========================================================================
def lesson_straight_lines():
    return {
        "slug": "straight-lines",
        "title": "Straight Lines and Their Gradients",
        "concreteComparison": (
            "A taxi meter is a straight line: a flat drop charge, then a fixed amount per "
            "kilometre. The drop charge is the $y$-intercept and the per-kilometre rate is the "
            "gradient — which is why a receipt for two different trips is enough to reconstruct "
            "the whole fare structure."
        ),
        "objective": (
            "Move between the three forms of a line, find a gradient from two points, and use "
            "the parallel and perpendicular conditions to build new lines."
        ),
        "concept": [
            "**Syllabus card — AI SL 2.1.** Different forms of the equation of a straight line; "
            "gradient and intercepts; parallel lines $m_1 = m_2$; perpendicular lines "
            "$m_1 m_2 = -1$. **Papers 1 and 2.** All three forms are in the formula booklet, so "
            "the marks are for choosing the right one and using it cleanly.",
            "Three forms, three jobs. $y = mx + c$ reads off the gradient and $y$-intercept at a "
            "glance. $ax + by + d = 0$ is the tidy form an exam answer is often demanded in — "
            "and the one where you must NOT read the gradient as $a/b$ without rearranging. "
            "$y - y_1 = m(x - x_1)$ is the one to reach for the moment you have a point and a "
            "gradient, which is most of the time.",
            "Gradient from two points: $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$. Whichever point you "
            "call 'first', use the SAME order top and bottom. Reversing one but not the other "
            "flips the sign, and a sign-flipped gradient is the single most common lost mark on "
            "this code.",
            "Parallel means equal gradients. Perpendicular means the product is $-1$, i.e. the "
            "negative reciprocal: flip it AND change its sign. A gradient of $\\frac{3}{4}$ has "
            "perpendicular partner $-\\frac{4}{3}$ — two changes, not one. A horizontal line "
            "($m = 0$) is perpendicular to a vertical line, which has no gradient at all; that "
            "pair is the one exception the product rule cannot express."
        ],
        "keyIdea": (
            "A gradient is a rate: how much $y$ changes per unit of $x$. Everything on this "
            "code — parallel, perpendicular, intercepts, contexts — is that one number read in "
            "a different light."
        ),
        "facts": [
            {
                "title": "The three forms",
                "latex": "y = mx + c \\quad|\\quad ax + by + d = 0 \\quad|\\quad y - y_1 = m(x - x_1)",
                "explanation": "All three are in the formula booklet (AI SL 2.1).",
            },
            {
                "title": "Gradient from two points",
                "latex": "m = \\frac{y_2 - y_1}{x_2 - x_1}",
                "explanation": "Booklet. Keep the point order the same in numerator and denominator.",
            },
            {
                "title": "Parallel and perpendicular",
                "latex": "m_1 = m_2 \\quad\\text{(parallel)} \\qquad m_1 m_2 = -1 \\quad\\text{(perpendicular)}",
                "explanation": "Booklet. The perpendicular condition is the negative RECIPROCAL.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-21-we1",
                "statement": (
                    "The points $A(-2, 7)$ and $B(4, -5)$ lie on a line $L$.  \n"
                    "**(a)** Find the gradient of $L$. **[2]**  \n"
                    "**(b)** Find the equation of $L$ in the form $ax + by + d = 0$. **[3]**  \n"
                    "**(c)** Find the equation of the line perpendicular to $L$ through $B$. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** $m = \\dfrac{-5 - 7}{4 - (-2)} = \\dfrac{-12}{6}$ *(M1)* $= -2$ "
                    "*(A1)*.  \n"
                    "**(b)** Using $A$: $y - 7 = -2(x + 2)$ *(M1)*, so $y = -2x + 3$ *(A1)*, "
                    "i.e. $2x + y - 3 = 0$ *(A1)*.  \n"
                    "**(c)** Perpendicular gradient $= \\dfrac{1}{2}$ *(A1)*. Through "
                    "$B(4, -5)$: $y + 5 = \\dfrac{1}{2}(x - 4)$ *(M1)*, so "
                    "$y = \\dfrac{1}{2}x - 7$ *(A1)*.  \n"
                    "**Narrative:** in (b) either point works — using $B$ gives "
                    "$y + 5 = -2(x - 4)$, the same line. Checking with the point you did NOT "
                    "use is the free verification: $-2(4) + 3 = -5$ ✓. In (c) the perpendicular "
                    "gradient is the negative reciprocal of $-2$, and the negative of a negative "
                    "is positive — students who write $-\\frac{1}{2}$ have changed the sign twice."
                ),
                "check": [
                    "Rational(-5 - 7, 4 - (-2)) == -2",
                    "-2*(-2) + 3 == 7",
                    "-2*4 + 3 == -5",
                    "-2*Rational(1, 2) == -1",
                    "Rational(1, 2)*4 - 7 == -5",
                ],
            },
            {
                "id": "aisl-21-we2",
                "statement": (
                    "A taxi company charges a fixed pick-up fee plus a fixed amount per "
                    "kilometre. A $5$ km trip costs $\\$8.50$ and a $12$ km trip costs "
                    "$\\$15.50$.  \n"
                    "**(a)** Find the cost per kilometre. **[2]**  \n"
                    "**(b)** Write a model for the cost $C$ of a $d$ km trip. **[2]**  \n"
                    "**(c)** Find the cost of a $20$ km trip. **[2]**"
                ),
                "solution": (
                    "**(a)** The rate is the gradient: "
                    "$m = \\dfrac{15.50 - 8.50}{12 - 5} = \\dfrac{7}{7}$ *(M1)* $= \\$1.00$ per "
                    "km *(A1)*.  \n"
                    "**(b)** $8.50 = 1.00(5) + c$ *(M1)*, so $c = 3.50$ and "
                    "$C = d + 3.50$ *(A1)*.  \n"
                    "**(c)** $C = 20 + 3.50 = \\$23.50$ *(M1 A1)*.  \n"
                    "**Narrative:** the two receipts are two points, $(5, 8.50)$ and "
                    "$(12, 15.50)$ — once you see them that way the question is (a) of the "
                    "previous example wearing a coat. The intercept $\\$3.50$ is the pick-up "
                    "fee: the cost of a trip of zero length, which is exactly what a $y$-intercept "
                    "means here. Interpreting BOTH numbers in context is usually worth a mark on "
                    "its own in Paper 2."
                ),
                "check": [
                    "Rational(155, 10) - Rational(85, 10) == 7",
                    "Rational(7, 7) == 1",
                    "Rational(85, 10) - 5 == Rational(35, 10)",
                    "20 + Rational(35, 10) == Rational(235, 10)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reading the gradient of $3x + 4y = 24$ as $3$ or as $\\frac{3}{4}$.",
                "correction": "Rearrange first: $y = -\\frac{3}{4}x + 6$, so $m = -\\frac{3}{4}$. The sign comes from moving the $x$ term across.",
                "authored": True,
            },
            {
                "text": "Writing the perpendicular gradient of $\\frac{2}{5}$ as $-\\frac{2}{5}$.",
                "correction": "Two changes, not one: flip to $\\frac{5}{2}$ AND negate, giving $-\\frac{5}{2}$. Check with the product: $\\frac{2}{5} \\times -\\frac{5}{2} = -1$.",
                "authored": True,
            },
            {
                "text": "Computing $m = \\dfrac{y_1 - y_2}{x_2 - x_1}$.",
                "correction": "Mixed order flips the sign. Fix one point as 'first' and use it in both the numerator and the denominator.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-21-t1",
                "statement": (
                    "For the line $3x + 4y = 24$, find the gradient and both axis intercepts. "
                    "**[3]**"
                ),
                "solution": (
                    "Rearranging: $4y = -3x + 24$, so $y = -\\dfrac{3}{4}x + 6$ *(M1)*, giving "
                    "$m = -\\dfrac{3}{4}$ *(A1)*.  \n"
                    "$y$-intercept $(0, 6)$; setting $y = 0$ gives $x = 8$, so $(8, 0)$ *(A1)*."
                ),
                "check": [
                    "Rational(-3, 4)*0 + 6 == 6",
                    "Rational(-3, 4)*8 + 6 == 0",
                ],
            },
            {
                "id": "aisl-21-t2",
                "statement": (
                    "Line $L$ is perpendicular to $y = 3x - 1$ and passes through $(6, 2)$. "
                    "Find its equation. **[3]**"
                ),
                "solution": (
                    "Perpendicular gradient $= -\\dfrac{1}{3}$ *(A1)*. Then "
                    "$y - 2 = -\\dfrac{1}{3}(x - 6)$ *(M1)*, so $y = -\\dfrac{1}{3}x + 4$ "
                    "*(A1)*."
                ),
                "check": [
                    "3*Rational(-1, 3) == -1",
                    "Rational(-1, 3)*6 + 4 == 2",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 2.1 · Papers 1 & 2",
                    "title": "A gradient is a rate wearing a hat",
                    "body": (
                        "Cost per kilometre, degrees per minute, dollars per hour — every "
                        "'per' in a context is a gradient, and every straight-line question on "
                        "this course is either finding one, using one, or building a second "
                        "line from it."
                    ),
                },
                {
                    "kind": "systemGraph",
                    "eyebrow": "Feel it",
                    "title": "Perpendicular, seen",
                    "teach": (
                        "The fixed line is $y = x + 2$; the blue one starts at $y = -x + 5$, "
                        "its perpendicular partner. Step the blue slope and watch the right "
                        "angle appear only at $m_2 = -1$ — because perpendicularity depends on "
                        "the gradients alone, never on where the lines sit."
                    ),
                    "config": {"m1": 1, "b1": 2, "m2": -1, "b2": 5, "interactive": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Point plus gradient, every time",
                    "beats": [
                        "Two points? Gradient first, same order top and bottom.",
                        "Gradient plus a point? Use $y - y_1 = m(x - x_1)$ — no simultaneous equations needed.",
                        "Asked for $ax + by + d = 0$? Clear fractions, then move everything to one side.",
                        "Check with the point you did not use.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two points, one line, one perpendicular",
                    "problemId": "aisl-21-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Negative reciprocal",
                    "title": "Flip and negate",
                    "prompt": "A line perpendicular to $y = -\\frac{2}{5}x + 1$ has gradient",
                    "options": [
                        "$\\frac{5}{2}$",
                        "$-\\frac{5}{2}$",
                        "$\\frac{2}{5}$",
                        "$-\\frac{2}{5}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Flip $-\\frac{2}{5}$ to $-\\frac{5}{2}$, then negate: $\\frac{5}{2}$. "
                        "Confirm with the product: $-\\frac{2}{5} \\times \\frac{5}{2} = -1$."
                    ),
                    "check": [
                        "Rational(-2, 5)*Rational(5, 2) == -1",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two receipts, one fare model",
                    "problemId": "aisl-21-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the context",
                    "title": "What the intercept means",
                    "prompt": (
                        "A gym's monthly cost is $C = 4v + 25$ dollars for $v$ visits. The $25$ is"
                    ),
                    "options": [
                        "the fixed monthly membership fee",
                        "the cost of one visit",
                        "the number of visits included free",
                        "the cost of 25 visits",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "At $v = 0$ the cost is $\\$25$ — what you pay for making no visits at "
                        "all. The $4$ is the per-visit rate."
                    ),
                    "check": [
                        "4*0 + 25 == 25",
                        "4*1 + 25 == 29",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "'In the form $ax + by + d = 0$' is an instruction",
                    "body": (
                        "If the question names a form, the final A-mark is for that form. "
                        "$y = -2x + 3$ is a correct line and an incomplete answer. Clear any "
                        "fractions first — $y = \\frac{1}{2}x - 7$ becomes $x - 2y - 14 = 0$."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-21-t1"},
                {"kind": "tryIt", "problemId": "aisl-21-t2"},
                {
                    "kind": "recap",
                    "title": "Lines, compressed",
                    "points": [
                        "$m = \\frac{y_2 - y_1}{x_2 - x_1}$ — same order top and bottom.",
                        "Point plus gradient goes straight into $y - y_1 = m(x - x_1)$.",
                        "Parallel: equal gradients. Perpendicular: flip AND negate.",
                        "In context the gradient is a rate and the intercept is the value at zero.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — AI SL 2.2: functions, domain, range, inverse
# ===========================================================================
def lesson_functions_domain_range():
    return {
        "slug": "functions-domain-and-range",
        "title": "Functions, Domain, Range and Inverses",
        "concreteComparison": (
            "A vending machine is a function: each button gives exactly one product. The set of "
            "buttons is the domain, the set of products that can actually come out is the range, "
            "and the inverse is the question 'which button produced this can?' — answerable only "
            "if no two buttons give the same thing."
        ),
        "objective": (
            "Use function notation, state a domain and a range from a context or a graph, and "
            "find and interpret an inverse function."
        ),
        "concept": [
            "**Syllabus card — AI SL 2.2.** Concept of a function; domain, range and graph; "
            "function notation; the function as a mathematical model; the informal concept of "
            "an inverse as the function that undoes $f$, its notation $f^{-1}(x)$, and its graph "
            "as the reflection of $y = f(x)$ in $y = x$. **Papers 1 and 2.**",
            "$f(x)$ is an instruction, not a multiplication. $f(4)$ means 'run the rule on the "
            "input $4$'. In a modelling context give the letters meaning: $C(n)$ for cost as a "
            "function of the number of people says more than $y$ ever will, and examiners reward "
            "notation that carries its own meaning.",
            "DOMAIN is the set of allowed inputs; RANGE is the set of outputs that actually "
            "occur. In pure questions the domain is whatever the algebra permits — no dividing "
            "by zero, no square roots of negatives. In modelling questions the CONTEXT sets it: "
            "a number of people is a whole number and cannot be negative, and a time since "
            "opening starts at zero. Saying so is a mark.",
            "An inverse undoes the function, so $f^{-1}(b) = a$ exactly when $f(a) = b$. To find "
            "it: write $y = f(x)$, swap the roles of $x$ and $y$, and make $y$ the subject. Its "
            "graph is $y = f(x)$ reflected in the line $y = x$, so domain and range swap places "
            "too."
        ],
        "keyIdea": (
            "A function is a machine with a specified set of legal inputs. Domain in, range out, "
            "and the inverse runs the machine backwards."
        ),
        "facts": [
            {
                "title": "Function notation",
                "latex": "f: x \\mapsto 3x - 5 \\quad\\Longleftrightarrow\\quad f(x) = 3x - 5",
                "explanation": "Two notations for the same rule. Both appear in AI papers.",
            },
            {
                "title": "The inverse undoes the function",
                "latex": "f^{-1}(b) = a \\iff f(a) = b",
                "explanation": "NOT in the booklet as a formula — it is the definition, and it is all you need.",
            },
            {
                "title": "The inverse is a reflection",
                "latex": "y = f^{-1}(x) \\text{ is } y = f(x) \\text{ reflected in } y = x",
                "explanation": "Domain and range swap. A sketch question often wants exactly this.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-22-we1",
                "statement": (
                    "The function $f$ is defined by $f(x) = 3x - 5$ for $0 \\le x \\le 6$.  \n"
                    "**(a)** Find $f(4)$. **[1]**  \n"
                    "**(b)** State the range of $f$. **[2]**  \n"
                    "**(c)** Find $f^{-1}(x)$, and hence find $f^{-1}(7)$. **[3]**"
                ),
                "solution": (
                    "**(a)** $f(4) = 3(4) - 5 = 7$ *(A1)*.  \n"
                    "**(b)** $f$ is increasing, so the ends of the domain give the ends of the "
                    "range: $f(0) = -5$ and $f(6) = 13$ *(M1)*, so "
                    "$-5 \\le f(x) \\le 13$ *(A1)*.  \n"
                    "**(c)** Let $y = 3x - 5$; then $x = \\dfrac{y + 5}{3}$ *(M1)*, so "
                    "$f^{-1}(x) = \\dfrac{x + 5}{3}$ *(A1)*. Hence "
                    "$f^{-1}(7) = \\dfrac{12}{3} = 4$ *(A1)*.  \n"
                    "**Narrative:** the 'hence' in (c) is real — part (a) already said "
                    "$f(4) = 7$, so $f^{-1}(7)$ had to be $4$, and that is the cheapest possible "
                    "check on your inverse. Note that (b) works only because $f$ is increasing; "
                    "for a parabola the endpoints are NOT the extremes, which is the trap in the "
                    "first tryIt below."
                ),
                "check": [
                    "3*4 - 5 == 7",
                    "3*0 - 5 == -5",
                    "3*6 - 5 == 13",
                    "Rational(7 + 5, 3) == 4",
                ],
            },
            {
                "id": "aisl-22-we2",
                "statement": (
                    "A hall costs $\\$250$ to hire plus $\\$12$ for each guest. The cost in "
                    "dollars for $n$ guests is $C(n) = 250 + 12n$, where $0 \\le n \\le 200$.  \n"
                    "**(a)** Find $C(80)$. **[2]**  \n"
                    "**(b)** Interpret the numbers $250$ and $12$ in context. **[2]**  \n"
                    "**(c)** A group has a budget of $\\$1930$. Find the greatest number of "
                    "guests it can invite. **[3]**"
                ),
                "solution": (
                    "**(a)** $C(80) = 250 + 12(80)$ *(M1)* $= \\$1210$ *(A1)*.  \n"
                    "**(b)** $\\$250$ is the fixed hire charge, paid even with no guests "
                    "*(A1)*; $\\$12$ is the cost per additional guest *(A1)*.  \n"
                    "**(c)** $250 + 12n \\le 1930$ *(M1)*, so $12n \\le 1680$ and "
                    "$n \\le 140$ *(A1)*. The greatest number of guests is $140$ *(A1)*.  \n"
                    "**Narrative:** the domain matters here. $n$ counts people, so it is a whole "
                    "number — had the budget been $\\$1900$ the algebra would give "
                    "$n \\le 137.5$ and the answer would be $137$, not $137.5$ and not $138$. "
                    "Rounding a modelling answer in the direction the CONTEXT demands, rather "
                    "than the direction arithmetic habit demands, is a standing AI theme."
                ),
                "check": [
                    "250 + 12*80 == 1210",
                    "250 + 12*140 == 1930",
                    "250 + 12*141 > 1930",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reading $f(x)$ as $f$ multiplied by $x$.",
                "correction": "It is an instruction: $f(3)$ means substitute $3$ into the rule. There is no multiplication anywhere in the notation.",
                "authored": True,
            },
            {
                "text": "Taking the range from the endpoints of the domain for any function.",
                "correction": "That only works when the function is increasing or decreasing throughout. Check for a turning point inside the domain first.",
                "authored": True,
            },
            {
                "text": "Writing $f^{-1}(x) = \\dfrac{1}{f(x)}$.",
                "correction": "The $-1$ is not an exponent here. $f^{-1}$ reverses $f$; $\\frac{1}{f(x)}$ is an entirely different function.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-22-t1",
                "statement": (
                    "$g(x) = x^{2} - 4$ for $-3 \\le x \\le 3$. Find the range of $g$. **[3]**"
                ),
                "solution": (
                    "The graph is a parabola with its minimum at $x = 0$ *(M1)*, giving "
                    "$g(0) = -4$ *(A1)*. The largest value is at the ends: "
                    "$g(3) = g(-3) = 5$. So $-4 \\le g(x) \\le 5$ *(A1)*.  \n"
                    "The endpoints alone would have given $5 \\le g(x) \\le 5$ — nonsense, and "
                    "the signal that a turning point sits inside the domain."
                ),
                "check": [
                    "0**2 - 4 == -4",
                    "3**2 - 4 == 5",
                    "(-3)**2 - 4 == 5",
                ],
            },
            {
                "id": "aisl-22-t2",
                "statement": (
                    "$h(x) = 4 - 2x$. Find $h^{-1}(x)$ and evaluate $h^{-1}(10)$. **[3]**"
                ),
                "solution": (
                    "Let $y = 4 - 2x$, so $2x = 4 - y$ and $x = \\dfrac{4 - y}{2}$ *(M1)*. "
                    "Hence $h^{-1}(x) = \\dfrac{4 - x}{2}$ *(A1)*, and "
                    "$h^{-1}(10) = \\dfrac{-6}{2} = -3$ *(A1)*.  \n"
                    "Check: $h(-3) = 4 + 6 = 10$ ✓."
                ),
                "check": [
                    "Rational(4 - 10, 2) == -3",
                    "4 - 2*(-3) == 10",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 2.2 · Papers 1 & 2",
                    "title": "One input, one output",
                    "body": (
                        "That is the whole definition. Everything else on this code — domain, "
                        "range, inverse — is about being precise regarding WHICH inputs are "
                        "allowed and WHICH outputs actually appear."
                    ),
                },
                {
                    "kind": "evaluator",
                    "eyebrow": "Play",
                    "title": "Feed the machine",
                    "teach": (
                        "This is $f(x) = 3x - 5$ from the worked example, on its stated domain "
                        "$0 \\le x \\le 6$. Slide the input and watch the output sweep from "
                        "$-5$ to $13$ — that swept interval IS the range."
                    ),
                    "config": {"a": 3, "b": -5, "varName": "x", "min": 0, "max": 6, "start": 4},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Finding a range without guessing",
                    "beats": [
                        "Sketch it on the GDC over the stated domain — nothing else is as fast.",
                        "Increasing or decreasing throughout? The endpoints give the range.",
                        "Turning point inside the domain? Include its $y$-value as the max or min.",
                        "Write the answer as an inequality in $f(x)$, not in $x$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Domain, range and an inverse",
                    "problemId": "aisl-22-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Run it backwards",
                    "title": "Which input gave 9?",
                    "prompt": "If $f(x) = 2x + 1$, then $f^{-1}(9)$ equals",
                    "options": ["$4$", "$19$", "$\\frac{1}{19}$", "$5$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$f^{-1}(9)$ asks which input gives $9$: solve $2x + 1 = 9$ to get "
                        "$x = 4$. Choosing $19$ is computing $f(9)$ — running the machine the "
                        "wrong way."
                    ),
                    "check": [
                        "2*4 + 1 == 9",
                        "2*9 + 1 == 19",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A cost function with a real domain",
                    "problemId": "aisl-22-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Context sets the domain",
                    "title": "What can $n$ be?",
                    "prompt": (
                        "$T(n)$ is the total mass of $n$ identical crates. A sensible domain is"
                    ),
                    "options": [
                        "the whole numbers $0, 1, 2, \\ldots$ up to the truck's limit",
                        "all real numbers",
                        "all real numbers greater than zero",
                        "the integers, positive and negative",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "You cannot load $2.4$ crates or $-3$ crates, and the truck caps the "
                        "top end. Naming that restriction is what earns the mark — the formula "
                        "alone does not."
                    ),
                    "check": [
                        "0 >= 0",
                        "Rational(24, 10) != floor(Rational(24, 10))",
                    ],
                },
                {
                    "kind": "funFact",
                    "eyebrow": "Why $y = x$?",
                    "title": "The mirror is the do-nothing function",
                    "body": (
                        "Reflecting in $y = x$ swaps every point $(a, b)$ with $(b, a)$ — which "
                        "is exactly what an inverse does to inputs and outputs. So the mirror "
                        "line is not a convention someone chose; it is the picture of the "
                        "definition."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-22-t1"},
                {"kind": "tryIt", "problemId": "aisl-22-t2"},
                {
                    "kind": "recap",
                    "title": "Functions, compressed",
                    "points": [
                        "$f(x)$ is an instruction; $f(4)$ means substitute.",
                        "Domain in, range out — and in modelling the context sets the domain.",
                        "Endpoints give the range only if there is no turning point inside.",
                        "$f^{-1}$ undoes $f$: swap and rearrange, and check with a known pair.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — AI SL 2.3: graphs and sketching with technology
# ===========================================================================
def lesson_graphs_and_sketching():
    return {
        "slug": "graphs-and-sketching",
        "title": "Graphs, Windows and Sketching from a Screen",
        "concreteComparison": (
            "A graph on a calculator screen is a photograph taken through a window. Point the "
            "camera at the wrong part of the plane and a perfectly good function looks like an "
            "empty grid, or like a straight line. Choosing the window IS half the question."
        ),
        "objective": (
            "Graph a function with technology, choose a window that shows its important "
            "behaviour, and transfer the graph to paper as a labelled sketch."
        ),
        "concept": [
            "**Syllabus card — AI SL 2.3.** The graph of a function and its equation "
            "$y = f(x)$; creating a sketch from given information or a context, including "
            "transferring a graph from screen to paper; using technology to graph functions "
            "including their sums and differences. **Papers 1 and 2.**",
            "A SKETCH is not a drawing. It needs the right overall shape, the axis intercepts, "
            "any asymptotes, any turning points, and labels — and nothing else. Marks come from "
            "the labelled features, so an accurate-looking curve with no numbers on it scores "
            "almost nothing while a rough curve with its intercepts marked scores almost "
            "everything.",
            "The window is a decision. Set $x$ from the domain the question gives you, then let "
            "the GDC fit $y$ — or set $y$ yourself if you already know roughly how big the "
            "outputs are. A blank screen almost always means the $y$-range is far too small, not "
            "that the function has no graph.",
            "Sums and differences graph directly: enter $Y_3 = Y_1 + Y_2$ rather than expanding "
            "by hand. It is faster, it cannot go wrong algebraically, and it lets you SEE where "
            "the combined function crosses zero — which is what a 'find when total cost equals "
            "total revenue' question is really asking."
        ],
        "keyIdea": (
            "Graph it, then label it. The sketch earns its marks from intercepts, asymptotes and "
            "turning points, and the window is what makes those visible in the first place."
        ),
        "facts": [
            {
                "title": "What a sketch must carry",
                "latex": "\\text{shape} \\;+\\; \\text{intercepts} \\;+\\; \\text{asymptotes} \\;+\\; \\text{turning points}",
                "explanation": "Not in the booklet — it is the marking convention. Label every one you find.",
            },
            {
                "title": "Sums of functions",
                "latex": "(f + g)(x) = f(x) + g(x)",
                "explanation": "Enter both, then add them on the GDC. Zeros of $f + g$ are where the two graphs are opposite.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-23-we1",
                "statement": (
                    "Consider $f(x) = x^{3} - 6x^{2} + 9x$ for $0 \\le x \\le 4$.  \n"
                    "**(a)** Write down the $x$-intercepts. **[2]**  \n"
                    "**(b)** Find the coordinates of the local maximum. **[2]**  \n"
                    "**(c)** Sketch the graph for the given domain, labelling the intercepts and "
                    "the local maximum. **[3]**"
                ),
                "solution": (
                    "**(a)** Factorising, $f(x) = x(x - 3)^{2}$ *(M1)*, so the intercepts are "
                    "$x = 0$ and $x = 3$ *(A1)*.  \n"
                    "**(b)** From the GDC the local maximum is at $(1, 4)$ *(M1 A1)*.  \n"
                    "**(c)** A curve from the origin, rising to $(1, 4)$, falling to touch the "
                    "axis at $(3, 0)$ and rising again to $(4, 4)$ *(A3)*.  \n"
                    "**Narrative:** the repeated factor $(x-3)^2$ is why the curve TOUCHES the "
                    "axis at $x = 3$ instead of crossing it — a feature worth a mark on its own "
                    "in a sketch question. Note that $f(4) = 4$ as well as $f(1) = 4$: the "
                    "domain endpoint reaches the same height as the local maximum, so the "
                    "GLOBAL maximum on $0 \\le x \\le 4$ is attained twice."
                ),
                "check": [
                    "expand(x*(x - 3)**2) == x**3 - 6*x**2 + 9*x",
                    "1 - 6 + 9 == 4",
                    "27 - 54 + 27 == 0",
                    "64 - 96 + 36 == 4",
                    "diff(x**3 - 6*x**2 + 9*x, x) == 3*x**2 - 12*x + 9",
                ],
            },
            {
                "id": "aisl-23-we2",
                "statement": (
                    "A workshop's daily profit, in dollars, from selling $x$ items is modelled "
                    "by $P(x) = 60x - 0.5x^{2} - 1000$ for $0 \\le x \\le 110$.  \n"
                    "**(a)** Write down a suitable window for graphing $P$. **[2]**  \n"
                    "**(b)** Find the break-even points. **[3]**  \n"
                    "**(c)** Find the maximum profit and the number of items that achieves it. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** $0 \\le x \\le 110$ from the domain, and $-1200 \\le y \\le 900$ "
                    "*(A1 A1)* — the $y$-range must reach below $P(0) = -1000$ and above the "
                    "maximum.  \n"
                    "**(b)** Solving $P(x) = 0$ on the GDC *(M1)*: $x = 20$ and $x = 100$ "
                    "*(A1 A1)*.  \n"
                    "**(c)** The vertex is midway between the roots, at $x = 60$ *(M1)*, and "
                    "$P(60) = 3600 - 1800 - 1000 = \\$800$ *(A1 A1)*.  \n"
                    "**Narrative:** part (a) is a real mark on AI papers, and the reason is "
                    "part (b): with the default $-10 \\le y \\le 10$ window this parabola is "
                    "entirely off-screen and the roots are unfindable. Also note the shape of "
                    "the answer to (c) — making MORE than $60$ items lowers profit, which is the "
                    "kind of conclusion a modelling question actually wants stated in words."
                ),
                "check": [
                    "60*20 - Rational(1, 2)*20**2 - 1000 == 0",
                    "60*100 - Rational(1, 2)*100**2 - 1000 == 0",
                    "60*60 - Rational(1, 2)*60**2 - 1000 == 800",
                    "Rational(20 + 100, 2) == 60",
                    "60*0 - Rational(1, 2)*0**2 - 1000 == -1000",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Submitting a sketch with a beautiful curve and no numbers on it.",
                "correction": "Marks live on the labels: intercepts, asymptotes, turning points, and the axis names. Label first, prettify never.",
                "authored": True,
            },
            {
                "text": "Concluding a function has no graph because the screen is blank.",
                "correction": "The window is wrong, not the function. Widen the $y$-range — or use the GDC's zoom-fit — before touching anything else.",
                "authored": True,
            },
            {
                "text": "Sketching outside the stated domain.",
                "correction": "If the question says $0 \\le x \\le 4$, the curve starts and stops there. Extra arms are wrong, not generous.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-23-t1",
                "statement": (
                    "Sketch $y = 2^{x} - 5$ for $-2 \\le x \\le 4$. Write down the "
                    "$y$-intercept, the $x$-intercept to 3 s.f., and the equation of the "
                    "horizontal asymptote. **[4]**"
                ),
                "solution": (
                    "$y$-intercept: $2^{0} - 5 = -4$, so $(0, -4)$ *(A1)*.  \n"
                    "$x$-intercept: $2^{x} = 5$ gives $x = 2.32$ *(M1 A1)*.  \n"
                    "As $x \\to -\\infty$, $2^{x} \\to 0$, so the asymptote is $y = -5$ *(A1)*."
                ),
                "check": [
                    "2**0 - 5 == -4",
                    "Abs(log(5, 2) - Rational(232, 100)) < Rational(5, 1000)",
                    "Eq(limit(2**x - 5, x, -oo), -5)",
                ],
            },
            {
                "id": "aisl-23-t2",
                "statement": (
                    "Use technology to graph $y = x^{3} - 3x - 1$ for $-3 \\le x \\le 3$. Write "
                    "down the number of $x$-intercepts and the coordinates of the local maximum. "
                    "**[3]**"
                ),
                "solution": (
                    "The local maximum is at $(-1, 1)$ and the local minimum at $(1, -3)$ "
                    "*(M1 A1)*.  \n"
                    "Since the maximum is above the axis and the minimum below it, the curve "
                    "crosses three times: three $x$-intercepts *(A1)*."
                ),
                "check": [
                    "diff(x**3 - 3*x - 1, x) == 3*x**2 - 3",
                    "(-1)**3 - 3*(-1) - 1 == 1",
                    "1 - 3 - 1 == -3",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 2.3 · Papers 1 & 2",
                    "title": "The screen is a window, not the graph",
                    "body": (
                        "Every AI paper assumes you will graph things. The assessed skills are "
                        "the two on either side of the button press: choosing what to look at, "
                        "and turning what you see into a labelled sketch on paper."
                    ),
                },
                {
                    "kind": "polyGraph",
                    "eyebrow": "See it",
                    "title": "Where a cubic meets the axis",
                    "teach": (
                        "Move the third zero and watch the curve. When two zeros collide the "
                        "curve stops crossing and starts TOUCHING — that is the repeated factor "
                        "from the worked example, seen from the outside."
                    ),
                    "config": {"mode": "zeros", "zeros": [-2, 1, 3]},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "From screen to paper",
                    "beats": [
                        "Set the $x$-window from the stated domain, then fit $y$.",
                        "Harvest features: intercepts, turning points, asymptotes.",
                        "Draw the shape freehand — smooth, correct direction, correct ends.",
                        "Label every harvested feature with its coordinates, and name the axes.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A cubic that touches the axis",
                    "problemId": "aisl-23-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Fix the window",
                    "title": "Nothing on the screen",
                    "prompt": (
                        "Graphing $y = 400 - 2x^{2}$ in the default window shows an empty grid. "
                        "The best fix is to"
                    ),
                    "options": [
                        "widen the $y$-range so it includes values near $400$",
                        "switch the calculator from degrees to radians",
                        "widen the $x$-range and leave $y$ alone",
                        "restrict the domain to $x \\ge 0$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "At $x = 0$ the curve is at $y = 400$, far above a default window that "
                        "stops at $10$. The graph was never missing — it was above the frame."
                    ),
                    "check": [
                        "400 - 2*0**2 == 400",
                        "400 > 10",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A profit model, break-even to peak",
                    "problemId": "aisl-23-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Sums of functions",
                    "title": "Where does the total vanish?",
                    "prompt": (
                        "$f(x) = x - 6$ and $g(x) = 2^{x}$. The graph of $y = f(x) + g(x)$ "
                        "crosses the $x$-axis where"
                    ),
                    "options": [
                        "$2^{x} = 6 - x$",
                        "$2^{x} = x - 6$",
                        "$2^{x} = 0$",
                        "$x = 6$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$f + g = 0$ means $x - 6 + 2^{x} = 0$, i.e. $2^{x} = 6 - x$. On the "
                        "GDC that is the crossing of $y = 2^{x}$ and $y = 6 - x$ — and here "
                        "it lands exactly on $x = 2$, since $2^{2} = 4 = 6 - 2$."
                    ),
                    "check": [
                        "2**2 == 6 - 2",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Write the window down",
                    "body": (
                        "When a question says 'sketch', writing the window you used costs one "
                        "line and often earns a method mark — and it tells the examiner your "
                        "curve is a report of something real rather than a guess at a shape."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-23-t1"},
                {"kind": "tryIt", "problemId": "aisl-23-t2"},
                {
                    "kind": "recap",
                    "title": "Sketching, compressed",
                    "points": [
                        "Window from the domain; if the screen is blank, the $y$-range is wrong.",
                        "Harvest intercepts, turning points and asymptotes before drawing.",
                        "A sketch is graded on its labels, not its beauty.",
                        "Enter sums as $Y_1 + Y_2$ and read their zeros straight off the screen.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — AI SL 2.4: key features and intersections
# ===========================================================================
def lesson_key_features():
    return {
        "slug": "key-features-and-intersections",
        "title": "Key Features and Points of Intersection",
        "concreteComparison": (
            "Two mobile-phone plans, one with a high monthly fee and cheap calls, the other the "
            "reverse. The question everyone actually asks — 'at how many minutes do they cost "
            "the same?' — is a point of intersection, and on this course you find it by graphing "
            "both and letting the calculator meet them."
        ),
        "objective": (
            "Identify the key features of a graph — intercepts, vertices, asymptotes, maxima and "
            "minima — and find points of intersection using technology."
        ),
        "concept": [
            "**Syllabus card — AI SL 2.4.** Determine key features of graphs: maximum and "
            "minimum values, intercepts, symmetry, vertex, zeros of functions or roots of "
            "equations, vertical and horizontal asymptotes. Finding the point of intersection of "
            "two curves or lines using technology. **Papers 1 and 2.**",
            "Every feature has a question that produces it. $y$-intercept: put $x = 0$. "
            "$x$-intercepts (zeros, roots): solve $f(x) = 0$. Vertex of a quadratic: the axis of "
            "symmetry $x = -\\frac{b}{2a}$, then substitute. Maxima and minima of anything else: "
            "the GDC's maximum/minimum tool.",
            "Asymptotes are the lines a graph approaches but never reaches. A VERTICAL asymptote "
            "sits where the function is undefined — for a rational function, where the "
            "denominator is zero. A HORIZONTAL asymptote is the value the function settles "
            "towards as $x$ runs off to $\\pm\\infty$; for $\\frac{ax + b}{cx + d}$ that value is "
            "$\\frac{a}{c}$, and for $ka^{x} + c$ it is $y = c$.",
            "Intersections: enter both functions and use the intersect tool. Report the "
            "COORDINATES unless the question asks only for one of them, and give 3 s.f. unless "
            "the values are exact. Two curves can meet twice, once, or not at all — and 'they do "
            "not meet' is a legitimate, markable answer."
        ],
        "keyIdea": (
            "Features are questions you ask the graph. Intercepts come from setting a variable "
            "to zero, asymptotes from where the function breaks or settles, and intersections "
            "from asking two graphs where they agree."
        ),
        "facts": [
            {
                "title": "Axis of symmetry of a parabola",
                "latex": "x = -\\frac{b}{2a}",
                "explanation": "Booklet (AI SL 2.5). Substitute back to get the vertex's $y$-coordinate.",
            },
            {
                "title": "Asymptotes of a rational function",
                "latex": "y = \\frac{ax + b}{cx + d} \\;\\Rightarrow\\; x = -\\frac{d}{c}, \\quad y = \\frac{a}{c}",
                "explanation": "Not in the booklet — read them off: the denominator's zero, and the ratio of leading coefficients.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-24-we1",
                "statement": (
                    "Consider $f(x) = \\dfrac{2x + 6}{x - 4}$.  \n"
                    "**(a)** Write down the equations of the two asymptotes. **[2]**  \n"
                    "**(b)** Find the $x$- and $y$-intercepts. **[3]**  \n"
                    "**(c)** Sketch the graph. **[3]**"
                ),
                "solution": (
                    "**(a)** The denominator vanishes at $x = 4$, so $x = 4$ is a vertical "
                    "asymptote *(A1)*. For large $|x|$ the ratio tends to $\\frac{2}{1}$, so "
                    "$y = 2$ is a horizontal asymptote *(A1)*.  \n"
                    "**(b)** $x$-intercept: $2x + 6 = 0$ gives $x = -3$ *(M1 A1)*. "
                    "$y$-intercept: $f(0) = \\dfrac{6}{-4} = -1.5$ *(A1)*.  \n"
                    "**(c)** Two branches, one in each region either side of $x = 4$, each "
                    "hugging both asymptotes, with the left branch passing through $(-3, 0)$ and "
                    "$(0, -1.5)$ *(A3)*.  \n"
                    "**Narrative:** the horizontal asymptote is the ratio of the LEADING "
                    "coefficients, $\\frac{2}{1}$ — the $+6$ and the $-4$ stop mattering once "
                    "$x$ is huge. A quick numeric sanity check beats memorising the rule: "
                    "$f(1000) = \\frac{2006}{996} \\approx 2.01$, which is $2$ from above."
                ),
                "check": [
                    "Rational(2*0 + 6, 0 - 4) == Rational(-3, 2)",
                    "2*(-3) + 6 == 0",
                    "Eq(limit((2*x + 6)/(x - 4), x, oo), 2)",
                    "Abs(Rational(2*1000 + 6, 1000 - 4) - 2) < Rational(2, 100)",
                ],
            },
            {
                "id": "aisl-24-we2",
                "statement": (
                    "**(a)** Find the coordinates of the points where $y = x^{2} - 2x - 3$ meets "
                    "$y = x + 1$. **[4]**  \n"
                    "**(b)** Use technology to find, to 3 s.f., the values of $x$ for which "
                    "$2^{x} = x + 3$. **[3]**"
                ),
                "solution": (
                    "**(a)** Setting them equal: $x^{2} - 2x - 3 = x + 1$ *(M1)*, so "
                    "$x^{2} - 3x - 4 = 0$ and $x = 4$ or $x = -1$ *(A1)*. Substituting into "
                    "$y = x + 1$: the points are $(4, 5)$ and $(-1, 0)$ *(A1 A1)*.  \n"
                    "**(b)** Graphing $y = 2^{x}$ and $y = x + 3$ and using the intersect tool "
                    "*(M1)*: $x = -2.86$ and $x = 2.44$ *(A1 A1)*.  \n"
                    "**Narrative:** part (a) can be done algebraically, and on an AI paper it "
                    "can equally be done by graphing — both earn full marks. Part (b) has no "
                    "algebraic route at all, which is exactly why AI is a calculator course. "
                    "Note the second intersection: it is easy to find the obvious crossing near "
                    "$x = 2.4$ and miss the one out at $x = -2.86$ where the exponential is "
                    "creeping along just above zero. Scroll left before you commit."
                ),
                "check": [
                    "4**2 - 2*4 - 3 == 4 + 1",
                    "(-1)**2 - 2*(-1) - 3 == -1 + 1",
                    "expand((x - 4)*(x + 1)) == x**2 - 3*x - 4",
                    "Abs(2**Rational(-286, 100) - (Rational(-286, 100) + 3)) < Rational(1, 100)",
                    "Abs(2**Rational(244, 100) - (Rational(244, 100) + 3)) < Rational(2, 100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Giving only the $x$-value of an intersection.",
                "correction": "'Find the point of intersection' wants coordinates. One number is half an answer and usually half the marks.",
                "authored": True,
            },
            {
                "text": "Reporting the first intersection the calculator offers as the only one.",
                "correction": "Scan the whole domain. A line and a curve routinely meet twice, and the second crossing carries its own mark.",
                "authored": True,
            },
            {
                "text": "Reading the horizontal asymptote of $\\frac{2x+6}{x-4}$ as $y = -\\frac{6}{4}$.",
                "correction": "That is the $y$-intercept. The horizontal asymptote is the ratio of the leading coefficients, $y = 2$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-24-t1",
                "statement": (
                    "Write down the equations of the asymptotes of $y = 3 + \\dfrac{5}{x - 2}$. "
                    "**[2]**"
                ),
                "solution": (
                    "The fraction is undefined at $x = 2$, so $x = 2$ is the vertical asymptote "
                    "*(A1)*.  \n"
                    "As $x \\to \\pm\\infty$ the fraction tends to $0$, leaving $y = 3$ *(A1)*."
                ),
                "check": [
                    "Eq(limit(3 + 5/(x - 2), x, oo), 3)",
                ],
            },
            {
                "id": "aisl-24-t2",
                "statement": (
                    "Find the coordinates of the local minimum of $f(x) = x^{3} - 6x^{2} + 5$. "
                    "**[3]**"
                ),
                "solution": (
                    "From the GDC the minimum is at $x = 4$ *(M1 A1)*, where "
                    "$f(4) = 64 - 96 + 5 = -27$, so the point is $(4, -27)$ *(A1)*.  \n"
                    "Confirming by hand: $f'(x) = 3x^{2} - 12x = 3x(x - 4)$, zero at $x = 0$ and "
                    "$x = 4$; $x = 0$ is the local maximum."
                ),
                "check": [
                    "diff(x**3 - 6*x**2 + 5, x) == 3*x**2 - 12*x",
                    "4**3 - 6*4**2 + 5 == -27",
                    "0**3 - 6*0**2 + 5 == 5",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 2.4 · Papers 1 & 2",
                    "title": "Interrogate the graph",
                    "body": (
                        "A graph will tell you anything if you ask precisely. Where do you cross "
                        "the axes? Where do you turn? What do you approach but never reach? "
                        "Where do you agree with this other graph? Four questions, and this "
                        "whole code is their answers."
                    ),
                },
                {
                    "kind": "parabolaGraph",
                    "eyebrow": "Play",
                    "title": "Move $b$ and $c$, watch the vertex",
                    "teach": (
                        "Step $b$ and $c$ and keep an eye on the axis of symmetry "
                        "$x = -\\frac{b}{2a}$. Changing $c$ slides the curve vertically and "
                        "leaves the axis where it was; changing $b$ moves the axis itself. That "
                        "is the whole reason the formula has no $c$ in it."
                    ),
                    "config": {"mode": "standard", "b": -2, "c": -3, "interactive": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "One question per feature",
                    "beats": [
                        "$y$-intercept: substitute $x = 0$.",
                        "Zeros: solve $f(x) = 0$, by graph or by solver.",
                        "Vertex: $x = -\\frac{b}{2a}$, then substitute back.",
                        "Vertical asymptote: denominator zero. Horizontal: the value $f$ settles on.",
                        "Intersection: graph both, use intersect, report coordinates.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A rational function, feature by feature",
                    "problemId": "aisl-24-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Settle down",
                    "title": "Where does it level off?",
                    "prompt": "The graph of $y = \\dfrac{4}{x + 3} - 2$ has a horizontal asymptote at",
                    "options": ["$y = -2$", "$y = 0$", "$y = 4$", "$x = -3$"],
                    "correctIndex": 0,
                    "explanation": (
                        "As $x$ grows, $\\frac{4}{x+3} \\to 0$ and the graph settles on "
                        "$y = -2$. The option $x = -3$ is the VERTICAL asymptote — a real "
                        "feature, but not the one asked for."
                    ),
                    "check": [
                        "Eq(limit(4/(x + 3) - 2, x, oo), -2)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two intersections, two methods",
                    "problemId": "aisl-24-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Count them",
                    "title": "How many meetings?",
                    "prompt": (
                        "The line $y = 5$ and the parabola $y = x^{2} - 4x + 9$ intersect at"
                    ),
                    "options": [
                        "exactly one point",
                        "two points",
                        "no points",
                        "infinitely many points",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$x^{2} - 4x + 9 = 5$ gives $x^{2} - 4x + 4 = 0$, i.e. "
                        "$(x - 2)^{2} = 0$ — a repeated root at $x = 2$. The line is the "
                        "tangent at the vertex $(2, 5)$, so it touches once."
                    ),
                    "check": [
                        "expand((x - 2)**2) == x**2 - 4*x + 4",
                        "2**2 - 4*2 + 9 == 5",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Three significant figures, unless it is exact",
                    "body": (
                        "$x = 2.44$ is right; $x = 2.4$ throws away a mark and $x = 2.4436$ "
                        "risks one. When the intersection is exact — $x = 4$, $x = -1$ — write "
                        "it exactly; padding it to $4.00$ suggests you rounded something that "
                        "was never approximate."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-24-t1"},
                {"kind": "tryIt", "problemId": "aisl-24-t2"},
                {
                    "kind": "recap",
                    "title": "Key features, compressed",
                    "points": [
                        "Intercepts come from setting one variable to zero.",
                        "Vertical asymptote: denominator zero. Horizontal: the settling value.",
                        "Vertex at $x = -\\frac{b}{2a}$; other turning points from the GDC.",
                        "Intersections: graph both, report coordinates, and check for a second one.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — AI SL 2.5: modelling with functions
# ===========================================================================
def lesson_modelling_with_functions():
    return {
        "slug": "modelling-with-functions",
        "title": "Choosing a Model: the Six Families",
        "concreteComparison": (
            "A cooling coffee, a thrown ball, a tide, a population, the brightness of a lamp as "
            "you back away from it — five behaviours, five different shapes. Recognising which "
            "shape a situation has is the single most valuable skill on this course, because it "
            "decides every equation you write afterwards."
        ),
        "objective": (
            "Recognise which function family a context calls for, fit it to given information, "
            "and read its parameters back as statements about the situation."
        ),
        "concept": [
            "**Syllabus card — AI SL 2.5.** Modelling with linear, quadratic, exponential "
            "growth and decay, direct and inverse variation, cubic, and sinusoidal functions. "
            "**Papers 1 and 2.** All six general forms are in the formula booklet; the marks are "
            "for choosing among them and interpreting the constants.",
            "How to tell them apart from data. Constant DIFFERENCES between successive values "
            "mean linear. Constant RATIOS mean exponential. A single turning point with "
            "symmetry means quadratic. Two turning points mean cubic. A repeating rise and fall "
            "means sinusoidal. A product $xy$ that stays constant means inverse variation.",
            "Exponential models carry an asymptote: $f(x) = ka^{x} + c$ settles on $y = c$, and "
            "in a cooling problem $c$ IS the room temperature. That constant is where most of "
            "the interpretation marks sit — a decay model without it decays all the way to zero, "
            "which no real coffee does.",
            "Sinusoidal models: in $f(x) = a\\sin(bx) + d$, $|a|$ is the amplitude (half the "
            "distance from lowest to highest), $d$ is the midline (their average), and the "
            "period is $\\frac{2\\pi}{b}$. A tide with a $12$-hour cycle therefore has "
            "$b = \\frac{\\pi}{6}$ — read the period off the context and solve for $b$."
        ],
        "keyIdea": (
            "Identify the family from the behaviour, fit the constants to the given facts, then "
            "say what each constant MEANS. Interpretation is where the marks are."
        ),
        "facts": [
            {
                "title": "The six booklet families",
                "latex": "mx + c \\;|\\; ax^2+bx+c \\;|\\; ka^{x} + c \\;|\\; ax^{n} \\;|\\; ax^3+bx^2+cx+d \\;|\\; a\\sin(bx)+d",
                "explanation": "Booklet (AI SL 2.5). Linear, quadratic, exponential, variation, cubic, sinusoidal.",
            },
            {
                "title": "Amplitude, midline, period",
                "latex": "a\\sin(bx) + d: \\quad \\text{amplitude } |a|, \\quad \\text{midline } y = d, \\quad \\text{period } \\frac{2\\pi}{b}",
                "explanation": "Booklet. Read the period from the context, then solve for $b$.",
            },
            {
                "title": "Direct and inverse variation",
                "latex": "y = ax^{n}, \\; n \\in \\mathbb{Z} \\qquad (n > 0 \\text{ direct}, \\; n < 0 \\text{ inverse})",
                "explanation": "Booklet. One data pair fixes $a$; the exponent comes from the physical law.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-25-we1",
                "statement": (
                    "A cup of coffee cools according to $T(t) = 22 + 58(0.94)^{t}$, where $T$ is "
                    "in $^\\circ$C and $t$ is in minutes.  \n"
                    "**(a)** Write down the initial temperature. **[1]**  \n"
                    "**(b)** State the temperature of the room, justifying your answer. **[2]**  \n"
                    "**(c)** Find the time taken for the coffee to cool to $40\\,^\\circ$C. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** $T(0) = 22 + 58 = 80\\,^\\circ$C *(A1)*.  \n"
                    "**(b)** As $t \\to \\infty$, $(0.94)^{t} \\to 0$ *(R1)*, so $T \\to 22$: "
                    "the room is at $22\\,^\\circ$C *(A1)*.  \n"
                    "**(c)** $22 + 58(0.94)^{t} = 40$ gives $(0.94)^{t} = \\dfrac{18}{58}$ "
                    "*(M1)*. Solving on the GDC *(A1)*: $t = 18.9$ minutes *(A1)*.  \n"
                    "**Narrative:** the $22$ is doing two jobs — it is the horizontal asymptote "
                    "of the graph AND the room temperature, and part (b) is asking you to say "
                    "that those are the same fact. The coffee never actually reaches "
                    "$22\\,^\\circ$C in the model, which is a limitation worth noting: real "
                    "coffee does, because real rooms are not infinitely large heat sinks."
                ),
                "check": [
                    "22 + 58 == 80",
                    "Eq(limit(22 + 58*Rational(94, 100)**t, t, oo), 22)",
                    "Abs(58*Rational(94, 100)**Rational(189, 10) - 18) < Rational(2, 10)",
                    "40 - 22 == 18",
                ],
            },
            {
                "id": "aisl-25-we2",
                "statement": (
                    "The depth of water in a harbour is modelled by "
                    "$d(t) = 5.2 + 3.4\\sin\\!\\left(\\dfrac{\\pi t}{6}\\right)$ metres, $t$ "
                    "hours after midnight.  \n"
                    "**(a)** Write down the maximum and minimum depths. **[2]**  \n"
                    "**(b)** Find the period, and interpret it. **[2]**  \n"
                    "**(c)** Find the first time after midnight at which the depth is $7$ m. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** Maximum $= 5.2 + 3.4 = 8.6$ m; minimum $= 5.2 - 3.4 = 1.8$ m "
                    "*(A1 A1)*.  \n"
                    "**(b)** Period $= \\dfrac{2\\pi}{\\pi/6} = 12$ hours *(A1)* — the tide "
                    "completes one full cycle every $12$ hours *(A1)*.  \n"
                    "**(c)** $3.4\\sin\\!\\left(\\frac{\\pi t}{6}\\right) = 1.8$ *(M1)*. "
                    "Solving on the GDC with the calculator in RADIANS *(A1)*: "
                    "$t = 1.07$ hours *(A1)*.  \n"
                    "**Narrative:** the midline $5.2$ is the average depth and the amplitude "
                    "$3.4$ is the swing either side of it — so the extremes are just "
                    "$5.2 \\pm 3.4$, no calculus required. In (c) the mode setting is not a "
                    "detail: in degrees the calculator reads $\\frac{\\pi t}{6}$ as a tiny angle "
                    "and returns an answer roughly $57$ times too large."
                ),
                "check": [
                    "Rational(52, 10) + Rational(34, 10) == Rational(86, 10)",
                    "Rational(52, 10) - Rational(34, 10) == Rational(18, 10)",
                    "Eq(2*pi/(pi/6), 12)",
                    "Abs(Rational(52, 10) + Rational(34, 10)*sin(pi*Rational(107, 100)/6) - 7) < Rational(1, 100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Fitting an exponential without its constant term.",
                "correction": "$ka^{x}$ decays to zero; $ka^{x} + c$ decays to $c$. In cooling and similar contexts the $c$ is the ambient value and carries the interpretation marks.",
                "authored": True,
            },
            {
                "text": "Leaving the calculator in degrees for a sinusoidal model.",
                "correction": "Models written with $\\pi$ in the argument are in radians. Set the mode before you solve anything.",
                "authored": True,
            },
            {
                "text": "Choosing a linear model because the values are increasing.",
                "correction": "Increasing is not enough. Test the DIFFERENCES for linear and the RATIOS for exponential, and let the data pick.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-25-t1",
                "statement": (
                    "The intensity $I$ of a lamp varies inversely with the square of the "
                    "distance $d$. At $d = 2$ m the intensity is $45$ lux. Find the intensity at "
                    "$d = 6$ m. **[3]**"
                ),
                "solution": (
                    "$I = \\dfrac{k}{d^{2}}$, so $k = 45 \\times 2^{2} = 180$ *(M1 A1)*.  \n"
                    "At $d = 6$: $I = \\dfrac{180}{36} = 5$ lux *(A1)*.  \n"
                    "Tripling the distance divided the intensity by nine — the inverse-square "
                    "law in one line."
                ),
                "check": [
                    "45*2**2 == 180",
                    "Rational(180, 6**2) == 5",
                    "Rational(45, 5) == 3**2",
                ],
            },
            {
                "id": "aisl-25-t2",
                "statement": (
                    "An open box is made from a $20$ cm by $14$ cm sheet by cutting squares of "
                    "side $x$ cm from the corners. Its volume is "
                    "$V(x) = x(20 - 2x)(14 - 2x)$, $0 < x < 7$. Find the value of $x$ that "
                    "maximises $V$, and the maximum volume. **[4]**"
                ),
                "solution": (
                    "Expanding, $V(x) = 4x^{3} - 68x^{2} + 280x$ *(A1)*. Using the GDC's maximum "
                    "tool on $0 < x < 7$ *(M1)*: $x = 2.70$ cm *(A1)*, giving "
                    "$V = 339$ cm$^{3}$ (3 s.f.) *(A1)*.  \n"
                    "The other stationary point, near $x = 8.6$, lies outside the domain — you "
                    "cannot cut two $8.6$ cm squares from a $14$ cm side."
                ),
                "check": [
                    "expand(x*(20 - 2*x)*(14 - 2*x)) == 4*x**3 - 68*x**2 + 280*x",
                    "Abs((34 - sqrt(316))/6 - Rational(270, 100)) < Rational(1, 100)",
                    "Abs(4*Rational(270, 100)**3 - 68*Rational(270, 100)**2 + 280*Rational(270, 100) - 339) < 1",
                    "2*(34 + sqrt(316))/6 > 14",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 2.5 · Papers 1 & 2",
                    "title": "Six shapes, one decision",
                    "body": (
                        "AA gives you the function and asks what it does. AI gives you a "
                        "situation and asks which function it is. Six families cover the whole "
                        "syllabus, and every one of them is in the formula booklet — the work is "
                        "in choosing and interpreting, not in remembering."
                    ),
                },
                {
                    "kind": "expGraph",
                    "eyebrow": "Play",
                    "title": "Growth, decay, and the line they leave behind",
                    "teach": (
                        "Slide the base past $1$ and back. Above $1$ the curve accelerates away; "
                        "below $1$ it flattens towards its asymptote without ever landing on it. "
                        "That asymptote is the constant term a cooling model needs and a raw "
                        "$ka^{x}$ lacks."
                    ),
                    "config": {"mode": "growth", "a": 4, "b": 0.75, "interactive": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Diagnose, fit, interpret",
                    "beats": [
                        "Diagnose: constant differences → linear; constant ratios → exponential; one turn → quadratic; repeats → sinusoidal.",
                        "Fit: substitute the given facts, one equation per unknown constant.",
                        "Solve for the constants — on the GDC, not by hand.",
                        "Interpret every constant in the words of the context.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Coffee, cooling towards the room",
                    "problemId": "aisl-25-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Diagnose",
                    "title": "Which family?",
                    "prompt": (
                        "A sequence of readings is $50, 65, 84.5, 109.85$. The best model is"
                    ),
                    "options": [
                        "exponential, because each reading is $1.3$ times the last",
                        "linear, because the readings increase steadily",
                        "quadratic, because the increases are getting bigger",
                        "sinusoidal, because the readings rise",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$65 \\div 50 = 1.3$, $84.5 \\div 65 = 1.3$, "
                        "$109.85 \\div 84.5 = 1.3$ — a constant ratio, which is the signature of "
                        "an exponential. The differences $15, 19.5, 25.35$ are not constant, so "
                        "linear is out."
                    ),
                    "check": [
                        "Rational(65, 50) == Rational(13, 10)",
                        "Rational(845, 650) == Rational(13, 10)",
                        "Rational(10985, 8450) == Rational(13, 10)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A tide, in amplitude and midline",
                    "problemId": "aisl-25-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the period",
                    "title": "Find $b$ from the cycle",
                    "prompt": (
                        "A wheel's height is $h = a\\sin(bt) + d$ and one full turn takes $8$ "
                        "minutes. Then $b$ equals"
                    ),
                    "options": [
                        "$\\frac{\\pi}{4}$",
                        "$8$",
                        "$\\frac{1}{8}$",
                        "$2\\pi$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The period is $\\frac{2\\pi}{b}$, so $\\frac{2\\pi}{b} = 8$ gives "
                        "$b = \\frac{2\\pi}{8} = \\frac{\\pi}{4}$."
                    ),
                    "check": [
                        "Eq(2*pi/(pi/4), 8)",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "The constants are the answer",
                    "body": (
                        "Almost every AI modelling question ends with 'interpret' or 'state what "
                        "this represents'. Practise saying it: the midline is the average, the "
                        "amplitude is the swing, the exponential constant is the ambient value, "
                        "the linear intercept is the fixed cost."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-25-t1"},
                {"kind": "tryIt", "problemId": "aisl-25-t2"},
                {
                    "kind": "recap",
                    "title": "Model families, compressed",
                    "points": [
                        "Constant differences → linear; constant ratios → exponential.",
                        "$ka^{x} + c$ settles on $y = c$ — the ambient value.",
                        "$a\\sin(bx) + d$: amplitude $|a|$, midline $d$, period $\\frac{2\\pi}{b}$.",
                        "$y = ax^{n}$ with $n < 0$ is inverse variation; one data pair fixes $a$.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — AI SL 2.6: the modelling process
# ===========================================================================
def lesson_modelling_process():
    return {
        "slug": "the-modelling-process",
        "title": "The Modelling Process: Fit, Test, Reflect",
        "concreteComparison": (
            "A weather forecast is a model that publishes its own confidence. Nobody expects it "
            "to be exactly right; they expect it to be useful over the next few days and to say "
            "so. A mathematical model on this course is judged the same way — by how well it "
            "fits, and by how honestly it names the range over which it can be trusted."
        ),
        "objective": (
            "Run the full modelling cycle: pose the problem and its assumptions, develop and fit "
            "a model, test it against the data, reflect on its limitations, and use it."
        ),
        "concept": [
            "**Syllabus card — AI SL 2.6.** Modelling skills: use the modelling process; "
            "develop and fit the model; test and reflect upon the model; use the model. "
            "**Papers 1 and 2.** This code is assessed as the closing parts of longer questions "
            "on every other topic — it is how AI ends a Paper 2 question.",
            "The cycle has four stages and exam questions walk them in order. POSE: what is "
            "being asked, and what are we assuming? DEVELOP: choose a family and fit the "
            "constants. TEST: compare predictions with the data, using $r$, residuals, or "
            "percentage error. REFLECT: where does it break, and what would you change?",
            "Fitting a line to data is done by regression on the GDC, and $r$ reports how well "
            "it fits: near $\\pm 1$ is strong, near $0$ is weak. Two warnings that carry marks. "
            "A strong $r$ does NOT mean one variable causes the other. And $r$ measures LINEAR "
            "fit only — a perfect parabola can have $r$ near zero.",
            "Interpolation — predicting inside the range of the data — is reasonable. "
            "EXTRAPOLATION, predicting outside it, is where models fail, and exam questions "
            "invite you to say so. A study-hours model that predicts a score of $130\\%$ has not "
            "made an arithmetic mistake; it has been used outside the range where it means "
            "anything."
        ],
        "keyIdea": (
            "Fit it, test it, then say where it stops being true. A model without a stated "
            "limitation is an incomplete answer on this course."
        ),
        "facts": [
            {
                "title": "The modelling cycle",
                "latex": "\\text{pose} \\to \\text{develop} \\to \\text{test} \\to \\text{reflect} \\to \\text{use}",
                "explanation": "Not a formula — the structure AI questions follow. Answer in the same order.",
            },
            {
                "title": "Percentage error",
                "latex": "\\varepsilon = \\left|\\frac{v_A - v_E}{v_E}\\right| \\times 100\\%",
                "explanation": "Booklet (AI SL 1.6). $v_E$ is the exact or measured value — it goes on the bottom.",
            },
            {
                "title": "What $r$ does and does not say",
                "latex": "|r| \\approx 1 \\Rightarrow \\text{strong LINEAR fit} \\quad\\not\\Rightarrow\\quad \\text{causation}",
                "explanation": "Two separate warnings, and each is a stock R-mark.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-26-we1",
                "statement": (
                    "A teacher records study hours $x$ and test scores $y$ for five students:  \n"
                    "$x$: $2, 4, 5, 7, 8$  \n"
                    "$y$: $55, 62, 68, 75, 80$  \n"
                    "**(a)** Find the equation of the regression line of $y$ on $x$. **[3]**  \n"
                    "**(b)** Find $r$ and interpret it. **[2]**  \n"
                    "**(c)** Estimate the score of a student who studies $6$ hours. **[2]**  \n"
                    "**(d)** Comment on using the model for a student who studies $20$ hours. "
                    "**[2]**"
                ),
                "solution": (
                    "**(a)** From the GDC's linear regression *(M1)*: $y = 4.17x + 46.3$ "
                    "(3 s.f.) *(A1 A1)*.  \n"
                    "**(b)** $r = 0.997$ *(A1)* — a very strong positive linear correlation "
                    "*(A1)*.  \n"
                    "**(c)** $y = 4.17(6) + 46.3 = 71.3$ *(M1 A1)*.  \n"
                    "**(d)** The model predicts about $130$, which is impossible on a test "
                    "scored out of $100$ *(A1)*; $20$ hours is far outside the data range "
                    "$2 \\le x \\le 8$, so this is extrapolation and the prediction is not "
                    "reliable *(R1)*.  \n"
                    "**Narrative:** part (c) is interpolation — $6$ sits comfortably inside the "
                    "data — and is exactly what the model is for. Part (d) is the same "
                    "arithmetic pushed past where the evidence reaches, and the mark is for "
                    "SAYING so rather than for the number. An $r$ of $0.997$ does not protect "
                    "you here: a strong fit inside the data says nothing at all about outside it."
                ),
                "check": [
                    "(5*1863 - 26*340)/(5*158 - 26**2) == Rational(25, 6)",
                    "(340 - Rational(25, 6)*26)/5 == Rational(139, 3)",
                    "Rational(25, 6)*6 + Rational(139, 3) == Rational(214, 3)",
                    "Abs(Rational(214, 3) - Rational(713, 10)) < Rational(5, 100)",
                    "Abs(95/sqrt(Rational(228, 10)*398) - Rational(997, 1000)) < Rational(1, 1000)",
                    "Rational(25, 6)*20 + Rational(139, 3) > 100",
                ],
            },
            {
                "id": "aisl-26-we2",
                "statement": (
                    "A biologist records a population $P$ at times $t$ years:  \n"
                    "$t$: $0, 5, 10, 15$  \n"
                    "$P$: $120, 190, 305, 487$  \n"
                    "**(a)** Explain why an exponential model is more suitable than a linear "
                    "one. **[2]**  \n"
                    "**(b)** The model is $P = 120a^{t}$. Use the value at $t = 15$ to find $a$. "
                    "**[3]**  \n"
                    "**(c)** Predict the population at $t = 20$. **[2]**  \n"
                    "**(d)** State one limitation of this model. **[1]**"
                ),
                "solution": (
                    "**(a)** The successive ratios are $1.58$, $1.61$, $1.60$ — close to "
                    "constant *(A1)* — while the differences $70, 115, 182$ grow steadily, so "
                    "the data is not linear *(A1)*.  \n"
                    "**(b)** $120a^{15} = 487$ gives $a^{15} = \\dfrac{487}{120}$ *(M1)*, so "
                    "$a = \\left(\\dfrac{487}{120}\\right)^{1/15}$ *(A1)* $= 1.098$ *(A1)*.  \n"
                    "**(c)** $P = 120(1.098)^{20} = 777$ *(M1 A1)*.  \n"
                    "**(d)** Unlimited exponential growth ignores food, space and disease; a "
                    "real population levels off *(R1)*.  \n"
                    "**Narrative:** part (a) is the diagnostic step done explicitly, and it is "
                    "worth writing out both tests even when the answer is obvious — the marks "
                    "are for the RATIOS, not for the conclusion. Part (b) fits through one "
                    "point, which is the standard AI approach when the model's starting value "
                    "is given; a regression on $\\ln P$ would give a slightly different $a$, and "
                    "either is acceptable if the method is shown."
                ),
                "check": [
                    "Abs(Rational(190, 120) - Rational(158, 100)) < Rational(1, 100)",
                    "Abs(Rational(305, 190) - Rational(161, 100)) < Rational(1, 100)",
                    "Abs(Rational(487, 305) - Rational(160, 100)) < Rational(1, 100)",
                    "Abs(Rational(487, 120)**Rational(1, 15) - Rational(1098, 1000)) < Rational(1, 1000)",
                    "Abs(120*(Rational(487, 120)**Rational(1, 15))**20 - 777) < 2",
                    "190 - 120 == 70",
                    "487 - 305 == 182",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reading a strong $r$ as proof that $x$ causes $y$.",
                "correction": "Correlation is not causation. A lurking variable or pure coincidence explains many strong correlations, and saying so is a stock R-mark.",
                "authored": True,
            },
            {
                "text": "Using the regression line far outside the data range without comment.",
                "correction": "That is extrapolation. Give the number if asked, then state that it is unreliable and why.",
                "authored": True,
            },
            {
                "text": "Putting the wrong value on the bottom of the percentage-error fraction.",
                "correction": "The denominator is the exact or measured value $v_E$, not your prediction. Swapping them changes the answer.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-26-t1",
                "statement": (
                    "A regression line is $y = 2.4x + 11.6$ with $r = 0.42$.  \n"
                    "**(a)** Predict $y$ when $x = 15$. **[2]**  \n"
                    "**(b)** Comment on the reliability of this prediction. **[2]**"
                ),
                "solution": (
                    "**(a)** $y = 2.4(15) + 11.6 = 47.6$ *(M1 A1)*.  \n"
                    "**(b)** $r = 0.42$ is a weak correlation *(A1)*, so the line explains "
                    "little of the variation and the prediction is unreliable regardless of "
                    "where $x = 15$ sits *(R1)*."
                ),
                "check": [
                    "Rational(24, 10)*15 + Rational(116, 10) == Rational(476, 10)",
                    "Rational(42, 100) < Rational(5, 10)",
                ],
            },
            {
                "id": "aisl-26-t2",
                "statement": (
                    "A model predicts a mass of $48.0$ g. The measured mass is $45.6$ g. Find "
                    "the percentage error. **[2]**"
                ),
                "solution": (
                    "$\\varepsilon = \\left|\\dfrac{48.0 - 45.6}{45.6}\\right| \\times 100$ "
                    "*(M1)* $= 5.26\\%$ (3 s.f.) *(A1)*.  \n"
                    "The measured value goes on the bottom — dividing by $48.0$ instead gives "
                    "$5.00\\%$, a different and wrong answer."
                ),
                "check": [
                    "Abs(Rational(24, 10)/Rational(456, 10)*100 - Rational(526, 100)) < Rational(1, 100)",
                    "Rational(24, 10)/48*100 == 5",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 2.6 · Papers 1 & 2",
                    "title": "A model is an argument, not an answer",
                    "body": (
                        "This code is where AI parts company with every other maths course you "
                        "have taken. The question is not only 'what does the model say' but "
                        "'should we believe it, and how far'. Those last parts of a Paper 2 "
                        "question are worth as much as the algebra that got you there."
                    ),
                },
                {
                    "kind": "scatterPlot",
                    "eyebrow": "Play",
                    "title": "Drag a line onto the cloud",
                    "teach": (
                        "Move the slope and intercept and watch the fit improve. Regression on "
                        "the GDC does exactly this, automatically, by making the total squared "
                        "vertical gap as small as it can go — and $r$ is the score it gives "
                        "itself."
                    ),
                    "config": {
                        "mode": "fit",
                        "xLabel": "hours studied",
                        "yLabel": "score (out of 10)",
                        "m0": 0.5,
                        "b0": 4,
                    },
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "The four stages, as exam parts",
                    "beats": [
                        "Pose: name the variables and state an assumption.",
                        "Develop: choose the family, fit the constants from the given facts.",
                        "Test: $r$, a residual, or a percentage error against a known value.",
                        "Reflect: name the range where it holds and one thing it ignores.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Regression, and where it stops working",
                    "problemId": "aisl-26-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read $r$ carefully",
                    "title": "What a strong $r$ proves",
                    "prompt": (
                        "Ice-cream sales and drowning incidents have $r = 0.93$ across a year. "
                        "The correct conclusion is"
                    ),
                    "options": [
                        "both rise with a third variable — hot weather",
                        "eating ice cream causes drowning",
                        "drowning incidents cause ice-cream sales",
                        "the correlation must be a calculation error",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "A strong correlation is real here, and it is explained by a lurking "
                        "variable: temperature drives both. Correlation measures association, "
                        "never cause."
                    ),
                    "check": [
                        "Rational(93, 100) > Rational(8, 10)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Choosing the family from the data",
                    "problemId": "aisl-26-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Inside or outside",
                    "title": "Which prediction is safe?",
                    "prompt": (
                        "A model is fitted to data covering $10 \\le x \\le 40$. The more "
                        "reliable prediction is at"
                    ),
                    "options": [
                        "$x = 25$, because it lies inside the data range",
                        "$x = 90$, because the model is a formula and works everywhere",
                        "$x = 5$, because it is close to the lower end",
                        "either — the range of the data has no bearing on reliability",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$x = 25$ is interpolation: the data actually supports it. Both $5$ and "
                        "$90$ are outside the range, and the further out you go the less the "
                        "evidence says."
                    ),
                    "check": [
                        "(10 < 25) & (25 < 40)",
                        "(5 < 10) | (90 > 40)",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Every 'comment' part wants two sentences",
                    "body": (
                        "One sentence with the number or the judgement, one with the reason. "
                        "'The prediction is $130$, which exceeds the maximum score, and $20$ "
                        "hours lies well outside the data range' is two marks. 'It is "
                        "unreliable' is none."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-26-t1"},
                {"kind": "tryIt", "problemId": "aisl-26-t2"},
                {
                    "kind": "recap",
                    "title": "Modelling, compressed",
                    "points": [
                        "Pose, develop, test, reflect, use — answer in that order.",
                        "$r$ measures LINEAR fit and never proves causation.",
                        "Interpolation is supported; extrapolation must be flagged.",
                        "Percentage error divides by the exact or measured value.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Unit banks
# ===========================================================================
def practice_bank():
    return [
        {
            "id": "aisl-fn-p01",
            "statement": "Find the gradient of the line through $(1, -2)$ and $(5, 6)$. **[2]**",
            "solution": "$m = \\dfrac{6 - (-2)}{5 - 1} = \\dfrac{8}{4}$ *(M1)* $= 2$ *(A1)*.",
            "badges": [{"text": "ib-ai-sl-2.1", "mono": True}, {"text": "P1"}],
            "check": ["Rational(6 - (-2), 5 - 1) == 2"],
        },
        {
            "id": "aisl-fn-p02",
            "statement": (
                "Write $2x - 5y = 20$ in the form $y = mx + c$ and state the gradient. **[2]**"
            ),
            "solution": (
                "$-5y = -2x + 20$, so $y = \\dfrac{2}{5}x - 4$ *(A1)*; the gradient is "
                "$\\dfrac{2}{5}$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.1", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(2, 5)*0 - 4 == -4",
                "Rational(2, 5)*10 - 4 == 0",
            ],
        },
        {
            "id": "aisl-fn-p03",
            "statement": (
                "Find the equation of the line through $(3, -1)$ that is parallel to "
                "$y = -4x + 7$. **[3]**"
            ),
            "solution": (
                "Parallel means the same gradient, $m = -4$ *(A1)*. Then "
                "$y + 1 = -4(x - 3)$ *(M1)*, so $y = -4x + 11$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.1", "mono": True}, {"text": "P1"}],
            "check": ["-4*3 + 11 == -1"],
        },
        {
            "id": "aisl-fn-p04",
            "statement": (
                "A line has gradient $\\dfrac{3}{4}$. Find the gradient of any line "
                "perpendicular to it. **[2]**"
            ),
            "solution": (
                "The negative reciprocal: $-\\dfrac{4}{3}$ *(M1 A1)*. Check: "
                "$\\dfrac{3}{4} \\times -\\dfrac{4}{3} = -1$ ✓."
            ),
            "badges": [{"text": "ib-ai-sl-2.1", "mono": True}, {"text": "P1"}],
            "check": ["Rational(3, 4)*Rational(-4, 3) == -1"],
        },
        {
            "id": "aisl-fn-p05",
            "statement": "Given $f(x) = 5 - 2x$, find $f(-3)$. **[2]**",
            "solution": "$f(-3) = 5 - 2(-3) = 5 + 6$ *(M1)* $= 11$ *(A1)*.",
            "badges": [{"text": "ib-ai-sl-2.2", "mono": True}, {"text": "P1"}],
            "check": ["5 - 2*(-3) == 11"],
        },
        {
            "id": "aisl-fn-p06",
            "statement": (
                "Given $f(x) = 4x + 9$, find $f^{-1}(x)$ and hence $f^{-1}(1)$. **[3]**"
            ),
            "solution": (
                "$y = 4x + 9 \\Rightarrow x = \\dfrac{y - 9}{4}$ *(M1)*, so "
                "$f^{-1}(x) = \\dfrac{x - 9}{4}$ *(A1)*, giving "
                "$f^{-1}(1) = \\dfrac{-8}{4} = -2$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.2", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(1 - 9, 4) == -2",
                "4*(-2) + 9 == 1",
            ],
        },
        {
            "id": "aisl-fn-p07",
            "statement": "State the domain and the range of $g(x) = \\sqrt{x - 2}$. **[2]**",
            "solution": (
                "The square root needs $x - 2 \\ge 0$, so the domain is $x \\ge 2$ *(A1)*. The "
                "output of a square root is never negative, so the range is "
                "$g(x) \\ge 0$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.2", "mono": True}, {"text": "P1"}],
            "check": [
                "sqrt(2 - 2) == 0",
                "sqrt(11 - 2) == 3",
            ],
        },
        {
            "id": "aisl-fn-p08",
            "statement": (
                "For $y = 3^{x} - 9$, write down the $x$-intercept and the equation of the "
                "horizontal asymptote. **[3]**"
            ),
            "solution": (
                "$3^{x} = 9$ gives $x = 2$, so the intercept is $(2, 0)$ *(M1 A1)*.  \n"
                "As $x \\to -\\infty$, $3^{x} \\to 0$, so the asymptote is $y = -9$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.3", "mono": True}, {"text": "P2"}],
            "check": [
                "3**2 - 9 == 0",
                "Eq(limit(3**x - 9, x, -oo), -9)",
            ],
        },
        {
            "id": "aisl-fn-p09",
            "statement": (
                "For $f(x) = x^{2} - 6x + 5$, write down the $y$-intercept and the equation of "
                "the axis of symmetry. **[2]**"
            ),
            "solution": (
                "$f(0) = 5$, so the $y$-intercept is $(0, 5)$ *(A1)*.  \n"
                "$x = -\\dfrac{-6}{2(1)} = 3$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.3", "mono": True}, {"text": "P1"}],
            "check": [
                "0**2 - 6*0 + 5 == 5",
                "Rational(6, 2*1) == 3",
            ],
        },
        {
            "id": "aisl-fn-p10",
            "statement": (
                "Write down the equations of the asymptotes of $y = \\dfrac{2}{x - 5} + 1$. "
                "**[2]**"
            ),
            "solution": (
                "Vertical: $x = 5$, where the denominator is zero *(A1)*.  \n"
                "Horizontal: as $x \\to \\pm\\infty$ the fraction vanishes, leaving "
                "$y = 1$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.4", "mono": True}, {"text": "P1"}],
            "check": ["Eq(limit(2/(x - 5) + 1, x, oo), 1)"],
        },
        {
            "id": "aisl-fn-p11",
            "statement": (
                "Find the coordinates of the vertex of $y = 2x^{2} - 12x + 7$. **[3]**"
            ),
            "solution": (
                "$x = -\\dfrac{-12}{2(2)} = 3$ *(M1 A1)*, and "
                "$y = 2(9) - 36 + 7 = -11$, so the vertex is $(3, -11)$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.4", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(12, 2*2) == 3",
                "2*3**2 - 12*3 + 7 == -11",
            ],
        },
        {
            "id": "aisl-fn-p12",
            "statement": (
                "Use technology to find the coordinates of the points where $y = x^{2}$ meets "
                "$y = x + 6$. **[3]**"
            ),
            "solution": (
                "The intersect tool gives $x = 3$ and $x = -2$ *(M1 A1)*, so the points are "
                "$(3, 9)$ and $(-2, 4)$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.4", "mono": True}, {"text": "P2"}],
            "check": [
                "3**2 == 3 + 6",
                "(-2)**2 == -2 + 6",
            ],
        },
        {
            "id": "aisl-fn-p13",
            "statement": (
                "A machine's value is $V(t) = 24\\,000(0.85)^{t}$ dollars after $t$ years. Find "
                "$V(5)$ to the nearest dollar. **[3]**"
            ),
            "solution": (
                "$V(5) = 24\\,000(0.85)^{5}$ *(M1 A1)* $= \\$10\\,649$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.5", "mono": True}, {"text": "P2"}],
            "check": ["Abs(24000*Rational(85, 100)**5 - 10649) < 1"],
        },
        {
            "id": "aisl-fn-p14",
            "statement": (
                "$y$ varies directly with $x^{3}$. When $x = 2$, $y = 40$. Find $y$ when "
                "$x = 5$. **[3]**"
            ),
            "solution": (
                "$y = ax^{3}$, so $a = \\dfrac{40}{2^{3}} = 5$ *(M1 A1)*.  \n"
                "Then $y = 5(5)^{3} = 625$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.5", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(40, 2**3) == 5",
                "5*5**3 == 625",
            ],
        },
        {
            "id": "aisl-fn-p15",
            "statement": (
                "The depth of water is $d(t) = 4 + 2.5\\sin\\!\\left(\\dfrac{\\pi t}{6}\\right)$ "
                "metres. Write down the maximum depth and the period. **[2]**"
            ),
            "solution": (
                "Maximum $= 4 + 2.5 = 6.5$ m *(A1)*.  \n"
                "Period $= \\dfrac{2\\pi}{\\pi/6} = 12$ hours *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.5", "mono": True}, {"text": "P1"}],
            "check": [
                "4 + Rational(25, 10) == Rational(65, 10)",
                "Eq(2*pi/(pi/6), 12)",
            ],
        },
        {
            "id": "aisl-fn-p16",
            "statement": (
                "A regression line is $y = -1.8x + 52$ with $r = -0.91$.  \n"
                "**(a)** Predict $y$ when $x = 12$. **[2]**  \n"
                "**(b)** Describe the correlation. **[1]**"
            ),
            "solution": (
                "**(a)** $y = -1.8(12) + 52 = 30.4$ *(M1 A1)*.  \n"
                "**(b)** Strong negative linear correlation *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.6", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(-18, 10)*12 + 52 == Rational(304, 10)",
                "Rational(-91, 100) < Rational(-8, 10)",
            ],
        },
        {
            "id": "aisl-fn-p17",
            "statement": (
                "A model predicts $250$ units; the measured value is $232$ units. Find the "
                "percentage error, to 3 s.f. **[2]**"
            ),
            "solution": (
                "$\\varepsilon = \\left|\\dfrac{250 - 232}{232}\\right| \\times 100$ *(M1)* "
                "$= 7.76\\%$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.6", "mono": True}, {"text": "P2"}],
            "check": ["Abs(Rational(18, 232)*100 - Rational(776, 100)) < Rational(1, 100)"],
        },
        {
            "id": "aisl-fn-p18",
            "statement": (
                "A linear model $P = 3.2t + 45$ was fitted to data for $0 \\le t \\le 10$.  \n"
                "**(a)** Use it to predict $P$ when $t = 60$. **[2]**  \n"
                "**(b)** Explain why this prediction is unreliable. **[2]**"
            ),
            "solution": (
                "**(a)** $P = 3.2(60) + 45 = 237$ *(M1 A1)*.  \n"
                "**(b)** $t = 60$ is far outside the range $0 \\le t \\le 10$ over which the "
                "model was fitted *(A1)*, so nothing in the data supports a straight line "
                "continuing that far — this is extrapolation *(R1)*."
            ),
            "badges": [{"text": "ib-ai-sl-2.6", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(32, 10)*60 + 45 == 237",
                "60 > 10",
            ],
        },
    ]


def test_bank():
    return [
        {
            "id": "aisl-fn-x01",
            "statement": (
                "The points are $A(-1, 4)$, $B(5, -2)$ and $C(k, 7)$.  \n"
                "**(a)** Find the equation of the line $AB$. **[3]**  \n"
                "**(b)** Given that $AC$ is perpendicular to $AB$, find $k$. **[4]**"
            ),
            "solution": (
                "**(a)** $m_{AB} = \\dfrac{-2 - 4}{5 - (-1)} = -1$ *(M1 A1)*, so "
                "$y - 4 = -(x + 1)$, i.e. $y = -x + 3$ *(A1)*.  \n"
                "**(b)** Perpendicular gradient $= 1$ *(A1)*. Then "
                "$\\dfrac{7 - 4}{k - (-1)} = 1$ *(M1)*, so $k + 1 = 3$ *(A1)* and "
                "$k = 2$ *(A1)*.  \n"
                "Check: $B$ lies on $AB$ since $-5 + 3 = -2$ ✓."
            ),
            "badges": [{"text": "ib-ai-sl-2.1", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(-2 - 4, 5 - (-1)) == -1",
                "-5 + 3 == -2",
                "Rational(7 - 4, 2 - (-1)) == 1",
                "(-1)*1 == -1",
            ],
        },
        {
            "id": "aisl-fn-x02",
            "statement": (
                "The function $f$ is given by $f(x) = \\dfrac{x + 3}{2}$ for "
                "$-5 \\le x \\le 7$.  \n"
                "**(a)** Find the range of $f$. **[2]**  \n"
                "**(b)** Find $f^{-1}(x)$. **[2]**  \n"
                "**(c)** Solve $f(x) = f^{-1}(x)$. **[3]**"
            ),
            "solution": (
                "**(a)** $f$ is increasing, so the range runs from $f(-5) = -1$ to "
                "$f(7) = 5$: $-1 \\le f(x) \\le 5$ *(M1 A1)*.  \n"
                "**(b)** $y = \\dfrac{x + 3}{2} \\Rightarrow x = 2y - 3$, so "
                "$f^{-1}(x) = 2x - 3$ *(M1 A1)*.  \n"
                "**(c)** $\\dfrac{x + 3}{2} = 2x - 3$ gives $x + 3 = 4x - 6$ *(M1)*, so "
                "$3x = 9$ and $x = 3$ *(A1 A1)*.  \n"
                "The solution sits on $y = x$ — as it must, since a function and its inverse "
                "are mirror images in that line."
            ),
            "badges": [{"text": "ib-ai-sl-2.2", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(-5 + 3, 2) == -1",
                "Rational(7 + 3, 2) == 5",
                "2*3 - 3 == 3",
                "Rational(3 + 3, 2) == 3",
            ],
        },
        {
            "id": "aisl-fn-x03",
            "statement": (
                "Consider $f(x) = x^{3} - 3x^{2} - 9x + 5$ for $-4 \\le x \\le 6$.  \n"
                "**(a)** Find the coordinates of the local maximum and the local minimum. "
                "**[4]**  \n"
                "**(b)** State the number of $x$-intercepts, justifying your answer. **[3]**"
            ),
            "solution": (
                "**(a)** From the GDC *(M1)*: local maximum $(-1, 10)$ *(A1)* and local "
                "minimum $(3, -22)$ *(A2)*.  \n"
                "**(b)** At the ends of the domain $f(-4) = -71$ and $f(6) = 59$ *(A1)*. The "
                "curve rises from $-71$ to the maximum $10$ (one crossing), falls to the "
                "minimum $-22$ (a second), and rises to $59$ (a third) *(R1)*, so there are "
                "three $x$-intercepts *(A1)*.  \n"
                "Confirming the turning points by hand: $f'(x) = 3x^{2} - 6x - 9 = "
                "3(x - 3)(x + 1)$."
            ),
            "badges": [{"text": "ib-ai-sl-2.3", "mono": True}, {"text": "P2"}],
            "check": [
                "diff(x**3 - 3*x**2 - 9*x + 5, x) == 3*x**2 - 6*x - 9",
                "expand(3*(x - 3)*(x + 1)) == 3*x**2 - 6*x - 9",
                "(-1)**3 - 3*(-1)**2 - 9*(-1) + 5 == 10",
                "3**3 - 3*3**2 - 9*3 + 5 == -22",
                "(-4)**3 - 3*(-4)**2 - 9*(-4) + 5 == -71",
                "6**3 - 3*6**2 - 9*6 + 5 == 59",
            ],
        },
        {
            "id": "aisl-fn-x04",
            "statement": (
                "Consider $y = \\dfrac{3x - 12}{x + 2}$.  \n"
                "**(a)** Write down the equations of the asymptotes. **[2]**  \n"
                "**(b)** Find both axis intercepts. **[2]**  \n"
                "**(c)** Find the coordinates of the points where the curve meets "
                "$y = x - 6$. **[4]**"
            ),
            "solution": (
                "**(a)** $x = -2$ and $y = 3$ *(A1 A1)*.  \n"
                "**(b)** $3x - 12 = 0$ gives $(4, 0)$; at $x = 0$, "
                "$y = \\dfrac{-12}{2} = -6$, giving $(0, -6)$ *(A1 A1)*.  \n"
                "**(c)** $\\dfrac{3x - 12}{x + 2} = x - 6$ gives "
                "$3x - 12 = x^{2} - 4x - 12$ *(M1)*, so $x^{2} - 7x = 0$ and "
                "$x = 0$ or $x = 7$ *(A1)*. The points are $(0, -6)$ and $(7, 1)$ *(A1 A1)*.  \n"
                "The first of these is the $y$-intercept found in (b) — the line "
                "$y = x - 6$ passes through it."
            ),
            "badges": [{"text": "ib-ai-sl-2.4", "mono": True}, {"text": "P2"}],
            "check": [
                "Eq(limit((3*x - 12)/(x + 2), x, oo), 3)",
                "3*4 - 12 == 0",
                "Rational(3*0 - 12, 0 + 2) == -6",
                "expand((x - 6)*(x + 2)) == x**2 - 4*x - 12",
                "Rational(3*7 - 12, 7 + 2) == 1",
                "7 - 6 == 1",
            ],
        },
        {
            "id": "aisl-fn-x05",
            "statement": (
                "A radioactive sample has mass $M(t) = 80e^{-0.045t}$ grams after $t$ days.  \n"
                "**(a)** Write down the initial mass. **[1]**  \n"
                "**(b)** Find the mass after $30$ days, to 3 s.f. **[2]**  \n"
                "**(c)** Find the half-life of the sample, to 3 s.f. **[4]**"
            ),
            "solution": (
                "**(a)** $M(0) = 80$ g *(A1)*.  \n"
                "**(b)** $M(30) = 80e^{-1.35}$ *(M1)* $= 20.7$ g *(A1)*.  \n"
                "**(c)** Half-life solves $80e^{-0.045t} = 40$, i.e. "
                "$e^{-0.045t} = 0.5$ *(M1 A1)*. Then "
                "$t = \\dfrac{\\ln 2}{0.045}$ *(A1)* $= 15.4$ days *(A1)*.  \n"
                "The initial mass cancels, which is why a half-life depends only on the decay "
                "constant — the same reason a doubling time depends only on the rate."
            ),
            "badges": [{"text": "ib-ai-sl-2.5", "mono": True}, {"text": "P2"}],
            "check": [
                "80*exp(0) == 80",
                "Abs(80*exp(Rational(-45, 1000)*30) - Rational(207, 10)) < Rational(5, 100)",
                "Abs(log(2)/Rational(45, 1000) - Rational(154, 10)) < Rational(5, 100)",
            ],
        },
        {
            "id": "aisl-fn-x06",
            "statement": (
                "A capsule on a wheel has height "
                "$h(t) = 32 - 28\\cos\\!\\left(\\dfrac{\\pi t}{5}\\right)$ metres, $t$ minutes "
                "after boarding.  \n"
                "**(a)** Write down the greatest and least heights. **[2]**  \n"
                "**(b)** Find the time for one full revolution. **[2]**  \n"
                "**(c)** Find the first time at which the height is $46$ m. **[3]**"
            ),
            "solution": (
                "**(a)** Greatest $= 32 + 28 = 60$ m; least $= 32 - 28 = 4$ m *(A1 A1)*.  \n"
                "**(b)** Period $= \\dfrac{2\\pi}{\\pi/5} = 10$ minutes *(M1 A1)*.  \n"
                "**(c)** $28\\cos\\!\\left(\\frac{\\pi t}{5}\\right) = -14$, so "
                "$\\cos\\!\\left(\\frac{\\pi t}{5}\\right) = -\\dfrac{1}{2}$ *(M1)*. The first "
                "solution is $\\frac{\\pi t}{5} = \\frac{2\\pi}{3}$ *(A1)*, giving "
                "$t = \\dfrac{10}{3} = 3.33$ minutes *(A1)*.  \n"
                "The cosine (rather than sine) form is what puts the capsule at its LOWEST "
                "point at $t = 0$ — which is where you board."
            ),
            "badges": [{"text": "ib-ai-sl-2.5", "mono": True}, {"text": "P2"}],
            "check": [
                "32 + 28 == 60",
                "32 - 28 == 4",
                "Eq(2*pi/(pi/5), 10)",
                "Eq(32 - 28*cos(pi*Rational(10, 3)/5), 46)",
                "Eq(32 - 28*cos(0), 4)",
            ],
        },
        {
            "id": "aisl-fn-x07",
            "statement": (
                "The power $P$ watts generated by a turbine varies directly with the cube of the "
                "wind speed $v$ m s$^{-1}$. At $v = 8$ the power is $1024$ W.  \n"
                "**(a)** Find the constant of variation. **[2]**  \n"
                "**(b)** Find the power at $v = 12$. **[2]**  \n"
                "**(c)** Find the wind speed that generates $6750$ W. **[3]**"
            ),
            "solution": (
                "**(a)** $P = av^{3}$, so $a = \\dfrac{1024}{8^{3}} = 2$ *(M1 A1)*.  \n"
                "**(b)** $P = 2(12)^{3} = 3456$ W *(M1 A1)*.  \n"
                "**(c)** $2v^{3} = 6750$ gives $v^{3} = 3375$ *(M1 A1)*, so "
                "$v = 15$ m s$^{-1}$ *(A1)*.  \n"
                "Note how fast a cube grows: raising the wind speed by half — from $8$ to $12$ "
                "— more than triples the power."
            ),
            "badges": [{"text": "ib-ai-sl-2.5", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(1024, 8**3) == 2",
                "2*12**3 == 3456",
                "2*15**3 == 6750",
                "3456 > 3*1024",
            ],
        },
        {
            "id": "aisl-fn-x08",
            "statement": (
                "A scientist records:  \n"
                "$x$: $1, 3, 4, 6, 7$  \n"
                "$y$: $9.2, 12.6, 13.8, 17.4, 19.6$  \n"
                "**(a)** Find the equation of the regression line of $y$ on $x$, giving the "
                "coefficients to 3 s.f. **[3]**  \n"
                "**(b)** Find $r$ and describe the correlation. **[2]**  \n"
                "**(c)** Estimate $y$ when $x = 5$, and state whether the estimate is reliable. "
                "**[3]**"
            ),
            "solution": (
                "**(a)** Linear regression on the GDC *(M1)* gives "
                "$y = 1.71x + 7.36$ *(A1 A1)*.  \n"
                "**(b)** $r = 0.998$ *(A1)* — a very strong positive linear correlation "
                "*(A1)*.  \n"
                "**(c)** $y = 1.71(5) + 7.36 = 15.9$ *(M1 A1)*. Since $x = 5$ lies inside the "
                "data range $1 \\le x \\le 7$ and the correlation is very strong, the estimate "
                "is reliable *(R1)*.  \n"
                "Interpolation plus a strong $r$ is the one combination that justifies calling "
                "a prediction reliable — either alone is not enough."
            ),
            "badges": [{"text": "ib-ai-sl-2.6", "mono": True}, {"text": "P2"}],
            "check": [
                "(5*Rational(3438, 10) - 21*Rational(726, 10))/(5*111 - 21**2) == Rational(162, 95)",
                "(Rational(726, 10) - Rational(162, 95)*21)/5 == Rational(699, 95)",
                "Abs(Rational(162, 95) - Rational(171, 100)) < Rational(5, 1000)",
                "Abs(Rational(699, 95) - Rational(736, 100)) < Rational(5, 1000)",
                "Rational(162, 95)*5 + Rational(699, 95) == Rational(1509, 95)",
                "Abs(Rational(1509, 95) - Rational(159, 10)) < Rational(2, 100)",
                "Abs(Rational(3888, 100)/sqrt(Rational(228, 10)*Rational(66608, 1000)) - Rational(998, 1000)) < Rational(1, 1000)",
            ],
        },
        {
            "id": "aisl-fn-x09",
            "statement": (
                "A drink cools according to $T(t) = 20 + Ae^{-kt}$, where $T$ is in "
                "$^\\circ$C and $t$ in minutes. It starts at $85\\,^\\circ$C and is "
                "$60\\,^\\circ$C after $8$ minutes.  \n"
                "**(a)** Find $A$. **[2]**  \n"
                "**(b)** Find $k$, to 3 s.f. **[4]**  \n"
                "**(c)** Find the temperature after $25$ minutes. **[2]**  \n"
                "**(d)** State what the constant $20$ represents, and one limitation of the "
                "model. **[2]**"
            ),
            "solution": (
                "**(a)** At $t = 0$: $20 + A = 85$ *(M1)*, so $A = 65$ *(A1)*.  \n"
                "**(b)** $20 + 65e^{-8k} = 60$ gives $e^{-8k} = \\dfrac{40}{65}$ *(M1 A1)*. "
                "Then $-8k = \\ln\\!\\left(\\dfrac{8}{13}\\right)$ *(A1)*, so "
                "$k = 0.0607$ *(A1)*.  \n"
                "**(c)** $T(25) = 20 + 65e^{-0.0607(25)}$ *(M1)* $= 34.3\\,^\\circ$C *(A1)*.  \n"
                "**(d)** The $20$ is the room temperature — the value $T$ approaches as "
                "$t \\to \\infty$ *(A1)*. The model assumes the room stays at exactly "
                "$20\\,^\\circ$C and that the drink never quite reaches it, which no real drink "
                "does *(R1)*.  \n"
                "Every part of this question is one stage of the modelling cycle: fit, solve, "
                "use, reflect."
            ),
            "badges": [{"text": "ib-ai-sl-2.6", "mono": True}, {"text": "P2"}],
            "check": [
                "85 - 20 == 65",
                "Rational(60 - 20, 65) == Rational(8, 13)",
                "Abs(log(Rational(13, 8))/8 - Rational(607, 10000)) < Rational(1, 10000)",
                "Abs(20 + 65*exp(-25*log(Rational(13, 8))/8) - Rational(343, 10)) < Rational(5, 100)",
                "Eq(limit(20 + 65*exp(-Rational(607, 10000)*t), t, oo), 20)",
            ],
        },
    ]


# ===========================================================================
# Assembly
# ===========================================================================
def build():
    lessons = [
        lesson_straight_lines(),
        lesson_functions_domain_range(),
        lesson_graphs_and_sketching(),
        lesson_key_features(),
        lesson_modelling_with_functions(),
        lesson_modelling_process(),
    ]
    return {
        "slug": "functions",
        "title": "Functions",
        "unit": 2,
        "status": "published",
        "blurb": (
            "AI Topic 2, complete: straight lines and their gradients, functions with domain, "
            "range and inverses, graphing and sketching with technology, key features and "
            "points of intersection, the six modelling families, and the modelling process "
            "itself — AI SL 2.1 to 2.6, taught to markscheme standard."
        ),
        "buildsOn": (
            "Unit 1's exponential and logarithmic work, which returns here as the exponential "
            "model family. The largest topic on the course by assessment weight."
        ),
        "lessons": lessons,
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }


def selfcheck(unit):
    from sympy import sympify
    n_checks = 0
    problems = []
    for les in unit["lessons"]:
        problems += les["workedExamples"] + les["tryIt"]
        ids = {p["id"] for p in les["workedExamples"] + les["tryIt"]}
        for step in les["interactive"]["steps"]:
            if step["kind"] in ("worked", "tryIt"):
                assert step["problemId"] in ids, f"{les['slug']}: dangling problemId {step['problemId']}"
            if step["kind"] == "tapQuestion":
                assert len(step["options"]) == len(set(step["options"])), f"{les['slug']}: dup options"
                for c in step["check"]:
                    assert bool(sympify(c)) is True, f"{les['slug']} tapQ: {c}"
                    n_checks += 1
    problems += unit["practice"] + unit["testYourself"]
    ids = [p["id"] for p in problems]
    assert len(ids) == len(set(ids)), "duplicate problem ids"
    for p in problems:
        for c in p["check"]:
            assert bool(sympify(c)) is True, f"{p['id']}: NOT TRUE: {c}"
            n_checks += 1
    return len(problems), n_checks


def main():
    unit = build()
    n_problems, n_checks = selfcheck(unit)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(unit, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    n_steps = sum(len(l["interactive"]["steps"]) for l in unit["lessons"])
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(unit['lessons'])} lessons, "
          f"{n_steps} interactive steps, {n_problems} problems, {n_checks} sympy checks OK")


if __name__ == "__main__":
    main()
