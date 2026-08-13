#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 3: Multiplication & Division.

One-digit and two-digit multiplication built on the distributive idea
(break a number into places, multiply each, add), division with
remainders and the receipt q × d + r = n, long division as the
divide-multiply-subtract-bring-down cycle, and word problems where the
skill is CHOOSING the operation — including what a remainder means.

Through-line: MULTIPLICATION DISTRIBUTES OVER PLACES. Every algorithm
in this topic — column multiplication, partial products, long division
— is the place-value ladder from Topic 1 doing repeated work.

Same construction as the other Grade 5 builders: every check anywhere
in the structure is sympy-asserted BEFORE the JSON is written. Every
division carries its multiplication receipt (quotient × divisor +
remainder == dividend, remainder < divisor) as checks, so a wrong
quotient or an oversized remainder cannot ship.

Run: python3 scripts/grade4/build_multiplication_division.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic)


def dchecks(n, d, q, r=0):
    """The division receipt as check strings: q*d + r == n and r < d."""
    out = ["Eq(%d*%d + %d, %d)" % (q, d, r, n)]
    out.append("%d < %d" % (r, d))
    return out


# ==========================================================================
# Lesson 1 — Multiplying by One Digit
# ==========================================================================

def lesson_one_digit():
    return {
        "slug": "multiplying-by-one-digit",
        "title": "Multiplying by One Digit",
        "concreteComparison": (
            "A truck carries $2\\,357$ bricks per trip and makes $4$ "
            "trips. You could add $2\\,357$ four times — or notice that "
            "four of EACH PART is enough: four $2\\,000$s, four $300$s, "
            "four $50$s, four $7$s, added up. Multiplication doesn't "
            "fight the whole number at once; it takes the places one at "
            "a time."),
        "objective": (
            "Multiply multi-digit numbers by a one-digit number using "
            "expanded form and the column method, and multiply by tens, "
            "hundreds and thousands using the trailing-zeros shortcut."),
        "concept": [
            "**Multiply the parts.** $4 \\times 2\\,357$ splits into $4 "
            "\\times 2\\,000 + 4 \\times 300 + 4 \\times 50 + 4 \\times "
            "7 = 8\\,000 + 1\\,200 + 200 + 28 = 9\\,428$. This is the "
            "DISTRIBUTIVE idea: the factor visits every place.",
            "**The column method** is the same visits written compactly, "
            "ones first, carrying as in addition: $6 \\times 5 = 30$ — "
            "write $0$, carry $3$ into the tens' product.",
            "**Trailing zeros ride along.** $4 \\times 700$: do $4 "
            "\\times 7 = 28$, then re-attach the two zeros: $2\\,800$. "
            "Multiplying by tens, hundreds, thousands is a small "
            "multiplication plus a place shift.",
        ],
        "keyIdea": (
            "One factor visits every place of the other: multiply each "
            "part, add the results. The column method is this idea "
            "written tightly, and trailing zeros just shift places."),
        "facts": [
            {"title": "The distributive idea",
             "latex": "4 \\times 2\\,357 = 4 \\times 2\\,000 + 4 \\times 300 + 4 \\times 50 + 4 \\times 7",
             "explanation": "The factor multiplies every place separately; the pieces add."},
            {"title": "Trailing zeros",
             "latex": "4 \\times 700 = (4 \\times 7) \\times 100 = 2\\,800",
             "explanation": "Multiply the leading digits, then re-attach the zeros — a place shift."},
        ],
        "workedExamples": [
            {"id": "g5md-l1-we1",
             "statement": "Compute $4 \\times 2\\,357$ by multiplying the parts.",
             "note": "Four of each place, then add.",
             "solution": ("$4 \\times 2\\,000 = 8\\,000$; $4 \\times 300 = 1\\,200$; "
                          "$4 \\times 50 = 200$; $4 \\times 7 = 28$. Sum: $8\\,000 + "
                          "1\\,200 + 200 + 28 = 9\\,428$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*2000, 8000)", "Eq(4*300, 1200)", "Eq(4*50, 200)",
                       "Eq(4*7, 28)", "Eq(8000 + 1200 + 200 + 28, 9428)",
                       "Eq(4*2357, 9428)"]},
            {"id": "g5md-l1-we2",
             "statement": "Compute $6 \\times 1\\,845$ with the column method.",
             "note": "Ones first; carries add into the next product.",
             "solution": ("Ones: $6 \\times 5 = 30$ — write $0$, carry $3$. Tens: $6 "
                          "\\times 4 = 24$, plus $3$ is $27$ — write $7$, carry $2$. "
                          "Hundreds: $6 \\times 8 = 48$, plus $2$ is $50$ — write "
                          "$0$, carry $5$. Thousands: $6 \\times 1 = 6$, plus $5$ is "
                          "$11$. Product: $11\\,070$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6*5, 30)", "Eq(24 + 3, 27)", "Eq(48 + 2, 50)",
                       "Eq(6 + 5, 11)", "Eq(6*1845, 11070)"]},
        ],
        "commonMistakes": [
            {"text": "Forgetting to ADD the carry into the next column's product.",
             "correction": "The carry from 6 × 5 = 30 joins the NEXT product: 6 × 4 = 24, plus the carried 3, is 27. Multiply first, then add the carry.",
             "authored": True},
            {"text": "Dropping trailing zeros — 4 × 700 = 28.",
             "correction": "The two zeros of 700 are places, and places survive multiplication: 4 × 700 = 2,800. Multiply the digits, then re-attach every zero.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5md-l1-t1",
             "statement": "Compute $7 \\times 463$.",
             "solution": "$7 \\times 400 = 2\\,800$; $7 \\times 60 = 420$; $7 \\times 3 = 21$. Sum: $3\\,241$.",
             "check": ["Eq(7*400, 2800)", "Eq(7*60, 420)", "Eq(7*3, 21)",
                       "Eq(7*463, 3241)"]},
            {"id": "g5md-l1-t2",
             "statement": "Compute $3 \\times 6\\,000$ and $5 \\times 800$.",
             "solution": "$3 \\times 6 = 18$ with three zeros: $18\\,000$. $5 \\times 8 = 40$ with two zeros: $4\\,000$.",
             "check": ["Eq(3*6000, 18000)", "Eq(5*800, 4000)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "The factor visits every place", [
                "$4 \\times 2\\,357$ is four $2\\,000$s, four $300$s, four $50$s and four $7$s — the factor VISITS each place, and the pieces add: $8\\,000 + 1\\,200 + 200 + 28 = 9\\,428$.",
                "This is the distributive idea, and it is the engine under every multiplication algorithm you will ever meet.",
                "The column method writes the same visits compactly, ones first, carrying like addition: multiply, then ADD the carry.",
            ]),
            workedset("Parts, then columns",
                      "Same multiplication, two notations.", [
                wex("Compute $4 \\times 2\\,357$ by parts.",
                    ["$4 \\times 2\\,000 = 8\\,000$, $4 \\times 300 = 1\\,200$, $4 \\times 50 = 200$, $4 \\times 7 = 28$.",
                     "Add: $9\\,428$."],
                    "$9\\,428$",
                    ["Eq(4*2357, 9428)"]),
                wex("Compute $6 \\times 1\\,845$ by columns.",
                    ["Ones: $30$ — write $0$ carry $3$. Tens: $24 + 3 = 27$. Hundreds: $48 + 2 = 50$. Thousands: $6 + 5 = 11$.",
                     "Product: $11\\,070$."],
                    "$11\\,070$",
                    ["Eq(6*1845, 11070)"]),
            ]),
            tryitset("One-digit products", "Parts or columns — your choice; the answer must agree.", [
                tp("$7 \\times 463$ equals:",
                   ["$3\\,241$", "$3\\,231$", "$2\\,841$"],
                   "$2\\,800 + 420 + 21 = 3\\,241$. (Forgetting the tens carry gives $3\\,231$.)",
                   ["Eq(7*463, 3241)"]),
                tp("$8 \\times 1\\,209$ equals:",
                   ["$9\\,672$", "$9\\,612$", "$8\\,672$"],
                   "$8\\,000 + 1\\,600 + 0 + 72 = 9\\,672$ — the zero tens contribute nothing, but hold their place.",
                   ["Eq(8*1209, 9672)"]),
                tp("$9 \\times 705$ equals:",
                   ["$6\\,345$", "$6\\,335$", "$6\\,435$"],
                   "$9 \\times 700 = 6\\,300$ and $9 \\times 5 = 45$: $6\\,345$.",
                   ["Eq(9*705, 6345)"]),
            ]),
            tapq("Multiply, then carry", "In $6 \\times 1\\,845$, the tens step is $6 \\times 4 = 24$ plus the carried $3$. You write:",
                 ["$7$, and carry $2$", "$27$ in the tens place", "$4$, and carry $2$", "$7$, and carry $3$"],
                 "$24 + 3 = 27$: one digit per place — the $7$ stays, the $2$ carries into the hundreds step.",
                 ["Eq(24 + 3, 27)"]),
            funfact("Times tables end at 9 on purpose",
                    "Every multiplication you will ever do — however enormous — reduces to one-digit products plus place shifts plus addition. The 81 facts of the times table are the complete alphabet; algorithms just spell with them."),
            teach("Concept B", "Zeros ride along", [
                "$4 \\times 700$: the $700$ is $7$ hundreds, so the product is $28$ hundreds — $2\\,800$. Multiply the digits, RE-ATTACH the zeros.",
                "$3 \\times 6\\,000 = 18\\,000$: three zeros in, three zeros out (the $18$ supplies its own extra digit).",
                "This is Topic 1's ten-times ladder at work: each zero is a place shift, and multiplication respects places.",
            ]),
            workedset("Round-number products",
                      "Digits times digits, zeros re-attached.", [
                wex("Compute $4 \\times 700$ and $5 \\times 800$.",
                    ["$4 \\times 7 = 28$, two zeros back: $2\\,800$.",
                     "$5 \\times 8 = 40$, two zeros back: $4\\,000$."],
                    "$2\\,800$ and $4\\,000$",
                    ["Eq(4*700, 2800)", "Eq(5*800, 4000)"]),
                wex("Compute $3 \\times 6\\,000$.",
                    ["$3 \\times 6 = 18$, three zeros back: $18\\,000$."],
                    "$18\\,000$",
                    ["Eq(3*6000, 18000)"]),
            ]),
            tryitset("Zeros in, zeros out", "Count the zeros before and after.", [
                tp("$6 \\times 900$ equals:",
                   ["$5\\,400$", "$540$", "$5\\,600$"],
                   "$6 \\times 9 = 54$, two zeros back: $5\\,400$.",
                   ["Eq(6*900, 5400)"]),
                tp("$7 \\times 5\\,000$ equals:",
                   ["$35\\,000$", "$3\\,500$", "$35\\,500$"],
                   "$7 \\times 5 = 35$, three zeros: $35\\,000$.",
                   ["Eq(7*5000, 35000)"]),
                tp("$8 \\times 4\\,000$ equals:",
                   ["$32\\,000$", "$3\\,200$", "$320\\,000$"],
                   "$8 \\times 4 = 32$ with three zeros: $32\\,000$.",
                   ["Eq(8*4000, 32000)"]),
            ]),
            tapq("Count the zeros", "$5 \\times 600$ ends in how many zeros?",
                 ["three — $3\\,000$", "two — $300$", "one — $30$", "none"],
                 "$5 \\times 6 = 30$ brings a zero of its own, and $600$ adds two more: $3\\,000$.",
                 ["Eq(5*600, 3000)"]),
            recap([
                "The factor visits every place; the pieces add — the distributive idea.",
                "Column method: multiply, THEN add the carry; one digit per place.",
                "Trailing zeros are places — multiply the digits, re-attach every zero.",
                "All of it reduces to times-table facts plus place shifts.",
            ]),
            tip("Mixed one-digit products — estimate each first (round the big factor) so a dropped carry has nowhere to hide."),
            tryitset("Mixed practice", "Parts, columns and zeros together.", [
                tp("$3 \\times 2\\,468$ equals:",
                   ["$7\\,404$", "$7\\,304$", "$6\\,404$"],
                   "$6\\,000 + 1\\,200 + 180 + 24 = 7\\,404$.",
                   ["Eq(3*2468, 7404)"]),
                tp("$5 \\times 1\\,286$ equals:",
                   ["$6\\,430$", "$6\\,420$", "$5\\,430$"],
                   "$5\\,000 + 1\\,000 + 400 + 30 = 6\\,430$.",
                   ["Eq(5*1286, 6430)"]),
                tp("$4 \\times 975$ equals:",
                   ["$3\\,900$", "$3\\,800$", "$3\\,600$"],
                   "Mental shortcut: $4 \\times 1\\,000 = 4\\,000$, repay $4 \\times 25 = 100$: $3\\,900$.",
                   ["Eq(4*975, 3900)", "Eq(4000 - 100, 3900)"]),
                tp("$6 \\times 808$ equals:",
                   ["$4\\,848$", "$4\\,808$", "$4\\,948$"],
                   "$4\\,800 + 48 = 4\\,848$ — the zero tens hold their place.",
                   ["Eq(6*808, 4848)"]),
                tp("A stable feeds $7$ horses $1\\,250$ g of oats each. Total grams:",
                   ["$8\\,750$", "$8\\,650$", "$7\\,750$"],
                   "$7 \\times 1\\,250 = 8\\,750$ — $7\\,000 + 1\\,400 + 350$.",
                   ["Eq(7*1250, 8750)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Multiplying by One Digit\"",
                    "Places visited one at a time, carries riding the ladder — next lesson the second factor grows to two digits, and the trick is that nothing new happens: just two rounds of today's method, shifted.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Multiplying by Two Digits
# ==========================================================================

def lesson_two_digit():
    return {
        "slug": "multiplying-by-two-digits",
        "title": "Multiplying by Two Digits",
        "concreteComparison": (
            "A concert hall has $24$ rows of $36$ seats. Split the $36$: "
            "$24$ rows of $30$ seats plus $24$ rows of $6$ — $720 + 144 "
            "= 864$ seats. Two-digit multiplication is two one-digit "
            "multiplications wearing one coat: one for the tens, one for "
            "the ones, added."),
        "objective": (
            "Multiply two multi-digit numbers using partial products and "
            "the column layout, multiplying by the tens digit with its "
            "place shift."),
        "concept": [
            "**Split the second factor.** $24 \\times 36 = 24 \\times 30 "
            "+ 24 \\times 6$: the tens part and the ones part, each a "
            "one-digit-style multiplication, added at the end. These "
            "pieces are the PARTIAL PRODUCTS.",
            "**Times ten shifts.** $24 \\times 30$ is $24 \\times 3$ "
            "with a zero attached: $720$. Multiplying by a tens digit "
            "is last lesson's skill plus one place shift.",
            "**The column layout** stacks the two partial products: the "
            "ones row first, then the tens row starting one place left "
            "(that shift IS the attached zero), then add.",
        ],
        "keyIdea": (
            "Split the second factor into tens and ones, multiply by "
            "each (the tens product shifted one place), and add the two "
            "partial products."),
        "facts": [
            {"title": "Partial products",
             "latex": "24 \\times 36 = 24 \\times 30 + 24 \\times 6 = 720 + 144",
             "explanation": "Tens part plus ones part — two easy products, one sum."},
            {"title": "The shift",
             "latex": "24 \\times 30 = (24 \\times 3) \\times 10 = 720",
             "explanation": "Multiplying by tens is a one-digit product with a place shift."},
        ],
        "workedExamples": [
            {"id": "g5md-l2-we1",
             "statement": "Compute $24 \\times 36$ with partial products.",
             "note": "Tens part, ones part, add.",
             "solution": ("Tens: $24 \\times 30 = 720$. Ones: $24 \\times 6 = 144$. "
                          "Add: $720 + 144 = 864$ — the hall seats $864$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(24*30, 720)", "Eq(24*6, 144)", "Eq(720 + 144, 864)",
                       "Eq(24*36, 864)"]},
            {"id": "g5md-l2-we2",
             "statement": "Compute $138 \\times 26$.",
             "note": "The first factor can be any size — the split happens to the second.",
             "solution": ("Tens: $138 \\times 20 = 2\\,760$. Ones: $138 \\times 6 = "
                          "828$. Add: $2\\,760 + 828 = 3\\,588$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(138*20, 2760)", "Eq(138*6, 828)", "Eq(2760 + 828, 3588)",
                       "Eq(138*26, 3588)"]},
        ],
        "commonMistakes": [
            {"text": "Forgetting the shift on the tens row — writing 24 × 3 instead of 24 × 30.",
             "correction": "The 3 of 36 is THIRTY. In the column layout the tens row starts one place left; in partial products it wears its zero: 720, not 72.",
             "authored": True},
            {"text": "Multiplying tens by tens and ones by ones only — 24 × 36 as 20×30 + 4×6.",
             "correction": "EVERY part of one factor meets EVERY part of the other: 20×30 + 20×6 + 4×30 + 4×6. The two-row method organises exactly that.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5md-l2-t1",
             "statement": "Compute $47 \\times 52$.",
             "solution": "$47 \\times 50 = 2\\,350$; $47 \\times 2 = 94$. Sum: $2\\,444$.",
             "check": ["Eq(47*50, 2350)", "Eq(47*2, 94)", "Eq(47*52, 2444)"]},
            {"id": "g5md-l2-t2",
             "statement": "Compute $60 \\times 40$.",
             "solution": "$6 \\times 4 = 24$, two zeros back: $2\\,400$.",
             "check": ["Eq(60*40, 2400)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Two products in a coat", [
                "$24 \\times 36$: split the $36$ into $30 + 6$. Then $24 \\times 30 = 720$ and $24 \\times 6 = 144$ — add: $864$.",
                "The pieces are called PARTIAL PRODUCTS: the tens part and the ones part, each a one-digit multiplication you already own.",
                "$24 \\times 30$ itself is $24 \\times 3$ shifted: $72 \\to 720$. Nothing here is new — it is last lesson twice, plus an addition.",
            ]),
            workedset("Partial products",
                      "Tens row, ones row, add.", [
                wex("Compute $24 \\times 36$.",
                    ["$24 \\times 30 = 720$; $24 \\times 6 = 144$.",
                     "$720 + 144 = 864$."],
                    "$864$",
                    ["Eq(24*36, 864)"]),
                wex("Compute $47 \\times 52$.",
                    ["$47 \\times 50 = 2\\,350$; $47 \\times 2 = 94$.",
                     "$2\\,350 + 94 = 2\\,444$."],
                    "$2\\,444$",
                    ["Eq(47*52, 2444)"]),
            ]),
            tryitset("Split and add", "Second factor into tens + ones; two products; one sum.", [
                tp("$32 \\times 41$ equals:",
                   ["$1\\,312$", "$1\\,282$", "$1\\,412$"],
                   "$32 \\times 40 = 1\\,280$ plus $32 \\times 1 = 32$: $1\\,312$.",
                   ["Eq(32*41, 1312)"]),
                tp("$25 \\times 48$ equals:",
                   ["$1\\,200$", "$1\\,100$", "$1\\,240$"],
                   "$25 \\times 48 = 25 \\times 40 + 25 \\times 8 = 1\\,000 + 200 = 1\\,200$. (Or: $25 \\times 4 = 100$, so $25 \\times 48 = 100 \\times 12$.)",
                   ["Eq(25*48, 1200)"]),
                tp("$53 \\times 67$ equals:",
                   ["$3\\,551$", "$3\\,451$", "$3\\,561$"],
                   "$53 \\times 60 = 3\\,180$ plus $53 \\times 7 = 371$: $3\\,551$.",
                   ["Eq(53*60, 3180)", "Eq(53*7, 371)", "Eq(53*67, 3551)"]),
            ]),
            tapq("The missing zero", "A student computes $24 \\times 36$ as $144 + 72 = 216$. The slip is:",
                 ["the tens row lost its shift — $24 \\times 30$ is $720$, not $72$",
                  "the ones row is wrong",
                  "the addition is wrong",
                  "nothing — $216$ is correct"],
                 "The $3$ of $36$ means THIRTY: $24 \\times 30 = 720$. With the shift restored, $720 + 144 = 864$.",
                 ["Eq(24*30, 720)", "Eq(720 + 144, 864)", "Ne(216, 864)"]),
            funfact("The lattice method",
                    "Medieval merchants multiplied on a drawn lattice — a grid where every digit-pair got its own cell and the diagonals did the carrying. Same partial products, different furniture. Our two-row layout won because it fits on a till receipt."),
            teach("Concept B", "The column layout", [
                "Stack the work: multiply by the ONES digit first (one full row), then by the TENS digit starting one place left — that shift is the attached zero.",
                "$138 \\times 26$: ones row $138 \\times 6 = 828$; tens row $138 \\times 2 = 276$, written from the tens place ($2\\,760$). Add: $3\\,588$.",
                "Two rows, two partial products, one sum — the coat that keeps every digit-pair meeting exactly once.",
            ]),
            workedset("Rows and shifts",
                      "Ones row, shifted tens row, add.", [
                wex("Compute $138 \\times 26$ in the column layout.",
                    ["Ones row: $138 \\times 6 = 828$.",
                     "Tens row: $138 \\times 20 = 2\\,760$ — one place left.",
                     "Add: $828 + 2\\,760 = 3\\,588$."],
                    "$3\\,588$",
                    ["Eq(138*26, 3588)"]),
                wex("Compute $214 \\times 23$.",
                    ["Ones: $214 \\times 3 = 642$. Tens: $214 \\times 20 = 4\\,280$.",
                     "Add: $642 + 4\\,280 = 4\\,922$."],
                    "$4\\,922$",
                    ["Eq(214*3, 642)", "Eq(214*20, 4280)", "Eq(214*23, 4922)"]),
            ]),
            tryitset("Column products", "Keep the tens row one place left.", [
                tp("$76 \\times 15$ equals:",
                   ["$1\\,140$", "$1\\,040$", "$1\\,240$"],
                   "$76 \\times 10 = 760$ plus $76 \\times 5 = 380$: $1\\,140$.",
                   ["Eq(76*15, 1140)"]),
                tp("$45 \\times 22$ equals:",
                   ["$990$", "$900$", "$980$"],
                   "$45 \\times 20 = 900$ plus $45 \\times 2 = 90$: $990$.",
                   ["Eq(45*22, 990)"]),
                tp("$18 \\times 72$ equals:",
                   ["$1\\,296$", "$1\\,286$", "$1\\,396$"],
                   "$18 \\times 70 = 1\\,260$ plus $18 \\times 2 = 36$: $1\\,296$.",
                   ["Eq(18*72, 1296)"]),
            ]),
            tapq("Estimate first", "$53 \\times 67$ should land near:",
                 ["$50 \\times 70 = 3\\,500$", "$500$", "$36\\,000$", "$5 \\times 7 = 35$"],
                 "Round both factors: $50 \\times 70 = 3\\,500$ — and the exact $3\\,551$ sits beside it. A product far from its estimate has lost a shift somewhere.",
                 ["Eq(50*70, 3500)", "Eq(53*67, 3551)"]),
            recap([
                "Split the second factor: tens part + ones part = two partial products.",
                "The tens row shifts one place left — that shift is its zero.",
                "Every digit of one factor meets every digit of the other, exactly once.",
                "Estimate with rounded factors; a missing shift shows up instantly.",
            ]),
            tip("Write BOTH rows for each of these, even where you could shortcut — the layout is the skill being built."),
            tryitset("Mixed practice", "Two-digit products, estimated then computed.", [
                tp("$35 \\times 35$ equals:",
                   ["$1\\,225$", "$1\\,125$", "$1\\,255$"],
                   "$35 \\times 30 = 1\\,050$ plus $35 \\times 5 = 175$: $1\\,225$.",
                   ["Eq(35*35, 1225)"]),
                tp("$29 \\times 61$ equals:",
                   ["$1\\,769$", "$1\\,669$", "$1\\,779$"],
                   "$29 \\times 60 = 1\\,740$ plus $29$: $1\\,769$. Estimate $30 \\times 60 = 1\\,800$ confirms.",
                   ["Eq(29*61, 1769)", "Eq(30*60, 1800)"]),
                tp("$214 \\times 23$ equals:",
                   ["$4\\,922$", "$4\\,822$", "$5\\,022$"],
                   "$4\\,280 + 642 = 4\\,922$.",
                   ["Eq(214*23, 4922)"]),
                tp("A camp buys $16$ crates of $48$ bottles. Bottles in all:",
                   ["$768$", "$668$", "$788$"],
                   "$16 \\times 48 = 16 \\times 50 - 16 \\times 2 = 800 - 32 = 768$.",
                   ["Eq(16*48, 768)", "Eq(800 - 32, 768)"]),
                tp("$80 \\times 90$ equals:",
                   ["$7\\,200$", "$720$", "$72\\,000$"],
                   "$8 \\times 9 = 72$, two zeros back: $7\\,200$.",
                   ["Eq(80*90, 7200)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Multiplying by Two Digits\"",
                    "Two rows, one shift, one sum — and the same pattern scales to three-digit factors and beyond: one row per digit, each shifted one more place. Next: division, multiplication's undo.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Division with Remainders
# ==========================================================================

def lesson_remainders():
    return {
        "slug": "division-with-remainders",
        "title": "Division with Remainders",
        "concreteComparison": (
            "You share $58$ sweets among $9$ friends. Six each uses "
            "$54$; four sweets sit left over — not enough for another "
            "round. That's division's honest answer: $58 \\div 9 = 6$ "
            "remainder $4$. The remainder is what's left when equal "
            "sharing has gone as far as it can."),
        "objective": (
            "Divide with remainders, state answers as quotient and "
            "remainder, verify with the receipt (quotient × divisor + "
            "remainder = dividend), and insist the remainder stays "
            "smaller than the divisor."),
        "concept": [
            "**Two questions, one operation.** $58 \\div 9$ asks either "
            "\"$58$ shared into $9$ equal parts — how big?\" or \"how "
            "many $9$s fit in $58$?\" Both give quotient $6$, remainder "
            "$4$.",
            "**The receipt:** quotient $\\times$ divisor $+$ remainder "
            "$=$ dividend. $6 \\times 9 + 4 = 58$ ✓. Every division can "
            "be rebuilt into a multiplication — that's how you check.",
            "**The remainder must be SMALLER than the divisor.** If $r "
            "\\ge d$, another whole share still fits: $50 \\div 6 = 7$ "
            "r $8$ is wrong ($8 \\ge 6$ — one more $6$ fits): the true "
            "answer is $8$ r $2$.",
        ],
        "keyIdea": (
            "Division finds how many whole shares fit and what's left: "
            "quotient × divisor + remainder = dividend, with the "
            "remainder always smaller than the divisor."),
        "facts": [
            {"title": "The receipt",
             "latex": "58 \\div 9 = 6 \\text{ r } 4 \\iff 6 \\times 9 + 4 = 58",
             "explanation": "Rebuild the dividend to check: shares times size, plus the leftover."},
            {"title": "The remainder rule",
             "latex": "r < d \\ \\text{always}",
             "explanation": "A remainder as big as the divisor means another whole share fits."},
        ],
        "workedExamples": [
            {"id": "g5md-l3-we1",
             "statement": "Compute $75 \\div 8$ and check the answer.",
             "note": "How many 8s fit? Then verify with the receipt.",
             "solution": ("$8 \\times 9 = 72$ fits; $8 \\times 10 = 80$ is too big. "
                          "Quotient $9$, remainder $75 - 72 = 3$. Receipt: $9 \\times "
                          "8 + 3 = 75$ ✓, and $3 < 8$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*9, 72)", "Eq(75 - 72, 3)"] + dchecks(75, 8, 9, 3)},
            {"id": "g5md-l3-we2",
             "statement": "A claim says $50 \\div 6 = 7$ remainder $8$. Judge it.",
             "note": "Check the remainder rule first.",
             "solution": ("The receipt holds ($7 \\times 6 + 8 = 50$) — but $8 \\ge "
                          "6$: another whole $6$ still fits in the leftover. Take it: "
                          "$50 \\div 6 = 8$ r $2$, receipt $8 \\times 6 + 2 = 50$ ✓, "
                          "$2 < 6$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7*6 + 8, 50)", "8 >= 6"] + dchecks(50, 6, 8, 2)},
        ],
        "commonMistakes": [
            {"text": "Leaving a remainder as big as the divisor — 50 ÷ 6 = 7 r 8.",
             "correction": "If r ≥ d, the sharing stopped early: another whole share fits. Push the quotient up until the leftover is SMALLER than the divisor: 8 r 2.",
             "authored": True},
            {"text": "Checking with multiplication but forgetting the remainder — 9 × 8 = 72 ≠ 75, \"so it's wrong\".",
             "correction": "The receipt has three parts: quotient × divisor PLUS remainder. 9 × 8 + 3 = 75 — the remainder belongs in the check.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5md-l3-t1",
             "statement": "Compute $92 \\div 9$ with its receipt.",
             "solution": "$9 \\times 10 = 90$; leftover $2$. So $10$ r $2$; receipt $10 \\times 9 + 2 = 92$ ✓, $2 < 9$ ✓.",
             "check": dchecks(92, 9, 10, 2)},
            {"id": "g5md-l3-t2",
             "statement": "Compute $67 \\div 7$ with its receipt.",
             "solution": "$7 \\times 9 = 63$; leftover $4$. So $9$ r $4$; receipt $9 \\times 7 + 4 = 67$ ✓, $4 < 7$ ✓.",
             "check": dchecks(67, 7, 9, 4)},
        ],
        "interactive": {"steps": [
            teach("Concept A", "What's left when sharing stops", [
                "$58 \\div 9$: how many whole $9$s fit in $58$? Six of them use $54$; the $4$ left can't make a seventh — QUOTIENT $6$, REMAINDER $4$.",
                "Same numbers, other reading: $58$ sweets shared among $9$ friends — $6$ each, $4$ left in the bag.",
                "Write it $58 \\div 9 = 6$ r $4$ — the remainder is part of the answer, not an apology.",
            ]),
            workedset("Fit, then count the leftover",
                      "Find the biggest multiple that fits; subtract for the remainder.", [
                wex("Compute $75 \\div 8$.",
                    ["$8 \\times 9 = 72$ fits, $8 \\times 10 = 80$ doesn't.",
                     "Remainder $75 - 72 = 3$: answer $9$ r $3$."],
                    "$9$ r $3$",
                    dchecks(75, 8, 9, 3)),
                wex("Compute $100 \\div 7$.",
                    ["$7 \\times 14 = 98$ fits, $7 \\times 15 = 105$ doesn't.",
                     "Remainder $2$: answer $14$ r $2$."],
                    "$14$ r $2$",
                    dchecks(100, 7, 14, 2)),
            ]),
            tryitset("Quotient and remainder", "Biggest fit first, then the leftover.", [
                tp("$43 \\div 5$ equals:",
                   ["$8$ r $3$", "$8$ r $5$", "$7$ r $8$"],
                   "$5 \\times 8 = 40$, leftover $3$. ($7$ r $8$ breaks the remainder rule — another $5$ fits.)",
                   dchecks(43, 5, 8, 3)),
                tp("$92 \\div 9$ equals:",
                   ["$10$ r $2$", "$9$ r $11$", "$10$ r $9$"],
                   "$9 \\times 10 = 90$, leftover $2$ — and both wrong options carry remainders $\\ge 9$.",
                   dchecks(92, 9, 10, 2)),
                tp("$67 \\div 7$ equals:",
                   ["$9$ r $4$", "$8$ r $11$", "$9$ r $7$"],
                   "$7 \\times 9 = 63$, leftover $4 < 7$ ✓.",
                   dchecks(67, 7, 9, 4)),
            ]),
            tapq("Receipt check", "Which computation CHECKS $75 \\div 8 = 9$ r $3$?",
                 ["$9 \\times 8 + 3 = 75$", "$9 \\times 8 = 72$", "$75 \\times 8 = 600$", "$9 + 8 + 3 = 20$"],
                 "The receipt rebuilds the dividend: quotient × divisor + remainder — $72 + 3 = 75$ ✓.",
                 ["Eq(9*8 + 3, 75)"]),
            funfact("Remainders run the calendar",
                    "\"What day of the week is it in 30 days?\" is a remainder question: $30 \\div 7 = 4$ r $2$ — four full weeks pass and the answer is two weekdays along. Clocks, calendars and rotas all count in remainders."),
            teach("Concept B", "The remainder rule", [
                "A remainder as big as the divisor is a division that STOPPED EARLY: $50 \\div 6 = 7$ r $8$ leaves an $8$ — but a whole $6$ still fits in it.",
                "Push on: $50 \\div 6 = 8$ r $2$. The rule: the remainder is always SMALLER than the divisor, $r < d$.",
                "So every answer gets two checks: the receipt ($q \\times d + r = n$) AND the rule ($r < d$). Both must hold.",
            ]),
            workedset("Catching stopped-early divisions",
                      "Receipt alone is not enough — check r < d too.", [
                wex("Judge the claim $50 \\div 6 = 7$ r $8$.",
                    ["Receipt: $7 \\times 6 + 8 = 50$ ✓ — but $8 \\ge 6$: rule broken.",
                     "One more $6$ fits: $8$ r $2$, and $2 < 6$ ✓."],
                    "wrong — the true answer is $8$ r $2$",
                    ["Eq(7*6 + 8, 50)", "8 >= 6"] + dchecks(50, 6, 8, 2)),
                wex("Judge the claim $88 \\div 4 = 21$ r $4$.",
                    ["$21 \\times 4 + 4 = 88$ ✓, but $r = 4 = d$: stopped early.",
                     "$88 \\div 4 = 22$ exactly — remainder $0$."],
                    "wrong — it divides exactly: $22$",
                    ["Eq(21*4 + 4, 88)"] + dchecks(88, 4, 22, 0)),
            ]),
            tryitset("Rule enforcement", "Receipt AND r < d — both, always.", [
                tp("Which answer is fully correct for $39 \\div 4$?",
                   ["$9$ r $3$", "$8$ r $7$", "$10$ r $-1$"],
                   "$9 \\times 4 + 3 = 39$ and $3 < 4$ ✓. ($8$ r $7$ passes the receipt but breaks the rule.)",
                   dchecks(39, 4, 9, 3) + ["Eq(8*4 + 7, 39)"]),
                tp("$85 \\div 6$ equals:",
                   ["$14$ r $1$", "$13$ r $7$", "$14$ r $6$"],
                   "$6 \\times 14 = 84$, leftover $1 < 6$ ✓.",
                   dchecks(85, 6, 14, 1)),
                tp("$60 \\div 6$ equals:",
                   ["$10$ exactly", "$9$ r $6$", "$10$ r $6$"],
                   "$6 \\times 10 = 60$ — remainder $0$. ($9$ r $6$ is the stopped-early version.)",
                   dchecks(60, 6, 10, 0)),
            ]),
            tapq("Spot the early stop", "$71 \\div 8 = 7$ r $15$ is wrong because:",
                 ["$15 \\ge 8$ — another whole $8$ fits (the answer is $8$ r $7$)",
                  "the receipt fails",
                  "remainders cannot exceed $9$",
                  "$71$ is odd"],
                 "$7 \\times 8 + 15 = 71$ — the receipt holds! Only the rule exposes it: $15$ holds another $8$, so push to $8$ r $7$ ($7 < 8$ ✓).",
                 ["Eq(7*8 + 15, 71)", "15 >= 8"] + dchecks(71, 8, 8, 7)),
            recap([
                "Quotient = how many whole shares fit; remainder = what's left.",
                "Receipt: quotient × divisor + remainder = dividend — every time.",
                "Rule: the remainder is SMALLER than the divisor, always.",
                "A receipt can pass while the rule fails — check both.",
            ]),
            tip("Every answer below needs both checks said aloud: the receipt and r < d. The second one catches what the first one misses."),
            tryitset("Mixed practice", "Divide, receipt, rule.", [
                tp("$53 \\div 7$ equals:",
                   ["$7$ r $4$", "$6$ r $11$", "$7$ r $7$"],
                   "$7 \\times 7 = 49$, leftover $4 < 7$ ✓.",
                   dchecks(53, 7, 7, 4)),
                tp("$99 \\div 4$ equals:",
                   ["$24$ r $3$", "$23$ r $7$", "$25$ r $1$"],
                   "$4 \\times 24 = 96$, leftover $3$. ($25$ would need $100$.)",
                   dchecks(99, 4, 24, 3)),
                tp("$84 \\div 6$ equals:",
                   ["$14$ exactly", "$13$ r $6$", "$14$ r $2$"],
                   "$6 \\times 14 = 84$ — divides exactly.",
                   dchecks(84, 6, 14, 0)),
                tp("$9$ friends share $75$ dumplings equally. Each gets, with leftovers:",
                   ["$8$ each, $3$ left", "$9$ each, $6$ short", "$7$ each, $12$ left"],
                   "$9 \\times 8 = 72$, three left over. ($7$ each leaves $12$ — enough for another round.)",
                   dchecks(75, 9, 8, 3)),
                tp("Which claim passes the receipt but FAILS the rule?",
                   ["$46 \\div 5 = 8$ r $6$", "$46 \\div 5 = 9$ r $1$", "$46 \\div 5 = 10$ r $4$"],
                   "$8 \\times 5 + 6 = 46$ ✓ but $6 \\ge 5$ ✗ — stopped early; the true answer is $9$ r $1$.",
                   ["Eq(8*5 + 6, 46)", "6 >= 5"] + dchecks(46, 5, 9, 1)),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Division with Remainders\"",
                    "Fit, leftover, receipt, rule — the full grammar of whole-number division. Next: LONG division, which runs this exact cycle place by place so no dividend is ever too big.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Long Division
# ==========================================================================

def lesson_long_division():
    return {
        "slug": "long-division",
        "title": "Long Division",
        "concreteComparison": (
            "Four friends split a prize of $5\\,208$ tögrög. Sharing "
            "thousands first, then hundreds, then tens, then ones — "
            "handing down whatever won't split — is exactly the written "
            "method: divide, multiply, subtract, bring down, repeat. "
            "Long division is short division done one place at a time."),
        "objective": (
            "Divide multi-digit numbers by a one-digit divisor with the "
            "long-division cycle, keep the zeros a quotient needs, and "
            "carry remainders correctly."),
        "concept": [
            "**The cycle:** DIVIDE the current amount, MULTIPLY back, "
            "SUBTRACT to find what's left, BRING DOWN the next digit — "
            "and repeat until the digits run out.",
            "**Sharing places, leftovers travel.** $5\\,208 \\div 4$: "
            "the $5$ thousands give $1$ each with $1$ left; that "
            "thousand becomes $10$ hundreds, joining the $2$: $12 \\div "
            "4 = 3$. Leftovers always slide one place right and keep "
            "playing.",
            "**Zeros hold their posts.** When a step divides to "
            "nothing — $0 \\div 4$ or a bring-down smaller than the "
            "divisor — the quotient takes a $0$ IN THAT PLACE. Skipping "
            "it shrinks the answer tenfold: $3\\,048 \\div 6$ is "
            "$508$, not $58$.",
        ],
        "keyIdea": (
            "Divide-multiply-subtract-bring-down, one place at a time, "
            "leftovers sliding right — and every quotient digit gets "
            "written, zeros included."),
        "facts": [
            {"title": "The cycle",
             "latex": "\\text{divide} \\to \\text{multiply} \\to \\text{subtract} \\to \\text{bring down}",
             "explanation": "One turn of the cycle per place of the dividend."},
            {"title": "The receipt, still",
             "latex": "5\\,208 \\div 4 = 1\\,302 \\iff 4 \\times 1\\,302 = 5\\,208",
             "explanation": "Long division answers check exactly like short ones."},
        ],
        "workedExamples": [
            {"id": "g5md-l4-we1",
             "statement": "Compute $5\\,208 \\div 4$ by long division.",
             "note": "Watch the zero take its post in the tens.",
             "solution": ("Thousands: $5 \\div 4 = 1$ r $1$. Bring down $2$: $12 \\div "
                          "4 = 3$. Bring down $0$: $0 \\div 4 = 0$ — the quotient "
                          "takes a $0$. Bring down $8$: $8 \\div 4 = 2$. Quotient "
                          "$1\\,302$; receipt $4 \\times 1\\,302 = 5\\,208$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12, 10 + 2)", "Eq(4*1302, 5208)"]},
            {"id": "g5md-l4-we2",
             "statement": "Compute $3\\,675 \\div 7$.",
             "note": "The first digit is smaller than the divisor — take two.",
             "solution": ("$3 < 7$, so start with $36$: $36 \\div 7 = 5$ r $1$. Bring "
                          "down $7$: $17 \\div 7 = 2$ r $3$. Bring down $5$: $35 \\div "
                          "7 = 5$. Quotient $525$; receipt $7 \\times 525 = 3\\,675$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7*5, 35)", "Eq(36 - 35, 1)", "Eq(7*525, 3675)"]},
        ],
        "commonMistakes": [
            {"text": "Skipping the zero when a step divides to nothing — 3,048 ÷ 6 = 58.",
             "correction": "Every bring-down produces a quotient digit, even when it's 0. 3,048 ÷ 6 = 508: the tens step (4 ÷ 6) writes a 0 before bringing down the 8.",
             "authored": True},
            {"text": "Losing a step's remainder instead of sliding it into the next place.",
             "correction": "The subtract step's leftover joins the brought-down digit: in 5,208 ÷ 4, the thousands' leftover 1 makes the next number 12, not 2.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5md-l4-t1",
             "statement": "Compute $936 \\div 4$.",
             "solution": "$9 \\div 4 = 2$ r $1$; $13 \\div 4 = 3$ r $1$; $16 \\div 4 = 4$. Quotient $234$; receipt $4 \\times 234 = 936$ ✓.",
             "check": ["Eq(4*234, 936)"]},
            {"id": "g5md-l4-t2",
             "statement": "Compute $6\\,037 \\div 8$ (a remainder survives).",
             "solution": "$60 \\div 8 = 7$ r $4$; $43 \\div 8 = 5$ r $3$; $37 \\div 8 = 4$ r $5$. Quotient $754$ r $5$; receipt $8 \\times 754 + 5 = 6\\,037$ ✓, $5 < 8$ ✓.",
             "check": dchecks(6037, 8, 754, 5)},
        ],
        "interactive": {"steps": [
            teach("Concept A", "The cycle, place by place", [
                "Long division shares the biggest places first: DIVIDE, MULTIPLY back, SUBTRACT the used amount, BRING DOWN the next digit — then the cycle turns again.",
                "$5\\,208 \\div 4$: thousands $5 \\div 4 = 1$ r $1$ — the leftover thousand becomes ten hundreds and joins the $2$: next up is $12$.",
                "Leftovers always slide one place right and stay in the game; nothing is ever thrown away until the ones are done.",
            ]),
            workedset("Turning the cycle",
                      "One quotient digit per turn.", [
                wex("Compute $5\\,208 \\div 4$.",
                    ["$5 \\div 4 = 1$ r $1$ → bring down $2$: $12 \\div 4 = 3$.",
                     "Bring down $0$: $0 \\div 4 = 0$ — write the zero. Bring down $8$: $8 \\div 4 = 2$.",
                     "Quotient $1\\,302$; receipt $4 \\times 1\\,302 = 5\\,208$ ✓."],
                    "$1\\,302$",
                    ["Eq(4*1302, 5208)"]),
                wex("Compute $3\\,675 \\div 7$.",
                    ["$3 < 7$: start with $36$. $36 \\div 7 = 5$ r $1$.",
                     "$17 \\div 7 = 2$ r $3$; $35 \\div 7 = 5$. Quotient $525$.",
                     "Receipt: $7 \\times 525 = 3\\,675$ ✓."],
                    "$525$",
                    ["Eq(7*525, 3675)"]),
            ]),
            tryitset("Run the cycle", "Divide, multiply, subtract, bring down — say it as you go.", [
                tp("$936 \\div 4$ equals:",
                   ["$234$", "$224$", "$134$"],
                   "$9 \\to 2$ r $1$; $13 \\to 3$ r $1$; $16 \\to 4$: $234$. Receipt $4 \\times 234 = 936$ ✓.",
                   ["Eq(4*234, 936)"]),
                tp("$2\\,415 \\div 5$ equals:",
                   ["$483$", "$473$", "$493$"],
                   "$24 \\to 4$ r $4$; $41 \\to 8$ r $1$; $15 \\to 3$: $483$. Receipt $5 \\times 483 = 2\\,415$ ✓.",
                   ["Eq(5*483, 2415)"]),
                tp("$812 \\div 7$ equals:",
                   ["$116$", "$126$", "$106$"],
                   "$8 \\to 1$ r $1$; $11 \\to 1$ r $4$; $42 \\to 6$: $116$. Receipt $7 \\times 116 = 812$ ✓.",
                   ["Eq(7*116, 812)"]),
            ]),
            tapq("Where does the leftover go?", "In $5\\,208 \\div 4$, the thousands step leaves $1$. The next number to divide is:",
                 ["$12$ — the leftover thousand becomes ten hundreds and joins the $2$",
                  "$2$ — the leftover is discarded",
                  "$1$ — divide the leftover alone",
                  "$52$ — take two digits again"],
                 "The leftover slides one place right: one thousand = ten hundreds, plus the dividend's own $2$ hundreds = $12$.",
                 ["Eq(10 + 2, 12)"]),
            funfact("Why it's called LONG",
                    "The name distinguishes it from \"short division\", where the leftovers are held in your head and only the quotient is written. Long division writes every subtract step down — slower, but it never overloads anyone's memory, which is why schools teach it first."),
            teach("Concept B", "Zeros on duty, remainders at the end", [
                "When a step divides to nothing — $0 \\div 4$, or a brought-down number smaller than the divisor — the quotient still takes a digit: $0$, in that place.",
                "$3\\,048 \\div 6$: $30 \\to 5$; bring down $4$ — but $4 < 6$, so write $0$ and bring down the $8$: $48 \\to 8$. Quotient $508$, not $58$ — skipping the zero shrinks the answer tenfold.",
                "If the ones step leaves something, that's the final remainder — and both old checks apply: receipt and $r < d$.",
            ]),
            workedset("The zero's post",
                      "Every bring-down writes a digit — zeros included.", [
                wex("Compute $3\\,048 \\div 6$.",
                    ["$30 \\div 6 = 5$. Bring down $4$: $4 < 6$ — write $0$.",
                     "Bring down $8$: $48 \\div 6 = 8$. Quotient $508$.",
                     "Receipt: $6 \\times 508 = 3\\,048$ ✓."],
                    "$508$",
                    ["Eq(6*508, 3048)"]),
                wex("Compute $8\\,569 \\div 6$.",
                    ["$8 \\to 1$ r $2$; $25 \\to 4$ r $1$; $16 \\to 2$ r $4$; $49 \\to 8$ r $1$.",
                     "Quotient $1\\,428$ remainder $1$; receipt $6 \\times 1\\,428 + 1 = 8\\,569$ ✓."],
                    "$1\\,428$ r $1$",
                    dchecks(8569, 6, 1428, 1)),
            ]),
            tryitset("Zeros and remainders", "Watch for posts the zero must hold.", [
                tp("$9\\,000 \\div 8$ equals:",
                   ["$1\\,125$", "$1\\,025$", "$1\\,215$"],
                   "$9 \\to 1$ r $1$; $10 \\to 1$ r $2$; $20 \\to 2$ r $4$; $40 \\to 5$: $1\\,125$. Receipt $8 \\times 1\\,125 = 9\\,000$ ✓.",
                   ["Eq(8*1125, 9000)"]),
                tp("$4\\,231 \\div 9$ equals:",
                   ["$470$ r $1$", "$47$ r $1$", "$470$ r $10$"],
                   "$42 \\to 4$ r $6$; $63 \\to 7$; bring down $1$: $1 < 9$ — write $0$, remainder $1$. Receipt $9 \\times 470 + 1 = 4\\,231$ ✓.",
                   dchecks(4231, 9, 470, 1)),
                tp("$1\\,000 \\div 3$ equals:",
                   ["$333$ r $1$", "$333$", "$334$ r $2$"],
                   "$10 \\to 3$ r $1$; $10 \\to 3$ r $1$; $10 \\to 3$ r $1$: $333$ r $1$. Receipt $3 \\times 333 + 1 = 1\\,000$ ✓.",
                   dchecks(1000, 3, 333, 1)),
            ]),
            tapq("The tenfold trap", "$3\\,048 \\div 6 = 58$ must be wrong because:",
                 ["$6 \\times 58 = 348$, nowhere near $3\\,048$ — a quotient zero was skipped",
                  "$58$ is even",
                  "$3\\,048$ doesn't divide by $6$",
                  "long division never gives two-digit answers"],
                 "The receipt exposes it instantly: $6 \\times 58 = 348 \\ne 3\\,048$. The tens place needed its $0$: the true quotient is $508$.",
                 ["Eq(6*58, 348)", "Ne(348, 3048)", "Eq(6*508, 3048)"]),
            recap([
                "The cycle: divide, multiply, subtract, bring down — one quotient digit per turn.",
                "Leftovers slide one place right and join the next digit.",
                "Every bring-down writes a quotient digit — zeros hold their posts.",
                "Finish with the receipt (and r < d when a remainder survives).",
            ]),
            tip("Run the receipt on every quotient below — the tenfold trap (a skipped zero) is invisible until you multiply back."),
            tryitset("Mixed practice", "Full cycles, receipts always.", [
                tp("$7\\,504 \\div 4$ equals:",
                   ["$1\\,876$", "$1\\,866$", "$1\\,976$"],
                   "$7 \\to 1$ r $3$; $35 \\to 8$ r $3$; $30 \\to 7$ r $2$; $24 \\to 6$: $1\\,876$. Receipt ✓.",
                   ["Eq(4*1876, 7504)"]),
                tp("$6\\,300 \\div 9$ equals:",
                   ["$700$", "$70$", "$710$"],
                   "$63 \\to 7$; two zeros hold their posts: $700$. Receipt $9 \\times 700 = 6\\,300$ ✓.",
                   ["Eq(9*700, 6300)"]),
                tp("$5\\,000 \\div 6$ equals:",
                   ["$833$ r $2$", "$833$ r $8$", "$832$ r $2$"],
                   "$50 \\to 8$ r $2$; $20 \\to 3$ r $2$; $20 \\to 3$ r $2$: $833$ r $2$; receipt $6 \\times 833 + 2 = 5\\,000$ ✓.",
                   dchecks(5000, 6, 833, 2)),
                tp("Four friends split $5\\,208$ tögrög. Each receives:",
                   ["$1\\,302$", "$1\\,320$", "$1\\,203$"],
                   "$5\\,208 \\div 4 = 1\\,302$ — the tens zero on duty. Receipt $4 \\times 1\\,302 = 5\\,208$ ✓.",
                   ["Eq(4*1302, 5208)"]),
                tp("$2\\,163 \\div 7$ equals:",
                   ["$309$", "$39$", "$319$"],
                   "$21 \\to 3$; bring down $6$: $6 < 7$ — write $0$; $63 \\to 9$: $309$. Receipt $7 \\times 309 = 2\\,163$ ✓.",
                   ["Eq(7*309, 2163)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Long Division\"",
                    "Divide, multiply, subtract, bring down — the cycle that tames any dividend. One lesson left in the topic: choosing WHICH operation a story needs, and what to do when a remainder shows up in real life.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Choosing the Operation
# ==========================================================================

def lesson_choosing():
    return {
        "slug": "choosing-the-operation",
        "title": "Choosing the Operation",
        "concreteComparison": (
            "\"$130$ students, buses seat $40$ — how many buses?\" The "
            "division says $3$ r $10$, but the ANSWER is $4$: those ten "
            "students still need a seat. Real problems don't name their "
            "operation, and they definitely don't tell you what the "
            "remainder means. Reading the STRUCTURE — equal groups? "
            "sharing? comparing? — is the last and biggest skill of this "
            "topic."),
        "objective": (
            "Choose multiplication or division (or both, with addition "
            "and subtraction) from a story's structure, and interpret "
            "remainders: round up, drop, or report."),
        "concept": [
            "**Equal groups → multiply.** \"$12$ boxes of $145$ "
            "pencils\" is $12 \\times 145$. Seeing the same-size group "
            "repeated is the multiplication signal — whatever verbs the "
            "story uses.",
            "**Sharing or grouping → divide.** \"Split $1\\,740$ among "
            "$29$ classes\" shares (how big is each part?); \"how many "
            "$40$-seat buses for $130$?\" groups (how many parts?). "
            "Both are division.",
            "**The remainder means what the STORY says.** Buses: round "
            "UP ($3$ r $10$ → $4$ buses — people can't be left). Full "
            "boxes from $130$ eggs by dozens: DROP ($10$ full). \"How "
            "many left over?\": the remainder itself IS the answer.",
        ],
        "keyIdea": (
            "Structure picks the operation — repeated equal groups "
            "multiply, sharing and grouping divide — and the story, not "
            "the arithmetic, decides what the remainder means."),
        "facts": [
            {"title": "The three remainder readings",
             "latex": "\\text{round up} \\ / \\ \\text{drop} \\ / \\ \\text{report}",
             "explanation": "Buses round up; full boxes drop; \"how many left\" reports the remainder itself."},
            {"title": "Structure over signal words",
             "latex": "\\text{equal groups} \\to \\times \\qquad \\text{share/group} \\to \\div",
             "explanation": "Words like \"each\" appear in both kinds — the structure decides, not the vocabulary."},
        ],
        "workedExamples": [
            {"id": "g5md-l5-we1",
             "statement": ("A school orders $12$ boxes of $145$ pencils and shares "
                           "them equally among $29$ classes. How many pencils does "
                           "each class receive?"),
             "note": "Two structures in one story: equal groups, then sharing.",
             "solution": ("Equal groups first: $12 \\times 145 = 1\\,740$ pencils. "
                          "Then share: $1\\,740 \\div 29 = 60$ each — receipt $29 "
                          "\\times 60 = 1\\,740$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12*145, 1740)", "Eq(29*60, 1740)"]},
            {"id": "g5md-l5-we2",
             "statement": ("$130$ students travel by $40$-seat buses. How many buses "
                           "are needed?"),
             "note": "The remainder decides the answer's direction.",
             "solution": ("$130 \\div 40 = 3$ r $10$: three full buses and ten "
                          "students still standing. They ride too — round UP: $4$ "
                          "buses. (Receipt: $3 \\times 40 + 10 = 130$ ✓.)"),
             "badges": [{"text": "core"}],
             "check": dchecks(130, 40, 3, 10) + ["Eq(3 + 1, 4)"]},
        ],
        "commonMistakes": [
            {"text": "Answering the bare division when the story needs the remainder interpreted — \"3 buses\" for 130 students.",
             "correction": "Finish the story: 3 buses seat 120, and 10 students remain. The context rounds UP to 4. Always re-read the question after dividing.",
             "authored": True},
            {"text": "Multiplying whenever numbers look big and dividing when they look small.",
             "correction": "Size is not structure. Ask: are equal groups being COMBINED (multiply) or is a total being SPLIT (divide)? The numbers' sizes have no vote.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5md-l5-t1",
             "statement": ("Eggs come $12$ to a box. From $130$ eggs, how many FULL "
                           "boxes can be packed?"),
             "solution": "$130 \\div 12 = 10$ r $10$: ten full boxes; the ten loose eggs don't fill an eleventh — DROP the remainder. Answer: $10$.",
             "check": dchecks(130, 12, 10, 10)},
            {"id": "g5md-l5-t2",
             "statement": ("A rope of $75$ m is cut into $9$ m pieces. How many "
                           "pieces, and how much rope is left over?"),
             "solution": "$75 \\div 9 = 8$ r $3$: eight pieces, and the leftover question REPORTS the remainder — $3$ m remain.",
             "check": dchecks(75, 9, 8, 3)},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Structure picks the operation", [
                "Stories don't name their operation. Look for the STRUCTURE: the same-size group repeated — \"$12$ boxes of $145$\" — multiplies.",
                "A total being split — \"share $1\\,740$ among $29$ classes\" — divides. So does grouping: \"how many $40$s fit in $130$?\"",
                "Signal words lie: \"each\" appears in both kinds. Ask what is HAPPENING — combining equal groups, or splitting a total?",
            ]),
            workedset("Read the structure",
                      "Name the structure aloud, then compute.", [
                wex("$12$ boxes of $145$ pencils, shared among $29$ classes — each class gets?",
                    ["Combine equal groups: $12 \\times 145 = 1\\,740$.",
                     "Split the total: $1\\,740 \\div 29 = 60$ each; receipt $29 \\times 60 = 1\\,740$ ✓."],
                    "$60$ pencils",
                    ["Eq(12*145, 1740)", "Eq(29*60, 1740)"]),
                wex("A farm packs $8$ melons per crate and fills $37$ crates. Melons in all?",
                    ["Equal groups combined: $37 \\times 8 = 296$."],
                    "$296$ melons",
                    ["Eq(37*8, 296)"]),
            ]),
            tryitset("Which operation?", "Structure first; arithmetic second.", [
                tp("\"$24$ shelves hold $35$ books each. How many books?\" calls for:",
                   ["$24 \\times 35 = 840$", "$35 \\div 24$", "$24 + 35 = 59$"],
                   "Same-size groups repeated — multiply: $840$ books.",
                   ["Eq(24*35, 840)"]),
                tp("\"$840$ books are boxed $28$ to a box. How many boxes?\" calls for:",
                   ["$840 \\div 28 = 30$", "$840 \\times 28$", "$840 - 28$"],
                   "Grouping a total into equal parts — divide: $30$ boxes; receipt $28 \\times 30 = 840$ ✓.",
                   ["Eq(28*30, 840)"]),
                tp("\"$7$ friends share $91\\,000$ tögrög equally.\" Each receives:",
                   ["$13\\,000$", "$12\\,000$", "$13\\,500$"],
                   "Sharing — divide: $91\\,000 \\div 7 = 13\\,000$; receipt $7 \\times 13\\,000 = 91\\,000$ ✓.",
                   ["Eq(7*13000, 91000)"]),
            ]),
            tapq("Same word, two structures", "\"Each\" appears in both stories below. Which one DIVIDES?",
                 ["\"$156$ apples, $12$ EACH bag — how many bags?\"",
                  "\"$12$ bags with $156$ apples EACH — how many apples?\"",
                  "both multiply", "both divide"],
                 "The first splits a known total into groups (divide: $156 \\div 12 = 13$ bags); the second combines equal groups (multiply: $1\\,872$). The word \"each\" was in both — structure decided.",
                 ["Eq(12*13, 156)", "Eq(12*156, 1872)"]),
            funfact("Word problems are the oldest math homework",
                    "A Babylonian clay tablet nearly 4,000 years old asks how many workers are needed to dig a canal — given the volume each worker digs per day. Choosing the operation from a story is literally the oldest exercise in mathematics."),
            teach("Concept B", "What the remainder means", [
                "The division gives $q$ r $r$; the STORY says what to do with it. Buses for $130$ students at $40$ a bus: $3$ r $10$ — the ten still travel, so ROUND UP: $4$ buses.",
                "FULL boxes from $130$ eggs by dozens: $10$ r $10$ — the loose eggs don't fill a box: DROP, answer $10$.",
                "\"How much rope is LEFT?\": the remainder itself is the answer — REPORT it. Three readings, one rule: re-read the question after dividing.",
            ]),
            workedset("Three remainders, three fates",
                      "Round up, drop, or report — the story decides.", [
                wex("$130$ students, $40$-seat buses. Buses needed?",
                    ["$130 \\div 40 = 3$ r $10$ — ten students still need seats.",
                     "Round UP: $4$ buses."],
                    "$4$ buses",
                    dchecks(130, 40, 3, 10)),
                wex("A rope of $75$ m cut into $9$ m pieces — pieces, and leftover?",
                    ["$75 \\div 9 = 8$ r $3$.",
                     "Pieces: $8$ (drop for the count) — and the leftover question reports the $3$ m."],
                    "$8$ pieces, $3$ m left",
                    dchecks(75, 9, 8, 3)),
            ]),
            tryitset("Interpret the remainder", "Divide, then re-read the question.", [
                tp("$95$ hikers, tents sleep $6$. Tents needed:",
                   ["$16$", "$15$", "$15$ r $5$"],
                   "$95 \\div 6 = 15$ r $5$ — five hikers still need cover: round up to $16$.",
                   dchecks(95, 6, 15, 5) + ["Eq(15 + 1, 16)"]),
                tp("$200$ tögrög coins into rolls of $25$ — FULL rolls:",
                   ["$8$", "$9$", "$7$"],
                   "$200 \\div 25 = 8$ exactly — eight full rolls, nothing dropped, nothing over.",
                   dchecks(200, 25, 8, 0)),
                tp("$67$ dumplings, plates of $8$. \"How many dumplings DON'T fit on full plates?\"",
                   ["$3$", "$8$", "$9$"],
                   "$67 \\div 8 = 8$ r $3$ — the question asks for the REMAINDER: $3$.",
                   dchecks(67, 8, 8, 3)),
            ]),
            tapq("Round up or drop?", "Which story rounds its remainder UP?",
                 ["\"$50$ people, $4$-seat taxis — taxis needed?\"",
                  "\"$50$ eggs — full boxes of $12$?\"",
                  "\"$50$ m of cloth — how much left after $12$ m pieces?\"",
                  "none of them"],
                 "People must all travel: $50 \\div 4 = 12$ r $2$ → $13$ taxis. The eggs drop ($4$ full boxes), and the cloth question reports its remainder ($2$ m).",
                 dchecks(50, 4, 12, 2) + ["Eq(12 + 1, 13)"]),
            recap([
                "Equal groups combined → multiply; a total split (sharing or grouping) → divide.",
                "Signal words lie; structure decides.",
                "Remainders: round up (everyone must fit), drop (only full groups count), report (the leftover IS the question).",
                "Always re-read the question sentence after computing.",
            ]),
            tip("For each story: name the structure, compute, then say which remainder reading the question wants — three steps, out loud."),
            tryitset("Mixed practice", "Full stories, operations chosen by you.", [
                tp("A hall seats $18$ rows of $26$. Total seats:",
                   ["$468$", "$458$", "$488$"],
                   "Equal groups: $18 \\times 26 = 468$.",
                   ["Eq(18*26, 468)"]),
                tp("$468$ programmes are printed in packs of $50$. Packs to order so every seat gets one:",
                   ["$10$", "$9$", "$9$ r $18$"],
                   "$468 \\div 50 = 9$ r $18$ — the $18$ still need programmes: round up to $10$ packs.",
                   dchecks(468, 50, 9, 18) + ["Eq(9 + 1, 10)"]),
                tp("$1\\,275$ kg of supplies is loaded onto $7$ vans as equally as whole kilograms allow. Each van carries, with the leftover:",
                   ["$182$ kg, $1$ kg left", "$183$ kg, $6$ kg short", "$180$ kg, $15$ kg left"],
                   "$1\\,275 \\div 7 = 182$ r $1$: receipt $7 \\times 182 + 1 = 1\\,275$ ✓.",
                   dchecks(1275, 7, 182, 1)),
                tp("A bakery sells trays of $6$ buns. From $1\\,005$ buns, FULL trays:",
                   ["$167$", "$168$", "$167$ r $3$"],
                   "$1\\,005 \\div 6 = 167$ r $3$ — the three loose buns don't fill a tray: drop, $167$ full trays.",
                   dchecks(1005, 6, 167, 3)),
                tp("Which story needs BOTH operations: multiply, then divide?",
                   ["\"$15$ crates of $24$ bottles shared among $9$ shops — bottles per shop?\"",
                    "\"$15$ crates of $24$ bottles — total bottles?\"",
                    "\"$360$ bottles among $9$ shops — bottles per shop?\""],
                   "Total first ($15 \\times 24 = 360$), then share ($360 \\div 9 = 40$). The other two are single-step.",
                   ["Eq(15*24, 360)", "Eq(9*40, 360)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Choosing the Operation\" — and the topic",
                    "Distributive multiplying, the two-row layout, remainders with receipts, the long-division cycle, and structure-reading: whole-number arithmetic is now complete. Grade 5's road continues into fractions — where a remainder learns to be a number of its own.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5md-pr1", "Compute $8 \\times 2\\,679$.",
             "$16\\,000 + 4\\,800 + 560 + 72 = 21\\,432$.",
             ["Eq(8*2679, 21432)"]),
        prob("g5md-pr2", "Compute $9 \\times 4\\,000$ and $6 \\times 5\\,500$.",
             "$9 \\times 4 = 36$, three zeros: $36\\,000$. $6 \\times 55 = 330$, two zeros: $33\\,000$.",
             ["Eq(9*4000, 36000)", "Eq(6*5500, 33000)"]),
        prob("g5md-pr3", "Compute $67 \\times 84$.",
             "$67 \\times 80 = 5\\,360$ plus $67 \\times 4 = 268$: $5\\,628$. Estimate $70 \\times 80 = 5\\,600$ confirms.",
             ["Eq(67*80, 5360)", "Eq(67*4, 268)", "Eq(67*84, 5628)", "Eq(70*80, 5600)"]),
        prob("g5md-pr4", "Compute $309 \\times 45$.",
             "$309 \\times 40 = 12\\,360$ plus $309 \\times 5 = 1\\,545$: $13\\,905$.",
             ["Eq(309*40, 12360)", "Eq(309*5, 1545)", "Eq(309*45, 13905)"]),
        prob("g5md-pr5", "Compute $94 \\div 8$ with receipt and rule.",
             "$8 \\times 11 = 88$, leftover $6$: $11$ r $6$. Receipt $11 \\times 8 + 6 = 94$ ✓, $6 < 8$ ✓.",
             dchecks(94, 8, 11, 6)),
        prob("g5md-pr6", "Compute $7\\,236 \\div 6$ by long division.",
             "$7 \\to 1$ r $1$; $12 \\to 2$ exactly; bring down $3$ — it is smaller than $6$, so the quotient takes a $0$ and the $3$ waits; $36 \\to 6$. Quotient $1\\,206$; receipt $6 \\times 1\\,206 = 7\\,236$ ✓.",
             ["Eq(6*1206, 7236)"]),
        prob("g5md-pr7", "Compute $5\\,830 \\div 9$.",
             "$58 \\to 6$ r $4$; $43 \\to 4$ r $7$; $70 \\to 7$ r $7$. Quotient $647$ r $7$; receipt $9 \\times 647 + 7 = 5\\,830$ ✓, $7 < 9$ ✓.",
             dchecks(5830, 9, 647, 7)),
        prob("g5md-pr8", ("A theatre runs $23$ shows selling $184$ tickets each. The "
                          "tickets are printed in books of $50$. How many books were "
                          "used, if partly-used books count?"),
             "Total: $23 \\times 184 = 4\\,232$ tickets. Books: $4\\,232 \\div 50 = 84$ r $32$ — the partly-used book counts: $85$ books.",
             ["Eq(23*184, 4232)"] + dchecks(4232, 50, 84, 32) + ["Eq(84 + 1, 85)"]),
    ]


def test_bank():
    return [
        prob("g5md-x1", "Compute $7 \\times 3\\,568$.",
             "$21\\,000 + 3\\,500 + 420 + 56 = 24\\,976$.",
             ["Eq(7*3568, 24976)"]),
        prob("g5md-x2", "Compute $58 \\times 73$.",
             "$58 \\times 70 = 4\\,060$ plus $58 \\times 3 = 174$: $4\\,234$.",
             ["Eq(58*70, 4060)", "Eq(58*3, 174)", "Eq(58*73, 4234)"]),
        prob("g5md-x3", "Compute $86 \\div 7$, with both checks.",
             "$7 \\times 12 = 84$, leftover $2$: $12$ r $2$. Receipt $12 \\times 7 + 2 = 86$ ✓, $2 < 7$ ✓.",
             dchecks(86, 7, 12, 2)),
        prob("g5md-x4", "Compute $6\\,048 \\div 7$ by long division.",
             "$60 \\to 8$ r $4$; $44 \\to 6$ r $2$; $28 \\to 4$. Quotient $864$; receipt $7 \\times 864 = 6\\,048$ ✓.",
             ["Eq(7*864, 6048)"]),
        prob("g5md-x5", ("Judge this claim and correct it if needed: "
                         "$61 \\div 7 = 7$ remainder $12$."),
             "Receipt: $7 \\times 7 + 12 = 61$ ✓ — but $12 \\ge 7$ breaks the rule: another $7$ fits. Correct answer: $8$ r $5$ ($8 \\times 7 + 5 = 61$ ✓, $5 < 7$ ✓).",
             ["Eq(7*7 + 12, 61)", "12 >= 7"] + dchecks(61, 7, 8, 5)),
        prob("g5md-x6", ("A club of $278$ members travels in minibuses seating $16$. "
                         "How many minibuses must be hired, and how many empty seats "
                         "ride along?"),
             "$278 \\div 16 = 17$ r $6$: seventeen full buses leave $6$ members standing — hire $18$. Empty seats on the last bus: $16 - 6 = 10$.",
             dchecks(278, 16, 17, 6) + ["Eq(17 + 1, 18)", "Eq(16 - 6, 10)"]),
    ]


def main():
    topic = {
        "slug": "multiplication-and-division",
        "title": "Multiplication & Division",
        "grade": 5,
        "status": "published",
        "blurb": ("One- and two-digit multiplication built on the distributive "
                  "idea, division with remainders and its receipt, long division, "
                  "and choosing the operation a story needs."),
        "lessons": [
            lesson_one_digit(),
            lesson_two_digit(),
            lesson_remainders(),
            lesson_long_division(),
            lesson_choosing(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "multiplication-and-division.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
