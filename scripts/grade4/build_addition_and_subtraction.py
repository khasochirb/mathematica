#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Addition & Subtraction.

Column addition (line up places, add from the right, carry past nine),
column subtraction (regrouping, zeros on top, the add-back receipt),
mental strategies (make-ten, near-doubles, compensation — with number-line
jump pictures), fact families and box equations solved by the inverse,
and one- and two-step word problems chosen by their story shape.

Through-line: ADDITION AND SUBTRACTION ARE ONE FACT READ TWO WAYS — so
every answer can sign its own receipt. Sums check by adding the other
way; differences check by adding back; boxes check by substitution;
two-step stories check by walking the second road.

Grade discipline: totals inside 10 000, no negative numbers, at most two
steps. Every check is sympy-asserted with exact integers BEFORE the JSON
is written — a wrong fact cannot ship. Figures are built from the SAME
variables as the statements they illustrate, so text and picture cannot
disagree.

Run: python3 scripts/grade4/build_addition_and_subtraction.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic, withfig,
                     fig_groups, fig_numline, fig_geo, P, poly,
                     C_ACCENT, C_WARM, C_GREEN)


# ==========================================================================
# Lesson 1 — Column Addition
# ==========================================================================

def lesson_column_addition():
    a, b = 358, 467
    a_ones, b_ones = a % 10, b % 10
    fig_carry = fig_groups(
        (a_ones, "ones in %d" % a, C_ACCENT),
        (b_ones, "ones in %d" % b, C_WARM),
    )
    return {
        "slug": "column-addition",
        "title": "Column Addition",
        "concreteComparison": (
            "Counting money after a market day: you sort the togrog "
            "notes into piles — thousands, hundreds, tens, ones — and "
            "count each pile on its own. Whenever ten small notes stack "
            "up, you swap them for one bigger note. Column addition is "
            "exactly that sorting: line the places up, add each pile, "
            "and trade every ten upward."),
        "objective": (
            "Add three- and four-digit numbers in columns — lining up "
            "places, adding from the ones, carrying past nine — and "
            "check every sum by adding the other way."),
        "concept": [
            "**Places line up from the right.** Ones under ones, tens "
            "under tens, hundreds under hundreds. A digit's column IS "
            "its value — slide $47$ one place left and it silently "
            "becomes $470$.",
            "**Add from the ones and trade every ten.** $8 + 7 = 15$ "
            "ones is too many for one column: five stay, and ten of "
            "them trade for $1$ ten that moves next door. The carry is "
            "real value on the move — and when you add TWO numbers it "
            "is always exactly $1$. (Stack three or more numbers in a "
            "column and a bigger carry can appear: $9 + 9 + 9 = 27$ "
            "carries a $2$.)",
            "**Check by adding the other way.** $358 + 467$ and $467 + "
            "358$ walk different roads to the SAME total. Re-adding in "
            "the other order is the sum's receipt: if the two answers "
            "disagree, a carry slipped somewhere.",
        ],
        "keyIdea": (
            "Line up the places, add from the right, and trade every "
            "ten upward — then add the other way and make the total "
            "repeat."),
        "facts": [
            {"title": "Ten of these make one of those",
             "latex": "10 \\ \\text{ones} = 1 \\ \\text{ten} \\qquad 10 \\ \\text{tens} = 1 \\ \\text{hundred}",
             "explanation": "Carrying is trading: ten in one column become one in the next."},
            {"title": "The other-way check",
             "latex": "358 + 467 = 825 \\quad \\text{and} \\quad 467 + 358 = 825",
             "explanation": "Order never changes a sum — add the other way and the total must repeat."},
        ],
        "workedExamples": [
            {"id": "g4as-l1-we1",
             "statement": "Add $358 + 467$ in columns, then check by adding the other way.",
             "note": "Ones first; every ten trades up.",
             "solution": ("Ones: $8 + 7 = 15$ — write $5$, carry $1$. Tens: $5 + 6 "
                          "+ 1 = 12$ — write $2$, carry $1$. Hundreds: $3 + 4 + 1 = "
                          "8$. Total $825$. Other way: $467 + 358 = 825$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8 + 7, 15)", "Eq(5 + 6 + 1, 12)",
                       "Eq(358 + 467, 825)", "Eq(467 + 358, 825)"]},
            {"id": "g4as-l1-we2",
             "statement": "Add $785 + 649$.",
             "note": "The hundreds outgrow one digit — the total crosses 1000.",
             "solution": ("Ones: $5 + 9 = 14$. Tens: $8 + 4 + 1 = 13$. Hundreds: "
                          "$7 + 6 + 1 = 14$ — fourteen hundreds are $1$ thousand "
                          "$4$ hundreds. Total $1\\,434$; other way $649 + 785 = "
                          "1\\,434$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5 + 9, 14)", "Eq(7 + 6 + 1, 14)",
                       "Eq(785 + 649, 1434)", "Eq(649 + 785, 1434)"]},
        ],
        "commonMistakes": [
            {"text": "Lining numbers up on the left — writing the 4 of 47 under the 3 of 385.",
             "correction": "Places line up from the RIGHT: ones under ones, tens under tens. 47 + 385 is 432; left-aligned, the 47 acts as 470 and the sum silently becomes 855.",
             "authored": True},
            {"text": "Writing a two-digit column total straight down — a 15 squeezed into the ones column.",
             "correction": "15 ones are 1 ten and 5 ones: write the 5, carry the 1 into the tens column. The carry is real value, not decoration.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4as-l1-t1",
             "statement": "Add $276 + 358$ and check it the other way.",
             "solution": "Ones $6 + 8 = 14$; tens $7 + 5 + 1 = 13$; hundreds $2 + 3 + 1 = 6$: total $634$. Check: $358 + 276 = 634$ ✓.",
             "check": ["Eq(276 + 358, 634)", "Eq(358 + 276, 634)"]},
            {"id": "g4as-l1-t2",
             "statement": "Add $894 + 538$.",
             "solution": "Ones $4 + 8 = 12$; tens $9 + 3 + 1 = 13$; hundreds $8 + 5 + 1 = 14$: total $1\\,432$. Check: $538 + 894 = 1\\,432$ ✓.",
             "check": ["Eq(894 + 538, 1432)", "Eq(538 + 894, 1432)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Line up, add from the right, trade", [
                "Write the numbers so PLACES line up — ones under ones, tens under tens, hundreds under hundreds. In $%d + %d$, the $%d$ and the $%d$ share the ones column." % (a, b, a_ones, b_ones),
                "Add from the RIGHT. Ones first: $%d + %d = 15$ — too many for one column. Ten of those ones trade for ONE ten: write $5$, carry $1$ into the tens." % (a_ones, b_ones),
                "The carry is real value, not decoration. Tens: $5 + 6 + 1 = 12$ — write $2$, carry $1$ again. Hundreds: $3 + 4 + 1 = 8$. Total: $825$.",
            ]), fig_carry),
            workedset("Carrying past nine",
                      "Ones first, and every ten trades up.", [
                wex("Add $358 + 467$ in columns.",
                    ["Ones: $8 + 7 = 15$ — write $5$, carry $1$.",
                     "Tens: $5 + 6 + 1 = 12$ — write $2$, carry $1$. Hundreds: $3 + 4 + 1 = 8$."],
                    "$825$",
                    ["Eq(8 + 7, 15)", "Eq(358 + 467, 825)"]),
                wex("Add $429 + 386$ in columns.",
                    ["Ones: $9 + 6 = 15$ — write $5$, carry $1$. Tens: $2 + 8 + 1 = 11$ — write $1$, carry $1$.",
                     "Hundreds: $4 + 3 + 1 = 8$. Total: $815$."],
                    "$815$",
                    ["Eq(9 + 6, 15)", "Eq(429 + 386, 815)"]),
            ]),
            tryitset("Carry it over", "Ones first; trade every ten upward.", [
                tp("$347 + 285$ equals:",
                   ["$632$", "$522$", "$622$"],
                   "Ones $7 + 5 = 12$ (write $2$, carry $1$); tens $4 + 8 + 1 = 13$; hundreds $3 + 2 + 1 = 6$: $632$. Dropping the carries gives $522$ — the no-trade trap.",
                   ["Eq(7 + 5, 12)", "Eq(347 + 285, 632)"]),
                tp("$508 + 293$ equals:",
                   ["$801$", "$791$", "$811$"],
                   "Ones $8 + 3 = 11$ (write $1$, carry $1$); tens $0 + 9 + 1 = 10$ (write $0$, carry $1$); hundreds $5 + 2 + 1 = 8$: $801$. Forgetting the ones carry leaves $791$.",
                   ["Eq(0 + 9 + 1, 10)", "Eq(508 + 293, 801)"]),
                tp("$634 + 187$ equals:",
                   ["$821$", "$721$", "$711$"],
                   "Ones $4 + 7 = 11$; tens $3 + 8 + 1 = 12$; hundreds $6 + 1 + 1 = 8$: $821$. Missing the tens carry gives $721$.",
                   ["Eq(3 + 8 + 1, 12)", "Eq(634 + 187, 821)"]),
            ]),
            tapq("Columns are places", "To add $47 + 385$, Dorj lines the numbers up on the LEFT, so the $4$ of $47$ sits under the $3$ of $385$. What really happens?",
                 ["the $47$ acts as $470$, and the sum comes out $855$ instead of $432$",
                  "nothing — lining up on the left works just as well",
                  "the sum still comes out $432$",
                  "the $385$ turns into $3\\,850$"],
                 "Columns are PLACES. Slid one place left, the $4$ of $47$ sits in the tens — the addition quietly computes $470 + 385 = 855$. Lined up from the right it is $47 + 385 = 432$.",
                 ["Eq(470 + 385, 855)", "Eq(47 + 385, 432)", "Ne(855, 432)"]),
            funfact("The carry that stays a 1",
                    "When you add TWO numbers, however long they get, one column can hold at most $9 + 9 = 18$, plus an incoming carry: $19$ at the very most. That is one ten and nine ones — so the number you carry is always exactly $1$, never more. The scariest-looking two-number column addition still moves only a quiet little $1$. Stack THREE or more numbers, though, and the carry can grow — $9 + 9 + 9 = 27$ writes $7$ and carries $2$."),
            teach("Concept B", "Into the thousands — and the other-way check", [
                "Two three-digit numbers can outgrow three digits: $785 + 649$ — ones $5 + 9 = 14$, tens $8 + 4 + 1 = 13$, hundreds $7 + 6 + 1 = 14$. Fourteen hundreds are $1$ thousand $4$ hundreds: $1\\,434$.",
                "That is as big as it gets for two three-digit numbers: even $999 + 999 = 1\\,998$, so the answer never needs more than one extra digit. And nothing changes when the numbers themselves are four digits — $1\\,748 + 2\\,596$ simply adds one more column, the thousands.",
                "Now the through-line of this whole topic: one fact can be read two ways. Check every sum by adding the OTHER way — $649 + 785$ must land on the same $1\\,434$. If the two reads disagree, one of them slipped.",
            ]),
            workedset("Crossing 1000 — and four digits",
                      "Add both ways; the total must repeat.", [
                wex("Add $785 + 649$, then check by adding the other way.",
                    ["Ones $5 + 9 = 14$; tens $8 + 4 + 1 = 13$; hundreds $7 + 6 + 1 = 14$: $1\\,434$.",
                     "Other way: $649 + 785 = 1\\,434$ — same total, sum confirmed."],
                    "$1\\,434$",
                    ["Eq(785 + 649, 1434)", "Eq(649 + 785, 1434)"]),
                wex("Add $967 + 568$ and check it.",
                    ["Ones $7 + 8 = 15$; tens $6 + 6 + 1 = 13$; hundreds $9 + 5 + 1 = 15$: $1\\,535$.",
                     "Check: $568 + 967 = 1\\,535$ ✓."],
                    "$1\\,535$",
                    ["Eq(967 + 568, 1535)", "Eq(568 + 967, 1535)"]),
                wex("Add $1\\,748 + 2\\,596$ — four digits, one more column.",
                    ["Ones $8 + 6 = 14$ (write $4$, carry $1$); tens $4 + 9 + 1 = 14$ (write $4$, carry $1$); hundreds $7 + 5 + 1 = 13$ (write $3$, carry $1$).",
                     "Thousands are just the next column along: $1 + 2 + 1 = 4$. Total $4\\,344$; other way $2\\,596 + 1\\,748 = 4\\,344$ ✓."],
                    "$4\\,344$",
                    ["Eq(8 + 6, 14)", "Eq(7 + 5 + 1, 13)", "Eq(1 + 2 + 1, 4)",
                     "Eq(1748 + 2596, 4344)", "Eq(2596 + 1748, 4344)"]),
            ]),
            tryitset("Past a thousand", "Four-digit totals, checked the other way.", [
                tp("$856 + 379$ equals:",
                   ["$1\\,235$", "$1\\,125$", "$477$"],
                   "Ones $6 + 9 = 15$; tens $5 + 7 + 1 = 13$; hundreds $8 + 3 + 1 = 12$: $1\\,235$. $1\\,125$ dropped the carries; $477$ subtracted instead of adding ($856 - 379 = 477$, since $477 + 379 = 856$).",
                   ["Eq(856 + 379, 1235)", "Eq(856 - 379, 477)", "Eq(477 + 379, 856)"]),
                tp("$604 + 517$ equals:",
                   ["$1\\,121$", "$1\\,111$", "$121$"],
                   "Ones $4 + 7 = 11$; tens $0 + 1 + 1 = 2$; hundreds $6 + 5 = 11$ — eleven hundreds are one thousand one hundred: $1\\,121$. $1\\,111$ lost the ones carry; $121$ lost the thousand.",
                   ["Eq(4 + 7, 11)", "Eq(604 + 517, 1121)"]),
                tp("You computed $358 + 467 = 825$. Which check adds the SAME two numbers in the other order?",
                   ["compute $467 + 358$ and expect $825$ again",
                    "compute $825 + 467$ and expect $358$",
                    "compute $358 + 467$ once more, the same way"],
                   "Swapping the order re-walks the sum by a different road: $467 + 358 = 825$ ✓. Adding $825 + 467$ climbs to $1\\,292$ — a sum can never shrink back to $358$. Re-adding the same way just repeats any slip.",
                   ["Eq(467 + 358, 825)", "Eq(358 + 467, 825)", "Eq(825 + 467, 1292)",
                    "Ne(1292, 358)"]),
                tp("$2\\,375 + 1\\,846$ equals:",
                   ["$4\\,221$", "$4\\,211$", "$4\\,121$"],
                   "Four digits, four columns: ones $5 + 6 = 11$; tens $7 + 4 + 1 = 12$; hundreds $3 + 8 + 1 = 12$; thousands $2 + 1 + 1 = 4$: $4\\,221$, and the other way $1\\,846 + 2\\,375 = 4\\,221$ ✓. $4\\,211$ dropped the ones carry.",
                   ["Eq(5 + 6, 11)", "Eq(2 + 1 + 1, 4)", "Eq(2375 + 1846, 4221)",
                    "Eq(1846 + 2375, 4221)"]),
            ]),
            tapq("The ceiling", "The LARGEST total two three-digit numbers can make is:",
                 ["$1\\,998$", "$999$", "$1\\,899$", "$9\\,999$"],
                 "$999 + 999 = 1\\,998$ — so the sum of two three-digit numbers never needs more than four digits, and when it does grow a digit, that digit is always $1$: $1\\,998 < 2\\,000$.",
                 ["Eq(999 + 999, 1998)", "1998 < 2000"]),
            recap([
                "Line up places from the right: ones under ones, tens under tens.",
                "Add from the ones; ten in any column trades for one in the next.",
                "Adding TWO numbers, the carry is always exactly 1 — a column holds at most 9 + 9 + 1 = 19. (Stack three or more and a bigger carry can appear.)",
                "Two three-digit numbers can reach four digits, never five.",
                "Check every sum by adding the other way — the total must repeat.",
            ]),
            tip("Say the trade out loud each time it happens — 'fifteen ones: five stay, one ten moves' — and finish every sum with the other-way check."),
            tryitset("Mixed practice", "Columns, carries, and the other-way check.", [
                tp("$263 + 349$ equals:",
                   ["$612$", "$602$", "$512$"],
                   "Ones $3 + 9 = 12$; tens $6 + 4 + 1 = 11$; hundreds $2 + 3 + 1 = 6$: $612$. $602$ lost the ones carry.",
                   ["Eq(263 + 349, 612)"]),
                tp("$578 + 246$ equals:",
                   ["$824$", "$814$", "$724$"],
                   "Ones $8 + 6 = 14$; tens $7 + 4 + 1 = 12$; hundreds $5 + 2 + 1 = 8$: $824$. $814$ dropped the ones carry into the tens.",
                   ["Eq(578 + 246, 824)"]),
                tp("$745 + 255$ equals:",
                   ["$1\\,000$", "$990$", "$900$"],
                   "Every column trades: ones $5 + 5 = 10$, tens $4 + 5 + 1 = 10$, hundreds $7 + 2 + 1 = 10$ — a clean thousand. $990$ carried nothing — it wrote the $0$ from $5 + 5$, then added $4 + 5 = 9$ and $7 + 2 = 9$ with no trades at all.",
                   ["Eq(745 + 255, 1000)", "Eq(7 + 2 + 1, 10)", "Eq(4 + 5, 9)",
                    "Eq(7 + 2, 9)"]),
                tp("$936 + 487$ equals:",
                   ["$1\\,423$", "$1\\,413$", "$1\\,323$"],
                   "Ones $6 + 7 = 13$; tens $3 + 8 + 1 = 12$; hundreds $9 + 4 + 1 = 14$: $1\\,423$ — checked the other way, $487 + 936 = 1\\,423$ ✓.",
                   ["Eq(936 + 487, 1423)", "Eq(487 + 936, 1423)"]),
                tp("A herder counts $486$ sheep and $375$ goats. How many animals altogether?",
                   ["$861$", "$851$", "$751$"],
                   "Altogether joins the flocks: $486 + 375 = 861$, and the other-way check $375 + 486 = 861$ agrees. $851$ lost the ones carry.",
                   ["Eq(486 + 375, 861)", "Eq(375 + 486, 861)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Column Addition\"",
                    "Line up, add from the right, trade every ten — and let the other-way check sign each answer. Next the machine runs in reverse: column subtraction, where every answer signs its receipt with the addition you just mastered.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Column Subtraction
# ==========================================================================

def lesson_column_subtraction():
    m, n = 634, 278
    m_ones = m % 10
    opened = 10
    fig_regroup = fig_groups(
        (m_ones, "ones %d already had" % m, C_ACCENT),
        (opened, "ones from one opened ten", C_WARM),
    )
    return {
        "slug": "column-subtraction",
        "title": "Column Subtraction",
        "concreteComparison": (
            "You owe a friend eight one-togrog coins but your pocket "
            "holds only four — so you break one ten-togrog coin into "
            "ten ones. Nothing gained, nothing lost: your money just "
            "changed outfits. Column subtraction regroups the same "
            "way — and afterwards you add your answer back, to prove "
            "nothing leaked."),
        "objective": (
            "Subtract three- and four-digit numbers with regrouping — "
            "including tops with zeros like $503 - 168$ and $3\\,005 - "
            "1\\,428$ — and prove every answer with the add-back "
            "check."),
        "concept": [
            "**The top number is the one being cut.** $634 - 278$ asks "
            "what is LEFT of $634$ — so when a top digit runs short "
            "($4$ ones facing $8$), you may not flip the column "
            "around. Open a ten instead: $634$ becomes $6$ hundreds, "
            "$2$ tens, $14$ ones — same value, readier outfit.",
            "**Zeros pass the borrow along.** In $503 - 168$ the tens "
            "hold nothing to lend, so knock one door further: a "
            "hundred opens into ten tens, THEN a ten opens into ten "
            "ones — $503 = 400 + 90 + 13$. Check the outfit before "
            "subtracting: it must still total $503$.",
            "**The add-back receipt, every time.** Subtraction and "
            "addition are one fact read two ways: if $634 - 278 = "
            "356$, then $356 + 278$ must rebuild $634$. Add the answer "
            "back every single time — a wrong answer fails its receipt "
            "on the spot.",
        ],
        "keyIdea": (
            "When the top digit runs short, open the next place — and "
            "prove every difference by adding it back: answer plus "
            "what you took away must rebuild what you started with."),
        "facts": [
            {"title": "Open a ten when the top runs short",
             "latex": "634 = 6 \\ \\text{hundreds}, \\ 2 \\ \\text{tens}, \\ 14 \\ \\text{ones}",
             "explanation": "Same number, new outfit — now the ones column can pay."},
            {"title": "The add-back receipt",
             "latex": "634 - 278 = 356 \\quad \\text{because} \\quad 356 + 278 = 634",
             "explanation": "Every subtraction is checked by the addition that undoes it."},
        ],
        "workedExamples": [
            {"id": "g4as-l2-we1",
             "statement": "Compute $634 - 278$, then sign the receipt.",
             "note": "Two tops run short — open a ten, then a hundred.",
             "solution": ("Ones: $4 < 8$, open a ten — $14 - 8 = 6$. Tens: now $2 < "
                          "7$, open a hundred — $12 - 7 = 5$. Hundreds: $5 - 2 = "
                          "3$. So $634 - 278 = 356$. Receipt: $356 + 278 = 634$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(14 - 8, 6)", "Eq(6 + 8, 14)", "Eq(12 - 7, 5)", "Eq(5 + 7, 12)",
                       "Eq(634 - 278, 356)", "Eq(356 + 278, 634)"]},
            {"id": "g4as-l2-we2",
             "statement": "Compute $503 - 168$.",
             "note": "The tens are zero — the borrow travels through them.",
             "solution": ("The tens hold nothing to lend, so open a hundred into "
                          "ten tens, then a ten into ten ones: $503 = 400 + 90 + "
                          "13$. Now subtract: $13 - 8 = 5$, $9 - 6 = 3$, $4 - 1 = "
                          "3$ — answer $335$. Receipt: $335 + 168 = 503$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(400 + 90 + 13, 503)", "Eq(13 - 8, 5)", "Eq(5 + 8, 13)",
                       "Eq(503 - 168, 335)", "Eq(335 + 168, 503)"]},
        ],
        "commonMistakes": [
            {"text": "Flipping a column to bigger-minus-smaller — for 634 − 278 computing 8 − 4 in the ones.",
             "correction": "The TOP number is the one being cut. If its digit is smaller, regroup — open a ten. Flip-work gives 444 here, and the receipt exposes it: 444 + 278 = 722, not 634.",
             "authored": True},
            {"text": "Jumping over a zero when borrowing — in 503 − 168, taking ones straight from the hundreds and leaving the tens untouched.",
             "correction": "Go through the zero door by door: 5 hundreds become 4 hundreds and 10 tens; one of those tens becomes 10 ones. Check it: 503 = 400 + 90 + 13 — then subtract.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4as-l2-t1",
             "statement": "Compute $725 - 468$, then prove it with the add-back check.",
             "solution": "Ones $15 - 8 = 7$; tens $11 - 6 = 5$; hundreds $6 - 4 = 2$: answer $257$. Receipt: $257 + 468 = 725$ ✓.",
             "check": ["Eq(725 - 468, 257)", "Eq(257 + 468, 725)"]},
            {"id": "g4as-l2-t2",
             "statement": "Compute $800 - 356$ and receipt it.",
             "solution": "$800 = 700 + 90 + 10$: ones $10 - 6 = 4$, tens $9 - 5 = 4$, hundreds $7 - 3 = 4$ — answer $444$. Receipt: $444 + 356 = 800$ ✓.",
             "check": ["Eq(700 + 90 + 10, 800)", "Eq(800 - 356, 444)", "Eq(444 + 356, 800)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Open a ten, then sign the receipt", [
                "Subtract from the right, and remember which number is being cut: $%d - %d$ asks what is left of $%d$. Ones first: $%d - 8$ cannot happen — the top ran short." % (m, n, m, m_ones),
                "Do not flip the column. REGROUP: open one of the $3$ tens into $%d$ ones — now $%d$ wears $6$ hundreds, $2$ tens, $14$ ones, and $14 - 8 = 6$ works fine." % (opened, m),
                "Tens next: $2 < 7$, so a hundred opens — $12 - 7 = 5$; hundreds $5 - 2 = 3$. Answer $356$ — and the receipt seals it: $356 + 278 = 634$ ✓.",
            ]), fig_regroup),
            workedset("Opening tens",
                      "The top runs short? Open the next place — then receipt.", [
                wex("Compute $634 - 278$.",
                    ["Ones: $14 - 8 = 6$ (a ten opened). Tens: $12 - 7 = 5$ (a hundred opened).",
                     "Hundreds: $5 - 2 = 3$. Receipt: $356 + 278 = 634$ ✓."],
                    "$356$",
                    ["Eq(634 - 278, 356)", "Eq(356 + 278, 634)"]),
                wex("Compute $852 - 367$, with its receipt.",
                    ["Ones: $12 - 7 = 5$; tens: $14 - 6 = 8$; hundreds: $7 - 3 = 4$.",
                     "Receipt: $485 + 367 = 852$ ✓."],
                    "$485$",
                    ["Eq(852 - 367, 485)", "Eq(485 + 367, 852)"]),
            ]),
            tryitset("Regroup and receipt", "Open the place, subtract, add it back.", [
                tp("$741 - 356$ equals:",
                   ["$385$", "$415$", "$495$"],
                   "Ones $11 - 6 = 5$; tens $13 - 5 = 8$; hundreds $6 - 3 = 3$: $385$, receipted by $385 + 356 = 741$ ✓. $415$ flipped columns to bigger-minus-smaller; $495$ forgot to reduce after lending.",
                   ["Eq(741 - 356, 385)", "Eq(385 + 356, 741)"]),
                tp("$623 - 189$ equals:",
                   ["$434$", "$566$", "$544$"],
                   "Ones $13 - 9 = 4$; tens $11 - 8 = 3$; hundreds $5 - 1 = 4$: $434$, and $434 + 189 = 623$ ✓. $566$ flipped every column.",
                   ["Eq(623 - 189, 434)", "Eq(434 + 189, 623)"]),
                tp("$917 - 528$ equals:",
                   ["$389$", "$411$", "$499$"],
                   "Ones $17 - 8 = 9$; tens $10 - 2 = 8$; hundreds $8 - 5 = 3$: $389$, and $389 + 528 = 917$ ✓. $499$ subtracted without ever reducing a lender.",
                   ["Eq(917 - 528, 389)", "Eq(389 + 528, 917)"]),
            ]),
            tapq("The receipt catches the flip", "For $634 - 278$, Suvdaa works each column as bigger digit minus smaller and gets $444$. What does the add-back check say?",
                 ["$444 + 278 = 722$, not $634$ — the receipt fails, so $444$ is wrong",
                  "$444 + 278 = 634$ — the receipt passes",
                  "the add-back check cannot catch this kind of slip",
                  "receipts are only for division"],
                 "The top number is the one being cut — flipping a column answers a different question. The receipt exposes it: $444 + 278 = 722$, not $634$. The true answer $356$ passes: $356 + 278 = 634$ ✓.",
                 ["Eq(444 + 278, 722)", "Ne(722, 634)", "Eq(634 - 278, 356)", "Eq(356 + 278, 634)"]),
            funfact("Cashiers count up",
                    "Watch change being made at a market stall: pay $1\\,000$ togrog for something costing $640$, and many sellers count UPWARD — six hundred forty, six hundred fifty, seven hundred, one thousand — dropping coins into your hand as they go. They are running the add-back check with real money: $640 + 360 = 1\\,000$, so the change is $360$."),
            teach("Concept B", "Zeros on top", [
                "$503 - 168$: the ones run short, but the tens have NOTHING to lend. Knock on the next door: open a hundred into ten tens first.",
                "Now a ten can open into ten ones: $503$ wears $4$ hundreds, $9$ tens, $13$ ones. Pause and check the outfit: $400 + 90 + 13 = 503$ — nothing leaked.",
                "Subtract: $13 - 8 = 5$, $9 - 6 = 3$, $4 - 1 = 3$ — answer $335$. Receipt: $335 + 168 = 503$ ✓. Zeros just pass the borrow along; the receipt signs exactly as before.",
            ]),
            workedset("Borrowing through zero",
                      "Open the hundred, then the ten — check the outfit, then subtract.", [
                wex("Compute $503 - 168$.",
                    ["Regroup: $503 = 400 + 90 + 13$ (check: still $503$).",
                     "$13 - 8 = 5$, $9 - 6 = 3$, $4 - 1 = 3$: answer $335$. Receipt $335 + 168 = 503$ ✓."],
                    "$335$",
                    ["Eq(400 + 90 + 13, 503)", "Eq(503 - 168, 335)", "Eq(335 + 168, 503)"]),
                wex("Compute $900 - 347$.",
                    ["$900 = 800 + 90 + 10$.",
                     "$10 - 7 = 3$, $9 - 4 = 5$, $8 - 3 = 5$: answer $553$. Receipt $553 + 347 = 900$ ✓."],
                    "$553$",
                    ["Eq(800 + 90 + 10, 900)", "Eq(900 - 347, 553)", "Eq(553 + 347, 900)"]),
                wex("Compute $3\\,005 - 1\\,428$ — four digits, same doors.",
                    ["The tens and hundreds are zero, so the borrow walks all the way to the thousands: $3\\,005 = 2\\,000 + 900 + 90 + 15$ (check: still $3\\,005$).",
                     "$15 - 8 = 7$, $9 - 2 = 7$, $9 - 4 = 5$, $2 - 1 = 1$: answer $1\\,577$. Receipt $1\\,577 + 1\\,428 = 3\\,005$ ✓."],
                    "$1\\,577$",
                    ["Eq(2000 + 900 + 90 + 15, 3005)", "Eq(15 - 8, 7)", "Eq(7 + 8, 15)",
                     "Eq(3005 - 1428, 1577)", "Eq(1577 + 1428, 3005)"]),
            ]),
            tryitset("Through the zero", "The borrow travels door to door; the receipt still signs.", [
                tp("$605 - 238$ equals:",
                   ["$367$", "$433$", "$467$"],
                   "$605 = 500 + 90 + 15$; subtract: $367$, receipted by $367 + 238 = 605$ ✓. $433$ flipped columns; $467$ forgot to reduce the hundreds.",
                   ["Eq(500 + 90 + 15, 605)", "Eq(605 - 238, 367)", "Eq(367 + 238, 605)"]),
                tp("$700 - 463$ equals:",
                   ["$237$", "$363$", "$337$"],
                   "$700 = 600 + 90 + 10$; subtract: $237$, and $237 + 463 = 700$ ✓. $363$ flipped the columns.",
                   ["Eq(700 - 463, 237)", "Eq(237 + 463, 700)"]),
                tp("$1\\,000 - 674$ equals:",
                   ["$326$", "$336$", "$436$"],
                   "$1\\,000 = 900 + 90 + 10$ — three doors open in a row. Subtract: $326$, receipted by $326 + 674 = 1\\,000$ ✓.",
                   ["Eq(900 + 90 + 10, 1000)", "Eq(1000 - 674, 326)", "Eq(326 + 674, 1000)"]),
                tp("$4\\,006 - 1\\,879$ equals:",
                   ["$2\\,127$", "$3\\,873$", "$3\\,127$"],
                   "$4\\,006 = 3\\,000 + 900 + 90 + 16$ — the borrow walks through both zeros. Subtract: $2\\,127$, receipted by $2\\,127 + 1\\,879 = 4\\,006$ ✓. $3\\,873$ flipped every column; $3\\,127$ forgot to reduce the thousands after lending.",
                   ["Eq(3000 + 900 + 90 + 16, 4006)", "Eq(4006 - 1879, 2127)",
                    "Eq(2127 + 1879, 4006)"]),
            ]),
            tapq("Check the outfit", "To compute $503 - 168$, the $503$ regroups as:",
                 ["$4$ hundreds, $9$ tens, $13$ ones",
                  "$5$ hundreds, $0$ tens, $13$ ones",
                  "$4$ hundreds, $0$ tens, $13$ ones",
                  "$5$ hundreds, $9$ tens, $3$ ones"],
                 "Only the first still totals $503$: $400 + 90 + 13 = 503$ ✓. The second claims $500 + 13 = 513$, the third only $413$ — but regrouping must never change the number, only its outfit.",
                 ["Eq(400 + 90 + 13, 503)", "Eq(500 + 13, 513)", "Ne(513, 503)", "Eq(400 + 13, 413)", "Ne(413, 503)"]),
            recap([
                "The top number is the one being cut — never flip a column.",
                "Top digit short? Open a ten; zeros pass the borrow to the next door.",
                "Check every regroup: the new outfit must total the same number.",
                "The add-back receipt, every time: difference + subtracted = start.",
                "A flipped or leaky answer fails its receipt instantly.",
            ]),
            tip("No subtraction is finished until its receipt is signed: add your answer to the number you took away, and watch the starting number reappear."),
            tryitset("Mixed practice", "Regrouping, zeros, and a receipt for every answer.", [
                tp("$542 - 267$ equals:",
                   ["$275$", "$325$", "$285$"],
                   "Ones $12 - 7 = 5$; tens $13 - 6 = 7$; hundreds $4 - 2 = 2$: $275$, and $275 + 267 = 542$ ✓. $325$ flipped the columns.",
                   ["Eq(542 - 267, 275)", "Eq(275 + 267, 542)"]),
                tp("$806 - 359$ equals:",
                   ["$447$", "$553$", "$457$"],
                   "Through the zero: $806 = 700 + 90 + 16$; subtract to $447$, receipted by $447 + 359 = 806$ ✓.",
                   ["Eq(700 + 90 + 16, 806)", "Eq(806 - 359, 447)", "Eq(447 + 359, 806)"]),
                tp("$903 - 457$ equals:",
                   ["$446$", "$554$", "$456$"],
                   "$903 = 800 + 90 + 13$; subtract to $446$, and $446 + 457 = 903$ ✓. $554$ flipped every column.",
                   ["Eq(903 - 457, 446)", "Eq(446 + 457, 903)"]),
                tp("$1\\,200 - 745$ equals:",
                   ["$455$", "$545$", "$465$"],
                   "$1\\,200 = 1\\,100 + 90 + 10$; subtract to $455$, receipted by $455 + 745 = 1\\,200$ ✓.",
                   ["Eq(1100 + 90 + 10, 1200)", "Eq(1200 - 745, 455)", "Eq(455 + 745, 1200)"]),
                tp("A ger camp steamed $500$ buuz for a feast; $268$ were eaten. How many are left?",
                   ["$232$", "$368$", "$342$"],
                   "What is left is a subtraction: $500 - 268 = 232$, receipted by $232 + 268 = 500$ ✓. $368$ flipped the columns.",
                   ["Eq(500 - 268, 232)", "Eq(232 + 268, 500)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Column Subtraction\"",
                    "Regroup when the top runs short, walk borrows through zeros, and let every difference sign its add-back receipt. Next: leaving the columns behind — the mental moves that make many of these sums faster than paper.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Mental Strategies
# ==========================================================================

def lesson_mental_strategies():
    # Make-ten jump: j_a + j_b, filling j_a up to the round j_mid.
    j_a, j_b = 48, 27
    j_fill = 2
    j_mid = j_a + j_fill        # 50
    j_end = j_a + j_b           # 75
    fig_maketen = fig_numline(
        [(j_a, str(j_a)), (j_mid, "+%d" % j_fill), (j_end, str(j_end), C_GREEN)],
        lo=40, hi=80)
    # Compensation jump: c0 + 99 = c0 + 100 - 1.
    c0 = 356
    c_over = c0 + 100           # 456
    c_end = c_over - 1          # 455
    fig_comp = fig_numline(
        [(c0, str(c0)), (c_over, "+100"), (c_end, str(c_end), C_WARM)],
        lo=350, hi=460)
    return {
        "slug": "mental-strategies",
        "title": "Mental Strategies",
        "concreteComparison": (
            "To pay $99$ togrog you do not count out ninety-nine "
            "coins — you hand over a hundred and take one back. Mental "
            "arithmetic works the same way: slide the numbers to a "
            "round, friendly place, do the easy sum there, and settle "
            "the small difference after. The answer never changes; "
            "only the road gets smoother."),
        "objective": (
            "Add and subtract in your head using make-ten, "
            "near-doubles, and compensation — moving amounts between "
            "numbers and giving back overshoots — with a number-line "
            "picture of every jump."),
        "concept": [
            "**Make a ten: jump to round ground.** $48 + 27$: move $2$ "
            "out of the $27$ to fill $48$ up to $50$, then jump the "
            "easy $25$: $50 + 25 = 75$. What one number gains, the "
            "other must lose — the total never moves.",
            "**Near-doubles ride a known fact.** $47 + 48$ sits next "
            "to a double you already own: $47 + 47 = 94$, so one more "
            "makes $95$. Spot neighbours and let the double carry the "
            "load.",
            "**Compensation overshoots on purpose.** Adding $99$ is "
            "awkward; adding $100$ is instant: $356 + 100 = 456$, "
            "then give the extra $1$ back — $455$. Subtracting works "
            "too: for $725 - 98$, jump back the round $100$ — $725 - "
            "100 = 625$ took $2$ too many, so hand $2$ back: $627$.",
        ],
        "keyIdea": (
            "Slide the sum to round ground — fill tens, lean on "
            "doubles, overshoot to hundreds — and always settle the "
            "difference you moved."),
        "facts": [
            {"title": "Make a ten",
             "latex": "48 + 27 = 48 + 2 + 25 = 50 + 25 = 75",
             "explanation": "The 2 that fills 48 to 50 comes out of the 27 — totals never change when amounts just move."},
            {"title": "Compensation",
             "latex": "356 + 99 = 356 + 100 - 1 = 455",
             "explanation": "Overshoot to the round hundred, then give the extra 1 back."},
        ],
        "workedExamples": [
            {"id": "g4as-l3-we1",
             "statement": "Compute $48 + 27$ in your head with the make-ten strategy.",
             "note": "Fill 48 up to the next round ten first.",
             "solution": ("Take $2$ from the $27$: $48 + 2 = 50$, and $25$ remains "
                          "to add (because $2 + 25 = 27$). Then $50 + 25 = 75$. "
                          "One tidy jump to round ground, one easy jump after."),
             "badges": [{"text": "core"}],
             "check": ["Eq(48 + 2, 50)", "Eq(2 + 25, 27)", "Eq(50 + 25, 75)",
                       "Eq(48 + 27, 75)"]},
            {"id": "g4as-l3-we2",
             "statement": "Compute $356 + 99$ with compensation.",
             "note": "99 is 100 with 1 to give back.",
             "solution": ("Overshoot: $356 + 100 = 456$. Give the extra $1$ back: "
                          "$456 - 1 = 455$ (and $455 + 1 = 456$ confirms the "
                          "settle). So $356 + 99 = 455$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(356 + 100, 456)", "Eq(456 - 1, 455)", "Eq(455 + 1, 456)",
                       "Eq(356 + 99, 455)"]},
        ],
        "commonMistakes": [
            {"text": "Moving an amount without taking it from anywhere — 48 + 27 computed as 50 + 27.",
             "correction": "The 2 that filled 48 up to 50 came OUT of the 27: what remains is 25, and 50 + 25 = 75. What one number gains, the other must lose.",
             "authored": True},
            {"text": "Settling the wrong way after subtracting — 725 − 98 finished as 625 − 2.",
             "correction": "Subtracting 100 took away 2 TOO MANY, so give the 2 back: 625 + 2 = 627. The receipt confirms it: 627 + 98 = 725.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4as-l3-t1",
             "statement": "Compute $65 + 29$ with make-ten.",
             "solution": "Take $5$ from the $29$: $65 + 5 = 70$, and $24$ remains ($5 + 24 = 29$). Then $70 + 24 = 94$.",
             "check": ["Eq(65 + 5, 70)", "Eq(5 + 24, 29)", "Eq(70 + 24, 94)", "Eq(65 + 29, 94)"]},
            {"id": "g4as-l3-t2",
             "statement": "Compute $725 - 98$ with compensation, and receipt the answer.",
             "solution": "$725 - 100 = 625$ — that took $2$ too many, so give them back: $625 + 2 = 627$. Receipt: $627 + 98 = 725$ ✓.",
             "check": ["Eq(725 - 100, 625)", "Eq(625 + 100, 725)", "Eq(625 + 2, 627)",
                       "Eq(725 - 98, 627)", "Eq(627 + 98, 725)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Fill the ten, lean on a double", [
                "See $%d + %d$ on the number line: standing at $%d$, the next round ten is $%d$ — just $%d$ away. Take that $%d$ out of the $%d$ and jump to round ground." % (j_a, j_b, j_a, j_mid, j_fill, j_fill, j_b),
                "From $%d$ the rest is easy: $25$ remains (because $2 + 25 = 27$), and $%d + 25 = %d$. Two friendly jumps instead of one awkward one." % (j_mid, j_mid, j_end),
                "Near-doubles pull the same trick with a fact you own: $47 + 48$ leans on $47 + 47 = 94$ — one more makes $95$. Move amounts, lean on rounds and doubles; the total never changes.",
            ]), fig_maketen),
            workedset("Jumps to round ground",
                      "Fill the ten; let a double do the lifting.", [
                wex("Compute $48 + 27$ with make-ten.",
                    ["Fill: $48 + 2 = 50$; the $27$ keeps $25$.",
                     "Jump: $50 + 25 = 75$."],
                    "$75$",
                    ["Eq(48 + 2, 50)", "Eq(50 + 25, 75)", "Eq(48 + 27, 75)"]),
                wex("Compute $47 + 48$ with a near-double.",
                    ["Double first: $47 + 47 = 94$.",
                     "$48$ is one more than $47$: $94 + 1 = 95$."],
                    "$95$",
                    ["Eq(47 + 47, 94)", "Eq(94 + 1, 95)", "Eq(47 + 48, 95)"]),
            ]),
            tryitset("Slide and jump", "Move an amount, then jump round-to-round.", [
                tp("$36 + 48$ equals:",
                   ["$84$", "$86$", "$74$"],
                   "Fill $48$ to $50$ with $2$ from the $36$ — $34$ remains ($34 + 2 = 36$): $50 + 34 = 84$. Choosing $86$ counts the moved $2$ twice ($50 + 36$).",
                   ["Eq(34 + 2, 36)", "Eq(50 + 34, 84)", "Eq(36 + 48, 84)", "Eq(50 + 36, 86)"]),
                tp("$65 + 29$ equals:",
                   ["$94$", "$95$", "$84$"],
                   "Take $5$ from the $29$: $65 + 5 = 70$, then $70 + 24 = 94$. Answering $95$ jumps $65 + 30$ and never gives the extra $1$ back.",
                   ["Eq(65 + 5, 70)", "Eq(70 + 24, 94)", "Eq(65 + 29, 94)", "Eq(65 + 30, 95)"]),
                tp("$25 + 26$ equals:",
                   ["$51$", "$50$", "$52$"],
                   "Double: $25 + 25 = 50$; one more: $51$. $50$ is the bare double — the extra $1$ still wants in.",
                   ["Eq(25 + 25, 50)", "Eq(50 + 1, 51)", "Eq(25 + 26, 51)"]),
            ]),
            tapq("Pick the move", "Which move computes $57 + 36$ by MAKING A TEN?",
                 ["move $3$ into the $57$: $60 + 33 = 93$",
                  "move $6$ into the $57$: $63 + 30 = 93$",
                  "add the tens and stop: $50 + 30 = 80$",
                  "double the $57$"],
                 "The next round ten above $57$ is $60$ — exactly $3$ away, and the $3$ comes out of the $36$: $60 + 33 = 93$. Moving $6$ lands on $63$ — the total survives, but there is no round ground to stand on. Adding only the tens abandons $13$.",
                 ["Eq(57 + 3, 60)", "Eq(60 + 33, 93)", "Eq(57 + 36, 93)",
                  "Eq(63 + 30, 93)", "Eq(50 + 30, 80)"]),
            funfact("Fingers named the digits",
                    "The Latin word for finger is digitus — and that is exactly why the symbols $0$ to $9$ are called DIGITS. People counted on ten fingers, numbers settled into a ten-based system, and the fingers' own name stuck to the figures. Every make-ten jump lands on the base your hands built."),
            withfig(teach("Concept B", "Overshoot and settle", [
                "Compensation on the line: to add $99$, overshoot with one big jump of $100$ — $%d + 100 = %d$ — then step $1$ back: $%d$. Big jump, small settle." % (c0, c_over, c_end),
                "Subtraction compensates too, but settle the OTHER way: $725 - 98$ — jump back $100$ to $625$; that removed $2$ too many, so walk $2$ forward: $627$.",
                "The receipt still rules the lesson: $627 + 98 = 725$ ✓. Mental shortcuts change the road, never the destination — and they never escape their receipts.",
            ]), fig_comp),
            workedset("Round jump first",
                      "Overshoot to the round number; settle the difference after.", [
                wex("Compute $467 + 199$.",
                    ["$467 + 200 = 667$.",
                     "Give the extra $1$ back: $666$."],
                    "$666$",
                    ["Eq(467 + 200, 667)", "Eq(667 - 1, 666)", "Eq(666 + 1, 667)",
                     "Eq(467 + 199, 666)"]),
                wex("Compute $843 - 299$, receipted.",
                    ["$843 - 300 = 543$ — that took $1$ too many.",
                     "Give it back: $544$. Receipt: $544 + 299 = 843$ ✓."],
                    "$544$",
                    ["Eq(843 - 300, 543)", "Eq(543 + 300, 843)", "Eq(543 + 1, 544)",
                     "Eq(843 - 299, 544)", "Eq(544 + 299, 843)"]),
            ]),
            tryitset("Settle the difference", "Which way does the settle go? Say it before you jump.", [
                tp("$534 + 98$ equals:",
                   ["$632$", "$634$", "$622$"],
                   "$534 + 100 = 634$, then give the $2$ back: $632$ ($632 + 2 = 634$ confirms). Stopping at $634$ keeps the borrowed $2$.",
                   ["Eq(534 + 100, 634)", "Eq(634 - 2, 632)", "Eq(632 + 2, 634)",
                    "Eq(534 + 98, 632)"]),
                tp("$500 - 199$ equals:",
                   ["$301$", "$299$", "$300$"],
                   "$500 - 200 = 300$ took $1$ too many — give it back: $301$, receipted by $301 + 199 = 500$ ✓. $299$ settled the wrong way.",
                   ["Eq(500 - 200, 300)", "Eq(300 + 200, 500)", "Eq(300 + 1, 301)",
                    "Eq(500 - 199, 301)", "Eq(301 + 199, 500)"]),
                tp("$276 + 99$ equals:",
                   ["$375$", "$376$", "$275$"],
                   "$276 + 100 = 376$, give $1$ back: $375$ ($375 + 1 = 376$). $376$ keeps the borrowed $1$; $275$ subtracted $1$ from $276$ and never added the hundred.",
                   ["Eq(276 + 100, 376)", "Eq(376 - 1, 375)", "Eq(375 + 1, 376)",
                    "Eq(276 + 99, 375)"]),
            ]),
            tapq("Settle the right way", "For $700 - 298$, Naran computes $700 - 300 = 400$, then takes $2$ MORE off and answers $398$. The truth:",
                 ["taking $300$ removed $2$ too many — give them back: $402$",
                  "$398$ is right — overshoots always subtract again",
                  "$400$ was already the answer",
                  "compensation never works on subtraction"],
                 "Removing $300$ removes MORE than $298$, so the running answer is $2$ too small: settle forward, $400 + 2 = 402$. Receipt: $402 + 298 = 700$ ✓. Settling backward doubles the error instead of fixing it.",
                 ["Eq(700 - 300, 400)", "Eq(400 + 300, 700)", "Eq(400 + 2, 402)",
                  "Eq(700 - 298, 402)", "Eq(402 + 298, 700)", "Ne(398, 402)"]),
            recap([
                "Make a ten: move just enough to reach round ground — the moved amount comes OUT of the other number.",
                "Near-doubles: compute the double you know, then adjust by 1.",
                "Compensation: overshoot to a round number, then settle — back after adding too much, forward after subtracting too much.",
                "Mental shortcuts change the road, never the total — receipts still apply.",
            ]),
            tip("Before each one, say the move you chose — fill the ten, lean on a double, or overshoot and settle. Naming the road is half the trip."),
            tryitset("Mixed practice", "All three tools; pick the smoothest road.", [
                tp("$38 + 45$ equals:",
                   ["$83$", "$85$", "$73$"],
                   "Fill $38$ to $40$ with $2$ from the $45$ — $43$ remains ($43 + 2 = 45$): $40 + 43 = 83$. $85$ counts the moved $2$ twice.",
                   ["Eq(38 + 2, 40)", "Eq(43 + 2, 45)", "Eq(40 + 43, 83)", "Eq(38 + 45, 83)"]),
                tp("$348 + 99$ equals:",
                   ["$447$", "$448$", "$347$"],
                   "$348 + 100 = 448$, give $1$ back: $447$ ($447 + 1 = 448$). $448$ keeps the borrowed $1$.",
                   ["Eq(348 + 100, 448)", "Eq(448 - 1, 447)", "Eq(447 + 1, 448)",
                    "Eq(348 + 99, 447)"]),
                tp("$75 + 76$ equals:",
                   ["$151$", "$150$", "$141$"],
                   "Near-double: $75 + 75 = 150$, one more: $151$. $150$ is the bare double.",
                   ["Eq(75 + 75, 150)", "Eq(150 + 1, 151)", "Eq(75 + 76, 151)"]),
                tp("$632 - 98$ equals:",
                   ["$534$", "$530$", "$532$"],
                   "$632 - 100 = 532$, give the $2$ back: $534$, receipted by $534 + 98 = 632$ ✓. $530$ settled the wrong way; $532$ never settled.",
                   ["Eq(632 - 100, 532)", "Eq(532 + 100, 632)", "Eq(532 + 2, 534)",
                    "Eq(632 - 98, 534)", "Eq(534 + 98, 632)"]),
                tp("$999 + 999$ equals:",
                   ["$1\\,998$", "$2\\,000$", "$1\\,988$"],
                   "Overshoot twice: $1\\,000 + 1\\,000 = 2\\,000$, then give back $1 + 1 = 2$: $1\\,998$ — the same ceiling column addition met. $2\\,000$ keeps the borrowed $2$.",
                   ["Eq(1000 + 1000, 2000)", "Eq(2000 - 2, 1998)", "Eq(1998 + 2, 2000)",
                    "Eq(999 + 999, 1998)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Mental Strategies\"",
                    "Fill the ten, lean on a double, overshoot and settle — three roads to the same honest total. Next: equations with a missing number, where the receipt idea stops checking answers and starts FINDING them.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Missing Numbers
# ==========================================================================

def lesson_missing_numbers():
    whole, part_a, part_b = 91, 53, 38
    fig_family = fig_geo(
        [P("W", 5, 7.4, str(whole)),
         P("A", 1.8, 2, str(part_a)),
         P("B", 8.2, 2, str(part_b))],
        poly(["W", "A", "B"], color=C_ACCENT),
        height=190)
    # Counting-up jumps for the box in [box] + 38 = 91.
    g0, g_end = part_b, whole                      # 38 -> 91
    g_j1, g_j2, g_j3 = 2, 50, 1                    # 38 -> 40 -> 90 -> 91
    fig_countup = fig_numline(
        [(g0, str(g0)), (g0 + g_j1, "+%d" % g_j1),
         (g0 + g_j1 + g_j2, "+%d" % g_j2), (g_end, str(g_end), C_GREEN)],
        lo=30, hi=100)
    return {
        "slug": "missing-numbers",
        "title": "Missing Numbers",
        "concreteComparison": (
            "Three numbers — $53$, $38$ and their whole $91$ — live "
            "like a small family in one ger: know any two and you "
            "know the third. Cover the $91$: the parts rebuild it. "
            "Cover the $53$: the whole gives it back as $91 - 38$. "
            "Three numbers, four facts, and no strangers allowed in."),
        "objective": (
            "Read a fact family as four faces of one fact, and solve "
            "box equations like $\\square + 38 = 91$ with the inverse "
            "operation — always checking by substitution."),
        "concept": [
            "**Three numbers, four facts.** $53$, $38$ and $91$ hold "
            "together: $53 + 38 = 91$, $38 + 53 = 91$, $91 - 38 = "
            "53$, $91 - 53 = 38$. Two additions, two subtractions — "
            "one triangle of numbers wearing four outfits.",
            "**The inverse opens the box.** $\\square + 38 = 91$ "
            "hides a family member. Addition put the $38$ in; "
            "subtraction takes it out: $\\square = 91 - 38 = 53$. And "
            "when the box was cut — $\\square - 47 = 129$ — addition "
            "restores it: $\\square = 129 + 47 = 176$.",
            "**Substitution is the receipt.** An answer for the box "
            "is only an OFFER until you put it back in: $53 + 38 = "
            "91$ ✓ — now it is a fact. Substitute every time; a wrong "
            "box fails its own equation on the spot.",
        ],
        "keyIdea": (
            "A fact family is one fact wearing four outfits — so a "
            "box equation is solved by the family member that undoes "
            "it, and proved by substitution."),
        "facts": [
            {"title": "One family, four facts",
             "latex": "53 + 38 = 91 \\quad 38 + 53 = 91 \\quad 91 - 38 = 53 \\quad 91 - 53 = 38",
             "explanation": "The whole stands alone on its side; the parts join together."},
            {"title": "The inverse opens the box",
             "latex": "\\square + 38 = 91 \\ \\Rightarrow \\ \\square = 91 - 38 = 53",
             "explanation": "Undo the addition with a subtraction — then substitute to check."},
        ],
        "workedExamples": [
            {"id": "g4as-l4-we1",
             "statement": "Write the four facts of the family $53$, $38$, $91$.",
             "note": "Two additions, two subtractions.",
             "solution": ("$53 + 38 = 91$ and $38 + 53 = 91$; $91 - 38 = 53$ and "
                          "$91 - 53 = 38$. The whole ($91$) always stands alone on "
                          "one side of the equals sign."),
             "badges": [{"text": "core"}],
             "check": ["Eq(53 + 38, 91)", "Eq(38 + 53, 91)", "Eq(91 - 38, 53)",
                       "Eq(91 - 53, 38)"]},
            {"id": "g4as-l4-we2",
             "statement": "Solve $\\square - 47 = 129$, and check by substitution.",
             "note": "The box was cut by 47 and still shows 129 — it started bigger.",
             "solution": ("Undo the cut with addition: $\\square = 129 + 47 = 176$. "
                          "Substitute: $176 - 47 = 129$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(129 + 47, 176)", "Eq(176 - 47, 129)"]},
        ],
        "commonMistakes": [
            {"text": "Adding whatever two numbers appear — solving □ + 38 = 91 as 91 + 38 = 129.",
             "correction": "The box and 38 TOGETHER make 91, so the box is smaller than 91: undo with 91 − 38 = 53, and substitute: 53 + 38 = 91 ✓.",
             "authored": True},
            {"text": "Subtracting on □ − 47 = 129 because the equation shows a minus sign.",
             "correction": "The box LOST 47 and still has 129 — it started bigger: □ = 129 + 47 = 176. Undo what the equation DID, not what its sign looks like.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4as-l4-t1",
             "statement": "Write the four facts of the family $160$, $340$, $500$.",
             "solution": "$340 + 160 = 500$, $160 + 340 = 500$, $500 - 160 = 340$, $500 - 340 = 160$.",
             "check": ["Eq(340 + 160, 500)", "Eq(160 + 340, 500)", "Eq(500 - 160, 340)",
                       "Eq(500 - 340, 160)"]},
            {"id": "g4as-l4-t2",
             "statement": "Solve $\\square + 260 = 730$ and substitute to check.",
             "solution": "Undo the added $260$: $\\square = 730 - 260 = 470$. Substitute: $470 + 260 = 730$ ✓.",
             "check": ["Eq(730 - 260, 470)", "Eq(470 + 260, 730)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Three numbers, four facts", [
                "Put the three numbers on a triangle: the whole $%d$ on top, the parts $%d$ and $%d$ below. That one triangle holds FOUR facts." % (whole, part_a, part_b),
                "Adding reads it upward — $%d + %d = %d$ and $%d + %d = %d$. Subtracting reads it downward — $%d - %d = %d$ and $%d - %d = %d$." % (
                    part_a, part_b, whole, part_b, part_a, whole,
                    whole, part_b, part_a, whole, part_a, part_b),
                "Cover any corner and the other two rebuild it. That is the secret of this whole lesson: addition and subtraction are ONE fact read in different directions.",
            ]), fig_family),
            workedset("Four outfits",
                      "The whole on top, parts below — four readings.", [
                wex("List the family of $27$, $45$, $72$.",
                    ["$27 + 45 = 72$ and $45 + 27 = 72$.",
                     "$72 - 45 = 27$ and $72 - 27 = 45$."],
                    "four facts",
                    ["Eq(27 + 45, 72)", "Eq(45 + 27, 72)", "Eq(72 - 45, 27)",
                     "Eq(72 - 27, 45)"]),
                wex("The family of $285$, $460$, $745$ — write its two subtractions.",
                    ["The whole is $745$, the largest.",
                     "$745 - 285 = 460$ and $745 - 460 = 285$ — each receipted by $285 + 460 = 745$."],
                    "$745 - 285 = 460$ and $745 - 460 = 285$",
                    ["Eq(285 + 460, 745)", "Eq(745 - 285, 460)", "Eq(745 - 460, 285)"]),
            ]),
            tryitset("Family members only", "The whole stands alone; the parts join.", [
                tp("Which fact belongs to the family of $27$, $45$, $72$?",
                   ["$72 - 45 = 27$", "$45 - 27 = 18$", "$27 + 72 = 99$"],
                   "The whole $72$ stands alone: $72 - 45 = 27$ ✓ (receipt $27 + 45 = 72$). The other two drag in strangers — $18$ and $99$ are not family members.",
                   ["Eq(72 - 45, 27)", "Eq(27 + 45, 72)", "Eq(45 - 27, 18)", "Eq(18 + 27, 45)",
                    "Eq(27 + 72, 99)"]),
                tp("In the family of $160$, $340$, $500$, one subtraction fact is:",
                   ["$500 - 160 = 340$", "$500 - 340 = 260$", "$340 - 160 = 500$"],
                   "The whole $500$ gives up a part: $500 - 160 = 340$ ✓ (receipt $340 + 160 = 500$). The middle claim misses: $500 - 340 = 160$, not $260$. And $340 - 160$ could never GROW to $500$.",
                   ["Eq(500 - 160, 340)", "Eq(340 + 160, 500)", "Eq(500 - 340, 160)"]),
                tp("Two members of a family are $250$ and $480$, with $480$ the whole. The third member is:",
                   ["$230$", "$730$", "$330$"],
                   "Part = whole minus part: $480 - 250 = 230$, receipted by $230 + 250 = 480$ ✓. $730$ ADDED the two — but a part can never outgrow its whole.",
                   ["Eq(480 - 250, 230)", "Eq(230 + 250, 480)", "Eq(250 + 480, 730)"]),
            ]),
            tapq("Count the outfits", "How many facts does the family $16$, $59$, $75$ hold?",
                 ["four — two additions and two subtractions",
                  "two — one of each",
                  "one big one",
                  "three — one for each number"],
                 "$16 + 59 = 75$, $59 + 16 = 75$, $75 - 59 = 16$, $75 - 16 = 59$: four faces of one fact. Learn one triangle, own four equations.",
                 ["Eq(16 + 59, 75)", "Eq(59 + 16, 75)", "Eq(75 - 59, 16)", "Eq(75 - 16, 59)"]),
            funfact("Two little lines",
                    "The $=$ sign was invented in the 1500s by Robert Recorde, a Welsh mathematician. He chose a pair of parallel lines of one length because, he wrote, no two things can be more equal. Every fact family you write balances on his little invention."),
            teach("Concept B", "Boxes opened by the inverse", [
                "$\\square + 38 = 91$ is a family with one corner hidden. Do not guess — the INVERSE digs it out: subtraction undoes addition, so $\\square = 91 - 38 = 53$.",
                "When the box was cut, addition restores it: $\\square - 47 = 129$ means the box LOST $47$ and still shows $129$ — so $\\square = 129 + 47 = 176$. Read what happened to the box, then do the opposite.",
                "Always SUBSTITUTE the answer back: $53 + 38 = 91$ ✓ and $176 - 47 = 129$ ✓. Substitution is the receipt in its smartest clothes.",
            ]),
            workedset("Undo, then substitute",
                      "Read what happened to the box; do the opposite.", [
                withfig(wex("Solve $\\square + %d = %d$." % (g0, g_end),
                    ["The box gained $%d$; take it away: $\\square = %d - %d = 53$. Counting up agrees: $%d$ to $40$ is $%d$, to $90$ is $%d$ more, to $%d$ is $%d$ more — $%d + %d + %d = 53$." % (
                        g0, g_end, g0, g0, g_j1, g_j2, g_end, g_j3, g_j1, g_j2, g_j3),
                     "Substitute: $53 + %d = %d$ ✓." % (g0, g_end)],
                    "$53$",
                    ["Eq(91 - 38, 53)", "Eq(2 + 50 + 1, 53)", "Eq(53 + 38, 91)"]),
                    fig_countup),
                wex("Solve $620 - \\square = 265$.",
                    ["$620$ lost the box and kept $265$ — so the box and $265$ are the two parts of $620$: $\\square = 620 - 265 = 355$.",
                     "Substitute: $620 - 355 = 265$ ✓."],
                    "$355$",
                    ["Eq(620 - 265, 355)", "Eq(355 + 265, 620)", "Eq(620 - 355, 265)"]),
            ]),
            tryitset("Open the box", "Inverse first, substitution always.", [
                tp("$\\square + 260 = 730$. The box holds:",
                   ["$470$", "$990$", "$530$"],
                   "Undo the added $260$: $730 - 260 = 470$; substitute $470 + 260 = 730$ ✓. $990$ ADDED instead ($730 + 260$) — but a box that gains $260$ to reach $730$ must start below $730$.",
                   ["Eq(730 - 260, 470)", "Eq(470 + 260, 730)", "Eq(730 + 260, 990)"]),
                tp("$\\square - 155 = 245$. The box holds:",
                   ["$400$", "$90$", "$300$"],
                   "The box lost $155$ and kept $245$: restore it — $245 + 155 = 400$; substitute $400 - 155 = 245$ ✓. $90$ comes from $245 - 155$ — undoing in the wrong direction.",
                   ["Eq(245 + 155, 400)", "Eq(400 - 155, 245)", "Eq(245 - 155, 90)",
                    "Eq(90 + 155, 245)"]),
                tp("$1\\,000 - \\square = 386$. The box holds:",
                   ["$614$", "$1\\,386$", "$724$"],
                   "The box and $386$ are the two parts of $1\\,000$: $\\square = 1\\,000 - 386 = 614$; substitute $1\\,000 - 614 = 386$ ✓.",
                   ["Eq(1000 - 386, 614)", "Eq(614 + 386, 1000)", "Eq(1000 - 614, 386)"]),
            ]),
            tapq("Substitution catches it", "$\\square - 84 = 312$. Otgo answers $228$, from computing $312 - 84$. What does substitution say?",
                 ["$228 - 84 = 144$, not $312$ — the box must be $312 + 84 = 396$",
                  "$228 - 84 = 312$ — the answer passes",
                  "substitution cannot test box equations",
                  "the equation has no answer"],
                 "Put the offer back: $228 - 84 = 144$, not $312$ — rejected. The box LOST $84$, so restore by adding: $312 + 84 = 396$, and indeed $396 - 84 = 312$ ✓. The minus sign in the equation does not mean YOU subtract — undo what the equation did.",
                 ["Eq(228 - 84, 144)", "Eq(144 + 84, 228)", "Ne(144, 312)",
                  "Eq(312 + 84, 396)", "Eq(396 - 84, 312)"]),
            recap([
                "Three numbers, four facts: two additions, two subtractions — one triangle.",
                "The whole stands alone on its side; parts join together.",
                "Open a box with the inverse: undo what the equation DID to it.",
                "Substitute every answer back — a wrong box fails its own equation.",
                "Addition and subtraction are one fact read two ways: that is the whole machinery.",
            ]),
            tip("For each box, first say aloud what happened to it — 'the box gained 260', 'the box lost 155' — then do the opposite, and substitute to sign the receipt."),
            tryitset("Mixed practice", "Families and boxes, receipts throughout.", [
                tp("Which addition belongs to the family $125$, $375$, $500$?",
                   ["$125 + 375 = 500$", "$125 + 500 = 625$", "$375 + 500 = 875$"],
                   "Parts join to make the whole: $125 + 375 = 500$ ✓. The others add the whole itself to a part, making the strangers $625$ and $875$.",
                   ["Eq(125 + 375, 500)", "Eq(125 + 500, 625)", "Eq(375 + 500, 875)"]),
                tp("$\\square + 476 = 900$. The box holds:",
                   ["$424$", "$1\\,376$", "$524$"],
                   "$900 - 476 = 424$; substitute $424 + 476 = 900$ ✓. $1\\,376$ added the two numbers.",
                   ["Eq(900 - 476, 424)", "Eq(424 + 476, 900)", "Eq(900 + 476, 1376)"]),
                tp("$\\square - 238 = 517$. The box holds:",
                   ["$755$", "$279$", "$745$"],
                   "The box lost $238$: restore it — $517 + 238 = 755$; substitute $755 - 238 = 517$ ✓. $279$ subtracted instead ($517 - 238$).",
                   ["Eq(517 + 238, 755)", "Eq(755 - 238, 517)", "Eq(517 - 238, 279)",
                    "Eq(279 + 238, 517)"]),
                tp("$903 - \\square = 447$. The box holds:",
                   ["$456$", "$1\\,350$", "$556$"],
                   "The box and $447$ are the parts of $903$: $903 - 447 = 456$; substitute $903 - 456 = 447$ ✓. $1\\,350$ added.",
                   ["Eq(903 - 447, 456)", "Eq(456 + 447, 903)", "Eq(903 - 456, 447)"]),
                tp("Saruul had some togrog saved. She spent $350$ on a hair clip and has $480$ left. How much did she start with?",
                   ["$830$", "$130$", "$730$"],
                   "The story is a box equation: $\\square - 350 = 480$. Restore: $480 + 350 = 830$; substitute $830 - 350 = 480$ ✓. $130$ subtracted the story's numbers — but spending REDUCED her savings, so the start must be the biggest number of the three.",
                   ["Eq(480 + 350, 830)", "Eq(830 - 350, 480)", "Eq(480 - 350, 130)",
                    "Eq(130 + 350, 480)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Missing Numbers\"",
                    "Fact families gave you the inverse; boxes taught substitution. Last lesson: stories — where the numbers arrive dressed as sheep, togrog and Naadam tickets, and YOU choose the operation.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Word Problems
# ==========================================================================

def lesson_word_problems():
    sheep_n, goat_n = 8, 5
    fig_flock = fig_groups(
        (sheep_n, "sheep", C_ACCENT),
        (goat_n, "goats", C_WARM))
    sheep2, goat2 = 14, 9
    fig_flock2 = fig_groups(
        (sheep2, "sheep", C_ACCENT),
        (goat2, "goats", C_WARM))
    return {
        "slug": "word-problems",
        "title": "Word Problems",
        "concreteComparison": (
            "Two questions about the same pen of animals: 'how many "
            "altogether?' wants the flocks JOINED — addition; 'how "
            "many more sheep than goats?' wants the gap measured — "
            "subtraction. The numbers are identical; the STORY picks "
            "the operation. Reading the story's shape is the real "
            "work; the arithmetic afterwards is last week's job."),
        "objective": (
            "Solve one- and two-step word problems inside 10 000 — "
            "reading the story's shape to choose addition or "
            "subtraction, finding hidden numbers first, and "
            "receipting every answer."),
        "concept": [
            "**The story picks the operation.** Joining shapes — "
            "altogether, in all, total, gained, more arrive — ADD. Gap "
            "shapes — how many more X than Y, how many fewer X than Y, "
            "how many left — SUBTRACT. One word decides nothing: "
            "'more' joins in '$29$ more arrive' and measures a gap in "
            "'how many more sheep than goats'. Read the whole question "
            "sentence.",
            "**Two-step stories hide a number.** 'Spent $1\\,250$ and "
            "then $850$ out of $3\\,600$' hides the TOTAL SPENT: find "
            "it first ($2\\,100$), then answer the real question "
            "($3\\,600 - 2\\,100 = 1\\,500$). Name the hidden number "
            "before touching any arithmetic.",
            "**Every answer carries a receipt.** One step or two: add "
            "the answer back, or walk the other road — $3\\,600 - "
            "1\\,250 - 850$ lands on the same $1\\,500$. Two roads "
            "agreeing is the strongest receipt there is.",
        ],
        "keyIdea": (
            "Read the story's shape, find the hidden number first, "
            "and receipt every answer — two roads to the same number "
            "make it true."),
        "facts": [
            {"title": "Story shapes",
             "latex": "\\text{altogether, in all} \\to + \\qquad \\text{how many more X than Y, how many left} \\to -",
             "explanation": "Joining stories add; gap and taking-away stories subtract. The word 'more' on its own is NOT a subtraction signal — '29 more arrive' joins."},
            {"title": "Two steps, one receipt",
             "latex": "3\\,600 - (1\\,250 + 850) = 1\\,500",
             "explanation": "Find the hidden total first; then receipt: 1500 + 2100 rebuilds 3600."},
        ],
        "workedExamples": [
            {"id": "g4as-l5-we1",
             "statement": "A herder's flock holds $1\\,250$ sheep and $860$ goats. How many animals altogether?",
             "note": "Altogether is a joining shape.",
             "solution": ("Join the flocks: $1\\,250 + 860 = 2\\,110$ animals. "
                          "Other-way check: $860 + 1\\,250 = 2\\,110$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1250 + 860, 2110)", "Eq(860 + 1250, 2110)"]},
            {"id": "g4as-l5-we2",
             "statement": "Bilguun saves $3\\,600$ togrog. At the market he buys a notebook for $1\\,250$ and a pen for $850$. How much is left?",
             "note": "Two steps — the total cost is hidden.",
             "solution": ("Hidden number, the total cost: $1\\,250 + 850 = "
                          "2\\,100$. Then $3\\,600 - 2\\,100 = 1\\,500$ togrog "
                          "left. Receipts: $1\\,500 + 2\\,100 = 3\\,600$ ✓, and "
                          "the second road $3\\,600 - 1\\,250 - 850 = 1\\,500$ "
                          "agrees ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1250 + 850, 2100)", "Eq(3600 - 2100, 1500)",
                       "Eq(1500 + 2100, 3600)", "Eq(3600 - 1250 - 850, 1500)"]},
        ],
        "commonMistakes": [
            {"text": "Grabbing the two numbers and adding, whatever the question asks.",
             "correction": "The STORY chooses the operation: joining shapes add; 'how many more X than Y' and 'how many left' subtract. Read the question sentence twice before touching the numbers — 'more' on its own can join ('29 more arrive') or measure a gap.",
             "authored": True},
            {"text": "Stopping after step one of a two-step problem.",
             "correction": "Ask: does my number answer THE question, or a stepping-stone question? 380 + 295 = 675 khuushuur SOLD is the stepping stone; 850 − 675 = 175 LEFT answers the question.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4as-l5-t1",
             "statement": "At the wrestling, $875$ spectators are watching; $390$ leave for the horse race. How many stay? Receipt your answer.",
             "solution": "A leaving shape subtracts: $875 - 390 = 485$ stay. Receipt: $485 + 390 = 875$ ✓.",
             "check": ["Eq(875 - 390, 485)", "Eq(485 + 390, 875)"]},
            {"id": "g4as-l5-t2",
             "statement": "A library holds $1\\,480$ books. It receives $260$ new ones, then lends out $575$. How many are on the shelves?",
             "solution": "Step 1: $1\\,480 + 260 = 1\\,740$. Step 2: $1\\,740 - 575 = 1\\,165$ books. Receipt: $1\\,165 + 575 = 1\\,740$ ✓.",
             "check": ["Eq(1480 + 260, 1740)", "Eq(1740 - 575, 1165)", "Eq(1165 + 575, 1740)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Read the story's shape", [
                "By the ger graze $%d$ sheep and $%d$ goats. 'How many animals ALTOGETHER?' joins the groups: $%d + %d = 13$. Joining words — altogether, in all, total, gained — always add." % (sheep_n, goat_n, sheep_n, goat_n),
                "Same animals, different question: 'how many MORE sheep THAN goats?' measures the gap: $%d - %d = 3$. Gap phrases — 'how many more X than Y', 'how many fewer X than Y', 'how many left', 'how many remain' — subtract." % (sheep_n, goat_n),
                "Watch out for the word 'more' on its own: it can JOIN instead. '$29$ more guests arrive' adds. Only the whole phrase 'how many more X THAN Y' asks for a gap — so read the phrase, never one word.",
                "The numbers never choose the operation; the story's SHAPE does. Read the question sentence twice, name the shape, then compute — and receipt: $3 + 5 = 8$ ✓.",
            ]), fig_flock),
            workedset("One-step stories",
                      "Name the shape first; compute second; receipt third.", [
                wex("$1\\,250$ sheep and $860$ goats — how many animals altogether?",
                    ["Joining shape: add. $1\\,250 + 860 = 2\\,110$.",
                     "Other-way check: $860 + 1\\,250 = 2\\,110$ ✓."],
                    "$2\\,110$ animals",
                    ["Eq(1250 + 860, 2110)", "Eq(860 + 1250, 2110)"]),
                wex("$875$ spectators are watching the wrestling; $390$ leave. How many stay?",
                    ["Leaving shape: subtract. $875 - 390 = 485$.",
                     "Receipt: $485 + 390 = 875$ ✓."],
                    "$485$ spectators",
                    ["Eq(875 - 390, 485)", "Eq(485 + 390, 875)"]),
            ]),
            tryitset("Joining or gap?", "The question sentence decides.", [
                withfig(tp("By the river graze $%d$ sheep and $%d$ goats. How many animals altogether?" % (sheep2, goat2),
                   ["$23$ animals", "$5$ animals", "$22$ animals"],
                   "Altogether joins: $14 + 9 = 23$. Answering $5$ measured the gap ($14 - 9 = 5$, since $5 + 9 = 14$) — the wrong shape for this question.",
                   ["Eq(14 + 9, 23)", "Eq(14 - 9, 5)", "Eq(5 + 9, 14)"]),
                   fig_flock2),
                tp("A school has $468$ girls and $415$ boys. How many MORE girls than boys?",
                   ["$53$", "$883$", "$63$"],
                   "'How many more' is a gap: $468 - 415 = 53$, receipted by $53 + 415 = 468$ ✓. $883$ joined the groups — the altogether answer to a gap question.",
                   ["Eq(468 - 415, 53)", "Eq(53 + 415, 468)", "Eq(468 + 415, 883)"]),
                tp("$2\\,500$ Naadam tickets were printed and $1\\,730$ sold. How many are unsold?",
                   ["$770$", "$4\\,230$", "$830$"],
                   "Unsold is what is LEFT: $2\\,500 - 1\\,730 = 770$, receipted by $770 + 1\\,730 = 2\\,500$ ✓. $4\\,230$ added the story's numbers.",
                   ["Eq(2500 - 1730, 770)", "Eq(770 + 1730, 2500)", "Eq(2500 + 1730, 4230)"]),
            ]),
            tapq("Spot the shape", "Which story needs SUBTRACTION?",
                 ["Tuya had $900$ togrog and spent $350$ — how much is left?",
                  "A pen holds $12$ sheep and $8$ goats — how many animals in all?",
                  "Bat read $365$ pages last month and $120$ this month — how many altogether?",
                  "A herd of $56$ horses gains $40$ foals — how big is it now?"],
                 "'Spent, and how much is LEFT' takes away: $900 - 350 = 550$, receipt $550 + 350 = 900$ ✓. The other three all JOIN amounts: $12 + 8 = 20$, $365 + 120 = 485$, $56 + 40 = 96$.",
                 ["Eq(900 - 350, 550)", "Eq(550 + 350, 900)", "Eq(12 + 8, 20)",
                  "Eq(365 + 120, 485)", "Eq(56 + 40, 96)"]),
            funfact("The three games of Naadam",
                    "Naadam, Mongolia's great summer festival, centres on three sports: wrestling, horse racing and archery. The long-distance horse races are ridden by child jockeys across open steppe rather than around a track. And the stands are full of arithmetic — scores, distances and ticket counts all day long."),
            teach("Concept B", "Two-step stories", [
                "Some stories will not solve in one move: 'Bilguun has $3\\,600$ togrog and buys a notebook for $1\\,250$ and a pen for $850$ — how much is left?' The cost of BOTH things is hidden. Name it, then find it: $1\\,250 + 850 = 2\\,100$.",
                "Now the real question is one step: $3\\,600 - 2\\,100 = 1\\,500$ togrog left. Step one finds the hidden number; step two answers the question.",
                "Receipt with two roads: subtracting the prices one at a time — $3\\,600 - 1\\,250 = 2\\,350$, then $2\\,350 - 850 = 1\\,500$ — lands on the same answer. Two roads agreeing is the strongest receipt there is.",
            ]),
            workedset("Hidden numbers",
                      "Find what the story hides; then answer what it asks.", [
                wex("Bilguun has $3\\,600$ togrog and buys a notebook for $1\\,250$ and a pen for $850$. How much is left?",
                    ["Hidden: total cost $1\\,250 + 850 = 2\\,100$.",
                     "Answer: $3\\,600 - 2\\,100 = 1\\,500$ togrog. Second road: $3\\,600 - 1\\,250 - 850 = 1\\,500$ ✓."],
                    "$1\\,500$ togrog",
                    ["Eq(1250 + 850, 2100)", "Eq(3600 - 2100, 1500)",
                     "Eq(1500 + 2100, 3600)", "Eq(3600 - 1250 - 850, 1500)"]),
                wex("A library holds $1\\,480$ books; $260$ new ones arrive, then $575$ are lent out. How many remain?",
                    ["Step 1 — arrivals join: $1\\,480 + 260 = 1\\,740$.",
                     "Step 2 — lending leaves: $1\\,740 - 575 = 1\\,165$ books. Receipt: $1\\,165 + 575 = 1\\,740$ ✓."],
                    "$1\\,165$ books",
                    ["Eq(1480 + 260, 1740)", "Eq(1740 - 575, 1165)", "Eq(1165 + 575, 1740)"]),
            ]),
            tryitset("Two moves, one answer", "Name the hidden number before you compute.", [
                tp("A bus carries $46$ passengers. At the market $18$ get off and $11$ get on. How many ride now?",
                   ["$39$", "$75$", "$17$"],
                   "Two steps: $46 - 18 = 28$ (receipt $28 + 18 = 46$ ✓), then $28 + 11 = 39$. $75$ added everything; $17$ subtracted everything — each ignored half the story.",
                   ["Eq(46 - 18, 28)", "Eq(28 + 18, 46)", "Eq(28 + 11, 39)",
                    "Eq(46 + 18 + 11, 75)", "Eq(46 - 18 - 11, 17)", "Eq(17 + 11 + 18, 46)"]),
                tp("A camp kitchen fried $850$ khuushuur, selling $380$ in the morning and $295$ in the afternoon. How many are left?",
                   ["$175$", "$675$", "$765$"],
                   "Hidden number — total sold: $380 + 295 = 675$. Left: $850 - 675 = 175$, receipted by $175 + 675 = 850$ ✓. $675$ stops at step one.",
                   ["Eq(380 + 295, 675)", "Eq(850 - 675, 175)", "Eq(175 + 675, 850)",
                    "Eq(850 - 380 - 295, 175)"]),
                tp("Bat picks $145$ sea buckthorn berries and his sister picks $168$. They eat $96$. How many berries remain?",
                   ["$217$", "$313$", "$207$"],
                   "Join: $145 + 168 = 313$; eat: $313 - 96 = 217$, receipted by $217 + 96 = 313$ ✓. $313$ stops at step one.",
                   ["Eq(145 + 168, 313)", "Eq(313 - 96, 217)", "Eq(217 + 96, 313)"]),
            ]),
            tapq("Finish the story", "In the khuushuur story, Zaya answers $675$. What happened?",
                 ["she stopped at step one — $675$ is the amount SOLD, but the question asks what is LEFT: $850 - 675 = 175$",
                  "nothing — $675$ is the final answer",
                  "she should have added the $850$ as well",
                  "the story cannot be solved without more information"],
                 "Step one's result answers a stepping-stone question, not the story's question. Re-read the final sentence: LEFT means subtract the sold total from $850$ — $175$, receipted by $175 + 675 = 850$ ✓.",
                 ["Eq(380 + 295, 675)", "Eq(850 - 675, 175)", "Eq(175 + 675, 850)"]),
            recap([
                "Joining shapes (altogether, in all, gained, more arrive) add; gap shapes (how many more X than Y, how many fewer X than Y, how many left) subtract.",
                "The numbers never pick the operation — the question sentence does. 'More' by itself decides nothing: read the whole phrase.",
                "Two-step stories hide a number: name it, find it, THEN answer the question.",
                "Receipt every answer — add it back, or walk the second road and watch the answers agree.",
                "An answer without a receipt is an offer, not a fact.",
            ]),
            tip("Underline the question sentence, say the shape aloud, and after computing ask: did I answer THE question, or a stepping stone?"),
            tryitset("Mixed practice", "Stories of every shape, receipts on every answer.", [
                tp("$1\\,675$ adults and $980$ children watched the horse race finish. How many spectators altogether?",
                   ["$2\\,655$", "$695$", "$2\\,555$"],
                   "Joining shape: $1\\,675 + 980 = 2\\,655$, and the other way $980 + 1\\,675$ agrees ✓. $695$ measured the gap ($1\\,675 - 980 = 695$, since $695 + 980 = 1\\,675$).",
                   ["Eq(1675 + 980, 2655)", "Eq(980 + 1675, 2655)", "Eq(1675 - 980, 695)",
                    "Eq(695 + 980, 1675)"]),
                tp("A book costs $3\\,250$ togrog; Oyun pays with a $5\\,000$ note. Her change is:",
                   ["$1\\,750$", "$8\\,250$", "$2\\,250$"],
                   "Change is what is left of the note: $5\\,000 - 3\\,250 = 1\\,750$, receipted the cashier's way: $1\\,750 + 3\\,250 = 5\\,000$ ✓. $8\\,250$ added the price to the note.",
                   ["Eq(5000 - 3250, 1750)", "Eq(1750 + 3250, 5000)", "Eq(5000 + 3250, 8250)"]),
                tp("A shelf holds $248$ books; $67$ are borrowed, then $35$ returned books come back. How many stand on the shelf?",
                   ["$216$", "$146$", "$350$"],
                   "$248 - 67 = 181$ (receipt $181 + 67 = 248$ ✓), then $181 + 35 = 216$. $146$ subtracted both numbers; $350$ added both.",
                   ["Eq(248 - 67, 181)", "Eq(181 + 67, 248)", "Eq(181 + 35, 216)",
                    "Eq(248 - 67 - 35, 146)", "Eq(146 + 35 + 67, 248)", "Eq(248 + 67 + 35, 350)"]),
                tp("Sarnai's book has $900$ pages. She reads $356$ pages one week and $288$ the next. How many pages are left?",
                   ["$256$", "$644$", "$344$"],
                   "Hidden number — pages read: $356 + 288 = 644$. Left: $900 - 644 = 256$, receipted by $256 + 644 = 900$ ✓. $644$ stops at step one.",
                   ["Eq(356 + 288, 644)", "Eq(900 - 644, 256)", "Eq(256 + 644, 900)"]),
                tp("The ger camp had $78$ guests; $29$ more arrive for Naadam. Which operation, and how many now?",
                   ["add — $78 + 29 = 107$ guests", "subtract — $78 - 29 = 49$ guests", "add — $78 + 29 = 97$ guests"],
                   "Arriving guests JOIN: $78 + 29 = 107$ (make-ten: $78 + 2 = 80$, then $80 + 27 = 107$). Here 'more' means 'more arrive', a joining word — the gap phrase would be 'how many MORE guests THAN yesterday'. So the subtraction $78 - 29 = 49$ reads the story backwards; $97$ drops the carry.",
                   ["Eq(78 + 29, 107)", "Eq(78 + 2, 80)", "Eq(80 + 27, 107)",
                    "Eq(78 - 29, 49)", "Eq(49 + 29, 78)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Word Problems\" — and the whole topic",
                    "Column addition, column subtraction, mental shortcuts, fact families, and stories: five lessons circling one idea — addition and subtraction are one fact read two ways, so every answer can sign its own receipt. Multiplication picks up the story from here.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    # Compensation jump for pr5: c0 + 399 = c0 + 400 - 1.
    c0 = 456
    c_over = c0 + 400            # 856
    c_end = c_over - 1           # 855
    fig_pr5 = fig_numline(
        [(c0, str(c0)), (c_over, "+400"), (c_end, str(c_end), C_WARM)],
        lo=450, hi=900)
    return [
        prob("g4as-pr1", "Compute $476 + 358$ in columns, then check by adding the other way.",
             "Ones $6 + 8 = 14$; tens $7 + 5 + 1 = 13$; hundreds $4 + 3 + 1 = 8$: total $834$. Other way: $358 + 476 = 834$ ✓.",
             ["Eq(6 + 8, 14)", "Eq(476 + 358, 834)", "Eq(358 + 476, 834)"]),
        prob("g4as-pr2", "Compute $685 + 777$.",
             "Ones $5 + 7 = 12$; tens $8 + 7 + 1 = 16$; hundreds $6 + 7 + 1 = 14$: total $1\\,462$. Check: $777 + 685 = 1\\,462$ ✓.",
             ["Eq(685 + 777, 1462)", "Eq(777 + 685, 1462)"]),
        prob("g4as-pr3", "Compute $823 - 457$ and sign the receipt.",
             "Ones $13 - 7 = 6$; tens $11 - 5 = 6$; hundreds $7 - 4 = 3$: answer $366$. Receipt: $366 + 457 = 823$ ✓.",
             ["Eq(13 - 7, 6)", "Eq(6 + 7, 13)", "Eq(823 - 457, 366)", "Eq(366 + 457, 823)"]),
        prob("g4as-pr4", "Compute $904 - 568$, showing the regrouped outfit of $904$ first.",
             "$904 = 800 + 90 + 14$ (check: still $904$). Subtract: $14 - 8 = 6$, $9 - 6 = 3$, $8 - 5 = 3$ — answer $336$. Receipt: $336 + 568 = 904$ ✓.",
             ["Eq(800 + 90 + 14, 904)", "Eq(904 - 568, 336)", "Eq(336 + 568, 904)"]),
        withfig(
            prob("g4as-pr5", "Compute $456 + 399$ in your head, with compensation.",
                 "Overshoot: $456 + 400 = 856$; give the extra $1$ back: $855$ (and $855 + 1 = 856$ confirms the settle). So $456 + 399 = 855$.",
                 ["Eq(456 + 400, 856)", "Eq(856 - 1, 855)", "Eq(855 + 1, 856)",
                  "Eq(456 + 399, 855)"]),
            fig_pr5),
        prob("g4as-pr6", "Solve $\\square - 260 = 480$ and substitute to check.",
             "The box lost $260$: restore it — $480 + 260 = 740$. Substitute: $740 - 260 = 480$ ✓.",
             ["Eq(480 + 260, 740)", "Eq(740 - 260, 480)"]),
        prob("g4as-pr7", "$1\\,265$ adults and $985$ children watched the archery at Naadam. How many spectators altogether?",
             "Joining shape: $1\\,265 + 985 = 2\\,250$. Other-way check: $985 + 1\\,265 = 2\\,250$ ✓.",
             ["Eq(1265 + 985, 2250)", "Eq(985 + 1265, 2250)"]),
        prob("g4as-pr8", "Tuya brings $5\\,000$ togrog to the bookshop and buys a book for $2\\,350$ and a pencil case for $1\\,425$. How much does she carry home?",
             "Hidden number — the total cost: $2\\,350 + 1\\,425 = 3\\,775$. Left: $5\\,000 - 3\\,775 = 1\\,225$ togrog. Receipts: $1\\,225 + 3\\,775 = 5\\,000$ ✓, and the second road $5\\,000 - 2\\,350 - 1\\,425 = 1\\,225$ agrees ✓.",
             ["Eq(2350 + 1425, 3775)", "Eq(5000 - 3775, 1225)", "Eq(1225 + 3775, 5000)",
              "Eq(5000 - 2350 - 1425, 1225)"]),
    ]


def test_bank():
    return [
        prob("g4as-x1", "Compute $2\\,486 + 3\\,957$, checked by adding the other way.",
             "Ones $6 + 7 = 13$; tens $8 + 5 + 1 = 14$; hundreds $4 + 9 + 1 = 14$; thousands $2 + 3 + 1 = 6$: total $6\\,443$. Other way: $3\\,957 + 2\\,486 = 6\\,443$ ✓.",
             ["Eq(2486 + 3957, 6443)", "Eq(3957 + 2486, 6443)"]),
        prob("g4as-x2", "Compute $6\\,004 - 2\\,758$ and sign the receipt.",
             "Regroup through the zeros: $6\\,004 = 5\\,000 + 900 + 90 + 14$ (check: still $6\\,004$). Subtract: $14 - 8 = 6$, $9 - 5 = 4$, $9 - 7 = 2$, $5 - 2 = 3$ — answer $3\\,246$. Receipt: $3\\,246 + 2\\,758 = 6\\,004$ ✓.",
             ["Eq(5000 + 900 + 90 + 14, 6004)", "Eq(6004 - 2758, 3246)",
              "Eq(3246 + 2758, 6004)"]),
        prob("g4as-x3", "Compute in your head, naming the strategy: $647 + 99$, then $835 - 97$.",
             "Compensation both times. $647 + 100 = 747$, give $1$ back: $746$. And $835 - 100 = 735$ took $3$ too many, so give them back: $735 + 3 = 738$. Receipt: $738 + 97 = 835$ ✓.",
             ["Eq(647 + 100, 747)", "Eq(747 - 1, 746)", "Eq(746 + 1, 747)", "Eq(647 + 99, 746)",
              "Eq(835 - 100, 735)", "Eq(735 + 100, 835)", "Eq(735 + 3, 738)",
              "Eq(835 - 97, 738)", "Eq(738 + 97, 835)"]),
        prob("g4as-x4", "Write the four facts of the family $245$, $380$, $625$.",
             "$245 + 380 = 625$, $380 + 245 = 625$, $625 - 380 = 245$, $625 - 245 = 380$ — one fact, four readings.",
             ["Eq(245 + 380, 625)", "Eq(380 + 245, 625)", "Eq(625 - 380, 245)",
              "Eq(625 - 245, 380)"]),
        prob("g4as-x5", "Solve $173 + \\square = 902$ and substitute to check.",
             "Undo the added $173$: $\\square = 902 - 173 = 729$. Substitute: $173 + 729 = 902$ ✓.",
             ["Eq(902 - 173, 729)", "Eq(173 + 729, 902)"]),
        prob("g4as-x6", "A herd of $2\\,400$ animals holds $1\\,350$ sheep; the rest are goats. After $275$ goats are sold, how many goats remain?",
             "Hidden number — the goats: $2\\,400 - 1\\,350 = 1\\,050$ (receipt $1\\,050 + 1\\,350 = 2\\,400$ ✓). Then $1\\,050 - 275 = 775$ goats remain (receipt $775 + 275 = 1\\,050$ ✓).",
             ["Eq(2400 - 1350, 1050)", "Eq(1050 + 1350, 2400)", "Eq(1050 - 275, 775)",
              "Eq(775 + 275, 1050)"]),
    ]


def main():
    topic = {
        "slug": "addition-and-subtraction",
        "title": "Addition & Subtraction",
        "grade": 4,
        "status": "published",
        "blurb": ("Column addition and subtraction with regrouping inside "
                  "10 000, mental strategies, missing-number fact families, "
                  "and one- and two-step word problems."),
        "lessons": [
            lesson_column_addition(),
            lesson_column_subtraction(),
            lesson_mental_strategies(),
            lesson_missing_numbers(),
            lesson_word_problems(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "addition-and-subtraction.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
