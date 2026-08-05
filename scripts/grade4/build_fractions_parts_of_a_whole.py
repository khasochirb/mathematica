#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Fractions — Parts of a Whole.

What a fraction really is: equal parts of a whole. Equal parts and the
names they earn (halves, thirds, quarters), unit fractions and the
more-parts-smaller-pieces rule, non-unit fractions as stacks of unit
pieces, comparing by meaning (same pieces: count them; unit fractions:
the bigger bottom loses), and taking a fraction of a set by sharing
into groups.

Through-line: THE BOTTOM NUMBER CUTS, THE TOP NUMBER COUNTS. Every
lesson returns to it — the denominator says how the whole is cut into
equal parts, the numerator says how many of those parts you take.

Grade discipline: meaning and comparing only — no equivalent-fraction
chains, no mixed numbers, no adding fractions. All divisions come from
times tables at most 10, no negative numbers, values inside 10 000.
Figures are built from the SAME variables as the statements they
illustrate, so text and picture cannot disagree.

Run: python3 scripts/grade4/build_fractions_parts_of_a_whole.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic, withfig,
                     fig_bar, fig_groups, C_GREEN, C_NEUTRAL)


# ==========================================================================
# Lesson 1 — Equal Parts
# ==========================================================================

def lesson_equal_parts():
    hd, td, qd = 2, 3, 4
    fig_half = fig_bar(1, hd, "%d equal parts, 1 shaded: one half" % hd)
    fig_third = fig_bar(1, td, "%d equal parts, 1 shaded: one third" % td)
    fig_quarter = fig_bar(1, qd, "%d equal parts, 1 shaded: one quarter" % qd)
    fig_sixth = fig_bar(1, 6, "6 equal parts, 1 shaded")
    fig_fifth = fig_bar(1, 5, "5 equal parts, 1 shaded")
    fig_eighth = fig_bar(1, 8, "8 equal parts, 1 shaded")
    return {
        "slug": "equal-parts",
        "title": "Equal Parts",
        "concreteComparison": (
            "Two friends share one khuushuur. Cut it in the middle and "
            "each holds one half — a fair share with a name. Cut it "
            "crooked, one big piece and one small, and NOBODY holds a "
            "half: just a lucky friend and an unlucky one. A fraction "
            "is born only when the parts are EQUAL."),
        "objective": (
            "Decide whether a cut makes equal parts, name equal parts "
            "from their count — halves, thirds, quarters — and read "
            "the bottom number of a fraction as the number of equal "
            "parts."),
        "concept": [
            "**A fraction needs equal parts.** Cut a whole into parts "
            "of the SAME size and each part earns a fraction name. "
            "Parts of different sizes have no fraction name at all — "
            "a big piece and a small piece are just pieces.",
            "**The count names the parts.** $2$ equal parts are "
            "HALVES, $3$ are THIRDS, $4$ are QUARTERS, $5$ are "
            "fifths. The name comes straight from how many equal "
            "parts make the whole.",
            "**The bottom number cuts.** Written as a fraction, the "
            "bottom number says how many equal parts the whole is "
            "cut into: in $\\frac{1}{4}$ the $4$ means four equal "
            "parts, and the $1$ on top counts one of them.",
        ],
        "keyIdea": (
            "Equal parts, or no fraction at all. The bottom number "
            "cuts the whole into that many equal parts; the top "
            "number counts the parts you take."),
        "facts": [
            {"title": "The naming rule",
             "latex": "2 \\to \\text{halves} \\quad 3 \\to \\text{thirds} \\quad 4 \\to \\text{quarters}",
             "explanation": "Count the equal parts; the count is the name."},
            {"title": "The parts rebuild the whole",
             "latex": "4 \\times \\frac{1}{4} = 1",
             "explanation": "Four quarter-pieces put back together make exactly one whole — the test of a fair cut."},
        ],
        "workedExamples": [
            {"id": "g4fr-l1-we1",
             "statement": "A khuushuur is cut into $2$ equal parts. What is each part called, and how many of them rebuild the whole?",
             "note": "Equal parts first — then the count gives the name.",
             "solution": ("Two EQUAL parts: each is one half, written $\\frac{1}{2}$. "
                          "Two halves rebuild the whole: $2 \\times \\frac{1}{2} = 1$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*Rational(1,2), 1)", "Rational(1,2) < 1"]},
            {"id": "g4fr-l1-we2",
             "statement": "Saraa cuts a ribbon into $4$ parts, but two are long and two are short. May any part be called one quarter?",
             "note": "Count the parts AND check their sizes.",
             "solution": ("No. A quarter means one of $4$ EQUAL parts — four true "
                          "quarters rebuild the whole exactly, $4 \\times \\frac{1}{4} "
                          "= 1$. Saraa's parts differ in size, so none of them earns "
                          "the name."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*Rational(1,4), 1)"]},
        ],
        "commonMistakes": [
            {"text": "Calling one of 4 unequal pieces \"a quarter\" just because there are 4 pieces.",
             "correction": "A quarter is one of 4 EQUAL pieces. Count the pieces and check their sizes — if the sizes differ, the name does not apply.",
             "authored": True},
            {"text": "Reading the bottom number as \"how many pieces I take\".",
             "correction": "The bottom number CUTS: it says how many equal parts make the whole. The top number is the one that counts what you take.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4fr-l1-t1",
             "statement": "A round bread is cut into $3$ equal parts. Name one part in words and as a fraction.",
             "solution": "Three equal parts are thirds: one part is one third, $\\frac{1}{3}$. Three of them rebuild the bread: $3 \\times \\frac{1}{3} = 1$ ✓.",
             "check": ["Eq(3*Rational(1,3), 1)", "Rational(1,3) < 1"]},
            {"id": "g4fr-l1-t2",
             "statement": "In the fraction $\\frac{1}{5}$, what does the $5$ tell you, and what does the $1$ tell you?",
             "solution": "The $5$ cuts: the whole is in $5$ equal parts. The $1$ counts: you take one part. Five such parts make the whole: $5 \\times \\frac{1}{5} = 1$ ✓.",
             "check": ["Eq(5*Rational(1,5), 1)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Equal parts, or no fraction", [
                "Two friends share one khuushuur. Cut it in the middle: $%d$ EQUAL parts, and each friend holds one half — the bar below shows the fair cut." % hd,
                "Cut it crooked instead — one big part, one small — and neither part is a half. It is just a big piece and a small piece, with no fraction name.",
                "That is the first rule of fractions: a fraction names one of EQUAL parts. No equal parts, no fraction.",
            ]), fig_half),
            workedset("Fair cut or not?",
                      "Check the sizes before giving any part a name.", [
                wex("A khuushuur is cut into $2$ equal parts. What is each part?",
                    ["Equal sizes, $2$ parts: each is one half.",
                     "Two halves rebuild the whole: $2 \\times \\frac{1}{2} = 1$ ✓."],
                    "one half",
                    ["Eq(2*Rational(1,2), 1)"]),
                wex("Saraa cuts a ribbon into $4$ parts: two long, two short. Is any part one quarter?",
                    ["Four parts, but NOT equal — sizes differ.",
                     "No part is a quarter: quarters are $4$ equal parts, and $4 \\times \\frac{1}{4} = 1$ only works for a fair cut."],
                    "no",
                    ["Eq(4*Rational(1,4), 1)"]),
            ]),
            tryitset("Spot the fair cut", "Equal sizes first, names second.", [
                tp("A pizza is cut into $2$ equal slices. Each slice is:",
                   ["one half", "one quarter", "one whole"],
                   "Two EQUAL parts are halves, and two halves rebuild the pizza: $2 \\times \\frac{1}{2} = 1$ ✓. A quarter would need $4$ equal parts, and a whole is the uncut pizza itself.",
                   ["Eq(2*Rational(1,2), 1)"]),
                tp("A chocolate bar snaps into $3$ pieces: one big, two tiny. Is each piece one third?",
                   ["no — thirds must be three EQUAL pieces",
                    "yes — three pieces always make thirds",
                    "only the big piece is one third"],
                   "Check sizes before names: thirds are three EQUAL pieces, and three of them rebuild the bar, $3 \\times \\frac{1}{3} = 1$ ✓. Counting three pieces without checking sizes is the trap.",
                   ["Eq(3*Rational(1,3), 1)"]),
                tp("How many EQUAL parts does a whole cut into quarters have?",
                   ["$4$", "$2$", "$3$"],
                   "Quarters means four equal parts — $4 \\times \\frac{1}{4} = 1$ ✓. Two equal parts would be halves, three would be thirds.",
                   ["Eq(4*Rational(1,4), 1)"]),
            ]),
            tapq("The equal-parts rule", "A cake is cut into $4$ parts of DIFFERENT sizes, and one part is on your plate. Do you hold one quarter of the cake?",
                 ["no — a quarter needs $4$ EQUAL parts",
                  "yes — one part of four is always a quarter",
                  "yes, if your part is the biggest",
                  "yes, if your part is the smallest"],
                 "The name quarter belongs to a fair cut only: four EQUAL parts, each $\\frac{1}{4}$, rebuilding the cake as $4 \\times \\frac{1}{4} = 1$ ✓. One unequal part of four could be almost any amount, so the name would lie.",
                 ["Eq(4*Rational(1,4), 1)"]),
            funfact("Folding is a fair cutter",
                    "Fold a strip of paper in half and the crease cuts it into $2$ equal parts. Fold it in half again: $2 \\times 2 = 4$ equal parts — quarters. One more fold gives $2 \\times 4 = 8$ equal parts. Every fold doubles the count of equal parts, and a fold never cheats — the two sides land exactly on each other."),
            withfig(teach("Concept B", "The count is the name", [
                "Equal parts are named by their COUNT: $%d$ equal parts are halves, $%d$ are thirds, $%d$ are quarters, $5$ are fifths, $6$ are sixths — the bar below shows quarters." % (hd, td, qd),
                "Write it with two numbers: the BOTTOM number says how many equal parts the whole is cut into; the TOP number counts how many parts you take. One part of four is $\\frac{1}{4}$.",
                "Say the rule the way you will use it all topic: THE BOTTOM NUMBER CUTS, THE TOP NUMBER COUNTS.",
            ]), fig_quarter),
            workedset("Name the parts",
                      "Count the equal parts; the count is the name.", [
                withfig(wex("A bread is cut into $%d$ equal parts and you take one. Write the fraction." % td,
                    ["Three equal parts: thirds. One of them is one third.",
                     "Bottom cuts ($%d$ equal parts), top counts ($1$ taken): $\\frac{1}{%d}$." % (td, td)],
                    "$\\frac{1}{3}$",
                    ["Eq(3*Rational(1,3), 1)", "Rational(1,3) < 1"]), fig_third),
                wex("What are $8$ equal parts of a whole called, and what fraction is one part?",
                    ["Eight equal parts: eighths.",
                     "One part is $\\frac{1}{8}$, and eight of them rebuild the whole: $8 \\times \\frac{1}{8} = 1$ ✓."],
                    "eighths; $\\frac{1}{8}$",
                    ["Eq(8*Rational(1,8), 1)", "Rational(1,8) < 1"]),
            ]),
            tryitset("Bottom cuts, top counts", "Read both numbers, in that order.", [
                withfig(tp("The bar shows $6$ equal parts with $1$ shaded. The shaded part is:",
                   ["$\\frac{1}{6}$", "$\\frac{6}{1}$", "$\\frac{1}{5}$"],
                   "Bottom cuts: $6$ equal parts. Top counts: $1$ shaded. So $\\frac{1}{6}$, and $6 \\times \\frac{1}{6} = 1$ rebuilds the bar ✓. $\\frac{6}{1}$ swaps the two jobs, and $\\frac{1}{5}$ miscounts the parts.",
                   ["Eq(6*Rational(1,6), 1)", "Rational(1,6) < 1"]), fig_sixth),
                tp("$5$ equal parts of a whole are called:",
                   ["fifths", "fours", "halves"],
                   "The count names the parts: five equal parts are fifths, each $\\frac{1}{5}$, and $5 \\times \\frac{1}{5} = 1$ ✓. Halves would mean only two equal parts.",
                   ["Eq(5*Rational(1,5), 1)"]),
                tp("In $\\frac{1}{4}$, the $4$ tells you:",
                   ["the whole is cut into $4$ equal parts",
                    "you take $4$ parts",
                    "there are $4$ wholes"],
                   "The bottom number cuts: $4$ equal parts make the whole, so each is $\\frac{1}{4}$ and $4 \\times \\frac{1}{4} = 1$ ✓. Taking parts is the top number's job.",
                   ["Eq(4*Rational(1,4), 1)"]),
            ]),
            tapq("Read the bottom number", "A bar is cut into $9$ equal pieces. One piece is:",
                 ["$\\frac{1}{9}$ of the bar",
                  "$\\frac{9}{1}$ of the bar",
                  "$\\frac{1}{8}$ of the bar",
                  "$9$ bars"],
                 "Bottom cuts: $9$ equal pieces, so one piece is $\\frac{1}{9}$, and nine of them rebuild the bar: $9 \\times \\frac{1}{9} = 1$ ✓. Writing $\\frac{9}{1}$ swaps cutter and counter.",
                 ["Eq(9*Rational(1,9), 1)", "Rational(1,9) < 1"]),
            recap([
                "A fraction names one of EQUAL parts — unequal pieces have no fraction name.",
                "The count names the parts: 2 halves, 3 thirds, 4 quarters, 5 fifths.",
                "The bottom number cuts the whole into equal parts.",
                "The top number counts the parts you take.",
                "All the parts together rebuild exactly one whole.",
            ]),
            tip("For every picture below, ask two questions in order: are the parts EQUAL, and how many are there? Only then give the name."),
            tryitset("Mixed practice", "Fair cuts, names, and the two numbers.", [
                withfig(tp("The bar shows $5$ equal parts with $1$ shaded. The shaded part is:",
                   ["$\\frac{1}{5}$", "$\\frac{5}{1}$", "$\\frac{1}{4}$"],
                   "Five equal parts, one taken: $\\frac{1}{5}$, and $5 \\times \\frac{1}{5} = 1$ ✓. $\\frac{1}{4}$ miscounts the cut; $\\frac{5}{1}$ puts the cutter on top.",
                   ["Eq(5*Rational(1,5), 1)"]), fig_fifth),
                tp("Temuulen cuts a melon into $2$ pieces, one clearly bigger than the other. The smaller piece is:",
                   ["not a half — the parts are not equal",
                    "exactly one half",
                    "one half of the bigger piece"],
                   "Halves demand two EQUAL parts, so that $2 \\times \\frac{1}{2} = 1$ ✓. An uneven cut makes pieces without fraction names — counting two pieces is not enough.",
                   ["Eq(2*Rational(1,2), 1)"]),
                tp("Which cut turns a bread into quarters?",
                   ["$4$ equal parts", "$4$ parts of any sizes", "$2$ equal parts"],
                   "Quarters are $4$ EQUAL parts — each $\\frac{1}{4}$, together $4 \\times \\frac{1}{4} = 1$ ✓. Any-size parts break the equal rule, and $2$ equal parts are halves.",
                   ["Eq(4*Rational(1,4), 1)"]),
                withfig(tp("The bar shows $8$ equal parts with $1$ shaded. Shaded part and its name:",
                   ["$\\frac{1}{8}$ — one eighth", "$\\frac{1}{6}$ — one sixth", "$\\frac{8}{1}$ — eight wholes"],
                   "Count the cut: $8$ equal parts, so one is $\\frac{1}{8}$ and $8 \\times \\frac{1}{8} = 1$ ✓. One sixth belongs to a $6$-part cut.",
                   ["Eq(8*Rational(1,8), 1)"]), fig_eighth),
                tp("The bottom number of a fraction always tells you:",
                   ["how many equal parts the whole is cut into",
                    "how many parts you take",
                    "how big the whole is"],
                   "The bottom cuts, the top counts. A bottom of $7$ means seven equal parts, each $\\frac{1}{7}$, and $7 \\times \\frac{1}{7} = 1$ ✓. What you take is the top number's story.",
                   ["Eq(7*Rational(1,7), 1)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Equal Parts\"",
                    "Equal parts, and names straight from the count — the ground every fraction stands on. Next: the fractions made of exactly ONE part, from $\\frac{1}{2}$ all the way down to $\\frac{1}{10}$, and a surprise about which of them is biggest.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Unit Fractions
# ==========================================================================

def lesson_unit_fractions():
    ua, ub = 4, 8  # the more-parts pair: quarters against eighths
    fig_one_sixth = fig_bar(1, 6, "1 of 6 equal pieces: one sixth")
    fig_one_eighth = fig_bar(1, ub, "1 of %d equal pieces" % ub)
    fig_one_ninth = fig_bar(1, 9, "1 of 9 equal pieces")
    fig_quarters = fig_bar(1, ua, "quarters: %d pieces share the whole" % ua)
    fig_eighths = fig_bar(1, ub, "eighths: %d pieces share the same whole" % ub)
    fig_one_seventh = fig_bar(1, 7, "1 of 7 equal pieces")
    return {
        "slug": "unit-fractions",
        "title": "Unit Fractions",
        "concreteComparison": (
            "One slab of aaruul, and hungry cousins keep arriving. "
            "Shared by $2$, each gets a big half. Shared by $4$, each "
            "gets a smaller quarter. Shared by $10$, each gets a thin "
            "tenth. The slab never grew or shrank — but the MORE "
            "people share it, the SMALLER each share becomes."),
        "objective": (
            "Read and write the unit fractions $\\frac{1}{2}$ to "
            "$\\frac{1}{10}$, know how many of each rebuild the "
            "whole, and use the rule that more parts make each part "
            "smaller."),
        "concept": [
            "**A unit fraction is ONE part.** Cut a whole into equal "
            "parts and take exactly one: $\\frac{1}{2}$, "
            "$\\frac{1}{3}$, $\\frac{1}{4}$, down to $\\frac{1}{10}$. "
            "The top is always $1$; only the cut changes.",
            "**The bottom number promises a rebuild.** Cut into $8$, "
            "and $8$ pieces of $\\frac{1}{8}$ make the whole again: "
            "$8 \\times \\frac{1}{8} = 1$. Whatever the cut, all its "
            "pieces together are exactly $1$.",
            "**More parts, smaller pieces.** The same whole shared "
            "into more parts leaves less for each: $\\frac{1}{8} < "
            "\\frac{1}{4}$, even though $8 > 4$. For unit fractions "
            "the bigger bottom number means the smaller piece.",
        ],
        "keyIdea": (
            "A unit fraction is one piece of an equal cut, and the "
            "finer the cut, the smaller the piece: the bigger the "
            "bottom number, the less you hold."),
        "facts": [
            {"title": "One piece of the cut",
             "latex": "\\frac{1}{2} \\quad \\frac{1}{3} \\quad \\frac{1}{4} \\quad \\frac{1}{5} \\quad \\frac{1}{10}",
             "explanation": "Top always 1 — one piece. The bottom says how fine the cut is."},
            {"title": "More parts, smaller pieces",
             "latex": "\\frac{1}{8} < \\frac{1}{4}",
             "explanation": "Eight pieces share the same whole that four shared — so each eighth is smaller."},
        ],
        "workedExamples": [
            {"id": "g4fr-l2-we1",
             "statement": "A bar is cut into $8$ equal pieces. Write the fraction for one piece, and say how many pieces rebuild the bar.",
             "note": "Top 1, bottom the cut.",
             "solution": ("One piece of an $8$-cut is $\\frac{1}{8}$. Eight of them "
                          "rebuild the bar: $8 \\times \\frac{1}{8} = 1$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*Rational(1,8), 1)", "Rational(1,8) < 1"]},
            {"id": "g4fr-l2-we2",
             "statement": "Which is bigger: $\\frac{1}{4}$ of a bar, or $\\frac{1}{8}$ of the same bar?",
             "note": "Same whole — compare how many pieces share it.",
             "solution": ("$\\frac{1}{4}$: only $4$ pieces share the whole, so each "
                          "is big. $\\frac{1}{8}$: $8$ pieces share the same whole, "
                          "so each is smaller. $\\frac{1}{8} < \\frac{1}{4}$, even "
                          "though $8 > 4$."),
             "badges": [{"text": "core"}],
             "check": ["Rational(1,8) < Rational(1,4)", "8 > 4"]},
        ],
        "commonMistakes": [
            {"text": "Thinking 1/8 is bigger than 1/4 because 8 is bigger than 4.",
             "correction": "The bottom number counts how many pieces SHARE the whole: more sharers, smaller shares. So 1/8 < 1/4 — the bigger bottom loses.",
             "authored": True},
            {"text": "Writing one piece of a 5-cut as 5/1.",
             "correction": "The bottom cuts, the top counts: one piece of 5 equal pieces is 1/5. Putting the 5 on top would claim five wholes.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4fr-l2-t1",
             "statement": "Cut a bar into $10$ equal pieces. What fraction is one piece, and how many rebuild the whole?",
             "solution": "One piece is $\\frac{1}{10}$; ten of them rebuild the bar: $10 \\times \\frac{1}{10} = 1$ ✓.",
             "check": ["Eq(10*Rational(1,10), 1)", "Rational(1,10) < 1"]},
            {"id": "g4fr-l2-t2",
             "statement": "Order from biggest to smallest: $\\frac{1}{3}$, $\\frac{1}{10}$, $\\frac{1}{5}$.",
             "solution": "Fewer sharers, bigger share: $\\frac{1}{3} > \\frac{1}{5} > \\frac{1}{10}$.",
             "check": ["Rational(1,3) > Rational(1,5)", "Rational(1,5) > Rational(1,10)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One piece of the cut", [
                "A UNIT fraction is exactly one piece of an equal cut. The bar below is cut into $6$ equal pieces with $1$ shaded: that shaded piece is $\\frac{1}{6}$.",
                "The whole family looks alike: $\\frac{1}{2}$, $\\frac{1}{3}$, $\\frac{1}{4}$, $\\frac{1}{5}$, all the way to $\\frac{1}{10}$. The top is always $1$ — one piece — and the bottom says how fine the cut is.",
                "Every cut keeps the rebuild promise: $6$ sixths make the whole, $10$ tenths make the whole. The bottom number cuts, and all its pieces together are exactly $1$.",
            ]), fig_one_sixth),
            workedset("Write the unit fraction",
                      "Top 1, bottom the cut — then check the rebuild.", [
                withfig(wex("A bar is cut into $%d$ equal pieces. What fraction is one piece?" % 8,
                    ["Top $1$ (one piece), bottom $8$ (the cut): $\\frac{1}{8}$.",
                     "Rebuild check: $8 \\times \\frac{1}{8} = 1$ ✓."],
                    "$\\frac{1}{8}$",
                    ["Eq(8*Rational(1,8), 1)", "Rational(1,8) < 1"]), fig_one_eighth),
                wex("How many $\\frac{1}{7}$ pieces make one whole?",
                    ["The bottom promises the rebuild: a $7$-cut needs all $7$ pieces.",
                     "$7 \\times \\frac{1}{7} = 1$ ✓."],
                    "$7$",
                    ["Eq(7*Rational(1,7), 1)"]),
            ]),
            tryitset("The unit family", "One piece each — read the cut.", [
                withfig(tp("The bar shows $9$ equal pieces with $1$ shaded. The shaded piece is:",
                   ["$\\frac{1}{9}$", "$\\frac{9}{1}$", "$\\frac{1}{8}$"],
                   "Nine equal pieces, one taken: $\\frac{1}{9}$, and $9 \\times \\frac{1}{9} = 1$ ✓. $\\frac{9}{1}$ swaps cutter and counter; $\\frac{1}{8}$ miscounts the cut.",
                   ["Eq(9*Rational(1,9), 1)"]), fig_one_ninth),
                tp("How many $\\frac{1}{10}$ pieces rebuild one whole?",
                   ["$10$", "$1$", "$5$"],
                   "The bottom's promise: a $10$-cut rebuilds from all $10$ pieces — $10 \\times \\frac{1}{10} = 1$ ✓. One piece alone is just $\\frac{1}{10}$, far short of the whole.",
                   ["Eq(10*Rational(1,10), 1)", "Rational(1,10) < 1"]),
                tp("One slice of a pizza cut into $6$ equal slices is:",
                   ["$\\frac{1}{6}$ of the pizza", "$\\frac{6}{6}$ of the pizza", "$\\frac{1}{5}$ of the pizza"],
                   "Six equal slices, one taken: $\\frac{1}{6}$, and $6 \\times \\frac{1}{6} = 1$ ✓. $\\frac{6}{6}$ would be ALL the slices — the entire pizza.",
                   ["Eq(6*Rational(1,6), 1)"]),
            ]),
            tapq("One piece, exactly", "Which fraction names ONE piece of a whole cut into $5$ equal pieces?",
                 ["$\\frac{1}{5}$", "$\\frac{5}{5}$", "$\\frac{5}{1}$", "$\\frac{1}{4}$"],
                 "Bottom cuts ($5$ equal pieces), top counts ($1$ piece): $\\frac{1}{5}$, and $5 \\times \\frac{1}{5} = 1$ ✓. $\\frac{5}{5}$ takes every piece — the whole — and $\\frac{5}{1}$ swaps the numbers' jobs.",
                 ["Eq(5*Rational(1,5), 1)", "Rational(1,5) < 1"]),
            funfact("Music runs on unit fractions",
                    "Musicians name note lengths exactly like fractions: a half note lasts half as long as a whole note, a quarter note a quarter, an eighth note an eighth. Two half notes fill the time of one whole note, and it takes eight eighth notes to fill the same time — the more notes per whole, the shorter each one sounds."),
            withfig(teach("Concept B", "More parts, smaller pieces", [
                "Take two same-size bars. Cut one into $%d$ and the other into $%d$. The bar below shows the $%d$-cut: only $%d$ pieces share the whole, so each piece is generous." % (ua, ub, ua, ua),
                "In the $%d$-cut, twice as many pieces share the SAME whole — so every piece is smaller. $\\frac{1}{%d} < \\frac{1}{%d}$, even though $%d > %d$." % (ub, ub, ua, ub, ua),
                "The rule for every unit fraction: the bigger the bottom number, the finer the cut, the SMALLER the piece. The bottom cuts more, each piece gets less.",
            ]), fig_quarters),
            workedset("Compare the cuts",
                      "Same whole — the finer cut makes the smaller piece.", [
                withfig(wex("Which is bigger: $\\frac{1}{%d}$ or $\\frac{1}{%d}$ of the same bar?" % (ua, ub),
                    ["The $%d$-cut shares the whole among fewer pieces, so each is bigger." % ua,
                     "$\\frac{1}{%d} < \\frac{1}{%d}$ — the bigger bottom loses." % (ub, ua)],
                    "$\\frac{1}{4}$",
                    ["Rational(1,8) < Rational(1,4)", "8 > 4"]), fig_eighths),
                wex("Order $\\frac{1}{2}$, $\\frac{1}{6}$, $\\frac{1}{4}$ from biggest to smallest.",
                    ["Fewest sharers first: the $2$-cut gives the biggest piece.",
                     "$\\frac{1}{2} > \\frac{1}{4} > \\frac{1}{6}$."],
                    "$\\frac{1}{2} > \\frac{1}{4} > \\frac{1}{6}$",
                    ["Rational(1,2) > Rational(1,4)", "Rational(1,4) > Rational(1,6)"]),
            ]),
            tryitset("Bigger bottom, smaller piece", "Picture the sharers before answering.", [
                tp("Which is SMALLER: $\\frac{1}{5}$ or $\\frac{1}{9}$?",
                   ["$\\frac{1}{9}$", "$\\frac{1}{5}$", "they are equal"],
                   "Nine pieces share the whole that five shared: each ninth is smaller — $\\frac{1}{9} < \\frac{1}{5}$. Picking $\\frac{1}{5}$ reads the bottoms forwards instead of backwards.",
                   ["Rational(1,9) < Rational(1,5)", "9 > 5"]),
                tp("Which piece is BIGGEST: $\\frac{1}{3}$, $\\frac{1}{7}$, $\\frac{1}{10}$?",
                   ["$\\frac{1}{3}$", "$\\frac{1}{7}$", "$\\frac{1}{10}$"],
                   "The coarsest cut wins: only $3$ pieces share the whole, so $\\frac{1}{3} > \\frac{1}{7} > \\frac{1}{10}$. The $10$-cut has the most sharers and the thinnest pieces.",
                   ["Rational(1,3) > Rational(1,7)", "Rational(1,7) > Rational(1,10)"]),
                tp("Two same-size breads: one shared equally by $6$ people, one by $8$. A bigger share comes from:",
                   ["the $6$-person bread", "the $8$-person bread", "both shares are equal"],
                   "Fewer sharers, bigger shares: $\\frac{1}{6} > \\frac{1}{8}$. The $8$-person bread splits the same amount among more people.",
                   ["Rational(1,6) > Rational(1,8)"]),
            ]),
            tapq("Backwards on purpose", "$\\frac{1}{10}$ compared with $\\frac{1}{2}$:",
                 ["$\\frac{1}{10}$ is smaller — ten pieces share the whole",
                  "$\\frac{1}{10}$ is bigger — ten beats two",
                  "they are equal — both have $1$ on top",
                  "they cannot be compared"],
                 "Ten sharers against two: each tenth is a sliver, each half is generous — $\\frac{1}{10} < \\frac{1}{2}$. \"Ten beats two\" reads the bottom forwards; unit fractions read it backwards.",
                 ["Rational(1,10) < Rational(1,2)", "10 > 2"]),
            recap([
                "A unit fraction is ONE piece of an equal cut: top always 1.",
                "The bottom number says how fine the cut is — and promises the rebuild.",
                "All the pieces of any cut together make exactly 1.",
                "More parts means smaller pieces: 1/8 < 1/4.",
                "For unit fractions, the bigger bottom number always loses.",
            ]),
            tip("Before comparing two unit fractions, say out loud how many people share each whole — the crowd with more sharers gets the smaller piece."),
            tryitset("Mixed practice", "Reading, rebuilding, and comparing unit fractions.", [
                withfig(tp("The bar shows $7$ equal pieces with $1$ shaded. The shaded piece is:",
                   ["$\\frac{1}{7}$", "$\\frac{7}{1}$", "$\\frac{1}{6}$"],
                   "Seven equal pieces, one taken: $\\frac{1}{7}$, and $7 \\times \\frac{1}{7} = 1$ ✓. The other options swap the numbers or miscount the cut.",
                   ["Eq(7*Rational(1,7), 1)"]), fig_one_seventh),
                tp("Which is bigger: $\\frac{1}{6}$ or $\\frac{1}{4}$ of the same cake?",
                   ["$\\frac{1}{4}$", "$\\frac{1}{6}$", "they are equal"],
                   "Four sharers beat six: $\\frac{1}{4} > \\frac{1}{6}$. Choosing $\\frac{1}{6}$ because $6 > 4$ is the forwards-reading trap.",
                   ["Rational(1,4) > Rational(1,6)", "6 > 4"]),
                tp("How many $\\frac{1}{8}$ pieces rebuild one whole?",
                   ["$8$", "$4$", "$1$"],
                   "The bottom's promise: $8 \\times \\frac{1}{8} = 1$ ✓. Four eighths reach only half the bar.",
                   ["Eq(8*Rational(1,8), 1)"]),
                tp("One slab of aaruul is shared equally by $10$ children. Each child gets:",
                   ["$\\frac{1}{10}$ of the slab", "$\\frac{10}{1}$ of the slab", "$\\frac{1}{9}$ of the slab"],
                   "Ten equal shares: each is $\\frac{1}{10}$, and $10 \\times \\frac{1}{10} = 1$ rebuilds the slab ✓. $\\frac{1}{9}$ would mean only nine sharers.",
                   ["Eq(10*Rational(1,10), 1)"]),
                tp("Order from smallest to biggest: $\\frac{1}{2}$, $\\frac{1}{8}$, $\\frac{1}{4}$.",
                   ["$\\frac{1}{8} < \\frac{1}{4} < \\frac{1}{2}$",
                    "$\\frac{1}{2} < \\frac{1}{4} < \\frac{1}{8}$",
                    "$\\frac{1}{4} < \\frac{1}{8} < \\frac{1}{2}$"],
                   "Most sharers first: the $8$-cut gives the thinnest piece, the $2$-cut the fattest — $\\frac{1}{8} < \\frac{1}{4} < \\frac{1}{2}$. The second option reads the bottoms forwards.",
                   ["Rational(1,8) < Rational(1,4)", "Rational(1,4) < Rational(1,2)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Unit Fractions\"",
                    "One piece of every cut, and the backwards rule — bigger bottom, smaller piece. Next: taking MORE than one piece, where the top number finally starts counting past $1$.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Non-Unit Fractions
# ==========================================================================

def lesson_non_unit_fractions():
    na, da = 3, 4  # three quarters, the anchor example
    fig_three_quarters = fig_bar(na, da, "%d of %d equal pieces shaded" % (na, da))
    fig_five_eighths = fig_bar(5, 8, "5 of 8 equal pieces shaded")
    fig_two_thirds = fig_bar(2, 3, "2 of 3 equal pieces shaded")
    fig_three_eighths = fig_bar(3, 8, "3 of 8 equal pieces shaded")
    fig_whole_eighths = fig_bar(8, 8, "all 8 pieces shaded: one whole")
    fig_four_sixths = fig_bar(4, 6, "4 of 6 equal pieces shaded")
    fig_four_fifths = fig_bar(4, 5, "4 of 5 equal pieces shaded")
    fig_seven_tenths = fig_bar(7, 10, "7 of 10 equal pieces shaded")
    return {
        "slug": "non-unit-fractions",
        "title": "Non-Unit Fractions",
        "concreteComparison": (
            "A chocolate bar snaps into $4$ equal pieces. Each piece "
            "is $\\frac{1}{4}$ — you know that. Now take THREE of "
            "them. You hold three pieces of the quarter size: "
            "$\\frac{3}{4}$ of the bar. The top number finally earns "
            "its keep — it counts the pieces you took."),
        "objective": (
            "Read and write non-unit fractions as several unit "
            "pieces, tell what the numerator and denominator each "
            "do, and recognise the fractions that equal one whole."),
        "concept": [
            "**A non-unit fraction is a stack of unit pieces.** "
            "$\\frac{3}{4}$ is three pieces of the $\\frac{1}{4}$ "
            "size: $3 \\times \\frac{1}{4} = \\frac{3}{4}$. Same "
            "cut as $\\frac{1}{4}$ — just more pieces taken.",
            "**The numerator counts, the denominator names.** Those "
            "are the proper names of the two numbers: the TOP number "
            "is the numerator, the BOTTOM number is the denominator. "
            "In $\\frac{5}{8}$ the denominator $8$ names the cut "
            "(eighths) and the numerator $5$ counts the pieces taken. "
            "The bottom number cuts, the top number counts.",
            "**When the top reaches the bottom, you hold the "
            "whole.** Take ALL $4$ quarters and you have "
            "$\\frac{4}{4} = 1$ — the entire bar. Every cut has its "
            "whole-name: $\\frac{6}{6}$, $\\frac{8}{8}$, "
            "$\\frac{10}{10}$ all equal $1$.",
        ],
        "keyIdea": (
            "The top number counts pieces, the bottom number names "
            "the cut — and when the top reaches the bottom, the "
            "pieces rebuild exactly one whole."),
        "facts": [
            {"title": "A stack of unit pieces",
             "latex": "\\frac{3}{4} = 3 \\times \\frac{1}{4}",
             "explanation": "Three quarter-pieces in one hand — that is all a non-unit fraction is."},
            {"title": "The whole, rebuilt",
             "latex": "\\frac{4}{4} = 1",
             "explanation": "All the pieces of the cut together: exactly one whole, never more, never less."},
        ],
        "workedExamples": [
            {"id": "g4fr-l3-we1",
             "statement": "A bar is cut into $4$ equal pieces and $3$ are shaded. What fraction is shaded, and what is it made of?",
             "note": "Name the cut first, then count the pieces.",
             "solution": ("The cut: quarters, each $\\frac{1}{4}$. The count: $3$ "
                          "pieces. Shaded: $\\frac{3}{4}$ — three pieces of the "
                          "quarter size, $3 \\times \\frac{1}{4} = \\frac{3}{4}$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*Rational(1,4), Rational(3,4))", "Rational(3,4) < 1"]},
            {"id": "g4fr-l3-we2",
             "statement": "All $6$ pieces of a $6$-piece bar are shaded. Write the shaded fraction, and give its other name.",
             "note": "The top has reached the bottom.",
             "solution": ("Shaded: $\\frac{6}{6}$ — six pieces of the sixth size, "
                          "$6 \\times \\frac{1}{6} = 1$. Its other name is $1$: the "
                          "whole bar."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6*Rational(1,6), 1)", "Eq(Rational(6,6), 1)"]},
        ],
        "commonMistakes": [
            {"text": "Reading 3/4 as two separate numbers, \"3 and 4\".",
             "correction": "A fraction is ONE amount: three pieces of the quarter size. The bar between the numbers is not a comma.",
             "authored": True},
            {"text": "Thinking 4/4 means 4 wholes.",
             "correction": "4/4 is four QUARTER pieces — together exactly one whole. The top counts pieces of the cut, not wholes.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4fr-l3-t1",
             "statement": "A bar of $8$ equal pieces has $5$ shaded. What fraction is shaded, and what fraction is plain?",
             "solution": "Shaded: $5$ pieces of the eighth size, $\\frac{5}{8}$. Plain: the other $3$ pieces, $\\frac{3}{8}$ — since $5 + 3 = 8$, together they use every piece of the bar.",
             "check": ["Eq(5*Rational(1,8), Rational(5,8))", "Eq(5 + 3, 8)",
                       "Eq(Rational(5,8) + Rational(3,8), 1)"]},
            {"id": "g4fr-l3-t2",
             "statement": "Write the fraction with denominator $8$ that equals one whole.",
             "solution": "$\\frac{8}{8} = 1$: all eight eighth-pieces together rebuild the bar, $8 \\times \\frac{1}{8} = 1$ ✓.",
             "check": ["Eq(8*Rational(1,8), 1)", "Eq(Rational(8,8), 1)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Stacks of unit pieces", [
                "The bar below is cut into $%d$ equal pieces and $%d$ are shaded. Each piece is $\\frac{1}{%d}$; three of them together are $\\frac{%d}{%d}$." % (da, na, da, na, da),
                "That is every non-unit fraction's secret: $\\frac{3}{4}$ is just $3$ pieces of the $\\frac{1}{4}$ size — $3 \\times \\frac{1}{4} = \\frac{3}{4}$.",
                "The two numbers keep their jobs: THE BOTTOM NUMBER CUTS (quarters), THE TOP NUMBER COUNTS (three of them).",
                "Both numbers have proper names too: the top number is the NUMERATOR (the counter) and the bottom number is the DENOMINATOR (the cutter). Same two jobs, longer names.",
            ]), fig_three_quarters),
            workedset("Name the cut, count the pieces",
                      "Bottom first, top second — always that order.", [
                withfig(wex("A bar of $8$ equal pieces has $5$ shaded. What fraction is shaded?",
                    ["The cut: eighths. The count: $5$ pieces.",
                     "$\\frac{5}{8}$ — five pieces of the eighth size, $5 \\times \\frac{1}{8} = \\frac{5}{8}$."],
                    "$\\frac{5}{8}$",
                    ["Eq(5*Rational(1,8), Rational(5,8))", "Rational(5,8) < 1"]), fig_five_eighths),
                wex("You eat $2$ pieces of a khuushuur cut into $5$ equal pieces. What fraction did you eat?",
                    ["The cut: fifths. The count: $2$ eaten.",
                     "$\\frac{2}{5}$ — two pieces of the fifth size, $2 \\times \\frac{1}{5} = \\frac{2}{5}$."],
                    "$\\frac{2}{5}$",
                    ["Eq(2*Rational(1,5), Rational(2,5))", "Rational(2,5) < 1"]),
            ]),
            tryitset("Top counts, bottom names", "Read the picture in the rule's order.", [
                withfig(tp("The bar shows $3$ equal pieces with $2$ shaded. The shaded fraction is:",
                   ["$\\frac{2}{3}$", "$\\frac{3}{2}$", "$\\frac{1}{3}$"],
                   "Cut into thirds, $2$ taken: $\\frac{2}{3} = 2 \\times \\frac{1}{3}$ ✓. $\\frac{3}{2}$ swaps the jobs, and $\\frac{1}{3}$ counts only one piece.",
                   ["Eq(2*Rational(1,3), Rational(2,3))"]), fig_two_thirds),
                tp("In $\\frac{5}{6}$, the $5$ tells you:",
                   ["you take $5$ pieces", "the whole is cut into $5$ parts", "each piece is worth $5$"],
                   "The top counts: five pieces of the sixth size, $5 \\times \\frac{1}{6} = \\frac{5}{6}$. Cutting is the bottom number's job — here the cut is $6$.",
                   ["Eq(5*Rational(1,6), Rational(5,6))"]),
                tp("$\\frac{7}{10}$ means:",
                   ["$7$ pieces of the $\\frac{1}{10}$ size",
                    "$10$ pieces of the $\\frac{1}{7}$ size",
                    "$7$ wholes and $10$ pieces"],
                   "Bottom cuts into tenths, top counts $7$ of them: $7 \\times \\frac{1}{10} = \\frac{7}{10}$. Swapping the numbers' jobs is the trap in the second option.",
                   ["Eq(7*Rational(1,10), Rational(7,10))", "Rational(7,10) < 1"]),
            ]),
            tapq("Count the shaded pieces", "A bar is cut into $8$ equal pieces and $3$ are shaded. The shaded fraction is:",
                 ["$\\frac{3}{8}$", "$\\frac{8}{3}$", "$\\frac{3}{5}$", "$\\frac{5}{8}$"],
                 "Cut: eighths. Count: $3$ shaded. So $\\frac{3}{8} = 3 \\times \\frac{1}{8}$ ✓. $\\frac{5}{8}$ counts the PLAIN pieces, $\\frac{3}{5}$ compares shaded with plain instead of with the whole, and $\\frac{8}{3}$ swaps the jobs.",
                 ["Eq(3*Rational(1,8), Rational(3,8))", "Eq(3 + 5, 8)"]),
            funfact("Quarter past, half past",
                    "Clock talk is fraction talk. An hour is $60$ minutes, and a quarter of it is $60 \\div 4 = 15$ minutes — so \"quarter past three\" means $15$ minutes after three o'clock. \"Half past\" uses $60 \\div 2 = 30$. People tell fractions of an hour every single day without noticing."),
            withfig(teach("Concept B", "When the top reaches the bottom", [
                "Take ALL the pieces of a cut and you hold the whole thing. The bar below has all $8$ of its $8$ pieces shaded: $\\frac{8}{8} = 1$.",
                "Every cut has a whole-name like this: $\\frac{4}{4}$, $\\frac{6}{6}$, $\\frac{10}{10}$ — all of them exactly $1$, because all the pieces together rebuild the whole.",
                "And the pieces always account for everything: if $5$ of $8$ pieces are shaded, the plain part is the other $3$ pieces — $\\frac{3}{8}$. Shaded pieces and plain pieces use all $8$ between them.",
            ]), fig_whole_eighths),
            workedset("The whole, and the rest",
                      "All the pieces make 1; the plain part is the missing count.", [
                wex("Write the fraction with denominator $10$ that equals one whole.",
                    ["All ten tenth-pieces: $\\frac{10}{10}$.",
                     "Rebuild check: $10 \\times \\frac{1}{10} = 1$ ✓."],
                    "$\\frac{10}{10} = 1$",
                    ["Eq(10*Rational(1,10), 1)", "Eq(Rational(10,10), 1)"]),
                withfig(wex("A bar of $6$ equal pieces has $4$ shaded. What fraction is plain?",
                    ["Plain pieces: $6 - 4 = 2$, and $2 + 4 = 6$ ✓ accounts for every piece.",
                     "Plain fraction: $\\frac{2}{6}$ — together with $\\frac{4}{6}$ the bar is whole."],
                    "$\\frac{2}{6}$",
                    ["Eq(2 + 4, 6)", "Eq(Rational(4,6) + Rational(2,6), 1)"]), fig_four_sixths),
            ]),
            tryitset("Wholes and leftovers", "The top meets the bottom, or falls short.", [
                tp("Which fraction equals $1$?",
                   ["$\\frac{9}{9}$", "$\\frac{1}{9}$", "$\\frac{9}{10}$"],
                   "All nine ninth-pieces rebuild the whole: $9 \\times \\frac{1}{9} = 1$ ✓. $\\frac{1}{9}$ is one thin piece, and $\\frac{9}{10}$ stops one piece short of the whole.",
                   ["Eq(9*Rational(1,9), 1)", "Rational(9,10) < 1"]),
                tp("You walk $\\frac{4}{10}$ of a path to the well. The fraction still ahead is:",
                   ["$\\frac{6}{10}$", "$\\frac{4}{10}$", "$\\frac{10}{10}$"],
                   "The path has $10$ tenth-parts; $4$ are behind you, so $10 - 4 = 6$ remain — $\\frac{6}{10}$, and $6 + 4 = 10$ ✓ accounts for the whole path.",
                   ["Eq(6 + 4, 10)", "Eq(Rational(4,10) + Rational(6,10), 1)"]),
                tp("How many $\\frac{1}{6}$ pieces are inside $\\frac{5}{6}$?",
                   ["$5$", "$6$", "$1$"],
                   "$\\frac{5}{6}$ is a stack of five sixth-pieces: $5 \\times \\frac{1}{6} = \\frac{5}{6}$ ✓. Six of them would already be the whole.",
                   ["Eq(5*Rational(1,6), Rational(5,6))", "Eq(6*Rational(1,6), 1)"]),
            ]),
            tapq("The top meets the bottom", "$\\frac{8}{8}$ of a khuushuur is:",
                 ["the whole khuushuur",
                  "$8$ khuushuur",
                  "one eighth of it",
                  "nothing at all"],
                 "Eight pieces of the eighth size: $8 \\times \\frac{1}{8} = 1$ — the whole khuushuur, exactly. It is not $8$ khuushuur: the top counts pieces of ONE whole, never wholes.",
                 ["Eq(8*Rational(1,8), 1)", "Eq(Rational(8,8), 1)"]),
            recap([
                "A non-unit fraction is a stack of unit pieces: 3/4 is three 1/4 pieces.",
                "The top number — the NUMERATOR — counts the pieces taken; the bottom number — the DENOMINATOR — names the cut.",
                "When the top reaches the bottom, the fraction equals 1 — the whole.",
                "Shaded and plain pieces together account for every piece of the bar.",
                "The bottom number cuts, the top number counts — same rule, bigger tops.",
            ]),
            tip("For every fraction below, say the cut first (\"eighths\"), then the count (\"five of them\") — the bottom cuts, the top counts."),
            tryitset("Mixed practice", "Stacks, wholes, and leftovers together.", [
                withfig(tp("The bar shows $5$ equal pieces with $4$ shaded. The shaded fraction is:",
                   ["$\\frac{4}{5}$", "$\\frac{5}{4}$", "$\\frac{1}{5}$"],
                   "Cut into fifths, $4$ taken: $\\frac{4}{5} = 4 \\times \\frac{1}{5}$ ✓. $\\frac{5}{4}$ swaps the jobs; $\\frac{1}{5}$ counts the plain piece instead.",
                   ["Eq(4*Rational(1,5), Rational(4,5))", "Eq(4 + 1, 5)"]), fig_four_fifths),
                tp("$\\frac{5}{9}$ is a stack of:",
                   ["$5$ pieces of the $\\frac{1}{9}$ size",
                    "$9$ pieces of the $\\frac{1}{5}$ size",
                    "$5$ whole bars"],
                   "Bottom cuts into ninths, top counts five: $5 \\times \\frac{1}{9} = \\frac{5}{9}$ ✓. The second option swaps the numbers' jobs.",
                   ["Eq(5*Rational(1,9), Rational(5,9))", "Rational(5,9) < 1"]),
                withfig(tp("The bar shows $10$ pieces with $7$ shaded. The PLAIN fraction is:",
                   ["$\\frac{3}{10}$", "$\\frac{7}{10}$", "$\\frac{3}{7}$"],
                   "Plain pieces: $10 - 7 = 3$, and $3 + 7 = 10$ ✓. So $\\frac{3}{10}$. $\\frac{7}{10}$ is the SHADED part, and $\\frac{3}{7}$ compares plain with shaded instead of with the whole.",
                   ["Eq(3 + 7, 10)", "Eq(Rational(7,10) + Rational(3,10), 1)"]), fig_seven_tenths),
                tp("Which fraction equals one whole?",
                   ["$\\frac{7}{7}$", "$\\frac{7}{8}$", "$\\frac{1}{7}$"],
                   "All seven sevenths: $7 \\times \\frac{1}{7} = 1$ ✓. $\\frac{7}{8}$ falls one eighth-piece short, and $\\frac{1}{7}$ is a single piece.",
                   ["Eq(7*Rational(1,7), 1)", "Rational(7,8) < 1"]),
                tp("A ger's roof has $6$ equal felt panels; $5$ are already tied on. The tied-on fraction is:",
                   ["$\\frac{5}{6}$", "$\\frac{6}{5}$", "$\\frac{1}{6}$"],
                   "Cut: sixths. Count: $5$ tied on. $\\frac{5}{6} = 5 \\times \\frac{1}{6}$ ✓ — with $1$ panel, $\\frac{1}{6}$, still to go, since $5 + 1 = 6$.",
                   ["Eq(5*Rational(1,6), Rational(5,6))", "Eq(5 + 1, 6)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Non-Unit Fractions\"",
                    "The top number counts stacks of unit pieces, and when it reaches the bottom you hold the whole. Next: putting two fractions side by side and deciding which is bigger — by MEANING, not by tricks.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Comparing Fractions
# ==========================================================================

def lesson_comparing():
    ca_n1, ca_n2, ca_d = 5, 3, 8  # same-denominator pair: 5/8 vs 3/8
    cb_d1, cb_d2 = 3, 8  # unit pair: 1/3 vs 1/8
    fig_five_e = fig_bar(ca_n1, ca_d, "%d of %d pieces shaded" % (ca_n1, ca_d))
    fig_three_e = fig_bar(ca_n2, ca_d, "%d of %d pieces shaded" % (ca_n2, ca_d))
    fig_two_fifths = fig_bar(2, 5, "2 of 5 pieces shaded")
    fig_one_third = fig_bar(1, cb_d1, "1 of %d pieces: a big piece" % cb_d1)
    fig_one_eighth = fig_bar(1, cb_d2, "1 of %d pieces: a small piece" % cb_d2)
    fig_four_sixths = fig_bar(4, 6, "4 of 6 pieces shaded")
    fig_one_half = fig_bar(1, 2, "1 of 2 pieces: one half")
    return {
        "slug": "comparing-fractions",
        "title": "Comparing Fractions",
        "concreteComparison": (
            "Two same-size chocolate bars, both cut into $8$ pieces. "
            "You shade $5$ pieces of yours; your friend shades $3$ "
            "of hers. Whose shaded part is bigger? The pieces match "
            "exactly — so just COUNT them: $5$ beats $3$. Comparing "
            "fractions starts with looking at the pieces, never with "
            "tricks."),
        "objective": (
            "Compare two fractions with the same denominator by "
            "counting pieces, compare two unit fractions by piece "
            "size, and always check that both fractions talk about "
            "the same whole."),
        "concept": [
            "**Same bottom: count the pieces.** $\\frac{5}{8}$ and "
            "$\\frac{3}{8}$ are stacks of the SAME piece — eighths. "
            "Same-size pieces compare by counting: $5 > 3$, so "
            "$\\frac{5}{8} > \\frac{3}{8}$.",
            "**Unit fractions: the bigger bottom loses.** "
            "$\\frac{1}{3}$ and $\\frac{1}{8}$ are ONE piece each, "
            "but a $3$-cut makes big pieces and an $8$-cut makes "
            "small ones: $\\frac{1}{3} > \\frac{1}{8}$.",
            "**Only same wholes compare.** Half of a small "
            "khuushuur can be less food than a quarter of a giant "
            "one. Fraction comparisons are promises about the SAME "
            "whole — check that before comparing anything.",
        ],
        "keyIdea": (
            "Same cut: more pieces wins. One piece each: the finer "
            "cut loses. And both fractions must talk about the same "
            "whole, or the comparison means nothing."),
        "facts": [
            {"title": "Same pieces, just count",
             "latex": "\\frac{5}{8} > \\frac{3}{8}",
             "explanation": "Eighths against eighths — the pieces match, so the bigger count wins."},
            {"title": "One piece each, size decides",
             "latex": "\\frac{1}{8} < \\frac{1}{3}",
             "explanation": "An 8-cut makes smaller pieces than a 3-cut — the bigger bottom loses."},
        ],
        "workedExamples": [
            {"id": "g4fr-l4-we1",
             "statement": "Compare $\\frac{5}{8}$ and $\\frac{3}{8}$ of the same bar.",
             "note": "The bottoms match — the pieces are the same size.",
             "solution": ("Both are stacks of eighth-pieces. Count them: $5 > 3$, "
                          "so $\\frac{5}{8} > \\frac{3}{8}$."),
             "badges": [{"text": "core"}],
             "check": ["Rational(5,8) > Rational(3,8)", "5 > 3"]},
            {"id": "g4fr-l4-we2",
             "statement": "Compare $\\frac{1}{6}$ and $\\frac{1}{9}$ of the same cake.",
             "note": "One piece each — compare the cuts.",
             "solution": ("One piece each, but a $6$-cut makes bigger pieces than a "
                          "$9$-cut: $\\frac{1}{6} > \\frac{1}{9}$, even though "
                          "$9 > 6$."),
             "badges": [{"text": "core"}],
             "check": ["Rational(1,6) > Rational(1,9)", "9 > 6"]},
        ],
        "commonMistakes": [
            {"text": "Choosing 1/8 over 1/4 because 8 is the bigger number.",
             "correction": "For unit fractions the bottom counts SHARERS: more sharers, smaller shares. 1/8 < 1/4 — the bigger bottom loses.",
             "authored": True},
            {"text": "Comparing fractions of different wholes — half of a small khuushuur against a quarter of a giant one.",
             "correction": "Fractions only compare when they cut the SAME whole. Before writing < or >, check that both fractions talk about one and the same thing.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4fr-l4-t1",
             "statement": "Which is bigger: $\\frac{4}{7}$ or $\\frac{6}{7}$ of the same bread?",
             "solution": "Same cut — sevenths — so count the pieces: $6 > 4$, and $\\frac{6}{7} > \\frac{4}{7}$.",
             "check": ["Rational(6,7) > Rational(4,7)", "6 > 4"]},
            {"id": "g4fr-l4-t2",
             "statement": "Which is bigger: $\\frac{1}{3}$ or $\\frac{1}{8}$ of the same bread?",
             "solution": "One piece each: the $3$-cut makes bigger pieces than the $8$-cut, so $\\frac{1}{3} > \\frac{1}{8}$.",
             "check": ["Rational(1,3) > Rational(1,8)", "8 > 3"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Same cut: count the pieces", [
                "Two same-size bars, both cut into $%d$. The bar below shows $%d$ shaded pieces; picture a second bar with only $%d$ shaded." % (ca_d, ca_n1, ca_n2),
                "The pieces are IDENTICAL — eighths against eighths — so the comparison is pure counting: $%d > %d$, and $\\frac{%d}{%d} > \\frac{%d}{%d}$." % (ca_n1, ca_n2, ca_n1, ca_d, ca_n2, ca_d),
                "Whenever the bottoms match, the cut is the same, and the top numbers settle it. The bottom cuts, the top counts — and here only the counting differs.",
            ]), fig_five_e),
            workedset("Matching bottoms",
                      "Same pieces — the bigger count wins.", [
                withfig(wex("Compare $\\frac{%d}{%d}$ and $\\frac{%d}{%d}$ of the same bar." % (ca_n1, ca_d, ca_n2, ca_d),
                    ["Bottoms match: both are stacks of eighth-pieces.",
                     "Count: $%d > %d$, so $\\frac{%d}{%d} > \\frac{%d}{%d}$." % (ca_n1, ca_n2, ca_n1, ca_d, ca_n2, ca_d)],
                    "$\\frac{5}{8} > \\frac{3}{8}$",
                    ["Rational(5,8) > Rational(3,8)", "5 > 3"]), fig_three_e),
                wex("Order $\\frac{2}{6}$, $\\frac{5}{6}$, $\\frac{3}{6}$ from smallest to biggest.",
                    ["All sixths — pure counting: $2 < 3 < 5$.",
                     "$\\frac{2}{6} < \\frac{3}{6} < \\frac{5}{6}$."],
                    "$\\frac{2}{6} < \\frac{3}{6} < \\frac{5}{6}$",
                    ["Rational(2,6) < Rational(3,6)", "Rational(3,6) < Rational(5,6)"]),
            ]),
            tryitset("Count the matching pieces", "Bottoms match, tops decide.", [
                tp("Which is bigger: $\\frac{7}{10}$ or $\\frac{9}{10}$ of the same bar?",
                   ["$\\frac{9}{10}$", "$\\frac{7}{10}$", "they are equal"],
                   "Tenths against tenths — count them: $9 > 7$, so $\\frac{9}{10} > \\frac{7}{10}$.",
                   ["Rational(9,10) > Rational(7,10)", "9 > 7"]),
                withfig(tp("The bar shows $\\frac{2}{5}$ shaded. Compared with $\\frac{4}{5}$ of the same bar, it is:",
                   ["less — $2$ pieces against $4$ of the same size",
                    "more — $2$ comes before $4$",
                    "equal"],
                   "Fifths against fifths: $2 < 4$, so $\\frac{2}{5} < \\frac{4}{5}$. The pieces match, so only the count matters.",
                   ["Rational(2,5) < Rational(4,5)", "4 > 2"]), fig_two_fifths),
                tp("The largest of $\\frac{3}{7}$, $\\frac{6}{7}$, $\\frac{5}{7}$ is:",
                   ["$\\frac{6}{7}$", "$\\frac{3}{7}$", "$\\frac{5}{7}$"],
                   "All sevenths — count: $6 > 5 > 3$, so $\\frac{6}{7}$ wins.",
                   ["Rational(6,7) > Rational(5,7)", "Rational(5,7) > Rational(3,7)"]),
            ]),
            tapq("Same pieces, just count", "$\\frac{5}{9}$ and $\\frac{7}{9}$ of the same cake — which is more?",
                 ["$\\frac{7}{9}$ — seven pieces beat five of the same size",
                  "$\\frac{5}{9}$ — the smaller top number means bigger pieces",
                  "they are equal — same bottom",
                  "they cannot be compared"],
                 "Both are stacks of ninth-pieces, so the count decides: $7 > 5$ and $\\frac{7}{9} > \\frac{5}{9}$. \"Smaller number, bigger pieces\" is the BOTTOM number's backwards rule, and here the bottoms already match — the pieces are the same size, so only the top count is left to decide. A matching bottom means matching PIECES, not matching amounts.",
                 ["Rational(7,9) > Rational(5,9)", "7 > 5"]),
            funfact("Games are cut into fractions",
                    "A basketball game is played in four quarters — four equal parts of the playing time, exactly like a bar cut into $4$. Football uses halves instead: two equal parts with the break in the middle. Sports announcers say fraction names all day long."),
            withfig(teach("Concept B", "One piece each: the finer cut loses", [
                "Now the tops match instead: $\\frac{1}{%d}$ against $\\frac{1}{%d}$ — one piece each. The bar below shows the $%d$-cut: big, generous pieces." % (cb_d1, cb_d2, cb_d1),
                "The $%d$-cut shares the SAME whole among far more pieces, so each one is small. One big piece beats one small piece: $\\frac{1}{%d} > \\frac{1}{%d}$." % (cb_d2, cb_d1, cb_d2),
                "One warning before any comparing: both fractions must cut the SAME whole. Half of a small khuushuur can be less food than a quarter of a giant one — fractions of different wholes do not compare.",
            ]), fig_one_third),
            workedset("Unit against unit",
                      "One piece each — the coarser cut wins.", [
                withfig(wex("Which is bigger: $\\frac{1}{%d}$ or $\\frac{1}{%d}$ of the same bread?" % (cb_d1, cb_d2),
                    ["One piece each; the $%d$-cut makes small pieces (see the bar)." % cb_d2,
                     "$\\frac{1}{%d} > \\frac{1}{%d}$ — the bigger bottom loses." % (cb_d1, cb_d2)],
                    "$\\frac{1}{3}$",
                    ["Rational(1,3) > Rational(1,8)", "8 > 3"]), fig_one_eighth),
                wex("Order $\\frac{1}{2}$, $\\frac{1}{5}$, $\\frac{1}{10}$ from biggest to smallest.",
                    ["Fewest sharers first: $2$-cut, then $5$-cut, then $10$-cut.",
                     "$\\frac{1}{2} > \\frac{1}{5} > \\frac{1}{10}$."],
                    "$\\frac{1}{2} > \\frac{1}{5} > \\frac{1}{10}$",
                    ["Rational(1,2) > Rational(1,5)", "Rational(1,5) > Rational(1,10)"]),
            ]),
            tryitset("One piece each", "Picture the cut before choosing.", [
                tp("Which is bigger: $\\frac{1}{7}$ or $\\frac{1}{4}$ of the same cake?",
                   ["$\\frac{1}{4}$", "$\\frac{1}{7}$", "they are equal"],
                   "A $4$-cut makes bigger pieces than a $7$-cut: $\\frac{1}{4} > \\frac{1}{7}$. Picking $\\frac{1}{7}$ because $7 > 4$ reads the bottom forwards — the trap.",
                   ["Rational(1,4) > Rational(1,7)", "7 > 4"]),
                tp("The smallest of $\\frac{1}{6}$, $\\frac{1}{2}$, $\\frac{1}{9}$ is:",
                   ["$\\frac{1}{9}$", "$\\frac{1}{6}$", "$\\frac{1}{2}$"],
                   "The finest cut loses: nine pieces share the whole, so $\\frac{1}{9} < \\frac{1}{6} < \\frac{1}{2}$.",
                   ["Rational(1,9) < Rational(1,6)", "Rational(1,6) < Rational(1,2)"]),
                tp("Naran gets $\\frac{1}{5}$ of a cake and Bold gets $\\frac{1}{8}$ of the SAME cake. Who gets more?",
                   ["Naran", "Bold", "equal shares"],
                   "Same whole, one piece each: the $5$-cut gives bigger pieces than the $8$-cut, so $\\frac{1}{5} > \\frac{1}{8}$ — Naran. Bold's $8$ only looks bigger.",
                   ["Rational(1,5) > Rational(1,8)", "8 > 5"]),
            ]),
            tapq("The forwards-reading trap", "Which is bigger: $\\frac{1}{6}$ or $\\frac{1}{9}$?",
                 ["$\\frac{1}{6}$ — sixth-pieces are bigger than ninth-pieces",
                  "$\\frac{1}{9}$ — because $9$ beats $6$",
                  "they are equal — both are one piece",
                  "they cannot be compared"],
                 "One piece each, so size decides: a $6$-cut shares the whole among fewer pieces than a $9$-cut, so $\\frac{1}{6} > \\frac{1}{9}$. \"$9$ beats $6$\" is the forwards-reading trap — unit fractions read backwards.",
                 ["Rational(1,6) > Rational(1,9)", "9 > 6"]),
            recap([
                "Same bottom: the pieces match, so the bigger count wins.",
                "Unit fractions: one piece each, and the bigger bottom loses.",
                "Never pick a unit fraction just because its bottom number is bigger.",
                "Fractions only compare when they cut the SAME whole.",
                "Every comparison here is done by meaning — picture the pieces.",
            ]),
            tip("Before each answer, say which case you are in: matching bottoms (count the pieces) or one piece each (the finer cut loses)."),
            tryitset("Mixed practice", "Both comparing rules, side by side.", [
                withfig(tp("The bar shows $\\frac{4}{6}$ shaded. Compared with $\\frac{1}{6}$ of the same bar:",
                   ["$\\frac{4}{6}$ is bigger — four sixths against one",
                    "$\\frac{1}{6}$ is bigger",
                    "they are equal"],
                   "Matching bottoms: sixths against sixths, and $4 > 1$, so $\\frac{4}{6} > \\frac{1}{6}$.",
                   ["Rational(4,6) > Rational(1,6)", "4 > 1"]), fig_four_sixths),
                withfig(tp("The bar shows one half. Which is bigger: $\\frac{1}{2}$ or $\\frac{1}{6}$ of the same bar?",
                   ["$\\frac{1}{2}$", "$\\frac{1}{6}$", "they are equal"],
                   "One piece each: a $2$-cut makes far bigger pieces than a $6$-cut, so $\\frac{1}{2} > \\frac{1}{6}$ — even though $6 > 2$.",
                   ["Rational(1,2) > Rational(1,6)", "6 > 2"]), fig_one_half),
                tp("Sara read $\\frac{7}{10}$ of a book and Dulguun read $\\frac{9}{10}$ of the SAME book. Who read more?",
                   ["Dulguun", "Sara", "they read the same amount"],
                   "Same book, same tenth-pieces: $9 > 7$, so $\\frac{9}{10} > \\frac{7}{10}$ — Dulguun.",
                   ["Rational(9,10) > Rational(7,10)"]),
                tp("One melon is shared equally by $3$ children, an identical melon by $10$. A bigger piece comes from:",
                   ["the melon shared by $3$", "the melon shared by $10$", "both pieces are equal"],
                   "Fewer sharers, bigger pieces: $\\frac{1}{3} > \\frac{1}{10}$. Ten sharers make thin slices of the same melon.",
                   ["Rational(1,3) > Rational(1,10)", "10 > 3"]),
                tp("Which comparison is TRUE?",
                   ["$\\frac{2}{9} < \\frac{7}{9}$",
                    "$\\frac{1}{5} < \\frac{1}{10}$",
                    "$\\frac{3}{8} > \\frac{7}{8}$"],
                   "Ninths against ninths: $2 < 7$ ✓. The second option falls for the forwards trap ($\\frac{1}{5}$ is the BIGGER piece), and the third counts backwards ($3 < 7$ with matching eighths).",
                   ["Rational(2,9) < Rational(7,9)",
                    "Rational(1,10) < Rational(1,5)",
                    "Rational(3,8) < Rational(7,8)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Comparing Fractions\"",
                    "Matching bottoms count pieces; matching tops of $1$ compare cuts — and everything happens on the same whole. Next: fractions leave the chocolate bar and start counting SHEEP — a fraction of a whole set of things.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — A Fraction of a Set
# ==========================================================================

def lesson_fraction_of_set():
    sn, sd, sq = 12, 3, 4      # 1/3 of 12 sheep: 3 groups of 4
    tn, tq = 2, 8              # 2/3 of 12: two groups, 8 sheep
    wn, wd, wq = 20, 4, 5      # 1/4 of 20: 4 groups of 5
    fig_share = fig_groups(*[(sq, "group %d" % (i + 1)) for i in range(sd)])
    fig_twothirds = fig_groups((sq, "taken", C_GREEN), (sq, "taken too", C_GREEN),
                               (sq, "stays", C_NEUTRAL))
    fig_quarters20 = fig_groups(*[(wq, "group %d" % (i + 1)) for i in range(wd)])
    fig_sixths24 = fig_groups(*[(4, "group %d" % (i + 1)) for i in range(6)])
    fig_threequarters20 = fig_groups((wq, "taken 1", C_GREEN), (wq, "taken 2", C_GREEN),
                                     (wq, "taken 3", C_GREEN), (wq, "stays", C_NEUTRAL))
    fig_fifths10 = fig_groups(*[(2, "group %d" % (i + 1)) for i in range(5)])
    return {
        "slug": "fraction-of-a-set",
        "title": "A Fraction of a Set",
        "concreteComparison": (
            "A herder's $12$ sheep drift into $3$ equal flocks of "
            "$4$. One flock — $4$ sheep — is $\\frac{1}{3}$ of the "
            "herd. Two flocks — $8$ sheep — are $\\frac{2}{3}$ of "
            "it. The whole is not a bar of chocolate any more: it is "
            "a SET of things, and the fraction shares it into "
            "groups."),
        "objective": (
            "Find a unit fraction of a set by sharing into equal "
            "groups, then a non-unit fraction by taking several of "
            "those groups — checking every division by multiplying "
            "back."),
        "concept": [
            "**The whole can be a set.** $\\frac{1}{3}$ OF $12$ "
            "sheep: share the $12$ into $3$ equal groups — $12 \\div "
            "3 = 4$ in each — and take one group. $\\frac{1}{3}$ of "
            "$12$ is $4$.",
            "**The bottom cuts the set, the top counts the "
            "groups.** For $\\frac{2}{3}$ of $12$: the bottom cuts "
            "the herd into $3$ groups of $4$; the top takes $2$ of "
            "them — $2 \\times 4 = 8$ sheep.",
            "**Multiply back to check.** The sharing step is a "
            "division, and every division signs a receipt: $12 \\div "
            "3 = 4$ because $4 \\times 3 = 12$. If the receipt "
            "fails, the groups were not equal.",
        ],
        "keyIdea": (
            "A fraction of a set is found in two moves: the bottom "
            "number shares the set into equal groups, the top number "
            "takes that many groups."),
        "facts": [
            {"title": "The bottom shares",
             "latex": "\\frac{1}{3} \\text{ of } 12 = 12 \\div 3 = 4",
             "explanation": "Share into 3 equal groups; one group is one third of the set."},
            {"title": "The top takes groups",
             "latex": "\\frac{2}{3} \\text{ of } 12 = 2 \\times 4 = 8",
             "explanation": "Two of the three groups — the top number counts groups, not single things."},
        ],
        "workedExamples": [
            {"id": "g4fr-l5-we1",
             "statement": "Find $\\frac{1}{3}$ of $12$ sheep.",
             "note": "Share the herd into 3 equal groups.",
             "solution": ("Share: $12 \\div 3 = 4$ sheep in each group, and the "
                          "receipt $4 \\times 3 = 12$ ✓ rebuilds the herd. One "
                          "group is $\\frac{1}{3}$ of the herd: $4$ sheep."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(12,3), 4)", "Eq(4*3, 12)",
                       "Eq(Rational(1,3)*12, 4)"]},
            {"id": "g4fr-l5-we2",
             "statement": "Find $\\frac{2}{3}$ of the same $12$ sheep.",
             "note": "Same groups — now take two of them.",
             "solution": ("The groups are already made: $3$ groups of $4$. Take "
                          "$2$ groups: $2 \\times 4 = 8$ sheep. So $\\frac{2}{3}$ "
                          "of $12$ is $8$ — and the third group holds the other "
                          "$4$, since $8 + 4 = 12$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*4, 8)", "Eq(Rational(2,3)*12, 8)", "Eq(8 + 4, 12)"]},
        ],
        "commonMistakes": [
            {"text": "Finding 1/3 of 12 by taking 3 away: 12 − 3 = 9.",
             "correction": "OF means share, not subtract: cut the 12 into 3 equal groups, 12 ÷ 3 = 4, and one group — 4 — is one third.",
             "authored": True},
            {"text": "Finding 2/3 of 12 by dividing by the top: 12 ÷ 2 = 6.",
             "correction": "The bottom shares first: 12 ÷ 3 = 4 in each group. Only then does the top count groups: 2 × 4 = 8.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4fr-l5-t1",
             "statement": "Find $\\frac{1}{4}$ of $20$ sweets.",
             "solution": "Share into $4$ equal groups: $20 \\div 4 = 5$, receipt $5 \\times 4 = 20$ ✓. One group — $5$ sweets — is $\\frac{1}{4}$ of the bag.",
             "check": ["Eq(Rational(20,4), 5)", "Eq(5*4, 20)", "Eq(Rational(1,4)*20, 5)"]},
            {"id": "g4fr-l5-t2",
             "statement": "Find $\\frac{3}{4}$ of the same $20$ sweets.",
             "solution": "The groups hold $5$ each; take $3$ groups: $3 \\times 5 = 15$ sweets. So $\\frac{3}{4}$ of $20$ is $15$, with $5$ left in the last group since $15 + 5 = 20$ ✓.",
             "check": ["Eq(Rational(20,4), 5)", "Eq(3*5, 15)",
                       "Eq(Rational(3,4)*20, 15)", "Eq(15 + 5, 20)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Share the set into groups", [
                "$\\frac{1}{%d}$ OF $%d$ sheep — the whole is now a HERD, not a bar. The bottom cuts all the same: share the $%d$ into $%d$ equal groups, as in the picture." % (sd, sn, sn, sd),
                "The sharing is a division: $%d \\div %d = %d$ in each group, and the receipt $%d \\times %d = %d$ ✓ rebuilds the herd." % (sn, sd, sq, sq, sd, sn),
                "Take ONE group: $%d$ sheep. That is $\\frac{1}{%d}$ of $%d$. The bottom number cuts — even when the whole is a flock of animals." % (sq, sd, sn),
            ]), fig_share),
            workedset("Unit fraction of a set",
                      "Share into bottom-many groups; take one.", [
                withfig(wex("Find $\\frac{1}{%d}$ of $%d$ sweets." % (wd, wn),
                    ["Share into $%d$ equal groups: $%d \\div %d = %d$, receipt $%d \\times %d = %d$ ✓." % (wd, wn, wd, wq, wq, wd, wn),
                     "One group is $\\frac{1}{%d}$ of the bag: $%d$ sweets." % (wd, wq)],
                    "$5$ sweets",
                    ["Eq(Rational(20,4), 5)", "Eq(5*4, 20)", "Eq(Rational(1,4)*20, 5)"]), fig_quarters20),
                wex("Find $\\frac{1}{5}$ of $30$ goats.",
                    ["Share into $5$ equal groups: $30 \\div 5 = 6$, receipt $6 \\times 5 = 30$ ✓.",
                     "One group — $6$ goats — is $\\frac{1}{5}$ of the herd."],
                    "$6$ goats",
                    ["Eq(Rational(30,5), 6)", "Eq(6*5, 30)", "Eq(Rational(1,5)*30, 6)"]),
            ]),
            tryitset("One group of the set", "Share first, then take one group.", [
                tp("$\\frac{1}{2}$ of $18$ khuushuur is:",
                   ["$9$", "$2$", "$16$"],
                   "Share into $2$ equal groups: $18 \\div 2 = 9$, receipt $9 \\times 2 = 18$ ✓. $16$ subtracts the $2$ instead of sharing — the OF-means-share rule.",
                   ["Eq(Rational(18,2), 9)", "Eq(9*2, 18)"]),
                tp("$\\frac{1}{3}$ of $15$ horses is:",
                   ["$5$", "$3$", "$12$"],
                   "Share into $3$ equal groups: $15 \\div 3 = 5$, receipt $5 \\times 3 = 15$ ✓. $12$ is $15 - 3$ — subtraction wearing a fraction costume.",
                   ["Eq(Rational(15,3), 5)", "Eq(5*3, 15)"]),
                withfig(tp("$24$ buuz are shared onto $6$ plates, as in the picture. $\\frac{1}{6}$ of the buuz is:",
                   ["$4$", "$6$", "$18$"],
                   "Share into $6$ equal groups: $24 \\div 6 = 4$, receipt $4 \\times 6 = 24$ ✓. One plate — $4$ buuz — is $\\frac{1}{6}$ of the batch.",
                   ["Eq(Rational(24,6), 4)", "Eq(4*6, 24)"]), fig_sixths24),
            ]),
            tapq("What OF does", "To find $\\frac{1}{4}$ of $16$, you:",
                 ["share $16$ into $4$ equal groups and take one — $4$",
                  "take $4$ away from $16$ — $12$",
                  "cut the number $4$ into $16$ parts",
                  "count $4$ wholes of $16$"],
                 "OF shares: $16 \\div 4 = 4$ in each group, receipt $4 \\times 4 = 16$ ✓, and one group is the answer. Taking $4$ away gives $12$ — subtraction, a different question entirely.",
                 ["Eq(Rational(16,4), 4)", "Eq(4*4, 16)"]),
            funfact("One third of every day",
                    "A day holds $24$ hours, and $24 \\div 3 = 8$ — so $8$ hours of sleep is exactly $\\frac{1}{3}$ of a whole day. Many people sleep about that much, which means about one third of a whole life is spent asleep."),
            withfig(teach("Concept B", "Take more than one group", [
                "$\\frac{%d}{%d}$ of $%d$: the bottom has already done its work — $%d$ groups of $%d$. Now the TOP counts groups: take $%d$ of them, the green groups in the picture." % (tn, sd, sn, sd, sq, tn),
                "Two groups of $%d$: $%d \\times %d = %d$ sheep. So $\\frac{%d}{%d}$ of $%d$ is $%d$ — and the grey group keeps the other $%d$, since $%d + %d = %d$ ✓." % (sq, tn, sq, tq, tn, sd, sn, tq, sq, tq, sq, sn),
                "The rule in full: the bottom number cuts the set into equal groups, the top number counts the groups you take. Same rule as the chocolate bar — the pieces are just groups now.",
            ]), fig_twothirds),
            workedset("Non-unit fraction of a set",
                      "Bottom shares, top takes groups.", [
                wex("Find $\\frac{2}{3}$ of $12$ sheep.",
                    ["Share: $12 \\div 3 = 4$ in each group, receipt $4 \\times 3 = 12$ ✓.",
                     "Take $2$ groups: $2 \\times 4 = 8$ sheep."],
                    "$8$ sheep",
                    ["Eq(Rational(12,3), 4)", "Eq(2*4, 8)", "Eq(Rational(2,3)*12, 8)"]),
                withfig(wex("Find $\\frac{3}{%d}$ of $%d$ sweets." % (wd, wn),
                    ["Share: $%d \\div %d = %d$ in each group, receipt $%d \\times %d = %d$ ✓." % (wn, wd, wq, wq, wd, wn),
                     "Take $3$ groups: $3 \\times %d = 15$ sweets — the grey group keeps the last $%d$." % (wq, wq)],
                    "$15$ sweets",
                    ["Eq(Rational(20,4), 5)", "Eq(3*5, 15)",
                     "Eq(Rational(3,4)*20, 15)", "Eq(15 + 5, 20)"]), fig_threequarters20),
            ]),
            tryitset("Groups taken, groups left", "Share, take, and account for the rest.", [
                tp("$\\frac{2}{5}$ of $15$ sweets is:",
                   ["$6$", "$3$", "$10$"],
                   "Share: $15 \\div 5 = 3$ each, receipt $3 \\times 5 = 15$ ✓. Take $2$ groups: $2 \\times 3 = 6$. Answering $3$ stops after the sharing step.",
                   ["Eq(Rational(15,5), 3)", "Eq(2*3, 6)", "Eq(Rational(2,5)*15, 6)"]),
                tp("$\\frac{3}{8}$ of $24$ buuz is:",
                   ["$9$", "$3$", "$8$"],
                   "Share: $24 \\div 8 = 3$ each, receipt $3 \\times 8 = 24$ ✓. Take $3$ groups: $3 \\times 3 = 9$. Answering $3$ stops after the sharing step, and $8$ divides by the TOP number ($24 \\div 3 = 8$) instead of by the bottom one.",
                   ["Eq(Rational(24,8), 3)", "Eq(3*3, 9)", "Eq(Rational(3,8)*24, 9)",
                    "Eq(Rational(24,3), 8)"]),
                tp("$\\frac{3}{3}$ of $12$ horses is:",
                   ["$12$ — all three groups, the whole herd", "$4$", "$9$"],
                   "Share: $12 \\div 3 = 4$ each. Take ALL $3$ groups: $3 \\times 4 = 12$ — the whole herd, because a fraction whose top meets its bottom equals $1$.",
                   ["Eq(Rational(12,3), 4)", "Eq(3*4, 12)"]),
            ]),
            tapq("Top counts groups", "$\\frac{2}{3}$ of $18$ goats is:",
                 ["$12$", "$6$", "$9$", "$16$"],
                 "Share: $18 \\div 3 = 6$ in each group, receipt $6 \\times 3 = 18$ ✓. Take $2$ groups: $2 \\times 6 = 12$. Answering $6$ takes only one group; $9$ is half the herd, a different fraction.",
                 ["Eq(Rational(18,3), 6)", "Eq(2*6, 12)", "Eq(Rational(2,3)*18, 12)"]),
            recap([
                "The whole can be a SET — a herd, a bag, a batch of buuz.",
                "The bottom number shares the set into equal groups (a division, with its receipt).",
                "A unit fraction of a set is one group.",
                "The top number counts how many groups you take: 2/3 of 12 is 2 groups of 4.",
                "The bottom cuts, the top counts — bars, breads, and herds alike.",
            ]),
            tip("Two moves every time: share by the bottom (and sign the division receipt), then take top-many groups. Say both moves before you compute."),
            tryitset("Mixed practice", "Fractions of sets, unit and non-unit.", [
                withfig(tp("$10$ aaruul pieces are shared into $5$ equal groups, as shown. $\\frac{1}{5}$ of them is:",
                   ["$2$", "$5$", "$8$"],
                   "Share: $10 \\div 5 = 2$ each, receipt $2 \\times 5 = 10$ ✓. One group is $2$ pieces. $8$ subtracts instead of sharing.",
                   ["Eq(Rational(10,5), 2)", "Eq(2*5, 10)"]), fig_fifths10),
                tp("$\\frac{3}{5}$ of $20$ togrog coins is:",
                   ["$12$", "$4$", "$15$"],
                   "Share: $20 \\div 5 = 4$ each, receipt $4 \\times 5 = 20$ ✓. Take $3$ groups: $3 \\times 4 = 12$ coins. $4$ stops after sharing; $15$ took $3$ quarters instead of $3$ fifths.",
                   ["Eq(Rational(20,5), 4)", "Eq(3*4, 12)", "Eq(Rational(3,5)*20, 12)"]),
                tp("$\\frac{1}{2}$ of $16$ khuushuur is:",
                   ["$8$", "$2$", "$14$"],
                   "Share into $2$ groups: $16 \\div 2 = 8$, receipt $8 \\times 2 = 16$ ✓. $14$ subtracts the $2$ — OF shares, never subtracts.",
                   ["Eq(Rational(16,2), 8)", "Eq(8*2, 16)"]),
                tp("$\\frac{2}{5}$ of a herd of $25$ goats are white. The white goats number:",
                   ["$10$", "$5$", "$15$"],
                   "Share: $25 \\div 5 = 5$ each, receipt $5 \\times 5 = 25$ ✓. Take $2$ groups: $2 \\times 5 = 10$ white goats. $5$ stops after one group, and $15$ counts the OTHER three groups — the goats that are not white, since $10 + 15 = 25$ ✓.",
                   ["Eq(Rational(25,5), 5)", "Eq(2*5, 10)", "Eq(Rational(2,5)*25, 10)",
                    "Eq(10 + 15, 25)"]),
                tp("$\\frac{5}{6}$ of $30$ sweets is:",
                   ["$25$", "$5$", "$24$"],
                   "Share: $30 \\div 6 = 5$ each, receipt $5 \\times 6 = 30$ ✓. Take $5$ groups: $5 \\times 5 = 25$. Answering $5$ stops at one group.",
                   ["Eq(Rational(30,6), 5)", "Eq(5*5, 25)", "Eq(Rational(5,6)*30, 25)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"A Fraction of a Set\" — and the topic",
                    "Equal parts, unit pieces, stacks of them, honest comparisons, and fractions that count sheep: the whole meaning of a fraction, drawn one bar and one herd at a time. The bottom number cuts, the top number counts — carry that sentence into Grade 5, where fractions learn many names and start to add.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = fig_bar(1, 4, "4 equal parts, 1 shaded")
    fig_pr3 = fig_bar(5, 6, "5 of 6 equal pieces shaded")
    fig_pr6 = fig_groups(*[(6, "group %d" % (i + 1)) for i in range(4)])
    return [
        withprobfig(
            prob("g4fr-pr1", "The bar shows $4$ equal parts with $1$ shaded. Name the shaded part in words and as a fraction.",
                 "Four equal parts are quarters; one of them is one quarter, $\\frac{1}{4}$. Four such parts rebuild the bar: $4 \\times \\frac{1}{4} = 1$ ✓.",
                 ["Eq(4*Rational(1,4), 1)", "Rational(1,4) < 1"]),
            fig_pr1),
        prob("g4fr-pr2", "Order from biggest to smallest: $\\frac{1}{3}$, $\\frac{1}{8}$, $\\frac{1}{5}$.",
             "One piece each, so the coarsest cut wins: $\\frac{1}{3} > \\frac{1}{5} > \\frac{1}{8}$ — the bigger bottom loses.",
             ["Rational(1,3) > Rational(1,5)", "Rational(1,5) > Rational(1,8)"]),
        withprobfig(
            prob("g4fr-pr3", "The bar shows $6$ equal pieces with $5$ shaded. Write the shaded fraction and the plain fraction.",
                 "Shaded: $5$ pieces of the sixth size, $\\frac{5}{6}$. Plain: the remaining $1$ piece, $\\frac{1}{6}$, since $1 + 5 = 6$ accounts for every piece and together they make the whole bar.",
                 ["Eq(5*Rational(1,6), Rational(5,6))", "Eq(1 + 5, 6)",
                  "Eq(Rational(5,6) + Rational(1,6), 1)"]),
            fig_pr3),
        prob("g4fr-pr4", "Which is more: $\\frac{4}{9}$ or $\\frac{7}{9}$ of the same cake?",
             "Matching bottoms mean matching pieces — ninths — so count: $7 > 4$, and $\\frac{7}{9} > \\frac{4}{9}$.",
             ["Rational(7,9) > Rational(4,9)", "7 > 4"]),
        prob("g4fr-pr5", "Which is more: $\\frac{1}{6}$ or $\\frac{1}{10}$ of the same melon?",
             "One piece each: a $6$-cut makes bigger pieces than a $10$-cut, so $\\frac{1}{6} > \\frac{1}{10}$ — even though $10 > 6$.",
             ["Rational(1,6) > Rational(1,10)", "10 > 6"]),
        withprobfig(
            prob("g4fr-pr6", "$24$ sweets are shared into $4$ equal groups, as shown. Find $\\frac{1}{4}$ of the sweets.",
                 "Share: $24 \\div 4 = 6$ in each group, receipt $6 \\times 4 = 24$ ✓. One group — $6$ sweets — is $\\frac{1}{4}$ of the bag.",
                 ["Eq(Rational(24,4), 6)", "Eq(6*4, 24)", "Eq(Rational(1,4)*24, 6)"]),
            fig_pr6),
        prob("g4fr-pr7", "Find $\\frac{3}{4}$ of the same $24$ sweets.",
             "The groups hold $6$ each; take $3$ groups: $3 \\times 6 = 18$ sweets. So $\\frac{3}{4}$ of $24$ is $18$, and the last group keeps $6$, since $18 + 6 = 24$ ✓.",
             ["Eq(Rational(24,4), 6)", "Eq(3*6, 18)",
              "Eq(Rational(3,4)*24, 18)", "Eq(18 + 6, 24)"]),
        prob("g4fr-pr8", "One of the fractions $\\frac{9}{9}$ and $\\frac{9}{10}$ equals one whole. Which one, and why?",
             "$\\frac{9}{9}$: the top has reached the bottom, so all nine ninth-pieces are taken — $9 \\times \\frac{1}{9} = 1$ ✓. $\\frac{9}{10}$ stops one tenth-piece short of the whole.",
             ["Eq(9*Rational(1,9), 1)", "Rational(9,10) < 1"]),
    ]


def test_bank():
    fig_x1 = fig_bar(3, 8, "3 of 8 equal slices taken")
    return [
        withprobfig(
            prob("g4fr-x1", "A pizza is cut into $8$ equal slices and you take $3$, as shown. What fraction did you take, and what fraction remains?",
                 "Taken: $3$ slices of the eighth size, $\\frac{3}{8}$. Remaining: $8 - 3 = 5$ slices, $\\frac{5}{8}$, and $5 + 3 = 8$ ✓ accounts for the whole pizza.",
                 ["Eq(3*Rational(1,8), Rational(3,8))", "Eq(5 + 3, 8)",
                  "Eq(Rational(3,8) + Rational(5,8), 1)"]),
            fig_x1),
        prob("g4fr-x2", "A cake is cut into $4$ parts of different sizes. Is one of those parts a quarter of the cake? Explain.",
             "No. A quarter is one of $4$ EQUAL parts — four true quarters rebuild the cake, $4 \\times \\frac{1}{4} = 1$ ✓. Unequal parts carry no fraction name, however many there are.",
             ["Eq(4*Rational(1,4), 1)"]),
        prob("g4fr-x3", "Order from biggest to smallest: $\\frac{1}{2}$, $\\frac{1}{7}$, $\\frac{1}{4}$.",
             "One piece each — the coarsest cut wins: $\\frac{1}{2} > \\frac{1}{4} > \\frac{1}{7}$. The bigger bottom always loses among unit fractions.",
             ["Rational(1,2) > Rational(1,4)", "Rational(1,4) > Rational(1,7)"]),
        prob("g4fr-x4", "Which is bigger: $\\frac{5}{12}$ or $\\frac{11}{12}$ of the same bar? Say why in one sentence.",
             "Matching bottoms, so the pieces match — twelfths — and counting decides: $11 > 5$, so $\\frac{11}{12} > \\frac{5}{12}$.",
             ["Rational(11,12) > Rational(5,12)", "11 > 5"]),
        prob("g4fr-x5", "Find $\\frac{2}{5}$ of $20$ khuushuur, showing both moves.",
             "Share: $20 \\div 5 = 4$ in each group, receipt $4 \\times 5 = 20$ ✓. Take $2$ groups: $2 \\times 4 = 8$ khuushuur. So $\\frac{2}{5}$ of $20$ is $8$.",
             ["Eq(Rational(20,5), 4)", "Eq(4*5, 20)",
              "Eq(2*4, 8)", "Eq(Rational(2,5)*20, 8)"]),
        prob("g4fr-x6", "Bataa says $\\frac{1}{8} > \\frac{1}{4}$ because $8 > 4$. Explain his mistake and write the true comparison.",
             "The bottom counts how many pieces SHARE the whole: eight sharers get smaller pieces than four. So $\\frac{1}{8} < \\frac{1}{4}$ — for unit fractions the bigger bottom loses, and reading $8 > 4$ forwards is exactly the trap.",
             ["Rational(1,8) < Rational(1,4)", "8 > 4"]),
    ]


def main():
    topic = {
        "slug": "fractions-parts-of-a-whole",
        "title": "Fractions — Parts of a Whole",
        "grade": 4,
        "status": "published",
        "blurb": ("What a fraction really is — equal parts of a whole — unit "
                  "and non-unit fractions, comparing them, and taking a "
                  "fraction of a set, drawn with fraction bars throughout."),
        "lessons": [
            lesson_equal_parts(),
            lesson_unit_fractions(),
            lesson_non_unit_fractions(),
            lesson_comparing(),
            lesson_fraction_of_set(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "fractions-parts-of-a-whole.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
