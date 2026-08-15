#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 5: Decimals — First Steps.

Tenths and hundredths as the place-value ladder continuing RIGHT of the
ones, decimals as fractions in disguise (and back), comparing without
falling for "longer is bigger", adding and subtracting by lining up the
POINT, and rounding/measuring with decimals.

Through-line: THE LADDER KEEPS GOING. Topic 1 built places climbing
left by tens; the decimal point just marks where the ones stand, and
the same ladder descends to the right — tenths, hundredths — dividing
by ten per step. Nothing about decimals is new; it is place value with
the staircase extended.

Checks discipline: decimal literals NEVER appear in checks — 0.35 is
not exactly representable in binary floats and a check like
Eq(0.35, 35/100) can silently fail. Every check uses exact Rational
arithmetic; statements render decimals, checks verify their fraction
identities.

Run: python3 scripts/grade4/build_decimals.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (C_ACCENT, C_GREEN, C_NEUTRAL, C_WARM, withfig,  # noqa: E402
                     fig_numline,
                     funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic)


# ==========================================================================
# Lesson 1 — Tenths & Hundredths
# ==========================================================================

def lesson_tenths():
    return {
        "slug": "tenths-and-hundredths",
        "title": "Tenths & Hundredths",
        "concreteComparison": (
            "Your height is $1.35$ metres: one whole metre, then $3$ "
            "tenths of a metre, then $5$ hundredths. The place-value "
            "ladder you built in Topic 1 climbed LEFT by tens — the "
            "decimal point simply marks where the ones stand, and the "
            "same ladder keeps going RIGHT, dividing by ten at every "
            "step. Decimals are not a new kind of number; they are the "
            "staircase, extended."),
        "objective": (
            "Read and write tenths and hundredths, name the value of "
            "each decimal digit, and tell 0.5 from 0.05 — the zero that "
            "holds a decimal place."),
        "concept": [
            "**The ladder continues.** Left of the point, each step "
            "multiplies by ten: ones, tens, hundreds. Right of the "
            "point, each step DIVIDES by ten: tenths "
            "($\\frac{1}{10}$), hundredths ($\\frac{1}{100}$). The "
            "point itself marks where the ones column stands.",
            "**Reading a decimal is reading places.** $1.35$ is $1$ "
            "whole $+ 3$ tenths $+ 5$ hundredths — that is $1 + "
            "\\frac{3}{10} + \\frac{5}{100} = \\frac{135}{100}$. Every "
            "digit's value is digit × place, exactly as before.",
            "**Zeros hold decimal places too.** $0.5$ is five TENTHS; "
            "$0.05$ is five HUNDREDTHS — ten times smaller, because "
            "the zero pushed the $5$ one place down the ladder. Right "
            "of the point, a zero between the point and a digit "
            "matters enormously.",
        ],
        "keyIdea": (
            "The decimal point marks the ones; the place-value ladder "
            "continues right of it, dividing by ten per step — tenths, "
            "then hundredths. Digit × place still tells the value."),
        "facts": [
            {"title": "The ladder, extended",
             "latex": "\\ldots\\ 100 \\ \\ 10 \\ \\ 1 \\ . \\ \\tfrac{1}{10} \\ \\ \\tfrac{1}{100}\\ \\ldots",
             "explanation": "Same staircase, same factor of ten — now descending to the right."},
            {"title": "Reading 1.35",
             "latex": "1.35 = 1 + \\tfrac{3}{10} + \\tfrac{5}{100} = \\tfrac{135}{100}",
             "explanation": "One whole, three tenths, five hundredths — digit times place, added."},
        ],
        "workedExamples": [
            {"id": "g5dc-l1-we1",
             "statement": "Break $1.35$ into wholes, tenths and hundredths, and write it as a single fraction.",
             "note": "Digit × place, then add.",
             "solution": ("$1.35 = 1 + \\frac{3}{10} + \\frac{5}{100}$. In "
                          "hundredths: $\\frac{100}{100} + \\frac{30}{100} + "
                          "\\frac{5}{100} = \\frac{135}{100}$ — one hundred "
                          "thirty-five hundredths."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1 + Rational(3,10) + Rational(5,100), Rational(135,100))"]},
            {"id": "g5dc-l1-we2",
             "statement": "Compare the values of the $5$ in $0.5$ and in $0.05$.",
             "note": "One place apart on the ladder.",
             "solution": ("$0.5$ is five tenths ($\\frac{5}{10}$); $0.05$ is five "
                          "hundredths ($\\frac{5}{100}$). One step down the ladder "
                          "divides by ten: $\\frac{5}{10} = 10 \\times "
                          "\\frac{5}{100}$ — the first is ten times the second."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(5,10), 10*Rational(5,100))"]},
        ],
        "commonMistakes": [
            {"text": "Reading 0.35 as \"thirty-five\" — ignoring the point.",
             "correction": "The point marks where wholes end: 0.35 is thirty-five HUNDREDTHS — less than one. Say the place name out loud when you read.",
             "authored": True},
            {"text": "Treating 0.5 and 0.05 as the same number.",
             "correction": "The zero after the point pushes the 5 a full step down the ladder: 0.5 = 5/10 while 0.05 = 5/100 — ten times smaller.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5dc-l1-t1",
             "statement": "Write $2.07$ as wholes + tenths + hundredths, and as a single fraction.",
             "solution": "$2 + \\frac{0}{10} + \\frac{7}{100} = \\frac{207}{100}$ — the zero tenths add nothing but hold the place.",
             "check": ["Eq(2 + Rational(7,100), Rational(207,100))"]},
            {"id": "g5dc-l1-t2",
             "statement": "What is the value of the digit $8$ in $3.82$? And in $3.08$?",
             "solution": "In $3.82$: eight tenths, $\\frac{8}{10}$. In $3.08$: eight hundredths, $\\frac{8}{100}$ — ten times smaller.",
             "check": ["Eq(Rational(8,10), 10*Rational(8,100))"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The staircase keeps going", [
                "Topic 1's ladder climbed LEFT by tens: ones, tens, hundreds. The decimal point marks where the ones stand — and the ladder continues RIGHT, dividing by ten per step: tenths, hundredths.",
                "$1.35$: one whole, $3$ tenths, $5$ hundredths — $1 + \\frac{3}{10} + \\frac{5}{100} = \\frac{135}{100}$.",
                "Digit × place still gives the value; nothing about the rule changed, only the direction of travel.",
            ]), {"mode": "decimalGrid", "decimal": {"value": 0.37, "label": "0.37 of one whole"}}),
            workedset("Reading the places",
                      "Name each digit's place; add the values.", [
                wex("Break $1.35$ into place values.",
                    ["$1$ whole, $3$ tenths, $5$ hundredths.",
                     "$1 + \\frac{3}{10} + \\frac{5}{100} = \\frac{135}{100}$."],
                    "$\\frac{135}{100}$",
                    ["Eq(1 + Rational(3,10) + Rational(5,100), Rational(135,100))"]),
                wex("Break $2.07$ into place values.",
                    ["$2$ wholes, $0$ tenths, $7$ hundredths — the zero holds its post.",
                     "$2 + \\frac{7}{100} = \\frac{207}{100}$."],
                    "$\\frac{207}{100}$",
                    ["Eq(2 + Rational(7,100), Rational(207,100))"]),
            ]),
            tryitset("Digit values", "Say the place name before the value.", [
                tp("The value of the $6$ in $4.63$ is:",
                   ["six tenths — $\\frac{6}{10}$", "six hundredths — $\\frac{6}{100}$", "six wholes"],
                   "First place right of the point: tenths. $4.63 = 4 + \\frac{6}{10} + \\frac{3}{100}$.",
                   ["Eq(4 + Rational(6,10) + Rational(3,100), Rational(463,100))"]),
                tp("$0.09$ means:",
                   ["nine hundredths", "nine tenths", "nine wholes"],
                   "The zero holds the tenths, pushing the $9$ to the hundredths: $\\frac{9}{100}$.",
                   ["Eq(Rational(9,10), 10*Rational(9,100))"]),
                tp("Which number is ten times $0.04$?",
                   ["$0.4$", "$0.004$", "$4$"],
                   "One step UP the ladder: $10 \\times \\frac{4}{100} = \\frac{4}{10}$, written $0.4$.",
                   ["Eq(10*Rational(4,100), Rational(4,10))"]),
            ]),
            tapq("Point of reference", "In $27.4$, the decimal point tells you that:",
                 ["the $7$ is the ones digit and the $4$ is tenths",
                  "the $4$ is the ones digit",
                  "the number is less than one",
                  "the $2$ is the ones digit"],
                 "The point sits just right of the ones: $27.4$ is $2$ tens, $7$ ones, $4$ tenths — $27 + \\frac{4}{10}$.",
                 ["Eq(27 + Rational(4,10), Rational(274,10))"]),
            funfact("The point that wanders the world",
                    "Mongolia and most of Europe write the decimal separator as a comma — $1{,}35$ — while English-language mathematics uses the point. Same ladder, different ink. On this site we write the point, because that's what calculators and programming languages the world over use."),
            withfig(teach("Concept B", "Zeros on the decimal side", [
                "A zero between the point and a digit pushes that digit down the ladder: $0.5$ is five tenths, $0.05$ five hundredths — ten times smaller.",
                "But a zero at the END changes nothing: $0.5$ and $0.50$ are the same amount ($\\frac{5}{10} = \\frac{50}{100}$) — the ladder just got described one step finer.",
                "The two zero rules — inside matters, trailing doesn't — do all the work in the comparing lesson ahead.",
            ]), {"mode": "decimalGrid", "decimal": {"value": 0.3, "label": "0.3 = 0.30"}}),
            workedset("The two zero rules",
                      "Inside pushes down; trailing changes nothing.", [
                wex("Compare the $5$ in $0.5$ and $0.05$.",
                    ["$\\frac{5}{10}$ against $\\frac{5}{100}$ — one ladder step apart.",
                     "$0.5 = 10 \\times 0.05$."],
                    "ten times",
                    ["Eq(Rational(5,10), 10*Rational(5,100))"]),
                wex("Are $0.7$ and $0.70$ the same?",
                    ["$\\frac{7}{10}$ and $\\frac{70}{100}$ — split every tenth into ten hundredths.",
                     "Same amount, finer description: yes."],
                    "yes — equal",
                    ["Eq(Rational(7,10), Rational(70,100))"]),
            ]),
            tryitset("Zero discipline", "Which zeros matter?", [
                tp("Which equals $0.30$?",
                   ["$0.3$", "$0.03$", "$3$"],
                   "Trailing zero: $\\frac{30}{100} = \\frac{3}{10}$. ($0.03$ is ten times smaller.)",
                   ["Eq(Rational(30,100), Rational(3,10))"]),
                tp("Which is the SMALLEST: $0.2$, $0.02$, $0.22$?",
                   ["$0.02$", "$0.2$", "$0.22$"],
                   "$\\frac{2}{100}$ sits a step below $\\frac{2}{10}$, and $0.22$ tops both.",
                   ["Rational(2,100) < Rational(2,10)", "Rational(2,10) < Rational(22,100)"]),
                tp("$1.05$ metres is:",
                   ["one metre and five hundredths of a metre", "one metre and five tenths", "fifteen metres"],
                   "The zero holds the tenths: $1 + \\frac{5}{100}$ — just over a metre.",
                   ["Eq(1 + Rational(5,100), Rational(105,100))"]),
            ]),
            tapq("Ladder steps", "How many times bigger is the $3$ in $0.3$ than the $3$ in $0.003$?",
                 ["$100$ times", "$10$ times", "$1\\,000$ times", "the same"],
                 "Tenths against thousandths: two ladder steps, $10 \\times 10 = 100$.",
                 ["Eq(Rational(3,10), 100*Rational(3,1000))"]),
            recap([
                "The point marks the ones; the ladder continues right, dividing by ten per step.",
                "Digit × place gives the value — tenths first, hundredths next.",
                "A zero between point and digit pushes it down the ladder (0.05 vs 0.5).",
                "A trailing zero changes nothing (0.5 = 0.50).",
            ]),
            tip("For every number below, say each digit's PLACE aloud before its value — tenths and hundredths must become as automatic as tens and hundreds."),
            tryitset("Mixed practice", "Places, values, and the two zero rules.", [
                tp("$5.06$ as a single fraction is:",
                   ["$\\frac{506}{100}$", "$\\frac{56}{100}$", "$\\frac{506}{10}$"],
                   "$5 + \\frac{6}{100} = \\frac{506}{100}$ — the zero tenths hold their place.",
                   ["Eq(5 + Rational(6,100), Rational(506,100))"]),
                tp("Ten times $0.07$ is:",
                   ["$0.7$", "$0.007$", "$7$"],
                   "One step up: $\\frac{7}{100} \\to \\frac{7}{10}$.",
                   ["Eq(10*Rational(7,100), Rational(7,10))"]),
                tp("Which pair are EQUAL?",
                   ["$0.9$ and $0.90$", "$0.9$ and $0.09$", "$0.90$ and $0.09$"],
                   "Trailing zero: $\\frac{9}{10} = \\frac{90}{100}$. The inside zero of $0.09$ is a different number entirely.",
                   ["Eq(Rational(9,10), Rational(90,100))", "Rational(9,100) < Rational(9,10)"]),
                tp("A runner's time is $9.58$ seconds. The $5$ is worth:",
                   ["five tenths of a second", "five seconds", "five hundredths of a second"],
                   "First place right of the point: $\\frac{5}{10}$ of a second.",
                   ["Eq(9 + Rational(5,10) + Rational(8,100), Rational(958,100))"]),
                tp("$0.4 + 0.06 + 3$ written as one decimal is:",
                   ["$3.46$", "$3.10$", "$0.463$"],
                   "Three wholes, four tenths, six hundredths: $3.46$.",
                   ["Eq(3 + Rational(4,10) + Rational(6,100), Rational(346,100))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tenths & Hundredths\"",
                    "The staircase now runs in both directions, and you can name any digit's worth on it. Next: the secret that decimals and fractions are the same numbers wearing different clothes.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Decimals & Fractions
# ==========================================================================

def lesson_conversion():
    return {
        "slug": "decimals-and-fractions",
        "title": "Decimals & Fractions",
        "concreteComparison": (
            "$0.25$ and $\\frac{1}{4}$ look nothing alike — yet both "
            "name a quarter. A decimal is just a fraction whose "
            "denominator is $10$ or $100$, written on the place-value "
            "staircase instead of with a bar. Every decimal is a "
            "fraction in disguise, and (for tenths and hundredths) "
            "every fraction can dress as a decimal."),
        "objective": (
            "Convert decimals to fractions and back, using equivalent "
            "fractions to reach denominators of 10 or 100, and simplify "
            "the results."),
        "concept": [
            "**Decimal → fraction: read the last place.** $0.7$ ends in "
            "the tenths: $\\frac{7}{10}$. $0.25$ ends in the "
            "hundredths: $\\frac{25}{100}$ — then simplify: "
            "$\\frac{1}{4}$. The place name IS the denominator.",
            "**Fraction → decimal: rename to tenths or hundredths.** "
            "$\\frac{3}{5}$: multiply top and bottom by $2$ — "
            "$\\frac{6}{10} = 0.6$. $\\frac{3}{4}$: by $25$ — "
            "$\\frac{75}{100} = 0.75$. Equivalent fractions (Topic 4's "
            "splitting move) are the bridge.",
            "**Mixed numbers ride along.** $2\\frac{3}{10} = 2.3$; and "
            "$1.75 = 1\\frac{75}{100} = 1\\frac{3}{4}$. Wholes stay "
            "wholes; only the fraction part changes clothes.",
        ],
        "keyIdea": (
            "The last decimal place names the denominator (tenths or "
            "hundredths); equivalent fractions carry any friendly "
            "fraction onto the staircase and back."),
        "facts": [
            {"title": "Decimal to fraction",
             "latex": "0.25 = \\tfrac{25}{100} = \\tfrac{1}{4}",
             "explanation": "The last place is the denominator; then simplify."},
            {"title": "Fraction to decimal",
             "latex": "\\tfrac{3}{5} = \\tfrac{6}{10} = 0.6",
             "explanation": "Rename to tenths or hundredths with the splitting move; read it off."},
        ],
        "workedExamples": [
            {"id": "g5dc-l2-we1",
             "statement": "Write $0.25$ and $0.6$ as fractions in simplest form.",
             "note": "Last place → denominator; then merge.",
             "solution": ("$0.25$: hundredths — $\\frac{25}{100}$, which merges by "
                          "$25$ to $\\frac{1}{4}$. $0.6$: tenths — $\\frac{6}{10} = "
                          "\\frac{3}{5}$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(25,100), Rational(1,4))",
                       "Eq(Rational(6,10), Rational(3,5))"]},
            {"id": "g5dc-l2-we2",
             "statement": "Write $\\frac{3}{4}$ and $\\frac{7}{20}$ as decimals.",
             "note": "Rename to hundredths.",
             "solution": ("$\\frac{3}{4} = \\frac{75}{100} = 0.75$ (times $25$). "
                          "$\\frac{7}{20} = \\frac{35}{100} = 0.35$ (times $5$)."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(3,4), Rational(75,100))",
                       "Eq(Rational(7,20), Rational(35,100))"]},
        ],
        "commonMistakes": [
            {"text": "Writing 0.7 as 7/100 — grabbing the wrong denominator.",
             "correction": "The LAST place names the denominator. 0.7 ends in the tenths: 7/10. Only two decimal places reach the hundredths.",
             "authored": True},
            {"text": "Turning 1/4 into 0.14 — writing the fraction's digits into decimal places.",
             "correction": "Digits don't transfer; AMOUNTS do. Rename first: 1/4 = 25/100 = 0.25. (0.14 would be 14/100 = 7/50 — a different number.)",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5dc-l2-t1",
             "statement": "Write $0.85$ as a fraction in simplest form.",
             "solution": "$\\frac{85}{100}$, merged by $5$: $\\frac{17}{20}$.",
             "check": ["Eq(Rational(85,100), Rational(17,20))"]},
            {"id": "g5dc-l2-t2",
             "statement": "Write $\\frac{9}{25}$ as a decimal.",
             "solution": "Times $4$: $\\frac{36}{100} = 0.36$.",
             "check": ["Eq(Rational(9,25), Rational(36,100))"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Decimals undress to fractions", [
                "Read the LAST place: that's the denominator. $0.7$ ends in tenths — $\\frac{7}{10}$; $0.25$ ends in hundredths — $\\frac{25}{100}$.",
                "Then Topic 4 takes over: simplify. $\\frac{25}{100} = \\frac{1}{4}$.",
                "So $0.25$ and a quarter were the same amount all along — the decimal was a fraction on the staircase.",
            ]), {"mode": "decimalGrid", "decimal": {"value": 0.6, "label": "0.6 = 6/10"}}),
            workedset("Decimal to fraction",
                      "Last place names the denominator; then merge.", [
                wex("Convert $0.25$ and $0.6$.",
                    ["$0.25 \\to \\frac{25}{100} \\to \\frac{1}{4}$.",
                     "$0.6 \\to \\frac{6}{10} \\to \\frac{3}{5}$."],
                    "$\\frac{1}{4}$ and $\\frac{3}{5}$",
                    ["Eq(Rational(25,100), Rational(1,4))", "Eq(Rational(6,10), Rational(3,5))"]),
                wex("Convert $1.75$ to a mixed number.",
                    ["The whole stays: $1$. The decimal part: $\\frac{75}{100} = \\frac{3}{4}$.",
                     "$1.75 = 1\\frac{3}{4}$."],
                    "$1\\frac{3}{4}$",
                    ["Eq(1 + Rational(75,100), 1 + Rational(3,4))"]),
            ]),
            tryitset("Undress the decimal", "Denominator from the last place; simplest form to finish.", [
                tp("$0.85$ in simplest form is:",
                   ["$\\frac{17}{20}$", "$\\frac{85}{100}$ and stop", "$\\frac{8}{5}$"],
                   "$\\frac{85}{100}$ merges by $5$: $\\frac{17}{20}$.",
                   ["Eq(Rational(85,100), Rational(17,20))"]),
                tp("$0.5$ as a fraction is:",
                   ["$\\frac{1}{2}$", "$\\frac{1}{5}$", "$\\frac{5}{100}$"],
                   "Five tenths: $\\frac{5}{10} = \\frac{1}{2}$.",
                   ["Eq(Rational(5,10), Rational(1,2))"]),
                tp("$0.04$ as a fraction is:",
                   ["$\\frac{1}{25}$", "$\\frac{2}{5}$", "$\\frac{4}{10}$"],
                   "Four hundredths: $\\frac{4}{100} = \\frac{1}{25}$. ($\\frac{4}{10}$ would be $0.4$.)",
                   ["Eq(Rational(4,100), Rational(1,25))"]),
            ]),
            tapq("Which denominator?", "$0.9$ undresses to:",
                 ["$\\frac{9}{10}$ — it ends in the tenths",
                  "$\\frac{9}{100}$ — decimals mean hundredths",
                  "$\\frac{9}{1}$",
                  "$\\frac{90}{10}$"],
                 "One decimal place = tenths. ($\\frac{9}{100}$ would be $0.09$ — the inside-zero number.)",
                 ["Eq(Rational(9,10), Rational(90,100))"]),
            funfact("Batting averages and shooting percentages",
                    "Sports statistics are this lesson at work: a basketball player who makes $\\frac{3}{4}$ of free throws \"shoots 0.750\" — three quarters renamed to thousandths. Every sports page is a fraction-to-decimal conversion table."),
            withfig(teach("Concept B", "Fractions dress as decimals", [
                "To put a fraction on the staircase, rename it to tenths or hundredths with the splitting move: $\\frac{3}{5} = \\frac{6}{10} = 0.6$.",
                "Denominators that divide $100$ — halves, quarters, fifths, tenths, twentieths, twenty-fifths, fiftieths — all reach the staircase: $\\frac{3}{4} = \\frac{75}{100} = 0.75$.",
                "Digits never transfer directly — AMOUNTS do. $\\frac{1}{4}$ is not $0.14$; rename first, then read.",
            ]), {"mode": "decimalGrid", "decimal": {"value": 0.14, "label": "14/100 = 0.14"}}),
            workedset("Fraction to decimal",
                      "Split to tenths or hundredths; read the staircase.", [
                wex("Convert $\\frac{3}{4}$ and $\\frac{7}{20}$.",
                    ["$\\frac{3}{4} \\times \\frac{25}{25} = \\frac{75}{100} = 0.75$.",
                     "$\\frac{7}{20} \\times \\frac{5}{5} = \\frac{35}{100} = 0.35$."],
                    "$0.75$ and $0.35$",
                    ["Eq(Rational(3,4), Rational(75,100))", "Eq(Rational(7,20), Rational(35,100))"]),
                wex("Convert $2\\frac{2}{5}$ to a decimal.",
                    ["The whole rides along; $\\frac{2}{5} = \\frac{4}{10} = 0.4$.",
                     "$2\\frac{2}{5} = 2.4$."],
                    "$2.4$",
                    ["Eq(2 + Rational(2,5), Rational(24,10))"]),
            ]),
            tryitset("Dress the fraction", "Find the multiplier to 10 or 100.", [
                tp("$\\frac{9}{25}$ as a decimal is:",
                   ["$0.36$", "$0.925$", "$0.9$"],
                   "Times $4$: $\\frac{36}{100} = 0.36$.",
                   ["Eq(Rational(9,25), Rational(36,100))"]),
                tp("$\\frac{1}{2}$ as a decimal is:",
                   ["$0.5$", "$0.12$", "$0.2$"],
                   "$\\frac{5}{10}$: $0.5$. (Writing the digits — $0.12$ — is the classic transfer error.)",
                   ["Eq(Rational(1,2), Rational(5,10))"]),
                tp("$\\frac{19}{50}$ as a decimal is:",
                   ["$0.38$", "$0.19$", "$0.95$"],
                   "Times $2$: $\\frac{38}{100} = 0.38$.",
                   ["Eq(Rational(19,50), Rational(38,100))"]),
            ]),
            tapq("The transfer trap", "A student writes $\\frac{1}{4} = 0.14$. The truth:",
                 ["$\\frac{1}{4} = \\frac{25}{100} = 0.25$ — rename amounts, don't copy digits",
                  "the student is right",
                  "$\\frac{1}{4} = 0.4$",
                  "quarters have no decimal"],
                 "$0.14$ is $\\frac{14}{100} = \\frac{7}{50}$ — a different number. The bridge is the equivalent fraction, never the digits.",
                 ["Eq(Rational(1,4), Rational(25,100))", "Eq(Rational(14,100), Rational(7,50))"]),
            recap([
                "Decimal → fraction: the last place names the denominator; then simplify.",
                "Fraction → decimal: rename to tenths or hundredths (splitting move), then read.",
                "Wholes ride along; only the fraction part changes clothes.",
                "Copy amounts, never digits — 1/4 is 0.25, not 0.14.",
            ]),
            tip("Convert each both ways where you can — a fraction that comes back changed caught an error in flight."),
            tryitset("Mixed practice", "Both directions, simplest form throughout.", [
                tp("$0.45$ in simplest form is:",
                   ["$\\frac{9}{20}$", "$\\frac{45}{100}$ and stop", "$\\frac{4}{5}$"],
                   "$\\frac{45}{100}$ merges by $5$: $\\frac{9}{20}$.",
                   ["Eq(Rational(45,100), Rational(9,20))"]),
                tp("$\\frac{4}{5}$ as a decimal is:",
                   ["$0.8$", "$0.45$", "$0.4$"],
                   "$\\frac{8}{10} = 0.8$.",
                   ["Eq(Rational(4,5), Rational(8,10))"]),
                tp("$3.5$ as a mixed number is:",
                   ["$3\\frac{1}{2}$", "$3\\frac{1}{5}$", "$\\frac{35}{100}$"],
                   "$3 + \\frac{5}{10} = 3\\frac{1}{2}$.",
                   ["Eq(3 + Rational(5,10), 3 + Rational(1,2))"]),
                tp("Which decimal equals $\\frac{13}{20}$?",
                   ["$0.65$", "$0.13$", "$0.652$"],
                   "Times $5$: $\\frac{65}{100} = 0.65$.",
                   ["Eq(Rational(13,20), Rational(65,100))"]),
                tp("Which is the odd one out: $0.75$, $\\frac{3}{4}$, $\\frac{75}{100}$, $\\frac{7}{5}$?",
                   ["$\\frac{7}{5}$ — the others all name three quarters", "$0.75$", "$\\frac{75}{100}$"],
                   "$\\frac{7}{5}$ is top-heavy — $1.4$, nearly double the rest.",
                   ["Eq(Rational(3,4), Rational(75,100))", "Eq(Rational(7,5), Rational(14,10))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Decimals & Fractions\"",
                    "Two notations, one number line. From here on you can pick whichever dress suits the work — decimals for measuring and money, fractions for exact shares. Next: putting decimals in order without falling for their favourite trick.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Comparing & Ordering Decimals
# ==========================================================================

def lesson_comparing():
    return {
        "slug": "comparing-and-ordering-decimals",
        "title": "Comparing & Ordering Decimals",
        "concreteComparison": (
            "Two runners clock $0.5$ and $0.47$ — and half the class "
            "declares $0.47$ bigger \"because $47$ beats $5$\". Pad the "
            "shorter one: $0.50$ against $0.47$ — fifty hundredths "
            "against forty-seven. The longer decimal LOOKED bigger and "
            "wasn't. Digits right of the point don't count length; they "
            "count ladder steps."),
        "objective": (
            "Compare and order decimals by aligning places (padding "
            "with trailing zeros), and place decimals between their "
            "neighbours on the number line."),
        "concept": [
            "**Pad, then compare place by place.** Give both numbers "
            "the same number of decimal places using trailing zeros "
            "(which change nothing): $0.5$ vs $0.47$ becomes $0.50$ vs "
            "$0.47$ — now compare like whole numbers of hundredths: "
            "$50 > 47$.",
            "**Longer is NOT bigger.** With whole numbers, more digits "
            "won outright. Right of the point that rule DIES: $0.5 > "
            "0.47 > 0.399$. Wholes first, then tenths, then "
            "hundredths — the leftmost difference still decides.",
            "**Every decimal has neighbours.** $0.47$ lives between "
            "$0.4$ and $0.5$ on the number line — split the tenth into "
            "ten hundredths and count seven. Neighbour-thinking makes "
            "ordering fast and rounding (next lesson) obvious.",
        ],
        "keyIdea": (
            "Pad with trailing zeros until the places match, then "
            "compare left to right — the whole-number 'longer is "
            "bigger' rule is dead right of the point."),
        "facts": [
            {"title": "Pad and compare",
             "latex": "0.5 \\ \\text{vs} \\ 0.47 \\ \\to \\ 0.50 > 0.47",
             "explanation": "Trailing zeros cost nothing and make the places comparable."},
            {"title": "Longer isn't bigger",
             "latex": "0.5 > 0.399",
             "explanation": "Three digits lose to one — ladder position beats digit count."},
        ],
        "workedExamples": [
            {"id": "g5dc-l3-we1",
             "statement": "Compare $0.5$ and $0.47$.",
             "note": "Pad first.",
             "solution": ("Pad: $0.50$ vs $0.47$ — fifty hundredths against "
                          "forty-seven. $0.5 > 0.47$. (The \"$47$ beats $5$\" "
                          "instinct compares digit COUNTS, which mean nothing "
                          "right of the point.)"),
             "badges": [{"text": "core"}],
             "check": ["Rational(5,10) > Rational(47,100)",
                       "Eq(Rational(5,10), Rational(50,100))"]},
            {"id": "g5dc-l3-we2",
             "statement": "Order from smallest to largest: $3.09$, $3.9$, $3.19$.",
             "note": "Wholes tie — pad and scan the decimal places.",
             "solution": ("Pad: $3.09$, $3.90$, $3.19$. Tenths decide: $0 < 1 < 9$. "
                          "Order: $3.09 < 3.19 < 3.9$."),
             "badges": [{"text": "core"}],
             "check": ["Rational(309,100) < Rational(319,100)",
                       "Rational(319,100) < Rational(39,10)"]},
        ],
        "commonMistakes": [
            {"text": "Longer decimal = bigger number — 0.47 > 0.5 \"because 47 > 5\".",
             "correction": "Pad to equal places first: 0.50 vs 0.47. Right of the point, digit count means nothing; ladder position is everything.",
             "authored": True},
            {"text": "Comparing decimal parts as whole numbers across different lengths — 0.8 vs 0.75 read as 8 vs 75.",
             "correction": "8 TENTHS vs 75 HUNDREDTHS: pad to 0.80 and the comparison is honest — 80 > 75.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5dc-l3-t1",
             "statement": "Place the correct symbol: $0.8 \\;\\square\\; 0.75$.",
             "solution": "Pad: $0.80$ vs $0.75$ — $80 > 75$ hundredths: $0.8 > 0.75$.",
             "check": ["Rational(8,10) > Rational(75,100)"]},
            {"id": "g5dc-l3-t2",
             "statement": "Between which two tenths does $0.63$ sit?",
             "solution": "Between $0.6$ and $0.7$ — six tenths and three hundredths more, seven hundredths short of the next tenth.",
             "check": ["Rational(6,10) < Rational(63,100)", "Rational(63,100) < Rational(7,10)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Pad, then march left to right", [
                "Trailing zeros are free — $0.5 = 0.50$ — so give both numbers the same decimal length before comparing.",
                "$0.5$ vs $0.47$: padded, $0.50$ vs $0.47$ — fifty hundredths beat forty-seven. $0.5$ wins.",
                "Then march as always: wholes, tenths, hundredths — the leftmost difference decides, exactly like Topic 1.",
            ]), fig_numline([(0.4, "0.4"), (0.45, "0.45"), (0.5, "0.5")], lo=0.4, hi=0.5)),
            workedset("Padded comparisons",
                      "Equal lengths first; then it's Topic 1 again.", [
                wex("Compare $0.5$ and $0.47$.",
                    ["Pad: $0.50$ vs $0.47$.",
                     "$50 > 47$ hundredths: $0.5 > 0.47$."],
                    "$0.5 > 0.47$",
                    ["Rational(5,10) > Rational(47,100)"]),
                wex("Order $3.09$, $3.9$, $3.19$.",
                    ["Pad: $3.09, 3.90, 3.19$; wholes tie, tenths decide ($0 < 1 < 9$).",
                     "$3.09 < 3.19 < 3.9$."],
                    "$3.09 < 3.19 < 3.9$",
                    ["Rational(309,100) < Rational(319,100)", "Rational(319,100) < Rational(39,10)"]),
            ]),
            tryitset("Pad and decide", "Same length, then left to right.", [
                tp("Which symbol fits: $0.8 \\;\\square\\; 0.75$?",
                   ["$>$", "$<$", "$=$"],
                   "$0.80$ vs $0.75$: eighty hundredths win.",
                   ["Rational(8,10) > Rational(75,100)"]),
                tp("Which is the LARGEST: $0.6$, $0.59$, $0.61$?",
                   ["$0.61$", "$0.6$", "$0.59$"],
                   "Padded: $0.60, 0.59, 0.61$ — and $61$ hundredths tops the list.",
                   ["Rational(61,100) > Rational(6,10)", "Rational(6,10) > Rational(59,100)"]),
                tp("Which symbol fits: $2.05 \\;\\square\\; 2.5$?",
                   ["$<$", "$>$", "$=$"],
                   "Pad: $2.05$ vs $2.50$ — the inside zero keeps $2.05$ low: $<$.",
                   ["Rational(205,100) < Rational(25,10)"]),
            ]),
            tapq("The length trap", "A student says $0.399 > 0.5$ \"because $399 > 5$\". The truth:",
                 ["$0.5 > 0.399$ — five tenths beat three tenths, however long the tail",
                  "the student is right",
                  "they are equal",
                  "three-place decimals always win"],
                 "March from the left: tenths $5 > 3$ — decided before the tail even speaks. Padded: $0.500$ vs $0.399$.",
                 ["Rational(5,10) > Rational(399,1000)"]),
            funfact("Photo finishes live in the hundredths",
                    "Olympic sprints are timed to $0.01$ s: a $9.58$ against a $9.63$ is a five-hundredths gap — about the length of a forearm at full speed. Padding decimals to equal places is literally how race results are ranked."),
            withfig(teach("Concept B", "Neighbours on the number line", [
                "Every decimal lives between two neighbours one place coarser: $0.63$ sits between $0.6$ and $0.7$ — split the tenth into ten hundredths, count three.",
                "Neighbour-thinking orders fast: $0.63$, $0.7$, $0.59$ — which tenths do they live in? $0.59$ below $0.6$; $0.63$ in the sixties; $0.7$ on the line above.",
                "It also sets up rounding: the nearer neighbour is exactly where a decimal rounds (next lesson's business).",
            ]), fig_numline([(0, "0"), (0.25, "0.25"), (0.5, "0.5"), (0.75, "0.75"), (1, "1")], lo=0, hi=1)),
            workedset("Between the tenths",
                      "Name the tenth below and above.", [
                wex("Between which tenths does $0.63$ sit — and nearer which?",
                    ["$0.60 < 0.63 < 0.70$.",
                     "Three hundredths past $0.6$, seven short of $0.7$: nearer $0.6$."],
                    "between $0.6$ and $0.7$, nearer $0.6$",
                    ["Rational(6,10) < Rational(63,100)", "Rational(63,100) < Rational(7,10)",
                     "Eq(Rational(63,100) - Rational(6,10), Rational(3,100))"]),
                wex("Order $0.59$, $0.7$, $0.63$ by their neighbourhoods.",
                    ["$0.59$ lives below $0.6$; $0.63$ between $0.6$ and $0.7$; $0.7$ on the line.",
                     "$0.59 < 0.63 < 0.7$."],
                    "$0.59 < 0.63 < 0.7$",
                    ["Rational(59,100) < Rational(63,100)", "Rational(63,100) < Rational(7,10)"]),
            ]),
            tryitset("Neighbourhood watch", "Which tenths bracket each number?", [
                tp("$0.86$ sits between:",
                   ["$0.8$ and $0.9$", "$0.85$ and $0.87$ only", "$0$ and $0.1$"],
                   "Eight tenths and six hundredths: $0.80 < 0.86 < 0.90$.",
                   ["Rational(8,10) < Rational(86,100)", "Rational(86,100) < Rational(9,10)"]),
                tp("Which number sits between $2.3$ and $2.4$?",
                   ["$2.35$", "$2.43$", "$2.05$"],
                   "$2.30 < 2.35 < 2.40$. ($2.43$ overshoots; $2.05$ lives two neighbourhoods down.)",
                   ["Rational(23,10) < Rational(235,100)", "Rational(235,100) < Rational(24,10)"]),
                tp("Which is nearest to $1$: $0.89$, $1.2$, $0.95$?",
                   ["$0.95$", "$0.89$", "$1.2$"],
                   "Gaps: $0.11$, $0.2$, $0.05$ — and five hundredths is the smallest.",
                   ["Eq(1 - Rational(95,100), Rational(5,100))",
                    "Eq(1 - Rational(89,100), Rational(11,100))",
                    "Eq(Rational(12,10) - 1, Rational(2,10))",
                    "Rational(5,100) < Rational(11,100)"]),
            ]),
            tapq("Between-ness", "How many hundredths lie strictly between $0.4$ and $0.5$?",
                 ["nine — $0.41$ through $0.49$", "none", "ten", "four"],
                 "The tenth splits into ten hundredths; the two endpoints belong to the boundary, leaving $0.41, \\ldots, 0.49$ — nine of them.",
                 ["Eq(49 - 41 + 1, 9)", "Rational(4,10) < Rational(41,100)"]),
            recap([
                "Pad with trailing zeros until decimal lengths match — they cost nothing.",
                "Then march left to right; the leftmost difference decides.",
                "Longer is NOT bigger right of the point — the whole-number rule is dead there.",
                "Every decimal lives between two coarser neighbours; name them to order and to round.",
            ]),
            tip("Pad EVERY pair before comparing, even when you can see the answer — the habit is what saves you when you can't."),
            tryitset("Mixed practice", "Padding, marching, neighbourhoods.", [
                tp("Which symbol fits: $0.09 \\;\\square\\; 0.1$?",
                   ["$<$", "$>$", "$=$"],
                   "Pad: $0.09$ vs $0.10$ — nine hundredths against ten.",
                   ["Rational(9,100) < Rational(1,10)"]),
                tp("The smallest of $5.51$, $5.15$, $5.5$ is:",
                   ["$5.15$", "$5.51$", "$5.5$"],
                   "Tenths decide: $1 < 5$ — $5.15$ loses to both fives.",
                   ["Rational(515,100) < Rational(55,10)", "Rational(55,10) < Rational(551,100)"]),
                tp("In order from largest to smallest:",
                   ["$0.72 > 0.7 > 0.27$", "$0.7 > 0.72 > 0.27$", "$0.27 > 0.72 > 0.7$"],
                   "Padded: $0.72, 0.70, 0.27$ — and the marching order follows.",
                   ["Rational(72,100) > Rational(7,10)", "Rational(7,10) > Rational(27,100)"]),
                tp("A jump of $4.05$ m against one of $4.5$ m — the longer jump is:",
                   ["$4.5$ m — five tenths beat five hundredths", "$4.05$ m — more digits", "they tie"],
                   "$4.50$ vs $4.05$: the tenths decide, $5 > 0$.",
                   ["Rational(45,10) > Rational(405,100)"]),
                tp("Which number is between $0.7$ and $0.8$ AND nearer $0.8$?",
                   ["$0.76$", "$0.72$", "$0.83$"],
                   "$0.76$: six hundredths past $0.7$, four short of $0.8$ — inside, and nearer the top.",
                   ["Rational(7,10) < Rational(76,100)", "Rational(76,100) < Rational(8,10)",
                    "Eq(Rational(8,10) - Rational(76,100), Rational(4,100))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Comparing & Ordering Decimals\"",
                    "Pad, march, and know your neighbours — the whole comparing toolkit, with the length trap defused. Next: decimal arithmetic, where the ONE rule is to line up the point.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Adding & Subtracting Decimals
# ==========================================================================

def lesson_arithmetic():
    return {
        "slug": "adding-and-subtracting-decimals",
        "title": "Adding & Subtracting Decimals",
        "concreteComparison": (
            "A relay team's two runners clock $2.35$ and $1.4$ minutes. "
            "Stack the times RIGHT-ALIGNED — the whole-number habit — "
            "and you'd add $2.35 + 0.14$ by accident. Decimals align on "
            "the POINT: tenths under tenths, hundredths under "
            "hundredths. One habit changes; every carry and borrow you "
            "own still works."),
        "objective": (
            "Add and subtract decimals by aligning the decimal point, "
            "padding with zeros where needed — including subtracting "
            "decimals from whole numbers."),
        "concept": [
            "**Line up the POINT, not the right edge.** $2.35 + 1.4$: "
            "the $4$ is TENTHS, so it stands under the $3$: $2.35 + "
            "1.40 = 3.75$. Right-aligning (the whole-number habit) "
            "adds hundredths to tenths — the one new error decimals "
            "invent.",
            "**Pad, then compute as usual.** Give both numbers the same "
            "decimal length ($1.4 \\to 1.40$) and every carry and "
            "borrow from Topic 2 works unchanged — ten hundredths "
            "trade for one tenth, ten tenths for one whole.",
            "**Whole numbers have invisible points.** $5$ is $5.00$: "
            "so $5 - 1.36 = 5.00 - 1.36 = 3.64$, borrows travelling "
            "across the zeros exactly as they did in Topic 2. Receipt: "
            "$3.64 + 1.36 = 5$ ✓.",
        ],
        "keyIdea": (
            "Align the decimal points, pad to equal length, then add or "
            "subtract exactly as with whole numbers — carries and "
            "borrows trade by tens on both sides of the point."),
        "facts": [
            {"title": "Point under point",
             "latex": "2.35 + 1.40 = 3.75",
             "explanation": "Tenths under tenths; the padded zero makes the alignment visible."},
            {"title": "Invisible points",
             "latex": "5 - 1.36 = 5.00 - 1.36 = 3.64",
             "explanation": "A whole number is a decimal with .00 — pad it and borrow as usual."},
        ],
        "workedExamples": [
            {"id": "g5dc-l4-we1",
             "statement": "Add $2.35 + 1.4$, and show what the right-alignment error would have produced.",
             "note": "The 4 is tenths — it stands under the 3.",
             "solution": ("Align the points and pad: $2.35 + 1.40$. Hundredths: $5 + "
                          "0 = 5$; tenths: $3 + 4 = 7$; wholes: $2 + 1 = 3$ — "
                          "$3.75$. Right-aligned, the $4$ would have landed under "
                          "the $5$ as fake hundredths: $2.35 + 0.14 = 2.49$ — a "
                          "different (wrong) sum."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(235,100) + Rational(14,10), Rational(375,100))",
                       "Eq(Rational(235,100) + Rational(14,100), Rational(249,100))",
                       "Ne(Rational(249,100), Rational(375,100))"]},
            {"id": "g5dc-l4-we2",
             "statement": "Subtract $5 - 1.36$.",
             "note": "Give 5 its invisible decimal places first.",
             "solution": ("$5 = 5.00$. Borrow across the zeros (Topic 2's "
                          "travelling break): $5.00 - 1.36 = 3.64$. Receipt: $3.64 "
                          "+ 1.36 = 5.00$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5 - Rational(136,100), Rational(364,100))",
                       "Eq(Rational(364,100) + Rational(136,100), 5)"]},
        ],
        "commonMistakes": [
            {"text": "Right-aligning the numbers like whole-number addition — 2.35 + 1.4 becoming 2.35 + 0.14.",
             "correction": "Align the POINTS. Pad 1.4 to 1.40 and the 4 stands where it belongs — under the tenths.",
             "authored": True},
            {"text": "Dropping the decimal point from the answer — 2.35 + 1.40 = 375.",
             "correction": "The answer's point drops straight down from the aligned points: 3.75. An estimate (2 + 1 ≈ 3-and-a-bit) catches the hundredfold slip instantly.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5dc-l4-t1",
             "statement": "Add $4.68 + 2.57$.",
             "solution": "Hundredths: $8 + 7 = 15$ — write $5$ carry $1$. Tenths: $6 + 5 + 1 = 12$ — write $2$ carry $1$. Wholes: $4 + 2 + 1 = 7$. Sum: $7.25$.",
             "check": ["Eq(Rational(468,100) + Rational(257,100), Rational(725,100))"]},
            {"id": "g5dc-l4-t2",
             "statement": "Subtract $4.2 - 1.75$, then receipt the answer.",
             "solution": "Pad: $4.20 - 1.75$. Borrows in the hundredths and tenths: $2.45$. Receipt: $2.45 + 1.75 = 4.20$ ✓.",
             "check": ["Eq(Rational(42,10) - Rational(175,100), Rational(245,100))",
                       "Eq(Rational(245,100) + Rational(175,100), Rational(42,10))"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One new habit: point under point", [
                "Whole-number columns aligned on the right edge. Decimal columns align on the POINT — tenths under tenths, hundredths under hundredths.",
                "$2.35 + 1.4$: pad to $1.40$ so the alignment is visible, then add columns as always: $3.75$.",
                "Right-aligning would drop the $4$ under the $5$ — adding tenths to hundredths, the one error decimals invent. Padding makes it impossible.",
            ]), {"mode": "decimalColumn", "column": {"a": 3.4, "b": 1.25, "op": "add"}}),
            workedset("Adding on the staircase",
                      "Align points, pad, and let the old carries work.", [
                wex("Add $2.35 + 1.4$.",
                    ["Pad: $2.35 + 1.40$; the points stack.",
                     "$5 + 0$, $3 + 4$, $2 + 1$: $3.75$."],
                    "$3.75$",
                    ["Eq(Rational(235,100) + Rational(14,10), Rational(375,100))"]),
                wex("Add $4.68 + 2.57$.",
                    ["Hundredths $8 + 7 = 15$: write $5$, carry. Tenths $6 + 5 + 1 = 12$: write $2$, carry.",
                     "Wholes $4 + 2 + 1 = 7$: sum $7.25$."],
                    "$7.25$",
                    ["Eq(Rational(468,100) + Rational(257,100), Rational(725,100))"]),
            ]),
            tryitset("Point-aligned sums", "Pad first; the carries are old friends.", [
                tp("$3.6 + 2.75$ equals:",
                   ["$6.35$", "$6.11$", "$3.11$"],
                   "Pad: $3.60 + 2.75 = 6.35$. ($3.11$ is the right-alignment wreck — the $3.6$ read as $0.36$.)",
                   ["Eq(Rational(36,10) + Rational(275,100), Rational(635,100))",
                    "Eq(Rational(36,100) + Rational(275,100), Rational(311,100))"]),
                tp("$0.85 + 0.15$ equals:",
                   ["$1$", "$0.9$", "$1.1$"],
                   "$85 + 15 = 100$ hundredths — exactly one whole.",
                   ["Eq(Rational(85,100) + Rational(15,100), 1)"]),
                tp("$12.5 + 3.75$ equals:",
                   ["$16.25$", "$15.8$", "$12.875$"],
                   "Pad: $12.50 + 3.75 = 16.25$.",
                   ["Eq(Rational(125,10) + Rational(375,100), Rational(1625,100))"]),
            ]),
            tapq("Catch the misalignment", "A student stacks $2.35 + 1.4$ right-aligned and gets $2.49$. The estimate $2 + 1 \\approx 3$ says:",
                 ["$2.49$ is too small — the $1.4$ was read as $0.14$",
                  "$2.49$ is fine",
                  "estimates don't work on decimals",
                  "the answer should be $24.9$"],
                 "Adding more than $1$ to $2.35$ must pass $3.35$ — but $2.49$ barely moved. The right edge stole a ladder step; point-alignment gives $3.75$.",
                 ["Eq(Rational(235,100) + Rational(14,10), Rational(375,100))",
                  "Rational(249,100) < 3"]),
            funfact("Cash registers add in hundredths",
                    "Every till on earth runs this lesson: prices are stored as whole HUNDREDTHS (cents, möngö) precisely so machines can add them like whole numbers and place the point at the end — the pad-and-align trick, industrialised."),
            withfig(teach("Concept B", "Subtraction, and the invisible point", [
                "Subtracting works the same: align points, pad, borrow as in Topic 2 — ten hundredths trade for a tenth, ten tenths for a whole.",
                "Whole numbers carry invisible decimal places: $5 = 5.00$. So $5 - 1.36$ becomes $5.00 - 1.36$, borrows travelling across the zeros: $3.64$.",
                "Keep the receipt habit: $3.64 + 1.36 = 5$ ✓ — additions still check subtractions on the staircase.",
            ]), {"mode": "decimalColumn", "column": {"a": 5.0, "b": 2.35, "op": "sub"}}),
            workedset("Borrowing past the point",
                      "Pad, borrow, receipt.", [
                wex("Subtract $4.2 - 1.75$.",
                    ["Pad: $4.20 - 1.75$; borrow through hundredths and tenths.",
                     "$2.45$; receipt $2.45 + 1.75 = 4.20$ ✓."],
                    "$2.45$",
                    ["Eq(Rational(42,10) - Rational(175,100), Rational(245,100))"]),
                wex("Subtract $5 - 1.36$.",
                    ["$5 = 5.00$; the borrow travels the zeros.",
                     "$3.64$; receipt $3.64 + 1.36 = 5$ ✓."],
                    "$3.64$",
                    ["Eq(5 - Rational(136,100), Rational(364,100))"]),
            ]),
            tryitset("Take-aways on the staircase", "Invisible points, travelling borrows.", [
                tp("$6.4 - 2.85$ equals:",
                   ["$3.55$", "$4.45$", "$3.65$"],
                   "Pad: $6.40 - 2.85 = 3.55$; receipt $3.55 + 2.85 = 6.40$ ✓.",
                   ["Eq(Rational(64,10) - Rational(285,100), Rational(355,100))"]),
                tp("$3 - 0.47$ equals:",
                   ["$2.53$", "$2.63$", "$3.47$"],
                   "$3.00 - 0.47$: borrows across both zeros — $2.53$.",
                   ["Eq(3 - Rational(47,100), Rational(253,100))"]),
                tp("$10 - 4.05$ equals:",
                   ["$5.95$", "$6.05$", "$5.05$"],
                   "$10.00 - 4.05 = 5.95$; receipt $5.95 + 4.05 = 10$ ✓.",
                   ["Eq(10 - Rational(405,100), Rational(595,100))"]),
            ]),
            tapq("Receipt on the staircase", "Which addition CHECKS $7.2 - 3.85 = 3.35$?",
                 ["$3.35 + 3.85 = 7.2$", "$7.2 + 3.85 = 11.05$", "$3.85 - 3.35 = 0.5$", "$3.35 + 7.2 = 10.55$"],
                 "Answer plus subtracted rebuilds the original: $3.35 + 3.85 = 7.20$ ✓.",
                 ["Eq(Rational(72,10) - Rational(385,100), Rational(335,100))",
                  "Eq(Rational(335,100) + Rational(385,100), Rational(72,10))"]),
            recap([
                "Align the POINTS, never the right edge; pad to equal length.",
                "Carries and borrows trade by tens on both sides of the point — nothing new.",
                "Whole numbers are decimals with invisible .00 — pad them before subtracting.",
                "Estimate every answer and receipt every subtraction, as always.",
            ]),
            tip("Write the padded zeros explicitly on every problem — visible alignment is what makes the point-habit permanent."),
            tryitset("Mixed practice", "Sums and differences, points stacked.", [
                tp("$7.09 + 0.91$ equals:",
                   ["$8$", "$7.1$", "$8.1$"],
                   "The decimal parts complete each other: $0.09 + 0.91 = 1.00$, and with the $7$ that is exactly $8$.",
                   ["Eq(Rational(9,100) + Rational(91,100), 1)",
                    "Eq(Rational(709,100) + Rational(91,100), 8)"]),
                tp("$5.5 - 0.75$ equals:",
                   ["$4.75$", "$5.25$", "$4.85$"],
                   "$5.50 - 0.75 = 4.75$; receipt $4.75 + 0.75 = 5.50$ ✓.",
                   ["Eq(Rational(55,10) - Rational(75,100), Rational(475,100))"]),
                tp("A rope of $8$ m loses a $2.35$ m piece. Remaining:",
                   ["$5.65$ m", "$6.65$ m", "$5.75$ m"],
                   "$8.00 - 2.35 = 5.65$.",
                   ["Eq(8 - Rational(235,100), Rational(565,100))"]),
                tp("$1.8 + 1.8 + 1.8$ equals:",
                   ["$5.4$", "$3.24$", "$5.24$"],
                   "Three lots of $1.8$: $5.4$ — eighteen tenths tripled is fifty-four tenths.",
                   ["Eq(3*Rational(18,10), Rational(54,10))"]),
                tp("Runners clock $12.65$ s and $11.9$ s. The gap is:",
                   ["$0.75$ s", "$0.85$ s", "$1.25$ s"],
                   "$12.65 - 11.90 = 0.75$; receipt $0.75 + 11.9 = 12.65$ ✓.",
                   ["Eq(Rational(1265,100) - Rational(119,10), Rational(75,100))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Adding & Subtracting Decimals\"",
                    "One habit — point under point — and the whole of Topic 2 came along for free. Last stop: rounding decimals and putting them to work on real measurements.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Rounding & Measuring with Decimals
# ==========================================================================

def lesson_measurement():
    return {
        "slug": "rounding-and-measuring-with-decimals",
        "title": "Rounding & Measuring with Decimals",
        "concreteComparison": (
            "The scale says your marmot-sized dog weighs $3.47$ kg. "
            "You tell your friend \"about three and a half kilos\" — "
            "you just rounded to the nearest tenth. Decimals are how "
            "the world measures — heights, weights, race times — and "
            "rounding them works exactly like Topic 1: same landmarks, "
            "same digit rule, one staircase further down."),
        "objective": (
            "Round decimals to the nearest whole and nearest tenth, "
            "convert measurements (metres–centimetres) through "
            "decimals, and estimate with rounded decimals."),
        "concept": [
            "**Same rounding, finer landmarks.** Nearest tenth: the "
            "landmarks are neighbouring tenths, and the hundredths "
            "digit decides — $3.47$ has hundredths digit $7 \\ge 5$: "
            "up to $3.5$. Nearest whole: the tenths digit decides — "
            "$3.47 \\to 3$.",
            "**Measurements are decimals in uniform.** $1.35$ m is "
            "$135$ cm — multiplying by $100$ walks every digit two "
            "steps up the ladder. $2.5$ kg is $2\\,500$ g. Unit "
            "conversions are place-value shifts.",
            "**Estimates guard decimal arithmetic too.** $3.9 + 2.1$: "
            "round to $4 + 2 = 6$ — and the exact answer ($6.0$) "
            "lands beside it. The Topic 1 guardrail works at every "
            "scale of the staircase.",
        ],
        "keyIdea": (
            "Round decimals with the same landmark-and-digit rule, one "
            "staircase further down; unit conversions are place shifts; "
            "rounded estimates still guard every computation."),
        "facts": [
            {"title": "Nearest tenth",
             "latex": "3.47 \\to 3.5 \\quad (\\text{hundredths digit } 7 \\ge 5)",
             "explanation": "The digit one place below the target still decides — same rule, finer landmarks."},
            {"title": "Metres to centimetres",
             "latex": "1.35 \\ \\text{m} = 135 \\ \\text{cm}",
             "explanation": "×100 walks the digits two ladder steps — conversions are place shifts."},
        ],
        "workedExamples": [
            {"id": "g5dc-l5-we1",
             "statement": "Round $3.47$ to the nearest tenth, and to the nearest whole.",
             "note": "Landmarks first; the digit below decides.",
             "solution": ("Nearest tenth: landmarks $3.4$ and $3.5$; hundredths "
                          "digit $7 \\ge 5$ — up to $3.5$ (it is $0.03$ from $3.5$ "
                          "but $0.07$ from $3.4$). Nearest whole: landmarks $3$ and "
                          "$4$; tenths digit $4 < 5$ — down to $3$."),
             "badges": [{"text": "core"}],
             "check": ["Abs(Rational(347,100) - Rational(35,10)) < Abs(Rational(347,100) - Rational(34,10))",
                       "Abs(Rational(347,100) - 3) < Abs(Rational(347,100) - 4)"]},
            {"id": "g5dc-l5-we2",
             "statement": "A board is $1.35$ m long. How many centimetres is that — and how many centimetres short of $2$ m?",
             "note": "×100 is two ladder steps.",
             "solution": ("$1.35 \\times 100 = 135$ cm. Two metres is $200$ cm: "
                          "$200 - 135 = 65$ cm short."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(135,100)*100, 135)", "Eq(200 - 135, 65)"]},
        ],
        "commonMistakes": [
            {"text": "Rounding 3.47 to the nearest tenth by looking at the tenths digit itself.",
             "correction": "The digit BELOW the target place decides. For tenths, look at the hundredths (7): 3.47 → 3.5. The tenths digit is what gets rounded, not what decides.",
             "authored": True},
            {"text": "Converting 1.35 m to 1,035 cm — treating the decimal digits as already-centimetres.",
             "correction": "×100 shifts EVERY digit two places: 1.35 m = 135 cm. Sanity check: a metre-and-a-third can't be ten metres of centimetres.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5dc-l5-t1",
             "statement": "Round $7.84$ to the nearest tenth and the nearest whole.",
             "solution": "Tenth: hundredths digit $4 < 5$ — $7.8$. Whole: tenths digit $8 \\ge 5$ — $8$.",
             "check": ["Abs(Rational(784,100) - Rational(78,10)) < Abs(Rational(784,100) - Rational(79,10))",
                       "Abs(Rational(784,100) - 8) < Abs(Rational(784,100) - 7)"]},
            {"id": "g5dc-l5-t2",
             "statement": "Convert $2.07$ m to centimetres, and $450$ cm to metres.",
             "solution": "$2.07 \\times 100 = 207$ cm. Backwards, $\\div 100$: $450$ cm $= 4.5$ m.",
             "check": ["Eq(Rational(207,100)*100, 207)", "Eq(Rational(450,100), Rational(45,10))"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Rounding, one staircase down", [
                "Rounding decimals is Topic 1's rule on finer landmarks. Nearest TENTH: the landmarks are neighbouring tenths, and the HUNDREDTHS digit decides — $3.47 \\to 3.5$.",
                "Nearest WHOLE: the tenths digit decides — $3.47 \\to 3$ (four tenths falls short of half).",
                "Always one place below the target: that digit, and only that digit, casts the vote.",
            ]), fig_numline([(2.0, "2"), (2.4, "2.4"), (2.5, "2.5 — the tie"), (3.0, "3")], lo=2, hi=3)),
            workedset("Landmark practice",
                      "Name the two landmarks; let the digit below vote.", [
                wex("Round $3.47$ both ways.",
                    ["Nearest tenth: $3.4$ | $3.5$; hundredths $7$ votes up — $3.5$.",
                     "Nearest whole: $3$ | $4$; tenths $4$ votes down — $3$."],
                    "$3.5$ and $3$",
                    ["Abs(Rational(347,100) - Rational(35,10)) < Abs(Rational(347,100) - Rational(34,10))",
                     "Abs(Rational(347,100) - 3) < Abs(Rational(347,100) - 4)"]),
                wex("Round $12.96$ to the nearest tenth.",
                    ["Landmarks $12.9$ and $13.0$; hundredths $6$ votes up.",
                     "$13.0$ — the round-up crosses into a new whole."],
                    "$13.0$",
                    ["Abs(Rational(1296,100) - 13) < Abs(Rational(1296,100) - Rational(129,10))"]),
            ]),
            tryitset("Round it", "One place below the target votes.", [
                tp("$7.84$ to the nearest tenth is:",
                   ["$7.8$", "$7.9$", "$8$"],
                   "Hundredths $4 < 5$: down to $7.8$.",
                   ["Abs(Rational(784,100) - Rational(78,10)) < Abs(Rational(784,100) - Rational(79,10))"]),
                tp("$7.84$ to the nearest WHOLE is:",
                   ["$8$", "$7$", "$7.8$"],
                   "Tenths $8 \\ge 5$: up to $8$. (Different target place, different vote.)",
                   ["Abs(Rational(784,100) - 8) < Abs(Rational(784,100) - 7)"]),
                tp("$0.45$ to the nearest tenth is:",
                   ["$0.5$", "$0.4$", "$0$"],
                   "Landmarks $0.4$ | $0.5$; hundredths $5$ — the tie votes up: $0.5$.",
                   ["Eq(Abs(Rational(45,100) - Rational(4,10)), Rational(5,100))",
                    "Eq(Abs(Rational(45,100) - Rational(5,10)), Rational(5,100))"]),
            ]),
            tapq("Which digit votes?", "Rounding $6.38$ to the nearest tenth, the deciding digit is:",
                 ["the $8$ — the hundredths", "the $3$ — the tenths", "the $6$ — the wholes", "no digit; guess"],
                 "One place below the target: the hundredths digit $8$ votes up — $6.38 \\to 6.4$.",
                 ["Abs(Rational(638,100) - Rational(64,10)) < Abs(Rational(638,100) - Rational(63,10))"]),
            funfact("Scales round for you",
                    "A kitchen scale showing $1.3$ kg has already rounded — the true weight might be anywhere from $1.25$ to $1.35$ kg. Every measuring device rounds at the limit of its display; knowing the landmark-width tells you how much to trust the last digit."),
            withfig(teach("Concept B", "Measurements ride the ladder", [
                "Unit conversions are place shifts. Metres to centimetres: $\\times 100$ — two ladder steps: $1.35$ m $= 135$ cm. Back again: $\\div 100$ — $450$ cm $= 4.5$ m.",
                "Kilograms to grams: $\\times 1\\,000$ — three steps: $2.5$ kg $= 2\\,500$ g.",
                "And the estimate guardrail survives: $3.9 + 2.1 \\approx 4 + 2 = 6$ — the exact $6.0$ lands on it. Round, compute, compare — at every scale.",
            ]), fig_numline([(0, "0 m"), (1.75, "1.75 m"), (2, "2 m")], lo=0, hi=2)),
            workedset("Converting and estimating",
                      "Shifts for units; rounds for guardrails.", [
                wex("Convert $1.35$ m to cm, and find the shortfall from $2$ m.",
                    ["$1.35 \\times 100 = 135$ cm.",
                     "$200 - 135 = 65$ cm short."],
                    "$135$ cm; $65$ cm short",
                    ["Eq(Rational(135,100)*100, 135)", "Eq(200 - 135, 65)"]),
                wex("Estimate, then compute: $4.85 + 3.2$.",
                    ["Estimate: $5 + 3 = 8$.",
                     "Exact: $4.85 + 3.20 = 8.05$ — right beside the guardrail. ✓"],
                    "$8.05$",
                    ["Eq(Rational(485,100) + Rational(32,10), Rational(805,100))"]),
            ]),
            tryitset("Shifts and guardrails", "Two steps for cm; three for grams.", [
                tp("$2.07$ m in centimetres is:",
                   ["$207$ cm", "$2\\,070$ cm", "$27$ cm"],
                   "$\\times 100$: every digit two steps up — $207$ cm.",
                   ["Eq(Rational(207,100)*100, 207)"]),
                tp("$450$ cm in metres is:",
                   ["$4.5$ m", "$45$ m", "$0.45$ m"],
                   "$\\div 100$: $4.5$ m.",
                   ["Eq(Rational(450,100), Rational(45,10))"]),
                tp("$2.5$ kg in grams is:",
                   ["$2\\,500$ g", "$250$ g", "$25\\,000$ g"],
                   "$\\times 1\\,000$: three steps — $2\\,500$ g.",
                   ["Eq(Rational(25,10)*1000, 2500)"]),
            ]),
            tapq("Guardrail at speed", "$7.9 + 4.2$ should land near:",
                 ["$12$ — from $8 + 4$", "$1.2$", "$120$", "$8.1$"],
                 "Round each: $8 + 4 = 12$; the exact $12.1$ sits beside it. An answer of $1.21$ or $121$ lost the point.",
                 ["Eq(Rational(79,10) + Rational(42,10), Rational(121,10))",
                  "Eq(8 + 4, 12)"]),
            recap([
                "Round decimals with the landmark rule; the digit one place below the target votes.",
                "Nearest tenth reads the hundredths; nearest whole reads the tenths.",
                "Unit conversions are ladder shifts: ×100 for m→cm, ×1,000 for kg→g.",
                "Rounded estimates guard decimal arithmetic at every scale.",
            ]),
            tip("Estimate before computing and name the deciding digit before rounding — the two habits that make decimals safe in the wild."),
            tryitset("Mixed practice", "Rounding, converting, estimating — the field kit.", [
                tp("$9.55$ to the nearest tenth is:",
                   ["$9.6$", "$9.5$", "$10$"],
                   "Hundredths $5$ — the tie votes up: $9.6$.",
                   ["Eq(Abs(Rational(955,100) - Rational(95,10)), Rational(5,100))",
                    "Eq(Abs(Rational(955,100) - Rational(96,10)), Rational(5,100))"]),
                tp("A $1.48$ m child, to the nearest tenth of a metre, is about:",
                   ["$1.5$ m", "$1.4$ m", "$1$ m"],
                   "Hundredths $8$ votes up: $1.5$ m.",
                   ["Abs(Rational(148,100) - Rational(15,10)) < Abs(Rational(148,100) - Rational(14,10))"]),
                tp("$3.05$ m equals:",
                   ["$305$ cm", "$35$ cm", "$3\\,050$ cm"],
                   "$\\times 100$: $305$ cm — the inside zero rides along.",
                   ["Eq(Rational(305,100)*100, 305)"]),
                tp("Two parcels weigh $2.7$ kg and $3.45$ kg. Together, to the nearest whole kg:",
                   ["$6$ kg", "$5$ kg", "$7$ kg"],
                   "Exact: $2.70 + 3.45 = 6.15$; tenths digit $1 < 5$: down to $6$ kg.",
                   ["Eq(Rational(27,10) + Rational(345,100), Rational(615,100))",
                    "Abs(Rational(615,100) - 6) < Abs(Rational(615,100) - 7)"]),
                tp("A shelf is $0.9$ m; the space is $84$ cm. Does it fit?",
                   ["no — the shelf is $90$ cm, $6$ cm too long", "yes — $0.9 < 84$", "they are equal"],
                   "Convert to one unit: $0.9$ m $= 90$ cm $> 84$ cm — six centimetres too long.",
                   ["Eq(Rational(9,10)*100, 90)", "Eq(90 - 84, 6)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Decimals\" — the whole topic",
                    "The staircase now runs both ways, decimals and fractions are one family, and you can compare, compute, round and measure with them. Grade 5's remaining topics — measurement, geometry, and data — will use these skills on every page.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5dc-pr1", "Write $4.09$ as a sum of place values and as one fraction.",
             "$4 + \\frac{0}{10} + \\frac{9}{100} = \\frac{409}{100}$ — the zero tenths hold the place.",
             ["Eq(4 + Rational(9,100), Rational(409,100))"]),
        prob("g5dc-pr2", "Which is bigger, and by how much: the $7$ in $0.7$ or the $7$ in $0.07$?",
             "Tenths against hundredths: $\\frac{7}{10} = 10 \\times \\frac{7}{100}$ — ten times bigger.",
             ["Eq(Rational(7,10), 10*Rational(7,100))"]),
        prob("g5dc-pr3", "Convert: $0.65$ to a simplest-form fraction, and $\\frac{7}{25}$ to a decimal.",
             "$0.65 = \\frac{65}{100} = \\frac{13}{20}$. And $\\frac{7}{25} = \\frac{28}{100} = 0.28$.",
             ["Eq(Rational(65,100), Rational(13,20))", "Eq(Rational(7,25), Rational(28,100))"]),
        prob("g5dc-pr4", "Order from smallest to largest: $0.72$, $0.7$, $0.27$, $0.702$.",
             "Pad to thousandths: $0.720, 0.700, 0.270, 0.702$ — so $0.27 < 0.7 < 0.702 < 0.72$.",
             ["Rational(27,100) < Rational(7,10)", "Rational(7,10) < Rational(702,1000)",
              "Rational(702,1000) < Rational(72,100)"]),
        prob("g5dc-pr5", "Add $5.68 + 3.7$, showing the padded alignment.",
             "Pad: $5.68 + 3.70$; carries in tenths: $9.38$.",
             ["Eq(Rational(568,100) + Rational(37,10), Rational(938,100))"]),
        prob("g5dc-pr6", "Subtract $7 - 2.64$ and receipt the answer.",
             "$7.00 - 2.64 = 4.36$; receipt $4.36 + 2.64 = 7$ ✓.",
             ["Eq(7 - Rational(264,100), Rational(436,100))",
              "Eq(Rational(436,100) + Rational(264,100), 7)"]),
        prob("g5dc-pr7", "Round $14.65$ to the nearest tenth and to the nearest whole.",
             "Tenth: hundredths $5$ — tie votes up: $14.7$. Whole: tenths $6$ — up: $15$.",
             ["Eq(Abs(Rational(1465,100) - Rational(146,10)), Rational(5,100))",
              "Eq(Abs(Rational(1465,100) - Rational(147,10)), Rational(5,100))",
              "Abs(Rational(1465,100) - 15) < Abs(Rational(1465,100) - 14)"]),
        prob("g5dc-pr8", "A jump of $3.85$ m beats one of $3.6$ m by how many centimetres?",
             "$3.85 - 3.60 = 0.25$ m $= 25$ cm.",
             ["Eq(Rational(385,100) - Rational(36,10), Rational(25,100))",
              "Eq(Rational(25,100)*100, 25)"]),
    ]


def test_bank():
    return [
        prob("g5dc-x1", "What is the value of the $4$ in $6.42$, and in $6.04$?",
             "In $6.42$: four tenths, $\\frac{4}{10}$. In $6.04$: four hundredths, $\\frac{4}{100}$ — ten times smaller.",
             ["Eq(Rational(4,10), 10*Rational(4,100))"]),
        prob("g5dc-x2", "Convert $0.35$ to a simplest-form fraction and $\\frac{4}{5}$ to a decimal.",
             "$0.35 = \\frac{35}{100} = \\frac{7}{20}$; and $\\frac{4}{5} = \\frac{8}{10} = 0.8$.",
             ["Eq(Rational(35,100), Rational(7,20))", "Eq(Rational(4,5), Rational(8,10))"]),
        prob("g5dc-x3", "Place the correct symbol: $0.6 \\;\\square\\; 0.58$, and explain the padding move.",
             "Pad: $0.60$ vs $0.58$ — sixty hundredths beat fifty-eight: $0.6 > 0.58$. The trailing zero costs nothing and makes the places comparable.",
             ["Rational(6,10) > Rational(58,100)", "Eq(Rational(6,10), Rational(60,100))"]),
        prob("g5dc-x4", "Add $6.75 + 2.8$.",
             "Pad: $6.75 + 2.80 = 9.55$.",
             ["Eq(Rational(675,100) + Rational(28,10), Rational(955,100))"]),
        prob("g5dc-x5", "Subtract $4 - 1.62$ and receipt the answer.",
             "$4.00 - 1.62 = 2.38$; receipt $2.38 + 1.62 = 4$ ✓.",
             ["Eq(4 - Rational(162,100), Rational(238,100))",
              "Eq(Rational(238,100) + Rational(162,100), 4)"]),
        prob("g5dc-x6", ("A relay's two legs take $13.48$ s and $12.7$ s. Find the total, "
                         "round it to the nearest second, and convert $1.35$ m to cm as a "
                         "final flourish."),
             "Total: $13.48 + 12.70 = 26.18$ s; tenths digit $1 < 5$ — rounds to $26$ s. And $1.35$ m $= 135$ cm.",
             ["Eq(Rational(1348,100) + Rational(127,10), Rational(2618,100))",
              "Abs(Rational(2618,100) - 26) < Abs(Rational(2618,100) - 27)",
              "Eq(Rational(135,100)*100, 135)"]),
    ]


def main():
    topic = {
        "slug": "decimals-first-steps",
        "title": "Decimals — First Steps",
        "grade": 5,
        "status": "published",
        "blurb": ("Tenths and hundredths on the extended place-value ladder, "
                  "decimals as fractions, comparing without the length trap, "
                  "adding and subtracting on the point, and rounding and "
                  "measuring with decimals."),
        "lessons": [
            lesson_tenths(),
            lesson_conversion(),
            lesson_comparing(),
            lesson_arithmetic(),
            lesson_measurement(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "decimals-first-steps.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
