#!/usr/bin/env python3
"""IB Mathematics: Applications & Interpretation SL — Unit 5 (Topic 5: Calculus).

Builds data/genmath/ib-ai-sl/calculus.json: eight lessons, one per official
subtopic code AI SL 5.1-5.8, same anatomy as Units 1-4 (syllabus cards,
booklet flags, M/A/R markscheme + narrative solutions, interactive widgets,
sympy check[] everywhere). Banks tagged ib-ai-sl-5.x.

AI's calculus is deliberately narrower than AA's and deliberately more
applied. There is no product rule, no quotient rule, no chain rule and no
trigonometric differentiation — the whole differentiation toolkit is the power
rule on integer exponents. What AI adds instead is 5.8, the trapezoidal rule,
which has no counterpart in Analysis & Approaches and exists because an
applied course needs to handle areas under curves it cannot integrate.

Run: python3 scripts/ib/build_ai_sl_unit5.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-ai-sl", "calculus.json")


# ===========================================================================
# Lesson 1 — AI SL 5.1: limits and the derivative
# ===========================================================================
def lesson_limits_and_derivative():
    return {
        "slug": "limits-and-the-derivative",
        "title": "Limits and the Derivative as a Rate of Change",
        "concreteComparison": (
            "A car's speedometer reads $80$ km/h at a single instant — but speed is distance "
            "over time, and at an instant no time passes and no distance is covered. The "
            "derivative is the idea that rescues the speedometer: the limit of the average speed "
            "as the interval shrinks to nothing."
        ),
        "objective": (
            "Understand a limit informally, and read the derivative both as the gradient of a "
            "curve and as a rate of change in context."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.1.** Introduction to the concept of a limit; derivative "
            "interpreted as gradient function and as rate of change. **Papers 1 and 2.** No "
            "formal limit algebra is required — the idea, and its two readings, are.",
            "A LIMIT is what a function heads towards. Writing "
            "$\\lim_{x \\to 2} f(x) = 5$ says that as $x$ gets arbitrarily close to $2$, "
            "$f(x)$ gets arbitrarily close to $5$ — and says nothing at all about $f(2)$, which "
            "may be $5$, may be something else, or may not exist.",
            "The derivative is built from a limit. The gradient of the line joining two points "
            "on a curve is $\\dfrac{f(x+h) - f(x)}{h}$; let $h$ shrink towards zero and that "
            "secant line settles onto the TANGENT. Its gradient is $f'(x)$, and the point of the "
            "limit is that you cannot simply set $h = 0$ — that gives $\\frac{0}{0}$.",
            "$f'(x)$ has two readings and AI examines both. GEOMETRICALLY it is the gradient of "
            "the curve at $x$ — positive where the curve rises, negative where it falls, zero at "
            "a turning point. In CONTEXT it is a rate of change, and its units are the units of "
            "$y$ divided by the units of $x$: dollars per item, metres per second, degrees per "
            "minute.",
            "Stating those units is a mark. If $C(x)$ is the cost in dollars of producing $x$ "
            "items, then $C'(20) = 4.5$ means 'when $20$ items are being produced, the cost is "
            "rising at $\\$4.50$ per additional item'. The number alone is half the answer."
        ],
        "keyIdea": (
            "The derivative is the limit of an average rate as the interval shrinks. Read it as "
            "a gradient on a graph and as a rate — with units — in a context."
        ),
        "facts": [
            {
                "title": "The derivative as a limit",
                "latex": "f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}",
                "explanation": "The definition. AI needs the idea, not the algebra.",
            },
            {
                "title": "Two readings of $f'(x)$",
                "latex": "\\text{gradient of the tangent} \\quad = \\quad \\text{rate of change of } y \\text{ with respect to } x",
                "explanation": "Same number, two languages. Context questions want the second, with units.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-51-we1",
                "statement": (
                    "For $f(x) = x^{2}$, consider the gradient of the line joining the point "
                    "where $x = 3$ to the point where $x = 3 + h$.  \n"
                    "**(a)** Show that this gradient equals $6 + h$. **[3]**  \n"
                    "**(b)** Complete the pattern for $h = 1$, $h = 0.1$ and $h = 0.01$, and "
                    "state the limit. **[3]**  \n"
                    "**(c)** Write down $f'(3)$ and interpret it. **[2]**"
                ),
                "solution": (
                    "**(a)** The gradient is "
                    "$\\dfrac{(3+h)^{2} - 3^{2}}{h} = \\dfrac{9 + 6h + h^{2} - 9}{h}$ "
                    "*(M1 A1)* $= \\dfrac{6h + h^{2}}{h} = 6 + h$ *(AG)*.  \n"
                    "**(b)** $h = 1$ gives $7$; $h = 0.1$ gives $6.1$; $h = 0.01$ gives $6.01$ "
                    "*(A1 A1)*. As $h \\to 0$ the gradient $\\to 6$ *(A1)*.  \n"
                    "**(c)** $f'(3) = 6$ *(A1)* — the tangent to $y = x^{2}$ at $x = 3$ has "
                    "gradient $6$ *(A1)*.  \n"
                    "**Narrative:** the cancellation in (a) is the whole trick. Before "
                    "cancelling, setting $h = 0$ gives $\\frac{0}{0}$ and says nothing; after "
                    "cancelling, the expression $6 + h$ is perfectly happy at $h = 0$. The limit "
                    "is not a value the gradient ever takes for a real secant — no two distinct "
                    "points give exactly $6$ — but it is the value they approach, and that is "
                    "what a tangent gradient means."
                ),
                "check": [
                    "expand(((3 + h)**2 - 3**2)/h) == 6 + h",
                    "6 + 1 == 7",
                    "6 + Rational(1, 10) == Rational(61, 10)",
                    "6 + Rational(1, 100) == Rational(601, 100)",
                    "Eq(limit((x**2 - 9)/(x - 3), x, 3), 6)",
                ],
            },
            {
                "id": "aisl-51-we2",
                "statement": (
                    "The cost in dollars of producing $x$ units is $C(x)$, and "
                    "$C'(50) = 12$.  \n"
                    "**(a)** State the units of $C'(x)$. **[1]**  \n"
                    "**(b)** Interpret $C'(50) = 12$ in context. **[2]**  \n"
                    "**(c)** Estimate the extra cost of increasing production from $50$ to $53$ "
                    "units, and state one reason your answer is only an estimate. **[3]**"
                ),
                "solution": (
                    "**(a)** Dollars per unit *(A1)*.  \n"
                    "**(b)** When $50$ units are being produced, the total cost is rising at "
                    "$\\$12$ per additional unit *(A1 A1)*.  \n"
                    "**(c)** Extra cost $\\approx 3 \\times 12 = \\$36$ *(M1 A1)*. This assumes "
                    "the rate stays at $\\$12$ per unit across the whole interval, whereas "
                    "$C'(x)$ generally changes as $x$ does *(R1)*.  \n"
                    "**Narrative:** part (c) is the derivative used as a local linear "
                    "approximation, and the reason it is only an estimate is exactly the reason "
                    "calculus exists: the rate is itself changing. Over three units the drift is "
                    "usually small; over three hundred it would be worthless."
                ),
                "check": [
                    "3*12 == 36",
                    "50 + 3 == 53",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reading $\\lim_{x \\to 2} f(x)$ as $f(2)$.",
                "correction": "A limit describes what the function APPROACHES near $2$. The value at $2$ may differ, or may not exist at all.",
                "authored": True,
            },
            {
                "text": "Giving a rate of change with no units.",
                "correction": "The units are those of $y$ per unit of $x$ — dollars per item, metres per second. Naming them is routinely a mark.",
                "authored": True,
            },
            {
                "text": "Setting $h = 0$ before simplifying the difference quotient.",
                "correction": "That gives $\\frac{0}{0}$. Expand and cancel the $h$ FIRST, then let $h$ go to zero.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-51-t1",
                "statement": (
                    "For $f(x) = x^{2}$, find the gradient of the line joining $x = 5$ to "
                    "$x = 5 + h$, and hence write down $f'(5)$. **[4]**"
                ),
                "solution": (
                    "$\\dfrac{(5+h)^{2} - 25}{h} = \\dfrac{10h + h^{2}}{h} = 10 + h$ "
                    "*(M1 A1)*.  \n"
                    "As $h \\to 0$ this tends to $10$ *(M1)*, so $f'(5) = 10$ *(A1)*."
                ),
                "check": [
                    "expand(((5 + h)**2 - 25)/h) == 10 + h",
                    "Eq(limit((x**2 - 25)/(x - 5), x, 5), 10)",
                ],
            },
            {
                "id": "aisl-51-t2",
                "statement": (
                    "A tank's volume $V$ litres after $t$ minutes satisfies $V'(8) = -3.5$. "
                    "State the units and interpret the value. **[3]**"
                ),
                "solution": (
                    "The units are litres per minute *(A1)*.  \n"
                    "At $t = 8$ minutes the volume is DECREASING at $3.5$ litres per minute "
                    "*(A1 A1)* — the negative sign is the emptying."
                ),
                "check": [
                    "Rational(-35, 10) < 0",
                    "Abs(Rational(-35, 10)) == Rational(35, 10)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.1 · Papers 1 & 2",
                    "title": "The speedometer problem",
                    "body": (
                        "Average speed needs an interval. Instantaneous speed needs no interval "
                        "at all — which sounds impossible until you take averages over shorter "
                        "and shorter intervals and watch them settle on a number. That number is "
                        "the derivative."
                    ),
                },
                {
                    "kind": "tangentGraph",
                    "eyebrow": "Play",
                    "title": "The secant collapses onto the tangent",
                    "teach": (
                        "Shrink $h$ and watch the line through two points swing until it just "
                        "touches. The gradient readout closes in on a single value — and it "
                        "never quite arrives, which is exactly why the definition needs a limit "
                        "rather than a substitution."
                    ),
                    "config": {"mode": "secant"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Reading a derivative in context",
                    "beats": [
                        "Identify what $y$ and $x$ measure.",
                        "The units of $f'$ are $y$-units per $x$-unit — say them.",
                        "Positive means increasing, negative means decreasing.",
                        "Multiply by a small change in $x$ to estimate the change in $y$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Shrinking $h$ on $y = x^{2}$",
                    "problemId": "aisl-51-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Units",
                    "title": "What does $P'(t)$ measure?",
                    "prompt": (
                        "$P(t)$ is a population in thousands, $t$ in years. The units of "
                        "$P'(t)$ are"
                    ),
                    "options": [
                        "thousands per year",
                        "years per thousand",
                        "thousands",
                        "years",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "A derivative is always the output's units divided by the input's — "
                        "here thousands of people per year. Inverting them describes how long "
                        "it takes to gain a thousand people, a different quantity."
                    ),
                    "check": [
                        "Rational(6, 3) == 2",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A marginal cost, interpreted",
                    "problemId": "aisl-51-we2",
                },
                {
                    "kind": "limitGraph",
                    "eyebrow": "See it",
                    "title": "Approaching a value the function never takes",
                    "teach": (
                        "The curve heads towards a height as $x$ closes in — even though the "
                        "point itself has been punched out. That is precisely the situation the "
                        "difference quotient is in at $h = 0$: undefined there, perfectly "
                        "well-behaved all around it."
                    ),
                    "config": {"mode": "hole"},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the sign",
                    "title": "What a negative derivative says",
                    "prompt": (
                        "A tank's volume satisfies $V'(6) = -2$ litres per minute. At $t = 6$ "
                        "the tank is"
                    ),
                    "options": [
                        "emptying at $2$ litres per minute",
                        "filling at $2$ litres per minute",
                        "holding $-2$ litres",
                        "empty",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The SIGN gives the direction of change and the SIZE gives the speed. "
                        "The derivative says nothing about how much is in the tank — only about "
                        "how fast that amount is changing."
                    ),
                    "check": [
                        "-2 < 0",
                    ],
                },
                {"kind": "tryIt", "problemId": "aisl-51-t1"},
                {"kind": "tryIt", "problemId": "aisl-51-t2"},
                {
                    "kind": "recap",
                    "title": "The derivative, compressed",
                    "points": [
                        "A limit is what a function approaches, not what it equals.",
                        "$f'(x)$ is the limit of the secant gradient as $h \\to 0$.",
                        "Geometrically a gradient; in context a rate, with units.",
                        "Sign gives direction of change, size gives speed.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — AI SL 5.3 (taught before 5.2): the power rule
# ===========================================================================
def lesson_power_rule():
    return {
        "slug": "differentiating-polynomials",
        "title": "The Power Rule and Polynomial Derivatives",
        "concreteComparison": (
            "The whole of AI's differentiation is one rule applied term by term. Multiply by the "
            "power, then drop the power by one. Learn that sentence and every derivative on this "
            "course is bookkeeping."
        ),
        "objective": (
            "Differentiate $ax^{n}$ for integer $n$, and hence any sum of such terms, including "
            "negative powers."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.3.** The derivative of $f(x) = ax^{n}$ is "
            "$f'(x) = anx^{n-1}$, $n \\in \\mathbb{Z}$; the derivative of functions of the form "
            "$f(x) = ax^{n} + bx^{n-1} + \\ldots$. **Papers 1 and 2.** The rule is in the "
            "booklet.",
            "Differentiate term by term: the derivative of a sum is the sum of the derivatives. "
            "Two special cases fall straight out of the rule and are worth knowing by sight. A "
            "term $ax$ has derivative $a$, because $n = 1$ leaves $x^{0} = 1$. A CONSTANT has "
            "derivative $0$ — a horizontal line has gradient zero, and the constant simply "
            "disappears.",
            "Negative powers are in scope and are where marks go missing. Rewrite a fraction as "
            "a power FIRST: $\\dfrac{5}{x^{2}} = 5x^{-2}$, whose derivative is "
            "$-10x^{-3} = -\\dfrac{10}{x^{3}}$. Dropping a negative power by one makes it more "
            "negative — from $-2$ to $-3$, not to $-1$.",
            "AI's toolkit stops here. There is no product rule, no quotient rule and no chain "
            "rule on this course, so anything that looks like it needs one must first be "
            "EXPANDED or SPLIT into separate terms: $x^{2}(x + 3)$ becomes $x^{3} + 3x^{2}$, "
            "and $\\dfrac{x^{3} + 2x}{x}$ becomes $x^{2} + 2$. If a function cannot be written "
            "as a sum of powers, AI will not ask you to differentiate it by hand."
        ],
        "keyIdea": (
            "Multiply by the power, subtract one from the power, term by term. Rewrite fractions "
            "and products as sums of powers before you start."
        ),
        "facts": [
            {
                "title": "The power rule",
                "latex": "f(x) = ax^{n} \\;\\Rightarrow\\; f'(x) = anx^{n-1}, \\quad n \\in \\mathbb{Z}",
                "explanation": "Booklet (AI SL 5.3). Integer powers, positive or negative.",
            },
            {
                "title": "Two sight-reads",
                "latex": "\\frac{d}{dx}(ax) = a, \\qquad \\frac{d}{dx}(c) = 0",
                "explanation": "Both are the power rule with $n = 1$ and $n = 0$.",
            },
            {
                "title": "Negative powers",
                "latex": "\\frac{a}{x^{n}} = ax^{-n} \\;\\Rightarrow\\; \\frac{d}{dx} = -anx^{-n-1}",
                "explanation": "Rewrite as a power before differentiating. The exponent gets MORE negative.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-53-we1",
                "statement": (
                    "**(a)** Differentiate $f(x) = 4x^{3} - 6x^{2} + 5x - 9$. **[3]**  \n"
                    "**(b)** Find $f'(2)$. **[2]**  \n"
                    "**(c)** Differentiate $g(x) = 3x^{2} - \\dfrac{8}{x}$. **[3]**"
                ),
                "solution": (
                    "**(a)** Term by term: $12x^{2} - 12x + 5$ *(A1 A1 A1)* — the $-9$ "
                    "vanishes.  \n"
                    "**(b)** $f'(2) = 12(4) - 12(2) + 5$ *(M1)* $= 48 - 24 + 5 = 29$ *(A1)*.  \n"
                    "**(c)** Rewrite: $g(x) = 3x^{2} - 8x^{-1}$ *(M1)*. Then "
                    "$g'(x) = 6x + 8x^{-2}$ *(A1)* $= 6x + \\dfrac{8}{x^{2}}$ *(A1)*.  \n"
                    "**Narrative:** part (c) contains the sign trap in miniature. "
                    "$-8x^{-1}$ differentiates to $(-8)(-1)x^{-2} = +8x^{-2}$ — two negatives "
                    "making a positive. Rewriting back into fraction form at the end is good "
                    "practice: it matches the form the question was asked in, and it makes the "
                    "answer readable."
                ),
                "check": [
                    "diff(4*x**3 - 6*x**2 + 5*x - 9, x) == 12*x**2 - 12*x + 5",
                    "12*2**2 - 12*2 + 5 == 29",
                    "diff(3*x**2 - 8/x, x) == 6*x + 8/x**2",
                ],
            },
            {
                "id": "aisl-53-we2",
                "statement": (
                    "**(a)** Expand and differentiate $h(x) = x^{2}(2x - 5)$. **[3]**  \n"
                    "**(b)** Simplify and differentiate "
                    "$p(x) = \\dfrac{6x^{4} - 3x^{2}}{3x^{2}}$. **[4]**"
                ),
                "solution": (
                    "**(a)** Expanding: $h(x) = 2x^{3} - 5x^{2}$ *(M1)*, so "
                    "$h'(x) = 6x^{2} - 10x$ *(A1 A1)*.  \n"
                    "**(b)** Splitting the fraction: "
                    "$p(x) = \\dfrac{6x^{4}}{3x^{2}} - \\dfrac{3x^{2}}{3x^{2}} = "
                    "2x^{2} - 1$ *(M1 A1)*, so $p'(x) = 4x$ *(A1 A1)*.  \n"
                    "**Narrative:** both parts exist to make the same point. AI has no product "
                    "or quotient rule, so the algebra comes FIRST — and once it is done, both "
                    "derivatives are one line. Attempting to differentiate $x^{2}$ and "
                    "$(2x - 5)$ separately and multiply the results gives $2x \\times 2 = 4x$, "
                    "which is wrong and is the mistake the missing product rule is there to "
                    "prevent."
                ),
                "check": [
                    "expand(x**2*(2*x - 5)) == 2*x**3 - 5*x**2",
                    "diff(2*x**3 - 5*x**2, x) == 6*x**2 - 10*x",
                    "simplify((6*x**4 - 3*x**2)/(3*x**2)) == 2*x**2 - 1",
                    "diff(2*x**2 - 1, x) == 4*x",
                    "diff(x**2, x)*diff(2*x - 5, x) != 6*x**2 - 10*x",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Leaving the constant term in the derivative.",
                "correction": "A constant has gradient zero, so it disappears entirely. $x^2 + 7$ and $x^2 - 3$ have the same derivative.",
                "authored": True,
            },
            {
                "text": "Differentiating $x^{-2}$ to $-2x^{-1}$.",
                "correction": "Subtract one from the power: $-2 - 1 = -3$, giving $-2x^{-3}$. Negative powers get MORE negative.",
                "authored": True,
            },
            {
                "text": "Multiplying the derivatives of two factors.",
                "correction": "There is no product rule on this course because there is no need for one — expand first, then differentiate term by term.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-53-t1",
                "statement": (
                    "Differentiate $y = 5x^{4} - 2x^{3} + 7x - 11$ and find the gradient at "
                    "$x = 1$. **[4]**"
                ),
                "solution": (
                    "$\\dfrac{dy}{dx} = 20x^{3} - 6x^{2} + 7$ *(A1 A1 A1)*.  \n"
                    "At $x = 1$: $20 - 6 + 7 = 21$ *(A1)*."
                ),
                "check": [
                    "diff(5*x**4 - 2*x**3 + 7*x - 11, x) == 20*x**3 - 6*x**2 + 7",
                    "20 - 6 + 7 == 21",
                ],
            },
            {
                "id": "aisl-53-t2",
                "statement": (
                    "Differentiate $f(x) = 2x^{3} + \\dfrac{9}{x^{3}}$. **[3]**"
                ),
                "solution": (
                    "Rewrite: $f(x) = 2x^{3} + 9x^{-3}$ *(M1)*.  \n"
                    "$f'(x) = 6x^{2} - 27x^{-4}$ *(A1)* $= 6x^{2} - \\dfrac{27}{x^{4}}$ *(A1)*."
                ),
                "check": [
                    "diff(2*x**3 + 9/x**3, x) == 6*x**2 - 27/x**4",
                    "9*(-3) == -27",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.3 · Papers 1 & 2",
                    "title": "One rule, applied term by term",
                    "body": (
                        "Multiply by the power, then knock the power down by one. That is the "
                        "entire differentiation syllabus for Applications & Interpretation — no "
                        "product rule, no quotient rule, no chain rule. What AI asks instead is "
                        "that you tidy the algebra first."
                    ),
                },
                {
                    "kind": "tangentGraph",
                    "eyebrow": "Play",
                    "title": "The derivative is itself a function",
                    "teach": (
                        "Here are $f$ and $f'$ on the same grid. Where $f$ climbs, $f'$ sits "
                        "above the axis; where $f$ flattens, $f'$ crosses it. The derivative is "
                        "not one number attached to one point — it is a whole new curve."
                    ),
                    "config": {"mode": "slopeCurve"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Before you differentiate",
                    "beats": [
                        "Expand any brackets; split any fraction over a single term.",
                        "Rewrite every $\\frac{a}{x^{n}}$ as $ax^{-n}$.",
                        "Apply $anx^{n-1}$ to each term; constants go to zero.",
                        "Return negative powers to fraction form if the question used fractions.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A polynomial and a negative power",
                    "problemId": "aisl-53-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Negative powers",
                    "title": "Which way does the exponent move?",
                    "prompt": "The derivative of $x^{-3}$ is",
                    "options": [
                        "$-3x^{-4}$",
                        "$-3x^{-2}$",
                        "$3x^{-4}$",
                        "$-\\frac{1}{3}x^{-2}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Multiply by the power, $-3$, and subtract one from it: "
                        "$-3 - 1 = -4$. Moving the exponent towards zero instead is the "
                        "reflex to unlearn."
                    ),
                    "check": [
                        "diff(x**(-3), x) == -3*x**(-4)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Tidy the algebra first",
                    "problemId": "aisl-53-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "No product rule",
                    "title": "How to handle a product",
                    "prompt": "To differentiate $y = x(x + 4)$ on this course you should",
                    "options": [
                        "expand to $x^{2} + 4x$, then differentiate",
                        "differentiate each factor and multiply",
                        "use the product rule",
                        "substitute $u = x + 4$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Expanding gives $x^{2} + 4x$, whose derivative is $2x + 4$. "
                        "Multiplying the separate derivatives gives $1 \\times 1 = 1$ — plainly "
                        "wrong, and exactly why the expansion is not optional."
                    ),
                    "check": [
                        "expand(x*(x + 4)) == x**2 + 4*x",
                        "diff(x**2 + 4*x, x) == 2*x + 4",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Check one value numerically",
                    "body": (
                        "After differentiating, test your $f'$ against a quick numerical "
                        "gradient: for $f(x) = x^3$ at $x = 2$, "
                        "$\\frac{f(2.01) - f(2)}{0.01} \\approx 12.06$, and $f'(2) = 12$. Close "
                        "agreement means the algebra survived."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-53-t1"},
                {"kind": "tryIt", "problemId": "aisl-53-t2"},
                {
                    "kind": "recap",
                    "title": "The power rule, compressed",
                    "points": [
                        "$ax^{n} \\to anx^{n-1}$, term by term.",
                        "Constants vanish; $ax$ becomes $a$.",
                        "Rewrite fractions as negative powers before differentiating.",
                        "No product, quotient or chain rule — expand or split instead.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — AI SL 5.2: increasing and decreasing functions
# ===========================================================================
def lesson_increasing_decreasing():
    return {
        "slug": "increasing-and-decreasing-functions",
        "title": "Increasing, Decreasing, and What $f'$ Tells You",
        "concreteComparison": (
            "Walking a hilly path, the slope under your feet tells you what the path is doing "
            "without your having to look ahead: uphill, downhill, or momentarily level at a "
            "summit. The derivative is that slope, and reading its sign is reading the shape of "
            "the curve."
        ),
        "objective": (
            "Use the sign of $f'(x)$ to decide where a function increases and decreases, and "
            "interpret $f'(x) = 0$."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.2.** Increasing and decreasing functions; graphical "
            "interpretation of $f'(x) > 0$, $f'(x) = 0$ and $f'(x) < 0$. **Papers 1 and 2.**",
            "The three cases are the whole code. $f'(x) > 0$ means the curve is RISING — as $x$ "
            "increases so does $y$. $f'(x) < 0$ means it is FALLING. $f'(x) = 0$ means the "
            "tangent is horizontal, which happens at a maximum, at a minimum, or at a point of "
            "inflexion where the curve pauses and carries on the same way.",
            "To find where a function increases, solve $f'(x) > 0$ — usually by finding where "
            "$f'(x) = 0$ first and then testing the intervals between those points. Give the "
            "answer as an interval in $x$, such as '$f$ is increasing for $x > 3$', not as a "
            "single value.",
            "Reading a graph of $f'$ is a standard AI question and it inverts the usual "
            "direction. Where the DERIVATIVE's graph is above the axis, the original function is "
            "increasing; where the derivative crosses the axis, the original has a turning "
            "point. A maximum of $f'$ is not a maximum of $f$ — it is where $f$ is climbing "
            "fastest.",
            "In context the sign carries meaning directly. If $P(t)$ is a population and "
            "$P'(t) < 0$ for $t > 8$, the population has been falling since year $8$; if "
            "$P'(8) = 0$ and the sign changes from positive to negative there, year $8$ is when "
            "the population peaked."
        ],
        "keyIdea": (
            "Positive derivative, rising curve. Negative derivative, falling curve. Zero "
            "derivative, level tangent — and a possible turning point."
        ),
        "facts": [
            {
                "title": "The three signs",
                "latex": "f'(x) > 0 \\Rightarrow \\text{increasing}, \\quad f'(x) < 0 \\Rightarrow \\text{decreasing}, \\quad f'(x) = 0 \\Rightarrow \\text{stationary}",
                "explanation": "The whole of AI SL 5.2, and the basis of 5.6.",
            },
            {
                "title": "Reading a graph of $f'$",
                "latex": "f' \\text{ above the axis} \\Rightarrow f \\text{ rising}, \\qquad f' \\text{ crosses the axis} \\Rightarrow f \\text{ turns}",
                "explanation": "The derivative's graph describes the original's shape, not its height.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-52-we1",
                "statement": (
                    "Consider $f(x) = x^{3} - 12x + 5$.  \n"
                    "**(a)** Find $f'(x)$. **[2]**  \n"
                    "**(b)** Find the values of $x$ where $f'(x) = 0$. **[3]**  \n"
                    "**(c)** State the intervals on which $f$ is increasing and decreasing. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** $f'(x) = 3x^{2} - 12$ *(A1 A1)*.  \n"
                    "**(b)** $3x^{2} - 12 = 0$ gives $x^{2} = 4$ *(M1 A1)*, so "
                    "$x = -2$ or $x = 2$ *(A1)*.  \n"
                    "**(c)** Testing: $f'(-3) = 15 > 0$, $f'(0) = -12 < 0$, "
                    "$f'(3) = 15 > 0$ *(M1)*. So $f$ is increasing for $x < -2$ and for "
                    "$x > 2$ *(A1)*, and decreasing for $-2 < x < 2$ *(A1)*.  \n"
                    "**Narrative:** the test points do the real work, and one point per interval "
                    "is enough because $f'$ is continuous and cannot change sign without passing "
                    "through zero. Note the answer's form: intervals in $x$, not values. 'The "
                    "function increases at $x = 3$' is a much weaker statement than 'the "
                    "function increases for all $x > 2$', and only the second answers the "
                    "question."
                ),
                "check": [
                    "diff(x**3 - 12*x + 5, x) == 3*x**2 - 12",
                    "solve(3*x**2 - 12, x) == [-2, 2]",
                    "3*(-3)**2 - 12 == 15",
                    "3*0**2 - 12 == -12",
                    "3*3**2 - 12 == 15",
                ],
            },
            {
                "id": "aisl-52-we2",
                "statement": (
                    "A company's profit, in thousands of dollars, is "
                    "$P(x) = -x^{2} + 14x - 33$, where $x$ is the price per item in dollars.  \n"
                    "**(a)** Find $P'(x)$ and the value of $x$ at which $P'(x) = 0$. **[3]**  \n"
                    "**(b)** State whether profit is rising or falling at $x = 5$ and at "
                    "$x = 10$, justifying each with a calculation. **[4]**  \n"
                    "**(c)** Interpret your answers for the company. **[2]**"
                ),
                "solution": (
                    "**(a)** $P'(x) = -2x + 14$ *(A1 A1)*; $-2x + 14 = 0$ gives "
                    "$x = 7$ *(A1)*.  \n"
                    "**(b)** $P'(5) = 4 > 0$, so profit is RISING at $\\$5$ *(M1 A1)*. "
                    "$P'(10) = -6 < 0$, so profit is FALLING at $\\$10$ *(M1 A1)*.  \n"
                    "**(c)** Raising the price above $\\$5$ increases profit, but beyond "
                    "$\\$7$ further increases reduce it *(A1)*; the profit peaks at a price of "
                    "$\\$7$ *(A1)*.  \n"
                    "**Narrative:** the sign change from positive to negative at $x = 7$ is what "
                    "identifies it as a MAXIMUM rather than just a stationary point, and that "
                    "distinction is the subject of Lesson 5.6. Here the context makes it "
                    "obvious — price too low and you earn too little per item, price too high "
                    "and nobody buys — which is exactly why AI teaches the sign reading before "
                    "the formal test."
                ),
                "check": [
                    "diff(-x**2 + 14*x - 33, x) == -2*x + 14",
                    "solve(-2*x + 14, x) == [7]",
                    "-2*5 + 14 == 4",
                    "-2*10 + 14 == -6",
                    "-(7**2) + 14*7 - 33 == 16",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Answering with a value of $x$ instead of an interval.",
                "correction": "'Increasing' describes a stretch of the domain. Write $x > 2$ or $-2 < x < 2$, not a single point.",
                "authored": True,
            },
            {
                "text": "Reading a maximum of $f'$ as a maximum of $f$.",
                "correction": "Where $f'$ peaks, $f$ is climbing FASTEST. $f$ turns where $f'$ CROSSES the axis.",
                "authored": True,
            },
            {
                "text": "Assuming every $f'(x) = 0$ is a maximum or minimum.",
                "correction": "It may be a point of inflexion, where the curve flattens and continues in the same direction. Test the sign on both sides.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-52-t1",
                "statement": (
                    "For $f(x) = x^{2} - 6x + 1$, find $f'(x)$ and state where $f$ is "
                    "decreasing. **[3]**"
                ),
                "solution": (
                    "$f'(x) = 2x - 6$ *(A1)*, which is zero at $x = 3$ *(A1)*.  \n"
                    "For $x < 3$, $f'(x) < 0$, so $f$ is decreasing for $x < 3$ *(A1)*."
                ),
                "check": [
                    "diff(x**2 - 6*x + 1, x) == 2*x - 6",
                    "solve(2*x - 6, x) == [3]",
                    "2*0 - 6 < 0",
                ],
            },
            {
                "id": "aisl-52-t2",
                "statement": (
                    "The graph of $f'$ is positive for $x < 1$, zero at $x = 1$, and negative "
                    "for $x > 1$. Describe the behaviour of $f$. **[3]**"
                ),
                "solution": (
                    "$f$ increases for $x < 1$ *(A1)* and decreases for $x > 1$ *(A1)*.  \n"
                    "The sign change from positive to negative means $x = 1$ is a local MAXIMUM "
                    "of $f$ *(A1)*."
                ),
                "check": [
                    "1 > 0",
                    "-1 < 0",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.2 · Papers 1 & 2",
                    "title": "The sign is the shape",
                    "body": (
                        "You do not need to see a curve to describe it — the sign of its "
                        "derivative is enough. Positive means climbing, negative means "
                        "descending, zero means momentarily level. Three signs, three shapes, "
                        "and this whole code."
                    ),
                },
                {
                    "kind": "tangentGraph",
                    "eyebrow": "Play",
                    "title": "Slide the point, watch the slope",
                    "teach": (
                        "Move the point of tangency and watch the gradient readout run from "
                        "negative, through zero, to positive. The moment it reads zero, the "
                        "tangent is horizontal — and that is the instant the curve stops falling "
                        "and starts to rise."
                    ),
                    "config": {"mode": "tangent"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Finding the intervals",
                    "beats": [
                        "Differentiate and solve $f'(x) = 0$ — these are the boundaries.",
                        "Pick one test value inside each interval.",
                        "Evaluate $f'$ there; the sign holds across the whole interval.",
                        "Report intervals in $x$: '$f$ increases for $x > 2$'.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A cubic, interval by interval",
                    "problemId": "aisl-52-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the sign",
                    "title": "What does $f'(4) = -3$ say?",
                    "prompt": "If $f'(4) = -3$, then at $x = 4$ the curve is",
                    "options": [
                        "falling",
                        "rising",
                        "at a minimum",
                        "below the $x$-axis",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "A negative gradient means the curve is going downhill there. It says "
                        "nothing about whether $f(4)$ itself is positive or negative — that is "
                        "the height, not the slope."
                    ),
                    "check": [
                        "-3 < 0",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Profit rising, then falling",
                    "problemId": "aisl-52-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Reading $f'$",
                    "title": "The derivative's graph",
                    "prompt": (
                        "The graph of $f'$ crosses the $x$-axis from positive to negative at "
                        "$x = 5$. At $x = 5$ the function $f$ has"
                    ),
                    "options": [
                        "a local maximum",
                        "a local minimum",
                        "a root",
                        "a vertical asymptote",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$f$ rises up to $x = 5$ and falls after it, so $x = 5$ is the top of a "
                        "hill. Positive-to-negative is a maximum; negative-to-positive is a "
                        "minimum."
                    ),
                    "check": [
                        "3*(-3)**2 - 12 > 0",
                        "3*0**2 - 12 < 0",
                    ],
                },
                {"kind": "tryIt", "problemId": "aisl-52-t1"},
                {"kind": "tryIt", "problemId": "aisl-52-t2"},
                {
                    "kind": "recap",
                    "title": "Increasing and decreasing, compressed",
                    "points": [
                        "$f' > 0$ rising, $f' < 0$ falling, $f' = 0$ level.",
                        "Solve $f'(x) = 0$ for the boundaries, then test each interval.",
                        "Answer with intervals in $x$, never single values.",
                        "$f'$ crossing the axis means $f$ turns; $f'$ peaking means $f$ is steepest.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — AI SL 5.4: tangents and normals
# ===========================================================================
def lesson_tangents_normals():
    return {
        "slug": "tangents-and-normals",
        "title": "Tangents and Normals",
        "concreteComparison": (
            "A stone whirled on a string and released flies off along the TANGENT — the "
            "direction it was travelling at the instant the string broke. The string itself, "
            "pointing back to the centre, lies along the NORMAL. Both lines are there in every "
            "curve, at every point."
        ),
        "objective": (
            "Find the equation of the tangent and of the normal to a curve at a given point."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.4.** Tangents and normals at a given point, and their "
            "equations. **Papers 1 and 2.** The technique is Topic 2's straight lines, with the "
            "gradient supplied by calculus.",
            "The recipe is fixed. Differentiate to get $f'(x)$; substitute the $x$-value to get "
            "the tangent's gradient $m$; find the $y$-value by substituting into $f$ (not into "
            "$f'$); then write $y - y_1 = m(x - x_1)$.",
            "The NORMAL is perpendicular to the tangent at the same point, so its gradient is "
            "$-\\dfrac{1}{m}$ — the negative reciprocal from AI SL 2.1. Same point, same "
            "formula, different gradient. If the tangent happens to be horizontal, the normal is "
            "vertical and is written $x = x_1$.",
            "The commonest error is a mix-up of the two substitutions: $f'(a)$ gives the "
            "GRADIENT at $x = a$ and $f(a)$ gives the $y$-COORDINATE. Using $f'(a)$ as the "
            "$y$-value produces a line with the right slope through the wrong point, which "
            "usually keeps the method mark and loses everything else."
        ],
        "keyIdea": (
            "Gradient from $f'$, point from $f$, then $y - y_1 = m(x - x_1)$. The normal reuses "
            "the point with gradient $-1/m$."
        ),
        "facts": [
            {
                "title": "Tangent at $x = a$",
                "latex": "m = f'(a), \\quad y_1 = f(a), \\quad y - y_1 = m(x - x_1)",
                "explanation": "Two different substitutions — one into $f'$, one into $f$.",
            },
            {
                "title": "Normal at the same point",
                "latex": "m_{\\text{normal}} = -\\frac{1}{f'(a)}",
                "explanation": "Perpendicular, so the negative reciprocal (AI SL 2.1).",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-54-we1",
                "statement": (
                    "The curve is $y = x^{3} - 4x + 1$.  \n"
                    "**(a)** Find the coordinates of the point where $x = 2$. **[2]**  \n"
                    "**(b)** Find the equation of the tangent at that point. **[3]**  \n"
                    "**(c)** Find the equation of the normal at that point. **[3]**"
                ),
                "solution": (
                    "**(a)** $y = 8 - 8 + 1 = 1$, so the point is $(2, 1)$ *(M1 A1)*.  \n"
                    "**(b)** $\\dfrac{dy}{dx} = 3x^{2} - 4$ *(A1)*, so at $x = 2$ the gradient "
                    "is $12 - 4 = 8$ *(M1)*. The tangent is $y - 1 = 8(x - 2)$, i.e. "
                    "$y = 8x - 15$ *(A1)*.  \n"
                    "**(c)** Normal gradient $= -\\dfrac{1}{8}$ *(A1)*. Through $(2, 1)$: "
                    "$y - 1 = -\\dfrac{1}{8}(x - 2)$ *(M1)*, i.e. "
                    "$y = -\\dfrac{1}{8}x + \\dfrac{5}{4}$ *(A1)*.  \n"
                    "**Narrative:** notice that the point comes from $f$ and the gradient from "
                    "$f'$ — the two substitutions are into different functions and both use "
                    "$x = 2$. A quick check: both lines must pass through $(2, 1)$, and "
                    "$8(2) - 15 = 1$ ✓ while $-\\frac{2}{8} + \\frac{5}{4} = 1$ ✓."
                ),
                "check": [
                    "2**3 - 4*2 + 1 == 1",
                    "diff(x**3 - 4*x + 1, x) == 3*x**2 - 4",
                    "3*2**2 - 4 == 8",
                    "8*2 - 15 == 1",
                    "8*Rational(-1, 8) == -1",
                    "Rational(-1, 8)*2 + Rational(5, 4) == 1",
                ],
            },
            {
                "id": "aisl-54-we2",
                "statement": (
                    "The curve is $y = \\dfrac{12}{x}$ for $x > 0$.  \n"
                    "**(a)** Find $\\dfrac{dy}{dx}$. **[2]**  \n"
                    "**(b)** Find the equation of the tangent at $x = 3$. **[4]**  \n"
                    "**(c)** Find where this tangent crosses the $x$-axis. **[2]**"
                ),
                "solution": (
                    "**(a)** Rewrite as $y = 12x^{-1}$ *(M1)*, so "
                    "$\\dfrac{dy}{dx} = -12x^{-2} = -\\dfrac{12}{x^{2}}$ *(A1)*.  \n"
                    "**(b)** At $x = 3$: $y = 4$ and the gradient is "
                    "$-\\dfrac{12}{9} = -\\dfrac{4}{3}$ *(M1 A1)*. The tangent is "
                    "$y - 4 = -\\dfrac{4}{3}(x - 3)$ *(M1)*, i.e. "
                    "$y = -\\dfrac{4}{3}x + 8$ *(A1)*.  \n"
                    "**(c)** Setting $y = 0$: $\\dfrac{4}{3}x = 8$ *(M1)*, so "
                    "$x = 6$ *(A1)*.  \n"
                    "**Narrative:** the negative gradient is the honest report of a curve that "
                    "falls everywhere for $x > 0$ — as $x$ doubles, $y$ halves. There is a tidy "
                    "fact hiding in (c): the tangent to $y = \\frac{k}{x}$ at $x = a$ always "
                    "crosses the $x$-axis at $2a$, and here $2 \\times 3 = 6$."
                ),
                "check": [
                    "diff(12/x, x) == -12/x**2",
                    "Rational(12, 3) == 4",
                    "Rational(-12, 9) == Rational(-4, 3)",
                    "Rational(-4, 3)*3 + 8 == 4",
                    "Rational(-4, 3)*6 + 8 == 0",
                    "6 == 2*3",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using $f'(a)$ as the $y$-coordinate of the point.",
                "correction": "The point is $(a, f(a))$; the gradient is $f'(a)$. Two substitutions, two different functions.",
                "authored": True,
            },
            {
                "text": "Using the tangent's gradient for the normal.",
                "correction": "The normal is perpendicular: take the negative reciprocal. Flip AND change the sign.",
                "authored": True,
            },
            {
                "text": "Differentiating $\\frac{12}{x}$ as $\\frac{12}{1} = 12$.",
                "correction": "Rewrite as $12x^{-1}$ and apply the power rule, giving $-12x^{-2}$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-54-t1",
                "statement": (
                    "Find the equation of the tangent to $y = x^{2} - 3x$ at the point where "
                    "$x = 4$. **[4]**"
                ),
                "solution": (
                    "$y = 16 - 12 = 4$, so the point is $(4, 4)$ *(A1)*.  \n"
                    "$\\dfrac{dy}{dx} = 2x - 3$, so the gradient is $5$ *(M1 A1)*.  \n"
                    "$y - 4 = 5(x - 4)$, i.e. $y = 5x - 16$ *(A1)*."
                ),
                "check": [
                    "4**2 - 3*4 == 4",
                    "diff(x**2 - 3*x, x) == 2*x - 3",
                    "2*4 - 3 == 5",
                    "5*4 - 16 == 4",
                ],
            },
            {
                "id": "aisl-54-t2",
                "statement": (
                    "Find the equation of the normal to $y = x^{2} + 1$ at the point "
                    "$(1, 2)$. **[4]**"
                ),
                "solution": (
                    "$\\dfrac{dy}{dx} = 2x$, so the tangent's gradient at $x = 1$ is $2$ "
                    "*(M1 A1)*.  \n"
                    "The normal's gradient is $-\\dfrac{1}{2}$ *(A1)*, giving "
                    "$y - 2 = -\\dfrac{1}{2}(x - 1)$, i.e. "
                    "$y = -\\dfrac{1}{2}x + \\dfrac{5}{2}$ *(A1)*."
                ),
                "check": [
                    "diff(x**2 + 1, x) == 2*x",
                    "2*1 == 2",
                    "2*Rational(-1, 2) == -1",
                    "Rational(-1, 2)*1 + Rational(5, 2) == 2",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.4 · Papers 1 & 2",
                    "title": "Calculus supplies the gradient, algebra does the rest",
                    "body": (
                        "This code is Topic 2's straight-line work with one new ingredient: the "
                        "gradient now comes from a derivative instead of from two points. "
                        "Everything after that — point-gradient form, negative reciprocals — you "
                        "already know."
                    ),
                },
                {
                    "kind": "tangentGraph",
                    "eyebrow": "Play",
                    "title": "One point, one tangent",
                    "teach": (
                        "Slide the point of tangency along the curve and watch the touching line "
                        "reorient. There is exactly one tangent at each point, and its gradient "
                        "is the number the derivative returns for that $x$."
                    ),
                    "config": {"mode": "tangent"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Four steps, in order",
                    "beats": [
                        "Differentiate to get $f'(x)$.",
                        "Substitute into $f'$ for the gradient; into $f$ for the $y$-coordinate.",
                        "Tangent: $y - y_1 = m(x - x_1)$.",
                        "Normal: same point, gradient $-1/m$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Tangent and normal to a cubic",
                    "problemId": "aisl-54-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Which substitution?",
                    "title": "Point or gradient?",
                    "prompt": (
                        "For $f(x) = x^{2}$, the tangent at $x = 3$ passes through the point"
                    ),
                    "options": [
                        "$(3, 9)$",
                        "$(3, 6)$",
                        "$(9, 3)$",
                        "$(6, 3)$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The $y$-coordinate comes from $f(3) = 9$. The value $6$ is "
                        "$f'(3)$ — the GRADIENT there, not a coordinate."
                    ),
                    "check": [
                        "3**2 == 9",
                        "diff(x**2, x).subs(x, 3) == 6",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A reciprocal curve and its tangent",
                    "problemId": "aisl-54-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Perpendicular",
                    "title": "The normal's gradient",
                    "prompt": (
                        "A tangent has gradient $\\frac{2}{5}$. The normal at that point has "
                        "gradient"
                    ),
                    "options": [
                        "$-\\frac{5}{2}$",
                        "$\\frac{5}{2}$",
                        "$-\\frac{2}{5}$",
                        "$\\frac{2}{5}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Flip and negate: $-\\frac{5}{2}$. Check the product: "
                        "$\\frac{2}{5} \\times -\\frac{5}{2} = -1$, which is what perpendicular "
                        "means."
                    ),
                    "check": [
                        "Rational(2, 5)*Rational(-5, 2) == -1",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Check the point satisfies your line",
                    "body": (
                        "Substitute $x_1$ back into your finished equation — it must return "
                        "$y_1$. It takes five seconds, it catches sign slips in the "
                        "point-gradient expansion, and it works for the normal too."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-54-t1"},
                {"kind": "tryIt", "problemId": "aisl-54-t2"},
                {
                    "kind": "recap",
                    "title": "Tangents and normals, compressed",
                    "points": [
                        "Gradient from $f'(a)$, point from $(a, f(a))$.",
                        "$y - y_1 = m(x - x_1)$ for both lines.",
                        "Normal gradient is $-1/m$.",
                        "Verify by substituting the point back in.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — AI SL 5.6: stationary points
# ===========================================================================
def lesson_stationary_points():
    return {
        "slug": "stationary-points",
        "title": "Stationary Points: Maxima and Minima",
        "concreteComparison": (
            "Walk over a hill and there is one step where you are neither climbing nor "
            "descending — the summit. Walk through a valley and there is one where you are "
            "neither descending nor climbing — the floor. Both are places where the slope is "
            "zero, and telling them apart is what this lesson is for."
        ),
        "objective": (
            "Solve $f'(x) = 0$ to locate stationary points and classify them as local maxima or "
            "local minima."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.6.** Values of $x$ where the gradient of a curve is "
            "zero; solution of $f'(x) = 0$; local maximum and minimum points. **Papers 1 and "
            "2.**",
            "A stationary point is where $f'(x) = 0$ — the tangent is horizontal. Finding them "
            "is mechanical: differentiate, set to zero, solve. A quadratic $f'$ gives at most "
            "two, and factorising it is usually faster than the quadratic formula.",
            "CLASSIFYING them is the assessed part. Test the sign of $f'$ just before and just "
            "after the point. Positive then negative is a local MAXIMUM (rising then falling); "
            "negative then positive is a local MINIMUM. No sign change means a point of "
            "inflexion, where the curve flattens and carries on the same way.",
            "AI does not use the second derivative for this — that belongs to the Higher Level "
            "course. The sign test is the expected method, and a small table with the test "
            "points, the values of $f'$ and the resulting shape is what earns the marks.",
            "'Local' matters. A local maximum is the highest point in its neighbourhood, not "
            "necessarily on the whole domain. On a closed interval the GLOBAL maximum may sit at "
            "an endpoint instead, so a question that restricts the domain expects you to compare "
            "the stationary values with the endpoint values."
        ],
        "keyIdea": (
            "Solve $f'(x) = 0$ to find them, then test the sign of $f'$ on either side to "
            "classify them. Check the endpoints too when the domain is closed."
        ),
        "facts": [
            {
                "title": "Stationary points",
                "latex": "f'(x) = 0",
                "explanation": "The defining condition — the tangent is horizontal there.",
            },
            {
                "title": "The sign test",
                "latex": "+ \\to - \\;\\Rightarrow\\; \\text{maximum} \\qquad - \\to + \\;\\Rightarrow\\; \\text{minimum}",
                "explanation": "AI's expected classification method; the second derivative is HL.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-56-we1",
                "statement": (
                    "Consider $f(x) = 2x^{3} - 9x^{2} + 12x + 1$.  \n"
                    "**(a)** Find $f'(x)$ and solve $f'(x) = 0$. **[4]**  \n"
                    "**(b)** Find the coordinates of both stationary points. **[2]**  \n"
                    "**(c)** Classify each, showing your reasoning. **[4]**"
                ),
                "solution": (
                    "**(a)** $f'(x) = 6x^{2} - 18x + 12$ *(A1)* $= 6(x - 1)(x - 2)$ *(M1 A1)*, "
                    "so $x = 1$ or $x = 2$ *(A1)*.  \n"
                    "**(b)** $f(1) = 2 - 9 + 12 + 1 = 6$ and "
                    "$f(2) = 16 - 36 + 24 + 1 = 5$, giving $(1, 6)$ and $(2, 5)$ *(A1 A1)*.  \n"
                    "**(c)** $f'(0) = 12 > 0$, $f'(1.5) = -1.5 < 0$, $f'(3) = 12 > 0$ "
                    "*(M1 A1)*. The sign runs $+ \\to -$ at $x = 1$, so $(1, 6)$ is a local "
                    "MAXIMUM *(A1)*; it runs $- \\to +$ at $x = 2$, so $(2, 5)$ is a local "
                    "MINIMUM *(A1)*.  \n"
                    "**Narrative:** the local maximum $6$ is barely above the local minimum "
                    "$5$ — a shallow dip, not a dramatic one — and that is a useful reminder "
                    "that 'maximum' is a LOCAL claim. Far to the right this cubic rises well "
                    "above $6$; $(1, 6)$ is only the highest point in its own neighbourhood."
                ),
                "check": [
                    "diff(2*x**3 - 9*x**2 + 12*x + 1, x) == 6*x**2 - 18*x + 12",
                    "expand(6*(x - 1)*(x - 2)) == 6*x**2 - 18*x + 12",
                    "2*1 - 9 + 12 + 1 == 6",
                    "2*8 - 9*4 + 24 + 1 == 5",
                    "6*0**2 - 18*0 + 12 == 12",
                    "6*Rational(3, 2)**2 - 18*Rational(3, 2) + 12 == Rational(-3, 2)",
                    "6*3**2 - 18*3 + 12 == 12",
                ],
            },
            {
                "id": "aisl-56-we2",
                "statement": (
                    "A bacterial count, in thousands, is modelled by "
                    "$N(t) = t^{3} - 12t^{2} + 36t + 10$ for $0 \\le t \\le 8$ hours.  \n"
                    "**(a)** Find the times at which the count is stationary. **[3]**  \n"
                    "**(b)** Find the count at each stationary time and at each endpoint. "
                    "**[4]**  \n"
                    "**(c)** State the greatest and least counts over the eight hours. **[3]**"
                ),
                "solution": (
                    "**(a)** $N'(t) = 3t^{2} - 24t + 36 = 3(t - 2)(t - 6)$ *(M1 A1)*, so "
                    "$t = 2$ and $t = 6$ *(A1)*.  \n"
                    "**(b)** $N(2) = 8 - 48 + 72 + 10 = 42$; "
                    "$N(6) = 216 - 432 + 216 + 10 = 10$ *(A1 A1)*. At the endpoints "
                    "$N(0) = 10$ and $N(8) = 512 - 768 + 288 + 10 = 42$ *(A1 A1)*.  \n"
                    "**(c)** The greatest count is $42$ thousand, reached at both $t = 2$ and "
                    "$t = 8$ *(A1 A1)*; the least is $10$ thousand, at both $t = 0$ and "
                    "$t = 6$ *(A1)*.  \n"
                    "**Narrative:** this is exactly why a closed domain changes the question. "
                    "The local maximum at $t = 2$ is matched by the ENDPOINT value at $t = 8$, "
                    "and the local minimum at $t = 6$ is matched by the endpoint at $t = 0$ — so "
                    "an answer that considered only the stationary points would still be right "
                    "here by luck, and wrong on a domain of $0 \\le t \\le 9$."
                ),
                "check": [
                    "diff(t**3 - 12*t**2 + 36*t + 10, t) == 3*t**2 - 24*t + 36",
                    "expand(3*(t - 2)*(t - 6)) == 3*t**2 - 24*t + 36",
                    "8 - 48 + 72 + 10 == 42",
                    "216 - 432 + 216 + 10 == 10",
                    "0 - 0 + 0 + 10 == 10",
                    "512 - 768 + 288 + 10 == 42",
                    "9**3 - 12*9**2 + 36*9 + 10 == 91",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Solving $f(x) = 0$ instead of $f'(x) = 0$.",
                "correction": "Stationary points are where the GRADIENT vanishes. Solving $f = 0$ gives the $x$-intercepts, a different feature entirely.",
                "authored": True,
            },
            {
                "text": "Naming a stationary point without classifying it.",
                "correction": "Test the sign of $f'$ on both sides and say which it is. The classification is usually worth as much as the location.",
                "authored": True,
            },
            {
                "text": "Ignoring the endpoints on a closed domain.",
                "correction": "The greatest value on $a \\le x \\le b$ may sit at $a$ or $b$. Compare the stationary values with both endpoint values.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-56-t1",
                "statement": (
                    "Find and classify the stationary points of $y = x^{3} - 3x$. **[5]**"
                ),
                "solution": (
                    "$\\dfrac{dy}{dx} = 3x^{2} - 3 = 0$ gives $x = \\pm 1$ *(M1 A1)*.  \n"
                    "$y(-1) = 2$ and $y(1) = -2$ *(A1)*.  \n"
                    "The gradient at $x = -2$ is $9 > 0$ and at $x = 0$ is $-3 < 0$, so "
                    "$(-1, 2)$ is a maximum *(A1)*; at $x = 2$ it is $9 > 0$, so $(1, -2)$ is a "
                    "minimum *(A1)*."
                ),
                "check": [
                    "diff(x**3 - 3*x, x) == 3*x**2 - 3",
                    "solve(3*x**2 - 3, x) == [-1, 1]",
                    "(-1)**3 - 3*(-1) == 2",
                    "1 - 3 == -2",
                    "3*(-2)**2 - 3 == 9",
                    "3*0**2 - 3 == -3",
                ],
            },
            {
                "id": "aisl-56-t2",
                "statement": (
                    "For $f(x) = x + \\dfrac{4}{x}$ with $x > 0$, find the stationary point and "
                    "classify it. **[5]**"
                ),
                "solution": (
                    "$f(x) = x + 4x^{-1}$, so $f'(x) = 1 - 4x^{-2}$ *(M1 A1)*.  \n"
                    "$1 - \\dfrac{4}{x^{2}} = 0$ gives $x^{2} = 4$, and $x > 0$ so $x = 2$ "
                    "*(A1)*, where $f(2) = 4$ *(A1)*.  \n"
                    "$f'(1) = -3 < 0$ and $f'(3) = \\frac{5}{9} > 0$, so $(2, 4)$ is a local "
                    "MINIMUM *(A1)*."
                ),
                "check": [
                    "diff(x + 4/x, x) == 1 - 4/x**2",
                    "2 + Rational(4, 2) == 4",
                    "1 - Rational(4, 1) == -3",
                    "1 - Rational(4, 9) == Rational(5, 9)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.6 · Papers 1 & 2",
                    "title": "Find them, then tell them apart",
                    "body": (
                        "Locating a stationary point is one line of algebra. Deciding whether it "
                        "is a peak or a trough is the part that carries marks — and on this "
                        "course the tool for it is the sign of $f'$ either side, nothing more "
                        "advanced."
                    ),
                },
                {
                    "kind": "polyGraph",
                    "eyebrow": "Play",
                    "title": "Two turning points on a cubic",
                    "teach": (
                        "Move a zero and watch the two turning points slide with it. A cubic has "
                        "at most two — the derivative is a quadratic, and a quadratic has at "
                        "most two roots. The degrees of $f$ and $f'$ set the shape's budget."
                    ),
                    "config": {"mode": "zeros", "zeros": [-1, 1, 3]},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Locate, evaluate, classify",
                    "beats": [
                        "Differentiate and solve $f'(x) = 0$ — factorise where you can.",
                        "Substitute back into $f$ for the $y$-coordinates.",
                        "Test $f'$ just left and just right of each point.",
                        "$+ \\to -$ maximum, $- \\to +$ minimum; on a closed domain, check the endpoints.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two stationary points, classified",
                    "problemId": "aisl-56-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Classify it",
                    "title": "Read the sign change",
                    "prompt": (
                        "At a stationary point, $f'$ changes from negative to positive. The "
                        "point is a"
                    ),
                    "options": [
                        "local minimum",
                        "local maximum",
                        "point of inflexion",
                        "root of $f$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Falling, then level, then rising — the bottom of a valley. "
                        "Positive-to-negative would be the top of a hill; no change at all would "
                        "be a point of inflexion."
                    ),
                    "check": [
                        "3*0**2 - 3 < 0",
                        "3*2**2 - 3 > 0",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A closed domain, and its endpoints",
                    "problemId": "aisl-56-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Which equation?",
                    "title": "What do you set to zero?",
                    "prompt": "To find the turning points of $y = f(x)$ you solve",
                    "options": [
                        "$f'(x) = 0$",
                        "$f(x) = 0$",
                        "$f(x) = f'(x)$",
                        "$f'(x) = 1$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The tangent is horizontal at a turning point, so the GRADIENT is zero. "
                        "Solving $f(x) = 0$ finds where the curve meets the $x$-axis — a "
                        "different question with a different answer."
                    ),
                    "check": [
                        "solve(3*x**2 - 3, x) == [-1, 1]",
                        "solve(x**3 - 3*x, x) != [-1, 1]",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Show the sign table",
                    "body": (
                        "Three columns — a test value below, the stationary point, a test value "
                        "above — with the sign of $f'$ in each. It is compact, it is exactly "
                        "what the classification marks are for, and it survives an arithmetic "
                        "slip elsewhere."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-56-t1"},
                {"kind": "tryIt", "problemId": "aisl-56-t2"},
                {
                    "kind": "recap",
                    "title": "Stationary points, compressed",
                    "points": [
                        "Solve $f'(x) = 0$; substitute back into $f$ for the coordinates.",
                        "$+ \\to -$ is a maximum, $- \\to +$ a minimum, no change an inflexion.",
                        "AI classifies by sign, not by the second derivative.",
                        "On a closed domain the extremes may be at the endpoints.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — AI SL 5.7: optimisation
# ===========================================================================
def lesson_optimisation():
    return {
        "slug": "optimisation",
        "title": "Optimisation in Context",
        "concreteComparison": (
            "A drinks can holds a fixed volume, and the manufacturer wants to spend as little "
            "aluminium as possible on it. Too tall and thin, too much side; too short and wide, "
            "too much top and bottom. Somewhere between is a shape that costs least — and "
            "calculus finds it exactly."
        ),
        "objective": (
            "Turn a context into a single-variable function, differentiate it, and find and "
            "justify the optimal value."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.7.** Optimisation problems in context. **Papers 1 and "
            "2.** Every one is Lesson 5.6 preceded by modelling — and the modelling is where the "
            "marks are.",
            "The routine never varies. Write the quantity to be optimised. Write the CONSTRAINT "
            "connecting the variables. Use the constraint to eliminate one variable so the "
            "quantity depends on ONE unknown. Differentiate, set to zero, solve, and justify "
            "that you have the right kind of stationary point.",
            "Eliminating the second variable is the step that separates candidates. A pen "
            "against a wall with $60$ m of fence has constraint $x + 2y = 60$; a can of volume "
            "$1000$ has constraint $\\pi r^{2}h = 1000$. Rearrange the constraint, substitute, "
            "and only then differentiate — differentiating a two-variable expression is not "
            "possible on this course.",
            "JUSTIFY the answer. A stationary point alone does not prove you have found the "
            "maximum: say the sign of the derivative changes from positive to negative, or that "
            "the graph of the function shows a single peak on the domain. Questions award a mark "
            "for this and it is routinely dropped.",
            "Finish in context. If the question asks for the dimensions, give lengths with "
            "units; if it asks for the minimum cost, give money. An answer of '$x = 15$' to a "
            "question about the largest possible area has stopped one line early."
        ],
        "keyIdea": (
            "One quantity, one constraint, one variable. Then differentiate, solve, justify, and "
            "answer the question that was asked."
        ),
        "facts": [
            {
                "title": "The optimisation routine",
                "latex": "\\text{quantity} \\;+\\; \\text{constraint} \\;\\Rightarrow\\; \\text{one variable} \\;\\Rightarrow\\; \\frac{dQ}{dx} = 0",
                "explanation": "Not a formula — the structure every one of these questions has.",
            },
            {
                "title": "Justification",
                "latex": "\\frac{dQ}{dx} > 0 \\text{ before}, \\; < 0 \\text{ after} \\;\\Rightarrow\\; \\text{maximum}",
                "explanation": "State it explicitly; it carries its own mark.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-57-we1",
                "statement": (
                    "A rectangular pen is built against a straight wall, using $60$ m of fencing "
                    "for the other three sides. Let the two sides perpendicular to the wall each "
                    "have length $y$ m and the side parallel to it have length $x$ m.  \n"
                    "**(a)** Write down the constraint and use it to express the area $A$ in "
                    "terms of $y$ alone. **[3]**  \n"
                    "**(b)** Find the value of $y$ that maximises $A$, justifying that it is a "
                    "maximum. **[4]**  \n"
                    "**(c)** State the dimensions and the maximum area. **[3]**"
                ),
                "solution": (
                    "**(a)** The constraint is $x + 2y = 60$ *(A1)*, so $x = 60 - 2y$ *(A1)* "
                    "and $A = xy = 60y - 2y^{2}$ *(A1)*.  \n"
                    "**(b)** $\\dfrac{dA}{dy} = 60 - 4y$ *(A1)*, which is zero at "
                    "$y = 15$ *(M1 A1)*. Since $\\frac{dA}{dy} > 0$ for $y < 15$ and $< 0$ for "
                    "$y > 15$, this is a maximum *(R1)*.  \n"
                    "**(c)** Then $x = 60 - 30 = 30$ m *(A1)*, so the pen is $30$ m by $15$ m "
                    "*(A1)* with area $450$ m$^{2}$ *(A1)*.  \n"
                    "**Narrative:** the wall is doing real work — it removes one side from the "
                    "fencing budget, which is why the optimal pen is twice as wide as it is "
                    "deep rather than square. With all four sides fenced the answer would be a "
                    "$15$ by $15$ square, and comparing the two is a good check that you used "
                    "the right constraint."
                ),
                "check": [
                    "60 - 2*15 == 30",
                    "expand((60 - 2*y)*y) == 60*y - 2*y**2",
                    "diff(60*y - 2*y**2, y) == 60 - 4*y",
                    "solve(60 - 4*y, y) == [15]",
                    "60 - 4*10 > 0",
                    "60 - 4*20 < 0",
                    "30*15 == 450",
                ],
            },
            {
                "id": "aisl-57-we2",
                "statement": (
                    "A closed cylindrical can must hold $1000$ cm$^{3}$. Its surface area is "
                    "$S = 2\\pi r^{2} + 2\\pi r h$.  \n"
                    "**(a)** Show that $S = 2\\pi r^{2} + \\dfrac{2000}{r}$. **[3]**  \n"
                    "**(b)** Find the radius that minimises $S$, to 3 s.f. **[4]**  \n"
                    "**(c)** Find the corresponding height and the minimum surface area, to "
                    "3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** The constraint is $\\pi r^{2}h = 1000$ *(A1)*, so "
                    "$h = \\dfrac{1000}{\\pi r^{2}}$ *(A1)*. Substituting: "
                    "$2\\pi r h = 2\\pi r \\cdot \\dfrac{1000}{\\pi r^{2}} = "
                    "\\dfrac{2000}{r}$ *(AG)* *(A1)*.  \n"
                    "**(b)** $\\dfrac{dS}{dr} = 4\\pi r - \\dfrac{2000}{r^{2}}$ *(A1)*. "
                    "Setting this to zero *(M1)*: $4\\pi r^{3} = 2000$, so "
                    "$r^{3} = \\dfrac{500}{\\pi}$ *(A1)* and $r = 5.42$ cm *(A1)*.  \n"
                    "**(c)** $h = \\dfrac{1000}{\\pi (5.419)^{2}} = 10.8$ cm *(A1)*, and "
                    "$S = 554$ cm$^{2}$ *(M1 A1)*.  \n"
                    "**Narrative:** the answer has a memorable shape: $h = 10.84$ is exactly "
                    "twice $r = 5.42$. The cheapest closed cylinder is always as tall as it is "
                    "wide — its height equals its diameter — which is a result worth recognising "
                    "and a strong check that the algebra survived. (Real drink cans are taller "
                    "and thinner than this, because they are also designed to be held.)"
                ),
                "check": [
                    "simplify(2*pi*r*(1000/(pi*r**2))) == 2000/r",
                    "diff(2*pi*r**2 + 2000/r, r) == 4*pi*r - 2000/r**2",
                    "Abs((500/pi)**Rational(1, 3) - Rational(542, 100)) < Rational(5, 1000)",
                    "Abs(1000/(pi*((500/pi)**Rational(1, 3))**2) - Rational(108, 10)) < Rational(5, 100)",
                    "Abs(2*pi*((500/pi)**Rational(1, 3))**2 + 2000/((500/pi)**Rational(1, 3)) - 554) < 1",
                    "Abs(1000/(pi*((500/pi)**Rational(1, 3))**2) - 2*(500/pi)**Rational(1, 3)) < Rational(1, 1000)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Differentiating an expression that still contains two variables.",
                "correction": "Use the constraint to eliminate one first. There is nothing to differentiate until the quantity depends on a single unknown.",
                "authored": True,
            },
            {
                "text": "Stopping at the value of $x$ that was optimised.",
                "correction": "Answer the question. If it asks for the maximum area or the minimum cost, substitute back and give that number, with units.",
                "authored": True,
            },
            {
                "text": "Not justifying that the stationary point is the maximum.",
                "correction": "Say why — the sign of the derivative changes from positive to negative, or the graph has a single peak. It is a mark on its own.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-57-t1",
                "statement": (
                    "An open-topped box has a square base of side $x$ cm and volume $32$ "
                    "cm$^{3}$. Find the value of $x$ that minimises the surface area, and that "
                    "minimum area. **[6]**"
                ),
                "solution": (
                    "Height $h = \\dfrac{32}{x^{2}}$ *(A1)*, so "
                    "$S = x^{2} + 4xh = x^{2} + \\dfrac{128}{x}$ *(M1 A1)*.  \n"
                    "$\\dfrac{dS}{dx} = 2x - \\dfrac{128}{x^{2}} = 0$ gives $x^{3} = 64$, so "
                    "$x = 4$ cm *(M1 A1)*.  \n"
                    "Then $h = 2$ cm and $S = 16 + 32 = 48$ cm$^{2}$ *(A1)*."
                ),
                "check": [
                    "Eq(simplify(x**2 + 4*x*(32/x**2) - x**2 - 128/x), 0)",
                    "diff(x**2 + 128/x, x) == 2*x - 128/x**2",
                    "4**3 == 64",
                    "Rational(32, 16) == 2",
                    "4**2 + Rational(128, 4) == 48",
                ],
            },
            {
                "id": "aisl-57-t2",
                "statement": (
                    "A rectangle has perimeter $200$ m. Find the dimensions that maximise its "
                    "area. **[4]**"
                ),
                "solution": (
                    "If the width is $x$ then the height is $100 - x$ *(A1)*, so "
                    "$A = x(100 - x) = 100x - x^{2}$ *(A1)*.  \n"
                    "$\\dfrac{dA}{dx} = 100 - 2x = 0$ gives $x = 50$ *(M1)*, so the rectangle "
                    "is a $50$ m square with area $2500$ m$^{2}$ *(A1)*."
                ),
                "check": [
                    "expand(x*(100 - x)) == 100*x - x**2",
                    "diff(100*x - x**2, x) == 100 - 2*x",
                    "solve(100 - 2*x, x) == [50]",
                    "50*50 == 2500",
                    "2*(50 + 50) == 200",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.7 · Papers 1 & 2",
                    "title": "The calculus is the easy half",
                    "body": (
                        "Every optimisation question ends with the same two lines — "
                        "differentiate, set to zero — and begins with the hard part: turning a "
                        "situation into one function of one variable. That translation is where "
                        "the marks are, and where the work is."
                    ),
                },
                {
                    "kind": "parabolaGraph",
                    "eyebrow": "Play",
                    "title": "The single peak",
                    "teach": (
                        "Most SL optimisation problems reduce to a quadratic, and a downward "
                        "quadratic has exactly one peak. Move $b$ and $c$ and watch the vertex "
                        "travel — that vertex is the answer the derivative is hunting for."
                    ),
                    "config": {"mode": "standard", "b": 4, "c": -1, "interactive": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Five steps, every time",
                    "beats": [
                        "Name the variables and write the quantity to optimise.",
                        "Write the constraint that links them.",
                        "Substitute so the quantity depends on ONE variable.",
                        "Differentiate, set to zero, solve.",
                        "Justify it is a max or min, then answer in context with units.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A pen against a wall",
                    "problemId": "aisl-57-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The constraint",
                    "title": "Which equation eliminates a variable?",
                    "prompt": (
                        "A box with square base $x$ and height $h$ has volume $500$. To write "
                        "the surface area in terms of $x$ alone, substitute"
                    ),
                    "options": [
                        "$h = \\frac{500}{x^{2}}$",
                        "$h = 500 - x^{2}$",
                        "$x = \\frac{500}{h}$",
                        "$h = \\frac{x^{2}}{500}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The constraint is $x^{2}h = 500$, so $h = \\frac{500}{x^{2}}$. "
                        "Substituting that into the surface-area expression leaves a function of "
                        "$x$ alone, which is the only kind you can differentiate here."
                    ),
                    "check": [
                        "Eq(x**2*(500/x**2), 500)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "The cheapest can",
                    "problemId": "aisl-57-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Justify it",
                    "title": "Why is it a maximum?",
                    "prompt": (
                        "You have found $\\frac{dA}{dx} = 0$ at $x = 8$. The best justification "
                        "that this gives a maximum is"
                    ),
                    "options": [
                        "$\\frac{dA}{dx} > 0$ before $x = 8$ and $< 0$ after",
                        "$A(8)$ is a large number",
                        "the question asked for a maximum",
                        "$x = 8$ is in the middle of the domain",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The sign change from rising to falling is what makes a stationary point "
                        "a peak. The size of $A(8)$ says nothing on its own, and the question's "
                        "wording is not evidence."
                    ),
                    "check": [
                        "60 - 4*10 > 0",
                        "60 - 4*20 < 0",
                    ],
                },
                {"kind": "tryIt", "problemId": "aisl-57-t1"},
                {"kind": "tryIt", "problemId": "aisl-57-t2"},
                {
                    "kind": "recap",
                    "title": "Optimisation, compressed",
                    "points": [
                        "Quantity, constraint, substitute — one variable before differentiating.",
                        "Differentiate, set to zero, solve.",
                        "Justify with the sign change; it is its own mark.",
                        "Answer the question asked, with units.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 7 — AI SL 5.5: integration
# ===========================================================================
def lesson_integration():
    return {
        "slug": "integration-and-area",
        "title": "Integration: Undoing the Derivative, and Area",
        "concreteComparison": (
            "A car's speedometer records speed; multiply speed by time and you get distance. "
            "When the speed keeps changing, that multiplication becomes an integral — and on a "
            "speed-time graph it is literally the area under the curve."
        ),
        "objective": (
            "Integrate polynomials, use a boundary condition to find the constant, and compute "
            "definite integrals and areas under curves."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.5.** Introduction to integration as anti-differentiation "
            "of functions of the form $f(x) = ax^{n} + bx^{n-1} + \\ldots$ where "
            "$n \\in \\mathbb{Z}$, $n \\ne -1$; anti-differentiation with a boundary condition "
            "to determine the constant term; definite integrals using technology; the area of a "
            "region enclosed by a curve $y = f(x)$ and the $x$-axis where $f(x) > 0$. **Papers 1 "
            "and 2.**",
            "Integration undoes differentiation, so the power rule runs backwards: ADD one to "
            "the power, then divide by the new power. "
            "$\\displaystyle\\int ax^{n}\\,dx = \\dfrac{ax^{n+1}}{n+1} + C$, and the exclusion "
            "$n \\ne -1$ is there because that rule would divide by zero.",
            "The $+C$ is not decoration. Every constant differentiates to zero, so infinitely "
            "many functions share one derivative — an indefinite integral is a whole family of "
            "parallel curves. Omitting $C$ loses a mark on sight.",
            "A BOUNDARY CONDITION picks one member of that family. Given "
            "$\\frac{dy}{dx} = 6x$ and the fact that the curve passes through $(1, 5)$: "
            "integrate to $y = 3x^{2} + C$, substitute the point to get $3 + C = 5$, so "
            "$C = 2$. Integrate first, substitute second — never the other way round.",
            "A DEFINITE integral has limits and produces a number: "
            "$\\int_a^b f(x)\\,dx = F(b) - F(a)$, with no constant, since the $C$s cancel. Where "
            "$f(x) > 0$ that number is the AREA between the curve and the $x$-axis from $a$ to "
            "$b$ — and on this course you may find it by hand or straight from the GDC."
        ],
        "keyIdea": (
            "Add one to the power and divide by it. Indefinite integrals need $+C$; definite "
            "ones need limits and give the area when the curve is above the axis."
        ),
        "facts": [
            {
                "title": "The integration rule",
                "latex": "\\int ax^{n}\\,dx = \\frac{ax^{n+1}}{n+1} + C, \\quad n \\ne -1",
                "explanation": "Booklet (AI SL 5.5). The power rule, run backwards.",
            },
            {
                "title": "Definite integral",
                "latex": "\\int_a^b f(x)\\,dx = F(b) - F(a)",
                "explanation": "A number, not a family — the constants cancel.",
            },
            {
                "title": "Area under a curve",
                "latex": "A = \\int_a^b f(x)\\,dx \\quad \\text{where } f(x) > 0 \\text{ on } [a, b]",
                "explanation": "Booklet. The positivity condition matters — below the axis the integral is negative.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-55-we1",
                "statement": (
                    "**(a)** Find $\\displaystyle\\int (6x^{2} - 4x + 3)\\,dx$. **[3]**  \n"
                    "**(b)** A curve has $\\dfrac{dy}{dx} = 6x^{2} - 4x + 3$ and passes through "
                    "$(1, 5)$. Find its equation. **[3]**  \n"
                    "**(c)** Find the value of $y$ when $x = 2$. **[2]**"
                ),
                "solution": (
                    "**(a)** $2x^{3} - 2x^{2} + 3x + C$ *(A1 A1 A1)* — each power raised by one "
                    "and divided by the new power.  \n"
                    "**(b)** Substituting $(1, 5)$: $2 - 2 + 3 + C = 5$ *(M1 A1)*, so "
                    "$C = 2$ and $y = 2x^{3} - 2x^{2} + 3x + 2$ *(A1)*.  \n"
                    "**(c)** $y = 16 - 8 + 6 + 2 = 16$ *(M1 A1)*.  \n"
                    "**Narrative:** part (b) is the boundary condition doing its one job — "
                    "selecting a single curve from the infinite family that (a) describes. The "
                    "check is instant and worth doing: differentiate your answer and you should "
                    "recover $6x^{2} - 4x + 3$, with the $+2$ vanishing exactly as it should."
                ),
                "check": [
                    "diff(2*x**3 - 2*x**2 + 3*x, x) == 6*x**2 - 4*x + 3",
                    "2 - 2 + 3 + 2 == 5",
                    "2*8 - 2*4 + 3*2 + 2 == 16",
                ],
            },
            {
                "id": "aisl-55-we2",
                "statement": (
                    "**(a)** Evaluate $\\displaystyle\\int_0^3 (x^{2} + 1)\\,dx$. **[3]**  \n"
                    "**(b)** Explain what this number represents. **[2]**  \n"
                    "**(c)** Find the area enclosed by $y = 4x - x^{2}$ and the $x$-axis. "
                    "**[4]**"
                ),
                "solution": (
                    "**(a)** $\\left[\\dfrac{x^{3}}{3} + x\\right]_0^3$ *(M1 A1)* "
                    "$= (9 + 3) - 0 = 12$ *(A1)*.  \n"
                    "**(b)** Since $x^{2} + 1 > 0$ throughout, it is the AREA between the curve "
                    "and the $x$-axis from $x = 0$ to $x = 3$ *(A1 A1)*.  \n"
                    "**(c)** The curve meets the axis where $x(4 - x) = 0$, at $x = 0$ and "
                    "$x = 4$ *(M1 A1)*. Then "
                    "$\\displaystyle\\int_0^4 (4x - x^{2})\\,dx = "
                    "\\left[2x^{2} - \\dfrac{x^{3}}{3}\\right]_0^4 = 32 - \\dfrac{64}{3}$ "
                    "*(M1)* $= \\dfrac{32}{3} = 10.7$ *(A1)*.  \n"
                    "**Narrative:** part (c) shows why the limits are usually the first thing to "
                    "find, not the last — 'the area enclosed by the curve and the axis' does not "
                    "state them, so the intercepts have to supply them. Note also that the "
                    "curve is above the axis on the whole of $0 \\le x \\le 4$, which is what "
                    "licenses calling the integral an area at all."
                ),
                "check": [
                    "integrate(x**2 + 1, (x, 0, 3)) == 12",
                    "solve(4*x - x**2, x) == [0, 4]",
                    "integrate(4*x - x**2, (x, 0, 4)) == Rational(32, 3)",
                    "Abs(Rational(32, 3) - Rational(107, 10)) < Rational(5, 100)",
                    "4*2 - 2**2 > 0",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Omitting the $+C$ from an indefinite integral.",
                "correction": "Every constant differentiates to zero, so the answer is a family. The $+C$ is part of the answer and part of the mark.",
                "authored": True,
            },
            {
                "text": "Substituting the boundary point before integrating.",
                "correction": "Integrate first to get the general form, then substitute to find $C$. Substituting into $\\frac{dy}{dx}$ finds a gradient, not a constant.",
                "authored": True,
            },
            {
                "text": "Calling a negative integral an area.",
                "correction": "Below the axis the integral is negative. Area is a positive quantity — this course only asks for it where $f(x) > 0$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-55-t1",
                "statement": (
                    "Find $\\displaystyle\\int (8x^{3} - 6x)\\,dx$. **[3]**"
                ),
                "solution": (
                    "$\\dfrac{8x^{4}}{4} - \\dfrac{6x^{2}}{2} + C$ *(M1 A1)* "
                    "$= 2x^{4} - 3x^{2} + C$ *(A1)*."
                ),
                "check": [
                    "diff(2*x**4 - 3*x**2, x) == 8*x**3 - 6*x",
                ],
            },
            {
                "id": "aisl-55-t2",
                "statement": (
                    "Evaluate $\\displaystyle\\int_1^4 (2x + 1)\\,dx$ and state what it "
                    "represents. **[4]**"
                ),
                "solution": (
                    "$\\left[x^{2} + x\\right]_1^4 = (16 + 4) - (1 + 1)$ *(M1 A1)* "
                    "$= 18$ *(A1)*.  \n"
                    "Since $2x + 1 > 0$ on $[1, 4]$, this is the area under the line between "
                    "$x = 1$ and $x = 4$ *(A1)*."
                ),
                "check": [
                    "integrate(2*x + 1, (x, 1, 4)) == 18",
                    "2*1 + 1 > 0",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.5 · Papers 1 & 2",
                    "title": "Run the power rule backwards",
                    "body": (
                        "Differentiation multiplies by the power and drops it. Integration adds "
                        "one to the power and divides by the new one. Two operations, exact "
                        "opposites — except for the constant, which differentiation destroys and "
                        "integration cannot recover without extra information."
                    ),
                },
                {
                    "kind": "areaGraph",
                    "eyebrow": "Play",
                    "title": "Rectangles closing in on the area",
                    "teach": (
                        "Add strips and watch the staircase approach the curve. The area under a "
                        "curve is the limit of that sum — and the remarkable fact of calculus is "
                        "that you can get it exactly by anti-differentiating instead of by "
                        "adding up infinitely many rectangles."
                    ),
                    "config": {"mode": "riemann"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Indefinite, then definite",
                    "beats": [
                        "Raise each power by one and divide by the new power.",
                        "Add $+C$ — always, for an indefinite integral.",
                        "Boundary condition? Substitute the point AFTER integrating.",
                        "Definite: evaluate at the top limit minus the bottom limit; no $C$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A boundary condition finds $C$",
                    "problemId": "aisl-55-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Backwards power rule",
                    "title": "Integrate $x^{3}$",
                    "prompt": "$\\displaystyle\\int x^{3}\\,dx$ equals",
                    "options": [
                        "$\\frac{x^{4}}{4} + C$",
                        "$3x^{2} + C$",
                        "$\\frac{x^{2}}{2} + C$",
                        "$4x^{4} + C$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Add one to the power to get $x^{4}$, then divide by $4$. Check by "
                        "differentiating: $\\frac{4x^{3}}{4} = x^{3}$ ✓. The option $3x^{2}$ is "
                        "the DERIVATIVE — the operation run the wrong way."
                    ),
                    "check": [
                        "diff(x**4/4, x) == x**3",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Definite integrals and an enclosed area",
                    "problemId": "aisl-55-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Find the limits",
                    "title": "Where does the region end?",
                    "prompt": (
                        "To find the area enclosed by $y = 6x - x^{2}$ and the $x$-axis, the "
                        "limits are"
                    ),
                    "options": [
                        "$0$ and $6$",
                        "$0$ and $3$",
                        "$-6$ and $6$",
                        "$1$ and $6$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The curve meets the axis where $x(6 - x) = 0$, at $x = 0$ and "
                        "$x = 6$. The value $3$ is where the curve PEAKS — the middle of the "
                        "region, not its edge."
                    ),
                    "check": [
                        "solve(6*x - x**2, x) == [0, 6]",
                        "integrate(6*x - x**2, (x, 0, 6)) == 36",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Differentiate your answer back",
                    "body": (
                        "Every integration can be checked in one line: differentiate what you "
                        "wrote and see whether the integrand reappears. It costs seconds and "
                        "catches the two commonest slips — a wrong new power and a missing "
                        "division."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-55-t1"},
                {"kind": "tryIt", "problemId": "aisl-55-t2"},
                {
                    "kind": "recap",
                    "title": "Integration, compressed",
                    "points": [
                        "Add one to the power, divide by the new power, $+C$.",
                        "A boundary condition fixes $C$ — integrate first, substitute second.",
                        "Definite integrals take limits and give a number.",
                        "Above the axis, that number is the area.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 8 — AI SL 5.8: the trapezoidal rule
# ===========================================================================
def lesson_trapezoidal_rule():
    return {
        "slug": "the-trapezoidal-rule",
        "title": "The Trapezoidal Rule",
        "concreteComparison": (
            "A river's width is measured every ten metres across. Nobody has a formula for the "
            "river bed, and there is nothing to integrate — but joining the measured depths with "
            "straight lines gives a row of trapeziums whose areas add up to a very good estimate "
            "of the cross-section."
        ),
        "objective": (
            "Use the trapezoidal rule to approximate an area or an integral, and say whether it "
            "over- or under-estimates."
        ),
        "concept": [
            "**Syllabus card — AI SL 5.8.** Approximating areas using the trapezoidal rule. "
            "**Papers 1 and 2.** The formula is in the booklet, and this code has no counterpart "
            "in Analysis & Approaches.",
            "The idea is to replace the curve by straight chords. Divide $[a, b]$ into $n$ "
            "strips of equal width $h = \\dfrac{b-a}{n}$, read off the $n+1$ heights "
            "$y_0, y_1, \\ldots, y_n$, and add the trapezium areas. Collecting terms gives the "
            "booklet formula, in which the two END heights are counted once and every INTERIOR "
            "height is counted twice.",
            "Counting the strips correctly is the commonest slip. $n$ strips need $n+1$ heights: "
            "four strips from $x = 0$ to $x = 4$ means $h = 1$ and heights at $0, 1, 2, 3, 4$. "
            "Using five strips' worth of heights with four strips' width is the standard way "
            "this goes wrong.",
            "The rule tells you which way the estimate errs. When the curve is CONCAVE UP "
            "(bending upwards, like $y = x^{2}$), each chord lies ABOVE the curve, so the "
            "trapeziums include a sliver too much and the rule OVER-estimates. When the curve is "
            "concave down, the chords lie below and it under-estimates.",
            "Its real value is data. A set of measured readings — speeds every ten seconds, "
            "widths every metre, rainfall every hour — has no formula at all, so no integration "
            "is possible. The trapezoidal rule works from the numbers alone, which is exactly "
            "the situation an applied course cares about."
        ],
        "keyIdea": (
            "Ends once, middles twice, all times $\\frac{h}{2}$. Concave up over-estimates; "
            "concave down under-estimates."
        ),
        "facts": [
            {
                "title": "The trapezoidal rule",
                "latex": "A \\approx \\frac{1}{2}h\\left((y_0 + y_n) + 2(y_1 + y_2 + \\cdots + y_{n-1})\\right), \\quad h = \\frac{b-a}{n}",
                "explanation": "Booklet (AI SL 5.8). Ends once, interiors twice.",
            },
            {
                "title": "Which way it errs",
                "latex": "\\text{concave up} \\Rightarrow \\text{over-estimate}, \\qquad \\text{concave down} \\Rightarrow \\text{under-estimate}",
                "explanation": "The chords sit above a curve that bends up, and below one that bends down.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-58-we1",
                "statement": (
                    "Use the trapezoidal rule with $4$ strips to estimate "
                    "$\\displaystyle\\int_0^4 (x^{2} + 1)\\,dx$.  \n"
                    "**(a)** Find $h$ and the five heights. **[3]**  \n"
                    "**(b)** Apply the rule. **[3]**  \n"
                    "**(c)** The exact value is $\\dfrac{76}{3}$. Find the percentage error and "
                    "explain the direction of the error. **[4]**"
                ),
                "solution": (
                    "**(a)** $h = \\dfrac{4 - 0}{4} = 1$ *(A1)*. The heights at "
                    "$x = 0, 1, 2, 3, 4$ are $1, 2, 5, 10, 17$ *(A1 A1)*.  \n"
                    "**(b)** $A \\approx \\dfrac{1}{2}(1)\\left((1 + 17) + 2(2 + 5 + 10)\\right)$ "
                    "*(M1 A1)* $= \\dfrac{1}{2}(18 + 34) = 26$ *(A1)*.  \n"
                    "**(c)** Exact $= \\dfrac{76}{3} = 25.33$, so the error is "
                    "$\\left|\\dfrac{26 - 25.33}{25.33}\\right| \\times 100 = 2.63\\%$ "
                    "*(M1 A1)*. The curve $y = x^{2} + 1$ is concave up, so each chord lies "
                    "above it *(R1)* and the rule over-estimates *(A1)*.  \n"
                    "**Narrative:** the over-estimate was predictable before any arithmetic — "
                    "$y = x^{2} + 1$ bends upwards everywhere, so every trapezium's sloping top "
                    "sits above the curve it is standing in for. Doubling the number of strips "
                    "would roughly quarter the error, which is why data collected at finer "
                    "intervals gives a much better estimate."
                ),
                "check": [
                    "Rational(4 - 0, 4) == 1",
                    "0**2 + 1 == 1",
                    "1**2 + 1 == 2",
                    "2**2 + 1 == 5",
                    "3**2 + 1 == 10",
                    "4**2 + 1 == 17",
                    "Rational(1, 2)*1*((1 + 17) + 2*(2 + 5 + 10)) == 26",
                    "integrate(x**2 + 1, (x, 0, 4)) == Rational(76, 3)",
                    "Abs(Abs(26 - Rational(76, 3))/Rational(76, 3)*100 - Rational(263, 100)) < Rational(1, 100)",
                    "26 > Rational(76, 3)",
                ],
            },
            {
                "id": "aisl-58-we2",
                "statement": (
                    "A car's speed, in m s$^{-1}$, is recorded every $10$ seconds:  \n"
                    "$t$: $0, 10, 20, 30, 40$  \n"
                    "$v$: $0, 12, 20, 25, 27$  \n"
                    "**(a)** Explain why the trapezoidal rule is appropriate here. **[2]**  \n"
                    "**(b)** Estimate the distance travelled in the $40$ seconds. **[4]**  \n"
                    "**(c)** State one way the estimate could be improved. **[1]**"
                ),
                "solution": (
                    "**(a)** Distance is the area under a speed–time graph *(A1)*, and there is "
                    "no formula for $v(t)$ — only measured readings — so the integral cannot be "
                    "evaluated and must be approximated *(A1)*.  \n"
                    "**(b)** $h = 10$ *(A1)*, so "
                    "$d \\approx \\dfrac{1}{2}(10)\\left((0 + 27) + 2(12 + 20 + 25)\\right)$ "
                    "*(M1 A1)* $= 5(27 + 114) = 705$ m *(A1)*.  \n"
                    "**(c)** Record the speed more often — smaller strips follow the curve more "
                    "closely *(A1)*.  \n"
                    "**Narrative:** part (a) is the reason this code exists. A modelling course "
                    "meets data far more often than it meets formulas, and the trapezoidal rule "
                    "is the tool that turns five numbers into a distance. Note the units: "
                    "m s$^{-1}$ multiplied by seconds gives metres, which is a free check that "
                    "the area really is a distance."
                ),
                "check": [
                    "Rational(40 - 0, 4) == 10",
                    "Rational(1, 2)*10*((0 + 27) + 2*(12 + 20 + 25)) == 705",
                    "12 + 20 + 25 == 57",
                    "5*(27 + 114) == 705",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Confusing the number of strips with the number of heights.",
                "correction": "$n$ strips need $n+1$ heights. Four strips over $[0, 4]$ means $h = 1$ and readings at $0, 1, 2, 3, 4$.",
                "authored": True,
            },
            {
                "text": "Doubling the end heights as well as the interior ones.",
                "correction": "Ends once, interiors twice. Each interior height is shared by two trapeziums; the ends belong to only one.",
                "authored": True,
            },
            {
                "text": "Forgetting the $\\frac{1}{2}h$ factor.",
                "correction": "The whole bracket is multiplied by $\\frac{h}{2}$. Leaving it out inflates the answer by a factor of $\\frac{2}{h}$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-58-t1",
                "statement": (
                    "Use the trapezoidal rule with $4$ strips to estimate "
                    "$\\displaystyle\\int_1^3 \\dfrac{1}{x}\\,dx$, to 3 s.f. **[4]**"
                ),
                "solution": (
                    "$h = \\dfrac{3 - 1}{4} = 0.5$ *(A1)*, with heights at "
                    "$x = 1, 1.5, 2, 2.5, 3$: $1, \\frac{2}{3}, \\frac{1}{2}, \\frac{2}{5}, "
                    "\\frac{1}{3}$ *(A1)*.  \n"
                    "$A \\approx \\dfrac{1}{2}(0.5)\\left(\\left(1 + \\tfrac{1}{3}\\right) + "
                    "2\\left(\\tfrac{2}{3} + \\tfrac{1}{2} + \\tfrac{2}{5}\\right)\\right)$ "
                    "*(M1)* $= 1.12$ *(A1)*.  \n"
                    "The exact value is $\\ln 3 = 1.0986$, so the rule over-estimates by about "
                    "$1.6\\%$ — as expected, since $y = \\frac{1}{x}$ is concave up."
                ),
                "check": [
                    "Rational(3 - 1, 4) == Rational(1, 2)",
                    "Abs(Rational(1, 2)*Rational(1, 2)*((1 + Rational(1, 3)) + 2*(Rational(2, 3) + Rational(1, 2) + Rational(2, 5))) - Rational(112, 100)) < Rational(5, 1000)",
                    "Rational(1, 2)*Rational(1, 2)*((1 + Rational(1, 3)) + 2*(Rational(2, 3) + Rational(1, 2) + Rational(2, 5))) > log(3)",
                ],
            },
            {
                "id": "aisl-58-t2",
                "statement": (
                    "State, with a reason, whether the trapezoidal rule over- or "
                    "under-estimates the area under a curve that is concave down throughout. "
                    "**[2]**"
                ),
                "solution": (
                    "It under-estimates *(A1)*.  \n"
                    "A concave-down curve bulges above its chords, so each trapezium misses the "
                    "sliver between the chord and the curve *(R1)*."
                ),
                "check": [
                    "Rational(1, 2)*1*((0 + 0) + 2*(3 + 4 + 3)) < integrate(4*x - x**2, (x, 0, 4))",
                    "4*1 - 1**2 == 3",
                    "4*2 - 2**2 == 4",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 5.8 · Papers 1 & 2",
                    "title": "When there is nothing to integrate",
                    "body": (
                        "Analysis & Approaches never meets this rule, because AA problems always "
                        "come with a formula. AI meets DATA — five readings from a river, a "
                        "speedometer, a rain gauge — and needs an area anyway. Straight lines "
                        "between the points are the answer."
                    ),
                },
                {
                    "kind": "areaGraph",
                    "eyebrow": "Play",
                    "title": "Strips under a curve",
                    "teach": (
                        "Add strips and watch the approximation tighten. The trapezoidal rule is "
                        "this picture with sloping tops instead of flat ones — which is why it "
                        "closes in on the true area much faster than rectangles do."
                    ),
                    "config": {"mode": "riemann"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Applying the rule",
                    "beats": [
                        "$h = \\frac{b-a}{n}$; you will need $n+1$ heights.",
                        "List the heights in order, $y_0$ to $y_n$.",
                        "Add the two ends; add the interiors and double them.",
                        "Multiply the total by $\\frac{h}{2}$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Four strips, and the error they leave",
                    "problemId": "aisl-58-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Count them",
                    "title": "How many heights?",
                    "prompt": (
                        "Using the trapezoidal rule with $6$ strips on $[2, 8]$, the width $h$ "
                        "and the number of heights are"
                    ),
                    "options": [
                        "$h = 1$ and $7$ heights",
                        "$h = 1$ and $6$ heights",
                        "$h = 6$ and $7$ heights",
                        "$h = \\frac{1}{6}$ and $6$ heights",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$h = \\frac{8-2}{6} = 1$, and $6$ strips have $7$ boundaries — "
                        "$x = 2, 3, 4, 5, 6, 7, 8$. There is always one more height than there "
                        "are strips."
                    ),
                    "check": [
                        "Rational(8 - 2, 6) == 1",
                        "6 + 1 == 7",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Distance from a speed table",
                    "problemId": "aisl-58-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Which way?",
                    "title": "Over or under?",
                    "prompt": (
                        "For a curve that is concave up throughout, the trapezoidal rule gives an"
                    ),
                    "options": [
                        "over-estimate, because the chords lie above the curve",
                        "under-estimate, because the chords lie below the curve",
                        "exact answer",
                        "estimate that could go either way",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "A curve bending upwards sags below the straight line joining any two of "
                        "its points, so each trapezium contains a little more than the region "
                        "under the curve. Concave down is the mirror image."
                    ),
                    "check": [
                        "26 > Rational(76, 3)",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Write the substitution in full",
                    "body": (
                        "Put the numbers into the formula on the page before evaluating: "
                        "$\\frac{1}{2}(10)((0 + 27) + 2(12 + 20 + 25))$. It earns the method "
                        "mark outright, and it makes a doubled end height or a missed interior "
                        "visible at a glance."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-58-t1"},
                {"kind": "tryIt", "problemId": "aisl-58-t2"},
                {
                    "kind": "recap",
                    "title": "The trapezoidal rule, compressed",
                    "points": [
                        "$h = \\frac{b-a}{n}$, and $n$ strips need $n+1$ heights.",
                        "Ends once, interiors twice, all multiplied by $\\frac{h}{2}$.",
                        "Concave up over-estimates; concave down under-estimates.",
                        "Its real use is data with no formula behind it.",
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
            "id": "aisl-cl-p01",
            "statement": (
                "$C(x)$ is the cost in dollars of producing $x$ chairs, and $C'(30) = 85$. "
                "State the units and interpret the value. **[3]**"
            ),
            "solution": (
                "The units are dollars per chair *(A1)*.  \n"
                "When $30$ chairs are being produced, the total cost is rising at $\\$85$ per "
                "additional chair *(A1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.1", "mono": True}, {"text": "P1"}],
            "check": ["85 > 0", "3*85 == 255"],
        },
        {
            "id": "aisl-cl-p02",
            "statement": "Differentiate $y = 7x^{4} - 3x^{2} + 8x - 2$. **[3]**",
            "solution": "$\\dfrac{dy}{dx} = 28x^{3} - 6x + 8$ *(A1 A1 A1)* — the $-2$ vanishes.",
            "badges": [{"text": "ib-ai-sl-5.3", "mono": True}, {"text": "P1"}],
            "check": ["diff(7*x**4 - 3*x**2 + 8*x - 2, x) == 28*x**3 - 6*x + 8"],
        },
        {
            "id": "aisl-cl-p03",
            "statement": "Differentiate $f(x) = \\dfrac{6}{x^{2}}$. **[3]**",
            "solution": (
                "Rewrite as $f(x) = 6x^{-2}$ *(M1)*.  \n"
                "$f'(x) = -12x^{-3}$ *(A1)* $= -\\dfrac{12}{x^{3}}$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.3", "mono": True}, {"text": "P1"}],
            "check": ["diff(6/x**2, x) == -12/x**3"],
        },
        {
            "id": "aisl-cl-p04",
            "statement": (
                "Expand and differentiate $y = x(3x - 2)$. **[3]**"
            ),
            "solution": (
                "$y = 3x^{2} - 2x$ *(M1)*, so $\\dfrac{dy}{dx} = 6x - 2$ *(A1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.3", "mono": True}, {"text": "P1"}],
            "check": [
                "expand(x*(3*x - 2)) == 3*x**2 - 2*x",
                "diff(3*x**2 - 2*x, x) == 6*x - 2",
            ],
        },
        {
            "id": "aisl-cl-p05",
            "statement": (
                "For $f(x) = x^{2} - 8x + 3$, find $f'(x)$ and state where $f$ is increasing. "
                "**[3]**"
            ),
            "solution": (
                "$f'(x) = 2x - 8$ *(A1)*, which is zero at $x = 4$ *(A1)*.  \n"
                "For $x > 4$, $f'(x) > 0$, so $f$ is increasing for $x > 4$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.2", "mono": True}, {"text": "P1"}],
            "check": [
                "diff(x**2 - 8*x + 3, x) == 2*x - 8",
                "solve(2*x - 8, x) == [4]",
                "2*5 - 8 > 0",
            ],
        },
        {
            "id": "aisl-cl-p06",
            "statement": (
                "A population satisfies $P'(t) = -140$ at $t = 12$ years, where $P$ is measured "
                "in people. Interpret this. **[2]**"
            ),
            "solution": (
                "At $t = 12$ years the population is DECREASING *(A1)* at a rate of $140$ "
                "people per year *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.2", "mono": True}, {"text": "P1"}],
            "check": ["-140 < 0", "Abs(-140) == 140"],
        },
        {
            "id": "aisl-cl-p07",
            "statement": (
                "Find the gradient of $y = x^{3} + 2x$ at the point where $x = 2$. **[3]**"
            ),
            "solution": (
                "$\\dfrac{dy}{dx} = 3x^{2} + 2$ *(A1 A1)*.  \n"
                "At $x = 2$: $12 + 2 = 14$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.4", "mono": True}, {"text": "P1"}],
            "check": [
                "diff(x**3 + 2*x, x) == 3*x**2 + 2",
                "3*2**2 + 2 == 14",
            ],
        },
        {
            "id": "aisl-cl-p08",
            "statement": (
                "Find the equation of the tangent to $y = x^{2} + 2x$ at $x = 1$. **[4]**"
            ),
            "solution": (
                "$y = 1 + 2 = 3$, so the point is $(1, 3)$ *(A1)*.  \n"
                "$\\dfrac{dy}{dx} = 2x + 2$, giving gradient $4$ *(M1 A1)*.  \n"
                "$y - 3 = 4(x - 1)$, i.e. $y = 4x - 1$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.4", "mono": True}, {"text": "P2"}],
            "check": [
                "1**2 + 2*1 == 3",
                "diff(x**2 + 2*x, x) == 2*x + 2",
                "2*1 + 2 == 4",
                "4*1 - 1 == 3",
            ],
        },
        {
            "id": "aisl-cl-p09",
            "statement": (
                "A tangent to a curve has gradient $-4$ at a point. Find the gradient of the "
                "normal there. **[2]**"
            ),
            "solution": (
                "The negative reciprocal: $\\dfrac{1}{4}$ *(M1 A1)*. Check: "
                "$-4 \\times \\dfrac{1}{4} = -1$ ✓."
            ),
            "badges": [{"text": "ib-ai-sl-5.4", "mono": True}, {"text": "P1"}],
            "check": ["-4*Rational(1, 4) == -1"],
        },
        {
            "id": "aisl-cl-p10",
            "statement": (
                "Find the coordinates of the stationary point of $y = x^{2} - 10x + 3$ and "
                "classify it. **[4]**"
            ),
            "solution": (
                "$\\dfrac{dy}{dx} = 2x - 10 = 0$ gives $x = 5$ *(M1 A1)*, where "
                "$y = 25 - 50 + 3 = -22$ *(A1)*.  \n"
                "The gradient is negative before $x = 5$ and positive after, so $(5, -22)$ is a "
                "minimum *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.6", "mono": True}, {"text": "P1"}],
            "check": [
                "diff(x**2 - 10*x + 3, x) == 2*x - 10",
                "solve(2*x - 10, x) == [5]",
                "25 - 50 + 3 == -22",
                "2*4 - 10 < 0",
                "2*6 - 10 > 0",
            ],
        },
        {
            "id": "aisl-cl-p11",
            "statement": (
                "Find the values of $x$ at which $y = 2x^{3} - 3x^{2} - 12x + 4$ is stationary. "
                "**[4]**"
            ),
            "solution": (
                "$\\dfrac{dy}{dx} = 6x^{2} - 6x - 12 = 6(x - 2)(x + 1)$ *(M1 A1 A1)*.  \n"
                "So $x = 2$ or $x = -1$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.6", "mono": True}, {"text": "P1"}],
            "check": [
                "diff(2*x**3 - 3*x**2 - 12*x + 4, x) == 6*x**2 - 6*x - 12",
                "expand(6*(x - 2)*(x + 1)) == 6*x**2 - 6*x - 12",
                "solve(6*x**2 - 6*x - 12, x) == [-1, 2]",
            ],
        },
        {
            "id": "aisl-cl-p12",
            "statement": (
                "A rectangle has perimeter $40$ cm. Find the dimensions giving the greatest "
                "area. **[4]**"
            ),
            "solution": (
                "With width $x$, the height is $20 - x$ *(A1)*, so "
                "$A = 20x - x^{2}$ *(A1)*.  \n"
                "$\\dfrac{dA}{dx} = 20 - 2x = 0$ at $x = 10$ *(M1)*, giving a $10$ cm square of "
                "area $100$ cm$^{2}$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.7", "mono": True}, {"text": "P2"}],
            "check": [
                "expand(x*(20 - x)) == 20*x - x**2",
                "diff(20*x - x**2, x) == 20 - 2*x",
                "solve(20 - 2*x, x) == [10]",
                "10*10 == 100",
            ],
        },
        {
            "id": "aisl-cl-p13",
            "statement": "Find $\\displaystyle\\int (10x^{4} - 6x)\\,dx$. **[3]**",
            "solution": "$2x^{5} - 3x^{2} + C$ *(A1 A1 A1)* — remember the constant.",
            "badges": [{"text": "ib-ai-sl-5.5", "mono": True}, {"text": "P1"}],
            "check": ["diff(2*x**5 - 3*x**2, x) == 10*x**4 - 6*x"],
        },
        {
            "id": "aisl-cl-p14",
            "statement": (
                "A curve has $\\dfrac{dy}{dx} = 4x - 1$ and passes through $(2, 7)$. Find its "
                "equation. **[4]**"
            ),
            "solution": (
                "$y = 2x^{2} - x + C$ *(M1 A1)*.  \n"
                "At $(2, 7)$: $8 - 2 + C = 7$ *(M1)*, so $C = 1$ and "
                "$y = 2x^{2} - x + 1$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.5", "mono": True}, {"text": "P2"}],
            "check": [
                "diff(2*x**2 - x + 1, x) == 4*x - 1",
                "2*4 - 2 + 1 == 7",
            ],
        },
        {
            "id": "aisl-cl-p15",
            "statement": (
                "Evaluate $\\displaystyle\\int_0^2 (3x^{2} + 2)\\,dx$. **[3]**"
            ),
            "solution": (
                "$\\left[x^{3} + 2x\\right]_0^2$ *(M1 A1)* $= (8 + 4) - 0 = 12$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.5", "mono": True}, {"text": "P1"}],
            "check": ["integrate(3*x**2 + 2, (x, 0, 2)) == 12"],
        },
        {
            "id": "aisl-cl-p16",
            "statement": (
                "Find the area enclosed by $y = 9 - x^{2}$ and the $x$-axis. **[4]**"
            ),
            "solution": (
                "The curve meets the axis at $x = \\pm 3$ *(M1 A1)*.  \n"
                "$\\displaystyle\\int_{-3}^{3} (9 - x^{2})\\,dx = "
                "\\left[9x - \\dfrac{x^{3}}{3}\\right]_{-3}^{3} = 18 - (-18)$ *(M1)* "
                "$= 36$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.5", "mono": True}, {"text": "P2"}],
            "check": [
                "solve(9 - x**2, x) == [-3, 3]",
                "integrate(9 - x**2, (x, -3, 3)) == 36",
                "9 - 0**2 > 0",
            ],
        },
        {
            "id": "aisl-cl-p17",
            "statement": (
                "Use the trapezoidal rule with $2$ strips to estimate "
                "$\\displaystyle\\int_0^2 x^{2}\\,dx$. **[3]**"
            ),
            "solution": (
                "$h = 1$, with heights $0, 1, 4$ *(A1)*.  \n"
                "$A \\approx \\dfrac{1}{2}(1)\\left((0 + 4) + 2(1)\\right)$ *(M1)* "
                "$= 3$ *(A1)*.  \n"
                "The exact value is $\\frac{8}{3} = 2.67$ — the rule over-estimates, as it "
                "always does for a concave-up curve."
            ),
            "badges": [{"text": "ib-ai-sl-5.8", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(1, 2)*1*((0 + 4) + 2*1) == 3",
                "integrate(x**2, (x, 0, 2)) == Rational(8, 3)",
                "3 > Rational(8, 3)",
            ],
        },
        {
            "id": "aisl-cl-p18",
            "statement": (
                "Using the trapezoidal rule with $5$ strips on the interval $[1, 11]$, find "
                "$h$ and state how many heights are needed. **[2]**"
            ),
            "solution": (
                "$h = \\dfrac{11 - 1}{5} = 2$ *(A1)*.  \n"
                "Five strips need six heights, at $x = 1, 3, 5, 7, 9, 11$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-5.8", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(11 - 1, 5) == 2",
                "5 + 1 == 6",
                "1 + 5*2 == 11",
            ],
        },
    ]


def test_bank():
    return [
        {
            "id": "aisl-cl-x01",
            "statement": (
                "Consider $f(x) = x^{3} - 6x^{2} + 9x + 2$.  \n"
                "**(a)** Find $f'(x)$. **[2]**  \n"
                "**(b)** Find and classify the stationary points. **[6]**  \n"
                "**(c)** State the intervals on which $f$ is increasing. **[2]**"
            ),
            "solution": (
                "**(a)** $f'(x) = 3x^{2} - 12x + 9$ *(A1 A1)*.  \n"
                "**(b)** $3(x - 1)(x - 3) = 0$ gives $x = 1$ and $x = 3$ *(M1 A1)*, with "
                "$f(1) = 6$ and $f(3) = 2$ *(A1 A1)*. Since $f'(0) = 9 > 0$, "
                "$f'(2) = -3 < 0$ and $f'(4) = 9 > 0$ *(M1)*, $(1, 6)$ is a maximum and "
                "$(3, 2)$ is a minimum *(A1)*.  \n"
                "**(c)** $f$ increases for $x < 1$ and for $x > 3$ *(A1 A1)*.  \n"
                "The local minimum value $2$ equals $f(0)$ — a reminder that a local minimum is "
                "only lowest in its own neighbourhood."
            ),
            "badges": [{"text": "ib-ai-sl-5.6", "mono": True}, {"text": "P2"}],
            "check": [
                "diff(x**3 - 6*x**2 + 9*x + 2, x) == 3*x**2 - 12*x + 9",
                "expand(3*(x - 1)*(x - 3)) == 3*x**2 - 12*x + 9",
                "1 - 6 + 9 + 2 == 6",
                "27 - 54 + 27 + 2 == 2",
                "3*0**2 - 12*0 + 9 == 9",
                "3*2**2 - 12*2 + 9 == -3",
                "3*4**2 - 12*4 + 9 == 9",
                "0**3 - 6*0**2 + 9*0 + 2 == 2",
            ],
        },
        {
            "id": "aisl-cl-x02",
            "statement": (
                "The curve is $y = 2x^{2} - 5x + 1$.  \n"
                "**(a)** Find the coordinates of the point where $x = 3$. **[2]**  \n"
                "**(b)** Find the equation of the tangent there. **[3]**  \n"
                "**(c)** Find the equation of the normal there. **[3]**  \n"
                "**(d)** Find where the normal crosses the $y$-axis. **[2]**"
            ),
            "solution": (
                "**(a)** $y = 18 - 15 + 1 = 4$, so $(3, 4)$ *(M1 A1)*.  \n"
                "**(b)** $\\dfrac{dy}{dx} = 4x - 5$, so the gradient is $7$ *(A1 M1)*. The "
                "tangent is $y = 7x - 17$ *(A1)*.  \n"
                "**(c)** Normal gradient $-\\dfrac{1}{7}$ *(A1)*, so "
                "$y - 4 = -\\dfrac{1}{7}(x - 3)$, i.e. "
                "$y = -\\dfrac{1}{7}x + \\dfrac{31}{7}$ *(M1 A1)*.  \n"
                "**(d)** At $x = 0$: $y = \\dfrac{31}{7} = 4.43$ *(M1 A1)*.  \n"
                "Both lines pass through $(3, 4)$: $7(3) - 17 = 4$ ✓ and "
                "$-\\frac{3}{7} + \\frac{31}{7} = 4$ ✓."
            ),
            "badges": [{"text": "ib-ai-sl-5.4", "mono": True}, {"text": "P2"}],
            "check": [
                "2*3**2 - 5*3 + 1 == 4",
                "diff(2*x**2 - 5*x + 1, x) == 4*x - 5",
                "4*3 - 5 == 7",
                "7*3 - 17 == 4",
                "7*Rational(-1, 7) == -1",
                "Rational(-1, 7)*3 + Rational(31, 7) == 4",
                "Abs(Rational(31, 7) - Rational(443, 100)) < Rational(5, 1000)",
            ],
        },
        {
            "id": "aisl-cl-x03",
            "statement": (
                "An open-topped tank has a square base of side $x$ m and must hold $108$ "
                "m$^{3}$.  \n"
                "**(a)** Show that the surface area is $S = x^{2} + \\dfrac{432}{x}$. **[3]**  \n"
                "**(b)** Find the value of $x$ that minimises $S$, justifying that it is a "
                "minimum. **[5]**  \n"
                "**(c)** Find the minimum surface area and the corresponding depth. **[3]**"
            ),
            "solution": (
                "**(a)** The depth is $h = \\dfrac{108}{x^{2}}$ *(A1)*. The surface is the base "
                "plus four sides: $S = x^{2} + 4xh$ *(A1)* "
                "$= x^{2} + \\dfrac{432}{x}$ *(AG)* *(A1)*.  \n"
                "**(b)** $\\dfrac{dS}{dx} = 2x - \\dfrac{432}{x^{2}}$ *(A1)*, zero when "
                "$2x^{3} = 432$ *(M1)*, so $x^{3} = 216$ and $x = 6$ m *(A1 A1)*. Since "
                "$\\frac{dS}{dx} < 0$ for $x < 6$ and $> 0$ for $x > 6$, this is a minimum "
                "*(R1)*.  \n"
                "**(c)** $S = 36 + 72 = 108$ m$^{2}$ *(M1 A1)*, and "
                "$h = \\dfrac{108}{36} = 3$ m *(A1)*.  \n"
                "The optimal tank is twice as wide as it is deep — the open-top analogue of the "
                "closed can's height-equals-diameter result."
            ),
            "badges": [{"text": "ib-ai-sl-5.7", "mono": True}, {"text": "P2"}],
            "check": [
                "Eq(simplify(x**2 + 4*x*(108/x**2) - x**2 - 432/x), 0)",
                "diff(x**2 + 432/x, x) == 2*x - 432/x**2",
                "6**3 == 216",
                "2*216 == 432",
                "2*3 - Rational(432, 9) < 0",
                "2*9 - Rational(432, 81) > 0",
                "36 + Rational(432, 6) == 108",
                "Rational(108, 36) == 3",
                "6 == 2*3",
            ],
        },
        {
            "id": "aisl-cl-x04",
            "statement": (
                "**(a)** Find $\\displaystyle\\int \\left(9x^{2} - \\dfrac{4}{x^{2}}\\right)dx$. "
                "**[4]**  \n"
                "**(b)** A curve has this expression as its gradient function and passes "
                "through $(1, 5)$. Find its equation. **[3]**  \n"
                "**(c)** Find the gradient of the curve at $x = 2$. **[2]**"
            ),
            "solution": (
                "**(a)** Rewrite the second term as $-4x^{-2}$ *(M1)*. Integrating: "
                "$3x^{3} + 4x^{-1} + C$ *(A1 A1)* $= 3x^{3} + \\dfrac{4}{x} + C$ *(A1)*.  \n"
                "**(b)** At $(1, 5)$: $3 + 4 + C = 5$ *(M1 A1)*, so $C = -2$ and "
                "$y = 3x^{3} + \\dfrac{4}{x} - 2$ *(A1)*.  \n"
                "**(c)** $\\dfrac{dy}{dx} = 9x^{2} - \\dfrac{4}{x^{2}}$, so at $x = 2$ it is "
                "$36 - 1 = 35$ *(M1 A1)*.  \n"
                "Integrating $-4x^{-2}$ raises the power to $-1$ and divides by $-1$, turning "
                "the minus into a plus — the sign flip that makes this question worth setting."
            ),
            "badges": [{"text": "ib-ai-sl-5.5", "mono": True}, {"text": "P2"}],
            "check": [
                "diff(3*x**3 + 4/x, x) == 9*x**2 - 4/x**2",
                "3 + 4 - 2 == 5",
                "9*2**2 - Rational(4, 4) == 35",
            ],
        },
        {
            "id": "aisl-cl-x05",
            "statement": (
                "The region $R$ is enclosed by the curve $y = x^{2} - 4x + 5$, the $x$-axis, "
                "and the lines $x = 1$ and $x = 4$.  \n"
                "**(a)** Verify that the curve lies above the $x$-axis on this interval. "
                "**[3]**  \n"
                "**(b)** Find the exact area of $R$. **[4]**  \n"
                "**(c)** Find the minimum value of $y$ on the interval. **[3]**"
            ),
            "solution": (
                "**(a)** $y = (x - 2)^{2} + 1$ *(M1 A1)*, and a square is never negative, so "
                "$y \\ge 1 > 0$ everywhere *(A1)*.  \n"
                "**(b)** $\\displaystyle\\int_1^4 (x^{2} - 4x + 5)\\,dx = "
                "\\left[\\dfrac{x^{3}}{3} - 2x^{2} + 5x\\right]_1^4$ *(M1 A1)*. At $x = 4$ this "
                "is $\\frac{64}{3} - 32 + 20 = \\frac{28}{3}$; at $x = 1$ it is "
                "$\\frac{1}{3} - 2 + 5 = \\frac{10}{3}$ *(A1)*. The area is $6$ *(A1)*.  \n"
                "**(c)** The vertex form gives the minimum directly: $y = 1$ at $x = 2$ "
                "*(M1 A1 A1)*.  \n"
                "Completing the square in (a) paid for itself twice — it settled the positivity "
                "and it answered (c) without any differentiation at all."
            ),
            "badges": [{"text": "ib-ai-sl-5.5", "mono": True}, {"text": "P2"}],
            "check": [
                "expand((x - 2)**2 + 1) == x**2 - 4*x + 5",
                "integrate(x**2 - 4*x + 5, (x, 1, 4)) == 6",
                "Rational(64, 3) - 32 + 20 == Rational(28, 3)",
                "Rational(1, 3) - 2 + 5 == Rational(10, 3)",
                "2**2 - 4*2 + 5 == 1",
            ],
        },
        {
            "id": "aisl-cl-x06",
            "statement": (
                "Use the trapezoidal rule with $4$ strips to estimate "
                "$\\displaystyle\\int_0^2 (x^{3} + 1)\\,dx$.  \n"
                "**(a)** Find $h$ and list the heights. **[3]**  \n"
                "**(b)** Apply the rule. **[3]**  \n"
                "**(c)** Find the exact value and the percentage error, to 3 s.f. **[4]**"
            ),
            "solution": (
                "**(a)** $h = 0.5$ *(A1)*, with heights at $x = 0, 0.5, 1, 1.5, 2$: "
                "$1, 1.125, 2, 4.375, 9$ *(A1 A1)*.  \n"
                "**(b)** $A \\approx \\dfrac{1}{2}(0.5)\\left((1 + 9) + "
                "2(1.125 + 2 + 4.375)\\right)$ *(M1 A1)* "
                "$= 0.25(10 + 15) = 6.25$ *(A1)*.  \n"
                "**(c)** Exactly, $\\left[\\dfrac{x^{4}}{4} + x\\right]_0^2 = 4 + 2 = 6$ "
                "*(M1 A1)*. The error is $\\dfrac{6.25 - 6}{6} \\times 100 = 4.17\\%$ "
                "*(M1 A1)*.  \n"
                "The over-estimate is expected: $y = x^{3} + 1$ is concave up on $[0, 2]$, so "
                "every chord lies above the curve."
            ),
            "badges": [{"text": "ib-ai-sl-5.8", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(2 - 0, 4) == Rational(1, 2)",
                "Rational(1, 2)**3 + 1 == Rational(9, 8)",
                "Rational(3, 2)**3 + 1 == Rational(35, 8)",
                "2**3 + 1 == 9",
                "Rational(1, 2)*Rational(1, 2)*((1 + 9) + 2*(Rational(9, 8) + 2 + Rational(35, 8))) == Rational(25, 4)",
                "integrate(x**3 + 1, (x, 0, 2)) == 6",
                "Abs((Rational(25, 4) - 6)/6*100 - Rational(417, 100)) < Rational(1, 100)",
            ],
        },
        {
            "id": "aisl-cl-x07",
            "statement": (
                "A stone is thrown upwards and its height in metres after $t$ seconds is "
                "$h(t) = 25t - 5t^{2}$.  \n"
                "**(a)** Find $h'(t)$ and state what it represents. **[3]**  \n"
                "**(b)** Find the time at which the stone reaches its greatest height, and that "
                "height. **[4]**  \n"
                "**(c)** Find the speed at which the stone hits the ground. **[4]**"
            ),
            "solution": (
                "**(a)** $h'(t) = 25 - 10t$ *(A1 A1)* — the vertical velocity in metres per "
                "second *(A1)*.  \n"
                "**(b)** $25 - 10t = 0$ gives $t = 2.5$ s *(M1 A1)*, where "
                "$h = 62.5 - 31.25 = 31.25$ m *(M1 A1)*.  \n"
                "**(c)** The stone lands when $h = 0$: $5t(5 - t) = 0$, so $t = 5$ s "
                "*(M1 A1)*. Then $h'(5) = 25 - 50 = -25$ *(A1)*, so it lands at $25$ m s$^{-1}$ "
                "*(A1)*.  \n"
                "The negative sign in (c) is the direction — downwards — and the speed is its "
                "magnitude. Note the symmetry: the stone lands at exactly the speed it was "
                "thrown."
            ),
            "badges": [{"text": "ib-ai-sl-5.2", "mono": True}, {"text": "P2"}],
            "check": [
                "diff(25*t - 5*t**2, t) == 25 - 10*t",
                "solve(25 - 10*t, t) == [Rational(5, 2)]",
                "25*Rational(5, 2) - 5*Rational(5, 2)**2 == Rational(125, 4)",
                "Rational(125, 4) == Rational(3125, 100)",
                "solve(25*t - 5*t**2, t) == [0, 5]",
                "25 - 10*5 == -25",
            ],
        },
        {
            "id": "aisl-cl-x08",
            "statement": (
                "A river's depth in metres is measured every $4$ m across a $24$ m span:  \n"
                "distance: $0, 4, 8, 12, 16, 20, 24$  \n"
                "depth: $0, 1.2, 2.1, 2.6, 2.3, 1.4, 0$  \n"
                "**(a)** Estimate the cross-sectional area using the trapezoidal rule. **[4]**  \n"
                "**(b)** The water flows at $0.8$ m s$^{-1}$. Estimate the volume passing in one "
                "minute. **[3]**  \n"
                "**(c)** State one assumption made in **(b)**. **[1]**"
            ),
            "solution": (
                "**(a)** $h = 4$, with six strips and seven depths *(A1)*. "
                "$A \\approx \\dfrac{1}{2}(4)\\left((0 + 0) + "
                "2(1.2 + 2.1 + 2.6 + 2.3 + 1.4)\\right)$ *(M1 A1)* "
                "$= 2 \\times 2 \\times 9.6 = 38.4$ m$^{2}$ *(A1)*.  \n"
                "**(b)** In one minute the water travels $0.8 \\times 60 = 48$ m *(M1)*, so "
                "the volume is $38.4 \\times 48$ *(A1)* $= 1843.2$ m$^{3}$ *(A1)*.  \n"
                "**(c)** It assumes the flow speed is the same everywhere in the "
                "cross-section *(A1)* — in reality the water runs slower near the bed and the "
                "banks.  \n"
                "There is no formula for a river bed, which is precisely why the trapezoidal "
                "rule earns its place on a modelling course."
            ),
            "badges": [{"text": "ib-ai-sl-5.8", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(24 - 0, 6) == 4",
                "Rational(12, 10) + Rational(21, 10) + Rational(26, 10) + Rational(23, 10) + Rational(14, 10) == Rational(96, 10)",
                "Rational(1, 2)*4*((0 + 0) + 2*Rational(96, 10)) == Rational(384, 10)",
                "Rational(8, 10)*60 == 48",
                "Rational(384, 10)*48 == Rational(18432, 10)",
            ],
        },
        {
            "id": "aisl-cl-x09",
            "statement": (
                "A company's daily profit in dollars from selling $x$ items is "
                "$P(x) = 90x - 3x^{2} - 200$ for $0 \\le x \\le 30$.  \n"
                "**(a)** Find $P'(x)$ and interpret $P'(10)$. **[4]**  \n"
                "**(b)** Find the number of items that maximises profit, justifying your "
                "answer. **[4]**  \n"
                "**(c)** Find the maximum daily profit. **[2]**  \n"
                "**(d)** Find the values of $x$ for which the company breaks even, to 3 s.f. "
                "**[3]**"
            ),
            "solution": (
                "**(a)** $P'(x) = 90 - 6x$ *(A1 A1)*. Then $P'(10) = 30$ *(A1)*: at $10$ items "
                "the profit is rising at $\\$30$ per additional item *(A1)*.  \n"
                "**(b)** $90 - 6x = 0$ gives $x = 15$ *(M1 A1)*. Since $P' > 0$ for $x < 15$ "
                "and $P' < 0$ for $x > 15$ *(R1)*, this is a maximum *(A1)*.  \n"
                "**(c)** $P(15) = 1350 - 675 - 200 = \\$475$ *(M1 A1)*.  \n"
                "**(d)** $P(x) = 0$ gives $3x^{2} - 90x + 200 = 0$ *(M1)*, so "
                "$x = 2.42$ or $x = 27.6$ *(A1 A1)*.  \n"
                "Between those two values the company profits; outside them, on this domain, it "
                "loses money — the fixed cost of $\\$200$ has to be covered first."
            ),
            "badges": [{"text": "ib-ai-sl-5.7", "mono": True}, {"text": "P2"}],
            "check": [
                "diff(90*x - 3*x**2 - 200, x) == 90 - 6*x",
                "90 - 6*10 == 30",
                "solve(90 - 6*x, x) == [15]",
                "90 - 6*10 > 0",
                "90 - 6*20 < 0",
                "90*15 - 3*15**2 - 200 == 475",
                "Abs((45 - sqrt(45**2 - 3*200))/3 - Rational(242, 100)) < Rational(1, 100)",
                "Abs((45 + sqrt(45**2 - 3*200))/3 - Rational(276, 10)) < Rational(5, 100)",
            ],
        },
    ]


# ===========================================================================
# Assembly
# ===========================================================================
def build():
    lessons = [
        lesson_limits_and_derivative(),
        lesson_power_rule(),
        lesson_increasing_decreasing(),
        lesson_tangents_normals(),
        lesson_stationary_points(),
        lesson_optimisation(),
        lesson_integration(),
        lesson_trapezoidal_rule(),
    ]
    return {
        "slug": "calculus",
        "title": "Calculus",
        "unit": 5,
        "status": "published",
        "blurb": (
            "AI Topic 5, complete: limits and the derivative as a rate of change, the power "
            "rule, increasing and decreasing functions, tangents and normals, stationary points, "
            "optimisation in context, integration and area, and the trapezoidal rule — AI SL 5.1 "
            "to 5.8, taught to markscheme standard."
        ),
        "buildsOn": (
            "Topic 2's graphs and key features, and its straight lines — which supply the "
            "tangent and normal equations. The lessons run 5.1, 5.3, 5.2, 5.4, 5.6, 5.7, 5.5, "
            "5.8: the power rule comes before the sign of the derivative because you cannot read "
            "a sign you cannot compute."
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
