#!/usr/bin/env python3
"""SAT Math — Problem-Solving and Data Analysis, Units 3-4.

Builds:
  data/genmath/sat/one-variable-data.json
  data/genmath/sat/two-variable-data.json

Run: python3 scripts/sat/build_psda_3_4.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
ONE_TAG = {"text": "sat-data-one-var", "mono": True}
TWO_TAG = {"text": "sat-data-two-var", "mono": True}


def _b(tag, level):
    return [tag, {"text": level}]


# ===========================================================================
# UNIT 3 — One-variable data
# ===========================================================================

def lesson_centre():
    worked = [
        problem(
            "sat-od1-w1",
            "The list $4, 7, 7, 9, 13, 20$ gives the number of books six students read. What "
            "are the mean and the median, and why do they differ?",
            "**Answer.** Mean $10$, median $8$; the $20$ pulls the mean upward.  \n"
            "The mean adds everything and divides by the count:\n"
            "$$\\frac{4 + 7 + 7 + 9 + 13 + 20}{6} = \\frac{60}{6} = 10$$\n"
            "The median is the middle value once the list is in order. With SIX values there "
            "is no single middle, so average the third and fourth:\n"
            "$$\\frac{7 + 9}{2} = 8$$\n"
            "The mean is larger because it uses every value's SIZE, so one unusually large "
            "reading drags it up. The median only cares about POSITION — the $20$ is simply "
            "'the biggest', and replacing it with $200$ would leave the median at $8$ while "
            "sending the mean to $40$.  \n"
            "That is the whole difference, and it is what the SAT tests: the mean is sensitive "
            "to outliers, the median is resistant to them.",
            [
                "Eq(4 + 7 + 7 + 9 + 13 + 20, 60)",
                "Eq(Rational(60,6), 10)",
                "Eq(Rational(7 + 9, 2), 8)",
                "Eq(Rational(4 + 7 + 7 + 9 + 13 + 200, 6), 40)",
            ],
        ),
        problem(
            "sat-od1-w2",
            "The mean of five numbers is $18$. When a sixth number is added the mean becomes "
            "$20$. What is the sixth number?",
            "**Answer.** $30$.  \n"
            "A mean question is really a TOTAL question. Work with the sums.\n"
            "$$\\text{sum of five} = 5 \\times 18 = 90$$\n"
            "$$\\text{sum of six} = 6 \\times 20 = 120$$\n"
            "The sixth number is whatever closes the gap:\n"
            "$$120 - 90 = 30$$\n"
            "Check: $\\frac{90 + 30}{6} = \\frac{120}{6} = 20$.  \n"
            "The instinct is to reach for the individual values, but they are neither given "
            "nor needed. Mean times count gives the total, and totals add — that single move "
            "handles every 'the mean changes when...' question the SAT sets.",
            [
                "Eq(5*18, 90)",
                "Eq(6*20, 120)",
                "Eq(120 - 90, 30)",
                "Eq(Rational(90 + 30, 6), 20)",
            ],
        ),
        problem(
            "sat-od1-w3",
            "Two data sets have the same mean. Set A is $10, 20, 30, 40, 50$ and Set B is "
            "$28, 29, 30, 31, 32$. Which has the larger standard deviation, and why?",
            "**Answer.** Set A, because its values are spread much further from the mean.  \n"
            "Both have mean $30$:\n"
            "$$\\frac{10 + 20 + 30 + 40 + 50}{5} = 30, \\qquad \\frac{28 + 29 + 30 + 31 + 32}{5} = 30$$\n"
            "Standard deviation measures typical distance from the mean. In Set A the "
            "distances are $20, 10, 0, 10, 20$; in Set B they are $2, 1, 0, 1, 2$. Every "
            "distance in A is ten times the matching one in B, so A's standard deviation is "
            "ten times B's.  \n"
            "The SAT never asks you to CALCULATE a standard deviation — it asks you to compare "
            "two, and comparing spreads by eye is enough. Look at how far the values reach "
            "from the centre: wider spread means larger standard deviation, and a set whose "
            "values are all nearly equal has a standard deviation near zero.  \n"
            "Note also what does NOT change it: adding a constant to every value shifts the "
            "mean but leaves every distance untouched, so the standard deviation is unchanged.",
            [
                "Eq(Rational(10 + 20 + 30 + 40 + 50, 5), 30)",
                "Eq(Rational(28 + 29 + 30 + 31 + 32, 5), 30)",
                "Eq(50 - 10, 40)",
                "Eq(32 - 28, 4)",
                "40 > 4",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-od1-t1",
            "What is the median of $3, 8, 2, 9, 5$?",
            "**Answer.** $5$. In order the list is $2, 3, 5, 8, 9$, and with five values the "
            "middle one is the third. Taking the middle of the UNSORTED list is the standard "
            "error and gives $2$.",
            ["Eq(5, 5)", "Eq(sorted([3,8,2,9,5])[2], 5)"],
        ),
        problem(
            "sat-od1-t2",
            "The mean of four numbers is $12$. Three of them are $8$, $10$ and $15$. What is "
            "the fourth?",
            "**Answer.** $15$. The total must be $4 \\times 12 = 48$, and the three given sum "
            "to $33$, so the fourth is $48 - 33 = 15$.",
            ["Eq(4*12, 48)", "Eq(8 + 10 + 15, 33)", "Eq(48 - 33, 15)"],
        ),
        problem(
            "sat-od1-t3",
            "A data set has mean $50$ and median $50$. One value of $50$ is changed to $500$. "
            "What happens to each?",
            "**Answer.** The mean rises; the median is unchanged. The mean uses every value's "
            "size, so replacing $50$ with $500$ adds $450$ to the total and raises the "
            "average. The median depends only on position, and moving one value from the "
            "middle of the range to the top does not move the middle value.",
            ["Eq(500 - 50, 450)", "450 > 0"],
        ),
        problem(
            "sat-od1-t4",
            "Set P is $5, 5, 5, 5$ and Set Q is $1, 4, 6, 9$. Which has the larger standard "
            "deviation?",
            "**Answer.** Set Q. Every value in P is identical, so nothing deviates from the "
            "mean at all and the standard deviation is exactly zero. Q's values spread from "
            "$1$ to $9$, so its standard deviation is positive.",
            [
                "Eq(Rational(5 + 5 + 5 + 5, 4), 5)",
                "Eq(Rational(1 + 4 + 6 + 9, 4), 5)",
                "Eq(5 - 5, 0)",
                "9 - 1 > 0",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "One-variable data",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "Usually 1 question, and it is almost never a calculation.",
                "Prerequisite: none beyond arithmetic.",
                "You are never asked to compute a standard deviation — only to compare two.",
            ],
        },
        {
            "kind": "teach",
            "title": "Mean uses size, median uses position",
            "body": "The mean adds every value and divides by the count, so a single extreme "
                    "reading moves it a long way. The median is just the middle value once the "
                    "list is sorted, so an extreme reading is merely 'the biggest' and moves "
                    "nothing. That is why house prices are reported by median and exam marks "
                    "by mean — and it is the distinction almost every SAT question here is "
                    "built on.",
        },
        {
            "kind": "dotPlot",
            "title": "Watch them separate",
            "teach": "Drag the highest dot further right. The median stays put while the mean "
                     "chases it — the mean is pulled by size, the median only counts places.",
            "config": {"mode": "meanMedian", "data": [4, 7, 7, 9, 13, 20], "min": 0, "max": 24,
                       "xLabel": "books read"},
        },
        {"kind": "worked", "title": "Mean against median", "problemId": "sat-od1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which one moves?",
            "prompt": "In the list $2, 4, 6, 8, 10$ the largest value is changed from $10$ to "
                      "$100$. What happens?",
            "options": [
                "The mean rises and the median does not change",
                "Both rise by the same amount",
                "The median rises and the mean does not change",
                "Neither changes",
            ],
            "correctIndex": 0,
            "explanation": "The mean goes from $6$ to $24$, because the total jumps by $90$. "
                           "The median is the third value in the sorted list, which is $6$ "
                           "before and after — the changed value is still simply the largest.",
            "check": [
                "Eq(Rational(2 + 4 + 6 + 8 + 10, 5), 6)",
                "Eq(Rational(2 + 4 + 6 + 8 + 100, 5), 24)",
                "Eq(sorted([2,4,6,8,100])[2], 6)",
            ],
        },
        {
            "kind": "tip",
            "title": "Turn a mean into a total",
            "body": "Mean times count equals total, and totals ADD. Every question of the form "
                    "'the mean of five is $18$; a sixth is added and the mean becomes $20$' is "
                    "answered by comparing $5 \\times 18$ with $6 \\times 20$. The individual "
                    "values are neither given nor needed.",
        },
        {"kind": "worked", "title": "A mean that changes", "problemId": "sat-od1-w2"},
        {
            "kind": "teach",
            "title": "Spread, without computing anything",
            "beats": [
                "Range is the largest minus the smallest — one subtraction.",
                "Standard deviation is the typical distance of a value from the mean.",
                "The SAT asks you to COMPARE two spreads, never to calculate one.",
                "Identical values give a standard deviation of exactly zero.",
                "Adding the same amount to every value leaves the standard deviation unchanged.",
            ],
        },
        {"kind": "worked", "title": "Comparing two spreads", "problemId": "sat-od1-w3"},
        {"kind": "tryIt", "title": "Your turn: sort first", "problemId": "sat-od1-t1"},
        {"kind": "tryIt", "title": "Your turn: the missing value", "problemId": "sat-od1-t2"},
        {"kind": "tryIt", "title": "Your turn: which measure moves?", "problemId": "sat-od1-t3"},
        {"kind": "tryIt", "title": "Your turn: compare the spreads", "problemId": "sat-od1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Sort the list before taking a median; with an even count, average the middle two.",
                "The mean is dragged by extreme values; the median is not.",
                "Mean times count is the total, and totals add — that solves the 'new mean' items.",
                "Standard deviation measures typical distance from the mean; compare, do not compute.",
                "Identical values give zero spread; shifting every value changes nothing about it.",
            ],
        },
    ]

    return lesson(
        slug="centre-and-spread",
        title="Centre and Spread, and Which One Moves",
        concrete=(
            "Nine people in a room earn about $\\$40{,}000$ each. A billionaire walks in. The "
            "average income in the room is now over $\\$100$ million; the median has barely "
            "moved. Neither number is lying — they are answering different questions."
        ),
        objective=(
            "Compute mean and median, predict which one an extreme value moves, use totals to "
            "handle changing means, and compare the spread of two data sets without computing "
            "a standard deviation."
        ),
        concept=[
            "**Skill card.** The College Board calls this *One-variable data: distributions "
            "and measures of center and spread*, in the **Problem-Solving and Data Analysis** "
            "domain. Usually one question a test, and it is almost never a calculation — it is "
            "a comparison.",
            "The mean adds every value and divides by the count, so it uses each value's SIZE "
            "and a single extreme reading drags it a long way. The median is the middle value "
            "of the sorted list, so it uses only POSITION and an extreme reading is merely "
            "'the largest'. Sorting first is not optional: the middle of an unsorted list "
            "means nothing.",
            "For questions where a mean changes, work with TOTALS. Mean times count is the "
            "total, and totals add. 'The mean of five numbers is $18$; adding a sixth makes it "
            "$20$' becomes $6 \\times 20 - 5 \\times 18 = 30$, with no need for the individual "
            "values.",
            "**The test's angle.** Standard deviation is never calculated on the SAT — you are "
            "asked which of two data sets has the larger one. It measures typical distance "
            "from the mean, so look at how far the values reach from the centre. Identical "
            "values give exactly zero. And adding the same amount to every value shifts the "
            "mean but leaves every distance untouched, so the standard deviation does not "
            "change at all.",
        ],
        key_idea=(
            "The mean follows size and the median follows position, which is why outliers move "
            "one and not the other. Spread is about distance from the centre, and the test "
            "only ever asks you to compare it."
        ),
        facts=[
            fact(
                "Mean and total",
                "\\text{mean} = \\frac{\\text{total}}{n} \\;\\Longleftrightarrow\\; \\text{total} = n \\times \\text{mean}",
                "Turning a mean into a total is the move behind every changing-mean question.",
            ),
            fact(
                "Median",
                "\\text{odd } n: \\text{ the middle value}; \\qquad \\text{even } n: \\text{ the mean of the middle two}",
                "Sort first, always.",
            ),
            fact(
                "What leaves the spread alone",
                "\\text{adding } c \\text{ to every value: mean} + c, \\text{ standard deviation unchanged}",
                "Shifting the whole data set moves the centre but not the distances from it.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Taking the middle of an unsorted list.",
                "The median is defined on the ORDERED data. Sort before you count in.",
            ),
            mistake(
                "Taking only one middle value when the count is even.",
                "With an even number of values there are two middles, and the median is their "
                "average.",
            ),
            mistake(
                "Believing an outlier moves the median.",
                "It moves the mean. The median only shifts if the middle POSITION now holds a "
                "different value.",
            ),
            mistake(
                "Trying to compute a standard deviation.",
                "The SAT never requires it. Compare how far the values sit from the centre and "
                "answer the comparison.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_shape():
    worked = [
        problem(
            "sat-od2-w1",
            "The table shows the number of siblings reported by $40$ students.\n\n"
            "| Siblings | Students |\n| --- | --- |\n| $0$ | $8$ |\n| $1$ | $16$ |\n"
            "| $2$ | $10$ |\n| $3$ | $6$ |\n\n"
            "What is the mean number of siblings?",
            "**Answer.** $1.35$.  \n"
            "A frequency table is a compressed list: eight students reported $0$, sixteen "
            "reported $1$, and so on. The total number of siblings is the WEIGHTED sum:\n"
            "$$0(8) + 1(16) + 2(10) + 3(6) = 0 + 16 + 20 + 18 = 54$$\n"
            "Divide by the number of students, which is the total FREQUENCY:\n"
            "$$\\frac{54}{40} = 1.35$$\n"
            "The trap is averaging the four sibling-counts themselves: "
            "$\\frac{0 + 1 + 2 + 3}{4} = 1.5$. That treats each row as one observation, but "
            "the rows represent $8$, $16$, $10$ and $6$ students respectively. Multiply each "
            "value by how many students reported it.",
            [
                "Eq(0*8 + 1*16 + 2*10 + 3*6, 54)",
                "Eq(8 + 16 + 10 + 6, 40)",
                "Eq(Rational(54,40), Rational(27,20))",
                "Eq(Rational(0 + 1 + 2 + 3, 4), Rational(3,2))",
            ],
        ),
        problem(
            "sat-od2-w2",
            "A distribution of salaries has a long tail of very high values. Which is larger, "
            "the mean or the median, and where does the tail point?",
            "**Answer.** The mean is larger; the tail points toward the higher values, so the "
            "distribution is skewed RIGHT.  \n"
            "A few very large salaries add a great deal to the total but occupy only a few "
            "positions in the ordered list. So they pull the MEAN toward them while leaving "
            "the median where the bulk of the data sits.\n"
            "$$\\text{skewed right} \\;\\Longrightarrow\\; \\text{mean} > \\text{median}$$\n"
            "The rule generalises: the mean is always dragged toward the tail. A left-skewed "
            "distribution, with a tail of unusually LOW values, has mean below median. A "
            "symmetric distribution has them equal.  \n"
            "A concrete check. In $1, 2, 3, 4, 40$ the median is $3$ and the mean is $10$ — "
            "the single large value has moved the mean past four of the five data points, "
            "which is exactly what a right tail does.",
            [
                "Eq(Rational(1 + 2 + 3 + 4 + 40, 5), 10)",
                "Eq(sorted([1,2,3,4,40])[2], 3)",
                "10 > 3",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-od2-t1",
            "A frequency table shows the value $5$ occurring $3$ times, $6$ occurring $2$ "
            "times, and $9$ occurring $5$ times. What is the mean?",
            "**Answer.** $7.2$. The weighted total is "
            "$5(3) + 6(2) + 9(5) = 15 + 12 + 45 = 72$, over $3 + 2 + 5 = 10$ observations, "
            "giving $7.2$.",
            [
                "Eq(5*3 + 6*2 + 9*5, 72)",
                "Eq(3 + 2 + 5, 10)",
                "Eq(Rational(72,10), Rational(36,5))",
            ],
        ),
        problem(
            "sat-od2-t2",
            "In the same table, what is the median?",
            "**Answer.** $7.5$. With ten observations the median is the average of the fifth and "
            "sixth in order. The sorted list is $5, 5, 5, 6, 6, 9, 9, 9, 9, 9$, so the fifth "
            "is $6$ and the sixth is $9$, giving $\\frac{6 + 9}{2} = 7.5$.",
            [
                "Eq(sorted([5,5,5,6,6,9,9,9,9,9])[4], 6)",
                "Eq(sorted([5,5,5,6,6,9,9,9,9,9])[5], 9)",
                "Eq(Rational(6 + 9, 2), Rational(15,2))",
            ],
        ),
        problem(
            "sat-od2-t3",
            "A distribution has mean $60$ and median $72$. What does that suggest about its "
            "shape?",
            "**Answer.** It is skewed LEFT — the tail points toward the low values. The mean "
            "is dragged toward the tail, and here it sits below the median, so the unusual "
            "values are the small ones.",
            ["60 < 72"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "A frequency table is a compressed list",
            "body": "Each row of a frequency table says 'this value appeared this many times'. "
                    "To find the mean, multiply every value by its frequency, add those "
                    "products, and divide by the TOTAL frequency. Averaging the values in the "
                    "left column instead treats every row as a single observation, which is "
                    "the error the tables are built to catch.",
        },
        {
            "kind": "histogramBins",
            "title": "Shape depends on how you bin it",
            "teach": "The same data, drawn with different bin widths. Wide bins hide detail "
                     "and narrow ones can invent it — but the tail, if there is one, survives "
                     "every choice, and the tail is what the SAT asks about.",
            "config": {"data": [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 9, 14], "min": 0, "max": 16,
                       "widths": [1, 2, 4], "xLabel": "value"},
        },
        {"kind": "worked", "title": "Mean from a frequency table", "problemId": "sat-od2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which way does the tail point?",
            "prompt": "A data set has mean $85$ and median $70$. What does this indicate?",
            "options": [
                "The distribution is skewed right, with a tail of high values",
                "The distribution is skewed left, with a tail of low values",
                "The distribution is symmetric",
                "The data set contains an error",
            ],
            "correctIndex": 0,
            "explanation": "The mean is dragged toward the tail. With the mean ABOVE the "
                           "median, the unusual values are the large ones, so the tail extends "
                           "to the right. A symmetric distribution would have the two equal.",
            "check": ["85 > 70", "Eq(Rational(1 + 2 + 3 + 4 + 40, 5), 10)", "10 > 3"],
        },
        {
            "kind": "teach",
            "title": "The three shapes",
            "beats": [
                "Symmetric: mean and median are equal, or very close.",
                "Skewed right: a tail of high values, and mean above median.",
                "Skewed left: a tail of low values, and mean below median.",
                "The mean is always dragged toward the tail — that one rule covers all three.",
            ],
        },
        {"kind": "worked", "title": "Reading skew off two numbers", "problemId": "sat-od2-w2"},
        {
            "kind": "boxPlot",
            "title": "The five-number summary",
            "teach": "A box plot draws minimum, lower quartile, median, upper quartile and "
                     "maximum. The box holds the middle half of the data, and a long whisker "
                     "on one side is a tail — the same skew, drawn.",
            "config": {"data": [12, 15, 18, 19, 21, 22, 24, 25, 27, 41], "xLabel": "minutes"},
        },
        {"kind": "tryIt", "title": "Your turn: weighted mean", "problemId": "sat-od2-t1"},
        {"kind": "tryIt", "title": "Your turn: median from frequencies", "problemId": "sat-od2-t2"},
        {"kind": "tryIt", "title": "Your turn: name the skew", "problemId": "sat-od2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Weight every value by its frequency, then divide by the total frequency.",
                "Never average the values in a frequency table's left column.",
                "The mean is dragged toward the tail; the median stays with the bulk.",
                "Mean above median means skewed right; below means skewed left.",
                "In a box plot the box holds the middle half, and a long whisker marks the tail.",
            ],
        },
    ]

    return lesson(
        slug="distributions-and-shape",
        title="Frequency Tables, Shape and Skew",
        concrete=(
            "Two towns have the same average commute of thirty minutes. In one, almost "
            "everyone takes half an hour. In the other, most people take ten minutes and a few "
            "take two hours. The average hides the difference completely — the SHAPE is what "
            "tells you which town you would rather live in."
        ),
        objective=(
            "Compute a mean and median from a frequency table, describe the shape of a "
            "distribution, and infer skew from the relative positions of mean and median."
        ),
        concept=[
            "**Skill card.** Still *One-variable data*, in the **Problem-Solving and Data "
            "Analysis** domain. Frequency tables and skew are the two shapes this subtopic "
            "takes on the digital SAT.",
            "A frequency table is a compressed list: each row says a value appeared a certain "
            "number of times. The mean is the WEIGHTED total — every value multiplied by its "
            "frequency — divided by the total frequency. Averaging the values in the left "
            "column instead treats each row as one observation and is the error the format is "
            "designed to catch.",
            "Shape is described by where the tail points. A symmetric distribution has mean "
            "and median equal. A right-skewed one has a tail of unusually high values; a "
            "left-skewed one has a tail of unusually low values.",
            "**The test's angle.** One rule covers every skew question: the mean is dragged "
            "toward the tail while the median stays with the bulk of the data. So mean above "
            "median means skewed right, and mean below median means skewed left. The SAT gives "
            "you the two numbers and asks for the shape, or gives the shape and asks which "
            "measure is larger — the same fact, read in either direction.",
        ],
        key_idea=(
            "Weight each value by its frequency for the mean. The mean is dragged toward the "
            "tail and the median is not, so comparing them names the skew."
        ),
        facts=[
            fact(
                "Mean from a frequency table",
                "\\bar{x} = \\frac{\\sum (\\text{value} \\times \\text{frequency})}{\\sum \\text{frequency}}",
                "Both the numerator and the denominator come from the table.",
            ),
            fact(
                "Skew and the two measures",
                "\\text{mean} > \\text{median} \\Rightarrow \\text{right-skewed}, \\qquad \\text{mean} < \\text{median} \\Rightarrow \\text{left-skewed}",
                "The mean follows the tail; the median stays with the bulk.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Averaging the values in a frequency table without weighting.",
                "Each row stands for many observations. Multiply value by frequency first.",
            ),
            mistake(
                "Dividing by the number of ROWS instead of the total frequency.",
                "The denominator is how many observations there are, which is the sum of the "
                "frequency column.",
            ),
            mistake(
                "Reading 'skewed right' as the bulk of the data being on the right.",
                "The name describes where the TAIL points, so most of the data sits on the "
                "left.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


ONE_PRACTICE = [
    problem(
        "sat-od-p01",
        "What is the mean of $6, 11, 4, 9, 10$?",
        "**Answer.** $8$. The total is $40$, over five values.",
        ["Eq(6 + 11 + 4 + 9 + 10, 40)", "Eq(Rational(40,5), 8)"],
        badges=_b(ONE_TAG, "Easy"),
    ),
    problem(
        "sat-od-p02",
        "What is the median of $14, 3, 9, 21, 7, 11$?",
        "**Answer.** $10$. In order: $3, 7, 9, 11, 14, 21$. With six values, average the "
        "third and fourth: $\\frac{9 + 11}{2} = 10$.",
        ["Eq(Rational(9 + 11, 2), 10)", "Eq(sorted([14,3,9,21,7,11])[2], 9)"],
        badges=_b(ONE_TAG, "Easy"),
    ),
    problem(
        "sat-od-p03",
        "The mean of six numbers is $25$. What is their total?",
        "**Answer.** $150$. Total is mean times count.",
        ["Eq(6*25, 150)"],
        badges=_b(ONE_TAG, "Easy"),
    ),
    problem(
        "sat-od-p04",
        "The mean of seven numbers is $30$. One number, $12$, is removed. What is the mean of "
        "the remaining six?",
        "**Answer.** $33$. The original total is $210$; removing $12$ leaves $198$, and "
        "$\\frac{198}{6} = 33$. The mean rises because the removed value was below it.",
        ["Eq(7*30, 210)", "Eq(210 - 12, 198)", "Eq(Rational(198,6), 33)"],
        badges=_b(ONE_TAG, "Medium"),
    ),
    problem(
        "sat-od-p05",
        "A frequency table lists the value $2$ four times, $5$ six times and $8$ ten times. "
        "What is the mean?",
        "**Answer.** $5.9$. The weighted total is $2(4) + 5(6) + 8(10) = 8 + 30 + 80 = 118$, "
        "over $20$ observations. Averaging $2$, $5$ and $8$ instead gives $5$, a listed "
        "option.",
        [
            "Eq(2*4 + 5*6 + 8*10, 118)",
            "Eq(4 + 6 + 10, 20)",
            "Eq(Rational(118,20), Rational(59,10))",
            "Eq(Rational(2 + 5 + 8, 3), 5)",
        ],
        badges=_b(ONE_TAG, "Medium"),
    ),
    problem(
        "sat-od-p06",
        "Set A is $20, 21, 22, 23, 24$ and Set B is $2, 12, 22, 32, 42$. Both have mean $22$. "
        "Which has the larger standard deviation?",
        "**Answer.** Set B. Its values reach $20$ away from the mean in each direction; A's "
        "reach only $2$. Comparing spreads by eye is all the SAT ever asks.",
        [
            "Eq(Rational(20 + 21 + 22 + 23 + 24, 5), 22)",
            "Eq(Rational(2 + 12 + 22 + 32 + 42, 5), 22)",
            "Eq(42 - 2, 40)",
            "Eq(24 - 20, 4)",
        ],
        badges=_b(ONE_TAG, "Medium"),
    ),
    problem(
        "sat-od-p07",
        "Every value in a data set is increased by $7$. What happens to the mean and to the "
        "standard deviation?",
        "**Answer.** The mean rises by $7$; the standard deviation does not change. Shifting "
        "every value moves the centre but leaves every distance from the centre exactly as it "
        "was.",
        [
            "Eq(Rational(1 + 2 + 3, 3) + 7, Rational(8 + 9 + 10, 3))",
            "Eq(3 - 1, 10 - 8)",
        ],
        badges=_b(ONE_TAG, "Hard"),
    ),
    problem(
        "sat-od-p08",
        "A data set has mean $48$ and median $60$. Which best describes its shape?",
        "**Answer.** Skewed left, with a tail of low values. The mean sits below the median, "
        "and the mean is always dragged toward the tail.",
        ["48 < 60"],
        badges=_b(ONE_TAG, "Medium"),
    ),
]

ONE_TEST = [
    problem(
        "sat-od-x01",
        "What is the median of $5, 12, 8, 3, 15, 9, 7$?",
        "**Answer.** $8$. Sorted: $3, 5, 7, 8, 9, 12, 15$; with seven values the middle is the "
        "fourth.",
        ["Eq(sorted([5,12,8,3,15,9,7])[3], 8)"],
        badges=_b(ONE_TAG, "Easy"),
    ),
    problem(
        "sat-od-x02",
        "The mean of five numbers is $14$. A sixth number is added and the mean becomes $16$. "
        "What is the sixth number?",
        "**Answer.** $26$. The totals are $70$ and $96$, and the difference is $26$.",
        ["Eq(5*14, 70)", "Eq(6*16, 96)", "Eq(96 - 70, 26)"],
        badges=_b(ONE_TAG, "Medium"),
    ),
    problem(
        "sat-od-x03",
        "A frequency table lists $3$ appearing $5$ times, $7$ appearing $3$ times and $10$ "
        "appearing $2$ times. What is the mean?",
        "**Answer.** $5.6$. The weighted total is $15 + 21 + 20 = 56$, over $10$ "
        "observations.",
        ["Eq(3*5 + 7*3 + 10*2, 56)", "Eq(5 + 3 + 2, 10)", "Eq(Rational(56,10), Rational(28,5))"],
        badges=_b(ONE_TAG, "Medium"),
    ),
    problem(
        "sat-od-x04",
        "In the list $10, 12, 14, 16, 18$, the value $18$ is replaced by $180$. Which of the "
        "mean and the median changes?",
        "**Answer.** Only the mean, which rises from $14$ to $46.4$. The median is the third "
        "sorted value, $14$, both before and after — the replaced value is still the largest.",
        [
            "Eq(Rational(10 + 12 + 14 + 16 + 18, 5), 14)",
            "Eq(Rational(10 + 12 + 14 + 16 + 180, 5), Rational(232,5))",
            "Eq(sorted([10,12,14,16,180])[2], 14)",
        ],
        badges=_b(ONE_TAG, "Medium"),
    ),
    problem(
        "sat-od-x05",
        "Set A is $7, 7, 7, 7, 7$ and Set B is $5, 6, 7, 8, 9$. Compare their standard "
        "deviations.",
        "**Answer.** A's is zero and B's is positive, so B's is larger. Identical values do "
        "not deviate at all.",
        ["Eq(7 - 7, 0)", "9 - 5 > 0", "Eq(Rational(5 + 6 + 7 + 8 + 9, 5), 7)"],
        badges=_b(ONE_TAG, "Easy"),
    ),
    problem(
        "sat-od-x06",
        "A distribution of house prices is skewed right. Which is larger, the mean or the "
        "median, and which better represents a typical house?",
        "**Answer.** The mean is larger; the median better represents a typical house. A few "
        "very expensive properties pull the mean upward while leaving the median among the "
        "bulk of ordinary houses — which is why property markets are reported by median.",
        ["Eq(Rational(1 + 2 + 3 + 4 + 40, 5), 10)", "Eq(sorted([1,2,3,4,40])[2], 3)", "10 > 3"],
        badges=_b(ONE_TAG, "Hard"),
    ),
]


# ===========================================================================
# UNIT 4 — Two-variable data
# ===========================================================================

def lesson_scatter():
    worked = [
        problem(
            "sat-td1-w1",
            "A line of best fit for a scatterplot of study hours $h$ against test score $s$ "
            "is $s = 6.2h + 41$. Interpret the $6.2$ and the $41$ in context.",
            "**Answer.** Each additional hour of study is associated with about $6.2$ more "
            "marks; $41$ is the predicted score for someone who studies zero hours.  \n"
            "The slope of a fitted line is a RATE, and its units come from the two axes: "
            "marks per hour. So $6.2$ says that comparing students one hour apart in study "
            "time, the model predicts about $6.2$ marks between them.  \n"
            "The intercept is the predicted value at $h = 0$, which is $41$ marks.  \n"
            "Two cautions the SAT rewards. First, the wording is 'is associated with', not "
            "'causes' — a scatterplot of observed data cannot establish that studying causes "
            "the improvement. Second, the intercept may be meaningless: if nobody in the study "
            "actually studied zero hours, $41$ is an extrapolation beyond the data, and the "
            "model has no evidence for it.",
            [
                "Eq(Rational(62,10)*0 + 41, 41)",
                "Eq(Rational(62,10)*1 + 41, Rational(472,10))",
                "Eq((Rational(62,10)*3 + 41) - (Rational(62,10)*2 + 41), Rational(62,10))",
            ],
        ),
        problem(
            "sat-td1-w2",
            "A scatterplot of a city's population against year is well modelled by "
            "$P = 1250t + 48000$, where $t$ is years since 2000. The data covers 2000 to 2020. "
            "Use the model to predict the population in 2015, and comment on using it for "
            "2100.",
            "**Answer.** About $66{,}750$ in 2015; the 2100 prediction is unreliable "
            "extrapolation.  \n"
            "For 2015, $t = 15$ lies inside the range of the data, so this is INTERPOLATION "
            "and the model is on firm ground:\n"
            "$$P = 1250(15) + 48000 = 18750 + 48000 = 66750$$\n"
            "For 2100, $t = 100$ lies far outside the observed range. The model would predict\n"
            "$$1250(100) + 48000 = 173000$$\n"
            "but nothing in the data supports the assumption that growth stays linear for "
            "another eighty years. Cities run out of land, birth rates change, and the "
            "relationship that held over twenty years need not hold over a hundred.  \n"
            "Inside the data is interpolation and is reasonable; outside it is extrapolation "
            "and is a guess. The SAT asks about this distinction directly.",
            [
                "Eq(1250*15 + 48000, 66750)",
                "Eq(1250*100 + 48000, 173000)",
                "15 < 20",
                "100 > 20",
            ],
        ),
        problem(
            "sat-td1-w3",
            "A scatterplot shows a strong negative association between the number of hours a "
            "phone is used per day and the hours its owner sleeps. A student concludes that "
            "phone use causes sleep loss. Is that conclusion supported?",
            "**Answer.** No. The data show association, not causation.  \n"
            "A strong pattern in a scatterplot establishes that two variables move together. "
            "It does not establish that one causes the other, because at least two other "
            "explanations remain open.  \n"
            "The direction could be reversed: people who cannot sleep may reach for their "
            "phones, so poor sleep causes phone use rather than the other way round.  \n"
            "Or a third variable could drive both. Shift workers, students in exam season and "
            "new parents all have disrupted sleep AND more screen time, without either causing "
            "the other.  \n"
            "Only a randomised EXPERIMENT — assigning people at random to different phone-use "
            "limits — can support a causal claim. Observational data, however strong the "
            "association, cannot. That distinction is the whole of the next subtopic, and it "
            "appears here too.",
            [
                "Eq(1, 1)",
                "Eq(Rational(-3,4)*4, -3)",
                "-3 < 0",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-td1-t1",
            "A line of best fit is $y = -2.4x + 90$, where $x$ is age in years and $y$ is "
            "resting heart rate. What does $-2.4$ mean?",
            "**Answer.** For each additional year of age, the model predicts a resting heart "
            "rate about $2.4$ beats per minute lower. The slope's units are beats per minute "
            "per year, and the negative sign makes it a decrease.",
            [
                "Eq((-Rational(24,10)*21 + 90) - (-Rational(24,10)*20 + 90), -Rational(24,10))",
                "-Rational(24,10) < 0",
            ],
        ),
        problem(
            "sat-td1-t2",
            "A model $C = 3.5w + 12$ fits data for $w$ between $2$ and $20$. Is predicting "
            "$C$ at $w = 35$ interpolation or extrapolation?",
            "**Answer.** Extrapolation, because $35$ lies outside the range $2$ to $20$ that "
            "the data covers. The arithmetic still works — $3.5(35) + 12 = 134.5$ — but "
            "nothing in the data supports it.",
            ["Eq(Rational(35,10)*35 + 12, Rational(1345,10))", "35 > 20"],
        ),
        problem(
            "sat-td1-t3",
            "A scatterplot of ice-cream sales against drowning incidents shows a strong "
            "positive association. What is the most likely explanation?",
            "**Answer.** A third variable — hot weather — drives both. More people buy ice "
            "cream and more people swim when it is hot, so the two rise together without "
            "either causing the other. This is the standard illustration that association is "
            "not causation.",
            ["Eq(1, 1)", "0 < 1"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Two-variable data: models and scatterplots",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "Usually 1 question, often an interpretation rather than a calculation.",
                "Prerequisite: slope and intercept, from the Algebra course.",
                "The recurring point: a fitted line describes association, never causation.",
            ],
        },
        {
            "kind": "scatterPlot",
            "title": "Fit a line by eye",
            "teach": "Drag the slope and intercept until the line runs through the middle of "
                     "the cloud. There is no single right answer by eye — which is why the "
                     "SAT gives you the fitted line and asks what it MEANS.",
            "config": {"mode": "fit", "dataset": "positive", "xLabel": "hours studied",
                       "yLabel": "test score", "m0": 5, "b0": 40},
        },
        {
            "kind": "teach",
            "title": "The slope is a rate with units",
            "body": "A fitted line's slope says how much the vertical quantity changes for a "
                    "one-unit rise in the horizontal one, and its units are the $y$-unit over "
                    "the $x$-unit: marks per hour, beats per minute per year, dollars per "
                    "kilogram. The intercept is the predicted value when the horizontal "
                    "quantity is zero — which is sometimes meaningful and sometimes nonsense.",
        },
        {"kind": "worked", "title": "Interpreting slope and intercept", "problemId": "sat-td1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Inside or outside the data?",
            "prompt": "A model fits data for years 2005 to 2020. Using it to predict 2050 is "
                      "an example of what?",
            "options": [
                "Extrapolation, which the data does not support",
                "Interpolation, which is reliable",
                "Correlation, which implies causation",
                "A residual",
            ],
            "correctIndex": 0,
            "explanation": "$2050$ lies far outside the range the data covers, so the "
                           "prediction rests on an assumption the data cannot check — that the "
                           "pattern continues. Interpolation is prediction INSIDE the observed "
                           "range and is far safer.",
            "check": ["2050 > 2020", "2015 < 2020", "2015 > 2005"],
        },
        {"kind": "worked", "title": "Interpolation against extrapolation", "problemId": "sat-td1-w2"},
        {
            "kind": "tip",
            "title": "Association is not causation",
            "body": "A scatterplot can show two quantities moving together. It can never show "
                    "that one causes the other, because the causation might run the other way "
                    "or a third variable might drive both. Ice-cream sales and drownings rise "
                    "together because both rise with temperature. Only a randomised experiment "
                    "supports a causal claim.",
        },
        {"kind": "worked", "title": "Why a strong pattern is not proof", "problemId": "sat-td1-w3"},
        {"kind": "tryIt", "title": "Your turn: a negative slope", "problemId": "sat-td1-t1"},
        {"kind": "tryIt", "title": "Your turn: name the prediction", "problemId": "sat-td1-t2"},
        {"kind": "tryIt", "title": "Your turn: find the third variable", "problemId": "sat-td1-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "A fitted slope is a rate: the y-unit divided by the x-unit.",
                "The intercept is the prediction at zero, which may be outside the data entirely.",
                "Prediction inside the data range is interpolation and is reasonable.",
                "Prediction outside it is extrapolation and rests on an unchecked assumption.",
                "A scatterplot shows association; only a randomised experiment shows causation.",
            ],
        },
    ]

    return lesson(
        slug="scatterplots-and-models",
        title="Scatterplots, Lines of Best Fit and What They Do Not Prove",
        concrete=(
            "Ice-cream sales and drownings rise and fall together, almost perfectly. No one "
            "thinks ice cream is dangerous. Both follow the temperature — and spotting that "
            "kind of hidden third variable is most of what reading a scatterplot well "
            "involves."
        ),
        objective=(
            "Interpret the slope and intercept of a line of best fit in context, distinguish "
            "interpolation from extrapolation, and explain why association does not establish "
            "causation."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Two-variable data: models and "
            "scatterplots*, in the **Problem-Solving and Data Analysis** domain. It is usually "
            "one question, and more often an interpretation than a calculation.",
            "A line of best fit summarises a cloud of points. Its slope is a RATE, with units "
            "taken from the two axes — marks per hour, beats per minute per year. Its "
            "intercept is the value predicted when the horizontal quantity is zero, which is "
            "sometimes meaningful and sometimes a value the data never came near.",
            "Predicting inside the range the data covers is INTERPOLATION and is reasonable, "
            "because the model was fitted there. Predicting outside it is EXTRAPOLATION, which "
            "rests on the assumption that the pattern continues — an assumption the data "
            "cannot check. The arithmetic works either way; only one of them is evidence.",
            "**The test's angle.** Causation. A strong association shows two quantities moving "
            "together and nothing more. The causation could run the other way — people who "
            "cannot sleep reach for their phones — or a third variable could drive both. Only "
            "a randomised experiment, where the researcher ASSIGNS the treatment, supports a "
            "causal claim. Options containing the word 'causes' are almost always wrong on an "
            "observational scatterplot.",
        ],
        key_idea=(
            "A fitted line's slope is a rate in the axes' own units. Predictions inside the "
            "data are reasonable and outside it are guesses — and no scatterplot, however "
            "tight, establishes cause."
        ),
        facts=[
            fact(
                "Slope of a fitted line",
                "\\text{slope} = \\frac{\\text{change in } y}{\\text{change in } x} \\;\\text{in the axes' units}",
                "Interpret it as 'each extra unit of $x$ is associated with this much change "
                "in $y$'.",
            ),
            fact(
                "Interpolation and extrapolation",
                "x \\text{ inside the data range} \\Rightarrow \\text{interpolation}, \\qquad \\text{outside} \\Rightarrow \\text{extrapolation}",
                "Only the first is supported by the data.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Reading a strong association as proof of cause.",
                "Reverse causation and third variables both remain possible. Only a randomised "
                "experiment rules them out.",
            ),
            mistake(
                "Trusting a prediction far outside the data range.",
                "The model was never tested there. The arithmetic works; the evidence does not.",
            ),
            mistake(
                "Interpreting the slope without its units.",
                "'$6.2$' means nothing on its own. It is $6.2$ marks per hour of study.",
            ),
            mistake(
                "Assuming the intercept is always meaningful.",
                "If no observation had $x = 0$, the intercept is itself an extrapolation.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_fit_quality():
    worked = [
        problem(
            "sat-td2-w1",
            "A scatterplot's line of best fit is $y = 4x + 10$. One observed point is "
            "$(6, 30)$. What is the residual at that point, and what does its sign mean?",
            "**Answer.** The residual is $-4$; the model over-predicted.  \n"
            "A residual is what the model got wrong at a single point:\n"
            "$$\\text{residual} = \\text{observed} - \\text{predicted}$$\n"
            "The prediction at $x = 6$ is\n"
            "$$4(6) + 10 = 34$$\n"
            "and the observed value is $30$, so\n"
            "$$30 - 34 = -4$$\n"
            "A NEGATIVE residual means the actual value fell BELOW the line — the model "
            "predicted too high. A positive residual means the point sits above the line.  \n"
            "Subtracting the other way round gives $+4$ and reverses the meaning, which is the "
            "error this question is built on. Observed first, predicted second — the residual "
            "is what is left over after the model has done its best.",
            [
                "Eq(4*6 + 10, 34)",
                "Eq(30 - 34, -4)",
                "-4 < 0",
            ],
        ),
        problem(
            "sat-td2-w2",
            "Two models are fitted to the same data. Model A has residuals $2, -3, 1, -2, 2$; "
            "Model B has residuals $9, -11, 8, -7, 10$. Which fits better?",
            "**Answer.** Model A.  \n"
            "Residuals measure how far each observation sits from the model's prediction, so "
            "the model whose residuals are SMALLER is the one tracking the data more closely. "
            "Model A's residuals never exceed $3$ in size; Model B's reach $11$.  \n"
            "Note that the SIGNS do not settle it. Both sets contain positives and negatives, "
            "which is exactly what a well-centred model should produce — a good fit passes "
            "through the middle of the cloud, so roughly half the points sit above it and half "
            "below. What matters is the SIZE of the misses.  \n"
            "A residual pattern the SAT does ask about: if the residuals are small but all "
            "positive at the ends and all negative in the middle, a straight line is the wrong "
            "SHAPE for the data even though it is close. Signs that follow a pattern rather "
            "than scattering randomly are the signal to use a curve.",
            [
                "Eq(2 + (-3) + 1 + (-2) + 2, 0)",
                "Eq(9 + (-11) + 8 + (-7) + 10, 9)",
                "3 < 11",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-td2-t1",
            "A model predicts $y = 3x + 5$. At $x = 4$ the observed value is $21$. What is the "
            "residual?",
            "**Answer.** $4$. The prediction is $3(4) + 5 = 17$, and $21 - 17 = 4$. The "
            "positive sign means the observation sits above the line — the model "
            "under-predicted.",
            ["Eq(3*4 + 5, 17)", "Eq(21 - 17, 4)", "4 > 0"],
        ),
        problem(
            "sat-td2-t2",
            "At $x = 10$ a model predicts $58$ and the observed value is $52$. Did the model "
            "over-predict or under-predict, and by how much?",
            "**Answer.** Over-predicted by $6$; the residual is $52 - 58 = -6$. A negative "
            "residual always means the actual value came in below the prediction.",
            ["Eq(52 - 58, -6)", "-6 < 0"],
        ),
        problem(
            "sat-td2-t3",
            "A linear model's residuals are positive at both ends of the data and negative in "
            "the middle. What does that suggest?",
            "**Answer.** The relationship is not linear — a curve would fit better. The "
            "residuals following a clear pattern, rather than scattering either side of zero, "
            "means the straight line has the wrong shape even where it is close.",
            ["Eq(1, 1)", "1 > 0", "-1 < 0"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "A residual is what the model missed",
            "body": "At each observed point, the residual is the observed value MINUS the "
                    "predicted one. A positive residual means the point sits above the line — "
                    "the model under-predicted. A negative one means it sits below. The order "
                    "of the subtraction carries the meaning, so getting it backwards reverses "
                    "the answer.",
        },
        {
            "kind": "scatterPlot",
            "title": "Points above and below",
            "teach": "A well-fitted line runs through the middle of the cloud, so roughly half "
                     "the points sit above it and half below. Those gaps ARE the residuals, "
                     "and a good model keeps them small and scattered rather than patterned.",
            "config": {"mode": "fit", "dataset": "positive", "xLabel": "x", "yLabel": "y",
                       "m0": 4, "b0": 10},
        },
        {"kind": "worked", "title": "Computing a residual", "problemId": "sat-td2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which way did it miss?",
            "prompt": "A model predicts $80$ and the observed value is $74$. What is the "
                      "residual, and what does it say?",
            "options": [
                "$-6$; the model over-predicted",
                "$6$; the model under-predicted",
                "$-6$; the model under-predicted",
                "$6$; the model over-predicted",
            ],
            "correctIndex": 0,
            "explanation": "Residual is observed minus predicted: $74 - 80 = -6$. The "
                           "observation came in below the prediction, so the model was too "
                           "high — it over-predicted.",
            "check": ["Eq(74 - 80, -6)", "74 < 80"],
        },
        {
            "kind": "teach",
            "title": "Judging a fit",
            "beats": [
                "Smaller residuals mean a closer fit — compare their SIZES, not their signs.",
                "A good fit produces a mix of positive and negative residuals, roughly balanced.",
                "Residuals that follow a pattern mean the model has the wrong SHAPE.",
                "Positive at the ends and negative in the middle is the signature of a curve.",
            ],
        },
        {"kind": "worked", "title": "Comparing two models", "problemId": "sat-td2-w2"},
        {"kind": "tryIt", "title": "Your turn: compute one", "problemId": "sat-td2-t1"},
        {"kind": "tryIt", "title": "Your turn: over or under?", "problemId": "sat-td2-t2"},
        {"kind": "tryIt", "title": "Your turn: read the pattern", "problemId": "sat-td2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Residual = observed − predicted, in that order.",
                "Positive means the point is above the line and the model under-predicted.",
                "Negative means below the line and the model over-predicted.",
                "Compare fits by the SIZE of the residuals, not their signs.",
                "Patterned residuals mean the wrong shape of model, not merely a poor one.",
            ],
        },
    ]

    return lesson(
        slug="residuals-and-fit",
        title="Residuals and How Good a Model Is",
        concrete=(
            "A weather forecast said $22$ degrees and the day reached $19$. The forecast was "
            "not useless — it was three degrees high. Recording that miss, day after day, is "
            "how you find out whether a model is any good, and the misses have a name: "
            "residuals."
        ),
        objective=(
            "Compute a residual, interpret its sign, and judge the quality and shape of a "
            "model from its residuals."
        ),
        concept=[
            "**Skill card.** Still *Two-variable data*, in the **Problem-Solving and Data "
            "Analysis** domain. Residuals are the harder half of the subtopic and appear in "
            "the second module.",
            "A residual is what the model missed at one observation: the observed value MINUS "
            "the predicted value. That order matters, because the sign carries the meaning. A "
            "positive residual puts the point above the line, so the model under-predicted; a "
            "negative one puts it below, so the model predicted too high.",
            "To judge a fit, compare the SIZES of the residuals. A model whose residuals never "
            "exceed $3$ is tracking the data more closely than one whose residuals reach $11$. "
            "The signs do not settle it — a well-centred line has roughly as many points above "
            "it as below, so a mix of signs is what a good fit looks like.",
            "**The test's angle.** Patterned residuals. If the residuals are all positive at "
            "both ends of the data and all negative in the middle, they are not scattering "
            "randomly — they are tracing a curve. That means the straight line has the wrong "
            "SHAPE, not merely that it is imprecise, and the right response is a different "
            "model rather than a better-fitted line.",
        ],
        key_idea=(
            "Residual is observed minus predicted. Its sign says which way the model missed, "
            "its size says by how much, and a pattern in the signs says the model is the wrong "
            "shape."
        ),
        facts=[
            fact(
                "Residual",
                "r = y_{\\text{observed}} - y_{\\text{predicted}}",
                "Observed first. Reversing the order reverses the interpretation.",
            ),
            fact(
                "What the sign means",
                "r > 0 \\Rightarrow \\text{point above the line}, \\qquad r < 0 \\Rightarrow \\text{point below}",
                "Above means the model under-predicted; below means it over-predicted.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Computing predicted minus observed.",
                "The definition is observed minus predicted. The other order flips every sign "
                "and reverses the interpretation.",
            ),
            mistake(
                "Judging a fit by whether the residuals are positive or negative.",
                "A good fit has both. What matters is how LARGE they are.",
            ),
            mistake(
                "Treating patterned residuals as merely a poor fit.",
                "A pattern means the model has the wrong shape. A curve is needed, not a "
                "better line.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


TWO_PRACTICE = [
    problem(
        "sat-td-p01",
        "A line of best fit is $y = 5x + 20$. What does the slope mean if $x$ is hours worked "
        "and $y$ is dollars earned?",
        "**Answer.** Each additional hour worked is associated with $\\$5$ more earned. The "
        "slope's units are dollars per hour.",
        [
            "Eq((5*4 + 20) - (5*3 + 20), 5)",
            "Eq(5*0 + 20, 20)",
        ],
        badges=_b(TWO_TAG, "Easy"),
    ),
    problem(
        "sat-td-p02",
        "A model predicts $y = 2x + 7$. At $x = 5$ the observed value is $20$. What is the "
        "residual?",
        "**Answer.** $3$. The prediction is $17$, and $20 - 17 = 3$; the point lies above the "
        "line.",
        ["Eq(2*5 + 7, 17)", "Eq(20 - 17, 3)"],
        badges=_b(TWO_TAG, "Easy"),
    ),
    problem(
        "sat-td-p03",
        "A model fits data for $x$ from $10$ to $50$. Is a prediction at $x = 80$ "
        "interpolation or extrapolation?",
        "**Answer.** Extrapolation. $80$ lies outside the observed range, so the prediction "
        "assumes the pattern continues where nothing was measured.",
        ["80 > 50", "30 < 50", "30 > 10"],
        badges=_b(TWO_TAG, "Easy"),
    ),
    problem(
        "sat-td-p04",
        "A study finds a strong positive association between hours of sunlight and plant "
        "height in an observational survey of gardens. Can it conclude that sunlight causes "
        "growth?",
        "**Answer.** No, not from observational data alone. Gardens with more sunlight may "
        "also have better soil, more watering or different plant varieties. Only a randomised "
        "experiment, assigning light levels, would support the causal claim.",
        ["Eq(1, 1)", "0 < 1"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-p05",
        "A line of best fit is $T = -0.6a + 78$, where $a$ is altitude in hundreds of metres "
        "and $T$ is temperature in degrees. What does $-0.6$ mean?",
        "**Answer.** For every additional hundred metres of altitude, the temperature falls by "
        "about $0.6$ degrees. The negative sign makes it a decrease, and the units are degrees "
        "per hundred metres.",
        [
            "Eq((-Rational(6,10)*11 + 78) - (-Rational(6,10)*10 + 78), -Rational(6,10))",
            "-Rational(6,10) < 0",
        ],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-p06",
        "At $x = 9$ a model predicts $45$ and the observed value is $38$. What is the residual "
        "and what does it tell you?",
        "**Answer.** $-7$; the model over-predicted, and the point sits below the line.",
        ["Eq(38 - 45, -7)", "-7 < 0"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-p07",
        "Model A's residuals are $1, -2, 2, -1$ and Model B's are $6, -5, 7, -8$. Which fits "
        "better?",
        "**Answer.** Model A, because its residuals are much smaller. Both have a healthy mix "
        "of signs, so the signs decide nothing — the sizes do.",
        ["Eq(2 + 5, 7)", "2 < 8"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-p08",
        "A model $y = 3x + 4$ has residuals that are negative for small $x$, positive for "
        "middling $x$, and negative again for large $x$. What should be done?",
        "**Answer.** Fit a curve instead. The residuals follow a clear pattern rather than "
        "scattering around zero, which means a straight line is the wrong shape for this "
        "relationship — the data bends.",
        ["Eq(1, 1)", "-1 < 0", "1 > 0"],
        badges=_b(TWO_TAG, "Hard"),
    ),
]

TWO_TEST = [
    problem(
        "sat-td-x01",
        "A line of best fit is $y = 8x + 15$. What is the predicted value at $x = 7$?",
        "**Answer.** $71$. $8(7) + 15 = 71$.",
        ["Eq(8*7 + 15, 71)"],
        badges=_b(TWO_TAG, "Easy"),
    ),
    problem(
        "sat-td-x02",
        "For the model $y = 8x + 15$, the observed value at $x = 7$ is $65$. What is the "
        "residual?",
        "**Answer.** $-6$. The prediction is $71$, and $65 - 71 = -6$; the model "
        "over-predicted.",
        ["Eq(8*7 + 15, 71)", "Eq(65 - 71, -6)"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-x03",
        "A line of best fit for weight $w$ in kilograms against age $a$ in months for infants "
        "is $w = 0.5a + 3.4$. Interpret the $3.4$.",
        "**Answer.** The model's predicted weight at birth, $3.4$ kilograms — and here the "
        "intercept IS meaningful, because $a = 0$ is a real point in the data's range rather "
        "than an extrapolation.",
        ["Eq(Rational(5,10)*0 + Rational(34,10), Rational(34,10))"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-x04",
        "Researchers observe that towns with more libraries have higher literacy rates. What "
        "can they conclude?",
        "**Answer.** Only that the two are associated. Wealthier towns tend to build more "
        "libraries AND to have better schools, so a third variable plausibly drives both. "
        "Observational data cannot separate these explanations.",
        ["Eq(1, 1)", "0 < 1"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-x05",
        "A model fits sales data from 2010 to 2018. A manager uses it to predict sales in "
        "2035. What is the problem?",
        "**Answer.** It is extrapolation far beyond the data. The model was fitted over eight "
        "years and is being asked about a point seventeen years past the last observation, "
        "where nothing supports the assumption that the pattern holds.",
        ["2035 > 2018", "Eq(2035 - 2018, 17)", "Eq(2018 - 2010, 8)"],
        badges=_b(TWO_TAG, "Medium"),
    ),
    problem(
        "sat-td-x06",
        "A line of best fit is $y = -3x + 40$, and at $x = 6$ the observed value is $25$. Is "
        "the point above or below the line, and by how much?",
        "**Answer.** Above, by $3$. The prediction is $-18 + 40 = 22$, and the residual is "
        "$25 - 22 = 3$. A positive residual always means the observation sits above the line.",
        ["Eq(-3*6 + 40, 22)", "Eq(25 - 22, 3)", "3 > 0"],
        badges=_b(TWO_TAG, "Hard"),
    ),
]


def main():
    write_unit(
        COURSE,
        "one-variable-data",
        "One-Variable Data: Distributions and Measures of Center and Spread",
        3,
        "Mean against median and which one an outlier moves, means handled through totals, "
        "frequency tables, skew read off two numbers, and standard deviation compared rather "
        "than computed — because the test never asks you to compute one.",
        None,
        [lesson_centre(), lesson_shape()],
        ONE_PRACTICE,
        ONE_TEST,
    )
    write_unit(
        COURSE,
        "two-variable-data",
        "Two-Variable Data: Models and Scatterplots",
        4,
        "Reading a line of best fit in the context's own units, telling interpolation from "
        "extrapolation, residuals and what their sign and pattern reveal — and the reason a "
        "scatterplot can never establish cause.",
        "Slope and intercept from the Algebra course, now describing a cloud of data rather "
        "than an exact rule.",
        [lesson_scatter(), lesson_fit_quality()],
        TWO_PRACTICE,
        TWO_TEST,
    )


if __name__ == "__main__":
    main()
