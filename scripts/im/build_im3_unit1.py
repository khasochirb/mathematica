#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 1: Polynomial Functions.

CCSS Integrated Math III: A-APR.2 (the Remainder Theorem: for a polynomial p
and a number a, p(a) is the remainder on division by x - a, so p(a) = 0 exactly
when x - a is a factor), A-APR.3 (identify zeros of polynomials when suitable
factorisations are available, and use the zeros to construct a rough graph),
F-IF.7c (graph polynomial functions, identifying zeros when factorisations are
available and showing end behaviour).

IM2 stopped at degree two. This unit is about what changes and what does not
when the degree rises: the leading term still decides the ends, a factor still
gives a zero, and multiplicity — which a quadratic could only show as a double
root — becomes the thing that decides whether the curve crosses or bounces.

Run: python3 scripts/im/build_im3_unit1.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — F-IF.7c: degree, leading coefficient and end behaviour
# ===========================================================================
def lesson_end_behaviour():
    return lesson(
        slug="degree-and-end-behaviour",
        title="Degree, Leading Coefficient and the Shape of the Ends",
        concrete=(
            "Zoom far enough out on any polynomial graph and the wiggles in the middle vanish. "
            "What survives is the leading term — every other term becomes invisible beside it. "
            "So two numbers, the degree and the sign of the leading coefficient, decide what the "
            "graph does at both extremes, before you compute anything at all."
        ),
        objective=(
            "Predict a polynomial's end behaviour from its degree and leading coefficient, and "
            "bound the number of zeros and turning points."
        ),
        concept=[
            "**Only the leading term matters at the extremes.** For large $|x|$, $x^{5}$ dwarfs "
            "$x^{4}$, which dwarfs $x^{3}$, and so on. At $x = 100$ the term $x^{5}$ is a hundred "
            "times $x^{4}$ — so the highest-degree term wins by an ever-widening margin, and the "
            "others stop mattering.",
            "**Even degree: both ends go the same way.** With a positive leading coefficient both "
            "ends rise; with a negative one both fall. The reason is that an even power of a "
            "negative number is positive, so the sign of the output is the same at both extremes.",
            "**Odd degree: the ends go opposite ways.** A positive leading coefficient falls on "
            "the left and rises on the right; a negative one does the reverse. An odd power keeps "
            "the sign of its input, so large negative $x$ gives large negative output.",
            "**An odd-degree polynomial always has at least one real zero.** Its ends point in "
            "opposite directions, so the graph must cross the horizontal axis somewhere. An "
            "even-degree polynomial can miss the axis entirely — $x^{2} + 1$ does.",
            "**The degree is a CEILING on the number of real zeros.** There can be fewer, if some zeros are "
            "complex or repeated, but never more. This is the ceiling the Fundamental Theorem of "
            "Algebra sets, and it is a fast plausibility check on any factorisation.",
            "**A polynomial turns at most one time fewer than its degree.** A cubic turns at most twice, a "
            "quartic at most three times. Counting the turns on a sketch gives a lower bound on "
            "the degree, which is how you read a degree off a graph.",
        ],
        key_idea=(
            "The degree's parity decides whether the ends agree, the leading coefficient's sign "
            "decides which way — and everything else about the graph lives in the middle."
        ),
        facts=[
            fact(
                "Even degree, positive lead",
                "x \\to \\pm\\infty \\Rightarrow f(x) \\to +\\infty",
                "Both ends rise, like a parabola. Negative lead: both fall.",
            ),
            fact(
                "Odd degree, positive lead",
                "x \\to -\\infty \\Rightarrow f(x) \\to -\\infty; \\quad x \\to +\\infty \\Rightarrow f(x) \\to +\\infty",
                "Down on the left, up on the right. Negative lead reverses both.",
            ),
            fact(
                "Zero count",
                "\\text{at most } n \\text{ real zeros}",
                "And an odd degree guarantees at least one, since the ends disagree.",
            ),
            fact(
                "Turning points",
                "\\text{at most } n - 1",
                "So counting turns on a graph gives a lower bound on the degree.",
            ),
        ],
        worked=[
            problem(
                "im3-u1-l1-we1",
                "Describe the end behaviour of $f(x) = -2x^{3} + 5x^{2} - x + 7$, and say how "
                "many real zeros and turning points it could have.",
                "**Find the leading term.** In standard form the highest power is $x^{3}$ with "
                "coefficient $-2$."
                "**Read the parity.** The degree $3$ is ODD, so the two ends behave differently."
                "**Read the sign.** The leading coefficient $-2$ is negative, which reverses the "
                "standard odd pattern:"
                "$$x \\to -\\infty: f(x) \\to +\\infty, \\qquad x \\to +\\infty: f(x) \\to "
                "-\\infty.$$"
                "The graph comes down from the top left and exits at the bottom right."
                "**Bound the zeros.** At most $3$, and at least $1$ — the ends are on opposite "
                "sides of the axis, so the curve must cross."
                "**Bound the turning points.** At most $3 - 1 = 2$."
                "**Check the end behaviour numerically.** At $x = 10$: "
                "$-2000 + 500 - 10 + 7 = -1503$, strongly negative ✓ At $x = -10$: "
                "$2000 + 500 + 10 + 7 = 2517$, strongly positive ✓"
                "**Notice how completely the leading term dominates.** At $x = 10$ the leading "
                "term alone is $-2000$ while everything else totals only $+497$ — under a quarter "
                "of its size, and the gap widens with every step outward.",
                [
                    "Eq(-2*10**3 + 5*10**2 - 10 + 7, -1503)",
                    "Eq(-2*(-10)**3 + 5*(-10)**2 - (-10) + 7, 2517)",
                    "Eq(-2*10**3, -2000)",
                    "Eq(5*10**2 - 10 + 7, 497)",
                    "-2*10**3 + 5*10**2 - 10 + 7 < 0",
                    "-2*(-10)**3 + 5*(-10)**2 + 10 + 7 > 0",
                ],
            ),
            problem(
                "im3-u1-l1-we2",
                "Compare the end behaviour of $g(x) = x^{4} - 3x^{2}$ and $h(x) = -x^{4} + "
                "3x^{2}$, and explain why an even-degree polynomial can have no real zeros at "
                "all.",
                "**The first.** Degree $4$ is even and the leading coefficient $1$ is positive, "
                "so BOTH ends rise:"
                "$$x \\to \\pm\\infty: g(x) \\to +\\infty.$$"
                "**The second.** Same even degree, but the leading coefficient is $-1$, so both "
                "ends fall."
                "**Check numerically.** $g(10) = 10000 - 300 = 9700$ and "
                "$g(-10) = 10000 - 300 = 9700$ — identical, because an even power erases the "
                "sign ✓ Meanwhile $h(10) = h(-10) = -9700$ ✓"
                "**Why an even degree can miss the axis.** Both ends head the same way, so the "
                "graph can sit entirely on one side. $x^{2} + 1$ has a minimum of $1$ and never "
                "reaches zero; $x^{4} + 5$ likewise."
                "**Why an odd degree cannot.** Its ends point opposite ways, so the graph is "
                "positive somewhere and negative somewhere else — and a continuous curve cannot "
                "get from one to the other without crossing."
                "**These two functions do have zeros, though.** "
                "$g(x) = x^{2}(x^{2} - 3) = 0$ at $x = 0$ and $x = \\pm\\sqrt{3}$ — three "
                "distinct real zeros, within the ceiling of four ✓",
                [
                    "Eq(10**4 - 3*10**2, 9700)",
                    "Eq((-10)**4 - 3*(-10)**2, 9700)",
                    "Eq(-(10**4) + 3*10**2, -9700)",
                    "Eq(0**4 - 3*0**2, 0)",
                    "Eq(simplify((sqrt(3))**4 - 3*(sqrt(3))**2), 0)",
                    "1**2 + 1 > 0",
                ],
            ),
            problem(
                "im3-u1-l1-we3",
                "A polynomial graph falls from the top left, turns three times, and rises to the "
                "top right, crossing the horizontal axis four times. What is the smallest "
                "possible degree, and what is the sign of the leading coefficient?",
                "**Read the ends.** Up on the left and up on the right — both ends the same, so "
                "the degree is EVEN."
                "**Read the sign.** Both ends rise, so with an even degree the leading "
                "coefficient must be POSITIVE."
                "**Use the turning points.** Three turns needs degree at least $3 + 1 = 4$."
                "**Use the zeros.** Four crossings needs degree at least $4$."
                "**Combine the three constraints.** Even, at least $4$ from the turns, at least "
                "$4$ from the crossings. The smallest even degree satisfying all of them is $4$."
                "**Check the answer is consistent.** A quartic can have four real zeros and three "
                "turning points — both at their maxima — and with a positive lead both ends rise. "
                "Every constraint is met exactly at the limit."
                "**A concrete instance.** $f(x) = (x + 2)(x + 1)(x - 1)(x - 2) = "
                "x^{4} - 5x^{2} + 4$ has zeros at $-2, -1, 1, 2$ and rises at both ends ✓ "
                "Testing: $f(0) = 4$ and $f(3) = 81 - 45 + 4 = 40$ ✓",
                [
                    "Eq(3 + 1, 4)",
                    "Eq((0 + 2)*(0 + 1)*(0 - 1)*(0 - 2), 4)",
                    "Eq(0**4 - 5*0**2 + 4, 4)",
                    "Eq(3**4 - 5*3**2 + 4, 40)",
                    "Eq(2**4 - 5*2**2 + 4, 0)",
                    "Eq((-1)**4 - 5*(-1)**2 + 4, 0)",
                ],
            ),
            problem(
                "im3-u1-l1-we4",
                "Show that $p(x) = x^{3} - 4x + 1$ has a zero between $0$ and $1$, and another "
                "between $1$ and $2$, without solving it.",
                "**Evaluate at the endpoints of the first interval.**"
                "$$p(0) = 1, \\qquad p(1) = 1 - 4 + 1 = -2.$$"
                "**Apply the sign change.** The function is positive at $0$ and negative at $1$. "
                "A polynomial is continuous — its graph has no breaks or jumps — so to get from "
                "$+1$ to $-2$ it must pass through $0$ somewhere between."
                "**Now the second interval.**"
                "$$p(1) = -2, \\qquad p(2) = 8 - 8 + 1 = 1.$$"
                "Negative to positive, so another crossing lies between $1$ and $2$."
                "**Locate a third.** $p(-3) = -27 + 12 + 1 = -14$ and $p(-2) = -8 + 8 + 1 = 1$, "
                "so a third zero lies between $-3$ and $-2$."
                "**Confirm the count is legal.** Three real zeros in a cubic — exactly the "
                "maximum, and consistent with the odd-degree guarantee of at least one ✓"
                "**Narrow the first one, to show the method continues.** "
                "$p(0.25) = 0.0156 - 1 + 1 = 0.0156$, still positive, and "
                "$p(0.3) = 0.027 - 1.2 + 1 = -0.173$, negative. So the zero lies between $0.25$ "
                "and $0.3$ — bisection will find it to any precision without any algebra."
                "**Why this matters here.** A general cubic has no factorisation you can spot, "
                "and no formula worth using by hand. Sign changes locate its roots anyway.",
                [
                    "Eq(0**3 - 4*0 + 1, 1)",
                    "Eq(1**3 - 4*1 + 1, -2)",
                    "Eq(2**3 - 4*2 + 1, 1)",
                    "Eq((-3)**3 - 4*(-3) + 1, -14)",
                    "Eq((-2)**3 - 4*(-2) + 1, 1)",
                    "Rational(1,4)**3 - 4*Rational(1,4) + 1 > 0",
                    "Rational(3,10)**3 - 4*Rational(3,10) + 1 < 0",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading end behaviour off the constant term or a middle term.",
                "Only the LEADING term matters as $|x|$ grows. For $-2x^3 + 500x^2$ the ends are "
                "governed by $-2x^3$, however large the $500$ looks at small $x$.",
            ),
            mistake(
                "Assuming a degree-5 polynomial must have five real zeros.",
                "Five is the CEILING. Some zeros may be complex or repeated. Only the count with "
                "multiplicity, over the complex numbers, is exactly $n$.",
            ),
            mistake(
                "Forgetting that a negative leading coefficient flips BOTH ends.",
                "For odd degree it swaps left and right; for even degree it turns both ends "
                "downward. Check with one large positive and one large negative input.",
            ),
            mistake(
                "Claiming a zero from a sign change without continuity.",
                "The argument works because polynomials are continuous. For a rational function "
                "with an asymptote between the two points, a sign change proves nothing.",
            ),
        ],
        try_it=[
            problem(
                "im3-u1-l1-t1",
                "Describe the end behaviour of $f(x) = 3x^{6} - x^{4} + 2x - 9$ and bound its "
                "zeros and turning points.",
                "Leading term $3x^{6}$: even degree, positive coefficient, so BOTH ends rise. At "
                "most $6$ real zeros and at most $5$ turning points; with an even degree there is "
                "no guarantee of any real zero. Check: $f(10) = 3{,}000{,}000 - 10{,}000 + 20 - "
                "9 = 2{,}990{,}011$ and $f(-10) = 3{,}000{,}000 - 10{,}000 - 20 - 9 = "
                "2{,}989{,}971$ — both large and positive ✓",
                [
                    "Eq(3*10**6 - 10**4 + 2*10 - 9, 2990011)",
                    "Eq(3*(-10)**6 - (-10)**4 + 2*(-10) - 9, 2989971)",
                    "Eq(6 - 1, 5)",
                ],
            ),
            problem(
                "im3-u1-l1-t2",
                "Show that $q(x) = x^{4} - x - 3$ has a zero between $1$ and $2$.",
                "$q(1) = 1 - 1 - 3 = -3$ and $q(2) = 16 - 2 - 3 = 11$. The sign changes from "
                "negative to positive, and a polynomial is continuous, so it must cross zero "
                "between $1$ and $2$. Narrowing: $q(1.5) = 5.0625 - 1.5 - 3 = 0.5625 > 0$, so the "
                "zero lies between $1$ and $1.5$.",
                [
                    "Eq(1**4 - 1 - 3, -3)",
                    "Eq(2**4 - 2 - 3, 11)",
                    "Rational(3,2)**4 - Rational(3,2) - 3 > 0",
                    "Eq(Rational(3,2)**4, Rational(81,16))",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "F-IF.7c",
                "title": "Two numbers decide both ends",
                "body": (
                    "The degree's parity says whether the ends agree; the leading coefficient's "
                    "sign says which way. Everything else about a polynomial graph happens in the "
                    "middle, where you have to do actual work."
                ),
                "beats": [
                    "Even degree: ends agree",
                    "Odd degree: ends disagree",
                    "Positive lead: right end up",
                    "Negative lead: flip both",
                ],
            },
            {
                "kind": "polyGraph",
                "eyebrow": "Feel the pattern",
                "title": "Step the degree and flip the sign",
                "teach": (
                    "Raise the degree and watch the ends swap between agreeing and disagreeing "
                    "with each step. Flip the sign and both arms turn over. Those two controls "
                    "are the whole of end behaviour."
                ),
                "config": {"mode": "endBehavior", "n": 3, "negative": False},
            },
            {
                "kind": "worked",
                "title": "An odd degree with a negative lead",
                "problemId": "im3-u1-l1-we1",
            },
            tap(
                "Read the ends",
                "For $f(x) = -4x^{6} + 3x^{2} - 1$, what happens as $x \\to \\pm\\infty$?",
                [
                    "both ends rise",
                    "both ends fall",
                    "down on the left, up on the right",
                    "up on the left, down on the right",
                ],
                1,
                "Degree $6$ is even, so the ends agree; the leading coefficient $-4$ is negative, "
                "so they both fall. Check at $x = 10$: $-4{,}000{,}000 + 300 - 1$, strongly "
                "negative — and the same at $x = -10$.",
                [
                    "-4*10**6 + 3*10**2 - 1 < 0",
                    "-4*(-10)**6 + 3*(-10)**2 - 1 < 0",
                    "Eq((-10)**6, 10**6)",
                ],
            ),
            {
                "kind": "worked",
                "title": "Even degree, and why it can miss the axis",
                "problemId": "im3-u1-l1-we2",
            },
            {
                "kind": "tip",
                "eyebrow": "Reading a graph",
                "title": "Count the turns for a lower bound on the degree",
                "body": (
                    "A degree-$n$ polynomial turns at most $n - 1$ times. So a graph with three "
                    "visible turns needs degree at least $4$ — and the direction of the ends then "
                    "tells you whether that degree can be exactly $4$."
                ),
            },
            {
                "kind": "worked",
                "title": "Reading the degree off a description",
                "problemId": "im3-u1-l1-we3",
            },
            tap(
                "How many turns at most?",
                "What is the maximum number of turning points on a degree-$7$ polynomial?",
                ["$7$", "$6$", "$8$", "$14$"],
                1,
                "At most $n - 1 = 6$. It may have fewer — $x^{7}$ has none at all — but never "
                "more.",
                ["Eq(7 - 1, 6)"],
            ),
            {
                "kind": "teach",
                "eyebrow": "Locating zeros",
                "title": "A sign change traps a root",
                "body": (
                    "Polynomials are continuous — no jumps, no breaks. So if the value is "
                    "positive at one point and negative at another, the curve crossed zero "
                    "somewhere in between. That locates roots you have no way to solve for."
                ),
            },
            {
                "kind": "worked",
                "title": "Trapping three roots of a cubic",
                "problemId": "im3-u1-l1-we4",
            },
            {"kind": "tryIt", "title": "A degree-6 polynomial", "problemId": "im3-u1-l1-t1"},
            {"kind": "tryIt", "title": "Trap a root", "problemId": "im3-u1-l1-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Only the leading term matters as $|x|$ grows",
                    "Even degree: ends agree. Odd degree: ends disagree",
                    "A negative leading coefficient flips both ends",
                    "At most $n$ real zeros and $n - 1$ turning points; odd degree guarantees a zero",
                    "A sign change between two points traps a root between them",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 2 — A-APR.3: zeros, multiplicity and sketching
# ===========================================================================
def lesson_zeros_and_multiplicity():
    return lesson(
        slug="zeros-and-multiplicity",
        title="Zeros, Multiplicity and Sketching from Factors",
        concrete=(
            "A factored polynomial is a set of instructions for drawing its graph. Each factor "
            "names a place where the curve touches the horizontal axis, and the POWER on that "
            "factor says whether the curve punches straight through or bounces off. Two pieces of "
            "information per factor, and the sketch follows."
        ),
        objective=(
            "Find zeros from a factorisation, use multiplicity to decide crossing or bouncing, "
            "and sketch a polynomial from its factored form."
        ),
        concept=[
            "**Each factor gives a zero, with the usual sign flip.** "
            "$(x - 3)$ gives a zero at $x = 3$; $(x + 5)$ gives one at $x = -5$; and $(2x - 1)$ "
            "gives one at $x = \\frac{1}{2}$. Set each factor to zero and solve.",
            "**Multiplicity is the exponent on the factor.** In "
            "$f(x) = (x - 1)^{3}(x + 2)^{2}$, the zero at $1$ has multiplicity $3$ and the zero "
            "at $-2$ has multiplicity $2$. The multiplicities sum to the degree — here $5$.",
            "**Odd multiplicity crosses; even multiplicity bounces.** At a zero of odd "
            "multiplicity the graph passes through the axis and the sign of $f$ changes. At even "
            "multiplicity it touches and turns back, and the sign does NOT change.",
            "**Why: the sign comes from the factor.** Near $x = a$, the factor $(x - a)^{k}$ is "
            "the only part changing sign. An odd power of a small negative number stays negative "
            "and an odd power of a small positive stays positive — so the sign flips. An even "
            "power is positive on both sides, so it does not.",
            "**Higher multiplicity flattens the curve at the zero.** A simple zero cuts through "
            "briskly; a triple zero flattens out and passes through almost horizontally. So the "
            "shape at a crossing tells you the multiplicity, not just its parity.",
            "**Sketching from factored form has a fixed procedure.** Plot the zeros; mark the "
            "$y$-intercept by substituting $x = 0$; decide the end behaviour from the degree and "
            "leading coefficient; then join them, crossing or bouncing at each zero as the "
            "multiplicity dictates.",
        ],
        key_idea=(
            "Each factor gives a zero and its exponent gives the multiplicity — odd multiplicity "
            "crosses, even multiplicity bounces."
        ),
        facts=[
            fact(
                "Factor to zero",
                "(x - a)^{k} \\ \\Rightarrow\\ \\text{zero at } x = a \\text{ of multiplicity } k",
                "The sign flips, exactly as in factored quadratics.",
            ),
            fact(
                "Multiplicities sum to the degree",
                "\\sum k_{i} = n",
                "A quick check that a factorisation is complete over the reals.",
            ),
            fact(
                "Crossing versus bouncing",
                "k \\text{ odd} \\Rightarrow \\text{crosses}; \\quad k \\text{ even} \\Rightarrow \\text{touches and turns}",
                "Because $(x-a)^k$ is the only factor changing sign near $a$.",
            ),
            fact(
                "Vertical intercept",
                "f(0) = a \\prod (-r_{i})^{k_{i}}",
                "Just substitute zero — no expansion needed.",
            ),
        ],
        worked=[
            problem(
                "im3-u1-l2-we1",
                "For $f(x) = (x - 2)^{2}(x + 1)(x - 4)$, list the zeros with multiplicities, "
                "state the degree and end behaviour, and describe the graph's behaviour at each "
                "zero.",
                "**Read the zeros with the sign flip.** $x = 2$ (multiplicity $2$), $x = -1$ "
                "(multiplicity $1$), $x = 4$ (multiplicity $1$)."
                "**Find the degree.** Add the multiplicities: $2 + 1 + 1 = 4$."
                "**Find the leading coefficient.** Multiplying the leading terms of all four "
                "factors gives $x \\cdot x \\cdot x \\cdot x = x^{4}$, so the coefficient is "
                "$+1$."
                "**End behaviour.** Even degree, positive lead — both ends rise."
                "**Behaviour at each zero.** At $x = -1$ (odd) the curve CROSSES. At $x = 2$ "
                "(even) it TOUCHES and turns back without changing sign. At $x = 4$ (odd) it "
                "crosses again."
                "**Find the vertical intercept.**"
                "$$f(0) = (-2)^{2}(1)(-4) = 4 \\times 1 \\times (-4) = -16.$$"
                "**Verify the bounce with a sign test.** Just left of $2$, at $x = 1.9$: the "
                "factors are $(-0.1)^{2} > 0$, $(2.9) > 0$, $(-2.1) < 0$, so $f$ is negative. "
                "Just right, at $x = 2.1$: $(0.1)^{2} > 0$, $(3.1) > 0$, $(-1.9) < 0$ — negative "
                "again ✓ No sign change, exactly as even multiplicity requires."
                "**Contrast with the simple zero.** At $x = 4$: At $x = 3.9$ the last factor is negative; at "
                "$x = 4.1$ it is positive, and the others are unchanged in sign — so $f$ does "
                "change sign there ✓",
                [
                    "Eq(2 + 1 + 1, 4)",
                    "Eq((0 - 2)**2*(0 + 1)*(0 - 4), -16)",
                    "(Rational(19,10) - 2)**2*(Rational(19,10) + 1)*(Rational(19,10) - 4) < 0",
                    "(Rational(21,10) - 2)**2*(Rational(21,10) + 1)*(Rational(21,10) - 4) < 0",
                    "(Rational(39,10) - 2)**2*(Rational(39,10) + 1)*(Rational(39,10) - 4) < 0",
                    "(Rational(41,10) - 2)**2*(Rational(41,10) + 1)*(Rational(41,10) - 4) > 0",
                ],
            ),
            problem(
                "im3-u1-l2-we2",
                "Compare the behaviour of $g(x) = x(x - 3)$ and $h(x) = x(x - 3)^{2}$ near "
                "$x = 3$, using sign tests.",
                "**The first function, near the shared zero.** At $x = 2.9$: $2.9 \\times (-0.1) = -0.29$, "
                "negative. At $x = 3.1$: $3.1 \\times 0.1 = 0.31$, positive. The sign CHANGED, so "
                "the graph crossed the axis."
                "**The second function, at the same point.** At $x = 2.9$: "
                "$2.9 \\times (-0.1)^{2} = 2.9 \\times 0.01 = 0.029$, positive. At $x = 3.1$: "
                "$3.1 \\times 0.01 = 0.031$, also positive. NO sign change — the graph touched "
                "and turned back."
                "**Where the difference comes from.** The squared factor is positive on both "
                "sides of $3$, because squaring destroys the sign. The unsquared factor is "
                "negative on the left and positive on the right, so it carries a sign change "
                "through."
                "**The general rule this illustrates.** Only the factor vanishing at that point "
                "can change sign there; every other factor is safely away from zero and keeps its "
                "sign. So the parity of that one exponent decides everything."
                "**Check both still vanish at 3.** $g(3) = 3 \\times 0 = 0$ ✓ and "
                "$h(3) = 3 \\times 0 = 0$ ✓ Both have a zero there — they differ only in what "
                "the curve does on arrival.",
                [
                    "Eq(3*(3 - 3), 0)",
                    "Eq(3*(3 - 3)**2, 0)",
                    "Rational(29,10)*(Rational(29,10) - 3) < 0",
                    "Rational(31,10)*(Rational(31,10) - 3) > 0",
                    "Rational(29,10)*(Rational(29,10) - 3)**2 > 0",
                    "Rational(31,10)*(Rational(31,10) - 3)**2 > 0",
                ],
            ),
            problem(
                "im3-u1-l2-we3",
                "Write a polynomial of degree $4$ with zeros at $-3$ (multiplicity $1$), $1$ "
                "(multiplicity $2$) and $2$ (multiplicity $1$), passing through $(0, 12)$.",
                "**Build the factors from the zeros.** Each zero $r$ with multiplicity $k$ "
                "contributes $(x - r)^{k}$:"
                "$$f(x) = a(x + 3)(x - 1)^{2}(x - 2).$$"
                "**Check the degree.** $1 + 2 + 1 = 4$ ✓ as required."
                "**Use the given point to find the multiplier.** Substituting $(0, 12)$:"
                "$$12 = a(3)(1)(-2) = -6a \\quad\\Longrightarrow\\quad a = -2.$$"
                "**Write the answer.**"
                "$$f(x) = -2(x + 3)(x - 1)^{2}(x - 2).$$"
                "**Check the given point.** $-2(3)(1)(-2) = 12$ ✓"
                "**Check a zero.** $f(1) = -2(4)(0)(-1) = 0$ ✓ and it is a double zero, so the "
                "curve bounces there."
                "**Describe the graph, for free.** The leading coefficient is $-2 < 0$ and the "
                "degree is even, so both ends fall. The curve crosses at $-3$, bounces off the "
                "axis at $1$, crosses at $2$, and passes through $(0, 12)$."
                "**Sanity-check the sign between zeros.** At $x = 0$, between $-3$ and $1$, the "
                "value is $+12$ — above the axis. At $x = 3$, beyond the last zero: "
                "$-2(6)(4)(1) = -48$, below the axis ✓ consistent with both ends falling.",
                [
                    "Eq(-2*(0 + 3)*(0 - 1)**2*(0 - 2), 12)",
                    "Eq(-2*(1 + 3)*(1 - 1)**2*(1 - 2), 0)",
                    "Eq(-2*(-3 + 3)*(-3 - 1)**2*(-3 - 2), 0)",
                    "Eq(-2*(2 + 3)*(2 - 1)**2*(2 - 2), 0)",
                    "Eq(-2*(3 + 3)*(3 - 1)**2*(3 - 2), -48)",
                    "Eq(1 + 2 + 1, 4)",
                ],
            ),
            problem(
                "im3-u1-l2-we4",
                "Sketch $f(x) = -x^{3}(x - 2)^{2}(x + 1)$ by finding its zeros, multiplicities, "
                "degree, end behaviour and the sign on each interval.",
                "**Zeros and multiplicities.** $x = 0$ (multiplicity $3$, odd — crosses, but "
                "flattened), $x = 2$ (multiplicity $2$, even — bounces), $x = -1$ (multiplicity "
                "$1$, odd — crosses)."
                "**Degree and leading coefficient.** $3 + 2 + 1 = 6$, and the leading term is "
                "$-x^{3} \\cdot x^{2} \\cdot x = -x^{6}$, so the coefficient is $-1$."
                "**End behaviour.** Even degree with a negative lead — BOTH ends fall."
                "**Test the sign on each interval.** The zeros split the line into four pieces."
                "$$x < -1: \\ f(-2) = -(-8)(16)(-1) = -128 \\ (\\text{negative})$$"
                "$$-1 < x < 0: \\ f(-0.5) = -(-0.125)(6.25)(0.5) = 0.39 \\ (\\text{positive})$$"
                "$$0 < x < 2: \\ f(1) = -(1)(1)(2) = -2 \\ (\\text{negative})$$"
                "$$x > 2: \\ f(3) = -(27)(1)(4) = -108 \\ (\\text{negative})$$"
                "**Check the signs against the multiplicities.** Crossing at $-1$: negative to "
                "positive ✓ Crossing at $0$: positive to negative ✓ Bouncing at $2$: negative "
                "to negative ✓ Every sign change matches the parity of the multiplicity, which is "
                "the point of the whole exercise."
                "**Describe the sketch.** The curve rises from the bottom left, crosses at $-1$ "
                "into positive territory, flattens as it crosses at $0$ (the triple zero), stays "
                "negative, touches the axis at $2$ without crossing, and falls away to the bottom "
                "right.",
                [
                    "Eq(-((-2)**3)*((-2) - 2)**2*((-2) + 1), -128)",
                    "Eq(-(1**3)*(1 - 2)**2*(1 + 1), -2)",
                    "Eq(-(3**3)*(3 - 2)**2*(3 + 1), -108)",
                    "-(Rational(-1,2)**3)*(Rational(-1,2) - 2)**2*(Rational(-1,2) + 1) > 0",
                    "Eq(3 + 2 + 1, 6)",
                    "Eq(-(0**3)*(0 - 2)**2*(0 + 1), 0)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading the zeros of $(x + 4)^2$ as $x = 4$.",
                "The factor vanishes at $x = -4$. The sign flips, exactly as with factored "
                "quadratics — and the multiplicity $2$ means the graph bounces there.",
            ),
            mistake(
                "Assuming every zero is a crossing.",
                "Only zeros of ODD multiplicity cross. Even multiplicity touches and turns back, "
                "with no sign change — which a single sign test either side confirms.",
            ),
            mistake(
                "Forgetting the leading coefficient when building from zeros.",
                "Zeros fix the factors but not the vertical scale. One extra point is needed to "
                "determine $a$, and without it infinitely many polynomials fit.",
            ),
            mistake(
                "Adding the number of DISTINCT zeros to get the degree.",
                "Add the MULTIPLICITIES. $(x-1)^3(x+2)^2$ has two distinct zeros but degree $5$.",
            ),
        ],
        try_it=[
            problem(
                "im3-u1-l2-t1",
                "For $f(x) = (x + 2)^{3}(x - 1)$, give the zeros with multiplicities, the degree, "
                "the end behaviour, and say what happens at each zero.",
                "Zeros: $x = -2$ (multiplicity $3$) and $x = 1$ (multiplicity $1$). Degree "
                "$3 + 1 = 4$, leading coefficient $+1$, so both ends rise. At $x = -2$ the "
                "multiplicity is odd, so it crosses — flattening as it does, because the "
                "multiplicity is $3$. At $x = 1$ it crosses normally. Vertical intercept: "
                "$(2)^{3}(-1) = -8$.",
                [
                    "Eq((0 + 2)**3*(0 - 1), -8)",
                    "Eq(3 + 1, 4)",
                    "Eq((-2 + 2)**3*(-2 - 1), 0)",
                    "(Rational(-21,10) + 2)**3*(Rational(-21,10) - 1) > 0",
                    "(Rational(-19,10) + 2)**3*(Rational(-19,10) - 1) < 0",
                ],
            ),
            problem(
                "im3-u1-l2-t2",
                "Write a degree-$3$ polynomial with a double zero at $2$ and a single zero at "
                "$-1$, passing through $(0, 8)$.",
                "Start with $f(x) = a(x - 2)^{2}(x + 1)$. Substituting $(0, 8)$: "
                "$a(4)(1) = 4a = 8$, so $a = 2$. The answer is "
                "$f(x) = 2(x - 2)^{2}(x + 1)$. Check: $f(0) = 2(4)(1) = 8$ ✓ and "
                "$f(2) = 0$ ✓ The curve bounces at $2$ and crosses at $-1$; odd degree with a "
                "positive lead, so it falls left and rises right.",
                [
                    "Eq(2*(0 - 2)**2*(0 + 1), 8)",
                    "Eq(2*(2 - 2)**2*(2 + 1), 0)",
                    "Eq(2*(-1 - 2)**2*(-1 + 1), 0)",
                    "Eq(2 + 1, 3)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-APR.3",
                "title": "A factored polynomial is a sketch waiting to be drawn",
                "body": (
                    "Each factor names a zero, and its exponent says whether the curve crosses or "
                    "bounces there. Add the end behaviour and the vertical intercept and the "
                    "sketch is complete."
                ),
                "beats": [
                    "Factor $\\to$ zero (sign flips)",
                    "Exponent $\\to$ multiplicity",
                    "Odd: crosses. Even: bounces",
                    "Multiplicities sum to the degree",
                ],
            },
            {
                "kind": "polyGraph",
                "eyebrow": "See the zeros",
                "title": "Move a zero and watch the curve follow",
                "teach": (
                    "Drag a zero along the axis. The curve is pinned to the axis exactly there, "
                    "and the pieces between the zeros flex to accommodate it — a factored "
                    "polynomial really is a set of instructions for where the graph must touch "
                    "down."
                ),
                "config": {"mode": "zeros", "n": 3, "negative": False},
            },
            {
                "kind": "worked",
                "title": "Reading everything off a factorisation",
                "problemId": "im3-u1-l2-we1",
            },
            tap(
                "Read the multiplicity",
                "In $f(x) = (x - 5)^{4}(x + 2)$, what does the graph do at $x = 5$?",
                [
                    "crosses the axis",
                    "touches the axis and turns back",
                    "has a vertical asymptote",
                    "is undefined",
                ],
                1,
                "The multiplicity is $4$ — even — so the curve touches and turns without changing "
                "sign. At $x = -2$ the multiplicity is $1$, odd, and there it does cross.",
                [
                    "Eq((5 - 5)**4*(5 + 2), 0)",
                    "(Rational(49,10) - 5)**4*(Rational(49,10) + 2) > 0",
                    "(Rational(51,10) - 5)**4*(Rational(51,10) + 2) > 0",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Why parity decides it",
                "title": "Only one factor changes sign near a zero",
                "body": (
                    "Near $x = a$ every factor except $(x - a)^{k}$ keeps its sign — they are all "
                    "safely away from zero. So the parity of that one exponent decides whether "
                    "the product changes sign, and therefore whether the curve crosses."
                ),
            },
            {
                "kind": "worked",
                "title": "Crossing against bouncing, by sign test",
                "problemId": "im3-u1-l2-we2",
            },
            {
                "kind": "tip",
                "eyebrow": "Building one",
                "title": "Zeros fix the factors; a point fixes the scale",
                "body": (
                    "Every polynomial with the same zeros and multiplicities differs only by a "
                    "constant multiplier. One extra point pins it down — which is why these "
                    "questions always supply one."
                ),
            },
            {
                "kind": "worked",
                "title": "Constructing a polynomial from its zeros",
                "problemId": "im3-u1-l2-we3",
            },
            tap(
                "What is the degree?",
                "What is the degree of $f(x) = (x - 1)^{2}(x + 3)^{3}(x - 5)$?",
                ["$3$", "$6$", "$5$", "$18$"],
                1,
                "Add the MULTIPLICITIES, not the number of distinct zeros: "
                "$2 + 3 + 1 = 6$. There are three distinct zeros but the degree is six.",
                ["Eq(2 + 3 + 1, 6)"],
            ),
            {
                "kind": "worked",
                "title": "A full sketch, interval by interval",
                "problemId": "im3-u1-l2-we4",
            },
            {"kind": "tryIt", "title": "A triple zero", "problemId": "im3-u1-l2-t1"},
            {"kind": "tryIt", "title": "Build from zeros and a point", "problemId": "im3-u1-l2-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Each factor gives a zero; the exponent gives its multiplicity",
                    "Odd multiplicity crosses; even multiplicity touches and turns",
                    "Higher odd multiplicity flattens the crossing",
                    "Multiplicities sum to the degree",
                    "To sketch: zeros, intercept, end behaviour, then sign-test each interval",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 3 — A-APR.2: division, the remainder and factor theorems
# ===========================================================================
def lesson_division_and_remainder():
    return lesson(
        slug="division-and-the-remainder-theorem",
        title="Polynomial Division and the Remainder Theorem",
        concrete=(
            "Dividing $17$ by $5$ gives $3$ remainder $2$, which is the statement "
            "$17 = 5 \\times 3 + 2$. Polynomial division says exactly the same thing with "
            "polynomials — and the remarkable part is that when you divide by $x - a$, the "
            "remainder is not something you have to compute. It is just $p(a)$."
        ),
        objective=(
            "Divide polynomials, state the division algorithm, and use the Remainder and Factor "
            "Theorems to test factors and find zeros."
        ),
        concept=[
            "**The division algorithm, for polynomials.** "
            "$p(x) = d(x)q(x) + r(x)$ where the remainder $r$ has smaller degree than the divisor "
            "$d$. Dividing by a linear $x - a$ therefore leaves a CONSTANT remainder — degree "
            "less than one means degree zero.",
            "**The Remainder Theorem.** When $p(x)$ is divided by $x - a$, the remainder is "
            "exactly $p(a)$. The proof is one substitution: putting $x = a$ into "
            "$p(x) = (x - a)q(x) + r$ kills the first term, leaving $p(a) = r$.",
            "**The Factor Theorem is the zero case.** $x - a$ is a factor of $p$ exactly when "
            "$p(a) = 0$. So testing a factor costs one substitution rather than a full division — "
            "and every zero you find hands you a factor.",
            "**Synthetic division is a shorthand for dividing by a linear factor.** Write the "
            "coefficients, bring down the first, multiply by $a$, add, repeat. The last number is "
            "the remainder and the others are the quotient's coefficients. It is the same "
            "arithmetic as long division with the bookkeeping stripped out.",
            "**Finding one zero reduces the degree.** Divide a cubic by the factor you found and "
            "what remains is a quadratic — which you can always finish. That is the standard "
            "route through a cubic: find one rational root, divide, solve the quadratic.",
            "**The Rational Root Theorem narrows the search.** Any rational zero "
            "$\\frac{p}{q}$ in lowest terms has $p$ dividing the constant term and $q$ dividing "
            "the leading coefficient. That turns an infinite search into a short list to test.",
        ],
        key_idea=(
            "The remainder on dividing by $x - a$ is $p(a)$ — so testing a factor is one "
            "substitution, and finding one zero drops the degree by one."
        ),
        facts=[
            fact(
                "Division algorithm",
                "p(x) = d(x)q(x) + r(x), \\quad \\deg r < \\deg d",
                "Exactly the integer statement, with polynomials.",
            ),
            fact(
                "Remainder Theorem",
                "p(x) \\div (x - a) \\ \\Rightarrow\\ \\text{remainder} = p(a)",
                "One substitution replaces an entire division.",
            ),
            fact(
                "Factor Theorem",
                "(x - a) \\mid p(x) \\iff p(a) = 0",
                "The zero case of the Remainder Theorem — and the bridge from zeros to factors.",
            ),
            fact(
                "Rational Root Theorem",
                "\\frac{p}{q}: \\ p \\mid a_{0}, \\quad q \\mid a_{n}",
                "Turns an infinite search for rational zeros into a finite list.",
            ),
        ],
        worked=[
            problem(
                "im3-u1-l3-we1",
                "Divide $p(x) = 2x^{3} - 5x^{2} + 3x - 7$ by $x - 3$ using synthetic division, "
                "and confirm the remainder with the Remainder Theorem.",
                "**Set up the coefficients.** In standard form: $2, -5, 3, -7$. The divisor "
                "$x - 3$ gives $a = 3$."
                "**Run the synthetic division.** Bring down the $2$. Multiply by $3$ and add to "
                "the next coefficient:"
                "$$2, \\quad -5 + 6 = 1, \\quad 3 + 3 = 6, \\quad -7 + 18 = 11.$$"
                "**Read the result.** The quotient's coefficients are $2, 1, 6$ and the remainder "
                "is $11$:"
                "$$2x^{3} - 5x^{2} + 3x - 7 = (x - 3)(2x^{2} + x + 6) + 11.$$"
                "**Confirm with the Remainder Theorem.** The remainder should equal $p(3)$:"
                "$$p(3) = 54 - 45 + 9 - 7 = 11 \\ \\checkmark$$"
                "One substitution reproduced the whole division's final number."
                "**Verify the identity at another value.** At $x = 0$: the left side is $-7$, and "
                "the right is $(-3)(6) + 11 = -18 + 11 = -7$ ✓"
                "**What the non-zero remainder tells you.** $x - 3$ is NOT a factor, since "
                "$p(3) \\neq 0$. Had we only wanted to know that, the substitution alone would "
                "have sufficed and the division was unnecessary.",
                [
                    "Eq(2*3**3 - 5*3**2 + 3*3 - 7, 11)",
                    "Eq(-5 + 6, 1)",
                    "Eq(3 + 3, 6)",
                    "Eq(-7 + 18, 11)",
                    "Eq((0 - 3)*(2*0**2 + 0 + 6) + 11, -7)",
                    "Eq(2*0**3 - 5*0**2 + 3*0 - 7, -7)",
                    "Eq((1 - 3)*(2*1**2 + 1 + 6) + 11, 2*1**3 - 5*1**2 + 3*1 - 7)",
                ],
            ),
            problem(
                "im3-u1-l3-we2",
                "Prove the Remainder Theorem, then use it to decide whether $x + 2$ is a factor "
                "of $q(x) = x^{4} + 3x^{3} - x - 6$.",
                "**Start from the division algorithm.** Dividing $p$ by $x - a$ gives"
                "$$p(x) = (x - a)Q(x) + r,$$"
                "where $r$ is a CONSTANT, because the remainder's degree must be less than the "
                "divisor's degree of $1$."
                "**Substitute the divisor's root.** The first term vanishes:"
                "$$p(a) = (a - a)Q(a) + r = 0 + r = r. \\qquad \\blacksquare$$"
                "The remainder is $p(a)$, and the proof is one line."
                "**Now the test.** $x + 2$ is $x - (-2)$, so $a = -2$:"
                "$$q(-2) = 16 - 24 + 2 - 6 = -12.$$"
                "**Conclude.** The remainder is $-12$, not zero, so $x + 2$ is NOT a factor."
                "**Test a different candidate.** Try $x - 1$, so $a = 1$:"
                "$$q(1) = 1 + 3 - 1 - 6 = -3,$$"
                "also not a factor. Try $a = -1$: $1 - 3 + 1 - 6 = -7$, no."
                "**Use the Rational Root Theorem to bound the search.** The constant is $-6$ and "
                "the leading coefficient is $1$, so any rational zero divides $6$: the candidates "
                "are $\\pm 1, \\pm 2, \\pm 3, \\pm 6$. Testing $a = -3$: "
                "$81 - 81 + 3 - 6 = -3$, no. And $a = 2$: $16 + 24 - 2 - 6 = 32$, no."
                "**What the failures establish.** None of the eight candidates works, so $q$ has "
                "NO rational zeros — a definite conclusion reached by a finite search, which is "
                "exactly what the Rational Root Theorem is for.",
                [
                    "Eq((-2)**4 + 3*(-2)**3 - (-2) - 6, -12)",
                    "Eq(1**4 + 3*1**3 - 1 - 6, -3)",
                    "Eq((-1)**4 + 3*(-1)**3 - (-1) - 6, -7)",
                    "Eq((-3)**4 + 3*(-3)**3 - (-3) - 6, -3)",
                    "Eq(2**4 + 3*2**3 - 2 - 6, 32)",
                    "Eq(3**4 + 3*3**3 - 3 - 6, 153)",
                    "Eq(6**4 + 3*6**3 - 6 - 6, 1932)",
                    "Eq((-6)**4 + 3*(-6)**3 - (-6) - 6, 648)",
                ],
            ),
            problem(
                "im3-u1-l3-we3",
                "Factor $p(x) = x^{3} - 6x^{2} + 11x - 6$ completely, and find all its zeros.",
                "**List the rational candidates.** The constant is $-6$ and the leading "
                "coefficient is $1$, so any rational zero divides $6$: "
                "$\\pm 1, \\pm 2, \\pm 3, \\pm 6$."
                "**Test the smallest first.**"
                "$$p(1) = 1 - 6 + 11 - 6 = 0 \\ \\checkmark$$"
                "So $x - 1$ is a factor."
                "**Divide it out.** Synthetic division with $a = 1$ on $1, -6, 11, -6$:"
                "$$1, \\quad -6 + 1 = -5, \\quad 11 - 5 = 6, \\quad -6 + 6 = 0.$$"
                "The remainder is $0$ ✓ and the quotient is $x^{2} - 5x + 6$."
                "**Factor the quadratic.** Two numbers with product $6$ and sum $-5$: $-2$ and "
                "$-3$:"
                "$$x^{2} - 5x + 6 = (x - 2)(x - 3).$$"
                "**Write the complete factorisation.**"
                "$$p(x) = (x - 1)(x - 2)(x - 3),$$"
                "with zeros $1$, $2$ and $3$ — all simple, so the curve crosses at each."
                "**Verify all three.** $p(2) = 8 - 24 + 22 - 6 = 0$ ✓ and "
                "$p(3) = 27 - 54 + 33 - 6 = 0$ ✓"
                "**Check by expanding at one value.** At $x = 0$: the factored form gives "
                "$(-1)(-2)(-3) = -6$, matching the constant term ✓"
                "**The general strategy this demonstrates.** Find one rational root, divide to "
                "drop the degree, then finish with a quadratic you can always solve. Every "
                "solvable cubic yields to it.",
                [
                    "Eq(1**3 - 6*1**2 + 11*1 - 6, 0)",
                    "Eq(2**3 - 6*2**2 + 11*2 - 6, 0)",
                    "Eq(3**3 - 6*3**2 + 11*3 - 6, 0)",
                    "Eq((0 - 1)*(0 - 2)*(0 - 3), -6)",
                    "Eq(-6 + 1, -5)",
                    "Eq(11 - 5, 6)",
                    "Eq((-2)*(-3), 6)",
                    "Eq(-2 + (-3), -5)",
                ],
            ),
            problem(
                "im3-u1-l3-we4",
                "Find the value of $k$ for which $x - 2$ is a factor of "
                "$f(x) = x^{3} + kx^{2} - 4x + 12$, and then factor the result completely.",
                "**Apply the Factor Theorem.** $x - 2$ is a factor exactly when $f(2) = 0$:"
                "$$f(2) = 8 + 4k - 8 + 12 = 4k + 12.$$"
                "**Set it to zero and solve.**"
                "$$4k + 12 = 0 \\quad\\Longrightarrow\\quad k = -3.$$"
                "**Write the polynomial.**"
                "$$f(x) = x^{3} - 3x^{2} - 4x + 12.$$"
                "**Confirm the factor.** $f(2) = 8 - 12 - 8 + 12 = 0$ ✓"
                "**Divide out the factor.** Synthetic division with $a = 2$ on $1, -3, -4, 12$:"
                "$$1, \\quad -3 + 2 = -1, \\quad -4 - 2 = -6, \\quad 12 - 12 = 0.$$"
                "Remainder $0$ ✓ quotient $x^{2} - x - 6$."
                "**Factor the quadratic.** Product $-6$, sum $-1$: $2$ and $-3$:"
                "$$x^{2} - x - 6 = (x + 2)(x - 3).$$"
                "**Complete factorisation.**"
                "$$f(x) = (x - 2)(x + 2)(x - 3),$$"
                "with zeros $2$, $-2$ and $3$."
                "**Verify the other two zeros.** $f(-2) = -8 - 12 + 8 + 12 = 0$ ✓ and "
                "$f(3) = 27 - 27 - 12 + 12 = 0$ ✓"
                "**Check the constant term.** The product of the negated zeros is "
                "$(-2)(2)(-3) = 12$ ✓ matching the polynomial's constant, which is a useful check "
                "on any complete factorisation.",
                [
                    "Eq(4*(-3) + 12, 0)",
                    "Eq(2**3 - 3*2**2 - 4*2 + 12, 0)",
                    "Eq((-2)**3 - 3*(-2)**2 - 4*(-2) + 12, 0)",
                    "Eq(3**3 - 3*3**2 - 4*3 + 12, 0)",
                    "Eq(-3 + 2, -1)",
                    "Eq(-4 - 2, -6)",
                    "Eq((0 - 2)*(0 + 2)*(0 - 3), 12)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Using $a = -3$ when dividing by $x - 3$.",
                "The Remainder Theorem uses the value that makes the divisor zero. For $x - 3$ "
                "that is $a = +3$; for $x + 2$ it is $a = -2$.",
            ),
            mistake(
                "Omitting a zero coefficient in synthetic division.",
                "$x^3 - 4$ has coefficients $1, 0, 0, -4$. Skipping the missing powers shifts "
                "every subsequent number and ruins the result.",
            ),
            mistake(
                "Concluding a polynomial has no zeros when the rational candidates all fail.",
                "It has no RATIONAL zeros. It may still have irrational or complex ones — an "
                "odd-degree polynomial always has at least one real zero.",
            ),
            mistake(
                "Dividing when a substitution would answer the question.",
                "To test whether $x - a$ is a factor, compute $p(a)$. The full division is only "
                "needed once you know it IS a factor and want the quotient.",
            ),
        ],
        try_it=[
            problem(
                "im3-u1-l3-t1",
                "Find the remainder when $p(x) = x^{4} - 2x^{3} + x - 5$ is divided by $x + 1$, "
                "and say whether $x + 1$ is a factor.",
                "The divisor $x + 1$ means $a = -1$. By the Remainder Theorem the remainder is "
                "$p(-1) = 1 + 2 - 1 - 5 = -3$. Since this is not zero, $x + 1$ is NOT a factor. "
                "One substitution answered both questions.",
                [
                    "Eq((-1)**4 - 2*(-1)**3 + (-1) - 5, -3)",
                    "Ne(-3, 0)",
                ],
            ),
            problem(
                "im3-u1-l3-t2",
                "Factor $p(x) = x^{3} + 2x^{2} - 5x - 6$ completely.",
                "Rational candidates divide $6$: $\\pm 1, \\pm 2, \\pm 3, \\pm 6$. Testing "
                "$x = -1$: $-1 + 2 + 5 - 6 = 0$ ✓ so $x + 1$ is a factor. Dividing gives "
                "$x^{2} + x - 6 = (x + 3)(x - 2)$. So "
                "$p(x) = (x + 1)(x + 3)(x - 2)$, with zeros $-1$, $-3$ and $2$. Check the "
                "constant: $(1)(3)(-2) = -6$ ✓",
                [
                    "Eq((-1)**3 + 2*(-1)**2 - 5*(-1) - 6, 0)",
                    "Eq((-3)**3 + 2*(-3)**2 - 5*(-3) - 6, 0)",
                    "Eq(2**3 + 2*2**2 - 5*2 - 6, 0)",
                    "Eq((0 + 1)*(0 + 3)*(0 - 2), -6)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-APR.2",
                "title": "Division, exactly as with integers",
                "body": (
                    "$17 = 5 \\times 3 + 2$ becomes $p(x) = d(x)q(x) + r(x)$, with the remainder "
                    "smaller than the divisor. Dividing by a linear factor therefore leaves a "
                    "constant — and that constant turns out to be free."
                ),
                "beats": [
                    "$p = dq + r$, $\\deg r < \\deg d$",
                    "Linear divisor $\\to$ constant remainder",
                    "That constant is $p(a)$",
                    "Zero remainder $\\to$ it is a factor",
                ],
            },
            {
                "kind": "worked",
                "title": "Synthetic division, checked by substitution",
                "problemId": "im3-u1-l3-we1",
            },
            tap(
                "Which value do you substitute?",
                "To find the remainder when dividing by $x + 4$, which value do you put into the "
                "polynomial?",
                ["$4$", "$-4$", "$\\frac{1}{4}$", "$0$"],
                1,
                "Use the value that makes the divisor zero: $x + 4 = 0$ gives $x = -4$. The "
                "remainder is $p(-4)$.",
                ["Eq(-4 + 4, 0)", "Ne(4 + 4, 0)"],
            ),
            {
                "kind": "stepProof",
                "eyebrow": "One substitution",
                "title": "Why the remainder is $p(a)$",
                "teach": (
                    "The division algorithm plus a single substitution proves it. Nothing "
                    "elaborate is needed — the whole theorem is that setting $x = a$ annihilates "
                    "the quotient term."
                ),
                "config": {
                    "given": "p(x) divided by (x - a) gives quotient Q(x) and remainder r",
                    "prove": "r = p(a)",
                    "rows": [
                        {
                            "statement": "p(x) = (x - a)Q(x) + r",
                            "reason": "the division algorithm",
                        },
                        {
                            "statement": "r is a constant",
                            "reason": "its degree is less than the divisor's degree of 1",
                        },
                        {
                            "statement": "p(a) = (a - a)Q(a) + r",
                            "reason": "substitute x = a",
                        },
                        {"statement": "p(a) = 0 + r", "reason": "a - a = 0"},
                        {"statement": "r = p(a)", "reason": "simplify"},
                    ],
                },
            },
            {
                "kind": "worked",
                "title": "The proof, and a factor test",
                "problemId": "im3-u1-l3-we2",
            },
            {
                "kind": "tip",
                "eyebrow": "Narrow the search",
                "title": "Rational zeros divide the constant over the lead",
                "body": (
                    "Any rational zero $\\frac{p}{q}$ has $p$ dividing the constant term and $q$ "
                    "dividing the leading coefficient. With a leading coefficient of $1$ that "
                    "reduces to: the zero divides the constant. A short list, not a search."
                ),
            },
            {
                "kind": "worked",
                "title": "One root, then a quadratic",
                "problemId": "im3-u1-l3-we3",
            },
            tap(
                "Is it a factor?",
                "For $p(x) = x^{3} - 7x + 6$, is $x - 2$ a factor?",
                [
                    "yes — $p(2) = 0$",
                    "no — $p(2) = 8$",
                    "no — $p(-2) \\neq 0$",
                    "you must divide to find out",
                ],
                0,
                "$p(2) = 8 - 14 + 6 = 0$, so by the Factor Theorem $x - 2$ IS a factor. One "
                "substitution settles it — no division required.",
                [
                    "Eq(2**3 - 7*2 + 6, 0)",
                    "Eq(1**3 - 7*1 + 6, 0)",
                    "Eq((-3)**3 - 7*(-3) + 6, 0)",
                ],
            ),
            {
                "kind": "worked",
                "title": "Solving for an unknown coefficient",
                "problemId": "im3-u1-l3-we4",
            },
            {"kind": "tryIt", "title": "A remainder by substitution", "problemId": "im3-u1-l3-t1"},
            {"kind": "tryIt", "title": "Factor a cubic completely", "problemId": "im3-u1-l3-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "$p(x) = d(x)q(x) + r(x)$ with $\\deg r < \\deg d$",
                    "Dividing by $x - a$ leaves remainder $p(a)$ — one substitution",
                    "$x - a$ is a factor exactly when $p(a) = 0$",
                    "Rational zeros divide the constant over the leading coefficient",
                    "Find one root, divide, and finish with a quadratic",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 4 — A-APR.1/A-SSE: operations, identities and applications
# ===========================================================================
def lesson_operations_and_identities():
    return lesson(
        slug="polynomial-operations-and-identities",
        title="Operations, Identities and Polynomial Models",
        concrete=(
            "A box folded from a flat sheet has a volume that is a polynomial in the size of the "
            "corner cut — and the useful range of that polynomial stops where the box stops being "
            "physically possible. Polynomials model well and mislead easily, and telling the two "
            "apart is the point of this lesson."
        ),
        objective=(
            "Multiply and factor higher-degree polynomials using the sum and difference of cubes "
            "and structural substitution, and build and interpret polynomial models."
        ),
        concept=[
            "**The sum and difference of cubes.** "
            "$a^{3} - b^{3} = (a - b)(a^{2} + ab + b^{2})$ and "
            "$a^{3} + b^{3} = (a + b)(a^{2} - ab + b^{2})$. Note that unlike the sum of SQUARES, "
            "a sum of CUBES does factor over the reals — the odd power makes the difference.",
            "**Remember the signs by their pattern.** The linear factor takes the SAME sign as "
            "the original; the middle term of the quadratic takes the OPPOSITE. And the quadratic "
            "factor never factors further over the reals, which is a useful thing to know before "
            "trying.",
            "**Structural substitution turns hard expressions into familiar ones.** "
            "$x^{4} - 13x^{2} + 36$ becomes $u^{2} - 13u + 36$ under $u = x^{2}$, factors as "
            "$(u - 4)(u - 9)$, and unpacks to $(x^{2} - 4)(x^{2} - 9) = "
            "(x - 2)(x + 2)(x - 3)(x + 3)$.",
            "**Grouping still works on four terms of any degree.** "
            "$x^{3} + 3x^{2} - 4x - 12 = x^{2}(x + 3) - 4(x + 3) = (x + 3)(x^{2} - 4)$, and then "
            "the difference of squares finishes it. Nothing about the technique required degree "
            "two.",
            "**A polynomial model's DOMAIN is usually smaller than the polynomial's.** A box "
            "volume $V(x) = x(20 - 2x)(16 - 2x)$ is a perfectly good cubic for every real $x$, "
            "but only $0 < x < 8$ describes a box that can exist. Stating that restriction is "
            "part of the answer.",
            "**Read a model's turning point as its optimum.** Where the volume function turns is "
            "where the box is largest — and locating it numerically, by testing values, is "
            "entirely legitimate before calculus supplies an exact method.",
        ],
        key_idea=(
            "The cube identities and structural substitution extend factoring past degree two — "
            "and every polynomial MODEL carries a domain narrower than the polynomial's own."
        ),
        facts=[
            fact(
                "Difference of cubes",
                "a^{3} - b^{3} = (a - b)(a^{2} + ab + b^{2})",
                "Same sign in the linear factor, opposite in the middle term.",
            ),
            fact(
                "Sum of cubes",
                "a^{3} + b^{3} = (a + b)(a^{2} - ab + b^{2})",
                "Unlike a sum of squares, this one DOES factor over the reals.",
            ),
            fact(
                "Structural substitution",
                "x^{4} + bx^{2} + c \\ \\xrightarrow{\\ u = x^{2}\\ } \\ u^{2} + bu + c",
                "Any quadratic in disguise yields to the same trinomial method.",
            ),
            fact(
                "Model domain",
                "\\text{physical constraints} \\subseteq \\text{algebraic domain}",
                "The formula outlives the situation; say where the model is valid.",
            ),
        ],
        worked=[
            problem(
                "im3-u1-l4-we1",
                "Factor $8x^{3} - 27$ and $x^{3} + 64$ completely.",
                "**Recognise the first as a difference of cubes.** "
                "$8x^{3} = (2x)^{3}$ and $27 = 3^{3}$, so $a = 2x$ and $b = 3$:"
                "$$8x^{3} - 27 = (2x - 3)\\left(4x^{2} + 6x + 9\\right).$$"
                "The linear factor takes the same sign as the original; the middle term of the "
                "quadratic takes the opposite."
                "**Check the quadratic cannot factor further.** Its discriminant is "
                "$36 - 4(4)(9) = 36 - 144 = -108 < 0$, so it has no real zeros ✓ The "
                "factorisation is complete."
                "**Now the second, a SUM of cubes.** $64 = 4^{3}$, so $a = x$ and $b = 4$:"
                "$$x^{3} + 64 = (x + 4)\\left(x^{2} - 4x + 16\\right).$$"
                "**Check that quadratic too.** $16 - 64 = -48 < 0$ ✓ irreducible."
                "**Verify the first by expanding at a value.** At $x = 2$: the original is "
                "$64 - 27 = 37$, and the factored form is $(1)(16 + 12 + 9) = 37$ ✓"
                "**Verify the second.** At $x = 1$: $1 + 64 = 65$, and "
                "$(5)(1 - 4 + 16) = 5 \\times 13 = 65$ ✓"
                "**The contrast worth remembering.** $x^{2} + 16$ is prime over the reals, but "
                "$x^{3} + 64$ is not. An odd power lets the sign work out; an even one does not.",
                [
                    "Eq(8*2**3 - 27, 37)",
                    "Eq((2*2 - 3)*(4*2**2 + 6*2 + 9), 37)",
                    "Eq(1**3 + 64, 65)",
                    "Eq((1 + 4)*(1**2 - 4*1 + 16), 65)",
                    "Eq(36 - 4*4*9, -108)",
                    "Eq(16 - 4*1*16, -48)",
                    "Eq(2**3, 8)",
                    "Eq(4**3, 64)",
                ],
            ),
            problem(
                "im3-u1-l4-we2",
                "Factor $x^{4} - 13x^{2} + 36$ completely, and find all its zeros.",
                "**Spot the quadratic in disguise.** Only even powers of $x$ appear, so "
                "substitute $u = x^{2}$:"
                "$$u^{2} - 13u + 36.$$"
                "**Factor the substituted trinomial.** Two numbers with product $36$ and sum $-13$: both negative, "
                "and $-4$ with $-9$ works:"
                "$$(u - 4)(u - 9).$$"
                "**Substitute back.**"
                "$$(x^{2} - 4)(x^{2} - 9).$$"
                "**Keep going — both are differences of squares.**"
                "$$(x - 2)(x + 2)(x - 3)(x + 3).$$"
                "**Read the zeros.** $x = \\pm 2$ and $x = \\pm 3$ — four distinct real zeros in "
                "a quartic, which is the maximum ✓"
                "**Verify one.** $3^{4} - 13(9) + 36 = 81 - 117 + 36 = 0$ ✓ And "
                "$(-2)^{4} - 13(4) + 36 = 16 - 52 + 36 = 0$ ✓"
                "**Check the constant term.** The product of the negated zeros is "
                "$(2)(-2)(3)(-3) = 36$ ✓ matching the polynomial's constant."
                "**Why stopping one step early would be wrong.** 'Completely' means "
                "no factor can be broken down further, and both of those can. Re-examining every "
                "factor is the habit that catches it.",
                [
                    "Eq(3**4 - 13*3**2 + 36, 0)",
                    "Eq((-2)**4 - 13*(-2)**2 + 36, 0)",
                    "Eq((-4)*(-9), 36)",
                    "Eq(-4 + (-9), -13)",
                    "Eq((0 - 2)*(0 + 2)*(0 - 3)*(0 + 3), 36)",
                    "Eq(1**4 - 13*1**2 + 36, (1 - 2)*(1 + 2)*(1 - 3)*(1 + 3))",
                ],
            ),
            problem(
                "im3-u1-l4-we3",
                "An open box is made from a $20$ cm by $16$ cm sheet by cutting a square of side "
                "$x$ from each corner and folding up the sides. Write the volume as a polynomial, "
                "state its physical domain, and find the cut size that maximises the volume to "
                "the nearest tenth.",
                "**Write the dimensions after folding.** The height is $x$; the base loses $x$ "
                "from each end of both dimensions:"
                "$$\\text{length } 20 - 2x, \\qquad \\text{width } 16 - 2x.$$"
                "**Write the volume.**"
                "$$V(x) = x(20 - 2x)(16 - 2x) = 4x^{3} - 72x^{2} + 320x.$$"
                "**State the physical domain.** All three dimensions must be positive: $x > 0$, "
                "$20 - 2x > 0$ and $16 - 2x > 0$. The binding constraint is the smaller one, so"
                "$$0 < x < 8.$$"
                "Outside that range the cubic still returns values, but they describe no box — "
                "at $x = 9$ it gives $4(729) - 72(81) + 320(9) = -36$, a negative volume."
                "**Search for the maximum.** Testing across the domain:"
                "$$V(2) = 2(16)(12) = 384, \\quad V(3) = 3(14)(10) = 420, \\quad "
                "V(4) = 4(12)(8) = 384.$$"
                "The peak is near $3$."
                "**Narrow it.** $V(2.9) = 2.9(14.2)(10.2) = 420.0$ and "
                "$V(3.1) = 3.1(13.8)(9.8) = 419.2$, and $V(2.94) \\approx 420.1$. So the maximum "
                "is about $420.1$ cm³ at $x \\approx 2.9$ cm."
                "**Sanity-check the shape.** The volume is zero at $x = 0$ (no height) and at "
                "$x = 8$ (no width), rising to a single peak between — exactly what a physical "
                "box should do ✓"
                "**A note on precision.** The function is very flat near its peak: $V(2.9)$ and "
                "$V(3.0)$ differ by less than one part in a thousand. So a cut anywhere between "
                "$2.8$ and $3.1$ cm is effectively optimal, which is worth saying rather than "
                "quoting a spurious number of decimals.",
                [
                    "Eq(2*(20 - 2*2)*(16 - 2*2), 384)",
                    "Eq(3*(20 - 2*3)*(16 - 2*3), 420)",
                    "Eq(4*(20 - 2*4)*(16 - 2*4), 384)",
                    "Eq(4*9**3 - 72*9**2 + 320*9, -36)",
                    "Eq(8*(20 - 2*8)*(16 - 2*8), 0)",
                    "Eq(0*(20 - 0)*(16 - 0), 0)",
                    "Abs(Rational(29,10)*(20 - 2*Rational(29,10))*(16 - 2*Rational(29,10)) - 420) < 1",
                    "Rational(29,10)*(20 - 2*Rational(29,10))*(16 - 2*Rational(29,10)) > Rational(31,10)*(20 - 2*Rational(31,10))*(16 - 2*Rational(31,10))",
                ],
            ),
            problem(
                "im3-u1-l4-we4",
                "Factor $x^{3} - 2x^{2} - 9x + 18$ by grouping, and confirm the zeros against the "
                "Factor Theorem.",
                "**Split into two pairs.**"
                "$$(x^{3} - 2x^{2}) + (-9x + 18).$$"
                "**Factor each pair.** The first shares $x^{2}$; the second shares $-9$ — and "
                "pulling out the NEGATIVE is what makes the brackets match:"
                "$$x^{2}(x - 2) - 9(x - 2).$$"
                "**Extract the common bracket.**"
                "$$(x - 2)(x^{2} - 9).$$"
                "**Finish with the difference of squares.**"
                "$$(x - 2)(x - 3)(x + 3).$$"
                "**Read the zeros.** $x = 2$, $x = 3$, $x = -3$."
                "**Confirm with the Factor Theorem.** "
                "$f(2) = 8 - 8 - 18 + 18 = 0$ ✓ "
                "$f(3) = 27 - 18 - 27 + 18 = 0$ ✓ "
                "$f(-3) = -27 - 18 + 27 + 18 = 0$ ✓ All three substitutions vanish, which "
                "independently verifies the grouping."
                "**Check the constant.** The product of the negated zeros: "
                "$(-2)(-3)(3) = 18$ ✓ matching the polynomial's constant term."
                "**Describe the graph, since the work is done.** Degree $3$ with a positive lead, "
                "so it falls left and rises right, crossing at $-3$, $2$ and $3$ — three simple "
                "zeros, the maximum for a cubic.",
                [
                    "Eq(2**3 - 2*2**2 - 9*2 + 18, 0)",
                    "Eq(3**3 - 2*3**2 - 9*3 + 18, 0)",
                    "Eq((-3)**3 - 2*(-3)**2 - 9*(-3) + 18, 0)",
                    "Eq((0 - 2)*(0 - 3)*(0 + 3), 18)",
                    "Eq(1**3 - 2*1**2 - 9*1 + 18, (1 - 2)*(1 - 3)*(1 + 3))",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Writing $a^3 - b^3 = (a - b)(a^2 - ab + b^2)$.",
                "The middle sign is the OPPOSITE of the linear factor's. Difference of cubes "
                "takes $+ab$; sum of cubes takes $-ab$. Check by expanding at $a = 2$, $b = 1$.",
            ),
            mistake(
                "Trying to factor the quadratic from a cube identity further.",
                "$a^2 + ab + b^2$ is irreducible over the reals — its discriminant is $-3b^2$. "
                "Confirm and move on rather than searching.",
            ),
            mistake(
                "Stopping a quartic factorisation at $(x^2 - 4)(x^2 - 9)$.",
                "Both factors are differences of squares. 'Completely' means re-examining every "
                "factor you write until none can be broken down.",
            ),
            mistake(
                "Reporting a model's optimum outside its physical domain.",
                "A box volume is meaningless for $x > 8$. State the domain from the physical "
                "constraints and search only inside it.",
            ),
        ],
        try_it=[
            problem(
                "im3-u1-l4-t1",
                "Factor $27x^{3} + 8$ completely.",
                "A sum of cubes with $a = 3x$ and $b = 2$: "
                "$27x^{3} + 8 = (3x + 2)(9x^{2} - 6x + 4)$. The quadratic has discriminant "
                "$36 - 144 = -108 < 0$, so it is irreducible. Check at $x = 1$: "
                "$27 + 8 = 35$, and $(5)(9 - 6 + 4) = 5 \\times 7 = 35$ ✓",
                [
                    "Eq(27*1**3 + 8, 35)",
                    "Eq((3*1 + 2)*(9*1**2 - 6*1 + 4), 35)",
                    "Eq(36 - 4*9*4, -108)",
                    "Eq(27*2**3 + 8, (3*2 + 2)*(9*2**2 - 6*2 + 4))",
                ],
            ),
            problem(
                "im3-u1-l4-t2",
                "Factor $x^{4} - 5x^{2} + 4$ completely and give its zeros.",
                "Substituting $u = x^{2}$ gives $u^{2} - 5u + 4 = (u - 1)(u - 4)$, so "
                "$(x^{2} - 1)(x^{2} - 4) = (x - 1)(x + 1)(x - 2)(x + 2)$. Zeros: "
                "$\\pm 1$ and $\\pm 2$. Check at $x = 2$: $16 - 20 + 4 = 0$ ✓ and the constant "
                "$(-1)(1)(-2)(2) = 4$ ✓",
                [
                    "Eq(2**4 - 5*2**2 + 4, 0)",
                    "Eq((-1)**4 - 5*(-1)**2 + 4, 0)",
                    "Eq((0 - 1)*(0 + 1)*(0 - 2)*(0 + 2), 4)",
                    "Eq((-1)*(-4), 4)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-SSE.2",
                "title": "Two more identities, and one habit",
                "body": (
                    "The sum and difference of cubes extend the pattern library past degree two. "
                    "The habit is structural substitution: if an expression is a quadratic in "
                    "disguise, undisguise it."
                ),
                "beats": [
                    "$a^{3} - b^{3} = (a-b)(a^{2}+ab+b^{2})$",
                    "$a^{3} + b^{3} = (a+b)(a^{2}-ab+b^{2})$",
                    "A sum of CUBES does factor",
                    "$u = x^{2}$ undisguises a quartic",
                ],
            },
            {
                "kind": "worked",
                "title": "Both cube identities",
                "problemId": "im3-u1-l4-we1",
            },
            tap(
                "Which sign in the middle?",
                "What is the correct factorisation of $x^{3} - 8$?",
                [
                    "$(x - 2)(x^{2} - 2x + 4)$",
                    "$(x - 2)(x^{2} + 2x + 4)$",
                    "$(x + 2)(x^{2} - 2x + 4)$",
                    "$(x - 2)^{3}$",
                ],
                1,
                "Difference of cubes: the linear factor takes the same sign, the middle term the "
                "opposite. Check at $x = 3$: $27 - 8 = 19$, and $(1)(9 + 6 + 4) = 19$ ✓",
                [
                    "Eq(3**3 - 8, 19)",
                    "Eq((3 - 2)*(3**2 + 2*3 + 4), 19)",
                    "Ne((3 - 2)*(3**2 - 2*3 + 4), 19)",
                ],
            ),
            {
                "kind": "tip",
                "eyebrow": "Look for the disguise",
                "title": "Only even powers? Substitute",
                "body": (
                    "$x^{4} + bx^{2} + c$ is a quadratic wearing a costume. Set $u = x^{2}$, "
                    "factor the trinomial you already know how to factor, then substitute back "
                    "and keep going — the results are usually differences of squares."
                ),
            },
            {
                "kind": "worked",
                "title": "A quartic through substitution",
                "problemId": "im3-u1-l4-we2",
            },
            {
                "kind": "worked",
                "title": "Grouping, at degree three",
                "problemId": "im3-u1-l4-we4",
            },
            {
                "kind": "teach",
                "eyebrow": "Modelling",
                "title": "The formula outlives the situation",
                "body": (
                    "A cubic volume function returns a value for every real input, including "
                    "negative volumes for impossible boxes. Stating the physical domain is part "
                    "of the model, not a footnote to it."
                ),
            },
            {
                "kind": "polyGraph",
                "eyebrow": "The box volume",
                "title": "A cubic with a real optimum inside it",
                "teach": (
                    "The volume is zero at both ends of the physical domain — no height at one "
                    "end, no width at the other — and peaks between. That single interior maximum "
                    "is the whole point of the model."
                ),
                "config": {"mode": "zeros", "n": 3, "negative": False},
            },
            {
                "kind": "worked",
                "title": "A box, its domain and its optimum",
                "problemId": "im3-u1-l4-we3",
            },
            tap(
                "What is the domain?",
                "A box is folded from a $12$ cm by $10$ cm sheet by cutting squares of side $x$. "
                "For what $x$ does a real box exist?",
                ["$0 < x < 12$", "$0 < x < 5$", "$0 < x < 10$", "any $x > 0$"],
                1,
                "Both base dimensions must stay positive: $12 - 2x > 0$ gives $x < 6$ and "
                "$10 - 2x > 0$ gives $x < 5$. The SMALLER bound binds, so $0 < x < 5$.",
                [
                    "Eq(10 - 2*5, 0)",
                    "Eq(12 - 2*6, 0)",
                    "5 < 6",
                    "Eq(4*(12 - 2*4)*(10 - 2*4), 32)",
                ],
            ),
            {"kind": "tryIt", "title": "A sum of cubes", "problemId": "im3-u1-l4-t1"},
            {"kind": "tryIt", "title": "Another disguised quadratic", "problemId": "im3-u1-l4-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "$a^{3} \\mp b^{3}$ both factor — the middle sign is opposite the linear one",
                    "The quadratic factor from a cube identity is irreducible over the reals",
                    "Even powers only? Substitute $u = x^{2}$ and factor the trinomial",
                    "Grouping works at any degree, not just two",
                    "Every model has a physical domain narrower than its formula's",
                ],
            },
        ],
    )


# ===========================================================================
# Practice and test banks
# ===========================================================================
def practice_bank():
    return [
        problem(
            "im3-u1-p1",
            "Describe the end behaviour of $f(x) = -x^{5} + 4x^{2} - 3$ and bound its zeros and "
            "turning points.",
            "Leading term $-x^{5}$: odd degree, negative coefficient, so the graph rises on the "
            "left and falls on the right. At most $5$ real zeros and at most $4$ turning points; "
            "odd degree guarantees at least one real zero. Check: $f(10) = -100000 + 400 - 3$, "
            "strongly negative; $f(-10) = 100000 + 400 - 3$, strongly positive ✓",
            [
                "Eq(-(10**5) + 4*10**2 - 3, -99603)",
                "Eq(-((-10)**5) + 4*(-10)**2 - 3, 100397)",
                "Eq(5 - 1, 4)",
            ],
        ),
        problem(
            "im3-u1-p2",
            "For $f(x) = (x + 1)^{2}(x - 3)^{3}$, give the zeros with multiplicities, the degree, "
            "the end behaviour, and the behaviour at each zero.",
            "Zeros: $x = -1$ (multiplicity $2$) and $x = 3$ (multiplicity $3$). Degree "
            "$2 + 3 = 5$, leading coefficient $+1$, so it falls left and rises right. At $-1$ the "
            "multiplicity is even, so the curve touches and turns; at $3$ it is odd, so it "
            "crosses — flattening as it does. Intercept: $(1)^{2}(-3)^{3} = -27$.",
            [
                "Eq((0 + 1)**2*(0 - 3)**3, -27)",
                "Eq(2 + 3, 5)",
                "Eq((-1 + 1)**2*(-1 - 3)**3, 0)",
                "(Rational(-11,10) + 1)**2*(Rational(-11,10) - 3)**3 < 0",
                "(Rational(-9,10) + 1)**2*(Rational(-9,10) - 3)**3 < 0",
            ],
        ),
        problem(
            "im3-u1-p3",
            "Find the remainder when $p(x) = 2x^{4} - x^{3} + 5x - 1$ is divided by $x - 2$.",
            "By the Remainder Theorem the remainder is $p(2) = 32 - 8 + 10 - 1 = 33$. Since it is "
            "not zero, $x - 2$ is not a factor. One substitution replaced the whole division.",
            [
                "Eq(2*2**4 - 2**3 + 5*2 - 1, 33)",
                "Ne(33, 0)",
            ],
        ),
        problem(
            "im3-u1-p4",
            "Factor $p(x) = x^{3} - 4x^{2} + x + 6$ completely.",
            "Rational candidates divide $6$. Testing $x = -1$: $-1 - 4 - 1 + 6 = 0$ ✓ so $x + 1$ "
            "is a factor. Dividing gives $x^{2} - 5x + 6 = (x - 2)(x - 3)$. So "
            "$p(x) = (x + 1)(x - 2)(x - 3)$, with zeros $-1$, $2$, $3$. Check the constant: "
            "$(1)(-2)(-3) = 6$ ✓",
            [
                "Eq((-1)**3 - 4*(-1)**2 + (-1) + 6, 0)",
                "Eq(2**3 - 4*2**2 + 2 + 6, 0)",
                "Eq(3**3 - 4*3**2 + 3 + 6, 0)",
                "Eq((0 + 1)*(0 - 2)*(0 - 3), 6)",
            ],
        ),
        problem(
            "im3-u1-p5",
            "Write a degree-$3$ polynomial with zeros $-2$, $0$ and $5$ passing through "
            "$(1, -12)$.",
            "Factors from the zeros: $f(x) = ax(x + 2)(x - 5)$. Substituting $(1, -12)$: "
            "$a(1)(3)(-4) = -12a = -12$, so $a = 1$. The answer is $f(x) = x(x + 2)(x - 5)$. "
            "Check: $f(1) = (1)(3)(-4) = -12$ ✓ and all three zeros vanish ✓",
            [
                "Eq(1*(1 + 2)*(1 - 5), -12)",
                "Eq(0*(0 + 2)*(0 - 5), 0)",
                "Eq((-2)*(-2 + 2)*(-2 - 5), 0)",
                "Eq(5*(5 + 2)*(5 - 5), 0)",
            ],
        ),
        problem(
            "im3-u1-p6",
            "Factor $125x^{3} - 1$ completely.",
            "A difference of cubes with $a = 5x$ and $b = 1$: "
            "$(5x - 1)(25x^{2} + 5x + 1)$. The quadratic's discriminant is $25 - 100 = -75 < 0$, "
            "so it is irreducible. Check at $x = 1$: $125 - 1 = 124$, and "
            "$(4)(25 + 5 + 1) = 4 \\times 31 = 124$ ✓",
            [
                "Eq(125*1**3 - 1, 124)",
                "Eq((5*1 - 1)*(25*1**2 + 5*1 + 1), 124)",
                "Eq(25 - 4*25*1, -75)",
            ],
        ),
        problem(
            "im3-u1-p7",
            "Factor $x^{4} - 10x^{2} + 9$ completely and list its zeros.",
            "Substituting $u = x^{2}$: $u^{2} - 10u + 9 = (u - 1)(u - 9)$, so "
            "$(x^{2} - 1)(x^{2} - 9) = (x - 1)(x + 1)(x - 3)(x + 3)$. Zeros: $\\pm 1$, $\\pm 3$ — "
            "four in a quartic, the maximum. Check at $x = 3$: $81 - 90 + 9 = 0$ ✓",
            [
                "Eq(3**4 - 10*3**2 + 9, 0)",
                "Eq(1**4 - 10*1**2 + 9, 0)",
                "Eq((0 - 1)*(0 + 1)*(0 - 3)*(0 + 3), 9)",
                "Eq((-1)*(-9), 9)",
            ],
        ),
        problem(
            "im3-u1-p8",
            "Show that $p(x) = x^{3} + x - 3$ has a zero between $1$ and $2$, and narrow it to "
            "one decimal place.",
            "$p(1) = 1 + 1 - 3 = -1$ and $p(2) = 8 + 2 - 3 = 7$. The sign changes and the "
            "function is continuous, so a zero lies between. Narrowing: $p(1.2) = 1.728 + 1.2 - "
            "3 = -0.072 < 0$ and $p(1.3) = 2.197 + 1.3 - 3 = 0.497 > 0$, so the zero is between "
            "$1.2$ and $1.3$.",
            [
                "Eq(1**3 + 1 - 3, -1)",
                "Eq(2**3 + 2 - 3, 7)",
                "Rational(12,10)**3 + Rational(12,10) - 3 < 0",
                "Rational(13,10)**3 + Rational(13,10) - 3 > 0",
            ],
        ),
        problem(
            "im3-u1-p9",
            "Find $k$ so that $x + 3$ is a factor of $f(x) = x^{3} + kx^{2} - 2x + 3$.",
            "By the Factor Theorem, $f(-3) = 0$: $-27 + 9k + 6 + 3 = 9k - 18 = 0$, so $k = 2$. "
            "Check: $f(x) = x^{3} + 2x^{2} - 2x + 3$ gives $f(-3) = -27 + 18 + 6 + 3 = 0$ ✓",
            [
                "Eq(9*2 - 18, 0)",
                "Eq((-3)**3 + 2*(-3)**2 - 2*(-3) + 3, 0)",
            ],
        ),
        problem(
            "im3-u1-p10",
            "Factor $2x^{3} + x^{2} - 8x - 4$ by grouping.",
            "Pair them: $(2x^{3} + x^{2}) + (-8x - 4) = x^{2}(2x + 1) - 4(2x + 1) = "
            "(2x + 1)(x^{2} - 4) = (2x + 1)(x - 2)(x + 2)$. Zeros: $-\\frac{1}{2}$, $2$, $-2$. "
            "Check at $x = 2$: $16 + 4 - 16 - 4 = 0$ ✓",
            [
                "Eq(2*2**3 + 2**2 - 8*2 - 4, 0)",
                "Eq(2*(-2)**3 + (-2)**2 - 8*(-2) - 4, 0)",
                "Eq(2*Rational(-1,2)**3 + Rational(-1,2)**2 - 8*Rational(-1,2) - 4, 0)",
                "Eq((0*2 + 1)*(0 - 2)*(0 + 2), -4)",
            ],
        ),
        problem(
            "im3-u1-p11",
            "A polynomial graph rises from the bottom left, turns twice, and rises to the top "
            "right, crossing the axis three times. What is the smallest possible degree and the "
            "sign of the leading coefficient?",
            "The ends disagree (up on the right, up from below on the left means it came from "
            "$-\\infty$), so the degree is ODD, and rising on the right means a POSITIVE leading "
            "coefficient. Two turns needs degree at least $3$; three crossings needs at least "
            "$3$. The smallest odd degree meeting both is $3$ — a standard cubic with three real "
            "zeros.",
            [
                "Eq(2 + 1, 3)",
                "Eq((0 - 1)*(0 - 2)*(0 - 3), -6)",
                "Eq(1*(1 - 2)*(1 - 3), 2)",
            ],
        ),
        problem(
            "im3-u1-p12",
            "An open box is folded from a $30$ cm square sheet by cutting squares of side $x$ "
            "from the corners. Write the volume, state the domain, and compare $V(4)$ with "
            "$V(5)$ and $V(6)$.",
            "$V(x) = x(30 - 2x)^{2}$, valid for $0 < x < 15$. Then $V(4) = 4(22)^{2} = 1936$, "
            "$V(5) = 5(20)^{2} = 2000$, and $V(6) = 6(18)^{2} = 1944$. The peak is near $x = 5$, "
            "and the volume falls away on both sides ✓ At $x = 15$ the volume is zero — the base "
            "has vanished.",
            [
                "Eq(4*(30 - 2*4)**2, 1936)",
                "Eq(5*(30 - 2*5)**2, 2000)",
                "Eq(6*(30 - 2*6)**2, 1944)",
                "Eq(15*(30 - 2*15)**2, 0)",
                "2000 > 1936",
                "2000 > 1944",
            ],
        ),
    ]


def test_bank():
    return [
        problem(
            "im3-u1-ty-1",
            "For $f(x) = -3x^{4} + 2x^{3} - x + 8$: state the degree, leading coefficient, end "
            "behaviour, the maximum number of real zeros and turning points, and the vertical "
            "intercept.",
            "**Degree and leading coefficient.** The highest power is $x^{4}$ with coefficient "
            "$-3$."
            "**End behaviour.** Degree $4$ is EVEN, so the ends agree; the coefficient is "
            "negative, so both fall:"
            "$$x \\to \\pm\\infty: f(x) \\to -\\infty.$$"
            "**Bounds.** At most $4$ real zeros; at most $3$ turning points. Even degree means "
            "there is no guarantee of any real zero."
            "**Vertical intercept.** $f(0) = 8$."
            "**Check the ends numerically.** $f(10) = -30000 + 2000 - 10 + 8 = -28002$ ✓ and "
            "$f(-10) = -30000 - 2000 + 10 + 8 = -31982$ ✓ Both large and negative."
            "**A conclusion the signs supply.** $f(0) = 8 > 0$ while both ends are negative, so "
            "the graph must cross the axis at least twice — once on each side of the origin. The "
            "end behaviour and one point together prove the existence of zeros without solving "
            "anything.",
            [
                "Eq(-3*10**4 + 2*10**3 - 10 + 8, -28002)",
                "Eq(-3*(-10)**4 + 2*(-10)**3 - (-10) + 8, -31982)",
                "Eq(-3*0**4 + 2*0**3 - 0 + 8, 8)",
                "Eq(4 - 1, 3)",
                "-3*10**4 + 2*10**3 - 10 + 8 < 0",
                "-3*0**4 + 2*0**3 - 0 + 8 > 0",
            ],
        ),
        problem(
            "im3-u1-ty-2",
            "Sketch $f(x) = (x + 2)(x - 1)^{2}(x - 3)$: give the zeros and multiplicities, "
            "degree, end behaviour, vertical intercept, and the sign of $f$ on each interval.",
            "**Zeros and multiplicities.** $x = -2$ (mult. $1$), $x = 1$ (mult. $2$), $x = 3$ "
            "(mult. $1$)."
            "**Degree and lead.** $1 + 2 + 1 = 4$, leading coefficient $+1$ — even degree, "
            "positive lead, so BOTH ends rise."
            "**Vertical intercept.** $f(0) = (2)(1)(-3) = -6$."
            "**Sign on each interval.** The zeros split the line into four pieces:"
            "$$f(-3) = (-1)(16)(-6) = 96 \\ (+)$$"
            "$$f(0) = -6 \\ (-)$$"
            "$$f(2) = (4)(1)(-1) = -4 \\ (-)$$"
            "$$f(4) = (6)(9)(1) = 54 \\ (+)$$"
            "**Check the signs against the multiplicities.** Crossing at $-2$: positive to "
            "negative ✓ Bouncing at $1$: negative to negative ✓ Crossing at $3$: negative to "
            "positive ✓ Every transition matches its multiplicity's parity."
            "**Describe the sketch.** Down from the top left, crossing at $-2$; a dip through "
            "$(0, -6)$; a touch on the axis at $1$ without crossing; back down; then crossing at "
            "$3$ and rising to the top right."
            "**Consistency with the ends.** Positive beyond both outermost zeros ✓ which is "
            "exactly what an even degree with a positive lead requires.",
            [
                "Eq((-3 + 2)*(-3 - 1)**2*(-3 - 3), 96)",
                "Eq((0 + 2)*(0 - 1)**2*(0 - 3), -6)",
                "Eq((2 + 2)*(2 - 1)**2*(2 - 3), -4)",
                "Eq((4 + 2)*(4 - 1)**2*(4 - 3), 54)",
                "Eq(1 + 2 + 1, 4)",
                "Eq((1 + 2)*(1 - 1)**2*(1 - 3), 0)",
            ],
        ),
        problem(
            "im3-u1-ty-3",
            "Factor $p(x) = 2x^{3} - 3x^{2} - 11x + 6$ completely, using the Rational Root "
            "Theorem and synthetic division.",
            "**List the candidates.** The constant is $6$ (divisors $1, 2, 3, 6$) and the leading "
            "coefficient is $2$ (divisors $1, 2$). So the possible rational zeros are"
            "$$\\pm 1, \\ \\pm 2, \\ \\pm 3, \\ \\pm 6, \\ \\pm \\tfrac{1}{2}, \\ "
            "\\pm \\tfrac{3}{2}.$$"
            "**Test them.** $p(1) = 2 - 3 - 11 + 6 = -6$, no. $p(-1) = -2 - 3 + 11 + 6 = 12$, "
            "no. $p(3) = 54 - 27 - 33 + 6 = 0$ ✓"
            "**Divide out the factor.** Synthetic division with $a = 3$ on $2, -3, -11, 6$:"
            "$$2, \\quad -3 + 6 = 3, \\quad -11 + 9 = -2, \\quad 6 - 6 = 0.$$"
            "Remainder $0$ ✓ quotient $2x^{2} + 3x - 2$."
            "**Factor the quadratic.** $ac = -4$, sum $3$: the pair is $4$ and $-1$, giving"
            "$$2x^{2} + 4x - x - 2 = 2x(x + 2) - (x + 2) = (x + 2)(2x - 1).$$"
            "**Complete factorisation.**"
            "$$p(x) = (x - 3)(x + 2)(2x - 1),$$"
            "with zeros $3$, $-2$ and $\\frac{1}{2}$."
            "**Verify all three.** $p(-2) = -16 - 12 + 22 + 6 = 0$ ✓ and "
            "$p\\!\\left(\\frac{1}{2}\\right) = \\frac{1}{4} - \\frac{3}{4} - \\frac{11}{2} + 6 "
            "= 0$ ✓"
            "**Note where the fractional zero came from.** The leading coefficient $2$ is what "
            "permits a denominator of $2$ — with a leading coefficient of $1$ every rational zero "
            "would have to be a whole number.",
            [
                "Eq(2*3**3 - 3*3**2 - 11*3 + 6, 0)",
                "Eq(2*(-2)**3 - 3*(-2)**2 - 11*(-2) + 6, 0)",
                "Eq(2*Rational(1,2)**3 - 3*Rational(1,2)**2 - 11*Rational(1,2) + 6, 0)",
                "Eq(2*1**3 - 3*1**2 - 11*1 + 6, -6)",
                "Eq(-3 + 6, 3)",
                "Eq(-11 + 9, -2)",
                "Eq((0 - 3)*(0 + 2)*(2*0 - 1), 6)",
            ],
        ),
        problem(
            "im3-u1-ty-4",
            "Factor $x^{6} - 64$ completely over the reals, and say how many real zeros it has.",
            "**Two readings are available.** $x^{6} = (x^{3})^{2} = (x^{2})^{3}$, so this is both "
            "a difference of squares and a difference of cubes. Take the SQUARES route first — "
            "it factors further."
            "**As a difference of squares.**"
            "$$x^{6} - 64 = (x^{3} - 8)(x^{3} + 8).$$"
            "**Now each is a difference or sum of cubes.**"
            "$$x^{3} - 8 = (x - 2)(x^{2} + 2x + 4), \\qquad "
            "x^{3} + 8 = (x + 2)(x^{2} - 2x + 4).$$"
            "**Complete factorisation over the reals.**"
            "$$x^{6} - 64 = (x - 2)(x + 2)(x^{2} + 2x + 4)(x^{2} - 2x + 4).$$"
            "**Check the two quadratics are irreducible.** Both have discriminant "
            "$4 - 16 = -12 < 0$ ✓ so neither factors further over the reals."
            "**Count the real zeros.** Only $x = 2$ and $x = -2$ — TWO real zeros in a degree-6 "
            "polynomial. The other four zeros are complex."
            "**Verify.** $2^{6} - 64 = 0$ ✓ and $(-2)^{6} - 64 = 64 - 64 = 0$ ✓"
            "**Check the constant.** At $x = 0$ the factored form gives "
            "$(-2)(2)(4)(4) = -64$ ✓ matching the original."
            "**Why the squares route first.** Taking cubes first gives "
            "$(x^{2} - 4)(x^{4} + 4x^{2} + 16)$ — correct, but the quartic then needs more work "
            "to break apart. Choosing the split that leaves the simplest pieces saves effort.",
            [
                "Eq(2**6 - 64, 0)",
                "Eq((-2)**6 - 64, 0)",
                "Eq((0 - 2)*(0 + 2)*(0**2 + 2*0 + 4)*(0**2 - 2*0 + 4), -64)",
                "Eq(4 - 4*1*4, -12)",
                "Eq(1**6 - 64, (1 - 2)*(1 + 2)*(1**2 + 2*1 + 4)*(1**2 - 2*1 + 4))",
                "Eq(2**3, 8)",
            ],
        ),
        problem(
            "im3-u1-ty-5",
            "Find the value of $k$ for which $x - 1$ is a factor of "
            "$f(x) = 2x^{3} + kx^{2} - 5x + 1$. Then factor $f$ completely and find all real "
            "zeros.",
            "**Apply the Factor Theorem.**"
            "$$f(1) = 2 + k - 5 + 1 = k - 2.$$"
            "**Set it to zero.** $k = 2$, so $f(x) = 2x^{3} + 2x^{2} - 5x + 1$."
            "**Confirm.** $f(1) = 2 + 2 - 5 + 1 = 0$ ✓"
            "**Divide out the factor.** Synthetic division with $a = 1$ on $2, 2, -5, 1$:"
            "$$2, \\quad 2 + 2 = 4, \\quad -5 + 4 = -1, \\quad 1 - 1 = 0.$$"
            "Quotient: $2x^{2} + 4x - 1$."
            "**Solve the quadratic.** Its discriminant is $16 + 8 = 24 > 0$, so there are two "
            "real roots:"
            "$$x = \\frac{-4 \\pm \\sqrt{24}}{4} = \\frac{-4 \\pm 2\\sqrt{6}}{4} = "
            "\\frac{-2 \\pm \\sqrt{6}}{2}.$$"
            "**List all three real zeros.** $x = 1$, and "
            "$x = \\frac{-2 + \\sqrt{6}}{2} \\approx 0.225$, and "
            "$x = \\frac{-2 - \\sqrt{6}}{2} \\approx -2.225$."
            "**Check the irrational pair by sum and product.** They sum to $-2 = -\\frac{4}{2}$ ✓ "
            "and multiply to $\\frac{4 - 6}{4} = -\\frac{1}{2} = \\frac{-1}{2}$ ✓ — both match "
            "the quadratic's coefficients."
            "**Note what the Rational Root Theorem could and could not do.** It found the zero at "
            "$1$; the other two are irrational, so no amount of candidate-testing would have "
            "reached them. Dividing down to a quadratic is what makes them accessible.",
            [
                "Eq(2*1**3 + 2*1**2 - 5*1 + 1, 0)",
                "Eq(2 + 2, 4)",
                "Eq(-5 + 4, -1)",
                "Eq(16 + 8, 24)",
                "Eq(simplify(sqrt(24)), 2*sqrt(6))",
                "Eq((-2 + sqrt(6))/2 + (-2 - sqrt(6))/2, -2)",
                "Eq(simplify(((-2 + sqrt(6))/2)*((-2 - sqrt(6))/2)), Rational(-1,2))",
                "Eq(simplify(2*((-2 + sqrt(6))/2)**2 + 4*((-2 + sqrt(6))/2) - 1), 0)",
            ],
        ),
        problem(
            "im3-u1-ty-6",
            "A rectangular box has a square base of side $x$ and a height of $12 - x$. Write its "
            "volume as a polynomial, state the physical domain, and find the base size that "
            "maximises the volume among whole-centimetre values.",
            "**Write the volume.** Square base times height:"
            "$$V(x) = x^{2}(12 - x) = 12x^{2} - x^{3}.$$"
            "**State the domain.** Both the base and the height must be positive: $x > 0$ and "
            "$12 - x > 0$, so"
            "$$0 < x < 12.$$"
            "**Evaluate at whole centimetres near the middle.**"
            "$$V(6) = 36(6) = 216, \\quad V(7) = 49(5) = 245, \\quad V(8) = 64(4) = 256,$$"
            "$$V(9) = 81(3) = 243, \\quad V(10) = 100(2) = 200.$$"
            "**Identify the maximum.** Among whole values the largest is $V(8) = 256$ cm³, with a "
            "base of $8$ cm and a height of $4$ cm."
            "**Check the shape of the function.** It is zero at both ends of the domain — no base "
            "at $x = 0$, no height at $x = 12$ — and rises to a single interior peak ✓ exactly "
            "what a physical volume should do."
            "**Confirm the peak is genuinely near 8.** $V(7.9) = 62.41(4.1) \\approx 255.9$ and "
            "$V(8.1) = 65.61(3.9) \\approx 255.9$, both just under $256$ ✓ so $x = 8$ really is "
            "the top."
            "**A note on the whole-number restriction.** The question asked among whole "
            "centimetres, and here that happens to coincide with the true maximum. It need not "
            "in general — the restriction is part of the problem, not a simplification of it.",
            [
                "Eq(6**2*(12 - 6), 216)",
                "Eq(7**2*(12 - 7), 245)",
                "Eq(8**2*(12 - 8), 256)",
                "Eq(9**2*(12 - 9), 243)",
                "Eq(10**2*(12 - 10), 200)",
                "Eq(0**2*(12 - 0), 0)",
                "Eq(12**2*(12 - 12), 0)",
                "256 > 245",
                "Rational(79,10)**2*(12 - Rational(79,10)) < 256",
            ],
        ),
        problem(
            "im3-u1-ty-7",
            "Show that $p(x) = x^{4} - 4x^{3} + 6x^{2} - 4x + 1$ has a single zero of "
            "multiplicity $4$, find it, and describe the graph.",
            "**Look for a pattern in the coefficients.** $1, -4, 6, -4, 1$ are the entries of the "
            "fourth row of Pascal's triangle with alternating signs — the signature of a "
            "binomial expansion."
            "**Identify the binomial.**"
            "$$(x - 1)^{4} = x^{4} - 4x^{3} + 6x^{2} - 4x + 1.$$"
            "So $p(x) = (x - 1)^{4}$."
            "**Read the zero.** A single zero at $x = 1$, with multiplicity $4$."
            "**Confirm by substitution.** $p(1) = 1 - 4 + 6 - 4 + 1 = 0$ ✓"
            "**Confirm the multiplicity via the Factor Theorem, repeatedly.** Dividing "
            "$(x - 1)^{4}$ by $(x-1)$ leaves $(x-1)^{3}$, which still vanishes at $1$ — and so on "
            "three more times. The factor divides out four times over."
            "**Describe the graph.** Even multiplicity, so the curve TOUCHES the axis at $x = 1$ "
            "and turns back without crossing. Degree $4$ with a positive lead, so both ends rise. "
            "The whole graph therefore sits on or above the axis, touching it only at $x = 1$."
            "**Verify it never goes negative.** $(x - 1)^{4}$ is a fourth power, so it is "
            "non-negative for every real $x$ ✓ At $x = 0$ it is $1$; at $x = 2$ it is $1$; at "
            "$x = 3$ it is $16$ — all positive, symmetric about $x = 1$."
            "**Why the multiplicities-sum check matters here.** One distinct zero, but the "
            "multiplicities must total the degree $4$ — and they do, which is what confirms "
            "nothing has been missed.",
            [
                "Eq(1**4 - 4*1**3 + 6*1**2 - 4*1 + 1, 0)",
                "Eq(expand((x - 1)**4), x**4 - 4*x**3 + 6*x**2 - 4*x + 1)",
                "Eq(0**4 - 4*0**3 + 6*0**2 - 4*0 + 1, 1)",
                "Eq(2**4 - 4*2**3 + 6*2**2 - 4*2 + 1, 1)",
                "Eq(3**4 - 4*3**3 + 6*3**2 - 4*3 + 1, 16)",
                "(0 - 1)**4 >= 0",
                "Eq((3 - 1)**4, (-1 - 1)**4)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="polynomial-functions",
        title="Polynomial Functions",
        unit_number=1,
        blurb=(
            "End behaviour read off the leading term, zeros and the multiplicity that decides "
            "crossing from bouncing, polynomial division with the Remainder and Factor Theorems, "
            "and the cube identities and structural substitutions that extend factoring past "
            "degree two — plus what a polynomial model can and cannot be asked."
        ),
        builds_on=(
            "Factoring from IM2 Unit 2 and the parabola from IM2 Unit 3 — the same ideas, now "
            "with the degree allowed to rise."
        ),
        lessons=[
            lesson_end_behaviour(),
            lesson_zeros_and_multiplicity(),
            lesson_division_and_remainder(),
            lesson_operations_and_identities(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
