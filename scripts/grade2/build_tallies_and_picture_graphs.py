#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Tallies & Picture Graphs.

Counting with tally marks bundled in fives; collecting the tallies into a
table with a total; drawing a picture graph where one picture stands for
one thing; drawing a block graph on the same one-for-one footing; and
reading answers — most, fewest, how many more, how many altogether —
straight off the picture.

Through-line: A GRAPH IS A COUNT YOU CAN SEE. Tallies make counting
reliable, a table makes the counts comparable, a picture graph makes the
comparison visible, and every question you can ask of the data is
answered by counting or comparing what is drawn.

Grade discipline: EVERY representation is one-for-one — one tally mark
per thing, one picture per thing, one block per thing. Keys where a
symbol stands for 2, 5 or 10, and bar charts with a scale, are Grade
4's; introducing them here would hide the counting behind a second
calculation. Nothing above 1000; every check is sympy-asserted BEFORE
the JSON is written, and every figure is built from the same counts the
statement quotes.

Run: python3 scripts/grade2/build_tallies_and_picture_graphs.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, withprobfig, workedset,
                     write_topic, fig_groups, C_ACCENT, C_WARM, C_GREEN)


def counts(*rows):
    """A one-for-one picture or block graph: each row is (label, count).
    The figure is built from the SAME counts the statement quotes, so the
    drawing and the words cannot disagree."""
    assert rows, "counts: no rows"
    palette = [C_ACCENT, C_WARM, C_GREEN]
    out = []
    for i, (label, n) in enumerate(rows):
        assert 0 <= n <= 20, "counts: %r out of drawable range" % (n,)
        out.append((n, "%s: %d" % (label, n), palette[i % len(palette)]))
    return fig_groups(*out)


def tally(n, label="count"):
    """Tally marks drawn as bundles of five plus singles — the picture of
    how the count was actually made."""
    assert 0 <= n <= 20, "tally: %r out of drawable range" % (n,)
    bundles, singles = divmod(n, 5)
    rows = []
    for i in range(bundles):
        rows.append((5, "bundle %d" % (i + 1), C_ACCENT))
    if singles:
        rows.append((singles, "%s: %d single" % (label, singles), C_WARM))
    if not rows:
        rows.append((0, "%s: none" % label, C_WARM))
    return fig_groups(*rows)


# ==========================================================================
# Lesson 1 — Tally Marks
# ==========================================================================

def lesson_tallies():
    fig_t7 = tally(7, "sheep")
    fig_t12 = tally(12, "goats")
    fig_t5 = tally(5, "horses")
    return {
        "slug": "tally-marks",
        "title": "Tally Marks",
        "concreteComparison": (
            "Counting a flock as it comes through the gate is hard — the "
            "animals do not wait while you remember where you were. A "
            "tally solves it: one mark per animal, and every fifth mark "
            "laid across the last four to close a bundle."),
        "objective": (
            "Record a count with tally marks bundled in fives, read a "
            "tally back as a number, and say why the bundles make "
            "counting reliable."),
        "concept": [
            "**One mark for each thing.** A tally records as you go, so "
            "you never have to hold the running total in your head. That "
            "is what makes it work while the sheep are still moving.",
            "**Every fifth mark closes a bundle.** Four upright marks, "
            "then the fifth laid across them. Bundles of five can be "
            "counted in fives instead of ones, so a long tally is read "
            "quickly and without losing your place.",
            "**Read it as fives and singles.** Two bundles and two "
            "singles is $2 \\times 5 + 2 = 12$. Count the bundles first, "
            "then add the leftovers — and there can never be five "
            "leftovers, because the fifth would have closed a new bundle.",
        ],
        "keyIdea": (
            "A tally records one mark per thing and closes a bundle every "
            "fifth mark, so the count can be read back in fives."),
        "facts": [
            {"title": "Reading a tally",
             "latex": "2 \\times 5 + 2 = 12",
             "explanation": "Two bundles of five and two singles make twelve."},
            {"title": "Never five singles",
             "latex": "5 - 5 = 0",
             "explanation": "A fifth single would close a bundle, so at most four are ever left over."},
        ],
        "workedExamples": [
            {"id": "g3da-l1-we1",
             "statement": "A tally shows one bundle of five and two singles. What is the count?",
             "note": "Bundles first, then the singles.",
             "solution": ("One bundle is $1 \\times 5 = 5$, and two singles add "
                          "$2$: the count is $5 + 2 = 7$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1*5, 5)", "Eq(5 + 2, 7)"]},
            {"id": "g3da-l1-we2",
             "statement": "Draw $12$ as tally marks. How many bundles and how many singles?",
             "note": "How many fives fit into twelve?",
             "solution": ("Two whole bundles use $2 \\times 5 = 10$ marks, "
                          "leaving $12 - 10 = 2$ singles. So the tally is two "
                          "bundles and two singles — and $2$ is less than $5$, "
                          "as it must be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*5, 10)", "Eq(12 - 10, 2)", "2 < 5"]},
        ],
        "commonMistakes": [
            {"text": "Leaving five singles standing instead of closing a bundle.",
             "correction": "The fifth mark goes ACROSS the other four and closes the bundle. If you can see five uprights, one of them should have been laid across.",
             "authored": True},
            {"text": "Counting the bundles as the answer — reading two bundles and two singles as 4.",
             "correction": "Each bundle is worth five, not one: 2 × 5 + 2 = 12. Counting bundles alone throws away four fifths of the count.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3da-l1-t1",
             "statement": "A tally shows three bundles and one single. What is the count?",
             "solution": ("$3 \\times 5 = 15$ from the bundles, plus $1$ single: "
                          "$15 + 1 = 16$."),
             "check": ["Eq(3*5, 15)", "Eq(15 + 1, 16)"]},
            {"id": "g3da-l1-t2",
             "statement": "Draw $9$ as tally marks and say how many singles are left over.",
             "solution": ("One bundle uses $5$ marks, leaving $9 - 5 = 4$ "
                          "singles. Four is the most that can ever be left, "
                          "since a fifth would close another bundle."),
             "check": ["Eq(9 - 5, 4)", "4 < 5"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One mark, one animal", [
                "Counting a moving flock in your head fails, because the animals do not wait. A tally records instead: one mark for each animal as it passes.",
                "The picture below shows a tally of $7$ sheep — one closed bundle of five, and two more standing on their own.",
                "The fifth mark of every bundle is laid ACROSS the other four. That is what turns a long row of marks into something you can read at a glance.",
            ]), fig_t7),
            workedset("Read the tally", "Count the bundles, then the singles.", [
                wex("One bundle and two singles. What is the count?",
                    ["One bundle is $1 \\times 5 = 5$.",
                     "Two singles add $2$: the count is $5 + 2 = 7$."],
                    "$7$",
                    ["Eq(1*5, 5)", "Eq(5 + 2, 7)"]),
                wex("Three bundles and one single. What is the count?",
                    ["Three bundles: $3 \\times 5 = 15$.",
                     "One single: $15 + 1 = 16$."],
                    "$16$",
                    ["Eq(3*5, 15)", "Eq(15 + 1, 16)"]),
            ]),
            tryitset("What does the tally say?", "Bundles are worth five each.", [
                withfig(tp("The tally below shows:",
                   ["$12$", "$3$", "$7$"],
                   "Two bundles are $2 \\times 5 = 10$, plus two singles: $10 + 2 = 12$. Counting the bundles and singles as one each would give only $4$.",
                   ["Eq(2*5, 10)", "Eq(10 + 2, 12)"]), fig_t12),
                tp("Two bundles and four singles is:",
                   ["$14$", "$6$", "$24$"],
                   "$2 \\times 5 = 10$ from the bundles, plus $4$: $10 + 4 = 14$. Four singles is the most there can ever be.",
                   ["Eq(2*5, 10)", "Eq(10 + 4, 14)", "4 < 5"]),
                tp("A tally of one bundle and no singles is:",
                   ["$5$", "$1$", "$0$"],
                   "A closed bundle is worth five marks: $1 \\times 5 = 5$.",
                   ["Eq(1*5, 5)", "Eq(5 - 5, 0)"]),
            ]),
            withfig(tapq("Why bundle at all?", "What do the bundles of five make easier?",
                 ["reading a long tally back quickly",
                  "drawing the marks more neatly",
                  "using fewer marks altogether",
                  "nothing — they are just decoration"],
                 "The marks are the same either way, but bundles can be counted in fives: $1 \\times 5 = 5$, then add the singles. Reading two bundles and two singles as $10 + 2 = 12$ is far faster and safer than counting twelve separate strokes.",
                 ["Eq(1*5, 5)", "Eq(2*5, 10)", "Eq(10 + 2, 12)"]), fig_t5),
            funfact("Tallies are older than writing",
                    "Notched bones tens of thousands of years old carry marks grouped in small bundles — the same idea you have just used, from before anyone had numerals to write down. Whoever cut them had worked out that counting things one at a time is unreliable, and that grouping fixes it."),
            withfig(teach("Concept B", "Drawing a tally from a number", [
                "Going the other way, from a number to a tally, asks how many whole bundles of five fit inside it.",
                "For $12$: two bundles use $2 \\times 5 = 10$ marks, and $12 - 10 = 2$ are left as singles — exactly what the picture below shows.",
                "There can never be five singles. The fifth would be laid across the other four and become a bundle, so the leftovers are always $0$, $1$, $2$, $3$ or $4$.",
            ]), fig_t12),
            workedset("Draw the tally",
                      "How many fives fit, and what is left?", [
                wex("Draw $12$ as tally marks.",
                    ["Two bundles: $2 \\times 5 = 10$ marks.",
                     "Left over: $12 - 10 = 2$ singles.",
                     "Two bundles and two singles — and $2 < 5$ ✓."],
                    "two bundles, two singles",
                    ["Eq(2*5, 10)", "Eq(12 - 10, 2)", "2 < 5"]),
                wex("Draw $9$ as tally marks.",
                    ["One bundle uses $5$ marks.",
                     "Left over: $9 - 5 = 4$ singles — the most possible."],
                    "one bundle, four singles",
                    ["Eq(9 - 5, 4)", "4 < 5"]),
            ]),
            tryitset("From number to tally", "Fill whole bundles first.", [
                tp("$17$ as tally marks is:",
                   ["three bundles and two singles",
                    "two bundles and seven singles",
                    "seventeen singles"],
                   "$3 \\times 5 = 15$, leaving $17 - 15 = 2$ singles. Seven singles could never stand — five of them would have closed another bundle.",
                   ["Eq(3*5, 15)", "Eq(17 - 15, 2)", "2 < 5"]),
                tp("The most singles a tally can ever show is:",
                   ["$4$", "$5$", "$9$"],
                   "A fifth single is laid across the other four and closes a bundle, so at most four stand alone: $5 - 5 = 0$ left standing.",
                   ["Eq(5 - 5, 0)", "4 < 5"]),
                tp("$10$ as tally marks is:",
                   ["two bundles and no singles",
                    "one bundle and five singles",
                    "ten bundles"],
                   "$2 \\times 5 = 10$ exactly, so both bundles close and nothing is left: $10 - 10 = 0$ singles.",
                   ["Eq(2*5, 10)", "Eq(10 - 10, 0)"]),
            ]),
            tapq("The impossible tally", "A tally shows one bundle and five singles. What is wrong?",
                 ["the fifth single should have closed a second bundle",
                  "nothing — it shows $10$",
                  "there should be no singles at all",
                  "bundles cannot be drawn beside singles"],
                 "The fifth mark is always laid across the other four, so five singles can never stand: at most four do. The count is $1 \\times 5 + 5 = 10$, which should have been drawn as two closed bundles.",
                 ["Eq(1*5 + 5, 10)", "Eq(2*5, 10)", "4 < 5"]),
            recap([
                "A tally records one mark per thing, as you go.",
                "Every fifth mark is laid across the other four to close a bundle.",
                "Read a tally as bundles then singles: $2 \\times 5 + 2 = 12$.",
                "There are never five singles — at most four are left standing.",
            ]),
            tip("When reading a tally, touch each bundle and count \"five, ten, fifteen\" out loud before you add the singles. Counting the bundles in ones is the mistake that costs four fifths of the answer."),
            tryitset("Chapter practice", "Bundles of five, then the leftovers.", [
                tp("Four bundles and three singles is:",
                   ["$23$", "$7$", "$43$"],
                   "$4 \\times 5 = 20$ from the bundles, plus $3$: $20 + 3 = 23$.",
                   ["Eq(4*5, 20)", "Eq(20 + 3, 23)"]),
                tp("$8$ as tally marks is:",
                   ["one bundle and three singles",
                    "eight bundles", "two bundles and three singles"],
                   "One bundle uses $5$, leaving $8 - 5 = 3$ singles.",
                   ["Eq(8 - 5, 3)", "3 < 5"]),
                tp("A tally of three bundles and no singles is:",
                   ["$15$", "$3$", "$8$"],
                   "$3 \\times 5 = 15$. Counting the bundles as one each gives $3$ — the classic error.",
                   ["Eq(3*5, 15)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tally Marks\"",
                    "You can now record a count that is happening too fast to hold in your head. The next lesson collects several of those counts side by side, where they can finally be compared.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Making a Table
# ==========================================================================

def lesson_tables():
    fig_table = counts(("sheep", 7), ("goats", 12), ("horses", 5))
    fig_total = counts(("sheep", 7), ("goats", 12))
    return {
        "slug": "making-a-table",
        "title": "Making a Table",
        "concreteComparison": (
            "Three tallies scattered across a page tell you three things "
            "separately. Put them in a table, one row each, and a fourth "
            "thing appears that no single tally could show — which is the "
            "biggest."),
        "objective": (
            "Collect several counts into a table, find the total, and use "
            "the total as a check on the individual counts."),
        "concept": [
            "**A table gives each count its own row.** Sheep $7$, goats "
            "$12$, horses $5$. Written in a column, the counts line up "
            "and can be compared at a glance — which no scattered tally "
            "can do.",
            "**The total is the sum of the rows.** $7 + 12 + 5 = 24$ "
            "animals altogether. It is worth writing down even when "
            "nobody asked for it, because it is a check on everything "
            "above it.",
            "**A missing row can be found from the total.** If the total "
            "is $24$ and two rows read $7$ and $12$, the third must be "
            "$24 - 19 = 5$. The total and the rows hold each other "
            "honest.",
        ],
        "keyIdea": (
            "A table lines counts up so they can be compared, and its "
            "total is both a summary and a check."),
        "facts": [
            {"title": "The total",
             "latex": "7 + 12 + 5 = 24",
             "explanation": "The rows add to the total number of animals."},
            {"title": "A missing row",
             "latex": "24 - 19 = 5",
             "explanation": "Total minus the known rows gives the one that is missing."},
        ],
        "workedExamples": [
            {"id": "g3da-l2-we1",
             "statement": "A herder counts $7$ sheep, $12$ goats and $5$ horses. Make the table and find the total.",
             "note": "One row per kind, then add.",
             "solution": ("Three rows: sheep $7$, goats $12$, horses $5$. The "
                          "total is $7 + 12 + 5 = 24$ animals. Lined up like "
                          "that, it is immediately clear that goats are the most "
                          "numerous, which the three separate tallies never "
                          "showed."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7 + 12 + 5, 24)", "12 > 7", "12 > 5"]},
            {"id": "g3da-l2-we2",
             "statement": "A table shows sheep $7$, goats $12$ and a smudged third row. The total is $24$. What was the third row?",
             "note": "Use the total.",
             "solution": ("The two readable rows come to $7 + 12 = 19$, and the "
                          "total is $24$, so the missing row is "
                          "$24 - 19 = 5$. Check: $19 + 5 = 24$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7 + 12, 19)", "Eq(24 - 19, 5)", "Eq(19 + 5, 24)"]},
        ],
        "commonMistakes": [
            {"text": "Writing the counts down without a total, so nothing can be checked afterwards.",
             "correction": "The total is the table's receipt. Without it, a wrong row can sit there forever; with it, the rows and the total have to agree.",
             "authored": True},
            {"text": "Adding the total into itself when finding a missing row.",
             "correction": "The total is not a row. Add only the rows — 7 + 12 = 19 — and subtract that from the total: 24 − 19 = 5.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3da-l2-t1",
             "statement": "A table reads red $6$, blue $9$, green $4$. Find the total and say which colour is most common.",
             "solution": ("$6 + 9 + 4 = 19$ altogether. Blue is the most common "
                          "at $9$, ahead of red by $9 - 6 = 3$."),
             "check": ["Eq(6 + 9 + 4, 19)", "9 > 6", "Eq(9 - 6, 3)"]},
            {"id": "g3da-l2-t2",
             "statement": "A table has rows of $8$ and $6$, and a total of $20$. What is the missing row?",
             "solution": ("The known rows come to $8 + 6 = 14$, so the missing "
                          "one is $20 - 14 = 6$. Check: $14 + 6 = 20$ ✓."),
             "check": ["Eq(8 + 6, 14)", "Eq(20 - 14, 6)", "Eq(14 + 6, 20)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counts side by side", [
                "Three tallies on three corners of a page tell you three separate things. Bring them into a table — one row each — and they line up.",
                "The picture below shows the three counts together: sheep $7$, goats $12$, horses $5$.",
                "Now a new fact is visible that no single tally could show: goats are the most numerous, beating the sheep by $12 - 7 = 5$. Comparison is what a table is FOR.",
            ]), fig_table),
            workedset("Build the table", "One row per kind, lined up.", [
                wex("Sheep $7$, goats $12$, horses $5$. Which is the most numerous, and by how much over the sheep?",
                    ["Lined up, the largest row is the goats at $12$.",
                     "Over the sheep: $12 - 7 = 5$ more."],
                    "goats, by $5$",
                    ["12 > 7", "Eq(12 - 7, 5)"]),
                wex("Red $6$, blue $9$, green $4$. Which is fewest, and by how much under the blue?",
                    ["The smallest row is green at $4$.",
                     "Under the blue: $9 - 4 = 5$ fewer."],
                    "green, by $5$",
                    ["4 < 9", "Eq(9 - 4, 5)"]),
            ]),
            tryitset("Read the table", "Compare the rows against each other.", [
                tp("Sheep $7$, goats $12$, horses $5$. The most numerous is:",
                   ["goats", "sheep", "horses"],
                   "$12$ is the largest of the three rows, ahead of the sheep by $12 - 7 = 5$ and the horses by $12 - 5 = 7$.",
                   ["12 > 7", "Eq(12 - 7, 5)", "Eq(12 - 5, 7)"]),
                tp("With rows of $6$, $9$ and $4$, how many more of the largest than the smallest?",
                   ["$5$", "$19$", "$3$"],
                   "Largest $9$, smallest $4$: $9 - 4 = 5$ more. The $19$ is the total of all three, a different question.",
                   ["Eq(9 - 4, 5)", "Eq(6 + 9 + 4, 19)"]),
                tp("The row with the SMALLEST count in sheep $7$, goats $12$, horses $5$ is:",
                   ["horses", "sheep", "goats"],
                   "$5$ is the smallest of the three, below the sheep by $7 - 5 = 2$.",
                   ["5 < 7", "Eq(7 - 5, 2)"]),
            ]),
            tapq("What a table adds", "What can a table show that three separate tallies cannot?",
                 ["which count is the biggest",
                  "how each count was made",
                  "the exact number in each count",
                  "nothing — it is the same information"],
                 "Each tally already gives its own number. What the table adds is COMPARISON: lined up, $12 > 7 > 5$ is visible at a glance, and the gap $12 - 7 = 5$ can be read off directly.",
                 ["12 > 7", "7 > 5", "Eq(12 - 7, 5)"]),
            funfact("Why the total goes at the bottom",
                    "Accountants have written the total under the column for centuries, and the reason is checking rather than tidiness: to verify the work you add the column again and see whether you land on the same number. A total sitting at the bottom is an invitation to check, and that is exactly what it is for."),
            withfig(teach("Concept B", "The total, and the missing row", [
                "Every table deserves a total. For sheep $7$ and goats $12$ — the picture below — the two rows come to $7 + 12 = 19$.",
                "Add the horses and the whole table totals $7 + 12 + 5 = 24$ animals. Write it down even when nobody asked: it is the table's receipt.",
                "And it works backwards. If the total is $24$ and one row is smudged, the missing count is $24 - 19 = 5$. The rows and the total keep each other honest.",
            ]), fig_total),
            workedset("Total and missing rows", "Rows add to the total; the total finds a row.", [
                wex("Sheep $7$, goats $12$, horses $5$. What is the total?",
                    ["Add the rows: $7 + 12 = 19$, then $19 + 5 = 24$.",
                     "The table totals $24$ animals."],
                    "$24$",
                    ["Eq(7 + 12, 19)", "Eq(19 + 5, 24)"]),
                wex("Rows of $7$ and $12$, total $24$. What is the missing row?",
                    ["Known rows: $7 + 12 = 19$.",
                     "Missing: $24 - 19 = 5$; check $19 + 5 = 24$ ✓."],
                    "$5$",
                    ["Eq(7 + 12, 19)", "Eq(24 - 19, 5)", "Eq(19 + 5, 24)"]),
            ]),
            tryitset("Totals and gaps", "Add the rows; subtract to find one.", [
                tp("Rows of $6$, $9$ and $4$ total:",
                   ["$19$", "$15$", "$9$"],
                   "$6 + 9 = 15$, then $15 + 4 = 19$. Stopping at $15$ leaves the green row out.",
                   ["Eq(6 + 9, 15)", "Eq(15 + 4, 19)"]),
                tp("Two rows read $8$ and $6$, and the total is $20$. The missing row is:",
                   ["$6$", "$14$", "$34$"],
                   "$8 + 6 = 14$, so the missing row is $20 - 14 = 6$. The $14$ is the two known rows, not the missing one.",
                   ["Eq(8 + 6, 14)", "Eq(20 - 14, 6)", "Eq(14 + 6, 20)"]),
                tp("A table's rows add to $22$ but the written total says $24$. This means:",
                   ["something is wrong — they must agree",
                    "the total is always bigger",
                    "two rows were counted twice"],
                   "The rows and the total have to match; a gap of $24 - 22 = 2$ means a row or the total is wrong. That is exactly why the total is worth writing down.",
                   ["Eq(24 - 22, 2)", "Ne(22, 24)"]),
            ]),
            tapq("Using the total backwards", "A table has rows of $9$ and $7$ and a total of $20$. The missing row is:",
                 ["$4$", "$16$", "$36$", "$20$"],
                 "The known rows come to $9 + 7 = 16$, so the missing one is $20 - 16 = 4$. Check: $16 + 4 = 20$ ✓ — the $16$ is what is already accounted for, not what is missing.",
                 ["Eq(9 + 7, 16)", "Eq(20 - 16, 4)", "Eq(16 + 4, 20)"]),
            recap([
                "A table gives each count its own row so the counts can be compared.",
                "The total is the sum of the rows: $7 + 12 + 5 = 24$.",
                "Write the total down even when nobody asks — it is the table's check.",
                "A missing row is the total minus the rows you have: $24 - 19 = 5$.",
            ]),
            tip("Add your table's rows twice, the second time from the bottom up. Two agreeing totals is far stronger evidence than one, and it costs a few seconds."),
            tryitset("Chapter practice", "Rows, total, and the gap between rows.", [
                tp("Rows of $5$, $8$ and $3$ total:",
                   ["$16$", "$13$", "$11$"],
                   "$5 + 8 = 13$, then $13 + 3 = 16$.",
                   ["Eq(5 + 8, 13)", "Eq(13 + 3, 16)"]),
                tp("In rows of $5$, $8$ and $3$, the largest beats the smallest by:",
                   ["$5$", "$16$", "$3$"],
                   "$8 - 3 = 5$. The $16$ is the total of all three rows.",
                   ["Eq(8 - 3, 5)", "Eq(5 + 8 + 3, 16)"]),
                tp("Rows of $10$ and $6$ with a total of $21$ leave a missing row of:",
                   ["$5$", "$16$", "$37$"],
                   "$10 + 6 = 16$, so the missing row is $21 - 16 = 5$; check $16 + 5 = 21$ ✓.",
                   ["Eq(10 + 6, 16)", "Eq(21 - 16, 5)", "Eq(16 + 5, 21)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Making a Table\"",
                    "A table makes counts comparable, but you still have to read the numbers to compare them. The next lesson draws them instead — and the comparison becomes something you can see without reading at all.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Picture Graphs
# ==========================================================================

def lesson_pictographs():
    fig_pict = counts(("horse", 6), ("sheep", 4), ("camel", 3))
    fig_row = counts(("Monday", 5), ("Tuesday", 8))
    return {
        "slug": "picture-graphs",
        "title": "Picture Graphs",
        "concreteComparison": (
            "A table says goats $12$, sheep $7$. A picture graph draws "
            "twelve little goats and seven little sheep — and now nobody "
            "has to read a number to see which row is longer. The "
            "comparison has become a length."),
        "objective": (
            "Read a picture graph where one picture stands for one thing, "
            "draw one from a table, and answer comparison questions from "
            "the rows."),
        "concept": [
            "**One picture stands for one thing.** Six horses drawn means "
            "six horses counted. Every row has one picture per animal, "
            "which is what makes the row lengths honest.",
            "**Longer rows mean bigger counts.** The horse row at $6$ is "
            "longer than the sheep row at $4$, so there are $6 - 4 = 2$ "
            "more horses. You can see it before you count it, which is "
            "the point of drawing the data at all.",
            "**Every row must start in the same place.** If one row "
            "begins further along than another, its length lies about its "
            "count. Line the rows up at the left and the picture tells "
            "the truth.",
        ],
        "keyIdea": (
            "In a picture graph one picture is one thing, so the length "
            "of a row IS its count — provided every row starts from the "
            "same line."),
        "facts": [
            {"title": "One for one",
             "latex": "6 - 4 = 2",
             "explanation": "Six horses against four sheep: two more, and the row is two longer."},
            {"title": "Rows total the whole",
             "latex": "6 + 4 + 3 = 13",
             "explanation": "Adding the rows gives the total number of animals drawn."},
        ],
        "workedExamples": [
            {"id": "g3da-l3-we1",
             "statement": "A picture graph shows $6$ horses, $4$ sheep and $3$ camels, one picture each. How many more horses than sheep, and how many animals altogether?",
             "note": "Compare the rows, then add them.",
             "solution": ("Horses beat sheep by $6 - 4 = 2$. Altogether the "
                          "rows come to $6 + 4 + 3 = 13$ animals. The horse row "
                          "is the longest, which is visible without counting a "
                          "single picture."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6 - 4, 2)", "Eq(6 + 4 + 3, 13)", "6 > 4"]},
            {"id": "g3da-l3-we2",
             "statement": "Monday $5$ and Tuesday $8$ are drawn one picture per visitor. Which row is longer, and by how much?",
             "note": "One picture per visitor means the row length is the count.",
             "solution": ("Tuesday's row is longer, because $8 > 5$. It is "
                          "$8 - 5 = 3$ pictures longer, which is exactly $3$ "
                          "more visitors — one picture, one visitor."),
             "badges": [{"text": "core"}],
             "check": ["8 > 5", "Eq(8 - 5, 3)", "Eq(5 + 3, 8)"]},
        ],
        "commonMistakes": [
            {"text": "Reading a row's length as its count when the rows do not start in line.",
             "correction": "A row that begins further along looks longer than it is. Every row must start from the same left-hand line, or the picture misleads even though every count is right.",
             "authored": True},
            {"text": "Answering \"how many more\" with the bigger row's count instead of the difference.",
             "correction": "\"How many more horses than sheep\" asks for the gap: 6 − 4 = 2, not 6. The bigger count answers a different question.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3da-l3-t1",
             "statement": "A picture graph shows $7$ birds and $3$ fish. How many more birds, and how many creatures altogether?",
             "solution": ("More birds: $7 - 3 = 4$. Altogether: "
                          "$7 + 3 = 10$ creatures."),
             "check": ["Eq(7 - 3, 4)", "Eq(7 + 3, 10)"]},
            {"id": "g3da-l3-t2",
             "statement": "Why must every row of a picture graph start from the same line?",
             "solution": ("Because the row's LENGTH is what a reader compares. A "
                          "row starting further along looks longer than its "
                          "count deserves, so a row of $4$ could appear to beat "
                          "a row of $6$ even though $6 > 4$."),
             "check": ["6 > 4", "Eq(6 - 4, 2)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Drawing the count", [
                "The graph below draws the animals instead of listing them: $6$ horses, $4$ sheep, $3$ camels — one picture for each animal counted.",
                "That one-for-one rule is what makes the rows honest. Six pictures means six animals, so the LENGTH of the row is the count.",
                "Now the comparison needs no reading at all. The horse row is visibly the longest, and it beats the sheep row by $6 - 4 = 2$.",
            ]), fig_pict),
            workedset("Read the rows", "One picture is one thing.", [
                wex("$6$ horses and $4$ sheep. How many more horses?",
                    ["The gap between the rows: $6 - 4 = 2$.",
                     "Two more horses than sheep."],
                    "$2$",
                    ["Eq(6 - 4, 2)", "6 > 4"]),
                wex("$6$ horses, $4$ sheep, $3$ camels. How many animals altogether?",
                    ["Add the rows: $6 + 4 = 10$, then $10 + 3 = 13$.",
                     "Thirteen animals in the graph."],
                    "$13$",
                    ["Eq(6 + 4, 10)", "Eq(10 + 3, 13)"]),
            ]),
            tryitset("Read the picture graph", "Row length is the count.", [
                withfig(tp("From the graph below, how many more horses than camels?",
                   ["$3$", "$9$", "$6$"],
                   "Horses $6$, camels $3$: the gap is $6 - 3 = 3$. The $9$ adds the rows instead of comparing them.",
                   ["Eq(6 - 3, 3)", "Eq(6 + 3, 9)"]), fig_pict),
                tp("A row of $8$ pictures against a row of $5$. The longer row has:",
                   ["$3$ more", "$13$ more", "$5$ more"],
                   "$8 - 5 = 3$ more — and because one picture is one thing, the row is also three pictures longer.",
                   ["Eq(8 - 5, 3)", "Eq(5 + 3, 8)"]),
                tp("In a one-for-one picture graph, a row of $7$ pictures means:",
                   ["$7$ things", "$1$ thing", "$70$ things"],
                   "One picture stands for one thing, so seven pictures is seven things — no key to apply and no multiplying to do.",
                   ["Eq(7*1, 7)"]),
            ]),
            tapq("What the row length means", "In a one-for-one picture graph, why is the longest row the biggest count?",
                 ["each picture is one thing, so length is the count",
                  "because longer rows are drawn first",
                  "it is not — you must count every picture",
                  "because the rows are always sorted"],
                 "One picture per thing means the row length and the count are the same number: $6$ horses draw a row of $6$, beating $4$ sheep by $6 - 4 = 2$ both in count and in length.",
                 ["Eq(6*1, 6)", "Eq(6 - 4, 2)", "6 > 4"]),
            funfact("The first graphs were drawn to argue",
                    "Picture graphs became popular when people realised a drawing persuades faster than a column of numbers — a nurse called Florence Nightingale famously drew her hospital data to win an argument about sanitation, and won it. Drawing data is not decoration; it is how a count gets noticed."),
            withfig(teach("Concept B", "Starting from the same line", [
                "The graph below compares two days: Monday $5$ and Tuesday $8$, one picture per visitor.",
                "Tuesday's row is longer, by $8 - 5 = 3$ pictures — which is exactly $3$ more visitors, because each picture is one visitor.",
                "But all of this depends on the rows starting from the SAME line. Let one row begin further along and its length no longer matches its count: a row of $4$ could sit further right and appear to beat a row of $6$. Line them up on the left, always.",
            ]), fig_row),
            workedset("Compare two rows", "Same starting line, then compare lengths.", [
                wex("Monday $5$, Tuesday $8$. Which day was busier, and by how much?",
                    ["$8 > 5$, so Tuesday.",
                     "By $8 - 5 = 3$ visitors; receipt $5 + 3 = 8$ ✓."],
                    "Tuesday, by $3$",
                    ["8 > 5", "Eq(8 - 5, 3)", "Eq(5 + 3, 8)"]),
                wex("Monday $5$ and Tuesday $8$. How many visitors over the two days?",
                    ["Add the rows: $5 + 8 = 13$.",
                     "Thirteen visitors altogether."],
                    "$13$",
                    ["Eq(5 + 8, 13)"]),
            ]),
            tryitset("Fair comparisons", "Do the rows start in line?", [
                tp("Monday $5$, Tuesday $8$. Over both days there were:",
                   ["$13$ visitors", "$3$ visitors", "$40$ visitors"],
                   "Adding the rows: $5 + 8 = 13$. The $3$ is the difference between the days, a different question.",
                   ["Eq(5 + 8, 13)", "Eq(8 - 5, 3)"]),
                tp("A picture graph draws its rows starting at different places. This makes it:",
                   ["misleading, even if the counts are right",
                    "easier to read", "more accurate"],
                   "The reader compares LENGTHS, so a row starting further along looks bigger than it is. Every count could be correct and the picture still lie.",
                   ["Eq(6 - 4, 2)", "6 > 4"]),
                tp("Row A has $9$ pictures and row B has $9$ pictures, but row B starts further right. The counts are:",
                   ["equal — both are $9$",
                    "different, because B looks longer",
                    "impossible to compare"],
                   "The counts are both $9$: $9 - 9 = 0$ difference. Only the drawing is unfair, which is exactly why the starting line matters.",
                   ["Eq(9 - 9, 0)"]),
            ]),
            tapq("The unfair graph", "Two rows both hold $9$ pictures, but one starts further right and looks longer. What is wrong?",
                 ["the rows do not start from the same line",
                  "one row has more pictures",
                  "nothing — one really is bigger",
                  "the pictures are different sizes"],
                 "Both counts are $9$, so the difference is $9 - 9 = 0$. The rows only LOOK different because they begin in different places — the counts are honest and the drawing is not.",
                 ["Eq(9 - 9, 0)", "Eq(9*1, 9)"]),
            recap([
                "One picture stands for one thing, so a row's length IS its count.",
                "Compare rows by their gap: $6$ horses against $4$ sheep is $6 - 4 = 2$ more.",
                "Add the rows for the total: $6 + 4 + 3 = 13$.",
                "Every row must start from the same line, or the picture misleads even with correct counts.",
            ]),
            tip("Before answering anything from a picture graph, check the rows all begin at the same left-hand line. A graph that fails that test cannot be trusted, however carefully its pictures were drawn."),
            tryitset("Chapter practice", "Gap for \"how many more\", sum for \"altogether\".", [
                tp("Rows of $7$ and $2$: how many more in the longer row?",
                   ["$5$", "$9$", "$7$"],
                   "$7 - 2 = 5$ more. The $9$ adds the rows and the $7$ just repeats the longer one.",
                   ["Eq(7 - 2, 5)", "Eq(7 + 2, 9)"]),
                tp("Rows of $6$, $3$ and $5$ hold altogether:",
                   ["$14$", "$9$", "$3$"],
                   "$6 + 3 = 9$, then $9 + 5 = 14$ things drawn in all.",
                   ["Eq(6 + 3, 9)", "Eq(9 + 5, 14)"]),
                tp("In a one-for-one graph, the row with the most pictures is:",
                   ["the biggest count", "the longest to draw only",
                    "impossible to know without a key"],
                   "One picture per thing means there is no key to apply — the longest row simply is the biggest count.",
                   ["Eq(6*1, 6)", "6 > 4"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Picture Graphs\"",
                    "Drawing a count turns a comparison into something you can see. The next lesson swaps the little pictures for plain blocks, which are quicker to draw and just as honest — as long as one block still means one thing.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Block Graphs
# ==========================================================================

def lesson_block_graphs():
    fig_blocks = counts(("red", 6), ("blue", 9), ("green", 4))
    fig_two = counts(("Monday", 7), ("Tuesday", 7))
    return {
        "slug": "block-graphs",
        "title": "Block Graphs",
        "concreteComparison": (
            "Drawing twelve little goats takes a while, and the goats "
            "were never the point — their number was. A block graph "
            "replaces each picture with a plain square, and nothing at "
            "all is lost."),
        "objective": (
            "Draw and read a block graph where one block stands for one "
            "thing, compare bars, and say what makes a block graph "
            "trustworthy."),
        "concept": [
            "**One block stands for one thing.** A bar of $9$ blocks "
            "means $9$ things counted. It is a picture graph with the "
            "drawing simplified away, and the counting rule is exactly "
            "the same.",
            "**Every block must be the same size.** If one bar's blocks "
            "are drawn larger, its bar looks bigger than its count "
            "deserves. Equal blocks, all starting from the same line, is "
            "what makes the comparison fair.",
            "**Equal counts must make equal bars.** If two days both had "
            "$7$ visitors, their bars are exactly as tall as each other — "
            "$7 - 7 = 0$ difference, and the graph should show none. A "
            "graph that shows a gap where there is none is wrong, however "
            "neat it looks.",
        ],
        "keyIdea": (
            "A block graph is a picture graph with plain blocks: one "
            "block per thing, all blocks the same size, all bars from the "
            "same line."),
        "facts": [
            {"title": "Reading a bar",
             "latex": "9 - 4 = 5",
             "explanation": "A bar of 9 blocks stands 5 blocks above a bar of 4."},
            {"title": "Equal counts, equal bars",
             "latex": "7 - 7 = 0",
             "explanation": "Two counts of 7 must produce bars of exactly the same height."},
        ],
        "workedExamples": [
            {"id": "g3da-l4-we1",
             "statement": "A block graph shows red $6$, blue $9$, green $4$. Which is tallest, and how far does it stand above the shortest?",
             "note": "One block per thing.",
             "solution": ("Blue is tallest at $9$ blocks, and green is shortest "
                          "at $4$. Blue stands $9 - 4 = 5$ blocks above green, "
                          "which is $5$ more things counted — one block, one "
                          "thing."),
             "badges": [{"text": "core"}],
             "check": ["9 > 4", "Eq(9 - 4, 5)", "Eq(4 + 5, 9)"]},
            {"id": "g3da-l4-we2",
             "statement": "Monday and Tuesday both had $7$ visitors, but Monday's bar is drawn taller. What is wrong?",
             "note": "Equal counts must give equal bars.",
             "solution": ("The counts are the same, so the difference is "
                          "$7 - 7 = 0$ and the bars must match exactly. Monday's "
                          "bar being taller means its blocks were drawn larger, "
                          "or it did not start from the same line — the graph is "
                          "misleading even though both counts are right."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7 - 7, 0)", "Eq(7*1, 7)"]},
        ],
        "commonMistakes": [
            {"text": "Drawing blocks of different sizes in different bars.",
             "correction": "The reader compares bar heights, so unequal blocks make the comparison false. Every block must be the same size and every bar must start from the same line.",
             "authored": True},
            {"text": "Counting the bars instead of the blocks — reading a three-bar graph as \"3\".",
             "correction": "The bars name the things being counted; the blocks are the count. Three bars of 6, 9 and 4 hold 6 + 9 + 4 = 19 things.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3da-l4-t1",
             "statement": "Bars of $8$ and $5$ blocks. How much taller is the first, and how many things in total?",
             "solution": ("Taller by $8 - 5 = 3$ blocks, which is $3$ more "
                          "things. Together they hold $8 + 5 = 13$."),
             "check": ["Eq(8 - 5, 3)", "Eq(8 + 5, 13)"]},
            {"id": "g3da-l4-t2",
             "statement": "Why must every block in a block graph be the same size?",
             "solution": ("Because the reader compares bar HEIGHTS. Larger "
                          "blocks in one bar make it stand taller than its count "
                          "deserves, so a bar of $4$ could out-tower a bar of "
                          "$6$ even though $6 > 4$."),
             "check": ["6 > 4", "Eq(6 - 4, 2)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Blocks instead of pictures", [
                "Drawing twelve little goats is slow, and the goats were never the point — the number was. So replace each picture with a plain block.",
                "The graph below shows red $6$, blue $9$, green $4$, one block per thing. Nothing has been lost: blue is still visibly the tallest.",
                "Blue stands $9 - 4 = 5$ blocks above green, and that is $5$ more things counted. One block, one thing — the same rule as a picture graph, drawn faster.",
            ]), fig_blocks),
            workedset("Read the bars", "Count the blocks, not the bars.", [
                wex("Red $6$, blue $9$, green $4$. Which is tallest, and by how much over green?",
                    ["Blue at $9$ blocks is tallest; green at $4$ is shortest.",
                     "Blue stands $9 - 4 = 5$ blocks above green."],
                    "blue, by $5$",
                    ["9 > 4", "Eq(9 - 4, 5)", "Eq(4 + 5, 9)"]),
                wex("Red $6$, blue $9$, green $4$. How many things altogether?",
                    ["Add the bars: $6 + 9 = 15$, then $15 + 4 = 19$.",
                     "Nineteen things counted in all."],
                    "$19$",
                    ["Eq(6 + 9, 15)", "Eq(15 + 4, 19)"]),
            ]),
            tryitset("Read the block graph", "One block is one thing.", [
                withfig(tp("From the graph below, how much taller is blue than red?",
                   ["$3$ blocks", "$15$ blocks", "$9$ blocks"],
                   "Blue $9$, red $6$: $9 - 6 = 3$ blocks taller, meaning three more things. The $15$ adds the bars instead of comparing them.",
                   ["Eq(9 - 6, 3)", "Eq(6 + 9, 15)"]), fig_blocks),
                tp("A three-bar graph with bars of $6$, $9$ and $4$ shows how many things?",
                   ["$19$", "$3$", "$9$"],
                   "The bars name the categories; the blocks are the count: $6 + 9 + 4 = 19$. Answering $3$ counts the bars.",
                   ["Eq(6 + 9 + 4, 19)"]),
                tp("A bar of $7$ blocks stands for:",
                   ["$7$ things", "$1$ thing", "$7$ bars"],
                   "One block per thing, so seven blocks is seven things — no key and no multiplying.",
                   ["Eq(7*1, 7)"]),
            ]),
            tapq("Bars against blocks", "A graph has $3$ bars holding $6$, $9$ and $4$ blocks. How many things were counted?",
                 ["$19$", "$3$", "$9$", "$13$"],
                 "The bars are the categories and the blocks are the count: $6 + 9 + 4 = 19$ things. Answering $3$ counts the bars and $9$ takes only the tallest.",
                 ["Eq(6 + 9 + 4, 19)", "9 > 6"]),
            funfact("Squared paper was invented for this",
                    "The reason exercise books come with squares printed on them is largely to make graphs like this honest. Every square is identical, so a bar of nine squares cannot accidentally be drawn taller than it should — the paper enforces the fairness that the drawer might forget."),
            withfig(teach("Concept B", "What makes a block graph fair", [
                "Two rules keep a block graph honest, and both are about the DRAWING rather than the counting.",
                "First, every block must be the same size. Second, every bar must start from the same line. Break either and a bar of $4$ can be made to tower over a bar of $6$, even though $6 > 4$.",
                "The graph below shows Monday $7$ and Tuesday $7$. The counts are identical, so $7 - 7 = 0$ — the bars must be exactly as tall as each other. A graph showing a gap here would be wrong however neatly it was drawn.",
            ]), fig_two),
            workedset("Fair or unfair?", "Same blocks, same starting line.", [
                wex("Monday $7$, Tuesday $7$, but Monday's bar is taller. What is wrong?",
                    ["The counts are equal: $7 - 7 = 0$.",
                     "So the bars must match. Monday's blocks were drawn larger, or its bar started higher — the drawing is wrong, not the count."],
                    "the drawing is unfair",
                    ["Eq(7 - 7, 0)", "Eq(7*1, 7)"]),
                wex("Why must all bars start from the same line?",
                    ["Readers compare bar heights, not their tops.",
                     "A bar starting higher looks bigger than its count: a bar of $4$ could seem to beat one of $6$, though $6 > 4$."],
                    "so heights match counts",
                    ["6 > 4", "Eq(6 - 4, 2)"]),
            ]),
            tryitset("Is the graph honest?", "Check the blocks and the baseline.", [
                tp("Two bars both hold $7$ blocks but one is drawn taller. This graph is:",
                   ["misleading — equal counts need equal bars",
                    "fine, if the counts are right",
                    "showing that one really is bigger"],
                   "$7 - 7 = 0$, so the bars must be identical. A visible gap where the counts agree means the drawing is at fault.",
                   ["Eq(7 - 7, 0)"]),
                tp("One bar's blocks are drawn twice the size of another's. The graph:",
                   ["cannot be compared fairly",
                    "is easier to read",
                    "is fine as long as the counts are labelled"],
                   "The reader compares heights, so double-size blocks double a bar's apparent count. Labels do not undo a picture that lies.",
                   ["Eq(6 - 4, 2)", "6 > 4"]),
                tp("A fair block graph needs:",
                   ["equal blocks and one starting line",
                    "the tallest bar on the left",
                    "at least three bars"],
                   "Those two rules are what make bar heights match counts. The order of the bars and how many there are is up to you.",
                   ["Eq(7*1, 7)", "Eq(9 - 4, 5)"]),
            ]),
            tapq("The rule that keeps it honest", "Why must every block be the same size?",
                 ["so a bar's height matches its count",
                  "so the graph looks tidy",
                  "so the bars fit on the page",
                  "so each bar has the same number of blocks"],
                 "Readers judge by height, so unequal blocks break the link between height and count — a bar of $4$ with big blocks could out-tower a bar of $6$, though $6 - 4 = 2$ says the opposite.",
                 ["6 > 4", "Eq(6 - 4, 2)", "Eq(7*1, 7)"]),
            recap([
                "A block graph is a picture graph with plain blocks: one block per thing.",
                "Compare bars by their gap: $9 - 4 = 5$ blocks is $5$ more things.",
                "Every block must be the same size and every bar must start from the same line.",
                "Equal counts must give equal bars — $7 - 7 = 0$ means no visible gap.",
            ]),
            tip("Draw block graphs on squared paper and use one printed square per block. The paper then guarantees the fairness for you, and there is nothing left to get wrong except the counting."),
            tryitset("Chapter practice", "Blocks are the count; bars are the categories.", [
                tp("Bars of $5$ and $9$ blocks: the taller stands above the shorter by:",
                   ["$4$ blocks", "$14$ blocks", "$9$ blocks"],
                   "$9 - 5 = 4$ blocks, meaning four more things counted.",
                   ["Eq(9 - 5, 4)", "Eq(5 + 4, 9)"]),
                tp("Four bars of $3$, $6$, $2$ and $5$ blocks hold:",
                   ["$16$ things", "$4$ things", "$6$ things"],
                   "$3 + 6 = 9$, $9 + 2 = 11$, $11 + 5 = 16$ things in all. Answering $4$ counts the bars.",
                   ["Eq(3 + 6, 9)", "Eq(9 + 2, 11)", "Eq(11 + 5, 16)"]),
                tp("Two counts of $6$ should be drawn as:",
                   ["two bars of exactly the same height",
                    "two bars of different heights",
                    "one bar of $12$"],
                   "Equal counts must give equal bars: $6 - 6 = 0$ difference, so no visible gap.",
                   ["Eq(6 - 6, 0)", "Eq(6*1, 6)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Block Graphs\"",
                    "You can now draw a count so that it can be seen and trusted. The last lesson of the year stops drawing and starts asking — because a graph is only useful once you know what questions it can answer.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Answering Questions from Data
# ==========================================================================

def lesson_questions():
    fig_data = counts(("wrestling", 9), ("archery", 5), ("racing", 6))
    fig_pair = counts(("boys", 8), ("girls", 11))
    return {
        "slug": "answering-questions-from-data",
        "title": "Answering Questions from Data",
        "concreteComparison": (
            "A finished graph is not the end of the work — it is the "
            "beginning. Which sport was most popular? How many more chose "
            "wrestling than archery? How many children were asked "
            "altogether? Every one of those is answered by reading the "
            "same three bars a different way."),
        "objective": (
            "Answer most, fewest, how-many-more and how-many-altogether "
            "questions from a graph, and say which arithmetic each "
            "question needs."),
        "concept": [
            "**Most and fewest need no arithmetic at all.** The tallest "
            "bar is the most popular and the shortest is the least. With "
            "wrestling $9$, archery $5$ and racing $6$, wrestling wins "
            "and archery comes last — read straight off the picture.",
            "**\"How many more\" is a subtraction.** Wrestling over "
            "archery is $9 - 5 = 4$. The answer is the GAP between two "
            "bars, never the height of the taller one.",
            "**\"How many altogether\" is an addition.** All three bars "
            "together: $9 + 5 + 6 = 20$ children asked. Different "
            "question, different operation — and reading which is which "
            "is the real skill.",
        ],
        "keyIdea": (
            "Most and fewest are read off; \"how many more\" subtracts "
            "two bars; \"how many altogether\" adds them all."),
        "facts": [
            {"title": "How many more",
             "latex": "9 - 5 = 4",
             "explanation": "The gap between the wrestling and archery bars."},
            {"title": "How many altogether",
             "latex": "9 + 5 + 6 = 20",
             "explanation": "All three bars added gives everyone who was asked."},
        ],
        "workedExamples": [
            {"id": "g3da-l5-we1",
             "statement": "A graph shows wrestling $9$, archery $5$, racing $6$. Name the most and least popular, and say how many more chose wrestling than archery.",
             "note": "Two readings and one subtraction.",
             "solution": ("Most popular: wrestling, the tallest bar at $9$. "
                          "Least: archery at $5$. More for wrestling than "
                          "archery: $9 - 5 = 4$ children — the gap between the "
                          "bars, not the height of either."),
             "badges": [{"text": "core"}],
             "check": ["9 > 6", "6 > 5", "Eq(9 - 5, 4)", "Eq(5 + 4, 9)"]},
            {"id": "g3da-l5-we2",
             "statement": "From the same graph, how many children were asked altogether?",
             "note": "Every child chose exactly one sport.",
             "solution": ("Each child appears in exactly one bar, so adding the "
                          "bars counts everyone: $9 + 5 + 6 = 20$ children. "
                          "Note this is an addition, while the previous question "
                          "was a subtraction — the words decide."),
             "badges": [{"text": "core"}],
             "check": ["Eq(9 + 5, 14)", "Eq(14 + 6, 20)"]},
        ],
        "commonMistakes": [
            {"text": "Answering \"how many more chose wrestling than archery\" with 9.",
             "correction": "9 is how many chose wrestling. The question asks for the GAP: 9 − 5 = 4. Read what is being compared before you answer.",
             "authored": True},
            {"text": "Adding bars to answer a comparison question, or subtracting to answer a total.",
             "correction": "\"How many more\" subtracts two bars; \"how many altogether\" adds them all. The words choose the operation, not the numbers.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3da-l5-t1",
             "statement": "From wrestling $9$, archery $5$, racing $6$: how many more chose racing than archery?",
             "solution": ("The gap between the two bars: $6 - 5 = 1$ child."),
             "check": ["Eq(6 - 5, 1)", "Eq(5 + 1, 6)"]},
            {"id": "g3da-l5-t2",
             "statement": "A graph shows boys $8$ and girls $11$. How many children altogether, and how many more girls?",
             "solution": ("Altogether: $8 + 11 = 19$ children. More girls: "
                          "$11 - 8 = 3$."),
             "check": ["Eq(8 + 11, 19)", "Eq(11 - 8, 3)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Reading most and fewest", [
                "The graph below shows what a class chose: wrestling $9$, archery $5$, racing $6$.",
                "\"Which was most popular?\" needs no arithmetic — the tallest bar answers it. Wrestling, at $9$, since $9 > 6$ and $9 > 5$.",
                "\"Which was least?\" is the shortest bar: archery at $5$. Two questions answered by looking, which is exactly why the data was drawn.",
            ]), fig_data),
            workedset("Most and fewest", "Read the tallest and shortest bars.", [
                wex("Wrestling $9$, archery $5$, racing $6$. Which is most popular?",
                    ["The tallest bar is wrestling at $9$.",
                     "$9 > 6$ and $9 > 5$, so wrestling wins."],
                    "wrestling",
                    ["9 > 6", "9 > 5"]),
                wex("Which was least popular?",
                    ["The shortest bar is archery at $5$.",
                     "$5 < 6$ and $5 < 9$."],
                    "archery",
                    ["5 < 6", "5 < 9"]),
            ]),
            tryitset("Read it off", "Tallest is most; shortest is fewest.", [
                withfig(tp("From the graph below, the least popular sport is:",
                   ["archery", "wrestling", "racing"],
                   "Archery's bar is shortest at $5$, below racing's $6$ and wrestling's $9$.",
                   ["5 < 6", "5 < 9"]), fig_data),
                tp("With bars of $8$, $11$ and $4$, the most popular has:",
                   ["$11$", "$23$", "$8$"],
                   "The tallest bar is $11$, since $11 > 8 > 4$. The $23$ adds all three bars, which answers a total instead.",
                   ["11 > 8", "8 > 4", "Eq(8 + 11 + 4, 23)"]),
                tp("Answering \"which is most popular\" requires:",
                   ["no arithmetic — just look",
                    "adding all the bars",
                    "subtracting the smallest from the largest"],
                   "The tallest bar answers it directly. Adding and subtracting answer the total and the gap, which are different questions.",
                   ["9 > 6", "Eq(9 - 5, 4)"]),
            ]),
            tapq("Which question needs no sum?", "Which of these can be answered just by looking at the bars?",
                 ["which sport was most popular",
                  "how many more chose wrestling than archery",
                  "how many children were asked altogether",
                  "none of them"],
                 "The tallest bar names the most popular with no arithmetic. The other two need $9 - 5 = 4$ and $9 + 5 + 6 = 20$ respectively.",
                 ["9 > 6", "Eq(9 - 5, 4)", "Eq(9 + 5 + 6, 20)"]),
            funfact("The question comes before the graph",
                    "Real surveys are designed backwards: someone decides what they need to know, and only then chooses what to count. A graph that answers no question anyone asked is a common and expensive mistake — which is why this lesson matters more than the drawing did."),
            withfig(teach("Concept B", "How many more, and how many altogether", [
                "The two remaining questions each need a sum, and the words tell you which.",
                "\"How many more chose wrestling than archery?\" asks for the GAP between two bars: $9 - 5 = 4$ children. Not $9$ — that is simply how many chose wrestling.",
                "\"How many children were asked altogether?\" adds every bar: $9 + 5 + 6 = 20$. The graph below shows a two-bar version — boys $8$, girls $11$ — where the same two questions give $11 - 8 = 3$ and $8 + 11 = 19$.",
            ]), fig_pair),
            workedset("Choose the operation",
                      "\"More\" subtracts; \"altogether\" adds.", [
                wex("How many more chose wrestling ($9$) than archery ($5$)?",
                    ["\"How many more\" asks for the gap.",
                     "$9 - 5 = 4$ children; receipt $5 + 4 = 9$ ✓."],
                    "$4$",
                    ["Eq(9 - 5, 4)", "Eq(5 + 4, 9)"]),
                wex("How many children were asked altogether, from bars of $9$, $5$ and $6$?",
                    ["Each child is in exactly one bar.",
                     "$9 + 5 = 14$, then $14 + 6 = 20$ children."],
                    "$20$",
                    ["Eq(9 + 5, 14)", "Eq(14 + 6, 20)"]),
            ]),
            tryitset("Which sum?", "Read the words, then choose.", [
                tp("Boys $8$, girls $11$. How many more girls than boys?",
                   ["$3$", "$19$", "$11$"],
                   "\"How many more\" is the gap: $11 - 8 = 3$. The $19$ adds them and $11$ just repeats the taller bar.",
                   ["Eq(11 - 8, 3)", "Eq(8 + 11, 19)"]),
                tp("Boys $8$, girls $11$. How many children altogether?",
                   ["$19$", "$3$", "$88$"],
                   "\"Altogether\" adds every bar: $8 + 11 = 19$ children.",
                   ["Eq(8 + 11, 19)", "Eq(11 - 8, 3)"]),
                tp("Wrestling $9$, archery $5$, racing $6$. How many more chose racing than archery?",
                   ["$1$", "$11$", "$6$"],
                   "The gap between those two bars: $6 - 5 = 1$ child. Adding them gives $11$, and $6$ is just racing's count.",
                   ["Eq(6 - 5, 1)", "Eq(6 + 5, 11)"]),
            ]),
            tapq("Reading the question", "\"How many more chose wrestling ($9$) than archery ($5$)?\" The answer is:",
                 ["$4$", "$9$", "$14$", "$5$"],
                 "The question asks for the GAP between the two bars: $9 - 5 = 4$ children, with receipt $5 + 4 = 9$ ✓. Answering $9$ gives wrestling's count and $14$ adds the two bars together.",
                 ["Eq(9 - 5, 4)", "Eq(5 + 4, 9)", "Eq(9 + 5, 14)"]),
            recap([
                "Most and fewest are read straight off — the tallest and shortest bars.",
                "\"How many more\" subtracts two bars: $9 - 5 = 4$.",
                "\"How many altogether\" adds every bar: $9 + 5 + 6 = 20$.",
                "The words of the question choose the operation, not the numbers in the graph.",
            ]),
            tip("Underline the question's key words before you look at the graph — \"most\", \"more than\", \"altogether\". The operation is decided by those words, and deciding it first stops the numbers from tempting you into the wrong one."),
            tryitset("Chapter practice", "Words first, then the arithmetic.", [
                tp("Bars of $7$, $4$ and $9$. How many altogether?",
                   ["$20$", "$5$", "$9$"],
                   "$7 + 4 = 11$, then $11 + 9 = 20$. The $5$ is the gap between the tallest and shortest.",
                   ["Eq(7 + 4, 11)", "Eq(11 + 9, 20)", "Eq(9 - 4, 5)"]),
                tp("Bars of $7$ and $4$. How many more in the taller?",
                   ["$3$", "$11$", "$7$"],
                   "$7 - 4 = 3$ more. Adding gives $11$ and $7$ just repeats the taller bar.",
                   ["Eq(7 - 4, 3)", "Eq(7 + 4, 11)"]),
                tp("Which question needs an ADDITION?",
                   ["how many altogether", "how many more",
                    "which is the most popular"],
                   "\"Altogether\" adds every bar. \"How many more\" subtracts two, and \"most popular\" needs no arithmetic at all.",
                   ["Eq(9 + 5 + 6, 20)", "Eq(9 - 5, 4)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Answering Questions from Data\" — and the Grade 3 year",
                    "Tallies, tables, picture graphs, block graphs and the questions they answer. And with them the whole year: numbers to a thousand, adding and subtracting them, multiplying and dividing, fractions, shapes, measuring, and now data. Everything here is waiting for you again next year, one size larger.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = tally(13, "visitors")
    fig_pr6 = counts(("wrestling", 9), ("archery", 5), ("racing", 6))
    return [
        withprobfig(prob("g3da-pr1", "Read the tally shown, and say how many bundles and singles it holds.",
             "Two bundles and three singles: $2 \\times 5 = 10$ from the bundles, plus $3$, giving $10 + 3 = 13$. Three is less than five, as the leftovers always must be.",
             ["Eq(2*5, 10)", "Eq(10 + 3, 13)", "3 < 5"]), fig_pr1),
        prob("g3da-pr2", "Draw $18$ as tally marks. How many bundles, how many singles, and how do you know no more bundles are possible?",
             "Three bundles use $3 \\times 5 = 15$ marks, leaving $18 - 15 = 3$ singles. No fourth bundle is possible because only $3$ marks remain and a bundle needs $5$ — and $3 < 5$.",
             ["Eq(3*5, 15)", "Eq(18 - 15, 3)", "3 < 5"]),
        prob("g3da-pr3", "A table reads sheep $9$, goats $6$, horses $4$. Give the total, the most numerous animal, and the gap between the largest and smallest rows.",
             "Total: $9 + 6 + 4 = 19$ animals. Most numerous: sheep at $9$. Gap between largest and smallest: $9 - 4 = 5$.",
             ["Eq(9 + 6 + 4, 19)", "9 > 6", "Eq(9 - 4, 5)"]),
        prob("g3da-pr4", "A table has rows of $12$ and $7$ and a total of $25$. Find the missing row and prove it.",
             "The known rows come to $12 + 7 = 19$, so the missing row is $25 - 19 = 6$. Proof: $19 + 6 = 25$ ✓, matching the written total.",
             ["Eq(12 + 7, 19)", "Eq(25 - 19, 6)", "Eq(19 + 6, 25)"]),
        prob("g3da-pr5", "Explain why every row of a picture graph must begin at the same line, using two rows of equal count as your example.",
             "The reader compares row LENGTHS, so the starting point decides what the length looks like. Two rows both holding $9$ pictures have a difference of $9 - 9 = 0$ and must look identical; if one begins further along it appears larger, and the picture lies even though both counts are correct.",
             ["Eq(9 - 9, 0)", "Eq(9*1, 9)"]),
        withprobfig(prob("g3da-pr6", "From the graph shown, answer all three: which sport was most popular, how many more chose wrestling than archery, and how many children were asked.",
             "Most popular: wrestling, the tallest bar at $9$. More for wrestling than archery: $9 - 5 = 4$ children. Asked altogether: $9 + 5 + 6 = 20$. Three questions, three different operations — none, a subtraction, and an addition.",
             ["9 > 6", "Eq(9 - 5, 4)", "Eq(9 + 5 + 6, 20)"]), fig_pr6),
        prob("g3da-pr7", "A block graph draws one bar with blocks twice the size of another's. Explain what goes wrong even if both counts are correct.",
             "Readers judge a bar by its height, and double-size blocks double the height a count produces. A bar of $4$ drawn with big blocks can stand taller than a bar of $6$ drawn with small ones, reversing the true comparison — $6 > 4$, with a real gap of $6 - 4 = 2$ in the other direction.",
             ["6 > 4", "Eq(6 - 4, 2)"]),
        prob("g3da-pr8", "Bat is asked how many more children chose racing ($6$) than archery ($5$) and answers $6$. Name his mistake and give the right answer.",
             "He gave racing's count instead of the gap between the two bars. \"How many more\" is a subtraction: $6 - 5 = 1$ child, with receipt $5 + 1 = 6$ ✓. His $6$ answers \"how many chose racing\", which was not the question.",
             ["Eq(6 - 5, 1)", "Eq(5 + 1, 6)"]),
    ]


def test_bank():
    return [
        prob("g3da-x1", "A tally shows three bundles and four singles. Give the count, and explain why four is the largest number of singles possible.",
             "Three bundles are $3 \\times 5 = 15$, plus $4$ singles: $15 + 4 = 19$. Four is the maximum because a fifth single would be laid across the other four and close a new bundle — so the leftovers are always fewer than five, and $4 < 5$.",
             ["Eq(3*5, 15)", "Eq(15 + 4, 19)", "4 < 5"]),
        prob("g3da-x2", "A table reads red $8$, blue $5$, green $7$, with a total written as $21$. Check the total and say whether the table is consistent.",
             "The rows add to $8 + 5 = 13$, then $13 + 7 = 20$. The written total of $21$ is one too many — $21 - 20 = 1$ — so the table is not consistent, and either a row or the total was recorded wrongly. This is exactly the error a written total exists to catch.",
             ["Eq(8 + 5, 13)", "Eq(13 + 7, 20)", "Eq(21 - 20, 1)",
              "Ne(20, 21)"]),
        prob("g3da-x3", "A one-for-one picture graph shows $7$ birds, $3$ fish and $5$ insects. Answer: most common, how many more birds than fish, and how many creatures in all.",
             "Most common: birds, the longest row at $7$. More birds than fish: $7 - 3 = 4$. Creatures in all: $7 + 3 + 5 = 15$.",
             ["7 > 5", "Eq(7 - 3, 4)", "Eq(7 + 3 + 5, 15)"]),
        prob("g3da-x4", "Two block graph bars each hold $6$ blocks, but one is drawn taller. Say what has gone wrong and what the true comparison is.",
             "The counts are equal, so the true difference is $6 - 6 = 0$ and the bars must be exactly the same height. One bar's blocks were drawn larger, or it did not start from the same baseline — the drawing is at fault, not the counting.",
             ["Eq(6 - 6, 0)", "Eq(6*1, 6)"]),
        prob("g3da-x5", "From bars of wrestling $9$, archery $5$ and racing $6$, write one question answered by adding and one answered by subtracting, and answer both.",
             "Adding: \"How many children were asked altogether?\" — $9 + 5 + 6 = 20$. Subtracting: \"How many more chose wrestling than archery?\" — $9 - 5 = 4$. The words of a question choose its operation, and the same three bars serve both.",
             ["Eq(9 + 5 + 6, 20)", "Eq(9 - 5, 4)", "Eq(5 + 4, 9)"]),
        prob("g3da-x6", "A survey records $12$ children choosing wrestling as two bundles and two singles in a tally, then draws it as a bar of $12$ blocks. Follow the count through all three forms and say what each form is good at.",
             "The tally reads $2 \\times 5 + 2 = 12$ — good for recording while the counting is still happening. The table row reads $12$ — good for comparing with other rows and for totalling. The bar of $12$ blocks — good for seeing the comparison without reading any number at all. The count never changed through any of it: $12$ throughout.",
             ["Eq(2*5 + 2, 12)", "Eq(2*5, 10)", "Eq(10 + 2, 12)",
              "Eq(12*1, 12)"]),
    ]


def main():
    topic = {
        "slug": "tallies-and-picture-graphs",
        "title": "Tallies & Picture Graphs",
        "grade": 3,
        "status": "published",
        "blurb": ("Counting with tally marks bundled in fives, collecting the "
                  "counts into a table with a total, drawing picture graphs "
                  "and block graphs one-for-one, and answering most, fewest, "
                  "how-many-more and altogether questions from them."),
        "lessons": [
            lesson_tallies(),
            lesson_tables(),
            lesson_pictographs(),
            lesson_block_graphs(),
            lesson_questions(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "tallies-and-picture-graphs.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
