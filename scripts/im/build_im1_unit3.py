#!/usr/bin/env python3
"""Integrated Mathematics 1 — Unit 3: Functions & Sequences.

CCSS Integrated Math I: F-IF.1-3 (function concept, notation, domain; sequences
as functions on a subset of the integers), F-BF.1a and F-BF.2 (write a function
describing a relationship; write arithmetic and geometric sequences both
recursively and explicitly), F-LE.2 (construct linear and exponential functions
from a description, a table, or two points).

This unit is the hinge of IM1. Everything before it manipulates expressions;
everything after it — lines, systems, exponential models, lines of best fit —
is a FUNCTION. Sequences are introduced here rather than as a separate topic
because an arithmetic sequence is a linear function on the whole numbers and a
geometric sequence is an exponential one, which is exactly the pairing Units 4
and 6 go on to develop.

Run: python3 scripts/im/build_im1_unit3.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-1"


# ===========================================================================
# Lesson 1 — F-IF.1: what makes a relation a function
# ===========================================================================
def lesson_what_is_a_function():
    return lesson(
        slug="what-is-a-function",
        title="What Makes a Relation a Function",
        concrete=(
            "A vending machine that returns a different item each time you press B4 is broken. "
            "You would not use it, and no shop would install it. The whole value of the machine is "
            "that one button gives one predictable result. That is not a metaphor for a function — "
            "it is the definition."
        ),
        objective=(
            "Decide whether a relation given as a set of pairs, a table, a graph or a rule is a "
            "function, and justify the decision with the one-output rule or the vertical line test."
        ),
        concept=[
            "**The one-output rule.** A relation from a set of inputs to a set of outputs is a "
            "FUNCTION when every input has exactly one output. Not at least one — exactly one. "
            "The input set is the *domain*, the outputs that actually occur form the *range*.",
            "**Repeated outputs are fine; repeated inputs are not.** The pairs "
            "$(1, 5), (2, 5), (3, 5)$ form a perfectly good function — three different buttons "
            "that happen to dispense the same item. But $(1, 5)$ together with $(1, 8)$ is not a "
            "function: the input $1$ cannot decide what it produces. Ask the question in the right "
            "direction and this never confuses you.",
            "**The vertical line test.** On a graph, a repeated input is a vertical line hitting "
            "the curve twice — two points sharing an $x$ but disagreeing about $y$. So a graph is "
            "a function exactly when no vertical line crosses it more than once. A circle fails "
            "instantly; a parabola opening upward passes.",
            "**Functions arrive in four dresses.** The same function can be a set of ordered "
            "pairs, a table, a graph, or a rule such as $y = 3x - 1$. Being fluent across the four "
            "is most of what F-IF asks for: read a value off a table, find it on a graph, compute "
            "it from the rule, and get the same number three ways.",
            "**Not every equation defines a function.** $y = x^2$ is a function — square any $x$ "
            "and exactly one $y$ comes out. But $x = y^2$ is not, because $x = 9$ admits both "
            "$y = 3$ and $y = -3$. The equation is a perfectly good relation; it just fails the "
            "one-output rule when $x$ is the input.",
        ],
        key_idea=(
            "One input, exactly one output. On a graph that means no vertical line meets the curve "
            "twice. Outputs may repeat freely; inputs may not."
        ),
        facts=[
            fact(
                "Function — the definition",
                "\\text{every } x \\text{ in the domain has exactly one } y",
                "Exactly one, not at least one. This single sentence decides every question in "
                "this lesson.",
            ),
            fact(
                "The vertical line test",
                "\\text{no vertical line meets the graph more than once}",
                "A vertical line is a set of points sharing one x-value. Two hits means one input "
                "with two outputs.",
            ),
            fact(
                "Domain and range",
                "\\text{domain} = \\text{the inputs}, \\qquad \\text{range} = \\text{the outputs "
                "that occur}",
                "The range collects the values actually produced — repeats counted once.",
            ),
        ],
        worked=[
            problem(
                "im1-u3-l1-we1",
                "Is the relation $\\{(1, 4), (2, 7), (3, 4), (5, 9)\\}$ a function? Give its "
                "domain and range.",
                "Check each input for a single output. The inputs are $1, 2, 3, 5$ — all "
                "different, so no input is asked to produce two things. It **is a function**."
                "The output $4$ appears twice, at $x = 1$ and $x = 3$, and that is entirely "
                "allowed: two buttons may dispense the same item."
                "$$\\text{domain} = \\{1, 2, 3, 5\\}, \\qquad \\text{range} = \\{4, 7, 9\\}.$$"
                "The range lists $4$ once — a range is a set of values that occur, not a tally of "
                "how often.",
                [
                    "Eq(len({1, 2, 3, 5}), 4)",
                    "Eq(len({4, 7, 4, 9}), 3)",
                ],
            ),
            problem(
                "im1-u3-l1-we2",
                "Is the relation $\\{(2, 3), (4, 1), (2, 8), (6, 5)\\}$ a function?",
                "Scan the inputs: $2, 4, 2, 6$. The input $2$ appears twice, paired once with $3$ "
                "and once with $8$."
                "$$(2, 3) \\ \\text{and} \\ (2, 8): \\quad 3 \\ne 8.$$"
                "One input, two different outputs — the machine cannot decide. It is **not a "
                "function**."
                "Note that removing either pair would fix it. The relation is not defective in "
                "some deep way; it simply fails the one rule that matters.",
                ["Ne(3, 8)", "Eq(len({2, 4, 2, 6}), 3)"],
            ),
            problem(
                "im1-u3-l1-we3",
                "Does the equation $x = y^2$ define $y$ as a function of $x$?",
                "Test the definition directly: pick an input and see how many outputs it admits. "
                "Take $x = 9$:"
                "$$9 = y^2 \\quad\\Longrightarrow\\quad y = 3 \\ \\text{ or } \\ y = -3.$$"
                "Both work: $3^2 = 9$ and $(-3)^2 = 9$. One input, two outputs, so $y$ is **not** "
                "a function of $x$."
                "Graphically the curve is a parabola lying on its side, and the vertical line "
                "$x = 9$ cuts it at $(9, 3)$ and $(9, -3)$ — the vertical line test fails."
                "Note the contrast with $y = x^2$, which IS a function: squaring an input produces "
                "exactly one output. Same two letters, opposite verdicts, because the roles of "
                "input and output are swapped.",
                [
                    "Eq(3**2, 9)",
                    "Eq((-3)**2, 9)",
                    "Ne(3, -3)",
                ],
            ),
            problem(
                "im1-u3-l1-we4",
                "A shop records $(\\text{kg of rice bought}, \\text{price paid})$ at "
                "$3000$₮ per kg: $(1, 3000), (2, 6000), (3, 9000)$. Is price a function of mass? "
                "Is mass a function of price?",
                "**Price as a function of mass.** Each mass appears once and produces one price, "
                "and the rule $P = 3000m$ gives exactly one output for any input. **Yes**, a "
                "function."
                "**Mass as a function of price.** Turn the pairs around: "
                "$(3000, 1), (6000, 2), (9000, 3)$. Each price also appears once, producing one "
                "mass. **Yes**, also a function — here the reverse works because the price rises "
                "steadily and never repeats."
                "**When the reverse would fail.** If the shop offered a flat $5000$₮ for anything "
                "up to $2$ kg, then $(1, 5000)$ and $(2, 5000)$ would both occur, and asking "
                "\"which mass costs $5000$₮?\" would have two answers. Price would still be a "
                "function of mass, but mass would no longer be a function of price. The direction "
                "of the question decides the verdict.",
                [
                    "Eq(3000*1, 3000)",
                    "Eq(3000*2, 6000)",
                    "Eq(3000*3, 9000)",
                    "Ne(1, 2)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Calling {(1,5), (2,5), (3,5)} 'not a function' because the output repeats.",
                "Repeated OUTPUTS are fine — several inputs may share a result. Only a repeated "
                "input with different outputs breaks the rule.",
            ),
            mistake(
                "Applying a horizontal line test to decide whether a graph is a function.",
                "The vertical line test decides function-hood. The horizontal line test answers a "
                "different question (whether the inverse is a function).",
            ),
            mistake(
                "Assuming any equation in x and y defines y as a function of x.",
                "x = y² does not: x = 9 gives y = 3 and y = −3. Always test by fixing an input and "
                "counting the outputs.",
            ),
            mistake(
                "Listing a repeated value twice in the range.",
                "A range is a set of values that occur. {4, 7, 4, 9} is written {4, 7, 9}.",
            ),
        ],
        try_it=[
            problem(
                "im1-u3-l1-t1",
                "Is $\\{(0, 2), (1, 3), (2, 2), (3, 5)\\}$ a function? Give the range.",
                "The inputs $0, 1, 2, 3$ are all different, so yes, it is a function. The output "
                "$2$ occurs twice, which is allowed. The range is $\\{2, 3, 5\\}$.",
                ["Eq(len({0, 1, 2, 3}), 4)", "Eq(len({2, 3, 2, 5}), 3)"],
            ),
            problem(
                "im1-u3-l1-t2",
                "Is $\\{(5, 1), (7, 2), (5, 9)\\}$ a function? Explain.",
                "No. The input $5$ appears with two different outputs, $1$ and $9$, so it fails "
                "the one-output rule.",
                ["Ne(1, 9)", "Eq(len({5, 7, 5}), 2)"],
            ),
            problem(
                "im1-u3-l1-t3",
                "A circle of radius $5$ centred at the origin has equation $x^2 + y^2 = 25$. Is "
                "$y$ a function of $x$?",
                "No. At $x = 3$, $y^2 = 25 - 9 = 16$, so $y = 4$ or $y = -4$ — two outputs for one "
                "input. A vertical line through $x = 3$ cuts the circle twice.",
                [
                    "Eq(3**2 + 4**2, 25)",
                    "Eq(3**2 + (-4)**2, 25)",
                    "Ne(4, -4)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "F-IF.1",
                "title": "One input, exactly one output",
                "body": (
                    "That is the whole definition. A machine whose button B4 sometimes gives crisps "
                    "and sometimes gives chocolate is broken — and a relation that lets one input "
                    "produce two outputs is not a function."
                ),
                "beats": [
                    "Every input gets **exactly one** output",
                    "The inputs form the **domain**",
                    "The outputs that occur form the **range**",
                    "Ask the question input-first, always",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "The direction that matters",
                "title": "Outputs may repeat; inputs may not",
                "body": (
                    "$(1,5), (2,5), (3,5)$ is a function — three buttons, one item. "
                    "$(1,5), (1,8)$ is not — one button, two items. The rule is about inputs "
                    "having a single destination, never about outputs being distinct."
                ),
            },
            {"kind": "worked", "title": "A function with a repeated output", "problemId": "im1-u3-l1-we1"},
            tap(
                "Function or not?",
                "Is $\\{(3, 1), (4, 1), (5, 1), (6, 1)\\}$ a function?",
                [
                    "Yes — every input has exactly one output",
                    "No — the output $1$ repeats",
                    "No — the range has only one element",
                    "Only if the domain is restricted",
                ],
                0,
                "The inputs $3, 4, 5, 6$ are all different and each produces exactly one output, "
                "so it is a function — a constant one. A repeated output is not a problem; four "
                "buttons dispensing the same item is a working machine, just a boring one.",
                ["Eq(len({3, 4, 5, 6}), 4)", "Eq(len({1}), 1)"],
            ),
            {"kind": "worked", "title": "When it fails", "problemId": "im1-u3-l1-we2"},
            {
                "kind": "teach",
                "eyebrow": "F-IF.1 on a graph",
                "title": "The vertical line test",
                "body": (
                    "A vertical line collects every point sharing one $x$-value. If it meets the "
                    "graph twice, that single input has two outputs. So: a graph is a function "
                    "exactly when no vertical line crosses it more than once."
                ),
            },
            {
                "kind": "coordinateGrid",
                "eyebrow": "See the failure",
                "title": "Two points, same x",
                "teach": (
                    "Plotted here are $(3, 4)$ and $(3, -4)$ — both on the circle "
                    "$x^2 + y^2 = 25$. They sit on the same vertical line, so the input $3$ has "
                    "two outputs and the circle is not a function."
                ),
                "config": {
                    "mode": "plot",
                    "min": -6,
                    "max": 6,
                    "points": [
                        {"x": 3, "y": 4, "label": "(3, 4)"},
                        {"x": 3, "y": -4, "label": "(3, -4)"},
                    ],
                },
            },
            {"kind": "worked", "title": "x = y² fails; y = x² passes", "problemId": "im1-u3-l1-we3"},
            tap(
                "Which graph is a function?",
                "Which of these graphs passes the vertical line test?",
                [
                    "A circle centred at the origin",
                    "A parabola opening upward",
                    "A parabola opening to the right",
                    "A horizontal figure-eight",
                ],
                1,
                "An upward parabola such as $y = x^2$ takes any $x$ and returns exactly one $y$ — "
                "no vertical line meets it twice. The circle and the sideways parabola both have "
                "vertical lines cutting them at two points, and a figure-eight is worse. "
                "Check the parabola at $x = 3$: $y = 9$, and only $9$.",
                ["Eq(3**2, 9)", "Eq((-3)**2, 9)", "Ne(3, -3)"],
            ),
            {
                "kind": "teach",
                "eyebrow": "F-IF.1",
                "title": "Four dresses, one function",
                "body": (
                    "Ordered pairs, a table, a graph, a rule — the same function wearing different "
                    "clothes. Fluency means reading a value off a table, locating it on the graph, "
                    "and computing it from the rule, and getting the same number all three ways."
                ),
            },
            {"kind": "worked", "title": "Which direction are you asking?", "problemId": "im1-u3-l1-we4"},
            {
                "kind": "tip",
                "title": "Test by fixing an input",
                "body": (
                    "Faced with any relation, pick one specific input and ask how many outputs it "
                    "admits. If the honest answer is 'two', you are done — it is not a function, "
                    "and you have the counterexample to prove it."
                ),
            },
            {"kind": "tryIt", "title": "Your turn — function or not", "problemId": "im1-u3-l1-t1"},
            {"kind": "tryIt", "title": "Your turn — a circle", "problemId": "im1-u3-l1-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "A function gives every input **exactly one** output",
                    "Repeated outputs are fine; repeated inputs with different outputs are not",
                    "Vertical line test: no vertical line meets the graph twice",
                    "Domain = the inputs; range = the outputs that occur, listed once each",
                    "Test any relation by fixing an input and counting outputs",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 2 — F-IF.1, F-IF.2, F-IF.5: notation, domain, range
# ===========================================================================
def lesson_notation():
    return lesson(
        slug="function-notation-domain-and-range",
        title="Function Notation, Domain & Range",
        concrete=(
            "A parking meter charges by the hour. Ask it \"what do three hours cost?\" and you get "
            "one number back. Writing $C(3)$ is just that question in symbols: the name of the "
            "machine, then the input in brackets. It is not $C$ multiplied by $3$ — a point worth "
            "settling now, because that misreading survives into calculus if you let it."
        ),
        objective=(
            "Read and write function notation, evaluate a function at a numerical or algebraic "
            "input, and determine the domain and range from a rule, a graph, or a real situation."
        ),
        concept=[
            "**The brackets hold an input, not a multiplication.** The value $f(x)$ is what comes out. The symbol $f$ is the machine's name and "
            "$x$ is what you feed it; $f(x)$ is what comes out. So $f(3)$ means \"the output when "
            "the input is $3$\". Reading it as $f$ times $3$ is the single most persistent "
            "misconception in all of algebra, and it makes every later line nonsense.",
            "**Evaluating is substitution, with brackets.** If $f(x) = 2x^2 - 5$, then "
            "$f(-3) = 2(-3)^2 - 5 = 2(9) - 5 = 13$. Wrap the substituted value in brackets before "
            "computing — without them, $2 \\cdot -3^2$ reads as $-18$ and the sign is lost. The "
            "brackets are not decoration; they carry the sign through the exponent.",
            "**You can feed a function an expression.** $f(x + 1)$ means: put $x + 1$ everywhere "
            "$x$ appeared. For $f(x) = 3x - 4$, $f(x+1) = 3(x+1) - 4 = 3x - 1$. This is how "
            "sequences, transformations and rates of change all get written, so it is worth being "
            "comfortable with early.",
            "**Domain: what may go in.** From a RULE, the domain is everything except inputs that "
            "break the arithmetic — you may not divide by zero, and (in this course) you may not "
            "take the square root of a negative. So $f(x) = \\frac{1}{x-2}$ has domain all reals "
            "except $2$, and $g(x) = \\sqrt{x - 5}$ has domain $x \\ge 5$.",
            "**Context overrides algebra.** A model has a domain the SITUATION allows, not the one "
            "the formula tolerates. $V = 450 - 12t$ makes arithmetic sense at $t = -100$ and at "
            "$t = 1000$, but a tank cannot drain before you start or below empty, so the real "
            "domain is $0 \\le t \\le 37.5$. Stating that restriction is part of the answer, not "
            "an afterthought.",
            "**Range: what actually comes out.** Feed the whole domain in and collect the outputs. "
            "For $f(x) = x^2$ over all reals the range is $f(x) \\ge 0$, because a square is never "
            "negative. For a linear function over all reals the range is all reals — a line "
            "eventually reaches every height.",
        ],
        key_idea=(
            "$f(3)$ is the output at input $3$, never $f$ times $3$. Substitute in brackets. The "
            "domain is what may go in — restricted by the arithmetic and, in a model, by the "
            "situation; the range is what comes out."
        ),
        facts=[
            fact(
                "Notation",
                "f(a) = \\text{the output of } f \\text{ when the input is } a",
                "The brackets hold the input. They never mean multiplication.",
            ),
            fact(
                "Substitute in brackets",
                "f(x) = 2x^2 - 5: \\quad f(-3) = 2(-3)^2 - 5 = 13",
                "Wrapping the value in brackets keeps the sign inside the exponent, where it "
                "belongs.",
            ),
            fact(
                "The two domain breakers",
                "\\frac{1}{x - a}: x \\ne a \\qquad \\sqrt{x - a}: x \\ge a",
                "Division by zero and even roots of negatives are the only two restrictions this "
                "course imposes from the rule alone.",
            ),
        ],
        worked=[
            problem(
                "im1-u3-l2-we1",
                "For $f(x) = 2x^2 - 5$, find $f(3)$, $f(-3)$ and $f(0)$.",
                "Substitute each input, in brackets."
                "$$f(3) = 2(3)^2 - 5 = 2(9) - 5 = 18 - 5 = 13.$$"
                "$$f(-3) = 2(-3)^2 - 5 = 2(9) - 5 = 13.$$"
                "$$f(0) = 2(0)^2 - 5 = -5.$$"
                "Note $f(3)$ and $f(-3)$ agree: squaring destroys the sign, so opposite inputs give "
                "the same output. That is a repeated OUTPUT, which is perfectly legal — the "
                "function is still a function. Without the brackets, $2 \\cdot -3^2$ would read as "
                "$-18$ and give the wrong answer $-23$.",
                [
                    "Eq(2*3**2 - 5, 13)",
                    "Eq(2*(-3)**2 - 5, 13)",
                    "Eq(2*0**2 - 5, -5)",
                ],
            ),
            problem(
                "im1-u3-l2-we2",
                "For $g(x) = 3x - 4$, find $g(x + 1)$ and simplify. Then find $g(x+1) - g(x)$.",
                "Feed the whole expression $x + 1$ into the machine, replacing every $x$:"
                "$$g(x + 1) = 3(x + 1) - 4 = 3x + 3 - 4 = 3x - 1.$$"
                "Now the difference:"
                "$$g(x+1) - g(x) = (3x - 1) - (3x - 4) = 3.$$"
                "The answer is a constant $3$ — moving one step to the right always raises the "
                "output by exactly $3$, whatever $x$ was. That constant step is the defining "
                "feature of a linear function, and it is the number Unit 4 will call the slope."
                "**Check numerically.** $g(5) = 11$ and $g(6) = 14$; the gap is $3$ ✓",
                [
                    "Eq(simplify(3*(Symbol('x') + 1) - 4), 3*Symbol('x') - 1)",
                    "Eq(simplify((3*(Symbol('x')+1) - 4) - (3*Symbol('x') - 4)), 3)",
                    "Eq(3*6 - 4 - (3*5 - 4), 3)",
                ],
            ),
            problem(
                "im1-u3-l2-we3",
                "State the domain of $f(x) = \\dfrac{1}{x - 2}$ and of $g(x) = \\sqrt{x - 5}$.",
                "**The rational function.** The only illegal move is dividing by zero, so exclude the input that "
                "makes the denominator vanish:"
                "$$x - 2 = 0 \\quad\\Longrightarrow\\quad x = 2.$$"
                "The domain is every real number except $2$. Everything else is fine: "
                "$f(3) = 1$, $f(1) = -1$, $f(2.5) = 2$."
                "**The square root.** In this course a square root needs a non-negative input:"
                "$$x - 5 \\ge 0 \\quad\\Longrightarrow\\quad x \\ge 5.$$"
                "The domain is $x \\ge 5$. Check the boundary: $g(5) = \\sqrt{0} = 0$, which is "
                "defined, so $5$ belongs. And $g(9) = \\sqrt{4} = 2$ ✓",
                [
                    "Eq(1/(3 - 2), 1)",
                    "Eq(1/(1 - 2), -1)",
                    "Eq(sqrt(5 - 5), 0)",
                    "Eq(sqrt(9 - 5), 2)",
                ],
            ),
            problem(
                "im1-u3-l2-we4",
                "A candle is $24$ cm tall and burns $4$ cm per hour, so $h(t) = 24 - 4t$. Find "
                "$h(3)$, and state the domain and range that the situation allows.",
                "**Evaluate.**"
                "$$h(3) = 24 - 4(3) = 24 - 12 = 12\\ \\text{cm}.$$"
                "After three hours the candle is $12$ cm tall."
                "**Domain.** Arithmetic would accept any $t$, but the situation will not. Time "
                "cannot be negative, so $t \\ge 0$; and the candle cannot have negative height, so"
                "$$24 - 4t \\ge 0 \\quad\\Longrightarrow\\quad t \\le 6.$$"
                "The domain is $0 \\le t \\le 6$ hours."
                "**Range.** Over that domain the height starts at $h(0) = 24$ and falls steadily "
                "to $h(6) = 0$, so the range is $0 \\le h \\le 24$ cm."
                "Stating both is the difference between a formula and a model: $h(-2) = 32$ is "
                "arithmetic, but it describes nothing.",
                [
                    "Eq(24 - 4*3, 12)",
                    "Eq(24 - 4*0, 24)",
                    "Eq(24 - 4*6, 0)",
                    "24 - 4*7 < 0",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading f(3) as f multiplied by 3.",
                "The brackets hold the INPUT. f(3) is the output when you feed in 3; there is no "
                "multiplication anywhere in the notation.",
            ),
            mistake(
                "Substituting a negative without brackets: writing f(−3) = 2·−3² − 5 = −23.",
                "Write 2(−3)² − 5. The brackets keep the minus inside the square, giving 2(9) − 5 "
                "= 13.",
            ),
            mistake(
                "Giving a model's domain as 'all real numbers' because the formula allows it.",
                "A model's domain is what the situation allows. A candle burns for 6 hours, so the "
                "domain is 0 ≤ t ≤ 6 — negative time and negative height describe nothing.",
            ),
            mistake(
                "Replacing only the first x when evaluating f(x + 1).",
                "Every occurrence of x becomes the new expression. For f(x) = x² + x, "
                "f(x+1) = (x+1)² + (x+1).",
            ),
        ],
        try_it=[
            problem(
                "im1-u3-l2-t1",
                "For $f(x) = 5 - 3x$, find $f(4)$, $f(-2)$ and $f(0)$.",
                "$f(4) = 5 - 12 = -7$; $f(-2) = 5 - 3(-2) = 5 + 6 = 11$; $f(0) = 5$.",
                [
                    "Eq(5 - 3*4, -7)",
                    "Eq(5 - 3*(-2), 11)",
                    "Eq(5 - 3*0, 5)",
                ],
            ),
            problem(
                "im1-u3-l2-t2",
                "For $h(x) = x^2 - 2x$, find $h(5)$ and $h(-1)$.",
                "$h(5) = 25 - 10 = 15$; $h(-1) = (-1)^2 - 2(-1) = 1 + 2 = 3$. The brackets matter "
                "in both places of the second one.",
                [
                    "Eq(5**2 - 2*5, 15)",
                    "Eq((-1)**2 - 2*(-1), 3)",
                ],
            ),
            problem(
                "im1-u3-l2-t3",
                "State the domain of $f(x) = \\dfrac{x + 1}{x - 7}$ and evaluate $f(9)$.",
                "The denominator vanishes at $x = 7$, so the domain is all reals except $7$. "
                "$f(9) = \\frac{10}{2} = 5$.",
                [
                    "Eq(Rational(9 + 1, 9 - 7), 5)",
                    "Eq(9 - 7, 2)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "F-IF.2",
                "title": "f(3) is an output, not a product",
                "body": (
                    "$f$ names the machine; the brackets hold what you feed it. $f(3)$ asks \"what "
                    "comes out when $3$ goes in?\" There is no multiplication in the notation, and "
                    "believing otherwise breaks everything downstream."
                ),
                "beats": [
                    "$f$ — the machine's name",
                    "$f(3)$ — feed it $3$",
                    "The result is one number",
                    "**Never** $f \\times 3$",
                ],
            },
            {
                "kind": "evaluator",
                "eyebrow": "Feed it and watch",
                "title": "One input in, one output out",
                "teach": (
                    "Drag the input for $f(x) = 3x + 2$. Every position of the slider produces "
                    "exactly one output — which is the definition of a function, made visible."
                ),
                "config": {"a": 3, "b": 2, "varName": "x", "min": -5, "max": 8, "start": 2},
            },
            {
                "kind": "tip",
                "title": "Always substitute in brackets",
                "body": (
                    "$f(-3)$ for $f(x) = 2x^2 - 5$ is $2(-3)^2 - 5 = 13$. Without brackets, "
                    "$2 \\cdot -3^2$ evaluates the square first and then applies the minus, giving "
                    "$-18$ and the wrong answer. One pair of brackets, every time."
                ),
            },
            {"kind": "worked", "title": "Three inputs, brackets throughout", "problemId": "im1-u3-l2-we1"},
            tap(
                "Evaluate with care",
                "If $f(x) = x^2 + 4x$, what is $f(-2)$?",
                ["$-4$", "$12$", "$4$", "$-12$"],
                0,
                "$f(-2) = (-2)^2 + 4(-2) = 4 - 8 = -4$. The square of $-2$ is positive $4$; the "
                "second term is negative $8$. Dropping the brackets on the first term would give "
                "$-4 - 8 = -12$, which is the trap answer.",
                [
                    "Eq((-2)**2 + 4*(-2), -4)",
                    "Eq((-2)**2, 4)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "F-IF.2",
                "title": "The input can be an expression",
                "body": (
                    "$f(x+1)$ means: put $x + 1$ wherever $x$ appeared — EVERY occurrence. For "
                    "$g(x) = 3x - 4$ that gives $g(x+1) = 3(x+1) - 4 = 3x - 1$. This is how a "
                    "step forward gets written, and Unit 4 will lean on it."
                ),
            },
            {"kind": "worked", "title": "A step forward, and its size", "problemId": "im1-u3-l2-we2"},
            {
                "kind": "teach",
                "eyebrow": "F-IF.5",
                "title": "Domain: what may go in",
                "body": (
                    "From a rule, the domain is everything except the inputs that break the "
                    "arithmetic. This course has exactly two breakers: a zero denominator, and a "
                    "negative under an even root."
                ),
                "beats": [
                    "$\\frac{1}{x-2}$ → all reals except $x = 2$",
                    "$\\sqrt{x-5}$ → $x \\ge 5$",
                    "Polynomials → all real numbers",
                    "Then ask what the **situation** allows",
                ],
            },
            {"kind": "worked", "title": "Two rules, two restrictions", "problemId": "im1-u3-l2-we3"},
            tap(
                "What is the domain here?",
                "What is the domain of $f(x) = \\dfrac{5}{x + 3}$?",
                [
                    "all real numbers",
                    "all real numbers except $3$",
                    "all real numbers except $-3$",
                    "$x \\ge -3$",
                ],
                2,
                "The denominator $x + 3$ is zero when $x = -3$, so that one input must be "
                "excluded; everything else is fine. Check a nearby legal value: "
                "$f(-2) = \\frac{5}{1} = 5$ ✓. The trap is excluding $+3$ instead — solve "
                "$x + 3 = 0$, do not read the sign off the page.",
                [
                    "Eq(-3 + 3, 0)",
                    "Eq(Rational(5, -2 + 3), 5)",
                    "Ne(3 + 3, 0)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "The modelling rule",
                "title": "Context beats arithmetic",
                "body": (
                    "$h(t) = 24 - 4t$ happily returns $32$ at $t = -2$, but a candle cannot burn "
                    "before it is lit. A model's domain is what the SITUATION permits — here "
                    "$0 \\le t \\le 6$ — and saying so is part of the answer."
                ),
            },
            {"kind": "worked", "title": "A candle's real domain and range", "problemId": "im1-u3-l2-we4"},
            {"kind": "tryIt", "title": "Your turn — evaluate three times", "problemId": "im1-u3-l2-t1"},
            {"kind": "tryIt", "title": "Your turn — a domain restriction", "problemId": "im1-u3-l2-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "$f(3)$ is the output at input $3$ — never a multiplication",
                    "Substitute in brackets so signs survive exponents",
                    "$f(x+1)$ replaces **every** $x$ with $x+1$",
                    "Domain breakers: zero denominator, negative under an even root",
                    "In a model the domain is what the situation allows, and you must say so",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 3 — F-IF.3, F-BF.2, F-LE.2: arithmetic sequences
# ===========================================================================
def lesson_arithmetic():
    return lesson(
        slug="arithmetic-sequences",
        title="Arithmetic Sequences",
        concrete=(
            "A stack of chairs is $80$ cm tall, and every extra chair adds $9$ cm. The heights go "
            "$80, 89, 98, 107, \\dots$ — a fixed amount added each time. That is an arithmetic "
            "sequence, and the reason it belongs in a unit about functions is that it IS one: feed "
            "it a chair number and it returns a height."
        ),
        objective=(
            "Recognise an arithmetic sequence by its constant difference, write it both recursively "
            "and explicitly, find any term without listing the ones before it, and read the "
            "sequence as a linear function on the whole numbers."
        ),
        concept=[
            "**A sequence is a function whose domain is the counting numbers.** The first term is "
            "the output at $n = 1$, the second at $n = 2$, and so on. Writing $a_n$ instead of "
            "$a(n)$ is a notational habit, nothing more — a sequence is a function that only "
            "accepts whole-number inputs.",
            "**Arithmetic means a constant DIFFERENCE.** Subtract each term from the next; if you "
            "always get the same number $d$, the sequence is arithmetic. In "
            "$80, 89, 98, 107$ the differences are $9, 9, 9$, so $d = 9$. If the differences "
            "change, the sequence is not arithmetic and none of this lesson's formulas apply.",
            "**The recursive rule says how to take one step.** "
            "$$a_1 = 80, \\qquad a_n = a_{n-1} + 9.$$ "
            "It is honest about the process — each term is the previous one plus $d$ — but "
            "useless for finding the $200$th term, because you would have to walk all $199$ steps "
            "to get there.",
            "**The explicit rule jumps straight there.** Starting at $a_1$ and taking $n-1$ steps "
            "of size $d$: "
            "$$a_n = a_1 + (n-1)d.$$ "
            "The $(n-1)$ is the whole point and the whole trap. The FIRST term has taken zero "
            "steps, so $a_1 = a_1 + 0 \\cdot d$ ✓. Writing $a_1 + nd$ instead lands you one term "
            "too far every single time.",
            "**An arithmetic sequence is a linear function on the whole numbers.** Rearranging, "
            "$a_n = dn + (a_1 - d)$ — a constant times $n$ plus a fixed number, which is exactly "
            "the shape $y = mx + b$ of Unit 4. The common difference $d$ IS the slope. The graph "
            "is a row of dots sitting on a straight line, and the only reason it is dots rather "
            "than a line is that the domain is whole numbers.",
            "**Two terms determine the whole sequence.** Given $a_4 = 23$ and $a_9 = 48$, the "
            "gap is $48 - 23 = 25$ across $9 - 4 = 5$ steps, so $d = 5$. Then back up from any "
            "known term to find $a_1$. This is the same 'two points determine a line' fact you "
            "will meet formally in Unit 4.",
        ],
        key_idea=(
            "Constant difference $d$. Recursive: $a_n = a_{n-1} + d$. Explicit: "
            "$a_n = a_1 + (n-1)d$ — $n-1$ steps, because the first term has taken none. It is a "
            "linear function with slope $d$."
        ),
        facts=[
            fact(
                "Recursive form",
                "a_1 = \\text{first term}, \\qquad a_n = a_{n-1} + d",
                "Describes the process: each term is the last one plus the common difference.",
            ),
            fact(
                "Explicit form",
                "a_n = a_1 + (n-1)d",
                "Jumps to any term directly. The (n−1) counts STEPS taken, and the first term has "
                "taken zero.",
            ),
            fact(
                "The common difference from two terms",
                "d = \\frac{a_q - a_p}{q - p}",
                "Total change divided by the number of steps between them — the slope formula, "
                "meeting you a unit early.",
            ),
        ],
        worked=[
            problem(
                "im1-u3-l3-we1",
                "For the sequence $80, 89, 98, 107, \\dots$, find the common difference, write the "
                "recursive and explicit rules, and find the $12$th term.",
                "**Common difference.** Subtract consecutive terms:"
                "$$89 - 80 = 9, \\quad 98 - 89 = 9, \\quad 107 - 98 = 9.$$"
                "Constant, so it is arithmetic with $d = 9$."
                "**Recursive rule.**"
                "$$a_1 = 80, \\qquad a_n = a_{n-1} + 9.$$"
                "**Explicit rule.**"
                "$$a_n = 80 + (n-1)(9) = 9n + 71.$$"
                "Sanity-check on a known term: $a_1 = 9(1) + 71 = 80$ ✓ and "
                "$a_3 = 27 + 71 = 98$ ✓."
                "**Twelfth term.**"
                "$$a_{12} = 9(12) + 71 = 108 + 71 = 179.$$"
                "Had you used $80 + 12(9) = 188$ you would be one term too far — that is the "
                "$(n-1)$ trap, and checking against $a_1$ catches it immediately.",
                [
                    "Eq(89 - 80, 9)",
                    "Eq(107 - 98, 9)",
                    "Eq(80 + (1-1)*9, 80)",
                    "Eq(80 + (3-1)*9, 98)",
                    "Eq(80 + (12-1)*9, 179)",
                    "Eq(9*12 + 71, 179)",
                ],
            ),
            problem(
                "im1-u3-l3-we2",
                "An arithmetic sequence has $a_4 = 23$ and $a_9 = 48$. Find $d$, $a_1$, and the "
                "explicit rule.",
                "**Common difference.** From term $4$ to term $9$ is $9 - 4 = 5$ steps, and the value rose "
                "by $48 - 23 = 25$:"
                "$$d = \\frac{25}{5} = 5.$$"
                "**First term.** Back up three steps from $a_4$:"
                "$$a_1 = a_4 - 3d = 23 - 15 = 8.$$"
                "**Explicit rule.**"
                "$$a_n = 8 + (n-1)(5) = 5n + 3.$$"
                "**Check both given terms.** $a_4 = 5(4) + 3 = 23$ ✓ and $a_9 = 45 + 3 = 48$ ✓. "
                "Checking against BOTH given values is what confirms $d$ and $a_1$ together — one "
                "check could pass with a wrong pair.",
                [
                    "Eq(Rational(48 - 23, 9 - 4), 5)",
                    "Eq(23 - 3*5, 8)",
                    "Eq(5*4 + 3, 23)",
                    "Eq(5*9 + 3, 48)",
                ],
            ),
            problem(
                "im1-u3-l3-we3",
                "A theatre has $18$ seats in row $1$ and $3$ more in each row after. How many seats "
                "in row $20$, and which row first has at least $60$ seats?",
                "**Model.** Seats in row $n$: $a_1 = 18$, $d = 3$, so"
                "$$a_n = 18 + (n-1)(3) = 3n + 15.$$"
                "Check row $1$: $3 + 15 = 18$ ✓."
                "**Row 20.**"
                "$$a_{20} = 3(20) + 15 = 75\\ \\text{seats}.$$"
                "**First row with at least 60.** Solve the inequality:"
                "$$3n + 15 \\ge 60 \\quad\\Longrightarrow\\quad 3n \\ge 45 \\quad\\Longrightarrow"
                "\\quad n \\ge 15.$$"
                "Row numbers are whole, so row $15$ is the first. Check: row $15$ has "
                "$3(15) + 15 = 60$ seats ✓ (exactly at the threshold, which $\\ge$ allows), while "
                "row $14$ has $57$ ✗.",
                [
                    "Eq(3*1 + 15, 18)",
                    "Eq(3*20 + 15, 75)",
                    "Eq(3*15 + 15, 60)",
                    "3*15 + 15 >= 60",
                    "Not(3*14 + 15 >= 60)",
                ],
            ),
            problem(
                "im1-u3-l3-we4",
                "Show that $2, 6, 18, 54$ is NOT arithmetic, and identify what kind of pattern it "
                "is.",
                "Test for a constant difference:"
                "$$6 - 2 = 4, \\qquad 18 - 6 = 12, \\qquad 54 - 18 = 36.$$"
                "The differences $4, 12, 36$ are not constant, so the sequence is **not "
                "arithmetic** and $a_n = a_1 + (n-1)d$ does not apply to it."
                "But look at the RATIOS instead:"
                "$$\\frac{6}{2} = 3, \\qquad \\frac{18}{6} = 3, \\qquad \\frac{54}{18} = 3.$$"
                "Constant ratio $3$ — each term is the previous one MULTIPLIED by $3$. That is a "
                "geometric sequence, and it is the subject of the next lesson."
                "**The habit worth keeping.** Always test differences first; if they fail, test "
                "ratios. Between them they identify almost every sequence you will meet in IM1.",
                [
                    "Eq(6 - 2, 4)",
                    "Eq(18 - 6, 12)",
                    "Ne(4, 12)",
                    "Eq(Rational(6,2), 3)",
                    "Eq(Rational(18,6), 3)",
                    "Eq(Rational(54,18), 3)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Using aₙ = a₁ + nd instead of a₁ + (n−1)d.",
                "Test on the first term: a₁ must come out as a₁, so the step count at n = 1 has to "
                "be zero. That forces (n−1).",
            ),
            mistake(
                "Computing d as a₉ − a₄ without dividing by the number of steps.",
                "From term 4 to term 9 is 5 steps, so d = (48 − 23)/5 = 5, not 25.",
            ),
            mistake(
                "Applying the arithmetic formula to a sequence with changing differences.",
                "Check that the differences are actually constant first. 2, 6, 18, 54 has "
                "differences 4, 12, 36 — it is geometric, not arithmetic.",
            ),
            mistake(
                "Treating the recursive rule as a way to reach a distant term.",
                "aₙ = aₙ₋₁ + d needs every earlier term. Use the explicit rule to jump straight to "
                "a₂₀₀.",
            ),
        ],
        try_it=[
            problem(
                "im1-u3-l3-t1",
                "For $7, 11, 15, 19, \\dots$ write the explicit rule and find $a_{10}$.",
                "The common difference is $4$ and $a_1 = 7$, so "
                "$a_n = 7 + (n-1)(4) = 4n + 3$. Check $a_1 = 7$ ✓. Then "
                "$a_{10} = 40 + 3 = 43$.",
                [
                    "Eq(11 - 7, 4)",
                    "Eq(4*1 + 3, 7)",
                    "Eq(4*10 + 3, 43)",
                ],
            ),
            problem(
                "im1-u3-l3-t2",
                "An arithmetic sequence has $a_1 = 100$ and $d = -6$. Find $a_{15}$ and the first "
                "negative term.",
                "$a_n = 100 + (n-1)(-6) = 106 - 6n$. Then $a_{15} = 106 - 90 = 16$. For the first "
                "negative term solve $106 - 6n < 0$, giving $n > \\frac{106}{6} \\approx 17.67$, "
                "so $n = 18$: $a_{18} = 106 - 108 = -2$, while $a_{17} = 4$ is still positive.",
                [
                    "Eq(106 - 6*1, 100)",
                    "Eq(106 - 6*15, 16)",
                    "106 - 6*18 < 0",
                    "Not(106 - 6*17 < 0)",
                ],
            ),
            problem(
                "im1-u3-l3-t3",
                "An arithmetic sequence has $a_3 = 14$ and $a_7 = 34$. Find $d$ and $a_1$.",
                "From term $3$ to term $7$ is $4$ steps and the value rose by $20$, so "
                "$d = \\frac{20}{4} = 5$. Backing up two steps from $a_3$: "
                "$a_1 = 14 - 10 = 4$. Check: $a_n = 5n - 1$ gives $a_3 = 14$ ✓ and $a_7 = 34$ ✓.",
                [
                    "Eq(Rational(34 - 14, 7 - 3), 5)",
                    "Eq(14 - 2*5, 4)",
                    "Eq(5*3 - 1, 14)",
                    "Eq(5*7 - 1, 34)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "F-IF.3",
                "title": "A sequence is a function on the counting numbers",
                "body": (
                    "Feed it $1$ and get the first term; feed it $2$ and get the second. Writing "
                    "$a_n$ rather than $a(n)$ is a habit of notation — everything you learned about "
                    "functions still applies, with the domain restricted to whole numbers."
                ),
            },
            {
                "kind": "teach",
                "eyebrow": "F-BF.2",
                "title": "Arithmetic = a constant difference",
                "body": (
                    "Subtract each term from the next. Always the same number? Then the sequence is "
                    "arithmetic and that number is $d$. In $80, 89, 98, 107$ every difference is "
                    "$9$."
                ),
                "beats": [
                    "$89 - 80 = 9$",
                    "$98 - 89 = 9$",
                    "$107 - 98 = 9$",
                    "Constant → arithmetic, $d = 9$",
                ],
            },
            {
                "kind": "evaluator",
                "eyebrow": "Feel the constant step",
                "title": "Same amount added, every step",
                "teach": (
                    "Drag the term number in $4n + 3$. Every step of $1$ moves the total by "
                    "exactly $4$ — never more, never less. That unchanging step is the common "
                    "difference, and it is why an arithmetic sequence turns out to be a linear "
                    "function."
                ),
                "config": {"a": 4, "b": 3, "varName": "n", "min": 1, "max": 10, "start": 1},
            },
            {
                "kind": "teach",
                "eyebrow": "Two rules, two jobs",
                "title": "Recursive describes; explicit computes",
                "body": (
                    "The recursive rule $a_n = a_{n-1} + d$ is honest about the process but forces "
                    "you to walk. The explicit rule $a_n = a_1 + (n-1)d$ teleports you to any term "
                    "at all — which is what you want for term $200$."
                ),
                "beats": [
                    "Recursive: $a_1 = 80$, $a_n = a_{n-1} + 9$",
                    "Explicit: $a_n = 80 + (n-1)(9)$",
                    "$(n-1)$ counts **steps taken**",
                    "The first term has taken **zero** steps",
                ],
            },
            {"kind": "worked", "title": "A stack of chairs", "problemId": "im1-u3-l3-we1"},
            tap(
                "Why n minus one?",
                "For $a_1 = 5$ and $d = 4$, what does $a_1 + n\\,d$ give at $n = 1$, and why is "
                "that wrong?",
                [
                    "$9$ — it is one step too far",
                    "$5$ — it is correct",
                    "$4$ — it forgets the first term",
                    "$1$ — it counts from zero",
                ],
                0,
                "$a_1 + 1 \\cdot 4 = 9$, but the first term is $5$. The formula has taken a step "
                "before the sequence started. The correct explicit rule "
                "$a_1 + (n-1)d$ gives $5 + 0 \\cdot 4 = 5$ ✓ — testing at $n = 1$ catches this "
                "error every time.",
                [
                    "Eq(5 + 1*4, 9)",
                    "Eq(5 + (1-1)*4, 5)",
                    "Ne(9, 5)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "F-LE.2",
                "title": "It is a linear function in disguise",
                "body": (
                    "Expand the explicit rule: $a_n = a_1 + (n-1)d = dn + (a_1 - d)$. A constant "
                    "times $n$, plus a fixed number — the shape $y = mx + b$. The common difference "
                    "IS the slope, and the graph is dots sitting on a straight line."
                ),
            },
            {
                "kind": "coordinateGrid",
                "eyebrow": "The dots line up",
                "title": "Plot the first four terms",
                "teach": (
                    "The sequence $5, 9, 13, 17$ plotted as $(n, a_n)$. The points sit perfectly on "
                    "a line of slope $4$ — the common difference. It is dots rather than a "
                    "continuous line only because the domain is whole numbers."
                ),
                "config": {
                    "mode": "plot",
                    "min": 0,
                    "max": 18,
                    "points": [
                        {"x": 1, "y": 5},
                        {"x": 2, "y": 9},
                        {"x": 3, "y": 13},
                        {"x": 4, "y": 17},
                    ],
                },
            },
            {"kind": "worked", "title": "Two terms determine everything", "problemId": "im1-u3-l3-we2"},
            tap(
                "Find the common difference",
                "An arithmetic sequence has $a_2 = 11$ and $a_8 = 41$. What is $d$?",
                ["$30$", "$6$", "$5$", "$3$"],
                2,
                "From term $2$ to term $8$ is $8 - 2 = 6$ steps, and the value rose by "
                "$41 - 11 = 30$. So $d = \\frac{30}{6} = 5$. Answering $30$ forgets to divide by "
                "the number of steps — the most common slip on this type. "
                "Check: $a_n = 5n + 1$ gives $a_2 = 11$ ✓ and $a_8 = 41$ ✓.",
                [
                    "Eq(Rational(41 - 11, 8 - 2), 5)",
                    "Eq(5*2 + 1, 11)",
                    "Eq(5*8 + 1, 41)",
                ],
            ),
            {"kind": "worked", "title": "Seats in a theatre", "problemId": "im1-u3-l3-we3"},
            {"kind": "worked", "title": "When it is NOT arithmetic", "problemId": "im1-u3-l3-we4"},
            {
                "kind": "tip",
                "title": "Test your formula on term 1",
                "body": (
                    "Whatever explicit rule you write, substitute $n = 1$ before using it. If it "
                    "does not return the first term, the $(n-1)$ has gone wrong — and you have "
                    "caught it in one line instead of after five wrong answers."
                ),
            },
            {"kind": "tryIt", "title": "Your turn — write the rule", "problemId": "im1-u3-l3-t1"},
            {"kind": "tryIt", "title": "Your turn — from two terms", "problemId": "im1-u3-l3-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "A sequence is a function whose domain is the counting numbers",
                    "Arithmetic ⇔ constant **difference** $d$",
                    "Recursive $a_n = a_{n-1} + d$; explicit $a_n = a_1 + (n-1)d$",
                    "$(n-1)$ counts steps taken — test the formula at $n = 1$",
                    "It is a linear function: $d$ is the slope, and the dots lie on a line",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 4 — F-BF.2, F-LE.2: geometric sequences
# ===========================================================================
def lesson_geometric():
    return lesson(
        slug="geometric-sequences",
        title="Geometric Sequences",
        concrete=(
            "Fold a sheet of paper in half and the thickness doubles. Fold again and it doubles "
            "again. Nothing is being ADDED — each step multiplies. Forty-two folds would reach the "
            "Moon, which sounds absurd until you notice that doubling is a completely different "
            "engine from adding, and this lesson is where you meet it."
        ),
        objective=(
            "Recognise a geometric sequence by its constant ratio, write it recursively and "
            "explicitly, find any term directly, and see it as the exponential counterpart to the "
            "arithmetic sequence."
        ),
        concept=[
            "**Geometric means a constant RATIO.** Divide each term by the one before it; if you "
            "always get the same number $r$, the sequence is geometric. In $2, 6, 18, 54$ the "
            "ratios are $3, 3, 3$, so $r = 3$. Contrast the previous lesson: arithmetic ADDS the "
            "same amount, geometric MULTIPLIES by the same amount.",
            "**Test differences first, then ratios.** Given an unfamiliar sequence, subtract "
            "consecutive terms. Constant? Arithmetic. Not constant? Divide consecutive terms "
            "instead. Constant? Geometric. Between them these two tests classify nearly every "
            "sequence in IM1, and applying the wrong formula to the wrong type is the main way "
            "this topic goes wrong.",
            "**Recursive and explicit, again.** "
            "$$a_1 = 2, \\qquad a_n = r \\cdot a_{n-1} \\qquad\\text{(recursive)}$$ "
            "$$a_n = a_1 \\cdot r^{\\,n-1} \\qquad\\text{(explicit)}$$ "
            "The exponent is $n-1$ for exactly the reason the arithmetic rule had $(n-1)d$: the "
            "first term has been multiplied zero times, and $r^0 = 1$ leaves it alone.",
            "**A ratio between zero and one means decay.** A ratio of $0.5$ halves each time: "
            "$800, 400, 200, 100$. The sequence still counts as geometric — it is falling, not "
            "growing, and $r < 1$ is exactly the signal. A negative $r$ makes the terms alternate "
            "in sign: with $r = -2$, the sequence $3, -6, 12, -24$ flips every step.",
            "**Geometric is to exponential what arithmetic is to linear.** $a_n = a_1 r^{n-1}$ has "
            "the variable in the EXPONENT, which is the shape of the exponential functions of "
            "Unit 6. Plotted, the dots curve away instead of lining up — and that curve eventually "
            "beats any straight line, however steep, which is the single most useful fact about "
            "growth you will learn this year.",
        ],
        key_idea=(
            "Constant ratio $r$. Recursive: $a_n = r\\,a_{n-1}$. Explicit: $a_n = a_1 r^{\\,n-1}$ "
            "— the exponent counts multiplications, and the first term has had none. $r > 1$ "
            "grows, $0 < r < 1$ decays."
        ),
        facts=[
            fact(
                "Recursive form",
                "a_1 = \\text{first term}, \\qquad a_n = r \\cdot a_{n-1}",
                "Each term is the previous one multiplied by the common ratio.",
            ),
            fact(
                "Explicit form",
                "a_n = a_1 \\cdot r^{\\,n-1}",
                "The exponent counts multiplications performed. At n = 1 it is r⁰ = 1, leaving the "
                "first term untouched.",
            ),
            fact(
                "Reading r",
                "r > 1 \\ \\text{grows}, \\quad 0 < r < 1 \\ \\text{decays}, \\quad "
                "r < 0 \\ \\text{alternates}",
                "The ratio's size decides growth or decay; its sign decides whether the terms "
                "flip.",
            ),
        ],
        worked=[
            problem(
                "im1-u3-l4-we1",
                "For $2, 6, 18, 54, \\dots$ find the common ratio, write both rules, and find the "
                "$8$th term.",
                "**Common ratio.** Divide consecutive terms:"
                "$$\\frac{6}{2} = 3, \\qquad \\frac{18}{6} = 3, \\qquad \\frac{54}{18} = 3.$$"
                "Constant, so it is geometric with $r = 3$. (The differences $4, 12, 36$ are not "
                "constant, confirming it is not arithmetic.)"
                "**Recursive rule.**"
                "$$a_1 = 2, \\qquad a_n = 3a_{n-1}.$$"
                "**Explicit rule.**"
                "$$a_n = 2 \\cdot 3^{\\,n-1}.$$"
                "Check at $n = 1$: $2 \\cdot 3^0 = 2 \\cdot 1 = 2$ ✓. At $n = 3$: "
                "$2 \\cdot 9 = 18$ ✓."
                "**Eighth term.**"
                "$$a_8 = 2 \\cdot 3^{7} = 2 \\cdot 2187 = 4374.$$"
                "Using $3^8$ instead would give $13\\,122$ — three times too big, the exact "
                "penalty for miscounting the exponent by one.",
                [
                    "Eq(Rational(6,2), 3)",
                    "Eq(Rational(54,18), 3)",
                    "Eq(2*3**0, 2)",
                    "Eq(2*3**2, 18)",
                    "Eq(2*3**7, 4374)",
                    "Eq(2*3**8, 3*4374)",
                ],
            ),
            problem(
                "im1-u3-l4-we2",
                "A bacterial culture starts at $500$ cells and doubles every hour. Write the "
                "explicit rule for the count after $n$ hours and find the count after $9$ hours.",
                "**Set it up as a sequence.** Let $a_n$ be the count at the START of hour $n$, so "
                "$a_1 = 500$ is the initial count and $r = 2$."
                "$$a_n = 500 \\cdot 2^{\\,n-1}.$$"
                "**After 9 hours** the culture has doubled nine times, which is term $n = 10$:"
                "$$a_{10} = 500 \\cdot 2^{9} = 500 \\cdot 512 = 256\\,000.$$"
                "**The off-by-one, made explicit.** \"After $9$ hours\" means nine doublings, and "
                "the explicit rule's exponent counts doublings — so it is $2^9$, reached at index "
                "$n = 10$. If you prefer, model it directly as $P(t) = 500 \\cdot 2^{t}$ with $t$ "
                "in hours, which gives $P(9) = 256\\,000$ without any index bookkeeping. Both are "
                "correct; the second is what Unit 6 will use.",
                [
                    "Eq(500*2**0, 500)",
                    "Eq(500*2**9, 256000)",
                    "Eq(2**9, 512)",
                ],
            ),
            problem(
                "im1-u3-l4-we3",
                "A car worth $24\\,000\\,000$₮ loses a quarter of its value each year. Write the "
                "sequence rule and find its value after $3$ years.",
                "**The ratio.** Losing a quarter means KEEPING three quarters:"
                "$$r = 1 - \\frac{1}{4} = \\frac{3}{4} = 0.75.$$"
                "Since $0 < r < 1$, this is decay — the sequence falls."
                "**Rule.** With $a_1 = 24\\,000\\,000$ as the value at year $0$:"
                "$$V(t) = 24\\,000\\,000 \\cdot (0.75)^{t}.$$"
                "**After 3 years.**"
                "$$V(3) = 24\\,000\\,000 \\times 0.421875 = 10\\,125\\,000.$$"
                "The car is worth $10\\,125\\,000$₮."
                "**Why it is not a quarter of the way to zero.** Three years of losing a quarter leaves "
                "$0.75^3 = 42.19\\%$, not $25\\%$. Each year's loss is taken from a smaller "
                "amount than the last, so the value approaches zero without ever reaching it — "
                "which is what makes decay geometric rather than arithmetic.",
                [
                    "Eq(Rational(3,4)**3, Rational(27,64))",
                    "Eq(24000000*Rational(3,4)**3, 10125000)",
                    "Eq(Rational(27,64), 0.421875)",
                    "Rational(27,64) > Rational(1,4)",
                ],
            ),
            problem(
                "im1-u3-l4-we4",
                "Compare $a_n = 3n + 5$ (arithmetic) with $b_n = 3 \\cdot 2^{\\,n-1}$ (geometric) "
                "at $n = 1, 3, 6$ and $10$. Which is bigger, and does that change?",
                "Evaluate both at each index."
                "$$n=1: \\quad a_1 = 8, \\qquad b_1 = 3.$$"
                "$$n=3: \\quad a_3 = 14, \\qquad b_3 = 12.$$"
                "$$n=6: \\quad a_6 = 23, \\qquad b_6 = 96.$$"
                "$$n=10: \\quad a_{10} = 35, \\qquad b_{10} = 1536.$$"
                "The linear sequence leads at first — it starts higher and the geometric one has "
                "small terms to multiply. By $n = 6$ the geometric sequence has overtaken it, and "
                "by $n = 10$ it is more than forty times larger."
                "**The lesson.** Adding a fixed amount produces steady, predictable growth. "
                "Multiplying by a fixed amount produces growth that starts slowly and then "
                "outruns ANY linear sequence, no matter how large its common difference. The "
                "crossover always happens eventually — Unit 6 makes this precise.",
                [
                    "Eq(3*1 + 5, 8)",
                    "Eq(3*2**0, 3)",
                    "Eq(3*3 + 5, 14)",
                    "Eq(3*2**2, 12)",
                    "Eq(3*6 + 5, 23)",
                    "Eq(3*2**5, 96)",
                    "Eq(3*10 + 5, 35)",
                    "Eq(3*2**9, 1536)",
                    "3*2**5 > 3*6 + 5",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Using aₙ = a₁ · rⁿ instead of a₁ · r^(n−1).",
                "Test at n = 1: the first term has been multiplied zero times, so the exponent must "
                "be 0 there. That forces n − 1.",
            ),
            mistake(
                "Reading 'loses 25% each year' as a ratio of 0.25.",
                "Losing a quarter means keeping three quarters, so r = 0.75. The ratio is what "
                "SURVIVES, not what is lost.",
            ),
            mistake(
                "Testing only the first pair of terms before declaring a sequence geometric.",
                "Check every consecutive pair. 2, 6, 18, 55 has ratios 3, 3, 3.06 — one bad ratio "
                "and it is not geometric at all.",
            ),
            mistake(
                "Assuming a sequence that grows fast must be geometric.",
                "Test the ratios. 1, 4, 9, 16 grows quickly but its ratios are 4, 2.25, 1.78 — it "
                "is the squares, neither arithmetic nor geometric.",
            ),
        ],
        try_it=[
            problem(
                "im1-u3-l4-t1",
                "For $5, 15, 45, 135, \\dots$ write the explicit rule and find $a_6$.",
                "The ratios are all $3$, so $r = 3$ and $a_n = 5 \\cdot 3^{\\,n-1}$. Check at "
                "$n = 1$: $5 \\cdot 1 = 5$ ✓. Then $a_6 = 5 \\cdot 3^5 = 5 \\cdot 243 = 1215$.",
                [
                    "Eq(Rational(15,5), 3)",
                    "Eq(5*3**0, 5)",
                    "Eq(5*3**5, 1215)",
                ],
            ),
            problem(
                "im1-u3-l4-t2",
                "A ball is dropped from $200$ cm and rebounds to $60\\%$ of its previous height "
                "each bounce. How high is the third bounce?",
                "The ratio is $r = 0.6$, and the third bounce is three rebounds after the drop:"
                "$$h = 200 \\times 0.6^{3} = 200 \\times 0.216 = 43.2\\ \\text{cm}.$$",
                [
                    "Eq(Rational(6,10)**3, Rational(216, 1000))",
                    "Eq(200*Rational(216,1000), Rational(216,5))",
                    "Eq(Rational(216,5), 43.2)",
                ],
            ),
            problem(
                "im1-u3-l4-t3",
                "Is $4, 12, 36, 108$ arithmetic, geometric, or neither? Justify.",
                "The differences are $8, 24, 72$ — not constant, so it is not arithmetic. The "
                "ratios are $\\frac{12}{4} = 3$, $\\frac{36}{12} = 3$, $\\frac{108}{36} = 3$ — "
                "constant, so it is **geometric** with $r = 3$ and "
                "$a_n = 4 \\cdot 3^{\\,n-1}$.",
                [
                    "Eq(12 - 4, 8)",
                    "Ne(8, 24)",
                    "Eq(Rational(12,4), 3)",
                    "Eq(Rational(108,36), 3)",
                    "Eq(4*3**3, 108)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "F-BF.2",
                "title": "Geometric = a constant ratio",
                "body": (
                    "Divide each term by the one before. Always the same number? Then the sequence "
                    "is geometric and that number is $r$. Arithmetic ADDS the same amount; "
                    "geometric MULTIPLIES by it."
                ),
                "beats": [
                    "$\\frac{6}{2} = 3$",
                    "$\\frac{18}{6} = 3$",
                    "$\\frac{54}{18} = 3$",
                    "Constant ratio → geometric, $r = 3$",
                ],
            },
            {
                "kind": "tip",
                "title": "Differences first, then ratios",
                "body": (
                    "Given any unfamiliar sequence: subtract consecutive terms. Constant → "
                    "arithmetic. Not constant → divide consecutive terms instead. Constant → "
                    "geometric. Applying an arithmetic formula to a geometric sequence is the "
                    "main way this topic goes wrong, and this two-step test prevents it."
                ),
            },
            {"kind": "worked", "title": "Ratio, both rules, eighth term", "problemId": "im1-u3-l4-we1"},
            tap(
                "Which exponent?",
                "A geometric sequence has $a_1 = 7$ and $r = 2$. What is $a_5$?",
                ["$112$", "$224$", "$70$", "$56$"],
                0,
                "$a_5 = 7 \\cdot 2^{\\,5-1} = 7 \\cdot 2^4 = 7 \\cdot 16 = 112$. The exponent is "
                "$4$, not $5$, because reaching term $5$ takes four multiplications. Using $2^5$ "
                "gives $224$ — exactly double, which is the signature of this off-by-one. "
                "Check by walking: $7, 14, 28, 56, 112$ ✓",
                [
                    "Eq(7*2**4, 112)",
                    "Eq(7*2**5, 224)",
                    "Eq(7*2*2*2*2, 112)",
                ],
            ),
            {
                "kind": "expGraph",
                "eyebrow": "See the curve",
                "title": "Multiplying bends the graph",
                "teach": (
                    "An arithmetic sequence's dots lie on a straight line. A geometric one's curve "
                    "upward, because each step multiplies what is already there. Same starting "
                    "point, completely different engine."
                ),
                "config": {"mode": "growth", "a": 2, "b": 3, "interactive": True},
            },
            {"kind": "worked", "title": "Doubling bacteria", "problemId": "im1-u3-l4-we2"},
            {
                "kind": "teach",
                "eyebrow": "Reading r",
                "title": "Above one grows, below one decays",
                "body": (
                    "$r = 2$ doubles. $r = 0.75$ keeps three quarters and so falls. $r = -2$ "
                    "flips the sign every step. The SIZE of $r$ decides growth or decay; its SIGN "
                    "decides whether the terms alternate."
                ),
                "beats": [
                    "$r > 1$ — grows: $3, 6, 12, 24$",
                    "$0 < r < 1$ — decays: $800, 400, 200$",
                    "$r < 0$ — alternates: $3, -6, 12, -24$",
                    "'Loses $25\\%$' means $r = 0.75$, not $0.25$",
                ],
            },
            tap(
                "What is the ratio?",
                "A population falls by $20\\%$ each year. What is the common ratio?",
                ["$0.2$", "$0.8$", "$1.2$", "$-0.2$"],
                1,
                "Losing $20\\%$ means keeping $80\\%$, so $r = 0.8$. The ratio is what SURVIVES "
                "each step, not what disappears. Check on $1000$: after one year "
                "$1000 \\times 0.8 = 800$, a loss of $200$, which is indeed $20\\%$ ✓",
                [
                    "Eq(1000*Rational(8,10), 800)",
                    "Eq(1000 - 800, 200)",
                    "Eq(Rational(200,1000), Rational(20,100))",
                ],
            ),
            {"kind": "worked", "title": "A car losing a quarter a year", "problemId": "im1-u3-l4-we3"},
            {
                "kind": "teach",
                "eyebrow": "F-LE.3, previewed",
                "title": "Multiplying always wins in the end",
                "body": (
                    "A geometric sequence can start far behind a linear one and still overtake it. "
                    "It is not a question of whether but of when — and once it passes, the gap "
                    "widens without limit. Unit 6 makes this precise; this is your first sight of "
                    "it."
                ),
            },
            {"kind": "worked", "title": "Linear versus geometric, side by side", "problemId": "im1-u3-l4-we4"},
            {
                "kind": "funFact",
                "title": "Forty-two folds to the Moon",
                "body": (
                    "A sheet of paper is about $0.1$ mm thick. Each fold doubles it, so after $n$ "
                    "folds the thickness is $0.1 \\times 2^{n}$ mm. At $n = 42$ that exceeds "
                    "$400\\,000$ km — past the Moon. Nobody can actually fold paper forty-two "
                    "times, but the arithmetic is honest, and it is the clearest demonstration of "
                    "what a constant ratio does."
                ),
            },
            {"kind": "tryIt", "title": "Your turn — write the rule", "problemId": "im1-u3-l4-t1"},
            {"kind": "tryIt", "title": "Your turn — classify it", "problemId": "im1-u3-l4-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "Geometric ⇔ constant **ratio** $r$ (test ratios after differences fail)",
                    "Recursive $a_n = r\\,a_{n-1}$; explicit $a_n = a_1 r^{\\,n-1}$",
                    "The exponent counts multiplications — the first term has had none",
                    "$r > 1$ grows, $0 < r < 1$ decays, $r < 0$ alternates",
                    "'Loses $p\\%$' gives $r = 1 - p/100$ — the ratio is what survives",
                ],
            },
        ],
    )


# ===========================================================================
# Unit banks
# ===========================================================================
def practice_bank():
    return [
        problem(
            "im1-u3-pr-1",
            "Is $\\{(1, 3), (2, 6), (3, 3), (4, 9)\\}$ a function? Give the domain and range.",
            "Yes — the inputs $1, 2, 3, 4$ are all distinct, each with one output. The repeated "
            "output $3$ is allowed. Domain $\\{1, 2, 3, 4\\}$, range $\\{3, 6, 9\\}$.",
            ["Eq(len({1, 2, 3, 4}), 4)", "Eq(len({3, 6, 3, 9}), 3)"],
        ),
        problem(
            "im1-u3-pr-2",
            "For $f(x) = 4x - 7$, find $f(3)$, $f(-1)$ and $f(0)$.",
            "$f(3) = 12 - 7 = 5$; $f(-1) = -4 - 7 = -11$; $f(0) = -7$.",
            [
                "Eq(4*3 - 7, 5)",
                "Eq(4*(-1) - 7, -11)",
                "Eq(4*0 - 7, -7)",
            ],
        ),
        problem(
            "im1-u3-pr-3",
            "For $g(x) = x^2 - 3x$, find $g(-2)$ and $g(4)$.",
            "$g(-2) = (-2)^2 - 3(-2) = 4 + 6 = 10$; $g(4) = 16 - 12 = 4$.",
            [
                "Eq((-2)**2 - 3*(-2), 10)",
                "Eq(4**2 - 3*4, 4)",
            ],
        ),
        problem(
            "im1-u3-pr-4",
            "State the domain of $f(x) = \\dfrac{2x}{x + 5}$.",
            "The denominator is zero at $x = -5$, so the domain is all real numbers except $-5$. "
            "Check a legal value: $f(-4) = \\frac{-8}{1} = -8$.",
            [
                "Eq(-5 + 5, 0)",
                "Eq(Rational(2*(-4), -4 + 5), -8)",
            ],
        ),
        problem(
            "im1-u3-pr-5",
            "For $f(x) = 2x + 9$, simplify $f(x + 3)$.",
            "Replace every $x$ with $x + 3$: $f(x+3) = 2(x+3) + 9 = 2x + 15$. Check at $x = 1$: "
            "$f(4) = 17$ and $2(1) + 15 = 17$ ✓",
            [
                "Eq(simplify(2*(Symbol('x') + 3) + 9), 2*Symbol('x') + 15)",
                "Eq(2*4 + 9, 17)",
            ],
        ),
        problem(
            "im1-u3-pr-6",
            "For $6, 13, 20, 27, \\dots$ write the explicit rule and find $a_{15}$.",
            "The common difference is $7$ and $a_1 = 6$, so $a_n = 6 + (n-1)(7) = 7n - 1$. Check "
            "$a_1 = 6$ ✓. Then $a_{15} = 105 - 1 = 104$.",
            [
                "Eq(13 - 6, 7)",
                "Eq(7*1 - 1, 6)",
                "Eq(7*15 - 1, 104)",
            ],
        ),
        problem(
            "im1-u3-pr-7",
            "An arithmetic sequence has $a_5 = 31$ and $a_{11} = 61$. Find $d$ and $a_1$.",
            "From term $5$ to term $11$ is $6$ steps and the value rose by $30$, so "
            "$d = \\frac{30}{6} = 5$. Backing up four steps: $a_1 = 31 - 20 = 11$. Check: "
            "$a_n = 5n + 6$ gives $a_5 = 31$ ✓ and $a_{11} = 61$ ✓.",
            [
                "Eq(Rational(61 - 31, 11 - 5), 5)",
                "Eq(31 - 4*5, 11)",
                "Eq(5*5 + 6, 31)",
                "Eq(5*11 + 6, 61)",
            ],
        ),
        problem(
            "im1-u3-pr-8",
            "For $3, 12, 48, 192, \\dots$ write the explicit rule and find $a_6$.",
            "The ratios are all $4$, so $a_n = 3 \\cdot 4^{\\,n-1}$. Check at $n = 1$: $3$ ✓. "
            "Then $a_6 = 3 \\cdot 4^5 = 3 \\cdot 1024 = 3072$.",
            [
                "Eq(Rational(12,3), 4)",
                "Eq(3*4**0, 3)",
                "Eq(3*4**5, 3072)",
            ],
        ),
        problem(
            "im1-u3-pr-9",
            "Is $1, 4, 9, 16, 25$ arithmetic, geometric, or neither?",
            "Differences: $3, 5, 7, 9$ — not constant, so not arithmetic. Ratios: $4$, $2.25$, "
            "$1.78$, $1.5625$ — not constant, so not geometric. It is **neither**; these are the "
            "perfect squares, $a_n = n^2$.",
            [
                "Eq(4 - 1, 3)",
                "Eq(9 - 4, 5)",
                "Ne(3, 5)",
                "Ne(Rational(4,1), Rational(9,4))",
                "Eq(5**2, 25)",
            ],
        ),
        problem(
            "im1-u3-pr-10",
            "A savings account holds $400\\,000$₮ and grows $6\\%$ a year. Write the value after "
            "$t$ years and find it after $4$ years.",
            "Growing $6\\%$ means multiplying by $1.06$ each year:"
            "$$V(t) = 400\\,000 \\cdot (1.06)^{t}.$$"
            "After $4$ years: $V(4) = 400\\,000 \\times 1.26247696 = 504\\,990.784$₮, about "
            "$504\\,991$₮.",
            [
                "Eq(Rational(106,100)**4, Rational(126247696, 100000000))",
                "Eq(400000*Rational(106,100)**0, 400000)",
                "Abs(400000*Rational(106,100)**4 - 504991) < 1",
            ],
        ),
        problem(
            "im1-u3-pr-11",
            "A candle is $30$ cm tall and burns $2.5$ cm per hour, so $h(t) = 30 - 2.5t$. Find "
            "$h(6)$ and state the domain the situation allows.",
            "$h(6) = 30 - 15 = 15$ cm. The candle is gone when $30 - 2.5t = 0$, i.e. $t = 12$, and "
            "time cannot be negative, so the domain is $0 \\le t \\le 12$ hours.",
            [
                "Eq(30 - Rational(25,10)*6, 15)",
                "Eq(30 - Rational(25,10)*12, 0)",
                "Eq(30 - Rational(25,10)*0, 30)",
            ],
        ),
        problem(
            "im1-u3-pr-12",
            "A gym starts with $240$ members and gains $15$ each month. In which month does "
            "membership first exceed $400$?",
            "This is arithmetic with $a_1 = 240$ and $d = 15$, so $a_n = 240 + (n-1)(15) = "
            "15n + 225$. Solve $15n + 225 > 400$: $15n > 175$, so $n > 11.67$ and $n = 12$. "
            "Check: month $12$ gives $405 > 400$ ✓, month $11$ gives $390$ ✗.",
            [
                "Eq(15*1 + 225, 240)",
                "Eq(15*12 + 225, 405)",
                "15*12 + 225 > 400",
                "Not(15*11 + 225 > 400)",
            ],
        ),
    ]


def test_bank():
    return [
        problem(
            "im1-u3-ty-1",
            "Decide whether each relation is a function, and justify: "
            "(a) $\\{(2, 5), (3, 5), (4, 5)\\}$; (b) $\\{(1, 2), (1, 3), (2, 4)\\}$; "
            "(c) the equation $x = y^2$.",
            "**(a) Function.** The inputs $2, 3, 4$ are distinct and each has exactly one output. "
            "The repeated output $5$ is irrelevant — three buttons may dispense the same item."
            "**(b) Not a function.** The input $1$ appears with outputs $2$ and $3$, and "
            "$2 \\ne 3$, so it fails the one-output rule."
            "**(c) Not a function.** At $x = 4$, $y^2 = 4$ gives $y = 2$ and $y = -2$ — one input, "
            "two outputs. The vertical line $x = 4$ cuts the sideways parabola twice.",
            [
                "Eq(len({2, 3, 4}), 3)",
                "Ne(2, 3)",
                "Eq(2**2, 4)",
                "Eq((-2)**2, 4)",
                "Ne(2, -2)",
            ],
        ),
        problem(
            "im1-u3-ty-2",
            "For $f(x) = x^2 - 4x + 1$, find $f(0)$, $f(-2)$, and $f(3)$. Then find $f(2)$ and "
            "explain what is special about it.",
            "Substitute each input in brackets."
            "$$f(0) = 0 - 0 + 1 = 1.$$"
            "$$f(-2) = (-2)^2 - 4(-2) + 1 = 4 + 8 + 1 = 13.$$"
            "$$f(3) = 9 - 12 + 1 = -2.$$"
            "$$f(2) = 4 - 8 + 1 = -3.$$"
            "**Why that last value matters.** It is the smallest value this function ever takes. "
            "Comparing neighbours: $f(1) = -2$ and $f(3) = -2$ both exceed $-3$, and the function "
            "is symmetric about $x = 2$ — which you can see in the pairs $f(1) = f(3)$ and "
            "$f(0) = f(4) = 1$. The range is therefore $f(x) \\ge -3$.",
            [
                "Eq(0**2 - 4*0 + 1, 1)",
                "Eq((-2)**2 - 4*(-2) + 1, 13)",
                "Eq(3**2 - 4*3 + 1, -2)",
                "Eq(2**2 - 4*2 + 1, -3)",
                "Eq(1**2 - 4*1 + 1, -2)",
                "Eq(4**2 - 4*4 + 1, 1)",
            ],
        ),
        problem(
            "im1-u3-ty-3",
            "State the domain of each, with a reason: (a) $f(x) = \\dfrac{3}{2x - 8}$; "
            "(b) $g(x) = \\sqrt{x + 4}$; (c) $h(x) = 5x^2 - x + 2$.",
            "**(a)** The denominator vanishes when $2x - 8 = 0$, i.e. $x = 4$. Domain: all reals "
            "except $4$. Check a legal value: $f(5) = \\frac{3}{2} $."
            "**(b)** A square root needs a non-negative input: $x + 4 \\ge 0$, so $x \\ge -4$. "
            "Check the boundary: $g(-4) = \\sqrt{0} = 0$, defined, so $-4$ belongs."
            "**(c)** A polynomial has no denominator and no root, so nothing is illegal. Domain: "
            "all real numbers.",
            [
                "Eq(2*4 - 8, 0)",
                "Eq(Rational(3, 2*5 - 8), Rational(3,2))",
                "Eq(sqrt(-4 + 4), 0)",
                "Eq(sqrt(5 + 4), 3)",
            ],
        ),
        problem(
            "im1-u3-ty-4",
            "An arithmetic sequence has $a_2 = 17$ and $a_7 = 47$. Find the common difference, the "
            "first term, the explicit rule, and $a_{20}$.",
            "**Common difference.** From term $2$ to term $7$ is $5$ steps, over which the value "
            "rose by $47 - 17 = 30$:"
            "$$d = \\frac{30}{5} = 6.$$"
            "**First term.** Back up one step from $a_2$:"
            "$$a_1 = 17 - 6 = 11.$$"
            "**Explicit rule.**"
            "$$a_n = 11 + (n-1)(6) = 6n + 5.$$"
            "Check against BOTH given terms: $a_2 = 12 + 5 = 17$ ✓ and $a_7 = 42 + 5 = 47$ ✓."
            "**Twentieth term.**"
            "$$a_{20} = 6(20) + 5 = 125.$$",
            [
                "Eq(Rational(47 - 17, 7 - 2), 6)",
                "Eq(17 - 6, 11)",
                "Eq(6*2 + 5, 17)",
                "Eq(6*7 + 5, 47)",
                "Eq(6*20 + 5, 125)",
            ],
        ),
        problem(
            "im1-u3-ty-5",
            "A geometric sequence has $a_1 = 6$ and $a_4 = 162$. Find the common ratio and $a_7$.",
            "**Common ratio.** Reaching term $4$ from term $1$ takes three multiplications:"
            "$$a_4 = a_1 r^{3} \\quad\\Longrightarrow\\quad 162 = 6r^{3} "
            "\\quad\\Longrightarrow\\quad r^{3} = 27 \\quad\\Longrightarrow\\quad r = 3.$$"
            "**Check.** $6, 18, 54, 162$ ✓ — four terms, three steps."
            "**Seventh term.**"
            "$$a_7 = 6 \\cdot 3^{6} = 6 \\times 729 = 4374.$$",
            [
                "Eq(6*3**3, 162)",
                "Eq(3**3, 27)",
                "Eq(6*3**6, 4374)",
                "Eq(3**6, 729)",
            ],
        ),
        problem(
            "im1-u3-ty-6",
            "Classify each sequence and give its explicit rule: (a) $100, 88, 76, 64$; "
            "(b) $80, 40, 20, 10$; (c) $2, 5, 10, 17$.",
            "**(a)** Differences: $-12, -12, -12$ — constant, so **arithmetic** with $d = -12$ and "
            "$a_1 = 100$:"
            "$$a_n = 100 + (n-1)(-12) = 112 - 12n.$$"
            "Check $a_1 = 100$ ✓, $a_4 = 64$ ✓."
            "**(b)** Differences $-40, -20, -10$ are not constant, so test ratios: "
            "$\\frac{40}{80} = \\frac{1}{2}$ throughout — **geometric** with $r = \\frac{1}{2}$:"
            "$$a_n = 80 \\cdot \\left(\\tfrac{1}{2}\\right)^{n-1}.$$"
            "Check $a_4 = 80 \\cdot \\frac{1}{8} = 10$ ✓."
            "**(c)** Differences $3, 5, 7$ are not constant; ratios $2.5, 2, 1.7$ are not either. "
            "**Neither.** The pattern is $a_n = n^2 + 1$: $2, 5, 10, 17$ ✓.",
            [
                "Eq(88 - 100, -12)",
                "Eq(112 - 12*4, 64)",
                "Eq(Rational(40,80), Rational(1,2))",
                "Eq(80*Rational(1,2)**3, 10)",
                "Eq(3**2 + 1, 10)",
                "Eq(4**2 + 1, 17)",
                "Ne(5 - 2, 10 - 5)",
            ],
        ),
        problem(
            "im1-u3-ty-7",
            "Two savings plans start on the same day. Plan A puts in $500\\,000$₮ and adds "
            "$60\\,000$₮ every year. Plan B puts in $500\\,000$₮ and grows $10\\%$ every year. "
            "Write a rule for each, compute both at years $1$, $5$ and $10$, and say which plan "
            "wins in the long run.",
            "**Plan A is arithmetic** — a fixed amount added:"
            "$$A(t) = 500\\,000 + 60\\,000t.$$"
            "**Plan B is geometric** — a fixed factor multiplied:"
            "$$B(t) = 500\\,000 \\cdot (1.1)^{t}.$$"
            "**Year 1.** $A = 560\\,000$; $B = 550\\,000$. Plan A leads."
            "**Year 5.** $A = 800\\,000$; $B = 500\\,000 \\times 1.61051 = 805\\,255$. Plan B has "
            "just overtaken."
            "**Year 10.** $A = 1\\,100\\,000$; $B = 500\\,000 \\times 2.5937424 = 1\\,296\\,871.2$. "
            "Plan B is now clearly ahead."
            "**Long run.** Plan B wins, and by a widening margin. Adding a fixed amount produces a "
            "straight line; multiplying by a fixed factor produces a curve that eventually "
            "outgrows any line, however steep. The only question is when the crossover happens — "
            "here, between years $4$ and $5$.",
            [
                "Eq(500000 + 60000*1, 560000)",
                "Eq(500000*Rational(11,10)**1, 550000)",
                "Eq(500000 + 60000*5, 800000)",
                "Eq(500000*Rational(11,10)**5, 805255)",
                "500000*Rational(11,10)**5 > 500000 + 60000*5",
                "Eq(500000 + 60000*10, 1100000)",
                "500000*Rational(11,10)**10 > 500000 + 60000*10",
                "500000*Rational(11,10)**4 < 500000 + 60000*4",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="functions-and-sequences",
        title="Functions & Sequences",
        unit_number=3,
        blurb=(
            "The one-output rule and the vertical line test, function notation, domain and range "
            "from a rule and from a situation, and arithmetic and geometric sequences written "
            "both recursively and explicitly."
        ),
        builds_on=(
            "Creating equations from Unit 1 and solving them from Unit 2 — a function is what an "
            "equation becomes when you start asking about all its inputs at once."
        ),
        lessons=[
            lesson_what_is_a_function(),
            lesson_notation(),
            lesson_arithmetic(),
            lesson_geometric(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
