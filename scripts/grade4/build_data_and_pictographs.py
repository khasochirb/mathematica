#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Data & Pictographs.

Tally marks bundled by five, frequency tables whose total row is a
receipt, pictographs with a key (one symbol = 2, 5 or 10), bar charts
read against scales stepping by 1, 2 and 5, and the questions people
actually ask of data — most popular, how many more, how many
altogether, and two-step reads that combine rows first.

Through-line: EVERY MARK STANDS FOR SOMETHING COUNTED, AND THE PARTS
MUST ADD BACK TO THE TOTAL. A tally bundle is worth five, a pictograph
symbol is worth the key, a gridline is worth the scale step — and in
every lesson the pieces are put back together to prove the reading was
honest.

Grade discipline: keys only 2, 5 and 10; bar scales only 1, 2 and 5;
no mean, no range, no line graphs (those are Grade 5). No negative
numbers, every value inside 10 000, every multiplication inside the
times tables. Figures are built from the SAME Python variables as the
statements they illustrate, so text and picture cannot disagree.

Run: python3 scripts/grade4/build_data_and_pictographs.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic, withfig,
                     fig_groups, C_ACCENT, C_WARM, C_GREEN)


def ordinal(n):
    """'$3$rd', '$4$th' — the numeral in math mode with the right English
    ending, so an ordinal in prose can never drift out of step with the
    number it was built from."""
    n = int(n)
    end = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return "$%d$%s" % (n, end)


def tally_fig(bundles, singles):
    """A tally picture: `bundles` gates of five, then the loose singles."""
    groups = [(5, "bundle %d" % (i + 1), C_ACCENT) for i in range(bundles)]
    if singles:
        groups.append((singles, "singles", C_WARM))
    return fig_groups(*groups)


# ==========================================================================
# Lesson 1 — Tally Marks
# ==========================================================================

def lesson_tally():
    # Reading: b bundles and s singles.
    b, s, n = 4, 3, 23
    # Second reading, used in the worked set.
    b2, s2, n2 = 7, 1, 36
    # Drawing: n3 becomes b3 bundles and s3 singles.
    n3, b3, s3 = 27, 5, 2
    n4, b4, s4 = 38, 7, 3
    # Chapter-practice picture.
    b5, s5, n5 = 6, 3, 33
    fig_read = tally_fig(b, s)
    fig_draw = tally_fig(b3, s3)
    fig_practice = tally_fig(b5, s5)
    return {
        "slug": "tally-marks",
        "title": "Tally Marks",
        "concreteComparison": (
            "Sheep come back through the gate faster than you can hold "
            "numbers in your head, so you scratch one mark for each — "
            "and every fifth mark strikes across the four before it, "
            "tying them into a bundle. At the end you never count marks "
            "one by one. You count bundles by fives and add the loose "
            "ones: $5 \\times 4 + 3 = 23$ sheep."),
        "objective": (
            "Read a tally as $5 \\times$ bundles plus singles, and turn "
            "any count into tally marks by dividing by five — bundles "
            "as the answer, singles as the leftover."),
        "concept": [
            "**Four marks and a gate make five.** You write four "
            "uprights, and the fifth mark strikes across them. That "
            "crossed group is one BUNDLE, and a bundle is always worth "
            "exactly $5$ — never four, never six.",
            "**Read a tally as five times the bundles, plus the "
            "singles.** $4$ bundles and $3$ loose marks is $5 \\times "
            "4 = 20$, then $20 + 3 = 23$. One multiplication and one "
            "addition instead of twenty-three separate counts.",
            "**Going back is division by five.** To draw $27$ as "
            "tallies, share $27$ into fives: $27 \\div 5 = 5$ with $2$ "
            "left, so $5$ bundles and $2$ singles. The receipt says "
            "$5 \\times 5 + 2 = 27$, and the leftover is always fewer "
            "than five.",
        ],
        "keyIdea": (
            "A tally is a count parcelled into fives: value $= 5 \\times "
            "\\text{bundles} + \\text{singles}$. Reading multiplies by "
            "five; drawing divides by five, and the singles are the "
            "remainder — always fewer than $5$."),
        "facts": [
            {"title": "Read the bundles",
             "latex": "5 \\times 4 + 3 = 23",
             "explanation": "Four bundles are worth 20; the three loose marks bring it to 23."},
            {"title": "Draw by dividing",
             "latex": "27 \\div 5 = 5 \\ \\text{r}\\ 2 \\ \\Rightarrow \\ 5 \\ \\text{bundles},\\ 2 \\ \\text{singles}",
             "explanation": "The quotient counts bundles, the remainder counts singles, and the remainder is under 5."},
        ],
        "workedExamples": [
            {"id": "g4da-l1-we1",
             "statement": "A herder's tally sheet shows $4$ full bundles and $3$ single marks. How many sheep came through the gate?",
             "note": "Bundles are worth five each; the singles are worth one each.",
             "solution": ("Count the bundles by fives: $5 \\times 4 = 20$. Add the "
                          "three loose marks: $20 + 3 = 23$ sheep. The singles are "
                          "fewer than five, so the tally is written properly."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*4, 20)", "Eq(20 + 3, 23)", "Eq(5*4 + 3, 23)", "3 < 5"]},
            {"id": "g4da-l1-we2",
             "statement": "Draw $27$ visitors as tally marks. How many bundles and how many singles?",
             "note": "Parcel the count into fives.",
             "solution": ("$27 \\div 5 = 5$ with $2$ left over: $5$ bundles and $2$ "
                          "singles. Receipt: $5 \\times 5 + 2 = 27$ and $2 < 5$, so "
                          "no sixth bundle is hiding in the leftovers."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*5 + 2, 27)", "2 < 5"]},
        ],
        "commonMistakes": [
            {"text": "Counting the crossing stroke as an extra mark, so a bundle looks like six.",
             "correction": "The stroke across IS the fifth mark, not a sixth. Every full bundle is worth exactly 5, so 4 bundles are 20 — not 24.",
             "authored": True},
            {"text": "Adding the bundles instead of multiplying them by five — reading 4 bundles and 3 singles as 7.",
             "correction": "Each bundle carries five marks: 5 × 4 + 3 = 23. Adding 4 + 3 counts the bundles as if each were a single mark.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4da-l1-t1",
             "statement": "A tally shows $6$ bundles and $4$ singles. What is the count?",
             "solution": "$5 \\times 6 = 30$, then $30 + 4 = 34$. The singles ($4$) are fewer than $5$, so the tally is tidy.",
             "check": ["Eq(5*6, 30)", "Eq(5*6 + 4, 34)", "4 < 5"]},
            {"id": "g4da-l1-t2",
             "statement": "Draw $38$ as tally marks.",
             "solution": "$38 \\div 5 = 7$ with $3$ left: $7$ bundles and $3$ singles. Receipt: $5 \\times 7 + 3 = 38$ and $3 < 5$.",
             "check": ["Eq(5*7 + 3, 38)", "3 < 5"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Four marks and a gate", [
                "One mark per thing counted — but marks in a long row are as hard to count as the sheep were. So every fifth mark strikes ACROSS the four before it and ties them into a bundle.",
                "A bundle is worth exactly $5$. To read the tally, count the bundles by fives and then add the loose singles: $%d$ bundles and $%d$ singles is $5 \\times %d + %d = %d$." % (b, s, b, s, n),
                "The singles are never five or more — the moment a fifth single arrives it strikes across and becomes a new bundle.",
            ]), fig_read),
            workedset("Reading a tally",
                      "Bundles by fives first, singles second.", [
                withfig(wex("A tally shows $%d$ bundles and $%d$ singles. What is the count?" % (b, s),
                    ["Bundles by fives: $5 \\times %d = %d$." % (b, 5 * b),
                     "Add the singles: $%d + %d = %d$." % (5 * b, s, n)],
                    "$%d$" % n,
                    ["Eq(5*4, 20)", "Eq(5*4 + 3, 23)", "3 < 5"]), fig_read),
                wex("A tally shows $%d$ bundles and $%d$ single. What is the count?" % (b2, s2),
                    ["$5 \\times %d = %d$ from the bundles." % (b2, 5 * b2),
                     "One loose mark more: $%d + %d = %d$." % (5 * b2, s2, n2)],
                    "$%d$" % n2,
                    ["Eq(5*7, 35)", "Eq(5*7 + 1, 36)", "1 < 5"]),
            ]),
            tryitset("Count the bundles", "Five for every bundle, one for every single.", [
                tp("A tally shows $3$ bundles and $2$ singles. The count is:",
                   ["$17$", "$5$", "$32$"],
                   "$5 \\times 3 = 15$ from the bundles, then $15 + 2 = 17$. The option $5$ came from adding $3 + 2$ as if a bundle were worth one; $32$ read the bundles as tens.",
                   ["Eq(5*3 + 2, 17)", "Eq(3 + 2, 5)"]),
                tp("A tally shows $9$ bundles and no singles. The count is:",
                   ["$45$", "$9$", "$14$"],
                   "Nine fives: $5 \\times 9 = 45$. The option $9$ counted the bundles as marks; $14$ added $9 + 5$ instead of multiplying.",
                   ["Eq(5*9, 45)", "Eq(9 + 5, 14)"]),
                tp("A tally shows $5$ bundles and $4$ singles. The count is:",
                   ["$29$", "$25$", "$54$"],
                   "$5 \\times 5 = 25$, then $25 + 4 = 29$. The option $25$ forgot the four loose marks entirely.",
                   ["Eq(5*5 + 4, 29)", "Eq(5*5, 25)", "4 < 5"]),
            ]),
            tapq("Five singles never stand", "A tally sheet shows $3$ bundles and $5$ singles. What should the writer have done?",
                 ["tied the five singles into a fourth bundle — the count is $20$",
                  "left it as it is, since singles may go up to nine",
                  "rubbed out one single to make it four",
                  "counted each single as a bundle"],
                 "The fifth single is exactly the mark that strikes across and makes a bundle, so singles stop at four. The count is unchanged either way: $5 \\times 3 + 5 = 20$, which is $5 \\times 4$ — four tidy bundles and nothing loose.",
                 ["Eq(5*3 + 5, 20)", "Eq(5*4, 20)"]),
            funfact("The five-times table does all the work",
                    "A tally never asks you to count past five. Whatever the pile, the total is $5 \\times \\text{bundles} + \\text{singles}$ — so counting $47$ sheep means skip-counting $5, 10, 15, 20, 25, 30, 35, 40, 45$ and then two single marks. Nine hops and two steps, instead of forty-seven separate counts."),
            withfig(teach("Concept B", "From a count back to tally marks", [
                "Reading multiplies by five, so drawing must DIVIDE by five. To show $%d$: how many fives fit? $%d \\div 5 = %d$ with $%d$ left over." % (n3, n3, b3, s3),
                "The answer counts the bundles and the leftover counts the singles: $%d$ bundles and $%d$ singles." % (b3, s3),
                "Sign the receipt every time: $5 \\times %d + %d = %d$, and $%d$ is fewer than $5$ — so no bundle was left untied." % (b3, s3, n3, s3),
            ]), fig_draw),
            workedset("Drawing a tally",
                      "Divide by five; the leftover must stay under five.", [
                withfig(wex("Draw $%d$ as tally marks." % n3,
                    ["$%d \\div 5 = %d$ with $%d$ left." % (n3, b3, s3),
                     "So $%d$ bundles and $%d$ singles; receipt $5 \\times %d + %d = %d$." % (b3, s3, b3, s3, n3)],
                    "$%d$ bundles, $%d$ singles" % (b3, s3),
                    ["Eq(5*5 + 2, 27)", "2 < 5"]), fig_draw),
                wex("Draw $%d$ as tally marks." % n4,
                    ["$5 \\times %d = %d$ fits inside $%d$." % (b4, 5 * b4, n4),
                     "$%d$ bundles and $%d$ singles; receipt $5 \\times %d + %d = %d$ and $%d < 5$." % (b4, s4, b4, s4, n4, s4)],
                    "$%d$ bundles, $%d$ singles" % (b4, s4),
                    ["Eq(5*7, 35)", "Eq(5*7 + 3, 38)", "3 < 5"]),
            ]),
            tryitset("Parcel it into fives", "Bundles are the answer; singles are the leftover.", [
                tp("Drawn as a tally, $30$ needs:",
                   ["$6$ bundles and no singles", "$5$ bundles and $5$ singles", "$3$ bundles and no singles"],
                   "$30 \\div 5 = 6$ exactly: $6$ bundles, nothing loose, and $5 \\times 6 = 30$ ✓. Five singles would have tied themselves into a sixth bundle.",
                   ["Eq(Rational(30,5), 6)", "Eq(5*6, 30)"]),
                tp("Drawn as a tally, $24$ needs:",
                   ["$4$ bundles and $4$ singles", "$2$ bundles and $4$ singles", "$5$ bundles and $1$ single"],
                   "$5 \\times 4 = 20$ fits, leaving $4$: receipt $5 \\times 4 + 4 = 24$ and $4 < 5$ ✓. Five bundles would already be $25$ — one too many.",
                   ["Eq(5*4 + 4, 24)", "4 < 5", "Eq(5*5, 25)"]),
                tp("Drawn as a tally, $16$ needs:",
                   ["$3$ bundles and $1$ single", "$1$ bundle and $6$ singles", "$4$ bundles and no singles"],
                   "$5 \\times 3 = 15$, leaving $1$: receipt $5 \\times 3 + 1 = 16$ ✓. Six singles break the rule, and four bundles would be $20$.",
                   ["Eq(5*3 + 1, 16)", "1 < 5", "Eq(5*4, 20)"]),
            ]),
            tapq("The leftover rule", "When a count is turned into tally marks, how many single marks can be left over?",
                 ["$0, 1, 2, 3$ or $4$ — never $5$",
                  "any number up to $9$",
                  "always exactly $4$",
                  "as many as there are bundles"],
                 "Singles stop at four because the fifth one strikes across and becomes a bundle: $5 \\times 4 + 4 = 24$ is the busiest a leftover ever gets, and one more mark makes $5 \\times 5 = 25$.",
                 ["Eq(5*4 + 4, 24)", "Eq(5*5, 25)", "4 < 5"]),
            recap([
                "A bundle is four uprights plus a crossing mark: worth exactly 5.",
                "Read a tally as 5 × bundles + singles.",
                "Draw a tally by dividing by 5: bundles are the answer, singles the leftover.",
                "Singles are always fewer than 5 — a fifth single makes a new bundle.",
                "Every reading carries its receipt: the bundles and singles must add back to the count.",
            ]),
            tip("Say the two moves out loud before answering: 'bundles times five' and then 'add the singles'. When you are drawing instead, say 'divide by five' and check that the leftover is under five."),
            tryitset("Mixed practice", "Reading tallies and drawing them.", [
                tp("A tally shows $8$ bundles and $2$ singles. The count is:",
                   ["$42$", "$10$", "$82$"],
                   "$5 \\times 8 = 40$, then $40 + 2 = 42$. The option $10$ added $8 + 2$; $82$ simply wrote the two numbers side by side.",
                   ["Eq(5*8 + 2, 42)", "Eq(8 + 2, 10)"]),
                tp("Drawn as a tally, $45$ needs:",
                   ["$9$ bundles and no singles", "$8$ bundles and $5$ singles", "$4$ bundles and $5$ singles"],
                   "$45 \\div 5 = 9$ exactly, and $5 \\times 9 = 45$ ✓. The other options leave five singles, which always tie into another bundle.",
                   ["Eq(Rational(45,5), 9)", "Eq(5*9, 45)"]),
                withfig(tp("The tally below counted the goats. How many goats?",
                   ["$%d$" % n5, "$%d$" % (b5 + s5), "$%d$" % (5 * b5)],
                   "$5 \\times %d = %d$ from the bundles, then $%d + %d = %d$. The option $%d$ added bundles and singles; $%d$ forgot the singles." % (b5, 5 * b5, 5 * b5, s5, n5, b5 + s5, 5 * b5),
                   ["Eq(5*6 + 3, 33)", "Eq(5*6, 30)", "3 < 5"]), fig_practice),
                tp("Which count is drawn as exactly $4$ bundles and $1$ single?",
                   ["$21$", "$41$", "$5$"],
                   "$5 \\times 4 + 1 = 21$. The option $41$ read the bundles as tens; $5$ added $4 + 1$.",
                   ["Eq(5*4 + 1, 21)", "1 < 5"]),
                tp("One tally shows $5$ bundles and $1$ single, another shows $4$ bundles and $4$ singles. The first is bigger by:",
                   ["$2$", "$1$", "$3$"],
                   "The tallies read $5 \\times 5 + 1 = 26$ and $5 \\times 4 + 4 = 24$; $26 - 24 = 2$, and adding back $2 + 24 = 26$ ✓. Counting only the bundles would wrongly say $1$.",
                   ["Eq(5*5 + 1, 26)", "Eq(5*4 + 4, 24)", "Eq(26 - 24, 2)", "Eq(2 + 24, 26)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tally Marks\"",
                    "Bundles of five, singles under five, and a receipt on every reading: the first place where a mark stands for something counted. Next, those counts move into a table — where the total row becomes the receipt for the whole page.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Tables & Totals
# ==========================================================================

def lesson_tables():
    # Frequency table 1: favourite animal, a class of 34.
    a1, a2, a3, a4 = 12, 9, 8, 5
    tot1 = a1 + a2 + a3 + a4          # 34
    # Missing-row table: four days of visitors, total known.
    d1, d2, d3, tot2 = 9, 11, 7, 40
    d4 = tot2 - (d1 + d2 + d3)        # 13
    # Chapter-practice table.
    p1, p2, p3 = 21, 13, 6
    ptot = p1 + p2 + p3               # 40
    fig_animals = fig_groups((a1, "horse"), (a2, "sheep"),
                             (a3, "goat"), (a4, "camel"))
    fig_days = fig_groups((d1, "Monday"), (d2, "Tuesday"),
                          (d3, "Wednesday"), (d4, "Thursday"))
    fig_practice = fig_groups((p1, "buuz"), (p2, "khuushuur"), (p3, "aaruul"))
    return {
        "slug": "tables-and-totals",
        "title": "Tables & Totals",
        "concreteComparison": (
            "A shopkeeper keeps a book: one line for each thing sold, "
            "with its count beside it. At closing time she adds the "
            "lines, and the sum must match what is in the till — if it "
            "does not, something was written down wrong. A frequency "
            "table works exactly the same way. The total row is not "
            "decoration; it is the receipt for every row above it."),
        "objective": (
            "Build a frequency table from tallies, check that the rows "
            "re-add to the total, and find a missing row when the "
            "total is known."),
        "concept": [
            "**A frequency table gives every group one row and one "
            "count.** The left column names the group (horse, sheep, "
            "goat, camel), the right column says how many chose it. "
            "Tally marks in a table are just counts wearing their "
            "working clothes.",
            "**The total is a receipt.** Add every row and you must "
            "land on the total: $12 + 9 + 8 + 5 = 34$. If the rows do "
            "not re-add, either a row or the total is wrong — the "
            "table tells you to look again.",
            "**A missing row falls out of the total.** Take ALL the "
            "known rows off the total: $40 - 9 - 11 - 7 = 13$. Then "
            "add back to be sure: $13 + 27 = 40$ ✓.",
        ],
        "keyIdea": (
            "Every row of a table is a count, and the total row is the "
            "receipt: the rows must add back to it. That one rule both "
            "checks a finished table and finds a row that is missing."),
        "facts": [
            {"title": "Rows re-add to the total",
             "latex": "12 + 9 + 8 + 5 = 34",
             "explanation": "The total row is the sum of the group rows — never a group of its own."},
            {"title": "A missing row",
             "latex": "40 - 9 - 11 - 7 = 13",
             "explanation": "Total minus every known row; add all four back to check you land on 40."},
        ],
        "workedExamples": [
            {"id": "g4da-l2-we1",
             "statement": "A class chose a favourite animal: horse $12$, sheep $9$, goat $8$, camel $5$. How many children are in the class?",
             "note": "The total row is the sum of the group rows.",
             "solution": ("Add the rows in easy steps: $12 + 9 = 21$, then $21 + 8 = "
                          "29$, then $29 + 5 = 34$. The class has $34$ children, and "
                          "$12 + 9 + 8 + 5 = 34$ is the receipt for the whole table."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12 + 9, 21)", "Eq(21 + 8, 29)", "Eq(29 + 5, 34)",
                       "Eq(12 + 9 + 8 + 5, 34)"]},
            {"id": "g4da-l2-we2",
             "statement": "A museum counted visitors on four days. Monday $9$, Tuesday $11$, Wednesday $7$, Thursday unknown; the total for the four days is $40$. How many came on Thursday?",
             "note": "Every known row comes off the total first.",
             "solution": ("The three known rows make $9 + 11 + 7 = 27$. Take that off "
                          "the total: $40 - 27 = 13$ visitors on Thursday. Add back to "
                          "check: $13 + 27 = 40$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(9 + 11 + 7, 27)", "Eq(40 - 27, 13)", "Eq(13 + 27, 40)"]},
        ],
        "commonMistakes": [
            {"text": "Adding the total row in with the groups, so the data is counted twice.",
             "correction": "The total is the SUM of the rows, not another row. With rows 14, 11 and 6 the total is 31 — adding 31 in again gives 62, exactly double.",
             "authored": True},
            {"text": "Finding a missing row by taking only one known row off the total.",
             "correction": "All the known rows come off: 40 - 9 - 11 - 7 = 13, not 40 - 9 = 31. The add-back check 13 + 9 + 11 + 7 = 40 catches this instantly.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4da-l2-t1",
             "statement": "A table of favourite drinks has rows: tea $7$, milk $6$, water $9$. How many children were asked?",
             "solution": "$7 + 6 = 13$, then $13 + 9 = 22$ children. The receipt: $7 + 6 + 9 = 22$.",
             "check": ["Eq(7 + 6, 13)", "Eq(7 + 6 + 9, 22)"]},
            {"id": "g4da-l2-t2",
             "statement": "A table has three rows and a total of $30$. Two rows read $8$ and $12$. What is the third row?",
             "solution": "Known rows: $8 + 12 = 20$. Missing row: $30 - 20 = 10$. Check: $10 + 20 = 30$ ✓.",
             "check": ["Eq(8 + 12, 20)", "Eq(30 - 20, 10)", "Eq(10 + 20, 30)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Rows, counts, and the receipt at the bottom", [
                "A frequency table gives each group its own row: horse $%d$, sheep $%d$, goat $%d$, camel $%d$. The word 'frequency' just means how many times that answer came up." % (a1, a2, a3, a4),
                "Under the rows sits the TOTAL. It is the sum of the rows and nothing else: $%d + %d + %d + %d = %d$." % (a1, a2, a3, a4, tot1),
                "That makes the total a receipt. Every time you finish a table, add the rows and see whether they land on it — a table whose rows do not re-add is telling you something was miscounted.",
            ]), fig_animals),
            workedset("Building the total",
                      "Add the rows in easy steps, then read the receipt.", [
                withfig(wex("Horse $%d$, sheep $%d$, goat $%d$, camel $%d$. How many children?" % (a1, a2, a3, a4),
                    ["$%d + %d = %d$, then $%d + %d = %d$." % (a1, a2, a1 + a2, a1 + a2, a3, a1 + a2 + a3),
                     "One more row: $%d + %d = %d$ children." % (a1 + a2 + a3, a4, tot1)],
                    "$%d$" % tot1,
                    ["Eq(12 + 9, 21)", "Eq(21 + 8, 29)", "Eq(12 + 9 + 8 + 5, 34)"]), fig_animals),
                wex("Three rows arrive as tallies: $3$ bundles and $2$ singles, $2$ bundles and $4$ singles, $1$ bundle and $1$ single. Turn them into numbers and total them.",
                    ["Read each tally: $5 \\times 3 + 2 = 17$, $5 \\times 2 + 4 = 14$, $5 \\times 1 + 1 = 6$.",
                     "Total the rows: $17 + 14 + 6 = 37$."],
                    "$17$, $14$, $6$ — total $37$",
                    ["Eq(5*3 + 2, 17)", "Eq(5*2 + 4, 14)", "Eq(5*1 + 1, 6)",
                     "Eq(17 + 14 + 6, 37)"]),
            ]),
            tryitset("Add the rows", "The total is whatever the rows make together.", [
                tp("A table has rows $15$, $12$ and $9$. The total is:",
                   ["$36$", "$27$", "$34$"],
                   "$15 + 12 = 27$, then $27 + 9 = 36$. The option $27$ stopped after two rows and never added the third.",
                   ["Eq(15 + 12, 27)", "Eq(27 + 9, 36)"]),
                tp("A table has rows $20$, $14$, $6$ and $10$. The total is:",
                   ["$50$", "$40$", "$44$"],
                   "$20 + 14 = 34$, $34 + 6 = 40$, $40 + 10 = 50$. The option $40$ left the last row out.",
                   ["Eq(20 + 14, 34)", "Eq(20 + 14 + 6 + 10, 50)"]),
                tp("A table's rows read $11$, $9$ and $14$, and the total row says $32$. The table is:",
                   ["wrong — the rows add to $34$", "right — $32$ is close enough", "wrong — the rows add to $30$"],
                   "$11 + 9 + 14 = 34$, and $34$ is not $32$: the receipt fails, so a row or the total was written down wrong. Totals are exact, never approximate.",
                   ["Eq(11 + 9 + 14, 34)", "Ne(34, 32)"]),
            ]),
            tapq("The total is not a group", "A table lists sheep $14$, goats $11$, horses $6$, and a total row of $31$. A student adds all four numbers and gets $62$. What went wrong?",
                 ["the total row was added in as if it were a group — the three rows alone make $31$",
                  "the total row should have been $62$ all along",
                  "the rows were added in the wrong order",
                  "one of the groups was counted twice by the surveyor"],
                 "The three group rows are the data: $14 + 11 + 6 = 31$. Adding the total row back in counts every child a second time, which is why the answer came out as $31 + 31 = 62$ — exactly double.",
                 ["Eq(14 + 11 + 6, 31)", "Eq(31 + 31, 62)"]),
            funfact("Any order, same total",
                    "You may add the rows of a table in any order you like and the total never changes: $12 + 9 + 8 + 5$ and $5 + 8 + 9 + 12$ both land on $34$. That is why adding a column downwards and then upwards is a real check — two different roads that must arrive at the same place, so a slip on one road shows up straight away."),
            withfig(teach("Concept B", "Finding a row that is missing", [
                "Sometimes the total is known but one row is blank. Monday $%d$, Tuesday $%d$, Wednesday $%d$, Thursday empty, total $%d$." % (d1, d2, d3, tot2),
                "Add the rows you CAN see: $%d + %d + %d = %d$. Then take them off the total: $%d - %d = %d$ visitors on Thursday." % (d1, d2, d3, d1 + d2 + d3, tot2, d1 + d2 + d3, d4),
                "Add back to be sure: $%d + %d = %d$ ✓. The receipt that checked a finished table is the same receipt that fills in a missing row." % (d4, d1 + d2 + d3, tot2),
            ]), fig_days),
            workedset("Total minus the known rows",
                      "Every visible row comes off; then add back to check.", [
                withfig(wex("Monday $%d$, Tuesday $%d$, Wednesday $%d$, total $%d$. Find Thursday." % (d1, d2, d3, tot2),
                    ["Known rows: $%d + %d + %d = %d$." % (d1, d2, d3, d1 + d2 + d3),
                     "$%d - %d = %d$, and the add-back $%d + %d = %d$ ✓." % (tot2, d1 + d2 + d3, d4, d4, d1 + d2 + d3, tot2)],
                    "$%d$ visitors" % d4,
                    ["Eq(9 + 11 + 7, 27)", "Eq(40 - 27, 13)", "Eq(13 + 27, 40)"]), fig_days),
                wex("A table of four sports totals $60$: wrestling $18$, horse racing $24$, archery $12$, and one blank row. Fill it.",
                    ["Known rows: $18 + 24 + 12 = 54$.",
                     "$60 - 54 = 6$, and $6 + 54 = 60$ ✓."],
                    "$6$",
                    ["Eq(18 + 24 + 12, 54)", "Eq(60 - 54, 6)", "Eq(6 + 54, 60)"]),
            ]),
            tryitset("Fill the blank row", "Take off every known row, then add back.", [
                tp("Three rows total $25$. Two of them are $7$ and $8$. The third row is:",
                   ["$10$", "$18$", "$15$"],
                   "$7 + 8 = 15$ known, so $25 - 15 = 10$, and $10 + 15 = 25$ ✓. The option $18$ took only the $7$ off the total.",
                   ["Eq(7 + 8, 15)", "Eq(25 - 15, 10)", "Eq(10 + 15, 25)"]),
                tp("Four rows total $48$. Three of them are $12$, $15$ and $9$. The fourth row is:",
                   ["$12$", "$36$", "$21$"],
                   "$12 + 15 + 9 = 36$ known, so $48 - 36 = 12$, checked by $12 + 36 = 48$ ✓. The option $36$ answered with the known rows instead of the blank one.",
                   ["Eq(12 + 15 + 9, 36)", "Eq(48 - 36, 12)", "Eq(12 + 36, 48)"]),
                tp("A total of $40$ has known rows $9$, $11$ and $7$, and the blank is filled in as $13$. Which check proves it?",
                   ["add all four rows: $9 + 11 + 7 + 13 = 40$", "check that $13$ is smaller than $40$", "check that $13$ is bigger than $9$"],
                   "A filled row is right only if the whole table re-adds to the total: $9 + 11 + 7 + 13 = 40$ ✓. Being smaller than the total is true of every row, so it proves nothing.",
                   ["Eq(9 + 11 + 7 + 13, 40)"]),
            ]),
            tapq("Read the blank", "A table of three rows totals $36$. Two rows read $14$ and $9$. The third row is:",
                 ["$13$", "$23$", "$22$", "$45$"],
                 "Known rows: $14 + 9 = 23$; the blank is $36 - 23 = 13$, checked by $13 + 23 = 36$ ✓. The option $23$ is the known rows themselves, and $45$ added the total to a row instead of subtracting.",
                 ["Eq(14 + 9, 23)", "Eq(36 - 23, 13)", "Eq(13 + 23, 36)"]),
            recap([
                "Each group gets one row; the number beside it is its frequency.",
                "The total row is the sum of the group rows and never a group itself.",
                "Rows that do not re-add to the total mean something was miscounted.",
                "A missing row = total minus ALL the known rows.",
                "Add back every time: the filled table must land on its total.",
            ]),
            tip("Whenever a table appears, add its rows once before answering anything. If they land on the total, you can trust every number on the page; if they do not, you have found the mistake before it found you."),
            tryitset("Mixed practice", "Totals, tallies, and missing rows.", [
                withfig(tp("A stall's table reads buuz $%d$, khuushuur $%d$, aaruul $%d$. Altogether it sold:" % (p1, p2, p3),
                   ["$%d$" % ptot, "$%d$" % (p1 + p2), "$%d$" % (p2 + p3)],
                   "$%d + %d = %d$, then $%d + %d = %d$. The option $%d$ stopped after two rows." % (p1, p2, p1 + p2, p1 + p2, p3, ptot, p1 + p2),
                   ["Eq(21 + 13, 34)", "Eq(34 + 6, 40)", "Eq(21 + 13 + 6, 40)"]), fig_practice),
                tp("Four rows total $45$. Three read $12$, $18$ and $7$. The fourth is:",
                   ["$8$", "$37$", "$13$"],
                   "$12 + 18 + 7 = 37$ known, so $45 - 37 = 8$, and $8 + 37 = 45$ ✓. The option $37$ gave the known rows back.",
                   ["Eq(12 + 18 + 7, 37)", "Eq(45 - 37, 8)", "Eq(8 + 37, 45)"]),
                tp("One row arrives as a tally of $4$ bundles and $2$ singles; the other row is $13$. The total is:",
                   ["$35$", "$19$", "$28$"],
                   "Read the tally first: $5 \\times 4 + 2 = 22$. Then $22 + 13 = 35$. The option $19$ added $4 + 2 + 13$, treating bundles as single marks.",
                   ["Eq(5*4 + 2, 22)", "Eq(22 + 13, 35)", "Eq(4 + 2 + 13, 19)"]),
                tp("A table's rows read $16$, $9$ and $12$, and the total row says $38$. The table is:",
                   ["wrong — the rows make $37$", "right", "wrong — the rows make $36$"],
                   "$16 + 9 = 25$ and $25 + 12 = 37$, which is one short of the printed $38$. The rows are the data, so the total row must be corrected.",
                   ["Eq(16 + 9, 25)", "Eq(16 + 9 + 12, 37)", "Ne(37, 38)"]),
                tp("A table has rows $10$, $10$ and $10$, and someone claims the total is $30$ because the rows are equal. This is:",
                   ["right — $3 \\times 10 = 30$, the same as adding them", "wrong — equal rows cannot be multiplied", "wrong — the total is $103$"],
                   "Adding equal rows is exactly what multiplication does: $10 + 10 + 10 = 30$ and $3 \\times 10 = 30$ agree. The shortcut is legal only because every row is the same size.",
                   ["Eq(10 + 10 + 10, 30)", "Eq(3*10, 30)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Tables & Totals\"",
                    "Rows, a total that acts as a receipt, and a blank row that the receipt fills in for you. Next, the same counts become a picture — where one little symbol stands for two, five or ten of the things counted.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Pictographs
# ==========================================================================

def lesson_pictographs():
    # Reading with a key of 5.
    key_a = 5
    sym_mon, sym_tue, sym_wed = 6, 4, 5
    val_mon = sym_mon * key_a          # 30
    val_tue = sym_tue * key_a          # 20
    val_wed = sym_wed * key_a          # 25
    # Reading with a key of 2.
    key_b, sym_b, val_b = 2, 7, 14
    # Drawing: 35 with key 5, and 45 with key 10 (four and a half symbols).
    draw_n, draw_sym = 35, 7
    key_c, half_full, half_val = 10, 4, 45
    fig_week = fig_groups((sym_mon, "symbols — Monday"),
                          (sym_tue, "symbols — Tuesday"),
                          (sym_wed, "symbols — Wednesday"))
    fig_two_days = fig_groups((sym_mon, "symbols — Monday"),
                              (sym_tue, "symbols — Tuesday"))
    fig_draw = fig_groups((draw_sym, "symbols — %d in all" % draw_n, C_GREEN))
    fig_half = fig_groups((half_full, "full symbols — %d each" % key_c, C_ACCENT),
                          (1, "half symbol — %d" % (key_c // 2), C_WARM))
    fig_practice = fig_groups((7, "symbols — Saturday"), (4, "symbols — Sunday"))
    return {
        "slug": "pictographs",
        "title": "Pictographs",
        "concreteComparison": (
            "A pictograph is a picture that makes a promise: one little "
            "sheep drawn on the page stands for FIVE real sheep out on "
            "the steppe. The key at the bottom of the chart is that "
            "promise written down. Read the key first and a row of six "
            "symbols becomes $30$ sheep; ignore it and every number you "
            "take off the chart is wrong."),
        "objective": (
            "Read a pictograph by multiplying symbols by the key, draw "
            "one by dividing the count by the key, and use a half "
            "symbol for half the key."),
        "concept": [
            "**The key says what one symbol is worth.** It might be "
            "$2$, $5$ or $10$. The key is part of the chart, not a "
            "decoration — the same row of symbols means different "
            "numbers under different keys.",
            "**Read by multiplying.** Count the symbols in the row and "
            "multiply by the key: $6$ symbols with a key of $5$ is "
            "$6 \\times 5 = 30$. Never answer with the number of "
            "symbols by itself.",
            "**Draw by dividing, and use a half symbol for half the "
            "key.** To show $35$ with a key of $5$: $35 \\div 5 = 7$ "
            "symbols. With a key of $10$, the number $45$ needs $4$ "
            "full symbols and a half one, because half of $10$ is $5$: "
            "$4 \\times 10 + 5 = 45$.",
        ],
        "keyIdea": (
            "One symbol is worth the key. Reading multiplies symbols by "
            "the key, drawing divides the count by the key, and a half "
            "symbol carries half the key — every row still adds back to "
            "the number it stands for."),
        "facts": [
            {"title": "Reading a row",
             "latex": "6 \\ \\text{symbols} \\times 5 = 30",
             "explanation": "Symbols counted, then multiplied by the key — the key never gets left out."},
            {"title": "Drawing a row",
             "latex": "35 \\div 5 = 7 \\ \\text{symbols}",
             "explanation": "Divide the count by the key; the answer is how many symbols to draw."},
        ],
        "workedExamples": [
            {"id": "g4da-l3-we1",
             "statement": "A pictograph of visitors has the key: one symbol $= 5$ visitors. Monday shows $6$ symbols and Tuesday shows $4$. How many visitors each day, and how many more came on Monday?",
             "note": "Multiply each row by the key before comparing anything.",
             "solution": ("Monday: $6 \\times 5 = 30$ visitors. Tuesday: $4 \\times 5 = "
                          "20$ visitors. Monday had $30 - 20 = 10$ more, and the "
                          "add-back $10 + 20 = 30$ ✓ confirms it. Comparing the "
                          "symbols alone would have said $2$ — but each of those "
                          "symbols is worth five."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6*5, 30)", "Eq(4*5, 20)", "Eq(30 - 20, 10)", "Eq(10 + 20, 30)"]},
            {"id": "g4da-l3-we2",
             "statement": "Draw $45$ sheep on a pictograph whose key is: one symbol $= 10$ sheep.",
             "note": "Divide by the key; a leftover of half the key becomes a half symbol.",
             "solution": ("$45 \\div 10 = 4$ with $5$ left over. That leftover is "
                          "exactly half of the key ($10 \\div 2 = 5$), so it is drawn "
                          "as a half symbol: $4$ full symbols and a half. Receipt: "
                          "$4 \\times 10 + 5 = 45$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(10,2), 5)", "Eq(4*10 + 5, 45)", "5 < 10"]},
        ],
        "commonMistakes": [
            {"text": "Counting the symbols and calling that the answer — reading a row of 6 symbols as 6.",
             "correction": "Each symbol carries the key. With a key of 5 that row is 6 × 5 = 30, and with a key of 10 the same row is 6 × 10 = 60.",
             "authored": True},
            {"text": "Reading a half symbol as 1.",
             "correction": "A half symbol is worth half the KEY: with a key of 10 it stands for 5, so 3 full symbols and a half is 3 × 10 + 5 = 35, not 31.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4da-l3-t1",
             "statement": "One symbol $= 2$ books. A row shows $9$ symbols. How many books?",
             "solution": "$9 \\times 2 = 18$ books. The row holds nine symbols, but each is worth two.",
             "check": ["Eq(9*2, 18)"]},
            {"id": "g4da-l3-t2",
             "statement": "One symbol $= 5$ goats. How many symbols do you draw to show $30$ goats?",
             "solution": "$30 \\div 5 = 6$ symbols, checked by $6 \\times 5 = 30$ ✓.",
             "check": ["Eq(Rational(30,5), 6)", "Eq(6*5, 30)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The key is the promise", [
                "A pictograph draws one symbol for every few things counted, and the KEY at the bottom says how many. Here the key is: one symbol $= %d$ visitors." % key_a,
                "Read a row by multiplying: Monday's $%d$ symbols are $%d \\times %d = %d$ visitors; Tuesday's $%d$ symbols are $%d \\times %d = %d$." % (sym_mon, sym_mon, key_a, val_mon, sym_tue, sym_tue, key_a, val_tue),
                "Wednesday shows $%d$ symbols: $%d \\times %d = %d$. Same picture, always the same move — count the symbols, then multiply by the key." % (sym_wed, sym_wed, key_a, val_wed),
            ]), fig_week),
            workedset("Reading rows",
                      "Count the symbols, then multiply by the key.", [
                withfig(wex("Key: one symbol $= %d$. Monday shows $%d$ symbols, Tuesday shows $%d$. How many each day?" % (key_a, sym_mon, sym_tue),
                    ["Monday: $%d \\times %d = %d$." % (sym_mon, key_a, val_mon),
                     "Tuesday: $%d \\times %d = %d$." % (sym_tue, key_a, val_tue)],
                    "$%d$ and $%d$" % (val_mon, val_tue),
                    ["Eq(6*5, 30)", "Eq(4*5, 20)"]), fig_two_days),
                wex("Key: one symbol $= %d$ books. A shelf row shows $%d$ symbols. How many books?" % (key_b, sym_b),
                    ["Each symbol is worth $%d$." % key_b,
                     "$%d \\times %d = %d$ books." % (sym_b, key_b, val_b)],
                    "$%d$" % val_b,
                    ["Eq(7*2, 14)"]),
            ]),
            tryitset("Multiply by the key", "The symbols are counted; the key does the rest.", [
                tp("Key: one symbol $= 10$. A row of $3$ symbols stands for:",
                   ["$30$", "$3$", "$13$"],
                   "$3 \\times 10 = 30$. The option $3$ counted symbols and forgot the key; $13$ added the key instead of multiplying by it.",
                   ["Eq(3*10, 30)", "Eq(3 + 10, 13)"]),
                tp("Key: one symbol $= 5$. A row of $8$ symbols stands for:",
                   ["$40$", "$8$", "$13$"],
                   "$8 \\times 5 = 40$. The option $13$ came from adding $8 + 5$ rather than multiplying.",
                   ["Eq(8*5, 40)", "Eq(8 + 5, 13)"]),
                tp("Key: one symbol $= 2$. A row of $7$ symbols stands for:",
                   ["$14$", "$7$", "$9$"],
                   "$7 \\times 2 = 14$. With the smallest key the picture is longest, but the move never changes: symbols times key.",
                   ["Eq(7*2, 14)", "Eq(7 + 2, 9)"]),
            ]),
            tapq("Never answer with the symbols", "A pictograph of goats has the key: one symbol $= 5$ goats. A row shows $9$ symbols. How many goats?",
                 ["$45$", "$9$", "$14$", "$50$"],
                 "$9 \\times 5 = 45$ goats. The option $9$ counted symbols; $14$ added $9 + 5$; $50$ is $10 \\times 5$, one symbol too many.",
                 ["Eq(9*5, 45)", "Eq(9 + 5, 14)", "Eq(10*5, 50)"]),
            funfact("One picture, three different numbers",
                    "The very same row of $6$ symbols means $12$ under a key of $2$, $30$ under a key of $5$, and $60$ under a key of $10$. The drawing never changes — the key changes everything. That is why a pictograph without its key is not data at all, just decoration."),
            withfig(teach("Concept B", "Drawing rows, and the half symbol", [
                "Drawing runs the reading backwards: divide the count by the key. To show $%d$ with a key of $%d$: $%d \\div %d = %d$ symbols." % (draw_n, key_a, draw_n, key_a, draw_sym),
                "Sometimes the count does not land on a whole symbol. With a key of $%d$, the number $%d$ gives $%d$ full symbols and $%d$ left over — and $%d$ is exactly half of $%d$." % (key_c, half_val, half_full, half_val - half_full * key_c, key_c // 2, key_c),
                "So you draw HALF a symbol for it: $%d$ full symbols and a half, and the receipt $%d \\times %d + %d = %d$ ✓ proves the row still says what it should." % (half_full, half_full, key_c, key_c // 2, half_val),
            ]), fig_half),
            workedset("Drawing rows",
                      "Divide by the key; half the key becomes half a symbol.", [
                withfig(wex("Key: one symbol $= %d$. How many symbols show $%d$?" % (key_a, draw_n),
                    ["$%d \\div %d = %d$." % (draw_n, key_a, draw_sym),
                     "Draw $%d$ symbols; check by reading back: $%d \\times %d = %d$ ✓." % (draw_sym, draw_sym, key_a, draw_n)],
                    "$%d$ symbols" % draw_sym,
                    ["Eq(Rational(35,5), 7)", "Eq(7*5, 35)"]), fig_draw),
                withfig(wex("Key: one symbol $= %d$. How do you show $%d$?" % (key_c, half_val),
                    ["$%d \\div %d = %d$ with $%d$ left; $%d$ is half of $%d$." % (half_val, key_c, half_full, key_c // 2, key_c // 2, key_c),
                     "So $%d$ full symbols and one half symbol: $%d \\times %d + %d = %d$ ✓." % (half_full, half_full, key_c, key_c // 2, half_val)],
                    "$%d$ full symbols and a half" % half_full,
                    ["Eq(Rational(10,2), 5)", "Eq(4*10 + 5, 45)", "5 < 10"]), fig_half),
            ]),
            tryitset("Divide to draw", "Count divided by key = symbols drawn.", [
                tp("Key: one symbol $= 5$. To show $25$ you draw:",
                   ["$5$ symbols", "$25$ symbols", "$20$ symbols"],
                   "$25 \\div 5 = 5$ symbols, checked by $5 \\times 5 = 25$ ✓. Drawing $25$ symbols would show $25 \\times 5 = 125$.",
                   ["Eq(Rational(25,5), 5)", "Eq(5*5, 25)"]),
                tp("Key: one symbol $= 10$. To show $70$ you draw:",
                   ["$7$ symbols", "$70$ symbols", "$60$ symbols"],
                   "$70 \\div 10 = 7$ symbols, checked by $7 \\times 10 = 70$ ✓.",
                   ["Eq(Rational(70,10), 7)", "Eq(7*10, 70)"]),
                tp("Key: one symbol $= 2$. To show $9$ you draw:",
                   ["$4$ symbols and a half", "$9$ symbols", "$5$ symbols"],
                   "$9 \\div 2 = 4$ with $1$ left, and $1$ is half of the key $2$ — so four symbols and a half: $4 \\times 2 + 1 = 9$ ✓. Five whole symbols would say $10$.",
                   ["Eq(Rational(2,2), 1)", "Eq(4*2 + 1, 9)", "Eq(5*2, 10)"]),
            ]),
            tapq("Half a symbol, half the key", "One symbol $= 10$ sheep. A row shows $3$ full symbols and one half symbol. The row stands for:",
                 ["$35$", "$31$", "$30$", "$13$"],
                 "The full symbols give $3 \\times 10 = 30$; the half symbol is worth half the key, $10 \\div 2 = 5$; together $30 + 5 = 35$. The option $31$ counted the half symbol as $1$, and $30$ ignored it altogether.",
                 ["Eq(3*10, 30)", "Eq(Rational(10,2), 5)", "Eq(30 + 5, 35)"]),
            recap([
                "The key says what one symbol is worth: 2, 5 or 10.",
                "Read a row by multiplying: symbols × key.",
                "Draw a row by dividing: count ÷ key = symbols.",
                "A half symbol is worth half the key, not 1.",
                "Every row reads back to the number it stands for — that is the receipt.",
            ]),
            tip("Find the key before you look at a single row, and say it out loud: 'one symbol is five'. Almost every mistake on a pictograph is made by someone who answered before reading the key."),
            tryitset("Mixed practice", "Reading, drawing, half symbols, and finding the key.", [
                withfig(tp("Key: one symbol $= 5$ tickets. Saturday shows $7$ symbols and Sunday shows $4$. Saturday sold more by:",
                   ["$15$ tickets", "$3$ tickets", "$35$ tickets"],
                   "Read both rows first: $7 \\times 5 = 35$ and $4 \\times 5 = 20$; the gap is $35 - 20 = 15$, checked by $15 + 20 = 35$ ✓. The option $3$ compared the symbols instead of the tickets.",
                   ["Eq(7*5, 35)", "Eq(4*5, 20)", "Eq(35 - 20, 15)", "Eq(15 + 20, 35)"]), fig_practice),
                tp("Key: one symbol $= 2$ litres. A row of $8$ symbols stands for:",
                   ["$16$ litres", "$8$ litres", "$10$ litres"],
                   "$8 \\times 2 = 16$ litres. The option $10$ added the key on instead of multiplying by it.",
                   ["Eq(8*2, 16)", "Eq(8 + 2, 10)"]),
                tp("Key: one symbol $= 10$. To show $60$ you draw:",
                   ["$6$ symbols", "$60$ symbols", "$16$ symbols"],
                   "$60 \\div 10 = 6$ symbols, checked by $6 \\times 10 = 60$ ✓.",
                   ["Eq(Rational(60,10), 6)", "Eq(6*10, 60)"]),
                tp("Key: one symbol $= 2$. A row shows $5$ full symbols and one half symbol. It stands for:",
                   ["$11$", "$10$", "$6$"],
                   "$5 \\times 2 = 10$ from the full symbols, plus half the key ($2 \\div 2 = 1$): $10 + 1 = 11$. The option $10$ dropped the half symbol.",
                   ["Eq(5*2, 10)", "Eq(Rational(2,2), 1)", "Eq(10 + 1, 11)"]),
                tp("On a pictograph a row of $4$ symbols stands for $40$. The key must be:",
                   ["one symbol $= 10$", "one symbol $= 4$", "one symbol $= 5$"],
                   "The key is the value shared out over the symbols: $40 \\div 4 = 10$, checked by $4 \\times 10 = 40$ ✓. A key of $5$ would make that row only $4 \\times 5 = 20$.",
                   ["Eq(Rational(40,4), 10)", "Eq(4*10, 40)", "Eq(4*5, 20)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Pictographs\"",
                    "A key, a multiplication to read and a division to draw — and every row still adding back to the count it stands for. Next, the symbols become solid bars, and the key becomes a scale up the side of the chart.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Bar Charts
# ==========================================================================

def lesson_bars():
    # Scale stepping by 5.
    step_a = 5
    lines_w, lines_a = 4, 3
    val_w, val_a = lines_w * step_a, lines_a * step_a   # 20, 15
    # Scale stepping by 2 — including a bar between two gridlines.
    step_b = 2
    lines_b = 3
    val_b = lines_b * step_b                            # 6
    mid_lo, mid_hi, mid = 6, 8, 7
    # Comparing two bars.
    tall, short = 20, 14
    diff = tall - short                                 # 6
    fig_bars = fig_groups((val_w, "wrestling — %d lines of %d" % (lines_w, step_a), C_ACCENT),
                          (val_a, "archery — %d lines of %d" % (lines_a, step_a), C_WARM))
    fig_compare = fig_groups((tall, "Monday", C_ACCENT), (short, "Tuesday", C_GREEN))
    fig_practice = fig_groups((22, "Saturday", C_ACCENT), (16, "Sunday", C_WARM))
    return {
        "slug": "bar-charts",
        "title": "Bar Charts",
        "concreteComparison": (
            "Bar charts are tally bundles standing up. The taller the "
            "bar, the more there were — but HOW MUCH more depends "
            "entirely on the numbers written up the left-hand side. On "
            "a chart whose lines step by $5$, a bar four lines high is "
            "$20$; on a chart whose lines step by $1$, the very same "
            "bar is only $4$. Read the side before you read the bar."),
        "objective": (
            "Read bar heights on scales stepping by $1$, $2$ and $5$, "
            "read a bar that stops halfway between two lines, and "
            "compare two bars with a subtraction that adds back."),
        "concept": [
            "**Read the scale before the bar.** The numbers up the "
            "side tell you what one gridline is worth — the STEP. In "
            "this topic a step is always $1$, $2$ or $5$, and it is "
            "written on the chart for you to find.",
            "**A bar's value is lines times step.** A bar reaching the "
            "fourth line on a step-of-$5$ chart is $4 \\times 5 = 20$. "
            "If a bar stops halfway between two lines, it is worth the "
            "number halfway between them: between $6$ and $8$ sits "
            "$7$.",
            "**Compare bars by subtracting, then add back.** 'How many "
            "more?' is never the taller bar's value: it is the gap. "
            "$20 - 14 = 6$, and the check $6 + 14 = 20$ ✓ proves the "
            "gap is right.",
        ],
        "keyIdea": (
            "A bar is worth lines $\\times$ step, so the scale must be "
            "read first. Comparing bars is subtraction, and the "
            "difference added back to the shorter bar must rebuild the "
            "taller one."),
        "facts": [
            {"title": "Height in numbers",
             "latex": "4 \\ \\text{lines} \\times 5 = 20",
             "explanation": "Count the gridlines the bar reaches, then multiply by the step written on the scale."},
            {"title": "How many more",
             "latex": "20 - 14 = 6 \\quad (6 + 14 = 20)",
             "explanation": "The difference is the gap between the bars, and adding it back must rebuild the taller one."},
        ],
        "workedExamples": [
            {"id": "g4da-l4-we1",
             "statement": "On a bar chart whose side numbers go $0, 5, 10, 15, 20$, the wrestling bar reaches the $4$th line and the archery bar reaches the $3$rd. Read both bars and say how many more chose wrestling.",
             "note": "The step is 5, so each gridline is worth five.",
             "solution": ("Wrestling: $4 \\times 5 = 20$. Archery: $3 \\times 5 = 15$. "
                          "The gap is $20 - 15 = 5$, checked by $5 + 15 = 20$ ✓. "
                          "Counting gridlines alone would have said $1$ — but each "
                          "line is worth five children."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*5, 20)", "Eq(3*5, 15)", "Eq(20 - 15, 5)", "Eq(5 + 15, 20)"]},
            {"id": "g4da-l4-we2",
             "statement": "On a chart whose side numbers step by $2$, one bar reaches the $3$rd line and another stops exactly halfway between the lines marked $6$ and $8$. Read both bars.",
             "note": "A bar between two lines takes the number between them.",
             "solution": ("The first bar: $3 \\times 2 = 6$. The second stops halfway "
                          "between $6$ and $8$, so it is worth $(6 + 8) \\div 2 = 7$ "
                          "— one more than $6$ and one less than $8$. Odd numbers "
                          "live between the lines on a step-of-two chart."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*2, 6)", "Eq(Rational(6 + 8, 2), 7)", "6 < 7", "7 < 8"]},
        ],
        "commonMistakes": [
            {"text": "Counting gridlines as ones on every chart.",
             "correction": "Read the numbers on the side first. If the lines step by 5, a bar four lines high is 4 × 5 = 20, not 4.",
             "authored": True},
            {"text": "Answering \"how many more?\" with the taller bar's value.",
             "correction": "How many MORE is the gap between the bars: 20 - 14 = 6. The add-back 6 + 14 = 20 proves the gap; answering 20 would be the whole bar, not the difference.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4da-l4-t1",
             "statement": "On a chart stepping by $2$, a bar reaches the $5$th line. What does it stand for?",
             "solution": "$5 \\times 2 = 10$. Five lines, each worth two.",
             "check": ["Eq(5*2, 10)"]},
            {"id": "g4da-l4-t2",
             "statement": "One bar stands for $18$ and another for $12$. How many more does the first show?",
             "solution": "$18 - 12 = 6$ more, checked by $6 + 12 = 18$ ✓.",
             "check": ["Eq(18 - 12, 6)", "Eq(6 + 12, 18)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The scale decides what a bar is worth", [
                "Up the left side of a bar chart runs a scale. Here it reads $0, 5, 10, 15, 20$ — so one gridline is worth $%d$. That number is called the STEP." % step_a,
                "A bar's value is lines $\\times$ step. The wrestling bar reaches the %s line: $%d \\times %d = %d$. The archery bar reaches the %s: $%d \\times %d = %d$." % (ordinal(lines_w), lines_w, step_a, val_w, ordinal(lines_a), lines_a, step_a, val_a),
                "Change the step and the same drawing says something else: on a step-of-$1$ chart those bars would be only $%d$ and $%d$. The scale is not decoration — it is half the chart." % (lines_w, lines_a),
            ]), fig_bars),
            workedset("Reading heights",
                      "Lines first, step second, multiply.", [
                withfig(wex("Scale $0, 5, 10, 15, 20$. Wrestling reaches the %s line, archery the %s. Read both." % (ordinal(lines_w), ordinal(lines_a)),
                    ["Step is $%d$, so wrestling is $%d \\times %d = %d$." % (step_a, lines_w, step_a, val_w),
                     "Archery is $%d \\times %d = %d$." % (lines_a, step_a, val_a)],
                    "$%d$ and $%d$" % (val_w, val_a),
                    ["Eq(4*5, 20)", "Eq(3*5, 15)"]), fig_bars),
                wex("On a chart stepping by $%d$, a bar reaches the %s line and another stops halfway between $%d$ and $%d$. Read both." % (step_b, ordinal(lines_b), mid_lo, mid_hi),
                    ["First bar: $%d \\times %d = %d$." % (lines_b, step_b, val_b),
                     "Second bar: halfway between $%d$ and $%d$ is $(%d + %d) \\div 2 = %d$." % (mid_lo, mid_hi, mid_lo, mid_hi, mid)],
                    "$%d$ and $%d$" % (val_b, mid),
                    ["Eq(3*2, 6)", "Eq(Rational(6 + 8, 2), 7)", "6 < 7"]),
            ]),
            tryitset("Lines times step", "Three scales, one method.", [
                tp("On a chart stepping by $1$, a bar reaching the $7$th line stands for $7$. On a chart stepping by $5$, that same bar stands for:",
                   ["$35$", "$7$", "$12$"],
                   "With a step of $1$ the lines count themselves; with a step of $5$ each line is worth five, so $7 \\times 5 = 35$. The option $12$ added $7 + 5$ instead of multiplying, and $7$ kept the step-of-$1$ reading.",
                   ["Eq(7*5, 35)", "Eq(7 + 5, 12)", "7 < 35"]),
                tp("A chart steps by $2$. A bar reaching the $9$th line stands for:",
                   ["$18$", "$9$", "$11$"],
                   "$9 \\times 2 = 18$. The option $9$ counted lines as ones; $11$ added the step instead of multiplying by it.",
                   ["Eq(9*2, 18)", "Eq(9 + 2, 11)"]),
                tp("A chart steps by $5$. A bar reaching the $6$th line stands for:",
                   ["$30$", "$6$", "$11$"],
                   "$6 \\times 5 = 30$ — six lines, each worth five.",
                   ["Eq(6*5, 30)", "Eq(6 + 5, 11)"]),
            ]),
            tapq("Read the side first", "A bar chart's side numbers read $0, 5, 10, 15, 20$. A bar reaches the third line above zero. It stands for:",
                 ["$15$", "$3$", "$5$", "$10$"],
                 "The step is $5$, so three lines are $3 \\times 5 = 15$. The option $3$ counted gridlines as ones, and $10$ stopped one line short.",
                 ["Eq(3*5, 15)", "Eq(2*5, 10)"]),
            funfact("The same 20, drawn two ways",
                    "Change the scale and the picture changes shape while the facts stay put. A bar standing for $20$ is $4$ lines tall on a step-of-$5$ chart and $10$ lines tall on a step-of-$2$ chart — two and a half times the drawing, exactly the same twenty sheep. That is why the scale is printed on every chart: the drawing alone cannot tell you."),
            withfig(teach("Concept B", "Comparing bars", [
                "Two bars, two numbers: Monday $%d$ and Tuesday $%d$. 'How many MORE on Monday?' asks for the gap between them, not for a bar's own height." % (tall, short),
                "Subtract: $%d - %d = %d$. Then add back to check: $%d + %d = %d$ ✓ — the gap put on top of the shorter bar rebuilds the taller one." % (tall, short, diff, diff, short, tall),
                "'How many ALTOGETHER?' is the other question, and it adds instead: $%d + %d = %d$. Ask which question you were given before you touch the numbers." % (tall, short, tall + short),
            ]), fig_compare),
            workedset("More, and altogether",
                      "Gap by subtracting; total by adding.", [
                withfig(wex("Monday $%d$, Tuesday $%d$. How many more on Monday?" % (tall, short),
                    ["$%d - %d = %d$." % (tall, short, diff),
                     "Add back: $%d + %d = %d$ ✓." % (diff, short, tall)],
                    "$%d$ more" % diff,
                    ["Eq(20 - 14, 6)", "Eq(6 + 14, 20)"]), fig_compare),
                wex("The same two bars: how many altogether over the two days?",
                    ["Altogether means add: $%d + %d$." % (tall, short),
                     "$%d + %d = %d$." % (tall, short, tall + short)],
                    "$%d$" % (tall + short),
                    ["Eq(20 + 14, 34)", "Eq(34 - 14, 20)"]),
            ]),
            tryitset("Which question is it?", "More means subtract; altogether means add.", [
                tp("One bar stands for $25$, another for $10$. The first shows more by:",
                   ["$15$", "$35$", "$25$"],
                   "$25 - 10 = 15$, checked by $15 + 10 = 25$ ✓. The option $35$ answered the altogether question, and $25$ gave the taller bar itself.",
                   ["Eq(25 - 10, 15)", "Eq(15 + 10, 25)", "Eq(25 + 10, 35)"]),
                tp("Two bars stand for $14$ and $8$. Altogether they show:",
                   ["$22$", "$6$", "$14$"],
                   "$14 + 8 = 22$. The option $6$ is the difference $14 - 8$ — the answer to a different question.",
                   ["Eq(14 + 8, 22)", "Eq(14 - 8, 6)"]),
                tp("On a step-of-$5$ chart, one bar reaches the $5$th line and another the $2$nd. The taller shows more by:",
                   ["$15$", "$3$", "$25$"],
                   "Read the bars first: $5 \\times 5 = 25$ and $2 \\times 5 = 10$, so the gap is $25 - 10 = 15$, checked by $15 + 10 = 25$ ✓. The option $3$ compared gridlines instead of values.",
                   ["Eq(5*5, 25)", "Eq(2*5, 10)", "Eq(25 - 10, 15)", "Eq(15 + 10, 25)"]),
            ]),
            tapq("The gap, not the bar", "Bar A stands for $24$ and bar B for $16$. How many more does A show?",
                 ["$8$", "$24$", "$40$", "$16$"],
                 "$24 - 16 = 8$, and the add-back $8 + 16 = 24$ ✓ proves it. The option $24$ is A's whole height, and $40$ answered 'altogether' instead of 'how many more'.",
                 ["Eq(24 - 16, 8)", "Eq(8 + 16, 24)", "Eq(24 + 16, 40)"]),
            recap([
                "The scale up the side gives the step: 1, 2 or 5 per gridline.",
                "A bar's value is lines × step — never the number of lines by itself.",
                "A bar halfway between two lines takes the number halfway between them.",
                "How many more = subtract, then add the gap back to check.",
                "How many altogether = add the bars.",
            ]),
            tip("Before answering anything about a bar chart, write the step in the margin: 'one line = 5'. Then decide which question you were asked — a height, a gap, or a total — because each one is a different move."),
            tryitset("Mixed practice", "Scales, gaps and totals together.", [
                tp("A chart steps by $5$. A bar reaching the $7$th line stands for:",
                   ["$35$", "$7$", "$12$"],
                   "$7 \\times 5 = 35$. The option $12$ added $7 + 5$ instead of multiplying.",
                   ["Eq(7*5, 35)", "Eq(7 + 5, 12)"]),
                tp("A chart steps by $2$. A bar stops halfway between the lines marked $10$ and $12$. It stands for:",
                   ["$11$", "$22$", "$10$"],
                   "Halfway between $10$ and $12$ is $(10 + 12) \\div 2 = 11$ — bigger than $10$, smaller than $12$. The option $22$ added the two line values together.",
                   ["Eq(Rational(10 + 12, 2), 11)", "10 < 11", "11 < 12"]),
                withfig(tp("Saturday's bar stands for $22$ and Sunday's for $16$. Saturday shows more by:",
                   ["$6$", "$38$", "$22$"],
                   "$22 - 16 = 6$, checked by $6 + 16 = 22$ ✓. The option $38$ is the two days added together.",
                   ["Eq(22 - 16, 6)", "Eq(6 + 16, 22)", "Eq(22 + 16, 38)"]), fig_practice),
                tp("Three bars stand for $12$, $9$ and $15$. Altogether they show:",
                   ["$36$", "$21$", "$27$"],
                   "$12 + 9 = 21$, then $21 + 15 = 36$. The option $21$ stopped after two bars.",
                   ["Eq(12 + 9, 21)", "Eq(12 + 9 + 15, 36)"]),
                tp("A bar reaching the $6$th line stands for $12$. The chart steps by:",
                   ["$2$", "$6$", "$5$"],
                   "The step is the value shared out over the lines: $12 \\div 6 = 2$, checked by $6 \\times 2 = 12$ ✓. A step of $5$ would make that bar $6 \\times 5 = 30$.",
                   ["Eq(Rational(12,6), 2)", "Eq(6*2, 12)", "Eq(6*5, 30)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Bar Charts\"",
                    "A scale to read, a height to work out, and a gap that adds back. Next, the last lesson puts tables, pictographs and bars to work answering the questions people actually ask.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Asking Questions of Data
# ==========================================================================

def lesson_questions():
    # Naadam table.
    wr, hr, ar, ab = 18, 24, 12, 6
    tot = wr + hr + ar + ab            # 60
    # Week of aaruul packs sold.
    mon, tue, wed, thu, fri = 12, 15, 9, 24, 20
    wtot = mon + tue + wed + thu + fri  # 80
    late = thu + fri                    # 44
    early = mon + wed                   # 21
    gap = late - early                  # 23
    fig_naadam = fig_groups((wr, "wrestling"), (hr, "horse racing"),
                            (ar, "archery"), (ab, "ankle-bone shooting"))
    fig_week = fig_groups((mon, "Mon"), (tue, "Tue"), (wed, "Wed"),
                          (thu, "Thu"), (fri, "Fri"))
    return {
        "slug": "questions-of-data",
        "title": "Asking Questions of Data",
        "concreteComparison": (
            "A finished chart is not an answer — it is the place "
            "answers live. Somebody asks which Naadam sport was most "
            "popular, somebody else asks how many more chose horse "
            "racing than archery, and a third asks how many children "
            "were asked altogether. Three questions, one table, three "
            "different moves: look for the biggest row, subtract two "
            "rows, or add them all."),
        "objective": (
            "Answer most-popular, least-popular, how-many-more and "
            "how-many-altogether questions from a table or chart, and "
            "handle two-step questions that combine rows first."),
        "concept": [
            "**Most and least popular are simply the biggest and "
            "smallest counts.** In a table of $18$, $24$, $12$ and "
            "$6$, horse racing wins with $24$ and ankle-bone shooting "
            "is last with $6$ — no arithmetic needed, only careful "
            "comparing.",
            "**How many MORE subtracts; how many ALTOGETHER adds.** "
            "$24 - 12 = 12$ more chose horse racing than archery (check "
            "$12 + 12 = 24$ ✓), while $18 + 24 + 12 + 6 = 60$ children "
            "were asked in all.",
            "**Two-step questions combine rows first.** 'Did more "
            "children choose wrestling and archery together than horse "
            "racing?' Add the two rows: $18 + 12 = 30$; then compare: "
            "$30 - 24 = 6$ more. Build the pieces, then ask the "
            "question of them.",
        ],
        "keyIdea": (
            "Every question of a chart is one of a few moves: find the "
            "biggest or smallest row, subtract two rows for a "
            "difference, add rows for a total — and in two-step "
            "questions, combine rows before comparing."),
        "facts": [
            {"title": "How many more",
             "latex": "24 - 12 = 12 \\quad (12 + 12 = 24)",
             "explanation": "A difference between two rows, with the add-back that proves it."},
            {"title": "How many altogether",
             "latex": "18 + 24 + 12 + 6 = 60",
             "explanation": "Every row added — the same total row that acts as the table's receipt."},
        ],
        "workedExamples": [
            {"id": "g4da-l5-we1",
             "statement": "A table of Naadam favourites reads: wrestling $18$, horse racing $24$, archery $12$, ankle-bone shooting $6$. Which was most popular, which least, and what is the gap between them?",
             "note": "Compare the counts, then subtract the two ends.",
             "solution": ("Most popular: horse racing with $24$, since $24 > 18$. Least "
                          "popular: ankle-bone shooting with $6$, since $6 < 12$. The "
                          "gap between them is $24 - 6 = 18$, checked by $18 + 6 = 24$ "
                          "✓."),
             "badges": [{"text": "core"}],
             "check": ["24 > 18", "6 < 12", "Eq(24 - 6, 18)", "Eq(18 + 6, 24)"]},
            {"id": "g4da-l5-we2",
             "statement": "From the same table, did more children choose wrestling and archery together than horse racing alone, and by how many?",
             "note": "A two-step question: build the combined row first.",
             "solution": ("Combine the two rows: $18 + 12 = 30$. Compare with horse "
                          "racing: $30 - 24 = 6$, so yes — six more. Add back to "
                          "check: $6 + 24 = 30$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(18 + 12, 30)", "Eq(30 - 24, 6)", "Eq(6 + 24, 30)", "30 > 24"]},
        ],
        "commonMistakes": [
            {"text": "Answering \"how many more?\" with the bigger number itself.",
             "correction": "How many more is a comparison: 24 - 12 = 12, and the add-back 12 + 12 = 24 proves it. Answering 24 gives the row, not the gap.",
             "authored": True},
            {"text": "Answering every question with the tallest bar or biggest row.",
             "correction": "Read the question. Most popular wants the biggest row (24); how many altogether wants every row added (18 + 24 + 12 + 6 = 60); how many more wants a difference.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4da-l5-t1",
             "statement": "From the Naadam table (wrestling $18$, horse racing $24$, archery $12$, ankle-bone shooting $6$): how many chose wrestling or archery altogether?",
             "solution": "Altogether means add those two rows: $18 + 12 = 30$ children.",
             "check": ["Eq(18 + 12, 30)"]},
            {"id": "g4da-l5-t2",
             "statement": "From the same table: how many more chose wrestling than ankle-bone shooting?",
             "solution": "$18 - 6 = 12$ more, checked by $12 + 6 = 18$ ✓.",
             "check": ["Eq(18 - 6, 12)", "Eq(12 + 6, 18)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Three questions, three moves", [
                "Here is the table: wrestling $%d$, horse racing $%d$, archery $%d$, ankle-bone shooting $%d$." % (wr, hr, ar, ab),
                "MOST popular is the biggest row — horse racing, $%d$. LEAST popular is the smallest — ankle-bone shooting, $%d$. Nothing to compute; just compare carefully." % (hr, ab),
                "HOW MANY MORE subtracts two rows: $%d - %d = %d$, checked by $%d + %d = %d$ ✓. HOW MANY ALTOGETHER adds every row: $%d + %d + %d + %d = %d$ children." % (hr, ar, hr - ar, hr - ar, ar, hr, wr, hr, ar, ab, tot),
            ]), fig_naadam),
            workedset("Reading the question",
                      "Biggest row, smallest row, a difference, or a total.", [
                withfig(wex("Which sport was most popular, which least, and what is the gap?",
                    ["Most: horse racing $%d$; least: ankle-bone shooting $%d$." % (hr, ab),
                     "Gap: $%d - %d = %d$, and $%d + %d = %d$ ✓." % (hr, ab, hr - ab, hr - ab, ab, hr)],
                    "horse racing, ankle-bone shooting, gap $%d$" % (hr - ab),
                    ["24 > 18", "6 < 12", "Eq(24 - 6, 18)", "Eq(18 + 6, 24)"]), fig_naadam),
                wex("How many children were asked altogether?",
                    ["Add every row: $%d + %d = %d$, then $%d + %d = %d$." % (wr, hr, wr + hr, wr + hr, ar, wr + hr + ar),
                     "One row left: $%d + %d = %d$ children." % (wr + hr + ar, ab, tot)],
                    "$%d$" % tot,
                    ["Eq(18 + 24, 42)", "Eq(42 + 12, 54)", "Eq(18 + 24 + 12 + 6, 60)"]),
            ]),
            tryitset("One table, many questions", "Say which move the question wants.", [
                tp("From the table (wrestling $18$, horse racing $24$, archery $12$, ankle-bone $6$): how many more chose horse racing than wrestling?",
                   ["$6$", "$24$", "$42$"],
                   "$24 - 18 = 6$, checked by $6 + 18 = 24$ ✓. The option $24$ is horse racing's own row, and $42$ added the two rows instead of comparing them.",
                   ["Eq(24 - 18, 6)", "Eq(6 + 18, 24)", "Eq(24 + 18, 42)"]),
                tp("From the same table: how many chose archery or ankle-bone shooting altogether?",
                   ["$18$", "$6$", "$72$"],
                   "$12 + 6 = 18$. The option $6$ is the difference $12 - 6$ — the answer to 'how many more'.",
                   ["Eq(12 + 6, 18)", "Eq(12 - 6, 6)"]),
                tp("From the same table: which sport was chosen by exactly half as many children as horse racing?",
                   ["archery", "wrestling", "ankle-bone shooting"],
                   "Half of horse racing is $24 \\div 2 = 12$, which is archery's row. Wrestling's $18$ is more than half, and ankle-bone's $6$ is a quarter of $24$.",
                   ["Eq(Rational(24,2), 12)", "Eq(2*12, 24)", "Eq(4*6, 24)"]),
            ]),
            tapq("Which move?", "A table reads football $16$, basketball $9$, volleyball $11$. How many more chose football than basketball?",
                 ["$7$", "$16$", "$25$", "$36$"],
                 "'How many more' is a difference: $16 - 9 = 7$, checked by $7 + 9 = 16$ ✓. The option $25$ added those two rows, and $36$ is the total of all three — answers to questions nobody asked.",
                 ["Eq(16 - 9, 7)", "Eq(7 + 9, 16)", "Eq(16 + 9, 25)", "Eq(16 + 9 + 11, 36)"]),
            funfact("Every difference can be read from both ends",
                    "If horse racing beat archery by $12$, then archery trailed horse racing by the same $12$: one subtraction, two sentences. That is exactly why the add-back check works — $12 + 12 = 24$ puts the gap back on the smaller row and rebuilds the bigger one."),
            withfig(teach("Concept B", "Two-step questions", [
                "Some questions need a total built before they can be answered. Here are aaruul packs sold in a week: Mon $%d$, Tue $%d$, Wed $%d$, Thu $%d$, Fri $%d$." % (mon, tue, wed, thu, fri),
                "'How many more were sold on Thursday and Friday together than on Monday and Wednesday together?' Build both pieces first: $%d + %d = %d$ and $%d + %d = %d$." % (thu, fri, late, mon, wed, early),
                "Now the question is an ordinary comparison: $%d - %d = %d$, checked by $%d + %d = %d$ ✓. Build the pieces, then ask the question of them." % (late, early, gap, gap, early, late),
            ]), fig_week),
            workedset("Combine, then compare",
                      "Build each piece; then subtract or add as asked.", [
                withfig(wex("Thursday and Friday together against Monday and Wednesday together — how many more?",
                    ["$%d + %d = %d$ and $%d + %d = %d$." % (thu, fri, late, mon, wed, early),
                     "$%d - %d = %d$, and $%d + %d = %d$ ✓." % (late, early, gap, gap, early, late)],
                    "$%d$ more" % gap,
                    ["Eq(24 + 20, 44)", "Eq(12 + 9, 21)", "Eq(44 - 21, 23)", "Eq(23 + 21, 44)"]), fig_week),
                wex("How many packs were sold in the whole week?",
                    ["$%d + %d = %d$, then $%d + %d = %d$." % (mon, tue, mon + tue, mon + tue, wed, mon + tue + wed),
                     "$%d + %d = %d$, then $%d + %d = %d$ packs." % (mon + tue + wed, thu, mon + tue + wed + thu, mon + tue + wed + thu, fri, wtot)],
                    "$%d$" % wtot,
                    ["Eq(12 + 15, 27)", "Eq(27 + 9, 36)", "Eq(36 + 24, 60)",
                     "Eq(12 + 15 + 9 + 24 + 20, 80)"]),
            ]),
            tryitset("Build first, then answer", "Combine the rows the question names.", [
                tp("Sales were Mon $12$, Tue $15$, Wed $9$, Thu $24$, Fri $20$. How many were sold on Monday, Tuesday and Wednesday together?",
                   ["$36$", "$27$", "$44$"],
                   "$12 + 15 = 27$, then $27 + 9 = 36$. The option $27$ stopped after two days, and $44$ combined the wrong pair of days.",
                   ["Eq(12 + 15, 27)", "Eq(12 + 15 + 9, 36)", "Eq(24 + 20, 44)"]),
                tp("From the same week: how many more were sold on Thursday than on Wednesday and Monday together?",
                   ["$3$", "$21$", "$12$"],
                   "Build the piece: $9 + 12 = 21$; then compare with Thursday: $24 - 21 = 3$, checked by $3 + 21 = 24$ ✓. The option $21$ is the combined piece itself.",
                   ["Eq(9 + 12, 21)", "Eq(24 - 21, 3)", "Eq(3 + 21, 24)"]),
                tp("From the same week: Tuesday and Wednesday together compared with Friday — the two days together show:",
                   ["$4$ more", "$4$ fewer", "the same"],
                   "$15 + 9 = 24$ against Friday's $20$: $24 - 20 = 4$ more, checked by $4 + 20 = 24$ ✓.",
                   ["Eq(15 + 9, 24)", "Eq(24 - 20, 4)", "Eq(4 + 20, 24)"]),
            ]),
            tapq("Build the piece first", "A pictograph with the key one symbol $= 5$ shows Monday $4$ symbols and Tuesday $3$ symbols. Wednesday's bar on another chart stands for $20$. How many more were counted on Monday and Tuesday together than on Wednesday?",
                 ["$15$", "$7$", "$35$", "$20$"],
                 "Read the pictograph rows through the key: $4 \\times 5 = 20$ and $3 \\times 5 = 15$, together $20 + 15 = 35$. Then compare: $35 - 20 = 15$, checked by $15 + 20 = 35$ ✓. The option $7$ added the symbols and forgot the key entirely.",
                 ["Eq(4*5, 20)", "Eq(3*5, 15)", "Eq(20 + 15, 35)", "Eq(35 - 20, 15)",
                  "Eq(15 + 20, 35)"]),
            recap([
                "Most popular = biggest row; least popular = smallest row.",
                "How many more = subtract, then add the gap back to check.",
                "How many altogether = add the rows the question names.",
                "Two-step questions: build each piece first, then compare or total.",
                "Whatever the chart, every mark stands for something counted — and the parts must add back.",
            ]),
            tip("Underline the question's key words before you look at the numbers: MORE means subtract, ALTOGETHER means add, MOST means look. If two rows are named together, build that piece first."),
            tryitset("Mixed practice", "Every question type, on tables, pictographs and bars.", [
                withfig(tp("From the Naadam table: how many children were asked altogether?",
                   ["$%d$" % tot, "$%d$" % hr, "$%d$" % (wr + hr)],
                   "Add every row: $%d + %d + %d + %d = %d$. The option $%d$ is the biggest row, which answers 'most popular' instead." % (wr, hr, ar, ab, tot, hr),
                   ["Eq(18 + 24, 42)", "Eq(18 + 24 + 12 + 6, 60)"]), fig_naadam),
                tp("A table reads tea $22$, milk $14$, water $9$. How many more chose tea than water?",
                   ["$13$", "$31$", "$22$"],
                   "$22 - 9 = 13$, checked by $13 + 9 = 22$ ✓. The option $31$ added the two rows.",
                   ["Eq(22 - 9, 13)", "Eq(13 + 9, 22)", "Eq(22 + 9, 31)"]),
                tp("A pictograph with the key one symbol $= 10$ shows a row of $4$ symbols and another of $6$. Together the two rows stand for:",
                   ["$100$", "$10$", "$24$"],
                   "Read each row through the key: $4 \\times 10 = 40$ and $6 \\times 10 = 60$, together $40 + 60 = 100$. The option $10$ added the symbols and never used the key.",
                   ["Eq(4*10, 40)", "Eq(6*10, 60)", "Eq(40 + 60, 100)"]),
                tp("A bar chart steps by $5$. One bar reaches the $6$th line, another the $2$nd. The taller bar shows more by:",
                   ["$20$", "$4$", "$30$"],
                   "$6 \\times 5 = 30$ and $2 \\times 5 = 10$, so the gap is $30 - 10 = 20$, checked by $20 + 10 = 30$ ✓. The option $4$ compared gridlines rather than values.",
                   ["Eq(6*5, 30)", "Eq(2*5, 10)", "Eq(30 - 10, 20)", "Eq(20 + 10, 30)"]),
                tp("A table reads Monday $16$, Tuesday $11$, Wednesday $13$, with a total row of $40$. Monday and Wednesday together beat Tuesday by:",
                   ["$18$", "$29$", "$5$"],
                   "Build the piece: $16 + 13 = 29$; then $29 - 11 = 18$, checked by $18 + 11 = 29$ ✓. The rows do re-add to the total ($16 + 11 + 13 = 40$), so the table can be trusted.",
                   ["Eq(16 + 13, 29)", "Eq(29 - 11, 18)", "Eq(18 + 11, 29)",
                    "Eq(16 + 11 + 13, 40)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Asking Questions of Data\" — and the topic",
                    "Bundles of five, tables with receipts, keys that turn symbols into numbers, scales that turn heights into numbers, and questions answered by looking, subtracting or adding. In every one of them the same promise held: every mark stands for something counted, and the parts add back to the total. Grade 5 takes the story on to line graphs and to the mean.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    # pr2 picture: 34 drawn as 6 bundles and 4 singles.
    b, s, n = 6, 4, 34
    fig_pr2 = tally_fig(b, s)
    # pr5 picture: pictograph rows of 8 and 5 symbols, key 5.
    key, sym_a, sym_b = 5, 8, 5
    fig_pr5 = fig_groups((sym_a, "symbols — Saturday", C_ACCENT),
                         (sym_b, "symbols — Sunday", C_WARM))
    return [
        prob("g4da-pr1", "A tally shows $7$ bundles and $2$ singles. What is the count?",
             "$5 \\times 7 = 35$ from the bundles, then $35 + 2 = 37$. The singles ($2$) are fewer than $5$, so the tally is written properly.",
             ["Eq(5*7, 35)", "Eq(5*7 + 2, 37)", "2 < 5"]),
        withprobfig(
            prob("g4da-pr2", "Draw $%d$ as tally marks. How many bundles and how many singles?" % n,
                 "$%d \\div 5 = %d$ with $%d$ left: $%d$ bundles and $%d$ singles. Receipt: $5 \\times %d + %d = %d$ ✓ and $%d < 5$ ✓." % (n, b, s, b, s, b, s, n, s),
                 ["Eq(5*6 + 4, 34)", "4 < 5"]),
            fig_pr2),
        prob("g4da-pr3", "A table of snacks sold reads: buuz $14$, khuushuur $21$, aaruul $9$, boortsog $6$. What is the total?",
             "Add the rows: $14 + 21 = 35$, then $35 + 9 = 44$, then $44 + 6 = 50$. The total row must read $50$.",
             ["Eq(14 + 21, 35)", "Eq(35 + 9, 44)", "Eq(14 + 21 + 9 + 6, 50)"]),
        prob("g4da-pr4", "A table of four rows totals $55$. Three rows read $17$, $13$ and $9$. Find the fourth row.",
             "Known rows: $17 + 13 + 9 = 39$. Missing row: $55 - 39 = 16$. Add back to check: $16 + 39 = 55$ ✓.",
             ["Eq(17 + 13 + 9, 39)", "Eq(55 - 39, 16)", "Eq(16 + 39, 55)"]),
        withprobfig(
            prob("g4da-pr5", "A pictograph has the key: one symbol $= %d$ tickets. Saturday shows $%d$ symbols and Sunday shows $%d$. How many tickets each day, and how many more on Saturday?" % (key, sym_a, sym_b),
                 "Saturday: $%d \\times %d = %d$. Sunday: $%d \\times %d = %d$. Saturday sold $%d - %d = %d$ more, checked by $%d + %d = %d$ ✓." % (sym_a, key, sym_a * key, sym_b, key, sym_b * key, sym_a * key, sym_b * key, (sym_a - sym_b) * key, (sym_a - sym_b) * key, sym_b * key, sym_a * key),
                 ["Eq(8*5, 40)", "Eq(5*5, 25)", "Eq(40 - 25, 15)", "Eq(15 + 25, 40)"]),
            fig_pr5),
        prob("g4da-pr6", "A pictograph's key is: one symbol $= 10$ sheep. How many symbols show $90$ sheep, and how would you show $45$?",
             "$90 \\div 10 = 9$ symbols, checked by $9 \\times 10 = 90$ ✓. For $45$: $4$ full symbols and a half, since half the key is $10 \\div 2 = 5$ and $4 \\times 10 + 5 = 45$ ✓.",
             ["Eq(Rational(90,10), 9)", "Eq(9*10, 90)", "Eq(Rational(10,2), 5)",
              "Eq(4*10 + 5, 45)"]),
        prob("g4da-pr7", "On a bar chart stepping by $2$, one bar reaches the $8$th line and another stands for $11$. How many more does the first bar show?",
             "The first bar is $8 \\times 2 = 16$. The gap is $16 - 11 = 5$, checked by $5 + 11 = 16$ ✓.",
             ["Eq(8*2, 16)", "Eq(16 - 11, 5)", "Eq(5 + 11, 16)"]),
        prob("g4da-pr8", "A table reads horses $12$, sheep $18$, goats $20$. How many more are there of horses and sheep together than of goats?",
             "Build the piece first: $12 + 18 = 30$. Then compare: $30 - 20 = 10$ more, checked by $10 + 20 = 30$ ✓.",
             ["Eq(12 + 18, 30)", "Eq(30 - 20, 10)", "Eq(10 + 20, 30)"]),
    ]


def test_bank():
    # x4 picture: bars of 25 and 15 on a step-of-5 chart.
    step, ln_a, ln_b = 5, 5, 3
    fig_x4 = fig_groups((ln_a, "gridlines — wrestling (%d each)" % step, C_ACCENT),
                        (ln_b, "gridlines — archery (%d each)" % step, C_WARM))
    return [
        prob("g4da-x1", "A tally shows $9$ bundles and $3$ singles. What is the count, and how do you know the tally is written properly?",
             "$5 \\times 9 = 45$, then $45 + 3 = 48$. It is written properly because the singles ($3$) are fewer than $5$ — a fifth single would have tied itself into another bundle.",
             ["Eq(5*9, 45)", "Eq(5*9 + 3, 48)", "3 < 5"]),
        prob("g4da-x2", "A table of three rows totals $50$. Two rows read $22$ and $16$. Find the missing row and prove it.",
             "Known rows: $22 + 16 = 38$. Missing row: $50 - 38 = 12$. Proof: all three rows re-add to the total, $12 + 38 = 50$ ✓.",
             ["Eq(22 + 16, 38)", "Eq(50 - 38, 12)", "Eq(12 + 38, 50)"]),
        prob("g4da-x3", "A pictograph's key is: one symbol $= 10$ horses. A row shows $6$ full symbols and one half symbol. How many horses?",
             "The full symbols give $6 \\times 10 = 60$. The half symbol is worth half the key, $10 \\div 2 = 5$. Together $60 + 5 = 65$ horses.",
             ["Eq(6*10, 60)", "Eq(Rational(10,2), 5)", "Eq(60 + 5, 65)"]),
        withprobfig(
            prob("g4da-x4", "On a bar chart stepping by $%d$, the wrestling bar reaches the %s line and the archery bar the %s. Read both bars, say how many more chose wrestling, and how many chose either sport altogether." % (step, ordinal(ln_a), ordinal(ln_b)),
                 "Wrestling: $%d \\times %d = %d$. Archery: $%d \\times %d = %d$. More: $%d - %d = %d$, checked by $%d + %d = %d$ ✓. Altogether: $%d + %d = %d$." % (ln_a, step, ln_a * step, ln_b, step, ln_b * step, ln_a * step, ln_b * step, (ln_a - ln_b) * step, (ln_a - ln_b) * step, ln_b * step, ln_a * step, ln_a * step, ln_b * step, (ln_a + ln_b) * step),
                 ["Eq(5*5, 25)", "Eq(3*5, 15)", "Eq(25 - 15, 10)", "Eq(10 + 15, 25)",
                  "Eq(25 + 15, 40)"]),
            fig_x4),
        prob("g4da-x5", "A pictograph's key is: one symbol $= 2$ books. How many symbols show $24$ books, and how many would show $9$?",
             "$24 \\div 2 = 12$ symbols, checked by $12 \\times 2 = 24$ ✓. For $9$: $4$ full symbols and a half, since half the key is $2 \\div 2 = 1$ and $4 \\times 2 + 1 = 9$ ✓.",
             ["Eq(Rational(24,2), 12)", "Eq(12*2, 24)", "Eq(Rational(2,2), 1)",
              "Eq(4*2 + 1, 9)"]),
        prob("g4da-x6", ("A survey table reads: football $14$, wrestling $21$, basketball $9$, archery $6$. "
                         "Name the most and least popular, give the total surveyed, and say how many more "
                         "chose wrestling than archery."),
             "Most popular: wrestling $21$ (bigger than football's $14$). Least popular: archery $6$ (smaller than basketball's $9$). Total: $14 + 21 + 9 + 6 = 50$ children. Wrestling beats archery by $21 - 6 = 15$, checked by $15 + 6 = 21$ ✓.",
             ["21 > 14", "6 < 9", "Eq(14 + 21, 35)", "Eq(14 + 21 + 9 + 6, 50)",
              "Eq(21 - 6, 15)", "Eq(15 + 6, 21)"]),
    ]


def main():
    topic = {
        "slug": "data-and-pictographs",
        "title": "Data & Pictographs",
        "grade": 4,
        "status": "published",
        "blurb": ("Tally marks in bundles of five, frequency tables with "
                  "totals as receipts, pictographs with keys, bar charts on "
                  "small scales, and answering questions from data."),
        "lessons": [
            lesson_tally(),
            lesson_tables(),
            lesson_pictographs(),
            lesson_bars(),
            lesson_questions(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "data-and-pictographs.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
