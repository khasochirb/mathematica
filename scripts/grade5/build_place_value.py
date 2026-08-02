#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 1: Whole Numbers & Place Value.

The topic that OPENS the primary band (grades 1–5). Grade 5 is the
school-entrance transition year, so per the resource blueprint it goes
live first, one topic at a time — exactly the way IM3 did.

Schema: the GRADE idiom (like data/genmath/6/*.json) — a GenMathTopic
whose lessons teach through embedded-set interactive steps (teach beats,
workedSet with worked items, tryItSet with tap-answer problems,
tapQuestion, funFact, recap, tip). Content is authored in English first,
per the locked buildout decision (memory/expansion-vision.md §4.7
amendment); the Mongolian mirror comes from the scripts/i18n pipeline in
a later pass, never by hand.

Every check anywhere in the structure is asserted with sympy BEFORE the
JSON is written — fail = crash, nothing written. Rounding is checked by
NEARNESS (|n - rounded| smaller than to the rival multiple), which makes
a wrong rounding target impossible to ship.

Run: python3 scripts/grade5/build_place_value.py   (then npm run verify:genmath)
"""
import json
import os
import sys

from sympy import sympify

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "5")
os.makedirs(OUT, exist_ok=True)

checks_run = 0


def _assert_checks(obj, path="topic"):
    """Walk the structure; every `check` list must sympify to True."""
    global checks_run
    if isinstance(obj, dict):
        for expr in obj.get("check", []):
            # sympify returns BooleanTrue (not Python True); bool() converts,
            # and an undecidable relational raises on bool() — both are fails.
            try:
                ok = bool(sympify(expr)) is True
            except Exception as e:  # noqa: BLE001
                raise SystemExit("%s: check does not sympify: %r (%s)" % (path, expr, e))
            if not ok:
                raise SystemExit("%s: check not True: %r" % (path, expr))
            checks_run += 1
        for k, v in obj.items():
            if k != "check":
                _assert_checks(v, "%s.%s" % (path, k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _assert_checks(v, "%s[%d]" % (path, i))


def th(n):
    """Thin-space thousands separator for KaTeX: 4708215 -> 4\\,708\\,215."""
    s = "{:,}".format(n)
    return s.replace(",", "\\,")


def near(n, target, rival):
    """Check string asserting `target` is the nearer multiple than `rival`."""
    return "Abs(%d - %d) < Abs(%d - %d)" % (n, target, n, rival)


# --------------------------------------------------------------------------
# step helpers (grade idiom)
# --------------------------------------------------------------------------

def teach(eyebrow, title, beats):
    return {"kind": "teach", "eyebrow": eyebrow, "title": title, "beats": beats}


def workedset(title, intro, examples):
    return {"kind": "workedSet", "eyebrow": "Worked examples", "title": title,
            "intro": intro, "examples": examples}


def wex(prompt, steps, answer, check):
    return {"prompt": prompt, "steps": steps, "answer": answer, "check": check}


def tryitset(title, intro, problems, eyebrow="Try it yourself"):
    return {"kind": "tryItSet", "eyebrow": eyebrow, "title": title,
            "intro": intro, "problems": problems}


def tp(prompt, options, explanation, check, correct=0):
    assert len(set(options)) == len(options), "duplicate options: %r" % prompt
    return {"prompt": prompt, "options": options, "correctIndex": correct,
            "explanation": explanation, "check": check}


def tapq(title, prompt, options, explanation, check):
    assert len(set(options)) == len(options), "duplicate options: %r" % prompt
    return {"kind": "tapQuestion", "eyebrow": "Quick check", "title": title,
            "prompt": prompt, "options": options, "correctIndex": 0,
            "explanation": explanation, "check": check}


def funfact(title, body, eyebrow="Fun fact"):
    return {"kind": "funFact", "eyebrow": eyebrow, "title": title, "body": body}


def recap(points):
    return {"kind": "recap", "eyebrow": "Recap", "title": "What you learned",
            "points": points}


def tip(body):
    return {"kind": "tip", "eyebrow": "Practice", "title": "Time to practice",
            "body": body}


def prob(id_, statement, solution, check):
    return {"id": id_, "statement": statement, "solution": solution, "check": check}


# ==========================================================================
# Lesson 1 — Reading & Writing Large Numbers
# ==========================================================================

def lesson_reading():
    return {
        "slug": "reading-and-writing-large-numbers",
        "title": "Reading & Writing Large Numbers",
        "concreteComparison": (
            "Ulaanbaatar has about $1\\,600\\,000$ people. Try saying that "
            "number out loud — if you read it digit by digit, it's a mouthful. "
            "But split it into groups of three — $1$ | $600$ | $000$ — and it "
            "reads itself: **one million, six hundred thousand**. The commas "
            "in a big number are exactly those group lines."),
        "objective": (
            "Read and write numbers up to millions using digit groups "
            "(periods), and translate between numerals, words, and expanded "
            "form."),
        "concept": [
            "Big numbers are read in **groups of three digits** called "
            "periods: ones, thousands, millions. $4\\,708\\,215$ splits as "
            "$4$ | $708$ | $215$: four million, seven hundred eight "
            "thousand, two hundred fifteen.",
            "Inside each group you only ever read a number up to $999$ — "
            "then you say the group's name (*million*, *thousand*). That's "
            "why you never need new words for bigger numbers, just new "
            "group names.",
            "**Expanded form** stretches a number into what each digit is "
            "worth: $52\\,304 = 50\\,000 + 2\\,000 + 300 + 4$. A zero digit "
            "simply contributes nothing — but it still holds its place.",
        ],
        "keyIdea": (
            "Split a big number into groups of three from the right, read "
            "each group like a small number, and say the group's name. "
            "Expanded form shows what every digit is worth."),
        "facts": [
            {"title": "The periods",
             "latex": "\\underbrace{4}_{\\text{millions}}\\,|\\,\\underbrace{708}_{\\text{thousands}}\\,|\\,\\underbrace{215}_{\\text{ones}}",
             "explanation": "Groups of three digits, named from the right: ones, thousands, millions."},
            {"title": "Expanded form",
             "latex": "52\\,304 = 50\\,000 + 2\\,000 + 300 + 4",
             "explanation": "Each digit times its place — zeros hold a place but add nothing."},
        ],
        "workedExamples": [
            {"id": "g5pv-l1-we1",
             "statement": "Write the numeral for *three hundred forty-five thousand, six hundred two*.",
             "note": "Work group by group: thousands group first, then the ones group.",
             "solution": ("The thousands group is $345$; the ones group is $602$. "
                          "Numeral: $345\\,602$. (Note the $0$ in the tens place — "
                          "\"six hundred two\" has no tens, so a zero holds that spot.)"),
             "badges": [{"text": "core"}],
             "check": ["Eq(345*1000 + 602, 345602)"]},
            {"id": "g5pv-l1-we2",
             "statement": "Write $4\\,708\\,215$ in words.",
             "note": "Split into periods first.",
             "solution": ("$4$ | $708$ | $215$: four million, seven hundred eight "
                          "thousand, two hundred fifteen."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*1000000 + 708*1000 + 215, 4708215)"]},
        ],
        "commonMistakes": [
            {"text": "Dropping the zeros that hold empty places — writing \"seventy thousand fifty\" as 7050.",
             "correction": "Seventy thousand is 70,000 — five digits. The fifty fills the last two: 70,050. Count the places, then fill the gaps with zeros.",
             "authored": True},
            {"text": "Reading digits one at a time (\"four, seven, zero, eight...\") instead of by groups.",
             "correction": "Group from the RIGHT in threes, then read each group like a small number followed by its period name.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5pv-l1-t1",
             "statement": "Write the numeral for *two million, forty thousand, nine*.",
             "solution": "$2$ | $040$ | $009$ = $2\\,040\\,009$ — zeros hold every empty place.",
             "check": ["Eq(2*1000000 + 40*1000 + 9, 2040009)"]},
            {"id": "g5pv-l1-t2",
             "statement": "Write $89\\,041$ in expanded form.",
             "solution": "$80\\,000 + 9\\,000 + 40 + 1$. The hundreds digit is $0$, so it contributes nothing.",
             "check": ["Eq(80000 + 9000 + 40 + 1, 89041)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Read in groups of three", [
                "A long number is hard to read digit by digit — so we split it into **groups of three from the right**, called periods: ones, thousands, millions.",
                "$4\\,708\\,215$ splits as $4$ | $708$ | $215$: **four million**, **seven hundred eight thousand**, **two hundred fifteen**.",
                "Inside a group you never read past $999$ — then you just say the group's name. Big numbers are three-digit numbers wearing name tags.",
            ]),
            workedset("Between words and numerals",
                      "Split into periods, read each group, say its name.", [
                wex("Write the numeral for *three hundred forty-five thousand, six hundred two*.",
                    ["Thousands group: $345$. Ones group: $602$ — note the zero tens.",
                     "Numeral: $345\\,602$."],
                    "$345\\,602$", ["Eq(345*1000 + 602, 345602)"]),
                wex("Write $4\\,708\\,215$ in words.",
                    ["Periods: $4$ | $708$ | $215$.",
                     "Four million, seven hundred eight thousand, two hundred fifteen."],
                    "four million, seven hundred eight thousand, two hundred fifteen",
                    ["Eq(4*1000000 + 708*1000 + 215, 4708215)"]),
            ]),
            tryitset("Words to numerals", "Watch for the zeros that hold empty places.", [
                tp("The numeral for *seventy thousand fifty* is:",
                   ["$70\\,050$", "$7\\,050$", "$70\\,500$"],
                   "Seventy thousand needs five digits: $70\\,000$. The fifty fills the last two places: $70\\,050$.",
                   ["Eq(70*1000 + 50, 70050)"]),
                tp("The numeral for *two million five* is:",
                   ["$2\\,000\\,005$", "$2\\,005$", "$2\\,500\\,000$"],
                   "Two million is $2\\,000\\,000$; the five sits in the ones place — every place between is a zero.",
                   ["Eq(2*1000000 + 5, 2000005)"]),
                tp("$6$ hundred-thousands, $3$ thousands and $9$ tens make:",
                   ["$603\\,090$", "$639\\,000$", "$60\\,390$"],
                   "$600\\,000 + 3\\,000 + 90 = 603\\,090$ — zeros hold the ten-thousands, hundreds and ones.",
                   ["Eq(600000 + 3000 + 90, 603090)"]),
            ]),
            tapq("Say the group", "In $5\\,214\\,830$, the digits $214$ form which period?",
                 ["the thousands", "the millions", "the ones", "the hundreds"],
                 "Groups of three from the right: $830$ is the ones period, $214$ the thousands, $5$ the millions — five million, two hundred fourteen thousand, eight hundred thirty.",
                 ["Eq(5*1000000 + 214*1000 + 830, 5214830)"]),
            funfact("Mongolian reads numbers the same way",
                    "Мянга (thousand) and сая (million) are period names too: $4\\,708\\,215$ is *дөрвөн сая долоон зуун найман мянга хоёр зуун арван тав*. Different words, exactly the same groups of three — the system is international."),
            teach("Concept B", "Expanded form — what each digit is worth", [
                "**Expanded form** stretches a number into a sum showing what every digit is worth: $52\\,304 = 50\\,000 + 2\\,000 + 300 + 4$.",
                "A **zero digit adds nothing** to the sum — but it still holds its place. Skip it in the sum, never in the numeral.",
                "Expanded form is the x-ray of a number: it shows the skeleton that place value builds.",
            ]),
            workedset("Stretching and rebuilding",
                      "Digit times place, added up — or the reverse.", [
                wex("Write $52\\,304$ in expanded form.",
                    ["$5$ ten-thousands, $2$ thousands, $3$ hundreds, $0$ tens, $4$ ones.",
                     "$52\\,304 = 50\\,000 + 2\\,000 + 300 + 4$."],
                    "$50\\,000 + 2\\,000 + 300 + 4$",
                    ["Eq(50000 + 2000 + 300 + 4, 52304)"]),
                wex("What number is $700\\,000 + 40\\,000 + 600 + 8$?",
                    ["Fill the places: $7$ hundred-thousands, $4$ ten-thousands, $0$ thousands, $6$ hundreds, $0$ tens, $8$ ones.",
                     "$740\\,608$."],
                    "$740\\,608$", ["Eq(700000 + 40000 + 600 + 8, 740608)"]),
            ]),
            tryitset("Expanded form", "Stretch it out — or rebuild the numeral.", [
                tp("The expanded form of $89\\,041$ is:",
                   ["$80\\,000 + 9\\,000 + 40 + 1$",
                    "$8\\,000 + 900 + 40 + 1$",
                    "$80\\,000 + 9\\,000 + 400 + 1$"],
                   "$8$ ten-thousands, $9$ thousands, $0$ hundreds, $4$ tens, $1$ one — the zero hundreds simply drops from the sum.",
                   ["Eq(80000 + 9000 + 40 + 1, 89041)"]),
                tp("$300\\,000 + 5\\,000 + 20 + 7$ equals:",
                   ["$305\\,027$", "$350\\,270$", "$30\\,527$"],
                   "Place the digits with zeros holding the gaps: $305\\,027$.",
                   ["Eq(300000 + 5000 + 20 + 7, 305027)"]),
                tp("Which term is MISSING from $46\\,213 = 40\\,000 + 6\\,000 + 10 + 3$?",
                   ["$200$", "$2\\,000$", "$20$"],
                   "The hundreds digit is $2$, worth $200$: $40\\,000 + 6\\,000 + 200 + 10 + 3 = 46\\,213$.",
                   ["Eq(40000 + 6000 + 200 + 10 + 3, 46213)"]),
            ]),
            tapq("Rebuild it", "$900\\,000 + 80\\,000 + 3\\,000 + 5$ equals:",
                 ["$983\\,005$", "$98\\,305$", "$983\\,500$", "$9\\,830\\,005$"],
                 "$9$ hundred-thousands, $8$ ten-thousands, $3$ thousands, $0$ hundreds, $0$ tens, $5$ ones: $983\\,005$.",
                 ["Eq(900000 + 80000 + 3000 + 5, 983005)"]),
            recap([
                "Big numbers read in groups of three (periods): ones, thousands, millions.",
                "Inside a group you never read past 999 — then say the group's name.",
                "Zeros add nothing to the value but hold places — never drop them from the numeral.",
                "Expanded form shows what each digit is worth: digit × place, added up.",
            ]),
            tip("Mixed reading and writing — watch the zero-filled places; they cause almost every error in this lesson."),
            tryitset("Mixed practice", "A little of everything you learned.", [
                tp("The numeral for *five hundred thousand, sixty* is:",
                   ["$500\\,060$", "$500\\,600$", "$50\\,060$"],
                   "Five hundred thousand = $500\\,000$; sixty fills the tens and ones: $500\\,060$.",
                   ["Eq(500000 + 60, 500060)"]),
                tp("$1\\,000\\,000 + 20\\,000 + 300$ equals:",
                   ["$1\\,020\\,300$", "$1\\,200\\,300$", "$1\\,002\\,300$"],
                   "One million, plus $2$ ten-thousands, plus $3$ hundreds: $1\\,020\\,300$.",
                   ["Eq(1000000 + 20000 + 300, 1020300)"]),
                tp("In words, $30\\,007$ is:",
                   ["thirty thousand seven", "three thousand seven", "thirty thousand seventy"],
                   "$30$ | $007$: thirty thousand, seven — three zeros hold the hundreds, tens and the empty spots.",
                   ["Eq(30*1000 + 7, 30007)"]),
                tp("The expanded form of $205\\,410$ is:",
                   ["$200\\,000 + 5\\,000 + 400 + 10$",
                    "$200\\,000 + 50\\,000 + 400 + 10$",
                    "$20\\,000 + 5\\,000 + 400 + 10$"],
                   "$2$ hundred-thousands, $0$ ten-thousands, $5$ thousands, $4$ hundreds, $1$ ten, $0$ ones.",
                   ["Eq(200000 + 5000 + 400 + 10, 205410)"]),
                tp("Which is the numeral for *one million, one thousand, one*?",
                   ["$1\\,001\\,001$", "$1\\,000\\,101$", "$1\\,100\\,001$"],
                   "$1$ | $001$ | $001$ — each period gets its three digits: $1\\,001\\,001$.",
                   ["Eq(1000000 + 1000 + 1, 1001001)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Reading & Writing Large Numbers\"",
                    "You can now read any number up to the millions — and the same three-digit-group trick keeps working forever: billions, trillions, and beyond are just more name tags. Next: what a single digit is worth depending on where it stands.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — The Value of a Digit
# ==========================================================================

def lesson_digit_value():
    return {
        "slug": "the-value-of-a-digit",
        "title": "The Value of a Digit",
        "concreteComparison": (
            "The digit $5$ appears twice in $5\\,352$ — but the two fives "
            "are not worth the same. The left one stands in the thousands "
            "place and is worth $5\\,000$; the right one stands in the tens "
            "place and is worth $50$. Same symbol, a hundred times the "
            "value. In our number system, **where** a digit stands decides "
            "**what** it is worth."),
        "objective": (
            "Name the place of any digit up to millions, state its value, "
            "and use the ten-times relationship between neighbouring "
            "places."),
        "concept": [
            "Each position in a numeral is a **place**: ones, tens, "
            "hundreds, thousands, ten-thousands, hundred-thousands, "
            "millions. A digit's **value** is the digit times its place: "
            "the $7$ in $4\\,708$ stands in the hundreds place, so it is "
            "worth $7 \\times 100 = 700$.",
            "Neighbouring places differ by a factor of **ten**: each step "
            "left multiplies a digit's worth by $10$, each step right "
            "divides it by $10$. The $5$ in $5\\,340$ is worth $5\\,000$ — "
            "ten times the $500$ it would be worth one place to the right.",
            "That factor of ten is the whole engine of our numerals: ten "
            "ones trade for one ten, ten tens for one hundred, ten "
            "hundreds for one thousand — the same trade at every step.",
        ],
        "keyIdea": (
            "A digit's value is the digit times its place, and each step "
            "left multiplies that value by ten. Place decides worth."),
        "facts": [
            {"title": "Digit value",
             "latex": "\\text{value} = \\text{digit} \\times \\text{place}",
             "explanation": "The 7 in 4,708 is worth 7 × 100 = 700."},
            {"title": "The ten-times ladder",
             "latex": "1 \\to 10 \\to 100 \\to 1\\,000 \\to 10\\,000 \\to \\cdots",
             "explanation": "Each place is ten of the place before it — the same trade all the way up."},
        ],
        "workedExamples": [
            {"id": "g5pv-l2-we1",
             "statement": "What is the value of the digit $7$ in $4\\,708$? And in $7\\,048$?",
             "note": "Name the place first, then multiply.",
             "solution": ("In $4\\,708$ the $7$ stands in the hundreds place: worth "
                          "$7 \\times 100 = 700$. In $7\\,048$ it stands in the "
                          "thousands place: worth $7 \\times 1\\,000 = 7\\,000$ — "
                          "ten times as much."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7*100, 700)", "Eq(7*1000, 7000)", "Eq(7000, 10*700)"]},
            {"id": "g5pv-l2-we2",
             "statement": "In $5\\,352$, how many times the value of the right-hand $5$ is the left-hand $5$?",
             "note": "Find both values, then divide.",
             "solution": ("Left $5$: thousands place, worth $5\\,000$. Right $5$: tens "
                          "place, worth $50$. $5\\,000 \\div 50 = 100$ — two places "
                          "apart means $10 \\times 10 = 100$ times the value."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*1000, 5000)", "Eq(5*10, 50)", "Eq(5000/50, 100)"]},
        ],
        "commonMistakes": [
            {"text": "Giving the digit itself as its value — \"the 7 in 4,708 is worth 7\".",
             "correction": "Seven WHAT? Hundreds. The value is digit × place: 7 × 100 = 700.",
             "authored": True},
            {"text": "Naming places from the left instead of the right.",
             "correction": "Places count from the RIGHT: ones, tens, hundreds... The left-most digit's place depends on how long the number is.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5pv-l2-t1",
             "statement": "State the value of the digit $9$ in $2\\,914\\,306$.",
             "solution": "The $9$ stands in the hundred-thousands place: $9 \\times 100\\,000 = 900\\,000$.",
             "check": ["Eq(9*100000, 900000)"]},
            {"id": "g5pv-l2-t2",
             "statement": "The digit $3$ appears in both $631$ and $6\\,310$. How do its values compare?",
             "solution": "In $631$: tens place, worth $30$. In $6\\,310$: hundreds place, worth $300$ — ten times as much, because it moved one place left.",
             "check": ["Eq(3*10, 30)", "Eq(3*100, 300)", "Eq(300, 10*30)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Place decides worth", [
                "Every position in a numeral is a **place**: ones, tens, hundreds, thousands, and so on, counted from the RIGHT.",
                "A digit's **value** is the digit times its place. The $7$ in $4\\,708$ stands in the hundreds place — it is worth $7 \\times 100 = 700$, not $7$.",
                "Move the same digit one place left and it is worth ten times as much: in $7\\,048$ the $7$ is worth $7\\,000$.",
            ]),
            workedset("Digit times place",
                      "Name the place first — the multiplication is the easy part.", [
                wex("Find the value of the $7$ in $4\\,708$ and in $7\\,048$.",
                    ["$4\\,708$: the $7$ is in the hundreds place — $7 \\times 100 = 700$.",
                     "$7\\,048$: thousands place — $7 \\times 1\\,000 = 7\\,000$, ten times as much."],
                    "$700$ and $7\\,000$",
                    ["Eq(7*100, 700)", "Eq(7*1000, 7000)", "Eq(7000, 10*700)"]),
                wex("Compare the two fives in $5\\,352$.",
                    ["Left $5$: thousands place, worth $5\\,000$. Right $5$: tens place, worth $50$.",
                     "$5\\,000 \\div 50 = 100$: two places apart = $100$ times the value."],
                    "$100$ times", ["Eq(5000/50, 100)"]),
            ]),
            tryitset("Name the place, state the value", "Count places from the right.", [
                tp("The value of the $9$ in $2\\,914\\,306$ is:",
                   ["$900\\,000$", "$9\\,000$", "$90\\,000$"],
                   "Counting from the right, the $9$ stands in the hundred-thousands place: $9 \\times 100\\,000 = 900\\,000$.",
                   ["Eq(9*100000, 900000)"]),
                tp("The value of the $4$ in $84\\,210$ is:",
                   ["$4\\,000$", "$40\\,000$", "$400$"],
                   "The $4$ stands in the thousands place: $4 \\times 1\\,000 = 4\\,000$.",
                   ["Eq(4*1000, 4000)"]),
                tp("In which number is the digit $6$ worth $60\\,000$?",
                   ["$367\\,120$", "$36\\,712$", "$3\\,671\\,200$"],
                   "$367\\,120$ puts the $6$ in the ten-thousands place: $6 \\times 10\\,000 = 60\\,000$.",
                   ["Eq(6*10000, 60000)"]),
            ]),
            tapq("Same digit, new place", "The $3$ in $631$ is worth $30$. What is the $3$ in $6\\,310$ worth?",
                 ["$300$", "$30$", "$3\\,000$", "$3$"],
                 "The whole number slid one place left, so the $3$ moved from tens to hundreds: $3 \\times 100 = 300$ — ten times its old value.",
                 ["Eq(3*100, 300)", "Eq(300, 10*30)"]),
            funfact("Why ten?",
                    "Our number system is base ten almost certainly because we count on ten fingers. Computers, with their two-state switches, use base two — where the number $13$ is written $1101$. Same idea, different trade: each place is worth TWO of the place before."),
            teach("Concept B", "The ten-times ladder", [
                "Neighbouring places always differ by a factor of **ten**: ten ones make a ten, ten tens make a hundred, ten hundreds make a thousand — the same trade at every rung.",
                "So one step left multiplies a digit's value by $10$; two steps left multiply it by $100$; three steps by $1\\,000$.",
                "This is why $10 \\times$ any number just shifts its digits one place left: $10 \\times 372 = 3\\,720$. The digits keep their order; every one of them gets ten times richer.",
            ]),
            workedset("Climbing the ladder",
                      "Each step left is a ×10 — count the steps.", [
                wex("How many times the value of the $8$ in $283$ is the $8$ in $86\\,000$?",
                    ["In $283$: tens place, worth $80$. In $86\\,000$: ten-thousands place, worth $80\\,000$.",
                     "$80\\,000 \\div 80 = 1\\,000$ — three places apart, so $10 \\times 10 \\times 10$."],
                    "$1\\,000$ times", ["Eq(8*10, 80)", "Eq(8*10000, 80000)", "Eq(80000/80, 1000)"]),
                wex("Compute $10 \\times 372$ and explain what happened to the digits.",
                    ["$10 \\times 372 = 3\\,720$.",
                     "Every digit slid one place left — the $3$ went from hundreds ($300$) to thousands ($3\\,000$), and a zero now holds the ones."],
                    "$3\\,720$", ["Eq(10*372, 3720)", "Eq(10*300, 3000)"]),
            ]),
            tryitset("Ten-times thinking", "Count the places between the digits.", [
                tp("$10 \\times 4\\,506$ equals:",
                   ["$45\\,060$", "$450\\,600$", "$40\\,560$"],
                   "Multiplying by ten slides every digit one place left and a zero fills the ones: $45\\,060$. ($450\\,600$ is a hundred times; $40\\,560$ scrambles the digits.)",
                   ["Eq(10*4506, 45060)"]),
                tp("The $2$ in $52\\,000$ is how many times the $2$ in $520$?",
                   ["$100$ times", "$10$ times", "$1\\,000$ times"],
                   "$2\\,000$ against $20$: two places apart, $2000 \\div 20 = 100$.",
                   ["Eq(2000/20, 100)"]),
                tp("Ten thousands make:",
                   ["$10\\,000$", "$1\\,000$", "$100\\,000$"],
                   "Ten of $1\\,000$ is $10\\,000$ — the next rung of the ladder.",
                   ["Eq(10*1000, 10000)"]),
            ]),
            tapq("Count the steps", "The value of a digit is multiplied by how much when it moves TWO places left?",
                 ["$100$", "$20$", "$10$", "$1\\,000$"],
                 "Each step is a ×10, and two steps make $10 \\times 10 = 100$.",
                 ["Eq(10*10, 100)"]),
            recap([
                "A digit's value = the digit × its place; the place is counted from the right.",
                "Each place left multiplies the value by ten — the ten-times ladder.",
                "Two places apart = ×100; three places = ×1,000.",
                "×10 slides all digits one place left and fills the ones with a zero.",
            ]),
            tip("Practice naming places fast — every later topic (comparing, rounding, the four operations) leans on it."),
            tryitset("Mixed practice", "Places, values, and the ladder together.", [
                tp("The value of the $5$ in $1\\,058\\,240$ is:",
                   ["$50\\,000$", "$5\\,000$", "$500\\,000$"],
                   "The $5$ stands in the ten-thousands place: $5 \\times 10\\,000 = 50\\,000$.",
                   ["Eq(5*10000, 50000)"]),
                tp("Which digit of $739\\,406$ is worth $9\\,000$?",
                   ["the $9$", "the $3$", "the $4$"],
                   "The $9$ stands in the thousands place: $9 \\times 1\\,000 = 9\\,000$.",
                   ["Eq(9*1000, 9000)"]),
                tp("$100 \\times 68$ equals:",
                   ["$6\\,800$", "$680$", "$68\\,000$"],
                   "Two steps left: $68 \\to 6\\,800$, zeros holding tens and ones.",
                   ["Eq(100*68, 6800)"]),
                tp("The $1$ in $612\\,530$ is how many times the $1$ in $6\\,125$?",
                   ["$100$ times", "$10$ times", "the same"],
                   "$10\\,000$ against $100$: $10000 \\div 100 = 100$ times.",
                   ["Eq(10000/100, 100)"]),
                tp("Ten hundred-thousands make:",
                   ["one million", "one hundred-thousand", "ten thousand"],
                   "$10 \\times 100\\,000 = 1\\,000\\,000$ — the ladder reaches the millions.",
                   ["Eq(10*100000, 1000000)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"The Value of a Digit\"",
                    "Place value is THE big idea of arithmetic — every algorithm you'll ever use for adding, subtracting, multiplying or dividing is just careful bookkeeping of these places. Next: putting numbers in order.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Comparing & Ordering
# ==========================================================================

def lesson_comparing():
    return {
        "slug": "comparing-and-ordering-numbers",
        "title": "Comparing & Ordering Numbers",
        "concreteComparison": (
            "Two aimags report their herd counts: $84\\,210$ and $9\\,875$. "
            "Which is larger? You don't need to study the digits — the "
            "first number is five digits long and the second only four, "
            "and a five-digit number ALWAYS beats a four-digit one. Length "
            "first, then digits: that's the whole method."),
        "objective": (
            "Compare whole numbers using digit count and left-to-right "
            "digit comparison, write the result with $<$ and $>$, and "
            "order lists of numbers."),
        "concept": [
            "**More digits wins.** A number with more digits is always "
            "larger: $84\\,210 > 9\\,875$ before you look at a single "
            "digit, because five places beat four.",
            "**Same length: compare from the LEFT.** March through the "
            "digits together and stop at the first difference — the "
            "bigger digit there decides. $56\\,342$ vs $56\\,297$: the "
            "ten-thousands and thousands agree ($5$, $6$), the hundreds "
            "differ ($3 > 2$), so $56\\,342$ is larger. The digits after "
            "the first difference cannot matter — they are worth less "
            "than the place already decided.",
            "**Ordering** is repeated comparing: to sort a list, compare "
            "pairs and line them up smallest to largest (ascending) or "
            "largest to smallest (descending). The symbols point at the "
            "smaller number: $9\\,875 < 84\\,210$.",
        ],
        "keyIdea": (
            "Compare digit counts first — more digits wins. Same count: "
            "scan from the left and the first differing digit decides."),
        "facts": [
            {"title": "The two-step compare",
             "latex": "\\text{count digits} \\to \\text{scan from the left}",
             "explanation": "More digits wins outright; otherwise the first difference decides."},
            {"title": "The symbols",
             "latex": "9\\,875 < 84\\,210 \\quad\\quad 84\\,210 > 9\\,875",
             "explanation": "The small end of the symbol points at the smaller number."},
        ],
        "workedExamples": [
            {"id": "g5pv-l3-we1",
             "statement": "Compare $56\\,342$ and $56\\,297$.",
             "note": "Same digit count — scan from the left.",
             "solution": ("Ten-thousands: $5 = 5$. Thousands: $6 = 6$. Hundreds: "
                          "$3 > 2$ — decided. $56\\,342 > 56\\,297$. The later digits "
                          "($42$ vs $97$) cannot overturn a hundreds-place lead."),
             "badges": [{"text": "core"}],
             "check": ["56342 > 56297", "Eq(56342 - 56297, 45)"]},
            {"id": "g5pv-l3-we2",
             "statement": "Order from smallest to largest: $23\\,502$, $9\\,999$, $23\\,089$, $102\\,000$.",
             "note": "Digit counts first, then left-to-right scans within equal lengths.",
             "solution": ("Digit counts: $9\\,999$ has four digits (smallest), "
                          "$102\\,000$ has six (largest). Between the five-digit pair: "
                          "$23\\,089 < 23\\,502$ (hundreds: $0 < 5$). Order: $9\\,999 < "
                          "23\\,089 < 23\\,502 < 102\\,000$."),
             "badges": [{"text": "core"}],
             "check": ["9999 < 23089", "23089 < 23502", "23502 < 102000"]},
        ],
        "commonMistakes": [
            {"text": "Comparing from the right because that's where arithmetic starts.",
             "correction": "Addition works right-to-left; COMPARING works left-to-right, because the left-most places are worth the most.",
             "authored": True},
            {"text": "Letting a big right-hand digit win — thinking 56,297 beats 56,342 because 9 > 4.",
             "correction": "The first difference (hundreds: 3 vs 2) already decided. Digits further right are worth less than that whole difference.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5pv-l3-t1",
             "statement": "Place the correct symbol: $308\\,415 \\;\\square\\; 308\\,514$.",
             "solution": "Scan left: $3, 0, 8$ agree; hundreds differ, $4 < 5$. So $308\\,415 < 308\\,514$.",
             "check": ["308415 < 308514"]},
            {"id": "g5pv-l3-t2",
             "statement": "Order from largest to smallest: $45\\,670$, $45\\,760$, $9\\,999$.",
             "solution": "$45\\,760 > 45\\,670$ (hundreds $7 > 6$), and the four-digit $9\\,999$ is last: $45\\,760 > 45\\,670 > 9\\,999$.",
             "check": ["45760 > 45670", "45670 > 9999"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "More digits wins", [
                "Comparing starts with a count: a number with MORE DIGITS is always larger — $84\\,210 > 9\\,875$ before you read a single digit.",
                "Why: the shortest five-digit number ($10\\,000$) already beats the longest four-digit one ($9\\,999$).",
                "The symbols: the small pointed end aims at the smaller number — $9\\,875 < 84\\,210$.",
            ]),
            workedset("Count first",
                      "Digit count settles most comparisons instantly.", [
                wex("Compare $84\\,210$ and $9\\,875$.",
                    ["$84\\,210$ has five digits; $9\\,875$ has four.",
                     "Five places beat four: $84\\,210 > 9\\,875$."],
                    "$84\\,210 > 9\\,875$", ["84210 > 9875", "10000 > 9999"]),
                wex("Compare $99\\,999$ and $100\\,000$.",
                    ["Five digits against six — the six-digit number wins even though its digits are mostly zeros.",
                     "$100\\,000 > 99\\,999$: one more place outweighs all those nines."],
                    "$100\\,000 > 99\\,999$", ["100000 > 99999", "Eq(100000 - 99999, 1)"]),
            ]),
            tryitset("Digit-count comparisons", "Count the places before reading the digits.", [
                tp("Which symbol fits: $7\\,654 \\;\\square\\; 10\\,001$?",
                   ["$<$", "$>$", "$=$"],
                   "Four digits against five: $7\\,654 < 10\\,001$, whatever the digits say.",
                   ["7654 < 10001"]),
                tp("The largest of $989$, $10\\,010$, $9\\,898$ is:",
                   ["$10\\,010$", "$9\\,898$", "$989$"],
                   "Only $10\\,010$ has five digits — it wins on length alone.",
                   ["10010 > 9898", "9898 > 989"]),
                tp("Which is smaller: $1\\,000\\,000$ or $999\\,999$?",
                   ["$999\\,999$", "$1\\,000\\,000$", "they are equal"],
                   "Six digits against seven: $999\\,999 < 1\\,000\\,000$ — by exactly one.",
                   ["999999 < 1000000"]),
            ]),
            tapq("Length check", "Which is larger: $50\\,000$ or $49\\,999$?",
                 ["$50\\,000$", "$49\\,999$", "they are equal", "cannot tell"],
                 "Same length, so scan from the left: ten-thousands $5 > 4$ — decided at the very first digit. $50\\,000 > 49\\,999$.",
                 ["50000 > 49999"]),
            funfact("The judge only needs one difference",
                    "Dictionaries order words exactly the way we order numbers: compare letter by letter from the left and stop at the first difference. That's why this method is called LEXICOGRAPHIC — the dictionary method. Numbers of equal length sort like words."),
            teach("Concept B", "Same length? Scan from the left", [
                "Equal digit counts: march through the digits TOGETHER from the left and stop at the first difference — the bigger digit there decides.",
                "$56\\,342$ vs $56\\,297$: $5=5$, $6=6$, then hundreds $3 > 2$ — done. $56\\,342$ is larger.",
                "Digits after the first difference can never overturn it: everything to the right is worth less than that one place difference.",
            ]),
            workedset("The left-to-right scan",
                      "Stop at the first difference — the rest is noise.", [
                wex("Compare $56\\,342$ and $56\\,297$.",
                    ["Scan: $5=5$, $6=6$, hundreds $3>2$ — decided.",
                     "$56\\,342 > 56\\,297$, even though $97$ ends bigger than $42$."],
                    "$56\\,342 > 56\\,297$", ["56342 > 56297"]),
                wex("Order $23\\,502$, $9\\,999$, $23\\,089$, $102\\,000$ from smallest to largest.",
                    ["Lengths: $9\\,999$ (4 digits) smallest, $102\\,000$ (6 digits) largest.",
                     "Five-digit pair: $23\\,089 < 23\\,502$ — hundreds $0 < 5$.",
                     "$9\\,999 < 23\\,089 < 23\\,502 < 102\\,000$."],
                    "$9\\,999 < 23\\,089 < 23\\,502 < 102\\,000$",
                    ["9999 < 23089", "23089 < 23502", "23502 < 102000"]),
            ]),
            tryitset("Scan and order", "Left to right; first difference decides.", [
                tp("Which symbol fits: $308\\,415 \\;\\square\\; 308\\,514$?",
                   ["$<$", "$>$", "$=$"],
                   "$3, 0, 8$ agree; hundreds differ $4 < 5$: $308\\,415 < 308\\,514$.",
                   ["308415 < 308514"]),
                tp("The largest of $45\\,670$, $45\\,760$, $45\\,067$ is:",
                   ["$45\\,760$", "$45\\,670$", "$45\\,067$"],
                   "All share $45$; the hundreds decide: $7 > 6 > 0$.",
                   ["45760 > 45670", "45670 > 45067"]),
                tp("Which list is in order from smallest to largest?",
                   ["$8\\,904 < 64\\,001 < 64\\,100$",
                    "$64\\,100 < 64\\,001 < 8\\,904$",
                    "$64\\,001 < 8\\,904 < 64\\,100$"],
                   "$8\\,904$ has four digits (smallest); then $64\\,001 < 64\\,100$ since the hundreds differ $0 < 1$.",
                   ["8904 < 64001", "64001 < 64100"]),
            ]),
            tapq("First difference", "Comparing $71\\,289$ and $71\\,298$: which place decides?",
                 ["the tens", "the ones", "the hundreds", "the thousands"],
                 "Scan: $7, 1, 2$ agree; tens differ ($8$ vs $9$) — decided there. $71\\,289 < 71\\,298$.",
                 ["71289 < 71298"]),
            recap([
                "More digits wins — the shortest longer number beats the longest shorter one.",
                "Equal lengths: scan from the LEFT; the first differing digit decides.",
                "Digits right of the first difference can never overturn it.",
                "The symbol's small end points at the smaller number.",
            ]),
            tip("Order these without computing anything — length first, then a single left-to-right scan each."),
            tryitset("Mixed practice", "Compare and order, the two-step way.", [
                tp("Which symbol fits: $99\\,090 \\;\\square\\; 99\\,900$?",
                   ["$<$", "$>$", "$=$"],
                   "$9, 9$ agree; hundreds $0 < 9$: $99\\,090 < 99\\,900$.",
                   ["99090 < 99900"]),
                tp("The smallest of $210\\,345$, $210\\,435$, $209\\,999$ is:",
                   ["$209\\,999$", "$210\\,345$", "$210\\,435$"],
                   "Thousands place: $209$ starts below $210$ — $209\\,999$ loses to both before the later digits matter.",
                   ["209999 < 210345", "210345 < 210435"]),
                tp("A town of $48\\,350$ people and a town of $48\\,530$: which is bigger?",
                   ["the second — $48\\,530$", "the first — $48\\,350$", "they are equal"],
                   "Hundreds decide: $3 < 5$, so $48\\,530$ is the bigger town.",
                   ["48350 < 48530"]),
                tp("Which number makes the statement true: $67\\,\\square 41 > 67\\,841$?",
                   ["$9$", "$8$", "$7$"],
                   "The hundreds digit must beat $8$: only $9$ works — $67\\,941 > 67\\,841$.",
                   ["67941 > 67841"]),
                tp("In order from largest to smallest:",
                   ["$100\\,200 > 99\\,999 > 89\\,999$",
                    "$99\\,999 > 100\\,200 > 89\\,999$",
                    "$89\\,999 > 99\\,999 > 100\\,200$"],
                   "Six digits first, then the five-digit pair by their leading digits: $9 > 8$.",
                   ["100200 > 99999", "99999 > 89999"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Comparing & Ordering\"",
                    "Two moves — count the digits, scan from the left — settle any comparison of whole numbers, however large. Next: rounding, where you'll trade exactness for convenience on purpose.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Rounding
# ==========================================================================

def lesson_rounding():
    return {
        "slug": "rounding-whole-numbers",
        "title": "Rounding Whole Numbers",
        "concreteComparison": (
            "A concert sells $4\\,683$ tickets. The newspaper prints "
            "\"about $4\\,700$ people attended\" — and everyone is happy. "
            "Rounding trades a little exactness for a lot of convenience: "
            "you jump to the NEAREST landmark number, like snapping to "
            "the closest bus stop on a route."),
        "objective": (
            "Round whole numbers to any place — tens through hundred-"
            "thousands — using the nearest-landmark idea and the digit "
            "rule, including the halfway case."),
        "concept": [
            "To round to a place, look at the two **landmarks** — the "
            "multiples of that place on either side — and jump to the "
            "NEARER one. $4\\,683$ sits between $4\\,600$ and $4\\,700$; "
            "it is $83$ past the lower and only $17$ short of the upper, "
            "so it rounds to $4\\,700$.",
            "The **digit rule** does the same thing without measuring: "
            "look at the digit one place RIGHT of the rounding place. "
            "$0$–$4$: round down (keep the digit). $5$–$9$: round up "
            "(digit grows by one). Everything right of the rounding "
            "place becomes zeros.",
            "**Exactly halfway** — like $450$ to the nearest hundred — "
            "is a tie between landmarks. The rule everyone agrees on: "
            "halfway rounds UP, so $450 \\to 500$.",
        ],
        "keyIdea": (
            "Round = jump to the nearest landmark multiple. The digit one "
            "place right tells you which way: 0–4 down, 5–9 up."),
        "facts": [
            {"title": "The digit rule",
             "latex": "0,1,2,3,4 \\to \\text{down} \\qquad 5,6,7,8,9 \\to \\text{up}",
             "explanation": "Check the digit one place right of where you're rounding."},
            {"title": "Halfway rounds up",
             "latex": "450 \\to 500 \\ (\\text{nearest hundred})",
             "explanation": "A tie between landmarks breaks upward, by convention."},
        ],
        "workedExamples": [
            {"id": "g5pv-l4-we1",
             "statement": "Round $4\\,683$ to the nearest hundred, and to the nearest thousand.",
             "note": "Find the landmarks, or use the digit rule.",
             "solution": ("Nearest hundred: landmarks $4\\,600$ and $4\\,700$; the tens "
                          "digit is $8 \\ge 5$, so up — $4\\,700$. Nearest thousand: "
                          "landmarks $4\\,000$ and $5\\,000$; the hundreds digit is $6 "
                          "\\ge 5$, so up — $5\\,000$."),
             "badges": [{"text": "core"}],
             "check": [near(4683, 4700, 4600), near(4683, 5000, 4000)]},
            {"id": "g5pv-l4-we2",
             "statement": "Round $349\\,502$ to the nearest ten-thousand.",
             "note": "Careful — the digit rule looks at the thousands digit.",
             "solution": ("Landmarks: $340\\,000$ and $350\\,000$. The thousands digit "
                          "is $9 \\ge 5$: round up to $350\\,000$. (Check by distance: "
                          "$349\\,502$ is only $498$ short of $350\\,000$ but $9\\,502$ "
                          "past $340\\,000$.)"),
             "badges": [{"text": "core"}],
             "check": [near(349502, 350000, 340000), "Eq(350000 - 349502, 498)"]},
        ],
        "commonMistakes": [
            {"text": "Looking at the wrong digit — rounding 4,683 to the nearest hundred by checking the ones digit.",
             "correction": "The decider is ONE place right of the rounding place. For hundreds, check the tens digit (8), not the ones.",
             "authored": True},
            {"text": "Rounding in two hops: 4,449 → 4,450 → 4,500.",
             "correction": "Round ONCE from the original number. 4,449 is nearer 4,400 than 4,500 (49 < 51) — chained roundings drift.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5pv-l4-t1",
             "statement": "Round $76\\,281$ to the nearest thousand.",
             "solution": "Landmarks $76\\,000$ and $77\\,000$; the hundreds digit is $2 < 5$: down to $76\\,000$.",
             "check": [near(76281, 76000, 77000)]},
            {"id": "g5pv-l4-t2",
             "statement": "Round $450$ to the nearest hundred.",
             "solution": "Exactly halfway between $400$ and $500$ — ties round UP: $500$.",
             "check": ["Eq(Abs(450 - 500), 50)", "Eq(Abs(450 - 400), 50)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Jump to the nearest landmark", [
                "Rounding to a place means jumping to the NEAREST multiple of that place — the two multiples either side are your landmarks.",
                "$4\\,683$, nearest hundred: landmarks $4\\,600$ and $4\\,700$. It sits $83$ past one and $17$ short of the other — jump to $4\\,700$.",
                "Rounding trades a little exactness for a lot of convenience: \"about $4\\,700$ tickets\" is the useful truth.",
            ]),
            workedset("Landmarks either side",
                      "Find the two multiples, measure which is nearer.", [
                wex("Round $4\\,683$ to the nearest hundred.",
                    ["Landmarks: $4\\,600$ and $4\\,700$.",
                     "Distances: $83$ back, $17$ forward — jump forward to $4\\,700$."],
                    "$4\\,700$", [near(4683, 4700, 4600), "Eq(4700 - 4683, 17)"]),
                wex("Round $4\\,683$ to the nearest thousand.",
                    ["Landmarks: $4\\,000$ and $5\\,000$.",
                     "$683$ past the lower, $317$ short of the upper — jump to $5\\,000$."],
                    "$5\\,000$", [near(4683, 5000, 4000), "Eq(5000 - 4683, 317)"]),
            ]),
            tryitset("Which landmark?", "Name both landmarks, then jump to the nearer one.", [
                tp("$76\\,281$ to the nearest thousand is:",
                   ["$76\\,000$", "$77\\,000$", "$76\\,300$"],
                   "Landmarks $76\\,000$ and $77\\,000$: it is $281$ past the lower — much nearer. Down.",
                   [near(76281, 76000, 77000)]),
                tp("$8\\,517$ to the nearest ten is:",
                   ["$8\\,520$", "$8\\,510$", "$8\\,500$"],
                   "Landmarks $8\\,510$ and $8\\,520$; the ones digit $7 \\ge 5$ sends it up.",
                   [near(8517, 8520, 8510)]),
                tp("$132\\,900$ to the nearest ten-thousand is:",
                   ["$130\\,000$", "$140\\,000$", "$133\\,000$"],
                   "Landmarks $130\\,000$ and $140\\,000$: $2\\,900$ past the lower, $7\\,100$ short of the upper. Down.",
                   [near(132900, 130000, 140000)]),
            ]),
            tapq("Measure the jump", "$4\\,683$ rounds to $4\\,700$, not $4\\,600$, because:",
                 ["$17 < 83$ — it is nearer to $4\\,700$",
                  "bigger numbers are better",
                  "the ones digit is $3$",
                  "hundreds always round up"],
                 "Rounding is a nearness contest: $4\\,700$ is $17$ away, $4\\,600$ is $83$ away. Nearer wins.",
                 ["Eq(4700 - 4683, 17)", "Eq(4683 - 4600, 83)", "17 < 83"]),
            funfact("Attendance figures are almost always rounded",
                    "When a stadium announces 20,000 spectators, the turnstiles counted something like 19,738. News, populations, and prices round constantly — one of the most-used pieces of math in daily life is exactly this lesson."),
            teach("Concept B", "The digit rule (and the halfway tie)", [
                "You don't need to measure distances — the digit ONE place right of the rounding place tells the direction: $0$–$4$ round down, $5$–$9$ round up.",
                "After the jump, every digit right of the rounding place becomes a zero: $349\\,502$ to the nearest ten-thousand → thousands digit $9$ → up → $350\\,000$.",
                "Exactly halfway ($450$ to the nearest hundred) is a genuine tie — the agreed rule breaks it UPWARD: $450 \\to 500$.",
            ]),
            workedset("Rule in action",
                      "One glance at the decider digit.", [
                wex("Round $349\\,502$ to the nearest ten-thousand.",
                    ["Rounding place: ten-thousands ($4$). Decider: thousands digit $9 \\ge 5$ — up.",
                     "$350\\,000$; check by distance: only $498$ short of it."],
                    "$350\\,000$", [near(349502, 350000, 340000)]),
                wex("Round $450$ to the nearest hundred.",
                    ["Landmarks $400$ and $500$ — both exactly $50$ away: a tie.",
                     "Ties round up: $500$."],
                    "$500$", ["Eq(Abs(450 - 400), 50)", "Eq(Abs(450 - 500), 50)"]),
            ]),
            tryitset("The decider digit", "Find the rounding place, glance one place right.", [
                tp("$62\\,451$ to the nearest hundred is:",
                   ["$62\\,500$", "$62\\,400$", "$62\\,000$"],
                   "Decider is the tens digit $5$ — up: $62\\,500$.",
                   [near(62451, 62500, 62400)]),
                tp("$895\\,214$ to the nearest hundred-thousand is:",
                   ["$900\\,000$", "$800\\,000$", "$890\\,000$"],
                   "Decider is the ten-thousands digit $9$ — up: $900\\,000$.",
                   [near(895214, 900000, 800000)]),
                tp("$4\\,449$ to the nearest hundred is:",
                   ["$4\\,400$", "$4\\,500$", "$4\\,450$"],
                   "Decider is the tens digit $4$ — down. (Two-hop rounding $4\\,449 \\to 4\\,450 \\to 4\\,500$ is the classic trap: round ONCE from the original.)",
                   [near(4449, 4400, 4500)]),
            ]),
            tapq("The halfway case", "$3\\,500$ to the nearest thousand is:",
                 ["$4\\,000$", "$3\\,000$", "$3\\,500$", "either is fine"],
                 "Exactly halfway between $3\\,000$ and $4\\,000$ — and ties round UP by the agreed rule: $4\\,000$.",
                 ["Eq(Abs(3500 - 3000), 500)", "Eq(Abs(3500 - 4000), 500)"]),
            recap([
                "Rounding jumps to the nearest landmark multiple of the rounding place.",
                "Digit rule: the digit one place right decides — 0–4 down, 5–9 up.",
                "After the jump, everything right of the rounding place becomes zeros.",
                "Exactly halfway rounds up; and always round ONCE from the original number.",
            ]),
            tip("Mixed places this time — nearest ten through nearest hundred-thousand. Name the decider digit before you answer."),
            tryitset("Mixed practice", "All places, one rule.", [
                tp("$7\\,777$ to the nearest ten is:",
                   ["$7\\,780$", "$7\\,770$", "$7\\,800$"],
                   "Ones digit $7 \\ge 5$: up to $7\\,780$.",
                   [near(7777, 7780, 7770)]),
                tp("$24\\,315$ to the nearest thousand is:",
                   ["$24\\,000$", "$25\\,000$", "$24\\,300$"],
                   "Hundreds digit $3 < 5$: down to $24\\,000$.",
                   [near(24315, 24000, 25000)]),
                tp("$650\\,000$ to the nearest hundred-thousand is:",
                   ["$700\\,000$", "$600\\,000$", "$650\\,000$"],
                   "Ten-thousands digit is $5$ — exactly halfway, and ties round up: $700\\,000$.",
                   ["Eq(Abs(650000 - 600000), 50000)", "Eq(Abs(650000 - 700000), 50000)"]),
                tp("A city of $187\\,904$ people, \"to the nearest ten-thousand\", is a city of about:",
                   ["$190\\,000$", "$180\\,000$", "$188\\,000$"],
                   "Thousands digit $7 \\ge 5$: up to $190\\,000$.",
                   [near(187904, 190000, 180000)]),
                tp("Which number rounds to $6\\,000$ at the nearest thousand?",
                   ["$5\\,712$", "$6\\,502$", "$5\\,499$"],
                   "$5\\,712$ has hundreds digit $7$ — up to $6\\,000$. ($6\\,502$ goes to $7\\,000$; $5\\,499$ goes to $5\\,000$.)",
                   [near(5712, 6000, 5000), near(6502, 7000, 6000), near(5499, 5000, 6000)]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Rounding\"",
                    "You now hold both pictures: the number-line jump to the nearest landmark, and the one-glance digit rule that computes it. Next: putting rounding to work — estimating answers before you compute them.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Estimation
# ==========================================================================

def lesson_estimation():
    return {
        "slug": "estimating-with-rounded-numbers",
        "title": "Estimating with Rounded Numbers",
        "concreteComparison": (
            "At the market you pick items costing $4\\,683$, $2\\,298$ and "
            "$1\\,050$ tögrög. Before the till rings you already know the "
            "total is \"about $8\\,000$\" — because $4\\,700 + 2\\,300 + "
            "1\\,000$ is easy in your head. Estimation is arithmetic on "
            "the rounded stand-ins: fast, rough on purpose, and good "
            "enough to catch a wrong bill."),
        "objective": (
            "Estimate sums and differences by rounding first, judge "
            "whether an exact answer is reasonable, and know when an "
            "estimate over- or under-shoots."),
        "concept": [
            "**Round, then compute.** Replace each number by a nearby "
            "landmark, then do the easy arithmetic: $4\\,683 + 2\\,298 "
            "\\approx 4\\,700 + 2\\,300 = 7\\,000$. The exact answer "
            "($6\\,981$) sits close by — the estimate cost seconds.",
            "**Estimates are lie detectors.** If a computed answer lands "
            "far from the estimate, the computation is wrong — a dropped "
            "digit or misplaced column. $4\\,683 + 2\\,298 = 26\\,981$? "
            "The estimate says $7\\,000$; someone's place value slipped.",
            "**Know your direction.** Rounding both numbers UP makes the "
            "estimated sum too big; rounding both DOWN makes it too "
            "small. Handy when you must be safe: to be sure money is "
            "enough, round the prices up.",
        ],
        "keyIdea": (
            "Round first, compute second — a seconds-long estimate that "
            "catches wrong answers and guides safe decisions."),
        "facts": [
            {"title": "Round, then compute",
             "latex": "4\\,683 + 2\\,298 \\approx 4\\,700 + 2\\,300 = 7\\,000",
             "explanation": "Arithmetic on the landmarks — fast and close."},
            {"title": "Direction of error",
             "latex": "\\text{both up} \\Rightarrow \\text{estimate too big} \\qquad \\text{both down} \\Rightarrow \\text{too small}",
             "explanation": "Choose the direction that keeps you safe."},
        ],
        "workedExamples": [
            {"id": "g5pv-l5-we1",
             "statement": "Estimate $4\\,683 + 2\\,298$ by rounding to the nearest hundred, then compare with the exact sum.",
             "note": "Round each number first.",
             "solution": ("$4\\,683 \\to 4\\,700$ and $2\\,298 \\to 2\\,300$: estimate "
                          "$7\\,000$. Exact: $6\\,981$ — the estimate missed by only "
                          "$19$, and took a fraction of the effort."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4700 + 2300, 7000)", "Eq(4683 + 2298, 6981)",
                       "Eq(7000 - 6981, 19)"]},
            {"id": "g5pv-l5-we2",
             "statement": "A student computes $8\\,132 - 4\\,905 = 4\\,227$. Use an estimate to judge the answer.",
             "note": "Round to the nearest thousand and subtract.",
             "solution": ("Estimate: $8\\,000 - 5\\,000 = 3\\,000$. The claimed "
                          "$4\\,227$ is more than a thousand off the estimate — "
                          "suspicious. Exact: $8\\,132 - 4\\,905 = 3\\,227$; the "
                          "student borrowed wrongly in the thousands."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8000 - 5000, 3000)", "Eq(8132 - 4905, 3227)",
                       "Ne(4227, 3227)"]},
        ],
        "commonMistakes": [
            {"text": "Computing exactly first and rounding the answer, calling it an estimate.",
             "correction": "That's just rounding, and it costs full effort. Estimation rounds FIRST so the arithmetic itself becomes easy.",
             "authored": True},
            {"text": "Treating the estimate as the answer.",
             "correction": "An estimate brackets the answer; it doesn't replace it. Use it to check the exact result — about 7,000 confirms 6,981, it doesn't overwrite it.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5pv-l5-t1",
             "statement": "Estimate $6\\,214 + 3\\,879$ by rounding to the nearest thousand.",
             "solution": "$6\\,000 + 4\\,000 = 10\\,000$. (Exact: $10\\,093$ — the estimate is $93$ under.)",
             "check": ["Eq(6000 + 4000, 10000)", "Eq(6214 + 3879, 10093)"]},
            {"id": "g5pv-l5-t2",
             "statement": "You have $10\\,000$ tögrög; items cost $4\\,683$ and $4\\,890$. Round UP to decide safely whether you have enough.",
             "solution": "Up: $4\\,700 + 4\\,900 = 9\\,600 \\le 10\\,000$ — safe. (The true total $9\\,573$ is even smaller, as an up-rounded estimate guarantees.)",
             "check": ["Eq(4700 + 4900, 9600)", "Eq(4683 + 4890, 9573)",
                       "9573 < 9600", "9600 < 10000"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Round first, compute second", [
                "An estimate replaces each number with a nearby landmark, THEN computes: $4\\,683 + 2\\,298 \\approx 4\\,700 + 2\\,300 = 7\\,000$.",
                "The exact sum is $6\\,981$ — the estimate landed within $19$, in a fraction of the time.",
                "The order matters: round FIRST so the arithmetic becomes easy. Computing exactly and then rounding is just... the exact computation.",
            ]),
            workedset("Fast sums and differences",
                      "Landmark arithmetic — pick a friendly rounding place.", [
                wex("Estimate $4\\,683 + 2\\,298$ (nearest hundred).",
                    ["$4\\,683 \\to 4\\,700$; $2\\,298 \\to 2\\,300$.",
                     "$4\\,700 + 2\\,300 = 7\\,000$ — the exact $6\\,981$ sits $19$ below."],
                    "about $7\\,000$",
                    ["Eq(4700 + 2300, 7000)", "Eq(4683 + 2298, 6981)"]),
                wex("Estimate $9\\,120 - 5\\,880$ (nearest thousand).",
                    ["$9\\,120 \\to 9\\,000$; $5\\,880 \\to 6\\,000$.",
                     "$9\\,000 - 6\\,000 = 3\\,000$ — exact: $3\\,240$."],
                    "about $3\\,000$",
                    ["Eq(9000 - 6000, 3000)", "Eq(9120 - 5880, 3240)"]),
            ]),
            tryitset("Estimate it", "Round to the stated place, then compute in your head.", [
                tp("$6\\,214 + 3\\,879$, estimated at the nearest thousand, is about:",
                   ["$10\\,000$", "$9\\,000$", "$11\\,000$"],
                   "$6\\,000 + 4\\,000 = 10\\,000$; the exact $10\\,093$ confirms it.",
                   ["Eq(6000 + 4000, 10000)", "Eq(6214 + 3879, 10093)"]),
                tp("$7\\,908 - 2\\,110$, estimated at the nearest thousand, is about:",
                   ["$6\\,000$", "$5\\,000$", "$10\\,000$"],
                   "$8\\,000 - 2\\,000 = 6\\,000$; exact $5\\,798$ — close by.",
                   ["Eq(8000 - 2000, 6000)", "Eq(7908 - 2110, 5798)"]),
                tp("$21\\,870 + 48\\,240$, estimated at the nearest ten-thousand, is about:",
                   ["$70\\,000$", "$60\\,000$", "$80\\,000$"],
                   "$20\\,000 + 50\\,000 = 70\\,000$; exact $70\\,110$.",
                   ["Eq(20000 + 50000, 70000)", "Eq(21870 + 48240, 70110)"]),
            ]),
            tapq("Estimate as lie detector",
                 "A student claims $4\\,683 + 2\\,298 = 26\\,981$. The estimate $4\\,700 + 2\\,300 = 7\\,000$ says:",
                 ["the claim is wrong — it is nowhere near the estimate",
                  "the claim is right — estimates always undershoot",
                  "nothing — estimates cannot judge exact answers",
                  "the estimate must be redone"],
                 "An exact answer should land NEAR its estimate. $26\\,981$ against $7\\,000$ means a place-value slip — the true sum is $6\\,981$.",
                 ["Eq(4683 + 2298, 6981)", "Eq(4700 + 2300, 7000)", "26981 > 3*7000"]),
            funfact("Engineers estimate before every calculation",
                    "A bridge engineer computes a beam's load exactly — but FIRST estimates it roughly. If the precise computer answer disagrees wildly with the rough one, they hunt the error before trusting anything. The habit you're learning here is professional practice."),
            teach("Concept B", "Direction — when estimates over- and under-shoot", [
                "Round both numbers UP and the estimated sum is guaranteed TOO BIG; round both DOWN and it is too small. The direction of the error is knowable.",
                "That's a tool: to be SURE your money covers the bill, round the prices UP — if the safe estimate fits, the true total fits better.",
                "Mixed roundings (one up, one down) tend to cancel — which is why nearest-landmark estimates usually land so close.",
            ]),
            workedset("Safe estimates",
                      "Choose the rounding direction to match the decision.", [
                wex("You have $10\\,000$; items cost $4\\,683$ and $4\\,890$. Enough?",
                    ["Round UP for safety: $4\\,700 + 4\\,900 = 9\\,600$.",
                     "$9\\,600 \\le 10\\,000$, and the true total $9\\,573$ is smaller still — safely enough."],
                    "yes — safely",
                    ["Eq(4700 + 4900, 9600)", "Eq(4683 + 4890, 9573)", "9573 < 9600"]),
                wex("A hall seats $1\\,500$. Bookings: $612$, $487$, $305$. Could the hall overflow?",
                    ["Round UP: $700 + 500 + 400 = 1\\,600 > 1\\,500$ — the safe estimate cannot promise a fit.",
                     "Check exactly: $612 + 487 + 305 = 1\\,404 \\le 1\\,500$ — it fits, but only the exact sum could say so."],
                    "the exact sum was needed: $1\\,404$ fits",
                    ["Eq(700 + 500 + 400, 1600)", "Eq(612 + 487 + 305, 1404)",
                     "1404 < 1500", "1600 > 1500"]),
            ]),
            tryitset("Which direction?", "Match the rounding direction to the decision.", [
                tp("To be CERTAIN your money covers the shopping, round every price:",
                   ["up", "down", "to the nearest landmark"],
                   "Rounding up overstates the total — if even the overstated total fits your money, the real one surely does.",
                   ["Eq(4700 + 4900, 9600)"]),
                tp("Both addends rounded DOWN. The estimated sum is:",
                   ["smaller than the true sum", "bigger than the true sum", "exactly the true sum"],
                   "Each stand-in is below its number, so the estimate under-shoots: $4\\,600 + 2\\,200 = 6\\,800 < 6\\,981$.",
                   ["Eq(4600 + 2200, 6800)", "6800 < 6981"]),
                tp("$3\\,190 + 4\\,870$: the nearest-hundred estimate is:",
                   ["$8\\,100$", "$8\\,000$", "$7\\,100$"],
                   "$3\\,190 \\to 3\\,200$ and $4\\,870 \\to 4\\,900$: the estimate is $3\\,200 + 4\\,900 = 8\\,100$ — and the exact sum $8\\,060$ sits just below it.",
                   ["Eq(3200 + 4900, 8100)", "Eq(3190 + 4870, 8060)"]),
            ]),
            tapq("Cancel or compound?", "One number rounds up by $40$, the other down by $30$. The estimated sum is off by:",
                 ["$10$", "$70$", "$40$", "$30$"],
                 "Opposite directions mostly cancel: $+40 - 30 = +10$. Mixed roundings are why nearest-landmark estimates land so close.",
                 ["Eq(40 - 30, 10)"]),
            recap([
                "Estimate = round FIRST, then compute on the landmarks.",
                "Exact answers should land near their estimate — a big gap means a computation error.",
                "Both up ⇒ estimate too big; both down ⇒ too small; mixed ⇒ mostly cancels.",
                "Round up on purpose when you need a safe over-estimate (money, capacity).",
            ]),
            tip("Estimate each one BEFORE any exact work — the goal is a confident \"about\" in under five seconds."),
            tryitset("Mixed practice", "Round, compute, judge.", [
                tp("$5\\,812 + 3\\,190$, nearest thousand, is about:",
                   ["$9\\,000$", "$8\\,000$", "$10\\,000$"],
                   "$6\\,000 + 3\\,000 = 9\\,000$; exact $9\\,002$ — a near-perfect estimate.",
                   ["Eq(6000 + 3000, 9000)", "Eq(5812 + 3190, 9002)"]),
                tp("$9\\,050 - 3\\,970$, nearest thousand, is about:",
                   ["$5\\,000$", "$6\\,000$", "$4\\,000$"],
                   "$9\\,000 - 4\\,000 = 5\\,000$; exact $5\\,080$.",
                   ["Eq(9000 - 4000, 5000)", "Eq(9050 - 3970, 5080)"]),
                tp("A claimed answer of $1\\,264$ for $612 + 487$ is:",
                   ["wrong — the estimate says about $1\\,100$",
                    "right — it matches the estimate",
                    "impossible to judge"],
                   "$600 + 500 = 1\\,100$; the exact sum is $1\\,099$. A claim of $1\\,264$ sits far outside — an addition slip.",
                   ["Eq(600 + 500, 1100)", "Eq(612 + 487, 1099)", "Ne(1264, 1099)"]),
                tp("To guarantee a bus fits every group, round each group's size:",
                   ["up", "down", "to the nearest ten"],
                   "Overstate to be safe: if the overstated total fits the seats, the true total does too.",
                   ["Eq(40 + 30, 70)"]),
                tp("$38\\,760 + 21\\,320$, nearest ten-thousand, is about:",
                   ["$60\\,000$", "$50\\,000$", "$70\\,000$"],
                   "$40\\,000 + 20\\,000 = 60\\,000$; exact $60\\,080$.",
                   ["Eq(40000 + 20000, 60000)", "Eq(38760 + 21320, 60080)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Estimating\" — and the whole topic",
                    "Reading, place value, comparing, rounding, estimating: you now own whole numbers up to the millions. Everything the rest of Grade 5 does — the four operations, fractions, decimals — stands on exactly these five lessons.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5pv-pr1", "Write the numeral for *six hundred four thousand, ninety*.",
             "Thousands group $604$, ones group $090$: $604\\,090$.",
             ["Eq(604*1000 + 90, 604090)"]),
        prob("g5pv-pr2", "Write $3\\,057\\,208$ in words.",
             "$3$ | $057$ | $208$: three million, fifty-seven thousand, two hundred eight.",
             ["Eq(3*1000000 + 57*1000 + 208, 3057208)"]),
        prob("g5pv-pr3", "Write $470\\,206$ in expanded form.",
             "$400\\,000 + 70\\,000 + 200 + 6$ — the thousands and tens places are zeros.",
             ["Eq(400000 + 70000 + 200 + 6, 470206)"]),
        prob("g5pv-pr4", "State the value of each $8$ in $8\\,284$.",
             "Left $8$: thousands, worth $8\\,000$. Right $8$: tens, worth $80$. The left one is $100$ times the right.",
             ["Eq(8*1000, 8000)", "Eq(8*10, 80)", "Eq(8000/80, 100)"]),
        prob("g5pv-pr5", "Place the correct symbol: $460\\,890 \\;\\square\\; 460\\,980$.",
             "Scan from the left: $4, 6, 0$ agree; hundreds $8 < 9$. So $460\\,890 < 460\\,980$.",
             ["460890 < 460980"]),
        prob("g5pv-pr6", "Order from smallest to largest: $78\\,102$, $9\\,998$, $78\\,021$, $100\\,003$.",
             "$9\\,998$ (4 digits) first, $100\\,003$ (6 digits) last; between them $78\\,021 < 78\\,102$ (tens of the hundreds: $0 < 1$). Order: $9\\,998 < 78\\,021 < 78\\,102 < 100\\,003$.",
             ["9998 < 78021", "78021 < 78102", "78102 < 100003"]),
        prob("g5pv-pr7", "Round $381\\,449$ to the nearest thousand and to the nearest hundred-thousand.",
             "Nearest thousand: hundreds digit $4$ — down to $381\\,000$. Nearest hundred-thousand: ten-thousands digit $8$ — up to $400\\,000$.",
             [near(381449, 381000, 382000), near(381449, 400000, 300000)]),
        prob("g5pv-pr8", "Estimate $27\\,880 + 41\\,210$ at the nearest ten-thousand, then compute exactly and compare.",
             "Estimate: $30\\,000 + 40\\,000 = 70\\,000$. Exact: $69\\,090$. The estimate overshoots by $910$ — close enough to confirm the exact sum.",
             ["Eq(30000 + 40000, 70000)", "Eq(27880 + 41210, 69090)",
              "Eq(70000 - 69090, 910)"]),
    ]


def test_bank():
    return [
        prob("g5pv-x1", "Write the numeral for *five million, sixty thousand, eleven*.",
             "$5$ | $060$ | $011$ = $5\\,060\\,011$.",
             ["Eq(5*1000000 + 60*1000 + 11, 5060011)"]),
        prob("g5pv-x2", "What number is $600\\,000 + 9\\,000 + 300 + 2$?",
             "$609\\,302$ — zeros hold the ten-thousands and tens.",
             ["Eq(600000 + 9000 + 300 + 2, 609302)"]),
        prob("g5pv-x3", "The digit $6$ in $2\\,631\\,000$ is how many times the digit $6$ in $2\\,163$?",
             "In $2\\,631\\,000$ the $6$ stands in the hundred-thousands place: worth $600\\,000$. In $2\\,163$ it stands in the tens place: worth $60$. So it is $600\\,000 \\div 60 = 10\\,000$ times as much — four places apart, four factors of ten.",
             ["Eq(6*100000, 600000)", "Eq(6*10, 60)", "Eq(600000/60, 10000)"]),
        prob("g5pv-x4", "Which is larger, $505\\,050$ or $505\\,500$? Name the deciding place.",
             "Scan: $5, 0, 5$ agree; the hundreds differ ($0 < 5$) — $505\\,500$ is larger, decided at the hundreds place.",
             ["505050 < 505500"]),
        prob("g5pv-x5", "Round $749\\,500$ to the nearest thousand.",
             "The hundreds digit is $5$ — exactly halfway between $749\\,000$ and $750\\,000$, and ties round up: $750\\,000$.",
             ["Eq(Abs(749500 - 749000), 500)", "Eq(Abs(749500 - 750000), 500)"]),
        prob("g5pv-x6", "A shop sold $18\\,940$ and then $23\\,180$ tögrög of goods. Estimate the total at the nearest thousand, and judge the clerk's claimed total of $42\\,120$.",
             "Estimate: $19\\,000 + 23\\,000 = 42\\,000$; exact: $42\\,120$ — the claim sits right beside the estimate, so it is credible (and in fact exact).",
             ["Eq(19000 + 23000, 42000)", "Eq(18940 + 23180, 42120)"]),
    ]


def main():
    topic = {
        "slug": "whole-numbers-and-place-value",
        "title": "Whole Numbers & Place Value",
        "grade": 5,
        "status": "published",
        "blurb": ("Reading and writing numbers to the millions, what each digit "
                  "is worth, comparing and ordering, rounding, and estimation — "
                  "the foundation of all Grade 5 arithmetic."),
        "lessons": [
            lesson_reading(),
            lesson_digit_value(),
            lesson_comparing(),
            lesson_rounding(),
            lesson_estimation(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    _assert_checks(topic)
    path = os.path.join(OUT, "whole-numbers-and-place-value.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(topic, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    n_steps = sum(len(l["interactive"]["steps"]) for l in topic["lessons"])
    print("wrote %s — %d lessons, %d steps, %d practice, %d test, %d sympy checks"
          % (os.path.relpath(path, ROOT), len(topic["lessons"]), n_steps,
             len(topic["practice"]), len(topic["testYourself"]), checks_run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
