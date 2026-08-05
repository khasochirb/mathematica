#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Times Tables & Multiplication.

Equal groups and repeated addition (multiplication as the short name for
adding the same number again and again), the friendly tables of 2, 5 and
10 with their endings patterns, the tables of 6 to 9 built from facts
already owned (sixes from fives, nines from tens, the digit-sum alarm),
arrays and the turnaround trick (one rectangle, two facts — the table
halved), and two-digit by one-digit multiplication split by place.

Through-line: BUILD THE FACT YOU NEED FROM A FACT YOU ALREADY OWN.
Every lesson returns to it: the count-bys give you the first facts, the
hard tables are one small step from the friendly ones, the turnaround
hands you every partner free, and big multiplications are just table
facts stacked by place.

Grade discipline: times tables to 10, no negative numbers, all values
inside 10 000; only the place-split lesson goes past single digits, and
only to two-digit by one-digit. Every check is sympy-asserted with exact
integers BEFORE the JSON is written — a wrong fact cannot ship. Figures
are built from the SAME Python variables as the statements they
illustrate, so text and picture cannot disagree.

Run: python3 scripts/grade4/build_times_tables_and_multiplication.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, workedset, write_topic,
                     fig_groups, fig_numline, fig_geo, P, seg, ang,
                     C_ACCENT, C_WARM, C_GREEN)


# ==========================================================================
# Lesson 1 — Equal Groups
# ==========================================================================

def lesson_equal_groups():
    # 4 gers with 3 horses each — the lesson's anchor picture
    g, s = 4, 3
    fig_gers = fig_groups((s, "ger 1"), (s, "ger 2"), (s, "ger 3"), (s, "ger 4"))
    # Concept B anchor: the fact 3 x 5 drawn as 3 groups of 5
    fig_draw = fig_groups((5, "group 1", C_GREEN), (5, "group 2", C_GREEN),
                          (5, "group 3", C_GREEN))
    # tp figures
    fig_plates = fig_groups((2, "plate 1", C_WARM), (2, "plate 2", C_WARM),
                            (2, "plate 3", C_WARM), (2, "plate 4", C_WARM),
                            (2, "plate 5", C_WARM))
    fig_baskets = fig_groups((9, "basket 1", C_ACCENT), (9, "basket 2", C_WARM))
    return {
        "slug": "equal-groups",
        "title": "Equal Groups",
        "concreteComparison": (
            "Four gers stand by the river, and three horses are tied at "
            "each one. To count the horses you could add: $3 + 3 + 3 + 3 "
            "= 12$. Multiplication says the same thing in one short "
            "word: $4 \\times 3 = 12$ — four groups of three. A times "
            "fact is repeated addition wearing a short name."),
        "objective": (
            "Read a picture of equal groups as a times fact, write a "
            "times fact as repeated addition, and draw the picture that "
            "a times fact describes."),
        "concept": [
            "**Multiplication counts equal groups.** $4 \\times 3$ means "
            "$4$ groups with $3$ in each: $3 + 3 + 3 + 3 = 12$. The "
            "first number counts the GROUPS, the second says how many "
            "are IN each group.",
            "**It only works when the groups match.** Groups of $3, 3, "
            "3$ and $4$ have no single times fact — the whole point of "
            "$\\times$ is that every group is the same size, so one "
            "number can speak for all of them.",
            "**Pictures and facts translate both ways.** See $5$ plates "
            "of $2$ buuz: write $5 \\times 2 = 10$. Read $3 \\times 5$: "
            "draw $3$ circles with $5$ dots in each and count $15$. "
            "Every times fact is a picture you could draw.",
        ],
        "keyIdea": (
            "A times fact is repeated addition in one word: the first "
            "number counts the equal groups, the second counts inside "
            "one group — and the picture and the fact must always tell "
            "the same story."),
        "facts": [
            {"title": "Groups of",
             "latex": "4 \\times 3 = 3 + 3 + 3 + 3 = 12",
             "explanation": "Four groups of three: the times sign is a short name for the repeated sum."},
            {"title": "Equal or nothing",
             "latex": "3 + 3 + 4 \\ne 3 \\times 3",
             "explanation": "Unequal groups have no times name — every group must be the same size."},
        ],
        "workedExamples": [
            {"id": "g4tm-l1-we1",
             "statement": "Four gers each have $3$ horses tied outside. Write the repeated addition and the times fact for the total.",
             "note": "Count the groups first, then look inside one group.",
             "solution": ("Four groups of three: $3 + 3 + 3 + 3 = 12$. In one "
                          "word: $4 \\times 3 = 12$ — twelve horses, counted at "
                          "a stroke."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3 + 3 + 3 + 3, 12)", "Eq(4*3, 12)"]},
            {"id": "g4tm-l1-we2",
             "statement": "Batu packs $6$ bags with $5$ buuz in each. How many buuz — as a sum and as a times fact?",
             "note": "Six groups of five.",
             "solution": ("$5 + 5 + 5 + 5 + 5 + 5 = 30$, which multiplication "
                          "writes as $6 \\times 5 = 30$. Six groups, five in "
                          "each — thirty buuz."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5 + 5 + 5 + 5 + 5 + 5, 30)", "Eq(6*5, 30)"]},
        ],
        "commonMistakes": [
            {"text": "Adding the two numbers — reading 4 × 3 as 4 + 3 = 7.",
             "correction": "The times sign counts GROUPS: four groups of three is 3 + 3 + 3 + 3 = 12. Adding 4 + 3 = 7 counts one group and the number of groups together — a different, wrong story.",
             "authored": True},
            {"text": "Writing a times fact for unequal groups — calling groups of 3, 3 and 4 \"3 × 3\".",
             "correction": "3 × 3 = 9, but the picture holds 3 + 3 + 4 = 10. Multiplication needs every group the same size; if one group differs, add instead.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4tm-l1-t1",
             "statement": "Write $7 \\times 2$ as repeated addition and find it.",
             "solution": "Seven groups of two: $2 + 2 + 2 + 2 + 2 + 2 + 2 = 14$, so $7 \\times 2 = 14$.",
             "check": ["Eq(2 + 2 + 2 + 2 + 2 + 2 + 2, 14)", "Eq(7*2, 14)"]},
            {"id": "g4tm-l1-t2",
             "statement": "A picture shows $3$ nests with $6$ eggs in each. Write the times fact and the total.",
             "solution": "Three groups of six: $6 + 6 + 6 = 18$, so $3 \\times 6 = 18$ eggs.",
             "check": ["Eq(6 + 6 + 6, 18)", "Eq(3*6, 18)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Groups of the same size", [
                "Four gers, three horses tied at each — the picture below. To count them you could add: $3 + 3 + 3 + 3 = 12$.",
                "Multiplication says it in one word: $4 \\times 3 = 12$, read \"four groups of three\". The first number counts the GROUPS; the second counts inside ONE group.",
                "The times sign is a promise: every group is the same size. That promise is what lets one short fact replace a long sum.",
            ]), fig_gers),
            workedset("From picture to fact",
                      "Count the groups, look inside one, write the fact.", [
                wex("Four gers, $3$ horses at each. The sum and the fact?",
                    ["Four groups of three: $3 + 3 + 3 + 3 = 12$.",
                     "One word: $4 \\times 3 = 12$."],
                    "$4 \\times 3 = 12$",
                    ["Eq(3 + 3 + 3 + 3, 12)", "Eq(4*3, 12)"]),
                wex("Six bags with $5$ buuz in each. The sum and the fact?",
                    ["$5 + 5 + 5 + 5 + 5 + 5 = 30$.",
                     "$6 \\times 5 = 30$ — six groups of five."],
                    "$6 \\times 5 = 30$",
                    ["Eq(5 + 5 + 5 + 5 + 5 + 5, 30)", "Eq(6*5, 30)"]),
            ]),
            tryitset("Read the groups", "Groups first, then inside one group.", [
                withfig(tp("The picture shows $5$ plates with $2$ buuz on each. The times fact is:",
                   ["$5 \\times 2 = 10$", "$5 + 2 = 7$", "$2 \\times 2 = 4$"],
                   "Five groups of two: $2 + 2 + 2 + 2 + 2 = 10$, so $5 \\times 2 = 10$. Writing $5 + 2 = 7$ adds the group count to one group — the classic mix-up.",
                   ["Eq(2 + 2 + 2 + 2 + 2, 10)", "Eq(5 + 2, 7)"]), fig_plates),
                tp("Three groups of $6$ written as repeated addition is:",
                   ["$6 + 6 + 6 = 18$", "$3 + 3 + 3 = 9$", "$6 + 3 = 9$"],
                   "Three groups, six in each: add the $6$ three times — $18$, which is $3 \\times 6$. Adding threes ($3 + 3 + 3 = 9$) counts the wrong thing three times.",
                   ["Eq(6 + 6 + 6, 18)", "Eq(3 + 3 + 3, 9)"]),
                tp("Which story matches $4 \\times 5$?",
                   ["$4$ boxes with $5$ pencils in each",
                    "$4$ pencils and $5$ more pencils",
                    "one box with $9$ pencils"],
                   "Four groups of five: $4 \\times 5 = 20$ pencils. The other stories are additions — $4 + 5 = 9$ — and an addition is not a times story.",
                   ["Eq(4*5, 20)", "Eq(4 + 5, 9)"]),
            ]),
            tapq("The broken promise", "A drawing shows groups of $4$, $4$, $4$ and $3$ apples. Can one times fact count it?",
                 ["no — one group has a different size",
                  "yes: $4 \\times 4 = 16$",
                  "yes: $4 \\times 3 = 12$",
                  "yes: $3 \\times 4 = 12$"],
                 "The total is $4 + 4 + 4 + 3 = 15$, but $4 \\times 4 = 16$ counts one apple too many — the times sign promises EQUAL groups, and this picture breaks the promise. Add instead.",
                 ["Eq(4 + 4 + 4 + 3, 15)", "Eq(4*4, 16)"]),
            funfact("Count the legs, not the horses",
                    "A horse stands on $4$ legs, so a herd of $6$ horses stands on $6 \\times 4 = 24$ legs — no need to count leg by leg. Multiplication was born exactly for this: whenever the world hands you equal groups, one fact counts them all at a stroke."),
            withfig(teach("Concept B", "From fact back to picture", [
                "Facts translate back into pictures. To draw $3 \\times 5$, draw $3$ groups with $5$ in each — like the picture below — and the count confirms it: $5 + 5 + 5 = 15$.",
                "Reading order matters for the picture: $3 \\times 5$ draws $3$ groups of $5$, while $5 \\times 3$ draws $5$ groups of $3$. Different drawings — later you will discover their totals secretly agree.",
                "If you can draw the picture, you own the fact. If you cannot say what the groups are, you are not multiplying yet.",
            ]), fig_draw),
            workedset("From fact to picture",
                      "Say the groups aloud, then draw and count them.", [
                wex("Draw $3 \\times 5$ and find the total.",
                    ["Three circles, five dots in each.",
                     "Count: $5 + 5 + 5 = 15$, so $3 \\times 5 = 15$."],
                    "$15$",
                    ["Eq(5 + 5 + 5, 15)", "Eq(3*5, 15)"]),
                wex("Saruul draws $2$ baskets with $9$ eggs in each. Which fact did she draw?",
                    ["Two groups of nine: $9 + 9 = 18$.",
                     "$2 \\times 9 = 18$."],
                    "$2 \\times 9 = 18$",
                    ["Eq(9 + 9, 18)", "Eq(2*9, 18)"]),
            ]),
            tryitset("Draw it in your head", "Groups from the first number, size from the second.", [
                tp("To draw $6 \\times 2$ you draw:",
                   ["$6$ groups with $2$ in each",
                    "$6$ groups with $6$ in each",
                    "$2$ groups with $2$ in each"],
                   "First number counts the groups, second the size: six groups of two, total $2 + 2 + 2 + 2 + 2 + 2 = 12$. Six groups of six would draw $36$ — a much bigger picture.",
                   ["Eq(6*2, 12)", "Eq(6*6, 36)"]),
                withfig(tp("The picture shows $2$ baskets of $9$ eggs. The total is:",
                   ["$18$", "$11$", "$81$"],
                   "Two groups of nine: $9 + 9 = 18$, so $2 \\times 9 = 18$. Answering $11$ adds $2 + 9$; answering $81$ multiplies $9 \\times 9$ — neither reads the picture.",
                   ["Eq(2*9, 18)", "Eq(2 + 9, 11)"]), fig_baskets),
                tp("Which repeated addition writes $8 \\times 3$, eight groups of three?",
                   ["$3 + 3 + 3 + 3 + 3 + 3 + 3 + 3$", "$8 + 8 + 8$", "$8 + 3$"],
                   "Eight groups of three is the $3$ added eight times: $24$. The sum $8 + 8 + 8$ also reaches $24$ — but it draws three groups of eight, a different picture. And $8 + 3 = 11$ is not a times story at all.",
                   ["Eq(8*3, 24)", "Eq(8 + 8 + 8, 24)"]),
            ]),
            tapq("Wheels in a row", "Seven motorbikes stand in a row, $2$ wheels each. How many wheels?",
                 ["$14$", "$9$", "$72$", "$7$"],
                 "Seven groups of two: $7 \\times 2 = 14$. Adding $7 + 2 = 9$ mixes the group count with a group; $72$ just glues the digits together.",
                 ["Eq(7*2, 14)", "Eq(7 + 2, 9)"]),
            recap([
                "A times fact is repeated addition in one word: 4 × 3 = 3 + 3 + 3 + 3.",
                "First number counts the groups; second counts inside one group.",
                "The times sign promises EQUAL groups — unequal groups must be added.",
                "Pictures and facts translate both ways: read groups into a fact, draw a fact into groups.",
            ]),
            tip("For every problem below, say the groups aloud first — \"so many groups of so many\" — before touching any numbers. The saying is the method."),
            tryitset("Mixed practice", "Pictures to facts and back again.", [
                tp("A ger camp has $5$ gers with $4$ beds in each. Total beds:",
                   ["$20$", "$9$", "$45$"],
                   "Five groups of four: $5 \\times 4 = 20$. Adding $5 + 4 = 9$ is the group-count trap; $45$ glues the digits.",
                   ["Eq(5*4, 20)", "Eq(5 + 4, 9)"]),
                tp("There are $3$ rows of stools with $7$ stools in each row. The times fact is:",
                   ["$3 \\times 7 = 21$", "$3 + 7 = 10$", "$3 \\times 7 = 24$"],
                   "Three groups of seven: $7 + 7 + 7 = 21$. The sum $3 + 7 = 10$ is an addition story, and $24$ is simply the wrong count.",
                   ["Eq(7 + 7 + 7, 21)", "Eq(3 + 7, 10)"]),
                tp("Which of these can NOT be written as one times fact?",
                   ["groups of $2$, $2$ and $3$",
                    "groups of $2$, $2$ and $2$",
                    "groups of $3$, $3$ and $3$"],
                   "Groups of $2, 2, 3$ total $2 + 2 + 3 = 7$, and no equal-groups fact makes $7$ from three groups: $3 \\times 2 = 6$ falls short and $3 \\times 3 = 9$ overshoots. The other two are $3 \\times 2 = 6$ and $3 \\times 3 = 9$ exactly.",
                   ["Eq(2 + 2 + 3, 7)", "Eq(3*2, 6)"]),
                tp("There are $6$ packets of $3$ pencils. Total pencils:",
                   ["$18$", "$9$", "$63$"],
                   "Six groups of three: $6 \\times 3 = 18$. Adding $6 + 3 = 9$ mixes the two numbers; $63$ glues the digits side by side.",
                   ["Eq(6*3, 18)", "Eq(6 + 3, 9)"]),
                tp("You draw $4$ circles and put $6$ dots in each. Total dots:",
                   ["$24$", "$10$", "$46$"],
                   "Four groups of six: $6 + 6 + 6 + 6 = 24$, so $4 \\times 6 = 24$. Adding gives $10$; gluing gives $46$ — both ignore the groups.",
                   ["Eq(4*6, 24)", "Eq(4 + 6, 10)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Equal Groups\"",
                    "Multiplication is repeated addition wearing a short name — groups first, size second, and the groups must match. Next: the three friendliest tables of all, the ones your hands and feet already know how to count.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Tables of 2, 5 and 10
# ==========================================================================

def lesson_friendly_tables():
    fig_2s = fig_numline([(2, "2"), (4, "4"), (6, "6"), (8, "8"),
                          (10, "10", C_WARM)], lo=0, hi=10)
    fig_5s = fig_numline([(5, "5"), (10, "10"), (15, "15"), (20, "20"),
                          (25, "25"), (30, "30", C_WARM)], lo=0, hi=30)
    fig_10s = fig_numline([(10, "10"), (20, "20"), (30, "30"), (40, "40"),
                           (50, "50", C_GREEN)], lo=0, hi=50)
    return {
        "slug": "tables-2-5-and-10",
        "title": "Tables of 2, 5 and 10",
        "concreteComparison": (
            "Boots at the ger door come in pairs — count them $2, 4, 6, "
            "8$. Fingers come in hands of five — $5, 10, 15, 20$. And "
            "ten fingers per person makes the tens table: $10, 20, 30$. "
            "The tables of $2$, $5$ and $10$ are the counts your hands "
            "and feet already know — the first times facts you will "
            "truly own."),
        "objective": (
            "Master the tables of 2, 5 and 10 through count-bys and "
            "doubles, and use their endings patterns — times-5 answers "
            "end in 0 or 5, times-10 answers end in 0 — to catch wrong "
            "answers on sight."),
        "concept": [
            "**A times table is a skip-count written down.** The table "
            "of $5$ IS the count $5, 10, 15, 20, 25, 30, 35, 40, 45, "
            "50$ — the fourth landing is $4 \\times 5 = 20$. Keep one "
            "finger up per landing and the count can never lose its "
            "place.",
            "**The 2s are doubles; the 10s are place value.** $7 \\times "
            "2$ is just $7 + 7 = 14$. And $7 \\times 10$ is $7$ tens — "
            "the $7$ slides into the tens column: $70$. No new work, "
            "only facts you already own.",
            "**Endings betray the table.** Every times-10 answer ends "
            "in $0$; every times-5 answer ends in $0$ or $5$; every "
            "times-2 answer is even. An answer with a forbidden ending "
            "is wrong before you even recount.",
        ],
        "keyIdea": (
            "The tables of 2, 5 and 10 are skip-counts you already "
            "carry: doubles, hands of five, whole tens — and their "
            "endings patterns work as an alarm that catches wrong "
            "answers on sight."),
        "facts": [
            {"title": "Doubles",
             "latex": "7 \\times 2 = 7 + 7 = 14",
             "explanation": "Two groups of anything is a double — the friendliest fact there is."},
            {"title": "The endings",
             "latex": "\\times 10 \\to \\text{ends in } 0 \\qquad \\times 5 \\to \\text{ends in } 0 \\text{ or } 5",
             "explanation": "Whole tens keep an empty ones column; fives take turns landing on 5 and 0."},
        ],
        "workedExamples": [
            {"id": "g4tm-l2-we1",
             "statement": "Find $6 \\times 2$ and $9 \\times 2$ using doubles.",
             "note": "Two groups of a number is the number plus itself.",
             "solution": ("$6 \\times 2 = 6 + 6 = 12$ and $9 \\times 2 = 9 + 9 = "
                          "18$. Both answers are even — as every times-2 answer "
                          "must be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6 + 6, 12)", "Eq(9 + 9, 18)"]},
            {"id": "g4tm-l2-we2",
             "statement": "Find $8 \\times 5$ and $8 \\times 10$, and compare them.",
             "note": "Fives are half of tens.",
             "solution": ("$8 \\times 5 = 40$ (count $5, 10, 15, 20, 25, 30, 35, "
                          "40$) and $8 \\times 10 = 80$ — eight tens. Notice "
                          "$80$ is double $40$: a ten is two fives, so times-10 "
                          "is always double times-5."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*5, 40)", "Eq(8*10, 80)", "Eq(2*40, 80)"]},
        ],
        "commonMistakes": [
            {"text": "Treating ×5 like ×10 — writing 7 × 5 = 75 by attaching the 5.",
             "correction": "Only times-10 slides the digit over: 7 × 10 = 70. For fives, count the landings: 5, 10, 15, 20, 25, 30, 35 — seven fives are 35.",
             "authored": True},
            {"text": "Losing count mid skip-count — reaching \"6 × 5\" by saying 5, 10, 15, 20, 25.",
             "correction": "That count has only FIVE landings, so it found 5 × 5 = 25. Raise one finger per landing; six fingers up means six fives: 30.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4tm-l2-t1",
             "statement": "Use a double to find $7 \\times 2$.",
             "solution": "$7 + 7 = 14$, so $7 \\times 2 = 14$ — and $14$ is even, as every times-2 answer is.",
             "check": ["Eq(7 + 7, 14)", "Eq(Mod(14, 2), 0)"]},
            {"id": "g4tm-l2-t2",
             "statement": "Count by fives to find $9 \\times 5$. What digit must the answer end in?",
             "solution": "Nine landings: $5, 10, 15, 20, 25, 30, 35, 40, 45$ — so $9 \\times 5 = 45$. Nine is odd, so the answer ends in $5$.",
             "check": ["Eq(9*5, 45)", "Eq(Mod(45, 10), 5)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Count-bys you already own", [
                "A times table is a skip-count written down. The line below counts by $2$s: $2, 4, 6, 8, 10$ — the fourth landing is $4 \\times 2 = 8$.",
                "The 2s are DOUBLES: $7 \\times 2 = 7 + 7 = 14$. The 5s are hands of five: $5, 10, 15, 20$. Keep one finger up per landing and the count cannot lose its place.",
                "The 10s are pure place value: $7 \\times 10$ is $7$ tens, so the $7$ slides into the tens column — $70$. You built this fact in place-value class without knowing it.",
            ]), fig_2s),
            workedset("Doubles and tens",
                      "Two groups is a double; ten groups slides the digit.", [
                wex("Find $6 \\times 2$ and $9 \\times 2$.",
                    ["Doubles: $6 + 6 = 12$ and $9 + 9 = 18$.",
                     "Both even — every times-2 answer is."],
                    "$12$ and $18$",
                    ["Eq(6 + 6, 12)", "Eq(9 + 9, 18)"]),
                wex("Find $4 \\times 10$ and $9 \\times 10$.",
                    ["Four tens and nine tens: the digit slides into the tens column.",
                     "$40$ and $90$ — both end in $0$."],
                    "$40$ and $90$",
                    ["Eq(4*10, 40)", "Eq(9*10, 90)"]),
            ]),
            tryitset("Friendly facts", "Doubles, hands, and sliding digits.", [
                tp("$8 \\times 2$ equals:",
                   ["$16$", "$10$", "$82$"],
                   "Double the $8$: $8 + 8 = 16$. Adding $8 + 2 = 10$ forgets the groups; $82$ glues the digits.",
                   ["Eq(8 + 8, 16)", "Eq(8 + 2, 10)"]),
                withfig(tp("Count along the line: $6 \\times 5$ equals:",
                   ["$30$", "$25$", "$35$"],
                   "Six landings: $5, 10, 15, 20, 25, 30$. Stopping at $25$ made only five landings — that is $5 \\times 5$. One finger per landing keeps the count honest.",
                   ["Eq(6*5, 30)", "Eq(5*5, 25)"]), fig_5s),
                tp("$9 \\times 10$ equals:",
                   ["$90$", "$19$", "$910$"],
                   "Nine tens: the $9$ slides into the tens column — $90$. Adding gives $19$; gluing the digits gives $910$, ten times too big.",
                   ["Eq(9*10, 90)", "Eq(9 + 10, 19)"]),
            ]),
            tapq("Hands of five", "One hand has $5$ fingers. How many fingers on $7$ hands?",
                 ["$35$", "$12$", "$57$", "$75$"],
                 "Seven groups of five: $7 \\times 5 = 35$ — count $5, 10, 15, 20, 25, 30, 35$. Adding $7 + 5 = 12$ misses the groups, and $75$ attaches the $5$ as if it were a ten.",
                 ["Eq(7*5, 35)", "Eq(7 + 5, 12)"]),
            funfact("The clock counts by fives",
                    "Look at a clock face: for the minute hand, each numeral marks five minutes. When the long hand points at the $7$, it shows $7 \\times 5 = 35$ minutes past — and the whole face holds $12 \\times 5 = 60$ minutes. Anyone who reads a clock is running the table of $5$."),
            withfig(teach("Concept B", "The endings alarm", [
                "Every times-10 answer ends in $0$ — the line below shows the landings $10, 20, 30, 40, 50$: whole tens keep an empty ones column.",
                "Times-5 answers take turns: an odd number of fives ends in $5$ ($7 \\times 5 = 35$), an even number pairs its fives into whole tens ($8 \\times 5 = 40$, because two fives make a ten).",
                "Use the endings as an ALARM. Someone claims $7 \\times 5 = 36$? It ends in $6$ — a forbidden ending for fives — so it is wrong before you even recount.",
            ]), fig_10s),
            workedset("The endings on patrol",
                      "Check the last digit before checking anything else.", [
                wex("Explain why $7 \\times 5 = 36$ must be wrong, then fix it.",
                    ["A times-5 answer ends in $0$ or $5$; $36$ ends in $6$ — alarm.",
                     "Count the fives: $7 \\times 5 = 35$, ending in $5$ as an odd count should."],
                    "$35$",
                    ["Eq(Mod(36, 10), 6)", "Eq(7*5, 35)"]),
                wex("What must $6 \\times 5$ and $9 \\times 5$ end in? Find both.",
                    ["$6$ is even: its fives pair into whole tens — ends in $0$: $30$.",
                     "$9$ is odd: one five left unpaired — ends in $5$: $45$."],
                    "$30$ and $45$",
                    ["Eq(6*5, 30)", "Eq(9*5, 45)"]),
            ]),
            tryitset("Alarm drills", "Forbidden endings mean wrong answers.", [
                tp("A times-10 answer always ends in:",
                   ["$0$", "$5$", "the digit you multiplied"],
                   "Ten groups make whole tens, and whole tens keep an empty ones column: $3 \\times 10 = 30$, $8 \\times 10 = 80$. The multiplied digit moves to the TENS column, not the end.",
                   ["Eq(Mod(30, 10), 0)", "Eq(8*10, 80)"]),
                tp("Which of these CANNOT be a times-5 answer: $32$, $40$ or $35$?",
                   ["$32$", "$40$", "$35$"],
                   "Fives land only on $0$ or $5$: $40 = 8 \\times 5$ and $35 = 7 \\times 5$ are honest landings, but $32$ ends in $2$ — no count of fives ever touches it.",
                   ["Eq(Mod(32, 5), 2)", "Eq(8*5, 40)"]),
                tp("$4 \\times 5$ ends in $0$ because:",
                   ["$4$ is even — the fives pair into whole tens",
                    "every times-5 answer ends in $0$",
                    "$5$ is an odd number"],
                   "Two fives make a ten, so an EVEN count of fives is whole tens: $4 \\times 5 = 2 \\times 10 = 20$. Odd counts leave one five over and end in $5$ — so not every times-5 answer ends in $0$.",
                   ["Eq(2*5, 10)", "Eq(4*5, 2*10)"]),
            ]),
            tapq("Even fives", "A student writes $8 \\times 5 = 45$. The endings alarm says:",
                 ["wrong — $8$ is even, so the answer must end in $0$: it is $40$",
                  "right — it ends in $5$, which fives allow",
                  "wrong — times-5 answers end only in $0$",
                  "the alarm cannot judge this fact"],
                 "$45$ is a genuine fives landing, but it belongs to $9 \\times 5$. An EVEN count of fives pairs into whole tens and must end in $0$: $8 \\times 5 = 40$. The alarm reads the ending AND the evenness together.",
                 ["Eq(8*5, 40)", "Eq(9*5, 45)"]),
            recap([
                "A times table is a skip-count written down — one finger per landing.",
                "2s are doubles: 7 × 2 = 7 + 7. 10s are place value: 7 × 10 = 70.",
                "Times-10 is always double times-5, because a ten is two fives.",
                "Endings alarm: ×10 ends in 0; ×5 ends in 0 (even count) or 5 (odd count); ×2 is always even.",
            ]),
            tip("Answer each one, then check its ENDING against the table's pattern before moving on — the alarm takes one second and catches almost everything."),
            tryitset("Mixed practice", "The three friendly tables, alarms on.", [
                tp("$7 \\times 2$ equals:",
                   ["$14$", "$9$", "$72$"],
                   "Double: $7 + 7 = 14$. Adding gives $9$; gluing gives $72$.",
                   ["Eq(7 + 7, 14)", "Eq(7 + 2, 9)"]),
                tp("$6 \\times 10$ equals:",
                   ["$60$", "$16$", "$6$"],
                   "Six tens — the $6$ slides into the tens column: $60$, ending in $0$ as every times-10 answer must.",
                   ["Eq(6*10, 60)", "Eq(6 + 10, 16)"]),
                tp("Nine people leave their boots in pairs at the ger door. How many boots?",
                   ["$18$", "$11$", "$81$"],
                   "Nine groups of two: $9 \\times 2 = 18$ — even, as a boots count in pairs must be. Adding $9 + 2 = 11$ misses the pairs.",
                   ["Eq(9*2, 18)", "Eq(9 + 2, 11)"]),
                tp("The count $5, 10, 15, 20$ lands next on:",
                   ["$25$", "$30$", "$21$"],
                   "One more five: $20 + 5 = 25$ — the fifth landing, $5 \\times 5$. Jumping to $30$ skips a landing; $21$ adds one instead of five.",
                   ["Eq(20 + 5, 25)", "Eq(5*5, 25)"]),
                tp("Which fact has the WRONG answer?",
                   ["$7 \\times 5 = 30$", "$6 \\times 5 = 30$", "$9 \\times 10 = 90$"],
                   "$7$ is odd, so $7 \\times 5$ must end in $5$: it is $35$, not $30$. The others check out: $6 \\times 5 = 30$ and $9 \\times 10 = 90$.",
                   ["Eq(7*5, 35)", "Eq(6*5, 30)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tables of 2, 5 and 10\"",
                    "Doubles, hands of five, sliding tens — and an endings alarm standing guard. These are the facts you now OWN. Next: the hard tables of 6 to 9, each built in one small step from a fact already in your pocket.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Tables of 6 to 9
# ==========================================================================

def lesson_hard_tables():
    # 7 x 6 built from 7 x 5: one more jump of 7
    a5, a6 = 7 * 5, 7 * 6
    fig_split = fig_numline([(a5, "7 × 5"), (a6, "7 × 6", C_WARM)], lo=0, hi=45)
    # tp: 4 x 6 from 4 x 5 — the line shows ONLY the owned anchor, so the
    # student must take the step of four themselves (no answer on show).
    b5 = 4 * 5
    fig_step = fig_numline([(b5, "4 × 5 = 20", C_ACCENT)], lo=0, hi=25)
    # the 9s landings
    fig_nines = fig_numline([(9, "9"), (18, "18"), (27, "27"), (36, "36"),
                             (45, "45", C_WARM)], lo=0, hi=45)
    return {
        "slug": "tables-6-to-9",
        "title": "Tables of 6 to 9",
        "concreteComparison": (
            "Nobody carries $7 \\times 6$ in their head at first — but "
            "you already own $7 \\times 5 = 35$. Seven groups of six "
            "are seven groups of five with one extra in each group: "
            "$35 + 7 = 42$. The hard tables are not new mountains; "
            "each fact is one small step up from a hill you have "
            "already climbed."),
        "objective": (
            "Build the tables of 6 to 9 from owned facts — sixes from "
            "fives, sevens from fives and twos, eights and nines from "
            "tens — and use the 9s digit patterns as a check."),
        "concept": [
            "**Sixes are fives plus one more each.** $7 \\times 6$ is "
            "$7$ groups of six, and each six is a five and a one: $7 "
            "\\times 6 = 7 \\times 5 + 7 = 35 + 7 = 42$. Sevens go one "
            "further — a seven is a five and a two: $7 \\times 7 = 35 "
            "+ 14 = 49$.",
            "**Eights and nines lean on the tens.** $7 \\times 9$ is "
            "seven tens with one taken back from each group: $70 - 7 = "
            "63$. Same road for eights: $6 \\times 8 = 60 - 12 = 48$. "
            "The subtraction signs its own receipt: $63 + 7 = 70$.",
            "**The 9s wear a pattern.** The answers $9, 18, 27, 36, "
            "45, 54, 63, 72, 81, 90$ hide two rules: the digits add to "
            "$9$ ($63$: $6 + 3 = 9$), and the tens digit is one less "
            "than the number you multiplied ($7 \\times 9$ starts with "
            "$6$). Use the pattern as an alarm, not as the answer.",
        ],
        "keyIdea": (
            "Build the fact you need from a fact you already own: "
            "sixes from fives, sevens from fives and twos, eights and "
            "nines from tens — and let the 9s digit pattern stand "
            "guard over the answers."),
        "facts": [
            {"title": "Sixes from fives",
             "latex": "7 \\times 6 = 7 \\times 5 + 7 = 35 + 7 = 42",
             "explanation": "Each of the seven groups grows by one — so add seven, once."},
            {"title": "Nines from tens",
             "latex": "7 \\times 9 = 70 - 7 = 63 \\quad (6 + 3 = 9)",
             "explanation": "Seven tens, minus one per group — and the digits of every 9s answer add to 9."},
        ],
        "workedExamples": [
            {"id": "g4tm-l3-we1",
             "statement": "Find $7 \\times 6$ starting from $7 \\times 5$.",
             "note": "Each of the seven groups grows by exactly one.",
             "solution": ("$7 \\times 5 = 35$. Growing each of the seven groups "
                          "from five to six adds seven ones: $35 + 7 = 42$. So "
                          "$7 \\times 6 = 42$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7*5, 35)", "Eq(7*6, 7*5 + 7)", "Eq(35 + 7, 42)"]},
            {"id": "g4tm-l3-we2",
             "statement": "Find $8 \\times 9$ from $8 \\times 10$, then check it with the digits pattern.",
             "note": "Eight tens, minus one from each group.",
             "solution": ("$8 \\times 10 = 80$; taking one back from each of the "
                          "eight groups leaves $80 - 8 = 72$ (receipt: $72 + 8 = "
                          "80$). Pattern check: $72$ starts with $7$, one less "
                          "than $8$, and $7 + 2 = 9$. Both guards are happy."),
             "badges": [{"text": "core"}],
             "check": ["Eq(80 - 8, 72)", "Eq(72 + 8, 80)", "Eq(7 + 2, 9)"]},
        ],
        "commonMistakes": [
            {"text": "Adding the wrong extra — building 7 × 6 as 7 × 5 + 5 = 40.",
             "correction": "SEVEN groups each grew by one, so the extra is 7, not 5: 35 + 7 = 42. Say it as \"one more in each of the seven groups\".",
             "authored": True},
            {"text": "Trusting the 9s digit-sum alone — answering 6 × 9 = 45 \"because 4 + 5 = 9\".",
             "correction": "Every 9s answer sums to 9, so a NEIGHBOUR'S answer passes the digit test too. Anchor first: 6 × 9 = 60 − 6 = 54; then let 5 + 4 = 9 confirm it.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4tm-l3-t1",
             "statement": "Build $9 \\times 6$ from $9 \\times 5$.",
             "solution": "$9 \\times 5 = 45$, and each of the nine groups grows by one: $45 + 9 = 54$. So $9 \\times 6 = 54$.",
             "check": ["Eq(9*6, 9*5 + 9)", "Eq(45 + 9, 54)"]},
            {"id": "g4tm-l3-t2",
             "statement": "Build $4 \\times 9$ from $4 \\times 10$, and check the digits.",
             "solution": "$4 \\times 10 = 40$; take one back per group: $40 - 4 = 36$ (receipt: $36 + 4 = 40$). Digits: $3 + 6 = 9$, and the $3$ is one less than $4$.",
             "check": ["Eq(40 - 4, 36)", "Eq(36 + 4, 40)", "Eq(3 + 6, 9)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One step up from a hill you own", [
                "The hard tables are built, not memorised cold. The line below: start at $7 \\times 5 = 35$ — a fact you own — and one more jump of $7$ lands on $7 \\times 6 = 42$.",
                "Why add SEVEN? Each of the seven groups grew from five to six: seven groups, one extra each. In symbols: $7 \\times 6 = 7 \\times 5 + 7$.",
                "Sevens take two steps: a seven is a five and a two, so $7 \\times 7 = 7 \\times 5 + 7 \\times 2 = 35 + 14 = 49$. Fives and twos — the tables from last lesson — carry you all the way.",
            ]), fig_split),
            workedset("Building the sixes and sevens",
                      "Fives plus extras; fives and twos together.", [
                wex("Find $7 \\times 6$ from $7 \\times 5$.",
                    ["$7 \\times 5 = 35$; each of the seven groups grows by one.",
                     "$35 + 7 = 42$."],
                    "$42$",
                    ["Eq(7*6, 7*5 + 7)", "Eq(35 + 7, 42)"]),
                wex("Find $6 \\times 7$ using fives and twos.",
                    ["A seven is a five and a two: $6 \\times 5 = 30$ and $6 \\times 2 = 12$.",
                     "$30 + 12 = 42$ — so $6 \\times 7 = 42$."],
                    "$42$",
                    ["Eq(6*7, 6*5 + 6*2)", "Eq(30 + 12, 42)"]),
            ]),
            tryitset("Small steps", "Name the owned fact, then the step.", [
                withfig(tp("The line marks the fact you own. Taking one step up from it, $4 \\times 6$ equals:",
                   ["$24$", "$25$", "$20$"],
                   "Start at $4 \\times 5 = 20$; the four groups each grow by one, so add $4$: $24$. Adding $5$ instead gives $25$ — the wrong extra. Stopping at $20$ never takes the step.",
                   ["Eq(4*6, 4*5 + 4)", "Eq(20 + 4, 24)"]), fig_step),
                tp("To build $8 \\times 7$ from $8 \\times 5 = 40$, you still need:",
                   ["$8 \\times 2 = 16$ more", "$2$ more", "$5$ more"],
                   "A seven is a five and a two, so the missing piece is $8 \\times 2 = 16$: $40 + 16 = 56$. Adding a bare $2$ forgets that all eight groups grew by two.",
                   ["Eq(8*2, 16)", "Eq(40 + 16, 56)"]),
                tp("$6 \\times 6$ equals:",
                   ["$36$", "$30$", "$35$"],
                   "From $6 \\times 5 = 30$, each of the six groups grows by one: $30 + 6 = 36$. Stopping at $30$ forgets the step; $35$ takes a step of five.",
                   ["Eq(30 + 6, 36)", "Eq(6*6, 36)"]),
            ]),
            tapq("The wrong extra", "A student builds $9 \\times 6$ as $9 \\times 5 + 5 = 50$. The slip:",
                 ["nine groups each grew by one — add $9$, not $5$: $45 + 9 = 54$",
                  "nothing — $50$ is right",
                  "the helper fact $9 \\times 5$ is wrong",
                  "sixes cannot be built from fives"],
                 "The extra counts the GROUPS: nine groups, one more in each, so add $9$. $9 \\times 5 = 45$ was correct; the step was not: $45 + 9 = 54 = 9 \\times 6$.",
                 ["Eq(45 + 9, 54)", "Eq(9*6, 54)", "Ne(50, 54)"]),
            funfact("Five, six, seven, eight",
                    "The fact $56 = 7 \\times 8$ spells out its own answer: read the digits $5, 6, 7, 8$ in a row and the first two are the answer to the last two. Its little cousin does the same trick: $12 = 3 \\times 4$ reads $1, 2, 3, 4$."),
            withfig(teach("Concept B", "Nines from tens, with a built-in alarm", [
                "Nines lean on tens: $7 \\times 9$ is seven tens with one taken back from each group — $70 - 7 = 63$, receipt $63 + 7 = 70$. Eights walk the same road two steps: $6 \\times 8 = 60 - 12 = 48$.",
                "The 9s landings — on the line below: $9, 18, 27, 36, 45$ — wear a pattern: the digits of every answer add to $9$, and the tens digit is ONE LESS than the number you multiplied ($7 \\times 9$ starts with $6$).",
                "The pattern is an alarm, not an answer: a claimed $9$s fact whose digits do not sum to $9$ is certainly wrong — but a wrong neighbour can pass, so always anchor with the tens first.",
            ]), fig_nines),
            workedset("Riding the nines",
                      "Tens minus one per group; digits standing guard.", [
                wex("Find $7 \\times 9$.",
                    ["Seven tens: $70$. One back per group: $70 - 7 = 63$ (receipt $63 + 7 = 70$).",
                     "Guards: $63$ starts with $6 = 7 - 1$, and $6 + 3 = 9$."],
                    "$63$",
                    ["Eq(70 - 7, 63)", "Eq(63 + 7, 70)", "Eq(6 + 3, 9)"]),
                wex("Fill the blank: $\\square \\times 9 = 54$.",
                    ["The tens digit of $54$ is $5$, one less than the mystery number: it is $6$.",
                     "Anchor: $6 \\times 9 = 60 - 6 = 54$, and $5 + 4 = 9$ confirms."],
                    "$6$",
                    ["Eq(54, 5*10 + 4)", "Eq(6*9, 54)"]),
            ]),
            tryitset("Tens roads", "Down from the ten, receipt in hand.", [
                tp("$5 \\times 9$ equals:",
                   ["$45$", "$44$", "$54$"],
                   "Five tens minus five: $50 - 5 = 45$ (receipt $45 + 5 = 50$). $44$ takes back one too many; $54$ belongs to $6 \\times 9$.",
                   ["Eq(50 - 5, 45)", "Eq(45 + 5, 50)"]),
                tp("Up to $9 \\times 10$, the digits of every answer in the 9s table add to:",
                   ["$9$", "$10$", "a different number each time"],
                   "Check any of them: $18$ gives $1 + 8 = 9$, $27$ gives $2 + 7 = 9$, $81$ gives $8 + 1 = 9$. One more guard for free: every 9s answer divides by $9$ exactly.",
                   ["Eq(2 + 7, 9)", "Eq(Mod(81, 9), 0)"]),
                tp("$3 \\times 9$ equals:",
                   ["$27$", "$21$", "$39$"],
                   "Three tens minus three: $30 - 3 = 27$ (receipt $27 + 3 = 30$), and $2 + 7 = 9$. $21$ takes back nine instead of three; $39$ glues the digits.",
                   ["Eq(30 - 3, 27)", "Eq(27 + 3, 30)"]),
            ]),
            tapq("The alarm that stays silent", "A student answers $8 \\times 9 = 63$. What does the digit-sum alarm do?",
                 ["stays silent — $6 + 3 = 9$ — yet the answer is still wrong: $8 \\times 9 = 72$",
                  "rings — the digits do not add to $9$",
                  "proves the answer is right",
                  "cannot be used on the 9s table"],
                 "$63$ is a true 9s answer — it just belongs to $7 \\times 9$. The digit sum passes, so the alarm stays silent; only the anchor exposes the slip: $80 - 8 = 72$ (receipt $72 + 8 = 80$). The pattern catches many errors, never all.",
                 ["Eq(6 + 3, 9)", "Eq(7*9, 63)", "Eq(8*9, 72)"]),
            recap([
                "Sixes = fives + one per group: 7 × 6 = 35 + 7 = 42.",
                "Sevens = fives + twos: 7 × 7 = 35 + 14 = 49.",
                "Eights and nines ride down from the tens: 7 × 9 = 70 − 7, receipt 63 + 7 = 70.",
                "9s pattern: digits add to 9; tens digit is one less than the multiplier.",
                "Patterns are alarms, not answers — anchor with an owned fact first.",
            ]),
            tip("For every fact below, say your building road aloud — \"fives plus\", \"fives and twos\", or \"tens minus\" — before you compute. The road is the answer's receipt."),
            tryitset("Mixed practice", "All four hard tables, built from owned facts.", [
                tp("$7 \\times 7$ equals:",
                   ["$49$", "$42$", "$56$"],
                   "Fives and twos: $35 + 14 = 49$. $42$ is the neighbour $7 \\times 6$; $56$ is the neighbour $7 \\times 8$.",
                   ["Eq(35 + 14, 49)", "Eq(7*7, 49)"]),
                tp("$6 \\times 8$ equals:",
                   ["$48$", "$42$", "$54$"],
                   "Tens road: $6 \\times 10 = 60$, take back $6 \\times 2 = 12$: $60 - 12 = 48$ (receipt $48 + 12 = 60$).",
                   ["Eq(60 - 12, 48)", "Eq(48 + 12, 60)"]),
                tp("$9 \\times 9$ equals:",
                   ["$81$", "$89$", "$72$"],
                   "Nine tens minus nine: $90 - 9 = 81$ (receipt $81 + 9 = 90$), and $8 + 1 = 9$ keeps the guard happy. $89$ fails the digit sum; $72$ belongs to $8 \\times 9$.",
                   ["Eq(90 - 9, 81)", "Eq(81 + 9, 90)"]),
                tp("A wrestler trains $6$ days each week. In $7$ weeks he trains:",
                   ["$42$ days", "$36$ days", "$13$ days"],
                   "Seven groups of six: $7 \\times 6 = 35 + 7 = 42$ days. $36$ is $6 \\times 6$ — a week short; $13$ adds $7 + 6$.",
                   ["Eq(7*6, 42)", "Eq(6*6, 36)"]),
                tp("Which number CANNOT belong to the 9s table: $54$, $72$ or $56$?",
                   ["$56$", "$54$", "$72$"],
                   "Digit sums: $5 + 6 = 11$ — not $9$, so $56$ is out (it is $7 \\times 8$). The others pass and are real: $54 = 6 \\times 9$ and $72 = 8 \\times 9$.",
                   ["Eq(5 + 6, 11)", "Eq(Mod(56, 9), 2)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tables of 6 to 9\"",
                    "Fives plus, fives and twos, tens minus — every hard fact built from a fact you own, with the 9s digits standing guard. Next: a trick that cuts the whole table nearly in half, hiding in plain sight inside any rectangle.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Arrays & the Turnaround Trick
# ==========================================================================

def lesson_arrays_turnaround():
    # the buuz tray: 4 rows of 6, read both ways
    r, c = 4, 6
    fig_rows = fig_groups(*[(c, "row %d" % (i + 1), C_ACCENT) for i in range(r)])
    fig_cols = fig_groups(*[(r, "column %d" % (i + 1), C_WARM) for i in range(c)])
    # tp array: 5 rows of 3
    fig_53 = fig_groups(*[(3, "row %d" % (i + 1), C_GREEN) for i in range(5)])
    return {
        "slug": "arrays-and-turnaround",
        "title": "Arrays & the Turnaround Trick",
        "concreteComparison": (
            "A tray of buuz sits in $4$ rows of $6$. Walk to the side "
            "of the table and look again: the same tray is $6$ columns "
            "of $4$. Nobody moved a single buuz — so $4 \\times 6$ and "
            "$6 \\times 4$ must name the same number, $24$. One "
            "rectangle, two facts: that is the turnaround trick, and "
            "it cuts the times table nearly in half."),
        "objective": (
            "Read an array as rows and as columns to see that the two "
            "readings give one total, use the turnaround a × b = b × a "
            "to get partner facts free, and count how much of the "
            "table is left to memorise."),
        "concept": [
            "**An array is equal groups in a rectangle.** $4$ rows of "
            "$6$ is the fact $4 \\times 6 = 24$ drawn as a neat "
            "rectangle — rows are the groups, and every row has the "
            "same count. That sameness is what makes it an array.",
            "**One array, two readings.** Read the same rectangle as "
            "columns and you get $6$ columns of $4$: $6 \\times 4 = "
            "24$. The buuz never moved, so the two facts MUST agree — "
            "$4 \\times 6 = 6 \\times 4$. Every pair of numbers turns "
            "around like this.",
            "**Turnaround halves the memory work.** Every fact hands "
            "you its partner free: own $2 \\times 9 = 18$ and $9 "
            "\\times 2$ costs nothing. Of the $100$ facts in the "
            "ten-by-ten table, $45$ are turnaround copies — only $55$ "
            "remain, and you already own the 2s, 5s, 10s and 9s rows "
            "AND their columns.",
        ],
        "keyIdea": (
            "An array read as rows and read as columns is the same "
            "count — so a × b = b × a always, every fact has a free "
            "partner, and the table you must memorise is barely half "
            "as big as it looks."),
        "facts": [
            {"title": "One array, two facts",
             "latex": "4 \\times 6 = 6 \\times 4 = 24",
             "explanation": "Rows or columns — the same rectangle counts the same buuz."},
            {"title": "The table, halved",
             "latex": "100 \\text{ facts} = 55 \\text{ to learn} + 45 \\text{ free partners}",
             "explanation": "Every fact off the diagonal has a turnaround twin that costs nothing."},
        ],
        "workedExamples": [
            {"id": "g4tm-l4-we1",
             "statement": "A tray holds $4$ rows of $6$ buuz. Count it as rows and as columns, and write both facts.",
             "note": "Walk around the table between the two counts.",
             "solution": ("Rows: $4$ rows of $6$ gives $4 \\times 6 = 24$. "
                          "Columns: $6$ columns of $4$ gives $6 \\times 4 = 24$. "
                          "Same tray, same $24$ — the two facts are one count "
                          "read two ways."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*6, 24)", "Eq(4*6, 6*4)"]},
            {"id": "g4tm-l4-we2",
             "statement": "You know $2 \\times 9 = 18$. Find $9 \\times 2$ without any new work, and say why that is allowed.",
             "note": "Turnaround: the same array, read the other way.",
             "solution": ("$9 \\times 2 = 18$ immediately: an array of $2$ rows "
                          "of $9$ IS an array of $9$ columns of $2$ — one "
                          "rectangle, one count. The turnaround gives every "
                          "fact's partner free."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*9, 18)", "Eq(9*2, 18)"]},
        ],
        "commonMistakes": [
            {"text": "Counting an array twice — 4 rows of 6 makes 24, \"plus\" 6 columns of 4 makes 48.",
             "correction": "The columns are the SAME buuz seen again, not a second tray. One rectangle, one total: 24. The two facts are two readings, not two amounts.",
             "authored": True},
            {"text": "Hoping turnaround erases all memorising — \"I'll just flip everything\".",
             "correction": "Flipping pairs each fact with a partner, but ONE of each pair must still be learned — and same-number facts like 7 × 7 = 49 are their own partners. Turnaround halves the work; it doesn't finish it.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4tm-l4-t1",
             "statement": "A chocolate bar has $3$ rows of $8$ squares. Write both times facts and the total.",
             "solution": "Rows: $3 \\times 8 = 24$. Columns: $8 \\times 3 = 24$. One bar, $24$ squares, two readings.",
             "check": ["Eq(3*8, 24)", "Eq(8*3, 24)"]},
            {"id": "g4tm-l4-t2",
             "statement": "You know $5 \\times 7 = 35$. What is $7 \\times 5$, and which table's work did the turnaround just save you?",
             "solution": "$7 \\times 5 = 35$, free of charge — a fact from the hard table of $7$, answered by the friendly table of $5$.",
             "check": ["Eq(5*7, 35)", "Eq(7*5, 35)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One rectangle, two facts", [
                "An ARRAY is equal groups drawn as a rectangle. Below: $4$ rows with $6$ in each — the fact $4 \\times 6 = 24$ laid out in neat lines.",
                "Now read the SAME rectangle the other way: $6$ columns with $4$ in each — $6 \\times 4$. Nothing moved, so the answer cannot change: $6 \\times 4 = 24$ too.",
                "That is the turnaround trick: $4 \\times 6 = 6 \\times 4$, and the same holds for ANY two numbers — the rectangle does not care which side you call rows.",
            ]), fig_rows),
            workedset("Rows, then columns",
                      "Two readings of one rectangle must agree.", [
                withfig(wex("Read the tray of $4$ rows of $6$ as COLUMNS.",
                    ["From the side, the same buuz line up as $6$ columns of $4$: $6 \\times 4 = 24$.",
                     "Both readings count the same tray: $4 \\times 6 = 6 \\times 4$."],
                    "$6 \\times 4 = 24$",
                    ["Eq(6*4, 24)", "Eq(4*6, 6*4)"]), fig_cols),
                wex("A chocolate bar has $3$ rows of $8$ squares. Both facts?",
                    ["Rows: $3 \\times 8 = 24$.",
                     "Columns: $8 \\times 3 = 24$ — same bar, same squares."],
                    "$3 \\times 8 = 8 \\times 3 = 24$",
                    ["Eq(3*8, 24)", "Eq(8*3, 24)"]),
            ]),
            tryitset("Two readings", "Rows or columns — one count.", [
                withfig(tp("The array shows $5$ rows of $3$. The two facts it proves are:",
                   ["$5 \\times 3 = 15$ and $3 \\times 5 = 15$",
                    "$5 \\times 3 = 15$ and $3 \\times 5 = 53$",
                    "$5 + 3 = 8$ and $3 + 5 = 8$"],
                   "Rows: $5 \\times 3 = 15$; columns: $3 \\times 5 = 15$. Turnaround partners always share one answer — $53$ just glues digits, and the additions count a different story.",
                   ["Eq(5*3, 15)", "Eq(3*5, 15)"]), fig_53),
                tp("An array with $2$ rows of $9$ has the same total as an array with:",
                   ["$9$ rows of $2$", "$9$ rows of $9$", "$2$ rows of $2$"],
                   "Turn the rectangle: $2 \\times 9 = 9 \\times 2 = 18$. The others are different rectangles entirely: $81$ and $4$.",
                   ["Eq(2*9, 18)", "Eq(9*9, 81)"]),
                tp("The turnaround partner of $8 \\times 4 = 32$ is:",
                   ["$4 \\times 8 = 32$", "$8 \\times 8 = 64$", "$4 \\times 4 = 16$"],
                   "Swap rows for columns, keep the answer: $4 \\times 8 = 32$. The other options change the rectangle itself.",
                   ["Eq(8*4, 32)", "Eq(4*8, 32)"]),
            ]),
            tapq("The tilted window", "A window has $3$ rows of $7$ panes. Tilting your head shows $7$ columns of $3$. What does this PROVE?",
                 ["$3 \\times 7 = 7 \\times 3$ — both count the same $21$ panes",
                  "the window has $21 + 21 = 42$ panes",
                  "$7 \\times 3$ is bigger than $3 \\times 7$",
                  "columns always count more than rows"],
                 "Tilting your head moves no glass: one window, one count — $21$. Reading it twice does not double it; it proves the two facts are one.",
                 ["Eq(3*7, 21)", "Eq(21 + 21, 42)"]),
            funfact("The most famous array in the world",
                    "A chessboard is an $8 \\times 8$ array: $64$ squares. Count it as $8$ rows of $8$ or as $8$ columns of $8$ — the same $64$ either way, and it is its own turnaround partner, because the rectangle is a perfect square."),
            teach("Concept B", "Half the table for free", [
                "The full ten-by-ten table holds $10 \\times 10 = 100$ facts. But every fact off the diagonal has a turnaround twin — $45$ of the $100$ are copies of the other $45$.",
                "So only $55$ facts truly need learning: the $45$ originals plus the $10$ same-number facts ($1 \\times 1$ up to $10 \\times 10$), which are their own partners.",
                "And you own more than you think: the 2s, 5s, 10s and 9s give you their whole ROW of the table — and the turnaround hands you their whole COLUMN free. What remains of the hard middle is a handful.",
            ]),
            workedset("Counting the real work",
                      "Partners share; only one of each pair is new.", [
                wex("How many facts are in the ten-by-ten table, and how many need learning once partners share?",
                    ["Total: $10 \\times 10 = 100$ facts.",
                     "$45$ are turnaround copies: $100 - 45 = 55$ to learn (receipt: $55 + 45 = 100$)."],
                    "$100$ facts; $55$ to learn",
                    ["Eq(10*10, 100)", "Eq(100 - 45, 55)", "Eq(55 + 45, 100)"]),
                wex("Batu must learn $6 \\times 5$, $5 \\times 6$, $9 \\times 6$ and $6 \\times 9$. How many DIFFERENT answers is that?",
                    ["$6 \\times 5 = 5 \\times 6 = 30$ — one pair, one answer.",
                     "$9 \\times 6 = 6 \\times 9 = 54$ — a second pair. Just two answers in all."],
                    "two: $30$ and $54$",
                    ["Eq(6*5, 30)", "Eq(5*6, 30)", "Eq(6*9, 54)"]),
            ]),
            tryitset("Free partners", "Learn one, get one free.", [
                tp("You know $10 \\times 7 = 70$. Free of charge you also know:",
                   ["$7 \\times 10 = 70$", "$7 \\times 7 = 49$", "$10 \\times 10 = 100$"],
                   "The turnaround gives the partner, nothing more: $7 \\times 10 = 70$. The other facts are different rectangles and must be earned separately.",
                   ["Eq(10*7, 70)", "Eq(7*10, 70)"]),
                tp("Which fact is its OWN turnaround partner?",
                   ["$8 \\times 8$", "$8 \\times 2$", "$2 \\times 8$"],
                   "Swapping $8$ and $8$ changes nothing: $8 \\times 8 = 64$ sits on the table's diagonal. The pair $8 \\times 2$ and $2 \\times 8$ are partners of each other, both $16$.",
                   ["Eq(8*8, 64)", "Eq(8*2, 16)"]),
                tp("$4 \\times 9 = 36$. So $9 \\times 4$ equals:",
                   ["$36$", "$63$", "$40$"],
                   "Turnaround keeps the answer: $36$. Writing $63$ reverses the DIGITS, not the fact; $40$ is the neighbour $10 \\times 4$.",
                   ["Eq(4*9, 36)", "Eq(9*4, 36)"]),
            ]),
            tapq("Already learned", "A student says: \"I learned $3 \\times 8 = 24$, but $8 \\times 3$ I have not learned yet.\" The truth:",
                 ["$8 \\times 3$ is the same array read the other way — $24$, already owned",
                  "the two facts can have different answers",
                  "$8 \\times 3$ is bigger because the $8$ comes first",
                  "only the full table can settle it"],
                 "One rectangle, two readings: $3$ rows of $8$ IS $8$ columns of $3$. Learning either fact buys both: $8 \\times 3 = 24$.",
                 ["Eq(3*8, 24)", "Eq(8*3, 24)"]),
            recap([
                "An array is equal groups in a rectangle — rows are groups.",
                "Rows-reading and columns-reading count the same things: a × b = b × a, always.",
                "Every fact hands you its turnaround partner free; same-number facts are their own partners.",
                "Of 100 table facts, only 55 need learning — and the friendly rows bring their columns along.",
            ]),
            tip("Whenever a fact looks hard, turn it around first — $8 \\times 5$ scares nobody who owns $5 \\times 8$. Check yourself: same answer both ways."),
            tryitset("Mixed practice", "Arrays, partners, and the halved table.", [
                tp("A choir stands in $6$ rows of $4$ singers. How many singers?",
                   ["$24$", "$10$", "$46$"],
                   "Six rows of four: $6 \\times 4 = 24$ — or turn it around, $4 \\times 6$, same count. Adding gives $10$; gluing gives $46$.",
                   ["Eq(6*4, 24)", "Eq(6 + 4, 10)"]),
                tp("$7 \\times 6 = 42$. Its turnaround partner says:",
                   ["$6 \\times 7 = 42$", "$6 \\times 7 = 24$", "$7 \\times 7 = 42$"],
                   "Partners swap the numbers and keep the answer: $6 \\times 7 = 42$. Changing the answer, or changing the rectangle to $7 \\times 7 = 49$, is not a turnaround.",
                   ["Eq(6*7, 42)", "Eq(7*7, 49)"]),
                tp("Which pair shows a turnaround, not two different facts?",
                   ["$5 \\times 8$ and $8 \\times 5$",
                    "$5 \\times 8$ and $4 \\times 10$",
                    "$5 \\times 8$ and $5 \\times 9$"],
                   "Turnaround swaps the SAME two numbers: $5 \\times 8 = 8 \\times 5 = 40$. Beware the imposter: $4 \\times 10 = 40$ shares the answer but is a different rectangle — same total, different fact.",
                   ["Eq(5*8, 40)", "Eq(4*10, 40)"]),
                tp("From the pair $7 \\times 9$ and $9 \\times 7$, how many facts must you memorise?",
                   ["one — the other comes free", "two", "none"],
                   "They are one rectangle read two ways, both $63$: learn either and the turnaround hands you the other. Zero would be too generous — someone must learn the first.",
                   ["Eq(7*9, 63)", "Eq(9*7, 63)"]),
                tp("A garden has $8$ rows of $5$ seedlings. Counting by columns instead, Ochir counts:",
                   ["$5$ columns of $8$", "$8$ columns of $5$", "$5$ columns of $5$"],
                   "Rows of $5$ stand in $5$ columns, each $8$ deep: $5 \\times 8 = 40$, agreeing with the rows' $8 \\times 5 = 40$ — as one garden must.",
                   ["Eq(8*5, 40)", "Eq(5*8, 40)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Arrays & the Turnaround Trick\"",
                    "One rectangle, two facts — and a hundred-fact table shrunk to fifty-five. You now hold every times fact to 10, plus the tools to rebuild any that slip. Next: numbers too big for any table, split into pieces the tables can handle.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Multiplying Bigger Numbers
# ==========================================================================

def lesson_bigger_numbers():
    # area model for 23 x 4 = 20 x 4 + 3 x 4, drawn to scale (x0.4, y0.5)
    n_tens, n_ones, mult = 20, 3, 4
    n = n_tens + n_ones
    sx, sy = 0.4, 0.5
    fig_area = fig_geo(
        [P("A", 0, 0, ""), P("B", n_tens * sx, 0, ""), P("C", n * sx, 0, ""),
         P("D", n * sx, mult * sy, ""), P("E", n_tens * sx, mult * sy, ""),
         P("F", 0, mult * sy, "")],
        [seg("A", "B", label="20"), seg("B", "C", label="3"),
         seg("C", "D"), seg("D", "E"), seg("E", "F"),
         seg("F", "A", label="4"),
         seg("B", "E", dashed=True, color=C_WARM),
         ang("A", "B", "F", right=True)],
        height=200)
    # number line: 37 x 5 lands at 150 (tens part) then 185
    t_part, full = 30 * 5, 37 * 5
    fig_jump = fig_numline([(t_part, "30 × 5"), (full, "37 × 5", C_WARM)],
                           lo=0, hi=200)
    return {
        "slug": "multiply-bigger-numbers",
        "title": "Multiplying Bigger Numbers",
        "concreteComparison": (
            "Four boxes each hold $23$ books. No times table reaches "
            "$23$ — but $23$ is just $20$ and $3$, and you own both "
            "pieces: four twenties are $80$, four threes are $12$, "
            "together $92$. Big multiplications are small ones stacked "
            "by place: split the number, multiply the pieces, add them "
            "back."),
        "objective": (
            "Multiply a two-digit number by a one-digit number by "
            "splitting it into tens and ones, keep the tens' place "
            "value honest, and solve simple money and word problems "
            "with a tens fence as the sanity check."),
        "concept": [
            "**Tens numbers multiply by table facts.** $20 \\times 4$ "
            "is $2$ tens taken $4$ times: $8$ tens, which is $80$. The "
            "table fact $2 \\times 4 = 8$ does the work; place value "
            "writes the zero.",
            "**Split by place, multiply each piece.** $23 \\times 4 = "
            "20 \\times 4 + 3 \\times 4 = 80 + 12 = 92$. The $4$ must "
            "visit BOTH pieces — every box holds a twenty and a three, "
            "so both get multiplied. The split is the receipt: if the "
            "pieces do not rebuild the answer, something got lost.",
            "**Fence the answer with tens.** Before trusting $37 "
            "\\times 5$, trap it: it must land between $30 \\times 5 = "
            "150$ and $40 \\times 5 = 200$. The real answer, $150 + 35 "
            "= 185$, sits inside the fence — an answer outside the "
            "fence is wrong on sight.",
        ],
        "keyIdea": (
            "Split the two-digit number by place, multiply each piece "
            "with a table fact you own, and add the pieces back — "
            "with a tens fence around the answer to catch any "
            "escape."),
        "facts": [
            {"title": "Split by place",
             "latex": "23 \\times 4 = 20 \\times 4 + 3 \\times 4 = 80 + 12 = 92",
             "explanation": "The multiplier visits both pieces; the pieces add back to the answer."},
            {"title": "The tens fence",
             "latex": "30 \\times 5 < 37 \\times 5 < 40 \\times 5",
             "explanation": "Every answer must land between its two tens neighbours — escapees are wrong on sight."},
        ],
        "workedExamples": [
            {"id": "g4tm-l5-we1",
             "statement": "Find $23 \\times 4$ by splitting into tens and ones.",
             "note": "The 4 must visit both pieces of the 23.",
             "solution": ("Split: $23 = 20 + 3$. Multiply each piece: $20 \\times "
                          "4 = 80$ and $3 \\times 4 = 12$. Add back: $80 + 12 = "
                          "92$. So $23 \\times 4 = 92$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(23*4, 20*4 + 3*4)", "Eq(20*4, 80)", "Eq(80 + 12, 92)"]},
            {"id": "g4tm-l5-we2",
             "statement": "A pencil costs $85$ togrog. Find the cost of $6$ pencils.",
             "note": "Money splits by place like any other number.",
             "solution": ("$85 = 80 + 5$. Then $80 \\times 6 = 480$ and $5 "
                          "\\times 6 = 30$; together $480 + 30 = 510$. Six "
                          "pencils cost $510$ togrog."),
             "badges": [{"text": "core"}],
             "check": ["Eq(80*6, 480)", "Eq(5*6, 30)", "Eq(480 + 30, 510)"]},
        ],
        "commonMistakes": [
            {"text": "Multiplying only the tens — 23 × 4 = 80.",
             "correction": "The 3 ones ride in every box too: 23 × 4 = 20 × 4 + 3 × 4 = 80 + 12 = 92. If your pieces don't rebuild the number you split, a piece was dropped.",
             "authored": True},
            {"text": "Gluing piece answers side by side — 37 × 5 from pieces \"15\" and \"35\" glued into 1535.",
             "correction": "30 × 5 is 150, not 15 — the tens piece keeps its place value. Then ADD the pieces: 150 + 35 = 185. Gluing digits skips the addition entirely.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4tm-l5-t1",
             "statement": "Find $34 \\times 2$ by the place split.",
             "solution": "$34 = 30 + 4$: then $30 \\times 2 = 60$, $4 \\times 2 = 8$, and $60 + 8 = 68$.",
             "check": ["Eq(30*2, 60)", "Eq(60 + 8, 68)"]},
            {"id": "g4tm-l5-t2",
             "statement": "Find $46 \\times 3$, and check it sits inside its tens fence.",
             "solution": "$40 \\times 3 = 120$ and $6 \\times 3 = 18$: total $138$. Fence: between $40 \\times 3 = 120$ and $50 \\times 3 = 150$ — and $138$ sits inside.",
             "check": ["Eq(40*3, 120)", "Eq(120 + 18, 138)", "138 < 150"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Split by place, then rebuild", [
                "First, tens numbers alone: $20 \\times 4$ is $2$ tens taken $4$ times — $8$ tens, $80$. The table fact $2 \\times 4 = 8$ does the work and place value writes the zero.",
                "Now any two-digit number: split it by place. The rectangle below is $23 \\times 4$ cut into two smaller rectangles — a $20 \\times 4$ piece and a $3 \\times 4$ piece.",
                "Multiply each piece, add them back: $80 + 12 = 92$. The multiplier visits BOTH pieces — every one of the four boxes holds a twenty and a three.",
            ]), fig_area),
            workedset("Two pieces, one answer",
                      "Split, multiply each piece, add back.", [
                wex("Find $23 \\times 4$.",
                    ["Split: $23 = 20 + 3$.",
                     "Pieces: $20 \\times 4 = 80$ and $3 \\times 4 = 12$; together $80 + 12 = 92$."],
                    "$92$",
                    ["Eq(3*4, 12)", "Eq(80 + 12, 92)"]),
                wex("Find $34 \\times 2$.",
                    ["Split: $34 = 30 + 4$.",
                     "$30 \\times 2 = 60$, $4 \\times 2 = 8$: total $68$."],
                    "$68$",
                    ["Eq(30*2, 60)", "Eq(34*2, 68)"]),
            ]),
            tryitset("Split and rebuild", "The multiplier visits both pieces.", [
                tp("$21 \\times 4$ equals:",
                   ["$84$", "$24$", "$81$"],
                   "$20 \\times 4 = 80$ and $1 \\times 4 = 4$: $84$. Answering $24$ multiplies only the ones and the $2$ as a bare digit; $81$ forgets the one entirely and glues.",
                   ["Eq(20*4, 80)", "Eq(80 + 4, 84)"]),
                tp("$32 \\times 3$ equals:",
                   ["$96$", "$36$", "$92$"],
                   "$30 \\times 3 = 90$ and $2 \\times 3 = 6$: $96$. The trap $36$ multiplies only the ones ($2 \\times 3 = 6$) and copies the tens digit $3$ untouched — the $30$ never got multiplied. $92$ multiplies the tens but copies the ones digit $2$ without multiplying it.",
                   ["Eq(30*3, 90)", "Eq(90 + 6, 96)"]),
                tp("The right split for $54 \\times 2$ is:",
                   ["$50 \\times 2 + 4 \\times 2$",
                    "$5 \\times 2 + 4 \\times 2$",
                    "$54 + 2$"],
                   "$54$ is $50$ and $4$ — the tens piece keeps its zero: $100 + 8 = 108$. Splitting into bare digits gives $10 + 8 = 18$, six times too small; $54 + 2 = 56$ adds instead of multiplying.",
                   ["Eq(54*2, 50*2 + 4*2)", "Eq(5*2 + 4*2, 18)"]),
            ]),
            tapq("Why the split works", "Four boxes each hold $23$ books. Why is $23 \\times 4 = 20 \\times 4 + 3 \\times 4$?",
                 ["every box holds a twenty AND a three — the $4$ must multiply both pieces",
                  "because $20 + 3 + 4 = 27$",
                  "the split only works for even numbers",
                  "it changes the answer by a little"],
                 "Each box is a $20$-pile and a $3$-pile: four boxes give four twenties ($80$) and four threes ($12$). Rebuilt: $80 + 12 = 92$ — exactly $23 \\times 4$, no change at all.",
                 ["Eq(23, 20 + 3)", "Eq(23*4, 92)"]),
            funfact("How big can it get?",
                    "The largest two-digit by one-digit multiplication is $99 \\times 9$ — and even that stays under a thousand: $90 \\times 9 = 810$, $9 \\times 9 = 81$, together $891$. Every answer in this lesson fits comfortably inside the numbers you already read and write."),
            withfig(teach("Concept B", "Stories, money, and the tens fence", [
                "Word problems hide the same split. One ticket costs $75$ togrog, five friends ride: $75 \\times 5 = 70 \\times 5 + 5 \\times 5 = 350 + 25 = 375$ togrog.",
                "When the ones piece is big, nothing changes: $37 \\times 5 = 150 + 35 = 185$ — the line below shows the tens piece landing at $150$ and the ones piece jumping the rest.",
                "FENCE every answer with tens: $37 \\times 5$ must land between $30 \\times 5 = 150$ and $40 \\times 5 = 200$. An answer outside its fence — like a glued $1535$ — is wrong on sight.",
            ]), fig_jump),
            workedset("Splits at work",
                      "Find the equal groups in the story, then split.", [
                wex("One bus ticket costs $75$ togrog. What do $5$ tickets cost?",
                    ["Five groups of $75$: split $75$ into $70$ and $5$.",
                     "$70 \\times 5 = 350$, $5 \\times 5 = 25$: $350 + 25 = 375$ togrog."],
                    "$375$ togrog",
                    ["Eq(70*5, 350)", "Eq(350 + 25, 375)"]),
                wex("A jeep drives $48$ km each day of a $3$-day trip. Total distance?",
                    ["$40 \\times 3 = 120$ and $8 \\times 3 = 24$.",
                     "$120 + 24 = 144$ km — inside the fence $120$ to $150$."],
                    "$144$ km",
                    ["Eq(40*3, 120)", "Eq(120 + 24, 144)", "144 < 150"]),
            ]),
            tryitset("Fenced answers", "Split, rebuild, and check the fence.", [
                tp("$29 \\times 3$ equals:",
                   ["$87$", "$627$", "$67$"],
                   "$20 \\times 3 = 60$ and $9 \\times 3 = 27$: $60 + 27 = 87$. Gluing the pieces makes $627$ — far outside the fence $60$ to $90$; $67$ adds only $7$ of the $27$.",
                   ["Eq(60 + 27, 87)", "87 < 90"]),
                tp("A bag holds $64$ candies. How many candies in $4$ bags?",
                   ["$256$", "$68$", "$2416$"],
                   "$60 \\times 4 = 240$ and $4 \\times 4 = 16$: $256$. Adding gives $68$; gluing the pieces gives $2416$, ten times past the fence $240$ to $280$.",
                   ["Eq(240 + 16, 256)", "Eq(64 + 4, 68)"]),
                tp("One notebook costs $95$ togrog. Two notebooks cost:",
                   ["$190$ togrog", "$97$ togrog", "$1810$ togrog"],
                   "$90 \\times 2 = 180$ and $5 \\times 2 = 10$: $190$. Adding gives $97$ — the price of one notebook and a cheap pencil, not two notebooks; $1810$ glues the pieces.",
                   ["Eq(180 + 10, 190)", "Eq(95*2, 190)"]),
            ]),
            tapq("Build the fence first", "Before computing $67 \\times 3$, its tens fence is:",
                 ["between $60 \\times 3 = 180$ and $70 \\times 3 = 210$",
                  "between $6 \\times 3 = 18$ and $7 \\times 3 = 21$",
                  "between $0$ and $100$",
                  "no fence is possible"],
                 "$67$ sits between $60$ and $70$, so $67 \\times 3$ must sit between their triples: $180$ and $210$. It does: $67 \\times 3 = 201$. The digit fence $18$ to $21$ forgot the place value.",
                 ["Eq(60*3, 180)", "Eq(70*3, 210)", "Eq(67*3, 201)"]),
            recap([
                "Tens numbers multiply by table facts: 20 × 4 = 8 tens = 80.",
                "Split by place: 23 × 4 = 20 × 4 + 3 × 4 — the multiplier visits both pieces.",
                "Add the pieces back — never glue their digits side by side.",
                "Fence every answer between its tens neighbours; escapees are wrong on sight.",
            ]),
            tip("For each problem: say the split, build the fence, then compute — and make sure the answer lands inside before you commit."),
            tryitset("Mixed practice", "Splits, stories, and fences.", [
                tp("$43 \\times 2$ equals:",
                   ["$86$", "$45$", "$83$"],
                   "$40 \\times 2 = 80$ and $3 \\times 2 = 6$: $86$. Adding gives $45$; $83$ drops half the ones piece.",
                   ["Eq(40*2, 80)", "Eq(80 + 6, 86)"]),
                tp("$36 \\times 4$ equals:",
                   ["$144$", "$124$", "$1224$"],
                   "$30 \\times 4 = 120$ and $6 \\times 4 = 24$: $144$. $124$ adds only $4$ of the $24$; $1224$ glues the pieces and escapes the fence $120$ to $160$.",
                   ["Eq(120 + 24, 144)", "144 < 160"]),
                tp("A library has $7$ shelves with $52$ books on each. Total books:",
                   ["$364$", "$59$", "$3514$"],
                   "$50 \\times 7 = 350$ and $2 \\times 7 = 14$: $364$. Adding gives $59$; gluing gives $3514$ — the fence $350$ to $420$ rejects it instantly.",
                   ["Eq(350 + 14, 364)", "Eq(52*7, 364)"]),
                tp("A ticket to the wrestling costs $90$ togrog. Five tickets cost:",
                   ["$450$ togrog", "$95$ togrog", "$405$ togrog"],
                   "$90$ is $9$ tens: $9 \\times 5 = 45$ tens, so $450$. Adding gives $95$; $405$ misplaces a ten mid-count.",
                   ["Eq(9*5, 45)", "Eq(90*5, 450)"]),
                tp("The right split for $78 \\times 3$ is:",
                   ["$70 \\times 3 + 8 \\times 3 = 210 + 24$",
                    "$7 \\times 3 + 8 \\times 3 = 21 + 24$",
                    "$78 + 3$"],
                   "$78$ is $70$ and $8$: $210 + 24 = 234$. The bare-digit split gives $21 + 24 = 45$ — the tens piece lost its zero; $78 + 3 = 81$ adds instead of multiplying.",
                   ["Eq(78*3, 70*3 + 8*3)", "Eq(210 + 24, 234)", "Eq(21 + 24, 45)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Multiplying Bigger Numbers\" — and the topic",
                    "Equal groups, the friendly tables, hard facts built from owned ones, the turnaround, and the place split: one idea ran through it all — build the fact you need from a fact you already own. Next year the same split stretches to bigger numbers, and division arrives to run every times fact backwards.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr5 = fig_groups(*[(7, "row %d" % (i + 1), C_ACCENT) for i in range(4)])
    return [
        prob("g4tm-pr1", "A ger camp pitches $5$ gers with $4$ beds in each. Write the repeated addition and the times fact for the total beds.",
             "Five groups of four: $4 + 4 + 4 + 4 + 4 = 20$, so $5 \\times 4 = 20$ beds.",
             ["Eq(4 + 4 + 4 + 4 + 4, 20)", "Eq(5*4, 20)"]),
        prob("g4tm-pr2", "Find $8 \\times 5$ and $8 \\times 10$. What must each answer end in, and how are the two answers related?",
             "$8 \\times 5 = 40$: an even count of fives pairs into whole tens, so it ends in $0$. $8 \\times 10 = 80$: every times-10 answer ends in $0$. And $80$ is double $40$ — a ten is two fives.",
             ["Eq(8*5, 40)", "Eq(Mod(40, 10), 0)", "Eq(2*40, 80)"]),
        prob("g4tm-pr3", "Build $7 \\times 8$ from the tens: $7 \\times 10$ minus $7 \\times 2$.",
             "$7 \\times 10 = 70$ and $7 \\times 2 = 14$: $70 - 14 = 56$ (receipt: $56 + 14 = 70$). So $7 \\times 8 = 56$.",
             ["Eq(70 - 14, 56)", "Eq(56 + 14, 70)", "Eq(7*8, 56)"]),
        prob("g4tm-pr4", "Find $6 \\times 9$, then verify it with both 9s patterns.",
             "Six tens minus six: $60 - 6 = 54$ (receipt: $54 + 6 = 60$). Patterns: the tens digit $5$ is one less than $6$, and $5 + 4 = 9$.",
             ["Eq(60 - 6, 54)", "Eq(54 + 6, 60)", "Eq(5 + 4, 9)"]),
        withprobfig(prob("g4tm-pr5", "The array shows $4$ rows of $7$ stones. Write both times facts it proves.",
             "Rows: $4 \\times 7 = 28$. Columns: $7 \\times 4 = 28$. One rectangle, two readings, one count.",
             ["Eq(4*7, 28)", "Eq(7*4, 28)"]), fig_pr5),
        prob("g4tm-pr6", "Find $57 \\times 3$ by the place split, and give the split as a receipt.",
             "$57 = 50 + 7$: then $50 \\times 3 = 150$ and $7 \\times 3 = 21$, so $57 \\times 3 = 150 + 21 = 171$.",
             ["Eq(50*3, 150)", "Eq(7*3, 21)", "Eq(150 + 21, 171)"]),
        prob("g4tm-pr7", "A copybook costs $65$ togrog. What do $4$ copybooks cost?",
             "Four groups of $65$: $60 \\times 4 = 240$ and $5 \\times 4 = 20$, together $260$ togrog — inside the fence $240$ to $280$.",
             ["Eq(60*4, 240)", "Eq(240 + 20, 260)", "Eq(65*4, 260)"]),
        prob("g4tm-pr8", "Saruul has mastered only the tables of $2$, $5$ and $10$. Show how she can still answer $9 \\times 5$ AND $5 \\times 9$.",
             "$9 \\times 5$ is in her table of $5$: count nine fives — $45$, ending in $5$ since $9$ is odd. The turnaround then hands her $5 \\times 9 = 45$ free: same array, read the other way.",
             ["Eq(9*5, 45)", "Eq(Mod(45, 10), 5)", "Eq(5*9, 45)"]),
    ]


def test_bank():
    return [
        prob("g4tm-x1", "Write $6 \\times 3$ as repeated addition and find it. Then explain why groups of $3$, $3$, $3$ and $4$ have NO single times fact.",
             "$6 \\times 3 = 3 + 3 + 3 + 3 + 3 + 3 = 18$. The four unequal groups total $3 + 3 + 3 + 4 = 13$, but four equal groups of three make only $4 \\times 3 = 12$ — the times sign demands equal groups, and these are not.",
             ["Eq(6*3, 18)", "Eq(3 + 3 + 3 + 4, 13)", "Eq(4*3, 12)", "Ne(13, 12)"]),
        prob("g4tm-x2", "Find $7 \\times 5$, $7 \\times 2$ and $7 \\times 10$, and give each answer's ending check.",
             "$7 \\times 5 = 35$: odd count of fives, ends in $5$. $7 \\times 2 = 7 + 7 = 14$: a double, so even. $7 \\times 10 = 70$: seven whole tens, ends in $0$.",
             ["Eq(7*5, 35)", "Eq(Mod(35, 10), 5)", "Eq(7*2, 14)", "Eq(7*10, 70)"]),
        prob("g4tm-x3", "Build $8 \\times 6$ from $8 \\times 5$, and $8 \\times 9$ from $8 \\times 10$.",
             "$8 \\times 5 = 40$; each of the eight groups grows by one: $40 + 8 = 48 = 8 \\times 6$. And $8 \\times 10 = 80$; one back per group: $80 - 8 = 72 = 8 \\times 9$ (receipt: $72 + 8 = 80$).",
             ["Eq(8*6, 8*5 + 8)", "Eq(40 + 8, 48)",
              "Eq(80 - 8, 72)", "Eq(72 + 8, 80)"]),
        prob("g4tm-x4", "A parade stands in $9$ rows of $6$ marchers. Write both times facts for the total, and say why they must agree.",
             "Rows: $9 \\times 6 = 54$. Columns: $6 \\times 9 = 54$. They must agree because both count the SAME marchers — one rectangle read two ways is the turnaround trick.",
             ["Eq(9*6, 54)", "Eq(6*9, 54)"]),
        prob("g4tm-x5", "Find $74 \\times 6$ by the place split, with the receipt.",
             "$74 = 70 + 4$: then $70 \\times 6 = 420$ and $4 \\times 6 = 24$, so $74 \\times 6 = 420 + 24 = 444$ — inside the fence $420$ to $480$.",
             ["Eq(70*6, 420)", "Eq(420 + 24, 444)", "Eq(74*6, 444)", "444 < 480"]),
        prob("g4tm-x6", "At the school fair a small kite costs $89$ togrog. Find the cost of $7$ kites, and show the tens fence that traps your answer.",
             "$80 \\times 7 = 560$ and $9 \\times 7 = 63$: $560 + 63 = 623$ togrog. Fence: between $80 \\times 7 = 560$ and $90 \\times 7 = 630$ — and $623$ sits inside.",
             ["Eq(80*7, 560)", "Eq(560 + 63, 623)", "Eq(90*7, 630)", "623 < 630"]),
    ]


def main():
    topic = {
        "slug": "times-tables-and-multiplication",
        "title": "Times Tables & Multiplication",
        "grade": 4,
        "status": "published",
        "blurb": ("Equal groups and repeated addition, the times tables to 10 "
                  "with their patterns, arrays and the turnaround trick, and "
                  "multiplying two-digit numbers by one digit."),
        "lessons": [
            lesson_equal_groups(),
            lesson_friendly_tables(),
            lesson_hard_tables(),
            lesson_arrays_turnaround(),
            lesson_bigger_numbers(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "times-tables-and-multiplication.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
