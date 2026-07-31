#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 3: Exponential & Logarithmic Functions.

CCSS Integrated Math III: F-LE.4 (for exponential models, express as a
logarithm the solution to ab^ct = d and evaluate it), F-BF.5 (understand the
inverse relationship between exponents and logarithms), F-IF.7e (graph
exponential and logarithmic functions, showing intercepts and end behaviour),
A-SSE.3c (use properties of exponents to transform exponential expressions).

The unit's through-line: A LOGARITHM IS AN EXPONENT. Not a new operation with
its own mysterious rules — the same exponent the student has used since IM1,
asked about in reverse. Every law of logarithms is an exponent law read
backwards, every equation-solving move is "bring the exponent down where we
can reach it", and the modelling lesson closes the loop the pathway opened in
IM1 Unit 6: exponential models could be BUILT there, but only now can they be
SOLVED for time. The domain discipline of Unit 2 carries straight in — a log
equation can manufacture extraneous candidates exactly the way a radical
equation does, and for the same reason.

Run: python3 scripts/im/build_im3_unit3.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — F-BF.5: the logarithm as an inverse
# ===========================================================================

def lesson_inverse():
    return lesson(
        slug="the-logarithm-as-an-inverse",
        title="The Logarithm as an Inverse",
        concrete=(
            "Start with $1$ and keep doubling: $2, 4, 8, \\dots$ How many doublings reach "
            "$1024$? Count them: ten. That count IS a logarithm — $\\log_2 1024 = 10$. The "
            "question \"$2$ to what power gives $1024$?\" is one the student can already "
            "answer; the logarithm is just its name."
        ),
        objective=(
            "Convert between exponential and logarithmic form, evaluate logarithms exactly, "
            "and state the domain of a logarithmic function."
        ),
        concept=[
            "The equation $2^y = 32$ asks for an output; the equation $2^5 = x$ asks for one "
            "too. But \"$2$ to WHAT power gives $32$?\" asks for the exponent itself, and "
            "that question gets its own notation: $y = \\log_2 32$. The two forms say the "
            "same thing — $b^y = x$ exactly when $y = \\log_b x$ — and converting between "
            "them is the single skill this whole unit stands on.",

            "Because a logarithm IS an exponent, evaluating one means asking the exponential "
            "question. $\\log_3 81$: three to what power is $81$? Four. "
            "$\\log_5 \\frac{1}{25}$: five to what power is $\\frac{1}{25}$? The power "
            "$-2$, because negative exponents make reciprocals. No new arithmetic is "
            "happening — only IM2's exponent facts, read in reverse.",

            "The base carries two standing restrictions: $b > 0$ and $b \\ne 1$ (powers of "
            "$1$ are all $1$, so the question \"$1$ to what power…\" has no useful answer). "
            "And the INPUT must be positive: a positive base raised to any real power is "
            "positive, so $\\log_b 0$ and $\\log_b(-8)$ ask for an exponent that does not "
            "exist. The domain of every logarithmic function is $x > 0$, shifted by whatever "
            "sits inside.",

            "Graphically, $y = \\log_b x$ is $y = b^x$ reflected across the line $y = x$ — "
            "the inverse function's graph. The exponential's horizontal asymptote $y = 0$ "
            "becomes the logarithm's VERTICAL asymptote $x = 0$; the exponential's intercept "
            "$(0, 1)$ becomes $(1, 0)$. Where the exponential races upward, the logarithm "
            "crawls — it grows without bound, but slower than any polynomial cares to.",
        ],
        key_idea=(
            "$\\log_b x$ is the exponent you put on $b$ to get $x$. Every evaluation, every "
            "law, every equation in this unit is that one sentence applied again."
        ),
        facts=[
            fact("Definition", "b^y = x \\iff y = \\log_b x",
                 "One statement, two costumes. Converting between them is the core skill."),
            fact("Log of 1", "\\log_b 1 = 0",
                 "Any base to the power 0 is 1."),
            fact("Log of the base", "\\log_b b = 1",
                 "The exponent that turns b into b is 1."),
            fact("Inverse pair", "\\log_b b^k = k",
                 "Asking 'b to what power gives b^k' answers itself."),
            fact("Domain", "x > 0",
                 "A positive base to any real power is positive, so only positive inputs "
                 "have logarithms."),
        ],
        worked=[
            problem(
                "im3-u3-l1-we1",
                "Evaluate exactly: (a) $\\log_3 81$, (b) $\\log_5 \\dfrac{1}{25}$, "
                "(c) $\\log_{10} 1000$.",
                "**(a) Ask the exponential question.** Three to what power is $81$? "
                "$3^4 = 81$, so $\\log_3 81 = 4$."
                "**(b) Reciprocals mean negative exponents.** $5^2 = 25$, so "
                "$5^{-2} = \\frac{1}{25}$ and $\\log_5 \\frac{1}{25} = -2$."
                "**(c) Count the zeros.** $10^3 = 1000$, so $\\log_{10} 1000 = 3$. Base-$10$ "
                "logarithms count orders of magnitude — which is why they run the decibel "
                "and Richter scales.",
                [
                    "Eq(3**4, 81)",
                    "Eq(simplify(log(81, 3)), 4)",
                    "Eq(5**(-2), Rational(1, 25))",
                    "Eq(simplify(log(Rational(1, 25), 5)), -2)",
                    "Eq(10**3, 1000)",
                ],
            ),
            problem(
                "im3-u3-l1-we2",
                "Solve for the unknown: (a) $\\log_2 x = 5$, (b) $\\log_x 49 = 2$.",
                "**(a) Convert to exponential form.** $\\log_2 x = 5$ says $x = 2^5 = 32$."
                "**(b) Convert again — the unknown is the base.** $\\log_x 49 = 2$ says "
                "$x^2 = 49$, so $x = 7$ or $x = -7$."
                "**Apply the base restrictions.** A base must be positive and not $1$, so "
                "$x = -7$ is rejected and $x = 7$ is the only solution. The restriction is "
                "part of the definition, not an afterthought — the same discipline as the "
                "domain checks of Unit 2.",
                [
                    "Eq(2**5, 32)",
                    "Eq(7**2, 49)",
                    "Eq((-7)**2, 49)",
                    "Ne(-7, 7)",
                ],
            ),
            problem(
                "im3-u3-l1-we3",
                "State the domain of $f(x) = \\log_2(x - 3)$ and the equation of its "
                "vertical asymptote.",
                "**Only positive inputs have logarithms.** The expression being logged is "
                "$x - 3$, so require $x - 3 > 0$, i.e. $x > 3$."
                "**The asymptote sits at the boundary.** As $x - 3$ shrinks toward $0^+$, "
                "the exponent needed plunges to $-\\infty$, so the graph dives along the "
                "line $x = 3$."
                "**Sanity-check a point.** At $x = 11$: $f(11) = \\log_2 8 = 3$ — the graph "
                "is well up and to the right of its asymptote, growing slowly.",
                [
                    "Eq(11 - 3, 8)",
                    "Eq(simplify(log(8, 2)), 3)",
                    "11 > 3",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading log_2 8 as '2 to the power 8'.",
                "It is the exponent, not the power: 2 to WHAT power gives 8? The answer is "
                "3, not 256. When in doubt, write the exponential form b^y = x first.",
            ),
            mistake(
                "Taking the logarithm of a negative number or of zero.",
                "A positive base to any real power is positive, so log_b 0 and log_b(-8) do "
                "not exist. Inputs must be strictly positive.",
            ),
            mistake(
                "Treating log_b x as the fraction b/x or x/b.",
                "The notation is a question about exponents, not a division. log_2 32 = 5 "
                "and neither 2/32 nor 32/2 is 5.",
            ),
            mistake(
                "Expecting logarithmic growth to be fast.",
                "The logarithm is the exponential run backwards: since 2^x explodes, log_2 x "
                "crawls. Doubling the input adds only 1 to the output — log_2 1024 = 10 but "
                "log_2 2048 = 11.",
            ),
        ],
        try_it=[
            problem(
                "im3-u3-l1-t1",
                "Evaluate $\\log_4 64$.",
                "Four to what power gives $64$? $4^3 = 64$, so $\\log_4 64 = 3$.",
                ["Eq(4**3, 64)", "Eq(simplify(log(64, 4)), 3)"],
            ),
            problem(
                "im3-u3-l1-t2",
                "Solve $\\log_3 x = 4$.",
                "Convert to exponential form: $x = 3^4 = 81$.",
                ["Eq(3**4, 81)"],
            ),
            problem(
                "im3-u3-l1-t3",
                "State the domain of $g(x) = \\log_{10}(5 - x)$.",
                "Require $5 - x > 0$, so $x < 5$. The vertical asymptote is $x = 5$ and the "
                "graph opens to the LEFT — the inside expression decides the direction.",
                ["Eq(5 - 5, 0)", "5 - 4 > 0"],
            ),
        ],
        steps=[
            tap(
                "The exponent question",
                "What is $\\log_2 32$?",
                ["$5$", "$16$", "$64$", "$\\frac{1}{5}$"],
                0,
                "Two to what power gives $32$? $2^5 = 32$, so the logarithm — the exponent "
                "— is $5$.",
                ["Eq(2**5, 32)"],
            ),
            tap(
                "Two costumes",
                "Which equation says the same thing as $\\log_6 x = 2$?",
                ["$x = 6^2$", "$x = 2^6$", "$6 = x^2$", "$x = \\frac{6}{2}$"],
                0,
                "$\\log_6 x = 2$ means '$6$ to the power $2$ gives $x$': $x = 36$. Converting "
                "to exponential form is always the first move.",
                ["Eq(6**2, 36)"],
            ),
            tap(
                "Where logs live",
                "What is the domain of $y = \\log_2(x + 4)$?",
                ["$x > -4$", "$x > 0$", "$x > 4$", "all real numbers"],
                0,
                "The INPUT to the log must be positive: $x + 4 > 0$, so $x > -4$. The "
                "asymptote moved with the inside expression.",
                ["Eq(-4 + 4, 0)", "-3 + 4 > 0"],
            ),
        ],
    )


# ===========================================================================
# Lesson 2 — the laws of logarithms
# ===========================================================================

def lesson_laws():
    return lesson(
        slug="the-laws-of-logarithms",
        title="The Laws of Logarithms",
        concrete=(
            "Multiply $32 \\times 8$ the lazy way: $2^5 \\cdot 2^3 = 2^8$. The exponents "
            "ADDED while the numbers multiplied. Logarithms are exponents — so the log of a "
            "product is the sum of the logs. Before calculators, entire books of logarithms "
            "were printed so that every multiplication in navigation and astronomy could be "
            "done as an addition."
        ),
        objective=(
            "Expand and condense logarithmic expressions with the product, quotient and "
            "power laws, and evaluate any logarithm with the change-of-base formula."
        ),
        concept=[
            "Each law of logarithms is an exponent law wearing the inverse costume. "
            "$b^m \\cdot b^n = b^{m+n}$ says 'multiply the numbers, add the exponents' — "
            "and since logs ARE the exponents, $\\log_b(xy) = \\log_b x + \\log_b y$. The "
            "quotient law comes from $b^m / b^n = b^{m-n}$ the same way.",

            "The power law is the workhorse: $\\log_b(x^n) = n \\log_b x$, because raising "
            "to the $n$th power multiplies the needed exponent by $n$. It is the law that "
            "will drag an unknown OUT of an exponent in the next lesson — the whole reason "
            "this unit can solve equations IM1 could only set up.",

            "The laws run in both directions. EXPANDING breaks a complicated log into a sum "
            "of simple ones; CONDENSING packs a sum into a single log, which is the "
            "direction equation-solving needs. Both are the same three laws, chosen by "
            "which side of the page you are walking toward.",

            "The change-of-base formula, $\\log_b x = \\frac{\\log x}{\\log b}$, follows in "
            "one line: if $y = \\log_b x$ then $b^y = x$; take the log of both sides in ANY "
            "base and the power law gives $y \\log b = \\log x$. One consequence worth "
            "internalising: no logarithm is exotic, since every one of them is a ratio of "
            "logs in whatever base a calculator offers.",
        ],
        key_idea=(
            "Products become sums, quotients become differences, powers become "
            "multipliers — because logs are exponents and that is how exponents already "
            "behave. There is no law for $\\log(x + y)$, and pretending there is one is "
            "the unit's most tempting error."
        ),
        facts=[
            fact("Product law", "\\log_b(xy) = \\log_b x + \\log_b y",
                 "From b^m · b^n = b^(m+n): multiply numbers, add exponents."),
            fact("Quotient law", "\\log_b\\tfrac{x}{y} = \\log_b x - \\log_b y",
                 "From b^m / b^n = b^(m-n)."),
            fact("Power law", "\\log_b(x^n) = n\\log_b x",
                 "The exponent-mover: it will pull unknowns down out of the exponent."),
            fact("Change of base", "\\log_b x = \\frac{\\log x}{\\log b}",
                 "Any base becomes a ratio of logs in a base you can compute."),
            fact("No sum law", "\\log_b(x + y) \\ne \\log_b x + \\log_b y",
                 "The laws convert BETWEEN operations; they never distribute over addition."),
        ],
        worked=[
            problem(
                "im3-u3-l2-we1",
                "Expand fully: $\\log_2 \\dfrac{8x^3}{y}$.",
                "**Quotient first.** $\\log_2 \\frac{8x^3}{y} = \\log_2(8x^3) - \\log_2 y$."
                "**Product next.** $\\log_2(8x^3) = \\log_2 8 + \\log_2 x^3$."
                "**Power law and known values.** $\\log_2 8 = 3$ and "
                "$\\log_2 x^3 = 3\\log_2 x$. Altogether: "
                "$$\\log_2 \\frac{8x^3}{y} = 3 + 3\\log_2 x - \\log_2 y.$$"
                "Each move traded one operation for a simpler one: quotient for difference, "
                "product for sum, power for multiplier.",
                [
                    "Eq(simplify(log(8, 2)), 3)",
                    "Eq(simplify(log(32, 2)), 5)",
                    "Eq(simplify(3 + 3*simplify(log(4, 2)) - simplify(log(8, 2))), 6)",
                ],
            ),
            problem(
                "im3-u3-l2-we2",
                "Condense and evaluate: $2\\log_{10} 5 + \\log_{10} 4$.",
                "**Power law in reverse.** $2\\log_{10} 5 = \\log_{10} 5^2 = \\log_{10} 25$."
                "**Product law in reverse.** $\\log_{10} 25 + \\log_{10} 4 = "
                "\\log_{10}(25 \\cdot 4) = \\log_{10} 100$."
                "**Evaluate.** $10^2 = 100$, so the whole expression equals $2$. Condensing "
                "turned an unpromising sum into a log of a round number — the standard "
                "payoff of packing logs together.",
                [
                    "Eq(5**2, 25)",
                    "Eq(25*4, 100)",
                    "Eq(simplify(log(100, 10)), 2)",
                    "Eq(simplify(2*log(5, 10) + log(4, 10)), 2)",
                ],
            ),
            problem(
                "im3-u3-l2-we3",
                "Evaluate $\\log_4 8$ exactly, using the change-of-base formula with "
                "base $2$.",
                "**Change to base 2** — the base both numbers are powers of: "
                "$$\\log_4 8 = \\frac{\\log_2 8}{\\log_2 4} = \\frac{3}{2}.$$"
                "**Read the answer as an exponent.** It claims $4^{3/2} = 8$. Check: "
                "$4^{3/2} = (4^{1/2})^3 = 2^3 = 8$ ✓. A fractional logarithm is nothing "
                "strange — IM2's rational exponents were built for exactly this.",
                [
                    "Eq(simplify(log(8, 2)), 3)",
                    "Eq(simplify(log(4, 2)), 2)",
                    "Eq(simplify(log(8, 4)), Rational(3, 2))",
                    "Eq(4**Rational(3, 2), 8)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Splitting log(x + y) into log x + log y.",
                "There is no law for the log of a SUM. The product law converts "
                "log(x·y) — multiplication inside — into addition outside. log(2 + 8) = 1 "
                "in base 10, but log 2 + log 8 = log 16 ≠ 1.",
            ),
            mistake(
                "Confusing (log x)^2 with log(x^2).",
                "The power law moves an exponent that sits on the ARGUMENT: "
                "log(x^2) = 2 log x. An exponent on the whole logarithm stays put — "
                "(log_10 100)^2 = 4 while log_10(100^2) = 4 only by coincidence of this "
                "example; try 1000: (log 1000)^2 = 9 but log(1000^2) = 6.",
            ),
            mistake(
                "Cancelling logs across a fraction: log a / log b = log(a/b).",
                "The quotient law speaks about log OF a quotient, not a quotient of logs. "
                "log 8 / log 2 = 3 (that is change of base), while log(8/2) = log 4 — "
                "different numbers entirely.",
            ),
            mistake(
                "Applying the power law to an exponent on the base.",
                "log(x^n) = n log x requires the power on the INPUT. In log_2(8) the 8 may "
                "be written 2^3 and the answer is 3 — but log_(2^3) 8 is a different "
                "question (it equals 1, since the base is 8).",
            ),
        ],
        try_it=[
            problem(
                "im3-u3-l2-t1",
                "Condense and evaluate: $\\log_{10} 50 + \\log_{10} 2$.",
                "$\\log_{10}(50 \\cdot 2) = \\log_{10} 100 = 2$.",
                [
                    "Eq(50*2, 100)",
                    "Eq(simplify(log(50, 10) + log(2, 10)), 2)",
                ],
            ),
            problem(
                "im3-u3-l2-t2",
                "Expand: $\\log_3 \\dfrac{x^2}{27}$.",
                "$\\log_3 x^2 - \\log_3 27 = 2\\log_3 x - 3$, using the power law and "
                "$3^3 = 27$.",
                ["Eq(3**3, 27)", "Eq(simplify(log(27, 3)), 3)"],
            ),
            problem(
                "im3-u3-l2-t3",
                "Evaluate $\\log_9 27$ exactly.",
                "Change to base $3$: $\\frac{\\log_3 27}{\\log_3 9} = \\frac{3}{2}$. Check "
                "as an exponent: $9^{3/2} = (9^{1/2})^3 = 3^3 = 27$ ✓.",
                [
                    "Eq(simplify(log(27, 9)), Rational(3, 2))",
                    "Eq(9**Rational(3, 2), 27)",
                ],
            ),
        ],
        steps=[
            tap(
                "Which law",
                "$\\log_2 x + \\log_2 y$ condenses to:",
                ["$\\log_2(xy)$", "$\\log_2(x + y)$", "$\\log_4(xy)$", "$\\log_2 x \\cdot \\log_2 y$"],
                0,
                "Adding logs multiplies their arguments — the product law read right to "
                "left. Nothing about the base changes.",
                ["Eq(simplify(log(4, 2) + log(8, 2)), simplify(log(32, 2)))"],
            ),
            tap(
                "The exponent-mover",
                "$\\log_5(x^7)$ equals:",
                ["$7\\log_5 x$", "$(\\log_5 x)^7$", "$\\log_{35} x$", "$\\frac{7}{\\log_5 x}$"],
                0,
                "The power law moves an exponent on the argument out front as a "
                "multiplier. $(\\log_5 x)^7$ — the power on the whole log — is a different "
                "expression that no law simplifies.",
                ["Eq(simplify(log(5**7, 5)), 7)"],
            ),
            tap(
                "No sum law",
                "In base $10$, which is TRUE?",
                ["$\\log 8 - \\log 2 = \\log 4$", "$\\log(2 + 8) = \\log 2 + \\log 8$",
                 "$\\log 8 / \\log 2 = \\log 4$", "$\\log(8 \\cdot 2) = \\log 8 \\cdot \\log 2$"],
                0,
                "Differences of logs divide the arguments: $\\log 8 - \\log 2 = "
                "\\log \\frac{8}{2} = \\log 4$ ✓. The other three each invent a law that "
                "does not exist.",
                [
                    "Eq(simplify(log(8, 10) - log(2, 10)), simplify(log(4, 10)))",
                    "Ne(simplify(log(10, 10)), simplify(log(2, 10) + log(8, 10)))",
                ],
            ),
        ],
    )


# ===========================================================================
# Lesson 3 — F-LE.4: solving exponential and logarithmic equations
# ===========================================================================

def lesson_equations():
    return lesson(
        slug="solving-exponential-and-logarithmic-equations",
        title="Solving Exponential & Logarithmic Equations",
        concrete=(
            "A rumour doubles its audience every day and $5$ people know it today. Asking "
            "\"how big in a week?\" is IM1 arithmetic: $5 \\cdot 2^7$. Asking \"WHEN do "
            "$5000$ people know?\" is new — the unknown is trapped in the exponent, and the "
            "logarithm is the tool built to reach it."
        ),
        objective=(
            "Solve exponential equations by matching bases or by taking logarithms, solve "
            "logarithmic equations by converting to exponential form, and reject "
            "candidates outside the domain."
        ),
        concept=[
            "When both sides can be written over ONE base, the exponents must match: "
            "$b^A = b^B$ forces $A = B$, because an exponential function never repeats a "
            "value. That turns an exponential equation into an ordinary one — the method "
            "to try FIRST, since it stays exact and needs no new machinery.",

            "When the bases refuse to match, take a logarithm of both sides and let the "
            "power law pull the unknown down: $2^t = 10$ becomes $t \\log 2 = \\log 10$, "
            "so $t = \\frac{\\log 10}{\\log 2}$. The answer is exact in log form; a "
            "calculator turns it into a decimal at the very last step, never earlier.",

            "A logarithmic equation runs the same road in reverse: condense to a single "
            "log, convert to exponential form, solve what remains. "
            "$\\log_2 x + \\log_2(x - 2) = 3$ condenses to $\\log_2\\big(x(x-2)\\big) = 3$, "
            "converts to $x(x - 2) = 8$, and lands in IM2's quadratic country.",

            "Here Unit 2's warning returns wearing new clothes. Condensing logs ASSUMED "
            "every log existed — assumed $x > 0$ and $x - 2 > 0$. The quadratic knows "
            "nothing of those assumptions and happily offers candidates that break them. "
            "Substitute every candidate into the ORIGINAL equation; a candidate that asks "
            "for the log of a negative number was never a solution, only a side effect of "
            "the algebra.",
        ],
        key_idea=(
            "Match the bases if you can; take a log if you cannot; convert to exponential "
            "form when the log surrounds the unknown. And check candidates against the "
            "original equation — condensing logs can invent solutions the same way "
            "squaring a radical does."
        ),
        facts=[
            fact("One-to-one", "b^A = b^B \\Rightarrow A = B",
                 "An exponential never repeats a value, so equal outputs force equal "
                 "exponents."),
            fact("Taking logs", "b^t = c \\Rightarrow t = \\frac{\\log c}{\\log b}",
                 "The power law pulls t down; the answer is exact in log form."),
            fact("Log equation", "\\log_b u = k \\Rightarrow u = b^k",
                 "Convert to exponential form once the log stands alone."),
            fact("Check", "\\text{every log's input} > 0",
                 "Candidates from the algebra must survive the original equation's "
                 "domains."),
        ],
        worked=[
            problem(
                "im3-u3-l3-we1",
                "Solve $9^{x-1} = 27^{x}$.",
                "**Match the bases.** Both are powers of $3$: $9 = 3^2$ and $27 = 3^3$, so "
                "the equation reads $3^{2(x-1)} = 3^{3x}$."
                "**Equal bases force equal exponents.** $2x - 2 = 3x$."
                "**Solve.** $x = -2$."
                "**Check.** $9^{-3} = \\frac{1}{729}$ and $27^{-2} = \\frac{1}{729}$ ✓ — "
                "the negative exponent is no obstacle, just a reciprocal.",
                [
                    "Eq(9, 3**2)",
                    "Eq(27, 3**3)",
                    "Eq(2*(-2) - 2, 3*(-2))",
                    "Eq(9**(-2 - 1), 27**(-2))",
                    "Eq(Rational(1, 729), Rational(1, 729))",
                ],
            ),
            problem(
                "im3-u3-l3-we2",
                "Solve $3 \\cdot 2^{t} = 96$.",
                "**Isolate the exponential FIRST.** Divide by $3$: $2^t = 32$. Dividing "
                "before logging keeps the arithmetic clean — logging $3 \\cdot 2^t$ head-on "
                "drags a $\\log 3$ along for no benefit."
                "**Recognise the power.** $32 = 2^5$, so $t = 5$ — the same-base shortcut "
                "applies after all."
                "**If it had not:** say $2^t = 30$. Then $t = \\frac{\\log 30}{\\log 2} = "
                "\\log_2 30$, a number a little less than $5$ — exact in log form, "
                "decimal only on demand.",
                [
                    "Eq(3*2**5, 96)",
                    "Eq(Rational(96, 3), 32)",
                    "Eq(2**5, 32)",
                    "Eq(simplify(2**(log(30)/log(2))), 30)",
                    "Eq(simplify(log(30, 2) - log(30, 2)), 0)",
                ],
            ),
            problem(
                "im3-u3-l3-we3",
                "Solve $\\log_2 x + \\log_2(x - 2) = 3$.",
                "**Condense.** $\\log_2\\big(x(x - 2)\\big) = 3$."
                "**Convert to exponential form.** $x(x - 2) = 2^3 = 8$."
                "**Solve the quadratic.** $x^2 - 2x - 8 = 0$ factors as "
                "$(x - 4)(x + 2) = 0$, so $x = 4$ or $x = -2$."
                "**Check both against the ORIGINAL.** $x = 4$: $\\log_2 4 + \\log_2 2 = "
                "2 + 1 = 3$ ✓. $x = -2$: the very first term asks for $\\log_2(-2)$, which "
                "does not exist — extraneous, exactly the way squaring manufactured "
                "candidates in Unit 2. The only solution is $x = 4$.",
                [
                    "Eq(2**3, 8)",
                    "Eq(expand((x - 4)*(x + 2)), x**2 - 2*x - 8)",
                    "Eq(4*(4 - 2), 8)",
                    "Eq(simplify(log(4, 2) + log(2, 2)), 3)",
                    "-2 < 0",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Logging both sides before isolating the exponential.",
                "In 3·2^t = 96, taking logs immediately gives log 3 + t log 2 = log 96 — "
                "correct but clumsy. Divide by 3 first: 2^t = 32, and the answer t = 5 is "
                "visible without a calculator.",
            ),
            mistake(
                "Equating exponents across DIFFERENT bases.",
                "2^x = 3^x does not force the exponents equal — the bases differ. (Its only "
                "solution is x = 0.) The one-to-one shortcut needs the same base on both "
                "sides first.",
            ),
            mistake(
                "Keeping every root of the resulting quadratic.",
                "Condensing logs assumes every input is positive; the quadratic does not "
                "remember that. Substitute each candidate into the ORIGINAL equation and "
                "discard any that asks for the log of a negative number or zero.",
            ),
            mistake(
                "Splitting log(a + b) while un-condensing.",
                "Moving between one log and many uses the product and quotient laws only. "
                "A sum INSIDE a logarithm stays where it is — there is no law for it.",
            ),
        ],
        try_it=[
            problem(
                "im3-u3-l3-t1",
                "Solve $4^{x} = 8^{x-1}$.",
                "Over base $2$: $2^{2x} = 2^{3(x-1)}$, so $2x = 3x - 3$ and $x = 3$. "
                "Check: $4^3 = 64$ and $8^2 = 64$ ✓.",
                [
                    "Eq(4, 2**2)",
                    "Eq(8, 2**3)",
                    "Eq(2*3, 3*(3 - 1))",
                    "Eq(4**3, 8**(3 - 1))",
                ],
            ),
            problem(
                "im3-u3-l3-t2",
                "Solve $\\log_3(2x + 1) = 2$.",
                "Convert: $2x + 1 = 3^2 = 9$, so $x = 4$. Check the input: "
                "$2 \\cdot 4 + 1 = 9 > 0$ ✓.",
                ["Eq(3**2, 9)", "Eq(2*4 + 1, 9)", "9 > 0"],
            ),
            problem(
                "im3-u3-l3-t3",
                "Solve $5 \\cdot 3^{n} = 405$.",
                "Divide first: $3^n = 81 = 3^4$, so $n = 4$.",
                ["Eq(Rational(405, 5), 81)", "Eq(3**4, 81)", "Eq(5*3**4, 405)"],
            ),
        ],
        steps=[
            tap(
                "First move",
                "To solve $5 \\cdot 2^{x} = 80$, the best first step is:",
                ["divide both sides by $5$", "take the log of both sides immediately",
                 "rewrite $80$ as $2^{?}$", "subtract $5$ from both sides"],
                0,
                "Isolate the exponential first: $2^x = 16$, and now $x = 4$ by "
                "inspection. Logging $5 \\cdot 2^x$ directly works but drags $\\log 5$ "
                "through every line.",
                ["Eq(Rational(80, 5), 16)", "Eq(2**4, 16)"],
            ),
            tap(
                "Matching bases",
                "Solve $25^{x} = 5^{x + 3}$.",
                ["$x = 3$", "$x = 1$", "$x = -3$", "$x = \\frac{3}{2}$"],
                0,
                "$25 = 5^2$, so $5^{2x} = 5^{x+3}$ forces $2x = x + 3$, giving $x = 3$. "
                "Check: $25^3 = 15625 = 5^6$ ✓.",
                ["Eq(25, 5**2)", "Eq(2*3, 3 + 3)", "Eq(25**3, 5**6)"],
            ),
            tap(
                "The check that matters",
                "Solving $\\log_5 x + \\log_5(x - 4) = 1$ gives candidates $x = 5$ and "
                "$x = -1$. The solution set is:",
                ["$\\{5\\}$", "$\\{5, -1\\}$", "$\\{-1\\}$", "empty"],
                0,
                "$x = -1$ asks for $\\log_5(-1)$, which does not exist — extraneous. "
                "$x = 5$: $\\log_5 5 + \\log_5 1 = 1 + 0 = 1$ ✓.",
                [
                    "Eq(5*(5 - 4), 5)",
                    "Eq(simplify(log(5, 5) + log(1, 5)), 1)",
                    "Eq(expand((x - 5)*(x + 1)), x**2 - 4*x - 5)",
                    "-1 < 0",
                ],
            ),
        ],
    )


# ===========================================================================
# Lesson 4 — modelling growth and decay
# ===========================================================================

def lesson_modelling():
    return lesson(
        slug="modelling-growth-and-decay",
        title="Modelling Growth & Decay",
        concrete=(
            "A hot cup of tea does not cool by the same number of degrees each minute — it "
            "loses the same FRACTION of its excess heat. Populations, investments, "
            "medicines in the bloodstream and radioactive samples all behave this way: "
            "equal time steps multiply by equal factors. IM1 could build these models; "
            "with logarithms this unit can finally ask them WHEN."
        ),
        objective=(
            "Build exponential models from growth rates, doubling times and half-lives, "
            "evaluate them, and solve them for the time variable."
        ),
        concept=[
            "Every exponential model is $A(t) = A_0 \\cdot b^{t}$: a starting amount and a "
            "constant factor per time step. A percentage rate hides the factor — growth of "
            "$5\\%$ per year means $b = 1.05$, decay of $10\\%$ means $b = 0.9$. The factor "
            "is $1 \\pm r$, never $r$ itself: the model keeps ALL of what it had, plus or "
            "minus the change.",

            "Doubling times and half-lives are the same idea with the clock rescaled: "
            "$A(t) = A_0 \\cdot 2^{t/d}$ doubles every $d$ units, and "
            "$A(t) = A_0 \\cdot \\left(\\frac{1}{2}\\right)^{t/h}$ halves every $h$. The "
            "exponent $t/d$ simply COUNTS the doublings — after $15$ hours with $d = 3$, "
            "five doublings have happened.",

            "Evaluating a model is substitution. SOLVING one for time is this unit's new "
            "power: isolate the exponential factor, then either recognise the power "
            "(when the numbers are kind) or take logarithms (when they are not). "
            "$500 \\cdot 2^{t/3} = 16000$ gives $2^{t/3} = 32 = 2^5$, so $t = 15$ — no "
            "calculator, just the definition of the logarithm in disguise.",

            "A model is a claim about a PATTERN, not a prophecy. The $5\\%$-growth town "
            "model is trustworthy over the range the rate was measured on; extrapolated "
            "fifty years it quietly assumes nothing else changes. Say what the base means, "
            "state the range you trust — that discipline returns in force in Unit 8.",
        ],
        key_idea=(
            "The base is the per-step multiplier: $1 + r$ growing, $1 - r$ decaying, $2$ "
            "per doubling time, $\\frac{1}{2}$ per half-life. Build the model by naming "
            "its factor; solve for time by reaching the exponent with a logarithm."
        ),
        facts=[
            fact("The model", "A(t) = A_0 \\cdot b^{t}",
                 "Start times factor-per-step. Everything else is choosing b well."),
            fact("Percent growth", "b = 1 + r",
                 "Growth of 5% per step means b = 1.05 — keep the 1."),
            fact("Percent decay", "b = 1 - r",
                 "Decay of 10% per step means b = 0.9."),
            fact("Doubling time d", "A(t) = A_0 \\cdot 2^{t/d}",
                 "t/d counts the doublings that have happened."),
            fact("Half-life h", "A(t) = A_0 \\cdot \\left(\\tfrac{1}{2}\\right)^{t/h}",
                 "t/h counts the halvings."),
        ],
        worked=[
            problem(
                "im3-u3-l4-we1",
                "A town of $8000$ people grows $5\\%$ per year. Write the model and find "
                "the population after $3$ years.",
                "**Name the factor.** Growth of $5\\%$ keeps $100\\%$ and adds $5\\%$: "
                "$b = 1.05$."
                "**Write the model.** $P(t) = 8000 \\cdot 1.05^{t}$."
                "**Evaluate at year three.** $1.05^3 = 1.157625$, so "
                "$P(3) = 8000 \\cdot 1.157625 = 9261$ — an exact figure here because "
                "$1.05 = \\frac{21}{20}$ and $8000$ conveniently absorbs the $20^3$."
                "**Interpret.** Three years of $5\\%$ growth is a factor of about $1.158$ — "
                "MORE than $15\\%$, because each year's growth compounds on the last.",
                [
                    "Eq(Rational(105, 100), Rational(21, 20))",
                    "Eq(8000*Rational(21, 20)**3, 9261)",
                    "Rational(21, 20)**3 > Rational(115, 100)",
                ],
            ),
            problem(
                "im3-u3-l4-we2",
                "A $96$ mg dose of a medicine has a half-life of $5$ hours. How much "
                "remains after $20$ hours?",
                "**Count the halvings.** $20$ hours at $5$ hours per halving is "
                "$\\frac{20}{5} = 4$ halvings."
                "**Apply them.** $A(20) = 96 \\cdot \\left(\\frac{1}{2}\\right)^4 = "
                "\\frac{96}{16} = 6$ mg."
                "**Read the model's shape.** Equal time steps multiply by equal factors — "
                "the amount never reaches zero, it only halves toward it. That asymptote "
                "at zero is the same one the exponential graph has always had.",
                [
                    "Eq(Rational(20, 5), 4)",
                    "Eq(96*Rational(1, 2)**4, 6)",
                    "Eq(Rational(96, 16), 6)",
                ],
            ),
            problem(
                "im3-u3-l4-we3",
                "A bacteria culture of $500$ cells doubles every $3$ hours. When does it "
                "reach $16{,}000$ cells?",
                "**Write the model.** $N(t) = 500 \\cdot 2^{t/3}$."
                "**Set and isolate.** $500 \\cdot 2^{t/3} = 16000$ gives "
                "$2^{t/3} = 32$."
                "**Reach the exponent.** $32 = 2^5$, so $\\frac{t}{3} = 5$ and $t = 15$ "
                "hours. (Had the target not been a clean power, "
                "$\\frac{t}{3} = \\log_2 32$ says the same thing in general costume.)"
                "**Check.** Five doublings from $500$: $1000, 2000, 4000, 8000, 16000$ ✓.",
                [
                    "Eq(Rational(16000, 500), 32)",
                    "Eq(2**5, 32)",
                    "Eq(500*2**5, 16000)",
                    "Eq(simplify(log(32, 2)), 5)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Using b = r instead of b = 1 + r.",
                "Growth of 5% per year is a factor of 1.05, not 0.05. A base of 0.05 "
                "would DESTROY 95% of the population each year — the model keeps what it "
                "had, plus the change.",
            ),
            mistake(
                "Adding the same amount each step (linear thinking).",
                "5% growth from 8000 is not '+400 per year'. The second year grows 5% of "
                "8400, not of 8000 — compounding is the whole point of the exponential "
                "model, and it is why P(3) = 9261 rather than 9200.",
            ),
            mistake(
                "Dividing the time by the wrong constant.",
                "In A_0 · 2^(t/d), the exponent counts doublings: t divided by the "
                "DOUBLING TIME. After 20 hours with a 5-hour half-life, 20/5 = 4 halvings "
                "have happened — not 5/20 of one.",
            ),
            mistake(
                "Reporting the log-form answer as unfinished.",
                "t = log_2 30 IS an answer — exact, checkable, and convertible to a "
                "decimal whenever needed. Rounding early and carrying 4.9 through further "
                "algebra is what loses marks.",
            ),
        ],
        try_it=[
            problem(
                "im3-u3-l4-t1",
                "A $4000$ tögrög account loses $10\\%$ of its value each year. What is it "
                "worth after $2$ years?",
                "Decay factor $b = 0.9$: $4000 \\cdot 0.9^2 = 4000 \\cdot 0.81 = 3240$ "
                "tögrög.",
                [
                    "Eq(4000*Rational(9, 10)**2, 3240)",
                    "Eq(Rational(9, 10)**2, Rational(81, 100))",
                ],
            ),
            problem(
                "im3-u3-l4-t2",
                "A sample of $80$ g has a half-life of $6$ days. How much remains after "
                "$18$ days?",
                "$\\frac{18}{6} = 3$ halvings: $80 \\cdot \\left(\\frac{1}{2}\\right)^3 = "
                "10$ g.",
                ["Eq(Rational(18, 6), 3)", "Eq(80*Rational(1, 2)**3, 10)"],
            ),
            problem(
                "im3-u3-l4-t3",
                "A population of $250$ doubles every $4$ years. When does it reach "
                "$4000$?",
                "$250 \\cdot 2^{t/4} = 4000$ gives $2^{t/4} = 16 = 2^4$, so "
                "$\\frac{t}{4} = 4$ and $t = 16$ years.",
                [
                    "Eq(Rational(4000, 250), 16)",
                    "Eq(2**4, 16)",
                    "Eq(250*2**4, 4000)",
                ],
            ),
        ],
        steps=[
            tap(
                "Name the factor",
                "A quantity DECAYS by $20\\%$ per week. Its weekly factor is:",
                ["$0.8$", "$0.2$", "$1.2$", "$-0.2$"],
                0,
                "Keep $100\\%$, lose $20\\%$: the multiplier is $0.8$. A factor of $0.2$ "
                "would be an $80\\%$ collapse each week.",
                ["Eq(1 - Rational(20, 100), Rational(4, 5))"],
            ),
            tap(
                "Counting doublings",
                "$N(t) = 300 \\cdot 2^{t/6}$, with $t$ in hours. After $18$ hours the "
                "population is:",
                ["$2400$", "$900$", "$5400$", "$1800$"],
                0,
                "$\\frac{18}{6} = 3$ doublings: $300 \\to 600 \\to 1200 \\to 2400$.",
                ["Eq(Rational(18, 6), 3)", "Eq(300*2**3, 2400)"],
            ),
            tap(
                "Solving for time",
                "$100 \\cdot 3^{t} = 8100$ gives $t = $:",
                ["$4$", "$3$", "$27$", "$81$"],
                0,
                "Isolate: $3^t = 81 = 3^4$, so $t = 4$. The logarithm answered before it "
                "was named.",
                ["Eq(Rational(8100, 100), 81)", "Eq(3**4, 81)"],
            ),
        ],
    )


# ===========================================================================
# Practice bank
# ===========================================================================

def practice_bank():
    return [
        problem(
            "im3-u3-p1",
            "Evaluate $\\log_2 64$.",
            "Two to what power is $64$? $2^6 = 64$, so the answer is $6$.",
            ["Eq(2**6, 64)", "Eq(simplify(log(64, 2)), 6)"],
        ),
        problem(
            "im3-u3-p2",
            "Evaluate $\\log_6 1$ and $\\log_9 9$.",
            "Any base to the power $0$ is $1$, so $\\log_6 1 = 0$; and the exponent that "
            "turns $9$ into $9$ is $1$, so $\\log_9 9 = 1$.",
            ["Eq(6**0, 1)", "Eq(9**1, 9)"],
        ),
        problem(
            "im3-u3-p3",
            "Evaluate $\\log_4 \\dfrac{1}{16}$.",
            "$4^2 = 16$, so $4^{-2} = \\frac{1}{16}$ and the logarithm is $-2$.",
            ["Eq(4**(-2), Rational(1, 16))", "Eq(simplify(log(Rational(1, 16), 4)), -2)"],
        ),
        problem(
            "im3-u3-p4",
            "Solve $\\log_5 x = 3$.",
            "Convert to exponential form: $x = 5^3 = 125$.",
            ["Eq(5**3, 125)"],
        ),
        problem(
            "im3-u3-p5",
            "Solve $\\log_x 64 = 3$.",
            "Convert: $x^3 = 64$, so $x = 4$ (the cube root; a base must be positive).",
            ["Eq(4**3, 64)"],
        ),
        problem(
            "im3-u3-p6",
            "State the domain of $f(x) = \\log_3(2x - 6)$.",
            "Require $2x - 6 > 0$, so $x > 3$. The vertical asymptote is $x = 3$.",
            ["Eq(2*3 - 6, 0)", "2*4 - 6 > 0"],
        ),
        problem(
            "im3-u3-p7",
            "Condense and evaluate: $\\log_2 40 - \\log_2 5$.",
            "The quotient law: $\\log_2 \\frac{40}{5} = \\log_2 8 = 3$.",
            [
                "Eq(Rational(40, 5), 8)",
                "Eq(simplify(log(40, 2) - log(5, 2)), 3)",
            ],
        ),
        problem(
            "im3-u3-p8",
            "Condense and evaluate: $3\\log_{10} 2 + \\log_{10} 125$.",
            "$3\\log 2 = \\log 8$, and $\\log 8 + \\log 125 = \\log 1000 = 3$.",
            [
                "Eq(2**3, 8)",
                "Eq(8*125, 1000)",
                "Eq(simplify(3*log(2, 10) + log(125, 10)), 3)",
            ],
        ),
        problem(
            "im3-u3-p9",
            "Expand: $\\log_5 \\dfrac{25a^2}{b}$.",
            "$\\log_5 25 + \\log_5 a^2 - \\log_5 b = 2 + 2\\log_5 a - \\log_5 b$.",
            ["Eq(5**2, 25)", "Eq(simplify(log(25, 5)), 2)"],
        ),
        problem(
            "im3-u3-p10",
            "Evaluate $\\log_8 32$ exactly.",
            "Change to base $2$: $\\frac{\\log_2 32}{\\log_2 8} = \\frac{5}{3}$. Check: "
            "$8^{5/3} = (8^{1/3})^5 = 2^5 = 32$ ✓.",
            [
                "Eq(simplify(log(32, 8)), Rational(5, 3))",
                "Eq(8**Rational(5, 3), 32)",
            ],
        ),
        problem(
            "im3-u3-p11",
            "Solve $2^{3x - 1} = 16$.",
            "$16 = 2^4$, so $3x - 1 = 4$ and $x = \\frac{5}{3}$.",
            [
                "Eq(2**4, 16)",
                "Eq(3*Rational(5, 3) - 1, 4)",
            ],
        ),
        problem(
            "im3-u3-p12",
            "Solve $7 \\cdot 5^{n} = 875$.",
            "Divide first: $5^n = 125 = 5^3$, so $n = 3$.",
            ["Eq(Rational(875, 7), 125)", "Eq(5**3, 125)", "Eq(7*5**3, 875)"],
        ),
        problem(
            "im3-u3-p13",
            "Solve $\\log_2(x + 3) = 4$.",
            "Convert: $x + 3 = 2^4 = 16$, so $x = 13$. The input $16$ is positive ✓.",
            ["Eq(2**4, 16)", "Eq(13 + 3, 16)", "16 > 0"],
        ),
        problem(
            "im3-u3-p14",
            "A car worth $20{,}000{,}000$ tögrög loses $10\\%$ of its value each year. "
            "What is it worth after $3$ years?",
            "Factor $0.9$ per year: $20\\,000\\,000 \\cdot 0.9^3 = 20\\,000\\,000 \\cdot "
            "0.729 = 14\\,580\\,000$ tögrög.",
            [
                "Eq(Rational(9, 10)**3, Rational(729, 1000))",
                "Eq(20000000*Rational(9, 10)**3, 14580000)",
            ],
        ),
        problem(
            "im3-u3-p15",
            "A culture of $600$ bacteria doubles every $5$ hours. Write the model and "
            "find the count after $15$ hours.",
            "$N(t) = 600 \\cdot 2^{t/5}$; at $t = 15$ there have been $3$ doublings: "
            "$600 \\cdot 8 = 4800$.",
            ["Eq(Rational(15, 5), 3)", "Eq(600*2**3, 4800)"],
        ),
        problem(
            "im3-u3-p16",
            "Solve $\\log_3 x + \\log_3(x - 8) = 2$.",
            "Condense: $x(x - 8) = 3^2 = 9$, so $x^2 - 8x - 9 = 0 = (x - 9)(x + 1)$, "
            "giving $x = 9$ or $x = -1$. Reject $x = -1$ (log of a negative); check "
            "$x = 9$: $\\log_3 9 + \\log_3 1 = 2 + 0 = 2$ ✓.",
            [
                "Eq(3**2, 9)",
                "Eq(expand((x - 9)*(x + 1)), x**2 - 8*x - 9)",
                "Eq(9*(9 - 8), 9)",
                "Eq(simplify(log(9, 3) + log(1, 3)), 2)",
                "-1 < 0",
            ],
        ),
    ]


# ===========================================================================
# Test-yourself bank
# ===========================================================================

def test_bank():
    return [
        problem(
            "im3-u3-x1",
            "Evaluate $\\log_7 343$ and $\\log_2 \\dfrac{1}{8}$.",
            "$7^3 = 343$, so the first is $3$. $2^3 = 8$, so $2^{-3} = \\frac{1}{8}$ and "
            "the second is $-3$.",
            [
                "Eq(7**3, 343)",
                "Eq(2**(-3), Rational(1, 8))",
                "Eq(simplify(log(343, 7)), 3)",
            ],
        ),
        problem(
            "im3-u3-x2",
            "Solve $\\log_x 81 = 4$.",
            "$x^4 = 81$, so $x = 3$ — the positive fourth root, since a base must be "
            "positive and not $1$. ($x = -3$ also satisfies the power but fails the base "
            "restriction.)",
            ["Eq(3**4, 81)", "Eq((-3)**4, 81)", "Ne(-3, 3)"],
        ),
        problem(
            "im3-u3-x3",
            "Condense and evaluate: $\\log_6 9 + \\log_6 4$.",
            "$\\log_6(9 \\cdot 4) = \\log_6 36 = 2$.",
            ["Eq(9*4, 36)", "Eq(simplify(log(9, 6) + log(4, 6)), 2)"],
        ),
        problem(
            "im3-u3-x4",
            "Given $\\log_{10} 2 \\approx 0.301$, estimate $\\log_{10} 32$ without a "
            "calculator, and explain the law you used.",
            "$32 = 2^5$, so the power law gives $\\log 32 = 5\\log 2 \\approx 5 \\cdot "
            "0.301 = 1.505$. The exact claim behind the estimate is "
            "$\\log_{10} 32 = 5\\log_{10} 2$.",
            [
                "Eq(2**5, 32)",
                "Eq(simplify(log(32, 10) - 5*log(2, 10)), 0)",
                "Eq(5*Rational(301, 1000), Rational(301, 200))",
                "Abs(Rational(301, 200) - Rational(3, 2)) < Rational(1, 100)",
            ],
        ),
        problem(
            "im3-u3-x5",
            "Solve $27^{x} = 9^{x + 2}$.",
            "Over base $3$: $3^{3x} = 3^{2(x+2)}$, so $3x = 2x + 4$ and $x = 4$. Check: "
            "$27^4 = 531441 = 9^6$ ✓.",
            [
                "Eq(27, 3**3)",
                "Eq(9, 3**2)",
                "Eq(3*4, 2*(4 + 2))",
                "Eq(27**4, 9**6)",
            ],
        ),
        problem(
            "im3-u3-x6",
            "Solve $\\log_2(x + 5) + \\log_2(x - 1) = 4$, rejecting any extraneous "
            "candidate and saying why it is extraneous.",
            "Condense: $(x + 5)(x - 1) = 2^4 = 16$, so $x^2 + 4x - 21 = 0 = "
            "(x + 7)(x - 3)$, giving $x = 3$ or $x = -7$. At $x = -7$ BOTH logs ask for "
            "negative inputs — the candidate came from the condensed equation, which never "
            "knew the domain. At $x = 3$: $\\log_2 8 + \\log_2 2 = 3 + 1 = 4$ ✓. Solution: "
            "$x = 3$.",
            [
                "Eq(2**4, 16)",
                "Eq(expand((x + 7)*(x - 3)), x**2 + 4*x - 21)",
                "Eq((3 + 5)*(3 - 1), 16)",
                "Eq(simplify(log(8, 2) + log(2, 2)), 4)",
                "-7 + 5 < 0",
            ],
        ),
        problem(
            "im3-u3-x7",
            "A radioactive sample of $54$ g has a half-life of $8$ days. How much remains "
            "after $24$ days, and after how many days does $27$ g remain?",
            "$\\frac{24}{8} = 3$ halvings: $54 \\cdot \\frac{1}{8} = 6.75$ g, i.e. "
            "$\\frac{27}{4}$ g. And $27$ g is exactly HALF of $54$, so it remains after "
            "one half-life: $8$ days.",
            [
                "Eq(Rational(24, 8), 3)",
                "Eq(54*Rational(1, 2)**3, Rational(27, 4))",
                "Eq(54*Rational(1, 2), 27)",
            ],
        ),
        problem(
            "im3-u3-x8",
            "An investment of $2{,}000{,}000$ tögrög grows $8\\%$ per year. Write the "
            "model, find its value after $2$ years, and write — as a logarithm — the "
            "number of years until it doubles.",
            "Model: $V(t) = 2\\,000\\,000 \\cdot 1.08^{t}$. After two years: "
            "$2\\,000\\,000 \\cdot 1.1664 = 2\\,332\\,800$ tögrög. Doubling asks "
            "$1.08^{t} = 2$, so $t = \\log_{1.08} 2 = \\frac{\\log 2}{\\log 1.08}$ — a "
            "little over $9$ years, exact in log form.",
            [
                "Eq(Rational(108, 100)**2, Rational(11664, 10000))",
                "Eq(2000000*Rational(108, 100)**2, 2332800)",
                "Rational(108, 100)**9 < 2",
                "Rational(108, 100)**10 > 2",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="exponential-and-logarithmic-functions",
        title="Exponential & Logarithmic Functions",
        unit_number=3,
        blurb=(
            "The logarithm as the inverse of an exponential, the three laws and where they "
            "come from, solving equations in the exponent, and modelling growth and decay."
        ),
        builds_on=(
            "Exponential functions from IM1 Unit 6 — now with a way to solve for the "
            "exponent — and the check-your-candidates discipline of IM3 Unit 2, which log "
            "equations demand for exactly the same reason."
        ),
        lessons=[
            lesson_inverse(),
            lesson_laws(),
            lesson_equations(),
            lesson_modelling(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
