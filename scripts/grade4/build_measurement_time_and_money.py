#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Measurement, Time & Money.

Centimetres and metres (the 100-trade, ruler reading, sensible units,
comparing after converting), grams and kilograms and litres and
millilitres (the 1000-trades), reading the clock to the quarter hour
(o'clock, half past, quarter past, quarter to — all as minutes of the
60-minute hour), the calendar and durations inside one day (start +
length = end, always in minutes), and togrog money (note totals,
making amounts different ways, and change by counting up).

Through-line: KNOW THE TRADE. Every measure in this topic swaps one
big unit for a FIXED count of small ones — 1 metre for 100 cm, 1 kg
for 1000 g, 1 litre for 1000 ml, 1 hour for 60 minutes, 1 week for
7 days, one 1000 note for two 500 notes. Know the trade first; only
then count.

Grade discipline: no km, no decimals, no negative numbers, no elapsed
time across days, values inside 10 000, times-table facts at most 10
(unit trades ×100, ×1000, ×60 are the taught scalings). Time checks
run in minutes — never decimal hours. Togrog stays in prose, never
inside math. Figures are built from the SAME variables as the
statements they illustrate, so text and picture cannot disagree.

Run: python3 scripts/grade4/build_measurement_time_and_money.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic, withfig,
                     fig_groups, fig_numline, fig_geo, P, seg, ang,
                     C_ACCENT, C_WARM, C_GREEN, C_NEUTRAL)


def mny(n):
    """Togrog amount with the thin thousands separator used topic-wide."""
    return "{:,}".format(n).replace(",", "\\,")


# ==========================================================================
# Lesson 1 — Length: cm and m
# ==========================================================================

def lesson_length():
    # ruler 1: pencil measured from the 0 mark
    p_len, r_hi = 7, 10
    fig_ruler_pencil = fig_numline(
        [(0, "0"), (p_len, "%d cm" % p_len, C_WARM), (r_hi, "%d" % r_hi)],
        lo=0, hi=r_hi)
    # ruler 2: stick that does NOT start at 0 — subtract the marks
    s_a, s_b = 2, 9
    s_len = s_b - s_a
    fig_ruler_stick = fig_numline(
        [(0, "0"), (s_a, "%d" % s_a, C_WARM), (s_b, "%d" % s_b, C_GREEN),
         (10, "10")], lo=0, hi=10)
    # ruler 3: crayon from 4 to 12 on a 15 cm ruler
    c_a, c_b = 4, 12
    c_len = c_b - c_a
    fig_ruler_crayon = fig_numline(
        [(0, "0"), (c_a, "%d" % c_a, C_WARM), (c_b, "%d" % c_b, C_GREEN),
         (15, "15")], lo=0, hi=15)
    # ruler 4 (chapter practice): stick from 1 to 10
    d_a, d_b = 1, 10
    d_len = d_b - d_a
    fig_ruler_chalk = fig_numline(
        [(0, "0"), (d_a, "%d" % d_a, C_WARM), (d_b, "%d" % d_b, C_GREEN)],
        lo=0, hi=10)
    # the metre line
    fig_metre = fig_numline(
        [(0, "0 cm"), (50, "50 cm"), (100, "100 cm = 1 m", C_ACCENT)],
        lo=0, hi=100)
    return {
        "slug": "length",
        "title": "Length: cm and m",
        "concreteComparison": (
            "Put one finger on a single centimetre mark of your school "
            "ruler and step it along the wall of a ger — you would have "
            "to step it a hundred times to cross one metre stick's "
            "worth of felt. That is the whole deal between the "
            "two length units: one metre TRADES for exactly $100$ "
            "centimetres, the way one big note trades for a fixed "
            "stack of small ones. Know the trade, then count."),
        "objective": (
            "Measure lengths with a ruler (even when the object does "
            "not start at the $0$ mark), choose the sensible unit — "
            "centimetres for small things, metres for big ones — and "
            "convert between metres and centimetres both ways."),
        "concept": [
            "**One metre trades for 100 centimetres.** The centimetre "
            "is the small unit (about a fingernail's width); the metre "
            "is the big one (a giant step). The trade is fixed: "
            "$1$ m $= 100$ cm, so $3$ m $= 3 \\times 100 = 300$ cm.",
            "**A ruler measures from mark to mark.** If the object "
            "starts at $0$, read its end. If it starts elsewhere, "
            "subtract the start mark from the end mark: from the $2$ "
            "to the $9$ is $7$ cm, because $7 + 2 = 9$.",
            "**Compare in ONE unit.** Is $2$ m longer than $180$ cm? "
            "Bare numbers lie ($180 > 2$). Trade first: $2$ m $= 200$ "
            "cm, and $200 > 180$ — the metres win. Same unit, then "
            "compare.",
        ],
        "keyIdea": (
            "One metre trades for exactly 100 centimetres. Measure "
            "from mark to mark, pick cm for small things and m for "
            "big ones, and never compare lengths until both wear the "
            "same unit."),
        "facts": [
            {"title": "The length trade",
             "latex": "1\\,\\text{m} = 100\\,\\text{cm}",
             "explanation": "The fixed trade: every metre is worth one hundred centimetres."},
            {"title": "Mark to mark",
             "latex": "9 - 2 = 7 \\quad (7 + 2 = 9)",
             "explanation": "An object lying from the 2 cm mark to the 9 cm mark is 7 cm long — subtract the marks, and add back to check."},
        ],
        "workedExamples": [
            {"id": "g4me-l1-we1",
             "statement": "A table is $2$ m long and a bench is $180$ cm long. Which is longer?",
             "note": "Trade into one unit before comparing.",
             "solution": ("Trade the metres: $2$ m $= 2 \\times 100 = 200$ cm. "
                          "Now both wear centimetres: $200 > 180$, so the table "
                          "is longer — by $20$ cm, since $180 + 20 = 200$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*100, 200)", "200 > 180", "Eq(180 + 20, 200)"]},
            {"id": "g4me-l1-we2",
             "statement": "A stick lies along a ruler from the $%d$ cm mark to the $%d$ cm mark. How long is the stick?" % (s_a, s_b),
             "note": "Not starting at 0 — subtract the marks.",
             "solution": ("Mark to mark: $%d - %d = %d$ cm. Add back to check: "
                          "$%d + %d = %d$ ✓. The stick is $%d$ cm long." %
                          (s_b, s_a, s_len, s_len, s_a, s_b, s_len)),
             "badges": [{"text": "core"}],
             "check": ["Eq(%d + %d, %d)" % (s_len, s_a, s_b), "%d < %d" % (s_len, s_b)]},
        ],
        "commonMistakes": [
            {"text": "Trading a metre for 10 centimetres — writing 3 m = 30 cm.",
             "correction": "The trade is 100 per metre, not 10: 3 m = 300 cm. Say the trade out loud before multiplying.",
             "authored": True},
            {"text": "Comparing 2 m with 180 cm by the bare numbers and deciding 180 wins.",
             "correction": "Numbers in different units cannot be compared. Trade first: 2 m = 200 cm, and 200 > 180.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4me-l1-t1",
             "statement": "Convert $6$ m to centimetres, and $900$ cm to metres.",
             "solution": "Big to small multiplies the trade: $6 \\times 100 = 600$ cm. Small to big divides it: $900 \\div 100 = 9$ m.",
             "check": ["Eq(6*100, 600)", "Eq(Rational(900,100), 9)"]},
            {"id": "g4me-l1-t2",
             "statement": "A ger door is about $2$ m tall. Could it be $2$ cm instead? Explain with the trade.",
             "solution": "No — $2$ m $= 200$ cm, taller than you. $2$ cm is about the width of two fingernails: $200 > 2$, a door of $2$ cm would not let a cat through.",
             "check": ["Eq(2*100, 200)", "200 > 2"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The 100-trade, and the ruler", [
                "Two length units, one fixed trade: $1$ metre $= 100$ centimetres. A centimetre is a fingernail's width; a metre is a giant step — and every metre is worth exactly $100$ of the small ones.",
                "The ruler below shows a pencil measured from the $0$ mark: its tip reaches $%d$, so it is $%d$ cm long. Starting at $0$ lets the end mark do all the work." % (p_len, p_len),
                "The through-line of this whole topic: KNOW THE TRADE. Every unit here swaps for a fixed count of smaller ones — length starts us off with $100$ cm per metre.",
            ]), fig_ruler_pencil),
            workedset("Trading and measuring",
                      "Multiply the trade going big-to-small; subtract marks on the ruler.", [
                wex("Convert $3$ m to centimetres.",
                    ["The trade: each metre is worth $100$ cm.",
                     "$3 \\times 100 = 300$ cm."],
                    "$300$ cm",
                    ["Eq(3*100, 300)"]),
                withfig(wex("A stick lies from the $%d$ cm mark to the $%d$ cm mark. Its length?" % (s_a, s_b),
                    ["The stick does not start at $0$ — subtract the marks: $%d - %d = %d$ cm." % (s_b, s_a, s_len),
                     "Add back to check: $%d + %d = %d$ ✓." % (s_len, s_a, s_b)],
                    "$%d$ cm" % s_len,
                    ["Eq(%d + %d, %d)" % (s_len, s_a, s_b)]), fig_ruler_stick),
            ]),
            tryitset("Trade and read", "Say the trade first; subtract marks second.", [
                tp("$5$ m in centimetres is:",
                   ["$500$ cm", "$50$ cm", "$105$ cm"],
                   "The trade is $100$ per metre: $5 \\times 100 = 500$ cm. Writing $50$ trades only $10$ per metre, and $105$ adds instead of trading.",
                   ["Eq(5*100, 500)"]),
                withfig(tp("A crayon lies from the $%d$ cm mark to the $%d$ cm mark. It is:" % (c_a, c_b),
                   ["$%d$ cm long" % c_len, "$%d$ cm long" % c_b, "$%d$ cm long" % (c_b + c_a)],
                   "Subtract the marks: $%d - %d = %d$ cm, and $%d + %d = %d$ ✓. Reading $%d$ forgets the crayon started at $%d$; adding the marks measures nothing at all." %
                   (c_b, c_a, c_len, c_len, c_a, c_b, c_b, c_a),
                   ["Eq(%d + %d, %d)" % (c_len, c_a, c_b)]), fig_ruler_crayon),
                tp("$700$ cm in metres is:",
                   ["$7$ m", "$70$ m", "$600$ m"],
                   "Small to big divides the trade: $700 \\div 100 = 7$ m, and $7 \\times 100 = 700$ ✓. $70$ divides by $10$ instead of $100$.",
                   ["Eq(Rational(700,100), 7)", "Eq(7*100, 700)"]),
            ]),
            tapq("The trade", "How many centimetres are in $4$ metres?",
                 ["$400$", "$40$", "$4$", "$1\\,000$"],
                 "Each metre trades for $100$ cm: $4 \\times 100 = 400$. The wrong answers trade at $10$, at $1$, and at $250$ — but the length trade never changes: $100$ per metre.",
                 ["Eq(4*100, 400)"]),
            funfact("Your body carries rulers",
                    "Stretch both arms out wide: for most people, fingertip to fingertip is about the same as their own height — your body is a rough measuring tape you always carry. Rough is the key word: real rulers win because they trade in exact centimetres, $100$ to every metre, the same for everybody."),
            withfig(teach("Concept B", "Sensible units, honest comparisons", [
                "Pick the unit that fits the job: CENTIMETRES for small things (a pencil, a book, your hand), METRES for big ones (a ger, a classroom, a rope for the horses). The line below is the whole metre laid out in centimetres — $100$ small steps.",
                "To compare lengths in DIFFERENT units, trade first: $3$ m of rope against $280$ cm of rope is really $300$ cm against $280$ cm — the metres win by $20$.",
                "Never compare bare numbers across units. $180 > 2$ says nothing about $180$ cm and $2$ m; only after the trade ($200$ cm) does the comparison become honest.",
            ]), fig_metre),
            workedset("Same unit, then compare",
                      "Trade everything into centimetres; then the bigger number wins.", [
                wex("Which is longer: $3$ m of rope, or $280$ cm of rope?",
                    ["Trade: $3$ m $= 3 \\times 100 = 300$ cm.",
                     "$300 > 280$ — the $3$ m rope is longer by $20$ cm, since $280 + 20 = 300$ ✓."],
                    "the $3$ m rope",
                    ["Eq(3*100, 300)", "300 > 280", "Eq(280 + 20, 300)"]),
                wex("A classroom is $8$ m long. How many centimetres is that, and why do we say $8$ m rather than $800$ cm?",
                    ["Trade: $8 \\times 100 = 800$ cm.",
                     "Both are true — but $8$ is a friendlier count than $800$, so for big things the big unit is the sensible choice."],
                    "$800$ cm",
                    ["Eq(8*100, 800)"]),
            ]),
            tryitset("Pick the unit, win the comparison", "Small things take cm; big things take m; comparisons take ONE unit.", [
                tp("The sensible unit for a toothbrush's length is:",
                   ["centimetres", "metres", "kilograms"],
                   "A toothbrush is about $15$ cm — much less than a whole metre, since $15 < 100$. Metres would make it a strange fraction, and kilograms measure mass, not length.",
                   ["15 < 100"]),
                tp("Which is shorter: $190$ cm or $2$ m?",
                   ["$190$ cm", "$2$ m", "they are equal"],
                   "Trade: $2$ m $= 200$ cm. Then $190 < 200$, so the $190$ cm length is shorter. Comparing $190$ against the bare $2$ is the trap.",
                   ["Eq(2*100, 200)", "190 < 200"]),
                tp("A rope measures $400$ cm. In metres that is:",
                   ["$4$ m", "$40$ m", "$300$ m"],
                   "Divide by the trade: $400 \\div 100 = 4$ m, and $4 \\times 100 = 400$ ✓. $40$ m would be a rope as long as five classrooms.",
                   ["Eq(Rational(400,100), 4)", "Eq(4*100, 400)"]),
            ]),
            tapq("Does the carpet fit?", "Baatar's ger is $5$ m across. A carpet is $480$ cm wide. Does the carpet fit?",
                 ["yes — $480$ cm is less than $500$ cm",
                  "no — $480$ is bigger than $5$",
                  "they are exactly equal",
                  "it cannot be decided"],
                 "Trade the ger's width: $5$ m $= 500$ cm. Then $480 < 500$ — the carpet fits with $20$ cm to spare ($480 + 20 = 500$ ✓). Comparing $480$ with the bare $5$ is the different-units trap.",
                 ["Eq(5*100, 500)", "480 < 500", "Eq(480 + 20, 500)"]),
            recap([
                "One metre trades for exactly 100 centimetres — the fixed trade.",
                "Big to small multiplies by 100; small to big divides by 100.",
                "On a ruler, measure from mark to mark: subtract the start from the end.",
                "Centimetres for small things, metres for big ones.",
                "Compare lengths only after trading them into ONE unit.",
            ]),
            tip("For every item below, say the trade out loud first — one metre, one hundred centimetres — and check whether your two lengths wear the same unit before you compare."),
            tryitset("Mixed practice", "Trades both ways, ruler reads, and honest comparisons.", [
                tp("$9$ m in centimetres is:",
                   ["$900$ cm", "$90$ cm", "$909$ cm"],
                   "$9 \\times 100 = 900$ cm. Trading at $10$ gives the too-small $90$.",
                   ["Eq(9*100, 900)"]),
                withfig(tp("A piece of chalk lies from the $%d$ cm mark to the $%d$ cm mark. Its length is:" % (d_a, d_b),
                   ["$%d$ cm" % d_len, "$%d$ cm" % d_b, "$%d$ cm" % (d_b + d_a)],
                   "Subtract the marks: $%d - %d = %d$ cm, and $%d + %d = %d$ ✓. Reading the end mark alone ignores where the chalk starts." %
                   (d_b, d_a, d_len, d_len, d_a, d_b),
                   ["Eq(%d + %d, %d)" % (d_len, d_a, d_b)]), fig_ruler_chalk),
                tp("$1\\,000$ cm in metres is:",
                   ["$10$ m", "$100$ m", "$1$ m"],
                   "$1\\,000 \\div 100 = 10$ m, and $10 \\times 100 = 1\\,000$ ✓.",
                   ["Eq(Rational(1000,100), 10)", "Eq(10*100, 1000)"]),
                tp("Which is longer: $6$ m or $590$ cm?",
                   ["$6$ m", "$590$ cm", "they are equal"],
                   "Trade: $6$ m $= 600$ cm, and $590 < 600$ — the metres win by $10$ cm ($590 + 10 = 600$ ✓).",
                   ["Eq(6*100, 600)", "590 < 600", "Eq(590 + 10, 600)"]),
                tp("A door's height is about:",
                   ["$2$ m", "$2$ cm", "$200$ m"],
                   "A door is a big thing — metres fit. $2$ m $= 200$ cm, taller than you; $2$ cm would not let a mouse through, and $200$ m is taller than any building in the town — about a hundred doors stacked up.",
                   ["Eq(2*100, 200)", "200 > 2"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Length: cm and m\"",
                    "One fixed trade — $100$ centimetres to the metre — plus mark-to-mark measuring and one-unit comparisons. Next: the same game with heavier stakes, where kilograms and litres each trade for a THOUSAND small units.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Mass & Capacity
# ==========================================================================

def lesson_mass_capacity():
    melon = 800
    fig_scale = fig_numline(
        [(0, "0"), (melon, "melon %d g" % melon, C_WARM),
         (1000, "1 kg = 1000 g", C_GREEN)], lo=0, hi=1000)
    jug = 750
    fig_jug = fig_numline(
        [(0, "0"), (500, "500"), (jug, "%d ml" % jug, C_ACCENT),
         (1000, "1000 ml = 1 l", C_GREEN)], lo=0, hi=1000)
    bags, bag_kg = 3, 2
    fig_flour = fig_groups(*[(bag_kg, "bag %d — %d kg" % (i + 1, bag_kg))
                             for i in range(bags)])
    return {
        "slug": "mass-and-capacity",
        "title": "Mass & Capacity",
        "concreteComparison": (
            "At the market a trader drops a whole kilogram weight on "
            "one pan of the balance scale and pours aaruul onto the "
            "other, piece by piece, until the pans level out. Each "
            "little piece weighs a few grams — and it takes a full "
            "$1\\,000$ grams of them to balance that one kilogram. "
            "Milk plays the same game in a jug: $1\\,000$ millilitres "
            "fill exactly one litre."),
        "objective": (
            "Use the trades $1$ kg $= 1\\,000$ g and $1$ l $= 1\\,000$ "
            "ml, choose the sensible unit for a mass or a capacity, "
            "convert whole numbers both ways, and compare two amounts "
            "after trading them into one unit."),
        "concept": [
            "**One kilogram trades for 1000 grams.** Grams weigh small "
            "things — a letter, an egg, a sweet. Kilograms weigh big "
            "ones — a sack of flour, a young goat, you. The trade is "
            "fixed: $2$ kg $= 2 \\times 1\\,000 = 2\\,000$ g.",
            "**One litre trades for 1000 millilitres.** Millilitres "
            "measure spoonfuls and cups; litres measure jugs, pots and "
            "buckets. Same fixed trade, new letters: $3$ l $= 3\\,000$ "
            "ml.",
            "**Compare in one unit — same rule as length.** Is $2$ kg "
            "more than $1\\,900$ g? Trade first: $2$ kg $= 2\\,000$ g, "
            "and $2\\,000 > 1\\,900$. The bare numbers ($1\\,900$ "
            "against $2$) would have lied again.",
        ],
        "keyIdea": (
            "Kilograms and litres both trade for exactly 1000 of "
            "their small units. Grams and millilitres for small "
            "amounts, kilograms and litres for big ones — and no "
            "comparison until both amounts wear the same unit."),
        "facts": [
            {"title": "The two 1000-trades",
             "latex": "1\\,\\text{kg} = 1\\,000\\,\\text{g} \\qquad 1\\,\\text{l} = 1\\,000\\,\\text{ml}",
             "explanation": "Mass and capacity trade big-for-small at the same fixed rate: one thousand."},
            {"title": "Mixed amounts",
             "latex": "2\\,000 + 500 = 2\\,500",
             "explanation": "2 l 500 ml is 2500 ml — trade the litres, then add the loose millilitres."},
        ],
        "workedExamples": [
            {"id": "g4me-l2-we1",
             "statement": "Convert $4$ kg to grams, and $5\\,000$ g to kilograms.",
             "note": "Big to small multiplies the trade; small to big divides it.",
             "solution": ("$4$ kg $= 4 \\times 1\\,000 = 4\\,000$ g. "
                          "$5\\,000$ g $= 5\\,000 \\div 1\\,000 = 5$ kg, and "
                          "$5 \\times 1\\,000 = 5\\,000$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*1000, 4000)", "Eq(Rational(5000,1000), 5)"]},
            {"id": "g4me-l2-we2",
             "statement": "A jug holds $2$ l of milk; a bottle holds $1\\,500$ ml. Which holds more?",
             "note": "Trade into millilitres before comparing.",
             "solution": ("Trade: $2$ l $= 2 \\times 1\\,000 = 2\\,000$ ml. "
                          "Then $1\\,500 < 2\\,000$ — the jug holds more, by "
                          "$500$ ml, since $1\\,500 + 500 = 2\\,000$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*1000, 2000)", "1500 < 2000", "Eq(1500 + 500, 2000)"]},
        ],
        "commonMistakes": [
            {"text": "Trading a kilogram for 100 grams — writing 2 kg = 200 g.",
             "correction": "Length trades at 100, but mass and capacity trade at 1000: 2 kg = 2000 g. Each unit has its own fixed rate — say it before you multiply.",
             "authored": True},
            {"text": "Deciding 900 ml is more than 1 l because 900 > 1.",
             "correction": "Different units cannot be compared bare. Trade: 1 l = 1000 ml, and 900 < 1000 — the litre wins.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4me-l2-t1",
             "statement": "Convert $3$ l to millilitres, and $8\\,000$ ml to litres.",
             "solution": "$3 \\times 1\\,000 = 3\\,000$ ml. $8\\,000 \\div 1\\,000 = 8$ l, and $8 \\times 1\\,000 = 8\\,000$ ✓.",
             "check": ["Eq(3*1000, 3000)", "Eq(Rational(8000,1000), 8)"]},
            {"id": "g4me-l2-t2",
             "statement": "A watermelon weighs about $5$ kg. Could it be $5$ g instead?",
             "solution": "No — $5$ kg $= 5\\,000$ g, a proper two-handed carry. $5$ g is lighter than a single sweet: $5 < 5\\,000$, a $5$ g watermelon would be a crumb.",
             "check": ["Eq(5*1000, 5000)", "5 < 5000"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Grams and kilograms — the 1000-trade", [
                "Mass has a small unit and a big one, just like length — but the trade is bigger: $1$ kilogram $= 1\\,000$ grams. A gram is a sweet's weight; a kilogram is a full bag of flour.",
                "The scale below shows a melon of $%d$ g against the full kilogram mark: it falls $200$ g short, because $%d + 200 = 1\\,000$." % (melon, melon),
                "The trades so far: metres trade at $100$, kilograms at $1\\,000$. Different rates, same game — KNOW THE TRADE, then count.",
            ]), fig_scale),
            workedset("Trading grams and kilograms",
                      "Multiply by 1000 going big-to-small; divide coming back.", [
                wex("Convert $2$ kg to grams.",
                    ["The trade: each kilogram is worth $1\\,000$ g.",
                     "$2 \\times 1\\,000 = 2\\,000$ g."],
                    "$2\\,000$ g",
                    ["Eq(2*1000, 2000)"]),
                wex("A young goat weighs $9$ kg. How many grams — and is the goat heavier than a $950$ g bag of aaruul?",
                    ["$9 \\times 1\\,000 = 9\\,000$ g.",
                     "$9\\,000 > 950$ — the goat outweighs the bag many times over."],
                    "$9\\,000$ g; yes",
                    ["Eq(9*1000, 9000)", "9000 > 950"]),
            ]),
            tryitset("The mass trade", "1000 grams per kilogram — both directions.", [
                tp("$6$ kg in grams is:",
                   ["$6\\,000$ g", "$600$ g", "$60$ g"],
                   "$6 \\times 1\\,000 = 6\\,000$ g. $600$ trades at length's rate of $100$ — mass trades at $1\\,000$.",
                   ["Eq(6*1000, 6000)"]),
                tp("$7\\,000$ g in kilograms is:",
                   ["$7$ kg", "$70$ kg", "$6$ kg"],
                   "$7\\,000 \\div 1\\,000 = 7$ kg, and $7 \\times 1\\,000 = 7\\,000$ ✓.",
                   ["Eq(Rational(7000,1000), 7)", "Eq(7*1000, 7000)"]),
                tp("The sensible unit for an apple's mass is:",
                   ["grams", "kilograms", "centimetres"],
                   "An apple weighs about $150$ g — well under one kilogram, since $150 < 1\\,000$. Kilograms suit sacks and goats; centimetres measure length, not mass.",
                   ["150 < 1000"]),
            ]),
            tapq("Trade before you judge", "Which is heavier: $2$ kg of flour, or $1\\,900$ g of rice?",
                 ["the flour — $2$ kg is $2\\,000$ g",
                  "the rice — $1\\,900$ is a bigger number than $2$",
                  "they are equal",
                  "it cannot be decided"],
                 "Trade first: $2$ kg $= 2\\,000$ g. Then $1\\,900 < 2\\,000$ — the flour wins by $100$ g ($1\\,900 + 100 = 2\\,000$ ✓). Comparing $1\\,900$ with the bare $2$ is the units trap again.",
                 ["Eq(2*1000, 2000)", "1900 < 2000", "Eq(1900 + 100, 2000)"]),
            funfact("A litre of water weighs a kilogram",
                    "Pour exactly one litre of water into a bottle and set it on a scale: it weighs almost exactly one kilogram — $1\\,000$ ml of water comes to about $1\\,000$ g. That is no accident: the units were designed to match, so this lesson's two trades are secretly one."),
            withfig(teach("Concept B", "Litres and millilitres", [
                "Capacity — how much a container holds — has the same shape of trade: $1$ litre $= 1\\,000$ millilitres. A spoon holds about $5$ ml; a milk jug holds a litre or two; a bucket holds many.",
                "The jug below is filled to $%d$ ml: past the half-litre mark ($500$ ml), still $250$ short of the full litre, because $%d + 250 = 1\\,000$." % (jug, jug),
                "Mixed amounts trade in two moves: $2$ l $500$ ml is $2\\,000 + 500 = 2\\,500$ ml. Trade the litres, then add the loose millilitres.",
            ]), fig_jug),
            workedset("Trading litres and millilitres",
                      "Same 1000-trade, new containers.", [
                wex("Convert $5$ l to millilitres.",
                    ["The trade: each litre is worth $1\\,000$ ml.",
                     "$5 \\times 1\\,000 = 5\\,000$ ml."],
                    "$5\\,000$ ml",
                    ["Eq(5*1000, 5000)"]),
                wex("Which holds more: a $1\\,200$ ml pot, or a $1$ l bottle — and by how much?",
                    ["$1\\,200$ ml is $1$ l with $200$ ml over: $1\\,000 + 200 = 1\\,200$ ✓.",
                     "The pot holds more, by $200$ ml."],
                    "the pot, by $200$ ml",
                    ["Eq(1000 + 200, 1200)", "1200 > 1000"]),
            ]),
            tryitset("The capacity trade", "1000 millilitres per litre.", [
                tp("$4$ l in millilitres is:",
                   ["$4\\,000$ ml", "$400$ ml", "$40$ ml"],
                   "$4 \\times 1\\,000 = 4\\,000$ ml — capacity trades at $1\\,000$, like mass.",
                   ["Eq(4*1000, 4000)"]),
                tp("$9\\,000$ ml in litres is:",
                   ["$9$ l", "$90$ l", "$900$ l"],
                   "$9\\,000 \\div 1\\,000 = 9$ l, and $9 \\times 1\\,000 = 9\\,000$ ✓.",
                   ["Eq(Rational(9000,1000), 9)", "Eq(9*1000, 9000)"]),
                tp("A bowl of airag holds $300$ ml. Half a litre is:",
                   ["more than the bowl — $500$ ml", "less than the bowl", "exactly the bowl"],
                   "Half of $1\\,000$ ml is $500$ ml, and $300 < 500$ — the half-litre wins.",
                   ["Eq(Rational(1000,2), 500)", "300 < 500"]),
            ]),
            tapq("Mixed amounts", "A teapot holds $2\\,500$ ml. In litres and millilitres that is:",
                 ["$2$ l $500$ ml", "$25$ l", "$2$ l $50$ ml", "$5$ l $200$ ml"],
                 "Trade out the full litres: $2 \\times 1\\,000 = 2\\,000$, leaving $500$ loose millilitres — $2\\,000 + 500 = 2\\,500$ ✓. Writing $2$ l $50$ ml drops a zero from the leftover.",
                 ["Eq(2*1000 + 500, 2500)"]),
            recap([
                "One kilogram trades for 1000 grams; one litre trades for 1000 millilitres.",
                "Grams and millilitres for small amounts; kilograms and litres for big ones.",
                "Big to small multiplies by 1000; small to big divides by 1000.",
                "Mixed amounts: trade the big unit, then add the loose small ones.",
                "Compare only after trading both amounts into ONE unit.",
            ]),
            tip("Before every answer below, name the trade in play — one hundred for length, one thousand for mass and capacity — then decide which direction you are trading."),
            tryitset("Mixed practice", "Both 1000-trades, both directions, honest comparisons.", [
                tp("$8$ kg in grams is:",
                   ["$8\\,000$ g", "$800$ g", "$8\\,100$ g"],
                   "$8 \\times 1\\,000 = 8\\,000$ g.",
                   ["Eq(8*1000, 8000)"]),
                tp("Which is heavier: $2\\,500$ g or $3$ kg?",
                   ["$3$ kg", "$2\\,500$ g", "they are equal"],
                   "Trade: $3$ kg $= 3\\,000$ g, and $2\\,500 < 3\\,000$ — the $3$ kg wins by $500$ g ($2\\,500 + 500 = 3\\,000$ ✓).",
                   ["Eq(3*1000, 3000)", "2500 < 3000", "Eq(2500 + 500, 3000)"]),
                tp("$6\\,000$ ml in litres is:",
                   ["$6$ l", "$60$ l", "$600$ l"],
                   "$6\\,000 \\div 1\\,000 = 6$ l, and $6 \\times 1\\,000 = 6\\,000$ ✓.",
                   ["Eq(Rational(6000,1000), 6)", "Eq(6*1000, 6000)"]),
                withfig(tp("Each flour bag holds $%d$ kg, and there are $%d$ bags. The total mass in grams is:" % (bag_kg, bags),
                   ["$6\\,000$ g", "$600$ g", "$3\\,000$ g"],
                   "Count the kilograms first: $%d \\times %d = 6$ kg. Then trade: $6 \\times 1\\,000 = 6\\,000$ g. $3\\,000$ g counts only half the bags." % (bags, bag_kg),
                   ["Eq(%d*%d, 6)" % (bags, bag_kg), "Eq(6*1000, 6000)"]), fig_flour),
                tp("A spoon holds about:",
                   ["$5$ ml", "$5$ l", "$5$ kg"],
                   "A spoonful is tiny next to a litre: $5 < 1\\,000$. Five litres is a full bucket, and kilograms measure mass, not how much a spoon holds.",
                   ["5 < 1000"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Mass & Capacity\"",
                    "Two more fixed trades — a thousand grams to the kilogram, a thousand millilitres to the litre — and the same one-unit rule for comparing. Next: a trade that is NOT built from tens at all — the sixty-minute hour.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Reading the Clock
# ==========================================================================

def lesson_clock():
    # a clock face at 3:00 — an actual rim (the twelve hour marks joined in
    # order), minute hand up to 12, hour hand right to 3; the two hands
    # really are perpendicular in the coordinates.
    cx, cy, rim_r = 5.0, 5.0, 4.2
    hour_pts, rim = [], []
    for k in range(1, 13):
        theta = math.radians(90 - 30 * k)
        label = {12: "12", 3: "3", 6: "6", 9: "9"}.get(k, "")
        hour_pts.append(P("h%d" % k, cx + rim_r * math.cos(theta),
                          cy + rim_r * math.sin(theta), label))
    for k in range(1, 13):
        rim.append(seg("h%d" % k, "h%d" % (k % 12 + 1), color=C_NEUTRAL))
    fig_clock = fig_geo(
        hour_pts + [P("C", cx, cy, ""), P("M", 5, 8.2, ""), P("H", 7.2, 5, "")],
        rim + [seg("C", "M", color=C_ACCENT), seg("C", "H", color=C_WARM),
               ang("C", "M", "H", right=True)],
        height=220)
    fig_track = fig_numline(
        [(0, "12 — o'clock"), (15, "3 — quarter past", C_GREEN),
         (30, "6 — half past", C_ACCENT), (45, "9 — quarter to", C_WARM),
         (60, "60 min")], lo=0, hi=60)
    return {
        "slug": "reading-the-clock",
        "title": "Reading the Clock",
        "concreteComparison": (
            "The minute hand runs a race track of $60$ little steps, "
            "once around every hour. Four flags stand on the track: "
            "the start at $12$ (o'clock), the quarter flag at $3$ "
            "($15$ minutes), the halfway flag at $6$ ($30$ minutes), "
            "and the three-quarter flag at $9$ ($45$ minutes) — where "
            "we stop saying PAST and start saying TO the next hour."),
        "objective": (
            "Read o'clock, half past, quarter past and quarter to on "
            "a clock face, say each as minutes past the hour, and use "
            "the fact that one hour trades for exactly $60$ minutes."),
        "concept": [
            "**One hour trades for 60 minutes.** Not $100$ — sixty. "
            "The minute hand's full lap is $60$ minutes; the hour "
            "hand meanwhile creeps from one number to the next. Two "
            "half-laps make the lap: $30 + 30 = 60$.",
            "**Half past and quarter past are fractions of 60.** Half "
            "the lap is $60 \\div 2 = 30$ minutes (minute hand at "
            "$6$); a quarter lap is $60 \\div 4 = 15$ minutes (minute "
            "hand at $3$). Half past $7$ means $7$:$30$.",
            "**Quarter to names the NEXT hour.** At $45$ minutes past "
            "(minute hand at $9$), three quarters are done — $3 "
            "\\times 15 = 45$ — and one quarter remains: $45 + 15 = "
            "60$. So $7$:$45$ is called quarter to $8$, not quarter "
            "to $7$.",
        ],
        "keyIdea": (
            "The hour trades for 60 minutes. O'clock is 0 minutes "
            "past, quarter past is 15, half past is 30, and quarter "
            "to is 45 — a quarter short of the NEXT hour."),
        "facts": [
            {"title": "The quarter marks",
             "latex": "\\frac{60}{4} = 15 \\qquad \\frac{60}{2} = 30",
             "explanation": "A quarter of the hour is 15 minutes; half is 30. The clock's flags are fractions of sixty."},
            {"title": "Quarter to",
             "latex": "45 + 15 = 60",
             "explanation": "At 45 minutes past, one quarter remains — so the time is named TO the next hour."},
        ],
        "workedExamples": [
            {"id": "g4me-l3-we1",
             "statement": "The minute hand points at $6$ and the hour hand sits halfway between $7$ and $8$. What time is it?",
             "note": "Minute hand at 6 = half the lap.",
             "solution": ("Half the $60$-minute lap is $60 \\div 2 = 30$ minutes. "
                          "The hour hand left $7$ but has not reached $8$: it is "
                          "half past $7$, written $7$:$30$. Another half-lap "
                          "reaches $8$ o'clock: $30 + 30 = 60$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(60,2), 30)", "Eq(30 + 30, 60)"]},
            {"id": "g4me-l3-we2",
             "statement": "Write \"quarter to $4$\" in digits.",
             "note": "Quarter to means 15 minutes BEFORE the named hour.",
             "solution": ("A quarter of the hour is $60 \\div 4 = 15$ minutes. "
                          "Quarter to $4$ is $15$ minutes before $4$ o'clock — "
                          "so the hour showing is still $3$, with $3 \\times 15 "
                          "= 45$ minutes past: $3$:$45$. Check: $45 + 15 = 60$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(60,4), 15)", "Eq(3*15, 45)", "Eq(45 + 15, 60)"]},
        ],
        "commonMistakes": [
            {"text": "Calling 7:45 \"quarter to 7\".",
             "correction": "Quarter TO names the hour coming NEXT: 7:45 is 15 minutes before 8, so it is quarter to 8. The hour digit on the clock lags behind the name.",
             "authored": True},
            {"text": "Treating the hour as 100 minutes — half past as 50 minutes.",
             "correction": "The hour trades for 60 minutes, so half past is 60 divided by 2, which is 30 — the minute hand at the 6, not at some 50-mark.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4me-l3-t1",
             "statement": "Where does the minute hand point at quarter past $9$, and how is the time written in digits?",
             "solution": "A quarter lap is $60 \\div 4 = 15$ minutes, so the minute hand points at $3$. In digits: $9$:$15$.",
             "check": ["Eq(Rational(60,4), 15)"]},
            {"id": "g4me-l3-t2",
             "statement": "How many minutes does the minute hand take for one full lap of the clock?",
             "solution": "Four quarter-laps of $15$ make the lap: $4 \\times 15 = 60$ minutes — one hour. Two half-laps agree: $2 \\times 30 = 60$ ✓.",
             "check": ["Eq(4*15, 60)", "Eq(2*30, 60)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "O'clock and half past", [
                "The clock face sketched below shows $3$ o'clock: the twelve hour marks ring the rim, the long minute hand points straight up at $12$ — zero minutes past — and the short hour hand points at $3$. At $3$ o'clock the two hands even make a perfect square corner.",
                "The hour's trade is SIXTY: one full lap of the minute hand is $60$ minutes, and from $12$:$00$ to $3$:$00$ it has made three laps — $3 \\times 60 = 180$ minutes.",
                "When the minute hand reaches $6$, it has run HALF its lap: $60 \\div 2 = 30$ minutes past. Hour hand between $4$ and $5$ with minute hand at $6$ reads: half past $4$.",
            ]), fig_clock),
            workedset("Reading the easy flags",
                      "Minute hand at 12: o'clock. Minute hand at 6: half past.", [
                wex("The minute hand points at $12$ and the hour hand at $3$. The time?",
                    ["Minute hand at $12$: zero minutes past — an o'clock time.",
                     "Since $12$:$00$ the minute hand has lapped $3$ times: $3 \\times 60 = 180$ minutes. It is $3$ o'clock."],
                    "$3$:$00$",
                    ["Eq(3*60, 180)"]),
                wex("Write \"half past $9$\" in digits.",
                    ["Half the lap: $60 \\div 2 = 30$ minutes past.",
                     "$9$:$30$ — and another $30$ minutes reaches $10$:$00$, since $30 + 30 = 60$ ✓."],
                    "$9$:$30$",
                    ["Eq(Rational(60,2), 30)", "Eq(30 + 30, 60)"]),
            ]),
            tryitset("O'clock and half past", "Find the minute hand first; it names the flag.", [
                tp("The minute hand points at $6$; the hour hand sits between $4$ and $5$. The time is:",
                   ["half past $4$", "half past $5$", "$4$ o'clock"],
                   "Minute hand at $6$ means $60 \\div 2 = 30$ minutes past. The hour hand has LEFT $4$ but not reached $5$ — so the hour is still $4$: half past $4$. Reading the nearer number $5$ is the trap.",
                   ["Eq(Rational(60,2), 30)", "30 < 60"]),
                tp("How many minutes pass from $7$:$00$ to half past $7$?",
                   ["$30$", "$7$", "$60$"],
                   "Half the hour's lap: $60 \\div 2 = 30$ minutes.",
                   ["Eq(Rational(60,2), 30)"]),
                tp("One full lap of the minute hand takes:",
                   ["$60$ minutes", "$100$ minutes", "$12$ minutes"],
                   "The hour trades for sixty: two half-laps of $30$ make it ($2 \\times 30 = 60$), and four quarter-laps of $15$ agree ($4 \\times 15 = 60$). $100$ is the tens reflex — clocks refuse it.",
                   ["Eq(2*30, 60)", "Eq(4*15, 60)"]),
            ]),
            tapq("Find the minute hand", "At half past $11$, the minute hand points at:",
                 ["$6$", "$11$", "$12$", "$3$"],
                 "Half past means half the lap is run: $60 \\div 2 = 30$ minutes, which is the $6$ at the bottom of the face. The hour hand is the one near $11$ — mixing the hands up swaps the whole reading.",
                 ["Eq(Rational(60,2), 30)"]),
            funfact("Why 60 and not 100?",
                    "The 60-minute hour comes from ancient Babylon, and it survived because $60$ splits so cleanly: by $2, 3, 4, 5, 6, 10, 12, 15, 20$ and $30$. So half an hour is a whole $30$, a third is $20$, a quarter is $15$ — no leftovers. A 100-minute hour would make a third of an hour impossible to say in whole minutes."),
            withfig(teach("Concept B", "Quarter past and quarter to", [
                "The minute track below lays the lap out straight, with all four flags. A quarter of the lap is $60 \\div 4 = 15$ minutes: minute hand at $3$, and we say QUARTER PAST — quarter past $6$ is $6$:$15$.",
                "At the $9$, three quarters are done: $3 \\times 15 = 45$ minutes past. Only one quarter remains — $45 + 15 = 60$ — so we name the hour that is COMING: quarter to.",
                "Quarter to $8$ is therefore $7$:$45$. The digits keep the old hour; the name looks ahead to the new one. That switch is the only tricky step on the whole track.",
            ]), fig_track),
            workedset("The quarter flags",
                      "15 past: quarter past. 45 past: quarter TO the next hour.", [
                wex("Write \"quarter past $6$\" in digits.",
                    ["A quarter lap: $60 \\div 4 = 15$ minutes past.",
                     "$6$:$15$, minute hand at $3$."],
                    "$6$:$15$",
                    ["Eq(Rational(60,4), 15)"]),
                wex("Write \"quarter to $8$\" in digits.",
                    ["Quarter to $8$ is $15$ minutes before $8$:$00$ — the hour showing is still $7$.",
                     "Minutes past $7$: $3 \\times 15 = 45$. So $7$:$45$, and $45 + 15 = 60$ ✓."],
                    "$7$:$45$",
                    ["Eq(3*15, 45)", "Eq(45 + 15, 60)"]),
            ]),
            tryitset("Past or to?", "Up to the 6, say PAST; after it, say TO the next hour.", [
                tp("A clock shows $2$:$15$. In words that is:",
                   ["quarter past $2$", "quarter to $2$", "half past $2$"],
                   "$15$ minutes is a quarter of the lap ($60 \\div 4 = 15$), and the hand is on its way PAST $2$ — quarter past $2$. Quarter to $2$ would be $1$:$45$.",
                   ["Eq(Rational(60,4), 15)"]),
                tp("\"Quarter to $10$\" in digits is:",
                   ["$9$:$45$", "$10$:$45$", "$10$:$15$"],
                   "Quarter to $10$ sits $15$ minutes before $10$:$00$, so the hour digit is still $9$: $9$:$45$, since $45 + 15 = 60$ ✓. Writing $10$:$45$ jumps a whole hour ahead.",
                   ["Eq(45 + 15, 60)", "Eq(3*15, 45)"]),
                tp("From quarter past $5$ to half past $5$ is:",
                   ["$15$ minutes", "$30$ minutes", "$45$ minutes"],
                   "From the $15$-minute flag to the $30$-minute flag: $15 + 15 = 30$ — one more quarter lap, $15$ minutes.",
                   ["Eq(15 + 15, 30)"]),
            ]),
            tapq("The name looks ahead", "A clock shows $7$:$45$. In words that is:",
                 ["quarter to $8$", "quarter to $7$", "quarter past $7$", "half past $7$"],
                 "$45$ minutes past means three quarter-laps done ($3 \\times 15 = 45$) and one to go ($45 + 15 = 60$) — so the name looks ahead: quarter to $8$. \"Quarter to $7$\" reads the digit instead of the direction.",
                 ["Eq(3*15, 45)", "Eq(45 + 15, 60)"]),
            recap([
                "One hour trades for 60 minutes — never 100.",
                "Minute hand at 12: o'clock, 0 minutes past.",
                "Minute hand at 3: quarter past, 15 minutes (60 divided by 4).",
                "Minute hand at 6: half past, 30 minutes (60 divided by 2).",
                "Minute hand at 9: quarter to the NEXT hour, 45 minutes past this one.",
            ]),
            tip("For each clock below, find the MINUTE hand first and say its flag — o'clock, quarter past, half past, or quarter to — then let the hour hand fill in the hour."),
            tryitset("Mixed practice", "All four flags of the 60-minute lap.", [
                tp("The minute hand points at $9$. Minutes past the hour:",
                   ["$45$", "$9$", "$15$"],
                   "The $9$ is the three-quarter flag: $3 \\times 15 = 45$ minutes past. Reading the $9$ itself as minutes is the trap.",
                   ["Eq(3*15, 45)"]),
                tp("$5$:$30$ in words is:",
                   ["half past $5$", "half past $6$", "quarter to $5$"],
                   "$30$ minutes is half the lap ($60 \\div 2 = 30$): half past $5$. Half past $6$ would show $6$:$30$.",
                   ["Eq(Rational(60,2), 30)"]),
                tp("How many quarter-hours fit in one hour?",
                   ["$4$", "$2$", "$15$"],
                   "Four quarters rebuild the lap: $4 \\times 15 = 60$ minutes.",
                   ["Eq(4*15, 60)"]),
                tp("From quarter to $9$ until $9$ o'clock is:",
                   ["$15$ minutes", "$45$ minutes", "$60$ minutes"],
                   "Quarter to means one quarter remains: $45 + 15 = 60$ — just $15$ minutes to the hour.",
                   ["Eq(45 + 15, 60)"]),
                tp("The hour hand sits halfway between $10$ and $11$, the minute hand at $6$. The time is:",
                   ["half past $10$", "half past $11$", "$10$ o'clock"],
                   "Minute hand at $6$: $60 \\div 2 = 30$ minutes past. The hour hand halfway between $10$ and $11$ says the hour $10$ is half spent: half past $10$.",
                   ["Eq(Rational(60,2), 30)", "30 < 60"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Reading the Clock\"",
                    "The 60-trade and its four flags — o'clock, quarter past, half past, quarter to. Next: the clock in motion — days, weeks, months, and how long things LAST, counted in minutes.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Calendar & Duration
# ==========================================================================

def lesson_calendar():
    wk, nw = 7, 4
    fig_weeks = fig_groups(*[(wk, "week %d" % (i + 1)) for i in range(nw)])
    # lesson timeline: 8:00 (480 min) + 40 min = 8:40 (520 min)
    t0, dur = 480, 40
    t1 = t0 + dur
    fig_timeline = fig_numline(
        [(t0, "8:00"), (t1, "8:40", C_GREEN), (540, "9:00")], lo=t0, hi=540)
    return {
        "slug": "calendar-and-duration",
        "title": "Calendar & Duration",
        "concreteComparison": (
            "A herder's summer runs on two clocks at once. The big "
            "one is the calendar: $7$ days to the week, $12$ months "
            "to the year, $365$ days in all. The small one is the "
            "day itself, where a milking that starts at $8$:$00$ and "
            "takes $40$ minutes ends at $8$:$40$ — start plus length "
            "gives the end, every single time."),
        "objective": (
            "Use the calendar trades — $7$ days a week, $12$ months "
            "and $365$ days a year — and find durations inside one "
            "day: start time plus length gives the end time, counted "
            "up through the round hour in minutes."),
        "concept": [
            "**The week trades for 7 days.** Three weeks are $3 "
            "\\times 7 = 21$ days; and $30$ days make $4$ full weeks "
            "with $2$ days over, since $4 \\times 7 + 2 = 30$.",
            "**The year holds 12 months and 365 days.** Months are "
            "uneven — $30$ or $31$ days, and February with $28$ — "
            "but the year's totals are fixed: $12$ months, $365$ "
            "days ($366$ in a leap year, one extra: $365 + 1 = 366$).",
            "**Start + length = end.** A lesson starting at $8$:$00$ "
            "and lasting $40$ minutes ends at $8$:$40$. When the "
            "minutes would pass the hour, count UP THROUGH the round "
            "hour: from $9$:$40$, first $20$ minutes to $10$:$00$, "
            "then the rest.",
        ],
        "keyIdea": (
            "Weeks trade for 7 days and years for 12 months and 365 "
            "days. Inside one day, start plus length equals end — and "
            "the round hour is the stepping stone when minutes spill "
            "over."),
        "facts": [
            {"title": "The calendar trades",
             "latex": "1\\,\\text{week} = 7\\,\\text{days} \\qquad 1\\,\\text{year} = 12\\,\\text{months}",
             "explanation": "The week's trade is fixed at 7; the year holds 12 months and 365 days (366 when leap)."},
            {"title": "Start + length = end",
             "latex": "480 + 40 = 520",
             "explanation": "In minutes: 8:00 is 480 minutes into the day, plus a 40-minute lesson lands on 520 — which is 8:40."},
        ],
        "workedExamples": [
            {"id": "g4me-l4-we1",
             "statement": "Summer camp lasts $3$ weeks. How many days is that?",
             "note": "The week's trade: 7 days each.",
             "solution": ("$3 \\times 7 = 21$ days. Three rows of a calendar "
                          "page — three Mondays, three Sundays, twenty-one "
                          "boxes."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*7, 21)"]},
            {"id": "g4me-l4-we2",
             "statement": "A maths lesson starts at $8$:$00$ and lasts $40$ minutes. When does it end?",
             "note": "Work in minutes: start + length = end.",
             "solution": ("In minutes since midnight, $8$:$00$ is $8 \\times 60 "
                          "= 480$. Add the length: $480 + 40 = 520$ minutes, "
                          "which is $8$:$40$ — still inside the same hour, no "
                          "spill-over."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*60, 480)", "Eq(480 + 40, 520)"]},
        ],
        "commonMistakes": [
            {"text": "Giving every month 30 days.",
             "correction": "Months are uneven: some have 31, some 30, and February has 28 (29 in a leap year). Only the year's totals are fixed — 12 months, 365 days.",
             "authored": True},
            {"text": "Adding minutes straight past the hour — 9:40 plus 30 minutes becomes 9:70.",
             "correction": "There is no 9:70; the hour holds only 60 minutes. Count up through the round hour: 20 minutes reach 10:00, and the other 10 land on 10:10.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4me-l4-t1",
             "statement": "How many days are in $4$ weeks?",
             "solution": "$4 \\times 7 = 28$ days — exactly February's count in an ordinary year.",
             "check": ["Eq(4*7, 28)"]},
            {"id": "g4me-l4-t2",
             "statement": "A film starts at $2$:$00$ and ends at $3$:$30$. How long is it?",
             "solution": "In minutes: $2$:$00$ is $2 \\times 60 = 120$ and $3$:$30$ is $3 \\times 60 + 30 = 210$. The length is $90$ minutes, since $120 + 90 = 210$ ✓ — one hour and thirty minutes, as $60 + 30 = 90$.",
             "check": ["Eq(2*60, 120)", "Eq(3*60 + 30, 210)", "Eq(120 + 90, 210)", "Eq(60 + 30, 90)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The calendar's trades", [
                "The calendar below shows $%d$ weeks of $%d$ days — $%d \\times %d = 28$ days, which is exactly February in an ordinary year." % (nw, wk, nw, wk),
                "The week's trade never bends: $7$ days, always. But months are uneven — $30$ or $31$ days, February $28$ — so a month is ABOUT four weeks, never exactly.",
                "The year's totals are fixed: $12$ months, $365$ days. A leap year adds one: $365 + 1 = 366$.",
            ]), fig_weeks),
            workedset("Weeks into days",
                      "Multiply by 7 for days; divide by 7 for weeks — remainders welcome.", [
                wex("How many days in $5$ weeks?",
                    ["The trade: $7$ days per week.",
                     "$5 \\times 7 = 35$ days."],
                    "$35$ days",
                    ["Eq(5*7, 35)"]),
                wex("February has $28$ days. How many full weeks is that?",
                    ["$28 \\div 7 = 4$ — exactly four weeks, nothing left over.",
                     "Receipt: $4 \\times 7 = 28$ ✓. February is the only month that can be all whole weeks."],
                    "$4$ weeks",
                    ["Eq(Rational(28,7), 4)", "Eq(4*7, 28)"]),
            ]),
            tryitset("Calendar counts", "Say the week's trade — seven — before multiplying.", [
                tp("$2$ weeks is how many days?",
                   ["$14$", "$9$", "$20$"],
                   "$2 \\times 7 = 14$ days. $9$ adds the $2$ and the $7$ instead of trading.",
                   ["Eq(2*7, 14)"]),
                tp("How many full weeks fit in $28$ days?",
                   ["$4$", "$3$", "$7$"],
                   "$28 \\div 7 = 4$ weeks, receipt $4 \\times 7 = 28$ ✓.",
                   ["Eq(Rational(28,7), 4)", "Eq(4*7, 28)"]),
                tp("June has $30$ days. As weeks and days that is:",
                   ["$4$ weeks $2$ days", "$3$ weeks $9$ days", "$5$ weeks exactly"],
                   "$4 \\times 7 = 28$, and $2$ more reach $30$: receipt $4 \\times 7 + 2 = 30$ with $2 < 7$ ✓. \"$3$ weeks $9$ days\" hides a whole extra week inside the $9$.",
                   ["Eq(4*7 + 2, 30)", "2 < 7"]),
            ]),
            tapq("The year's totals", "How many days are in an ordinary year, and in a leap year?",
                 ["$365$, and $366$ in a leap year",
                  "$360$, and $361$ in a leap year",
                  "$300$, and $301$ in a leap year",
                  "$400$ in both"],
                 "An ordinary year has $365$ days; a leap year adds one extra day at the end of February: $365 + 1 = 366$. The months are uneven, but these totals never change.",
                 ["Eq(365 + 1, 366)"]),
            funfact("Why leap years exist",
                    "A year is $365$ days because that is how long Earth takes to travel once around the Sun — almost. The true trip takes about a quarter of a day longer, so every fourth year the calendar collects the four quarters into one whole extra day: $4 \\times \\frac{1}{4} = 1$, and February gets a $29$th day."),
            withfig(teach("Concept B", "Durations inside one day", [
                "How long something lasts obeys one equation: START + LENGTH = END. The timeline below shows it in minutes: $8$:$00$ is $8 \\times 60 = %d$ minutes into the day, and a $%d$-minute lesson lands on $%d + %d = %d$ — that is $8$:$40$." % (t0, dur, t0, dur, t1),
                "When minutes would spill past the hour, use the round hour as a stepping stone. From $9$:$40$ to $10$:$10$: first $20$ minutes climb to $10$:$00$, then $10$ more — $20 + 10 = 30$ minutes in all.",
                "The spill-over trap has a name: there is no $9$:$70$. The hour holds only $60$ minutes, so every count must STEP ON the round hour, never run straight past it — that is why $9$:$40$ plus $30$ minutes is $10$:$10$, not $9$:$70$.",
            ]), fig_timeline),
            workedset("Start, length, end",
                      "All three in minutes; the round hour is the stepping stone.", [
                wex("A lesson starts at $8$:$00$ and lasts $40$ minutes. End time?",
                    ["$8$:$00$ is $8 \\times 60 = 480$ minutes into the day.",
                     "$480 + 40 = 520$ minutes — which is $8$:$40$."],
                    "$8$:$40$",
                    ["Eq(8*60, 480)", "Eq(480 + 40, 520)"]),
                wex("How long is it from $9$:$40$ to $10$:$10$?",
                    ["Step to the round hour: $20$ minutes reach $10$:$00$; then $10$ more.",
                     "$20 + 10 = 30$ minutes. Receipt in minutes: $9$:$40$ is $9 \\times 60 + 40 = 580$, and $580 + 30 = 610$, which is $10$:$10$ ✓."],
                    "$30$ minutes",
                    ["Eq(20 + 10, 30)", "Eq(9*60 + 40, 580)", "Eq(580 + 30, 610)"]),
            ]),
            tryitset("Count the minutes", "Start + length = end — receipt every answer.", [
                tp("A cartoon starts at $5$:$00$ and lasts $30$ minutes. It ends at:",
                   ["$5$:$30$", "$5$:$03$", "$6$:$30$"],
                   "$5$:$00$ is $5 \\times 60 = 300$ minutes; $300 + 30 = 330$, which is $5$:$30$. Writing $5$:$03$ drops a zero, and $6$:$30$ adds a whole extra hour.",
                   ["Eq(5*60, 300)", "Eq(300 + 30, 330)"]),
                tp("From $9$:$15$ to $9$:$45$ is:",
                   ["$30$ minutes", "$45$ minutes", "$15$ minutes"],
                   "Same hour, so the minutes tell all: from $15$ past to $45$ past is $30$, since $15 + 30 = 45$ ✓.",
                   ["Eq(15 + 30, 45)"]),
                tp("Buses leave at $7$:$00$, $7$:$30$ and $8$:$00$. They run every:",
                   ["$30$ minutes", "$70$ minutes", "$7$ minutes"],
                   "$7$:$00$ is $7 \\times 60 = 420$ minutes and $7$:$30$ is $450$: the gap is $30$, since $420 + 30 = 450$ ✓ — and $30$ more reaches $8$:$00$ at $480$.",
                   ["Eq(7*60, 420)", "Eq(420 + 30, 450)", "Eq(450 + 30, 480)"]),
            ]),
            tapq("Through the round hour", "Wrestling is on TV from $6$:$30$ to $7$:$15$. How long is that?",
                 ["$45$ minutes", "$85$ minutes", "$15$ minutes", "$30$ minutes"],
                 "Step through $7$:$00$: from $6$:$30$ that is $30$ minutes, then $15$ more — $30 + 15 = 45$ minutes. Receipt: $6$:$30$ is $6 \\times 60 + 30 = 390$ minutes, and $390 + 45 = 435$, which is $7$:$15$ ✓.",
                 ["Eq(30 + 15, 45)", "Eq(6*60 + 30, 390)", "Eq(390 + 45, 435)"]),
            recap([
                "The week trades for 7 days — always.",
                "A year holds 12 months and 365 days; a leap year has 366.",
                "Months are uneven: 30 or 31 days, and February with 28.",
                "Start + length = end, with everything counted in minutes.",
                "When minutes spill past the hour, step through the round hour — no 9:70 exists.",
            ]),
            tip("For every duration below, write start + length = end in minutes and check the sum — the receipt catches every spill-over mistake."),
            tryitset("Mixed practice", "Calendar trades and one-day durations together.", [
                tp("$6$ weeks is how many days?",
                   ["$42$", "$13$", "$60$"],
                   "$6 \\times 7 = 42$ days. $13$ adds instead of trading.",
                   ["Eq(6*7, 42)"]),
                tp("A $31$-day month is how many weeks and days?",
                   ["$4$ weeks $3$ days", "$4$ weeks $1$ day", "$3$ weeks $3$ days"],
                   "$4 \\times 7 = 28$, and $3$ more reach $31$: receipt $4 \\times 7 + 3 = 31$ with $3 < 7$ ✓.",
                   ["Eq(4*7 + 3, 31)", "3 < 7"]),
                tp("From $3$:$20$ to $4$:$00$ is:",
                   ["$40$ minutes", "$20$ minutes", "$80$ minutes"],
                   "Climb to the round hour: $20 + 40 = 60$, so $40$ minutes. Receipt: $3$:$20$ is $3 \\times 60 + 20 = 200$ minutes and $200 + 40 = 240$, which is $4$:$00$ ✓.",
                   ["Eq(20 + 40, 60)", "Eq(3*60 + 20, 200)", "Eq(200 + 40, 240)"]),
                tp("Football practice starts at $5$:$20$ and lasts $50$ minutes. It ends at:",
                   ["$6$:$10$", "$5$:$70$", "$6$:$20$"],
                   "$5$:$20$ is $5 \\times 60 + 20 = 320$ minutes; $320 + 50 = 370$, which is $6 \\times 60 + 10$ — so $6$:$10$. \"$5$:$70$\" is the spill-over trap: no hour holds $70$ minutes.",
                   ["Eq(5*60 + 20, 320)", "Eq(320 + 50, 370)", "Eq(6*60 + 10, 370)"]),
                tp("How many days does a leap year have?",
                   ["$366$", "$365$", "$364$"],
                   "The ordinary $365$ plus February's extra day: $365 + 1 = 366$.",
                   ["Eq(365 + 1, 366)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Calendar & Duration\"",
                    "Weeks of seven, years of twelve months and $365$ days, and the one-day equation start + length = end. Next: the trade you can hold in your hand — togrog notes, and change counted UP instead of down.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Counting Money
# ==========================================================================

def lesson_money():
    n5000, n1000, n500 = 1, 2, 1
    purse = n5000 * 5000 + n1000 * 1000 + n500 * 500  # 7500
    fig_purse = fig_groups(
        (n5000, "5000 note", C_ACCENT),
        (n1000, "1000 notes", C_GREEN),
        (n500, "500 note", C_WARM))
    price, paid = 700, 1000
    change = paid - price  # 300
    fig_countup = fig_numline(
        [(price, "%d — price" % price, C_WARM), (800, "800"), (900, "900"),
         (paid, "%d — paid" % paid, C_GREEN)], lo=600, hi=1000)
    return {
        "slug": "togrog-money",
        "title": "Counting Money",
        "concreteComparison": (
            "At the Naadam fair a khuushuur costs $700$ togrog and "
            "you hand over a $1\\,000$ note. The seller does not "
            "subtract — she counts UP, pressing coins into your hand: "
            "eight hundred, nine hundred, one thousand. You walk away "
            "with $300$ togrog of change, and the receipt is built "
            "into the counting: change plus price makes exactly what "
            "you paid."),
        "objective": (
            "Total a handful of $500$, $1\\,000$, $5\\,000$ and "
            "$10\\,000$ togrog notes, make one amount in different "
            "ways, and give change from a round payment by counting "
            "up from the price."),
        "concept": [
            "**Count value, not paper.** A purse's worth is each "
            "note's value times its count, added up: one $5\\,000$ "
            "note, two $1\\,000$ notes and a $500$ note make $5\\,000 "
            "+ 2\\,000 + 500 = 7\\,500$ togrog. Three notes can beat "
            "ten — value decides, never the count of papers.",
            "**Notes trade like units.** Two $500$ notes trade for "
            "one $1\\,000$ note ($2 \\times 500 = 1\\,000$); five "
            "$1\\,000$ notes trade for one $5\\,000$. So one amount "
            "can be MADE many ways — $4\\,000$ is four $1\\,000$ "
            "notes, or eight $500$ notes.",
            "**Change counts UP.** Price $700$, paid $1\\,000$: start "
            "at the price and climb to the payment — $800$, $900$, "
            "$1\\,000$ — that climb is the change, $300$. The receipt "
            "is automatic: $300 + 700 = 1\\,000$.",
        ],
        "keyIdea": (
            "Money is measured in value, not in pieces of paper: "
            "total the values, trade notes like units, and give "
            "change by counting up from the price to the payment — "
            "change plus price equals paid."),
        "facts": [
            {"title": "Notes trade like units",
             "latex": "2 \\times 500 = 1\\,000 \\qquad 5 \\times 1\\,000 = 5\\,000",
             "explanation": "Two 500-togrog notes are worth one 1000 note; five 1000 notes are worth one 5000 note."},
            {"title": "Change counts up",
             "latex": "300 + 700 = 1\\,000",
             "explanation": "Change plus price equals what was paid — counting up builds the receipt as you go."},
        ],
        "workedExamples": [
            {"id": "g4me-l5-we1",
             "statement": "A purse holds one $5\\,000$ note, two $1\\,000$ notes and one $500$ note. How many togrog in all?",
             "note": "Value times count for each kind, then add.",
             "solution": ("$5\\,000 + 2 \\times 1\\,000 + 500 = 5\\,000 + "
                          "2\\,000 + 500 = 7\\,500$ togrog. Four pieces of "
                          "paper, seven and a half thousand of value."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5000 + 2*1000 + 500, 7500)"]},
            {"id": "g4me-l5-we2",
             "statement": "A khuushuur costs $700$ togrog and you pay with a $1\\,000$ note. What is your change?",
             "note": "Count up from the price to the payment.",
             "solution": ("Climb from $700$: $800$, $900$, $1\\,000$ — three "
                          "steps of $100$, so the change is $300$ togrog. "
                          "Receipt: $300 + 700 = 1\\,000$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*100, 300)", "Eq(300 + 700, 1000)"]},
        ],
        "commonMistakes": [
            {"text": "Judging a purse by its number of notes — three 1000 notes must beat one 5000 note.",
             "correction": "Count VALUE, not paper: three thousands make 3000, and 3000 < 5000. One big note outweighs a small stack.",
             "authored": True},
            {"text": "Giving change without a receipt, so a slip of 100 goes unnoticed.",
             "correction": "Always add the change back to the price: if change + price does not equal what was paid, the change is wrong. 300 + 700 = 1000 is the whole proof.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4me-l5-t1",
             "statement": "Show two different ways to make $3\\,000$ togrog with notes.",
             "solution": "Three $1\\,000$ notes: $3 \\times 1\\,000 = 3\\,000$. Or six $500$ notes: $6 \\times 500 = 3\\,000$. Same value, different paper.",
             "check": ["Eq(3*1000, 3000)", "Eq(6*500, 3000)"]},
            {"id": "g4me-l5-t2",
             "statement": "A book costs $4\\,200$ togrog and you pay with a $5\\,000$ note. Find the change by counting up.",
             "solution": "From $4\\,200$: up $300$ to $4\\,500$, up $500$ more to $5\\,000$ — change $800$ togrog, since $300 + 500 = 800$. Receipt: $800 + 4\\,200 = 5\\,000$ ✓.",
             "check": ["Eq(300 + 500, 800)", "Eq(800 + 4200, 5000)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Count value, not paper", [
                "Togrog notes come in sizes: $500$, $1\\,000$, $5\\,000$, $10\\,000$. A purse's worth is VALUE times COUNT for each size, added up — the purse below holds $5\\,000 + 2\\,000 + 500 = 7\\,500$ togrog in just four notes.",
                "Notes trade like every unit in this topic: two $500$ notes make a $1\\,000$ ($2 \\times 500 = 1\\,000$), five $1\\,000$ notes make a $5\\,000$, two $5\\,000$ notes make a $10\\,000$.",
                "Because of the trades, one amount wears many outfits: $4\\,000$ togrog is four $1\\,000$ notes, or eight $500$ notes — the value never notices the difference.",
            ]), fig_purse),
            workedset("Purse totals",
                      "Biggest notes first; value times count; add.", [
                wex("Total one $5\\,000$ note, two $1\\,000$ notes and one $500$ note.",
                    ["$5\\,000$, then $2 \\times 1\\,000 = 2\\,000$, then $500$.",
                     "$5\\,000 + 2\\,000 + 500 = 7\\,500$ togrog."],
                    "$7\\,500$ togrog",
                    ["Eq(2*1000, 2000)", "Eq(5000 + 2000 + 500, 7500)"]),
                wex("Make $4\\,000$ togrog two different ways.",
                    ["Four $1\\,000$ notes: $4 \\times 1\\,000 = 4\\,000$.",
                     "Or eight $500$ notes: $8 \\times 500 = 4\\,000$ — same value, twice the paper."],
                    "$4 \\times 1\\,000$ or $8 \\times 500$",
                    ["Eq(4*1000, 4000)", "Eq(8*500, 4000)"]),
            ]),
            tryitset("Total the notes", "Value times count — paper is just a costume.", [
                tp("Two $1\\,000$ notes and one $500$ note make:",
                   ["$2\\,500$ togrog", "$3\\,000$ togrog", "$1\\,500$ togrog"],
                   "$2 \\times 1\\,000 = 2\\,000$, plus $500$: $2\\,500$ togrog. $1\\,500$ counts only one of the thousands.",
                   ["Eq(2*1000 + 500, 2500)"]),
                tp("One $5\\,000$ note and three $1\\,000$ notes make:",
                   ["$8\\,000$ togrog", "$5\\,300$ togrog", "$9\\,000$ togrog"],
                   "$5\\,000 + 3 \\times 1\\,000 = 5\\,000 + 3\\,000 = 8\\,000$ togrog. $5\\,300$ treats the three thousands as three hundreds.",
                   ["Eq(3*1000, 3000)", "Eq(5000 + 3000, 8000)"]),
                tp("How many $500$ notes make $2\\,000$ togrog?",
                   ["$4$", "$2$", "$5$"],
                   "$4 \\times 500 = 2\\,000$ — every pair of $500$s trades for a $1\\,000$, and two pairs make two thousand.",
                   ["Eq(4*500, 2000)", "Eq(2*500, 1000)"]),
            ]),
            tapq("Paper against value", "Which purse holds more: three $1\\,000$ notes, or one $5\\,000$ note?",
                 ["the one $5\\,000$ note",
                  "the three $1\\,000$ notes — more paper",
                  "they are equal",
                  "it cannot be decided"],
                 "Count value, not paper: $3 \\times 1\\,000 = 3\\,000$, and $3\\,000 < 5\\,000$. The single note wins by $2\\,000$ togrog ($3\\,000 + 2\\,000 = 5\\,000$ ✓).",
                 ["Eq(3*1000, 3000)", "3000 < 5000", "Eq(3000 + 2000, 5000)"]),
            funfact("Shopkeepers count up, not down",
                    "Watch a market seller give change: she starts at the PRICE and counts upward, laying money in your palm until she reaches what you paid. No subtraction sum in sight — yet it cannot go wrong, because the pile in your hand plus the price adds up to your note. Counting up carries its own receipt."),
            withfig(teach("Concept B", "Change by counting up", [
                "Change is the climb from the price to what you paid. Price $%s$, paid $%s$: the line below climbs $800$, $900$, $1\\,000$ — three steps of $100$, so the change is $%s$ togrog." % (mny(price), mny(paid), mny(change)),
                "The receipt comes free: CHANGE + PRICE = PAID, here $%s + %s = %s$ ✓. If the sum misses, the change is wrong — no exceptions." % (mny(change), mny(price), mny(paid)),
                "Bigger gaps use bigger steps: price $3\\,200$, paid $5\\,000$ — up $800$ to $4\\,000$, then $1\\,000$ more: change $1\\,800$, and $1\\,800 + 3\\,200 = 5\\,000$ ✓.",
            ]), fig_countup),
            workedset("The counting-up till",
                      "Climb from price to payment; the climb IS the change.", [
                wex("Price $700$ togrog, paid with a $1\\,000$ note. Change?",
                    ["Climb: $800$, $900$, $1\\,000$ — three hundreds.",
                     "Change $300$ togrog. Receipt: $300 + 700 = 1\\,000$ ✓."],
                    "$300$ togrog",
                    ["Eq(3*100, 300)", "Eq(300 + 700, 1000)"]),
                wex("Price $3\\,200$ togrog, paid with a $5\\,000$ note. Change?",
                    ["Climb: $800$ reaches $4\\,000$; $1\\,000$ more reaches $5\\,000$.",
                     "Change $800 + 1\\,000 = 1\\,800$ togrog. Receipt: $1\\,800 + 3\\,200 = 5\\,000$ ✓."],
                    "$1\\,800$ togrog",
                    ["Eq(800 + 1000, 1800)", "Eq(1800 + 3200, 5000)"]),
            ]),
            tryitset("Climb to the note", "Count up, then receipt: change + price = paid.", [
                tp("Sweets cost $600$ togrog; you pay with a $1\\,000$ note. Change:",
                   ["$400$ togrog", "$600$ togrog", "$300$ togrog"],
                   "Climb from $600$ to $1\\,000$: four hundreds. Receipt: $400 + 600 = 1\\,000$ ✓. Answering $600$ hands back the price itself.",
                   ["Eq(400 + 600, 1000)"]),
                tp("A notebook costs $1\\,500$ togrog; you pay $2\\,000$. Change:",
                   ["$500$ togrog", "$1\\,500$ togrog", "$1\\,000$ togrog"],
                   "One step of $500$ climbs from $1\\,500$ to $2\\,000$. Receipt: $500 + 1\\,500 = 2\\,000$ ✓.",
                   ["Eq(500 + 1500, 2000)"]),
                tp("A toy costs $7\\,300$ togrog; you pay with a $10\\,000$ note. Change:",
                   ["$2\\,700$ togrog", "$3\\,700$ togrog", "$2\\,300$ togrog"],
                   "Climb: $700$ reaches $8\\,000$, then $2\\,000$ more reaches $10\\,000$ — change $700 + 2\\,000 = 2\\,700$. Receipt: $2\\,700 + 7\\,300 = 10\\,000$ ✓.",
                   ["Eq(700 + 2000, 2700)", "Eq(2700 + 7300, 10000)"]),
            ]),
            tapq("Receipt the change", "A bowl of airag costs $900$ togrog; you pay with a $1\\,000$ note. Your change is:",
                 ["$100$ togrog", "$900$ togrog", "$190$ togrog", "$1\\,000$ togrog"],
                 "One small step: from $900$ to $1\\,000$ is $100$. Receipt: $100 + 900 = 1\\,000$ ✓ — any other answer fails the add-back.",
                 ["Eq(100 + 900, 1000)"]),
            recap([
                "Purse totals: each note's value times its count, added up — value beats paper.",
                "Notes trade like units: two 500s make a 1000, five 1000s make a 5000.",
                "One amount can be made many ways with different notes.",
                "Change counts UP from the price to the payment.",
                "The receipt is law: change + price = paid, every time.",
            ]),
            tip("For every change question below, count up first, then say the receipt out loud — change plus price equals paid. If the receipt fails, climb again."),
            tryitset("Mixed practice", "Totals, trades, and change with receipts.", [
                tp("One $5\\,000$ note, four $1\\,000$ notes and one $500$ note make:",
                   ["$9\\,500$ togrog", "$5\\,900$ togrog", "$9\\,050$ togrog"],
                   "$5\\,000 + 4 \\times 1\\,000 + 500 = 5\\,000 + 4\\,000 + 500 = 9\\,500$ togrog. "
                   "The $9\\,050$ trap wrote the $500$ in the tens column instead of the hundreds.",
                   ["Eq(4*1000, 4000)", "Eq(5000 + 4000 + 500, 9500)",
                    "Eq(5000 + 4000 + 50, 9050)", "Ne(9050, 9500)"]),
                tp("How many $1\\,000$ notes make $10\\,000$ togrog?",
                   ["$10$", "$100$", "$5$"],
                   "$10 \\times 1\\,000 = 10\\,000$ — or two $5\\,000$ notes, since $2 \\times 5\\,000 = 10\\,000$ says the same value in less paper.",
                   ["Eq(10*1000, 10000)", "Eq(2*5000, 10000)"]),
                tp("A pencil costs $450$ togrog; you pay with a $500$ note. Change:",
                   ["$50$ togrog", "$150$ togrog", "$450$ togrog"],
                   "A short climb: from $450$ to $500$ is $50$. Receipt: $50 + 450 = 500$ ✓.",
                   ["Eq(50 + 450, 500)"]),
                tp("A khuushuur costs $800$ togrog and tea costs $400$. You pay for both with a $2\\,000$ note. Change:",
                   ["$800$ togrog", "$1\\,200$ togrog", "$600$ togrog"],
                   "Total first: $800 + 400 = 1\\,200$. Then climb from $1\\,200$ to $2\\,000$: $800$. Receipt: $800 + 1\\,200 = 2\\,000$ ✓.",
                   ["Eq(800 + 400, 1200)", "Eq(800 + 1200, 2000)"]),
                tp("A book costs $4\\,500$ togrog and a toy costs $5\\,000$. The toy costs more by:",
                   ["$500$ togrog", "$1\\,000$ togrog", "$4\\,500$ togrog"],
                   "Count up from $4\\,500$ to $5\\,000$: one step of $500$. Receipt: $4\\,500 + 500 = 5\\,000$ ✓.",
                   ["Eq(4500 + 500, 5000)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Counting Money\" — and the topic",
                    "Rulers, scales, jugs, clocks, calendars and purses — six faces of one idea: KNOW THE TRADE, then count. $100$ centimetres to the metre, $1\\,000$ grams to the kilogram, $60$ minutes to the hour, $7$ days to the week, and two $500$ notes to the thousand. Every measurement you will ever make starts with a trade like these.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    pa, pb = 3, 11
    plen = pb - pa
    fig_pr2 = fig_numline(
        [(0, "0"), (pa, "%d" % pa, C_WARM), (pb, "%d" % pb, C_GREEN),
         (15, "15")], lo=0, hi=15)
    return [
        prob("g4me-pr1", "Convert $8$ m to centimetres, and say which is longer: $8$ m or $750$ cm.",
             "Trade: $8 \\times 100 = 800$ cm. Then $800 > 750$ — the $8$ m is longer by $50$ cm, since $750 + 50 = 800$ ✓.",
             ["Eq(8*100, 800)", "800 > 750", "Eq(750 + 50, 800)"]),
        withfig(prob("g4me-pr2", "A pencil lies along a ruler from the $%d$ cm mark to the $%d$ cm mark. How long is the pencil?" % (pa, pb),
             "Mark to mark: $%d - %d = %d$ cm. Add back: $%d + %d = %d$ ✓." % (pb, pa, plen, plen, pa, pb),
             ["Eq(%d + %d, %d)" % (plen, pa, pb)]), fig_pr2),
        prob("g4me-pr3", "Convert $7$ kg to grams, and $2\\,000$ g to kilograms.",
             "Big to small: $7 \\times 1\\,000 = 7\\,000$ g. Small to big: $2\\,000 \\div 1\\,000 = 2$ kg, receipt $2 \\times 1\\,000 = 2\\,000$ ✓.",
             ["Eq(7*1000, 7000)", "Eq(Rational(2000,1000), 2)", "Eq(2*1000, 2000)"]),
        prob("g4me-pr4", "Which holds more: a pot of $1$ l $300$ ml, or a bottle of $1\\,250$ ml?",
             "Trade the pot: $1\\,000 + 300 = 1\\,300$ ml. Then $1\\,250 < 1\\,300$ — the pot wins by $50$ ml, since $1\\,250 + 50 = 1\\,300$ ✓.",
             ["Eq(1000 + 300, 1300)", "1250 < 1300", "Eq(1250 + 50, 1300)"]),
        prob("g4me-pr5", "Write \"quarter to $6$\" in digits, and say where the minute hand points.",
             "Quarter to $6$ is $15$ minutes before $6$:$00$, so the hour showing is $5$ with $3 \\times 15 = 45$ minutes past: $5$:$45$, minute hand at the $9$. Check: $45 + 15 = 60$ ✓.",
             ["Eq(3*15, 45)", "Eq(45 + 15, 60)", "Eq(Rational(60,4), 15)"]),
        prob("g4me-pr6", "A pony trek lasts $3$ weeks and $4$ days. How many days is that in all?",
             "Trade the weeks: $3 \\times 7 = 21$ days, plus the $4$ loose days: $21 + 4 = 25$ days. Receipt: $3 \\times 7 + 4 = 25$ with $4 < 7$ ✓.",
             ["Eq(3*7, 21)", "Eq(3*7 + 4, 25)", "4 < 7"]),
        prob("g4me-pr7", "Choir practice runs from $4$:$50$ to $5$:$30$. How long is it?",
             "Step through the round hour: $10$ minutes reach $5$:$00$, then $30$ more — $10 + 30 = 40$ minutes. Receipt in minutes: $4$:$50$ is $4 \\times 60 + 50 = 290$, and $290 + 40 = 330$, which is $5$:$30$ ✓.",
             ["Eq(10 + 30, 40)", "Eq(4*60 + 50, 290)", "Eq(290 + 40, 330)"]),
        prob("g4me-pr8", "A deel costs $6\\,400$ togrog and you pay with a $10\\,000$ note. Find the change by counting up.",
             "Climb: $600$ reaches $7\\,000$, then $3\\,000$ more reaches $10\\,000$ — change $600 + 3\\,000 = 3\\,600$ togrog. Receipt: $3\\,600 + 6\\,400 = 10\\,000$ ✓.",
             ["Eq(600 + 3000, 3600)", "Eq(3600 + 6400, 10000)"]),
    ]


def test_bank():
    return [
        prob("g4me-x1", "Convert $600$ cm to metres and $4$ m to centimetres. Then say which is longer: $4$ m or $380$ cm.",
             "$600 \\div 100 = 6$ m (receipt $6 \\times 100 = 600$ ✓) and $4 \\times 100 = 400$ cm. Comparing: $380 < 400$, so the $4$ m is longer.",
             ["Eq(Rational(600,100), 6)", "Eq(6*100, 600)", "Eq(4*100, 400)", "380 < 400"]),
        prob("g4me-x2", "Which is heavier: $3$ kg or $2\\,800$ g? Which holds more: $2$ l or $2\\,200$ ml?",
             "Mass: $3$ kg $= 3\\,000$ g and $2\\,800 < 3\\,000$ — the $3$ kg wins. Capacity: $2$ l $= 2\\,000$ ml and $2\\,200 > 2\\,000$ — the $2\\,200$ ml wins. Trade first, compare second, both times.",
             ["Eq(3*1000, 3000)", "2800 < 3000", "Eq(2*1000, 2000)", "2200 > 2000"]),
        prob("g4me-x3", "The minute hand points at $9$ and the hour hand sits just before $8$. What time is it, in words and in digits?",
             "Minute hand at $9$: three quarter-laps done, $3 \\times 15 = 45$ minutes past. The hour hand has nearly finished hour $7$: the time is $7$:$45$ — quarter to $8$, since $45 + 15 = 60$ ✓.",
             ["Eq(3*15, 45)", "Eq(45 + 15, 60)"]),
        prob("g4me-x4", "How many days are in a leap year? And how many full weeks are in $35$ days?",
             "A leap year adds one day to $365$: $365 + 1 = 366$ days. Weeks: $35 \\div 7 = 5$, receipt $5 \\times 7 = 35$ ✓.",
             ["Eq(365 + 1, 366)", "Eq(Rational(35,7), 5)", "Eq(5*7, 35)"]),
        prob("g4me-x5", "A concert starts at $7$:$15$ and lasts $45$ minutes. When does it end?",
             "In minutes: $7$:$15$ is $7 \\times 60 + 15 = 435$. Add the length: $435 + 45 = 480$, which is $8 \\times 60$ — exactly $8$:$00$. The quarters agree: $15 + 45 = 60$, one whole hour's worth of minutes closed.",
             ["Eq(7*60 + 15, 435)", "Eq(435 + 45, 480)", "Eq(8*60, 480)", "Eq(15 + 45, 60)"]),
        prob("g4me-x6", "Fabric for a deel costs $7\\,500$ togrog and you pay with a $10\\,000$ note. Find the change by counting up, and say which notes the seller could hand you.",
             "Climb: $500$ reaches $8\\,000$, then $2\\,000$ more reaches $10\\,000$ — change $500 + 2\\,000 = 2\\,500$ togrog. Receipt: $2\\,500 + 7\\,500 = 10\\,000$ ✓. The seller could hand you two $1\\,000$ notes and one $500$ note: $2 \\times 1\\,000 + 500 = 2\\,500$ ✓.",
             ["Eq(500 + 2000, 2500)", "Eq(2500 + 7500, 10000)", "Eq(2*1000 + 500, 2500)"]),
    ]


def main():
    topic = {
        "slug": "measurement-time-and-money",
        "title": "Measurement, Time & Money",
        "grade": 4,
        "status": "published",
        "blurb": ("Centimetres and metres, grams and kilograms, litres and "
                  "millilitres, reading the clock to the quarter hour, the "
                  "calendar, and counting togrog and making change."),
        "lessons": [
            lesson_length(),
            lesson_mass_capacity(),
            lesson_clock(),
            lesson_calendar(),
            lesson_money(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "measurement-time-and-money.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
