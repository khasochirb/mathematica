#!/usr/bin/env python3
"""IB Mathematics: Analysis & Approaches HL — Unit 1 (Topic 1: Number & Algebra, AHL).

Builds data/genmath/ib-hl/number-and-algebra.json: seven lessons, one per
official AHL subtopic code 1.10–1.16, pitched at HL depth — counting and the
extended binomial theorem, partial fractions, complex numbers from Cartesian
form to De Moivre and n-th roots, proof by induction/contradiction/
counterexample, and 3×3 linear systems with parameter cases. Every worked
example carries M/A/R markscheme lines AND a narrative layer; every numeric
claim is sympy-checked; banks are tagged with the official codes
(ib-aa-hl-1.x) via badges.

Run: python3 scripts/ib/build_hl_unit1.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-hl", "number-and-algebra.json")


def code_badge(code, marks=None, paper=None):
    b = [{"text": code, "mono": True}]
    if marks:
        b.append({"text": f"[{marks} marks]"})
    if paper:
        b.append({"text": paper})
    return b


# ===========================================================================
# Lesson 1 — AHL 1.10: Counting principles & the extended binomial theorem
# ===========================================================================
def lesson_counting_binomial():
    return {
        "slug": "counting-and-extended-binomial",
        "title": "Counting & the Extended Binomial Theorem",
        "concreteComparison": (
            "A 5-person team from 6 boys and 5 girls with 'at least 3 girls' is not one count — "
            "it is three disjoint counts added. And $\\sqrt{1.02}$ to six decimal places without a "
            "calculator? That is $(1+x)^{1/2}$ with $x = 0.02$ — the binomial theorem running on a "
            "FRACTIONAL exponent, something SL's version never allowed."
        ),
        "objective": (
            "Count arrangements and selections with $^nP_r$ and $\\binom{n}{r}$ under constraints, "
            "and expand $(1+x)^n$ for $n \\in \\mathbb{Q}$ as an infinite series, stating where it "
            "converges."
        ),
        "concept": [
            "**Syllabus card — AHL 1.10.** Counting principles: permutations $^nP_r$ and combinations "
            "$\\binom{n}{r}$; extension of the binomial theorem to fractional and negative indices. "
            "Papers 1 and 2, HL only. Typical weight: 5–8 marks. Builds directly on SL 1.9's binomial "
            "theorem — this lesson is where its guardrails come off.",
            "**Order or not?** $^nP_r = \\dfrac{n!}{(n-r)!}$ counts ARRANGEMENTS (order matters); "
            "$\\binom{n}{r} = \\dfrac{n!}{r!\\,(n-r)!}$ counts SELECTIONS (order ignored). The HL exam "
            "rarely says which — the context does. Medals are permutations; committees are combinations. "
            "When a problem says 'at least' or 'at most', split into disjoint cases and ADD; when a "
            "block of people must sit together, glue them into one unit, arrange, then arrange inside "
            "the glue: $2! \\times 6!$ for a couple inside seven seats.",
            "**The extended binomial theorem.** For ANY rational $n$, "
            "$(1+x)^n = 1 + nx + \\dfrac{n(n-1)}{2!}x^2 + \\dfrac{n(n-1)(n-2)}{3!}x^3 + \\cdots$ — "
            "but now the series never terminates, and it only CONVERGES for $|x| < 1$. The binomial "
            "coefficients still work: $\\binom{-2}{2} = \\dfrac{(-2)(-3)}{2!} = 3$. Pascal's triangle "
            "cannot draw these rows — there is no row $-2$ — which is exactly why the formula, not the "
            "triangle, is the real theorem.",
            "**Validity is a mark.** Every expansion of $(1+ax)^n$ with $n \\notin \\mathbb{N}$ must "
            "carry its interval: valid for $|ax| < 1$, i.e. $|x| < 1/|a|$. Writing the expansion of "
            "$(1-2x)^{-1}$ without $|x| < \\tfrac{1}{2}$ costs an A mark on Paper 1 — the examiner "
            "reads the missing interval as not knowing the series is infinite.",
            "**Why HL cares:** $(1-2x)^{-1} = 1 + 2x + 4x^2 + 8x^3 + \\cdots$ is the geometric series "
            "of SL 1.8 wearing binomial clothes — set $r = 2x$. The extended theorem is the bridge "
            "between Topic 1's two halves, and later it powers Maclaurin series (AHL 5.19) and "
            "approximation questions.",
        ],
        "keyIdea": (
            "Counting: decide order-or-not, split 'at least' into disjoint cases. Expanding: the "
            "binomial formula survives any rational exponent — the price is an infinite series and a "
            "validity interval $|x| < 1$."
        ),
        "facts": [
            {
                "title": "Permutations & combinations",
                "latex": "^nP_r = \\frac{n!}{(n-r)!}, \\qquad \\binom{n}{r} = \\frac{n!}{r!\\,(n-r)!}",
                "explanation": (
                    "IN the HL formula booklet (Topic 1 HL section). $^nP_r$ counts ordered "
                    "arrangements, $\\binom{n}{r}$ unordered selections — the exam expects you to "
                    "choose the right one from context."
                ),
            },
            {
                "title": "Extended binomial theorem",
                "latex": "(1+x)^n = 1 + nx + \\frac{n(n-1)}{2!}x^2 + \\cdots, \\quad n \\in \\mathbb{Q},\\ |x| < 1",
                "explanation": (
                    "IN the HL booklet. Infinite series; converges only for $|x| < 1$. For "
                    "$(a + bx)^n$ with fractional $n$, factor out $a^n$ first — the booklet form "
                    "needs a leading 1."
                ),
            },
            {
                "title": "Repeated letters",
                "latex": "\\frac{n!}{p!\\,q!\\,\\cdots}",
                "explanation": (
                    "NOT in the booklet — memorize. Arrangements of $n$ objects where one letter "
                    "repeats $p$ times, another $q$ times: divide out the invisible re-orderings."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-110-we1",
                "statement": (
                    "A school council of 5 students is chosen from 6 boys and 5 girls.  \n"
                    "**(a)** Find the number of councils containing **at least 3 girls**. **[4]**  \n"
                    "**(b)** Two particular students, Anar and Bataa, refuse to serve together. "
                    "Find the number of possible councils. **[3]**"
                ),
                "solution": (
                    "**(a)** 'At least 3 girls' splits into three disjoint cases *(M1 for case split)*:  \n"
                    "$$\\binom{5}{3}\\binom{6}{2} + \\binom{5}{4}\\binom{6}{1} + \\binom{5}{5}\\binom{6}{0}$$ "
                    "*(A1 for any two correct products)*  \n"
                    "$$= 10(15) + 5(6) + 1(1) = 150 + 30 + 1 \\;(A1)$$ "
                    "$$= 181 \\;(A1)$$  \n"
                    "**(b)** Count ALL councils, subtract the forbidden ones *(M1 for complement)*. "
                    "All: $\\binom{11}{5} = 462$. Councils containing BOTH Anar and Bataa: the other "
                    "3 seats from the remaining 9: $\\binom{9}{3} = 84$ *(A1)*. "
                    "$$462 - 84 = 378 \\;(A1)$$  \n"
                    "**Narrative:** (a) adds because the cases cannot overlap — a council has exactly "
                    "one girl-count. (b) subtracts because 'not both' is easier through its complement; "
                    "counting 'Anar without Bataa' + 'Bataa without Anar' + 'neither' also works but "
                    "triples the arithmetic."
                ),
                "check": [
                    "binomial(5, 3)*binomial(6, 2) == 150",
                    "binomial(5, 4)*binomial(6, 1) == 30",
                    "binomial(5, 5)*binomial(6, 0) == 1",
                    "binomial(5, 3)*binomial(6, 2) + binomial(5, 4)*binomial(6, 1) + binomial(5, 5)*binomial(6, 0) == 181",
                    "binomial(11, 5) == 462",
                    "binomial(9, 3) == 84",
                    "462 - 84 == 378",
                ],
            },
            {
                "id": "ibhl-110-we2",
                "statement": (
                    "**(a)** Expand $(1+3x)^{-2}$ in ascending powers of $x$ up to and including the "
                    "term in $x^3$, and state the values of $x$ for which the expansion is valid. **[5]**  \n"
                    "**(b)** Hence find the coefficient of $x^3$ in the expansion of "
                    "$\\dfrac{1 - x}{(1+3x)^{2}}$. **[3]**"
                ),
                "solution": (
                    "**(a)** Apply the extended theorem with $n = -2$ *(M1)*:  \n"
                    "$$1 + (-2)(3x) + \\frac{(-2)(-3)}{2!}(3x)^2 + \\frac{(-2)(-3)(-4)}{3!}(3x)^3$$ "
                    "*(A1 for unsimplified form)*  \n"
                    "$$= 1 - 6x + 27x^2 - 108x^3 \\;(A2: A1\\ per\\ two\\ terms)$$  \n"
                    "Valid for $|3x| < 1$, i.e. $|x| < \\dfrac{1}{3}$ *(A1)*.  \n"
                    "**(b)** Multiply the series by $(1 - x)$ and collect the $x^3$ terms *(M1)*: "
                    "$x^3$ arises as $1 \\cdot (-108x^3)$ and $(-x) \\cdot 27x^2$ *(A1)*:  \n"
                    "$$-108 - 27 = -135 \\;(A1)$$  \n"
                    "**Narrative:** the signs alternate because $n = -2$ makes every next factor "
                    "negative; the powers of 3 grow because the '$x$' of the theorem is $3x$. In (b) "
                    "you never expand the product fully — you harvest exactly the pairs of terms whose "
                    "powers add to 3. That harvesting IS the method mark."
                ),
                "check": [
                    "binomial(-2, 1)*3 == -6",
                    "binomial(-2, 2)*3**2 == 27",
                    "binomial(-2, 3)*3**3 == -108",
                    "Eq(series((1 + 3*x)**(-2), x, 0, 4).removeO(), -108*x**3 + 27*x**2 - 6*x + 1)",
                    "-108 - 27 == -135",
                    "Eq(series((1 - x)*(1 + 3*x)**(-2), x, 0, 4).removeO(), -135*x**3 + 33*x**2 - 7*x + 1)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using $^nP_r$ for a committee — 'choose 5 people' has no order, so $^{11}P_5$ overcounts by $5!$.",
                "correction": "Committees, teams, subsets: $\\binom{n}{r}$. Podiums, PIN codes, seatings: $^nP_r$ or direct slot-counting.",
                "authored": True,
            },
            {
                "text": "Expanding $(1+3x)^{-2}$ but treating the theorem's '$x$' as $x$ instead of $3x$ — every power of 3 goes missing.",
                "correction": "Substitute the WHOLE inner term: $(3x)^2 = 9x^2$, $(3x)^3 = 27x^3$. Bracket it before you square it.",
                "authored": True,
            },
            {
                "text": "Omitting the validity interval, or writing $|x| < 1$ out of habit.",
                "correction": "The condition is $|\\text{inner}| < 1$: for $(1+3x)^{-2}$ that is $|x| < \\tfrac{1}{3}$; for $(1 - \\tfrac{x}{2})^{-1}$ it is $|x| < 2$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-110-t1",
                "statement": (
                    "Seven students, including Sarnai and Tuguldur, sit in a row for a photo. Find the "
                    "number of arrangements in which Sarnai and Tuguldur sit **together**. **[3]**"
                ),
                "solution": (
                    "Glue the pair into one unit: $6$ units arrange in $6!$ ways *(M1)*, and the pair "
                    "arranges internally in $2!$ ways *(A1)*: $6! \\times 2! = 720 \\times 2 = 1440$ "
                    "*(A1)*. Refusing-to-sit-together would be the complement: $7! - 1440 = 3600$."
                ),
                "check": [
                    "factorial(6)*factorial(2) == 1440",
                    "factorial(7) - 1440 == 3600",
                ],
            },
            {
                "id": "ibhl-110-t2",
                "statement": (
                    "**(a)** Expand $\\sqrt{1+x}$ up to and including the term in $x^2$. **[3]**  \n"
                    "**(b)** Hence estimate $\\sqrt{1.02}$ to 6 decimal places. **[2]**"
                ),
                "solution": (
                    "**(a)** $n = \\tfrac{1}{2}$: $1 + \\tfrac{1}{2}x + \\dfrac{\\tfrac{1}{2}(-\\tfrac{1}{2})}{2!}x^2 "
                    "= 1 + \\tfrac{x}{2} - \\tfrac{x^2}{8}$ *(M1 A1)*, valid $|x| < 1$ *(A1)*.  \n"
                    "**(b)** $x = 0.02$: $1 + 0.01 - \\dfrac{0.0004}{8} = 1 + 0.01 - 0.00005 = 1.009950$ "
                    "*(M1 A1)*. (True value $1.0099504\\ldots$ — three terms already nail 6 d.p.)"
                ),
                "check": [
                    "Eq(series(sqrt(1 + x), x, 0, 3).removeO(), 1 + x/2 - x**2/8)",
                    "Eq(1 + Rational(1, 100) - Rational(1, 20000), Rational(100995, 100000))",
                    "Abs(sqrt(Rational(102, 100)) - Rational(100995, 100000)) < 0.0000005",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.10 · Papers 1 & 2",
                    "title": "The guardrails come off",
                    "body": (
                        "SL's binomial theorem stopped at natural exponents and finite rows. HL removes "
                        "both fences at once: counting grows constraints ('at least', 'must sit together', "
                        "'never together'), and $(1+x)^n$ starts accepting $n = -2$ and $n = \\tfrac{1}{2}$ "
                        "— at the price of an infinite series and a convergence condition."
                    ),
                },
                {
                    "kind": "pascalTriangle",
                    "eyebrow": "Where the triangle ends",
                    "title": "Pascal's triangle has no row −2",
                    "teach": (
                        "Every SL expansion lived in this triangle. Now try to point at row $-2$ or row "
                        "$\\tfrac{1}{2}$ — there isn't one. The FORMULA $\\binom{n}{r} = \\frac{n(n-1)\\cdots(n-r+1)}{r!}$ "
                        "still computes: $\\binom{-2}{2} = \\frac{(-2)(-3)}{2} = 3$. The triangle was the "
                        "training wheels; the formula is the theorem."
                    ),
                    "config": {"mode": "expansion", "rows": 6},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Order or not?",
                    "title": "Pick the right counter",
                    "prompt": (
                        "A club of 12 must pick a president, a secretary and a treasurer (all "
                        "different people). How many ways?"
                    ),
                    "options": [
                        "$^{12}P_3 = 1320$",
                        "$\\binom{12}{3} = 220$",
                        "$12^3 = 1728$",
                        "$3^{12}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The three jobs are DIFFERENT, so order matters: $12 \\times 11 \\times 10 = "
                        "{}^{12}P_3 = 1320$. $\\binom{12}{3}$ would count unlabeled trios; $12^3$ lets "
                        "one person hold all three jobs."
                    ),
                    "check": [
                        "factorial(12)/factorial(9) == 1320",
                        "binomial(12, 3) == 220",
                        "12*11*10 == 1320",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "At least 3 girls, and a feud",
                    "problemId": "ibhl-110-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Glue the pair",
                    "problemId": "ibhl-110-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "The extension",
                    "title": "Negative and fractional exponents",
                    "body": (
                        "$(1+x)^n = 1 + nx + \\frac{n(n-1)}{2!}x^2 + \\cdots$ for ANY rational $n$ — "
                        "the factors $n, n-1, n-2, \\ldots$ simply never reach zero, so the series never "
                        "stops. It converges only when $|x| < 1$; the validity statement is a scoring "
                        "line, not decoration. Sanity anchor: $n = -1$ reproduces the geometric series "
                        "$1 + x + x^2 + \\cdots$ for $\\frac{1}{1-x}$ (with $x \\to -x$)."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Coefficient check",
                    "title": "One binomial coefficient, negative upstairs",
                    "prompt": "What is $\\dbinom{-2}{3} = \\dfrac{(-2)(-3)(-4)}{3!}$?",
                    "options": ["$-4$", "$4$", "$-8$", "$\\dfrac{-2}{3}$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$(-2)(-3)(-4) = -24$ and $3! = 6$, so $\\binom{-2}{3} = -4$. Three negative "
                        "factors keep the minus — the alternating signs of $(1+x)^{-2}$ come exactly "
                        "from this."
                    ),
                    "check": [
                        "binomial(-2, 3) == -4",
                        "(-2)*(-3)*(-4) == -24",
                        "factorial(3) == 6",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Expand, bound, then harvest",
                    "problemId": "ibhl-110-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "A square root without a calculator",
                    "problemId": "ibhl-110-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.10 in four lines",
                    "points": [
                        "Order matters → $^nP_r$; selections → $\\binom{n}{r}$; 'at least' → disjoint cases, ADD; 'together' → glue; 'never together' → complement.",
                        "$(1+x)^n$ for $n \\in \\mathbb{Q}$: infinite series, coefficients from $\\frac{n(n-1)\\cdots}{r!}$.",
                        "ALWAYS state validity: $|\\text{inner}| < 1$.",
                        "Products of series: harvest only the powers you need — never expand everything.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — AHL 1.11: Partial fractions
# ===========================================================================
def lesson_partial_fractions():
    return {
        "slug": "partial-fractions",
        "title": "Partial Fractions",
        "concreteComparison": (
            "$\\dfrac{5x+1}{(x-1)(x+2)}$ is two simple fractions welded together — like a chord "
            "you can't play until you split it into notes. Partial fractions un-weld it: "
            "$\\dfrac{2}{x-1} + \\dfrac{3}{x+2}$. Every later HL tool — series expansion, "
            "integration — plays the notes, not the chord."
        ),
        "objective": (
            "Decompose a rational function with a denominator of up to two distinct linear factors "
            "into partial fractions, by substitution or by equating coefficients."
        ),
        "concept": [
            "**Syllabus card — AHL 1.11.** Partial fractions with denominators of up to two distinct "
            "linear factors: $\\dfrac{px+q}{(ax+b)(cx+d)} = \\dfrac{A}{ax+b} + \\dfrac{B}{cx+d}$. "
            "Papers 1 and 2. Weight: 4–6 marks alone, more when chained into an expansion (AHL 1.10) "
            "or an integral (AHL 5.16) — which is its real job.",
            "**The template first.** Write the identity BEFORE any arithmetic: "
            "$\\dfrac{5x+1}{(x-1)(x+2)} \\equiv \\dfrac{A}{x-1} + \\dfrac{B}{x+2}$. Multiplying up: "
            "$5x + 1 \\equiv A(x+2) + B(x-1)$. The $\\equiv$ matters — this holds for EVERY $x$, which "
            "is exactly the license to feed it convenient values.",
            "**The cover-up shortcut.** Substitute the root of each factor: $x = 1$ kills the $B$ "
            "term: $6 = 3A$, so $A = 2$. $x = -2$ kills the $A$ term: $-9 = -3B$, so $B = 3$. Two "
            "substitutions, two answers, no simultaneous equations. Equating coefficients ($x$: "
            "$5 = A + B$; constant: $1 = 2A - B$) gives the same pair and doubles as the CHECK.",
            "**Improper fractions divide first.** If the numerator's degree reaches the denominator's, "
            "long-divide before the template: $\\dfrac{x^2+3}{(x-1)(x+2)} = 1 + \\dfrac{-x+5}{(x-1)(x+2)}$, "
            "then split the remainder. The template only fits proper fractions — degree of top strictly "
            "below degree of bottom.",
            "**Why HL bothers:** $\\dfrac{2}{x-1}$ expands by the extended binomial theorem; "
            "$\\displaystyle\\int \\dfrac{2}{x-1}\\,dx = 2\\ln|x-1|$. The welded form does neither. "
            "Partial fractions is not a topic — it is a pre-processor for the rest of HL."
        ],
        "keyIdea": (
            "Template with $\\equiv$, multiply up, then substitute each factor's root — one letter "
            "dies per substitution. Check by equating coefficients."
        ),
        "facts": [
            {
                "title": "Two-factor template",
                "latex": "\\frac{px+q}{(ax+b)(cx+d)} \\equiv \\frac{A}{ax+b} + \\frac{B}{cx+d}",
                "explanation": (
                    "NOT in the booklet — the method is assumed known. AA HL keeps to two DISTINCT "
                    "linear factors (no repeated factors, no quadratic factors — those are beyond the "
                    "syllabus)."
                ),
            },
            {
                "title": "The license",
                "latex": "px + q \\equiv A(cx+d) + B(ax+b) \\;\\; \\text{for all } x",
                "explanation": (
                    "An identity, not an equation — substitute ANY value of $x$ (the factor roots are "
                    "the killers), or equate coefficients of like powers. Both earn the method mark."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-111-we1",
                "statement": (
                    "**(a)** Express $\\dfrac{5x+1}{(x-1)(x+2)}$ in partial fractions. **[4]**  \n"
                    "**(b)** Hence write down the first three terms of the expansion of "
                    "$\\dfrac{5x+1}{(x-1)(x+2)}$ in ascending powers of $x$, for $|x| < 1$. **[4]**"
                ),
                "solution": (
                    "**(a)** Template: $\\dfrac{5x+1}{(x-1)(x+2)} \\equiv \\dfrac{A}{x-1} + "
                    "\\dfrac{B}{x+2}$ *(M1)*, so $5x + 1 \\equiv A(x+2) + B(x-1)$ *(A1)*.  \n"
                    "$x = 1$: $\\;6 = 3A \\Rightarrow A = 2$ *(A1)*.  \n"
                    "$x = -2$: $\\;-9 = -3B \\Rightarrow B = 3$ *(A1)*.  \n"
                    "$$\\frac{5x+1}{(x-1)(x+2)} = \\frac{2}{x-1} + \\frac{3}{x+2}$$  \n"
                    "**(b)** Rewrite each piece for the theorem *(M1)*: "
                    "$\\dfrac{2}{x-1} = -2(1-x)^{-1} = -2(1 + x + x^2 + \\cdots)$ *(A1)*; "
                    "$\\dfrac{3}{x+2} = \\dfrac{3}{2}\\left(1+\\dfrac{x}{2}\\right)^{-1} = "
                    "\\dfrac{3}{2}\\left(1 - \\dfrac{x}{2} + \\dfrac{x^2}{4} - \\cdots\\right)$ *(A1)*.  \n"
                    "Sum: $\\left(-2 + \\dfrac{3}{2}\\right) + \\left(-2 - \\dfrac{3}{4}\\right)x + "
                    "\\left(-2 + \\dfrac{3}{8}\\right)x^2 = -\\dfrac{1}{2} - \\dfrac{11}{4}x - "
                    "\\dfrac{13}{8}x^2$ *(A1)*.  \n"
                    "**Narrative:** part (b) is impossible from the welded form — that is the point of "
                    "(a). Note the factor-out step: $(x+2)^{-1}$ is NOT $(1 + \\tfrac{x}{2})^{-1}$; "
                    "you must pull out the 2 first and pay $\\tfrac{1}{2}$."
                ),
                "check": [
                    "Eq(5*1 + 1, 6)",
                    "Rational(6, 3) == 2",
                    "Eq(5*(-2) + 1, -9)",
                    "Rational(-9, -3) == 3",
                    "simplify((5*x + 1)/((x - 1)*(x + 2)) - (2/(x - 1) + 3/(x + 2))) == 0",
                    "Eq(series((5*x + 1)/((x - 1)*(x + 2)), x, 0, 3).removeO(), -Rational(13, 8)*x**2 - Rational(11, 4)*x - Rational(1, 2))",
                    "Eq(-2 + Rational(3, 2), -Rational(1, 2))",
                    "Eq(-2 - Rational(3, 4), -Rational(11, 4))",
                    "Eq(-2 + Rational(3, 8), -Rational(13, 8))",
                ],
            },
            {
                "id": "ibhl-111-we2",
                "statement": (
                    "Express $\\dfrac{x-13}{(x+3)(x-1)}$ in the form "
                    "$\\dfrac{A}{x+3} + \\dfrac{B}{x-1}$. **[4]**"
                ),
                "solution": (
                    "Multiply up: $x - 13 \\equiv A(x-1) + B(x+3)$ *(M1)*.  \n"
                    "$x = -3$: $\\;-16 = -4A \\Rightarrow A = 4$ *(A1)*.  \n"
                    "$x = 1$: $\\;-12 = 4B \\Rightarrow B = -3$ *(A1)*.  \n"
                    "$$\\frac{x-13}{(x+3)(x-1)} = \\frac{4}{x+3} - \\frac{3}{x-1} \\;(A1)$$  \n"
                    "**Narrative:** check by coefficients: $x$-terms $A + B = 4 - 3 = 1$ ✓ and "
                    "constants $-A + 3B = -4 - 9 = -13$ ✓. Ten seconds of checking converts a "
                    "plausible answer into a certain one — HL papers punish unchecked sign slips."
                ),
                "check": [
                    "Eq(-3 - 13, -16)",
                    "Rational(-16, -4) == 4",
                    "Eq(1 - 13, -12)",
                    "Rational(-12, 4) == -3",
                    "simplify((x - 13)/((x + 3)*(x - 1)) - (4/(x + 3) - 3/(x - 1))) == 0",
                    "4 + (-3) == 1",
                    "-4 + 3*(-3) == -13",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Splitting $\\dfrac{x^2+3}{(x-1)(x+2)}$ straight into $\\frac{A}{x-1}+\\frac{B}{x+2}$ — the fraction is improper, and the split silently loses the '1'.",
                "correction": "Degree(top) ≥ degree(bottom) → long-divide first: quotient $+$ proper remainder, THEN the template.",
                "authored": True,
            },
            {
                "text": "Writing $\\dfrac{3}{x+2} = 3(1 + \\tfrac{x}{2})^{-1}$ when expanding — the factored-out 2 vanished.",
                "correction": "$\\dfrac{3}{x+2} = \\dfrac{3}{2}\\left(1 + \\dfrac{x}{2}\\right)^{-1}$. Factoring $a$ out of $(a+bx)^{-1}$ costs $a^{-1}$, and the validity becomes $|x| < a/|b|$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-111-t1",
                "statement": (
                    "Express $\\dfrac{7x+4}{(2x+1)(x-2)}$ in the form "
                    "$\\dfrac{A}{2x+1} + \\dfrac{B}{x-2}$. **[4]**"
                ),
                "solution": (
                    "$7x + 4 \\equiv A(x-2) + B(2x+1)$ *(M1)*. $x = 2$: $18 = 5B \\Rightarrow B = "
                    "\\tfrac{18}{5}$ *(A1)*. $x = -\\tfrac{1}{2}$: $\\tfrac{1}{2} = -\\tfrac{5}{2}A "
                    "\\Rightarrow A = -\\tfrac{1}{5}$ *(A1)*. So the split is "
                    "$-\\dfrac{1}{5(2x+1)} + \\dfrac{18}{5(x-2)}$ *(A1)*. Non-integer constants are "
                    "normal at HL — resist the urge to 'fix' them."
                ),
                "check": [
                    "Eq(7*2 + 4, 18)",
                    "Rational(18, 5) == Rational(18, 5)",
                    "Eq(7*Rational(-1, 2) + 4, Rational(1, 2))",
                    "Eq(Rational(-1, 2) - 2, Rational(-5, 2))",
                    "simplify((7*x + 4)/((2*x + 1)*(x - 2)) - (Rational(-1, 5)/(2*x + 1) + Rational(18, 5)/(x - 2))) == 0",
                ],
            },
            {
                "id": "ibhl-111-t2",
                "statement": (
                    "Given $\\dfrac{x^2 + 3}{(x-1)(x+2)} = 1 + \\dfrac{A}{x-1} + \\dfrac{B}{x+2}$, "
                    "find $A$ and $B$. **[5]**"
                ),
                "solution": (
                    "The fraction is improper (degrees equal), and the '1' is the quotient of the "
                    "division *(R1 for recognizing)*. Multiply up: $x^2 + 3 \\equiv (x-1)(x+2) + "
                    "A(x+2) + B(x-1)$ *(M1)*. $x = 1$: $4 = 3A \\Rightarrow A = \\tfrac{4}{3}$ *(A1)*. "
                    "$x = -2$: $7 = -3B \\Rightarrow B = -\\tfrac{7}{3}$ *(A1)*. So "
                    "$\\dfrac{x^2+3}{(x-1)(x+2)} = 1 + \\dfrac{4}{3(x-1)} - \\dfrac{7}{3(x+2)}$ *(A1)*."
                ),
                "check": [
                    "Eq(1**2 + 3, 4)",
                    "Rational(4, 3) == Rational(4, 3)",
                    "Eq((-2)**2 + 3, 7)",
                    "Rational(7, -3) == -Rational(7, 3)",
                    "simplify((x**2 + 3)/((x - 1)*(x + 2)) - (1 + Rational(4, 3)/(x - 1) - Rational(7, 3)/(x + 2))) == 0",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.11 · Papers 1 & 2",
                    "title": "Un-welding a fraction",
                    "body": (
                        "A rational function with two linear factors downstairs is two simple "
                        "fractions in disguise. The disguise blocks everything: you cannot expand it, "
                        "cannot integrate it, cannot read its behaviour. Partial fractions is the "
                        "un-welding tool — and at HL it is almost always step (a) of a longer question."
                    ),
                },
                {
                    "kind": "limitGraph",
                    "eyebrow": "Two spikes, one curve",
                    "title": "Each factor owns one asymptote",
                    "teach": (
                        "Near a vertical asymptote the function is dominated by ONE of its partial "
                        "fractions — the $\\frac{2}{x-1}$ piece blows up at $x = 1$ while "
                        "$\\frac{3}{x+2}$ stays polite there, and they swap jobs at $x = -2$. The "
                        "split is not algebra for its own sake: it separates the two behaviours the "
                        "welded form mixes."
                    ),
                    "config": {"mode": "infinite"},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Template check",
                    "title": "Which template fits?",
                    "prompt": (
                        "Which of these needs LONG DIVISION before the partial-fraction template?"
                    ),
                    "options": [
                        "$\\dfrac{x^2 + 3}{(x-1)(x+2)}$",
                        "$\\dfrac{5x + 1}{(x-1)(x+2)}$",
                        "$\\dfrac{7}{(2x+1)(x-2)}$",
                        "$\\dfrac{x - 13}{(x+3)(x-1)}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The template fits only PROPER fractions. $(x-1)(x+2)$ has degree 2, and "
                        "$x^2 + 3$ matches it — divide first ($= 1 + $ remainder), then split the "
                        "remainder. The other three all have degree-1 (or 0) numerators."
                    ),
                    "check": [
                        "Eq(expand((x - 1)*(x + 2)), x**2 + x - 2)",
                        "Eq(expand((x**2 + 3) - (x**2 + x - 2)), -x + 5)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Split, then expand — the classic chain",
                    "problemId": "ibhl-111-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Cover-up speed run",
                    "title": "Kill the B term",
                    "prompt": (
                        "For $x - 13 \\equiv A(x-1) + B(x+3)$, which substitution finds $A$ in one line?"
                    ),
                    "options": ["$x = -3$", "$x = 1$", "$x = 0$", "$x = 13$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$x = -3$ zeroes the $B(x+3)$ term: $-16 = -4A$, so $A = 4$. $x = 1$ finds $B$ "
                        "instead; $x = 0$ gives an equation MIXING both letters — legal, but you'd "
                        "need a second equation."
                    ),
                    "check": [
                        "Eq(-3 + 3, 0)",
                        "Rational(-16, -4) == 4",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Cover-up with a sign to survive",
                    "problemId": "ibhl-111-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Fractional constants are fine",
                    "problemId": "ibhl-111-t1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn — harder",
                    "title": "Improper: divide, then split",
                    "problemId": "ibhl-111-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.11 in four lines",
                    "points": [
                        "Template with $\\equiv$: $\\frac{A}{ax+b} + \\frac{B}{cx+d}$ — proper fractions only.",
                        "Substitute each factor's root: one letter dies per substitution.",
                        "Improper? Long-divide first; the quotient rides in front.",
                        "The split exists to FEED other tools: binomial expansion now, integration in Topic 5.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — AHL 1.12: Complex numbers — Cartesian form & the Argand diagram
# ===========================================================================
def lesson_complex_cartesian():
    return {
        "slug": "complex-numbers-cartesian",
        "title": "Complex Numbers: Cartesian Form",
        "concreteComparison": (
            "$x^2 = -9$ has no answer on the number LINE — so mathematics added a second axis. "
            "On the Argand plane, $3i$ lives one turn of $90°$ above $3$, and suddenly every "
            "quadratic has exactly two roots, no exceptions. It is not a trick; it is a bigger map."
        ),
        "objective": (
            "Compute with $z = a + bi$ — add, multiply, divide by the conjugate, equate real and "
            "imaginary parts — and read $z$, $z^*$ and $|z|$ off the Argand diagram."
        ),
        "concept": [
            "**Syllabus card — AHL 1.12.** Cartesian form $z = a + bi$; sums, products and quotients; "
            "the complex plane (Argand diagram); complex conjugate $z^*$; modulus $|z|$. Papers 1 "
            "and 2. Weight: 4–7 marks, and the FOUNDATION for AHL 1.13–1.14 — polar form and De "
            "Moivre assume today's fluency.",
            "**One new number, all old rules.** $i^2 = -1$ is the entire new axiom. Everything else "
            "is ordinary algebra: $(3+2i) + (1-4i) = 4 - 2i$; "
            "$(3+2i)(1-4i) = 3 - 12i + 2i - 8i^2 = 3 - 10i + 8 = 11 - 10i$. Collect real with real, "
            "imaginary with imaginary — like terms, HL edition.",
            "**Division is a rationalization.** $\\dfrac{3+2i}{1-4i}$ has a complex denominator; "
            "multiply top and bottom by the CONJUGATE $1+4i$: the denominator becomes "
            "$1^2 + 4^2 = 17$ (always real, always $a^2+b^2$), and the quotient lands in Cartesian "
            "form: $\\dfrac{-5+14i}{17}$. Same move as rationalizing $\\frac{1}{1-\\sqrt{2}}$ — the "
            "conjugate is the universal denominator-cleaner.",
            "**Equating parts is a system.** If $(x+yi)(2-i) = 5+5i$ with $x, y$ real, expand and "
            "match: real $2x + y = 5$, imaginary $2y - x = 5$ — two equations, two unknowns, "
            "$x = 1$, $y = 3$. One complex equation always carries TWO real equations inside it. "
            "That doubling is the exam's favourite trick.",
            "**The Argand picture.** Plot $a + bi$ at $(a, b)$: the real axis is the old number "
            "line, the imaginary axis its $90°$ rotation. $|z| = \\sqrt{a^2+b^2}$ is the arrow's "
            "length (Pythagoras); the conjugate $z^* = a - bi$ is the mirror image in the real "
            "axis. Quadratics with negative discriminant have roots OFF the line — a conjugate "
            "pair, symmetric about the real axis.",
        ],
        "keyIdea": (
            "$i^2 = -1$ plus ordinary algebra. Divide by multiplying with the conjugate; one "
            "complex equation = two real equations; the Argand diagram turns all of it into "
            "geometry."
        ),
        "facts": [
            {
                "title": "Cartesian form & conjugate",
                "latex": "z = a + bi, \\qquad z^* = a - bi, \\qquad zz^* = a^2 + b^2",
                "explanation": (
                    "NOT in the booklet — core definitions. $zz^*$ is real and equals $|z|^2$: the "
                    "engine of complex division."
                ),
            },
            {
                "title": "Modulus",
                "latex": "|z| = \\sqrt{a^2 + b^2}",
                "explanation": (
                    "The arrow's length on the Argand diagram — Pythagoras on the legs $a$ and $b$. "
                    "Multiplicative: $|zw| = |z||w|$."
                ),
            },
            {
                "title": "Equality",
                "latex": "a + bi = c + di \\iff a = c \\text{ and } b = d",
                "explanation": (
                    "Real parts match AND imaginary parts match — one complex equation is two real "
                    "ones. Only legal when $a, b, c, d$ are known to be real: say so in solutions."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-112-we1",
                "statement": (
                    "Let $z = \\dfrac{3+2i}{1-4i}$.  \n"
                    "**(a)** Express $z$ in the form $a + bi$, where $a, b \\in \\mathbb{Q}$. **[3]**  \n"
                    "**(b)** Find $|z|$, giving your answer in the form $\\dfrac{\\sqrt{p}}{q}$. **[3]**"
                ),
                "solution": (
                    "**(a)** Multiply by the conjugate of the denominator *(M1)*:  \n"
                    "$$z = \\frac{(3+2i)(1+4i)}{(1-4i)(1+4i)} = \\frac{3 + 12i + 2i + 8i^2}{1 + 16}$$ "
                    "*(A1 for either product)*  \n"
                    "$$= \\frac{-5 + 14i}{17} = -\\frac{5}{17} + \\frac{14}{17}i \\;(A1)$$  \n"
                    "**(b)** Route 1 — from (a): $|z| = \\dfrac{1}{17}\\sqrt{5^2 + 14^2} = "
                    "\\dfrac{\\sqrt{221}}{17}$. Route 2 — the modulus shortcut *(M1)*: "
                    "$|z| = \\dfrac{|3+2i|}{|1-4i|} = \\dfrac{\\sqrt{13}}{\\sqrt{17}}$ *(A1)* "
                    "$= \\sqrt{\\dfrac{13}{17}} = \\dfrac{\\sqrt{221}}{17}$ *(A1)*.  \n"
                    "**Narrative:** the shortcut $|z/w| = |z|/|w|$ skips the division entirely — and "
                    "confirms (a): $\\sqrt{\\left(\\frac{5}{17}\\right)^2 + \\left(\\frac{14}{17}\\right)^2} "
                    "= \\frac{\\sqrt{221}}{17}$ ✓. When an HL part (b) can be done two ways, do both: "
                    "one is the answer, the other is the check."
                ),
                "check": [
                    "simplify((3 + 2*I)/(1 - 4*I) - (Rational(-5, 17) + Rational(14, 17)*I)) == 0",
                    "Eq(expand((3 + 2*I)*(1 + 4*I)), -5 + 14*I)",
                    "Eq(expand((1 - 4*I)*(1 + 4*I)), 17)",
                    "Eq(5**2 + 14**2, 221)",
                    "Eq(Abs(3 + 2*I), sqrt(13))",
                    "Eq(Abs(1 - 4*I), sqrt(17))",
                    "Eq(sqrt(13)/sqrt(17), sqrt(221)/17)",
                ],
            },
            {
                "id": "ibhl-112-we2",
                "statement": (
                    "**(a)** Solve $z^2 - 4z + 13 = 0$. **[3]**  \n"
                    "**(b)** The roots are $z_1$ and $z_2$ with $\\mathrm{Im}(z_1) > 0$. Plot them on "
                    "an Argand diagram and **write down** the geometric relationship between them. **[2]**  \n"
                    "**(c)** Verify that $z_1 z_2 = |z_1|^2$. **[2]**"
                ),
                "solution": (
                    "**(a)** Quadratic formula *(M1)*: $z = \\dfrac{4 \\pm \\sqrt{16 - 52}}{2} = "
                    "\\dfrac{4 \\pm \\sqrt{-36}}{2}$ *(A1)* $= 2 \\pm 3i$ *(A1)*.  \n"
                    "**(b)** $z_1 = 2 + 3i$ at $(2, 3)$, $z_2 = 2 - 3i$ at $(2, -3)$: they are a "
                    "conjugate pair — reflections of each other in the real axis *(A1 for plot, A1 for "
                    "'reflection/conjugates')*.  \n"
                    "**(c)** $z_1 z_2 = (2+3i)(2-3i) = 4 + 9 = 13$ *(A1)* and $|z_1|^2 = 2^2 + 3^2 = "
                    "13$ ✓ *(A1)*.  \n"
                    "**Narrative:** real coefficients force complex roots into conjugate pairs — the "
                    "diagram makes it visible: the parabola's roots hide symmetrically above and below "
                    "the axis it never crossed. And $z z^* = |z|^2$ is why (c) had to work: the "
                    "product of a conjugate pair is always the squared distance from the origin."
                ),
                "check": [
                    "Eq(expand((2 + 3*I)**2 - 4*(2 + 3*I) + 13), 0)",
                    "Eq(expand((2 - 3*I)**2 - 4*(2 - 3*I) + 13), 0)",
                    "Eq(16 - 52, -36)",
                    "Eq(expand((2 + 3*I)*(2 - 3*I)), 13)",
                    "Eq(Abs(2 + 3*I)**2, 13)",
                ],
            },
            {
                "id": "ibhl-112-we3",
                "statement": (
                    "Find the real numbers $x$ and $y$ such that $(x + yi)(2 - i) = 5 + 5i$. **[5]**"
                ),
                "solution": (
                    "Expand the left side *(M1)*: $(x+yi)(2-i) = 2x - xi + 2yi - y i^2 = "
                    "(2x + y) + (2y - x)i$ *(A1)*.  \n"
                    "Equate real and imaginary parts *(M1 — say '$x, y$ real' out loud)*:  \n"
                    "$$2x + y = 5, \\qquad -x + 2y = 5$$  \n"
                    "Doubling the first and adding: $5y = 15 \\Rightarrow y = 3$, then $x = 1$ "
                    "*(A1 A1)*.  \n"
                    "**Narrative:** check by substituting back: $(1 + 3i)(2 - i) = 2 - i + 6i - 3i^2 "
                    "= 5 + 5i$ ✓. The alternative route — divide $5+5i$ by $2-i$ — lands on the same "
                    "$1 + 3i$ and is often faster; knowing both is HL fluency."
                ),
                "check": [
                    "simplify((x + y*I)*(2 - I) - (2*x + y + (2*y - x)*I)) == 0",
                    "solve([Eq(2*x + y, 5), Eq(-x + 2*y, 5)], [x, y]) == {x: 1, y: 3}",
                    "Eq(expand((1 + 3*I)*(2 - I)), 5 + 5*I)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Writing $(1-4i)(1+4i) = 1 - 16$ — forgetting that $-(4i)(4i) = -16i^2 = +16$.",
                "correction": "Conjugate products are SUMS of squares: $(a-bi)(a+bi) = a^2 + b^2$. The denominator of a complex division is always positive.",
                "authored": True,
            },
            {
                "text": "Equating real and imaginary parts without stating $x, y \\in \\mathbb{R}$ — if they could be complex, the split is illegal.",
                "correction": "One sentence buys the R mark: 'since $x$ and $y$ are real, comparing real and imaginary parts…'",
                "authored": True,
            },
            {
                "text": "Plotting $2 - 3i$ at $(-3, 2)$ — coordinates swapped.",
                "correction": "Argand: horizontal = REAL part, vertical = IMAGINARY part. $2 - 3i \\mapsto (2, -3)$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-112-t1",
                "statement": (
                    "Let $w = \\dfrac{10}{3 - i}$. Express $w$ in the form $a + bi$ and find $|w|$. **[4]**"
                ),
                "solution": (
                    "$w = \\dfrac{10(3+i)}{(3-i)(3+i)} = \\dfrac{30 + 10i}{10} = 3 + i$ *(M1 A1)*. "
                    "Then $|w| = \\sqrt{9 + 1} = \\sqrt{10}$ *(A1)*. Shortcut check: "
                    "$|w| = \\dfrac{|10|}{|3-i|} = \\dfrac{10}{\\sqrt{10}} = \\sqrt{10}$ ✓ *(A1)*."
                ),
                "check": [
                    "simplify(10/(3 - I) - (3 + I)) == 0",
                    "Eq(expand((3 - I)*(3 + I)), 10)",
                    "Eq(Abs(3 + I), sqrt(10))",
                    "Eq(10/sqrt(10), sqrt(10))",
                ],
            },
            {
                "id": "ibhl-112-t2",
                "statement": (
                    "The complex number $z$ satisfies $z + 2z^* = 9 + 2i$. Find $z$ in the form "
                    "$a + bi$. **[4]**"
                ),
                "solution": (
                    "Let $z = a + bi$ with $a, b$ real *(M1)*. Then $z + 2z^* = (a + bi) + 2(a - bi) "
                    "= 3a - bi$ *(A1)*. Equate parts: $3a = 9 \\Rightarrow a = 3$; $-b = 2 "
                    "\\Rightarrow b = -2$ *(A1)*. So $z = 3 - 2i$ *(A1)*. The conjugate FLIPS the "
                    "sign of $b$ — that flip is what makes the imaginary part shrink to $-b$, not $3b$."
                ),
                "check": [
                    "Eq(expand((3 - 2*I) + 2*conjugate(3 - 2*I)), 9 + 2*I)",
                    "Eq(3*3, 9)",
                    "Eq(-(-2), 2)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.12 · Papers 1 & 2",
                    "title": "The number line grows a second axis",
                    "body": (
                        "$x^2 = -9$ is unsolvable on a LINE. Define $i$ with $i^2 = -1$ and the line "
                        "becomes a PLANE: every complex number $a + bi$ is a point (and an arrow) at "
                        "$(a, b)$. Nothing else changes — algebra proceeds as usual, collecting $i$ "
                        "terms like any other like terms."
                    ),
                },
                {
                    "kind": "argandPlot",
                    "eyebrow": "The map",
                    "title": "Walk z around the plane",
                    "teach": (
                        "Step $\\mathrm{Re}(z)$ and $\\mathrm{Im}(z)$ and watch the arrow: its length "
                        "is $|z| = \\sqrt{a^2 + b^2}$ (Pythagoras on the dashed legs), and the mirror "
                        "arrow below the real axis is the conjugate $z^*$. Reflection in the real "
                        "axis IS conjugation — keep that picture; it explains half of this topic."
                    ),
                    "config": {"mode": "plot", "a": 3, "b": 2, "showConjugate": True},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Multiply two complex numbers",
                    "prompt": "$(3 + 2i)(1 - 4i) = {}$?",
                    "options": ["$11 - 10i$", "$3 - 8i$", "$-5 - 10i$", "$11 + 14i$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$3 - 12i + 2i - 8i^2 = 3 - 10i + 8 = 11 - 10i$. The $-8i^2$ becoming $+8$ "
                        "is the whole game — $i^2 = -1$ turns the last term real."
                    ),
                    "check": [
                        "Eq(expand((3 + 2*I)*(1 - 4*I)), 11 - 10*I)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Divide by the conjugate, twice-check the modulus",
                    "problemId": "ibhl-112-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Conjugate instinct",
                    "title": "Clean the denominator",
                    "prompt": "To express $\\dfrac{2+i}{3+4i}$ in Cartesian form, multiply top and bottom by:",
                    "options": ["$3 - 4i$", "$3 + 4i$", "$2 - i$", "$-3 - 4i$"],
                    "correctIndex": 0,
                    "explanation": (
                        "The conjugate of the DENOMINATOR: $(3+4i)(3-4i) = 9 + 16 = 25$, real. "
                        "Multiplying by $2-i$ cleans nothing; by $3+4i$ makes it worse."
                    ),
                    "check": [
                        "Eq(expand((3 + 4*I)*(3 - 4*I)), 25)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A quadratic leaves the real line",
                    "problemId": "ibhl-112-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "One division, two moduli",
                    "problemId": "ibhl-112-t1",
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "One complex equation, two real ones",
                    "problemId": "ibhl-112-we3",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn — harder",
                    "title": "z meets its conjugate",
                    "problemId": "ibhl-112-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.12 in four lines",
                    "points": [
                        "$i^2 = -1$; everything else is like-terms algebra on $a + bi$.",
                        "Division: multiply by the denominator's conjugate — $(a+bi)(a-bi) = a^2 + b^2$.",
                        "One complex equation = two real equations (state that $x, y$ are real).",
                        "Argand: $z$ at $(a, b)$, $|z|$ the length, $z^*$ the mirror in the real axis.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — AHL 1.13: Modulus–argument form & Euler form
# ===========================================================================
def lesson_polar_euler():
    return {
        "slug": "modulus-argument-and-euler-form",
        "title": "Modulus–Argument & Euler Form",
        "concreteComparison": (
            "Cartesian form is a street address: go $a$ east, $b$ north. Polar form is a compass "
            "bearing: length $r$, angle $\\theta$. Same point, two languages — and multiplication, "
            "clumsy in street-addresses, becomes one sentence in compass language: lengths multiply, "
            "angles add."
        ),
        "objective": (
            "Convert between $a + bi$, $r(\\cos\\theta + i\\sin\\theta)$ and $re^{i\\theta}$, and "
            "multiply/divide complex numbers by multiplying moduli and adding arguments."
        ),
        "concept": [
            "**Syllabus card — AHL 1.13.** Modulus–argument (polar) form "
            "$z = r(\\cos\\theta + i\\sin\\theta) = r\\,\\mathrm{cis}\\,\\theta$; Euler form "
            "$z = re^{i\\theta}$; products and quotients in polar form. Papers 1 and 2. Weight: 4–7 "
            "marks, and the launchpad for De Moivre (AHL 1.14).",
            "**Converting is a triangle.** From $z = a + bi$: modulus $r = \\sqrt{a^2+b^2}$, argument "
            "$\\theta = \\arg z$ measured from the positive real axis, $-\\pi < \\theta \\le \\pi$. "
            "DRAW the point first: $\\tan^{-1}\\!\\frac{b}{a}$ alone lies in the wrong quadrant half "
            "the time — $-2 + 2i$ sits in the second quadrant at $\\theta = \\frac{3\\pi}{4}$, not "
            "$-\\frac{\\pi}{4}$. The sketch is not decoration; it is the error-catcher.",
            "**Why polar exists: multiplication.** If $z_1 = r_1\\,\\mathrm{cis}\\,\\theta_1$ and "
            "$z_2 = r_2\\,\\mathrm{cis}\\,\\theta_2$, then $z_1 z_2 = r_1 r_2\\,\\mathrm{cis}(\\theta_1 "
            "+ \\theta_2)$ and $\\dfrac{z_1}{z_2} = \\dfrac{r_1}{r_2}\\,\\mathrm{cis}(\\theta_1 - "
            "\\theta_2)$. Multiplying by $z$ ROTATES by $\\arg z$ and SCALES by $|z|$ — complex "
            "multiplication is geometry. Multiplying by $i$ is a pure quarter-turn.",
            "**Euler form.** $e^{i\\theta} = \\cos\\theta + i\\sin\\theta$, so $z = re^{i\\theta}$ — "
            "polar form in exponential clothing. Now the product rule is just exponent laws: "
            "$r_1e^{i\\theta_1} \\cdot r_2e^{i\\theta_2} = r_1r_2\\,e^{i(\\theta_1+\\theta_2)}$. Set "
            "$r = 1, \\theta = \\pi$: $e^{i\\pi} + 1 = 0$ — five constants, one line.",
            "**The exact-value harvest.** Multiply two friendly numbers in BOTH languages and the "
            "languages must agree — comparing them yields exact values of awkward angles: "
            "$(1 + i\\sqrt{3})(1 - i)$ has argument $\\frac{\\pi}{3} - \\frac{\\pi}{4} = "
            "\\frac{\\pi}{12}$, and its Cartesian form hands you $\\cos\\frac{\\pi}{12} = "
            "\\frac{\\sqrt{6}+\\sqrt{2}}{4}$. HL Paper 1 loves this move.",
        ],
        "keyIdea": (
            "$z = re^{i\\theta}$: length and angle. Multiply → moduli multiply, arguments add. "
            "Always sketch before claiming an argument."
        ),
        "facts": [
            {
                "title": "Polar / Euler form",
                "latex": "z = r(\\cos\\theta + i\\sin\\theta) = re^{i\\theta}",
                "explanation": (
                    "NOT in the booklet — memorize. $r = |z| = \\sqrt{a^2+b^2}$; $\\theta = \\arg z$ "
                    "with principal range $-\\pi < \\theta \\le \\pi$."
                ),
            },
            {
                "title": "Product & quotient",
                "latex": "z_1 z_2 = r_1 r_2\\, e^{i(\\theta_1 + \\theta_2)}, \\qquad \\frac{z_1}{z_2} = \\frac{r_1}{r_2}\\, e^{i(\\theta_1 - \\theta_2)}",
                "explanation": (
                    "Moduli multiply/divide, arguments add/subtract. Multiplication by $z$ = rotate "
                    "by $\\arg z$, scale by $|z|$."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-113-we1",
                "statement": (
                    "**(a)** Express $z = -2 + 2i$ in the form $re^{i\\theta}$, where $r > 0$ and "
                    "$-\\pi < \\theta \\le \\pi$. **[3]**  \n"
                    "**(b)** Hence express $z^2$ in Cartesian form. **[3]**"
                ),
                "solution": (
                    "**(a)** $r = \\sqrt{(-2)^2 + 2^2} = 2\\sqrt{2}$ *(A1)*. The point $(-2, 2)$ lies "
                    "in the SECOND quadrant *(M1 — sketch)*: $\\theta = \\pi - \\frac{\\pi}{4} = "
                    "\\frac{3\\pi}{4}$ *(A1)*. So $z = 2\\sqrt{2}\\,e^{3\\pi i/4}$.  \n"
                    "**(b)** Square in Euler form *(M1)*: $z^2 = (2\\sqrt{2})^2 e^{3\\pi i/2} = "
                    "8e^{3\\pi i/2}$ *(A1)*. Principal form: $e^{3\\pi i/2} = e^{-\\pi i/2} = -i$, so "
                    "$z^2 = -8i$ *(A1)*.  \n"
                    "**Narrative:** check in Cartesian: $(-2+2i)^2 = 4 - 8i + 4i^2 = -8i$ ✓. The "
                    "naive $\\tan^{-1}\\frac{2}{-2} = -\\frac{\\pi}{4}$ points into the FOURTH "
                    "quadrant — the sketch is what saves the argument mark."
                ),
                "check": [
                    "Eq(Abs(-2 + 2*I), 2*sqrt(2))",
                    "Eq(arg(-2 + 2*I), 3*pi/4)",
                    "Eq(expand((-2 + 2*I)**2), -8*I)",
                    "simplify(expand_complex((2*sqrt(2))**2*exp(3*pi*I/2) - (-8*I))) == 0",
                ],
            },
            {
                "id": "ibhl-113-we2",
                "statement": (
                    "Let $z_1 = 1 + i\\sqrt{3}$ and $z_2 = 1 - i$.  \n"
                    "**(a)** Write $z_1$ and $z_2$ in the form $r\\,\\mathrm{cis}\\,\\theta$. **[4]**  \n"
                    "**(b)** Find $z_1 z_2$ in Cartesian form. **[2]**  \n"
                    "**(c)** Hence show that $\\cos\\dfrac{\\pi}{12} = \\dfrac{\\sqrt{6} + \\sqrt{2}}{4}$. **[3]**"
                ),
                "solution": (
                    "**(a)** $|z_1| = \\sqrt{1+3} = 2$, $\\arg z_1 = \\frac{\\pi}{3}$ *(A1 A1)*; "
                    "$|z_2| = \\sqrt{2}$, $\\arg z_2 = -\\frac{\\pi}{4}$ *(A1 A1)*.  \n"
                    "**(b)** Expand *(M1)*: $z_1 z_2 = 1 - i + i\\sqrt{3} - i^2\\sqrt{3} = "
                    "(1 + \\sqrt{3}) + (\\sqrt{3} - 1)i$ *(A1)*.  \n"
                    "**(c)** In polar: $z_1 z_2 = 2\\sqrt{2}\\,\\mathrm{cis}\\!\\left(\\frac{\\pi}{3} - "
                    "\\frac{\\pi}{4}\\right) = 2\\sqrt{2}\\,\\mathrm{cis}\\,\\frac{\\pi}{12}$ *(M1)*. "
                    "The two forms describe ONE number, so the real parts agree *(R1)*:  \n"
                    "$$2\\sqrt{2}\\cos\\frac{\\pi}{12} = 1 + \\sqrt{3} \\;\\Rightarrow\\; "
                    "\\cos\\frac{\\pi}{12} = \\frac{1+\\sqrt{3}}{2\\sqrt{2}} = "
                    "\\frac{\\sqrt{2} + \\sqrt{6}}{4} \\;(AG)$$  \n"
                    "**Narrative:** multiply once in each language, then eavesdrop on the agreement — "
                    "this is THE standard exact-value derivation, and 'show that' means the printed "
                    "target must fall out, not be assumed."
                ),
                "check": [
                    "Eq(Abs(1 + sqrt(3)*I), 2)",
                    "Eq(arg(1 + sqrt(3)*I), pi/3)",
                    "Eq(Abs(1 - I), sqrt(2))",
                    "Eq(arg(1 - I), -pi/4)",
                    "simplify((1 + sqrt(3)*I)*(1 - I) - (1 + sqrt(3) + (sqrt(3) - 1)*I)) == 0",
                    "Eq(pi/3 - pi/4, pi/12)",
                    "Eq(cos(pi/12), sqrt(6)/4 + sqrt(2)/4)",
                    "simplify((1 + sqrt(3))/(2*sqrt(2)) - (sqrt(6) + sqrt(2))/4) == 0",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reading $\\arg(-2+2i)$ as $\\tan^{-1}(2/{-2}) = -\\frac{\\pi}{4}$ — the calculator's arctan only knows two quadrants.",
                "correction": "Sketch first. Second quadrant: $\\theta = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4}$. Third quadrant: $\\theta = -\\pi + \\text{ref}$.",
                "authored": True,
            },
            {
                "text": "Leaving an argument outside the principal range, e.g. $z^2 = 8e^{3\\pi i/2}$ as the final answer.",
                "correction": "Wrap into $-\\pi < \\theta \\le \\pi$: $\\frac{3\\pi}{2} \\equiv -\\frac{\\pi}{2}$. Same point, legal label.",
                "authored": True,
            },
            {
                "text": "Multiplying polar forms by multiplying the arguments.",
                "correction": "Moduli MULTIPLY, arguments ADD: $r_1r_2\\,\\mathrm{cis}(\\theta_1 + \\theta_2)$. (Adding moduli is the other classic slip.)",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-113-t1",
                "statement": (
                    "Express $w = -1 - i\\sqrt{3}$ in the form $re^{i\\theta}$ with "
                    "$-\\pi < \\theta \\le \\pi$, and hence write $\\dfrac{4}{w}$ in Euler form. **[5]**"
                ),
                "solution": (
                    "$r = \\sqrt{1 + 3} = 2$ *(A1)*. Third quadrant *(M1)*: $\\theta = -\\pi + "
                    "\\frac{\\pi}{3} = -\\frac{2\\pi}{3}$ *(A1)*, so $w = 2e^{-2\\pi i/3}$. Then "
                    "$\\dfrac{4}{w} = \\dfrac{4}{2}e^{-(-2\\pi/3)i} = 2e^{2\\pi i/3}$ *(M1 A1)* — "
                    "modulus divides, argument negates."
                ),
                "check": [
                    "Eq(Abs(-1 - sqrt(3)*I), 2)",
                    "Eq(arg(-1 - sqrt(3)*I), -2*pi/3)",
                    "simplify(expand_complex(4/(-1 - sqrt(3)*I) - 2*exp(2*pi*I/3))) == 0",
                ],
            },
            {
                "id": "ibhl-113-t2",
                "statement": (
                    "Given $z_1 = 4e^{5\\pi i/6}$ and $z_2 = 2e^{\\pi i/3}$, express "
                    "$\\dfrac{z_1}{z_2}$ in Cartesian form. **[3]**"
                ),
                "solution": (
                    "$\\dfrac{z_1}{z_2} = \\dfrac{4}{2}e^{i(5\\pi/6 - \\pi/3)} = 2e^{i\\pi/2}$ "
                    "*(M1 A1)* $= 2\\left(\\cos\\frac{\\pi}{2} + i\\sin\\frac{\\pi}{2}\\right) = 2i$ "
                    "*(A1)*. A quotient of two messy-looking numbers can be purely imaginary — the "
                    "arguments did all the work."
                ),
                "check": [
                    "Eq(5*pi/6 - pi/3, pi/2)",
                    "simplify(expand_complex(4*exp(5*pi*I/6)/(2*exp(pi*I/3)) - 2*I)) == 0",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.13 · Papers 1 & 2",
                    "title": "Street address vs compass bearing",
                    "body": (
                        "Cartesian $a + bi$ says how far east and north. Polar $r\\,\\mathrm{cis}\\,"
                        "\\theta$ says how FAR and in what DIRECTION. Adding likes Cartesian; "
                        "multiplying loves polar — because multiplication rotates and scales, and "
                        "polar form is built from exactly those two dials."
                    ),
                },
                {
                    "kind": "argandPlot",
                    "eyebrow": "Read the dials",
                    "title": "Modulus and argument, live",
                    "teach": (
                        "Steer $z$ and watch the two polar dials: $|z|$ is the arrow's length, "
                        "$\\arg z$ its angle from the positive real axis (radians, principal range). "
                        "Park $z$ in the second quadrant and compare $\\arg z$ with what "
                        "$\\tan^{-1}(b/a)$ would claim — the quadrant correction you must make by "
                        "hand is exactly what the sketch is for."
                    ),
                    "config": {"mode": "plot", "a": -2, "b": 2, "showConjugate": False},
                },
                {
                    "kind": "unitCircle",
                    "eyebrow": "The r = 1 skeleton",
                    "title": "cis θ walks the unit circle",
                    "teach": (
                        "$\\mathrm{cis}\\,\\theta = \\cos\\theta + i\\sin\\theta$ is precisely the "
                        "unit-circle point at angle $\\theta$ — the $x$-coordinate is the real part, "
                        "the $y$-coordinate the imaginary part. Every complex number is this point "
                        "scaled by $r$. Your SL unit-circle fluency just became complex-number "
                        "fluency."
                    ),
                    "config": {"mode": "explore", "start": 60},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Quadrant discipline",
                    "title": "Argument of a third-quadrant number",
                    "prompt": "What is $\\arg(-1 - i)$ in the principal range $-\\pi < \\theta \\le \\pi$?",
                    "options": [
                        "$-\\dfrac{3\\pi}{4}$",
                        "$\\dfrac{\\pi}{4}$",
                        "$\\dfrac{3\\pi}{4}$",
                        "$-\\dfrac{\\pi}{4}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$(-1, -1)$ sits in the third quadrant; reference angle $\\frac{\\pi}{4}$, "
                        "measured NEGATIVELY from the positive real axis: $-\\pi + \\frac{\\pi}{4} = "
                        "-\\frac{3\\pi}{4}$. Naive arctan gives $\\frac{\\pi}{4}$ — first-quadrant "
                        "nonsense."
                    ),
                    "check": [
                        "Eq(arg(-1 - I), -3*pi/4)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Convert, then square in one line",
                    "problemId": "ibhl-113-we1",
                },
                {
                    "kind": "argandPlot",
                    "eyebrow": "Multiplication is rotation",
                    "title": "Watch arguments add",
                    "teach": (
                        "Set $|z| = 1$ and step the power: each multiplication by $z$ turns the "
                        "arrow by $\\arg z$ without changing its length — the points walk the unit "
                        "circle. Nudge $|z|$ above 1 and the walk becomes an outward spiral: moduli "
                        "multiplying, arguments adding, both visible at once."
                    ),
                    "config": {"mode": "powers", "r": 1, "thetaDeg": 30, "n": 6},
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two languages, one exact value",
                    "problemId": "ibhl-113-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Third quadrant, then reciprocate",
                    "problemId": "ibhl-113-t1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Divide in Euler form",
                    "problemId": "ibhl-113-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.13 in four lines",
                    "points": [
                        "$z = re^{i\\theta}$: $r = \\sqrt{a^2+b^2}$, $\\theta$ from a SKETCH, principal range $-\\pi < \\theta \\le \\pi$.",
                        "Multiply: moduli multiply, arguments add. Divide: divide, subtract.",
                        "Multiplying by $z$ rotates by $\\arg z$ and scales by $|z|$; by $i$ = quarter-turn.",
                        "Same product in both forms → exact values of $\\frac{\\pi}{12}$-style angles.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — AHL 1.14: De Moivre — powers, roots & the conjugate root theorem
# ===========================================================================
def lesson_de_moivre():
    return {
        "slug": "de-moivre-powers-and-roots",
        "title": "De Moivre: Powers & Roots",
        "concreteComparison": (
            "$(1+i)^8$ by expansion is eight rounds of algebra. In polar form it is one sentence: "
            "modulus $(\\sqrt{2})^8 = 16$, argument $8 \\times \\frac{\\pi}{4} = 2\\pi$ — answer "
            "$16$. And running the machine backwards splits a number into $n$ equally-spaced roots: "
            "a perfect polygon hiding inside every equation $z^n = w$."
        ),
        "objective": (
            "Use De Moivre's theorem to compute powers, derive trig identities, and find all $n$ "
            "n-th roots of a complex number; use the conjugate root theorem on real-coefficient "
            "polynomials."
        ),
        "concept": [
            "**Syllabus card — AHL 1.14.** De Moivre's theorem $(\\cos\\theta + i\\sin\\theta)^n = "
            "\\cos n\\theta + i\\sin n\\theta$ (its proof by induction belongs to AHL 1.15); powers "
            "and n-th roots of complex numbers; conjugate roots of polynomials with real "
            "coefficients. Papers 1 and 2. Weight: 6–9 marks — a Section B favourite.",
            "**Powers.** $z = re^{i\\theta} \\Rightarrow z^n = r^n e^{in\\theta}$: modulus to the "
            "power, argument times $n$. $(1+i)^8$: $r = \\sqrt{2}$, $\\theta = \\frac{\\pi}{4}$, so "
            "$z^8 = (\\sqrt2)^8 e^{2\\pi i} = 16$. Wrap the final argument back into "
            "$-\\pi < \\theta \\le \\pi$ before converting to Cartesian.",
            "**Identities for free.** Expand $(\\cos\\theta + i\\sin\\theta)^3$ two ways — "
            "binomially and by De Moivre — and equate real parts: $\\cos 3\\theta = 4\\cos^3\\theta "
            "- 3\\cos\\theta$. The imaginary parts hand you $\\sin 3\\theta$. One theorem, a whole "
            "identity factory.",
            "**Roots.** $z^n = w$ with $w = Re^{i\\phi}$ has EXACTLY $n$ solutions: "
            "$z_k = R^{1/n} e^{i(\\phi + 2\\pi k)/n}$ for $k = 0, 1, \\ldots, n-1$. All share "
            "modulus $R^{1/n}$; their arguments step by $\\frac{2\\pi}{n}$ — a regular $n$-gon on a "
            "circle. Forgetting the $+2\\pi k$ is forgetting $n-1$ of the answers.",
            "**Conjugate root theorem.** If a polynomial has REAL coefficients and $z_0$ is a root, "
            "then $z_0^*$ is a root too — complex roots hunt in mirror pairs. Given one root "
            "$2 + i$ of a real cubic, you immediately own $(z - (2+i))(z - (2-i)) = z^2 - 4z + 5$; "
            "divide it out and the last root falls out real. This is the exam's favourite way to "
            "hand you a cubic.",
        ],
        "keyIdea": (
            "$z^n = r^n e^{in\\theta}$ — powers in one line. Roots: $n$ of them, equally spaced, "
            "arguments $\\frac{\\phi + 2\\pi k}{n}$. Real coefficients → conjugate pairs."
        ),
        "facts": [
            {
                "title": "De Moivre's theorem",
                "latex": "(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta",
                "explanation": (
                    "NOT in the booklet — memorize. Valid for all $n \\in \\mathbb{Z}$ (and used for "
                    "rational $n$ in root-finding). Its induction proof is an AHL 1.15 exam classic."
                ),
            },
            {
                "title": "n-th roots",
                "latex": "z^n = Re^{i\\phi} \\;\\Rightarrow\\; z_k = R^{1/n} e^{i(\\phi + 2\\pi k)/n}, \\; k = 0, \\ldots, n-1",
                "explanation": (
                    "Memorize the $+2\\pi k$. The $n$ roots are equally spaced ($\\frac{2\\pi}{n}$ "
                    "apart) on the circle of radius $R^{1/n}$ — always a regular polygon."
                ),
            },
            {
                "title": "Conjugate root theorem",
                "latex": "P(z_0) = 0,\\ P \\text{ real coefficients} \\;\\Rightarrow\\; P(z_0^*) = 0",
                "explanation": (
                    "Complex roots of real polynomials come in conjugate pairs — so a real cubic has "
                    "either three real roots or one real root and one mirror pair."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-114-we1",
                "statement": (
                    "**(a)** Use De Moivre's theorem to show that $(1+i)^8 = 16$. **[4]**  \n"
                    "**(b)** Use the binomial expansion of $(\\cos\\theta + i\\sin\\theta)^3$ to show "
                    "that $\\cos 3\\theta = 4\\cos^3\\theta - 3\\cos\\theta$. **[5]**"
                ),
                "solution": (
                    "**(a)** $|1+i| = \\sqrt{2}$, $\\arg(1+i) = \\frac{\\pi}{4}$ *(A1 A1)*. By De "
                    "Moivre *(M1)*: $(1+i)^8 = (\\sqrt{2})^8\\,\\mathrm{cis}\\!\\left(8 \\cdot "
                    "\\frac{\\pi}{4}\\right) = 16\\,\\mathrm{cis}\\,2\\pi = 16$ *(AG)*.  \n"
                    "**(b)** Expand binomially *(M1)*: $(c + is)^3 = c^3 + 3c^2(is) + 3c(is)^2 + "
                    "(is)^3 = (c^3 - 3cs^2) + i(3c^2s - s^3)$ *(A1)*, writing $c = \\cos\\theta$, "
                    "$s = \\sin\\theta$. De Moivre says the same cube equals $\\cos 3\\theta + "
                    "i\\sin 3\\theta$ *(M1)*. Equate REAL parts *(R1)*: $\\cos 3\\theta = c^3 - "
                    "3cs^2$. Substitute $s^2 = 1 - c^2$:  \n"
                    "$$\\cos 3\\theta = c^3 - 3c(1 - c^2) = 4\\cos^3\\theta - 3\\cos\\theta \\;(AG)$$  \n"
                    "**Narrative:** the imaginary parts, for free, give $\\sin 3\\theta = 3s - 4s^3$. "
                    "On 'show that' parts the target is printed — your job is the unbroken chain to "
                    "it, and the R mark pays for SAYING 'equate real parts', not just doing it."
                ),
                "check": [
                    "Eq(expand((1 + I)**8), 16)",
                    "Eq(Abs(1 + I), sqrt(2))",
                    "Eq(arg(1 + I), pi/4)",
                    "Eq(sqrt(2)**8, 16)",
                    "Eq(expand_trig(cos(3*t)), 4*cos(t)**3 - 3*cos(t))",
                    "Eq(expand_trig(sin(3*t)), -4*sin(t)**3 + 3*sin(t))",
                ],
            },
            {
                "id": "ibhl-114-we2",
                "statement": (
                    "**(a)** Solve $z^3 = 8i$, giving your answers in the form $re^{i\\theta}$. **[4]**  \n"
                    "**(b)** Write the three roots in Cartesian form and verify that their sum is "
                    "zero. **[4]**"
                ),
                "solution": (
                    "**(a)** $8i = 8e^{i\\pi/2}$ *(A1)*. Roots *(M1)*: $z_k = 8^{1/3} "
                    "e^{i(\\pi/2 + 2\\pi k)/3} = 2e^{i(\\pi/6 + 2\\pi k/3)}$:  \n"
                    "$$z_0 = 2e^{i\\pi/6}, \\quad z_1 = 2e^{i5\\pi/6}, \\quad z_2 = 2e^{-i\\pi/2} "
                    "\\;(A1\\ A1)$$  \n"
                    "(the $k = 2$ argument $\\frac{3\\pi}{2}$ wraps to $-\\frac{\\pi}{2}$).  \n"
                    "**(b)** Convert *(M1)*: $z_0 = 2\\left(\\frac{\\sqrt3}{2} + \\frac{i}{2}\\right) "
                    "= \\sqrt{3} + i$; $z_1 = -\\sqrt{3} + i$; $z_2 = -2i$ *(A1 A1)*. Sum: "
                    "$(\\sqrt3 - \\sqrt3) + (1 + 1 - 2)i = 0$ ✓ *(A1)*.  \n"
                    "**Narrative:** the three roots sit $120°$ apart on the circle $|z| = 2$ — an "
                    "equilateral triangle balanced on its centroid, which is WHY the sum is zero "
                    "(true for the $n$-th roots of any number, $n \\ge 2$: the polygon's centre is "
                    "the origin)."
                ),
                "check": [
                    "Eq(expand((sqrt(3) + I)**3), 8*I)",
                    "Eq(expand((-sqrt(3) + I)**3), 8*I)",
                    "Eq((-2*I)**3, 8*I)",
                    "Eq(sqrt(3) + I + (-sqrt(3) + I) + (-2*I), 0)",
                    "Eq(Abs(sqrt(3) + I), 2)",
                    "Eq(arg(sqrt(3) + I), pi/6)",
                    "Eq(arg(-sqrt(3) + I), 5*pi/6)",
                ],
            },
            {
                "id": "ibhl-114-we3",
                "statement": (
                    "The polynomial $P(z) = z^3 - 7z^2 + 17z - 15$ has real coefficients, and "
                    "$z = 2 + i$ is a root.  \n"
                    "**(a)** Write down a second root of $P(z) = 0$. **[1]**  \n"
                    "**(b)** Find the third root. **[4]**"
                ),
                "solution": (
                    "**(a)** Real coefficients → conjugate pairs: $z = 2 - i$ *(A1)*.  \n"
                    "**(b)** The pair builds a real quadratic factor *(M1)*:  \n"
                    "$$(z - (2+i))(z - (2-i)) = z^2 - 4z + 5 \\;(A1)$$  \n"
                    "Divide (or compare coefficients) *(M1)*: $z^3 - 7z^2 + 17z - 15 = "
                    "(z^2 - 4z + 5)(z - 3)$, so the third root is $z = 3$ *(A1)*.  \n"
                    "**Narrative:** no long division needed if you look at the constant term: "
                    "$5 \\times c = 15 \\Rightarrow c = 3$ — comparing constants is the fast lane. "
                    "Check the $z^2$ coefficient: $-4 + (-3)\\cdot 1 = -7$ ✓."
                ),
                "check": [
                    "Eq(expand((z - (2 + I))*(z - (2 - I))), z**2 - 4*z + 5)",
                    "Eq(expand((z**2 - 4*z + 5)*(z - 3)), z**3 - 7*z**2 + 17*z - 15)",
                    "Eq(expand((2 + I)**3 - 7*(2 + I)**2 + 17*(2 + I) - 15), 0)",
                    "Eq(Rational(15, 5), 3)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Finding ONE cube root of $8i$ and stopping — the equation $z^3 = 8i$ promises three.",
                "correction": "Roots come from $\\frac{\\phi + 2\\pi k}{n}$ for $k = 0, \\ldots, n-1$: three $k$'s, three roots, $120°$ apart.",
                "authored": True,
            },
            {
                "text": "Applying the conjugate root theorem to a polynomial with a complex coefficient.",
                "correction": "The theorem NEEDS real coefficients — $z^2 - iz$ has roots $0$ and $i$, no conjugate pair in sight. Quote the hypothesis when you use it.",
                "authored": True,
            },
            {
                "text": "Leaving $z_2 = 2e^{3\\pi i/2}$ as a final answer.",
                "correction": "Wrap to the principal range: $\\frac{3\\pi}{2} - 2\\pi = -\\frac{\\pi}{2}$, so $z_2 = 2e^{-i\\pi/2} = -2i$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-114-t1",
                "statement": (
                    "Use De Moivre's theorem to evaluate $(\\sqrt{3} + i)^6$. **[4]**"
                ),
                "solution": (
                    "$|\\sqrt3 + i| = 2$, $\\arg = \\frac{\\pi}{6}$ *(A1 A1)*. Then "
                    "$(\\sqrt3 + i)^6 = 2^6\\,\\mathrm{cis}\\!\\left(6 \\cdot \\frac{\\pi}{6}\\right) "
                    "= 64\\,\\mathrm{cis}\\,\\pi$ *(M1)* $= -64$ *(A1)*. A sixth power collapsing to "
                    "a negative real number — the argument landed exactly on $\\pi$."
                ),
                "check": [
                    "Eq(Abs(sqrt(3) + I), 2)",
                    "Eq(arg(sqrt(3) + I), pi/6)",
                    "Eq(expand((sqrt(3) + I)**6), -64)",
                ],
            },
            {
                "id": "ibhl-114-t2",
                "statement": (
                    "Solve $z^4 = -16$, giving your answers in Cartesian form. **[5]**"
                ),
                "solution": (
                    "$-16 = 16e^{i\\pi}$ *(A1)*. Roots: $z_k = 2e^{i(\\pi + 2\\pi k)/4}$ *(M1)*: "
                    "arguments $\\frac{\\pi}{4}, \\frac{3\\pi}{4}, -\\frac{3\\pi}{4}, -\\frac{\\pi}{4}$ "
                    "*(A1)*. Since $2\\,\\mathrm{cis}(\\pm\\frac{\\pi}{4}) = \\sqrt2 (1 \\pm i)$ etc., "
                    "the four roots are $z = \\sqrt{2}(\\pm 1 \\pm i)$ *(A2)* — the corners of a "
                    "square. Note they form TWO conjugate pairs, as the real coefficients of "
                    "$z^4 + 16$ demand."
                ),
                "check": [
                    "Eq(expand((sqrt(2) + sqrt(2)*I)**4), -16)",
                    "Eq(expand((sqrt(2) - sqrt(2)*I)**4), -16)",
                    "Eq(expand((-sqrt(2) + sqrt(2)*I)**4), -16)",
                    "Eq(expand((-sqrt(2) - sqrt(2)*I)**4), -16)",
                    "Eq(Abs(sqrt(2) + sqrt(2)*I), 2)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.14 · Papers 1 & 2",
                    "title": "Powers in one line, roots as polygons",
                    "body": (
                        "De Moivre is polar multiplication run $n$ times: $z^n = r^n e^{in\\theta}$. "
                        "Forwards it crushes $(1+i)^8$ into arithmetic. Backwards it opens $z^n = w$ "
                        "into exactly $n$ roots, equally spaced — algebra's most photogenic theorem."
                    ),
                },
                {
                    "kind": "argandPlot",
                    "eyebrow": "Forwards",
                    "title": "The De Moivre spiral",
                    "teach": (
                        "Step the power $n$: each multiplication scales the modulus by $|z|$ and adds "
                        "$\\arg z$ to the angle. With $|z| = 1.1$ the powers spiral outwards; drop "
                        "$|z|$ below 1 and the spiral turns inwards. Read the caption: $|z^n| = |z|^n$ "
                        "and $\\arg(z^n) = n\\arg z$ — that pair of facts IS De Moivre."
                    ),
                    "config": {"mode": "powers", "r": 1.1, "thetaDeg": 30, "n": 6},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "One-line power",
                    "title": "Eighth power, no expansion",
                    "prompt": "Using $1 + i = \\sqrt{2}\\,e^{i\\pi/4}$, what is $(1+i)^8$?",
                    "options": ["$16$", "$16i$", "$-16$", "$8\\sqrt{2}$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$(\\sqrt2)^8 = 2^4 = 16$ and $8 \\cdot \\frac{\\pi}{4} = 2\\pi$ — a full "
                        "turn, back on the positive real axis. Modulus to the power, argument times "
                        "$n$."
                    ),
                    "check": [
                        "Eq(expand((1 + I)**8), 16)",
                        "Eq(8*pi/4, 2*pi)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A power and an identity factory",
                    "problemId": "ibhl-114-we1",
                },
                {
                    "kind": "argandPlot",
                    "eyebrow": "Backwards",
                    "title": "Roots are a regular polygon",
                    "teach": (
                        "Step $n$ and rotate the target $w$: the $n$-th roots of $w$ always form a "
                        "regular $n$-gon on the circle of radius $|w|^{1/n}$, first vertex at "
                        "$\\frac{\\arg w}{n}$, the rest every $\\frac{360°}{n}$. Solving $z^n = w$ "
                        "is drawing this polygon — the algebra just labels its corners."
                    ),
                    "config": {"mode": "roots", "n": 3, "targetDeg": 90},
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Three cube roots of 8i",
                    "problemId": "ibhl-114-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Count the roots",
                    "title": "How many, how far apart?",
                    "prompt": "The solutions of $z^5 = 32$ are:",
                    "options": [
                        "5 roots of modulus 2, spaced $72°$ apart",
                        "1 root: $z = 2$",
                        "5 roots of modulus 32, spaced $72°$ apart",
                        "5 roots of modulus 2, spaced $36°$ apart",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$32^{1/5} = 2$ gives the shared modulus; five roots share the circle at "
                        "$\\frac{360°}{5} = 72°$ spacing, starting from $z = 2$ on the real axis. "
                        "Only one is real — the other four hide as two conjugate pairs."
                    ),
                    "check": [
                        "Eq(2**5, 32)",
                        "Eq(Rational(360, 5), 72)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "One root given, two for free",
                    "problemId": "ibhl-114-we3",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "A sixth power collapses",
                    "problemId": "ibhl-114-t1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn — harder",
                    "title": "Four fourth roots of −16",
                    "problemId": "ibhl-114-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.14 in four lines",
                    "points": [
                        "$z^n = r^n e^{in\\theta}$ — then wrap the argument into $(-\\pi, \\pi]$.",
                        "$z^n = w$: exactly $n$ roots, modulus $|w|^{1/n}$, arguments $\\frac{\\arg w + 2\\pi k}{n}$ — a regular $n$-gon.",
                        "Expand $(c + is)^n$ two ways, equate parts → multiple-angle identities.",
                        "Real coefficients → complex roots in conjugate pairs; a known root gifts a real quadratic factor.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — AHL 1.15: Proof by induction, contradiction & counterexample
# ===========================================================================
def lesson_proof_methods():
    return {
        "slug": "induction-contradiction-counterexample",
        "title": "Proof: Induction, Contradiction, Counterexample",
        "concreteComparison": (
            "Induction is a ladder: prove you can reach rung 1, prove every rung lifts you to the "
            "next, and you own the whole ladder — infinitely many statements from two finite "
            "checks. Contradiction is the opposite art: assume the thing you doubt, and watch the "
            "assumption destroy itself."
        ),
        "objective": (
            "Write full-marks proofs by mathematical induction (sums and divisibility), by "
            "contradiction, and disprove claims with a single counterexample."
        ),
        "concept": [
            "**Syllabus card — AHL 1.15.** Proof by mathematical induction; proof by contradiction; "
            "use of a counterexample to show a statement is false. Paper 1 territory, 6–9 marks. "
            "Induction also certifies De Moivre (AHL 1.14) and later, derivative formulas "
            "(AHL 5.12).",
            "**Induction's four beats.** (1) BASE: verify the claim at $n = 1$ (or the stated "
            "start). (2) ASSUME the claim for $n = k$ — write it out fully. (3) STEP: prove it for "
            "$n = k+1$, and the assumption MUST be used visibly. (4) CONCLUDE with the ritual "
            "sentence: 'true for $n = 1$, and true for $n = k \\Rightarrow$ true for $n = k+1$; "
            "hence true for all $n \\in \\mathbb{Z}^+$ by induction.' The examiner pays R marks for "
            "beats 2 and 4 as WORDS — skipping the sentence costs marks even when the algebra is "
            "perfect.",
            "**Divisibility induction.** To show $9^n - 1$ is divisible by 8: assume $9^k - 1 = 8m$ "
            "for some $m \\in \\mathbb{Z}$. Then $9^{k+1} - 1 = 9 \\cdot 9^k - 1 = 9(9^k - 1) + 8 "
            "= 8(9m + 1)$ — the trick is always the same: peel one factor, re-express through the "
            "assumed multiple, and show the leftover is also a multiple.",
            "**Contradiction.** To prove $P$, assume NOT-$P$ and derive an impossibility. The "
            "classic: $\\sqrt{2} = \\frac{p}{q}$ in lowest terms $\\Rightarrow p^2 = 2q^2 "
            "\\Rightarrow p$ even $\\Rightarrow p = 2m \\Rightarrow q^2 = 2m^2 \\Rightarrow q$ even "
            "— but $\\frac{p}{q}$ was in lowest terms. Contradiction; $\\sqrt{2}$ is irrational. "
            "The phrase 'in lowest terms' is not scenery — it is the tripwire the contradiction "
            "trips.",
            "**Counterexample.** To DISPROVE a universal claim, one failing case suffices — and "
            "no number of confirming cases proves it. '$n^2 + n + 41$ is prime for all $n \\in "
            "\\mathbb{Z}^+$' survives $n = 1$ to $39$ and dies at $n = 40$: $40^2 + 40 + 41 = "
            "1681 = 41^2$. Checking is evidence; only proof is certainty — that asymmetry is the "
            "whole lesson.",
        ],
        "keyIdea": (
            "Induction: base, assume, step (using the assumption), ritual conclusion. "
            "Contradiction: assume the opposite, break mathematics. Disproof: one counterexample."
        ),
        "facts": [
            {
                "title": "Induction skeleton",
                "latex": "P(1) \\;\\wedge\\; \\big(P(k) \\Rightarrow P(k+1)\\big) \\;\\Rightarrow\\; P(n)\\ \\forall n \\in \\mathbb{Z}^+",
                "explanation": (
                    "No formula in the booklet — the STRUCTURE is the content. The conclusion "
                    "sentence is a scoring line (R1): write it verbatim, every time."
                ),
            },
            {
                "title": "Contradiction template",
                "latex": "\\text{Assume } \\neg P \\;\\rightsquigarrow\\; \\text{impossibility} \\;\\Rightarrow\\; P",
                "explanation": (
                    "State the assumption explicitly ('suppose, for contradiction, that…'), and "
                    "name the contradiction when it lands."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-115-we1",
                "statement": (
                    "Prove by mathematical induction that "
                    "$1 + 3 + 5 + \\cdots + (2n-1) = n^2$ for all $n \\in \\mathbb{Z}^+$. **[6]**"
                ),
                "solution": (
                    "**Base** $n = 1$: LHS $= 1$, RHS $= 1^2 = 1$ ✓ *(A1)*.  \n"
                    "**Assume** true for $n = k$: $1 + 3 + \\cdots + (2k-1) = k^2$ *(M1 — written "
                    "in full)*.  \n"
                    "**Step** $n = k+1$: the next odd number is $2(k+1) - 1 = 2k+1$ *(A1)*:  \n"
                    "$$1 + 3 + \\cdots + (2k-1) + (2k+1) = k^2 + (2k+1) \\;(M1\\ using\\ the\\ "
                    "assumption)$$"
                    "$$= k^2 + 2k + 1 = (k+1)^2 \\;(A1)$$  \n"
                    "which is the claim at $n = k+1$.  \n"
                    "**Conclusion:** true for $n = 1$; true for $n = k$ implies true for $n = k+1$; "
                    "therefore true for all $n \\in \\mathbb{Z}^+$ by mathematical induction *(R1)*.  \n"
                    "**Narrative:** the only creative move is recognizing $k^2 + 2k + 1$ as a "
                    "perfect square — everything else is scaffolding. But the scaffolding IS the "
                    "marks: the R1 dies without the closing sentence, and the M1 dies if the "
                    "assumption never appears in the algebra."
                ),
                "check": [
                    "Eq(Sum(2*k - 1, (k, 1, n)).doit(), n**2)",
                    "Eq(2*1 - 1, 1**2)",
                    "Eq(expand(k**2 + 2*k + 1), expand((k + 1)**2))",
                    "Eq(2*(k + 1) - 1, 2*k + 1)",
                ],
            },
            {
                "id": "ibhl-115-we2",
                "statement": (
                    "Prove by mathematical induction that $9^n - 1$ is divisible by 8 for all "
                    "$n \\in \\mathbb{Z}^+$. **[6]**"
                ),
                "solution": (
                    "**Base** $n = 1$: $9^1 - 1 = 8$, divisible by 8 ✓ *(A1)*.  \n"
                    "**Assume** for $n = k$: $9^k - 1 = 8m$ for some $m \\in \\mathbb{Z}$ *(M1)*.  \n"
                    "**Step**: $9^{k+1} - 1 = 9 \\cdot 9^k - 1$ *(M1)*  \n"
                    "$$= 9(9^k - 1) + 9 - 1 = 9(8m) + 8 \\;(A1)$$"
                    "$$= 8(9m + 1) \\;(A1)$$  \n"
                    "which is a multiple of 8 since $9m + 1 \\in \\mathbb{Z}$.  \n"
                    "**Conclusion:** true for $n = 1$ and inherited from $k$ to $k+1$, so true for "
                    "all $n \\in \\mathbb{Z}^+$ by induction *(R1)*.  \n"
                    "**Narrative:** the pivot line $9 \\cdot 9^k - 1 = 9(9^k - 1) + 8$ is the whole "
                    "proof — add and subtract what the assumption knows. The same peel-one-factor "
                    "move handles every divisibility induction on the paper."
                ),
                "check": [
                    "Eq(9**1 - 1, 8)",
                    "simplify(9*(9**k - 1) + 8 - (9**(k + 1) - 1)) == 0",
                    "Eq(9*8*m + 8, 8*(9*m + 1))",
                    "(9**5 - 1) % 8 == 0",
                    "(9**7 - 1) % 8 == 0",
                ],
            },
            {
                "id": "ibhl-115-we3",
                "statement": (
                    "Prove by contradiction that $\\sqrt{2}$ is irrational. **[6]**"
                ),
                "solution": (
                    "Suppose, for contradiction, that $\\sqrt{2} = \\dfrac{p}{q}$ with $p, q \\in "
                    "\\mathbb{Z}$, $q \\ne 0$, and the fraction in LOWEST terms *(M1 — assumption "
                    "stated with the lowest-terms clause)*.  \n"
                    "Squaring: $2q^2 = p^2$ *(A1)*, so $p^2$ is even, hence $p$ is even *(R1 — odd² "
                    "is odd)*. Write $p = 2m$ *(M1)*:  \n"
                    "$$2q^2 = 4m^2 \\;\\Rightarrow\\; q^2 = 2m^2 \\;(A1)$$  \n"
                    "so $q$ is even too. Then $p$ and $q$ share the factor 2 — contradicting lowest "
                    "terms. Hence no such fraction exists: $\\sqrt{2}$ is irrational *(R1)*.  \n"
                    "**Narrative:** both R marks are SENTENCES: why $p$ must be even, and what "
                    "exactly contradicts what. A proof that computes but never says 'contradiction "
                    "with the lowest-terms assumption' leaves the last mark on the table."
                ),
                "check": [
                    "sqrt(2).is_rational == False",
                    "Eq((2*m)**2, 4*m**2)",
                    "Eq(expand(2*q**2 - (2*m)**2), 2*q**2 - 4*m**2)",
                    "Eq((2*3 + 1)**2 % 2, 1)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Omitting the concluding sentence of an induction — or writing 'proven' without naming the two ingredients.",
                "correction": "The ritual earns R1: 'true for $n=1$; true for $k$ ⟹ true for $k+1$; hence true for all $n \\in \\mathbb{Z}^+$ by induction.'",
                "authored": True,
            },
            {
                "text": "An inductive step that never USES the assumption — re-deriving the sum from scratch proves nothing.",
                "correction": "The assumed identity must visibly enter: replace $1 + 3 + \\cdots + (2k-1)$ by $k^2$ and SAY 'by the inductive hypothesis'.",
                "authored": True,
            },
            {
                "text": "Trying to prove '$2^n > n^2$ for all $n$' — and pushing induction through a false claim.",
                "correction": "Test small cases FIRST: $n = 2$ gives $4 = 4$, $n = 3$ gives $8 < 9$ — the claim fails; a counterexample settles it. Induction can only prove what is true.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-115-t1",
                "statement": (
                    "Prove by mathematical induction that "
                    "$\\displaystyle\\sum_{r=1}^{n} r \\cdot r! = (n+1)! - 1$ for all "
                    "$n \\in \\mathbb{Z}^+$. **[6]**"
                ),
                "solution": (
                    "**Base** $n=1$: LHS $= 1 \\cdot 1! = 1$; RHS $= 2! - 1 = 1$ ✓ *(A1)*. "
                    "**Assume** $\\sum_{r=1}^{k} r \\cdot r! = (k+1)! - 1$ *(M1)*. **Step**: add "
                    "the next term *(M1)*: $(k+1)! - 1 + (k+1)(k+1)! = (k+1)!\\,(1 + k + 1) - 1$ "
                    "*(A1)* $= (k+2)! - 1$ *(A1)* — the claim at $n = k+1$. **Conclusion** by "
                    "induction *(R1)*. The factor-out move $(k+1)!(k+2) = (k+2)!$ is the step's "
                    "only idea."
                ),
                "check": [
                    "Eq(1*factorial(1), factorial(2) - 1)",
                    "Eq(Sum(r*factorial(r), (r, 1, 5)).doit(), factorial(6) - 1)",
                    "Eq(expand((factorial(4))*(1 + 3 + 1)), expand(factorial(5)))",
                    "Eq(Sum(r*factorial(r), (r, 1, 8)).doit(), factorial(9) - 1)",
                ],
            },
            {
                "id": "ibhl-115-t2",
                "statement": (
                    "**(a)** Show that the statement '$2^n + 1$ is prime for all $n \\in "
                    "\\mathbb{Z}^+$' is false. **[2]**  \n"
                    "**(b)** Prove by contradiction that there is no largest even integer. **[4]**"
                ),
                "solution": (
                    "**(a)** $n = 3$: $2^3 + 1 = 9 = 3 \\times 3$, not prime *(A1 counterexample, "
                    "A1 shown composite)*. One failure kills a 'for all'.  \n"
                    "**(b)** Suppose, for contradiction, that $N$ is the largest even integer "
                    "*(M1)*. Then $N + 2$ is an integer, it is even (sum of evens) *(A1)*, and "
                    "$N + 2 > N$ *(A1)* — contradicting the maximality of $N$. Hence no largest "
                    "even integer exists *(R1)*. The proof manufactures a bigger witness from the "
                    "assumed champion — the standard 'no largest…' template."
                ),
                "check": [
                    "Eq(2**3 + 1, 9)",
                    "Eq(9, 3*3)",
                    "isprime(9) == False",
                    "Eq((2*m + 2) - 2*m, 2)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.15 · Paper 1",
                    "title": "Three weapons, one asymmetry",
                    "body": (
                        "A universal claim needs PROOF to stand and one COUNTEREXAMPLE to fall — "
                        "that asymmetry runs the whole lesson. Induction proves infinitely many "
                        "statements with two finite checks; contradiction proves by controlled "
                        "demolition; and no pile of confirming cases ever substitutes for either."
                    ),
                },
                {
                    "kind": "conjectureTest",
                    "eyebrow": "Evidence is not proof",
                    "title": "A conjecture that survives 39 rounds",
                    "teach": (
                        "Euler's polynomial $n^2 + n + 41$ churns out primes with terrifying "
                        "consistency — tap through the cases. Thirty-nine successes feel like "
                        "certainty. They are not: watch $n = 40$. This is WHY the syllabus demands "
                        "proof, and why 'I checked many values' earns zero marks."
                    ),
                    "config": {
                        "conjecture": "n² + n + 41 is prime for every positive integer n.",
                        "items": [
                            {"label": "n = 1: 43", "holds": True, "note": "Prime ✓ — promising."},
                            {"label": "n = 10: 151", "holds": True, "note": "Prime ✓ — still holding."},
                            {"label": "n = 39: 1601", "holds": True, "note": "Prime ✓ — 39 straight wins."},
                            {"label": "n = 40: 1681 = 41²", "holds": False, "note": "Composite ✗ — one counterexample ends it."},
                        ],
                    },
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Kill a claim",
                    "title": "Choose the counterexample",
                    "prompt": "Which single value disproves '$2^n + 1$ is prime for all $n \\in \\mathbb{Z}^+$'?",
                    "options": ["$n = 3$", "$n = 1$", "$n = 2$", "$n = 4$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$2^3 + 1 = 9 = 3^2$ — composite. ($n = 1, 2, 4$ give $3, 5, 17$: all "
                        "prime, all useless for disproof.) One counterexample suffices; also note "
                        "$n = 4$ WORKING doesn't rescue the claim."
                    ),
                    "check": [
                        "Eq(2**3 + 1, 9)",
                        "isprime(9) == False",
                        "isprime(2**4 + 1) == True",
                    ],
                },
                {
                    "kind": "stepProof",
                    "eyebrow": "The ladder",
                    "title": "Induction, beat by beat",
                    "teach": (
                        "Step through the four beats on the odd-number sum. Watch WHERE the "
                        "assumption enters the algebra — an inductive step that never uses $P(k)$ "
                        "proves nothing, and the examiner checks for exactly that."
                    ),
                    "config": {
                        "given": "$P(n)$: $1 + 3 + \\cdots + (2n-1) = n^2$",
                        "prove": "$P(n)$ holds for all $n \\in \\mathbb{Z}^+$",
                        "rows": [
                            {"statement": "$n = 1$: LHS $= 1 = 1^2 =$ RHS", "reason": "Base case verified"},
                            {"statement": "Assume $1 + 3 + \\cdots + (2k-1) = k^2$", "reason": "Inductive hypothesis, written in full"},
                            {"statement": "$1 + \\cdots + (2k-1) + (2k+1) = k^2 + 2k + 1$", "reason": "Add the next odd term; USE the hypothesis"},
                            {"statement": "$k^2 + 2k + 1 = (k+1)^2$", "reason": "Perfect square — this is $P(k+1)$"},
                            {"statement": "True for all $n \\in \\mathbb{Z}^+$", "reason": "Base + inheritance ⟹ induction (the R-mark sentence)"},
                        ],
                    },
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "The odd-number staircase",
                    "problemId": "ibhl-115-we1",
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Divisibility: peel one factor",
                    "problemId": "ibhl-115-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The pivot line",
                    "title": "Spot the inductive move",
                    "prompt": (
                        "In proving $9^{k+1} - 1$ divisible by 8, which rewrite lets the assumption "
                        "$9^k - 1 = 8m$ enter?"
                    ),
                    "options": [
                        "$9^{k+1} - 1 = 9(9^k - 1) + 8$",
                        "$9^{k+1} - 1 = 9^k \\cdot 9 - 9^k$",
                        "$9^{k+1} - 1 = (9-1)(9^k + \\cdots)$",
                        "$9^{k+1} - 1 = 9^{k+1} - 9 + 8$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$9 \\cdot 9^k - 1 = 9(9^k - 1) + 9 - 1$: the bracket is exactly the "
                        "assumed multiple of 8, and the leftover $+8$ is one too. (The factored "
                        "form in option C also works but proves divisibility by 8 the long way "
                        "round.)"
                    ),
                    "check": [
                        "simplify(9*(9**k - 1) + 8 - (9**(k + 1) - 1)) == 0",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "√2, by demolition",
                    "problemId": "ibhl-115-we3",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn — harder",
                    "title": "A factorial staircase",
                    "problemId": "ibhl-115-t1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "One kill, one demolition",
                    "problemId": "ibhl-115-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.15 in four lines",
                    "points": [
                        "Induction: base, full written assumption, step that USES it, ritual conclusion (R1).",
                        "Divisibility: peel one factor and re-express through the assumed multiple.",
                        "Contradiction: state the negation, name the impossibility when it lands.",
                        "Disproof: one counterexample; confirming cases prove nothing.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 7 — AHL 1.16: Systems of linear equations
# ===========================================================================
def lesson_linear_systems():
    return {
        "slug": "systems-of-linear-equations",
        "title": "Systems of Linear Equations",
        "concreteComparison": (
            "Three planes in space can meet like three pages at a book's spine-corner (one point), "
            "like pages sharing the spine itself (a whole line of solutions), or like a triangular "
            "prism's faces (no common point at all). Solving a 3×3 system is discovering which of "
            "the three pictures you are in."
        ),
        "objective": (
            "Solve systems of up to three linear equations in three unknowns by elimination, "
            "recognise unique / infinite / no-solution cases (including with a parameter), and "
            "interpret them geometrically."
        ),
        "concept": [
            "**Syllabus card — AHL 1.16.** Systems of linear equations, up to three equations in "
            "three unknowns: unique solution, infinitely many solutions, or none. Papers 1 and 2. "
            "Weight: 5–8 marks; the parameter version ('find $k$ such that…') is a Paper 1 "
            "regular.",
            "**Elimination with an audit trail.** Label the equations $R_1, R_2, R_3$ and write "
            "every move: $R_2 - 2R_1 \\to R_2'$. Kill $x$ from two pairs, then $y$ from the "
            "resulting pair — triangular form, back-substitute. The labels are not bureaucracy: "
            "on a 6-mark question the method marks live in them.",
            "**Three endings.** Triangular form ends one of three ways. A row $cz = d$ with "
            "$c \\ne 0$: UNIQUE solution. A row $0 = 0$: the third equation was dependent — "
            "INFINITELY many solutions, one free parameter. A row $0 = d \\ne 0$: INCONSISTENT, "
            "no solutions. The ending is a fact you must NAME, not just notice.",
            "**Parametrising a line.** In the infinite case, set the free unknown $z = t$ and "
            "express the rest: $(x, y, z) = (-2 + t,\\ 3 - 2t,\\ t)$ — a LINE in space, written "
            "as a point plus a direction. HL vectors (AHL 3.14) will call this "
            "$\\mathbf{r} = \\mathbf{a} + t\\mathbf{d}$; the algebra is already here.",
            "**Geometry of the three endings.** Unique = three planes meeting at a point (the "
            "book-corner). Infinite = three planes sharing a line (a sheaf, like pages sharing a "
            "spine). None = parallel planes, or the triangular-prism configuration — pairwise "
            "intersections, no common point. Exam questions ask for the picture by name; have "
            "all three ready.",
        ],
        "keyIdea": (
            "Eliminate to triangular form with labelled row moves. Last row tells the story: "
            "$cz = d$ → point; $0 = 0$ → line (parametrise with $t$); $0 = d$ → nothing."
        ),
        "facts": [
            {
                "title": "The three cases",
                "latex": "cz = d \\Rightarrow \\text{unique}; \\quad 0 = 0 \\Rightarrow \\text{infinite (line)}; \\quad 0 = d \\ne 0 \\Rightarrow \\text{none}",
                "explanation": (
                    "Read off the last row of triangular form. No booklet entry — the method IS "
                    "the content. Geometric names: point / sheaf of planes through a line / "
                    "prism (or parallel planes)."
                ),
            },
            {
                "title": "Parametric line of solutions",
                "latex": "(x, y, z) = (x_0, y_0, z_0) + t(d_1, d_2, d_3), \\quad t \\in \\mathbb{R}",
                "explanation": (
                    "In the infinite case set the free variable to $t$ and back-substitute. This "
                    "is the vector line equation of AHL 3.14, met early."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-116-we1",
                "statement": (
                    "Solve the system  \n"
                    "$$x + y + z = 6$$  \n"
                    "$$2x - y + z = 3$$  \n"
                    "$$x + 2y - z = 2$$ **[5]**"
                ),
                "solution": (
                    "$R_2 - 2R_1$: $-3y - z = -9$, i.e. $3y + z = 9$ *(M1 A1)*.  \n"
                    "$R_3 - R_1$: $y - 2z = -4$ *(A1)*.  \n"
                    "From the first new row $z = 9 - 3y$; substitute *(M1)*: $y - 2(9 - 3y) = -4 "
                    "\\Rightarrow 7y = 14 \\Rightarrow y = 2$, then $z = 3$, and $R_1$ gives "
                    "$x = 1$ *(A1)*.  \n"
                    "$$\\boxed{(x, y, z) = (1, 2, 3)}$$  \n"
                    "**Narrative:** always spend ten seconds checking in an UNUSED equation: "
                    "$R_2$: $2(1) - 2 + 3 = 3$ ✓. Three planes meeting at the single point "
                    "$(1, 2, 3)$ — the generic ending, but never assume it before the algebra "
                    "says so."
                ),
                "check": [
                    "solve([Eq(x + y + z, 6), Eq(2*x - y + z, 3), Eq(x + 2*y - z, 2)], [x, y, z]) == {x: 1, y: 2, z: 3}",
                    "Eq(1 + 2 + 3, 6)",
                    "Eq(2*1 - 2 + 3, 3)",
                    "Eq(1 + 2*2 - 3, 2)",
                ],
            },
            {
                "id": "ibhl-116-we2",
                "statement": (
                    "Consider the system  \n"
                    "$$x + y + z = 1$$  \n"
                    "$$x + 2y + 3z = 4$$  \n"
                    "$$x + 3y + 5z = k$$  \n"
                    "**(a)** Find the value of $k$ for which the system has solutions. **[4]**  \n"
                    "**(b)** For this value of $k$, solve the system, giving your answer in the "
                    "form $(x, y, z) = (a, b, c) + t(d_1, d_2, d_3)$. **[4]**  \n"
                    "**(c)** Describe the configuration of the three planes. **[1]**"
                ),
                "solution": (
                    "**(a)** $R_2 - R_1$: $y + 2z = 3$ *(A1)*. $R_3 - R_2$: $y + 2z = k - 4$ "
                    "*(A1)*. Subtracting these twins *(M1)*: $0 = k - 7$, so solutions exist only "
                    "for $k = 7$ *(A1)* — any other $k$ makes the last row $0 = $ nonzero: "
                    "inconsistent.  \n"
                    "**(b)** With $k = 7$ the system collapses to two equations. Set $z = t$ "
                    "*(M1)*: $y = 3 - 2t$ *(A1)*, and $R_1$: $x = 1 - y - z = -2 + t$ *(A1)*:  \n"
                    "$$(x, y, z) = (-2, 3, 0) + t(1, -2, 1) \\;(A1)$$  \n"
                    "**(c)** The three planes form a SHEAF — they share the common line above "
                    "*(A1)*.  \n"
                    "**Narrative:** check the parametric line in $R_2$ for ALL $t$: "
                    "$(-2+t) + 2(3-2t) + 3t = 4$ ✓ — the $t$'s cancel, which is exactly what "
                    "'the whole line solves the system' means. For $k \\ne 7$ the planes make a "
                    "prism: pairwise lines of intersection, all parallel, no common point."
                ),
                "check": [
                    "Eq(expand((-2 + t) + (3 - 2*t) + t), 1)",
                    "Eq(expand((-2 + t) + 2*(3 - 2*t) + 3*t), 4)",
                    "Eq(expand((-2 + t) + 3*(3 - 2*t) + 5*t), 7)",
                    "Eq(3 - (k - 4), 7 - k)",
                    "solve(Eq(3, k - 4), k) == [7]",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Unlabelled row operations — a page of arithmetic with no $R_2 - 2R_1$ trail.",
                "correction": "Label every move. When a sign slips (it will), the trail is what lets you — and the examiner — find the surviving marks.",
                "authored": True,
            },
            {
                "text": "Reading the row $0 = 0$ as 'no solutions'.",
                "correction": "$0 = 0$ means a REDUNDANT equation: infinitely many solutions along a line. 'No solutions' is $0 = d$ with $d \\ne 0$. Opposite verdicts.",
                "authored": True,
            },
            {
                "text": "In the infinite case, stopping at 'infinitely many solutions' when the question says 'solve'.",
                "correction": "Parametrise: set $z = t$, back-substitute, and present $(x, y, z) = \\mathbf{a} + t\\mathbf{d}$. The line IS the answer.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-116-t1",
                "statement": (
                    "Solve the system  \n"
                    "$$2x + y - z = 1$$  \n"
                    "$$x - y + 2z = 5$$  \n"
                    "$$3x + 2y + z = 10$$ **[5]**"
                ),
                "solution": (
                    "$R_1 + R_2$: $3x + z = 6$ *(M1 A1)*. $2R_2 + R_3$: $5x + 5z = 20$, i.e. "
                    "$x + z = 4$ *(A1)*. Subtract: $2x = 2 \\Rightarrow x = 1$, $z = 3$, and "
                    "$R_2$ gives $y = x + 2z - 5 = 2$ *(A1)*. So $(x, y, z) = (1, 2, 3)$ *(A1)*. "
                    "Check in $R_3$: $3 + 4 + 3 = 10$ ✓."
                ),
                "check": [
                    "solve([Eq(2*x + y - z, 1), Eq(x - y + 2*z, 5), Eq(3*x + 2*y + z, 10)], [x, y, z]) == {x: 1, y: 2, z: 3}",
                    "Eq(2*1 + 2 - 3, 1)",
                    "Eq(1 - 2 + 2*3, 5)",
                    "Eq(3*1 + 2*2 + 3, 10)",
                ],
            },
            {
                "id": "ibhl-116-t2",
                "statement": (
                    "Find the values of $a$ and $b$ for which the system  \n"
                    "$$x + 2y - z = 3$$  \n"
                    "$$2x + 5y + z = 10$$  \n"
                    "$$3x + 7y + az = b$$  \n"
                    "has infinitely many solutions. **[6]**"
                ),
                "solution": (
                    "$R_2 - 2R_1$: $y + 3z = 4$ *(M1 A1)*. $R_3 - 3R_1$: $y + (a+3)z = b - 9$ "
                    "*(A1)*. Infinitely many requires this row to DUPLICATE the previous one "
                    "*(M1)*: $a + 3 = 3$ and $b - 9 = 4$, so $a = 0$, $b = 13$ *(A1 A1)*. "
                    "(Then $z = t$, $y = 4 - 3t$, $x = 3 - 2y + z = -5 + 7t$ — the shared line. "
                    "$a = 0$ is legal: the third plane simply has no $z$-tilt.)"
                ),
                "check": [
                    "solve(Eq(a + 3, 3), a) == [0]",
                    "solve(Eq(b - 9, 4), b) == [13]",
                    "Eq(expand((-5 + 7*t) + 2*(4 - 3*t) - t), 3)",
                    "Eq(expand(2*(-5 + 7*t) + 5*(4 - 3*t) + t), 10)",
                    "Eq(expand(3*(-5 + 7*t) + 7*(4 - 3*t) + 0*t), 13)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 1.16 · Papers 1 & 2",
                    "title": "Three planes, three endings",
                    "body": (
                        "Every 3×3 linear system is a geometry question in disguise: three planes "
                        "either pin down one point, share a whole line, or miss each other "
                        "entirely. Elimination is how the algebra confesses which — and the exam "
                        "wants the ending NAMED, not just computed."
                    ),
                },
                {
                    "kind": "systemGraph",
                    "eyebrow": "Warm up in 2D",
                    "title": "Two lines first",
                    "teach": (
                        "Steer the second line: cross (one solution), parallel (none), or the "
                        "same line (infinitely many). These are the 2D shadows of the three 3×3 "
                        "endings — one dimension up, 'same line' becomes 'planes sharing a line', "
                        "and 'parallel' grows a third possibility: the triangular prism."
                    ),
                    "config": {"m1": 1, "b1": 1, "m2": -1, "b2": 3, "interactive": True},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the last row",
                    "title": "Triangular form speaks",
                    "prompt": (
                        "Elimination leaves the rows $x + y + z = 1$, $y + 2z = 3$, $0 = 5$. "
                        "The system has:"
                    ),
                    "options": [
                        "no solutions — the planes have no common point",
                        "the unique solution $z = 5$",
                        "infinitely many solutions",
                        "the solution $(1, 3, 5)$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$0 = 5$ is false for EVERY $(x, y, z)$ — inconsistent, nothing solves "
                        "it. ($0 = 0$ would have meant infinitely many; a row $cz = d$, unique.)"
                    ),
                    "check": [
                        "Eq(5 - 0, 5)",
                        "(0 == 5) == False",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "The book-corner: one point",
                    "problemId": "ibhl-116-we1",
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A parameter decides the ending",
                    "problemId": "ibhl-116-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Name the picture",
                    "title": "Which configuration?",
                    "prompt": (
                        "A 3×3 system reduces to $y + 2z = 3$ appearing TWICE (and one original "
                        "row). Geometrically the three planes:"
                    ),
                    "options": [
                        "share a common line — a sheaf",
                        "meet at exactly one point",
                        "are all parallel",
                        "form a triangular prism",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "A duplicated row means only two independent planes — their intersection "
                        "line lies in all three. That is the sheaf (pages sharing a spine). The "
                        "prism happens when the last row turns into $0 = d \\ne 0$."
                    ),
                    "check": [
                        "Eq(3 - 3, 0)",
                    ],
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Eliminate to a point",
                    "problemId": "ibhl-116-t1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn — harder",
                    "title": "Force the sheaf",
                    "problemId": "ibhl-116-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 1.16 in four lines",
                    "points": [
                        "Labelled row operations → triangular form; check the answer in an unused equation.",
                        "Last row: $cz = d$ point · $0 = 0$ line · $0 = d \\ne 0$ nothing.",
                        "Infinite case: set $z = t$, present the line $(x,y,z) = \\mathbf{a} + t\\mathbf{d}$.",
                        "Geometry by name: book-corner point, sheaf through a line, prism with no common point.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Unit banks — HL practice + test-yourself, tagged with official AHL codes
# ===========================================================================
def practice_bank():
    return [
        {
            "id": "ibhl-na-p01",
            "statement": (
                "Find the number of arrangements of the seven letters of the word COMBINE in "
                "which the three vowels are all together. **[3]**"
            ),
            "solution": (
                "Glue O, I, E into one block: 5 units arrange in $5!$ ways *(M1)*, the vowels "
                "arrange inside the block in $3!$ ways *(A1)*: $5! \\times 3! = 120 \\times 6 = "
                "720$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.10", 3, "P1"),
            "check": [
                "factorial(5)*factorial(3) == 720",
            ],
        },
        {
            "id": "ibhl-na-p02",
            "statement": (
                "Find the coefficient of $x^2$ in the expansion of $(1-2x)^{-3}$, and state the "
                "values of $x$ for which the expansion is valid. **[4]**"
            ),
            "solution": (
                "$\\binom{-3}{2}(-2x)^2 = \\dfrac{(-3)(-4)}{2!} \\cdot 4x^2 = 6 \\cdot 4x^2$ "
                "*(M1 A1)*: coefficient $24$ *(A1)*. Valid for $|2x| < 1$, i.e. "
                "$|x| < \\tfrac{1}{2}$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.10", 4, "P1"),
            "check": [
                "binomial(-3, 2)*(-2)**2 == 24",
                "Eq(series((1 - 2*x)**(-3), x, 0, 3).removeO(), 24*x**2 + 6*x + 1)",
            ],
        },
        {
            "id": "ibhl-na-p03",
            "statement": (
                "Express $\\dfrac{3x+11}{(x-3)(x+1)}$ in partial fractions. **[4]**"
            ),
            "solution": (
                "$3x + 11 \\equiv A(x+1) + B(x-3)$ *(M1)*. $x = 3$: $20 = 4A \\Rightarrow A = 5$ "
                "*(A1)*. $x = -1$: $8 = -4B \\Rightarrow B = -2$ *(A1)*. So "
                "$\\dfrac{5}{x-3} - \\dfrac{2}{x+1}$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.11", 4, "P1"),
            "check": [
                "Eq(3*3 + 11, 20)",
                "Eq(3*(-1) + 11, 8)",
                "simplify((3*x + 11)/((x - 3)*(x + 1)) - (5/(x - 3) - 2/(x + 1))) == 0",
            ],
        },
        {
            "id": "ibhl-na-p04",
            "statement": (
                "Given $z = (2 + 5i)(4 - 3i)$, find $z$ in Cartesian form and verify that "
                "$|z| = |2+5i|\\,|4-3i|$. **[4]**"
            ),
            "solution": (
                "$z = 8 - 6i + 20i - 15i^2 = 23 + 14i$ *(M1 A1)*. $|z| = \\sqrt{23^2 + 14^2} = "
                "\\sqrt{725}$ *(A1)*; and $|2+5i||4-3i| = \\sqrt{29}\\sqrt{25} = 5\\sqrt{29} = "
                "\\sqrt{725}$ ✓ *(A1)* — moduli multiply."
            ),
            "badges": code_badge("ib-aa-hl-1.12", 4, "P1"),
            "check": [
                "Eq(expand((2 + 5*I)*(4 - 3*I)), 23 + 14*I)",
                "Eq(23**2 + 14**2, 725)",
                "Eq(Abs(2 + 5*I)*Abs(4 - 3*I), sqrt(725))",
                "Eq(5*sqrt(29), sqrt(725))",
            ],
        },
        {
            "id": "ibhl-na-p05",
            "statement": (
                "Solve $z^2 + 6z + 13 = 0$, and state the geometric relationship between the two "
                "roots on an Argand diagram. **[4]**"
            ),
            "solution": (
                "$z = \\dfrac{-6 \\pm \\sqrt{36 - 52}}{2} = \\dfrac{-6 \\pm 4i}{2}$ *(M1 A1)* "
                "$= -3 \\pm 2i$ *(A1)*. They are a conjugate pair — mirror images in the real "
                "axis *(A1)*, as real coefficients demand."
            ),
            "badges": code_badge("ib-aa-hl-1.12", 4, "P1"),
            "check": [
                "Eq(expand((-3 + 2*I)**2 + 6*(-3 + 2*I) + 13), 0)",
                "Eq(expand((-3 - 2*I)**2 + 6*(-3 - 2*I) + 13), 0)",
                "Eq(36 - 52, -16)",
            ],
        },
        {
            "id": "ibhl-na-p06",
            "statement": (
                "Express $z = -1 + i$ in the form $re^{i\\theta}$, $-\\pi < \\theta \\le \\pi$, "
                "and hence find $z^{10}$ in Cartesian form. **[6]**"
            ),
            "solution": (
                "$r = \\sqrt{2}$, second quadrant: $\\theta = \\dfrac{3\\pi}{4}$ *(A1 A1)*. "
                "$z^{10} = (\\sqrt2)^{10} e^{i \\cdot 30\\pi/4} = 32\\,e^{i 15\\pi/2}$ *(M1 A1)*. "
                "Wrap: $\\frac{15\\pi}{2} - 8\\pi = -\\frac{\\pi}{2}$ *(A1)*, so "
                "$z^{10} = 32e^{-i\\pi/2} = -32i$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.13", 6, "P1"),
            "check": [
                "Eq(Abs(-1 + I), sqrt(2))",
                "Eq(arg(-1 + I), 3*pi/4)",
                "Eq(expand((-1 + I)**10), -32*I)",
                "Eq(sqrt(2)**10, 32)",
            ],
        },
        {
            "id": "ibhl-na-p07",
            "statement": (
                "Prove by mathematical induction that $\\displaystyle\\sum_{r=1}^{n} r = "
                "\\frac{n(n+1)}{2}$ for all $n \\in \\mathbb{Z}^+$. **[6]**"
            ),
            "solution": (
                "**Base** $n=1$: LHS $=1$, RHS $= \\frac{1 \\cdot 2}{2} = 1$ ✓ *(A1)*. "
                "**Assume** $\\sum_{r=1}^{k} r = \\frac{k(k+1)}{2}$ *(M1)*. **Step**: add "
                "$(k+1)$ *(M1)*: $\\frac{k(k+1)}{2} + (k+1) = (k+1)\\left(\\frac{k}{2} + 1\\right) "
                "= \\frac{(k+1)(k+2)}{2}$ *(A1 A1)* — the claim at $k+1$. **Conclusion** by "
                "induction *(R1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.15", 6, "P1"),
            "check": [
                "Eq(Sum(r, (r, 1, n)).doit(), expand(n*(n + 1)/2))",
                "Eq(expand(k*(k + 1)/2 + (k + 1)), expand((k + 1)*(k + 2)/2))",
                "Eq(Rational(1*2, 2), 1)",
            ],
        },
        {
            "id": "ibhl-na-p08",
            "statement": (
                "Solve the system $x + y + z = 2$, $\\;2x + y - z = 1$, $\\;x - y + 2z = 3$. **[5]**"
            ),
            "solution": (
                "$R_2 - 2R_1$: $-y - 3z = -3$, i.e. $y + 3z = 3$ *(M1 A1)*. $R_3 - R_1$: "
                "$-2y + z = 1$ *(A1)*. From the first: $y = 3 - 3z$; substitute: "
                "$-2(3 - 3z) + z = 1 \\Rightarrow 7z = 7 \\Rightarrow z = 1$, $y = 0$, $x = 1$ "
                "*(A1)*. $(x, y, z) = (1, 0, 1)$ *(A1)*; check $R_2$: $2 + 0 - 1 = 1$ ✓."
            ),
            "badges": code_badge("ib-aa-hl-1.16", 5, "P1"),
            "check": [
                "solve([Eq(x + y + z, 2), Eq(2*x + y - z, 1), Eq(x - y + 2*z, 3)], [x, y, z]) == {x: 1, y: 0, z: 1}",
                "Eq(2*1 + 0 - 1, 1)",
            ],
        },
        {
            "id": "ibhl-na-p09",
            "statement": (
                "Use a counterexample to show that the statement "
                "'$|a + b| = |a| + |b|$ for all $a, b \\in \\mathbb{R}$' is false. **[2]**"
            ),
            "solution": (
                "Take $a = 3$, $b = -3$ *(M1)*: $|3 + (-3)| = 0$ but $|3| + |-3| = 6$ *(A1)*. "
                "One failing pair disproves the 'for all'. (The true statement is the triangle "
                "INEQUALITY $|a+b| \\le |a| + |b|$.)"
            ),
            "badges": code_badge("ib-aa-hl-1.15", 2, "P1"),
            "check": [
                "Eq(Abs(3 + (-3)), 0)",
                "Eq(Abs(3) + Abs(-3), 6)",
                "0 != 6",
            ],
        },
    ]


def test_bank():
    return [
        {
            "id": "ibhl-na-q01",
            "statement": (
                "A committee of 4 is selected from 5 women and 4 men. Find the number of "
                "committees with **at least 2 women**, (a) by adding cases, and (b) by "
                "subtracting from the total — verifying your answers agree. **[6]**"
            ),
            "solution": (
                "**(a)** $\\binom{5}{2}\\binom{4}{2} + \\binom{5}{3}\\binom{4}{1} + \\binom{5}{4} "
                "= 60 + 40 + 5 = 105$ *(M1 A1 A1)*.  \n"
                "**(b)** Total $\\binom{9}{4} = 126$; subtract 0-women ($\\binom{4}{4} = 1$) and "
                "1-woman ($\\binom{5}{1}\\binom{4}{3} = 20$) *(M1 A1)*: $126 - 21 = 105$ ✓ "
                "*(A1)*. Two routes, one answer — the agreement is the check."
            ),
            "badges": code_badge("ib-aa-hl-1.10", 6, "P1"),
            "check": [
                "binomial(5, 2)*binomial(4, 2) == 60",
                "binomial(5, 3)*binomial(4, 1) == 40",
                "binomial(5, 4) == 5",
                "60 + 40 + 5 == 105",
                "binomial(9, 4) == 126",
                "binomial(5, 1)*binomial(4, 3) == 20",
                "126 - 1 - 20 == 105",
            ],
        },
        {
            "id": "ibhl-na-q02",
            "statement": (
                "**(a)** Show that $\\sqrt{4+x} = 2\\left(1 + \\dfrac{x}{4}\\right)^{1/2}$. **[1]**  \n"
                "**(b)** Hence expand $\\sqrt{4+x}$ in ascending powers of $x$ up to the term in "
                "$x^2$, stating the interval of validity. **[5]**"
            ),
            "solution": (
                "**(a)** $\\sqrt{4+x} = \\sqrt{4}\\sqrt{1 + \\tfrac{x}{4}} = 2(1+\\tfrac{x}{4})^{1/2}$ "
                "*(AG)*.  \n"
                "**(b)** $2\\left[1 + \\tfrac{1}{2}\\cdot\\tfrac{x}{4} + "
                "\\tfrac{\\frac12(-\\frac12)}{2!}\\left(\\tfrac{x}{4}\\right)^2\\right]$ *(M1 A1)* "
                "$= 2 + \\tfrac{x}{4} - \\tfrac{x^2}{64}$ *(A1 A1)*. Valid for "
                "$\\left|\\tfrac{x}{4}\\right| < 1$, i.e. $|x| < 4$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.10", 6, "P1"),
            "check": [
                "Eq(series(sqrt(4 + x), x, 0, 3).removeO(), 2 + x/4 - x**2/64)",
                "Eq(sqrt(4), 2)",
            ],
        },
        {
            "id": "ibhl-na-q03",
            "statement": (
                "Express $\\dfrac{x+5}{(x-1)(x+3)}$ in the form $\\dfrac{A}{x-1} + "
                "\\dfrac{B}{x+3}$. **[4]**"
            ),
            "solution": (
                "$x + 5 \\equiv A(x+3) + B(x-1)$ *(M1)*. $x = 1$: $6 = 4A \\Rightarrow A = "
                "\\tfrac{3}{2}$ *(A1)*. $x = -3$: $2 = -4B \\Rightarrow B = -\\tfrac{1}{2}$ "
                "*(A1)*. So $\\dfrac{3}{2(x-1)} - \\dfrac{1}{2(x+3)}$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.11", 4, "P1"),
            "check": [
                "Eq(1 + 5, 6)",
                "Eq(-3 + 5, 2)",
                "simplify((x + 5)/((x - 1)*(x + 3)) - (Rational(3, 2)/(x - 1) - Rational(1, 2)/(x + 3))) == 0",
            ],
        },
        {
            "id": "ibhl-na-q04",
            "statement": (
                "Let $z_1 = 1 - i$ and $z_2 = \\sqrt{3} + i$. Find the modulus and argument of "
                "$z_1 z_2$. **[5]**"
            ),
            "solution": (
                "$|z_1| = \\sqrt2$, $\\arg z_1 = -\\tfrac{\\pi}{4}$ *(A1)*; $|z_2| = 2$, "
                "$\\arg z_2 = \\tfrac{\\pi}{6}$ *(A1)*. Product *(M1)*: $|z_1z_2| = 2\\sqrt2$ "
                "*(A1)*, $\\arg(z_1z_2) = -\\tfrac{\\pi}{4} + \\tfrac{\\pi}{6} = "
                "-\\tfrac{\\pi}{12}$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.13", 5, "P1"),
            "check": [
                "Eq(Abs((1 - I)*(sqrt(3) + I)), 2*sqrt(2))",
                "simplify(expand((1 - I)*(sqrt(3) + I)) - 2*sqrt(2)*(cos(pi/12) - I*sin(pi/12))) == 0",
                "Eq(-pi/4 + pi/6, -pi/12)",
            ],
        },
        {
            "id": "ibhl-na-q05",
            "statement": (
                "**(a)** Solve $z^4 = -16$, giving your answers in the form $re^{i\\theta}$. **[4]**  \n"
                "**(b)** Show that the four roots form the vertices of a square, and state its "
                "area. **[3]**"
            ),
            "solution": (
                "**(a)** $-16 = 16e^{i\\pi}$ *(A1)*; $z_k = 2e^{i(\\pi + 2\\pi k)/4}$ *(M1)*: "
                "arguments $\\tfrac{\\pi}{4}, \\tfrac{3\\pi}{4}, -\\tfrac{3\\pi}{4}, "
                "-\\tfrac{\\pi}{4}$ *(A2)*.  \n"
                "**(b)** Equal moduli 2, arguments $90°$ apart → vertices of a square inscribed "
                "in the circle $|z| = 2$ *(R1)*. Side $= \\sqrt{2^2 + 2^2} = 2\\sqrt2$ *(A1)*, "
                "area $= (2\\sqrt2)^2 = 8$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.14", 7, "P1"),
            "check": [
                "Eq(expand((sqrt(2) + sqrt(2)*I)**4), -16)",
                "Eq(Abs(sqrt(2) + sqrt(2)*I), 2)",
                "Eq((2*sqrt(2))**2, 8)",
                "Eq(Abs((sqrt(2) + sqrt(2)*I) - (sqrt(2) - sqrt(2)*I)), 2*sqrt(2))",
            ],
        },
        {
            "id": "ibhl-na-q06",
            "statement": (
                "Consider the system $x + y + z = 3$, $\\;2x - y + 3z = 4$, $\\;4x + y + 5z = k$.  \n"
                "**(a)** Find the value of $k$ for which the system has solutions, and describe "
                "the solution set geometrically. **[5]**  \n"
                "**(b)** For that $k$, give the general solution. **[3]**"
            ),
            "solution": (
                "**(a)** $R_2 - 2R_1$: $-3y + z = -2$ *(A1)*. $R_3 - 4R_1$: $-3y + z = k - 12$ "
                "*(A1)*. The twin rows agree only when $k - 12 = -2$, i.e. $k = 10$ *(M1 A1)*; "
                "then the three planes form a sheaf sharing a line *(A1)*. For $k \\ne 10$: no "
                "solutions (prism).  \n"
                "**(b)** Set $y = t$ *(M1)*: $z = 3t - 2$ and $x = 3 - y - z = 5 - 4t$ *(A1)*: "
                "$(x, y, z) = (5, 0, -2) + t(-4, 1, 3)$ *(A1)*."
            ),
            "badges": code_badge("ib-aa-hl-1.16", 8, "P1"),
            "check": [
                "solve(Eq(k - 12, -2), k) == [10]",
                "Eq(expand((5 - 4*t) + t + (3*t - 2)), 3)",
                "Eq(expand(2*(5 - 4*t) - t + 3*(3*t - 2)), 4)",
                "Eq(expand(4*(5 - 4*t) + t + 5*(3*t - 2)), 10)",
            ],
        },
    ]


# ===========================================================================
def build():
    lessons = [
        lesson_counting_binomial(),
        lesson_partial_fractions(),
        lesson_complex_cartesian(),
        lesson_polar_euler(),
        lesson_de_moivre(),
        lesson_proof_methods(),
        lesson_linear_systems(),
    ]
    unit = {
        "slug": "number-and-algebra",
        "title": "Number & Algebra (AHL)",
        "unit": 1,
        "status": "published",
        "blurb": (
            "The HL extension of Topic 1, complete: permutations and the extended binomial "
            "theorem, partial fractions, complex numbers from Cartesian form through Euler form "
            "to De Moivre's powers and roots, proof by induction and contradiction, and 3×3 "
            "systems with parameter cases — every subtopic code from AHL 1.10 to AHL 1.16."
        ),
        "buildsOn": (
            "The WHOLE of SL Topic 1 (sequences, exponents, logarithms, the binomial theorem) — "
            "work it first in the SL course. HL problems here chain two or three of those ideas "
            "per question, at Paper 1 pace."
        ),
        "lessons": lessons,
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    return unit


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
