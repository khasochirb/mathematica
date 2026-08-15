#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 8: Data & Graphs.

Collecting data with tallies and organizing it into frequency tables,
reading and drawing pictographs (where a key decides what one symbol is
worth), bar graphs (where the gridline step decides what one square is
worth), line graphs (where the story is change over time), and finally
the two numbers that summarize a whole data set: the mean and the range.

Through-line: READ THE SCALE BEFORE THE SHAPE. Every chart in this topic
encodes numbers with a scale — tallies bundle by five, a pictograph
carries a key, a bar graph counts by its gridline step, a line graph by
its axis. A picture read without its scale is a guess wearing a
uniform, and that single habit is the difference between reading data
and being fooled by it.

Same construction as the other Grade 5 builders: every check is
sympy-asserted with exact integers and Rationals before the JSON is
written. Every total carries its receipt (the parts must re-add to the
whole), every mean is checked back by mean x count = sum.

Run: python3 scripts/grade4/build_data_and_graphs.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (C_ACCENT, C_GREEN, C_NEUTRAL, C_WARM, fig_barchart,  # noqa: E402
                     fig_groups, fig_linegraph, fig_pictograph, withfig,
                     funfact, prob, recap, tapq, teach, tip, tp,
                     tryitset, wex, workedset, write_topic)


# ==========================================================================
# Lesson 1 — Tally Charts & Tables
# ==========================================================================

def lesson_tallies():
    return {
        "slug": "tally-charts-and-tables",
        "title": "Tally Charts & Tables",
        "concreteComparison": (
            "At the gate the herder marks one scratch per sheep as the "
            "flock comes in — but scratches in a long row blur together "
            "and the count is lost. So the fifth scratch is struck "
            "ACROSS the other four, making a little fence of five. Now "
            "the tally reads at a glance: three fences and two more is "
            "seventeen. That is a tally chart, and every graph in this "
            "topic begins as one."),
        "objective": (
            "Record data with tally marks bundled in fives, organize the "
            "counts into a frequency table, and use the total as a "
            "receipt that nothing was lost or double-counted."),
        "concept": [
            "**Tallies bundle by five.** Four uprights, then a fifth "
            "struck across them — one bundle. Reading a tally is "
            "arithmetic, not recounting: $5 \\times \\text{bundles} + "
            "\\text{singles}$, so three bundles and two singles is "
            "$5 \\times 3 + 2 = 17$.",
            "**A frequency table is the fair copy.** One row per "
            "category, one number per row — the FREQUENCY, meaning how "
            "many times that category turned up. Tallies are the field "
            "notes taken while counting; the table is what you show "
            "other people.",
            "**The total is the receipt.** Add every frequency; the sum "
            "must equal how many things you counted altogether. If the "
            "rows say $17 + 12 + 9 = 38$ animals but $39$ came through "
            "the gate, one is missing — and the receipt is what tells "
            "you before the graph does.",
        ],
        "keyIdea": (
            "Tally marks bundle in fives and become a frequency table; "
            "the total is the receipt proving nothing was lost or "
            "counted twice."),
        "facts": [
            {"title": "One bundle",
             "latex": "\\text{4 uprights} + \\text{1 struck across} = 5",
             "explanation": "The fifth stroke lies across the first four, so the eye reads fives instead of scratches."},
            {"title": "Reading a tally",
             "latex": "\\text{count} = 5 \\times \\text{bundles} + \\text{singles}",
             "explanation": "Multiply the bundles, add the leftovers: 3 bundles and 2 singles is 17."},
        ],
        "workedExamples": [
            {"id": "g5da-l1-we1",
             "statement": "A herder's tally for goats shows $4$ full bundles and $3$ singles. How many goats?",
             "note": "Multiply the bundles first.",
             "solution": ("$5 \\times 4 = 20$, plus the $3$ singles: $23$ goats. "
                          "Counting stroke by stroke gives the same $23$ — the "
                          "bundles only make it fast and hard to lose your place."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*4, 20)", "Eq(20 + 3, 23)", "Eq(5*4 + 3, 23)"]},
            {"id": "g5da-l1-we2",
             "statement": "A class survey of favourite Naadam events records wrestling $12$, horse racing $15$, archery $8$. The class has $35$ students and each voted once. Does the table balance?",
             "note": "Add the rows and compare with the class size.",
             "solution": ("$12 + 15 + 8 = 35$, and the class has $35$ students — "
                          "the receipt matches exactly, so no vote is missing and "
                          "none was counted twice."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12 + 15 + 8, 35)"]},
        ],
        "commonMistakes": [
            {"text": "Drawing the fifth tally mark upright, leaving a row of five uprights.",
             "correction": "The fifth stroke goes ACROSS the other four. A row of uprights forces a one-by-one recount — exactly what tallying exists to prevent.",
             "authored": True},
            {"text": "Reporting the number of bundles as the count.",
             "correction": "Each bundle is worth FIVE. Three bundles is 15, not 3 — multiply by five, then add the singles.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5da-l1-t1",
             "statement": "Read this tally: $6$ bundles and $4$ singles.",
             "solution": "$5 \\times 6 = 30$, plus $4$: $34$.",
             "check": ["Eq(5*6 + 4, 34)"]},
            {"id": "g5da-l1-t2",
             "statement": "A bird table records $9$ sparrows, $14$ pigeons and $7$ crows. The watcher says she saw $30$ birds in all. Does the table balance?",
             "solution": "$9 + 14 + 7 = 30$ — it balances, so nothing was lost.",
             "check": ["Eq(9 + 14 + 7, 30)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counting in fives", [
                "A tally records one mark per thing counted — but the fifth mark is struck ACROSS the previous four, making a bundle worth $5$.",
                "Reading is then arithmetic, not recounting: $5 \\times \\text{bundles} + \\text{singles}$. Three bundles and two singles: $5 \\times 3 + 2 = 17$.",
                "This is why tallying survives: your eye counts fives, and losing your place costs one bundle, not the whole flock.",
            ]), fig_groups((5, "bundle of 5", C_ACCENT), (5, "bundle of 5", C_ACCENT), (5, "bundle of 5", C_ACCENT), (2, "2 singles", C_WARM))),
            workedset("Reading bundles",
                      "Multiply the fences, then add what's left over.", [
                wex("$4$ bundles and $3$ singles.",
                    ["$5 \\times 4 = 20$ from the bundles.",
                     "Add the singles: $20 + 3 = 23$."],
                    "$23$",
                    ["Eq(5*4 + 3, 23)"]),
                wex("$7$ bundles and no singles.",
                    ["$5 \\times 7 = 35$.",
                     "No leftovers to add — the count is exactly $35$."],
                    "$35$",
                    ["Eq(5*7, 35)"]),
            ]),
            tryitset("Bundle arithmetic", "Five per bundle, every time.", [
                tp("$6$ bundles and $2$ singles is:",
                   ["$32$", "$8$", "$62$"],
                   "$5 \\times 6 + 2 = 32$. ($8$ counted the marks as ones; $62$ glued the digits together.)",
                   ["Eq(5*6 + 2, 32)"]),
                tp("A tally of $23$ needs how many full bundles?",
                   ["$4$ bundles and $3$ singles", "$5$ bundles and $3$ singles", "$3$ bundles and $8$ singles"],
                   "$23 \\div 5 = 4$ remainder $3$: four bundles, three singles. Check: $5 \\times 4 + 3 = 23$.",
                   ["Eq(5*4 + 3, 23)", "3 < 5"]),
                tp("$9$ bundles and $1$ single is:",
                   ["$46$", "$10$", "$91$"],
                   "$5 \\times 9 + 1 = 46$.",
                   ["Eq(5*9 + 1, 46)"]),
            ]),
            tapq("Bundles, not marks", "A tally shows $8$ bundles and $4$ singles. The count is:",
                 ["$44$", "$12$", "$84$", "$40$"],
                 "$5 \\times 8 = 40$, plus $4$: $44$. Reading the bundles as ones gives $12$ — the commonest tally error there is.",
                 ["Eq(5*8 + 4, 44)", "Ne(44, 12)"]),
            funfact("The oldest data format still in use",
                    "Tally marks are older than writing: notched bones tens of thousands of years old carry them in groups. England's treasury ran on split wooden tally sticks — each debt notched, then split so both halves had to match — until 1826. When the leftover sticks were finally burned in 1834, the furnace set the Houses of Parliament on fire."),
            withfig(teach("Concept B", "The table and its receipt", [
                "A frequency table gives each category one row and one number: how many times it appeared. Tallies are field notes; the table is the fair copy.",
                "The TOTAL row is a receipt. Add every frequency; it must equal the number of things counted altogether.",
                "When the receipt fails, the data is wrong — not the arithmetic. Recount before you graph, because a graph makes a mistake look official.",
            ]), fig_barchart([("sheep", 17, C_ACCENT), ("goats", 12, C_WARM), ("horses", 9, C_GREEN)], step=5, unit="animals")),
            workedset("Balancing a table",
                      "Add the rows and compare with what you counted.", [
                wex("Wrestling $12$, horse racing $15$, archery $8$, in a class of $35$ where everyone voted once.",
                    ["$12 + 15 = 27$, and $27 + 8 = 35$.",
                     "The total matches the class size, so the table balances."],
                    "balanced: $35 = 35$",
                    ["Eq(12 + 15 + 8, 35)"]),
                wex("A ger camp logs $18$, $11$ and $6$ visitors over three days and claims $36$ in all.",
                    ["$18 + 11 + 6 = 35$.",
                     "The claim of $36$ is one too many — the receipt fails, so the log needs checking."],
                    "the total is $35$, not $36$",
                    ["Eq(18 + 11 + 6, 35)", "Ne(35, 36)"]),
            ]),
            tryitset("Receipts", "Add the rows; compare with the claim.", [
                tp("A table shows $14$, $9$ and $12$. Its total is:",
                   ["$35$", "$34$", "$36$"],
                   "$14 + 9 + 12 = 35$.",
                   ["Eq(14 + 9 + 12, 35)"]),
                tp("Four rows total $40$ animals; three of them are $12$, $9$ and $11$. The fourth is:",
                   ["$8$", "$7$", "$9$"],
                   "$40 - 12 - 9 - 11 = 8$. Check: $12 + 9 + 11 + 8 = 40$.",
                   ["Eq(40 - 12 - 9 - 11, 8)", "Eq(12 + 9 + 11 + 8, 40)"]),
                tp("A survey of $30$ students reports $11$, $10$ and $8$. This table:",
                   ["does not balance — it totals $29$", "balances exactly", "totals $31$"],
                   "$11 + 10 + 8 = 29$, one short of $30$: someone's answer is missing.",
                   ["Eq(11 + 10 + 8, 29)", "Ne(29, 30)"]),
            ]),
            tapq("Find the gap", "A herd of $60$ animals is tabled as sheep $27$, goats $19$, horses $9$, camels — how many camels?",
                 ["$5$", "$6$", "$4$", "$15$"],
                 "$60 - 27 - 19 - 9 = 5$. The receipt runs backwards just as well as forwards: a known total minus the known rows gives the missing one.",
                 ["Eq(60 - 27 - 19 - 9, 5)", "Eq(27 + 19 + 9 + 5, 60)"]),
            recap([
                "A tally bundles by five: four uprights and a fifth struck across.",
                "Read a tally as 5 × bundles + singles — never by recounting marks.",
                "A frequency table gives each category a row and a count.",
                "The total is a receipt: the rows must add to what you counted.",
            ]),
            tip("Before you draw anything, add your table's rows and check the total. A graph built on an unbalanced table is a neat picture of a mistake."),
            tryitset("Mixed practice", "Tallies, tables and receipts together.", [
                tp("$5$ bundles and $3$ singles is:",
                   ["$28$", "$8$", "$53$"],
                   "$5 \\times 5 + 3 = 28$.",
                   ["Eq(5*5 + 3, 28)"]),
                tp("$41$ recorded as tallies is:",
                   ["$8$ bundles and $1$ single", "$4$ bundles and $1$ single", "$8$ bundles and $5$ singles"],
                   "$41 \\div 5 = 8$ remainder $1$. Check: $5 \\times 8 + 1 = 41$. (Five singles would have made a ninth bundle.)",
                   ["Eq(5*8 + 1, 41)", "1 < 5"]),
                tp("Rows of $22$, $17$ and $16$ total:",
                   ["$55$", "$45$", "$56$"],
                   "$22 + 17 = 39$, and $39 + 16 = 55$.",
                   ["Eq(22 + 17 + 16, 55)"]),
                tp("A class of $28$ votes once each; three options get $9$, $7$ and $6$. The fourth option got:",
                   ["$6$", "$5$", "$7$"],
                   "$28 - 9 - 7 - 6 = 6$. Two options tie on $6$ — ties are ordinary in data.",
                   ["Eq(28 - 9 - 7 - 6, 6)", "Eq(9 + 7 + 6 + 6, 28)"]),
                tp("Which table CANNOT be right for $50$ counted animals?",
                   ["$20 + 15 + 12$", "$20 + 18 + 12$", "$25 + 15 + 10$"],
                   "$20 + 15 + 12 = 47$, three short of $50$. The other two total exactly $50$.",
                   ["Eq(20 + 15 + 12, 47)", "Ne(47, 50)", "Eq(20 + 18 + 12, 50)", "Eq(25 + 15 + 10, 50)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tally Charts & Tables\"",
                    "Counted in fives, tabled the counts, and proved them with a receipt. Next: turning those numbers into pictures — starting with pictographs, where a single drawn symbol can be worth ten.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Pictographs
# ==========================================================================

def lesson_pictographs():
    return {
        "slug": "pictographs",
        "title": "Pictographs",
        "concreteComparison": (
            "A poster in the school corridor shows rows of little sheep, "
            "one row per class. Class 5A has four sheep and 5B has two — "
            "but the small print at the bottom says each sheep means "
            "$10$ sheep. So the poster is not saying four against two; "
            "it is saying forty against twenty. That small print is the "
            "KEY, and a pictograph without it means nothing at all."),
        "objective": (
            "Read and draw pictographs by using the key, including part "
            "symbols, and compare rows by value rather than by how many "
            "pictures are drawn."),
        "concept": [
            "**The key sets the value of one symbol.** Every pictograph "
            "carries a line like 'one symbol $= 10$'. Reading is "
            "multiplication: $\\text{symbols} \\times \\text{key}$, so "
            "$4$ symbols with a key of $10$ means $40$.",
            "**Part symbols carry part of the key.** Half a symbol is "
            "half the key: with a key of $10$, four and a half symbols "
            "mean $4 \\times 10 + 5 = 45$. A quarter symbol with a key "
            "of $20$ means $5$.",
            "**Drawing runs the multiplication backwards.** To show a "
            "value, divide by the key: $70$ with a key of $10$ needs "
            "$70 \\div 10 = 7$ symbols. Choose a key that makes the "
            "rows short and the parts easy — a key of $10$ turns $35$ "
            "into three and a half symbols, but a key of $4$ would make "
            "an awkward eight and three-quarters.",
        ],
        "keyIdea": (
            "In a pictograph the key says what one symbol is worth: "
            "reading multiplies by the key, drawing divides by it, and "
            "part symbols carry the matching part."),
        "facts": [
            {"title": "Reading a pictograph",
             "latex": "\\text{value} = \\text{symbols} \\times \\text{key}",
             "explanation": "Four symbols with a key of 10 mean 40, not 4."},
            {"title": "Drawing one",
             "latex": "\\text{symbols} = \\text{value} \\div \\text{key}",
             "explanation": "70 with a key of 10 needs 7 symbols; the division picks the picture."},
        ],
        "workedExamples": [
            {"id": "g5da-l2-we1",
             "statement": "A pictograph of visitors uses the key 'one tent $= 20$ visitors'. Monday shows $3$ tents, Tuesday shows $3$ and a half. How many visitors on each day?",
             "note": "Half a symbol is half the key.",
             "solution": ("Monday: $3 \\times 20 = 60$. Tuesday: $3 \\times 20 = 60$ "
                          "plus half of $20$, which is $10$ — so $70$. Tuesday beat "
                          "Monday by $10$ visitors, even though the rows look almost "
                          "identical."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*20, 60)", "Eq(Rational(20,2), 10)", "Eq(3*20 + 10, 70)", "Eq(70 - 60, 10)"]},
            {"id": "g5da-l2-we2",
             "statement": "Draw $45$ books with the key 'one book symbol $= 10$ books'. How many symbols?",
             "note": "Divide by the key; the remainder becomes a part symbol.",
             "solution": ("$45 \\div 10 = 4$ remainder $5$, and $5$ is half of the "
                          "key — so four whole symbols and a half symbol. Check: "
                          "$4 \\times 10 + 5 = 45$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*10 + 5, 45)", "Eq(Rational(10,2), 5)"]},
        ],
        "commonMistakes": [
            {"text": "Counting the symbols and reporting that as the answer.",
             "correction": "Symbols are not the data — the key is. Four symbols with a key of 10 is 40. Read the key line FIRST, every single time.",
             "authored": True},
            {"text": "Treating half a symbol as one whole, or ignoring it.",
             "correction": "Half a symbol is half the key: with a key of 20 it is worth 10. Part symbols exist precisely so the picture can be exact.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5da-l2-t1",
             "statement": "Key: one horse $= 5$ horses. A row shows $6$ horses. What value is that?",
             "solution": "$6 \\times 5 = 30$ horses.",
             "check": ["Eq(6*5, 30)"]},
            {"id": "g5da-l2-t2",
             "statement": "Key: one symbol $= 20$. How would you draw $50$?",
             "solution": "$50 \\div 20 = 2$ remainder $10$, and $10$ is half of $20$: two and a half symbols. Check: $2 \\times 20 + 10 = 50$.",
             "check": ["Eq(2*20 + 10, 50)", "Eq(Rational(20,2), 10)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The key is the whole story", [
                "A pictograph draws data as repeated symbols — and a KEY line says what one symbol is worth: 'one sheep $= 10$ sheep'.",
                "Reading is multiplication: $4$ symbols with a key of $10$ means $4 \\times 10 = 40$. The row of pictures is shorthand, not the number.",
                "Skip the key and every comparison collapses: two rows of $4$ and $2$ symbols might be $40$ against $20$, or $8$ against $4$ — the key decides.",
            ]), fig_pictograph([("5A", 40), ("5B", 20)], 10)),
            workedset("Reading with a key",
                      "Symbols times key, every time.", [
                wex("Key: one tent $= 20$. A row of $3$ tents.",
                    ["$3 \\times 20 = 60$.",
                     "Three pictures, sixty visitors."],
                    "$60$",
                    ["Eq(3*20, 60)"]),
                wex("Key: one book $= 10$. A row of $7$ books.",
                    ["$7 \\times 10 = 70$.",
                     "The row is seven long; the value is seventy."],
                    "$70$",
                    ["Eq(7*10, 70)"]),
            ]),
            tryitset("Multiply by the key", "The picture counts symbols; the key counts data.", [
                tp("Key: one symbol $= 5$. A row of $8$ symbols means:",
                   ["$40$", "$8$", "$13$"],
                   "$8 \\times 5 = 40$. ($8$ ignored the key; $13$ added instead of multiplying.)",
                   ["Eq(8*5, 40)"]),
                tp("Key: one symbol $= 100$. A row of $6$ symbols means:",
                   ["$600$", "$106$", "$60$"],
                   "$6 \\times 100 = 600$.",
                   ["Eq(6*100, 600)"]),
                tp("Two rows show $5$ and $3$ symbols, key $= 20$. The first row beats the second by:",
                   ["$40$", "$2$", "$20$"],
                   "$5 \\times 20 = 100$ and $3 \\times 20 = 60$: the gap is $40$. Counting symbols would have said $2$ — the key multiplies the gap too.",
                   ["Eq(5*20, 100)", "Eq(3*20, 60)", "Eq(100 - 60, 40)"]),
            ]),
            tapq("Small print, big difference", "A row of $4$ symbols sits under the key 'one symbol $= 25$'. The row's value is:",
                 ["$100$", "$4$", "$29$", "$25$"],
                 "$4 \\times 25 = 100$. The drawing is four pictures long; the data is one hundred. That gap between picture and value is the whole point of the key.",
                 ["Eq(4*25, 100)"]),
            funfact("How pictures mislead",
                    "When a designer doubles a symbol to show 'twice as much', they usually double its width AND its height — which multiplies the ink by $2 \\times 2 = 4$. The eye reads area, so a doubling looks like a quadrupling. Honest pictographs repeat one fixed-size symbol instead of growing it, which is exactly why yours should too."),
            withfig(teach("Concept B", "Part symbols, and drawing your own", [
                "Half a symbol carries half the key: with a key of $10$, four and a half symbols mean $4 \\times 10 + 5 = 45$.",
                "Drawing runs the multiplication backwards — divide by the key: $70$ with a key of $10$ needs $70 \\div 10 = 7$ symbols.",
                "Choose the key to fit the data: a key of $10$ turns $35$ into a tidy three and a half symbols, while a key of $1$ would need thirty-five drawings.",
            ]), fig_pictograph([("Class 3", 45), ("Class 4", 70)], 10)),
            workedset("Halves and drawing",
                      "Divide by the key; the leftover becomes a part symbol.", [
                wex("Key $= 20$. A row of $3$ and a half symbols.",
                    ["Whole symbols: $3 \\times 20 = 60$.",
                     "Half a symbol is $20 \\div 2 = 10$; total $60 + 10 = 70$."],
                    "$70$",
                    ["Eq(3*20 + Rational(20,2), 70)"]),
                wex("Draw $45$ with key $= 10$.",
                    ["$45 \\div 10 = 4$ remainder $5$.",
                     "The leftover $5$ is half of $10$: four symbols and a half."],
                    "$4\\frac{1}{2}$ symbols",
                    ["Eq(4*10 + 5, 45)", "Eq(Rational(10,2), 5)"]),
            ]),
            tryitset("Parts of the key", "A part symbol is worth the matching part of the key.", [
                tp("Key $= 10$. Two and a half symbols mean:",
                   ["$25$", "$2.5$", "$20$"],
                   "$2 \\times 10 + 5 = 25$.",
                   ["Eq(2*10 + Rational(10,2), 25)"]),
                tp("Key $= 8$. Half a symbol is worth:",
                   ["$4$", "$8$", "$16$"],
                   "Half of $8$ is $4$.",
                   ["Eq(Rational(8,2), 4)"]),
                tp("Key $= 20$. To draw $90$ you need:",
                   ["$4$ and a half symbols", "$9$ symbols", "$4$ symbols"],
                   "$90 \\div 20 = 4$ remainder $10$, and $10$ is half of $20$. Check: $4 \\times 20 + 10 = 90$.",
                   ["Eq(4*20 + 10, 90)", "Eq(Rational(20,2), 10)"]),
            ]),
            tapq("Choosing a key", "You must show $30$, $45$ and $60$ in a pictograph. The best key is:",
                 ["$15$ — every value lands on a whole or half symbol",
                  "$1$ — one symbol per unit is clearest",
                  "$7$ — the values are close to multiples of seven",
                  "$100$ — big keys keep rows short"],
                 "With key $15$: $30 \\div 15 = 2$, $45 \\div 15 = 3$, $60 \\div 15 = 4$ — short, exact rows. Key $1$ needs $135$ drawings; key $7$ leaves ragged remainders; key $100$ squashes all three into part symbols smaller than a third.",
                 ["Eq(Rational(30,15), 2)", "Eq(Rational(45,15), 3)", "Eq(Rational(60,15), 4)", "Eq(30 + 45 + 60, 135)"]),
            recap([
                "The key says what one symbol is worth — read it first.",
                "Reading: value = symbols × key. Drawing: symbols = value ÷ key.",
                "A part symbol carries the matching part of the key.",
                "A good key makes rows short and leftovers land on neat parts.",
            ]),
            tip("Before answering anything about a pictograph, say the key out loud — 'one symbol is twenty'. Every question after that is multiplication or division."),
            tryitset("Mixed practice", "Reading, comparing and drawing with keys.", [
                tp("Key $= 50$. A row of $3$ symbols means:",
                   ["$150$", "$53$", "$15$"],
                   "$3 \\times 50 = 150$.",
                   ["Eq(3*50, 150)"]),
                tp("Key $= 4$. A row of $6$ and a half symbols means:",
                   ["$26$", "$24$", "$65$"],
                   "$6 \\times 4 = 24$, plus half of $4$ which is $2$: $26$.",
                   ["Eq(6*4 + Rational(4,2), 26)"]),
                tp("Key $= 10$. Rows of $8$ and $5$ symbols differ by:",
                   ["$30$", "$3$", "$13$"],
                   "$80 - 50 = 30$ — the key multiplies the gap as well as the values.",
                   ["Eq(8*10 - 5*10, 30)"]),
                tp("Key $= 25$. To draw $175$ you need:",
                   ["$7$ symbols", "$5$ symbols", "$7$ and a half symbols"],
                   "$175 \\div 25 = 7$ exactly — no part symbol needed.",
                   ["Eq(Rational(175,25), 7)", "Eq(7*25, 175)"]),
                tp("A pictograph has lost its key line. What can you still say?",
                   ["only which row is longest — no actual values",
                    "the exact values, by counting symbols",
                    "nothing at all about the data"],
                   "The ORDER survives: more symbols still means more. But without the key no symbol has a value, so no number can be read off.",
                   ["5 > 3"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Pictographs\"",
                    "One symbol, one key, and multiplication both ways. Next: bar graphs, where the key becomes a scale running up the side — and the gridline step decides what every square is worth.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Bar Graphs
# ==========================================================================

def lesson_bar_graphs():
    return {
        "slug": "bar-graphs",
        "title": "Bar Graphs",
        "concreteComparison": (
            "Four classes race to read the most books, and the results "
            "go up on the wall as four columns. From the door you can "
            "see instantly who won — that is what a bar graph is for. "
            "But to say by HOW MUCH, you have to look at the numbers "
            "climbing the left-hand side and notice what they step by. "
            "Marked every $5$, one square means five books; marked every "
            "$20$, that same square means twenty."),
        "objective": (
            "Read values from a bar graph by using its scale, compare "
            "bars by difference and by multiple, and choose a sensible "
            "scale when drawing one."),
        "concept": [
            "**Bars compare amounts; the axis supplies the numbers.** "
            "The height of each bar is read against the vertical scale. "
            "Gridlines every $5$ mean each gridline is worth $5$ — a "
            "bar reaching the seventh gridline stands at $35$.",
            "**Two ways to compare, and they answer different "
            "questions.** 'How many MORE?' subtracts: $45 - 15 = 30$. "
            "'How many TIMES as many?' divides: $45 \\div 15 = 3$. Read "
            "the question's wording and pick the operation it asks for.",
            "**Drawing means choosing a scale.** Pick a step that makes "
            "the tallest bar fit and the values land on gridlines: for "
            "data of $15$ to $45$, steps of $5$ work well. Bars always "
            "start at zero and keep equal widths, or the picture "
            "exaggerates the differences.",
        ],
        "keyIdea": (
            "A bar graph shows amounts as heights read against a scale; "
            "subtract to compare by how many more, divide to compare by "
            "how many times."),
        "facts": [
            {"title": "Reading a bar",
             "latex": "\\text{value} = \\text{gridlines} \\times \\text{step}",
             "explanation": "Seven gridlines on a scale stepping by 5 is a value of 35."},
            {"title": "Two comparisons",
             "latex": "\\text{how many more} = a - b \\qquad \\text{how many times} = a \\div b",
             "explanation": "45 is 30 more than 15, and 3 times as many as 15 — both true, different questions."},
        ],
        "workedExamples": [
            {"id": "g5da-l3-we1",
             "statement": "Four classes read $35$, $15$, $45$ and $25$ books. How many books altogether, and how many more did the best class read than the worst?",
             "note": "Total by adding; comparison by subtracting.",
             "solution": ("Total: $35 + 15 + 45 + 25 = 120$ books. The tallest bar "
                          "is $45$ and the shortest is $15$, so the gap is "
                          "$45 - 15 = 30$ books."),
             "badges": [{"text": "core"}],
             "check": ["Eq(35 + 15 + 45 + 25, 120)", "Eq(45 - 15, 30)", "45 > 35", "15 < 25"]},
            {"id": "g5da-l3-we2",
             "statement": "In the same graph, how many TIMES as many books did the top class read compared with the bottom class?",
             "note": "'Times as many' divides.",
             "solution": ("$45 \\div 15 = 3$: three times as many. Notice this is a "
                          "different answer from '$30$ more' — both describe the same "
                          "two bars, but they answer different questions."),
             "badges": [{"text": "stretch"}],
             "check": ["Eq(Rational(45,15), 3)", "Eq(3*15, 45)", "Ne(3, 30)"]},
        ],
        "commonMistakes": [
            {"text": "Counting gridlines as ones when the scale steps by 5, 10 or 20.",
             "correction": "Read the numbers on the axis before reading any bar. Seven gridlines on a step-of-5 scale is 35, not 7.",
             "authored": True},
            {"text": "Answering 'how many times as many' by subtracting.",
             "correction": "'More' subtracts; 'times as many' divides. 45 against 15 is both 30 more AND 3 times as many — the wording picks which one is wanted.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5da-l3-t1",
             "statement": "A scale steps by $10$. A bar reaches the fourth gridline. What is its value?",
             "solution": "$4 \\times 10 = 40$.",
             "check": ["Eq(4*10, 40)"]},
            {"id": "g5da-l3-t2",
             "statement": "Bars stand at $24$ and $8$. Answer both: how many more, and how many times as many?",
             "solution": "More: $24 - 8 = 16$. Times: $24 \\div 8 = 3$.",
             "check": ["Eq(24 - 8, 16)", "Eq(Rational(24,8), 3)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The scale decides everything", [
                "A bar graph turns amounts into heights: taller bar, bigger number. Which is largest is visible from across the room.",
                "The numbers come from the vertical scale. If gridlines are marked every $5$, a bar at the seventh gridline stands at $7 \\times 5 = 35$.",
                "Read the scale FIRST. The same drawing with steps of $20$ instead of $5$ would make that bar $140$ — the picture is identical, the data is not.",
            ]), fig_barchart([("wrestling", 20, C_ACCENT), ("archery", 15, C_WARM), ("racing", 25, C_GREEN)], step=5, unit="children")),
            workedset("Reading heights",
                      "Gridlines times step.", [
                wex("Steps of $5$; a bar reaches the seventh gridline.",
                    ["$7 \\times 5 = 35$.",
                     "Seven lines up, thirty-five books."],
                    "$35$",
                    ["Eq(7*5, 35)"]),
                wex("Steps of $20$; a bar sits halfway between the second and third gridlines.",
                    ["The gridlines there are $40$ and $60$.",
                     "Halfway is $(40 + 60) \\div 2 = 50$."],
                    "$50$",
                    ["Eq(2*20, 40)", "Eq(3*20, 60)", "Eq(Rational(40 + 60, 2), 50)"]),
            ]),
            tryitset("Read the axis", "Count gridlines, then multiply by the step.", [
                tp("Steps of $10$; a bar at the sixth gridline is:",
                   ["$60$", "$6$", "$16$"],
                   "$6 \\times 10 = 60$.",
                   ["Eq(6*10, 60)"]),
                tp("Steps of $5$; a bar halfway between $20$ and $25$ is:",
                   ["$22.5$", "$45$", "$23$"],
                   "Halfway between $20$ and $25$ is $22\\frac{1}{2}$ — with a step of $5$, half a square is $2\\frac{1}{2}$.",
                   ["Eq(Rational(20 + 25, 2), Rational(45,2))", "Eq(Rational(5,2), Rational(5,2))"]),
                tp("A bar stands at $80$ on a scale stepping by $20$. It reaches gridline number:",
                   ["$4$", "$8$", "$16$"],
                   "$80 \\div 20 = 4$.",
                   ["Eq(Rational(80,20), 4)"]),
            ]),
            tapq("Same picture, different data", "Two graphs are drawn identically, but one steps by $5$ and the other by $50$. A bar at the third gridline shows:",
                 ["$15$ on the first graph and $150$ on the second",
                  "$15$ on both — the drawing is the same",
                  "$3$ on both",
                  "$150$ on both"],
                 "$3 \\times 5 = 15$ and $3 \\times 50 = 150$. Identical shapes, tenfold different data — which is exactly why the scale is read before the shape.",
                 ["Eq(3*5, 15)", "Eq(3*50, 150)", "Eq(150, 10*15)"]),
            funfact("Who invented the bar chart",
                    "The Scottish engineer William Playfair drew the first bar chart in 1786, to show Scotland's imports and exports when he had no year-by-year figures to plot. He invented the line graph in the same book and the pie chart fifteen years later. Nearly every chart in this topic traces back to one restless man with a printing press."),
            withfig(teach("Concept B", "Comparing, and drawing your own", [
                "'How many MORE?' subtracts: bars of $45$ and $15$ differ by $45 - 15 = 30$.",
                "'How many TIMES as many?' divides: $45 \\div 15 = 3$. Same two bars, different question, different answer.",
                "Drawing: choose a step so the tallest bar fits and values land on gridlines, start every bar at zero, and keep the widths equal.",
            ]), fig_barchart([("Mon", 12, C_ACCENT), ("Tue", 18, C_WARM), ("Wed", 9, C_GREEN), ("Thu", 15, C_NEUTRAL)], step=3, unit="visitors")),
            workedset("Two kinds of comparison",
                      "The wording picks the operation.", [
                wex("Bars of $45$ and $15$: how many more?",
                    ["Subtract: $45 - 15 = 30$.",
                     "The top class read $30$ more books."],
                    "$30$ more",
                    ["Eq(45 - 15, 30)"]),
                wex("The same bars: how many times as many?",
                    ["Divide: $45 \\div 15 = 3$.",
                     "Check by multiplying back: $3 \\times 15 = 45$ ✓."],
                    "$3$ times as many",
                    ["Eq(Rational(45,15), 3)", "Eq(3*15, 45)"]),
            ]),
            tryitset("More, or times?", "Subtract for 'more'; divide for 'times as many'.", [
                tp("Bars of $36$ and $12$: how many times as many?",
                   ["$3$", "$24$", "$48$"],
                   "$36 \\div 12 = 3$. ($24$ answered 'how many more' instead.)",
                   ["Eq(Rational(36,12), 3)", "Eq(36 - 12, 24)"]),
                tp("Bars of $50$ and $35$: how many more?",
                   ["$15$", "$85$", "$10$"],
                   "$50 - 35 = 15$.",
                   ["Eq(50 - 35, 15)"]),
                tp("A bar of $60$ is four times another bar. The other bar is:",
                   ["$15$", "$240$", "$56$"],
                   "$60 \\div 4 = 15$. Check: $4 \\times 15 = 60$.",
                   ["Eq(Rational(60,4), 15)", "Eq(4*15, 60)"]),
            ]),
            tapq("Picking a scale", "Your data runs from $15$ to $45$ in steps of $5$. The best vertical scale is:",
                 ["steps of $5$, up to $50$",
                  "steps of $1$, up to $45$",
                  "steps of $50$, up to $50$",
                  "steps of $7$, up to $49$"],
                 "Steps of $5$ let every value ($15$, $25$, $35$, $45$) land exactly on a gridline, and $50$ leaves room above the tallest bar. Steps of $1$ need $45$ lines; a single step of $50$ squashes every bar below the first line; steps of $7$ put no value on a gridline.",
                 ["Eq(Rational(45,5), 9)", "Eq(Rational(15,5), 3)", "50 > 45"]),
            recap([
                "Bar heights are read against the scale: gridlines × step.",
                "'How many more' subtracts; 'how many times as many' divides.",
                "The same drawing under a different scale is different data.",
                "When drawing: bars from zero, equal widths, values on gridlines.",
            ]),
            tip("Write the step size at the top of your page before answering — 'each square = 5'. Nearly every bar-graph mistake is a scale that was never read."),
            tryitset("Mixed practice", "Reading, comparing and totalling bars.", [
                tp("Steps of $25$; a bar at the third gridline is:",
                   ["$75$", "$3$", "$28$"],
                   "$3 \\times 25 = 75$.",
                   ["Eq(3*25, 75)"]),
                tp("Bars of $35$, $15$, $45$ and $25$ total:",
                   ["$120$", "$110$", "$130$"],
                   "$35 + 15 + 45 + 25 = 120$ books in all.",
                   ["Eq(35 + 15 + 45 + 25, 120)"]),
                tp("The tallest bar is $45$ and the shortest is $15$. Which statement is true?",
                   ["both: it is $30$ more AND $3$ times as many",
                    "only that it is $30$ more",
                    "only that it is $3$ times as many"],
                   "$45 - 15 = 30$ and $45 \\div 15 = 3$ — both are correct descriptions of the same pair of bars.",
                   ["Eq(45 - 15, 30)", "Eq(Rational(45,15), 3)"]),
                tp("A bar of $28$ must be drawn on a scale stepping by $4$. It reaches gridline:",
                   ["$7$", "$4$", "$14$"],
                   "$28 \\div 4 = 7$.",
                   ["Eq(Rational(28,4), 7)"]),
                tp("Two bars look nearly equal, but the scale starts at $90$ instead of $0$. This means:",
                   ["the difference between them is exaggerated by the cut axis",
                    "the difference is hidden by the cut axis",
                    "nothing — where the axis starts does not matter"],
                   "Cutting the bottom off the axis magnifies small gaps: bars of $95$ and $100$ look five times different when only the top $10$ is drawn. Honest bar graphs start at zero.",
                   ["Eq(100 - 95, 5)", "Eq(100 - 90, 10)", "Eq(95 - 90, 5)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Bar Graphs\"",
                    "Heights read against a scale, and two ways to compare them. Next: line graphs, where the horizontal axis becomes time and the picture stops showing amounts and starts showing CHANGE.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Line Graphs
# ==========================================================================

def lesson_line_graphs():
    return {
        "slug": "line-graphs",
        "title": "Line Graphs",
        "concreteComparison": (
            "A sunflower is measured every Sunday and the heights are "
            "dotted onto a grid: week $1$ at $4$ cm, week $2$ at $7$, "
            "week $3$ at $11$. Join the dots and something new appears — "
            "not just how tall, but how FAST. The steep stretch between "
            "weeks $2$ and $3$ is the plant's best week, and you can see "
            "it without doing a single subtraction."),
        "objective": (
            "Read values from a line graph, describe change over time as "
            "rising, falling or level, and identify the steepest stretch "
            "as the fastest change."),
        "concept": [
            "**Time runs along the bottom.** A line graph puts time on "
            "the horizontal axis and the measured quantity up the side. "
            "Each point is one measurement: week $3$, height $11$ cm.",
            "**The line between points shows change.** Rising means "
            "growing, falling means shrinking, and a flat stretch means "
            "no change at all. Steeper means faster: a jump of $4$ cm in "
            "one week is a steeper climb than a jump of $1$ cm.",
            "**Change is subtraction between two readings.** From week "
            "$1$ ($4$ cm) to week $5$ ($12$ cm) the total growth is "
            "$12 - 4 = 8$ cm. Week by week, the growths are $3$, $4$, "
            "$1$ and $0$ — and those four add back to the $8$, which is "
            "the receipt.",
        ],
        "keyIdea": (
            "A line graph shows change over time: read points off both "
            "axes, subtract to measure change between them, and read "
            "steepness as speed of change."),
        "facts": [
            {"title": "Change between readings",
             "latex": "\\text{change} = \\text{later} - \\text{earlier}",
             "explanation": "From 4 cm to 12 cm is a growth of 8 cm."},
            {"title": "What the slope says",
             "latex": "\\text{rising} \\uparrow \\quad \\text{level} \\rightarrow \\quad \\text{falling} \\downarrow",
             "explanation": "Steeper means faster change; flat means no change, not zero height."},
        ],
        "workedExamples": [
            {"id": "g5da-l4-we1",
             "statement": "A sunflower measures $4$, $7$, $11$, $12$, $12$ cm over five weeks. Find the growth in each week, and say which week was fastest.",
             "note": "Each week's growth is a subtraction.",
             "solution": ("Week 1 to 2: $7 - 4 = 3$ cm. Week 2 to 3: $11 - 7 = 4$ cm. "
                          "Week 3 to 4: $12 - 11 = 1$ cm. Week 4 to 5: $12 - 12 = 0$ — "
                          "the plant stopped. The fastest week is the second one at "
                          "$4$ cm, and it is the steepest stretch on the graph."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7 - 4, 3)", "Eq(11 - 7, 4)", "Eq(12 - 11, 1)", "Eq(12 - 12, 0)", "4 > 3", "4 > 1"]},
            {"id": "g5da-l4-we2",
             "statement": "For the same sunflower, find the total growth over the five weeks, and check it against the weekly growths.",
             "note": "Total change is last minus first.",
             "solution": ("Total: $12 - 4 = 8$ cm. Receipt: the weekly growths "
                          "$3 + 4 + 1 + 0 = 8$ ✓ — the steps must always re-add to "
                          "the whole journey."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12 - 4, 8)", "Eq(3 + 4 + 1 + 0, 8)"]},
        ],
        "commonMistakes": [
            {"text": "Reading a flat line as 'zero' rather than 'no change'.",
             "correction": "A flat stretch means the value stayed the same. A sunflower flat at 12 cm is still 12 cm tall — it just stopped growing.",
             "authored": True},
            {"text": "Comparing steepness between two graphs with different scales.",
             "correction": "Steepness only compares fairly INSIDE one graph. Two graphs with different axis steps can show the same change at very different angles.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5da-l4-t1",
             "statement": "A temperature reads $9^\\circ$C at 6 am and $21^\\circ$C at noon. How much did it rise?",
             "solution": "$21 - 9 = 12$ degrees.",
             "check": ["Eq(21 - 9, 12)"]},
            {"id": "g5da-l4-t2",
             "statement": "A line graph runs level from Tuesday to Wednesday at $30$ visitors. How many visitors came on Wednesday?",
             "solution": "$30$ — a level line means the change was $30 - 30 = 0$, so the value stayed at $30$.",
             "check": ["Eq(30 - 30, 0)", "Ne(30, 0)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Time along the bottom", [
                "A line graph puts TIME on the horizontal axis and the measured quantity up the side; each dot is one measurement.",
                "Reading a point uses both axes: across to week $3$, up to $11$ — the sunflower was $11$ cm tall in week three.",
                "Joining the dots is what makes it a line graph: the connecting segments show what happened BETWEEN measurements.",
            ]), fig_linegraph([("Mon", 4), ("Tue", 7), ("Wed", 11), ("Thu", 12), ("Fri", 12)], step=2, unit="cm")),
            workedset("Reading points",
                      "Across for the time, up for the value.", [
                wex("The sunflower graph reads $4, 7, 11, 12, 12$ cm for weeks $1$ to $5$. How tall in week $3$?",
                    ["Across to week $3$, then up to the dot.",
                     "The dot sits at $11$ cm."],
                    "$11$ cm",
                    ["Eq(4 + 3 + 4, 11)", "11 > 7"]),
                wex("In which week did it first pass $10$ cm?",
                    ["Week $2$ is $7$ cm — not yet.",
                     "Week $3$ is $11$ cm, which is above $10$."],
                    "week $3$",
                    ["7 < 10", "11 > 10"]),
            ]),
            tryitset("Point reading", "Both axes, every time.", [
                tp("Heights $4, 7, 11, 12, 12$ for weeks $1$–$5$. The height in week $4$ is:",
                   ["$12$ cm", "$11$ cm", "$4$ cm"],
                   "The fourth reading is $12$ cm — one more than week $3$'s $11$.",
                   ["Eq(11 + 1, 12)", "12 > 11"]),
                tp("A graph of daily visitors reads $20, 25, 30, 15, 10$. The busiest day is day:",
                   ["$3$", "$5$", "$1$"],
                   "$30$ is the largest reading, on day $3$.",
                   ["30 > 25", "30 > 20", "30 > 15", "30 > 10"]),
                tp("Using those visitor numbers, the quietest day had:",
                   ["$10$ visitors", "$0$ visitors", "$15$ visitors"],
                   "The smallest reading is $10$, on day $5$. A low point is not a zero point.",
                   ["10 < 15", "Ne(10, 0)"]),
            ]),
            tapq("Flat is not empty", "A line graph of visitors runs level at $30$ for two days. On the second day the camp had:",
                 ["$30$ visitors — level means unchanged",
                  "$0$ visitors",
                  "$60$ visitors",
                  "no way to tell"],
                 "A flat stretch means the value stayed put. Level at $30$ means $30$ on both days — the line is describing the number, not the change in it.",
                 ["Eq(30 - 30, 0)", "Ne(30, 0)", "Ne(30, 60)"]),
            funfact("The graph that changed a war",
                    "In 1858 Florence Nightingale drew data from the Crimean War as a circular cousin of the bar chart, showing month by month that far more soldiers were dying of preventable disease than of wounds. Officials who had ignored her tables could not ignore the picture, and army sanitation was overhauled. She was elected the first woman member of the Royal Statistical Society."),
            withfig(teach("Concept B", "Change, and how fast", [
                "Change between two readings is subtraction: from $4$ cm to $12$ cm is $12 - 4 = 8$ cm of growth.",
                "Week by week the growths were $3$, $4$, $1$, $0$ — and $3 + 4 + 1 + 0 = 8$, the receipt that the steps re-add to the whole.",
                "Steeper means faster. The $4$ cm week is the steepest stretch; the $0$ cm week is flat. Falling lines are negative change — the value went down.",
            ]), fig_linegraph([("Jan", 8), ("Feb", 14), ("Mar", 20), ("Apr", 15), ("May", 6)], step=4, unit="°C")),
            workedset("Measuring change",
                      "Later minus earlier, then check the steps add up.", [
                wex("Sunflower: $4, 7, 11, 12, 12$. Which week grew fastest?",
                    ["Growths: $3$, $4$, $1$, $0$.",
                     "The largest is $4$ cm — week $2$ to week $3$, the steepest stretch."],
                    "week $2$ to $3$, at $4$ cm",
                    ["Eq(7 - 4, 3)", "Eq(11 - 7, 4)", "Eq(12 - 11, 1)", "4 > 3", "4 > 1"]),
                wex("Total growth across the five weeks, checked two ways.",
                    ["Ends: $12 - 4 = 8$ cm.",
                     "Steps: $3 + 4 + 1 + 0 = 8$ cm — the roads agree ✓."],
                    "$8$ cm",
                    ["Eq(12 - 4, 8)", "Eq(3 + 4 + 1 + 0, 8)"]),
            ]),
            tryitset("Rise and fall", "Subtract to measure; compare to judge speed.", [
                tp("Visitors go $20, 25, 30, 15, 10$. The change from day $3$ to day $4$ is:",
                   ["a fall of $15$", "a rise of $15$", "a fall of $5$"],
                   "$30$ down to $15$: a fall of $15$, the steepest drop on the graph.",
                   ["Eq(30 - 15, 15)", "15 < 30"]),
                tp("Temperature climbs from $9^\\circ$ to $21^\\circ$. The rise is:",
                   ["$12^\\circ$", "$30^\\circ$", "$11^\\circ$"],
                   "$21 - 9 = 12$ degrees.",
                   ["Eq(21 - 9, 12)"]),
                tp("A line rises $2$, then $6$, then $1$. The steepest stretch is the one rising:",
                   ["$6$", "$2$", "$1$"],
                   "$6 > 2 > 1$: the middle stretch climbs fastest, so it is drawn steepest.",
                   ["6 > 2", "6 > 1"]),
            ]),
            tapq("Total change", "Visitors run $20, 25, 30, 15, 10$ across five days. From the first day to the last, the change is:",
                 ["a fall of $10$", "a rise of $10$", "a fall of $20$", "no change"],
                 "First $20$, last $10$: the value fell by $20 - 10 = 10$. The line rose in the middle, but the journey from end to end is downward — total change compares the ENDS.",
                 ["Eq(20 - 10, 10)", "10 < 20"]),
            recap([
                "Time runs along the bottom; each dot is one measurement.",
                "Change between readings is later minus earlier.",
                "Steeper means faster; flat means unchanged, not zero.",
                "Step-by-step changes must re-add to the change between the ends.",
            ]),
            tip("Describe a line graph in words before touching the numbers — 'rose fast, then slowed, then flattened'. The arithmetic afterwards just puts sizes on a story you already know."),
            tryitset("Mixed practice", "Points, change, and steepness together.", [
                tp("Heights $4, 7, 11, 12, 12$. Total growth over the five weeks:",
                   ["$8$ cm", "$12$ cm", "$46$ cm"],
                   "$12 - 4 = 8$ cm. ($12$ is the final height, not the growth; $46$ added all the readings together, which measures nothing.)",
                   ["Eq(12 - 4, 8)", "Eq(4 + 7 + 11 + 12 + 12, 46)"]),
                tp("In which week did that sunflower stop growing?",
                   ["week $5$ — the line runs flat", "week $1$", "it never stopped"],
                   "$12 - 12 = 0$: no change from week $4$ to week $5$, drawn as a flat stretch.",
                   ["Eq(12 - 12, 0)"]),
                tp("A shop's sales fall from $80$ to $65$. The change is:",
                   ["a fall of $15$", "a fall of $25$", "a rise of $15$"],
                   "$80 - 65 = 15$, and the later reading is smaller, so it is a fall.",
                   ["Eq(80 - 65, 15)", "65 < 80"]),
                tp("Two stretches rise by $9$ and by $3$. The first is drawn:",
                   ["three times as steep", "three times as long", "flatter"],
                   "$9 \\div 3 = 3$: over the same time span, three times the rise is three times the steepness.",
                   ["Eq(Rational(9,3), 3)"]),
                tp("Which question can a line graph of daily temperature answer that a bar graph of the same numbers answers less well?",
                   ["when the temperature was rising fastest",
                    "which day was hottest",
                    "what the temperature was on Tuesday"],
                   "All three numbers are readable from either chart, but the LINE draws the change itself — the steepest segment is visible instantly, while separate bars leave you to compare heights in your head.",
                   ["Eq(21 - 9, 12)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Line Graphs\"",
                    "Points, change, and steepness as speed. One lesson remains in Grade 5: squeezing a whole data set down to two honest numbers — the mean and the range.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Mean & Range
# ==========================================================================

def lesson_mean_and_range():
    return {
        "slug": "mean-and-range",
        "title": "Mean & Range",
        "concreteComparison": (
            "Four friends bring $12$, $15$, $9$ and $16$ sweets to a "
            "picnic and decide to share fairly. They pour everything "
            "into one pile — $52$ sweets — and deal it back out four "
            "ways: $13$ each. Nobody actually arrived with $13$, and "
            "that is fine: the MEAN is the level everyone would have if "
            "the pile were flattened. The RANGE, meanwhile, remembers "
            "the argument: from $9$ up to $16$ is a spread of $7$."),
        "objective": (
            "Find the mean of a data set by sharing the total equally, "
            "check it by multiplying back, and find the range as the "
            "spread between largest and smallest."),
        "concept": [
            "**The mean is the fair share.** Add every value, then "
            "divide by how many there are: $12 + 15 + 9 + 16 = 52$ and "
            "$52 \\div 4 = 13$. On a bar graph it is the level the bars "
            "would sit at if you scraped the tall ones into the short "
            "ones.",
            "**Check the mean by multiplying back.** If the mean is "
            "right, then $\\text{mean} \\times \\text{count}$ returns "
            "the total: $13 \\times 4 = 52$ ✓. This receipt catches a "
            "miscounted divisor faster than anything else.",
            "**The range measures spread, not centre.** Largest minus "
            "smallest: $16 - 9 = 7$. Two data sets can share a mean and "
            "have completely different ranges — $13, 13, 13, 13$ and "
            "$9, 12, 15, 16$ both average $13$, but one is identical "
            "throughout and the other is spread over $7$.",
        ],
        "keyIdea": (
            "The mean is the total shared equally (and mean × count "
            "returns the total); the range is largest minus smallest, "
            "describing spread rather than centre."),
        "facts": [
            {"title": "The mean",
             "latex": "\\text{mean} = \\dfrac{\\text{total}}{\\text{how many}}",
             "explanation": "52 sweets among 4 friends is a mean of 13 each."},
            {"title": "The range",
             "latex": "\\text{range} = \\text{largest} - \\text{smallest}",
             "explanation": "From 9 to 16 is a spread of 7 — it says nothing about the middle."},
        ],
        "workedExamples": [
            {"id": "g5da-l5-we1",
             "statement": "Find the mean and the range of $12$, $15$, $9$, $16$.",
             "note": "Total, then share; largest minus smallest.",
             "solution": ("Total: $12 + 15 + 9 + 16 = 52$. Mean: $52 \\div 4 = 13$. "
                          "Check: $13 \\times 4 = 52$ ✓. Range: the largest is $16$ "
                          "and the smallest $9$, so $16 - 9 = 7$. Notice that no "
                          "friend brought exactly $13$ — a mean need not be one of "
                          "the values."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12 + 15 + 9 + 16, 52)", "Eq(Rational(52,4), 13)", "Eq(13*4, 52)",
                       "Eq(16 - 9, 7)", "Ne(13, 12)", "Ne(13, 15)", "Ne(13, 9)", "Ne(13, 16)"]},
            {"id": "g5da-l5-we2",
             "statement": "A camp records $20$, $25$, $30$, $15$ and $10$ visitors over five days. Find the mean daily number, and the range.",
             "note": "Five values means dividing by five.",
             "solution": ("Total: $20 + 25 + 30 + 15 + 10 = 100$. Mean: "
                          "$100 \\div 5 = 20$ visitors a day. Check: $20 \\times 5 = "
                          "100$ ✓. Range: $30 - 10 = 20$. Here the mean happens to "
                          "equal one of the readings — allowed, but a coincidence, "
                          "not a rule."),
             "badges": [{"text": "core"}],
             "check": ["Eq(20 + 25 + 30 + 15 + 10, 100)", "Eq(Rational(100,5), 20)",
                       "Eq(20*5, 100)", "Eq(30 - 10, 20)"]},
        ],
        "commonMistakes": [
            {"text": "Dividing by the wrong count — often by the number of categories rather than the number of values.",
             "correction": "Count the values you actually added. Then check: mean × count must return the total. That receipt catches the wrong divisor immediately.",
             "authored": True},
            {"text": "Believing the mean must be one of the data values.",
             "correction": "It need not be. 12, 15, 9, 16 has mean 13 even though nobody brought 13 — the mean is a level, not a member of the list.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5da-l5-t1",
             "statement": "Find the mean of $8$, $10$, $6$ and $16$.",
             "solution": "$8 + 10 + 6 + 16 = 40$, and $40 \\div 4 = 10$. Check: $10 \\times 4 = 40$ ✓.",
             "check": ["Eq(8 + 10 + 6 + 16, 40)", "Eq(Rational(40,4), 10)", "Eq(10*4, 40)"]},
            {"id": "g5da-l5-t2",
             "statement": "Find the range of $34$, $19$, $28$ and $41$.",
             "solution": "Largest $41$, smallest $19$: $41 - 19 = 22$.",
             "check": ["Eq(41 - 19, 22)", "41 > 34", "19 < 28"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The mean is the fair share", [
                "Pour every value into one pile, then deal it back out equally: $12 + 15 + 9 + 16 = 52$ sweets among $4$ friends is $13$ each.",
                "That is the MEAN — the level the bars would sit at if the tall ones were scraped into the short ones.",
                "The mean need not be one of the values. Nobody brought $13$ sweets, yet $13$ is exactly the fair share.",
            ]), fig_groups((11, "Bat", C_ACCENT), (16, "Suvd", C_WARM), (12, "Nomin", C_GREEN))),
            workedset("Sharing the pile",
                      "Add everything, divide by how many.", [
                wex("Mean of $12$, $15$, $9$, $16$.",
                    ["Total: $12 + 15 + 9 + 16 = 52$.",
                     "Share among $4$: $52 \\div 4 = 13$."],
                    "$13$",
                    ["Eq(12 + 15 + 9 + 16, 52)", "Eq(Rational(52,4), 13)"]),
                wex("Mean of $20$, $25$, $30$, $15$, $10$.",
                    ["Total: $100$.",
                     "Five values: $100 \\div 5 = 20$."],
                    "$20$",
                    ["Eq(20 + 25 + 30 + 15 + 10, 100)", "Eq(Rational(100,5), 20)"]),
            ]),
            tryitset("Fair shares", "Total first, then divide by the count.", [
                tp("The mean of $6$, $8$ and $10$ is:",
                   ["$8$", "$24$", "$10$"],
                   "$6 + 8 + 10 = 24$, and $24 \\div 3 = 8$.",
                   ["Eq(6 + 8 + 10, 24)", "Eq(Rational(24,3), 8)"]),
                tp("The mean of $5$, $5$, $5$ and $5$ is:",
                   ["$5$", "$20$", "$4$"],
                   "$20 \\div 4 = 5$ — when every value is the same, the fair share IS that value.",
                   ["Eq(Rational(5 + 5 + 5 + 5, 4), 5)"]),
                tp("Four numbers total $36$. Their mean is:",
                   ["$9$", "$36$", "$4$"],
                   "$36 \\div 4 = 9$. You never needed the individual numbers — only the total and the count.",
                   ["Eq(Rational(36,4), 9)"]),
            ]),
            tapq("Multiply back", "Six children have a mean of $7$ books each. Altogether they have:",
                 ["$42$ books", "$13$ books", "$7$ books", "$6$ books"],
                 "The receipt runs backwards: $\\text{mean} \\times \\text{count} = 7 \\times 6 = 42$. Any mean you find should pass this check.",
                 ["Eq(7*6, 42)", "Eq(Rational(42,6), 7)"]),
            funfact("Nobody has 2.4 children",
                    "Family sizes are often reported as a mean — 'the average family has $2.4$ children' — yet no family anywhere contains four tenths of a child. A mean is a balance point, not a person. It is the most useful number in statistics and the one most often mistaken for a description of somebody real."),
            withfig(teach("Concept B", "The range measures spread", [
                "The RANGE is largest minus smallest: from $9$ to $16$ is $16 - 9 = 7$. It describes how spread out the data is, not where its centre sits.",
                "Mean and range are independent. $13, 13, 13, 13$ and $9, 12, 15, 16$ both have mean $13$, but ranges of $0$ and $7$.",
                "So report both: the mean says what level, the range says how much the values disagree with each other.",
            ]), fig_barchart([("lowest", 6, C_NEUTRAL), ("highest", 21, C_ACCENT)], step=3, unit="marks")),
            workedset("Spread, and why it is separate",
                      "Largest minus smallest — the middle plays no part.", [
                wex("Range of $12$, $15$, $9$, $16$.",
                    ["Largest $16$, smallest $9$.",
                     "$16 - 9 = 7$."],
                    "$7$",
                    ["Eq(16 - 9, 7)", "16 > 15", "9 < 12"]),
                wex("Two sets: $13, 13, 13, 13$ and $9, 12, 15, 16$. Compare their means and ranges.",
                    ["Means: $52 \\div 4 = 13$ for both.",
                     "Ranges: $13 - 13 = 0$ against $16 - 9 = 7$ — same level, very different agreement."],
                    "same mean $13$; ranges $0$ and $7$",
                    ["Eq(Rational(13 + 13 + 13 + 13, 4), 13)", "Eq(Rational(9 + 12 + 15 + 16, 4), 13)",
                     "Eq(13 - 13, 0)", "Eq(16 - 9, 7)"]),
            ]),
            tryitset("Measuring spread", "Only the two extremes matter.", [
                tp("The range of $34$, $19$, $28$, $41$ is:",
                   ["$22$", "$41$", "$13$"],
                   "$41 - 19 = 22$.",
                   ["Eq(41 - 19, 22)"]),
                tp("A set has range $0$. This means:",
                   ["every value is the same", "every value is zero", "there is only one value"],
                   "Largest minus smallest is $0$ only when largest equals smallest — so all the values are identical, whatever that value is.",
                   ["Eq(7 - 7, 0)", "Ne(7, 0)"]),
                tp("Daily temperatures peak at $27^\\circ$ and bottom out at $13^\\circ$. The range is:",
                   ["$14^\\circ$", "$40^\\circ$", "$20^\\circ$"],
                   "$27 - 13 = 14$ degrees.",
                   ["Eq(27 - 13, 14)"]),
            ]),
            tapq("Same mean, different spread", "Two shops both average $20$ sales a day. Shop A ranges $19$ to $21$; shop B ranges $2$ to $38$. What do the ranges tell you?",
                 ["shop A is steady while shop B swings wildly",
                  "shop A sells more overall",
                  "shop B sells more overall",
                  "nothing — the means are equal, so the shops are the same"],
                 "Equal means say the LEVELS match; the ranges say how reliable those levels are. $21 - 19 = 2$ against $38 - 2 = 36$: same average, completely different day-to-day life.",
                 ["Eq(21 - 19, 2)", "Eq(38 - 2, 36)", "36 > 2"]),
            recap([
                "Mean = total ÷ how many — the fair share, the levelled bar height.",
                "Check every mean by multiplying back: mean × count = total.",
                "A mean need not be one of the data values.",
                "Range = largest − smallest; it measures spread, not centre.",
            ]),
            tip("Always report a mean with its range. On its own, an average hides whether the data agreed or argued — and that is usually the more interesting half of the story."),
            tryitset("Mixed practice", "Means, receipts and ranges together.", [
                tp("The mean of $8$, $10$, $6$, $16$ is:",
                   ["$10$", "$40$", "$8$"],
                   "$8 + 10 + 6 + 16 = 40$, and $40 \\div 4 = 10$. Check: $10 \\times 4 = 40$ ✓.",
                   ["Eq(8 + 10 + 6 + 16, 40)", "Eq(Rational(40,4), 10)", "Eq(10*4, 40)"]),
                tp("Five tests have a mean of $12$. The total of the marks is:",
                   ["$60$", "$17$", "$12$"],
                   "$12 \\times 5 = 60$ — the multiply-back receipt used as the whole method.",
                   ["Eq(12*5, 60)"]),
                tp("The range of $50$, $22$, $37$, $22$ is:",
                   ["$28$", "$50$", "$15$"],
                   "$50 - 22 = 28$. Repeated values change nothing — only the extremes count.",
                   ["Eq(50 - 22, 28)"]),
                tp("Three numbers have mean $10$; two of them are $7$ and $11$. The third is:",
                   ["$12$", "$10$", "$9$"],
                   "The total must be $10 \\times 3 = 30$; so far $7 + 11 = 18$, leaving $30 - 18 = 12$.",
                   ["Eq(10*3, 30)", "Eq(7 + 11, 18)", "Eq(30 - 18, 12)", "Eq(Rational(7 + 11 + 12, 3), 10)"]),
                tp("Adding a value of $30$ to the set $10$, $12$, $14$ will:",
                   ["raise the mean and raise the range",
                    "raise the mean but leave the range unchanged",
                    "leave the mean unchanged"],
                   "Old mean $36 \\div 3 = 12$; new mean $66 \\div 4 = 16\\frac{1}{2}$ — higher. Old range $14 - 10 = 4$; new range $30 - 10 = 20$ — also higher. A value far outside the set pulls both.",
                   ["Eq(Rational(10 + 12 + 14, 3), 12)", "Eq(Rational(10 + 12 + 14 + 30, 4), Rational(33,2))",
                    "Rational(33,2) > 12", "Eq(14 - 10, 4)", "Eq(30 - 10, 20)", "20 > 4"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Mean & Range\" — and all of Grade 5",
                    "Tallies became tables, tables became pictures, and pictures became two honest numbers. That closes the Grade 5 year: place value, the four operations, fractions, decimals, measurement, geometry, and data. Everything from here — ratios, percentages, integers, algebra — is built on exactly these foundations.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5da-pr1", "A tally shows $7$ bundles and $2$ singles. How many were counted?",
             "$5 \\times 7 = 35$, plus $2$: $37$.",
             ["Eq(5*7 + 2, 37)"]),
        prob("g5da-pr2", "A survey of $45$ students records $16$, $13$ and $11$ votes. Does the table balance? If not, how many are missing?",
             "$16 + 13 + 11 = 40$, which is $45 - 40 = 5$ short: five students' answers are missing.",
             ["Eq(16 + 13 + 11, 40)", "Eq(45 - 40, 5)", "Ne(40, 45)"]),
        prob("g5da-pr3", "A pictograph uses the key 'one symbol $= 20$'. One row shows $4$ symbols and another shows $2$ and a half. Find both values and their difference.",
             "$4 \\times 20 = 80$; $2 \\times 20 + 10 = 50$. Difference $80 - 50 = 30$.",
             ["Eq(4*20, 80)", "Eq(2*20 + Rational(20,2), 50)", "Eq(80 - 50, 30)"]),
        prob("g5da-pr4", "A bar graph's scale steps by $25$. One bar reaches the fourth gridline and another the sixth. Find both values and how many more the taller one shows.",
             "$4 \\times 25 = 100$ and $6 \\times 25 = 150$; the taller shows $150 - 100 = 50$ more.",
             ["Eq(4*25, 100)", "Eq(6*25, 150)", "Eq(150 - 100, 50)"]),
        prob("g5da-pr5", "Bars stand at $48$ and $16$. Answer both questions: how many more, and how many times as many?",
             "More: $48 - 16 = 32$. Times: $48 \\div 16 = 3$, checked by $3 \\times 16 = 48$.",
             ["Eq(48 - 16, 32)", "Eq(Rational(48,16), 3)", "Eq(3*16, 48)"]),
        prob("g5da-pr6", "A plant measures $5$, $9$, $14$, $16$ cm over four weeks. Find each week's growth, the total growth, and the fastest week.",
             "Growths $4$, $5$, $2$; total $16 - 5 = 11$ cm, and $4 + 5 + 2 = 11$ ✓. The fastest week is the second, at $5$ cm.",
             ["Eq(9 - 5, 4)", "Eq(14 - 9, 5)", "Eq(16 - 14, 2)", "Eq(16 - 5, 11)", "Eq(4 + 5 + 2, 11)", "5 > 4", "5 > 2"]),
        prob("g5da-pr7", "Find the mean and the range of $14$, $9$, $17$, $12$.",
             "Total $52$; mean $52 \\div 4 = 13$ (check $13 \\times 4 = 52$ ✓). Range $17 - 9 = 8$.",
             ["Eq(14 + 9 + 17 + 12, 52)", "Eq(Rational(52,4), 13)", "Eq(13*4, 52)", "Eq(17 - 9, 8)"]),
        prob("g5da-pr8", "Four days of visitors have a mean of $18$. Three of the days had $14$, $20$ and $19$. How many came on the fourth day?",
             "Total must be $18 \\times 4 = 72$; so far $14 + 20 + 19 = 53$, leaving $72 - 53 = 19$.",
             ["Eq(18*4, 72)", "Eq(14 + 20 + 19, 53)", "Eq(72 - 53, 19)", "Eq(Rational(14 + 20 + 19 + 19, 4), 18)"]),
    ]


def test_bank():
    return [
        prob("g5da-x1", "A herd of $80$ animals is tabled as sheep $34$, goats $26$, horses $12$ and camels. Find the camels, and check the receipt.",
             "$80 - 34 - 26 - 12 = 8$ camels. Check: $34 + 26 + 12 + 8 = 80$ ✓.",
             ["Eq(80 - 34 - 26 - 12, 8)", "Eq(34 + 26 + 12 + 8, 80)"]),
        prob("g5da-x2", "A pictograph must show $60$, $90$ and $150$ with as few symbols as possible while keeping every row a whole number of symbols. Give a key that works and the resulting rows.",
             "A key of $30$: rows of $2$, $3$ and $5$ symbols, since $60 \\div 30 = 2$, $90 \\div 30 = 3$ and $150 \\div 30 = 5$.",
             ["Eq(Rational(60,30), 2)", "Eq(Rational(90,30), 3)", "Eq(Rational(150,30), 5)"]),
        prob("g5da-x3", "On a bar graph stepping by $10$, one bar reaches the ninth gridline and another sits halfway between the third and fourth. Find both values.",
             "$9 \\times 10 = 90$; halfway between $30$ and $40$ is $(30 + 40) \\div 2 = 35$.",
             ["Eq(9*10, 90)", "Eq(Rational(30 + 40, 2), 35)"]),
        prob("g5da-x4", "A line graph of daily sales reads $40$, $55$, $55$, $30$. Describe each stretch in words and give the total change from first day to last.",
             "Rose by $15$, ran level ($55 - 55 = 0$), then fell by $25$. From end to end: $40 - 30 = 10$, a fall of $10$.",
             ["Eq(55 - 40, 15)", "Eq(55 - 55, 0)", "Eq(55 - 30, 25)", "Eq(40 - 30, 10)"]),
        prob("g5da-x5", "Two classes both have a mean score of $15$. Class A's scores range from $14$ to $16$; class B's from $5$ to $25$. What does that tell you, and what are the two ranges?",
             "Ranges: $16 - 14 = 2$ and $25 - 5 = 20$. Same average level, but class A's scores agree closely while class B's are spread ten times as widely — the mean alone would have hidden that.",
             ["Eq(16 - 14, 2)", "Eq(25 - 5, 20)", "Eq(20, 10*2)"]),
        prob("g5da-x6", ("A camp tables five days of visitors: $22$, $18$, $25$, $15$ and one unreadable day. "
                         "The week's total is known to be $100$. Find the missing day, the mean, and the range."),
             "Missing: $100 - 22 - 18 - 25 - 15 = 20$. Mean: $100 \\div 5 = 20$ (check $20 \\times 5 = 100$ ✓). Range: $25 - 15 = 10$.",
             ["Eq(100 - 22 - 18 - 25 - 15, 20)", "Eq(Rational(100,5), 20)", "Eq(20*5, 100)", "Eq(25 - 15, 10)"]),
    ]


def main():
    topic = {
        "slug": "data-and-graphs",
        "title": "Data & Graphs",
        "grade": 5,
        "status": "published",
        "blurb": ("Tally charts and frequency tables, pictographs with a "
                  "key, bar graphs and their scales, line graphs of change "
                  "over time, and summarizing a whole data set with the "
                  "mean and the range."),
        "lessons": [
            lesson_tallies(),
            lesson_pictographs(),
            lesson_bar_graphs(),
            lesson_line_graphs(),
            lesson_mean_and_range(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "data-and-graphs.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
