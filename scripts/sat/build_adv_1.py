#!/usr/bin/env python3
"""SAT Math — Advanced Math, Unit 1: Equivalent expressions.

Builds data/genmath/sat/equivalent-expressions.json. Three lessons: exponent
and radical rules, polynomial arithmetic and factoring, rational expressions.
"Which of the following is equivalent to" is the single most common stem in
this domain.

Run: python3 scripts/sat/build_adv_1.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
UNIT_SLUG = "equivalent-expressions"
TAG = {"text": "sat-equivalent-expressions", "mono": True}


def _b(level):
    return [TAG, {"text": level}]


# ===========================================================================
# Lesson 1 — exponents and radicals
# ===========================================================================

def lesson_exponents():
    worked = [
        problem(
            "sat-ae1-w1",
            "Which expression is equivalent to $\\dfrac{(2x^{3})^{4}}{4x^{5}}$ for $x \\ne 0$?",
            "**Answer.** $4x^{7}$.  \n"
            "Handle the power of a product first. The outer exponent hits EVERY factor inside "
            "the brackets, including the $2$:\n"
            "$$(2x^{3})^{4} = 2^{4}\\,(x^{3})^{4} = 16x^{12}$$\n"
            "Note $(x^{3})^{4} = x^{12}$ — a power of a power MULTIPLIES the exponents.\n"
            "$$\\frac{16x^{12}}{4x^{5}}$$\n"
            "Now divide the coefficients and subtract the exponents:\n"
            "$$= 4x^{7}$$\n"
            "Check with $x = 2$: the original is $\\frac{(16)^{4}}{4 \\cdot 32} = "
            "\\frac{65536}{128} = 512$, and $4 \\cdot 2^{7} = 512$.  \n"
            "The two traps: leaving the $2$ un-powered gives $\\frac{2x^{12}}{4x^{5}}$, and "
            "ADDING the exponents inside gives $x^{7}$ in the numerator. Both appear as "
            "options.",
            [
                "Eq(simplify((2*x**3)**4 / (4*x**5) - 4*x**7), 0)",
                "Eq((2*2**3)**4 / (4*2**5), 512)",
                "Eq(4*2**7, 512)",
            ],
        ),
        problem(
            "sat-ae1-w2",
            "Which expression is equivalent to $\\sqrt[3]{x^{5}} \\cdot \\sqrt{x}$ for "
            "$x > 0$?",
            "**Answer.** $x^{13/6}$.  \n"
            "Rewrite both radicals as fractional exponents — the root goes in the denominator "
            "of the exponent, the power in the numerator:\n"
            "$$\\sqrt[3]{x^{5}} = x^{5/3}, \\qquad \\sqrt{x} = x^{1/2}$$\n"
            "Multiplying powers of the same base ADDS the exponents:\n"
            "$$x^{5/3} \\cdot x^{1/2} = x^{5/3 + 1/2}$$\n"
            "$$\\frac{5}{3} + \\frac{1}{2} = \\frac{10}{6} + \\frac{3}{6} = \\frac{13}{6}$$\n"
            "$$= x^{13/6}$$\n"
            "Check with $x = 64$: $\\sqrt[3]{64^{5}} = 4^{5} = 1024$ and $\\sqrt{64} = 8$, so "
            "the product is $8192$; and $64^{13/6} = 2^{13} = 8192$.  \n"
            "The reflex error is multiplying the exponents instead of adding them. "
            "Multiplication of powers adds; a power of a power multiplies.",
            [
                "Eq(Rational(5,3) + Rational(1,2), Rational(13,6))",
                "Eq(64**Rational(5,3) * 64**Rational(1,2), 8192)",
                "Eq(64**Rational(13,6), 8192)",
            ],
        ),
        problem(
            "sat-ae1-w3",
            "Which expression is equivalent to $\\left(\\dfrac{9a^{6}}{b^{-2}}\\right)^{1/2}$ "
            "for $a > 0$ and $b > 0$?",
            "**Answer.** $3a^{3}b$.  \n"
            "Clear the negative exponent first. A negative exponent in the DENOMINATOR moves "
            "up to the numerator and turns positive:\n"
            "$$\\frac{9a^{6}}{b^{-2}} = 9a^{6}b^{2}$$\n"
            "Now apply the outer $\\frac{1}{2}$ power to each factor, multiplying exponents:\n"
            "$$(9)^{1/2}\\,(a^{6})^{1/2}\\,(b^{2})^{1/2} = 3a^{3}b$$\n"
            "Check with $a = 2$, $b = 5$: inside the brackets is "
            "$\\frac{9 \\cdot 64}{1/25} = 14400$, and $\\sqrt{14400} = 120$; the answer gives "
            "$3 \\cdot 8 \\cdot 5 = 120$.  \n"
            "A negative exponent never means a negative number — it means a reciprocal. "
            "$b^{-2}$ is $\\frac{1}{b^{2}}$, so dividing by it multiplies by $b^{2}$.",
            [
                "Eq(simplify((9*Symbol('a',positive=True)**6/Symbol('b',positive=True)**(-2))**Rational(1,2) - 3*Symbol('a',positive=True)**3*Symbol('b',positive=True)), 0)",
                "Eq((9*2**6/5**(-2))**Rational(1,2), 120)",
                "Eq(3*2**3*5, 120)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ae1-t1",
            "Which expression is equivalent to $(3x^{2})^{3}$?",
            "**Answer.** $27x^{6}$. The outer exponent reaches the $3$ as well: "
            "$3^{3} = 27$, and $(x^{2})^{3} = x^{6}$.",
            ["Eq(simplify((3*x**2)**3 - 27*x**6), 0)", "Eq((3*2**2)**3, 27*2**6)"],
        ),
        problem(
            "sat-ae1-t2",
            "Which expression is equivalent to $\\dfrac{x^{9}y^{2}}{x^{4}y^{5}}$ for "
            "$x \\ne 0$ and $y \\ne 0$?",
            "**Answer.** $\\dfrac{x^{5}}{y^{3}}$. Subtract exponents for each base: "
            "$x^{9-4} = x^{5}$ and $y^{2-5} = y^{-3}$, and a negative exponent goes to the "
            "denominator.",
            ["Eq(simplify(x**9*y**2/(x**4*y**5) - x**5/y**3), 0)"],
        ),
        problem(
            "sat-ae1-t3",
            "Which expression is equivalent to $\\sqrt{50x^{4}}$ for $x > 0$?",
            "**Answer.** $5x^{2}\\sqrt{2}$. Split the radicand into a perfect square times "
            "what is left: $50 = 25 \\cdot 2$ and $x^{4}$ is already a perfect square. So "
            "$\\sqrt{25} \\cdot \\sqrt{x^{4}} \\cdot \\sqrt{2} = 5x^{2}\\sqrt{2}$.",
            [
                "Eq(simplify(sqrt(50*Symbol('x',positive=True)**4) - 5*Symbol('x',positive=True)**2*sqrt(2)), 0)",
                "Eq(sqrt(50*3**4), 5*3**2*sqrt(2))",
            ],
        ),
        problem(
            "sat-ae1-t4",
            "If $x > 0$, which expression is equivalent to $x^{-1/2}$?",
            "**Answer.** $\\dfrac{1}{\\sqrt{x}}$. The negative sign means reciprocal and the "
            "$\\frac{1}{2}$ means square root. Check with $x = 9$: "
            "$9^{-1/2} = \\frac{1}{3}$.",
            ["Eq(9**Rational(-1,2), Rational(1,3))", "Eq(simplify(Symbol('x',positive=True)**Rational(-1,2) - 1/sqrt(Symbol('x',positive=True))), 0)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Equivalent expressions",
            "beats": [
                "Domain: Advanced Math — 13 to 15 of the 44 questions on the Math section.",
                "'Which of the following is equivalent to' is this domain's commonest stem.",
                "Prerequisite: arithmetic with fractions and negative numbers.",
                "Every one of these is checkable by substituting a number — use that.",
            ],
        },
        {
            "kind": "teach",
            "title": "Five rules, and they never change",
            "beats": [
                "Multiplying powers of the same base ADDS the exponents.",
                "Dividing SUBTRACTS them.",
                "A power of a power MULTIPLIES them.",
                "A negative exponent means a reciprocal, never a negative number.",
                "A fractional exponent is a root: the denominator is the root, the numerator the power.",
            ],
        },
        {
            "kind": "exponentBuilder",
            "title": "Why the rules are what they are",
            "teach": "An exponent is a count of factors. Three copies of x times four copies of "
                     "x is seven copies — that is why multiplying adds. Build the tower and "
                     "watch the count.",
            "config": {"base": 2, "exp": 5, "maxExp": 8},
        },
        {"kind": "worked", "title": "A power of a product", "problemId": "sat-ae1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Add or multiply?",
            "prompt": "Which is equivalent to $(x^{4})^{3} \\cdot x^{2}$?",
            "options": ["$x^{14}$", "$x^{9}$", "$x^{24}$", "$x^{7}$"],
            "correctIndex": 0,
            "explanation": "The power of a power multiplies: $(x^{4})^{3} = x^{12}$. Then "
                           "multiplying by $x^{2}$ adds: $x^{14}$. Option B adds where it "
                           "should multiply, C multiplies where it should add, D adds all "
                           "three exponents.",
            "check": [
                "Eq(simplify((x**4)**3 * x**2 - x**14), 0)",
                "Eq((2**4)**3 * 2**2, 2**14)",
            ],
        },
        {
            "kind": "tip",
            "title": "Substitute a number and check",
            "body": "Every 'which is equivalent to' question can be settled by picking a "
                    "convenient value and evaluating both the original and each option. Use "
                    "$x = 2$ or $x = 3$ — never $0$ or $1$, because those make different "
                    "expressions agree by accident. This is slower than the algebra but it "
                    "cannot go wrong, and on a hard item it is worth the thirty seconds.",
        },
        {"kind": "worked", "title": "Radicals as fractional exponents", "problemId": "sat-ae1-w2"},
        {
            "kind": "teach",
            "title": "Negative exponents are reciprocals",
            "body": "$x^{-3}$ is $\\frac{1}{x^{3}}$, not $-x^{3}$. A negative exponent flips "
                    "the factor across the fraction bar and turns positive: a $b^{-2}$ in the "
                    "DENOMINATOR becomes a $b^{2}$ in the numerator. Nothing about the sign of "
                    "the value changes — $2^{-3} = \\frac{1}{8}$, which is positive.",
        },
        {"kind": "worked", "title": "Clearing a negative exponent", "problemId": "sat-ae1-w3"},
        {"kind": "tryIt", "title": "Your turn: power of a product", "problemId": "sat-ae1-t1"},
        {"kind": "tryIt", "title": "Your turn: divide two bases", "problemId": "sat-ae1-t2"},
        {"kind": "tryIt", "title": "Your turn: simplify a radical", "problemId": "sat-ae1-t3"},
        {"kind": "tryIt", "title": "Your turn: a negative fractional exponent", "problemId": "sat-ae1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Multiply powers: add exponents. Divide: subtract. Power of a power: multiply.",
                "An outer exponent reaches every factor inside the brackets, coefficients included.",
                "A negative exponent is a reciprocal — it never makes the value negative.",
                "A fractional exponent is a root over a power: the denominator is the root.",
                "When in doubt, substitute x = 2 or 3 into the original and into each option.",
            ],
        },
    ]

    return lesson(
        slug="exponents-and-radicals",
        title="Exponent and Radical Rules",
        concrete=(
            "A sheet of paper folded $n$ times has $2^{n}$ layers. Fold it seven more times "
            "and you do not add seven layers — you multiply by $2^{7}$. Exponent rules are the "
            "bookkeeping for that kind of growth, and the SAT tests whether you can do the "
            "bookkeeping without thinking about it."
        ),
        objective=(
            "Simplify expressions with integer, negative and fractional exponents, convert "
            "between radical and exponent notation, and recognise equivalent forms."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Equivalent expressions*, in the "
            "**Advanced Math** domain — 13 to 15 of the 44 questions, tied with Algebra as the "
            "largest domain. 'Which of the following is equivalent to' is its commonest stem, "
            "and exponent rules are where those questions start.",
            "Five rules cover almost everything. Multiplying powers of the same base ADDS the "
            "exponents. Dividing SUBTRACTS them. A power of a power MULTIPLIES them. A "
            "negative exponent means a reciprocal. A fractional exponent is a root, with the "
            "denominator naming the root and the numerator the power.",
            "The rule people break most often is the outer exponent's reach. In $(2x^{3})^{4}$ "
            "the $4$ applies to the $2$ as well as to the $x^{3}$, giving $16x^{12}$ — not "
            "$2x^{12}$. Everything inside the brackets is a factor, and every factor gets the "
            "power.",
            "**The test's angle.** These items are always checkable. Pick a convenient value — "
            "$x = 2$ or $x = 3$, never $0$ or $1$ — and evaluate the original and each option. "
            "It takes longer than the algebra but it is immune to the sign and exponent slips "
            "the distractors are built from, and on a hard item that trade is worth making.",
        ],
        key_idea=(
            "Add exponents to multiply, subtract to divide, multiply for a power of a power. "
            "A negative exponent is a reciprocal and a fractional one is a root — and the "
            "outer power reaches every factor in the brackets."
        ),
        facts=[
            fact(
                "The product and quotient rules",
                "x^{a} \\cdot x^{b} = x^{a+b}, \\qquad \\frac{x^{a}}{x^{b}} = x^{a-b}",
                "Same base only. $x^{2} \\cdot y^{3}$ combines into nothing.",
            ),
            fact(
                "Power of a power, power of a product",
                "(x^{a})^{b} = x^{ab}, \\qquad (cx)^{n} = c^{n}x^{n}",
                "The outer exponent reaches every factor inside, coefficients included.",
            ),
            fact(
                "Negative and fractional exponents",
                "x^{-n} = \\frac{1}{x^{n}}, \\qquad x^{m/n} = \\sqrt[n]{x^{m}}",
                "Negative means reciprocal; the denominator of a fractional exponent is the "
                "root.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Leaving the coefficient un-powered in $(2x^{3})^{4}$.",
                "The $4$ applies to the $2$ too: $2^{4}x^{12} = 16x^{12}$.",
            ),
            mistake(
                "Multiplying exponents when multiplying powers.",
                "$x^{3} \\cdot x^{4} = x^{7}$, not $x^{12}$. Multiplication adds; a power of a "
                "power multiplies.",
            ),
            mistake(
                "Reading $x^{-2}$ as a negative quantity.",
                "It is $\\frac{1}{x^{2}}$, which is positive whenever $x$ is real and non-zero.",
            ),
            mistake(
                "Inverting a fractional exponent: reading $x^{2/3}$ as the square root of "
                "$x^{3}$.",
                "The DENOMINATOR is the root: $x^{2/3} = \\sqrt[3]{x^{2}}$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 2 — polynomials and factoring
# ===========================================================================

def lesson_polynomials():
    worked = [
        problem(
            "sat-ae2-w1",
            "Which expression is equivalent to $(2x - 5)(3x + 4)$?",
            "**Answer.** $6x^{2} - 7x - 20$.  \n"
            "Multiply every term in the first bracket by every term in the second:\n"
            "$$2x \\cdot 3x = 6x^{2}$$\n"
            "$$2x \\cdot 4 = 8x$$\n"
            "$$-5 \\cdot 3x = -15x$$\n"
            "$$-5 \\cdot 4 = -20$$\n"
            "Collect the two middle terms:\n"
            "$$6x^{2} + 8x - 15x - 20 = 6x^{2} - 7x - 20$$\n"
            "Check with $x = 1$: the original is $(-3)(7) = -21$, and "
            "$6 - 7 - 20 = -21$.  \n"
            "The middle coefficient is where the points go. $8x - 15x$ is $-7x$; treating the "
            "$-5$ as a $5$ gives $+23x$, and both signs of the middle term appear in the "
            "options.",
            [
                "Eq(expand((2*x - 5)*(3*x + 4)), 6*x**2 - 7*x - 20)",
                "Eq((2*1 - 5)*(3*1 + 4), -21)",
                "Eq(6 - 7 - 20, -21)",
            ],
        ),
        problem(
            "sat-ae2-w2",
            "Which expression is equivalent to $9x^{2} - 49$?",
            "**Answer.** $(3x - 7)(3x + 7)$.  \n"
            "Both terms are perfect squares and they are SUBTRACTED, which is the signature of "
            "a difference of squares:\n"
            "$$9x^{2} = (3x)^{2}, \\qquad 49 = 7^{2}$$\n"
            "$$a^{2} - b^{2} = (a - b)(a + b)$$\n"
            "$$9x^{2} - 49 = (3x - 7)(3x + 7)$$\n"
            "Check by expanding: $9x^{2} + 21x - 21x - 49 = 9x^{2} - 49$. The middle terms "
            "cancel, which is exactly why the pattern works.  \n"
            "Two things to know. A SUM of squares, $9x^{2} + 49$, does not factor over the "
            "real numbers at all — that is a listed distractor. And $(3x - 7)^{2}$ is "
            "$9x^{2} - 42x + 49$, a different expression entirely.",
            [
                "Eq(expand((3*x - 7)*(3*x + 7)), 9*x**2 - 49)",
                "Eq(expand((3*x - 7)**2), 9*x**2 - 42*x + 49)",
                "Ne(expand((3*x - 7)**2).subs(x, 1), (9*x**2 - 49).subs(x, 1))",
            ],
        ),
        problem(
            "sat-ae2-w3",
            "Which expression is equivalent to $6x^{2} + 5x - 6$?",
            "**Answer.** $(3x - 2)(2x + 3)$.  \n"
            "The leading coefficient is not $1$, so look for two numbers multiplying to "
            "$6 \\times (-6) = -36$ and adding to $5$:\n"
            "$$9 \\times (-4) = -36, \\qquad 9 + (-4) = 5$$\n"
            "Split the middle term using those two numbers and factor in pairs:\n"
            "$$6x^{2} + 9x - 4x - 6$$\n"
            "$$3x(2x + 3) - 2(2x + 3)$$\n"
            "$$(3x - 2)(2x + 3)$$\n"
            "Check by expanding: $6x^{2} + 9x - 4x - 6 = 6x^{2} + 5x - 6$.  \n"
            "On the real test there is a faster route when the options are four factorisations: "
            "expand each and keep the one that matches, or substitute $x = 1$ into the "
            "original ($5$) and into each option, keeping the one that also gives $5$.",
            [
                "Eq(expand((3*x - 2)*(2*x + 3)), 6*x**2 + 5*x - 6)",
                "Eq(6*1 + 5 - 6, 5)",
                "Eq((3*1 - 2)*(2*1 + 3), 5)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ae2-t1",
            "Which expression is equivalent to $(x + 6)(x - 2)$?",
            "**Answer.** $x^{2} + 4x - 12$. The outer and inner products are $-2x$ and $6x$, "
            "summing to $4x$; the last terms give $-12$.",
            ["Eq(expand((x + 6)*(x - 2)), x**2 + 4*x - 12)"],
        ),
        problem(
            "sat-ae2-t2",
            "Which expression is equivalent to $x^{2} - 81$?",
            "**Answer.** $(x - 9)(x + 9)$. A difference of squares: $81 = 9^{2}$.",
            ["Eq(expand((x - 9)*(x + 9)), x**2 - 81)"],
        ),
        problem(
            "sat-ae2-t3",
            "Which expression is equivalent to $4x^{2} + 12x + 9$?",
            "**Answer.** $(2x + 3)^{2}$. Both outer terms are perfect squares — $(2x)^{2}$ and "
            "$3^{2}$ — and the middle term is twice their product: "
            "$2 \\cdot 2x \\cdot 3 = 12x$. That is the perfect-square pattern.",
            ["Eq(expand((2*x + 3)**2), 4*x**2 + 12*x + 9)", "Eq(2*2*3, 12)"],
        ),
        problem(
            "sat-ae2-t4",
            "Which expression is equivalent to $2x^{2} - 7x + 3$?",
            "**Answer.** $(2x - 1)(x - 3)$. Two numbers multiplying to $2 \\times 3 = 6$ and "
            "adding to $-7$ are $-1$ and $-6$: $2x^{2} - x - 6x + 3 = x(2x - 1) - 3(2x - 1)$.",
            ["Eq(expand((2*x - 1)*(x - 3)), 2*x**2 - 7*x + 3)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Expanding is bookkeeping",
            "body": "To multiply two brackets, multiply every term in the first by every term "
                    "in the second and collect. With two terms each that is four products, and "
                    "the two middle ones combine. There is nothing to remember beyond 'every "
                    "term meets every term' — which is also why it extends to longer brackets "
                    "without any new rule.",
        },
        {
            "kind": "algebraTiles",
            "title": "Terms that combine, and terms that do not",
            "teach": "Build an expression out of x-tiles and unit tiles, then collect. Two "
                     "x-tiles and three x-tiles make five; an x-tile and a unit tile never "
                     "merge. That is the whole of 'collect like terms' — and it is why "
                     "expanding leaves an x-squared, an x, and a constant, never fewer.",
            "config": {"x": 4, "units": 6, "mode": "build"},
        },
        {"kind": "worked", "title": "Expanding two brackets", "problemId": "sat-ae2-w1"},
        {
            "kind": "teach",
            "title": "Three patterns worth recognising instantly",
            "beats": [
                "Difference of squares: a² − b² = (a − b)(a + b). Squares, subtracted.",
                "Perfect square: a² + 2ab + b² = (a + b)². The middle is twice the product.",
                "A SUM of squares does not factor over the reals — a common distractor.",
                "Recognising a pattern turns a 90-second factorisation into a 5-second one.",
            ],
        },
        {"kind": "worked", "title": "A difference of squares", "problemId": "sat-ae2-w2"},
        {
            "kind": "tapQuestion",
            "title": "Which pattern is it?",
            "prompt": "Which expression factors as a difference of squares?",
            "options": [
                "$25x^{2} - 16$",
                "$25x^{2} + 16$",
                "$25x^{2} - 16x$",
                "$25x^{3} - 16$",
            ],
            "correctIndex": 0,
            "explanation": "Only A is a perfect square minus a perfect square: "
                           "$(5x)^{2} - 4^{2} = (5x - 4)(5x + 4)$. B is a SUM of squares and "
                           "does not factor over the reals; C factors, but as a common factor "
                           "$x(25x - 16)$; D is a difference of a cube and a square, not of "
                           "two squares.",
            "check": [
                "Eq(expand((5*x - 4)*(5*x + 4)), 25*x**2 - 16)",
                "Eq(factor(25*x**2 - 16*x), x*(25*x - 16))",
            ],
        },
        {
            "kind": "tip",
            "title": "Factor by expanding the options",
            "body": "When the question asks you to factor and gives four factorisations, do "
                    "not factor at all — EXPAND the options, or substitute a value. Putting "
                    "$x = 1$ into $6x^{2} + 5x - 6$ gives $5$; whichever option also gives $5$ "
                    "is almost certainly the answer, and a second value settles any tie. This "
                    "is faster and safer than splitting the middle term.",
        },
        {"kind": "worked", "title": "A leading coefficient greater than one", "problemId": "sat-ae2-w3"},
        {"kind": "tryIt", "title": "Your turn: expand", "problemId": "sat-ae2-t1"},
        {"kind": "tryIt", "title": "Your turn: spot the pattern", "problemId": "sat-ae2-t2"},
        {"kind": "tryIt", "title": "Your turn: a perfect square", "problemId": "sat-ae2-t3"},
        {"kind": "tryIt", "title": "Your turn: split the middle term", "problemId": "sat-ae2-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Expanding is every term meeting every term, then collecting.",
                "Difference of squares needs both terms square AND subtracted.",
                "A sum of squares does not factor over the real numbers.",
                "In a perfect square the middle term is twice the product of the roots.",
                "Given four factorisations, expand them or substitute a value — do not factor.",
            ],
        },
    ]

    return lesson(
        slug="polynomials-and-factoring",
        title="Expanding and Factoring Polynomials",
        concrete=(
            "A garden $x$ metres square gets a border: three metres on one side, two on the "
            "other. The new area is $(x + 3)(x + 2)$ — and also $x^{2} + 5x + 6$. Two "
            "descriptions of the same patch of ground, and being able to swap between them on "
            "demand is what this skill is."
        ),
        objective=(
            "Expand products of polynomials, factor quadratics including a leading coefficient "
            "greater than one, and recognise the difference-of-squares and perfect-square "
            "patterns on sight."
        ),
        concept=[
            "**Skill card.** Still *Equivalent expressions*, in the **Advanced Math** domain. "
            "Factoring underpins the whole nonlinear-equations subtopic that follows, so time "
            "spent here pays twice.",
            "Expanding is bookkeeping: every term in the first bracket multiplies every term in "
            "the second, and then like terms collect. Two brackets of two terms give four "
            "products, of which the middle two combine. Nothing else is involved, which is why "
            "the same method works for longer brackets without any new rule.",
            "Factoring runs it backwards. Three patterns are worth recognising instantly. A "
            "difference of squares, $a^{2} - b^{2} = (a-b)(a+b)$, needs both terms to be "
            "squares AND to be subtracted — a sum of squares does not factor over the reals. A "
            "perfect square, $a^{2} + 2ab + b^{2} = (a+b)^{2}$, has a middle term equal to "
            "twice the product of the outer roots. Everything else needs the middle term split.",
            "**The test's angle.** When the options are four factorisations, do not factor. "
            "Expand each option, or substitute a value into the original and into each option "
            "and keep what matches. Putting $x = 1$ into $6x^{2} + 5x - 6$ gives $5$, and the "
            "correct factorisation must give $5$ too. Two values settle any tie, and neither "
            "route can go wrong the way splitting the middle term can.",
        ],
        key_idea=(
            "Expanding is every term meeting every term. Factoring is the same move backwards "
            "— and when the options are already factorisations, expanding them is faster than "
            "factoring anything."
        ),
        facts=[
            fact(
                "Difference of squares",
                "a^{2} - b^{2} = (a - b)(a + b)",
                "Both terms square, and subtracted. A sum of squares does not factor over the "
                "reals.",
            ),
            fact(
                "Perfect square",
                "a^{2} \\pm 2ab + b^{2} = (a \\pm b)^{2}",
                "The middle term is twice the product of the outer square roots. If it is not, "
                "this is not the pattern.",
            ),
            fact(
                "Splitting the middle term",
                "ax^{2} + bx + c: \\text{ find } p, q \\text{ with } pq = ac, \\; p + q = b",
                "Then split $bx$ into $px + qx$ and factor in pairs.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Forgetting the two middle products when expanding.",
                "$(x + 3)(x + 2)$ is not $x^{2} + 6$. Four products, and the two middle ones "
                "combine into $5x$.",
            ),
            mistake(
                "Trying to factor a sum of squares.",
                "$x^{2} + 16$ has no real factorisation. Only a DIFFERENCE of squares factors.",
            ),
            mistake(
                "Reading $(a + b)^{2}$ as $a^{2} + b^{2}$.",
                "The middle term $2ab$ is real. $(2x + 3)^{2} = 4x^{2} + 12x + 9$.",
            ),
            mistake(
                "Losing a sign in the middle coefficient.",
                "In $(2x - 5)(3x + 4)$ the middle is $8x - 15x = -7x$. Both signs of that "
                "coefficient will be on the option list.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


# ===========================================================================
# Lesson 3 — rational expressions
# ===========================================================================

def lesson_rational():
    worked = [
        problem(
            "sat-ae3-w1",
            "Which expression is equivalent to $\\dfrac{x^{2} - 9}{x^{2} + 7x + 12}$ for "
            "$x \\ne -3$ and $x \\ne -4$?",
            "**Answer.** $\\dfrac{x - 3}{x + 4}$.  \n"
            "Factor top and bottom before cancelling anything. The numerator is a difference "
            "of squares; the denominator needs two numbers multiplying to $12$ and adding to "
            "$7$, namely $3$ and $4$:\n"
            "$$\\frac{(x - 3)(x + 3)}{(x + 3)(x + 4)}$$\n"
            "Now the common FACTOR $(x + 3)$ cancels:\n"
            "$$= \\frac{x - 3}{x + 4}$$\n"
            "Check with $x = 1$: the original is $\\frac{1 - 9}{1 + 7 + 12} = \\frac{-8}{20} = "
            "-\\frac{2}{5}$, and $\\frac{1 - 3}{1 + 4} = -\\frac{2}{5}$.  \n"
            "Cancelling requires FACTORS, not terms. You may not cancel the $x^{2}$ from top "
            "and bottom of the original — they are terms inside sums, and doing it gives "
            "$\\frac{-9}{7x + 12}$, which is a different expression.",
            [
                "Eq(simplify((x**2 - 9)/(x**2 + 7*x + 12) - (x - 3)/(x + 4)), 0)",
                "Eq(Rational(1 - 9, 1 + 7 + 12), Rational(-2, 5))",
                "Eq(Rational(1 - 3, 1 + 4), Rational(-2, 5))",
            ],
        ),
        problem(
            "sat-ae3-w2",
            "Which expression is equivalent to $\\dfrac{3}{x} + \\dfrac{2}{x + 1}$ for "
            "$x \\ne 0$ and $x \\ne -1$?",
            "**Answer.** $\\dfrac{5x + 3}{x(x + 1)}$.  \n"
            "Adding fractions needs a common denominator, and here the two denominators share "
            "nothing, so the common denominator is their product:\n"
            "$$\\frac{3(x + 1)}{x(x + 1)} + \\frac{2x}{x(x + 1)}$$\n"
            "Now the numerators add:\n"
            "$$\\frac{3x + 3 + 2x}{x(x + 1)} = \\frac{5x + 3}{x(x + 1)}$$\n"
            "Check with $x = 1$: the original is $3 + 1 = 4$, and "
            "$\\frac{5 + 3}{1 \\cdot 2} = 4$.  \n"
            "Adding numerators and denominators separately — getting $\\frac{5}{2x + 1}$ — is "
            "the standard wrong option. At $x = 1$ that gives $\\frac{5}{3}$, nothing like $4$, "
            "which is exactly why substituting a value catches it.",
            [
                "Eq(simplify(3/x + 2/(x + 1) - (5*x + 3)/(x*(x + 1))), 0)",
                "Eq(Rational(3,1) + Rational(2,2), 4)",
                "Eq(Rational(5*1 + 3, 1*2), 4)",
                "Ne(Rational(5, 2*1 + 1), 4)",
            ],
        ),
        problem(
            "sat-ae3-w3",
            "The expression $\\dfrac{2x^{2} + 7x + 3}{x + 3}$ is equivalent to which of the "
            "following for $x \\ne -3$?",
            "**Answer.** $2x + 1$.  \n"
            "Factor the numerator. Two numbers multiplying to $2 \\times 3 = 6$ and adding to "
            "$7$ are $6$ and $1$:\n"
            "$$2x^{2} + 6x + x + 3 = 2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3)$$\n"
            "So\n"
            "$$\\frac{(2x + 1)(x + 3)}{x + 3} = 2x + 1$$\n"
            "Check with $x = 0$: the original is $\\frac{3}{3} = 1$, and $2(0) + 1 = 1$.  \n"
            "The restriction $x \\ne -3$ matters even though the simplified form is perfectly "
            "happy there. The two expressions agree everywhere EXCEPT $x = -3$, where the "
            "original is undefined — which is why the question states the restriction rather "
            "than leaving it out.",
            [
                "Eq(expand((2*x + 1)*(x + 3)), 2*x**2 + 7*x + 3)",
                "Eq(simplify((2*x**2 + 7*x + 3)/(x + 3) - (2*x + 1)), 0)",
                "Eq(Rational(2*0 + 0 + 3, 0 + 3), 1)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-ae3-t1",
            "Which expression is equivalent to $\\dfrac{x^{2} - 4}{x - 2}$ for $x \\ne 2$?",
            "**Answer.** $x + 2$. The numerator factors as $(x - 2)(x + 2)$, and the "
            "$(x - 2)$ cancels.",
            ["Eq(simplify((x**2 - 4)/(x - 2) - (x + 2)), 0)"],
        ),
        problem(
            "sat-ae3-t2",
            "Which expression is equivalent to $\\dfrac{1}{x} - \\dfrac{1}{x + 2}$ for "
            "$x \\ne 0$ and $x \\ne -2$?",
            "**Answer.** $\\dfrac{2}{x(x + 2)}$. Over the common denominator $x(x+2)$ the "
            "numerators are $(x + 2)$ and $x$, and their difference is $2$. Check at $x = 2$: "
            "$\\frac{1}{2} - \\frac{1}{4} = \\frac{1}{4}$, and $\\frac{2}{2 \\cdot 4} = "
            "\\frac{1}{4}$.",
            [
                "Eq(simplify(1/x - 1/(x + 2) - 2/(x*(x + 2))), 0)",
                "Eq(Rational(1,2) - Rational(1,4), Rational(1,4))",
            ],
        ),
        problem(
            "sat-ae3-t3",
            "For what value of $x$ is $\\dfrac{x + 5}{x^{2} - 16}$ undefined?",
            "**Answer.** $x = 4$ and $x = -4$. A fraction is undefined exactly where its "
            "denominator is zero, and $x^{2} - 16 = (x - 4)(x + 4)$ is zero at both. The "
            "numerator plays no part — $x = -5$ makes the fraction ZERO, which is perfectly "
            "well defined.",
            [
                "Eq(4**2 - 16, 0)",
                "Eq((-4)**2 - 16, 0)",
                "Eq((-5) + 5, 0)",
                "Ne((-5)**2 - 16, 0)",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Factor first, cancel second",
            "body": "A rational expression simplifies only when the top and bottom share a "
                    "FACTOR. That means factoring both completely before touching anything. "
                    "The single biggest error in this lesson is cancelling terms — striking "
                    "the $x^{2}$ off the top and bottom of "
                    "$\\frac{x^{2} - 9}{x^{2} + 7x + 12}$ — which changes the value of the "
                    "expression entirely.",
        },
        {
            "kind": "tapQuestion",
            "title": "Can this cancel?",
            "prompt": "In $\\dfrac{x + 4}{x + 8}$, may the $x$ terms be cancelled?",
            "options": [
                "No — they are terms inside sums, not factors",
                "Yes, leaving $\\dfrac{4}{8}$",
                "Yes, leaving $\\dfrac{1}{2}$",
                "Only when $x$ is positive",
            ],
            "correctIndex": 0,
            "explanation": "Cancelling needs a common FACTOR of the whole numerator and the "
                           "whole denominator. Here $x$ is added, not multiplied. Test it with "
                           "$x = 4$: the expression is $\\frac{8}{12} = \\frac{2}{3}$, not "
                           "$\\frac{1}{2}$.",
            "check": [
                "Eq(Rational(4 + 4, 4 + 8), Rational(2,3))",
                "Ne(Rational(2,3), Rational(1,2))",
            ],
        },
        {"kind": "worked", "title": "Factor, then cancel", "problemId": "sat-ae3-w1"},
        {
            "kind": "teach",
            "title": "Adding needs a common denominator",
            "beats": [
                "Two fractions add only over a shared denominator.",
                "If the denominators share nothing, the common denominator is their product.",
                "Rescale each numerator by whatever its denominator was missing.",
                "Numerators add; denominators do NOT.",
            ],
        },
        {"kind": "worked", "title": "Adding two rational expressions", "problemId": "sat-ae3-w2"},
        {
            "kind": "tip",
            "title": "One substitution kills three options",
            "body": "Rational-expression items are the easiest place on the test to check by "
                    "substitution. Pick $x = 1$ or $x = 2$, evaluate the original, then "
                    "evaluate each option. The wrong options come from cancelling terms or "
                    "adding denominators, and both of those go visibly wrong at almost any "
                    "value you pick.",
        },
        {"kind": "worked", "title": "Dividing out a whole factor", "problemId": "sat-ae3-w3"},
        {
            "kind": "teach",
            "title": "Where an expression is undefined",
            "body": "A rational expression is undefined exactly where its DENOMINATOR is zero. "
                    "The numerator has nothing to do with it — a zero numerator makes the "
                    "expression equal zero, which is a perfectly ordinary value. That is why "
                    "these questions state restrictions like '$x \\ne -3$': the simplified "
                    "form would happily accept $-3$, but the original never could.",
        },
        {"kind": "tryIt", "title": "Your turn: cancel a factor", "problemId": "sat-ae3-t1"},
        {"kind": "tryIt", "title": "Your turn: subtract two fractions", "problemId": "sat-ae3-t2"},
        {"kind": "tryIt", "title": "Your turn: where is it undefined?", "problemId": "sat-ae3-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Cancel factors, never terms — factor top and bottom completely first.",
                "Adding fractions needs a common denominator; denominators never add.",
                "An expression is undefined where the DENOMINATOR is zero, not the numerator.",
                "A cancelled factor leaves a restriction behind, which is why the stem states one.",
                "Substituting x = 1 or 2 into the original and each option settles most items.",
            ],
        },
    ]

    return lesson(
        slug="rational-expressions",
        title="Rational Expressions",
        concrete=(
            "Two workers paint a room in $x$ hours and $x + 1$ hours on their own. Their "
            "combined rate is $\\frac{1}{x} + \\frac{1}{x+1}$ rooms per hour — a single "
            "fraction once you put it over a common denominator, and useless until you do."
        ),
        objective=(
            "Simplify rational expressions by factoring and cancelling common factors, add and "
            "subtract them over a common denominator, and identify where one is undefined."
        ),
        concept=[
            "**Skill card.** Still *Equivalent expressions*, in the **Advanced Math** domain. "
            "Rational expressions carry the harder end of this subtopic, and almost every "
            "wrong answer comes from one of two specific illegal moves.",
            "A rational expression simplifies only when the numerator and denominator share a "
            "FACTOR. So factor both completely, then cancel whole factors. You may never "
            "cancel terms: striking the $x^{2}$ from the top and bottom of "
            "$\\frac{x^{2}-9}{x^{2}+7x+12}$ is not a simplification, it is a different "
            "expression.",
            "Adding or subtracting needs a common denominator. When the two denominators share "
            "no factor, the common denominator is their product, and each numerator gets "
            "rescaled by whatever its own denominator was missing. Numerators then add; "
            "denominators never do.",
            "**The test's angle.** Restrictions. An expression is undefined exactly where its "
            "DENOMINATOR is zero — the numerator is irrelevant, since a zero numerator just "
            "makes the value zero. And when a factor cancels, the restriction it created "
            "survives: $\\frac{(2x+1)(x+3)}{x+3}$ equals $2x + 1$ everywhere except at "
            "$x = -3$, which is why the stem says '$x \\ne -3$'.",
        ],
        key_idea=(
            "Factor first, then cancel FACTORS — never terms. Add only over a common "
            "denominator, and remember the expression is undefined wherever the original "
            "denominator was zero."
        ),
        facts=[
            fact(
                "Cancelling",
                "\\frac{a \\cdot c}{b \\cdot c} = \\frac{a}{b} \\quad (c \\ne 0)",
                "Only common FACTORS cancel. $\\frac{a + c}{b + c}$ simplifies to nothing.",
            ),
            fact(
                "Adding",
                "\\frac{a}{p} + \\frac{b}{q} = \\frac{aq + bp}{pq}",
                "Rescale each numerator by the other denominator. Denominators multiply; they "
                "never add.",
            ),
            fact(
                "Undefined where",
                "\\frac{N(x)}{D(x)} \\text{ is undefined} \\iff D(x) = 0",
                "Factor the denominator and set each factor to zero. The numerator does not "
                "matter.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Cancelling terms instead of factors.",
                "In $\\frac{x + 4}{x + 8}$ nothing cancels — the $x$ is added, not multiplied. "
                "Substitute $x = 4$ and you get $\\frac{2}{3}$, not $\\frac{1}{2}$.",
            ),
            mistake(
                "Adding numerators and denominators separately.",
                "$\\frac{3}{x} + \\frac{2}{x+1}$ is not $\\frac{5}{2x+1}$. Rescale both over "
                "the common denominator first.",
            ),
            mistake(
                "Looking at the numerator to find where an expression is undefined.",
                "A zero numerator makes the expression zero. Only a zero DENOMINATOR makes it "
                "undefined.",
            ),
            mistake(
                "Dropping the restriction after a factor cancels.",
                "The original was undefined at that value and the simplified form is not, so "
                "the two expressions agree everywhere except there.",
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
        "sat-ae-p01",
        "Which expression is equivalent to $x^{5} \\cdot x^{3}$?",
        "**Answer.** $x^{8}$. Multiplying powers of the same base adds the exponents.",
        ["Eq(simplify(x**5*x**3 - x**8), 0)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-p02",
        "Which expression is equivalent to $(4x^{2})^{3}$?",
        "**Answer.** $64x^{6}$. The outer exponent reaches the $4$ as well: $4^{3} = 64$, and "
        "$(x^{2})^{3} = x^{6}$. Leaving the coefficient alone gives $4x^{6}$, a listed option.",
        ["Eq(simplify((4*x**2)**3 - 64*x**6), 0)", "Ne(4*2**6, (4*2**2)**3)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-p03",
        "Which expression is equivalent to $(x + 7)(x - 3)$?",
        "**Answer.** $x^{2} + 4x - 21$. The middle terms are $-3x$ and $7x$, summing to $4x$.",
        ["Eq(expand((x + 7)*(x - 3)), x**2 + 4*x - 21)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-p04",
        "Which expression is equivalent to $16x^{2} - 25$?",
        "**Answer.** $(4x - 5)(4x + 5)$. A difference of squares: $(4x)^{2} - 5^{2}$.",
        ["Eq(expand((4*x - 5)*(4*x + 5)), 16*x**2 - 25)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-p05",
        "Which expression is equivalent to $\\dfrac{12x^{7}y^{3}}{3x^{2}y^{6}}$ for "
        "$x \\ne 0$ and $y \\ne 0$?",
        "**Answer.** $\\dfrac{4x^{5}}{y^{3}}$. Divide the coefficients and subtract exponents "
        "per base: $x^{7-2} = x^{5}$, $y^{3-6} = y^{-3}$, and the negative exponent moves the "
        "$y$ down.",
        ["Eq(simplify(12*x**7*y**3/(3*x**2*y**6) - 4*x**5/y**3), 0)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-p06",
        "Which expression is equivalent to $3x^{2} + 11x - 4$?",
        "**Answer.** $(3x - 1)(x + 4)$. Two numbers multiplying to $3 \\times (-4) = -12$ and "
        "adding to $11$ are $12$ and $-1$: $3x^{2} + 12x - x - 4 = 3x(x + 4) - 1(x + 4)$. "
        "Check with $x = 1$: the original is $10$, and $(2)(5) = 10$.",
        ["Eq(expand((3*x - 1)*(x + 4)), 3*x**2 + 11*x - 4)", "Eq(3 + 11 - 4, 10)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-p07",
        "Which expression is equivalent to $\\dfrac{x^{2} + 5x + 6}{x + 2}$ for $x \\ne -2$?",
        "**Answer.** $x + 3$. The numerator factors as $(x + 2)(x + 3)$ and the $(x + 2)$ "
        "cancels.",
        ["Eq(simplify((x**2 + 5*x + 6)/(x + 2) - (x + 3)), 0)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-p08",
        "Which expression is equivalent to $\\sqrt{75}$?",
        "**Answer.** $5\\sqrt{3}$. Split off the largest perfect square: "
        "$75 = 25 \\times 3$, so $\\sqrt{75} = 5\\sqrt{3}$.",
        ["Eq(simplify(sqrt(75) - 5*sqrt(3)), 0)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-p09",
        "If $x > 0$, which expression is equivalent to $\\left(x^{4}\\right)^{3/2}$?",
        "**Answer.** $x^{6}$. A power of a power multiplies the exponents: "
        "$4 \\times \\frac{3}{2} = 6$. Check with $x = 2$: $(16)^{3/2} = 64 = 2^{6}$.",
        ["Eq(4*Rational(3,2), 6)", "Eq((2**4)**Rational(3,2), 64)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-p10",
        "Which expression is equivalent to $\\dfrac{4}{x - 1} - \\dfrac{2}{x}$ for "
        "$x \\ne 0$ and $x \\ne 1$?",
        "**Answer.** $\\dfrac{2x + 2}{x(x - 1)}$. Over the common denominator $x(x-1)$ the "
        "numerators are $4x$ and $2(x - 1) = 2x - 2$, and their difference is $2x + 2$. Check "
        "at $x = 2$: $4 - 1 = 3$, and $\\frac{6}{2} = 3$.",
        [
            "Eq(simplify(4/(x - 1) - 2/x - (2*x + 2)/(x*(x - 1))), 0)",
            "Eq(Rational(4,1) - Rational(2,2), 3)",
            "Eq(Rational(2*2 + 2, 2*1), 3)",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ae-p11",
        "Which expression is equivalent to $(2x + 5)^{2}$?",
        "**Answer.** $4x^{2} + 20x + 25$. The middle term is twice the product of the two "
        "parts: $2 \\times 2x \\times 5 = 20x$. Writing $4x^{2} + 25$ — squaring each term "
        "separately — is the standard wrong option.",
        ["Eq(expand((2*x + 5)**2), 4*x**2 + 20*x + 25)", "Ne(4*1**2 + 25, expand((2*x + 5)**2).subs(x, 1))"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-p12",
        "For which values of $x$ is $\\dfrac{2x - 1}{x^{2} - 5x + 6}$ undefined?",
        "**Answer.** $x = 2$ and $x = 3$. The denominator factors as $(x - 2)(x - 3)$, which "
        "is zero at both. The value $x = \\frac{1}{2}$ makes the NUMERATOR zero, so the "
        "expression equals zero there — perfectly well defined.",
        [
            "Eq(2**2 - 5*2 + 6, 0)",
            "Eq(3**2 - 5*3 + 6, 0)",
            "Eq(expand((x - 2)*(x - 3)), x**2 - 5*x + 6)",
        ],
        badges=_b("Medium"),
    ),
]

TEST = [
    problem(
        "sat-ae-x01",
        "Which expression is equivalent to $(5x^{3})^{2}$?",
        "**Answer.** $25x^{6}$. Square the coefficient and multiply the exponents.",
        ["Eq(simplify((5*x**3)**2 - 25*x**6), 0)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-x02",
        "Which expression is equivalent to $(x - 8)(x + 8)$?",
        "**Answer.** $x^{2} - 64$. A difference of squares — the middle terms cancel.",
        ["Eq(expand((x - 8)*(x + 8)), x**2 - 64)"],
        badges=_b("Easy"),
    ),
    problem(
        "sat-ae-x03",
        "Which expression is equivalent to $\\dfrac{x^{2} - 25}{x^{2} - 2x - 15}$ for "
        "$x \\ne 5$ and $x \\ne -3$?",
        "**Answer.** $\\dfrac{x + 5}{x + 3}$. Factor both parts before cancelling anything: "
        "the numerator is a difference of squares, $(x - 5)(x + 5)$, and the denominator needs "
        "two numbers multiplying to $-15$ and adding to $-2$, giving $(x - 5)(x + 3)$. The "
        "common factor $(x - 5)$ cancels. Check at $x = 0$: the original is "
        "$\\frac{-25}{-15} = \\frac{5}{3}$, and $\\frac{5}{3}$ matches.",
        [
            "Eq(simplify((x**2 - 25)/(x**2 - 2*x - 15) - (x + 5)/(x + 3)), 0)",
            "Eq(Rational(-25, -15), Rational(5,3))",
        ],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-x04",
        "If $a > 0$, which expression is equivalent to $\\dfrac{a^{3}}{a^{-2}}$?",
        "**Answer.** $a^{5}$. Subtracting a negative exponent adds: $3 - (-2) = 5$. Check "
        "with $a = 2$: $\\frac{8}{1/4} = 32 = 2^{5}$.",
        ["Eq(Rational(8,1)/Rational(1,4), 32)", "Eq(2**5, 32)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-x05",
        "Which expression is equivalent to $4x^{2} - 20x + 25$?",
        "**Answer.** $(2x - 5)^{2}$. Both outer terms are squares and the middle is twice "
        "their product with a minus sign: $2 \\times 2x \\times 5 = 20x$.",
        ["Eq(expand((2*x - 5)**2), 4*x**2 - 20*x + 25)"],
        badges=_b("Medium"),
    ),
    problem(
        "sat-ae-x06",
        "Which expression is equivalent to $\\dfrac{5}{x + 2} + \\dfrac{3}{x}$ for "
        "$x \\ne 0$ and $x \\ne -2$?",
        "**Answer.** $\\dfrac{8x + 6}{x(x + 2)}$. Over the common denominator the numerators "
        "are $5x$ and $3(x + 2) = 3x + 6$, summing to $8x + 6$. Check at $x = 2$: "
        "$\\frac{5}{4} + \\frac{3}{2} = \\frac{11}{4}$, and $\\frac{22}{8} = \\frac{11}{4}$.",
        [
            "Eq(simplify(5/(x + 2) + 3/x - (8*x + 6)/(x*(x + 2))), 0)",
            "Eq(Rational(5,4) + Rational(3,2), Rational(11,4))",
            "Eq(Rational(8*2 + 6, 2*4), Rational(11,4))",
        ],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ae-x07",
        "If $x > 0$, which expression is equivalent to $\\sqrt[4]{x^{6}}$?",
        "**Answer.** $x^{3/2}$. The fourth root is an exponent of $\\frac{1}{4}$, so "
        "$x^{6/4} = x^{3/2}$. Check with $x = 4$: $\\sqrt[4]{4096} = 8$ and "
        "$4^{3/2} = 8$.",
        ["Eq(Rational(6,4), Rational(3,2))", "Eq(4096**Rational(1,4), 8)", "Eq(4**Rational(3,2), 8)"],
        badges=_b("Hard"),
    ),
    problem(
        "sat-ae-x08",
        "Which expression is equivalent to $6x^{2} - 13x + 6$?",
        "**Answer.** $(3x - 2)(2x - 3)$. Two numbers multiplying to $6 \\times 6 = 36$ and "
        "adding to $-13$ are $-4$ and $-9$: $6x^{2} - 4x - 9x + 6 = 2x(3x - 2) - 3(3x - 2)$. "
        "Substituting $x = 1$ into the original gives $-1$, and $(1)(-1) = -1$ agrees.",
        [
            "Eq(expand((3*x - 2)*(2*x - 3)), 6*x**2 - 13*x + 6)",
            "Eq(6 - 13 + 6, -1)",
            "Eq((3*1 - 2)*(2*1 - 3), -1)",
        ],
        badges=_b("Hard"),
    ),
]


def main():
    lessons = [lesson_exponents(), lesson_polynomials(), lesson_rational()]
    write_unit(
        COURSE,
        UNIT_SLUG,
        "Equivalent Expressions",
        1,
        "Exponent and radical rules, expanding and factoring polynomials, and rewriting "
        "rational expressions — the machinery behind 'which of the following is equivalent to', "
        "this domain's commonest question.",
        None,
        lessons,
        PRACTICE,
        TEST,
    )


if __name__ == "__main__":
    main()
