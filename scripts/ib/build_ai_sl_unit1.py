#!/usr/bin/env python3
"""IB Mathematics: Applications & Interpretation SL — Unit 1 (Topic 1: Number & Algebra).

Builds data/genmath/ib-ai-sl/number-and-algebra.json: eight lessons, one per
official subtopic code AI SL 1.1–1.8, same anatomy as the AA SL units
(syllabus cards, booklet flags, M/A/R markscheme + narrative solutions,
interactive widgets, sympy check[] everywhere). Banks tagged ib-ai-sl-1.x.

AI is CALCULATOR-ALWAYS — there is no non-calculator paper in this course, so
methods are written for a GDC and the "by hand for Paper 1" split that the AA
lessons carry has no place here. Three of these eight codes exist only in AI:
1.6 (approximation, bounds, percentage error), 1.7 (amortization and
annuities) and 1.8 (systems and polynomials by technology).

Run: python3 scripts/ib/build_ai_sl_unit1.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-ai-sl", "number-and-algebra.json")


# ===========================================================================
# Lesson 1 — AI SL 1.1: standard form
# ===========================================================================
def lesson_standard_form():
    return {
        "slug": "standard-form",
        "title": "Standard Form and the Size of Things",
        "concreteComparison": (
            "A red blood cell is $7 \\times 10^{-6}$ m across; the Sun is $1.4 \\times 10^{9}$ m "
            "across. Written out, that is a millimetre of digits and a screenful of zeros. "
            "Standard form keeps both on one line — and lets you divide them in your head to "
            "learn the Sun is about $2 \\times 10^{14}$ cells wide."
        ),
        "objective": (
            "Write numbers in the form $a \\times 10^{k}$ with $1 \\le a < 10$ and $k \\in "
            "\\mathbb{Z}$, convert both ways, and compute with standard form on the GDC without "
            "losing the exponent."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.1.** Operations with numbers in the form $a \\times "
            "10^{k}$ where $1 \\le a < 10$ and $k$ is an integer. **Papers 1 and 2.** Rarely a "
            "question on its own — it is the notation every other topic answers in, so an "
            "error here quietly costs A-marks all over the paper.",
            "The rule is exactly one non-zero digit before the point. $47\\,000 = 4.7 \\times "
            "10^{4}$; $0.00082 = 8.2 \\times 10^{-4}$. Negative $k$ means a number BELOW one — "
            "it never means a negative number. $-4.7 \\times 10^{3}$ is negative; $4.7 \\times "
            "10^{-3}$ is small.",
            "Your GDC displays standard form as $4.7\\text{E}4$. The $\\text{E}$ is the "
            "calculator's shorthand for $\\times 10^{\\square}$ — and copying it onto the answer "
            "line in that form is a presentation error that costs the A-mark. Write "
            "$4.7 \\times 10^{4}$.",
            "Multiplying and dividing: handle the $a$s and the powers separately. $(3 \\times "
            "10^{5}) \\times (4 \\times 10^{-2}) = 12 \\times 10^{3}$ — and then FIX IT, because "
            "$12$ is not between 1 and 10: $1.2 \\times 10^{4}$. That final tidy-up is the "
            "step most often skipped."
        ],
        "keyIdea": (
            "One digit before the point, always. If your answer starts with $12$ or $0.4$, it "
            "is not in standard form yet — shift once more and adjust $k$."
        ),
        "facts": [
            {
                "title": "The form itself",
                "latex": "a \\times 10^{k}, \\qquad 1 \\le a < 10, \\qquad k \\in \\mathbb{Z}",
                "explanation": "NOT in the formula booklet — it is notation, assumed known. The constraint on $a$ is the whole definition.",
            },
            {
                "title": "Multiply and divide",
                "latex": "(a \\times 10^{m})(b \\times 10^{n}) = ab \\times 10^{m+n}",
                "explanation": "Then renormalise so the leading number sits in $[1, 10)$. Division subtracts the exponents.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-11-we1",
                "statement": (
                    "A country's national debt is $\\$4.28 \\times 10^{11}$ and its population "
                    "is $3.5 \\times 10^{7}$.  \n"
                    "**(a)** Write the debt as an ordinary number. **[1]**  \n"
                    "**(b)** Find the debt per person, giving your answer in standard form "
                    "correct to three significant figures. **[3]**"
                ),
                "solution": (
                    "**(a)** $428\\,000\\,000\\,000$ *(A1)*.  \n"
                    "**(b)** Divide: $\\dfrac{4.28 \\times 10^{11}}{3.5 \\times 10^{7}} = "
                    "\\dfrac{4.28}{3.5} \\times 10^{4}$ *(M1)* $= 1.2228\\ldots \\times 10^{4}$ "
                    "*(A1)* $= 1.22 \\times 10^{4}$ dollars per person *(A1)*.  \n"
                    "**Narrative:** the exponents subtract ($11 - 7 = 4$) and the leading "
                    "numbers divide — two independent jobs, which is exactly why standard form "
                    "is worth the trouble. The answer happens to already sit in $[1, 10)$, so "
                    "no renormalising is needed; check that every time rather than assuming it."
                ),
                "check": [
                    "Rational(428, 100)*10**11 == 428000000000",
                    "11 - 7 == 4",
                    "floor(Rational(428, 350)*1000)/1000 == Rational(1222, 1000)",
                    "Abs(Rational(428, 350) - Rational(122, 100)) < Rational(5, 1000)",
                ],
            },
            {
                "id": "aisl-11-we2",
                "statement": (
                    "Let $p = 6.4 \\times 10^{-3}$ and $q = 8 \\times 10^{5}$.  \n"
                    "**(a)** Find $pq$, giving your answer in standard form. **[2]**  \n"
                    "**(b)** Find $\\dfrac{q}{p}$, giving your answer in standard form correct "
                    "to two significant figures. **[2]**"
                ),
                "solution": (
                    "**(a)** $pq = (6.4 \\times 8) \\times 10^{-3+5} = 51.2 \\times 10^{2}$ "
                    "*(M1)*. Renormalise: $5.12 \\times 10^{3}$ *(A1)*.  \n"
                    "**(b)** $\\dfrac{q}{p} = \\dfrac{8}{6.4} \\times 10^{5-(-3)} = 1.25 \\times "
                    "10^{8}$ *(M1)* $= 1.3 \\times 10^{8}$ to 2 s.f. *(A1)*.  \n"
                    "**Narrative:** part (a) is the renormalising trap in its purest form — "
                    "$51.2 \\times 10^{2}$ is arithmetically right and gets the M1, but it is "
                    "not standard form and loses the A1. In (b), subtracting a NEGATIVE "
                    "exponent adds: $5 - (-3) = 8$."
                ),
                "check": [
                    "Rational(64, 10)*8 == Rational(512, 10)",
                    "Rational(512, 10)*10**2 == Rational(512, 100)*10**3",
                    "5 - (-3) == 8",
                    "Rational(8, 1)/Rational(64, 10) == Rational(125, 100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Leaving an answer as $51.2 \\times 10^{2}$ or $0.4 \\times 10^{6}$.",
                "correction": "Standard form allows exactly one non-zero digit before the point: $5.12 \\times 10^{3}$ and $4 \\times 10^{5}$.",
                "authored": True,
            },
            {
                "text": "Copying the calculator's `1.25E8` straight onto the answer line.",
                "correction": "`E` is calculator shorthand. Write $1.25 \\times 10^{8}$ — the examiner marks what you wrote, not what the screen said.",
                "authored": True,
            },
            {
                "text": "Reading $4.7 \\times 10^{-3}$ as a negative number.",
                "correction": "A negative exponent makes the number SMALL, not negative: $4.7 \\times 10^{-3} = 0.0047 > 0$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-11-t1",
                "statement": (
                    "Write in standard form: **(a)** $0.000\\,915$; **(b)** $73\\,400\\,000$. "
                    "**[2]**"
                ),
                "solution": (
                    "**(a)** $9.15 \\times 10^{-4}$ *(A1)*. **(b)** $7.34 \\times 10^{7}$ "
                    "*(A1)*.  \n"
                    "Count the places the point moves: four to the right in (a) gives $-4$; "
                    "seven to the left in (b) gives $+7$."
                ),
                "check": [
                    "Rational(915, 1000)*10**(-3) == Rational(915, 1000000)",
                    "Rational(734, 100)*10**7 == 73400000",
                ],
            },
            {
                "id": "aisl-11-t2",
                "statement": (
                    "The mass of one water molecule is $3.0 \\times 10^{-23}$ g. Find the number "
                    "of molecules in $18$ g of water, in standard form to 2 s.f. **[3]**"
                ),
                "solution": (
                    "$\\dfrac{18}{3.0 \\times 10^{-23}} = 6 \\times 10^{23}$ *(M1 A1)*, which is "
                    "$6.0 \\times 10^{23}$ to 2 s.f. *(A1)*.  \n"
                    "Dividing by a tiny number gives an enormous one — the exponent flips sign "
                    "coming out of the denominator. (That number has a name: Avogadro's.)"
                ),
                "check": [
                    "18/(Rational(3, 1)*10**(-23)) == 6*10**23",
                    "-(-23) == 23",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.1 · Papers 1 & 2",
                    "title": "One digit, then the point",
                    "body": (
                        "Applications & Interpretation runs on real quantities — populations, "
                        "budgets, half-lives, distances — and real quantities are often absurdly "
                        "large or absurdly small. Standard form is the notation that keeps them "
                        "readable and, more importantly, keeps them COMPUTABLE: the leading "
                        "numbers and the powers of ten are handled separately."
                    ),
                },
                {
                    "kind": "teach",
                    "eyebrow": "The rules",
                    "title": "What counts as standard form",
                    "beats": [
                        "$a \\times 10^{k}$ with $1 \\le a < 10$ — exactly one non-zero digit before the point.",
                        "$k$ is an INTEGER, positive or negative. Negative $k$ means small, never negative.",
                        "Multiplying: multiply the $a$s, ADD the powers. Dividing: divide the $a$s, SUBTRACT the powers.",
                        "Then renormalise. $51.2 \\times 10^{2}$ is not an answer yet.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Debt per person",
                    "problemId": "aisl-11-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Spot the imposter",
                    "title": "Which one is in standard form?",
                    "prompt": "Only one of these is correctly written.",
                    "options": [
                        "$3.05 \\times 10^{-7}$",
                        "$30.5 \\times 10^{-8}$",
                        "$0.305 \\times 10^{-6}$",
                        "$3.05 \\times 10^{-7.5}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "All four have the same value except the last, but only $3.05 \\times "
                        "10^{-7}$ obeys the form: one non-zero digit before the point and an "
                        "INTEGER exponent. The fourth is not even a legal expression in this "
                        "notation."
                    ),
                    "check": [
                        "Rational(305, 100)*10**(-7) == Rational(305, 10)*10**(-8)",
                        "Rational(305, 1000)*10**(-6) == Rational(305, 100)*10**(-7)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Multiply, divide, renormalise",
                    "problemId": "aisl-11-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Exponent arithmetic",
                    "title": "Subtracting a negative",
                    "prompt": "$\\dfrac{9 \\times 10^{4}}{3 \\times 10^{-5}} =$",
                    "options": [
                        "$3 \\times 10^{9}$",
                        "$3 \\times 10^{-1}$",
                        "$3 \\times 10^{-9}$",
                        "$27 \\times 10^{9}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$9 \\div 3 = 3$, and $4 - (-5) = 9$. Dividing by something small makes "
                        "the result large — a sanity check worth two seconds."
                    ),
                    "check": [
                        "4 - (-5) == 9",
                        "Rational(9, 1)/Rational(3, 1) == 3",
                        "(9*10**4)/(Rational(3, 1)*10**(-5)) == 3*10**9",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Calculator discipline",
                    "title": "The E is not part of the answer",
                    "body": (
                        "Every GDC prints standard form with an `E`. It is a display convention, "
                        "not mathematics. Marking guides treat `2.4E5` on an answer line as a "
                        "presentation error — the A-mark goes to $2.4 \\times 10^{5}$. Build the "
                        "habit now, in Topic 1, because you will be quoting calculator output "
                        "for the whole of this course."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-11-t1"},
                {"kind": "tryIt", "problemId": "aisl-11-t2"},
                {
                    "kind": "recap",
                    "title": "Standard form in three lines",
                    "beats": [
                        "$a \\times 10^{k}$, $1 \\le a < 10$, $k$ an integer.",
                        "Multiply/divide the leading numbers; add/subtract the exponents.",
                        "Renormalise, and never write `E` on the answer line.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — AI SL 1.2: arithmetic sequences and series
# ===========================================================================
def lesson_arithmetic():
    return {
        "slug": "arithmetic-sequences-and-series",
        "title": "Arithmetic Sequences & Series",
        "concreteComparison": (
            "A gym membership charges a $\\$60$ joining fee then $\\$35$ a month. Month 12 costs "
            "$\\$35$; the TOTAL by then is $60 + 12 \\times 35 = \\$480$. Sequence versus series — "
            "one term against the running total — is the distinction this whole code turns on."
        ),
        "objective": (
            "Use $u_n = u_1 + (n-1)d$ and the two sum formulas, read sigma notation, and apply "
            "both to the linear-growth contexts AI favours."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.2.** Arithmetic sequences and series; use of the formulas "
            "for the $n$th term and the sum of $n$ terms; use of sigma notation; applications. "
            "**Papers 1 and 2.** In AI these arrive dressed as contexts — salary scales, seating "
            "plans, depreciation by a fixed amount — so reading the model out of the words is "
            "half the question.",
            "A sequence is arithmetic when consecutive terms differ by a constant $d$. Then "
            "$u_n = u_1 + (n-1)d$. The $(n-1)$ carries the whole idea: term 1 has taken zero "
            "steps, term 12 has taken eleven.",
            "Two sum formulas, both in the booklet: $S_n = \\frac{n}{2}\\left(2u_1 + (n-1)d"
            "\\right)$ when you know the common difference, and $S_n = \\frac{n}{2}(u_1 + u_n)$ "
            "when you know the last term. The second is Gauss's pairing — first with last, and "
            "every pair sums to the same total.",
            "Sigma notation packs a series into one symbol: $\\sum_{r=1}^{15}(4r + 3)$ means "
            "evaluate $4r + 3$ at $r = 1, 2, \\ldots, 15$ and add. Any LINEAR recipe in $r$ is "
            "arithmetic with $d$ equal to the coefficient of $r$, so the booklet formulas apply "
            "directly — no need to list terms."
        ],
        "keyIdea": (
            "Term $n$ has taken $n - 1$ steps. Nearly every arithmetic error in this topic is "
            "that one subtraction, forgotten."
        ),
        "facts": [
            {
                "title": "The nth term",
                "latex": "u_n = u_1 + (n-1)d",
                "explanation": "IN the formula booklet (AI SL 1.2).",
            },
            {
                "title": "Sum of n terms",
                "latex": "S_n = \\tfrac{n}{2}\\left(2u_1 + (n-1)d\\right) = \\tfrac{n}{2}(u_1 + u_n)",
                "explanation": "Both forms IN the booklet. Use the second whenever the last term is already known.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-12-we1",
                "statement": (
                    "A theatre has 24 rows. The first row has 18 seats and each row behind has "
                    "3 more seats than the one in front.  \n"
                    "**(a)** Find the number of seats in the last row. **[2]**  \n"
                    "**(b)** Find the total number of seats in the theatre. **[3]**"
                ),
                "solution": (
                    "**(a)** $u_{24} = 18 + 23 \\times 3$ *(M1)* $= 87$ seats *(A1)*.  \n"
                    "**(b)** $S_{24} = \\dfrac{24}{2}(18 + 87)$ *(M1)* $= 12 \\times 105$ *(A1)* "
                    "$= 1260$ seats *(A1)*.  \n"
                    "**Narrative:** part (a) hands part (b) its last term, so the "
                    "first-plus-last form is the efficient one — and follow-through protects (b) "
                    "if (a) slipped. Sanity check: 24 rows averaging about 52 seats is roughly "
                    "1250. The answer is the right size."
                ),
                "check": [
                    "18 + 23*3 == 87",
                    "Rational(24, 2)*(18 + 87) == 1260",
                    "Rational(24, 2)*(2*18 + 23*3) == 1260",
                ],
            },
            {
                "id": "aisl-12-we2",
                "statement": (
                    "The first three terms of an arithmetic sequence are $7$, $11$, $15$.  \n"
                    "**(a)** Write down the common difference. **[1]**  \n"
                    "**(b)** Find the least value of $n$ for which $S_n > 500$. **[4]**"
                ),
                "solution": (
                    "**(a)** $d = 4$ *(A1)*.  \n"
                    "**(b)** $S_n = \\dfrac{n}{2}\\left(14 + 4(n-1)\\right) = n(2n + 5)$ *(M1)*. "
                    "Solving $2n^2 + 5n - 500 = 0$ with the GDC gives $n = 14.6\\ldots$ or a "
                    "negative root *(A1)*. Since $n$ must be a positive integer and $S_n$ "
                    "increases, the least value is $n = 15$ *(A1)*, and $S_{15} = 525 > 500$ "
                    "confirms it *(A1)*.  \n"
                    "**Narrative:** in AI you are expected to solve that quadratic on the "
                    "calculator — no formula needed. But the R-mark is the reasoning: rounding "
                    "$14.6$ DOWN would give $S_{14} = 462$, which fails the inequality. "
                    "\"Least $n$ with $S_n > 500$\" always rounds up, and checking the value is "
                    "the cheapest mark on the page."
                ),
                "check": [
                    "11 - 7 == 4",
                    "Rational(15, 2)*(2*7 + 14*4) == 525",
                    "Rational(14, 2)*(2*7 + 13*4) == 462",
                    "525 > 500",
                    "462 < 500",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Writing $u_{20} = u_1 + 20d$.",
                "correction": "Term 20 has taken 19 steps: $u_{20} = u_1 + 19d$.",
                "authored": True,
            },
            {
                "text": "Rounding the solution of $S_n > k$ the wrong way, or not checking it.",
                "correction": "For 'least $n$ such that $S_n$ exceeds', round UP and then verify with the actual sum — one line, one mark.",
                "authored": True,
            },
            {
                "text": "Confusing the term with the total: answering $u_{24}$ when the question asked for $S_{24}$.",
                "correction": "Sequence = one term. Series = running total. Re-read the last five words of the question before writing.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-12-t1",
                "statement": (
                    "For $5, 12, 19, 26, \\ldots$ find **(a)** $u_{18}$ and **(b)** $S_{18}$. "
                    "**[4]**"
                ),
                "solution": (
                    "**(a)** $d = 7$, so $u_{18} = 5 + 17 \\times 7 = 124$ *(M1 A1)*.  \n"
                    "**(b)** $S_{18} = \\dfrac{18}{2}(5 + 124) = 9 \\times 129 = 1161$ *(M1 A1)*."
                ),
                "check": [
                    "5 + 17*7 == 124",
                    "Rational(18, 2)*(5 + 124) == 1161",
                ],
            },
            {
                "id": "aisl-12-t2",
                "statement": (
                    "A worker's salary is $\\$32\\,000$ in year 1 and rises by $\\$1\\,500$ each "
                    "year. Find the total earned over 10 years. **[3]**"
                ),
                "solution": (
                    "$u_1 = 32\\,000$, $d = 1500$, $n = 10$: $S_{10} = \\dfrac{10}{2}\\left(64\\,"
                    "000 + 9 \\times 1500\\right)$ *(M1)* $= 5 \\times 77\\,500$ *(A1)* $= \\$387"
                    "\\,500$ *(A1)*.  \n"
                    "A fixed annual RISE is arithmetic. A fixed annual PERCENTAGE rise would be "
                    "geometric — that distinction is the next lesson, and the exam loves to put "
                    "the two side by side."
                ),
                "check": [
                    "Rational(10, 2)*(2*32000 + 9*1500) == 387500",
                    "32000 + 9*1500 == 45500",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.2 · Papers 1 & 2",
                    "title": "Constant steps",
                    "body": (
                        "Anything that grows by the same AMOUNT each period is arithmetic: "
                        "salary scales with fixed rises, seating that widens row by row, savings "
                        "with a fixed monthly deposit. Two booklet formulas turn 'add them all "
                        "up' into a single line."
                    ),
                },
                {
                    "kind": "patternGrow",
                    "eyebrow": "See the steps",
                    "title": "A sequence you can watch grow",
                    "teach": (
                        "The odd numbers $1, 3, 5, 7, \\ldots$ are arithmetic with $d = 2$. Step "
                        "through and watch each stage add the same-sized layer — that constant "
                        "layer IS the common difference."
                    ),
                    "config": {"pattern": "odds", "maxSteps": 6},
                },
                {
                    "kind": "teach",
                    "eyebrow": "The formulas",
                    "title": "n − 1 steps, and Gauss's pairing",
                    "beats": [
                        "$u_n = u_1 + (n-1)d$ — term $n$ has taken $n-1$ steps. Booklet.",
                        "$S_n = \\frac{n}{2}\\left(2u_1 + (n-1)d\\right)$ — when you know $d$. Booklet.",
                        "$S_n = \\frac{n}{2}(u_1 + u_n)$ — when you know the last term. Booklet.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A theatre, row by row",
                    "problemId": "aisl-12-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Count the hops",
                    "title": "How many steps to term 30?",
                    "prompt": "In $4, 10, 16, 22, \\ldots$, $u_{30} =$",
                    "options": ["$178$", "$184$", "$180$", "$174$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$u_{30} = 4 + 29 \\times 6 = 178$. The tempting $184$ uses thirty hops, "
                        "but term 1 has taken none."
                    ),
                    "check": ["4 + 29*6 == 178", "4 + 30*6 == 184"],
                },
                {
                    "kind": "teach",
                    "eyebrow": "Sigma notation",
                    "title": "A series in uniform",
                    "body": (
                        "$\\sum_{r=1}^{15}(4r + 3)$ says: run $r$ from 1 to 15, evaluate $4r + 3$ "
                        "each time, add the results. Unpack three things — first term $7$, last "
                        "term $63$, fifteen terms — and it is Gauss again: $\\frac{15}{2}(7 + 63) "
                        "= 525$."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Sigma fluency",
                    "title": "Unpack the uniform",
                    "prompt": "$\\displaystyle\\sum_{r=1}^{15} (4r + 3) =$",
                    "options": ["$525$", "$540$", "$510$", "$495$"],
                    "correctIndex": 0,
                    "explanation": (
                        "First term $4(1) + 3 = 7$; last term $4(15) + 3 = 63$; fifteen terms. "
                        "$\\frac{15}{2}(7 + 63) = 525$."
                    ),
                    "check": [
                        "4*1 + 3 == 7",
                        "4*15 + 3 == 63",
                        "Rational(15, 2)*(7 + 63) == 525",
                        "Sum(4*r + 3, (r, 1, 15)).doit() == 525",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Least n with S_n above a target",
                    "problemId": "aisl-12-we2",
                },
                {
                    "kind": "tip",
                    "eyebrow": "Markscheme wisdom",
                    "title": "Round up, then check",
                    "body": (
                        "\"Find the least $n$ such that $S_n > 500$\" is a four-mark question and "
                        "the last mark is almost always the CHECK. Solve, round in the direction "
                        "the inequality demands, then evaluate the sum at your $n$ and say it "
                        "clears the bar. Two extra lines, one guaranteed mark."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-12-t1"},
                {"kind": "tryIt", "problemId": "aisl-12-t2"},
                {
                    "kind": "recap",
                    "title": "Arithmetic, compressed",
                    "beats": [
                        "Constant DIFFERENCE $d$; term $n$ has taken $n-1$ steps.",
                        "$S_n = \\frac{n}{2}(u_1 + u_n)$ whenever the last term is known.",
                        "A linear recipe inside $\\sum$ is arithmetic — use the formulas, don't list terms.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — AI SL 1.3: geometric sequences and series
# ===========================================================================
def lesson_geometric():
    return {
        "slug": "geometric-sequences-and-series",
        "title": "Geometric Sequences & Series",
        "concreteComparison": (
            "A rumour reaches 3 people on day 1, and each of them tells 3 more the next day. By "
            "day 10 it reaches $3^{10} = 59\\,049$ people in that day alone. Constant "
            "MULTIPLICATION, not constant addition — and the difference between the two is the "
            "difference between a salary rise and a pandemic."
        ),
        "objective": (
            "Use $u_n = u_1 r^{n-1}$ and the geometric sum formula, recognise a common ratio "
            "from context, and solve for $n$ or $r$ with the GDC."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.3.** Geometric sequences and series; use of the formulas "
            "for the $n$th term and the sum of $n$ terms. **Papers 1 and 2.** Pairs constantly "
            "with 1.4 (compound interest is a geometric sequence wearing a suit) and contrasts "
            "with 1.2 — a question giving both models and asking which fits is standard.",
            "Geometric means a constant RATIO: divide any term by the one before and you get the "
            "same $r$ every time. Then $u_n = u_1 r^{\\,n-1}$ — the same $n-1$ count as the "
            "arithmetic case, now as an exponent.",
            "The sum of $n$ terms is $S_n = \\dfrac{u_1(r^{n} - 1)}{r - 1} = \\dfrac{u_1(1 - "
            "r^{n})}{1 - r}$, both in the booklet, both valid for $r \\ne 1$. The two forms are "
            "algebraically identical; use whichever keeps your arithmetic positive.",
            "Spotting the model from words: 'increases by 6 each year' is arithmetic; 'increases "
            "by 6% each year' is geometric with $r = 1.06$. 'Loses a quarter of its value each "
            "year' is geometric with $r = 0.75$. Converting a percentage into a MULTIPLIER is "
            "the move that unlocks most of Topic 1."
        ],
        "keyIdea": (
            "Constant difference adds; constant ratio multiplies. Turn every percentage into a "
            "multiplier and the geometric formulas do the rest."
        ),
        "facts": [
            {
                "title": "The nth term",
                "latex": "u_n = u_1 r^{\\,n-1}",
                "explanation": "IN the booklet (AI SL 1.3). Same $n-1$ count as arithmetic, now an exponent.",
            },
            {
                "title": "Sum of n terms",
                "latex": "S_n = \\frac{u_1(r^{n} - 1)}{r - 1} = \\frac{u_1(1 - r^{n})}{1 - r}, \\quad r \\ne 1",
                "explanation": "Both forms IN the booklet. Identical in value — pick the one that avoids negatives.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-13-we1",
                "statement": (
                    "A geometric sequence has $u_1 = 5$ and $u_4 = 40$.  \n"
                    "**(a)** Find the common ratio. **[2]**  \n"
                    "**(b)** Find $S_{8}$. **[3]**"
                ),
                "solution": (
                    "**(a)** $u_4 = u_1 r^{3}$, so $40 = 5r^{3}$ *(M1)*, giving $r^{3} = 8$ and "
                    "$r = 2$ *(A1)*.  \n"
                    "**(b)** $S_8 = \\dfrac{5(2^{8} - 1)}{2 - 1}$ *(M1)* $= 5 \\times 255$ *(A1)* "
                    "$= 1275$ *(A1)*.  \n"
                    "**Narrative:** from term 1 to term 4 is THREE multiplications, not four — "
                    "the same off-by-one that haunts arithmetic sequences, now in the exponent. "
                    "In (b) the first sum form is the natural one because $r > 1$ keeps both "
                    "numerator and denominator positive."
                ),
                "check": [
                    "5*2**3 == 40",
                    "Rational(5*(2**8 - 1), 2 - 1) == 1275",
                    "2**8 - 1 == 255",
                ],
            },
            {
                "id": "aisl-13-we2",
                "statement": (
                    "A machine bought for $\\$45\\,000$ loses $18\\%$ of its value each year.  \n"
                    "**(a)** Write down the common ratio. **[1]**  \n"
                    "**(b)** Find its value after 6 years, to the nearest dollar. **[2]**  \n"
                    "**(c)** Find the first year in which its value falls below $\\$10\\,000$. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** $r = 0.82$ *(A1)*.  \n"
                    "**(b)** Value $= 45\\,000 \\times 0.82^{6}$ *(M1)* $= \\$13\\,680$ (nearest "
                    "dollar) *(A1)*.  \n"
                    "**(c)** Solve $45\\,000 \\times 0.82^{n} < 10\\,000$ on the GDC *(M1)*: "
                    "$n > 7.58\\ldots$ *(A1)*, so the value first falls below $\\$10\\,000$ during "
                    "year $8$ *(A1)*.  \n"
                    "**Narrative:** losing $18\\%$ leaves $82\\%$ — write the multiplier, not the "
                    "loss. In (c) an inequality with the unknown in the exponent is a "
                    "calculator job in AI: graph both sides and read the crossing, or use the "
                    "solver. Rounding $7.58$ DOWN would name a year when the value is still "
                    "above the threshold."
                ),
                "check": [
                    "1 - Rational(18, 100) == Rational(82, 100)",
                    "floor(45000*Rational(82, 100)**6) == 13680",
                    "45000*Rational(82, 100)**8 < 10000",
                    "45000*Rational(82, 100)**7 > 10000",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using $r = 0.18$ for 'loses 18% each year'.",
                "correction": "Losing 18% keeps 82%: $r = 0.82$. A gain of 18% would be $r = 1.18$.",
                "authored": True,
            },
            {
                "text": "Writing $u_n = u_1 r^{n}$.",
                "correction": "$u_n = u_1 r^{\\,n-1}$ — reaching term $n$ takes $n-1$ multiplications.",
                "authored": True,
            },
            {
                "text": "Applying the arithmetic sum formula to a percentage-growth context.",
                "correction": "Percentages multiply. Test the data: constant DIFFERENCES mean arithmetic, constant RATIOS mean geometric.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-13-t1",
                "statement": (
                    "A geometric sequence begins $80, 60, 45, \\ldots$  \n"
                    "**(a)** Find $r$. **[1]**  \n"
                    "**(b)** Find $u_{7}$, to 3 s.f. **[2]**"
                ),
                "solution": (
                    "**(a)** $r = \\dfrac{60}{80} = 0.75$ *(A1)*.  \n"
                    "**(b)** $u_7 = 80 \\times 0.75^{6} = 14.238\\ldots = 14.2$ (3 s.f.) *(M1 A1)*."
                ),
                "check": [
                    "Rational(60, 80) == Rational(3, 4)",
                    "Rational(45, 60) == Rational(3, 4)",
                    "Abs(80*Rational(3, 4)**6 - Rational(142, 10)) < Rational(5, 100)",
                ],
            },
            {
                "id": "aisl-13-t2",
                "statement": (
                    "A population of 2000 bacteria triples every hour. Find the total number of "
                    "bacteria-hours recorded if the population is logged at the end of each of "
                    "the first 5 hours — that is, find $S_5$ for the sequence of hourly "
                    "populations. **[3]**"
                ),
                "solution": (
                    "The populations are $6000, 18\\,000, 54\\,000, \\ldots$ with $u_1 = 6000$, "
                    "$r = 3$.  \n"
                    "$S_5 = \\dfrac{6000(3^{5} - 1)}{3 - 1}$ *(M1)* $= \\dfrac{6000 \\times 242}"
                    "{2}$ *(A1)* $= 726\\,000$ *(A1)*."
                ),
                "check": [
                    "2000*3 == 6000",
                    "3**5 - 1 == 242",
                    "Rational(6000*(3**5 - 1), 3 - 1) == 726000",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.3 · Papers 1 & 2",
                    "title": "Constant ratio",
                    "body": (
                        "Populations, investments, radioactive decay, depreciation — anything "
                        "that changes by a constant PERCENTAGE is geometric. The whole family "
                        "runs on one move: turn the percentage into a multiplier $r$, then two "
                        "booklet formulas do the work."
                    ),
                },
                {
                    "kind": "expGraph",
                    "eyebrow": "See the growth",
                    "title": "Multiplying, again and again",
                    "teach": (
                        "Geometric terms sit on an exponential curve. Slide the base and watch "
                        "the difference between $r > 1$ (growth that starts slow and turns "
                        "vertical) and $0 < r < 1$ (decay that flattens without ever reaching "
                        "zero) — the two shapes AI models with all course long."
                    ),
                    "config": {"mode": "growth", "a": 1, "b": 2, "interactive": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "The formulas",
                    "title": "Powers, and the sum that telescopes",
                    "beats": [
                        "$u_n = u_1 r^{\\,n-1}$ — $n-1$ multiplications to reach term $n$. Booklet.",
                        "$S_n = \\frac{u_1(r^n - 1)}{r - 1}$, valid for $r \\ne 1$. Booklet.",
                        "Percentage UP by $p\\%$: $r = 1 + \\frac{p}{100}$. DOWN by $p\\%$: $r = 1 - \\frac{p}{100}$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Ratio from two terms",
                    "problemId": "aisl-13-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Percentage to multiplier",
                    "title": "Down by 35% a year",
                    "prompt": "A value falls by $35\\%$ each year. The common ratio is",
                    "options": ["$0.65$", "$0.35$", "$1.35$", "$-0.35$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Losing $35\\%$ leaves $65\\%$, so $r = 0.65$. The multiplier is what "
                        "SURVIVES, not what is lost."
                    ),
                    "check": [
                        "1 - Rational(35, 100) == Rational(65, 100)",
                        "1000*Rational(65, 100) == 650",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Depreciation, and when it crosses a line",
                    "problemId": "aisl-13-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Which model?",
                    "title": "Arithmetic or geometric?",
                    "prompt": "Rent starts at $\\$800$ and rises by $4\\%$ each year. Year 5's rent is",
                    "options": [
                        "$800 \\times 1.04^{4}$",
                        "$800 \\times 1.04^{5}$",
                        "$800 + 4 \\times 4$",
                        "$800 \\times 0.04^{4}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "A PERCENTAGE rise is geometric with $r = 1.04$, and year 5 has taken "
                        "four rises: $800 \\times 1.04^{4} \\approx \\$935.89$."
                    ),
                    "check": [
                        "1 + Rational(4, 100) == Rational(104, 100)",
                        "floor(800*Rational(104, 100)**4*100) == 93588",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Read the data before choosing a formula",
                    "body": (
                        "Given a table of values, test both: subtract consecutive terms (constant "
                        "⇒ arithmetic) and divide consecutive terms (constant ⇒ geometric). Two "
                        "subtractions and two divisions settle it in ten seconds, and picking "
                        "the wrong family costs every mark that follows."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-13-t1"},
                {"kind": "tryIt", "problemId": "aisl-13-t2"},
                {
                    "kind": "recap",
                    "title": "Geometric, compressed",
                    "beats": [
                        "Constant RATIO $r$; $u_n = u_1 r^{\\,n-1}$.",
                        "$S_n = \\frac{u_1(r^n - 1)}{r - 1}$ for $r \\ne 1$.",
                        "Percentages become multipliers: $+p\\% \\to 1 + \\frac{p}{100}$, $-p\\% \\to 1 - \\frac{p}{100}$.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — AI SL 1.4: financial applications
# ===========================================================================
def lesson_financial():
    return {
        "slug": "financial-applications",
        "title": "Compound Interest & Depreciation",
        "concreteComparison": (
            "$\\$1000$ at $5\\%$ compounded annually is $\\$1628$ after ten years. Compounded "
            "MONTHLY it is $\\$1647$. The rate did not change and the time did not change — only "
            "how often the interest gets to join in. That gap is what this code is about."
        ),
        "objective": (
            "Apply the compound-interest formula with any compounding frequency, handle "
            "depreciation as negative growth, and use the GDC's finance solver correctly."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.4.** Financial applications of geometric sequences and "
            "series: compound interest, annual depreciation. **Papers 1 and 2.** A guaranteed "
            "presence in AI — the course's identity is applying mathematics to real decisions, "
            "and money is the most examined of those.",
            "The booklet gives $FV = PV \\times \\left(1 + \\dfrac{r}{100k}\\right)^{kn}$, where "
            "$PV$ is the present value, $FV$ the future value, $r$ the ANNUAL percentage rate, "
            "$k$ the number of compounding periods per year, and $n$ the number of YEARS. Get "
            "$k$ and $n$ straight and the formula is mechanical.",
            "Compounding frequency: annually $k = 1$, half-yearly $k = 2$, quarterly $k = 4$, "
            "monthly $k = 12$. Note what the formula does — it divides the rate by $k$ AND "
            "multiplies the exponent by $k$. More frequent compounding always yields slightly "
            "more, with rapidly diminishing returns.",
            "Depreciation is the same formula with a negative rate: a $15\\%$ annual loss is "
            "$r = -15$, giving a multiplier of $0.85$. Your GDC's finance solver (TVM) handles "
            "all of this, but it demands a sign convention — money paid OUT is negative, money "
            "received is positive — and mixing the signs is the most common way to get a "
            "confidently wrong answer."
        ],
        "keyIdea": (
            "$k$ appears twice: it divides the rate and multiplies the time. Change the "
            "compounding frequency and you must change both."
        ),
        "facts": [
            {
                "title": "Compound interest",
                "latex": "FV = PV\\left(1 + \\frac{r}{100k}\\right)^{kn}",
                "explanation": "IN the booklet (AI SL 1.4). $r$ is the annual % rate, $k$ periods per year, $n$ YEARS.",
            },
            {
                "title": "Depreciation",
                "latex": "FV = PV\\left(1 - \\frac{p}{100}\\right)^{n}",
                "explanation": "The same machinery with a negative rate. A $p\\%$ annual loss keeps $\\left(1 - \\frac{p}{100}\\right)$ of the value each year.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-14-we1",
                "statement": (
                    "Maria invests $\\$8000$ at a nominal annual rate of $6\\%$, compounded "
                    "quarterly.  \n"
                    "**(a)** Find the value of the investment after 5 years, to the nearest "
                    "dollar. **[3]**  \n"
                    "**(b)** Find the total interest earned. **[1]**"
                ),
                "solution": (
                    "**(a)** $k = 4$, $n = 5$, so $FV = 8000\\left(1 + \\dfrac{6}{400}\\right)^{20}$ "
                    "*(M1 A1)* $= 8000 \\times 1.015^{20} = \\$10\\,774$ *(A1)*.  \n"
                    "**(b)** Interest $= 10\\,774 - 8000 = \\$2774$ *(A1)*.  \n"
                    "**Narrative:** quarterly means $k = 4$, so the quarterly rate is "
                    "$6 \\div 4 = 1.5\\%$ and there are $4 \\times 5 = 20$ quarters. Both "
                    "adjustments, or neither. Part (b) is a reminder that 'interest earned' is "
                    "the GAIN, not the final balance — a one-mark question that is regularly "
                    "answered with the wrong number."
                ),
                "check": [
                    "Rational(6, 100*4) == Rational(15, 1000)",
                    "4*5 == 20",
                    "floor(8000*(1 + Rational(6, 400))**20) == 10774",
                    "floor(8000*(1 + Rational(6, 400))**20) - 8000 == 2774",
                ],
            },
            {
                "id": "aisl-14-we2",
                "statement": (
                    "A car is bought for $\\$32\\,000$ and depreciates at $14\\%$ per year.  \n"
                    "**(a)** Find its value after 4 years, to the nearest dollar. **[2]**  \n"
                    "**(b)** Find how many complete years pass before it is worth less than "
                    "half its original price. **[3]**"
                ),
                "solution": (
                    "**(a)** $32\\,000 \\times 0.86^{4}$ *(M1)* $= \\$17\\,504$ *(A1)*.  \n"
                    "**(b)** Solve $32\\,000 \\times 0.86^{n} < 16\\,000$, i.e. $0.86^{n} < 0.5$ "
                    "*(M1)*. The GDC gives $n > 4.59\\ldots$ *(A1)*, so after $5$ complete years "
                    "*(A1)*.  \n"
                    "**Narrative:** halving is independent of the starting price — the $32\\,000$ "
                    "cancels, which is worth noticing because it makes the arithmetic "
                    "trivially checkable. And 'complete years' means the answer is an integer: "
                    "at $n = 4$ the car is still worth more than half."
                ),
                "check": [
                    "1 - Rational(14, 100) == Rational(86, 100)",
                    "floor(32000*Rational(86, 100)**4) == 17504",
                    "Rational(86, 100)**5 < Rational(1, 2)",
                    "Rational(86, 100)**4 > Rational(1, 2)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Adjusting the rate for quarterly compounding but leaving the exponent as the number of years.",
                "correction": "$k$ appears twice: $\\left(1 + \\frac{r}{100k}\\right)^{kn}$. Quarterly for 5 years is a rate of $r/4$ over 20 periods.",
                "authored": True,
            },
            {
                "text": "Answering the final BALANCE when the question asked for the INTEREST.",
                "correction": "Interest earned $= FV - PV$. Read the last line of the question again.",
                "authored": True,
            },
            {
                "text": "Entering both $PV$ and $FV$ as positive in the GDC's finance solver.",
                "correction": "The solver needs opposite signs: money you pay in is negative, money you receive is positive. Same sign gives nonsense.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-14-t1",
                "statement": (
                    "$\\$5000$ is invested at $4.5\\%$ per year compounded monthly. Find the "
                    "value after 3 years, to the nearest dollar. **[3]**"
                ),
                "solution": (
                    "$k = 12$, $n = 3$: $FV = 5000\\left(1 + \\dfrac{4.5}{1200}\\right)^{36}$ "
                    "*(M1 A1)* $= \\$5721$ *(A1)*."
                ),
                "check": [
                    "12*3 == 36",
                    "floor(5000*(1 + Rational(45, 10*1200))**36) == 5721",
                ],
            },
            {
                "id": "aisl-14-t2",
                "statement": (
                    "A laptop bought for $\\$1800$ is worth $\\$1200$ after 2 years. Assuming "
                    "constant annual depreciation, find the annual rate to 3 s.f. **[3]**"
                ),
                "solution": (
                    "$1800r^{2} = 1200$ *(M1)*, so $r^{2} = \\dfrac{2}{3}$ and $r = 0.8164\\ldots$ "
                    "*(A1)*. The annual depreciation rate is $1 - 0.8165 = 0.1835$, i.e. "
                    "$18.4\\%$ to 3 s.f. *(A1)*.  \n"
                    "The multiplier is not the rate — subtract from 1 at the end."
                ),
                "check": [
                    "Rational(1200, 1800) == Rational(2, 3)",
                    "Abs(sqrt(Rational(2, 3)) - Rational(8165, 10000)) < Rational(1, 10000)",
                    "Abs((1 - sqrt(Rational(2, 3))) - Rational(184, 1000)) < Rational(5, 10000)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.4 · Papers 1 & 2",
                    "title": "Money is a geometric sequence",
                    "body": (
                        "Every compound-interest problem is the previous lesson in financial "
                        "clothing: a starting amount multiplied by the same factor over and over. "
                        "What the finance context adds is the compounding FREQUENCY — how often "
                        "the interest is credited and starts earning interest itself."
                    ),
                },
                {
                    "kind": "teach",
                    "eyebrow": "The formula",
                    "title": "Where each letter goes",
                    "beats": [
                        "$FV = PV\\left(1 + \\frac{r}{100k}\\right)^{kn}$ — booklet, AI SL 1.4.",
                        "$r$ is the ANNUAL percentage rate, quoted as a number like $6$, not $0.06$.",
                        "$k$ = periods per year: annually 1, half-yearly 2, quarterly 4, monthly 12.",
                        "$n$ = number of YEARS. The exponent $kn$ is the number of periods.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Quarterly compounding",
                    "problemId": "aisl-14-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Frequency check",
                    "title": "How many periods?",
                    "prompt": "$\\$2000$ at $8\\%$ compounded half-yearly for 6 years uses",
                    "options": [
                        "rate $4\\%$ over $12$ periods",
                        "rate $8\\%$ over $12$ periods",
                        "rate $4\\%$ over $6$ periods",
                        "rate $8\\%$ over $6$ periods",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Half-yearly is $k = 2$: the rate halves to $4\\%$ and the count doubles "
                        "to $2 \\times 6 = 12$. Both, or the answer is wrong."
                    ),
                    "check": [
                        "Rational(8, 2) == 4",
                        "2*6 == 12",
                        "floor(2000*(1 + Rational(8, 200))**12) == 3202",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Depreciation, and halving",
                    "problemId": "aisl-14-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Interest vs balance",
                    "title": "What did the question ask?",
                    "prompt": "$\\$500$ grows to $\\$610$. The interest earned is",
                    "options": ["$\\$110$", "$\\$610$", "$\\$500$", "$22\\%$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Interest is the GAIN: $610 - 500 = \\$110$. The $22\\%$ is the total "
                        "percentage growth, which is a different question again."
                    ),
                    "check": ["610 - 500 == 110", "Rational(110, 500)*100 == 22"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Calculator discipline",
                    "title": "The finance solver's sign convention",
                    "body": (
                        "TVM solvers model cash FLOW. Money leaving your pocket — the deposit, "
                        "the loan repayment — is negative; money arriving is positive. Enter "
                        "$PV = -8000$ to find a positive $FV$. If your answer comes back with an "
                        "unexpected minus sign, that is the solver telling you which direction "
                        "the money moved, not an error."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-14-t1"},
                {"kind": "tryIt", "problemId": "aisl-14-t2"},
                {
                    "kind": "recap",
                    "title": "Finance, compressed",
                    "beats": [
                        "$FV = PV\\left(1 + \\frac{r}{100k}\\right)^{kn}$ — $k$ divides the rate and multiplies the time.",
                        "Depreciation is a negative rate; the multiplier is what remains.",
                        "Interest earned $= FV - PV$, never $FV$.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — AI SL 1.5: exponents and logarithms
# ===========================================================================
def lesson_exponents_logs():
    return {
        "slug": "exponents-and-logarithms",
        "title": "Exponent Laws & Introducing Logarithms",
        "concreteComparison": (
            "A sheet of paper $0.1$ mm thick, folded 42 times, would reach the Moon. Asking "
            "'how many folds?' means asking for an exponent — and the operation that extracts "
            "an exponent is the logarithm. That is its entire job description."
        ),
        "objective": (
            "Apply the laws of exponents with integer exponents, convert between exponential "
            "and logarithmic form, and evaluate logarithms with the GDC."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.5.** Laws of exponents with integer exponents; "
            "introduction to logarithms with base 10 and $e$; numerical evaluation of "
            "logarithms using technology. **Papers 1 and 2.** Note the boundary: AI SL needs the "
            "IDEA of a logarithm and the ability to evaluate one, not the full log-law algebra "
            "that AA carries.",
            "The exponent laws: $a^{m} \\times a^{n} = a^{m+n}$, $\\dfrac{a^{m}}{a^{n}} = "
            "a^{m-n}$, $(a^{m})^{n} = a^{mn}$, $a^{0} = 1$ and $a^{-n} = \\dfrac{1}{a^{n}}$. "
            "Every one is a bookkeeping rule about how many copies of $a$ are being multiplied.",
            "A logarithm answers 'what exponent?'. $\\log_{a} b = x$ means exactly $a^{x} = b$ — "
            "the two statements carry the same information written two ways, and converting "
            "between them is the single most useful move in this code. In the booklet.",
            "Two bases matter here: $\\log_{10}$, written $\\log$, and $\\log_{e}$, written "
            "$\\ln$, where $e \\approx 2.718$. Your GDC has both keys. AI SL asks you to "
            "EVALUATE these — $\\ln 40 = 3.69$ — and to use them to release an exponent when "
            "solving growth equations."
        ],
        "keyIdea": (
            "$\\log_{a} b = x$ and $a^{x} = b$ are the same sentence. Whenever the unknown is "
            "stuck in an exponent, that equivalence is the way out."
        ),
        "facts": [
            {
                "title": "The exponent laws",
                "latex": "a^{m}a^{n} = a^{m+n}, \\quad \\frac{a^{m}}{a^{n}} = a^{m-n}, \\quad (a^{m})^{n} = a^{mn}, \\quad a^{-n} = \\frac{1}{a^{n}}",
                "explanation": "IN the booklet (AI SL 1.5). All follow from counting copies of $a$.",
            },
            {
                "title": "The logarithm, defined",
                "latex": "a^{x} = b \\iff x = \\log_{a} b, \\qquad a > 0,\\ b > 0,\\ a \\ne 1",
                "explanation": "IN the booklet. Reading it both ways is the skill.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-15-we1",
                "statement": (
                    "**(a)** Simplify $\\dfrac{6x^{5} \\times 2x^{-3}}{4x^{2}}$. **[3]**  \n"
                    "**(b)** Write $\\log_{3} 81 = 4$ in exponential form, and evaluate "
                    "$\\log_{2} 32$. **[2]**"
                ),
                "solution": (
                    "**(a)** Numerator: $6 \\times 2 = 12$ and $x^{5} \\times x^{-3} = x^{2}$ "
                    "*(M1)*. So the expression is $\\dfrac{12x^{2}}{4x^{2}}$ *(A1)* $= 3$ "
                    "*(A1)*.  \n"
                    "**(b)** $3^{4} = 81$ *(A1)*. And $\\log_{2} 32 = 5$ since $2^{5} = 32$ "
                    "*(A1)*.  \n"
                    "**Narrative:** the powers of $x$ cancel completely in (a) — an answer with "
                    "no $x$ in it is not a mistake, it is the point. In (b), 'write in "
                    "exponential form' is asking you to perform the conversion, so show the "
                    "rearranged statement rather than just asserting a value."
                ),
                "check": [
                    "6*2 == 12",
                    "5 + (-3) == 2",
                    "Rational(12, 4) == 3",
                    "3**4 == 81",
                    "2**5 == 32",
                ],
            },
            {
                "id": "aisl-15-we2",
                "statement": (
                    "A colony of bacteria is modelled by $P = 500e^{0.15t}$, where $t$ is in "
                    "hours.  \n"
                    "**(a)** Find the population after 8 hours, to the nearest whole number. "
                    "**[2]**  \n"
                    "**(b)** Find the time taken for the population to reach 4000. **[3]**"
                ),
                "solution": (
                    "**(a)** $P = 500e^{0.15 \\times 8} = 500e^{1.2}$ *(M1)* $= 1660$ bacteria "
                    "*(A1)*.  \n"
                    "**(b)** Solve $500e^{0.15t} = 4000$: divide to get $e^{0.15t} = 8$ *(M1)*, "
                    "take natural logs to get $0.15t = \\ln 8$ *(A1)*, so $t = \\dfrac{\\ln 8}"
                    "{0.15} = 13.9$ hours *(A1)*.  \n"
                    "**Narrative:** in AI you may equally solve (b) by graphing $y = 500e^{0.15t}$ "
                    "and $y = 4000$ and reading the intersection — both routes earn full marks, "
                    "and the graph is often faster. The log route is shown here because it "
                    "generalises: whenever the unknown is an exponent, $\\ln$ is the tool that "
                    "brings it down."
                ),
                "check": [
                    "Rational(15, 100)*8 == Rational(12, 10)",
                    "floor(500*exp(Rational(12, 10))) == 1660",
                    "Rational(4000, 500) == 8",
                    "Abs(log(8)/Rational(15, 100) - Rational(139, 10)) < Rational(5, 100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Writing $a^{m} \\times a^{n} = a^{mn}$.",
                "correction": "Multiplying powers ADDS the exponents; raising a power to a power multiplies them.",
                "authored": True,
            },
            {
                "text": "Treating $a^{-n}$ as a negative number.",
                "correction": "$a^{-n} = \\frac{1}{a^{n}}$ — a reciprocal, always positive when $a > 0$.",
                "authored": True,
            },
            {
                "text": "Dividing by $0.15$ before taking logs when solving $500e^{0.15t} = 4000$.",
                "correction": "The $0.15$ is trapped in the exponent. Isolate the exponential first, then take $\\ln$ of both sides.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-15-t1",
                "statement": (
                    "Simplify **(a)** $(2x^{3})^{4}$ and **(b)** $\\dfrac{15a^{6}}{5a^{-2}}$. "
                    "**[4]**"
                ),
                "solution": (
                    "**(a)** $2^{4}x^{12} = 16x^{12}$ *(M1 A1)*.  \n"
                    "**(b)** $\\dfrac{15}{5} = 3$ and $a^{6 - (-2)} = a^{8}$, giving $3a^{8}$ "
                    "*(M1 A1)*.  \n"
                    "In (a) the outer power hits the 2 as well as the $x$ — a bracket applies "
                    "to everything inside it."
                ),
                "check": [
                    "2**4 == 16",
                    "3*4 == 12",
                    "Rational(15, 5) == 3",
                    "6 - (-2) == 8",
                ],
            },
            {
                "id": "aisl-15-t2",
                "statement": (
                    "Evaluate to 3 s.f.: **(a)** $\\log 250$; **(b)** $\\ln 0.4$. Then solve "
                    "$10^{x} = 250$. **[3]**"
                ),
                "solution": (
                    "**(a)** $\\log 250 = 2.40$ *(A1)*. **(b)** $\\ln 0.4 = -0.916$ *(A1)*.  \n"
                    "$10^{x} = 250 \\Rightarrow x = \\log 250 = 2.40$ *(A1)*.  \n"
                    "Part (a) and the equation are the same question — which is exactly what "
                    "the definition of a logarithm says."
                ),
                "check": [
                    "Abs(log(250, 10) - Rational(240, 100)) < Rational(5, 1000)",
                    "Abs(log(Rational(4, 10)) - Rational(-916, 1000)) < Rational(5, 10000)",
                    "Eq(simplify(10**log(250, 10)), 250)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.5 · Papers 1 & 2",
                    "title": "Exponents up, logarithms down",
                    "body": (
                        "Exponents build big numbers fast; logarithms undo them. AI SL asks for "
                        "the exponent LAWS in full, but only the IDEA of a logarithm plus the "
                        "ability to evaluate one on your GDC — enough to release an unknown "
                        "trapped in an exponent, which is where every growth model eventually "
                        "puts it."
                    ),
                },
                {
                    "kind": "exponentBuilder",
                    "eyebrow": "See the laws",
                    "title": "Counting copies of a",
                    "teach": (
                        "Every exponent law is bookkeeping. Build $a^{3} \\times a^{4}$ and count "
                        "the copies: seven, so the exponents added. There is nothing to memorise "
                        "here that counting cannot rederive."
                    ),
                    "config": {"base": 2, "exp": 3, "minExp": 0, "maxExp": 6},
                },
                {
                    "kind": "teach",
                    "eyebrow": "The definition",
                    "title": "Two ways to say one thing",
                    "beats": [
                        "$a^{x} = b$ and $\\log_{a} b = x$ carry identical information. Booklet.",
                        "$\\log$ means base 10; $\\ln$ means base $e \\approx 2.718$.",
                        "Both are single keys on the GDC — AI SL evaluates them, it does not manipulate them algebraically.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Laws, then the conversion",
                    "problemId": "aisl-15-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read it backwards",
                    "title": "What exponent?",
                    "prompt": "$\\log_{5} 125 =$",
                    "options": ["$3$", "$25$", "$5$", "$625$"],
                    "correctIndex": 0,
                    "explanation": (
                        "The question is 'five to WHAT power gives 125?'. Since $5^{3} = 125$, "
                        "the answer is 3. A logarithm always returns an exponent."
                    ),
                    "check": ["5**3 == 125", "log(125, 5) == 3"],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Releasing t from the exponent",
                    "problemId": "aisl-15-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Law check",
                    "title": "Power of a power",
                    "prompt": "$(3x^{2})^{3} =$",
                    "options": ["$27x^{6}$", "$9x^{6}$", "$27x^{5}$", "$3x^{6}$"],
                    "correctIndex": 0,
                    "explanation": (
                        "The outer exponent applies to EVERYTHING in the bracket: $3^{3} = 27$ "
                        "and $(x^{2})^{3} = x^{6}$. Forgetting the coefficient is the usual slip."
                    ),
                    "check": ["3**3 == 27", "2*3 == 6"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Two legal routes, one answer",
                    "body": (
                        "AI is calculator-always, so 'solve $500e^{0.15t} = 4000$' can be answered "
                        "by logs OR by graphing both sides and reading the intersection. Both get "
                        "full marks — but whichever you choose, WRITE DOWN the equation you "
                        "solved. A bare answer with no visible method risks the M-mark even when "
                        "the number is right."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-15-t1"},
                {"kind": "tryIt", "problemId": "aisl-15-t2"},
                {
                    "kind": "recap",
                    "title": "Exponents and logs, compressed",
                    "beats": [
                        "Multiply → add exponents; power of a power → multiply them; negative → reciprocal.",
                        "$a^{x} = b \\iff \\log_{a} b = x$ — the conversion is the whole tool.",
                        "$\\log$ is base 10, $\\ln$ is base $e$; evaluate both on the GDC.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — AI SL 1.6: approximation, bounds and error  (AI-only code)
# ===========================================================================
def lesson_approximation():
    return {
        "slug": "approximation-and-error",
        "title": "Approximation, Bounds & Percentage Error",
        "concreteComparison": (
            "A shelf measured as $80$ cm 'to the nearest centimetre' is really anywhere from "
            "$79.5$ to $80.5$ cm. Cut four of them for a $320$ cm wall and the accumulated "
            "uncertainty is $\\pm 2$ cm — enough to miss. Rounding is not a cosmetic step; it "
            "propagates."
        ),
        "objective": (
            "Round to decimal places and significant figures, state upper and lower bounds for "
            "a rounded measurement, and compute percentage error."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.6.** Approximation: decimal places, significant figures; "
            "upper and lower bounds of rounded numbers; percentage errors; estimation. "
            "**Papers 1 and 2.** This code exists only in AI — AA has no equivalent — and it "
            "reflects the course's stance that a number without a sense of its accuracy is not "
            "yet an answer.",
            "Significant figures count from the first non-zero digit. In $0.004\\,073$, the "
            "first significant figure is the 4; to 2 s.f. it is $0.0041$. Leading zeros never "
            "count; trailing zeros after a decimal point do. Decimal places, by contrast, count "
            "from the point regardless of what the digits are.",
            "A value rounded to the nearest unit $u$ has bounds half a unit either side: "
            "$x_{\\text{rounded}} - \\frac{u}{2} \\le x < x_{\\text{rounded}} + \\frac{u}{2}$. "
            "A mass of $6.4$ kg to 1 d.p. lies in $[6.35,\\ 6.45)$. The lower bound is included, "
            "the upper is not — that asymmetry is genuine, though examiners accept $6.45$ as the "
            "upper bound.",
            "Percentage error compares an approximate value $v_{A}$ with the exact value $v_{E}$: "
            "$\\varepsilon = \\left|\\dfrac{v_{A} - v_{E}}{v_{E}}\\right| \\times 100\\%$. It is "
            "IN the booklet. Two things to hold onto: the EXACT value goes on the bottom, and "
            "the absolute-value bars mean the answer is never negative."
        ],
        "keyIdea": (
            "Every rounded measurement is an interval, not a point. Percentage error divides by "
            "the EXACT value and is never negative."
        ),
        "facts": [
            {
                "title": "Percentage error",
                "latex": "\\varepsilon = \\left|\\frac{v_A - v_E}{v_E}\\right| \\times 100\\%",
                "explanation": "IN the booklet (AI SL 1.6). $v_E$ is the exact value and sits in the DENOMINATOR.",
            },
            {
                "title": "Bounds of a rounded value",
                "latex": "x - \\tfrac{u}{2} \\le x_{\\text{true}} < x + \\tfrac{u}{2}",
                "explanation": "NOT in the booklet — a definition to know. $u$ is the rounding unit: 1, 0.1, 0.01, 10, …",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-16-we1",
                "statement": (
                    "The length of a rectangle is $12.4$ cm and its width is $7.8$ cm, each "
                    "correct to 1 decimal place.  \n"
                    "**(a)** Write down the lower bound of the length. **[1]**  \n"
                    "**(b)** Find the upper bound of the area of the rectangle. **[3]**"
                ),
                "solution": (
                    "**(a)** $12.35$ cm *(A1)*.  \n"
                    "**(b)** The area is largest when BOTH dimensions are largest: upper bounds "
                    "$12.45$ and $7.85$ *(M1)*. Area $= 12.45 \\times 7.85$ *(A1)* $= 97.7$ "
                    "cm$^2$ (3 s.f.) *(A1)*.  \n"
                    "**Narrative:** 1 d.p. means a rounding unit of $0.1$, so the bounds sit "
                    "$0.05$ either side. For a PRODUCT, both bounds move the same direction — "
                    "but be careful with quotients, where the largest result needs the largest "
                    "numerator and the SMALLEST denominator."
                ),
                "check": [
                    "Rational(124, 10) - Rational(5, 100) == Rational(1235, 100)",
                    "Rational(124, 10) + Rational(5, 100) == Rational(1245, 100)",
                    "Rational(78, 10) + Rational(5, 100) == Rational(785, 100)",
                    "Abs(Rational(1245, 100)*Rational(785, 100) - Rational(977, 10)) < Rational(5, 100)",
                ],
            },
            {
                "id": "aisl-16-we2",
                "statement": (
                    "A student measures the circumference of a circular table as $2.4$ m. The "
                    "true circumference is $2.51$ m.  \n"
                    "**(a)** Find the percentage error in the student's measurement. **[3]**  \n"
                    "**(b)** The student uses $\\pi \\approx 3$ to estimate the table's diameter "
                    "from the true circumference. Find the percentage error in that estimate of "
                    "the diameter. **[3]**"
                ),
                "solution": (
                    "**(a)** $\\varepsilon = \\left|\\dfrac{2.4 - 2.51}{2.51}\\right| \\times 100$ "
                    "*(M1 A1)* $= 4.38\\%$ (3 s.f.) *(A1)*.  \n"
                    "**(b)** With $\\pi \\approx 3$: $d = \\dfrac{2.51}{3} = 0.8367$ m *(M1)*. "
                    "The true diameter is $\\dfrac{2.51}{\\pi} = 0.7990$ m. So $\\varepsilon = "
                    "\\left|\\dfrac{0.8367 - 0.7990}{0.7990}\\right| \\times 100$ *(A1)* $= "
                    "4.72\\%$ *(A1)*.  \n"
                    "**Narrative:** the exact value is always the denominator, and here part (b) "
                    "makes you decide what 'exact' means — the value computed with the true "
                    "$\\pi$. Using $3$ for $\\pi$ understates $\\pi$ by about $4.5\\%$, and "
                    "because $\\pi$ is in a denominator, the error in $d$ comes out slightly "
                    "larger in the other direction."
                ),
                "check": [
                    "Abs(Abs((Rational(24, 10) - Rational(251, 100))/Rational(251, 100))*100 - Rational(438, 100)) < Rational(5, 1000)",
                    "Abs(Rational(251, 100)/3 - Rational(8367, 10000)) < Rational(1, 10000)",
                    "Abs(Rational(251, 100)/pi - Rational(7990, 10000)) < Rational(1, 10000)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Dividing by the approximate value when computing percentage error.",
                "correction": "The EXACT value is the denominator: $\\left|\\frac{v_A - v_E}{v_E}\\right| \\times 100$.",
                "authored": True,
            },
            {
                "text": "Giving the bounds of $6.4$ (1 d.p.) as $6.3$ and $6.5$.",
                "correction": "Bounds sit HALF a unit either side: $6.35$ and $6.45$.",
                "authored": True,
            },
            {
                "text": "Counting leading zeros as significant: calling $0.00305$ five significant figures.",
                "correction": "Significant figures start at the first non-zero digit — $0.00305$ has three.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-16-t1",
                "statement": (
                    "Write $0.040\\,682$ to **(a)** 3 significant figures and **(b)** 3 decimal "
                    "places. **[2]**"
                ),
                "solution": (
                    "**(a)** The first significant figure is the 4, so three of them give "
                    "$0.0407$ *(A1)*.  \n"
                    "**(b)** Counting three places from the point: $0.041$ *(A1)*.  \n"
                    "Same number, different instructions, different answers — read which one is "
                    "being asked for."
                ),
                "check": [
                    "Abs(Rational(40682, 1000000) - Rational(407, 10000)) < Rational(5, 100000)",
                    "Abs(Rational(40682, 1000000) - Rational(41, 1000)) < Rational(5, 10000)",
                ],
            },
            {
                "id": "aisl-16-t2",
                "statement": (
                    "A runner's time is recorded as $54$ seconds, to the nearest second, over a "
                    "track measured as $400$ m to the nearest metre. Find the upper bound of "
                    "the runner's average speed, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "Speed is largest with the LONGEST distance and the SHORTEST time *(M1)*: "
                    "$\\dfrac{400.5}{53.5}$ *(A1)* $= 7.49$ m s$^{-1}$ *(A1)*.  \n"
                    "In a quotient the two bounds pull in opposite directions — the single most "
                    "examined idea in this code."
                ),
                "check": [
                    "400 + Rational(1, 2) == Rational(801, 2)",
                    "54 - Rational(1, 2) == Rational(107, 2)",
                    "Abs(Rational(801, 2)/Rational(107, 2) - Rational(749, 100)) < Rational(5, 1000)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.6 · Papers 1 & 2",
                    "title": "A number needs an accuracy",
                    "body": (
                        "This code belongs to AI alone. Applications & Interpretation takes the "
                        "position that a measurement is a RANGE, that rounding propagates through "
                        "a calculation, and that saying how wrong an approximation might be is "
                        "part of doing the mathematics — not an afterthought."
                    ),
                },
                {
                    "kind": "decimalRounder",
                    "eyebrow": "See the rounding",
                    "title": "Places against figures",
                    "teach": (
                        "Round $\\pi$ place by place and watch the kept digit change. Decimal "
                        "places count from the point; significant figures count from the first "
                        "non-zero digit. For $\\pi$ the two rules agree, which is why $\\pi$ "
                        "hides the distinction; for a number like $0.00408$ they give completely "
                        "different answers, and that is why the exam always says which one it "
                        "wants."
                    ),
                    "config": {"value": 3.14159, "place": "hundredth"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Bounds",
                    "title": "Half a unit either side",
                    "beats": [
                        "Rounded to the nearest $u$, the true value lies within $\\pm\\frac{u}{2}$.",
                        "$80$ to the nearest $10$: bounds $75$ and $85$. $6.4$ to 1 d.p.: bounds $6.35$ and $6.45$.",
                        "Products: both bounds move the same way. Quotients: numerator up, denominator DOWN for the maximum.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Bounds of an area",
                    "problemId": "aisl-16-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Bound check",
                    "title": "To the nearest 10",
                    "prompt": "A crowd is reported as $2400$ to the nearest hundred. The lower bound is",
                    "options": ["$2350$", "$2390$", "$2300$", "$2395$"],
                    "correctIndex": 0,
                    "explanation": (
                        "The rounding unit is $100$, so the bounds are $50$ either side: $2350$ "
                        "and $2450$."
                    ),
                    "check": ["2400 - Rational(100, 2) == 2350", "2400 + Rational(100, 2) == 2450"],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Percentage error, twice",
                    "problemId": "aisl-16-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Which is the denominator?",
                    "title": "Estimate 300, true value 250",
                    "prompt": "The percentage error is",
                    "options": ["$20\\%$", "$16.7\\%$", "$-20\\%$", "$50\\%$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$\\left|\\frac{300 - 250}{250}\\right| \\times 100 = 20\\%$. Dividing by "
                        "the approximate $300$ instead gives $16.7\\%$ — the classic wrong "
                        "denominator."
                    ),
                    "check": [
                        "Abs(Rational(300 - 250, 250))*100 == 20",
                        "Abs(Rational(300 - 250, 300))*100 == Rational(50, 3)",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Round only at the end",
                    "body": (
                        "Carry full calculator accuracy through every intermediate step and round "
                        "ONCE, on the answer line. Rounding early and then continuing is a real "
                        "source of lost A-marks: your final digit drifts and the markscheme's "
                        "tolerance will not save you. The IB default, unless told otherwise, is "
                        "3 significant figures."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-16-t1"},
                {"kind": "tryIt", "problemId": "aisl-16-t2"},
                {
                    "kind": "recap",
                    "title": "Accuracy, compressed",
                    "beats": [
                        "Significant figures start at the first non-zero digit; decimal places start at the point.",
                        "A value rounded to the nearest $u$ has bounds $\\pm\\frac{u}{2}$.",
                        "$\\varepsilon = \\left|\\frac{v_A - v_E}{v_E}\\right| \\times 100$ — exact value on the bottom.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 7 — AI SL 1.7: amortization and annuities  (AI-only code)
# ===========================================================================
def lesson_amortization():
    return {
        "slug": "amortization-and-annuities",
        "title": "Loans, Annuities & the Finance Solver",
        "concreteComparison": (
            "Borrow $\\$20\\,000$ over 5 years at $7\\%$ and you repay about $\\$396$ a month — "
            "$\\$23\\,760$ in total. The extra $\\$3760$ is what the loan cost. No formula on "
            "the page gets you there; the calculator's finance solver does, and knowing how to "
            "drive it IS the syllabus content."
        ),
        "objective": (
            "Use technology to solve amortization and annuity problems: find the payment, the "
            "term, the rate or the balance, with the sign convention handled correctly."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.7.** Amortization and annuities using technology. "
            "**Papers 1 and 2.** Another AI-only code, and an unusual one: the syllabus "
            "explicitly names TECHNOLOGY as the method. There is no closed formula to memorise — "
            "the assessment is whether you can set the solver up and read what it returns.",
            "An AMORTIZED loan is repaid by equal instalments; each instalment covers the "
            "interest accrued since the last one and puts the remainder against the balance. "
            "Early payments are mostly interest; late payments are mostly principal. An ANNUITY "
            "is the mirror image — a lump sum that pays out equal instalments until exhausted.",
            "The GDC's TVM solver has five slots: $N$ (number of payment periods), $I\\%$ (annual "
            "interest rate), $PV$ (present value), $PMT$ (payment per period), $FV$ (future "
            "value). Enter four, solve for the fifth. Also set $P/Y$ and $C/Y$ — payments and "
            "compounds per year — which are 12 for a monthly loan.",
            "The sign convention is the whole battle. Money flowing TO you is positive; money "
            "flowing FROM you is negative. Borrowing $\\$20\\,000$ means $PV = 20\\,000$ "
            "(you receive it) and $PMT$ comes back negative (you pay it). Enter both as "
            "positive and the solver returns an answer that is confidently, silently wrong."
        ],
        "keyIdea": (
            "Four slots in, one slot out — and opposite signs for money in and money out. The "
            "solver is the method, not a shortcut around it."
        ),
        "facts": [
            {
                "title": "The five TVM slots",
                "latex": "N,\\quad I\\%,\\quad PV,\\quad PMT,\\quad FV",
                "explanation": "NOT in the booklet — calculator knowledge the syllabus assumes. Set P/Y and C/Y to the payments per year.",
            },
            {
                "title": "Total paid and total interest",
                "latex": "\\text{Total paid} = N \\times |PMT|, \\qquad \\text{Interest} = \\text{Total paid} - PV",
                "explanation": "NOT in the booklet. The most common follow-up part in this code.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-17-we1",
                "statement": (
                    "Ana borrows $\\$18\\,000$ to be repaid in equal monthly instalments over 4 "
                    "years. The bank charges $6\\%$ per annum, compounded monthly.  \n"
                    "**(a)** Find the monthly repayment, to the nearest cent. **[3]**  \n"
                    "**(b)** Find the total interest Ana pays over the 4 years. **[2]**"
                ),
                "solution": (
                    "**(a)** In the TVM solver: $N = 48$, $I\\% = 6$, $PV = 18\\,000$, $FV = 0$, "
                    "$P/Y = C/Y = 12$ *(M1 A1)*. Solving for $PMT$ gives $-422.73$, so the "
                    "repayment is $\\$422.73$ per month *(A1)*.  \n"
                    "**(b)** Total paid $= 48 \\times 422.73 = \\$20\\,291.04$ *(M1)*, so the "
                    "interest is $20\\,291.04 - 18\\,000 = \\$2291.04$ *(A1)*.  \n"
                    "**Narrative:** $N$ counts PAYMENTS, not years — $4 \\times 12 = 48$. The "
                    "negative $PMT$ is the solver saying 'this leaves your account', which is "
                    "correct; report it as a positive repayment. Part (b) is where the marks "
                    "are most often dropped, by subtracting from the wrong thing: interest is "
                    "total paid MINUS the amount borrowed."
                ),
                "check": [
                    "4*12 == 48",
                    "Abs(48*Rational(42273, 100) - Rational(2029104, 100)) < Rational(1, 100)",
                    "Abs(Rational(2029104, 100) - 18000 - Rational(229104, 100)) < Rational(1, 100)",
                ],
            },
            {
                "id": "aisl-17-we2",
                "statement": (
                    "Ben has $\\$150\\,000$ in a retirement account earning $4.8\\%$ per annum "
                    "compounded monthly. He withdraws $\\$1200$ at the end of each month.  \n"
                    "**(a)** Find how many complete months the account will last. **[3]**  \n"
                    "**(b)** Explain what would happen if the monthly withdrawal were $\\$600$. "
                    "**[2]**"
                ),
                "solution": (
                    "**(a)** TVM: $I\\% = 4.8$, $PV = -150\\,000$, $PMT = 1200$, $FV = 0$, "
                    "$P/Y = C/Y = 12$ *(M1)*. Solving for $N$ gives $N = 176.6$ *(A1)*, so the "
                    "account lasts $176$ complete months *(A1)*.  \n"
                    "**(b)** Monthly interest on $\\$150\\,000$ at $4.8\\%$ p.a. is "
                    "$150\\,000 \\times \\dfrac{0.048}{12} = \\$600$ *(M1)*. A withdrawal of "
                    "exactly $\\$600$ removes only the interest, so the balance never falls — "
                    "the annuity lasts forever *(A1)*.  \n"
                    "**Narrative:** here $PV$ is negative because Ben PAYS the money into the "
                    "account and $PMT$ is positive because he RECEIVES the withdrawals — the "
                    "mirror of the loan. Part (b) is the conceptual payoff: there is a "
                    "withdrawal rate at which an annuity becomes perpetual, and it is exactly "
                    "the interest."
                ),
                "check": [
                    "150000*Rational(48, 1000)/12 == 600",
                    "Rational(48, 1000)/12 == Rational(4, 1000)",
                    "150000*Rational(4, 1000) == 600",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Entering $N$ as the number of YEARS for a monthly loan.",
                "correction": "$N$ counts payment periods. Four years of monthly payments is $N = 48$.",
                "authored": True,
            },
            {
                "text": "Giving $PV$ and $PMT$ the same sign.",
                "correction": "Money in and money out have opposite signs. Borrowing: $PV$ positive, $PMT$ negative.",
                "authored": True,
            },
            {
                "text": "Reporting total interest as 'total paid minus one payment' or as the final balance.",
                "correction": "Interest $= N \\times |PMT| - PV$: everything you paid, less what you borrowed.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-17-t1",
                "statement": (
                    "A $\\$9000$ car loan is repaid monthly over 3 years at $8\\%$ per annum "
                    "compounded monthly. Find the monthly repayment, to the nearest cent, and "
                    "the total interest paid. **[4]**"
                ),
                "solution": (
                    "$N = 36$, $I\\% = 8$, $PV = 9000$, $FV = 0$, $P/Y = C/Y = 12$ *(M1)*. "
                    "$PMT = -282.03$, so the repayment is $\\$282.03$ *(A1)*.  \n"
                    "Total paid $= 36 \\times 282.03 = \\$10\\,153.08$ *(M1)*; interest "
                    "$= \\$1153.08$ *(A1)*."
                ),
                "check": [
                    "3*12 == 36",
                    "Abs(36*Rational(28203, 100) - Rational(1015308, 100)) < Rational(1, 100)",
                    "Abs(Rational(1015308, 100) - 9000 - Rational(115308, 100)) < Rational(1, 100)",
                ],
            },
            {
                "id": "aisl-17-t2",
                "statement": (
                    "An account holds $\\$80\\,000$ at $5.4\\%$ per annum compounded monthly. "
                    "Find the monthly withdrawal that would leave the balance unchanged forever. "
                    "**[2]**"
                ),
                "solution": (
                    "The monthly interest is $80\\,000 \\times \\dfrac{0.054}{12}$ *(M1)* "
                    "$= \\$360$ *(A1)*.  \n"
                    "Withdraw exactly the interest and the principal is untouched — the "
                    "perpetuity condition."
                ),
                "check": [
                    "Rational(54, 1000)/12 == Rational(45, 10000)",
                    "80000*Rational(45, 10000) == 360",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.7 · Papers 1 & 2",
                    "title": "The syllabus says: use technology",
                    "body": (
                        "This is the most unusual code in Topic 1. There is no formula to learn — "
                        "the IB specifies that amortization and annuities are done with "
                        "technology, and assesses whether you can set the solver up, drive it, "
                        "and interpret what comes back. Marks go to correct SETUP as much as to "
                        "the number."
                    ),
                },
                {
                    "kind": "teach",
                    "eyebrow": "The five slots",
                    "title": "What each letter means",
                    "beats": [
                        "$N$ — number of payment PERIODS (months, not years, for a monthly loan).",
                        "$I\\%$ — the ANNUAL rate, entered as a percentage: 6, not 0.06.",
                        "$PV$ — present value; $PMT$ — payment per period; $FV$ — future value (usually 0 for a loan repaid in full).",
                        "$P/Y$ and $C/Y$ — payments and compounds per year: 12 for monthly.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A loan, and what it costs",
                    "problemId": "aisl-17-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Setup check",
                    "title": "How many periods?",
                    "prompt": "A 7-year loan repaid FORTNIGHTLY (26 payments a year) has",
                    "options": ["$N = 182$", "$N = 7$", "$N = 84$", "$N = 26$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$N$ counts payments: $7 \\times 26 = 182$. Setting $P/Y = C/Y = 26$ as "
                        "well is what makes the annual rate land correctly on each fortnight."
                    ),
                    "check": ["7*26 == 182", "7*12 == 84"],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "An annuity, and when it never runs out",
                    "problemId": "aisl-17-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Sign convention",
                    "title": "Which way does the money move?",
                    "prompt": "You BORROW $\\$5000$ and repay monthly. In the solver,",
                    "options": [
                        "$PV = 5000$ and $PMT$ is negative",
                        "$PV = -5000$ and $PMT$ is negative",
                        "both are positive",
                        "both are negative",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The loan arrives in your account, so $PV$ is positive; the repayments "
                        "leave it, so $PMT$ is negative. Opposite signs, always."
                    ),
                    "check": ["5000 > 0", "-5000 < 0"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Markscheme wisdom",
                    "title": "Write down what you typed",
                    "body": (
                        "A bare number from a finance solver is fragile. Write the five inputs — "
                        "$N = 48$, $I\\% = 6$, $PV = 18000$, $FV = 0$, $P/Y = 12$ — and the M-mark "
                        "is secured even if a keystroke slipped. This is the AI equivalent of "
                        "'show your working', and examiners award it exactly that way."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-17-t1"},
                {"kind": "tryIt", "problemId": "aisl-17-t2"},
                {
                    "kind": "recap",
                    "title": "Loans and annuities, compressed",
                    "beats": [
                        "Four slots in, one out; $N$ counts PAYMENTS.",
                        "Money in and money out take opposite signs.",
                        "Interest $= N \\times |PMT| - PV$; write your inputs down for the method mark.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 8 — AI SL 1.8: systems and polynomials by technology  (AI-only code)
# ===========================================================================
def lesson_solving_with_technology():
    return {
        "slug": "solving-with-technology",
        "title": "Systems & Polynomials on the GDC",
        "concreteComparison": (
            "Three unknowns, three equations, and a page of elimination — or thirty seconds in "
            "the calculator's simultaneous-equation solver. AI takes the second route on "
            "purpose: the mathematics being assessed is setting the system up and reading what "
            "the solution means, not the bookkeeping of eliminating $z$."
        ),
        "objective": (
            "Use technology to solve systems of up to three linear equations in three unknowns "
            "and to solve polynomial equations, and interpret the solutions in context."
        ),
        "concept": [
            "**Syllabus card — AI SL 1.8.** Use of technology to solve systems of linear "
            "equations in up to 3 variables, and polynomial equations. **Papers 1 and 2.** The "
            "third AI-only code in this topic. The exam gives you a context, and the marks are "
            "for TRANSLATING it into equations and for interpreting the answer — the solving "
            "itself is a button.",
            "Translating a context: name your variables explicitly ('let $x$ be the number of "
            "adult tickets'), then write one equation per piece of information. Three unknowns "
            "need three independent facts. Writing 'let $x$, $y$, $z$ be…' is itself worth a "
            "mark on most of these questions.",
            "Systems can have one solution, no solution, or infinitely many. Your GDC will say "
            "so — a 'no solution' message means the planes never meet at a common point, and "
            "'infinitely many' means the equations were not independent. Reporting the message, "
            "with what it means for the context, is the answer.",
            "For polynomial equations, the polynomial-root solver or the graph both work: enter "
            "the coefficients, or graph the function and read the $x$-intercepts. In context, "
            "sift the roots — a negative time, a fractional number of people or a length beyond "
            "the physical range gets REJECTED, and saying why earns the R-mark."
        ],
        "keyIdea": (
            "The calculator solves; you translate and interpret. Define your variables, write "
            "one equation per fact, then sift the roots against the context."
        ),
        "facts": [
            {
                "title": "A 3×3 linear system",
                "latex": "\\begin{cases} a_1x + b_1y + c_1z = d_1 \\\\ a_2x + b_2y + c_2z = d_2 \\\\ a_3x + b_3y + c_3z = d_3 \\end{cases}",
                "explanation": "NOT in the booklet. Enter the coefficient grid into the GDC's simultaneous-equation solver.",
            },
            {
                "title": "Three outcomes",
                "latex": "\\text{unique solution} \\quad|\\quad \\text{no solution} \\quad|\\quad \\text{infinitely many}",
                "explanation": "The GDC reports which. Interpreting the message in context is the assessed skill.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-18-we1",
                "statement": (
                    "A cinema sells adult, student and child tickets. On one evening it sold 250 "
                    "tickets in total and took $\\$2990$. Adult tickets cost $\\$15$, student "
                    "$\\$10$ and child $\\$6$. Twice as many student tickets were sold as child "
                    "tickets.  \n"
                    "**(a)** Write a system of three equations. **[3]**  \n"
                    "**(b)** Solve it. **[3]**"
                ),
                "solution": (
                    "**(a)** Let $a$, $s$, $c$ be the numbers of adult, student and child "
                    "tickets *(A1)*.  \n"
                    "$a + s + c = 250$; $15a + 10s + 6c = 2990$; $s = 2c$ *(A1 A1)*.  \n"
                    "**(b)** Rewriting the third as $s - 2c = 0$ and solving with the GDC "
                    "*(M1)*: $a = 130$, $s = 80$, $c = 40$ *(A2)*.  \n"
                    "**Narrative:** the third fact looks unlike the others but is just another "
                    "linear equation — rearrange it to the same shape before entering the "
                    "coefficients. Then check the answer against ALL THREE facts, not just the "
                    "easy one: $130 + 80 + 40 = 250$ ✓, $80 = 2 \\times 40$ ✓, and "
                    "$15(130) + 10(80) + 6(40) = 1950 + 800 + 240 = 2990$ ✓. That twenty-second "
                    "check is what catches a mistyped coefficient before it costs the A-marks."
                ),
                "check": [
                    "130 + 80 + 40 == 250",
                    "80 == 2*40",
                    "15*130 + 10*80 + 6*40 == 2990",
                ],
            },
            {
                "id": "aisl-18-we2",
                "statement": (
                    "A box is made from a $30$ cm by $20$ cm sheet by cutting squares of side $x$ "
                    "cm from each corner and folding up the sides. Its volume is $1000$ cm$^3$.  \n"
                    "**(a)** Show that $x$ satisfies $4x^{3} - 100x^{2} + 600x - 1000 = 0$. "
                    "**[3]**  \n"
                    "**(b)** Find the possible values of $x$, and state which are valid. **[3]**"
                ),
                "solution": (
                    "**(a)** The base is $(30 - 2x)$ by $(20 - 2x)$ and the height is $x$ "
                    "*(M1)*, so $V = x(30 - 2x)(20 - 2x)$ *(A1)*. Expanding: "
                    "$x(600 - 100x + 4x^{2}) = 4x^{3} - 100x^{2} + 600x$. Setting this equal to "
                    "$1000$ gives $4x^{3} - 100x^{2} + 600x - 1000 = 0$ *(AG)*.  \n"
                    "**(b)** The GDC's polynomial solver gives $x = 2.93$, $x = 5$ and "
                    "$x = 17.1$ (3 s.f.) *(A2)*. Since two squares are cut from the $20$ cm "
                    "side, we need $0 < x < 10$, so $x = 2.93$ or $x = 5$; $x = 17.1$ is "
                    "rejected *(A1)*.  \n"
                    "**Narrative:** part (a) is a 'show that', so the printed cubic earns no mark "
                    "by itself — the marks are in the setup and the expansion. In (b) the "
                    "rejection needs its REASON: cutting squares of side $17.1$ cm from a "
                    "$20$ cm side would leave nothing behind, and saying so is the R-mark."
                ),
                "check": [
                    "expand(x*(30 - 2*x)*(20 - 2*x)) == 4*x**3 - 100*x**2 + 600*x",
                    "5*(30 - 2*5)*(20 - 2*5) == 1000",
                    "expand(4*(x - 5)*(x**2 - 20*x + 50)) == 4*x**3 - 100*x**2 + 600*x - 1000",
                    "Eq(simplify(4*(10 - 5*sqrt(2))**3 - 100*(10 - 5*sqrt(2))**2 + 600*(10 - 5*sqrt(2)) - 1000), 0)",
                    "Abs((10 - 5*sqrt(2)) - Rational(293, 100)) < Rational(1, 100)",
                    "2*(10 + 5*sqrt(2)) > 20",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Not defining the variables before writing the equations.",
                "correction": "'Let $a$ be the number of adult tickets' is a mark. Undefined letters make the rest unmarkable.",
                "authored": True,
            },
            {
                "text": "Accepting every root the calculator returns.",
                "correction": "Sift against the context: negative lengths, negative times and impossible cut sizes are rejected — with a stated reason.",
                "authored": True,
            },
            {
                "text": "Entering $s = 2c$ into the solver without rearranging.",
                "correction": "Every equation must be in the same form. Write it as $s - 2c = 0$ so the coefficient grid lines up.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-18-t1",
                "statement": (
                    "Solve the system $2x + y - z = 8$, $x - y + 2z = -3$, $3x + 2y + z = 11$. "
                    "**[3]**"
                ),
                "solution": (
                    "Entering the coefficients into the GDC's simultaneous solver *(M1)* gives "
                    "$x = 2$, $y = 3$, $z = -1$ *(A2)*.  \n"
                    "Verify in all three: $4 + 3 + 1 = 8$ ✓, $2 - 3 - 2 = -3$ ✓, "
                    "$6 + 6 - 1 = 11$ ✓."
                ),
                "check": [
                    "2*2 + 3 - (-1) == 8",
                    "2 - 3 + 2*(-1) == -3",
                    "3*2 + 2*3 + (-1) == 11",
                ],
            },
            {
                "id": "aisl-18-t2",
                "statement": (
                    "Solve $x^{3} - 6x^{2} + 11x - 6 = 0$. **[2]**"
                ),
                "solution": (
                    "The polynomial solver (or the graph's $x$-intercepts) gives $x = 1$, "
                    "$x = 2$, $x = 3$ *(M1 A1)*.  \n"
                    "Three real roots, all integers — check one by substitution: "
                    "$8 - 24 + 22 - 6 = 0$ ✓."
                ),
                "check": [
                    "solve(x**3 - 6*x**2 + 11*x - 6, x) == [1, 2, 3]",
                    "2**3 - 6*2**2 + 11*2 - 6 == 0",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 1.8 · Papers 1 & 2",
                    "title": "The calculator solves; you model",
                    "body": (
                        "AI puts the algebra of elimination out of scope and the MODELLING in "
                        "its place. Given a context, your job is to name variables, extract one "
                        "equation per fact, hand the system to the machine, and then decide what "
                        "the numbers mean — including which of them to throw away."
                    ),
                },
                {
                    "kind": "systemGraph",
                    "eyebrow": "See the intersection",
                    "title": "Where the lines meet",
                    "teach": (
                        "Two equations in two unknowns are two lines: they cross once, never, or "
                        "everywhere. Drag them and watch the three cases appear. In three "
                        "unknowns the same story runs with planes — and the GDC reports which "
                        "case you are in."
                    ),
                    "config": {"m1": -1, "b1": 5, "m2": 2, "b2": -1, "interactive": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "From words to a coefficient grid",
                    "beats": [
                        "Define every variable in words first — it is a mark.",
                        "One equation per given fact; three unknowns need three independent facts.",
                        "Rearrange each to $ax + by + cz = d$ before entering coefficients.",
                        "Read the GDC's verdict: unique, none, or infinitely many.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Three ticket types",
                    "problemId": "aisl-18-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Rearrange first",
                    "title": "Same form, please",
                    "prompt": "To enter $y = 3x - 4$ into a simultaneous solver, write it as",
                    "options": [
                        "$-3x + y = -4$",
                        "$3x + y = -4$",
                        "$y - 3x = 4$",
                        "$3x - y = -4$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Move everything but the constant to the left: $y - 3x = -4$, i.e. "
                        "$-3x + y = -4$. Multiplying through by $-1$ gives $3x - y = 4$, which is "
                        "equally valid — but then EVERY term changes sign, the constant included."
                    ),
                    "check": [
                        "3*2 - 4 == 2",
                        "-3*2 + 2 == -4",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A cubic from a box",
                    "problemId": "aisl-18-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Sift the roots",
                    "title": "Which root survives?",
                    "prompt": (
                        "A time $t$ (seconds) satisfies $t^{2} - 3t - 10 = 0$. The valid solution is"
                    ),
                    "options": ["$t = 5$", "$t = -2$", "both", "neither"],
                    "correctIndex": 0,
                    "explanation": (
                        "The roots are $5$ and $-2$; a negative time has no meaning in the "
                        "context, so it is rejected — and saying WHY is the R-mark."
                    ),
                    "check": [
                        "solve(t**2 - 3*t - 10, t) == [-2, 5]",
                        "5**2 - 3*5 - 10 == 0",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Check against every equation",
                    "body": (
                        "A mistyped coefficient produces a confident, wrong triple. Substituting "
                        "your solution back into ALL the original equations takes twenty seconds "
                        "and catches it — and in a context question, also catches the answer "
                        "that is arithmetically fine but physically absurd."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-18-t1"},
                {"kind": "tryIt", "problemId": "aisl-18-t2"},
                {
                    "kind": "recap",
                    "title": "Solving by technology, compressed",
                    "beats": [
                        "Define variables, one equation per fact, rearrange to a common form.",
                        "The GDC reports unique / none / infinitely many — interpret it.",
                        "Sift roots against the context and state the reason for each rejection.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Unit banks
# ===========================================================================
def practice_bank():
    return [
        {
            "id": "aisl-na-p01",
            "statement": "Write $0.000\\,0624$ in standard form. **[1]**",
            "solution": "$6.24 \\times 10^{-5}$ *(A1)*.",
            "badges": [{"text": "ib-ai-sl-1.1", "mono": True}, {"text": "P1"}],
            "check": ["Rational(624, 100)*10**(-5) == Rational(624, 10000000)"],
        },
        {
            "id": "aisl-na-p02",
            "statement": (
                "Given $p = 3.2 \\times 10^{6}$ and $q = 8 \\times 10^{-2}$, find $pq$ in "
                "standard form. **[2]**"
            ),
            "solution": "$pq = 25.6 \\times 10^{4} = 2.56 \\times 10^{5}$ *(M1 A1)*.",
            "badges": [{"text": "ib-ai-sl-1.1", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(32, 10)*8 == Rational(256, 10)",
                "Rational(256, 10)*10**4 == Rational(256, 100)*10**5",
            ],
        },
        {
            "id": "aisl-na-p03",
            "statement": (
                "An arithmetic sequence has $u_1 = 9$ and $d = 4$. Find $u_{25}$ and $S_{25}$. "
                "**[4]**"
            ),
            "solution": (
                "$u_{25} = 9 + 24 \\times 4 = 105$ *(M1 A1)*; "
                "$S_{25} = \\frac{25}{2}(9 + 105) = 1425$ *(M1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.2", "mono": True}, {"text": "P1"}],
            "check": ["9 + 24*4 == 105", "Rational(25, 2)*(9 + 105) == 1425"],
        },
        {
            "id": "aisl-na-p04",
            "statement": "Evaluate $\\displaystyle\\sum_{r=1}^{20}(3r - 1)$. **[3]**",
            "solution": (
                "First term $2$, last term $59$, twenty terms: "
                "$\\frac{20}{2}(2 + 59) = 610$ *(M1 A1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.2", "mono": True}, {"text": "P1"}],
            "check": [
                "3*1 - 1 == 2",
                "3*20 - 1 == 59",
                "Sum(3*r - 1, (r, 1, 20)).doit() == 610",
            ],
        },
        {
            "id": "aisl-na-p05",
            "statement": (
                "The third term of a geometric sequence is $12$ and the sixth is $96$. Find the "
                "common ratio and the first term. **[4]**"
            ),
            "solution": (
                "$\\frac{u_6}{u_3} = r^{3} = \\frac{96}{12} = 8$ *(M1)*, so $r = 2$ *(A1)*. "
                "Then $u_1 = \\frac{12}{r^{2}} = 3$ *(M1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.3", "mono": True}, {"text": "P1"}],
            "check": ["Rational(96, 12) == 8", "2**3 == 8", "Rational(12, 4) == 3", "3*2**2 == 12"],
        },
        {
            "id": "aisl-na-p06",
            "statement": (
                "A town's population of $52\\,000$ grows by $2.4\\%$ each year. Find the "
                "population after 12 years, to the nearest hundred. **[3]**"
            ),
            "solution": (
                "$52\\,000 \\times 1.024^{12}$ *(M1 A1)* $= 69\\,200$ to the nearest hundred "
                "*(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.3", "mono": True}, {"text": "P2"}],
            "check": [
                "1 + Rational(24, 1000) == Rational(1024, 1000)",
                "Abs(52000*Rational(1024, 1000)**12 - 69200) < 100",
            ],
        },
        {
            "id": "aisl-na-p07",
            "statement": (
                "$\\$12\\,000$ is invested at $5\\%$ per annum compounded half-yearly. Find the "
                "value after 8 years, to the nearest dollar. **[3]**"
            ),
            "solution": (
                "$k = 2$, $n = 8$: $12\\,000\\left(1 + \\frac{5}{200}\\right)^{16}$ *(M1 A1)* "
                "$= \\$17\\,814$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.4", "mono": True}, {"text": "P2"}],
            "check": [
                "2*8 == 16",
                "floor(12000*(1 + Rational(5, 200))**16) == 17814",
            ],
        },
        {
            "id": "aisl-na-p08",
            "statement": (
                "A tractor bought for $\\$68\\,000$ depreciates at $11\\%$ per year. Find its "
                "value after 5 years, to the nearest dollar. **[2]**"
            ),
            "solution": "$68\\,000 \\times 0.89^{5}$ *(M1)* $= \\$37\\,972$ (nearest dollar) *(A1)*.",
            "badges": [{"text": "ib-ai-sl-1.4", "mono": True}, {"text": "P2"}],
            "check": [
                "1 - Rational(11, 100) == Rational(89, 100)",
                "floor(68000*Rational(89, 100)**5) == 37971",
            ],
        },
        {
            "id": "aisl-na-p09",
            "statement": "Simplify $\\dfrac{(3a^{4})^{2}}{9a^{-1}}$. **[3]**",
            "solution": (
                "Numerator $= 9a^{8}$ *(M1)*. Dividing: $\\frac{9}{9} = 1$ and $a^{8 - (-1)} = "
                "a^{9}$ *(A1)*, giving $a^{9}$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.5", "mono": True}, {"text": "P1"}],
            "check": ["3**2 == 9", "4*2 == 8", "8 - (-1) == 9"],
        },
        {
            "id": "aisl-na-p10",
            "statement": (
                "Solve $200 \\times 1.08^{t} = 500$, giving $t$ to 3 s.f. **[3]**"
            ),
            "solution": (
                "$1.08^{t} = 2.5$ *(M1)*, so $t = \\dfrac{\\ln 2.5}{\\ln 1.08}$ *(A1)* "
                "$= 11.9$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.5", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(500, 200) == Rational(5, 2)",
                "Abs(log(Rational(5, 2))/log(Rational(108, 100)) - Rational(119, 10)) < Rational(5, 100)",
            ],
        },
        {
            "id": "aisl-na-p11",
            "statement": (
                "A mass is recorded as $4.7$ kg, correct to 1 decimal place. Write down its "
                "lower and upper bounds. **[2]**"
            ),
            "solution": "Lower $4.65$ kg, upper $4.75$ kg *(A1 A1)*.",
            "badges": [{"text": "ib-ai-sl-1.6", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(47, 10) - Rational(5, 100) == Rational(465, 100)",
                "Rational(47, 10) + Rational(5, 100) == Rational(475, 100)",
            ],
        },
        {
            "id": "aisl-na-p12",
            "statement": (
                "A student estimates a distance as $45$ km when the true distance is $48$ km. "
                "Find the percentage error. **[2]**"
            ),
            "solution": (
                "$\\left|\\frac{45 - 48}{48}\\right| \\times 100$ *(M1)* $= 6.25\\%$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.6", "mono": True}, {"text": "P1"}],
            "check": ["Abs(Rational(45 - 48, 48))*100 == Rational(25, 4)"],
        },
        {
            "id": "aisl-na-p13",
            "statement": (
                "A loan of $\\$25\\,000$ is repaid monthly over 6 years at $9\\%$ per annum "
                "compounded monthly. Find the monthly repayment, to the nearest cent. **[3]**"
            ),
            "solution": (
                "$N = 72$, $I\\% = 9$, $PV = 25\\,000$, $FV = 0$, $P/Y = C/Y = 12$ *(M1 A1)*: "
                "$PMT = -450.99$, so $\\$450.99$ per month *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.7", "mono": True}, {"text": "P2"}],
            "check": [
                "6*12 == 72",
                "Abs(72*Rational(45099, 100) - Rational(3247128, 100)) < Rational(1, 100)",
            ],
        },
        {
            "id": "aisl-na-p14",
            "statement": (
                "For the loan in the previous question, find the total interest paid over the 6 "
                "years. **[2]**"
            ),
            "solution": (
                "Total paid $= 72 \\times 450.99 = \\$32\\,471.28$ *(M1)*; interest "
                "$= 32\\,471.28 - 25\\,000 = \\$7471.28$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.7", "mono": True}, {"text": "P2"}],
            "check": [
                "Abs(Rational(3247128, 100) - 25000 - Rational(747128, 100)) < Rational(1, 100)",
            ],
        },
        {
            "id": "aisl-na-p15",
            "statement": (
                "Solve the system $x + y + z = 6$, $2x - y + z = 3$, $x + 2y - z = 2$. **[3]**"
            ),
            "solution": (
                "Entering the coefficients into the GDC's simultaneous solver *(M1)* gives "
                "$x = 1$, $y = 2$, $z = 3$ *(A2)*. Check: $1 + 2 + 3 = 6$ ✓, "
                "$2 - 2 + 3 = 3$ ✓, $1 + 4 - 3 = 2$ ✓."
            ),
            "badges": [{"text": "ib-ai-sl-1.8", "mono": True}, {"text": "P2"}],
            "check": [
                "1 + 2 + 3 == 6",
                "2*1 - 2 + 3 == 3",
                "1 + 2*2 - 3 == 2",
            ],
        },
        {
            "id": "aisl-na-p16",
            "statement": "Solve $2x^{3} - 3x^{2} - 11x + 6 = 0$. **[3]**",
            "solution": (
                "The polynomial solver gives $x = -2$, $x = \\frac{1}{2}$, $x = 3$ *(M1 A2)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.8", "mono": True}, {"text": "P2"}],
            "check": [
                "solve(2*x**3 - 3*x**2 - 11*x + 6, x) == [-2, Rational(1, 2), 3]",
                "2*(-2)**3 - 3*(-2)**2 - 11*(-2) + 6 == 0",
            ],
        },
        {
            "id": "aisl-na-p17",
            "statement": (
                "The first term of an arithmetic sequence is $80$ and the tenth term is $26$. "
                "Find the common difference. **[2]**"
            ),
            "solution": "$26 = 80 + 9d$ *(M1)*, so $d = -6$ *(A1)*.",
            "badges": [{"text": "ib-ai-sl-1.2", "mono": True}, {"text": "P1"}],
            "check": ["80 + 9*(-6) == 26", "solve(80 + 9*d - 26, d) == [-6]"],
        },
        {
            "id": "aisl-na-p18",
            "statement": (
                "A rectangle measures $8.3$ cm by $5.6$ cm, each to 1 d.p. Find the lower bound "
                "of its perimeter. **[3]**"
            ),
            "solution": (
                "Lower bounds $8.25$ and $5.55$ *(M1)*. Perimeter $= 2(8.25 + 5.55)$ *(A1)* "
                "$= 27.6$ cm *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.6", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(83, 10) - Rational(5, 100) == Rational(825, 100)",
                "2*(Rational(825, 100) + Rational(555, 100)) == Rational(276, 10)",
            ],
        },
    ]


def test_bank():
    return [
        {
            "id": "aisl-na-x01",
            "statement": (
                "Light travels at $3.0 \\times 10^{8}$ m s$^{-1}$. Find the distance it travels "
                "in $4.5 \\times 10^{-3}$ seconds, in standard form. **[3]**"
            ),
            "solution": (
                "$(3.0 \\times 10^{8})(4.5 \\times 10^{-3}) = 13.5 \\times 10^{5}$ *(M1 A1)* "
                "$= 1.35 \\times 10^{6}$ m *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.1", "mono": True}, {"text": "P1"}],
            "check": [
                "3*Rational(45, 10) == Rational(135, 10)",
                "8 + (-3) == 5",
                "Rational(135, 10)*10**5 == Rational(135, 100)*10**6",
            ],
        },
        {
            "id": "aisl-na-x02",
            "statement": (
                "A stack of logs has 30 logs in the bottom row, 28 in the next, and so on, down "
                "to 4 in the top row.  \n"
                "**(a)** How many rows are there? **[3]**  \n"
                "**(b)** How many logs in total? **[2]**"
            ),
            "solution": (
                "**(a)** $u_1 = 30$, $d = -2$, $u_n = 4$: $4 = 30 - 2(n-1)$ *(M1)*, so "
                "$n - 1 = 13$ and $n = 14$ rows *(A1 A1)*.  \n"
                "**(b)** $S_{14} = \\frac{14}{2}(30 + 4) = 238$ logs *(M1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.2", "mono": True}, {"text": "P1"}],
            "check": [
                "30 - 2*13 == 4",
                "Rational(14, 2)*(30 + 4) == 238",
            ],
        },
        {
            "id": "aisl-na-x03",
            "statement": (
                "A car's value falls from $\\$26\\,000$ to $\\$15\\,000$ over 4 years.  \n"
                "**(a)** Find the annual depreciation rate, to 3 s.f. **[3]**  \n"
                "**(b)** Predict its value after a further 3 years. **[2]**"
            ),
            "solution": (
                "**(a)** $26\\,000r^{4} = 15\\,000$ *(M1)*, so $r = \\left(\\frac{15}{26}\\right)"
                "^{1/4} = 0.8715$ *(A1)*; the rate is $12.8\\%$ *(A1)*.  \n"
                "**(b)** $15\\,000 \\times 0.8715^{3}$ *(M1)* $= \\$9930$ (3 s.f.) *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.4", "mono": True}, {"text": "P2"}],
            "check": [
                "Abs((Rational(15, 26))**Rational(1, 4) - Rational(8715, 10000)) < Rational(1, 10000)",
                "Abs(100*(1 - (Rational(15, 26))**Rational(1, 4)) - Rational(128, 10)) < Rational(5, 100)",
                "Abs(15000*(Rational(15, 26))**Rational(3, 4) - 9930) < 5",
            ],
        },
        {
            "id": "aisl-na-x04",
            "statement": (
                "Solve $8 \\times 3^{x} = 500$, giving your answer to 3 s.f. **[3]**"
            ),
            "solution": (
                "$3^{x} = 62.5$ *(M1)*, so $x = \\dfrac{\\ln 62.5}{\\ln 3}$ *(A1)* $= 3.76$ "
                "*(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.5", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(500, 8) == Rational(125, 2)",
                "Abs(log(Rational(125, 2))/log(3) - Rational(376, 100)) < Rational(5, 1000)",
            ],
        },
        {
            "id": "aisl-na-x05",
            "statement": (
                "The side of a square is measured as $12$ cm, correct to the nearest "
                "centimetre.  \n"
                "**(a)** Write down the upper bound of the side. **[1]**  \n"
                "**(b)** Find the upper bound of the area. **[2]**  \n"
                "**(c)** Find the percentage error if the area is taken to be $144$ cm$^2$ when "
                "the true side is $12.5$ cm. **[3]**"
            ),
            "solution": (
                "**(a)** $12.5$ cm *(A1)*.  \n"
                "**(b)** $12.5^{2} = 156.25$ cm$^2$ *(M1 A1)*.  \n"
                "**(c)** True area $= 156.25$; $\\left|\\frac{144 - 156.25}{156.25}\\right| "
                "\\times 100$ *(M1 A1)* $= 7.84\\%$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.6", "mono": True}, {"text": "P1"}],
            "check": [
                "12 + Rational(1, 2) == Rational(25, 2)",
                "Rational(25, 2)**2 == Rational(625, 4)",
                "Abs(Rational(144, 1) - Rational(625, 4))/Rational(625, 4)*100 == Rational(784, 100)",
            ],
        },
        {
            "id": "aisl-na-x06",
            "statement": (
                "Jo borrows $\\$40\\,000$ over 10 years at $6.5\\%$ per annum compounded "
                "monthly, repaid in equal monthly instalments.  \n"
                "**(a)** Find the monthly repayment. **[3]**  \n"
                "**(b)** Find the total amount repaid. **[2]**"
            ),
            "solution": (
                "**(a)** $N = 120$, $I\\% = 6.5$, $PV = 40\\,000$, $FV = 0$, $P/Y = C/Y = 12$ "
                "*(M1 A1)*: $PMT = -454.23$, so $\\$454.23$ *(A1)*.  \n"
                "**(b)** $120 \\times 454.23 = \\$54\\,507.60$ *(M1 A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.7", "mono": True}, {"text": "P2"}],
            "check": [
                "10*12 == 120",
                "Abs(120*Rational(45423, 100) - Rational(5450760, 100)) < Rational(1, 100)",
            ],
        },
        {
            "id": "aisl-na-x07",
            "statement": (
                "A shop sells three sizes of candle. A small costs $\\$4$, a medium $\\$7$ and a "
                "large $\\$12$. One day it sold 90 candles for $\\$615$, and it sold twice as "
                "many small as large.  \n"
                "**(a)** Write down three equations. **[3]**  \n"
                "**(b)** Solve for the number of each size sold. **[3]**"
            ),
            "solution": (
                "**(a)** Let $s$, $m$, $l$ be the numbers sold *(A1)*: $s + m + l = 90$; "
                "$4s + 7m + 12l = 615$; $s = 2l$, i.e. $s - 2l = 0$ *(A1 A1)*.  \n"
                "**(b)** The GDC gives $s = 30$, $m = 45$, $l = 15$ *(M1 A2)*. Check all three: "
                "$30 + 45 + 15 = 90$ ✓; $120 + 315 + 180 = 615$ ✓; $30 = 2 \\times 15$ ✓."
            ),
            "badges": [{"text": "ib-ai-sl-1.8", "mono": True}, {"text": "P2"}],
            "check": [
                "30 + 45 + 15 == 90",
                "30 == 2*15",
                "4*30 + 7*45 + 12*15 == 615",
            ],
        },
        {
            "id": "aisl-na-x08",
            "statement": (
                "An investment of $\\$P$ doubles in 9 years under annual compounding. Find the "
                "annual interest rate, to 3 s.f. **[4]**"
            ),
            "solution": (
                "$P(1 + i)^{9} = 2P$, so $(1 + i)^{9} = 2$ *(M1)*. Then $1 + i = 2^{1/9} = "
                "1.0801$ *(A1 A1)*, so the rate is $8.01\\%$ *(A1)*.  \n"
                "The starting amount cancels — doubling time depends only on the rate."
            ),
            "badges": [{"text": "ib-ai-sl-1.4", "mono": True}, {"text": "P2"}],
            "check": [
                "Abs(2**Rational(1, 9) - Rational(10801, 10000)) < Rational(1, 10000)",
                "Abs(100*(2**Rational(1, 9) - 1) - Rational(801, 100)) < Rational(5, 1000)",
            ],
        },
        {
            "id": "aisl-na-x09",
            "statement": (
                "A geometric sequence has $u_1 = 400$ and $r = 0.6$.  \n"
                "**(a)** Find $u_{5}$. **[2]**  \n"
                "**(b)** Find $S_{5}$, to 3 s.f. **[3]**"
            ),
            "solution": (
                "**(a)** $u_5 = 400 \\times 0.6^{4} = 51.84$ *(M1 A1)*.  \n"
                "**(b)** $S_5 = \\dfrac{400(1 - 0.6^{5})}{1 - 0.6}$ *(M1)* $= 922.24$ *(A1)* "
                "$= 922$ (3 s.f.) *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-1.3", "mono": True}, {"text": "P1"}],
            "check": [
                "400*Rational(6, 10)**4 == Rational(5184, 100)",
                "Rational(400*(1 - Rational(6, 10)**5), 1 - Rational(6, 10)) == Rational(92224, 100)",
            ],
        },
    ]


# ===========================================================================
# Assembly
# ===========================================================================
def build():
    lessons = [
        lesson_standard_form(),
        lesson_arithmetic(),
        lesson_geometric(),
        lesson_financial(),
        lesson_exponents_logs(),
        lesson_approximation(),
        lesson_amortization(),
        lesson_solving_with_technology(),
    ]
    return {
        "slug": "number-and-algebra",
        "title": "Number & Algebra",
        "unit": 1,
        "status": "published",
        "blurb": (
            "AI Topic 1, complete: standard form, arithmetic and geometric sequences and "
            "series, compound interest and depreciation, exponents and logarithms, "
            "approximation with bounds and percentage error, amortization and annuities on the "
            "finance solver, and systems and polynomials by technology — AI SL 1.1 to 1.8, "
            "taught to markscheme standard."
        ),
        "buildsOn": (
            "Nothing — this is where the course starts. Three of its eight codes (1.6, 1.7, "
            "1.8) exist only in Applications & Interpretation."
        ),
        "lessons": lessons,
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }


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
