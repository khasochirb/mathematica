#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 8: Modelling with Functions.

CCSS Integrated Math III capstone modelling unit: F-LE.1 (distinguish
situations modelled by linear vs exponential functions — equal
differences vs equal factors over equal intervals), F-LE.2 (construct
linear and exponential functions from a graph, a description, or two
points), F-BF.1 (write a function that describes a relationship between
quantities), S-ID.6a-b (fit a function to data; assess the fit by
plotting and analysing residuals), F-IF.4/5 (interpret key features and
relate the domain of a function to the quantitative relationship it
describes), and the modelling cycle of the CCSS Modelling conceptual
category.

The unit's through-line: THE PATHWAY IN REVERSE. For three courses the
student was handed a function and asked about its behaviour. The
capstone flips the direction: here is a situation, here is data — YOU
pick the family, YOU build the function, YOU check it against reality
(residuals), and YOU say where it stops being true (domain, model
breakdown). Every family met in IM1–IM3 shows up again, this time as a
candidate to be chosen or rejected on evidence: constant differences,
constant ratios, constant second differences, and the honesty to say
"this model is done" when extrapolation turns absurd.

Run: python3 scripts/im/build_im3_unit8.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — choosing a function family
# ===========================================================================

def lesson_choosing():
    return lesson(
        slug="choosing-a-function-family",
        title="Choosing a Family",
        concrete=(
            "Three savings plans grow on a shelf: one adds the same amount "
            "every month, one multiplies by the same factor every month, "
            "and a thrown ball's height does neither — it rises, tops out, "
            "and falls. Before any equation gets written, the DATA has "
            "already picked its function family, and it announces the "
            "choice in a whisper you can compute: take differences, take "
            "ratios, take differences of the differences. The family that "
            "stays constant is the one the data belongs to."
        ),
        objective=(
            "Decide from a table or a situation which function family fits "
            "— linear, exponential, or quadratic — using constant "
            "differences, constant ratios, and constant second "
            "differences, and justify the choice."
        ),
        concept=[
            "Equal steps in $x$ are the test bench. A LINEAR function "
            "adds the same amount over every step: its first differences "
            "are constant, and that constant is the slope. The table "
            "$7, 10, 13, 16, 19$ steps by $+3$ every time — linear, "
            "$y = 3x + 7$, no further questions.",

            "An EXPONENTIAL function multiplies by the same factor over "
            "every step: its RATIOS are constant. The table $5, 10, 20, "
            "40$ doubles each step — exponential, $y = 5 \\cdot 2^x$. "
            "Growth by percent is this in disguise: adding $4\\%$ each "
            "year is multiplying by $1.04$ each year, so percent change "
            "always says exponential.",

            "A QUADRATIC function does neither, but its first "
            "differences change by a constant amount: the SECOND "
            "differences are constant, and they equal $2a$. The table "
            "$3, 8, 17, 30, 47$ has first differences $5, 9, 13, 17$ — "
            "not constant — but second differences $4, 4, 4$: quadratic "
            "with $a = 2$. Falling objects, areas against side length, "
            "and braking distances all live here.",

            "Situations declare their family in words before any table "
            "appears. \"The same amount per unit\" — linear. \"The same "
            "percent per unit\" or \"doubles/halves every ...\" — "
            "exponential. \"Accelerating from rest\", \"area of a "
            "square\" — quadratic. The skill is hearing the constant: "
            "constant DIFFERENCE, constant FACTOR, or constant CHANGE "
            "OF CHANGE.",
        ],
        key_idea=(
            "Over equal x-steps, the family shows itself: constant first "
            "differences mean linear, constant ratios mean exponential, "
            "constant second differences mean quadratic. Compute all "
            "three and believe the one that holds still."
        ),
        facts=[
            fact("The linear signature", "\\Delta y = \\text{constant}",
                 "Equal differences over equal intervals — the constant "
                 "is the slope."),
            fact("The exponential signature",
                 "\\dfrac{y_{n+1}}{y_n} = \\text{constant}",
                 "Equal factors over equal intervals — the constant is "
                 "the base b."),
            fact("The quadratic signature",
                 "\\Delta(\\Delta y) = \\text{constant} = 2a",
                 "First differences change steadily; the second "
                 "difference equals twice the leading coefficient."),
            fact("Percent change is a factor",
                 "+4\\% \\ \\text{per year} \\iff \\times 1.04 \\ \\text{per year}",
                 "Any per-unit percent change is exponential, growth or "
                 "decay."),
            fact("The whisper test",
                 "\\text{differences} \\to \\text{ratios} \\to \\text{second differences}",
                 "Run the three tests on equal x-steps; the family whose "
                 "test is constant is the fit."),
        ],
        worked=[
            problem(
                "im3-u8-l1-we1",
                "For equal steps $x = 0, 1, 2, 3, 4$ a table reads "
                "$y = 7, 10, 13, 16, 19$. Identify the family and write "
                "the function.",
                "**Take first differences.** $10 - 7 = 3$, $13 - 10 = 3$, "
                "$16 - 13 = 3$, $19 - 16 = 3$ — constant. The family is "
                "linear, and the constant IS the slope."
                "**Read off the pieces.** At $x = 0$ the table says $7$: "
                "that is the intercept. So $y = 3x + 7$."
                "**Check the far end.** $3 \\cdot 4 + 7 = 19$ — matches "
                "the last entry, so the model reproduces the whole "
                "table.",
                [
                    "Eq(10 - 7, 3)",
                    "Eq(19 - 16, 3)",
                    "Eq(3*4 + 7, 19)",
                ],
            ),
            problem(
                "im3-u8-l1-we2",
                "For $x = 0, 1, 2, 3$ a table reads $y = 5, 10, 20, 40$. "
                "Identify the family and write the function.",
                "**Differences first.** $5, 10, 20$ — not constant, so "
                "not linear."
                "**Try ratios.** $\\frac{10}{5} = 2$, $\\frac{20}{10} = "
                "2$, $\\frac{40}{20} = 2$ — constant factor. Exponential "
                "with base $2$."
                "**Anchor at zero.** The $x = 0$ entry is the starting "
                "amount $a = 5$, so $y = 5 \\cdot 2^x$. Check: $5 \\cdot "
                "2^3 = 40$ — the table's last word.",
                [
                    "Eq(Rational(10, 5), 2)",
                    "Eq(Rational(40, 20), 2)",
                    "Eq(5*2**3, 40)",
                ],
            ),
            problem(
                "im3-u8-l1-we3",
                "For $x = 0, 1, 2, 3, 4$ a table reads $y = 3, 8, 17, "
                "30, 47$. Identify the family and write the function.",
                "**First differences.** $5, 9, 13, 17$ — climbing, not "
                "constant: rules out linear."
                "**Second differences.** $9 - 5 = 4$, $13 - 9 = 4$, "
                "$17 - 13 = 4$ — constant. Quadratic, with $2a = 4$, so "
                "$a = 2$."
                "**Pin down the rest.** At $x = 0$: $c = 3$. At $x = 1$: "
                "$2 + b + 3 = 8$ gives $b = 3$. So $y = 2x^2 + 3x + 3$; "
                "check at $x = 4$: $32 + 12 + 3 = 47$. The whole table "
                "accounted for.",
                [
                    "Eq(9 - 5, 4)",
                    "Eq(17 - 13, 4)",
                    "Eq(2 + 3 + 3, 8)",
                    "Eq(2*16 + 3*4 + 3, 47)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Testing ratios or differences on unequal x-steps.",
                "The signatures only speak over EQUAL intervals. A table "
                "with x = 1, 2, 5, 6 must be re-spaced (or read in equal-"
                "step pairs) before differences or ratios mean anything.",
            ),
            mistake(
                "Reading \"grows fast\" as exponential.",
                "Steep is not a family. A quadratic outruns any line and "
                "an exponential eventually outruns both — the test is "
                "never speed, it is CONSTANT ratio vs constant "
                "difference. Compute, don't eyeball.",
            ),
            mistake(
                "Calling percent growth linear.",
                "\"+4% each year\" adds a DIFFERENT amount each year (4% "
                "of an ever-changing total) — that's a constant factor of "
                "1.04, not a constant difference. Percent per unit always "
                "means exponential.",
            ),
            mistake(
                "Forgetting that second differences give 2a, not a.",
                "Second differences of 4 mean a = 2. Writing a = 4 "
                "doubles the curvature and misses every table entry from "
                "x = 2 onward — check one entry before trusting the "
                "formula.",
            ),
        ],
        try_it=[
            problem(
                "im3-u8-l1-t1",
                "For $x = 0, 1, 2, 3$ the table reads $y = 12, 9, 6, 3$. "
                "Identify the family and write the function.",
                "First differences: $-3, -3, -3$ — constant, so linear "
                "with slope $-3$ and intercept $12$: $y = -3x + 12$. "
                "Check: $-3 \\cdot 3 + 12 = 3$. Falling steadily is "
                "still linear — the difference is just negative.",
                [
                    "Eq(9 - 12, -3)",
                    "Eq(-3*3 + 12, 3)",
                ],
            ),
            problem(
                "im3-u8-l1-t2",
                "For $x = 0, 1, 2, 3$ the table reads $y = 81, 27, 9, "
                "3$. Identify the family and write the function.",
                "Ratios: $\\frac{27}{81} = \\frac{1}{3}$, $\\frac{9}{27} "
                "= \\frac{1}{3}$, $\\frac{3}{9} = \\frac{1}{3}$ — "
                "constant factor, so exponential decay: $y = 81 \\cdot "
                "\\left(\\frac{1}{3}\\right)^x$. Check: $81 \\cdot "
                "\\frac{1}{27} = 3$ at $x = 3$.",
                [
                    "Eq(Rational(27, 81), Rational(1, 3))",
                    "Eq(81*Rational(1, 3)**3, 3)",
                ],
            ),
            problem(
                "im3-u8-l1-t3",
                "Name the family for each situation, with the signature "
                "that gives it away: (a) a taxi charges a flat fee plus "
                "a fixed amount per kilometre; (b) a town of $10000$ "
                "grows $2\\%$ per year; (c) a dropped stone falls "
                "$5t^2$ metres in $t$ seconds.",
                "(a) Fixed amount per kilometre = constant difference — "
                "LINEAR. (b) Percent per year = constant factor "
                "$1.02$ — EXPONENTIAL: after one year $10000 \\cdot "
                "1.02 = 10200$. (c) $5t^2$ has constant second "
                "differences — QUADRATIC: distances $5, 20, 45$ at "
                "$t = 1, 2, 3$ step by $15, 25$ — differences that "
                "themselves step by $10$.",
                [
                    "Eq(10000*Rational(102, 100), 10200)",
                    "Eq(5*2**2, 20)",
                    "Eq((45 - 20) - (20 - 5), 10)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "The data picks first",
             "body": "Before any equation, run the tests on equal $x$-steps. Constant first differences: LINEAR (the constant is the slope). Constant ratios: EXPONENTIAL (the constant is the base). Constant second differences: QUADRATIC (the constant is $2a$). One of the three holds still — that one is the family.",
             "beats": ["Differences constant $\\to$ linear",
                       "Ratios constant $\\to$ exponential",
                       "Second differences constant $\\to$ quadratic ($= 2a$)"]},
            {"kind": "worked", "title": "Steps of three", "problemId": "im3-u8-l1-we1"},
            tap(
                "Read the signature",
                "Over equal steps a table's first differences are $4, 4, "
                "4, 4$. The family is:",
                ["linear — constant differences",
                 "exponential — it keeps growing",
                 "quadratic — four values are given",
                 "impossible to tell"],
                0,
                "A constant first difference is the linear signature, "
                "and the constant is the slope: $y$ climbs by $4$ per "
                "step, e.g. $11 - 7 = 4$.",
                ["Eq(11 - 7, 4)"],
            ),
            {"kind": "worked", "title": "Doubling on the shelf", "problemId": "im3-u8-l1-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Steep is not a family",
             "body": "\"It grows really fast\" identifies nothing — a quadratic beats every line eventually, and an exponential beats both. Only the computed signature decides: differences for linear, ratios for exponential, second differences for quadratic. Equal $x$-steps first, always."},
            tap(
                "Percent per year",
                "A quantity grows by $50\\%$ each step: $10, 15, "
                "22.5, \\ldots$ The family is:",
                ["exponential — constant factor $1.5$",
                 "linear — it adds $5$ each step",
                 "quadratic — the differences change",
                 "none — the numbers aren't whole"],
                0,
                "$\\frac{15}{10} = 1.5$ and $\\frac{22.5}{15} = 1.5$: a "
                "constant FACTOR. Percent-per-step is always "
                "exponential; the added amount changes precisely "
                "because the factor doesn't.",
                ["Eq(Rational(15, 10), Rational(3, 2))",
                 "Eq(Rational(45, 2)/15, Rational(3, 2))"],
            ),
            {"kind": "worked", "title": "The change of the change", "problemId": "im3-u8-l1-we3"},
            {"kind": "teach", "title": "Hearing the family in words",
             "body": "Situations declare themselves before tables do. \"Same amount per unit\" — linear. \"Same percent per unit\", \"doubles every...\", \"halves every...\" — exponential. \"Accelerating from rest\", \"area against side\" — quadratic. Listen for WHICH constant the situation keeps: the difference, the factor, or the change of the change.",
             "beats": ["Same amount each step $\\to$ linear",
                       "Same percent or factor each step $\\to$ exponential",
                       "Steadily changing rate $\\to$ quadratic"]},
            {"kind": "tryIt", "title": "Falling by threes", "problemId": "im3-u8-l1-t1"},
            {"kind": "tryIt", "title": "A third at a time", "problemId": "im3-u8-l1-t2"},
            {"kind": "tryIt", "title": "Three situations, three families", "problemId": "im3-u8-l1-t3"},
            tap(
                "Halves every hour",
                "A medicine's amount in the blood halves every hour "
                "from $80$ mg. The right model family is:",
                ["exponential decay — constant factor one-half",
                 "linear — it loses the same amount hourly",
                 "quadratic — it falls, then levels",
                 "no family fits decay"],
                0,
                "\"Halves every hour\" is a constant FACTOR of "
                "$\\frac{1}{2}$: $80, 40, 20, \\ldots$ — the amount "
                "lost changes every hour, the factor never does.",
                ["Eq(Rational(1, 2)*80, 40)"],
            ),
            {"kind": "recap", "title": "Choosing a family — what sticks",
             "points": [
                 "Test over equal x-steps: differences, then ratios, then second differences.",
                 "Constant differences = linear; constant ratios = exponential; constant second differences = quadratic.",
                 "Second differences equal 2a, not a.",
                 "Percent-per-unit change is always exponential — a factor in disguise.",
                 "Steepness is not evidence; a computed constant is.",
             ]},
        ],
    )


# ===========================================================================
# Lesson 2 — building models from data
# ===========================================================================

def lesson_building():
    return lesson(
        slug="building-models-from-data",
        title="Building the Model",
        concrete=(
            "Two measurements of a growing plant, two readings of a "
            "cooling engine, a peak and one other point on a thrown "
            "ball's arc — that's usually ALL you get. The remarkable "
            "fact of this lesson: for each family, a tiny amount of "
            "data pins the entire function. Two points force one line. "
            "Two points force one exponential. A vertex and one point "
            "force one parabola. The craft is knowing which pieces you "
            "hold, and turning them into the equation with no guessing."
        ),
        objective=(
            "Construct a linear function from two points, an exponential "
            "function from two points, and a quadratic function from its "
            "vertex and one point — and use each model to predict."
        ),
        concept=[
            "LINEAR from two points: the slope is the rise over the "
            "run, and one point then fixes the intercept. Through "
            "$(2, 11)$ and $(5, 26)$: $m = \\frac{26 - 11}{5 - 2} = 5$, "
            "then $11 = 5 \\cdot 2 + b$ gives $b = 1$, so $y = 5x + "
            "1$. Two points, one line, no freedom left.",

            "EXPONENTIAL from two points: ratios do the work. Write "
            "$y = a \\cdot b^x$; the $x = 0$ value hands you $a$ "
            "directly, and dividing the two data values isolates a "
            "power of $b$. Through $(0, 6)$ and $(3, 48)$: $a = 6$ and "
            "$b^3 = \\frac{48}{6} = 8$, so $b = 2$ and $y = 6 \\cdot "
            "2^x$. When neither point sits at $x = 0$, divide anyway — "
            "the $a$'s cancel and $b$ falls out first.",

            "QUADRATIC from vertex plus a point: vertex form $y = "
            "a(x - h)^2 + k$ is built for exactly this data. The "
            "vertex supplies $h$ and $k$; the extra point supplies "
            "$a$. Vertex $(3, 2)$ through $(5, 10)$: $10 = a(5-3)^2 + "
            "2$ gives $4a = 8$, $a = 2$ — the whole parabola from two "
            "pieces of information.",

            "A built model earns its keep by PREDICTING. Substitute "
            "the $x$ you care about and read the answer — then, "
            "before trusting it, glance back at the data: does the "
            "prediction sit inside the range you measured, or far "
            "outside it? (Lesson 4 makes that glance a discipline.)",
        ],
        key_idea=(
            "Each family is pinned by a minimal kit: two points for a "
            "line, two points for an exponential (ratios isolate the "
            "base), vertex plus one point for a parabola. Identify the "
            "kit you hold, and the equation assembles itself."
        ),
        facts=[
            fact("Line from two points",
                 "m = \\dfrac{y_2 - y_1}{x_2 - x_1}, \\quad b = y_1 - m x_1",
                 "Slope first, then substitute either point to get the "
                 "intercept."),
            fact("Exponential from two points",
                 "\\dfrac{y_2}{y_1} = b^{\\,x_2 - x_1}",
                 "Dividing the data values cancels a and leaves a pure "
                 "power of b."),
            fact("The x = 0 anchor", "y = a \\cdot b^0 = a",
                 "An x = 0 data point IS the coefficient a — no algebra "
                 "needed."),
            fact("Parabola from vertex + point",
                 "y = a(x - h)^2 + k",
                 "The vertex gives h and k; one more point determines "
                 "a."),
            fact("Predict, then look back",
                 "x \\ \\text{in} \\ \\to\\ y \\ \\text{out} \\ \\to\\ \\text{is } x \\text{ near the data?}",
                 "A model predicts anywhere; it deserves trust only near "
                 "where it was built."),
        ],
        worked=[
            problem(
                "im3-u8-l2-we1",
                "A ski lift ticket costs $11$ after $2$ uses of a "
                "punch-card top-up and $26$ after $5$ uses (cost in "
                "thousands). Build the linear model and predict the "
                "cost after $8$ uses.",
                "**Slope from the two points.** $m = \\frac{26 - 11}"
                "{5 - 2} = \\frac{15}{3} = 5$ per use."
                "**Intercept from either point.** $11 = 5 \\cdot 2 + b$ "
                "gives $b = 1$, so $y = 5x + 1$."
                "**Predict.** At $x = 8$: $5 \\cdot 8 + 1 = 41$. And a "
                "sanity check on the other data point: $5 \\cdot 5 + 1 "
                "= 26$ — the model reproduces what it was built from.",
                [
                    "Eq(Rational(26 - 11, 5 - 2), 5)",
                    "Eq(5*2 + 1, 11)",
                    "Eq(5*8 + 1, 41)",
                    "Eq(5*5 + 1, 26)",
                ],
            ),
            problem(
                "im3-u8-l2-we2",
                "A bacteria culture measures $6$ (thousand) at time "
                "$0$ hours and $48$ at $3$ hours. Build the "
                "exponential model and predict the count at $2$ "
                "hours.",
                "**Anchor.** The $t = 0$ reading is the coefficient: "
                "$a = 6$."
                "**Isolate the base.** $\\frac{48}{6} = 8 = b^3$, so "
                "$b = \\sqrt[3]{8} = 2$: the culture doubles each "
                "hour, $y = 6 \\cdot 2^t$."
                "**Predict.** At $t = 2$: $6 \\cdot 4 = 24$ thousand. "
                "Note the ratio did all the work — dividing the data "
                "cancelled $a$ and left a pure power of $b$.",
                [
                    "Eq(Rational(48, 6), 8)",
                    "Eq(8**Rational(1, 3), 2)",
                    "Eq(6*2**2, 24)",
                ],
            ),
            problem(
                "im3-u8-l2-we3",
                "A drone's altitude follows a parabola whose lowest "
                "point — the vertex — is $(3, 2)$: two metres up, "
                "three seconds in. It also passes through $(5, 10)$. "
                "Build the quadratic model and find the altitude at "
                "$x = 0$.",
                "**Vertex form immediately.** $y = a(x - 3)^2 + 2$ — "
                "the vertex supplies both $h = 3$ and $k = 2$."
                "**The extra point fixes a.** $10 = a(5 - 3)^2 + 2$ "
                "gives $4a = 8$, so $a = 2$ and $y = 2(x - 3)^2 + 2$."
                "**Evaluate.** At $x = 0$: $2 \\cdot 9 + 2 = 20$. Two "
                "pieces of data — a vertex and one point — pinned "
                "every value the function will ever take.",
                [
                    "Eq(2*(5 - 3)**2 + 2, 10)",
                    "Eq(Rational(10 - 2, 4), 2)",
                    "Eq(2*(0 - 3)**2 + 2, 20)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Averaging the two y-values to find a line.",
                "A line is slope-then-intercept, not averages. Compute "
                "m = rise/run first; averaging the data points produces "
                "a number that belongs to no line through them.",
            ),
            mistake(
                "Subtracting instead of dividing for an exponential.",
                "Exponentials are multiplicative: y2/y1 = b^(x2-x1). "
                "Subtracting the y-values feeds the linear machinery to "
                "an exponential situation and the model misses every "
                "other point.",
            ),
            mistake(
                "Using vertex form with the vertex sign flipped.",
                "y = a(x - h)^2 + k has a MINUS: vertex (3, 2) means "
                "(x - 3), not (x + 3). Substitute the vertex back — the "
                "squared term must vanish there. If it doesn't, the "
                "sign flipped.",
            ),
            mistake(
                "Solving for the base but forgetting the root.",
                "b^3 = 8 gives b = 2, not b = 8. The exponent counts "
                "the steps BETWEEN the data points — divide the y's, "
                "then take the (x2 - x1)-th root.",
            ),
        ],
        try_it=[
            problem(
                "im3-u8-l2-t1",
                "Build the linear function through $(1, 9)$ and "
                "$(4, 3)$, and find its $x$-intercept.",
                "$m = \\frac{3 - 9}{4 - 1} = -2$; then $9 = -2 \\cdot 1 "
                "+ b$ gives $b = 11$, so $y = -2x + 11$. The "
                "$x$-intercept solves $-2x + 11 = 0$: $x = \\frac{11}"
                "{2}$.",
                [
                    "Eq(Rational(3 - 9, 4 - 1), -2)",
                    "Eq(-2*1 + 11, 9)",
                    "Eq(-2*Rational(11, 2) + 11, 0)",
                ],
            ),
            problem(
                "im3-u8-l2-t2",
                "Build the exponential function through $(0, 5)$ and "
                "$(2, 45)$, and evaluate it at $x = 3$.",
                "$a = 5$ from the $x = 0$ point; $\\frac{45}{5} = 9 = "
                "b^2$, so $b = 3$ and $y = 5 \\cdot 3^x$. At $x = 3$: "
                "$5 \\cdot 27 = 135$.",
                [
                    "Eq(Rational(45, 5), 9)",
                    "Eq(sqrt(9), 3)",
                    "Eq(5*3**3, 135)",
                ],
            ),
            problem(
                "im3-u8-l2-t3",
                "A parabola has vertex $(2, -3)$ and passes through "
                "$(4, 5)$. Build it and find its $y$-intercept.",
                "$y = a(x - 2)^2 - 3$; the point gives $5 = 4a - 3$, "
                "so $a = 2$ and $y = 2(x - 2)^2 - 3$. At $x = 0$: "
                "$2 \\cdot 4 - 3 = 5$ — the $y$-intercept is $5$, "
                "matching the given point's height by the symmetry of "
                "the parabola about $x = 2$.",
                [
                    "Eq(2*(4 - 2)**2 - 3, 5)",
                    "Eq(Rational(5 + 3, 4), 2)",
                    "Eq(2*(0 - 2)**2 - 3, 5)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "Minimal kits",
             "body": "Each family is pinned by a tiny kit of data. Two points force one LINE: slope $m = \\frac{y_2 - y_1}{x_2 - x_1}$, then one point fixes $b$. Two points force one EXPONENTIAL: dividing the values cancels $a$ and leaves a power of $b$. A vertex and one point force one PARABOLA: $y = a(x-h)^2 + k$ with only $a$ to find.",
             "beats": ["Line: slope, then intercept",
                       "Exponential: divide the data — $\\frac{y_2}{y_1} = b^{\\,x_2 - x_1}$",
                       "Parabola: vertex form, one point fixes $a$"]},
            {"kind": "worked", "title": "Two points, one line", "problemId": "im3-u8-l2-we1"},
            tap(
                "Slope from a table",
                "A linear model passes through $(0, 14)$ and $(6, 2)$. "
                "Its slope is:",
                ["$-2$", "$2$", "$-12$", "$\\dfrac{1}{2}$"],
                0,
                "$m = \\frac{2 - 14}{6 - 0} = \\frac{-12}{6} = -2$ — "
                "falling $12$ over a run of $6$. The intercept is "
                "already given: the $x = 0$ point.",
                ["Eq(Rational(2 - 14, 6), -2)"],
            ),
            {"kind": "worked", "title": "Ratios isolate the base", "problemId": "im3-u8-l2-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Divide for exponentials, always",
             "body": "The linear reflex — subtract the $y$'s — is exactly wrong for an exponential. Divide them: $\\frac{y_2}{y_1} = b^{\\,x_2 - x_1}$, then take the root the step-count demands. $b^3 = 8$ means $b = 2$: three steps of doubling, not one step of eight."},
            tap(
                "Find the base",
                "An exponential passes through $(0, 5)$ and $(2, 45)$. "
                "Its base $b$ is:",
                ["$3$", "$9$", "$40$", "$45$"],
                0,
                "$\\frac{45}{5} = 9$ covers TWO steps, so $b^2 = 9$ "
                "and $b = 3$. Forgetting the square root is the "
                "classic slip — the ratio spans $x_2 - x_1$ steps.",
                ["Eq(Rational(45, 5), 9)", "Eq(sqrt(9), 3)"],
            ),
            {"kind": "worked", "title": "Vertex plus one point", "problemId": "im3-u8-l2-we3"},
            {"kind": "teach", "title": "Predict — then look back at the data",
             "body": "A built model will happily predict anywhere. Substitute the $x$ you care about, read off $y$ — then check whether that $x$ sits NEAR the data that built the model. Inside the measured range, predictions inherit the data's credibility; far outside it they are guesses wearing an equation. Lesson 4 turns this glance into a rule.",
             "beats": ["Substitute, evaluate, predict",
                       "Near the data: credible",
                       "Far from the data: a guess in a suit"]},
            {"kind": "tryIt", "title": "Down to the intercept", "problemId": "im3-u8-l2-t1"},
            {"kind": "tryIt", "title": "Base three", "problemId": "im3-u8-l2-t2"},
            {"kind": "tryIt", "title": "A symmetric check", "problemId": "im3-u8-l2-t3"},
            tap(
                "Percent to factor",
                "A car's value drops $4\\%$ per year. The base of the "
                "exponential model is:",
                ["$0.96$", "$1.04$", "$0.04$", "$-0.04$"],
                0,
                "Losing $4\\%$ keeps $96\\%$: the factor is $1 - 0.04 "
                "= 0.96$. A base must be what REMAINS per step — "
                "$0.04$ would erase $96\\%$ of the car every year.",
                ["Eq(1 - Rational(4, 100), Rational(24, 25))",
                 "Eq(Rational(96, 100), Rational(24, 25))"],
            ),
            {"kind": "recap", "title": "Building the model — what sticks",
             "points": [
                 "Two points pin a line: slope from the quotient of differences, then the intercept.",
                 "Two points pin an exponential: divide the y-values, take the step-count root.",
                 "An x = 0 data point IS the exponential's coefficient a.",
                 "Vertex + one point pin a parabola via vertex form.",
                 "Predictions are credible near the data that built the model.",
             ]},
        ],
    )


# ===========================================================================
# Lesson 3 — residuals and goodness of fit
# ===========================================================================

def lesson_residuals():
    return lesson(
        slug="residuals-and-goodness-of-fit",
        title="Residuals",
        concrete=(
            "Two friends both claim their model predicts your test "
            "scores from hours studied. How do you judge them? Not by "
            "confidence — by LEFTOVERS. Subtract each model's "
            "prediction from what actually happened; the differences "
            "are the residuals, the part of reality the model failed "
            "to explain. Small, patternless leftovers: good model. "
            "Small leftovers marching in a curve: wrong FAMILY — the "
            "model is quietly bending away from the data and the "
            "residuals are where the bend shows up first."
        ),
        objective=(
            "Compute residuals, use their sizes to compare competing "
            "models, and read their pattern to detect a wrong function "
            "family — including why a residual sum of zero proves "
            "nothing."
        ),
        concept=[
            "A RESIDUAL is actual minus predicted: $r = y - \\hat{y}$. "
            "Positive means the data point sits ABOVE the model "
            "(the model under-predicted); negative, below. If the "
            "model $\\hat{y} = 3x + 2$ predicts $14$ at $x = 4$ and "
            "the measurement was $16$, the residual is $+2$: two "
            "units of reality the model didn't capture.",

            "Residual SIZES compare models. For each candidate, "
            "compute every residual and total the absolute values "
            "(squaring them is the standard variant — it punishes big "
            "misses harder). The model leaving smaller leftovers "
            "explains more of the data. A model that is excellent on "
            "four points and terrible on one may still lose to a "
            "model that is merely good everywhere — one huge miss "
            "outweighs several small ones.",

            "Residual PATTERNS diagnose the family. A well-chosen "
            "family leaves residuals that look like noise — small, "
            "both signs, no trend. A LINE fitted to curved data "
            "leaves a signature arc: positive at the ends, negative "
            "in the middle (or the reverse) — the line cuts through "
            "the curve. A steady march from negative to positive "
            "means the model grows too slowly. Pattern = wrong "
            "family, no matter how small the residuals are.",

            "One trap deserves its own paragraph: residuals that sum "
            "to ZERO. The leftovers $-5, +5$ cancel perfectly and "
            "the fit is still terrible. Cancellation is why sizes "
            "are totalled as absolute values (or squares) — a zero "
            "SUM proves balance, not accuracy.",
        ],
        key_idea=(
            "A residual is actual minus predicted — the leftover the "
            "model couldn't explain. Judge models by the SIZE of their "
            "leftovers and the PATTERN: small and patternless wins; "
            "any systematic curve or trend means the wrong family was "
            "chosen."
        ),
        facts=[
            fact("The residual", "r = y_{\\text{actual}} - \\hat{y}",
                 "Actual minus predicted: positive above the model, "
                 "negative below."),
            fact("Comparing fits",
                 "\\text{total of } |r| \\ (\\text{or } r^2) \\ \\text{smaller} \\Rightarrow \\text{better fit}",
                 "Absolute values (or squares) stop opposite-sign "
                 "misses from cancelling."),
            fact("The noise ideal",
                 "\\text{good fit: residuals small, both signs, no pattern}",
                 "What the model failed to explain should look like "
                 "chance, not structure."),
            fact("The curvature signature",
                 "+, -, -, + \\ \\text{(or reverse)} \\Rightarrow \\text{wrong family}",
                 "A line through curved data cuts the curve — ends one "
                 "side, middle the other."),
            fact("The zero-sum trap", "\\sum r = 0 \\ \\not\\Rightarrow\\ \\text{good fit}",
                 "Leftovers of -5 and +5 cancel; balance is not "
                 "accuracy."),
        ],
        worked=[
            problem(
                "im3-u8-l3-we1",
                "The model $\\hat{y} = 3x + 2$ predicts a plant's "
                "height. Measurements: $16$ cm at $x = 4$ weeks and "
                "$18$ cm at $x = 6$. Compute both residuals and say "
                "what each means.",
                "**Predict, then subtract.** At $x = 4$: $\\hat{y} = "
                "14$, so $r = 16 - 14 = +2$ — the plant sits $2$ cm "
                "ABOVE the model's story."
                "**Second point.** At $x = 6$: $\\hat{y} = 20$, so "
                "$r = 18 - 20 = -2$ — now $2$ cm below."
                "**Read them together.** One above, one below, same "
                "size: no trend visible from two points, and small "
                "leftovers — so far the model is holding.",
                [
                    "Eq(3*4 + 2, 14)",
                    "Eq(16 - 14, 2)",
                    "Eq(3*6 + 2, 20)",
                    "Eq(18 - 20, -2)",
                ],
            ),
            problem(
                "im3-u8-l3-we2",
                "Two models predict the same four measurements. "
                "Model A leaves residuals $1, -1, 2, -2$; model B "
                "leaves $4, -3, 5, -4$. Which fits better, and by "
                "what measure?",
                "**Total the sizes.** A: $|1| + |-1| + |2| + |-2| = "
                "6$. B: $4 + 3 + 5 + 4 = 16$."
                "**Verdict.** A leaves $6$ units of unexplained "
                "reality against B's $16$ — A fits better."
                "**Why absolute values.** BOTH models' residuals sum "
                "to zero: $1 - 1 + 2 - 2 = 0$ and $4 - 3 + 5 - 4 = "
                "2$... almost — B's raw sum is $2$, A's is $0$, and "
                "neither number measures fit. Sizes, not sums.",
                [
                    "Eq(1 + 1 + 2 + 2, 6)",
                    "Eq(4 + 3 + 5 + 4, 16)",
                    "6 < 16",
                    "Eq(1 - 1 + 2 - 2, 0)",
                    "Eq(4 - 3 + 5 - 4, 2)",
                ],
            ),
            problem(
                "im3-u8-l3-we3",
                "Data: $(1, 5), (2, 8), (3, 13), (4, 20)$. The line "
                "through the endpoints, $\\hat{y} = 5x$, is proposed "
                "as a model. Compute the residuals, read their "
                "pattern, and diagnose.",
                "**Residuals.** Predictions $5, 10, 15, 20$ give "
                "leftovers $0, -2, -2, 0$."
                "**The pattern.** Zero at the ends, negative in the "
                "middle — the data sags below the line mid-range: "
                "that is CURVATURE, the signature of a wrong family."
                "**Diagnose.** Second differences of the data: "
                "$(13 - 8) - (8 - 5) = 2$ and $(20 - 13) - (13 - 8) "
                "= 2$ — constant. The family is quadratic ($y = x^2 "
                "+ 4$ fits every point exactly), and no line, "
                "however tuned, can erase that arc.",
                [
                    "Eq(Rational(20 - 5, 4 - 1), 5)",
                    "Eq(8 - 10, -2)",
                    "Eq(13 - 15, -2)",
                    "Eq((13 - 8) - (8 - 5), 2)",
                    "Eq(1**2 + 4, 5)",
                    "Eq(4**2 + 4, 20)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Computing predicted minus actual.",
                "The convention is actual - predicted, and the SIGN "
                "carries meaning: positive means the data sits above "
                "the model. Flipping the order flips every diagnosis "
                "of over- vs under-prediction.",
            ),
            mistake(
                "Judging fit by the residual SUM.",
                "Residuals of -5 and +5 sum to zero around a terrible "
                "model — cancellation is not accuracy. Total absolute "
                "values or squares; only sizes measure leftovers.",
            ),
            mistake(
                "Ignoring a pattern because residuals are small.",
                "Small-but-curved residuals mean the family is wrong "
                "and the error will EXPLODE outside the data range. "
                "Noise-like leftovers, not just small ones, are the "
                "passing grade.",
            ),
            mistake(
                "Keeping a model that nails four points and misses one "
                "badly.",
                "One residual of 7 outweighs several of 1 — especially "
                "under squaring, which the standard method uses "
                "precisely to punish the big miss. Check the worst "
                "point, not just the average.",
            ),
        ],
        try_it=[
            problem(
                "im3-u8-l3-t1",
                "For the model $\\hat{y} = 2x + 1$, compute the "
                "residuals at the measured points $(3, 9)$ and "
                "$(5, 9)$.",
                "At $x = 3$: $\\hat{y} = 7$, residual $9 - 7 = +2$ "
                "(above the model). At $x = 5$: $\\hat{y} = 11$, "
                "residual $9 - 11 = -2$ (below). Same measurement, "
                "opposite verdicts — residuals judge the point "
                "AGAINST the model, not on its own.",
                [
                    "Eq(2*3 + 1, 7)",
                    "Eq(9 - 7, 2)",
                    "Eq(9 - 11, -2)",
                ],
            ),
            problem(
                "im3-u8-l3-t2",
                "Model A leaves residuals $2, 2, 1$; model B leaves "
                "$0, 1, 7$. Which fits better? Answer with totals, "
                "then with one sentence about B's shape.",
                "Totals: A gives $2 + 2 + 1 = 5$; B gives $0 + 1 + 7 "
                "= 8$. A fits better — and B's story is worse than "
                "its total: two near-perfect points and one disaster "
                "of $7$, the profile of a model that got lucky twice "
                "rather than one that understands the data.",
                [
                    "Eq(2 + 2 + 1, 5)",
                    "Eq(0 + 1 + 7, 8)",
                    "5 < 8",
                ],
            ),
            problem(
                "im3-u8-l3-t3",
                "A linear model's residuals, in $x$-order, are $-3, "
                "-1, 1, 3$. Their sum is zero. Is the fit good?",
                "No. The sum $-3 - 1 + 1 + 3 = 0$ only says the "
                "misses balance. The PATTERN — a steady march from "
                "$-3$ up to $+3$ — says the data rises faster than "
                "the model: the slope is too small (or the family "
                "curves upward). A good fit's residuals hop between "
                "signs without a trend; these climb like a staircase.",
                [
                    "Eq(-3 - 1 + 1 + 3, 0)",
                    "Eq(-1 - (-3), 2)",
                    "Eq(3 - 1, 2)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "The leftovers",
             "body": "A residual is what the model failed to explain: $r = y_{\\text{actual}} - \\hat{y}$. Positive: the data sits above the model. Negative: below. Every fitted model leaves residuals; the whole craft of judging fit is reading their SIZES and their PATTERN.",
             "beats": ["$r = \\text{actual} - \\text{predicted}$",
                       "Positive $=$ above the model, negative $=$ below",
                       "Sizes and pattern — the two dials of fit"]},
            {"kind": "worked", "title": "Two leftovers", "problemId": "im3-u8-l3-we1"},
            tap(
                "Sign and size",
                "A model predicts $25$; the measurement is $22$. The "
                "residual is:",
                ["$-3$ — the data sits below the model",
                 "$+3$ — the data sits above the model",
                 "$3$ — residuals have no sign",
                 "$47$ — add them"],
                0,
                "Actual minus predicted: $22 - 25 = -3$. The sign is "
                "information — this model OVER-predicted by three.",
                ["Eq(22 - 25, -3)"],
            ),
            {"kind": "worked", "title": "Six against sixteen", "problemId": "im3-u8-l3-we2"},
            {"kind": "tip", "eyebrow": "The trap", "title": "A zero sum proves nothing",
             "body": "Residuals of $-5$ and $+5$ sum to zero around a model that misses everything by five. Cancellation is balance, not accuracy — which is exactly why fits are totalled with absolute values or squares. Never report $\\sum r$ as evidence of quality."},
            tap(
                "Which model wins?",
                "Model A leaves residuals $1, -2, 1$; model B leaves "
                "$3, -4, 3$. The better fit is:",
                ["A — total size $4$ against B's $10$",
                 "B — its residuals are more symmetric",
                 "they tie — both sums are near zero",
                 "neither can be compared without a graph"],
                0,
                "Total the sizes: A gives $1 + 2 + 1 = 4$, B gives "
                "$3 + 4 + 3 = 10$. Sums near zero say nothing — "
                "sizes are the measure.",
                ["Eq(1 + 2 + 1, 4)", "Eq(3 + 4 + 3, 10)", "4 < 10"],
            ),
            {"kind": "worked", "title": "The sagging middle", "problemId": "im3-u8-l3-we3"},
            {"kind": "teach", "title": "Reading the pattern",
             "body": "A right-family model leaves residuals that look like noise: small, both signs, no order. Structure is a diagnosis. Ends positive / middle negative (or the reverse): curvature — wrong family, try quadratic or exponential. A steady climb from negative to positive: the model grows too slowly. Pattern trumps size: small-but-curved residuals still mean the family is wrong.",
             "beats": ["Noise $=$ healthy; structure $=$ diagnosis",
                       "$+, -, -, +$ arc $\\to$ curvature, wrong family",
                       "Steady climb $\\to$ model grows too slowly"]},
            {"kind": "tryIt", "title": "One point above, one below", "problemId": "im3-u8-l3-t1"},
            {"kind": "tryIt", "title": "Lucky twice", "problemId": "im3-u8-l3-t2"},
            {"kind": "tryIt", "title": "The staircase", "problemId": "im3-u8-l3-t3"},
            tap(
                "Diagnose the arc",
                "A line fitted to data leaves residuals $+2, -1, -2, "
                "-1, +2$ in $x$-order. The diagnosis is:",
                ["curvature — the data bends; try another family",
                 "excellent fit — the residuals sum to zero",
                 "the slope is slightly too small",
                 "two outliers at the ends"],
                0,
                "Positive at both ends, negative through the middle: "
                "the line cuts through a curve. The zero sum ($2 - 1 "
                "- 2 - 1 + 2 = 0$) is exactly the trap — pattern, "
                "not sum, tells the truth.",
                ["Eq(2 - 1 - 2 - 1 + 2, 0)"],
            ),
            {"kind": "recap", "title": "Residuals — what sticks",
             "points": [
                 "Residual = actual − predicted; the sign says above or below the model.",
                 "Compare models by totalled absolute (or squared) residuals — smaller wins.",
                 "A zero residual sum proves balance, never accuracy.",
                 "Noise-like residuals = good family; arcs and staircases = wrong family.",
                 "One huge miss can outweigh several tiny ones — check the worst point.",
             ]},
        ],
    )


# ===========================================================================
# Lesson 4 — domains, limits and model breakdown
# ===========================================================================

def lesson_breakdown():
    return lesson(
        slug="domains-and-model-breakdown",
        title="Where Models Break",
        concrete=(
            "A model of a thrown ball says its height at $t = 5$ "
            "seconds is $-25$ metres. The algebra is flawless; the "
            "ball is not twenty-five metres underground — it landed a "
            "second earlier and the MODEL'S JURISDICTION ended with "
            "it. Every model is a local law: true over the domain "
            "that built it, fiction beyond. The last modelling skill "
            "is drawing that border — and it is the difference "
            "between using mathematics and being used by it."
        ),
        objective=(
            "Restrict a model to the domain where it means something, "
            "distinguish interpolation from extrapolation, and "
            "recognise when a model's predictions stop describing "
            "reality — however correct the algebra."
        ),
        concept=[
            "The APPROPRIATE DOMAIN is dictated by the situation, not "
            "the formula. $h = 20t - 5t^2$ is defined for every real "
            "$t$, but the ball it models exists from launch to "
            "landing: $h = 0$ at $t = 0$ and $t = 4$, so the model's "
            "jurisdiction is $0 \\le t \\le 4$. Outside it the "
            "formula still computes — it just stops describing "
            "anything.",

            "Counting situations restrict domains differently: a "
            "cost-per-notebook model $C = 2500n$ accepts only whole "
            "$n \\ge 0$ — the graph is dots, not a line, and "
            "\"$2.7$ notebooks\" is not a purchase. Write the domain "
            "with the model; it is part of the answer, not a "
            "footnote.",

            "INTERPOLATION predicts inside the measured range; "
            "EXTRAPOLATION predicts beyond it. Interpolation "
            "inherits the data's credibility — the model was tested "
            "on both sides of the question. Extrapolation is a bet "
            "that the pattern continues, and the further out, the "
            "wilder the bet: a tree growing $0.3$ m per year from "
            "$2$ m stands a plausible $5$ m after ten years — and an "
            "absurd $32$ m after a hundred. Same model, same "
            "algebra; only the jurisdiction changed.",

            "Whole FAMILIES break in characteristic ways. Linear "
            "models break because nothing physical climbs forever at "
            "a constant rate. Exponential models break faster: "
            "doubling bacteria pass every physical limit within "
            "days — real growth bends into an S-curve when "
            "resources bite. A good modeller states the model AND "
            "its expiry: \"exponential for the first day, logistic "
            "after\". The formula never announces its own "
            "breakdown; that judgment is yours.",
        ],
        key_idea=(
            "A model is a local law: the situation, not the formula, "
            "sets its domain. Interpolation is backed by data; "
            "extrapolation is a bet that grows wilder with distance — "
            "and every family eventually breaks, the formula never "
            "says when, and stating the border is part of the model."
        ),
        facts=[
            fact("Domain from the situation",
                 "\\text{formula domain} \\ne \\text{model domain}",
                 "The algebra computes everywhere; the model only "
                 "means something where the situation exists."),
            fact("Interpolation vs extrapolation",
                 "\\text{inside the data: tested} \\quad \\text{beyond it: a bet}",
                 "Predictions between measurements inherit their "
                 "credibility; predictions beyond them do not."),
            fact("Counting domains",
                 "n \\in \\{0, 1, 2, \\ldots\\}",
                 "Items, tickets and people make dot-graphs — whole "
                 "numbers only."),
            fact("How lines break",
                 "\\text{constant rate forever} \\to \\text{absurdity}",
                 "Nothing physical climbs at a fixed rate "
                 "indefinitely; linear models expire quietly."),
            fact("How exponentials break",
                 "\\text{doubling} \\to \\text{resource limits} \\to \\text{S-curve}",
                 "Unchecked doubling passes every physical bound "
                 "within days; real growth bends."),
        ],
        worked=[
            problem(
                "im3-u8-l4-we1",
                "A ball thrown upward has height $h = 20t - 5t^2$ "
                "metres after $t$ seconds. State the model's "
                "appropriate domain, and explain what $h(5) = -25$ "
                "does and does not mean.",
                "**Find the jurisdiction.** $h = 0$ when $5t(4 - t) "
                "= 0$: at $t = 0$ (launch) and $t = 4$ (landing). "
                "The model describes a ball for $0 \\le t \\le 4$ "
                "only."
                "**Inside, it works.** At $t = 2$: $h = 40 - 20 = "
                "20$ m — the peak, believable."
                "**Outside, it computes fiction.** $h(5) = 100 - 125 "
                "= -25$ is correct algebra about no ball at all: the "
                "flight ended at $t = 4$, and the formula doesn't "
                "know. The domain is part of the model.",
                [
                    "Eq(20*4 - 5*16, 0)",
                    "Eq(20*2 - 5*4, 20)",
                    "Eq(20*5 - 5*25, -25)",
                ],
            ),
            problem(
                "im3-u8-l4-we2",
                "A pine grows $0.3$ m per year and stands $2$ m "
                "today: $h = 0.3t + 2$. Evaluate the model at $t = "
                "10$ and $t = 100$, and judge each prediction.",
                "**Ten years.** $h = 0.3 \\cdot 10 + 2 = 5$ m — a "
                "plausible pine, and $t = 10$ sits near the growth "
                "data that built the rate."
                "**A hundred years.** $h = 0.3 \\cdot 100 + 2 = 32$ "
                "m — taller than almost any pine on Earth. The "
                "algebra is identical; the EXTRAPOLATION is a "
                "hundred-year bet that a sapling's growth rate never "
                "slows, and biology declines the bet."
                "**The lesson.** The model didn't get worse at "
                "$t = 100$; it left its jurisdiction. Growth slows, "
                "the line doesn't.",
                [
                    "Eq(Rational(3, 10)*10 + 2, 5)",
                    "Eq(Rational(3, 10)*100 + 2, 32)",
                ],
            ),
            problem(
                "im3-u8-l4-we3",
                "A culture of $1000$ bacteria doubles every hour: "
                "$N = 1000 \\cdot 2^t$. Evaluate at $t = 4$ hours "
                "and comment on $t = 72$ hours (three days).",
                "**Four hours.** $N = 1000 \\cdot 2^4 = 16000$ — "
                "fine; early growth really is exponential."
                "**Three days.** $2^{72}$ is astronomically large — "
                "beyond $10^{21}$, so the model predicts more than a "
                "billion trillion bacteria from one dish: more mass "
                "than the dish, the lab, and the building. Food and "
                "space run out long before; real growth bends into "
                "an S-curve."
                "**The moral.** Exponential models carry the "
                "shortest jurisdiction of all — state the expiry "
                "with the model: \"exponential for the first day\".",
                [
                    "Eq(1000*2**4, 16000)",
                    "2**72 > 10**21",
                    "Eq(2**10, 1024)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Trusting the formula outside the situation.",
                "h(5) = -25 for a ball that landed at t = 4 is correct "
                "algebra about nothing. Find where the situation "
                "starts and ends (often the zeros) and staple that "
                "domain to the model.",
            ),
            mistake(
                "Treating interpolation and extrapolation as equals.",
                "Between the data, the model was tested; beyond it, "
                "it's a bet that the pattern continues. Report "
                "extrapolations with their distance: predicting one "
                "step past the data is caution, fifty steps is "
                "fiction.",
            ),
            mistake(
                "Graphing count data as a continuous line.",
                "2.7 tickets cannot be bought. Cost-per-item models "
                "have whole-number domains — dots, not lines — and "
                "answers must be whole numbers too.",
            ),
            mistake(
                "Expecting the model to announce its own breakdown.",
                "No formula flags its expiry — 2^t computes forever, "
                "cheerfully. The breakdown check is yours: compare "
                "predictions against physical limits (space, food, "
                "height, capacity) and cut the domain where they "
                "collide.",
            ),
        ],
        try_it=[
            problem(
                "im3-u8-l4-t1",
                "Notebooks cost $2500$ each, so a purchase costs "
                "$C = 2500n$. State the model's domain, and the cost "
                "of $4$ notebooks.",
                "$n$ counts notebooks: the domain is the whole "
                "numbers $n = 0, 1, 2, \\ldots$ — the graph is dots, "
                "and $n = 2.7$ is not a purchase. $C(4) = 2500 \\cdot "
                "4 = 10000$.",
                [
                    "Eq(2500*4, 10000)",
                ],
            ),
            problem(
                "im3-u8-l4-t2",
                "From data collected 2010–2020, a town's population "
                "is modelled by $p = 1200 + 40t$ ($t$ in years since "
                "2010). Predict the population in 2015 and in 2035, "
                "and label each prediction interpolation or "
                "extrapolation.",
                "2015 is $t = 5$: $p = 1200 + 200 = 1400$ — "
                "INTERPOLATION, inside the measured decade, backed "
                "by data on both sides. 2035 is $t = 25$: $p = 1200 "
                "+ 1000 = 2200$ — EXTRAPOLATION, fifteen years past "
                "the last measurement, a bet that a decade's trend "
                "holds for twenty-five.",
                [
                    "Eq(1200 + 40*5, 1400)",
                    "Eq(1200 + 40*25, 2200)",
                ],
            ),
            problem(
                "im3-u8-l4-t3",
                "A phone battery drains $12\\%$ of a full charge per "
                "hour of video: $B = 100 - 12t$ (percent). Find "
                "where the model must stop, and what it would claim "
                "one hour later.",
                "$B = 0$ at $t = \\frac{100}{12} = \\frac{25}{3} "
                "\\approx 8.3$ hours — the phone is dead and the "
                "model's domain is $0 \\le t \\le \\frac{25}{3}$. "
                "One hour on, the formula claims $B = 100 - 112 = "
                "-12$: negative charge, meaning nothing. Batteries "
                "stop; linear formulas don't.",
                [
                    "Eq(Rational(100, 12), Rational(25, 3))",
                    "Eq(100 - 12*Rational(25, 3), 0)",
                    "Eq(100 - 12*Rational(28, 3), -12)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "Local laws",
             "body": "Every model is a local law: the FORMULA computes for all $x$; the MODEL only describes reality where the situation exists. A thrown ball's $h = 20t - 5t^2$ is true from launch to landing — $0 \\le t \\le 4$ — and pure fiction after. The domain is not a footnote; it is part of the model.",
             "beats": ["Formula domain $\\ne$ model domain",
                       "The situation (often its zeros) draws the border",
                       "State the domain WITH the model"]},
            {"kind": "worked", "title": "The underground ball", "problemId": "im3-u8-l4-we1"},
            tap(
                "Minus twenty-five metres",
                "The ball model $h = 20t - 5t^2$ gives $h(5) = -25$. "
                "This means:",
                ["nothing — the flight ended at $t = 4$, outside the model's domain",
                 "the ball is $25$ m underground",
                 "the model was wrong all along",
                 "the ball was thrown downward"],
                0,
                "$20 \\cdot 5 - 5 \\cdot 25 = -25$ is flawless "
                "arithmetic about no ball at all — the model's "
                "jurisdiction ended at landing, $t = 4$.",
                ["Eq(20*5 - 5*25, -25)", "Eq(20*4 - 5*16, 0)"],
            ),
            {"kind": "worked", "title": "The hundred-year pine", "problemId": "im3-u8-l4-we2"},
            {"kind": "tip", "eyebrow": "The rule of thumb", "title": "Distance measures the bet",
             "body": "Interpolation — predicting INSIDE the measured range — inherits the data's credibility. Extrapolation is a bet that the pattern continues, and the odds worsen with distance: one step past the data is caution, fifty steps is fiction. Always report how far outside the data a prediction reaches."},
            tap(
                "Which prediction to trust",
                "A model was built from data for $x$ between $0$ and "
                "$10$. Which prediction deserves the most trust?",
                ["$x = 7$ — inside the measured range",
                 "$x = 30$ — the model is the same everywhere",
                 "$x = 100$ — big $x$ averages out errors",
                 "$x = -20$ — negative values are safer"],
                0,
                "$x = 7$ is interpolation: the model was tested on "
                "both sides of the question ($0 \\le 7 \\le 10$). "
                "The others bet the pattern survives far beyond "
                "anything measured.",
                ["Rational(7, 1) < 10", "0 < 7"],
            ),
            {"kind": "worked", "title": "Three days of doubling", "problemId": "im3-u8-l4-we3"},
            {"kind": "teach", "title": "How families die",
             "body": "Lines break because nothing climbs at a constant rate forever — the hundred-year pine. Exponentials break faster: $2^{t}$ passes every physical limit within days, and real growth bends into an S-curve when food or space bite. The formula NEVER announces its expiry: $2^t$ computes cheerfully forever. Stating the border — \"exponential for the first day\" — is the modeller's job, and the mark of one.",
             "beats": ["Lines expire quietly; exponentials expire fast",
                       "Physical limits, not algebra, end a model",
                       "State the expiry with the model"]},
            {"kind": "tryIt", "title": "Dots, not lines", "problemId": "im3-u8-l4-t1"},
            {"kind": "tryIt", "title": "2015 and 2035", "problemId": "im3-u8-l4-t2"},
            {"kind": "tryIt", "title": "The dead battery", "problemId": "im3-u8-l4-t3"},
            tap(
                "Doubling forever?",
                "A video's shares double daily: $3, 6, 12, \\ldots$ "
                "The model $3 \\cdot 2^d$ must eventually fail "
                "because:",
                ["the audience is finite — doublings outrun any population",
                 "exponents cannot exceed $30$",
                 "the algebra breaks down for large $d$",
                 "it won't — exponential models hold forever"],
                0,
                "Twenty days in, $3 \\cdot 2^{20}$ exceeds three "
                "million shares — past most audiences already, since "
                "$2^{20} > 10^6$. The algebra is fine; the AUDIENCE "
                "runs out, and growth bends into an S-curve.",
                ["Eq(2**20, 1048576)", "2**20 > 10**6"],
            ),
            {"kind": "recap", "title": "Where models break — what sticks",
             "points": [
                 "The situation, not the formula, sets the domain — often between the zeros.",
                 "Counting models take whole numbers: dot graphs, whole-number answers.",
                 "Interpolation is tested; extrapolation is a bet that worsens with distance.",
                 "Lines break because constant rates end; exponentials break because resources do.",
                 "The formula never announces its expiry — stating the border is part of the model.",
             ]},
        ],
    )


# ===========================================================================
# Practice bank
# ===========================================================================

def practice_bank():
    return [
        problem(
            "im3-u8-p1",
            "For $x = 0, 1, 2, 3$ a table reads $y = 4, 10, 16, 22$. "
            "Identify the family and write the function.",
            "First differences $6, 6, 6$ — constant, so linear with "
            "slope $6$; the $x = 0$ entry gives the intercept $4$: "
            "$y = 6x + 4$. Check: $6 \\cdot 3 + 4 = 22$.",
            [
                "Eq(10 - 4, 6)",
                "Eq(6*3 + 4, 22)",
            ],
        ),
        problem(
            "im3-u8-p2",
            "For $x = 0, 1, 2, 3$ a table reads $y = 500, 400, 320, "
            "256$. Identify the family and write the function.",
            "Ratios: $\\frac{400}{500} = \\frac{4}{5}$, $\\frac{320}"
            "{400} = \\frac{4}{5}$, $\\frac{256}{320} = \\frac{4}{5}$ "
            "— constant factor, exponential decay: $y = 500 \\cdot "
            "\\left(\\frac{4}{5}\\right)^x$. Check: $500 \\cdot "
            "\\frac{64}{125} = 256$.",
            [
                "Eq(Rational(400, 500), Rational(4, 5))",
                "Eq(500*Rational(4, 5)**3, 256)",
            ],
        ),
        problem(
            "im3-u8-p3",
            "For $x = 0, 1, 2, 3, 4$ a table reads $y = 1, 4, 11, "
            "22, 37$. Identify the family and write the function.",
            "First differences $3, 7, 11, 15$; second differences "
            "$4, 4, 4$ — quadratic with $2a = 4$, so $a = 2$. From "
            "$x = 0$: $c = 1$; from $x = 1$: $2 + b + 1 = 4$ gives "
            "$b = 1$. So $y = 2x^2 + x + 1$; check at $x = 4$: $32 + "
            "4 + 1 = 37$.",
            [
                "Eq(7 - 3, 4)",
                "Eq(2 + 1 + 1, 4)",
                "Eq(2*16 + 4 + 1, 37)",
            ],
        ),
        problem(
            "im3-u8-p4",
            "Name the family and the reason: (a) a printer "
            "depreciates $15\\%$ per year; (b) a pool fills at $40$ "
            "litres per minute; (c) the area of a square against its "
            "side length.",
            "(a) Percent per year is a constant factor $0.85$ — "
            "EXPONENTIAL decay. (b) Constant amount per minute — "
            "LINEAR, slope $40$. (c) $A = s^2$ — QUADRATIC: second "
            "differences of $1, 4, 9, 16$ are constant at $2$.",
            [
                "Eq(1 - Rational(15, 100), Rational(17, 20))",
                "Eq((9 - 4) - (4 - 1), 2)",
                "Eq(40*3, 120)",
            ],
        ),
        problem(
            "im3-u8-p5",
            "Build the linear function through $(3, 4)$ and $(7, "
            "16)$, and predict $y$ at $x = 10$.",
            "$m = \\frac{16 - 4}{7 - 3} = 3$; then $4 = 3 \\cdot 3 + "
            "b$ gives $b = -5$: $y = 3x - 5$. At $x = 10$: $y = "
            "25$.",
            [
                "Eq(Rational(16 - 4, 7 - 3), 3)",
                "Eq(3*3 - 5, 4)",
                "Eq(3*10 - 5, 25)",
            ],
        ),
        problem(
            "im3-u8-p6",
            "Build the exponential function through $(0, 8)$ and "
            "$(2, 50)$, and evaluate it at $x = 1$.",
            "$a = 8$; $\\frac{50}{8} = \\frac{25}{4} = b^2$, so $b = "
            "\\frac{5}{2}$: $y = 8 \\cdot \\left(\\frac{5}{2}\\right)"
            "^x$. At $x = 1$: $8 \\cdot \\frac{5}{2} = 20$ — the "
            "geometric mean of the two data values, as it must be.",
            [
                "Eq(Rational(50, 8), Rational(25, 4))",
                "Eq(sqrt(Rational(25, 4)), Rational(5, 2))",
                "Eq(8*Rational(5, 2), 20)",
                "Eq(20**2, 8*50)",
            ],
        ),
        problem(
            "im3-u8-p7",
            "A parabola has vertex $(1, 6)$ and passes through "
            "$(3, -2)$. Build it and find its $x$-intercepts "
            "exactly.",
            "$y = a(x - 1)^2 + 6$; the point gives $-2 = 4a + 6$, so "
            "$a = -2$: $y = -2(x - 1)^2 + 6$. Intercepts: $(x - 1)^2 "
            "= 3$, so $x = 1 \\pm \\sqrt{3}$.",
            [
                "Eq(-2*(3 - 1)**2 + 6, -2)",
                "Eq(-2*(1 + sqrt(3) - 1)**2 + 6, 0)",
            ],
        ),
        problem(
            "im3-u8-p8",
            "A herd of $4000$ doubles every $12$ years. Build the "
            "model with $t$ in years and predict the herd after "
            "$36$ years.",
            "Doubling every $12$ years means $N = 4000 \\cdot "
            "2^{t/12}$. After $36$ years that is $4000 \\cdot 2^3 = "
            "32000$ — three doublings.",
            [
                "Eq(Rational(36, 12), 3)",
                "Eq(4000*2**3, 32000)",
            ],
        ),
        problem(
            "im3-u8-p9",
            "For the model $\\hat{y} = 4x + 3$, compute the "
            "residuals at $(2, 12)$, $(4, 17)$ and $(6, 30)$.",
            "Predictions: $11, 19, 27$. Residuals: $12 - 11 = +1$, "
            "$17 - 19 = -2$, $30 - 27 = +3$. Two points above the "
            "model, one below; the biggest miss is the last point.",
            [
                "Eq(4*2 + 3, 11)",
                "Eq(12 - 11, 1)",
                "Eq(17 - 19, -2)",
                "Eq(30 - 27, 3)",
            ],
        ),
        problem(
            "im3-u8-p10",
            "Model A leaves residuals $2, -1, 3, -1$; model B "
            "leaves $-4, 3, -3, 2$. Which fits the data better?",
            "Total sizes: A gives $2 + 1 + 3 + 1 = 7$; B gives $4 + "
            "3 + 3 + 2 = 12$. A leaves less unexplained — A fits "
            "better. (Neither raw sum — $3$ and $-2$ — measures "
            "anything.)",
            [
                "Eq(2 + 1 + 3 + 1, 7)",
                "Eq(4 + 3 + 3 + 2, 12)",
                "7 < 12",
                "Eq(2 - 1 + 3 - 1, 3)",
            ],
        ),
        problem(
            "im3-u8-p11",
            "A linear fit leaves residuals $0, -2, -2, 0$ in "
            "$x$-order. What do the sizes say, and what does the "
            "pattern say?",
            "The sizes are small — at most $2$. But the pattern is "
            "an arc: zero at the ends, negative through the middle — "
            "the data sags below the line, which is CURVATURE. "
            "Diagnosis: wrong family (try quadratic); small "
            "residuals cannot excuse a systematic shape, because the "
            "error will grow outside the data range.",
            [
                "Eq(0 + (-2) + (-2) + 0, -4)",
                "Eq(Abs(-2), 2)",
            ],
        ),
        problem(
            "im3-u8-p12",
            "A fitted line for exam score against study hours is "
            "$\\hat{y} = 2.5x + 40$. Interpret the slope and "
            "intercept, predict the score after $8$ hours, and "
            "compute the residual if the actual score was $65$.",
            "Slope: $2.5$ points per study hour. Intercept: $40$, "
            "the predicted score with no studying. At $x = 8$: "
            "$\\hat{y} = 20 + 40 = 60$. Residual: $65 - 60 = +5$ — "
            "this student beat the model by five points.",
            [
                "Eq(Rational(5, 2)*8 + 40, 60)",
                "Eq(65 - 60, 5)",
            ],
        ),
        problem(
            "im3-u8-p13",
            "A rectangular garden has width $w$ and length $30 - w$ "
            "metres (its half-perimeter is $30$). The area model is "
            "$A = w(30 - w)$. State the appropriate domain and the "
            "maximum area.",
            "A width must be positive and leave positive length: "
            "$0 < w < 30$. The parabola peaks halfway between the "
            "zeros, at $w = 15$: $A = 15 \\cdot 15 = 225$ square "
            "metres. Outside the domain the formula computes "
            "negative \"areas\" — fiction, as usual, beyond the "
            "border.",
            [
                "Eq(Rational(0 + 30, 2), 15)",
                "Eq(15*(30 - 15), 225)",
            ],
        ),
        problem(
            "im3-u8-p14",
            "A sunflower measured over its first week grows $8$ cm "
            "per day from $20$ cm: $h = 8d + 20$. Predict its height "
            "at day $10$ and day $100$, and judge the two "
            "predictions.",
            "Day $10$: $h = 100$ cm — one metre, plausible, a short "
            "extrapolation from a week of data. Day $100$: $h = 820$ "
            "cm — an eight-metre sunflower; the linear model has "
            "left its jurisdiction, because growth slows and stops. "
            "Same formula, different verdicts: distance from the "
            "data is what changed.",
            [
                "Eq(8*10 + 20, 100)",
                "Eq(8*100 + 20, 820)",
            ],
        ),
        problem(
            "im3-u8-p15",
            "A laptop bought for $9000$ (thousand) loses $750$ "
            "(thousand) per month of value: $V = 9000 - 750m$. Find "
            "where the model must stop and state its domain.",
            "$V = 0$ at $m = \\frac{9000}{750} = 12$ months. Value "
            "cannot go negative, so the domain is $0 \\le m \\le "
            "12$ — after a year the model (and the resale value) is "
            "done.",
            [
                "Eq(Rational(9000, 750), 12)",
                "Eq(9000 - 750*12, 0)",
            ],
        ),
        problem(
            "im3-u8-p16",
            "A rumour reaches $3$ people on day $0$ and doubles "
            "daily: $N = 3 \\cdot 2^d$. Predict day $5$, then "
            "explain why the model must fail well before day $20$ "
            "in a school of $800$.",
            "Day $5$: $3 \\cdot 32 = 96$ people — plausible. But "
            "day $20$ would demand $3 \\cdot 2^{20} > 3000000$ "
            "hearers — nearly four thousand schools' worth. The "
            "rumour saturates its $800$-person audience within "
            "about $8$ days ($3 \\cdot 2^8 = 768$), and growth "
            "bends into an S-curve as the un-told run out.",
            [
                "Eq(3*2**5, 96)",
                "3*2**20 > 800",
                "Eq(3*2**8, 768)",
            ],
        ),
    ]


# ===========================================================================
# Test bank
# ===========================================================================

def test_bank():
    return [
        problem(
            "im3-u8-x1",
            "For $x = 0, 1, 2, 3$ a table reads $y = 2, 6, 18, 54$. "
            "Identify the family, write the function, and predict "
            "$y$ at $x = 5$.",
            "Ratios $\\frac{6}{2} = \\frac{18}{6} = \\frac{54}{18} = "
            "3$ — constant factor: exponential, $y = 2 \\cdot 3^x$. "
            "At $x = 5$: $2 \\cdot 243 = 486$.",
            [
                "Eq(Rational(6, 2), 3)",
                "Eq(Rational(54, 18), 3)",
                "Eq(2*3**5, 486)",
            ],
        ),
        problem(
            "im3-u8-x2",
            "A candle is $19$ cm tall $2$ hours after lighting and "
            "$7$ cm tall after $6$ hours. Build the linear model "
            "and interpret its slope and intercept.",
            "$m = \\frac{7 - 19}{6 - 2} = -3$ cm per hour — the "
            "burn rate. Intercept: $19 = -3 \\cdot 2 + b$ gives $b "
            "= 25$ — the candle's original height. Model: $h = -3t "
            "+ 25$; it must stop at $h = 0$, $t = \\frac{25}{3}$ "
            "hours.",
            [
                "Eq(Rational(7 - 19, 6 - 2), -3)",
                "Eq(-3*2 + 25, 19)",
                "Eq(-3*6 + 25, 7)",
                "Eq(-3*Rational(25, 3) + 25, 0)",
            ],
        ),
        problem(
            "im3-u8-x3",
            "Build the exponential function through $(0, 12)$ and "
            "$(4, 192)$, and evaluate it at $x = 5$.",
            "$a = 12$; $\\frac{192}{12} = 16 = b^4$, so $b = 2$: "
            "$y = 12 \\cdot 2^x$. At $x = 5$: $12 \\cdot 32 = "
            "384$.",
            [
                "Eq(Rational(192, 12), 16)",
                "Eq(16**Rational(1, 4), 2)",
                "Eq(12*2**5, 384)",
            ],
        ),
        problem(
            "im3-u8-x4",
            "A stunt rider's arc has vertex $(4, 50)$ (metres) and "
            "passes through $(0, 18)$. Build the quadratic model, "
            "find where the height is zero, and state the "
            "appropriate domain.",
            "$y = a(x - 4)^2 + 50$; the point gives $18 = 16a + "
            "50$, so $a = -2$: $y = -2(x - 4)^2 + 50$. Zeros: "
            "$(x - 4)^2 = 25$, so $x = 9$ or $x = -1$; a jump "
            "starting at $x = 0$ makes the appropriate domain $0 "
            "\\le x \\le 9$ — the landing, not $x = -1$, ends the "
            "story.",
            [
                "Eq(-2*(0 - 4)**2 + 50, 18)",
                "Eq(-2*(9 - 4)**2 + 50, 0)",
                "Eq(Rational(18 - 50, 16), -2)",
            ],
        ),
        problem(
            "im3-u8-x5",
            "For the model $\\hat{y} = 6x + 10$, compute residuals "
            "at $(1, 17)$, $(3, 26)$ and $(5, 42)$, and name the "
            "model's best and worst points.",
            "Predictions $16, 28, 40$; residuals $+1, -2, +2$. Best "
            "fit at $x = 1$ (off by one); worst are the last two "
            "(off by two each, on opposite sides). Total size $5$ — "
            "and no visible trend from three points.",
            [
                "Eq(6*1 + 10, 16)",
                "Eq(17 - 16, 1)",
                "Eq(26 - 28, -2)",
                "Eq(42 - 40, 2)",
                "Eq(1 + 2 + 2, 5)",
            ],
        ),
        problem(
            "im3-u8-x6",
            "Two models of the same data leave residuals — A: $1, "
            "-2, 1, -1$; B: $3, -3, 2, -3$. Choose the better model "
            "and justify with a computation.",
            "Total absolute residuals: A leaves $1 + 2 + 1 + 1 = "
            "5$; B leaves $3 + 3 + 2 + 3 = 11$. A explains more of "
            "the data — chosen. Note both raw sums ($-1$ and $-1$) "
            "are equal and near zero: the sum cannot separate them; "
            "sizes can.",
            [
                "Eq(1 + 2 + 1 + 1, 5)",
                "Eq(3 + 3 + 2 + 3, 11)",
                "5 < 11",
                "Eq(1 - 2 + 1 - 1, -1)",
                "Eq(3 - 3 + 2 - 3, -1)",
            ],
        ),
        problem(
            "im3-u8-x7",
            "A firework's height is $h = 45t - 5t^2$ metres. Find "
            "the appropriate domain, the peak height, and explain "
            "what the model says at $t = 10$ — and why it doesn't "
            "matter.",
            "Zeros: $5t(9 - t) = 0$ at $t = 0$ and $t = 9$ — the "
            "domain is $0 \\le t \\le 9$. The peak sits midway, $t "
            "= \\frac{9}{2}$: $h = 45 \\cdot \\frac{9}{2} - 5 \\cdot "
            "\\frac{81}{4} = \\frac{405}{4} = 101.25$ m. At $t = "
            "10$ the formula computes $450 - 500 = -50$ — fiction: "
            "the flight ended at $t = 9$, and the model's "
            "jurisdiction with it.",
            [
                "Eq(45*9 - 5*81, 0)",
                "Eq(45*Rational(9, 2) - 5*Rational(81, 4), Rational(405, 4))",
                "Eq(45*10 - 5*100, -50)",
            ],
        ),
        problem(
            "im3-u8-x8",
            "A car worth $24$ million (₮) halves in value every $3$ "
            "years. Build the model, find the value after $9$ "
            "years, and explain what goes wrong applying it at $60$ "
            "years.",
            "Halving every $3$ years: $V = 24 \\cdot \\left("
            "\\frac{1}{2}\\right)^{t/3}$ million. After $9$ years — "
            "three halvings — $V = 24 \\cdot \\frac{1}{8} = 3$ "
            "million. At $t = 60$ (twenty halvings) the model "
            "computes $24000000 \\cdot 2^{-20}$ — about $23$ "
            "tögrög, the price of nothing: long before that the car "
            "is scrap with a floor value the exponential never "
            "reaches. Decay models expire when their prediction "
            "drops below the coarseness of reality.",
            [
                "Eq(Rational(9, 3), 3)",
                "Eq(24*Rational(1, 2)**3, 3)",
                "24000000*Rational(1, 2)**20 < 30",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="modelling-with-functions",
        title="Modelling with Functions",
        unit_number=8,
        blurb=(
            "Choosing a function family from a situation, fitting it to "
            "data, judging a model against its residuals, and knowing "
            "the range over which it can be trusted."
        ),
        builds_on=(
            "Every function family in the pathway — this unit is about "
            "choosing between them."
        ),
        lessons=[
            lesson_choosing(),
            lesson_building(),
            lesson_residuals(),
            lesson_breakdown(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
