#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Measuring, Time & Money.

Measuring length in centimetres with a ruler that must start at zero;
metres for the lengths a ruler cannot reach, and comparing two lengths
in the same unit; heavier, lighter and holds-more, with kilograms and
litres as the units for saying how much; telling the time to o'clock and
half past on a real clock face; and counting tögrög notes to find a
total and the change.

Through-line: A MEASUREMENT IS A COUNT OF UNITS. The number means
nothing without the unit beside it, two measurements can only be
compared in the same unit, and every one of these skills is counting
something you have chosen to count in.

Grade discipline: centimetres and metres, kilograms and litres — no
millilitres, no gram/kilogram trading and no unit conversion beyond "a
metre is 100 cm" (Grade 4 owns the 1000-trades). The clock goes to
o'clock and half past only; quarter past, quarter to and the calendar
are Grade 4's. Money totals stay under 1000 tögrög. Every check is
sympy-asserted BEFORE the JSON is written, and the clock hands are
computed from the same hour and minute the statement quotes.

Run: python3 scripts/grade2/build_measuring_time_and_money.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, withprobfig, workedset,
                     write_topic, clock, coins, fig_groups, fig_numline,
                     C_ACCENT, C_WARM, C_GREEN)


def ruler(marks, lo=0, hi=10, highlight=None):
    """A centimetre ruler as a number line, with the measured span's ends
    called out. `marks` are the cm values to label."""
    pts = []
    for m in marks:
        color = C_WARM if highlight and m in highlight else None
        pts.append((m, "%d cm" % m, color) if color else (m, "%d cm" % m))
    return fig_numline(pts, lo=lo, hi=hi)


# ==========================================================================
# Lesson 1 — Measuring in Centimetres
# ==========================================================================

def lesson_centimetres():
    fig_from0 = ruler([0, 4, 8], lo=0, hi=10, highlight=[0, 8])
    fig_offset = ruler([2, 5, 9], lo=0, hi=10, highlight=[2, 9])
    fig_pencil = ruler([0, 6], lo=0, hi=10, highlight=[0, 6])
    return {
        "slug": "measuring-in-centimetres",
        "title": "Measuring in Centimetres",
        "concreteComparison": (
            "Two children measure the same pencil and get different "
            "answers. One started at the $0$ on the ruler; the other "
            "started at the metal edge, a little before the $0$. The "
            "pencil never changed — the counting did."),
        "objective": (
            "Measure a length in centimetres with a ruler, start the "
            "count in the right place, and read a length whose ends do "
            "not sit at zero."),
        "concept": [
            "**A centimetre is the unit you are counting.** Measuring "
            "means asking how many centimetres fit along the object. The "
            "answer is a number AND a unit — \"$8$\" alone says nothing, "
            "\"$8$ cm\" says everything.",
            "**Line the object up with the ZERO, not the end of the "
            "ruler.** Most rulers have a little blank strip before the "
            "$0$. Start from the ruler's edge and every measurement comes "
            "out too big.",
            "**If the object does not start at zero, subtract.** A stick "
            "lying from the $2$ cm mark to the $9$ cm mark is not $9$ cm "
            "long. It covers $9 - 2 = 7$ centimetres — count the marks "
            "the object actually spans.",
        ],
        "keyIdea": (
            "A length is a count of centimetres, so start the count at "
            "zero — and when the object starts elsewhere, subtract to "
            "find how many centimetres it really covers."),
        "facts": [
            {"title": "Start at zero",
             "latex": "8 - 0 = 8",
             "explanation": "An object laid from 0 to 8 covers 8 centimetres."},
            {"title": "Subtract when it does not",
             "latex": "9 - 2 = 7",
             "explanation": "From the 2 cm mark to the 9 cm mark is 7 centimetres, not 9."},
        ],
        "workedExamples": [
            {"id": "g3me-l1-we1",
             "statement": "A pencil is laid on a ruler from the $0$ mark to the $8$ cm mark. How long is it?",
             "note": "Count the centimetres it covers.",
             "solution": ("Starting at zero, the pencil covers every centimetre "
                          "up to $8$: $8 - 0 = 8$, so it is $8$ cm long. Note "
                          "the unit — \"$8$\" on its own would not say whether "
                          "we meant centimetres, metres or steps."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8 - 0, 8)"]},
            {"id": "g3me-l1-we2",
             "statement": "A stick lies along a ruler from the $2$ cm mark to the $9$ cm mark. How long is it?",
             "note": "It does not start at zero.",
             "solution": ("The stick covers the centimetres from $2$ up to $9$, "
                          "which is $9 - 2 = 7$ of them. So it is $7$ cm long — "
                          "not $9$ cm, which would be the answer only if it had "
                          "started at zero."),
             "badges": [{"text": "core"}],
             "check": ["Eq(9 - 2, 7)", "Ne(7, 9)"]},
        ],
        "commonMistakes": [
            {"text": "Reading off the mark at the far end when the object did not start at zero — calling the 2-to-9 stick 9 cm.",
             "correction": "That reads the ruler's position, not the object's length. Subtract: 9 − 2 = 7 cm is how many centimetres the stick actually covers.",
             "authored": True},
            {"text": "Starting the measurement at the ruler's metal edge instead of the 0 mark.",
             "correction": "Most rulers have a blank strip before the 0. Starting there adds that strip to every measurement, so line the object up with the printed 0 every time.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3me-l1-t1",
             "statement": "A ribbon lies from the $0$ mark to the $6$ cm mark. How long is it?",
             "solution": ("It covers all six centimetres from zero: "
                          "$6 - 0 = 6$, so the ribbon is $6$ cm long."),
             "check": ["Eq(6 - 0, 6)"]},
            {"id": "g3me-l1-t2",
             "statement": "A twig lies from the $3$ cm mark to the $10$ cm mark. How long is it?",
             "solution": ("$10 - 3 = 7$, so the twig is $7$ cm long. Reading "
                          "only the far end would give $10$ cm, which is $3$ cm "
                          "too much."),
             "check": ["Eq(10 - 3, 7)", "Eq(10 - 7, 3)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counting centimetres from zero", [
                "The ruler below shows an object laid from the $0$ mark to the $8$ cm mark.",
                "Measuring is counting: how many centimetres fit along the object? Starting from zero, the answer is read straight off — $8 - 0 = 8$, so $8$ cm.",
                "Always say the unit. \"$8$\" could be centimetres, metres or paces; \"$8$ cm\" is a measurement, and a number without its unit is not one.",
            ]), fig_from0),
            workedset("Measure from zero", "Line the object up with the $0$ mark.", [
                wex("A pencil lies from $0$ to $8$ cm. How long is it?",
                    ["It starts at zero, so read the far end.",
                     "$8 - 0 = 8$: the pencil is $8$ cm long."],
                    "$8$ cm",
                    ["Eq(8 - 0, 8)"]),
                wex("A ribbon lies from $0$ to $6$ cm. How long is it?",
                    ["Again it starts at zero.",
                     "$6 - 0 = 6$: the ribbon is $6$ cm long."],
                    "$6$ cm",
                    ["Eq(6 - 0, 6)"]),
            ]),
            tryitset("Read the ruler", "Where does the object start?", [
                withfig(tp("The object below runs from $0$ to $6$ cm. It is:",
                   ["$6$ cm long", "$0$ cm long", "$60$ cm long"],
                   "Starting at zero, the far end gives the length directly: $6 - 0 = 6$ cm.",
                   ["Eq(6 - 0, 6)"]), fig_pencil),
                tp("A measurement written as just \"$7$\" is:",
                   ["incomplete — it needs a unit",
                    "$7$ centimetres", "$7$ metres"],
                   "A number alone does not say what was counted. Seven centimetres and seven metres are wildly different lengths, and $7$ says neither.",
                   ["Eq(7 - 0, 7)"]),
                tp("Starting a measurement at the ruler's metal edge instead of the $0$ makes every answer:",
                   ["too big", "too small", "exactly right"],
                   "The blank strip before the $0$ gets counted as part of the object, so every length comes out longer than it really is.",
                   ["Eq(8 - 0, 8)"]),
            ]),
            tapq("Where does the count start?", "Why must you line an object up with the $0$ and not the ruler's edge?",
                 ["the blank strip before $0$ would be counted too",
                  "because the edge is made of metal",
                  "it makes no difference which you use",
                  "because rulers start at $1$"],
                 "Most rulers have a small blank strip before the printed $0$. Starting there adds it to every measurement, making each one too long — whereas from the $0$ mark, an object reaching $8$ is exactly $8 - 0 = 8$ cm.",
                 ["Eq(8 - 0, 8)"]),
            funfact("Why the centimetre is the size it is",
                    "A centimetre is one hundredth of a metre, and the metre was first defined so that the distance from the equator to the North Pole would be exactly ten million of them. Almost nobody has ever needed that fact — but it is why a centimetre is a comfortable size for a fingernail and a metre for a stride."),
            withfig(teach("Concept B", "When the object does not start at zero", [
                "Objects do not always begin at the $0$ mark. The ruler below shows one lying from the $2$ cm mark to the $9$ cm mark.",
                "It is not $9$ cm long. Read the ruler as a count: the object covers the centimetres from $2$ up to $9$, which is $9 - 2 = 7$ of them.",
                "So subtract the starting mark from the finishing one. And check the answer makes sense — $7$ cm must be shorter than the $9$ cm mark it reaches, which it is.",
            ]), fig_offset),
            workedset("Subtract the start",
                      "Finishing mark minus starting mark.", [
                wex("A stick lies from $2$ cm to $9$ cm. How long is it?",
                    ["It covers the centimetres from $2$ to $9$.",
                     "$9 - 2 = 7$, so the stick is $7$ cm long."],
                    "$7$ cm",
                    ["Eq(9 - 2, 7)", "Eq(7 + 2, 9)"]),
                wex("A twig lies from $3$ cm to $10$ cm. How long is it?",
                    ["$10 - 3 = 7$.",
                     "The twig is $7$ cm long — the same length as the stick above, in a different place on the ruler."],
                    "$7$ cm",
                    ["Eq(10 - 3, 7)", "Eq(7 + 3, 10)"]),
            ]),
            tryitset("Not starting at zero", "Take the starting mark away.", [
                withfig(tp("The object below runs from the $2$ cm mark to the $9$ cm mark. It is:",
                   ["$7$ cm long", "$9$ cm long", "$11$ cm long"],
                   "It covers $9 - 2 = 7$ centimetres. Reading only the far end gives $9$, and adding the marks gives $11$ — neither counts the object.",
                   ["Eq(9 - 2, 7)", "Eq(9 + 2, 11)"]), fig_offset),
                tp("A ribbon runs from the $4$ cm mark to the $10$ cm mark. It is:",
                   ["$6$ cm long", "$10$ cm long", "$14$ cm long"],
                   "$10 - 4 = 6$ centimetres covered. The receipt confirms it: $6 + 4 = 10$ ✓.",
                   ["Eq(10 - 4, 6)", "Eq(6 + 4, 10)"]),
                tp("Two sticks measure $2$ to $7$ cm and $0$ to $5$ cm. They are:",
                   ["the same length", "different lengths",
                    "impossible to compare"],
                   "The first covers $7 - 2 = 5$ cm and the second $5 - 0 = 5$ cm — both $5$ cm, just lying in different places on the ruler.",
                   ["Eq(7 - 2, 5)", "Eq(5 - 0, 5)"]),
            ]),
            tapq("Position against length", "A pencil lies from the $3$ cm mark to the $9$ cm mark. How long is it?",
                 ["$6$ cm", "$9$ cm", "$12$ cm", "$3$ cm"],
                 "The pencil covers the centimetres from $3$ up to $9$: $9 - 3 = 6$ cm. The $9$ is where the pencil ENDS on the ruler, not how long it is — receipt: $6 + 3 = 9$ ✓.",
                 ["Eq(9 - 3, 6)", "Eq(6 + 3, 9)"]),
            recap([
                "Measuring is counting units — and the unit must be said, not just the number.",
                "Line the object up with the printed $0$, never the ruler's edge.",
                "If it starts elsewhere, subtract: from $2$ cm to $9$ cm is $9 - 2 = 7$ cm.",
                "Two objects of the same length can sit at quite different places on the ruler.",
            ]),
            tip("Before reading any ruler, put your finger on the $0$ and check the object's end is there. Almost every wrong measurement in this lesson comes from a start that was never checked."),
            tryitset("Chapter practice", "Where does it start, and where does it end?", [
                tp("An object from $0$ to $9$ cm is:",
                   ["$9$ cm long", "$0$ cm long", "$90$ cm long"],
                   "Starting at zero, the far mark IS the length: $9 - 0 = 9$ cm.",
                   ["Eq(9 - 0, 9)"]),
                tp("An object from $5$ cm to $8$ cm is:",
                   ["$3$ cm long", "$8$ cm long", "$13$ cm long"],
                   "$8 - 5 = 3$ centimetres covered; the receipt $3 + 5 = 8$ ✓ confirms it.",
                   ["Eq(8 - 5, 3)", "Eq(3 + 5, 8)"]),
                tp("Which measurement is written properly?",
                   ["$12$ cm", "$12$", "cm"],
                   "A measurement is a number AND a unit. Either one alone leaves the reader guessing what was counted.",
                   ["Eq(12 - 0, 12)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Measuring in Centimetres\"",
                    "You can now measure anything that fits on a ruler. The next lesson deals with the things that do not — and finds that the answer is simply a bigger unit.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Metres and Comparing
# ==========================================================================

def lesson_metres():
    fig_m = fig_groups((10, "10 cm", C_ACCENT), (10, "20 cm", C_ACCENT),
                       (10, "30 cm", C_ACCENT))
    fig_cmp = fig_numline([(0, "0"), (45, "ribbon: 45 cm"),
                           (80, "rope: 80 cm"), (100, "1 m")], lo=0, hi=100)
    return {
        "slug": "metres-and-comparing",
        "title": "Metres & Comparing Lengths",
        "concreteComparison": (
            "Measuring a ger with a $30$ cm ruler would take all "
            "afternoon. For long things there is a bigger unit — the "
            "metre, which is $100$ centimetres — and a doorway is about "
            "two of them."),
        "objective": (
            "Choose between centimetres and metres for a given object, "
            "use the fact that a metre is $100$ cm, and compare two "
            "lengths given in the same unit."),
        "concept": [
            "**A metre is one hundred centimetres.** It is the unit for things "
            "a ruler cannot reach: a room, a rope, the height of a door. "
            "One metre is about a long stride.",
            "**Choose the unit to fit the object.** A pencil in metres "
            "would be a fraction of one; a ger in centimetres would be "
            "hundreds. Pick the unit that gives a comfortable, countable "
            "number — that is the whole art of choosing a unit.",
            "**Compare only in the SAME unit.** A ribbon of $45$ cm and a "
            "rope of $80$ cm compare directly: $80 > 45$, so the rope is "
            "$80 - 45 = 35$ cm longer. Comparing $45$ cm with \"$2$\" is "
            "meaningless until you know what the $2$ counts.",
        ],
        "keyIdea": (
            "A metre is $100$ centimetres; choose whichever unit gives a "
            "comfortable number, and only ever compare two lengths that "
            "are counted in the same one."),
        "facts": [
            {"title": "A metre in centimetres",
             "latex": "1 \\times 100 = 100",
             "explanation": "One metre is 100 centimetres — the unit for long things."},
            {"title": "Compare in one unit",
             "latex": "80 - 45 = 35",
             "explanation": "A rope of 80 cm is 35 cm longer than a ribbon of 45 cm."},
        ],
        "workedExamples": [
            {"id": "g3me-l2-we1",
             "statement": "Would you measure a pencil in centimetres or metres? And a ger?",
             "note": "Which gives a comfortable number?",
             "solution": ("A pencil in centimetres — perhaps $18$ cm, a "
                          "comfortable number. In metres it would be less than "
                          "one whole metre, which is awkward to say. A ger is "
                          "the other way round: in metres it might be $5$ m, "
                          "while in centimetres that is $5 \\times 100 = 500$ "
                          "cm, a big number to carry about."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*100, 500)", "Eq(1*100, 100)"]},
            {"id": "g3me-l2-we2",
             "statement": "A ribbon is $45$ cm and a rope is $80$ cm. Which is longer, and by how much?",
             "note": "Same unit, so compare directly.",
             "solution": ("Both are in centimetres, so they compare straight "
                          "away: $80 > 45$, so the rope is longer, by "
                          "$80 - 45 = 35$ cm. Receipt: $35 + 45 = 80$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["80 > 45", "Eq(80 - 45, 35)", "Eq(35 + 45, 80)"]},
        ],
        "commonMistakes": [
            {"text": "Comparing a length in centimetres with one in metres as if the numbers meant the same thing.",
             "correction": "2 m is far longer than 45 cm, even though 45 is the bigger number — because a metre is 100 cm, and 2 m is 200 cm. Put both into one unit before comparing.",
             "authored": True},
            {"text": "Measuring long things in centimetres out of habit, giving numbers like 500 cm for a ger.",
             "correction": "That is not wrong, but it is uncomfortable. 500 cm is 5 m, and the smaller number is easier to say, remember and check.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3me-l2-t1",
             "statement": "How many centimetres are there in $3$ metres?",
             "solution": ("Each metre is $100$ cm, so three of them is "
                          "$3 \\times 100 = 300$ cm."),
             "check": ["Eq(3*100, 300)"]},
            {"id": "g3me-l2-t2",
             "statement": "A stick is $60$ cm and a pole is $90$ cm. How much longer is the pole?",
             "solution": ("Both in centimetres, so subtract: $90 - 60 = 30$ cm "
                          "longer. Receipt: $30 + 60 = 90$ ✓."),
             "check": ["Eq(90 - 60, 30)", "Eq(30 + 60, 90)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "A bigger unit for bigger things", [
                "A ruler runs out quickly. For a rope, a room or a doorway there is a bigger unit: the metre.",
                "One metre is $100$ centimetres — the picture below counts three lots of ten to give you a feel for how the centimetres stack up. A metre is about one long stride.",
                "So $3$ metres is $3 \\times 100 = 300$ cm. The length has not changed; only the unit you count it in has.",
            ]), fig_m),
            workedset("Metres and centimetres",
                      "One metre is one hundred centimetres.", [
                wex("How many centimetres in $3$ metres?",
                    ["Each metre is $100$ cm.",
                     "$3 \\times 100 = 300$ cm."],
                    "$300$ cm",
                    ["Eq(3*100, 300)"]),
                wex("A ger is about $5$ m across. How many centimetres is that?",
                    ["$5$ metres, each of $100$ cm.",
                     "$5 \\times 100 = 500$ cm — which is why metres are the friendlier unit here."],
                    "$500$ cm",
                    ["Eq(5*100, 500)", "500 > 5"]),
            ]),
            tryitset("Which unit?", "Pick the one that gives a comfortable number.", [
                tp("You would measure a pencil in:",
                   ["centimetres", "metres", "either — it makes no difference"],
                   "A pencil is about $18$ cm, a comfortable number. In metres it would not even reach one whole metre.",
                   ["Eq(1*100, 100)", "100 > 18"]),
                tp("$2$ metres is the same as:",
                   ["$200$ cm", "$20$ cm", "$2$ cm"],
                   "Each metre is $100$ cm, so $2 \\times 100 = 200$ cm.",
                   ["Eq(2*100, 200)"]),
                tp("You would measure the height of a door in:",
                   ["metres", "centimetres", "neither"],
                   "A door is about $2$ m. Measuring it in centimetres gives $200$ — correct, but a bigger number to carry about for no benefit.",
                   ["Eq(2*100, 200)", "200 > 2"]),
            ]),
            tapq("How many centimetres?", "A rope is $4$ metres long. In centimetres that is:",
                 ["$400$ cm", "$40$ cm", "$104$ cm", "$4$ cm"],
                 "Each metre is $100$ centimetres, so four metres is $4 \\times 100 = 400$ cm. The rope has not changed length — only the unit counting it.",
                 ["Eq(4*100, 400)"]),
            funfact("The metre that lived in a vault",
                    "For most of a century, the metre was a particular metal bar kept in a vault near Paris, and every ruler in the world was ultimately a copy of it. That stopped a few decades ago: the metre is now defined by how far light travels in a fixed sliver of a second, which nobody can lose, bend or steal."),
            withfig(teach("Concept B", "Comparing lengths", [
                "The line below shows a ribbon of $45$ cm and a rope of $80$ cm against a full metre.",
                "Both are measured in centimetres, so they compare directly: $80 > 45$, and the rope is $80 - 45 = 35$ cm longer.",
                "But comparing only works in ONE unit. A rope of \"$2$\" and a ribbon of \"$45$ cm\" cannot be ranked until you know what the $2$ counts — if it is metres, that rope is $200$ cm and far the longer.",
            ]), fig_cmp),
            workedset("Compare fairly", "Get both lengths into the same unit.", [
                wex("A ribbon is $45$ cm and a rope is $80$ cm. Which is longer, and by how much?",
                    ["Same unit, so compare directly: $80 > 45$.",
                     "$80 - 45 = 35$ cm longer; receipt $35 + 45 = 80$ ✓."],
                    "the rope, by $35$ cm",
                    ["80 > 45", "Eq(80 - 45, 35)", "Eq(35 + 45, 80)"]),
                wex("A rope is $2$ m and a ribbon is $45$ cm. Which is longer?",
                    ["Different units — put them into one.",
                     "$2$ m is $2 \\times 100 = 200$ cm.",
                     "$200 > 45$, so the rope is longer, by $200 - 45 = 155$ cm."],
                    "the rope",
                    ["Eq(2*100, 200)", "200 > 45", "Eq(200 - 45, 155)"]),
            ]),
            tryitset("Which is longer?", "Same unit first, then compare.", [
                tp("A stick of $70$ cm and a pole of $95$ cm: the pole is longer by:",
                   ["$25$ cm", "$165$ cm", "$35$ cm"],
                   "$95 - 70 = 25$ cm. Adding the two would give $165$, which answers a question nobody asked.",
                   ["Eq(95 - 70, 25)", "Eq(25 + 70, 95)"]),
                tp("Which is longer, $1$ m or $80$ cm?",
                   ["$1$ m", "$80$ cm", "they are equal"],
                   "One metre is $100$ cm, and $100 > 80$ — so the metre wins by $100 - 80 = 20$ cm, even though $80$ is the bigger-looking number.",
                   ["Eq(1*100, 100)", "100 > 80", "Eq(100 - 80, 20)"]),
                tp("Before comparing $3$ m with $250$ cm you should:",
                   ["put both into the same unit",
                    "compare the numbers $3$ and $250$",
                    "measure them again"],
                   "$3$ m is $3 \\times 100 = 300$ cm, and $300 > 250$ — so the three metres is longer, by $50$ cm. Comparing $3$ with $250$ would give the wrong answer entirely.",
                   ["Eq(3*100, 300)", "300 > 250", "Eq(300 - 250, 50)"]),
            ]),
            tapq("The bigger number that is shorter", "Which is longer, $2$ m or $150$ cm?",
                 ["$2$ m", "$150$ cm", "they are the same",
                  "you cannot compare them"],
                 "Put both in one unit: $2$ m is $2 \\times 100 = 200$ cm, and $200 > 150$. So the two metres is longer by $50$ cm, even though $150$ looks like the bigger number.",
                 ["Eq(2*100, 200)", "200 > 150", "Eq(200 - 150, 50)"]),
            recap([
                "A metre is $100$ centimetres — the unit for ropes, rooms and doorways.",
                "Choose the unit that gives a comfortable number: pencils in cm, gers in m.",
                "Two lengths can only be compared in the SAME unit.",
                "$2$ m beats $150$ cm, because $2$ m is $200$ cm — the bigger number is not always the longer thing.",
            ]),
            tip("Whenever two lengths carry different units, write both in centimetres before you compare a single digit. It takes one multiplication and it removes the only real trap in this lesson."),
            tryitset("Chapter practice", "Same unit, then compare.", [
                tp("$5$ metres in centimetres is:",
                   ["$500$ cm", "$50$ cm", "$105$ cm"],
                   "Each metre is $100$ cm: $5 \\times 100 = 500$ cm.",
                   ["Eq(5*100, 500)"]),
                tp("A rope of $90$ cm and a rope of $1$ m. The longer is:",
                   ["the $1$ m rope", "the $90$ cm rope", "they are equal"],
                   "One metre is $100$ cm, and $100 > 90$ — longer by $10$ cm.",
                   ["Eq(1*100, 100)", "Eq(100 - 90, 10)"]),
                tp("You would measure the length of a classroom in:",
                   ["metres", "centimetres", "neither"],
                   "A classroom is several metres across. In centimetres the number would run into the hundreds for no benefit.",
                   ["Eq(5*100, 500)", "500 > 5"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Metres & Comparing Lengths\"",
                    "Choosing a unit and comparing within it is the habit behind every measurement you will ever make. The next lesson applies it to two new questions: how heavy, and how much does it hold.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Heavier, Lighter, Holds More
# ==========================================================================

def lesson_mass_capacity():
    fig_balance = fig_groups((5, "left pan: 5 kg", C_ACCENT),
                             (3, "right pan: 3 kg", C_WARM))
    fig_jugs = fig_groups((4, "jug A: 4 litres", C_GREEN),
                          (6, "jug B: 6 litres", C_ACCENT))
    fig_same = fig_groups((2, "big box: 2 kg", C_WARM),
                          (7, "small box: 7 kg", C_ACCENT))
    return {
        "slug": "heavier-lighter-holds-more",
        "title": "Heavier, Lighter, Holds More",
        "concreteComparison": (
            "A big bag of wool and a small bag of salt sit on the "
            "counter. The big one looks heavier, but lift them and the "
            "salt wins. Size and weight are different questions, and only "
            "a balance settles the second one."),
        "objective": (
            "Compare masses with a balance and capacities by filling, use "
            "kilograms and litres to say how much, and explain why size "
            "does not decide weight."),
        "concept": [
            "**A balance compares two masses directly.** Put one thing in "
            "each pan: the heavier side goes down. If a $5$ kg sack sinks "
            "against a $3$ kg one, it is heavier by $5 - 3 = 2$ kg.",
            "**Capacity is how much a container holds.** A jug that takes "
            "$6$ litres holds more than one that takes $4$: "
            "$6 - 4 = 2$ litres more. You find out by filling, not by "
            "looking.",
            "**Size does not decide weight.** A big box of wool can be "
            "lighter than a small box of salt — $2$ kg against $7$ kg. "
            "How much room something takes up and how heavy it is are two "
            "separate measurements, and only weighing answers the second.",
        ],
        "keyIdea": (
            "Mass is measured in kilograms with a balance and capacity in "
            "litres by filling — and neither can be judged by how big "
            "something looks."),
        "facts": [
            {"title": "Comparing masses",
             "latex": "5 - 3 = 2",
             "explanation": "A 5 kg sack is 2 kg heavier than a 3 kg one."},
            {"title": "Comparing capacities",
             "latex": "6 - 4 = 2",
             "explanation": "A 6-litre jug holds 2 litres more than a 4-litre one."},
        ],
        "workedExamples": [
            {"id": "g3me-l3-we1",
             "statement": "A sack of $5$ kg is balanced against one of $3$ kg. Which pan goes down, and by how much is it heavier?",
             "note": "The heavier side sinks.",
             "solution": ("The $5$ kg pan goes down, because $5 > 3$. It is "
                          "heavier by $5 - 3 = 2$ kg — and adding $2$ kg to the "
                          "lighter pan would level the balance: "
                          "$3 + 2 = 5$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["5 > 3", "Eq(5 - 3, 2)", "Eq(3 + 2, 5)"]},
            {"id": "g3me-l3-we2",
             "statement": "A big box of wool weighs $2$ kg and a small box of salt weighs $7$ kg. Which is heavier, and what does that show?",
             "note": "Compare the masses, not the sizes.",
             "solution": ("The salt, by $7 - 2 = 5$ kg — even though its box is "
                          "the smaller of the two. Size and weight are separate "
                          "measurements: how much room a thing takes up says "
                          "nothing about how heavy it is."),
             "badges": [{"text": "core"}],
             "check": ["7 > 2", "Eq(7 - 2, 5)", "Eq(2 + 5, 7)"]},
        ],
        "commonMistakes": [
            {"text": "Deciding the bigger object must be the heavier one.",
             "correction": "A big box of wool can weigh 2 kg while a small box of salt weighs 7 kg. Size is one measurement and mass is another — only a balance settles the second.",
             "authored": True},
            {"text": "Giving a mass or a capacity as a bare number, with no unit.",
             "correction": "\"5\" could be kilograms, litres or sacks. Always say 5 kg or 5 litres — the unit is half the measurement.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3me-l3-t1",
             "statement": "A jug holds $8$ litres and a bucket holds $5$. How much more does the jug hold?",
             "solution": ("$8 - 5 = 3$ litres more. Receipt: "
                          "$5 + 3 = 8$ ✓."),
             "check": ["Eq(8 - 5, 3)", "Eq(5 + 3, 8)"]},
            {"id": "g3me-l3-t2",
             "statement": "Two sacks weigh $9$ kg and $4$ kg. Which pan of a balance goes down, and by how much?",
             "solution": ("The $9$ kg pan, since $9 > 4$. It is heavier by "
                          "$9 - 4 = 5$ kg."),
             "check": ["9 > 4", "Eq(9 - 4, 5)", "Eq(4 + 5, 9)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The balance settles it", [
                "A balance answers one question and answers it honestly: which of these two is heavier? Put one thing in each pan and the heavier side goes down.",
                "The picture below shows $5$ kg against $3$ kg. The left pan sinks, because $5 > 3$, and it is heavier by $5 - 3 = 2$ kg.",
                "The kilogram is the unit for saying HOW heavy. Without it, \"$5$\" could mean anything — five kilograms, five sacks, five stones.",
            ]), fig_balance),
            workedset("Compare two masses", "The heavier pan goes down.", [
                wex("Which pan goes down: $5$ kg or $3$ kg? By how much?",
                    ["$5 > 3$, so the $5$ kg pan sinks.",
                     "It is heavier by $5 - 3 = 2$ kg; adding $2$ kg to the other pan would level it."],
                    "the $5$ kg pan, by $2$ kg",
                    ["5 > 3", "Eq(5 - 3, 2)", "Eq(3 + 2, 5)"]),
                wex("Two sacks weigh $9$ kg and $4$ kg. Compare them.",
                    ["$9 > 4$, so the $9$ kg sack is heavier.",
                     "By $9 - 4 = 5$ kg."],
                    "$5$ kg heavier",
                    ["9 > 4", "Eq(9 - 4, 5)", "Eq(4 + 5, 9)"]),
            ]),
            tryitset("Which is heavier?", "Compare the masses, in kilograms.", [
                tp("A $7$ kg sack and a $4$ kg sack. The heavier is:",
                   ["the $7$ kg sack, by $3$ kg",
                    "the $4$ kg sack, by $3$ kg",
                    "they balance"],
                   "$7 > 4$, so the seven-kilogram sack sinks — heavier by $7 - 4 = 3$ kg.",
                   ["7 > 4", "Eq(7 - 4, 3)", "Eq(4 + 3, 7)"]),
                tp("To level a balance holding $6$ kg against $2$ kg, you add to the light side:",
                   ["$4$ kg", "$8$ kg", "$2$ kg"],
                   "The gap is $6 - 2 = 4$ kg, so adding $4$ kg makes both sides $6$: $2 + 4 = 6$ ✓.",
                   ["Eq(6 - 2, 4)", "Eq(2 + 4, 6)"]),
                tp("A mass written as just \"$5$\" is:",
                   ["incomplete — it needs a unit",
                    "$5$ kilograms", "$5$ litres"],
                   "The unit is half the measurement. Five kilograms and five litres measure quite different things.",
                   ["Eq(5 - 3, 2)"]),
            ]),
            withfig(tapq("Size against weight", "A big box weighs $2$ kg and a small box weighs $7$ kg. Which is heavier?",
                 ["the small box, by $5$ kg", "the big box, because it is bigger",
                  "they weigh the same", "you cannot tell without lifting them"],
                 "The masses are given, and $7 > 2$ — so the small box is heavier by $7 - 2 = 5$ kg. How much room a thing takes up and how heavy it is are two separate measurements.",
                 ["7 > 2", "Eq(7 - 2, 5)", "Eq(2 + 5, 7)"]), fig_same),
            funfact("Why a balance beats a guess",
                    "A balance does not need to know what a kilogram is. It only compares, and comparing is something it does perfectly — which is why balances are thousands of years older than any agreed unit of weight. Traders were weighing goods against each other long before anyone decided how heavy a kilogram should be."),
            withfig(teach("Concept B", "How much does it hold?", [
                "Capacity is a different question again: not how heavy a container is, but how much it HOLDS.",
                "You find out by filling. The picture below shows a $4$-litre jug beside a $6$-litre one — the second holds $6 - 4 = 2$ litres more.",
                "The litre is the unit here, and looks can mislead just as badly as with weight: a tall thin jug and a short wide one can hold exactly the same amount.",
            ]), fig_jugs),
            workedset("Compare two capacities", "Fill them and count the litres.", [
                wex("A jug holds $6$ litres and another holds $4$. Which holds more, and by how much?",
                    ["$6 > 4$, so the first holds more.",
                     "By $6 - 4 = 2$ litres; receipt $4 + 2 = 6$ ✓."],
                    "the $6$-litre jug, by $2$ litres",
                    ["6 > 4", "Eq(6 - 4, 2)", "Eq(4 + 2, 6)"]),
                wex("A bucket holds $9$ litres and a pot holds $5$. Compare them.",
                    ["$9 > 5$, so the bucket holds more.",
                     "By $9 - 5 = 4$ litres."],
                    "$4$ litres more",
                    ["9 > 5", "Eq(9 - 5, 4)", "Eq(5 + 4, 9)"]),
            ]),
            tryitset("Which holds more?", "Litres, not looks.", [
                tp("A pot of $7$ litres and a jug of $3$ litres. The pot holds:",
                   ["$4$ litres more", "$10$ litres more", "$3$ litres more"],
                   "$7 - 3 = 4$ litres more. Adding the two would give $10$, which is what they hold together, not the difference.",
                   ["Eq(7 - 3, 4)", "Eq(7 + 3, 10)"]),
                tp("A tall thin jug and a short wide one both hold $5$ litres. This shows:",
                   ["shape does not decide capacity",
                    "the tall jug must hold more",
                    "one of them was measured wrongly"],
                   "Capacity is found by filling, not by looking. Two containers of quite different shapes can hold exactly the same $5$ litres.",
                   ["Eq(5 - 5, 0)"]),
                tp("Two buckets hold $8$ and $6$ litres. Together they hold:",
                   ["$14$ litres", "$2$ litres", "$48$ litres"],
                   "Together means add: $8 + 6 = 14$ litres. The $2$ is their difference, which answers a different question.",
                   ["Eq(8 + 6, 14)", "Eq(8 - 6, 2)"]),
            ]),
            tapq("Two different questions", "A jug is bigger than a tin but the tin is heavier. Is that possible?",
                 ["yes — size and weight are different measurements",
                  "no — bigger always means heavier",
                  "only if the jug is empty",
                  "no — one of them was measured wrongly"],
                 "Perfectly possible: a big box of wool at $2$ kg against a small box of salt at $7$ kg is the same situation, and $7 > 2$. How much room a thing takes and how heavy it is are answered by different instruments.",
                 ["7 > 2", "Eq(7 - 2, 5)"]),
            recap([
                "A balance compares two masses: the heavier pan goes down.",
                "Mass is said in kilograms; capacity is said in litres.",
                "Capacity is found by filling — shape does not decide how much a container holds.",
                "Size does not decide weight: a big light box can lose to a small heavy one.",
            ]),
            tip("For every measurement, ask yourself what question it answers: how long, how heavy, or how much does it hold. Three questions, three units — and mixing them up is the only way to go badly wrong here."),
            tryitset("Chapter practice", "Which question is being asked?", [
                tp("A $10$ kg sack against a $6$ kg sack: heavier by:",
                   ["$4$ kg", "$16$ kg", "$6$ kg"],
                   "$10 - 6 = 4$ kg. Adding gives their combined weight, not the difference.",
                   ["Eq(10 - 6, 4)", "Eq(6 + 4, 10)"]),
                tp("The right unit for how much a bucket holds is:",
                   ["litres", "kilograms", "centimetres"],
                   "Capacity is measured in litres. Kilograms answer how heavy, and centimetres how long.",
                   ["Eq(6 - 4, 2)"]),
                tp("A feather-filled box is bigger than a stone. The stone is heavier. This is:",
                   ["perfectly normal", "impossible",
                    "only true for very small stones"],
                   "Size and weight are separate measurements — exactly like $2$ kg of wool against $7$ kg of salt, where the smaller box wins by $5$ kg.",
                   ["7 > 2", "Eq(7 - 2, 5)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Heavier, Lighter, Holds More\"",
                    "Three questions now have their own units: how long, how heavy, how much it holds. The next lesson measures something you cannot hold at all — time.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Telling the Time
# ==========================================================================

def lesson_time():
    fig_3 = clock(3, 0)
    fig_half4 = clock(4, 30)
    fig_7 = clock(7, 0)
    return {
        "slug": "telling-the-time",
        "title": "Telling the Time",
        "concreteComparison": (
            "Two hands, one face, and they mean different things. The "
            "short hand says which hour, the long hand says how far "
            "through it you are. Straight up is the start of an hour; "
            "straight down is halfway through."),
        "objective": (
            "Read o'clock and half past on a clock face, say which hand "
            "does which job, and know that an hour is $60$ minutes."),
        "concept": [
            "**The short hand names the hour; the long hand counts the "
            "minutes.** At $3$ o'clock the short hand points at the $3$ "
            "and the long hand points straight up at the $12$ — zero "
            "minutes past.",
            "**An hour is sixty minutes, and half of one is thirty.** When "
            "the long hand points straight down at the $6$, half the hour "
            "has gone: that is half past, $30$ minutes in. Half of $60$ "
            "is $30$ because $2 \\times 30 = 60$.",
            "**At half past, the short hand sits BETWEEN two numbers.** "
            "At half past four it has left the $4$ but not reached the "
            "$5$ — it is halfway between, because half the hour has "
            "passed. Reading it as five o'clock is the classic mistake.",
        ],
        "keyIdea": (
            "The short hand names the hour and the long hand counts the "
            "minutes into it — straight up is o'clock, straight down is "
            "half past."),
        "facts": [
            {"title": "An hour in minutes",
             "latex": "2 \\times 30 = 60",
             "explanation": "An hour is 60 minutes, so half an hour is 30."},
            {"title": "Half past",
             "latex": "60 - 30 = 30",
             "explanation": "At half past, 30 minutes have gone and 30 remain."},
        ],
        "workedExamples": [
            {"id": "g3me-l4-we1",
             "statement": "The long hand points straight up and the short hand points at the $3$. What time is it?",
             "note": "Long hand first — how many minutes?",
             "solution": ("The long hand straight up at the $12$ means zero "
                          "minutes past, so the hour has just begun. The short "
                          "hand at the $3$ names it: $3$ o'clock. A whole hour "
                          "from now the long hand will have gone right round, "
                          "all $60$ minutes of it."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*30, 60)", "Eq(60 - 60, 0)"]},
            {"id": "g3me-l4-we2",
             "statement": "The long hand points straight down and the short hand sits between the $4$ and the $5$. What time is it?",
             "note": "How much of the hour has gone?",
             "solution": ("The long hand straight down at the $6$ means half the "
                          "hour has passed: $30$ minutes of the $60$. The short "
                          "hand has therefore moved halfway from the $4$ towards "
                          "the $5$, so the hour is still the fourth: it is half "
                          "past four."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*30, 60)", "Eq(60 - 30, 30)"]},
        ],
        "commonMistakes": [
            {"text": "Reading half past four as half past five, because the short hand is nearly at the 5.",
             "correction": "The hour is the number the short hand has PASSED, not the one it is heading for. Half past four is 30 minutes into the fourth hour, so the hand sits halfway between 4 and 5.",
             "authored": True},
            {"text": "Swapping the hands and reading 3 o'clock as \"12 past 3\".",
             "correction": "The short hand names the hour and the long hand counts minutes. Long hand straight up means zero minutes past, not twelve.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3me-l4-t1",
             "statement": "How many minutes are there in an hour, and how many in half an hour?",
             "solution": ("An hour is $60$ minutes, and half of that is $30$, "
                          "because $2 \\times 30 = 60$."),
             "check": ["Eq(2*30, 60)", "Eq(60 - 30, 30)"]},
            {"id": "g3me-l4-t2",
             "statement": "At half past seven, where is each hand?",
             "solution": ("The long hand points straight down at the $6$ — $30$ "
                          "minutes past. The short hand sits halfway between the "
                          "$7$ and the $8$, because half of the seventh hour has "
                          "gone."),
             "check": ["Eq(2*30, 60)", "Eq(7 + 1, 8)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Two hands, two jobs", [
                "The clock below reads $3$ o'clock. Look at the two hands: the long one points straight up at the $12$, and the short one points at the $3$.",
                "The long hand counts MINUTES. Straight up means zero minutes past — the hour has only just begun.",
                "The short hand names the HOUR. It is at the $3$, so the time is $3$ o'clock. Two hands, two entirely different jobs, and mixing them up is the only real difficulty here.",
            ]), fig_3),
            workedset("Read o'clock", "Long hand up means the hour has just started.", [
                wex("Long hand straight up, short hand at the $3$. The time?",
                    ["Long hand up: zero minutes past.",
                     "Short hand at $3$: the third hour. So $3$ o'clock."],
                    "$3$ o'clock",
                    ["Eq(60 - 60, 0)", "Eq(2*30, 60)"]),
                wex("Long hand straight up, short hand at the $7$. The time?",
                    ["Zero minutes past again.",
                     "Short hand at $7$: it is $7$ o'clock."],
                    "$7$ o'clock",
                    ["Eq(60 - 60, 0)", "Eq(7 + 1, 8)"]),
            ]),
            tryitset("O'clock", "Which hand names the hour?", [
                withfig(tp("The clock below shows:",
                   ["$7$ o'clock", "$12$ o'clock", "half past seven"],
                   "The long hand points straight up — zero minutes past — and the short hand points at the $7$, naming the hour.",
                   ["Eq(60 - 60, 0)", "Eq(2*30, 60)"]), fig_7),
                tp("The long hand pointing straight up means:",
                   ["zero minutes past the hour",
                    "twelve minutes past the hour",
                    "twelve o'clock, always"],
                   "Straight up is the start of an hour, whatever the short hand says. The short hand is what names WHICH hour.",
                   ["Eq(60 - 60, 0)"]),
                tp("The hand that names the hour is:",
                   ["the short one", "the long one", "either one"],
                   "The short hand names the hour and the long hand counts minutes into it — two hands, two jobs.",
                   ["Eq(2*30, 60)"]),
            ]),
            tapq("Which hand?", "Which hand tells you how many minutes have passed?",
                 ["the long one", "the short one", "both together",
                  "neither — you need a third hand"],
                 "The long hand counts the minutes of the hour, all $60$ of them per lap. The short hand only names which hour you are in.",
                 ["Eq(2*30, 60)", "Eq(60 - 60, 0)"]),
            funfact("Why sixty and not a hundred",
                    "Sixty minutes in an hour is inherited from Babylonian astronomers, who counted in sixties — and it survived because $60$ shares out so beautifully. It splits exactly into halves, thirds, quarters, fifths and sixths: $2 \\times 30$, $3 \\times 20$, $4 \\times 15$. A hundred-minute hour would not divide into thirds at all."),
            withfig(teach("Concept B", "Half past", [
                "The clock below reads half past four. The long hand points straight DOWN, at the $6$.",
                "Straight down means half the hour has gone: $30$ minutes of the $60$, since $2 \\times 30 = 60$. Thirty have passed and thirty remain.",
                "Now look carefully at the short hand. It is no longer on the $4$, but it has not reached the $5$ either — it sits halfway between, because half the fourth hour has gone. The hour is the number it has PASSED, so this is half past four, not half past five.",
            ]), fig_half4),
            workedset("Read half past",
                      "The hour is the number the short hand has passed.", [
                wex("Long hand straight down, short hand between $4$ and $5$. The time?",
                    ["Long hand down: $30$ minutes past.",
                     "Short hand has passed the $4$ but not reached the $5$.",
                     "So it is half past four."],
                    "half past four",
                    ["Eq(2*30, 60)", "Eq(60 - 30, 30)"]),
                wex("Where are the hands at half past seven?",
                    ["Long hand straight down at the $6$: $30$ minutes past.",
                     "Short hand halfway between the $7$ and the $8$."],
                    "down, and between $7$ and $8$",
                    ["Eq(60 - 30, 30)", "Eq(7 + 1, 8)"]),
            ]),
            tryitset("Half past", "Which number has the short hand passed?", [
                withfig(tp("The clock below shows:",
                   ["half past four", "half past five", "$4$ o'clock"],
                   "The long hand is straight down — $30$ minutes past — and the short hand sits between the $4$ and the $5$, so the hour it has passed is the fourth.",
                   ["Eq(60 - 30, 30)", "Eq(2*30, 60)"]), fig_half4),
                tp("At half past six, the long hand points:",
                   ["straight down", "straight up", "at the $3$"],
                   "Straight down at the $6$ marks half the hour: $30$ of the $60$ minutes gone.",
                   ["Eq(60 - 30, 30)"]),
                tp("At half past nine, the short hand is:",
                   ["between the $9$ and the $10$",
                    "exactly on the $9$", "exactly on the $10$"],
                   "Half the ninth hour has gone, so the short hand has moved halfway from the $9$ towards the $10$ — the hour named is still nine.",
                   ["Eq(9 + 1, 10)", "Eq(60 - 30, 30)"]),
            ]),
            tapq("The hour it has passed", "At half past four, why is the short hand not on the $4$?",
                 ["half the hour has gone, so it has moved halfway to the $5$",
                  "because the clock is broken",
                  "it should be on the $5$ by then",
                  "the short hand never points at numbers"],
                 "The short hand moves steadily through the hour, so after $30$ of the $60$ minutes it is halfway between the $4$ and the $5$. The hour is the one it has PASSED — four.",
                 ["Eq(2*30, 60)", "Eq(60 - 30, 30)"]),
            recap([
                "The short hand names the hour; the long hand counts the minutes.",
                "Long hand straight up is o'clock — zero minutes past.",
                "Long hand straight down is half past — $30$ of the hour's $60$ minutes.",
                "At half past, the short hand sits BETWEEN two numbers, and the hour is the one it has passed.",
            ]),
            tip("Read the long hand first and the short hand second — minutes, then hour. Doing it in that order makes the half-past trap almost impossible to fall into, because you already know the hour is only half done."),
            tryitset("Chapter practice", "Long hand first, then the short.", [
                tp("Long hand up, short hand at $5$. The time is:",
                   ["$5$ o'clock", "half past five", "$12$ o'clock"],
                   "Straight up means zero minutes past, and the short hand names the hour: $5$ o'clock.",
                   ["Eq(60 - 60, 0)"]),
                tp("Half an hour is how many minutes?",
                   ["$30$", "$60$", "$15$"],
                   "An hour is $60$ minutes and half of it is $30$, since $2 \\times 30 = 60$.",
                   ["Eq(2*30, 60)", "Eq(60 - 30, 30)"]),
                tp("The short hand sits between the $2$ and the $3$, long hand down. The time is:",
                   ["half past two", "half past three", "$2$ o'clock"],
                   "Long hand down means $30$ minutes past, and the hour is the one the short hand has already passed — the second.",
                   ["Eq(60 - 30, 30)", "Eq(2 + 1, 3)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Telling the Time\"",
                    "Two hands with two jobs, and an hour that halves into thirty. The last lesson counts something people care about even more than the time — money.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Counting Money
# ==========================================================================

def lesson_money():
    fig_notes = coins((100, 3), (50, 2))
    fig_change = coins((500, 1))
    fig_pay = coins((100, 2), (20, 3))
    return {
        "slug": "counting-money",
        "title": "Counting Tögrög",
        "concreteComparison": (
            "A handful of notes is not a number until you count it — and "
            "the fast way is to start with the biggest. Three hundreds "
            "and two fifties: $300$, then $400$, and the answer is on its "
            "way before you have looked at every note."),
        "objective": (
            "Find the total of a set of tögrög notes, work out the change "
            "from a payment, and check the change with a receipt."),
        "concept": [
            "**Count the big notes first.** Three $100$ notes make "
            "$3 \\times 100 = 300$; two $50$ notes make $2 \\times 50 = "
            "100$. Together $300 + 100 = 400$ tögrög. Starting with the "
            "biggest keeps the running total simple.",
            "**Change is what is left after paying.** Pay $400$ tögrög "
            "for something costing $260$ and the change is "
            "$400 - 260 = 140$ tögrög. It is a subtraction like any "
            "other, and it takes the same receipt.",
            "**The receipt proves the change.** $140 + 260 = 400$ ✓ — "
            "the change plus the price must give back exactly what you "
            "handed over. Shopkeepers count change UP from the price for "
            "this very reason.",
        ],
        "keyIdea": (
            "Count money from the biggest note down, and check every "
            "amount of change by adding it back to the price."),
        "facts": [
            {"title": "Counting notes",
             "latex": "3 \\times 100 = 300",
             "explanation": "Three hundred-tögrög notes make 300 tögrög."},
            {"title": "The change receipt",
             "latex": "140 + 260 = 400",
             "explanation": "Change plus price returns what you handed over."},
        ],
        "workedExamples": [
            {"id": "g3me-l5-we1",
             "statement": "Count three $100$ tögrög notes and two $50$ tögrög notes.",
             "note": "Biggest notes first.",
             "solution": ("The hundreds: $3 \\times 100 = 300$ tögrög. The "
                          "fifties: $2 \\times 50 = 100$ tögrög. Together "
                          "$300 + 100 = 400$ tögrög."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*100, 300)", "Eq(2*50, 100)",
                       "Eq(300 + 100, 400)"]},
            {"id": "g3me-l5-we2",
             "statement": "A pencil costs $260$ tögrög and you pay with $400$. What is the change?",
             "note": "Subtract, then take the receipt.",
             "solution": ("Change is what remains after the price is taken off: "
                          "$400 - 260 = 140$ tögrög. Receipt: "
                          "$140 + 260 = 400$ ✓ — the change and the price "
                          "together return exactly what was handed over."),
             "badges": [{"text": "core"}],
             "check": ["Eq(400 - 260, 140)", "Eq(140 + 260, 400)"]},
        ],
        "commonMistakes": [
            {"text": "Counting the number of notes instead of their value — calling five notes \"5 tögrög\".",
             "correction": "A note's value is what counts, not the note itself. Three 100s and two 50s are five notes but 400 tögrög.",
             "authored": True},
            {"text": "Handing over change without checking it adds back to the amount paid.",
             "correction": "Change plus price must return the payment: 140 + 260 = 400 ✓. The check takes a second and catches every slip.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3me-l5-t1",
             "statement": "Count two $100$ notes and three $20$ notes.",
             "solution": ("Hundreds: $2 \\times 100 = 200$. Twenties: "
                          "$3 \\times 20 = 60$. Together $200 + 60 = 260$ "
                          "tögrög."),
             "check": ["Eq(2*100, 200)", "Eq(3*20, 60)",
                       "Eq(200 + 60, 260)"]},
            {"id": "g3me-l5-t2",
             "statement": "A notebook costs $340$ tögrög and you pay with a $500$ note. What is the change, and how do you check it?",
             "solution": ("$500 - 340 = 160$ tögrög. Check with the receipt: "
                          "$160 + 340 = 500$ ✓."),
             "check": ["Eq(500 - 340, 160)", "Eq(160 + 340, 500)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Biggest notes first", [
                "The picture below shows three $100$ tögrög notes and two $50$ tögrög notes. Five notes — but five is not the answer to anything.",
                "Count by VALUE, and start with the biggest: $3 \\times 100 = 300$ tögrög from the hundreds, then $2 \\times 50 = 100$ from the fifties.",
                "Together that is $300 + 100 = 400$ tögrög. Starting from the biggest note keeps the running total tidy and gets you most of the way there in one step.",
            ]), fig_notes),
            workedset("Count the notes", "Value, not number — biggest first.", [
                wex("Count three $100$ notes and two $50$ notes.",
                    ["Hundreds: $3 \\times 100 = 300$.",
                     "Fifties: $2 \\times 50 = 100$.",
                     "Total: $300 + 100 = 400$ tögrög."],
                    "$400$ tögrög",
                    ["Eq(3*100, 300)", "Eq(2*50, 100)",
                     "Eq(300 + 100, 400)"]),
                wex("Count two $100$ notes and three $20$ notes.",
                    ["Hundreds: $2 \\times 100 = 200$.",
                     "Twenties: $3 \\times 20 = 60$.",
                     "Total: $200 + 60 = 260$ tögrög."],
                    "$260$ tögrög",
                    ["Eq(2*100, 200)", "Eq(3*20, 60)",
                     "Eq(200 + 60, 260)"]),
            ]),
            tryitset("How much altogether?", "Count by value, biggest first.", [
                withfig(tp("The notes below come to:",
                   ["$260$ tögrög", "$5$ tögrög", "$120$ tögrög"],
                   "Two hundreds make $200$ and three twenties make $60$: $200 + 60 = 260$ tögrög. Answering $5$ counts the notes rather than their value.",
                   ["Eq(2*100, 200)", "Eq(3*20, 60)",
                    "Eq(200 + 60, 260)"]), fig_pay),
                tp("Four $50$ tögrög notes come to:",
                   ["$200$ tögrög", "$54$ tögrög", "$4$ tögrög"],
                   "$4 \\times 50 = 200$ tögrög — and two fifties make a hundred, so four make two hundreds.",
                   ["Eq(4*50, 200)", "Eq(2*50, 100)"]),
                tp("Five notes are worth $500$ tögrög. They could be:",
                   ["five $100$ notes", "five $50$ notes", "five $20$ notes"],
                   "$5 \\times 100 = 500$ ✓. Five fifties give only $250$ and five twenties $100$ — the number of notes never settles the value.",
                   ["Eq(5*100, 500)", "Eq(5*50, 250)", "Eq(5*20, 100)"]),
            ]),
            tapq("Notes against value", "You hold five notes. How much money is that?",
                 ["you cannot tell without knowing the notes",
                  "$5$ tögrög", "$500$ tögrög", "$50$ tögrög"],
                 "The number of notes says nothing about the value. Five $100$ notes are $5 \\times 100 = 500$ tögrög, but five $20$ notes are only $5 \\times 20 = 100$.",
                 ["Eq(5*100, 500)", "Eq(5*20, 100)", "500 > 100"]),
            funfact("Why shopkeepers count change upwards",
                    "Handed $400$ for a $260$ purchase, a shopkeeper rarely subtracts. They count UP from the price — \"$260$, $300$, $400$\" — handing over notes as they go, and the change is whatever they handed you. It is the same arithmetic as $400 - 260 = 140$, done in the direction that is harder to get wrong."),
            withfig(teach("Concept B", "Change, and the receipt", [
                "Something costs $260$ tögrög and you pay with $400$. The change is what is left over: $400 - 260 = 140$ tögrög.",
                "That is an ordinary subtraction, and it deserves an ordinary receipt: $140 + 260 = 400$ ✓. The change plus the price must give back exactly what you handed over.",
                "The picture below shows a $500$ note. Pay $340$ with it and the change is $500 - 340 = 160$, with receipt $160 + 340 = 500$ ✓. Never hand over change you have not checked.",
            ]), fig_change),
            workedset("Work out the change",
                      "Subtract, then add it back to the price.", [
                wex("A pencil costs $260$ and you pay $400$. What is the change?",
                    ["$400 - 260 = 140$ tögrög.",
                     "Receipt: $140 + 260 = 400$ ✓."],
                    "$140$ tögrög",
                    ["Eq(400 - 260, 140)", "Eq(140 + 260, 400)"]),
                wex("A notebook costs $340$ and you pay with $500$.",
                    ["$500 - 340 = 160$ tögrög.",
                     "Receipt: $160 + 340 = 500$ ✓."],
                    "$160$ tögrög",
                    ["Eq(500 - 340, 160)", "Eq(160 + 340, 500)"]),
            ]),
            tryitset("What is the change?", "Subtract, then check with the receipt.", [
                tp("A book costs $180$ and you pay $200$. The change is:",
                   ["$20$", "$380$", "$120$"],
                   "$200 - 180 = 20$ tögrög, and the receipt $20 + 180 = 200$ ✓ confirms it. Adding would give $380$, more than you handed over.",
                   ["Eq(200 - 180, 20)", "Eq(20 + 180, 200)"]),
                tp("A sweet costs $70$ and you pay with a $100$ note. The change is:",
                   ["$30$", "$170$", "$70$"],
                   "$100 - 70 = 30$ tögrög; receipt $30 + 70 = 100$ ✓.",
                   ["Eq(100 - 70, 30)", "Eq(30 + 70, 100)"]),
                tp("Bat pays $500$ for a $250$ item and is given $300$ change. The receipt says:",
                   ["$300 + 250 = 550$, so it is wrong",
                    "$300 + 250 = 500$, so it is right",
                    "the receipt cannot check change"],
                   "$300 + 250 = 550$, which is $50$ more than he handed over — so the change is too much. The correct change is $500 - 250 = 250$ tögrög.",
                   ["Eq(300 + 250, 550)", "Eq(550 - 500, 50)",
                    "Eq(500 - 250, 250)"]),
            ]),
            tapq("Checking the change", "You pay $400$ for a $260$ item and get $140$ back. Which sum proves it is right?",
                 ["$140 + 260 = 400$", "$400 + 260 = 660$",
                  "$400 - 140 = 260$ is the only check",
                  "$140 \\times 260$"],
                 "Change plus price must return the payment: $140 + 260 = 400$ ✓. (The third option is also true, but the receipt is deliberately an ADDITION — additions are easier to get right than a second subtraction.)",
                 ["Eq(140 + 260, 400)", "Eq(400 - 260, 140)"]),
            recap([
                "Count money by value and start with the biggest note.",
                "Three $100$ notes and two $50$ notes are $400$ tögrög — five notes, but that is not the answer.",
                "Change is payment minus price: $400 - 260 = 140$.",
                "Always check change with the receipt: change plus price equals what you handed over.",
            ]),
            tip("After working out any change, count it back UP to the amount you paid, the way a shopkeeper does. If the count does not land exactly on the payment, the change is wrong."),
            tryitset("Chapter practice", "Value first; then check the change.", [
                tp("Three $50$ notes and one $100$ note come to:",
                   ["$250$ tögrög", "$4$ tögrög", "$150$ tögrög"],
                   "$3 \\times 50 = 150$ plus $100$ gives $150 + 100 = 250$ tögrög.",
                   ["Eq(3*50, 150)", "Eq(150 + 100, 250)"]),
                tp("An item costs $430$ and you pay $500$. The change is:",
                   ["$70$", "$930$", "$130$"],
                   "$500 - 430 = 70$ tögrög; receipt $70 + 430 = 500$ ✓.",
                   ["Eq(500 - 430, 70)", "Eq(70 + 430, 500)"]),
                tp("Which change FAILS its receipt?",
                   ["$300$ paid, $120$ item, $200$ change",
                    "$300$ paid, $120$ item, $180$ change",
                    "$200$ paid, $150$ item, $50$ change"],
                   "$200 + 120 = 320$, which overshoots the $300$ handed over by $20$ — so that change is wrong. The correct amount is $300 - 120 = 180$.",
                   ["Eq(200 + 120, 320)", "Eq(320 - 300, 20)",
                    "Eq(300 - 120, 180)", "Eq(200 - 150, 50)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Counting Tögrög\" — and the topic",
                    "Length, mass, capacity, time and money: five different things to measure, five sets of units, and one habit running through all of them — a number means nothing without the unit beside it. The last topic of the year collects numbers and draws them.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = ruler([1, 5, 8], lo=0, hi=10, highlight=[1, 8])
    fig_pr5 = clock(9, 30)
    return [
        withprobfig(prob("g3me-pr1", "A stick lies along the ruler shown, from the $1$ cm mark to the $8$ cm mark. How long is it, and what answer would a careless reader give?",
             "It covers $8 - 1 = 7$ centimetres, so it is $7$ cm long. A careless reader takes the far mark alone and answers $8$ cm — one centimetre too many, because the stick never started at zero.",
             ["Eq(8 - 1, 7)", "Eq(7 + 1, 8)"]),
             fig_pr1),
        prob("g3me-pr2", "How many centimetres are in $4$ metres? Say which unit you would use for a rope that long, and why.",
             "$4 \\times 100 = 400$ cm. Metres is the better unit here: $4$ is a comfortable number to say and remember, while $400$ is a big number carrying no extra information.",
             ["Eq(4*100, 400)", "400 > 4"]),
        prob("g3me-pr3", "A rope is $2$ m and a ribbon is $170$ cm. Which is longer, and by how much?",
             "Put both in one unit: $2$ m is $2 \\times 100 = 200$ cm. Then $200 > 170$, so the rope is longer by $200 - 170 = 30$ cm. Comparing $2$ with $170$ directly would have given exactly the wrong answer.",
             ["Eq(2*100, 200)", "200 > 170", "Eq(200 - 170, 30)"]),
        prob("g3me-pr4", "A balance holds $8$ kg on one side and $3$ kg on the other. Which way does it tip, and what would level it?",
             "The $8$ kg side goes down, since $8 > 3$. Adding $8 - 3 = 5$ kg to the light side levels it: $3 + 5 = 8$ ✓.",
             ["8 > 3", "Eq(8 - 3, 5)", "Eq(3 + 5, 8)"]),
        withprobfig(prob("g3me-pr5", "Read the clock shown, and say where each hand is and why.",
             "The long hand points straight down at the $6$, so $30$ of the hour's $60$ minutes have gone — half past. The short hand sits between the $9$ and the $10$, having moved halfway through the ninth hour, so the time is half past nine. The hour is the number the short hand has PASSED.",
             ["Eq(2*30, 60)", "Eq(60 - 30, 30)", "Eq(9 + 1, 10)"]), fig_pr5),
        prob("g3me-pr6", "Count four $100$ tögrög notes and one $50$ tögrög note, then say how many notes that is.",
             "Hundreds: $4 \\times 100 = 400$. The fifty adds $50$: $400 + 50 = 450$ tögrög. That is $4 + 1 = 5$ notes — but five is the number of notes, not the amount of money.",
             ["Eq(4*100, 400)", "Eq(400 + 50, 450)", "Eq(4 + 1, 5)"]),
        prob("g3me-pr7", "An item costs $370$ tögrög and Saruul pays with a $500$ note. Find her change and prove it two ways.",
             "Subtracting: $500 - 370 = 130$ tögrög. Counting up the way a shopkeeper does: from $370$ to $400$ is $30$, and from $400$ to $500$ is $100$, so $30 + 100 = 130$ ✓. Receipt: $130 + 370 = 500$ ✓.",
             ["Eq(500 - 370, 130)", "Eq(400 - 370, 30)",
              "Eq(30 + 100, 130)", "Eq(130 + 370, 500)"]),
        prob("g3me-pr8", "Bat says his big box of feathers must be heavier than a small box of salt. Explain what is wrong with his reasoning.",
             "He is judging mass by size, and they are separate measurements. A big box of feathers might weigh $2$ kg while a small box of salt weighs $7$ kg — the salt is heavier by $7 - 2 = 5$ kg despite the smaller box. Only a balance settles which is heavier.",
             ["7 > 2", "Eq(7 - 2, 5)", "Eq(2 + 5, 7)"]),
    ]


def test_bank():
    return [
        prob("g3me-x1", "A pencil lies from the $2$ cm mark to the $9$ cm mark and a ribbon from $0$ to $7$ cm. Which is longer?",
             "The pencil covers $9 - 2 = 7$ cm and the ribbon covers $7 - 0 = 7$ cm — they are exactly the same length, $7$ cm each, despite sitting at different places on the ruler. Reading the pencil's far mark alone would have wrongly made it $9$ cm.",
             ["Eq(9 - 2, 7)", "Eq(7 - 0, 7)"]),
        prob("g3me-x2", "Put $3$ m, $250$ cm and $1$ m in order from shortest to longest.",
             "Into one unit: $3$ m is $300$ cm and $1$ m is $100$ cm. Then $100 < 250 < 300$, so the order is $1$ m, $250$ cm, $3$ m. The gap between the longest and shortest is $300 - 100 = 200$ cm.",
             ["Eq(3*100, 300)", "Eq(1*100, 100)", "100 < 250", "250 < 300",
              "Eq(300 - 100, 200)"]),
        prob("g3me-x3", "A jug holds $9$ litres and a bucket holds $4$. Give both their difference and their combined capacity, and say which question each answers.",
             "Difference: $9 - 4 = 5$ litres, which answers \"how much more does the jug hold\". Combined: $9 + 4 = 13$ litres, which answers \"how much do they hold between them\". Two questions, two different sums.",
             ["Eq(9 - 4, 5)", "Eq(9 + 4, 13)"]),
        prob("g3me-x4", "At half past three, describe exactly where both hands point, and explain why the hour is three and not four.",
             "The long hand points straight down at the $6$: $30$ of the hour's $60$ minutes have gone, since $2 \\times 30 = 60$. The short hand sits halfway between the $3$ and the $4$, because half of the third hour has passed. The hour named is the one the short hand has already PASSED — three — and the fourth hour has not started until the long hand returns to the top.",
             ["Eq(2*30, 60)", "Eq(60 - 30, 30)", "Eq(3 + 1, 4)"]),
        prob("g3me-x5", "Count two $100$ notes, one $50$ note and two $20$ notes. Then find the change from paying a $200$ tögrög item with that money.",
             "Hundreds: $2 \\times 100 = 200$. Fifty: $50$. Twenties: $2 \\times 20 = 40$. Total $200 + 50 + 40 = 290$ tögrög. Paying $200$ from that leaves $290 - 200 = 90$ tögrög, with receipt $90 + 200 = 290$ ✓.",
             ["Eq(2*100, 200)", "Eq(2*20, 40)", "Eq(200 + 50 + 40, 290)",
              "Eq(290 - 200, 90)", "Eq(90 + 200, 290)"]),
        prob("g3me-x6", "Saruul pays $400$ tögrög for an item costing $220$ and is handed $200$ change. Use the receipt to show she has been given the wrong amount, and say how much it is out by.",
             "Receipt: $200 + 220 = 420$, which is $20$ more than the $400$ she handed over — so the change is too much by exactly that. The correct change is $400 - 220 = 180$ tögrög, and $180 + 220 = 400$ ✓.",
             ["Eq(200 + 220, 420)", "Eq(420 - 400, 20)",
              "Eq(400 - 220, 180)", "Eq(180 + 220, 400)"]),
    ]


def main():
    topic = {
        "slug": "measuring-time-and-money",
        "title": "Measuring, Time & Money",
        "grade": 3,
        "status": "published",
        "blurb": ("Measuring length in centimetres from the zero mark, metres "
                  "for the things a ruler cannot reach, comparing masses on a "
                  "balance and capacities by filling, telling o'clock and half "
                  "past, and counting tögrög notes and change."),
        "lessons": [
            lesson_centimetres(),
            lesson_metres(),
            lesson_mass_capacity(),
            lesson_time(),
            lesson_money(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "measuring-time-and-money.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
