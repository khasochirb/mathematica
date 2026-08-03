#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 4: Fractions — First Steps.

What a fraction IS (equal parts of a whole, fractions of a set, the
number line), equivalent fractions (split and merge the pieces),
comparing (same-denominator, same-numerator, and benchmark thinking),
improper fractions and mixed numbers (division wearing new clothes),
and adding/subtracting with like denominators — including the
denominator-adding error, named and hunted.

Through-line: THE DENOMINATOR NAMES THE PIECE. Everything in this topic
— equivalence, comparison, addition — follows from one question: what
size piece are we talking about, and how many of them are there?

Same construction as the other Grade 5 builders: every check anywhere
in the structure is sympy-asserted (exact Rational arithmetic) BEFORE
the JSON is written — a wrong fraction fact cannot ship.

Run: python3 scripts/grade5/build_fractions.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic)


# ==========================================================================
# Lesson 1 — What a Fraction Is
# ==========================================================================

def lesson_meaning():
    return {
        "slug": "what-a-fraction-is",
        "title": "What a Fraction Is",
        "concreteComparison": (
            "A round bread is cut into $8$ EQUAL pieces and you eat $3$. "
            "The amount you ate has a name: $\\frac{3}{8}$ of the bread. "
            "The bottom number says what size the pieces are (eighths — "
            "eight of them make the whole); the top number counts how "
            "many you took. Two numbers, one amount — and the word "
            "EQUAL is doing all the honest work."),
        "objective": (
            "Read and write fractions as equal parts of a whole, find a "
            "fraction of a set, place fractions on the number line, and "
            "recognise when parts are NOT equal."),
        "concept": [
            "**The denominator names the piece.** The bottom number says "
            "how many EQUAL parts make one whole — eighths mean eight "
            "equal parts. The top number, the numerator, counts how many "
            "of those parts you have: $\\frac{3}{8}$ is three pieces of "
            "the eight-piece size.",
            "**Unit fractions are the atoms.** $\\frac{1}{8}$ is ONE "
            "piece; every fraction is a stack of unit fractions — "
            "$\\frac{3}{8}$ is $\\frac{1}{8} + \\frac{1}{8} + "
            "\\frac{1}{8}$. And eight eighths rebuild the whole: "
            "$\\frac{8}{8} = 1$.",
            "**Fractions live on the number line and in sets.** "
            "$\\frac{3}{4}$ is a POINT between $0$ and $1$ (split the "
            "unit into four, count three); and $\\frac{3}{4}$ OF $12$ "
            "apples is $9$ apples — split the set into four equal "
            "groups of $3$, take three groups.",
        ],
        "keyIdea": (
            "The denominator says what size the equal pieces are; the "
            "numerator counts them. Same two numbers work for shapes, "
            "sets, and points on the number line."),
        "facts": [
            {"title": "Numerator over denominator",
             "latex": "\\frac{3}{8}: \\ 3 \\ \\text{pieces of the}\\ 8\\text{-per-whole size}",
             "explanation": "Bottom names the piece size; top counts the pieces."},
            {"title": "The whole rebuilt",
             "latex": "\\frac{8}{8} = 1",
             "explanation": "All the pieces together are exactly one whole — the denominator's promise."},
        ],
        "workedExamples": [
            {"id": "g5fr-l1-we1",
             "statement": "A bread is cut into $8$ equal pieces; you eat $3$ and your brother eats $5$. What fraction did each eat, and what do the two fractions make together?",
             "note": "Count pieces; the whole is eight eighths.",
             "solution": ("You: $\\frac{3}{8}$. Brother: $\\frac{5}{8}$. Together: "
                          "$\\frac{3}{8} + \\frac{5}{8} = \\frac{8}{8} = 1$ — the "
                          "whole bread, as it must be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(3,8) + Rational(5,8), 1)"]},
            {"id": "g5fr-l1-we2",
             "statement": "Find $\\frac{3}{4}$ of $12$ apples.",
             "note": "Split into four equal groups, take three.",
             "solution": ("Four equal groups of $12 \\div 4 = 3$ apples each; take "
                          "three groups: $3 \\times 3 = 9$ apples. So $\\frac{3}{4}$ "
                          "of $12$ is $9$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(12,4), 3)", "Eq(3*3, 9)", "Eq(Rational(3,4)*12, 9)"]},
        ],
        "commonMistakes": [
            {"text": "Counting unequal parts as a fraction — calling a lopsided 3-of-5 cut \"3/5\".",
             "correction": "Fractions require EQUAL parts. If the pieces differ, the denominator's name is a lie — cut again or count differently.",
             "authored": True},
            {"text": "Reading 3/8 as \"3 and 8\" — two separate numbers.",
             "correction": "A fraction is ONE amount: three pieces of the eighth size. The bar is not a comma.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5fr-l1-t1",
             "statement": "A week has $7$ days; you train on $4$ of them. What fraction of the week do you train, and what fraction is training-free?",
             "solution": "Training: $\\frac{4}{7}$. Free: $\\frac{3}{7}$. Together $\\frac{4}{7} + \\frac{3}{7} = \\frac{7}{7} = 1$ — the whole week.",
             "check": ["Eq(Rational(4,7) + Rational(3,7), 1)"]},
            {"id": "g5fr-l1-t2",
             "statement": "Find $\\frac{2}{5}$ of $20$.",
             "solution": "Five equal groups of $4$; take two: $\\frac{2}{5}$ of $20 = 8$.",
             "check": ["Eq(Rational(20,5), 4)", "Eq(Rational(2,5)*20, 8)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Bottom names, top counts", [
                "Cut a whole into EQUAL parts: the denominator (bottom) says how many parts make the whole — that's the piece's NAME. Eighths: eight per whole.",
                "The numerator (top) counts how many pieces you have: $\\frac{3}{8}$ is three pieces of the eighth size.",
                "Every fraction is a stack of unit fractions — $\\frac{3}{8} = \\frac{1}{8} + \\frac{1}{8} + \\frac{1}{8}$ — and all the pieces together rebuild the whole: $\\frac{8}{8} = 1$.",
            ]),
            workedset("Reading fractions",
                      "Name the piece, count the pieces.", [
                wex("A bread in $8$ equal pieces: you eat $3$, your brother $5$. Fractions?",
                    ["You: $\\frac{3}{8}$; brother: $\\frac{5}{8}$.",
                     "Together: $\\frac{3}{8} + \\frac{5}{8} = \\frac{8}{8} = 1$ — the whole bread."],
                    "$\\frac{3}{8}$ and $\\frac{5}{8}$",
                    ["Eq(Rational(3,8) + Rational(5,8), 1)"]),
                wex("What fraction of an hour is $45$ minutes?",
                    ["An hour is $60$ minutes; each minute is $\\frac{1}{60}$ of it.",
                     "$45$ minutes is $\\frac{45}{60}$ — which you'll soon write as $\\frac{3}{4}$."],
                    "$\\frac{45}{60}$",
                    ["Eq(Rational(45,60), Rational(3,4))"]),
            ]),
            tryitset("Count the pieces", "Equal parts only — check before counting.", [
                tp("A pizza is cut into $6$ equal slices and $5$ are taken. The fraction taken is:",
                   ["$\\frac{5}{6}$", "$\\frac{6}{5}$", "$\\frac{5}{11}$"],
                   "Six equal slices make the whole (sixths); five are taken: $\\frac{5}{6}$. And $\\frac{1}{6}$ remains: $\\frac{5}{6} + \\frac{1}{6} = 1$.",
                   ["Eq(Rational(5,6) + Rational(1,6), 1)"]),
                tp("You train $4$ days of a $7$-day week. The training-free fraction is:",
                   ["$\\frac{3}{7}$", "$\\frac{4}{7}$", "$\\frac{3}{4}$"],
                   "$7 - 4 = 3$ free days of the seven: $\\frac{3}{7}$.",
                   ["Eq(7 - 4, 3)", "Eq(Rational(4,7) + Rational(3,7), 1)"]),
                tp("How many $\\frac{1}{5}$ pieces make one whole?",
                   ["$5$", "$1$", "$10$"],
                   "The denominator's promise: five fifths rebuild the whole — $\\frac{5}{5} = 1$.",
                   ["Eq(5*Rational(1,5), 1)"]),
            ]),
            tapq("The equal-parts rule", "A circle is cut into $4$ parts of DIFFERENT sizes, and one part is shaded. Is the shaded amount $\\frac{1}{4}$?",
                 ["no — fractions need EQUAL parts",
                  "yes — one of four parts is always a quarter",
                  "yes, if the shaded part is the biggest",
                  "only on a number line"],
                 "The denominator names a piece SIZE, and that only means something when all pieces share it. One unequal part of four could be almost anything — the word \"quarter\" would lie. (With equal parts, $4 \\times \\frac{1}{4} = 1$.)",
                 ["Eq(4*Rational(1,4), 1)"]),
            funfact("Fractions are older than the alphabet",
                    "Egyptian scribes four thousand years ago wrote almost everything using UNIT fractions — amounts like $\\frac{2}{5}$ had to be expressed as sums such as $\\frac{1}{3} + \\frac{1}{15}$. Check it: that sum really is $\\frac{2}{5}$. Your notation is friendlier — but the unit-fraction atoms are the same ones."),
            teach("Concept B", "Sets and the number line", [
                "Fractions measure SETS too: $\\frac{3}{4}$ of $12$ apples — split the set into $4$ equal groups ($3$ each), take $3$ groups: $9$ apples.",
                "And fractions are POINTS: on the number line, $\\frac{3}{4}$ lives between $0$ and $1$ — split the unit into four, count three marks.",
                "One notation, three pictures — shape, set, point. The denominator names the split in all three.",
            ]),
            workedset("Fractions of sets",
                      "Split into denominator-many groups; take numerator-many.", [
                wex("Find $\\frac{3}{4}$ of $12$.",
                    ["Four equal groups: $12 \\div 4 = 3$ each.",
                     "Take three groups: $9$."],
                    "$9$",
                    ["Eq(Rational(3,4)*12, 9)"]),
                wex("Find $\\frac{2}{3}$ of $18$.",
                    ["Three equal groups of $6$; take two.",
                     "$\\frac{2}{3}$ of $18 = 12$."],
                    "$12$",
                    ["Eq(Rational(18,3), 6)", "Eq(Rational(2,3)*18, 12)"]),
            ]),
            tryitset("Of a set, on a line", "Groups for sets; marks for lines.", [
                tp("$\\frac{2}{5}$ of $20$ equals:",
                   ["$8$", "$4$", "$10$"],
                   "Five groups of $4$; take two: $8$.",
                   ["Eq(Rational(2,5)*20, 8)"]),
                tp("$\\frac{3}{8}$ of $24$ equals:",
                   ["$9$", "$8$", "$12$"],
                   "Eight groups of $3$; take three: $9$.",
                   ["Eq(Rational(3,8)*24, 9)"]),
                tp("On a number line from $0$ to $1$ split into sixths, the point $\\frac{5}{6}$ sits:",
                   ["one mark before $1$", "one mark after $0$", "exactly at the middle"],
                   "Five of the six marks along: one short of the whole — $\\frac{5}{6} + \\frac{1}{6} = 1$.",
                   ["Eq(Rational(5,6) + Rational(1,6), 1)", "Rational(5,6) < 1"]),
            ]),
            tapq("Which picture?", "$\\frac{3}{4}$ of $12$ students wear deel. How many students is that?",
                 ["$9$", "$3$", "$4$", "$12$"],
                 "Split $12$ into four equal groups of $3$; three groups wear deel: $9$ students.",
                 ["Eq(Rational(3,4)*12, 9)"]),
            recap([
                "Denominator names the piece size (equal parts per whole); numerator counts pieces.",
                "Unit fractions are the atoms; all the pieces together make exactly 1.",
                "Fractions of a set: split into denominator-many groups, take numerator-many.",
                "On the number line a fraction is a point — split the unit, count the marks.",
                "No equal parts, no fraction — the equal-parts rule is the foundation.",
            ]),
            tip("Mixed pictures below — shapes, sets, and number lines. Say the piece's NAME (sixths, eighths...) before answering each."),
            tryitset("Mixed practice", "All three pictures of a fraction.", [
                tp("A chocolate bar of $10$ equal squares: you eat $7$. Fraction remaining:",
                   ["$\\frac{3}{10}$", "$\\frac{7}{10}$", "$\\frac{3}{7}$"],
                   "$10 - 7 = 3$ squares of the tenth size remain: $\\frac{3}{10}$.",
                   ["Eq(Rational(7,10) + Rational(3,10), 1)"]),
                tp("$\\frac{4}{6}$ of $30$ equals:",
                   ["$20$", "$24$", "$5$"],
                   "Six groups of $5$; take four: $20$.",
                   ["Eq(Rational(4,6)*30, 20)"]),
                tp("How many $\\frac{1}{12}$ pieces make one whole?",
                   ["$12$", "$6$", "$1$"],
                   "Twelve twelfths: $\\frac{12}{12} = 1$.",
                   ["Eq(12*Rational(1,12), 1)"]),
                tp("What fraction of a metre is $30$ cm?",
                   ["$\\frac{30}{100}$", "$\\frac{100}{30}$", "$\\frac{30}{60}$"],
                   "A metre is $100$ cm; each cm is $\\frac{1}{100}$ of it: $\\frac{30}{100}$ (soon you'll also call it $\\frac{3}{10}$).",
                   ["Eq(Rational(30,100), Rational(3,10))"]),
                tp("A garden is split into $8$ equal beds, $8$ flowers in each. Roses fill $\\frac{5}{8}$ of the garden. How many flowers are roses?",
                   ["$40$", "$64$", "$13$"],
                   "Five of the eight beds are roses: $5 \\times 8 = 40$ flowers — which is exactly $\\frac{5}{8}$ of the garden's $64$.",
                   ["Eq(5*8, 40)", "Eq(Rational(5,8)*64, 40)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"What a Fraction Is\"",
                    "One notation, three pictures — and the equal-parts rule underneath them all. Next: the surprising fact that one amount wears MANY fraction names, and how to switch between them.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Equivalent Fractions
# ==========================================================================

def lesson_equivalent():
    return {
        "slug": "equivalent-fractions",
        "title": "Equivalent Fractions",
        "concreteComparison": (
            "Half a bread is half a bread — whether you cut that half "
            "into $2$ quarters, $3$ sixths, or $4$ eighths. "
            "$\\frac{1}{2}$, $\\frac{2}{4}$, $\\frac{3}{6}$, "
            "$\\frac{4}{8}$: four names, one amount. Splitting every "
            "piece into smaller ones changes the NUMBERS but not the "
            "bread — and that's the whole secret of equivalent "
            "fractions."),
        "objective": (
            "Make equivalent fractions by multiplying or dividing the "
            "numerator and denominator by the same number, and reduce a "
            "fraction to simplest form."),
        "concept": [
            "**Split every piece the same way.** Cut each half into $3$: "
            "the $1$ half becomes $3$ pieces, the $2$-per-whole becomes "
            "$6$-per-whole — $\\frac{1}{2} = \\frac{3}{6}$. Numerator "
            "and denominator both got multiplied by $3$, and the amount "
            "never moved.",
            "**Merging runs it backwards.** If numerator and denominator "
            "share a factor, glue that many small pieces into one big "
            "one: $\\frac{9}{12}$ — divide both by $3$ — is "
            "$\\frac{3}{4}$. Same amount, chunkier pieces.",
            "**Simplest form** is the fully-merged name: numerator and "
            "denominator share no factor but $1$. Every fraction has "
            "exactly one simplest name — $\\frac{9}{12}$, "
            "$\\frac{6}{8}$, $\\frac{75}{100}$ all answer to "
            "$\\frac{3}{4}$.",
        ],
        "keyIdea": (
            "Multiply or divide top AND bottom by the same number and "
            "the amount doesn't move — only its name changes. The "
            "simplest name is the one with nothing left to divide."),
        "facts": [
            {"title": "The splitting move",
             "latex": "\\frac{1}{2} = \\frac{1 \\times 3}{2 \\times 3} = \\frac{3}{6}",
             "explanation": "Same amount, finer pieces — top and bottom scale together."},
            {"title": "The merging move",
             "latex": "\\frac{9}{12} = \\frac{9 \\div 3}{12 \\div 3} = \\frac{3}{4}",
             "explanation": "Divide out the shared factor; the fully-merged name is simplest form."},
        ],
        "workedExamples": [
            {"id": "g5fr-l2-we1",
             "statement": "Fill the blank: $\\frac{2}{3} = \\frac{\\square}{12}$.",
             "note": "What multiplied the 3 into 12? The top gets the same.",
             "solution": ("$3 \\times 4 = 12$, so the numerator scales by $4$ too: "
                          "$2 \\times 4 = 8$. $\\frac{2}{3} = \\frac{8}{12}$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*4, 12)", "Eq(2*4, 8)", "Eq(Rational(2,3), Rational(8,12))"]},
            {"id": "g5fr-l2-we2",
             "statement": "Write $\\frac{18}{24}$ in simplest form.",
             "note": "Hunt the biggest shared factor.",
             "solution": ("$18$ and $24$ share the factor $6$: divide both — "
                          "$\\frac{18 \\div 6}{24 \\div 6} = \\frac{3}{4}$. Nothing "
                          "but $1$ divides both $3$ and $4$, so $\\frac{3}{4}$ is "
                          "the simplest name."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(18,6), 3)", "Eq(Rational(24,6), 4)",
                       "Eq(Rational(18,24), Rational(3,4))"]},
        ],
        "commonMistakes": [
            {"text": "Adding the same number to top and bottom — 1/2 = 2/3 \"because I added 1 to both\".",
             "correction": "Equivalence comes from MULTIPLYING or dividing both, never adding. Adding 1 to both moves the amount: 1/2 ≠ 2/3 (a half is less than two-thirds).",
             "authored": True},
            {"text": "Stopping the simplification early — calling 12/16 \"simplified\" as 6/8.",
             "correction": "6 and 8 still share a 2: keep dividing until the only shared factor is 1. 12/16 = 6/8 = 3/4 — simplest form is the END of the road.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5fr-l2-t1",
             "statement": "Fill the blank: $\\frac{3}{5} = \\frac{\\square}{20}$.",
             "solution": "$5 \\times 4 = 20$, so the top scales by $4$: $\\frac{12}{20}$.",
             "check": ["Eq(Rational(3,5), Rational(12,20))"]},
            {"id": "g5fr-l2-t2",
             "statement": "Write $\\frac{45}{60}$ in simplest form.",
             "solution": "Divide both by $15$: $\\frac{3}{4}$. (Or by $5$ then $3$ — the road doesn't matter, the end does.)",
             "check": ["Eq(Rational(45,60), Rational(3,4))"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Split the pieces, keep the amount", [
                "Cut every piece of $\\frac{1}{2}$ into three: now there are $3$ pieces of the $6$-per-whole size — $\\frac{1}{2} = \\frac{3}{6}$. The bread never moved.",
                "The rule underneath: multiply numerator AND denominator by the same number. $\\frac{1 \\times 3}{2 \\times 3} = \\frac{3}{6}$.",
                "It must be the SAME number top and bottom — that's what keeps the splitting honest.",
            ]),
            workedset("Scaling up",
                      "Find what scaled the denominator; scale the numerator to match.", [
                wex("Fill the blank: $\\frac{2}{3} = \\frac{\\square}{12}$.",
                    ["$3 \\to 12$ is $\\times 4$; the top follows: $2 \\times 4 = 8$.",
                     "$\\frac{2}{3} = \\frac{8}{12}$."],
                    "$8$",
                    ["Eq(Rational(2,3), Rational(8,12))"]),
                wex("Give three names for $\\frac{3}{4}$.",
                    ["$\\times 2$: $\\frac{6}{8}$. $\\times 3$: $\\frac{9}{12}$. $\\times 25$: $\\frac{75}{100}$.",
                     "Four names, one amount."],
                    "$\\frac{6}{8}, \\frac{9}{12}, \\frac{75}{100}$",
                    ["Eq(Rational(3,4), Rational(6,8))", "Eq(Rational(3,4), Rational(9,12))",
                     "Eq(Rational(3,4), Rational(75,100))"]),
            ]),
            tryitset("Scale to match", "Same multiplier, top and bottom.", [
                tp("$\\frac{3}{5} = \\frac{\\square}{20}$. The blank is:",
                   ["$12$", "$18$", "$15$"],
                   "$5 \\to 20$ is $\\times 4$: top becomes $12$.",
                   ["Eq(Rational(3,5), Rational(12,20))"]),
                tp("$\\frac{5}{6} = \\frac{35}{\\square}$. The blank is:",
                   ["$42$", "$36$", "$40$"],
                   "$5 \\to 35$ is $\\times 7$: bottom becomes $42$.",
                   ["Eq(Rational(5,6), Rational(35,42))"]),
                tp("Which fraction is NOT equal to $\\frac{1}{2}$?",
                   ["$\\frac{5}{12}$", "$\\frac{6}{12}$", "$\\frac{50}{100}$"],
                   "$\\frac{6}{12}$ and $\\frac{50}{100}$ both merge back to $\\frac{1}{2}$; $\\frac{5}{12}$ falls short of it.",
                   ["Eq(Rational(6,12), Rational(1,2))", "Eq(Rational(50,100), Rational(1,2))",
                    "Rational(5,12) < Rational(1,2)"]),
            ]),
            tapq("The forbidden move", "A student writes $\\frac{1}{2} = \\frac{2}{3}$ \"because I added $1$ to the top and bottom\". This is:",
                 ["wrong — equivalence multiplies, never adds",
                  "right — same change, same fraction",
                  "right only for small numbers",
                  "wrong only because he added 1"],
                 "Adding moves the amount: $\\frac{1}{2}$ is genuinely less than $\\frac{2}{3}$. Only MULTIPLYING (or dividing) both keeps the bread in place.",
                 ["Rational(1,2) < Rational(2,3)"]),
            funfact("Why 75/100 shows up everywhere",
                    "Percent is just an equivalent-fraction convention: every amount renamed with denominator $100$. \"$75\\%$\" IS $\\frac{75}{100}$, which is $\\frac{3}{4}$ in simplest form. When you meet percents next year, you already know the whole trick."),
            teach("Concept B", "Merging, and the simplest name", [
                "Run the splitting backwards: if top and bottom share a factor, DIVIDE it out — merge small pieces into big ones. $\\frac{9}{12} \\to \\frac{3}{4}$ (divide by $3$).",
                "Keep merging until nothing but $1$ divides both — that's SIMPLEST FORM, the fraction's shortest name.",
                "Any road works: $\\frac{12}{16} \\to \\frac{6}{8} \\to \\frac{3}{4}$, or straight there dividing by $4$. The end is the same because the simplest name is unique.",
            ]),
            workedset("Down to simplest form",
                      "Divide out shared factors until none remain.", [
                wex("Simplify $\\frac{18}{24}$.",
                    ["Both share $6$: $\\frac{18}{24} = \\frac{3}{4}$.",
                     "$3$ and $4$ share only $1$ — done."],
                    "$\\frac{3}{4}$",
                    ["Eq(Rational(18,24), Rational(3,4))"]),
                wex("Simplify $\\frac{45}{60}$.",
                    ["By $5$: $\\frac{9}{12}$. By $3$: $\\frac{3}{4}$.",
                     "(Or by $15$ in one hop — same destination.)"],
                    "$\\frac{3}{4}$",
                    ["Eq(Rational(45,60), Rational(3,4))", "Eq(Rational(9,12), Rational(3,4))"]),
            ]),
            tryitset("Simplest form", "Merge until only 1 divides both.", [
                tp("$\\frac{16}{20}$ in simplest form is:",
                   ["$\\frac{4}{5}$", "$\\frac{8}{10}$", "$\\frac{2}{3}$"],
                   "Divide both by $4$: $\\frac{4}{5}$. ($\\frac{8}{10}$ merges only halfway.)",
                   ["Eq(Rational(16,20), Rational(4,5))", "Eq(Rational(8,10), Rational(4,5))"]),
                tp("$\\frac{35}{50}$ in simplest form is:",
                   ["$\\frac{7}{10}$", "$\\frac{5}{7}$", "$\\frac{35}{50}$"],
                   "Divide both by $5$: $\\frac{7}{10}$ — and $7, 10$ share nothing more.",
                   ["Eq(Rational(35,50), Rational(7,10))"]),
                tp("Which is already in simplest form?",
                   ["$\\frac{8}{15}$", "$\\frac{9}{12}$", "$\\frac{10}{25}$"],
                   "$8$ and $15$ share only $1$. The others still merge: $\\frac{9}{12} = \\frac{3}{4}$, $\\frac{10}{25} = \\frac{2}{5}$.",
                   ["Eq(Rational(9,12), Rational(3,4))", "Eq(Rational(10,25), Rational(2,5))"]),
            ]),
            tapq("Halfway is not done", "A student simplifies $\\frac{12}{16}$ to $\\frac{6}{8}$ and stops. The finished answer is:",
                 ["$\\frac{3}{4}$ — $6$ and $8$ still share a $2$",
                  "$\\frac{6}{8}$ — one division is enough",
                  "$\\frac{12}{16}$ — it was fine as it was",
                  "$\\frac{2}{4}$"],
                 "Simplest form is the END of the merging road: $\\frac{6}{8}$ still divides by $2$ to $\\frac{3}{4}$, and there the road ends.",
                 ["Eq(Rational(12,16), Rational(3,4))", "Eq(Rational(6,8), Rational(3,4))"]),
            recap([
                "Multiply top AND bottom by the same number: finer pieces, same amount.",
                "Divide out shared factors: chunkier pieces, same amount.",
                "Adding to top and bottom moves the amount — the forbidden move.",
                "Simplest form = nothing but 1 divides both; every fraction has exactly one.",
            ]),
            tip("For each item, say which move you're using — splitting (×) or merging (÷) — before touching the numbers."),
            tryitset("Mixed practice", "Both moves, in both directions.", [
                tp("$\\frac{4}{9} = \\frac{\\square}{36}$. The blank is:",
                   ["$16$", "$12$", "$18$"],
                   "$9 \\to 36$ is $\\times 4$: top becomes $16$.",
                   ["Eq(Rational(4,9), Rational(16,36))"]),
                tp("$\\frac{24}{36}$ in simplest form is:",
                   ["$\\frac{2}{3}$", "$\\frac{4}{6}$", "$\\frac{6}{9}$"],
                   "Divide both by $12$: $\\frac{2}{3}$. The other options merge only partway.",
                   ["Eq(Rational(24,36), Rational(2,3))", "Eq(Rational(4,6), Rational(2,3))"]),
                tp("$\\frac{45}{60}$ of an hour is the same as:",
                   ["$\\frac{3}{4}$ of an hour", "$\\frac{4}{5}$ of an hour", "$\\frac{2}{3}$ of an hour"],
                   "$\\frac{45}{60}$ merges by $15$ to $\\frac{3}{4}$ — the $45$-minute mark.",
                   ["Eq(Rational(45,60), Rational(3,4))"]),
                tp("Which pair are two names for one amount?",
                   ["$\\frac{6}{10}$ and $\\frac{9}{15}$", "$\\frac{2}{5}$ and $\\frac{3}{5}$", "$\\frac{1}{3}$ and $\\frac{3}{1}$"],
                   "Both merge to $\\frac{3}{5}$: $\\frac{6}{10} = \\frac{9}{15} = \\frac{3}{5}$.",
                   ["Eq(Rational(6,10), Rational(3,5))", "Eq(Rational(9,15), Rational(3,5))"]),
                tp("$\\frac{100}{100}$ equals:",
                   ["$1$", "$100$", "$\\frac{1}{100}$"],
                   "All the pieces together: one whole — however fine the cut.",
                   ["Eq(Rational(100,100), 1)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Equivalent Fractions\"",
                    "Splitting and merging — the two moves that let one amount wear many names — power everything ahead: comparing fractions and (next year) adding ones with different denominators. Next: which of two fractions is bigger?",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Comparing Fractions
# ==========================================================================

def lesson_comparing():
    return {
        "slug": "comparing-fractions",
        "title": "Comparing Fractions",
        "concreteComparison": (
            "Who ate more bread: you with $\\frac{3}{5}$ of yours, or "
            "your friend with $\\frac{3}{8}$ of hers? Same COUNT of "
            "pieces — three — but your pieces are fifths and hers are "
            "eighths, and fifths are bigger (fewer pieces make the "
            "whole). Three big pieces beat three small ones. Comparing "
            "fractions is always about piece size versus piece count."),
        "objective": (
            "Compare fractions with the same denominator, the same "
            "numerator, and using the benchmarks one-half and one — "
            "choosing the fastest strategy each time."),
        "concept": [
            "**Same denominator: count wins.** Pieces are the same size, "
            "so more pieces is more: $\\frac{5}{8} > \\frac{3}{8}$.",
            "**Same numerator: piece size wins — backwards.** A bigger "
            "denominator means MORE pieces per whole, so each is "
            "SMALLER: $\\frac{3}{5} > \\frac{3}{8}$, because fifths "
            "beat eighths.",
            "**Different everything: use a benchmark.** Is each "
            "fraction more or less than $\\frac{1}{2}$? $\\frac{4}{9}$ "
            "is under half ($4$ is less than half of $9$), $\\frac{5}{8}$ "
            "is over half ($5$ is more than half of $8$): so "
            "$\\frac{4}{9} < \\frac{5}{8}$ without any common name.",
        ],
        "keyIdea": (
            "Same-size pieces: count them. Same count: bigger "
            "denominator means smaller pieces. Neither: park each "
            "fraction against one-half or one, and compare the parks."),
        "facts": [
            {"title": "Same numerator flips",
             "latex": "\\frac{3}{5} > \\frac{3}{8}",
             "explanation": "More pieces per whole = smaller pieces — the denominator compares backwards."},
            {"title": "The half benchmark",
             "latex": "\\frac{4}{9} < \\frac{1}{2} < \\frac{5}{8}",
             "explanation": "Double the numerator against the denominator: 8 < 9 (under half); 10 > 8 (over half)."},
        ],
        "workedExamples": [
            {"id": "g5fr-l3-we1",
             "statement": "Compare $\\frac{3}{5}$ and $\\frac{3}{8}$.",
             "note": "Same count — so compare the piece sizes.",
             "solution": ("Both are three pieces, but fifths are bigger than "
                          "eighths ($5$ pieces per whole against $8$). Three big "
                          "beats three small: $\\frac{3}{5} > \\frac{3}{8}$."),
             "badges": [{"text": "core"}],
             "check": ["Rational(3,5) > Rational(3,8)"]},
            {"id": "g5fr-l3-we2",
             "statement": "Compare $\\frac{4}{9}$ and $\\frac{5}{8}$ using the half benchmark.",
             "note": "Neither denominators nor numerators match — park each against 1/2.",
             "solution": ("$\\frac{4}{9}$: half of $9$ is $4\\frac{1}{2}$, and $4$ "
                          "falls short — under half. $\\frac{5}{8}$: half of $8$ is "
                          "$4$, and $5$ exceeds it — over half. Under beats over... "
                          "the other way: $\\frac{4}{9} < \\frac{1}{2} < "
                          "\\frac{5}{8}$."),
             "badges": [{"text": "core"}],
             "check": ["Rational(4,9) < Rational(1,2)", "Rational(5,8) > Rational(1,2)",
                       "Rational(4,9) < Rational(5,8)"]},
        ],
        "commonMistakes": [
            {"text": "Bigger denominator = bigger fraction — reading 3/8 > 3/5 because 8 > 5.",
             "correction": "The denominator counts pieces PER WHOLE: more pieces means each is smaller. With equal numerators the bigger denominator LOSES.",
             "authored": True},
            {"text": "Comparing numerators across different denominators — 5/9 > 4/5 \"because 5 > 4\".",
             "correction": "Five small pieces can be less than four big ones: 5/9 is barely over half while 4/5 is nearly whole. Match the pieces (or benchmark) before counting.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5fr-l3-t1",
             "statement": "Order from smallest to largest: $\\frac{5}{8}, \\frac{3}{8}, \\frac{7}{8}$.",
             "solution": "Same pieces — count them: $\\frac{3}{8} < \\frac{5}{8} < \\frac{7}{8}$.",
             "check": ["Rational(3,8) < Rational(5,8)", "Rational(5,8) < Rational(7,8)"]},
            {"id": "g5fr-l3-t2",
             "statement": "Which is bigger: $\\frac{7}{12}$ or $\\frac{5}{11}$?",
             "solution": "Benchmark: $\\frac{7}{12}$ is over half ($14 > 12$), $\\frac{5}{11}$ is under half ($10 < 11$): $\\frac{7}{12} > \\frac{5}{11}$.",
             "check": ["Rational(7,12) > Rational(1,2)", "Rational(5,11) < Rational(1,2)",
                       "Rational(7,12) > Rational(5,11)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Count, or size — never both blindly", [
                "Same DENOMINATOR: the pieces match, so the count decides — $\\frac{5}{8} > \\frac{3}{8}$.",
                "Same NUMERATOR: the counts match, so piece size decides — and it compares BACKWARDS: $\\frac{3}{5} > \\frac{3}{8}$, because a whole cut into five gives bigger pieces than one cut into eight.",
                "The backwards rule surprises everyone once: more pieces per whole = smaller pieces. Say it until it stops surprising.",
            ]),
            workedset("Matching pieces or matching counts",
                      "Spot which part matches; the other part decides.", [
                wex("Compare $\\frac{3}{5}$ and $\\frac{3}{8}$.",
                    ["Same count (three), different sizes: fifths beat eighths.",
                     "$\\frac{3}{5} > \\frac{3}{8}$."],
                    "$\\frac{3}{5} > \\frac{3}{8}$",
                    ["Rational(3,5) > Rational(3,8)"]),
                wex("Order $\\frac{5}{8}, \\frac{3}{8}, \\frac{7}{8}$.",
                    ["Same pieces — pure counting.",
                     "$\\frac{3}{8} < \\frac{5}{8} < \\frac{7}{8}$."],
                    "$\\frac{3}{8} < \\frac{5}{8} < \\frac{7}{8}$",
                    ["Rational(3,8) < Rational(5,8)", "Rational(5,8) < Rational(7,8)"]),
            ]),
            tryitset("Match and compare", "Which part matches? The other decides.", [
                tp("Which is larger: $\\frac{4}{7}$ or $\\frac{6}{7}$?",
                   ["$\\frac{6}{7}$", "$\\frac{4}{7}$", "they are equal"],
                   "Same sevenths — more of them wins: $\\frac{6}{7}$.",
                   ["Rational(6,7) > Rational(4,7)"]),
                tp("Which is larger: $\\frac{2}{3}$ or $\\frac{2}{9}$?",
                   ["$\\frac{2}{3}$", "$\\frac{2}{9}$", "they are equal"],
                   "Same count, different sizes: thirds are three-per-whole, ninths nine-per-whole — thirds are bigger.",
                   ["Rational(2,3) > Rational(2,9)"]),
                tp("Which is SMALLEST: $\\frac{5}{6}, \\frac{5}{9}, \\frac{5}{12}$?",
                   ["$\\frac{5}{12}$", "$\\frac{5}{6}$", "$\\frac{5}{9}$"],
                   "Five pieces each — the finest cut (twelfths) gives the smallest pieces: $\\frac{5}{12}$.",
                   ["Rational(5,12) < Rational(5,9)", "Rational(5,9) < Rational(5,6)"]),
            ]),
            tapq("The backwards rule", "$\\frac{1}{10}$ compared with $\\frac{1}{4}$:",
                 ["$\\frac{1}{10} < \\frac{1}{4}$ — tenths are smaller pieces",
                  "$\\frac{1}{10} > \\frac{1}{4}$ — ten beats four",
                  "equal — both are one piece",
                  "cannot compare"],
                 "One piece each, but a whole cut into ten gives far smaller pieces than one cut into four. The denominator compares backwards.",
                 ["Rational(1,10) < Rational(1,4)"]),
            funfact("The quarter-pound lesson",
                    "A famous marketing failure: a chain sold third-pound burgers against quarter-pounders at the same price — and customers refused, reasoning that $3 < 4$ meant less meat. The backwards rule in the wild: $\\frac{1}{3}$ of a pound is MORE than $\\frac{1}{4}$."),
            teach("Concept B", "Benchmarks — park against a half", [
                "Different numerators AND denominators? Park each fraction against $\\frac{1}{2}$: double the numerator and compare with the denominator. $\\frac{4}{9}$: $8 < 9$ — under half. $\\frac{5}{8}$: $10 > 8$ — over half.",
                "Under beats over is settled instantly: $\\frac{4}{9} < \\frac{5}{8}$, no common name needed.",
                "The other great benchmark is $1$: $\\frac{7}{8}$ misses one whole by a thin $\\frac{1}{8}$, while $\\frac{5}{4}$ has already passed it.",
            ]),
            workedset("Benchmark comparisons",
                      "Double the top; compare with the bottom.", [
                wex("Compare $\\frac{4}{9}$ and $\\frac{5}{8}$.",
                    ["$\\frac{4}{9}$: doubled top $8 < 9$ — under half.",
                     "$\\frac{5}{8}$: doubled top $10 > 8$ — over half.",
                     "$\\frac{4}{9} < \\frac{5}{8}$."],
                    "$\\frac{4}{9} < \\frac{5}{8}$",
                    ["Rational(4,9) < Rational(5,8)"]),
                wex("Compare $\\frac{7}{12}$ and $\\frac{5}{11}$.",
                    ["$\\frac{7}{12}$: $14 > 12$ — over half. $\\frac{5}{11}$: $10 < 11$ — under half.",
                     "$\\frac{7}{12} > \\frac{5}{11}$."],
                    "$\\frac{7}{12} > \\frac{5}{11}$",
                    ["Rational(7,12) > Rational(5,11)"]),
            ]),
            tryitset("Park and decide", "Half and one — the two great landmarks.", [
                tp("$\\frac{3}{7}$ against $\\frac{1}{2}$:",
                   ["under — $6 < 7$", "over — $3 > 2$", "exactly half"],
                   "Double the top: $6$, against the bottom $7$ — falls short: under half.",
                   ["Rational(3,7) < Rational(1,2)"]),
                tp("Which is bigger: $\\frac{5}{9}$ or $\\frac{3}{8}$?",
                   ["$\\frac{5}{9}$ — over half beats under half", "$\\frac{3}{8}$", "they are equal"],
                   "$\\frac{5}{9}$: $10 > 9$, over. $\\frac{3}{8}$: $6 < 8$, under. Done.",
                   ["Rational(5,9) > Rational(1,2)", "Rational(3,8) < Rational(1,2)",
                    "Rational(5,9) > Rational(3,8)"]),
                tp("Which sits CLOSEST to $1$: $\\frac{7}{8}, \\frac{2}{3}, \\frac{5}{6}$?",
                   ["$\\frac{7}{8}$ — only $\\frac{1}{8}$ short", "$\\frac{2}{3}$", "$\\frac{5}{6}$"],
                   "Their gaps to $1$: $\\frac{1}{8}, \\frac{1}{3}, \\frac{1}{6}$ — and eighths are the smallest gap (backwards rule again).",
                   ["Rational(1,8) < Rational(1,6)", "Rational(1,6) < Rational(1,3)",
                    "Rational(7,8) > Rational(5,6)"]),
            ]),
            tapq("Numerals lie across sizes", "$\\frac{5}{9}$ or $\\frac{4}{5}$ — a student picks $\\frac{5}{9}$ \"because $5 > 4$\". The truth:",
                 ["$\\frac{4}{5} > \\frac{5}{9}$ — four big pieces beat five small ones",
                  "the student is right",
                  "they are equal",
                  "neither can be compared"],
                 "$\\frac{4}{5}$ is one small fifth short of a whole; $\\frac{5}{9}$ barely clears half. Counting numerators across different piece sizes is the classic trap.",
                 ["Rational(4,5) > Rational(5,9)", "Rational(5,9) > Rational(1,2)"]),
            recap([
                "Same denominator: more pieces wins.",
                "Same numerator: bigger denominator = smaller pieces — the backwards rule.",
                "Benchmarks: double the top against the bottom for the half test; measure gaps to 1.",
                "Never compare bare numerators across different piece sizes.",
            ]),
            tip("Name your strategy before each answer — same-pieces, same-count, or benchmark. The naming is faster than any computation."),
            tryitset("Mixed practice", "Pick the fastest road each time.", [
                tp("Which symbol fits: $\\frac{7}{10} \\;\\square\\; \\frac{9}{10}$?",
                   ["$<$", "$>$", "$=$"],
                   "Same tenths: $7 < 9$.",
                   ["Rational(7,10) < Rational(9,10)"]),
                tp("Which symbol fits: $\\frac{4}{5} \\;\\square\\; \\frac{4}{11}$?",
                   ["$>$", "$<$", "$=$"],
                   "Same count — fifths beat elevenths: $>$.",
                   ["Rational(4,5) > Rational(4,11)"]),
                tp("Which is bigger: $\\frac{6}{11}$ or $\\frac{4}{9}$?",
                   ["$\\frac{6}{11}$", "$\\frac{4}{9}$", "they are equal"],
                   "Half test: $12 > 11$ (over) against $8 < 9$ (under).",
                   ["Rational(6,11) > Rational(1,2)", "Rational(4,9) < Rational(1,2)"]),
                tp("Order smallest to largest: $\\frac{1}{2}, \\frac{3}{8}, \\frac{3}{4}$.",
                   ["$\\frac{3}{8} < \\frac{1}{2} < \\frac{3}{4}$",
                    "$\\frac{1}{2} < \\frac{3}{8} < \\frac{3}{4}$",
                    "$\\frac{3}{8} < \\frac{3}{4} < \\frac{1}{2}$"],
                   "$\\frac{3}{8}$ is under half ($6 < 8$), $\\frac{3}{4}$ is over ($6 > 4$).",
                   ["Rational(3,8) < Rational(1,2)", "Rational(1,2) < Rational(3,4)"]),
                tp("Two runners finish $\\frac{5}{6}$ and $\\frac{7}{9}$ of the same trail. Who ran further?",
                   ["the first — $\\frac{5}{6} > \\frac{7}{9}$", "the second", "equal distances"],
                   "Gaps to the finish: $\\frac{1}{6}$ against $\\frac{2}{9}$ — and $\\frac{1}{6} = \\frac{3}{18}$ is less than $\\frac{2}{9} = \\frac{4}{18}$: the first is closer to done.",
                   ["Rational(5,6) > Rational(7,9)", "Eq(1 - Rational(5,6), Rational(1,6))",
                    "Eq(1 - Rational(7,9), Rational(2,9))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Comparing Fractions\"",
                    "Count against size, and two great landmarks — that's the whole comparing toolkit. Next: fractions that outgrow the whole, and the two names they answer to.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Improper Fractions & Mixed Numbers
# ==========================================================================

def lesson_mixed():
    return {
        "slug": "improper-fractions-and-mixed-numbers",
        "title": "Improper Fractions & Mixed Numbers",
        "concreteComparison": (
            "Seven guests each take a third of a bread. You need seven "
            "thirds — $\\frac{7}{3}$ — which is more than two whole "
            "breads and a piece besides. The SAME amount has two "
            "honest names: $\\frac{7}{3}$ (count the pieces) and "
            "$2\\frac{1}{3}$ (count the wholes, then the leftover). "
            "Switching between the names is division you already know."),
        "objective": (
            "Read improper fractions and mixed numbers as two names for "
            "one amount, and convert both ways using division with "
            "remainders."),
        "concept": [
            "**Top-heavy fractions pass the whole.** When the numerator "
            "reaches the denominator you have exactly $1$; beyond it "
            "you're past a whole — $\\frac{7}{3}$ is more than $2$ but "
            "less than $3$. These are IMPROPER fractions (nothing wrong "
            "with them — just top-heavy).",
            "**Improper → mixed is division.** $\\frac{7}{3}$: divide — "
            "$7 \\div 3 = 2$ r $1$. Two wholes, one third left: "
            "$2\\frac{1}{3}$. The remainder keeps its denominator.",
            "**Mixed → improper multiplies back.** $3\\frac{2}{5}$: "
            "each whole is $\\frac{5}{5}$, so three wholes are "
            "$\\frac{15}{5}$, plus the $\\frac{2}{5}$: $\\frac{17}{5}$ "
            "— the division receipt $3 \\times 5 + 2 = 17$ in fraction "
            "clothes.",
        ],
        "keyIdea": (
            "Improper fractions and mixed numbers are two names for one "
            "amount, and division with remainders converts between "
            "them: quotient = wholes, remainder = the leftover pieces."),
        "facts": [
            {"title": "Improper to mixed",
             "latex": "\\frac{7}{3} = 2\\frac{1}{3} \\quad (7 \\div 3 = 2 \\text{ r } 1)",
             "explanation": "Quotient counts the wholes; the remainder keeps its denominator."},
            {"title": "Mixed to improper",
             "latex": "3\\frac{2}{5} = \\frac{3 \\times 5 + 2}{5} = \\frac{17}{5}",
             "explanation": "Wholes times pieces-per-whole, plus the loose pieces — the receipt, refolded."},
        ],
        "workedExamples": [
            {"id": "g5fr-l4-we1",
             "statement": "Write $\\frac{23}{6}$ as a mixed number.",
             "note": "Divide; the remainder keeps the denominator.",
             "solution": ("$23 \\div 6 = 3$ r $5$: three wholes and five sixths — "
                          "$3\\frac{5}{6}$. Receipt: $3 \\times 6 + 5 = 23$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*6 + 5, 23)", "Eq(Rational(23,6), 3 + Rational(5,6))"]},
            {"id": "g5fr-l4-we2",
             "statement": "Write $4\\frac{3}{8}$ as an improper fraction.",
             "note": "Wholes become eighths first.",
             "solution": ("Four wholes are $4 \\times 8 = 32$ eighths; add the three "
                          "loose ones: $\\frac{35}{8}$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*8 + 3, 35)", "Eq(4 + Rational(3,8), Rational(35,8))"]},
        ],
        "commonMistakes": [
            {"text": "Dropping the remainder's denominator — writing 23/6 as \"3 r 5\" or \"3.5\".",
             "correction": "The leftover is five SIXTHS: 3 5/6. The remainder is a fraction with the same denominator, not a decimal and not a bare number.",
             "authored": True},
            {"text": "Adding wholes to the numerator without scaling — 4 3/8 = 7/8.",
             "correction": "A whole is EIGHT eighths, not one. Four wholes contribute 32 eighths: 4 3/8 = 35/8.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5fr-l4-t1",
             "statement": "Write $\\frac{19}{4}$ as a mixed number.",
             "solution": "$19 \\div 4 = 4$ r $3$: $4\\frac{3}{4}$. Receipt $4 \\times 4 + 3 = 19$ ✓.",
             "check": ["Eq(4*4 + 3, 19)", "Eq(Rational(19,4), 4 + Rational(3,4))"]},
            {"id": "g5fr-l4-t2",
             "statement": "Write $2\\frac{5}{9}$ as an improper fraction.",
             "solution": "Two wholes are $18$ ninths; plus five: $\\frac{23}{9}$.",
             "check": ["Eq(2*9 + 5, 23)", "Eq(2 + Rational(5,9), Rational(23,9))"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Past the whole", [
                "When the numerator reaches the denominator, you hold exactly one whole: $\\frac{3}{3} = 1$. Past it, the fraction is TOP-HEAVY — improper: $\\frac{7}{3}$ is more than $2$, less than $3$.",
                "Its second name counts wholes first: $\\frac{7}{3} = 2\\frac{1}{3}$ — two wholes and a third.",
                "The converter is division with remainders, which you own: $7 \\div 3 = 2$ r $1$ — quotient counts wholes, the remainder keeps its denominator.",
            ]),
            workedset("Improper to mixed",
                      "Divide; wholes from the quotient, pieces from the remainder.", [
                wex("Write $\\frac{23}{6}$ as a mixed number.",
                    ["$23 \\div 6 = 3$ r $5$.",
                     "$3\\frac{5}{6}$; receipt $3 \\times 6 + 5 = 23$ ✓."],
                    "$3\\frac{5}{6}$",
                    ["Eq(Rational(23,6), 3 + Rational(5,6))"]),
                wex("Write $\\frac{19}{4}$ as a mixed number.",
                    ["$19 \\div 4 = 4$ r $3$.",
                     "$4\\frac{3}{4}$ — four wholes, three quarters."],
                    "$4\\frac{3}{4}$",
                    ["Eq(Rational(19,4), 4 + Rational(3,4))"]),
            ]),
            tryitset("Count the wholes", "Divide, then dress the remainder.", [
                tp("$\\frac{11}{4}$ as a mixed number is:",
                   ["$2\\frac{3}{4}$", "$2\\frac{1}{4}$", "$3\\frac{1}{4}$"],
                   "$11 \\div 4 = 2$ r $3$: two wholes and three quarters.",
                   ["Eq(Rational(11,4), 2 + Rational(3,4))"]),
                tp("$\\frac{20}{5}$ equals:",
                   ["$4$ exactly", "$4\\frac{1}{5}$", "$3\\frac{5}{5}$"],
                   "$20 \\div 5 = 4$ with nothing left: four exact wholes.",
                   ["Eq(Rational(20,5), 4)"]),
                tp("$\\frac{31}{7}$ as a mixed number is:",
                   ["$4\\frac{3}{7}$", "$4\\frac{4}{7}$", "$3\\frac{3}{7}$"],
                   "$31 \\div 7 = 4$ r $3$: $4\\frac{3}{7}$; receipt $4 \\times 7 + 3 = 31$ ✓.",
                   ["Eq(4*7 + 3, 31)", "Eq(Rational(31,7), 4 + Rational(3,7))"]),
            ]),
            tapq("Where does it live?", "On the number line, $\\frac{7}{3}$ sits between:",
                 ["$2$ and $3$", "$1$ and $2$", "$0$ and $1$", "$3$ and $4$"],
                 "$\\frac{6}{3} = 2$ and $\\frac{9}{3} = 3$ — seven thirds lands a third past $2$.",
                 ["Rational(7,3) > 2", "Rational(7,3) < 3"]),
            funfact("\"Improper\" is a terrible name",
                    "There is nothing wrong with a top-heavy fraction — mathematicians prefer them, because they add and multiply more cleanly than mixed numbers. The name is a fossil from centuries-old textbooks. Use whichever name serves the moment: mixed to SAY an amount, improper to COMPUTE with it."),
            teach("Concept B", "Mixed to improper — the receipt refolded", [
                "To turn $3\\frac{2}{5}$ improper, turn the wholes into fifths first: each whole is $\\frac{5}{5}$, so three wholes are $\\frac{15}{5}$.",
                "Add the loose pieces: $\\frac{15}{5} + \\frac{2}{5} = \\frac{17}{5}$. In one line: wholes × denominator + numerator, over the same denominator.",
                "That formula IS the division receipt ($3 \\times 5 + 2 = 17$) — the two conversions are one fact, read in both directions.",
            ]),
            workedset("Refolding the receipt",
                      "Wholes × pieces-per-whole + loose pieces.", [
                wex("Write $4\\frac{3}{8}$ as an improper fraction.",
                    ["Four wholes: $4 \\times 8 = 32$ eighths.",
                     "Plus three: $\\frac{35}{8}$."],
                    "$\\frac{35}{8}$",
                    ["Eq(4 + Rational(3,8), Rational(35,8))"]),
                wex("Write $2\\frac{5}{9}$ as an improper fraction.",
                    ["$2 \\times 9 + 5 = 23$.",
                     "$\\frac{23}{9}$."],
                    "$\\frac{23}{9}$",
                    ["Eq(2 + Rational(5,9), Rational(23,9))"]),
            ]),
            tryitset("Make it top-heavy", "Scale the wholes; add the loose pieces.", [
                tp("$5\\frac{1}{2}$ as an improper fraction is:",
                   ["$\\frac{11}{2}$", "$\\frac{6}{2}$", "$\\frac{10}{2}$"],
                   "$5 \\times 2 + 1 = 11$: $\\frac{11}{2}$.",
                   ["Eq(5 + Rational(1,2), Rational(11,2))"]),
                tp("$3\\frac{4}{7}$ as an improper fraction is:",
                   ["$\\frac{25}{7}$", "$\\frac{12}{7}$", "$\\frac{34}{7}$"],
                   "$3 \\times 7 + 4 = 25$: $\\frac{25}{7}$.",
                   ["Eq(3 + Rational(4,7), Rational(25,7))"]),
                tp("Which is LARGER: $2\\frac{3}{4}$ or $\\frac{12}{4}$?",
                   ["$\\frac{12}{4}$ — it is $3$ whole", "$2\\frac{3}{4}$", "they are equal"],
                   "$2\\frac{3}{4} = \\frac{11}{4}$, and $\\frac{12}{4} = 3$: twelve quarters beat eleven.",
                   ["Eq(2 + Rational(3,4), Rational(11,4))", "Rational(12,4) > Rational(11,4)"]),
            ]),
            tapq("The seven-eighths trap", "A student converts $4\\frac{3}{8}$ to $\\frac{7}{8}$ by adding $4 + 3$. The slip:",
                 ["a whole is EIGHT eighths — four wholes contribute $32$, not $4$",
                  "the denominator should change to $12$",
                  "nothing — $\\frac{7}{8}$ is right",
                  "mixed numbers cannot be converted"],
                 "Wholes must be renamed into the piece size first: $4 \\times 8 = 32$ eighths, plus $3$ gives $\\frac{35}{8}$ — an amount past four, while $\\frac{7}{8}$ is less than one.",
                 ["Eq(4 + Rational(3,8), Rational(35,8))", "Rational(7,8) < 1"]),
            recap([
                "Numerator reaches the denominator: exactly one whole; beyond: top-heavy (improper).",
                "Improper → mixed: divide; quotient = wholes, remainder keeps its denominator.",
                "Mixed → improper: wholes × denominator + numerator, same denominator.",
                "Both conversions are one division receipt, read in two directions.",
            ]),
            tip("Convert each one BOTH ways — there and back — and check you return to where you started. Round trips catch every slip."),
            tryitset("Mixed practice", "Two names, full round trips.", [
                tp("$\\frac{17}{5}$ as a mixed number is:",
                   ["$3\\frac{2}{5}$", "$3\\frac{1}{5}$", "$2\\frac{7}{5}$"],
                   "$17 \\div 5 = 3$ r $2$: $3\\frac{2}{5}$. ($2\\frac{7}{5}$ smuggles a whole inside the fraction.)",
                   ["Eq(Rational(17,5), 3 + Rational(2,5))"]),
                tp("$6\\frac{2}{3}$ as an improper fraction is:",
                   ["$\\frac{20}{3}$", "$\\frac{8}{3}$", "$\\frac{62}{3}$"],
                   "$6 \\times 3 + 2 = 20$: $\\frac{20}{3}$.",
                   ["Eq(6 + Rational(2,3), Rational(20,3))"]),
                tp("Between which whole numbers does $\\frac{29}{6}$ sit?",
                   ["$4$ and $5$", "$5$ and $6$", "$3$ and $4$"],
                   "$\\frac{24}{6} = 4$ and $\\frac{30}{6} = 5$: it lands at $4\\frac{5}{6}$.",
                   ["Eq(Rational(29,6), 4 + Rational(5,6))", "Rational(29,6) < 5"]),
                tp("A recipe needs $\\frac{9}{4}$ cups of flour. In whole cups and quarters that is:",
                   ["$2\\frac{1}{4}$ cups", "$2\\frac{3}{4}$ cups", "$1\\frac{5}{4}$ cups"],
                   "$9 \\div 4 = 2$ r $1$: two full cups and one quarter-cup.",
                   ["Eq(Rational(9,4), 2 + Rational(1,4))"]),
                tp("Which pair are the SAME amount?",
                   ["$\\frac{22}{7}$ and $3\\frac{1}{7}$", "$\\frac{22}{7}$ and $2\\frac{2}{7}$", "$\\frac{22}{7}$ and $3\\frac{2}{7}$"],
                   "$22 \\div 7 = 3$ r $1$: $3\\frac{1}{7}$; receipt $3 \\times 7 + 1 = 22$ ✓.",
                   ["Eq(Rational(22,7), 3 + Rational(1,7))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Improper Fractions & Mixed Numbers\"",
                    "Division with remainders turned out to be fraction notation in disguise — the remainder was a numerator all along. Last stop: adding and subtracting fractions whose pieces already match.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Adding & Subtracting with Like Denominators
# ==========================================================================

def lesson_add_subtract():
    return {
        "slug": "adding-and-subtracting-like-denominators",
        "title": "Adding & Subtracting Fractions",
        "concreteComparison": (
            "You eat $\\frac{3}{8}$ of a bread; your sister eats "
            "$\\frac{2}{8}$. Together: five pieces of the eighth size — "
            "$\\frac{5}{8}$. NOT $\\frac{5}{16}$: nobody recut the "
            "bread. When the pieces already match, adding fractions is "
            "just counting pieces — the denominator is the pieces' "
            "name, and names don't add."),
        "objective": (
            "Add and subtract fractions with like denominators, "
            "simplify results, handle sums past one whole, and subtract "
            "a fraction from a whole number."),
        "concept": [
            "**Count the pieces; keep the name.** $\\frac{3}{8} + "
            "\\frac{2}{8} = \\frac{5}{8}$: three eighths plus two "
            "eighths is five eighths — exactly like $3$ sheep $+ 2$ "
            "sheep $= 5$ sheep. Adding the denominators would rename "
            "the pieces mid-count: the one unforgivable move.",
            "**Results like to be simplified.** $\\frac{3}{8} + "
            "\\frac{1}{8} = \\frac{4}{8}$ — which answers to its "
            "simplest name, $\\frac{1}{2}$. Finish every sum with a "
            "merge check.",
            "**Past one whole, and back from one.** $\\frac{5}{6} + "
            "\\frac{4}{6} = \\frac{9}{6} = 1\\frac{1}{2}$ — top-heavy "
            "sums convert to mixed. And to subtract FROM a whole, "
            "rename it first: $1 = \\frac{4}{4}$, so $1 - \\frac{3}{4} "
            "= \\frac{1}{4}$.",
        ],
        "keyIdea": (
            "Like pieces add and subtract by their counts — the "
            "denominator is a name, not a number to add. Simplify the "
            "result, convert top-heavy answers, and rename wholes "
            "before subtracting from them."),
        "facts": [
            {"title": "Count, don't rename",
             "latex": "\\frac{3}{8} + \\frac{2}{8} = \\frac{5}{8} \\quad (\\ne \\tfrac{5}{16})",
             "explanation": "Pieces of one size add like objects of one kind; the name stays."},
            {"title": "Wholes rename before subtracting",
             "latex": "1 - \\frac{3}{4} = \\frac{4}{4} - \\frac{3}{4} = \\frac{1}{4}",
             "explanation": "Dress the whole in the needed denominator, then count."},
        ],
        "workedExamples": [
            {"id": "g5fr-l5-we1",
             "statement": "Add $\\frac{3}{8} + \\frac{2}{8}$, and explain why the answer is not $\\frac{5}{16}$.",
             "note": "The pieces already match — just count.",
             "solution": ("Three eighths plus two eighths is five eighths: "
                          "$\\frac{5}{8}$. Writing $\\frac{5}{16}$ would claim the "
                          "pieces became sixteenths — but nobody recut the bread. "
                          "(And $\\frac{5}{16}$ is LESS than $\\frac{3}{8}$ alone — "
                          "an addition that shrinks is its own alarm bell.)"),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(3,8) + Rational(2,8), Rational(5,8))",
                       "Rational(5,16) < Rational(3,8)"]},
            {"id": "g5fr-l5-we2",
             "statement": "Compute $\\frac{5}{6} + \\frac{4}{6}$.",
             "note": "The sum passes a whole.",
             "solution": ("$\\frac{5}{6} + \\frac{4}{6} = \\frac{9}{6}$ — top-heavy. "
                          "Convert: $9 \\div 6 = 1$ r $3$, so $1\\frac{3}{6}$, and "
                          "$\\frac{3}{6}$ simplifies: $1\\frac{1}{2}$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(5,6) + Rational(4,6), Rational(9,6))",
                       "Eq(Rational(9,6), 1 + Rational(1,2))"]},
        ],
        "commonMistakes": [
            {"text": "Adding the denominators — 3/8 + 2/8 = 5/16.",
             "correction": "The denominator NAMES the pieces; it doesn't count anything. Five eighths, same name: 5/8. If your \"sum\" is smaller than one addend, this is what happened.",
             "authored": True},
            {"text": "Refusing to subtract from a whole number — \"1 − 3/4 can't be done, 1 has no fourths\".",
             "correction": "It does once you rename it: 1 = 4/4. Then 4/4 − 3/4 = 1/4. Wholes wear any denominator you need.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5fr-l5-t1",
             "statement": "Compute $\\frac{7}{10} - \\frac{3}{10}$ and simplify.",
             "solution": "Seven tenths minus three tenths: $\\frac{4}{10} = \\frac{2}{5}$.",
             "check": ["Eq(Rational(7,10) - Rational(3,10), Rational(2,5))"]},
            {"id": "g5fr-l5-t2",
             "statement": "Compute $2 - \\frac{5}{8}$.",
             "solution": "Rename one whole: $2 = 1\\frac{8}{8}$, so $2 - \\frac{5}{8} = 1\\frac{3}{8}$. (Check: $1\\frac{3}{8} + \\frac{5}{8} = 2$ ✓.)",
             "check": ["Eq(2 - Rational(5,8), 1 + Rational(3,8))",
                       "Eq(1 + Rational(3,8) + Rational(5,8), 2)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Count the pieces, keep the name", [
                "When denominators match, the pieces are the same size — so adding is COUNTING: $\\frac{3}{8} + \\frac{2}{8} = \\frac{5}{8}$, exactly like $3$ sheep $+ 2$ sheep.",
                "The denominator is the pieces' NAME. Adding names ($\\frac{5}{16}$) claims someone recut the bread — and produces a \"sum\" smaller than one of the addends. An addition that shrinks is an alarm bell.",
                "Subtraction counts the other way: $\\frac{7}{10} - \\frac{3}{10} = \\frac{4}{10}$ — then simplify: $\\frac{2}{5}$.",
            ]),
            workedset("Matching pieces",
                      "Add or subtract the counts; the name rides along.", [
                wex("Add $\\frac{3}{8} + \\frac{2}{8}$.",
                    ["Count: $3 + 2 = 5$ pieces of the eighth size.",
                     "$\\frac{5}{8}$ — and note $\\frac{5}{16}$ would be SMALLER than $\\frac{3}{8}$: the alarm bell."],
                    "$\\frac{5}{8}$",
                    ["Eq(Rational(3,8) + Rational(2,8), Rational(5,8))"]),
                wex("Subtract $\\frac{7}{10} - \\frac{3}{10}$ and simplify.",
                    ["$7 - 3 = 4$ tenths: $\\frac{4}{10}$.",
                     "Merge by $2$: $\\frac{2}{5}$."],
                    "$\\frac{2}{5}$",
                    ["Eq(Rational(7,10) - Rational(3,10), Rational(2,5))"]),
            ]),
            tryitset("Same-name arithmetic", "Counts move; names don't.", [
                tp("$\\frac{4}{9} + \\frac{2}{9}$ equals:",
                   ["$\\frac{6}{9} = \\frac{2}{3}$", "$\\frac{6}{18}$", "$\\frac{8}{9}$"],
                   "Six ninths — which merges to $\\frac{2}{3}$. ($\\frac{6}{18}$ added the names.)",
                   ["Eq(Rational(4,9) + Rational(2,9), Rational(2,3))"]),
                tp("$\\frac{11}{12} - \\frac{5}{12}$ equals:",
                   ["$\\frac{1}{2}$", "$\\frac{6}{24}$", "$\\frac{5}{12}$"],
                   "$\\frac{6}{12}$, which is $\\frac{1}{2}$ in simplest form.",
                   ["Eq(Rational(11,12) - Rational(5,12), Rational(1,2))"]),
                tp("$\\frac{2}{7} + \\frac{3}{7} + \\frac{1}{7}$ equals:",
                   ["$\\frac{6}{7}$", "$\\frac{6}{21}$", "$1$"],
                   "$2 + 3 + 1 = 6$ sevenths: $\\frac{6}{7}$ — one seventh short of the whole.",
                   ["Eq(Rational(2,7) + Rational(3,7) + Rational(1,7), Rational(6,7))"]),
            ]),
            tapq("The alarm bell", "A student computes $\\frac{1}{4} + \\frac{2}{4} = \\frac{3}{8}$. What gives the error away instantly?",
                 ["$\\frac{3}{8}$ is SMALLER than the addend $\\frac{2}{4}$ — adding can't shrink",
                  "the numerator is wrong",
                  "quarters cannot be added",
                  "nothing — the answer is right"],
                 "Adding positive amounts must grow: but $\\frac{3}{8} < \\frac{2}{4} = \\frac{4}{8}$. The denominators were added — the pieces are still quarters: $\\frac{3}{4}$.",
                 ["Eq(Rational(1,4) + Rational(2,4), Rational(3,4))",
                  "Rational(3,8) < Rational(2,4)"]),
            funfact("Same rule, every size",
                    "\"Three eighths plus two eighths is five eighths\" works for exactly the same reason as \"three metres plus two metres is five metres\" — you can only count things that share a unit. Next year, adding $\\frac{1}{2} + \\frac{1}{3}$ will start by MAKING the units match (sixths) — equivalent fractions again."),
            teach("Concept B", "Past the whole, and back from it", [
                "Sums can pass a whole: $\\frac{5}{6} + \\frac{4}{6} = \\frac{9}{6}$ — top-heavy. Convert: $1\\frac{3}{6} = 1\\frac{1}{2}$.",
                "To subtract FROM a whole, dress it in the needed name first: $1 = \\frac{4}{4}$, so $1 - \\frac{3}{4} = \\frac{1}{4}$. For $2 - \\frac{5}{8}$: take the eighths from ONE of the wholes — $1\\frac{8}{8} - \\frac{5}{8} = 1\\frac{3}{8}$.",
                "Receipt thinking still applies: $1\\frac{3}{8} + \\frac{5}{8} = 2$ ✓ — additions check subtractions here exactly as with whole numbers.",
            ]),
            workedset("Crossing one",
                      "Convert top-heavy sums; rename wholes before subtracting.", [
                wex("Compute $\\frac{5}{6} + \\frac{4}{6}$.",
                    ["$\\frac{9}{6}$, top-heavy: $9 \\div 6 = 1$ r $3$.",
                     "$1\\frac{3}{6} = 1\\frac{1}{2}$."],
                    "$1\\frac{1}{2}$",
                    ["Eq(Rational(5,6) + Rational(4,6), 1 + Rational(1,2))"]),
                wex("Compute $2 - \\frac{5}{8}$.",
                    ["Rename a whole: $2 = 1\\frac{8}{8}$.",
                     "$1\\frac{8}{8} - \\frac{5}{8} = 1\\frac{3}{8}$; receipt $1\\frac{3}{8} + \\frac{5}{8} = 2$ ✓."],
                    "$1\\frac{3}{8}$",
                    ["Eq(2 - Rational(5,8), 1 + Rational(3,8))"]),
            ]),
            tryitset("Over and back", "Top-heavy? Convert. From a whole? Rename first.", [
                tp("$\\frac{7}{9} + \\frac{5}{9}$ equals:",
                   ["$1\\frac{3}{9} = 1\\frac{1}{3}$", "$\\frac{12}{18}$", "$\\frac{12}{9}$ and stop"],
                   "$\\frac{12}{9}$ converts: $1\\frac{3}{9}$, and $\\frac{3}{9}$ merges to $\\frac{1}{3}$.",
                   ["Eq(Rational(7,9) + Rational(5,9), 1 + Rational(1,3))"]),
                tp("$1 - \\frac{2}{5}$ equals:",
                   ["$\\frac{3}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{5}$"],
                   "$1 = \\frac{5}{5}$: five fifths minus two is three — $\\frac{3}{5}$.",
                   ["Eq(1 - Rational(2,5), Rational(3,5))"]),
                tp("$3 - \\frac{3}{4}$ equals:",
                   ["$2\\frac{1}{4}$", "$2\\frac{3}{4}$", "$3\\frac{1}{4}$"],
                   "Take the quarters from one whole: $2\\frac{4}{4} - \\frac{3}{4} = 2\\frac{1}{4}$; receipt $2\\frac{1}{4} + \\frac{3}{4} = 3$ ✓.",
                   ["Eq(3 - Rational(3,4), 2 + Rational(1,4))"]),
            ]),
            tapq("Rename, then count", "To compute $1 - \\frac{5}{12}$, the first move is:",
                 ["rename: $1 = \\frac{12}{12}$", "subtract numerators: $1 - 5$",
                  "add the denominators", "convert $\\frac{5}{12}$ to a mixed number"],
                 "Dress the whole in twelfths, then count: $\\frac{12}{12} - \\frac{5}{12} = \\frac{7}{12}$.",
                 ["Eq(1 - Rational(5,12), Rational(7,12))"]),
            recap([
                "Like denominators: add or subtract the COUNTS; the name stays.",
                "A sum smaller than an addend means the denominators were added — the alarm bell.",
                "Top-heavy results convert to mixed numbers; simplify what merges.",
                "Subtracting from wholes: rename the whole first (1 = n/n) — and receipt the answer.",
            ]),
            tip("Simplify every answer and receipt every subtraction — the two finishing moves that separate done from almost-done."),
            tryitset("Mixed practice", "The full like-denominator toolkit.", [
                tp("$\\frac{5}{12} + \\frac{1}{12}$ equals:",
                   ["$\\frac{1}{2}$", "$\\frac{6}{24}$", "$\\frac{5}{12}$"],
                   "$\\frac{6}{12}$, merged: $\\frac{1}{2}$.",
                   ["Eq(Rational(5,12) + Rational(1,12), Rational(1,2))"]),
                tp("$\\frac{13}{10} - \\frac{7}{10}$ equals:",
                   ["$\\frac{3}{5}$", "$\\frac{6}{20}$", "$\\frac{6}{10}$ and stop"],
                   "$\\frac{6}{10}$, merged by $2$: $\\frac{3}{5}$.",
                   ["Eq(Rational(13,10) - Rational(7,10), Rational(3,5))"]),
                tp("A jug holds $1$ litre; $\\frac{3}{8}$ has been poured out. Remaining:",
                   ["$\\frac{5}{8}$ litre", "$\\frac{3}{8}$ litre", "$\\frac{5}{16}$ litre"],
                   "$1 = \\frac{8}{8}$: $\\frac{8}{8} - \\frac{3}{8} = \\frac{5}{8}$.",
                   ["Eq(1 - Rational(3,8), Rational(5,8))"]),
                tp("You walk $\\frac{4}{5}$ km to school and $\\frac{4}{5}$ km back. Total:",
                   ["$1\\frac{3}{5}$ km", "$\\frac{8}{10}$ km", "$\\frac{4}{5}$ km"],
                   "$\\frac{4}{5} + \\frac{4}{5} = \\frac{8}{5} = 1\\frac{3}{5}$ km — past one whole kilometre, as a there-and-back should be. ($\\frac{8}{10}$ added the names.)",
                   ["Eq(Rational(4,5) + Rational(4,5), 1 + Rational(3,5))"]),
                tp("$2\\frac{1}{6} + \\frac{4}{6}$ equals:",
                   ["$2\\frac{5}{6}$", "$2\\frac{5}{12}$", "$3\\frac{1}{6}$"],
                   "The sixths add: $\\frac{1}{6} + \\frac{4}{6} = \\frac{5}{6}$, riding with the $2$: $2\\frac{5}{6}$.",
                   ["Eq(2 + Rational(1,6) + Rational(4,6), 2 + Rational(5,6))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Adding & Subtracting Fractions\" — and the topic",
                    "Parts of a whole, many names for one amount, size against count, two names for top-heavy amounts, and same-name arithmetic: the complete first tour of fractions. Different denominators — and the equivalent-fraction bridge that tames them — are where Grade 6 picks up the story.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5fr-pr1", "A cake is cut into $12$ equal pieces and $7$ are eaten. What fraction remains?",
             "$12 - 7 = 5$ pieces of the twelfth size: $\\frac{5}{12}$. Check: $\\frac{7}{12} + \\frac{5}{12} = 1$.",
             ["Eq(Rational(7,12) + Rational(5,12), 1)"]),
        prob("g5fr-pr2", "Find $\\frac{5}{6}$ of $42$.",
             "Six equal groups of $7$; take five: $35$.",
             ["Eq(Rational(42,6), 7)", "Eq(Rational(5,6)*42, 35)"]),
        prob("g5fr-pr3", "Fill the blank: $\\frac{7}{8} = \\frac{\\square}{40}$.",
             "$8 \\to 40$ is $\\times 5$; the top follows: $35$.",
             ["Eq(Rational(7,8), Rational(35,40))"]),
        prob("g5fr-pr4", "Write $\\frac{36}{48}$ in simplest form.",
             "Divide both by $12$: $\\frac{3}{4}$.",
             ["Eq(Rational(36,48), Rational(3,4))"]),
        prob("g5fr-pr5", "Order from smallest to largest: $\\frac{5}{9}, \\frac{5}{7}, \\frac{5}{11}$.",
             "Same count — finer cuts are smaller: $\\frac{5}{11} < \\frac{5}{9} < \\frac{5}{7}$.",
             ["Rational(5,11) < Rational(5,9)", "Rational(5,9) < Rational(5,7)"]),
        prob("g5fr-pr6", "Write $\\frac{47}{9}$ as a mixed number, with its receipt.",
             "$47 \\div 9 = 5$ r $2$: $5\\frac{2}{9}$. Receipt: $5 \\times 9 + 2 = 47$ ✓.",
             ["Eq(5*9 + 2, 47)", "Eq(Rational(47,9), 5 + Rational(2,9))"]),
        prob("g5fr-pr7", "Compute $\\frac{9}{14} + \\frac{5}{14}$ and simplify.",
             "$\\frac{14}{14} = 1$ — the pieces rebuild the whole exactly.",
             ["Eq(Rational(9,14) + Rational(5,14), 1)"]),
        prob("g5fr-pr8", "A bottle holds $2$ litres; $\\frac{7}{10}$ of a litre is poured out. How much remains?",
             "Take the tenths from one whole: $1\\frac{10}{10} - \\frac{7}{10} = 1\\frac{3}{10}$ litres. Receipt: $1\\frac{3}{10} + \\frac{7}{10} = 2$ ✓.",
             ["Eq(2 - Rational(7,10), 1 + Rational(3,10))"]),
    ]


def test_bank():
    return [
        prob("g5fr-x1", "Find $\\frac{3}{7}$ of $56$.",
             "Seven groups of $8$; take three: $24$.",
             ["Eq(Rational(3,7)*56, 24)"]),
        prob("g5fr-x2", "Which is larger, $\\frac{7}{12}$ or $\\frac{4}{9}$? Use the half benchmark.",
             "$\\frac{7}{12}$: $14 > 12$ — over half. $\\frac{4}{9}$: $8 < 9$ — under half. So $\\frac{7}{12} > \\frac{4}{9}$.",
             ["Rational(7,12) > Rational(1,2)", "Rational(4,9) < Rational(1,2)",
              "Rational(7,12) > Rational(4,9)"]),
        prob("g5fr-x3", "Write $\\frac{40}{72}$ in simplest form.",
             "Divide both by $8$: $\\frac{5}{9}$.",
             ["Eq(Rational(40,72), Rational(5,9))"]),
        prob("g5fr-x4", "Write $5\\frac{4}{7}$ as an improper fraction, and $\\frac{34}{8}$ as a simplified mixed number.",
             "$5 \\times 7 + 4 = 39$: $\\frac{39}{7}$. And $34 \\div 8 = 4$ r $2$: $4\\frac{2}{8} = 4\\frac{1}{4}$.",
             ["Eq(5 + Rational(4,7), Rational(39,7))",
              "Eq(Rational(34,8), 4 + Rational(1,4))"]),
        prob("g5fr-x5", "Compute $\\frac{8}{15} + \\frac{11}{15}$, giving the answer as a mixed number.",
             "$\\frac{19}{15}$, top-heavy: $19 \\div 15 = 1$ r $4$ — $1\\frac{4}{15}$.",
             ["Eq(Rational(8,15) + Rational(11,15), 1 + Rational(4,15))"]),
        prob("g5fr-x6", ("A family eats $\\frac{5}{8}$ of a bread at breakfast and $\\frac{2}{8}$ "
                         "at lunch. What fraction of the bread remains, and why is the answer "
                         "NOT $\\frac{7}{16}$ eaten?"),
             "Eaten: $\\frac{5}{8} + \\frac{2}{8} = \\frac{7}{8}$ — the pieces stayed eighths; adding denominators would claim the bread was recut. Remaining: $1 - \\frac{7}{8} = \\frac{1}{8}$.",
             ["Eq(Rational(5,8) + Rational(2,8), Rational(7,8))",
              "Eq(1 - Rational(7,8), Rational(1,8))",
              "Rational(7,16) < Rational(5,8)"]),
    ]


def main():
    topic = {
        "slug": "fractions-first-steps",
        "title": "Fractions — First Steps",
        "grade": 5,
        "status": "published",
        "blurb": ("Fractions as parts of a whole, equivalent fractions, "
                  "comparing, improper fractions and mixed numbers, and adding "
                  "and subtracting with like denominators."),
        "lessons": [
            lesson_meaning(),
            lesson_equivalent(),
            lesson_comparing(),
            lesson_mixed(),
            lesson_add_subtract(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "fractions-first-steps.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
