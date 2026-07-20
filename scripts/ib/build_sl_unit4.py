#!/usr/bin/env python3
"""IB Mathematics: Analysis & Approaches SL — Unit 4 (Topic 4: Statistics & Probability).

Builds data/genmath/ib-sl/statistics-and-probability.json: twelve lessons, one
per official subtopic code SL 4.1–4.12, same anatomy as Units 1–3. Banks
tagged ib-aa-sl-4.x.

Run: python3 scripts/ib/build_sl_unit4.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-sl", "statistics-and-probability.json")


# ===========================================================================
# Lesson 1 — SL 4.1: Sampling
# ===========================================================================
def lesson_sampling():
    return {
        "slug": "populations-samples-and-sampling",
        "title": "Populations, Samples & Sampling",
        "concreteComparison": (
            "Taste one spoonful of soup and judge the pot — that's sampling, and it works ONLY "
            "if you stirred first. Every statistical claim in Topic 4 stands on how the "
            "spoonful was chosen, which is why the IB starts here."
        ),
        "objective": (
            "Distinguish population from sample and discrete from continuous data; recognize "
            "the five sampling techniques and their biases; identify outliers and comment on "
            "reliability."
        ),
        "concept": [
            "**Syllabus card — SL 4.1.** Concepts of population, sample, random sample, "
            "discrete and continuous data; reliability of data sources and bias in sampling; "
            "interpretation of outliers; sampling techniques: simple random, convenience, "
            "systematic, quota and stratified. **Mostly Paper 2**, worth quick marks — the "
            "questions are vocabulary plus judgement, and 'comment' answers need a REASON.",
            "The POPULATION is everyone you want to know about; the SAMPLE is who you actually "
            "measured. Data is DISCRETE when it counts (goals, siblings) and CONTINUOUS when "
            "it measures (height, time). A RANDOM sample gives every member an equal chance — "
            "the gold standard the other methods approximate or betray.",
            "The five techniques: SIMPLE RANDOM (names from a hat — unbiased, sometimes "
            "impractical); SYSTEMATIC (every $k$th member from a random start); CONVENIENCE "
            "(whoever's nearby — fast, bias-prone); QUOTA (fill category targets, "
            "non-randomly); STRATIFIED (split the population into groups, sample each in "
            "PROPORTION — random within structure). Exam verbs: NAME the technique, then "
            "JUSTIFY or CRITIQUE it.",
            "An OUTLIER is a value far from the pack — formally flagged in SL 4.2's fence "
            "test. The SL 4.1 skill is interpretation: is it an error (remove, and say why) "
            "or a genuine extreme (keep, and note its pull on the mean)? One-sentence "
            "verdicts with reasons are what the markscheme prints."
        ],
        "keyIdea": (
            "Who you asked decides what your numbers mean. Random beats convenient; "
            "stratified mirrors the population; every 'comment' answer is claim + reason."
        ),
        "facts": [
            {
                "title": "Stratified allocation",
                "latex": "n_{\\text{group}} = \\frac{\\text{group size}}{\\text{population}} \\times n_{\\text{sample}}",
                "explanation": (
                    "NOT in the booklet — the one computation of SL 4.1: each stratum gets its "
                    "proportional share of the sample."
                ),
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-41-we1",
                "statement": (
                    "A school of $1200$ students has $400$ in Grade 10, $500$ in Grade 11 and "
                    "$300$ in Grade 12. A stratified sample of $60$ students is taken.  \n"
                    "**(a)** Find how many students should be sampled from each grade. **[3]**  \n"
                    "**(b)** State ONE advantage of stratified sampling over simple random "
                    "sampling here. **[1]**"
                ),
                "solution": (
                    "**(a)** Sampling fraction $\\frac{60}{1200} = \\frac{1}{20}$: Grade 10: "
                    "$\\frac{400}{20} = 20$; Grade 11: $\\frac{500}{20} = 25$; Grade 12: "
                    "$\\frac{300}{20} = 15$ *(M1 A1 A1)*. (Check: $20 + 25 + 15 = 60$ ✓)  \n"
                    "**(b)** It guarantees every grade is represented in proportion — a simple "
                    "random sample could by chance under-represent a grade *(R1)*.  \n"
                    "**Narrative:** one fraction, three multiplications, and a total that must "
                    "reconcile. The (b) mark needs the COMPARISON ('could under-represent'), "
                    "not just 'it's fairer'."
                ),
                "check": [
                    "Rational(60, 1200)*400 == 20",
                    "Rational(60, 1200)*500 == 25",
                    "Rational(60, 1200)*300 == 15",
                    "20 + 25 + 15 == 60",
                ],
            },
            {
                "id": "ibsl-41-we2",
                "statement": (
                    "For each scenario, **name** the sampling technique and state one weakness:  \n"
                    "**(a)** A researcher surveys shoppers at one mall entrance on a Tuesday "
                    "morning. **[2]**  \n"
                    "**(b)** From an alphabetical list of $2000$ members, every $40$th name is "
                    "chosen after a random start. **[2]**"
                ),
                "solution": (
                    "**(a)** Convenience sampling *(A1)*; weakness: Tuesday-morning mall "
                    "shoppers are unrepresentative (e.g. working people excluded) — biased "
                    "*(R1)*.  \n"
                    "**(b)** Systematic sampling *(A1)*; weakness: any hidden pattern with "
                    "period 40 in the list would bias the sample; also every member must be "
                    "listed first *(R1)*.  \n"
                    "**Narrative:** naming is one word; the mark-earning half is the SPECIFIC "
                    "weakness tied to the scenario, not a memorized generic."
                ),
                "check": ["Rational(2000, 40) == 50"],
            },
        ],
        "commonMistakes": [
            {
                "text": "Calling any 'every kth person' scheme random.",
                "correction": "That's SYSTEMATIC. It needs a random start, and a periodic list pattern can bias it.",
                "authored": True,
            },
            {
                "text": "Stratified allocations that don't total the sample size.",
                "correction": "Always reconcile: the group counts must sum to $n$. If rounding breaks it, say how you fixed it.",
                "authored": True,
            },
            {
                "text": "Deleting an outlier silently.",
                "correction": "Outliers are removed only with a stated reason (measurement error); genuine extremes stay and get discussed.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-41-t1",
                "statement": (
                    "A gym has $150$ female and $100$ male members. A stratified sample of "
                    "$40$ is taken. **Find** the number of each. **[2]**"
                ),
                "solution": (
                    "Fraction $\\frac{40}{250} = \\frac{4}{25}$: females $150 \\cdot "
                    "\\frac{4}{25} = 24$, males $16$ *(M1 A1)*. Total $40$ ✓."
                ),
                "check": ["Rational(40, 250)*150 == 24", "Rational(40, 250)*100 == 16", "24 + 16 == 40"],
            },
            {
                "id": "ibsl-41-t2",
                "statement": (
                    "Classify each as discrete or continuous: number of goals in a match; "
                    "time to run 100 m; shoe size; body temperature. **[2]**"
                ),
                "solution": (
                    "Goals: discrete. Time: continuous. Shoe size: discrete (fixed listed "
                    "values, despite halves). Temperature: continuous *(A1 A1)*."
                ),
                "check": ["1 + 1 == 2"],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.1 · mostly Paper 2",
                    "title": "The spoonful and the pot",
                    "body": (
                        "Statistics begins before any number is crunched: WHO did you "
                        "measure, and HOW were they chosen? Five techniques, their biases, "
                        "and one small computation (stratified shares) make up this code."
                    ),
                },
                {
                    "kind": "samplingWobble",
                    "eyebrow": "Why size matters",
                    "title": "Samples wobble — bigger ones wobble less",
                    "teach": (
                        "The true population value is fixed; each sample's estimate lands "
                        "near it, not on it. Draw samples at different sizes and watch the "
                        "pile tighten — reliability is bought with sample size."
                    ),
                    "config": {"p": 0.6, "pLabel": "60%", "statLabel": "sample % who say yes", "showMoe": True},
                },
                {
                    "kind": "teach",
                    "eyebrow": "The five techniques",
                    "title": "Name, then judge",
                    "beats": [
                        "Simple random (hat) · Systematic (every $k$th, random start) · Convenience (whoever's near).",
                        "Quota (fill category targets, non-random) · Stratified (proportional shares, random within groups).",
                        "Exam pattern: name it in one word, then critique it IN THIS SCENARIO.",
                    ],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Stratified shares", "problemId": "ibsl-41-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Technique ID",
                    "title": "Name it",
                    "prompt": "A pollster interviews people until reaching 50 men and 50 women, choosing whoever agrees. This is:",
                    "options": ["Quota sampling", "Stratified sampling", "Simple random sampling", "Systematic sampling"],
                    "correctIndex": 0,
                    "explanation": (
                        "Category targets filled NON-randomly = quota. Stratified would "
                        "choose randomly within each group — the randomness is the "
                        "difference."
                    ),
                    "check": ["50 + 50 == 100"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Name and critique", "problemId": "ibsl-41-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Bias radar",
                    "title": "Spot the flaw",
                    "prompt": "An online poll on a gaming site asks 'how many hours do you game weekly?'. The main problem is:",
                    "options": [
                        "The sample over-represents gamers — selection bias",
                        "The sample is too small",
                        "Hours are continuous data",
                        "The question is too personal",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Visitors of a gaming site are not the general population — however "
                        "large the sample, the frame is biased. Size never fixes selection "
                        "bias."
                    ),
                    "check": ["1 == 1"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Markscheme wisdom",
                    "title": "Comment = claim + reason",
                    "body": (
                        "Every 'state', 'comment', 'suggest' answer in this code is two "
                        "clauses: the verdict AND the scenario-specific reason. 'Biased "
                        "because Tuesday-morning shoppers exclude workers' scores; 'it's "
                        "biased' alone does not."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Gym strata", "problemId": "ibsl-41-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Discrete or continuous?", "problemId": "ibsl-41-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.1 in four lines",
                    "points": [
                        "Population = target; sample = measured; random = equal chances.",
                        "Five techniques — name in one word, critique in the scenario.",
                        "Stratified shares: group size ÷ population × sample size; totals must reconcile.",
                        "Outliers: remove only with a reason; otherwise keep and discuss.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — SL 4.2: Presentation of data
# ===========================================================================
def lesson_presentation():
    return {
        "slug": "presenting-data",
        "title": "Presenting Data: Histograms, Cumulative Frequency & Box Plots",
        "concreteComparison": (
            "The same 30 test scores can look like a mountain (histogram), a climbing S-curve "
            "(cumulative frequency), or a five-number skeleton (box plot). Three pictures, one "
            "dataset — the IB tests whether you can read each and translate between them."
        ),
        "objective": (
            "Build and read frequency tables and histograms, cumulative frequency graphs "
            "(medians and quartiles off the curve), and box-and-whisker diagrams, including "
            "the $1.5 \\times$ IQR outlier fences."
        ),
        "concept": [
            "**Syllabus card — SL 4.2.** Presentation of data: frequency distributions and "
            "histograms (equal class widths at SL); cumulative frequency graphs, used to find "
            "medians, quartiles and percentiles; box-and-whisker diagrams; identifying "
            "outliers as values beyond $Q_1 - 1.5 \\times IQR$ or $Q_3 + 1.5 \\times IQR$. "
            "**Papers 1 and 2**, with reading-off-the-graph questions a Paper 2 staple.",
            "A HISTOGRAM stacks frequencies over class intervals — shape at a glance: "
            "symmetric, skewed, bimodal. Grouped data trades detail for clarity; the "
            "modal class is the tallest bar, and SL keeps class widths equal so height IS "
            "frequency.",
            "The CUMULATIVE FREQUENCY graph plots 'how many are at or below' against the "
            "UPPER boundary of each class, always climbing. Read the median at half the "
            "total, $Q_1$ at a quarter, $Q_3$ at three-quarters — horizontal in from the "
            "count axis, down to the value axis. Percentiles generalize the same move.",
            "The BOX PLOT draws the five-number summary: min, $Q_1$, median, $Q_3$, max — "
            "the box holds the middle 50% (its width IS the IQR). The FENCE TEST makes "
            "'outlier' precise: anything beyond $1.5 \\times IQR$ outside the box gets "
            "plotted as a separate point. Two box plots on one axis is the IB's favorite "
            "'compare the distributions' setup: compare a CENTER (medians) and a SPREAD "
            "(IQRs), in context, one sentence each."
        ],
        "keyIdea": (
            "Histogram = shape; cumulative curve = read any quantile; box plot = five-number "
            "skeleton with fences at $1.5 \\times IQR$. Comparisons quote one center and one "
            "spread."
        ),
        "facts": [
            {
                "title": "Outlier fences",
                "latex": "x < Q_1 - 1.5 \\times IQR \\quad\\text{or}\\quad x > Q_3 + 1.5 \\times IQR",
                "explanation": "The syllabus's own definition (SL 4.2). IQR $= Q_3 - Q_1$.",
            },
            {
                "title": "Reading the cumulative curve",
                "latex": "\\text{median at } \\tfrac{n}{2}, \\quad Q_1 \\text{ at } \\tfrac{n}{4}, \\quad Q_3 \\text{ at } \\tfrac{3n}{4}",
                "explanation": "Horizontal in from the count, down to the value. NOT in the booklet — a graph skill.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-42-we1",
                "statement": (
                    "The times (minutes) of $11$ runners are: $3, 5, 5, 6, 7, 8, 9, 10, 12, "
                    "13, 15$.  \n"
                    "**(a)** **Write down** the median. **[1]**  \n"
                    "**(b)** Find $Q_1$, $Q_3$ and the IQR. **[3]**  \n"
                    "**(c)** Use the fence test to show there are no outliers. **[2]**"
                ),
                "solution": (
                    "**(a)** The 6th of 11 values: median $= 8$ *(A1)*.  \n"
                    "**(b)** Lower half $3, 5, 5, 6, 7$: $Q_1 = 5$; upper half $9, 10, 12, "
                    "13, 15$: $Q_3 = 12$; IQR $= 7$ *(A1 A1 A1)*.  \n"
                    "**(c)** Fences: $5 - 10.5 = -5.5$ and $12 + 10.5 = 22.5$ *(M1)*. All "
                    "values lie in $[-5.5, 22.5]$ — no outliers *(R1)*.  \n"
                    "**Narrative:** the five-number summary $3, 5, 8, 12, 15$ IS the box "
                    "plot. The fence conclusion needs the comparison sentence — computing "
                    "$22.5$ and stopping loses the R-mark."
                ),
                "check": [
                    "Rational(11 + 1, 2) == 6",
                    "12 - 5 == 7",
                    "5 - Rational(3,2)*7 == Rational(-11, 2)",
                    "12 + Rational(3,2)*7 == Rational(45, 2)",
                    "15 < Rational(45, 2)",
                ],
            },
            {
                "id": "ibsl-42-we2",
                "statement": (
                    "A cumulative frequency graph shows the masses of $80$ parcels. The curve "
                    "passes through $(1.0, 20)$, $(1.4, 40)$ and $(2.0, 60)$, where mass is "
                    "in kg.  \n"
                    "**(a)** **Write down** the median and the IQR. **[3]**  \n"
                    "**(b)** The heaviest parcel is $3.1$ kg. Determine whether it is an "
                    "outlier. **[2]**"
                ),
                "solution": (
                    "**(a)** $n = 80$: median at count $40 \\to 1.4$ kg; $Q_1$ at $20 \\to "
                    "1.0$; $Q_3$ at $60 \\to 2.0$: IQR $= 1.0$ kg *(A1 A1 A1)*.  \n"
                    "**(b)** Upper fence: $2.0 + 1.5 \\times 1.0 = 3.5$ *(M1)*. Since "
                    "$3.1 < 3.5$, NOT an outlier *(R1)*.  \n"
                    "**Narrative:** the counts $20, 40, 60$ are exactly $\\frac{n}{4}, "
                    "\\frac{n}{2}, \\frac{3n}{4}$ — the question hands you the read-offs. "
                    "Verdicts always carry the comparison ('$3.1 < 3.5$')."
                ),
                "check": [
                    "Rational(80, 2) == 40",
                    "2 - 1 == 1",
                    "2 + Rational(3,2)*1 == Rational(7,2)",
                    "Rational(31,10) < Rational(7,2)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Plotting cumulative frequency over class MIDPOINTS.",
                "correction": "Cumulative counts attach to UPPER class boundaries — 'at or below the top of this class'.",
                "authored": True,
            },
            {
                "text": "Comparing two box plots by listing all ten numbers.",
                "correction": "One sentence on centers (medians), one on spreads (IQRs), both in context. That's the whole rubric.",
                "authored": True,
            },
            {
                "text": "Whiskers drawn to the fences instead of to the most extreme non-outlier data.",
                "correction": "Fences are invisible test lines; whiskers end at real data points.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-42-t1",
                "statement": (
                    "A dataset has $Q_1 = 24$ and $Q_3 = 38$. **Find** the fences, and "
                    "determine whether the value $60$ is an outlier. **[3]**"
                ),
                "solution": (
                    "IQR $= 14$; fences $24 - 21 = 3$ and $38 + 21 = 59$ *(M1 A1)*. "
                    "$60 > 59$: outlier ✓ *(R1)* — plotted as a lone point beyond the whisker."
                ),
                "check": ["38 - 24 == 14", "38 + Rational(3,2)*14 == 59", "60 > 59"],
            },
            {
                "id": "ibsl-42-t2",
                "statement": (
                    "On a cumulative frequency graph of $200$ students' scores, the 90th "
                    "percentile is read at which cumulative count? And the median at which? "
                    "**[2]**"
                ),
                "solution": (
                    "90th percentile: count $0.9 \\times 200 = 180$; median: count $100$ "
                    "*(A1 A1)*. In from the count axis, down to the score axis."
                ),
                "check": ["Rational(90, 100)*200 == 180", "Rational(200, 2) == 100"],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.2 · Papers 1 & 2",
                    "title": "Three pictures of one dataset",
                    "body": (
                        "Histogram for shape, cumulative curve for quantiles, box plot for "
                        "the five-number skeleton. The exam draws one and asks you to read "
                        "it — or hands you two box plots and asks for a comparison worth "
                        "two sentences."
                    ),
                },
                {
                    "kind": "histogramBins",
                    "eyebrow": "Shape from bars",
                    "title": "One dataset, several histograms",
                    "teach": (
                        "Regroup the same values into wider or narrower classes and watch "
                        "the shape sharpen or drown. Grouping is a lens: the data doesn't "
                        "change, the story told does."
                    ),
                    "config": {"data": [3, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 15, 16, 18, 21, 22, 26], "min": 0, "max": 30, "widths": [2, 5, 10], "start": 1, "xLabel": "time (min)"},
                },
                {
                    "kind": "boxPlot",
                    "eyebrow": "The skeleton",
                    "title": "Five numbers and their fences",
                    "teach": (
                        "The box holds the middle half; the whiskers reach the extreme "
                        "non-outliers; anything beyond the $1.5 \\times IQR$ fences plots "
                        "alone. Toggle the fences to see the test lines the whiskers obey."
                    ),
                    "config": {"data": [3, 5, 5, 6, 7, 8, 9, 10, 12, 13, 15, 30], "xLabel": "time (min)", "showFences": True},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Five numbers and a fence test", "problemId": "ibsl-42-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Fence fluency",
                    "title": "Outlier or not?",
                    "prompt": "$Q_1 = 10$, $Q_3 = 18$. Which value is an outlier?",
                    "options": ["$31$", "$29$", "$0$", "$25$"],
                    "correctIndex": 0,
                    "explanation": (
                        "IQR $= 8$: fences at $10 - 12 = -2$ and $18 + 12 = 30$. Only $31$ "
                        "escapes; $29$ and $25$ sit inside, and even $0$ clears the lower "
                        "fence."
                    ),
                    "check": ["18 + Rational(3,2)*8 == 30", "31 > 30", "29 < 30", "0 > -2"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Reading the climbing curve", "problemId": "ibsl-42-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Curve reading",
                    "title": "Which count for Q3?",
                    "prompt": "A cumulative frequency graph shows $120$ plants. $Q_3$ is read at cumulative count:",
                    "options": ["$90$", "$60$", "$30$", "$75$"],
                    "correctIndex": 0,
                    "explanation": "Three-quarters of $120$: in at $90$, down to the value axis. ($60$ reads the median, $30$ reads $Q_1$.)",
                    "check": ["Rational(3,4)*120 == 90"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Compare like an examiner",
                    "title": "The two-sentence comparison",
                    "body": (
                        "'Compare the distributions' has a fixed rubric: one sentence on "
                        "CENTER ('B's median time is 2 min lower — typically faster') and "
                        "one on SPREAD ('B's IQR is wider — less consistent'), both in "
                        "context. Extra sentences add nothing; missing either loses a mark."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Test a suspect value", "problemId": "ibsl-42-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Percentile read-offs", "problemId": "ibsl-42-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.2 in four lines",
                    "points": [
                        "Histogram: shape over equal classes; modal class = tallest bar.",
                        "Cumulative curve: upper boundaries; quantiles read at $\\frac{n}{4}, \\frac{n}{2}, \\frac{3n}{4}$.",
                        "Box plot: five numbers; outliers beyond $1.5 \\times IQR$ fences plot alone.",
                        "Comparisons: one center sentence + one spread sentence, in context.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — SL 4.3: Central tendency and dispersion
# ===========================================================================
def lesson_center_spread():
    return {
        "slug": "centre-and-spread",
        "title": "Centre & Spread: Mean, Median, Standard Deviation",
        "concreteComparison": (
            "Two classes both average 70 on a test — but one packs every score between 65 and "
            "75 while the other swings from 40 to 100. The centre says they're twins; the "
            "SPREAD says they're strangers. You need both numbers to tell any data story."
        ),
        "objective": (
            "Compute and interpret mean, median and mode; variance and standard deviation "
            "(by GDC); quartiles and IQR; and track how linear transformations of the data "
            "move each statistic."
        ),
        "concept": [
            "**Syllabus card — SL 4.3.** Measures of central tendency (mean, median, mode); "
            "estimation of the mean from grouped data; modal class; measures of dispersion "
            "(IQR, standard deviation, variance) obtained by TECHNOLOGY; the effect of "
            "constants on the statistics; outliers' influence. **Papers 1 and 2** — the "
            "syllabus explicitly expects sd from the GDC, but the exam expects you to know "
            "what it MEANS.",
            "The mean $\\bar{x} = \\frac{\\sum x}{n}$ balances the data (every value pulls "
            "it); the median splits the sorted list (outliers barely touch it); the mode is "
            "the most frequent. Skewed data pulls the mean toward its tail — which is why "
            "salaries report medians. For grouped data, the mean is ESTIMATED with class "
            "midpoints, and the question says 'estimate' for exactly that reason.",
            "Standard deviation measures typical distance from the mean; VARIANCE is its "
            "square ($\\sigma^2$). On the exam you read both from the GDC's one-variable "
            "stats — but interpretation questions ('which class is more consistent?') want "
            "the smaller sd, cited in context.",
            "The transformation rules: adding a constant $k$ to every value shifts mean and "
            "median by $k$ but leaves sd and IQR UNCHANGED (the pack moves, its width "
            "doesn't); multiplying by $a$ scales EVERYTHING — mean by $a$, sd by $|a|$, "
            "variance by $a^2$. Combined $y = ax + k$: new mean $a\\bar{x} + k$, new sd "
            "$|a| s$. These rules are quick marks every session."
        ],
        "keyIdea": (
            "Centre (mean/median) plus spread (sd/IQR) tell the story together. Shifts move "
            "centres only; scalings stretch both — sd by $|a|$, variance by $a^2$."
        ),
        "facts": [
            {
                "title": "The mean",
                "latex": "\\bar{x} = \\frac{\\sum_{i=1}^{n} x_i}{n}",
                "explanation": "IN the booklet (SL 4.3). Grouped data: use class midpoints — and say 'estimate'.",
            },
            {
                "title": "Linear transformation rules",
                "latex": "y = ax + k: \\quad \\bar{y} = a\\bar{x} + k, \\qquad s_y = |a| \\, s_x",
                "explanation": "NOT in the booklet. Shifts don't touch spread; scales multiply it (variance by $a^2$).",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-43-we1",
                "statement": (
                    "Six friends score $2, 4, 4, 5, 7, 8$ in a game.  \n"
                    "**(a)** Find the mean, median and mode. **[3]**  \n"
                    "**(b)** Given that the population variance is $4$, **write down** the "
                    "standard deviation. **[1]**  \n"
                    "**(c)** Verify the variance value by direct computation. **[2]**"
                ),
                "solution": (
                    "**(a)** Mean $= \\frac{30}{6} = 5$; median $= \\frac{4 + 5}{2} = 4.5$; "
                    "mode $= 4$ *(A1 A1 A1)*.  \n"
                    "**(b)** $\\sigma = \\sqrt{4} = 2$ *(A1)*.  \n"
                    "**(c)** Squared deviations: $9, 1, 1, 0, 4, 9$; sum $24$; variance "
                    "$= \\frac{24}{6} = 4$ ✓ *(M1 A1)*.  \n"
                    "**Narrative:** three different centres from one dataset — they agree "
                    "only for symmetric data. On the exam the GDC does (c) instantly; the "
                    "by-hand version here is so the number MEANS something: average squared "
                    "distance from the mean."
                ),
                "check": [
                    "Rational(2+4+4+5+7+8, 6) == 5",
                    "Rational(4+5, 2) == Rational(9,2)",
                    "9 + 1 + 1 + 0 + 4 + 9 == 24",
                    "Rational(24, 6) == 4",
                    "sqrt(4) == 2",
                ],
            },
            {
                "id": "ibsl-43-we2",
                "statement": (
                    "Exam scores have mean $62$ and standard deviation $8$. The teacher "
                    "rescales every score using $y = 1.1x + 5$.  \n"
                    "**(a)** Find the new mean and new standard deviation. **[3]**  \n"
                    "**(b)** **Write down** the new variance. **[1]**"
                ),
                "solution": (
                    "**(a)** New mean $= 1.1(62) + 5 = 73.2$ *(M1 A1)*; new sd $= 1.1 "
                    "\\times 8 = 8.8$ *(A1)* — the $+5$ shift never touches the spread.  \n"
                    "**(b)** New variance $= 8.8^2 = 77.44$ *(A1)*.  \n"
                    "**Narrative:** the mean rides the whole transformation; the sd feels "
                    "only the stretch. Wrong answers almost always add the 5 to the sd — "
                    "shifting everyone up doesn't spread them out."
                ),
                "check": [
                    "Rational(11,10)*62 + 5 == Rational(366, 5)",
                    "Rational(11,10)*8 == Rational(44, 5)",
                    "Rational(44,5)**2 == Rational(1936, 25)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Adding the shift constant to the standard deviation.",
                "correction": "Shifts move the pack, not its width: $y = x + k$ leaves sd (and IQR) unchanged.",
                "authored": True,
            },
            {
                "text": "Scaling variance by $a$ instead of $a^2$.",
                "correction": "Variance is squared units: $y = ax$ gives $s_y^2 = a^2 s_x^2$ (sd scales by $|a|$).",
                "authored": True,
            },
            {
                "text": "Reporting the mean for salary-like skewed data without comment.",
                "correction": "Outliers drag the mean toward the tail; the median resists — and saying so is often the R-mark.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-43-t1",
                "statement": (
                    "Data has mean $40$ and sd $6$. Every value is transformed by "
                    "$y = 2x - 10$. **Write down** the new mean, sd and variance. **[3]**"
                ),
                "solution": (
                    "Mean $2(40) - 10 = 70$; sd $2 \\times 6 = 12$; variance $144$ "
                    "*(A1 A1 A1)*."
                ),
                "check": ["2*40 - 10 == 70", "2*6 == 12", "12**2 == 144"],
            },
            {
                "id": "ibsl-43-t2",
                "statement": (
                    "Grouped data: class $[0, 10)$ frequency $4$; $[10, 20)$ frequency "
                    "$10$; $[20, 30)$ frequency $6$. **Estimate** the mean. **[3]**"
                ),
                "solution": (
                    "Midpoints $5, 15, 25$: $\\bar{x} \\approx \\frac{4(5) + 10(15) + "
                    "6(25)}{20} = \\frac{320}{20} = 16$ *(M1 A1 A1)*. 'Estimate' because "
                    "the true values inside each class are unknown."
                ),
                "check": ["4*5 + 10*15 + 6*25 == 320", "Rational(320, 20) == 16"],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.3 · Papers 1 & 2",
                    "title": "Two numbers tell the story",
                    "body": (
                        "A centre without a spread is half a description. This code: three "
                        "centres, two spreads, the GDC's role, and the transformation rules "
                        "that turn into quick marks every exam session."
                    ),
                },
                {
                    "kind": "dotPlot",
                    "eyebrow": "Mean vs median",
                    "title": "Drag one value, watch who follows",
                    "teach": (
                        "Pull the largest value away and the MEAN chases it — every value "
                        "tugs the balance point. The MEDIAN stays planted: only order "
                        "matters to it. This is why outliers argue for medians."
                    ),
                    "config": {"mode": "meanMedian", "data": [2, 4, 4, 5, 7, 8], "min": 0, "max": 20, "xLabel": "score"},
                },
                {
                    "kind": "dotPlot",
                    "eyebrow": "What sd measures",
                    "title": "Sticks from the mean",
                    "teach": (
                        "Each stick runs from the mean to a data point; the standard "
                        "deviation summarizes their typical length. Tight data, short "
                        "sticks, small sd — consistency made visible."
                    ),
                    "config": {"mode": "deviations", "data": [2, 4, 4, 5, 7, 8], "min": 0, "max": 12, "xLabel": "score"},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Three centres, one variance", "problemId": "ibsl-43-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Robustness",
                    "title": "Who resists the outlier?",
                    "prompt": "Replacing the largest of $2, 4, 4, 5, 7, 8$ with $80$ changes:",
                    "options": [
                        "The mean a lot, the median not at all",
                        "Both equally",
                        "The median a lot, the mean slightly",
                        "Neither",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "New mean $= \\frac{102}{6} = 17$ (was 5); the sorted middle pair "
                        "is still $4, 5$ — median stays $4.5$. Balance point vs order "
                        "statistic."
                    ),
                    "check": ["Rational(2+4+4+5+7+80, 6) == 17", "Rational(4+5, 2) == Rational(9,2)"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Rescaled scores", "problemId": "ibsl-43-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Transformation rules",
                    "title": "The shift that does nothing",
                    "prompt": "Every value in a dataset is increased by $12$. The standard deviation:",
                    "options": ["Is unchanged", "Increases by $12$", "Increases by $\\sqrt{12}$", "Is multiplied by $12$"],
                    "correctIndex": 0,
                    "explanation": (
                        "The whole pack slides together — distances from the (also-shifted) "
                        "mean are identical. Spread ignores shifts."
                    ),
                    "check": ["(5 + 12) - (2 + 12) == 5 - 2"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "GDC + markscheme",
                    "title": "Technology with a sentence",
                    "body": (
                        "The syllabus SAYS sd comes from technology — so on Paper 2, run "
                        "one-variable stats and quote it. The marks beyond A1 come from "
                        "interpretation: 'smaller sd, so more consistent' in the question's "
                        "context. Number + sentence, every time."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Transform everything", "problemId": "ibsl-43-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Midpoint estimate", "problemId": "ibsl-43-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.3 in four lines",
                    "points": [
                        "Mean balances, median splits, mode repeats — they agree only when data is symmetric.",
                        "sd = typical distance from the mean; variance = sd². Read both from the GDC.",
                        "Shifts: centres move, spreads don't. Scales: sd × $|a|$, variance × $a^2$.",
                        "Grouped data: midpoints, and the word 'estimate'.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — SL 4.4: Correlation and the y-on-x regression line
# ===========================================================================
def lesson_correlation():
    return {
        "slug": "correlation-and-regression",
        "title": "Correlation & the Regression Line",
        "concreteComparison": (
            "Hours studied vs exam score, drawn as a cloud of points: the cloud leans, and "
            "Pearson's $r$ measures the lean in one number from $-1$ to $1$. The regression "
            "line is the cloud's spine — and the IB will ask you to use it, and to know when "
            "you shouldn't."
        ),
        "objective": (
            "Interpret scatter diagrams and Pearson's $r$ (from the GDC); find and use the "
            "$y$-on-$x$ regression line; respect the mean point; distinguish interpolation "
            "from extrapolation; never confuse correlation with causation."
        ),
        "concept": [
            "**Syllabus card — SL 4.4.** Linear correlation of bivariate data; Pearson's "
            "product-moment correlation coefficient $r$; scatter diagrams; lines of best fit "
            "BY EYE passing through the mean point $(\\bar{x}, \\bar{y})$; equation of the "
            "regression line of $y$ on $x$ (by TECHNOLOGY); use of the line for prediction. "
            "**Mostly Paper 2** — the GDC computes $r$ and the line; you interpret and "
            "predict.",
            "$r$ measures LINEAR association only: sign gives direction, magnitude gives "
            "strength ($|r|$ near 1 strong, near 0 weak). The IB's interpretation sentence "
            "has a fixed shape: STRENGTH + DIRECTION + 'linear' + context — '$r = 0.92$: a "
            "strong positive linear correlation between hours studied and score'. A curved "
            "relationship can have $r \\approx 0$; always glance at the scatter first.",
            "The $y$-on-$x$ regression line minimizes VERTICAL misses, and it always passes "
            "through the mean point $(\\bar{x}, \\bar{y})$ — a fact exam questions test "
            "directly ('find the line given the means and gradient'). Use it to predict "
            "$y$ FROM $x$; predicting $x$ from it is the wrong tool (SL 4.10 has the right "
            "one).",
            "Prediction etiquette: INTERPOLATION (inside the data's $x$-range) is reliable "
            "when $|r|$ is strong; EXTRAPOLATION (outside the range) is untrustworthy — say "
            "so, in those words, for the mark. And $r = 0.9$ between ice-cream sales and "
            "drownings doesn't mean ice cream drowns people: correlation is not causation, "
            "and the IB asks for exactly that sentence about once a year."
        ],
        "keyIdea": (
            "$r$ = strength + direction of the LINEAR lean; the regression line is the "
            "cloud's spine through $(\\bar{x}, \\bar{y})$. Predict inside the data; distrust "
            "outside it; never infer cause."
        ),
        "facts": [
            {
                "title": "Reading r",
                "latex": "-1 \\le r \\le 1: \\quad \\text{sign = direction}, \\quad |r| = \\text{strength (linear only)}",
                "explanation": "$r$ comes from the GDC. The interpretation sentence: strength + direction + linear + context.",
            },
            {
                "title": "The mean point",
                "latex": "\\text{the } y\\text{-on-}x \\text{ line always passes through } (\\bar{x}, \\bar{y})",
                "explanation": "The syllabus states it (SL 4.4); exams test it by handing you means and a gradient.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-44-we1",
                "statement": (
                    "For 10 students, hours studied $x$ and score $y$ give (by GDC) "
                    "$r = 0.92$ and regression line $y = 2.4x + 11$, for $2 \\le x \\le 15$.  \n"
                    "**(a)** Interpret the value of $r$. **[2]**  \n"
                    "**(b)** Estimate the score of a student who studied $10$ hours. **[2]**  \n"
                    "**(c)** Explain why the line should NOT be used for a student who "
                    "studied $40$ hours. **[1]**"
                ),
                "solution": (
                    "**(a)** A strong, positive, linear correlation between hours studied "
                    "and score *(A1 A1 — strength AND direction, in context)*.  \n"
                    "**(b)** $y = 2.4(10) + 11 = 35$ *(M1 A1)*.  \n"
                    "**(c)** $40$ lies far outside the data range ($2 \\le x \\le 15$) — "
                    "extrapolation is unreliable *(R1)*.  \n"
                    "**Narrative:** three marks here are SENTENCES, not numbers. The "
                    "interpretation template and the word 'extrapolation' are worth "
                    "memorizing verbatim."
                ),
                "check": [
                    "Rational(24,10)*10 + 11 == 35",
                    "40 > 15",
                ],
            },
            {
                "id": "ibsl-44-we2",
                "statement": (
                    "A dataset has $\\bar{x} = 6$, $\\bar{y} = 20$, and the regression line "
                    "of $y$ on $x$ has gradient $2.5$.  \n"
                    "**(a)** Find the equation of the regression line. **[3]**  \n"
                    "**(b)** Predict $y$ when $x = 8$. **[1]**"
                ),
                "solution": (
                    "**(a)** The line passes through the mean point $(6, 20)$ *(M1 — the "
                    "property IS the method)*: $20 = 2.5(6) + c \\Rightarrow c = 5$ *(A1)*: "
                    "$y = 2.5x + 5$ *(A1)*.  \n"
                    "**(b)** $y = 2.5(8) + 5 = 25$ *(A1)*.  \n"
                    "**Narrative:** no raw data needed — the mean-point property plus one "
                    "substitution builds the whole line. This is the standard Paper 1 "
                    "version of a Paper 2 topic."
                ),
                "check": [
                    "solve(Eq(Rational(5,2)*6 + c, 20), c) == [5]",
                    "Rational(5,2)*8 + 5 == 25",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Interpreting $r = 0.92$ as 'studying causes high scores'.",
                "correction": "Correlation measures association, not cause. The IB sentence: 'strong positive linear correlation' — nothing more.",
                "authored": True,
            },
            {
                "text": "Using the $y$-on-$x$ line to predict $x$ from a known $y$.",
                "correction": "That line minimizes vertical misses only. Predicting $x$ needs the $x$-on-$y$ line (SL 4.10).",
                "authored": True,
            },
            {
                "text": "Predicting far outside the data range without comment.",
                "correction": "Extrapolation — name it and distrust it. The R-mark is the word plus the range.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-44-t1",
                "statement": (
                    "Match each to a value of $r$: (i) strong negative linear; (ii) no "
                    "linear association; (iii) moderate positive linear. Choices: $0.55$, "
                    "$-0.94$, $0.03$. **[3]**"
                ),
                "solution": (
                    "(i) $-0.94$; (ii) $0.03$; (iii) $0.55$ *(A1 A1 A1)*. Magnitude is "
                    "strength; sign is direction."
                ),
                "check": ["Abs(Rational(-94,100)) > Abs(Rational(55,100))", "Abs(Rational(3,100)) < Rational(1,10)"],
            },
            {
                "id": "ibsl-44-t2",
                "statement": (
                    "A regression line $y = -1.8x + 74$ models temperature $y$ (°C) against "
                    "altitude $x$ (hundreds of m), for $5 \\le x \\le 30$. Predict $y$ at "
                    "$x = 20$, and state whether predicting at $x = 3$ is interpolation or "
                    "extrapolation. **[3]**"
                ),
                "solution": (
                    "$y = -1.8(20) + 74 = 38$ °C *(M1 A1)*. $x = 3 < 5$: outside the range — "
                    "extrapolation *(A1)*."
                ),
                "check": ["Rational(-18,10)*20 + 74 == 38", "3 < 5"],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.4 · mostly Paper 2",
                    "title": "The lean of the cloud",
                    "body": (
                        "Bivariate data is a cloud of points; $r$ scores its lean, the "
                        "regression line is its spine. Your GDC computes both — the exam "
                        "pays for interpretation, prediction, and knowing the limits."
                    ),
                },
                {
                    "kind": "scatterPlot",
                    "eyebrow": "See r change",
                    "title": "Clouds at every strength",
                    "teach": (
                        "Morph the dataset between tight positive, loose, and negative "
                        "shapes — and watch what $r$ would say. Strength is TIGHTNESS "
                        "around a line, direction is the lean; a curved cloud can fool "
                        "$r$ entirely."
                    ),
                    "config": {"mode": "correlation", "xLabel": "hours studied", "yLabel": "score"},
                },
                {
                    "kind": "scatterPlot",
                    "eyebrow": "The spine",
                    "title": "Fit the line yourself",
                    "teach": (
                        "Steer the line to minimize the average miss — then compare with "
                        "the least-squares fit. The winning line always passes through "
                        "the mean point: the cloud's centre of gravity."
                    ),
                    "config": {"mode": "fit", "xLabel": "hours studied", "yLabel": "score", "m0": 1, "b0": 20},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Interpret, predict, refuse", "problemId": "ibsl-44-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Interpretation template",
                    "title": "Say it like the markscheme",
                    "prompt": "$r = -0.85$ for ice-cream sales vs month rank. The correct interpretation is:",
                    "options": [
                        "A strong negative linear correlation",
                        "Ice cream sales cause the months to change",
                        "A weak negative correlation",
                        "No conclusion is possible",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "$|r| = 0.85$ is strong; the sign is negative; 'linear' completes "
                        "the template. Causation is never on offer."
                    ),
                    "check": ["Abs(Rational(-85,100)) > Rational(7,10)"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Build the line from the means", "problemId": "ibsl-44-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The mean point",
                    "title": "One point every line shares",
                    "prompt": "A regression line of $y$ on $x$ MUST pass through:",
                    "options": [
                        "$(\\bar{x}, \\bar{y})$",
                        "The origin",
                        "The first data point",
                        "$(\\text{median } x, \\text{median } y)$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The least-squares line balances vertical misses, and the balance "
                        "point is the mean point — the property SL 4.4 states and exams "
                        "exploit."
                    ),
                    "check": ["1 == 1"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Paper 2 wisdom",
                    "title": "Three sentences to memorize",
                    "body": (
                        "(1) '$r = \\ldots$: a strong/moderate/weak, positive/negative, "
                        "LINEAR correlation between [x] and [y].' (2) 'Reliable: "
                        "interpolation within the data range with strong $|r|$.' (3) "
                        "'Unreliable: extrapolation outside the range.' These three "
                        "sentences are worth 3–4 marks nearly every session."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Match the r values", "problemId": "ibsl-44-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Altitude and temperature", "problemId": "ibsl-44-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.4 in four lines",
                    "points": [
                        "$r \\in [-1, 1]$: sign = direction, size = strength, LINEAR only.",
                        "The $y$-on-$x$ line predicts $y$ from $x$ and passes through $(\\bar{x}, \\bar{y})$.",
                        "Interpolate with confidence; extrapolate with a warning; cause never follows.",
                        "GDC computes; you interpret in the template sentence.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — SL 4.5: Probability concepts
# ===========================================================================
def lesson_probability_concepts():
    return {
        "slug": "probability-concepts",
        "title": "Probability: The Language of Chance",
        "concreteComparison": (
            "Roll a die 600 times and 'a six' happens ABOUT 100 times — not exactly, but the "
            "longer you roll, the closer the fraction creeps to $\\frac{1}{6}$. Probability "
            "is that long-run fraction, captured before the first roll."
        ),
        "objective": (
            "Use the vocabulary (trial, outcome, sample space, event); compute equally-likely "
            "probabilities; use complements; find expected numbers of occurrences; connect "
            "theoretical probability with relative frequency."
        ),
        "concept": [
            "**Syllabus card — SL 4.5.** Concepts of trial, outcome, equally likely outcomes, "
            "relative frequency, sample space $U$ and event; $P(A) = \\frac{n(A)}{n(U)}$; "
            "complementary events $A$ and $A'$ with $P(A) + P(A') = 1$; expected number of "
            "occurrences. **Papers 1 and 2** — short questions, quick marks, and the "
            "foundation everything in 4.6–4.8 stands on.",
            "When outcomes are equally likely, probability is counting: $P(A) = "
            "\\frac{n(A)}{n(U)}$, favourable over possible. The sample space $U$ is the "
            "complete list of outcomes — write it down for anything non-obvious (two dice: "
            "36 pairs, not 11 sums!). Every probability lives in $[0, 1]$.",
            "The complement $A'$ ('not $A$') satisfies $P(A') = 1 - P(A)$ — in the booklet. "
            "Its exam superpower: 'at least one' questions flip to 'none' — computing "
            "$1 - P(\\text{none})$ is almost always faster than adding cases.",
            "EXPECTED occurrences $= n \\times p$: in 60 draws with $P(\\text{red}) = "
            "\\frac{1}{4}$, expect 15 reds — a long-run average, not a promise. Relative "
            "frequency (observed fraction) ESTIMATES probability and sharpens as trials "
            "grow; comparing the two ('is the die fair?') is a standard one-mark comment."
        ],
        "keyIdea": (
            "Probability = favourable over possible, on a fully listed sample space. "
            "Complements flip 'at least one' into 'none'; expected count = $np$."
        ),
        "facts": [
            {
                "title": "Equally likely outcomes",
                "latex": "P(A) = \\frac{n(A)}{n(U)}",
                "explanation": "IN the booklet (SL 4.5). Valid only when outcomes are equally likely — list them to be sure.",
            },
            {
                "title": "Complement",
                "latex": "P(A) + P(A') = 1",
                "explanation": "IN the booklet. 'At least one' = $1 - P(\\text{none})$: the exam's favourite shortcut.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-45-we1",
                "statement": (
                    "A bag holds $3$ red, $5$ blue and $4$ green counters. One is drawn at "
                    "random.  \n"
                    "**(a)** **Write down** $P(\\text{red})$. **[1]**  \n"
                    "**(b)** Find $P(\\text{not green})$. **[2]**  \n"
                    "**(c)** In $60$ draws (with replacement), find the expected number of "
                    "reds. **[2]**"
                ),
                "solution": (
                    "**(a)** $P(\\text{red}) = \\frac{3}{12} = \\frac{1}{4}$ *(A1)*.  \n"
                    "**(b)** Complement: $1 - \\frac{4}{12} = \\frac{8}{12} = \\frac{2}{3}$ "
                    "*(M1 A1)*.  \n"
                    "**(c)** $60 \\times \\frac{1}{4} = 15$ *(M1 A1)*.  \n"
                    "**Narrative:** three booklet-backed one-liners. In (c), 15 is the "
                    "long-run average — writing 'expect about 15' shows you know what "
                    "expectation means."
                ),
                "check": [
                    "Rational(3, 12) == Rational(1, 4)",
                    "1 - Rational(4, 12) == Rational(2, 3)",
                    "60*Rational(1, 4) == 15",
                ],
            },
            {
                "id": "ibsl-45-we2",
                "statement": (
                    "Two fair dice are rolled and the scores added.  \n"
                    "**(a)** **Write down** the number of equally likely outcomes. **[1]**  \n"
                    "**(b)** Find the probability the total is $9$. **[2]**  \n"
                    "**(c)** Find the probability the total is at least $4$. **[2]**"
                ),
                "solution": (
                    "**(a)** $6 \\times 6 = 36$ ordered pairs *(A1)*.  \n"
                    "**(b)** Total 9: $(3,6), (4,5), (5,4), (6,3)$ — four pairs: "
                    "$\\frac{4}{36} = \\frac{1}{9}$ *(M1 A1)*.  \n"
                    "**(c)** Complement: totals below 4 are $2$ and $3$ — pairs $(1,1), "
                    "(1,2), (2,1)$: $P = 1 - \\frac{3}{36} = \\frac{33}{36} = \\frac{11}{12}$ "
                    "*(M1 A1)*.  \n"
                    "**Narrative:** the sample space is 36 PAIRS, not 11 sums — sums aren't "
                    "equally likely. And (c) flips 'at least' to its tiny complement: 3 "
                    "pairs beat 33."
                ),
                "check": [
                    "6*6 == 36",
                    "Rational(4, 36) == Rational(1, 9)",
                    "1 - Rational(3, 36) == Rational(11, 12)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Treating the 11 possible dice totals as equally likely.",
                "correction": "The 36 ordered PAIRS are equally likely; totals inherit different counts (7 gets six pairs, 2 gets one).",
                "authored": True,
            },
            {
                "text": "Computing 'at least one' by adding every qualifying case.",
                "correction": "$1 - P(\\text{none})$ — one subtraction replaces a case-by-case slog.",
                "authored": True,
            },
            {
                "text": "Reading 'expected number 15' as a guarantee.",
                "correction": "Expectation is the long-run average; single runs vary. Say 'on average' and mean it.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-45-t1",
                "statement": (
                    "A spinner has $P(\\text{win}) = 0.15$. It is spun $200$ times. **Find** "
                    "the expected number of wins, and $P(\\text{not win})$ on one spin. **[2]**"
                ),
                "solution": (
                    "$200 \\times 0.15 = 30$ wins expected *(A1)*; complement "
                    "$1 - 0.15 = 0.85$ *(A1)*."
                ),
                "check": ["200*Rational(15,100) == 30", "1 - Rational(15,100) == Rational(17,20)"],
            },
            {
                "id": "ibsl-45-t2",
                "statement": (
                    "A die is rolled $300$ times; a six appears $62$ times. **Write down** "
                    "the relative frequency of a six, the theoretical probability, and "
                    "comment on the die's fairness. **[3]**"
                ),
                "solution": (
                    "Relative frequency $\\frac{62}{300} \\approx 0.207$; theoretical "
                    "$\\frac{1}{6} \\approx 0.167$ *(A1 A1)*. The observed rate is somewhat "
                    "high but a 300-roll sample varies; more trials needed before calling "
                    "it biased *(R1)*."
                ),
                "check": ["Abs(Rational(62,300) - 0.2067) < 0.001", "Abs(Rational(1,6) - 0.1667) < 0.001"],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.5 · Papers 1 & 2",
                    "title": "Chance, before it happens",
                    "body": (
                        "Probability assigns tomorrow's long-run fraction today. The "
                        "machinery is counting — favourable over possible — plus one "
                        "shortcut (the complement) and one bridge to reality (relative "
                        "frequency)."
                    ),
                },
                {
                    "kind": "longRunFrequency",
                    "eyebrow": "Watch it converge",
                    "title": "The long run, live",
                    "teach": (
                        "Roll in batches and watch the observed fraction wobble toward "
                        "$\\frac{1}{6}$. Early chaos, late calm — probability is the value "
                        "the wobble settles on, which is why more trials mean better "
                        "estimates."
                    ),
                    "config": {"p": 0.1667, "pLabel": "1/6", "eventLabel": "roll a 6", "actionLabel": "roll"},
                },
                {
                    "kind": "teach",
                    "eyebrow": "The toolkit",
                    "title": "Count, complement, expect",
                    "beats": [
                        "$P(A) = \\frac{n(A)}{n(U)}$ — booklet; valid on EQUALLY LIKELY outcomes (list them!).",
                        "$P(A') = 1 - P(A)$ — booklet; 'at least one' = $1 - P(\\text{none})$.",
                        "Expected occurrences $= np$ — an average, not a promise.",
                    ],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Counters, complements, expectation", "problemId": "ibsl-45-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Sample-space discipline",
                    "title": "Count the space",
                    "prompt": "Two fair coins are flipped. $P(\\text{exactly one head}) =$",
                    "options": ["$\\dfrac{1}{2}$", "$\\dfrac{1}{3}$", "$\\dfrac{1}{4}$", "$\\dfrac{2}{3}$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Sample space: HH, HT, TH, TT — four equally likely outcomes, two "
                        "favourable. The famous wrong answer $\\frac{1}{3}$ comes from "
                        "counting unordered outcomes as equally likely."
                    ),
                    "check": ["Rational(2, 4) == Rational(1, 2)"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Two dice, done right", "problemId": "ibsl-45-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The shortcut",
                    "title": "At least one",
                    "prompt": "A die is rolled 3 times. $P(\\text{at least one six}) =$",
                    "options": [
                        "$1 - \\left(\\dfrac{5}{6}\\right)^3$",
                        "$\\dfrac{1}{2}$",
                        "$3 \\times \\dfrac{1}{6}$",
                        "$\\left(\\dfrac{1}{6}\\right)^3$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Complement of 'no sixes in three rolls'. Adding $\\frac{1}{6}$ "
                        "three times double-counts overlaps (and would exceed 1 with seven "
                        "rolls — a built-in absurdity check)."
                    ),
                    "check": ["1 - Rational(125, 216) == Rational(91, 216)"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "List, then count",
                    "body": (
                        "For any compound experiment, WRITE the sample space (or its size) "
                        "before assigning probabilities — two dice make 36 pairs, three "
                        "coins make 8 strings. Half the errors in this code are counting "
                        "on an unlisted space."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Spinner expectations", "problemId": "ibsl-45-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Is the die fair?", "problemId": "ibsl-45-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.5 in four lines",
                    "points": [
                        "$P = \\frac{n(A)}{n(U)}$ on a LISTED, equally likely sample space.",
                        "$P(A') = 1 - P(A)$; 'at least one' flips to 'none'.",
                        "Expected count $= np$ — a long-run average.",
                        "Relative frequency estimates $p$, and improves with trials.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — SL 4.6: Combined events: Venn, tree, union, conditional
# ===========================================================================
def lesson_combined_events():
    return {
        "slug": "combined-events-venn-and-tree-diagrams",
        "title": "Combined Events: Venn & Tree Diagrams",
        "concreteComparison": (
            "18 students play football, 14 play basketball — but the class has only 30, so "
            "some play both. The Venn diagram sorts the double-counted; the union formula "
            "subtracts them once; the tree diagram handles chance in stages. Three tools, "
            "one code."
        ),
        "objective": (
            "Organize combined events with Venn diagrams, tree diagrams and sample-space "
            "tables; use $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$; recognize mutually "
            "exclusive and independent events; compute with and without replacement."
        ),
        "concept": [
            "**Syllabus card — SL 4.6.** Use of Venn diagrams, tree diagrams, sample-space "
            "diagrams and tables of outcomes; combined events $P(A \\cup B) = P(A) + P(B) - "
            "P(A \\cap B)$; mutually exclusive events ($P(A \\cap B) = 0$); conditional "
            "probability; independent events with $P(A \\cap B) = P(A)P(B)$. All formulas "
            "IN the booklet. **Papers 1 and 2** — a guaranteed appearance, often multi-part.",
            "The UNION formula fixes double-counting: adding $P(A)$ and $P(B)$ counts the "
            "overlap twice, so subtract it once. MUTUALLY EXCLUSIVE events can't co-occur — "
            "the overlap is empty and the formula collapses to plain addition. Fill Venn "
            "diagrams from the INSIDE OUT: overlap first, then the 'only' regions, then "
            "check the total.",
            "TREE diagrams run chance in stages: multiply ALONG a branch (and-then), add "
            "BETWEEN branches (or). WITHOUT replacement, the second stage's fractions shift "
            "— numerator and denominator both drop. Trees make 'exactly one of each' "
            "mechanical: two qualifying paths, added.",
            "CONDITIONAL probability $P(A \\mid B)$ shrinks the world to $B$: read it off "
            "the Venn as $\\frac{\\text{overlap}}{B\\text{'s total}}$. INDEPENDENT events "
            "don't inform each other: $P(A \\cap B) = P(A)P(B)$ — a checkable equation, not "
            "a vibe. (Don't confuse: mutually exclusive events are maximally DEpendent — "
            "one happening forbids the other.) The formal treatment deepens in SL 4.11."
        ],
        "keyIdea": (
            "Venn for overlap, tree for stages: multiply along, add across. Union subtracts "
            "the double-count; independence is the equation $P(A \\cap B) = P(A)P(B)$."
        ),
        "facts": [
            {
                "title": "Union",
                "latex": "P(A \\cup B) = P(A) + P(B) - P(A \\cap B)",
                "explanation": "IN the booklet (SL 4.6). Mutually exclusive: $P(A \\cap B) = 0$, so it collapses to addition.",
            },
            {
                "title": "Independence",
                "latex": "P(A \\cap B) = P(A)\\,P(B)",
                "explanation": "IN the booklet. An equation to CHECK, not assume — and unrelated to mutual exclusivity.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-46-we1",
                "statement": (
                    "In a class of $30$, $18$ play football ($F$), $14$ play basketball "
                    "($B$), and $8$ play both.  \n"
                    "**(a)** Draw the Venn information: find how many play only football, "
                    "only basketball, and neither. **[3]**  \n"
                    "**(b)** Find $P(F \\cup B)$. **[2]**  \n"
                    "**(c)** Find $P(F \\mid B)$. **[2]**"
                ),
                "solution": (
                    "**(a)** Inside out: both $= 8$; only $F = 18 - 8 = 10$; only $B = "
                    "14 - 8 = 6$; neither $= 30 - 24 = 6$ *(A1 A1 A1)*.  \n"
                    "**(b)** $P(F \\cup B) = \\frac{10 + 8 + 6}{30} = \\frac{24}{30} = "
                    "\\frac{4}{5}$ *(M1 A1)* — or by the formula: $\\frac{18}{30} + "
                    "\\frac{14}{30} - \\frac{8}{30}$.  \n"
                    "**(c)** Shrink the world to $B$'s 14: $P(F \\mid B) = \\frac{8}{14} = "
                    "\\frac{4}{7}$ *(M1 A1)*.  \n"
                    "**Narrative:** the Venn, filled overlap-first, answers everything by "
                    "reading regions. Conditional probability is a CHANGE OF DENOMINATOR — "
                    "that one idea is (c)'s whole method."
                ),
                "check": [
                    "18 - 8 == 10",
                    "14 - 8 == 6",
                    "30 - (10 + 8 + 6) == 6",
                    "Rational(24, 30) == Rational(4, 5)",
                    "Rational(8, 14) == Rational(4, 7)",
                ],
            },
            {
                "id": "ibsl-46-we2",
                "statement": (
                    "A bag holds $5$ red and $3$ blue counters. Two are drawn WITHOUT "
                    "replacement.  \n"
                    "**(a)** Find $P(\\text{both red})$. **[2]**  \n"
                    "**(b)** Find $P(\\text{one of each colour})$. **[3]**"
                ),
                "solution": (
                    "**(a)** Along the branch: $\\frac{5}{8} \\cdot \\frac{4}{7} = "
                    "\\frac{20}{56} = \\frac{5}{14}$ *(M1 A1)*.  \n"
                    "**(b)** Two qualifying paths: RB $= \\frac{5}{8} \\cdot \\frac{3}{7} = "
                    "\\frac{15}{56}$ and BR $= \\frac{3}{8} \\cdot \\frac{5}{7} = "
                    "\\frac{15}{56}$ *(M1 A1)*. Add: $\\frac{30}{56} = \\frac{15}{28}$ "
                    "*(A1)*.  \n"
                    "**Narrative:** without replacement, the second fraction remembers the "
                    "first draw — $\\frac{4}{7}$, not $\\frac{5}{8}$. And 'one of each' "
                    "ALWAYS has two paths; forgetting BR is the classic half-answer."
                ),
                "check": [
                    "Rational(5,8)*Rational(4,7) == Rational(5, 14)",
                    "Rational(5,8)*Rational(3,7) + Rational(3,8)*Rational(5,7) == Rational(15, 28)",
                    "Rational(5,14) + Rational(15,28) + Rational(3,8)*Rational(2,7) == 1",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Adding $P(A) + P(B)$ for a union and ignoring the overlap.",
                "correction": "The overlap was counted twice — subtract it once: $P(A) + P(B) - P(A \\cap B)$.",
                "authored": True,
            },
            {
                "text": "Confusing mutually exclusive with independent.",
                "correction": "Exclusive: can't co-occur ($P(A \\cap B) = 0$). Independent: don't inform each other ($P(A \\cap B) = P(A)P(B)$). Exclusive events (with nonzero probs) are never independent.",
                "authored": True,
            },
            {
                "text": "Keeping the same fractions on the second draw without replacement.",
                "correction": "The bag changed: numerator AND denominator drop. $\\frac{5}{8}$ then $\\frac{4}{7}$.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-46-t1",
                "statement": (
                    "$P(A) = 0.6$, $P(B) = 0.5$, $P(A \\cap B) = 0.3$. **Find** "
                    "$P(A \\cup B)$, and determine whether $A$ and $B$ are independent. **[4]**"
                ),
                "solution": (
                    "$P(A \\cup B) = 0.6 + 0.5 - 0.3 = 0.8$ *(M1 A1)*. Independence check: "
                    "$P(A)P(B) = 0.3 = P(A \\cap B)$ ✓ — independent *(M1 R1)*."
                ),
                "check": [
                    "Rational(6,10) + Rational(5,10) - Rational(3,10) == Rational(8,10)",
                    "Rational(6,10)*Rational(5,10) == Rational(3,10)",
                ],
            },
            {
                "id": "ibsl-46-t2",
                "statement": (
                    "Cards numbered $1$–$10$; one is drawn. $A$: the number is even. $B$: "
                    "the number is greater than $7$. **Find** $P(A \\cap B)$, $P(A \\cup B)$ "
                    "and $P(B \\mid A)$. **[4]**"
                ),
                "solution": (
                    "$A = \\{2,4,6,8,10\\}$, $B = \\{8,9,10\\}$, $A \\cap B = \\{8,10\\}$: "
                    "$P(A \\cap B) = \\frac{2}{10}$ *(A1)*. Union: $\\frac{5}{10} + "
                    "\\frac{3}{10} - \\frac{2}{10} = \\frac{3}{5}$ *(M1 A1)*. "
                    "$P(B \\mid A) = \\frac{2}{5}$ *(A1)*."
                ),
                "check": [
                    "Rational(5,10) + Rational(3,10) - Rational(2,10) == Rational(3,5)",
                    "Rational(2, 5) == Rational(2, 5)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.6 · Papers 1 & 2",
                    "title": "Overlaps and stages",
                    "body": (
                        "Real events overlap (Venn) and unfold in stages (tree). This "
                        "code hands you both diagrams, the union formula that fixes "
                        "double-counting, and the first taste of conditional probability "
                        "— the exam's favourite probability question shape."
                    ),
                },
                {
                    "kind": "vennCounts",
                    "eyebrow": "The overlap problem",
                    "title": "Why we subtract once",
                    "teach": (
                        "Watch the double-count happen: $|F| + |B|$ counts the middle "
                        "region twice. Tap the regions, read their counts, and see the "
                        "union formula as bookkeeping, not magic."
                    ),
                    "config": {"mode": "addition", "labelA": "Football", "labelB": "Basketball", "onlyA": 10, "onlyB": 6, "both": 8},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "The Venn workhorse", "problemId": "ibsl-46-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Union fluency",
                    "title": "Subtract the overlap",
                    "prompt": "$P(A) = 0.7$, $P(B) = 0.4$, $P(A \\cap B) = 0.2$. Then $P(A \\cup B) =$",
                    "options": ["$0.9$", "$1.1$", "$0.5$", "$0.28$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$0.7 + 0.4 - 0.2 = 0.9$. Option B forgot the subtraction — and "
                        "landed above 1, probability's built-in alarm bell."
                    ),
                    "check": ["Rational(7,10) + Rational(4,10) - Rational(2,10) == Rational(9,10)"],
                },
                {
                    "kind": "treeDiagram",
                    "eyebrow": "Chance in stages",
                    "title": "Multiply along, add across",
                    "teach": (
                        "Two draws without replacement: follow a branch and multiply; "
                        "collect qualifying branches and add. Note the second stage's "
                        "fractions REMEMBER the first draw — the bag has changed."
                    ),
                    "config": {
                        "mode": "prob",
                        "caption": "Two draws from 5 red, 3 blue — no replacement",
                        "stages": [
                            {"name": "first draw", "options": [{"label": "R", "pLabel": "5/8", "p": 0.625}, {"label": "B", "pLabel": "3/8", "p": 0.375}]},
                            {"name": "second draw", "byPath": {
                                "R": [{"label": "R", "pLabel": "4/7", "p": 0.5714}, {"label": "B", "pLabel": "3/7", "p": 0.4286}],
                                "B": [{"label": "R", "pLabel": "5/7", "p": 0.7143}, {"label": "B", "pLabel": "2/7", "p": 0.2857}]
                            }},
                        ],
                    },
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Without replacement", "problemId": "ibsl-46-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Concept check",
                    "title": "Exclusive vs independent",
                    "prompt": "$A$ and $B$ are mutually exclusive with $P(A) = 0.3$, $P(B) = 0.4$. Then $P(A \\cap B) =$",
                    "options": ["$0$", "$0.12$", "$0.7$", "$0.1$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Exclusive means they CANNOT co-occur: the overlap is empty. "
                        "$0.12$ would be the INDEPENDENT answer — the two concepts are "
                        "opposites here, not synonyms."
                    ),
                    "check": ["Rational(3,10)*Rational(4,10) == Rational(12,100)"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Diagram choice in one line",
                    "body": (
                        "Categories overlapping? VENN (fill the overlap first). Events in "
                        "sequence? TREE (multiply along, add across). Two dice or spinners? "
                        "TABLE. The first mark of most 4.6 questions is just choosing and "
                        "starting the right diagram."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Union and independence check", "problemId": "ibsl-46-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Cards and conditions", "problemId": "ibsl-46-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.6 in four lines",
                    "points": [
                        "$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$; exclusive → overlap 0.",
                        "Venn: fill overlap first. Tree: multiply along, add across.",
                        "Without replacement: the second stage remembers the first.",
                        "Independent = the equation $P(A \\cap B) = P(A)P(B)$ checks out.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 7 — SL 4.7: Discrete random variables and E(X)
# ===========================================================================
def lesson_discrete_rv():
    return {
        "slug": "discrete-random-variables",
        "title": "Discrete Random Variables & Expected Value",
        "concreteComparison": (
            "A carnival game pays $\\$5$ a quarter of the time and takes $\\$2$ the rest: "
            "your average take is $\\$5 \\cdot \\frac{1}{4} - \\$2 \\cdot \\frac{3}{4} = "
            "-\\$0.25$ per play. That number — the probability-weighted average — is the "
            "expected value, and it prices every game of chance."
        ),
        "objective": (
            "Set up probability distributions for discrete random variables (probabilities "
            "sum to 1), find unknown parameters, compute $E(X)$, and judge fairness of "
            "games."
        ),
        "concept": [
            "**Syllabus card — SL 4.7.** Concept of discrete random variables and their "
            "probability distributions; expected value $E(X) = \\sum x \\, P(X = x)$ "
            "(IN the booklet); applications, including that $E(X) = 0$ means a FAIR game. "
            "**Papers 1 and 2** — the distribution-table question is one of the most "
            "reliable on the SL paper.",
            "A DISCRETE RANDOM VARIABLE attaches a number to each outcome of a chance "
            "process — the number of heads, the prize won, the total rolled. Its "
            "distribution is a table of values and probabilities, and the table's law is "
            "absolute: probabilities are non-negative and SUM TO 1. Half the exam "
            "questions hide a parameter ($k$) behind that law.",
            "The expected value $E(X) = \\sum x \\, P(X = x)$ weights each value by its "
            "chance — a long-run average per trial, not a value you expect on any single "
            "trial ($E(X) = 3$ can be impossible to roll). It is the distribution's "
            "balance point, exactly like the mean of data.",
            "Fairness: a game is FAIR when the expected GAIN is zero. Price a game by "
            "letting $X$ = net winnings (winnings minus stake, signs matter!) and "
            "computing $E(X)$: negative means the house wins on average. 'Find the stake "
            "that makes the game fair' = set $E(X) = 0$ and solve."
        ],
        "keyIdea": (
            "The table sums to 1 — that finds $k$. $E(X) = \\sum x P(x)$ — that prices "
            "the game. Fair means $E = 0$."
        ),
        "facts": [
            {
                "title": "Expected value",
                "latex": "E(X) = \\sum x \\, P(X = x)",
                "explanation": "IN the booklet (SL 4.7). Weighted average = balance point of the distribution.",
            },
            {
                "title": "The table's law",
                "latex": "\\sum P(X = x) = 1, \\qquad P(X = x) \\ge 0",
                "explanation": "Every distribution question leans on this — it's how hidden parameters are found.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-47-we1",
                "statement": (
                    "A discrete random variable $X$ has $P(X = x) = kx$ for $x = 1, 2, 3, "
                    "4$.  \n"
                    "**(a)** Find the value of $k$. **[2]**  \n"
                    "**(b)** Find $E(X)$. **[2]**  \n"
                    "**(c)** Find $P(X \\ge 3)$. **[1]**"
                ),
                "solution": (
                    "**(a)** $k + 2k + 3k + 4k = 10k = 1 \\Rightarrow k = \\frac{1}{10}$ "
                    "*(M1 A1)*.  \n"
                    "**(b)** $E(X) = 1 \\cdot \\frac{1}{10} + 2 \\cdot \\frac{2}{10} + 3 "
                    "\\cdot \\frac{3}{10} + 4 \\cdot \\frac{4}{10} = \\frac{30}{10} = 3$ "
                    "*(M1 A1)*.  \n"
                    "**(c)** $\\frac{3}{10} + \\frac{4}{10} = \\frac{7}{10}$ *(A1)*.  \n"
                    "**Narrative:** the sum-to-1 law finds $k$ in one line — the M1 is "
                    "writing that equation. $E(X) = 3$ sits toward the heavy end of the "
                    "table, as a balance point should."
                ),
                "check": [
                    "solve(10*k - 1, k) == [Rational(1, 10)]",
                    "Rational(1,10) + 2*Rational(2,10) + 3*Rational(3,10) + 4*Rational(4,10) == 3",
                    "Rational(3,10) + Rational(4,10) == Rational(7,10)",
                ],
            },
            {
                "id": "ibsl-47-we2",
                "statement": (
                    "A game costs $\\$3$ to play. A spinner pays $\\$10$ with probability "
                    "$0.2$, $\\$5$ with probability $0.3$, and nothing otherwise.  \n"
                    "**(a)** Letting $X$ be the NET winnings, complete the distribution of "
                    "$X$. **[2]**  \n"
                    "**(b)** Find $E(X)$ and interpret it. **[3]**"
                ),
                "solution": (
                    "**(a)** Net values: $10 - 3 = 7$ (p $= 0.2$); $5 - 3 = 2$ (p "
                    "$= 0.3$); $-3$ (p $= 0.5$) *(A1 A1)*.  \n"
                    "**(b)** $E(X) = 7(0.2) + 2(0.3) + (-3)(0.5) = 1.4 + 0.6 - 1.5 = 0.5$ "
                    "*(M1 A1)*. On average a player GAINS \\$0.50 per play — generous, and "
                    "unsustainable for the operator *(R1)*.  \n"
                    "**Narrative:** the whole difficulty is the bookkeeping — NET means "
                    "the stake comes off every branch, including the winning ones. Sign "
                    "errors here are the code's top mark-loser."
                ),
                "check": [
                    "Rational(2,10) + Rational(3,10) + Rational(5,10) == 1",
                    "7*Rational(2,10) + 2*Rational(3,10) - 3*Rational(5,10) == Rational(1,2)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Forgetting to subtract the stake when defining winnings.",
                "correction": "NET winnings = payout − stake, on every branch. A \\$10 payout on a \\$3 game is a $+\\$7$ value.",
                "authored": True,
            },
            {
                "text": "Expecting $E(X)$ to be an achievable value of $X$.",
                "correction": "It's a long-run average — $E = 3$ is fine even if $X$ can only be 1, 2 or 4.",
                "authored": True,
            },
            {
                "text": "Tables whose probabilities don't sum to 1 going unnoticed.",
                "correction": "Sum the row FIRST, always — it finds $k$, catches typos, and is usually a mark.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-47-t1",
                "statement": (
                    "$X$ takes values $0, 1, 2$ with $P(X = 0) = 0.3$ and $P(X = 1) = "
                    "0.5$. **Find** $P(X = 2)$ and $E(X)$. **[3]**"
                ),
                "solution": (
                    "$P(X = 2) = 1 - 0.8 = 0.2$ *(A1)*. $E(X) = 0(0.3) + 1(0.5) + 2(0.2) "
                    "= 0.9$ *(M1 A1)*."
                ),
                "check": [
                    "1 - Rational(8,10) == Rational(2,10)",
                    "Rational(5,10) + 2*Rational(2,10) == Rational(9,10)",
                ],
            },
            {
                "id": "ibsl-47-t2",
                "statement": (
                    "A raffle sells $200$ tickets at $\\$2$ each; one ticket wins $\\$150$. "
                    "**Find** the expected net winnings per ticket, and determine whether "
                    "the raffle is fair. **[4]**"
                ),
                "solution": (
                    "Net: win $148$ (p $= \\frac{1}{200}$), lose $2$ (p $= "
                    "\\frac{199}{200}$). $E(X) = \\frac{148 - 398}{200} = -\\frac{250}{200} "
                    "= -\\$1.25$ *(M1 A1 A1)*. Negative — not fair; the organizer keeps "
                    "\\$1.25 per ticket on average *(R1)*."
                ),
                "check": [
                    "148*Rational(1,200) - 2*Rational(199,200) == Rational(-5, 4)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.7 · Papers 1 & 2",
                    "title": "Numbers attached to chance",
                    "body": (
                        "A random variable turns outcomes into numbers; its table of "
                        "probabilities is the whole object. Two laws run the code: the "
                        "table sums to 1, and the weighted average $E(X)$ prices "
                        "everything from raffles to insurance."
                    ),
                },
                {
                    "kind": "distributionBars",
                    "eyebrow": "The balance point",
                    "title": "A distribution you can weigh",
                    "teach": (
                        "Each bar is a value with its probability; tap one for its "
                        "$x \\cdot P(x)$ contribution. The mean marker sits where the "
                        "bars balance — that point IS $E(X)$."
                    ),
                    "config": {"values": [1, 2, 3, 4], "probs": [0.1, 0.2, 0.3, 0.4], "pLabels": ["1/10", "2/10", "3/10", "4/10"], "xLabel": "x", "showMean": True},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Find k, then the mean", "problemId": "ibsl-47-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The table's law",
                    "title": "Hidden parameter",
                    "prompt": "$P(X = x) = \\dfrac{k}{x}$ for $x = 1, 2, 4$. Then $k =$",
                    "options": ["$\\dfrac{4}{7}$", "$\\dfrac{7}{4}$", "$\\dfrac{1}{3}$", "$\\dfrac{1}{7}$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$k + \\frac{k}{2} + \\frac{k}{4} = \\frac{7k}{4} = 1$, so "
                        "$k = \\frac{4}{7}$. The sum-to-1 law, as always."
                    ),
                    "check": ["solve(k + k/2 + k/4 - 1, k) == [Rational(4, 7)]"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Pricing a game", "problemId": "ibsl-47-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Fairness",
                    "title": "Make it fair",
                    "prompt": "A game pays $\\$6$ with probability $\\dfrac{1}{3}$, else nothing. The fair stake is:",
                    "options": ["$\\$2$", "$\\$3$", "$\\$6$", "$\\$1$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Fair means expected payout = stake: $6 \\cdot \\frac{1}{3} = 2$. "
                        "Stake \\$2 and the long-run exchange is even."
                    ),
                    "check": ["6*Rational(1,3) == 2"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Table first, always",
                    "body": (
                        "Write the full distribution table before computing anything — "
                        "values (net of stakes!) in one row, probabilities in the next, "
                        "sum checked to 1. Every later mark reads off it, and the "
                        "examiner can award follow-through from a visible table even "
                        "when arithmetic slips."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Complete the table", "problemId": "ibsl-47-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Price the raffle", "problemId": "ibsl-47-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.7 in four lines",
                    "points": [
                        "A distribution is a table: values + probabilities summing to 1.",
                        "Hidden $k$? The sum-to-1 equation finds it.",
                        "$E(X) = \\sum x P(x)$ — booklet; a long-run average, the balance point.",
                        "Games: $X$ = NET winnings; fair $\\iff E(X) = 0$.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 8 — SL 4.8: The binomial distribution
# ===========================================================================
def lesson_binomial_dist():
    return {
        "slug": "the-binomial-distribution",
        "title": "The Binomial Distribution",
        "concreteComparison": (
            "Guess all 8 answers on a 4-option quiz: how likely are exactly 3 right? Fixed "
            "number of tries, same chance each, only right/wrong — that's the binomial "
            "signature, and one formula (with your GDC's help) answers every 'how many "
            "successes' question."
        ),
        "objective": (
            "Recognize binomial situations, compute $P(X = k)$ and cumulative "
            "probabilities (GDC binompdf/binomcdf), and use $E(X) = np$, "
            "$\\mathrm{Var}(X) = np(1 - p)$."
        ),
        "concept": [
            "**Syllabus card — SL 4.8.** The binomial distribution: situations giving rise "
            "to it; mean $np$ and variance $np(1-p)$ (both IN the booklet); probabilities "
            "found using TECHNOLOGY. **Papers 1 and 2** — Paper 2 leans on binompdf/cdf; "
            "Paper 1 keeps the numbers exact-friendly.",
            "The binomial checklist (quote it when asked to justify): a FIXED number of "
            "trials $n$; each trial has TWO outcomes; the success probability $p$ is "
            "CONSTANT; trials are INDEPENDENT. Then $X \\sim B(n, p)$ counts successes, "
            "and $P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}$ — SL 1.9's binomial "
            "coefficients pricing the orderings.",
            "The GDC does the arithmetic: binompdf for EXACTLY $k$, binomcdf for AT MOST "
            "$k$. Translate inequalities before touching buttons: $P(X \\ge 3) = 1 - "
            "P(X \\le 2)$; $P(2 \\le X \\le 5) = P(X \\le 5) - P(X \\le 1)$. The "
            "translation line is the method mark.",
            "Mean and variance come free: $E(X) = np$ (expect $np$ successes — exactly "
            "the 'expected occurrences' of SL 4.5, now with a distribution around it) and "
            "$\\mathrm{Var}(X) = np(1 - p)$, tightest when $p$ nears 0 or 1."
        ],
        "keyIdea": (
            "Fixed $n$, two outcomes, constant $p$, independent — then $X \\sim B(n, p)$: "
            "pdf for 'exactly', cdf for 'at most', $1 -$ cdf for 'at least', mean $np$."
        ),
        "facts": [
            {
                "title": "Binomial probability",
                "latex": "P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}",
                "explanation": "The GDC computes it (binompdf); the structure is SL 1.9's coefficients × one path's probability.",
            },
            {
                "title": "Mean and variance",
                "latex": "E(X) = np, \\qquad \\mathrm{Var}(X) = np(1 - p)",
                "explanation": "Both IN the booklet (SL 4.8). sd $= \\sqrt{np(1-p)}$.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-48-we1",
                "statement": (
                    "$30\\%$ of seeds germinate. Ten seeds are planted; let $X$ be the "
                    "number that germinate.  \n"
                    "**(a)** State the distribution of $X$ and justify the binomial model. "
                    "**[2]**  \n"
                    "**(b)** Find $P(X = 3)$. **[2]**  \n"
                    "**(c)** **Write down** $E(X)$ and find $\\mathrm{Var}(X)$. **[2]**"
                ),
                "solution": (
                    "**(a)** $X \\sim B(10, 0.3)$: fixed $n = 10$, each seed germinates "
                    "or not with constant $p = 0.3$, independently *(A1 R1)*.  \n"
                    "**(b)** $P(X = 3) = \\binom{10}{3}(0.3)^3(0.7)^7 \\approx 0.267$ "
                    "*(M1 A1)*.  \n"
                    "**(c)** $E(X) = 10(0.3) = 3$; $\\mathrm{Var}(X) = 10(0.3)(0.7) = 2.1$ "
                    "*(A1 A1)*.  \n"
                    "**Narrative:** the justification in (a) is the checklist recited in "
                    "context — two lines, one mark, often skipped. The mode of this "
                    "distribution sits at 3, agreeing with $E(X)$: a sanity check the "
                    "bars make visible."
                ),
                "check": [
                    "binomial(10, 3) == 120",
                    "Abs(120*Rational(3,10)**3*Rational(7,10)**7 - 0.2668) < 0.001",
                    "10*Rational(3,10) == 3",
                    "10*Rational(3,10)*Rational(7,10) == Rational(21,10)",
                ],
            },
            {
                "id": "ibsl-48-we2",
                "statement": (
                    "A quiz has $8$ multiple-choice questions with $4$ options each; a "
                    "student guesses every answer.  \n"
                    "**(a)** Find the probability of exactly $2$ correct answers. **[2]**  \n"
                    "**(b)** Find the probability of AT LEAST one correct answer, exactly. "
                    "**[3]**"
                ),
                "solution": (
                    "**(a)** $X \\sim B(8, \\frac{1}{4})$: $P(X = 2) = \\binom{8}{2}"
                    "\\left(\\frac{1}{4}\\right)^2\\left(\\frac{3}{4}\\right)^6 = 28 \\cdot "
                    "\\frac{729}{65536} \\cdot \\frac{1}{16} \\approx 0.311$ *(M1 A1)*.  \n"
                    "**(b)** Complement: $P(X \\ge 1) = 1 - P(X = 0) = 1 - \\left("
                    "\\frac{3}{4}\\right)^8 = 1 - \\frac{6561}{65536} = \\frac{58975}"
                    "{65536} \\approx 0.900$ *(M1 A1 A1)*.  \n"
                    "**Narrative:** SL 4.5's complement shortcut, now inside a binomial: "
                    "'at least one' is ALWAYS $1 - P(0)$. The exact fraction earns "
                    "'exactly'; the decimal is the courtesy reading."
                ),
                "check": [
                    "binomial(8, 2)*Rational(1,4)**2*Rational(3,4)**6 == Rational(5103, 16384)",
                    "Abs(Rational(5103, 16384) - 0.3115) < 0.001",
                    "1 - Rational(3,4)**8 == Rational(58975, 65536)",
                    "Abs(Rational(58975, 65536) - 0.8999) < 0.001",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using binompdf for 'at least 3'.",
                "correction": "pdf is EXACTLY; 'at least 3' = $1 - P(X \\le 2)$ = 1 − binomcdf(n, p, 2). Translate first.",
                "authored": True,
            },
            {
                "text": "Off-by-one in the complement: $P(X \\ge 3) = 1 - P(X \\le 3)$.",
                "correction": "$1 - P(X \\le 2)$ — the boundary belongs to one side only. Write the translation line.",
                "authored": True,
            },
            {
                "text": "Applying the binomial where trials aren't independent (drawing without replacement).",
                "correction": "Without replacement changes $p$ each draw — that's SL 4.6's tree, not a binomial.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-48-t1",
                "statement": (
                    "$X \\sim B(20, 0.4)$. **Write down** $E(X)$, and find "
                    "$\\mathrm{Var}(X)$ and the standard deviation. **[3]**"
                ),
                "solution": (
                    "$E(X) = 8$ *(A1)*; $\\mathrm{Var} = 20(0.4)(0.6) = 4.8$ *(A1)*; "
                    "sd $= \\sqrt{4.8} \\approx 2.19$ *(A1)*."
                ),
                "check": [
                    "20*Rational(4,10) == 8",
                    "20*Rational(4,10)*Rational(6,10) == Rational(24,5)",
                    "Abs(sqrt(Rational(24,5)) - 2.191) < 0.001",
                ],
            },
            {
                "id": "ibsl-48-t2",
                "statement": (
                    "A fair coin is flipped $6$ times. **Find** the exact probability of "
                    "exactly $4$ heads. **[3]**"
                ),
                "solution": (
                    "$P(X = 4) = \\binom{6}{4}\\left(\\frac{1}{2}\\right)^6 = "
                    "\\frac{15}{64}$ *(M1 A1 A1)* — with $p = \\frac{1}{2}$, every path "
                    "weighs the same and only the count matters."
                ),
                "check": ["binomial(6,4)*Rational(1,2)**6 == Rational(15, 64)"],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.8 · Papers 1 & 2",
                    "title": "Counting successes",
                    "body": (
                        "Fixed tries, two outcomes, constant chance, independence — the "
                        "binomial signature. SL 1.9's coefficients count the orderings, "
                        "your GDC does the arithmetic, and the booklet hands you the mean "
                        "and variance."
                    ),
                },
                {
                    "kind": "binomialBars",
                    "eyebrow": "The whole distribution",
                    "title": "Steer n and p",
                    "teach": (
                        "Every bar is a possible success count with its probability — "
                        "tap one for its $\\binom{n}{k}p^k q^{n-k}$ reading. Step $p$ and "
                        "watch the hump slide to track $np$; step $n$ and watch it "
                        "spread."
                    ),
                    "config": {"n0": 10, "p0": 0.3, "nMax": 14, "showMuSigma": True, "highlightK": 3},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Seeds: justify, compute, summarize", "problemId": "ibsl-48-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Model recognition",
                    "title": "Binomial or not?",
                    "prompt": "Which situation is binomial?",
                    "options": [
                        "Counting sixes in 20 rolls of a fair die",
                        "Drawing 5 cards from a deck without replacement, counting hearts",
                        "Rolling a die until the first six appears",
                        "Measuring the heights of 20 students",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Fixed $n = 20$, success/failure, constant $p = \\frac{1}{6}$, "
                        "independent rolls ✓. Without replacement breaks constant $p$; "
                        "'until the first' has no fixed $n$; heights aren't counts."
                    ),
                    "check": ["20*Rational(1,6) == Rational(10,3)"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "The guessing student", "problemId": "ibsl-48-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "cdf translation",
                    "title": "Say it in cdf",
                    "prompt": "$X \\sim B(12, 0.35)$. $P(X \\ge 5)$ equals:",
                    "options": [
                        "$1 - P(X \\le 4)$",
                        "$1 - P(X \\le 5)$",
                        "$P(X \\le 5)$",
                        "$P(X = 5)$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "'At least 5' excludes 0–4 and nothing else: $1 - P(X \\le 4)$. "
                        "The boundary case decides between the top two options — write "
                        "the translation before the GDC."
                    ),
                    "check": ["12 - 5 == 7"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "GDC + markscheme",
                    "title": "The translation line",
                    "body": (
                        "Every binomial question: (1) state $X \\sim B(n, p)$; (2) write "
                        "the inequality translation ($P(X \\ge 3) = 1 - P(X \\le 2)$); "
                        "(3) then compute. Lines 1 and 2 are marks that survive any "
                        "keystroke slip — and 'justify the model' means recite the "
                        "checklist in context."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Mean, variance, sd", "problemId": "ibsl-48-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Fair-coin exact", "problemId": "ibsl-48-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.8 in four lines",
                    "points": [
                        "Checklist: fixed $n$, two outcomes, constant $p$, independent.",
                        "$P(X = k) = \\binom{n}{k}p^k(1-p)^{n-k}$; pdf = exactly, cdf = at most.",
                        "'At least' → $1 -$ cdf, boundary shifted by one. Translate in writing.",
                        "$E(X) = np$, $\\mathrm{Var} = np(1-p)$ — booklet.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 9 — SL 4.9: The normal distribution
# ===========================================================================
def lesson_normal():
    return {
        "slug": "the-normal-distribution",
        "title": "The Normal Distribution",
        "concreteComparison": (
            "Measure a thousand people's heights and the histogram melts into one shape: "
            "the bell. Most values crowd the mean, symmetric tails fade fast — and one "
            "curve, set by just $\\mu$ and $\\sigma$, answers every 'what fraction "
            "between…' question your GDC is asked."
        ),
        "objective": (
            "Use the normal curve's shape and symmetry, the 68–95–99.7 landmarks, and the "
            "GDC (normalcdf, invNorm) to find probabilities and boundary values."
        ),
        "concept": [
            "**Syllabus card — SL 4.9.** The normal distribution and curve: properties "
            "(bell shape, symmetry about $\\mu$, total area 1); diagrammatic "
            "representation; normal probabilities and INVERSE normal calculations by "
            "TECHNOLOGY (with $\\mu$ and $\\sigma$ known). **Mostly Paper 2** — the GDC "
            "does the integration; you do the setup and the sketch.",
            "$X \\sim N(\\mu, \\sigma^2)$: the curve peaks at $\\mu$ (mean = median = "
            "mode) and $\\sigma$ sets the width. Probability IS area under the curve, "
            "total 1 — so $P(X > \\mu) = 0.5$ by symmetry alone, and single points have "
            "probability zero ($P(X = a) = 0$; $<$ and $\\le$ agree).",
            "The landmark percentages: about $68\\%$ of values within $1\\sigma$ of "
            "$\\mu$, $95\\%$ within $2\\sigma$, $99.7\\%$ within $3\\sigma$. Exam "
            "questions quote these directly ('heights between 162 and 178') — recognize "
            "$\\mu \\pm k\\sigma$ before reaching for the GDC.",
            "Two GDC moves: NORMALCDF(lower, upper, $\\mu$, $\\sigma$) turns any interval "
            "into a probability; INVNORM(area, $\\mu$, $\\sigma$) runs backward from a "
            "percentile to the boundary value — watch that the area supplied is the LEFT "
            "tail ('top 10%' means area 0.9). Every answer deserves a two-second sketch "
            "with the region shaded: it catches tail errors before they cost marks."
        ],
        "keyIdea": (
            "Bell at $\\mu$, width $\\sigma$, area = probability. 68–95–99.7 for "
            "landmarks; normalcdf forward, invNorm backward — and always sketch the "
            "shaded region."
        ),
        "facts": [
            {
                "title": "The landmarks",
                "latex": "P(\\mu - \\sigma < X < \\mu + \\sigma) \\approx 0.68, \\quad \\pm 2\\sigma \\approx 0.95, \\quad \\pm 3\\sigma \\approx 0.997",
                "explanation": "Worth memorizing (not in the booklet) — many Paper 2 parts are these in costume.",
            },
            {
                "title": "The two GDC moves",
                "latex": "\\text{normalcdf: interval} \\to \\text{probability}, \\qquad \\text{invNorm: LEFT area} \\to \\text{value}",
                "explanation": "invNorm eats the left-tail area: top 10% ⇒ feed it 0.9.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-49-we1",
                "statement": (
                    "Heights are $X \\sim N(170, 8^2)$ cm.  \n"
                    "**(a)** **Write down** $P(X > 170)$. **[1]**  \n"
                    "**(b)** Find $P(162 < X < 178)$. **[2]**  \n"
                    "**(c)** Find $P(X > 186)$. **[2]**"
                ),
                "solution": (
                    "**(a)** $0.5$ — symmetry about the mean *(A1)*.  \n"
                    "**(b)** $162 = \\mu - \\sigma$ and $178 = \\mu + \\sigma$: the "
                    "$1\\sigma$ band, $\\approx 0.683$ *(M1 A1)*.  \n"
                    "**(c)** $186 = \\mu + 2\\sigma$: above two sigmas lies "
                    "$\\frac{1 - 0.954}{2} \\approx 0.0228$ *(M1 A1)*.  \n"
                    "**Narrative:** all three parts fall to symmetry and landmarks — no "
                    "GDC needed, though normalcdf confirms each. Spotting $\\mu \\pm "
                    "k\\sigma$ before computing is the skill being paid."
                ),
                "check": [
                    "170 - 8 == 162",
                    "170 + 8 == 178",
                    "Abs(erf(1/sqrt(2)) - 0.6827) < 0.001",
                    "Abs((1 - erf(2/sqrt(2)))/2 - 0.02275) < 0.0005",
                ],
            },
            {
                "id": "ibsl-49-we2",
                "statement": (
                    "Exam scores are $X \\sim N(500, 100^2)$. The top $10\\%$ of "
                    "candidates receive a distinction.  \n"
                    "**(a)** Sketch the situation, shading the distinction region. **[1]**  \n"
                    "**(b)** Find the minimum distinction score, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** Bell centred at 500; the right tail beyond an unknown "
                    "boundary shaded, labelled area $0.1$ *(A1)*.  \n"
                    "**(b)** invNorm needs the LEFT area: $1 - 0.1 = 0.9$ *(M1)*. "
                    "invNorm$(0.9, 500, 100) \\approx 628$ *(A1 A1)*.  \n"
                    "**Narrative:** the whole trap is the tail flip — feeding invNorm "
                    "$0.1$ returns $372$, the BOTTOM 10% boundary, and the sketch is what "
                    "catches it: 628 sits right of centre, as a top-decile score must."
                ),
                "check": [
                    "1 - Rational(1,10) == Rational(9,10)",
                    "Abs((1 + erf(1.28155/sqrt(2)))/2 - 0.9) < 0.0005",
                    "Abs(500 + 100*1.28155 - 628.2) < 0.1",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Feeding invNorm the right-tail area for 'top k%'.",
                "correction": "invNorm speaks LEFT areas: top 10% ⇒ 0.9. The sketch (is the answer the correct side of μ?) is the alarm.",
                "authored": True,
            },
            {
                "text": "Writing $N(170, 8)$ for sd $= 8$.",
                "correction": "The IB writes the VARIANCE second: $N(170, 8^2)$. Misread it and every number is wrong.",
                "authored": True,
            },
            {
                "text": "Treating $P(X \\ge a)$ and $P(X > a)$ as different.",
                "correction": "Continuous distributions give single points probability 0 — the two are equal.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-49-t1",
                "statement": (
                    "$X \\sim N(60, 5^2)$. Using landmarks only, **write down** "
                    "$P(55 < X < 65)$, $P(X < 50)$, and $P(X > 60)$. **[3]**"
                ),
                "solution": (
                    "$\\pm 1\\sigma$: $\\approx 0.68$ *(A1)*. Below $\\mu - 2\\sigma$: "
                    "$\\approx 0.025$ *(A1)*. Above the mean: $0.5$ *(A1)*."
                ),
                "check": [
                    "60 - 5 == 55",
                    "60 - 2*5 == 50",
                    "Abs((1 - erf(2/sqrt(2)))/2 - 0.02275) < 0.0005",
                ],
            },
            {
                "id": "ibsl-49-t2",
                "statement": (
                    "Battery lives are $N(120, 15^2)$ hours. A battery is returned if it "
                    "lasts under $90$ hours. **Find** the returned proportion, and "
                    "identify $90$ as $\\mu + k\\sigma$. **[3]**"
                ),
                "solution": (
                    "$90 = 120 - 2(15) = \\mu - 2\\sigma$ *(A1)*: the lower tail beyond "
                    "$2\\sigma$, $\\approx 0.0228$ — about $2.3\\%$ returned *(M1 A1)*."
                ),
                "check": [
                    "120 - 2*15 == 90",
                    "Abs((1 - erf(2/sqrt(2)))/2 - 0.02275) < 0.0005",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.9 · mostly Paper 2",
                    "title": "The shape nature keeps choosing",
                    "body": (
                        "Heights, masses, measurement errors — sums of many small "
                        "influences pile into the bell. Two numbers pin the whole curve: "
                        "$\\mu$ centres it, $\\sigma$ widths it, and area IS probability."
                    ),
                },
                {
                    "kind": "normalCurve",
                    "eyebrow": "The landmarks",
                    "title": "68 – 95 – 99.7, shaded live",
                    "teach": (
                        "Tap the bands: one sigma holds about 68% of everything, two "
                        "hold 95%, three hold virtually all. These landmarks answer half "
                        "of Paper 2's normal questions before the GDC wakes up."
                    ),
                    "config": {"mode": "empirical", "mu": 170, "sigma": 8, "xLabel": "height (cm)"},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Heights by landmarks", "problemId": "ibsl-49-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Symmetry",
                    "title": "No calculator required",
                    "prompt": "$X \\sim N(50, 4^2)$. $P(X < 42) \\approx$",
                    "options": ["$0.025$", "$0.16$", "$0.05$", "$0.475$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$42 = 50 - 2\\sigma$: below two sigmas lies half of the missing "
                        "5%, i.e. 2.5%. Landmark thinking, zero buttons."
                    ),
                    "check": ["50 - 2*4 == 42", "Abs((1 - erf(2/sqrt(2)))/2 - 0.02275) < 0.0005"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "invNorm and the tail flip", "problemId": "ibsl-49-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Inverse thinking",
                    "title": "Which area to feed?",
                    "prompt": "For the LOWEST 5% boundary of $N(\\mu, \\sigma^2)$, invNorm should be fed area:",
                    "options": ["$0.05$", "$0.95$", "$0.5$", "$0.45$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Lowest 5% IS a left area — feed 0.05 directly. (Top 5% would "
                        "need 0.95.) The sketch settles every such question."
                    ),
                    "check": ["1 - Rational(95,100) == Rational(5,100)"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Paper 2 wisdom",
                    "title": "Sketch, state, then press",
                    "body": (
                        "The unbreakable routine: draw the bell, mark $\\mu$, shade the "
                        "region, write the probability statement ($P(X > 186) = \\ldots$), "
                        "THEN compute. The sketch often carries a mark itself — and it "
                        "catches every tail flip before the examiner does. Notation "
                        "reminder: $N(\\mu, \\sigma^2)$ — variance in the bracket."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Landmarks only", "problemId": "ibsl-49-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Battery returns", "problemId": "ibsl-49-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.9 in four lines",
                    "points": [
                        "$N(\\mu, \\sigma^2)$ — variance written second; curve symmetric about $\\mu$.",
                        "Area = probability; total 1; $P(X = a) = 0$.",
                        "Landmarks: 68 / 95 / 99.7 within 1 / 2 / 3 sigmas.",
                        "normalcdf forward, invNorm backward (LEFT areas) — sketch first, always.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 10 — SL 4.10: The regression line of x on y
# ===========================================================================
def lesson_x_on_y():
    return {
        "slug": "the-x-on-y-regression-line",
        "title": "The Other Regression Line: x on y",
        "concreteComparison": (
            "You know a fossil's chemical decay reading and want its AGE — but your line "
            "was built to predict decay FROM age. Rearranging it is statistically wrong: "
            "predicting in the other direction needs the OTHER regression line, and the "
            "IB tests exactly this choice."
        ),
        "objective": (
            "Use the regression line of $x$ on $y$ for predicting $x$ from $y$; choose the "
            "correct line for each prediction direction; use the fact that both lines meet "
            "at the mean point."
        ),
        "concept": [
            "**Syllabus card — SL 4.10.** Equation of the regression line of $x$ on $y$ "
            "(by TECHNOLOGY); use of the equation for prediction purposes. **Mostly "
            "Paper 2**, nearly always as one pointed part: 'which line should be used, "
            "and why?'",
            "The $y$-on-$x$ line (SL 4.4) minimizes VERTICAL misses — errors in $y$ — so "
            "it's built for predicting $y$ from a known $x$. The $x$-on-$y$ line "
            "minimizes HORIZONTAL misses and is built for predicting $x$ from a known "
            "$y$. They are DIFFERENT lines (unless $|r| = 1$): rearranging one does not "
            "produce the other.",
            "The choice rule is one sentence: predict the variable you DON'T know using "
            "the line named '(unknown) on (known)'. Know $y$, want $x$? Use $x$ on $y$. "
            "The justification mark is the sentence 'because we are predicting $x$ from "
            "a known $y$'.",
            "Both lines pass through the mean point $(\\bar{x}, \\bar{y})$ — so they "
            "intersect exactly there. Exam use: given both equations, solving them "
            "simultaneously recovers $\\bar{x}$ and $\\bar{y}$ — a favorite Paper 1 "
            "adaptation of a calculator topic. And all the SL 4.4 etiquette (strong "
            "$|r|$, interpolation only) applies unchanged."
        ],
        "keyIdea": (
            "Two lines, two jobs: $y$-on-$x$ predicts $y$; $x$-on-$y$ predicts $x$. "
            "Never rearrange one into the other — and both cross at $(\\bar{x}, "
            "\\bar{y})$."
        ),
        "facts": [
            {
                "title": "The choice rule",
                "latex": "\\text{predict } y \\text{ from } x: \; y \\text{ on } x, \\qquad \\text{predict } x \\text{ from } y: \; x \\text{ on } y",
                "explanation": "The '(unknown) on (known)' naming carries the whole decision. Justify in one sentence.",
            },
            {
                "title": "Where the lines meet",
                "latex": "\\text{both regression lines pass through } (\\bar{x}, \\bar{y})",
                "explanation": "Solve the two equations simultaneously to recover the means.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-410-we1",
                "statement": (
                    "For a dataset, the GDC gives the regression lines $y = 1.8x + 4$ "
                    "($y$ on $x$) and $x = 0.5y - 1$ ($x$ on $y$).  \n"
                    "**(a)** A new case has $x = 10$. Predict its $y$-value, justifying "
                    "your choice of line. **[2]**  \n"
                    "**(b)** A new case has $y = 30$. Predict its $x$-value. **[2]**"
                ),
                "solution": (
                    "**(a)** Predicting $y$ from known $x$: use $y$ on $x$ *(R1)*: "
                    "$y = 1.8(10) + 4 = 22$ *(A1)*.  \n"
                    "**(b)** Predicting $x$ from known $y$: use $x$ on $y$: "
                    "$x = 0.5(30) - 1 = 14$ *(M1 A1)*.  \n"
                    "**Narrative:** notice what we did NOT do — rearrange $y = 1.8x + 4$ "
                    "into $x = \\frac{y - 4}{1.8} \\approx 14.4$. Close, but wrong line, "
                    "wrong method, no marks for the rearrangement route."
                ),
                "check": [
                    "Rational(18,10)*10 + 4 == 22",
                    "Rational(1,2)*30 - 1 == 14",
                ],
            },
            {
                "id": "ibsl-410-we2",
                "statement": (
                    "Using the same two lines, find $\\bar{x}$ and $\\bar{y}$. **[3]**"
                ),
                "solution": (
                    "Both lines pass through the mean point, so solve simultaneously "
                    "*(M1 — the property is the method)*: substitute $y = 1.8x + 4$ into "
                    "$x = 0.5y - 1$: $x = 0.5(1.8x + 4) - 1 = 0.9x + 1$, so $0.1x = 1$, "
                    "$\\bar{x} = 10$ *(A1)*; then $\\bar{y} = 1.8(10) + 4 = 22$ *(A1)*.  \n"
                    "**Narrative:** the intersection of the two regression lines IS the "
                    "mean point — the one place they must agree. (Consistency check: "
                    "part (a)'s prediction at $x = 10$ returned exactly $\\bar{y}$, as "
                    "it must at the mean.)"
                ),
                "check": [
                    "solve(Eq(x, Rational(1,2)*(Rational(18,10)*x + 4) - 1), x) == [10]",
                    "Rational(18,10)*10 + 4 == 22",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Rearranging the $y$-on-$x$ line to predict $x$.",
                "correction": "The rearranged line minimizes the WRONG errors. Predicting $x$ needs the $x$-on-$y$ line, full stop.",
                "authored": True,
            },
            {
                "text": "Expecting the two lines to be the same equation.",
                "correction": "They coincide only when $|r| = 1$. Otherwise: two lines, one intersection — the mean point.",
                "authored": True,
            },
            {
                "text": "Skipping the justification sentence when the question says 'which line'.",
                "correction": "'Because we predict $x$ from a known $y$' — the R-mark is that clause.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-410-t1",
                "statement": (
                    "Lines: $y = 3x + 2$ ($y$ on $x$) and $x = 0.3y + 1$ ($x$ on $y$). "
                    "**Predict** $x$ when $y = 20$, and state why that line. **[2]**"
                ),
                "solution": (
                    "$x = 0.3(20) + 1 = 7$ *(A1)* — the $x$-on-$y$ line, because $x$ is "
                    "being predicted from a known $y$ *(R1)*."
                ),
                "check": ["Rational(3,10)*20 + 1 == 7"],
            },
            {
                "id": "ibsl-410-t2",
                "statement": (
                    "Lines $y = 2x + 3$ and $x = 0.4y - 1$ describe one dataset. **Find** "
                    "the mean point. **[3]**"
                ),
                "solution": (
                    "$x = 0.4(2x + 3) - 1 = 0.8x + 0.2 \\Rightarrow 0.2x = 0.2 "
                    "\\Rightarrow \\bar{x} = 1$ *(M1 A1)*; $\\bar{y} = 2(1) + 3 = 5$ "
                    "*(A1)*. Mean point $(1, 5)$."
                ),
                "check": [
                    "solve(Eq(x, Rational(4,10)*(2*x + 3) - 1), x) == [1]",
                    "2*1 + 3 == 5",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.10 · mostly Paper 2",
                    "title": "Two spines, two directions",
                    "body": (
                        "SL 4.4's line predicted $y$; this code adds its twin for "
                        "predicting $x$. One rule (unknown-on-known), one property (both "
                        "meet at the mean point), one trap (never rearrange). Short "
                        "code, reliable marks."
                    ),
                },
                {
                    "kind": "scatterPlot",
                    "eyebrow": "Vertical vs horizontal misses",
                    "title": "What each line minimizes",
                    "teach": (
                        "The fit game scores VERTICAL misses — that's the $y$-on-$x$ "
                        "objective. The $x$-on-$y$ line plays the same game sideways, "
                        "minimizing horizontal misses. Different objectives, different "
                        "winning lines."
                    ),
                    "config": {"mode": "fit", "xLabel": "x", "yLabel": "y", "m0": 1.5, "b0": 8},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Choose, justify, predict", "problemId": "ibsl-410-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The choice rule",
                    "title": "Which line?",
                    "prompt": "Shoe size ($s$) and height ($h$) are recorded. To estimate the SHOE SIZE of someone $185$ cm tall, use:",
                    "options": [
                        "The $s$-on-$h$ regression line",
                        "The $h$-on-$s$ regression line",
                        "Either, rearranged as needed",
                        "The line through the two extreme points",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Unknown on known: shoe size is predicted from known height, so "
                        "$s$ on $h$. Rearranging the other line is the tested trap."
                    ),
                    "check": ["1 == 1"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Recover the means", "problemId": "ibsl-410-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The meeting point",
                    "title": "Where they agree",
                    "prompt": "The two regression lines of a dataset intersect at:",
                    "options": [
                        "$(\\bar{x}, \\bar{y})$",
                        "The origin",
                        "They never intersect",
                        "The strongest data point",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Both must pass through the mean point, so that's their (only) "
                        "meeting place — and solving them simultaneously recovers it."
                    ),
                    "check": ["1 == 1"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "One sentence earns the mark",
                    "body": (
                        "Whenever two lines are on offer, write the choice sentence "
                        "before substituting: 'predicting $x$ from known $y$ ⇒ use the "
                        "$x$-on-$y$ line'. It's the R-mark, and it inoculates against "
                        "the rearrangement reflex. All SL 4.4 warnings (extrapolation, "
                        "weak $r$) still apply."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Pick and predict", "problemId": "ibsl-410-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Intersect for the means", "problemId": "ibsl-410-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.10 in four lines",
                    "points": [
                        "$x$-on-$y$ predicts $x$ from known $y$ — its own line, from the GDC.",
                        "Never rearrange the other line; they differ unless $|r| = 1$.",
                        "Both pass through $(\\bar{x}, \\bar{y})$ — intersect to recover the means.",
                        "Justify the choice in one written sentence.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 11 — SL 4.11: Formal conditional probability and independence
# ===========================================================================
def lesson_formal_conditional():
    return {
        "slug": "conditional-probability-and-independence",
        "title": "Conditional Probability, Formally",
        "concreteComparison": (
            "A test for a rare condition is '99% accurate' — yet most positive results "
            "are false alarms. The resolution is conditional probability done FORMALLY: "
            "$P(\\text{condition} \\mid \\text{positive})$ is not "
            "$P(\\text{positive} \\mid \\text{condition})$, and the formula keeps them "
            "straight."
        ),
        "objective": (
            "Use $P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$ formally; test independence "
            "three equivalent ways; work from tables, Venn diagrams and given "
            "probabilities."
        ),
        "concept": [
            "**Syllabus card — SL 4.11.** Formal definition of conditional probability "
            "$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$ (IN the booklet); formal "
            "definition of independence: $P(A \\mid B) = P(A \\mid B') = P(A)$; testing "
            "for independence. **Papers 1 and 2** — SL 4.6's ideas, now wielded as "
            "algebra on given probabilities.",
            "The formula is the shrink-the-world idea made computable: given that $B$ "
            "happened, the relevant universe is $B$, and $A$'s share of it is "
            "$\\frac{P(A \\cap B)}{P(B)}$. Rearranged, it CHAINS: $P(A \\cap B) = "
            "P(B) \\, P(A \\mid B)$ — exactly what tree branches multiply.",
            "Direction matters absolutely: $P(A \\mid B) \\ne P(B \\mid A)$ in general — "
            "they share a numerator but divide by different worlds. Reading 'given' "
            "correctly (which event shrank the world?) is half the marks in this code.",
            "Independence now has THREE equivalent tests, any one sufficient: "
            "$P(A \\cap B) = P(A)P(B)$; $P(A \\mid B) = P(A)$; $P(A \\mid B') = P(A)$. "
            "The exam's standard demand: compute both sides of one test from a table or "
            "Venn, compare, and CONCLUDE in a sentence ('not equal, so not "
            "independent')."
        ],
        "keyIdea": (
            "$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$: $B$ is the new world. "
            "Independence = conditioning changes nothing — test it, don't assume it."
        ),
        "facts": [
            {
                "title": "Conditional probability",
                "latex": "P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}",
                "explanation": "IN the booklet (SL 4.11). Rearranged: $P(A \\cap B) = P(B)P(A \\mid B)$ — the tree's multiplication rule.",
            },
            {
                "title": "Independence, three ways",
                "latex": "P(A \\cap B) = P(A)P(B) \\iff P(A \\mid B) = P(A) \\iff P(A \\mid B') = P(A)",
                "explanation": "Any one test settles it. Compute both sides, compare, conclude in words.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-411-we1",
                "statement": (
                    "$P(A) = 0.5$, $P(B) = 0.4$ and $P(A \\cap B) = 0.2$.  \n"
                    "**(a)** Find $P(A \\mid B)$ and $P(B \\mid A)$. **[3]**  \n"
                    "**(b)** Determine, with justification, whether $A$ and $B$ are "
                    "independent. **[2]**"
                ),
                "solution": (
                    "**(a)** $P(A \\mid B) = \\frac{0.2}{0.4} = 0.5$; $P(B \\mid A) = "
                    "\\frac{0.2}{0.5} = 0.4$ *(M1 A1 A1)* — same numerator, different "
                    "worlds, different answers.  \n"
                    "**(b)** $P(A \\mid B) = 0.5 = P(A)$ — knowing $B$ changed nothing, "
                    "so independent ✓ *(M1 R1)*. (Equivalently $P(A)P(B) = 0.2 = "
                    "P(A \\cap B)$.)  \n"
                    "**Narrative:** (a) is the direction lesson in miniature. The "
                    "conclusion sentence in (b) — comparison plus verdict — is where "
                    "the R-mark lives."
                ),
                "check": [
                    "Rational(2,10)/Rational(4,10) == Rational(1,2)",
                    "Rational(2,10)/Rational(5,10) == Rational(2,5)",
                    "Rational(5,10)*Rational(4,10) == Rational(2,10)",
                ],
            },
            {
                "id": "ibsl-411-we2",
                "statement": (
                    "$100$ students by gender and sport: $30$ male students play sport "
                    "and $20$ do not; $25$ female students play and $25$ do not.  \n"
                    "**(a)** Find $P(\\text{plays} \\mid \\text{male})$ and "
                    "$P(\\text{plays})$. **[3]**  \n"
                    "**(b)** Hence determine whether playing sport is independent of "
                    "gender. **[2]**"
                ),
                "solution": (
                    "**(a)** Male world: $50$ students, $30$ play: $P(\\text{plays} "
                    "\\mid \\text{male}) = 0.6$ *(A1)*. Whole school: $\\frac{55}{100} "
                    "= 0.55$ *(A1 A1)*.  \n"
                    "**(b)** $0.6 \\ne 0.55$: conditioning on gender CHANGES the "
                    "probability, so NOT independent *(M1 R1)*.  \n"
                    "**Narrative:** two-way tables make conditionals into row-reading — "
                    "the denominator is the row total, not the grand total. 'Hence' "
                    "insists you compare exactly the two numbers from (a)."
                ),
                "check": [
                    "Rational(30, 50) == Rational(3, 5)",
                    "Rational(30 + 25, 100) == Rational(11, 20)",
                    "Rational(3,5) != Rational(11,20)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Swapping the direction: computing $P(B \\mid A)$ when 'given B' was stated.",
                "correction": "'Given' names the SHRUNKEN WORLD — it goes in the denominator. Re-read before dividing.",
                "authored": True,
            },
            {
                "text": "Dividing by the grand total in a table conditional.",
                "correction": "Condition on a row ⇒ divide by the ROW total. The world shrank; so must the denominator.",
                "authored": True,
            },
            {
                "text": "Concluding 'independent' without computing both sides.",
                "correction": "Independence is a checked EQUATION plus a sentence: 'LHS = RHS, hence independent'. Numbers first, verdict second.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-411-t1",
                "statement": (
                    "$P(A \\cap B) = 0.12$ and $P(B) = 0.3$. **Find** $P(A \\mid B)$. "
                    "Given also $P(A) = 0.4$, test independence. **[3]**"
                ),
                "solution": (
                    "$P(A \\mid B) = \\frac{0.12}{0.3} = 0.4$ *(M1 A1)*. Equal to "
                    "$P(A)$ — independent ✓ *(R1)*."
                ),
                "check": [
                    "Rational(12,100)/Rational(3,10) == Rational(2,5)",
                    "Rational(2,5) == Rational(4,10)",
                ],
            },
            {
                "id": "ibsl-411-t2",
                "statement": (
                    "Events with $P(A) = 0.6$, $P(A \\mid B) = 0.75$, $P(B) = 0.4$. "
                    "**Find** $P(A \\cap B)$ and $P(A \\cup B)$. **[4]**"
                ),
                "solution": (
                    "Chain rule: $P(A \\cap B) = P(B)P(A \\mid B) = 0.4 \\times 0.75 = "
                    "0.3$ *(M1 A1)*. Union: $0.6 + 0.4 - 0.3 = 0.7$ *(M1 A1)*. (And "
                    "$0.75 \\ne 0.6$: not independent.)"
                ),
                "check": [
                    "Rational(4,10)*Rational(3,4) == Rational(3,10)",
                    "Rational(6,10) + Rational(4,10) - Rational(3,10) == Rational(7,10)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.11 · Papers 1 & 2",
                    "title": "The formula behind the shrinking world",
                    "body": (
                        "SL 4.6 read conditionals off diagrams; this code computes them "
                        "from probabilities alone. One booklet formula, a direction "
                        "discipline, and three equivalent independence tests."
                    ),
                },
                {
                    "kind": "vennCounts",
                    "eyebrow": "The shrunken world",
                    "title": "Condition = new denominator",
                    "teach": (
                        "Tap region B: given B, only its 14 members exist, and A's "
                        "share is the overlap's 8 of those 14. That fraction IS "
                        "$\\frac{P(A \\cap B)}{P(B)}$ — the formula is the picture."
                    ),
                    "config": {"mode": "regions", "labelA": "A", "labelB": "B", "onlyA": 10, "onlyB": 6, "both": 8},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Both directions, then the test", "problemId": "ibsl-411-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Direction discipline",
                    "title": "Which world shrank?",
                    "prompt": "$P(A \\cap B) = 0.1$, $P(A) = 0.25$, $P(B) = 0.5$. Then $P(B \\mid A) =$",
                    "options": ["$0.4$", "$0.2$", "$0.1$", "$0.5$"],
                    "correctIndex": 0,
                    "explanation": (
                        "'Given A': divide by $P(A)$: $\\frac{0.1}{0.25} = 0.4$. "
                        "Option B divided by $P(B)$ — the other direction, the classic "
                        "swap."
                    ),
                    "check": ["Rational(1,10)/Rational(1,4) == Rational(2,5)"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "A table, tested", "problemId": "ibsl-411-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Chain rule",
                    "title": "Multiply back",
                    "prompt": "$P(B) = 0.6$ and $P(A \\mid B) = 0.35$. Then $P(A \\cap B) =$",
                    "options": ["$0.21$", "$0.95$", "$0.583$", "$0.35$"],
                    "correctIndex": 0,
                    "explanation": (
                        "The rearranged definition: $P(A \\cap B) = P(B)P(A \\mid B) = "
                        "0.21$ — exactly what a tree branch multiplies."
                    ),
                    "check": ["Rational(6,10)*Rational(35,100) == Rational(21,100)"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Markscheme wisdom",
                    "title": "Compute, compare, conclude",
                    "body": (
                        "Independence answers have a fixed three-beat: both sides "
                        "computed, an explicit comparison ('$0.6 \\ne 0.55$'), and the "
                        "verdict sentence. Any beat missing drops a mark. And when "
                        "'given' appears, underline which event it names before "
                        "dividing anything."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Divide, then test", "problemId": "ibsl-411-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Chain to the union", "problemId": "ibsl-411-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.11 in four lines",
                    "points": [
                        "$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$ — booklet; 'given' names the denominator.",
                        "$P(A \\mid B) \\ne P(B \\mid A)$: same numerator, different worlds.",
                        "Chain: $P(A \\cap B) = P(B)P(A \\mid B)$ — trees, formalized.",
                        "Independence: one test, both sides shown, verdict in words.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 12 — SL 4.12: Standardization and z-values
# ===========================================================================
def lesson_z_values():
    return {
        "slug": "z-values-and-standardization",
        "title": "z-Values & Standardization",
        "concreteComparison": (
            "An 82 in a hard test can beat a 90 in an easy one. Convert both to "
            "'sigmas above the mean' — $z = 1$ versus $z = 1.2$ — and scores from "
            "different worlds become comparable. That conversion also unlocks normal "
            "problems where $\\mu$ or $\\sigma$ is the unknown."
        ),
        "objective": (
            "Standardize with $z = \\frac{x - \\mu}{\\sigma}$; compare values across "
            "distributions; and find unknown means or standard deviations from given "
            "normal probabilities via inverse-normal $z$-values."
        ),
        "concept": [
            "**Syllabus card — SL 4.12.** Standardization of normal variables "
            "($z$-values); the standard normal $Z \\sim N(0, 1)$; inverse normal "
            "calculations where MEAN OR STANDARD DEVIATION IS UNKNOWN. The formula "
            "$z = \\frac{x - \\mu}{\\sigma}$ is IN the booklet. **Paper 2's favorite "
            "hard normal question** — SL 4.9 with the unknowns moved.",
            "$z$ counts sigmas from the mean, signed: $z = 1.5$ means one-and-a-half "
            "sigmas above; $z = -2$ means two below. Standardizing maps ANY normal "
            "onto $Z \\sim N(0, 1)$, which is what makes cross-distribution comparison "
            "honest — compare $z$'s, not raw scores.",
            "The unknown-parameter recipe: (1) translate the given probability into a "
            "$z$-value with invNorm on $N(0,1)$ — e.g. $P(X < 80) = 0.9$ gives "
            "$z = 1.2816$; (2) write the standardization equation $\\frac{80 - \\mu}"
            "{\\sigma} = 1.2816$; (3) solve for the unknown. Two unknowns? Two given "
            "probabilities, two equations, simultaneous solve.",
            "Sign discipline: probabilities BELOW $0.5$ produce NEGATIVE $z$-values — "
            "$P(X < 62) = 0.1$ means 62 sits below the mean, $z = -1.2816$. The sketch "
            "(is the boundary left or right of $\\mu$?) is the sign's guardian, exactly "
            "as in SL 4.9."
        ],
        "keyIdea": (
            "$z = \\frac{x - \\mu}{\\sigma}$ measures position in sigmas. Known "
            "probability → invNorm $z$ → standardization equation → solve for the "
            "unknown $\\mu$ or $\\sigma$."
        ),
        "facts": [
            {
                "title": "Standardization",
                "latex": "z = \\frac{x - \\mu}{\\sigma}, \\qquad Z \\sim N(0, 1)",
                "explanation": "IN the booklet (SL 4.12). Sigmas above (+) or below (−) the mean.",
            },
        ],
        "workedExamples": [
            {
                "id": "ibsl-412-we1",
                "statement": (
                    "Amina scores $82$ in Mathematics ($\\mu = 74$, $\\sigma = 8$) and "
                    "$90$ in English ($\\mu = 84$, $\\sigma = 5$).  \n"
                    "**(a)** Find her $z$-score in each subject. **[3]**  \n"
                    "**(b)** In which subject was her performance relatively better? "
                    "Justify. **[1]**"
                ),
                "solution": (
                    "**(a)** Maths: $z = \\frac{82 - 74}{8} = 1$; English: $z = "
                    "\\frac{90 - 84}{5} = 1.2$ *(M1 A1 A1)*.  \n"
                    "**(b)** English: $1.2 > 1$ — she sits further above the cohort's "
                    "mean there *(R1)*.  \n"
                    "**Narrative:** raw scores said Maths (82 < 90 anyway); sigma "
                    "distances say English, and sigma distances are the honest "
                    "comparison. The justification mark wants the comparison stated in "
                    "$z$'s."
                ),
                "check": [
                    "Rational(82 - 74, 8) == 1",
                    "Rational(90 - 84, 5) == Rational(6, 5)",
                    "Rational(6,5) > 1",
                ],
            },
            {
                "id": "ibsl-412-we2",
                "statement": (
                    "$X \\sim N(\\mu, 10^2)$ and $P(X < 80) = 0.9$.  \n"
                    "**(a)** **Write down** the $z$-value for which $P(Z < z) = 0.9$. "
                    "**[1]**  \n"
                    "**(b)** Hence find $\\mu$, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** $z = 1.28$ (invNorm$(0.9)$ $\\approx 1.2816$) *(A1)*.  \n"
                    "**(b)** Standardize: $\\dfrac{80 - \\mu}{10} = 1.2816$ *(M1)*, so "
                    "$\\mu = 80 - 12.816 \\approx 67.2$ *(A1 A1)*.  \n"
                    "**Narrative:** the whole method is 'probability → $z$ → equation'. "
                    "Sanity: $P(X < 80)$ is HIGH, so 80 sits well above the mean — and "
                    "indeed $67.2 < 80$ ✓. A sketch makes that check automatic."
                ),
                "check": [
                    "Abs((1 + erf(1.2816/sqrt(2)))/2 - 0.9) < 0.0005",
                    "Abs(80 - 10*1.2816 - 67.18) < 0.05",
                    "67.2 < 80",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Dropping the sign: using $z = +1.28$ for $P(X < 62) = 0.1$.",
                "correction": "Left-tail areas below 0.5 mean the boundary is BELOW the mean: $z = -1.28$. Sketch first.",
                "authored": True,
            },
            {
                "text": "Comparing raw scores across different tests.",
                "correction": "Different $\\mu$ and $\\sigma$ make raw scores incomparable — convert to $z$ and compare sigmas.",
                "authored": True,
            },
            {
                "text": "In two-unknown problems, mixing up which $z$ pairs with which $x$.",
                "correction": "One equation per given probability, each with ITS boundary and ITS $z$ — label them before solving.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "ibsl-412-t1",
                "statement": (
                    "$X \\sim N(75, 8^2)$. **Find** the $z$-value of $x = 85$, and of "
                    "$x = 63$. **[2]**"
                ),
                "solution": (
                    "$z = \\frac{85 - 75}{8} = 1.25$; $z = \\frac{63 - 75}{8} = -1.5$ "
                    "*(A1 A1)* — one and a quarter sigmas above; one and a half below."
                ),
                "check": ["Rational(85 - 75, 8) == Rational(5, 4)", "Rational(63 - 75, 8) == Rational(-3, 2)"],
            },
            {
                "id": "ibsl-412-t2",
                "statement": (
                    "$X \\sim N(70, \\sigma^2)$ and $P(X < 62) = 0.1$. Given "
                    "invNorm$(0.1) \\approx -1.2816$, **find** $\\sigma$ to 3 s.f. "
                    "**[3]**"
                ),
                "solution": (
                    "$\\dfrac{62 - 70}{\\sigma} = -1.2816$ *(M1)*: $\\sigma = "
                    "\\dfrac{-8}{-1.2816} \\approx 6.24$ *(A1 A1)*. The negatives "
                    "cancel — as they must, since $\\sigma > 0$."
                ),
                "check": [
                    "Abs(8/1.2816 - 6.242) < 0.005",
                    "Abs((1 + erf(-1.2816/sqrt(2)))/2 - 0.1) < 0.0005",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "SL 4.12 · the capstone",
                    "title": "Position, measured in sigmas",
                    "body": (
                        "The last code of Topic 4 turns every normal into the same "
                        "standard one. $z$-scores compare across worlds and — the exam's "
                        "favorite — let you solve BACKWARD for an unknown mean or sigma."
                    ),
                },
                {
                    "kind": "normalCurve",
                    "eyebrow": "Walk the axis",
                    "title": "x and its z, side by side",
                    "teach": (
                        "Step $x$ along the axis and read $z = \\frac{x - \\mu}{\\sigma}$ "
                        "update live — distance from the mean, measured in sigmas, sign "
                        "and all. This one number is the whole idea."
                    ),
                    "config": {"mode": "zscore", "mu": 74, "sigma": 8, "x0": 82, "xLabel": "score"},
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Two tests, one honest comparison", "problemId": "ibsl-412-we1"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "z fluency",
                    "title": "Sigmas, signed",
                    "prompt": "$X \\sim N(40, 6^2)$. The value $x = 31$ has $z =$",
                    "options": ["$-1.5$", "$1.5$", "$-9$", "$-0.67$"],
                    "correctIndex": 0,
                    "explanation": (
                        "$z = \\frac{31 - 40}{6} = -1.5$: below the mean, so negative. "
                        "Option C forgot to divide by $\\sigma$."
                    ),
                    "check": ["Rational(31 - 40, 6) == Rational(-3, 2)"],
                },
                {"kind": "worked", "eyebrow": "Exam format", "title": "Unknown mean, recovered", "problemId": "ibsl-412-we2"},
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Sign discipline",
                    "title": "Which z?",
                    "prompt": "$P(X < a) = 0.2$ for a normal $X$. The corresponding $z$-value is:",
                    "options": ["Negative", "Positive", "Zero", "Cannot tell"],
                    "correctIndex": 0,
                    "explanation": (
                        "A left area below one-half puts $a$ below the mean — negative "
                        "$z$ (about $-0.842$). The sketch shows it instantly."
                    ),
                    "check": ["Rational(2,10) < Rational(1,2)"],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Paper 2 wisdom",
                    "title": "The backward recipe",
                    "body": (
                        "Unknown $\\mu$ or $\\sigma$: (1) sketch; (2) invNorm the given "
                        "probability into a $z$ (mind the sign); (3) write $\\frac{x - "
                        "\\mu}{\\sigma} = z$; (4) solve. Two unknowns need two given "
                        "probabilities and a simultaneous solve — label each equation "
                        "with its boundary."
                    ),
                },
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Above and below", "problemId": "ibsl-412-t1"},
                {"kind": "tryIt", "eyebrow": "Your turn", "title": "Unknown sigma", "problemId": "ibsl-412-t2"},
                {
                    "kind": "recap",
                    "title": "SL 4.12 in four lines",
                    "points": [
                        "$z = \\frac{x - \\mu}{\\sigma}$ — booklet; sigmas above (+) or below (−).",
                        "Compare performances via $z$, never via raw scores.",
                        "Unknown parameter: probability → invNorm $z$ → equation → solve.",
                        "Left areas under 0.5 ⇒ negative $z$ — the sketch guards the sign.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Unit practice bank — 2 per subtopic, tagged ib-aa-sl-4.x
# ===========================================================================
def practice_bank():
    return [
        {
            "id": "ibsl-sp-p01",
            "statement": "A school has $500$ juniors and $300$ seniors. A stratified sample of $40$ is taken. **Find** the number from each year. **[2]**",
            "solution": "Fraction $\\frac{40}{800} = \\frac{1}{20}$: juniors $25$, seniors $15$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.1", "mono": True}, {"text": "P2"}],
            "check": ["Rational(40,800)*500 == 25", "Rational(40,800)*300 == 15"],
        },
        {
            "id": "ibsl-sp-p02",
            "statement": "A shop surveys every $25$th customer from a random start. **Name** the technique and give one condition for it to be unbiased. **[2]**",
            "solution": "Systematic sampling *(A1)*; unbiased provided the customer stream has no pattern with period 25 *(R1)*.",
            "badges": [{"text": "ib-aa-sl-4.1", "mono": True}, {"text": "P2"}],
            "check": ["25*4 == 100"],
        },
        {
            "id": "ibsl-sp-p03",
            "statement": "A dataset has $Q_1 = 15$, $Q_3 = 27$. **Find** the outlier fences, and test the value $44$. **[3]**",
            "solution": "IQR $12$; fences $-3$ and $45$ *(M1 A1)*. $44 < 45$: not an outlier *(R1)*.",
            "badges": [{"text": "ib-aa-sl-4.2", "mono": True}, {"text": "P1"}],
            "check": ["27 + Rational(3,2)*12 == 45", "44 < 45", "15 - Rational(3,2)*12 == -3"],
        },
        {
            "id": "ibsl-sp-p04",
            "statement": "A cumulative frequency graph shows $60$ plants' heights. **Write down** the cumulative counts at which the median, $Q_1$ and $Q_3$ are read. **[2]**",
            "solution": "Median at $30$; $Q_1$ at $15$; $Q_3$ at $45$ *(A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.2", "mono": True}, {"text": "P2"}],
            "check": ["Rational(60,2) == 30", "Rational(60,4) == 15", "Rational(3*60,4) == 45"],
        },
        {
            "id": "ibsl-sp-p05",
            "statement": "For the data $1, 3, 5, 5, 6$: **find** the mean, median, mode and population variance. **[4]**",
            "solution": (
                "Mean $4$; median $5$; mode $5$ *(A1 A1)*. Deviations² $9, 1, 1, 1, 4$: "
                "variance $\\frac{16}{5} = 3.2$ *(M1 A1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.3", "mono": True}, {"text": "P1"}],
            "check": ["Rational(1+3+5+5+6, 5) == 4", "9 + 1 + 1 + 1 + 4 == 16", "Rational(16,5) == Rational(16,5)"],
        },
        {
            "id": "ibsl-sp-p06",
            "statement": "Data has mean $10$ and sd $4$. Under $y = 3x + 2$, **write down** the new mean, sd and variance. **[3]**",
            "solution": "Mean $32$; sd $12$; variance $144$ *(A1 A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.3", "mono": True}, {"text": "P1"}],
            "check": ["3*10 + 2 == 32", "3*4 == 12", "12**2 == 144"],
        },
        {
            "id": "ibsl-sp-p07",
            "statement": "A regression line of $y$ on $x$ has gradient $-2$ and passes through the mean point $(5, 12)$. **Find** its equation and predict $y$ at $x = 4$. **[3]**",
            "solution": "$12 = -2(5) + c \\Rightarrow c = 22$: $y = -2x + 22$ *(M1 A1)*. At $x = 4$: $y = 14$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.4", "mono": True}, {"text": "P1"}],
            "check": ["solve(Eq(-2*5 + c, 12), c) == [22]", "-2*4 + 22 == 14"],
        },
        {
            "id": "ibsl-sp-p08",
            "statement": "**Interpret** $r = -0.78$ for hours of TV vs test score, and state whether a prediction at an $x$ inside the data range is reliable. **[3]**",
            "solution": (
                "A moderately strong, negative, linear correlation between TV hours and "
                "score *(A1 A1)*. Interpolation with $|r| = 0.78$: reasonably reliable "
                "*(R1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.4", "mono": True}, {"text": "P2"}],
            "check": ["Abs(Rational(-78,100)) > Rational(1,2)"],
        },
        {
            "id": "ibsl-sp-p09",
            "statement": "A fair $20$-sided die is rolled. **Find** $P(\\text{prime})$, and the expected number of primes in $100$ rolls. **[3]**",
            "solution": (
                "Primes $\\le 20$: $2,3,5,7,11,13,17,19$ — eight: $P = \\frac{8}{20} = "
                "\\frac{2}{5}$ *(M1 A1)*. Expected: $100 \\cdot \\frac{2}{5} = 40$ *(A1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.5", "mono": True}, {"text": "P1"}],
            "check": ["Rational(8,20) == Rational(2,5)", "100*Rational(2,5) == 40"],
        },
        {
            "id": "ibsl-sp-p10",
            "statement": "A letter is chosen at random from STATISTICS. **Find** $P(T)$ and $P(\\text{vowel})$. **[2]**",
            "solution": "Ten letters: three T's, vowels A, I, I: $P(T) = \\frac{3}{10}$, $P(\\text{vowel}) = \\frac{3}{10}$ *(A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.5", "mono": True}, {"text": "P1"}],
            "check": ["Rational(3,10) == Rational(3,10)", "3 + 3 + 1 + 2 + 1 == 10"],
        },
        {
            "id": "ibsl-sp-p11",
            "statement": "$A$ and $B$ are independent with $P(A) = 0.45$, $P(B) = 0.3$. **Find** $P(A \\cap B)$ and $P(A \\cup B)$. **[3]**",
            "solution": "$P(A \\cap B) = 0.135$ *(M1 A1)*; union $= 0.45 + 0.3 - 0.135 = 0.615$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.6", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(45,100)*Rational(3,10) == Rational(27,200)",
                "Rational(45,100) + Rational(3,10) - Rational(27,200) == Rational(123,200)",
            ],
        },
        {
            "id": "ibsl-sp-p12",
            "statement": "A bag has $4$ green and $6$ red counters. Two are drawn without replacement. **Find** $P(\\text{both green})$. **[2]**",
            "solution": "$\\frac{4}{10} \\cdot \\frac{3}{9} = \\frac{2}{15}$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.6", "mono": True}, {"text": "P1"}],
            "check": ["Rational(4,10)*Rational(3,9) == Rational(2,15)"],
        },
        {
            "id": "ibsl-sp-p13",
            "statement": "$X$ takes $1, 2, 3, 4$ with $P = 0.1, 0.2, p, 0.4$. **Find** $p$ and $E(X)$. **[3]**",
            "solution": "$p = 0.3$ *(A1)*. $E(X) = 0.1 + 0.4 + 0.9 + 1.6 = 3$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.7", "mono": True}, {"text": "P1"}],
            "check": [
                "1 - Rational(1,10) - Rational(2,10) - Rational(4,10) == Rational(3,10)",
                "Rational(1,10) + 2*Rational(2,10) + 3*Rational(3,10) + 4*Rational(4,10) == 3",
            ],
        },
        {
            "id": "ibsl-sp-p14",
            "statement": "A game pays $\\$12$ with probability $\\dfrac{1}{3}$ and nothing otherwise. **Find** the stake that makes the game fair. **[2]**",
            "solution": "Fair: stake $=$ expected payout $= 12 \\cdot \\frac{1}{3} = \\$4$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.7", "mono": True}, {"text": "P1"}],
            "check": ["12*Rational(1,3) == 4"],
        },
        {
            "id": "ibsl-sp-p15",
            "statement": "$X \\sim B(15, 0.2)$. **Write down** $E(X)$ and find $\\mathrm{Var}(X)$. **[2]**",
            "solution": "$E(X) = 3$ *(A1)*; $\\mathrm{Var} = 15(0.2)(0.8) = 2.4$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.8", "mono": True}, {"text": "P1"}],
            "check": ["15*Rational(2,10) == 3", "15*Rational(2,10)*Rational(8,10) == Rational(12,5)"],
        },
        {
            "id": "ibsl-sp-p16",
            "statement": "$X \\sim B\\left(5, \\dfrac{1}{3}\\right)$. **Find** the exact value of $P(X = 2)$. **[3]**",
            "solution": "$\\binom{5}{2}\\left(\\frac{1}{3}\\right)^2\\left(\\frac{2}{3}\\right)^3 = 10 \\cdot \\frac{1}{9} \\cdot \\frac{8}{27} = \\frac{80}{243}$ *(M1 A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.8", "mono": True}, {"text": "P1"}],
            "check": ["binomial(5,2)*Rational(1,3)**2*Rational(2,3)**3 == Rational(80, 243)"],
        },
        {
            "id": "ibsl-sp-p17",
            "statement": "$X \\sim N(100, 15^2)$. Using landmark percentages, **write down** $P(85 < X < 115)$ and $P(X > 130)$. **[2]**",
            "solution": "$\\pm 1\\sigma$: $\\approx 0.68$ *(A1)*; beyond $+2\\sigma$: $\\approx 0.025$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.9", "mono": True}, {"text": "P2"}],
            "check": ["100 - 15 == 85", "100 + 2*15 == 130", "Abs(erf(1/sqrt(2)) - 0.6827) < 0.001"],
        },
        {
            "id": "ibsl-sp-p18",
            "statement": "$X \\sim N(70, 6^2)$. Given invNorm$(0.05) \\approx -1.6449$, **find** the value below which the lowest $5\\%$ of values fall. **[2]**",
            "solution": "$x = 70 - 1.6449 \\times 6 \\approx 60.1$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.9", "mono": True}, {"text": "P2"}],
            "check": ["Abs(70 - 6*1.6449 - 60.13) < 0.05"],
        },
        {
            "id": "ibsl-sp-p19",
            "statement": "The lines $y = 2.1x + 3$ ($y$ on $x$) and $x = 0.4y - 0.5$ ($x$ on $y$) fit a dataset. **State** which line predicts $x$ when $y = 25$, and compute the prediction. **[2]**",
            "solution": "The $x$-on-$y$ line *(R1)*: $x = 0.4(25) - 0.5 = 9.5$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.10", "mono": True}, {"text": "P2"}],
            "check": ["Rational(4,10)*25 - Rational(1,2) == Rational(19,2)"],
        },
        {
            "id": "ibsl-sp-p20",
            "statement": "The regression lines $y = 2x + 3$ and $x = 0.4y - 1$ describe one dataset. **Find** $\\bar{x}$ and $\\bar{y}$. **[3]**",
            "solution": "Solve simultaneously: $x = 0.4(2x + 3) - 1 = 0.8x + 0.2 \\Rightarrow \\bar{x} = 1$, $\\bar{y} = 5$ *(M1 A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.10", "mono": True}, {"text": "P1"}],
            "check": ["solve(Eq(x, Rational(4,10)*(2*x + 3) - 1), x) == [1]", "2*1 + 3 == 5"],
        },
        {
            "id": "ibsl-sp-p21",
            "statement": "$P(A \\cap B) = 0.12$, $P(B) = 0.3$. **Find** $P(A \\mid B)$. **[2]**",
            "solution": "$\\frac{0.12}{0.3} = 0.4$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.11", "mono": True}, {"text": "P1"}],
            "check": ["Rational(12,100)/Rational(3,10) == Rational(2,5)"],
        },
        {
            "id": "ibsl-sp-p22",
            "statement": "$P(A) = 0.55$, $P(A \\mid B) = 0.55$, $P(B) = 0.2$. **State** with reason whether $A$ and $B$ are independent, and find $P(A \\cap B)$. **[3]**",
            "solution": "$P(A \\mid B) = P(A)$: independent *(R1)*. $P(A \\cap B) = 0.2 \\times 0.55 = 0.11$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.11", "mono": True}, {"text": "P1"}],
            "check": ["Rational(2,10)*Rational(55,100) == Rational(11,100)"],
        },
        {
            "id": "ibsl-sp-p23",
            "statement": "$X \\sim N(75, 8^2)$. **Find** the $z$-value of $x = 85$. **[2]**",
            "solution": "$z = \\frac{85 - 75}{8} = 1.25$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.12", "mono": True}, {"text": "P1"}],
            "check": ["Rational(10, 8) == Rational(5, 4)"],
        },
        {
            "id": "ibsl-sp-p24",
            "statement": "$X \\sim N(\\mu, 5^2)$ and $P(X > 30) = 0.1$. Given invNorm$(0.9) \\approx 1.2816$, **find** $\\mu$. **[3]**",
            "solution": "$P(X < 30) = 0.9$: $\\frac{30 - \\mu}{5} = 1.2816 \\Rightarrow \\mu = 30 - 6.408 \\approx 23.6$ *(M1 A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.12", "mono": True}, {"text": "P2"}],
            "check": ["Abs(30 - 5*1.2816 - 23.59) < 0.05"],
        },
    ]


# ===========================================================================
# Test-yourself bank — one exam-style question per subtopic
# ===========================================================================
def test_bank():
    return [
        {
            "id": "ibsl-sp-q01",
            "statement": "A university has $4000$ undergraduates and $1000$ postgraduates. **Find** the stratified allocation of a sample of $100$, and state why stratification helps here. **[3]**",
            "solution": "Undergrads $80$, postgrads $20$ *(M1 A1)*; it guarantees proportional representation of both groups *(R1)*.",
            "badges": [{"text": "ib-aa-sl-4.1", "mono": True}],
            "check": ["Rational(100,5000)*4000 == 80", "Rational(100,5000)*1000 == 20"],
        },
        {
            "id": "ibsl-sp-q02",
            "statement": "Eleven values: $4, 6, 7, 8, 9, 10, 11, 13, 14, 16, 40$. **Find** the five-number summary and show $40$ is an outlier. **[5]**",
            "solution": (
                "Min $4$, $Q_1 = 7$, median $10$, $Q_3 = 14$, max $40$ *(A1 A1 A1)*. IQR "
                "$7$: upper fence $14 + 10.5 = 24.5$; $40 > 24.5$: outlier ✓ *(M1 R1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.2", "mono": True}],
            "check": ["14 - 7 == 7", "14 + Rational(3,2)*7 == Rational(49,2)", "40 > Rational(49,2)"],
        },
        {
            "id": "ibsl-sp-q03",
            "statement": "Six values have mean $12$ and variance $9$. Each is multiplied by $2$ then reduced by $4$. **Find** the new mean, sd and variance. **[4]**",
            "solution": "Mean $2(12) - 4 = 20$ *(A1)*; sd $2 \\times 3 = 6$ *(M1 A1)*; variance $36$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.3", "mono": True}],
            "check": ["2*12 - 4 == 20", "sqrt(9) == 3", "2*3 == 6", "6**2 == 36"],
        },
        {
            "id": "ibsl-sp-q04",
            "statement": "A regression line $y = 4.2x + 8$ fits data with $2 \\le x \\le 9$ and $r = 0.95$. **Predict** $y$ at $x = 6$; comment on a prediction at $x = 20$. **[3]**",
            "solution": "$y = 4.2(6) + 8 = 33.2$ *(M1 A1)*. $x = 20$ is extrapolation — unreliable *(R1)*.",
            "badges": [{"text": "ib-aa-sl-4.4", "mono": True}],
            "check": ["Rational(42,10)*6 + 8 == Rational(166,5)", "20 > 9"],
        },
        {
            "id": "ibsl-sp-q05",
            "statement": "Two fair dice are rolled. **Find** the probability that the total is $7$, and the expected number of $7$s in $180$ rolls of the pair. **[4]**",
            "solution": "Six pairs of 36: $P = \\frac{1}{6}$ *(M1 A1)*. Expected: $180 \\cdot \\frac{1}{6} = 30$ *(M1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.5", "mono": True}],
            "check": ["Rational(6,36) == Rational(1,6)", "180*Rational(1,6) == 30"],
        },
        {
            "id": "ibsl-sp-q06",
            "statement": "In a group of $50$: $28$ like tea, $23$ like coffee, $9$ like both. **Find** $P(\\text{tea} \\cup \\text{coffee})$ and $P(\\text{tea} \\mid \\text{coffee})$. **[4]**",
            "solution": (
                "$P(T \\cup C) = \\frac{28 + 23 - 9}{50} = \\frac{42}{50} = \\frac{21}{25}$ "
                "*(M1 A1)*. $P(T \\mid C) = \\frac{9}{23}$ *(M1 A1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.6", "mono": True}],
            "check": ["Rational(28 + 23 - 9, 50) == Rational(21, 25)", "Rational(9, 23) == Rational(9, 23)"],
        },
        {
            "id": "ibsl-sp-q07",
            "statement": "$X$ takes $-2, 0, 3$ with $P(X = -2) = 0.4$, $P(X = 0) = 0.25$. **Find** $P(X = 3)$ and $E(X)$, and state whether a game with these net winnings favours the player. **[4]**",
            "solution": (
                "$P(X = 3) = 0.35$ *(A1)*. $E(X) = -0.8 + 0 + 1.05 = 0.25$ *(M1 A1)*. "
                "Positive: favours the player *(R1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.7", "mono": True}],
            "check": [
                "1 - Rational(4,10) - Rational(25,100) == Rational(35,100)",
                "-2*Rational(4,10) + 3*Rational(35,100) == Rational(1,4)",
            ],
        },
        {
            "id": "ibsl-sp-q08",
            "statement": "$X \\sim B(12, 0.25)$. **Write** $P(X \\ge 4)$ in terms of a cumulative probability, and **write down** $E(X)$ and $\\mathrm{Var}(X)$. **[4]**",
            "solution": "$P(X \\ge 4) = 1 - P(X \\le 3)$ *(M1 A1)*. $E(X) = 3$; $\\mathrm{Var} = 12(0.25)(0.75) = 2.25$ *(A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.8", "mono": True}],
            "check": ["12*Rational(1,4) == 3", "12*Rational(1,4)*Rational(3,4) == Rational(9,4)"],
        },
        {
            "id": "ibsl-sp-q09",
            "statement": "Masses are $N(60, 4^2)$ kg. **Write down** $P(X > 60)$, and use landmarks for $P(52 < X < 68)$ and $P(X < 52)$. **[3]**",
            "solution": "$0.5$ *(A1)*; $\\pm 2\\sigma$: $\\approx 0.95$ *(A1)*; below $-2\\sigma$: $\\approx 0.025$ *(A1)*.",
            "badges": [{"text": "ib-aa-sl-4.9", "mono": True}],
            "check": ["60 - 2*4 == 52", "60 + 2*4 == 68", "Abs(erf(2/sqrt(2)) - 0.9545) < 0.001"],
        },
        {
            "id": "ibsl-sp-q10",
            "statement": "For one dataset: $y = 1.5x + 6$ ($y$ on $x$) and $x = 0.6y - 2$ ($x$ on $y$). **Find** the mean point. **[4]**",
            "solution": (
                "$x = 0.6(1.5x + 6) - 2 = 0.9x + 1.6 \\Rightarrow 0.1x = 1.6 \\Rightarrow "
                "\\bar{x} = 16$ *(M1 A1)*; $\\bar{y} = 1.5(16) + 6 = 30$ *(A1 A1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.10", "mono": True}],
            "check": ["solve(Eq(x, Rational(6,10)*(Rational(3,2)*x + 6) - 2), x) == [16]", "Rational(3,2)*16 + 6 == 30"],
        },
        {
            "id": "ibsl-sp-q11",
            "statement": "$P(A) = 0.6$, $P(B) = 0.5$, $P(A \\cup B) = 0.8$. **Find** $P(A \\cap B)$ and $P(A \\mid B)$, and test independence. **[5]**",
            "solution": (
                "$P(A \\cap B) = 0.6 + 0.5 - 0.8 = 0.3$ *(M1 A1)*. $P(A \\mid B) = "
                "\\frac{0.3}{0.5} = 0.6 = P(A)$ *(M1 A1)*: independent ✓ *(R1)*."
            ),
            "badges": [{"text": "ib-aa-sl-4.11", "mono": True}],
            "check": [
                "Rational(6,10) + Rational(5,10) - Rational(8,10) == Rational(3,10)",
                "Rational(3,10)/Rational(5,10) == Rational(3,5)",
            ],
        },
        {
            "id": "ibsl-sp-q12",
            "statement": "$X \\sim N(\\mu, 12^2)$ and $P(X < 100) = 0.75$. Given invNorm$(0.75) \\approx 0.6745$, **find** $\\mu$ to 3 s.f. **[3]**",
            "solution": "$\\frac{100 - \\mu}{12} = 0.6745 \\Rightarrow \\mu = 100 - 8.094 \\approx 91.9$ *(M1 A1 A1)*.",
            "badges": [{"text": "ib-aa-sl-4.12", "mono": True}],
            "check": ["Abs(100 - 12*0.6745 - 91.9) < 0.05"],
        },
    ]


# ===========================================================================
# Assembly
# ===========================================================================
def build():
    lessons = [
        lesson_sampling(),
        lesson_presentation(),
        lesson_center_spread(),
        lesson_correlation(),
        lesson_probability_concepts(),
        lesson_combined_events(),
        lesson_discrete_rv(),
        lesson_binomial_dist(),
        lesson_normal(),
        lesson_x_on_y(),
        lesson_formal_conditional(),
        lesson_z_values(),
    ]
    unit = {
        "slug": "statistics-and-probability",
        "title": "Statistics & Probability",
        "unit": 4,
        "status": "published",
        "blurb": (
            "IB Topic 4, complete: sampling and bias, data presentation, centre and spread, "
            "correlation and both regression lines, the language of probability, combined "
            "events with Venn and tree diagrams, discrete random variables, the binomial "
            "and normal distributions, formal conditional probability, and z-values — "
            "SL 4.1 to 4.12, taught to markscheme standard."
        ),
        "buildsOn": (
            "SL 1.9's binomial coefficients power the binomial distribution; SL 2.10's "
            "equation craft returns in expected-value and unknown-parameter problems."
        ),
        "lessons": lessons,
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    return unit


def selfcheck(unit):
    from sympy import sympify
    n_checks = 0
    problems = []
    for les in unit["lessons"]:
        problems += les["workedExamples"] + les["tryIt"]
        ids = {p["id"] for p in les["workedExamples"] + les["tryIt"]}
        for step in les["interactive"]["steps"]:
            if step["kind"] in ("worked", "tryIt"):
                assert step["problemId"] in ids, f"{les['slug']}: dangling problemId {step['problemId']}"
            if step["kind"] == "tapQuestion":
                assert len(step["options"]) == len(set(step["options"])), f"{les['slug']}: dup options"
                for c in step["check"]:
                    assert bool(sympify(c)) is True, f"{les['slug']} tapQ: {c}"
                    n_checks += 1
    problems += unit["practice"] + unit["testYourself"]
    ids = [p["id"] for p in problems]
    assert len(ids) == len(set(ids)), "duplicate problem ids"
    for p in problems:
        for c in p["check"]:
            assert bool(sympify(c)) is True, f"{p['id']}: NOT TRUE: {c}"
            n_checks += 1
    return len(problems), n_checks


def main():
    unit = build()
    n_problems, n_checks = selfcheck(unit)
    with open(OUT, "w") as fh:
        json.dump(unit, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    n_steps = sum(len(l["interactive"]["steps"]) for l in unit["lessons"])
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(unit['lessons'])} lessons, "
          f"{n_steps} interactive steps, {n_problems} problems, {n_checks} sympy checks OK")


if __name__ == "__main__":
    main()
