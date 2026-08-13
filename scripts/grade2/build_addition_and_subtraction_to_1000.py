#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Addition & Subtraction to 1000.

Adding and subtracting whole hundreds and tens in the head (one column
moves, the rest are copied); column addition where ten ones trade up for
a ten; column subtraction where a ten is broken back into ten ones; fact
families that turn every addition into two subtractions and back; and
choosing the right operation from the words of a problem.

Through-line: TEN OF ANY COLUMN IS ONE OF THE NEXT. Carrying is that
trade going up, borrowing is the same trade coming back down, and a fact
family is the trade left alone while you look at it from a different
side.

Grade discipline: everything inside 1000, at most ONE regroup per
calculation (Grade 4 owns the multi-regroup algorithm), no negatives,
no decimals. Every subtraction carries a receipt — the answer added back
to what was taken away must return the original — and every check is
sympy-asserted BEFORE the JSON is written.

Run: python3 scripts/grade2/build_addition_and_subtraction_to_1000.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, workedset, write_topic,
                     fig_groups, fig_numline, C_ACCENT, C_WARM, C_GREEN)


def cols(h, t, o, who):
    """One number's columns, labelled with whose number it is — used to put
    two addends side by side so a child can see which columns meet."""
    return ((h, "%s: %d hundreds" % (who, h), C_ACCENT),
            (t, "%s: %d tens" % (who, t), C_WARM),
            (o, "%s: %d ones" % (who, o), C_GREEN))


# ==========================================================================
# Lesson 1 — Adding Tens and Hundreds in Your Head
# ==========================================================================

def lesson_mental():
    fig_hundreds = fig_numline([(240, "240"), (340, "340"), (440, "440"),
                                (540, "540")], lo=240, hi=540)
    fig_tens = fig_numline([(360, "360"), (370, "370"), (380, "380"),
                            (390, "390")], lo=360, hi=390)
    fig_bridge = fig_numline([(280, "280"), (300, "300"), (320, "320")],
                             lo=280, hi=320)
    return {
        "slug": "adding-tens-and-hundreds",
        "title": "Adding Tens and Hundreds",
        "concreteComparison": (
            "A shopkeeper adding $300$ tögrög to a $240$ tögrög bill does "
            "not reach for a pencil. Three more hundred-notes go on the "
            "pile, the tens and ones are untouched, and the answer is "
            "$540$. Whole hundreds and whole tens can be added in the "
            "head, because they only ever disturb ONE column."),
        "objective": (
            "Add and subtract whole hundreds and whole tens mentally, "
            "explain which column moves, and handle the case where a "
            "column fills up and spills into the next one."),
        "concept": [
            "**A whole hundred moves only the hundreds digit.** $240 + "
            "300$: three more hundreds bundles join the two already "
            "there, giving five. The $4$ tens and $0$ ones are not "
            "involved at all, so the answer is $540$.",
            "**A whole ten moves only the tens digit** — as long as the "
            "tens column has room. $360 + 30$ makes $6 + 3 = 9$ tens, so "
            "the answer is $390$. Same idea, one column to the right.",
            "**When a column fills up, it spills into the next one.** "
            "$280 + 40$ would need $8 + 4 = 12$ tens, and a column only "
            "holds nine. Ten of those tens trade up for one hundred, "
            "leaving $2$ tens: the answer is $320$. Nothing was lost — "
            "$12$ tens and \"one hundred and two tens\" are the same "
            "amount.",
        ],
        "keyIdea": (
            "Adding a whole hundred or a whole ten changes just one "
            "column — and if that column would go past nine, ten of it "
            "trades up for one of the column to its left."),
        "facts": [
            {"title": "Hundreds keep to themselves",
             "latex": "240 + 300 = 540",
             "explanation": "Only the hundreds digit changes; the tens and ones are copied down."},
            {"title": "A full column trades up",
             "latex": "280 + 40 = 320",
             "explanation": "12 tens is one hundred and 2 tens — the ten extra tens become a hundred."},
        ],
        "workedExamples": [
            {"id": "g3as-l1-we1",
             "statement": "Work out $240 + 300$ in your head, and say which digits moved.",
             "note": "Count the hundreds bundles.",
             "solution": ("$2$ hundreds and $3$ hundreds make $5$ hundreds. The "
                          "tens stay at $4$ and the ones stay at $0$, because "
                          "nothing was added to them. So $240 + 300 = 540$ — "
                          "only the leading digit changed."),
             "badges": [{"text": "core"}],
             "check": ["Eq(240 + 300, 540)", "Eq(2 + 3, 5)",
                       "Eq(Mod(540, 100), Mod(240, 100))"]},
            {"id": "g3as-l1-we2",
             "statement": "Work out $280 + 40$ in your head.",
             "note": "Count the tens first — see whether they fit.",
             "solution": ("$8$ tens plus $4$ tens is $12$ tens, which is more "
                          "than one column can hold. Ten of those tens trade up "
                          "for one hundred, so the hundreds go from $2$ to $3$ "
                          "and $2$ tens are left: $280 + 40 = 320$. Check by "
                          "counting on from $280$ to $300$ ($20$) and then $20$ "
                          "more."),
             "badges": [{"text": "core"}],
             "check": ["Eq(280 + 40, 320)", "Eq(8 + 4, 12)",
                       "Eq(300 - 280, 20)", "Eq(300 + 20, 320)"]},
        ],
        "commonMistakes": [
            {"text": "Adding a hundred to the wrong column — turning 240 + 300 into 270.",
             "correction": "300 is three HUNDREDS bundles, so it lands in the hundreds column: 540. Landing it in the tens would be adding 30, not 300.",
             "authored": True},
            {"text": "Writing 12 in the tens column — answering 280 + 40 as 2120.",
             "correction": "A column holds a single digit. Twelve tens is one hundred and two tens, so the hundred moves left and a 2 stays behind: 320.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3as-l1-t1",
             "statement": "Work out $517 + 200$ and say which digits stayed still.",
             "solution": ("$5$ hundreds plus $2$ hundreds is $7$ hundreds, so the "
                          "answer is $717$. The $1$ and the $7$ never moved."),
             "check": ["Eq(517 + 200, 717)",
                       "Eq(Mod(717, 100), Mod(517, 100))"]},
            {"id": "g3as-l1-t2",
             "statement": "Work out $460 - 90$ in your head.",
             "solution": ("There are only $6$ tens but $9$ are needed, so one "
                          "hundred is broken back into $10$ tens: $16$ tens less "
                          "$9$ tens leaves $7$ tens, with $3$ hundreds. The "
                          "answer is $370$ — and the receipt is "
                          "$370 + 90 = 460$."),
             "check": ["Eq(460 - 90, 370)", "Eq(370 + 90, 460)",
                       "Eq(16 - 9, 7)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Whole hundreds move one digit", [
                "The line below steps in hundreds from $240$: $340$, $440$, $540$. Watch the tens and ones — they never budge.",
                "So $240 + 300$ is three of those steps at once: $2$ hundreds plus $3$ hundreds is $5$ hundreds, and the answer is $540$.",
                "That is why whole hundreds can be added in your head. There is only one digit to think about; the rest of the number is copied straight down.",
            ]), fig_hundreds),
            workedset("Add whole hundreds", "Count the hundreds; copy the rest.", [
                wex("Work out $240 + 300$.",
                    ["Hundreds: $2 + 3 = 5$.",
                     "Tens and ones are untouched: $4$ and $0$.",
                     "$240 + 300 = 540$."],
                    "$540$",
                    ["Eq(2 + 3, 5)", "Eq(240 + 300, 540)"]),
                wex("Work out $625 - 400$.",
                    ["Hundreds: $6 - 4 = 2$.",
                     "The $2$ tens and $5$ ones are untouched.",
                     "$625 - 400 = 225$, and the receipt is $225 + 400 = 625$."],
                    "$225$",
                    ["Eq(6 - 4, 2)", "Eq(625 - 400, 225)", "Eq(225 + 400, 625)"]),
            ]),
            tryitset("Hundreds in your head", "Only the leading digit moves.", [
                tp("$316 + 500$ is:",
                   ["$816$", "$366$", "$321$"],
                   "Five hundreds join three: $8$ hundreds, with $1$ ten and $6$ ones copied down. $366$ would be adding $50$, and $321$ adding $5$.",
                   ["Eq(316 + 500, 816)", "Eq(316 + 50, 366)"]),
                tp("$780 - 300$ is:",
                   ["$480$", "$750$", "$477$"],
                   "Seven hundreds less three is four: $480$, and the receipt $480 + 300 = 780$ confirms it. $750$ subtracts only $30$.",
                   ["Eq(780 - 300, 480)", "Eq(480 + 300, 780)"]),
                tp("Which sum leaves the tens and ones completely unchanged?",
                   ["$142 + 700$", "$142 + 70$", "$142 + 7$"],
                   "Only a whole HUNDRED avoids the smaller columns: $142 + 700 = 842$, still $4$ tens and $2$ ones. Adding $70$ changes the tens and adding $7$ changes the ones.",
                   ["Eq(142 + 700, 842)", "Eq(142 + 70, 212)",
                    "Eq(142 + 7, 149)"]),
            ]),
            tapq("Which column did it land in?", "Sara works out $240 + 300$ and writes $270$. What went wrong?",
                 ["she added $3$ tens instead of $3$ hundreds",
                  "she forgot to add anything",
                  "she added $3$ ones instead of $3$ hundreds",
                  "nothing — $270$ is right"],
                 "$270$ is $240 + 30$, so the three landed in the tens column. Three HUNDREDS gives $240 + 300 = 540$ — the two answers differ by $270$.",
                 ["Eq(240 + 30, 270)", "Eq(240 + 300, 540)",
                  "Eq(540 - 270, 270)"]),
            funfact("Why the head beats the pencil here",
                    "Written columns were invented for hard sums, not easy ones. When only one column changes, writing it out actually costs you accuracy — every extra digit copied is another chance to copy it wrong. Shopkeepers all over the world add whole hundreds in their heads for exactly this reason, and then reach for paper the moment two columns start talking to each other."),
            withfig(teach("Concept B", "When a column fills up", [
                "Whole tens work the same way — the line below steps $360, 370, 380, 390$, and only the tens digit moves.",
                "But a column can only hold a single digit. $280 + 40$ asks for $8 + 4 = 12$ tens, and there is no way to write $12$ in one column.",
                "So ten of those tens trade up for one hundred: the hundreds go $2 \\to 3$, and $2$ tens stay behind. $280 + 40 = 320$. Nothing was gained or lost — the same amount is just wearing bigger bundles.",
            ]), fig_tens),
            workedset("Trading a full column", "Count the tens; trade ten of them for a hundred.", [
                wex("Work out $280 + 40$.",
                    ["Tens: $8 + 4 = 12$ — too many for one column.",
                     "Ten tens trade up for one hundred: $2 \\to 3$ hundreds.",
                     "$2$ tens are left, so $280 + 40 = 320$."],
                    "$320$",
                    ["Eq(8 + 4, 12)", "Eq(280 + 40, 320)", "Eq(12 - 10, 2)"]),
                wex("Work out $460 - 90$.",
                    ["Only $6$ tens, but $9$ are needed.",
                     "Break one hundred back into $10$ tens: $16$ tens, $3$ hundreds.",
                     "$16 - 9 = 7$ tens, so $460 - 90 = 370$. Receipt: $370 + 90 = 460$ ✓."],
                    "$370$",
                    ["Eq(16 - 9, 7)", "Eq(460 - 90, 370)", "Eq(370 + 90, 460)"]),
            ]),
            tryitset("Over the top", "If the column would pass nine, trade.", [
                withfig(tp("$280 + 40$ is:",
                   ["$320$", "$300$", "$284$"],
                   "Twelve tens cannot sit in one column: ten of them become a hundred, leaving $2$ tens — the line above shows the jump landing past $300$, at $320$. Stopping at $300$ forgets those leftover tens, and $284$ adds four ONES instead of four tens.",
                   ["Eq(280 + 40, 320)", "Eq(8 + 4, 12)",
                    "Eq(280 + 4, 284)"]), fig_bridge),
                tp("$170 + 60$ is:",
                   ["$230$", "$730$", "$176$"],
                   "$7 + 6 = 13$ tens: ten trade up for a hundred, leaving $3$ tens with $2$ hundreds. So $230$, which you can also see as $170 \\to 200 \\to 230$.",
                   ["Eq(7 + 6, 13)", "Eq(170 + 60, 230)", "Eq(200 + 30, 230)"]),
                tp("$520 - 70$ is:",
                   ["$450$", "$490$", "$550$"],
                   "Only $2$ tens are there, so a hundred breaks into ten more: $12 - 7 = 5$ tens with $4$ hundreds, giving $450$. The receipt is $450 + 70 = 520$ ✓.",
                   ["Eq(12 - 7, 5)", "Eq(520 - 70, 450)", "Eq(450 + 70, 520)"]),
            ]),
            tapq("How many tens is that?", "In $280 + 40$, how many tens are there before any trading?",
                 ["$12$", "$4$", "$8$", "$120$"],
                 "$280$ carries $8$ tens and $40$ carries $4$ more: $8 + 4 = 12$ tens altogether, which is $120$. Since a column holds only one digit, ten of them trade up for a hundred and the answer becomes $320$.",
                 ["Eq(8 + 4, 12)", "Eq(12*10, 120)", "Eq(280 + 40, 320)"]),
            recap([
                "Adding a whole hundred moves only the hundreds digit; a whole ten moves only the tens.",
                "$240 + 300 = 540$ — the untouched columns are simply copied down.",
                "If a column would pass nine, ten of it trades up for one of the next column left.",
                "$280 + 40 = 320$, because $12$ tens is one hundred and $2$ tens.",
            ]),
            tip("Before adding, ask \"how many tens will there be?\" out loud. If the answer is more than nine you already know a trade is coming, and a trade you expected is a trade you will not forget."),
            tryitset("Chapter practice", "Name the column, then add.", [
                tp("$405 + 300$ is:",
                   ["$705$", "$435$", "$408$"],
                   "Four hundreds plus three is seven: $705$, with the $0$ tens and $5$ ones copied down. The zero in the tens column stays a zero.",
                   ["Eq(405 + 300, 705)", "Eq(400 + 300, 700)"]),
                tp("$390 + 50$ is:",
                   ["$440$", "$395$", "$840$"],
                   "$9 + 5 = 14$ tens: ten trade up for a hundred, leaving $4$ tens with $4$ hundreds. So $440$.",
                   ["Eq(9 + 5, 14)", "Eq(390 + 50, 440)"]),
                tp("$630 - 80$ is:",
                   ["$550$", "$650$", "$558$"],
                   "Three tens will not cover eight, so a hundred breaks into ten more: $13 - 8 = 5$ tens with $5$ hundreds. $550$, and $550 + 80 = 630$ ✓.",
                   ["Eq(13 - 8, 5)", "Eq(630 - 80, 550)", "Eq(550 + 80, 630)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Adding Tens and Hundreds\"",
                    "The trade you just met — ten of one column becoming one of the next — is the single idea behind every written addition and subtraction you will ever do. The next two lessons only give it a place to stand on the page.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Column Addition
# ==========================================================================

def lesson_column_addition():
    # 156 + 237: ones 6+7 = 13, one ten carried. Both addends drawn.
    a_h, a_t, a_o = 1, 5, 6
    b_h, b_t, b_o = 2, 3, 7
    total = 100 * (a_h + b_h) + 10 * (a_t + b_t) + (a_o + b_o)  # 393
    fig_add = fig_groups(*(cols(a_h, a_t, a_o, "156")[:1]
                           + cols(a_h, a_t, a_o, "156")[1:]))
    fig_ones = fig_groups((a_o, "156: 6 ones", C_GREEN),
                          (b_o, "237: 7 ones", C_ACCENT))
    fig_check = fig_numline([(156, "156"), (356, "+200"), (386, "+30"),
                             (393, "+7")], lo=156, hi=400)
    return {
        "slug": "column-addition",
        "title": "Column Addition",
        "concreteComparison": (
            "Two herds are driven into one pen: $156$ animals and $237$. "
            "Counting the whole pen from scratch would take an hour. "
            "Counting hundreds with hundreds, tens with tens and ones "
            "with ones takes a moment — and that is all a written "
            "addition is."),
        "objective": (
            "Add two three-digit numbers by columns, carry a ten when the "
            "ones column passes nine, and check the answer by adding the "
            "parts a second way."),
        "concept": [
            "**Line up the columns and add each one.** Write the numbers "
            "one above the other with hundreds over hundreds, tens over "
            "tens, ones over ones. Then add each column on its own, "
            "starting from the ones.",
            "**When a column passes nine, carry.** $6 + 7 = 13$ ones. Ten "
            "of them trade up for one ten, which is written as a small "
            "$1$ above the tens column; the $3$ stays in the ones. That "
            "carried $1$ is not decoration — it is a real ten waiting to "
            "be added.",
            "**Finish the remaining columns, carry included.** Tens: $5 + "
            "3 = 8$, plus the carried $1$ makes $9$. Hundreds: $1 + 2 = "
            "3$. The answer is $393$ — and you can check it by adding in "
            "chunks instead: $156 + 200 + 30 + 7$.",
        ],
        "keyIdea": (
            "Column addition adds each place separately, and a carry is "
            "simply ten of one column arriving in the next as a single "
            "unit."),
        "facts": [
            {"title": "Ones can overflow",
             "latex": "6 + 7 = 13",
             "explanation": "Thirteen ones is one ten and three ones — the ten is carried."},
            {"title": "The carry is a real ten",
             "latex": "156 + 237 = 393",
             "explanation": "Tens column: 5 + 3 = 8, plus the carried 1 makes 9."},
        ],
        "workedExamples": [
            {"id": "g3as-l2-we1",
             "statement": "Add $156 + 237$ in columns.",
             "note": "Start at the ones and work left.",
             "solution": ("Ones: $6 + 7 = 13$ — write $3$, carry $1$ ten. Tens: "
                          "$5 + 3 = 8$, plus the carried $1$ gives $9$. "
                          "Hundreds: $1 + 2 = 3$. So $156 + 237 = 393$. Check "
                          "another way: $156 + 200 = 356$, $+30 = 386$, "
                          "$+7 = 393$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6 + 7, 13)", "Eq(5 + 3 + 1, 9)",
                       "Eq(156 + 237, 393)", "Eq(356 + 30, 386)",
                       "Eq(386 + 7, 393)"]},
            {"id": "g3as-l2-we2",
             "statement": "Add $324 + 145$ in columns.",
             "note": "Check each column before you write anything.",
             "solution": ("Ones: $4 + 5 = 9$ — no carry, since nine still fits. "
                          "Tens: $2 + 4 = 6$. Hundreds: $3 + 1 = 4$. So "
                          "$324 + 145 = 469$. Not every addition needs a "
                          "carry; look before you assume one."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4 + 5, 9)", "Eq(2 + 4, 6)", "Eq(324 + 145, 469)"]},
        ],
        "commonMistakes": [
            {"text": "Writing the whole 13 in the ones column, giving 156 + 237 = 3813.",
             "correction": "A column holds one digit. Thirteen ones is one ten and three ones: the 3 stays and the ten is carried to the tens column, giving 393.",
             "authored": True},
            {"text": "Forgetting to add the carried 1 into the next column, giving 383.",
             "correction": "The carried 1 is a real ten that has moved house. The tens column is 5 + 3 + 1 = 9, not 8 — the answer is 393.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3as-l2-t1",
             "statement": "Add $248 + 135$ in columns and say where the carry happens.",
             "solution": ("Ones: $8 + 5 = 13$ — write $3$, carry $1$. Tens: "
                          "$4 + 3 = 7$, plus $1$ is $8$. Hundreds: $2 + 1 = 3$. "
                          "So $248 + 135 = 383$."),
             "check": ["Eq(8 + 5, 13)", "Eq(4 + 3 + 1, 8)",
                       "Eq(248 + 135, 383)"]},
            {"id": "g3as-l2-t2",
             "statement": "Add $506 + 271$ in columns.",
             "solution": ("Ones: $6 + 1 = 7$. Tens: $0 + 7 = 7$. Hundreds: "
                          "$5 + 2 = 7$. So $506 + 271 = 777$, with no carry "
                          "anywhere."),
             "check": ["Eq(6 + 1, 7)", "Eq(0 + 7, 7)", "Eq(506 + 271, 777)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One column at a time", [
                "Two herds join in one pen: $156$ and $237$. Rather than recount everything, add like with like — hundreds with hundreds, tens with tens, ones with ones.",
                "Start at the ones, because that is where a trade can begin. The picture below shows the two ones columns meeting: $6$ ones and $7$ ones.",
                "$6 + 7 = 13$, and thirteen ones will not fit in a single column. That is the whole reason carrying exists.",
            ]), fig_ones),
            workedset("Add the ones first", "Ones, then tens, then hundreds.", [
                wex("Add $324 + 145$ in columns.",
                    ["Ones: $4 + 5 = 9$ — it fits, no carry.",
                     "Tens: $2 + 4 = 6$. Hundreds: $3 + 1 = 4$.",
                     "$324 + 145 = 469$."],
                    "$469$",
                    ["Eq(4 + 5, 9)", "Eq(324 + 145, 469)"]),
                wex("Add $213 + 462$ in columns.",
                    ["Ones: $3 + 2 = 5$. Tens: $1 + 6 = 7$.",
                     "Hundreds: $2 + 4 = 6$.",
                     "$213 + 462 = 675$ — no column passed nine."],
                    "$675$",
                    ["Eq(3 + 2, 5)", "Eq(1 + 6, 7)", "Eq(213 + 462, 675)"]),
            ]),
            tryitset("Column by column", "Add each place on its own.", [
                tp("$342 + 236$ is:",
                   ["$578$", "$678$", "$478$"],
                   "Ones $2 + 6 = 8$, tens $4 + 3 = 7$, hundreds $3 + 2 = 5$: $578$. No column passed nine, so nothing was carried — $678$ invents a carry that never happened, and $478$ loses a hundred.",
                   ["Eq(2 + 6, 8)", "Eq(4 + 3, 7)", "Eq(3 + 2, 5)",
                    "Eq(342 + 236, 578)"]),
                tp("$105 + 371$ is:",
                   ["$476$", "$576$", "$466$"],
                   "Ones $5 + 1 = 6$, tens $0 + 7 = 7$, hundreds $1 + 3 = 4$: $476$. The zero in the tens column adds nothing, which is exactly what it should do; $576$ carries a hundred out of a column that never overflowed.",
                   ["Eq(5 + 1, 6)", "Eq(0 + 7, 7)", "Eq(1 + 3, 4)",
                    "Eq(105 + 371, 476)"]),
                tp("In $253 + 124$, which column would need a carry?",
                   ["none of them", "the ones", "the tens"],
                   "Ones $3 + 4 = 7$, tens $5 + 2 = 7$, hundreds $2 + 1 = 3$ — every column stays under ten, so $253 + 124 = 377$ with no carry at all.",
                   ["Eq(3 + 4, 7)", "Eq(5 + 2, 7)", "Eq(253 + 124, 377)"]),
            ]),
            tapq("Does it fit?", "Adding the ones gives $6 + 7$. What goes in the ones column of the answer?",
                 ["$3$, with a ten carried", "$13$",
                  "$1$, with three carried", "$7$"],
                 "$6 + 7 = 13$ ones, which is one ten and three ones. The $3$ stays in the ones column and the ten moves next door as a carried $1$.",
                 ["Eq(6 + 7, 13)", "Eq(13 - 10, 3)"]),
            funfact("The little carried one is a thousand years old",
                    "The habit of writing a small digit above the next column travelled to Europe from Indian and Arabic arithmetic, alongside the digits themselves. Before that, addition was done by sliding counters on a board — and the \"carry\" was literally a counter you picked up from one groove and carried to the next. The name outlived the board."),
            withfig(teach("Concept B", "Carrying, and checking your work", [
                "Back to $156 + 237$. Ones: $6 + 7 = 13$, so write $3$ and carry one ten. Tens: $5 + 3 = 8$, plus the carried ten makes $9$. Hundreds: $1 + 2 = 3$. The answer is $393$.",
                "The carried $1$ is not a decoration — it is one whole ten that changed columns. Forget to add it and the answer is $383$, ten short.",
                "Always check a different way. The line below adds $156$ in chunks: $+200$ to $356$, $+30$ to $386$, $+7$ to $393$. Same answer by a different road means the answer is right.",
            ]), fig_check),
            workedset("Carry, then check", "Add in columns; check in chunks.", [
                wex("Add $156 + 237$ in columns.",
                    ["Ones: $6 + 7 = 13$ — write $3$, carry $1$.",
                     "Tens: $5 + 3 = 8$, plus the carry is $9$.",
                     "Hundreds: $1 + 2 = 3$. So $393$; check $156 + 200 + 30 + 7 = 393$ ✓."],
                    "$393$",
                    ["Eq(6 + 7, 13)", "Eq(5 + 3 + 1, 9)", "Eq(156 + 237, 393)",
                     "Eq(156 + 200 + 30 + 7, 393)"]),
                wex("Add $437 + 216$ in columns.",
                    ["Ones: $7 + 6 = 13$ — write $3$, carry $1$.",
                     "Tens: $3 + 1 = 4$, plus the carry is $5$.",
                     "Hundreds: $4 + 2 = 6$. So $653$; check $437 + 200 + 10 + 6 = 653$ ✓."],
                    "$653$",
                    ["Eq(7 + 6, 13)", "Eq(3 + 1 + 1, 5)", "Eq(437 + 216, 653)",
                     "Eq(437 + 200 + 10 + 6, 653)"]),
            ]),
            tryitset("Mind the carry", "The carried ten must be added in.", [
                tp("$268 + 125$ is:",
                   ["$393$", "$383$", "$493$"],
                   "Ones $8 + 5 = 13$: write $3$, carry $1$. Tens $6 + 2 = 8$ plus the carry is $9$. Hundreds $2 + 1 = 3$. Forgetting the carry gives $383$ — exactly ten short; sending the carry into the HUNDREDS instead gives $493$, a hundred too many.",
                   ["Eq(8 + 5, 13)", "Eq(6 + 2 + 1, 9)", "Eq(268 + 125, 393)",
                    "Eq(393 - 383, 10)", "Eq(493 - 393, 100)"]),
                tp("$347 + 528$ is:",
                   ["$875$", "$865$", "$975$"],
                   "Ones $7 + 8 = 15$: write $5$, carry $1$. Tens $4 + 2 = 6$ plus the carry is $7$. Hundreds $3 + 5 = 8$. So $875$ — $865$ drops the carry and $975$ puts it in the wrong column.",
                   ["Eq(7 + 8, 15)", "Eq(4 + 2 + 1, 7)", "Eq(347 + 528, 875)",
                    "Eq(875 - 865, 10)"]),
                tp("Bat adds $156 + 237$ and gets $383$. His mistake was:",
                   ["he forgot the carried ten",
                    "he added the hundreds wrongly",
                    "he added the ones wrongly"],
                   "His ones and hundreds are both right; the tens should be $5 + 3 + 1 = 9$, not $8$. The missing carry costs exactly $10$: $393 - 383 = 10$.",
                   ["Eq(5 + 3 + 1, 9)", "Eq(393 - 383, 10)",
                    "Eq(156 + 237, 393)"]),
            ]),
            tapq("Where does the carry go?", "In $268 + 125$, the ones give $13$. The carried ten is added to:",
                 ["the tens column", "the ones column",
                  "the hundreds column", "nowhere — it is just marked"],
                 "Ten ones are worth exactly one ten, so the carry joins the tens column: $6 + 2 + 1 = 9$. That makes the answer $393$ rather than $383$.",
                 ["Eq(6 + 2 + 1, 9)", "Eq(268 + 125, 393)"]),
            recap([
                "Line the numbers up by column and add the ones first.",
                "If a column passes nine, write the ones digit and carry the ten next door.",
                "The carried $1$ must be added into the next column — forgetting it costs exactly $10$.",
                "Check every answer a second way, by adding in chunks: $156 + 200 + 30 + 7 = 393$.",
            ]),
            tip("Write the carried $1$ small and above the line, never squeezed beside a digit. A carry you cannot see is a carry you will forget, and that mistake always costs the same $10$."),
            tryitset("Chapter practice", "Ones first; carry when a column overflows.", [
                tp("$418 + 273$ is:",
                   ["$691$", "$681$", "$791$"],
                   "Ones $8 + 3 = 11$: write $1$, carry $1$. Tens $1 + 7 = 8$ plus the carry is $9$. Hundreds $4 + 2 = 6$. So $691$ — $681$ drops the carry, and $791$ adds it to the hundreds as well.",
                   ["Eq(8 + 3, 11)", "Eq(1 + 7 + 1, 9)", "Eq(418 + 273, 691)",
                    "Eq(691 - 681, 10)"]),
                tp("$305 + 462$ is:",
                   ["$767$", "$757$", "$776$"],
                   "Ones $5 + 2 = 7$, tens $0 + 6 = 6$, hundreds $3 + 4 = 7$: $767$, with no carry needed anywhere.",
                   ["Eq(5 + 2, 7)", "Eq(0 + 6, 6)", "Eq(305 + 462, 767)"]),
                tp("Which of these needs a carry out of the ones?",
                   ["$236 + 147$", "$236 + 142$", "$231 + 147$"],
                   "$6 + 7 = 13$ passes nine, so that one carries and gives $383$. The others give $6 + 2 = 8$ and $1 + 7 = 8$, both of which fit.",
                   ["Eq(6 + 7, 13)", "Eq(236 + 147, 383)", "Eq(6 + 2, 8)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Column Addition\"",
                    "You can now add any two numbers below a thousand. Subtraction is next, and it is the same trade running backwards: instead of ten ones becoming a ten, a ten breaks back into ten ones whenever the column above is too small.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Column Subtraction
# ==========================================================================

def lesson_column_subtraction():
    fig_short = fig_groups((2, "342: 2 ones", C_ACCENT),
                           (7, "128: 7 ones needed", C_WARM))
    fig_broken = fig_groups((3, "hundreds", C_ACCENT),
                            (3, "tens after breaking one", C_WARM),
                            (12, "ones after breaking", C_GREEN))
    fig_receipt = fig_numline([(214, "214"), (342, "342")], lo=200, hi=350)
    return {
        "slug": "column-subtraction",
        "title": "Column Subtraction",
        "concreteComparison": (
            "A pen holds $342$ animals and $128$ are driven out. Counting "
            "what is left one by one would take all morning. Take them "
            "away column by column instead — and when a column has too "
            "few, break one bundle from the column to its left."),
        "objective": (
            "Subtract a three-digit number from another by columns, break "
            "a ten or a hundred when a column is short, and prove every "
            "answer with a receipt."),
        "concept": [
            "**Subtract column by column, starting at the ones.** For "
            "$342 - 128$: the ones column asks $2 - 8$, and there are not "
            "enough ones to do it. That is the signal to break a bundle.",
            "**Break one ten into ten ones.** Take one of the four tens "
            "and open it: the tens drop from $4$ to $3$, and the ones "
            "rise from $2$ to $12$. Nothing has changed in size — $342$ "
            "is still $342$, just packed differently. Now $12 - 8 = 4$.",
            "**Finish the other columns, then take the receipt.** Tens: "
            "$3 - 2 = 1$ (remember the $4$ became $3$). Hundreds: $3 - 1 "
            "= 2$. So $342 - 128 = 214$. The receipt is the check: "
            "$214 + 128 = 342$. If the receipt does not come back to the "
            "number you started with, the answer is wrong.",
        ],
        "keyIdea": (
            "Subtraction breaks bundles down — one ten becomes ten ones "
            "— and every answer must pay its receipt: what is left plus "
            "what was taken must equal what you started with."),
        "facts": [
            {"title": "Breaking a ten",
             "latex": "342 = 300 + 30 + 12",
             "explanation": "One of the four tens has been opened into ten ones, so the number is repacked but unchanged."},
            {"title": "The receipt",
             "latex": "214 + 128 = 342",
             "explanation": "What is left plus what was taken returns the starting number — the proof the answer is right."},
        ],
        "workedExamples": [
            {"id": "g3as-l3-we1",
             "statement": "Work out $342 - 128$ in columns, and give the receipt.",
             "note": "Check the ones column before you start writing.",
             "solution": ("Ones: $2 - 8$ cannot be done, so break one ten. The "
                          "tens go $4 \\to 3$ and the ones go $2 \\to 12$; now "
                          "$12 - 8 = 4$. Tens: $3 - 2 = 1$. Hundreds: $3 - 1 = "
                          "2$. So $342 - 128 = 214$, and the receipt "
                          "$214 + 128 = 342$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(12 - 8, 4)", "Eq(3 - 2, 1)", "Eq(342 - 128, 214)",
                       "Eq(214 + 128, 342)", "Eq(300 + 30 + 12, 342)"]},
            {"id": "g3as-l3-we2",
             "statement": "Work out $475 - 231$ in columns.",
             "note": "Look first — you may not need to break anything.",
             "solution": ("Ones: $5 - 1 = 4$ — no breaking needed. Tens: "
                          "$7 - 3 = 4$. Hundreds: $4 - 2 = 2$. So "
                          "$475 - 231 = 244$, and the receipt "
                          "$244 + 231 = 475$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5 - 1, 4)", "Eq(7 - 3, 4)", "Eq(475 - 231, 244)",
                       "Eq(244 + 231, 475)"]},
        ],
        "commonMistakes": [
            {"text": "Turning 2 − 8 upside down and writing 6, because \"8 take away 2 is easier\".",
             "correction": "The column says 2 minus 8, and swapping it changes the question. Break a ten first: 12 − 8 = 4. The swap gives 216 instead of 214.",
             "authored": True},
            {"text": "Breaking a ten but forgetting to reduce the tens digit, subtracting from 4 tens instead of 3.",
             "correction": "The broken ten has moved into the ones — it cannot be in both places. The tens column is 3 − 2 = 1, so the answer is 214, not 224.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3as-l3-t1",
             "statement": "Work out $563 - 247$ and give the receipt.",
             "solution": ("Ones: $3 - 7$ needs a break, so $6$ tens become $5$ "
                          "and $3$ ones become $13$: $13 - 7 = 6$. Tens: "
                          "$5 - 4 = 1$. Hundreds: $5 - 2 = 3$. So "
                          "$563 - 247 = 316$, and $316 + 247 = 563$ ✓."),
             "check": ["Eq(13 - 7, 6)", "Eq(563 - 247, 316)",
                       "Eq(316 + 247, 563)"]},
            {"id": "g3as-l3-t2",
             "statement": "Work out $806 - 302$.",
             "solution": ("Ones: $6 - 2 = 4$. Tens: $0 - 0 = 0$. Hundreds: "
                          "$8 - 3 = 5$. So $806 - 302 = 504$, receipt "
                          "$504 + 302 = 806$ ✓."),
             "check": ["Eq(6 - 2, 4)", "Eq(806 - 302, 504)",
                       "Eq(504 + 302, 806)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "When a column runs short", [
                "Take $128$ away from $342$. Start at the ones, as always — and immediately there is trouble.",
                "The picture below shows why: there are only $2$ ones in $342$, but $7$ ones from $128$ are more than that, and even $8$ are needed once you count properly. You cannot take $8$ from $2$.",
                "This is not a dead end. It is the signal to break a bundle from the column to the left — the same trade as carrying, running the other way.",
            ]), fig_short),
            workedset("Subtract without breaking",
                      "First, the easy case: every column has enough.", [
                wex("Work out $475 - 231$.",
                    ["Ones: $5 - 1 = 4$. Tens: $7 - 3 = 4$.",
                     "Hundreds: $4 - 2 = 2$.",
                     "$475 - 231 = 244$; receipt $244 + 231 = 475$ ✓."],
                    "$244$",
                    ["Eq(5 - 1, 4)", "Eq(475 - 231, 244)",
                     "Eq(244 + 231, 475)"]),
                wex("Work out $689 - 154$.",
                    ["Ones: $9 - 4 = 5$. Tens: $8 - 5 = 3$.",
                     "Hundreds: $6 - 1 = 5$.",
                     "$689 - 154 = 535$; receipt $535 + 154 = 689$ ✓."],
                    "$535$",
                    ["Eq(9 - 4, 5)", "Eq(689 - 154, 535)",
                     "Eq(535 + 154, 689)"]),
            ]),
            tryitset("No breaking needed", "Check each column has enough first.", [
                tp("$758 - 316$ is:",
                   ["$442$", "$432$", "$448$"],
                   "Ones $8 - 6 = 2$, tens $5 - 1 = 4$, hundreds $7 - 3 = 4$: $442$. Receipt: $442 + 316 = 758$ ✓.",
                   ["Eq(8 - 6, 2)", "Eq(758 - 316, 442)", "Eq(442 + 316, 758)"]),
                tp("$597 - 264$ is:",
                   ["$333$", "$323$", "$343$"],
                   "Ones $7 - 4 = 3$, tens $9 - 6 = 3$, hundreds $5 - 2 = 3$: $333$. Receipt: $333 + 264 = 597$ ✓.",
                   ["Eq(9 - 6, 3)", "Eq(597 - 264, 333)", "Eq(333 + 264, 597)"]),
                tp("Which subtraction needs a column broken?",
                   ["$451 - 126$", "$451 - 121$", "$456 - 121$"],
                   "$1 - 6$ cannot be done, so that one needs a break: the answer is $325$. The other two have enough ones already.",
                   ["Eq(451 - 126, 325)", "Eq(451 - 121, 330)",
                    "Eq(11 - 6, 5)"]),
            ]),
            tapq("Reading the column honestly", "The ones column says $2 - 8$. What should you do?",
                 ["break a ten into ten ones",
                  "swap it round and do $8 - 2$",
                  "write $0$ and move on",
                  "start again from the hundreds"],
                 "Swapping the column changes the question and gives a wrong answer. Break one ten instead: the ones become $12$ and $12 - 8 = 4$, which leads to the true answer $214$.",
                 ["Eq(12 - 8, 4)", "Eq(342 - 128, 214)", "Ne(8 - 2, 12 - 8)"]),
            funfact("Subtraction is addition wearing a disguise",
                    "Shopkeepers giving change almost never subtract. Handed $500$ tögrög for a $342$ tögrög purchase, they count UP: \"$342$, $350$, $400$, $500$\" — and the change is what they counted. Every subtraction has this twin, which is exactly why the receipt works: if $158$ is what you counted up, then $342 + 158$ must come back to $500$."),
            withfig(teach("Concept B", "Breaking a bundle, and the receipt", [
                "Break one of the four tens in $342$. The tens drop from $4$ to $3$ and the ones jump from $2$ to $12$ — the picture below shows the repacked number.",
                "Nothing changed in size: $300 + 30 + 12$ is still $342$. Now the columns work. Ones: $12 - 8 = 4$. Tens: $3 - 2 = 1$ (using the reduced $3$). Hundreds: $3 - 1 = 2$. The answer is $214$.",
                "Then take the receipt: $214 + 128 = 342$. This is not an optional extra — it is the only way to know you are right, and it catches the two commonest slips instantly.",
            ]), fig_broken),
            workedset("Break, subtract, check", "Reduce the column you borrowed from.", [
                wex("Work out $342 - 128$.",
                    ["Ones: $2 - 8$ is impossible, so break a ten: $4 \\to 3$ tens, $2 \\to 12$ ones.",
                     "Ones: $12 - 8 = 4$. Tens: $3 - 2 = 1$. Hundreds: $3 - 1 = 2$.",
                     "$342 - 128 = 214$; receipt $214 + 128 = 342$ ✓."],
                    "$214$",
                    ["Eq(12 - 8, 4)", "Eq(342 - 128, 214)",
                     "Eq(214 + 128, 342)"]),
                wex("Work out $624 - 371$.",
                    ["Ones: $4 - 1 = 3$, no break needed there.",
                     "Tens: $2 - 7$ is impossible, so break a hundred: $6 \\to 5$ hundreds, $2 \\to 12$ tens. Then $12 - 7 = 5$.",
                     "Hundreds: $5 - 3 = 2$. So $253$; receipt $253 + 371 = 624$ ✓."],
                    "$253$",
                    ["Eq(12 - 7, 5)", "Eq(624 - 371, 253)",
                     "Eq(253 + 371, 624)"]),
            ]),
            tryitset("Break and check", "Reduce the lending column, then take the receipt.", [
                withfig(tp("$342 - 128$ is:",
                   ["$214$", "$216$", "$224$"],
                   "Breaking a ten gives $12 - 8 = 4$ ones and leaves $3$ tens: $3 - 2 = 1$. So $214$, and $214 + 128 = 342$ ✓. Swapping the ones column gives $216$; forgetting to reduce the tens gives $224$.",
                   ["Eq(342 - 128, 214)", "Eq(214 + 128, 342)",
                    "Eq(12 - 8, 4)"]), fig_receipt),
                tp("$725 - 148$ is:",
                   ["$577$", "$677$", "$587$"],
                   "Ones: break a ten, $15 - 8 = 7$. Tens: $1 - 4$ needs a hundred broken, $11 - 4 = 7$. Hundreds: $6 - 1 = 5$. So $577$, and $577 + 148 = 725$ ✓.",
                   ["Eq(15 - 8, 7)", "Eq(11 - 4, 7)", "Eq(725 - 148, 577)",
                    "Eq(577 + 148, 725)"]),
                tp("Saruul answers $342 - 128 = 224$. The receipt says:",
                   ["$224 + 128 = 352$, so she is wrong",
                    "$224 + 128 = 342$, so she is right",
                    "the receipt cannot be used here"],
                   "$224 + 128 = 352$, which is $10$ more than $342$ — she borrowed a ten but never reduced the tens column. The true answer is $214$.",
                   ["Eq(224 + 128, 352)", "Eq(352 - 342, 10)",
                    "Eq(342 - 128, 214)"]),
            ]),
            tapq("What the receipt proves", "You answer $563 - 247 = 316$. Which sum proves it?",
                 ["$316 + 247 = 563$", "$563 + 247 = 810$",
                  "$316 + 563 = 879$", "$563 - 316 = 247$"],
                 "The receipt puts back what was taken: what is LEFT plus what was REMOVED must return the starting number, and $316 + 247 = 563$ ✓. (The last option is true as well, but it is a second subtraction — the receipt is deliberately an addition, because addition is the easier thing to get right.)",
                 ["Eq(316 + 247, 563)", "Eq(563 - 247, 316)"]),
            recap([
                "Subtract column by column, starting at the ones.",
                "If a column is short, break one bundle from the left: a ten becomes ten ones, a hundred becomes ten tens.",
                "The lending column must go DOWN by one — the bundle cannot be in two places.",
                "Every answer pays a receipt: what is left plus what was taken equals what you started with.",
            ]),
            tip("Never write an answer to a subtraction without the receipt underneath it. It takes five seconds, it catches both of the classic mistakes, and it turns \"I think so\" into \"I know\"."),
            tryitset("Chapter practice", "Break when short; always take the receipt.", [
                tp("$450 - 126$ is:",
                   ["$324$", "$334$", "$336$"],
                   "Ones: break a ten, $10 - 6 = 4$, leaving $4$ tens. Tens: $4 - 2 = 2$. Hundreds: $4 - 1 = 3$. So $324$, and $324 + 126 = 450$ ✓.",
                   ["Eq(10 - 6, 4)", "Eq(450 - 126, 324)",
                    "Eq(324 + 126, 450)"]),
                tp("$938 - 415$ is:",
                   ["$523$", "$513$", "$533$"],
                   "Ones $8 - 5 = 3$, tens $3 - 1 = 2$, hundreds $9 - 4 = 5$: $523$, with nothing broken. Receipt: $523 + 415 = 938$ ✓.",
                   ["Eq(8 - 5, 3)", "Eq(938 - 415, 523)",
                    "Eq(523 + 415, 938)"]),
                tp("Which answer FAILS its receipt?",
                   ["$681 - 245 = 446$", "$681 - 245 = 436$",
                    "$579 - 132 = 447$"],
                   "$446 + 245 = 691$, which overshoots $681$ by $10$ — so that answer is wrong. The true value is $436$, and $436 + 245 = 681$ ✓.",
                   ["Eq(446 + 245, 691)", "Eq(691 - 681, 10)",
                    "Eq(681 - 245, 436)", "Eq(579 - 132, 447)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Column Subtraction\"",
                    "Carrying and breaking are one idea seen from two sides: ten of a column is one of the next. Next you will see that addition and subtraction are also one idea from two sides — every sum you know hides two subtractions inside it.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Fact Families and Missing Numbers
# ==========================================================================

def lesson_fact_families():
    fig_family = fig_groups((6, "part: 60", C_ACCENT),
                            (8, "part: 80", C_WARM),
                            (14, "whole: 140", C_GREEN))
    fig_bar = fig_groups((3, "part: 30", C_ACCENT),
                         (9, "rest of the whole", C_WARM))
    return {
        "slug": "fact-families-and-missing-numbers",
        "title": "Fact Families & Missing Numbers",
        "concreteComparison": (
            "Two flocks of $60$ and $80$ make one flock of $140$. Split "
            "the big flock again and you are back where you started. "
            "Every joining has an undoing, and knowing one fact hands you "
            "three more for free."),
        "objective": (
            "Write the four facts of a whole-and-parts family, use them "
            "to find a missing number in an addition or subtraction, and "
            "say which operation undoes which."),
        "concept": [
            "**Two parts and a whole make four facts.** From $60$, $80$ "
            "and $140$ you can write $60 + 80 = 140$, $80 + 60 = 140$, "
            "$140 - 60 = 80$ and $140 - 80 = 60$. That is a fact family, "
            "and every member is true the moment any one of them is.",
            "**Subtraction undoes addition.** If $60 + 80 = 140$, then "
            "taking $80$ back off $140$ must leave the $60$ you started "
            "with. That is why the receipt in the last lesson worked — "
            "it was a fact family being used as a check.",
            "**A missing number is a family with one member hidden.** "
            "$? + 30 = 140$ hides a part. Since the whole is $140$ and "
            "one part is $30$, the other part is $140 - 30 = 110$. Find "
            "out whether the gap is a PART or the WHOLE, and the family "
            "tells you what to do.",
        ],
        "keyIdea": (
            "Every pair of parts and their whole make four facts. A "
            "missing part is found by subtracting; a missing whole is "
            "found by adding."),
        "facts": [
            {"title": "The four facts",
             "latex": "60 + 80 = 140",
             "explanation": "This one fact also gives 80 + 60 = 140, 140 − 60 = 80 and 140 − 80 = 60."},
            {"title": "Missing part, so subtract",
             "latex": "140 - 30 = 110",
             "explanation": "If a part and the whole are known, the other part is the difference."},
        ],
        "workedExamples": [
            {"id": "g3as-l4-we1",
             "statement": "Write the four facts of the family for $60$, $80$ and $140$.",
             "note": "Two additions and two subtractions.",
             "solution": ("$60 + 80 = 140$ and $80 + 60 = 140$ join the parts; "
                          "$140 - 60 = 80$ and $140 - 80 = 60$ split them apart "
                          "again. Four facts, one relationship — the whole is "
                          "always on its own side of the equals sign."),
             "badges": [{"text": "core"}],
             "check": ["Eq(60 + 80, 140)", "Eq(80 + 60, 140)",
                       "Eq(140 - 60, 80)", "Eq(140 - 80, 60)"]},
            {"id": "g3as-l4-we2",
             "statement": "Find the missing number: $? + 30 = 140$.",
             "note": "Is the gap a part or the whole?",
             "solution": ("$140$ is the whole and $30$ is one part, so the gap is "
                          "the OTHER part — and a missing part is found by "
                          "subtracting: $140 - 30 = 110$. Check it in the "
                          "family: $110 + 30 = 140$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(140 - 30, 110)", "Eq(110 + 30, 140)"]},
        ],
        "commonMistakes": [
            {"text": "Adding when the whole is already known — answering ? + 30 = 140 with 170.",
             "correction": "140 is the whole, so the answer cannot be bigger than it. The gap is a part: 140 − 30 = 110, and 110 + 30 = 140 checks out.",
             "authored": True},
            {"text": "Writing 140 − 60 = 80 and then claiming 60 − 140 is also in the family.",
             "correction": "The whole always sits at the front of a subtraction: you can take a part from the whole, but not the whole from a part. The family has exactly four members.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3as-l4-t1",
             "statement": "Write the four facts for $250$, $130$ and $380$.",
             "solution": ("$250 + 130 = 380$, $130 + 250 = 380$, "
                          "$380 - 250 = 130$ and $380 - 130 = 250$."),
             "check": ["Eq(250 + 130, 380)", "Eq(380 - 250, 130)",
                       "Eq(380 - 130, 250)"]},
            {"id": "g3as-l4-t2",
             "statement": "Find the missing number: $420 - ? = 200$.",
             "solution": ("Here $420$ is the whole and $200$ is one part, so the "
                          "gap is the other part: $420 - 200 = 220$. Check: "
                          "$420 - 220 = 200$ ✓."),
             "check": ["Eq(420 - 200, 220)", "Eq(420 - 220, 200)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One fact, four facts", [
                "Two flocks join: $60$ and $80$ make $140$. The picture below shows the two parts and the whole they build.",
                "From that single picture come FOUR true sentences: $60 + 80 = 140$, $80 + 60 = 140$, $140 - 60 = 80$, and $140 - 80 = 60$.",
                "They are one relationship seen from four sides. Learn any one of them and you have quietly learned the other three — which is why fact families make arithmetic four times cheaper to remember.",
            ]), fig_family),
            workedset("Write the family", "Two additions, then two subtractions.", [
                wex("Write the four facts for $60$, $80$, $140$.",
                    ["Joining: $60 + 80 = 140$ and $80 + 60 = 140$.",
                     "Splitting: $140 - 60 = 80$ and $140 - 80 = 60$.",
                     "The whole, $140$, stands alone on one side every time."],
                    "four facts",
                    ["Eq(60 + 80, 140)", "Eq(140 - 60, 80)",
                     "Eq(140 - 80, 60)"]),
                wex("Write the four facts for $150$, $240$, $390$.",
                    ["Joining: $150 + 240 = 390$ and $240 + 150 = 390$.",
                     "Splitting: $390 - 150 = 240$ and $390 - 240 = 150$.",
                     "$390$ is the whole, so it never appears as a part."],
                    "four facts",
                    ["Eq(150 + 240, 390)", "Eq(390 - 150, 240)",
                     "Eq(390 - 240, 150)"]),
            ]),
            tryitset("Spot the family", "The whole stands alone; the parts share a side.", [
                tp("Which fact belongs to the family of $70$, $50$ and $120$?",
                   ["$120 - 50 = 70$", "$70 - 50 = 120$", "$120 + 50 = 70$"],
                   "The whole is $120$, so it leads any subtraction: $120 - 50 = 70$ ✓. The other two put a part where the whole should be.",
                   ["Eq(120 - 50, 70)", "Eq(70 + 50, 120)"]),
                tp("If $340 + 250 = 590$, then $590 - 250$ equals:",
                   ["$340$", "$250$", "$840$"],
                   "Subtraction undoes addition: taking back the $250$ that was added returns the $340$ you started with.",
                   ["Eq(340 + 250, 590)", "Eq(590 - 250, 340)"]),
                tp("Which number is the WHOLE in the family $180$, $320$, $500$?",
                   ["$500$", "$320$", "$180$"],
                   "The whole is the one the other two build: $180 + 320 = 500$. It is always the largest of the three.",
                   ["Eq(180 + 320, 500)", "500 > 320"]),
            ]),
            tapq("Undoing", "$260 + 140 = 400$. Which subtraction undoes it?",
                 ["$400 - 140 = 260$", "$400 - 260 = 140$ is the only one",
                  "$260 - 140 = 120$", "$140 - 260$"],
                 "Taking back the $140$ that was added returns the original $260$: $400 - 140 = 260$ ✓. (Note $400 - 260 = 140$ is also in the family — but it undoes the addition of $260$, not of $140$.)",
                 ["Eq(260 + 140, 400)", "Eq(400 - 140, 260)",
                  "Eq(400 - 260, 140)"]),
            funfact("Why teachers call it a family",
                    "The name comes from the idea that the facts live together and cannot be separated: change one number and all four change at once. It is also a promise about memory — a child who has to learn every addition and every subtraction separately faces four times the work of a child who sees the family."),
            withfig(teach("Concept B", "Finding the hidden member", [
                "A missing number is just a family with one member covered up. The bar below shows a whole with one part known, $30$, and the rest hidden.",
                "First ask: is the missing number a PART or the WHOLE? In $? + 30 = 140$ the whole ($140$) is already showing, so the gap is a part — and a missing part is found by SUBTRACTING: $140 - 30 = 110$.",
                "In $250 + 130 = ?$ the two parts are showing and the whole is hidden, so you ADD. Decide which role is missing and the operation chooses itself.",
            ]), fig_bar),
            workedset("Fill the gap", "Missing part means subtract; missing whole means add.", [
                wex("Find $?$ in $? + 30 = 140$.",
                    ["$140$ is the whole; $30$ is a part.",
                     "The gap is the other part, so subtract: $140 - 30 = 110$.",
                     "Check: $110 + 30 = 140$ ✓."],
                    "$110$",
                    ["Eq(140 - 30, 110)", "Eq(110 + 30, 140)"]),
                wex("Find $?$ in $480 - ? = 150$.",
                    ["$480$ is the whole; $150$ is what is left — also a part.",
                     "The gap is the other part: $480 - 150 = 330$.",
                     "Check: $480 - 330 = 150$ ✓."],
                    "$330$",
                    ["Eq(480 - 150, 330)", "Eq(480 - 330, 150)"]),
            ]),
            tryitset("Find the hidden number", "Name the missing role first.", [
                tp("$? + 60 = 200$. The missing number is:",
                   ["$140$", "$260$", "$120$"],
                   "The whole $200$ is showing, so the gap is a part: $200 - 60 = 140$, and $140 + 60 = 200$ ✓. Adding instead gives $260$, which is bigger than the whole — impossible.",
                   ["Eq(200 - 60, 140)", "Eq(140 + 60, 200)", "260 > 200"]),
                tp("$350 - ? = 120$. The missing number is:",
                   ["$230$", "$470$", "$120$"],
                   "$350$ is the whole and $120$ is what remains, so the missing part is $350 - 120 = 230$. Check: $350 - 230 = 120$ ✓.",
                   ["Eq(350 - 120, 230)", "Eq(350 - 230, 120)"]),
                tp("$180 + 240 = ?$. Here you should:",
                   ["add, because the WHOLE is missing",
                    "subtract, because a part is missing",
                    "either — both give the same answer"],
                   "Both parts are showing and the whole is hidden, so you add: $180 + 240 = 420$. Subtracting would give $60$, which is smaller than either part.",
                   ["Eq(180 + 240, 420)", "Eq(240 - 180, 60)", "420 > 240"]),
            ]),
            tapq("Part or whole?", "In $? - 130 = 210$, what is the missing number?",
                 ["the whole, so add: $340$", "a part, so subtract: $80$",
                  "the whole, so subtract: $80$", "a part, so add: $340$"],
                 "Both $130$ (taken away) and $210$ (left) are parts, so the WHOLE is missing — and a missing whole is found by adding: $130 + 210 = 340$. Check: $340 - 130 = 210$ ✓.",
                 ["Eq(130 + 210, 340)", "Eq(340 - 130, 210)"]),
            recap([
                "Two parts and their whole make four facts — two additions and two subtractions.",
                "Subtraction undoes addition, which is exactly why a receipt proves a subtraction.",
                "A missing PART is found by subtracting; a missing WHOLE is found by adding.",
                "An answer bigger than the whole is always wrong — the whole is the largest number in the family.",
            ]),
            tip("Before filling any gap, point at the biggest number in the sentence and say \"that is the whole\". Everything else follows from knowing which role is missing."),
            tryitset("Chapter practice", "Whole or part — decide, then act.", [
                tp("$? + 250 = 610$. The missing number is:",
                   ["$360$", "$860$", "$250$"],
                   "The whole $610$ is showing, so subtract: $610 - 250 = 360$, and $360 + 250 = 610$ ✓.",
                   ["Eq(610 - 250, 360)", "Eq(360 + 250, 610)"]),
                tp("Which fact does NOT belong with $90$, $210$ and $300$?",
                   ["$210 - 300 = 90$", "$300 - 210 = 90$",
                    "$90 + 210 = 300$"],
                   "You cannot take the whole away from a part. The true facts are $90 + 210 = 300$, $300 - 90 = 210$ and $300 - 210 = 90$.",
                   ["Eq(90 + 210, 300)", "Eq(300 - 210, 90)", "300 > 210"]),
                tp("$? - 175 = 225$. The missing number is:",
                   ["$400$", "$50$", "$175$"],
                   "Both showing numbers are parts, so the whole is missing: $175 + 225 = 400$. Check: $400 - 175 = 225$ ✓.",
                   ["Eq(175 + 225, 400)", "Eq(400 - 175, 225)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Fact Families & Missing Numbers\"",
                    "Knowing which number is the whole is the skill that turns a word problem from a guess into a decision. That is exactly what the last lesson of this topic is about — reading a story and knowing, before you calculate anything, whether you are joining or splitting.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Word Problems
# ==========================================================================

def lesson_word_problems():
    fig_join = fig_groups((12, "morning: 120", C_ACCENT),
                          (9, "afternoon: 90", C_WARM))
    fig_split = fig_groups((16, "started with 160", C_ACCENT),
                           (7, "sold 70", C_WARM))
    return {
        "slug": "word-problems",
        "title": "Word Problems",
        "concreteComparison": (
            "A dairy sells $120$ litres of milk in the morning and $90$ "
            "in the afternoon. Another day it starts with $160$ litres "
            "and sells $70$. One story joins, the other splits — and "
            "telling which is which, before touching the numbers, is the "
            "whole skill."),
        "objective": (
            "Decide from the words whether a problem joins or splits, "
            "solve it in one or two steps, and check that the answer "
            "makes sense in the story."),
        "concept": [
            "**Joining stories add.** Two amounts put together, more "
            "arriving, a total wanted: $120$ litres and $90$ litres sold "
            "altogether is $120 + 90 = 210$ litres. The answer is bigger "
            "than either part, which is what \"altogether\" should "
            "produce.",
            "**Splitting stories subtract.** Something taken away, given "
            "out, or lost; or the DIFFERENCE between two amounts. From "
            "$160$ litres, selling $70$ leaves $160 - 70 = 90$. The "
            "answer is smaller than what you started with.",
            "**Two-step stories do one thing, then the next.** \"She had "
            "$300$, spent $120$, then earned $50$\" is two moves: "
            "$300 - 120 = 180$, then $180 + 50 = 230$. Finish one step "
            "completely before starting the second, and write down what "
            "the middle number MEANS.",
        ],
        "keyIdea": (
            "Read the story first and decide whether it joins or splits, "
            "then calculate — and finally ask whether an answer that size "
            "makes sense for the story."),
        "facts": [
            {"title": "Altogether joins",
             "latex": "120 + 90 = 210",
             "explanation": "A total is bigger than either of the parts it came from."},
            {"title": "Left over splits",
             "latex": "160 - 70 = 90",
             "explanation": "What remains is smaller than what you started with."},
        ],
        "workedExamples": [
            {"id": "g3as-l5-we1",
             "statement": "A dairy sells $120$ litres of milk in the morning and $90$ in the afternoon. How much altogether?",
             "note": "\"Altogether\" is a joining word.",
             "solution": ("Two amounts are being put together, so add: "
                          "$120 + 90 = 210$ litres. Sense check: $210$ is bigger "
                          "than both $120$ and $90$, which is exactly what a "
                          "total should be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(120 + 90, 210)", "210 > 120", "210 > 90"]},
            {"id": "g3as-l5-we2",
             "statement": "Saruul has $300$ tögrög. She spends $120$ on bread, then her aunt gives her $50$. How much does she have now?",
             "note": "Two moves, in the order the story tells them.",
             "solution": ("Step one — spending splits: $300 - 120 = 180$ tögrög "
                          "left. Step two — a gift joins: $180 + 50 = 230$ "
                          "tögrög. The middle number $180$ is not the answer; it "
                          "is how much she had between the two events."),
             "badges": [{"text": "core"}],
             "check": ["Eq(300 - 120, 180)", "Eq(180 + 50, 230)",
                       "Eq(300 - 120 + 50, 230)"]},
        ],
        "commonMistakes": [
            {"text": "Adding every number in the story, so 300, 120 and 50 become 470.",
             "correction": "Spending takes money away and a gift brings it back: 300 − 120 + 50 = 230. The operations come from what happens in the story, never from how many numbers appear.",
             "authored": True},
            {"text": "Stopping at the middle number of a two-step problem and answering 180.",
             "correction": "180 is what she had after the bread, before the gift. The question asks what she has NOW, so the second step must be done: 180 + 50 = 230.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3as-l5-t1",
             "statement": "A herd of $245$ goats is joined by $130$ more. How many now?",
             "solution": ("More arriving is a joining story, so add: "
                          "$245 + 130 = 375$ goats. It is bigger than the herd "
                          "we started with, as it should be."),
             "check": ["Eq(245 + 130, 375)", "375 > 245"]},
            {"id": "g3as-l5-t2",
             "statement": "A shop had $410$ eggs and sold $175$. How many are left?",
             "solution": ("Selling takes away, so subtract: $410 - 175 = 235$ "
                          "eggs. Receipt: $235 + 175 = 410$ ✓."),
             "check": ["Eq(410 - 175, 235)", "Eq(235 + 175, 410)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Joining stories", [
                "A dairy sells $120$ litres in the morning and $90$ in the afternoon — the two batches are drawn below.",
                "The question \"how much altogether?\" asks for the two amounts put TOGETHER, so this is a joining story and you add: $120 + 90 = 210$ litres.",
                "Then check the size. $210$ is bigger than both $120$ and $90$ — a total always is. If your \"total\" comes out smaller than one of its parts, you have subtracted by accident.",
            ]), fig_join),
            workedset("Stories that join", "Look for altogether, in total, and more arriving.", [
                wex("$120$ litres in the morning and $90$ in the afternoon. How much altogether?",
                    ["\"Altogether\" joins the two amounts.",
                     "$120 + 90 = 210$ litres.",
                     "Sense check: $210$ is bigger than both parts ✓."],
                    "$210$ litres",
                    ["Eq(120 + 90, 210)", "210 > 120"]),
                wex("A library has $260$ books and buys $145$ more. How many now?",
                    ["\"More\" arriving is a joining story.",
                     "$260 + 145 = 405$ books.",
                     "Bigger than the $260$ it started with ✓."],
                    "$405$ books",
                    ["Eq(260 + 145, 405)", "405 > 260"]),
            ]),
            tryitset("Join or not?", "What is the story doing to the amounts?", [
                tp("A herd of $312$ is joined by $85$ more. The herd is now:",
                   ["$397$", "$227$", "$312$"],
                   "Animals arriving is a joining story: $312 + 85 = 397$, which is bigger than the herd we started with. Subtracting would give $227$ — a herd that shrank when more arrived.",
                   ["Eq(312 + 85, 397)", "397 > 312", "Eq(312 - 85, 227)"]),
                tp("Two sacks weigh $180$ kg and $240$ kg. Together they weigh:",
                   ["$420$ kg", "$60$ kg", "$240$ kg"],
                   "\"Together\" joins: $180 + 240 = 420$ kg. The $60$ is their difference, which answers a different question — how much heavier one is.",
                   ["Eq(180 + 240, 420)", "Eq(240 - 180, 60)"]),
                tp("Which question is asking you to ADD?",
                   ["How many are there in total?",
                    "How many are left?",
                    "How many more does one have?"],
                   "\"In total\" joins the amounts. \"How many are left\" and \"how many more\" are both splitting questions, answered by subtracting.",
                   ["Eq(120 + 90, 210)", "Eq(160 - 70, 90)"]),
            ]),
            tapq("Reading the size of the answer", "A total comes out SMALLER than one of the amounts being joined. This means:",
                 ["something went wrong — a total is never smaller",
                  "the amounts must have been very close together",
                  "that is normal for large numbers",
                  "you should add one of them again"],
                 "Joining can only grow an amount, so a total must be at least as big as each part: $120 + 90 = 210$, which beats both. A smaller answer means a subtraction slipped in — for instance $120 - 90 = 30$.",
                 ["Eq(120 + 90, 210)", "210 > 120", "Eq(120 - 90, 30)"]),
            funfact("The words that give the game away",
                    "Word problems tend to reuse the same signposts: \"altogether\", \"in total\" and \"joins\" point one way; \"left\", \"remains\", \"gives away\" and \"how many more\" point the other. But signposts can lie — \"he gave away $20$ and then received $50$\" contains both — so the safe habit is to picture the story happening, not to hunt for a keyword."),
            withfig(teach("Concept B", "Splitting stories, and two steps", [
                "A shop starts with $160$ litres and sells $70$ — drawn below. Selling takes away, so this is a splitting story: $160 - 70 = 90$ litres left.",
                "Some stories move twice. \"She had $300$, spent $120$, then was given $50$\" is a split followed by a join: $300 - 120 = 180$, then $180 + 50 = 230$.",
                "Do the steps in the order the story tells them, and say out loud what the middle number means — \"$180$ is what she had after the bread\". That sentence is what stops you handing in the middle number as the answer.",
            ]), fig_split),
            workedset("Splitting, and two-step stories",
                      "One step at a time; name the middle number.", [
                wex("A shop has $160$ litres and sells $70$. How much is left?",
                    ["Selling takes away — a splitting story.",
                     "$160 - 70 = 90$ litres.",
                     "Receipt: $90 + 70 = 160$ ✓."],
                    "$90$ litres",
                    ["Eq(160 - 70, 90)", "Eq(90 + 70, 160)"]),
                wex("Saruul has $300$, spends $120$, then is given $50$. How much now?",
                    ["Step 1 — spending splits: $300 - 120 = 180$.",
                     "That $180$ is what she had after the bread, not the answer.",
                     "Step 2 — the gift joins: $180 + 50 = 230$ tögrög."],
                    "$230$ tögrög",
                    ["Eq(300 - 120, 180)", "Eq(180 + 50, 230)"]),
            ]),
            tryitset("Split, or split then join", "Finish step one before starting step two.", [
                tp("A tank holds $520$ litres and $185$ are used. What is left?",
                   ["$335$ litres", "$705$ litres", "$385$ litres"],
                   "Using takes away: $520 - 185 = 335$ litres, and the receipt $335 + 185 = 520$ ✓. Adding would give $705$ — more than the tank ever held.",
                   ["Eq(520 - 185, 335)", "Eq(335 + 185, 520)"]),
                tp("Bat had $250$ tögrög, spent $80$, then earned $60$. He now has:",
                   ["$230$", "$390$", "$170$"],
                   "$250 - 80 = 170$ after spending, then $170 + 60 = 230$ after earning. Adding all three numbers gives $390$; stopping at the middle step gives $170$.",
                   ["Eq(250 - 80, 170)", "Eq(170 + 60, 230)",
                    "Eq(250 + 80 + 60, 390)"]),
                tp("A flock of $400$ loses $130$, then gains $70$. The flock is now:",
                   ["$340$", "$600$", "$270$"],
                   "$400 - 130 = 270$, then $270 + 70 = 340$. The $270$ is the flock between the two events — a real number, but not the answer.",
                   ["Eq(400 - 130, 270)", "Eq(270 + 70, 340)"]),
            ]),
            tapq("Which number is the answer?", "\"She had $300$, spent $120$, then was given $50$.\" What does the $180$ mean?",
                 ["what she had after the bread, before the gift",
                  "the final answer",
                  "the amount she was given",
                  "a mistake — $180$ should not appear"],
                 "$300 - 120 = 180$ is a real and useful number: her money between the two events. The question asks about NOW, so the gift must still be added: $180 + 50 = 230$.",
                 ["Eq(300 - 120, 180)", "Eq(180 + 50, 230)", "Ne(180, 230)"]),
            recap([
                "Decide what the story DOES — joins or splits — before touching the numbers.",
                "Joining stories add and the answer grows; splitting stories subtract and the answer shrinks.",
                "A two-step story is two complete steps; say what the middle number means so you do not hand it in.",
                "Always sense-check the size: a total below one of its parts, or a remainder above the start, is wrong.",
            ]),
            tip("Retell the problem in your own words before writing anything — \"she loses some, then gets some back\". A story you can retell is a story whose operations you already know."),
            tryitset("Chapter practice", "Story first, numbers second.", [
                tp("A school has $365$ pupils and $148$ join. The school now has:",
                   ["$513$", "$217$", "$365$"],
                   "Pupils joining is a joining story: $365 + 148 = 513$, bigger than before ✓. The $217$ is the difference, which answers nothing that was asked.",
                   ["Eq(365 + 148, 513)", "513 > 365", "Eq(365 - 148, 217)"]),
                tp("A shop had $640$ eggs, sold $260$, then received $130$. It now has:",
                   ["$510$", "$250$", "$380$"],
                   "$640 - 260 = 380$ after selling, then $380 + 130 = 510$ after the delivery. Subtracting the delivery as well gives $250$, and stopping at $380$ answers only half the story.",
                   ["Eq(640 - 260, 380)", "Eq(380 + 130, 510)",
                    "Eq(380 - 130, 250)"]),
                tp("Two herders have $180$ and $215$ animals. How many MORE does the second have?",
                   ["$35$", "$395$", "$215$"],
                   "\"How many more\" asks for the difference, so subtract: $215 - 180 = 35$. Adding would answer a question nobody asked — the combined size of both herds.",
                   ["Eq(215 - 180, 35)", "Eq(180 + 215, 395)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Word Problems\" — and the topic",
                    "Mental steps, column addition, column subtraction, fact families and now the stories themselves. Every one of them rested on the same trade: ten of any column is one of the next. Next comes multiplication, where equal groups let you count many bundles at once.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr4 = fig_groups((5, "part: 50", C_ACCENT), (9, "part: 90", C_WARM))
    return [
        prob("g3as-pr1", "Work out $360 + 400$ and $360 + 40$ in your head, and say which digit moved each time.",
             "$360 + 400 = 760$: only the hundreds digit moved, from $3$ to $7$. $360 + 40 = 400$: the tens filled up, since $6 + 4 = 10$ tens, so all ten traded up for a hundred and the tens column was left empty.",
             ["Eq(360 + 400, 760)", "Eq(6 + 4, 10)", "Eq(360 + 40, 400)"]),
        prob("g3as-pr2", "Add $267 + 158$ in columns, showing the carry, then check by adding in chunks.",
             "Ones: $7 + 8 = 15$ — write $5$, carry $1$. Tens: $6 + 5 = 11$, plus the carry is $12$ — write $2$, carry $1$. Hundreds: $2 + 1 + 1 = 4$. So $425$. Chunk check: $267 + 100 = 367$, $+50 = 417$, $+8 = 425$ ✓.",
             ["Eq(7 + 8, 15)", "Eq(6 + 5 + 1, 12)", "Eq(267 + 158, 425)",
              "Eq(367 + 50, 417)", "Eq(417 + 8, 425)"]),
        prob("g3as-pr3", "Work out $604 - 137$ and prove it with a receipt.",
             "Ones: $4 - 7$ needs a break, but the tens are empty, so a hundred is broken first: $6$ hundreds $\\to 5$, giving $10$ tens; then one of those tens opens into ones. That leaves $5$ hundreds, $9$ tens, $14$ ones. Now $14 - 7 = 7$, $9 - 3 = 6$, $5 - 1 = 4$: the answer is $467$. Receipt: $467 + 137 = 604$ ✓.",
             ["Eq(14 - 7, 7)", "Eq(9 - 3, 6)", "Eq(604 - 137, 467)",
              "Eq(467 + 137, 604)"]),
        withprobfig(prob("g3as-pr4", "The picture shows two parts of a family. Write all four facts.",
             "The parts are $50$ and $90$, so the whole is $140$. The four facts are $50 + 90 = 140$, $90 + 50 = 140$, $140 - 50 = 90$ and $140 - 90 = 50$.",
             ["Eq(50 + 90, 140)", "Eq(140 - 50, 90)", "Eq(140 - 90, 50)"]), fig_pr4),
        prob("g3as-pr5", "Find the missing number in $? - 240 = 160$, and say whether it is a part or the whole.",
             "Both $240$ and $160$ are parts — one taken away, one left — so the WHOLE is missing and you add: $240 + 160 = 400$. Check: $400 - 240 = 160$ ✓.",
             ["Eq(240 + 160, 400)", "Eq(400 - 240, 160)"]),
        prob("g3as-pr6", "A well holds $500$ litres. $180$ are drawn in the morning and $145$ in the afternoon. How much is left?",
             "Two withdrawals, so subtract twice: $500 - 180 = 320$, then $320 - 145 = 175$ litres. You can also join the withdrawals first — $180 + 145 = 325$ — and take them off together: $500 - 325 = 175$ ✓. Both roads agree.",
             ["Eq(500 - 180, 320)", "Eq(320 - 145, 175)",
              "Eq(180 + 145, 325)", "Eq(500 - 325, 175)"]),
        prob("g3as-pr7", "Bat adds $348 + 275$ and answers $513$. Find his mistake.",
             "Ones: $8 + 5 = 13$, write $3$ carry $1$. Tens: $4 + 7 = 11$ plus the carry is $12$, write $2$ carry $1$. Hundreds: $3 + 2 + 1 = 6$. The answer is $623$. Bat's $513$ is $110$ short — he dropped the carry out of the tens column, which costs one hundred, and mis-added the tens by one ten as well.",
             ["Eq(8 + 5, 13)", "Eq(4 + 7 + 1, 12)", "Eq(348 + 275, 623)",
              "Eq(623 - 513, 110)"]),
        prob("g3as-pr8", "Explain why the receipt for a subtraction is an ADDITION, not another subtraction.",
             "A subtraction splits a whole into two parts, and the family says those parts must join back to the whole. So $410 - 175 = 235$ is proved by $235 + 175 = 410$. The check is deliberately an addition because addition never needs breaking — there is no borrowing to get wrong the second time.",
             ["Eq(410 - 175, 235)", "Eq(235 + 175, 410)"]),
    ]


def test_bank():
    return [
        prob("g3as-x1", "Work out $470 + 60$ and $470 - 80$ in your head, explaining each trade.",
             "$470 + 60$: $7 + 6 = 13$ tens, so ten of them trade up for a hundred, leaving $3$ tens with $5$ hundreds — $530$. $470 - 80$: only $7$ tens are there, so a hundred breaks into ten more, giving $17 - 8 = 9$ tens with $3$ hundreds — $390$, and $390 + 80 = 470$ ✓.",
             ["Eq(7 + 6, 13)", "Eq(470 + 60, 530)", "Eq(17 - 8, 9)",
              "Eq(470 - 80, 390)", "Eq(390 + 80, 470)"]),
        prob("g3as-x2", "Add $186 + 247$ in columns and check the answer a second way.",
             "Ones: $6 + 7 = 13$ — write $3$, carry $1$. Tens: $8 + 4 = 12$ plus the carry is $13$ — write $3$, carry $1$. Hundreds: $1 + 2 + 1 = 4$. So $433$. Chunk check: $186 + 200 = 386$, $+40 = 426$, $+7 = 433$ ✓.",
             ["Eq(6 + 7, 13)", "Eq(8 + 4 + 1, 13)", "Eq(186 + 247, 433)",
              "Eq(386 + 40, 426)", "Eq(426 + 7, 433)"]),
        prob("g3as-x3", "Work out $732 - 458$ and prove it with a receipt.",
             "Ones: break a ten, $12 - 8 = 4$, leaving $2$ tens. Tens: $2 - 5$ needs a hundred broken, $12 - 5 = 7$, leaving $6$ hundreds. Hundreds: $6 - 4 = 2$. So $732 - 458 = 274$, and the receipt $274 + 458 = 732$ ✓.",
             ["Eq(12 - 8, 4)", "Eq(12 - 5, 7)", "Eq(732 - 458, 274)",
              "Eq(274 + 458, 732)"]),
        prob("g3as-x4", "Write the four facts for the family $145$, $255$ and $400$, and use one of them to find $? + 145 = 400$.",
             "The facts are $145 + 255 = 400$, $255 + 145 = 400$, $400 - 145 = 255$ and $400 - 255 = 145$. The gap in $? + 145 = 400$ is a part, so use the third fact: $400 - 145 = 255$.",
             ["Eq(145 + 255, 400)", "Eq(400 - 145, 255)",
              "Eq(400 - 255, 145)"]),
        prob("g3as-x5", "A market stall starts with $530$ apples, sells $265$, then receives $180$ more. How many now?",
             "Step 1 — selling splits: $530 - 265 = 265$ apples left. Step 2 — a delivery joins: $265 + 180 = 445$ apples. The middle number $265$ is the stall between the two events, not the answer.",
             ["Eq(530 - 265, 265)", "Eq(265 + 180, 445)"]),
        prob("g3as-x6", "Saruul says that because $250$ is bigger than $180$, the missing number in $? + 250 = 180$ must be small. What is really wrong with the question?",
             "Nothing can be added to $250$ to reach $180$, because adding only grows a number: any answer would have to make the whole SMALLER than one of its parts, which the fact family forbids. The question as written has no answer among the numbers we use. Had it read $? + 180 = 250$, the answer would be $250 - 180 = 70$.",
             ["250 > 180", "Eq(250 - 180, 70)", "Eq(70 + 180, 250)"]),
    ]


def main():
    topic = {
        "slug": "addition-and-subtraction-to-1000",
        "title": "Addition & Subtraction to 1000",
        "grade": 3,
        "status": "published",
        "blurb": ("Adding whole tens and hundreds in your head, column "
                  "addition with a carry, column subtraction with a break, "
                  "fact families and missing numbers, and reading a word "
                  "problem to decide whether it joins or splits."),
        "lessons": [
            lesson_mental(),
            lesson_column_addition(),
            lesson_column_subtraction(),
            lesson_fact_families(),
            lesson_word_problems(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "addition-and-subtraction-to-1000.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
