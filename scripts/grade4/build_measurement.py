#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 6: Measurement & Units.

The metric ladders for length (mm–cm–m–km) and mass/capacity
(g–kg–tonne, ml–litre), the deliberately AWKWARD base-60 ladder of
time, elapsed-time reckoning by counting up through round hours, and
word problems whose first commandment is CONVERT FIRST.

Through-line: A MEASUREMENT IS A COUNT OF UNITS. Converting is
re-counting the same amount in a different unit — place-value shifts
for the metric ladders (×10, ×100, ×1,000), and the sixty-trade for
time. You can only add or compare counts of the SAME unit; every
error in this topic is a violation of that one sentence.

Same construction as the other Grade 5 builders: every check is
sympy-asserted with exact integers/Rationals before the JSON is
written. Time facts are checked in minutes and seconds — never as
decimal hours, where 1.5 h = 90 min but the ×100 reflex says 150.

Run: python3 scripts/grade4/build_measurement.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (C_ACCENT, C_GREEN, C_NEUTRAL, C_WARM, withfig,  # noqa: E402
                     fig_barchart, fig_clock, fig_groups, fig_numline,
                     funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic)


# ==========================================================================
# Lesson 1 — Units of Length
# ==========================================================================

def lesson_length():
    return {
        "slug": "units-of-length",
        "title": "Units of Length",
        "concreteComparison": (
            "A pencil is $17$ cm, a ger is about $6$ m across, and the "
            "road from Ulaanbaatar to Darkhan runs $220$ km. Measuring "
            "the road in centimetres would take a $22$-million-count; "
            "measuring the pencil in kilometres would need a decimal "
            "with a parade of zeros. Units are TOOLS — you pick the one "
            "sized to the job, and convert when jobs meet."),
        "objective": (
            "Know the metric length ladder (mm, cm, m, km), choose the "
            "sensible unit for a task, and convert in both directions — "
            "including mixed forms like 3 m 45 cm."),
        "concept": [
            "**The length ladder.** $1$ cm $= 10$ mm; $1$ m $= 100$ cm; "
            "$1$ km $= 1\\,000$ m. The rungs are place-value shifts — "
            "×$10$, ×$100$, ×$1\\,000$ — so converting is Topic 5's "
            "ladder-walking with unit names attached.",
            "**Down the ladder multiplies.** A bigger unit re-counted "
            "in a smaller one needs MORE of them: $3$ m $= 300$ cm. "
            "Mixed forms unfold the same way: $3$ m $45$ cm $= 300 + "
            "45 = 345$ cm.",
            "**Up the ladder divides.** $2\\,500$ m $= 2$ km $500$ m — "
            "or, with a decimal, $2.5$ km. Choosing the unit is part "
            "of the answer: a carpenter says $345$ cm, a mapmaker says "
            "$2.5$ km, and both are re-counting, not re-measuring.",
        ],
        "keyIdea": (
            "A measurement is a count of units. Converting re-counts "
            "the same length: down the ladder multiplies (more, smaller "
            "units), up the ladder divides."),
        "facts": [
            {"title": "The length ladder",
             "latex": "1\\ \\text{cm} = 10\\ \\text{mm} \\quad 1\\ \\text{m} = 100\\ \\text{cm} \\quad 1\\ \\text{km} = 1\\,000\\ \\text{m}",
             "explanation": "Three rungs, all powers of ten — the metric system's whole design."},
            {"title": "Mixed form unfolds",
             "latex": "3\\ \\text{m}\\ 45\\ \\text{cm} = 345\\ \\text{cm}",
             "explanation": "Convert the big part, then add the small part — place value with names."},
        ],
        "workedExamples": [
            {"id": "g5me-l1-we1",
             "statement": "A plank measures $3$ m $45$ cm. Express it in centimetres, and in metres as a decimal.",
             "note": "Unfold the metres; then rename with the decimal ladder.",
             "solution": ("Centimetres: $3 \\times 100 + 45 = 345$ cm. As metres: "
                          "$345$ cm $= \\frac{345}{100}$ m $= 3.45$ m — Topic 5's "
                          "staircase wearing a unit."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*100 + 45, 345)", "Eq(Rational(345,100), 3 + Rational(45,100))"]},
            {"id": "g5me-l1-we2",
             "statement": "A trail is $2\\,500$ m long. Write it in kilometres-and-metres, and as a decimal of kilometres.",
             "note": "Up the ladder divides by 1,000.",
             "solution": ("$2\\,500 = 2 \\times 1\\,000 + 500$: $2$ km $500$ m. As a "
                          "decimal: $\\frac{2500}{1000} = 2.5$ km."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*1000 + 500, 2500)", "Eq(Rational(2500,1000), Rational(25,10))"]},
        ],
        "commonMistakes": [
            {"text": "Converting metres to centimetres by ×10 — 3 m = 30 cm.",
             "correction": "Each rung has its own factor: m→cm is ×100 (3 m = 300 cm); only cm→mm is ×10. Say the rung's factor before multiplying.",
             "authored": True},
            {"text": "Multiplying when going UP the ladder — 2,500 m = 2,500,000 km.",
             "correction": "Bigger units mean FEWER of them: going up divides. 2,500 m ÷ 1,000 = 2.5 km. Sanity: a trail can't be two and a half million kilometres.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5me-l1-t1",
             "statement": "Convert $7$ m $8$ cm to centimetres. (Watch the missing tens.)",
             "solution": "$7 \\times 100 + 8 = 708$ cm — the zero tens hold their place, exactly as in Topic 1.",
             "check": ["Eq(7*100 + 8, 708)"]},
            {"id": "g5me-l1-t2",
             "statement": "A ribbon is $460$ cm. Express it in metres-and-centimetres, and decide: is it longer than $4.5$ m?",
             "solution": "$460 = 4 \\times 100 + 60$: $4$ m $60$ cm $= 4.6$ m. And $4.6 > 4.5$ — yes, by $10$ cm.",
             "check": ["Eq(4*100 + 60, 460)", "Rational(46,10) > Rational(45,10)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Pick the tool, know the ladder", [
                "Millimetres for a coin's thickness, centimetres for a pencil, metres for a ger, kilometres for a road — units are tools sized to jobs.",
                "The ladder: $1$ cm $= 10$ mm, $1$ m $= 100$ cm, $1$ km $= 1\\,000$ m — every rung a power of ten.",
                "DOWN the ladder multiplies: the same length re-counted in smaller units needs more of them. $3$ m $= 300$ cm; and $3$ m $45$ cm unfolds to $345$ cm.",
            ]), fig_numline([(0, "0 cm"), (100, "1 m = 100 cm"), (345, "3 m 45 cm")], lo=0, hi=400)),
            workedset("Down the ladder",
                      "Convert the big part; add the small part.", [
                wex("Express $3$ m $45$ cm in centimetres, then as decimal metres.",
                    ["$3 \\times 100 + 45 = 345$ cm.",
                     "$345$ cm $= 3.45$ m — the decimal staircase with a unit on."],
                    "$345$ cm $= 3.45$ m",
                    ["Eq(3*100 + 45, 345)"]),
                wex("Express $6$ km $80$ m in metres.",
                    ["$6 \\times 1\\,000 + 80 = 6\\,080$ m — the zero hundreds hold their place."],
                    "$6\\,080$ m",
                    ["Eq(6*1000 + 80, 6080)"]),
            ]),
            tryitset("Unfold the units", "Name the rung's factor first.", [
                tp("$7$ m $8$ cm in centimetres is:",
                   ["$708$ cm", "$78$ cm", "$780$ cm"],
                   "$700 + 8 = 708$ — the missing tens take a zero. ($78$ dropped it; $780$ misplaced it.)",
                   ["Eq(7*100 + 8, 708)"]),
                tp("$5$ cm $3$ mm in millimetres is:",
                   ["$53$ mm", "$503$ mm", "$530$ mm"],
                   "cm→mm is the ×$10$ rung: $50 + 3 = 53$ mm.",
                   ["Eq(5*10 + 3, 53)"]),
                tp("$2$ km $40$ m in metres is:",
                   ["$2\\,040$ m", "$240$ m", "$2\\,400$ m"],
                   "$2\\,000 + 40 = 2\\,040$ m — zeros on duty in the hundreds.",
                   ["Eq(2*1000 + 40, 2040)"]),
            ]),
            tapq("Which tool?", "The distance from Ulaanbaatar to Darkhan is best measured in:",
                 ["kilometres", "centimetres", "metres", "millimetres"],
                 "Intercity distances are kilometre-sized: about $220$ km — which would be a hopeless $22\\,000\\,000$ cm.",
                 ["Eq(220*1000*100, 22000000)"]),
            funfact("The metre lives in Paris",
                    "For over a century the metre WAS a physical platinum bar kept in a Paris vault — every ruler on earth a copy of it. Today it's defined by the speed of light, so no fire or thief can change how long a metre is."),
            withfig(teach("Concept B", "Up the ladder, and mixed decisions", [
                "UP the ladder divides — bigger units, fewer of them: $2\\,500$ m $= 2.5$ km, or $2$ km $500$ m.",
                "The decimals topic pays off here: $\\div 1\\,000$ walks the digits three steps — $460$ cm $= 4.6$ m.",
                "Which form to use is a communication choice: the carpenter's $345$ cm, the runner's $2.5$ km — same lengths, different audiences.",
            ]), fig_numline([(0, "0"), (1000, "1 km = 1000 m")], lo=0, hi=1000)),
            workedset("Up the ladder",
                      "Divide out the rung; the remainder keeps the small unit.", [
                wex("Express $2\\,500$ m two ways.",
                    ["$2\\,500 \\div 1\\,000 = 2$ r $500$: $2$ km $500$ m.",
                     "Decimal: $2.5$ km."],
                    "$2$ km $500$ m $= 2.5$ km",
                    ["Eq(2*1000 + 500, 2500)", "Eq(Rational(2500,1000), Rational(25,10))"]),
                wex("A ribbon of $460$ cm, in metres — and is it longer than $4.5$ m?",
                    ["$460$ cm $= 4$ m $60$ cm $= 4.6$ m.",
                     "$4.6 > 4.5$: longer by $10$ cm."],
                    "$4.6$ m — yes",
                    ["Eq(4*100 + 60, 460)", "Rational(46,10) > Rational(45,10)"]),
            ]),
            tryitset("Re-count upward", "Divide; keep the remainder in the small unit.", [
                tp("$3\\,250$ m equals:",
                   ["$3$ km $250$ m", "$32$ km $50$ m", "$3$ km $25$ m"],
                   "$3\\,250 = 3 \\times 1\\,000 + 250$.",
                   ["Eq(3*1000 + 250, 3250)"]),
                tp("$85$ mm equals:",
                   ["$8$ cm $5$ mm", "$8$ m $5$ cm", "$85$ cm"],
                   "$85 = 8 \\times 10 + 5$: eight centimetres and five millimetres.",
                   ["Eq(8*10 + 5, 85)"]),
                tp("$907$ cm equals:",
                   ["$9.07$ m", "$9.7$ m", "$90.7$ m"],
                   "$\\div 100$: $9.07$ m — the zero tenths matter (Topic 5's inside zero).",
                   ["Eq(Rational(907,100), 9 + Rational(7,100))"]),
            ]),
            tapq("Direction check", "Converting $1\\,200$ m to kilometres, you should:",
                 ["divide by $1\\,000$ — bigger unit, fewer of them",
                  "multiply by $1\\,000$",
                  "divide by $100$",
                  "add $1\\,000$"],
                 "Up the ladder divides: $1\\,200 \\div 1\\,000 = 1.2$ km. (Multiplying would claim the walk got a thousand times longer by renaming it.)",
                 ["Eq(Rational(1200,1000), Rational(12,10))"]),
            recap([
                "The ladder: 10 mm in a cm, 100 cm in a m, 1,000 m in a km.",
                "Down the ladder multiplies; up the ladder divides — say the rung's factor first.",
                "Mixed forms unfold: 3 m 45 cm = 345 cm; zeros hold missing places.",
                "The decimal staircase does the up-conversions: 460 cm = 4.6 m.",
            ]),
            tip("Before every conversion, say the rung and its factor aloud — \"m to cm, times 100\". The naming kills both classic errors at once."),
            tryitset("Mixed practice", "Both directions, all three rungs.", [
                tp("$5$ km $60$ m in metres is:",
                   ["$5\\,060$ m", "$560$ m", "$5\\,600$ m"],
                   "$5\\,000 + 60 = 5\\,060$ m.",
                   ["Eq(5*1000 + 60, 5060)"]),
                tp("$34$ mm in centimetres-and-millimetres is:",
                   ["$3$ cm $4$ mm", "$34$ cm", "$3$ cm $40$ mm"],
                   "$34 = 3 \\times 10 + 4$.",
                   ["Eq(3*10 + 4, 34)"]),
                tp("Which is LONGEST: $0.9$ km, $950$ m, $9\\,000$ cm?",
                   ["$950$ m", "$0.9$ km", "$9\\,000$ cm"],
                   "One unit for all: $900$ m, $950$ m, $90$ m — the middle one wins.",
                   ["Eq(Rational(9,10)*1000, 900)", "Eq(Rational(9000,100), 90)",
                    "950 > 900", "900 > 90"]),
                tp("A high jump bar sits at $1$ m $27$ cm. In centimetres:",
                   ["$127$ cm", "$1\\,027$ cm", "$12.7$ cm"],
                   "$100 + 27 = 127$ cm.",
                   ["Eq(1*100 + 27, 127)"]),
                tp("A marathon is about $42\\,195$ m. In kilometres that is:",
                   ["$42.195$ km", "$421.95$ km", "$4.2195$ km"],
                   "$\\div 1\\,000$: three steps down the staircase — $42.195$ km.",
                   ["Eq(Rational(42195,1000), 42 + Rational(195,1000))"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Units of Length\"",
                    "One ladder, three rungs, two directions. Mass and capacity next — the same design with new names, which is exactly why the metric system conquered the world.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Mass & Capacity
# ==========================================================================

def lesson_mass_capacity():
    return {
        "slug": "mass-and-capacity",
        "title": "Mass & Capacity",
        "concreteComparison": (
            "A packet of tea is $250$ g, a sack of flour $25$ kg, and a "
            "loaded truck $3$ tonnes. A cup of airag holds $250$ ml; "
            "the jug, $2$ litres. Mass and capacity run on the same "
            "ladder design as length — thousand-steps between "
            "neighbours — so everything you did with metres transfers "
            "in one move."),
        "objective": (
            "Convert between grams, kilograms and tonnes, and between "
            "millilitres and litres, including mixed forms and "
            "how-many-fit problems."),
        "concept": [
            "**The mass ladder.** $1$ kg $= 1\\,000$ g; $1$ tonne $= "
            "1\\,000$ kg. Two rungs, both thousand-steps: $2$ kg $350$ "
            "g $= 2\\,350$ g, and $4\\,700$ kg $= 4$ t $700$ kg.",
            "**The capacity ladder.** $1$ L $= 1\\,000$ ml — one rung, "
            "same design: $1.5$ L $= 1\\,500$ ml. (Capacity measures "
            "how much a container HOLDS; the units are litres and "
            "their thousandths.)",
            "**How many fit?** Capacity problems love division: a $2$ L "
            "jug fills $2\\,000 \\div 250 = 8$ cups of $250$ ml. "
            "Convert to ONE unit first; then it's Topic 3's division, "
            "receipts and all.",
        ],
        "keyIdea": (
            "Mass and capacity reuse the length ladder's design — "
            "thousand-steps between units. Convert to one unit, then "
            "count, add, or divide as usual."),
        "facts": [
            {"title": "The mass ladder",
             "latex": "1\\ \\text{kg} = 1\\,000\\ \\text{g} \\qquad 1\\ \\text{t} = 1\\,000\\ \\text{kg}",
             "explanation": "Two thousand-step rungs — grams to kilograms to tonnes."},
            {"title": "The capacity rung",
             "latex": "1\\ \\text{L} = 1\\,000\\ \\text{ml}",
             "explanation": "One rung; a millilitre is a thousandth of a litre."},
        ],
        "workedExamples": [
            {"id": "g5me-l2-we1",
             "statement": "A parcel weighs $2$ kg $350$ g. Express it in grams, and as a decimal of kilograms.",
             "note": "Thousand-step down, then the staircase back up.",
             "solution": ("$2 \\times 1\\,000 + 350 = 2\\,350$ g. As kilograms: "
                          "$\\frac{2350}{1000} = 2.35$ kg."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*1000 + 350, 2350)", "Eq(Rational(2350,1000), 2 + Rational(35,100))"]},
            {"id": "g5me-l2-we2",
             "statement": "How many $250$ ml cups does a $2$ L jug fill?",
             "note": "One unit first; then divide.",
             "solution": ("Convert: $2$ L $= 2\\,000$ ml. Divide: $2\\,000 \\div 250 "
                          "= 8$ cups. Receipt: $8 \\times 250 = 2\\,000$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*1000, 2000)", "Eq(8*250, 2000)"]},
        ],
        "commonMistakes": [
            {"text": "Converting kg to g by ×100 because metres did that.",
             "correction": "The mass rungs are THOUSAND-steps: 1 kg = 1,000 g. Each ladder has its own factors — say the rung before you multiply.",
             "authored": True},
            {"text": "Dividing mixed units directly — \"2 L ÷ 250 ml = 0.008\".",
             "correction": "Convert to ONE unit first: 2,000 ml ÷ 250 ml = 8 cups. Mixed-unit arithmetic is the cardinal sin of measurement.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5me-l2-t1",
             "statement": "A truck carries $4\\,700$ kg of hay. Express the load in tonnes-and-kilograms.",
             "solution": "$4\\,700 = 4 \\times 1\\,000 + 700$: $4$ t $700$ kg (or $4.7$ t).",
             "check": ["Eq(4*1000 + 700, 4700)", "Eq(Rational(4700,1000), Rational(47,10))"]},
            {"id": "g5me-l2-t2",
             "statement": "How many $200$ ml glasses does a $1.5$ L bottle fill, and what is left over?",
             "solution": "$1.5$ L $= 1\\,500$ ml; $1\\,500 \\div 200 = 7$ r $100$: seven full glasses, $100$ ml left. Receipt: $7 \\times 200 + 100 = 1\\,500$ ✓.",
             "check": ["Eq(Rational(15,10)*1000, 1500)", "Eq(7*200 + 100, 1500)", "100 < 200"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The thousand-step ladders", [
                "Mass climbs by thousands: $1$ kg $= 1\\,000$ g, $1$ tonne $= 1\\,000$ kg. A tea packet is grams, a flour sack kilograms, a loaded truck tonnes.",
                "Mixed forms unfold as with length: $2$ kg $350$ g $= 2\\,350$ g; and the staircase renames upward: $2\\,350$ g $= 2.35$ kg.",
                "Same design as metres — only the factors changed. Say the rung (\"kg to g, times a thousand\") and the length habits transfer whole.",
            ]), fig_groups((1, "1 kg", C_ACCENT), (10, "= 1000 g", C_WARM))),
            workedset("Mass conversions",
                      "Thousand-steps, both directions.", [
                wex("Express $2$ kg $350$ g in grams and decimal kilograms.",
                    ["$2\\,000 + 350 = 2\\,350$ g.",
                     "$\\div 1\\,000$: $2.35$ kg."],
                    "$2\\,350$ g $= 2.35$ kg",
                    ["Eq(2*1000 + 350, 2350)"]),
                wex("Express $4\\,700$ kg in tonnes-and-kilograms.",
                    ["$4\\,700 \\div 1\\,000 = 4$ r $700$.",
                     "$4$ t $700$ kg $= 4.7$ t."],
                    "$4$ t $700$ kg",
                    ["Eq(4*1000 + 700, 4700)"]),
            ]),
            tryitset("Grams, kilograms, tonnes", "Name the rung; then shift.", [
                tp("$3$ kg $60$ g in grams is:",
                   ["$3\\,060$ g", "$360$ g", "$3\\,600$ g"],
                   "$3\\,000 + 60 = 3\\,060$ g — the hundreds place takes its zero.",
                   ["Eq(3*1000 + 60, 3060)"]),
                tp("$5\\,200$ g equals:",
                   ["$5.2$ kg", "$52$ kg", "$0.52$ kg"],
                   "$\\div 1\\,000$: $5.2$ kg.",
                   ["Eq(Rational(5200,1000), Rational(52,10))"]),
                tp("Which is HEAVIER: $0.8$ kg or $795$ g?",
                   ["$0.8$ kg — it is $800$ g", "$795$ g", "they are equal"],
                   "One unit: $0.8$ kg $= 800$ g $> 795$ g — by five grams.",
                   ["Eq(Rational(8,10)*1000, 800)", "800 > 795"]),
            ]),
            tapq("Which unit?", "A sheep's mass is most sensibly given in:",
                 ["kilograms", "grams", "tonnes", "millilitres"],
                 "A sheep runs tens of kilograms — about $50$ kg. Grams would need $50\\,000$; tonnes would need $0.05$; and millilitres measure liquid, not mass.",
                 ["Eq(50*1000, 50000)"]),
            funfact("A litre of water weighs a kilogram",
                    "The metric system's secret handshake: $1$ litre of water has a mass of almost exactly $1$ kilogram — the units were DESIGNED to match. A $2$ L bottle of water: about $2$ kg. No other measurement system ever linked its ladders so neatly."),
            withfig(teach("Concept B", "Capacity, and how-many-fit", [
                "Capacity — how much a container holds — runs one rung: $1$ L $= 1\\,000$ ml. A cup is $250$ ml; a kettle, $1.7$ L.",
                "How-many-fit questions are divisions in disguise: a $2$ L jug into $250$ ml cups — convert first ($2\\,000$ ml), then divide: $8$ cups.",
                "Leftovers behave like Topic 3: $1\\,500 \\div 200 = 7$ r $100$ — seven full glasses and $100$ ml left, receipt and all.",
            ]), fig_groups((4, "4 full jugs", C_ACCENT), (1, "100 ml left", C_WARM))),
            workedset("Capacity work",
                      "One unit, then divide with receipts.", [
                wex("How many $250$ ml cups fill a $2$ L jug?",
                    ["$2$ L $= 2\\,000$ ml; $2\\,000 \\div 250 = 8$.",
                     "Receipt: $8 \\times 250 = 2\\,000$ ✓."],
                    "$8$ cups",
                    ["Eq(8*250, 2000)"]),
                wex("A $1.5$ L bottle into $200$ ml glasses — how many, what remains?",
                    ["$1\\,500 \\div 200 = 7$ r $100$.",
                     "Seven glasses, $100$ ml left; receipt $7 \\times 200 + 100 = 1\\,500$ ✓."],
                    "$7$ glasses, $100$ ml left",
                    ["Eq(7*200 + 100, 1500)"]),
            ]),
            tryitset("Litres and millilitres", "Convert, divide, receipt.", [
                tp("$3.2$ L in millilitres is:",
                   ["$3\\,200$ ml", "$320$ ml", "$32\\,000$ ml"],
                   "$\\times 1\\,000$: $3\\,200$ ml.",
                   ["Eq(Rational(32,10)*1000, 3200)"]),
                tp("How many $500$ ml bottles fill a $4$ L container?",
                   ["$8$", "$4$", "$80$"],
                   "$4\\,000 \\div 500 = 8$; receipt $8 \\times 500 = 4\\,000$ ✓.",
                   ["Eq(8*500, 4000)"]),
                tp("A recipe needs $750$ ml of milk; you have a full $1$ L carton. After cooking, you have:",
                   ["$250$ ml left", "$350$ ml left", "$0.75$ L left"],
                   "$1\\,000 - 750 = 250$ ml.",
                   ["Eq(1000 - 750, 250)"]),
            ]),
            tapq("The cardinal sin", "To find how many $250$ ml cups a $2$ L jug fills, a student computes $2 \\div 250$. The fix:",
                 ["convert first — $2\\,000 \\div 250 = 8$",
                  "swap: $250 \\div 2$",
                  "multiply instead",
                  "nothing — $2 \\div 250$ is right"],
                 "Litres and millilitres cannot meet in one division. Re-count the jug in millilitres ($2\\,000$), THEN divide: $8$ cups.",
                 ["Eq(2*1000, 2000)", "Eq(8*250, 2000)"]),
            recap([
                "Mass: 1 kg = 1,000 g; 1 t = 1,000 kg. Capacity: 1 L = 1,000 ml.",
                "Same ladder design as length — only the factors differ; name the rung first.",
                "How-many-fit = convert to one unit, then divide (receipts included).",
                "Never compute across mixed units — the cardinal sin of measurement.",
            ]),
            tip("Every problem below hides a unit mismatch — find it and convert BEFORE any arithmetic."),
            tryitset("Mixed practice", "Mass and capacity, one unit at a time.", [
                tp("$6$ t $50$ kg in kilograms is:",
                   ["$6\\,050$ kg", "$650$ kg", "$6\\,500$ kg"],
                   "$6\\,000 + 50 = 6\\,050$ kg.",
                   ["Eq(6*1000 + 50, 6050)"]),
                tp("Which is MORE: $2.05$ L or $2\\,045$ ml?",
                   ["$2.05$ L — it is $2\\,050$ ml", "$2\\,045$ ml", "they are equal"],
                   "$2.05$ L $= 2\\,050$ ml $> 2\\,045$ ml — by five millilitres.",
                   ["Eq(Rational(205,100)*1000, 2050)", "2050 > 2045"]),
                tp("Four parcels of $1$ kg $200$ g each weigh, in total:",
                   ["$4.8$ kg", "$4.08$ kg", "$5.2$ kg"],
                   "Each is $1\\,200$ g; four make $4\\,800$ g $= 4.8$ kg.",
                   ["Eq(4*1200, 4800)", "Eq(Rational(4800,1000), Rational(48,10))"]),
                tp("A $330$ ml can, a $0.5$ L bottle, a $1$ L jug — total capacity:",
                   ["$1\\,830$ ml", "$1\\,330$ ml", "$831$ ml"],
                   "One unit: $330 + 500 + 1\\,000 = 1\\,830$ ml.",
                   ["Eq(330 + 500 + 1000, 1830)"]),
                tp("How many $25$ kg sacks make one tonne?",
                   ["$40$", "$4$", "$400$"],
                   "$1\\,000 \\div 25 = 40$; receipt $40 \\times 25 = 1\\,000$ ✓.",
                   ["Eq(40*25, 1000)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Mass & Capacity\"",
                    "Two more ladders, zero new ideas — the metric design pays its dividend. Next: TIME, the one ladder that refuses to run on tens.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Units of Time
# ==========================================================================

def lesson_time_units():
    return {
        "slug": "units-of-time",
        "title": "Units of Time",
        "concreteComparison": (
            "Every ladder so far ran on tens — and then comes the "
            "clock. Sixty seconds to a minute, sixty minutes to an "
            "hour, twenty-four hours to a day: time's ladder was built "
            "four thousand years ago in Babylon, long before decimals, "
            "and it never converted. One habit must change: with time "
            "you trade by SIXTIES, and the ×10 reflexes must stay at "
            "the door."),
        "objective": (
            "Convert between seconds, minutes, hours and days — "
            "including mixed forms and fraction-of-an-hour amounts — "
            "without importing base-ten reflexes."),
        "concept": [
            "**The sixty-ladder.** $1$ min $= 60$ s; $1$ h $= 60$ min; "
            "$1$ day $= 24$ h; $1$ week $= 7$ days. No tens anywhere — "
            "each rung has its own factor, and each must be said aloud.",
            "**Mixed forms trade by the rung.** $2$ h $15$ min $= 2 "
            "\\times 60 + 15 = 135$ min. Backwards: $200$ s $= 3$ min "
            "$20$ s, because $200 \\div 60 = 3$ r $20$ — division with "
            "remainders, wearing a watch.",
            "**Fractions of an hour are sixtieths.** Half an hour $= "
            "30$ min; a quarter $= 15$; three-quarters $= 45$. The "
            "decimal trap: $1.5$ h $= 90$ min, NOT $150$ — the $0.5$ "
            "multiplies sixty, never a hundred.",
        ],
        "keyIdea": (
            "Time trades by sixties (and twenty-fours), not tens: "
            "convert with the rung's own factor, use division with "
            "remainders for mixed forms, and never let 1.5 h become "
            "150 minutes."),
        "facts": [
            {"title": "The sixty-ladder",
             "latex": "1\\ \\text{min} = 60\\ \\text{s} \\quad 1\\ \\text{h} = 60\\ \\text{min} \\quad 1\\ \\text{day} = 24\\ \\text{h}",
             "explanation": "Babylonian rungs — no tens; each factor said aloud."},
            {"title": "The decimal trap",
             "latex": "1.5\\ \\text{h} = 90\\ \\text{min} \\ (\\ne 150)",
             "explanation": "Half an hour is thirty minutes — the .5 multiplies sixty."},
        ],
        "workedExamples": [
            {"id": "g5me-l3-we1",
             "statement": "Convert $2$ h $15$ min to minutes, and $200$ s to minutes-and-seconds.",
             "note": "Down: ×60 and add. Up: divide by 60, keep the remainder.",
             "solution": ("Down: $2 \\times 60 + 15 = 135$ min. Up: $200 \\div 60 = "
                          "3$ r $20$ — three minutes twenty seconds. Receipt: $3 "
                          "\\times 60 + 20 = 200$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*60 + 15, 135)", "Eq(3*60 + 20, 200)", "20 < 60"]},
            {"id": "g5me-l3-we2",
             "statement": "A film lasts $1.5$ hours. How many minutes is that — and why is $150$ wrong?",
             "note": "The .5 is half an HOUR.",
             "solution": ("$1.5$ h $= 1$ h $+ \\frac{1}{2}$ h $= 60 + 30 = 90$ min. "
                          "Writing $150$ applies the base-ten reflex ($1.5 \\times "
                          "100$) to a base-sixty ladder — half an hour has thirty "
                          "minutes, not fifty."),
             "badges": [{"text": "core"}],
             "check": ["Eq(60 + 30, 90)", "Eq(Rational(15,10)*60, 90)", "Ne(90, 150)"]},
        ],
        "commonMistakes": [
            {"text": "Converting 1.5 h to 150 min — the ×100 reflex on a ×60 ladder.",
             "correction": "The decimal part multiplies SIXTY: 0.5 × 60 = 30, so 1.5 h = 90 min. Time is the one ladder where decimal shifting lies.",
             "authored": True},
            {"text": "Writing 200 s as 2 min 00 s — dividing by 100.",
             "correction": "Divide by 60: 200 = 3 × 60 + 20, so 3 min 20 s. The remainder must stay under 60 — a '2 min 80 s' answer stopped early.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5me-l3-t1",
             "statement": "Convert $3$ h $40$ min to minutes, and $500$ s to minutes-and-seconds.",
             "solution": "$3 \\times 60 + 40 = 220$ min. And $500 \\div 60 = 8$ r $20$: $8$ min $20$ s; receipt $8 \\times 60 + 20 = 500$ ✓.",
             "check": ["Eq(3*60 + 40, 220)", "Eq(8*60 + 20, 500)", "20 < 60"]},
            {"id": "g5me-l3-t2",
             "statement": "How many minutes are in $\\frac{3}{4}$ of an hour? In $2\\frac{1}{4}$ hours?",
             "solution": "$\\frac{3}{4} \\times 60 = 45$ min. And $2\\frac{1}{4}$ h $= 120 + 15 = 135$ min.",
             "check": ["Eq(Rational(3,4)*60, 45)", "Eq(2*60 + 15, 135)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The ladder that refuses tens", [
                "Time's rungs: $60$ s to the minute, $60$ min to the hour, $24$ h to the day, $7$ days to the week. Not a ten in sight.",
                "Down the ladder still multiplies — by the RUNG'S factor: $2$ h $15$ min $= 2 \\times 60 + 15 = 135$ min.",
                "Up the ladder is division with remainders: $200$ s $= 3$ min $20$ s ($200 \\div 60 = 3$ r $20$) — and the remainder must stay under sixty.",
            ]), fig_clock(1, 0, label="60 minutes = 1 hour")),
            workedset("Trading by sixties",
                      "×60 down; ÷60 with remainders up.", [
                wex("Convert $2$ h $15$ min to minutes; $200$ s to min-and-s.",
                    ["$2 \\times 60 + 15 = 135$ min.",
                     "$200 \\div 60 = 3$ r $20$: $3$ min $20$ s ✓."],
                    "$135$ min; $3$ min $20$ s",
                    ["Eq(2*60 + 15, 135)", "Eq(3*60 + 20, 200)"]),
                wex("Convert $3$ days to hours, and $100$ h to days-and-hours.",
                    ["$3 \\times 24 = 72$ h.",
                     "$100 \\div 24 = 4$ r $4$: $4$ days $4$ h; receipt $4 \\times 24 + 4 = 100$ ✓."],
                    "$72$ h; $4$ days $4$ h",
                    ["Eq(3*24, 72)", "Eq(4*24 + 4, 100)"]),
            ]),
            tryitset("Rung by rung", "Say the factor — 60 or 24 — before converting.", [
                tp("$3$ h $40$ min in minutes is:",
                   ["$220$ min", "$340$ min", "$180$ min"],
                   "$180 + 40 = 220$. ($340$ is the base-ten reflex gluing digits.)",
                   ["Eq(3*60 + 40, 220)"]),
                tp("$500$ s equals:",
                   ["$8$ min $20$ s", "$5$ min $0$ s", "$8$ min $33$ s"],
                   "$500 \\div 60 = 8$ r $20$; receipt $480 + 20 = 500$ ✓.",
                   ["Eq(8*60 + 20, 500)"]),
                tp("$2$ days $6$ h in hours is:",
                   ["$54$ h", "$26$ h", "$60$ h"],
                   "$48 + 6 = 54$ h.",
                   ["Eq(2*24 + 6, 54)"]),
            ]),
            tapq("Remainder discipline", "A student writes $170$ s $= 2$ min $50$ s. Verdict:",
                 ["correct — $2 \\times 60 + 50 = 170$ and $50 < 60$",
                  "wrong — it should be $1$ min $70$ s",
                  "wrong — divide by $100$",
                  "wrong — seconds cannot exceed $100$"],
                 "Receipt: $120 + 50 = 170$ ✓, remainder under sixty ✓. ($1$ min $70$ s names the same amount but stopped trading early.)",
                 ["Eq(2*60 + 50, 170)", "50 < 60"]),
            funfact("Blame Babylon",
                    "Sixty survives from Babylonian astronomy: $60$ divides evenly by $2, 3, 4, 5, 6, 10, 12, 15, 20$ and $30$ — perfect for splitting hours into clean parts. A decimal clock was actually tried during the French Revolution ($10$-hour days!); it lasted about two years."),
            withfig(teach("Concept B", "Fractions of an hour, and the trap", [
                "An hour splits like any whole: half $= 30$ min, a quarter $= 15$, three-quarters $= 45$ — the fraction multiplies SIXTY.",
                "The decimal trap: $1.5$ h is $1$ h $+ 0.5 \\times 60 = 90$ min. The $\\times 100$ reflex says $150$ — and lies.",
                "Mixed hours convert the same way: $2\\frac{1}{4}$ h $= 120 + 15 = 135$ min. Fractions of a minute too: $\\frac{1}{2}$ min $= 30$ s.",
            ]), fig_clock(3, 30, label="half past 3 = 30 min")),
            workedset("Hour fractions",
                      "The fraction multiplies sixty, never a hundred.", [
                wex("How many minutes in $1.5$ h?",
                    ["$1$ h $= 60$; $0.5$ h $= 30$.",
                     "$90$ min — the $150$ answer used the wrong ladder."],
                    "$90$ min",
                    ["Eq(Rational(15,10)*60, 90)", "Ne(90, 150)"]),
                wex("How many minutes in $\\frac{3}{4}$ h and in $2\\frac{1}{4}$ h?",
                    ["$\\frac{3}{4} \\times 60 = 45$ min.",
                     "$2\\frac{1}{4}$ h $= 120 + 15 = 135$ min."],
                    "$45$ and $135$ min",
                    ["Eq(Rational(3,4)*60, 45)", "Eq(2*60 + 15, 135)"]),
            ]),
            tryitset("Fraction hours", "Multiply the sixty.", [
                tp("$\\frac{1}{4}$ h equals:",
                   ["$15$ min", "$25$ min", "$40$ min"],
                   "$60 \\div 4 = 15$ minutes.",
                   ["Eq(Rational(1,4)*60, 15)"]),
                tp("$2.5$ h equals:",
                   ["$150$ min", "$250$ min", "$130$ min"],
                   "$120 + 30 = 150$ min — and here $150$ IS right, because $2.5 \\times 60 = 150$. (The trap is using $\\times 100$; $2.5 \\times 100$ would give $250$.)",
                   ["Eq(Rational(25,10)*60, 150)", "Ne(150, 250)"]),
                tp("$\\frac{2}{3}$ h equals:",
                   ["$40$ min", "$20$ min", "$66$ min"],
                   "$\\frac{2}{3} \\times 60 = 40$ minutes. ($66$ is the decimal-digits reflex.)",
                   ["Eq(Rational(2,3)*60, 40)"]),
            ]),
            tapq("Spot the ladder", "Which conversion is WRONG?",
                 ["$1.2$ h $= 120$ min", "$\\frac{1}{2}$ h $= 30$ min", "$2$ h $= 120$ min", "$\\frac{1}{6}$ h $= 10$ min"],
                 "$1.2$ h $= 60 + 0.2 \\times 60 = 72$ min — the $120$ came from $\\times 100$. The others all multiplied sixty honestly.",
                 ["Eq(Rational(12,10)*60, 72)", "Ne(72, 120)", "Eq(Rational(1,6)*60, 10)"]),
            recap([
                "Time's rungs: 60 s, 60 min, 24 h, 7 days — no tens anywhere.",
                "Down multiplies by the rung's factor; up divides with a remainder under it.",
                "Fractions of an hour multiply sixty: 3/4 h = 45 min.",
                "The decimal trap: 1.5 h = 90 min — the ×100 reflex lies on this ladder.",
            ]),
            tip("Before every conversion say WHICH sixty (or twenty-four) you're trading — the spoken factor is the whole defence."),
            tryitset("Mixed practice", "All rungs, traps armed.", [
                tp("$4$ min $35$ s in seconds is:",
                   ["$275$ s", "$435$ s", "$240$ s"],
                   "$240 + 35 = 275$ s.",
                   ["Eq(4*60 + 35, 275)"]),
                tp("$150$ min equals:",
                   ["$2$ h $30$ min", "$1$ h $50$ min", "$2$ h $50$ min"],
                   "$150 \\div 60 = 2$ r $30$; receipt $120 + 30 = 150$ ✓.",
                   ["Eq(2*60 + 30, 150)"]),
                tp("A week has how many hours?",
                   ["$168$", "$70$", "$144$"],
                   "$7 \\times 24 = 168$ hours.",
                   ["Eq(7*24, 168)"]),
                tp("Which is LONGER: $\\frac{3}{4}$ h or $50$ min?",
                   ["$50$ min", "$\\frac{3}{4}$ h", "they are equal"],
                   "$\\frac{3}{4}$ h $= 45$ min $< 50$ min.",
                   ["Eq(Rational(3,4)*60, 45)", "50 > 45"]),
                tp("$0.25$ h equals:",
                   ["$15$ min", "$25$ min", "$2.5$ min"],
                   "A quarter of sixty: $15$ min. ($25$ is the decimal-digits reflex again.)",
                   ["Eq(Rational(25,100)*60, 15)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Units of Time\"",
                    "The one ladder that trades by sixties — and now its traps are labelled. Next: reading the clock in motion, where counting up through round hours does all the work.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Elapsed Time
# ==========================================================================

def lesson_elapsed():
    return {
        "slug": "elapsed-time",
        "title": "Elapsed Time",
        "concreteComparison": (
            "The train leaves Ulaanbaatar at $9{:}45$ and reaches "
            "Darkhan at $11{:}20$. How long is the ride? Don't subtract "
            "the clock faces — CLIMB: $9{:}45$ to $10{:}00$ is $15$ "
            "minutes, to $11{:}00$ is an hour more, to $11{:}20$ is "
            "twenty more. Total: $1$ h $35$ min. The cashier's "
            "counting-up move from Topic 2, reading a clock."),
        "objective": (
            "Find elapsed time by counting up through round hours, find "
            "end times from a start and a duration, and read simple "
            "timetables."),
        "concept": [
            "**Count up through round hours.** From $9{:}45$: climb "
            "$15$ min to $10{:}00$, then whole hours, then the loose "
            "minutes — $15 + 60 + 20 = 95$ min $= 1$ h $35$ min. The "
            "round hours are the landmarks; the climb is the answer.",
            "**Clock subtraction is a trap.** $11{:}20 - 9{:}45$ "
            "column-style hits '$20 - 45$' and tempts a base-ten "
            "borrow — but an hour breaks into SIXTY minutes, not a "
            "hundred. Counting up avoids the broken borrow entirely.",
            "**End times add the same way.** Start $8{:}40$, duration "
            "$1$ h $50$ min: add the hour ($9{:}40$), then the "
            "minutes — $40 + 50 = 90$ min $= 1$ h $30$, so $10{:}30$. "
            "Minutes past sixty trade up into an hour, always.",
        ],
        "keyIdea": (
            "Elapsed time is a climb through round hours — count up to "
            "the next hour, across the whole hours, then the loose "
            "minutes. Minutes trade at sixty, never at a hundred."),
        "facts": [
            {"title": "The climb",
             "latex": "9{:}45 \\xrightarrow{+15} 10{:}00 \\xrightarrow{+60} 11{:}00 \\xrightarrow{+20} 11{:}20",
             "explanation": "15 + 60 + 20 = 95 min = 1 h 35 min — landmarks at the round hours."},
            {"title": "Minutes trade at sixty",
             "latex": "40 + 50 = 90 = 60 + 30 \\ \\Rightarrow\\ +1\\ \\text{h}\\ 30",
             "explanation": "Past sixty, minutes carry into the hour — never at a hundred."},
        ],
        "workedExamples": [
            {"id": "g5me-l4-we1",
             "statement": "A train leaves at $9{:}45$ and arrives at $11{:}20$. How long is the journey?",
             "note": "Climb through the round hours.",
             "solution": ("$9{:}45 \\to 10{:}00$: $15$ min. $10{:}00 \\to 11{:}00$: "
                          "$60$ min. $11{:}00 \\to 11{:}20$: $20$ min. Total $15 + "
                          "60 + 20 = 95$ min $= 1$ h $35$ min."),
             "badges": [{"text": "core"}],
             "check": ["Eq(15 + 60 + 20, 95)", "Eq(95, 60 + 35)"]},
            {"id": "g5me-l4-we2",
             "statement": "A lesson starts at $8{:}40$ and lasts $1$ h $50$ min. When does it end?",
             "note": "Hours first, then minutes — trading at sixty.",
             "solution": ("Add the hour: $9{:}40$. Add $50$ min: $40 + 50 = 90$ min "
                          "$= 1$ h $30$ min — trade up: $10{:}30$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(40 + 50, 90)", "Eq(90, 60 + 30)", "Eq(8 + 1 + 1, 10)"]},
        ],
        "commonMistakes": [
            {"text": "Subtracting clock readings like base-ten numbers — 11:20 − 9:45 with a hundred-borrow.",
             "correction": "An hour breaks into 60 minutes, not 100. Count UP through the round hours instead — the climb never borrows wrong.",
             "authored": True},
            {"text": "Leaving 90 minutes unconverted in an end time — \"9:90\".",
             "correction": "Sixty minutes make the next hour: 9:90 trades to 10:30. No clock reading carries minutes ≥ 60.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5me-l4-t1",
             "statement": "A film runs from $10{:}20$ to $12{:}05$. How long is it?",
             "solution": "$10{:}20 \\to 11{:}00$: $40$. $\\to 12{:}00$: $60$. $\\to 12{:}05$: $5$. Total $105$ min $= 1$ h $45$ min.",
             "check": ["Eq(40 + 60 + 5, 105)", "Eq(105, 60 + 45)"]},
            {"id": "g5me-l4-t2",
             "statement": "Training starts at $16{:}35$ and lasts $45$ min. When does it end?",
             "solution": "$35 + 45 = 80$ min $= 1$ h $20$: the clock reads $17{:}20$.",
             "check": ["Eq(35 + 45, 80)", "Eq(80, 60 + 20)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Climb, don't subtract", [
                "Elapsed time is a journey between clock readings — and the fastest route climbs through the ROUND HOURS.",
                "$9{:}45 \\to 11{:}20$: fifteen to the hour, sixty across, twenty beyond — $95$ min $= 1$ h $35$.",
                "Column subtraction on clock faces invites a base-ten borrow into a base-sixty world; the climb never breaks an hour wrong.",
            ]), fig_clock(7, 50, until=(9, 15), label="7:50 start", until_label="9:15 finish")),
            workedset("Climbing the clock",
                      "To the hour, across the hours, past the hour.", [
                wex("How long from $9{:}45$ to $11{:}20$?",
                    ["$+15$ to $10{:}00$; $+60$ to $11{:}00$; $+20$ to arrival.",
                     "$95$ min $= 1$ h $35$ min."],
                    "$1$ h $35$ min",
                    ["Eq(15 + 60 + 20, 95)"]),
                wex("How long from $10{:}20$ to $12{:}05$?",
                    ["$+40$, $+60$, $+5$.",
                     "$105$ min $= 1$ h $45$ min."],
                    "$1$ h $45$ min",
                    ["Eq(40 + 60 + 5, 105)"]),
            ]),
            tryitset("Journey lengths", "Climb through the round hours.", [
                tp("From $7{:}50$ to $9{:}15$ is:",
                   ["$1$ h $25$ min", "$1$ h $35$ min", "$2$ h $25$ min"],
                   "$+10$, $+60$, $+15$: $85$ min $= 1$ h $25$.",
                   ["Eq(10 + 60 + 15, 85)", "Eq(85, 60 + 25)"]),
                tp("From $13{:}30$ to $16{:}10$ is:",
                   ["$2$ h $40$ min", "$3$ h $20$ min", "$2$ h $20$ min"],
                   "$+30$ to $14{:}00$, $+120$ to $16{:}00$, $+10$: $160$ min $= 2$ h $40$.",
                   ["Eq(30 + 120 + 10, 160)", "Eq(160, 2*60 + 40)"]),
                tp("A shop opens $9{:}00$ and closes $18{:}30$. It is open for:",
                   ["$9$ h $30$ min", "$8$ h $30$ min", "$9$ h $70$ min"],
                   "Nine whole hours to $18{:}00$, then thirty: $9$ h $30$ min.",
                   ["Eq(9*60 + 30, 570)"]),
            ]),
            tapq("The broken borrow", "Computing $11{:}20 - 9{:}45$ by columns, a student borrows and writes \"$1{:}75$\". The real elapsed time is:",
                 ["$1$ h $35$ min — the borrowed hour is $60$ min, not $100$",
                  "$1$ h $75$ min",
                  "$2$ h $25$ min",
                  "$1$ h $15$ min"],
                 "The borrow crossed an HOUR: $20 + 60 = 80$, then $80 - 45 = 35$ — giving $1$ h $35$. The climb ($15 + 60 + 20 = 95$ min) gets there without any borrow at all.",
                 ["Eq(80 - 45, 35)", "Eq(15 + 60 + 20, 95)", "Eq(95, 60 + 35)"]),
            funfact("The 24-hour clock skips the guesswork",
                    "Timetables use $16{:}35$ instead of \"4:35 in the afternoon\" so that no journey ever looks like it ends before it starts. Reading both clocks — $16{:}35$ IS $4{:}35$ pm — is a five-second skill worth having before every train you'll ever catch."),
            withfig(teach("Concept B", "End times and timetables", [
                "Start $+$ duration: add hours first, then minutes — and minutes past sixty trade UP: $8{:}40 + 1$ h $50$ → $9{:}40$, then $40 + 50 = 90 = 60 + 30$ → $10{:}30$.",
                "Backwards works too: to arrive at $11{:}00$ after a $35$-min walk, leave by $10{:}25$.",
                "A timetable is rows of this arithmetic: departure, duration, arrival — one of them always missing, the other two rebuilding it.",
            ]), fig_clock(10, 20, until=(11, 5), label="depart 10:20", until_label="arrive 11:05")),
            workedset("Start + duration",
                      "Hours, then minutes; trade at sixty.", [
                wex("A lesson starts $8{:}40$ and lasts $1$ h $50$ min. End time?",
                    ["$+1$ h: $9{:}40$. $+50$ min: $90$ min total — trade: $+1$ h $30$.",
                     "$10{:}30$."],
                    "$10{:}30$",
                    ["Eq(40 + 50, 90)", "Eq(90, 60 + 30)"]),
                wex("To reach school at $8{:}15$ after a $25$-min ride, leave by:",
                    ["Climb back: $8{:}15 - 15 = 8{:}00$; $-10$ more: $7{:}50$.",
                     "$7{:}50$."],
                    "$7{:}50$",
                    ["Eq(15 + 10, 25)", "Eq(50 + 25 - 60, 15)"]),
            ]),
            tryitset("Arrivals and departures", "One missing piece each time.", [
                tp("Training starts $16{:}35$, lasts $45$ min. It ends at:",
                   ["$17{:}20$", "$16{:}80$", "$17{:}10$"],
                   "$35 + 45 = 80 = 60 + 20$: $17{:}20$. (A clock never shows $80$ minutes.)",
                   ["Eq(35 + 45, 80)", "Eq(80, 60 + 20)"]),
                tp("A bus leaves $10{:}50$ and rides $30$ min. It arrives at:",
                   ["$11{:}20$", "$10{:}80$", "$11{:}30$"],
                   "$50 + 30 = 80 = 60 + 20$: $11{:}20$.",
                   ["Eq(50 + 30, 80)"]),
                tp("Dinner must be ready at $19{:}00$; cooking takes $1$ h $25$ min. Start by:",
                   ["$17{:}35$", "$18{:}35$", "$17{:}25$"],
                   "Back $1$ h: $18{:}00$; back $25$ min: $17{:}35$. Check: $17{:}35 + 1$ h $25 = 19{:}00$ ✓.",
                   ["Eq(35 + 25, 60)", "Eq(17 + 1 + 1, 19)"]),
            ]),
            tapq("Timetable row", "A timetable shows: departs $14{:}55$, arrives $16{:}10$. The journey takes:",
                 ["$1$ h $15$ min", "$1$ h $55$ min", "$2$ h $15$ min", "$1$ h $25$ min"],
                 "Climb: $+5$ to $15{:}00$, $+60$ to $16{:}00$, $+10$: $75$ min $= 1$ h $15$ min.",
                 ["Eq(5 + 60 + 10, 75)", "Eq(75, 60 + 15)"]),
            recap([
                "Elapsed time: climb to the next round hour, across whole hours, then loose minutes.",
                "Clock subtraction invites the hundred-borrow — an hour is 60 minutes; climb instead.",
                "End times: hours first, minutes second, trading past-sixty minutes up.",
                "Backwards planning climbs down the same landmarks.",
            ]),
            tip("Draw the climb for each one — start time, round-hour landmarks, arrival — before any arithmetic. The picture is the method."),
            tryitset("Mixed practice", "Journeys, endings, and departures.", [
                tp("From $6{:}40$ to $8{:}05$ is:",
                   ["$1$ h $25$ min", "$1$ h $35$ min", "$2$ h $25$ min"],
                   "$+20$, $+60$, $+5$: $85$ min $= 1$ h $25$.",
                   ["Eq(20 + 60 + 5, 85)"]),
                tp("Homework starts $17{:}45$ and takes $50$ min. It ends at:",
                   ["$18{:}35$", "$17{:}95$", "$18{:}45$"],
                   "$45 + 50 = 95 = 60 + 35$: $18{:}35$.",
                   ["Eq(45 + 50, 95)", "Eq(95, 60 + 35)"]),
                tp("A bakery bakes from $5{:}30$ to $11{:}15$. Baking time:",
                   ["$5$ h $45$ min", "$6$ h $15$ min", "$5$ h $15$ min"],
                   "$+30$ to $6{:}00$, five hours to $11{:}00$, $+15$: $5$ h $45$ min.",
                   ["Eq(30 + 5*60 + 15, 345)", "Eq(345, 5*60 + 45)"]),
                tp("To catch a $9{:}05$ train with a $40$-min ride, leave by:",
                   ["$8{:}25$", "$8{:}35$", "$8{:}65$"],
                   "Back $5$ to $9{:}00$, back $35$ more: $8{:}25$. Check: $8{:}25 + 40 = 9{:}05$ ✓.",
                   ["Eq(5 + 35, 40)", "Eq(25 + 40, 65)", "Eq(65, 60 + 5)"]),
                tp("A match kicks off $19{:}30$ and lasts $105$ min. Full-time whistle:",
                   ["$21{:}15$", "$20{:}75$", "$21{:}35$"],
                   "$105$ min $= 1$ h $45$: $19{:}30 + 1$ h $= 20{:}30$, $+45 = 21{:}15$.",
                   ["Eq(105, 60 + 45)", "Eq(30 + 45, 75)", "Eq(75, 60 + 15)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Elapsed Time\"",
                    "Counting up through landmarks — the same move that made change at the market — now reads any clock, timetable or schedule. One lesson left: measurement problems in the wild, where the first rule is CONVERT FIRST.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Measurement Word Problems
# ==========================================================================

def lesson_word_problems():
    return {
        "slug": "measurement-word-problems",
        "title": "Measurement Word Problems",
        "concreteComparison": (
            "A shelf plan calls for a board of $1.2$ m plus a ledge of "
            "$45$ cm. Add them as written — $1.2 + 45 = 46.2$ — and "
            "you've built nonsense: metres and centimetres cannot meet "
            "in one sum. CONVERT FIRST: $120 + 45 = 165$ cm. Every "
            "measurement problem starts with one question — are all my "
            "numbers speaking the same unit?"),
        "objective": (
            "Solve multi-step measurement problems across length, mass, "
            "capacity and time, converting to a common unit BEFORE any "
            "arithmetic, and reporting answers in sensible units."),
        "concept": [
            "**Convert first.** Mixed units in one computation is the "
            "cardinal sin: $1.2$ m $+ 45$ cm becomes $120 + 45 = 165$ "
            "cm (or $1.2 + 0.45 = 1.65$ m — either unit works, as long "
            "as it's ONE unit).",
            "**Then it's Topics 2 and 3.** Once units agree, "
            "measurement problems are event queues, receipts, and "
            "division with remainders wearing unit names: a $2$ L "
            "bottle minus $750$ ml is $2\\,000 - 750 = 1\\,250$ ml.",
            "**Answer in a sensible unit.** $3\\,600$ g is truthful, "
            "but the shopper hears $3.6$ kg. Finish by climbing the "
            "ladder to the unit the situation speaks — that last "
            "conversion is part of the answer.",
        ],
        "keyIdea": (
            "One unit before any arithmetic, familiar arithmetic in the "
            "middle, and a sensible unit at the end — the three-part "
            "shape of every measurement problem."),
        "facts": [
            {"title": "The three-part shape",
             "latex": "\\text{convert} \\to \\text{compute} \\to \\text{report sensibly}",
             "explanation": "Unit alignment first, Topics 2–3 in the middle, a ladder-climb to finish."},
            {"title": "The cardinal sin",
             "latex": "1.2\\ \\text{m} + 45\\ \\text{cm} \\ne 46.2",
             "explanation": "Mixed units in one sum build nonsense — 165 cm is the truth."},
        ],
        "workedExamples": [
            {"id": "g5me-l5-we1",
             "statement": "A board of $1.2$ m and a ledge of $45$ cm are joined end to end. How long is the whole, in centimetres and in metres?",
             "note": "Convert first — either unit, but one unit.",
             "solution": ("Convert: $1.2$ m $= 120$ cm. Add: $120 + 45 = 165$ cm "
                          "$= 1.65$ m. (Adding $1.2 + 45$ raw would claim a "
                          "$46$-metre shelf.)"),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(12,10)*100, 120)", "Eq(120 + 45, 165)",
                       "Eq(Rational(165,100), 1 + Rational(65,100))"]},
            {"id": "g5me-l5-we2",
             "statement": "Three parcels each weigh $1$ kg $200$ g. What is the total mass, in a sensible unit?",
             "note": "Convert, multiply, climb back.",
             "solution": ("Each: $1\\,200$ g. Total: $3 \\times 1\\,200 = 3\\,600$ g "
                          "— reported sensibly, $3.6$ kg."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*1200, 3600)", "Eq(Rational(3600,1000), Rational(36,10))"]},
        ],
        "commonMistakes": [
            {"text": "Computing across mixed units — 2 L − 750 ml = 1.25 by luck, or 748 by disaster.",
             "correction": "Convert first, every time: 2,000 − 750 = 1,250 ml. Getting it right by accident once teaches the habit of getting it wrong forever.",
             "authored": True},
            {"text": "Reporting raw ladder-bottom answers — \"the parcels weigh 3,600 g\".",
             "correction": "True but tone-deaf: climb to the unit the situation speaks — 3.6 kg. The final conversion is part of the answer.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5me-l5-t1",
             "statement": "A $2$ L kettle is filled from a jug holding $750$ ml, poured twice. How much more water is needed?",
             "solution": "Poured: $2 \\times 750 = 1\\,500$ ml. Needed: $2\\,000 - 1\\,500 = 500$ ml more.",
             "check": ["Eq(2*750, 1500)", "Eq(2000 - 1500, 500)"]},
            {"id": "g5me-l5-t2",
             "statement": "A hike covers $3.4$ km before lunch and $2\\,800$ m after. What is the day's total, in kilometres?",
             "solution": "One unit: $3\\,400 + 2\\,800 = 6\\,200$ m $= 6.2$ km.",
             "check": ["Eq(3400 + 2800, 6200)", "Eq(Rational(6200,1000), Rational(62,10))"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Convert first — the one commandment", [
                "Before ANY arithmetic, ask: do all my numbers speak the same unit? $1.2$ m $+ 45$ cm — not yet. Convert: $120 + 45 = 165$ cm.",
                "Either direction works ($1.20 + 0.45 = 1.65$ m) — the sin is mixing, not the choice of unit.",
                "After conversion it's old arithmetic: event queues, receipts, remainders — Topics 2 and 3 wearing unit names.",
            ]), fig_numline([(0, "0 cm"), (250, "2.5 m"), (400, "4 m")], lo=0, hi=400)),
            workedset("Unit alignment",
                      "One unit in, familiar arithmetic after.", [
                wex("Join a $1.2$ m board and a $45$ cm ledge.",
                    ["Convert: $120$ cm. Add: $165$ cm $= 1.65$ m.",
                     "(Raw addition would claim $46.2$ — a shelf longer than a ger row.)"],
                    "$165$ cm",
                    ["Eq(120 + 45, 165)"]),
                wex("A $2$ L bottle loses $750$ ml. What remains?",
                    ["Convert: $2\\,000$ ml. Subtract: $1\\,250$ ml.",
                     "Receipt: $1\\,250 + 750 = 2\\,000$ ✓."],
                    "$1\\,250$ ml",
                    ["Eq(2000 - 750, 1250)", "Eq(1250 + 750, 2000)"]),
            ]),
            tryitset("Align, then compute", "Spot the mixed units before they meet.", [
                tp("$3.4$ km $+ 2\\,800$ m equals:",
                   ["$6.2$ km", "$2\\,803.4$ m", "$31.4$ km"],
                   "$3\\,400 + 2\\,800 = 6\\,200$ m $= 6.2$ km. (The wrong options added mixed units raw.)",
                   ["Eq(3400 + 2800, 6200)"]),
                tp("$1$ kg $- 350$ g equals:",
                   ["$650$ g", "$0.65$ g", "$999.65$ g"],
                   "$1\\,000 - 350 = 650$ g.",
                   ["Eq(1000 - 350, 650)"]),
                tp("A $1.5$ L jug plus a $250$ ml cup hold, together:",
                   ["$1\\,750$ ml", "$251.5$ ml", "$1\\,300$ ml"],
                   "$1\\,500 + 250 = 1\\,750$ ml.",
                   ["Eq(1500 + 250, 1750)"]),
            ]),
            tapq("Catch the sin", "A student computes a fence as $2$ m $+ 75$ cm $= 77$ cm... wait — $2 + 75 = 77$. The mistake:",
                 ["metres and centimetres met in one sum — convert first: $200 + 75 = 275$ cm",
                  "the addition itself is wrong",
                  "fences cannot be added",
                  "nothing — $77$ cm is right"],
                 "The $2$ was METRES: $200$ cm. Aligned, the fence is $275$ cm $= 2.75$ m — three and a half times the broken answer.",
                 ["Eq(200 + 75, 275)", "Ne(77, 275)"]),
            funfact("A spacecraft died of mixed units",
                    "In 1999 NASA's Mars Climate Orbiter burned up because one team computed thrust in metric units and another in imperial — nobody converted first. The cardinal sin of this lesson, at a cost of $327$ million dollars. Your fence arithmetic and their orbit arithmetic fail the same way."),
            withfig(teach("Concept B", "Multi-step, and the sensible finish", [
                "Real problems chain steps: convert, run the event queue, then CLIMB BACK to a sensible unit. Three parcels of $1$ kg $200$ g: $3 \\times 1\\,200 = 3\\,600$ g — reported as $3.6$ kg.",
                "Division joins in: a $3$ m ribbon into $40$ cm pieces — $300 \\div 40 = 7$ r $20$: seven pieces, $20$ cm left.",
                "The guardrail travels too: estimate in round units ($3$ parcels ≈ $1$ kg each ≈ $3.6$... about $3$–$4$ kg ✓) and the exact answer must land beside it.",
            ]), fig_barchart([("estimate", 12, C_NEUTRAL), ("exact", 11, C_ACCENT)], step=3, unit="m")),
            workedset("Full-shape problems",
                      "Convert → compute → report sensibly.", [
                wex("Three parcels of $1$ kg $200$ g — total, sensibly.",
                    ["$3 \\times 1\\,200 = 3\\,600$ g.",
                     "Climb: $3.6$ kg."],
                    "$3.6$ kg",
                    ["Eq(3*1200, 3600)"]),
                wex("A $3$ m ribbon cut into $40$ cm pieces — how many, what's left?",
                    ["$300 \\div 40 = 7$ r $20$.",
                     "Seven pieces, $20$ cm over; receipt $7 \\times 40 + 20 = 300$ ✓."],
                    "$7$ pieces, $20$ cm left",
                    ["Eq(7*40 + 20, 300)", "20 < 40"]),
            ]),
            tryitset("The whole shape", "All three parts, every time.", [
                tp("A $2$ L kettle gets two $750$ ml pours. Water still needed:",
                   ["$500$ ml", "$1\\,250$ ml", "$0.5$ ml"],
                   "$2 \\times 750 = 1\\,500$; $2\\,000 - 1\\,500 = 500$ ml.",
                   ["Eq(2*750, 1500)", "Eq(2000 - 1500, 500)"]),
                tp("A $5$ m rope loses three $120$ cm pieces. Remaining:",
                   ["$140$ cm", "$360$ cm", "$4.64$ m"],
                   "$3 \\times 120 = 360$; $500 - 360 = 140$ cm $= 1.4$ m.",
                   ["Eq(3*120, 360)", "Eq(500 - 360, 140)"]),
                tp("A $1.5$ kg bag of rice serves $75$ g portions. Full portions:",
                   ["$20$", "$2$", "$200$"],
                   "$1\\,500 \\div 75 = 20$; receipt $20 \\times 75 = 1\\,500$ ✓.",
                   ["Eq(20*75, 1500)"]),
            ]),
            tapq("Sensible reporting", "A hiking day totals $6\\,200$ m. The trail sign should say:",
                 ["$6.2$ km", "$6\\,200$ m", "$620\\,000$ cm", "$62$ km"],
                 "All but the last are true — but kilometres are how trails speak: $6.2$ km. Climbing to the audience's unit is part of the answer.",
                 ["Eq(Rational(6200,1000), Rational(62,10))"]),
            recap([
                "Convert FIRST — mixed units must never meet in one computation.",
                "The middle is familiar: queues, receipts, remainders — with unit names on.",
                "Finish on the ladder rung the situation speaks (3,600 g → 3.6 kg).",
                "Estimates in round units still guard every answer.",
            ]),
            tip("For each problem write the one unit you'll work in BEFORE reading the numbers again — the choice, made early, is the whole battle."),
            tryitset("Mixed practice", "Length, mass, capacity, time — full shapes.", [
                tp("A shelf needs boards of $85$ cm and $1.15$ m. Total wood:",
                   ["$2$ m", "$86.15$ cm", "$1.7$ m"],
                   "$85 + 115 = 200$ cm $= 2$ m exactly.",
                   ["Eq(85 + 115, 200)"]),
                tp("A $3$ kg sack of flour loses $750$ g to baking. Remaining:",
                   ["$2.25$ kg", "$2.75$ kg", "$22.5$ kg"],
                   "$3\\,000 - 750 = 2\\,250$ g $= 2.25$ kg.",
                   ["Eq(3000 - 750, 2250)", "Eq(Rational(2250,1000), Rational(225,100))"]),
                tp("Six glasses of $150$ ml drain a jug of $1$ L. The jug:",
                   ["runs short — the glasses need $900$ ml and a seventh won't fill",
                    "overflows",
                    "empties exactly"],
                   "$6 \\times 150 = 900 \\le 1\\,000$: the six pours fit with $100$ ml left — not enough for a seventh.",
                   ["Eq(6*150, 900)", "Eq(1000 - 900, 100)", "100 < 150"]),
                tp("A bus journey of $1$ h $35$ min starts at $7{:}40$. Arrival:",
                   ["$9{:}15$", "$8{:}75$", "$9{:}05$"],
                   "$+1$ h: $8{:}40$; $+35$: $75$ min $= 1$ h $15$ — $9{:}15$.",
                   ["Eq(40 + 35, 75)", "Eq(75, 60 + 15)"]),
                tp("Which is the BEST buy by mass: $2$ kg for the same price as $1\\,850$ g?",
                   ["the $2$ kg bag — $150$ g more for the same money", "the $1\\,850$ g bag", "they are identical"],
                   "$2\\,000 - 1\\,850 = 150$ g of free porridge.",
                   ["Eq(2000 - 1850, 150)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Measurement & Units\" — the whole topic",
                    "Four ladders, one commandment, and a spacecraft's worth of motivation. Two topics remain in Grade 5: shapes and their measurements, then data — both of which will use every unit in this one.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5me-pr1", "Convert $4$ m $7$ cm to centimetres, and $6\\,020$ m to kilometres-and-metres.",
             "$4 \\times 100 + 7 = 407$ cm. And $6\\,020 = 6 \\times 1\\,000 + 20$: $6$ km $20$ m.",
             ["Eq(4*100 + 7, 407)", "Eq(6*1000 + 20, 6020)"]),
        prob("g5me-pr2", "Which is longer: $3.05$ m or $340$ cm? By how much?",
             "$3.05$ m $= 305$ cm $< 340$ cm — the $340$ cm ribbon wins by $35$ cm.",
             ["Eq(Rational(305,100)*100, 305)", "Eq(340 - 305, 35)"]),
        prob("g5me-pr3", "Express $7$ kg $80$ g in grams, and $5\\,600$ ml in litres.",
             "$7\\,000 + 80 = 7\\,080$ g. And $5\\,600 \\div 1\\,000 = 5.6$ L.",
             ["Eq(7*1000 + 80, 7080)", "Eq(Rational(5600,1000), Rational(56,10))"]),
        prob("g5me-pr4", "How many $125$ ml cups does a $1$ L carton fill?",
             "$1\\,000 \\div 125 = 8$; receipt $8 \\times 125 = 1\\,000$ ✓.",
             ["Eq(8*125, 1000)"]),
        prob("g5me-pr5", "Convert $2\\frac{1}{2}$ h to minutes and $400$ s to minutes-and-seconds.",
             "$2\\frac{1}{2}$ h $= 150$ min. And $400 \\div 60 = 6$ r $40$: $6$ min $40$ s.",
             ["Eq(Rational(5,2)*60, 150)", "Eq(6*60 + 40, 400)", "40 < 60"]),
        prob("g5me-pr6", "A class runs $9{:}35$ to $11{:}10$. How long is it?",
             "Climb: $+25$ to $10{:}00$, $+60$, $+10$: $95$ min $= 1$ h $35$ min.",
             ["Eq(25 + 60 + 10, 95)", "Eq(95, 60 + 35)"]),
        prob("g5me-pr7", "A recipe mixes $1.2$ kg of flour with $300$ g of sugar. Total dry mass, sensibly?",
             "$1\\,200 + 300 = 1\\,500$ g $= 1.5$ kg.",
             ["Eq(1200 + 300, 1500)", "Eq(Rational(1500,1000), Rational(15,10))"]),
        prob("g5me-pr8", "A $4$ m plank is cut into $65$ cm shelves. How many shelves, and what offcut remains?",
             "$400 \\div 65 = 6$ r $10$: six shelves and a $10$ cm offcut. Receipt: $6 \\times 65 + 10 = 400$ ✓.",
             ["Eq(6*65 + 10, 400)", "10 < 65"]),
    ]


def test_bank():
    return [
        prob("g5me-x1", "Convert $8$ km $45$ m to metres, and $2\\,930$ cm to metres as a decimal.",
             "$8\\,000 + 45 = 8\\,045$ m. And $2\\,930 \\div 100 = 29.3$ m.",
             ["Eq(8*1000 + 45, 8045)", "Eq(Rational(2930,100), Rational(293,10))"]),
        prob("g5me-x2", "Order from lightest to heaviest: $0.9$ kg, $850$ g, $1.05$ kg.",
             "One unit: $900$ g, $850$ g, $1\\,050$ g — so $850$ g $< 0.9$ kg $< 1.05$ kg.",
             ["Eq(Rational(9,10)*1000, 900)", "850 < 900", "900 < 1050"]),
        prob("g5me-x3", "How many $250$ ml bottles fill a $3.5$ L container, and is anything left over?",
             "$3\\,500 \\div 250 = 14$ exactly — fourteen bottles, nothing over. Receipt: $14 \\times 250 = 3\\,500$ ✓.",
             ["Eq(14*250, 3500)"]),
        prob("g5me-x4", "Convert $1\\frac{3}{4}$ h to minutes, and explain why $1.75$ h is NOT $175$ min.",
             "$1\\frac{3}{4}$ h $= 60 + 45 = 105$ min. The fraction multiplies SIXTY ($\\frac{3}{4} \\times 60 = 45$), not a hundred — $175$ is the base-ten reflex on a base-sixty ladder.",
             ["Eq(60 + 45, 105)", "Eq(Rational(175,100)*60, 105)", "Ne(105, 175)"]),
        prob("g5me-x5", "A train departs $13{:}50$ and arrives $16{:}25$. How long is the journey?",
             "Climb: $+10$ to $14{:}00$, $+120$ to $16{:}00$, $+25$: $155$ min $= 2$ h $35$ min.",
             ["Eq(10 + 120 + 25, 155)", "Eq(155, 2*60 + 35)"]),
        prob("g5me-x6", ("A herder's cart carries two churns of $15.5$ L each and one of "
                         "$8\\,750$ ml. What is the total, in litres — and how far below "
                         "the cart's $40$ L limit is it?"),
             "One unit: $15\\,500 + 15\\,500 + 8\\,750 = 39\\,750$ ml $= 39.75$ L. Below the limit by $40 - 39.75 = 0.25$ L ($250$ ml).",
             ["Eq(15500 + 15500 + 8750, 39750)",
              "Eq(Rational(39750,1000), Rational(3975,100))",
              "Eq(40000 - 39750, 250)"]),
    ]


def main():
    topic = {
        "slug": "measurement-and-units",
        "title": "Measurement & Units",
        "grade": 5,
        "status": "published",
        "blurb": ("The metric ladders for length, mass and capacity, the "
                  "base-sixty ladder of time, elapsed-time reckoning, and "
                  "measurement problems solved convert-first."),
        "lessons": [
            lesson_length(),
            lesson_mass_capacity(),
            lesson_time_units(),
            lesson_elapsed(),
            lesson_word_problems(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "measurement-and-units.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
