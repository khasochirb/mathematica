#!/usr/bin/env python3
"""Integrated Mathematics 2 — Unit 4: Solving Quadratic Equations.

CCSS Integrated Math II: A-REI.4a (complete the square to derive the quadratic
formula), A-REI.4b (solve by inspection, taking square roots, completing the
square, the quadratic formula and factoring; recognise when the roots are
complex), N-CN.1 (the number i and the form a + bi), N-CN.2 (arithmetic with
complex numbers), N-CN.7 (solve quadratic equations with complex solutions).

The unit's spine is that there are four methods and they are not equal: three
are shortcuts that work sometimes, one always works, and the one that always
works is DERIVED from completing the square rather than handed down. Complex
numbers arrive at the end because the discriminant forces them — not as a new
topic but as the answer to "what if it is negative?".

Run: python3 scripts/im/build_im2_unit4.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-2"


# ===========================================================================
# Lesson 1 — A-REI.4b: factoring and square roots
# ===========================================================================
def lesson_factoring_and_roots():
    return lesson(
        slug="solving-by-factoring-and-roots",
        title="Solving by Factoring and by Square Roots",
        concrete=(
            "If two numbers multiply to zero, at least one of them IS zero. That single sentence "
            "is the whole engine behind solving by factoring — and it is the reason the equation "
            "must be arranged with zero on one side before anything else happens. Multiply to "
            "twelve and you learn nothing; multiply to zero and you learn everything."
        ),
        objective=(
            "Solve a quadratic equation by factoring using the zero-product property, and solve "
            "equations of the form $a(x - h)^{2} = c$ by taking square roots."
        ),
        concept=[
            "**The zero-product property is the whole method.** If $AB = 0$ then $A = 0$ or "
            "$B = 0$. Nothing comparable is true for any other number: $AB = 6$ tells you nothing "
            "about $A$ and $B$ individually. Zero is special, and that specialness is what makes "
            "factoring a solving technique rather than just a rewriting technique.",
            "**Rearrange to zero first, always.** To solve $x^{2} + 5x = 24$, move everything to "
            "one side: $x^{2} + 5x - 24 = 0$, then factor. Factoring the left side while $24$ sits "
            "on the right achieves nothing at all, and this is the single most common wasted step "
            "in the topic.",
            "**Then factor and split.** $(x + 8)(x - 3) = 0$ becomes two tiny linear equations, "
            "$x + 8 = 0$ and $x - 3 = 0$, giving $x = -8$ and $x = 3$. A quadratic has been "
            "reduced to two problems you could solve years ago.",
            "**Square roots handle equations with no linear term.** For $(x - 3)^{2} = 16$ there "
            "is no need to expand: take the square root of both sides and remember BOTH signs, "
            "$x - 3 = \\pm 4$, giving $x = 7$ and $x = -1$. Missing the negative root is the "
            "characteristic error of this method.",
            "**Why the plus-or-minus is compulsory.** Both $4$ and $-4$ square to $16$, so both "
            "must be considered. The symbol $\\sqrt{16}$ means the positive root only, by "
            "convention — which is exactly why the $\\pm$ has to be written in by hand when you "
            "undo a square.",
            "**A double root is one solution, counted twice.** $x^{2} - 6x + 9 = 0$ factors as "
            "$(x - 3)^{2} = 0$, so $x = 3$ is the only solution. Graphically the parabola touches "
            "the horizontal axis without crossing it — the two roots have merged into one point "
            "of tangency.",
        ],
        key_idea=(
            "Get zero on one side, factor, then set each factor to zero — because a product is "
            "zero exactly when one of its factors is."
        ),
        facts=[
            fact(
                "Zero-product property",
                "AB = 0 \\iff A = 0 \\text{ or } B = 0",
                "True for zero and no other number. This is why the rearrangement comes first.",
            ),
            fact(
                "Square-root method",
                "(x - h)^{2} = c \\ \\Rightarrow\\ x = h \\pm \\sqrt{c}",
                "Both signs, every time — $\\sqrt{c}$ alone means the positive root only.",
            ),
            fact(
                "Double root",
                "(x - r)^{2} = 0 \\ \\Rightarrow\\ x = r \\text{ (twice)}",
                "The parabola touches the axis instead of crossing it.",
            ),
            fact(
                "Roots and factors",
                "x = r \\text{ is a root} \\iff (x - r) \\text{ is a factor}",
                "The link that makes factoring and solving the same activity.",
            ),
        ],
        worked=[
            problem(
                "im2-u4-l1-we1",
                "Solve $x^{2} + 5x = 24$.",
                "**Move everything to one side.** The zero-product property needs a zero, so "
                "subtract $24$:"
                "$$x^{2} + 5x - 24 = 0.$$"
                "**Factor.** Two numbers with product $-24$ and sum $5$: opposite signs, larger "
                "one positive, so $8$ and $-3$:"
                "$$(x + 8)(x - 3) = 0.$$"
                "**Split into two linear equations.**"
                "$$x + 8 = 0 \\quad\\text{or}\\quad x - 3 = 0,$$"
                "giving $x = -8$ or $x = 3$."
                "**Check both in the ORIGINAL equation.** At $x = -8$: $64 - 40 = 24$ ✓ At "
                "$x = 3$: $9 + 15 = 24$ ✓ Checking in the original, not the rearranged version, "
                "catches an arithmetic slip made during the rearrangement."
                "**Why factoring the un-rearranged form would fail.** $x(x + 5) = 24$ is true, but "
                "it does not tell you that $x = 24$ or $x + 5 = 24$ — those give $x = 24$ and "
                "$x = 19$, neither of which is a solution. Only zero has the splitting property.",
                [
                    "Eq((-8)**2 + 5*(-8), 24)",
                    "Eq(3**2 + 5*3, 24)",
                    "Eq(8*(-3), -24)",
                    "Eq(8 + (-3), 5)",
                    "Ne(24**2 + 5*24, 24)",
                ],
            ),
            problem(
                "im2-u4-l1-we2",
                "Solve $3x^{2} - 12x = 0$ and $2x^{2} = 50$.",
                "**The first has a common factor, and no constant term.** Do not divide by $x$ — "
                "that would silently discard the solution $x = 0$. Factor instead:"
                "$$3x(x - 4) = 0.$$"
                "**Split.** $3x = 0$ gives $x = 0$; $x - 4 = 0$ gives $x = 4$. Two solutions."
                "**The second has no linear term, so use square roots.** Isolate the square first:"
                "$$x^{2} = 25 \\quad\\Longrightarrow\\quad x = \\pm 5.$$"
                "**Both signs are genuine solutions.** $2(25) = 50$ ✓ and $2(-5)^{2} = 2(25) = "
                "50$ ✓ — squaring destroys the sign, so both survive."
                "**The trap in the first equation, spelled out.** Dividing $3x^{2} = 12x$ by $x$ "
                "gives $3x = 12$ and $x = 4$ only. The solution $x = 0$ has vanished, because "
                "dividing by $x$ assumes $x \\neq 0$ — an assumption nobody stated and nobody "
                "checked. Factor, never divide by a variable.",
                [
                    "Eq(3*0**2 - 12*0, 0)",
                    "Eq(3*4**2 - 12*4, 0)",
                    "Eq(2*5**2, 50)",
                    "Eq(2*(-5)**2, 50)",
                    "Eq(3*0*(0 - 4), 0)",
                ],
            ),
            problem(
                "im2-u4-l1-we3",
                "Solve $2(x - 3)^{2} - 32 = 0$.",
                "**Isolate the squared expression.** Add $32$, then divide by $2$:"
                "$$2(x - 3)^{2} = 32 \\quad\\Longrightarrow\\quad (x - 3)^{2} = 16.$$"
                "Note the division by $2$ comes AFTER the addition — you are undoing the "
                "operations in reverse order."
                "**Take square roots of both sides, with both signs.**"
                "$$x - 3 = \\pm 4.$$"
                "**Split into two cases.** $x - 3 = 4$ gives $x = 7$; $x - 3 = -4$ gives "
                "$x = -1$."
                "**Check both.** At $x = 7$: $2(16) - 32 = 0$ ✓ At $x = -1$: $2(16) - 32 = 0$ ✓ "
                "Both give the same squared value because $4$ and $-4$ are equally far from zero."
                "**Notice the symmetry.** The two roots, $7$ and $-1$, are each $4$ units from "
                "$x = 3$ — the vertex's $x$-coordinate, visible directly in the vertex form. "
                "Square-root solving and vertex form are the same structure viewed from two "
                "directions.",
                [
                    "Eq(2*(7 - 3)**2 - 32, 0)",
                    "Eq(2*(-1 - 3)**2 - 32, 0)",
                    "Eq((7 + (-1))/2, 3)",
                    "Eq(7 - 3, 4)",
                    "Eq(3 - (-1), 4)",
                ],
            ),
            problem(
                "im2-u4-l1-we4",
                "Solve $x^{2} - 10x + 25 = 0$ and $6x^{2} + x - 15 = 0$.",
                "**The first is a perfect square.** The ends are $x^{2}$ and $5^{2}$, and the "
                "middle is $2 \\times 5 = 10$ ✓ so"
                "$$(x - 5)^{2} = 0 \\quad\\Longrightarrow\\quad x = 5.$$"
                "This is a DOUBLE root: one solution, arising from two identical factors. The "
                "parabola touches the horizontal axis at $x = 5$ without crossing it."
                "**The second needs the ac-method.** $ac = 6 \\times (-15) = -90$, and the sum "
                "must be $1$. Opposite signs with the larger positive: $10$ and $-9$."
                "**Split the middle term and group.**"
                "$$6x^{2} + 10x - 9x - 15 = 2x(3x + 5) - 3(3x + 5) = (3x + 5)(2x - 3) = 0.$$"
                "**Split and solve.** $3x + 5 = 0$ gives $x = -\\frac{5}{3}$; $2x - 3 = 0$ gives "
                "$x = \\frac{3}{2}$."
                "**Check the fractional roots.** At $x = \\frac{3}{2}$: "
                "$6 \\cdot \\frac{9}{4} + \\frac{3}{2} - 15 = \\frac{27}{2} + \\frac{3}{2} - 15 = "
                "15 - 15 = 0$ ✓ Fractional roots are perfectly ordinary — they simply mean the "
                "parabola crosses between integers.",
                [
                    "Eq(5**2 - 10*5 + 25, 0)",
                    "Eq(10*(-9), -90)",
                    "Eq(10 + (-9), 1)",
                    "Eq(6*Rational(3,2)**2 + Rational(3,2) - 15, 0)",
                    "Eq(6*Rational(-5,3)**2 + Rational(-5,3) - 15, 0)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Factoring before moving everything to one side.",
                "$x(x + 5) = 24$ does not split. The zero-product property needs a ZERO. "
                "Rearrange to $x^2 + 5x - 24 = 0$ first, every time.",
            ),
            mistake(
                "Dividing both sides by $x$ to solve $3x^{2} = 12x$.",
                "That destroys the solution $x = 0$. Factor instead: $3x(x - 4) = 0$ keeps both "
                "roots. Never divide an equation by a variable.",
            ),
            mistake(
                "Writing only the positive root when taking a square root.",
                "$(x - 3)^2 = 16$ gives $x - 3 = \\pm 4$, so $x = 7$ AND $x = -1$. The $\\pm$ is "
                "not optional — $\\sqrt{16}$ by itself means only the positive root.",
            ),
            mistake(
                "Reporting a double root as two different solutions.",
                "$(x - 5)^2 = 0$ has the single solution $x = 5$. It is called a double root "
                "because the factor appears twice, not because there are two values.",
            ),
        ],
        try_it=[
            problem(
                "im2-u4-l1-t1",
                "Solve $x^{2} - 7x = 18$.",
                "Rearrange: $x^{2} - 7x - 18 = 0$. Product $-18$, sum $-7$: $2$ and $-9$. So "
                "$(x + 2)(x - 9) = 0$ and $x = -2$ or $x = 9$. Check in the original: "
                "$4 + 14 = 18$ ✓ and $81 - 63 = 18$ ✓",
                [
                    "Eq((-2)**2 - 7*(-2), 18)",
                    "Eq(9**2 - 7*9, 18)",
                    "Eq(2*(-9), -18)",
                    "Eq(2 + (-9), -7)",
                ],
            ),
            problem(
                "im2-u4-l1-t2",
                "Solve $3(x + 2)^{2} = 27$.",
                "Divide by $3$: $(x + 2)^{2} = 9$. Take roots with both signs: $x + 2 = \\pm 3$, "
                "so $x = 1$ or $x = -5$. Check: $3(9) = 27$ ✓ for both, since $(1+2)^{2} = 9$ and "
                "$(-5+2)^{2} = 9$. Note the two roots are each $3$ units from $x = -2$, the "
                "vertex.",
                [
                    "Eq(3*(1 + 2)**2, 27)",
                    "Eq(3*(-5 + 2)**2, 27)",
                    "Eq((1 + (-5))/2, -2)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-REI.4b",
                "title": "Zero is the only useful right-hand side",
                "body": (
                    "A product equal to zero forces one factor to be zero. A product equal to any "
                    "other number forces nothing. That asymmetry is why every factoring solution "
                    "begins by moving everything to one side."
                ),
                "beats": [
                    "Rearrange to $= 0$",
                    "Factor the left side",
                    "Set each factor to zero",
                    "Solve the tiny linear equations",
                ],
            },
            {
                "kind": "worked",
                "title": "Rearrange, factor, split",
                "problemId": "im2-u4-l1-we1",
            },
            tap(
                "What can you conclude?",
                "You know $(x - 2)(x + 7) = 0$. What follows?",
                [
                    "$x = 2$ or $x = -7$",
                    "$x = -2$ or $x = 7$",
                    "$x = 2$ and $x = -7$ simultaneously",
                    "nothing without more information",
                ],
                0,
                "A product is zero when a factor is zero: $x - 2 = 0$ gives $x = 2$, and "
                "$x + 7 = 0$ gives $x = -7$. It is 'or', not 'and' — a single value of $x$ cannot "
                "be both.",
                ["Eq((2 - 2)*(2 + 7), 0)", "Eq((-7 - 2)*(-7 + 7), 0)"],
            ),
            {
                "kind": "tip",
                "eyebrow": "The vanishing root",
                "title": "Never divide by a variable",
                "body": (
                    "Dividing $3x^{2} = 12x$ by $x$ loses the solution $x = 0$, silently. "
                    "Factoring loses nothing. Whenever both sides share a variable factor, factor "
                    "it out rather than cancelling it away."
                ),
            },
            {
                "kind": "worked",
                "title": "A common factor, and a pure square",
                "problemId": "im2-u4-l1-we2",
            },
            {
                "kind": "parabolaGraph",
                "eyebrow": "Roots on the graph",
                "title": "Solving is finding the crossings",
                "teach": (
                    "Every solution of $ax^{2} + bx + c = 0$ is a point where the parabola meets "
                    "the horizontal axis. Drag the curve up and down and watch the two crossings "
                    "approach each other, merge into a single touch, then disappear entirely."
                ),
                "config": {"mode": "roots", "a": 1, "h": 1, "k": -4, "interactive": True, "min": -8, "max": 8},
            },
            {
                "kind": "teach",
                "eyebrow": "No linear term",
                "title": "When there is no middle term, take roots",
                "body": (
                    "$(x - h)^{2} = c$ does not need expanding, factoring, or any formula. Isolate "
                    "the square, take the root of both sides, and write $\\pm$. It is the fastest "
                    "method available and it is available more often than people notice."
                ),
            },
            {
                "kind": "worked",
                "title": "The square-root method, step by step",
                "problemId": "im2-u4-l1-we3",
            },
            tap(
                "How many solutions?",
                "How many real solutions does $(x + 4)^{2} = 0$ have?",
                ["two", "one", "none", "infinitely many"],
                1,
                "Only $x = -4$. The factor $(x + 4)$ appears twice, so it is called a double "
                "root — but there is a single value of $x$, and the parabola touches the axis "
                "there rather than crossing.",
                ["Eq((-4 + 4)**2, 0)", "(0 + 4)**2 > 0"],
            ),
            {
                "kind": "worked",
                "title": "A double root, and fractional roots",
                "problemId": "im2-u4-l1-we4",
            },
            {"kind": "tryIt", "title": "Rearrange then factor", "problemId": "im2-u4-l1-t1"},
            {"kind": "tryIt", "title": "Isolate then take roots", "problemId": "im2-u4-l1-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Zero on one side FIRST — the zero-product property needs a zero",
                    "Factor, then set each factor to zero",
                    "Never divide by a variable; factor it out and keep the root",
                    "No linear term? Isolate the square and take roots — with $\\pm$",
                    "A repeated factor gives a double root: one value, a touching parabola",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 2 — A-REI.4a: completing the square
# ===========================================================================
def lesson_completing_the_square():
    return lesson(
        slug="completing-the-square",
        title="Completing the Square",
        concrete=(
            "Lay out $x^{2} + 6x$ as a square tile and six strips. Put three strips down one side "
            "and three down the other and you almost have a square — with a $3 \\times 3$ corner "
            "missing. Add nine, and the picture is complete. That missing corner is what "
            "'completing the square' literally means, and it is why the number you add is always "
            "the square of half the middle coefficient."
        ),
        objective=(
            "Complete the square to rewrite a quadratic in vertex form, solve any quadratic "
            "equation this way, and see why the method works geometrically."
        ),
        concept=[
            "**The pattern being reversed.** $(x + p)^{2} = x^{2} + 2px + p^{2}$. So if you are "
            "given $x^{2} + bx$, matching gives $2p = b$, hence $p = \\frac{b}{2}$, and the "
            "missing constant is $p^{2} = \\left(\\frac{b}{2}\\right)^{2}$. Halve, then square — "
            "in that order.",
            "**Whatever you add must be added to both sides.** Adding $9$ to complete "
            "$x^{2} + 6x$ changes the expression, so the equation must be balanced by adding $9$ "
            "on the other side too. Skipping this is not a small slip; it produces a different "
            "equation with different solutions.",
            "**The leading coefficient must be 1 before you start.** For $2x^{2} + 8x = 10$, "
            "divide through by $2$ first: $x^{2} + 4x = 5$. Trying to halve $8$ while the $2$ is "
            "still attached gives the wrong constant, because the pattern being matched assumes a "
            "leading coefficient of one.",
            "**Completing the square converts standard form into vertex form.** "
            "$x^{2} - 6x + 5 = (x - 3)^{2} - 4$ — and the vertex $(3, -4)$ is now readable. This "
            "is the algebraic bridge between the forms that Unit 3 could only describe.",
            "**When the constant is added inside a bracket, it gets multiplied.** In "
            "$3(x^{2} + 4x) + 1$, adding $4$ inside the bracket actually adds $12$ to the "
            "expression, so $12$ must be subtracted outside to compensate. This bookkeeping is "
            "where most errors live.",
            "**It always works.** Unlike factoring, completing the square never fails and never "
            "requires a lucky pair of integers. That universality is exactly why the next lesson "
            "can run it on the general equation and obtain a formula.",
        ],
        key_idea=(
            "To complete $x^{2} + bx$, add $\\left(\\frac{b}{2}\\right)^{2}$ — halve the middle "
            "coefficient, then square it — and balance the equation by adding the same amount to "
            "the other side."
        ),
        facts=[
            fact(
                "The completing constant",
                "x^{2} + bx + \\left(\\frac{b}{2}\\right)^{2} = \\left(x + \\frac{b}{2}\\right)^{2}",
                "Halve, then square. The order matters and is easy to reverse by accident.",
            ),
            fact(
                "Balance the equation",
                "x^{2} + bx = c \\ \\Rightarrow\\ x^{2} + bx + \\left(\\tfrac{b}{2}\\right)^{2} = c + \\left(\\tfrac{b}{2}\\right)^{2}",
                "Both sides, or it is a different equation.",
            ),
            fact(
                "Divide out the leading coefficient first",
                "ax^{2} + bx + c = 0 \\ \\Rightarrow\\ x^{2} + \\frac{b}{a}x + \\frac{c}{a} = 0",
                "The pattern assumes a leading coefficient of one.",
            ),
            fact(
                "The result is vertex form",
                "a(x - h)^{2} + k",
                "So completing the square finds the vertex as a by-product of solving.",
            ),
        ],
        worked=[
            problem(
                "im2-u4-l2-we1",
                "Solve $x^{2} + 6x - 7 = 0$ by completing the square.",
                "**Move the constant to the right.** Keep the variable terms together on the "
                "left:"
                "$$x^{2} + 6x = 7.$$"
                "**Halve the middle coefficient and square it.** Half of $6$ is $3$; $3^{2} = 9$. "
                "That $9$ is the missing corner of the square."
                "**Add it to BOTH sides.**"
                "$$x^{2} + 6x + 9 = 7 + 9 = 16.$$"
                "**Write the left side as a square.**"
                "$$(x + 3)^{2} = 16.$$"
                "**Take roots, with both signs.** $x + 3 = \\pm 4$, so $x = 1$ or $x = -7$."
                "**Check both in the original.** At $x = 1$: $1 + 6 - 7 = 0$ ✓ At $x = -7$: "
                "$49 - 42 - 7 = 0$ ✓"
                "**A by-product worth noticing.** The working produced "
                "$x^{2} + 6x - 7 = (x + 3)^{2} - 16$, so the vertex is $(-3, -16)$ — obtained for "
                "free while solving.",
                [
                    "Eq(1**2 + 6*1 - 7, 0)",
                    "Eq((-7)**2 + 6*(-7) - 7, 0)",
                    "Eq((6/2)**2, 9)",
                    "Eq((1 + 3)**2, 16)",
                    "Eq((-3)**2 + 6*(-3) - 7, -16)",
                ],
            ),
            problem(
                "im2-u4-l2-we2",
                "Solve $x^{2} - 8x + 3 = 0$ by completing the square, leaving the answers in "
                "exact form.",
                "**Move the constant.**"
                "$$x^{2} - 8x = -3.$$"
                "**Halve and square.** Half of $-8$ is $-4$; $(-4)^{2} = 16$. Note the square is "
                "positive even though the coefficient was negative."
                "**Add to both sides.**"
                "$$x^{2} - 8x + 16 = -3 + 16 = 13.$$"
                "**Factor the left side.**"
                "$$(x - 4)^{2} = 13.$$"
                "**Take roots.**"
                "$$x - 4 = \\pm\\sqrt{13} \\quad\\Longrightarrow\\quad x = 4 \\pm \\sqrt{13}.$$"
                "**Leave it exact.** $\\sqrt{13}$ is irrational, so $4 + \\sqrt{13}$ and "
                "$4 - \\sqrt{13}$ ARE the answers — writing $7.606$ would be an approximation, not "
                "a solution."
                "**Check the pair against the structure.** Their sum is $8$, which must equal "
                "$-\\frac{b}{a} = 8$ ✓ and their product is $16 - 13 = 3$, which must equal "
                "$\\frac{c}{a} = 3$ ✓ Two independent confirmations without substituting a "
                "radical into anything."
                "**Why factoring was never going to work here.** No pair of integers multiplies "
                "to $3$ and adds to $-8$. Completing the square does not care.",
                [
                    "Eq(((-8)/2)**2, 16)",
                    "Eq((4 + sqrt(13)) + (4 - sqrt(13)), 8)",
                    "Eq(simplify((4 + sqrt(13))*(4 - sqrt(13))), 3)",
                    "Eq(simplify((4 + sqrt(13))**2 - 8*(4 + sqrt(13)) + 3), 0)",
                    "Eq(simplify((4 - sqrt(13))**2 - 8*(4 - sqrt(13)) + 3), 0)",
                ],
            ),
            problem(
                "im2-u4-l2-we3",
                "Solve $2x^{2} + 12x - 14 = 0$ by completing the square.",
                "**Divide through by the leading coefficient first.** The pattern needs a leading "
                "coefficient of $1$:"
                "$$x^{2} + 6x - 7 = 0.$$"
                "Dividing an equation by $2$ is safe because the right side is zero — zero divided "
                "by two is still zero, so no solutions are gained or lost."
                "**Move the constant.**"
                "$$x^{2} + 6x = 7.$$"
                "**Halve, square, add to both sides.** Half of $6$ is $3$, squared is $9$:"
                "$$(x + 3)^{2} = 16.$$"
                "**Solve.** $x + 3 = \\pm 4$, giving $x = 1$ and $x = -7$."
                "**Check in the ORIGINAL, undivided equation.** At $x = 1$: "
                "$2 + 12 - 14 = 0$ ✓ At $x = -7$: $98 - 84 - 14 = 0$ ✓"
                "**What goes wrong without the division.** Halving $12$ gives $6$ and squaring "
                "gives $36$; adding $36$ to $2x^{2} + 12x$ produces $2x^{2} + 12x + 36$, which is "
                "not a perfect square — $(x+6)^2$ would need a leading coefficient of $1$, and "
                "$2(x+3)^2 = 2x^2 + 12x + 18$ needs $18$, not $36$. The division is not optional.",
                [
                    "Eq(2*1**2 + 12*1 - 14, 0)",
                    "Eq(2*(-7)**2 + 12*(-7) - 14, 0)",
                    "Eq(2*(1**2 + 6*1 - 7), 2*1**2 + 12*1 - 14)",
                    "Eq(2*(0 + 3)**2, 2*0**2 + 12*0 + 18)",
                    "Ne(2*0**2 + 12*0 + 36, 2*(0 + 3)**2)",
                ],
            ),
            problem(
                "im2-u4-l2-we4",
                "Rewrite $f(x) = 3x^{2} - 12x + 5$ in vertex form by completing the square, and "
                "state the minimum value.",
                "**Factor the leading coefficient out of the variable terms only.** The constant "
                "stays outside:"
                "$$f(x) = 3(x^{2} - 4x) + 5.$$"
                "**Complete the square inside the bracket.** Half of $-4$ is $-2$, squared is $4$. "
                "Add it inside — but adding $4$ inside a bracket multiplied by $3$ adds $12$ to "
                "the function, so subtract $12$ outside to compensate:"
                "$$f(x) = 3(x^{2} - 4x + 4) + 5 - 12.$$"
                "**Write the bracket as a square and tidy.**"
                "$$f(x) = 3(x - 2)^{2} - 7.$$"
                "**Read off the vertex.** $(2, -7)$, and since $a = 3 > 0$ the parabola opens "
                "upward, so $-7$ is the MINIMUM value, attained at $x = 2$."
                "**Verify the two forms agree.** At $x = 0$: standard gives $5$; vertex form gives "
                "$3(4) - 7 = 5$ ✓ At $x = 3$: standard gives $27 - 36 + 5 = -4$; vertex form gives "
                "$3(1) - 7 = -4$ ✓"
                "**The compensation step, restated.** Whatever you add inside the bracket is "
                "multiplied by the coefficient in front. Adding $4$ inside a bracket times $3$ "
                "means the function grew by $12$, so $12$ must come back off.",
                [
                    "Eq(3*0**2 - 12*0 + 5, 5)",
                    "Eq(3*(0 - 2)**2 - 7, 5)",
                    "Eq(3*3**2 - 12*3 + 5, -4)",
                    "Eq(3*(3 - 2)**2 - 7, -4)",
                    "Eq(3*(2 - 2)**2 - 7, -7)",
                    "Eq(3*4, 12)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Squaring the middle coefficient before halving it.",
                "For $x^2 + 6x$ the constant is $(6/2)^2 = 9$, not $6^2/2 = 18$. Halve FIRST, "
                "then square. Check by expanding $(x + 3)^2 = x^2 + 6x + 9$ ✓",
            ),
            mistake(
                "Adding the completing constant to only one side.",
                "$x^2 + 6x = 7$ becomes $x^2 + 6x + 9 = 16$, not $= 7$. Adding to one side "
                "produces a different equation with different solutions.",
            ),
            mistake(
                "Completing the square without dividing out the leading coefficient.",
                "$2x^2 + 12x$ needs the $2$ removed first. The pattern $x^2 + bx + (b/2)^2$ "
                "assumes a leading coefficient of one.",
            ),
            mistake(
                "Forgetting that a constant added INSIDE a bracket is multiplied.",
                "In $3(x^2 - 4x + 4)$ the added $4$ contributes $12$ to the expression, so $12$ "
                "must be subtracted outside. Check by expanding both forms at one value of $x$.",
            ),
        ],
        try_it=[
            problem(
                "im2-u4-l2-t1",
                "Solve $x^{2} + 10x + 9 = 0$ by completing the square.",
                "Move the constant: $x^{2} + 10x = -9$. Half of $10$ is $5$, squared is $25$; add "
                "to both sides: $(x + 5)^{2} = 16$. Roots: $x + 5 = \\pm 4$, so $x = -1$ or "
                "$x = -9$. Check: $1 - 10 + 9 = 0$ ✓ and $81 - 90 + 9 = 0$ ✓",
                [
                    "Eq((10/2)**2, 25)",
                    "Eq((-1)**2 + 10*(-1) + 9, 0)",
                    "Eq((-9)**2 + 10*(-9) + 9, 0)",
                    "Eq((-1 + 5)**2, 16)",
                ],
            ),
            problem(
                "im2-u4-l2-t2",
                "Write $y = x^{2} + 5x + 2$ in vertex form.",
                "Half of $5$ is $\\frac{5}{2}$, squared is $\\frac{25}{4}$. Add and subtract it: "
                "$y = \\left(x^{2} + 5x + \\frac{25}{4}\\right) + 2 - \\frac{25}{4} = "
                "\\left(x + \\frac{5}{2}\\right)^{2} - \\frac{17}{4}$. Vertex "
                "$\\left(-\\frac{5}{2}, -\\frac{17}{4}\\right)$. Check at $x = 0$: standard gives "
                "$2$, and $\\frac{25}{4} - \\frac{17}{4} = 2$ ✓ Fractions are normal here — an "
                "odd middle coefficient guarantees them.",
                [
                    "Eq(Rational(5,2)**2, Rational(25,4))",
                    "Eq(2 - Rational(25,4), Rational(-17,4))",
                    "Eq((0 + Rational(5,2))**2 - Rational(17,4), 2)",
                    "Eq((1 + Rational(5,2))**2 - Rational(17,4), 1**2 + 5*1 + 2)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-REI.4a",
                "title": "The one method that never fails",
                "body": (
                    "Factoring needs luck. Square roots need a missing middle term. Completing the "
                    "square works on every quadratic ever written — which is why the next lesson "
                    "can run it on the general case and get a formula out."
                ),
                "beats": [
                    "Leading coefficient to $1$",
                    "Constant to the right",
                    "Add $\\left(\\frac{b}{2}\\right)^{2}$ to both sides",
                    "Factor, take roots, solve",
                ],
            },
            {
                "kind": "algebraTiles",
                "eyebrow": "Where the name comes from",
                "title": "The missing corner",
                "teach": (
                    "One $x^{2}$ tile and six $x$-strips: put three strips along the top and three "
                    "down the side and the arrangement is a square except for a $3 \\times 3$ hole "
                    "in the corner. Nine unit tiles fill it — and $9$ is exactly "
                    "$\\left(\\frac{6}{2}\\right)^{2}$."
                ),
                "config": {"x": 6, "units": 9, "mode": "build", "maxX": 10, "maxUnits": 16},
            },
            {
                "kind": "teach",
                "eyebrow": "The rule, and why",
                "title": "Halve, then square",
                "body": (
                    "$(x + p)^{2} = x^{2} + 2px + p^{2}$. Comparing with $x^{2} + bx$ forces "
                    "$p = \\frac{b}{2}$, so the constant needed is "
                    "$\\left(\\frac{b}{2}\\right)^{2}$. The rule is not arbitrary — it is what the "
                    "expansion demands."
                ),
            },
            {
                "kind": "worked",
                "title": "The full procedure on a friendly example",
                "problemId": "im2-u4-l2-we1",
            },
            tap(
                "What do you add?",
                "To complete the square on $x^{2} - 14x$, what constant do you add?",
                ["$-7$", "$49$", "$-49$", "$196$"],
                1,
                "Half of $-14$ is $-7$, and $(-7)^{2} = 49$. The added constant is always "
                "positive, because it is a square. Check: $x^{2} - 14x + 49 = (x - 7)^{2}$ ✓",
                ["Eq((-14/2)**2, 49)", "Eq((3 - 7)**2, 3**2 - 14*3 + 49)"],
            ),
            {
                "kind": "worked",
                "title": "When the answer is irrational",
                "problemId": "im2-u4-l2-we2",
            },
            {
                "kind": "tip",
                "eyebrow": "Order of operations",
                "title": "Leading coefficient first",
                "body": (
                    "Divide (or factor) out the leading coefficient before halving anything. The "
                    "completing pattern assumes a bare $x^{2}$, and applying it to $2x^{2} + 12x$ "
                    "produces a constant that does not fit."
                ),
            },
            {
                "kind": "worked",
                "title": "With a leading coefficient",
                "problemId": "im2-u4-l2-we3",
            },
            {
                "kind": "parabolaGraph",
                "eyebrow": "What you have produced",
                "title": "Completing the square IS finding the vertex",
                "teach": (
                    "The output of completing the square is $a(x - h)^{2} + k$ — vertex form. So "
                    "the method that solves the equation also hands you the turning point, without "
                    "any extra work."
                ),
                "config": {"mode": "vertex", "a": 1, "h": 2, "k": -1, "interactive": True, "min": -8, "max": 8},
            },
            {
                "kind": "worked",
                "title": "Standard form to vertex form",
                "problemId": "im2-u4-l2-we4",
            },
            tap(
                "Inside the bracket",
                "In $2(x^{2} + 6x) + 1$, you add $9$ inside the bracket. What must you do "
                "outside to keep the expression unchanged?",
                ["subtract $9$", "subtract $18$", "add $18$", "nothing"],
                1,
                "The bracket is multiplied by $2$, so adding $9$ inside adds $2 \\times 9 = 18$ "
                "to the whole expression. Subtract $18$ outside to compensate.",
                ["Eq(2*9, 18)", "Eq(2*(1**2 + 6*1 + 9) + 1 - 18, 2*(1**2 + 6*1) + 1)"],
            ),
            {"kind": "tryIt", "title": "A clean completion", "problemId": "im2-u4-l2-t1"},
            {"kind": "tryIt", "title": "An odd middle coefficient", "problemId": "im2-u4-l2-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Add $\\left(\\frac{b}{2}\\right)^{2}$ — halve first, then square",
                    "Balance: whatever you add on the left goes on the right too",
                    "Divide out the leading coefficient before starting",
                    "A constant added inside a bracket is multiplied by the coefficient outside",
                    "The output is vertex form, so the vertex arrives free with the solution",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 3 — A-REI.4a/b: the quadratic formula and the discriminant
# ===========================================================================
def lesson_quadratic_formula():
    return lesson(
        slug="the-quadratic-formula",
        title="The Quadratic Formula and the Discriminant",
        concrete=(
            "Completing the square works on every quadratic, which means it works on the general "
            "quadratic — the one with letters instead of numbers. Do it once, on "
            "$ax^{2} + bx + c = 0$, and the answer is a formula that solves every quadratic "
            "forever. The formula is not a separate fact to memorise; it is last lesson's method, "
            "done once and saved."
        ),
        objective=(
            "Derive the quadratic formula by completing the square on the general equation, apply "
            "it, and use the discriminant to predict the number and type of roots before solving."
        ),
        concept=[
            "**The derivation, in five steps.** Divide by $a$; move the constant; add "
            "$\\left(\\frac{b}{2a}\\right)^{2}$ to both sides; factor the left as "
            "$\\left(x + \\frac{b}{2a}\\right)^{2}$; take roots. What comes out is "
            "$x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$ — nothing was invented along the way.",
            "**The discriminant is the part under the root.** $D = b^{2} - 4ac$ decides "
            "everything about the roots without producing them: $D > 0$ gives two distinct real "
            "roots, $D = 0$ gives one repeated real root, $D < 0$ gives no real roots (two complex "
            "ones, as Lesson 4 will show).",
            "**Why the discriminant controls the count.** The formula adds and subtracts "
            "$\\sqrt{D}$. If $D$ is positive that is two different numbers; if $D$ is zero the "
            "$\\pm$ adds nothing and both branches coincide; if $D$ is negative there is no real "
            "square root and the real line has nothing to offer.",
            "**A perfect-square discriminant means the quadratic factors over the integers.** "
            "$D = 49$ produces $\\sqrt{D} = 7$, a whole number, so the roots are rational and the "
            "expression could have been factored. This is a useful check BEFORE attempting to "
            "factor, and it never lies.",
            "**Choose the method by the equation, not by habit.** No middle term? Square roots. "
            "Factors visibly? Factor. Neither? Formula. Need the vertex as well? Complete the "
            "square. The formula always works but is rarely the fastest.",
            "**Watch the sign of the middle coefficient.** For $x^{2} - 5x + 6 = 0$ the formula opens "
            "with $-b = +5$. Substituting $b = -5$ correctly, including the minus, is where most "
            "formula errors happen — write the values down before substituting.",
        ],
        key_idea=(
            "$x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$ is completing the square done once on "
            "the general equation, and the sign of $b^{2} - 4ac$ tells you what kind of answer to "
            "expect before you compute it."
        ),
        facts=[
            fact(
                "The quadratic formula",
                "x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}",
                "Works on every quadratic. Requires standard form with zero on one side.",
            ),
            fact(
                "The discriminant",
                "D = b^{2} - 4ac",
                "$D > 0$: two real roots. $D = 0$: one. $D < 0$: none real.",
            ),
            fact(
                "Sum and product of the roots",
                "r_{1} + r_{2} = -\\frac{b}{a}, \\qquad r_{1}r_{2} = \\frac{c}{a}",
                "A fast check on any pair of answers, radicals included.",
            ),
            fact(
                "Rational-root test",
                "D \\text{ a perfect square} \\iff \\text{the roots are rational}",
                "So a non-square discriminant means factoring over the integers is hopeless.",
            ),
        ],
        worked=[
            problem(
                "im2-u4-l3-we1",
                "Derive the quadratic formula by completing the square on $ax^{2} + bx + c = 0$.",
                "**Divide by the leading coefficient.** Legal because $a \\neq 0$:"
                "$$x^{2} + \\frac{b}{a}x + \\frac{c}{a} = 0.$$"
                "**Move the constant to the right.**"
                "$$x^{2} + \\frac{b}{a}x = -\\frac{c}{a}.$$"
                "**Halve the middle coefficient and square it.** Half of $\\frac{b}{a}$ is "
                "$\\frac{b}{2a}$, and its square is $\\frac{b^{2}}{4a^{2}}$. Add to both sides:"
                "$$x^{2} + \\frac{b}{a}x + \\frac{b^{2}}{4a^{2}} = "
                "\\frac{b^{2}}{4a^{2}} - \\frac{c}{a}.$$"
                "**Factor the left and combine the right over a common denominator.**"
                "$$\\left(x + \\frac{b}{2a}\\right)^{2} = \\frac{b^{2} - 4ac}{4a^{2}}.$$"
                "**Take roots of both sides.**"
                "$$x + \\frac{b}{2a} = \\pm\\frac{\\sqrt{b^{2} - 4ac}}{2a}.$$"
                "**Isolate the variable.**"
                "$$x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}.$$"
                "**Test the formula on a case you can check independently.** For "
                "$x^{2} - 5x + 6 = 0$: $D = 25 - 24 = 1$, so "
                "$x = \\frac{5 \\pm 1}{2}$, giving $3$ and $2$. Factoring gives "
                "$(x - 2)(x - 3) = 0$ — the same roots ✓ The derivation produces a formula that "
                "agrees with the methods it generalises.",
                [
                    "Eq(25 - 24, 1)",
                    "Eq((5 + 1)/2, 3)",
                    "Eq((5 - 1)/2, 2)",
                    "Eq(3**2 - 5*3 + 6, 0)",
                    "Eq(2**2 - 5*2 + 6, 0)",
                    "Eq((2 - 2)*(2 - 3), 0)",
                ],
            ),
            problem(
                "im2-u4-l3-we2",
                "Solve $2x^{2} - 7x - 4 = 0$ with the quadratic formula, and confirm with "
                "factoring.",
                "**Identify the coefficients before substituting.** $a = 2$, $b = -7$, $c = -4$. "
                "Writing them down separately is what prevents sign errors."
                "**Compute the discriminant.**"
                "$$D = (-7)^{2} - 4(2)(-4) = 49 + 32 = 81.$$"
                "Positive, and a perfect square — so expect two rational roots, which also means "
                "the expression factors over the integers."
                "**Substitute into the formula.**"
                "$$x = \\frac{7 \\pm \\sqrt{81}}{4} = \\frac{7 \\pm 9}{4}.$$"
                "Note $-b = -(-7) = +7$."
                "**Split the two branches.**"
                "$$x = \\frac{16}{4} = 4 \\quad\\text{or}\\quad x = \\frac{-2}{4} = -\\frac{1}{2}.$$"
                "**Confirm by factoring.** $ac = -8$, sum $-7$: the pair is $1$ and $-8$. "
                "Splitting: $2x^{2} + x - 8x - 4 = x(2x + 1) - 4(2x + 1) = (2x + 1)(x - 4) = 0$, "
                "giving $x = -\\frac{1}{2}$ and $x = 4$ ✓ Same answers by two independent routes."
                "**A third check, using sum and product.** The roots sum to "
                "$4 - \\frac{1}{2} = \\frac{7}{2} = -\\frac{b}{a}$ ✓ and multiply to "
                "$-2 = \\frac{c}{a}$ ✓",
                [
                    "Eq((-7)**2 - 4*2*(-4), 81)",
                    "Eq((7 + 9)/4, 4)",
                    "Eq((7 - 9)/4, Rational(-1,2))",
                    "Eq(2*4**2 - 7*4 - 4, 0)",
                    "Eq(2*Rational(-1,2)**2 - 7*Rational(-1,2) - 4, 0)",
                    "Eq(4 + Rational(-1,2), Rational(7,2))",
                    "Eq(4*Rational(-1,2), -2)",
                ],
            ),
            problem(
                "im2-u4-l3-we3",
                "Use the discriminant to describe the roots of each, without solving: "
                "(a) $x^{2} - 6x + 9 = 0$; (b) $2x^{2} + 3x - 4 = 0$; (c) $x^{2} + x + 5 = 0$; "
                "(d) $3x^{2} - 5x - 2 = 0$.",
                "**Part (a).** $D = 36 - 36 = 0$. One repeated real root — the parabola touches "
                "the horizontal axis. Indeed $x^{2} - 6x + 9 = (x - 3)^{2}$, so the root is $3$."
                "**Part (b).** $D = 9 - 4(2)(-4) = 9 + 32 = 41$. Positive but not a perfect "
                "square, so two IRRATIONAL real roots. Factoring over the integers is impossible "
                "here, and knowing that in advance saves a fruitless search."
                "**Part (c).** $D = 1 - 20 = -19$. Negative, so no real roots — the parabola sits "
                "entirely above the horizontal axis. (Lesson 4 supplies two complex roots.)"
                "**Part (d).** $D = 25 - 4(3)(-2) = 25 + 24 = 49$. Positive and a perfect square, "
                "so two RATIONAL roots and the expression factors: "
                "$(3x + 1)(x - 2) = 0$, giving $-\\frac{1}{3}$ and $2$."
                "**The general reading.** The sign of $D$ gives the count; whether $D$ is a "
                "perfect square gives the type. Both are available for the cost of one "
                "subtraction, before any solving happens.",
                [
                    "Eq(36 - 4*1*9, 0)",
                    "Eq(3**2 - 4*2*(-4), 41)",
                    "Eq(1 - 4*1*5, -19)",
                    "Eq((-5)**2 - 4*3*(-2), 49)",
                    "Eq(3*2**2 - 5*2 - 2, 0)",
                    "Eq(3*Rational(-1,3)**2 - 5*Rational(-1,3) - 2, 0)",
                    "Eq(3**2 - 6*3 + 9, 0)",
                ],
            ),
            problem(
                "im2-u4-l3-we4",
                "A ball is kicked from ground level and its height in metres after $t$ seconds is "
                "$h(t) = -5t^{2} + 17t$. Find when it is $12$ metres high, and when it lands.",
                "**Set up the height equation.** Twelve metres means:"
                "$$-5t^{2} + 17t = 12 \\quad\\Longrightarrow\\quad -5t^{2} + 17t - 12 = 0.$$"
                "**Tidy the signs.** Multiplying through by $-1$ is safe and makes the arithmetic "
                "easier:"
                "$$5t^{2} - 17t + 12 = 0.$$"
                "**Check the discriminant first.**"
                "$$D = 289 - 4(5)(12) = 289 - 240 = 49,$$"
                "a perfect square — so the answers will be rational."
                "**Apply the formula.**"
                "$$t = \\frac{17 \\pm 7}{10},$$"
                "giving $t = \\frac{24}{10} = 2.4$ and $t = 1$."
                "**Interpret BOTH answers.** The ball passes $12$ m on the way up at $t = 1$ s and "
                "again on the way down at $t = 2.4$ s. Neither is spurious — a thrown object "
                "genuinely visits most heights twice."
                "**Find the landing time.** Height zero: $-5t^{2} + 17t = 0$, so "
                "$t(-5t + 17) = 0$ and $t = 0$ or $t = \\frac{17}{5} = 3.4$ s. The root $t = 0$ is "
                "the kick itself; the ball lands at $3.4$ s."
                "**Sanity-check against symmetry.** The peak is midway between $0$ and $3.4$, at "
                "$t = 1.7$ s, and $h(1.7) = -5(2.89) + 28.9 = 14.45$ m. Both $12$-metre times, "
                "$1$ and $2.4$, are $0.7$ s either side of $1.7$ ✓",
                [
                    "Eq((-17)**2 - 4*5*12, 49)",
                    "Eq((17 + 7)/10, Rational(12,5))",
                    "Eq((17 - 7)/10, 1)",
                    "Eq(-5*1**2 + 17*1, 12)",
                    "Eq(-5*Rational(12,5)**2 + 17*Rational(12,5), 12)",
                    "Eq(-5*Rational(17,5)**2 + 17*Rational(17,5), 0)",
                    "Eq(-5*Rational(17,10)**2 + 17*Rational(17,10), Rational(289,20))",
                    "Eq(Rational(17,10) - 1, Rational(12,5) - Rational(17,10))",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Substituting $b$ without its sign.",
                "For $x^2 - 5x + 6$, $b = -5$, so $-b = +5$ and $b^2 = 25$. Write $a$, $b$ and "
                "$c$ down as signed numbers before touching the formula.",
            ),
            mistake(
                "Dividing only the radical by $2a$.",
                "The whole numerator $-b \\pm \\sqrt{D}$ sits over $2a$. Writing "
                "$-b \\pm \\frac{\\sqrt{D}}{2a}$ gives wrong roots — check with a case you can "
                "factor.",
            ),
            mistake(
                "Applying the formula without moving everything to one side.",
                "$2x^2 - 7x = 4$ has $c = -4$, not $+4$. The formula reads coefficients from "
                "$ax^2 + bx + c = 0$, so rearrange first.",
            ),
            mistake(
                "Reading $D < 0$ as 'no solutions'.",
                "It means no REAL solutions. There are always two complex ones — that is Lesson "
                "4, and the distinction matters.",
            ),
        ],
        try_it=[
            problem(
                "im2-u4-l3-t1",
                "Solve $x^{2} + 4x - 6 = 0$ with the formula, leaving the answers exact.",
                "$a = 1$, $b = 4$, $c = -6$. $D = 16 + 24 = 40$, positive but not a perfect "
                "square, so the roots are irrational. $x = \\frac{-4 \\pm \\sqrt{40}}{2} = "
                "\\frac{-4 \\pm 2\\sqrt{10}}{2} = -2 \\pm \\sqrt{10}$. Check via sum and product: "
                "the roots sum to $-4 = -\\frac{b}{a}$ ✓ and multiply to $4 - 10 = -6 = "
                "\\frac{c}{a}$ ✓",
                [
                    "Eq(4**2 - 4*1*(-6), 40)",
                    "Eq(simplify(sqrt(40)), 2*sqrt(10))",
                    "Eq((-2 + sqrt(10)) + (-2 - sqrt(10)), -4)",
                    "Eq(simplify((-2 + sqrt(10))*(-2 - sqrt(10))), -6)",
                    "Eq(simplify((-2 + sqrt(10))**2 + 4*(-2 + sqrt(10)) - 6), 0)",
                ],
            ),
            problem(
                "im2-u4-l3-t2",
                "Without solving, say how many real roots each has: $4x^{2} - 12x + 9 = 0$ and "
                "$x^{2} + 2x + 7 = 0$.",
                "First: $D = 144 - 4(4)(9) = 144 - 144 = 0$, so exactly ONE real root (a double "
                "root at $x = \\frac{3}{2}$; indeed $4x^{2} - 12x + 9 = (2x - 3)^{2}$). Second: "
                "$D = 4 - 28 = -24 < 0$, so NO real roots — the parabola never reaches the "
                "horizontal axis.",
                [
                    "Eq((-12)**2 - 4*4*9, 0)",
                    "Eq(4*Rational(3,2)**2 - 12*Rational(3,2) + 9, 0)",
                    "Eq(2**2 - 4*1*7, -24)",
                    "1**2 + 2*1 + 7 > 0",
                    "(-1)**2 + 2*(-1) + 7 > 0",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-REI.4a",
                "title": "One derivation, every quadratic",
                "body": (
                    "Completing the square works on any quadratic — so run it on the general one, "
                    "with letters. The result is a formula, and every step of the derivation is a "
                    "step you did with numbers last lesson."
                ),
                "beats": [
                    "Divide by $a$",
                    "Move $\\frac{c}{a}$ across",
                    "Add $\\left(\\frac{b}{2a}\\right)^{2}$",
                    "Take roots and isolate $x$",
                ],
            },
            {
                "kind": "worked",
                "title": "The derivation, in full",
                "problemId": "im2-u4-l3-we1",
            },
            {
                "kind": "tip",
                "eyebrow": "Before you substitute",
                "title": "Write down $a$, $b$ and $c$ with their signs",
                "body": (
                    "Three lines: $a = \\ldots$, $b = \\ldots$, $c = \\ldots$, each with its sign "
                    "attached. Almost every formula error is a sign that went missing between the "
                    "equation and the substitution, and this habit eliminates it."
                ),
            },
            {
                "kind": "worked",
                "title": "The formula, cross-checked by factoring",
                "problemId": "im2-u4-l3-we2",
            },
            {
                "kind": "teach",
                "eyebrow": "The part under the root",
                "title": "The discriminant answers before you solve",
                "body": (
                    "$D = b^{2} - 4ac$ costs one subtraction and tells you the count and the type "
                    "of the roots. Positive means two, zero means one, negative means none real — "
                    "and a perfect square means the roots are rational, so factoring will work."
                ),
            },
            {
                "kind": "parabolaGraph",
                "eyebrow": "See the discriminant",
                "title": "Two crossings, one touch, or none",
                "teach": (
                    "Slide the parabola vertically. Cutting the axis twice is $D > 0$; touching it "
                    "is $D = 0$; floating clear of it is $D < 0$. The discriminant is measuring "
                    "exactly this vertical position."
                ),
                "config": {"mode": "vertex", "a": 1, "h": 0, "k": -4, "interactive": True, "min": -8, "max": 8},
            },
            {
                "kind": "worked",
                "title": "Four discriminants, four verdicts",
                "problemId": "im2-u4-l3-we3",
            },
            tap(
                "Read the discriminant",
                "For $3x^{2} - 4x + 5 = 0$, what does the discriminant tell you?",
                [
                    "two distinct real roots",
                    "one repeated real root",
                    "no real roots",
                    "the roots are rational",
                ],
                2,
                "$D = 16 - 4(3)(5) = 16 - 60 = -44 < 0$. No real roots — the parabola opens "
                "upward and its minimum sits above the horizontal axis.",
                [
                    "Eq((-4)**2 - 4*3*5, -44)",
                    "3*1**2 - 4*1 + 5 > 0",
                    "3*0**2 - 4*0 + 5 > 0",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Choosing",
                "title": "Four methods, ranked by speed",
                "body": (
                    "No middle term: take roots. Factors jump out: factor. Vertex wanted as well: "
                    "complete the square. None of the above: formula. The formula always works, "
                    "which is not the same as always being the right choice."
                ),
            },
            {
                "kind": "worked",
                "title": "A projectile, with two answers that both mean something",
                "problemId": "im2-u4-l3-we4",
            },
            {"kind": "tryIt", "title": "An irrational pair", "problemId": "im2-u4-l3-t1"},
            {"kind": "tryIt", "title": "Discriminants only", "problemId": "im2-u4-l3-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "$x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$ — completing the square, saved",
                    "$D > 0$ two real roots, $D = 0$ one, $D < 0$ none real",
                    "$D$ a perfect square means rational roots, so factoring will succeed",
                    "Write $a$, $b$, $c$ with signs before substituting",
                    "The whole numerator is divided by $2a$, not just the radical",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 4 — N-CN.1/2/7: complex numbers
# ===========================================================================
def lesson_complex_numbers():
    return lesson(
        slug="complex-numbers",
        title="Complex Numbers: When the Discriminant Is Negative",
        concrete=(
            "Every time mathematics has run out of numbers, it has invented more. Subtraction "
            "forced negatives; division forced fractions; the diagonal of a square forced "
            "irrationals. Now $x^{2} = -1$ forces one more, and the pattern is exactly the same: "
            "the new numbers are defined by the property they were needed for, and everything "
            "already known keeps working."
        ),
        objective=(
            "Define $i$, write numbers in the form $a + bi$, add, subtract and multiply complex "
            "numbers, and solve quadratic equations with a negative discriminant."
        ),
        concept=[
            "**The definition.** $i$ is the number satisfying $i^{2} = -1$. That is the entire "
            "definition — everything else about complex numbers is a consequence of it plus the "
            "ordinary rules of algebra, exactly as everything about $\\sqrt{2}$ follows from "
            "$(\\sqrt{2})^{2} = 2$.",
            "**Square roots of negatives.** $\\sqrt{-25} = \\sqrt{25}\\sqrt{-1} = 5i$. In general "
            "$\\sqrt{-k} = i\\sqrt{k}$ for positive $k$. Write the $i$ FIRST when the radical "
            "remains — $i\\sqrt{7}$, not $\\sqrt{7}i$, which reads dangerously like $\\sqrt{7i}$.",
            "**Standard form has a real part and an imaginary part.** The real part is $a$, the imaginary part is $b$ (the "
            "coefficient, not $bi$). Real numbers are the case $b = 0$, so the complex numbers "
            "CONTAIN the reals rather than replacing them — nothing you knew has been discarded.",
            "**Adding and subtracting treats the unit like a variable.** "
            "$(3 + 4i) + (5 - 7i) = 8 - 3i$. Combine real with real and imaginary with imaginary, "
            "exactly as you combine like terms in a polynomial.",
            "**Multiplying means distributing, then applying the definition.** "
            "$(2 + 3i)(4 - i) = 8 - 2i + 12i - 3i^{2} = 8 + 10i + 3 = 11 + 10i$. The final step "
            "is the only place complex arithmetic differs from polynomial arithmetic, and it "
            "always simplifies rather than complicates.",
            "**Complex roots come in conjugate pairs.** If $a + bi$ solves a quadratic with real "
            "coefficients, so does $a - bi$. The $\\pm$ in the quadratic formula is what produces "
            "the pair, and it is why a negative discriminant gives two solutions, not zero.",
        ],
        key_idea=(
            "$i^{2} = -1$ is the only new fact; every negative discriminant then yields a "
            "conjugate pair $a \\pm bi$, so every quadratic has exactly two roots."
        ),
        facts=[
            fact(
                "The imaginary unit",
                "i^{2} = -1, \\qquad i = \\sqrt{-1}",
                "One definition; all complex arithmetic follows from it plus ordinary algebra.",
            ),
            fact(
                "Roots of negatives",
                "\\sqrt{-k} = i\\sqrt{k} \\quad (k > 0)",
                "Write the $i$ in front of the radical to avoid reading it as $\\sqrt{ki}$.",
            ),
            fact(
                "Standard form",
                "a + bi",
                "Real part $a$, imaginary part $b$. Real numbers are the case $b = 0$.",
            ),
            fact(
                "Conjugate pairs",
                "a + bi \\text{ is a root} \\iff a - bi \\text{ is a root}",
                "True whenever the coefficients are real — which the $\\pm$ in the formula guarantees.",
            ),
        ],
        worked=[
            problem(
                "im2-u4-l4-we1",
                "Simplify $\\sqrt{-49}$, $\\sqrt{-18}$ and $i^{2} + i^{4}$.",
                "**The first.** Split off the negative:"
                "$$\\sqrt{-49} = \\sqrt{49}\\sqrt{-1} = 7i.$$"
                "**The second, which also needs simplifying.**"
                "$$\\sqrt{-18} = \\sqrt{18}\\,i = 3\\sqrt{2}\\,i = 3i\\sqrt{2}.$$"
                "The $i$ is written before the radical so the expression cannot be misread as "
                "$3\\sqrt{2i}$."
                "**The third uses only the definition.** $i^{2} = -1$ by definition, and "
                "$i^{4} = (i^{2})^{2} = (-1)^{2} = 1$. So"
                "$$i^{2} + i^{4} = -1 + 1 = 0.$$"
                "**Check the first two by squaring back.** $(7i)^{2} = 49i^{2} = -49$ ✓ and "
                "$(3i\\sqrt{2})^{2} = 9 \\cdot 2 \\cdot i^{2} = -18$ ✓ Squaring is the natural "
                "check because a square root is defined by what it squares to."
                "**The pattern in the powers.** $i, -1, -i, 1$, then it repeats every four. Any "
                "power of $i$ is one of those four values, decided by the remainder on division by "
                "four.",
                [
                    "Eq((7*I)**2, -49)",
                    "Eq(simplify((3*I*sqrt(2))**2), -18)",
                    "Eq(I**2 + I**4, 0)",
                    "Eq(I**4, 1)",
                    "Eq(I**3, -I)",
                ],
            ),
            problem(
                "im2-u4-l4-we2",
                "Compute $(3 + 5i) + (2 - 8i)$, $(3 + 5i) - (2 - 8i)$, and $(3 + 5i)(2 - 8i)$.",
                "**The sum: combine like parts.**"
                "$$(3 + 2) + (5 - 8)i = 5 - 3i.$$"
                "**The difference: distribute the minus over both parts.**"
                "$$(3 - 2) + (5 - (-8))i = 1 + 13i.$$"
                "The imaginary part became $+13$ because subtracting $-8i$ adds $8i$ — the same "
                "sign discipline as subtracting polynomials."
                "**The product: distribute all four, then use the definition.**"
                "$$6 - 24i + 10i - 40i^{2}.$$"
                "**Apply the definition.** Replacing $i^{2}$ with $-1$, The last term becomes $-40(-1) = +40$:"
                "$$6 + 40 + (-24 + 10)i = 46 - 14i.$$"
                "**Where the real part came from.** The $40$ appeared in the REAL part even though "
                "it came from multiplying two imaginary terms. That migration is the whole "
                "character of complex multiplication — imaginary times imaginary is real."
                "**Check the product a second way.** Evaluating at the conjugate: "
                "$(3 - 5i)(2 + 8i) = 6 + 24i - 10i - 40i^{2} = 46 + 14i$ — the conjugate of the "
                "answer ✓ Conjugating both factors conjugates the product, which is a strong "
                "structural check.",
                [
                    "Eq((3 + 5*I) + (2 - 8*I), 5 - 3*I)",
                    "Eq((3 + 5*I) - (2 - 8*I), 1 + 13*I)",
                    "Eq(expand((3 + 5*I)*(2 - 8*I)), 46 - 14*I)",
                    "Eq(expand((3 - 5*I)*(2 + 8*I)), 46 + 14*I)",
                    "Eq(-40*I**2, 40)",
                ],
            ),
            problem(
                "im2-u4-l4-we3",
                "Solve $x^{2} + 4x + 13 = 0$.",
                "**Check the discriminant first.**"
                "$$D = 16 - 52 = -36.$$"
                "Negative, so there are no real roots — but there are two complex ones, and the "
                "formula produces them without any change of method."
                "**Apply the quadratic formula.**"
                "$$x = \\frac{-4 \\pm \\sqrt{-36}}{2}.$$"
                "**Convert the negative root.** $\\sqrt{-36} = 6i$:"
                "$$x = \\frac{-4 \\pm 6i}{2}.$$"
                "**Divide BOTH terms by 2.** This is the step most often botched — the $2$ divides "
                "the whole numerator:"
                "$$x = -2 \\pm 3i.$$"
                "**Check by substituting the first root.** First "
                "$(-2 + 3i)^{2} = 4 - 12i + 9i^{2} = 4 - 12i - 9 = -5 - 12i$. Then "
                "$4x = -8 + 12i$. Adding: $-5 - 12i - 8 + 12i + 13 = 0$ ✓ The imaginary parts "
                "cancelled exactly, which is what a genuine root does."
                "**Note the conjugate pair.** The two roots are $-2 + 3i$ and $-2 - 3i$ — same "
                "real part, opposite imaginary parts. Their sum is $-4 = -\\frac{b}{a}$ ✓ and "
                "their product is $4 + 9 = 13 = \\frac{c}{a}$ ✓ The sum-and-product check works "
                "for complex roots exactly as it does for real ones.",
                [
                    "Eq(4**2 - 4*1*13, -36)",
                    "Eq(expand((-2 + 3*I)**2 + 4*(-2 + 3*I) + 13), 0)",
                    "Eq(expand((-2 - 3*I)**2 + 4*(-2 - 3*I) + 13), 0)",
                    "Eq((-2 + 3*I) + (-2 - 3*I), -4)",
                    "Eq(expand((-2 + 3*I)*(-2 - 3*I)), 13)",
                ],
            ),
            problem(
                "im2-u4-l4-we4",
                "Solve $2x^{2} - 4x + 5 = 0$, and explain what the answer means about the graph "
                "of $y = 2x^{2} - 4x + 5$.",
                "**Discriminant.**"
                "$$D = 16 - 4(2)(5) = 16 - 40 = -24.$$"
                "Negative — expect a conjugate pair."
                "**Formula.**"
                "$$x = \\frac{4 \\pm \\sqrt{-24}}{4}.$$"
                "**Simplify the radical.** $\\sqrt{-24} = i\\sqrt{24} = 2i\\sqrt{6}$:"
                "$$x = \\frac{4 \\pm 2i\\sqrt{6}}{4} = 1 \\pm \\frac{i\\sqrt{6}}{2}.$$"
                "Both terms of the numerator were divided by $4$."
                "**What it means for the graph.** No real roots means the parabola never touches "
                "the horizontal axis. Since $a = 2 > 0$ it opens upward, so it sits entirely "
                "ABOVE the axis."
                "**Confirm with the vertex.** Completing the square: "
                "$2(x^{2} - 2x) + 5 = 2(x - 1)^{2} - 2 + 5 = 2(x - 1)^{2} + 3$. The minimum value "
                "is $3$, which is positive ✓ A curve whose lowest point is $3$ units above the "
                "axis obviously cannot cross it."
                "**The two facts are the same fact.** A negative discriminant and a vertex on the "
                "wrong side of the axis are two descriptions of one situation — which is why the "
                "discriminant can be trusted without drawing anything.",
                [
                    "Eq((-4)**2 - 4*2*5, -24)",
                    "Eq(simplify(sqrt(24)), 2*sqrt(6))",
                    "Eq(expand(2*(1 + I*sqrt(6)/2)**2 - 4*(1 + I*sqrt(6)/2) + 5), 0)",
                    "Eq(expand(2*(1 - I*sqrt(6)/2)**2 - 4*(1 - I*sqrt(6)/2) + 5), 0)",
                    "Eq(2*(1 - 1)**2 + 3, 3)",
                    "Eq(2*1**2 - 4*1 + 5, 3)",
                    "2*0**2 - 4*0 + 5 > 0",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Writing $\\sqrt{-9} \\cdot \\sqrt{-4} = \\sqrt{36} = 6$.",
                "The product rule for radicals fails for negatives. Convert first: "
                "$(3i)(2i) = 6i^2 = -6$. Always turn $\\sqrt{-k}$ into $i\\sqrt{k}$ before "
                "multiplying.",
            ),
            mistake(
                "Dividing only one term of the numerator by $2a$.",
                "$\\frac{-4 \\pm 6i}{2}$ is $-2 \\pm 3i$, not $-4 \\pm 3i$. Both terms are "
                "divided — the same error as with real roots, and just as fatal.",
            ),
            mistake(
                "Leaving $i^{2}$ in an answer.",
                "$i^2$ is $-1$; a simplified complex number contains no $i^2$. Replace it and "
                "combine into the real part.",
            ),
            mistake(
                "Saying a negative discriminant means 'no solutions'.",
                "It means no REAL solutions. There are exactly two complex ones, and they are a "
                "conjugate pair — which is why every quadratic has exactly two roots.",
            ),
        ],
        try_it=[
            problem(
                "im2-u4-l4-t1",
                "Simplify $(4 - 3i)(1 + 2i)$.",
                "Distribute: $4 + 8i - 3i - 6i^{2}$. Replace $i^{2} = -1$: the last term becomes "
                "$+6$. Combine: $(4 + 6) + (8 - 3)i = 10 + 5i$. Check by conjugating both "
                "factors: $(4 + 3i)(1 - 2i) = 4 - 8i + 3i + 6 = 10 - 5i$, the conjugate of the "
                "answer ✓",
                [
                    "Eq(expand((4 - 3*I)*(1 + 2*I)), 10 + 5*I)",
                    "Eq(expand((4 + 3*I)*(1 - 2*I)), 10 - 5*I)",
                    "Eq(-6*I**2, 6)",
                ],
            ),
            problem(
                "im2-u4-l4-t2",
                "Solve $x^{2} - 6x + 25 = 0$.",
                "$D = 36 - 100 = -64$, so complex roots. $x = \\frac{6 \\pm \\sqrt{-64}}{2} = "
                "\\frac{6 \\pm 8i}{2} = 3 \\pm 4i$. Check via sum and product: the roots sum to "
                "$6 = -\\frac{b}{a}$ ✓ and multiply to $9 + 16 = 25 = \\frac{c}{a}$ ✓",
                [
                    "Eq((-6)**2 - 4*1*25, -64)",
                    "Eq(expand((3 + 4*I)**2 - 6*(3 + 4*I) + 25), 0)",
                    "Eq(expand((3 - 4*I)**2 - 6*(3 - 4*I) + 25), 0)",
                    "Eq(expand((3 + 4*I)*(3 - 4*I)), 25)",
                    "Eq((3 + 4*I) + (3 - 4*I), 6)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "N-CN.1",
                "title": "Mathematics has done this before",
                "body": (
                    "Subtraction demanded negatives. Division demanded fractions. The diagonal of "
                    "a unit square demanded irrationals. Each time the answer was the same: define "
                    "the new number by the property it was needed for, and check the old rules "
                    "survive."
                ),
                "beats": [
                    "$3 - 5$ demanded negatives",
                    "$3 \\div 2$ demanded fractions",
                    "$x^{2} = 2$ demanded irrationals",
                    "$x^{2} = -1$ demands $i$",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "The whole definition",
                "title": "One new fact, and only one",
                "body": (
                    "$i^{2} = -1$. Everything else about complex numbers — how they add, multiply, "
                    "and solve equations — follows from that plus the algebra you already have. "
                    "No new rules are being introduced."
                ),
            },
            {
                "kind": "worked",
                "title": "Roots of negatives, and powers of $i$",
                "problemId": "im2-u4-l4-we1",
            },
            tap(
                "Simplify the root",
                "What is $\\sqrt{-45}$ in simplest form?",
                ["$45i$", "$3i\\sqrt{5}$", "$5i\\sqrt{3}$", "$-3\\sqrt{5}$"],
                1,
                "$\\sqrt{-45} = i\\sqrt{45} = i\\sqrt{9 \\cdot 5} = 3i\\sqrt{5}$. Check by "
                "squaring: $(3i\\sqrt{5})^{2} = 9 \\cdot 5 \\cdot i^{2} = -45$ ✓",
                [
                    "Eq(simplify((3*I*sqrt(5))**2), -45)",
                    "Eq(simplify(sqrt(45)), 3*sqrt(5))",
                ],
            ),
            {
                "kind": "tip",
                "eyebrow": "Notation",
                "title": "Put the $i$ in front of the radical",
                "body": (
                    "Write $3i\\sqrt{5}$, never $3\\sqrt{5}i$ — the second is one careless glance "
                    "away from being read as $3\\sqrt{5i}$, which means something else entirely."
                ),
            },
            {
                "kind": "worked",
                "title": "Adding, subtracting and multiplying",
                "problemId": "im2-u4-l4-we2",
            },
            tap(
                "Multiply carefully",
                "What is $(1 + i)^{2}$?",
                ["$2$", "$2i$", "$1 + i^{2}$", "$0$"],
                1,
                "$(1 + i)(1 + i) = 1 + 2i + i^{2} = 1 + 2i - 1 = 2i$. The real parts cancelled "
                "exactly — squaring a complex number does not generally give a real answer.",
                [
                    "Eq(expand((1 + I)**2), 2*I)",
                    "Eq(I**2, -1)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "N-CN.7",
                "title": "The negative discriminant, resolved",
                "body": (
                    "Nothing about the quadratic formula changes. $\\sqrt{-36}$ simply becomes "
                    "$6i$ and the two branches of the $\\pm$ become a conjugate pair. Every "
                    "quadratic has exactly two roots — the real ones were only ever a special "
                    "case."
                ),
            },
            {
                "kind": "worked",
                "title": "A quadratic with complex roots",
                "problemId": "im2-u4-l4-we3",
            },
            {
                "kind": "parabolaGraph",
                "eyebrow": "What complex roots look like",
                "title": "A parabola that misses the axis",
                "teach": (
                    "Lift the curve until it clears the horizontal axis entirely. The equation "
                    "still has two roots — they have simply moved off the real line. The graph "
                    "shows you the real solutions only, which is a limitation of the picture, not "
                    "of the algebra."
                ),
                "config": {"mode": "vertex", "a": 1, "h": 1, "k": 3, "interactive": True, "min": -6, "max": 8},
            },
            {
                "kind": "worked",
                "title": "Complex roots and the graph, reconciled",
                "problemId": "im2-u4-l4-we4",
            },
            {"kind": "tryIt", "title": "A complex product", "problemId": "im2-u4-l4-t1"},
            {"kind": "tryIt", "title": "Solving with a negative discriminant", "problemId": "im2-u4-l4-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "$i^{2} = -1$ is the only new fact; the rest is ordinary algebra",
                    "$\\sqrt{-k} = i\\sqrt{k}$ — convert before multiplying, never after",
                    "Standard form $a + bi$; real numbers are the case $b = 0$",
                    "Multiply by distributing, then replace $i^{2}$ with $-1$",
                    "A negative discriminant gives a conjugate pair, so every quadratic has two roots",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 5 — A-REI.7: systems of a linear and a quadratic equation
# ===========================================================================

def lesson_linear_quadratic_systems():
    return lesson(
        slug="linear-and-quadratic-systems",
        title="Where a Line Meets a Parabola",
        concrete=(
            "A ball is thrown and follows a parabola; a drone flies across the field in a "
            "straight line at a steady climb. Do they collide? The question is not about "
            "either path on its own — it is about the points that lie on BOTH, and there "
            "can be two of them, one, or none. Solving the system tells you which, and the "
            "discriminant tells you before you finish."
        ),
        objective=(
            "Solve a system of one linear and one quadratic equation algebraically by "
            "substitution, interpret the solutions as intersection points, and use the "
            "discriminant to count them in advance — including the tangent case."
        ),
        concept=[
            "**A solution of a system is a point on every curve at once.** IM1's systems "
            "were two lines, so there was at most one crossing. Replace one line with a "
            "parabola and the count can be $2$, $1$ or $0$ — a straight line can cut a "
            "curve twice, graze it once, or miss it entirely.",

            "**Substitution is the whole method.** The linear equation gives $y$ in terms "
            "of $x$ with no work; put that expression wherever $y$ appears in the quadratic "
            "and you are left with one quadratic equation in $x$ alone. Every technique "
            "from this unit then applies — factoring, the square root, completing the "
            "square, the formula.",

            "**Do not stop at the x values.** Each $x$ you find is only half of a point. Substitute "
            "it back into the LINEAR equation (it is the easier of the two) to recover the "
            "matching $y$, and report ordered pairs. A pair of $x$ values with no $y$ values "
            "is an unfinished answer.",

            "**The discriminant counts the intersections.** After substituting you have "
            "$ax^2 + bx + c = 0$, and $b^2 - 4ac$ decides everything: positive means two "
            "crossings, zero means the line is TANGENT — touching at exactly one point — "
            "and negative means the line and curve never meet in the real plane. This is "
            "the same discriminant as before, now answering a geometric question.",

            "**Tangency is a condition you can solve for.** 'Find the value of $k$ for "
            "which $y = x + k$ touches the parabola' means 'find $k$ making the "
            "discriminant zero'. Set $b^2 - 4ac = 0$ and solve for $k$ — a favourite exam "
            "move, because it looks geometric and turns out to be algebra you already have.",

            "**Two curves work the same way.** A line and a circle, a parabola and a "
            "circle: substitute one equation into the other, reduce to a single-variable "
            "equation, and let the discriminant count. Nothing about the method needed the "
            "second curve to be a parabola.",
        ],
        key_idea=(
            "Substitute the line into the curve to get one quadratic in $x$, then let the "
            "discriminant count the intersections: positive two, zero tangent, negative "
            "none. Finish by putting each $x$ back into the LINE to get its $y$."
        ),
        facts=[
            fact("The method", "y = mx + c \\rightarrow \\text{substitute into the quadratic}",
                 "One equation in x alone, solvable by every method in this unit."),
            fact("Counting the crossings", "b^2 - 4ac > 0 \\Rightarrow \\text{two points}",
                 "Zero gives a tangent, negative gives no real intersection."),
            fact("The tangency condition", "b^2 - 4ac = 0",
                 "Set this and solve for the unknown parameter."),
            fact("Finishing the answer", "(x_1, y_1) \\text{ and } (x_2, y_2)",
                 "Each x must be paired with its y — solutions are POINTS."),
        ],
        worked=[
            problem(
                "im2-u4-l5-we1",
                "Solve the system $y = x^2 - 2x - 3$ and $y = x + 1$.",
                "**Substitute the line into the curve.** Both right-hand sides equal $y$, "
                "so set them equal: $x^2 - 2x - 3 = x + 1$."
                "**Collect on one side.** $x^2 - 3x - 4 = 0$."
                "**Factor.** $(x - 4)(x + 1) = 0$, so $x = 4$ or $x = -1$."
                "**Recover each y from the LINE.** At $x = 4$: $y = 5$. At "
                "$x = -1$: $y = 0$."
                "**Answer.** The curves meet at $(4, 5)$ and $(-1, 0)$.",
                [
                    "Eq(expand((x - 4)*(x + 1)), x**2 - 3*x - 4)",
                    "Eq(4**2 - 2*4 - 3, 4 + 1)",
                    "Eq((-1)**2 - 2*(-1) - 3, -1 + 1)",
                ],
            ),
            problem(
                "im2-u4-l5-we2",
                "Show that the line $y = 2x - 5$ is tangent to the parabola $y = x^2 - 4$, "
                "and find the point of contact.",
                "**Substitute.** $x^2 - 4 = 2x - 5$, so $x^2 - 2x + 1 = 0$."
                "**Compute the discriminant.** $b^2 - 4ac = (-2)^2 - 4(1)(1) = 4 - 4 = 0$. "
                "A zero discriminant means exactly one solution, which geometrically is a "
                "single point of contact — the line is tangent."
                "**Find it.** $x^2 - 2x + 1 = (x - 1)^2 = 0$ gives $x = 1$, and the line "
                "gives $y = 2(1) - 5 = -3$."
                "**Point of contact.** $(1, -3)$.",
                [
                    "Eq((-2)**2 - 4*1*1, 0)",
                    "Eq(expand((x - 1)**2), x**2 - 2*x + 1)",
                    "Eq(1**2 - 4, 2*1 - 5)",
                ],
            ),
            problem(
                "im2-u4-l5-we3",
                "For which value of $k$ is the line $y = 4x + k$ tangent to the parabola "
                "$y = x^2 + 2x + 7$?",
                "**Substitute and collect.** $x^2 + 2x + 7 = 4x + k$ gives "
                "$x^2 - 2x + (7 - k) = 0$."
                "**Tangency means one solution, so the discriminant is zero.** "
                "$(-2)^2 - 4(1)(7 - k) = 0$."
                "**Solve for the constant.** $4 - 28 + 4k = 0$, so $4k = 24$ and $k = 6$."
                "**Check.** With $k = 6$ the equation is $x^2 - 2x + 1 = 0$, a perfect "
                "square with the single root $x = 1$ — one contact point, as required.",
                [
                    "Eq(4 - 4*(7 - 6), 0)",
                    "Eq(expand(x**2 + 2*x + 7 - (4*x + 6)), x**2 - 2*x + 1)",
                    "Eq(1**2 + 2*1 + 7, 4*1 + 6)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reporting the x values and stopping.",
                "A system's solutions are POINTS. x = 4 and x = -1 is half an answer; the "
                "points are (4, 5) and (-1, 0). Substitute each x back into the line.",
            ),
            mistake(
                "Substituting back into the quadratic instead of the line.",
                "It gives the same y, but with far more arithmetic and far more chances to "
                "slip. The line was chosen as the substitution source for a reason — use it "
                "again at the end.",
            ),
            mistake(
                "Treating a zero discriminant as 'no solution'.",
                "Zero means exactly ONE solution — the tangent case, where the line touches "
                "the curve at a single point. Negative is the no-intersection case.",
            ),
            mistake(
                "Solving the tangency condition by trial and error.",
                "'Tangent' translates directly into b² - 4ac = 0. Set that equation up in "
                "the unknown parameter and solve it — guessing values of k is slow and "
                "rarely lands on the exact answer.",
            ),
        ],
        try_it=[
            problem(
                "im2-u4-l5-t1",
                "Solve the system $y = x^2 + 3x - 2$ and $y = 2x + 4$.",
                "$x^2 + 3x - 2 = 2x + 4$ gives $x^2 + x - 6 = 0$, so $(x + 3)(x - 2) = 0$ "
                "and $x = -3$ or $x = 2$. From the line, $y = -2$ and $y = 8$. The points "
                "are $(-3, -2)$ and $(2, 8)$.",
                [
                    "Eq(expand((x + 3)*(x - 2)), x**2 + x - 6)",
                    "Eq((-3)**2 + 3*(-3) - 2, 2*(-3) + 4)",
                    "Eq(2**2 + 3*2 - 2, 2*2 + 4)",
                ],
            ),
            problem(
                "im2-u4-l5-t2",
                "How many points does the line $y = x - 5$ share with the parabola "
                "$y = x^2 + 1$?",
                "$x^2 + 1 = x - 5$ gives $x^2 - x + 6 = 0$, whose discriminant is "
                "$1 - 24 = -23$. Negative, so there are NO real intersection points — the "
                "line passes entirely below the parabola.",
                [
                    "Eq(1 - 4*1*6, -23)",
                    "-23 < 0",
                ],
            ),
            problem(
                "im2-u4-l5-t3",
                "For which value of $k$ is $y = 6x + k$ tangent to $y = x^2 + 10x + 3$?",
                "$x^2 + 10x + 3 = 6x + k$ gives $x^2 + 4x + (3 - k) = 0$. Tangency needs "
                "$16 - 4(3 - k) = 0$, so $16 - 12 + 4k = 0$ and $k = -1$.",
                [
                    "Eq(16 - 4*(3 - (-1)), 0)",
                    "Eq(expand(x**2 + 10*x + 3 - (6*x - 1)), x**2 + 4*x + 4)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "Two lines could cross once. A line and a curve cannot be trusted to.",
             "body": "A system asks for the points lying on BOTH graphs. With two lines there was one crossing at most. Swap one for a parabola and a straight line can cut it twice, touch it once, or miss it — so the first question is no longer 'where' but 'how many'.",
             "beats": ["A solution is a point on both graphs", "Two, one or none", "The count comes before the coordinates"]},
            {"kind": "teach", "title": "Substitute, then it is just a quadratic",
             "body": "The linear equation already gives $y$ in terms of $x$. Put that expression into the quadratic and every $y$ disappears, leaving one quadratic equation in $x$ — solvable by factoring, square roots, completing the square, or the formula. Nothing new is needed.",
             "beats": ["Replace $y$ using the line", "One equation, one variable", "Every method from this unit applies"]},
            {"kind": "worked", "title": "Two crossings", "problemId": "im2-u4-l5-we1"},
            tap(
                "Finishing the answer",
                "You have solved down to $x = 4$ and $x = -1$. The system's solution is:",
                ["the points $(4, 5)$ and $(-1, 0)$, after substituting each $x$ into the line",
                 "$x = 4$ and $x = -1$",
                 "$y = 5$ and $y = 0$",
                 "$x = 4$ only, because a system has one solution"],
                0,
                "A system of two equations in $x$ and $y$ is solved by POINTS. Each $x$ must "
                "be paired with the $y$ that goes with it.",
                ["Eq(4**2 - 2*4 - 3, 5)", "Eq((-1)**2 - 2*(-1) - 3, 0)"],
            ),
            {"kind": "tip", "eyebrow": "Save yourself work",
             "title": "Go back to the line, not the curve",
             "body": "Both equations give the same $y$, but the line is one multiplication and one addition while the parabola is a squaring as well. Substituting into the line is faster and safer — and it is the equation you already trusted enough to substitute FROM."},
            {"kind": "worked", "title": "The tangent case", "problemId": "im2-u4-l5-we2"},
            tap(
                "What a zero discriminant means here",
                "After substituting, the quadratic has discriminant $0$. Geometrically:",
                ["the line is tangent — it touches the curve at exactly one point",
                 "the line misses the curve entirely",
                 "the line cuts the curve twice",
                 "the line lies along the curve"],
                0,
                "Zero discriminant means one repeated root, so one shared point: the line "
                "grazes the parabola rather than cutting it.",
                ["Eq((-2)**2 - 4*1*1, 0)", "Eq(expand((x - 1)**2), x**2 - 2*x + 1)"],
            ),
            {"kind": "worked", "title": "Solving for the tangency condition", "problemId": "im2-u4-l5-we3"},
            {"kind": "tryIt", "title": "Two points", "problemId": "im2-u4-l5-t1"},
            {"kind": "tryIt", "title": "Counting without solving", "problemId": "im2-u4-l5-t2"},
            {"kind": "tryIt", "title": "Find the tangent line", "problemId": "im2-u4-l5-t3"},
            {"kind": "funFact", "title": "This is how tangents were found before calculus",
             "body": "Descartes located tangents to curves by demanding a repeated root — exactly the discriminant-equals-zero move above — decades before derivatives existed. Calculus later made it general, but for a line meeting a parabola the algebraic route is still the shorter one."},
            {"kind": "recap", "title": "What to carry forward",
             "points": ["Substitute the line into the curve to get one quadratic in $x$",
                        "$b^2 - 4ac$ counts the intersections: $+$ two, $0$ tangent, $-$ none",
                        "Put each $x$ back into the LINE to get its $y$",
                        "Solutions are POINTS, written as ordered pairs",
                        "'Tangent' translates to $b^2 - 4ac = 0$ — solve it for the parameter"]},
        ],
    )


# ===========================================================================
# Practice and test banks
# ===========================================================================
def practice_bank():
    return [
        problem(
            "im2-u4-p1",
            "Solve $x^{2} + 2x - 35 = 0$ by factoring.",
            "Product $-35$, sum $2$: the pair is $7$ and $-5$. So $(x + 7)(x - 5) = 0$ and "
            "$x = -7$ or $x = 5$. Check: $49 - 14 - 35 = 0$ ✓ and $25 + 10 - 35 = 0$ ✓",
            [
                "Eq(7*(-5), -35)",
                "Eq(7 + (-5), 2)",
                "Eq((-7)**2 + 2*(-7) - 35, 0)",
                "Eq(5**2 + 2*5 - 35, 0)",
            ],
        ),
        problem(
            "im2-u4-p2",
            "Solve $5x^{2} = 20x$.",
            "Do not divide by $x$. Rearrange and factor: $5x^{2} - 20x = 0$, so $5x(x - 4) = 0$ "
            "and $x = 0$ or $x = 4$. Check: $0 = 0$ ✓ and $80 = 80$ ✓ Dividing by $x$ would have "
            "lost the root $x = 0$ entirely.",
            [
                "Eq(5*0**2, 20*0)",
                "Eq(5*4**2, 20*4)",
                "Eq(5*0*(0 - 4), 0)",
            ],
        ),
        problem(
            "im2-u4-p3",
            "Solve $(x + 5)^{2} = 49$.",
            "Take roots with both signs: $x + 5 = \\pm 7$. So $x = 2$ or $x = -12$. Check: "
            "$(2 + 5)^{2} = 49$ ✓ and $(-12 + 5)^{2} = (-7)^{2} = 49$ ✓ The roots are each $7$ "
            "units from $x = -5$.",
            [
                "Eq((2 + 5)**2, 49)",
                "Eq((-12 + 5)**2, 49)",
                "Eq((2 + (-12))/2, -5)",
            ],
        ),
        problem(
            "im2-u4-p4",
            "Solve $x^{2} - 4x - 12 = 0$ by completing the square.",
            "Move the constant: $x^{2} - 4x = 12$. Half of $-4$ is $-2$, squared is $4$; add to "
            "both sides: $(x - 2)^{2} = 16$. Roots: $x - 2 = \\pm 4$, so $x = 6$ or $x = -2$. "
            "Check: $36 - 24 - 12 = 0$ ✓ and $4 + 8 - 12 = 0$ ✓",
            [
                "Eq(((-4)/2)**2, 4)",
                "Eq(6**2 - 4*6 - 12, 0)",
                "Eq((-2)**2 - 4*(-2) - 12, 0)",
                "Eq((6 - 2)**2, 16)",
            ],
        ),
        problem(
            "im2-u4-p5",
            "Write $y = x^{2} - 12x + 20$ in vertex form and state the minimum.",
            "Half of $-12$ is $-6$, squared is $36$. Add and subtract: "
            "$y = (x^{2} - 12x + 36) + 20 - 36 = (x - 6)^{2} - 16$. Vertex $(6, -16)$; since "
            "$a = 1 > 0$ the minimum value is $-16$ at $x = 6$. Check at $x = 0$: standard gives "
            "$20$, and $36 - 16 = 20$ ✓",
            [
                "Eq((0 - 6)**2 - 16, 20)",
                "Eq((6 - 6)**2 - 16, -16)",
                "Eq(6**2 - 12*6 + 20, -16)",
                "Eq((2 - 6)**2 - 16, 2**2 - 12*2 + 20)",
            ],
        ),
        problem(
            "im2-u4-p6",
            "Solve $3x^{2} - 5x - 2 = 0$ with the quadratic formula.",
            "$a = 3$, $b = -5$, $c = -2$. $D = 25 + 24 = 49$, a perfect square, so the roots are "
            "rational. $x = \\frac{5 \\pm 7}{6}$, giving $x = 2$ and $x = -\\frac{1}{3}$. Check: "
            "$12 - 10 - 2 = 0$ ✓ and $\\frac{1}{3} + \\frac{5}{3} - 2 = 0$ ✓",
            [
                "Eq((-5)**2 - 4*3*(-2), 49)",
                "Eq((5 + 7)/6, 2)",
                "Eq((5 - 7)/6, Rational(-1,3))",
                "Eq(3*2**2 - 5*2 - 2, 0)",
                "Eq(3*Rational(-1,3)**2 - 5*Rational(-1,3) - 2, 0)",
            ],
        ),
        problem(
            "im2-u4-p7",
            "Without solving, state the number and type of roots of $4x^{2} - 4x + 1 = 0$ and "
            "$x^{2} - 3x - 7 = 0$.",
            "First: $D = 16 - 16 = 0$, so one repeated rational root ($x = \\frac{1}{2}$, since "
            "$4x^{2} - 4x + 1 = (2x - 1)^{2}$). Second: $D = 9 + 28 = 37$, positive but not a "
            "perfect square, so two irrational real roots — and no integer factorisation exists.",
            [
                "Eq((-4)**2 - 4*4*1, 0)",
                "Eq(4*Rational(1,2)**2 - 4*Rational(1,2) + 1, 0)",
                "Eq((-3)**2 - 4*1*(-7), 37)",
                "37 > 36",
                "37 < 49",
            ],
        ),
        problem(
            "im2-u4-p8",
            "Solve $x^{2} - 2x + 10 = 0$.",
            "$D = 4 - 40 = -36 < 0$, so the roots are complex. "
            "$x = \\frac{2 \\pm \\sqrt{-36}}{2} = \\frac{2 \\pm 6i}{2} = 1 \\pm 3i$. Check via "
            "sum and product: sum $2 = -\\frac{b}{a}$ ✓ and product $1 + 9 = 10 = "
            "\\frac{c}{a}$ ✓",
            [
                "Eq((-2)**2 - 4*1*10, -36)",
                "Eq(expand((1 + 3*I)**2 - 2*(1 + 3*I) + 10), 0)",
                "Eq(expand((1 - 3*I)**2 - 2*(1 - 3*I) + 10), 0)",
                "Eq(expand((1 + 3*I)*(1 - 3*I)), 10)",
            ],
        ),
        problem(
            "im2-u4-p9",
            "Simplify $\\sqrt{-64}$, $\\sqrt{-50}$ and $i^{6}$.",
            "$\\sqrt{-64} = 8i$. $\\sqrt{-50} = i\\sqrt{50} = 5i\\sqrt{2}$. For the power: "
            "$i^{6} = (i^{2})^{3} = (-1)^{3} = -1$. Check the first two by squaring: "
            "$(8i)^{2} = -64$ ✓ and $(5i\\sqrt{2})^{2} = 25 \\cdot 2 \\cdot (-1) = -50$ ✓",
            [
                "Eq((8*I)**2, -64)",
                "Eq(simplify((5*I*sqrt(2))**2), -50)",
                "Eq(I**6, -1)",
                "Eq(simplify(sqrt(50)), 5*sqrt(2))",
            ],
        ),
        problem(
            "im2-u4-p10",
            "Compute $(5 - 2i)(3 + 4i)$.",
            "Distribute: $15 + 20i - 6i - 8i^{2}$. Replace $i^{2} = -1$: the last term is $+8$. "
            "Combine: $(15 + 8) + (20 - 6)i = 23 + 14i$. Check by conjugating both factors: "
            "$(5 + 2i)(3 - 4i) = 23 - 14i$ ✓",
            [
                "Eq(expand((5 - 2*I)*(3 + 4*I)), 23 + 14*I)",
                "Eq(expand((5 + 2*I)*(3 - 4*I)), 23 - 14*I)",
                "Eq(-8*I**2, 8)",
            ],
        ),
        problem(
            "im2-u4-p11",
            "A rectangle has area $77$ square metres and its length is $4$ metres more than its "
            "width. Find the dimensions.",
            "Let the width be $x$. Then $x(x + 4) = 77$, so $x^{2} + 4x - 77 = 0$. Product $-77$, "
            "sum $4$: the pair is $11$ and $-7$, giving $(x + 11)(x - 7) = 0$ and $x = 7$ or "
            "$x = -11$. A width cannot be negative, so $x = 7$: the rectangle is $7$ m by $11$ m. "
            "Check: $7 \\times 11 = 77$ ✓ Rejecting the negative root is part of the answer, not "
            "an afterthought.",
            [
                "Eq(7*(7 + 4), 77)",
                "Eq(11*(-7), -77)",
                "Eq(11 + (-7), 4)",
                "Eq(7**2 + 4*7 - 77, 0)",
                "-11 < 0",
            ],
        ),
        problem(
            "im2-u4-p12",
            "For which values of $k$ does $x^{2} + kx + 9 = 0$ have exactly one real root?",
            "Exactly one real root means $D = 0$: $k^{2} - 36 = 0$, so $k^{2} = 36$ and "
            "$k = \\pm 6$. Both work: $k = 6$ gives $(x + 3)^{2} = 0$ with root $-3$, and "
            "$k = -6$ gives $(x - 3)^{2} = 0$ with root $3$. Check: $6^{2} - 36 = 0$ ✓ and "
            "$(-6)^{2} - 36 = 0$ ✓",
            [
                "Eq(6**2 - 4*1*9, 0)",
                "Eq((-6)**2 - 4*1*9, 0)",
                "Eq((-3)**2 + 6*(-3) + 9, 0)",
                "Eq(3**2 - 6*3 + 9, 0)",
            ],
        ),
    ]


def test_bank():
    return [
        problem(
            "im2-u4-ty-1",
            "Solve $2x^{2} + 5x - 12 = 0$ by factoring, and verify with the quadratic formula.",
            "**Factor with the ac-method.** $ac = 2 \\times (-12) = -24$, sum $5$. Opposite signs "
            "with the larger positive: $8$ and $-3$."
            "**Split and group.**"
            "$$2x^{2} + 8x - 3x - 12 = 2x(x + 4) - 3(x + 4) = (x + 4)(2x - 3) = 0.$$"
            "**Solve each factor.** $x = -4$ or $x = \\frac{3}{2}$."
            "**Verify with the formula.** $D = 25 - 4(2)(-12) = 25 + 96 = 121$, and "
            "$\\sqrt{121} = 11$:"
            "$$x = \\frac{-5 \\pm 11}{4},$$"
            "giving $\\frac{6}{4} = \\frac{3}{2}$ and $\\frac{-16}{4} = -4$ ✓ Same pair."
            "**A note on the discriminant.** $121$ is a perfect square, which is exactly why "
            "factoring succeeded. Had it not been, no integer split would have existed.",
            [
                "Eq(5**2 - 4*2*(-12), 121)",
                "Eq((-5 + 11)/4, Rational(3,2))",
                "Eq((-5 - 11)/4, -4)",
                "Eq(2*(-4)**2 + 5*(-4) - 12, 0)",
                "Eq(2*Rational(3,2)**2 + 5*Rational(3,2) - 12, 0)",
                "Eq(8*(-3), -24)",
            ],
        ),
        problem(
            "im2-u4-ty-2",
            "Solve $x^{2} - 6x + 2 = 0$ by completing the square, giving exact answers, and state "
            "the vertex of $y = x^{2} - 6x + 2$.",
            "**Move the constant.**"
            "$$x^{2} - 6x = -2.$$"
            "**Halve and square.** Half of $-6$ is $-3$; $(-3)^{2} = 9$. Add to both sides:"
            "$$x^{2} - 6x + 9 = 7.$$"
            "**Factor and take roots.**"
            "$$(x - 3)^{2} = 7 \\quad\\Longrightarrow\\quad x = 3 \\pm \\sqrt{7}.$$"
            "**State the vertex.** The working shows $x^{2} - 6x + 2 = (x - 3)^{2} - 7$, so the "
            "vertex is $(3, -7)$ — a minimum, since $a = 1 > 0$."
            "**Check the roots by sum and product.** They sum to $6 = -\\frac{b}{a}$ ✓ and "
            "multiply to $9 - 7 = 2 = \\frac{c}{a}$ ✓"
            "**Check the vertex form at a point.** At $x = 0$: standard gives $2$, and "
            "$9 - 7 = 2$ ✓",
            [
                "Eq(((-6)/2)**2, 9)",
                "Eq((3 + sqrt(7)) + (3 - sqrt(7)), 6)",
                "Eq(simplify((3 + sqrt(7))*(3 - sqrt(7))), 2)",
                "Eq(simplify((3 + sqrt(7))**2 - 6*(3 + sqrt(7)) + 2), 0)",
                "Eq((0 - 3)**2 - 7, 2)",
                "Eq((3 - 3)**2 - 7, -7)",
            ],
        ),
        problem(
            "im2-u4-ty-3",
            "For $x^{2} + 6x + c = 0$, find the values of $c$ for which the equation has (a) two "
            "distinct real roots, (b) exactly one real root, (c) no real roots.",
            "**Write the discriminant.**"
            "$$D = 36 - 4c.$$"
            "**Part (a) needs a positive discriminant.**"
            "$$36 - 4c > 0 \\quad\\Longrightarrow\\quad c < 9.$$"
            "**Part (b) needs a zero discriminant.**"
            "$$36 - 4c = 0 \\quad\\Longrightarrow\\quad c = 9,$$"
            "and indeed $x^{2} + 6x + 9 = (x + 3)^{2}$, with the double root $x = -3$."
            "**Part (c) needs a negative discriminant.**"
            "$$c > 9.$$"
            "**Test one value from each region.** At $c = 5$: $D = 16 > 0$, and the equation "
            "factors as $(x + 1)(x + 5) = 0$ — two roots ✓ At $c = 9$: the double root above ✓ At "
            "$c = 13$: $D = -16 < 0$, and the roots are $-3 \\pm 2i$ ✓"
            "**The geometric reading.** Raising $c$ lifts the whole parabola. At $c = 9$ its "
            "vertex just touches the axis; above that it clears it entirely.",
            [
                "Eq(36 - 4*5, 16)",
                "Eq(36 - 4*9, 0)",
                "Eq(36 - 4*13, -16)",
                "Eq((-1)**2 + 6*(-1) + 5, 0)",
                "Eq((-5)**2 + 6*(-5) + 5, 0)",
                "Eq((-3)**2 + 6*(-3) + 9, 0)",
                "Eq(expand((-3 + 2*I)**2 + 6*(-3 + 2*I) + 13), 0)",
            ],
        ),
        problem(
            "im2-u4-ty-4",
            "Solve $3x^{2} - 6x + 7 = 0$, express the roots in the form $a + bi$, and explain "
            "what the answer says about the graph.",
            "**Discriminant.**"
            "$$D = 36 - 4(3)(7) = 36 - 84 = -48.$$"
            "Negative, so the roots are a complex conjugate pair."
            "**Apply the formula.**"
            "$$x = \\frac{6 \\pm \\sqrt{-48}}{6}.$$"
            "**Simplify the radical.** $\\sqrt{-48} = i\\sqrt{48} = 4i\\sqrt{3}$:"
            "$$x = \\frac{6 \\pm 4i\\sqrt{3}}{6} = 1 \\pm \\frac{2i\\sqrt{3}}{3}.$$"
            "Both terms of the numerator were divided by $6$, and $\\frac{4}{6}$ reduced to "
            "$\\frac{2}{3}$."
            "**What it says about the graph.** No real roots means the parabola never meets the "
            "horizontal axis; with $a = 3 > 0$ it opens upward, so it lies entirely above."
            "**Confirm with the vertex.** $3(x^{2} - 2x) + 7 = 3(x - 1)^{2} - 3 + 7 = "
            "3(x - 1)^{2} + 4$, so the minimum value is $4 > 0$ ✓ A curve whose lowest point is "
            "$4$ cannot reach zero."
            "**Verify one root by substitution.** Expanding "
            "$3\\left(1 + \\frac{2i\\sqrt{3}}{3}\\right)^{2} - "
            "6\\left(1 + \\frac{2i\\sqrt{3}}{3}\\right) + 7$ gives $0$ ✓",
            [
                "Eq((-6)**2 - 4*3*7, -48)",
                "Eq(simplify(sqrt(48)), 4*sqrt(3))",
                "Eq(expand(3*(1 + 2*I*sqrt(3)/3)**2 - 6*(1 + 2*I*sqrt(3)/3) + 7), 0)",
                "Eq(expand(3*(1 - 2*I*sqrt(3)/3)**2 - 6*(1 - 2*I*sqrt(3)/3) + 7), 0)",
                "Eq(3*(1 - 1)**2 + 4, 4)",
                "Eq(3*1**2 - 6*1 + 7, 4)",
            ],
        ),
        problem(
            "im2-u4-ty-5",
            "Compute $(2 + 3i)^{2}$ and $(2 + 3i)(2 - 3i)$. Explain why the second is real.",
            "**The square.**"
            "$$(2 + 3i)(2 + 3i) = 4 + 6i + 6i + 9i^{2} = 4 + 12i - 9 = -5 + 12i.$$"
            "**The conjugate product.**"
            "$$(2 + 3i)(2 - 3i) = 4 - 6i + 6i - 9i^{2} = 4 + 9 = 13.$$"
            "**Why it had to be real.** The cross terms $-6i$ and $+6i$ cancel — the same "
            "cancellation as the difference of squares, $(a + b)(a - b) = a^{2} - b^{2}$. Here "
            "$a^{2} - b^{2}i^{2} = a^{2} + b^{2}$, which is a sum of two real squares and "
            "therefore always real and positive."
            "**The general statement.** $(a + bi)(a - bi) = a^{2} + b^{2}$ for every real $a$ and "
            "$b$. Multiplying by the conjugate is how you clear an imaginary part — the same trick "
            "as rationalising a denominator with a conjugate in Unit 1."
            "**Check with different numbers.** $(5 + i)(5 - i) = 25 + 1 = 26$ ✓ real, as "
            "predicted.",
            [
                "Eq(expand((2 + 3*I)**2), -5 + 12*I)",
                "Eq(expand((2 + 3*I)*(2 - 3*I)), 13)",
                "Eq(2**2 + 3**2, 13)",
                "Eq(expand((5 + I)*(5 - I)), 26)",
                "Eq(5**2 + 1**2, 26)",
            ],
        ),
        problem(
            "im2-u4-ty-6",
            "A rectangular garden is enclosed on three sides by $40$ metres of fencing, the "
            "fourth side being a wall. Find the two widths that give an area of $150$ square "
            "metres, and the width that maximises the area.",
            "**Set up.** Let the width (perpendicular to the wall) be $x$. Two widths and one "
            "length use the fence, so the length is $40 - 2x$ and"
            "$$A(x) = x(40 - 2x) = 40x - 2x^{2}.$$"
            "**Set the area to 150.**"
            "$$40x - 2x^{2} = 150 \\quad\\Longrightarrow\\quad 2x^{2} - 40x + 150 = 0 "
            "\\quad\\Longrightarrow\\quad x^{2} - 20x + 75 = 0.$$"
            "**Factor.** Product $75$, sum $-20$, both negative: $-5$ and $-15$:"
            "$$(x - 5)(x - 15) = 0.$$"
            "**Both answers are physically valid.** $x = 5$ gives a $5 \\times 30$ garden; "
            "$x = 15$ gives $15 \\times 10$. Both use exactly $40$ m of fence and both have area "
            "$150$ ✓ Neither can be discarded — the question genuinely has two answers."
            "**Find the maximising width.** The area function has $a = -2 < 0$, so its vertex is a "
            "maximum:"
            "$$x = -\\frac{40}{2(-2)} = 10, \\qquad A(10) = 10 \\times 20 = 200.$$"
            "**Sanity-check the relationship.** The two $150$-area widths, $5$ and $15$, are "
            "symmetric about $10$ ✓ — exactly as the parabola's symmetry requires, and the "
            "maximum $200$ exceeds both.",
            [
                "Eq(5*(40 - 2*5), 150)",
                "Eq(15*(40 - 2*15), 150)",
                "Eq(-40/(2*(-2)), 10)",
                "Eq(10*(40 - 2*10), 200)",
                "Eq((5 + 15)/2, 10)",
                "Eq((-5)*(-15), 75)",
                "Eq(-5 + (-15), -20)",
            ],
        ),
        problem(
            "im2-u4-ty-7",
            "Solve $x^{2} - 4x + k = 0$ for $k = 3$, $k = 4$ and $k = 8$, and describe how the "
            "roots change as $k$ increases.",
            "**The first value.** With $k = 3$: $D = 16 - 12 = 4 > 0$. Factoring: $(x - 1)(x - 3) = 0$, so $x = 1$ "
            "and $x = 3$ — two distinct real roots."
            "**The second value.** With $k = 4$: $D = 16 - 16 = 0$. The expression is $(x - 2)^{2}$, so $x = 2$ is a "
            "double root. The two roots have merged."
            "**The third value.** With $k = 8$: $D = 16 - 32 = -16 < 0$. The formula gives"
            "$$x = \\frac{4 \\pm 4i}{2} = 2 \\pm 2i,$$"
            "a complex conjugate pair."
            "**Describe the motion.** As $k$ rises, the parabola lifts. Its two crossings slide "
            "toward each other, meet at $k = 4$ where the vertex touches the axis, and then leave "
            "the real line together as a conjugate pair. Nothing is ever destroyed — there are "
            "always exactly two roots."
            "**Notice what stays fixed.** In all three cases the roots sum to "
            "$4 = -\\frac{b}{a}$: $1 + 3 = 4$, $2 + 2 = 4$, and $(2 + 2i) + (2 - 2i) = 4$ ✓ The "
            "vertex stays at $x = 2$ throughout, because $k$ never touches $b$."
            "**Verify the complex pair.** $(2 + 2i)^{2} = 8i$, and "
            "$8i - 4(2 + 2i) + 8 = 8i - 8 - 8i + 8 = 0$ ✓",
            [
                "Eq(16 - 4*1*3, 4)",
                "Eq(1**2 - 4*1 + 3, 0)",
                "Eq(3**2 - 4*3 + 3, 0)",
                "Eq(16 - 4*1*4, 0)",
                "Eq(2**2 - 4*2 + 4, 0)",
                "Eq(16 - 4*1*8, -16)",
                "Eq(expand((2 + 2*I)**2 - 4*(2 + 2*I) + 8), 0)",
                "Eq((2 + 2*I) + (2 - 2*I), 4)",
                "Eq(expand((2 + 2*I)**2), 8*I)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="solving-quadratic-equations",
        title="Solving Quadratic Equations",
        unit_number=4,
        blurb=(
            "Four methods and how to choose between them: factoring with the zero-product "
            "property, square roots, completing the square, and the quadratic formula derived "
            "from it. The discriminant predicts the answer before you compute it — and when it "
            "turns out negative, complex numbers supply the two roots the real line could not."
        ),
        builds_on=(
            "Factoring from Unit 2 and the shape of a parabola from Unit 3 — solving is finding "
            "where that parabola meets the axis."
        ),
        lessons=[
            lesson_factoring_and_roots(),
            lesson_completing_the_square(),
            lesson_quadratic_formula(),
            lesson_complex_numbers(),
            lesson_linear_quadratic_systems(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
