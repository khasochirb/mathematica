#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 2: Rational & Radical Functions.

CCSS Integrated Math III: A-APR.6 (rewrite a(x)/b(x) as q(x) + r(x)/b(x)),
A-APR.7 (rational expressions form a system closed under +, -, x and division
by a nonzero expression — the analogue of the rational numbers), F-IF.7d
(graph rational functions, identifying zeros and asymptotes), A-REI.2 (solve
rational and radical equations, and give examples showing how extraneous
solutions arise).

The unit has one through-line, and it is worth saying out loud because the
two halves look unrelated: DIVIDING and ROOTING both narrow the domain, and
a solving step that ignores the narrowing is exactly what manufactures an
extraneous root. Multiplying away a denominator and squaring away a radical
are the same move — each is a non-reversible step that can only ever ADD
candidates, never lose them, which is why checking is not optional
bookkeeping but the last line of the method.

Run: python3 scripts/im/build_im3_unit2.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — F-IF.7d: domain, holes and asymptotes
# ===========================================================================

def lesson_asymptotes():
    return lesson(
        slug="rational-functions-and-asymptotes",
        title="Rational Functions & Their Asymptotes",
        concrete=(
            "Sharing $12$ sweets among $n$ children gives $\\frac{12}{n}$ each. Ask what happens "
            "as more children arrive and the shares shrink toward nothing but never reach it; "
            "ask what happens as $n$ approaches zero and the shares blow up. Both behaviours "
            "are already in the arithmetic — the graph just draws them."
        ),
        objective=(
            "Find the domain of a rational function, distinguish a hole from a vertical "
            "asymptote, and read the horizontal asymptote off the degrees."
        ),
        concept=[
            "A rational function is one polynomial over another, $f(x) = \\frac{p(x)}{q(x)}$. "
            "Everything interesting about it comes from one fact: division by zero is undefined, "
            "so every $x$ with $q(x) = 0$ is thrown out of the domain.",

            "Being thrown out of the domain is not the same as having a vertical asymptote. "
            "Factor first. If a factor cancels between top and bottom, the function is "
            "undefined there but the values on either side approach an ordinary number — that "
            "is a HOLE. If the factor survives in the denominator, the values grow without "
            "bound — that is a VERTICAL ASYMPTOTE.",

            "The end behaviour is a race between degrees. If the bottom wins (denominator has "
            "the higher degree) the fraction is squeezed to $0$, so $y = 0$ is the horizontal "
            "asymptote. If the degrees tie, the leading coefficients decide and the asymptote "
            "is their ratio. If the top wins there is no horizontal asymptote at all — the "
            "function escapes.",

            "None of this needs a table of values. Factor, cancel, compare degrees: the domain, "
            "the holes, the vertical asymptotes and the horizontal asymptote all fall out of "
            "the algebra, and the sketch is then a matter of joining the pieces.",
        ],
        key_idea=(
            "Factor before you conclude anything. A cancelled factor is a hole; a surviving "
            "one is a vertical asymptote; and the degrees — not the graph — decide the "
            "horizontal asymptote."
        ),
        facts=[
            fact("Domain", "q(x) \\ne 0",
                 "Every zero of the denominator leaves the domain, whether it turns out to be a "
                 "hole or an asymptote."),
            fact("Vertical asymptote", "x = a \\text{ when } (x - a) \\text{ survives in } q(x)",
                 "The factor must remain in the denominator AFTER cancelling."),
            fact("Hole", "x = a \\text{ when } (x - a) \\text{ cancels}",
                 "Undefined at that point, but the nearby values approach a finite number."),
            fact("Horizontal asymptote", "\\deg p < \\deg q \\Rightarrow y = 0",
                 "The denominator outgrows the numerator, so the ratio is squeezed to zero."),
            fact("Equal degrees", "y = \\frac{a_n}{b_n}",
                 "A tie is settled by the leading coefficients."),
            fact("Numerator wins", "\\deg p > \\deg q \\Rightarrow \\text{none}",
                 "The values grow without bound; there is no horizontal asymptote."),
        ],
        worked=[
            problem(
                "im3-u2-l1-we1",
                "Find the domain of $f(x) = \\dfrac{x + 3}{x^2 - 5x + 6}$.",
                "**Factor the denominator.** $x^2 - 5x + 6 = (x - 2)(x - 3)$."
                "**Set it to zero.** It vanishes at $x = 2$ and $x = 3$."
                "**State the domain.** Everything except those two values: "
                "$x \\ne 2$ and $x \\ne 3$."
                "**Check the numerator does not rescue either.** At $x = 2$ the numerator is "
                "$2 + 3 = 5 \\ne 0$, and at $x = 3$ it is $6 \\ne 0$. Neither factor cancels, so "
                "both are genuine vertical asymptotes rather than holes.",
                [
                    "Eq(expand((x - 2)*(x - 3)), x**2 - 5*x + 6)",
                    "Eq(2 + 3, 5)",
                    "Ne(2 + 3, 0)",
                    "Ne(3 + 3, 0)",
                ],
            ),
            problem(
                "im3-u2-l1-we2",
                "Identify every hole and vertical asymptote of "
                "$g(x) = \\dfrac{x^2 - 9}{x^2 - 2x - 3}$.",
                "**Factor both.** $x^2 - 9 = (x - 3)(x + 3)$ and "
                "$x^2 - 2x - 3 = (x - 3)(x + 1)$."
                "**Cancel what is common.** The $(x - 3)$ appears in both, so for $x \\ne 3$, "
                "$$g(x) = \\frac{x + 3}{x + 1}.$$"
                "**Read the two kinds of break.** The cancelled factor gives a HOLE at $x = 3$; "
                "the surviving $(x + 1)$ gives a VERTICAL ASYMPTOTE at $x = -1$."
                "**Locate the hole's height.** Substituting $x = 3$ into the simplified form: "
                "$\\frac{3 + 3}{3 + 1} = \\frac{6}{4} = \\frac{3}{2}$. So the graph is a normal "
                "curve with a single point punched out at $\\left(3,\\ \\frac{3}{2}\\right)$ — "
                "the function is undefined there, but nothing dramatic happens.",
                [
                    "Eq(expand((x - 3)*(x + 3)), x**2 - 9)",
                    "Eq(expand((x - 3)*(x + 1)), x**2 - 2*x - 3)",
                    "Eq(Rational(3 + 3, 3 + 1), Rational(3, 2))",
                ],
            ),
            problem(
                "im3-u2-l1-we3",
                "Find the horizontal asymptote of each: "
                "(a) $\\dfrac{2x + 1}{x^2 - 4}$, (b) $\\dfrac{3x^2 - x}{5x^2 + 2}$, "
                "(c) $\\dfrac{x^3}{x^2 + 1}$.",
                "**(a) Compare degrees.** Top is degree $1$, bottom degree $2$ — the bottom "
                "wins, so the fraction is squeezed toward zero: $y = 0$."
                "**(b) A tie.** Both are degree $2$, so the leading coefficients decide: "
                "$y = \\frac{3}{5}$. Sanity-check with a large input: at $x = 100$ the value is "
                "$\\frac{30000 - 100}{50000 + 2} = \\frac{29900}{50002} \\approx 0.598$, already "
                "close to $0.6$."
                "**(c) Top wins.** Degree $3$ over degree $2$ grows without bound, so there is "
                "NO horizontal asymptote."
                "**The rule behind all three.** Only the leading terms matter far from the "
                "origin; every lower-order term becomes negligible in the comparison.",
                [
                    "Eq(Rational(3, 5), Rational(3, 5))",
                    "Eq(Rational(3*100**2 - 100, 5*100**2 + 2), Rational(29900, 50002))",
                    "Abs(Rational(29900, 50002) - Rational(3,5)) < Rational(1, 100)",
                    "3 > 2",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Calling every zero of the denominator a vertical asymptote.",
                "Cancel first. A factor common to top and bottom gives a HOLE, not an asymptote "
                "— the graph is finite there, just missing one point.",
            ),
            mistake(
                "Reading the horizontal asymptote off the constant terms.",
                "Only the LEADING terms matter as x grows. In (3x^2 - x)/(5x^2 + 2) the "
                "asymptote is 3/5, nothing to do with the -x or the +2.",
            ),
            mistake(
                "Assuming a graph can never cross its horizontal asymptote.",
                "It may cross in the middle; the asymptote only describes the behaviour far out. "
                "A VERTICAL asymptote genuinely can never be crossed — the function is "
                "undefined there.",
            ),
            mistake(
                "Cancelling a factor and forgetting the point is still excluded.",
                "Simplifying to (x + 3)/(x + 1) is only valid for x ≠ 3. The hole survives the "
                "simplification even though the algebra no longer shows it.",
            ),
        ],
        try_it=[
            problem(
                "im3-u2-l1-t1",
                "State the domain of $h(x) = \\dfrac{x - 1}{x^2 - 16}$.",
                "$x^2 - 16 = (x - 4)(x + 4)$, which vanishes at $x = 4$ and $x = -4$. The "
                "numerator is nonzero at both, so both are vertical asymptotes and the domain "
                "is every real number except $4$ and $-4$.",
                [
                    "Eq(expand((x - 4)*(x + 4)), x**2 - 16)",
                    "Ne(4 - 1, 0)",
                    "Ne(-4 - 1, 0)",
                ],
            ),
            problem(
                "im3-u2-l1-t2",
                "Does $f(x) = \\dfrac{x^2 - 4}{x - 2}$ have a hole or an asymptote at $x = 2$? "
                "Give the height if it is a hole.",
                "$x^2 - 4 = (x - 2)(x + 2)$, so the $(x - 2)$ cancels and $f(x) = x + 2$ for "
                "$x \\ne 2$. That is a HOLE, not an asymptote. Its height is $2 + 2 = 4$, so the "
                "graph is the line $y = x + 2$ with the point $(2,\\ 4)$ removed.",
                [
                    "Eq(expand((x - 2)*(x + 2)), x**2 - 4)",
                    "Eq(2 + 2, 4)",
                ],
            ),
            problem(
                "im3-u2-l1-t3",
                "Find the horizontal asymptote of $\\dfrac{7x^2 + 3}{2x^2 - x}$.",
                "The degrees tie at $2$, so the leading coefficients settle it: "
                "$y = \\frac{7}{2}$.",
                ["Eq(Rational(7, 2), Rational(7, 2))"],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "Division by zero writes the map", "body": "A rational function is one polynomial over another, and everything interesting about it comes from the places the bottom is zero. But being thrown out of the domain is not the same as having an asymptote — FACTOR first. A factor that cancels leaves a hole; a factor that survives forces a vertical asymptote.", "beats": ["Domain: bottom ≠ 0", "Cancelled factor → hole", "Surviving factor → vertical asymptote"]},
            {"kind": "worked", "title": "Reading the domain off the denominator", "problemId": "im3-u2-l1-we1"},
            
            tap(
                "Domain first",
                "Which values must be excluded from the domain of "
                "$\\dfrac{x + 5}{x^2 - x - 6}$?",
                ["$x \\ne 3$ and $x \\ne -2$", "$x \\ne -5$",
                 "$x \\ne 6$ and $x \\ne -1$", "no values are excluded"],
                0,
                "Factor: $x^2 - x - 6 = (x - 3)(x + 2)$, which vanishes at $x = 3$ and "
                "$x = -2$. The numerator's zero at $x = -5$ is perfectly legal — it just makes "
                "the function equal zero there.",
                [
                    "Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
                    "Eq(3**2 - 3 - 6, 0)",
                    "Eq((-2)**2 - (-2) - 6, 0)",
                ],
            ),
            {"kind": "worked", "title": "Hole or asymptote — factor and see", "problemId": "im3-u2-l1-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "A hole still empties the domain", "body": "Cancelling $(x - 3)$ from top and bottom removes the asymptote, not the exclusion. The simplified formula is a different function unless you carry the restriction $x \\ne 3$ along with it."},
            tap(
                "Hole or asymptote",
                "In $\\dfrac{(x - 4)(x + 1)}{(x - 4)(x - 2)}$, what happens at $x = 4$?",
                ["a hole", "a vertical asymptote", "a horizontal asymptote",
                 "nothing — it is in the domain"],
                0,
                "The $(x - 4)$ cancels, so the function is undefined at $x = 4$ but approaches "
                "the finite value $\\frac{4 + 1}{4 - 2} = \\frac{5}{2}$. That is a hole. The "
                "surviving $(x - 2)$ is what gives the vertical asymptote, at $x = 2$.",
                [
                    "Eq(Rational(4 + 1, 4 - 2), Rational(5, 2))",
                ],
            ),
            {"kind": "worked", "title": "Three horizontal-asymptote races", "problemId": "im3-u2-l1-we3"},
            {"kind": "teach", "title": "The ends are a race between degrees", "body": "As $|x|$ grows, only the leading terms matter — so compare degrees. Bottom wins: the fraction is squeezed to $y = 0$. A tie: $y$ levels off at the ratio of leading coefficients. Top wins: no horizontal asymptote at all.", "beats": ["Bottom wins → $y = 0$", "Tie → ratio of leading coefficients", "Top wins → none"]},
            {"kind": "tryIt", "title": "Domain drill", "problemId": "im3-u2-l1-t1"},
            {"kind": "tryIt", "title": "Hole or asymptote?", "problemId": "im3-u2-l1-t2"},
            tap(
                "The degree race",
                "What is the horizontal asymptote of $\\dfrac{4x + 9}{x^2 + 1}$?",
                ["$y = 0$", "$y = 4$", "$y = 9$", "there is none"],
                0,
                "The denominator has the higher degree, so it outgrows the numerator and the "
                "ratio is squeezed toward zero: $y = 0$. At $x = 100$ the value is already "
                "$\\frac{409}{10001} \\approx 0.04$.",
                [
                    "Eq(Rational(4*100 + 9, 100**2 + 1), Rational(409, 10001))",
                    "Rational(409, 10001) < Rational(1, 20)",
                    "2 > 1",
                ],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["Domain: every zero of the denominator is excluded", "Factor first — cancelled factor is a hole, surviving factor is a vertical asymptote", "Horizontal asymptote: compare degrees, not constants", "A graph may cross its horizontal asymptote in the middle; it describes the ENDS", "The excluded point survives every simplification"]},
        ],
    )


# ===========================================================================
# Lesson 2 — A-APR.7: the algebra of rational expressions
# ===========================================================================

def lesson_operations():
    return lesson(
        slug="operations-on-rational-expressions",
        title="Adding, Multiplying & Dividing Rational Expressions",
        concrete=(
            "Adding $\\frac{1}{6} + \\frac{1}{4}$ needs a common denominator of $12$, not $24$ "
            "— and finding it means factoring $6 = 2 \\cdot 3$ and $4 = 2^2$ and taking each "
            "prime the greatest number of times it appears. Rational expressions work the same "
            "way with $(x - 1)$ in place of the prime $2$."
        ),
        objective=(
            "Multiply, divide, add and subtract rational expressions, and state the "
            "restrictions the operations require."
        ),
        concept=[
            "Rational expressions behave exactly like fractions of integers, because they are "
            "built the same way: a ratio of two objects you can add and multiply. Sums, "
            "differences, products and quotients of rational expressions are rational "
            "expressions again — the system is CLOSED, just as the rational numbers are.",

            "Multiplying is the easy direction: multiply tops, multiply bottoms, then cancel "
            "common factors. The only discipline is to factor FIRST, so you cancel factors and "
            "never terms.",

            "Dividing is multiplying by the reciprocal. The one extra care point is that the "
            "expression you flip must not be zero, so its numerator contributes a restriction "
            "of its own — a restriction that vanishes from the written answer and must be "
            "carried anyway.",

            "Adding needs a common denominator, and the efficient one is the LEAST common "
            "denominator: factor every denominator, then take each distinct factor the greatest "
            "number of times it appears in any one of them. Multiplying all the denominators "
            "together also works, but produces an expression you then have to simplify back "
            "down.",
        ],
        key_idea=(
            "Factor first, every time. Cancelling is only legal on FACTORS, the LCD is built "
            "from factors, and the restrictions are read off factors."
        ),
        facts=[
            fact("Multiply", "\\frac{a}{b} \\cdot \\frac{c}{d} = \\frac{ac}{bd}",
                 "Then cancel common factors — never common terms."),
            fact("Divide", "\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\cdot \\frac{d}{c}",
                 "Flip and multiply; the flipped numerator c must also be nonzero."),
            fact("Add", "\\frac{a}{b} + \\frac{c}{d} = \\frac{ad + bc}{bd}",
                 "Correct always, but the LCD is usually smaller than bd."),
            fact("LCD", "\\text{each factor, greatest power seen}",
                 "Factor every denominator first, exactly as with numerical fractions."),
            fact("Closure", "\\text{rational} \\pm \\times \\div \\text{rational} = \\text{rational}",
                 "The system mirrors the rational numbers, which is why the rules feel familiar."),
        ],
        worked=[
            problem(
                "im3-u2-l2-we1",
                "Simplify $\\dfrac{x^2 - 4}{x^2 + 6x + 9} \\cdot \\dfrac{x + 3}{x - 2}$.",
                "**Factor everything.** $x^2 - 4 = (x - 2)(x + 2)$ and "
                "$x^2 + 6x + 9 = (x + 3)^2$."
                "**Write the single product.**"
                "$$\\frac{(x - 2)(x + 2)}{(x + 3)^2} \\cdot \\frac{x + 3}{x - 2}$$"
                "**Cancel common FACTORS.** The $(x - 2)$ cancels, and one $(x + 3)$ cancels "
                "against the square, leaving"
                "$$\\frac{x + 2}{x + 3}.$$"
                "**State the restrictions.** The original denominators required $x \\ne -3$ and "
                "$x \\ne 2$. The $x \\ne 2$ is invisible in the simplified answer, which is "
                "exactly why it has to be written down.",
                [
                    "Eq(expand((x - 2)*(x + 2)), x**2 - 4)",
                    "Eq(expand((x + 3)**2), x**2 + 6*x + 9)",
                    "Eq(simplify(((x**2 - 4)/(x**2 + 6*x + 9))*((x + 3)/(x - 2)) - (x + 2)/(x + 3)), 0)",
                ],
            ),
            problem(
                "im3-u2-l2-we2",
                "Simplify $\\dfrac{x^2 - 1}{x + 4} \\div \\dfrac{x - 1}{x^2 - 16}$.",
                "**Flip the divisor and multiply.**"
                "$$\\frac{x^2 - 1}{x + 4} \\cdot \\frac{x^2 - 16}{x - 1}$$"
                "**Factor.** $x^2 - 1 = (x - 1)(x + 1)$ and $x^2 - 16 = (x - 4)(x + 4)$."
                "**Cancel.** The $(x - 1)$ and the $(x + 4)$ both go, leaving"
                "$$(x + 1)(x - 4).$$"
                "**Collect the restrictions.** From the original denominators, $x \\ne -4$ and "
                "$x \\ne 1$; and because we DIVIDED by $\\frac{x - 1}{x^2 - 16}$, that quotient "
                "may not be zero either, which also forbids $x = 1$. The polynomial answer looks "
                "defined everywhere — the restrictions are the only record that it is not.",
                [
                    "Eq(expand((x - 1)*(x + 1)), x**2 - 1)",
                    "Eq(expand((x - 4)*(x + 4)), x**2 - 16)",
                    "Eq(simplify(((x**2 - 1)/(x + 4))/((x - 1)/(x**2 - 16)) - (x + 1)*(x - 4)), 0)",
                ],
            ),
            problem(
                "im3-u2-l2-we3",
                "Add $\\dfrac{3}{x - 2} + \\dfrac{5}{x + 1}$ and state the restrictions.",
                "**Factor the denominators.** They are already factored and share nothing, so "
                "the LCD is their product $(x - 2)(x + 1)$."
                "**Rewrite each fraction over the LCD.**"
                "$$\\frac{3(x + 1)}{(x - 2)(x + 1)} + \\frac{5(x - 2)}{(x - 2)(x + 1)}$$"
                "**Add the numerators.**"
                "$$\\frac{3x + 3 + 5x - 10}{(x - 2)(x + 1)} = \\frac{8x - 7}{(x - 2)(x + 1)}$$"
                "**Restrictions.** $x \\ne 2$ and $x \\ne -1$."
                "**Check with a number.** At $x = 3$ the original is "
                "$\\frac{3}{1} + \\frac{5}{4} = \\frac{17}{4}$, and the answer is "
                "$\\frac{24 - 7}{(1)(4)} = \\frac{17}{4}$ ✓",
                [
                    "Eq(expand(3*(x + 1) + 5*(x - 2)), 8*x - 7)",
                    "Eq(Rational(3,1) + Rational(5,4), Rational(17,4))",
                    "Eq(Rational(8*3 - 7, (3 - 2)*(3 + 1)), Rational(17,4))",
                ],
            ),
            problem(
                "im3-u2-l2-we4",
                "Subtract $\\dfrac{4}{x^2 - 9} - \\dfrac{1}{x + 3}$.",
                "**Factor to find the LCD.** $x^2 - 9 = (x - 3)(x + 3)$, and the second "
                "denominator $(x + 3)$ already divides it — so the LCD is $(x - 3)(x + 3)$, not "
                "the product of the two denominators."
                "**Rewrite the second fraction.** Multiply top and bottom by $(x - 3)$:"
                "$$\\frac{4}{(x-3)(x+3)} - \\frac{x - 3}{(x-3)(x+3)}$$"
                "**Subtract the numerators, keeping the minus across the whole thing.**"
                "$$\\frac{4 - (x - 3)}{(x-3)(x+3)} = \\frac{7 - x}{(x-3)(x+3)}$$"
                "**Restrictions.** $x \\ne 3$ and $x \\ne -3$."
                "**Check with a number.** At $x = 0$ the original is $\\frac{4}{-9} - \\frac{1}{3} = "
                "-\\frac{4}{9} - \\frac{3}{9} = -\\frac{7}{9}$, and the answer is "
                "$\\frac{7}{(-3)(3)} = -\\frac{7}{9}$ ✓",
                [
                    "Eq(expand(4 - (x - 3)), 7 - x)",
                    "Eq(Rational(4, -9) - Rational(1, 3), Rational(-7, 9))",
                    "Eq(Rational(7 - 0, (0 - 3)*(0 + 3)), Rational(-7, 9))",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Cancelling a term instead of a factor.",
                "In (x + 2)/(x + 3) nothing cancels — the x's are TERMS. Cancelling is only "
                "legal when the whole numerator and whole denominator share a multiplied factor.",
            ),
            mistake(
                "Subtracting only the first term of the second numerator.",
                "The minus sign applies to the entire numerator: 4 - (x - 3) = 7 - x, not "
                "4 - x - 3 = 1 - x. Bracket it before you distribute.",
            ),
            mistake(
                "Dropping restrictions that the simplified form hides.",
                "If a factor cancels, its restriction still holds. The simplified expression is "
                "equal to the original only where the original was defined.",
            ),
            mistake(
                "Multiplying all denominators together every time.",
                "Legal but wasteful. Factoring first often reveals that one denominator already "
                "divides another, giving a much smaller LCD and far less simplifying afterwards.",
            ),
        ],
        try_it=[
            problem(
                "im3-u2-l2-t1",
                "Simplify $\\dfrac{x^2 + 5x + 6}{x^2 - 1} \\cdot \\dfrac{x - 1}{x + 2}$.",
                "Factoring: $x^2 + 5x + 6 = (x + 2)(x + 3)$ and $x^2 - 1 = (x - 1)(x + 1)$. The "
                "$(x + 2)$ and $(x - 1)$ cancel, leaving $\\frac{x + 3}{x + 1}$, with "
                "$x \\ne 1$, $x \\ne -1$ and $x \\ne -2$.",
                [
                    "Eq(expand((x + 2)*(x + 3)), x**2 + 5*x + 6)",
                    "Eq(simplify(((x**2 + 5*x + 6)/(x**2 - 1))*((x - 1)/(x + 2)) - (x + 3)/(x + 1)), 0)",
                ],
            ),
            problem(
                "im3-u2-l2-t2",
                "Add $\\dfrac{2}{x} + \\dfrac{3}{x + 1}$.",
                "The LCD is $x(x + 1)$. Rewriting: "
                "$\\frac{2(x + 1) + 3x}{x(x+1)} = \\frac{5x + 2}{x(x+1)}$, with $x \\ne 0$ and "
                "$x \\ne -1$. Check at $x = 1$: $2 + \\frac{3}{2} = \\frac{7}{2}$ and "
                "$\\frac{7}{2} $ ✓",
                [
                    "Eq(expand(2*(x + 1) + 3*x), 5*x + 2),",
                    "Eq(Rational(2,1) + Rational(3,2), Rational(7,2))",
                    "Eq(Rational(5*1 + 2, 1*(1 + 1)), Rational(7,2))",
                ],
            ),
            problem(
                "im3-u2-l2-t3",
                "Simplify $\\dfrac{x + 5}{x^2 - 4} \\div \\dfrac{x + 5}{x - 2}$.",
                "Flip and multiply: $\\frac{x + 5}{(x-2)(x+2)} \\cdot \\frac{x - 2}{x + 5}$. The "
                "$(x + 5)$ and $(x - 2)$ cancel, leaving $\\frac{1}{x + 2}$, with $x \\ne 2$, "
                "$x \\ne -2$ and $x \\ne -5$ (the last because we divided by an expression whose "
                "numerator is $x + 5$).",
                [
                    "Eq(expand((x - 2)*(x + 2)), x**2 - 4)",
                    "Eq(simplify(((x + 5)/(x**2 - 4))/((x + 5)/(x - 2)) - 1/(x + 2)), 0)",
                ],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "Fractions, grown up", "body": "Rational expressions behave exactly like fractions of integers, because they are built the same way. Multiply tops and bottoms; divide by flipping; add over a common denominator. The one discipline that makes all three legal: factor FIRST, because cancelling is only ever allowed on factors.", "beats": ["Multiply → cancel factors", "Divide → flip, then multiply", "Add → build the LCD from factors"]},
            {"kind": "worked", "title": "Multiply, then cancel factors", "problemId": "im3-u2-l2-we1"},
            
            tap(
                "Factors, not terms",
                "What does $\\dfrac{x^2 + 3x}{x}$ simplify to?",
                ["$x + 3$", "$x^2 + 3$", "$3x$", "it does not simplify"],
                0,
                "Factor the numerator first: $x^2 + 3x = x(x + 3)$, and now the $x$ is a genuine "
                "FACTOR that cancels, giving $x + 3$ for $x \\ne 0$. Cancelling the $x$ out of "
                "the un-factored form would be cancelling a term, which is not legal.",
                [
                    "Eq(expand(x*(x + 3)), x**2 + 3*x)",
                    "Eq(simplify((x**2 + 3*x)/x - (x + 3)), 0)",
                ],
            ),
            {"kind": "worked", "title": "Division is multiplication by the reciprocal", "problemId": "im3-u2-l2-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Cancel factors, never terms", "body": "In $\\frac{x + 3}{x^2 + 3}$ nothing cancels: the $3$s are TERMS, glued on by addition. Only a factor — something multiplying the whole top and the whole bottom — can be struck out."},
            tap(
                "Choosing the LCD",
                "What is the least common denominator of $\\dfrac{1}{x^2 - x}$ and "
                "$\\dfrac{1}{x - 1}$?",
                ["$x(x - 1)$", "$x(x-1)^2$", "$x^2 - x - 1$", "$(x^2 - x)(x - 1)$"],
                0,
                "Factor: $x^2 - x = x(x - 1)$, which already CONTAINS the second denominator. So "
                "the LCD is just $x(x - 1)$ — multiplying the two denominators together would "
                "give an unnecessary extra $(x - 1)$ to cancel later.",
                [
                    "Eq(expand(x*(x - 1)), x**2 - x)",
                ],
            ),
            {"kind": "worked", "title": "Adding over the least common denominator", "problemId": "im3-u2-l2-we3"},
            {"kind": "worked", "title": "Subtraction distributes over the whole numerator", "problemId": "im3-u2-l2-we4"},
            {"kind": "teach", "title": "The LCD is built from factors, not products", "body": "Factor every denominator, then take each distinct factor at its greatest power. Multiplying all the denominators together always works but bloats the algebra — the LEAST common denominator keeps the numerators small and the restrictions readable.", "beats": ["Factor each denominator", "Each factor once, at its highest power", "Restrictions come from every factor you used"]},
            {"kind": "tryIt", "title": "Multiply and simplify", "problemId": "im3-u2-l2-t1"},
            {"kind": "tryIt", "title": "Add with an LCD", "problemId": "im3-u2-l2-t2"},
            tap(
                "The subtraction trap",
                "Simplify the numerator of $\\dfrac{5}{x-1} - \\dfrac{x+2}{x-1}$.",
                ["$3 - x$", "$x + 7$", "$7 - x$", "$3 + x$"],
                0,
                "The denominators already match, so subtract the whole numerator: "
                "$5 - (x + 2) = 5 - x - 2 = 3 - x$. Forgetting to distribute the minus across "
                "the $+2$ would give $7 - x$.",
                [
                    "Eq(expand(5 - (x + 2)), 3 - x)",
                ],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["Factor first, every time", "Cancelling is legal only on factors", "Divide = multiply by the reciprocal; the flipped numerator adds a restriction", "LCD: each distinct factor at its greatest power", "When subtracting, the minus applies to the WHOLE second numerator"]},
        ],
    )


# ===========================================================================
# Lesson 3 — A-REI.2: rational equations and where extraneous roots come from
# ===========================================================================

def lesson_rational_equations():
    return lesson(
        slug="solving-rational-equations",
        title="Rational Equations & Extraneous Solutions",
        concrete=(
            "Two taps fill a tank in $3$ and $6$ hours. Together they fill $\\frac{1}{3} + "
            "\\frac{1}{6} = \\frac{1}{2}$ of it per hour, so the job takes $2$ hours. The "
            "equation that models this has the unknown in a denominator — and the first move, "
            "clearing the denominators, is the move that can manufacture a false answer."
        ),
        objective=(
            "Solve rational equations by clearing denominators, and identify which candidate "
            "solutions are extraneous and why."
        ),
        concept=[
            "To solve an equation with fractions, multiply both sides by the LCD. Every "
            "denominator cancels and what is left is a polynomial equation you already know how "
            "to solve.",

            "But multiplying by the LCD is not a reversible step. The LCD contains the variable, "
            "so it may be ZERO for some $x$ — and multiplying an equation by zero turns a false "
            "statement into a true one. That is the whole mechanism: the polynomial equation you "
            "end up with can have roots the original never had.",

            "Such a root is EXTRANEOUS. It is not an arithmetic mistake and you cannot avoid it "
            "by being careful; it is a consequence of the method. The only defence is to check "
            "each candidate against the ORIGINAL equation's domain and discard any that makes a "
            "denominator zero.",

            "This also tells you where to look. The extraneous candidates, if any, are exactly "
            "the excluded values — so before solving, note which $x$ are forbidden, and then "
            "any candidate matching one of them is thrown out on sight.",
        ],
        key_idea=(
            "Clearing denominators can only ADD candidate solutions, never lose them. So every "
            "candidate must be checked against the original domain — the check is part of the "
            "method, not a formality."
        ),
        facts=[
            fact("The method", "\\text{multiply both sides by the LCD}",
                 "Every denominator cancels, leaving a polynomial equation."),
            fact("Why extras appear", "\\text{LCD} = 0 \\text{ for some } x",
                 "Multiplying by something that can be zero is not reversible."),
            fact("Excluded values", "\\text{zeros of any denominator}",
                 "Note them BEFORE solving; extraneous roots can only be among them."),
            fact("The check", "\\text{substitute into the ORIGINAL}",
                 "Never into the cleared version — that is the equation that gained the extras."),
        ],
        worked=[
            problem(
                "im3-u2-l3-we1",
                "Solve $\\dfrac{1}{x} + \\dfrac{1}{2} = \\dfrac{3}{4}$.",
                "**Note the exclusion.** $x \\ne 0$."
                "**Multiply by the LCD.** Using $4x$:"
                "$$4 + 2x = 3x$$"
                "**Solve.** $4 = x$, so $x = 4$."
                "**Check against the original.** $\\frac{1}{4} + \\frac{1}{2} = \\frac{1}{4} + "
                "\\frac{2}{4} = \\frac{3}{4}$ ✓ and $4 \\ne 0$, so the solution stands."
                "**Why nothing went wrong here.** The only excluded value was $0$, and $0$ never "
                "appeared as a candidate — so this equation had no opportunity to produce an "
                "extraneous root.",
                [
                    "Eq(Rational(1,4) + Rational(1,2), Rational(3,4))",
                    "Eq(4 + 2*4, 3*4)",
                ],
            ),
            problem(
                "im3-u2-l3-we2",
                "Solve $\\dfrac{x}{x - 3} = \\dfrac{3}{x - 3} + 2$.",
                "**Note the exclusion.** The denominator vanishes at $x = 3$, so $x \\ne 3$ — "
                "write it down now, because it is about to matter."
                "**Multiply by the LCD.** Using $(x - 3)$:"
                "$$x = 3 + 2(x - 3)$$"
                "**Solve.** $x = 3 + 2x - 6$, so $x = 2x - 3$, giving $x = 3$."
                "**Check against the original.** $x = 3$ makes BOTH denominators zero — the "
                "expression is undefined there. So this candidate is EXTRANEOUS and must be "
                "rejected."
                "**Conclusion.** The equation has NO solution. And notice the mechanism plainly: "
                "the step that multiplied by $(x - 3)$ multiplied by zero at exactly $x = 3$, "
                "which is why a value that solves nothing came out of the algebra.",
                [
                    "Eq(3, 3 + 2*(3 - 3))",
                    "Eq(3 - 3, 0)",
                ],
            ),
            problem(
                "im3-u2-l3-we3",
                "Solve $\\dfrac{2}{x - 1} + \\dfrac{1}{x + 1} = \\dfrac{4}{x^2 - 1}$.",
                "**Factor and note exclusions.** $x^2 - 1 = (x - 1)(x + 1)$, so $x \\ne 1$ and "
                "$x \\ne -1$, and the LCD is $(x - 1)(x + 1)$."
                "**Multiply through.**"
                "$$2(x + 1) + 1(x - 1) = 4$$"
                "**Solve.** $2x + 2 + x - 1 = 4$, so $3x + 1 = 4$ and $x = 1$."
                "**Check.** $x = 1$ is an EXCLUDED value — it makes $x - 1$ and $x^2 - 1$ zero. "
                "Rejected."
                "**Conclusion.** No solution. The candidate landed exactly on a forbidden value, "
                "which is the only place an extraneous root can ever land.",
                [
                    "Eq(expand(2*(x + 1) + (x - 1)), 3*x + 1)",
                    "Eq(3*1 + 1, 4)",
                    "Eq(1**2 - 1, 0)",
                ],
            ),
            problem(
                "im3-u2-l3-we4",
                "Two pipes fill a tank in $4$ and $12$ hours. How long do they take together?",
                "**Set up rates.** In one hour the first fills $\\frac{1}{4}$ of the tank and "
                "the second $\\frac{1}{12}$. Together they fill $\\frac{1}{t}$ per hour, where "
                "$t$ is the time for the whole job:"
                "$$\\frac{1}{4} + \\frac{1}{12} = \\frac{1}{t}$$"
                "**Note the exclusion.** $t \\ne 0$ — which is physically obvious too."
                "**Add the left side.** $\\frac{3}{12} + \\frac{1}{12} = \\frac{4}{12} = "
                "\\frac{1}{3}$."
                "**Solve.** $\\frac{1}{3} = \\frac{1}{t}$ gives $t = 3$ hours."
                "**Judge the answer.** $3$ hours is less than either pipe alone, which is the "
                "sanity check this kind of problem always deserves — two taps must beat one.",
                [
                    "Eq(Rational(1,4) + Rational(1,12), Rational(1,3))",
                    "Eq(Rational(1,3), Rational(1,3))",
                    "3 < 4",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Checking the candidate in the cleared equation instead of the original.",
                "The cleared equation is the one that GAINED the extra root, so it will happily "
                "confirm it. Substitute into the original.",
            ),
            mistake(
                "Concluding 'no solution' means an error was made.",
                "No solution is a legitimate answer. If every candidate is excluded, the "
                "equation genuinely has none.",
            ),
            mistake(
                "Adding the times instead of the rates in a work problem.",
                "Two pipes taking 4 and 12 hours do not take 16, or 8. RATES add: 1/4 + 1/12 "
                "per hour. The answer must come out smaller than the faster pipe alone.",
            ),
            mistake(
                "Forgetting to factor before finding the LCD.",
                "x² - 1 hides the factors (x - 1)(x + 1). Without factoring you miss both the "
                "correct LCD and the exclusion at x = -1.",
            ),
        ],
        try_it=[
            problem(
                "im3-u2-l3-t1",
                "Solve $\\dfrac{6}{x} = \\dfrac{2}{x} + 1$.",
                "Exclusion: $x \\ne 0$. Multiplying by $x$: $6 = 2 + x$, so $x = 4$. Checking in "
                "the original: $\\frac{6}{4} = \\frac{3}{2}$ and $\\frac{2}{4} + 1 = "
                "\\frac{1}{2} + 1 = \\frac{3}{2}$ ✓ Since $4 \\ne 0$, the solution is $x = 4$.",
                [
                    "Eq(6, 2 + 4)",
                    "Eq(Rational(6,4), Rational(3,2))",
                    "Eq(Rational(2,4) + 1, Rational(3,2))",
                ],
            ),
            problem(
                "im3-u2-l3-t2",
                "Solve $\\dfrac{x}{x - 5} = \\dfrac{5}{x - 5}$ and say what happens.",
                "Exclusion: $x \\ne 5$. Multiplying by $(x - 5)$ gives $x = 5$ — which is "
                "precisely the excluded value. It is extraneous, so the equation has NO "
                "solution. The two sides can never be equal, because equality would require the "
                "very value that makes them undefined.",
                [
                    "Eq(5 - 5, 0)",
                    "Eq(5, 5)",
                ],
            ),
            problem(
                "im3-u2-l3-t3",
                "One worker paints a room in $6$ hours, another in $3$ hours. Together?",
                "Rates add: $\\frac{1}{6} + \\frac{1}{3} = \\frac{1}{6} + \\frac{2}{6} = "
                "\\frac{3}{6} = \\frac{1}{2}$ of the room per hour, so the job takes $2$ hours. "
                "That is less than the faster worker's $3$ hours, as it must be.",
                [
                    "Eq(Rational(1,6) + Rational(1,3), Rational(1,2))",
                    "2 < 3",
                ],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "Clear the denominators — carefully", "body": "Multiply both sides by the LCD and every fraction disappears, leaving a polynomial equation you already know how to solve. But the LCD contains the variable, so for some $x$ you just multiplied the equation by ZERO — and that step can quietly invent solutions.", "beats": ["Multiply through by the LCD", "Solve the polynomial that remains", "Then check every candidate"]},
            {"kind": "worked", "title": "A clean clearing, no surprises", "problemId": "im3-u2-l3-we1"},
            
            tap(
                "Spot the exclusion first",
                "Before solving $\\dfrac{4}{x - 2} = \\dfrac{x}{x - 2}$, which value is "
                "forbidden?",
                ["$x = 2$", "$x = 4$", "$x = 0$", "none"],
                0,
                "The denominator $x - 2$ vanishes at $x = 2$, so $x = 2$ is excluded. Noting "
                "this BEFORE solving means you will recognise an extraneous candidate the "
                "moment it appears.",
                ["Eq(2 - 2, 0)"],
            ),
            {"kind": "worked", "title": "The candidate that betrays you", "problemId": "im3-u2-l3-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Check in the ORIGINAL equation", "body": "A candidate can satisfy the cleared equation perfectly and still be illegal in the original — that is what extraneous means. The check is against the original denominators, and it is part of the method, not a courtesy."},
            tap(
                "Is it extraneous?",
                "Clearing denominators in $\\dfrac{x}{x-4} = \\dfrac{4}{x-4}$ gives $x = 4$. "
                "What is the solution set?",
                ["empty — $x = 4$ is extraneous", "$x = 4$", "all real numbers",
                 "$x = 0$"],
                0,
                "$x = 4$ makes the denominator zero, so it is not in the domain of the original "
                "equation. It is extraneous, and the solution set is empty.",
                ["Eq(4 - 4, 0)"],
            ),
            {"kind": "worked", "title": "Two fractions, one factored LCD", "problemId": "im3-u2-l3-we3"},
            {"kind": "worked", "title": "Work problems: rates add, times don't", "problemId": "im3-u2-l3-we4"},
            {"kind": "teach", "title": "Extraneous roots are a feature of the method", "body": "You cannot avoid them by being careful; multiplying by something that can be zero is simply not reversible. The upside: candidates can only go wrong at the EXCLUDED values, so note those before you start and the check takes seconds.", "beats": ["Excluded values first", "Candidates equal to an excluded value die", "'No solution' can be the right answer"]},
            {"kind": "tryIt", "title": "Clear and solve", "problemId": "im3-u2-l3-t1"},
            {"kind": "tryIt", "title": "Spot the extraneous root", "problemId": "im3-u2-l3-t2"},
            tap(
                "Rates, not times",
                "A tap fills a tank in $2$ hours, another in $6$. How long together?",
                ["$1.5$ hours", "$4$ hours", "$8$ hours", "$3$ hours"],
                0,
                "Rates add: $\\frac{1}{2} + \\frac{1}{6} = \\frac{3}{6} + \\frac{1}{6} = "
                "\\frac{4}{6} = \\frac{2}{3}$ of the tank per hour, so the time is "
                "$\\frac{3}{2} = 1.5$ hours — faster than either alone, as it must be.",
                [
                    "Eq(Rational(1,2) + Rational(1,6), Rational(2,3))",
                    "Eq(Rational(1, Rational(2,3)), Rational(3,2))",
                    "Rational(3,2) < 2",
                ],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["Multiply both sides by the LCD to clear every fraction", "Clearing can ADD candidates, never lose them", "Check candidates against the ORIGINAL equation's domain", "The bad candidates are exactly the excluded values", "In work problems, add the RATES, then invert"]},
        ],
    )


# ===========================================================================
# Lesson 4 — A-REI.2: radical functions and squaring as the same hazard
# ===========================================================================

def lesson_radical():
    return lesson(
        slug="radical-functions-and-equations",
        title="Radical Functions & Radical Equations",
        concrete=(
            "A square of area $A$ has side $\\sqrt{A}$. Areas cannot be negative, so the input "
            "is restricted; and sides cannot be negative, so the output is restricted too. Both "
            "halves of the graph's shape are already decided by that sentence."
        ),
        objective=(
            "State the domain and range of a square-root function, solve radical equations by "
            "squaring, and reject the extraneous roots squaring creates."
        ),
        concept=[
            "$\\sqrt{x}$ is only defined for $x \\ge 0$, and it returns the NON-NEGATIVE root. "
            "So $y = \\sqrt{x}$ has domain $x \\ge 0$ and range $y \\ge 0$: a half-parabola "
            "lying on its side, starting at the origin.",

            "Shifting works exactly as it did for parabolas. In $y = \\sqrt{x - h} + k$, the "
            "expression under the root must be non-negative, which gives domain $x \\ge h$, and "
            "the output starts at $k$, giving range $y \\ge k$.",

            "To solve a radical equation, isolate the radical and square both sides. And here "
            "the same hazard returns in a new costume: squaring is not reversible. "
            "$a = b$ implies $a^2 = b^2$, but $a^2 = b^2$ only implies $a = \\pm b$ — so "
            "squaring can introduce roots that solve the squared equation and not the original.",

            "That is the unit's whole point, seen twice. Multiplying by a denominator that might "
            "be zero, and squaring away a sign — both are one-way steps that can only ADD "
            "candidates. In both cases the fix is identical: substitute every candidate back "
            "into the original and keep only what survives.",
        ],
        key_idea=(
            "Squaring, like clearing denominators, is a one-way step. It never loses a solution "
            "and it may invent one, so checking in the original equation is compulsory."
        ),
        facts=[
            fact("Domain", "\\sqrt{u} \\text{ needs } u \\ge 0",
                 "Set the whole expression under the root to be non-negative and solve."),
            fact("Range", "\\sqrt{x} \\ge 0",
                 "The radical sign means the non-negative root, so the output never goes below."),
            fact("Shifted root", "y = \\sqrt{x - h} + k",
                 "Domain x ≥ h, range y ≥ k — the starting corner sits at (h, k)."),
            fact("Squaring is one-way", "a = b \\Rightarrow a^2 = b^2",
                 "The converse fails, which is exactly where extraneous roots come from."),
            fact("A negative equals nothing", "\\sqrt{u} = c < 0 \\Rightarrow \\text{no solution}",
                 "You can see this before any algebra — a non-negative thing is never negative."),
        ],
        worked=[
            problem(
                "im3-u2-l4-we1",
                "State the domain and range of $f(x) = \\sqrt{x - 4} + 1$.",
                "**Domain.** The expression under the root must be non-negative: "
                "$x - 4 \\ge 0$, so $x \\ge 4$."
                "**Range.** $\\sqrt{x - 4}$ is at least $0$, so $f(x)$ is at least $0 + 1 = 1$: "
                "$y \\ge 1$."
                "**The corner.** The graph starts at $(4,\\ 1)$ and rises to the right, ever "
                "more slowly."
                "**Spot-check.** At $x = 8$, $f(8) = \\sqrt{4} + 1 = 3$ — inside the domain and "
                "above the minimum, as expected.",
                [
                    "Eq(sqrt(8 - 4) + 1, 3)",
                    "Eq(sqrt(4 - 4) + 1, 1)",
                ],
            ),
            problem(
                "im3-u2-l4-we2",
                "Solve $\\sqrt{2x + 3} = 5$.",
                "**The radical is already isolated.** Square both sides:"
                "$$2x + 3 = 25$$"
                "**Solve.** $2x = 22$, so $x = 11$."
                "**Check in the original.** $\\sqrt{2(11) + 3} = \\sqrt{25} = 5$ ✓"
                "**Why this one was safe.** The right side, $5$, is non-negative — so the "
                "squared equation and the original agree, and no extraneous root could appear.",
                [
                    "Eq(2*11 + 3, 25)",
                    "Eq(sqrt(2*11 + 3), 5)",
                ],
            ),
            problem(
                "im3-u2-l4-we3",
                "Solve $\\sqrt{x + 6} = x$.",
                "**Square both sides.**"
                "$$x + 6 = x^2$$"
                "**Rearrange and factor.** $x^2 - x - 6 = 0$, so $(x - 3)(x + 2) = 0$ and the "
                "candidates are $x = 3$ and $x = -2$."
                "**Check the first candidate.** At $x = 3$, $\\sqrt{3 + 6} = \\sqrt{9} = 3$ ✓"
                "**Check the second candidate.** At $x = -2$, $\\sqrt{-2 + 6} = \\sqrt{4} = 2$, but the right side is "
                "$-2$. Since $2 \\ne -2$, this candidate FAILS."
                "**Conclusion.** Only $x = 3$."
                "**Where the extra came from.** Squaring destroyed the sign: $2$ and $-2$ have "
                "the same square, so $x = -2$ solves the squared equation while making the "
                "original demand that a non-negative root equal a negative number.",
                [
                    "Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
                    "Eq(sqrt(3 + 6), 3)",
                    "Eq(sqrt(-2 + 6), 2)",
                    "Ne(2, -2)",
                ],
            ),
            problem(
                "im3-u2-l4-we4",
                "Solve $\\sqrt{3x + 1} + 5 = 2$.",
                "**Isolate the radical.** Subtract $5$:"
                "$$\\sqrt{3x + 1} = -3$$"
                "**Stop and read it.** A square root is never negative, so no $x$ can satisfy "
                "this. The equation has NO solution — and this is visible before any squaring."
                "**What squaring would have done.** Squaring gives $3x + 1 = 9$, so $x = "
                "\\frac{8}{3}$; substituting back gives $\\sqrt{9} + 5 = 8 \\ne 2$. The "
                "candidate is extraneous, which confirms the conclusion the long way round.",
                [
                    "Eq(3*Rational(8,3) + 1, 9)",
                    "Eq(sqrt(9) + 5, 8)",
                    "Ne(8, 2)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Squaring before isolating the radical.",
                "Squaring √(x+1) + 3 gives x + 1 + 6√(x+1) + 9 — the radical survives and the "
                "equation is worse. Isolate it on one side first.",
            ),
            mistake(
                "Treating √(a + b) as √a + √b.",
                "It is not. √(9 + 16) = 5, while √9 + √16 = 7. Roots do not distribute over "
                "addition — only over multiplication.",
            ),
            mistake(
                "Keeping every candidate the squared equation produces.",
                "Squaring can only add candidates. Substitute each back into the ORIGINAL and "
                "discard those that fail.",
            ),
            mistake(
                "Missing that √u = (negative) has no solution.",
                "The radical is non-negative by definition, so an isolated radical equal to a "
                "negative number ends the problem immediately.",
            ),
        ],
        try_it=[
            problem(
                "im3-u2-l4-t1",
                "State the domain of $g(x) = \\sqrt{7 - x}$.",
                "The expression under the root must be non-negative: $7 - x \\ge 0$, so "
                "$x \\le 7$. Note the inequality flips when $x$ is moved across — the domain "
                "runs to the LEFT here, unlike $\\sqrt{x - 7}$.",
                [
                    "Eq(sqrt(7 - 7), 0)",
                    "Eq(sqrt(7 - 3), 2)",
                ],
            ),
            problem(
                "im3-u2-l4-t2",
                "Solve $\\sqrt{5x - 1} = 3$.",
                "Squaring: $5x - 1 = 9$, so $5x = 10$ and $x = 2$. Check: "
                "$\\sqrt{5(2) - 1} = \\sqrt{9} = 3$ ✓ The right side was non-negative, so no "
                "extraneous root was possible.",
                [
                    "Eq(5*2 - 1, 9)",
                    "Eq(sqrt(5*2 - 1), 3)",
                ],
            ),
            problem(
                "im3-u2-l4-t3",
                "Solve $\\sqrt{x + 12} = x$ and identify any extraneous root.",
                "Squaring: $x + 12 = x^2$, so $x^2 - x - 12 = 0$ and $(x - 4)(x + 3) = 0$, "
                "giving candidates $4$ and $-3$. Checking $x = 4$: $\\sqrt{16} = 4$ ✓ Checking "
                "$x = -3$: $\\sqrt{9} = 3 \\ne -3$, so $-3$ is EXTRANEOUS. The solution is "
                "$x = 4$ only.",
                [
                    "Eq(expand((x - 4)*(x + 3)), x**2 - x - 12)",
                    "Eq(sqrt(4 + 12), 4)",
                    "Eq(sqrt(-3 + 12), 3)",
                    "Ne(3, -3)",
                ],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "Half a parabola, on its side", "body": "$\\sqrt{x}$ is defined only for $x \\ge 0$ and returns only the non-negative root — so its graph is a half-parabola lying on its side. Shifts work exactly as they did for parabolas: in $y = \\sqrt{x - h} + k$ the domain starts where the inside turns non-negative, at $x = h$.", "beats": ["Domain: inside $\\ge 0$", "Range: outputs from $k$ up", "Shifts move the endpoint $(h, k)$"]},
            {"kind": "worked", "title": "Domain and range from the shift", "problemId": "im3-u2-l4-we1"},
            
            tap(
                "Reading the domain",
                "What is the domain of $\\sqrt{x + 5}$?",
                ["$x \\ge -5$", "$x \\ge 5$", "$x \\le -5$", "all real numbers"],
                0,
                "The inside must be non-negative: $x + 5 \\ge 0$, so $x \\ge -5$. The graph "
                "starts at $(-5,\\ 0)$ and rises to the right.",
                ["Eq(sqrt(-5 + 5), 0)", "Eq(sqrt(4 + 5), 3)"],
            ),
            {"kind": "worked", "title": "Isolate, square, solve", "problemId": "im3-u2-l4-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Isolate the radical BEFORE squaring", "body": "Squaring $\\sqrt{2x + 3} + 1$ as it stands creates a cross-term that still contains the root — you gain nothing. Move everything else to the other side first, THEN square: one clean step, radical gone."},
            tap(
                "Before you square",
                "How many solutions does $\\sqrt{x - 1} = -4$ have?",
                ["none", "one", "two", "infinitely many"],
                0,
                "A square root is never negative, so it can never equal $-4$. No solution — and "
                "you can say so without squaring anything. Squaring would produce the candidate "
                "$x = 17$, which then fails the check.",
                ["Eq(sqrt(17 - 1), 4)", "Ne(4, -4)"],
            ),
            {"kind": "worked", "title": "Squaring invents a candidate", "problemId": "im3-u2-l4-we3"},
            {"kind": "worked", "title": "When the radical can't reach", "problemId": "im3-u2-l4-we4"},
            {"kind": "teach", "title": "Squaring is a one-way street", "body": "$a = b$ implies $a^2 = b^2$, but not the reverse: $-3 \\ne 3$ while their squares agree. So squaring can only ADD candidates — the same asymmetry as clearing denominators, wearing a new costume. A square root can never equal a negative number, and no amount of algebra changes that.", "beats": ["Squaring never loses a solution", "It may invent one", "$\\sqrt{u} = $ negative has NO solution"]},
            {"kind": "tryIt", "title": "Read the domain", "problemId": "im3-u2-l4-t1"},
            {"kind": "tryIt", "title": "Solve a radical equation", "problemId": "im3-u2-l4-t2"},
            tap(
                "Which candidate survives",
                "Squaring $\\sqrt{x + 20} = x$ gives candidates $x = 5$ and $x = -4$. Which "
                "solve the ORIGINAL?",
                ["only $x = 5$", "only $x = -4$", "both", "neither"],
                0,
                "$\\sqrt{5 + 20} = \\sqrt{25} = 5$ ✓ But $\\sqrt{-4 + 20} = \\sqrt{16} = 4$, "
                "which is not $-4$. Squaring lost the sign, inventing the second candidate.",
                [
                    "Eq(expand((x - 5)*(x + 4)), x**2 - x - 20)",
                    "Eq(sqrt(5 + 20), 5)",
                    "Eq(sqrt(-4 + 20), 4)",
                    "Ne(4, -4)",
                ],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["$y = \\sqrt{x - h} + k$: domain $x \\ge h$, range $y \\ge k$", "Isolate the radical, then square both sides", "Squaring can only add candidates — check in the original", "$\\sqrt{u}$ is never negative, so $\\sqrt{u} = -3$ has no solution", "Same lesson as rational equations: one-way steps demand a check"]},
        ],
    )


# ===========================================================================
# Practice & test banks
# ===========================================================================

def practice_bank():
    return [
        problem(
            "im3-u2-p1",
            "State the domain of $\\dfrac{x + 2}{x^2 - 25}$.",
            "$x^2 - 25 = (x - 5)(x + 5)$ vanishes at $x = 5$ and $x = -5$, so the domain is "
            "every real number except those two.",
            ["Eq(expand((x - 5)*(x + 5)), x**2 - 25)"],
        ),
        problem(
            "im3-u2-p2",
            "Does $\\dfrac{x^2 - 16}{x - 4}$ have a hole or a vertical asymptote at $x = 4$?",
            "$x^2 - 16 = (x - 4)(x + 4)$, so the factor cancels: a HOLE at $x = 4$, at height "
            "$4 + 4 = 8$.",
            ["Eq(expand((x - 4)*(x + 4)), x**2 - 16)", "Eq(4 + 4, 8)"],
        ),
        problem(
            "im3-u2-p3",
            "Find the horizontal asymptote of $\\dfrac{5x^3 + 1}{2x^3 - x}$.",
            "The degrees tie at $3$, so the leading coefficients give $y = \\frac{5}{2}$.",
            ["Eq(Rational(5,2), Rational(5,2))"],
        ),
        problem(
            "im3-u2-p4",
            "Find the horizontal asymptote of $\\dfrac{x + 4}{x^3 - 2}$.",
            "The denominator has the higher degree, so the ratio is squeezed to zero: $y = 0$.",
            ["3 > 1"],
        ),
        problem(
            "im3-u2-p5",
            "Simplify $\\dfrac{x^2 - x - 6}{x^2 - 9}$ and state the restrictions.",
            "$x^2 - x - 6 = (x - 3)(x + 2)$ and $x^2 - 9 = (x - 3)(x + 3)$, so the result is "
            "$\\frac{x + 2}{x + 3}$ with $x \\ne 3$ and $x \\ne -3$.",
            [
                "Eq(expand((x - 3)*(x + 2)), x**2 - x - 6)",
                "Eq(simplify((x**2 - x - 6)/(x**2 - 9) - (x + 2)/(x + 3)), 0)",
            ],
        ),
        problem(
            "im3-u2-p6",
            "Multiply $\\dfrac{x + 1}{x - 5} \\cdot \\dfrac{x^2 - 25}{x^2 - 1}$.",
            "Factoring gives $\\frac{x+1}{x-5} \\cdot \\frac{(x-5)(x+5)}{(x-1)(x+1)}$; the "
            "$(x - 5)$ and $(x + 1)$ cancel, leaving $\\frac{x + 5}{x - 1}$.",
            [
                "Eq(simplify(((x + 1)/(x - 5))*((x**2 - 25)/(x**2 - 1)) - (x + 5)/(x - 1)), 0)",
            ],
        ),
        problem(
            "im3-u2-p7",
            "Add $\\dfrac{1}{x - 3} + \\dfrac{2}{x + 2}$.",
            "The LCD is $(x-3)(x+2)$: $\\frac{(x + 2) + 2(x - 3)}{(x-3)(x+2)} = "
            "\\frac{3x - 4}{(x-3)(x+2)}$, with $x \\ne 3$ and $x \\ne -2$.",
            ["Eq(expand((x + 2) + 2*(x - 3)), 3*x - 4)"],
        ),
        problem(
            "im3-u2-p8",
            "Subtract $\\dfrac{5}{x + 1} - \\dfrac{3}{x - 1}$.",
            "LCD $(x+1)(x-1)$: $\\frac{5(x - 1) - 3(x + 1)}{(x+1)(x-1)} = "
            "\\frac{2x - 8}{(x+1)(x-1)}$. Distribute the minus across BOTH terms of $3(x+1)$.",
            ["Eq(expand(5*(x - 1) - 3*(x + 1)), 2*x - 8)"],
        ),
        problem(
            "im3-u2-p9",
            "Solve $\\dfrac{2}{x} + \\dfrac{1}{3} = 1$.",
            "Exclusion $x \\ne 0$. Multiply by $3x$: $6 + x = 3x$, so $6 = 2x$ and $x = 3$. "
            "Check: $\\frac{2}{3} + \\frac{1}{3} = 1$ ✓",
            ["Eq(6 + 3, 3*3)", "Eq(Rational(2,3) + Rational(1,3), 1)"],
        ),
        problem(
            "im3-u2-p10",
            "Solve $\\dfrac{x}{x - 6} = \\dfrac{6}{x - 6} + 1$ and say what happens.",
            "Exclusion $x \\ne 6$. Multiplying by $(x-6)$: $x = 6 + (x - 6) = x$, which is true "
            "for EVERY $x$. So every value in the domain works: the solution is all real "
            "numbers except $6$.",
            ["Eq(6 + (10 - 6), 10)", "Eq(Rational(10, 10 - 6), Rational(6, 10 - 6) + 1)"],
        ),
        problem(
            "im3-u2-p11",
            "Solve $\\dfrac{3}{x - 2} = \\dfrac{x + 1}{x - 2}$.",
            "Exclusion $x \\ne 2$. Multiplying gives $3 = x + 1$, so $x = 2$ — the excluded "
            "value. Extraneous, so there is NO solution.",
            ["Eq(3, 2 + 1)", "Eq(2 - 2, 0)"],
        ),
        problem(
            "im3-u2-p12",
            "State the domain and range of $\\sqrt{x + 9} - 2$.",
            "Domain: $x + 9 \\ge 0$, so $x \\ge -9$. Range: the root is at least $0$, so the "
            "output is at least $-2$, i.e. $y \\ge -2$. The corner sits at $(-9,\\ -2)$.",
            ["Eq(sqrt(-9 + 9) - 2, -2)", "Eq(sqrt(7 + 9) - 2, 2)"],
        ),
        problem(
            "im3-u2-p13",
            "Solve $\\sqrt{4x - 3} = 7$.",
            "Squaring: $4x - 3 = 49$, so $4x = 52$ and $x = 13$. Check: "
            "$\\sqrt{52 - 3} = \\sqrt{49} = 7$ ✓",
            ["Eq(4*13 - 3, 49)", "Eq(sqrt(4*13 - 3), 7)"],
        ),
        problem(
            "im3-u2-p14",
            "Solve $\\sqrt{x + 2} = x$ and identify any extraneous root.",
            "Squaring: $x + 2 = x^2$, so $x^2 - x - 2 = 0$ and $(x - 2)(x + 1) = 0$. Candidates "
            "$2$ and $-1$. $\\sqrt{4} = 2$ ✓ but $\\sqrt{1} = 1 \\ne -1$, so $-1$ is "
            "extraneous. Solution: $x = 2$.",
            [
                "Eq(expand((x - 2)*(x + 1)), x**2 - x - 2)",
                "Eq(sqrt(2 + 2), 2)",
                "Eq(sqrt(-1 + 2), 1)",
                "Ne(1, -1)",
            ],
        ),
        problem(
            "im3-u2-p15",
            "Solve $\\sqrt{2x + 1} + 6 = 4$.",
            "Isolating: $\\sqrt{2x + 1} = -2$. A square root is never negative, so there is NO "
            "solution — no squaring required.",
            ["Eq(sqrt(4), 2)", "Ne(2, -2)"],
        ),
        problem(
            "im3-u2-p16",
            "Three taps fill a tank in $2$, $3$ and $6$ hours. How long do all three take?",
            "Rates add: $\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6} = \\frac{3+2+1}{6} = 1$ tank "
            "per hour, so together they take exactly $1$ hour — faster than the fastest tap "
            "alone, as required.",
            ["Eq(Rational(1,2) + Rational(1,3) + Rational(1,6), 1)", "1 < 2"],
        ),
    ]


def test_bank():
    return [
        problem(
            "im3-u2-x1",
            "Identify every hole and vertical asymptote of "
            "$\\dfrac{x^2 - x - 12}{x^2 - 8x + 16}$.",
            "$x^2 - x - 12 = (x - 4)(x + 3)$ and $x^2 - 8x + 16 = (x - 4)^2$. One $(x - 4)$ "
            "cancels, leaving $\\frac{x + 3}{x - 4}$ — so there is NO hole: a factor of "
            "$(x - 4)$ survives in the denominator and $x = 4$ is a vertical asymptote. "
            "(Cancelling once is not enough when the denominator carried it twice.)",
            [
                "Eq(expand((x - 4)*(x + 3)), x**2 - x - 12)",
                "Eq(expand((x - 4)**2), x**2 - 8*x + 16)",
                "Eq(simplify((x**2 - x - 12)/(x**2 - 8*x + 16) - (x + 3)/(x - 4)), 0)",
            ],
        ),
        problem(
            "im3-u2-x2",
            "Give the horizontal asymptote of each, with a reason: "
            "(a) $\\dfrac{6x^2}{3x^2 + 5}$, (b) $\\dfrac{x^2}{x^3 + 1}$, "
            "(c) $\\dfrac{x^4}{x^2 - 1}$.",
            "**(a)** Degrees tie at $2$, so the leading coefficients give $y = \\frac{6}{3} = 2$."
            "**(b)** The denominator's degree $3$ beats the numerator's $2$, so $y = 0$."
            "**(c)** The numerator's degree $4$ beats $2$, so there is NO horizontal asymptote "
            "— the values grow without bound.",
            ["Eq(Rational(6,3), 2)", "3 > 2", "4 > 2"],
        ),
        problem(
            "im3-u2-x3",
            "Simplify $\\dfrac{x^2 - 4x}{x^2 - 16} \\div \\dfrac{x}{x + 4}$ and state all "
            "restrictions.",
            "Flip and multiply: $\\frac{x(x - 4)}{(x-4)(x+4)} \\cdot \\frac{x + 4}{x}$. The "
            "$x$, the $(x - 4)$ and the $(x + 4)$ all cancel, leaving $1$. Restrictions: "
            "$x \\ne 4$, $x \\ne -4$ and $x \\ne 0$ — the last because we divided by "
            "$\\frac{x}{x+4}$, which is zero at $x = 0$. The answer is the constant $1$ "
            "everywhere those three values are avoided.",
            [
                "Eq(expand(x*(x - 4)), x**2 - 4*x)",
                "Eq(simplify(((x**2 - 4*x)/(x**2 - 16))/(x/(x + 4)) - 1), 0)",
            ],
        ),
        problem(
            "im3-u2-x4",
            "Combine $\\dfrac{3}{x^2 - 4} + \\dfrac{2}{x + 2}$ into a single fraction.",
            "$x^2 - 4 = (x-2)(x+2)$, and $(x + 2)$ already divides it, so the LCD is "
            "$(x-2)(x+2)$. Rewriting the second: $\\frac{2(x - 2)}{(x-2)(x+2)}$. Adding: "
            "$\\frac{3 + 2x - 4}{(x-2)(x+2)} = \\frac{2x - 1}{(x-2)(x+2)}$, with $x \\ne 2$ and "
            "$x \\ne -2$.",
            [
                "Eq(expand(3 + 2*(x - 2)), 2*x - 1)",
                "Eq(simplify(3/(x**2 - 4) + 2/(x + 2) - (2*x - 1)/((x - 2)*(x + 2))), 0)",
            ],
        ),
        problem(
            "im3-u2-x5",
            "Solve $\\dfrac{1}{x - 1} + \\dfrac{2}{x + 1} = \\dfrac{4}{x^2 - 1}$, checking "
            "every candidate.",
            "$x^2 - 1 = (x-1)(x+1)$, so exclusions are $x \\ne 1$ and $x \\ne -1$, and the LCD "
            "is $(x-1)(x+1)$. Multiplying through: $(x + 1) + 2(x - 1) = 4$, so $3x - 1 = 4$ "
            "and $x = \\frac{5}{3}$. Since $\\frac{5}{3}$ is neither $1$ nor $-1$, it is "
            "legitimate. Check: $\\frac{1}{2/3} + \\frac{2}{8/3} = \\frac{3}{2} + \\frac{3}{4} "
            "= \\frac{9}{4}$, and $\\frac{4}{25/9 - 1} = \\frac{4}{16/9} = \\frac{9}{4}$ ✓",
            [
                "Eq(expand((x + 1) + 2*(x - 1)), 3*x - 1)",
                "Eq(3*Rational(5,3) - 1, 4)",
                "Eq(Rational(1, Rational(5,3) - 1) + Rational(2, Rational(5,3) + 1), Rational(9,4))",
                "Eq(Rational(4, Rational(5,3)**2 - 1), Rational(9,4))",
            ],
        ),
        problem(
            "im3-u2-x6",
            "Solve $\\sqrt{x + 7} = x - 5$, checking every candidate.",
            "Squaring: $x + 7 = x^2 - 10x + 25$, so $x^2 - 11x + 18 = 0$ and "
            "$(x - 9)(x - 2) = 0$, giving candidates $9$ and $2$. Check $x = 9$: "
            "$\\sqrt{16} = 4$ and $9 - 5 = 4$ ✓ Check $x = 2$: $\\sqrt{9} = 3$ but "
            "$2 - 5 = -3$, and $3 \\ne -3$, so $2$ is EXTRANEOUS. The solution is $x = 9$. "
            "The right side had to be non-negative, which already ruled out any $x < 5$.",
            [
                "Eq(expand((x - 9)*(x - 2)), x**2 - 11*x + 18)",
                "Eq(sqrt(9 + 7), 4)",
                "Eq(9 - 5, 4)",
                "Eq(sqrt(2 + 7), 3)",
                "Ne(3, 2 - 5)",
            ],
        ),
        problem(
            "im3-u2-x7",
            "Explain, in terms of the method rather than arithmetic, why clearing denominators "
            "and squaring both require a check — and why neither can LOSE a solution.",
            "Both steps apply a non-reversible operation to the whole equation. Multiplying by "
            "the LCD multiplies by an expression that may be zero; squaring discards a sign. "
            "In each case any genuine solution still satisfies the new equation — so nothing is "
            "lost — but values that were never solutions can now satisfy it, so candidates can "
            "be GAINED. That asymmetry is why the check is one-directional: substitute each "
            "candidate into the ORIGINAL and discard failures, never the reverse. And it says "
            "where to look: for a rational equation the extraneous candidates can only be "
            "excluded values, and for a radical equation only values making the two sides "
            "opposite in sign.",
            ["Eq(3 - 3, 0)", "Eq((-2)**2, 2**2)", "Ne(-2, 2)"],
        ),
        problem(
            "im3-u2-x8",
            "A boat travels $12$ km upstream and $12$ km back in $5$ hours. In still water it "
            "does $5$ km/h. Find the current speed $c$.",
            "Upstream speed is $5 - c$ and downstream $5 + c$, so the times are "
            "$\\frac{12}{5-c}$ and $\\frac{12}{5+c}$, summing to $5$. Exclusions: $c \\ne 5$ "
            "and $c \\ne -5$. Multiplying by $(5-c)(5+c) = 25 - c^2$: "
            "$12(5 + c) + 12(5 - c) = 5(25 - c^2)$, so $120 = 125 - 5c^2$, giving $5c^2 = 5$ "
            "and $c^2 = 1$. So $c = 1$ or $c = -1$; a current speed is non-negative, so "
            "$c = 1$ km/h. Check: $\\frac{12}{4} + \\frac{12}{6} = 3 + 2 = 5$ ✓",
            [
                "Eq(expand(12*(5 + c) + 12*(5 - c)), 120)",
                "Eq(expand(5*(25 - c**2)), 125 - 5*c**2)",
                "Eq(Rational(12, 5 - 1) + Rational(12, 5 + 1), 5)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="rational-and-radical-functions",
        title="Rational & Radical Functions",
        unit_number=2,
        blurb=(
            "Domains, holes and asymptotes read off the factored form; the arithmetic of "
            "rational expressions; and the one idea that ties the unit together — clearing a "
            "denominator and squaring a radical are both one-way steps, so both can invent "
            "solutions that were never there."
        ),
        builds_on=(
            "Factoring from IM2 Unit 2 and the polynomial division of IM3 Unit 1 — a rational "
            "function is one polynomial over another, so everything here starts by factoring."
        ),
        lessons=[
            lesson_asymptotes(),
            lesson_operations(),
            lesson_rational_equations(),
            lesson_radical(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
