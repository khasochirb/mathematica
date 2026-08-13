#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic 1: Numbers to 10 000.

Reading and writing four-digit numbers (numerals and words, both ways,
with zero holding empty columns), place value to thousands (what each
digit is worth, expanded form, building numbers from parts), comparing
and ordering (place by place from the LEFT, between-ness on the number
line), rounding to the nearest 10 and 100 (the two neighbours, the
halfway rule, round-then-estimate), and number patterns (skip counting
by 25s, 50s and 100s; odd and even from the ones digit alone).

Through-line: THE PLACE GIVES THE DIGIT ITS VALUE. A 7 can mean seven,
seventy, or seven thousand — every lesson in this topic is one more
consequence of reading the place before the digit.

Same construction as the Grade 5 builders: every check anywhere in the
structure is sympy-asserted with exact integers BEFORE the JSON is
written — a wrong number fact cannot ship. Figures are built from the
SAME Python variables as the statements they illustrate, so text and
picture cannot disagree.

Run: python3 scripts/grade3/build_numbers_to_10000.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (withprobfig, C_GREEN, C_WARM, fig_groups, fig_numline,  # noqa: E402
                     funfact, near, prob, recap, tapq, teach, th, tip, tp,
                     tryitset, wex, withfig, workedset, write_topic)


def M(v):
    """A number typeset in math mode with thin-space separators."""
    return "$" + th(v) + "$"


def lab(v):
    """A number-line label: plain text with a space separator."""
    return "{:,}".format(v).replace(",", " ")


# ==========================================================================
# Lesson 1 — Reading & Writing Numbers
# ==========================================================================

def lesson_reading():
    # figure numbers, shared by statements and figure configs
    n1 = 3482          # columns demo: 3 thousands, 4 hundreds, 8 tens, 2 ones
    n2 = 4052          # zero-as-placeholder demo: 4 thousands, 5 tens, 2 ones
    fig_cols = fig_groups((3, "thousands"), (4, "hundreds"),
                          (8, "tens"), (2, "ones"))
    # The hundreds group is kept with a count of 0 — an empty column that is
    # still standing is the whole point of the beat, and dropping it would
    # draw the columns of 452 instead.
    fig_zero = fig_groups((4, "thousands"), (0, "hundreds"),
                          (5, "tens"), (2, "ones"))
    return {
        "slug": "reading-and-writing-numbers",
        "title": "Reading & Writing Numbers",
        "concreteComparison": (
            "A herder with " + M(n1) + " sheep cannot count them one by "
            "one at a glance — but say the number as THREE thousands, "
            "FOUR hundreds, EIGHT tens and TWO ones, and it fits in "
            "four short words. Every four-digit number is just four "
            "columns standing in a row, and each column has a name: "
            "thousands, hundreds, tens, ones."),
        "objective": (
            "Read four-digit numerals in words and write word names as "
            "numerals, name the thousands, hundreds, tens and ones "
            "columns, and use zero to hold a column that is empty."),
        "concept": [
            "**Four columns, four names.** A four-digit number has a "
            "thousands column, a hundreds column, a tens column and a "
            "ones column — always in that order, biggest on the left. "
            "In " + M(n1) + ": $3$ thousands, $4$ hundreds, $8$ tens, "
            "$2$ ones.",
            "**Reading is naming the columns.** " + M(n1) + " reads "
            "\"three thousand four hundred and eighty-two\" — the words "
            "walk the columns left to right. Writing goes the other "
            "way: hear the words, fill the columns. The little word "
            "\"and\" before the last part is optional: \"three thousand "
            "four hundred and eighty-two\" and \"three thousand four "
            "hundred eighty-two\" name the same number. This topic "
            "always says \"and\", so your answers can too.",
            "**Zero holds an empty column.** " + M(n2) + " has NO "
            "hundreds — but the column cannot be left out, or the "
            "other digits would slide into the wrong places. The zero "
            "is a guard standing in the empty column.",
        ],
        "keyIdea": (
            "Four-digit numbers are four named columns — thousands, "
            "hundreds, tens, ones. Reading walks the columns left to "
            "right, and zero stands guard in any column that is "
            "empty."),
        "facts": [
            {"title": "The four columns",
             "latex": th(n1) + " = 3\\ \\text{thousands},\\ 4\\ \\text{hundreds},\\ 8\\ \\text{tens},\\ 2\\ \\text{ones}",
             "explanation": "Biggest column on the left; each digit sits in exactly one column."},
            {"title": "Zero stands guard",
             "latex": th(n2) + " = 4\\ \\text{thousands},\\ 0\\ \\text{hundreds},\\ 5\\ \\text{tens},\\ 2\\ \\text{ones}",
             "explanation": "An empty column keeps its zero — drop it and every other digit slides."},
        ],
        "workedExamples": [
            {"id": "g4nu-l1-we1",
             "statement": "Write " + M(n1) + " in words.",
             "note": "Walk the columns left to right.",
             "solution": ("$3$ thousands, $4$ hundreds, $8$ tens, $2$ ones: "
                          "\"three thousand four hundred and eighty-two\". The "
                          "columns rebuild it: $3\\,000 + 400 + 80 + 2 = " + th(n1) + "$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*1000 + 4*100 + 8*10 + 2, 3482)"]},
            {"id": "g4nu-l1-we2",
             "statement": "Write \"four thousand and fifty-two\" as a numeral.",
             "note": "No hundreds are spoken — so the hundreds column gets a zero.",
             "solution": ("$4$ in the thousands, nothing in the hundreds, $5$ in "
                          "the tens, $2$ in the ones: " + M(n2) + ". The zero "
                          "guards the empty hundreds column — without it the "
                          "digits would collapse to $452$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*1000 + 5*10 + 2, 4052)"]},
        ],
        "commonMistakes": [
            {"text": "Putting the fifty in the wrong column — writing \"four thousand and fifty-two\" as 4 520.",
             "correction": "Fifty is 5 TENS. The hundreds column is empty and keeps its zero: 4 052. Adding the columns back exposes the slip — 4 000 + 500 + 20 makes 4 520, the wrong number.",
             "authored": True},
            {"text": "Skipping the zero when reading — calling 4 052 \"four hundred and fifty-two\".",
             "correction": "The 4 stands in the THOUSANDS column, four places from the right. Read the columns, not just the digits: four thousand and fifty-two.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4nu-l1-t1",
             "statement": "Write " + M(6704) + " in words.",
             "solution": "$6$ thousands, $7$ hundreds, $0$ tens, $4$ ones: \"six thousand seven hundred and four\". The empty tens column is silent in words but keeps its zero in the numeral.",
             "check": ["Eq(6*1000 + 7*100 + 4, 6704)"]},
            {"id": "g4nu-l1-t2",
             "statement": "Write \"nine thousand six hundred and forty\" as a numeral.",
             "solution": "Columns: $9$, $6$, $4$, and an empty ones column — " + M(9640) + ".",
             "check": ["Eq(9*1000 + 6*100 + 4*10, 9640)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Four columns, read left to right", [
                "Every four-digit number is four columns standing in a row: THOUSANDS, HUNDREDS, TENS, ONES — biggest on the left. The place gives the digit its value.",
                M(n1) + " is $3$ thousands, $4$ hundreds, $8$ tens and $2$ ones — the picture below shows the four columns as four groups.",
                "Reading just walks the columns: \"three thousand four hundred and eighty-two\". Writing walks back: hear the words, fill the columns.",
            ]), fig_cols),
            workedset("Numerals into words",
                      "Name each column, then say them left to right.", [
                wex("Write " + M(n1) + " in words.",
                    ["Columns: $3$ thousands, $4$ hundreds, $8$ tens, $2$ ones.",
                     "\"Three thousand four hundred and eighty-two\" — and the columns rebuild it: $3\\,000 + 400 + 80 + 2$."],
                    "three thousand four hundred and eighty-two",
                    ["Eq(3*1000 + 4*100 + 8*10 + 2, 3482)"]),
                wex("Write " + M(5217) + " in words.",
                    ["Columns: $5$, $2$, $1$, $7$.",
                     "\"Five thousand two hundred and seventeen\"."],
                    "five thousand two hundred and seventeen",
                    ["Eq(5*1000 + 2*100 + 1*10 + 7, 5217)"]),
            ]),
            tryitset("Name the columns", "Which column is each digit standing in?", [
                tp("In " + M(7368) + ", the digit in the hundreds column is:",
                   ["$3$", "$6$", "$7$"],
                   "Count columns from the left: $7$ thousands, $3$ hundreds, $6$ tens, $8$ ones. The hundreds digit is $3$ — the $6$ is tens and the $7$ is thousands.",
                   ["Eq(7*1000 + 3*100 + 6*10 + 8, 7368)"]),
                tp("Written in words, " + M(2590) + " is:",
                   ["two thousand five hundred and ninety",
                    "two thousand and fifty-nine",
                    "two hundred and fifty-nine"],
                   "Columns: $2$ thousands, $5$ hundreds, $9$ tens, $0$ ones. \"Two thousand and fifty-nine\" would be " + M(2059) + " — it moves the $5$ out of the hundreds.",
                   ["Eq(2*1000 + 5*100 + 9*10, 2590)"]),
                tp("Which numeral is \"eight thousand three hundred and six\"?",
                   ["$8\\,306$", "$8\\,360$", "$8\\,036$"],
                   "Six ONES, so the $6$ ends the number and a zero guards the tens: " + M(8306) + ". Choosing $8\\,360$ puts the six in the tens — that reads \"sixty\".",
                   ["Eq(8*1000 + 3*100 + 6, 8306)"]),
            ]),
            tapq("Find the column", "In " + M(6437) + ", the digit $4$ stands in which column?",
                 ["hundreds", "tens", "thousands", "ones"],
                 "Walk from the left: $6$ thousands, $4$ hundreds, $3$ tens, $7$ ones. Standing in the hundreds column, the $4$ is worth $4 \\times 100 = 400$ — the place gives the digit its value.",
                 ["Eq(6*1000 + 4*100 + 3*10 + 7, 6437)", "Eq(4*100, 400)"]),
            funfact("Nine thousand of them",
                    "How many four-digit numbers exist? They run from $1\\,000$ up to $9\\,999$, so there are $9\\,999 - 1\\,000 + 1 = 9\\,000$ of them — nine thousand numbers, and this topic's four columns can name every single one."),
            withfig(teach("Concept B", "Zero stands guard", [
                "What if a column is EMPTY? " + M(n2) + " has $4$ thousands, $5$ tens, $2$ ones — and no hundreds at all. In the picture the hundreds column is still standing, holding nothing: $0$ hundreds.",
                "The empty column still needs a digit, or everything slides: drop the zero from " + M(n2) + " and you get $452$ — a completely different number. Zero is the guard that keeps every other digit in its place.",
                "Words to numerals: \"three thousand and eight\" has empty hundreds AND empty tens — two guards: " + M(3008) + ".",
            ]), fig_zero),
            workedset("Words into numerals",
                      "Fill all four columns; empty ones get a zero.", [
                wex("Write \"four thousand and fifty-two\" as a numeral.",
                    ["Thousands $4$, hundreds empty, tens $5$, ones $2$.",
                     "The guard goes in: " + M(n2) + " — not $452$, which has lost a whole column."],
                    M(n2),
                    ["Eq(4*1000 + 5*10 + 2, 4052)"]),
                wex("Write \"six thousand seven hundred and four\" as a numeral.",
                    ["Thousands $6$, hundreds $7$, tens empty, ones $4$.",
                     M(6704) + " — the zero holds the tens."],
                    M(6704),
                    ["Eq(6*1000 + 7*100 + 4, 6704)"]),
            ]),
            tryitset("Guard duty", "Spot the empty columns before writing.", [
                tp("\"Three thousand and eight\" as a numeral is:",
                   ["$3\\,008$", "$3\\,800$", "$3\\,080$"],
                   "Eight ONES and two empty columns between: " + M(3008) + ". Writing $3\\,800$ promotes the eight into the hundreds — that reads \"eight hundred\".",
                   ["Eq(3*1000 + 8, 3008)"]),
                tp("In " + M(9041) + ", the zero holds which column?",
                   ["hundreds", "tens", "thousands"],
                   "Columns left to right: $9$ thousands, $0$ hundreds, $4$ tens, $1$ one. The guard stands in the hundreds.",
                   ["Eq(9*1000 + 4*10 + 1, 9041)"]),
                tp("Which number has a zero in the TENS column?",
                   ["$5\\,306$", "$5\\,360$", "$5\\,036$"],
                   "In " + M(5306) + " the columns are $5, 3, 0, 6$ — zero on tens duty. In $5\\,360$ the zero guards the ones; in $5\\,036$ it guards the hundreds.",
                   ["Eq(5*1000 + 3*100 + 6, 5306)"]),
            ]),
            tapq("The fifth column", "Counting up from " + M(9999) + ", the very next number needs:",
                 ["a fifth column — it is $10\\,000$",
                  "a bigger digit than $9$",
                  "no change — $9\\,999$ is the last number",
                  "a zero in front"],
                 "One more than " + M(9999) + " is $9\\,999 + 1 = 10\\,000$ — ten thousand, the first number too big for four columns. This whole topic lives below it.",
                 ["Eq(9999 + 1, 10000)"]),
            recap([
                "Four columns, left to right: thousands, hundreds, tens, ones.",
                "Reading walks the columns; writing fills them from the words.",
                "An empty column keeps a zero — drop it and every digit slides.",
                "The place gives the digit its value: the same 4 can mean 4, 40, 400 or 4 000.",
                "Ten thousand is the first number that needs a fifth column.",
            ]),
            tip("For every number below, touch each column and say its name — thousands, hundreds, tens, ones — before you answer. The naming is the method."),
            tryitset("Mixed practice", "Both directions, guards included.", [
                tp("Written in words, " + M(6235) + " is:",
                   ["six thousand two hundred and thirty-five",
                    "six thousand two hundred and fifty-three",
                    "six hundred and twenty-three"],
                   "Columns $6, 2, 3, 5$ — thirty-five, not fifty-three: the $3$ is tens and the $5$ is ones.",
                   ["Eq(6*1000 + 2*100 + 3*10 + 5, 6235)"]),
                tp("The thousands digit of " + M(1987) + " is:",
                   ["$1$", "$9$", "$7$"],
                   "Leftmost column of a four-digit number is thousands: the $1$, worth $1\\,000$. The $9$ is hundreds.",
                   ["Eq(1*1000 + 9*100 + 8*10 + 7, 1987)"]),
                tp("\"Seven thousand and ninety\" as a numeral is:",
                   ["$7\\,090$", "$7\\,900$", "$790$"],
                   "Ninety is $9$ TENS, so the hundreds column is empty and gets its guard: " + M(7090) + ". Writing $7\\,900$ turns ninety into nine hundred.",
                   ["Eq(7*1000 + 9*10, 7090)"]),
                tp("Written in words, " + M(2004) + " is:",
                   ["two thousand and four", "two hundred and four", "two thousand and forty"],
                   "Two guards hold the hundreds and tens; only thousands and ones speak: \"two thousand and four\". \"Two thousand and forty\" would be " + M(2040) + ".",
                   ["Eq(2*1000 + 4, 2004)"]),
                tp("A herder's winter count is " + M(5067) + " animals. In words that is:",
                   ["five thousand and sixty-seven",
                    "five thousand six hundred and seven",
                    "five hundred and sixty-seven"],
                   "Columns $5, 0, 6, 7$: the zero silences the hundreds, so the words jump from thousands straight to sixty-seven.",
                   ["Eq(5*1000 + 6*10 + 7, 5067)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Reading & Writing Numbers\"",
                    "Four named columns and a zero standing guard — you can now read and write every number below ten thousand. Next: what each digit is WORTH, and how to take a number apart into thousands, hundreds, tens and ones.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Place Value
# ==========================================================================

def lesson_place_value():
    n1 = 2745          # groups figure: 2 thousands, 7 hundreds, 4 tens, 5 ones
    n2 = 3482          # expanded-form star, built on the number line
    fig_cols = fig_groups((2, "thousands"), (7, "hundreds"),
                          (4, "tens"), (5, "ones"))
    # Three landings, not four: at this scale a step of 2 is thinner than the
    # marker itself, so plotting 3 482 beside 3 480 would draw one dot with
    # two labels. The last tiny step is told in prose instead — and how small
    # it looks next to a jump of 3 000 is itself the place-value point.
    fig_build = fig_numline([(3000, lab(3000)), (3400, lab(3400)),
                             (3480, lab(3480), C_WARM)],
                            lo=3000, hi=3500)
    return {
        "slug": "place-value",
        "title": "Place Value",
        "concreteComparison": (
            "Pay " + M(3482) + " togrog at the shop: three $1\\,000$ "
            "notes, four $100$ notes, eight $10$ coins and two $1$ "
            "coins. The SAME kind of counting hides inside every "
            "number — each digit is a count of notes of one size, and "
            "the column says which size. That is place value."),
        "objective": (
            "Say what each digit of a four-digit number is worth, "
            "write numbers in expanded form, and build numbers back "
            "from thousands, hundreds, tens and ones."),
        "concept": [
            "**A digit's worth is digit times place.** In " + M(n2) +
            " the $3$ stands in the thousands column, so it is worth "
            "$3 \\times 1\\,000 = 3\\,000$ — not $3$. Same digit in "
            "the tens column would be worth only $30$.",
            "**Expanded form takes the number apart.** " + M(n2) +
            " $= 3\\,000 + 400 + 80 + 2$: one part per column, and "
            "the parts really do add back to the number. It is the "
            "note-and-coin payment written as a sum.",
            "**Building runs it backwards.** Given $8\\,000 + 40 + 6$, "
            "fill the columns: $8$ thousands, $0$ hundreds (the guard "
            "returns), $4$ tens, $6$ ones — " + M(8046) + ". Parts in, "
            "number out.",
        ],
        "keyIdea": (
            "Each digit is worth digit times place: expanded form "
            "spells the worths out as a sum, and building from parts "
            "folds the sum back into a numeral — with zero guarding "
            "any missing part."),
        "facts": [
            {"title": "Worth = digit × place",
             "latex": th(n2) + ":\\ \\text{the } 3 \\text{ is worth } 3 \\times 1\\,000 = 3\\,000",
             "explanation": "Read the place before the digit — the column multiplies the digit."},
            {"title": "Expanded form",
             "latex": th(n2) + " = 3\\,000 + 400 + 80 + 2",
             "explanation": "One part per column; the parts add back to the number exactly."},
        ],
        "workedExamples": [
            {"id": "g4nu-l2-we1",
             "statement": "What is the $7$ worth in " + M(2745) + "? And in " + M(7245) + "?",
             "note": "Same digit, different column, different worth.",
             "solution": ("In " + M(2745) + " the $7$ stands in the hundreds: "
                          "worth $7 \\times 100 = 700$. In " + M(7245) + " it "
                          "stands in the thousands: worth $7 \\times 1\\,000 = "
                          "7\\,000$ — ten times as much, one column over."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7*100, 700)", "Eq(7*1000, 7000)"]},
            {"id": "g4nu-l2-we2",
             "statement": "Write " + M(3482) + " in expanded form.",
             "note": "One part per column.",
             "solution": ("$3$ thousands $= 3\\,000$, $4$ hundreds $= 400$, $8$ "
                          "tens $= 80$, $2$ ones $= 2$. So " + M(3482) +
                          " $= 3\\,000 + 400 + 80 + 2$ — and the parts add "
                          "straight back."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3000 + 400 + 80 + 2, 3482)", "Eq(3*1000, 3000)"]},
        ],
        "commonMistakes": [
            {"text": "Saying the 3 in 3 482 \"is worth 3\".",
             "correction": "The digit alone is 3, but its PLACE multiplies it: 3 × 1 000 = 3 000. Cover the other digits and read what remains: 3 000.",
             "authored": True},
            {"text": "Expanded form that invents a part — writing 4 052 as 4 000 + 500 + 2.",
             "correction": "The 5 stands in the TENS column: 4 052 = 4 000 + 50 + 2. Check by adding your parts back — 4 000 + 500 + 2 = 4 502, the wrong number.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4nu-l2-t1",
             "statement": "Write " + M(6913) + " in expanded form.",
             "solution": "$6\\,000 + 900 + 10 + 3$ — four parts, one per column, adding back to " + M(6913) + ".",
             "check": ["Eq(6000 + 900 + 10 + 3, 6913)"]},
            {"id": "g4nu-l2-t2",
             "statement": "What number is $8\\,000 + 40 + 6$?",
             "solution": "Thousands $8$, hundreds empty (guard!), tens $4$, ones $6$: " + M(8046) + ".",
             "check": ["Eq(8000 + 40 + 6, 8046)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "What each digit is worth", [
                "The place gives the digit its value: a digit is worth digit TIMES place. In " + M(n1) + " — pictured below as notes and coins — the $2$ is worth $2\\,000$, the $7$ is worth $700$, the $4$ is worth $40$, the $5$ just $5$.",
                "Move a digit one column left and its worth grows ten times: $7$ tens are $70$, $7$ hundreds are $700$, $7$ thousands are $7\\,000$.",
                "To hear a digit's worth, cover everything to its right with your finger and read what the column says.",
            ]), fig_cols),
            workedset("Digit worths",
                      "Read the place before the digit.", [
                wex("What is the $7$ worth in " + M(2745) + "? In " + M(7245) + "?",
                    ["Hundreds column: $7 \\times 100 = 700$.",
                     "Thousands column: $7 \\times 1\\,000 = 7\\,000$ — same digit, ten times the worth."],
                    "$700$, then $7\\,000$",
                    ["Eq(7*100, 700)", "Eq(7*1000, 7000)"]),
                wex("Write " + M(3482) + " in expanded form.",
                    ["Worths, column by column: $3\\,000$, $400$, $80$, $2$.",
                     "$" + th(3482) + " = 3\\,000 + 400 + 80 + 2$ — the parts add back exactly."],
                    "$3\\,000 + 400 + 80 + 2$",
                    ["Eq(3000 + 400 + 80 + 2, 3482)"]),
            ]),
            tryitset("Worth spotting", "Digit times place, every time.", [
                tp("In " + M(4915) + ", the $9$ is worth:",
                   ["$900$", "$9$", "$9\\,000$"],
                   "The $9$ stands in the hundreds: $9 \\times 100 = 900$. Answering $9$ ignores the place; $9\\,000$ moves it a column left.",
                   ["Eq(9*100, 900)"]),
                tp("In " + M(6208) + ", the $6$ is worth:",
                   ["$6\\,000$", "$600$", "$6$"],
                   "Leftmost of four columns is thousands: $6 \\times 1\\,000 = 6\\,000$.",
                   ["Eq(6*1000, 6000)"]),
                tp("The expanded form of " + M(5371) + " is:",
                   ["$5\\,000 + 300 + 70 + 1$",
                    "$5\\,000 + 300 + 7 + 1$",
                    "$500 + 300 + 70 + 1$"],
                   "The $7$ is seven TENS, worth $70$. Add each option back: only $5\\,000 + 300 + 70 + 1$ returns " + M(5371) + ".",
                   ["Eq(5000 + 300 + 70 + 1, 5371)"]),
            ]),
            tapq("Same digit, three worths", "In " + M(5505) + " the digit $5$ appears three times. Why are the three worth different amounts?",
                 ["the place gives each its value — $5\\,000$, $500$ and $5$",
                  "the first $5$ is written bigger",
                  "they are all worth the same $5$",
                  "the zero between them changes the fives"],
                 "Thousands, hundreds and ones columns: $5 \\times 1\\,000 = 5\\,000$, $5 \\times 100 = 500$, $5 \\times 1 = 5$. Together with the guard on tens duty: $5\\,000 + 500 + 5 = " + th(5505) + "$.",
                 ["Eq(5*1000, 5000)", "Eq(5000 + 500 + 5, 5505)"]),
            funfact("Ten symbols beat a whole alphabet",
                    "Place value is why you only ever need the ten digits $0$ to $9$: the same $7$ can mean seven, seventy or seven thousand depending on where it stands. Roman numerals had no places, so bigger numbers kept needing new letters — X for ten, C for a hundred, M for a thousand — and arithmetic with them was famously painful."),
            withfig(teach("Concept B", "Expanded form, there and back", [
                "Expanded form takes a number apart into its worths: " + M(n2) + " $= 3\\,000 + 400 + 80 + 2$. The number line below builds it part by part: jump $3\\,000$, then $400$ more to $3\\,400$, then $80$ to $3\\,480$ — three landings you can see. The last part is a single step of $2$ from $3\\,480$ onto " + M(n2) + ", far too small to draw beside a jump of $3\\,000$ — which is exactly what place value means.",
                "Building runs backwards: $8\\,000 + 40 + 6$ fills the columns as $8$, guard, $4$, $6$ — " + M(8046) + ". A missing part means a zero, never a shorter number.",
                "Always add your parts back. If they return a different number, a part sat in the wrong column.",
            ]), fig_build),
            workedset("Building from parts",
                      "Fill the columns; the guard covers missing parts.", [
                wex("What number is $8\\,000 + 40 + 6$?",
                    ["Thousands $8$, hundreds EMPTY, tens $4$, ones $6$.",
                     M(8046) + " — the zero holds the hundreds open."],
                    M(8046),
                    ["Eq(8000 + 40 + 6, 8046)"]),
                wex("Build the number with $7$ thousands, $0$ hundreds, $2$ tens and $9$ ones.",
                    ["Worths: $7\\,000 + 20 + 9$.",
                     M(7029) + "."],
                    M(7029),
                    ["Eq(7*1000 + 2*10 + 9, 7029)"]),
            ]),
            tryitset("Parts in, number out", "Add the parts; watch for guards.", [
                tp("$4\\,000 + 600 + 5$ equals:",
                   ["$4\\,605$", "$4\\,650$", "$4\\,065$"],
                   "No tens part, so a zero guards the tens: " + M(4605) + ". Choosing $4\\,650$ pushes the $5$ into the tens, making it $50$.",
                   ["Eq(4000 + 600 + 5, 4605)"]),
                tp("$2$ thousands, $3$ tens and $3$ ones make:",
                   ["$2\\,033$", "$2\\,330$", "$2\\,303$"],
                   "$2\\,000 + 30 + 3 = " + th(2033) + "$ — the hundreds column is empty, so its guard steps in.",
                   ["Eq(2*1000 + 3*10 + 3, 2033)"]),
                tp("Which sum builds " + M(6090) + "?",
                   ["$6\\,000 + 90$", "$6\\,000 + 900$", "$600 + 90$"],
                   "The $9$ stands in the tens: $6\\,000 + 90$. The trap $6\\,000 + 900$ builds " + M(6900) + " instead.",
                   ["Eq(6000 + 90, 6090)"]),
            ]),
            tapq("The silent column", "A number's expanded form is $9\\,000 + 300 + 8$. Its tens digit is:",
                 ["$0$", "$8$", "$3$", "$9$"],
                 "No tens part appears, so the tens column is empty and holds the guard: the number is " + M(9308) + ", tens digit $0$.",
                 ["Eq(9000 + 300 + 8, 9308)"]),
            recap([
                "A digit's worth is digit × place — read the place before the digit.",
                "One column left = worth ten times more.",
                "Expanded form: one part per column, and the parts must add back exactly.",
                "Building from parts: fill the columns; a missing part becomes a zero.",
                "Adding parts back is the receipt that catches wrong columns.",
            ]),
            tip("For each answer, add the parts back (or take the number apart) as a receipt — parts and number must agree before you move on."),
            tryitset("Mixed practice", "Worths, parts and receipts.", [
                tp("In " + M(4786) + ", the $4$ is worth:",
                   ["$4\\,000$", "$400$", "$4$"],
                   "Thousands column: $4 \\times 1\\,000 = 4\\,000$.",
                   ["Eq(4*1000, 4000)"]),
                tp("The expanded form of " + M(7604) + " is:",
                   ["$7\\,000 + 600 + 4$",
                    "$7\\,000 + 600 + 40$",
                    "$7\\,000 + 60 + 4$"],
                   "Zero guards the tens, so there is no tens part: $7\\,000 + 600 + 4$. Adding $40$ instead builds " + M(7640) + ".",
                   ["Eq(7000 + 600 + 4, 7604)"]),
                tp("$5\\,000 + 500 + 50 + 5$ equals:",
                   ["$5\\,555$", "$5\\,055$", "$5\\,505$"],
                   "Every column holds a $5$: " + M(5555) + " — four fives, four different worths.",
                   ["Eq(5000 + 500 + 50 + 5, 5555)"]),
                tp("Using each of the digit cards $1, 7, 4, 9$ once, the LARGEST number you can build is:",
                   ["$9\\,741$", "$9\\,714$", "$1\\,479$"],
                   "Big digits want big places: $9$ in thousands, then $7$, $4$, $1$ — " + M(9741) + ". Smallest would be " + M(1479) + ", the same cards reversed into small places.",
                   ["Eq(9*1000 + 7*100 + 4*10 + 1, 9741)", "9741 > 1479"]),
                tp("Paying " + M(3260) + " togrog with $1\\,000$ notes, $100$ notes and $10$ coins takes:",
                   ["$3$ notes, $2$ notes, $6$ coins",
                    "$3$ notes, $6$ notes, $2$ coins",
                    "$2$ notes, $3$ notes, $6$ coins"],
                   "Read the columns: $3$ thousands, $2$ hundreds, $6$ tens — $3 \\times 1\\,000 + 2 \\times 100 + 6 \\times 10 = " + th(3260) + "$ togrog.",
                   ["Eq(3*1000 + 2*100 + 6*10, 3260)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Place Value\"",
                    "Digit times place, taken apart and rebuilt — expanded form is the receipt behind every number. Next: putting numbers in ORDER, where the leftmost place speaks first and settles almost every argument.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Comparing & Ordering
# ==========================================================================

def lesson_comparing():
    a, n, b = 5600, 5642, 5700     # between-ness demo on the number line
    fig_between = fig_numline([(a, lab(a)), (n, lab(n), C_WARM), (b, lab(b))],
                              lo=a, hi=b)
    p, q, r = 3400, 3456, 3500     # tp figure: the GAP, not the answer
    # Only the two ends of the gap are marked. Plotting q here would print
    # the correct option on screen beside the options themselves — the line
    # gives the student somewhere to place each candidate, nothing more.
    fig_tp = fig_numline([(p, lab(p), C_GREEN), (r, lab(r), C_GREEN)],
                         lo=p, hi=r)
    # Concept A: the leftmost place decides — 3 025 against 2 970, column by
    # column, in the topic's fixed place-to-colour mapping.
    fig_compare = fig_groups((3, "thousands in 3 025"), (0, "hundreds in 3 025"),
                             (2, "tens in 3 025"), (5, "ones in 3 025"),
                             (2, "thousands in 2 970"), (9, "hundreds in 2 970"),
                             (7, "tens in 2 970"), (0, "ones in 2 970"))
    return {
        "slug": "comparing-and-ordering",
        "title": "Comparing & Ordering",
        "concreteComparison": (
            "Two herds meet at the well: one of " + M(3025) + " animals, "
            "one of " + M(2970) + ". The second has showier digits — "
            "$970$ looks grander than $25$ — but three THOUSANDS beat "
            "two thousands before the small columns even get to speak. "
            "Comparing numbers is a conversation where the leftmost "
            "place talks first, and the rest only matter if it ties."),
        "objective": (
            "Compare four-digit numbers place by place from the left, "
            "order sets of three or four numbers, and place a number "
            "between its neighbouring hundreds on the number line."),
        "concept": [
            "**More digits wins outright.** A four-digit number always "
            "beats a three-digit one: " + M(1023) + " $> 987$, because "
            "$987$ never even reaches $1\\,000$. Count digits before "
            "comparing them.",
            "**Same length: leftmost place speaks first.** Compare "
            "thousands, then hundreds, then tens, then ones — and the "
            "FIRST difference settles it. " + M(3025) + " $>$ " + M(2970) +
            " because $3 > 2$ in the thousands; the $970$ never gets a "
            "vote.",
            "**Every number lives between two hundreds.** " + M(n) +
            " sits between " + M(a) + " and " + M(b) + " on the number "
            "line — $42$ steps past " + M(a) + ", $58$ short of " + M(b) +
            ". Placing a number between its neighbours is how ordering "
            "becomes a picture.",
        ],
        "keyIdea": (
            "Count digits first, then compare place by place from the "
            "left — the first difference decides. On the number line, "
            "bigger simply means further right."),
        "facts": [
            {"title": "Leftmost place speaks first",
             "latex": th(3025) + " > " + th(2970) + "\\ \\ (3\\ \\text{thousands beat}\\ 2)",
             "explanation": "The first column that differs settles it; later columns cannot overturn it."},
            {"title": "Between the hundreds",
             "latex": th(a) + " < " + th(n) + " < " + th(b),
             "explanation": "Every four-digit number sits between two neighbouring hundreds on the line."},
        ],
        "workedExamples": [
            {"id": "g4nu-l3-we1",
             "statement": "Which herd is larger: " + M(3025) + " animals or " + M(2970) + "?",
             "note": "Thousands first — the flashy hundreds never vote.",
             "solution": ("Both have four digits, so compare thousands: $3 > 2$, "
                          "done — " + M(3025) + " $>$ " + M(2970) + ". Even the "
                          "smaller herd's whole $2\\,970$ stays below the bigger "
                          "herd's $3\\,000$ of thousands alone."),
             "badges": [{"text": "core"}],
             "check": ["3025 > 2970", "3000 > 2970"]},
            {"id": "g4nu-l3-we2",
             "statement": "Order from smallest to largest: " + M(5470) + ", " + M(5461) + ", " + M(5504) + ".",
             "note": "Walk the columns left to right until they differ.",
             "solution": ("All share $5$ thousands. Hundreds: $4, 4, 5$ — so " +
                          M(5504) + " is largest. Between the two with $4$ "
                          "hundreds, tens decide: $6 < 7$, so " + M(5461) +
                          " $<$ " + M(5470) + ". Order: " + M(5461) + " $<$ " +
                          M(5470) + " $<$ " + M(5504) + "."),
             "badges": [{"text": "core"}],
             "check": ["5461 < 5470", "5470 < 5504"]},
        ],
        "commonMistakes": [
            {"text": "Letting a flashy small column decide — 2 895 > 3 014 \"because 8 beats 0\".",
             "correction": "The hundreds only speak if the thousands TIE. 3 > 2 in the thousands ends the contest: 3 014 is bigger, whatever the later digits.",
             "authored": True},
            {"text": "Comparing first digits across different lengths — 987 > 1 023 \"because 9 beats 1\".",
             "correction": "Count digits first. Four columns beat three: 987 is below 1 000 and 1 023 is above it, so 1 023 > 987.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4nu-l3-t1",
             "statement": "Compare " + M(6384) + " and " + M(6348) + " with $<$, $>$ or $=$.",
             "solution": "Thousands tie, hundreds tie; tens: $8 > 4$ — so " + M(6384) + " $>$ " + M(6348) + ". The difference is $36$: $" + th(6348) + " + 36 = " + th(6384) + "$.",
             "check": ["6384 > 6348", "Eq(6348 + 36, 6384)"]},
            {"id": "g4nu-l3-t2",
             "statement": "What number sits exactly halfway between " + M(4200) + " and " + M(4300) + "?",
             "solution": M(4250) + " — it is $50$ past " + M(4200) + " and $50$ short of " + M(4300) + ".",
             "check": ["Eq(4250 - 4200, 50)", "Eq(4300 - 4250, 50)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The leftmost place speaks first", [
                "Count digits before anything else: a four-digit number beats a three-digit one every time — $987 < 1\\,023$, because $987$ never reaches $1\\,000$.",
                "Same length? Compare column by column from the LEFT: thousands, hundreds, tens, ones. The first difference settles it — " + M(3025) + " beats " + M(2970) + " because $3 > 2$ in the thousands. The picture below stacks the two numbers column by column: " + M(2970) + " has the showier hundreds and tens, and still loses on the very first column.",
                "The place gives the digit its value — that is exactly why the left column outvotes everything: one step of a thousand is more than the other three columns can hold together.",
            ]), fig_compare),
            workedset("First difference wins",
                      "Digits counted, then columns walked from the left.", [
                wex("Compare " + M(3025) + " and " + M(2970) + ".",
                    ["Both four digits. Thousands: $3 > 2$ — decided.",
                     M(3025) + " $>$ " + M(2970) + "; even $3\\,000$ alone beats all of " + M(2970) + "."],
                    M(3025) + " $>$ " + M(2970),
                    ["3025 > 2970", "3000 > 2970"]),
                wex("Compare $987$ and " + M(1023) + ".",
                    ["Three digits against four: no contest.",
                     "$987 < 1\\,000$ and $" + th(1023) + " > 1\\,000$, so $987 < " + th(1023) + "$."],
                    "$987 <$ " + M(1023),
                    ["987 < 1000", "1023 > 987"]),
            ]),
            tryitset("Column court", "First difference from the left decides.", [
                tp("Which symbol fits: " + M(7216) + " $\\;\\square\\;$ " + M(7261) + "?",
                   ["$<$", "$>$", "$=$"],
                   "Thousands and hundreds tie; tens: $1 < 6$ — so $<$. The swapped last digits try to distract; the tens speak before the ones.",
                   ["7216 < 7261"]),
                tp("The largest of " + M(4989) + ", " + M(5001) + ", " + M(4998) + " is:",
                   ["$5\\,001$", "$4\\,998$", "$4\\,989$"],
                   "Thousands first: $5$ beats $4$, so " + M(5001) + " wins despite its tiny-looking $001$ tail.",
                   ["5001 > 4998", "4998 > 4989"]),
                tp("Which symbol fits: $999 \\;\\square\\; " + th(1001) + "$?",
                   ["$<$", "$>$", "$=$"],
                   "Three digits against four: $999$ is the LAST three-digit number and still loses — $999 + 2 = " + th(1001) + "$.",
                   ["999 < 1001"]),
            ]),
            tapq("Flashy digits do not vote", "A student says " + M(2895) + " $>$ " + M(3014) + " \"because $8$ beats $0$\". The truth:",
                 ["thousands speak first: $3 > 2$, so " + M(3014) + " is bigger",
                  "the student is right — hundreds count more",
                  "the numbers are equal",
                  "you cannot compare them"],
                 "Hundreds only get a vote when thousands TIE. Here $3\\,000$ alone already beats the whole of " + M(2895) + " — the later columns cannot catch up.",
                 ["3014 > 2895", "3000 > 2895"]),
            funfact("Why the later columns cannot rebel",
                    "Once the thousands differ, the contest is truly over: the hundreds, tens and ones together can only ever add up to $999$ — one whole step of a thousand is bigger, since $999 < 1\\,000$. The leftmost place is not just first, it is unbeatable."),
            withfig(teach("Concept B", "Ordering, and the number line", [
                "To order three or four numbers, run the same contest repeatedly: find the smallest, then the next — " + M(5461) + " $<$ " + M(5470) + " $<$ " + M(5504) + ".",
                "Every number lives BETWEEN two neighbouring hundreds. On the line below, " + M(n) + " sits between " + M(a) + " and " + M(b) + ": it is $42$ past " + M(a) + " and $58$ short of " + M(b) + ".",
                "On the number line, bigger simply means further right — ordering numbers is placing them on the line and reading left to right.",
            ]), fig_between),
            workedset("Between the neighbours",
                      "Find the hundreds on each side; measure both gaps.", [
                wex("Which hundreds does " + M(n) + " sit between, and how far from each?",
                    ["Neighbouring hundreds: " + M(a) + " and " + M(b) + ".",
                     "Gaps: $" + th(n) + " - " + th(a) + " = 42$ and $" + th(b) + " - " + th(n) + " = 58$."],
                    M(a) + " and " + M(b),
                    ["Eq(5642 - 5600, 42)", "Eq(5700 - 5642, 58)"]),
                wex("Order " + M(5470) + ", " + M(5461) + ", " + M(5504) + " from smallest to largest.",
                    ["Thousands tie; hundreds put " + M(5504) + " on top.",
                     "Tens split the rest: " + M(5461) + " $<$ " + M(5470) + " $<$ " + M(5504) + "."],
                    M(5461) + " $<$ " + M(5470) + " $<$ " + M(5504),
                    ["5461 < 5470", "5470 < 5504"]),
            ]),
            tryitset("On the line", "Between-ness is a picture — read it left to right.", [
                withfig(tp("The line below shows the gap from " + M(p) + " to " + M(r) + ". Which number lands inside it?",
                   ["$3\\,456$", "$3\\,390$", "$3\\,540$"],
                   "Only " + M(q) + " lands inside the gap: $" + th(p) + " < " + th(q) + " < " + th(r) + "$. The others fall outside — $3\\,390$ is below " + M(p) + " and $3\\,540$ beyond " + M(r) + ".",
                   ["3400 < 3456", "3456 < 3500"]), fig_tp),
                tp("Ordered smallest to largest, " + M(4098) + ", " + M(4089) + ", " + M(4908) + " become:",
                   ["$4\\,089 < 4\\,098 < 4\\,908$",
                    "$4\\,908 < 4\\,098 < 4\\,089$",
                    "$4\\,098 < 4\\,089 < 4\\,908$"],
                   "Hundreds first: the $9$-hundreds number " + M(4908) + " is largest. Then tens: $8 < 9$ puts " + M(4089) + " before " + M(4098) + ".",
                   ["4089 < 4098", "4098 < 4908"]),
                tp("Exactly halfway between " + M(6000) + " and " + M(7000) + " sits:",
                   ["$6\\,500$", "$6\\,050$", "$6\\,750$"],
                   "Half of the thousand-wide gap is $500$: $" + th(6000) + " + 500 = " + th(6500) + "$, and $500$ more reaches " + M(7000) + ".",
                   ["Eq(6500 - 6000, 500)", "Eq(7000 - 6500, 500)"]),
            ]),
            tapq("Herds in order", "A family counts " + M(2041) + " sheep, " + M(1998) + " goats and " + M(1899) + " horses. From largest herd to smallest:",
                 ["sheep, goats, horses", "goats, sheep, horses",
                  "horses, goats, sheep", "sheep, horses, goats"],
                 "Sheep clear $2\\,000$; the others stay below it. Between goats and horses the hundreds decide: $9 > 8$, so goats beat horses.",
                 ["2041 > 1998", "1998 > 1899"]),
            recap([
                "Count digits first: four columns beat three, always.",
                "Same length: compare place by place from the LEFT — first difference decides.",
                "Later columns cannot overturn an earlier difference: they top out at 999.",
                "Every number sits between two neighbouring hundreds; measure both gaps.",
                "On the number line, bigger means further right.",
            ]),
            tip("Before each comparison, say which column will speak first — then let it. Ordering is just comparing, repeated."),
            tryitset("Mixed practice", "Contests, orders, and the line.", [
                tp("Which symbol fits: " + M(8514) + " $\\;\\square\\;$ " + M(8541) + "?",
                   ["$<$", "$>$", "$=$"],
                   "Tens speak first here: $1 < 4$, so $<$. The gap is $27$: $" + th(8514) + " + 27 = " + th(8541) + "$.",
                   ["8514 < 8541", "Eq(8514 + 27, 8541)"]),
                tp("The largest of " + M(9090) + ", " + M(9009) + ", " + M(9900) + " is:",
                   ["$9\\,900$", "$9\\,090$", "$9\\,009$"],
                   "Thousands all tie at $9$ — the hundreds decide: $9 > 0$, so " + M(9900) + " leads. The zeros sit in different columns in each number.",
                   ["9900 > 9090", "9090 > 9009"]),
                tp("Which number lies between " + M(7800) + " and " + M(7900) + "?",
                   ["$7\\,856$", "$7\\,908$", "$7\\,790$"],
                   "$" + th(7800) + " < " + th(7856) + " < " + th(7900) + "$. The others miss the gap: $7\\,908$ overshoots, $7\\,790$ falls short.",
                   ["7800 < 7856", "7856 < 7900"]),
                tp("Three Naadam riders cover " + M(4320) + " m, " + M(4230) + " m and " + M(4302) + " m. Ordered shortest ride to longest:",
                   ["$4\\,230 < 4\\,302 < 4\\,320$",
                    "$4\\,230 < 4\\,320 < 4\\,302$",
                    "$4\\,302 < 4\\,230 < 4\\,320$"],
                   "Hundreds first: $2 < 3$ makes " + M(4230) + " shortest. Then tens: $0 < 2$ puts " + M(4302) + " before " + M(4320) + ".",
                   ["4230 < 4302", "4302 < 4320"]),
                tp("Which statement is TRUE?",
                   ["$1\\,000 > 999$", "$999 > 1\\,000$", "$999 = 1\\,000$"],
                   "The first four-digit number beats the last three-digit one by exactly $1$: $999 + 1 = 1\\,000$. Digit count before digit size.",
                   ["1000 > 999", "Eq(999 + 1, 1000)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Comparing & Ordering\"",
                    "Digit count, then the leftmost difference — and the number line to see it all at once. Next: ROUNDING, where the two neighbouring tens or hundreds you just learned to find become the only two answers allowed.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Rounding
# ==========================================================================

def lesson_rounding():
    # nearest-10 star: 3482 between 3480 and 3490
    n10, lo10, hi10 = 3482, 3480, 3490
    fig_n10 = fig_numline([(lo10, lab(lo10)), (n10, lab(n10), C_WARM),
                           (hi10, lab(hi10))], lo=lo10, hi=hi10)
    # nearest-100 worked example: 7258 between 7200 and 7300
    n100, lo100, hi100 = 7258, 7200, 7300
    fig_n100 = fig_numline([(lo100, lab(lo100)), (n100, lab(n100), C_WARM),
                            (hi100, lab(hi100))], lo=lo100, hi=hi100)
    # tp figure: 8361 between 8300 and 8400
    t, tlo, thi = 8361, 8300, 8400
    fig_tp = fig_numline([(tlo, lab(tlo)), (t, lab(t), C_GREEN),
                          (thi, lab(thi))], lo=tlo, hi=thi)
    # halfway demo: 645 dead centre of 640 and 650
    h, hlo, hhi = 645, 640, 650
    fig_half = fig_numline([(hlo, lab(hlo)), (h, lab(h), C_WARM),
                            (hhi, lab(hhi))], lo=hlo, hi=hhi)
    return {
        "slug": "rounding",
        "title": "Rounding",
        "concreteComparison": (
            "The Naadam stadium counted " + M(4872) + " visitors — but "
            "you tell your friend \"about $4\\,900$\". Rounding trades "
            "an exact number for a nearby round one that the mouth and "
            "the mind can carry. The whole skill is finding a number's "
            "two round NEIGHBOURS on the number line and moving to the "
            "closer one."),
        "objective": (
            "Round four-digit numbers to the nearest 10 and nearest "
            "100 by comparing the two neighbours on the number line, "
            "apply the halfway-rounds-up rule, and use rounding to "
            "estimate sums."),
        "concept": [
            "**Every number has two round neighbours.** To the nearest "
            "$10$, " + M(n10) + " sits between " + M(lo10) + " and " +
            M(hi10) + ". Measure both gaps — $2$ back, $8$ forward — "
            "and move to the closer neighbour: " + M(lo10) + ".",
            "**The place you round to picks the neighbours.** Nearest "
            "$10$: neighbours are tens. Nearest $100$: neighbours are "
            "hundreds — " + M(n100) + " sits between " + M(lo100) +
            " and " + M(hi100) + ", gaps $58$ and $42$, so it rounds "
            "to " + M(hi100) + ". Same number, different question, "
            "different answer.",
            "**Halfway rounds up.** " + M(h) + " is exactly $5$ from "
            "both " + M(hlo) + " and " + M(hhi) + " — no closer "
            "neighbour exists, so the rule steps in: exactly halfway "
            "goes UP, to " + M(hhi) + ".",
        ],
        "keyIdea": (
            "Rounding is a two-neighbour contest on the number line: "
            "find the round number on each side, measure both gaps, "
            "move to the closer one — and when the gaps tie, go up."),
        "facts": [
            {"title": "The two neighbours",
             "latex": th(lo10) + " \\;\\leftarrow\\; " + th(n10) + " \\;\\rightarrow\\; " + th(hi10),
             "explanation": "Gaps of 2 and 8 — the closer neighbour wins, so 3 482 rounds to 3 480."},
            {"title": "The halfway rule",
             "latex": "645 \\to 650 \\qquad 450 \\to 500",
             "explanation": "Equal gaps on both sides: the rule sends halfway numbers UP."},
        ],
        "workedExamples": [
            {"id": "g4nu-l4-we1",
             "statement": "Round " + M(n10) + " to the nearest $10$.",
             "note": "Find both neighbours; measure both gaps.",
             "solution": ("Neighbouring tens: " + M(lo10) + " and " + M(hi10) +
                          ". Gaps: $" + th(n10) + " - " + th(lo10) + " = 2$ back, "
                          "$" + th(hi10) + " - " + th(n10) + " = 8$ forward. "
                          "The gap of $2$ wins: " + M(n10) + " rounds to " +
                          M(lo10) + "."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3482 - 3480, 2)", "Eq(3490 - 3482, 8)",
                       near(3482, 3480, 3490)]},
            {"id": "g4nu-l4-we2",
             "statement": "Round " + M(n100) + " to the nearest $100$.",
             "note": "Nearest hundred means the neighbours are hundreds.",
             "solution": ("Neighbouring hundreds: " + M(lo100) + " and " + M(hi100) +
                          ". Gaps: $58$ back, $42$ forward — the forward gap is "
                          "smaller, so " + M(n100) + " rounds UP to " + M(hi100) +
                          "."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7258 - 7200, 58)", "Eq(7300 - 7258, 42)",
                       near(7258, 7300, 7200)]},
        ],
        "commonMistakes": [
            {"text": "Rounding to the wrong place — asked for the nearest 10, answering 3 500 for 3 482.",
             "correction": "Nearest TEN means the neighbours are tens: 3 480 and 3 490. Say which place the question names before hunting neighbours.",
             "authored": True},
            {"text": "Sending halfway numbers down — rounding 645 to 640.",
             "correction": "645 is exactly 5 from both neighbours; no side is closer. The agreed rule breaks the tie UPWARD: 645 rounds to 650.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4nu-l4-t1",
             "statement": "Round " + M(6237) + " to the nearest $10$.",
             "solution": "Neighbours " + M(6230) + " and " + M(6240) + "; gaps $7$ and $3$. Closer neighbour: " + M(6240) + ".",
             "check": ["Eq(6237 - 6230, 7)", "Eq(6240 - 6237, 3)",
                       near(6237, 6240, 6230)]},
            {"id": "g4nu-l4-t2",
             "statement": "Round " + M(1650) + " to the nearest $100$.",
             "solution": "Neighbours " + M(1600) + " and " + M(1700) + "; gaps $50$ and $50$ — exactly halfway, so the rule sends it UP: " + M(1700) + ".",
             "check": ["Eq(1650 - 1600, 50)", "Eq(1700 - 1650, 50)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The two-neighbour contest", [
                "Rounding to the nearest $10$: find the ten on each side. On the line below, " + M(n10) + " stands between " + M(lo10) + " and " + M(hi10) + " — $2$ steps past one, $8$ short of the other.",
                "The closer neighbour wins: " + M(n10) + " rounds to " + M(lo10) + ". Never guess from the digits alone — MEASURE both gaps.",
                "Nearest $100$ plays the same game with hundred-neighbours: the place named in the question picks which neighbours compete. The place gives the digit its value — and the question names the place.",
            ]), fig_n10),
            workedset("Neighbours and gaps",
                      "Name the place, find both neighbours, measure both gaps.", [
                wex("Round " + M(n10) + " to the nearest $10$.",
                    ["Neighbours: " + M(lo10) + " and " + M(hi10) + "; gaps $2$ and $8$.",
                     "Closer wins: " + M(lo10) + "."],
                    M(lo10),
                    ["Eq(3482 - 3480, 2)", "Eq(3490 - 3482, 8)",
                     near(3482, 3480, 3490)]),
                withfig(wex("Round " + M(n100) + " to the nearest $100$.",
                    ["Hundred-neighbours: " + M(lo100) + " and " + M(hi100) + "; gaps $58$ and $42$.",
                     "The forward gap is smaller — up to " + M(hi100) + "."],
                    M(hi100),
                    ["Eq(7258 - 7200, 58)", "Eq(7300 - 7258, 42)",
                     near(7258, 7300, 7200)]), fig_n100),
            ]),
            tryitset("Closer neighbour wins", "Measure both gaps before deciding.", [
                tp("Rounded to the nearest $10$, " + M(5623) + " becomes:",
                   ["$5\\,620$", "$5\\,630$", "$5\\,600$"],
                   "Neighbours " + M(5620) + " and " + M(5630) + ": gaps $3$ and $7$, so " + M(5620) + ". Answering $5\\,600$ rounds to the wrong place — that is the nearest hundred.",
                   ["Eq(5623 - 5620, 3)", near(5623, 5620, 5630)]),
                tp("Rounded to the nearest $100$, " + M(2380) + " becomes:",
                   ["$2\\,400$", "$2\\,300$", "$2\\,380$"],
                   "Hundred-neighbours " + M(2300) + " and " + M(2400) + ": gaps $80$ and $20$. The $20$ wins — up to " + M(2400) + ".",
                   ["Eq(2400 - 2380, 20)", near(2380, 2400, 2300)]),
                withfig(tp("The line shows " + M(t) + " between its hundred-neighbours. To the nearest $100$ it rounds to:",
                   ["$8\\,400$", "$8\\,300$", "$8\\,360$"],
                   "Gaps: $61$ back to " + M(tlo) + ", $39$ forward to " + M(thi) + " — forward is closer. ($8\\,360$ answers a nearest-ten question instead.)",
                   ["Eq(8361 - 8300, 61)", "Eq(8400 - 8361, 39)",
                    near(8361, 8400, 8300)]), fig_tp),
            ]),
            tapq("Just under the middle", "Rounded to the nearest $100$, " + M(4049) + " becomes:",
                 ["$4\\,000$", "$4\\,100$", "$4\\,050$", "$4\\,049$"],
                 "Neighbours " + M(4000) + " and " + M(4100) + ": gaps $49$ and $51$. One short of halfway — the smaller gap points down to " + M(4000) + ". ($4\\,050$ rounds to the nearest ten, a different question.)",
                 ["Eq(4049 - 4000, 49)", "Eq(4100 - 4049, 51)",
                  near(4049, 4000, 4100)]),
            funfact("Rounding never wanders far",
                    "A rounded number can never drift more than HALF a step from the truth: to the nearest $10$ at most $5$ away, to the nearest $100$ at most $50$. That guarantee is what makes estimates trustworthy — the error is fenced in before you even start."),
            withfig(teach("Concept B", "Halfway up, then estimate", [
                "Sometimes the contest ties: " + M(h) + " is exactly $5$ from " + M(hlo) + " and $5$ from " + M(hhi) + " — the line below shows it dead centre. The agreed rule: exactly halfway rounds UP, so " + M(h) + " goes to " + M(hhi) + ".",
                "The same rule at hundreds: $450$ sits $50$ from $400$ and $50$ from $500$ — up to $500$.",
                "Rounding earns its keep in ESTIMATES: to check $2\\,387 + 4\\,615$, round both to hundreds — $2\\,400 + 4\\,600 = 7\\,000$. The exact sum, $7\\,002$, lands right beside it: the estimate backs up the answer.",
            ]), fig_half),
            workedset("Ties and estimates",
                      "Halfway goes up; rounded sums forecast exact ones.", [
                wex("Round " + M(h) + " to the nearest $10$.",
                    ["Gaps: $5$ to " + M(hlo) + " and $5$ to " + M(hhi) + " — a tie.",
                     "Halfway rounds UP: " + M(hhi) + "."],
                    M(hhi),
                    ["Eq(645 - 640, 5)", "Eq(650 - 645, 5)"]),
                wex("Estimate $" + th(2387) + " + " + th(4615) + "$ by rounding each to the nearest $100$, then compare with the exact sum.",
                    ["Round: $2\\,400 + 4\\,600 = 7\\,000$.",
                     "Exact: $" + th(2387) + " + " + th(4615) + " = " + th(7002) + "$ — just $2$ from the estimate."],
                    "estimate $7\\,000$; exact $7\\,002$",
                    [near(2387, 2400, 2300), near(4615, 4600, 4700),
                     "Eq(2400 + 4600, 7000)", "Eq(2387 + 4615, 7002)"]),
            ]),
            tryitset("Halfway and beyond", "Ties go up; estimates go first.", [
                tp("Rounded to the nearest $100$, $750$ becomes:",
                   ["$800$", "$700$", "$750$"],
                   "Gaps: $50$ to $700$ and $50$ to $800$ — exactly halfway, and halfway rounds UP: $800$.",
                   ["Eq(750 - 700, 50)", "Eq(800 - 750, 50)"]),
                tp("Rounding to the nearest $100$, the estimate for $" + th(3190) + " + " + th(2807) + "$ is:",
                   ["$3\\,200 + 2\\,800 = 6\\,000$",
                    "$3\\,100 + 2\\,800 = 5\\,900$",
                    "$3\\,200 + 2\\,900 = 6\\,100$"],
                   "Round each number to its own closer neighbour: " + M(3190) + " is $10$ from $3\\,200$, and " + M(2807) + " is $7$ from $2\\,800$. The exact sum $" + th(5997) + "$ sits $3$ below the estimate. The wrong options round one number the far way and land $100$ off.",
                   [near(3190, 3200, 3100), near(2807, 2800, 2900),
                    "Eq(3200 + 2800, 6000)", "Eq(3190 + 2807, 5997)",
                    "Eq(3100 + 2800, 5900)", "Eq(3200 + 2900, 6100)",
                    "Ne(5900, 6000)", "Ne(6100, 6000)"]),
                tp("Rounded to the nearest $100$, " + M(9950) + " becomes:",
                   ["$10\\,000$", "$9\\,900$", "$9\\,950$"],
                   "Gaps: $50$ to " + M(9900) + " and $50$ to " + M(10000) + " — halfway rounds UP, straight to the fifth-column number itself.",
                   ["Eq(9950 - 9900, 50)", "Eq(10000 - 9950, 50)"]),
            ]),
            tapq("The estimate as a check", "To check $" + th(4512) + " + " + th(3498) + "$, a student estimates $4\\,500 + 3\\,500 = 8\\,000$. The exact sum is $" + th(8010) + "$. The estimate is:",
                 ["$10$ under — close enough to back up the exact answer",
                  "exactly right",
                  "$100$ under — the addition must be wrong",
                  "useless, because it is not exact"],
                 "Each rounding moved at most $50$, so estimate and truth must land near each other: $" + th(8010) + " - 8\\,000 = 10$. An estimate is a check, not a replacement.",
                 [near(4512, 4500, 4600), near(3498, 3500, 3400),
                  "Eq(4500 + 3500, 8000)", "Eq(4512 + 3498, 8010)",
                  "Eq(8010 - 8000, 10)"]),
            recap([
                "Rounding is a two-neighbour contest: find both, measure both gaps, move to the closer.",
                "The question names the place, and the place picks the neighbours — ten-neighbours or hundred-neighbours.",
                "Exactly halfway (gap 5, or gap 50) rounds UP.",
                "Nearest 10 stays within 5 of the truth; nearest 100 within 50.",
                "Round-then-add gives an estimate that backs up the exact sum.",
            ]),
            tip("For every rounding below, write BOTH neighbours and both gaps before answering — the wrong-place trap cannot survive that habit."),
            tryitset("Mixed practice", "Neighbours, ties, and estimates.", [
                tp("Rounded to the nearest $10$, " + M(2764) + " becomes:",
                   ["$2\\,760$", "$2\\,770$", "$2\\,800$"],
                   "Neighbours " + M(2760) + " and " + M(2770) + ": gaps $4$ and $6$ — down to " + M(2760) + ". ($2\\,800$ answers the nearest-hundred question.)",
                   ["Eq(2764 - 2760, 4)", near(2764, 2760, 2770)]),
                tp("Rounded to the nearest $100$, " + M(6149) + " becomes:",
                   ["$6\\,100$", "$6\\,200$", "$6\\,150$"],
                   "Gaps: $49$ back to " + M(6100) + ", $51$ forward to " + M(6200) + " — one short of halfway, so DOWN.",
                   ["Eq(6149 - 6100, 49)", "Eq(6200 - 6149, 51)",
                    near(6149, 6100, 6200)]),
                tp("Rounded to the nearest $10$, $985$ becomes:",
                   ["$990$", "$980$", "$1\\,000$"],
                   "Gaps: $5$ and $5$ — halfway rounds UP to $990$. ($1\\,000$ would answer a nearest-hundred question.)",
                   ["Eq(985 - 980, 5)", "Eq(990 - 985, 5)"]),
                tp("Rounded to the nearest $100$, " + M(1450) + " becomes:",
                   ["$1\\,500$", "$1\\,400$", "$1\\,450$"],
                   "Halfway between " + M(1400) + " and " + M(1500) + " — gaps of $50$ each — and halfway goes UP.",
                   ["Eq(1450 - 1400, 50)", "Eq(1500 - 1450, 50)"]),
                tp("A shop sells " + M(2480) + " tickets in June and " + M(1520) + " in July. Rounding each to the nearest $100$, the estimated total is:",
                   ["$2\\,500 + 1\\,500 = 4\\,000$ — and the exact total is $4\\,000$ too",
                    "$2\\,400 + 1\\,500 = 3\\,900$",
                    "$2\\,500 + 1\\,600 = 4\\,100$"],
                   "Each number is $20$ from its closer neighbour, in opposite directions — the errors cancel and the estimate lands exactly: $" + th(2480) + " + " + th(1520) + " = " + th(4000) + "$. The wrong options send one number to its FAR neighbour ($" + th(2480) + "$ down to $2\\,400$, or $" + th(1520) + "$ up to $1\\,600$) and miss by $100$.",
                   [near(2480, 2500, 2400), near(1520, 1500, 1600),
                    "Eq(2500 + 1500, 4000)", "Eq(2480 + 1520, 4000)",
                    "Eq(2400 + 1500, 3900)", "Eq(2500 + 1600, 4100)",
                    "Eq(4000 - 3900, 100)", "Eq(4100 - 4000, 100)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Rounding\"",
                    "Two neighbours, a measured gap, and a tie-breaking rule — plus estimates that check your arithmetic. Last stop: number PATTERNS, where the same step repeats and the ones digit tells secrets.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Number Patterns
# ==========================================================================

def lesson_patterns():
    # skip-counting star: 4200, 4250, 4300, then 4350, 4400 (step 50)
    s0, s1, s2, s3, s4 = 4200, 4250, 4300, 4350, 4400
    fig_skip = fig_numline([(s0, lab(s0)), (s1, lab(s1)), (s2, lab(s2)),
                            (s3, lab(s3), C_WARM), (s4, lab(s4), C_WARM)],
                           lo=s0, hi=s4)
    # even split: 8 children into two equal teams of 4
    fig_teams = fig_groups((4, "team A"), (4, "team B", C_GREEN))
    return {
        "slug": "number-patterns",
        "title": "Number Patterns",
        "concreteComparison": (
            "Counting togrog notes into a tin — $100$, $200$, $300$ — "
            "your hand finds the rhythm before your head does. A "
            "number pattern is exactly that rhythm written down: the "
            "SAME step, taken again and again. Name the step and you "
            "own the pattern — you can continue it as far as you "
            "like."),
        "objective": (
            "Skip count by 25s, 50s and 100s, find a pattern's step by "
            "subtracting neighbours, continue and describe patterns, "
            "and tell odd from even using the ones digit."),
        "concept": [
            "**A pattern's step is found by subtracting.** In $" +
            th(s0) + ", " + th(s1) + ", " + th(s2) + "$ the step is $" +
            th(s1) + " - " + th(s0) + " = 50$ — and every neighbouring "
            "pair must agree. To continue, keep adding the step: $" +
            th(s3) + ", " + th(s4) + "$.",
            "**The favourite steps are 25, 50 and 100.** They fit "
            "hundreds perfectly: four 25s or two 50s make $100$, so "
            "these counts land on round numbers again and again — "
            "$925, 950, 975, 1\\,000$.",
            "**Odd or even lives in the ones digit.** A number is EVEN "
            "if it splits into two equal teams, and only the ones "
            "digit decides: every ten, hundred and thousand already "
            "splits evenly, so the leftover ones digit settles it — " +
            M(3482) + " ends in $2$: even. " + M(4507) + " ends in "
            "$7$: odd.",
        ],
        "keyIdea": (
            "Subtract neighbours to name the step, then add it to "
            "continue — and for odd or even, ask only the ones digit: "
            "all the bigger places split evenly by themselves."),
        "facts": [
            {"title": "Name the step",
             "latex": th(s0) + ",\\ " + th(s1) + ",\\ " + th(s2) + "\\ \\ (+50\\ \\text{each time})",
             "explanation": "Subtract any neighbouring pair; every pair must give the same step."},
            {"title": "The ones digit decides",
             "latex": th(3482) + " \\to 2:\\ \\text{even} \\qquad " + th(4507) + " \\to 7:\\ \\text{odd}",
             "explanation": "Tens, hundreds and thousands split into pairs by themselves — only the ones digit can leave one out."},
        ],
        "workedExamples": [
            {"id": "g4nu-l5-we1",
             "statement": "Continue the pattern with two more numbers, and name its step: $" + th(s0) + ", " + th(s1) + ", " + th(s2) + "$.",
             "note": "Subtract neighbours first — never guess the step.",
             "solution": ("Step: $" + th(s1) + " - " + th(s0) + " = 50$, and $" +
                          th(s2) + " - " + th(s1) + " = 50$ agrees. Keep adding: $" +
                          th(s2) + " + 50 = " + th(s3) + "$, then $" + th(s3) +
                          " + 50 = " + th(s4) + "$. The pattern counts by $50$s."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4250 - 4200, 50)", "Eq(4300 - 4250, 50)",
                       "Eq(4300 + 50, 4350)", "Eq(4350 + 50, 4400)"]},
            {"id": "g4nu-l5-we2",
             "statement": "Is " + M(3482) + " odd or even? And " + M(4507) + "?",
             "note": "Ask only the ones digit.",
             "solution": (M(3482) + " ends in $2$ — even: it splits into two "
                          "equal teams with nobody left over. " + M(4507) +
                          " ends in $7$ — odd: pairing always leaves one out. "
                          "The big columns never matter; they split evenly by "
                          "themselves."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Mod(3482, 2), 0)", "Eq(Mod(4507, 2), 1)"]},
        ],
        "commonMistakes": [
            {"text": "Guessing the step from the loudest changing digit — calling 5 650, 5 700, 5 750 \"counting by 100s\" because the hundreds digit keeps moving.",
             "correction": "Subtract neighbours: 5 700 − 5 650 = 50. The hundreds digit moves because the 50s keep crossing into it — the step itself is 50.",
             "authored": True},
            {"text": "Judging odd or even by the first digit — \"2 467 is even because it starts with 2\".",
             "correction": "Only the ONES digit votes: 2 467 ends in 7, so it is odd. The 2 000 and 400 and 60 all split into pairs without help.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4nu-l5-t1",
             "statement": "Continue with one more number and name the step: $" + th(6100) + ", " + th(6200) + ", " + th(6300) + "$.",
             "solution": "Step: $" + th(6200) + " - " + th(6100) + " = 100$; next is $" + th(6300) + " + 100 = " + th(6400) + "$. Counting by $100$s.",
             "check": ["Eq(6200 - 6100, 100)", "Eq(6300 + 100, 6400)"]},
            {"id": "g4nu-l5-t2",
             "statement": "Odd or even: " + M(5550) + " and " + M(5505) + "?",
             "solution": M(5550) + " ends in $0$ — even. " + M(5505) + " ends in $5$ — odd. Same digits, different ones place, different answer.",
             "check": ["Eq(Mod(5550, 2), 0)", "Eq(Mod(5505, 2), 1)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Name the step, own the pattern", [
                "A skip-count takes the SAME step again and again. To name the step, SUBTRACT neighbours: in $" + th(s0) + ", " + th(s1) + ", " + th(s2) + "$ the step is $50$ — and every pair must agree.",
                "To continue, keep adding: the line below shows the next two landings, $" + th(s3) + "$ and $" + th(s4) + "$.",
                "The favourite steps $25$, $50$ and $100$ fit the hundreds column perfectly — four $25$s make $100$ — so these counts land on round numbers again and again.",
            ]), fig_skip),
            workedset("Continue the count",
                      "Subtract to name the step; add to continue it.", [
                wex("Continue $" + th(s0) + ", " + th(s1) + ", " + th(s2) + "$ with two more numbers.",
                    ["Step: $" + th(s1) + " - " + th(s0) + " = 50$ (and the next pair agrees).",
                     "$" + th(s2) + " + 50 = " + th(s3) + "$, then $" + th(s3) + " + 50 = " + th(s4) + "$."],
                    "$" + th(s3) + ",\\ " + th(s4) + "$",
                    ["Eq(4250 - 4200, 50)", "Eq(4300 + 50, 4350)",
                     "Eq(4350 + 50, 4400)"]),
                wex("Continue $850, 875, 900$ with two more numbers.",
                    ["Step: $875 - 850 = 25$; $900 - 875 = 25$ agrees.",
                     "$900 + 25 = 925$, then $925 + 25 = 950$."],
                    "$925, 950$",
                    ["Eq(875 - 850, 25)", "Eq(900 + 25, 925)",
                     "Eq(925 + 25, 950)"]),
            ]),
            tryitset("Step detective", "Subtract neighbours; never guess.", [
                tp("The next number in $" + th(3000) + ", " + th(3100) + ", " + th(3200) + "$ is:",
                   ["$3\\,300$", "$3\\,250$", "$4\\,200$"],
                   "Step: $" + th(3100) + " - " + th(3000) + " = 100$; so $" + th(3200) + " + 100 = " + th(3300) + "$. Jumping to $4\\,200$ adds a thousand, not a hundred.",
                   ["Eq(3100 - 3000, 100)", "Eq(3200 + 100, 3300)"]),
                tp("The step in $" + th(7425) + ", " + th(7450) + ", " + th(7475) + "$ is:",
                   ["$25$", "$50$", "$75$"],
                   "$" + th(7450) + " - " + th(7425) + " = 25$, and the second pair agrees. The ones and tens digits cycle $25, 50, 75$ — the signature of a $25$ count.",
                   ["Eq(7450 - 7425, 25)", "Eq(7475 - 7450, 25)"]),
                tp("Counting by $50$s: $" + th(9800) + ", " + th(9850) + ", " + th(9900) + ", " + th(9950) + "$, and then:",
                   ["$10\\,000$", "$9\\,990$", "$9\\,955$"],
                   "$" + th(9950) + " + 50 = " + th(10000) + "$ — the count walks right up to the fifth-column number.",
                   ["Eq(9850 - 9800, 50)", "Eq(9950 + 50, 10000)"]),
            ]),
            tapq("The loud digit lies", "In $" + th(5650) + ", " + th(5700) + ", " + th(5750) + "$ a student names the step $100$, because the hundreds digit keeps changing. The real step:",
                 ["$50$ — subtract neighbours: $" + th(5700) + " - " + th(5650) + " = 50$",
                  "$100$ — the student is right",
                  "$25$",
                  "$10$"],
                 "Subtraction, not appearances: both gaps are $50$. The hundreds digit moves because each $50$ step keeps crossing a hundred boundary — the loud digit is a side effect, not the step.",
                 ["Eq(5700 - 5650, 50)", "Eq(5750 - 5700, 50)"]),
            funfact("Why 25 feels so round",
                    "Counting by $25$s lands on a whole hundred every fourth step — $25, 50, 75, 100$ — because $4 \\times 25 = 100$. Keep going and every landing stays friendly: forty steps of $25$ reach exactly $1\\,000$. That perfect fit is why coins and scores the world over love quarters of a hundred."),
            withfig(teach("Concept B", "Odd and even — ask the ones digit", [
                "A number is EVEN when it splits into two equal teams with nobody left over: $8$ children make teams of $4$ and $4$, as the picture shows. ODD numbers always leave one out.",
                "For big numbers you never need to split anything: every ten, hundred and thousand splits evenly by itself, so only the ONES digit can leave someone out. Ending $0, 2, 4, 6, 8$: even. Ending $1, 3, 5, 7, 9$: odd.",
                "So " + M(3482) + " is even (ends in $2$) and " + M(4507) + " is odd (ends in $7$) — verdicts read straight off the last digit.",
            ]), fig_teams),
            workedset("Even splits",
                      "The ones digit gives the verdict; a fair split is the receipt.", [
                wex("Is " + M(3482) + " odd or even? And " + M(4507) + "?",
                    ["Ones digits: $2$ and $7$.",
                     M(3482) + " even; " + M(4507) + " odd — the big columns never vote."],
                    "even; odd",
                    ["Eq(Mod(3482, 2), 0)", "Eq(Mod(4507, 2), 1)"]),
                wex("Can $746$ sheep be split into two equal flocks?",
                    ["Ones digit $6$: even — yes.",
                     "Two flocks of $373$: receipt $373 + 373 = 746$ ✓."],
                    "yes — $373$ and $373$",
                    ["Eq(Mod(746, 2), 0)", "Eq(373 + 373, 746)"]),
            ]),
            tryitset("Odd one out", "Last digit only — the rest is noise.", [
                tp("Which number is ODD: " + M(2435) + ", " + M(2434) + " or " + M(2438) + "?",
                   ["$2\\,435$", "$2\\,434$", "$2\\,438$"],
                   "Ones digits $5, 4, 8$: only the $5$ is odd. The shared $2\\,43$ start is identical noise.",
                   ["Eq(Mod(2435, 2), 1)", "Eq(Mod(2434, 2), 0)"]),
                tp(M(6001) + " is:",
                   ["odd — it ends in $1$", "even — it is mostly zeros", "even — $6$ is even"],
                   "Only the ones digit votes: $1$ is odd, so " + M(6001) + " is odd — even though " + M(6000) + " right beside it is even.",
                   ["Eq(Mod(6001, 2), 1)"]),
                tp("Every EVEN number ends in:",
                   ["$0, 2, 4, 6$ or $8$", "$1, 3, 5, 7$ or $9$", "any digit at all"],
                   "The bigger places always split evenly, so the ones digit is the whole test — " + M(3480) + " is even, " + M(3485) + " is odd, and only the last digit changed the verdict.",
                   ["Eq(Mod(3480, 2), 0)", "Eq(Mod(3485, 2), 1)"]),
            ]),
            tapq("The first digit has no vote", "A student calls " + M(2467) + " even \"because it starts with $2$\". The truth:",
                 ["odd — only the ones digit votes, and $7$ is odd",
                  "even — the student is right",
                  "even — more of its digits are even than odd",
                  "it depends on the number before it"],
                 "The $2\\,460$ part splits into pairs perfectly — it is even on its own — so everything hangs on the final $7$, which leaves one out: odd.",
                 ["Eq(Mod(2467, 2), 1)", "Eq(Mod(2460, 2), 0)"]),
            recap([
                "Name a pattern's step by SUBTRACTING neighbours — every pair must agree.",
                "Continue by adding the step; describe the pattern by its step, not its digits.",
                "25, 50 and 100 fit the hundreds perfectly — their counts keep landing on round numbers.",
                "Even splits into two equal teams; odd leaves one out.",
                "Only the ones digit decides odd or even — the bigger places split evenly by themselves.",
            ]),
            tip("For each pattern below, write the step above every gap before continuing — and for each odd-or-even, point at the ones digit and ignore the rest."),
            tryitset("Mixed practice", "Steps, continuations, and verdicts.", [
                tp("The next number in $" + th(1975) + ", " + th(2000) + ", " + th(2025) + "$ is:",
                   ["$2\\,050$", "$2\\,125$", "$2\\,030$"],
                   "Step: $" + th(2000) + " - " + th(1975) + " = 25$; so $" + th(2025) + " + 25 = " + th(2050) + "$. The count strides across the thousand boundary without stumbling.",
                   ["Eq(2000 - 1975, 25)", "Eq(2025 + 25, 2050)"]),
                tp("Counting DOWN by $50$s: $950, 900, 850$, and then:",
                   ["$800$", "$750$", "$845$"],
                   "Each neighbour drops by $50$: $950 - 900 = 50$, $900 - 850 = 50$, so $850 - 50 = 800$. (Receipt: $800 + 50 = 850$.)",
                   ["Eq(950 - 900, 50)", "Eq(850 - 50, 800)",
                    "Eq(800 + 50, 850)"]),
                tp("Odd or even: " + M(9999) + " and " + M(10000) + "?",
                   ["$9\\,999$ odd, $10\\,000$ even",
                    "both odd",
                    "$9\\,999$ even, $10\\,000$ odd"],
                   "Ones digits: $9$ (odd) and $0$ (even). Neighbouring numbers ALWAYS disagree — odd and even alternate forever.",
                   ["Eq(Mod(9999, 2), 1)", "Eq(Mod(10000, 2), 0)"]),
                tp("Ticket sales climb by $100$s: $" + th(4700) + ", " + th(4800) + ", " + th(4900) + "$, and then:",
                   ["$5\\,000$", "$4\\,910$", "$5\\,900$"],
                   "Step $100$: $" + th(4900) + " + 100 = " + th(5000) + "$ — the count rolls the thousands column over.",
                   ["Eq(4800 - 4700, 100)", "Eq(4900 + 100, 5000)"]),
                tp("Which number BREAKS the by-$25$ pattern $" + th(4025) + ", " + th(4050) + ", " + th(4075) + ", " + th(4090) + "$?",
                   ["$4\\,090$", "$4\\,050$", "$4\\,075$"],
                   "The first gaps are $25$ and $25$, but $" + th(4090) + " - " + th(4075) + " = 15$ — the wrong step. The true next landing is $" + th(4100) + "$.",
                   ["Eq(4050 - 4025, 25)", "Eq(4090 - 4075, 15)",
                    "Ne(15, 25)", "Eq(4075 + 25, 4100)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Number Patterns\" — and the topic",
                    "Columns and their names, digit times place, the leftmost contest, the two-neighbour round, and steps that repeat: the whole world below ten thousand, mapped. Next year the same place-value ideas stretch to numbers in the millions — the columns just keep going left.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    a, n, b = 2700, 2764, 2800
    fig_pr5 = fig_numline([(a, lab(a)), (n, lab(n), C_WARM), (b, lab(b))],
                          lo=a, hi=b)
    return [
        prob("g4nu-pr1", "Write \"eight thousand and forty\" as a numeral.",
             "Thousands $8$, hundreds empty, tens $4$, ones empty — two zero guards: " + M(8040) + ".",
             ["Eq(8*1000 + 4*10, 8040)"]),
        prob("g4nu-pr2", "What is the $5$ worth in " + M(5213) + "? And in " + M(2513) + "?",
             "In " + M(5213) + " it stands in the thousands: $5 \\times 1\\,000 = 5\\,000$. In " + M(2513) + " it stands in the hundreds: $5 \\times 100 = 500$ — one column right, one tenth the worth.",
             ["Eq(5*1000, 5000)", "Eq(5*100, 500)"]),
        prob("g4nu-pr3", "Write " + M(9306) + " in expanded form.",
             "$9\\,000 + 300 + 6$ — the tens column is empty, so no tens part appears. Receipt: the parts add back to " + M(9306) + ".",
             ["Eq(9000 + 300 + 6, 9306)"]),
        prob("g4nu-pr4", "Order from smallest to largest: " + M(6512) + ", " + M(6125) + ", " + M(6521) + ".",
             "Thousands tie at $6$. Hundreds: $1 < 5$ makes " + M(6125) + " smallest. Between the two with $5$ hundreds, tens decide: $1 < 2$, so " + M(6512) + " $<$ " + M(6521) + ". Order: " + M(6125) + " $<$ " + M(6512) + " $<$ " + M(6521) + ".",
             ["6125 < 6512", "6512 < 6521"]),
        withprobfig(prob("g4nu-pr5", "The line shows " + M(n) + " between its neighbouring hundreds. How far is it from each of them, and what does " + M(n) + " round to at the nearest $100$?",
             "Gaps: $" + th(n) + " - " + th(a) + " = 64$ past " + M(a) + ", and $" + th(b) + " - " + th(n) + " = 36$ short of " + M(b) + ". The smaller gap wins, so to the nearest $100$, " + M(n) + " rounds to " + M(b) + ".",
             ["Eq(2764 - 2700, 64)", "Eq(2800 - 2764, 36)",
              near(2764, 2800, 2700)]), fig_pr5),
        prob("g4nu-pr6", "Round " + M(4385) + " to the nearest $10$, and then to the nearest $100$.",
             "Nearest $10$: neighbours " + M(4380) + " and " + M(4390) + ", gaps $5$ and $5$ — halfway rounds UP to " + M(4390) + ". Nearest $100$: neighbours " + M(4300) + " and " + M(4400) + ", gaps $85$ and $15$ — the $15$ wins: " + M(4400) + ".",
             ["Eq(4385 - 4380, 5)", "Eq(4390 - 4385, 5)",
              "Eq(4385 - 4300, 85)", "Eq(4400 - 4385, 15)",
              near(4385, 4400, 4300)]),
        prob("g4nu-pr7", "Estimate $" + th(3245) + " + " + th(2178) + "$ by rounding each to the nearest $100$, then find the exact sum.",
             "Round: $3\\,200 + 2\\,200 = 5\\,400$. Exact: $" + th(3245) + " + " + th(2178) + " = " + th(5423) + "$ — the estimate sits $23$ below, close enough to back it up.",
             [near(3245, 3200, 3300), near(2178, 2200, 2100),
              "Eq(3200 + 2200, 5400)", "Eq(3245 + 2178, 5423)"]),
        prob("g4nu-pr8", "Continue $" + th(8500) + ", " + th(8550) + ", " + th(8600) + "$ with two more numbers. Is your first new number odd or even?",
             "Step: $" + th(8550) + " - " + th(8500) + " = 50$; continue $" + th(8650) + ", " + th(8700) + "$. " + M(8650) + " ends in $0$: even.",
             ["Eq(8550 - 8500, 50)", "Eq(8600 + 50, 8650)",
              "Eq(8650 + 50, 8700)", "Eq(Mod(8650, 2), 0)"]),
    ]


def test_bank():
    return [
        prob("g4nu-x1", "Write \"seven thousand and six\" as a numeral, and " + M(3090) + " in words.",
             "Seven thousand and six: thousands $7$, then two zero guards, then $6$ — " + M(7006) + ". And " + M(3090) + " reads \"three thousand and ninety\": the guard silences the hundreds.",
             ["Eq(7*1000 + 6, 7006)", "Eq(3*1000 + 9*10, 3090)"]),
        prob("g4nu-x2", "What is the $8$ worth in " + M(8245) + ", and in " + M(2845) + "? Write " + M(8245) + " in expanded form.",
             "Thousands column: $8 \\times 1\\,000 = 8\\,000$; hundreds column: $8 \\times 100 = 800$. Expanded: $" + th(8245) + " = 8\\,000 + 200 + 40 + 5$.",
             ["Eq(8*1000, 8000)", "Eq(8*100, 800)",
              "Eq(8000 + 200 + 40 + 5, 8245)"]),
        prob("g4nu-x3", "Order from smallest to largest: " + M(4087) + ", " + M(4807) + ", " + M(4078) + ", " + M(4870) + ".",
             "Thousands all tie. Hundreds split the field: the $0$-hundreds pair comes first, the $8$-hundreds pair second. Tens finish it: " + M(4078) + " $<$ " + M(4087) + " $<$ " + M(4807) + " $<$ " + M(4870) + ".",
             ["4078 < 4087", "4087 < 4807", "4807 < 4870"]),
        prob("g4nu-x4", "Round " + M(6550) + " and " + M(6549) + " to the nearest $100$.",
             M(6550) + ": gaps of $50$ to each neighbour — exactly halfway, so UP to " + M(6600) + ". " + M(6549) + ": gaps $49$ down, $51$ up — one below halfway, so DOWN to " + M(6500) + ". One apart, they round apart.",
             ["Eq(6550 - 6500, 50)", "Eq(6600 - 6550, 50)",
              "Eq(6549 - 6500, 49)", "Eq(6600 - 6549, 51)",
              near(6549, 6500, 6600)]),
        prob("g4nu-x5", "A school orders " + M(1890) + " red caps and " + M(2130) + " blue caps. Estimate the total by rounding each to the nearest $100$, then find the exact total.",
             "Round: $1\\,900 + 2\\,100 = 4\\,000$. Exact: $" + th(1890) + " + " + th(2130) + " = " + th(4020) + "$ — the estimate lands $20$ under, backing up the sum.",
             [near(1890, 1900, 1800), near(2130, 2100, 2200),
              "Eq(1900 + 2100, 4000)", "Eq(1890 + 2130, 4020)",
              "Eq(4020 - 4000, 20)"]),
        prob("g4nu-x6", "Continue $" + th(2925) + ", " + th(2950) + ", " + th(2975) + "$ with two more numbers, name the step, and say which of your two new numbers is even.",
             "Step: $" + th(2950) + " - " + th(2925) + " = 25$. Continue: $" + th(3000) + "$ and $" + th(3025) + "$. Ones digits $0$ and $5$: " + M(3000) + " is even, " + M(3025) + " odd.",
             ["Eq(2950 - 2925, 25)", "Eq(2975 + 25, 3000)",
              "Eq(3000 + 25, 3025)",
              "Eq(Mod(3000, 2), 0)", "Eq(Mod(3025, 2), 1)"]),
    ]


def main():
    topic = {
        "slug": "numbers-to-10000",
        "title": "Numbers to 10 000",
        "grade": 4,
        "status": "published",
        "blurb": ("Reading and writing four-digit numbers, place value to "
                  "thousands, comparing and ordering, rounding to 10 and 100, "
                  "and skip-counting patterns."),
        "lessons": [
            lesson_reading(),
            lesson_place_value(),
            lesson_comparing(),
            lesson_rounding(),
            lesson_patterns(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "numbers-to-10000.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
