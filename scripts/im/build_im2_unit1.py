#!/usr/bin/env python3
"""Integrated Mathematics 2 — Unit 1: Rational Exponents & Radicals.

CCSS Integrated Math II: N-RN.1 (extend the properties of integer exponents to
rational exponents, explaining WHY the extension is forced rather than chosen),
N-RN.2 (rewrite expressions involving radicals and rational exponents using the
properties), N-RN.3 (explain why sums and products of rationals are rational,
and why a rational plus an irrational is irrational).

IM1 Unit 6 let the exponent be any integer. This unit lets it be a fraction —
and the point of the first lesson is that once you insist the exponent rules
keep working, the meaning of $x^{1/2}$ is not a definition someone chose. It is
the only value that can possibly work.

Run: python3 scripts/im/build_im2_unit1.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-2"


# ===========================================================================
# Lesson 1 — N-RN.1: why a fractional exponent must mean a root
# ===========================================================================
def lesson_rational_exponents():
    return lesson(
        slug="rational-exponents",
        title="Why a Fractional Exponent Means a Root",
        concrete=(
            "Nobody sat down and DECIDED that $9^{1/2}$ should be $3$. They noticed that if the "
            "exponent rules are to keep working when the exponent becomes a fraction, then "
            "$9^{1/2}$ has no choice but to be $3$ — anything else breaks arithmetic that already "
            "worked. This lesson is the argument, not the announcement."
        ),
        objective=(
            "Explain why $x^{1/n}$ must equal $\\sqrt[n]{x}$ if the exponent rules are to survive, "
            "convert between radical and rational-exponent form, and evaluate rational powers of "
            "numbers."
        ),
        concept=[
            "**Start from the rule you already trust.** For integer exponents, "
            "$(x^{a})^{b} = x^{ab}$ — a rule IM1 established and used constantly. The whole "
            "question is: if we allow $a$ to be a fraction, what must $x^{1/2}$ be for that rule "
            "to keep holding?",
            "**The argument, in one line.** Suppose the rule survives. Then "
            "$$\\left(9^{1/2}\\right)^{2} = 9^{\\frac{1}{2} \\times 2} = 9^{1} = 9.$$ "
            "So $9^{1/2}$ is a number whose square is $9$. Taking the positive root by "
            "convention, $9^{1/2} = 3$. Nothing was defined — the value was FORCED by insisting "
            "the old rule still works.",
            "**The general statement.** The same argument with $n$ in place of $2$ gives "
            "$$x^{1/n} = \\sqrt[n]{x},$$ "
            "because $\\left(x^{1/n}\\right)^{n} = x^{1} = x$, which is exactly what \"the $n$th "
            "root of $x$\" means.",
            "**And then every fraction follows.** Write $\\frac{m}{n}$ as $m \\times \\frac{1}{n}$: "
            "$$x^{m/n} = \\left(x^{1/n}\\right)^{m} = \\left(\\sqrt[n]{x}\\right)^{m} "
            "= \\sqrt[n]{x^{m}}.$$ "
            "Both orders give the same answer, but ROOT FIRST is almost always easier by hand: "
            "$8^{2/3}$ is $\\left(\\sqrt[3]{8}\\right)^{2} = 2^{2} = 4$, whereas power-first asks "
            "you to find $\\sqrt[3]{64}$.",
            "**Negative exponents still mean reciprocals.** $x^{-m/n} = \\frac{1}{x^{m/n}}$, so "
            "$8^{-2/3} = \\frac{1}{4}$. The negative sign controls the reciprocal and the "
            "fraction controls the root; they are independent instructions and both apply.",
            "**When the base is negative, be careful.** $(-8)^{1/3} = -2$ is fine, because an odd "
            "root of a negative number exists. But $(-9)^{1/2}$ is not a real number — no real "
            "number squares to $-9$. Even roots need a non-negative base, which is exactly the "
            "restriction that will produce complex numbers in Unit 4.",
        ],
        key_idea=(
            "$x^{1/n} = \\sqrt[n]{x}$ is forced, not chosen: it is the only value for which "
            "$(x^{a})^{b} = x^{ab}$ keeps working. Then $x^{m/n} = (\\sqrt[n]{x})^{m}$ — take the "
            "root first."
        ),
        facts=[
            fact(
                "The forced meaning",
                "x^{1/n} = \\sqrt[n]{x} \\quad \\text{because} \\quad "
                "\\left(x^{1/n}\\right)^{n} = x^{1} = x",
                "Not a definition — the only value consistent with the exponent rule you already "
                "had.",
            ),
            fact(
                "The general rational power",
                "x^{m/n} = \\left(\\sqrt[n]{x}\\right)^{m} = \\sqrt[n]{x^{m}}",
                "Both are correct; take the root FIRST to keep the numbers small.",
            ),
            fact(
                "Negative rational exponents",
                "x^{-m/n} = \\frac{1}{x^{m/n}}",
                "The minus sign means reciprocal; the fraction means root. Independent "
                "instructions, both applied.",
            ),
        ],
        worked=[
            problem(
                "im2-u1-l1-we1",
                "Show that if the rule $(x^{a})^{b} = x^{ab}$ is to hold for fractional exponents, "
                "then $25^{1/2}$ must be $5$.",
                "**Assume the rule survives** and square the quantity:"
                "$$\\left(25^{1/2}\\right)^{2} = 25^{\\frac{1}{2} \\times 2} = 25^{1} = 25.$$"
                "**Read what that says.** $25^{1/2}$ is a number whose square is $25$. There are "
                "two such numbers, $5$ and $-5$; by convention the symbol denotes the "
                "non-negative one, so"
                "$$25^{1/2} = 5.$$"
                "**Why this is a proof and not a definition.** We did not decide the value. We "
                "required one rule — the rule that already worked for integers — to keep working, "
                "and that requirement left exactly one answer available. Any other value would "
                "make $(x^a)^b = x^{ab}$ false somewhere, breaking arithmetic that was already "
                "correct.",
                [
                    "Eq(5**2, 25)",
                    "Eq((-5)**2, 25)",
                    "Eq(Rational(1,2)*2, 1)",
                    "Eq(sqrt(25), 5)",
                ],
            ),
            problem(
                "im2-u1-l1-we2",
                "Evaluate $8^{2/3}$, $16^{3/4}$ and $32^{2/5}$, taking the root first each time.",
                "**Root first, then power.**"
                "$$8^{2/3} = \\left(\\sqrt[3]{8}\\right)^{2} = 2^{2} = 4.$$"
                "$$16^{3/4} = \\left(\\sqrt[4]{16}\\right)^{3} = 2^{3} = 8.$$"
                "$$32^{2/5} = \\left(\\sqrt[5]{32}\\right)^{2} = 2^{2} = 4.$$"
                "**Check one the other way.** Power first on the middle one: "
                "$16^{3} = 4096$, and $\\sqrt[4]{4096} = 8$ ✓ — same answer, but you had to know "
                "the fourth root of a four-digit number."
                "**Why root-first is the habit.** In every case the root of the base was a small "
                "whole number, and the power of that was trivial. Reversing the order forces you "
                "to take a root of a large number instead. Same result, much more work.",
                [
                    "Eq(8**Rational(2,3), 4)",
                    "Eq(16**Rational(3,4), 8)",
                    "Eq(32**Rational(2,5), 4)",
                    "Eq(16**3, 4096)",
                    "Eq(4096**Rational(1,4), 8)",
                ],
            ),
            problem(
                "im2-u1-l1-we3",
                "Rewrite in radical form: $x^{3/5}$ and $y^{-1/2}$. Rewrite with rational "
                "exponents: $\\sqrt[4]{t^{3}}$ and $\\dfrac{1}{\\sqrt{w}}$.",
                "**To radical form.** The denominator of the exponent is the root index and the "
                "numerator is the power:"
                "$$x^{3/5} = \\sqrt[5]{x^{3}} = \\left(\\sqrt[5]{x}\\right)^{3}.$$"
                "A negative exponent means a reciprocal:"
                "$$y^{-1/2} = \\frac{1}{y^{1/2}} = \\frac{1}{\\sqrt{y}}.$$"
                "**To exponent form.** Read the index as the denominator:"
                "$$\\sqrt[4]{t^{3}} = t^{3/4}.$$"
                "$$\\frac{1}{\\sqrt{w}} = \\frac{1}{w^{1/2}} = w^{-1/2}.$$"
                "**Sanity-check with numbers.** Put $t = 16$: $\\sqrt[4]{16^3} = "
                "\\sqrt[4]{4096} = 8$, and $16^{3/4} = 2^{3} = 8$ ✓. Put $w = 9$: "
                "$\\frac{1}{\\sqrt{9}} = \\frac{1}{3}$, and $9^{-1/2} = \\frac{1}{3}$ ✓",
                [
                    "Eq(16**Rational(3,4), 8)",
                    "Eq(4096**Rational(1,4), 8)",
                    "Eq(9**Rational(-1,2), Rational(1,3))",
                    "Eq(Rational(1, 3), Rational(1,3))",
                ],
            ),
            problem(
                "im2-u1-l1-we4",
                "Simplify $\\dfrac{x^{3/4} \\cdot x^{1/2}}{x^{1/4}}$, and evaluate it at $x = 16$.",
                "**Use the exponent rules — they work unchanged on fractions.** Multiplying adds "
                "the exponents:"
                "$$x^{3/4} \\cdot x^{1/2} = x^{\\frac{3}{4} + \\frac{1}{2}} "
                "= x^{\\frac{3}{4} + \\frac{2}{4}} = x^{5/4}.$$"
                "Dividing subtracts them:"
                "$$\\frac{x^{5/4}}{x^{1/4}} = x^{\\frac{5}{4} - \\frac{1}{4}} = x^{1} = x.$$"
                "The whole expression simplifies to just $x$."
                "**Now substitute.** At $x = 16$ the answer is $16$."
                "**Verify by brute force**, to confirm the rules really did transfer:"
                "$$16^{3/4} = 8, \\qquad 16^{1/2} = 4, \\qquad 16^{1/4} = 2,$$"
                "$$\\frac{8 \\times 4}{2} = \\frac{32}{2} = 16 \\ \\checkmark$$"
                "That agreement is the point of the whole lesson: the rules were extended so that "
                "this kind of check can never fail.",
                [
                    "Eq(Rational(3,4) + Rational(1,2), Rational(5,4))",
                    "Eq(Rational(5,4) - Rational(1,4), 1)",
                    "Eq(16**Rational(3,4), 8)",
                    "Eq(16**Rational(1,2), 4)",
                    "Eq(16**Rational(1,4), 2)",
                    "Eq(Rational(8*4, 2), 16)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading x^(1/2) as half of x.",
                "The exponent is not a multiplier. x^(1/2) is the number whose square is x — "
                "9^(1/2) is 3, not 4.5.",
            ),
            mistake(
                "Flipping the root and the power: reading x^(2/3) as the square root of x cubed.",
                "The DENOMINATOR is the root index. x^(2/3) is the cube root, squared. Check on "
                "8: 8^(2/3) = 4, while √(8³) = √512 ≈ 22.6.",
            ),
            mistake(
                "Treating a negative exponent as making the answer negative.",
                "It makes it a reciprocal: 8^(−2/3) = 1/4, a positive number. The sign of the "
                "exponent never becomes the sign of the answer.",
            ),
            mistake(
                "Evaluating an even root of a negative base.",
                "(−9)^(1/2) is not a real number — nothing real squares to −9. Odd roots are fine: "
                "(−8)^(1/3) = −2.",
            ),
        ],
        try_it=[
            problem(
                "im2-u1-l1-t1",
                "Evaluate $27^{2/3}$ and $81^{3/4}$.",
                "Root first: $27^{2/3} = \\left(\\sqrt[3]{27}\\right)^{2} = 3^{2} = 9$, and "
                "$81^{3/4} = \\left(\\sqrt[4]{81}\\right)^{3} = 3^{3} = 27$.",
                [
                    "Eq(27**Rational(2,3), 9)",
                    "Eq(81**Rational(3,4), 27)",
                ],
            ),
            problem(
                "im2-u1-l1-t2",
                "Evaluate $16^{-3/4}$ and explain the effect of each part of the exponent.",
                "The minus makes it a reciprocal and the fraction takes a root then a power:"
                "$$16^{-3/4} = \\frac{1}{16^{3/4}} = \\frac{1}{\\left(\\sqrt[4]{16}\\right)^{3}} "
                "= \\frac{1}{2^{3}} = \\frac{1}{8}.$$"
                "The answer is positive — a negative exponent never produces a negative result.",
                [
                    "Eq(16**Rational(-3,4), Rational(1,8))",
                    "Eq(16**Rational(3,4), 8)",
                    "16**Rational(-3,4) > 0",
                ],
            ),
            problem(
                "im2-u1-l1-t3",
                "Simplify $\\left(x^{2/3}\\right)^{9}$ and check at $x = 8$.",
                "Multiply the exponents: $x^{\\frac{2}{3} \\times 9} = x^{6}$. At $x = 8$: "
                "$8^{6} = 262\\,144$. Checking the other way, $8^{2/3} = 4$ and "
                "$4^{9} = 262\\,144$ ✓",
                [
                    "Eq(Rational(2,3)*9, 6)",
                    "Eq(8**6, 262144)",
                    "Eq(8**Rational(2,3), 4)",
                    "Eq(4**9, 262144)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "N-RN.1",
                "title": "Nobody chose what a fractional exponent means",
                "body": (
                    "The value of $9^{1/2}$ was not decided by committee. It is the only number "
                    "that lets the exponent rule you already trust keep working — and that is a "
                    "much stronger reason than a definition."
                ),
                "beats": [
                    "The rule: $(x^{a})^{b} = x^{ab}$",
                    "It worked for every **integer** exponent",
                    "Insist it still works for fractions…",
                    "…and only one value of $9^{1/2}$ survives",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "The argument",
                "title": "Square it and see what is left",
                "body": (
                    "$\\left(9^{1/2}\\right)^{2} = 9^{\\frac{1}{2} \\times 2} = 9^{1} = 9$. So "
                    "$9^{1/2}$ is a number whose square is $9$. That is the definition of a square "
                    "root — the meaning was forced, not assigned."
                ),
            },
            {"kind": "worked", "title": "The forcing argument, in full", "problemId": "im2-u1-l1-we1"},
            {
                "kind": "exponentBuilder",
                "eyebrow": "The rule being extended",
                "title": "Powers of a power multiply",
                "teach": (
                    "This is the integer rule the whole lesson leans on: raising a power to a "
                    "power multiplies the exponents. Everything about fractional exponents is a "
                    "consequence of insisting this keeps holding."
                ),
                "config": {"base": 2, "exp": 5, "maxExp": 8},
            },
            tap(
                "What must this equal?",
                "If the exponent rules hold, what is $\\left(64^{1/3}\\right)^{3}$?",
                ["$64$", "$4$", "$192$", "$21.3$"],
                0,
                "$\\left(64^{1/3}\\right)^{3} = 64^{\\frac{1}{3} \\times 3} = 64^{1} = 64$. That "
                "is what makes $64^{1/3}$ the cube root: it is the number you must cube to get "
                "$64$ back — namely $4$. Note $4$ is the value of $64^{1/3}$ itself, not of the "
                "cubed expression.",
                [
                    "Eq(Rational(1,3)*3, 1)",
                    "Eq(64**Rational(1,3), 4)",
                    "Eq(4**3, 64)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "N-RN.2",
                "title": "Denominator is the root, numerator is the power",
                "body": (
                    "$x^{m/n} = \\left(\\sqrt[n]{x}\\right)^{m}$. Split the fraction and each part "
                    "does its own job: the bottom takes a root, the top raises a power. Take the "
                    "ROOT first and the numbers stay small."
                ),
                "beats": [
                    "$8^{2/3}$: cube root first → $2$",
                    "Then square it → $4$",
                    "Power first works too: $\\sqrt[3]{64} = 4$",
                    "Same answer, harder arithmetic",
                ],
            },
            {"kind": "worked", "title": "Three rational powers, root first", "problemId": "im2-u1-l1-we2"},
            tap(
                "Which root, which power?",
                "What is $32^{3/5}$?",
                ["$8$", "$2$", "$96$", "$\\sqrt[3]{32^5}$"],
                0,
                "The denominator $5$ is the root index: $\\sqrt[5]{32} = 2$. The numerator $3$ is "
                "the power: $2^{3} = 8$. Answering $2$ stops after the root; answering "
                "$\\sqrt[3]{32^5}$ swaps the two roles, giving a completely different number.",
                [
                    "Eq(32**Rational(1,5), 2)",
                    "Eq(2**3, 8)",
                    "Eq(32**Rational(3,5), 8)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Two independent instructions",
                "title": "A minus sign means reciprocal, not negative",
                "body": (
                    "$8^{-2/3} = \\frac{1}{8^{2/3}} = \\frac{1}{4}$. The minus flips the fraction; "
                    "the $\\frac{2}{3}$ takes a root and a power. Both apply, and the result is "
                    "positive — a negative exponent never produces a negative answer."
                ),
            },
            {"kind": "worked", "title": "Converting both directions", "problemId": "im2-u1-l1-we3"},
            {
                "kind": "tip",
                "title": "The rules did not change — only what may sit in the exponent",
                "body": (
                    "$x^{a} \\cdot x^{b} = x^{a+b}$ and $\\frac{x^{a}}{x^{b}} = x^{a-b}$ hold "
                    "exactly as before, now with fractions in the exponent. The whole point of "
                    "the forcing argument was to extend the domain WITHOUT changing the rules."
                ),
            },
            {"kind": "worked", "title": "The rules transfer intact", "problemId": "im2-u1-l1-we4"},
            {
                "kind": "teach",
                "eyebrow": "One restriction",
                "title": "Even roots need a non-negative base",
                "body": (
                    "$(-8)^{1/3} = -2$ is perfectly fine — an odd root of a negative number "
                    "exists. But $(-9)^{1/2}$ is not real, because nothing real squares to $-9$. "
                    "That gap is exactly where complex numbers enter in Unit 4."
                ),
            },
            {"kind": "tryIt", "title": "Your turn — two rational powers", "problemId": "im2-u1-l1-t1"},
            {"kind": "tryIt", "title": "Your turn — a negative exponent", "problemId": "im2-u1-l1-t2"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "$x^{1/n} = \\sqrt[n]{x}$ is **forced** by the rule $(x^a)^b = x^{ab}$",
                    "$x^{m/n}$: denominator is the root, numerator is the power — root first",
                    "A negative exponent means a **reciprocal**, never a negative answer",
                    "All the old exponent rules hold unchanged on fractions",
                    "Odd roots of negatives are fine; even roots need a non-negative base",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 2 — N-RN.2: simplifying radicals
# ===========================================================================
def lesson_simplifying():
    return lesson(
        slug="simplifying-radicals",
        title="Simplifying Radicals",
        concrete=(
            "$\\sqrt{72}$ and $6\\sqrt{2}$ are the same number. One of them tells you at a glance "
            "that it is a bit over eight; the other tells you nothing until you reach for a "
            "calculator. Simplest radical form is not a ritual — it is the form in which you can "
            "see the size, compare two answers, and spot that two expressions match."
        ),
        objective=(
            "Simplify a radical by extracting perfect-power factors, using the product and "
            "quotient properties, and recognise when an expression is in simplest radical form."
        ),
        concept=[
            "**The product property.** For non-negative $a$ and $b$, "
            "$$\\sqrt{ab} = \\sqrt{a} \\cdot \\sqrt{b}.$$ "
            "It follows immediately from the exponent rules of the last lesson: "
            "$(ab)^{1/2} = a^{1/2} b^{1/2}$. This is the property that lets you split a radical "
            "into a piece you can simplify and a piece you cannot.",
            "**Simplifying is factoring out the largest perfect square.** For $\\sqrt{72}$, look "
            "for the biggest perfect square dividing $72$. That is $36$, so "
            "$$\\sqrt{72} = \\sqrt{36 \\cdot 2} = \\sqrt{36} \\cdot \\sqrt{2} = 6\\sqrt{2}.$$ "
            "If you spot a smaller square first it still works — you just repeat. "
            "$\\sqrt{72} = \\sqrt{4 \\cdot 18} = 2\\sqrt{18} = 2\\sqrt{9 \\cdot 2} = 6\\sqrt{2}$, "
            "same destination by a longer road.",
            "**Prime factorisation never fails.** When the largest square is not obvious, break "
            "the number into primes and pull out every PAIR: "
            "$72 = 2^{3} \\cdot 3^{2}$, so one pair of $2$s and one pair of $3$s escape as "
            "$2 \\cdot 3 = 6$, leaving a single $2$ inside. For a cube root, pull out every "
            "TRIPLE instead.",
            "**The quotient property.** $\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}$ for "
            "$b \\neq 0$. Simplify the top and bottom separately: "
            "$\\sqrt{\\frac{50}{9}} = \\frac{\\sqrt{50}}{3} = \\frac{5\\sqrt{2}}{3}$.",
            "**Variables under a radical.** $\\sqrt{x^{6}} = x^{3}$ because $\\frac{6}{2} = 3$ — "
            "halve the exponent. For an odd exponent, split off one factor: "
            "$\\sqrt{x^{7}} = \\sqrt{x^{6} \\cdot x} = x^{3}\\sqrt{x}$. (Throughout this unit "
            "variables under an even root are assumed non-negative, so no absolute-value bars are "
            "needed.)",
            "**What 'simplest form' actually requires.** Three conditions: no perfect-power factor "
            "left inside the radical, no fraction inside a radical, and no radical in a "
            "denominator. The third is the subject of the next lesson.",
        ],
        key_idea=(
            "$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$ lets you split off the largest perfect square and "
            "extract it. Prime-factorise when the square is not obvious, and pull out one factor "
            "per pair."
        ),
        facts=[
            fact(
                "Product property",
                "\\sqrt{ab} = \\sqrt{a} \\cdot \\sqrt{b} \\quad (a, b \\ge 0)",
                "A direct consequence of (ab)^(1/2) = a^(1/2)·b^(1/2) from the last lesson.",
            ),
            fact(
                "Quotient property",
                "\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}} \\quad (a \\ge 0, b > 0)",
                "Simplify numerator and denominator separately.",
            ),
            fact(
                "Pull out pairs (or triples)",
                "\\sqrt{2^3 \\cdot 3^2} = 2 \\cdot 3 \\sqrt{2} = 6\\sqrt{2}",
                "Each PAIR of identical prime factors escapes a square root; each TRIPLE escapes a "
                "cube root.",
            ),
        ],
        worked=[
            problem(
                "im2-u1-l2-we1",
                "Simplify $\\sqrt{72}$ two ways: by spotting the largest perfect square, and by "
                "prime factorisation.",
                "**Way one — largest perfect square.** The perfect squares dividing $72$ are "
                "$4$, $9$ and $36$. Take the largest:"
                "$$\\sqrt{72} = \\sqrt{36 \\cdot 2} = \\sqrt{36} \\cdot \\sqrt{2} = 6\\sqrt{2}.$$"
                "**Way two — prime factorisation.**"
                "$$72 = 2 \\cdot 2 \\cdot 2 \\cdot 3 \\cdot 3 = 2^{3} \\cdot 3^{2}.$$"
                "Pull out one factor per PAIR: the two $2$s give a $2$, the two $3$s give a $3$, "
                "and the leftover $2$ stays inside:"
                "$$\\sqrt{72} = 2 \\cdot 3 \\cdot \\sqrt{2} = 6\\sqrt{2}.$$"
                "**Check numerically.** $6\\sqrt{2} \\approx 6 \\times 1.41421 = 8.485$, and "
                "$\\sqrt{72} \\approx 8.485$ ✓. Squaring the answer is the exact check: "
                "$(6\\sqrt{2})^{2} = 36 \\times 2 = 72$ ✓"
                "**Why simplest form is worth the trouble.** From $6\\sqrt{2}$ you can see the "
                "answer is a bit over $8$ without a calculator, because $\\sqrt{2}$ is a shade "
                "over $1.4$. From $\\sqrt{72}$ you can see nothing.",
                [
                    "Eq(72, 36*2)",
                    "Eq(72, 2**3 * 3**2)",
                    "Eq((6*sqrt(2))**2, 72)",
                    "Eq(simplify(sqrt(72)), 6*sqrt(2))",
                ],
            ),
            problem(
                "im2-u1-l2-we2",
                "Simplify $\\sqrt{200}$, $\\sqrt[3]{54}$ and $\\sqrt{\\dfrac{50}{9}}$.",
                "**The square root.** The largest perfect square dividing $200$ is $100$:"
                "$$\\sqrt{200} = \\sqrt{100 \\cdot 2} = 10\\sqrt{2}.$$"
                "**The cube root.** Here look for a perfect CUBE factor instead. "
                "$54 = 27 \\cdot 2$ and $27 = 3^{3}$:"
                "$$\\sqrt[3]{54} = \\sqrt[3]{27 \\cdot 2} = 3\\sqrt[3]{2}.$$"
                "Note the $2$ cannot come out — you would need three of them, not one."
                "**The fraction under the radical.** Split top and bottom by the quotient property:"
                "$$\\sqrt{\\frac{50}{9}} = \\frac{\\sqrt{50}}{\\sqrt{9}} = "
                "\\frac{5\\sqrt{2}}{3}.$$"
                "**Check each by squaring or cubing.** $(10\\sqrt{2})^{2} = 200$ ✓; "
                "$(3\\sqrt[3]{2})^{3} = 27 \\times 2 = 54$ ✓; "
                "$\\left(\\frac{5\\sqrt{2}}{3}\\right)^{2} = \\frac{50}{9}$ ✓",
                [
                    "Eq((10*sqrt(2))**2, 200)",
                    "Eq(simplify(sqrt(200)), 10*sqrt(2))",
                    "Eq((3*2**Rational(1,3))**3, 54)",
                    "Eq(simplify((5*sqrt(2)/3)**2), Rational(50,9))",
                ],
            ),
            problem(
                "im2-u1-l2-we3",
                "Simplify $\\sqrt{48x^{5}y^{2}}$, assuming $x$ and $y$ are non-negative.",
                "**Handle the number.** The largest perfect square dividing $48$ is $16$, so "
                "$48 = 16 \\cdot 3$ and the $16$ contributes a $4$."
                "**Handle each variable.** Halve the exponent where it is even; split off one "
                "factor where it is odd:"
                "$$x^{5} = x^{4} \\cdot x \\quad\\Longrightarrow\\quad \\sqrt{x^{5}} = "
                "x^{2}\\sqrt{x},$$"
                "$$\\sqrt{y^{2}} = y.$$"
                "**Put it together.**"
                "$$\\sqrt{48x^{5}y^{2}} = 4x^{2}y\\sqrt{3x}.$$"
                "**Check with numbers.** Take $x = 3$, $y = 2$. Inside: "
                "$48 \\times 243 \\times 4 = 46\\,656$, and $\\sqrt{46\\,656} = 216$. The "
                "simplified form: $4 \\times 9 \\times 2 \\times \\sqrt{9} = 72 \\times 3 = 216$ ✓ "
                "— exact agreement, which is what confirms the extraction was done correctly.",
                [
                    "Eq(48*3**5*2**2, 46656)",
                    "Eq(sqrt(46656), 216)",
                    "Eq(4*3**2*2*sqrt(3*3), 216)",
                    "Eq(48, 16*3)",
                ],
            ),
            problem(
                "im2-u1-l2-we4",
                "Decide whether each is in simplest radical form, and simplify if not: "
                "$3\\sqrt{20}$, $\\sqrt{\\dfrac{3}{4}}$, $2\\sqrt{15}$.",
                "**The first one is not simplest.** In $3\\sqrt{20}$ the $20$ still contains the "
                "perfect square $4$:"
                "$$3\\sqrt{20} = 3\\sqrt{4 \\cdot 5} = 3 \\cdot 2\\sqrt{5} = 6\\sqrt{5}.$$"
                "The coefficient outside multiplies whatever comes out."
                "**The second one is not simplest either.** A fraction under a radical violates "
                "the second condition:"
                "$$\\sqrt{\\frac{3}{4}} = \\frac{\\sqrt{3}}{\\sqrt{4}} = \\frac{\\sqrt{3}}{2}.$$"
                "**The third one is already simplest.** Here $15 = 3 \\times 5$, two distinct primes "
                "with no repeats, so nothing can be pulled out. There is no fraction inside and no "
                "radical in a denominator. Done."
                "**The three conditions, restated.** No perfect-power factor inside; no fraction "
                "inside; no radical in a denominator. An expression is simplest exactly when all "
                "three hold.",
                [
                    "Eq(simplify(3*sqrt(20)), 6*sqrt(5)),".rstrip(","),
                    "Eq((6*sqrt(5))**2, 180)",
                    "Eq((3*sqrt(20))**2, 180)",
                    "Eq(simplify(sqrt(Rational(3,4))), sqrt(3)/2)",
                    "Eq(15, 3*5)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Splitting a radical across addition: writing √(9 + 16) as 3 + 4.",
                "The product property covers multiplication only. √25 = 5, not 7. There is no "
                "rule for the square root of a sum.",
            ),
            mistake(
                "Pulling out a single factor instead of a pair.",
                "√(2³) is 2√2, not 4√2. Each PAIR of identical factors releases ONE copy — count "
                "the pairs, not the factors.",
            ),
            mistake(
                "Stopping before the radicand is fully reduced.",
                "3√20 is not simplest — 20 still holds a 4. Check the remaining radicand for "
                "perfect squares every time before declaring done.",
            ),
            mistake(
                "Using pairs when simplifying a cube root.",
                "A cube root releases one factor per TRIPLE. ∛54 = 3∛2 because 54 = 3³·2 — the "
                "lone 2 stays inside.",
            ),
        ],
        try_it=[
            problem(
                "im2-u1-l2-t1",
                "Simplify $\\sqrt{98}$ and $\\sqrt{45}$.",
                "$98 = 49 \\cdot 2$, so $\\sqrt{98} = 7\\sqrt{2}$. And $45 = 9 \\cdot 5$, so "
                "$\\sqrt{45} = 3\\sqrt{5}$. Check by squaring: $49 \\times 2 = 98$ ✓ and "
                "$9 \\times 5 = 45$ ✓",
                [
                    "Eq((7*sqrt(2))**2, 98)",
                    "Eq((3*sqrt(5))**2, 45)",
                    "Eq(simplify(sqrt(98)), 7*sqrt(2))",
                ],
            ),
            problem(
                "im2-u1-l2-t2",
                "Simplify $\\sqrt[3]{80}$.",
                "Look for a perfect cube factor: $80 = 8 \\cdot 10$ and $8 = 2^{3}$, so "
                "$\\sqrt[3]{80} = 2\\sqrt[3]{10}$. Check: $2^{3} \\times 10 = 80$ ✓",
                [
                    "Eq((2*10**Rational(1,3))**3, 80)",
                    "Eq(80, 8*10)",
                ],
            ),
            problem(
                "im2-u1-l2-t3",
                "Simplify $\\sqrt{75a^{3}}$, assuming $a \\ge 0$.",
                "$75 = 25 \\cdot 3$ gives a $5$; $a^{3} = a^{2} \\cdot a$ gives an $a$ with one "
                "left inside. So $\\sqrt{75a^{3}} = 5a\\sqrt{3a}$. Check at $a = 3$: inside is "
                "$75 \\times 27 = 2025$ and $\\sqrt{2025} = 45$; the form gives "
                "$5 \\times 3 \\times \\sqrt{9} = 45$ ✓",
                [
                    "Eq(75*3**3, 2025)",
                    "Eq(sqrt(2025), 45)",
                    "Eq(5*3*sqrt(3*3), 45)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "N-RN.2",
                "title": "Why bother simplifying at all",
                "body": (
                    "$\\sqrt{72}$ and $6\\sqrt{2}$ are the same number, but only one of them lets "
                    "you see it is a bit over $8$, compare it with another answer, or notice that "
                    "two expressions are secretly equal."
                ),
            },
            {
                "kind": "teach",
                "eyebrow": "The engine",
                "title": "The product property, and where it comes from",
                "body": (
                    "$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$ is not a new rule — it is "
                    "$(ab)^{1/2} = a^{1/2}b^{1/2}$, the exponent rule from Lesson 1 written with "
                    "radical signs. That is what licenses splitting a radical in two."
                ),
                "beats": [
                    "$\\sqrt{72} = \\sqrt{36 \\cdot 2}$",
                    "$= \\sqrt{36} \\cdot \\sqrt{2}$",
                    "$= 6\\sqrt{2}$",
                    "Split off the largest perfect square",
                ],
            },
            {"kind": "worked", "title": "Two routes to the same simplest form", "problemId": "im2-u1-l2-we1"},
            {
                "kind": "factorTree",
                "eyebrow": "When the square is not obvious",
                "title": "Prime-factorise and count pairs",
                "teach": (
                    "$72 = 2^{3} \\cdot 3^{2}$. Each PAIR of identical primes releases one copy: "
                    "the pair of $2$s gives a $2$, the pair of $3$s gives a $3$, and the odd $2$ "
                    "stays inside. So $6\\sqrt{2}$."
                ),
                "config": {"n": 72},
            },
            tap(
                "How many escape?",
                "Simplifying $\\sqrt{2^{5}}$, how many factors of $2$ come outside the radical?",
                ["$2$", "$5$", "$3$", "$1$"],
                0,
                "$2^{5}$ contains two complete PAIRS with one factor left over: "
                "$\\sqrt{2^5} = \\sqrt{2^4 \\cdot 2} = 4\\sqrt{2}$, so two $2$s escape as the "
                "product $4$. Answering $5$ counts the factors rather than the pairs. "
                "Check: $4^2 \\times 2 = 32 = 2^5$ ✓",
                [
                    "Eq(2**5, 32)",
                    "Eq((4*sqrt(2))**2, 32)",
                    "Eq(simplify(sqrt(32)), 4*sqrt(2))",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Higher roots",
                "title": "Cube roots want triples",
                "body": (
                    "A square root releases one factor per pair; a cube root needs a TRIPLE. "
                    "$\\sqrt[3]{54} = \\sqrt[3]{3^{3} \\cdot 2} = 3\\sqrt[3]{2}$ — the lone $2$ "
                    "has no companions and stays inside."
                ),
            },
            {"kind": "worked", "title": "A square root, a cube root, a fraction", "problemId": "im2-u1-l2-we2"},
            {
                "kind": "teach",
                "eyebrow": "Variables",
                "title": "Halve the exponent; split off the odd one",
                "body": (
                    "$\\sqrt{x^{6}} = x^{3}$ — halve it. For an odd exponent, peel one off first: "
                    "$\\sqrt{x^{7}} = \\sqrt{x^{6} \\cdot x} = x^{3}\\sqrt{x}$. (Variables under "
                    "even roots are assumed non-negative here.)"
                ),
            },
            {"kind": "worked", "title": "Numbers and variables together", "problemId": "im2-u1-l2-we3"},
            {
                "kind": "tip",
                "title": "There is no rule for the root of a sum",
                "body": (
                    "$\\sqrt{9 + 16} = \\sqrt{25} = 5$, NOT $3 + 4 = 7$. The product property "
                    "covers multiplication and division only. Whenever you are tempted to split "
                    "across a $+$, test it on $9$ and $16$ — the counterexample is immediate."
                ),
            },
            tap(
                "Is this simplified?",
                "Is $2\\sqrt{18}$ in simplest radical form?",
                [
                    "Yes",
                    "No — it is $6\\sqrt{2}$",
                    "No — it is $2\\sqrt{9}\\sqrt{2}$",
                    "No — it is $\\sqrt{36}$",
                ],
                1,
                "$18$ still contains the perfect square $9$: "
                "$2\\sqrt{18} = 2\\sqrt{9 \\cdot 2} = 2 \\cdot 3\\sqrt{2} = 6\\sqrt{2}$. "
                "Option C is a mid-working line, not a final form. Check by squaring both: "
                "$(2\\sqrt{18})^2 = 72$ and $(6\\sqrt{2})^2 = 72$ ✓",
                [
                    "Eq((2*sqrt(18))**2, 72)",
                    "Eq((6*sqrt(2))**2, 72)",
                    "Eq(simplify(2*sqrt(18)), 6*sqrt(2))",
                ],
            ),
            {"kind": "worked", "title": "The three conditions applied", "problemId": "im2-u1-l2-we4"},
            {"kind": "tryIt", "title": "Your turn — two square roots", "problemId": "im2-u1-l2-t1"},
            {"kind": "tryIt", "title": "Your turn — with a variable", "problemId": "im2-u1-l2-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "$\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$ — from the exponent rule, not a new law",
                    "Extract the largest perfect square, or prime-factorise and count **pairs**",
                    "Cube roots release one factor per **triple**",
                    "Variables: halve the exponent, split off an odd leftover",
                    "Simplest = no perfect-power factor inside, no fraction inside, no radical below",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 3 — operations with radicals
# ===========================================================================
def lesson_operations():
    return lesson(
        slug="operations-with-radicals",
        title="Adding, Multiplying & Rationalising",
        concrete=(
            "$3\\sqrt{2} + 5\\sqrt{2} = 8\\sqrt{2}$ for exactly the reason that "
            "$3x + 5x = 8x$ — you are counting the same object. And $3\\sqrt{2} + 5\\sqrt{3}$ "
            "will not combine for the same reason $3x + 5y$ will not. Radicals behave like "
            "variables, which means you already know most of this."
        ),
        objective=(
            "Add and subtract like radicals, multiply radical expressions including binomials, and "
            "rationalise a denominator using a conjugate."
        ),
        concept=[
            "**Like radicals combine; unlike ones do not.** Two radical terms are LIKE when their "
            "radicands and indices match. $3\\sqrt{2}$ and $5\\sqrt{2}$ are like, so they add to "
            "$8\\sqrt{2}$ exactly as $3x + 5x = 8x$. $3\\sqrt{2}$ and $5\\sqrt{3}$ are not, and "
            "no manipulation will merge them.",
            "**Simplify FIRST — terms often become like.** $\\sqrt{8} + \\sqrt{18}$ looks "
            "hopeless until you simplify: $2\\sqrt{2} + 3\\sqrt{2} = 5\\sqrt{2}$. Skipping the "
            "simplification step is the most common way to declare two terms uncombinable when "
            "they are not.",
            "**Multiplying uses the product property forwards.** "
            "$\\sqrt{6} \\cdot \\sqrt{10} = \\sqrt{60} = 2\\sqrt{15}$: multiply the radicands, "
            "then simplify. Coefficients multiply separately — "
            "$2\\sqrt{3} \\cdot 5\\sqrt{6} = 10\\sqrt{18} = 30\\sqrt{2}$.",
            "**Binomials expand exactly as in algebra.** $(\\sqrt{3} + 2)(\\sqrt{3} - 5)$ expands "
            "term by term like any pair of binomials, using $\\sqrt{3} \\cdot \\sqrt{3} = 3$. The "
            "radical is just an object being multiplied; nothing new is required.",
            "**Rationalising a single-term denominator.** Multiply above and below by the radical: "
            "$$\\frac{5}{\\sqrt{3}} = \\frac{5}{\\sqrt{3}} \\cdot \\frac{\\sqrt{3}}{\\sqrt{3}} "
            "= \\frac{5\\sqrt{3}}{3}.$$ "
            "You are multiplying by $1$, so the value is unchanged — only the form.",
            "**Conjugates clear a two-term denominator.** The conjugate of $\\sqrt{5} + 2$ is "
            "$\\sqrt{5} - 2$, and multiplying them gives a difference of squares with no radical "
            "left: $(\\sqrt{5})^{2} - 2^{2} = 5 - 4 = 1$. That is why conjugates work — the "
            "cross terms cancel and the squares kill the radicals.",
        ],
        key_idea=(
            "Like radicals add like like terms — simplify first so more of them match. Multiply "
            "radicands directly. Clear a denominator by multiplying by the radical, or by the "
            "conjugate when there are two terms."
        ),
        facts=[
            fact(
                "Combining like radicals",
                "a\\sqrt{c} + b\\sqrt{c} = (a + b)\\sqrt{c}",
                "Same radicand, same index. Identical in form to a·x + b·x = (a+b)x.",
            ),
            fact(
                "Multiplying",
                "a\\sqrt{p} \\cdot b\\sqrt{q} = ab\\sqrt{pq}",
                "Coefficients multiply, radicands multiply — then simplify the result.",
            ),
            fact(
                "The conjugate",
                "(\\sqrt{a} + b)(\\sqrt{a} - b) = a - b^{2}",
                "A difference of squares: the cross terms cancel and the radical squares away.",
            ),
        ],
        worked=[
            problem(
                "im2-u1-l3-we1",
                "Simplify $\\sqrt{8} + \\sqrt{18} - \\sqrt{50}$.",
                "**Simplify each term first** — this is what makes them comparable:"
                "$$\\sqrt{8} = \\sqrt{4 \\cdot 2} = 2\\sqrt{2},$$"
                "$$\\sqrt{18} = \\sqrt{9 \\cdot 2} = 3\\sqrt{2},$$"
                "$$\\sqrt{50} = \\sqrt{25 \\cdot 2} = 5\\sqrt{2}.$$"
                "**Now they are all like terms** — every one is a multiple of $\\sqrt{2}$:"
                "$$2\\sqrt{2} + 3\\sqrt{2} - 5\\sqrt{2} = (2 + 3 - 5)\\sqrt{2} = 0.$$"
                "The expression is exactly zero."
                "**Check numerically.** $\\sqrt{8} \\approx 2.828$, $\\sqrt{18} \\approx 4.243$, "
                "$\\sqrt{50} \\approx 7.071$, and $2.828 + 4.243 - 7.071 = 0$ ✓"
                "**The lesson.** Before simplifying, the three terms looked entirely unrelated. "
                "Simplification revealed they were all the same object counted differently — and "
                "that they cancelled completely.",
                [
                    "Eq(simplify(sqrt(8)), 2*sqrt(2))",
                    "Eq(simplify(sqrt(18)), 3*sqrt(2))",
                    "Eq(simplify(sqrt(50)), 5*sqrt(2))",
                    "Eq(simplify(sqrt(8) + sqrt(18) - sqrt(50)), 0)",
                ],
            ),
            problem(
                "im2-u1-l3-we2",
                "Multiply and simplify: $2\\sqrt{6} \\cdot 5\\sqrt{10}$, and "
                "$\\sqrt{3}\\left(\\sqrt{12} + \\sqrt{27}\\right)$.",
                "**First product.** Coefficients multiply, radicands multiply:"
                "$$2\\sqrt{6} \\cdot 5\\sqrt{10} = 10\\sqrt{60}.$$"
                "Now simplify $\\sqrt{60} = \\sqrt{4 \\cdot 15} = 2\\sqrt{15}$:"
                "$$10 \\cdot 2\\sqrt{15} = 20\\sqrt{15}.$$"
                "**Second product — distribute first.**"
                "$$\\sqrt{3} \\cdot \\sqrt{12} + \\sqrt{3} \\cdot \\sqrt{27} "
                "= \\sqrt{36} + \\sqrt{81} = 6 + 9 = 15.$$"
                "Both radicals vanished entirely — the products happened to be perfect squares."
                "**Check the second another way.** Simplify inside first: "
                "$\\sqrt{12} = 2\\sqrt{3}$ and $\\sqrt{27} = 3\\sqrt{3}$, so the bracket is "
                "$5\\sqrt{3}$, and $\\sqrt{3} \\cdot 5\\sqrt{3} = 5 \\cdot 3 = 15$ ✓ — same "
                "answer by a different route, which is a genuine check rather than a repetition.",
                [
                    "Eq(simplify(2*sqrt(6)*5*sqrt(10)), 20*sqrt(15))",
                    "Eq(simplify(sqrt(3)*sqrt(12)), 6)",
                    "Eq(simplify(sqrt(3)*sqrt(27)), 9)",
                    "Eq(simplify(sqrt(3)*(sqrt(12) + sqrt(27))), 15)",
                ],
            ),
            problem(
                "im2-u1-l3-we3",
                "Expand $\\left(\\sqrt{5} + 3\\right)\\left(\\sqrt{5} - 2\\right)$.",
                "**Expand term by term, exactly as with any binomials.**"
                "$$\\sqrt{5} \\cdot \\sqrt{5} = 5,$$"
                "$$\\sqrt{5} \\cdot (-2) = -2\\sqrt{5},$$"
                "$$3 \\cdot \\sqrt{5} = 3\\sqrt{5},$$"
                "$$3 \\cdot (-2) = -6.$$"
                "**Collect.** The two middle terms are like radicals:"
                "$$5 - 2\\sqrt{5} + 3\\sqrt{5} - 6 = -1 + \\sqrt{5}.$$"
                "**Check numerically.** $\\sqrt{5} \\approx 2.2361$, so the factors are about "
                "$5.2361$ and $0.2361$, whose product is $\\approx 1.2361$. And "
                "$-1 + 2.2361 = 1.2361$ ✓"
                "**Note what happened to the radical.** $\\sqrt{5} \\cdot \\sqrt{5} = 5$ removed "
                "one radical entirely, but the cross terms left a $\\sqrt{5}$ behind. That is the "
                "general case — and it is precisely why the NEXT technique chooses the second "
                "factor so the cross terms cancel.",
                [
                    "Eq(simplify((sqrt(5) + 3)*(sqrt(5) - 2)), -1 + sqrt(5))",
                    "Eq(simplify(sqrt(5)*sqrt(5)), 5)",
                    "Eq(-2 + 3, 1)",
                ],
            ),
            problem(
                "im2-u1-l3-we4",
                "Rationalise the denominators: $\\dfrac{6}{\\sqrt{3}}$ and "
                "$\\dfrac{4}{\\sqrt{7} - 2}$.",
                "**Single-term denominator.** Multiply above and below by $\\sqrt{3}$ — that is "
                "multiplying by $1$, so the value cannot change:"
                "$$\\frac{6}{\\sqrt{3}} \\cdot \\frac{\\sqrt{3}}{\\sqrt{3}} "
                "= \\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}.$$"
                "**Two-term denominator — use the conjugate.** The conjugate of $\\sqrt{7} - 2$ "
                "is $\\sqrt{7} + 2$:"
                "$$\\frac{4}{\\sqrt{7} - 2} \\cdot \\frac{\\sqrt{7} + 2}{\\sqrt{7} + 2} "
                "= \\frac{4(\\sqrt{7} + 2)}{(\\sqrt{7})^{2} - 2^{2}} "
                "= \\frac{4(\\sqrt{7} + 2)}{7 - 4} = \\frac{4(\\sqrt{7} + 2)}{3}.$$"
                "**Why the conjugate works.** Multiplying $(\\sqrt{7} - 2)(\\sqrt{7} + 2)$ gives "
                "the cross terms $+2\\sqrt{7}$ and $-2\\sqrt{7}$, which cancel, leaving "
                "$7 - 4 = 3$ — a plain integer. The sign flip is chosen precisely to make that "
                "cancellation happen."
                "**Check numerically.** $\\sqrt{7} \\approx 2.6458$, so the original is "
                "$\\frac{4}{0.6458} \\approx 6.194$, and the answer is "
                "$\\frac{4(4.6458)}{3} \\approx 6.194$ ✓",
                [
                    "Eq(simplify(6/sqrt(3)), 2*sqrt(3))",
                    "Eq(simplify((sqrt(7) - 2)*(sqrt(7) + 2)), 3)",
                    "Eq(simplify(4/(sqrt(7) - 2)), simplify(4*(sqrt(7) + 2)/3))",
                    "Eq(7 - 4, 3)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Adding unlike radicals: writing √2 + √3 as √5.",
                "Test it: √2 + √3 ≈ 3.15, but √5 ≈ 2.24. Only LIKE radicals combine — the "
                "radicands must match.",
            ),
            mistake(
                "Declaring terms uncombinable before simplifying them.",
                "√8 + √18 looks unlike and becomes 2√2 + 3√2 = 5√2. Always simplify each term "
                "first, then look again.",
            ),
            mistake(
                "Adding the radicands when multiplying: √6 · √10 = √16.",
                "Multiplying radicals MULTIPLIES the radicands: √60 = 2√15. Adding them is a "
                "different operation entirely.",
            ),
            mistake(
                "Using the same sign for the conjugate.",
                "The conjugate of √7 − 2 is √7 + 2 — the sign FLIPS. Keeping it would give "
                "(√7 − 2)² = 11 − 4√7, which still contains a radical.",
            ),
        ],
        try_it=[
            problem(
                "im2-u1-l3-t1",
                "Simplify $\\sqrt{27} + \\sqrt{75}$.",
                "$\\sqrt{27} = 3\\sqrt{3}$ and $\\sqrt{75} = 5\\sqrt{3}$, so the sum is "
                "$8\\sqrt{3}$. Check: $8\\sqrt{3} \\approx 13.86$, and "
                "$5.196 + 8.660 = 13.86$ ✓",
                [
                    "Eq(simplify(sqrt(27)), 3*sqrt(3))",
                    "Eq(simplify(sqrt(75)), 5*sqrt(3))",
                    "Eq(simplify(sqrt(27) + sqrt(75)), 8*sqrt(3))",
                ],
            ),
            problem(
                "im2-u1-l3-t2",
                "Expand $\\left(\\sqrt{2} + 4\\right)^{2}$.",
                "Square the binomial: $(\\sqrt{2})^{2} + 2(4)(\\sqrt{2}) + 16 = "
                "2 + 8\\sqrt{2} + 16 = 18 + 8\\sqrt{2}$. Note the middle term keeps a radical — "
                "squaring a binomial does not remove it.",
                [
                    "Eq(simplify((sqrt(2) + 4)**2), 18 + 8*sqrt(2))",
                    "Eq(simplify((sqrt(2))**2), 2)",
                ],
            ),
            problem(
                "im2-u1-l3-t3",
                "Rationalise $\\dfrac{10}{\\sqrt{5} + 3}$.",
                "Multiply above and below by the conjugate $\\sqrt{5} - 3$. The denominator "
                "becomes $5 - 9 = -4$, so"
                "$$\\frac{10(\\sqrt{5} - 3)}{-4} = \\frac{-5(\\sqrt{5} - 3)}{2} "
                "= \\frac{15 - 5\\sqrt{5}}{2}.$$"
                "A negative denominator is fine mid-working — just carry the sign into the "
                "numerator at the end.",
                [
                    "Eq(simplify((sqrt(5) + 3)*(sqrt(5) - 3)), -4)",
                    "Eq(simplify(10/(sqrt(5) + 3)), simplify((15 - 5*sqrt(5))/2))",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The whole idea",
                "title": "A radical behaves like a variable",
                "body": (
                    "$3\\sqrt{2} + 5\\sqrt{2} = 8\\sqrt{2}$ for the same reason "
                    "$3x + 5x = 8x$: you are counting copies of one object. And $3\\sqrt{2} + "
                    "5\\sqrt{3}$ refuses to combine for the same reason $3x + 5y$ does."
                ),
                "beats": [
                    "Same radicand + same index = **like** terms",
                    "Like terms add by adding coefficients",
                    "Unlike terms simply stay apart",
                    "Everything you know about $x$ transfers",
                ],
            },
            {
                "kind": "tip",
                "title": "Simplify first — terms become like",
                "body": (
                    "$\\sqrt{8} + \\sqrt{18}$ looks uncombinable and is not: it is "
                    "$2\\sqrt{2} + 3\\sqrt{2} = 5\\sqrt{2}$. Declaring two terms unlike before "
                    "simplifying them is the single most common error in this lesson."
                ),
            },
            {"kind": "worked", "title": "Three terms that cancel completely", "problemId": "im2-u1-l3-we1"},
            tap(
                "Can these combine?",
                "Can $\\sqrt{12} + \\sqrt{75}$ be written as a single radical term?",
                [
                    "No — the radicands differ",
                    "Yes — it is $7\\sqrt{3}$",
                    "Yes — it is $\\sqrt{87}$",
                    "Yes — it is $9\\sqrt{3}$",
                ],
                1,
                "Simplify first: $\\sqrt{12} = 2\\sqrt{3}$ and $\\sqrt{75} = 5\\sqrt{3}$, so the "
                "sum is $7\\sqrt{3}$. Option A gives up too early; option C adds the radicands, "
                "which is never valid. Check: $7\\sqrt{3} \\approx 12.12$, and "
                "$3.46 + 8.66 = 12.12$ ✓",
                [
                    "Eq(simplify(sqrt(12)), 2*sqrt(3))",
                    "Eq(simplify(sqrt(75)), 5*sqrt(3))",
                    "Eq(simplify(sqrt(12) + sqrt(75)), 7*sqrt(3))",
                    "Ne(simplify(sqrt(12) + sqrt(75)), sqrt(87))",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Multiplying",
                "title": "Coefficients multiply, radicands multiply",
                "body": (
                    "$2\\sqrt{6} \\cdot 5\\sqrt{10} = 10\\sqrt{60}$, then simplify to "
                    "$20\\sqrt{15}$. The product property used forwards. Never ADD the radicands "
                    "— that is a different operation with a different answer."
                ),
            },
            {"kind": "worked", "title": "Products, including one that clears entirely", "problemId": "im2-u1-l3-we2"},
            {
                "kind": "teach",
                "eyebrow": "Binomials",
                "title": "Expand exactly as you always have",
                "body": (
                    "$(\\sqrt{5} + 3)(\\sqrt{5} - 2)$ multiplies out term by term like any pair of "
                    "brackets, using $\\sqrt{5} \\cdot \\sqrt{5} = 5$. Nothing new is needed — the "
                    "radical is just an object."
                ),
            },
            {"kind": "worked", "title": "A binomial product", "problemId": "im2-u1-l3-we3"},
            {
                "kind": "teach",
                "eyebrow": "The third condition",
                "title": "Clearing a radical from a denominator",
                "body": (
                    "One term below? Multiply top and bottom by that radical. Two terms below? "
                    "Multiply by the CONJUGATE — the same expression with the middle sign flipped "
                    "— and the cross terms cancel into a difference of squares."
                ),
                "beats": [
                    "$\\frac{5}{\\sqrt{3}} \\to \\frac{5\\sqrt{3}}{3}$",
                    "Conjugate of $\\sqrt{5} + 2$ is $\\sqrt{5} - 2$",
                    "$(\\sqrt{5}+2)(\\sqrt{5}-2) = 5 - 4 = 1$",
                    "You multiply by $1$, so the value never changes",
                ],
            },
            tap(
                "What is the conjugate?",
                "What should you multiply $\\dfrac{3}{\\sqrt{11} + 4}$ by, top and bottom?",
                [
                    "$\\sqrt{11} + 4$",
                    "$\\sqrt{11} - 4$",
                    "$\\sqrt{11}$",
                    "$4 - \\sqrt{11}$",
                ],
                1,
                "The conjugate flips the middle sign: $\\sqrt{11} - 4$. Then the denominator "
                "becomes $11 - 16 = -5$, with no radical left. Option A squares the denominator "
                "and leaves $27 + 8\\sqrt{11}$ — still irrational. Option D is the conjugate "
                "negated; it also clears the radical but flips the sign unnecessarily.",
                [
                    "Eq(simplify((sqrt(11) + 4)*(sqrt(11) - 4)), -5)",
                    "Eq(simplify((sqrt(11) + 4)**2), 27 + 8*sqrt(11))",
                ],
            ),
            {"kind": "worked", "title": "Both rationalising techniques", "problemId": "im2-u1-l3-we4"},
            {"kind": "tryIt", "title": "Your turn — combine after simplifying", "problemId": "im2-u1-l3-t1"},
            {"kind": "tryIt", "title": "Your turn — rationalise with a conjugate", "problemId": "im2-u1-l3-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "Like radicals add like like terms — **simplify first** so more of them match",
                    "Multiplying multiplies the radicands; it never adds them",
                    "Binomials expand exactly as in algebra, with $\\sqrt{a} \\cdot \\sqrt{a} = a$",
                    "One term below: multiply by the radical. Two: multiply by the **conjugate**",
                    "Rationalising multiplies by $1$ — the value is untouched, only the form",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 4 — N-RN.3: rational and irrational numbers
# ===========================================================================
def lesson_rational_irrational():
    return lesson(
        slug="rational-and-irrational-numbers",
        title="Rational & Irrational Numbers",
        concrete=(
            "Add two fractions and you always get a fraction — that is obvious enough that nobody "
            "questions it. Add $2$ to $\\sqrt{3}$ and you can never get a fraction, no matter what "
            "you add. That second fact is not obvious at all, and proving it takes three lines of "
            "reasoning that are worth more than the result."
        ),
        objective=(
            "Classify numbers as rational or irrational, explain why the rationals are closed "
            "under the four operations, and prove that a rational plus an irrational is always "
            "irrational."
        ),
        concept=[
            "**A rational number is a ratio of integers.** Any number expressible as "
            "$\\frac{a}{b}$ with $a$ and $b$ integers and $b \\neq 0$. That includes every "
            "integer ($5 = \\frac{5}{1}$), every terminating decimal "
            "($0.25 = \\frac{1}{4}$), and every repeating decimal "
            "($0.\\overline{3} = \\frac{1}{3}$). An IRRATIONAL number is a real number that is "
            "not such a ratio — its decimal expansion never terminates and never repeats.",
            "**The usual suspects.** $\\sqrt{2}$, $\\sqrt{3}$, $\\sqrt{5}$ and $\\pi$ are "
            "irrational. But $\\sqrt{9} = 3$ is perfectly rational — a square root is irrational "
            "only when the radicand is not a perfect square. Checking that first prevents the "
            "commonest classification error.",
            "**The rationals are CLOSED under all four operations.** Combine two rationals and "
            "the result is always rational. The proof is just fraction arithmetic: "
            "$$\\frac{a}{b} + \\frac{c}{d} = \\frac{ad + bc}{bd},$$ "
            "and since integers are closed under multiplication and addition, both the numerator "
            "and denominator are integers — so the result is a ratio of integers. Products, "
            "differences and quotients work the same way (division excluding zero).",
            "**Rational + irrational is ALWAYS irrational.** Suppose $r$ is rational and $x$ is "
            "irrational, and suppose their sum $r + x$ were rational. Then "
            "$$x = (r + x) - r$$ "
            "would be the difference of two rationals — and by closure that difference is "
            "rational. But $x$ was irrational. Contradiction, so $r + x$ cannot be rational.",
            "**Rational × irrational is irrational — except for zero.** The same argument works "
            "with division: if $r \\neq 0$ is rational and $x$ irrational, then $rx$ rational "
            "would make $x = \\frac{rx}{r}$ rational, a contradiction. The exception matters: "
            "$0 \\times \\sqrt{2} = 0$, which is rational.",
            "**Irrational combined with irrational can go either way.** $\\sqrt{2} + \\sqrt{2} = "
            "2\\sqrt{2}$ is irrational, but $\\sqrt{2} + (-\\sqrt{2}) = 0$ is rational, and "
            "$\\sqrt{2} \\times \\sqrt{2} = 2$ is rational. So there is NO closure theorem for the "
            "irrationals — the only reliable statements are the ones involving a rational.",
        ],
        key_idea=(
            "The rationals are closed under the four operations. That closure is what proves a "
            "rational plus an irrational must be irrational — if the sum were rational, "
            "subtracting would make the irrational rational."
        ),
        facts=[
            fact(
                "Rational number",
                "\\frac{a}{b} \\ \\text{ with } a, b \\in \\mathbb{Z}, \\ b \\ne 0",
                "Includes integers, terminating decimals, and repeating decimals.",
            ),
            fact(
                "Closure of the rationals",
                "\\frac{a}{b} + \\frac{c}{d} = \\frac{ad + bc}{bd}",
                "Integer numerator over integer denominator — so the sum is rational. Same for "
                "−, × and ÷.",
            ),
            fact(
                "The key theorem",
                "r \\in \\mathbb{Q}, \\ x \\notin \\mathbb{Q} \\ \\Longrightarrow\\ "
                "r + x \\notin \\mathbb{Q}",
                "Proved by contradiction from closure. The same argument gives rx irrational "
                "whenever r ≠ 0.",
            ),
        ],
        worked=[
            problem(
                "im2-u1-l4-we1",
                "Classify each as rational or irrational: $\\sqrt{16}$, $\\sqrt{20}$, "
                "$0.\\overline{45}$, $\\frac{22}{7}$, $\\pi$.",
                "**The first is RATIONAL:** $\\sqrt{16} = 4$. The radicand is a perfect square, so "
                "the root is an integer. A radical sign does not make a number irrational."
                "**The second is IRRATIONAL:** $20$ is not a perfect square. Simplifying gives "
                "$2\\sqrt{5}$, and $\\sqrt{5}$ is irrational; a rational multiple of an irrational "
                "is irrational."
                "**The third is RATIONAL:** a repeating decimal is always a ratio of "
                "integers; here $0.\\overline{45} = \\frac{45}{99} = \\frac{5}{11}$. Check: "
                "$5 \\div 11 = 0.454545\\ldots$ ✓"
                "**The fourth is RATIONAL:** $\\frac{22}{7}$ is literally a ratio of integers. It is "
                "a well-known APPROXIMATION to $\\pi$, but being close to an irrational number does "
                "not make it one."
                "**The fifth is IRRATIONAL:** the decimal expansion of $\\pi$ never terminates and never "
                "repeats. Note $\\frac{22}{7} = 3.142857\\ldots$ while $\\pi = 3.141592\\ldots$ — "
                "they differ in the third decimal place, so they are genuinely different numbers.",
                [
                    "Eq(sqrt(16), 4)",
                    "Eq(Rational(45,99), Rational(5,11))",
                    "Eq(simplify(sqrt(20)), 2*sqrt(5))",
                    "Ne(Rational(22,7), pi)",
                    "Abs(Rational(22,7) - pi) < Rational(2,1000)",
                ],
            ),
            problem(
                "im2-u1-l4-we2",
                "Prove that the sum of two rational numbers is rational.",
                "**Set up.** Let the two numbers be rational, so each is a ratio of integers:"
                "$$r_1 = \\frac{a}{b}, \\qquad r_2 = \\frac{c}{d},$$"
                "with $a, b, c, d$ integers and $b, d \\neq 0$."
                "**Add them.**"
                "$$r_1 + r_2 = \\frac{a}{b} + \\frac{c}{d} = \\frac{ad + bc}{bd}.$$"
                "**Check the result is a ratio of integers.** The integers are closed under "
                "multiplication and addition, so $ad + bc$ is an integer and $bd$ is an integer. "
                "And $bd \\neq 0$, because a product of two non-zero numbers is non-zero."
                "**Conclude.** $r_1 + r_2$ is an integer over a non-zero integer — the definition "
                "of rational. $\\blacksquare$"
                "**Try it on a case.** $\\frac{3}{4} + \\frac{2}{5} = \\frac{15 + 8}{20} "
                "= \\frac{23}{20}$ — an integer over an integer, as the proof promised ✓"
                "**Why this matters.** This unglamorous fact is the engine of the next proof. "
                "Closure is what makes the contradiction argument work.",
                [
                    "Eq(Rational(3,4) + Rational(2,5), Rational(23,20))",
                    "Eq(3*5 + 4*2, 23)",
                    "Eq(4*5, 20)",
                ],
            ),
            problem(
                "im2-u1-l4-we3",
                "Prove that a rational number plus an irrational number is always irrational.",
                "**Set up the contradiction.** Let $r$ be rational and $x$ irrational. Suppose, "
                "for contradiction, that their sum $s = r + x$ is RATIONAL."
                "**Rearrange.** Solving for $x$:"
                "$$x = s - r.$$"
                "**Apply closure.** Both $s$ and $r$ are rational by assumption, and the rationals "
                "are closed under subtraction (previous result, with a minus). Therefore $s - r$ "
                "is rational."
                "**The contradiction.** That says $x$ is rational. But $x$ was given as "
                "irrational, and no number is both."
                "**Conclude.** The assumption must be false, so $r + x$ is irrational. "
                "$\\blacksquare$"
                "**Test the theorem.** $2 + \\sqrt{3} \\approx 3.732$, and no fraction equals it. "
                "Subtracting the $2$ back recovers $\\sqrt{3} \\approx 1.732$ — the very step the "
                "proof uses."
                "**Why the proof needs closure.** Without it, \"$s - r$ is rational\" would be an "
                "assertion rather than a fact, and the contradiction would collapse. The previous "
                "worked example is doing real work here.",
                [
                    "Abs((2 + sqrt(3)) - Rational(3732, 1000)) < Rational(1,1000)",
                    "Eq(simplify((2 + sqrt(3)) - 2), sqrt(3))",
                    "Abs(sqrt(3) - Rational(1732,1000)) < Rational(1,1000)",
                ],
            ),
            problem(
                "im2-u1-l4-we4",
                "Decide whether each is rational or irrational, with a reason: "
                "(a) $5 + \\sqrt{7}$; (b) $\\sqrt{2} \\cdot \\sqrt{8}$; "
                "(c) $3\\sqrt{5}$; (d) $0 \\cdot \\pi$; (e) $\\sqrt{6} - \\sqrt{6}$.",
                "**Part (a) is IRRATIONAL.** Rational plus irrational, by the theorem "
                "just proved. ($7$ is not a perfect square, so $\\sqrt{7}$ is irrational.)"
                "**Part (b) is RATIONAL.** Multiply the radicands: "
                "$\\sqrt{2} \\cdot \\sqrt{8} = \\sqrt{16} = 4$. Two irrationals whose product is a "
                "whole number — which shows there is no closure theorem for irrationals."
                "**Part (c) is IRRATIONAL.** A non-zero rational times an irrational. If "
                "$3\\sqrt{5}$ were rational, dividing by $3$ would make $\\sqrt{5}$ rational."
                "**Part (d) is RATIONAL**, the exception to (c): $0 \\cdot \\pi = 0$. Zero times "
                "anything is zero, and $0 = \\frac{0}{1}$ is rational. This is exactly why the "
                "theorem says \"non-zero rational\"."
                "**Part (e) is RATIONAL** too: $\\sqrt{6} - \\sqrt{6} = 0$, two irrationals whose "
                "difference is rational. Again: no closure for irrationals."
                "**The pattern worth extracting.** Any statement combining a RATIONAL with an "
                "irrational is decidable in advance. Any statement combining two IRRATIONALS must "
                "be computed — it could go either way.",
                [
                    "Eq(simplify(sqrt(2)*sqrt(8)), 4)",
                    "Eq(0*pi, 0)",
                    "Eq(simplify(sqrt(6) - sqrt(6)), 0)",
                    "Eq(simplify(3*sqrt(5)/3), sqrt(5))",
                    "Ne(sqrt(7), 2)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Calling every square root irrational.",
                "√9 = 3 and √16 = 4 are rational. A square root is irrational only when the "
                "radicand is not a perfect square — check that first.",
            ),
            mistake(
                "Calling 22/7 irrational because it approximates π.",
                "It is a ratio of two integers, so it is rational by definition. Being near an "
                "irrational number is not a property that transfers.",
            ),
            mistake(
                "Assuming two irrationals always combine to something irrational.",
                "√2 · √2 = 2 and √6 − √6 = 0 are both rational. There is no closure theorem for "
                "the irrationals — only for the rationals.",
            ),
            mistake(
                "Forgetting the non-zero condition in 'rational × irrational is irrational'.",
                "0 · π = 0 is rational. The theorem requires the rational factor to be non-zero, "
                "and that exception is not a technicality.",
            ),
        ],
        try_it=[
            problem(
                "im2-u1-l4-t1",
                "Classify: $\\sqrt{49}$, $\\sqrt{50}$, $\\frac{7}{3}$, $0.\\overline{6}$.",
                "$\\sqrt{49} = 7$ — rational (perfect square). $\\sqrt{50} = 5\\sqrt{2}$ — "
                "irrational. $\\frac{7}{3}$ — rational by definition. "
                "$0.\\overline{6} = \\frac{2}{3}$ — rational, since every repeating decimal is.",
                [
                    "Eq(sqrt(49), 7)",
                    "Eq(simplify(sqrt(50)), 5*sqrt(2))",
                    "Eq(Rational(6,9), Rational(2,3))",
                ],
            ),
            problem(
                "im2-u1-l4-t2",
                "Is $\\sqrt{12} \\cdot \\sqrt{3}$ rational or irrational? Show why.",
                "Multiply the radicands: $\\sqrt{36} = 6$ — **rational**. Two irrational factors "
                "produced a whole number, which is possible precisely because there is no closure "
                "theorem for irrationals.",
                [
                    "Eq(simplify(sqrt(12)*sqrt(3)), 6)",
                    "Eq(12*3, 36)",
                ],
            ),
            problem(
                "im2-u1-l4-t3",
                "Explain why $\\dfrac{\\sqrt{5}}{4}$ must be irrational.",
                "Suppose it were rational. Multiplying by the rational number $4$ would give a "
                "rational result (closure under multiplication), and that result is $\\sqrt{5}$ — "
                "which is irrational. Contradiction, so $\\frac{\\sqrt{5}}{4}$ is irrational. This "
                "is the same contradiction structure as the main theorem, with division in place "
                "of subtraction.",
                [
                    "Eq(simplify(4*sqrt(5)/4), sqrt(5))",
                    "Ne(sqrt(5), 2)",
                    "Ne(sqrt(5), 3)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "N-RN.3",
                "title": "Rational means a ratio of integers",
                "body": (
                    "$\\frac{a}{b}$ with $a, b$ integers and $b \\ne 0$. That covers every "
                    "integer, every terminating decimal, and every repeating decimal. Irrational "
                    "means a real number that is NOT such a ratio."
                ),
                "beats": [
                    "$5 = \\frac{5}{1}$ — rational",
                    "$0.25 = \\frac{1}{4}$ — rational",
                    "$0.\\overline{3} = \\frac{1}{3}$ — rational",
                    "$\\sqrt{2}$, $\\pi$ — never a ratio",
                ],
            },
            {
                "kind": "tip",
                "title": "A radical sign does not make a number irrational",
                "body": (
                    "$\\sqrt{9} = 3$ and $\\sqrt{16} = 4$ are rational. A square root is "
                    "irrational only when its radicand is NOT a perfect square. Check for that "
                    "first — it prevents the commonest classification error in this lesson."
                ),
            },
            {"kind": "worked", "title": "Five numbers, classified", "problemId": "im2-u1-l4-we1"},
            tap(
                "Rational or irrational?",
                "Which of these is RATIONAL?",
                [
                    "$\\sqrt{18}$",
                    "$\\sqrt{81}$",
                    "$\\pi - 1$",
                    "$2 + \\sqrt{5}$",
                ],
                1,
                "$\\sqrt{81} = 9$, an integer — rational, because $81$ is a perfect square. "
                "$\\sqrt{18} = 3\\sqrt{2}$ is irrational; $\\pi - 1$ and $2 + \\sqrt{5}$ are "
                "rational-plus-irrational, hence irrational by the theorem this lesson proves.",
                [
                    "Eq(sqrt(81), 9)",
                    "Eq(simplify(sqrt(18)), 3*sqrt(2))",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "Closure",
                "title": "Combine two rationals and you get a rational",
                "body": (
                    "$\\frac{a}{b} + \\frac{c}{d} = \\frac{ad + bc}{bd}$ — an integer over a "
                    "non-zero integer, because the integers are themselves closed under $+$ and "
                    "$\\times$. The same holds for $-$, $\\times$ and $\\div$."
                ),
            },
            {"kind": "worked", "title": "Proving closure under addition", "problemId": "im2-u1-l4-we2"},
            {
                "kind": "teach",
                "eyebrow": "The theorem",
                "title": "Rational plus irrational is always irrational",
                "body": (
                    "Suppose $r + x$ were rational, with $r$ rational and $x$ irrational. Then "
                    "$x = (r + x) - r$ is a difference of two rationals — rational by closure. "
                    "But $x$ is irrational. Contradiction."
                ),
                "beats": [
                    "Assume the opposite: $r + x$ is rational",
                    "Rearrange: $x = (r + x) - r$",
                    "Closure: that difference is **rational**",
                    "But $x$ is irrational — contradiction",
                ],
            },
            {"kind": "worked", "title": "The proof in full", "problemId": "im2-u1-l4-we3"},
            {
                "kind": "conjectureTest",
                "eyebrow": "Test the claim",
                "title": "Is a sum of two irrationals always irrational?",
                "teach": (
                    "The rational-plus-irrational theorem is airtight. But try the same claim for "
                    "two irrationals: $\\sqrt{2} + \\sqrt{2}$ is irrational, while "
                    "$\\sqrt{2} + (-\\sqrt{2}) = 0$ is not. One counterexample is enough to kill a "
                    "conjecture."
                ),
                "config": {
                    "conjecture": "The sum of two irrational numbers is always irrational",
                    "items": [
                        {
                            "label": "√2 + √2",
                            "holds": True,
                            "note": "Equals 2√2, still irrational — the conjecture survives.",
                        },
                        {
                            "label": "√3 + √5",
                            "holds": True,
                            "note": "No cancellation is possible; the sum is irrational.",
                        },
                        {
                            "label": "√2 + (−√2)",
                            "holds": False,
                            "note": "Equals 0, which is rational. One counterexample is fatal.",
                        },
                        {
                            "label": "(1 + √2) + (1 − √2)",
                            "holds": False,
                            "note": "Equals 2 — the irrational parts destroy each other.",
                        },
                    ],
                },
            },
            tap(
                "Which combination is decidable in advance?",
                "Without computing, which of these can you be certain is irrational?",
                [
                    "The sum of two irrationals",
                    "The product of two irrationals",
                    "A non-zero rational plus an irrational",
                    "The quotient of two irrationals",
                ],
                2,
                "Only statements combining a RATIONAL with an irrational are decidable in advance "
                "— that is what the theorem gives you. Two irrationals can go either way: "
                "$\\sqrt{2} + (-\\sqrt{2}) = 0$ and $\\sqrt{2} \\cdot \\sqrt{2} = 2$ are both "
                "rational, while $\\sqrt{2} + \\sqrt{3}$ is not.",
                [
                    "Eq(simplify(sqrt(2) + (-sqrt(2))), 0)",
                    "Eq(simplify(sqrt(2)*sqrt(2)), 2)",
                    "Eq(simplify(sqrt(8)/sqrt(2)), 2)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "The exception",
                "title": "Zero is the one escape",
                "body": (
                    "A NON-ZERO rational times an irrational is irrational. But "
                    "$0 \\times \\pi = 0$ is rational — which is why the theorem carries that "
                    "condition. It is not a technicality; it is the single case where the "
                    "argument genuinely fails."
                ),
            },
            {"kind": "worked", "title": "Five classifications, with reasons", "problemId": "im2-u1-l4-we4"},
            {"kind": "tryIt", "title": "Your turn — classify four", "problemId": "im2-u1-l4-t1"},
            {"kind": "tryIt", "title": "Your turn — argue by contradiction", "problemId": "im2-u1-l4-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "Rational = a ratio of integers: includes repeating and terminating decimals",
                    "A radical is irrational only when its radicand is not a perfect power",
                    "The rationals are **closed** under $+$, $-$, $\\times$, $\\div$ (non-zero)",
                    "Rational + irrational is always irrational — proved by contradiction from closure",
                    "Two irrationals can combine either way; only a zero rational escapes the product rule",
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
            "im2-u1-pr-1",
            "Evaluate $49^{1/2}$, $64^{2/3}$ and $81^{1/4}$.",
            "$49^{1/2} = 7$. $64^{2/3} = \\left(\\sqrt[3]{64}\\right)^{2} = 4^{2} = 16$. "
            "$81^{1/4} = 3$.",
            [
                "Eq(49**Rational(1,2), 7)",
                "Eq(64**Rational(2,3), 16)",
                "Eq(81**Rational(1,4), 3)",
            ],
        ),
        problem(
            "im2-u1-pr-2",
            "Evaluate $125^{-2/3}$.",
            "The minus gives a reciprocal: $\\frac{1}{125^{2/3}} = "
            "\\frac{1}{\\left(\\sqrt[3]{125}\\right)^{2}} = \\frac{1}{25}$. Positive, as a "
            "negative exponent always is.",
            [
                "Eq(125**Rational(-2,3), Rational(1,25))",
                "Eq(125**Rational(1,3), 5)",
            ],
        ),
        problem(
            "im2-u1-pr-3",
            "Write $\\sqrt[3]{x^{2}}$ with a rational exponent, and $y^{5/2}$ in radical form.",
            "$\\sqrt[3]{x^{2}} = x^{2/3}$ — the index is the denominator. "
            "$y^{5/2} = \\left(\\sqrt{y}\\right)^{5} = \\sqrt{y^{5}}$. Check at $y = 4$: "
            "$4^{5/2} = 2^{5} = 32$ ✓",
            [
                "Eq(4**Rational(5,2), 32)",
                "Eq(2**5, 32)",
                "Eq(8**Rational(2,3), 4)",
            ],
        ),
        problem(
            "im2-u1-pr-4",
            "Simplify $\\sqrt{108}$.",
            "The largest perfect square dividing $108$ is $36$: "
            "$\\sqrt{108} = \\sqrt{36 \\cdot 3} = 6\\sqrt{3}$. Check: $36 \\times 3 = 108$ ✓",
            [
                "Eq((6*sqrt(3))**2, 108)",
                "Eq(simplify(sqrt(108)), 6*sqrt(3))",
            ],
        ),
        problem(
            "im2-u1-pr-5",
            "Simplify $\\sqrt[3]{128}$.",
            "Look for a perfect cube: $128 = 64 \\cdot 2$ and $64 = 4^{3}$, so "
            "$\\sqrt[3]{128} = 4\\sqrt[3]{2}$. Check: $4^{3} \\times 2 = 128$ ✓",
            [
                "Eq((4*2**Rational(1,3))**3, 128)",
                "Eq(128, 64*2),".rstrip(","),
            ],
        ),
        problem(
            "im2-u1-pr-6",
            "Simplify $\\sqrt{50x^{4}y^{3}}$, assuming $x, y \\ge 0$.",
            "$50 = 25 \\cdot 2$ gives a $5$; $x^{4}$ halves to $x^{2}$; $y^{3} = y^{2} \\cdot y$ "
            "gives a $y$ with one inside. So $\\sqrt{50x^{4}y^{3}} = 5x^{2}y\\sqrt{2y}$. Check at "
            "$x = 1$, $y = 2$: inside is $50 \\times 8 = 400$, root $20$; the form gives "
            "$5 \\times 2 \\times \\sqrt{4} = 20$ ✓",
            [
                "Eq(50*1**4*2**3, 400)",
                "Eq(sqrt(400), 20)",
                "Eq(5*1*2*sqrt(2*2), 20)",
            ],
        ),
        problem(
            "im2-u1-pr-7",
            "Simplify $\\sqrt{32} + \\sqrt{72} - \\sqrt{8}$.",
            "Each simplifies to a multiple of $\\sqrt{2}$: $4\\sqrt{2} + 6\\sqrt{2} - 2\\sqrt{2} "
            "= 8\\sqrt{2}$. Check numerically: $5.657 + 8.485 - 2.828 = 11.314 \\approx "
            "8\\sqrt{2}$ ✓",
            [
                "Eq(simplify(sqrt(32)), 4*sqrt(2))",
                "Eq(simplify(sqrt(72)), 6*sqrt(2))",
                "Eq(simplify(sqrt(32) + sqrt(72) - sqrt(8)), 8*sqrt(2))",
            ],
        ),
        problem(
            "im2-u1-pr-8",
            "Multiply and simplify $3\\sqrt{5} \\cdot 4\\sqrt{15}$.",
            "Coefficients and radicands multiply: $12\\sqrt{75}$. Then "
            "$\\sqrt{75} = 5\\sqrt{3}$, so the answer is $60\\sqrt{3}$.",
            [
                "Eq(simplify(3*sqrt(5)*4*sqrt(15)), 60*sqrt(3))",
                "Eq(simplify(sqrt(75)), 5*sqrt(3))",
            ],
        ),
        problem(
            "im2-u1-pr-9",
            "Expand $\\left(\\sqrt{7} - 3\\right)\\left(\\sqrt{7} + 3\\right)$.",
            "This is a difference of squares: $(\\sqrt{7})^{2} - 3^{2} = 7 - 9 = -2$. The cross "
            "terms cancel, which is exactly the conjugate mechanism.",
            [
                "Eq(simplify((sqrt(7) - 3)*(sqrt(7) + 3)), -2)",
                "Eq(7 - 9, -2)",
            ],
        ),
        problem(
            "im2-u1-pr-10",
            "Rationalise $\\dfrac{8}{\\sqrt{2}}$.",
            "Multiply top and bottom by $\\sqrt{2}$: $\\frac{8\\sqrt{2}}{2} = 4\\sqrt{2}$.",
            [
                "Eq(simplify(8/sqrt(2)), 4*sqrt(2))",
                "Eq(simplify((4*sqrt(2))*sqrt(2)), 8)",
            ],
        ),
        problem(
            "im2-u1-pr-11",
            "Rationalise $\\dfrac{6}{\\sqrt{5} - 1}$.",
            "Multiply by the conjugate $\\sqrt{5} + 1$. The denominator becomes $5 - 1 = 4$, so "
            "the result is $\\frac{6(\\sqrt{5} + 1)}{4} = \\frac{3(\\sqrt{5} + 1)}{2}$.",
            [
                "Eq(simplify((sqrt(5) - 1)*(sqrt(5) + 1)), 4)",
                "Eq(simplify(6/(sqrt(5) - 1)), simplify(3*(sqrt(5) + 1)/2))",
            ],
        ),
        problem(
            "im2-u1-pr-12",
            "Classify as rational or irrational, with a reason: $\\sqrt{144}$, "
            "$4 - \\sqrt{2}$, $\\sqrt{3} \\cdot \\sqrt{27}$.",
            "$\\sqrt{144} = 12$ — **rational**, a perfect square. $4 - \\sqrt{2}$ — "
            "**irrational**, a rational combined with an irrational. "
            "$\\sqrt{3} \\cdot \\sqrt{27} = \\sqrt{81} = 9$ — **rational**, two irrationals whose "
            "product happens to be a perfect square.",
            [
                "Eq(sqrt(144), 12)",
                "Eq(simplify(sqrt(3)*sqrt(27)), 9)",
                "Eq(simplify((4 - sqrt(2)) + sqrt(2)), 4)",
            ],
        ),
    ]


def test_bank():
    return [
        problem(
            "im2-u1-ty-1",
            "Explain why $x^{1/3}$ must equal $\\sqrt[3]{x}$ if the exponent rules are to hold, "
            "then evaluate $27^{4/3}$ and $27^{-4/3}$.",
            "**The forcing argument.** Assume $(x^{a})^{b} = x^{ab}$ still holds when the exponent "
            "is a fraction. Then"
            "$$\\left(x^{1/3}\\right)^{3} = x^{\\frac{1}{3} \\times 3} = x^{1} = x.$$"
            "So $x^{1/3}$ is a number whose cube is $x$ — which is precisely what "
            "$\\sqrt[3]{x}$ means. The value was forced by the requirement, not assigned by "
            "definition."
            "**The positive exponent.** Root first:"
            "$$27^{4/3} = \\left(\\sqrt[3]{27}\\right)^{4} = 3^{4} = 81.$$"
            "**The negative exponent.** The minus takes a reciprocal:"
            "$$27^{-4/3} = \\frac{1}{81}.$$"
            "**Check the pair.** Their product is $81 \\times \\frac{1}{81} = 1$, which is what "
            "$x^{n} \\cdot x^{-n} = x^{0} = 1$ demands ✓ — the rules really are intact.",
            [
                "Eq(Rational(1,3)*3, 1)",
                "Eq(27**Rational(4,3), 81)",
                "Eq(27**Rational(-4,3), Rational(1,81))",
                "Eq(27**Rational(4,3) * 27**Rational(-4,3), 1)",
            ],
        ),
        problem(
            "im2-u1-ty-2",
            "Simplify completely: $\\sqrt{162}$, $\\sqrt[3]{250}$, and $\\sqrt{98a^{5}b^{2}}$ "
            "with $a, b \\ge 0$.",
            "**The first.** The largest perfect square factor of $162$ is $81$:"
            "$$\\sqrt{162} = \\sqrt{81 \\cdot 2} = 9\\sqrt{2}.$$"
            "Check: $81 \\times 2 = 162$ ✓"
            "**The second.** For a cube root, find a perfect cube factor. "
            "$250 = 125 \\cdot 2$ and $125 = 5^{3}$:"
            "$$\\sqrt[3]{250} = 5\\sqrt[3]{2}.$$"
            "Check: $5^{3} \\times 2 = 250$ ✓"
            "**The third.** Take the parts separately. $98 = 49 \\cdot 2$ gives a "
            "$7$; $a^{5} = a^{4} \\cdot a$ gives $a^{2}$ with one $a$ inside; $b^{2}$ gives $b$:"
            "$$\\sqrt{98a^{5}b^{2}} = 7a^{2}b\\sqrt{2a}.$$"
            "Check at $a = 2$, $b = 1$: inside is $98 \\times 32 = 3136$, whose root is $56$; the "
            "form gives $7 \\times 4 \\times 1 \\times \\sqrt{4} = 28 \\times 2 = 56$ ✓",
            [
                "Eq((9*sqrt(2))**2, 162)",
                "Eq((5*2**Rational(1,3))**3, 250)",
                "Eq(98*2**5*1**2, 3136)",
                "Eq(sqrt(3136), 56)",
                "Eq(7*2**2*1*sqrt(2*2), 56)",
            ],
        ),
        problem(
            "im2-u1-ty-3",
            "Simplify $\\sqrt{45} + \\sqrt{80} - \\sqrt{20}$, and explain why the terms could be "
            "combined at all.",
            "**Simplify each term.** All three radicands contain a factor of $5$:"
            "$$\\sqrt{45} = \\sqrt{9 \\cdot 5} = 3\\sqrt{5},$$"
            "$$\\sqrt{80} = \\sqrt{16 \\cdot 5} = 4\\sqrt{5},$$"
            "$$\\sqrt{20} = \\sqrt{4 \\cdot 5} = 2\\sqrt{5}.$$"
            "**Combine.** Now every term is a multiple of $\\sqrt{5}$ — they are like terms:"
            "$$3\\sqrt{5} + 4\\sqrt{5} - 2\\sqrt{5} = 5\\sqrt{5}.$$"
            "**Why they combined.** Radicals add like variables do: $3\\sqrt{5}$ and $4\\sqrt{5}$ "
            "are counting copies of the same object, exactly as $3x$ and $4x$ do. Before "
            "simplifying, the three radicands ($45$, $80$, $20$) were all different and the terms "
            "looked unrelated. Simplification exposed the shared $\\sqrt{5}$."
            "**Check numerically.** $5\\sqrt{5} \\approx 11.18$, and "
            "$6.708 + 8.944 - 4.472 = 11.18$ ✓",
            [
                "Eq(simplify(sqrt(45)), 3*sqrt(5))",
                "Eq(simplify(sqrt(80)), 4*sqrt(5))",
                "Eq(simplify(sqrt(20)), 2*sqrt(5))",
                "Eq(simplify(sqrt(45) + sqrt(80) - sqrt(20)), 5*sqrt(5))",
            ],
        ),
        problem(
            "im2-u1-ty-4",
            "Rationalise $\\dfrac{12}{\\sqrt{6} + 2}$ and verify the result numerically.",
            "**Multiply by the conjugate** $\\sqrt{6} - 2$, top and bottom:"
            "$$\\frac{12}{\\sqrt{6} + 2} \\cdot \\frac{\\sqrt{6} - 2}{\\sqrt{6} - 2} "
            "= \\frac{12(\\sqrt{6} - 2)}{(\\sqrt{6})^{2} - 2^{2}}.$$"
            "**The denominator clears.**"
            "$$6 - 4 = 2,$$"
            "so"
            "$$\\frac{12(\\sqrt{6} - 2)}{2} = 6(\\sqrt{6} - 2) = 6\\sqrt{6} - 12.$$"
            "**Verify numerically.** $\\sqrt{6} \\approx 2.4495$. The original is "
            "$\\frac{12}{4.4495} \\approx 2.6970$. The answer is "
            "$6(2.4495) - 12 = 14.697 - 12 = 2.697$ ✓"
            "**Why the conjugate and not the same sign.** Multiplying by $\\sqrt{6} + 2$ instead "
            "would give $(\\sqrt{6}+2)^{2} = 10 + 4\\sqrt{6}$ — still irrational, so nothing would "
            "have been achieved. The sign flip is what makes the cross terms cancel.",
            [
                "Eq(simplify((sqrt(6) + 2)*(sqrt(6) - 2)), 2)",
                "Eq(simplify(12/(sqrt(6) + 2)), simplify(6*sqrt(6) - 12)),".rstrip(","),
                "Eq(simplify((sqrt(6) + 2)**2), 10 + 4*sqrt(6))",
                "Abs((6*sqrt(6) - 12) - Rational(2697, 1000)) < Rational(1,1000)",
            ],
        ),
        problem(
            "im2-u1-ty-5",
            "Prove that the product of a non-zero rational number and an irrational number is "
            "irrational, then explain why the non-zero condition is needed.",
            "**Set up the contradiction.** Let $r$ be a non-zero rational and $x$ irrational. "
            "Suppose, for contradiction, that the product $p = rx$ is RATIONAL."
            "**Rearrange.** Since $r \\neq 0$ we may divide by it:"
            "$$x = \\frac{p}{r}.$$"
            "**Apply closure.** Both $p$ and $r$ are rational, and the rationals are closed under "
            "division by a non-zero rational. So $\\frac{p}{r}$ is rational."
            "**The contradiction.** That makes $x$ rational, but $x$ was given as irrational. "
            "No number is both, so the assumption fails and $rx$ is irrational. $\\blacksquare$"
            "**Why non-zero is required.** The proof divides by $r$, and that step is illegal "
            "when $r = 0$. And the theorem genuinely fails there: "
            "$0 \\times \\sqrt{2} = 0$, which is rational. So the condition is not a technical "
            "nicety — it names the one case where the conclusion is false."
            "**Test the theorem.** $3\\sqrt{2} \\approx 4.243$ is irrational; dividing by $3$ "
            "recovers $\\sqrt{2}$, the very step the proof uses.",
            [
                "Eq(simplify(3*sqrt(2)/3), sqrt(2))",
                "Eq(0*sqrt(2), 0)",
                "Abs(3*sqrt(2) - Rational(4243,1000)) < Rational(1,1000)",
            ],
        ),
        problem(
            "im2-u1-ty-6",
            "Classify each with a reason: (a) $\\sqrt{2} + \\sqrt{18}$; "
            "(b) $\\left(1 + \\sqrt{3}\\right)\\left(1 - \\sqrt{3}\\right)$; "
            "(c) $\\dfrac{\\sqrt{7}}{2}$; (d) $\\sqrt{5} \\cdot \\sqrt{20}$.",
            "**(a) IRRATIONAL.** Simplify: $\\sqrt{18} = 3\\sqrt{2}$, so the sum is "
            "$\\sqrt{2} + 3\\sqrt{2} = 4\\sqrt{2}$ — a non-zero rational times an irrational."
            "**(b) RATIONAL.** A difference of squares: $1 - 3 = -2$. Two irrational factors "
            "producing an integer, which is possible because there is no closure theorem for "
            "irrationals."
            "**(c) IRRATIONAL.** If $\\frac{\\sqrt{7}}{2}$ were rational, multiplying by the "
            "rational number $2$ would give a rational result — but that result is $\\sqrt{7}$, "
            "which is irrational. Contradiction."
            "**(d) RATIONAL.** Multiply the radicands: $\\sqrt{100} = 10$."
            "**The pattern.** In (a) and (c) a rational was combined with an irrational, so the "
            "answer was decidable in advance. In (b) and (d) two irrationals were combined, so "
            "the answer had to be computed — and both happened to come out rational.",
            [
                "Eq(simplify(sqrt(2) + sqrt(18)), 4*sqrt(2))",
                "Eq(simplify((1 + sqrt(3))*(1 - sqrt(3))), -2)",
                "Eq(simplify(sqrt(5)*sqrt(20)), 10)",
                "Eq(simplify(2*(sqrt(7)/2)), sqrt(7))",
            ],
        ),
        problem(
            "im2-u1-ty-7",
            "A square has area $200$ cm². Find its exact side length in simplest radical form, "
            "its perimeter, and the exact length of its diagonal.",
            "**Side length.** The side $s$ satisfies $s^{2} = 200$, so"
            "$$s = \\sqrt{200} = \\sqrt{100 \\cdot 2} = 10\\sqrt{2}\\ \\text{cm}.$$"
            "**Perimeter.** Four equal sides:"
            "$$P = 4 \\times 10\\sqrt{2} = 40\\sqrt{2}\\ \\text{cm} \\approx 56.6\\ \\text{cm}.$$"
            "**Diagonal.** By Pythagoras on half the square:"
            "$$d = \\sqrt{s^{2} + s^{2}} = \\sqrt{2s^{2}} = s\\sqrt{2} = 10\\sqrt{2} \\cdot "
            "\\sqrt{2} = 10 \\times 2 = 20\\ \\text{cm}.$$"
            "**Notice the diagonal is rational.** Two irrational quantities multiplied to give a "
            "whole number — $\\sqrt{2} \\cdot \\sqrt{2} = 2$. The side is irrational and the "
            "diagonal is not, in the same square."
            "**Check.** $d^{2}$ should be twice the area: $20^{2} = 400 = 2 \\times 200$ ✓ And "
            "$s^{2} = (10\\sqrt{2})^{2} = 100 \\times 2 = 200$ ✓, matching the given area.",
            [
                "Eq((10*sqrt(2))**2, 200)",
                "Eq(simplify(4*10*sqrt(2)), 40*sqrt(2))",
                "Eq(simplify(10*sqrt(2)*sqrt(2)), 20)",
                "Eq(20**2, 2*200)",
                "Abs(40*sqrt(2) - Rational(566, 10)) < Rational(1,10)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="rational-exponents-and-radicals",
        title="Rational Exponents & Radicals",
        unit_number=1,
        blurb=(
            "Why a fractional exponent is forced to mean a root, simplifying radicals by "
            "extracting perfect powers, adding and multiplying radical expressions, rationalising "
            "denominators with conjugates, and proving that a rational plus an irrational is "
            "always irrational."
        ),
        builds_on=(
            "Exponential functions from IM1 Unit 6 — the same exponent rules, now with the "
            "exponent allowed to be a fraction."
        ),
        lessons=[
            lesson_rational_exponents(),
            lesson_simplifying(),
            lesson_operations(),
            lesson_rational_irrational(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
