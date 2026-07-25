#!/usr/bin/env python3
"""IB Mathematics: Analysis & Approaches HL — Unit 3 (Topic 3: Geometry &
Trigonometry, AHL).

Builds data/genmath/ib-hl/geometry-and-trigonometry.json: nine lessons, one per
official AHL subtopic code 3.9-3.18 — the reciprocal ratios and inverse trig
functions, compound and double angle identities, the symmetry relationships
that turn one solution into all of them, and then the whole HL vector toolkit:
components and magnitude, the scalar product, vector equations of lines, the
parallel/intersecting/skew classification, the vector product, and planes with
their intersections and angles. HL depth throughout; every numeric claim
sympy-checked; banks tagged ib-aa-hl-3.x.

Run: python3 scripts/ib/build_hl_unit3.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-hl", "geometry-and-trigonometry.json")


def code_badge(code, marks=None, paper=None):
    b = [{"text": code, "mono": True}]
    if marks:
        b.append({"text": f"[{marks} marks]"})
    if paper:
        b.append({"text": paper})
    return b


# ===========================================================================
# Lesson 1 — AHL 3.9: Reciprocal ratios & inverse trigonometric functions
# ===========================================================================
def lesson_reciprocal_inverse():
    return {
        "slug": "reciprocal-and-inverse-trig",
        "title": "Reciprocal Ratios & Inverse Trig Functions",
        "concreteComparison": (
            "A camera has a zoom ring and an aperture ring, and turning one is not the same as "
            "turning the other. $\\sec\\theta$ is the RECIPROCAL of cosine — flip the value. "
            "$\\arccos x$ is the INVERSE — flip the question. Students merge them constantly; "
            "the syllabus separates them on purpose, and so does every markscheme."
        ),
        "objective": (
            "Work fluently with $\\sec$, $\\csc$ and $\\cot$, deploy the two derived Pythagorean "
            "identities to convert and solve trigonometric equations, and evaluate inverse "
            "trigonometric functions correctly inside their restricted ranges."
        ),
        "concept": [
            "**Syllabus card — AHL 3.9.** Definition of the reciprocal trigonometric ratios "
            "$\\sec\\theta$, $\\csc\\theta$ and $\\cot\\theta$; Pythagorean identities "
            "$1 + \\tan^2\\theta = \\sec^2\\theta$ and $1 + \\cot^2\\theta = \\csc^2\\theta$; the "
            "inverse functions $\\arcsin x$, $\\arccos x$, $\\arctan x$, their domains and ranges. "
            "Papers 1 and 2. Weight: 4-7 marks.",
            "**The three reciprocals, and the naming trap.** "
            "$$\\sec\\theta = \\frac{1}{\\cos\\theta}, \\qquad \\csc\\theta = \\frac{1}{\\sin\\theta}, "
            "\\qquad \\cot\\theta = \\frac{1}{\\tan\\theta} = \\frac{\\cos\\theta}{\\sin\\theta}.$$ "
            "The initial letters deliberately do NOT match: **se**cant pairs with **co**sine, "
            "**co**secant pairs with **si**ne. Read the third letter instead — se**C** goes with "
            "cosine, cose**C** goes with sine. Each is undefined exactly where its partner is zero.",
            "**Two identities for free.** Divide $\\sin^2\\theta + \\cos^2\\theta = 1$ by "
            "$\\cos^2\\theta$ and you get $\\tan^2\\theta + 1 = \\sec^2\\theta$; divide it by "
            "$\\sin^2\\theta$ instead and you get $1 + \\cot^2\\theta = \\csc^2\\theta$. Both are "
            "in the booklet, but knowing where they come from means you can rebuild them under "
            "pressure — and it tells you which one to reach for: the equation that already "
            "contains $\\tan$ wants the $\\sec$ version.",
            "**The solving move.** An HL equation mixing $\\sec^2$ with $\\tan$, or $\\csc^2$ with "
            "$\\cot$, is a disguised quadratic. Substitute the identity so ONE ratio survives, "
            "then factorise. $\\sec^2 x + \\tan x = 7$ becomes $\\tan^2 x + \\tan x - 6 = 0$, i.e. "
            "$(\\tan x + 3)(\\tan x - 2) = 0$ — from transcendental to school algebra in one line.",
            "**Inverses need a restricted range, or they are not functions.** Sine takes the value "
            "$0.5$ infinitely often, so 'the angle whose sine is $0.5$' has to be pinned down. The "
            "syllabus pins it thus: "
            "$$\\arcsin: [-1, 1] \\to \\left[-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2}\\right], \\qquad "
            "\\arccos: [-1, 1] \\to [0, \\pi], \\qquad \\arctan: \\mathbb{R} \\to "
            "\\left(-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2}\\right).$$ "
            "Consequence: $\\arcsin(\\sin x) = x$ only when $x$ already lives in that range. "
            "$\\arcsin\\!\\left(\\sin\\frac{5\\pi}{6}\\right) = \\frac{\\pi}{6}$, not "
            "$\\frac{5\\pi}{6}$ — the function must return an answer in $[-\\frac{\\pi}{2}, "
            "\\frac{\\pi}{2}]$, and it does.",
        ],
        "keyIdea": (
            "Reciprocal ratios flip the VALUE; inverse functions flip the QUESTION. "
            "$1 + \\tan^2 = \\sec^2$ and $1 + \\cot^2 = \\csc^2$ turn mixed equations into "
            "quadratics; the inverse functions always answer inside their restricted range, so "
            "$\\arcsin(\\sin x)$ need not be $x$."
        ),
        "facts": [
            {
                "title": "The reciprocal ratios",
                "latex": "\\sec\\theta = \\frac{1}{\\cos\\theta}, \\quad \\csc\\theta = \\frac{1}{\\sin\\theta}, \\quad \\cot\\theta = \\frac{\\cos\\theta}{\\sin\\theta}",
                "explanation": (
                    "IN the HL booklet. Note $\\cot\\theta = \\frac{\\cos\\theta}{\\sin\\theta}$ is "
                    "the safer form — it still works where $\\tan\\theta$ is undefined."
                ),
            },
            {
                "title": "The derived Pythagorean identities",
                "latex": "1 + \\tan^2\\theta = \\sec^2\\theta, \\qquad 1 + \\cot^2\\theta = \\csc^2\\theta",
                "explanation": (
                    "IN the booklet. Both are $\\sin^2 + \\cos^2 = 1$ divided through — by "
                    "$\\cos^2\\theta$ and by $\\sin^2\\theta$ respectively."
                ),
            },
            {
                "title": "Inverse ranges (memorize)",
                "latex": "\\arcsin \\to \\left[-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2}\\right], \\quad \\arccos \\to [0, \\pi], \\quad \\arctan \\to \\left(-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2}\\right)",
                "explanation": (
                    "NOT in the booklet. $\\arccos$ is the odd one out — it runs $0$ to $\\pi$, "
                    "covering quadrants 1 and 2, while the other two straddle zero."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-309-we1",
                "statement": (
                    "Given that $\\tan\\theta = -\\dfrac{3}{4}$ and $\\dfrac{\\pi}{2} < \\theta < "
                    "\\pi$, find the exact values of $\\sec\\theta$, $\\csc\\theta$ and "
                    "$\\cot\\theta$. **[6]**"
                ),
                "solution": (
                    "Use the identity rather than a triangle — the sign is decided by the quadrant, "
                    "not by the sketch *(M1)*:  \n"
                    "$$\\sec^2\\theta = 1 + \\tan^2\\theta = 1 + \\frac{9}{16} = \\frac{25}{16} "
                    "\\;\\Rightarrow\\; \\sec\\theta = \\pm\\frac{5}{4}.$$  \n"
                    "In the second quadrant $\\cos\\theta < 0$, so $\\sec\\theta = -\\frac{5}{4}$ "
                    "*(A1)* and $\\cos\\theta = -\\frac{4}{5}$ *(A1)*.  \n"
                    "Then $\\sin\\theta = \\tan\\theta\\cos\\theta = \\left(-\\frac{3}{4}\\right)"
                    "\\left(-\\frac{4}{5}\\right) = \\frac{3}{5}$ *(M1)* — positive, as the second "
                    "quadrant demands. Hence  \n"
                    "$$\\csc\\theta = \\frac{5}{3}, \\qquad \\cot\\theta = \\frac{1}{\\tan\\theta} "
                    "= -\\frac{4}{3}. \\;(A1\\,A1)$$  \n"
                    "**Narrative:** the quadrant does all the sign work. Check with the second "
                    "identity: $1 + \\cot^2\\theta = 1 + \\frac{16}{9} = \\frac{25}{9} = "
                    "\\csc^2\\theta$ ✓."
                ),
                "check": [
                    "Eq(1 + Rational(-3,4)**2, Rational(25,16))",
                    "Eq(Rational(-3,4)*Rational(-4,5), Rational(3,5))",
                    "Eq(Rational(3,5)**2 + Rational(-4,5)**2, 1)",
                    "Eq(1 + Rational(-4,3)**2, Rational(25,9))",
                    "Eq(1/Rational(3,5), Rational(5,3))",
                ],
            },
            {
                "id": "ibhl-309-we2",
                "statement": (
                    "**(a)** Find the exact value of $\\arccos\\!\\left(-\\dfrac{1}{2}\\right) + "
                    "\\arcsin\\!\\left(-\\dfrac{1}{2}\\right) + \\arctan\\!\\left(-\\sqrt{3}\\right)$. "
                    "**[4]**  \n"
                    "**(b)** Explain why $\\arcsin\\!\\left(\\sin\\dfrac{5\\pi}{6}\\right) \\ne "
                    "\\dfrac{5\\pi}{6}$, and state its value. **[3]**"
                ),
                "solution": (
                    "**(a)** Take each inside its own range *(M1)*:  \n"
                    "$\\arccos\\!\\left(-\\frac{1}{2}\\right) = \\frac{2\\pi}{3}$ — must lie in "
                    "$[0, \\pi]$, so the second-quadrant angle *(A1)*;  \n"
                    "$\\arcsin\\!\\left(-\\frac{1}{2}\\right) = -\\frac{\\pi}{6}$ — must lie in "
                    "$[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$, so NEGATIVE, not $\\frac{7\\pi}{6}$ "
                    "*(A1)*;  \n"
                    "$\\arctan(-\\sqrt3) = -\\frac{\\pi}{3}$ *(A1)*.  \n"
                    "$$\\frac{2\\pi}{3} - \\frac{\\pi}{6} - \\frac{\\pi}{3} = "
                    "\\frac{4\\pi - \\pi - 2\\pi}{6} = \\frac{\\pi}{6}.$$  \n"
                    "**(b)** $\\sin\\frac{5\\pi}{6} = \\frac{1}{2}$ *(A1)*. But $\\arcsin$ must "
                    "return a value in $\\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right]$, and "
                    "$\\frac{5\\pi}{6}$ is outside it *(R1)*. The value in range with sine "
                    "$\\frac{1}{2}$ is $\\frac{\\pi}{6}$, so "
                    "$\\arcsin\\!\\left(\\sin\\frac{5\\pi}{6}\\right) = \\frac{\\pi}{6}$ *(A1)*.  \n"
                    "**Narrative:** $\\arcsin(\\sin x) = x$ is a conditional identity, not a law. "
                    "It holds precisely on the restricted range — everywhere else the function "
                    "folds the input back in."
                ),
                "check": [
                    "Eq(acos(-Rational(1,2)), 2*pi/3)",
                    "Eq(asin(-Rational(1,2)), -pi/6)",
                    "Eq(atan(-sqrt(3)), -pi/3)",
                    "Eq(acos(-Rational(1,2)) + asin(-Rational(1,2)) + atan(-sqrt(3)), pi/6)",
                    "Eq(sin(5*pi/6), Rational(1,2))",
                    "Eq(asin(sin(5*pi/6)), pi/6)",
                    "Ne(asin(sin(5*pi/6)), 5*pi/6)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "$\\sec\\theta$ read as $\\frac{1}{\\sin\\theta}$ because both start with 's'.",
                "correction": "Third letter rule: se**c**ant $\\to$ **c**osine, cose**c**ant $\\to$ **s**ine. $\\sec\\theta = \\frac{1}{\\cos\\theta}$.",
                "authored": True,
            },
            {
                "text": "$\\sec\\theta$ confused with $\\arccos\\theta$ — reciprocal treated as inverse.",
                "correction": "$\\sec\\theta$ is a NUMBER flipped ($1/\\cos\\theta$); $\\arccos x$ is an ANGLE returned. $\\sec\\frac{\\pi}{3} = 2$ but $\\arccos\\frac{\\pi}{3} \\approx 0.281$ — nothing alike.",
                "authored": True,
            },
            {
                "text": "Taking $\\sec\\theta = +\\frac{5}{4}$ from $\\sec^2\\theta = \\frac{25}{16}$ without consulting the quadrant.",
                "correction": "Squaring destroyed the sign; the given interval restores it. Always name the quadrant before choosing the root.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-309-t1",
                "statement": (
                    "Given $\\csc\\theta = \\dfrac{13}{5}$ and $\\theta$ is obtuse, find the exact "
                    "value of $\\cot\\theta$. **[4]**"
                ),
                "solution": (
                    "$\\sin\\theta = \\frac{5}{13}$ *(A1)*. Then $\\cot^2\\theta = \\csc^2\\theta - "
                    "1 = \\frac{169}{25} - 1 = \\frac{144}{25}$ *(M1)*, so $\\cot\\theta = "
                    "\\pm\\frac{12}{5}$. Obtuse means the second quadrant, where cosine — and "
                    "therefore cotangent — is negative *(R1)*:  \n"
                    "$$\\cot\\theta = -\\frac{12}{5}. \\;(A1)$$  \n"
                    "Cross-check with the $5$-$12$-$13$ triangle: $\\cos\\theta = -\\frac{12}{13}$, "
                    "so $\\frac{\\cos\\theta}{\\sin\\theta} = -\\frac{12}{5}$ ✓."
                ),
                "check": [
                    "Eq(1/Rational(13,5), Rational(5,13))",
                    "Eq(Rational(169,25) - 1, Rational(144,25))",
                    "Eq(Rational(-12,13)/Rational(5,13), Rational(-12,5))",
                    "Eq(Rational(5,13)**2 + Rational(-12,13)**2, 1)",
                ],
            },
            {
                "id": "ibhl-309-t2",
                "statement": (
                    "Solve $\\csc^2 x - 3\\cot x - 5 = 0$, giving your answers for $\\cot x$ "
                    "exactly. **[4]**"
                ),
                "solution": (
                    "Replace $\\csc^2 x$ with $1 + \\cot^2 x$ so only one ratio survives *(M1)*:  \n"
                    "$$1 + \\cot^2 x - 3\\cot x - 5 = 0 \\;\\Longleftrightarrow\\; "
                    "\\cot^2 x - 3\\cot x - 4 = 0. \\;(A1)$$  \n"
                    "Factorise *(M1)*: $(\\cot x - 4)(\\cot x + 1) = 0$, so  \n"
                    "$$\\cot x = 4 \\quad\\text{or}\\quad \\cot x = -1, \\qquad\\text{i.e.}\\qquad "
                    "\\tan x = \\tfrac{1}{4} \\;\\text{ or }\\; \\tan x = -1. \\;(A1)$$  \n"
                    "The identity was chosen to match the surviving ratio: $\\csc$ pairs with "
                    "$\\cot$, never with $\\tan$."
                ),
                "check": [
                    "Eq(expand((c - 4)*(c + 1)), c**2 - 3*c - 4)",
                    "Eq(1 + 4**2 - 3*4 - 5, 0)",
                    "Eq(1 + (-1)**2 - 3*(-1) - 5, 0)",
                    "Eq(1/Rational(1,4), 4)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.9 · Papers 1 & 2",
                    "title": "Flip the value, or flip the question",
                    "body": (
                        "Two different operations wear similar names. $\\sec\\theta = "
                        "\\frac{1}{\\cos\\theta}$ takes an angle and returns a flipped NUMBER. "
                        "$\\arccos x$ takes a number and returns an ANGLE. Keeping them apart is "
                        "worth a mark on nearly every HL trig question, because the notation "
                        "$\\cos^{-1}$ is used for the inverse while $\\cos^{2}$ means the square — "
                        "the one genuinely inconsistent piece of notation in the whole syllabus."
                    ),
                },
                {
                    "kind": "unitCircle",
                    "eyebrow": "Where the ratios live",
                    "title": "Sign by quadrant, before anything else",
                    "teach": (
                        "Drag the angle and watch which of $\\sin$ and $\\cos$ is negative. Every "
                        "reciprocal inherits its partner's sign exactly — $\\sec$ is negative "
                        "precisely where $\\cos$ is, in quadrants 2 and 3. This picture is what "
                        "you consult after taking a square root, and it is why "
                        "$\\sec^2\\theta = \\frac{25}{16}$ alone can never finish a question."
                    ),
                    "config": {"mode": "explore", "start": 120},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Name the identity",
                    "prompt": "$1 + \\cot^2\\theta$ is identical to:",
                    "options": [
                        "$\\csc^2\\theta$",
                        "$\\sec^2\\theta$",
                        "$\\tan^2\\theta$",
                        "$1$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Divide $\\sin^2\\theta + \\cos^2\\theta = 1$ by $\\sin^2\\theta$: "
                        "$1 + \\cot^2\\theta = \\csc^2\\theta$. The $\\cot$/$\\csc$ pair always "
                        "travel together; $\\tan$/$\\sec$ is the other pair."
                    ),
                    "check": [
                        "Eq(simplify(1 + cot(x)**2 - csc(x)**2), 0)",
                        "Eq(simplify(1 + tan(x)**2 - sec(x)**2), 0)",
                    ],
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Exact value",
                    "title": "A reciprocal at a special angle",
                    "prompt": "$\\sec\\dfrac{2\\pi}{3}$ equals:",
                    "options": ["$-2$", "$2$", "$-\\dfrac{1}{2}$", "$\\dfrac{2\\sqrt3}{3}$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$\\cos\\frac{2\\pi}{3} = -\\frac{1}{2}$, so $\\sec\\frac{2\\pi}{3} = "
                        "\\frac{1}{-1/2} = -2$. Choosing $-\\frac{1}{2}$ means the reciprocal was "
                        "never taken; $\\frac{2\\sqrt3}{3}$ is $\\csc\\frac{2\\pi}{3}$, the wrong "
                        "partner."
                    ),
                    "check": [
                        "Eq(cos(2*pi/3), -Rational(1,2))",
                        "Eq(sec(2*pi/3), -2)",
                        "Eq(csc(2*pi/3), 2*sqrt(3)/3)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "One ratio given, three demanded",
                    "problemId": "ibhl-309-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Obtuse, so choose the sign",
                    "problemId": "ibhl-309-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "The restriction",
                    "title": "Why inverses need a leash",
                    "body": (
                        "$\\sin x = \\frac{1}{2}$ has infinitely many solutions, so 'the' angle "
                        "does not exist until we choose one. The syllabus chooses: $\\arcsin$ "
                        "returns from $\\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right]$, "
                        "$\\arccos$ from $[0, \\pi]$, $\\arctan$ from $\\left(-\\frac{\\pi}{2}, "
                        "\\frac{\\pi}{2}\\right)$. Those intervals are exactly where each function "
                        "is one-to-one. Every 'evaluate $\\arcsin(\\sin\\ldots)$' question on the "
                        "paper is testing whether you know them."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Range discipline",
                    "title": "Fold it back in",
                    "prompt": "$\\arccos\\!\\left(\\cos\\dfrac{7\\pi}{6}\\right)$ equals:",
                    "options": [
                        "$\\dfrac{5\\pi}{6}$",
                        "$\\dfrac{7\\pi}{6}$",
                        "$-\\dfrac{7\\pi}{6}$",
                        "$\\dfrac{\\pi}{6}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$\\cos\\frac{7\\pi}{6} = -\\frac{\\sqrt3}{2}$. $\\arccos$ must answer "
                        "inside $[0, \\pi]$, and the angle there with that cosine is "
                        "$\\frac{5\\pi}{6}$. Returning $\\frac{7\\pi}{6}$ ignores the range — the "
                        "single most common HL slip on this code."
                    ),
                    "check": [
                        "Eq(cos(7*pi/6), -sqrt(3)/2)",
                        "Eq(acos(cos(7*pi/6)), 5*pi/6)",
                        "Eq(cos(5*pi/6), -sqrt(3)/2)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Three inverses, exactly",
                    "problemId": "ibhl-309-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "A disguised quadratic",
                    "problemId": "ibhl-309-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.9 in four lines",
                    "points": [
                        "$\\sec = 1/\\cos$, $\\csc = 1/\\sin$, $\\cot = \\cos/\\sin$ — third letter names the partner.",
                        "$1 + \\tan^2 = \\sec^2$ and $1 + \\cot^2 = \\csc^2$: both are $\\sin^2 + \\cos^2 = 1$, divided.",
                        "Mixed equation $\\Rightarrow$ substitute so ONE ratio survives, then factorise the quadratic.",
                        "Inverse ranges: $\\arcsin\\,[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$, $\\arccos\\,[0, \\pi]$, $\\arctan\\,(-\\frac{\\pi}{2}, \\frac{\\pi}{2})$.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — AHL 3.10: Compound angle identities & tan of a double angle
# ===========================================================================
def lesson_compound_angles():
    return {
        "slug": "compound-and-double-angle",
        "title": "Compound & Double Angle Identities",
        "concreteComparison": (
            "Nobody stores every phone number — you store the area codes and dial the rest. "
            "$\\cos 15^\\circ$ is not on any exact-value list, but $45^\\circ$ and $30^\\circ$ are, "
            "and $15 = 45 - 30$. The compound angle formulas are the dialling rule that reaches "
            "every angle built from the ones you already know."
        ),
        "objective": (
            "Apply the compound angle identities for $\\sin$, $\\cos$ and $\\tan$ to find exact "
            "values, derive the double angle formula for $\\tan$, and prove identities by "
            "combining or splitting angles."
        ),
        "concept": [
            "**Syllabus card — AHL 3.10.** Compound angle identities; double angle identity for "
            "$\\tan$. Papers 1 and 2. Weight: 5-9 marks. Partner code: the SL double angle "
            "identities for $\\sin$ and $\\cos$ (SL 3.6), which are the $A = B$ case of these.",
            "**The three families.** "
            "$$\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A \\sin B$$ "
            "$$\\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A \\sin B$$ "
            "$$\\tan(A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1 \\mp \\tan A\\tan B}$$ "
            "All three are in the booklet. Sine keeps the sign you were given; cosine FLIPS it, "
            "and so does the denominator of tangent. That flip is the single most examined detail "
            "on this code.",
            "**Exact values beyond the standard list.** Any angle expressible as a sum or "
            "difference of $30^\\circ$, $45^\\circ$, $60^\\circ$ and $90^\\circ$ is now exact. "
            "$$\\cos 15^\\circ = \\cos(45^\\circ - 30^\\circ) = \\cos 45\\cos 30 + \\sin 45 \\sin 30 "
            "= \\frac{\\sqrt2}{2}\\cdot\\frac{\\sqrt3}{2} + \\frac{\\sqrt2}{2}\\cdot\\frac{1}{2} = "
            "\\frac{\\sqrt6 + \\sqrt2}{4}.$$ "
            "Note the answer is positive and a shade under $1$, as a $15^\\circ$ cosine must be — "
            "a five-second sanity check that catches a mis-copied sign.",
            "**Double angle for tangent.** Set $B = A$ in the tangent formula: "
            "$$\\tan 2A = \\frac{2\\tan A}{1 - \\tan^2 A}.$$ "
            "It is in the booklet, but derive it once so the derivation is available if the paper "
            "asks for it (it does, roughly every third session). The formula is undefined when "
            "$\\tan^2 A = 1$, which is exactly where $2A$ is an odd multiple of $\\frac{\\pi}{2}$ — "
            "the algebra knows about the asymptote.",
            "**Reading the identities backwards.** $\\sin A\\cos B + \\cos A \\sin B$ appearing in a "
            "question is a compound angle waiting to be collapsed. Adding two of the identities "
            "gives the sum-to-product moves: $\\sin(A+B) + \\sin(A-B) = 2\\sin A\\cos B$, which "
            "converts $\\sin 5x + \\sin 3x$ into $2\\sin 4x\\cos x$ — the standard opening for "
            "'solve $\\sin 5x + \\sin 3x = 0$'.",
        ],
        "keyIdea": (
            "$\\sin$ keeps the given sign; $\\cos$ flips it; $\\tan$'s denominator flips it too. "
            "Forwards they build exact values for non-standard angles; backwards they collapse a "
            "four-term expression into a single trig function."
        ),
        "facts": [
            {
                "title": "Compound angles",
                "latex": "\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A\\sin B; \\quad \\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A\\sin B",
                "explanation": (
                    "IN the booklet. The $\\mp$ in cosine is the whole game — $\\cos(A+B)$ uses a "
                    "MINUS between the products."
                ),
            },
            {
                "title": "Compound angle for tangent",
                "latex": "\\tan(A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1 \\mp \\tan A\\tan B}",
                "explanation": (
                    "IN the booklet. Numerator keeps the sign, denominator flips it. Undefined "
                    "when the denominator vanishes — which is a real asymptote, not an error."
                ),
            },
            {
                "title": "Double angle for tangent",
                "latex": "\\tan 2A = \\frac{2\\tan A}{1 - \\tan^2 A}",
                "explanation": (
                    "IN the booklet, and one substitution ($B = A$) away from the line above. Know "
                    "the derivation — 'show that' questions ask for it."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-310-we1",
                "statement": (
                    "Find the exact value of  \n"
                    "**(a)** $\\cos 15^\\circ$; **[3]**  \n"
                    "**(b)** $\\tan 75^\\circ$, giving your answer in the form $a + b\\sqrt3$ "
                    "where $a, b \\in \\mathbb{Z}$. **[4]**"
                ),
                "solution": (
                    "**(a)** Split into known angles *(M1)*: $15^\\circ = 45^\\circ - 30^\\circ$, "
                    "and $\\cos(A - B) = \\cos A\\cos B + \\sin A\\sin B$ — a PLUS, because the "
                    "given sign flips.  \n"
                    "$$\\cos 15^\\circ = \\frac{\\sqrt2}{2}\\cdot\\frac{\\sqrt3}{2} + "
                    "\\frac{\\sqrt2}{2}\\cdot\\frac{1}{2} \\;(A1) \\;=\\; "
                    "\\frac{\\sqrt6 + \\sqrt2}{4}. \\;(A1)$$  \n"
                    "**(b)** $75^\\circ = 45^\\circ + 30^\\circ$, with $\\tan 45^\\circ = 1$ and "
                    "$\\tan 30^\\circ = \\frac{1}{\\sqrt3}$ *(M1)*:  \n"
                    "$$\\tan 75^\\circ = \\frac{1 + \\frac{1}{\\sqrt3}}{1 - \\frac{1}{\\sqrt3}} = "
                    "\\frac{\\sqrt3 + 1}{\\sqrt3 - 1}. \\;(A1)$$  \n"
                    "Rationalise by multiplying above and below by $\\sqrt3 + 1$ *(M1)*:  \n"
                    "$$\\frac{(\\sqrt3+1)^2}{3 - 1} = \\frac{4 + 2\\sqrt3}{2} = 2 + \\sqrt3. "
                    "\\;(A1)$$  \n"
                    "**Narrative:** $2 + \\sqrt3 \\approx 3.73$, and $\\tan 75^\\circ$ should "
                    "indeed be large and positive — check the size, not just the algebra."
                ),
                "check": [
                    "Eq(simplify(cos(pi/4)*cos(pi/6) + sin(pi/4)*sin(pi/6)), (sqrt(6) + sqrt(2))/4)",
                    "Eq(simplify(cos(pi/12) - (sqrt(6) + sqrt(2))/4), 0)",
                    "Eq(simplify((1 + 1/sqrt(3))/(1 - 1/sqrt(3))), 2 + sqrt(3))",
                    "Eq(simplify(tan(5*pi/12) - (2 + sqrt(3))), 0)",
                    "Eq(expand((sqrt(3) + 1)**2), 4 + 2*sqrt(3))",
                ],
            },
            {
                "id": "ibhl-310-we2",
                "statement": (
                    "$A$ is acute with $\\sin A = \\dfrac{3}{5}$, and $B$ is obtuse with "
                    "$\\cos B = -\\dfrac{5}{13}$.  \n"
                    "**(a)** Find $\\sin(A + B)$. **[3]**  \n"
                    "**(b)** Find $\\tan(A + B)$. **[4]**"
                ),
                "solution": (
                    "First complete both triangles, using the stated quadrants for the signs "
                    "*(M1)*: $A$ acute gives $\\cos A = \\frac{4}{5}$; $B$ obtuse gives "
                    "$\\sin B = +\\frac{12}{13}$ *(A1)*.  \n"
                    "**(a)** $$\\sin(A+B) = \\frac{3}{5}\\cdot\\left(-\\frac{5}{13}\\right) + "
                    "\\frac{4}{5}\\cdot\\frac{12}{13} = -\\frac{15}{65} + \\frac{48}{65} = "
                    "\\frac{33}{65}. \\;(A1)$$  \n"
                    "**(b)** Rather than build $\\tan A$ and $\\tan B$ and wrestle the quotient "
                    "formula, get $\\cos(A+B)$ and divide *(M1)*:  \n"
                    "$$\\cos(A+B) = \\frac{4}{5}\\cdot\\left(-\\frac{5}{13}\\right) - "
                    "\\frac{3}{5}\\cdot\\frac{12}{13} = -\\frac{20}{65} - \\frac{36}{65} = "
                    "-\\frac{56}{65}. \\;(A1)$$  \n"
                    "$$\\tan(A+B) = \\frac{33/65}{-56/65} = -\\frac{33}{56}. \\;(A1\\,A1)$$  \n"
                    "**Narrative:** sine positive, cosine negative means $A + B$ is obtuse — "
                    "consistent, since $A$ is acute and $B$ is already past $90^\\circ$. The "
                    "$65$s cancelling is the signal you did it the efficient way."
                ),
                "check": [
                    "Eq(Rational(3,5)**2 + Rational(4,5)**2, 1)",
                    "Eq(Rational(-5,13)**2 + Rational(12,13)**2, 1)",
                    "Eq(Rational(3,5)*Rational(-5,13) + Rational(4,5)*Rational(12,13), Rational(33,65))",
                    "Eq(Rational(4,5)*Rational(-5,13) - Rational(3,5)*Rational(12,13), Rational(-56,65))",
                    "Eq(Rational(33,65)/Rational(-56,65), Rational(-33,56))",
                    "Eq(Rational(33,65)**2 + Rational(-56,65)**2, 1)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "$\\cos(A + B)$ written as $\\cos A\\cos B + \\sin A\\sin B$ — the sign not flipped.",
                "correction": "Cosine reverses: $\\cos(A+B) = \\cos A\\cos B - \\sin A\\sin B$. Sanity test with $A = B = 60^\\circ$: the true value is $\\cos 120^\\circ = -\\frac{1}{2}$, and only the minus version gives it.",
                "authored": True,
            },
            {
                "text": "$\\sin(A + B)$ expanded as $\\sin A + \\sin B$.",
                "correction": "Trig functions are not linear. $\\sin 90^\\circ = 1$ but $\\sin 45^\\circ + \\sin 45^\\circ = \\sqrt2 \\approx 1.41$ — the counterexample takes ten seconds.",
                "authored": True,
            },
            {
                "text": "Both triangles completed with positive values, ignoring 'obtuse'.",
                "correction": "Obtuse fixes $\\cos B < 0$ and $\\sin B > 0$. Signs come from the stated quadrant, never from the triangle sketch.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-310-t1",
                "statement": (
                    "**(a)** Show that $\\tan 2\\theta = \\dfrac{2\\tan\\theta}{1 - \\tan^2\\theta}$. "
                    "**[2]**  \n"
                    "**(b)** Given $\\tan\\theta = \\dfrac{3}{4}$, find the exact value of "
                    "$\\tan 2\\theta$. **[3]**"
                ),
                "solution": (
                    "**(a)** Put $B = \\theta$ into $\\tan(A + B) = \\frac{\\tan A + \\tan B}"
                    "{1 - \\tan A\\tan B}$ with $A = \\theta$ *(M1)*:  \n"
                    "$$\\tan 2\\theta = \\frac{\\tan\\theta + \\tan\\theta}{1 - \\tan\\theta"
                    "\\tan\\theta} = \\frac{2\\tan\\theta}{1 - \\tan^2\\theta}. \\;(AG)$$  \n"
                    "**(b)** Substitute $\\tan\\theta = \\frac{3}{4}$ *(M1)*:  \n"
                    "$$\\tan 2\\theta = \\frac{2 \\cdot \\frac{3}{4}}{1 - \\frac{9}{16}} = "
                    "\\frac{\\frac{3}{2}}{\\frac{7}{16}} \\;(A1) \\;=\\; \\frac{24}{7}. \\;(A1)$$  \n"
                    "The answer exceeds $\\tan\\theta$ sharply — expected, since doubling an angle "
                    "in the first quadrant pushes it towards the asymptote."
                ),
                "check": [
                    "Eq(simplify(expand_trig(tan(2*x) - 2*tan(x)/(1 - tan(x)**2))), 0)",
                    "Eq(2*Rational(3,4)/(1 - Rational(3,4)**2), Rational(24,7))",
                    "Abs(tan(2*atan(Rational(3,4))) - Rational(24,7)) < Rational(1,1000000)",
                ],
            },
            {
                "id": "ibhl-310-t2",
                "statement": (
                    "**(a)** Show that $\\sin(A + B) + \\sin(A - B) = 2\\sin A\\cos B$. **[3]**  \n"
                    "**(b)** Hence write $\\sin 5x + \\sin 3x$ as a product. **[3]**"
                ),
                "solution": (
                    "**(a)** Expand both *(M1)*:  \n"
                    "$$(\\sin A\\cos B + \\cos A\\sin B) + (\\sin A\\cos B - \\cos A\\sin B) "
                    "\\;(A1)$$  \n"
                    "The $\\cos A\\sin B$ terms cancel, leaving $2\\sin A\\cos B$ *(AG)*.  \n"
                    "**(b)** Match $A + B = 5x$ and $A - B = 3x$ *(M1)*, so $A = 4x$ and $B = x$ "
                    "*(A1)*:  \n"
                    "$$\\sin 5x + \\sin 3x = 2\\sin 4x\\cos x. \\;(A1)$$  \n"
                    "This is why 'solve $\\sin 5x + \\sin 3x = 0$' is tractable — a product equals "
                    "zero, so each factor gives its own family of solutions."
                ),
                "check": [
                    "Eq(simplify(expand_trig(sin(a + b) + sin(a - b) - 2*sin(a)*cos(b))), 0)",
                    "Eq(simplify(expand_trig(sin(5*x) + sin(3*x) - 2*sin(4*x)*cos(x))), 0)",
                    "Eq(4*x + x, 5*x)",
                    "Eq(4*x - x, 3*x)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.10 · Papers 1 & 2",
                    "title": "Angles that add",
                    "body": (
                        "$\\sin$ and $\\cos$ do not distribute over addition — but they do "
                        "decompose, in a fixed and memorable pattern. Sine mixes the two functions "
                        "($\\sin\\cos + \\cos\\sin$) and keeps your sign; cosine keeps like with "
                        "like ($\\cos\\cos - \\sin\\sin$) and flips it. Everything on this code "
                        "follows from those two lines and the quotient that builds $\\tan$."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The flip",
                    "title": "Which sign, exactly?",
                    "prompt": "$\\cos(A - B)$ expands to:",
                    "options": [
                        "$\\cos A\\cos B + \\sin A\\sin B$",
                        "$\\cos A\\cos B - \\sin A\\sin B$",
                        "$\\cos A\\sin B + \\sin A\\cos B$",
                        "$\\cos A - \\cos B$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Cosine reverses the sign it is given, so a MINUS inside becomes a PLUS "
                        "between the products. Test it with $A = B$: the formula returns "
                        "$\\cos^2 + \\sin^2 = 1 = \\cos 0$ ✓, while the minus version would give "
                        "$\\cos 2A$."
                    ),
                    "check": [
                        "Eq(simplify(expand_trig(cos(a - b) - (cos(a)*cos(b) + sin(a)*sin(b)))), 0)",
                        "Eq(simplify(cos(a - a) - (cos(a)**2 + sin(a)**2)), 0)",
                        "Eq(simplify(expand_trig(cos(a + b) - (cos(a)*cos(b) - sin(a)*sin(b)))), 0)",
                    ],
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Exact value",
                    "title": "Fifteen degrees, no calculator",
                    "prompt": "$\\sin 75^\\circ$ in exact form is:",
                    "options": [
                        "$\\dfrac{\\sqrt6 + \\sqrt2}{4}$",
                        "$\\dfrac{\\sqrt6 - \\sqrt2}{4}$",
                        "$\\dfrac{\\sqrt3 + 1}{2}$",
                        "$\\dfrac{\\sqrt2}{2}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$\\sin(45^\\circ + 30^\\circ) = \\frac{\\sqrt2}{2}\\cdot\\frac{\\sqrt3}{2} "
                        "+ \\frac{\\sqrt2}{2}\\cdot\\frac{1}{2} = \\frac{\\sqrt6 + \\sqrt2}{4} "
                        "\\approx 0.966$. The difference version is $\\sin 15^\\circ \\approx "
                        "0.259$ — one glance at the size separates them."
                    ),
                    "check": [
                        "Eq(simplify(sin(5*pi/12) - (sqrt(6) + sqrt(2))/4), 0)",
                        "Eq(simplify(sin(pi/12) - (sqrt(6) - sqrt(2))/4), 0)",
                        "((sqrt(6) + sqrt(2))/4) > Rational(9,10)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two exact values, two routes",
                    "problemId": "ibhl-310-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Derive, then use, tan 2θ",
                    "problemId": "ibhl-310-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "Backwards",
                    "title": "Collapsing, not expanding",
                    "body": (
                        "Half the marks on this code come from reading the identities RIGHT to "
                        "LEFT. Spot $\\sin A\\cos B + \\cos A\\sin B$ and write $\\sin(A+B)$. Add "
                        "the two sine identities and the $\\cos A\\sin B$ terms annihilate, giving "
                        "$\\sin(A+B) + \\sin(A-B) = 2\\sin A\\cos B$ — a sum turned into a product, "
                        "which is what makes equations like $\\sin 5x + \\sin 3x = 0$ solvable at "
                        "all."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read it backwards",
                    "title": "Collapse the expression",
                    "prompt": "$\\cos 3\\theta\\cos\\theta - \\sin 3\\theta\\sin\\theta$ simplifies to:",
                    "options": [
                        "$\\cos 4\\theta$",
                        "$\\cos 2\\theta$",
                        "$\\sin 4\\theta$",
                        "$\\cos 3\\theta^2$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Like-with-like products and a MINUS between them is exactly "
                        "$\\cos(A + B)$ with $A = 3\\theta$, $B = \\theta$: the answer is "
                        "$\\cos 4\\theta$. A minus sign here means addition of angles — the reverse "
                        "of the instinct most students bring."
                    ),
                    "check": [
                        "Eq(simplify(expand_trig(cos(3*x)*cos(x) - sin(3*x)*sin(x) - cos(4*x))), 0)",
                        "Eq(simplify(expand_trig(cos(3*x)*cos(x) + sin(3*x)*sin(x) - cos(2*x))), 0)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two quadrants, one sum",
                    "problemId": "ibhl-310-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Sum into product",
                    "problemId": "ibhl-310-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.10 in four lines",
                    "points": [
                        "$\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A\\sin B$ — mixed products, sign kept.",
                        "$\\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A\\sin B$ — like products, sign flipped.",
                        "$\\tan(A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1 \\mp \\tan A\\tan B}$; set $B = A$ for $\\tan 2A$.",
                        "Backwards: four terms collapse to one function; sums of sines become products.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — AHL 3.11: Symmetry relationships between trig functions
# ===========================================================================
def lesson_trig_symmetry():
    return {
        "slug": "trig-symmetry-and-relationships",
        "title": "Symmetry: One Solution into All of Them",
        "concreteComparison": (
            "A tiled floor is described completely by one tile plus the rule for repeating it. A "
            "calculator gives you one angle; the symmetry of the graph gives you every other "
            "angle with the same value. Students who stop at the calculator's answer lose the "
            "other three marks — and there are almost always other marks."
        ),
        "objective": (
            "Use the symmetry and periodicity of the trigonometric graphs to convert a single "
            "principal value into the complete solution set of an equation over a given interval, "
            "and to simplify expressions involving shifted or reflected angles."
        ),
        "concept": [
            "**Syllabus card — AHL 3.11.** The relationship between trigonometric functions and "
            "the symmetry properties of their graphs. Papers 1 and 2. Weight: 4-7 marks. This is "
            "the code that makes 'find ALL solutions in the interval' a reliable procedure rather "
            "than a guessing game.",
            "**The reflection rules.** Reflecting in the vertical axis: $\\sin(-x) = -\\sin x$ and "
            "$\\tan(-x) = -\\tan x$ (both ODD — the graphs have rotational symmetry about the "
            "origin), while $\\cos(-x) = \\cos x$ (EVEN — mirror symmetry in the $y$-axis). "
            "Reflecting in $x = \\frac{\\pi}{2}$: "
            "$$\\sin(\\pi - x) = \\sin x, \\qquad \\cos(\\pi - x) = -\\cos x, \\qquad "
            "\\tan(\\pi - x) = -\\tan x.$$",
            "**The shift rules.** Translating by $\\pi$ flips sine and cosine but leaves tangent "
            "alone (its period is only $\\pi$): $\\sin(x + \\pi) = -\\sin x$, $\\cos(x + \\pi) = "
            "-\\cos x$, $\\tan(x + \\pi) = \\tan x$. Translating by $\\frac{\\pi}{2}$ swaps the "
            "pair: $\\sin\\!\\left(x + \\frac{\\pi}{2}\\right) = \\cos x$ — the cosine graph IS "
            "the sine graph shifted left by a quarter period.",
            "**The procedure that earns the marks.** To solve $\\sin\\theta = k$ over an interval: "
            "(1) find the principal value $\\theta_1 = \\arcsin k$; (2) apply the symmetry partner "
            "$\\theta_2 = \\pi - \\theta_1$; (3) add multiples of $2\\pi$ to BOTH and keep every "
            "result inside the interval. For cosine the partner is $-\\theta_1$ (equivalently "
            "$2\\pi - \\theta_1$); for tangent the partner is $\\theta_1 + \\pi$, because tangent "
            "repeats twice as fast.",
            "**Watch the transformed interval.** If the equation is in $2x - \\frac{\\pi}{3}$ and "
            "$x$ runs over $[0, 2\\pi]$, then the ARGUMENT runs over $\\left[-\\frac{\\pi}{3}, "
            "4\\pi - \\frac{\\pi}{3}\\right]$ — more than two full turns, so expect roughly twice "
            "as many solutions. Solve for the argument across ITS interval first, then unwind to "
            "$x$. Skipping this is how candidates report two solutions when the paper wanted five.",
        ],
        "keyIdea": (
            "One principal value plus one symmetry partner plus the period generates the entire "
            "solution set. Sine's partner is $\\pi - \\theta$, cosine's is $-\\theta$, tangent's "
            "is $\\theta + \\pi$ — and a transformed argument runs over a transformed interval."
        ),
        "facts": [
            {
                "title": "Odd and even",
                "latex": "\\sin(-x) = -\\sin x, \\quad \\tan(-x) = -\\tan x, \\quad \\cos(-x) = \\cos x",
                "explanation": (
                    "NOT in the booklet. Sine and tangent are odd (origin symmetry); cosine is "
                    "even ($y$-axis symmetry). Read straight off the graphs."
                ),
            },
            {
                "title": "Supplementary angles",
                "latex": "\\sin(\\pi - x) = \\sin x, \\quad \\cos(\\pi - x) = -\\cos x",
                "explanation": (
                    "NOT in the booklet. The source of the second solution in every sine equation "
                    "— and of the ambiguous case in the sine rule."
                ),
            },
            {
                "title": "Quarter-turn shift",
                "latex": "\\sin\\!\\left(x + \\tfrac{\\pi}{2}\\right) = \\cos x, \\qquad \\cos\\!\\left(x - \\tfrac{\\pi}{2}\\right) = \\sin x",
                "explanation": (
                    "NOT in the booklet. Sine and cosine are the same wave a quarter period apart; "
                    "this is why either can model the same oscillation."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-311-we1",
                "statement": (
                    "Solve $2\\cos\\!\\left(2x - \\dfrac{\\pi}{3}\\right) = 1$ for "
                    "$0 \\le x \\le 2\\pi$. **[6]**"
                ),
                "solution": (
                    "Isolate the ratio and name the argument: let $u = 2x - \\frac{\\pi}{3}$, so "
                    "$\\cos u = \\frac{1}{2}$ *(M1)*.  \n"
                    "As $x$ runs over $[0, 2\\pi]$, $u$ runs over $\\left[-\\frac{\\pi}{3}, "
                    "4\\pi - \\frac{\\pi}{3}\\right]$ — over two full turns, so expect several "
                    "solutions *(A1)*.  \n"
                    "Principal value $u = \\frac{\\pi}{3}$; cosine's symmetry partner is $-u$, so "
                    "the general solution is $u = \\pm\\frac{\\pi}{3} + 2k\\pi$ *(M1)*. Unwind:  \n"
                    "$$2x = \\frac{\\pi}{3} \\pm \\frac{\\pi}{3} + 2k\\pi \\;\\Longrightarrow\\; "
                    "x = k\\pi \\quad\\text{or}\\quad x = \\frac{\\pi}{3} + k\\pi. \\;(A1)$$  \n"
                    "Keep everything in $[0, 2\\pi]$ *(A1)*:  \n"
                    "$$x = 0,\\;\\; \\frac{\\pi}{3},\\;\\; \\pi,\\;\\; \\frac{4\\pi}{3},\\;\\; "
                    "2\\pi. \\;(A1)$$  \n"
                    "**Narrative:** five solutions, and the endpoints $0$ and $2\\pi$ both count "
                    "because the interval is closed. Checking one — $x = \\frac{4\\pi}{3}$ gives "
                    "$2\\cos\\!\\left(\\frac{8\\pi}{3} - \\frac{\\pi}{3}\\right) = 2\\cos"
                    "\\frac{7\\pi}{3} = 2\\cos\\frac{\\pi}{3} = 1$ ✓ — is worth the ten seconds."
                ),
                "check": [
                    "Eq(2*cos(2*0 - pi/3), 1)",
                    "Eq(2*cos(2*(pi/3) - pi/3), 1)",
                    "Eq(2*cos(2*pi - pi/3), 1)",
                    "Eq(2*cos(2*(4*pi/3) - pi/3), 1)",
                    "Eq(2*cos(2*(2*pi) - pi/3), 1)",
                    "Ne(2*cos(2*(pi/2) - pi/3), 1)",
                    "Eq(cos(pi/3), Rational(1,2))",
                ],
            },
            {
                "id": "ibhl-311-we2",
                "statement": (
                    "**(a)** Show that $\\cos x = \\sin\\!\\left(x + \\dfrac{\\pi}{2}\\right)$, and "
                    "state the transformation this represents. **[3]**  \n"
                    "**(b)** Hence or otherwise solve $\\sin x = \\cos x$ for "
                    "$0 \\le x < 2\\pi$. **[4]**"
                ),
                "solution": (
                    "**(a)** Expand with the compound angle identity *(M1)*:  \n"
                    "$$\\sin\\!\\left(x + \\frac{\\pi}{2}\\right) = \\sin x\\cos\\frac{\\pi}{2} + "
                    "\\cos x\\sin\\frac{\\pi}{2} = \\sin x \\cdot 0 + \\cos x \\cdot 1 = \\cos x. "
                    "\\;(AG)$$  \n"
                    "The graph of $y = \\cos x$ is the graph of $y = \\sin x$ translated "
                    "$\\frac{\\pi}{2}$ units in the NEGATIVE $x$-direction *(A1 A1)*.  \n"
                    "**(b)** Divide by $\\cos x$ — legitimate, because $\\cos x = 0$ would force "
                    "$\\sin x = 0$ too, and they are never both zero *(R1)*:  \n"
                    "$$\\tan x = 1. \\;(M1)$$  \n"
                    "Principal value $x = \\frac{\\pi}{4}$; tangent's partner is $x + \\pi$ "
                    "*(A1)*:  \n"
                    "$$x = \\frac{\\pi}{4}, \\;\\; \\frac{5\\pi}{4}. \\;(A1)$$  \n"
                    "**Narrative:** these are exactly the two points where the sine and cosine "
                    "waves cross, one in the first quadrant and one in the third — where both are "
                    "negative and still equal."
                ),
                "check": [
                    "Eq(simplify(sin(x + pi/2) - cos(x)), 0)",
                    "Eq(sin(pi/2), 1)",
                    "Eq(cos(pi/2), 0)",
                    "Eq(sin(pi/4) - cos(pi/4), 0)",
                    "Eq(sin(5*pi/4) - cos(5*pi/4), 0)",
                    "Eq(tan(pi/4), 1)",
                    "Eq(tan(5*pi/4), 1)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reporting only the calculator's principal value as 'the' solution.",
                "correction": "A trig equation over an interval has a solution SET. Find the partner ($\\pi - \\theta$ for sine, $-\\theta$ for cosine, $\\theta + \\pi$ for tangent), then sweep the period.",
                "authored": True,
            },
            {
                "text": "Solving for the argument, then forgetting to unwind the interval for $x$.",
                "correction": "If the argument is $2x - \\frac{\\pi}{3}$ and $x \\in [0, 2\\pi]$, the argument covers $[-\\frac{\\pi}{3}, \\frac{11\\pi}{3}]$ — nearly two extra turns' worth of solutions.",
                "authored": True,
            },
            {
                "text": "Dividing $\\sin x = \\cos x$ by $\\cos x$ without checking whether $\\cos x$ can be zero.",
                "correction": "Here it cannot: $\\cos x = 0$ would force $\\sin x = 0$, contradicting $\\sin^2 + \\cos^2 = 1$. Say so — it is an R mark.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-311-t1",
                "statement": (
                    "Simplify $\\sin(\\pi - x)\\cos(-x) + \\cos\\!\\left(\\dfrac{\\pi}{2} - x\\right)"
                    "\\sin(\\pi + x)$, giving your answer as a product of two factors. **[5]**"
                ),
                "solution": (
                    "Translate each piece with the symmetry rules *(M1)*: $\\sin(\\pi - x) = "
                    "\\sin x$; $\\cos(-x) = \\cos x$; $\\cos\\!\\left(\\frac{\\pi}{2} - x\\right) "
                    "= \\sin x$; $\\sin(\\pi + x) = -\\sin x$ *(A1 A1)*.  \n"
                    "$$\\sin x\\cos x + \\sin x(-\\sin x) = \\sin x\\cos x - \\sin^2 x \\;(A1)$$  \n"
                    "$$= \\sin x\\,(\\cos x - \\sin x). \\;(A1)$$  \n"
                    "Spot-check at $x = \\frac{\\pi}{4}$: both terms are $\\frac{1}{2}$ and the "
                    "expression vanishes, matching $\\cos x - \\sin x = 0$ there ✓."
                ),
                "check": [
                    "Eq(simplify(sin(pi - x)*cos(-x) + cos(pi/2 - x)*sin(pi + x) - sin(x)*(cos(x) - sin(x))), 0)",
                    "Eq(simplify(sin(pi - x) - sin(x)), 0)",
                    "Eq(simplify(cos(pi/2 - x) - sin(x)), 0)",
                    "Eq(simplify(sin(pi + x) + sin(x)), 0)",
                    "Eq(simplify((sin(pi - x)*cos(-x) + cos(pi/2 - x)*sin(pi + x)).subs(x, pi/4)), 0)",
                ],
            },
            {
                "id": "ibhl-311-t2",
                "statement": (
                    "Solve $\\sin 3x = \\dfrac{\\sqrt3}{2}$ for $0 \\le x < \\pi$. **[5]**"
                ),
                "solution": (
                    "Let $u = 3x$; as $x$ runs over $[0, \\pi)$, $u$ runs over $[0, 3\\pi)$ — three "
                    "half-turns, so expect three solutions *(M1)*.  \n"
                    "Principal value $u = \\frac{\\pi}{3}$; sine's partner is $\\pi - u = "
                    "\\frac{2\\pi}{3}$ *(A1)*. Adding $2\\pi$ to the first gives "
                    "$\\frac{7\\pi}{3}$, still under $3\\pi$; adding $2\\pi$ to the second gives "
                    "$\\frac{8\\pi}{3}$, also under $3\\pi$ *(A1)*. So "
                    "$u = \\frac{\\pi}{3}, \\frac{2\\pi}{3}, \\frac{7\\pi}{3}, \\frac{8\\pi}{3}$.  \n"
                    "$$x = \\frac{\\pi}{9}, \\;\\; \\frac{2\\pi}{9}, \\;\\; \\frac{7\\pi}{9}, "
                    "\\;\\; \\frac{8\\pi}{9}. \\;(A1\\,A1)$$  \n"
                    "Four solutions, not three — the estimate was a guide, the interval sweep is "
                    "the proof."
                ),
                "check": [
                    "Eq(sin(3*(pi/9)), sqrt(3)/2)",
                    "Eq(sin(3*(2*pi/9)), sqrt(3)/2)",
                    "Eq(sin(3*(7*pi/9)), sqrt(3)/2)",
                    "Eq(sin(3*(8*pi/9)), sqrt(3)/2)",
                    "Ne(sin(3*(pi/2)), sqrt(3)/2)",
                    "(8*pi/9) < pi",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.11 · Papers 1 & 2",
                    "title": "The calculator gives you one; the graph gives you all",
                    "body": (
                        "$\\arcsin 0.5 = \\frac{\\pi}{6}$ — one answer, because a function may only "
                        "return one. But $\\sin\\theta = 0.5$ has infinitely many solutions, and "
                        "the graph shows you where: reflect in the peak to get "
                        "$\\pi - \\frac{\\pi}{6}$, then repeat every $2\\pi$. Symmetry is not "
                        "decoration; it is the algorithm."
                    ),
                },
                {
                    "kind": "unitCircle",
                    "eyebrow": "See the partner",
                    "title": "Two angles, one sine",
                    "teach": (
                        "Sweep the angle and watch the height. Every height above the axis is hit "
                        "TWICE per turn — once on the way up, once on the way down — and the two "
                        "angles are supplementary, $\\theta$ and $\\pi - \\theta$. The horizontal "
                        "coordinate tells the same story for cosine, with partner $-\\theta$."
                    ),
                    "config": {"mode": "explore", "start": 30},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Find the partner",
                    "prompt": "If $\\sin\\theta = 0.4$ and $\\theta_1 = \\arcsin 0.4$, the other solution in $[0, 2\\pi)$ is:",
                    "options": [
                        "$\\pi - \\theta_1$",
                        "$-\\theta_1$",
                        "$\\theta_1 + \\pi$",
                        "$2\\pi - \\theta_1$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Sine is symmetric about $x = \\frac{\\pi}{2}$, so its partner is the "
                        "supplement $\\pi - \\theta_1$. The option $2\\pi - \\theta_1$ is COSINE's "
                        "partner, and $\\theta_1 + \\pi$ is tangent's — each function has its own."
                    ),
                    "check": [
                        "Eq(simplify(sin(pi - x) - sin(x)), 0)",
                        "Eq(simplify(cos(2*pi - x) - cos(x)), 0)",
                        "Eq(simplify(tan(x + pi) - tan(x)), 0)",
                    ],
                },
                {
                    "kind": "unitCircle",
                    "eyebrow": "Circle to wave",
                    "title": "Where the symmetry comes from",
                    "teach": (
                        "Unroll the circle into the sine wave and the reflection rules become "
                        "visible facts about the graph: the mirror line at each peak gives "
                        "$\\sin(\\pi - x) = \\sin x$, the rotational symmetry at the origin gives "
                        "$\\sin(-x) = -\\sin x$, and the whole picture repeats every $2\\pi$."
                    ),
                    "config": {"mode": "wave"},
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Transformed argument, five solutions",
                    "problemId": "ibhl-311-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Sweep the stretched interval",
                    "problemId": "ibhl-311-t2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Odd or even",
                    "title": "Reflect in the y-axis",
                    "prompt": "Which statement is TRUE for all $x$?",
                    "options": [
                        "$\\cos(-x) = \\cos x$",
                        "$\\sin(-x) = \\sin x$",
                        "$\\tan(-x) = \\tan x$",
                        "$\\cos(-x) = -\\cos x$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Cosine is even — its graph is a mirror image in the $y$-axis. Sine and "
                        "tangent are odd, so both pick up a minus sign. Test at "
                        "$x = \\frac{\\pi}{3}$: $\\cos(-\\frac{\\pi}{3}) = \\frac{1}{2} = "
                        "\\cos\\frac{\\pi}{3}$ ✓, while $\\sin(-\\frac{\\pi}{3}) = "
                        "-\\frac{\\sqrt3}{2}$."
                    ),
                    "check": [
                        "Eq(cos(-pi/3), cos(pi/3))",
                        "Eq(sin(-pi/3), -sin(pi/3))",
                        "Eq(tan(-pi/3), -tan(pi/3))",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Cosine as a shifted sine",
                    "problemId": "ibhl-311-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Simplify with the symmetry rules",
                    "problemId": "ibhl-311-t1",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.11 in four lines",
                    "points": [
                        "Partners: sine $\\pi - \\theta$, cosine $-\\theta$, tangent $\\theta + \\pi$.",
                        "Odd: $\\sin$, $\\tan$. Even: $\\cos$. Shift by $\\frac{\\pi}{2}$ swaps sine and cosine.",
                        "Solve for the ARGUMENT over ITS transformed interval, then unwind to $x$.",
                        "Endpoints count when the interval is closed — read $\\le$ versus $<$ carefully.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — AHL 3.12: Vectors, components, magnitude & algebra
# ===========================================================================
def lesson_vectors_components():
    return {
        "slug": "vectors-components-and-algebra",
        "title": "Vectors: Components, Magnitude & Algebra",
        "concreteComparison": (
            "'The museum is 400 m away' is nearly useless; '400 m north-east' gets you there. A "
            "vector is the second kind of instruction — size AND direction, stored as a list of "
            "components. Once geometry is written as lists of numbers, three-dimensional "
            "questions stop needing a diagram you cannot draw."
        ),
        "objective": (
            "Represent points and displacements as vectors in two and three dimensions, compute "
            "magnitudes and unit vectors, add and scale vectors algebraically, and use the "
            "proportionality test for parallel vectors."
        ),
        "concept": [
            "**Syllabus card — AHL 3.12.** Concept of a vector; position vectors and displacement "
            "vectors; representation as directed line segments; base vectors $\\mathbf{i}$, "
            "$\\mathbf{j}$, $\\mathbf{k}$; components; algebraic and geometric approaches to the "
            "sum and difference of vectors, the zero vector, the vector $-\\mathbf{v}$, "
            "multiplication by a scalar, magnitude, and parallel vectors. Papers 1 and 2. Weight: "
            "5-8 marks, and it underpins every remaining code in this unit.",
            "**Position versus displacement.** The position vector $\\overrightarrow{OA} = "
            "\\mathbf{a}$ pins a point relative to the origin; the displacement "
            "$\\overrightarrow{AB}$ is the journey from $A$ to $B$. The relationship between them "
            "is the single most-used line in HL vectors: "
            "$$\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a} \\quad (\\text{destination minus "
            "start}).$$ "
            "Reversing this subtraction is the classic error, and it flips every subsequent sign.",
            "**Two notations, one object.** Column form and base-vector form say the same thing: "
            "$$\\begin{pmatrix} 4 \\\\ 3 \\\\ -12 \\end{pmatrix} = 4\\mathbf{i} + 3\\mathbf{j} - "
            "12\\mathbf{k}.$$ "
            "Columns are cleaner for arithmetic and are what markschemes usually print; "
            "$\\mathbf{i}$, $\\mathbf{j}$, $\\mathbf{k}$ appear more often in question stems. Be "
            "fluent both ways and translate immediately on reading the question.",
            "**Magnitude and unit vectors.** Pythagoras, extended to three dimensions: "
            "$$|\\mathbf{v}| = \\sqrt{v_1^2 + v_2^2 + v_3^2}.$$ "
            "Dividing a vector by its own magnitude produces the unit vector "
            "$\\hat{\\mathbf{v}} = \\frac{\\mathbf{v}}{|\\mathbf{v}|}$ — same direction, length "
            "one. Unit vectors are how you separate 'which way' from 'how far', and they are "
            "asked for directly on Paper 1.",
            "**Parallel means proportional.** $\\mathbf{u} \\parallel \\mathbf{v}$ exactly when "
            "$\\mathbf{u} = k\\mathbf{v}$ for some scalar $k \\ne 0$. Test it by dividing "
            "component by component: ALL ratios must agree. $(3, 6, -9)$ and $(2, 4, -6)$ give "
            "$\\frac{3}{2}$, $\\frac{3}{2}$, $\\frac{3}{2}$ — parallel. A single disagreeing "
            "ratio kills it, so check every component, not the first two.",
        ],
        "keyIdea": (
            "$\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a}$: destination minus start. "
            "Magnitude is 3D Pythagoras, a unit vector is $\\mathbf{v}/|\\mathbf{v}|$, and "
            "parallel means every component ratio is the same scalar $k$."
        ),
        "facts": [
            {
                "title": "Displacement from positions",
                "latex": "\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a}",
                "explanation": (
                    "NOT in the booklet — but used in nearly every vector question. Destination "
                    "minus start; reversing it reverses the direction."
                ),
            },
            {
                "title": "Magnitude in 3D",
                "latex": "|\\mathbf{v}| = \\sqrt{v_1^2 + v_2^2 + v_3^2}",
                "explanation": (
                    "IN the booklet. The distance between two points is just "
                    "$|\\overrightarrow{AB}|$ — one formula, not two."
                ),
            },
            {
                "title": "Unit vector",
                "latex": "\\hat{\\mathbf{v}} = \\frac{\\mathbf{v}}{|\\mathbf{v}|}, \\qquad |\\hat{\\mathbf{v}}| = 1",
                "explanation": (
                    "NOT in the booklet. Always verify by squaring and adding the components of "
                    "your answer — they must total exactly 1."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-312-we1",
                "statement": (
                    "Points $A$ and $B$ have position vectors $\\mathbf{a} = \\mathbf{i} - "
                    "2\\mathbf{j} + 4\\mathbf{k}$ and $\\mathbf{b} = 5\\mathbf{i} + \\mathbf{j} - "
                    "8\\mathbf{k}$.  \n"
                    "**(a)** Find $\\overrightarrow{AB}$ and $|\\overrightarrow{AB}|$. **[4]**  \n"
                    "**(b)** Find the unit vector in the direction of $\\overrightarrow{AB}$. "
                    "**[2]**"
                ),
                "solution": (
                    "**(a)** Destination minus start *(M1)*:  \n"
                    "$$\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a} = "
                    "\\begin{pmatrix} 5 - 1 \\\\ 1 - (-2) \\\\ -8 - 4 \\end{pmatrix} = "
                    "\\begin{pmatrix} 4 \\\\ 3 \\\\ -12 \\end{pmatrix}. \\;(A1)$$  \n"
                    "$$|\\overrightarrow{AB}| = \\sqrt{4^2 + 3^2 + (-12)^2} = \\sqrt{16 + 9 + 144} "
                    "= \\sqrt{169} = 13. \\;(M1\\,A1)$$  \n"
                    "**(b)** Divide by the magnitude *(M1)*:  \n"
                    "$$\\hat{\\mathbf{u}} = \\frac{1}{13}\\begin{pmatrix} 4 \\\\ 3 \\\\ -12 "
                    "\\end{pmatrix} = \\begin{pmatrix} \\frac{4}{13} \\\\ \\frac{3}{13} \\\\ "
                    "-\\frac{12}{13} \\end{pmatrix}. \\;(A1)$$  \n"
                    "**Narrative:** confirm the unit vector by squaring: $\\frac{16 + 9 + 144}"
                    "{169} = 1$ ✓. Note $|\\overrightarrow{AB}|$ is also the DISTANCE $AB$ — the "
                    "same computation answers both phrasings."
                ),
                "check": [
                    "Eq(Matrix([5,1,-8]) - Matrix([1,-2,4]), Matrix([4,3,-12]))",
                    "Eq(Matrix([4,3,-12]).norm(), 13)",
                    "Eq(Rational(4,13)**2 + Rational(3,13)**2 + Rational(-12,13)**2, 1)",
                    "Eq(sqrt(16 + 9 + 144), 13)",
                ],
            },
            {
                "id": "ibhl-312-we2",
                "statement": (
                    "Let $\\mathbf{a} = 2\\mathbf{i} - \\mathbf{j} + 3\\mathbf{k}$ and "
                    "$\\mathbf{b} = -\\mathbf{i} + 4\\mathbf{j} + \\mathbf{k}$.  \n"
                    "**(a)** Find $3\\mathbf{a} - 2\\mathbf{b}$ in component form. **[3]**  \n"
                    "**(b)** Find $|3\\mathbf{a} - 2\\mathbf{b}|$ in exact surd form. **[3]**"
                ),
                "solution": (
                    "**(a)** Scale each vector first, then subtract componentwise *(M1)*:  \n"
                    "$$3\\mathbf{a} = \\begin{pmatrix} 6 \\\\ -3 \\\\ 9 \\end{pmatrix}, \\qquad "
                    "2\\mathbf{b} = \\begin{pmatrix} -2 \\\\ 8 \\\\ 2 \\end{pmatrix} \\;(A1)$$  \n"
                    "$$3\\mathbf{a} - 2\\mathbf{b} = \\begin{pmatrix} 6 - (-2) \\\\ -3 - 8 \\\\ "
                    "9 - 2 \\end{pmatrix} = \\begin{pmatrix} 8 \\\\ -11 \\\\ 7 \\end{pmatrix}. "
                    "\\;(A1)$$  \n"
                    "**(b)** $$|3\\mathbf{a} - 2\\mathbf{b}| = \\sqrt{64 + 121 + 49} = \\sqrt{234} "
                    "\\;(M1\\,A1)$$  \n"
                    "$$= \\sqrt{9 \\times 26} = 3\\sqrt{26}. \\;(A1)$$  \n"
                    "**Narrative:** the $-3 - 8 = -11$ step is where marks vanish — subtracting a "
                    "POSITIVE 8 from a NEGATIVE 3. Paper 1 wants the surd simplified: pull out "
                    "the largest square factor, here $9$."
                ),
                "check": [
                    "Eq(3*Matrix([2,-1,3]) - 2*Matrix([-1,4,1]), Matrix([8,-11,7]))",
                    "Eq(Matrix([8,-11,7]).norm(), 3*sqrt(26))",
                    "Eq(64 + 121 + 49, 234)",
                    "Eq(sqrt(234), 3*sqrt(26))",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "$\\overrightarrow{AB}$ computed as $\\mathbf{a} - \\mathbf{b}$.",
                "correction": "Destination minus start: $\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a}$. The reversed version is $\\overrightarrow{BA}$ — same length, opposite direction, and every later sign wrong.",
                "authored": True,
            },
            {
                "text": "Declaring vectors parallel after checking only the first two components.",
                "correction": "ALL component ratios must equal the same $k$. $(3, 6, -9)$ vs $(2, 4, -5)$ agrees twice and fails on the third — not parallel.",
                "authored": True,
            },
            {
                "text": "Leaving $|\\mathbf{v}| = \\sqrt{234}$ unsimplified on Paper 1.",
                "correction": "Extract the square factor: $\\sqrt{234} = \\sqrt{9 \\cdot 26} = 3\\sqrt{26}$. Exact form means SIMPLIFIED exact form.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-312-t1",
                "statement": (
                    "The vectors $\\begin{pmatrix} t \\\\ 6 \\\\ -9 \\end{pmatrix}$ and "
                    "$\\begin{pmatrix} 2 \\\\ 4 \\\\ -6 \\end{pmatrix}$ are parallel. Find $t$. "
                    "**[3]**"
                ),
                "solution": (
                    "Parallel means one is a scalar multiple of the other *(M1)*. Use a component "
                    "pair that is fully known: $\\frac{6}{4} = \\frac{3}{2}$, and the third "
                    "components agree, $\\frac{-9}{-6} = \\frac{3}{2}$ ✓ *(A1)*. So $k = "
                    "\\frac{3}{2}$ and  \n"
                    "$$t = \\tfrac{3}{2} \\times 2 = 3. \\;(A1)$$  \n"
                    "Confirm: $(3, 6, -9) = \\frac{3}{2}(2, 4, -6)$ ✓. Finding $k$ from the KNOWN "
                    "components first, then applying it to the unknown, is the reliable order."
                ),
                "check": [
                    "Eq(Rational(6,4), Rational(3,2))",
                    "Eq(Rational(-9,-6), Rational(3,2))",
                    "Eq(Matrix([3,6,-9]), Rational(3,2)*Matrix([2,4,-6]))",
                ],
            },
            {
                "id": "ibhl-312-t2",
                "statement": (
                    "$P$ has coordinates $(2, -1, 3)$ and $Q$ has coordinates $(4, 3, -1)$.  \n"
                    "**(a)** Find the distance $PQ$. **[3]**  \n"
                    "**(b)** Find the position vector of the midpoint $M$ of $[PQ]$. **[2]**"
                ),
                "solution": (
                    "**(a)** $\\overrightarrow{PQ} = \\begin{pmatrix} 2 \\\\ 4 \\\\ -4 "
                    "\\end{pmatrix}$ *(M1 A1)*, so  \n"
                    "$$PQ = \\sqrt{4 + 16 + 16} = \\sqrt{36} = 6. \\;(A1)$$  \n"
                    "**(b)** The midpoint is the average of the position vectors *(M1)*:  \n"
                    "$$\\mathbf{m} = \\tfrac{1}{2}\\left(\\begin{pmatrix} 2 \\\\ -1 \\\\ 3 "
                    "\\end{pmatrix} + \\begin{pmatrix} 4 \\\\ 3 \\\\ -1 \\end{pmatrix}\\right) = "
                    "\\begin{pmatrix} 3 \\\\ 1 \\\\ 1 \\end{pmatrix}. \\;(A1)$$  \n"
                    "Check: $\\overrightarrow{PM} = (1, 2, -2)$ has magnitude $3$, exactly half of "
                    "$PQ$ ✓."
                ),
                "check": [
                    "Eq(Matrix([4,3,-1]) - Matrix([2,-1,3]), Matrix([2,4,-4]))",
                    "Eq(Matrix([2,4,-4]).norm(), 6)",
                    "Eq((Matrix([2,-1,3]) + Matrix([4,3,-1]))/2, Matrix([3,1,1]))",
                    "Eq(Matrix([1,2,-2]).norm(), 3)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.12 · Papers 1 & 2",
                    "title": "Geometry, rewritten as arithmetic",
                    "body": (
                        "A vector carries two facts at once — how far and which way — and stores "
                        "them as a short list of numbers. That is the whole trick: once a "
                        "three-dimensional configuration is a set of lists, distances, angles, "
                        "areas and intersections all become arithmetic. No perspective drawing "
                        "required, which matters enormously when the figure lives in space."
                    ),
                },
                {
                    "kind": "vectorGraph",
                    "eyebrow": "Components",
                    "title": "Drag the arrow, read the numbers",
                    "teach": (
                        "Move the arrow and watch its components and magnitude update together. "
                        "The components are the horizontal and vertical journeys; the magnitude is "
                        "the straight-line distance, which is Pythagoras on those journeys. In 3D "
                        "nothing changes except that there are three of them under the root."
                    ),
                    "config": {"mode": "components"},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Which subtraction?",
                    "prompt": "$A$ has position vector $\\mathbf{a}$ and $B$ has position vector $\\mathbf{b}$. Then $\\overrightarrow{AB}$ equals:",
                    "options": [
                        "$\\mathbf{b} - \\mathbf{a}$",
                        "$\\mathbf{a} - \\mathbf{b}$",
                        "$\\mathbf{a} + \\mathbf{b}$",
                        "$\\tfrac{1}{2}(\\mathbf{a} + \\mathbf{b})$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Destination minus start. With $\\mathbf{a} = (1, 0)$ and $\\mathbf{b} = "
                        "(4, 0)$, the journey from $A$ to $B$ is clearly $+3$ in $x$ — and only "
                        "$\\mathbf{b} - \\mathbf{a}$ delivers that. The last option is the "
                        "midpoint, a different question entirely."
                    ),
                    "check": [
                        "Eq(Matrix([4,0]) - Matrix([1,0]), Matrix([3,0]))",
                        "Eq(Matrix([1,0]) - Matrix([4,0]), Matrix([-3,0]))",
                        "Eq((Matrix([1,0]) + Matrix([4,0]))/2, Matrix([Rational(5,2),0]))",
                    ],
                },
                {
                    "kind": "vectorGraph",
                    "eyebrow": "Adding",
                    "title": "Nose to tail",
                    "teach": (
                        "Adding vectors geometrically means walking one journey then the other; "
                        "adding them algebraically means adding matching components. Drag both and "
                        "confirm the two descriptions never disagree — that equivalence is what "
                        "lets you abandon the diagram whenever it becomes inconvenient."
                    ),
                    "config": {"mode": "add"},
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Displacement, distance, direction",
                    "problemId": "ibhl-312-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Distance and midpoint",
                    "problemId": "ibhl-312-t2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Parallel test",
                    "title": "Same direction?",
                    "prompt": "Which vector is parallel to $\\begin{pmatrix} 2 \\\\ -3 \\\\ 4 \\end{pmatrix}$?",
                    "options": [
                        "$\\begin{pmatrix} -6 \\\\ 9 \\\\ -12 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 4 \\\\ -6 \\\\ 9 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 2 \\\\ 3 \\\\ 4 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 6 \\\\ -9 \\\\ 8 \\end{pmatrix}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$(-6, 9, -12) = -3(2, -3, 4)$ — every ratio is $-3$, so parallel (pointing "
                        "the opposite way, which still counts). The second and fourth options match "
                        "on two components and fail on the third: the classic trap."
                    ),
                    "check": [
                        "Eq(Matrix([-6,9,-12]), -3*Matrix([2,-3,4]))",
                        "Ne(Matrix([4,-6,9]), 2*Matrix([2,-3,4]))",
                        "Ne(Matrix([6,-9,8]), 3*Matrix([2,-3,4]))",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Scale, combine, simplify the surd",
                    "problemId": "ibhl-312-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Find the scalar first",
                    "problemId": "ibhl-312-t1",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.12 in four lines",
                    "points": [
                        "$\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a}$ — destination minus start.",
                        "$|\\mathbf{v}| = \\sqrt{v_1^2 + v_2^2 + v_3^2}$; the distance $AB$ is $|\\overrightarrow{AB}|$.",
                        "Unit vector $= \\mathbf{v}/|\\mathbf{v}|$; verify its components square to 1.",
                        "Parallel $\\iff \\mathbf{u} = k\\mathbf{v}$ — check EVERY component ratio.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — AHL 3.13: The scalar (dot) product
# ===========================================================================
def lesson_scalar_product():
    return {
        "slug": "scalar-product-and-angles",
        "title": "The Scalar Product & Angles Between Vectors",
        "concreteComparison": (
            "Pushing a sledge with a rope at an angle: only the part of your force pointing along "
            "the ground does any useful work. The scalar product is that measurement — how much "
            "of one vector points along another. When the answer is zero, nothing at all points "
            "along it, which is exactly what perpendicular means."
        ),
        "objective": (
            "Compute the scalar product from components and from magnitudes and the included "
            "angle, use it to find angles between vectors, and apply the zero test for "
            "perpendicularity — including finding unknown parameters that force it."
        ),
        "concept": [
            "**Syllabus card — AHL 3.13.** The definition of the scalar product of two vectors; "
            "the angle between two vectors; perpendicular vectors and parallel vectors. Papers 1 "
            "and 2. Weight: 5-8 marks. It is also the engine behind every angle in the plane and "
            "line codes that follow.",
            "**Two formulas, one number.** From components, "
            "$$\\mathbf{v}\\cdot\\mathbf{w} = v_1w_1 + v_2w_2 + v_3w_3,$$ "
            "and geometrically "
            "$$\\mathbf{v}\\cdot\\mathbf{w} = |\\mathbf{v}||\\mathbf{w}|\\cos\\theta.$$ "
            "Both are in the booklet. The first is how you CALCULATE it; the second is what it "
            "MEANS. Setting them equal and rearranging gives the angle — which is why this single "
            "code unlocks so much of the unit.",
            "**The angle formula.** "
            "$$\\cos\\theta = \\frac{\\mathbf{v}\\cdot\\mathbf{w}}{|\\mathbf{v}||\\mathbf{w}|}.$$ "
            "The result is a SCALAR (hence the name) and the angle returned is the one between "
            "$0$ and $\\pi$, since $\\arccos$ answers there. A negative scalar product therefore "
            "means an obtuse angle — a useful instant read, before any arithmetic.",
            "**The perpendicularity test.** $\\cos 90^\\circ = 0$, so "
            "$$\\mathbf{v} \\perp \\mathbf{w} \\iff \\mathbf{v}\\cdot\\mathbf{w} = 0$$ "
            "(for non-zero vectors). This converts a geometric condition into ONE linear equation, "
            "which is why 'find the value of $\\lambda$ for which these are perpendicular' is such "
            "a common 3-mark opener. Contrast the parallel test, which needs proportionality of "
            "every component.",
            "**Algebraic properties worth knowing.** The scalar product is commutative and "
            "distributes over addition, and $\\mathbf{v}\\cdot\\mathbf{v} = |\\mathbf{v}|^2$. "
            "Together these expand $|\\mathbf{a} + \\mathbf{b}|^2 = |\\mathbf{a}|^2 + "
            "2\\mathbf{a}\\cdot\\mathbf{b} + |\\mathbf{b}|^2$ — the vector version of the cosine "
            "rule, and the fastest route through any 'given $|\\mathbf{a}|$, $|\\mathbf{b}|$ and "
            "the angle, find $|\\mathbf{a} + \\mathbf{b}|$' question.",
        ],
        "keyIdea": (
            "$\\mathbf{v}\\cdot\\mathbf{w} = v_1w_1 + v_2w_2 + v_3w_3 = "
            "|\\mathbf{v}||\\mathbf{w}|\\cos\\theta$. Equate the two to extract the angle; a zero "
            "product means perpendicular, and a negative one means obtuse."
        ),
        "facts": [
            {
                "title": "Scalar product, both ways",
                "latex": "\\mathbf{v}\\cdot\\mathbf{w} = v_1w_1 + v_2w_2 + v_3w_3 = |\\mathbf{v}||\\mathbf{w}|\\cos\\theta",
                "explanation": (
                    "IN the booklet. Left side computes, right side interprets. The output is a "
                    "number, never a vector."
                ),
            },
            {
                "title": "Angle between vectors",
                "latex": "\\cos\\theta = \\frac{\\mathbf{v}\\cdot\\mathbf{w}}{|\\mathbf{v}||\\mathbf{w}|}",
                "explanation": (
                    "IN the booklet. Returns $\\theta \\in [0, \\pi]$. Negative numerator "
                    "$\\Rightarrow$ obtuse angle, with no further work."
                ),
            },
            {
                "title": "Perpendicular test",
                "latex": "\\mathbf{v} \\perp \\mathbf{w} \\iff \\mathbf{v}\\cdot\\mathbf{w} = 0",
                "explanation": (
                    "NOT stated separately in the booklet — it is the $\\cos 90^\\circ = 0$ case. "
                    "One equation, and it is linear in any unknown parameter."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-313-we1",
                "statement": (
                    "Let $\\mathbf{a} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 3 \\end{pmatrix}$ and "
                    "$\\mathbf{b} = \\begin{pmatrix} 1 \\\\ 4 \\\\ -2 \\end{pmatrix}$.  \n"
                    "**(a)** Find $\\mathbf{a}\\cdot\\mathbf{b}$. **[2]**  \n"
                    "**(b)** Find the angle between $\\mathbf{a}$ and $\\mathbf{b}$, correct to "
                    "the nearest degree. **[4]**"
                ),
                "solution": (
                    "**(a)** Multiply matching components and add *(M1)*:  \n"
                    "$$\\mathbf{a}\\cdot\\mathbf{b} = (2)(1) + (-1)(4) + (3)(-2) = 2 - 4 - 6 = "
                    "-8. \\;(A1)$$  \n"
                    "Negative already tells us the angle is obtuse.  \n"
                    "**(b)** Magnitudes *(A1)*: $|\\mathbf{a}| = \\sqrt{4 + 1 + 9} = \\sqrt{14}$ "
                    "and $|\\mathbf{b}| = \\sqrt{1 + 16 + 4} = \\sqrt{21}$, so "
                    "$|\\mathbf{a}||\\mathbf{b}| = \\sqrt{294} = 7\\sqrt6$.  \n"
                    "$$\\cos\\theta = \\frac{-8}{7\\sqrt6} \\approx -0.4666 \\;(M1\\,A1)$$  \n"
                    "$$\\theta = \\arccos(-0.4666\\ldots) = 117.8\\ldots^\\circ \\approx "
                    "118^\\circ. \\;(A1)$$  \n"
                    "**Narrative:** obtuse, as the negative product promised — a free check on "
                    "four marks' worth of arithmetic. Keep $7\\sqrt6$ exact until the final step; "
                    "rounding $\\sqrt{14}$ and $\\sqrt{21}$ early can shift the last digit."
                ),
                "check": [
                    "Eq(Matrix([2,-1,3]).dot(Matrix([1,4,-2])), -8)",
                    "Eq(Matrix([2,-1,3]).norm(), sqrt(14))",
                    "Eq(Matrix([1,4,-2]).norm(), sqrt(21))",
                    "Eq(simplify(sqrt(14)*sqrt(21)), 7*sqrt(6))",
                    "Abs(deg(acos(-8/(7*sqrt(6)))) - 117.8118) < Rational(1,100)",
                    "deg(acos(-8/(7*sqrt(6)))) > 90",
                ],
            },
            {
                "id": "ibhl-313-we2",
                "statement": (
                    "**(a)** Find the value of $\\lambda$ for which "
                    "$\\begin{pmatrix} 3 \\\\ \\lambda \\\\ -2 \\end{pmatrix}$ and "
                    "$\\begin{pmatrix} \\lambda \\\\ 5 \\\\ 4 \\end{pmatrix}$ are perpendicular. "
                    "**[3]**  \n"
                    "**(b)** Using this value of $\\lambda$, find the angle between the first "
                    "vector and $\\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix}$, to 3 "
                    "significant figures. **[4]**"
                ),
                "solution": (
                    "**(a)** Perpendicular means the scalar product vanishes *(M1)*:  \n"
                    "$$3\\lambda + 5\\lambda + (-2)(4) = 8\\lambda - 8 = 0 \\;(A1) "
                    "\\;\\Longrightarrow\\; \\lambda = 1. \\;(A1)$$  \n"
                    "**(b)** The first vector is now $\\begin{pmatrix} 3 \\\\ 1 \\\\ -2 "
                    "\\end{pmatrix}$. Scalar product with $(1, 1, 1)$ *(M1)*: $3 + 1 - 2 = 2$ "
                    "*(A1)*. Magnitudes are $\\sqrt{14}$ and $\\sqrt3$, so  \n"
                    "$$\\cos\\theta = \\frac{2}{\\sqrt{42}} \\approx 0.30861 \\;(A1)$$  \n"
                    "$$\\theta = 72.0^\\circ \\;(3\\text{ s.f.}). \\;(A1)$$  \n"
                    "**Narrative:** part (a) is linear in $\\lambda$ precisely because each term "
                    "contains $\\lambda$ at most once — that is typical, and it is why "
                    "perpendicularity questions are quick marks. Positive product in (b), so an "
                    "acute angle ✓."
                ),
                "check": [
                    "Eq(3*1 + 1*5 + (-2)*4, 0)",
                    "solve(Eq(8*L - 8, 0), L) == [1]",
                    "Eq(Matrix([3,1,-2]).dot(Matrix([1,5,4])), 0)",
                    "Eq(Matrix([3,1,-2]).dot(Matrix([1,1,1])), 2)",
                    "Eq(simplify(Matrix([3,1,-2]).norm()*Matrix([1,1,1]).norm()), sqrt(42))",
                    "Abs(deg(acos(2/sqrt(42))) - 72.0247) < Rational(1,100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Reporting the scalar product as a vector.",
                "correction": "The clue is in the name: SCALAR product. $(2)(1) + (-1)(4) + (3)(-2) = -8$, a single number. The product that returns a vector is the VECTOR product, a different code.",
                "authored": True,
            },
            {
                "text": "Dividing by $|\\mathbf{v}| + |\\mathbf{w}|$ instead of $|\\mathbf{v}||\\mathbf{w}|$ in the angle formula.",
                "correction": "The denominator is a PRODUCT of magnitudes. A quick check: for equal vectors it must give $\\cos\\theta = 1$, and only the product does.",
                "authored": True,
            },
            {
                "text": "Reading a negative $\\cos\\theta$ as an error and dropping the sign.",
                "correction": "Negative is meaningful — it says the angle is obtuse. $\\arccos$ handles negatives happily and returns an angle between $90^\\circ$ and $180^\\circ$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-313-t1",
                "statement": (
                    "Show that $\\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}$ and "
                    "$\\begin{pmatrix} 2 \\\\ -2 \\\\ 1 \\end{pmatrix}$ are perpendicular, and "
                    "state the magnitude of each. **[4]**"
                ),
                "solution": (
                    "Scalar product *(M1)*:  \n"
                    "$$(1)(2) + (2)(-2) + (2)(1) = 2 - 4 + 2 = 0,$$  \n"
                    "and since neither vector is zero, they are perpendicular *(A1 R1)*.  \n"
                    "Magnitudes: $\\sqrt{1 + 4 + 4} = 3$ and $\\sqrt{4 + 4 + 1} = 3$ *(A1)*.  \n"
                    "Both have length $3$, so dividing each by $3$ gives a perpendicular pair of "
                    "UNIT vectors — the beginnings of an orthonormal set, which is how coordinate "
                    "axes are built in the first place."
                ),
                "check": [
                    "Eq(Matrix([1,2,2]).dot(Matrix([2,-2,1])), 0)",
                    "Eq(Matrix([1,2,2]).norm(), 3)",
                    "Eq(Matrix([2,-2,1]).norm(), 3)",
                ],
            },
            {
                "id": "ibhl-313-t2",
                "statement": (
                    "Vectors $\\mathbf{a}$ and $\\mathbf{b}$ satisfy $|\\mathbf{a}| = 4$, "
                    "$|\\mathbf{b}| = 5$, and the angle between them is $60^\\circ$.  \n"
                    "**(a)** Find $\\mathbf{a}\\cdot\\mathbf{b}$. **[2]**  \n"
                    "**(b)** Find $|\\mathbf{a} + \\mathbf{b}|$ in exact form. **[4]**"
                ),
                "solution": (
                    "**(a)** Use the geometric form *(M1)*:  \n"
                    "$$\\mathbf{a}\\cdot\\mathbf{b} = 4 \\times 5 \\times \\cos 60^\\circ = "
                    "20 \\times \\tfrac{1}{2} = 10. \\;(A1)$$  \n"
                    "**(b)** Expand the square of the magnitude *(M1)*:  \n"
                    "$$|\\mathbf{a} + \\mathbf{b}|^2 = (\\mathbf{a} + \\mathbf{b})\\cdot"
                    "(\\mathbf{a} + \\mathbf{b}) = |\\mathbf{a}|^2 + 2\\,\\mathbf{a}\\cdot"
                    "\\mathbf{b} + |\\mathbf{b}|^2 \\;(A1)$$  \n"
                    "$$= 16 + 20 + 25 = 61 \\;(A1) \\;\\Longrightarrow\\; |\\mathbf{a} + "
                    "\\mathbf{b}| = \\sqrt{61}. \\;(A1)$$  \n"
                    "No components were ever needed — this is the cosine rule wearing vector "
                    "notation."
                ),
                "check": [
                    "Eq(4*5*cos(pi/3), 10)",
                    "Eq(16 + 2*10 + 25, 61)",
                    "Eq(sqrt(61)**2, 61)",
                    "Abs(sqrt(61) - 7.8102) < Rational(1,1000)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.13 · Papers 1 & 2",
                    "title": "How much of this points along that?",
                    "body": (
                        "The scalar product measures overlap of direction. Two vectors pointing the "
                        "same way give a large positive number; at right angles they give exactly "
                        "zero; pointing away from each other, a negative. Because the same quantity "
                        "also equals $|\\mathbf{v}||\\mathbf{w}|\\cos\\theta$, one computation "
                        "yields the angle between ANY two vectors — in two dimensions or three, "
                        "with no diagram."
                    ),
                },
                {
                    "kind": "vectorGraph",
                    "eyebrow": "Watch the sign",
                    "title": "Positive, zero, negative",
                    "teach": (
                        "Rotate one vector and watch the scalar product pass through zero exactly "
                        "as the arrows reach a right angle, then go negative as they open past it. "
                        "That sign change is the whole perpendicularity test — and it is why a "
                        "negative answer is information, not a mistake."
                    ),
                    "config": {"mode": "dot"},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Zero means what?",
                    "prompt": "For non-zero vectors $\\mathbf{v}$ and $\\mathbf{w}$, $\\mathbf{v}\\cdot\\mathbf{w} = 0$ means:",
                    "options": [
                        "they are perpendicular",
                        "they are parallel",
                        "one of them is the zero vector",
                        "they have equal magnitudes",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$|\\mathbf{v}||\\mathbf{w}|\\cos\\theta = 0$ with both magnitudes non-zero "
                        "forces $\\cos\\theta = 0$, i.e. $\\theta = 90^\\circ$. PARALLEL is the "
                        "opposite extreme, where the product reaches $\\pm|\\mathbf{v}||\\mathbf{w}|$."
                    ),
                    "check": [
                        "Eq(cos(pi/2), 0)",
                        "Eq(Matrix([1,0,0]).dot(Matrix([0,1,0])), 0)",
                        "Eq(Matrix([1,0,0]).dot(Matrix([3,0,0])), 3)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Product, then angle",
                    "problemId": "ibhl-313-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "A perpendicular pair",
                    "problemId": "ibhl-313-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "The algebra",
                    "title": "Expanding a magnitude",
                    "body": (
                        "Because $\\mathbf{v}\\cdot\\mathbf{v} = |\\mathbf{v}|^2$ and the product "
                        "distributes, squares of sums expand exactly as in ordinary algebra: "
                        "$$|\\mathbf{a} + \\mathbf{b}|^2 = |\\mathbf{a}|^2 + 2\\,\\mathbf{a}\\cdot"
                        "\\mathbf{b} + |\\mathbf{b}|^2.$$ "
                        "Read it with $\\mathbf{a}\\cdot\\mathbf{b} = |\\mathbf{a}||\\mathbf{b}|"
                        "\\cos\\theta$ and you are looking at the cosine rule. Questions giving you "
                        "magnitudes and an angle — but no components — want this line."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Instant read",
                    "title": "Acute or obtuse?",
                    "prompt": "Two vectors have scalar product $-15$. The angle between them is:",
                    "options": [
                        "obtuse",
                        "acute",
                        "exactly $90^\\circ$",
                        "impossible to classify without the magnitudes",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Magnitudes are always positive, so the SIGN of the scalar product is the "
                        "sign of $\\cos\\theta$. Negative $\\Rightarrow$ $\\cos\\theta < 0$ "
                        "$\\Rightarrow$ $90^\\circ < \\theta < 180^\\circ$. The magnitudes affect "
                        "the size of the angle, never which side of $90^\\circ$ it falls."
                    ),
                    "check": [
                        "cos(2*pi/3) < 0",
                        "cos(pi/3) > 0",
                        "Matrix([1,0,0]).dot(Matrix([-3,1,0])) < 0",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Force perpendicularity, then measure",
                    "problemId": "ibhl-313-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "No components given",
                    "problemId": "ibhl-313-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.13 in four lines",
                    "points": [
                        "$\\mathbf{v}\\cdot\\mathbf{w} = v_1w_1 + v_2w_2 + v_3w_3$ — a NUMBER, not a vector.",
                        "$\\cos\\theta = \\frac{\\mathbf{v}\\cdot\\mathbf{w}}{|\\mathbf{v}||\\mathbf{w}|}$, returning $\\theta \\in [0, \\pi]$.",
                        "Zero product $\\iff$ perpendicular; negative product $\\iff$ obtuse.",
                        "$|\\mathbf{a} + \\mathbf{b}|^2 = |\\mathbf{a}|^2 + 2\\mathbf{a}\\cdot\\mathbf{b} + |\\mathbf{b}|^2$ — the cosine rule in disguise.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — AHL 3.14: Vector equations of lines
# ===========================================================================
def lesson_vector_lines():
    return {
        "slug": "vector-equations-of-lines",
        "title": "Vector Equations of Lines",
        "concreteComparison": (
            "Giving directions to a hiking trail needs two things: a trailhead and a compass "
            "bearing. Everything else on the trail is 'walk $\\lambda$ kilometres that way'. A "
            "vector equation of a line is exactly that — one point on it, one direction along it, "
            "and a parameter that slides you to every other point."
        ),
        "objective": (
            "Write the vector, parametric and Cartesian equations of a line in two or three "
            "dimensions, move between the three forms, test whether a point lies on a line, and "
            "find the angle between two lines from their direction vectors."
        ),
        "concept": [
            "**Syllabus card — AHL 3.14.** Vector equation of a line in two and three dimensions: "
            "$\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}$; the angle between two lines; "
            "simple applications to kinematics. Papers 1 and 2. Weight: 5-9 marks.",
            "**One point, one direction.** "
            "$$\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}, \\qquad \\lambda \\in \\mathbb{R}$$ "
            "where $\\mathbf{a}$ is the position vector of ANY point on the line and $\\mathbf{b}$ "
            "is ANY vector along it. Because both choices are free, the same line has infinitely "
            "many correct equations — a fact worth stating in your answer, since markschemes "
            "accept any valid version and students often think theirs is wrong.",
            "**Building it from two points.** Given $A$ and $B$ on the line, take $\\mathbf{a}$ as "
            "the position vector of $A$ and $\\mathbf{b} = \\overrightarrow{AB} = \\mathbf{b}_{\\!"
            "\\text{pos}} - \\mathbf{a}$ as the direction. Then $\\lambda = 0$ lands on $A$ and "
            "$\\lambda = 1$ lands on $B$ — a built-in check that costs nothing.",
            "**Three equivalent forms.** From $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ -1 "
            "\\end{pmatrix} + \\lambda\\begin{pmatrix} 2 \\\\ -3 \\\\ 6 \\end{pmatrix}$ read off "
            "the PARAMETRIC form $x = 1 + 2\\lambda$, $y = 2 - 3\\lambda$, $z = -1 + 6\\lambda$, "
            "then eliminate $\\lambda$ to reach the CARTESIAN form "
            "$$\\frac{x - 1}{2} = \\frac{y - 2}{-3} = \\frac{z + 1}{6}.$$ "
            "The denominators are the direction components, and the numerators subtract the point "
            "— which is how you read a direction straight out of a Cartesian equation.",
            "**Is this point on the line?** Substitute and solve for $\\lambda$ using ONE "
            "component, then check that the SAME $\\lambda$ works for the others. Agreement on two "
            "components and failure on the third is the standard distractor: the point is then "
            "off the line, and saying so with the failing component named is the A mark.",
            "**Angle between two lines.** Lines have no single direction — $\\mathbf{b}$ and "
            "$-\\mathbf{b}$ describe the same line — so the angle between two lines is taken "
            "between their DIRECTION vectors, with the acute value reported: "
            "$$\\cos\\theta = \\frac{|\\mathbf{b}_1\\cdot\\mathbf{b}_2|}{|\\mathbf{b}_1|"
            "|\\mathbf{b}_2|}.$$ "
            "The absolute value is what forces the acute answer, and omitting it is a routine "
            "one-mark loss.",
        ],
        "keyIdea": (
            "$\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}$ — a point plus a direction. "
            "Parametric and Cartesian forms are the same information rewritten; a point lies on "
            "the line only if one $\\lambda$ satisfies ALL components; the angle between lines "
            "uses $|\\mathbf{b}_1\\cdot\\mathbf{b}_2|$ so the answer comes out acute."
        ),
        "facts": [
            {
                "title": "Vector equation of a line",
                "latex": "\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}",
                "explanation": (
                    "IN the booklet. $\\mathbf{a}$ = any point on it, $\\mathbf{b}$ = any direction "
                    "along it. Infinitely many correct forms per line."
                ),
            },
            {
                "title": "Cartesian (symmetric) form",
                "latex": "\\frac{x - a_1}{b_1} = \\frac{y - a_2}{b_2} = \\frac{z - a_3}{b_3}",
                "explanation": (
                    "NOT in the booklet. Denominators ARE the direction components — read them "
                    "straight off when a question hands you this form."
                ),
            },
            {
                "title": "Angle between two lines",
                "latex": "\\cos\\theta = \\frac{|\\mathbf{b}_1\\cdot\\mathbf{b}_2|}{|\\mathbf{b}_1||\\mathbf{b}_2|}",
                "explanation": (
                    "The modulus is essential: it reports the ACUTE angle, independent of which "
                    "way each direction vector happens to point."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-314-we1",
                "statement": (
                    "The line $L$ passes through $A(1, 2, -1)$ and $B(3, -1, 5)$.  \n"
                    "**(a)** Find a vector equation of $L$. **[3]**  \n"
                    "**(b)** Write $L$ in Cartesian form. **[2]**  \n"
                    "**(c)** Determine whether $C(7, -7, 17)$ and $D(5, -4, 10)$ lie on $L$. "
                    "**[4]**"
                ),
                "solution": (
                    "**(a)** Direction $\\overrightarrow{AB} = \\mathbf{b} - \\mathbf{a} = "
                    "\\begin{pmatrix} 2 \\\\ -3 \\\\ 6 \\end{pmatrix}$ *(M1 A1)*, so  \n"
                    "$$\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ -1 \\end{pmatrix} + \\lambda"
                    "\\begin{pmatrix} 2 \\\\ -3 \\\\ 6 \\end{pmatrix}. \\;(A1)$$  \n"
                    "**(b)** Eliminate $\\lambda$ from $x = 1 + 2\\lambda$, $y = 2 - 3\\lambda$, "
                    "$z = -1 + 6\\lambda$ *(M1)*:  \n"
                    "$$\\frac{x - 1}{2} = \\frac{y - 2}{-3} = \\frac{z + 1}{6}. \\;(A1)$$  \n"
                    "**(c)** For $C$: the $x$-component gives $1 + 2\\lambda = 7$, so $\\lambda = "
                    "3$ *(M1)*. Test the rest: $y = 2 - 9 = -7$ ✓ and $z = -1 + 18 = 17$ ✓, so "
                    "$C$ LIES on $L$ *(A1)*.  \n"
                    "For $D$: $1 + 2\\lambda = 5$ gives $\\lambda = 2$ *(M1)*, and then $y = 2 - 6 "
                    "= -4$ ✓ but $z = -1 + 12 = 11 \\ne 10$ ✗. $D$ does NOT lie on $L$ *(A1)*.  \n"
                    "**Narrative:** $D$ is the designed trap — it agrees on two components out of "
                    "three. Always test every component, and name the one that fails."
                ),
                "check": [
                    "Eq(Matrix([3,-1,5]) - Matrix([1,2,-1]), Matrix([2,-3,6]))",
                    "Eq(Matrix([1,2,-1]) + 3*Matrix([2,-3,6]), Matrix([7,-7,17]))",
                    "Eq(Matrix([1,2,-1]) + 2*Matrix([2,-3,6]), Matrix([5,-4,11]))",
                    "Ne(Matrix([1,2,-1]) + 2*Matrix([2,-3,6]), Matrix([5,-4,10]))",
                    "Eq(Matrix([1,2,-1]) + Matrix([2,-3,6]), Matrix([3,-1,5]))",
                    "Eq(Matrix([2,-3,6]).norm(), 7)",
                ],
            },
            {
                "id": "ibhl-314-we2",
                "statement": (
                    "$L_1$ has equation $\\mathbf{r} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 3 "
                    "\\end{pmatrix} + \\lambda\\begin{pmatrix} 1 \\\\ 2 \\\\ -1 \\end{pmatrix}$ "
                    "and $L_2$ has equation $\\mathbf{r} = \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 "
                    "\\end{pmatrix} + \\mu\\begin{pmatrix} 2 \\\\ -1 \\\\ 2 \\end{pmatrix}$.  \n"
                    "**(a)** Find the point where $L_1$ crosses the plane $z = 0$. **[3]**  \n"
                    "**(b)** Find the acute angle between $L_1$ and $L_2$, to 3 significant "
                    "figures. **[4]**"
                ),
                "solution": (
                    "**(a)** The $z$-component of a general point on $L_1$ is $3 - \\lambda$ "
                    "*(M1)*. Setting it to zero gives $\\lambda = 3$ *(A1)*, so the point is  \n"
                    "$$\\begin{pmatrix} 2 \\\\ -1 \\\\ 3 \\end{pmatrix} + 3\\begin{pmatrix} 1 \\\\ "
                    "2 \\\\ -1 \\end{pmatrix} = \\begin{pmatrix} 5 \\\\ 5 \\\\ 0 \\end{pmatrix}, "
                    "\\quad\\text{i.e. } (5, 5, 0). \\;(A1)$$  \n"
                    "**(b)** Use the direction vectors only *(M1)*:  \n"
                    "$$\\mathbf{b}_1\\cdot\\mathbf{b}_2 = (1)(2) + (2)(-1) + (-1)(2) = -2, \\qquad "
                    "|\\mathbf{b}_1| = \\sqrt6, \\quad |\\mathbf{b}_2| = 3. \\;(A1)$$  \n"
                    "$$\\cos\\theta = \\frac{|-2|}{3\\sqrt6} \\approx 0.27217 \\;(A1)$$  \n"
                    "$$\\theta = 74.2^\\circ \\;(3\\text{ s.f.}). \\;(A1)$$  \n"
                    "**Narrative:** without the modulus you would get $105.8^\\circ$ — the "
                    "supplement, and the wrong answer to 'acute'. The two angles always sum to "
                    "$180^\\circ$, so if your value exceeds $90^\\circ$, subtract."
                ),
                "check": [
                    "Eq(Matrix([2,-1,3]) + 3*Matrix([1,2,-1]), Matrix([5,5,0]))",
                    "Eq(3 - 3, 0)",
                    "Eq(Matrix([1,2,-1]).dot(Matrix([2,-1,2])), -2)",
                    "Eq(Matrix([1,2,-1]).norm(), sqrt(6))",
                    "Eq(Matrix([2,-1,2]).norm(), 3)",
                    "Abs(deg(acos(2/(3*sqrt(6)))) - 74.2068) < Rational(1,100)",
                    "Abs(deg(acos(2/(3*sqrt(6)))) + deg(acos(-2/(3*sqrt(6)))) - 180) < Rational(1,1000000)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Assuming your vector equation is wrong because it differs from the markscheme's.",
                "correction": "Any point on the line and any parallel direction are valid. $\\mathbf{r} = \\mathbf{b} + \\lambda(-\\mathbf{d})$ describes the same line as $\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{d}$ and earns full marks.",
                "authored": True,
            },
            {
                "text": "Declaring a point on the line after checking only one or two components.",
                "correction": "Solve for $\\lambda$ with one component, then VERIFY the others. Two out of three is the standard trap and scores nothing.",
                "authored": True,
            },
            {
                "text": "Omitting the modulus in the angle formula and reporting an obtuse angle.",
                "correction": "$\\cos\\theta = \\frac{|\\mathbf{b}_1\\cdot\\mathbf{b}_2|}{|\\mathbf{b}_1||\\mathbf{b}_2|}$. If you already have an obtuse value, the acute answer is $180^\\circ$ minus it.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-314-t1",
                "statement": (
                    "A line passes through $(4, 0, -2)$ and is parallel to $3\\mathbf{i} - "
                    "\\mathbf{j} + 2\\mathbf{k}$.  \n"
                    "**(a)** Write down a vector equation of the line. **[2]**  \n"
                    "**(b)** Find the coordinates of the point on the line with $x = 10$. **[3]**"
                ),
                "solution": (
                    "**(a)** Point plus direction, straight from the stem *(A1 A1)*:  \n"
                    "$$\\mathbf{r} = \\begin{pmatrix} 4 \\\\ 0 \\\\ -2 \\end{pmatrix} + \\lambda"
                    "\\begin{pmatrix} 3 \\\\ -1 \\\\ 2 \\end{pmatrix}.$$  \n"
                    "**(b)** Set the $x$-component to $10$ *(M1)*: $4 + 3\\lambda = 10$, so "
                    "$\\lambda = 2$ *(A1)*. Then $y = 0 - 2 = -2$ and $z = -2 + 4 = 2$:  \n"
                    "$$(10, -2, 2). \\;(A1)$$  \n"
                    "'Write down' in part (a) signals no working is expected — two marks for "
                    "reading the question correctly."
                ),
                "check": [
                    "Eq(Matrix([4,0,-2]) + 2*Matrix([3,-1,2]), Matrix([10,-2,2]))",
                    "solve(Eq(4 + 3*L, 10), L) == [2]",
                ],
            },
            {
                "id": "ibhl-314-t2",
                "statement": (
                    "The point $(5, p, 7)$ lies on the line $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ "
                    "2 \\\\ 3 \\end{pmatrix} + \\lambda\\begin{pmatrix} 2 \\\\ -1 \\\\ 2 "
                    "\\end{pmatrix}$. Find $p$. **[4]**"
                ),
                "solution": (
                    "Use a component with no unknown. From $x$: $1 + 2\\lambda = 5$, so $\\lambda "
                    "= 2$ *(M1 A1)*.  \n"
                    "Confirm with $z$, also free of $p$: $3 + 2(2) = 7$ ✓ *(R1)* — so the point "
                    "genuinely is on the line and the question is consistent.  \n"
                    "Now read off $y$:  \n"
                    "$$p = 2 - 1(2) = 0. \\;(A1)$$  \n"
                    "Choosing the $x$-component first is deliberate: never solve for $\\lambda$ "
                    "using the component that contains the unknown."
                ),
                "check": [
                    "solve(Eq(1 + 2*L, 5), L) == [2]",
                    "Eq(3 + 2*2, 7)",
                    "Eq(Matrix([1,2,3]) + 2*Matrix([2,-1,2]), Matrix([5,0,7]))",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.14 · Papers 1 & 2",
                    "title": "A trailhead and a bearing",
                    "body": (
                        "In two dimensions $y = mx + c$ does the job, but in three dimensions there "
                        "is no single gradient to quote. The vector equation solves this cleanly: "
                        "state where the line passes and which way it runs, then let $\\lambda$ "
                        "sweep along it. $\\lambda$ is often time in kinematics questions, which is "
                        "why the same equation answers 'where is the particle at $t = 3$?'"
                    ),
                },
                {
                    "kind": "coordinateGrid",
                    "eyebrow": "In two dimensions first",
                    "title": "Point plus direction, plotted",
                    "teach": (
                        "Plot a point, then step repeatedly by the direction vector. Every landing "
                        "spot is on the line, and the number of steps is $\\lambda$ — fractional "
                        "and negative values included. In 3D the picture is identical; only the "
                        "number of components changes."
                    ),
                    "config": {"mode": "plot"},
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Read the direction",
                    "prompt": "The line $\\dfrac{x - 3}{4} = \\dfrac{y + 1}{-2} = \\dfrac{z}{5}$ has direction vector:",
                    "options": [
                        "$\\begin{pmatrix} 4 \\\\ -2 \\\\ 5 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 3 \\\\ -1 \\\\ 0 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 3 \\\\ 1 \\\\ 0 \\end{pmatrix}$",
                        "$\\begin{pmatrix} -4 \\\\ 2 \\\\ -5 \\end{pmatrix}$ only",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The DENOMINATORS are the direction components; the numerators reveal the "
                        "point $(3, -1, 0)$. Note $(-4, 2, -5)$ is also a valid direction — it is "
                        "the same line reversed — but the option says 'only', which is false."
                    ),
                    "check": [
                        "Eq(Matrix([3,-1,0]) + 1*Matrix([4,-2,5]), Matrix([7,-3,5]))",
                        "Eq(Matrix([-4,2,-5]), -1*Matrix([4,-2,5]))",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two points to three forms",
                    "problemId": "ibhl-314-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Write it down, then land on a point",
                    "problemId": "ibhl-314-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "Angles",
                    "title": "Directions only, and take the modulus",
                    "body": (
                        "The angle between two lines ignores where they sit — only their directions "
                        "matter, so the position vectors play no part. And since a line's direction "
                        "vector can be written either way round, take the modulus of the scalar "
                        "product to force the acute answer: $\\cos\\theta = "
                        "\\frac{|\\mathbf{b}_1\\cdot\\mathbf{b}_2|}{|\\mathbf{b}_1||\\mathbf{b}_2|}$. "
                        "This holds even for lines that never meet."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Angle discipline",
                    "title": "Which vectors go into the formula?",
                    "prompt": "To find the angle between $\\mathbf{r} = \\mathbf{a}_1 + \\lambda\\mathbf{b}_1$ and $\\mathbf{r} = \\mathbf{a}_2 + \\mu\\mathbf{b}_2$, you use:",
                    "options": [
                        "$\\mathbf{b}_1$ and $\\mathbf{b}_2$",
                        "$\\mathbf{a}_1$ and $\\mathbf{a}_2$",
                        "$\\mathbf{a}_1$ and $\\mathbf{b}_2$",
                        "all four vectors",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Only the DIRECTIONS set the angle. The position vectors merely place the "
                        "lines in space — slide a line without turning it and the angle is "
                        "untouched, which is why skew lines still have a well-defined angle "
                        "between them."
                    ),
                    "check": [
                        "Eq(Matrix([1,0,0]).dot(Matrix([0,1,0])), 0)",
                        "Eq(acos(Matrix([1,0,0]).dot(Matrix([0,1,0]))/(Matrix([1,0,0]).norm()*Matrix([0,1,0]).norm())), pi/2)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Cross a plane, then measure an angle",
                    "problemId": "ibhl-314-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Solve with the safe component",
                    "problemId": "ibhl-314-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.14 in four lines",
                    "points": [
                        "$\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}$: any point on it, any direction along it.",
                        "Parametric $\\to$ Cartesian by eliminating $\\lambda$; denominators are the direction.",
                        "Point on line? One $\\lambda$ must satisfy ALL components — verify every one.",
                        "Angle between lines: directions only, with $|\\mathbf{b}_1\\cdot\\mathbf{b}_2|$ for the acute value.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 7 — AHL 3.15: Coincident, parallel, intersecting & skew lines
# ===========================================================================
def lesson_line_relationships():
    return {
        "slug": "line-relationships-and-intersections",
        "title": "Lines in Space: Parallel, Intersecting or Skew",
        "concreteComparison": (
            "Two roads on a flat map either run parallel or cross. Add a third dimension — a "
            "flyover — and a fourth possibility appears: they pass one above the other and never "
            "meet, without being parallel. That fourth case is 'skew', it exists only in 3D, and "
            "recognising it is worth marks on almost every HL vectors question."
        ),
        "objective": (
            "Classify a pair of lines in space as coincident, parallel and distinct, intersecting, "
            "or skew, and find the point of intersection when one exists."
        ),
        "concept": [
            "**Syllabus card — AHL 3.15.** Coincident, parallel, intersecting and skew lines; "
            "distinguishing between these cases; points of intersection. Papers 1 and 2. Weight: "
            "6-9 marks, very often as a Section B opener.",
            "**Four cases, decided in two questions.** First ask: are the DIRECTIONS parallel? "
            "If yes, the lines are either coincident (every point shared) or parallel and distinct "
            "(no point shared) — test one point of the first line against the second to decide. "
            "If the directions are NOT parallel, the lines either intersect at exactly one point "
            "or are skew — and only solving the system tells you which.",
            "**The system, and the crucial third equation.** Equating $\\mathbf{a}_1 + "
            "\\lambda\\mathbf{b}_1 = \\mathbf{a}_2 + \\mu\\mathbf{b}_2$ produces THREE equations "
            "in TWO unknowns — an over-determined system. Solve two of them for $\\lambda$ and "
            "$\\mu$, then SUBSTITUTE INTO THE THIRD. If it holds, the lines intersect; if it "
            "fails, they are skew. The third equation is not a formality, it is the entire test, "
            "and skipping it is the single most expensive error on this code.",
            "**Different parameters, always.** The two lines must use DIFFERENT letters "
            "($\\lambda$ and $\\mu$). Using $\\lambda$ for both silently demands that the point be "
            "reached after the same number of steps along each line — a far stronger condition "
            "than intersection, and it will manufacture false 'skew' verdicts.",
            "**Reporting the verdict.** Markschemes want the classification stated in words plus "
            "the evidence: 'directions are not parallel, and the equations are inconsistent "
            "($-\\frac{1}{3} \\ne \\frac{8}{3}$), so the lines are skew'. If they intersect, give "
            "the point of intersection — obtained by substituting your $\\lambda$ back into the "
            "FIRST line, then confirming with $\\mu$ in the second.",
        ],
        "keyIdea": (
            "Directions parallel? Then coincident or parallel-distinct — test a point. Not "
            "parallel? Solve two of the three equations, then CHECK THE THIRD: consistent means "
            "they intersect, inconsistent means skew."
        ),
        "facts": [
            {
                "title": "The four cases",
                "latex": "\\text{parallel directions} \\Rightarrow \\{\\text{coincident}, \\text{parallel distinct}\\}; \\quad \\text{otherwise} \\Rightarrow \\{\\text{intersecting}, \\text{skew}\\}",
                "explanation": (
                    "NOT in the booklet. Skew is the 3D-only case: not parallel, and yet never "
                    "meeting."
                ),
            },
            {
                "title": "The intersection system",
                "latex": "\\mathbf{a}_1 + \\lambda\\mathbf{b}_1 = \\mathbf{a}_2 + \\mu\\mathbf{b}_2 \\;\\Rightarrow\\; 3 \\text{ equations},\\; 2 \\text{ unknowns}",
                "explanation": (
                    "Solve any two, then test the third. Consistency IS the intersection test — "
                    "there is no separate criterion to memorise."
                ),
            },
            {
                "title": "Angle survives skewness",
                "latex": "\\cos\\theta = \\frac{|\\mathbf{b}_1\\cdot\\mathbf{b}_2|}{|\\mathbf{b}_1||\\mathbf{b}_2|}",
                "explanation": (
                    "Skew lines still have a well-defined angle — slide one until they meet; the "
                    "directions never changed."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-315-we1",
                "statement": (
                    "$L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix} + "
                    "\\lambda\\begin{pmatrix} 2 \\\\ -1 \\\\ 1 \\end{pmatrix}$ and "
                    "$L_2: \\mathbf{r} = \\begin{pmatrix} 2 \\\\ 0 \\\\ 5 \\end{pmatrix} + "
                    "\\mu\\begin{pmatrix} 1 \\\\ 1 \\\\ -1 \\end{pmatrix}$.  \n"
                    "**(a)** Show that $L_1$ and $L_2$ intersect, and find the point of "
                    "intersection. **[6]**  \n"
                    "**(b)** Find the angle between the lines. **[3]**"
                ),
                "solution": (
                    "**(a)** The directions are not proportional ($\\frac{2}{1} \\ne "
                    "\\frac{-1}{1}$), so the lines are not parallel *(R1)*. Equate the position "
                    "vectors *(M1)*:  \n"
                    "$$1 + 2\\lambda = 2 + \\mu, \\qquad 2 - \\lambda = \\mu, \\qquad "
                    "3 + \\lambda = 5 - \\mu.$$  \n"
                    "From the second, $\\mu = 2 - \\lambda$. Substituting into the first *(M1)*:  \n"
                    "$$1 + 2\\lambda = 2 + 2 - \\lambda \\;\\Longrightarrow\\; 3\\lambda = 3 "
                    "\\;\\Longrightarrow\\; \\lambda = 1, \\quad \\mu = 1. \\;(A1)$$  \n"
                    "**Test the third equation** *(M1)*: LHS $= 3 + 1 = 4$; RHS $= 5 - 1 = 4$ ✓ — "
                    "consistent, so the lines DO intersect *(A1)*.  \n"
                    "$$\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix} + "
                    "\\begin{pmatrix} 2 \\\\ -1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 1 "
                    "\\\\ 4 \\end{pmatrix}, \\quad\\text{i.e. } (3, 1, 4). \\;(A1)$$  \n"
                    "**(b)** $\\mathbf{b}_1\\cdot\\mathbf{b}_2 = 2 - 1 - 1 = 0$ *(M1 A1)*, so "
                    "$\\cos\\theta = 0$ and the lines meet at  \n"
                    "$$\\theta = 90^\\circ. \\;(A1)$$  \n"
                    "**Narrative:** verify the intersection point on the SECOND line too — "
                    "$(2, 0, 5) + (1, 1, -1) = (3, 1, 4)$ ✓. Two independent routes to the same "
                    "point is as certain as this gets."
                ),
                "check": [
                    "Eq(Matrix([1,2,3]) + 1*Matrix([2,-1,1]), Matrix([3,1,4]))",
                    "Eq(Matrix([2,0,5]) + 1*Matrix([1,1,-1]), Matrix([3,1,4]))",
                    "Eq(Matrix([2,-1,1]).dot(Matrix([1,1,-1])), 0)",
                    "Eq(3 + 1, 5 - 1)",
                    "Ne(Rational(2,1), Rational(-1,1))",
                ],
            },
            {
                "id": "ibhl-315-we2",
                "statement": (
                    "$L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix} + "
                    "\\lambda\\begin{pmatrix} 1 \\\\ 2 \\\\ -1 \\end{pmatrix}$ and "
                    "$L_2: \\mathbf{r} = \\begin{pmatrix} 0 \\\\ 3 \\\\ 1 \\end{pmatrix} + "
                    "\\mu\\begin{pmatrix} 2 \\\\ 1 \\\\ 1 \\end{pmatrix}$.  \n"
                    "Show that $L_1$ and $L_2$ are skew. **[6]**"
                ),
                "solution": (
                    "**Step 1 — not parallel.** $\\begin{pmatrix} 1 \\\\ 2 \\\\ -1 \\end{pmatrix} "
                    "= k\\begin{pmatrix} 2 \\\\ 1 \\\\ 1 \\end{pmatrix}$ would need $k = "
                    "\\frac{1}{2}$ from the first component and $k = 2$ from the second — "
                    "impossible, so the directions are not parallel *(R1)*.  \n"
                    "**Step 2 — try to intersect.** Equate *(M1)*:  \n"
                    "$$1 + \\lambda = 2\\mu, \\qquad 2\\lambda = 3 + \\mu, \\qquad "
                    "2 - \\lambda = 1 + \\mu.$$  \n"
                    "From the first, $\\lambda = 2\\mu - 1$. Substituting into the second "
                    "*(M1)*:  \n"
                    "$$2(2\\mu - 1) = 3 + \\mu \\;\\Longrightarrow\\; 3\\mu = 5 "
                    "\\;\\Longrightarrow\\; \\mu = \\tfrac{5}{3}, \\quad \\lambda = \\tfrac{7}{3}. "
                    "\\;(A1)$$  \n"
                    "**Step 3 — the third equation decides** *(M1)*:  \n"
                    "$$\\text{LHS} = 2 - \\tfrac{7}{3} = -\\tfrac{1}{3}, \\qquad \\text{RHS} = "
                    "1 + \\tfrac{5}{3} = \\tfrac{8}{3}, \\qquad -\\tfrac{1}{3} \\ne \\tfrac{8}{3}. "
                    "\\;(A1)$$  \n"
                    "The system is inconsistent, so no point lies on both lines. Not parallel and "
                    "not intersecting means the lines are **skew** *(R1)*.  \n"
                    "**Narrative:** notice how much of the work is Step 1 and Step 3 — the middle "
                    "algebra is routine. A solution that solves for $\\lambda$ and $\\mu$ and "
                    "stops has done the easy part and answered nothing."
                ),
                "check": [
                    "Ne(Rational(1,2), Rational(2,1))",
                    "Eq(2*(2*Rational(5,3) - 1), 3 + Rational(5,3))",
                    "Eq(1 + Rational(7,3), 2*Rational(5,3))",
                    "Ne(2 - Rational(7,3), 1 + Rational(5,3))",
                    "Eq(2 - Rational(7,3), Rational(-1,3))",
                    "Eq(1 + Rational(5,3), Rational(8,3))",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Solving two equations for $\\lambda$ and $\\mu$ and declaring the lines intersect.",
                "correction": "Two equations in two unknowns nearly always have a solution — that proves nothing. The THIRD equation is the test; without checking it you cannot distinguish intersecting from skew.",
                "authored": True,
            },
            {
                "text": "Using $\\lambda$ as the parameter on both lines.",
                "correction": "Use $\\lambda$ and $\\mu$. A shared parameter demands the meeting happen at the same 'time' on both lines — a stronger and wrong condition.",
                "authored": True,
            },
            {
                "text": "Calling non-intersecting lines 'parallel' without checking the directions.",
                "correction": "Parallel and skew both fail to meet. Check proportionality of the direction vectors FIRST — that is what separates the two verdicts.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-315-t1",
                "statement": (
                    "$L_1: \\mathbf{r} = \\begin{pmatrix} 3 \\\\ 1 \\\\ -2 \\end{pmatrix} + "
                    "\\lambda\\begin{pmatrix} 2 \\\\ -4 \\\\ 6 \\end{pmatrix}$ and "
                    "$L_2: \\mathbf{r} = \\begin{pmatrix} 0 \\\\ 7 \\\\ 1 \\end{pmatrix} + "
                    "\\mu\\begin{pmatrix} -1 \\\\ 2 \\\\ -3 \\end{pmatrix}$.  \n"
                    "Show that the lines are parallel, and determine whether they are coincident. "
                    "**[5]**"
                ),
                "solution": (
                    "$\\begin{pmatrix} 2 \\\\ -4 \\\\ 6 \\end{pmatrix} = -2\\begin{pmatrix} -1 "
                    "\\\\ 2 \\\\ -3 \\end{pmatrix}$ — every ratio is $-2$, so the directions are "
                    "parallel *(M1 A1)*.  \n"
                    "Now test whether $L_2$'s point $(0, 7, 1)$ lies on $L_1$ *(M1)*. From the "
                    "$x$-component: $3 + 2\\lambda = 0$, so $\\lambda = -\\frac{3}{2}$. Then  \n"
                    "$$y = 1 - 4\\left(-\\tfrac{3}{2}\\right) = 7 \\;✓, \\qquad "
                    "z = -2 + 6\\left(-\\tfrac{3}{2}\\right) = -11 \\ne 1. \\;(A1)$$  \n"
                    "The point is not on $L_1$, so the lines are parallel and **distinct**, not "
                    "coincident *(A1)*.  \n"
                    "Two out of three components agreeing is exactly the trap — the $z$-component "
                    "settles it."
                ),
                "check": [
                    "Eq(Matrix([2,-4,6]), -2*Matrix([-1,2,-3]))",
                    "Eq(Matrix([3,1,-2]) + Rational(-3,2)*Matrix([2,-4,6]), Matrix([0,7,-11]))",
                    "Ne(Matrix([3,1,-2]) + Rational(-3,2)*Matrix([2,-4,6]), Matrix([0,7,1]))",
                ],
            },
            {
                "id": "ibhl-315-t2",
                "statement": (
                    "Determine whether $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 "
                    "\\end{pmatrix} + \\lambda\\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix}$ "
                    "and $L_2: \\mathbf{r} = \\begin{pmatrix} 2 \\\\ 1 \\\\ 3 \\end{pmatrix} + "
                    "\\mu\\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix}$ intersect, and if so "
                    "find the point. **[6]**"
                ),
                "solution": (
                    "Directions $(1, 0, 2)$ and $(0, 1, 1)$ are not proportional — the first has a "
                    "zero where the second does not *(R1)*.  \n"
                    "Equate *(M1)*:  \n"
                    "$$1 + \\lambda = 2, \\qquad 1 = 1 + \\mu, \\qquad 1 + 2\\lambda = 3 + \\mu.$$  \n"
                    "The first gives $\\lambda = 1$ and the second gives $\\mu = 0$ immediately "
                    "*(A1 A1)* — the zeros in the direction vectors do the work for us.  \n"
                    "Third equation *(M1)*: LHS $= 1 + 2 = 3$, RHS $= 3 + 0 = 3$ ✓ *(A1)*. "
                    "Consistent, so the lines intersect at  \n"
                    "$$\\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix} + \\begin{pmatrix} 1 \\\\ 0 "
                    "\\\\ 2 \\end{pmatrix} = (2, 1, 3). \\;(A1)$$  \n"
                    "The intersection is $L_2$'s own starting point, which is why $\\mu = 0$."
                ),
                "check": [
                    "Eq(Matrix([1,1,1]) + 1*Matrix([1,0,2]), Matrix([2,1,3]))",
                    "Eq(Matrix([2,1,3]) + 0*Matrix([0,1,1]), Matrix([2,1,3]))",
                    "Eq(1 + 2*1, 3 + 0)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.15 · Papers 1 & 2",
                    "title": "The case that only exists in three dimensions",
                    "body": (
                        "In a plane, two lines that are not parallel MUST cross — there is nowhere "
                        "else to go. In space they can miss each other entirely while pointing in "
                        "quite different directions: one passes above the other. Skew lines are "
                        "why the third equation matters, and why 'not parallel' can never be "
                        "shortened to 'therefore they meet'."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "What makes lines skew?",
                    "prompt": "Two lines in space are skew when:",
                    "options": [
                        "their directions are not parallel and they do not intersect",
                        "their directions are parallel and they do not intersect",
                        "they intersect at exactly one point",
                        "they lie in the same plane",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Parallel-and-non-meeting is the PARALLEL case, not skew. Skew requires "
                        "both conditions: different directions AND no common point — which is only "
                        "possible in three or more dimensions, and means no single plane contains "
                        "them both."
                    ),
                    "check": [
                        "Ne(Rational(1,2), Rational(2,1))",
                        "Ne(2 - Rational(7,3), 1 + Rational(5,3))",
                    ],
                },
                {
                    "kind": "stepProof",
                    "eyebrow": "The decision procedure",
                    "title": "Four cases in three steps",
                    "teach": (
                        "Every classification question follows this fixed route. Learn it as a "
                        "flowchart and the marks become mechanical — the thinking is in executing "
                        "step 3, not in choosing what to do."
                    ),
                    "config": {
                        "given": "Two lines $\\mathbf{r} = \\mathbf{a}_1 + \\lambda\\mathbf{b}_1$ and $\\mathbf{r} = \\mathbf{a}_2 + \\mu\\mathbf{b}_2$",
                        "prove": "The lines are coincident, parallel-distinct, intersecting, or skew",
                        "rows": [
                            {
                                "statement": "Is $\\mathbf{b}_1 = k\\mathbf{b}_2$ for some scalar $k$?",
                                "reason": "Compare EVERY component ratio — the parallel test",
                            },
                            {
                                "statement": "If YES: does $\\mathbf{a}_1$ satisfy the second line's equation?",
                                "reason": "Yes $\\Rightarrow$ coincident; No $\\Rightarrow$ parallel and distinct",
                            },
                            {
                                "statement": "If NO: equate the two lines to get 3 equations in $\\lambda, \\mu$",
                                "reason": "A common point must satisfy all three simultaneously",
                            },
                            {
                                "statement": "Solve any two for $\\lambda$ and $\\mu$",
                                "reason": "Two equations, two unknowns — routine algebra",
                            },
                            {
                                "statement": "Substitute those values into the THIRD equation",
                                "reason": "Consistent $\\Rightarrow$ intersecting; inconsistent $\\Rightarrow$ skew",
                            },
                            {
                                "statement": "If consistent, substitute $\\lambda$ back to get the point",
                                "reason": "Then confirm with $\\mu$ on the other line",
                            },
                        ],
                    },
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "They meet — and at a right angle",
                    "problemId": "ibhl-315-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Zeros make it quick",
                    "problemId": "ibhl-315-t2",
                },
                {
                    "kind": "teach",
                    "eyebrow": "The parallel branch",
                    "title": "Coincident or merely parallel",
                    "body": (
                        "When the directions ARE proportional, there is no system to solve — the "
                        "lines either lie on top of each other or never touch. One test settles "
                        "it: take any point from one line and ask whether it satisfies the other. "
                        "On it, and the lines are the same line written two ways; off it, and "
                        "they are parallel and distinct, at constant separation forever."
                    ),
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Parallel — but the same line?",
                    "problemId": "ibhl-315-t1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The fatal shortcut",
                    "title": "You solved two equations. Now what?",
                    "prompt": "You equate two lines, solve the first two equations and get $\\lambda = 2$, $\\mu = -1$. You should next:",
                    "options": [
                        "substitute both into the third equation and check it holds",
                        "state the lines intersect and find the point",
                        "state the lines are skew",
                        "check whether the directions are perpendicular",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Two equations in two unknowns almost always solve — that is not evidence "
                        "of anything. The third equation is the actual intersection test: if it "
                        "fails, those $\\lambda$ and $\\mu$ values reach two DIFFERENT points and "
                        "the lines are skew."
                    ),
                    "check": [
                        "Eq(3 + 1, 5 - 1)",
                        "Ne(2 - Rational(7,3), 1 + Rational(5,3))",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Skew, proved properly",
                    "problemId": "ibhl-315-we2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.15 in four lines",
                    "points": [
                        "Directions proportional? $\\Rightarrow$ coincident or parallel-distinct; test one point.",
                        "Not proportional? $\\Rightarrow$ equate the lines: 3 equations, 2 unknowns.",
                        "Solve two, then CHECK THE THIRD — consistent means intersecting, inconsistent means skew.",
                        "Use different parameters $\\lambda$ and $\\mu$, and state the verdict in words.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 8 — AHL 3.16: The vector (cross) product
# ===========================================================================
def lesson_vector_product():
    return {
        "slug": "vector-product-and-areas",
        "title": "The Vector Product & Areas",
        "concreteComparison": (
            "Turn a bolt with a spanner and the bolt moves along the axis — perpendicular to both "
            "the spanner and your push. The vector product does the same thing algebraically: "
            "feed it two directions and it returns the direction perpendicular to both, with a "
            "length that measures how much area they sweep out between them."
        ),
        "objective": (
            "Compute the vector product from components, interpret its magnitude as the area of "
            "the parallelogram spanned by two vectors, and use it to find normals, triangle areas "
            "and perpendicular unit vectors."
        ),
        "concept": [
            "**Syllabus card — AHL 3.16.** The definition of the vector product of two vectors; "
            "the geometric interpretation of $|\\mathbf{v} \\times \\mathbf{w}|$. Papers 1 and 2. "
            "Weight: 5-8 marks — and it is the tool that makes the plane code (AHL 3.17) possible "
            "at all.",
            "**The determinant layout.** "
            "$$\\mathbf{v} \\times \\mathbf{w} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & "
            "\\mathbf{k} \\\\ v_1 & v_2 & v_3 \\\\ w_1 & w_2 & w_3 \\end{vmatrix} = "
            "\\begin{pmatrix} v_2w_3 - v_3w_2 \\\\ v_3w_1 - v_1w_3 \\\\ v_1w_2 - v_2w_1 "
            "\\end{pmatrix}$$ "
            "The component form is in the booklet. Note the MIDDLE component is the odd one out — "
            "expanding the determinant attaches a minus sign to the $\\mathbf{j}$ term, which is "
            "why writing $v_3w_1 - v_1w_3$ (indices reversed) gets it right automatically.",
            "**Always perpendicular — and that is the point.** $\\mathbf{v}\\times\\mathbf{w}$ is "
            "perpendicular to BOTH inputs. Verify it free of charge by dotting your answer with "
            "each original vector: two zeros, and your arithmetic is confirmed. This is the "
            "cheapest self-check in the entire unit, and it catches the sign slip almost before "
            "you have made it.",
            "**Magnitude measures area.** "
            "$$|\\mathbf{v}\\times\\mathbf{w}| = |\\mathbf{v}||\\mathbf{w}|\\sin\\theta$$ "
            "which is precisely the area of the parallelogram with sides $\\mathbf{v}$ and "
            "$\\mathbf{w}$ — hence half of it is the area of the triangle they span: "
            "$$\\text{Area of }\\triangle ABC = \\tfrac{1}{2}\\left|\\overrightarrow{AB} \\times "
            "\\overrightarrow{AC}\\right|.$$ "
            "This is how HL computes triangle areas in 3D, where 'base times height' has no "
            "convenient meaning.",
            "**Order matters.** $\\mathbf{w}\\times\\mathbf{v} = -(\\mathbf{v}\\times\\mathbf{w})$ "
            "— the vector product is ANTI-commutative, unlike the scalar product. For areas the "
            "sign is irrelevant (you take the magnitude), but for a normal direction it flips "
            "which way the arrow points. Also note $\\mathbf{v}\\times\\mathbf{v} = \\mathbf{0}$: "
            "parallel vectors span no area at all.",
        ],
        "keyIdea": (
            "$\\mathbf{v}\\times\\mathbf{w}$ is a VECTOR perpendicular to both, with magnitude "
            "$|\\mathbf{v}||\\mathbf{w}|\\sin\\theta$ = the parallelogram's area. Halve it for a "
            "triangle; dot it with the inputs to check your arithmetic."
        ),
        "facts": [
            {
                "title": "Vector product in components",
                "latex": "\\mathbf{v} \\times \\mathbf{w} = \\begin{pmatrix} v_2w_3 - v_3w_2 \\\\ v_3w_1 - v_1w_3 \\\\ v_1w_2 - v_2w_1 \\end{pmatrix}",
                "explanation": (
                    "IN the booklet. The middle row's indices run 3-1 then 1-3 — that ordering IS "
                    "the minus sign from the determinant expansion."
                ),
            },
            {
                "title": "Magnitude and area",
                "latex": "|\\mathbf{v} \\times \\mathbf{w}| = |\\mathbf{v}||\\mathbf{w}|\\sin\\theta = \\text{area of the parallelogram}",
                "explanation": (
                    "IN the booklet. Compare the scalar product's $\\cos\\theta$: the two products "
                    "measure complementary things — alignment versus spread."
                ),
            },
            {
                "title": "Triangle area in 3D",
                "latex": "\\text{Area}(\\triangle ABC) = \\tfrac{1}{2}\\left|\\overrightarrow{AB} \\times \\overrightarrow{AC}\\right|",
                "explanation": (
                    "NOT in the booklet as such, but the standard HL route — no height, no "
                    "trigonometry, works in any number of dimensions up to three."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-316-we1",
                "statement": (
                    "Let $\\mathbf{a} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 3 \\end{pmatrix}$ and "
                    "$\\mathbf{b} = \\begin{pmatrix} 1 \\\\ 4 \\\\ -2 \\end{pmatrix}$.  \n"
                    "**(a)** Find $\\mathbf{a} \\times \\mathbf{b}$. **[3]**  \n"
                    "**(b)** Verify that your answer is perpendicular to both $\\mathbf{a}$ and "
                    "$\\mathbf{b}$. **[2]**  \n"
                    "**(c)** Find the area of the triangle with sides $\\mathbf{a}$ and "
                    "$\\mathbf{b}$ from a common vertex, in exact form. **[3]**"
                ),
                "solution": (
                    "**(a)** Expand the determinant *(M1)*:  \n"
                    "$$\\mathbf{i}\\text{-component}: (-1)(-2) - (3)(4) = 2 - 12 = -10$$  \n"
                    "$$\\mathbf{j}\\text{-component}: (3)(1) - (2)(-2) = 3 + 4 = 7$$  \n"
                    "$$\\mathbf{k}\\text{-component}: (2)(4) - (-1)(1) = 8 + 1 = 9$$  \n"
                    "$$\\mathbf{a} \\times \\mathbf{b} = \\begin{pmatrix} -10 \\\\ 7 \\\\ 9 "
                    "\\end{pmatrix}. \\;(A1\\,A1)$$  \n"
                    "**(b)** $(-10)(2) + (7)(-1) + (9)(3) = -20 - 7 + 27 = 0$ ✓ *(A1)*, and "
                    "$(-10)(1) + (7)(4) + (9)(-2) = -10 + 28 - 18 = 0$ ✓ *(A1)*. Perpendicular to "
                    "both, as it must be.  \n"
                    "**(c)** $|\\mathbf{a} \\times \\mathbf{b}| = \\sqrt{100 + 49 + 81} = "
                    "\\sqrt{230}$ *(M1 A1)*, and the triangle is half the parallelogram:  \n"
                    "$$\\text{Area} = \\frac{\\sqrt{230}}{2}. \\;(A1)$$  \n"
                    "**Narrative:** part (b) is really free marks for a check you should be doing "
                    "anyway. If either dot product were non-zero, part (a) is wrong and you know "
                    "it before spending part (c)'s marks on a bad number."
                ),
                "check": [
                    "Eq(Matrix([2,-1,3]).cross(Matrix([1,4,-2])), Matrix([-10,7,9]))",
                    "Eq(Matrix([-10,7,9]).dot(Matrix([2,-1,3])), 0)",
                    "Eq(Matrix([-10,7,9]).dot(Matrix([1,4,-2])), 0)",
                    "Eq(Matrix([-10,7,9]).norm(), sqrt(230))",
                    "Eq(100 + 49 + 81, 230)",
                ],
            },
            {
                "id": "ibhl-316-we2",
                "statement": (
                    "A triangle has vertices $A(1, 0, 2)$, $B(3, 2, -1)$ and $C(0, 4, 1)$.  \n"
                    "**(a)** Find $\\overrightarrow{AB}$ and $\\overrightarrow{AC}$. **[2]**  \n"
                    "**(b)** Find $\\overrightarrow{AB} \\times \\overrightarrow{AC}$. **[3]**  \n"
                    "**(c)** Hence find the area of triangle $ABC$. **[3]**"
                ),
                "solution": (
                    "**(a)** Destination minus start *(A1 A1)*:  \n"
                    "$$\\overrightarrow{AB} = \\begin{pmatrix} 2 \\\\ 2 \\\\ -3 \\end{pmatrix}, "
                    "\\qquad \\overrightarrow{AC} = \\begin{pmatrix} -1 \\\\ 4 \\\\ -1 "
                    "\\end{pmatrix}.$$  \n"
                    "**(b)** *(M1)*  \n"
                    "$$\\mathbf{i}: (2)(-1) - (-3)(4) = -2 + 12 = 10$$  \n"
                    "$$\\mathbf{j}: (-3)(-1) - (2)(-1) = 3 + 2 = 5$$  \n"
                    "$$\\mathbf{k}: (2)(4) - (2)(-1) = 8 + 2 = 10$$  \n"
                    "$$\\overrightarrow{AB} \\times \\overrightarrow{AC} = \\begin{pmatrix} 10 "
                    "\\\\ 5 \\\\ 10 \\end{pmatrix}. \\;(A1\\,A1)$$  \n"
                    "**(c)** $\\left|\\overrightarrow{AB} \\times \\overrightarrow{AC}\\right| = "
                    "\\sqrt{100 + 25 + 100} = \\sqrt{225} = 15$ *(M1 A1)*, so  \n"
                    "$$\\text{Area} = \\tfrac{1}{2}(15) = 7.5. \\;(A1)$$  \n"
                    "**Narrative:** no height was ever constructed and no angle was ever found. "
                    "The vector product handles a triangle floating in space exactly as easily as "
                    "one lying flat — which is the whole reason HL introduces it."
                ),
                "check": [
                    "Eq(Matrix([3,2,-1]) - Matrix([1,0,2]), Matrix([2,2,-3]))",
                    "Eq(Matrix([0,4,1]) - Matrix([1,0,2]), Matrix([-1,4,-1]))",
                    "Eq(Matrix([2,2,-3]).cross(Matrix([-1,4,-1])), Matrix([10,5,10]))",
                    "Eq(Matrix([10,5,10]).norm(), 15)",
                    "Eq(Rational(1,2)*15, Rational(15,2))",
                    "Eq(Matrix([10,5,10]).dot(Matrix([2,2,-3])), 0)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Getting the sign of the middle component wrong.",
                "correction": "The $\\mathbf{j}$ term carries a minus from the determinant. Write it as $v_3w_1 - v_1w_3$ (indices reversed relative to the pattern) and the sign takes care of itself. Then dot-check.",
                "authored": True,
            },
            {
                "text": "Reporting the parallelogram area when the question asked for a triangle.",
                "correction": "$|\\mathbf{v}\\times\\mathbf{w}|$ is the PARALLELOGRAM. Halve it for the triangle. Read the question twice — this is a single careless mark, repeatedly lost.",
                "authored": True,
            },
            {
                "text": "Assuming $\\mathbf{v}\\times\\mathbf{w} = \\mathbf{w}\\times\\mathbf{v}$.",
                "correction": "It is ANTI-commutative: swapping the order negates the result. Harmless for areas (magnitudes match) but it reverses a normal vector's direction.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-316-t1",
                "statement": (
                    "Find a unit vector perpendicular to both $\\begin{pmatrix} 1 \\\\ 2 \\\\ 2 "
                    "\\end{pmatrix}$ and $\\begin{pmatrix} 2 \\\\ -2 \\\\ 1 \\end{pmatrix}$. "
                    "**[5]**"
                ),
                "solution": (
                    "The vector product supplies a perpendicular direction *(M1)*:  \n"
                    "$$\\mathbf{i}: (2)(1) - (2)(-2) = 6, \\quad \\mathbf{j}: (2)(2) - (1)(1) = 3, "
                    "\\quad \\mathbf{k}: (1)(-2) - (2)(2) = -6 \\;(A1)$$  \n"
                    "$$\\mathbf{n} = \\begin{pmatrix} 6 \\\\ 3 \\\\ -6 \\end{pmatrix}, \\qquad "
                    "|\\mathbf{n}| = \\sqrt{36 + 9 + 36} = 9. \\;(A1)$$  \n"
                    "Divide by the magnitude *(M1)*:  \n"
                    "$$\\hat{\\mathbf{n}} = \\begin{pmatrix} \\frac{2}{3} \\\\ \\frac{1}{3} \\\\ "
                    "-\\frac{2}{3} \\end{pmatrix}. \\;(A1)$$  \n"
                    "$-\\hat{\\mathbf{n}}$ is equally valid — 'a' unit vector, not 'the'. Check: "
                    "$\\frac{4 + 1 + 4}{9} = 1$ ✓, and the dot products with both originals vanish."
                ),
                "check": [
                    "Eq(Matrix([1,2,2]).cross(Matrix([2,-2,1])), Matrix([6,3,-6]))",
                    "Eq(Matrix([6,3,-6]).norm(), 9)",
                    "Eq(Rational(2,3)**2 + Rational(1,3)**2 + Rational(-2,3)**2, 1)",
                    "Eq(Matrix([6,3,-6]).dot(Matrix([1,2,2])), 0)",
                    "Eq(Matrix([6,3,-6]).dot(Matrix([2,-2,1])), 0)",
                ],
            },
            {
                "id": "ibhl-316-t2",
                "statement": (
                    "$|\\mathbf{a}| = 3$, $|\\mathbf{b}| = 5$, and the angle between them is "
                    "$30^\\circ$.  \n"
                    "**(a)** Find $|\\mathbf{a} \\times \\mathbf{b}|$. **[2]**  \n"
                    "**(b)** Verify that $|\\mathbf{a} \\times \\mathbf{b}|^2 + (\\mathbf{a}\\cdot"
                    "\\mathbf{b})^2 = |\\mathbf{a}|^2|\\mathbf{b}|^2$. **[4]**"
                ),
                "solution": (
                    "**(a)** *(M1)* $|\\mathbf{a}\\times\\mathbf{b}| = 3 \\times 5 \\times "
                    "\\sin 30^\\circ = 15 \\times \\frac{1}{2} = 7.5$ *(A1)*.  \n"
                    "**(b)** $\\mathbf{a}\\cdot\\mathbf{b} = 15\\cos 30^\\circ = "
                    "\\frac{15\\sqrt3}{2}$ *(M1 A1)*. Then  \n"
                    "$$\\left(\\tfrac{15}{2}\\right)^2 + \\left(\\tfrac{15\\sqrt3}{2}\\right)^2 = "
                    "\\frac{225}{4} + \\frac{675}{4} = \\frac{900}{4} = 225 \\;(A1)$$  \n"
                    "$$= 3^2 \\times 5^2 = 225. \\;✓\\;(A1)$$  \n"
                    "The identity is just $\\sin^2\\theta + \\cos^2\\theta = 1$ multiplied through "
                    "by $|\\mathbf{a}|^2|\\mathbf{b}|^2$ — the two products really are two halves "
                    "of one measurement."
                ),
                "check": [
                    "Eq(3*5*sin(pi/6), Rational(15,2))",
                    "Eq(3*5*cos(pi/6), 15*sqrt(3)/2)",
                    "Eq(Rational(15,2)**2 + (15*sqrt(3)/2)**2, 225)",
                    "Eq(3**2*5**2, 225)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.16 · Papers 1 & 2",
                    "title": "Two vectors in, one perpendicular vector out",
                    "body": (
                        "The scalar product asked 'how aligned are these?' and answered with a "
                        "number. The vector product asks 'how spread apart are these, and in which "
                        "plane?' and answers with a VECTOR: pointing perpendicular to both, with "
                        "length equal to the area they span. Those two outputs — a direction and "
                        "an area — are exactly what the plane and area codes need."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "What comes out?",
                    "prompt": "$\\mathbf{v} \\times \\mathbf{w}$ produces:",
                    "options": [
                        "a vector perpendicular to both $\\mathbf{v}$ and $\\mathbf{w}$",
                        "a scalar equal to $|\\mathbf{v}||\\mathbf{w}|\\cos\\theta$",
                        "a vector in the same plane as $\\mathbf{v}$ and $\\mathbf{w}$",
                        "a scalar equal to the area of the parallelogram",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "It returns a VECTOR, perpendicular to both inputs. Its MAGNITUDE is the "
                        "parallelogram's area — the last option confuses the vector with its own "
                        "length, and the second describes the scalar product."
                    ),
                    "check": [
                        "Eq(Matrix([1,0,0]).cross(Matrix([0,1,0])), Matrix([0,0,1]))",
                        "Eq(Matrix([0,0,1]).dot(Matrix([1,0,0])), 0)",
                        "Eq(Matrix([0,0,1]).dot(Matrix([0,1,0])), 0)",
                    ],
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Parallel inputs",
                    "title": "No spread, no area",
                    "prompt": "If $\\mathbf{v}$ and $\\mathbf{w}$ are parallel, then $\\mathbf{v} \\times \\mathbf{w}$ is:",
                    "options": [
                        "the zero vector",
                        "equal to $\\mathbf{v}$",
                        "of magnitude $|\\mathbf{v}||\\mathbf{w}|$",
                        "perpendicular to $\\mathbf{v}$ but not to $\\mathbf{w}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$\\sin 0 = 0$, so the magnitude vanishes: parallel vectors span a "
                        "degenerate parallelogram with no area. Compare the SCALAR product, which "
                        "is at its maximum for parallel vectors — the two products are exact "
                        "opposites in this respect."
                    ),
                    "check": [
                        "Eq(Matrix([2,-3,4]).cross(Matrix([4,-6,8])), Matrix([0,0,0]))",
                        "Eq(sin(0), 0)",
                        "Eq(Matrix([2,-3,4]).cross(Matrix([2,-3,4])), Matrix([0,0,0]))",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Compute, check, then measure",
                    "problemId": "ibhl-316-we1",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "A perpendicular unit vector",
                    "problemId": "ibhl-316-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "Areas",
                    "title": "Why this beats base × height in 3D",
                    "body": (
                        "A triangle drifting in space has no obvious base and no measurable height "
                        "— finding them would mean projecting, and that is more work than the "
                        "answer is worth. The vector product bypasses all of it: "
                        "$\\frac{1}{2}\\left|\\overrightarrow{AB} \\times "
                        "\\overrightarrow{AC}\\right|$ takes two subtractions, one determinant and "
                        "one square root, and it does not care how the triangle is oriented."
                    ),
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Three vertices to an area",
                    "problemId": "ibhl-316-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "The two products, together",
                    "problemId": "ibhl-316-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.16 in four lines",
                    "points": [
                        "$\\mathbf{v}\\times\\mathbf{w}$ is a VECTOR perpendicular to both; the middle component carries the minus.",
                        "$|\\mathbf{v}\\times\\mathbf{w}| = |\\mathbf{v}||\\mathbf{w}|\\sin\\theta$ = parallelogram area; halve for a triangle.",
                        "Free check: dot your answer with both inputs — two zeros or start again.",
                        "Anti-commutative ($\\mathbf{w}\\times\\mathbf{v} = -\\mathbf{v}\\times\\mathbf{w}$), and zero for parallel vectors.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 9 — AHL 3.17 & 3.18: Planes, intersections and angles
# ===========================================================================
def lesson_planes():
    return {
        "slug": "planes-and-intersections",
        "title": "Planes: Equations, Intersections & Angles",
        "concreteComparison": (
            "To describe a flat tabletop you do not list its points — you say where it sits and "
            "which way is 'up' from it. One point and one perpendicular direction pin a plane "
            "completely and unambiguously. That normal vector is the whole idea: every question "
            "about planes turns into a question about their normals."
        ),
        "objective": (
            "Write the vector and Cartesian equations of a plane, construct a plane through three "
            "points, find where a line meets a plane, and compute the angle between two planes and "
            "between a line and a plane."
        ),
        "concept": [
            "**Syllabus cards — AHL 3.17 and 3.18.** Vector equation of a plane $\\mathbf{r} = "
            "\\mathbf{a} + \\lambda\\mathbf{b} + \\mu\\mathbf{c}$; use of the normal vector to "
            "obtain $\\mathbf{r}\\cdot\\mathbf{n} = \\mathbf{a}\\cdot\\mathbf{n}$; Cartesian "
            "equation $ax + by + cz = d$. Intersections of a line with a plane and of two planes; "
            "the angle between two planes and between a line and a plane. Papers 1 and 2. "
            "Combined weight: 8-14 marks, usually as a full Section B question.",
            "**The normal form, and why it is the useful one.** The parametric form "
            "$\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b} + \\mu\\mathbf{c}$ needs two "
            "parameters and is awkward to test points against. The normal form is far better: "
            "$$\\mathbf{r}\\cdot\\mathbf{n} = \\mathbf{a}\\cdot\\mathbf{n} \\qquad\\text{i.e.}"
            "\\qquad ax + by + cz = d,$$ "
            "where $\\mathbf{n} = (a, b, c)$. The COEFFICIENTS of the Cartesian equation ARE the "
            "normal vector — read it off instantly, and the constant $d$ comes from substituting "
            "any known point.",
            "**A plane through three points.** Form two direction vectors from the points, take "
            "their vector product for $\\mathbf{n}$, then substitute one point to get $d$. From "
            "$A(1, 0, 2)$, $B(3, 2, -1)$, $C(0, 4, 1)$: $\\overrightarrow{AB}\\times"
            "\\overrightarrow{AC} = (10, 5, 10)$, which simplifies to $\\mathbf{n} = (2, 1, 2)$, "
            "and $d = 2(1) + 0 + 2(2) = 6$, giving $2x + y + 2z = 6$. Scaling the normal down is "
            "legitimate and keeps the arithmetic clean — then CHECK the other two points satisfy "
            "it.",
            "**Line meets plane: one substitution.** Put the line's parametric coordinates into "
            "the plane equation and solve the resulting LINEAR equation for $\\lambda$. Three "
            "outcomes, all examinable: one solution (the line crosses the plane at a single "
            "point); no solution, i.e. the $\\lambda$ terms cancel and leave a false statement "
            "(the line is parallel to the plane and misses it); or the equation reduces to $0 = 0$ "
            "(the line lies IN the plane).",
            "**Two angle formulas — and they are not the same.** Between two PLANES, use the "
            "normals directly: "
            "$$\\cos\\theta = \\frac{|\\mathbf{n}_1\\cdot\\mathbf{n}_2|}{|\\mathbf{n}_1|"
            "|\\mathbf{n}_2|}.$$ "
            "Between a LINE and a PLANE, the direction vector is at $(90^\\circ - \\theta)$ to the "
            "normal, so the cosine becomes a SINE: "
            "$$\\sin\\theta = \\frac{|\\mathbf{d}\\cdot\\mathbf{n}|}{|\\mathbf{d}||\\mathbf{n}|}.$$ "
            "Using cosine for the line-plane case is the most-penalised single error in this "
            "whole unit — it returns the complement of the correct answer.",
        ],
        "keyIdea": (
            "A plane is one point plus one normal: $ax + by + cz = d$ with $\\mathbf{n} = "
            "(a, b, c)$ read off the coefficients. Three points $\\to$ normal by vector product. "
            "Line meets plane by substituting for $\\lambda$. Plane-plane angle uses COSINE of the "
            "normals; line-plane angle uses SINE."
        ),
        "facts": [
            {
                "title": "Plane in normal form",
                "latex": "\\mathbf{r}\\cdot\\mathbf{n} = \\mathbf{a}\\cdot\\mathbf{n} \\quad\\Longleftrightarrow\\quad ax + by + cz = d",
                "explanation": (
                    "IN the booklet. The coefficients $(a, b, c)$ ARE the normal vector — the "
                    "single most useful fact about planes."
                ),
            },
            {
                "title": "Angle between two planes",
                "latex": "\\cos\\theta = \\frac{|\\mathbf{n}_1\\cdot\\mathbf{n}_2|}{|\\mathbf{n}_1||\\mathbf{n}_2|}",
                "explanation": (
                    "The angle between planes equals the angle between their normals. The modulus "
                    "forces the acute answer."
                ),
            },
            {
                "title": "Angle between a line and a plane",
                "latex": "\\sin\\theta = \\frac{|\\mathbf{d}\\cdot\\mathbf{n}|}{|\\mathbf{d}||\\mathbf{n}|}",
                "explanation": (
                    "SINE, not cosine — the direction sits $90^\\circ - \\theta$ from the normal. "
                    "Mixing these up returns the complement of the right answer."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibhl-317-we1",
                "statement": (
                    "The plane $\\Pi$ contains the points $A(1, 0, 2)$, $B(3, 2, -1)$ and "
                    "$C(0, 4, 1)$.  \n"
                    "**(a)** Find a normal vector to $\\Pi$. **[3]**  \n"
                    "**(b)** Find the Cartesian equation of $\\Pi$. **[3]**  \n"
                    "**(c)** Verify that $B$ and $C$ satisfy your equation. **[2]**"
                ),
                "solution": (
                    "**(a)** Two directions inside the plane *(M1)*: $\\overrightarrow{AB} = "
                    "(2, 2, -3)$ and $\\overrightarrow{AC} = (-1, 4, -1)$. Their vector product is "
                    "perpendicular to both, hence normal to the plane *(M1)*:  \n"
                    "$$\\overrightarrow{AB} \\times \\overrightarrow{AC} = \\begin{pmatrix} 10 "
                    "\\\\ 5 \\\\ 10 \\end{pmatrix} \\;\\longrightarrow\\; \\mathbf{n} = "
                    "\\begin{pmatrix} 2 \\\\ 1 \\\\ 2 \\end{pmatrix} \\;(A1)$$  \n"
                    "(dividing by $5$ — any scalar multiple is still normal).  \n"
                    "**(b)** Use $\\mathbf{r}\\cdot\\mathbf{n} = \\mathbf{a}\\cdot\\mathbf{n}$ "
                    "with $A$ *(M1)*:  \n"
                    "$$d = 2(1) + 1(0) + 2(2) = 6 \\;(A1)$$  \n"
                    "$$\\Pi: \\; 2x + y + 2z = 6. \\;(A1)$$  \n"
                    "**(c)** $B$: $2(3) + 2 + 2(-1) = 6 + 2 - 2 = 6$ ✓ *(A1)*. $C$: $2(0) + 4 + "
                    "2(1) = 6$ ✓ *(A1)*.  \n"
                    "**Narrative:** simplifying $(10, 5, 10)$ to $(2, 1, 2)$ before finding $d$ "
                    "keeps every later number small — and part (c) is not busywork, it is the only "
                    "thing standing between a sign slip and a wrong plane."
                ),
                "check": [
                    "Eq(Matrix([3,2,-1]) - Matrix([1,0,2]), Matrix([2,2,-3]))",
                    "Eq(Matrix([0,4,1]) - Matrix([1,0,2]), Matrix([-1,4,-1]))",
                    "Eq(Matrix([2,2,-3]).cross(Matrix([-1,4,-1])), Matrix([10,5,10]))",
                    "Eq(Matrix([10,5,10])/5, Matrix([2,1,2]))",
                    "Eq(Matrix([2,1,2]).dot(Matrix([1,0,2])), 6)",
                    "Eq(Matrix([2,1,2]).dot(Matrix([3,2,-1])), 6)",
                    "Eq(Matrix([2,1,2]).dot(Matrix([0,4,1])), 6)",
                ],
            },
            {
                "id": "ibhl-318-we2",
                "statement": (
                    "The line $L$ has equation $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 "
                    "\\end{pmatrix} + \\lambda\\begin{pmatrix} 2 \\\\ -1 \\\\ 1 \\end{pmatrix}$ "
                    "and the plane $\\Pi$ has equation $2x + y + 2z = 6$.  \n"
                    "**(a)** Find the coordinates of the point where $L$ meets $\\Pi$. **[4]**  \n"
                    "**(b)** Find the angle between $L$ and $\\Pi$, correct to 3 significant "
                    "figures. **[4]**"
                ),
                "solution": (
                    "**(a)** A general point on $L$ is $(1 + 2\\lambda,\\; 2 - \\lambda,\\; "
                    "3 + \\lambda)$. Substitute into the plane *(M1)*:  \n"
                    "$$2(1 + 2\\lambda) + (2 - \\lambda) + 2(3 + \\lambda) = 6$$  \n"
                    "$$2 + 4\\lambda + 2 - \\lambda + 6 + 2\\lambda = 10 + 5\\lambda = 6 \\;(A1)$$  \n"
                    "$$\\Longrightarrow\\; \\lambda = -\\tfrac{4}{5}. \\;(A1)$$  \n"
                    "Substituting back *(A1)*:  \n"
                    "$$\\left(-\\tfrac{3}{5},\\; \\tfrac{14}{5},\\; \\tfrac{11}{5}\\right).$$  \n"
                    "**(b)** Line to plane means SINE of the normal angle *(M1)*. With "
                    "$\\mathbf{d} = (2, -1, 1)$ and $\\mathbf{n} = (2, 1, 2)$:  \n"
                    "$$\\mathbf{d}\\cdot\\mathbf{n} = 4 - 1 + 2 = 5, \\qquad |\\mathbf{d}| = "
                    "\\sqrt6, \\quad |\\mathbf{n}| = 3 \\;(A1)$$  \n"
                    "$$\\sin\\theta = \\frac{5}{3\\sqrt6} \\approx 0.68041 \\;(A1) "
                    "\\;\\Longrightarrow\\; \\theta = 42.9^\\circ \\;(3\\text{ s.f.}). \\;(A1)$$  \n"
                    "**Narrative:** check part (a) by substituting the point back: "
                    "$2(-\\frac{3}{5}) + \\frac{14}{5} + 2(\\frac{11}{5}) = \\frac{-6 + 14 + 22}"
                    "{5} = 6$ ✓. And in (b), had you used cosine you would have got $47.1^\\circ$ "
                    "— the complement, and no marks."
                ),
                "check": [
                    "Eq(2*(1 + 2*Rational(-4,5)) + (2 - Rational(-4,5)) + 2*(3 + Rational(-4,5)), 6)",
                    "solve(Eq(10 + 5*L, 6), L) == [Rational(-4,5)]",
                    "Eq(Matrix([1,2,3]) + Rational(-4,5)*Matrix([2,-1,1]), Matrix([Rational(-3,5), Rational(14,5), Rational(11,5)]))",
                    "Eq(Matrix([2,1,2]).dot(Matrix([Rational(-3,5), Rational(14,5), Rational(11,5)])), 6)",
                    "Eq(Matrix([2,-1,1]).dot(Matrix([2,1,2])), 5)",
                    "Abs(deg(asin(5/(3*sqrt(6)))) - 42.876) < Rational(1,100)",
                    "Abs(deg(asin(5/(3*sqrt(6)))) + deg(acos(5/(3*sqrt(6)))) - 90) < Rational(1,1000000)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using cosine for the angle between a line and a plane.",
                "correction": "The direction vector makes angle $90^\\circ - \\theta$ with the normal, so $\\sin\\theta = \\frac{|\\mathbf{d}\\cdot\\mathbf{n}|}{|\\mathbf{d}||\\mathbf{n}|}$. If you used cosine, your answer is the complement — subtract from $90^\\circ$.",
                "authored": True,
            },
            {
                "text": "Treating $ax + by + cz = d$ as though $(a, b, c)$ were a point on the plane.",
                "correction": "The coefficients are the NORMAL vector, pointing perpendicular to the plane. To get a point, choose convenient values for two variables and solve for the third.",
                "authored": True,
            },
            {
                "text": "Declaring 'no intersection' when the $\\lambda$ terms cancel, without reading the remaining statement.",
                "correction": "If it collapses to something false ($10 = 6$) the line is parallel and misses. If it collapses to $0 = 0$, the line lies IN the plane — every point works. Two very different answers.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibhl-318-t1",
                "statement": (
                    "Find the acute angle between the planes $x + 2y - 2z = 5$ and "
                    "$2x - y + 2z = 1$, correct to 3 significant figures. **[5]**"
                ),
                "solution": (
                    "Read the normals straight off the coefficients *(A1)*: $\\mathbf{n}_1 = "
                    "(1, 2, -2)$ and $\\mathbf{n}_2 = (2, -1, 2)$.  \n"
                    "$$\\mathbf{n}_1\\cdot\\mathbf{n}_2 = 2 - 2 - 4 = -4, \\qquad |\\mathbf{n}_1| "
                    "= 3, \\quad |\\mathbf{n}_2| = 3. \\;(M1\\,A1)$$  \n"
                    "Plane to plane means COSINE, with a modulus for the acute value *(M1)*:  \n"
                    "$$\\cos\\theta = \\frac{|-4|}{9} = \\frac{4}{9} \\approx 0.4444 "
                    "\\;\\Longrightarrow\\; \\theta = 63.6^\\circ \\;(3\\text{ s.f.}). \\;(A1)$$  \n"
                    "Without the modulus you would report $116^\\circ$ — the obtuse partner, and "
                    "the question said acute."
                ),
                "check": [
                    "Eq(Matrix([1,2,-2]).dot(Matrix([2,-1,2])), -4)",
                    "Eq(Matrix([1,2,-2]).norm(), 3)",
                    "Eq(Matrix([2,-1,2]).norm(), 3)",
                    "Abs(deg(acos(Rational(4,9))) - 63.612) < Rational(1,100)",
                    "Abs(deg(acos(Rational(4,9))) + deg(acos(Rational(-4,9))) - 180) < Rational(1,1000000)",
                ],
            },
            {
                "id": "ibhl-318-t2",
                "statement": (
                    "Find the shortest distance from the point $P(4, 2, 1)$ to the plane "
                    "$2x + y + 2z = 6$. **[5]**"
                ),
                "solution": (
                    "Take any point on the plane, say $Q(3, 0, 0)$ — check: $2(3) = 6$ ✓ *(A1)*. "
                    "The shortest distance is the component of $\\overrightarrow{QP}$ along the "
                    "unit normal *(M1)*, since the perpendicular is the shortest route to a "
                    "plane.  \n"
                    "$$\\overrightarrow{QP} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 1 \\end{pmatrix}, "
                    "\\qquad \\mathbf{n} = \\begin{pmatrix} 2 \\\\ 1 \\\\ 2 \\end{pmatrix}, "
                    "\\qquad |\\mathbf{n}| = 3. \\;(A1)$$  \n"
                    "$$\\text{distance} = \\frac{\\left|\\overrightarrow{QP}\\cdot\\mathbf{n}"
                    "\\right|}{|\\mathbf{n}|} = \\frac{|2 + 2 + 2|}{3} = \\frac{6}{3} = 2. "
                    "\\;(M1\\,A1)$$  \n"
                    "Equivalently, substitute $P$ into the plane and compare: "
                    "$\\frac{|2(4) + 2 + 2(1) - 6|}{3} = \\frac{6}{3} = 2$ — the same computation, "
                    "written more compactly."
                ),
                "check": [
                    "Eq(Matrix([2,1,2]).dot(Matrix([3,0,0])), 6)",
                    "Eq(Matrix([4,2,1]) - Matrix([3,0,0]), Matrix([1,2,1]))",
                    "Eq(Matrix([1,2,1]).dot(Matrix([2,1,2])), 6)",
                    "Eq(Matrix([2,1,2]).norm(), 3)",
                    "Eq(Abs(Matrix([2,1,2]).dot(Matrix([4,2,1])) - 6)/Matrix([2,1,2]).norm(), 2)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AHL 3.17 · Papers 1 & 2",
                    "title": "A plane is a point and a perpendicular",
                    "body": (
                        "Fix a point and a direction perpendicular to the surface, and the plane is "
                        "determined — there is exactly one flat surface through that point at right "
                        "angles to that direction. Algebraically: a point $\\mathbf{r}$ is on the "
                        "plane precisely when $\\mathbf{r} - \\mathbf{a}$ is perpendicular to "
                        "$\\mathbf{n}$, i.e. $(\\mathbf{r} - \\mathbf{a})\\cdot\\mathbf{n} = 0$, "
                        "which rearranges to $\\mathbf{r}\\cdot\\mathbf{n} = "
                        "\\mathbf{a}\\cdot\\mathbf{n}$."
                    ),
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Check yourself",
                    "title": "Read the normal",
                    "prompt": "The plane $3x - y + 4z = 12$ has normal vector:",
                    "options": [
                        "$\\begin{pmatrix} 3 \\\\ -1 \\\\ 4 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 3 \\\\ -1 \\\\ 4 \\\\ 12 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 12 \\\\ 12 \\\\ 12 \\end{pmatrix}$",
                        "$\\begin{pmatrix} 4 \\\\ -12 \\\\ 3 \\end{pmatrix}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The coefficients of $x$, $y$, $z$ ARE the normal. The constant $12$ fixes "
                        "how far the plane sits from the origin — it plays no part in the "
                        "direction, which is why parallel planes differ only in their constant."
                    ),
                    "check": [
                        "Eq(Matrix([3,-1,4]).dot(Matrix([4,0,0])), 12)",
                        "Eq(Matrix([3,-1,4]).dot(Matrix([0,-12,0])), 12)",
                        "Eq(Matrix([3,-1,4]).dot(Matrix([0,0,3])), 12)",
                    ],
                },
                {
                    "kind": "teach",
                    "eyebrow": "Construction",
                    "title": "Three points make a plane",
                    "body": (
                        "Three non-collinear points determine a plane, and the vector product turns "
                        "that fact into an algorithm: subtract to get two directions lying IN the "
                        "plane, cross them to get a direction perpendicular to it, then substitute "
                        "any of the three points to find $d$. Simplify the normal by dividing out "
                        "common factors first — it costs nothing and every subsequent number gets "
                        "smaller."
                    ),
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Three points to a Cartesian equation",
                    "problemId": "ibhl-317-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "AHL 3.18",
                    "title": "Which formula, which situation?",
                    "prompt": "To find the angle between a LINE and a PLANE you use:",
                    "options": [
                        "$\\sin\\theta = \\dfrac{|\\mathbf{d}\\cdot\\mathbf{n}|}{|\\mathbf{d}||\\mathbf{n}|}$",
                        "$\\cos\\theta = \\dfrac{|\\mathbf{d}\\cdot\\mathbf{n}|}{|\\mathbf{d}||\\mathbf{n}|}$",
                        "$\\tan\\theta = \\dfrac{|\\mathbf{d}\\times\\mathbf{n}|}{\\mathbf{d}\\cdot\\mathbf{n}}$",
                        "$\\cos\\theta = \\dfrac{|\\mathbf{n}_1\\cdot\\mathbf{n}_2|}{|\\mathbf{n}_1||\\mathbf{n}_2|}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The formula computes the angle to the NORMAL, but the angle you want is to "
                        "the PLANE — and those two are complementary. Since $\\cos(90^\\circ - "
                        "\\theta) = \\sin\\theta$, the cosine formula becomes a sine. The last "
                        "option is the plane-to-plane formula, a different question."
                    ),
                    "check": [
                        "Eq(simplify(cos(pi/2 - x) - sin(x)), 0)",
                        "Abs(deg(asin(5/(3*sqrt(6)))) + deg(acos(5/(3*sqrt(6)))) - 90) < Rational(1,1000000)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Line meets plane, and at what angle",
                    "problemId": "ibhl-318-we2",
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Two planes, one acute angle",
                    "problemId": "ibhl-318-t1",
                },
                {
                    "kind": "teach",
                    "eyebrow": "Three outcomes",
                    "title": "When a line does not cross",
                    "body": (
                        "Substituting the line into the plane always produces a linear equation in "
                        "$\\lambda$, and the shape of that equation is the answer. A normal "
                        "solution means one crossing point. If the $\\lambda$ terms cancel and "
                        "leave something false, the line runs parallel to the plane and never "
                        "reaches it. If they cancel and leave $0 = 0$, EVERY $\\lambda$ works — the "
                        "line lies entirely within the plane. Read the collapsed equation before "
                        "declaring anything."
                    ),
                },
                {
                    "kind": "tryIt",
                    "eyebrow": "Your turn",
                    "title": "Perpendicular is shortest",
                    "problemId": "ibhl-318-t2",
                },
                {
                    "kind": "recap",
                    "title": "AHL 3.17-3.18 in five lines",
                    "points": [
                        "$ax + by + cz = d$ with $\\mathbf{n} = (a, b, c)$ — the coefficients ARE the normal.",
                        "Three points $\\to$ two directions $\\to$ vector product $\\to$ normal $\\to$ substitute for $d$.",
                        "Line meets plane: substitute the parametric coordinates and solve for $\\lambda$.",
                        "Collapse to something false $\\Rightarrow$ parallel and missing; collapse to $0 = 0$ $\\Rightarrow$ line lies in the plane.",
                        "Plane-plane angle: COSINE of normals. Line-plane angle: SINE. Modulus both times.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Practice bank — one or two per subtopic code, exam-shaped
# ===========================================================================
def practice_bank():
    return [
        {
            "id": "ibhl-gt-p01",
            "statement": (
                "Given that $\\sec\\theta = -\\dfrac{13}{5}$ and $\\pi < \\theta < "
                "\\dfrac{3\\pi}{2}$, find the exact value of $\\tan\\theta$. **[4]**"
            ),
            "solution": (
                "$\\tan^2\\theta = \\sec^2\\theta - 1 = \\frac{169}{25} - 1 = \\frac{144}{25}$ "
                "*(M1 A1)*, so $\\tan\\theta = \\pm\\frac{12}{5}$. The interval places $\\theta$ "
                "in the third quadrant, where sine and cosine are both negative and tangent is "
                "therefore POSITIVE *(R1)*:  \n"
                "$$\\tan\\theta = \\frac{12}{5}. \\;(A1)$$  \n"
                "Cross-check: $\\cos\\theta = -\\frac{5}{13}$ and $\\sin\\theta = -\\frac{12}{13}$ "
                "give the same quotient ✓."
            ),
            "badges": code_badge("ib-aa-hl-3.9", 4, "P1"),
            "check": [
                "Eq(Rational(169,25) - 1, Rational(144,25))",
                "Eq(Rational(-12,13)/Rational(-5,13), Rational(12,5))",
                "Eq(Rational(-5,13)**2 + Rational(-12,13)**2, 1)",
                "Eq(1/Rational(-5,13), Rational(-13,5))",
            ],
        },
        {
            "id": "ibhl-gt-p02",
            "statement": (
                "Find the exact value of $\\arctan 1 + \\arcsin\\dfrac{\\sqrt3}{2} - "
                "\\arccos 0$. **[4]**"
            ),
            "solution": (
                "Each inverse answers inside its own range *(M1)*:  \n"
                "$$\\arctan 1 = \\frac{\\pi}{4}, \\qquad \\arcsin\\frac{\\sqrt3}{2} = "
                "\\frac{\\pi}{3}, \\qquad \\arccos 0 = \\frac{\\pi}{2}. \\;(A1\\,A1)$$  \n"
                "$$\\frac{\\pi}{4} + \\frac{\\pi}{3} - \\frac{\\pi}{2} = "
                "\\frac{3\\pi + 4\\pi - 6\\pi}{12} = \\frac{\\pi}{12}. \\;(A1)$$  \n"
                "Note $\\arccos 0 = \\frac{\\pi}{2}$, not $0$ — the question asks for the ANGLE "
                "whose cosine is zero."
            ),
            "badges": code_badge("ib-aa-hl-3.9", 4, "P1"),
            "check": [
                "Eq(atan(1), pi/4)",
                "Eq(asin(sqrt(3)/2), pi/3)",
                "Eq(acos(0), pi/2)",
                "Eq(atan(1) + asin(sqrt(3)/2) - acos(0), pi/12)",
            ],
        },
        {
            "id": "ibhl-gt-p03",
            "statement": (
                "$A$ and $B$ are acute angles with $\\tan A = \\dfrac{1}{2}$ and $\\tan B = "
                "\\dfrac{1}{3}$. Show that $A + B = \\dfrac{\\pi}{4}$. **[4]**"
            ),
            "solution": (
                "Apply the compound angle formula for tangent *(M1)*:  \n"
                "$$\\tan(A + B) = \\frac{\\frac{1}{2} + \\frac{1}{3}}{1 - \\frac{1}{2}\\cdot"
                "\\frac{1}{3}} = \\frac{\\frac{5}{6}}{\\frac{5}{6}} = 1. \\;(A1\\,A1)$$  \n"
                "Both $A$ and $B$ are acute and each has tangent less than $1$, so each is under "
                "$\\frac{\\pi}{4}$ and their sum is under $\\frac{\\pi}{2}$ *(R1)*. The only such "
                "angle with tangent $1$ is $\\frac{\\pi}{4}$ *(AG)*.  \n"
                "The range argument is doing real work here: $\\tan(A+B) = 1$ alone would also "
                "permit $\\frac{5\\pi}{4}$."
            ),
            "badges": code_badge("ib-aa-hl-3.10", 4, "P1"),
            "check": [
                "Eq((Rational(1,2) + Rational(1,3))/(1 - Rational(1,2)*Rational(1,3)), 1)",
                "Abs(atan(Rational(1,2)) + atan(Rational(1,3)) - pi/4) < Rational(1,1000000)",
                "Eq(tan(pi/4), 1)",
                "atan(Rational(1,2)) < pi/4",
            ],
        },
        {
            "id": "ibhl-gt-p04",
            "statement": (
                "Solve $2\\sin^2 x = \\sin x$ for $0 \\le x < 2\\pi$. **[5]**"
            ),
            "solution": (
                "Do NOT divide by $\\sin x$ — that discards solutions. Factorise instead "
                "*(M1)*:  \n"
                "$$2\\sin^2 x - \\sin x = 0 \\;\\Longleftrightarrow\\; \\sin x\\,(2\\sin x - 1) "
                "= 0. \\;(A1)$$  \n"
                "$\\sin x = 0$ gives $x = 0, \\pi$ *(A1)*; $\\sin x = \\frac{1}{2}$ gives "
                "$x = \\frac{\\pi}{6}$ and its supplement $\\frac{5\\pi}{6}$ *(A1)*.  \n"
                "$$x = 0, \\;\\frac{\\pi}{6}, \\;\\frac{5\\pi}{6}, \\;\\pi. \\;(A1)$$  \n"
                "Dividing through by $\\sin x$ would have lost the first and last — two of the "
                "four marks, for a step that felt like simplification."
            ),
            "badges": code_badge("ib-aa-hl-3.11", 5, "P1"),
            "check": [
                "Eq(2*sin(0)**2, sin(0))",
                "Eq(2*sin(pi)**2, sin(pi))",
                "Eq(2*sin(pi/6)**2, sin(pi/6))",
                "Eq(2*sin(5*pi/6)**2, sin(5*pi/6))",
                "Ne(2*sin(pi/2)**2, sin(pi/2))",
            ],
        },
        {
            "id": "ibhl-gt-p05",
            "statement": (
                "Let $\\mathbf{a} = \\begin{pmatrix} 3 \\\\ -1 \\\\ 2 \\end{pmatrix}$ and "
                "$\\mathbf{b} = \\begin{pmatrix} 1 \\\\ 2 \\\\ -2 \\end{pmatrix}$. Find "
                "$|2\\mathbf{a} + \\mathbf{b}|$ in exact form. **[4]**"
            ),
            "solution": (
                "Scale first, then add componentwise *(M1)*:  \n"
                "$$2\\mathbf{a} + \\mathbf{b} = \\begin{pmatrix} 6 + 1 \\\\ -2 + 2 \\\\ 4 - 2 "
                "\\end{pmatrix} = \\begin{pmatrix} 7 \\\\ 0 \\\\ 2 \\end{pmatrix}. \\;(A1)$$  \n"
                "$$|2\\mathbf{a} + \\mathbf{b}| = \\sqrt{49 + 0 + 4} = \\sqrt{53}. \\;(M1\\,A1)$$  \n"
                "$53$ is prime, so the surd is already in simplest form."
            ),
            "badges": code_badge("ib-aa-hl-3.12", 4, "P1"),
            "check": [
                "Eq(2*Matrix([3,-1,2]) + Matrix([1,2,-2]), Matrix([7,0,2]))",
                "Eq(Matrix([7,0,2]).norm(), sqrt(53))",
                "Eq(49 + 4, 53)",
            ],
        },
        {
            "id": "ibhl-gt-p06",
            "statement": (
                "Find the angle between $\\begin{pmatrix} 1 \\\\ -2 \\\\ 2 \\end{pmatrix}$ and "
                "$\\begin{pmatrix} 3 \\\\ 0 \\\\ 4 \\end{pmatrix}$, correct to 3 significant "
                "figures. **[4]**"
            ),
            "solution": (
                "Scalar product *(M1)*: $(1)(3) + (-2)(0) + (2)(4) = 3 + 0 + 8 = 11$ *(A1)*.  \n"
                "Magnitudes: $\\sqrt{1 + 4 + 4} = 3$ and $\\sqrt{9 + 0 + 16} = 5$ *(A1)*.  \n"
                "$$\\cos\\theta = \\frac{11}{15} \\approx 0.73333 \\;\\Longrightarrow\\; "
                "\\theta = 42.8^\\circ \\;(3\\text{ s.f.}). \\;(A1)$$  \n"
                "Both magnitudes came out whole — the vectors were chosen from Pythagorean "
                "triples, which is common on Paper 1 where no calculator is available."
            ),
            "badges": code_badge("ib-aa-hl-3.13", 4, "P2"),
            "check": [
                "Eq(Matrix([1,-2,2]).dot(Matrix([3,0,4])), 11)",
                "Eq(Matrix([1,-2,2]).norm(), 3)",
                "Eq(Matrix([3,0,4]).norm(), 5)",
                "Abs(deg(acos(Rational(11,15))) - 42.8334) < Rational(1,100)",
            ],
        },
        {
            "id": "ibhl-gt-p07",
            "statement": (
                "The line $L$ passes through $A(2, 1, -3)$ and $B(4, -3, 1)$.  \n"
                "**(a)** Write $L$ in Cartesian form, using the simplest integer direction "
                "vector. **[4]**  \n"
                "**(b)** Find the coordinates of the point on $L$ with $y = -7$. **[3]**"
            ),
            "solution": (
                "**(a)** $\\overrightarrow{AB} = \\begin{pmatrix} 2 \\\\ -4 \\\\ 4 \\end{pmatrix}$ "
                "*(M1)*, which divides by $2$ to give $\\begin{pmatrix} 1 \\\\ -2 \\\\ 2 "
                "\\end{pmatrix}$ — same direction, smaller numbers *(A1)*.  \n"
                "$$\\frac{x - 2}{1} = \\frac{y - 1}{-2} = \\frac{z + 3}{2}. \\;(A1\\,A1)$$  \n"
                "**(b)** Using $\\mathbf{r} = (2, 1, -3) + \\lambda(1, -2, 2)$: set "
                "$1 - 2\\lambda = -7$ *(M1)*, so $\\lambda = 4$ *(A1)*, giving  \n"
                "$$(2 + 4,\\; -7,\\; -3 + 8) = (6, -7, 5). \\;(A1)$$  \n"
                "Confirm with the Cartesian form: $\\frac{6-2}{1} = 4$, $\\frac{-7-1}{-2} = 4$, "
                "$\\frac{5+3}{2} = 4$ — all three equal, so the point is genuinely on $L$ ✓."
            ),
            "badges": code_badge("ib-aa-hl-3.14", 7, "P1"),
            "check": [
                "Eq(Matrix([4,-3,1]) - Matrix([2,1,-3]), Matrix([2,-4,4]))",
                "Eq(Matrix([2,-4,4])/2, Matrix([1,-2,2]))",
                "Eq(Matrix([2,1,-3]) + 4*Matrix([1,-2,2]), Matrix([6,-7,5]))",
                "Eq(Rational(6-2,1), 4)",
                "Eq(Rational(-7-1,-2), 4)",
                "Eq(Rational(5+3,2), 4)",
            ],
        },
        {
            "id": "ibhl-gt-p08",
            "statement": (
                "Find the exact area of the triangle with vertices $P(1, 1, 0)$, $Q(3, 0, 2)$ and "
                "$R(2, 3, 1)$. **[6]**"
            ),
            "solution": (
                "Two edge vectors from the same vertex *(M1)*: $\\overrightarrow{PQ} = "
                "(2, -1, 2)$ and $\\overrightarrow{PR} = (1, 2, 1)$ *(A1)*.  \n"
                "Vector product *(M1)*:  \n"
                "$$\\mathbf{i}: (-1)(1) - (2)(2) = -5, \\quad \\mathbf{j}: (2)(1) - (2)(1) = 0, "
                "\\quad \\mathbf{k}: (2)(2) - (-1)(1) = 5$$  \n"
                "$$\\overrightarrow{PQ} \\times \\overrightarrow{PR} = \\begin{pmatrix} -5 \\\\ 0 "
                "\\\\ 5 \\end{pmatrix}, \\qquad \\left|\\;\\right| = \\sqrt{50} = 5\\sqrt2. "
                "\\;(A1\\,A1)$$  \n"
                "$$\\text{Area} = \\tfrac{1}{2}\\left(5\\sqrt2\\right) = \\frac{5\\sqrt2}{2}. "
                "\\;(A1)$$  \n"
                "Free check: $(-5, 0, 5)\\cdot(2, -1, 2) = -10 + 0 + 10 = 0$ ✓."
            ),
            "badges": code_badge("ib-aa-hl-3.16", 6, "P1"),
            "check": [
                "Eq(Matrix([3,0,2]) - Matrix([1,1,0]), Matrix([2,-1,2]))",
                "Eq(Matrix([2,3,1]) - Matrix([1,1,0]), Matrix([1,2,1]))",
                "Eq(Matrix([2,-1,2]).cross(Matrix([1,2,1])), Matrix([-5,0,5]))",
                "Eq(Matrix([-5,0,5]).norm(), 5*sqrt(2))",
                "Eq(Matrix([-5,0,5]).dot(Matrix([2,-1,2])), 0)",
                "Eq(Matrix([-5,0,5]).dot(Matrix([1,2,1])), 0)",
            ],
        },
        {
            "id": "ibhl-gt-p09",
            "statement": (
                "Find the Cartesian equation of the plane through $(2, -1, 3)$ with normal vector "
                "$\\begin{pmatrix} 1 \\\\ 4 \\\\ -2 \\end{pmatrix}$, and state whether the origin "
                "lies on it. **[4]**"
            ),
            "solution": (
                "The coefficients come straight from the normal, so the equation is "
                "$x + 4y - 2z = d$ *(M1)*. Substitute the given point to find $d$ *(A1)*:  \n"
                "$$d = 2 + 4(-1) - 2(3) = 2 - 4 - 6 = -8.$$  \n"
                "$$x + 4y - 2z = -8. \\;(A1)$$  \n"
                "The origin gives $0 + 0 - 0 = 0 \\ne -8$, so it does NOT lie on the plane "
                "*(A1)*. Indeed $d \\ne 0$ is exactly the condition for a plane to miss the "
                "origin."
            ),
            "badges": code_badge("ib-aa-hl-3.17", 4, "P1"),
            "check": [
                "Eq(Matrix([1,4,-2]).dot(Matrix([2,-1,3])), -8)",
                "Eq(Matrix([1,4,-2]).dot(Matrix([0,0,0])), 0)",
                "Ne(0, -8)",
            ],
        },
    ]


# ===========================================================================
# Test-yourself bank — six multi-part questions in exam register
# ===========================================================================
def test_bank():
    return [
        {
            "id": "ibhl-gt-q01",
            "statement": (
                "$\\theta$ is obtuse and $\\cos\\theta = -\\dfrac{3}{5}$.  \n"
                "**(a)** Find $\\sin 2\\theta$ and $\\cos 2\\theta$. **[4]**  \n"
                "**(b)** Hence find $\\tan 2\\theta$. **[2]**"
            ),
            "solution": (
                "$\\theta$ obtuse means $\\sin\\theta > 0$, so $\\sin\\theta = \\frac{4}{5}$ "
                "*(A1)*.  \n"
                "**(a)** $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta = 2\\left(\\frac{4}{5}\\right)"
                "\\left(-\\frac{3}{5}\\right) = -\\frac{24}{25}$ *(M1 A1)*;  \n"
                "$\\cos 2\\theta = 2\\cos^2\\theta - 1 = 2\\left(\\frac{9}{25}\\right) - 1 = "
                "-\\frac{7}{25}$ *(A1)*.  \n"
                "**(b)** $$\\tan 2\\theta = \\frac{-24/25}{-7/25} = \\frac{24}{7}. \\;(M1\\,A1)$$  \n"
                "Both doubles are negative, so $2\\theta$ sits in the third quadrant — consistent "
                "with $\\theta$ between $90^\\circ$ and $180^\\circ$, and it is why "
                "$\\tan 2\\theta$ comes out positive."
            ),
            "badges": code_badge("ib-aa-hl-3.10", 6, "P1"),
            "check": [
                "Eq(Rational(-3,5)**2 + Rational(4,5)**2, 1)",
                "Eq(2*Rational(4,5)*Rational(-3,5), Rational(-24,25))",
                "Eq(2*Rational(-3,5)**2 - 1, Rational(-7,25))",
                "Eq(Rational(-24,25)/Rational(-7,25), Rational(24,7))",
                "Eq(Rational(-24,25)**2 + Rational(-7,25)**2, 1)",
            ],
        },
        {
            "id": "ibhl-gt-q02",
            "statement": (
                "Solve $\\sqrt3\\,\\tan 2x = 1$ for $0 \\le x < \\pi$. **[5]**"
            ),
            "solution": (
                "Isolate the ratio *(M1)*: $\\tan 2x = \\frac{1}{\\sqrt3}$.  \n"
                "Let $u = 2x$; as $x$ runs over $[0, \\pi)$, $u$ runs over $[0, 2\\pi)$ "
                "*(A1)*.  \n"
                "The principal value is $u = \\frac{\\pi}{6}$, and tangent's partner is "
                "$u + \\pi = \\frac{7\\pi}{6}$ — tangent repeats every $\\pi$, not every $2\\pi$ "
                "*(A1)*.  \n"
                "$$u = \\frac{\\pi}{6}, \\;\\frac{7\\pi}{6} \\;\\Longrightarrow\\; "
                "x = \\frac{\\pi}{12}, \\;\\frac{7\\pi}{12}. \\;(A1\\,A1)$$  \n"
                "Using $2\\pi$ as tangent's period would have produced only one solution and cost "
                "two marks."
            ),
            "badges": code_badge("ib-aa-hl-3.11", 5, "P1"),
            "check": [
                "Eq(sqrt(3)*tan(2*(pi/12)), 1)",
                "Eq(sqrt(3)*tan(2*(7*pi/12)), 1)",
                "Eq(tan(pi/6), sqrt(3)/3)",
                "Eq(simplify(tan(x + pi) - tan(x)), 0)",
                "(7*pi/12) < pi",
            ],
        },
        {
            "id": "ibhl-gt-q03",
            "statement": (
                "Points $A$, $B$ and $C$ have coordinates $A(2, -1, 4)$, $B(5, 1, -2)$ and "
                "$C(0, 3, 1)$.  \n"
                "**(a)** Find $\\overrightarrow{AB}$ and $\\overrightarrow{AC}$. **[2]**  \n"
                "**(b)** Find the size of $\\widehat{BAC}$, correct to 3 significant figures. "
                "**[5]**"
            ),
            "solution": (
                "**(a)** *(A1 A1)* $\\overrightarrow{AB} = \\begin{pmatrix} 3 \\\\ 2 \\\\ -6 "
                "\\end{pmatrix}$, $\\overrightarrow{AC} = \\begin{pmatrix} -2 \\\\ 4 \\\\ -3 "
                "\\end{pmatrix}$.  \n"
                "**(b)** Both vectors must start at the VERTEX $A$ — that is what makes the "
                "scalar product measure the angle at $A$ *(M1)*.  \n"
                "$$\\overrightarrow{AB}\\cdot\\overrightarrow{AC} = -6 + 8 + 18 = 20 \\;(A1)$$  \n"
                "$$\\left|\\overrightarrow{AB}\\right| = \\sqrt{9 + 4 + 36} = 7, \\qquad "
                "\\left|\\overrightarrow{AC}\\right| = \\sqrt{4 + 16 + 9} = \\sqrt{29} \\;(A1)$$  \n"
                "$$\\cos\\widehat{BAC} = \\frac{20}{7\\sqrt{29}} \\approx 0.53056 \\;(A1) "
                "\\;\\Longrightarrow\\; \\widehat{BAC} = 58.0^\\circ \\;(3\\text{ s.f.}). "
                "\\;(A1)$$  \n"
                "Using $\\overrightarrow{BA}$ instead of $\\overrightarrow{AB}$ would flip the "
                "sign and return the supplement, $122^\\circ$ — the standard error on this "
                "archetype."
            ),
            "badges": code_badge("ib-aa-hl-3.13", 7, "P2"),
            "check": [
                "Eq(Matrix([5,1,-2]) - Matrix([2,-1,4]), Matrix([3,2,-6]))",
                "Eq(Matrix([0,3,1]) - Matrix([2,-1,4]), Matrix([-2,4,-3]))",
                "Eq(Matrix([3,2,-6]).dot(Matrix([-2,4,-3])), 20)",
                "Eq(Matrix([3,2,-6]).norm(), 7)",
                "Eq(Matrix([-2,4,-3]).norm(), sqrt(29))",
                "Abs(deg(acos(20/(7*sqrt(29)))) - 57.9568) < Rational(1,100)",
            ],
        },
        {
            "id": "ibhl-gt-q04",
            "statement": (
                "$L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix} + "
                "\\lambda\\begin{pmatrix} 3 \\\\ 1 \\\\ -1 \\end{pmatrix}$ and "
                "$L_2: \\mathbf{r} = \\begin{pmatrix} 4 \\\\ 0 \\\\ 1 \\end{pmatrix} + "
                "\\mu\\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$.  \n"
                "**(a)** Show that the lines intersect and find the point of intersection. "
                "**[6]**  \n"
                "**(b)** Find the acute angle between the lines, to 3 significant figures. "
                "**[4]**"
            ),
            "solution": (
                "**(a)** The directions are not proportional ($\\frac{3}{1} \\ne \\frac{1}{2}$), "
                "so the lines are not parallel *(R1)*. Equating gives *(M1)*  \n"
                "$$1 + 3\\lambda = 4 + \\mu, \\qquad -1 + \\lambda = 2\\mu, \\qquad "
                "2 - \\lambda = 1 + 3\\mu.$$  \n"
                "From the second, $\\mu = \\frac{\\lambda - 1}{2}$. Substituting into the first "
                "*(M1)*: $2 + 6\\lambda = 8 + \\lambda - 1$, so $5\\lambda = 5$ and $\\lambda = "
                "1$, $\\mu = 0$ *(A1)*.  \n"
                "Third equation *(M1)*: $2 - 1 = 1$ and $1 + 0 = 1$ ✓ — consistent, so they "
                "intersect *(A1)*, at  \n"
                "$$\\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix} + \\begin{pmatrix} 3 \\\\ 1 "
                "\\\\ -1 \\end{pmatrix} = (4, 0, 1).$$  \n"
                "**(b)** $\\mathbf{b}_1\\cdot\\mathbf{b}_2 = 3 + 2 - 3 = 2$ *(M1 A1)*, with "
                "$|\\mathbf{b}_1| = \\sqrt{11}$ and $|\\mathbf{b}_2| = \\sqrt{14}$ *(A1)*:  \n"
                "$$\\cos\\theta = \\frac{2}{\\sqrt{154}} \\approx 0.16116 \\;\\Longrightarrow\\; "
                "\\theta = 80.7^\\circ. \\;(A1)$$  \n"
                "$\\mu = 0$ means the intersection is $L_2$'s own base point — a nice consistency "
                "check, since $(4, 0, 1)$ is exactly the vector written in $L_2$'s equation."
            ),
            "badges": code_badge("ib-aa-hl-3.15", 10, "P2"),
            "check": [
                "Eq(Matrix([1,-1,2]) + 1*Matrix([3,1,-1]), Matrix([4,0,1]))",
                "Eq(Matrix([4,0,1]) + 0*Matrix([1,2,3]), Matrix([4,0,1]))",
                "Eq(2 - 1, 1 + 3*0)",
                "Eq(Matrix([3,1,-1]).dot(Matrix([1,2,3])), 2)",
                "Eq(Matrix([3,1,-1]).norm(), sqrt(11))",
                "Eq(Matrix([1,2,3]).norm(), sqrt(14))",
                "Abs(deg(acos(2/sqrt(154))) - 80.7255) < Rational(1,100)",
            ],
        },
        {
            "id": "ibhl-gt-q05",
            "statement": (
                "The plane $\\Pi$ passes through $P(1, 2, 0)$, $Q(3, 1, 2)$ and $R(2, 4, 3)$.  \n"
                "**(a)** Find $\\overrightarrow{PQ} \\times \\overrightarrow{PR}$. **[4]**  \n"
                "**(b)** Hence find the Cartesian equation of $\\Pi$. **[3]**  \n"
                "**(c)** Find the exact area of triangle $PQR$. **[3]**"
            ),
            "solution": (
                "**(a)** $\\overrightarrow{PQ} = (2, -1, 2)$ and $\\overrightarrow{PR} = "
                "(1, 2, 3)$ *(A1)*. Then *(M1)*  \n"
                "$$\\mathbf{i}: (-1)(3) - (2)(2) = -7, \\quad \\mathbf{j}: (2)(1) - (2)(3) = -4, "
                "\\quad \\mathbf{k}: (2)(2) - (-1)(1) = 5$$  \n"
                "$$\\overrightarrow{PQ} \\times \\overrightarrow{PR} = \\begin{pmatrix} -7 \\\\ "
                "-4 \\\\ 5 \\end{pmatrix}. \\;(A1\\,A1)$$  \n"
                "**(b)** Use $\\mathbf{n} = (7, 4, -5)$, the negative — either is normal, and this "
                "one keeps the leading coefficient positive *(M1)*. With $P$: $d = 7 + 8 - 0 = "
                "15$ *(A1)*.  \n"
                "$$\\Pi: \\; 7x + 4y - 5z = 15. \\;(A1)$$  \n"
                "Check $Q$: $21 + 4 - 10 = 15$ ✓; $R$: $14 + 16 - 15 = 15$ ✓.  \n"
                "**(c)** $\\left|\\overrightarrow{PQ} \\times \\overrightarrow{PR}\\right| = "
                "\\sqrt{49 + 16 + 25} = \\sqrt{90} = 3\\sqrt{10}$ *(M1 A1)*, so  \n"
                "$$\\text{Area} = \\frac{3\\sqrt{10}}{2}. \\;(A1)$$  \n"
                "One vector product, and it answered both the plane and the area — which is why "
                "parts (a)-(c) are so often bundled into a single Section B question."
            ),
            "badges": code_badge("ib-aa-hl-3.17", 10, "P1"),
            "check": [
                "Eq(Matrix([3,1,2]) - Matrix([1,2,0]), Matrix([2,-1,2]))",
                "Eq(Matrix([2,4,3]) - Matrix([1,2,0]), Matrix([1,2,3]))",
                "Eq(Matrix([2,-1,2]).cross(Matrix([1,2,3])), Matrix([-7,-4,5]))",
                "Eq(Matrix([7,4,-5]).dot(Matrix([1,2,0])), 15)",
                "Eq(Matrix([7,4,-5]).dot(Matrix([3,1,2])), 15)",
                "Eq(Matrix([7,4,-5]).dot(Matrix([2,4,3])), 15)",
                "Eq(Matrix([-7,-4,5]).norm(), 3*sqrt(10))",
            ],
        },
        {
            "id": "ibhl-gt-q06",
            "statement": (
                "The plane $\\Pi_1$ has equation $2x - y + z = 4$.  \n"
                "**(a)** Find the acute angle between $\\Pi_1$ and the plane $x + y - 2z = 3$, "
                "to 3 significant figures. **[4]**  \n"
                "**(b)** Find the angle between $\\Pi_1$ and the line $\\mathbf{r} = "
                "\\begin{pmatrix} 0 \\\\ 1 \\\\ 2 \\end{pmatrix} + \\lambda\\begin{pmatrix} 1 "
                "\\\\ -1 \\\\ 1 \\end{pmatrix}$, to 3 significant figures. **[4]**"
            ),
            "solution": (
                "**(a)** Normals read off the coefficients: $\\mathbf{n}_1 = (2, -1, 1)$ and "
                "$\\mathbf{n}_2 = (1, 1, -2)$ *(A1)*. Plane to plane uses COSINE *(M1)*:  \n"
                "$$\\mathbf{n}_1\\cdot\\mathbf{n}_2 = 2 - 1 - 2 = -1, \\qquad |\\mathbf{n}_1| = "
                "|\\mathbf{n}_2| = \\sqrt6 \\;(A1)$$  \n"
                "$$\\cos\\theta = \\frac{|-1|}{6} = \\frac{1}{6} \\;\\Longrightarrow\\; "
                "\\theta = 80.4^\\circ. \\;(A1)$$  \n"
                "**(b)** Line to plane uses SINE, because the formula measures against the NORMAL "
                "*(M1)*:  \n"
                "$$\\mathbf{d}\\cdot\\mathbf{n}_1 = 2 + 1 + 1 = 4, \\qquad |\\mathbf{d}| = "
                "\\sqrt3, \\quad |\\mathbf{n}_1| = \\sqrt6 \\;(A1)$$  \n"
                "$$\\sin\\theta = \\frac{4}{\\sqrt{18}} = \\frac{4}{3\\sqrt2} \\approx 0.94281 "
                "\\;(A1) \\;\\Longrightarrow\\; \\theta = 70.5^\\circ. \\;(A1)$$  \n"
                "Had part (b) used cosine, the answer would have been $19.5^\\circ$ — the "
                "complement. The two parts are deliberately adjacent to test exactly that "
                "distinction."
            ),
            "badges": code_badge("ib-aa-hl-3.18", 8, "P2"),
            "check": [
                "Eq(Matrix([2,-1,1]).dot(Matrix([1,1,-2])), -1)",
                "Eq(Matrix([2,-1,1]).norm(), sqrt(6))",
                "Eq(Matrix([1,1,-2]).norm(), sqrt(6))",
                "Abs(deg(acos(Rational(1,6))) - 80.4059) < Rational(1,100)",
                "Eq(Matrix([1,-1,1]).dot(Matrix([2,-1,1])), 4)",
                "Eq(Matrix([1,-1,1]).norm(), sqrt(3))",
                "Abs(deg(asin(4/sqrt(18))) - 70.5288) < Rational(1,100)",
                "Abs(deg(asin(4/sqrt(18))) + deg(acos(4/sqrt(18))) - 90) < Rational(1,1000000)",
            ],
        },
    ]


# <<LESSONS_TAIL>>


# ===========================================================================
def build():
    lessons = [
        lesson_reciprocal_inverse(),
        lesson_compound_angles(),
        lesson_trig_symmetry(),
        lesson_vectors_components(),
        lesson_scalar_product(),
        lesson_vector_lines(),
        lesson_line_relationships(),
        lesson_vector_product(),
        lesson_planes(),
    ]
    unit = {
        "slug": "geometry-and-trigonometry",
        "title": "Geometry & Trigonometry (AHL)",
        "unit": 3,
        "status": "published",
        "blurb": (
            "The HL extension of Topic 3, complete: the reciprocal ratios sec, csc and cot with "
            "their two Pythagorean identities, the inverse trigonometric functions and their "
            "restricted ranges, compound and double angle identities, the symmetry relationships "
            "that turn one solution into all of them, and then the entire vector toolkit — "
            "components and magnitude, the scalar product, vector equations of lines, the "
            "parallel/intersecting/skew classification, the vector product with its areas, and "
            "planes with their intersections and angles. Every subtopic code from AHL 3.9 to "
            "AHL 3.18."
        ),
        "buildsOn": (
            "SL Topic 3 end to end — the unit circle, exact values, the Pythagorean identity, the "
            "sine and cosine rules, and 3D distances in a solid. HL adds a second dimension of "
            "machinery: identities that manipulate angles algebraically, and vectors that handle "
            "3D geometry without a single diagram."
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
        assert les.get("concreteComparison", "").strip(), f"{les['slug']}: empty concreteComparison"
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
