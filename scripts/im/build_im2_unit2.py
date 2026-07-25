#!/usr/bin/env python3
"""Integrated Mathematics 2 — Unit 2: Polynomials & Factoring.

CCSS Integrated Math II: A-APR.1 (polynomials form a system closed under
addition, subtraction and multiplication — the analogy with the integers is the
point, not an aside), A-SSE.2 (use the structure of an expression to identify
ways to rewrite it), A-SSE.3a (factor a quadratic to reveal its zeros).

The unit is deliberately built as a single arc: multiplication is taught first
and factoring second, because factoring is nothing but multiplication read
backwards. Every factoring technique in Lessons 3 and 4 is introduced by first
showing the multiplication that produced the pattern.

Run: python3 scripts/im/build_im2_unit2.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-2"


# ===========================================================================
# Lesson 1 — A-APR.1: the polynomial system, and why closure matters
# ===========================================================================
def lesson_polynomial_system():
    return lesson(
        slug="the-polynomial-system",
        title="Polynomials as a Number System",
        concrete=(
            "Add two whole numbers and you get a whole number. Multiply them and you get a whole "
            "number. Divide them and you might not. Polynomials behave exactly the same way — "
            "closed under addition, subtraction and multiplication, but not under division. That "
            "parallel is not a coincidence, and it is why almost everything you know about "
            "arithmetic transfers here unchanged."
        ),
        objective=(
            "Name the parts of a polynomial, state its degree, add and subtract polynomials, and "
            "explain what it means for the polynomials to be CLOSED under an operation."
        ),
        concept=[
            "**What counts as a polynomial.** A sum of terms, each of which is a number times a "
            "variable raised to a whole-number power. So $3x^{2} - 5x + 7$ qualifies. "
            "$\\frac{4}{x}$ does not, because $\\frac{4}{x} = 4x^{-1}$ and $-1$ is not a whole "
            "number. Neither does $\\sqrt{x} = x^{1/2}$. The exponent restriction is the whole "
            "definition.",
            "**Degree is the highest exponent.** In $5x^{3} - 2x + 9$ the degree is $3$. Degree "
            "controls almost everything downstream: how many solutions the equation can have, what "
            "the graph looks like at its extremes, and how the polynomial behaves when you divide "
            "by it. Degree $1$ is linear, degree $2$ is quadratic, degree $3$ is cubic.",
            "**Standard form orders the terms by descending degree.** $7 - 2x + 5x^{3}$ becomes "
            "$5x^{3} - 2x + 7$. The leading coefficient is the number on the highest-degree term "
            "($5$ here), and the constant term is the one with no variable ($7$). Writing in "
            "standard form first is what makes two polynomials comparable at a glance.",
            "**Adding means combining like terms.** Terms are LIKE when the variable parts match "
            "exactly — same letters, same exponents. $3x^{2}$ and $-8x^{2}$ are like terms; "
            "$3x^{2}$ and $3x$ are not. Combining them is just the distributive property run "
            "backwards: $3x^{2} - 8x^{2} = (3 - 8)x^{2} = -5x^{2}$.",
            "**Subtracting means adding the opposite of EVERY term.** This is the single most "
            "common place to lose a sign. $(4x^{2} + 3x) - (x^{2} - 5x)$ is "
            "$4x^{2} + 3x - x^{2} + 5x$ — the minus sign flipped the $-5x$ to $+5x$. Writing the "
            "distributed row before combining costs one line and prevents the error.",
            "**Closure is the real content of this lesson.** Add, subtract or multiply two "
            "polynomials and the result is another polynomial — never a fraction, never a root, "
            "never something new. Divide, and you can leave the system: "
            "$\\frac{x^{2}}{x + 1}$ is not a polynomial. This is exactly the integers' situation, "
            "and the analogy will keep paying off.",
        ],
        key_idea=(
            "Polynomials are closed under addition, subtraction and multiplication — the same three "
            "operations the integers are closed under, and for the same structural reason."
        ),
        facts=[
            fact(
                "Standard form",
                "a_{n}x^{n} + a_{n-1}x^{n-1} + \\cdots + a_{1}x + a_{0}",
                "Descending degree. The leading coefficient is $a_n$; the constant term is $a_0$.",
            ),
            fact(
                "Combining like terms",
                "ax^{k} + bx^{k} = (a + b)x^{k}",
                "Only the coefficients add. The exponent never changes — it is what makes them like.",
            ),
            fact(
                "Subtraction distributes the minus",
                "P - Q = P + (-1)Q",
                "Every term of $Q$ changes sign, not just the first one.",
            ),
            fact(
                "Degree of a sum",
                "\\deg(P + Q) \\le \\max(\\deg P, \\deg Q)",
                "Usually equal — but leading terms can cancel, as in $(x^2 + x) - (x^2 - 1)$.",
            ),
        ],
        worked=[
            problem(
                "im2-u2-l1-we1",
                "Write $6 - 4x^{3} + x - 9x^{2}$ in standard form, then state its degree, leading "
                "coefficient and constant term.",
                "**Order by descending exponent.** The powers present are $3$, $2$, $1$ and $0$:"
                "$$-4x^{3} - 9x^{2} + x + 6.$$"
                "**Read off the three quantities.** The degree is $3$ — the highest exponent "
                "appearing. The leading coefficient is $-4$, the number attached to $x^{3}$; note "
                "the sign belongs to the coefficient. The constant term is $6$."
                "**Why standard form is worth the rewrite.** Two polynomials in standard form can "
                "be compared term by term, and their degrees are visible without hunting. In the "
                "original ordering the leading term was buried in the middle."
                "**Spot-check at a value.** At $x = 1$ the original gives "
                "$6 - 4 + 1 - 9 = -6$, and the standard form gives $-4 - 9 + 1 + 6 = -6$ ✓ — "
                "reordering a sum cannot change its value, which is exactly what the check "
                "confirms.",
                [
                    "Eq(6 - 4*1**3 + 1 - 9*1**2, -6)",
                    "Eq(-4*1**3 - 9*1**2 + 1 + 6, -6)",
                    "Eq(6 - 4*2**3 + 2 - 9*2**2, -60)",
                    "Eq(-4*2**3 - 9*2**2 + 2 + 6, -60)",
                ],
            ),
            problem(
                "im2-u2-l1-we2",
                "Add $(3x^{2} - 7x + 2)$ and $(5x^{2} + 4x - 9)$.",
                "**Line up like terms.** The $x^{2}$ terms combine with each other, the $x$ terms "
                "with each other, the constants with each other:"
                "$$(3 + 5)x^{2} + (-7 + 4)x + (2 - 9).$$"
                "**Do the three small additions.**"
                "$$8x^{2} - 3x - 7.$$"
                "**Notice what did NOT happen.** The exponents were untouched. Adding "
                "$3x^{2} + 5x^{2}$ gives $8x^{2}$, not $8x^{4}$ — you are counting how many "
                "$x^{2}$s you have, exactly as $3$ apples plus $5$ apples is $8$ apples."
                "**Check the answer.** At $x = 2$: First polynomial: $12 - 14 + 2 = 0$. Second: "
                "$20 + 8 - 9 = 19$. Sum should be $19$, and $8(4) - 6 - 7 = 32 - 13 = 19$ ✓",
                [
                    "Eq(3*2**2 - 7*2 + 2, 0)",
                    "Eq(5*2**2 + 4*2 - 9, 19)",
                    "Eq(8*2**2 - 3*2 - 7, 19)",
                    "Eq(3*(-1)**2 - 7*(-1) + 2 + 5*(-1)**2 + 4*(-1) - 9, 8*(-1)**2 - 3*(-1) - 7)",
                ],
            ),
            problem(
                "im2-u2-l1-we3",
                "Subtract: $(4x^{3} + x^{2} - 6x) - (x^{3} - 5x^{2} + 6x - 11)$.",
                "**Distribute the minus sign across every term of the second polynomial.** This is "
                "the step worth writing out:"
                "$$4x^{3} + x^{2} - 6x - x^{3} + 5x^{2} - 6x + 11.$$"
                "Three of the four signs changed. The $-11$ became $+11$ — a term with no variable "
                "is no more exempt than any other."
                "**Now combine like terms.**"
                "$$(4 - 1)x^{3} + (1 + 5)x^{2} + (-6 - 6)x + 11 = 3x^{3} + 6x^{2} - 12x + 11.$$"
                "**Check the answer.** At $x = 1$: First: $4 + 1 - 6 = -1$. Second: $1 - 5 + 6 - 11 = -9$. "
                "Difference: $-1 - (-9) = 8$. The answer at $x = 1$: $3 + 6 - 12 + 11 = 8$ ✓"
                "**Why this check is worth the ten seconds.** A dropped sign almost always changes "
                "the value at $x = 1$, so a single substitution catches the commonest error in the "
                "whole lesson.",
                [
                    "Eq(4*1**3 + 1**2 - 6*1, -1)",
                    "Eq(1**3 - 5*1**2 + 6*1 - 11, -9)",
                    "Eq(-1 - (-9), 8)",
                    "Eq(3*1**3 + 6*1**2 - 12*1 + 11, 8)",
                    "Eq(4*2**3 + 2**2 - 6*2 - (2**3 - 5*2**2 + 6*2 - 11), 3*2**3 + 6*2**2 - 12*2 + 11)",
                ],
            ),
            problem(
                "im2-u2-l1-we4",
                "Decide which of these are polynomials, and give the degree of those that are: "
                "(a) $4x^{2} - \\sqrt{3}x + 1$; (b) $\\dfrac{5}{x} + 2$; (c) $x^{3}\\sqrt{x}$; "
                "(d) $7$.",
                "**Part (a) is a polynomial of degree 2.** The coefficient $-\\sqrt{3}$ is "
                "irrational, but the definition restricts the EXPONENTS, not the coefficients. "
                "Coefficients may be any real numbers."
                "**Part (b) is not.** Rewrite it: $\\frac{5}{x} = 5x^{-1}$, and $-1$ is not a "
                "whole number. This is the classic trap — the expression looks harmless until you "
                "move the variable out of the denominator."
                "**Part (c) is not either.** $x^{3}\\sqrt{x} = x^{3} \\cdot x^{1/2} = x^{7/2}$, and "
                "$\\frac{7}{2}$ is not a whole number. A variable under a radical is always "
                "disqualifying."
                "**Part (d) IS a polynomial, of degree 0.** A constant is $7x^{0}$, and $0$ is a "
                "whole number. Constants are the degree-zero case, not an exception to the "
                "definition."
                "**The test in one sentence.** Rewrite every part as a power of $x$; if any "
                "exponent is negative or fractional, it is not a polynomial.",
                [
                    "Eq(Rational(5,1)*2**(-1), Rational(5,2))",
                    "Eq(2**3 * sqrt(2), 2**Rational(7,2))",
                    "Eq(7*3**0, 7)",
                    "Eq(4*2**2 - sqrt(3)*2 + 1, 17 - 2*sqrt(3))",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Adding the exponents when adding like terms: $3x^{2} + 5x^{2} = 8x^{4}$.",
                "Adding counts terms; it never touches the exponent. $3x^2 + 5x^2 = 8x^2$. "
                "Check at $x = 1$: $3 + 5 = 8$, and $8(1)^2 = 8$ ✓ but $8(1)^4 = 8$ too — so check "
                "at $x = 2$: $12 + 20 = 32 = 8 \\cdot 4$ ✓, while $8 \\cdot 16 = 128$ ✗.",
            ),
            mistake(
                "Distributing a subtraction only onto the first term of the second polynomial.",
                "The minus sign multiplies the whole bracket. Write the fully distributed row "
                "before combining — every term of the subtracted polynomial changes sign.",
            ),
            mistake(
                "Calling $\\frac{3}{x} + x$ a polynomial because it 'has no roots or decimals'.",
                "Rewrite each part as a power: $3x^{-1} + x$. The exponent $-1$ disqualifies it. "
                "The test is on the exponents, always.",
            ),
            mistake(
                "Reading the leading coefficient of $-4x^3 + 2x$ as $4$.",
                "The sign is part of the coefficient: it is $-4$. This matters immediately in "
                "Unit 3, where the sign of the leading coefficient decides which way a parabola "
                "opens.",
            ),
        ],
        try_it=[
            problem(
                "im2-u2-l1-t1",
                "Write $5x - 2 + 3x^{4} - x^{2}$ in standard form and state its degree and leading "
                "coefficient.",
                "Descending exponents: $3x^{4} - x^{2} + 5x - 2$. Degree $4$; leading coefficient "
                "$3$; constant term $-2$. Check at $x = 1$: original gives $5 - 2 + 3 - 1 = 5$, "
                "and the standard form gives $3 - 1 + 5 - 2 = 5$ ✓",
                [
                    "Eq(5*1 - 2 + 3*1**4 - 1**2, 5)",
                    "Eq(3*1**4 - 1**2 + 5*1 - 2, 5)",
                    "Eq(3*2**4 - 2**2 + 5*2 - 2, 52)",
                ],
            ),
            problem(
                "im2-u2-l1-t2",
                "Simplify $(2x^{2} - 9x + 4) - (7x^{2} - 9x - 1)$.",
                "Distribute the minus: $2x^{2} - 9x + 4 - 7x^{2} + 9x + 1$. Combine: the $x$ terms "
                "cancel completely ($-9x + 9x = 0$), leaving $-5x^{2} + 5$. Check at $x = 2$: "
                "$(8 - 18 + 4) - (28 - 18 - 1) = -6 - 9 = -15$, and $-5(4) + 5 = -15$ ✓ — the "
                "vanishing middle term is real, not a slip.",
                [
                    "Eq(2*2**2 - 9*2 + 4, -6)",
                    "Eq(7*2**2 - 9*2 - 1, 9)",
                    "Eq(-6 - 9, -15)",
                    "Eq(-5*2**2 + 5, -15)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-APR.1",
                "title": "A number system you already know how to use",
                "body": (
                    "Polynomials add, subtract and multiply exactly like integers, and fail to "
                    "divide exactly like integers. Once you see that, most of this unit is "
                    "arithmetic you have done since primary school, wearing a letter."
                ),
                "beats": [
                    "Integers: closed under $+$, $-$, $\\times$",
                    "Not closed under $\\div$ — $\\frac{3}{2}$ escapes",
                    "Polynomials: closed under $+$, $-$, $\\times$",
                    "Not under $\\div$ — $\\frac{x^2}{x+1}$ escapes",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "The definition",
                "title": "Everything hangs on the exponents",
                "body": (
                    "A polynomial allows only whole-number exponents on the variable. The "
                    "coefficients can be anything — negative, fractional, even $\\sqrt{3}$. The "
                    "restriction is on the exponents alone, and every 'is this a polynomial?' "
                    "question is settled by rewriting each part as a power of $x$."
                ),
            },
            {
                "kind": "worked",
                "title": "Standard form, degree, leading coefficient",
                "problemId": "im2-u2-l1-we1",
            },
            {
                "kind": "algebraTiles",
                "eyebrow": "See like terms",
                "title": "Why only matching tiles combine",
                "teach": (
                    "The $x$-tiles and the unit squares are different shapes, so they cannot be "
                    "stacked into one pile. That is the whole content of 'like terms' — you can "
                    "only count together the things that are the same size."
                ),
                "config": {"x": 3, "units": 5, "mode": "build", "maxX": 8, "maxUnits": 10},
            },
            tap(
                "Which pair are like terms?",
                "Only one of these pairs can be combined into a single term. Which?",
                ["$4x^{2}$ and $9x^{3}$", "$4x^{2}$ and $-11x^{2}$", "$4x^{2}$ and $4x$", "$4x$ and $4$"],
                1,
                "Like terms need identical variable parts — same letter, same exponent. Only "
                "$4x^{2}$ and $-11x^{2}$ match, and they combine to $-7x^{2}$.",
                ["Eq(4 - 11, -7)", "Eq(4*3**2 - 11*3**2, -7*3**2)"],
            ),
            {
                "kind": "worked",
                "title": "Adding: count the like terms",
                "problemId": "im2-u2-l1-we2",
            },
            {
                "kind": "tip",
                "eyebrow": "The sign trap",
                "title": "Write the distributed row",
                "body": (
                    "When subtracting, write out the row where every sign has already been "
                    "flipped BEFORE you combine anything. One extra line eliminates the single "
                    "most common error in the entire unit."
                ),
            },
            {
                "kind": "worked",
                "title": "Subtracting: the minus hits everything",
                "problemId": "im2-u2-l1-we3",
            },
            tap(
                "Distribute the minus",
                "What is $(x^{2} + 3x) - (2x^{2} - 3x + 5)$?",
                ["$-x^{2} + 6x - 5$", "$-x^{2} + 5$", "$3x^{2} - 5$", "$-x^{2} - 5$"],
                0,
                "Flipping all three signs gives $x^{2} + 3x - 2x^{2} + 3x - 5$, which combines to "
                "$-x^{2} + 6x - 5$. Check at $x = 1$: $(1 + 3) - (2 - 3 + 5) = 4 - 4 = 0$, and "
                "$-1 + 6 - 5 = 0$ ✓",
                [
                    "Eq(1**2 + 3*1 - (2*1**2 - 3*1 + 5), 0)",
                    "Eq(-1**2 + 6*1 - 5, 0)",
                    "Eq(2**2 + 3*2 - (2*2**2 - 3*2 + 5), -4 + 12 - 5)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "The real point",
                "title": "Closure, and why anyone cares",
                "body": (
                    "Closure means you never have to ask what KIND of object you will get. Add two "
                    "polynomials — polynomial. Multiply a hundred of them — still a polynomial. "
                    "That guarantee is what lets you build long algebraic arguments without "
                    "stopping to check the type of every intermediate result."
                ),
            },
            {
                "kind": "worked",
                "title": "Is it a polynomial?",
                "problemId": "im2-u2-l1-we4",
            },
            {"kind": "tryIt", "title": "Standard form", "problemId": "im2-u2-l1-t1"},
            {"kind": "tryIt", "title": "A subtraction where terms vanish", "problemId": "im2-u2-l1-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Polynomial = whole-number exponents only; coefficients are unrestricted",
                    "Degree is the highest exponent; it controls the graph and the solution count",
                    "Adding combines like terms — exponents never change",
                    "Subtracting flips the sign of EVERY term in the second polynomial",
                    "Closed under $+$, $-$, $\\times$; not under $\\div$ — exactly like the integers",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 2 — A-APR.1: multiplying, and the special products
# ===========================================================================
def lesson_multiplying():
    return lesson(
        slug="multiplying-polynomials",
        title="Multiplying Polynomials",
        concrete=(
            "Multiplying $(x + 3)(x + 5)$ is the same bookkeeping as multiplying $23 \\times 15$ "
            "by hand: every digit of one number meets every digit of the other. Polynomials just "
            "keep the place values visible as powers of $x$ instead of collapsing them into "
            "columns."
        ),
        objective=(
            "Multiply polynomials by distributing every term over every term, and recognise the "
            "two special products that will be run backwards in Lesson 4."
        ),
        concept=[
            "**One rule covers every case: every term times every term.** FOIL is not a separate "
            "method — it is a name for what the distributive property does when both brackets "
            "happen to have two terms. For $(x + 2)(x^{2} - 3x + 4)$ there is no F, O, I or L, but "
            "the rule is unchanged: three products from the $x$, three from the $2$, six in total.",
            "**Count the products before you start.** A binomial times a trinomial gives "
            "$2 \\times 3 = 6$ products. If you end up with five, you dropped one. This count is "
            "the cheapest error-detector available and it takes no time at all.",
            "**The degree of a product is the sum of the degrees.** Multiply a degree-2 by a "
            "degree-3 and the answer has degree $5$, because the leading terms multiply and "
            "nothing else can reach that high. So you know the shape of the answer before you have "
            "written a single term.",
            "**The difference of squares.** $(a + b)(a - b) = a^{2} - b^{2}$. The middle terms are "
            "$+ab$ and $-ab$, which annihilate each other. Nothing here is memorised — the "
            "cancellation is visible the moment you write the four products out.",
            "**The perfect square.** $(a + b)^{2} = a^{2} + 2ab + b^{2}$, and note carefully that "
            "it is NOT $a^{2} + b^{2}$. The middle term is there because $a \\cdot b$ appears "
            "twice, once from each ordering. Similarly $(a - b)^{2} = a^{2} - 2ab + b^{2}$.",
            "**Why these two get names.** Lesson 4 runs them backwards. Recognising "
            "$x^{2} - 49$ as a difference of squares is what lets you write it as "
            "$(x + 7)(x - 7)$ instantly. Learning the forward direction cleanly is what makes the "
            "reverse direction feel obvious.",
        ],
        key_idea=(
            "Multiplication is one rule — every term times every term — and the two special "
            "products are just the cases where the cross terms behave in a way worth remembering."
        ),
        facts=[
            fact(
                "Difference of squares",
                "(a + b)(a - b) = a^{2} - b^{2}",
                "The two middle products, $+ab$ and $-ab$, cancel exactly.",
            ),
            fact(
                "Square of a sum",
                "(a + b)^{2} = a^{2} + 2ab + b^{2}",
                "The $2ab$ is there because $ab$ appears twice. It is never optional.",
            ),
            fact(
                "Square of a difference",
                "(a - b)^{2} = a^{2} - 2ab + b^{2}",
                "Only the middle term changes sign; $b^2$ stays positive.",
            ),
            fact(
                "Degree of a product",
                "\\deg(PQ) = \\deg P + \\deg Q",
                "Leading terms multiply and cannot be cancelled by anything else.",
            ),
        ],
        worked=[
            problem(
                "im2-u2-l2-we1",
                "Expand $(x + 3)(x + 5)$, and explain where the middle term comes from.",
                "**Four products, one from each pairing.**"
                "$$x \\cdot x = x^{2}, \\quad x \\cdot 5 = 5x, \\quad 3 \\cdot x = 3x, "
                "\\quad 3 \\cdot 5 = 15.$$"
                "**Combine the two like terms.** The $5x$ and $3x$ are like, so they merge:"
                "$$x^{2} + 8x + 15.$$"
                "**Where the middle coefficient came from.** It is $5 + 3$ — the SUM of the two constants. And "
                "the $15$ is $5 \\times 3$, their PRODUCT. That sum-and-product pairing is the "
                "entire basis of the factoring method in Lesson 3, so it is worth noticing here "
                "rather than discovering it later."
                "**Check the answer.** At $x = 2$: $(2 + 3)(2 + 5) = 5 \\times 7 = 35$, and "
                "$4 + 16 + 15 = 35$ ✓",
                [
                    "Eq((2 + 3)*(2 + 5), 35)",
                    "Eq(2**2 + 8*2 + 15, 35)",
                    "Eq(3 + 5, 8)",
                    "Eq(3*5, 15)",
                    "Eq((10 + 3)*(10 + 5), 10**2 + 8*10 + 15)",
                ],
            ),
            problem(
                "im2-u2-l2-we2",
                "Expand $(2x - 3)(x^{2} + 4x - 1)$.",
                "**Count first.** Two terms times three terms means six products. If the working "
                "produces five, something was dropped."
                "**Distribute the first term across the trinomial.**"
                "$$2x \\cdot x^{2} = 2x^{3}, \\quad 2x \\cdot 4x = 8x^{2}, "
                "\\quad 2x \\cdot (-1) = -2x.$$"
                "**Distribute the second term, carrying its sign.**"
                "$$-3 \\cdot x^{2} = -3x^{2}, \\quad -3 \\cdot 4x = -12x, "
                "\\quad -3 \\cdot (-1) = 3.$$"
                "**Collect like terms.** Six products, then combine:"
                "$$2x^{3} + (8 - 3)x^{2} + (-2 - 12)x + 3 = 2x^{3} + 5x^{2} - 14x + 3.$$"
                "**Two checks.** The degree should be $1 + 2 = 3$, and it is. At $x = 1$: "
                "$(2 - 3)(1 + 4 - 1) = (-1)(4) = -4$, and $2 + 5 - 14 + 3 = -4$ ✓",
                [
                    "Eq((2*1 - 3)*(1**2 + 4*1 - 1), -4)",
                    "Eq(2*1**3 + 5*1**2 - 14*1 + 3, -4)",
                    "Eq((2*2 - 3)*(2**2 + 4*2 - 1), 11)",
                    "Eq(2*2**3 + 5*2**2 - 14*2 + 3, 11)",
                    "Eq(2*(-1) - 3, -5)",
                ],
            ),
            problem(
                "im2-u2-l2-we3",
                "Expand $(x + 7)(x - 7)$ and $(3x - 2)(3x + 2)$, and say what the two have in "
                "common.",
                "**The first, written out in full.**"
                "$$x^{2} - 7x + 7x - 49 = x^{2} - 49.$$"
                "The $-7x$ and $+7x$ destroy each other. Nothing was memorised — the cancellation "
                "is simply what the four products do."
                "**The second, same structure.**"
                "$$9x^{2} + 6x - 6x - 4 = 9x^{2} - 4.$$"
                "**What they share.** Both are (something $+$ something)(same $-$ same). Whenever "
                "the two brackets differ only in a sign, the cross terms are exact opposites and "
                "the answer is a difference of two squares:"
                "$$(a + b)(a - b) = a^{2} - b^{2}.$$"
                "**Check the second one.** At $x = 1$: $(3 - 2)(3 + 2) = 1 \\times 5 = 5$, and "
                "$9 - 4 = 5$ ✓",
                [
                    "Eq((1 + 7)*(1 - 7), 1**2 - 49)",
                    "Eq((3*1 - 2)*(3*1 + 2), 9*1**2 - 4)",
                    "Eq((3*2 - 2)*(3*2 + 2), 9*2**2 - 4)",
                    "Eq((10 + 7)*(10 - 7), 100 - 49)",
                ],
            ),
            problem(
                "im2-u2-l2-we4",
                "Expand $(x + 6)^{2}$ and $(2x - 5)^{2}$. Then explain why $(x + 6)^{2}$ is not "
                "$x^{2} + 36$.",
                "**The first.** A square means the bracket times itself:"
                "$$(x + 6)(x + 6) = x^{2} + 6x + 6x + 36 = x^{2} + 12x + 36.$$"
                "**The second, with the sign carried carefully.**"
                "$$(2x - 5)(2x - 5) = 4x^{2} - 10x - 10x + 25 = 4x^{2} - 20x + 25.$$"
                "Note $(-5)(-5) = +25$ — the last term is positive even though the bracket had a "
                "minus."
                "**Why the middle term must be there.** The product $x \\cdot 6$ arises twice, "
                "once from each ordering, so it contributes $12x$, not nothing. Dropping it is the "
                "single most common algebra error at this level."
                "**A numerical proof that it matters.** At $x = 4$: $(4 + 6)^{2} = 100$. The "
                "correct expansion gives $16 + 48 + 36 = 100$ ✓, while $x^{2} + 36$ would give "
                "$16 + 36 = 52$ ✗ — off by $48$, which is precisely the missing middle term.",
                [
                    "Eq((4 + 6)**2, 100)",
                    "Eq(4**2 + 12*4 + 36, 100)",
                    "Eq(4**2 + 36, 52)",
                    "Eq(100 - 52, 48)",
                    "Eq((2*3 - 5)**2, 4*3**2 - 20*3 + 25)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Writing $(a + b)^{2} = a^{2} + b^{2}$.",
                "Squaring a sum is not squaring each piece. Test with numbers: "
                "$(3 + 4)^2 = 49$, but $9 + 16 = 25$. The missing $24$ is the $2ab$ term.",
            ),
            mistake(
                "Using FOIL on a binomial times a trinomial and stopping after four products.",
                "FOIL only names the four products of two binomials. The real rule is every term "
                "times every term — count the products first ($2 \\times 3 = 6$ here).",
            ),
            mistake(
                "Losing the sign when distributing a negative term.",
                "The sign belongs to the term. In $(2x - 3)(\\ldots)$ you distribute $-3$, not $3$, "
                "and $-3 \\times -1 = +3$.",
            ),
            mistake(
                "Expecting $(a - b)^2$ to end in $-b^2$.",
                "The last term is $(-b)(-b) = +b^2$. Only the middle term carries the minus.",
            ),
        ],
        try_it=[
            problem(
                "im2-u2-l2-t1",
                "Expand $(x - 4)(x + 9)$.",
                "Four products: $x^{2} + 9x - 4x - 36 = x^{2} + 5x - 36$. The middle coefficient "
                "is $9 + (-4) = 5$ and the constant is $9 \\times (-4) = -36$ — sum and product "
                "again. Check at $x = 1$: $(-3)(10) = -30$, and $1 + 5 - 36 = -30$ ✓",
                [
                    "Eq((1 - 4)*(1 + 9), -30)",
                    "Eq(1**2 + 5*1 - 36, -30)",
                    "Eq(9 - 4, 5)",
                    "Eq(9*(-4), -36)",
                ],
            ),
            problem(
                "im2-u2-l2-t2",
                "Expand $(3x + 4)^{2}$ and $(5x - 1)(5x + 1)$.",
                "The square: $9x^{2} + 12x + 12x + 16 = 9x^{2} + 24x + 16$. The difference of "
                "squares: the cross terms $+5x$ and $-5x$ cancel, leaving $25x^{2} - 1$. Check "
                "both at $x = 1$: $(3 + 4)^{2} = 49 = 9 + 24 + 16$ ✓ and "
                "$(5 - 1)(5 + 1) = 24 = 25 - 1$ ✓",
                [
                    "Eq((3*1 + 4)**2, 49)",
                    "Eq(9*1**2 + 24*1 + 16, 49)",
                    "Eq((5*1 - 1)*(5*1 + 1), 24)",
                    "Eq(25*1**2 - 1, 24)",
                    "Eq((3*2 + 4)**2, 9*2**2 + 24*2 + 16)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-APR.1",
                "title": "One rule, not four methods",
                "body": (
                    "Every term of the first bracket multiplies every term of the second. FOIL, "
                    "the box method, vertical multiplication — they are three ways of organising "
                    "that single rule, and they always produce the same products."
                ),
                "beats": [
                    "Count the products first: $m \\times n$",
                    "Multiply every pair",
                    "Combine like terms",
                    "Check the degree: $\\deg P + \\deg Q$",
                ],
            },
            {
                "kind": "worked",
                "title": "Two binomials, and where the middle term comes from",
                "problemId": "im2-u2-l2-we1",
            },
            {
                "kind": "algebraTiles",
                "eyebrow": "The area picture",
                "title": "A product is a rectangle",
                "teach": (
                    "Lay $(x + 3)$ along one side and $(x + 5)$ along the other. The rectangle "
                    "splits into an $x^{2}$ square, eight $x$-strips and fifteen unit squares — "
                    "which is exactly $x^{2} + 8x + 15$. Multiplication is area."
                ),
                "config": {"x": 3, "units": 5, "mode": "build", "maxX": 8, "maxUnits": 15},
            },
            tap(
                "How many products?",
                "Multiplying a 3-term polynomial by a 4-term polynomial, how many products before "
                "combining like terms?",
                ["$7$", "$12$", "$34$", "$3$"],
                1,
                "Every term meets every term: $3 \\times 4 = 12$ products. Counting first is the "
                "cheapest way to notice you dropped one.",
                ["Eq(3*4, 12)", "Ne(3 + 4, 12)"],
            ),
            {
                "kind": "worked",
                "title": "Binomial times trinomial: six products",
                "problemId": "im2-u2-l2-we2",
            },
            {
                "kind": "teach",
                "eyebrow": "Special product 1",
                "title": "When the middle terms cancel",
                "body": (
                    "$(a + b)(a - b)$ produces $+ab$ and $-ab$ in the middle. They cancel every "
                    "time, leaving $a^{2} - b^{2}$. This is worth naming only because Lesson 4 "
                    "runs it backwards — spotting $x^{2} - 49$ as a difference of squares is a "
                    "one-second factorisation."
                ),
            },
            {
                "kind": "worked",
                "title": "Difference of squares, twice",
                "problemId": "im2-u2-l2-we3",
            },
            {
                "kind": "teach",
                "eyebrow": "Special product 2",
                "title": "The middle term nobody wants to write",
                "body": (
                    "$(a + b)^{2} = a^{2} + 2ab + b^{2}$. The $2ab$ exists because $ab$ appears "
                    "twice, once from each ordering. Test it with numbers whenever you are "
                    "tempted to drop it: $(3 + 4)^{2} = 49$, not $9 + 16 = 25$."
                ),
            },
            {
                "kind": "worked",
                "title": "Squaring a binomial, and why $a^2 + b^2$ is wrong",
                "problemId": "im2-u2-l2-we4",
            },
            tap(
                "Expand the square",
                "What is $(x - 8)^{2}$?",
                ["$x^{2} - 64$", "$x^{2} + 64$", "$x^{2} - 16x + 64$", "$x^{2} - 16x - 64$"],
                2,
                "$(x - 8)(x - 8) = x^{2} - 8x - 8x + 64 = x^{2} - 16x + 64$. The last term is "
                "positive because $(-8)(-8) = +64$; only the middle term is negative.",
                [
                    "Eq((1 - 8)**2, 49)",
                    "Eq(1**2 - 16*1 + 64, 49)",
                    "Eq((-8)*(-8), 64)",
                ],
            ),
            {"kind": "tryIt", "title": "Two binomials with a negative", "problemId": "im2-u2-l2-t1"},
            {"kind": "tryIt", "title": "Both special products", "problemId": "im2-u2-l2-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Every term times every term — FOIL is just the 2-by-2 case",
                    "Count the products first; $m$ terms times $n$ terms gives $mn$ products",
                    "$(a + b)(a - b) = a^{2} - b^{2}$ — the cross terms cancel",
                    "$(a \\pm b)^{2} = a^{2} \\pm 2ab + b^{2}$ — the middle term is never optional",
                    "In $(x + p)(x + q)$ the middle coefficient is $p + q$ and the constant is $pq$",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 3 — A-SSE.2, A-SSE.3a: common factors, x^2+bx+c, grouping
# ===========================================================================
def lesson_factoring_basics():
    return lesson(
        slug="factoring-basics",
        title="Factoring: Common Factors and Simple Trinomials",
        concrete=(
            "Factoring $x^{2} + 8x + 15$ into $(x + 3)(x + 5)$ is the same act as writing $15$ as "
            "$3 \\times 5$: rewriting a sum as a product so that its hidden structure becomes "
            "visible. And the payoff is identical — a product tells you when the whole thing is "
            "zero, which a sum never does."
        ),
        objective=(
            "Pull out the greatest common factor, factor $x^{2} + bx + c$ by finding two numbers "
            "with the right sum and product, and factor four-term expressions by grouping."
        ),
        concept=[
            "**Factoring is multiplication read backwards.** Everything in this lesson is a "
            "question of the form: what did I multiply to get this? That is why Lesson 2 came "
            "first — you cannot reverse a process you cannot run forwards.",
            "**Always look for a common factor first.** In $6x^{2} + 15x$ both terms contain $3x$, "
            "so it comes out: $3x(2x + 5)$. Skipping this step makes every later step harder, and "
            "sometimes makes an expression look unfactorable when it is not.",
            "**For a monic trinomial, find two numbers with the right sum and product.** For "
            "$x^{2} + bx + c$ they must multiply to $c$ and add to $b$. This "
            "is not a trick to memorise — it is exactly what Lesson 2 showed. Expanding "
            "$(x + p)(x + q)$ gives $x^{2} + (p + q)x + pq$, so the constant is the product and "
            "the middle coefficient is the sum.",
            "**The signs tell you where to look before you start searching.** If $c > 0$ the two "
            "numbers share a sign, and it is the sign of $b$. If $c < 0$ they have opposite signs, "
            "and the larger-in-size one carries the sign of $b$. Reading the signs first cuts the "
            "candidate list roughly in half.",
            "**Grouping handles four terms.** Split into two pairs, factor each pair, and hope the "
            "leftover brackets match: "
            "$x^{3} + 2x^{2} + 5x + 10 = x^{2}(x + 2) + 5(x + 2) = (x + 2)(x^{2} + 5)$. If the "
            "brackets do not match, try a different pairing before giving up.",
            "**Not everything factors over the integers.** $x^{2} + x + 1$ has no integer pair "
            "multiplying to $1$ and adding to $1$. Saying so is a complete and correct answer — "
            "'prime' is a result, not a failure. Unit 4 will give such expressions roots anyway, "
            "just not integer ones.",
        ],
        key_idea=(
            "To factor $x^{2} + bx + c$, find two numbers whose product is $c$ and whose sum is "
            "$b$ — because that is precisely what expanding $(x + p)(x + q)$ produced."
        ),
        facts=[
            fact(
                "The sum-and-product rule",
                "x^{2} + bx + c = (x + p)(x + q) \\text{ where } pq = c,\\ p + q = b",
                "Read straight off the expansion of $(x+p)(x+q)$ — nothing extra is assumed.",
            ),
            fact(
                "Greatest common factor",
                "ab + ac = a(b + c)",
                "The distributive property, used right-to-left. Always the first thing to try.",
            ),
            fact(
                "Factoring by grouping",
                "ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)",
                "Works when the two leftover brackets come out identical.",
            ),
            fact(
                "Sign reading",
                "c > 0 \\Rightarrow \\text{same signs};\\quad c < 0 \\Rightarrow \\text{opposite signs}",
                "And when the signs are the same, $b$ tells you which one.",
            ),
        ],
        worked=[
            problem(
                "im2-u2-l3-we1",
                "Factor $12x^{3} - 18x^{2} + 30x$ completely.",
                "**Find the greatest common factor of the coefficients.** $12$, $18$ and $30$ "
                "share $6$ — and $6$ is the greatest such number, since $12$ and $18$ also share "
                "$6$ but nothing larger divides all three."
                "**Find the greatest common variable factor.** The powers present are $x^{3}$, "
                "$x^{2}$ and $x^{1}$; the smallest exponent is $1$, so $x$ comes out. You can "
                "never extract more than the smallest power available."
                "**Divide each term by the common factor and write the result.**"
                "$$12x^{3} - 18x^{2} + 30x = 6x(2x^{2} - 3x + 5).$$"
                "**Check by expanding back.** $6x \\cdot 2x^{2} = 12x^{3}$ ✓, "
                "$6x \\cdot (-3x) = -18x^{2}$ ✓, $6x \\cdot 5 = 30x$ ✓ — three terms out, three "
                "terms back."
                "**Is the bracket factorable further?** For $2x^{2} - 3x + 5$ you would need two "
                "numbers multiplying to $2 \\times 5 = 10$ and adding to $-3$. The pairs are "
                "$(-1, -10)$ and $(-2, -5)$, summing to $-11$ and $-7$. Neither is $-3$, so the "
                "factorisation is complete.",
                [
                    "Eq(6*1*(2*1**2 - 3*1 + 5), 12*1**3 - 18*1**2 + 30*1)",
                    "Eq(6*2*(2*2**2 - 3*2 + 5), 12*2**3 - 18*2**2 + 30*2)",
                    "Eq(gcd(gcd(12, 18), 30), 6)",
                    "Eq(-1 + -10, -11)",
                    "Eq(-2 + -5, -7)",
                ],
            ),
            problem(
                "im2-u2-l3-we2",
                "Factor $x^{2} + 11x + 24$.",
                "**State what you are looking for.** Two numbers whose product is $24$ and whose "
                "sum is $11$."
                "**Read the signs first.** The constant $24$ is positive, so the two numbers share "
                "a sign; the middle coefficient $11$ is positive, so both are positive. Negative "
                "candidates can be ignored entirely."
                "**List the positive factor pairs and their sums.**"
                "$$1 + 24 = 25, \\quad 2 + 12 = 14, \\quad 3 + 8 = 11 \\ \\checkmark, "
                "\\quad 4 + 6 = 10.$$"
                "**Write the factorisation.**"
                "$$x^{2} + 11x + 24 = (x + 3)(x + 8).$$"
                "**Verify by expanding.** $x^{2} + 8x + 3x + 24 = x^{2} + 11x + 24$ ✓ — and note "
                "the sum $3 + 8$ reappearing as the middle coefficient, exactly as Lesson 2 "
                "predicted.",
                [
                    "Eq(3*8, 24)",
                    "Eq(3 + 8, 11)",
                    "Eq((5 + 3)*(5 + 8), 5**2 + 11*5 + 24)",
                    "Eq(2 + 12, 14)",
                    "Eq(4 + 6, 10)",
                ],
            ),
            problem(
                "im2-u2-l3-we3",
                "Factor $x^{2} - 5x - 36$.",
                "**Read the signs.** The constant $-36$ is negative, so the two numbers have "
                "OPPOSITE signs. The middle coefficient $-5$ is negative, so the number with the "
                "larger absolute value is the negative one."
                "**Search the pairs with product thirty-six, then attach the signs.**"
                "$$1 \\text{ and } 36 \\to -35, \\quad 2 \\text{ and } 18 \\to -16, "
                "\\quad 3 \\text{ and } 12 \\to -9, \\quad 4 \\text{ and } 9 \\to -5 "
                "\\ \\checkmark$$"
                "So the numbers are $4$ and $-9$."
                "**Write and verify.**"
                "$$x^{2} - 5x - 36 = (x + 4)(x - 9).$$"
                "Expanding: $x^{2} - 9x + 4x - 36 = x^{2} - 5x - 36$ ✓"
                "**What this immediately gives you.** A product is zero exactly when a factor is "
                "zero, so this expression is zero at $x = -4$ and $x = 9$. That is the whole "
                "reason factoring is worth doing, and Unit 4 will use it constantly.",
                [
                    "Eq(4*(-9), -36)",
                    "Eq(4 + (-9), -5)",
                    "Eq((-4)**2 - 5*(-4) - 36, 0)",
                    "Eq(9**2 - 5*9 - 36, 0)",
                    "Eq((2 + 4)*(2 - 9), 2**2 - 5*2 - 36)",
                ],
            ),
            problem(
                "im2-u2-l3-we4",
                "Factor $2x^{3} + 6x^{2} + 5x + 15$ by grouping.",
                "**Split into two pairs.**"
                "$$(2x^{3} + 6x^{2}) + (5x + 15).$$"
                "**Factor each pair separately.** The first pair shares $2x^{2}$; the second "
                "shares $5$:"
                "$$2x^{2}(x + 3) + 5(x + 3).$$"
                "**Notice the shared bracket.** Both pieces now contain $(x + 3)$, so it can be "
                "pulled out as a common factor exactly like a number would be:"
                "$$(x + 3)(2x^{2} + 5).$$"
                "**Why the matching bracket is the whole method.** If the two leftover brackets "
                "had not matched, the grouping would have failed and you would try the other "
                "pairing. The match is the signal that the factorisation exists."
                "**Check the answer.** At $x = 1$: Original: $2 + 6 + 5 + 15 = 28$. Factored: "
                "$(1 + 3)(2 + 5) = 4 \\times 7 = 28$ ✓",
                [
                    "Eq(2*1**3 + 6*1**2 + 5*1 + 15, 28)",
                    "Eq((1 + 3)*(2*1**2 + 5), 28)",
                    "Eq(2*2**3 + 6*2**2 + 5*2 + 15, (2 + 3)*(2*2**2 + 5))",
                    "Eq(2*(-3)**3 + 6*(-3)**2 + 5*(-3) + 15, 0)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Factoring the trinomial first and forgetting the common factor.",
                "$2x^2 + 10x + 12$ is not fully factored as $(2x + 4)(x + 3)$ — pull the $2$ out "
                "first: $2(x^2 + 5x + 6) = 2(x + 2)(x + 3)$. 'Completely' means nothing is left "
                "to extract.",
            ),
            mistake(
                "Getting the signs backwards on $x^2 - 5x - 36$, writing $(x - 4)(x + 9)$.",
                "That expands to $x^2 + 5x - 36$ — the middle sign is wrong. The number with the "
                "larger absolute value carries the sign of $b$, so it is $(x + 4)(x - 9)$.",
            ),
            mistake(
                "Declaring an expression prime after checking only two factor pairs.",
                "List every pair systematically before concluding. For $x^2 + 11x + 24$ the "
                "answer is the third pair; stopping at the second would have missed it.",
            ),
            mistake(
                "Giving up on grouping when the first pairing fails.",
                "Try the other pairing. $x^3 + 5x + 2x^2 + 10$ fails as written but works "
                "reordered: $(x^3 + 2x^2) + (5x + 10) = (x + 2)(x^2 + 5)$.",
            ),
        ],
        try_it=[
            problem(
                "im2-u2-l3-t1",
                "Factor completely: $3x^{2} - 27x + 42$.",
                "Common factor $3$ first: $3(x^{2} - 9x + 14)$. Now two numbers with product $14$ "
                "and sum $-9$: both negative, and $-2 \\times -7 = 14$ with $-2 + -7 = -9$ ✓ So "
                "the answer is $3(x - 2)(x - 7)$. Check at $x = 1$: $3 - 27 + 42 = 18$, and "
                "$3(-1)(-6) = 18$ ✓",
                [
                    "Eq((-2)*(-7), 14)",
                    "Eq(-2 + (-7), -9)",
                    "Eq(3*1**2 - 27*1 + 42, 18)",
                    "Eq(3*(1 - 2)*(1 - 7), 18)",
                ],
            ),
            problem(
                "im2-u2-l3-t2",
                "Factor $x^{3} - 4x^{2} + 7x - 28$ by grouping.",
                "Pair them: $(x^{3} - 4x^{2}) + (7x - 28) = x^{2}(x - 4) + 7(x - 4)$. The brackets "
                "match, so $(x - 4)(x^{2} + 7)$. Check at $x = 1$: $1 - 4 + 7 - 28 = -24$, and "
                "$(1 - 4)(1 + 7) = -3 \\times 8 = -24$ ✓ Note $x^{2} + 7$ cannot factor further "
                "over the integers — a sum of squares never does.",
                [
                    "Eq(1**3 - 4*1**2 + 7*1 - 28, -24)",
                    "Eq((1 - 4)*(1**2 + 7), -24)",
                    "Eq(4**3 - 4*4**2 + 7*4 - 28, 0)",
                    "Eq(2**3 - 4*2**2 + 7*2 - 28, (2 - 4)*(2**2 + 7))",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-SSE.2",
                "title": "Factoring is Lesson 2 in reverse",
                "body": (
                    "Every technique here answers one question: what did I multiply to get this? "
                    "You already know the forward direction, so the work is recognising which "
                    "forward pattern produced what you are looking at."
                ),
                "beats": [
                    "Common factor out first — always",
                    "Two terms? Look for a difference of squares",
                    "Three terms? Sum and product",
                    "Four terms? Group in pairs",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "Step zero",
                "title": "The common factor is never optional",
                "body": (
                    "Before any other technique, ask what every term shares. Take the greatest "
                    "common numerical factor and the LOWEST power of each variable present. "
                    "Skipping this makes the remaining work harder and often leaves an answer "
                    "that is not fully factored."
                ),
            },
            {"kind": "worked", "title": "Pulling out the GCF", "problemId": "im2-u2-l3-we1"},
            {
                "kind": "factorTree",
                "eyebrow": "Where common factors live",
                "title": "Break the coefficients into primes",
                "teach": (
                    "The greatest common factor of a set of numbers is the product of the primes "
                    "they all share. Splitting $12$, $18$ and $30$ into primes shows a $2$ and a "
                    "$3$ in every one — and $2 \\times 3 = 6$ is the GCF."
                ),
                "config": {"number": 30},
            },
            {
                "kind": "teach",
                "eyebrow": "The core technique",
                "title": "Sum and product, straight from the expansion",
                "body": (
                    "$(x + p)(x + q) = x^{2} + (p + q)x + pq$. So to reverse it, find two numbers "
                    "with product $c$ and sum $b$. This is not a rule to memorise — it is the "
                    "expansion you already did, read from right to left."
                ),
            },
            {"kind": "worked", "title": "All positive: product 24, sum 11", "problemId": "im2-u2-l3-we2"},
            {
                "kind": "tip",
                "eyebrow": "Halve the search",
                "title": "Read the signs before you list anything",
                "body": (
                    "Constant positive means the two numbers share a sign, and $b$ says which. "
                    "Constant negative means opposite signs, with the bigger one carrying $b$'s "
                    "sign. Two seconds of sign reading removes half the candidates."
                ),
            },
            {"kind": "worked", "title": "Opposite signs: product $-36$, sum $-5$", "problemId": "im2-u2-l3-we3"},
            tap(
                "Find the pair",
                "Which two numbers factor $x^{2} - 2x - 15$?",
                ["$-3$ and $5$", "$3$ and $-5$", "$-3$ and $-5$", "$3$ and $5$"],
                1,
                "Product $-15$, sum $-2$. Opposite signs (constant is negative), and the larger "
                "one is negative (middle is negative): $3$ and $-5$. So "
                "$x^{2} - 2x - 15 = (x + 3)(x - 5)$.",
                [
                    "Eq(3*(-5), -15)",
                    "Eq(3 + (-5), -2)",
                    "Eq((-3)*5, -15)",
                    "Eq(-3 + 5, 2)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Four terms",
                "title": "Grouping: factor twice, then once more",
                "body": (
                    "Split into two pairs, factor each pair, and check whether the leftover "
                    "brackets are identical. If they are, that bracket comes out as a common "
                    "factor. If they are not, re-pair the terms and try again before concluding "
                    "it does not factor."
                ),
            },
            {"kind": "worked", "title": "Grouping in action", "problemId": "im2-u2-l3-we4"},
            {"kind": "tryIt", "title": "GCF first, then the trinomial", "problemId": "im2-u2-l3-t1"},
            {"kind": "tryIt", "title": "Grouping with a subtraction", "problemId": "im2-u2-l3-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "Common factor first, every time — GCF of coefficients, lowest power of each variable",
                    "For $x^{2} + bx + c$: two numbers with product $c$ and sum $b$",
                    "Signs: $c > 0$ means same signs (as $b$); $c < 0$ means opposite signs",
                    "Four terms: group in pairs and look for a matching bracket",
                    "'Does not factor over the integers' is a legitimate final answer",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 4 — A-SSE.2/3a: special forms and leading coefficients other than 1
# ===========================================================================
def lesson_special_factoring():
    return lesson(
        slug="special-factoring-forms",
        title="Special Forms and Leading Coefficients",
        concrete=(
            "A locksmith does not try every key. They look at the shape of the keyhole first. "
            "Factoring works the same way: two terms with a minus between two squares is one "
            "shape, a trinomial whose ends are both perfect squares is another, and recognising "
            "the shape turns a search into a single line of writing."
        ),
        objective=(
            "Factor a difference of squares and a perfect-square trinomial on sight, factor "
            "$ax^{2} + bx + c$ when $a \\neq 1$ using the ac-method, and know when to stop."
        ),
        concept=[
            "**Difference of squares.** The identity is $a^{2} - b^{2} = (a + b)(a - b)$: two terms, both perfect "
            "squares, with a minus between them. $x^{2} - 49 = (x + 7)(x - 7)$; "
            "$9x^{2} - 25 = (3x + 5)(3x - 5)$. The check is always the same — square each half "
            "and confirm you recover the original.",
            "**A SUM of squares does not factor over the reals.** $x^{2} + 49$ is prime. There is "
            "no sign arrangement of $(x \\pm 7)(x \\pm 7)$ that produces it, because any such "
            "product has a middle term or a minus. Unit 4 will factor it using complex numbers, "
            "but not before.",
            "**Perfect-square trinomial.** The identity is $a^{2} \\pm 2ab + b^{2} = (a \\pm b)^{2}$. Recognise it "
            "by checking the two ends are perfect squares and the middle is exactly twice the "
            "product of their roots. For $x^{2} + 12x + 36$: ends are $x^{2}$ and $6^{2}$, and "
            "$2 \\times x \\times 6 = 12x$ ✓ so it is $(x + 6)^{2}$.",
            "**The middle-term test is what makes it a THEOREM rather than a guess.** "
            "$x^{2} + 13x + 36$ also has square ends, but $2 \\times 6 = 12 \\neq 13$, so it is "
            "not a perfect square. It happens to factor as $(x + 4)(x + 9)$ — square ends alone "
            "prove nothing.",
            "**When the leading coefficient is not one, use the ac-method.** For $ax^{2} + bx + c$, find two numbers with "
            "product $ac$ and sum $b$, split the middle term into those two pieces, then group. "
            "It works because splitting the middle term is exactly the reverse of the collection "
            "step in the forward multiplication.",
            "**Completely factored means nothing is left to do.** Check each factor: any common "
            "factor left? Any difference of squares? Any trinomial that still factors? "
            "$4x^{4} - 64 = 4(x^{4} - 16) = 4(x^{2} + 4)(x^{2} - 4) = 4(x^{2} + 4)(x + 2)(x - 2)$ "
            "takes three passes, and stopping early is the commonest way to lose marks.",
        ],
        key_idea=(
            "Identify the shape before you search: difference of squares, perfect square, or "
            "neither — and when $a \\neq 1$, split the middle term using product $ac$ and sum $b$."
        ),
        facts=[
            fact(
                "Difference of squares",
                "a^{2} - b^{2} = (a + b)(a - b)",
                "Two terms, both squares, minus between. A sum of squares does not factor.",
            ),
            fact(
                "Perfect-square trinomial",
                "a^{2} \\pm 2ab + b^{2} = (a \\pm b)^{2}",
                "Square ends AND middle exactly $2ab$ — both conditions, or it is not one.",
            ),
            fact(
                "The ac-method",
                "\\text{product } = ac, \\quad \\text{sum } = b",
                "Split $bx$ into those two pieces, then factor by grouping.",
            ),
            fact(
                "Completely factored",
                "\\text{no common factor, no square difference, no factorable trinomial remains}",
                "Re-examine every factor you write until all three questions answer no.",
            ),
        ],
        worked=[
            problem(
                "im2-u2-l4-we1",
                "Factor $49x^{2} - 81$ and $x^{4} - 16$ completely.",
                "**The first one is a plain difference of squares.** $49x^{2} = (7x)^{2}$ and "
                "$81 = 9^{2}$:"
                "$$49x^{2} - 81 = (7x + 9)(7x - 9).$$"
                "Check by expanding: the cross terms $+63x$ and $-63x$ cancel, leaving "
                "$49x^{2} - 81$ ✓"
                "**The second one is a difference of squares TWICE.** First pass: "
                "$x^{4} = (x^{2})^{2}$ and $16 = 4^{2}$, so"
                "$$x^{4} - 16 = (x^{2} + 4)(x^{2} - 4).$$"
                "**Now examine each factor.** The second factor is itself a difference of squares:"
                "$$x^{2} - 4 = (x + 2)(x - 2).$$"
                "The first factor, $x^{2} + 4$, is a SUM of squares and does not factor over the "
                "reals. So the complete factorisation is"
                "$$x^{4} - 16 = (x^{2} + 4)(x + 2)(x - 2).$$"
                "**Check the answer.** At $x = 3$: $81 - 16 = 65$, and $(9 + 4)(3 + 2)(3 - 2) = 13 \\times 5 "
                "\\times 1 = 65$ ✓ — the multi-pass factorisation survives a numerical test.",
                [
                    "Eq((7*2 + 9)*(7*2 - 9), 49*2**2 - 81)",
                    "Eq(3**4 - 16, 65)",
                    "Eq((3**2 + 4)*(3 + 2)*(3 - 2), 65)",
                    "Eq((7*1 + 9)*(7*1 - 9), -32)",
                    "Eq(49*1**2 - 81, -32)",
                ],
            ),
            problem(
                "im2-u2-l4-we2",
                "Decide whether $x^{2} + 12x + 36$ and $x^{2} + 13x + 36$ are perfect-square "
                "trinomials, and factor both.",
                "**Test the first.** The ends are $x^{2}$ and $36 = 6^{2}$, both perfect squares. "
                "The middle term must equal $2 \\times x \\times 6 = 12x$ — and it does:"
                "$$x^{2} + 12x + 36 = (x + 6)^{2}.$$"
                "**Test the second.** The ends are the same two squares, so the shape is "
                "tempting. But the required middle term is $12x$, and this one has $13x$. It is "
                "NOT a perfect square."
                "**It still factors, just not as a square.** Product $36$, sum $13$: the pair is "
                "$4$ and $9$."
                "$$x^{2} + 13x + 36 = (x + 4)(x + 9).$$"
                "**The lesson from the pair.** Square ends are necessary but not sufficient. The "
                "middle-term test is what separates a perfect square from an ordinary trinomial "
                "that merely resembles one — and $(x + 6)^{2}$ would have been a genuine error "
                "for the second expression, since it expands with $12x$, not $13x$.",
                [
                    "Eq(2*6, 12)",
                    "Eq((1 + 6)**2, 1**2 + 12*1 + 36)",
                    "Eq(4*9, 36)",
                    "Eq(4 + 9, 13)",
                    "Eq((1 + 4)*(1 + 9), 1**2 + 13*1 + 36)",
                    "Ne(1**2 + 13*1 + 36, (1 + 6)**2)",
                ],
            ),
            problem(
                "im2-u2-l4-we3",
                "Factor $6x^{2} + 19x + 10$ using the ac-method.",
                "**Compute the ac product.** Here $a = 6$ and $c = 10$, so $ac = 60$. You need two numbers "
                "with product $60$ and sum $19$."
                "**Search the pairs.** Both must be positive (product and sum are both positive):"
                "$$1 + 60 = 61, \\quad 2 + 30 = 32, \\quad 3 + 20 = 23, \\quad 4 + 15 = 19 "
                "\\ \\checkmark$$"
                "**Split the middle term into those two pieces.**"
                "$$6x^{2} + 4x + 15x + 10.$$"
                "**Group and factor each pair.**"
                "$$2x(3x + 2) + 5(3x + 2) = (3x + 2)(2x + 5).$$"
                "**Why the brackets had to match.** Splitting the middle term with the ac-pair is "
                "exactly the reverse of collecting like terms in the forward multiplication, so "
                "the matching bracket is guaranteed whenever the ac-pair exists."
                "**Check the answer.** At $x = 1$: $6 + 19 + 10 = 35$, and $(3 + 2)(2 + 5) = 5 \\times 7 = "
                "35$ ✓",
                [
                    "Eq(6*10, 60)",
                    "Eq(4*15, 60)",
                    "Eq(4 + 15, 19)",
                    "Eq(6*1**2 + 19*1 + 10, 35)",
                    "Eq((3*1 + 2)*(2*1 + 5), 35)",
                    "Eq((3*2 + 2)*(2*2 + 5), 6*2**2 + 19*2 + 10)",
                ],
            ),
            problem(
                "im2-u2-l4-we4",
                "Factor $8x^{3} - 18x$ completely, and then $3x^{2} - 14x + 8$.",
                "**The first: common factor before anything else.** Both terms contain $2x$:"
                "$$8x^{3} - 18x = 2x(4x^{2} - 9).$$"
                "**Examine the bracket.** $4x^{2} - 9 = (2x)^{2} - 3^{2}$ — a difference of "
                "squares:"
                "$$8x^{3} - 18x = 2x(2x + 3)(2x - 3).$$"
                "Had the common factor been skipped, $8x^{3} - 18x$ would not have looked like any "
                "recognisable pattern at all."
                "**The second: ac-method with a negative middle term.** $ac = 3 \\times 8 = 24$, "
                "and the sum must be $-14$. Since the product is positive and the sum negative, "
                "both numbers are negative: $-2$ and $-12$ give $24$ and $-14$ ✓"
                "**Split and group.**"
                "$$3x^{2} - 2x - 12x + 8 = x(3x - 2) - 4(3x - 2) = (3x - 2)(x - 4).$$"
                "Note the $-4$ pulled out of the second pair — factoring out a negative is what "
                "makes the brackets match."
                "**Check the answer.** At $x = 1$: $3 - 14 + 8 = -3$, and $(3 - 2)(1 - 4) = 1 \\times (-3) = "
                "-3$ ✓",
                [
                    "Eq(2*1*(2*1 + 3)*(2*1 - 3), 8*1**3 - 18*1)",
                    "Eq(2*2*(2*2 + 3)*(2*2 - 3), 8*2**3 - 18*2)",
                    "Eq((-2)*(-12), 24)",
                    "Eq(-2 + (-12), -14)",
                    "Eq(3*1**2 - 14*1 + 8, -3)",
                    "Eq((3*1 - 2)*(1 - 4), -3)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Factoring $x^{2} + 25$ as $(x + 5)(x + 5)$ or $(x + 5)(x - 5)$.",
                "Neither works: the first expands to $x^2 + 10x + 25$ and the second to "
                "$x^2 - 25$. A sum of squares is prime over the reals.",
            ),
            mistake(
                "Calling $x^{2} + 13x + 36$ a perfect square because $36 = 6^{2}$.",
                "Square ends are not enough. The middle must be exactly $2 \\times 1 \\times 6 = "
                "12x$. Since it is $13x$, factor by sum and product instead: $(x + 4)(x + 9)$.",
            ),
            mistake(
                "Stopping after one pass on $x^{4} - 16$.",
                "$(x^2 + 4)(x^2 - 4)$ is not complete — the second factor is another difference "
                "of squares. Re-examine every factor you write.",
            ),
            mistake(
                "Using product $c$ instead of product $ac$ when the leading coefficient is not 1.",
                "For $6x^2 + 19x + 10$ the product is $6 \\times 10 = 60$, not $10$. Using $10$ "
                "gives no pair summing to $19$ and makes a factorable expression look prime.",
            ),
        ],
        try_it=[
            problem(
                "im2-u2-l4-t1",
                "Factor completely: $5x^{3} - 45x$.",
                "Common factor $5x$: $5x(x^{2} - 9)$. The bracket is a difference of squares, so "
                "$5x(x + 3)(x - 3)$. Check at $x = 2$: $40 - 90 = -50$, and "
                "$5 \\times 2 \\times 5 \\times (-1) = -50$ ✓",
                [
                    "Eq(5*2**3 - 45*2, -50)",
                    "Eq(5*2*(2 + 3)*(2 - 3), -50)",
                    "Eq(5*1**3 - 45*1, 5*1*(1 + 3)*(1 - 3))",
                ],
            ),
            problem(
                "im2-u2-l4-t2",
                "Factor $4x^{2} - 4x - 15$.",
                "$ac = 4 \\times (-15) = -60$, sum $-4$. Opposite signs; $6$ and $-10$ give "
                "$-60$ and $-4$ ✓ Split: $4x^{2} + 6x - 10x - 15 = 2x(2x + 3) - 5(2x + 3) = "
                "(2x + 3)(2x - 5)$. Check at $x = 1$: $4 - 4 - 15 = -15$, and $5 \\times (-3) = "
                "-15$ ✓",
                [
                    "Eq(6*(-10), -60)",
                    "Eq(6 + (-10), -4)",
                    "Eq(4*1**2 - 4*1 - 15, -15)",
                    "Eq((2*1 + 3)*(2*1 - 5), -15)",
                    "Eq((2*3 + 3)*(2*3 - 5), 4*3**2 - 4*3 - 15)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "A-SSE.2",
                "title": "Look at the shape before you search",
                "body": (
                    "Two terms with a minus between two squares? One line. Three terms with square "
                    "ends and the right middle? One line. Anything else? Do the work. Reading the "
                    "shape first is what separates fast factoring from slow factoring."
                ),
                "beats": [
                    "$a^{2} - b^{2} \\to (a+b)(a-b)$",
                    "$a^{2} + 2ab + b^{2} \\to (a+b)^{2}$",
                    "$a^{2} + b^{2} \\to$ prime",
                    "Otherwise: sum-and-product, or ac",
                ],
            },
            {
                "kind": "worked",
                "title": "Difference of squares, once and twice",
                "problemId": "im2-u2-l4-we1",
            },
            tap(
                "Which one is prime?",
                "Which of these does NOT factor over the real numbers?",
                ["$x^{2} - 36$", "$x^{2} + 36$", "$4x^{2} - 9$", "$x^{2} - 1$"],
                1,
                "A DIFFERENCE of squares always factors; a SUM of squares never does over the "
                "reals. $x^{2} + 36$ is prime — you will factor it in Unit 4 using complex "
                "numbers.",
                [
                    "Eq((3 + 6)*(3 - 6), 3**2 - 36)",
                    "Eq((2*3 + 3)*(2*3 - 3), 4*3**2 - 9)",
                    "Ne(3**2 + 36, (3 + 6)*(3 - 6))",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "The middle-term test",
                "title": "Square ends are not enough",
                "body": (
                    "A perfect-square trinomial needs BOTH square ends AND a middle term of "
                    "exactly $2ab$. $x^{2} + 12x + 36$ passes; $x^{2} + 13x + 36$ has the same "
                    "ends and fails. Always compute $2ab$ and compare."
                ),
            },
            {
                "kind": "worked",
                "title": "Two trinomials that look alike",
                "problemId": "im2-u2-l4-we2",
            },
            {
                "kind": "algebraTiles",
                "eyebrow": "Why it is called a square",
                "title": "The tiles form an actual square",
                "teach": (
                    "$x^{2} + 12x + 36$ lays out as one $x^{2}$ tile, twelve $x$-strips and "
                    "thirty-six units — and they assemble into a square of side $x + 6$. The six "
                    "strips along each of two sides are where the $12x$ comes from."
                ),
                "config": {"x": 6, "units": 9, "mode": "build", "maxX": 12, "maxUnits": 36},
            },
            {
                "kind": "teach",
                "eyebrow": "When $a \\neq 1$",
                "title": "The ac-method: split, then group",
                "body": (
                    "Find two numbers with product $ac$ and sum $b$, split the middle term into "
                    "those two pieces, and group. The brackets are guaranteed to match, because "
                    "splitting the middle term undoes the collection step of the forward "
                    "multiplication."
                ),
            },
            {"kind": "worked", "title": "The ac-method in full", "problemId": "im2-u2-l4-we3"},
            tap(
                "What product do you need?",
                "To factor $10x^{2} - 11x - 6$ by the ac-method, which two numbers do you look "
                "for?",
                [
                    "product $-6$, sum $-11$",
                    "product $-60$, sum $-11$",
                    "product $60$, sum $-11$",
                    "product $10$, sum $-6$",
                ],
                1,
                "$ac = 10 \\times (-6) = -60$ and $b = -11$. The pair is $4$ and $-15$: "
                "$4 \\times (-15) = -60$ and $4 + (-15) = -11$ ✓",
                [
                    "Eq(10*(-6), -60)",
                    "Eq(4*(-15), -60)",
                    "Eq(4 + (-15), -11)",
                ],
            ),
            {
                "kind": "tip",
                "eyebrow": "Before you write the final answer",
                "title": "Three questions, every time",
                "body": (
                    "Look at each factor you have written and ask: common factor left? difference "
                    "of squares? factorable trinomial? Only when all three answers are no is the "
                    "expression completely factored."
                ),
            },
            {
                "kind": "worked",
                "title": "GCF first, then the pattern",
                "problemId": "im2-u2-l4-we4",
            },
            {"kind": "tryIt", "title": "Common factor plus a square difference", "problemId": "im2-u2-l4-t1"},
            {"kind": "tryIt", "title": "ac-method with a negative constant", "problemId": "im2-u2-l4-t2"},
            {
                "kind": "recap",
                "title": "What to carry forward",
                "points": [
                    "$a^{2} - b^{2} = (a + b)(a - b)$; a sum of squares is prime over the reals",
                    "Perfect square needs square ends AND middle exactly $2ab$",
                    "$a \\neq 1$: product $ac$, sum $b$, split the middle term, group",
                    "Common factor first — it often reveals the pattern underneath",
                    "Completely factored means no factor can still be broken down",
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
            "im2-u2-p1",
            "Write $8 - x^{3} + 5x^{2}$ in standard form and state the degree and leading "
            "coefficient.",
            "Descending powers: $-x^{3} + 5x^{2} + 8$. Degree $3$, leading coefficient $-1$ (the "
            "sign belongs to the coefficient), constant term $8$. Check at $x = 2$: "
            "$8 - 8 + 20 = 20$, and $-8 + 20 + 8 = 20$ ✓",
            [
                "Eq(8 - 2**3 + 5*2**2, 20)",
                "Eq(-2**3 + 5*2**2 + 8, 20)",
                "Eq(8 - 3**3 + 5*3**2, -3**3 + 5*3**2 + 8)",
            ],
        ),
        problem(
            "im2-u2-p2",
            "Simplify $(6x^{2} - x + 3) + (2x^{2} + 7x - 10)$.",
            "Combine like terms: $(6 + 2)x^{2} + (-1 + 7)x + (3 - 10) = 8x^{2} + 6x - 7$. Check at "
            "$x = 1$: $(6 - 1 + 3) + (2 + 7 - 10) = 8 + (-1) = 7$, and $8 + 6 - 7 = 7$ ✓",
            [
                "Eq(6*1**2 - 1 + 3, 8)",
                "Eq(2*1**2 + 7*1 - 10, -1)",
                "Eq(8*1**2 + 6*1 - 7, 7)",
            ],
        ),
        problem(
            "im2-u2-p3",
            "Simplify $(5x^{2} + 2x - 8) - (3x^{2} - 6x + 1)$.",
            "Distribute the minus over all three terms: $5x^{2} + 2x - 8 - 3x^{2} + 6x - 1$. "
            "Combine: $2x^{2} + 8x - 9$. Check at $x = 1$: $(5 + 2 - 8) - (3 - 6 + 1) = "
            "-1 - (-2) = 1$, and $2 + 8 - 9 = 1$ ✓",
            [
                "Eq(5*1**2 + 2*1 - 8, -1)",
                "Eq(3*1**2 - 6*1 + 1, -2)",
                "Eq(2*1**2 + 8*1 - 9, 1)",
                "Eq(5*2**2 + 2*2 - 8 - (3*2**2 - 6*2 + 1), 2*2**2 + 8*2 - 9)",
            ],
        ),
        problem(
            "im2-u2-p4",
            "Expand $(x + 6)(x - 2)$.",
            "$x^{2} - 2x + 6x - 12 = x^{2} + 4x - 12$. The middle coefficient is $6 + (-2) = 4$ "
            "and the constant is $6 \\times (-2) = -12$. Check at $x = 3$: $9 \\times 1 = 9$, and "
            "$9 + 12 - 12 = 9$ ✓",
            [
                "Eq((3 + 6)*(3 - 2), 9)",
                "Eq(3**2 + 4*3 - 12, 9)",
                "Eq(6*(-2), -12)",
                "Eq(6 + (-2), 4)",
            ],
        ),
        problem(
            "im2-u2-p5",
            "Expand $(2x - 5)(3x + 4)$.",
            "Four products: $6x^{2} + 8x - 15x - 20 = 6x^{2} - 7x - 20$. Check at $x = 1$: "
            "$(-3)(7) = -21$, and $6 - 7 - 20 = -21$ ✓ The degree is $1 + 1 = 2$, as expected.",
            [
                "Eq((2*1 - 5)*(3*1 + 4), -21)",
                "Eq(6*1**2 - 7*1 - 20, -21)",
                "Eq((2*2 - 5)*(3*2 + 4), 6*2**2 - 7*2 - 20)",
            ],
        ),
        problem(
            "im2-u2-p6",
            "Expand $(x - 3)(x^{2} + 2x - 5)$.",
            "Six products. From $x$: $x^{3} + 2x^{2} - 5x$. From $-3$: $-3x^{2} - 6x + 15$. "
            "Combine: $x^{3} - x^{2} - 11x + 15$. Check at $x = 1$: $(-2)(1 + 2 - 5) = "
            "(-2)(-2) = 4$, and $1 - 1 - 11 + 15 = 4$ ✓",
            [
                "Eq((1 - 3)*(1**2 + 2*1 - 5), 4)",
                "Eq(1**3 - 1**2 - 11*1 + 15, 4)",
                "Eq((2 - 3)*(2**2 + 2*2 - 5), 2**3 - 2**2 - 11*2 + 15)",
            ],
        ),
        problem(
            "im2-u2-p7",
            "Expand $(4x + 3)^{2}$ and $(4x + 3)(4x - 3)$, and compare the results.",
            "Square: $16x^{2} + 12x + 12x + 9 = 16x^{2} + 24x + 9$. Difference of squares: the "
            "cross terms cancel, giving $16x^{2} - 9$. The two differ by $24x + 18$ — everything "
            "the cancellation removed. Check at $x = 1$: $49$ versus $7$, and "
            "$49 - 7 = 42 = 24 + 18$ ✓",
            [
                "Eq((4*1 + 3)**2, 49)",
                "Eq(16*1**2 + 24*1 + 9, 49)",
                "Eq((4*1 + 3)*(4*1 - 3), 7)",
                "Eq(16*1**2 - 9, 7)",
                "Eq(49 - 7, 24*1 + 18)",
            ],
        ),
        problem(
            "im2-u2-p8",
            "Factor completely: $14x^{3} + 21x^{2} - 35x$.",
            "The coefficients share $7$ and the lowest power of $x$ present is $x$, so pull out "
            "$7x$: $7x(2x^{2} + 3x - 5)$. The bracket factors too — $ac = -10$, sum $3$, giving "
            "$5$ and $-2$: $2x^{2} + 5x - 2x - 5 = x(2x + 5) - (2x + 5) = (2x + 5)(x - 1)$. So "
            "the answer is $7x(2x + 5)(x - 1)$. Check at $x = 2$: $112 + 84 - 70 = 126$, and "
            "$14 \\times 9 \\times 1 = 126$ ✓",
            [
                "Eq(14*2**3 + 21*2**2 - 35*2, 126)",
                "Eq(7*2*(2*2 + 5)*(2 - 1), 126)",
                "Eq(5*(-2), -10)",
                "Eq(5 + (-2), 3)",
            ],
        ),
        problem(
            "im2-u2-p9",
            "Factor $x^{2} - 3x - 40$.",
            "Product $-40$, sum $-3$. Opposite signs with the larger negative: $5$ and $-8$. So "
            "$(x + 5)(x - 8)$. Check: it should vanish at $x = -5$ and $x = 8$ — "
            "$25 + 15 - 40 = 0$ ✓ and $64 - 24 - 40 = 0$ ✓",
            [
                "Eq(5*(-8), -40)",
                "Eq(5 + (-8), -3)",
                "Eq((-5)**2 - 3*(-5) - 40, 0)",
                "Eq(8**2 - 3*8 - 40, 0)",
            ],
        ),
        problem(
            "im2-u2-p10",
            "Factor $9x^{2} - 64$ and $9x^{2} + 64$.",
            "The first is a difference of squares: $(3x)^{2} - 8^{2} = (3x + 8)(3x - 8)$. The "
            "second is a SUM of squares and does not factor over the reals — it is prime. Check "
            "the first at $x = 3$: $81 - 64 = 17$, and $(9 + 8)(9 - 8) = 17 \\times 1 = 17$ ✓",
            [
                "Eq(9*3**2 - 64, 17)",
                "Eq((3*3 + 8)*(3*3 - 8), 17)",
                "Eq(9*1**2 + 64, 73)",
                "Ne(9*1**2 + 64, (3*1 + 8)*(3*1 - 8))",
            ],
        ),
        problem(
            "im2-u2-p11",
            "Factor $x^{3} + 6x^{2} - 4x - 24$ by grouping.",
            "Pair: $(x^{3} + 6x^{2}) + (-4x - 24) = x^{2}(x + 6) - 4(x + 6) = (x + 6)(x^{2} - 4)$. "
            "The second factor is a difference of squares, so continue: "
            "$(x + 6)(x + 2)(x - 2)$. Check at $x = 1$: $1 + 6 - 4 - 24 = -21$, and "
            "$7 \\times 3 \\times (-1) = -21$ ✓ Stopping at $(x + 6)(x^{2} - 4)$ would have been "
            "incomplete.",
            [
                "Eq(1**3 + 6*1**2 - 4*1 - 24, -21)",
                "Eq((1 + 6)*(1 + 2)*(1 - 2), -21)",
                "Eq(2**3 + 6*2**2 - 4*2 - 24, 0)",
                "Eq((-6)**3 + 6*(-6)**2 - 4*(-6) - 24, 0)",
            ],
        ),
        problem(
            "im2-u2-p12",
            "Factor $12x^{2} + 11x - 5$.",
            "$ac = 12 \\times (-5) = -60$, sum $11$. Opposite signs with the larger positive: "
            "$15$ and $-4$. Split: $12x^{2} + 15x - 4x - 5 = 3x(4x + 5) - (4x + 5) = "
            "(4x + 5)(3x - 1)$. Check at $x = 1$: $12 + 11 - 5 = 18$, and $9 \\times 2 = 18$ ✓",
            [
                "Eq(15*(-4), -60)",
                "Eq(15 + (-4), 11)",
                "Eq(12*1**2 + 11*1 - 5, 18)",
                "Eq((4*1 + 5)*(3*1 - 1), 18)",
            ],
        ),
    ]


def test_bank():
    return [
        problem(
            "im2-u2-ty-1",
            "Simplify completely: $(3x^{3} - x + 4) - (x^{3} + 2x^{2} - x - 6)$. State the degree "
            "of the result.",
            "**Distribute the minus across all four terms.**"
            "$$3x^{3} - x + 4 - x^{3} - 2x^{2} + x + 6.$$"
            "Both the $-x$ and the $-6$ changed sign."
            "**Combine like terms.** The $x$ terms cancel entirely:"
            "$$2x^{3} - 2x^{2} + 10.$$"
            "**The degree is three**, with leading coefficient $2$."
            "**Check the answer.** At $x = 2$: First: $24 - 2 + 4 = 26$. Second: $8 + 8 - 2 - 6 = 8$. "
            "Difference $18$. The answer: $16 - 8 + 10 = 18$ ✓",
            [
                "Eq(3*2**3 - 2 + 4, 26)",
                "Eq(2**3 + 2*2**2 - 2 - 6, 8)",
                "Eq(26 - 8, 18)",
                "Eq(2*2**3 - 2*2**2 + 10, 18)",
                "Eq(3*1**3 - 1 + 4 - (1**3 + 2*1**2 - 1 - 6), 2*1**3 - 2*1**2 + 10)",
            ],
        ),
        problem(
            "im2-u2-ty-2",
            "Expand $(2x + 1)(x^{2} - 3x + 4)$ and confirm the degree of the answer.",
            "**Count first.** Two terms times three terms gives six products; the degree should be "
            "$1 + 2 = 3$."
            "**Distribute the leading term.**"
            "$$2x^{3} - 6x^{2} + 8x.$$"
            "**Distribute the constant term.**"
            "$$x^{2} - 3x + 4.$$"
            "**Combine.**"
            "$$2x^{3} + (-6 + 1)x^{2} + (8 - 3)x + 4 = 2x^{3} - 5x^{2} + 5x + 4.$$"
            "Degree $3$ ✓ as predicted."
            "**Check the answer.** At $x = 1$: $(3)(1 - 3 + 4) = 3 \\times 2 = 6$, and "
            "$2 - 5 + 5 + 4 = 6$ ✓",
            [
                "Eq((2*1 + 1)*(1**2 - 3*1 + 4), 6)",
                "Eq(2*1**3 - 5*1**2 + 5*1 + 4, 6)",
                "Eq((2*2 + 1)*(2**2 - 3*2 + 4), 2*2**3 - 5*2**2 + 5*2 + 4)",
                "Eq((2*(-1) + 1)*((-1)**2 - 3*(-1) + 4), 2*(-1)**3 - 5*(-1)**2 + 5*(-1) + 4)",
            ],
        ),
        problem(
            "im2-u2-ty-3",
            "Expand $(x - 5)^{2}$ and $(x - 5)(x + 5)$, then explain in one sentence why the "
            "answers differ.",
            "**The square.**"
            "$$(x - 5)(x - 5) = x^{2} - 5x - 5x + 25 = x^{2} - 10x + 25.$$"
            "**The difference of squares.**"
            "$$(x - 5)(x + 5) = x^{2} + 5x - 5x - 25 = x^{2} - 25.$$"
            "**Why they differ.** In the square the two cross terms are both $-5x$, so they ADD "
            "to $-10x$; in the second the cross terms are $+5x$ and $-5x$, so they CANCEL. The "
            "sign pattern of the brackets decides whether the middle survives."
            "**Check the answer.** At $x = 2$: $(-3)^{2} = 9$, and $4 - 20 + 25 = 9$ ✓. Also "
            "$(-3)(7) = -21$, and $4 - 25 = -21$ ✓",
            [
                "Eq((2 - 5)**2, 9)",
                "Eq(2**2 - 10*2 + 25, 9)",
                "Eq((2 - 5)*(2 + 5), -21)",
                "Eq(2**2 - 25, -21)",
                "Eq((3 - 5)**2 - (3 - 5)*(3 + 5), -10*3 + 25 + 25)",
            ],
        ),
        problem(
            "im2-u2-ty-4",
            "Factor completely: $4x^{3} - 100x$.",
            "**Common factor first.** Both terms contain $4x$:"
            "$$4x^{3} - 100x = 4x(x^{2} - 25).$$"
            "**Examine the bracket.** $x^{2} - 25 = x^{2} - 5^{2}$, a difference of squares:"
            "$$4x(x + 5)(x - 5).$$"
            "**Check every factor once more.** $4x$ is a monomial, $(x + 5)$ and $(x - 5)$ are "
            "linear — nothing left to break down. The factorisation is complete."
            "**A numerical check.** At $x = 3$: $108 - 300 = -192$, and "
            "$12 \\times 8 \\times (-2) = -192$ ✓"
            "**A note on what the answer tells you.** The expression is zero at $x = 0$, $x = 5$ "
            "and $x = -5$ — three roots for a degree-3 polynomial, which is the most it can have.",
            [
                "Eq(4*3**3 - 100*3, -192)",
                "Eq(4*3*(3 + 5)*(3 - 5), -192)",
                "Eq(4*5**3 - 100*5, 0)",
                "Eq(4*(-5)**3 - 100*(-5), 0)",
                "Eq(4*0**3 - 100*0, 0)",
            ],
        ),
        problem(
            "im2-u2-ty-5",
            "Factor $x^{2} - 14x + 45$, and state the values of $x$ that make it zero.",
            "**Read the signs.** The constant $45$ is positive so both numbers share a sign; the "
            "middle $-14$ is negative so both are negative."
            "**Search the negative pairs with product 45.**"
            "$$-1 + (-45) = -46, \\quad -3 + (-15) = -18, \\quad -5 + (-9) = -14 \\ \\checkmark$$"
            "**Write the factorisation.**"
            "$$x^{2} - 14x + 45 = (x - 5)(x - 9).$$"
            "**Read off the zeros.** A product is zero exactly when one factor is zero, so the "
            "expression vanishes at $x = 5$ and $x = 9$."
            "**Verify both.** $25 - 70 + 45 = 0$ ✓ and $81 - 126 + 45 = 0$ ✓ — the factorisation "
            "is correct and the zeros are exact.",
            [
                "Eq((-5)*(-9), 45)",
                "Eq(-5 + (-9), -14)",
                "Eq(5**2 - 14*5 + 45, 0)",
                "Eq(9**2 - 14*9 + 45, 0)",
                "Eq(-3 + (-15), -18)",
            ],
        ),
        problem(
            "im2-u2-ty-6",
            "Factor $6x^{2} - 7x - 3$ using the ac-method, showing the split.",
            "**Compute the ac product.** $a = 6$, $c = -3$, so $ac = -18$, and the sum must be $-7$."
            "**Find the pair.** The product is negative so the signs are opposite; the sum is "
            "negative so the larger is negative:"
            "$$2 \\times (-9) = -18, \\quad 2 + (-9) = -7 \\ \\checkmark$$"
            "**Split the middle term.**"
            "$$6x^{2} + 2x - 9x - 3.$$"
            "**Group and factor each pair.**"
            "$$2x(3x + 1) - 3(3x + 1) = (3x + 1)(2x - 3).$$"
            "The $-3$ had to be pulled out of the second pair — factoring out a positive $3$ would "
            "have left $(-3x - 1)$ and the brackets would not have matched."
            "**Check the answer.** At $x = 2$: $24 - 14 - 3 = 7$, and $(6 + 1)(4 - 3) = 7 \\times 1 = 7$ ✓",
            [
                "Eq(6*(-3), -18)",
                "Eq(2*(-9), -18)",
                "Eq(2 + (-9), -7)",
                "Eq(6*2**2 - 7*2 - 3, 7)",
                "Eq((3*2 + 1)*(2*2 - 3), 7)",
            ],
        ),
        problem(
            "im2-u2-ty-7",
            "A rectangular garden is $x$ metres wide and $(x + 7)$ metres long. A path $2$ metres "
            "wide is added along the two longer sides only, so the width grows by $4$ metres. "
            "Write the new area as a polynomial in standard form, and find how much larger it is "
            "than the original.",
            "**Write the original area.**"
            "$$A_{\\text{old}} = x(x + 7) = x^{2} + 7x.$$"
            "**Write the new dimensions.** The width grows from $x$ to $x + 4$; the length is "
            "unchanged at $x + 7$:"
            "$$A_{\\text{new}} = (x + 4)(x + 7) = x^{2} + 11x + 28.$$"
            "**Subtract to find the increase.**"
            "$$A_{\\text{new}} - A_{\\text{old}} = (x^{2} + 11x + 28) - (x^{2} + 7x) = 4x + 28.$$"
            "**Sanity-check the answer's shape.** The added region is a $4$-metre strip of length "
            "$x + 7$, whose area is $4(x + 7) = 4x + 28$ ✓ — the algebra and the geometry agree, "
            "which is the real confirmation."
            "**A numerical check.** At $x = 6$: Old area $6 \\times 13 = 78$; new area "
            "$10 \\times 13 = 130$; increase $52$. And $4(6) + 28 = 52$ ✓",
            [
                "Eq(6*(6 + 7), 78)",
                "Eq((6 + 4)*(6 + 7), 130)",
                "Eq(130 - 78, 52)",
                "Eq(4*6 + 28, 52)",
                "Eq(4*(6 + 7), 52)",
                "Eq((9 + 4)*(9 + 7), 9**2 + 11*9 + 28)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="polynomials-and-factoring",
        title="Polynomials & Factoring",
        unit_number=2,
        blurb=(
            "Polynomials as a number system closed under addition, subtraction and "
            "multiplication; multiplying by distributing every term over every term; and every "
            "factoring technique from a common factor through the ac-method, each introduced as "
            "the multiplication that produced it, read backwards."
        ),
        builds_on=(
            "The structure of expressions from IM1 Unit 1 — the same distributive property, now "
            "applied to whole brackets rather than single terms."
        ),
        lessons=[
            lesson_polynomial_system(),
            lesson_multiplying(),
            lesson_factoring_basics(),
            lesson_special_factoring(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
