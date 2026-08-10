#!/usr/bin/env python3
"""SAT Math — Problem-Solving and Data Analysis, Units 1-2.

Builds two unit files:
  data/genmath/sat/ratios-rates-proportions-units.json
  data/genmath/sat/percentages.json

Two units in one script because they share a spine — everything here is a
multiplicative comparison — and because the College Board's subtopics in this
domain are narrower than in Algebra: 5 to 7 questions cover all seven of them.

Run: python3 scripts/sat/build_psda_1_2.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
RATIO_TAG = {"text": "sat-ratios-rates", "mono": True}
PCT_TAG = {"text": "sat-percentages", "mono": True}


def _b(tag, level):
    return [tag, {"text": level}]


# ===========================================================================
# UNIT 1 — Ratios, rates, proportional relationships and units
# ===========================================================================

def lesson_ratios():
    worked = [
        problem(
            "sat-rr1-w1",
            "In a bag of red and blue marbles the ratio of red to blue is $3 : 5$. If there "
            "are $96$ marbles in total, how many are red?",
            "**Answer.** $36$.  \n"
            "A ratio of $3 : 5$ means the marbles come in identical groups of $8$ — three red "
            "and five blue in each group. So the whole is divided into\n"
            "$$3 + 5 = 8 \\text{ parts}$$\n"
            "and each part is\n"
            "$$\\frac{96}{8} = 12 \\text{ marbles}$$\n"
            "Red takes three of those parts:\n"
            "$$3 \\times 12 = 36$$\n"
            "Check: blue is $5 \\times 12 = 60$, and $36 + 60 = 96$. The ratio "
            "$36 : 60$ reduces to $3 : 5$.  \n"
            "The trap is dividing by $3$ or by $5$ instead of by the TOTAL number of parts. "
            "$\\frac{96}{5}$ and $\\frac{96}{3}$ are both on the option list, and neither "
            "means anything here.",
            [
                "Eq(Rational(96, 3 + 5), 12)",
                "Eq(3*12, 36)",
                "Eq(5*12, 60)",
                "Eq(36 + 60, 96)",
                "Eq(Rational(36, 60), Rational(3, 5))",
            ],
        ),
        problem(
            "sat-rr1-w2",
            "A printer produces $14$ pages every $8$ seconds. At this rate, how many pages "
            "does it produce in $3$ minutes?",
            "**Answer.** $315$.  \n"
            "Two things have to line up: the rate and the time must use the same unit. "
            "Convert the three minutes first:\n"
            "$$3 \\text{ minutes} = 180 \\text{ seconds}$$\n"
            "Now set up a proportion, keeping pages above and seconds below on BOTH sides:\n"
            "$$\\frac{14 \\text{ pages}}{8 \\text{ s}} = \\frac{p}{180 \\text{ s}}$$\n"
            "Cross-multiply:\n"
            "$$8p = 14 \\times 180 = 2520$$\n"
            "$$p = 315$$\n"
            "Check by rate: $\\frac{14}{8} = 1.75$ pages per second, and "
            "$1.75 \\times 180 = 315$.  \n"
            "Forgetting to convert minutes to seconds gives $\\frac{14 \\times 3}{8}$, about "
            "$5$ pages — a number so small it should look wrong immediately. Checking that "
            "your answer is the right ORDER of magnitude catches most unit errors.",
            [
                "Eq(3*60, 180)",
                "Eq(Rational(14, 8), Rational(7, 4))",
                "Eq(Rational(7,4)*180, 315)",
                "Eq(8*315, 14*180)",
            ],
        ),
        problem(
            "sat-rr1-w3",
            "A recipe uses $250$ millilitres of milk for every $400$ grams of flour. A baker "
            "uses $1.4$ kilograms of flour. How many litres of milk are needed?",
            "**Answer.** $0.875$ litres.  \n"
            "Convert both quantities into matching units before setting anything up. "
            "$1.4$ kilograms is $1400$ grams:\n"
            "$$\\frac{250 \\text{ mL}}{400 \\text{ g}} = \\frac{m}{1400 \\text{ g}}$$\n"
            "$$400m = 250 \\times 1400 = 350\\,000$$\n"
            "$$m = 875 \\text{ mL}$$\n"
            "The question asks for LITRES, so convert once more:\n"
            "$$875 \\text{ mL} = 0.875 \\text{ L}$$\n"
            "Check the proportion: $\\frac{250}{400} = 0.625$ mL per gram, and "
            "$0.625 \\times 1400 = 875$.  \n"
            "Two conversions, one at each end. Answering $875$ is right arithmetic in the "
            "wrong unit, and it is always an option.",
            [
                "Eq(Rational(14,10)*1000, 1400)",
                "Eq(400*875, 250*1400)",
                "Eq(Rational(875, 1000), Rational(875,1000))",
                "Eq(Rational(250,400)*1400, 875)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-rr1-t1",
            "The ratio of cats to dogs at a shelter is $4 : 7$. If there are $28$ dogs, how "
            "many cats are there?",
            "**Answer.** $16$. Each part is $\\frac{28}{7} = 4$ animals, and cats take four "
            "parts: $4 \\times 4 = 16$. Check: $16 : 28$ reduces to $4 : 7$.",
            ["Eq(Rational(28,7), 4)", "Eq(4*4, 16)", "Eq(Rational(16,28), Rational(4,7))"],
        ),
        problem(
            "sat-rr1-t2",
            "A car travels $246$ kilometres in $3$ hours. At this rate, how far does it "
            "travel in $50$ minutes?",
            "**Answer.** $\\dfrac{205}{3}$ kilometres, about $68.3$. The rate is "
            "$\\frac{246}{3} = 82$ kilometres per hour, and $50$ minutes is $\\frac{5}{6}$ of "
            "an hour, so the distance is $82 \\times \\frac{5}{6} = \\frac{410}{6} = "
            "\\frac{205}{3}$.",
            [
                "Eq(Rational(246,3), 82)",
                "Eq(Rational(50,60), Rational(5,6))",
                "Eq(82*Rational(5,6), Rational(205,3))",
            ],
        ),
        problem(
            "sat-rr1-t3",
            "In a mixture the ratio of sand to cement to gravel is $5 : 2 : 3$. If the "
            "mixture weighs $60$ kilograms, how much gravel does it contain?",
            "**Answer.** $18$ kilograms. The parts total $5 + 2 + 3 = 10$, so each part is "
            "$6$ kilograms, and gravel takes three: $3 \\times 6 = 18$.",
            ["Eq(5 + 2 + 3, 10)", "Eq(Rational(60,10), 6)", "Eq(3*6, 18)"],
        ),
        problem(
            "sat-rr1-t4",
            "A machine fills $900$ bottles per hour. How many bottles does it fill in $25$ "
            "minutes?",
            "**Answer.** $375$. In one minute it fills $\\frac{900}{60} = 15$ bottles, so in "
            "$25$ minutes it fills $15 \\times 25 = 375$.",
            ["Eq(Rational(900,60), 15)", "Eq(15*25, 375)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Ratios, rates, proportional relationships and units",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "This subtopic is usually 1 or 2 of them, and they are rarely hard.",
                "Prerequisite: fractions, and solving a linear equation.",
                "Almost every lost point here is a unit that was never converted.",
            ],
        },
        {
            "kind": "teach",
            "title": "A ratio counts parts, not things",
            "body": "A ratio of $3 : 5$ does not mean three of one and five of the other — it "
                    "means the whole splits into identical groups, each holding three of one "
                    "and five of the other. The total number of PARTS is $3 + 5 = 8$, and "
                    "dividing the total by that gives the size of one part. Everything else "
                    "follows by multiplying.",
        },
        {
            "kind": "ratioTable",
            "title": "Scale a ratio without losing it",
            "teach": "Multiply both sides of a ratio by the same number and it describes the "
                     "same mixture. Slide through the multiples and watch the pair change "
                     "while the ratio does not.",
            "config": {
                "a": 3,
                "b": 5,
                "maxCols": 6,
                "tokenA": {"label": "red marble", "plural": "red marbles", "color": "#d1495b"},
                "tokenB": {"label": "blue marble", "plural": "blue marbles", "color": "#3a6ea5"},
            },
        },
        {"kind": "worked", "title": "Splitting a total by a ratio", "problemId": "sat-rr1-w1"},
        {
            "kind": "tapQuestion",
            "title": "How many parts?",
            "prompt": "The ratio of boys to girls in a class is $2 : 3$ and there are $30$ "
                      "students. How many are boys?",
            "options": ["$12$", "$15$", "$20$", "$10$"],
            "correctIndex": 0,
            "explanation": "The parts total $2 + 3 = 5$, so each part is $\\frac{30}{5} = 6$ "
                           "students and boys take two: $12$. Dividing by $2$ or by $3$ "
                           "instead of by $5$ gives $15$ and $10$, both listed.",
            "check": ["Eq(Rational(30, 2 + 3), 6)", "Eq(2*6, 12)", "Eq(3*6, 18)", "Eq(12 + 18, 30)"],
        },
        {
            "kind": "teach",
            "title": "Rates and the unit trap",
            "beats": [
                "A rate compares two DIFFERENT quantities: pages per second, kilometres per hour.",
                "Before using a rate, make the units on both sides match.",
                "Set the proportion up with the same quantity on top on both sides.",
                "Then check the answer's ORDER of magnitude — a missed conversion is usually obvious.",
            ],
        },
        {"kind": "worked", "title": "A rate with mismatched units", "problemId": "sat-rr1-w2"},
        {
            "kind": "tip",
            "title": "Convert at both ends",
            "body": "The hard versions of these questions convert twice: the quantity going in "
                    "is in the wrong unit AND the answer is wanted in a different one. Write "
                    "down what unit you are in at every line. Getting $875$ millilitres when "
                    "the question asked for litres is correct arithmetic that scores zero.",
        },
        {"kind": "worked", "title": "Two conversions in one question", "problemId": "sat-rr1-w3"},
        {"kind": "tryIt", "title": "Your turn: one side given", "problemId": "sat-rr1-t1"},
        {"kind": "tryIt", "title": "Your turn: match the time units", "problemId": "sat-rr1-t2"},
        {"kind": "tryIt", "title": "Your turn: a three-part ratio", "problemId": "sat-rr1-t3"},
        {"kind": "tryIt", "title": "Your turn: per hour to per minute", "problemId": "sat-rr1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Add the parts of a ratio and divide the total by that sum to size one part.",
                "A ratio given for one side only still needs the part size first.",
                "Match units before setting up a proportion, not after.",
                "Convert the answer into the unit the question asked for.",
                "Sanity-check the magnitude — a missed conversion is off by a factor of 60 or 1000.",
            ],
        },
    ]

    return lesson(
        slug="ratios-rates-and-units",
        title="Ratios, Rates and Getting the Units Right",
        concrete=(
            "Concrete mixed $5 : 2 : 3$ sand to cement to gravel is the same concrete whether "
            "you make a bucket or a lorry-load. The ratio is not an amount — it is a recipe, "
            "and the SAT's questions are all about turning a recipe into an amount, or back."
        ),
        objective=(
            "Split a total by a ratio, use a rate to convert between quantities, and carry "
            "units correctly through both ends of a conversion."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Ratios, rates, proportional "
            "relationships, and units*, in the **Problem-Solving and Data Analysis** domain. "
            "That domain is 5 to 7 of the 44 questions in total, and this subtopic is usually "
            "one or two of them.",
            "A ratio describes PARTS, not amounts. $3 : 5$ means the whole divides into "
            "identical groups of $3 + 5 = 8$ parts. Divide the total by the number of parts to "
            "find how big one part is, then multiply. Dividing by one side of the ratio "
            "instead of by their sum is the commonest error, and both wrong answers appear as "
            "options.",
            "A rate compares two different quantities — pages per second, kilometres per hour, "
            "millilitres per gram. Using one is a proportion, with the same quantity on top on "
            "both sides. The only real difficulty is units: the rate and the quantity you "
            "apply it to must be measured the same way.",
            "**The test's angle.** Units, at both ends. The harder items give you a quantity "
            "in the wrong unit AND ask for the answer in a third one — grams in, kilograms "
            "given, litres wanted. Write the unit down on every line. A missed conversion is "
            "usually off by a factor of $60$ or $1000$, so a quick sanity check on the "
            "magnitude of your answer catches almost all of them.",
        ],
        key_idea=(
            "Add the parts of a ratio and divide the total by that sum. For a rate, match the "
            "units first, set up the proportion with the same quantity on top, and convert the "
            "answer into whatever the question asked for."
        ),
        facts=[
            fact(
                "Splitting by a ratio",
                "a : b \\;\\Longrightarrow\\; \\text{one part} = \\frac{\\text{total}}{a + b}",
                "The denominator is the SUM of the parts, never one side of the ratio.",
            ),
            fact(
                "Proportion",
                "\\frac{p_1}{q_1} = \\frac{p_2}{q_2} \\;\\Longrightarrow\\; p_1 q_2 = p_2 q_1",
                "Same quantity on top on both sides, in the same units.",
            ),
            fact(
                "Common conversions",
                "1 \\text{ h} = 60 \\text{ min}, \\quad 1 \\text{ kg} = 1000 \\text{ g}, \\quad 1 \\text{ L} = 1000 \\text{ mL}",
                "The SAT gives unusual conversions in the question; these it assumes.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Dividing the total by one side of a ratio instead of by the sum.",
                "For $3 : 5$ with a total of $96$, one part is $\\frac{96}{8} = 12$, not "
                "$\\frac{96}{3}$ or $\\frac{96}{5}$.",
            ),
            mistake(
                "Using a rate without matching the units.",
                "A rate in pages per SECOND cannot be multiplied by a time in minutes. Convert "
                "first.",
            ),
            mistake(
                "Answering in the unit you computed in rather than the one asked for.",
                "$875$ millilitres is $0.875$ litres. The unconverted number is always an "
                "option.",
            ),
            mistake(
                "Inverting a proportion by putting different quantities on top.",
                "If pages are on top on the left, pages go on top on the right too. Otherwise "
                "the cross-multiplication is meaningless.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_proportional():
    worked = [
        problem(
            "sat-rr2-w1",
            "The table shows the cost of buying different numbers of identical tickets.\n\n"
            "| Tickets | Cost (dollars) |\n| --- | --- |\n| $4$ | $30$ |\n| $10$ | $75$ |\n"
            "| $16$ | $120$ |\n\n"
            "Is the cost proportional to the number of tickets, and what would $25$ tickets "
            "cost?",
            "**Answer.** Yes, it is proportional; $25$ tickets cost $\\$187.50$.  \n"
            "A relationship is PROPORTIONAL when the ratio of the two quantities is the same "
            "in every row — equivalently, when doubling one doubles the other, and zero of one "
            "means zero of the other.\n"
            "$$\\frac{30}{4} = 7.5, \\qquad \\frac{75}{10} = 7.5, \\qquad \\frac{120}{16} = 7.5$$\n"
            "Every row gives $7.5$ dollars per ticket, so the cost is proportional with "
            "constant of proportionality $7.5$:\n"
            "$$C = 7.5n$$\n"
            "$$C(25) = 7.5 \\times 25 = 187.5$$\n"
            "Note what proportional rules OUT. If there were a booking fee — say "
            "$C = 7.5n + 5$ — the ratios would not match: $\\frac{35}{4} = 8.75$ but "
            "$\\frac{80}{10} = 8$. A proportional relationship is a straight line THROUGH THE "
            "ORIGIN, and any fixed fee destroys it.",
            [
                "Eq(Rational(30,4), Rational(15,2))",
                "Eq(Rational(75,10), Rational(15,2))",
                "Eq(Rational(120,16), Rational(15,2))",
                "Eq(Rational(15,2)*25, Rational(375,2))",
            ],
        ),
        problem(
            "sat-rr2-w2",
            "On a map, $2.5$ centimetres represents $40$ kilometres. Two towns are $17$ "
            "centimetres apart on the map. How far apart are they in reality?",
            "**Answer.** $272$ kilometres.  \n"
            "Map scales are proportional relationships. Find the constant first — how many "
            "kilometres one centimetre represents:\n"
            "$$\\frac{40}{2.5} = 16 \\text{ km per cm}$$\n"
            "Then multiply:\n"
            "$$17 \\times 16 = 272 \\text{ km}$$\n"
            "Check with a proportion instead: $\\frac{2.5}{40} = \\frac{17}{d}$ gives "
            "$2.5d = 680$, so $d = 272$. Same answer, and it is worth being able to run both "
            "ways — the constant route is faster when you need several answers from one scale.",
            [
                "Eq(Rational(40, Rational(25,10)), 16)",
                "Eq(17*16, 272)",
                "Eq(Rational(25,10)*272, 40*17)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-rr2-t1",
            "The cost $C$ of $n$ identical items is proportional to $n$, and $6$ items cost "
            "$\\$27$. What do $14$ items cost?",
            "**Answer.** $\\$63$. The constant is $\\frac{27}{6} = 4.5$ dollars per item, so "
            "$14$ items cost $14 \\times 4.5 = 63$.",
            ["Eq(Rational(27,6), Rational(9,2))", "Eq(14*Rational(9,2), 63)"],
        ),
        problem(
            "sat-rr2-t2",
            "Which table shows a proportional relationship: one with $(2, 5)$ and $(4, 10)$, "
            "or one with $(2, 5)$ and $(4, 9)$?",
            "**Answer.** The first. Its ratios are $\\frac{5}{2} = 2.5$ and "
            "$\\frac{10}{4} = 2.5$ — equal, so proportional. The second gives $2.5$ and "
            "$2.25$, which differ, so it is linear but not proportional; its graph misses the "
            "origin.",
            [
                "Eq(Rational(5,2), Rational(10,4))",
                "Ne(Rational(5,2), Rational(9,4))",
            ],
        ),
        problem(
            "sat-rr2-t3",
            "A scale drawing uses $3$ centimetres for every $12$ metres. A wall is $7.5$ "
            "centimetres long on the drawing. How long is the real wall?",
            "**Answer.** $30$ metres. One centimetre represents $\\frac{12}{3} = 4$ metres, so "
            "$7.5 \\times 4 = 30$.",
            ["Eq(Rational(12,3), 4)", "Eq(Rational(75,10)*4, 30)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Proportional is stricter than linear",
            "body": "Two quantities are PROPORTIONAL when their ratio is the same every time — "
                    "double one and the other doubles, and zero of one means zero of the "
                    "other. On a graph that is a straight line THROUGH THE ORIGIN. A line "
                    "that misses the origin, like a cost with a booking fee, is linear but not "
                    "proportional, and the SAT tests that distinction directly.",
        },
        {
            "kind": "proportionBuilder",
            "title": "The constant of proportionality",
            "teach": "Set the two known quantities and read off the constant — how much of one "
                     "goes with a single unit of the other. Once you have it, every other "
                     "question about that relationship is one multiplication.",
            "config": {
                "aLabel": "tickets",
                "bLabel": "dollars",
                "a": 4,
                "b": 30,
                "knownSide": "a",
                "knownValue": 10,
                "tokenA": {"label": "ticket", "plural": "tickets", "color": "#3a6ea5"},
                "tokenB": {"label": "dollar", "plural": "dollars", "color": "#2a9d8f"},
            },
        },
        {"kind": "worked", "title": "Testing a table for proportionality", "problemId": "sat-rr2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Proportional or just linear?",
            "prompt": "A taxi charges $\\$4$ plus $\\$2$ per kilometre. Is the fare "
                      "proportional to the distance?",
            "options": [
                "No — a zero-kilometre ride still costs $\\$4$",
                "Yes — the fare rises steadily with distance",
                "Yes — the rate per kilometre is constant",
                "Only for rides longer than $2$ kilometres",
            ],
            "correctIndex": 0,
            "explanation": "Proportional requires that zero of one gives zero of the other. "
                           "Here $F(0) = 4$, so the graph misses the origin. The ratios "
                           "confirm it: $\\frac{6}{1} = 6$ but $\\frac{8}{2} = 4$. A steady "
                           "rise makes it LINEAR, which is not the same thing.",
            "check": [
                "Eq(2*0 + 4, 4)",
                "Eq(Rational(2*1 + 4, 1), 6)",
                "Eq(Rational(2*2 + 4, 2), 4)",
                "Ne(6, 4)",
            ],
        },
        {
            "kind": "tip",
            "title": "Find the constant, then multiply",
            "body": "For any proportional relationship, divide once to get the constant — "
                    "dollars per ticket, kilometres per centimetre — and then every further "
                    "question is a single multiplication. Setting up a fresh proportion each "
                    "time works too, but it is slower and gives cross-multiplication more "
                    "chances to go wrong.",
        },
        {"kind": "worked", "title": "A map scale", "problemId": "sat-rr2-w2"},
        {"kind": "tryIt", "title": "Your turn: scale up a cost", "problemId": "sat-rr2-t1"},
        {"kind": "tryIt", "title": "Your turn: which table?", "problemId": "sat-rr2-t2"},
        {"kind": "tryIt", "title": "Your turn: a scale drawing", "problemId": "sat-rr2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Proportional means the ratio is constant AND the graph passes through the origin.",
                "A fixed fee makes a relationship linear but not proportional.",
                "Test a table by dividing each output by its input — all the answers must match.",
                "Find the constant once, then answer everything else by multiplying.",
                "Map and drawing scales are proportional relationships in disguise.",
            ],
        },
    ]

    return lesson(
        slug="proportional-relationships",
        title="Proportional Relationships and Scales",
        concrete=(
            "Double the tickets and you double the bill — unless there is a booking fee, and "
            "then you do not. That single difference is what separates a proportional "
            "relationship from a merely linear one, and the SAT asks about it more often than "
            "students expect."
        ),
        objective=(
            "Recognise a proportional relationship from a table, a graph or a description, "
            "find its constant of proportionality, and use it — including for map and drawing "
            "scales."
        ),
        concept=[
            "**Skill card.** Still *Ratios, rates, proportional relationships, and units*, in "
            "the **Problem-Solving and Data Analysis** domain. The proportional-versus-linear "
            "distinction is a favourite because it costs nothing to compute and everything to "
            "misunderstand.",
            "Two quantities are proportional when their ratio is the same every time. "
            "Equivalently: doubling one doubles the other, and zero of one gives zero of the "
            "other. On a graph that is a straight line through the ORIGIN, with equation "
            "$y = kx$ where $k$ is the constant of proportionality.",
            "That is stricter than linear. A taxi fare of $\\$4$ plus $\\$2$ per kilometre "
            "rises steadily and graphs as a straight line — but it is $\\$4$ for zero "
            "kilometres, so the line misses the origin and the ratios do not match. Linear, "
            "not proportional.",
            "**The test's angle.** Find the constant once and everything else is a "
            "multiplication. Divide one output by its input — dollars per ticket, kilometres "
            "per centimetre — and use that number for every subsequent question about the same "
            "relationship. It is faster than setting up a fresh proportion each time and gives "
            "cross-multiplication fewer chances to go wrong.",
        ],
        key_idea=(
            "Proportional means constant ratio and a graph through the origin. Find the "
            "constant once, then multiply."
        ),
        facts=[
            fact(
                "Proportional relationship",
                "y = kx, \\qquad k = \\frac{y}{x} \\text{ for every pair}",
                "Passes through the origin. Any non-zero intercept breaks proportionality.",
            ),
            fact(
                "Testing a table",
                "\\frac{y_1}{x_1} = \\frac{y_2}{x_2} = \\cdots",
                "All the ratios must agree. One mismatch is enough to rule it out.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Calling any straight-line relationship proportional.",
                "It must also pass through the origin. A fixed fee makes it linear but not "
                "proportional.",
            ),
            mistake(
                "Testing only two rows of a table.",
                "Every row's ratio must match. A table can agree on two rows and fail on the "
                "third.",
            ),
            mistake(
                "Inverting the constant of proportionality.",
                "If the scale is $2.5$ cm to $40$ km, one centimetre is $16$ km, not "
                "$\\frac{1}{16}$. Check which way the question needs it.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


RATIO_PRACTICE = [
    problem(
        "sat-rr-p01",
        "The ratio of red to green sweets is $2 : 7$ and there are $63$ green sweets. How "
        "many red sweets are there?",
        "**Answer.** $18$. Each part is $\\frac{63}{7} = 9$ sweets, and red takes two parts.",
        ["Eq(Rational(63,7), 9)", "Eq(2*9, 18)", "Eq(Rational(18,63), Rational(2,7))"],
        badges=_b(RATIO_TAG, "Easy"),
    ),
    problem(
        "sat-rr-p02",
        "A tap fills $18$ litres in $4$ minutes. How many litres does it fill in $10$ minutes?",
        "**Answer.** $45$. The rate is $\\frac{18}{4} = 4.5$ litres per minute, so ten minutes "
        "gives $45$ litres.",
        ["Eq(Rational(18,4), Rational(9,2))", "Eq(Rational(9,2)*10, 45)"],
        badges=_b(RATIO_TAG, "Easy"),
    ),
    problem(
        "sat-rr-p03",
        "A recipe for $6$ people needs $450$ grams of rice. How much rice is needed for $10$ "
        "people?",
        "**Answer.** $750$ grams. Per person it is $\\frac{450}{6} = 75$ grams, so ten people "
        "need $750$ grams.",
        ["Eq(Rational(450,6), 75)", "Eq(75*10, 750)"],
        badges=_b(RATIO_TAG, "Easy"),
    ),
    problem(
        "sat-rr-p04",
        "A car uses $7$ litres of fuel per $100$ kilometres. How many litres does it use on a "
        "journey of $340$ kilometres?",
        "**Answer.** $23.8$ litres. The rate is $0.07$ litres per kilometre, and "
        "$0.07 \\times 340 = 23.8$.",
        ["Eq(Rational(7,100)*340, Rational(238,10))"],
        badges=_b(RATIO_TAG, "Medium"),
    ),
    problem(
        "sat-rr-p05",
        "In a mixture the ratio of water to syrup is $9 : 2$. If the mixture is $2.2$ litres, "
        "how many millilitres of syrup does it contain?",
        "**Answer.** $400$ millilitres. Convert first: $2.2$ litres is $2200$ millilitres. The "
        "parts total $11$, so each part is $200$ mL, and syrup takes two.",
        [
            "Eq(Rational(22,10)*1000, 2200)",
            "Eq(Rational(2200, 9 + 2), 200)",
            "Eq(2*200, 400)",
        ],
        badges=_b(RATIO_TAG, "Hard"),
    ),
    problem(
        "sat-rr-p06",
        "The table shows a relationship.\n\n"
        "| $x$ | $y$ |\n| --- | --- |\n| $3$ | $12$ |\n| $5$ | $20$ |\n| $8$ | $32$ |\n\n"
        "Is $y$ proportional to $x$, and what is the constant?",
        "**Answer.** Yes; the constant is $4$. Every ratio $\\frac{y}{x}$ equals $4$, so "
        "$y = 4x$ and the graph passes through the origin.",
        [
            "Eq(Rational(12,3), 4)",
            "Eq(Rational(20,5), 4)",
            "Eq(Rational(32,8), 4)",
        ],
        badges=_b(RATIO_TAG, "Medium"),
    ),
    problem(
        "sat-rr-p07",
        "On a plan, $4$ centimetres represents $10$ metres. A room is $22$ metres long. How "
        "long is it on the plan, in centimetres?",
        "**Answer.** $8.8$ centimetres. One metre is $\\frac{4}{10} = 0.4$ centimetres on the "
        "plan, so $22 \\times 0.4 = 8.8$. Running the scale the other way — multiplying by "
        "$2.5$ — gives $55$, a listed option.",
        ["Eq(Rational(4,10), Rational(2,5))", "Eq(22*Rational(2,5), Rational(44,5))"],
        badges=_b(RATIO_TAG, "Medium"),
    ),
    problem(
        "sat-rr-p08",
        "A pump moves $2{,}400$ litres per hour. How many litres does it move in $45$ seconds?",
        "**Answer.** $30$ litres. Per second the pump moves "
        "$\\frac{2400}{3600} = \\frac{2}{3}$ litres, and $45 \\times \\frac{2}{3} = 30$.",
        [
            "Eq(60*60, 3600)",
            "Eq(Rational(2400,3600), Rational(2,3))",
            "Eq(45*Rational(2,3), 30)",
        ],
        badges=_b(RATIO_TAG, "Hard"),
    ),
]

RATIO_TEST = [
    problem(
        "sat-rr-x01",
        "The ratio of teachers to students at a school is $1 : 18$. If there are $54$ "
        "teachers, how many students are there?",
        "**Answer.** $972$. Each teacher corresponds to $18$ students, so "
        "$54 \\times 18 = 972$.",
        ["Eq(54*18, 972)", "Eq(Rational(54,972), Rational(1,18))"],
        badges=_b(RATIO_TAG, "Easy"),
    ),
    problem(
        "sat-rr-x02",
        "A worker earns $\\$102$ for $8$ hours. At the same rate, how much do they earn for "
        "$14$ hours?",
        "**Answer.** $\\$178.50$. The rate is $\\frac{102}{8} = 12.75$ dollars per hour, and "
        "$14 \\times 12.75 = 178.5$.",
        ["Eq(Rational(102,8), Rational(51,4))", "Eq(14*Rational(51,4), Rational(357,2))"],
        badges=_b(RATIO_TAG, "Medium"),
    ),
    problem(
        "sat-rr-x03",
        "In a class the ratio of those who walk to those who cycle to those who ride the bus "
        "is $4 : 3 : 5$. There are $36$ students. How many cycle?",
        "**Answer.** $9$. The parts total $12$, so each part is $3$ students and cycling takes "
        "three parts.",
        ["Eq(4 + 3 + 5, 12)", "Eq(Rational(36,12), 3)", "Eq(3*3, 9)"],
        badges=_b(RATIO_TAG, "Medium"),
    ),
    problem(
        "sat-rr-x04",
        "A printer uses $1$ cartridge every $1{,}250$ pages. How many cartridges are needed "
        "for $8{,}000$ pages?",
        "**Answer.** $6.4$, so $7$ cartridges must be bought. The arithmetic gives "
        "$\\frac{8000}{1250} = 6.4$; since a cartridge cannot be part-bought and running out "
        "is not an option, this is a case where you round UP. Contrast the budget questions in "
        "Algebra Unit 5, where an 'at most' limit forces rounding down.",
        ["Eq(Rational(8000,1250), Rational(32,5))", "6*1250 < 8000", "7*1250 > 8000"],
        badges=_b(RATIO_TAG, "Hard"),
    ),
    problem(
        "sat-rr-x05",
        "A machine produces $3$ items every $8$ seconds. How many items does it produce in "
        "$2$ hours?",
        "**Answer.** $2{,}700$. Two hours is $7{,}200$ seconds, and "
        "$\\frac{7200}{8} = 900$ groups of $8$ seconds, each giving $3$ items: "
        "$900 \\times 3 = 2700$.",
        ["Eq(2*3600, 7200)", "Eq(Rational(7200,8), 900)", "Eq(900*3, 2700)"],
        badges=_b(RATIO_TAG, "Medium"),
    ),
    problem(
        "sat-rr-x06",
        "The quantity $y$ is proportional to $x$, and $y = 21$ when $x = 6$. What is $y$ when "
        "$x = 10$?",
        "**Answer.** $35$. The constant is $\\frac{21}{6} = 3.5$, so $y = 3.5 \\times 10 = 35$.",
        ["Eq(Rational(21,6), Rational(7,2))", "Eq(Rational(7,2)*10, 35)"],
        badges=_b(RATIO_TAG, "Medium"),
    ),
]


# ===========================================================================
# UNIT 2 — Percentages
# ===========================================================================

def lesson_percent_basics():
    worked = [
        problem(
            "sat-pc1-w1",
            "A jacket priced at $\\$85$ is reduced by $30\\%$. What is the sale price?",
            "**Answer.** $\\$59.50$.  \n"
            "There are two routes and the second is faster.  \n"
            "The long way: $30\\%$ of $85$ is $0.30 \\times 85 = 25.50$, so the sale price is "
            "$85 - 25.50 = 59.50$.  \n"
            "The one-step way: a $30\\%$ discount leaves $70\\%$, so multiply once:\n"
            "$$0.70 \\times 85 = 59.50$$\n"
            "That single multiplier is worth the habit. It halves the arithmetic, and — more "
            "importantly — it is the only practical way to handle two changes in a row, which "
            "the harder questions always involve.",
            [
                "Eq(Rational(30,100)*85, Rational(255,10))",
                "Eq(85 - Rational(255,10), Rational(595,10))",
                "Eq(Rational(70,100)*85, Rational(595,10))",
            ],
        ),
        problem(
            "sat-pc1-w2",
            "After a $20\\%$ discount, a coat costs $\\$96$. What was the original price?",
            "**Answer.** $\\$120$.  \n"
            "The discount was taken off the ORIGINAL price, which is what you are looking for. "
            "Call it $p$. A $20\\%$ discount multiplies by $0.80$:\n"
            "$$0.80p = 96$$\n"
            "$$p = \\frac{96}{0.80} = 120$$\n"
            "Check: $20\\%$ of $120$ is $24$, and $120 - 24 = 96$.  \n"
            "The trap is adding $20\\%$ back onto $\\$96$, which gives $\\$115.20$ — not "
            "$\\$120$. The reason it fails is that $20\\%$ of the SMALLER number is a smaller "
            "amount than $20\\%$ of the larger one. To undo a percentage change you DIVIDE by "
            "the multiplier; you never apply the reverse percentage.",
            [
                "Eq(Rational(80,100)*120, 96)",
                "Eq(120 - Rational(20,100)*120, 96)",
                "Eq(96 + Rational(20,100)*96, Rational(1152,10))",
                "Ne(Rational(1152,10), 120)",
            ],
        ),
        problem(
            "sat-pc1-w3",
            "A share price rises by $25\\%$ and then falls by $20\\%$. What is the overall "
            "percentage change?",
            "**Answer.** No change at all.  \n"
            "Percentages do not add. Each change is a MULTIPLIER, and successive changes "
            "multiply:\n"
            "$$1.25 \\times 0.80 = 1.00$$\n"
            "The price ends exactly where it started, so the overall change is $0\\%$.  \n"
            "Trace it with a real number to see why. Starting at $\\$200$: a $25\\%$ rise adds "
            "$\\$50$, giving $\\$250$; a $20\\%$ fall on $\\$250$ subtracts $\\$50$, giving "
            "$\\$200$. The two percentages are of DIFFERENT amounts, which is exactly why "
            "$+25\\%$ and $-20\\%$ do not sum to $+5\\%$.  \n"
            "Adding them is the standard wrong answer, and it is wrong even in sign for many "
            "pairs.",
            [
                "Eq(Rational(125,100)*Rational(80,100), 1)",
                "Eq(200*Rational(125,100), 250)",
                "Eq(250*Rational(80,100), 200)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-pc1-t1",
            "What is $15\\%$ of $240$?",
            "**Answer.** $36$. $0.15 \\times 240 = 36$. A useful check: $10\\%$ is $24$ and "
            "$5\\%$ is half of that, $12$, and $24 + 12 = 36$.",
            ["Eq(Rational(15,100)*240, 36)", "Eq(24 + 12, 36)"],
        ),
        problem(
            "sat-pc1-t2",
            "A price of $\\$60$ increases by $35\\%$. What is the new price?",
            "**Answer.** $\\$81$. Multiply by $1.35$: $60 \\times 1.35 = 81$.",
            ["Eq(60*Rational(135,100), 81)", "Eq(60 + Rational(35,100)*60, 81)"],
        ),
        problem(
            "sat-pc1-t3",
            "After a $40\\%$ increase, a population is $2{,}100$. What was it before?",
            "**Answer.** $1{,}500$. A $40\\%$ increase multiplies by $1.4$, so the original is "
            "$\\frac{2100}{1.4} = 1500$. Check: $40\\%$ of $1500$ is $600$, and "
            "$1500 + 600 = 2100$.",
            [
                "Eq(Rational(14,10)*1500, 2100)",
                "Eq(1500 + Rational(40,100)*1500, 2100)",
            ],
        ),
        problem(
            "sat-pc1-t4",
            "A value falls by $10\\%$ and then falls by a further $10\\%$. What is the total "
            "percentage decrease?",
            "**Answer.** $19\\%$. The multipliers are $0.9$ and $0.9$, and "
            "$0.9 \\times 0.9 = 0.81$, so $81\\%$ remains and $19\\%$ has gone. Adding the two "
            "drops to get $20\\%$ is the standard error — the second $10\\%$ is taken off a "
            "smaller amount.",
            [
                "Eq(Rational(9,10)*Rational(9,10), Rational(81,100))",
                "Eq(1 - Rational(81,100), Rational(19,100))",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Percentages",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "Usually 1 question, and it is nearly always a percent CHANGE.",
                "Prerequisite: solving a linear equation in one variable.",
                "One habit carries the whole subtopic: turn every change into a multiplier.",
            ],
        },
        {
            "kind": "teach",
            "title": "Every change is a multiplier",
            "body": "An increase of $r$ percent multiplies by $1 + \\frac{r}{100}$; a decrease "
                    "multiplies by $1 - \\frac{r}{100}$. So $+35\\%$ is $\\times 1.35$ and "
                    "$-30\\%$ is $\\times 0.70$. Building that habit turns two-step problems "
                    "into one multiplication and makes reversing a change obvious: you divide "
                    "by the multiplier.",
        },
        {
            "kind": "percentChange",
            "title": "Increase and decrease as one move",
            "teach": "Slide the percentage and watch the bar move. Notice that the multiplier "
                     "shown is what does the work — the amount added or removed is a "
                     "consequence, not the method.",
            "config": {"original": 85, "start": 30, "mode": "discount"},
        },
        {"kind": "worked", "title": "A discount in one step", "problemId": "sat-pc1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Undo the change",
            "prompt": "After a $25\\%$ increase a value is $\\$150$. What was it before?",
            "options": ["$\\$120$", "$\\$112.50$", "$\\$125$", "$\\$187.50$"],
            "correctIndex": 0,
            "explanation": "A $25\\%$ increase multiplies by $1.25$, so the original is "
                           "$\\frac{150}{1.25} = 120$. Check: $25\\%$ of $120$ is $30$, and "
                           "$120 + 30 = 150$. Taking $25\\%$ OFF $150$ gives $112.50$ — the "
                           "trap — because $25\\%$ of $150$ is bigger than $25\\%$ of $120$.",
            "check": [
                "Eq(Rational(125,100)*120, 150)",
                "Eq(150 - Rational(25,100)*150, Rational(2250,20))",
                "Ne(Rational(2250,20), 120)",
            ],
        },
        {"kind": "worked", "title": "Working backwards to the original", "problemId": "sat-pc1-w2"},
        {
            "kind": "tip",
            "title": "Percentages never add",
            "body": "Two changes in a row MULTIPLY their multipliers. A $25\\%$ rise followed "
                    "by a $20\\%$ fall is $1.25 \\times 0.80 = 1.00$ — no change at all, not "
                    "the $+5\\%$ that adding would suggest. The reason is that the second "
                    "percentage is taken of a different amount from the first.",
        },
        {"kind": "worked", "title": "Two changes in a row", "problemId": "sat-pc1-w3"},
        {"kind": "tryIt", "title": "Your turn: percent of", "problemId": "sat-pc1-t1"},
        {"kind": "tryIt", "title": "Your turn: an increase", "problemId": "sat-pc1-t2"},
        {"kind": "tryIt", "title": "Your turn: reverse it", "problemId": "sat-pc1-t3"},
        {"kind": "tryIt", "title": "Your turn: two drops", "problemId": "sat-pc1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "An increase of r% is a multiplier of 1 + r/100; a decrease is 1 − r/100.",
                "To undo a percentage change, DIVIDE by the multiplier — never subtract it back.",
                "Successive changes multiply; they never add.",
                "A 10% drop followed by another 10% drop is 19%, not 20%.",
                "A percentage is always OF something — check which amount it refers to.",
            ],
        },
    ]

    return lesson(
        slug="percent-change",
        title="Percent Change, and Working Backwards",
        concrete=(
            "A shop marks a coat up $25\\%$, then holds a $20\\%$-off sale. Customers expect "
            "to be $5\\%$ ahead. They are exactly level — because the two percentages are "
            "taken of different amounts, and percentages have never added."
        ),
        objective=(
            "Compute percent increases and decreases as single multipliers, reverse a "
            "percentage change to find an original amount, and combine successive changes "
            "correctly."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Percentages*, in the "
            "**Problem-Solving and Data Analysis** domain. Usually one question a test, and it "
            "is nearly always a percent CHANGE rather than a plain 'percent of'.",
            "Turn every change into a multiplier. An increase of $r$ percent multiplies by "
            "$1 + \\frac{r}{100}$; a decrease multiplies by $1 - \\frac{r}{100}$. So a "
            "$35\\%$ rise is $\\times 1.35$ and a $30\\%$ discount is $\\times 0.70$. This is "
            "not just faster — it is the only practical way to handle the two-step questions.",
            "Reversing a change is then obvious: DIVIDE by the multiplier. If a $20\\%$ "
            "discount leaves $\\$96$, the original was $\\frac{96}{0.8} = \\$120$. Adding "
            "$20\\%$ back to $\\$96$ gives $\\$115.20$, and it is wrong because $20\\%$ of the "
            "smaller number is a smaller amount.",
            "**The test's angle.** Successive changes multiply. A $25\\%$ rise then a $20\\%$ "
            "fall is $1.25 \\times 0.80 = 1.00$ — completely unchanged, not $+5\\%$. Two "
            "$10\\%$ drops give $0.9 \\times 0.9 = 0.81$, a $19\\%$ decrease rather than "
            "$20\\%$. Adding the percentages is the wrong answer the question is designed "
            "around.",
        ],
        key_idea=(
            "Every percentage change is a multiplier. Multiply to apply one, divide to undo "
            "one, and multiply the multipliers together for two in a row — never add the "
            "percentages."
        ),
        facts=[
            fact(
                "Change as a multiplier",
                "\\text{new} = \\left(1 \\pm \\frac{r}{100}\\right)\\text{old}",
                "Plus for an increase, minus for a decrease.",
            ),
            fact(
                "Reversing a change",
                "\\text{old} = \\frac{\\text{new}}{1 \\pm \\frac{r}{100}}",
                "Divide by the multiplier. Applying the reverse percentage gives a different, "
                "wrong number.",
            ),
            fact(
                "Successive changes",
                "\\text{overall multiplier} = m_1 \\times m_2",
                "$1.25 \\times 0.80 = 1.00$. Percentages multiply through their multipliers "
                "and never add.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Undoing a discount by adding the same percentage back.",
                "Divide by the multiplier instead. Adding $20\\%$ to $\\$96$ gives "
                "$\\$115.20$, not the true original of $\\$120$.",
            ),
            mistake(
                "Adding two successive percentage changes.",
                "They multiply. $+25\\%$ then $-20\\%$ is no change at all, not $+5\\%$.",
            ),
            mistake(
                "Losing track of what the percentage is OF.",
                "A markup is a percentage of the cost; a discount is a percentage of the "
                "listed price. They are percentages of different numbers.",
            ),
            mistake(
                "Treating two $10\\%$ decreases as a $20\\%$ decrease.",
                "The second is taken off an already smaller amount, so the total is $19\\%$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_percent_context():
    worked = [
        problem(
            "sat-pc2-w1",
            "A town's population rose from $18{,}500$ to $21{,}090$. What was the percentage "
            "increase?",
            "**Answer.** $14\\%$.  \n"
            "A percentage change is always the change divided by the ORIGINAL amount:\n"
            "$$\\text{percent change} = \\frac{\\text{new} - \\text{old}}{\\text{old}} \\times 100\\%$$\n"
            "$$= \\frac{21090 - 18500}{18500} \\times 100\\%$$\n"
            "$$= \\frac{2590}{18500} \\times 100\\% = 14\\%$$\n"
            "Check: $14\\%$ of $18{,}500$ is $2{,}590$, and $18500 + 2590 = 21090$.  \n"
            "Dividing by the NEW value instead gives $\\frac{2590}{21090} \\approx 12.3\\%$, "
            "which is a different quantity — it answers 'what fraction of the new population "
            "is the growth', which nobody asked.",
            [
                "Eq(21090 - 18500, 2590)",
                "Eq(Rational(2590, 18500), Rational(14, 100))",
                "Eq(18500 + Rational(14,100)*18500, 21090)",
            ],
        ),
        problem(
            "sat-pc2-w2",
            "In a survey of $1{,}200$ people, $18\\%$ said they cycle to work. Of those "
            "cyclists, $25\\%$ also walk some days. How many people both cycle and walk?",
            "**Answer.** $54$.  \n"
            "The second percentage is taken OF THE FIRST GROUP, not of the whole survey. Work "
            "outward one layer at a time.\n"
            "$$\\text{cyclists} = 0.18 \\times 1200 = 216$$\n"
            "$$\\text{both} = 0.25 \\times 216 = 54$$\n"
            "Check as a single multiplication: $0.18 \\times 0.25 = 0.045$, and "
            "$0.045 \\times 1200 = 54$ — that is $4.5\\%$ of the whole survey.  \n"
            "Applying $25\\%$ to the full $1{,}200$ gives $300$, and adding the percentages to "
            "get $43\\%$ gives $516$. Both are listed. The phrase 'of those' is the signal "
            "that a percentage refers to a subgroup.",
            [
                "Eq(Rational(18,100)*1200, 216)",
                "Eq(Rational(25,100)*216, 54)",
                "Eq(Rational(18,100)*Rational(25,100)*1200, 54)",
                "Eq(Rational(25,100)*1200, 300)",
            ],
        ),
        problem(
            "sat-pc2-w3",
            "A shop buys an item for $\\$40$ and sells it for $\\$52$. What is the percentage "
            "markup on the cost, and what is the profit as a percentage of the selling price?",
            "**Answer.** Markup $30\\%$ of cost; profit is about $23.1\\%$ of the selling "
            "price.  \n"
            "The profit is $52 - 40 = \\$12$ either way — but which number you divide by "
            "changes the answer entirely.  \n"
            "As a percentage of COST:\n"
            "$$\\frac{12}{40} = 0.30 = 30\\%$$\n"
            "As a percentage of the SELLING PRICE:\n"
            "$$\\frac{12}{52} = 0.2307\\ldots \\approx 23.1\\%$$\n"
            "Both are correct answers to different questions, and both appear as options. The "
            "phrase 'markup' conventionally means a percentage of the COST; 'margin' means a "
            "percentage of the selling price. Whenever a percentage question feels ambiguous, "
            "the fix is to identify the base — the amount the percentage is OF — before "
            "dividing.",
            [
                "Eq(52 - 40, 12)",
                "Eq(Rational(12,40), Rational(30,100))",
                "Eq(40*Rational(130,100), 52)",
                "Eq(Rational(12,52), Rational(3,13))",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-pc2-t1",
            "A price falls from $\\$80$ to $\\$68$. What is the percentage decrease?",
            "**Answer.** $15\\%$. The change is $12$, and $\\frac{12}{80} = 0.15$.",
            ["Eq(80 - 68, 12)", "Eq(Rational(12,80), Rational(15,100))"],
        ),
        problem(
            "sat-pc2-t2",
            "Of $800$ students, $35\\%$ study a language. Of those, $40\\%$ study French. How "
            "many study French?",
            "**Answer.** $112$. The language students number $0.35 \\times 800 = 280$, and "
            "$40\\%$ of $280$ is $112$. That is $14\\%$ of the whole school.",
            [
                "Eq(Rational(35,100)*800, 280)",
                "Eq(Rational(40,100)*280, 112)",
                "Eq(Rational(112,800), Rational(14,100))",
            ],
        ),
        problem(
            "sat-pc2-t3",
            "An item costing $\\$25$ is sold for $\\$32$. What is the markup as a percentage "
            "of the cost?",
            "**Answer.** $28\\%$. The profit is $7$, and $\\frac{7}{25} = 0.28$. As a "
            "percentage of the selling price it would be $\\frac{7}{32} \\approx 21.9\\%$ — a "
            "different question.",
            ["Eq(32 - 25, 7)", "Eq(Rational(7,25), Rational(28,100))"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Percent change divides by the ORIGINAL",
            "body": "The percentage change is the change divided by the amount you started "
                    "with, never by the amount you ended with. Rising from $18{,}500$ to "
                    "$21{,}090$ is a rise of $2{,}590$ on a base of $18{,}500$, which is "
                    "$14\\%$. Dividing by the new figure answers a different question and "
                    "gives a smaller number, which is always on the option list.",
        },
        {
            "kind": "percentChangeFinder",
            "title": "Find the percentage from two amounts",
            "teach": "Set a before and an after and watch the percentage change appear. Notice "
                     "that swapping the two numbers does NOT just flip the sign — the base "
                     "changes too, so the size of the percentage changes as well.",
            "config": {"original": 80, "final": 68},
        },
        {"kind": "worked", "title": "Percentage increase from two figures", "problemId": "sat-pc2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Percent of what?",
            "prompt": "In a group of $500$ people, $40\\%$ own a bicycle. Of those owners, "
                      "$30\\%$ cycle daily. How many cycle daily?",
            "options": ["$60$", "$150$", "$200$", "$350$"],
            "correctIndex": 0,
            "explanation": "Owners number $0.40 \\times 500 = 200$, and $30\\%$ of those is "
                           "$60$. Option B applies the $30\\%$ to the whole group, C stops at "
                           "the owners, and D adds the percentages. 'Of those' always means "
                           "the previous subgroup.",
            "check": [
                "Eq(Rational(40,100)*500, 200)",
                "Eq(Rational(30,100)*200, 60)",
                "Eq(Rational(30,100)*500, 150)",
            ],
        },
        {"kind": "worked", "title": "A percentage of a percentage", "problemId": "sat-pc2-w2"},
        {
            "kind": "tip",
            "title": "Name the base before you divide",
            "body": "Every percentage is OF something, and the hard questions make you choose. "
                    "Profit as a percentage of COST and profit as a percentage of the SELLING "
                    "PRICE are different numbers from the same two figures, and both are "
                    "options. Underline the noun after 'percentage of' before you compute.",
        },
        {"kind": "worked", "title": "Two bases, two answers", "problemId": "sat-pc2-w3"},
        {"kind": "tryIt", "title": "Your turn: percentage decrease", "problemId": "sat-pc2-t1"},
        {"kind": "tryIt", "title": "Your turn: a subgroup", "problemId": "sat-pc2-t2"},
        {"kind": "tryIt", "title": "Your turn: markup on cost", "problemId": "sat-pc2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Percent change is the change divided by the ORIGINAL amount.",
                "'Of those' means the percentage applies to the previous subgroup, not the whole.",
                "Two percentages applied in sequence multiply: 18% of 25% is 4.5% overall.",
                "Identify the base — cost or selling price — before dividing.",
                "Both bases give correct-looking answers, and both will be on the option list.",
            ],
        },
    ]

    return lesson(
        slug="percentages-in-context",
        title="Percentages of What? Bases and Subgroups",
        concrete=(
            "A shop makes $\\$12$ on a $\\$40$ item sold for $\\$52$. Is that a $30\\%$ "
            "profit or a $23\\%$ one? Both, depending on whether you divide by what it cost or "
            "by what it sold for — and the SAT will offer you both numbers."
        ),
        objective=(
            "Compute a percentage change from two amounts, apply a percentage to a subgroup, "
            "and identify which quantity a percentage is being taken of."
        ),
        concept=[
            "**Skill card.** Still *Percentages*, in the **Problem-Solving and Data Analysis** "
            "domain. This is the half where the arithmetic is easy and the reading is not.",
            "A percentage change divides the CHANGE by the ORIGINAL amount. From $18{,}500$ to "
            "$21{,}090$ is a rise of $2{,}590$ on a base of $18{,}500$, that is $14\\%$. "
            "Dividing by the new figure gives about $12.3\\%$, which answers a question nobody "
            "asked — and is always among the options.",
            "When a second percentage appears, read carefully which group it applies to. 'Of "
            "those' means the previous subgroup: $18\\%$ of $1{,}200$ cycle, and $25\\%$ of "
            "THOSE also walk, giving $0.18 \\times 0.25 = 4.5\\%$ of the whole. Applying the "
            "$25\\%$ to the full $1{,}200$ is the error the sentence is built to catch.",
            "**The test's angle.** Naming the base. Profit as a percentage of cost and profit "
            "as a percentage of selling price are different numbers computed from the same two "
            "figures, and both look plausible. Underline the noun that follows 'percentage of' "
            "before dividing — that noun IS the denominator.",
        ],
        key_idea=(
            "Every percentage is OF something. For a change, that something is the original "
            "amount; for a subgroup, it is the group just named. Find the base before you "
            "divide."
        ),
        facts=[
            fact(
                "Percentage change",
                "\\frac{\\text{new} - \\text{old}}{\\text{old}} \\times 100\\%",
                "The denominator is the ORIGINAL. Using the new value answers a different "
                "question.",
            ),
            fact(
                "Percentage of a percentage",
                "r_1\\% \\text{ of } r_2\\% \\text{ of } N = \\frac{r_1}{100} \\cdot \\frac{r_2}{100} \\cdot N",
                "Two proportions in sequence multiply. $18\\%$ then $25\\%$ is $4.5\\%$ of the "
                "whole.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Dividing by the new amount when computing a percentage change.",
                "The base is what you started with. Using the new figure always gives a "
                "smaller percentage, and it is an option.",
            ),
            mistake(
                "Applying a subgroup's percentage to the whole population.",
                "'Of those' restricts it to the group just named. Compute that group first, "
                "then take the percentage of it.",
            ),
            mistake(
                "Adding two chained percentages.",
                "$18\\%$ of the group, then $25\\%$ of those, is $4.5\\%$ overall — not "
                "$43\\%$.",
            ),
            mistake(
                "Dividing profit by the wrong base.",
                "Markup is a percentage of COST; margin is a percentage of the SELLING PRICE. "
                "Read which one is wanted.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


PCT_PRACTICE = [
    problem(
        "sat-pc-p01",
        "What is $22\\%$ of $350$?",
        "**Answer.** $77$. $0.22 \\times 350 = 77$.",
        ["Eq(Rational(22,100)*350, 77)"],
        badges=_b(PCT_TAG, "Easy"),
    ),
    problem(
        "sat-pc-p02",
        "A price of $\\$45$ rises by $20\\%$. What is the new price?",
        "**Answer.** $\\$54$. Multiply by $1.2$.",
        ["Eq(45*Rational(120,100), 54)"],
        badges=_b(PCT_TAG, "Easy"),
    ),
    problem(
        "sat-pc-p03",
        "A quantity falls from $250$ to $200$. What is the percentage decrease?",
        "**Answer.** $20\\%$. The change is $50$, and $\\frac{50}{250} = 0.2$. Dividing by "
        "$200$ instead gives $25\\%$, a listed option.",
        ["Eq(Rational(50,250), Rational(20,100))", "Eq(Rational(50,200), Rational(25,100))"],
        badges=_b(PCT_TAG, "Medium"),
    ),
    problem(
        "sat-pc-p04",
        "After a $15\\%$ discount an item costs $\\$68$. What was the original price?",
        "**Answer.** $\\$80$. A $15\\%$ discount multiplies by $0.85$, so the original is "
        "$\\frac{68}{0.85} = 80$. Check: $15\\%$ of $80$ is $12$, and $80 - 12 = 68$.",
        ["Eq(Rational(85,100)*80, 68)", "Eq(80 - Rational(15,100)*80, 68)"],
        badges=_b(PCT_TAG, "Medium"),
    ),
    problem(
        "sat-pc-p05",
        "A value increases by $50\\%$ and then decreases by $50\\%$. What is the overall "
        "percentage change?",
        "**Answer.** A $25\\%$ decrease. The multipliers give $1.5 \\times 0.5 = 0.75$, so "
        "$75\\%$ remains. Starting from $100$: up to $150$, then down to $75$.",
        [
            "Eq(Rational(150,100)*Rational(50,100), Rational(75,100))",
            "Eq(100*Rational(150,100), 150)",
            "Eq(150*Rational(50,100), 75)",
        ],
        badges=_b(PCT_TAG, "Hard"),
    ),
    problem(
        "sat-pc-p06",
        "Of $2{,}500$ visitors, $24\\%$ bought a ticket in advance. Of those, $15\\%$ "
        "requested a refund. How many requested a refund?",
        "**Answer.** $90$. Advance buyers number $600$, and $15\\%$ of $600$ is $90$ — which "
        "is $3.6\\%$ of all visitors.",
        [
            "Eq(Rational(24,100)*2500, 600)",
            "Eq(Rational(15,100)*600, 90)",
            "Eq(Rational(90,2500), Rational(36,1000))",
        ],
        badges=_b(PCT_TAG, "Medium"),
    ),
    problem(
        "sat-pc-p07",
        "An item costs a shop $\\$60$ and is sold at a $45\\%$ markup. What is the selling "
        "price?",
        "**Answer.** $\\$87$. A $45\\%$ markup on the COST multiplies by $1.45$: "
        "$60 \\times 1.45 = 87$.",
        ["Eq(60*Rational(145,100), 87)", "Eq(60 + Rational(45,100)*60, 87)"],
        badges=_b(PCT_TAG, "Medium"),
    ),
    problem(
        "sat-pc-p08",
        "A salary of $\\$52{,}000$ rises by $6\\%$ and then by a further $4\\%$ the next year. "
        "What is the salary after both rises?",
        "**Answer.** $\\$57{,}324.80$. The multipliers are $1.06$ and $1.04$, giving "
        "$1.06 \\times 1.04 = 1.1024$, so the salary is $52000 \\times 1.1024 = 57324.80$. "
        "Adding the percentages to get $10\\%$ gives $\\$57{,}200$ — close, but wrong, and "
        "the gap grows with bigger percentages.",
        [
            "Eq(Rational(106,100)*Rational(104,100), Rational(11024,10000))",
            "Eq(52000*Rational(11024,10000), Rational(573248,10))",
            "Ne(Rational(573248,10), 57200)",
        ],
        badges=_b(PCT_TAG, "Hard"),
    ),
]

PCT_TEST = [
    problem(
        "sat-pc-x01",
        "What is $8\\%$ of $650$?",
        "**Answer.** $52$. $0.08 \\times 650 = 52$.",
        ["Eq(Rational(8,100)*650, 52)"],
        badges=_b(PCT_TAG, "Easy"),
    ),
    problem(
        "sat-pc-x02",
        "A population grows from $4{,}000$ to $4{,}600$. What is the percentage increase?",
        "**Answer.** $15\\%$. The change is $600$, and $\\frac{600}{4000} = 0.15$.",
        ["Eq(Rational(600,4000), Rational(15,100))"],
        badges=_b(PCT_TAG, "Easy"),
    ),
    problem(
        "sat-pc-x03",
        "After a $30\\%$ increase, a value is $\\$260$. What was it before?",
        "**Answer.** $\\$200$. Divide by $1.3$: $\\frac{260}{1.3} = 200$. Taking $30\\%$ off "
        "$260$ gives $182$, the trap.",
        [
            "Eq(Rational(130,100)*200, 260)",
            "Eq(260 - Rational(30,100)*260, 182)",
            "Ne(182, 200)",
        ],
        badges=_b(PCT_TAG, "Medium"),
    ),
    problem(
        "sat-pc-x04",
        "A price rises $10\\%$ and then falls $10\\%$. What is the overall change?",
        "**Answer.** A $1\\%$ decrease. The multipliers give $1.1 \\times 0.9 = 0.99$. "
        "Starting from $\\$100$: up to $\\$110$, then down to $\\$99$. The two changes look "
        "symmetric but are taken of different amounts.",
        [
            "Eq(Rational(110,100)*Rational(90,100), Rational(99,100))",
            "Eq(100*Rational(110,100), 110)",
            "Eq(110*Rational(90,100), 99)",
        ],
        badges=_b(PCT_TAG, "Hard"),
    ),
    problem(
        "sat-pc-x05",
        "Of $1{,}500$ employees, $60\\%$ work full time. Of those, $25\\%$ work remotely. How "
        "many work full time and remotely?",
        "**Answer.** $225$. Full-timers number $900$, and $25\\%$ of $900$ is $225$ — that is "
        "$15\\%$ of all employees.",
        [
            "Eq(Rational(60,100)*1500, 900)",
            "Eq(Rational(25,100)*900, 225)",
            "Eq(Rational(225,1500), Rational(15,100))",
        ],
        badges=_b(PCT_TAG, "Medium"),
    ),
    problem(
        "sat-pc-x06",
        "A shop buys a chair for $\\$120$ and sells it for $\\$150$. What is the profit as a "
        "percentage of the cost?",
        "**Answer.** $25\\%$. The profit is $30$, and $\\frac{30}{120} = 0.25$. As a "
        "percentage of the selling price it would be $\\frac{30}{150} = 20\\%$ — also on the "
        "option list, answering a different question.",
        [
            "Eq(150 - 120, 30)",
            "Eq(Rational(30,120), Rational(25,100))",
            "Eq(Rational(30,150), Rational(20,100))",
        ],
        badges=_b(PCT_TAG, "Hard"),
    ),
]


def main():
    write_unit(
        COURSE,
        "ratios-rates-proportions-units",
        "Ratios, Rates, Proportional Relationships and Units",
        1,
        "Splitting a total by a ratio, using a rate across a unit change, and the proportional "
        "relationships that pass through the origin — plus the unit conversions that cost more "
        "points here than the mathematics does.",
        None,
        [lesson_ratios(), lesson_proportional()],
        RATIO_PRACTICE,
        RATIO_TEST,
    )
    write_unit(
        COURSE,
        "percentages",
        "Percentages",
        2,
        "Percent change as a multiplier, reversing a change to find the original amount, "
        "successive changes that multiply rather than add, and the question behind every hard "
        "percentage item: a percentage of WHAT?",
        "Ratios and proportional reasoning from Unit 1 — a percentage is a ratio out of 100.",
        [lesson_percent_basics(), lesson_percent_context()],
        PCT_PRACTICE,
        PCT_TEST,
    )


if __name__ == "__main__":
    main()
