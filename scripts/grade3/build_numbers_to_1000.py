#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Numbers to 1000.

The three-digit world: hundreds, tens and ones as three bundles you could
actually tie; reading and writing those numbers in digits and in words,
with zero holding a place open; comparing and ordering by walking left to
right; counting in steps of 2, 5, 10 and 100 and hearing the pattern in
the endings; and rounding to the nearest ten by asking which ten the
number is closer to.

Through-line: A DIGIT'S VALUE IS ITS PLACE. Every lesson returns to it —
the columns give each digit a job, the words say the jobs aloud, the
comparison reads the biggest job first, the step-counting marches one
column at a time, and rounding asks which ten a number is nearest.

Grade discipline: nothing above 1000, no negatives, no decimals, no
formal algorithms (that is Grade 4's column work). Every check is
sympy-asserted with exact integers BEFORE the JSON is written — a wrong
fact cannot ship. Figures are built from the SAME Python variables as the
statements they illustrate, so text and picture cannot disagree.

Run: python3 scripts/grade3/build_numbers_to_1000.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, workedset, write_topic,
                     fig_groups, fig_numline, C_ACCENT, C_WARM, C_GREEN)


def bundles(h, t, o, colors=(C_ACCENT, C_WARM, C_GREEN)):
    """A place-value picture: h hundreds, t tens, o ones as three labelled
    groups. Built from the same digits the statement quotes, so the picture
    and the number are the same fact told twice."""
    assert 0 <= h <= 9 and 0 <= t <= 9 and 0 <= o <= 9, "bundles: not digits"
    return fig_groups((h, "%d hundreds" % h, colors[0]),
                      (t, "%d tens" % t, colors[1]),
                      (o, "%d ones" % o, colors[2]))


# ==========================================================================
# Lesson 1 — Hundreds, Tens and Ones
# ==========================================================================

def lesson_hundreds_tens_ones():
    # The anchor number, used by the statement AND the figure.
    h1, t1, o1 = 3, 4, 2
    n1 = 100 * h1 + 10 * t1 + o1  # 342
    fig_flock = bundles(h1, t1, o1)
    # The twin-digit number that proves place beats shape.
    fig_twin = bundles(3, 5, 3)
    # The zero-placeholder picture: an empty tens column still standing.
    fig_zero = bundles(4, 0, 6)
    fig_207 = bundles(2, 0, 7)
    return {
        "slug": "hundreds-tens-and-ones",
        "title": "Hundreds, Tens and Ones",
        "concreteComparison": (
            "A herder counts the flock by tying it into bundles: $3$ "
            "bundles of one hundred, $4$ bundles of ten, and $2$ sheep "
            "still loose. Written down that is $342$ — and the $3$, the "
            "$4$ and the $2$ are not three numbers in a row. They are "
            "the count of hundreds, the count of tens, and the count of "
            "ones. The digits are a receipt for the bundles."),
        "objective": (
            "Say what each digit of a three-digit number is worth, split "
            "a number into hundreds, tens and ones, and build a number "
            "back from its parts."),
        "concept": [
            "**Three columns, three jobs.** A three-digit number has a "
            "hundreds column, a tens column and a ones column, always in "
            "that order from the left. In $342$ the $3$ counts hundreds "
            "($300$), the $4$ counts tens ($40$) and the $2$ counts ones "
            "($2$): $300 + 40 + 2 = 342$.",
            "**The same digit is worth different amounts in different "
            "places.** In $353$ the left $3$ sits in the hundreds column "
            "and is worth $300$; the right $3$ sits in the ones column "
            "and is worth $3$. The digit is the same shape both times — "
            "its PLACE decides what it is worth.",
            "**Zero holds a place open.** $406$ means $4$ hundreds, $0$ "
            "tens and $6$ ones. Without that zero the $4$ and the $6$ "
            "would slide together into $46$, which is a completely "
            "different number. Zero counts nothing, and that is exactly "
            "the job: it keeps the other digits standing in their own "
            "columns.",
        ],
        "keyIdea": (
            "A digit's value is its place. Read a three-digit number as "
            "three counts — so many hundreds, so many tens, so many ones "
            "— and a zero in a column means that column is empty, not "
            "missing."),
        "facts": [
            {"title": "Split by place",
             "latex": "342 = 300 + 40 + 2",
             "explanation": "Three hundreds, four tens, two ones — the number is the sum of what its digits are worth."},
            {"title": "Zero keeps the column",
             "latex": "406 = 400 + 0 + 6",
             "explanation": "The empty tens column still has to be written, or the 4 and the 6 collapse into 46."},
        ],
        "workedExamples": [
            {"id": "g3nt-l1-we1",
             "statement": "The flock has $%d$ sheep. How many bundles of one hundred, bundles of ten, and loose sheep is that?" % n1,
             "note": "Read the digits from the left: hundreds, then tens, then ones.",
             "solution": ("The $3$ is in the hundreds column, so $3$ bundles of "
                          "one hundred — worth $300$. The $4$ is in the tens "
                          "column: $4$ bundles of ten, worth $40$. The $2$ is in "
                          "the ones column: $2$ loose sheep. Together "
                          "$300 + 40 + 2 = 342$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(100*3 + 10*4 + 2, 342)", "Eq(300 + 40 + 2, 342)"]},
            {"id": "g3nt-l1-we2",
             "statement": "In the number $353$, what is each $3$ worth?",
             "note": "Same digit, two different columns.",
             "solution": ("The left $3$ sits in the hundreds column, so it is "
                          "worth $300$. The right $3$ sits in the ones column, so "
                          "it is worth $3$. The place, not the shape, decides: "
                          "$300 + 50 + 3 = 353$, and $300$ is a hundred times as "
                          "much as $3$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(300 + 50 + 3, 353)", "Eq(100*3, 300)", "Ne(300, 3)"]},
        ],
        "commonMistakes": [
            {"text": "Reading every digit as its bare shape — calling the 3 in 342 \"three\".",
             "correction": "That 3 stands in the hundreds column, so it counts three HUNDREDS: 300. Reading it as 3 shrinks the number from 342 to something near 9.",
             "authored": True},
            {"text": "Dropping the zero when writing four hundred and six, giving 46.",
             "correction": "406 has an empty tens column, and the 0 is what keeps it empty. Leave the 0 out and the 6 slides into the tens place: 46, which is smaller by 360.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3nt-l1-t1",
             "statement": "Split $528$ into hundreds, tens and ones.",
             "solution": "$5$ hundreds, $2$ tens and $8$ ones: $500 + 20 + 8 = 528$.",
             "check": ["Eq(500 + 20 + 8, 528)", "Eq(100*5 + 10*2 + 8, 528)"]},
            {"id": "g3nt-l1-t2",
             "statement": "Build the number with $7$ hundreds, $0$ tens and $3$ ones. Why can the $0$ not be left out?",
             "solution": ("$700 + 0 + 3 = 703$. Leaving the $0$ out writes $73$ — "
                          "the $7$ would drop from the hundreds column to the "
                          "tens column and lose $630$."),
             "check": ["Eq(700 + 0 + 3, 703)", "Eq(703 - 73, 630)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Three bundles, three columns", [
                "The picture below is a flock tied into bundles: $%d$ bundles of one hundred, $%d$ bundles of ten, and $%d$ sheep still loose." % (h1, t1, o1),
                "Written as a number that is $%d$. The first digit counts the HUNDREDS, the second counts the TENS, the third counts the ONES — always in that order, left to right." % n1,
                "So $%d$ is really a short way of writing $300 + 40 + 2$. Every three-digit number is three counts wearing one coat." % n1,
            ]), fig_flock),
            workedset("Split it by place",
                      "Name the column each digit stands in, then say what it is worth.", [
                wex("Split $%d$ into hundreds, tens and ones." % n1,
                    ["$3$ in the hundreds column: $300$.",
                     "$4$ in the tens column: $40$. $2$ in the ones column: $2$.",
                     "$300 + 40 + 2 = 342$."],
                    "$3$ hundreds, $4$ tens, $2$ ones",
                    ["Eq(300 + 40 + 2, 342)"]),
                wex("Split $615$ into hundreds, tens and ones.",
                    ["$6$ hundreds is $600$.",
                     "$1$ ten is $10$, and $5$ ones is $5$.",
                     "$600 + 10 + 5 = 615$."],
                    "$6$ hundreds, $1$ ten, $5$ ones",
                    ["Eq(600 + 10 + 5, 615)"]),
            ]),
            tryitset("Which column?", "Count in from the left: hundreds, tens, ones.", [
                tp("In $487$, the digit $4$ is worth:",
                   ["$400$", "$4$", "$40$"],
                   "The $4$ stands in the hundreds column, so it counts four hundreds: $400$. Reading it as $4$ or $40$ would put it in the wrong column — $487$ would shrink to $87$ or $127$.",
                   ["Eq(400 + 80 + 7, 487)", "Eq(100*4, 400)"]),
                tp("The number with $2$ hundreds, $6$ tens and $9$ ones is:",
                   ["$269$", "$629$", "$296$"],
                   "Hundreds first, then tens, then ones: $200 + 60 + 9 = 269$. $629$ reads the columns in the wrong order altogether, and $296$ swaps just the last two.",
                   ["Eq(200 + 60 + 9, 269)", "Eq(600 + 20 + 9, 629)",
                    "Eq(296 - 269, 27)"]),
                withfig(tp("The picture shows the bundles for:",
                   ["$353$", "$335$", "$533$"],
                   "Three hundreds, five tens, three ones: $300 + 50 + 3 = 353$. The two $3$s look alike but do different jobs — one counts hundreds, one counts ones.",
                   ["Eq(300 + 50 + 3, 353)", "Eq(300 + 30 + 5, 335)"]), fig_twin),
            ]),
            tapq("Same digit, different job", "In $353$, how much bigger is the left $3$ than the right $3$?",
                 ["$297$ bigger", "the same — both are $3$",
                  "$30$ bigger", "$3$ bigger"],
                 "The left $3$ is worth $300$ and the right $3$ is worth $3$: $300 - 3 = 297$. The digits look identical, but their columns make them worth wildly different amounts.",
                 ["Eq(300 - 3, 297)", "Ne(300, 3)"]),
            funfact("Why three digits and not more names",
                    "Some old counting systems gave every size its own symbol, so a big number meant learning a new sign. Place value threw all those signs away and kept ten digits, letting the COLUMN do the work. It is why $342$ and $243$ can be written with the same three digits and still be different numbers — and why you can read a number you have never seen before."),
            withfig(teach("Concept B", "The zero that holds a place", [
                "The picture below shows $4$ bundles of one hundred, NO bundles of ten, and $6$ loose. The tens column is empty — but it is still there.",
                "So the number is $406$: four hundreds, zero tens, six ones. The $0$ counts nothing, and that is precisely its job — it keeps the $4$ up in the hundreds column and the $6$ down in the ones.",
                "Leave the $0$ out and you write $46$. The $4$ falls two columns and the number shrinks by $360$. A zero is never decoration.",
            ]), fig_zero),
            workedset("Numbers with an empty column",
                      "Write the count for EVERY column, even the empty ones.", [
                wex("Write four hundreds, no tens and six ones as a number.",
                    ["Hundreds: $4$. Tens: $0$. Ones: $6$.",
                     "Reading the columns in order gives $406$.",
                     "Check: $400 + 0 + 6 = 406$."],
                    "$406$",
                    ["Eq(400 + 0 + 6, 406)", "Eq(406 - 46, 360)"]),
                wex("What is the $0$ doing in $270$?",
                    ["The columns are $2$ hundreds, $7$ tens, $0$ ones.",
                     "There are no loose ones, so the ones column is empty.",
                     "$200 + 70 + 0 = 270$ — and without the $0$ you would write $27$."],
                    "It marks an empty ones column",
                    ["Eq(200 + 70 + 0, 270)", "Eq(270 - 27, 243)"]),
            ]),
            tryitset("Mind the empty column", "An empty column still gets a digit — a zero.", [
                withfig(tp("The picture shows $2$ hundreds, no tens and $7$ ones. The number is:",
                   ["$207$", "$27$", "$270$"],
                   "Two hundreds, zero tens, seven ones: $200 + 0 + 7 = 207$. Writing $27$ drops the hundreds altogether; $270$ moves the $7$ into the tens column.",
                   ["Eq(200 + 0 + 7, 207)", "Eq(207 - 27, 180)"]), fig_207),
                tp("In $580$, the $0$ tells you there are:",
                   ["no ones", "no tens", "no hundreds"],
                   "The last column is the ones column, so the $0$ says there are no loose ones: $500 + 80 + 0 = 580$. The tens column holds an $8$, so there certainly are tens.",
                   ["Eq(500 + 80 + 0, 580)", "Eq(Mod(580, 10), 0)"]),
                tp("Which number has an empty TENS column?",
                   ["$904$", "$940$", "$490$"],
                   "$904$ is $9$ hundreds, $0$ tens, $4$ ones. In $940$ the empty column is the ones; in $490$ it is the ones again, with $9$ tens standing.",
                   ["Eq(900 + 0 + 4, 904)", "Eq(900 + 40 + 0, 940)"]),
            ]),
            tapq("The vanishing zero", "Bat writes six hundred and five as $65$. How far wrong is he?",
                 ["$540$ too small", "$5$ too small",
                  "$60$ too small", "he is right"],
                 "Six hundred and five is $605$: six hundreds, zero tens, five ones. Bat's $65$ is short by $605 - 65 = 540$, because his $6$ slipped from the hundreds column down into the tens.",
                 ["Eq(600 + 0 + 5, 605)", "Eq(605 - 65, 540)"]),
            recap([
                "A three-digit number is three counts: hundreds, tens and ones, read left to right.",
                "A digit's value is its PLACE — the $3$ in $342$ is worth $300$, not $3$.",
                "$342 = 300 + 40 + 2$: the number is the sum of what its digits are worth.",
                "A zero marks an empty column and holds the other digits in theirs — drop it and every digit to its left falls.",
            ]),
            tip("Say each number aloud as its columns — \"four hundreds, no tens, six ones\" — before you write it. The words put every digit in the right place before your pencil can drop one."),
            tryitset("Chapter practice", "Columns first, value second.", [
                tp("$800 + 30 + 9$ is:",
                   ["$839$", "$893$", "$389$"],
                   "Eight hundreds, three tens, nine ones: $839$. $893$ swaps the tens and ones columns; $389$ demotes the $8$ all the way to the ones.",
                   ["Eq(800 + 30 + 9, 839)", "Eq(800 + 90 + 3, 893)",
                    "Eq(300 + 80 + 9, 389)"]),
                tp("In $161$, the two $1$s are worth:",
                   ["$100$ and $1$", "$1$ and $1$", "$10$ and $1$"],
                   "The left $1$ is in the hundreds column ($100$); the right $1$ is in the ones column ($1$). The $6$ in the middle holds the tens: $100 + 60 + 1 = 161$.",
                   ["Eq(100 + 60 + 1, 161)", "Ne(100, 1)"]),
                tp("Which of these is three hundred and forty?",
                   ["$340$", "$304$", "$34$"],
                   "Three hundreds, four tens, no ones: $300 + 40 + 0 = 340$. $304$ puts the $4$ in the ones column instead, and $34$ has no hundreds at all.",
                   ["Eq(300 + 40 + 0, 340)", "Eq(300 + 0 + 4, 304)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Hundreds, Tens and Ones\"",
                    "You can now take any three-digit number apart and put it back together. That one habit — asking what column a digit stands in — is the whole of the next four lessons too: it is how you will read numbers aloud, compare them, count in steps and round them.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Reading and Writing Numbers
# ==========================================================================

def lesson_reading_writing():
    fig_word = bundles(2, 7, 5)
    fig_teen = bundles(1, 1, 4)
    fig_630 = bundles(6, 3, 0)
    return {
        "slug": "reading-and-writing-numbers",
        "title": "Reading and Writing Numbers",
        "concreteComparison": (
            "A shop sign says the ger costs \"two hundred and seventy-five "
            "thousand tögrög\", but the price tag just says $275$ "
            "thousand. Words and digits are two spellings of the same "
            "number, and you have to be able to swap between them without "
            "losing a single column."),
        "objective": (
            "Read a three-digit number aloud in words, write a number "
            "from its words, and place a number correctly when the words "
            "skip a column."),
        "concept": [
            "**Say the columns in order.** $275$ is read \"two hundred "
            "and seventy-five\": the hundreds first ($2$ hundred), then "
            "the tens and ones together as one spoken chunk "
            "(\"seventy-five\"). The order you say it in is the order the "
            "digits sit in.",
            "**The teens are the tricky corner.** From $11$ to $19$ the "
            "spoken name puts the ONES first — \"fourteen\" is four-and-"
            "ten. So one hundred and fourteen is $114$, not $141$. Say "
            "the columns to yourself and the trap disappears.",
            "**A skipped word means a zero.** If the words never mention "
            "tens — \"six hundred and three\" — the tens column is empty, "
            "so a $0$ goes there: $603$. If the words end at the tens — "
            "\"six hundred and thirty\" — the ones column is empty: "
            "$630$.",
        ],
        "keyIdea": (
            "Words and digits carry the same three counts. Read left to "
            "right, and whenever the words are silent about a column, "
            "write a zero there rather than nothing at all."),
        "facts": [
            {"title": "Words to digits",
             "latex": "275 = 200 + 70 + 5",
             "explanation": "\"Two hundred and seventy-five\" says the hundreds, then the tens and ones."},
            {"title": "A silent column is a zero",
             "latex": "603 = 600 + 0 + 3",
             "explanation": "\"Six hundred and three\" never mentions tens, so the tens column takes a 0."},
        ],
        "workedExamples": [
            {"id": "g3nt-l2-we1",
             "statement": "Write \"two hundred and seventy-five\" in digits.",
             "note": "Take the words one column at a time.",
             "solution": ("\"Two hundred\" fills the hundreds column with $2$. "
                          "\"Seventy\" is $7$ tens and \"five\" is $5$ ones. "
                          "So the digits are $275$, and $200 + 70 + 5 = 275$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(200 + 70 + 5, 275)"]},
            {"id": "g3nt-l2-we2",
             "statement": "Write \"one hundred and fourteen\" in digits, and say why it is not $141$.",
             "note": "\"Fourteen\" is a teen — the ones are spoken first.",
             "solution": ("\"One hundred\" gives $1$ in the hundreds column. "
                          "\"Fourteen\" is $1$ ten and $4$ ones, so the digits "
                          "are $114$: $100 + 10 + 4 = 114$. Writing $141$ hears "
                          "\"four\" as tens and \"teen\" as ones, which makes a "
                          "number $27$ bigger."),
             "badges": [{"text": "core"}],
             "check": ["Eq(100 + 10 + 4, 114)", "Eq(141 - 114, 27)"]},
        ],
        "commonMistakes": [
            {"text": "Writing the teens backwards — hearing \"fourteen\" and writing 41.",
             "correction": "Fourteen is one ten and four ones: 14. The English name says the ones first, but the digits keep the usual order — tens then ones.",
             "authored": True},
            {"text": "Writing \"six hundred and three\" as 63, leaving the empty tens column out.",
             "correction": "The words are silent about tens, which means zero tens, not no column: 603. Skipping it costs 540.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3nt-l2-t1",
             "statement": "Write \"four hundred and ninety\" in digits.",
             "solution": "Four hundreds, nine tens, and no ones: $400 + 90 + 0 = 490$.",
             "check": ["Eq(400 + 90 + 0, 490)", "Eq(Mod(490, 10), 0)"]},
            {"id": "g3nt-l2-t2",
             "statement": "Read $308$ aloud in words.",
             "solution": ("\"Three hundred and eight\" — the tens column holds a "
                          "$0$, so the words say nothing between the hundreds "
                          "and the ones: $300 + 0 + 8 = 308$."),
             "check": ["Eq(300 + 0 + 8, 308)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Say the columns in order", [
                "The bundles below are $2$ hundreds, $7$ tens and $5$ ones — the number $275$.",
                "Aloud that is \"two hundred and seventy-five\". Notice the order: the hundreds are named first, then the tens and ones are said together as one chunk.",
                "That is the whole rule for reading. The mouth walks the columns in the same direction the eye does — left to right.",
            ]), fig_word),
            workedset("From words to digits",
                      "Fill one column per chunk of the words.", [
                wex("Write \"two hundred and seventy-five\" in digits.",
                    ["\"Two hundred\" — hundreds column gets $2$.",
                     "\"Seventy-five\" — $7$ tens and $5$ ones.",
                     "$200 + 70 + 5 = 275$."],
                    "$275$",
                    ["Eq(200 + 70 + 5, 275)"]),
                wex("Write \"eight hundred and sixty-two\" in digits.",
                    ["\"Eight hundred\" gives $8$ hundreds.",
                     "\"Sixty-two\" gives $6$ tens and $2$ ones.",
                     "$800 + 60 + 2 = 862$."],
                    "$862$",
                    ["Eq(800 + 60 + 2, 862)"]),
            ]),
            tryitset("Words into digits", "One chunk of words, one column.", [
                tp("\"Five hundred and forty-one\" in digits is:",
                   ["$541$", "$514$", "$451$"],
                   "Five hundreds, four tens, one one: $500 + 40 + 1 = 541$. $514$ swaps the last two columns and $451$ swaps the first two.",
                   ["Eq(500 + 40 + 1, 541)", "Eq(541 - 514, 27)"]),
                tp("\"Nine hundred and thirty\" in digits is:",
                   ["$930$", "$903$", "$93$"],
                   "Nine hundreds, three tens, no ones: $900 + 30 + 0 = 930$. $903$ puts the $3$ in the ones column instead; $93$ loses the hundreds entirely.",
                   ["Eq(900 + 30 + 0, 930)", "Eq(900 + 0 + 3, 903)"]),
                tp("$746$ read aloud is:",
                   ["seven hundred and forty-six",
                    "seven hundred and sixty-four",
                    "four hundred and seventy-six"],
                   "The columns are $7$ hundreds, $4$ tens, $6$ ones: $700 + 40 + 6 = 746$. \"Sixty-four\" would be $764$ — the same digits in a different order.",
                   ["Eq(700 + 40 + 6, 746)", "Eq(700 + 60 + 4, 764)"]),
            ]),
            tapq("The teen trap", "Which number is \"one hundred and fourteen\"?",
                 ["$114$", "$141$", "$411$", "$104$"],
                 "\"Fourteen\" means $1$ ten and $4$ ones, so the number is $100 + 10 + 4 = 114$. Hearing \"four\" as the tens gives $141$ — which is $27$ too big.",
                 ["Eq(100 + 10 + 4, 114)", "Eq(141 - 114, 27)"]),
            funfact("The teens are the leftovers of an older count",
                    "\"Eleven\" and \"twelve\" do not sound like \"one-teen\" and \"two-teen\" because they are older words, from a time when people counted in twelves as often as in tens — eleven meant \"one left over\" after ten. From thirteen onward the pattern settles down and every name is just the ones and the ten stuck together backwards. It is the only corner of English counting where the digits and the words march in opposite directions."),
            withfig(teach("Concept B", "When the words skip a column", [
                "The bundles below are $6$ hundreds, $3$ tens and NO ones. Aloud: \"six hundred and thirty\" — the words simply stop, because there is nothing in the ones column to name.",
                "But the digits cannot stop. The ones column still has to be written, so it takes a $0$: $630$.",
                "The same happens in the middle. \"Six hundred and three\" names hundreds and ones but never tens, so the tens column takes a $0$: $603$. Silence in the words means a zero in the digits.",
            ]), fig_630),
            workedset("Silent columns", "Every column the words skip gets a $0$.", [
                wex("Write \"six hundred and three\" in digits.",
                    ["\"Six hundred\" fills the hundreds with $6$.",
                     "No tens are named, so the tens column takes $0$.",
                     "\"Three\" gives $3$ ones: $600 + 0 + 3 = 603$."],
                    "$603$",
                    ["Eq(600 + 0 + 3, 603)", "Eq(603 - 63, 540)"]),
                wex("Write \"four hundred and twenty\" in digits.",
                    ["\"Four hundred\" gives $4$ hundreds.",
                     "\"Twenty\" gives $2$ tens; no ones are named.",
                     "$400 + 20 + 0 = 420$."],
                    "$420$",
                    ["Eq(400 + 20 + 0, 420)", "Eq(Mod(420, 10), 0)"]),
            ]),
            tryitset("Fill the silent column", "Nothing said about a column means a zero in it.", [
                tp("\"Two hundred and nine\" in digits is:",
                   ["$209$", "$29$", "$290$"],
                   "No tens are named, so a $0$ holds that column: $200 + 0 + 9 = 209$. $29$ throws the hundreds away, and $290$ moves the $9$ up into the tens.",
                   ["Eq(200 + 0 + 9, 209)", "Eq(209 - 29, 180)"]),
                tp("$570$ read aloud is:",
                   ["five hundred and seventy",
                    "five hundred and seven",
                    "fifty-seven"],
                   "The ones column holds a $0$, so nothing is said after \"seventy\": $500 + 70 + 0 = 570$. \"Five hundred and seven\" would be $507$.",
                   ["Eq(500 + 70 + 0, 570)", "Eq(500 + 0 + 7, 507)"]),
                tp("Which pair of words describes $101$?",
                   ["one hundred and one",
                    "one hundred and ten",
                    "eleven"],
                   "One hundred, zero tens, one one: $100 + 0 + 1 = 101$. \"One hundred and ten\" is $110$, where the $1$ has moved into the tens column.",
                   ["Eq(100 + 0 + 1, 101)", "Eq(100 + 10 + 0, 110)"]),
            ]),
            tapq("Two names, one gap", "How much bigger is \"three hundred and thirty\" than \"three hundred and three\"?",
                 ["$27$ bigger", "$3$ bigger", "$30$ bigger", "they are equal"],
                 "The two numbers are $330$ and $303$: $330 - 303 = 27$. Same three digits, but the $3$ moved from the ones column up to the tens, and $27$ appeared out of the move.",
                 ["Eq(300 + 30 + 0, 330)", "Eq(300 + 0 + 3, 303)", "Eq(330 - 303, 27)"]),
            recap([
                "Read a number left to right: hundreds first, then tens and ones together.",
                "The teens hide their tens — \"fourteen\" is $1$ ten and $4$ ones, so it is $14$, never $41$.",
                "If the words never mention a column, that column holds a $0$: \"six hundred and three\" is $603$.",
                "Words and digits must agree column for column, or the number changes.",
            ]),
            tip("When you write a number from words, draw three short lines first — one for each column — and fill them in as you hear the words. Any line still blank at the end gets a $0$."),
            tryitset("Chapter practice", "Say it in columns, then write it.", [
                tp("\"Seven hundred and sixteen\" in digits is:",
                   ["$716$", "$761$", "$617$"],
                   "\"Sixteen\" is $1$ ten and $6$ ones, so the number is $700 + 10 + 6 = 716$. Hearing \"six\" as tens gives $761$, which is $45$ too big.",
                   ["Eq(700 + 10 + 6, 716)", "Eq(761 - 716, 45)"]),
                tp("$480$ read aloud is:",
                   ["four hundred and eighty",
                    "four hundred and eight",
                    "eight hundred and forty"],
                   "Four hundreds, eight tens, no ones: $400 + 80 + 0 = 480$. \"Four hundred and eight\" is $408$ — the $8$ dropped a column.",
                   ["Eq(400 + 80 + 0, 480)", "Eq(400 + 0 + 8, 408)"]),
                tp("Which number needs a zero in the MIDDLE column?",
                   ["nine hundred and four",
                    "nine hundred and forty",
                    "four hundred and nine"],
                   "\"Nine hundred and four\" names no tens, so it is $904$. \"Nine hundred and forty\" is $940$ and \"four hundred and nine\" is $409$ — each of those has its zero at the end or the tens filled.",
                   ["Eq(900 + 0 + 4, 904)", "Eq(400 + 0 + 9, 409)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Reading and Writing Numbers\"",
                    "Digits and words now travel both ways for you. That matters more than it looks: prices, bus numbers and page numbers all arrive in one form or the other, and the column habit is what keeps a $603$ from turning into a $63$ on the way into your notebook.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Comparing and Ordering
# ==========================================================================

def lesson_comparing_ordering():
    fig_cmp = fig_groups((4, "463: 4 hundreds", C_ACCENT),
                         (2, "258: 2 hundreds", C_WARM))
    fig_tie = fig_groups((3, "376: 7 tens", C_ACCENT),
                         (3, "349: 4 tens", C_WARM))
    fig_line = fig_numline([(258, "258"), (376, "376"), (463, "463")],
                           lo=200, hi=500)
    return {
        "slug": "comparing-and-ordering",
        "title": "Comparing and Ordering",
        "concreteComparison": (
            "Three herders bring their flocks to market: $463$, $258$ and "
            "$376$ animals. To line them up biggest to smallest nobody "
            "counts a single sheep — they look at the hundreds first, and "
            "only look further if the hundreds tie."),
        "objective": (
            "Compare two three-digit numbers by walking the columns from "
            "the left, use the $>$, $<$ and $=$ signs correctly, and put "
            "a list of numbers in order."),
        "concept": [
            "**Start at the biggest column.** Hundreds outweigh "
            "everything to their right: $463$ beats $258$ the moment you "
            "see $4$ hundreds against $2$, because even the largest "
            "possible tens and ones ($99$) cannot make up a whole "
            "hundred.",
            "**Only move right on a tie.** If the hundreds match, compare "
            "the tens; if those match too, compare the ones. $376$ and "
            "$349$ both have $3$ hundreds, so the tens decide: $7$ tens "
            "beat $4$ tens, and $376 > 349$.",
            "**The signs point at the smaller number.** $463 > 258$ reads "
            "\"four hundred and sixty-three is greater than two hundred "
            "and fifty-eight\"; the wide end faces the bigger number and "
            "the point faces the smaller. $258 < 463$ says exactly the "
            "same thing from the other side.",
        ],
        "keyIdea": (
            "Compare from the left and stop at the first column where the "
            "digits differ — that column decides, no matter what follows "
            "it."),
        "facts": [
            {"title": "Hundreds decide first",
             "latex": "463 > 258",
             "explanation": "4 hundreds beat 2 hundreds; the tens and ones never get a vote."},
            {"title": "A tie moves you right",
             "latex": "376 > 349",
             "explanation": "Equal hundreds, so the tens decide: 7 tens beat 4 tens."},
        ],
        "workedExamples": [
            {"id": "g3nt-l3-we1",
             "statement": "Compare $463$ and $258$ with the correct sign.",
             "note": "Look at the hundreds column first.",
             "solution": ("$463$ has $4$ hundreds and $258$ has $2$. Four beats "
                          "two, so $463 > 258$ — and no further looking is "
                          "needed. Even the biggest tens and ones, $99$, could "
                          "not close a gap of two whole hundreds."),
             "badges": [{"text": "core"}],
             "check": ["463 > 258", "Eq(463 - 258, 205)", "205 > 99"]},
            {"id": "g3nt-l3-we2",
             "statement": "Compare $376$ and $349$.",
             "note": "The hundreds tie, so keep going.",
             "solution": ("Both have $3$ hundreds, so that column tells you "
                          "nothing. Move right: $7$ tens against $4$ tens. Seven "
                          "wins, so $376 > 349$ — even though the $9$ in $349$ "
                          "is the biggest digit on the page."),
             "badges": [{"text": "core"}],
             "check": ["376 > 349", "Eq(376 - 349, 27)", "70 > 40"]},
        ],
        "commonMistakes": [
            {"text": "Picking the number with the biggest single digit — calling 349 larger than 376 because of the 9.",
             "correction": "A digit's size means nothing without its column. The 9 in 349 sits in the ones and is worth 9; the 7 in 376 sits in the tens and is worth 70. Compare columns from the left, and 376 wins.",
             "authored": True},
            {"text": "Turning the sign the wrong way — writing 258 > 463.",
             "correction": "The wide end of the sign always faces the bigger number. 463 is bigger, so it is 463 > 258, or 258 < 463 said the other way round.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3nt-l3-t1",
             "statement": "Put $258$, $463$ and $376$ in order from smallest to largest.",
             "solution": ("Hundreds first: $2$, then $3$, then $4$. So the order "
                          "is $258$, $376$, $463$ — and $258 < 376 < 463$."),
             "check": ["258 < 376", "376 < 463"]},
            {"id": "g3nt-l3-t2",
             "statement": "Compare $505$ and $550$ and explain which column decided.",
             "solution": ("The hundreds tie at $5$. The tens decide: $0$ tens "
                          "against $5$ tens, so $505 < 550$. The gap is $45$."),
             "check": ["505 < 550", "Eq(550 - 505, 45)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Hundreds get the first word", [
                "Two flocks: $463$ animals and $258$ animals. The picture below shows only their HUNDREDS bundles — $4$ against $2$.",
                "That is already enough. Four hundreds beat two hundreds, so $463 > 258$, and the tens and ones never need looking at.",
                "Why is that safe? Because the most the tens and ones can ever add is $99$, and the hundreds gap here is $200$. A smaller column can never overturn a bigger one.",
            ]), fig_cmp),
            workedset("Compare from the left",
                      "First column that differs wins the argument.", [
                wex("Which is greater, $463$ or $258$?",
                    ["Hundreds: $4$ against $2$.",
                     "Four beats two, so $463 > 258$.",
                     "The gap is $463 - 258 = 205$ — more than the $99$ that tens and ones could ever supply."],
                    "$463 > 258$",
                    ["463 > 258", "Eq(463 - 258, 205)", "205 > 99"]),
                wex("Which is greater, $198$ or $210$?",
                    ["Hundreds: $1$ against $2$.",
                     "Two beats one, so $210 > 198$.",
                     "The $9$ and $8$ in $198$ look big, but they sit in small columns."],
                    "$210 > 198$",
                    ["210 > 198", "Eq(210 - 198, 12)"]),
            ]),
            tryitset("Which is greater?", "Read the hundreds column first.", [
                tp("$372$ and $419$ — the greater is:",
                   ["$419$", "$372$", "they are equal"],
                   "Hundreds: $4$ beats $3$, so $419 > 372$. The $7$ in $372$ is the biggest digit on show but it only counts tens.",
                   ["419 > 372", "Eq(419 - 372, 47)"]),
                tp("$189$ and $91$ — the greater is:",
                   ["$189$", "$91$", "they are equal"],
                   "$189$ has a hundreds digit and $91$ has none, so $189 > 91$. A three-digit number always beats a two-digit one.",
                   ["189 > 91", "Eq(189 - 91, 98)"]),
                tp("The correct sign for $604$ and $640$ is:",
                   ["$604 < 640$", "$604 > 640$", "$604 = 640$"],
                   "The hundreds tie at $6$, so the tens decide: $0$ tens against $4$ tens, and $604 < 640$. The gap is $36$.",
                   ["604 < 640", "Eq(640 - 604, 36)"]),
            ]),
            tapq("Big digit, small column", "Which is greater, $349$ or $376$?",
                 ["$376$", "$349$", "they are equal", "you cannot tell"],
                 "The hundreds tie at $3$, so the TENS decide: $7$ tens ($70$) against $4$ tens ($40$), and $376 > 349$ by $27$. The lonely $9$ in $349$ is worth only $9$ because it sits in the ones column.",
                 ["376 > 349", "Eq(376 - 349, 27)", "70 > 40"]),
            funfact("Why the sign has a wide end",
                    "The $>$ and $<$ signs first appeared in a book of algebra about four hundred years ago, and the shape was chosen to be read at a glance: the wide, open end faces the bigger amount and the pinched point faces the smaller. In all that time nobody has improved on it — you can still tell which way it faces from across a room."),
            withfig(teach("Concept B", "Ordering a whole list", [
                "To put several numbers in order, sort them by hundreds first — the number line below does exactly that with $258$, $376$ and $463$.",
                "$258$ has $2$ hundreds, $376$ has $3$, $463$ has $4$, so smallest to largest is $258$, $376$, $463$. On the line they appear in that order left to right, which is what a number line is for.",
                "If two numbers shared their hundreds, you would separate just those two by their tens — the rest of the list would not move.",
            ]), fig_line),
            workedset("Put them in order", "Sort by hundreds; break ties by tens.", [
                wex("Order $258$, $463$, $376$ from smallest to largest.",
                    ["Hundreds: $2$, $4$, $3$.",
                     "Smallest hundreds first: $258$, then $376$, then $463$.",
                     "So $258 < 376 < 463$."],
                    "$258$, $376$, $463$",
                    ["258 < 376", "376 < 463"]),
                wex("Order $512$, $521$, $498$ from smallest to largest.",
                    ["$498$ has only $4$ hundreds, so it is smallest.",
                     "$512$ and $521$ tie at $5$ hundreds — compare tens: $1$ against $2$.",
                     "So $498 < 512 < 521$."],
                    "$498$, $512$, $521$",
                    ["498 < 512", "512 < 521", "Eq(521 - 512, 9)"]),
            ]),
            tryitset("Order the list", "Hundreds first, and only then the tens.", [
                tp("Smallest to largest: $307$, $73$, $370$.",
                   ["$73$, $307$, $370$", "$73$, $370$, $307$", "$307$, $370$, $73$"],
                   "$73$ has no hundreds at all, so it is smallest. Then $307$ and $370$ tie at $3$ hundreds and the tens decide: $0$ tens against $7$ tens, so $307 < 370$.",
                   ["73 < 307", "307 < 370", "Eq(370 - 307, 63)"]),
                tp("Largest to smallest: $645$, $654$, $564$.",
                   ["$654$, $645$, $564$", "$645$, $654$, $564$", "$564$, $654$, $645$"],
                   "$564$ has only $5$ hundreds, so it is smallest. $654$ and $645$ tie at $6$ hundreds; the tens decide, $5$ beating $4$, so $654 > 645$.",
                   ["654 > 645", "645 > 564", "Eq(654 - 645, 9)"]),
                tp("Which number sits BETWEEN $420$ and $480$?",
                   ["$455$", "$419$", "$482$"],
                   "$455$ has $4$ hundreds and $5$ tens, so $420 < 455 < 480$. $419$ falls just below the bottom and $482$ just above the top.",
                   ["420 < 455", "455 < 480", "419 < 420"]),
            ]),
            tapq("The deciding column", "For $728$ and $731$, which column settles it?",
                 ["the tens", "the hundreds", "the ones", "no column — they are equal"],
                 "The hundreds tie at $7$, so you move right: $2$ tens against $3$ tens, and that is where it ends — $728 < 731$. The ones never get a vote, even though $8$ is bigger than $1$.",
                 ["728 < 731", "Eq(731 - 728, 3)", "30 > 20"]),
            recap([
                "Compare from the LEFT: the first column where the digits differ decides.",
                "A bigger single digit means nothing on its own — $70$ beats $9$ because of the column it sits in.",
                "The wide end of $>$ or $<$ always faces the bigger number.",
                "To order a list, sort by hundreds and break any ties with the tens, then the ones.",
            ]),
            tip("When two numbers look confusing, write them one above the other with their columns lined up. The first place where the digits disagree is the answer, and it is impossible to miss when they are stacked."),
            tryitset("Chapter practice", "Left column first, every time.", [
                tp("The correct sign for $890$ and $908$ is:",
                   ["$890 < 908$", "$890 > 908$", "$890 = 908$"],
                   "Hundreds: $8$ against $9$, so $890 < 908$. The $9$ in $890$ is in the tens and cannot outrank a hundreds digit.",
                   ["890 < 908", "Eq(908 - 890, 18)"]),
                tp("Smallest to largest: $209$, $290$, $92$.",
                   ["$92$, $209$, $290$", "$92$, $290$, $209$", "$209$, $92$, $290$"],
                   "$92$ has no hundreds. Then $209$ and $290$ tie at $2$ hundreds, and the tens decide: $0$ against $9$, so $209 < 290$.",
                   ["92 < 209", "209 < 290", "Eq(290 - 209, 81)"]),
                tp("Which is the largest?",
                   ["$811$", "$799$", "$781$"],
                   "$811$ has $8$ hundreds while $799$ has only $7$, so $811$ leads despite its small tens and ones. Among the rest, $799 > 781$ on the tens.",
                   ["811 > 799", "799 > 781", "Eq(811 - 799, 12)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Comparing and Ordering\"",
                    "Comparing from the left is the same habit you used to read numbers aloud — the biggest column speaks first. It will still be the habit next year with thousands, and the year after with millions: the columns get more numerous, but the rule never changes.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Counting in Steps
# ==========================================================================

def lesson_counting_steps():
    fives = [(0, "0"), (5, "5"), (10, "10"), (15, "15"), (20, "20")]
    fig_fives = fig_numline(fives, lo=0, hi=20)
    fig_hundreds = fig_numline([(200, "200"), (300, "300"), (400, "400"),
                                (500, "500")], lo=200, hi=500)
    fig_twos = fig_groups((2, "step 1", C_ACCENT), (2, "step 2", C_ACCENT),
                          (2, "step 3", C_ACCENT), (2, "step 4", C_ACCENT))
    return {
        "slug": "counting-in-steps",
        "title": "Counting in Steps",
        "concreteComparison": (
            "Nobody counts a stack of $100$-tögrög notes one by one. They "
            "count $100$, $200$, $300$ — one note, one jump. Counting in "
            "steps is counting with bigger feet, and the endings of the "
            "numbers tell you at once whether your feet are landing where "
            "they should."),
        "objective": (
            "Count on and back in steps of $2$, $5$, $10$ and $100$, "
            "continue a step pattern, and use the endings of the numbers "
            "to check that a count is right."),
        "concept": [
            "**A step count adds the same amount every time.** Counting "
            "in fives from $0$ gives $0, 5, 10, 15, 20$ — each number is "
            "the one before plus $5$. The list is really a repeated "
            "addition written out.",
            "**Each step size leaves its own fingerprint.** Counting in "
            "twos from an even number gives only even endings — $0, 2, 4, "
            "6, 8$. Counting in fives gives endings that alternate $5, 0, "
            "5, 0$. Counting in tens keeps the ones digit frozen. If your "
            "ending breaks the pattern, you have miscounted.",
            "**Counting in hundreds moves one column only.** From $200$, "
            "counting on in hundreds gives $300, 400, 500$ — the tens and "
            "ones never move, because you are adding whole bundles of a "
            "hundred and nothing else.",
        ],
        "keyIdea": (
            "Every step count is repeated addition, and every step size "
            "leaves a pattern in the digits — so the pattern is a free "
            "check on whether your count is right."),
        "facts": [
            {"title": "Fives alternate their endings",
             "latex": "0,\\ 5,\\ 10,\\ 15,\\ 20",
             "explanation": "Counting in fives from 0, the ones digit goes 0, 5, 0, 5 forever."},
            {"title": "Hundreds move one column",
             "latex": "200 + 100 = 300",
             "explanation": "Adding a hundred changes the hundreds digit and leaves the tens and ones untouched."},
        ],
        "workedExamples": [
            {"id": "g3nt-l4-we1",
             "statement": "Count on in fives from $0$, five steps. What do you notice about the endings?",
             "note": "Add $5$ each time and watch the last digit.",
             "solution": ("$0, 5, 10, 15, 20$ — five steps of five, and "
                          "$5 \\times 5 = 25$ would be the next one. The endings "
                          "run $0, 5, 0, 5, 0$: every count in fives from zero "
                          "ends in a $0$ or a $5$, never anything else."),
             "badges": [{"text": "core"}],
             "check": ["Eq(0 + 5, 5)", "Eq(15 + 5, 20)", "Eq(5*5, 25)",
                       "Eq(Mod(20, 5), 0)"]},
            {"id": "g3nt-l4-we2",
             "statement": "Count on in hundreds from $246$, three steps.",
             "note": "Only the hundreds column moves.",
             "solution": ("$246, 346, 446, 546$. The tens and ones stay at $4$ "
                          "and $6$ the whole way, because each step adds one "
                          "whole bundle of a hundred and touches nothing else: "
                          "$246 + 300 = 546$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(246 + 100, 346)", "Eq(246 + 300, 546)",
                       "Eq(Mod(546, 100), Mod(246, 100))"]},
        ],
        "commonMistakes": [
            {"text": "Losing a step in the middle of a count — going 5, 10, 20, 25.",
             "correction": "Check the gaps, not just the numbers: 10 to 20 is a jump of 10, which is two steps of five at once. The 15 was skipped.",
             "authored": True},
            {"text": "Changing the tens digit when counting on in hundreds — going 246, 356, 466.",
             "correction": "A step of 100 adds a whole hundreds bundle and nothing else, so the tens and ones must stay frozen: 246, 346, 446.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3nt-l4-t1",
             "statement": "Count on in tens from $370$, four steps.",
             "solution": ("$380, 390, 400, 410$. The ones digit stays $0$ "
                          "throughout, and $370 + 40 = 410$."),
             "check": ["Eq(370 + 10, 380)", "Eq(370 + 40, 410)",
                       "Eq(Mod(410, 10), 0)"]},
            {"id": "g3nt-l4-t2",
             "statement": "Count BACK in fives from $30$, four steps.",
             "solution": ("$25, 20, 15, 10$. Each step subtracts $5$, so after "
                          "four steps you have gone down $20$: $30 - 20 = 10$."),
             "check": ["Eq(30 - 5, 25)", "Eq(30 - 20, 10)", "Eq(4*5, 20)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counting with bigger feet", [
                "The number line below marks a count in fives from $0$: $0, 5, 10, 15, 20$. Every jump is the same size.",
                "That is what a step count IS — repeated addition, written as a list. Five steps of five have carried you to $20$, and one more would reach $5 \\times 5 = 25$.",
                "Look at the last digits: $0, 5, 0, 5, 0$. Counting in fives from zero can only ever end in a $0$ or a $5$, so an answer ending in $3$ is wrong before you check anything else.",
            ]), fig_fives),
            workedset("Take the steps", "Add the step size, then check the ending.", [
                wex("Count on in fives from $0$, five steps.",
                    ["$0, 5, 10, 15, 20$.",
                     "Each number is the last plus $5$.",
                     "Endings run $0, 5, 0, 5, 0$ — the fives fingerprint."],
                    "$0, 5, 10, 15, 20$",
                    ["Eq(0 + 5, 5)", "Eq(15 + 5, 20)", "Eq(Mod(20, 5), 0)"]),
                wex("Count on in twos from $8$, four steps.",
                    ["$10, 12, 14, 16$.",
                     "Four steps of two is $4 \\times 2 = 8$ altogether.",
                     "$8 + 8 = 16$ ✓, and every number stayed even."],
                    "$10, 12, 14, 16$",
                    ["Eq(8 + 2, 10)", "Eq(4*2, 8)", "Eq(8 + 8, 16)",
                     "Eq(Mod(16, 2), 0)"]),
            ]),
            tryitset("Continue the count", "Same jump every time — check the gaps.", [
                withfig(tp("Four steps of $2$ are drawn below. Altogether they add:",
                   ["$8$", "$6$", "$24$"],
                   "Four groups of two: $2 + 2 + 2 + 2 = 8$, which is $4 \\times 2$. Counting the groups instead of the dots gives $4$; multiplying the labels gives $24$, which counts nothing in the picture.",
                   ["Eq(2 + 2 + 2 + 2, 8)", "Eq(4*2, 8)"]), fig_twos),
                tp("Counting in fives: $35, 40, 45, \\ldots$ The next number is:",
                   ["$50$", "$46$", "$55$"],
                   "Each step adds $5$: $45 + 5 = 50$. Adding $1$ gives $46$ and jumping two steps at once gives $55$.",
                   ["Eq(45 + 5, 50)", "Eq(45 + 10, 55)"]),
                tp("Which list is a correct count in tens?",
                   ["$260, 270, 280$", "$260, 270, 290$", "$260, 280, 300$"],
                   "Every gap must be exactly $10$: $260, 270, 280$ ✓. The second list jumps $20$ at the end, and the third jumps $20$ every time.",
                   ["Eq(270 - 260, 10)", "Eq(290 - 270, 20)"]),
            ]),
            tapq("The broken pattern", "A count in fives reads $10, 15, 20, 30$. Which number is wrong?",
                 ["$30$ — it should be $25$", "$15$ — it should be $14$",
                  "$20$ — it should be $21$", "nothing is wrong"],
                 "The gaps should all be $5$, but $20$ to $30$ is a gap of $10$ — two steps taken at once. The missing number is $20 + 5 = 25$.",
                 ["Eq(30 - 20, 10)", "Eq(20 + 5, 25)", "Eq(15 - 10, 5)"]),
            funfact("Why shepherds count in fives",
                    "A hand has five fingers, which is why counting in fives is older than writing: one full hand, then another. Mongolian herders checking a flock still count in bundles rather than one at a time, for the same reason you will — bigger feet mean fewer chances to lose your place."),
            withfig(teach("Concept B", "Stepping in hundreds", [
                "The line below counts on in hundreds: $200, 300, 400, 500$. Each jump is a whole bundle of one hundred.",
                "Because a hundred is exactly one bundle, only the HUNDREDS digit changes. Start at $246$ and step in hundreds and you get $346, 446, 546$ — the $4$ and the $6$ never move.",
                "That makes hundred-steps the easiest count of all: read the hundreds digit, add one to it, and copy the rest of the number straight down.",
            ]), fig_hundreds),
            workedset("Hundred steps", "One column moves; the others are copied.", [
                wex("Count on in hundreds from $246$, three steps.",
                    ["$346$: the hundreds digit goes from $2$ to $3$.",
                     "$446$, then $546$ — tens and ones stay $4$ and $6$.",
                     "Check: $246 + 300 = 546$ ✓."],
                    "$346, 446, 546$",
                    ["Eq(246 + 100, 346)", "Eq(246 + 300, 546)"]),
                wex("Count BACK in hundreds from $780$, two steps.",
                    ["$680$: one bundle of a hundred removed.",
                     "$580$: another one gone.",
                     "Check: $780 - 200 = 580$ ✓, and the $8$ and $0$ never moved."],
                    "$680, 580$",
                    ["Eq(780 - 100, 680)", "Eq(780 - 200, 580)"]),
            ]),
            tryitset("Step by hundreds", "Change the hundreds digit; copy the rest.", [
                tp("Counting on in hundreds from $317$, the next number is:",
                   ["$417$", "$327$", "$318$"],
                   "One whole hundred is added, so only the hundreds digit moves: $317 + 100 = 417$. $327$ adds a ten and $318$ adds a one.",
                   ["Eq(317 + 100, 417)", "Eq(317 + 10, 327)"]),
                tp("$594, 494, 394, \\ldots$ — this count is going:",
                   ["back in hundreds", "back in tens", "on in hundreds"],
                   "Each number is $100$ less than the one before: $594 - 100 = 494$. The count is going backwards, so the next number would be $294$.",
                   ["Eq(594 - 100, 494)", "Eq(394 - 100, 294)"]),
                tp("Start at $150$ and take four steps of $100$. You land on:",
                   ["$550$", "$190$", "$450$"],
                   "Four hundreds is $4 \\times 100 = 400$, so $150 + 400 = 550$. Landing on $450$ means only three steps were taken.",
                   ["Eq(4*100, 400)", "Eq(150 + 400, 550)", "Eq(150 + 300, 450)"]),
            ]),
            tapq("Which column moved?", "A count goes $431, 441, 451$. What is the step?",
                 ["$10$", "$1$", "$100$", "$11$"],
                 "Only the tens digit is changing — $3$, then $4$, then $5$ — so each step adds one ten: $441 - 431 = 10$. A step of $100$ would move the leading digit instead.",
                 ["Eq(441 - 431, 10)", "Eq(451 - 441, 10)"]),
            recap([
                "A step count adds the same amount every time — it is repeated addition in a list.",
                "Twos keep every number even; fives end in $0$ or $5$; tens freeze the ones digit.",
                "A step of $100$ changes only the hundreds digit: $246, 346, 446$.",
                "If an ending breaks the pattern, the count is wrong — check the gaps, not the numbers.",
            ]),
            tip("Count the GAPS out loud, not the numbers: \"plus five, plus five, plus five\". A skipped step is almost impossible to hear when you say the numbers, and almost impossible to miss when you say the jumps."),
            tryitset("Chapter practice", "Same jump, every time.", [
                tp("Counting on in twos from $46$: $48, 50, \\ldots$ The next is:",
                   ["$52$", "$51$", "$60$"],
                   "Every step adds $2$ and every number stays even: $50 + 2 = 52$. An odd answer like $51$ breaks the twos pattern immediately.",
                   ["Eq(50 + 2, 52)", "Eq(Mod(52, 2), 0)"]),
                tp("$725, 715, 705, \\ldots$ The next number is:",
                   ["$695$", "$700$", "$605$"],
                   "The count is going back in tens: $705 - 10 = 695$. Note the hundreds digit finally changes here, because $705$ has no tens left to give.",
                   ["Eq(715 - 10, 705)", "Eq(705 - 10, 695)"]),
                tp("Six steps of $10$ from $340$ land on:",
                   ["$400$", "$346$", "$940$"],
                   "Six tens is $6 \\times 10 = 60$, so $340 + 60 = 400$. Adding six ONES would give $346$ instead.",
                   ["Eq(6*10, 60)", "Eq(340 + 60, 400)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Counting in Steps\"",
                    "Counting in twos, fives and tens is the ground floor of the times tables you meet later this year — every step count you can say fluently is a row of a table you will barely have to learn. The steps became facts while you were just counting.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Rounding to the Nearest Ten
# ==========================================================================

def lesson_rounding():
    fig_r47 = fig_numline([(40, "40"), (47, "47"), (50, "50")], lo=40, hi=50)
    fig_r62 = fig_numline([(60, "60"), (62, "62"), (70, "70")], lo=60, hi=70)
    fig_r35 = fig_numline([(30, "30"), (35, "35"), (40, "40")], lo=30, hi=40)
    return {
        "slug": "rounding-to-the-nearest-ten",
        "title": "Rounding to the Nearest Ten",
        "concreteComparison": (
            "Asked how far the well is, nobody says \"$47$ steps\". They "
            "say \"about $50$\". Rounding is the polite version of a "
            "number — close enough to be useful, short enough to "
            "remember. The only question is which ten the number is "
            "nearer to."),
        "objective": (
            "Round a two- or three-digit number to the nearest ten by "
            "finding the tens on either side, decide ties with the "
            "halfway rule, and say when a rounded answer is good enough."),
        "concept": [
            "**Find the two tens the number sits between.** $47$ lies "
            "between $40$ and $50$. Those are the only two answers "
            "possible, so rounding is always a choice between exactly "
            "two neighbours.",
            "**Go to the nearer one.** $47$ is $7$ away from $40$ and "
            "only $3$ away from $50$, so it rounds to $50$. You can read "
            "this straight off the ones digit: $1, 2, 3, 4$ are nearer "
            "the ten below; $6, 7, 8, 9$ are nearer the ten above.",
            "**An exact half is a tie, so we agree on a rule.** $35$ is "
            "$5$ from $30$ and $5$ from $40$ — genuinely tied. The rule "
            "everyone uses is round UP, so $35$ becomes $40$. It is a "
            "convention, not a discovery: we pick one so that two people "
            "rounding the same number always agree.",
        ],
        "keyIdea": (
            "Rounding to the nearest ten means choosing between the two "
            "tens a number sits between — the nearer one wins, and an "
            "exact halfway goes up by agreement."),
        "facts": [
            {"title": "Nearer wins",
             "latex": "47 \\to 50",
             "explanation": "47 is 3 from 50 but 7 from 40, so 50 is nearer."},
            {"title": "Halfway rounds up",
             "latex": "35 \\to 40",
             "explanation": "35 is 5 from each neighbour; the agreed rule sends an exact half upward."},
        ],
        "workedExamples": [
            {"id": "g3nt-l5-we1",
             "statement": "Round $47$ to the nearest ten.",
             "note": "Name both neighbours, then measure the distance to each.",
             "solution": ("$47$ sits between $40$ and $50$. It is $47 - 40 = 7$ "
                          "above the lower ten and $50 - 47 = 3$ below the upper "
                          "one. Three is less than seven, so $50$ is nearer: "
                          "$47$ rounds to $50$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(47 - 40, 7)", "Eq(50 - 47, 3)", "3 < 7"]},
            {"id": "g3nt-l5-we2",
             "statement": "Round $362$ to the nearest ten.",
             "note": "Only the last two digits do any work.",
             "solution": ("$362$ sits between $360$ and $370$. It is $2$ above "
                          "$360$ and $8$ below $370$, so $360$ is nearer and "
                          "$362$ rounds to $360$. The hundreds digit never "
                          "moved — rounding to tens only ever disturbs the end "
                          "of the number."),
             "badges": [{"text": "core"}],
             "check": ["Eq(362 - 360, 2)", "Eq(370 - 362, 8)", "2 < 8"]},
        ],
        "commonMistakes": [
            {"text": "Rounding down whenever the ones digit is small-looking, including 5 — turning 35 into 30.",
             "correction": "35 is exactly halfway, and the agreed rule sends halves UP: 35 rounds to 40. The rule exists so two people never round the same number two different ways.",
             "authored": True},
            {"text": "Changing the hundreds digit when rounding to the nearest ten — turning 362 into 400.",
             "correction": "Rounding to the nearest TEN only chooses between 360 and 370. 400 is the answer to a different question — the nearest hundred.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3nt-l5-t1",
             "statement": "Round $62$ to the nearest ten and show both distances.",
             "solution": ("$62$ is between $60$ and $70$. It is $2$ above $60$ "
                          "and $8$ below $70$, so it rounds to $60$."),
             "check": ["Eq(62 - 60, 2)", "Eq(70 - 62, 8)", "2 < 8"]},
            {"id": "g3nt-l5-t2",
             "statement": "Round $285$ to the nearest ten.",
             "solution": ("$285$ sits between $280$ and $290$, exactly $5$ from "
                          "each. The halfway rule rounds up, so the answer is "
                          "$290$."),
             "check": ["Eq(285 - 280, 5)", "Eq(290 - 285, 5)", "Eq(285 + 5, 290)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Which ten is nearer?", [
                "The line below shows $47$ sitting between $40$ and $50$. Those two tens are the only possible answers — rounding is always a choice between two neighbours.",
                "Measure both gaps: $47 - 40 = 7$ down to $40$, and $50 - 47 = 3$ up to $50$. Three is the shorter walk, so $47$ rounds to $50$.",
                "You can shortcut the measuring by reading the ones digit. A $7$ means the number is past the middle of its ten, so it goes up. Ones of $1, 2, 3, 4$ go down; $6, 7, 8, 9$ go up.",
            ]), fig_r47),
            workedset("Round to the nearest ten",
                      "Name both neighbours, compare the two gaps.", [
                wex("Round $47$ to the nearest ten.",
                    ["Neighbours: $40$ and $50$.",
                     "Gaps: $47 - 40 = 7$ and $50 - 47 = 3$.",
                     "$3 < 7$, so $47$ rounds to $50$."],
                    "$50$",
                    ["Eq(47 - 40, 7)", "Eq(50 - 47, 3)", "3 < 7"]),
                wex("Round $83$ to the nearest ten.",
                    ["Neighbours: $80$ and $90$.",
                     "Gaps: $83 - 80 = 3$ and $90 - 83 = 7$.",
                     "$3 < 7$, so $83$ rounds to $80$."],
                    "$80$",
                    ["Eq(83 - 80, 3)", "Eq(90 - 83, 7)", "3 < 7"]),
            ]),
            tryitset("Up or down?", "Compare the two gaps, or read the ones digit.", [
                withfig(tp("Rounded to the nearest ten, $62$ becomes:",
                   ["$60$", "$70$", "$62$"],
                   "$62$ is only $2$ above $60$ but $8$ below $70$, so $60$ is nearer. A ones digit of $2$ always sends a number down.",
                   ["Eq(62 - 60, 2)", "Eq(70 - 62, 8)", "2 < 8"]), fig_r62),
                tp("Rounded to the nearest ten, $78$ becomes:",
                   ["$80$", "$70$", "$79$"],
                   "$78$ is $8$ above $70$ and only $2$ below $80$, so it rounds up to $80$. A rounded answer must always BE a ten, which rules out $79$.",
                   ["Eq(78 - 70, 8)", "Eq(80 - 78, 2)", "2 < 8"]),
                tp("Which number rounds to $50$?",
                   ["$46$", "$44$", "$55$"],
                   "$46$ is $4$ from $50$ and $6$ from $40$, so it rounds up to $50$. $44$ is nearer $40$, and $55$ is a halfway case that rounds up to $60$.",
                   ["Eq(50 - 46, 4)", "Eq(46 - 40, 6)", "4 < 6"]),
            ]),
            tapq("Reading the ones digit", "A number ends in $3$. Rounded to the nearest ten it goes:",
                 ["down, to the ten below", "up, to the ten above",
                  "nowhere — it stays put", "it depends on the hundreds digit"],
                 "A ones digit of $3$ means the number is only $3$ past its lower ten but $7$ short of the upper one, so the lower ten is always nearer. For example $83 \\to 80$, and $3 < 7$ every time.",
                 ["Eq(83 - 80, 3)", "Eq(90 - 83, 7)", "3 < 7"]),
            funfact("Rounding is a promise about size",
                    "Rounding to the nearest ten can never move a number by more than $5$, no matter how big the number is. That is the guarantee that makes it safe: \"about $350$ sheep\" might be $345$ or $354$, but it is certainly not $400$. Rounding trades a little exactness for a lot of memorability, and it tells you in advance exactly how much it traded."),
            withfig(teach("Concept B", "The halfway rule", [
                "The line below shows the awkward case: $35$ sits exactly in the middle, $5$ from $30$ and $5$ from $40$. Neither ten is nearer.",
                "So a rule is agreed rather than discovered: an exact half rounds UP. $35$ becomes $40$, $285$ becomes $290$, $5$ becomes $10$.",
                "Why agree at all? Because rounding is for sharing numbers. If you rounded halves down and your friend rounded them up, the same flock would be \"about $30$\" and \"about $40$\" on the same day. One rule, one answer.",
            ]), fig_r35),
            workedset("Halves and three-digit numbers",
                      "The last two digits do the work; a $5$ goes up.", [
                wex("Round $35$ to the nearest ten.",
                    ["Neighbours: $30$ and $40$.",
                     "Gaps: $35 - 30 = 5$ and $40 - 35 = 5$ — a tie.",
                     "The halfway rule rounds up: $40$."],
                    "$40$",
                    ["Eq(35 - 30, 5)", "Eq(40 - 35, 5)", "Eq(35 + 5, 40)"]),
                wex("Round $362$ to the nearest ten.",
                    ["Neighbours: $360$ and $370$.",
                     "Gaps: $2$ down, $8$ up.",
                     "$2 < 8$, so $362$ rounds to $360$ — the hundreds digit never moves."],
                    "$360$",
                    ["Eq(362 - 360, 2)", "Eq(370 - 362, 8)", "2 < 8"]),
            ]),
            tryitset("Three digits and ties", "Look only at the last two digits.", [
                withfig(tp("Rounded to the nearest ten, $35$ becomes:",
                   ["$40$", "$30$", "$35$"],
                   "$35$ is exactly $5$ from both neighbours, and the agreed rule sends an exact half up: $40$. Rounding down to $30$ is the single most common slip here.",
                   ["Eq(40 - 35, 5)", "Eq(35 - 30, 5)"]), fig_r35),
                tp("Rounded to the nearest ten, $604$ becomes:",
                   ["$600$", "$610$", "$700$"],
                   "$604$ lies between $600$ and $610$, and is only $4$ above $600$: it rounds down. $700$ answers a different question — the nearest hundred.",
                   ["Eq(604 - 600, 4)", "Eq(610 - 604, 6)", "4 < 6"]),
                tp("Rounded to the nearest ten, $297$ becomes:",
                   ["$300$", "$290$", "$200$"],
                   "$297$ sits between $290$ and $300$, just $3$ below $300$, so it rounds up — and the hundreds digit changes as a side effect, because $300$ happens to be a ten as well.",
                   ["Eq(300 - 297, 3)", "Eq(297 - 290, 7)", "3 < 7"]),
            ]),
            tapq("How far can rounding move a number?", "Rounded to the nearest ten, at most how far does a number move?",
                 ["$5$", "$10$", "$9$", "as far as it needs to"],
                 "The two neighbouring tens are $10$ apart, so the furthest any number can be from BOTH is half of that: $5$. That is the case of an exact half, like $35 \\to 40$, which moves exactly $5$.",
                 ["Eq(40 - 35, 5)", "Eq(40 - 30, 10)", "5 < 10"]),
            recap([
                "A number rounds to one of the two tens it sits between — never anywhere else.",
                "The nearer ten wins; measure both gaps if you are unsure.",
                "Ones digits $1$–$4$ go down and $6$–$9$ go up; an exact $5$ goes UP by agreement.",
                "Rounding to the nearest ten can never move a number more than $5$.",
            ]),
            tip("Sketch the little stretch of number line between the two tens and mark your number on it. Rounding stops being a rule to remember and becomes something you can simply see."),
            tryitset("Chapter practice", "Two neighbours, two gaps, nearer wins.", [
                tp("Rounded to the nearest ten, $148$ becomes:",
                   ["$150$", "$140$", "$100$"],
                   "$148$ is $8$ above $140$ and only $2$ below $150$, so it rounds up. $100$ would be the nearest hundred, a different question.",
                   ["Eq(150 - 148, 2)", "Eq(148 - 140, 8)", "2 < 8"]),
                tp("Rounded to the nearest ten, $415$ becomes:",
                   ["$420$", "$410$", "$400$"],
                   "$415$ is exactly halfway between $410$ and $420$, and the halfway rule rounds up: $420$.",
                   ["Eq(420 - 415, 5)", "Eq(415 - 410, 5)"]),
                tp("Which of these does NOT round to $70$?",
                   ["$64$", "$68$", "$73$"],
                   "$64$ is $4$ above $60$ and $6$ below $70$, so it rounds DOWN to $60$. Both $68$ and $73$ are within $5$ of $70$ and round there.",
                   ["Eq(64 - 60, 4)", "Eq(70 - 64, 6)", "4 < 6"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Rounding to the Nearest Ten\" — and the topic",
                    "Hundreds, tens and ones; words and digits; comparing; step counting; rounding. Every one of them turned on the same question — which column is this digit in? Next comes adding and subtracting these numbers, and the columns do that job too.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = bundles(5, 0, 8)
    return [
        withprobfig(prob("g3nt-pr1", "The picture shows the bundles for a number. Write it in digits and in words.",
             "Five hundreds, no tens, eight ones: $500 + 0 + 8 = 508$, read \"five hundred and eight\". The empty tens column still needs its $0$ — without it the number would read $58$.",
             ["Eq(500 + 0 + 8, 508)", "Eq(508 - 58, 450)"]), fig_pr1),
        prob("g3nt-pr2", "In $737$, what is each $7$ worth? How much bigger is one than the other?",
             "The left $7$ is in the hundreds column, worth $700$; the right $7$ is in the ones column, worth $7$. The difference is $700 - 7 = 693$ — same digit, wildly different jobs.",
             ["Eq(700 + 30 + 7, 737)", "Eq(700 - 7, 693)"]),
        prob("g3nt-pr3", "Write \"nine hundred and six\" in digits, and explain what goes wrong if the zero is left out.",
             "$900 + 0 + 6 = 906$. Leaving the zero out writes $96$, which drops the $9$ from the hundreds column to the tens — a loss of $906 - 96 = 810$.",
             ["Eq(900 + 0 + 6, 906)", "Eq(906 - 96, 810)"]),
        prob("g3nt-pr4", "Put $415$, $451$ and $145$ in order from smallest to largest, saying which column decides each comparison.",
             "$145$ has only $1$ hundred, so it is smallest. $415$ and $451$ tie at $4$ hundreds, so the tens decide: $1$ ten against $5$ tens, giving $415 < 451$. The order is $145$, $415$, $451$.",
             ["145 < 415", "415 < 451", "Eq(451 - 415, 36)"]),
        prob("g3nt-pr5", "Count on in hundreds from $189$, three steps. Which digits move and which stay?",
             "$289$, $389$, $489$. Only the hundreds digit moves, because each step adds one whole bundle of a hundred: $189 + 300 = 489$, and the $8$ and $9$ are untouched.",
             ["Eq(189 + 100, 289)", "Eq(189 + 300, 489)",
              "Eq(Mod(489, 100), Mod(189, 100))"]),
        prob("g3nt-pr6", "A count in fives reads $60, 65, 75, 80$. Find the mistake and fix it.",
             "The gaps should all be $5$, but $65$ to $75$ is a gap of $10$ — two steps in one. The missing number is $65 + 5 = 70$, so the correct count is $60, 65, 70, 75, 80$.",
             ["Eq(75 - 65, 10)", "Eq(65 + 5, 70)", "Eq(80 - 75, 5)"]),
        prob("g3nt-pr7", "Round $246$ and $245$ to the nearest ten, and say why they give different answers.",
             "$246$ is $6$ above $240$ and $4$ below $250$, so it rounds up to $250$. $245$ is exactly $5$ from each neighbour — a tie — and the halfway rule also sends it up, to $250$. Both land on $250$, but for different reasons: one is nearer, the other is a tie decided by the rule.",
             ["Eq(246 - 240, 6)", "Eq(250 - 246, 4)", "Eq(245 - 240, 5)",
              "Eq(250 - 245, 5)"]),
        prob("g3nt-pr8", "Bat says $99$ is bigger than $101$ because it has bigger digits. Explain his mistake with columns.",
             "$99$ has no hundreds at all: $90 + 9$. $101$ has one whole hundred: $100 + 0 + 1$. Comparing from the left, the hundreds column decides immediately, so $101 > 99$ — by $2$. Big digits in small columns lose to small digits in big ones.",
             ["Eq(90 + 9, 99)", "Eq(100 + 0 + 1, 101)", "101 > 99",
              "Eq(101 - 99, 2)"]),
    ]


def test_bank():
    return [
        prob("g3nt-x1", "Split $604$ into hundreds, tens and ones, then say what the $0$ is doing.",
             "$600 + 0 + 4 = 604$: six hundreds, zero tens, four ones. The $0$ marks an empty tens column and keeps the $6$ in the hundreds; without it the number would read $64$, smaller by $540$.",
             ["Eq(600 + 0 + 4, 604)", "Eq(604 - 64, 540)"]),
        prob("g3nt-x2", "Write \"three hundred and nineteen\" in digits, and explain why it is not $391$.",
             "\"Nineteen\" is $1$ ten and $9$ ones, so the number is $300 + 10 + 9 = 319$. Hearing \"nine\" as the tens gives $391$ instead, which is $72$ too big.",
             ["Eq(300 + 10 + 9, 319)", "Eq(391 - 319, 72)"]),
        prob("g3nt-x3", "Compare $508$ and $580$, naming the column that decides.",
             "The hundreds tie at $5$, so the tens decide: $0$ tens against $8$ tens. So $508 < 580$, a gap of $72$. The ones column never gets a vote.",
             ["508 < 580", "Eq(580 - 508, 72)", "80 > 0"]),
        prob("g3nt-x4", "Order $270$, $207$, $72$ and $702$ from largest to smallest.",
             "By hundreds: $702$ has $7$, then $270$ and $207$ tie at $2$, and $72$ has none. The tie breaks on tens — $7$ tens against $0$ tens — so the order is $702$, $270$, $207$, $72$.",
             ["702 > 270", "270 > 207", "207 > 72", "Eq(270 - 207, 63)"]),
        prob("g3nt-x5", "Count back in tens from $312$, four steps. What happens to the hundreds digit and why?",
             "$302$, $292$, $282$, $272$. The hundreds digit drops from $3$ to $2$ at the second step, because $302$ has no tens left to give — the next ten has to come out of a hundreds bundle. Check: $312 - 40 = 272$.",
             ["Eq(312 - 10, 302)", "Eq(302 - 10, 292)", "Eq(312 - 40, 272)"]),
        prob("g3nt-x6", "Round $75$, $74$ and $175$ to the nearest ten, and state the rule each one used.",
             "$75$ is a tie, $5$ from both $70$ and $80$, so the halfway rule sends it up to $80$. $74$ is $4$ above $70$ and $6$ below $80$, so nearness sends it down to $70$. $175$ is a tie again and rounds up to $180$.",
             ["Eq(80 - 75, 5)", "Eq(75 - 70, 5)", "Eq(74 - 70, 4)",
              "Eq(80 - 74, 6)", "Eq(180 - 175, 5)"]),
    ]


def main():
    topic = {
        "slug": "numbers-to-1000",
        "title": "Numbers to 1000",
        "grade": 3,
        "status": "published",
        "blurb": ("Hundreds, tens and ones as bundles you could tie, reading "
                  "and writing three-digit numbers in words and digits, "
                  "comparing and ordering from the left, counting in steps of "
                  "2, 5, 10 and 100, and rounding to the nearest ten."),
        "lessons": [
            lesson_hundreds_tens_ones(),
            lesson_reading_writing(),
            lesson_comparing_ordering(),
            lesson_counting_steps(),
            lesson_rounding(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "numbers-to-1000.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
