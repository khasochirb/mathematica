#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 2: Addition & Subtraction.

Multi-digit addition and subtraction with regrouping, the mental
strategies that beat the written method on friendly numbers, the
add/subtract inverse relationship (and the checking habit it gives),
and multi-step word problems.

Through-line: REGROUPING IS TRADING. A carry is ten of one place traded
for one of the next; a borrow is the same trade run backwards. Once
that trade is visible, the written algorithms stop being magic — and
the mental strategies are just smarter trades.

Same construction as build_place_value.py: every check anywhere in the
structure is sympy-asserted BEFORE the JSON is written. Subtractions
additionally carry their addition inverse as a check (answer + subtrahend
== minuend), so a wrong difference cannot ship.

Run: python3 scripts/grade4/build_addition_subtraction.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (C_ACCENT, C_GREEN, C_NEUTRAL, C_WARM, withfig,  # noqa: E402
                     fig_barchart, fig_groups, fig_numline,
                     funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic)


# ==========================================================================
# Lesson 1 — Adding with Regrouping
# ==========================================================================

def lesson_adding():
    return {
        "slug": "adding-with-regrouping",
        "title": "Adding with Regrouping",
        "concreteComparison": (
            "Two herder families combine their flocks for the winter: "
            "$4\\,586$ sheep and $2\\,747$ sheep. Nobody counts the merged "
            "flock from scratch — you ADD, place by place, and whenever a "
            "place overflows past nine you trade ten of it for one of the "
            "next place up. That trade is the carry, and it is the only "
            "new move in all of column addition."),
        "objective": (
            "Add multi-digit numbers with the column method, carrying "
            "(regrouping) through any number of places, and add three or "
            "more numbers by grouping them cleverly."),
        "concept": [
            "**Line up the places.** Column addition works because ones "
            "add with ones, tens with tens, hundreds with hundreds — the "
            "place-value ladder from Topic 1 doing bookkeeping.",
            "**Carry = trade ten for one.** When a column's sum passes "
            "$9$ — say $6 + 7 = 13$ — you cannot write two digits in one "
            "place. Trade: ten ones become one ten. Write the $3$, carry "
            "the $1$ into the tens column.",
            "**Order is yours to choose.** Addition doesn't care about "
            "order or grouping, so with three numbers, pair the friendly "
            "ones first: $618 + 254 + 382$ goes fastest as $(618 + 382) "
            "+ 254 = 1\\,000 + 254$.",
        ],
        "keyIdea": (
            "Add place by place from the ones; when a column passes nine, "
            "trade ten of it for one of the next place — that's the carry, "
            "and it's the whole algorithm."),
        "facts": [
            {"title": "The carry",
             "latex": "6 + 7 = 13 \\;\\Rightarrow\\; \\text{write } 3,\\ \\text{carry } 1",
             "explanation": "Ten ones trade for one ten — the sum keeps one digit per place."},
            {"title": "Group the friendly pair",
             "latex": "618 + 254 + 382 = (618 + 382) + 254 = 1\\,000 + 254",
             "explanation": "Addition lets you reorder and regroup — hunt for sums that make round numbers."},
        ],
        "workedExamples": [
            {"id": "g5as-l1-we1",
             "statement": "Add $4\\,586 + 2\\,747$ with the column method.",
             "note": "Watch the carry travel through three columns.",
             "solution": ("Ones: $6 + 7 = 13$ — write $3$, carry $1$. Tens: $8 + 4 "
                          "+ 1 = 13$ — write $3$, carry $1$. Hundreds: $5 + 7 + 1 = "
                          "13$ — write $3$, carry $1$. Thousands: $4 + 2 + 1 = 7$. "
                          "Sum: $7\\,333$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6 + 7, 13)", "Eq(8 + 4 + 1, 13)", "Eq(5 + 7 + 1, 13)",
                       "Eq(4 + 2 + 1, 7)", "Eq(4586 + 2747, 7333)"]},
            {"id": "g5as-l1-we2",
             "statement": "A tent costs $12\\,485$ tögrög and a stove $9\\,635$. What do they cost together?",
             "note": "Different lengths — align by place, not by first digit.",
             "solution": ("Line up the ones: $12\\,485 + 9\\,635$. Ones: $5 + 5 = 10$ "
                          "— write $0$, carry $1$. Tens: $8 + 3 + 1 = 12$. Hundreds: "
                          "$4 + 6 + 1 = 11$. Thousands: $2 + 9 + 1 = 12$. "
                          "Ten-thousands: $1 + 1 = 2$. Total: $22\\,120$ tögrög."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5 + 5, 10)", "Eq(12485 + 9635, 22120)"]},
        ],
        "commonMistakes": [
            {"text": "Writing the whole two-digit column sum in one place — 6 + 7 = 13, so writing \"13\".",
             "correction": "One digit per place. Write the 3, TRADE the ten: carry 1 into the next column.",
             "authored": True},
            {"text": "Lining numbers up by their first digits instead of their last.",
             "correction": "Align the ONES (the right edge). 12,485 + 9,635 lines the 5 under the 5 — the 9 sits under the 2, not under the 1.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5as-l1-t1",
             "statement": "Add $3\\,668 + 1\\,554$.",
             "solution": "Ones $8+4=12$ (carry), tens $6+5+1=12$ (carry), hundreds $6+5+1=12$ (carry), thousands $3+1+1=5$: $5\\,222$.",
             "check": ["Eq(3668 + 1554, 5222)"]},
            {"id": "g5as-l1-t2",
             "statement": "Compute $618 + 254 + 382$ the clever way.",
             "solution": "Pair the friendly two first: $618 + 382 = 1\\,000$, then $1\\,000 + 254 = 1\\,254$.",
             "check": ["Eq(618 + 382, 1000)", "Eq(618 + 254 + 382, 1254)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The carry is a trade", [
                "Column addition adds place by place, starting from the ones — the place-value ladder doing bookkeeping.",
                "When a column passes $9$, you cannot write two digits in one place. TRADE ten of it for one of the next place: $6 + 7 = 13$ → write $3$, carry $1$.",
                "The carry is not a rule to memorise — it is ten ones becoming one ten, the Topic 1 trade in action.",
            ]), fig_groups((10, "10 ones become...", C_WARM), (1, "...1 ten", C_ACCENT))),
            workedset("Carries in action",
                      "Ones first; trade every overflow upward.", [
                wex("Add $4\\,586 + 2\\,747$.",
                    ["Ones: $6 + 7 = 13$ — write $3$, carry $1$.",
                     "Tens: $8 + 4 + 1 = 13$ — write $3$, carry $1$. Hundreds: $5 + 7 + 1 = 13$ — write $3$, carry $1$.",
                     "Thousands: $4 + 2 + 1 = 7$. Sum: $7\\,333$."],
                    "$7\\,333$",
                    ["Eq(6 + 7, 13)", "Eq(4586 + 2747, 7333)"]),
                wex("Add $12\\,485 + 9\\,635$ (different lengths).",
                    ["Align the ONES, not the first digits.",
                     "Column by column with carries: $22\\,120$."],
                    "$22\\,120$", ["Eq(12485 + 9635, 22120)"]),
            ]),
            tryitset("Column sums", "Ones first — and let the carries travel.", [
                tp("$3\\,668 + 1\\,554$ equals:",
                   ["$5\\,222$", "$5\\,212$", "$4\\,222$"],
                   "Three carries in a row: $5\\,222$. (Dropping the tens carry gives $5\\,212$ — the classic slip.)",
                   ["Eq(3668 + 1554, 5222)"]),
                tp("$7\\,849 + 1\\,163$ equals:",
                   ["$9\\,012$", "$8\\,912$", "$9\\,002$"],
                   "Ones $9+3=12$, tens $4+6+1=11$, hundreds $8+1+1=10$, thousands $7+1+1=9$: $9\\,012$.",
                   ["Eq(7849 + 1163, 9012)"]),
                tp("$25\\,706 + 4\\,518$ equals:",
                   ["$30\\,224$", "$29\\,224$", "$30\\,214$"],
                   "Align by the ones: $25\\,706 + 4\\,518 = 30\\,224$ — the thousands column carries into the ten-thousands.",
                   ["Eq(25706 + 4518, 30224)"]),
            ]),
            tapq("Where does the 1 go?",
                 "In the ones column you get $8 + 5 = 13$. What do you write, and what do you carry?",
                 ["write $3$, carry $1$ ten", "write $13$ in the ones", "write $1$, carry $3$", "write $3$, carry nothing"],
                 "Thirteen ones trade into one ten and three ones: the $3$ stays in the ones place, the $1$ joins the tens column.",
                 ["Eq(8 + 5, 13)", "Eq(13, 10 + 3)"]),
            funfact("The abacus carries the same way",
                    "On a Mongolian abacus (самбар тоолуур), when a rod fills past nine you clear it and push one bead on the next rod — a physical carry. The written algorithm is the abacus move in pencil form; both are the ten-for-one trade."),
            withfig(teach("Concept B", "Three numbers? Choose your order", [
                "Addition doesn't care about order or grouping — so with several numbers, YOU choose the friendliest path.",
                "$618 + 254 + 382$: spot the pair that makes a round number — $618 + 382 = 1\\,000$ — then $1\\,000 + 254 = 1\\,254$.",
                "Hunting for pairs that make tens, hundreds or thousands turns long sums into short ones.",
            ]), fig_groups((7, "7", C_ACCENT), (3, "3 — pairs to 10", C_WARM), (8, "8", C_GREEN))),
            workedset("Friendly pairs first",
                      "Reorder to build round numbers, then finish.", [
                wex("Compute $618 + 254 + 382$.",
                    ["Friendly pair: $618 + 382 = 1\\,000$.",
                     "Then $1\\,000 + 254 = 1\\,254$."],
                    "$1\\,254$",
                    ["Eq(618 + 382, 1000)", "Eq(618 + 254 + 382, 1254)"]),
                wex("Compute $175 + 493 + 325$.",
                    ["$175 + 325 = 500$ — the friendly pair.",
                     "$500 + 493 = 993$."],
                    "$993$",
                    ["Eq(175 + 325, 500)", "Eq(175 + 493 + 325, 993)"]),
            ]),
            tryitset("Pick the pair", "Find the round-number pair before adding anything.", [
                tp("The fastest first move for $246 + 588 + 754$ is:",
                   ["$246 + 754 = 1\\,000$", "$246 + 588$ first", "add left to right"],
                   "$246 + 754 = 1\\,000$, then $1\\,588$. The other orders work but fight the carries.",
                   ["Eq(246 + 754, 1000)", "Eq(246 + 588 + 754, 1588)"]),
                tp("$460 + 380 + 540$ equals:",
                   ["$1\\,380$", "$1\\,280$", "$1\\,480$"],
                   "$460 + 540 = 1\\,000$, then $+ 380$: $1\\,380$.",
                   ["Eq(460 + 540, 1000)", "Eq(460 + 380 + 540, 1380)"]),
                tp("$127 + 205 + 373 + 95$ equals:",
                   ["$800$", "$790$", "$810$"],
                   "Two friendly pairs: $127 + 373 = 500$ and $205 + 95 = 300$ — total $800$.",
                   ["Eq(127 + 373, 500)", "Eq(205 + 95, 300)", "Eq(127 + 205 + 373 + 95, 800)"]),
            ]),
            tapq("Does order matter?", "Which is TRUE about $a + b + c$?",
                 ["any order gives the same sum", "you must add left to right",
                  "the biggest number must go first", "order changes the answer"],
                 "Addition is commutative and associative — every order and grouping gives the same total, so pick the friendliest: e.g. $2 + 9 + 8 = (2 + 8) + 9 = 19$.",
                 ["Eq(2 + 9 + 8, 19)", "Eq((2 + 8) + 9, 19)"]),
            recap([
                "Add place by place, starting from the ones.",
                "A column past nine trades ten for one — write the digit, carry the 1.",
                "Align numbers by their ONES, never their first digits.",
                "With several numbers, pair the ones that make round numbers first.",
            ]),
            tip("Mixed column sums — say the carry out loud each time it happens; the dropped carry is this lesson's only real enemy."),
            tryitset("Mixed practice", "Carries and clever grouping together.", [
                tp("$5\\,378 + 2\\,845$ equals:",
                   ["$8\\,223$", "$8\\,213$", "$7\\,223$"],
                   "Three carries: $8\\,223$.",
                   ["Eq(5378 + 2845, 8223)"]),
                tp("$9\\,999 + 1$ equals:",
                   ["$10\\,000$", "$9\\,990$", "$10\\,999$"],
                   "The carry ripples through every column: four nines roll over to $10\\,000$.",
                   ["Eq(9999 + 1, 10000)"]),
                tp("$316 + 447 + 684$ equals:",
                   ["$1\\,447$", "$1\\,437$", "$1\\,347$"],
                   "$316 + 684 = 1\\,000$, then $+ 447$: $1\\,447$.",
                   ["Eq(316 + 684, 1000)", "Eq(316 + 447 + 684, 1447)"]),
                tp("A school library has $6\\,485$ books and buys $2\\,738$ more. Now it has:",
                   ["$9\\,223$ books", "$9\\,123$ books", "$8\\,223$ books"],
                   "$6\\,485 + 2\\,738 = 9\\,223$ — carries in the ones, tens and hundreds.",
                   ["Eq(6485 + 2738, 9223)"]),
                tp("$18\\,264 + 7\\,957$ equals:",
                   ["$26\\,221$", "$25\\,221$", "$26\\,211$"],
                   "$18\\,264 + 7\\,957 = 26\\,221$ — the thousands carry lifts $18$ to $26$.",
                   ["Eq(18264 + 7957, 26221)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Adding with Regrouping\"",
                    "Every carry you wrote was a ten-for-one trade up the place-value ladder. Next lesson runs the same trade BACKWARDS: subtraction, where a ten breaks back into ten ones.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Subtracting with Regrouping
# ==========================================================================

def lesson_subtracting():
    return {
        "slug": "subtracting-with-regrouping",
        "title": "Subtracting with Regrouping",
        "concreteComparison": (
            "A concert hall printed $5\\,003$ tickets and sold $1\\,647$. "
            "How many remain? Column subtraction hits a wall at once: you "
            "cannot take $7$ from $3$. The fix is the carry run backwards "
            "— BREAK one of the next place into ten of this one. Borrowing "
            "is just un-trading."),
        "objective": (
            "Subtract multi-digit numbers with the column method, "
            "borrowing (regrouping) through any place — including across "
            "zeros — and check every subtraction by adding back."),
        "concept": [
            "**Borrow = break one into ten.** When a column's top digit "
            "is too small, break one unit of the next place into ten of "
            "this place: in $52 - 38$, break a ten so the ones read "
            "$12 - 8$.",
            "**Across zeros, the break travels.** In $5\\,003 - 1\\,647$ "
            "the ones need a ten, but the tens and hundreds are $0$ — so "
            "the break walks left: a thousand breaks into ten hundreds, "
            "one of those into ten tens, one of those into ten ones.",
            "**Addition is the receipt.** Every subtraction can be "
            "checked: answer $+$ what-you-took-away must rebuild "
            "what-you-started-with. $5\\,003 - 1\\,647 = 3\\,356$ because "
            "$3\\,356 + 1\\,647 = 5\\,003$.",
        ],
        "keyIdea": (
            "Borrowing is the carry run backwards — break one of the next "
            "place into ten of this one — and every answer can be checked "
            "by adding back what was subtracted."),
        "facts": [
            {"title": "The borrow",
             "latex": "52 - 38: \\ 4\\,\\cancel{5}\\;{}^{1}2 - 38 \\;\\Rightarrow\\; 12 - 8 = 4",
             "explanation": "One ten breaks into ten ones; the tens column drops by one."},
            {"title": "The add-back check",
             "latex": "a - b = c \\iff c + b = a",
             "explanation": "The answer plus the subtracted amount must rebuild the original."},
        ],
        "workedExamples": [
            {"id": "g5as-l2-we1",
             "statement": "Subtract $8\\,254 - 3\\,478$.",
             "note": "Three borrows — watch each break.",
             "solution": ("Ones: $4 < 8$, break a ten: $14 - 8 = 6$. Tens: now $4$, "
                          "and $4 < 7$, break a hundred: $14 - 7 = 7$. Hundreds: now "
                          "$1$, and $1 < 4$, break a thousand: $11 - 4 = 7$. "
                          "Thousands: $7 - 3 = 4$. Difference: $4\\,776$. Check: "
                          "$4\\,776 + 3\\,478 = 8\\,254$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(14 - 8, 6)", "Eq(14 - 7, 7)", "Eq(11 - 4, 7)",
                       "Eq(8254 - 3478, 4776)", "Eq(4776 + 3478, 8254)"]},
            {"id": "g5as-l2-we2",
             "statement": "The hall printed $5\\,003$ tickets and sold $1\\,647$. How many remain?",
             "note": "Borrowing across two zeros.",
             "solution": ("The ones need a ten, but tens and hundreds are $0$: break "
                          "the thousand — $5\\,003$ regroups as $4$ thousands, $9$ "
                          "hundreds, $9$ tens, $13$ ones. Now subtract: $13 - 7 = 6$, "
                          "$9 - 4 = 5$, $9 - 6 = 3$, $4 - 1 = 3$: $3\\,356$ tickets. "
                          "Check: $3\\,356 + 1\\,647 = 5\\,003$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4000 + 900 + 90 + 13, 5003)", "Eq(13 - 7, 6)",
                       "Eq(5003 - 1647, 3356)", "Eq(3356 + 1647, 5003)"]},
        ],
        "commonMistakes": [
            {"text": "Flipping the digits instead of borrowing — reading 2 − 8 as \"8 − 2 = 6\".",
             "correction": "The columns are not symmetric: 52 − 38 is 14, not 26. When the top digit is smaller, BORROW; never swap.",
             "authored": True},
            {"text": "Forgetting that a borrowed-from digit shrinks by one.",
             "correction": "Breaking a ten leaves one fewer ten. Mark the break (cross out, write the new digit) — unmarked borrows are the top source of wrong answers.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5as-l2-t1",
             "statement": "Subtract $7\\,132 - 4\\,815$, then check by adding back.",
             "solution": "Borrow in the ones and hundreds: $7\\,132 - 4\\,815 = 2\\,317$. Check: $2\\,317 + 4\\,815 = 7\\,132$. ✓",
             "check": ["Eq(7132 - 4815, 2317)", "Eq(2317 + 4815, 7132)"]},
            {"id": "g5as-l2-t2",
             "statement": "Subtract $6\\,000 - 2\\,384$.",
             "solution": "Break across the zeros: $6\\,000$ becomes $5$ thousands, $9$ hundreds, $9$ tens, $10$ ones. $6\\,000 - 2\\,384 = 3\\,616$; check $3\\,616 + 2\\,384 = 6\\,000$.",
             "check": ["Eq(5000 + 900 + 90 + 10, 6000)", "Eq(6000 - 2384, 3616)",
                       "Eq(3616 + 2384, 6000)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Borrowing is the carry, backwards", [
                "When a column's top digit is too small — $2 - 8$ won't go — BREAK one of the next place into ten of this one.",
                "$52 - 38$: break a ten. The $5$ tens become $4$, the $2$ ones become $12$: now $12 - 8 = 4$ and $4 - 3 = 1$. Answer $14$.",
                "It is exactly the addition carry run in reverse: there you traded ten-for-one going up; here one breaks into ten coming down.",
            ]), fig_groups((1, "1 ten breaks into...", C_ACCENT), (10, "...10 ones", C_WARM))),
            workedset("Breaks in action",
                      "Mark every break — the lender shrinks by one.", [
                wex("Subtract $8\\,254 - 3\\,478$.",
                    ["Ones: break a ten — $14 - 8 = 6$. Tens: break a hundred — $14 - 7 = 7$.",
                     "Hundreds: break a thousand — $11 - 4 = 7$. Thousands: $7 - 3 = 4$.",
                     "Difference $4\\,776$; check $4\\,776 + 3\\,478 = 8\\,254$. ✓"],
                    "$4\\,776$",
                    ["Eq(8254 - 3478, 4776)", "Eq(4776 + 3478, 8254)"]),
                wex("Subtract $903 - 458$.",
                    ["Ones: tens are $0$, so the break travels — a hundred breaks into ten tens, one ten into ten ones: $13 - 8 = 5$.",
                     "Tens: $9 - 5 = 4$. Hundreds: $8 - 4 = 4$. Difference $445$; check $445 + 458 = 903$. ✓"],
                    "$445$",
                    ["Eq(903 - 458, 445)", "Eq(445 + 458, 903)"]),
            ]),
            tryitset("Column differences", "Borrow where needed; mark the lender.", [
                tp("$7\\,132 - 4\\,815$ equals:",
                   ["$2\\,317$", "$2\\,327$", "$3\\,317$"],
                   "Borrows in the ones and hundreds: $2\\,317$. Check: $2\\,317 + 4\\,815 = 7\\,132$.",
                   ["Eq(7132 - 4815, 2317)", "Eq(2317 + 4815, 7132)"]),
                tp("$52 - 38$ equals:",
                   ["$14$", "$26$", "$24$"],
                   "$2 - 8$ needs a borrow: $12 - 8 = 4$, then $4 - 3 = 1$. ($26$ comes from illegally flipping to $8 - 2$.)",
                   ["Eq(52 - 38, 14)", "Eq(14 + 38, 52)"]),
                tp("$9\\,406 - 2\\,159$ equals:",
                   ["$7\\,247$", "$7\\,347$", "$7\\,257$"],
                   "Break a ten for the ones ($16 - 9 = 7$); the rest follows: $7\\,247$.",
                   ["Eq(9406 - 2159, 7247)", "Eq(7247 + 2159, 9406)"]),
            ]),
            tapq("Spot the illegal flip", "A student computes $63 - 47 = 24$, reading the ones as \"$7 - 3$\". The true answer is:",
                 ["$16$", "$24$", "$26$", "$14$"],
                 "Columns don't flip: $3 - 7$ needs a borrow — $13 - 7 = 6$, then $5 - 4 = 1$: $16$. The flip error ($24$) fails the add-back check: $24 + 47 = 71 \\ne 63$.",
                 ["Eq(63 - 47, 16)", "Eq(24 + 47, 71)", "Ne(71, 63)"]),
            funfact("Cashiers subtract by adding",
                    "Old-school market change-making runs subtraction as addition: for a $6\\,350$ tögrög purchase paid with $10\\,000$, the seller counts UP — \"$6\\,350$, $6\\,400$ ($50$), $7\\,000$ ($600$), $10\\,000$ ($3\\,000$)\" — handing you $3\\,650$. Adding up IS subtraction; next lesson makes it a strategy."),
            withfig(teach("Concept B", "Zeros, and the receipt", [
                "Subtracting from a number full of zeros — $5\\,003 - 1\\,647$ — sends the break TRAVELLING: the thousand breaks into ten hundreds, one hundred into ten tens, one ten into ten ones.",
                "After the travelling break, $5\\,003$ reads as $4$ thousands, $9$ hundreds, $9$ tens, $13$ ones — and the subtraction runs smoothly.",
                "Always collect the receipt: answer $+$ subtracted $=$ original. $3\\,356 + 1\\,647 = 5\\,003$ — if the receipt fails, the subtraction was wrong.",
            ]), fig_groups((3, "3 zeros to cross", C_NEUTRAL), (10, "each becomes 10", C_WARM))),
            workedset("Across the zeros",
                      "Let the break travel, then subtract column by column.", [
                wex("Subtract $5\\,003 - 1\\,647$.",
                    ["Regroup: $5\\,003 = 4$ thousands $+ 9$ hundreds $+ 9$ tens $+ 13$ ones.",
                     "$13 - 7 = 6$, $9 - 4 = 5$, $9 - 6 = 3$, $4 - 1 = 3$: $3\\,356$.",
                     "Receipt: $3\\,356 + 1\\,647 = 5\\,003$. ✓"],
                    "$3\\,356$",
                    ["Eq(4000 + 900 + 90 + 13, 5003)", "Eq(5003 - 1647, 3356)",
                     "Eq(3356 + 1647, 5003)"]),
                wex("Subtract $6\\,000 - 2\\,384$.",
                    ["Regroup: $6\\,000 = 5$ thousands $+ 9$ hundreds $+ 9$ tens $+ 10$ ones.",
                     "$10 - 4 = 6$, $9 - 8 = 1$, $9 - 3 = 6$, $5 - 2 = 3$: $3\\,616$.",
                     "Receipt: $3\\,616 + 2\\,384 = 6\\,000$. ✓"],
                    "$3\\,616$",
                    ["Eq(6000 - 2384, 3616)", "Eq(3616 + 2384, 6000)"]),
            ]),
            tryitset("Zero-crossing subtraction", "Regroup once, then every column has enough.", [
                tp("$4\\,002 - 1\\,358$ equals:",
                   ["$2\\,644$", "$2\\,654$", "$3\\,644$"],
                   "$4\\,002$ regroups to $3$ | $9$ | $9$ | $12$: difference $2\\,644$; receipt $2\\,644 + 1\\,358 = 4\\,002$.",
                   ["Eq(4002 - 1358, 2644)", "Eq(2644 + 1358, 4002)"]),
                tp("$10\\,000 - 4\\,275$ equals:",
                   ["$5\\,725$", "$6\\,725$", "$5\\,735$"],
                   "The break travels through four zeros: $5\\,725$. Receipt: $5\\,725 + 4\\,275 = 10\\,000$.",
                   ["Eq(10000 - 4275, 5725)", "Eq(5725 + 4275, 10000)"]),
                tp("Which computation CHECKS the subtraction $802 - 356 = 446$?",
                   ["$446 + 356 = 802$", "$802 + 356 = 1\\,158$", "$446 - 356 = 90$"],
                   "The receipt: answer plus subtracted rebuilds the original — $446 + 356 = 802$. ✓",
                   ["Eq(802 - 356, 446)", "Eq(446 + 356, 802)"]),
            ]),
            tapq("The travelling break", "To subtract the ones in $700 - 258$, the ten you need comes from:",
                 ["a hundred breaking into tens, then one ten into ones",
                  "the ones column itself",
                  "adding ten to both numbers",
                  "nowhere — the subtraction is impossible"],
                 "The tens are $0$, so the break travels: one hundred → ten tens, one of those → ten ones. $700$ reads as $6$ | $9$ | $10$, and $700 - 258 = 442$.",
                 ["Eq(600 + 90 + 10, 700)", "Eq(700 - 258, 442)"]),
            recap([
                "Borrowing breaks one of the next place into ten of this one — the carry in reverse.",
                "Never flip a column: when the top digit is smaller, borrow.",
                "Across zeros, the break travels leftward until it finds a nonzero digit.",
                "Collect the receipt: answer + subtracted = original, every time.",
            ]),
            tip("Every problem below has a receipt — run it. If answer + subtracted misses the original, find the unmarked borrow."),
            tryitset("Mixed practice", "Borrows, zeros, receipts.", [
                tp("$6\\,241 - 3\\,867$ equals:",
                   ["$2\\,374$", "$2\\,384$", "$3\\,374$"],
                   "Three borrows: $2\\,374$. Receipt: $2\\,374 + 3\\,867 = 6\\,241$.",
                   ["Eq(6241 - 3867, 2374)", "Eq(2374 + 3867, 6241)"]),
                tp("$8\\,050 - 4\\,325$ equals:",
                   ["$3\\,725$", "$3\\,735$", "$4\\,725$"],
                   "Ones: $0 - 5$ needs a ten from the $5$ tens — $10 - 5 = 5$, tens now $4 - 2 = 2$. Hundreds: $0 - 3$ breaks a thousand — $10 - 3 = 7$, thousands $7 - 4 = 3$: $3\\,725$. Receipt: $3\\,725 + 4\\,325 = 8\\,050$ ✓.",
                   ["Eq(8050 - 4325, 3725)", "Eq(3725 + 4325, 8050)"]),
                tp("A granary held $9\\,000$ kg of flour and shipped $3\\,485$ kg. It still holds:",
                   ["$5\\,515$ kg", "$6\\,515$ kg", "$5\\,525$ kg"],
                   "$9\\,000 - 3\\,485 = 5\\,515$; receipt $5\\,515 + 3\\,485 = 9\\,000$.",
                   ["Eq(9000 - 3485, 5515)", "Eq(5515 + 3485, 9000)"]),
                tp("$5\\,555 - 5\\,556$ is:",
                   ["not possible with whole-number answers here — the second number is bigger",
                    "$1$", "$0$"],
                   "Subtraction of whole numbers needs the first number to be at least the second: $5\\,556 > 5\\,555$. (Negative numbers arrive in later grades.)",
                   ["5556 > 5555"]),
                tp("Which answer FAILS its receipt: someone claims $7\\,403 - 2\\,168 = 5\\,335$?",
                   ["it fails — $5\\,335 + 2\\,168 = 7\\,503$, not $7\\,403$",
                    "it passes — the receipt matches",
                    "receipts cannot check this"],
                   "$5\\,335 + 2\\,168 = 7\\,503 \\ne 7\\,403$: an unmarked borrow. The true difference is $5\\,235$.",
                   ["Eq(5335 + 2168, 7503)", "Ne(7503, 7403)", "Eq(7403 - 2168, 5235)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Subtracting with Regrouping\"",
                    "Carry up, break down — the two directions of one trade. And the receipt habit (answer + subtracted = original) will guard every subtraction you ever do. Next: doing all this in your head, faster than the written method.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Mental Strategies
# ==========================================================================

def lesson_mental():
    return {
        "slug": "mental-addition-and-subtraction",
        "title": "Mental Addition & Subtraction",
        "concreteComparison": (
            "The market price is $499$ tögrög and you buy that item plus "
            "one for $276$. No paper needed: charge yourself $500$, add "
            "$276$ to get $776$, hand back the borrowed $1$ — total "
            "$775$. Round numbers are easy numbers, and the whole art of "
            "mental arithmetic is trading your problem for a round-number "
            "one, then repaying the trade."),
        "objective": (
            "Add and subtract mentally using compensation (round, then "
            "repay), making tens and hundreds, and counting up — and "
            "choose the strategy that fits the numbers."),
        "concept": [
            "**Compensation:** move a number to the nearest round one, "
            "compute, then repay. $499 + 276$: do $500 + 276 = 776$, "
            "repay the borrowed $1$: $775$. Works for subtraction too — "
            "$1\\,995 + 2\\,468 = 2\\,000 + 2\\,468 - 5$.",
            "**Make a ten (or hundred):** split one number so a piece "
            "completes the other. $47 + 38$: take $3$ from the $38$ to "
            "complete $47 \\to 50$, then $50 + 35 = 85$.",
            "**Count up for subtraction:** the cashier's move. $1\\,000 "
            "- 674$: climb $674 \\to 700$ ($26$), then $700 \\to 1\\,000$ "
            "($300$) — total climbed $326$, and that IS the difference.",
        ],
        "keyIdea": (
            "Trade your problem for a round-number problem, then repay "
            "the trade — compensation, making tens, and counting up are "
            "all this one idea."),
        "facts": [
            {"title": "Compensation",
             "latex": "499 + 276 = (500 + 276) - 1 = 775",
             "explanation": "Round, compute, repay — the borrowed amount comes back at the end."},
            {"title": "Counting up",
             "latex": "1\\,000 - 674: \\ 674 \\xrightarrow{+26} 700 \\xrightarrow{+300} 1\\,000 \\Rightarrow 326",
             "explanation": "The distance climbed IS the difference — subtraction as a journey."},
        ],
        "workedExamples": [
            {"id": "g5as-l3-we1",
             "statement": "Compute $499 + 276$ in your head.",
             "note": "Compensate through 500.",
             "solution": ("$499$ is one short of $500$. Compute $500 + 276 = 776$, "
                          "then repay the borrowed $1$: $776 - 1 = 775$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(500 + 276, 776)", "Eq(776 - 1, 775)", "Eq(499 + 276, 775)"]},
            {"id": "g5as-l3-we2",
             "statement": "Compute $1\\,000 - 674$ by counting up.",
             "note": "Climb to the next round numbers.",
             "solution": ("$674 \\to 700$ is $26$; $700 \\to 1\\,000$ is $300$. Total "
                          "climb: $26 + 300 = 326$, so $1\\,000 - 674 = 326$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(674 + 26, 700)", "Eq(700 + 300, 1000)",
                       "Eq(26 + 300, 326)", "Eq(1000 - 674, 326)"]},
        ],
        "commonMistakes": [
            {"text": "Repaying the compensation in the wrong direction — 499 + 276 = 776 + 1.",
             "correction": "You ADDED an extra 1 when you rounded 499 up, so you must SUBTRACT it back: 775. Ask: did rounding make my problem bigger or smaller?",
             "authored": True},
            {"text": "Using the written algorithm in your head for numbers built for a strategy.",
             "correction": "Mental column-subtraction of 1,000 − 674 juggles three borrows. Counting up does it in two easy hops. Look at the NUMBERS before picking the method.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5as-l3-t1",
             "statement": "Compute $1\\,995 + 2\\,468$ mentally.",
             "solution": "Round $1\\,995 \\to 2\\,000$: $2\\,000 + 2\\,468 = 4\\,468$; repay $5$: $4\\,463$.",
             "check": ["Eq(2000 + 2468, 4468)", "Eq(4468 - 5, 4463)",
                       "Eq(1995 + 2468, 4463)"]},
            {"id": "g5as-l3-t2",
             "statement": "Compute $47 + 38 + 53$ mentally.",
             "solution": "Friendly pair first: $47 + 53 = 100$, then $100 + 38 = 138$.",
             "check": ["Eq(47 + 53, 100)", "Eq(47 + 38 + 53, 138)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Compensation — borrow a round number", [
                "Round numbers are easy numbers. Compensation trades your problem for a round one, then repays: $499 + 276 \\to 500 + 276 = 776$, repay $1$: $775$.",
                "The repay direction follows the trade: rounded UP means you added too much — subtract it back. Rounded the subtracted number up? You took too much — add it back.",
                "$3\\,000 - 1\\,998$: round $1\\,998 \\to 2\\,000$, get $1\\,000$, repay the extra $2$ you took: $1\\,002$.",
            ]), fig_numline([(0, "start"), (998, "998"), (1000, "round up"), (1002, "give back 2")], lo=0, hi=1100)),
            workedset("Round, compute, repay",
                      "Say the repay out loud — direction is everything.", [
                wex("Compute $499 + 276$.",
                    ["$500 + 276 = 776$ — but $500$ overpaid by $1$.",
                     "Repay: $776 - 1 = 775$."],
                    "$775$",
                    ["Eq(499 + 276, 775)"]),
                wex("Compute $3\\,000 - 1\\,998$.",
                    ["Take $2\\,000$ instead: $3\\,000 - 2\\,000 = 1\\,000$ — but that took $2$ too many.",
                     "Give them back: $1\\,000 + 2 = 1\\,002$."],
                    "$1\\,002$",
                    ["Eq(3000 - 2000, 1000)", "Eq(3000 - 1998, 1002)"]),
            ]),
            tryitset("Compensate", "Round to the friendliest neighbour; repay at the end.", [
                tp("$1\\,995 + 2\\,468$ equals:",
                   ["$4\\,463$", "$4\\,468$", "$4\\,473$"],
                   "$2\\,000 + 2\\,468 = 4\\,468$, repay $5$: $4\\,463$. (Forgetting the repay leaves $4\\,468$.)",
                   ["Eq(1995 + 2468, 4463)"]),
                tp("$704 - 299$ equals:",
                   ["$405$", "$395$", "$415$"],
                   "Take $300$: $704 - 300 = 404$; you took $1$ too many — return it: $405$.",
                   ["Eq(704 - 300, 404)", "Eq(704 - 299, 405)"]),
                tp("$598 + 598$ equals:",
                   ["$1\\,196$", "$1\\,200$", "$1\\,186$"],
                   "$600 + 600 = 1\\,200$, repay $2 + 2 = 4$: $1\\,196$.",
                   ["Eq(600 + 600, 1200)", "Eq(598 + 598, 1196)"]),
            ]),
            tapq("Which way is the repay?", "You compute $825 - 498$ as $825 - 500 = 325$. To finish, you:",
                 ["add $2$ — you took $2$ too many", "subtract $2$ more", "add $5$", "stop — $325$ is the answer"],
                 "Taking $500$ instead of $498$ removed $2$ extra, so give them back: $325 + 2 = 327$.",
                 ["Eq(825 - 500, 325)", "Eq(825 - 498, 327)"]),
            funfact("The 99-price trick",
                    "Shops price things at $1\\,990$ or $9\\,900$ partly because the leading digit reads small. Mental compensators are immune: you instantly see $1\\,990$ as \"$2\\,000$ minus $10$\" — and the till total stops being a surprise."),
            withfig(teach("Concept B", "Making tens, and counting up", [
                "**Make a ten:** split one addend to complete the other. $47 + 38$: move $3$ across — $50 + 35 = 85$. Nothing was rounded, so nothing to repay.",
                "**Count up** turns subtraction into a journey: $1\\,000 - 674$ climbs $674 \\to 700$ ($+26$) $\\to 1\\,000$ ($+300$): difference $326$. Two easy hops instead of three borrows.",
                "Choose by the numbers: near a round number → compensate; digits that complete each other → make tens; subtracting from a round number → count up.",
            ]), fig_numline([(47, "47"), (50, "+3 to 50"), (80, "+30 to 80")], lo=40, hi=90)),
            workedset("Two more tools",
                      "Split to complete; climb to compare.", [
                wex("Compute $47 + 38$ by making a ten.",
                    ["Move $3$ from the $38$ to complete $47 \\to 50$.",
                     "$50 + 35 = 85$."],
                    "$85$",
                    ["Eq(47 + 3, 50)", "Eq(50 + 35, 85)", "Eq(47 + 38, 85)"]),
                wex("Compute $1\\,000 - 674$ by counting up.",
                    ["$674 \\to 700$: $26$. $700 \\to 1\\,000$: $300$.",
                     "Climb total: $326$ — that IS the difference."],
                    "$326$",
                    ["Eq(26 + 300, 326)", "Eq(1000 - 674, 326)"]),
            ]),
            tryitset("Pick your tool", "Compensate, make tens, or count up — the numbers tell you.", [
                tp("$36 + 47 + 64$ equals:",
                   ["$147$", "$137$", "$157$"],
                   "$36 + 64 = 100$ — then $+ 47$: $147$.",
                   ["Eq(36 + 64, 100)", "Eq(36 + 47 + 64, 147)"]),
                tp("$500 - 238$ equals:",
                   ["$262$", "$272$", "$252$"],
                   "Count up: $238 \\to 240$ ($2$), $\\to 300$ ($60$), $\\to 500$ ($200$): $262$.",
                   ["Eq(2 + 60 + 200, 262)", "Eq(500 - 238, 262)"]),
                tp("$68 + 27$ by making a ten is:",
                   ["$95$", "$85$", "$97$"],
                   "Move $2$: $70 + 25 = 95$.",
                   ["Eq(68 + 2, 70)", "Eq(70 + 25, 95)", "Eq(68 + 27, 95)"]),
            ]),
            tapq("The cashier's move", "You pay for a $6\\,350$ item with $10\\,000$. Counting up, the change is:",
                 ["$3\\,650$", "$3\\,750$", "$4\\,650$", "$3\\,550$"],
                 "$6\\,350 \\to 6\\,400$ ($50$), $\\to 7\\,000$ ($600$), $\\to 10\\,000$ ($3\\,000$): $50 + 600 + 3\\,000 = 3\\,650$.",
                 ["Eq(50 + 600 + 3000, 3650)", "Eq(10000 - 6350, 3650)"]),
            recap([
                "Compensation: round, compute, repay — direction of the repay follows the trade.",
                "Make a ten: split one number to complete the other; nothing to repay.",
                "Count up: subtraction as a climb — the distance IS the difference.",
                "Read the numbers first; they tell you which tool is fastest.",
            ]),
            tip("Do every one of these in your head — no columns. If you catch yourself borrowing mentally, look again for the round-number trade."),
            tryitset("Mixed practice", "All three tools, your choice each time.", [
                tp("$399 + 555$ equals:",
                   ["$954$", "$944$", "$964$"],
                   "$400 + 555 = 955$, repay $1$: $954$.",
                   ["Eq(399 + 555, 954)"]),
                tp("$1\\,000 - 918$ equals:",
                   ["$82$", "$92$", "$182$"],
                   "Count up: $918 \\to 920$ ($2$), $\\to 1\\,000$ ($80$): $82$.",
                   ["Eq(2 + 80, 82)", "Eq(1000 - 918, 82)"]),
                tp("$75 + 49 + 25$ equals:",
                   ["$149$", "$139$", "$159$"],
                   "$75 + 25 = 100$, then $100 + 49 = 149$.",
                   ["Eq(75 + 25, 100)", "Eq(75 + 49 + 25, 149)"]),
                tp("$2\\,003 - 1\\,996$ equals:",
                   ["$7$", "$17$", "$13$"],
                   "Count up: $1\\,996 \\to 2\\,000$ ($4$), $\\to 2\\,003$ ($3$): $7$. No borrows needed at all.",
                   ["Eq(4 + 3, 7)", "Eq(2003 - 1996, 7)"]),
                tp("$4\\,998 + 2\\,997$ equals:",
                   ["$7\\,995$", "$7\\,985$", "$8\\,005$"],
                   "$5\\,000 + 3\\,000 = 8\\,000$, repay $2 + 3 = 5$: $7\\,995$.",
                   ["Eq(4998 + 2997, 7995)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Mental Addition & Subtraction\"",
                    "The written algorithm always works; the mental strategies win whenever the numbers are friendly — and prices, times and scores usually are. Next: the deep link between adding and subtracting, and the missing-number puzzles it unlocks.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Fact Families & Missing Numbers
# ==========================================================================

def lesson_families():
    return {
        "slug": "fact-families-and-missing-numbers",
        "title": "Fact Families & Missing Numbers",
        "concreteComparison": (
            "You saved some money, spent $456$ tögrög, and have $789$ "
            "left. How much did you start with? Nobody hands you the "
            "subtraction — you REBUILD it: what you have plus what you "
            "spent, $789 + 456 = 1\\,245$. Addition and subtraction are "
            "one relationship read in two directions, and once you see "
            "that, every missing-number puzzle solves itself."),
        "objective": (
            "Use the inverse relationship between addition and "
            "subtraction to write fact families, check computations, and "
            "solve missing-number equations."),
        "concept": [
            "**One family, four facts.** The triple $456, 789, 1\\,245$ "
            "makes four true statements: $456 + 789 = 1\\,245$, $789 + "
            "456 = 1\\,245$, $1\\,245 - 456 = 789$, $1\\,245 - 789 = "
            "456$. Same relationship, four readings.",
            "**The whole and its parts.** In every family there is one "
            "WHOLE ($1\\,245$) and two PARTS. Addition builds the whole "
            "from parts; subtraction finds a missing part. Ask first: is "
            "the unknown the whole, or a part?",
            "**Missing numbers:** $\\square - 456 = 789$ — the unknown "
            "is the whole (it was there before the spending), so ADD: "
            "$789 + 456 = 1\\,245$. But $350 + \\square = 1\\,000$ — the "
            "unknown is a part, so SUBTRACT: $1\\,000 - 350 = 650$.",
        ],
        "keyIdea": (
            "Addition and subtraction are one whole-and-parts "
            "relationship read in two directions: the unknown whole comes "
            "from adding the parts, an unknown part from subtracting the "
            "other part from the whole."),
        "facts": [
            {"title": "The fact family",
             "latex": "456 + 789 = 1\\,245 \\iff 1\\,245 - 789 = 456",
             "explanation": "Four facts, one relationship — two additions, two subtractions."},
            {"title": "Whole or part?",
             "latex": "\\square - b = c \\Rightarrow \\square = c + b \\qquad a + \\square = c \\Rightarrow \\square = c - a",
             "explanation": "Name what's missing first; the operation follows."},
        ],
        "workedExamples": [
            {"id": "g5as-l4-we1",
             "statement": "Check the subtraction $7\\,254 - 3\\,867 = 3\\,387$ using its fact family.",
             "note": "The family's addition rebuilds the whole.",
             "solution": ("If the claim is right, then part $+$ part $=$ whole: "
                          "$3\\,387 + 3\\,867 = 7\\,254$. It does — the subtraction "
                          "is correct."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7254 - 3867, 3387)", "Eq(3387 + 3867, 7254)"]},
            {"id": "g5as-l4-we2",
             "statement": "Solve: $\\square - 456 = 789$.",
             "note": "Is the unknown the whole or a part?",
             "solution": ("The box lost $456$ and still shows $789$ — the box is the "
                          "WHOLE. Rebuild it: $\\square = 789 + 456 = 1\\,245$. Check: "
                          "$1\\,245 - 456 = 789$. ✓"),
             "badges": [{"text": "core"}],
             "check": ["Eq(789 + 456, 1245)", "Eq(1245 - 456, 789)"]},
        ],
        "commonMistakes": [
            {"text": "Always subtracting when a problem shows a minus sign — solving □ − 456 = 789 as 789 − 456.",
             "correction": "Name the unknown first. In □ − 456 = 789 the box is the WHOLE, and wholes are rebuilt by ADDING: 789 + 456.",
             "authored": True},
            {"text": "Writing a fact family with the whole in a part's position, like 456 − 1,245 = 789.",
             "correction": "The whole (the biggest number) leads every subtraction and ends every addition. 1,245 leads: 1,245 − 456 = 789.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5as-l4-t1",
             "statement": "Write the four facts of the family $350, 650, 1\\,000$.",
             "solution": "$350 + 650 = 1\\,000$; $650 + 350 = 1\\,000$; $1\\,000 - 350 = 650$; $1\\,000 - 650 = 350$.",
             "check": ["Eq(350 + 650, 1000)", "Eq(1000 - 350, 650)", "Eq(1000 - 650, 350)"]},
            {"id": "g5as-l4-t2",
             "statement": "Solve: $2\\,340 + \\square = 5\\,000$.",
             "solution": "The unknown is a part: $\\square = 5\\,000 - 2\\,340 = 2\\,660$. Check: $2\\,340 + 2\\,660 = 5\\,000$. ✓",
             "check": ["Eq(5000 - 2340, 2660)", "Eq(2340 + 2660, 5000)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One relationship, four facts", [
                "Three numbers where two parts build a whole — $456$, $789$, $1\\,245$ — make a FACT FAMILY: two additions and two subtractions, all saying the same thing.",
                "$456 + 789 = 1\\,245$, $789 + 456 = 1\\,245$, $1\\,245 - 456 = 789$, $1\\,245 - 789 = 456$.",
                "This is why addition CHECKS subtraction (last lesson's receipt): they are the same relationship read in opposite directions.",
            ]), fig_groups((8, "part", C_ACCENT), (5, "part", C_WARM), (13, "whole", C_GREEN))),
            workedset("Families at work",
                      "The whole ends the additions and leads the subtractions.", [
                wex("Check $7\\,254 - 3\\,867 = 3\\,387$ via the family.",
                    ["Parts $3\\,387$ and $3\\,867$ must rebuild the whole $7\\,254$.",
                     "$3\\,387 + 3\\,867 = 7\\,254$ ✓ — the subtraction stands."],
                    "correct — the family closes",
                    ["Eq(3387 + 3867, 7254)"]),
                wex("Write the family of $350$, $650$, $1\\,000$.",
                    ["Additions: $350 + 650 = 1\\,000$ and $650 + 350 = 1\\,000$.",
                     "Subtractions: $1\\,000 - 350 = 650$ and $1\\,000 - 650 = 350$."],
                    "four facts, one family",
                    ["Eq(350 + 650, 1000)", "Eq(1000 - 650, 350)"]),
            ]),
            tryitset("Family membership", "The whole is the biggest — it anchors all four facts.", [
                tp("Which fact belongs to the family of $280$, $520$, $800$?",
                   ["$800 - 520 = 280$", "$520 - 280 = 800$", "$280 + 800 = 520$"],
                   "The whole $800$ leads subtractions and ends additions: $800 - 520 = 280$. ✓",
                   ["Eq(800 - 520, 280)", "Eq(280 + 520, 800)"]),
                tp("The subtraction $9\\,100 - 4\\,600 = 4\\,500$ is checked by:",
                   ["$4\\,500 + 4\\,600 = 9\\,100$", "$9\\,100 + 4\\,600 = 13\\,700$", "$4\\,600 - 4\\,500 = 100$"],
                   "Parts rebuild the whole: $4\\,500 + 4\\,600 = 9\\,100$. ✓",
                   ["Eq(9100 - 4600, 4500)", "Eq(4500 + 4600, 9100)"]),
                tp("Which triple is NOT a fact family?",
                   ["$120, 340, 480$", "$150, 350, 500$", "$220, 380, 600$"],
                   "$120 + 340 = 460 \\ne 480$ — the parts don't build that whole. (The other two close: $150 + 350 = 500$, $220 + 380 = 600$.)",
                   ["Eq(120 + 340, 460)", "Ne(460, 480)", "Eq(150 + 350, 500)",
                    "Eq(220 + 380, 600)"]),
            ]),
            tapq("Read it backwards", "$5\\,003 - 1\\,647 = 3\\,356$. Which fact is in the same family?",
                 ["$1\\,647 + 3\\,356 = 5\\,003$", "$5\\,003 + 1\\,647 = 6\\,650$",
                  "$3\\,356 - 1\\,647 = 1\\,709$", "$1\\,647 - 3\\,356 = 5\\,003$"],
                 "Parts $1\\,647$ and $3\\,356$ rebuild the whole: $1\\,647 + 3\\,356 = 5\\,003$ — the receipt from last lesson IS the fact family.",
                 ["Eq(1647 + 3356, 5003)"]),
            funfact("Algebra is impatient fact families",
                    "In a few grades you'll write x − 456 = 789 and \"add 456 to both sides\". That's exactly today's move — the unknown is the whole, rebuild it by adding — wearing algebra's clothes. You're doing algebra already; it just doesn't have letters yet."),
            withfig(teach("Concept B", "Whole or part? Then solve", [
                "Every missing-number equation asks ONE question: is the box the WHOLE or a PART?",
                "$\\square - 456 = 789$: the box had $456$ removed and $789$ remains — the box is the whole. Rebuild: $789 + 456 = 1\\,245$.",
                "$350 + \\square = 1\\,000$: the box is a part of $1\\,000$. Take the other part away: $1\\,000 - 350 = 650$. Name the unknown; the operation follows.",
            ]), fig_groups((12, "known part", C_ACCENT), (0, "unknown part", C_NEUTRAL), (20, "whole", C_GREEN))),
            workedset("Solve for the box",
                      "Name whole-or-part BEFORE choosing the operation.", [
                wex("Solve $\\square - 456 = 789$.",
                    ["The box is the whole (it lost a part and shows the rest).",
                     "$\\square = 789 + 456 = 1\\,245$; check $1\\,245 - 456 = 789$ ✓."],
                    "$1\\,245$",
                    ["Eq(789 + 456, 1245)", "Eq(1245 - 456, 789)"]),
                wex("Solve $2\\,340 + \\square = 5\\,000$.",
                    ["The box is a part of the whole $5\\,000$.",
                     "$\\square = 5\\,000 - 2\\,340 = 2\\,660$; check $2\\,340 + 2\\,660 = 5\\,000$ ✓."],
                    "$2\\,660$",
                    ["Eq(5000 - 2340, 2660)", "Eq(2340 + 2660, 5000)"]),
            ]),
            tryitset("Missing numbers", "Whole → add the parts. Part → subtract the other part.", [
                tp("$\\square - 275 = 640$. The box is:",
                   ["$915$", "$365$", "$815$"],
                   "The box is the whole: $640 + 275 = 915$. (Subtracting instead gives the trap answer $365$.)",
                   ["Eq(640 + 275, 915)", "Eq(915 - 275, 640)"]),
                tp("$730 + \\square = 1\\,205$. The box is:",
                   ["$475$", "$575$", "$1\\,935$"],
                   "The box is a part: $1\\,205 - 730 = 475$; check $730 + 475 = 1\\,205$ ✓.",
                   ["Eq(1205 - 730, 475)", "Eq(730 + 475, 1205)"]),
                tp("$4\\,000 - \\square = 1\\,725$. The box is:",
                   ["$2\\,275$", "$5\\,725$", "$2\\,375$"],
                   "The box is the part that was removed: $4\\,000 - 1\\,725 = 2\\,275$; check $4\\,000 - 2\\,275 = 1\\,725$ ✓.",
                   ["Eq(4000 - 1725, 2275)", "Eq(4000 - 2275, 1725)"]),
            ]),
            tapq("Name the unknown", "In $\\square - 830 = 1\\,450$, the box is the:",
                 ["whole — rebuild it by adding", "smaller part", "difference", "same as $1\\,450$"],
                 "Something lost $830$ and still shows $1\\,450$ — it must be the whole: $1\\,450 + 830 = 2\\,280$.",
                 ["Eq(1450 + 830, 2280)"]),
            recap([
                "Three whole-and-parts numbers make four facts — two additions, two subtractions.",
                "Addition checks subtraction because they are the same relationship, read backwards.",
                "Missing number? Name it first: whole → add the parts; part → subtract the other part.",
                "The whole is the biggest number — it ends additions and leads subtractions.",
            ]),
            tip("For every box below, say \"whole\" or \"part\" OUT LOUD before computing — the naming is the skill."),
            tryitset("Mixed practice", "Families, receipts, and boxes.", [
                tp("$\\square + 460 = 1\\,000$. The box is:",
                   ["$540$", "$640$", "$1\\,460$"],
                   "A part: $1\\,000 - 460 = 540$.",
                   ["Eq(1000 - 460, 540)"]),
                tp("$\\square - 1\\,240 = 3\\,760$. The box is:",
                   ["$5\\,000$", "$2\\,520$", "$4\\,900$"],
                   "The whole: $3\\,760 + 1\\,240 = 5\\,000$.",
                   ["Eq(3760 + 1240, 5000)"]),
                tp("$6\\,500 - \\square = 2\\,850$. The box is:",
                   ["$3\\,650$", "$3\\,750$", "$9\\,350$"],
                   "The removed part: $6\\,500 - 2\\,850 = 3\\,650$.",
                   ["Eq(6500 - 2850, 3650)", "Eq(6500 - 3650, 2850)"]),
                tp("Which addition checks $12\\,000 - 7\\,350 = 4\\,650$?",
                   ["$4\\,650 + 7\\,350 = 12\\,000$", "$12\\,000 + 7\\,350 = 19\\,350$", "$7\\,350 - 4\\,650 = 2\\,700$"],
                   "Parts rebuild the whole: $4\\,650 + 7\\,350 = 12\\,000$ ✓.",
                   ["Eq(4650 + 7350, 12000)"]),
                tp("A family of $x, 2\\,750, 8\\,000$ (with $8\\,000$ the whole) has $x$ equal to:",
                   ["$5\\,250$", "$10\\,750$", "$5\\,350$"],
                   "The missing part: $8\\,000 - 2\\,750 = 5\\,250$.",
                   ["Eq(8000 - 2750, 5250)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Fact Families & Missing Numbers\"",
                    "Whole-and-parts thinking is the skeleton under every equation you will ever solve. Last stop in this topic: word problems that need TWO or three of these moves in a row.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Multi-Step Word Problems
# ==========================================================================

def lesson_word_problems():
    return {
        "slug": "multi-step-word-problems",
        "title": "Multi-Step Word Problems",
        "concreteComparison": (
            "A shop opens with $12\\,450$ tögrög in the till, takes in "
            "$3\\,780$ in the morning and $4\\,265$ in the afternoon, "
            "then pays a $8\\,900$ delivery bill. Nobody solves that in "
            "one operation — you take it one EVENT at a time, writing "
            "the running total after each. Multi-step problems are just "
            "single-step problems standing in a queue."),
        "objective": (
            "Solve word problems needing two or more additions and "
            "subtractions: track a changing total, compare amounts, and "
            "check the result against an estimate."),
        "concept": [
            "**One event, one operation.** Read the story and list what "
            "happens in order: gained → add, lost → subtract. Compute a "
            "running total after each event; never try to hold two "
            "steps in one.",
            "**Grouping is allowed.** Losing $3\\,780$ then $4\\,265$ is "
            "the same as losing $(3\\,780 + 4\\,265)$ at once — combine "
            "the like events first if it's friendlier: $12\\,450 - "
            "8\\,045$.",
            "**Estimate as the guardrail.** Round the numbers, run the "
            "same steps, and the exact answer must land near the rough "
            "one — a Topic 1 habit that catches dropped steps and "
            "misread signs.",
        ],
        "keyIdea": (
            "Break the story into events, one operation each, running "
            "total after every step — and let a rounded version of the "
            "same plan check the answer."),
        "facts": [
            {"title": "Events in order",
             "latex": "12\\,450 - 3\\,780 - 4\\,265 = (12\\,450 - 8\\,045)",
             "explanation": "Losses can be taken one by one or bundled — same result."},
            {"title": "Comparison asks for a difference",
             "latex": "\\text{\"how many more\"} = \\text{larger} - \\text{smaller}",
             "explanation": "More/fewer/left-over questions are subtractions in disguise."},
        ],
        "workedExamples": [
            {"id": "g5as-l5-we1",
             "statement": ("A shop's till holds $12\\,450$ tögrög. The morning brings "
                           "in $3\\,780$ of takings and the afternoon $4\\,265$ more; "
                           "then the shop pays a supplier $8\\,900$ from the till. How "
                           "much is in the till at closing?"),
             "note": "List the events with their signs first.",
             "solution": ("Events: $+3\\,780$, $+4\\,265$, $-8\\,900$. Running total: "
                          "$12\\,450 + 3\\,780 = 16\\,230$; $16\\,230 + 4\\,265 = "
                          "20\\,495$; $20\\,495 - 8\\,900 = 11\\,595$. Estimate check: "
                          "$12\\,000 + 4\\,000 + 4\\,000 - 9\\,000 = 11\\,000$ — the "
                          "exact answer sits beside it. ✓"),
             "badges": [{"text": "core"}],
             "check": ["Eq(12450 + 3780, 16230)", "Eq(16230 + 4265, 20495)",
                       "Eq(20495 - 8900, 11595)",
                       "Eq(12000 + 4000 + 4000 - 9000, 11000)"]},
            {"id": "g5as-l5-we2",
             "statement": ("A library owns $8\\,540$ books. It receives a donation of "
                           "$1\\,260$ and lends out $2\\,375$. How many books are on "
                           "its shelves?"),
             "note": "Two events: a gain and a loss.",
             "solution": ("$8\\,540 + 1\\,260 = 9\\,800$ (after the donation); "
                          "$9\\,800 - 2\\,375 = 7\\,425$ on the shelves. Estimate: "
                          "$8\\,500 + 1\\,300 - 2\\,400 = 7\\,400$ — matches. ✓"),
             "badges": [{"text": "core"}],
             "check": ["Eq(8540 + 1260, 9800)", "Eq(9800 - 2375, 7425)",
                       "Eq(8500 + 1300 - 2400, 7400)"]},
        ],
        "commonMistakes": [
            {"text": "Adding every number in the story because they're there.",
             "correction": "Numbers don't tell you their sign — EVENTS do. \"Lends out 2,375\" is a loss. List the events with + or − before touching the arithmetic.",
             "authored": True},
            {"text": "Answering the wrong question — computing the afternoon takings when the problem asked for the till total.",
             "correction": "Re-read the question sentence LAST, after solving: does your number answer exactly what was asked?",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5as-l5-t1",
             "statement": ("A train leaves with $845$ passengers. At the first stop "
                           "$278$ get off and $164$ get on. How many ride on?"),
             "solution": "$845 - 278 = 567$, then $567 + 164 = 731$ passengers.",
             "check": ["Eq(845 - 278, 567)", "Eq(567 + 164, 731)"]},
            {"id": "g5as-l5-t2",
             "statement": ("Two schools collected paper: one gathered $4\\,320$ kg, "
                           "the other $3\\,485$ kg. How much more did the first "
                           "school collect?"),
             "solution": "\"How much more\" is a difference: $4\\,320 - 3\\,485 = 835$ kg.",
             "check": ["Eq(4320 - 3485, 835)", "Eq(835 + 3485, 4320)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One event, one operation", [
                "A multi-step story is single steps in a queue. Read it and LIST the events in order: gained → $+$, lost → $-$.",
                "Then compute a RUNNING TOTAL, one event at a time: till $12\\,450$, $+3\\,780 \\to 16\\,230$, $+4\\,265 \\to 20\\,495$, $-8\\,900 \\to 11\\,595$.",
                "Never juggle two steps at once — the queue exists so each move is easy.",
            ]), fig_numline([(0, "start"), (35, "+35"), (60, "-25")], lo=0, hi=80)),
            workedset("Running totals",
                      "Sign the events first; then it's just arithmetic.", [
                wex("Till $12\\,450$; takings $3\\,780$ and $4\\,265$; a bill of $8\\,900$ paid. Final till?",
                    ["Events: $+3\\,780$, $+4\\,265$, $-8\\,900$.",
                     "$12\\,450 \\to 16\\,230 \\to 20\\,495 \\to 11\\,595$.",
                     "Estimate: $12\\,000 + 4\\,000 + 4\\,000 - 9\\,000 = 11\\,000$ — close. ✓"],
                    "$11\\,595$ tögrög",
                    ["Eq(12450 + 3780 + 4265 - 8900, 11595)"]),
                wex("Library: $8\\,540$ books, $+1\\,260$ donated, $-2\\,375$ lent. On the shelves?",
                    ["$8\\,540 + 1\\,260 = 9\\,800$; $9\\,800 - 2\\,375 = 7\\,425$."],
                    "$7\\,425$ books",
                    ["Eq(8540 + 1260 - 2375, 7425)"]),
            ]),
            tryitset("Queue the events", "Sign each event, then run the total.", [
                tp("A train carries $845$; $278$ get off, $164$ get on. Riding on:",
                   ["$731$", "$567$", "$403$"],
                   "$845 - 278 = 567$, then $+164$: $731$. ($567$ answers only half the story.)",
                   ["Eq(845 - 278 + 164, 731)"]),
                tp("A herder has $1\\,240$ sheep, sells $385$, buys $150$. Now:",
                   ["$1\\,005$", "$855$", "$1\\,475$"],
                   "$1\\,240 - 385 = 855$, then $+150 = 1\\,005$.",
                   ["Eq(1240 - 385 + 150, 1005)"]),
                tp("A water tank holds $9\\,000$ L; $2\\,450$ L is used, then $1\\,780$ L more. Remaining:",
                   ["$4\\,770$ L", "$5\\,770$ L", "$4\\,670$ L"],
                   "Bundle the losses: $2\\,450 + 1\\,780 = 4\\,230$; then $9\\,000 - 4\\,230 = 4\\,770$.",
                   ["Eq(2450 + 1780, 4230)", "Eq(9000 - 4230, 4770)"]),
            ]),
            tapq("Same answer, two roads", "Losing $3\\,780$ then $4\\,265$ from $12\\,450$ equals:",
                 ["$12\\,450 - (3\\,780 + 4\\,265)$ — bundle the losses",
                  "$12\\,450 - 3\\,780 + 4\\,265$",
                  "$(12\\,450 - 3\\,780) + 4\\,265$",
                  "$3\\,780 + 4\\,265 - 12\\,450$"],
                 "Two losses in a row equal one combined loss: $12\\,450 - 8\\,045 = 4\\,405$ — same as subtracting them one at a time.",
                 ["Eq(3780 + 4265, 8045)", "Eq(12450 - 3780 - 4265, 4405)",
                  "Eq(12450 - 8045, 4405)"]),
            funfact("Accountants call it a ledger",
                    "A business's account book is exactly your running total: every gain and loss on its own line, the balance recomputed after each. Five-hundred-year-old Venetian bookkeeping and your word-problem method are the same technology."),
            withfig(teach("Concept B", "Comparisons, and the estimate guardrail", [
                "\"How many MORE\", \"how much LESS\", \"what's LEFT\" — comparison words always ask for a DIFFERENCE: larger minus smaller.",
                "Two schools collect $4\\,320$ and $3\\,485$ kg: \"how much more\" $= 4\\,320 - 3\\,485 = 835$ kg.",
                "Guardrail every answer with an estimate: run the SAME event queue on rounded numbers. Exact and rough must land together — if not, hunt the dropped step.",
            ]), fig_barchart([("estimate", 40, C_NEUTRAL), ("exact", 38, C_ACCENT)], step=10)),
            workedset("Compare and check",
                      "Differences for comparisons; estimates as guardrails.", [
                wex("Schools collect $4\\,320$ kg and $3\\,485$ kg. How much more did the first gather?",
                    ["Comparison → difference: $4\\,320 - 3\\,485 = 835$ kg.",
                     "Receipt: $835 + 3\\,485 = 4\\,320$ ✓."],
                    "$835$ kg",
                    ["Eq(4320 - 3485, 835)", "Eq(835 + 3485, 4320)"]),
                wex("Estimate-check: till problem, rounded.",
                    ["Rounded queue: $12\\,000 + 4\\,000 + 4\\,000 - 9\\,000 = 11\\,000$.",
                     "Exact was $11\\,595$ — beside the estimate, so the plan held. ✓"],
                    "estimate $11\\,000$, exact $11\\,595$",
                    ["Eq(12000 + 4000 + 4000 - 9000, 11000)",
                     "Eq(12450 + 3780 + 4265 - 8900, 11595)"]),
            ]),
            tryitset("Comparisons", "Larger minus smaller — then receipt it.", [
                tp("A mountain is $3\\,905$ m, another $2\\,760$ m. The first is taller by:",
                   ["$1\\,145$ m", "$1\\,245$ m", "$1\\,155$ m"],
                   "$3\\,905 - 2\\,760 = 1\\,145$; receipt $1\\,145 + 2\\,760 = 3\\,905$ ✓.",
                   ["Eq(3905 - 2760, 1145)", "Eq(1145 + 2760, 3905)"]),
                tp("Saturday's fair drew $6\\,214$ visitors, Sunday's $5\\,975$. Sunday drew fewer by:",
                   ["$239$", "$339$", "$249$"],
                   "$6\\,214 - 5\\,975 = 239$ — count up: $5\\,975 \\to 6\\,000$ ($25$) $\\to 6\\,214$ ($214$).",
                   ["Eq(25 + 214, 239)", "Eq(6214 - 5975, 239)"]),
                tp("An answer of $20\\,495$ for the till problem (estimate $11\\,000$) means:",
                   ["a step was missed — the $8\\,900$ bill was never subtracted",
                    "the estimate is wrong",
                    "nothing — estimates vary"],
                   "$20\\,495$ sits far from the $11\\,000$ guardrail — and indeed $12\\,450 + 3\\,780 + 4\\,265 = 20\\,495$ is exactly the total BEFORE the bill. Subtracting the $8\\,900$ gives the true $11\\,595$.",
                   ["Eq(12450 + 3780 + 4265, 20495)", "Eq(20495 - 8900, 11595)",
                    "Ne(20495, 11595)"]),
            ]),
            tapq("Which question was asked?",
                 "\"A farmer had $2\\,400$ bales, sold $850$, then baled $600$ more. How many NOW?\" The answer is:",
                 ["$2\\,150$", "$950$", "$3\\,850$", "$1\\,550$"],
                 "$2\\,400 - 850 = 1\\,550$, then $+600 = 2\\,150$. ($1\\,550$ answers the story only halfway through.)",
                 ["Eq(2400 - 850 + 600, 2150)"]),
            recap([
                "List the story's events with signs; run the total one event at a time.",
                "Like events can bundle: two losses = one combined loss.",
                "Comparison words (more, fewer, left) ask for larger minus smaller.",
                "Guardrail with an estimate run on the same plan — big gaps mean dropped steps.",
            ]),
            tip("Write the event list for each problem before computing — the list is where these are won and lost."),
            tryitset("Mixed practice", "Full stories, start to finish.", [
                tp("A bakery makes $1\\,850$ buns, sells $1\\,320$, bakes $475$ more. Buns now:",
                   ["$1\\,005$", "$530$", "$905$"],
                   "$1\\,850 - 1\\,320 = 530$, then $+475 = 1\\,005$.",
                   ["Eq(1850 - 1320 + 475, 1005)"]),
                tp("Two towns are $12\\,308$ and $9\\,540$ people. The larger exceeds the smaller by:",
                   ["$2\\,768$", "$2\\,868$", "$3\\,768$"],
                   "$12\\,308 - 9\\,540 = 2\\,768$; receipt $2\\,768 + 9\\,540 = 12\\,308$ ✓.",
                   ["Eq(12308 - 9540, 2768)", "Eq(2768 + 9540, 12308)"]),
                tp("A wallet holds $20\\,000$; spends of $7\\,450$ and $6\\,180$; a refund of $1\\,500$. Left:",
                   ["$7\\,870$", "$6\\,370$", "$8\\,870$"],
                   "$20\\,000 - 7\\,450 - 6\\,180 + 1\\,500 = 7\\,870$.",
                   ["Eq(20000 - 7450 - 6180 + 1500, 7870)"]),
                tp("A stadium seats $15\\,000$; sections of $4\\,850$ and $5\\,675$ are full. Empty seats:",
                   ["$4\\,475$", "$4\\,575$", "$5\\,475$"],
                   "Bundle: $4\\,850 + 5\\,675 = 10\\,525$; then $15\\,000 - 10\\,525 = 4\\,475$.",
                   ["Eq(4850 + 5675, 10525)", "Eq(15000 - 10525, 4475)"]),
                tp("Which estimate guards the wallet problem above?",
                   ["$20\\,000 - 7\\,000 - 6\\,000 + 2\\,000 = 9\\,000$",
                    "$20\\,000 + 7\\,000 + 6\\,000 = 33\\,000$",
                    "$7\\,000 - 6\\,000 = 1\\,000$"],
                   "Same plan, rounded numbers: about $9\\,000$ — the exact $7\\,870$ lands near it. The other options run a different plan entirely.",
                   ["Eq(20000 - 7000 - 6000 + 2000, 9000)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Multi-Step Word Problems\" — and the topic",
                    "Carries, borrows, mental trades, fact families, and event queues: the complete addition-and-subtraction toolkit. Next topic on the Grade 5 road: multiplication and division, where repeated adding gets an upgrade.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5as-pr1", "Add $6\\,847 + 5\\,398$.",
             "Carries in every column: $6\\,847 + 5\\,398 = 12\\,245$.",
             ["Eq(6847 + 5398, 12245)"]),
        prob("g5as-pr2", "Compute $353 + 619 + 647$ the clever way.",
             "Friendly pair: $353 + 647 = 1\\,000$; then $1\\,000 + 619 = 1\\,619$.",
             ["Eq(353 + 647, 1000)", "Eq(353 + 619 + 647, 1619)"]),
        prob("g5as-pr3", "Subtract $9\\,213 - 5\\,847$, then check by adding back.",
             "$9\\,213 - 5\\,847 = 3\\,366$; receipt $3\\,366 + 5\\,847 = 9\\,213$ ✓.",
             ["Eq(9213 - 5847, 3366)", "Eq(3366 + 5847, 9213)"]),
        prob("g5as-pr4", "Subtract $7\\,000 - 3\\,254$.",
             "The break travels across the zeros: $7\\,000 - 3\\,254 = 3\\,746$; receipt $3\\,746 + 3\\,254 = 7\\,000$ ✓.",
             ["Eq(7000 - 3254, 3746)", "Eq(3746 + 3254, 7000)"]),
        prob("g5as-pr5", "Compute $2\\,997 + 4\\,586$ mentally, naming your strategy.",
             "Compensation: $3\\,000 + 4\\,586 = 7\\,586$, repay $3$: $7\\,583$.",
             ["Eq(3000 + 4586, 7586)", "Eq(2997 + 4586, 7583)"]),
        prob("g5as-pr6", "Solve $\\square - 1\\,368 = 2\\,945$.",
             "The box is the whole: $2\\,945 + 1\\,368 = 4\\,313$; check $4\\,313 - 1\\,368 = 2\\,945$ ✓.",
             ["Eq(2945 + 1368, 4313)", "Eq(4313 - 1368, 2945)"]),
        prob("g5as-pr7", "Solve $5\\,420 + \\square = 9\\,000$.",
             "The box is a part: $9\\,000 - 5\\,420 = 3\\,580$; check $5\\,420 + 3\\,580 = 9\\,000$ ✓.",
             ["Eq(9000 - 5420, 3580)", "Eq(5420 + 3580, 9000)"]),
        prob("g5as-pr8", ("A cinema sold $2\\,485$ tickets on Friday, $3\\,178$ on Saturday, "
                          "and $1\\,940$ on Sunday. How many more tickets did the weekend "
                          "days (Saturday + Sunday) sell than Friday?"),
             "Weekend: $3\\,178 + 1\\,940 = 5\\,118$. Comparison: $5\\,118 - 2\\,485 = 2\\,633$ more.",
             ["Eq(3178 + 1940, 5118)", "Eq(5118 - 2485, 2633)"]),
    ]


def test_bank():
    return [
        prob("g5as-x1", "Add $8\\,676 + 4\\,879$.",
             "$8\\,676 + 4\\,879 = 13\\,555$ — four carries.",
             ["Eq(8676 + 4879, 13555)"]),
        prob("g5as-x2", "Subtract $10\\,000 - 6\\,437$.",
             "The break travels through the zeros: $3\\,563$; receipt $3\\,563 + 6\\,437 = 10\\,000$ ✓.",
             ["Eq(10000 - 6437, 3563)", "Eq(3563 + 6437, 10000)"]),
        prob("g5as-x3", "Compute $4\\,999 + 4\\,999$ mentally.",
             "$5\\,000 + 5\\,000 = 10\\,000$, repay $1 + 1 = 2$: $9\\,998$.",
             ["Eq(4999 + 4999, 9998)"]),
        prob("g5as-x4", "Solve $\\square - 2\\,584 = 6\\,416$.",
             "The box is the whole: $6\\,416 + 2\\,584 = 9\\,000$; check $9\\,000 - 2\\,584 = 6\\,416$ ✓.",
             ["Eq(6416 + 2584, 9000)", "Eq(9000 - 2584, 6416)"]),
        prob("g5as-x5", ("A claimed result says $8\\,205 - 3\\,647 = 4\\,658$. Run the "
                         "add-back check and give a verdict."),
             "Receipt: $4\\,658 + 3\\,647 = 8\\,305 \\ne 8\\,205$ — wrong. The true difference is $4\\,558$.",
             ["Eq(4658 + 3647, 8305)", "Ne(8305, 8205)", "Eq(8205 - 3647, 4558)"]),
        prob("g5as-x6", ("A warehouse stores $18\\,500$ boxes. It ships $6\\,720$ and "
                         "$4\\,915$, then receives $2\\,300$. How many boxes does it "
                         "hold, and what rounded estimate guards the answer?"),
             "Bundle the shipments: $6\\,720 + 4\\,915 = 11\\,635$. Then $18\\,500 - 11\\,635 + 2\\,300 = 9\\,165$. Guardrail: $18\\,500 - 7\\,000 - 5\\,000 + 2\\,300 \\approx 8\\,800$ — beside the exact answer. ✓",
             ["Eq(6720 + 4915, 11635)", "Eq(18500 - 11635 + 2300, 9165)",
              "Eq(18500 - 7000 - 5000 + 2300, 8800)"]),
    ]


def main():
    topic = {
        "slug": "addition-and-subtraction",
        "title": "Addition & Subtraction",
        "grade": 5,
        "status": "published",
        "blurb": ("Multi-digit addition and subtraction with regrouping, mental "
                  "strategies, fact families with missing numbers, and multi-step "
                  "word problems."),
        "lessons": [
            lesson_adding(),
            lesson_subtracting(),
            lesson_mental(),
            lesson_families(),
            lesson_word_problems(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "addition-and-subtraction.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
