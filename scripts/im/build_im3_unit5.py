#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 5: Function Families & Inverses.

CCSS Integrated Math III: F-BF.3 (identify the effect of f(x) + k, k·f(x),
f(kx) and f(x + k) on a graph, and recognise even and odd functions from
their graphs and algebraic expressions), F-BF.1b/c (combine and compose
functions), F-BF.4a (find inverse functions: solve an equation of the form
f(x) = c, and write an expression for the inverse).

The unit's through-line: STOP STUDYING FUNCTIONS ONE AT A TIME. IM2 moved
parabolas around; Unit 3 flipped exponentials into logarithms without naming
the move. This unit names the moves and shows they work on EVERY family at
once: the same four transformations slide and stretch any graph, the same
f(-x) test detects symmetry in any formula, composition chains any two
machines into one, and an inverse — when it exists — is the machine run
backwards. The exp/log pair the student already trusts becomes one example
of a completely general idea.

Run: python3 scripts/im/build_im3_unit5.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — F-BF.3: the four transformations, on every family
# ===========================================================================

def lesson_transformations():
    return lesson(
        slug="transformations-of-functions",
        title="Transformations of Every Family",
        concrete=(
            "Moving a photo around a screen never changes the photo: drag it right, "
            "drag it up, stretch it taller, flip it over — the picture is the same "
            "picture in a new position. Graphs work exactly the same way. You already "
            "moved parabolas like this in IM2; this lesson shows the SAME four moves "
            "work on $|x|$, $\\sqrt{x}$, $2^x$ — on every function you will ever meet."
        ),
        objective=(
            "Predict how the graph of any function changes under vertical and "
            "horizontal shifts, stretches, and reflections, and write the transformed "
            "formula from a description."
        ),
        concept=[
            "Adding OUTSIDE the function moves the graph vertically: $f(x) + k$ is "
            "every output raised by $k$, so the whole graph slides up $k$ (down when "
            "$k$ is negative). Adding INSIDE moves it horizontally — and backwards "
            "from what the sign suggests: $f(x - h)$ slides the graph RIGHT by $h$, "
            "because the input $x = h$ is what now behaves the way $x = 0$ used to.",

            "Multiplying OUTSIDE stretches vertically: $a\\,f(x)$ makes every output "
            "$a$ times as large, so the graph is $a$ times taller. When $a$ is "
            "negative the graph also flips across the $x$-axis — $-f(x)$ is the "
            "mirror image, every high point becoming a low one. Multiplying INSIDE, "
            "$f(bx)$, compresses horizontally by a factor of $b$: the graph does "
            "everything it used to do, $b$ times sooner.",

            "The moves stack, and the formula records the whole recipe. "
            "$g(x) = -2\\,f(x - 3) + 4$ reads: shift right $3$, stretch vertically "
            "by $2$, flip across the $x$-axis, then raise by $4$. Reading a formula "
            "as a recipe is the skill — one glance at $g$ and you can sketch it from "
            "the parent graph without plotting a single point.",

            "Order matters exactly where it matters in arithmetic. Stretch-then-shift "
            "and shift-then-stretch give different graphs, because $3f(x) - 1$ and "
            "$3\\left(f(x) - 1\\right)$ are different formulas. The reliable "
            "convention: work from the inside of the formula out, the same order the "
            "machine itself computes.",
        ],
        key_idea=(
            "Outside the function acts on outputs (vertical, behaves as written); "
            "inside acts on inputs (horizontal, behaves in reverse). Those two "
            "sentences transform every function family there is."
        ),
        facts=[
            fact("Vertical shift", "y = f(x) + k",
                 "Every output raised by k — the graph slides up k."),
            fact("Horizontal shift", "y = f(x - h)",
                 "The graph slides RIGHT h: inside changes run backwards."),
            fact("Vertical stretch", "y = a\\,f(x)",
                 "Outputs scale by a; negative a also flips across the x-axis."),
            fact("Horizontal compression", "y = f(bx)",
                 "The graph does everything b times sooner — width shrinks by b."),
            fact("Read inside-out", "g(x) = a\\,f(x - h) + k",
                 "Shift right h, scale by a, then raise k — the order the machine "
                 "computes."),
        ],
        worked=[
            problem(
                "im3-u5-l1-we1",
                "Describe the transformations that turn $f(x) = |x|$ into "
                "$g(x) = -2|x - 3| + 4$, and find the vertex of $g$.",
                "**Read the formula inside-out.** Inside: $x - 3$ shifts the graph "
                "right $3$. Outside: the factor $2$ stretches it vertically, the "
                "minus sign flips it across the $x$-axis, and the $+4$ raises it $4$."
                "**Track the vertex.** The corner of $|x|$ sits at $(0, 0)$; right "
                "$3$ and up $4$ carries it to $(3, 4)$. Because of the flip the "
                "graph now opens DOWNWARD, so $(3, 4)$ is a maximum: "
                "$g(3) = -2|0| + 4 = 4$."
                "**Check a second point.** $g(5) = -2|2| + 4 = 0$ — two steps right "
                "of the vertex, the graph has fallen $4$, twice as fast as $|x|$ "
                "rises. Every feature matches the recipe.",
                [
                    "Eq(-2*Abs(3 - 3) + 4, 4)",
                    "Eq(-2*Abs(5 - 3) + 4, 0)",
                    "Eq(-2*Abs(1 - 3) + 4, 0)",
                ],
            ),
            problem(
                "im3-u5-l1-we2",
                "Write the formula for $\\sqrt{x}$ shifted left $2$, reflected "
                "across the $x$-axis, and raised $5$. Then evaluate it at $x = 2$.",
                "**Build the recipe in formula order.** Left $2$ means the inside "
                "gains $+2$: $\\sqrt{x + 2}$. The reflection puts a minus sign in "
                "front: $-\\sqrt{x + 2}$. Raising by $5$ adds outside: "
                "$g(x) = -\\sqrt{x + 2} + 5$."
                "**Evaluate.** $g(2) = -\\sqrt{4} + 5 = -2 + 5 = 3$."
                "**Sanity-check the endpoint.** The parent's endpoint $(0,0)$ moves "
                "left $2$ and up $5$ to $(-2, 5)$: indeed $g(-2) = -\\sqrt{0} + 5 = "
                "5$, and the graph now falls away from that point instead of "
                "rising.",
                [
                    "Eq(-sqrt(2 + 2) + 5, 3)",
                    "Eq(-sqrt(0) + 5, 5)",
                    "Eq(-sqrt(7 + 2) + 5, 2)",
                ],
            ),
            problem(
                "im3-u5-l1-we3",
                "Starting from $f(x) = x^2$, one student stretches vertically by "
                "$3$ THEN shifts down $1$; another shifts down $1$ THEN stretches "
                "by $3$. Write both formulas and show they disagree.",
                "**First student.** Stretch first gives $3x^2$; the shift then acts "
                "on that: $g(x) = 3x^2 - 1$."
                "**Second student.** Shift first gives $x^2 - 1$; the stretch "
                "scales the WHOLE thing: $h(x) = 3(x^2 - 1) = 3x^2 - 3$."
                "**Compare.** At $x = 0$: $g(0) = -1$ but $h(0) = -3$. The second "
                "student's stretch magnified the shift itself — a downward move of "
                "$1$ became a move of $3$. Order matters precisely because a "
                "stretch scales everything done before it.",
                [
                    "Eq(3*0**2 - 1, -1)",
                    "Eq(3*(0**2 - 1), -3)",
                    "Ne(3*0**2 - 1, 3*(0**2 - 1))",
                    "Eq(expand(3*(x**2 - 1)), 3*x**2 - 3)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading f(x - 3) as a shift LEFT because of the minus sign.",
                "Inside changes run backwards: x - 3 means the input 3 now plays the "
                "role 0 used to play, so the graph moves RIGHT 3. Test one point "
                "before trusting the sign.",
            ),
            mistake(
                "Applying a vertical stretch to only part of the formula.",
                "The stretch a·f(x) multiplies the ENTIRE output. Turning "
                "x² - 1 into 3x² - 1 is stretch-then-shift; a stretch of the whole "
                "graph of x² - 1 is 3(x² - 1) = 3x² - 3.",
            ),
            mistake(
                "Confusing f(-x) with -f(x).",
                "f(-x) reflects across the y-AXIS (inputs run backwards); -f(x) "
                "reflects across the x-AXIS (outputs flip sign). For f(x) = √x they "
                "produce entirely different graphs.",
            ),
            mistake(
                "Moving the vertex but forgetting the flip reverses max and min.",
                "After a reflection across the x-axis the transformed vertex is a "
                "MAXIMUM if it was a minimum. State whether the graph opens up or "
                "down before naming the extreme value.",
            ),
        ],
        try_it=[
            problem(
                "im3-u5-l1-t1",
                "Find the vertex of $g(x) = (x + 4)^2 - 3$ and say whether it is a "
                "maximum or a minimum.",
                "Inside $+4$ shifts left $4$; outside $-3$ shifts down $3$. The "
                "vertex is $(-4, -3)$, and with no reflection the parabola still "
                "opens up, so it is a minimum: $g(-4) = -3$, while a step away "
                "$g(-3) = -2$ is already higher.",
                [
                    "Eq((-4 + 4)**2 - 3, -3)",
                    "Eq((-3 + 4)**2 - 3, -2)",
                    "((-3 + 4)**2 - 3) > ((-4 + 4)**2 - 3)",
                ],
            ),
            problem(
                "im3-u5-l1-t2",
                "Write the formula for $|x|$ shifted right $2$ and down $1$, and "
                "evaluate it at $x = 5$.",
                "Right $2$: $|x - 2|$. Down $1$: $g(x) = |x - 2| - 1$. Then "
                "$g(5) = |3| - 1 = 2$, and the corner sits at $(2, -1)$.",
                [
                    "Eq(Abs(5 - 2) - 1, 2)",
                    "Eq(Abs(2 - 2) - 1, -1)",
                ],
            ),
            problem(
                "im3-u5-l1-t3",
                "Which single transformation turns $y = 2^x$ into $y = 2^{-x}$?",
                "The input is replaced by its opposite, so the graph reflects "
                "across the $y$-axis. The point $(1, 2)$ moves to $(-1, 2)$: "
                "indeed $2^{-(-1)} = 2$, while $2^{-1} = \\frac{1}{2}$ now sits at "
                "$x = 1$.",
                [
                    "Eq(2**(-(-1)), 2)",
                    "Eq(2**(-1), Rational(1, 2))",
                ],
            ),
        ],
        steps=[
            tap(
                "Outside the function",
                "The graph of $g(x) = f(x) + 5$ is the graph of $f$ moved:",
                ["up $5$", "right $5$", "left $5$", "stretched by $5$"],
                0,
                "Adding outside the function raises every OUTPUT by $5$ — a "
                "vertical slide, exactly as written.",
                ["Eq((x**2 + 5) - x**2, 5)"],
            ),
            tap(
                "Inside the function",
                "The graph of $g(x) = f(x - 3)$ is the graph of $f$ moved:",
                ["right $3$", "left $3$", "up $3$", "down $3$"],
                0,
                "Inside changes run backwards: the input $3$ now does what $0$ "
                "used to do, so the graph slides right. For $f(x) = x^2$ the "
                "vertex lands at $x = 3$.",
                ["Eq((3 - 3)**2, 0)", "Eq((4 - 3)**2, 1)"],
            ),
            tap(
                "Two different mirrors",
                "For $f(x) = \\sqrt{x}$, which formula reflects the graph across "
                "the x-axis?",
                ["$-\\sqrt{x}$", "$\\sqrt{-x}$", "$\\sqrt{x} - 1$", "$\\dfrac{1}{\\sqrt{x}}$"],
                0,
                "Flipping across the $x$-axis negates OUTPUTS: $-f(x)$. At "
                "$x = 4$ the value $2$ becomes $-2$. ($\\sqrt{-x}$ is the "
                "$y$-axis mirror instead.)",
                ["Eq(-sqrt(4), -2)", "Eq(sqrt(4), 2)"],
            ),
        ],
    )


# ===========================================================================
# Lesson 2 — F-BF.3: even and odd symmetry
# ===========================================================================

def lesson_even_odd():
    return lesson(
        slug="even-and-odd-functions",
        title="Even & Odd Symmetry",
        concrete=(
            "Fold a butterfly down the middle and the wings match — that is mirror "
            "symmetry. Spin a playing card's face through half a turn and it looks "
            "unchanged — that is rotational symmetry. Graphs carry the same two "
            "symmetries, and unlike the butterfly, a graph will confess which one it "
            "has to a single algebraic test: feed the function $-x$ and watch what "
            "comes back."
        ),
        objective=(
            "Test any formula for even or odd symmetry by computing the function at "
            "the opposite input, and connect each outcome to its graph: mirror in "
            "the y-axis, or half-turn about the origin."
        ),
        concept=[
            "A function is EVEN when opposite inputs give equal outputs: "
            "$f(-x) = f(x)$ for every $x$. Graphically the left half is the mirror "
            "image of the right half in the $y$-axis — whatever happens at $x = 3$ "
            "happens identically at $x = -3$. The parent examples are $x^2$ and "
            "$|x|$: squaring or taking absolute value destroys the sign.",

            "A function is ODD when opposite inputs give opposite outputs: "
            "$f(-x) = -f(x)$. Graphically the graph is unchanged by a half-turn "
            "about the origin — the part in the first quadrant reappears, upside "
            "down, in the third. The parents are $x$ and $x^3$: an odd power "
            "carries the input's sign straight through.",

            "The names come from polynomials, and for polynomials the test is a "
            "glance: if every exponent is even the function is even, if every "
            "exponent is odd it is odd. $x^4 - 3x^2 + 1$ is even (the constant is "
            "$x^0$, an even power); $x^3 - 5x$ is odd. Mix the parities — "
            "$x^2 + x$ — and the function is NEITHER, which is the common case.",

            "Two small consequences are worth keeping. An odd function that is "
            "defined at $0$ must satisfy $f(0) = -f(0)$, forcing $f(0) = 0$ — odd "
            "graphs pass through the origin. And the test must hold for EVERY "
            "input: one working example proves nothing, but one failing example "
            "settles neither-ness for good.",
        ],
        key_idea=(
            "Feed the function the opposite input. Same output back: even, a "
            "y-axis mirror. Opposite output back: odd, a half-turn about the "
            "origin. Anything else: neither."
        ),
        facts=[
            fact("Even test", "f(-x) = f(x)",
                 "Opposite inputs, equal outputs — mirror symmetry in the y-axis."),
            fact("Odd test", "f(-x) = -f(x)",
                 "Opposite inputs, opposite outputs — half-turn symmetry about the "
                 "origin."),
            fact("Polynomial shortcut", "x^4 - 3x^2 \\text{ even},\\quad x^3 - 5x \\text{ odd}",
                 "All exponents even makes it even; all odd makes it odd; mixed is "
                 "neither."),
            fact("Odd through the origin", "f(0) = 0",
                 "f(0) = -f(0) forces it, whenever an odd function is defined at 0."),
            fact("One counterexample suffices", "f(-1) \\ne \\pm f(1) \\Rightarrow \\text{neither}",
                 "The symmetry must hold everywhere, so a single failure ends the "
                 "test."),
        ],
        worked=[
            problem(
                "im3-u5-l2-we1",
                "Classify $f(x) = x^4 - 3x^2 + 1$ as even, odd, or neither.",
                "**Substitute the opposite input.** $f(-x) = (-x)^4 - 3(-x)^2 + 1$. "
                "Even powers erase the sign: $(-x)^4 = x^4$ and $(-x)^2 = x^2$."
                "**Compare.** $f(-x) = x^4 - 3x^2 + 1 = f(x)$, identical for every "
                "$x$ — the function is EVEN."
                "**See it numerically.** $f(2) = 16 - 12 + 1 = 5$ and "
                "$f(-2) = 5$: opposite inputs, equal outputs, exactly the y-axis "
                "mirror the algebra promised.",
                [
                    "Eq(expand((-x)**4 - 3*(-x)**2 + 1), expand(x**4 - 3*x**2 + 1))",
                    "Eq(2**4 - 3*2**2 + 1, 5)",
                    "Eq((-2)**4 - 3*(-2)**2 + 1, 5)",
                ],
            ),
            problem(
                "im3-u5-l2-we2",
                "Classify $g(x) = x^3 - 5x$ as even, odd, or neither.",
                "**Substitute.** $g(-x) = (-x)^3 - 5(-x) = -x^3 + 5x$."
                "**Factor out the sign.** $-x^3 + 5x = -(x^3 - 5x) = -g(x)$ — "
                "opposite outputs for opposite inputs, so $g$ is ODD."
                "**Confirm the origin.** $g(0) = 0$, as every odd function defined "
                "at $0$ must give; and $g(2) = -2$ against $g(-2) = 2$ shows the "
                "half-turn in action.",
                [
                    "Eq(expand((-x)**3 - 5*(-x)), expand(-(x**3 - 5*x)))",
                    "Eq(0**3 - 5*0, 0)",
                    "Eq(2**3 - 5*2, -2)",
                    "Eq((-2)**3 - 5*(-2), 2)",
                ],
            ),
            problem(
                "im3-u5-l2-we3",
                "Classify $h(x) = x^2 + x$ as even, odd, or neither.",
                "**Test one pair of opposite inputs.** $h(1) = 2$ and "
                "$h(-1) = 1 - 1 = 0$."
                "**Compare against both symmetries.** Even would need "
                "$h(-1) = h(1)$, but $0 \\ne 2$. Odd would need $h(-1) = -h(1)$, "
                "but $0 \\ne -2$. Both fail, so $h$ is NEITHER."
                "**Why it had to fail.** The exponents mix parities — the $x^2$ "
                "term survives the sign flip while the $x$ term reverses, so the "
                "two halves of the formula pull in different directions.",
                [
                    "Eq(1**2 + 1, 2)",
                    "Eq((-1)**2 + (-1), 0)",
                    "Ne((-1)**2 + (-1), 1**2 + 1)",
                    "Ne((-1)**2 + (-1), -(1**2 + 1))",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Testing one value, finding it works, and declaring symmetry.",
                "f(x) = x³ - x + 5 has f(-1) = f(1) = 5, yet f(2) = 11 while "
                "f(-2) = -1 — one matching pair can be pure luck. Symmetry claims "
                "need the identity in x to hold for EVERY input; only NEITHER can "
                "be settled by a single example.",
            ),
            mistake(
                "Believing every function is either even or odd.",
                "Neither is the default. x² + x, 2^x and √x are all neither — the "
                "two symmetric kinds are the exception, which is why they earn "
                "names.",
            ),
            mistake(
                "Dropping the sign when substituting -x into an odd power.",
                "(-x)³ = -x³, not x³. Write the substitution with parentheses "
                "around -x every time; the sign errors all come from skipping "
                "them.",
            ),
            mistake(
                "Confusing odd symmetry with 'the graph looks decreasing'.",
                "Odd means the graph maps to itself under a half-turn about the "
                "origin — x³ is odd and increasing everywhere. Symmetry and "
                "direction are independent properties.",
            ),
        ],
        try_it=[
            problem(
                "im3-u5-l2-t1",
                "Is $f(x) = |x|$ even, odd, or neither?",
                "$f(-x) = |-x| = |x| = f(x)$ — even. Numerically $|-3| = |3| = 3$: "
                "the V-shape is its own mirror image in the $y$-axis.",
                [
                    "Eq(Abs(-x), Abs(x))",
                    "Eq(Abs(-3), 3)",
                ],
            ),
            problem(
                "im3-u5-l2-t2",
                "Is $g(x) = x^5$ even, odd, or neither?",
                "$g(-x) = (-x)^5 = -x^5 = -g(x)$ — odd. Check: $g(-2) = -32 = "
                "-g(2)$, the half-turn pairing.",
                [
                    "Eq((-x)**5, -x**5)",
                    "Eq((-2)**5, -(2**5))",
                ],
            ),
            problem(
                "im3-u5-l2-t3",
                "Is $h(x) = x^2 + 1$ even, odd, or neither?",
                "$h(-x) = (-x)^2 + 1 = x^2 + 1 = h(x)$ — even. The parabola's "
                "shift straight up preserves the mirror; a sideways shift would "
                "have broken it.",
                [
                    "Eq((-x)**2 + 1, x**2 + 1)",
                    "Eq((-3)**2 + 1, 3**2 + 1)",
                ],
            ),
        ],
        steps=[
            tap(
                "Read the test",
                "For every $x$, a function satisfies $f(-x) = f(x)$. Its graph "
                "is symmetric across:",
                ["the $y$-axis", "the $x$-axis", "the origin", "the line $y = x$"],
                0,
                "Equal outputs at opposite inputs means the left half mirrors "
                "the right half — $y$-axis symmetry, the definition of even. "
                "$x^2$ shows it: $(-3)^2 = 3^2$.",
                ["Eq((-3)**2, 3**2)"],
            ),
            tap(
                "Spot the odd one",
                "Which function is odd?",
                ["$x^3 - x$", "$x^2 + x$", "$x^2 + 1$", "$|x|$"],
                0,
                "All exponents in $x^3 - x$ are odd, so $f(-x) = -f(x)$: at "
                "$x = 2$, $f(2) = 6$ and $f(-2) = -6$. The others are neither, "
                "even, and even.",
                [
                    "Eq(expand((-x)**3 - (-x)), expand(-(x**3 - x)))",
                    "Eq(2**3 - 2, 6)",
                    "Eq((-2)**3 - (-2), -6)",
                ],
            ),
            tap(
                "The origin clue",
                "An odd function $f$ is defined at $x = 0$. What is $f(0)$?",
                ["$0$", "$1$", "any value", "undefined"],
                0,
                "Oddness at $x = 0$ says $f(-0) = -f(0)$, i.e. $f(0) = -f(0)$ — "
                "only $0$ equals its own opposite.",
                ["Eq(0, -0)"],
            ),
        ],
    )


# ===========================================================================
# Lesson 3 — F-BF.1c: composing functions
# ===========================================================================

def lesson_composition():
    return lesson(
        slug="composition-of-functions",
        title="Composing Functions",
        concrete=(
            "A store runs two promotions: 20% off everything, and a \\$10-off "
            "coupon. On an \\$80 jacket, does the order matter? Discount first: "
            "$0.8 \\times 80 - 10 = 54$. Coupon first: $0.8 \\times (80 - 10) = 56$. "
            "Two dollars apart — because applying one rule to the RESULT of another "
            "is a genuinely new operation. Mathematics calls it composition, and it "
            "is how simple functions assemble into complicated ones."
        ),
        objective=(
            "Evaluate and simplify compositions of two functions, in both orders, "
            "and decompose a complicated function into an inner and an outer part."
        ),
        concept=[
            "Composition chains two machines: the output of the first becomes the "
            "input of the second. The notation $(f \\circ g)(x) = f(g(x))$ reads "
            "RIGHT to left — $g$ acts first, $f$ acts on what $g$ produced. To "
            "evaluate at a number, work from the inside out: find $g(2)$, then feed "
            "that number to $f$.",

            "To get a FORMULA for the composition, substitute the whole inner "
            "formula wherever the outer function's variable appears. With "
            "$f(x) = 2x - 3$ and $g(x) = x^2 + 1$: $(f \\circ g)(x) = "
            "2(x^2 + 1) - 3 = 2x^2 - 1$. The parentheses around the inner formula "
            "are doing real work — every symptom of a botched composition traces "
            "back to dropping them.",

            "Order matters, and usually changes everything: $(g \\circ f)(x) = "
            "(2x - 3)^2 + 1$ is a different function from $2x^2 - 1$ — different "
            "formula, different graph, different values. Composition is not "
            "multiplication; $f \\circ g$ and $g \\circ f$ are as different as "
            "putting on socks-then-shoes and shoes-then-socks.",

            "Decomposition runs the idea backwards: seeing $h(x) = \\sqrt{3x + 4}$ "
            "as $f(g(x))$ with inner $g(x) = 3x + 4$ and outer $f(x) = \\sqrt{x}$. "
            "The inner function is whatever the formula computes FIRST. This "
            "reading turns one complicated function into two simple ones — the "
            "move that unlocks solving layered equations, and later, calculus.",
        ],
        key_idea=(
            "A composition is a chain of machines: $(f \\circ g)(x) = f(g(x))$, "
            "inner first, outer second. Substitute the whole inner formula — in "
            "parentheses — and never expect the two orders to agree."
        ),
        facts=[
            fact("Definition", "(f \\circ g)(x) = f(g(x))",
                 "g acts first; f acts on g's output. Read right to left."),
            fact("Evaluate inside-out", "(f \\circ g)(2) = f(g(2))",
                 "Compute the inner value, then feed it to the outer function."),
            fact("Order matters", "f \\circ g \\ne g \\circ f \\text{ in general}",
                 "The two orders give different functions — check before swapping."),
            fact("Decomposition", "h(x) = f(g(x))",
                 "The inner g is what the formula computes first; the outer f is "
                 "what happens to that result."),
            fact("Not multiplication", "(f \\circ g)(x) \\ne f(x) \\cdot g(x)",
                 "The circle is substitution, not a product — the two operations "
                 "rarely agree."),
        ],
        worked=[
            problem(
                "im3-u5-l3-we1",
                "For $f(x) = 2x - 3$ and $g(x) = x^2 + 1$, evaluate "
                "$(f \\circ g)(2)$ and $(g \\circ f)(2)$.",
                "**Inner first, then outer.** $(f \\circ g)(2) = f(g(2))$: the "
                "inner value is $g(2) = 4 + 1 = 5$, and then $f(5) = 10 - 3 = 7$."
                "**Reverse the order.** $(g \\circ f)(2) = g(f(2))$: now "
                "$f(2) = 1$ goes first, and $g(1) = 1 + 1 = 2$."
                "**Compare.** $7$ against $2$ — same functions, same input, "
                "different answers. The order of the chain is part of the "
                "question.",
                [
                    "Eq(2**2 + 1, 5)",
                    "Eq(2*5 - 3, 7)",
                    "Eq(2*2 - 3, 1)",
                    "Eq(1**2 + 1, 2)",
                    "Ne(7, 2)",
                ],
            ),
            problem(
                "im3-u5-l3-we2",
                "For the same $f(x) = 2x - 3$ and $g(x) = x^2 + 1$, find formulas "
                "for $(f \\circ g)(x)$ and $(g \\circ f)(x)$.",
                "**Substitute the whole inner formula.** $(f \\circ g)(x) = "
                "f(x^2 + 1) = 2(x^2 + 1) - 3 = 2x^2 - 1$."
                "**Now the other order.** $(g \\circ f)(x) = g(2x - 3) = "
                "(2x - 3)^2 + 1 = 4x^2 - 12x + 10$."
                "**Cross-check with the last example.** At $x = 2$ the formulas "
                "give $2(4) - 1 = 7$ and $16 - 24 + 10 = 2$ — matching the "
                "inside-out evaluations exactly.",
                [
                    "Eq(expand(2*(x**2 + 1) - 3), 2*x**2 - 1)",
                    "Eq(expand((2*x - 3)**2 + 1), 4*x**2 - 12*x + 10)",
                    "Eq(2*2**2 - 1, 7)",
                    "Eq(4*2**2 - 12*2 + 10, 2)",
                ],
            ),
            problem(
                "im3-u5-l3-we3",
                "Write $h(x) = \\sqrt{3x + 4}$ as a composition $f(g(x))$ of two "
                "simpler functions, and use the decomposition to evaluate $h(4)$.",
                "**Name what happens first.** The formula computes $3x + 4$ before "
                "anything else: that is the inner function, $g(x) = 3x + 4$."
                "**Name what happens to the result.** The square root acts on that "
                "output: the outer function is $f(x) = \\sqrt{x}$, and indeed "
                "$f(g(x)) = \\sqrt{3x + 4} = h(x)$."
                "**Evaluate through the chain.** $g(4) = 16$, then "
                "$f(16) = 4$ — so $h(4) = 4$, each machine doing one simple job.",
                [
                    "Eq(3*4 + 4, 16)",
                    "Eq(sqrt(16), 4)",
                    "Eq(sqrt(3*4 + 4), 4)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading (f ∘ g) left to right and applying f first.",
                "The symbol closest to the input acts first: (f ∘ g)(x) = f(g(x)), "
                "so g goes first. Saying 'f AFTER g' out loud prevents the swap.",
            ),
            mistake(
                "Substituting without parentheses.",
                "Composing f(x) = 2x - 3 with g(x) = x² + 1 needs 2(x² + 1) - 3. "
                "Writing 2·x² + 1 - 3 loses the doubling of the +1 and gives "
                "2x² - 2 instead of 2x² - 1.",
            ),
            mistake(
                "Treating (f ∘ g)(x) as f(x) times g(x).",
                "The circle is substitution. For f(x) = 2x - 3, g(x) = x² + 1 the "
                "product at x = 2 is 1 · 5 = 5, while the composition is 7 — "
                "different operations, different answers.",
            ),
            mistake(
                "Assuming f ∘ g = g ∘ f after checking one convenient input.",
                "The two orders can agree at isolated points and still be "
                "different functions. Only identical FORMULAS (or an inverse "
                "relationship, next lesson) make the orders interchangeable.",
            ),
        ],
        try_it=[
            problem(
                "im3-u5-l3-t1",
                "For $f(x) = x - 4$ and $g(x) = 3x$, evaluate $(f \\circ g)(5)$ "
                "and $(g \\circ f)(5)$.",
                "$(f \\circ g)(5) = f(15) = 11$; $(g \\circ f)(5) = g(1) = 3$. "
                "Different orders, different results.",
                [
                    "Eq(3*5 - 4, 11)",
                    "Eq(3*(5 - 4), 3)",
                    "Ne(11, 3)",
                ],
            ),
            problem(
                "im3-u5-l3-t2",
                "For $f(x) = x^2$ and $g(x) = x + 3$, find the formula for "
                "$(f \\circ g)(x)$.",
                "$(f \\circ g)(x) = f(x + 3) = (x + 3)^2 = x^2 + 6x + 9$. Note "
                "$(g \\circ f)(x) = x^2 + 3$ is different — at $x = 1$ they give "
                "$16$ and $4$.",
                [
                    "Eq(expand((x + 3)**2), x**2 + 6*x + 9)",
                    "Eq((1 + 3)**2, 16)",
                    "Eq(1**2 + 3, 4)",
                ],
            ),
            problem(
                "im3-u5-l3-t3",
                "Write $h(x) = (5x - 2)^3$ as $f(g(x))$, naming the inner and "
                "outer functions.",
                "Inner: $g(x) = 5x - 2$ (computed first). Outer: $f(x) = x^3$. "
                "Check at $x = 1$: $g(1) = 3$, then $f(3) = 27 = h(1)$.",
                [
                    "Eq(5*1 - 2, 3)",
                    "Eq(3**3, 27)",
                    "Eq((5*1 - 2)**3, 27)",
                ],
            ),
        ],
        steps=[
            tap(
                "Who goes first",
                "In $(f \\circ g)(x)$, which function receives $x$ directly?",
                ["$g$", "$f$", "both at once", "whichever is written first"],
                0,
                "$(f \\circ g)(x) = f(g(x))$ — the inner $g$ takes $x$, and $f$ "
                "takes $g$'s output. Right to left, always.",
                ["Eq(2*(3*2) - 1, 11)"],
            ),
            tap(
                "Evaluate a chain",
                "With $f(x) = x + 1$ and $g(x) = 2x$, what is "
                "$(f \\circ g)(3)$?",
                ["$7$", "$8$", "$6$", "$9$"],
                0,
                "Inner first: $g(3) = 6$; then $f(6) = 7$. (The other order "
                "gives $g(f(3)) = 8$ — a different chain.)",
                [
                    "Eq(2*3 + 1, 7)",
                    "Eq(2*(3 + 1), 8)",
                ],
            ),
            tap(
                "Name the inner function",
                "To write $h(x) = \\sqrt{x^2 + 9}$ as $f(g(x))$, the inner "
                "function $g$ is:",
                ["$x^2 + 9$", "$\\sqrt{x}$", "$x^2$", "$\\sqrt{x} + 9$"],
                0,
                "The formula computes $x^2 + 9$ before the root acts — the "
                "first computation is the inner function. At $x = 4$: "
                "$g(4) = 25$, then $\\sqrt{25} = 5$.",
                [
                    "Eq(4**2 + 9, 25)",
                    "Eq(sqrt(25), 5)",
                ],
            ),
        ],
    )


# ===========================================================================
# Lesson 4 — F-BF.4: inverse functions
# ===========================================================================

def lesson_inverses():
    return lesson(
        slug="inverse-functions",
        title="Inverse Functions",
        concrete=(
            "Getting dressed: socks, then shoes. Getting undressed: shoes off, "
            "then socks — the opposite steps in the opposite order. An inverse "
            "function is exactly that idea for computation: it undoes what the "
            "function did, and Unit 3 already handed you the flagship example — "
            "$2^x$ raises, $\\log_2 x$ un-raises. This lesson makes the idea work "
            "for every function that can have one."
        ),
        objective=(
            "Find the inverse of a function algebraically, verify it by "
            "composition, read it graphically as a reflection across the line "
            "through the origin at $45^\\circ$, and decide when an inverse exists."
        ),
        concept=[
            "The inverse $f^{-1}$ undoes $f$: if $f$ sends $6$ to $7$, then "
            "$f^{-1}$ sends $7$ back to $6$. Undone-ness in symbols is "
            "composition: $f^{-1}(f(x)) = x$ and $f(f^{-1}(x)) = x$ — run the "
            "machine and then run it backwards, and you are where you started. "
            "That composition identity is also the CHECK for any claimed inverse.",

            "To find one, name the output and solve for the input. For "
            "$f(x) = 2x - 5$: write $y = 2x - 5$, solve for $x$ to get "
            "$x = \\frac{y + 5}{2}$, then swap the letters (the inverse is a "
            "function of ITS input): $f^{-1}(x) = \\frac{x + 5}{2}$. Notice it "
            "undoes the steps of $f$ in reverse order — $f$ doubles then "
            "subtracts $5$; $f^{-1}$ adds $5$ then halves.",

            "Graphically, inverting swaps the roles of the axes, so the graph of "
            "$f^{-1}$ is the graph of $f$ reflected across the line $y = x$. "
            "Every point $(a, b)$ on $f$ has its partner $(b, a)$ on $f^{-1}$ — "
            "which is why the exponential's graph and the logarithm's graph in "
            "Unit 3 were mirror images across that diagonal.",

            "Not every function has an inverse. If two inputs share an output — "
            "$(-3)^2 = 3^2 = 9$ — then 'undoing' from $9$ has no single answer. "
            "A function must be one-to-one (no horizontal line crosses its graph "
            "twice) to be invertible. The repair is to RESTRICT the domain: "
            "$x^2$ on $x \\ge 0$ keeps one branch, and its inverse is exactly "
            "$\\sqrt{x}$. One more habit: $f^{-1}$ is notation for the inverse "
            "FUNCTION, not the reciprocal $\\frac{1}{f(x)}$.",
        ],
        key_idea=(
            "An inverse runs the machine backwards: solve for the input, and "
            "verify with composition — both $f^{-1}(f(x))$ and $f(f^{-1}(x))$ "
            "must simplify all the way to $x$."
        ),
        facts=[
            fact("What inverse means", "f^{-1}(f(x)) = x",
                 "Do, then undo, and nothing has happened — in both orders."),
            fact("How to find it", "y = f(x) \\ \\to\\ \\text{solve for } x",
                 "Solve for the input, then swap letters so the inverse reads as "
                 "a function of its own input."),
            fact("The graphs", "(a, b) \\text{ on } f \\iff (b, a) \\text{ on } f^{-1}",
                 "Reflection across the line y = x — inputs and outputs trade "
                 "places."),
            fact("When it exists", "\\text{one-to-one} \\iff \\text{invertible}",
                 "No horizontal line may cross the graph twice; otherwise restrict "
                 "the domain first."),
            fact("Notation warning", "f^{-1}(x) \\ne \\tfrac{1}{f(x)}",
                 "The -1 marks an inverse function, not a reciprocal."),
        ],
        worked=[
            problem(
                "im3-u5-l4-we1",
                "Find the inverse of $f(x) = 2x - 5$ and verify it by "
                "composition.",
                "**Solve for the input.** From $y = 2x - 5$: add $5$, then halve: "
                "$x = \\frac{y + 5}{2}$. Swapping letters, $f^{-1}(x) = "
                "\\frac{x + 5}{2}$."
                "**Verify both compositions.** $f(f^{-1}(x)) = "
                "2 \\cdot \\frac{x + 5}{2} - 5 = x$ and $f^{-1}(f(x)) = "
                "\\frac{(2x - 5) + 5}{2} = x$. Both collapse to $x$: confirmed."
                "**Watch it undo one value.** $f(6) = 7$, and "
                "$f^{-1}(7) = \\frac{12}{2} = 6$ — back where we started.",
                [
                    "Eq(simplify(2*((x + 5)/2) - 5), x)",
                    "Eq(simplify(((2*x - 5) + 5)/2), x)",
                    "Eq(2*6 - 5, 7)",
                    "Eq(Rational(7 + 5, 2), 6)",
                ],
            ),
            problem(
                "im3-u5-l4-we2",
                "Find the inverse of $f(x) = x^3 + 1$, and use it to solve "
                "$f(x) = 9$.",
                "**Solve for the input.** From $y = x^3 + 1$: subtract $1$, then "
                "take the cube root: $x = \\sqrt[3]{y - 1}$, so $f^{-1}(x) = "
                "\\sqrt[3]{x - 1}$. Cubing is one-to-one — every number has "
                "exactly one real cube root — so no restriction is needed."
                "**Solve the equation with it.** $f(x) = 9$ means $x = "
                "f^{-1}(9) = \\sqrt[3]{8} = 2$."
                "**Check.** $f(2) = 8 + 1 = 9$ — the inverse turned an equation "
                "into a single evaluation.",
                [
                    "Eq((9 - 1)**Rational(1, 3), 2)",
                    "Eq(2**3 + 1, 9)",
                    "Eq((28 - 1)**Rational(1, 3), 3)",
                ],
            ),
            problem(
                "im3-u5-l4-we3",
                "Explain why $f(x) = x^2$ has no inverse on all real numbers, and "
                "fix it by restricting the domain.",
                "**Find the failure.** $f(-3) = 9$ and $f(3) = 9$: two inputs, one "
                "output. Undoing from $9$ has no single answer, so no function can "
                "be the inverse — the horizontal line at height $9$ crosses the "
                "parabola twice."
                "**Restrict.** Keep only $x \\ge 0$. On that domain each output "
                "comes from exactly one input, and solving $y = x^2$ for "
                "nonnegative $x$ gives $x = \\sqrt{y}$: the inverse is "
                "$f^{-1}(x) = \\sqrt{x}$."
                "**Verify on the kept branch.** $f(5) = 25$ and $\\sqrt{25} = 5$. "
                "The discarded branch is why $\\sqrt{9} = 3$, never $-3$: the "
                "root function returns the branch we kept.",
                [
                    "Eq((-3)**2, 3**2)",
                    "Eq(sqrt(25), 5)",
                    "Eq(sqrt(9), 3)",
                    "Ne(sqrt(9), -3)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading f⁻¹(x) as 1 divided by f(x).",
                "The superscript marks the inverse FUNCTION. For f(x) = 2x - 5, "
                "f⁻¹(7) = 6, while 1/f(7) = 1/9 — unrelated numbers. Say "
                "'f-inverse', never 'f to the minus one'.",
            ),
            mistake(
                "Verifying only one composition order.",
                "A full verification checks f(f⁻¹(x)) = x AND f⁻¹(f(x)) = x. For "
                "the functions in this lesson one order implies the other, but the "
                "habit of checking both catches domain mismatches later.",
            ),
            mistake(
                "Inverting a function that is not one-to-one without restricting.",
                "If two inputs share an output, the 'inverse' sends that output "
                "two places — not a function. Check the horizontal line test "
                "first; restrict the domain when it fails.",
            ),
            mistake(
                "Swapping letters first and then solving for y sloppily.",
                "Either order works IF the algebra is careful, but solve-then-swap "
                "keeps the meaning visible: you are solving for the INPUT in "
                "terms of the output, which is what undoing means.",
            ),
        ],
        try_it=[
            problem(
                "im3-u5-l4-t1",
                "Find the inverse of $f(x) = x + 7$.",
                "Solve $y = x + 7$ for $x$: $x = y - 7$, so $f^{-1}(x) = x - 7$. "
                "Check: $f(3) = 10$ and $f^{-1}(10) = 3$.",
                [
                    "Eq(simplify((x + 7) - 7), x)",
                    "Eq(10 - 7, 3)",
                ],
            ),
            problem(
                "im3-u5-l4-t2",
                "Find the inverse of $f(x) = \\dfrac{x - 4}{3}$.",
                "Solve $y = \\frac{x - 4}{3}$: multiply by $3$, add $4$ — "
                "$x = 3y + 4$, so $f^{-1}(x) = 3x + 4$. Composition check: "
                "$\\frac{(3x + 4) - 4}{3} = x$.",
                [
                    "Eq(simplify(((3*x + 4) - 4)/3), x)",
                    "Eq(simplify(3*((x - 4)/3) + 4), x)",
                ],
            ),
            problem(
                "im3-u5-l4-t3",
                "The point $(2, 11)$ lies on the graph of a one-to-one function "
                "$f$. What point must lie on the graph of $f^{-1}$?",
                "$(11, 2)$ — inverting swaps input and output, reflecting the "
                "point across the diagonal line. If $f(x) = 4x + 3$, indeed "
                "$f(2) = 11$ and $f^{-1}(11) = \\frac{11 - 3}{4} = 2$.",
                [
                    "Eq(4*2 + 3, 11)",
                    "Eq(Rational(11 - 3, 4), 2)",
                ],
            ),
        ],
        steps=[
            tap(
                "Undo one value",
                "A one-to-one function has $f(5) = 12$. What is $f^{-1}(12)$?",
                ["$5$", "$12$", "$\\dfrac{1}{12}$", "cannot be determined"],
                0,
                "The inverse sends every output back to its input: $12$ came "
                "from $5$. With $f(x) = 2x + 2$ as an example: $f(5) = 12$ and "
                "$\\frac{12 - 2}{2} = 5$.",
                [
                    "Eq(2*5 + 2, 12)",
                    "Eq(Rational(12 - 2, 2), 5)",
                ],
            ),
            tap(
                "The mirror line",
                "The graphs of $f$ and $f^{-1}$ are reflections of each other "
                "across:",
                ["the line $y = x$", "the $x$-axis", "the $y$-axis", "the origin"],
                0,
                "Inverting swaps coordinates: $(2, 7)$ on $f$ pairs with "
                "$(7, 2)$ on $f^{-1}$, and swapping coordinates is reflection "
                "across the diagonal. With $f(x) = 2x + 3$: $f(2) = 7$, and the "
                "inverse takes $7$ back to $2$.",
                [
                    "Eq(2*2 + 3, 7)",
                    "Eq(Rational(7 - 3, 2), 2)",
                ],
            ),
            tap(
                "Who gets an inverse",
                "Which function needs a domain restriction before it can have an "
                "inverse?",
                ["$x^2$", "$x^3$", "$2x - 5$", "$x + 1$"],
                0,
                "$x^2$ sends $-2$ and $2$ to the same output, failing the "
                "horizontal line test; the others are one-to-one as they stand. "
                "Restricted to nonnegative inputs, its inverse is the square "
                "root.",
                [
                    "Eq((-2)**2, 2**2)",
                    "Ne((-2)**3, 2**3)",
                ],
            ),
        ],
    )


# ===========================================================================
# Practice bank
# ===========================================================================

def practice_bank():
    return [
        problem(
            "im3-u5-p1",
            "Describe the transformations that turn $f(x) = x^2$ into "
            "$g(x) = (x - 2)^2 + 3$, and state the vertex of $g$.",
            "Inside $-2$: shift right $2$. Outside $+3$: shift up $3$. The vertex "
            "moves from $(0,0)$ to $(2, 3)$: $g(2) = 0 + 3 = 3$, and one step "
            "away $g(4) = 4 + 3 = 7$ rises exactly like the parent.",
            [
                "Eq((2 - 2)**2 + 3, 3)",
                "Eq((4 - 2)**2 + 3, 7)",
            ],
        ),
        problem(
            "im3-u5-p2",
            "Write the formula for $|x|$ stretched vertically by $3$, reflected "
            "across the $x$-axis, and raised $6$. Where does the graph cross the "
            "$x$-axis?",
            "The recipe gives $g(x) = -3|x| + 6$. Crossing means $g(x) = 0$: "
            "$3|x| = 6$, so $|x| = 2$ and $x = \\pm 2$. Check: $g(2) = -6 + 6 = "
            "0$ and $g(0) = 6$ is the flipped peak.",
            [
                "Eq(-3*Abs(2) + 6, 0)",
                "Eq(-3*Abs(-2) + 6, 0)",
                "Eq(-3*Abs(0) + 6, 6)",
            ],
        ),
        problem(
            "im3-u5-p3",
            "The graph of $g(x) = \\sqrt{x - 4}$ is the graph of $\\sqrt{x}$ "
            "shifted which way? State the domain of $g$ and evaluate $g(13)$.",
            "Inside $-4$ shifts RIGHT $4$. The root needs $x - 4 \\ge 0$, so the "
            "domain is $x \\ge 4$ — the parent's domain, carried along by the "
            "shift. $g(13) = \\sqrt{9} = 3$, and the endpoint sits at $(4, 0)$.",
            [
                "Eq(sqrt(13 - 4), 3)",
                "Eq(sqrt(4 - 4), 0)",
            ],
        ),
        problem(
            "im3-u5-p4",
            "Classify $f(x) = x^5 - 4x^3$ as even, odd, or neither.",
            "$f(-x) = (-x)^5 - 4(-x)^3 = -x^5 + 4x^3 = -f(x)$ — every exponent "
            "is odd, so the function is ODD. Check a pair: $f(1) = -3$ and "
            "$f(-1) = 3$.",
            [
                "Eq(expand((-x)**5 - 4*(-x)**3), expand(-(x**5 - 4*x**3)))",
                "Eq(1**5 - 4*1**3, -3)",
                "Eq((-1)**5 - 4*(-1)**3, 3)",
            ],
        ),
        problem(
            "im3-u5-p5",
            "Classify $g(x) = 3x^4 + x^2 - 7$ as even, odd, or neither.",
            "Every exponent is even (the constant is the $x^0$ term), so "
            "$g(-x) = g(x)$: EVEN. Check: $g(2) = 48 + 4 - 7 = 45 = g(-2)$ — "
            "the y-axis mirror in numbers.",
            [
                "Eq(expand(3*(-x)**4 + (-x)**2 - 7), expand(3*x**4 + x**2 - 7))",
                "Eq(3*2**4 + 2**2 - 7, 45)",
                "Eq(3*(-2)**4 + (-2)**2 - 7, 45)",
            ],
        ),
        problem(
            "im3-u5-p6",
            "Classify $h(x) = x^3 + x^2$ as even, odd, or neither.",
            "Test $x = 1$: $h(1) = 2$ and $h(-1) = -1 + 1 = 0$. Even fails "
            "($0 \\ne 2$) and odd fails ($0 \\ne -2$): NEITHER. The mixed "
            "parities of the exponents doomed it from the start.",
            [
                "Eq(1**3 + 1**2, 2)",
                "Eq((-1)**3 + (-1)**2, 0)",
                "Ne((-1)**3 + (-1)**2, 1**3 + 1**2)",
                "Ne((-1)**3 + (-1)**2, -(1**3 + 1**2))",
            ],
        ),
        problem(
            "im3-u5-p7",
            "Is $f(x) = |x| - x^2$ even, odd, or neither? Justify with the "
            "algebraic test.",
            "$f(-x) = |-x| - (-x)^2 = |x| - x^2 = f(x)$ — both pieces are even, "
            "so the difference is EVEN. Check: $f(3) = 3 - 9 = -6 = f(-3)$.",
            [
                "Eq(Abs(-x) - (-x)**2, Abs(x) - x**2)",
                "Eq(Abs(3) - 3**2, -6)",
                "Eq(Abs(-3) - (-3)**2, -6)",
            ],
        ),
        problem(
            "im3-u5-p8",
            "For $f(x) = x - 4$ and $g(x) = 3x$, evaluate $(f \\circ g)(5)$ and "
            "$(g \\circ f)(5)$.",
            "$(f \\circ g)(5)$: inner $g(5) = 15$, then $f(15) = 11$. "
            "$(g \\circ f)(5)$: inner $f(5) = 1$, then $g(1) = 3$. The orders "
            "disagree, as they usually do.",
            [
                "Eq(3*5 - 4, 11)",
                "Eq(3*(5 - 4), 3)",
                "Ne(11, 3)",
            ],
        ),
        problem(
            "im3-u5-p9",
            "For $f(x) = x^2$ and $g(x) = x + 3$, find formulas for both "
            "$(f \\circ g)(x)$ and $(g \\circ f)(x)$, and evaluate each at "
            "$x = 1$.",
            "$(f \\circ g)(x) = (x + 3)^2 = x^2 + 6x + 9$; at $x = 1$ it gives "
            "$16$. $(g \\circ f)(x) = x^2 + 3$; at $x = 1$ it gives $4$. Same "
            "pieces, different chains.",
            [
                "Eq(expand((x + 3)**2), x**2 + 6*x + 9)",
                "Eq((1 + 3)**2, 16)",
                "Eq(1**2 + 3, 4)",
            ],
        ),
        problem(
            "im3-u5-p10",
            "Write $h(x) = (5x - 2)^3$ as a composition $f(g(x))$ and evaluate "
            "$h(1)$ through the chain.",
            "Inner (computed first): $g(x) = 5x - 2$. Outer: $f(x) = x^3$. "
            "Chain at $x = 1$: $g(1) = 3$, then $f(3) = 27$, so $h(1) = 27$.",
            [
                "Eq(5*1 - 2, 3)",
                "Eq(3**3, 27)",
                "Eq((5*1 - 2)**3, 27)",
            ],
        ),
        problem(
            "im3-u5-p11",
            "A store offers 20% off, and you also hold a \\$10 coupon. On an "
            "\\$80 jacket, compute the price for discount-then-coupon and for "
            "coupon-then-discount. Which order should you ask for?",
            "Discount first: $0.8 \\times 80 - 10 = 64 - 10 = 54$. Coupon "
            "first: $0.8 \\times (80 - 10) = 0.8 \\times 70 = 56$. Ask for the "
            "discount first and save \\$2 — the two compositions are different "
            "functions of the price.",
            [
                "Eq(Rational(4, 5)*80 - 10, 54)",
                "Eq(Rational(4, 5)*(80 - 10), 56)",
                "Ne(54, 56)",
            ],
        ),
        problem(
            "im3-u5-p12",
            "Find the inverse of $f(x) = 4x - 9$ and verify one composition.",
            "Solve $y = 4x - 9$: $x = \\frac{y + 9}{4}$, so $f^{-1}(x) = "
            "\\frac{x + 9}{4}$. Verify: $f(f^{-1}(x)) = 4 \\cdot "
            "\\frac{x + 9}{4} - 9 = x$. Spot check: $f(3) = 3$ and "
            "$f^{-1}(3) = 3$ — this function happens to cross the mirror line "
            "there.",
            [
                "Eq(simplify(4*((x + 9)/4) - 9), x)",
                "Eq(simplify(((4*x - 9) + 9)/4), x)",
                "Eq(4*3 - 9, 3)",
            ],
        ),
        problem(
            "im3-u5-p13",
            "Find the inverse of $f(x) = \\dfrac{x}{2} + 3$.",
            "Solve $y = \\frac{x}{2} + 3$: subtract $3$, double — "
            "$x = 2(y - 3) = 2y - 6$, so $f^{-1}(x) = 2x - 6$. Check: "
            "$f(10) = 8$ and $f^{-1}(8) = 10$.",
            [
                "Eq(simplify(2*((x/2 + 3)) - 6), x)",
                "Eq(Rational(10, 2) + 3, 8)",
                "Eq(2*8 - 6, 10)",
            ],
        ),
        problem(
            "im3-u5-p14",
            "Show by composition (both orders) that $g(x) = \\dfrac{x - 1}{5}$ "
            "is the inverse of $f(x) = 5x + 1$.",
            "$f(g(x)) = 5 \\cdot \\frac{x - 1}{5} + 1 = (x - 1) + 1 = x$, and "
            "$g(f(x)) = \\frac{(5x + 1) - 1}{5} = \\frac{5x}{5} = x$. Both "
            "orders collapse to $x$, which is the definition of an inverse "
            "pair.",
            [
                "Eq(simplify(5*((x - 1)/5) + 1), x)",
                "Eq(simplify(((5*x + 1) - 1)/5), x)",
            ],
        ),
        problem(
            "im3-u5-p15",
            "One of $f(x) = x^3$ and $g(x) = x^4$ is invertible on all real "
            "numbers and one is not. Which is which, and why?",
            "$f(x) = x^3$ is one-to-one: opposite inputs give opposite outputs "
            "($(-1)^3 = -1 \\ne 1 = 1^3$), and no horizontal line crosses a "
            "cubic's graph twice — it is invertible, with inverse "
            "$\\sqrt[3]{x}$. $g(x) = x^4$ fails: $(-1)^4 = 1^4 = 1$, two inputs "
            "sharing an output, so $g$ needs a domain restriction first.",
            [
                "Ne((-1)**3, 1**3)",
                "Eq((-1)**4, 1**4)",
                "Eq(8**Rational(1, 3), 2)",
            ],
        ),
        problem(
            "im3-u5-p16",
            "The Celsius formula is $C(F) = \\dfrac{5}{9}(F - 32)$. Find the "
            "inverse and use both to convert $212^\\circ$F to Celsius and back.",
            "Solve $C = \\frac{5}{9}(F - 32)$ for $F$: multiply by "
            "$\\frac{9}{5}$, add $32$ — $F(C) = \\frac{9}{5}C + 32$. Forward: "
            "$C(212) = \\frac{5}{9} \\cdot 180 = 100$. Back: $F(100) = 180 + 32 "
            "= 212$. The round trip returns the start, as an inverse pair must.",
            [
                "Eq(Rational(5, 9)*(212 - 32), 100)",
                "Eq(Rational(9, 5)*100 + 32, 212)",
                "Eq(simplify(Rational(9, 5)*(Rational(5, 9)*(x - 32)) + 32), x)",
            ],
        ),
    ]


# ===========================================================================
# Test bank
# ===========================================================================

def test_bank():
    return [
        problem(
            "im3-u5-x1",
            "Describe every transformation taking $f(x) = x^2$ to "
            "$g(x) = -(x + 1)^2 + 8$, state the vertex, and say whether it is a "
            "maximum or a minimum.",
            "Inside $+1$: shift LEFT $1$. The minus sign: reflect across the "
            "$x$-axis. Outside $+8$: raise $8$. The vertex lands at $(-1, 8)$, "
            "and the reflection makes the parabola open downward, so it is a "
            "MAXIMUM: $g(-1) = 8$, while $g(1) = -4 + 8 = 4$ two steps away.",
            [
                "Eq(-(-1 + 1)**2 + 8, 8)",
                "Eq(-(1 + 1)**2 + 8, 4)",
                "(-(0 + 1)**2 + 8) < 8",
            ],
        ),
        problem(
            "im3-u5-x2",
            "Classify $f(x) = x^3 - x$ as even, odd, or neither, and state what "
            "its symmetry forces $f(0)$ to be.",
            "$f(-x) = -x^3 + x = -(x^3 - x) = -f(x)$: ODD, a half-turn about the "
            "origin. Oddness forces $f(0) = -f(0)$, so $f(0) = 0$ — and indeed "
            "$0^3 - 0 = 0$. Pair check: $f(2) = 6$, $f(-2) = -6$.",
            [
                "Eq(expand((-x)**3 - (-x)), expand(-(x**3 - x)))",
                "Eq(0**3 - 0, 0)",
                "Eq(2**3 - 2, 6)",
                "Eq((-2)**3 - (-2), -6)",
            ],
        ),
        problem(
            "im3-u5-x3",
            "Write the formula for $\\sqrt{x}$ shifted left $1$, stretched "
            "vertically by $2$, and lowered $3$. Then find where the graph "
            "starts and where it crosses the $x$-axis.",
            "The recipe gives $g(x) = 2\\sqrt{x + 1} - 3$. The endpoint is the "
            "parent's $(0, 0)$ carried left $1$ and down $3$: $g(-1) = -3$. "
            "Crossing: $2\\sqrt{x + 1} = 3$ gives $\\sqrt{x + 1} = \\frac{3}{2}$, "
            "so $x + 1 = \\frac{9}{4}$ and $x = \\frac{5}{4}$. Check: "
            "$g\\left(\\frac{5}{4}\\right) = 2 \\cdot \\frac{3}{2} - 3 = 0$.",
            [
                "Eq(2*sqrt(-1 + 1) - 3, -3)",
                "Eq(2*sqrt(Rational(5, 4) + 1) - 3, 0)",
                "Eq(2*sqrt(3 + 1) - 3, 1)",
            ],
        ),
        problem(
            "im3-u5-x4",
            "For $f(x) = 3x - 2$ and $g(x) = x^2 + x$, find formulas for "
            "$(f \\circ g)(x)$ and $(g \\circ f)(x)$ and show they disagree at "
            "$x = 0$.",
            "$(f \\circ g)(x) = 3(x^2 + x) - 2 = 3x^2 + 3x - 2$. "
            "$(g \\circ f)(x) = (3x - 2)^2 + (3x - 2) = 9x^2 - 9x + 2$. At "
            "$x = 0$ the first gives $-2$, the second $4 - 2 = 2$ — different "
            "functions.",
            [
                "Eq(expand(3*(x**2 + x) - 2), 3*x**2 + 3*x - 2)",
                "Eq(expand((3*x - 2)**2 + (3*x - 2)), 9*x**2 - 9*x + 2)",
                "Eq(3*0**2 + 3*0 - 2, -2)",
                "Eq(9*0**2 - 9*0 + 2, 2)",
                "Ne(-2, 2)",
            ],
        ),
        problem(
            "im3-u5-x5",
            "Write $h(x) = \\sqrt{x^2 + 9}$ as a composition $f(g(x))$, and "
            "evaluate $h(4)$ through the chain.",
            "Inner: $g(x) = x^2 + 9$, the first computation. Outer: "
            "$f(x) = \\sqrt{x}$. At $x = 4$: $g(4) = 25$, then $f(25) = 5$, so "
            "$h(4) = 5$. (Note $h$ is even — $g$ only uses $x^2$ — so "
            "$h(-4) = 5$ too.)",
            [
                "Eq(4**2 + 9, 25)",
                "Eq(sqrt(25), 5)",
                "Eq(sqrt((-4)**2 + 9), 5)",
            ],
        ),
        problem(
            "im3-u5-x6",
            "Find the inverse of $f(x) = \\dfrac{2x + 1}{3}$ and verify both "
            "compositions.",
            "Solve $y = \\frac{2x + 1}{3}$: triple, subtract $1$, halve — "
            "$x = \\frac{3y - 1}{2}$, so $f^{-1}(x) = \\frac{3x - 1}{2}$. "
            "Verify: $f(f^{-1}(x)) = \\frac{2 \\cdot \\frac{3x - 1}{2} + 1}{3} "
            "= \\frac{3x}{3} = x$, and $f^{-1}(f(x)) = \\frac{3 \\cdot "
            "\\frac{2x + 1}{3} - 1}{2} = \\frac{2x}{2} = x$. Both collapse: "
            "confirmed.",
            [
                "Eq(simplify((2*((3*x - 1)/2) + 1)/3), x)",
                "Eq(simplify((3*((2*x + 1)/3) - 1)/2), x)",
                "Eq(Rational(2*7 + 1, 3), 5)",
                "Eq(Rational(3*5 - 1, 2), 7)",
            ],
        ),
        problem(
            "im3-u5-x7",
            "The function $f(x) = (x - 3)^2$ is restricted to $x \\ge 3$. Find "
            "its inverse, and explain why the restriction was necessary.",
            "Unrestricted, $f$ repeats outputs — $f(1) = f(5) = 4$ — so no "
            "inverse exists. On $x \\ge 3$ each output has one source: solving "
            "$y = (x - 3)^2$ with $x - 3 \\ge 0$ gives $x = 3 + \\sqrt{y}$, so "
            "$f^{-1}(x) = 3 + \\sqrt{x}$. Check: $f(5) = 4$ and "
            "$f^{-1}(4) = 3 + 2 = 5$.",
            [
                "Eq((1 - 3)**2, (5 - 3)**2)",
                "Eq((5 - 3)**2, 4)",
                "Eq(3 + sqrt(4), 5)",
            ],
        ),
        problem(
            "im3-u5-x8",
            "Unit 3 claimed that $f(x) = 2^x$ and $g(x) = \\log_2 x$ are "
            "inverses. Verify the claim at $x = 3$ in both directions, and state "
            "the composition identity it illustrates.",
            "Forward through $f$ then $g$: $f(3) = 8$ and $g(8) = \\log_2 8 = "
            "3$ — back to the start. Forward through $g$ then $f$: $g(8) = 3$ "
            "and $f(3) = 8$. This is $g(f(x)) = x$ and $f(g(x)) = x$: raising "
            "and un-raising with the same base undo each other, the flagship "
            "inverse pair of the course.",
            [
                "Eq(2**3, 8)",
                "Eq(simplify(log(8, 2)), 3)",
                "Eq(simplify(log(2**5, 2)), 5)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="function-families-and-inverses",
        title="Function Families & Inverses",
        unit_number=5,
        blurb=(
            "Transformations applied to every family at once, even and odd "
            "symmetry, composing functions, and inverses — what they undo and "
            "when they exist."
        ),
        builds_on=(
            "Transformations of parabolas from IM2 Unit 3, generalised to every "
            "function — and the exponential-logarithm pair from Unit 3 becomes "
            "the flagship example of an inverse."
        ),
        lessons=[
            lesson_transformations(),
            lesson_even_odd(),
            lesson_composition(),
            lesson_inverses(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
