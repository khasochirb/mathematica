#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Fractions — Halves, Thirds & Quarters.

What makes a part a fraction (the parts must be EQUAL); naming one part
of two, three or four; comparing unit fractions of the same whole and
discovering that a bigger bottom number means a smaller piece; taking
more than one part; and finding a half or a quarter of a set of objects.

Through-line: THE BOTTOM NUMBER SAYS HOW MANY EQUAL PARTS THE WHOLE WAS
CUT INTO. Everything follows from it — the name of one piece, why thirds
are smaller than halves, what two of them mean, and how to find a
fraction of a group.

Grade discipline: denominators of 2, 3 and 4 ONLY. No equivalence, no
adding fractions, no fractions on a number line beyond one whole, no
improper fractions — Grade 4 owns all of those, plus the wider set of
denominators. Fractions are written EXACTLY as the picture shows them
and are never silently reduced. Nothing above 1000; every check is
sympy-asserted BEFORE the JSON is written.

Run: python3 scripts/grade2/build_fractions_halves_and_quarters.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, withprobfig, workedset,
                     write_topic, fig_bar, fig_groups,
                     C_ACCENT, C_WARM, C_GREEN)


def sets_of(total, parts, color=C_ACCENT):
    """A set of `total` objects dealt into `parts` equal groups — the
    picture for "a half of" or "a quarter of" a collection."""
    assert parts in (2, 3, 4), "sets_of: Grade 3 denominators only"
    assert total % parts == 0, "sets_of: %r does not split into %r" % (total, parts)
    each = total // parts
    return fig_groups(*[(each, "group %d" % (i + 1), color)
                        for i in range(parts)])


# ==========================================================================
# Lesson 1 — Equal Parts
# ==========================================================================

def lesson_equal_parts():
    fig_half = fig_bar(1, 2, "one half shaded")
    fig_quarter = fig_bar(1, 4, "one quarter shaded")
    fig_three = fig_bar(1, 3, "one third shaded")
    return {
        "slug": "equal-parts",
        "title": "Equal Parts",
        "concreteComparison": (
            "A round bread is cut for two people. Cut it down the middle "
            "and each piece is a half. Cut it lopsidedly and one person "
            "gets more — the bread is still in two pieces, but neither is "
            "a half. Fractions begin with a promise: the parts must be "
            "EQUAL."),
        "objective": (
            "Say why the parts of a fraction must be equal, count the "
            "equal parts a whole has been cut into, and reject a picture "
            "whose parts are not equal."),
        "concept": [
            "**A fraction needs equal parts.** Cutting a bread into two "
            "pieces is not enough — the two pieces must be the same size "
            "before either can be called a half. The same goes for "
            "thirds, quarters and every fraction after them.",
            "**The bottom number counts the equal parts.** In "
            "$\\frac{1}{4}$ the $4$ says the whole was cut into four "
            "equal parts; the $1$ says you are talking about one of "
            "them. Read the bottom number first — it sets up everything "
            "else.",
            "**More parts means smaller parts.** Cut the same bread into "
            "$4$ instead of $2$ and each piece shrinks. That is obvious "
            "with bread in front of you, and it is the single most useful "
            "thing to remember when the bread is only on paper.",
        ],
        "keyIdea": (
            "A fraction describes EQUAL parts of one whole, and the "
            "bottom number says how many equal parts that whole was cut "
            "into."),
        "facts": [
            {"title": "The bottom number counts the parts",
             "latex": "\\frac{1}{4}",
             "explanation": "Four equal parts; one of them is being talked about."},
            {"title": "More parts, smaller pieces",
             "latex": "\\frac{1}{4} < \\frac{1}{2}",
             "explanation": "The same bread cut four ways gives smaller pieces than cut two ways."},
        ],
        "workedExamples": [
            {"id": "g3fr-l1-we1",
             "statement": "A bread is cut into $4$ equal parts and one part is taken. Write the fraction taken.",
             "note": "Bottom number first — how many equal parts?",
             "solution": ("The whole was cut into $4$ equal parts, so the bottom "
                          "number is $4$. One part was taken, so the top number "
                          "is $1$: the fraction is $\\frac{1}{4}$, read \"one "
                          "quarter\"."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(1, 4)*4, 1)", "Rational(1,4) < Rational(1,2)"]},
            {"id": "g3fr-l1-we2",
             "statement": "A bread is cut into two pieces, one much bigger than the other. Is either piece a half?",
             "note": "Check the promise.",
             "solution": ("No. There are two pieces, but they are not equal, and "
                          "a half means one of TWO EQUAL parts. Cut properly, "
                          "each piece would be $\\frac{1}{2}$ and the two "
                          "together would rebuild the whole: "
                          "$\\frac{1}{2} + \\frac{1}{2} = 1$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(1,2) + Rational(1,2), 1)",
                       "Eq(Rational(1,2)*2, 1)"]},
        ],
        "commonMistakes": [
            {"text": "Calling any two pieces \"halves\" just because there are two of them.",
             "correction": "A half is one of two EQUAL parts. Two unequal pieces are simply two pieces — neither one is a half of anything.",
             "authored": True},
            {"text": "Reading the bottom number as how many parts you TOOK.",
             "correction": "The bottom number counts the equal parts the whole was cut into; the top number counts how many you took. In 1/4 the whole was cut four ways and one piece was taken.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3fr-l1-t1",
             "statement": "A bar is cut into $3$ equal pieces. What fraction is one piece?",
             "solution": ("Three equal parts, so the bottom number is $3$; one "
                          "piece is $\\frac{1}{3}$, read \"one third\"."),
             "check": ["Eq(Rational(1,3)*3, 1)"]},
            {"id": "g3fr-l1-t2",
             "statement": "Which is bigger — one of $2$ equal parts of a bread, or one of $4$?",
             "solution": ("One of two: $\\frac{1}{2}$ is bigger than "
                          "$\\frac{1}{4}$. Cutting the same bread into more "
                          "pieces makes each piece smaller."),
             "check": ["Rational(1,2) > Rational(1,4)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The parts must be equal", [
                "The bar below is cut into $2$ equal parts with one of them shaded. That shaded piece is a half — written $\\frac{1}{2}$.",
                "The word \"equal\" is doing real work. Cut a bread into two pieces of different sizes and you have two pieces, but you do not have halves. A half is one of two EQUAL parts.",
                "Together the two halves rebuild the whole: $\\frac{1}{2} + \\frac{1}{2} = 1$. Every fraction works this way — all the equal parts put back together make one whole.",
            ]), fig_half),
            workedset("Name the equal parts",
                      "Count the equal parts, then count the shaded ones.", [
                wex("A bar is cut into $2$ equal parts. What is one part called?",
                    ["Two equal parts, so the bottom number is $2$.",
                     "One of them is $\\frac{1}{2}$ — a half.",
                     "Both together make the whole: $\\frac{1}{2} + \\frac{1}{2} = 1$."],
                    "$\\frac{1}{2}$",
                    ["Eq(Rational(1,2) + Rational(1,2), 1)"]),
                wex("A bar is cut into $4$ equal parts. What is one part called?",
                    ["Four equal parts, so the bottom number is $4$.",
                     "One of them is $\\frac{1}{4}$ — a quarter.",
                     "All four rebuild the whole: $\\frac{1}{4} \\times 4 = 1$."],
                    "$\\frac{1}{4}$",
                    ["Eq(Rational(1,4)*4, 1)"]),
            ]),
            tryitset("Equal or not?", "The parts have to be the same size.", [
                withfig(tp("The bar below is cut into $4$ equal parts with one shaded. The shaded part is:",
                   ["$\\frac{1}{4}$", "$\\frac{1}{3}$", "$\\frac{4}{1}$"],
                   "Four equal parts, one shaded: $\\frac{1}{4}$. The bottom number counts the parts the whole was cut into, so it cannot be $3$ here.",
                   ["Eq(Rational(1,4)*4, 1)",
                    "Rational(1,4) < Rational(1,3)"]), fig_quarter),
                tp("A bread is cut into two pieces, one bigger than the other. The smaller piece is:",
                   ["not a half — the parts are unequal",
                    "a half, because there are two pieces",
                    "a quarter"],
                   "A half is one of two EQUAL parts, and these are not equal. Cut properly, each piece would be $\\frac{1}{2}$.",
                   ["Eq(Rational(1,2)*2, 1)"]),
                tp("In $\\frac{1}{3}$, the $3$ tells you:",
                   ["the whole was cut into $3$ equal parts",
                    "you took $3$ parts",
                    "there are $3$ wholes"],
                   "The bottom number counts the equal parts the whole was cut into. The top number, $1$, is how many of them are being talked about.",
                   ["Eq(Rational(1,3)*3, 1)"]),
            ]),
            withfig(tapq("Reading the bottom number", "A bar is cut into $3$ equal parts and one is shaded. The shaded part is:",
                 ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{1}$",
                  "$\\frac{2}{3}$"],
                 "Three equal parts with one shaded gives $\\frac{1}{3}$. Three of them rebuild the whole: $\\frac{1}{3} \\times 3 = 1$.",
                 ["Eq(Rational(1,3)*3, 1)",
                  "Rational(1,3) < Rational(1,2)"]), fig_three),
            funfact("Why halves came before numbers",
                    "Long before anyone wrote a fraction down, people were halving things — a carcass, a field, a day. Halving needs no arithmetic at all, only a fair eye, which is why every language on earth has a word for \"half\" and almost none had a word for \"three-sevenths\". Fractions are the moment sharing became writing."),
            withfig(teach("Concept B", "More parts, smaller pieces", [
                "Compare the two bars you have seen. The first was cut into $2$ equal parts; the second, below, into $4$ — from the same whole.",
                "Each quarter is visibly smaller than each half. Cutting the same bread into more pieces cannot make the pieces bigger, and $\\frac{1}{4} < \\frac{1}{2}$.",
                "This runs against a habit: with whole numbers, $4$ is bigger than $2$. With fractions the bigger bottom number means the SMALLER piece, because the whole is being shared more ways.",
            ]), fig_quarter),
            workedset("Which piece is bigger?",
                      "More parts from the same whole means smaller parts.", [
                wex("Which is bigger, $\\frac{1}{2}$ or $\\frac{1}{4}$ of the same bread?",
                    ["Two parts against four parts, from one bread.",
                     "Four pieces are smaller than two, so $\\frac{1}{2} > \\frac{1}{4}$."],
                    "$\\frac{1}{2}$",
                    ["Rational(1,2) > Rational(1,4)"]),
                wex("Which is bigger, $\\frac{1}{3}$ or $\\frac{1}{4}$ of the same bar?",
                    ["Three parts against four parts.",
                     "Fewer parts means bigger pieces, so $\\frac{1}{3} > \\frac{1}{4}$."],
                    "$\\frac{1}{3}$",
                    ["Rational(1,3) > Rational(1,4)"]),
            ]),
            tryitset("Bigger or smaller?", "Bigger bottom number, smaller piece.", [
                tp("Which is the biggest piece of the same bread?",
                   ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{4}$"],
                   "The fewest parts gives the biggest piece: $\\frac{1}{2} > \\frac{1}{3} > \\frac{1}{4}$. Cutting more ways only makes pieces smaller.",
                   ["Rational(1,2) > Rational(1,3)",
                    "Rational(1,3) > Rational(1,4)"]),
                tp("Two children share one bread; four children share another bread of the same size. Who gets more?",
                   ["a child from the group of two",
                    "a child from the group of four",
                    "they get the same"],
                   "The pair each get $\\frac{1}{2}$; the four each get $\\frac{1}{4}$. Same bread, more sharers, smaller share.",
                   ["Rational(1,2) > Rational(1,4)",
                    "Eq(Rational(1,2)*2, 1)"]),
                tp("A bread cut into $3$ equal parts gives pieces that are:",
                   ["smaller than halves but bigger than quarters",
                    "bigger than halves",
                    "the same as quarters"],
                   "Three parts sit between two and four, so $\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$.",
                   ["Rational(1,3) < Rational(1,2)",
                    "Rational(1,3) > Rational(1,4)"]),
            ]),
            tapq("The upside-down rule", "Why is $\\frac{1}{4}$ smaller than $\\frac{1}{2}$, even though $4 > 2$?",
                 ["the same whole is being shared more ways",
                  "because $4$ is an even number",
                  "it is not — $\\frac{1}{4}$ is bigger",
                  "because quarters are always tiny"],
                 "The bottom number counts how many ways the whole is cut, and cutting more ways makes every piece smaller: $\\frac{1}{4} < \\frac{1}{2}$. It is the one place where a bigger number means less.",
                 ["Rational(1,4) < Rational(1,2)", "4 > 2",
                  "Eq(Rational(1,4)*4, 1)"]),
            recap([
                "A fraction describes EQUAL parts of one whole — unequal pieces are not fractions.",
                "The bottom number counts the equal parts the whole was cut into.",
                "All the parts put back together make one whole: $\\frac{1}{4} \\times 4 = 1$.",
                "More parts means smaller parts: $\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$.",
            ]),
            tip("Whenever you see a fraction, picture the bread being cut. The bottom number is how many cuts-worth of pieces there are, and one glance tells you whether the piece is big or small."),
            tryitset("Chapter practice", "Count the equal parts first.", [
                tp("A bar in $2$ equal parts with $1$ shaded shows:",
                   ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{2}{1}$"],
                   "Two equal parts, one shaded: a half. The two halves rebuild the whole.",
                   ["Eq(Rational(1,2)*2, 1)"]),
                tp("Which statement is TRUE?",
                   ["$\\frac{1}{3}$ is smaller than $\\frac{1}{2}$",
                    "$\\frac{1}{3}$ is bigger than $\\frac{1}{2}$",
                    "$\\frac{1}{3}$ equals $\\frac{1}{2}$"],
                   "Cutting into three gives smaller pieces than cutting into two, so $\\frac{1}{3} < \\frac{1}{2}$.",
                   ["Rational(1,3) < Rational(1,2)"]),
                tp("A cake in $4$ unequal pieces. One piece is:",
                   ["not a quarter", "a quarter", "a half"],
                   "A quarter is one of four EQUAL parts. Four unequal pieces are just four pieces — the promise of equality is what makes a fraction.",
                   ["Eq(Rational(1,4)*4, 1)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Equal Parts\"",
                    "You now know what the bottom number is for, and the rule that surprises everyone — bigger bottom, smaller piece. The next lesson gives the pieces their names and starts taking more than one at a time.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Halves and Quarters
# ==========================================================================

def lesson_halves_quarters():
    fig_h = fig_bar(1, 2, "a half")
    fig_q = fig_bar(1, 4, "a quarter")
    fig_2q = fig_bar(2, 4, "two quarters")
    return {
        "slug": "halves-and-quarters",
        "title": "Halves and Quarters",
        "concreteComparison": (
            "Halves and quarters are the two fractions everyone meets "
            "first, because they come from folding: fold a sheet once for "
            "halves, fold it again for quarters. Two quarters cover "
            "exactly the same space as one half — you can see it on the "
            "folded paper."),
        "objective": (
            "Name and write halves and quarters, count how many of each "
            "make a whole, and see that two quarters cover the same "
            "amount as one half."),
        "concept": [
            "**A half is one of two equal parts; a quarter is one of "
            "four.** Written $\\frac{1}{2}$ and $\\frac{1}{4}$. Fold a "
            "sheet once and you have halves; fold it again and you have "
            "quarters, four of them.",
            "**Count how many make a whole.** Two halves make one whole: "
            "$\\frac{1}{2} + \\frac{1}{2} = 1$. Four quarters make one "
            "whole: $\\frac{1}{4} \\times 4 = 1$. The bottom number "
            "always tells you how many it takes.",
            "**Two quarters cover the same space as a half.** Fold the "
            "sheet and lay one half over two quarters — they match "
            "exactly. So $\\frac{2}{4}$ and $\\frac{1}{2}$ describe the "
            "same amount of bread, even though they count it in "
            "differently-sized pieces.",
        ],
        "keyIdea": (
            "Two halves or four quarters make one whole, and two quarters "
            "cover exactly as much as one half."),
        "facts": [
            {"title": "Four quarters make a whole",
             "latex": "\\frac{1}{4} \\times 4 = 1",
             "explanation": "Fold twice and the four pieces rebuild the sheet."},
            {"title": "Two quarters cover a half",
             "latex": "\\frac{2}{4} = \\frac{1}{2}",
             "explanation": "Different-sized pieces, the same amount of bread."},
        ],
        "workedExamples": [
            {"id": "g3fr-l2-we1",
             "statement": "How many quarters make one whole? Show it with the folding.",
             "note": "Fold once for halves, again for quarters.",
             "solution": ("Folding once gives $2$ halves; folding again cuts "
                          "each half in two, giving $4$ quarters. So four "
                          "quarters rebuild the whole sheet: "
                          "$\\frac{1}{4} \\times 4 = 1$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(1,4)*4, 1)", "Eq(Rational(1,2)*2, 1)"]},
            {"id": "g3fr-l2-we2",
             "statement": "A bar of $4$ equal pieces has $2$ shaded. Name the shaded part two ways.",
             "note": "Count the pieces, then compare with a half.",
             "solution": ("Two of the four pieces are shaded, so the shaded part "
                          "is $\\frac{2}{4}$. Laid against a bar folded once, "
                          "those two quarters cover exactly one half — so the "
                          "same amount is also $\\frac{1}{2}$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(2,4), Rational(1,2))",
                       "Eq(Rational(2,4)*2, 1)"]},
        ],
        "commonMistakes": [
            {"text": "Thinking two quarters must be smaller than a half because \"quarters are the small ones\".",
             "correction": "One quarter is smaller than a half, but TWO of them together cover exactly a half: 2/4 = 1/2. How many pieces you take matters as much as how big they are.",
             "authored": True},
            {"text": "Saying a whole is made of two quarters, by copying the halves rule.",
             "correction": "The bottom number tells you how many it takes: two halves, but FOUR quarters. Two quarters only reach a half.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3fr-l2-t1",
             "statement": "How many halves make one whole, and how many quarters?",
             "solution": ("Two halves: $\\frac{1}{2} \\times 2 = 1$. Four "
                          "quarters: $\\frac{1}{4} \\times 4 = 1$. The bottom "
                          "number is always the count needed."),
             "check": ["Eq(Rational(1,2)*2, 1)", "Eq(Rational(1,4)*4, 1)"]},
            {"id": "g3fr-l2-t2",
             "statement": "A bar of $4$ equal pieces has $3$ shaded. Write the shaded fraction, and say how much is plain.",
             "solution": ("Shaded: $\\frac{3}{4}$. One piece of the four is "
                          "plain, so plain is $\\frac{1}{4}$ — and together they "
                          "rebuild the whole: "
                          "$\\frac{3}{4} + \\frac{1}{4} = 1$."),
             "check": ["Eq(Rational(3,4) + Rational(1,4), 1)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Fold once, fold again", [
                "Fold a sheet of paper down the middle and open it: two equal parts. Each one is a half, $\\frac{1}{2}$ — the bar below shows one shaded.",
                "Fold it again the other way and each half is cut in two: now there are four equal parts, and each is a quarter, $\\frac{1}{4}$.",
                "So the count needed for a whole is the bottom number: two halves, four quarters. $\\frac{1}{2} \\times 2 = 1$ and $\\frac{1}{4} \\times 4 = 1$.",
            ]), fig_h),
            workedset("How many make a whole?",
                      "The bottom number is the count you need.", [
                wex("How many halves make one whole?",
                    ["A half is one of TWO equal parts.",
                     "So two of them rebuild it: $\\frac{1}{2} \\times 2 = 1$."],
                    "$2$",
                    ["Eq(Rational(1,2)*2, 1)"]),
                wex("How many quarters make one whole?",
                    ["A quarter is one of FOUR equal parts.",
                     "So four of them rebuild it: $\\frac{1}{4} \\times 4 = 1$."],
                    "$4$",
                    ["Eq(Rational(1,4)*4, 1)"]),
            ]),
            tryitset("Counting to a whole", "Look at the bottom number.", [
                withfig(tp("The bar shows one quarter shaded. How many more quarters would fill it?",
                   ["$3$", "$1$", "$4$"],
                   "Four quarters make a whole and one is already shaded, so three more are needed: $\\frac{1}{4} + \\frac{3}{4} = 1$.",
                   ["Eq(Rational(1,4) + Rational(3,4), 1)",
                    "Eq(Rational(1,4)*4, 1)"]), fig_q),
                tp("How many halves are there in one whole?",
                   ["$2$", "$4$", "$1$"],
                   "A half is one of two equal parts, so two of them rebuild the whole. Answering $4$ copies the quarters rule by mistake.",
                   ["Eq(Rational(1,2)*2, 1)", "Eq(Rational(1,4)*4, 1)"]),
                tp("A bar of $4$ equal pieces has $3$ shaded. The plain part is:",
                   ["$\\frac{1}{4}$", "$\\frac{3}{4}$", "$\\frac{1}{3}$"],
                   "Three of four are shaded, so one of four is plain: $\\frac{1}{4}$. Together they rebuild the bar.",
                   ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
            ]),
            tapq("Filling the whole", "Two quarters of a bread have been eaten. How much is left?",
                 ["$\\frac{2}{4}$", "$\\frac{1}{4}$", "$\\frac{3}{4}$",
                  "none of it"],
                 "Four quarters make the whole and two are gone, so two remain: $\\frac{2}{4}$ — which is the same as a half. Check: $\\frac{2}{4} + \\frac{2}{4} = 1$.",
                 ["Eq(Rational(2,4) + Rational(2,4), 1)",
                  "Eq(Rational(2,4), Rational(1,2))"]),
            funfact("A quarter of an hour",
                    "Clocks are the place most people meet quarters every day: a quarter of an hour is $15$ minutes, because $60$ minutes shared four ways gives $15$ each — and $4 \\times 15 = 60$ ✓. Half an hour is $30$ minutes for the same reason. The fractions on a clock face are doing exactly what the fractions on a bread do."),
            withfig(teach("Concept B", "Two quarters cover a half", [
                "Take the folded sheet again. Lay one half over two quarters — the bar below shows two of four pieces shaded — and they match exactly, edge for edge.",
                "So $\\frac{2}{4}$ and $\\frac{1}{2}$ describe the same amount of bread. The pieces are different sizes and there are different numbers of them, but the bread covered is identical.",
                "That is worth holding on to: how MUCH you have depends on both numbers, not just the bottom one. One quarter is less than a half, but two quarters are exactly a half.",
            ]), fig_2q),
            workedset("The same amount, counted differently",
                      "Compare what is covered, not how many pieces.", [
                wex("A bar of $4$ equal pieces has $2$ shaded. Name it two ways.",
                    ["Two of four pieces: $\\frac{2}{4}$.",
                     "Laid against a half, they cover exactly the same: $\\frac{2}{4} = \\frac{1}{2}$."],
                    "$\\frac{2}{4}$, which is $\\frac{1}{2}$",
                    ["Eq(Rational(2,4), Rational(1,2))"]),
                wex("Which is more: $\\frac{1}{4}$ of a bread, or $\\frac{1}{2}$?",
                    ["One quarter is one of four; a half is one of two.",
                     "Fewer parts means bigger pieces: $\\frac{1}{2} > \\frac{1}{4}$.",
                     "But TWO quarters would tie with the half."],
                    "$\\frac{1}{2}$",
                    ["Rational(1,2) > Rational(1,4)",
                     "Eq(Rational(2,4), Rational(1,2))"]),
            ]),
            tryitset("How much is covered?", "Both numbers matter, not just the bottom.", [
                tp("$\\frac{2}{4}$ of a bread is the same as:",
                   ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "the whole bread"],
                   "Two of the four pieces cover exactly one of the two halves — lay them side by side and they match.",
                   ["Eq(Rational(2,4), Rational(1,2))"]),
                tp("Bat eats $\\frac{1}{4}$ of a bread and Saruul eats $\\frac{1}{2}$ of an identical one. Who ate more?",
                   ["Saruul", "Bat", "they ate the same"],
                   "A half is one of two parts and a quarter one of four, so Saruul's piece is bigger: $\\frac{1}{2} > \\frac{1}{4}$. Bat would need two quarters to match her.",
                   ["Rational(1,2) > Rational(1,4)",
                    "Eq(Rational(2,4), Rational(1,2))"]),
                tp("Which is NOT the same as one half of a bar?",
                   ["$\\frac{1}{4}$ of the bar", "$\\frac{2}{4}$ of the bar",
                    "one of two equal pieces"],
                   "One quarter is only half as much as a half. Both other descriptions cover the same amount.",
                   ["Rational(1,4) < Rational(1,2)",
                    "Eq(Rational(2,4), Rational(1,2))"]),
            ]),
            tapq("Piece size against piece count", "Bat has $2$ quarters of a bread. Saruul has $1$ half of an identical bread. Who has more?",
                 ["they have the same amount",
                  "Bat, because he has two pieces",
                  "Saruul, because halves are bigger",
                  "you cannot compare them"],
                 "Bat's pieces are smaller but he has two of them, and the two effects cancel exactly: $\\frac{2}{4} = \\frac{1}{2}$. Piece size alone does not decide who has more.",
                 ["Eq(Rational(2,4), Rational(1,2))",
                  "Rational(1,4) < Rational(1,2)"]),
            recap([
                "A half is one of two equal parts; a quarter is one of four.",
                "The bottom number is how many it takes to rebuild the whole: two halves, four quarters.",
                "Two quarters cover exactly the same amount as one half.",
                "How much you have depends on BOTH numbers — the size of a piece and how many you took.",
            ]),
            tip("Fold a real sheet of paper once, then again, and keep it beside you. Every question about halves and quarters this year can be answered by laying the folds against each other."),
            tryitset("Chapter practice", "Count the pieces, then compare what they cover.", [
                tp("Three quarters of a bread, plus one more quarter, makes:",
                   ["one whole bread", "half a bread", "two breads"],
                   "Four quarters rebuild the whole: $\\frac{3}{4} + \\frac{1}{4} = 1$.",
                   ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
                tp("A bar of $4$ pieces with $2$ shaded shows the same amount as:",
                   ["a bar of $2$ pieces with $1$ shaded",
                    "a bar of $4$ pieces with $1$ shaded",
                    "a whole bar"],
                   "$\\frac{2}{4}$ and $\\frac{1}{2}$ cover the same space — different pieces, same amount of bread.",
                   ["Eq(Rational(2,4), Rational(1,2))"]),
                tp("How many quarters are in half a bread?",
                   ["$2$", "$4$", "$1$"],
                   "Two quarters cover a half, so half a bread holds two of them — and four quarters would be the whole bread.",
                   ["Eq(Rational(2,4), Rational(1,2))",
                    "Eq(Rational(1,4)*4, 1)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Halves and Quarters\"",
                    "Halves and quarters get on well because one folds neatly into the other. Thirds do not fold from either — which is exactly what makes the next lesson interesting.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Thirds, and Comparing
# ==========================================================================

def lesson_thirds():
    fig_third = fig_bar(1, 3, "one third")
    fig_two_thirds = fig_bar(2, 3, "two thirds")
    fig_cmp = fig_bar(1, 2, "a half — bigger than a third")
    return {
        "slug": "thirds-and-comparing",
        "title": "Thirds & Comparing",
        "concreteComparison": (
            "Three children share one bread. No amount of folding will do "
            "it — a third cannot be reached by halving. It has to be cut "
            "into three equal parts from the start, and each child gets "
            "$\\frac{1}{3}$."),
        "objective": (
            "Name and write thirds, count how many make a whole, and put "
            "halves, thirds and quarters of the same whole in order."),
        "concept": [
            "**A third is one of three equal parts.** Written "
            "$\\frac{1}{3}$, and three of them rebuild the whole: "
            "$\\frac{1}{3} \\times 3 = 1$. Unlike quarters, thirds cannot "
            "be folded from halves — three is an awkward number for "
            "paper.",
            "**Compare unit fractions by their bottom numbers.** For "
            "$\\frac{1}{2}$, $\\frac{1}{3}$ and $\\frac{1}{4}$ of the "
            "same whole, the bigger the bottom number the smaller the "
            "piece: $\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$.",
            "**It only works on the SAME whole.** A third of a big bread "
            "can easily beat a half of a small one. Comparing fractions "
            "means comparing parts of wholes that are the same size — "
            "otherwise the fractions are describing different things.",
        ],
        "keyIdea": (
            "Three thirds make a whole, and among unit fractions of the "
            "same whole, a bigger bottom number always means a smaller "
            "piece."),
        "facts": [
            {"title": "Three thirds make a whole",
             "latex": "\\frac{1}{3} \\times 3 = 1",
             "explanation": "Three equal parts put back together rebuild the bread."},
            {"title": "Ordering unit fractions",
             "latex": "\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}",
             "explanation": "Of one whole: more parts always means smaller pieces."},
        ],
        "workedExamples": [
            {"id": "g3fr-l3-we1",
             "statement": "Three children share one bread equally. What fraction does each get, and how do you check?",
             "note": "How many equal parts?",
             "solution": ("Three equal parts, so each child gets "
                          "$\\frac{1}{3}$. The check is that all three put "
                          "together rebuild the bread: "
                          "$\\frac{1}{3} \\times 3 = 1$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(1,3)*3, 1)"]},
            {"id": "g3fr-l3-we2",
             "statement": "Put $\\frac{1}{2}$, $\\frac{1}{3}$ and $\\frac{1}{4}$ of the same bread in order, smallest first.",
             "note": "More parts, smaller pieces.",
             "solution": ("Cutting into four gives the smallest pieces, then "
                          "three, then two: $\\frac{1}{4} < \\frac{1}{3} < "
                          "\\frac{1}{2}$. The order of the bottom numbers is "
                          "exactly reversed."),
             "badges": [{"text": "core"}],
             "check": ["Rational(1,4) < Rational(1,3)",
                       "Rational(1,3) < Rational(1,2)"]},
        ],
        "commonMistakes": [
            {"text": "Ordering fractions by their bottom numbers as if they were whole numbers: 1/2 < 1/3 < 1/4.",
             "correction": "The order flips. A bigger bottom number cuts the whole more ways, so the piece is smaller: 1/4 < 1/3 < 1/2.",
             "authored": True},
            {"text": "Comparing fractions of different-sized wholes — claiming 1/3 of a small bread beats 1/2 of a big one.",
             "correction": "Fractions can only be compared when the wholes are the same size. Of one bread, 1/2 always beats 1/3; of two different breads, the fractions are not describing the same thing.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3fr-l3-t1",
             "statement": "A bar of $3$ equal pieces has $2$ shaded. Write the shaded and the plain fractions.",
             "solution": ("Shaded $\\frac{2}{3}$, plain $\\frac{1}{3}$ — and "
                          "together they rebuild the bar: "
                          "$\\frac{2}{3} + \\frac{1}{3} = 1$."),
             "check": ["Eq(Rational(2,3) + Rational(1,3), 1)"]},
            {"id": "g3fr-l3-t2",
             "statement": "Which is bigger, $\\frac{1}{3}$ or $\\frac{1}{4}$ of the same bread? Explain in one sentence.",
             "solution": ("$\\frac{1}{3}$ — cutting into three gives bigger "
                          "pieces than cutting the same bread into four."),
             "check": ["Rational(1,3) > Rational(1,4)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Cutting into three", [
                "Three children, one bread. Folding will not help — a third cannot be reached by halving, because three is not two doubled.",
                "The bread must be cut into three equal parts from the start. Each child gets one of them: $\\frac{1}{3}$, shown shaded below.",
                "The check is the same as always: all three parts put back together rebuild the bread, $\\frac{1}{3} \\times 3 = 1$.",
            ]), fig_third),
            workedset("Name the thirds", "Three equal parts, one of them named.", [
                wex("Three children share one bread. What does each get?",
                    ["Three equal parts.",
                     "Each gets $\\frac{1}{3}$; the three rebuild the bread ✓."],
                    "$\\frac{1}{3}$",
                    ["Eq(Rational(1,3)*3, 1)"]),
                wex("A bar of $3$ equal pieces has $2$ shaded. Name the shaded part.",
                    ["Two of the three pieces are shaded.",
                     "That is $\\frac{2}{3}$, and the plain part is $\\frac{1}{3}$.",
                     "Together: $\\frac{2}{3} + \\frac{1}{3} = 1$ ✓."],
                    "$\\frac{2}{3}$",
                    ["Eq(Rational(2,3) + Rational(1,3), 1)"]),
            ]),
            tryitset("Thirds", "Three equal parts make the whole.", [
                withfig(tp("The bar shows $2$ of $3$ equal parts shaded. The shaded fraction is:",
                   ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "$\\frac{3}{2}$"],
                   "Two shaded out of three parts: $\\frac{2}{3}$. The plain third completes the bar.",
                   ["Eq(Rational(2,3) + Rational(1,3), 1)"]), fig_two_thirds),
                tp("How many thirds make one whole?",
                   ["$3$", "$2$", "$4$"],
                   "A third is one of three equal parts, so three of them rebuild the whole: $\\frac{1}{3} \\times 3 = 1$.",
                   ["Eq(Rational(1,3)*3, 1)"]),
                tp("One third of a bread has been eaten. How much is left?",
                   ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "$\\frac{1}{2}$"],
                   "Three thirds make the whole and one is gone, so two remain: $\\frac{1}{3} + \\frac{2}{3} = 1$ ✓.",
                   ["Eq(Rational(1,3) + Rational(2,3), 1)"]),
            ]),
            tapq("Thirds do not fold", "Why can a third not be made by folding a sheet in half repeatedly?",
                 ["folding halves gives $2$, $4$, $8$ parts — never $3$",
                  "because thirds are too small to fold",
                  "it can — fold it once and a half",
                  "because paper only folds in two"],
                 "Each fold doubles the number of parts, so folding gives $2$, then $4$, then $8$ — three never appears in that list. A third has to be cut deliberately into three equal parts, and $\\frac{1}{3} \\times 3 = 1$ is the check.",
                 ["Eq(Rational(1,3)*3, 1)", "Eq(2*2, 4)", "Ne(4, 3)"]),
            funfact("The fraction that broke the ruler",
                    "Rulers are marked in halves, quarters and eighths because those come from folding — every mark is the middle of the one before. Thirds never appear, which is why carpenters measuring a third of a plank do something clever instead: they lay the ruler at a slant across the plank until a number divisible by three fits, and mark from there."),
            withfig(teach("Concept B", "Putting the pieces in order", [
                "Now line up three cuts of the SAME bread: into two, into three, into four. The bar below shows the half — the largest of the three pieces.",
                "The more parts you cut, the smaller each piece: $\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$. Notice the bottom numbers run the other way, $4$, $3$, $2$.",
                "One warning. This only works on the same whole. A third of a large bread can easily beat a half of a small one — comparing fractions means comparing parts of equal wholes.",
            ]), fig_cmp),
            workedset("Order the pieces",
                      "Reverse the bottom numbers to get the sizes.", [
                wex("Order $\\frac{1}{2}$, $\\frac{1}{3}$, $\\frac{1}{4}$ of one bread, smallest first.",
                    ["Most parts gives smallest pieces: four, then three, then two.",
                     "$\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$."],
                    "$\\frac{1}{4}$, $\\frac{1}{3}$, $\\frac{1}{2}$",
                    ["Rational(1,4) < Rational(1,3)",
                     "Rational(1,3) < Rational(1,2)"]),
                wex("Which is bigger, $\\frac{1}{3}$ or $\\frac{1}{2}$ of the same bar?",
                    ["Three parts against two parts.",
                     "Fewer parts means bigger pieces, so $\\frac{1}{2} > \\frac{1}{3}$."],
                    "$\\frac{1}{2}$",
                    ["Rational(1,2) > Rational(1,3)"]),
            ]),
            tryitset("Which is bigger?", "Bigger bottom number, smaller piece.", [
                tp("Of the same bread, the biggest piece is:",
                   ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{4}$"],
                   "Cutting into the fewest parts gives the biggest piece: $\\frac{1}{2} > \\frac{1}{3} > \\frac{1}{4}$.",
                   ["Rational(1,2) > Rational(1,3)",
                    "Rational(1,3) > Rational(1,4)"]),
                tp("Smallest first, the correct order is:",
                   ["$\\frac{1}{4}$, $\\frac{1}{3}$, $\\frac{1}{2}$",
                    "$\\frac{1}{2}$, $\\frac{1}{3}$, $\\frac{1}{4}$",
                    "$\\frac{1}{3}$, $\\frac{1}{4}$, $\\frac{1}{2}$"],
                   "The bottom numbers run $4, 3, 2$ while the pieces grow — the order of sizes is the reverse of the order of bottom numbers.",
                   ["Rational(1,4) < Rational(1,3)",
                    "Rational(1,3) < Rational(1,2)"]),
                tp("Saruul says $\\frac{1}{3}$ of her small bread beats $\\frac{1}{2}$ of Bat's large one. Is she right?",
                   ["possibly — the breads are different sizes",
                    "no — a half always beats a third",
                    "no — thirds are always tiny"],
                   "Fractions can only be ordered when the wholes match. Of ONE bread $\\frac{1}{2} > \\frac{1}{3}$ always, but across two different breads the pieces are not comparable by their fractions alone.",
                   ["Rational(1,2) > Rational(1,3)"]),
            ]),
            tapq("The reversal", "Among $\\frac{1}{2}$, $\\frac{1}{3}$ and $\\frac{1}{4}$ of one bread, which has the SMALLEST piece?",
                 ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{1}{3}$",
                  "they are all the same"],
                 "The biggest bottom number cuts the bread the most ways, so its pieces are smallest: $\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$. With whole numbers $4$ is the biggest — here it marks the smallest piece.",
                 ["Rational(1,4) < Rational(1,3)",
                  "Rational(1,3) < Rational(1,2)"]),
            recap([
                "A third is one of three equal parts, and three of them rebuild the whole.",
                "Thirds cannot be folded from halves — folding only ever gives $2$, $4$, $8$ parts.",
                "Of the same whole: $\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$ — bigger bottom, smaller piece.",
                "Fractions can only be compared when the wholes are the same size.",
            ]),
            tip("When ordering unit fractions, write the bottom numbers down and then read them BACKWARDS. The reversal is the whole trick, and writing it out stops the whole-number habit taking over."),
            tryitset("Chapter practice", "Reverse the bottom numbers.", [
                tp("$\\frac{2}{3}$ of a bar is shaded. The plain part is:",
                   ["$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{1}{2}$"],
                   "Three parts, two shaded, so one is plain: $\\frac{1}{3}$, and the two fractions rebuild the bar.",
                   ["Eq(Rational(2,3) + Rational(1,3), 1)"]),
                tp("Which is TRUE of the same bread?",
                   ["$\\frac{1}{3} > \\frac{1}{4}$",
                    "$\\frac{1}{3} < \\frac{1}{4}$",
                    "$\\frac{1}{3} = \\frac{1}{4}$"],
                   "Three parts are bigger than four parts of the same bread, so $\\frac{1}{3} > \\frac{1}{4}$.",
                   ["Rational(1,3) > Rational(1,4)"]),
                tp("Three children share one bread equally. Each gets:",
                   ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$3$ breads"],
                   "Three equal parts of one bread: each child gets a third, and $\\frac{1}{3} \\times 3 = 1$ rebuilds it.",
                   ["Eq(Rational(1,3)*3, 1)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Thirds & Comparing\"",
                    "You can now name and order every fraction this year uses. The last two lessons stop asking about single pieces — first taking several at once, then finding a fraction of a whole group of objects.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — More Than One Part
# ==========================================================================

def lesson_more_than_one():
    fig_34 = fig_bar(3, 4, "three quarters")
    fig_23 = fig_bar(2, 3, "two thirds")
    fig_44 = fig_bar(4, 4, "four quarters — the whole")
    return {
        "slug": "more-than-one-part",
        "title": "More Than One Part",
        "concreteComparison": (
            "A bread cut into four and three pieces taken is not a "
            "quarter — it is three quarters, $\\frac{3}{4}$. The bottom "
            "number still says how the bread was cut. The top number is "
            "new: it counts how many of those pieces you have."),
        "objective": (
            "Read and write fractions with more than one part, say what "
            "each number counts, and find the part that is left over."),
        "concept": [
            "**The top number counts the pieces you have.** In "
            "$\\frac{3}{4}$ the bottom $4$ says the bread was cut into "
            "four equal parts, and the top $3$ says you have three of "
            "them. Bottom: how it was cut. Top: how many you took.",
            "**The shaded and the plain always rebuild the whole.** If "
            "$\\frac{3}{4}$ is shaded, the plain part must be "
            "$\\frac{1}{4}$, because $\\frac{3}{4} + \\frac{1}{4} = 1$. "
            "Finding the leftover is just counting the pieces you did not "
            "take.",
            "**When the top and bottom match, you have the whole thing.** "
            "$\\frac{4}{4} = 1$: all four pieces of a bread cut in four "
            "IS the bread. Likewise $\\frac{3}{3} = 1$ and "
            "$\\frac{2}{2} = 1$.",
        ],
        "keyIdea": (
            "The bottom number says how the whole was cut; the top number "
            "says how many pieces you have — and when they match, you "
            "have one whole."),
        "facts": [
            {"title": "Top counts what you took",
             "latex": "\\frac{3}{4}",
             "explanation": "Cut into four; three of those pieces are yours."},
            {"title": "Top equals bottom means one whole",
             "latex": "\\frac{4}{4} = 1",
             "explanation": "All four quarters together are the whole bread."},
        ],
        "workedExamples": [
            {"id": "g3fr-l4-we1",
             "statement": "A bar of $4$ equal pieces has $3$ shaded. Write the shaded fraction and the plain one.",
             "note": "Bottom from the cutting, top from the counting.",
             "solution": ("The bar was cut into $4$, so the bottom number is $4$. "
                          "Three pieces are shaded, so shaded is $\\frac{3}{4}$ "
                          "and the one remaining piece is $\\frac{1}{4}$. "
                          "Together: $\\frac{3}{4} + \\frac{1}{4} = 1$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(3,4) + Rational(1,4), 1)"]},
            {"id": "g3fr-l4-we2",
             "statement": "What is $\\frac{4}{4}$ of a bread?",
             "note": "Count the pieces against the cuts.",
             "solution": ("The bread was cut into four and all four pieces are "
                          "taken — that is the whole bread: $\\frac{4}{4} = 1$. "
                          "Whenever the top and bottom numbers match, the "
                          "fraction is one whole."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(4,4), 1)", "Eq(Rational(3,3), 1)"]},
        ],
        "commonMistakes": [
            {"text": "Reading 3/4 as \"three breads cut into four\".",
             "correction": "It is one bread cut into four, with three of the pieces taken. The bottom number never counts breads — it counts the equal parts one whole was cut into.",
             "authored": True},
            {"text": "Thinking 4/4 must be bigger than one whole because 4 + 4 sounds like a lot.",
             "correction": "Four quarters ARE the bread: 4/4 = 1. The top number cannot exceed the bottom this year, because you cannot take more pieces than the bread was cut into.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3fr-l4-t1",
             "statement": "A bar of $3$ equal pieces has $2$ shaded. What fraction is plain?",
             "solution": ("Three pieces, two shaded, so one is plain: "
                          "$\\frac{1}{3}$. Check: "
                          "$\\frac{2}{3} + \\frac{1}{3} = 1$ ✓."),
             "check": ["Eq(Rational(2,3) + Rational(1,3), 1)"]},
            {"id": "g3fr-l4-t2",
             "statement": "Bat eats $\\frac{2}{4}$ of a bread. How much is left, and what simpler name does that leftover have?",
             "solution": ("Four pieces, two eaten, so two are left: "
                          "$\\frac{2}{4}$ — which covers the same amount as "
                          "$\\frac{1}{2}$. Check: "
                          "$\\frac{2}{4} + \\frac{2}{4} = 1$ ✓."),
             "check": ["Eq(Rational(2,4) + Rational(2,4), 1)",
                       "Eq(Rational(2,4), Rational(1,2))"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counting the pieces you have", [
                "The bar below is cut into $4$ equal parts with $3$ of them shaded. That shaded amount is $\\frac{3}{4}$ — three quarters.",
                "Each number has its own job. The bottom $4$ records how the bread was CUT; the top $3$ records how many pieces you HAVE.",
                "So $\\frac{1}{4}$ and $\\frac{3}{4}$ come from the same cutting — the pieces are the same size, and only how many you took has changed.",
            ]), fig_34),
            workedset("Read both numbers",
                      "Bottom from the cutting, top from the counting.", [
                wex("A bar of $4$ pieces has $3$ shaded. Name the shaded part.",
                    ["Cut into four: bottom number $4$.",
                     "Three pieces shaded: top number $3$.",
                     "The shaded part is $\\frac{3}{4}$."],
                    "$\\frac{3}{4}$",
                    ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
                wex("A bar of $3$ pieces has $2$ shaded. Name the shaded part.",
                    ["Cut into three: bottom number $3$.",
                     "Two pieces shaded: top number $2$.",
                     "The shaded part is $\\frac{2}{3}$."],
                    "$\\frac{2}{3}$",
                    ["Eq(Rational(2,3) + Rational(1,3), 1)"]),
            ]),
            tryitset("Name the fraction", "How was it cut, and how many did you take?", [
                withfig(tp("The bar shows $2$ of $3$ equal parts shaded. That is:",
                   ["$\\frac{2}{3}$", "$\\frac{3}{2}$", "$\\frac{1}{3}$"],
                   "Cut into three, two taken: $\\frac{2}{3}$. Writing $\\frac{3}{2}$ swaps the jobs of the two numbers.",
                   ["Eq(Rational(2,3) + Rational(1,3), 1)"]), fig_23),
                tp("In $\\frac{3}{4}$, the $3$ counts:",
                   ["the pieces you have", "how the bread was cut",
                    "the number of breads"],
                   "The top number counts the pieces taken; the bottom, $4$, records that the bread was cut into four equal parts.",
                   ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
                tp("A bar cut into $4$ with $1$ shaded, and a bar cut into $4$ with $3$ shaded, have pieces that are:",
                   ["the same size — only the count differs",
                    "different sizes",
                    "impossible to compare"],
                   "Both were cut into four, so every piece is a quarter. Only how many were taken changed: $\\frac{1}{4}$ against $\\frac{3}{4}$.",
                   ["Rational(1,4) < Rational(3,4)",
                    "Eq(Rational(3,4) + Rational(1,4), 1)"]),
            ]),
            tapq("Which number changed?", "A bar of quarters goes from $1$ shaded to $3$ shaded. What changed?",
                 ["how many pieces were taken",
                  "the size of each piece",
                  "how the bar was cut",
                  "both the size and the count"],
                 "The cutting never changed — both bars are in quarters, so every piece is the same size. Only the top number moved, from $\\frac{1}{4}$ to $\\frac{3}{4}$.",
                 ["Rational(1,4) < Rational(3,4)",
                  "Eq(Rational(3,4) + Rational(1,4), 1)"]),
            funfact("Three quarters of an hour",
                    "Ask when the bus leaves and you might hear \"in three quarters of an hour\". That is $45$ minutes, because a quarter of $60$ is $15$ and three of them make $45$: $3 \\times 15 = 45$. Everyday speech is full of non-unit fractions, and almost nobody notices they are doing arithmetic."),
            withfig(teach("Concept B", "The leftover, and the whole", [
                "If $\\frac{3}{4}$ of a bar is shaded, what is plain? Just count the pieces you did not take: one of the four, so $\\frac{1}{4}$.",
                "The two always rebuild the whole: $\\frac{3}{4} + \\frac{1}{4} = 1$. Finding a leftover is never a new calculation — it is the pieces you left behind.",
                "And if you take EVERY piece? The bar below has all four quarters shaded, which is simply the whole bar: $\\frac{4}{4} = 1$. Whenever the top and bottom numbers match, the fraction is one whole.",
            ]), fig_44),
            workedset("Leftovers and wholes",
                      "Count what you did not take.", [
                wex("$\\frac{3}{4}$ of a bar is shaded. What is plain?",
                    ["Four pieces, three shaded, so one is left.",
                     "Plain is $\\frac{1}{4}$; check $\\frac{3}{4} + \\frac{1}{4} = 1$ ✓."],
                    "$\\frac{1}{4}$",
                    ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
                wex("What is $\\frac{3}{3}$ of a bread?",
                    ["Cut into three, all three taken.",
                     "That is the whole bread: $\\frac{3}{3} = 1$."],
                    "$1$ whole",
                    ["Eq(Rational(3,3), 1)", "Eq(Rational(4,4), 1)"]),
            ]),
            tryitset("What is left?", "Count the pieces you did not take.", [
                tp("$\\frac{1}{4}$ of a bread is eaten. What is left?",
                   ["$\\frac{3}{4}$", "$\\frac{1}{4}$", "$\\frac{1}{2}$"],
                   "Four pieces, one gone, three remain: $\\frac{1}{4} + \\frac{3}{4} = 1$ ✓.",
                   ["Eq(Rational(1,4) + Rational(3,4), 1)"]),
                tp("$\\frac{2}{3}$ of a bar is shaded. Plain is:",
                   ["$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{1}{2}$"],
                   "Three pieces, two shaded, so one is plain: $\\frac{1}{3}$.",
                   ["Eq(Rational(2,3) + Rational(1,3), 1)"]),
                tp("$\\frac{4}{4}$ of a bread is:",
                   ["the whole bread", "half the bread",
                    "four breads"],
                   "All four quarters of one bread ARE that bread: $\\frac{4}{4} = 1$. The bottom number never counts breads.",
                   ["Eq(Rational(4,4), 1)"]),
            ]),
            tapq("All the pieces", "A bread is cut into $3$ and all $3$ pieces are taken. How much is that?",
                 ["one whole bread", "three breads", "a third of a bread",
                  "two breads"],
                 "Taking every piece of one bread gives that bread back: $\\frac{3}{3} = 1$. The bottom number records how it was cut, never how many breads there were.",
                 ["Eq(Rational(3,3), 1)", "Eq(Rational(1,3)*3, 1)"]),
            recap([
                "The bottom number says how the whole was cut; the top says how many pieces you have.",
                "$\\frac{1}{4}$ and $\\frac{3}{4}$ have the same size pieces — only the count differs.",
                "The part taken and the part left always rebuild the whole: $\\frac{3}{4} + \\frac{1}{4} = 1$.",
                "When the top and bottom numbers match, the fraction is one whole: $\\frac{4}{4} = 1$.",
            ]),
            tip("Read every fraction as a sentence: \"cut into four, take three\". Two numbers, two jobs — and said that way round, they are almost impossible to swap."),
            tryitset("Chapter practice", "Cut into how many, take how many?", [
                tp("A bar of $4$ pieces with $3$ shaded shows:",
                   ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{1}{4}$"],
                   "Cut into four, three taken: $\\frac{3}{4}$. The remaining piece is $\\frac{1}{4}$.",
                   ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
                tp("$\\frac{2}{2}$ of a bread is:",
                   ["the whole bread", "half the bread", "two breads"],
                   "Both halves of one bread are that bread: $\\frac{2}{2} = 1$.",
                   ["Eq(Rational(2,2), 1)"]),
                tp("Saruul eats $\\frac{1}{3}$ and Bat eats $\\frac{1}{3}$ of the same bread. Together they ate:",
                   ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "the whole bread"],
                   "Two of the three pieces are gone: $\\frac{2}{3}$, with $\\frac{1}{3}$ still on the plate.",
                   ["Eq(Rational(1,3) + Rational(1,3), Rational(2,3))",
                    "Eq(Rational(2,3) + Rational(1,3), 1)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"More Than One Part\"",
                    "Both numbers of a fraction now have jobs you can name. The last lesson takes fractions off the bread entirely and puts them onto a group of objects — where finding a half turns out to be a division you already know.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — A Fraction of a Set
# ==========================================================================

def lesson_of_a_set():
    fig_half10 = sets_of(10, 2)
    fig_quarter12 = sets_of(12, 4, C_GREEN)
    fig_third9 = sets_of(9, 3, C_WARM)
    return {
        "slug": "a-fraction-of-a-set",
        "title": "A Fraction of a Set",
        "concreteComparison": (
            "Half a bread is a piece you can hold. Half of $10$ sweets is "
            "not a piece at all — it is $5$ sweets. Finding a fraction of "
            "a group means sharing the group into equal parts, which is "
            "the division you already know."),
        "objective": (
            "Find a half, a third or a quarter of a set of objects by "
            "sharing it equally, and connect the answer to a division "
            "fact."),
        "concept": [
            "**A fraction of a set is a sharing.** Half of $10$ sweets "
            "means sharing the $10$ into $2$ equal groups and taking one "
            "group: $10 \\div 2 = 5$. The bottom number tells you how "
            "many groups to make.",
            "**A quarter means four groups.** A quarter of $12$ pencils "
            "is $12 \\div 4 = 3$ pencils, and a third of $9$ stones is "
            "$9 \\div 3 = 3$ stones. Every one of these is a division fact "
            "you already own.",
            "**More than one part means take more groups.** "
            "$\\frac{3}{4}$ of $12$ is three of those four groups: "
            "$3 \\times 3 = 9$. Share first, then count out as many "
            "groups as the top number says.",
        ],
        "keyIdea": (
            "To find a fraction of a set, divide by the bottom number to "
            "make the groups, then take as many groups as the top number "
            "says."),
        "facts": [
            {"title": "Half of a set",
             "latex": "10 \\div 2 = 5",
             "explanation": "Half of 10 sweets is 5 — sharing into two equal groups."},
            {"title": "Three quarters of a set",
             "latex": "3 \\times 3 = 9",
             "explanation": "A quarter of 12 is 3, so three quarters is three of those groups."},
        ],
        "workedExamples": [
            {"id": "g3fr-l5-we1",
             "statement": "Find half of $10$ sweets.",
             "note": "The bottom number says how many groups.",
             "solution": ("A half means two equal groups, so share the sweets "
                          "into two: $10 \\div 2 = 5$. Half of $10$ is $5$ "
                          "sweets, and the receipt $2 \\times 5 = 10$ ✓ "
                          "confirms it."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(10, 2), 5)", "Eq(2*5, 10)"]},
            {"id": "g3fr-l5-we2",
             "statement": "Find $\\frac{3}{4}$ of $12$ pencils.",
             "note": "Make the groups first, then count them out.",
             "solution": ("The bottom number $4$ says make four equal groups: "
                          "$12 \\div 4 = 3$ pencils in each. The top number $3$ "
                          "says take three of those groups: "
                          "$3 \\times 3 = 9$ pencils. So $\\frac{3}{4}$ of $12$ "
                          "is $9$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(12, 4), 3)", "Eq(3*3, 9)", "9 < 12"]},
        ],
        "commonMistakes": [
            {"text": "Dividing by the TOP number — finding 3/4 of 12 by working out 12 ÷ 3.",
             "correction": "The bottom number makes the groups, so divide by 4: 12 ÷ 4 = 3 in each group, then take 3 groups for 9. Dividing by 3 answers a different question.",
             "authored": True},
            {"text": "Stopping after the division when the top number is not 1 — answering 3/4 of 12 with 3.",
             "correction": "3 is a quarter of 12, which is one group. Three quarters takes three of those groups: 3 × 3 = 9.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3fr-l5-t1",
             "statement": "Find a quarter of $12$ pencils, and give the receipt.",
             "solution": ("Four equal groups: $12 \\div 4 = 3$ pencils. Receipt: "
                          "$4 \\times 3 = 12$ ✓."),
             "check": ["Eq(Rational(12, 4), 3)", "Eq(4*3, 12)"]},
            {"id": "g3fr-l5-t2",
             "statement": "Find $\\frac{2}{3}$ of $9$ stones.",
             "solution": ("Three equal groups: $9 \\div 3 = 3$ stones each. Take "
                          "two groups: $2 \\times 3 = 6$ stones."),
             "check": ["Eq(Rational(9, 3), 3)", "Eq(2*3, 6)", "6 < 9"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Sharing a group instead of a bread", [
                "Half of a bread is a piece. Half of $10$ sweets is not a piece at all — you cannot cut the pile down the middle without cutting a sweet.",
                "Instead you SHARE. Two equal groups, as the picture below shows: $10 \\div 2 = 5$ sweets in each. Half of $10$ is $5$.",
                "So a fraction of a set is a division, and the bottom number tells you how many groups to make. Every one of these is a division fact you already know.",
            ]), fig_half10),
            workedset("A unit fraction of a set",
                      "Divide by the bottom number.", [
                wex("Find half of $10$ sweets.",
                    ["A half means two equal groups.",
                     "$10 \\div 2 = 5$ sweets each; receipt $2 \\times 5 = 10$ ✓."],
                    "$5$ sweets",
                    ["Eq(Rational(10, 2), 5)", "Eq(2*5, 10)"]),
                wex("Find a quarter of $12$ pencils.",
                    ["A quarter means four equal groups.",
                     "$12 \\div 4 = 3$ pencils each; receipt $4 \\times 3 = 12$ ✓."],
                    "$3$ pencils",
                    ["Eq(Rational(12, 4), 3)", "Eq(4*3, 12)"]),
            ]),
            tryitset("Share the group", "The bottom number is how many groups.", [
                withfig(tp("The picture shows $12$ pencils in four equal groups. A quarter of $12$ is:",
                   ["$3$", "$4$", "$8$"],
                   "$12 \\div 4 = 3$ pencils in each group. Answering $4$ repeats the number of groups, and $8$ subtracts.",
                   ["Eq(Rational(12, 4), 3)", "Eq(4*3, 12)",
                    "Eq(12 - 4, 8)"]), fig_quarter12),
                tp("Half of $16$ buuz is:",
                   ["$8$", "$2$", "$14$"],
                   "Two equal groups: $16 \\div 2 = 8$ buuz each. Receipt: $2 \\times 8 = 16$ ✓.",
                   ["Eq(Rational(16, 2), 8)", "Eq(2*8, 16)"]),
                tp("A third of $9$ stones is:",
                   ["$3$", "$6$", "$27$"],
                   "Three equal groups: $9 \\div 3 = 3$ stones each. Answering $6$ takes two groups instead of one.",
                   ["Eq(Rational(9, 3), 3)", "Eq(3*3, 9)", "Eq(2*3, 6)"]),
            ]),
            withfig(tapq("Which number makes the groups?", "To find a third of $9$ stones, you should:",
                 ["share the $9$ into $3$ equal groups",
                  "share the $9$ into $1$ group",
                  "multiply $9$ by $3$",
                  "subtract $3$ from $9$"],
                 "The bottom number says how many groups: three of them, $9 \\div 3 = 3$ stones each. Multiplying would give $27$, more stones than there are.",
                 ["Eq(Rational(9, 3), 3)", "Eq(3*9, 27)", "27 > 9"]),
                 fig_third9),
            funfact("Why shopkeepers love halves and quarters",
                    "Ask for half a kilo and everyone knows what you mean; ask for three sevenths of a kilo and the shop stops. Halves, thirds and quarters survive in daily trade because their divisions come out cleanly on the numbers people actually use — $10$, $12$, $20$, $60$. The fractions we kept are the ones that share out without argument."),
            withfig(teach("Concept B", "Taking more than one group", [
                "Now for $\\frac{3}{4}$ of $12$ pencils. The bottom number still makes the groups: $12 \\div 4 = 3$ pencils in each — the picture below.",
                "Then the top number counts how many groups to take. Three of them: $3 \\times 3 = 9$ pencils. So $\\frac{3}{4}$ of $12$ is $9$.",
                "Two steps, in that order — share, then count out. Stopping after the division answers $\\frac{1}{4}$ instead, and dividing by the top number answers nothing at all.",
            ]), fig_quarter12),
            workedset("More than one group",
                      "Divide by the bottom, multiply by the top.", [
                wex("Find $\\frac{3}{4}$ of $12$ pencils.",
                    ["Four groups: $12 \\div 4 = 3$ each.",
                     "Take three groups: $3 \\times 3 = 9$ pencils."],
                    "$9$ pencils",
                    ["Eq(Rational(12, 4), 3)", "Eq(3*3, 9)"]),
                wex("Find $\\frac{2}{3}$ of $12$ sweets.",
                    ["Three groups: $12 \\div 3 = 4$ each.",
                     "Take two groups: $2 \\times 4 = 8$ sweets."],
                    "$8$ sweets",
                    ["Eq(Rational(12, 3), 4)", "Eq(2*4, 8)", "8 < 12"]),
            ]),
            tryitset("Share, then count out", "Bottom number divides; top number multiplies.", [
                tp("$\\frac{3}{4}$ of $8$ apples is:",
                   ["$6$", "$2$", "$4$"],
                   "$8 \\div 4 = 2$ apples per group, then three groups: $3 \\times 2 = 6$. Stopping at $2$ answers only a quarter.",
                   ["Eq(Rational(8, 4), 2)", "Eq(3*2, 6)", "6 < 8"]),
                tp("$\\frac{2}{3}$ of $6$ stones is:",
                   ["$4$", "$2$", "$3$"],
                   "$6 \\div 3 = 2$ stones per group, then two groups: $2 \\times 2 = 4$.",
                   ["Eq(Rational(6, 3), 2)", "Eq(2*2, 4)"]),
                tp("To find $\\frac{3}{4}$ of $12$, Bat works out $12 \\div 3$. He:",
                   ["divided by the top number instead of the bottom",
                    "should have multiplied first",
                    "is right — the answer is $4$"],
                   "The bottom number makes the groups, so it should be $12 \\div 4 = 3$, then $3 \\times 3 = 9$. Bat's $12 \\div 3 = 4$ answers a different question altogether.",
                   ["Eq(Rational(12, 4), 3)", "Eq(3*3, 9)",
                    "Eq(Rational(12, 3), 4)"]),
            ]),
            tapq("Two steps, in order", "To find $\\frac{2}{3}$ of $9$, what do you do?",
                 ["divide by $3$, then multiply by $2$",
                  "divide by $2$, then multiply by $3$",
                  "multiply by $2$, then divide by $9$",
                  "divide by $2$ only"],
                 "The bottom number makes the groups: $9 \\div 3 = 3$ in each. Then the top number counts them out: $2 \\times 3 = 6$. So $\\frac{2}{3}$ of $9$ is $6$.",
                 ["Eq(Rational(9, 3), 3)", "Eq(2*3, 6)", "6 < 9"]),
            recap([
                "A fraction of a set is a sharing, not a cutting.",
                "Divide by the BOTTOM number to make the equal groups.",
                "Multiply by the TOP number to count out how many groups you take.",
                "Half of $10$ is $5$; $\\frac{3}{4}$ of $12$ is $9$ — and the answer is always smaller than the set.",
            ]),
            tip("Say it as two moves before you write anything: \"share into four, take three\". The order is the whole method, and saying it stops the two numbers swapping jobs."),
            tryitset("Chapter practice", "Share by the bottom, take by the top.", [
                tp("Half of $20$ sweets is:",
                   ["$10$", "$2$", "$18$"],
                   "Two equal groups: $20 \\div 2 = 10$ sweets each. Receipt: $2 \\times 10 = 20$ ✓.",
                   ["Eq(Rational(20, 2), 10)", "Eq(2*10, 20)"]),
                tp("$\\frac{3}{4}$ of $20$ sweets is:",
                   ["$15$", "$5$", "$60$"],
                   "$20 \\div 4 = 5$ per group, then three groups: $3 \\times 5 = 15$. Stopping at $5$ answers only a quarter.",
                   ["Eq(Rational(20, 4), 5)", "Eq(3*5, 15)", "15 < 20"]),
                tp("A third of $30$ stones is:",
                   ["$10$", "$3$", "$90$"],
                   "Three equal groups: $30 \\div 3 = 10$ stones each. Multiplying would give $90$, three times more stones than exist.",
                   ["Eq(Rational(30, 3), 10)", "Eq(3*10, 30)",
                    "Eq(3*30, 90)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"A Fraction of a Set\" — and the topic",
                    "Equal parts, halves and quarters, thirds and comparing, more than one part, and fractions of a group. Every one of them came back to the bottom number and what it counts. Next comes shapes — and the same word, \"equal\", turns out to matter there too.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = fig_bar(1, 4, "one quarter shaded")
    fig_pr6 = sets_of(12, 3, C_WARM)
    return [
        withprobfig(prob("g3fr-pr1", "The bar shows equal parts with one shaded. Name the shaded part, and say how many more would fill the bar.",
             "The bar is cut into $4$ equal parts with one shaded, so the shaded part is $\\frac{1}{4}$. Three more quarters would fill it: $\\frac{1}{4} + \\frac{3}{4} = 1$.",
             ["Eq(Rational(1,4) + Rational(3,4), 1)",
              "Eq(Rational(1,4)*4, 1)"]), fig_pr1),
        prob("g3fr-pr2", "A bread is cut into two pieces, one bigger than the other. Explain why neither piece is a half.",
             "A half is one of two EQUAL parts. These pieces are not equal, so neither is a half — the bread is simply in two pieces. Cut fairly, each would be $\\frac{1}{2}$ and the two would rebuild the bread: $\\frac{1}{2} + \\frac{1}{2} = 1$.",
             ["Eq(Rational(1,2) + Rational(1,2), 1)"]),
        prob("g3fr-pr3", "Put $\\frac{1}{2}$, $\\frac{1}{3}$ and $\\frac{1}{4}$ of the same bread in order from smallest to largest, and explain the pattern in one sentence.",
             "$\\frac{1}{4} < \\frac{1}{3} < \\frac{1}{2}$. The more parts the bread is cut into, the smaller each part becomes — so the sizes run in the reverse order of the bottom numbers.",
             ["Rational(1,4) < Rational(1,3)", "Rational(1,3) < Rational(1,2)"]),
        prob("g3fr-pr4", "A bar of $4$ equal pieces has $2$ shaded. Give two names for the shaded amount and explain why both are right.",
             "Two of four pieces is $\\frac{2}{4}$. Laid against a bar folded once, those two quarters cover exactly one half, so the same amount is also $\\frac{1}{2}$. The pieces differ in size and number, but the bread covered is identical.",
             ["Eq(Rational(2,4), Rational(1,2))",
              "Eq(Rational(2,4) + Rational(2,4), 1)"]),
        prob("g3fr-pr5", "$\\frac{2}{3}$ of a bar is shaded. What fraction is plain, and how do you know without measuring?",
             "The bar has three equal parts and two are shaded, so exactly one is plain: $\\frac{1}{3}$. No measuring is needed — the shaded and the plain always rebuild the whole, and $\\frac{2}{3} + \\frac{1}{3} = 1$ ✓.",
             ["Eq(Rational(2,3) + Rational(1,3), 1)"]),
        withprobfig(prob("g3fr-pr6", "The picture shows a set shared into three equal groups. Find a third of $12$, then $\\frac{2}{3}$ of $12$.",
             "Three equal groups: $12 \\div 3 = 4$, so a third of $12$ is $4$. Two of those groups gives $\\frac{2}{3}$: $2 \\times 4 = 8$. Share first, then count out as many groups as the top number says.",
             ["Eq(Rational(12, 3), 4)", "Eq(2*4, 8)", "8 < 12"]), fig_pr6),
        prob("g3fr-pr7", "Find $\\frac{3}{4}$ of $16$ sweets, showing both steps, and say what answer a pupil gets if they stop after the first step.",
             "Step one — four equal groups: $16 \\div 4 = 4$ sweets each. Step two — take three groups: $3 \\times 4 = 12$ sweets. A pupil who stops after step one answers $4$, which is a quarter of the sweets rather than three quarters.",
             ["Eq(Rational(16, 4), 4)", "Eq(3*4, 12)", "12 < 16"]),
        prob("g3fr-pr8", "Saruul says $\\frac{1}{3}$ of her bread is more than $\\frac{1}{2}$ of Bat's. Say when she could be right and when she must be wrong.",
             "If the two breads are the same size she is wrong, because $\\frac{1}{2} > \\frac{1}{3}$ always for one whole. But if her bread is much larger, a third of it really can be more bread than half of his — fractions only compare when the wholes match.",
             ["Rational(1,2) > Rational(1,3)", "Eq(Rational(1,3)*3, 1)"]),
    ]


def test_bank():
    return [
        prob("g3fr-x1", "A bar is cut into $3$ equal parts with $1$ shaded. Name the shaded and the plain fractions, and show they rebuild the bar.",
             "Shaded $\\frac{1}{3}$, plain $\\frac{2}{3}$. Together they rebuild the bar: $\\frac{1}{3} + \\frac{2}{3} = 1$ ✓.",
             ["Eq(Rational(1,3) + Rational(2,3), 1)",
              "Eq(Rational(1,3)*3, 1)"]),
        prob("g3fr-x2", "Explain why $\\frac{1}{4}$ is smaller than $\\frac{1}{2}$ even though $4$ is bigger than $2$.",
             "The bottom number counts how many ways the whole was cut, and cutting more ways makes every piece smaller. Four pieces from one bread are each smaller than two pieces from the same bread, so $\\frac{1}{4} < \\frac{1}{2}$ — the one place in arithmetic where a bigger number means less.",
             ["Rational(1,4) < Rational(1,2)", "4 > 2",
              "Eq(Rational(1,4)*4, 1)"]),
        prob("g3fr-x3", "How many quarters make one whole, and how many make one half? Show both.",
             "Four quarters make a whole: $\\frac{1}{4} \\times 4 = 1$. Two quarters make a half: $\\frac{2}{4} = \\frac{1}{2}$. The bottom number is always the count needed to rebuild the whole.",
             ["Eq(Rational(1,4)*4, 1)", "Eq(Rational(2,4), Rational(1,2))"]),
        prob("g3fr-x4", "A bread is cut into $4$ and Bat eats $3$ pieces. Write what he ate and what is left, and say what the two numbers of each fraction count.",
             "He ate $\\frac{3}{4}$ and $\\frac{1}{4}$ is left, since $\\frac{3}{4} + \\frac{1}{4} = 1$. In each fraction the bottom $4$ records that the bread was cut into four equal parts, and the top number counts how many of those pieces the fraction is talking about.",
             ["Eq(Rational(3,4) + Rational(1,4), 1)"]),
        prob("g3fr-x5", "Find half of $18$ stones and a third of $18$ stones. Which is bigger, and does that match the fractions?",
             "Half: $18 \\div 2 = 9$. A third: $18 \\div 3 = 6$. The half is bigger, which matches $\\frac{1}{2} > \\frac{1}{3}$ — sharing among fewer groups always leaves more in each group.",
             ["Eq(Rational(18, 2), 9)", "Eq(Rational(18, 3), 6)", "9 > 6",
              "Rational(1,2) > Rational(1,3)"]),
        prob("g3fr-x6", "Find $\\frac{3}{4}$ of $12$ and $\\frac{2}{3}$ of $12$, showing both steps of each, and say which is more.",
             "$\\frac{3}{4}$ of $12$: four groups give $12 \\div 4 = 3$ each, and three groups is $3 \\times 3 = 9$. $\\frac{2}{3}$ of $12$: three groups give $12 \\div 3 = 4$ each, and two groups is $2 \\times 4 = 8$. So $\\frac{3}{4}$ of $12$ is the larger, by one sweet.",
             ["Eq(Rational(12, 4), 3)", "Eq(3*3, 9)", "Eq(Rational(12, 3), 4)",
              "Eq(2*4, 8)", "9 > 8", "Eq(9 - 8, 1)"]),
    ]


def main():
    topic = {
        "slug": "fractions-halves-and-quarters",
        "title": "Fractions — Halves, Thirds & Quarters",
        "grade": 3,
        "status": "published",
        "blurb": ("Equal parts as the promise every fraction makes, naming "
                  "halves, thirds and quarters, why a bigger bottom number "
                  "means a smaller piece, taking more than one part, and "
                  "finding a fraction of a set by sharing it."),
        "lessons": [
            lesson_equal_parts(),
            lesson_halves_quarters(),
            lesson_thirds(),
            lesson_more_than_one(),
            lesson_of_a_set(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "fractions-halves-and-quarters.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
