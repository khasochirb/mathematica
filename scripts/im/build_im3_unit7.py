#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 7: Statistical Inference.

CCSS Integrated Math III: S-IC.1 (statistics as a process for making
inferences about population parameters from a random sample), S-IC.3
(recognise the purposes of and differences among surveys, observational
studies and experiments; explain how randomisation relates to each),
S-ID.4 (use the mean and standard deviation of a data set to fit it to a
normal distribution and estimate population percentages; the empirical
rule), S-IC.2 (decide whether a specified model is consistent with
results from a given data-generating process, e.g. by simulation),
S-IC.4 (use data from a sample survey to estimate a population
proportion; develop a margin of error through simulation), S-IC.5 (use
data from a randomised experiment to compare two treatments; use
simulation to decide if differences are significant), S-IC.6 (evaluate
reports based on data).

The unit's through-line: FROM DESCRIBING TO INFERRING. IM1 Unit 9
taught the student to summarise the data in hand — mean, spread, shape.
This unit asks the harder question: what does the data in hand say
about everyone who ISN'T in it? The answer has three moving parts. A
random sample earns the right to speak for the population; the normal
model and simulation say how much a statistic naturally wobbles; and
the margin of error turns that wobble into an honest interval. The
capstone is the randomised experiment — the one study design whose
conclusions get to use the word "causes".

Run: python3 scripts/im/build_im3_unit7.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — populations, samples and study types
# ===========================================================================

def lesson_samples():
    return lesson(
        slug="populations-samples-and-study-types",
        title="Samples & Study Types",
        concrete=(
            "A cook doesn't drink the whole pot to check the soup — one "
            "spoonful does it, PROVIDED the pot was stirred. An unstirred "
            "spoonful off the top tastes only the top. Every poll you have "
            "ever seen is a spoonful from a very large pot, and the whole "
            "game is in the stirring: a random sample of $50$ students can "
            "speak for a school of $1200$, while an unstirred sample of "
            "$5000$ speaks only for itself."
        ),
        objective=(
            "Distinguish population from sample and parameter from statistic, "
            "recognise biased sampling methods, classify surveys, "
            "observational studies and experiments, and explain why only a "
            "randomised experiment supports a causal conclusion."
        ),
        concept=[
            "The POPULATION is everyone you want to know about; the SAMPLE "
            "is the part you actually measure. A number describing the whole "
            "population is a PARAMETER; the same kind of number computed "
            "from the sample is a STATISTIC, and it exists to estimate the "
            "parameter. Ask $50$ of a school's $1200$ students and find "
            "$32$ in favour: the statistic is $\\hat{p} = \\frac{32}{50} = "
            "0.64$, and it estimates the parameter you cannot afford to "
            "measure — the true school-wide proportion.",

            "The estimate is only as good as the stirring. A RANDOM sample "
            "gives every member of the population the same chance of being "
            "chosen, which is what entitles the spoonful to taste like the "
            "pot. Convenient substitutes fail quietly: poll the $40$ "
            "students at the gym door about sports funding and $90\\%$ say "
            "yes; poll $50$ at random and $42\\%$ do. Nothing was computed "
            "wrong — the gym sample answered a different question, namely "
            "what gym-goers think.",

            "Studies come in three kinds, sorted by what the researcher "
            "DOES. A SURVEY asks. An OBSERVATIONAL STUDY watches groups "
            "that formed themselves — comparing students who already sleep "
            "eight hours against those who don't. An EXPERIMENT imposes: "
            "the researcher assigns who gets the treatment and who "
            "doesn't, by coin flip.",

            "Only the experiment can conclude CAUSE, and the reason is the "
            "coin flip. In an observational study the groups chose "
            "themselves, so anything that drives the choice — wealth, "
            "health, habits — rides along and could be the real cause. "
            "Random ASSIGNMENT breaks every such link: with $120$ plants "
            "split $60$–$60$ by chance, the two groups differ, on average, "
            "in nothing but the treatment. If the outcomes then differ, "
            "the treatment did it.",
        ],
        key_idea=(
            "A random sample is a stirred spoonful: its statistic estimates "
            "the population's parameter. And only a randomised experiment — "
            "where chance assigns the treatment — can turn \"goes together\" "
            "into \"causes\"."
        ),
        facts=[
            fact("Parameter vs statistic",
                 "p\\ \\text{(population)} \\quad \\text{vs} \\quad \\hat{p}\\ \\text{(sample)}",
                 "A parameter describes the whole population; a statistic is "
                 "computed from a sample and estimates it."),
            fact("Sample proportion",
                 "\\hat{p} = \\dfrac{\\text{count with the trait}}{n}",
                 "The fraction of the sample showing the trait — the "
                 "workhorse statistic of this unit."),
            fact("Random sampling",
                 "\\text{every member gets an equal chance}",
                 "Randomness is the stirring: it removes systematic bias, "
                 "leaving only chance wobble, which the rest of the unit "
                 "learns to measure."),
            fact("Three study types",
                 "\\text{ask, watch, or impose}",
                 "A survey asks, an observational study watches groups that "
                 "formed themselves, an experiment assigns treatments."),
            fact("Causation",
                 "\\text{random assignment} \\Rightarrow \\text{causal conclusion}",
                 "Only when chance decides who is treated do the groups "
                 "start equal — so only an experiment can say \"causes\"."),
        ],
        worked=[
            problem(
                "im3-u7-l1-we1",
                "A school has $1200$ students. A random sample of $50$ is "
                "asked whether school should start later; $32$ say yes. "
                "Identify the population, the sample, the statistic — and "
                "estimate how many students school-wide favour the change.",
                "**Name the pieces.** The population is all $1200$ students; "
                "the sample is the $50$ asked. The true school-wide "
                "proportion is the parameter — unknown, and the whole point."
                "**Compute the statistic.** $\\hat{p} = \\frac{32}{50} = "
                "\\frac{16}{25} = 0.64$."
                "**Scale it up.** Because the sample was random, $0.64$ is "
                "an honest estimate of the parameter: about $0.64 \\cdot "
                "1200 = 768$ students. An estimate, not a count — the next "
                "lessons measure how far off it might be.",
                [
                    "Eq(Rational(32, 50), Rational(16, 25))",
                    "Eq(Rational(16, 25), Rational(64, 100))",
                    "Eq(Rational(16, 25)*1200, 768)",
                ],
            ),
            problem(
                "im3-u7-l1-we2",
                "Asked about sports funding, $36$ of the $40$ students "
                "polled at the gym door said yes; in a random sample of "
                "$50$, only $21$ did. Compute both proportions, explain the "
                "gap, and say which number deserves trust.",
                "**Two proportions.** Gym door: $\\frac{36}{40} = 0.90$. "
                "Random sample: $\\frac{21}{50} = 0.42$. The gap is $0.90 - "
                "0.42 = 0.48$ — forty-eight points."
                "**Explain the gap.** The gym-door poll is a convenience "
                "sample: students at the gym are exactly the ones who "
                "benefit from sports funding. The method, not the "
                "arithmetic, is what's biased."
                "**Which to trust.** The random $42\\%$. A biased sample "
                "does not improve with size — $4000$ gym-goers would be "
                "just as skewed as $40$.",
                [
                    "Eq(Rational(36, 40), Rational(9, 10))",
                    "Eq(Rational(9, 10) - Rational(21, 50), Rational(12, 25))",
                    "Eq(Rational(12, 25), Rational(48, 100))",
                ],
            ),
            problem(
                "im3-u7-l1-we3",
                "Classify each study, and state which one could justify the "
                "claim \"the supplement CAUSES taller seedlings\": (a) "
                "$200$ gardeners are asked whether they use the supplement; "
                "(b) growth is compared between $60$ gardens that already "
                "use it and $60$ that don't; (c) $120$ seedlings are "
                "randomly split into two groups of $60$, one fed the "
                "supplement.",
                "**Sort by what the researcher does.** (a) asks — a survey. "
                "(b) watches groups that formed themselves — an "
                "observational study. (c) imposes the treatment by random "
                "assignment — an experiment."
                "**Only (c) supports cause.** In (b), gardens that chose "
                "the supplement may also water more, own better soil, or "
                "fuss more — any of those could be the real cause. In (c) "
                "the coin flip makes the groups of $60$ alike on average "
                "in everything except the supplement, so a growth gap can "
                "be pinned on the supplement itself.",
                [
                    "Eq(Rational(120, 2), 60)",
                    "Eq(60 + 60, 120)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Calling the sample's number a parameter.",
                "The 64% computed from the 50 students is a STATISTIC — it "
                "lives in the sample. The parameter is the school-wide "
                "value it estimates, which stays unknown. Statistic from "
                "Sample, Parameter from Population — the initials match.",
            ),
            mistake(
                "Trusting a big sample over a random one.",
                "Size fixes wobble, not bias. Fifty random students beat "
                "five thousand volunteers, because volunteers select "
                "themselves and no amount of them un-selects the sample.",
            ),
            mistake(
                "Reading causation off an observational study.",
                "Watching self-formed groups can show association only — "
                "whatever made the groups form (wealth, habits, health) is "
                "tangled with the treatment. Only random assignment "
                "untangles it.",
            ),
            mistake(
                "Confusing random sampling with random assignment.",
                "Random SAMPLING (who gets measured) lets you generalise to "
                "the population. Random ASSIGNMENT (who gets treated) lets "
                "you conclude cause. They are different coins doing "
                "different jobs, and a study can have either, both, or "
                "neither.",
            ),
        ],
        try_it=[
            problem(
                "im3-u7-l1-t1",
                "A library has $800$ members. In a random sample of $40$, "
                "exactly $18$ want longer weekend hours. Give the statistic "
                "$\\hat{p}$ and estimate how many members want the change.",
                "$\\hat{p} = \\frac{18}{40} = \\frac{9}{20} = 0.45$, so "
                "about $0.45 \\cdot 800 = 360$ members. The population is "
                "the $800$ members; the $45\\%$ is a statistic estimating "
                "the unknown parameter.",
                [
                    "Eq(Rational(18, 40), Rational(9, 20))",
                    "Eq(Rational(9, 20)*800, 360)",
                ],
            ),
            problem(
                "im3-u7-l1-t2",
                "A radio show invites listeners to call in about a proposed "
                "curfew; $84$ of the $120$ callers oppose it. Compute the "
                "proportion and explain why it should not be reported as "
                "\"$70\\%$ of the town opposes the curfew\".",
                "$\\frac{84}{120} = \\frac{7}{10} = 70\\%$ — of the "
                "CALLERS. This is a voluntary-response sample: people angry "
                "enough to phone a radio show select themselves, and "
                "strong feelings dial more often. The town's proportion "
                "could be far from $70\\%$ in either direction; only a "
                "random sample could say.",
                [
                    "Eq(Rational(84, 120), Rational(7, 10))",
                ],
            ),
            problem(
                "im3-u7-l1-t3",
                "Design an experiment to test a new fertiliser on $48$ "
                "tomato seedlings: state the two groups, how seedlings get "
                "into them, and why that method is required.",
                "Split the $48$ seedlings into two groups of $24$ BY RANDOM "
                "DRAW — fertiliser for one group, none (same water, light, "
                "soil) for the other. The random draw is the load-bearing "
                "part: it makes the groups alike on average in every "
                "hidden way (seed vigour, pot position), so a difference "
                "in growth can be attributed to the fertiliser and not to "
                "how the groups were chosen.",
                [
                    "Eq(Rational(48, 2), 24)",
                    "Eq(24 + 24, 48)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "The spoonful and the pot",
             "body": "The POPULATION is everyone you want to know about; the SAMPLE is the part you measure. A number for the whole population is a PARAMETER; the same number computed from the sample is a STATISTIC, and its job is to estimate the parameter. The soup rule: one stirred spoonful speaks for the pot — and random choice is the stirring.",
             "beats": ["Population = the whole pot, sample = the spoonful",
                       "Parameter (population) vs statistic (sample)",
                       "$\\hat{p} = \\dfrac{\\text{count}}{n}$ estimates the true $p$"]},
            {"kind": "worked", "title": "Fifty students speak for 1200", "problemId": "im3-u7-l1-we1"},
            tap(
                "Parameter or statistic?",
                "A random sample of $50$ of a school's $1200$ students "
                "finds $64\\%$ support a later start. The $64\\%$ is:",
                ["a statistic — computed from the sample",
                 "a parameter — it describes the school",
                 "a census of the school",
                 "a margin of error"],
                0,
                "It was computed from the $50$ sampled students, so it is "
                "a statistic: $\\frac{32}{50} = 0.64$. The parameter is "
                "the true school-wide proportion it estimates — unknown "
                "unless all $1200$ are asked.",
                ["Eq(Rational(32, 50), Rational(64, 100))"],
            ),
            {"kind": "worked", "title": "The gym-door poll", "problemId": "im3-u7-l1-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Big is not better than random",
             "body": "Sample size fixes chance wobble; it cannot fix bias. A convenience or volunteer sample answers the wrong question no matter how large it grows — $5000$ gym-door students are exactly as skewed as $40$. Fifty random students beat them all."},
            tap(
                "Spot the bias",
                "To gauge support for sports funding, a reporter polls the "
                "first $40$ students at the gym door: $36$ say yes. The "
                "flaw is:",
                ["a convenience sample — gym-goers over-represent sports fans",
                 "the sample is too small to mean anything",
                 "the reporter should have polled teachers instead",
                 "there is no flaw — 90 percent is decisive"],
                0,
                "$\\frac{36}{40} = 90\\%$ of GYM-GOERS — the people most "
                "invested in sports. The method selects its own answer; "
                "randomness is what removes that thumb from the scale.",
                ["Eq(Rational(36, 40), Rational(9, 10))"],
            ),
            {"kind": "worked", "title": "Survey, observe, or experiment", "problemId": "im3-u7-l1-we3"},
            {"kind": "teach", "title": "Why the coin flip earns \"causes\"",
             "body": "Ask, watch, or impose: survey, observational study, experiment. In an observational study the groups chose themselves, so whatever drove the choice rides along as a hidden cause. Random ASSIGNMENT — a coin flip deciding who is treated — makes the groups alike on average in everything else. Then, and only then, an outcome gap convicts the treatment.",
             "beats": ["Survey asks · observational study watches · experiment imposes",
                       "Self-formed groups carry hidden differences",
                       "Random assignment equalises them — experiments may say \"causes\""]},
            {"kind": "tryIt", "title": "Estimate for the library", "problemId": "im3-u7-l1-t1"},
            {"kind": "tryIt", "title": "The call-in poll", "problemId": "im3-u7-l1-t2"},
            {"kind": "tryIt", "title": "Design the experiment", "problemId": "im3-u7-l1-t3"},
            tap(
                "Who may say \"causes\"?",
                "Three studies link a supplement to seedling growth: a "
                "survey of gardeners, an observational comparison of "
                "$60$ + $60$ self-selected gardens, and an experiment "
                "randomly splitting $120$ seedlings $60$–$60$. Which can "
                "conclude the supplement CAUSES growth?",
                ["only the randomised experiment",
                 "the observational study — its groups are equal in size",
                 "the survey — it has the most gardeners",
                 "all three equally"],
                0,
                "Equal group sizes are not equal groups. Only random "
                "assignment makes the two groups of $60$ alike on average "
                "in everything but the treatment — so only the experiment "
                "supports a causal verdict.",
                ["Eq(Rational(120, 2), 60)"],
            ),
            {"kind": "recap", "title": "Samples & study types — what sticks",
             "points": [
                 "Parameter describes the population; a statistic, computed from the sample, estimates it.",
                 "Random sampling is the stirring: every member equally likely, bias removed.",
                 "A big biased sample is still biased — size fixes wobble, never bias.",
                 "Survey asks, observational study watches, experiment imposes.",
                 "Random assignment is what lets an experiment — and nothing else — say \"causes\".",
             ]},
        ],
    )


# ===========================================================================
# Lesson 2 — the normal model
# ===========================================================================

def lesson_normal():
    return lesson(
        slug="the-normal-model",
        title="The Normal Model",
        concrete=(
            "Measure the heights of every sixteen-year-old in a city and "
            "the histogram piles up in the middle and thins out "
            "symmetrically — the bell shape. So do bottle volumes off a "
            "filling machine, test scores, reaction times. One curve fits "
            "them all, and it is completely described by just two numbers: "
            "where the middle is, and how wide the pile spreads. Know "
            "those two and you can say what fraction of a city falls in "
            "any range — without measuring anyone else."
        ),
        objective=(
            "Use the mean and standard deviation of a normal distribution "
            "with the 68–95–99.7 rule to estimate percentages and counts, "
            "and use z-scores to place and compare values from different "
            "distributions."
        ),
        concept=[
            "Many measured quantities — heights, machine outputs, scores — "
            "pile up symmetrically around their mean. The NORMAL MODEL is "
            "that idealised bell curve, and it is completely pinned down "
            "by two numbers: the mean $\\mu$ (the centre) and the "
            "standard deviation $\\sigma$ (the spread). Same shape every "
            "time; only centre and width change.",

            "The EMPIRICAL RULE says how much of a normal population sits "
            "within each band: about $68\\%$ within one standard "
            "deviation of the mean, $95\\%$ within two, $99.7\\%$ within "
            "three. Heights with $\\mu = 170$ cm and $\\sigma = 8$ cm: "
            "$68\\%$ of students stand between $162$ and $178$ cm — no "
            "extra measuring required.",

            "Symmetry lets you cut the leftovers in half. Outside "
            "$\\mu \\pm 2\\sigma$ lives $100 - 95 = 5\\%$ of the "
            "population — so each TAIL holds $2.5\\%$. Outside one "
            "standard deviation: $32\\%$ total, $16\\%$ per tail. Every "
            "empirical-rule question is these two moves: pick the band, "
            "then split what's left.",

            "The Z-SCORE puts every normal distribution on one ruler: "
            "$z = \\frac{x - \\mu}{\\sigma}$ counts how many standard "
            "deviations a value sits from its mean — positive above, "
            "negative below. An $82$ on a test with $\\mu = 70, \\sigma "
            "= 8$ is $z = 1.5$; a $75$ on a test with $\\mu = 60, "
            "\\sigma = 12$ is $z = 1.25$. The first score is rarer air, "
            "even though $75 < 82$ says nothing by itself.",
        ],
        key_idea=(
            "Two numbers describe a whole normal population: 68% of it "
            "lies within one standard deviation of the mean, 95% within "
            "two, 99.7% within three — and the z-score converts any value "
            "onto that shared ruler."
        ),
        facts=[
            fact("The z-score", "z = \\dfrac{x - \\mu}{\\sigma}",
                 "How many standard deviations x sits from the mean — "
                 "negative below, positive above."),
            fact("The empirical rule",
                 "\\mu \\pm \\sigma:\\ 68\\% \\quad \\mu \\pm 2\\sigma:\\ 95\\% \\quad \\mu \\pm 3\\sigma:\\ 99.7\\%",
                 "The three bands of a normal distribution — memorise the "
                 "triple 68, 95, 99.7."),
            fact("One tail beyond 2 sigma", "\\tfrac{100 - 95}{2} = 2.5\\%",
                 "What's outside the band splits evenly between the two "
                 "tails, by symmetry."),
            fact("One tail beyond 1 sigma", "\\tfrac{100 - 68}{2} = 16\\%",
                 "Same halving move, one standard deviation out."),
            fact("Reading z backwards", "x = \\mu + z\\sigma",
                 "A z-score converts back to a raw value: start at the "
                 "mean, step z standard deviations."),
        ],
        worked=[
            problem(
                "im3-u7-l2-we1",
                "Student heights are approximately normal with mean $170$ "
                "cm and standard deviation $8$ cm. What fraction of "
                "students stand between $162$ and $178$ cm? Between $154$ "
                "and $186$ cm? About how many of $200$ students fall in "
                "the first band?",
                "**Convert the endpoints to bands.** $162 = 170 - 8$ and "
                "$178 = 170 + 8$: that is $\\mu \\pm \\sigma$, so about "
                "$68\\%$. And $154 = 170 - 16$, $186 = 170 + 16$: "
                "$\\mu \\pm 2\\sigma$, so about $95\\%$."
                "**Count.** $0.68 \\cdot 200 = 136$ of the $200$ students "
                "— the empirical rule turns two numbers into a headcount.",
                [
                    "Eq(170 - 8, 162)",
                    "Eq(170 + 8, 178)",
                    "Eq(170 - 2*8, 154)",
                    "Eq(170 + 2*8, 186)",
                    "Eq(Rational(68, 100)*200, 136)",
                ],
            ),
            problem(
                "im3-u7-l2-we2",
                "Ana scored $82$ on a maths test with mean $70$ and "
                "standard deviation $8$, and $75$ on a history test with "
                "mean $60$ and standard deviation $12$. Which score is "
                "relatively stronger?",
                "**Put both on the z ruler.** Maths: $z = \\frac{82 - 70}"
                "{8} = 1.5$. History: $z = \\frac{75 - 60}{12} = 1.25$."
                "**Compare positions, not points.** The maths score sits "
                "one and a half spreads above its class; the history "
                "score, one and a quarter. Maths is the stronger "
                "performance — raw scores from different distributions "
                "cannot be compared until z converts them to the same "
                "ruler.",
                [
                    "Eq(Rational(82 - 70, 8), Rational(3, 2))",
                    "Eq(Rational(75 - 60, 12), Rational(5, 4))",
                    "Rational(3, 2) > Rational(5, 4)",
                ],
            ),
            problem(
                "im3-u7-l2-we3",
                "A machine fills bottles with mean $500$ ml and standard "
                "deviation $5$ ml, approximately normally. Out of $2000$ "
                "bottles, about how many hold more than $510$ ml? Fewer "
                "than $495$ ml?",
                "**Locate each cutoff in sigmas.** $510 = 500 + 2 \\cdot "
                "5$ is two standard deviations up. Outside $\\mu \\pm "
                "2\\sigma$ lies $5\\%$, so the upper tail holds "
                "$2.5\\%$: about $0.025 \\cdot 2000 = 50$ bottles."
                "**Second cutoff.** $495 = 500 - 5$ is one standard "
                "deviation down; the lower tail beyond it holds "
                "$\\frac{100 - 68}{2} = 16\\%$: about $0.16 \\cdot 2000 "
                "= 320$ bottles."
                "**The pattern.** Band, leftover, halve — every tail "
                "question is those three moves.",
                [
                    "Eq(500 + 2*5, 510)",
                    "Eq(Rational(100 - 95, 2), Rational(5, 2))",
                    "Eq(Rational(5, 2)/100*2000, 50)",
                    "Eq(500 - 5, 495)",
                    "Eq(Rational(100 - 68, 2), 16)",
                    "Eq(Rational(16, 100)*2000, 320)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Applying the empirical rule to skewed data.",
                "The 68–95–99.7 numbers belong to the bell shape. Incomes, "
                "house prices and waiting times pile up on one side and "
                "trail off on the other — for them the rule simply lies. "
                "Check the shape before quoting the percentages.",
            ),
            mistake(
                "Forgetting to halve the tail.",
                "Outside two standard deviations lies 5% — split between "
                "TWO tails. \"Above mu + 2 sigma\" is 2.5%, not 5%. "
                "Symmetry does half the work; let it.",
            ),
            mistake(
                "Comparing raw scores from different tests.",
                "An 82 in maths against a 75 in history compares nothing "
                "until each is measured against its own mean and spread. "
                "Convert both to z-scores first; the bigger z is the "
                "stronger performance.",
            ),
            mistake(
                "Thinking a z-score must be positive.",
                "Values below the mean have negative z — that's the sign "
                "doing its job, not an error. z = -2 is exactly as far "
                "from the mean as z = 2, just on the quiet side.",
            ),
        ],
        try_it=[
            problem(
                "im3-u7-l2-t1",
                "Exam scores are approximately normal with mean $64$ and "
                "standard deviation $3$. Between which two scores do the "
                "middle $95\\%$ fall? What percent score above $67$?",
                "Middle $95\\%$: $\\mu \\pm 2\\sigma = 64 \\pm 6$, so "
                "between $58$ and $70$. Above $67 = 64 + 3$ is one "
                "standard deviation up: one tail of $\\frac{100 - 68}{2} "
                "= 16\\%$.",
                [
                    "Eq(64 - 2*3, 58)",
                    "Eq(64 + 2*3, 70)",
                    "Eq(64 + 3, 67)",
                    "Eq(Rational(100 - 68, 2), 16)",
                ],
            ),
            problem(
                "im3-u7-l2-t2",
                "A distribution has mean $74$ and standard deviation $6$. "
                "Find the z-score of the value $86$, and the value whose "
                "z-score is $-1$.",
                "$z = \\frac{86 - 74}{6} = 2$ — two standard deviations "
                "above the mean. Backwards: $x = 74 + (-1) \\cdot 6 = 68$ "
                "— one step below.",
                [
                    "Eq(Rational(86 - 74, 6), 2)",
                    "Eq(74 - 6, 68)",
                ],
            ),
            problem(
                "im3-u7-l2-t3",
                "Batteries last a mean of $40$ hours with standard "
                "deviation $4$ hours, approximately normally. Out of "
                "$500$ batteries, about how many die before $36$ hours?",
                "$36 = 40 - 4$ is one standard deviation below the mean, "
                "so the tail below it holds $\\frac{100 - 68}{2} = "
                "16\\%$: about $0.16 \\cdot 500 = 80$ batteries.",
                [
                    "Eq(40 - 4, 36)",
                    "Eq(Rational(100 - 68, 2), 16)",
                    "Eq(Rational(16, 100)*500, 80)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "One curve, two numbers",
             "body": "Heights, fill volumes, scores — measured quantities pile up symmetrically in a bell shape. The normal model is that curve, pinned down entirely by the mean $\\mu$ (centre) and standard deviation $\\sigma$ (spread). The empirical rule reads it off: $68\\%$ of the population within $\\mu \\pm \\sigma$, $95\\%$ within $\\mu \\pm 2\\sigma$, $99.7\\%$ within $\\mu \\pm 3\\sigma$.",
             "beats": ["Bell shape: symmetric pile around the mean",
                       "Two numbers describe it all: $\\mu$ and $\\sigma$",
                       "Bands: $68$–$95$–$99.7$ percent"]},
            {"kind": "worked", "title": "Heights in bands", "problemId": "im3-u7-l2-we1"},
            tap(
                "Within one sigma",
                "Heights are normal with mean $170$ cm and standard "
                "deviation $8$ cm. About what percent of students stand "
                "between $162$ and $178$ cm?",
                ["$68\\%$", "$95\\%$", "$50\\%$", "$34\\%$"],
                0,
                "$162$ and $178$ are exactly $\\mu - \\sigma$ and "
                "$\\mu + \\sigma$, and the middle one-sigma band always "
                "holds about $68\\%$ of a normal population.",
                ["Eq(170 - 8, 162)", "Eq(170 + 8, 178)"],
            ),
            {"kind": "worked", "title": "Two tests, one ruler", "problemId": "im3-u7-l2-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Tails come in pairs",
             "body": "The rule tells you what's INSIDE a band; what's outside splits evenly between two tails. Beyond $\\mu \\pm 2\\sigma$ lies $5\\%$ — so above $\\mu + 2\\sigma$ is $2.5\\%$, not $5\\%$. Forgetting to halve is the single most common error in this lesson."},
            tap(
                "The top tail",
                "For a normal distribution, about what percent of values "
                "lie ABOVE $\\mu + 2\\sigma$?",
                ["$2.5\\%$", "$5\\%$", "$95\\%$", "$47.5\\%$"],
                0,
                "Outside the two-sigma band lies $100 - 95 = 5\\%$, and "
                "symmetry splits it: $2.5\\%$ in each tail.",
                ["Eq(Rational(100 - 95, 2), Rational(5, 2))"],
            ),
            {"kind": "worked", "title": "Counting the tails", "problemId": "im3-u7-l2-we3"},
            {"kind": "teach", "title": "The universal ruler",
             "body": "The z-score $z = \\frac{x - \\mu}{\\sigma}$ counts standard deviations from the mean — positive above, negative below. It makes different distributions comparable: an $82$ at $z = 1.5$ outranks a $75$ at $z = 1.25$, whatever the raw scores say. And it runs backwards: $x = \\mu + z\\sigma$.",
             "beats": ["$z = \\dfrac{x - \\mu}{\\sigma}$ — sigmas from the mean",
                       "Compare z-scores, never raw scores",
                       "Backwards: $x = \\mu + z\\sigma$"]},
            {"kind": "tryIt", "title": "Bands and a tail", "problemId": "im3-u7-l2-t1"},
            {"kind": "tryIt", "title": "z, forwards and back", "problemId": "im3-u7-l2-t2"},
            {"kind": "tryIt", "title": "Battery early deaths", "problemId": "im3-u7-l2-t3"},
            tap(
                "Read the z",
                "A score of $59$ comes from a distribution with mean $65$ "
                "and standard deviation $3$. Its z-score is:",
                ["$-2$", "$2$", "$-6$", "$-0.5$"],
                0,
                "$z = \\frac{59 - 65}{3} = \\frac{-6}{3} = -2$: two "
                "standard deviations BELOW the mean — the sign carries "
                "the direction.",
                ["Eq(Rational(59 - 65, 3), -2)"],
            ),
            {"kind": "recap", "title": "The normal model — what sticks",
             "points": [
                 "A normal distribution is fully described by its mean and standard deviation.",
                 "Empirical rule: about 68% within one sigma, 95% within two, 99.7% within three.",
                 "What's outside a band splits evenly: 2.5% per tail beyond two sigma, 16% beyond one.",
                 "The z-score counts sigmas from the mean and makes different distributions comparable.",
                 "The rule is for bell-shaped data only — check the shape before using it.",
             ]},
        ],
    )


# ===========================================================================
# Lesson 3 — simulation and sampling variability
# ===========================================================================

def lesson_simulation():
    return lesson(
        slug="simulation-and-sampling-variability",
        title="Simulation & Sampling Variability",
        concrete=(
            "Flip a fair coin $100$ times and you will almost never get "
            "exactly $50$ heads — $47$, $53$, even $58$ are everyday "
            "results. So when a friend's \"fair\" coin shows $62$ heads, "
            "is that ordinary wobble or evidence of a crooked coin? "
            "There's a way to find out without any new formula: make "
            "fair coins flip $100$ times over and over — hundreds of "
            "simulated rounds — and see how often $62$ actually happens. "
            "If honest coins almost never do that, stop blaming luck."
        ),
        objective=(
            "Recognise that statistics vary from sample to sample, design "
            "simulations with random digits, and use the results of many "
            "simulated trials to judge whether an observed result is "
            "consistent with a claimed model."
        ),
        concept=[
            "SAMPLING VARIABILITY is the fact that honest samples "
            "disagree: two random samples from the same population give "
            "two different values of $\\hat{p}$, and neither is wrong. "
            "The statistic dances around the parameter. The dance "
            "tightens as the sample grows — big samples wobble less — "
            "but it never stops entirely.",

            "A SIMULATION makes the wobble visible. To test a claim, "
            "pretend the claim is true, build it from a chance device — "
            "coins, dice, random digits — and run the sampling many "
            "times. Two hundred simulated rounds of $100$ fair flips "
            "draw a picture of what fair coins DO: mostly $40$–$60$ "
            "heads, a shape you can hold a real result against.",

            "The verdict rule: find where the OBSERVED result falls "
            "among the simulated ones. If results at least as extreme "
            "show up often, the observation is consistent with the "
            "claim — wobble explains it. If they show up rarely — as a "
            "working habit, in fewer than about $5\\%$ of trials — the "
            "claim itself is what's doubtful. $62$ heads reached in "
            "only $4$ of $200$ fair-coin rounds is a $2\\%$ event: "
            "suspect the coin, not your luck.",

            "Random DIGITS make a simulator for any probability. For a "
            "$30\\%$ free-throw shooter, let digits $0,1,2$ be a make "
            "and $3$–$9$ a miss — three digits of ten, exactly "
            "$30\\%$. A run of $5$ digits is then a $5$-shot trip. The "
            "assignment must match the probability by COUNT of digits: "
            "$45\\%$ needs pairs $00$–$44$, forty-five pairs of the "
            "hundred.",
        ],
        key_idea=(
            "To judge a claim, assume it, simulate it, and see where the "
            "real result lands: if outcomes that extreme almost never "
            "occur in the simulation, doubt the claim — not your luck."
        ),
        facts=[
            fact("Sampling variability",
                 "\\text{same } p \\ \\longrightarrow\\ \\text{different } \\hat{p}",
                 "Honest random samples disagree with each other; the "
                 "statistic wobbles around the parameter."),
            fact("The simulation recipe",
                 "\\text{assume the claim} \\to \\text{simulate many trials} \\to \\text{locate the observed result}",
                 "Pretend the claim is true and watch what it produces — "
                 "then see if reality fits."),
            fact("The 5 percent habit",
                 "\\text{observed in} < 5\\% \\text{ of trials} \\Rightarrow \\text{doubt the claim}",
                 "The working threshold for \"too rare to blame on "
                 "wobble\" — a convention, not a law of nature."),
            fact("Digit assignment",
                 "30\\%:\\ \\text{digits } 0,1,2 \\text{ hit},\\ 3\\text{–}9 \\text{ miss}",
                 "Probabilities become shares of the ten digits (or a "
                 "hundred digit pairs) — match by count."),
            fact("Size calms the wobble",
                 "n \\uparrow\\ \\Longrightarrow\\ \\text{spread of } \\hat{p} \\downarrow",
                 "Larger samples produce statistics that cluster more "
                 "tightly around the truth."),
        ],
        worked=[
            problem(
                "im3-u7-l3-we1",
                "A coin claimed fair lands heads $62$ times in $100$ "
                "flips. In $200$ simulated rounds of $100$ genuinely "
                "fair flips, only $4$ rounds reached $62$ or more heads. "
                "Is the coin's claim believable?",
                "**Locate the observation.** Among fair coins, $62$-or-"
                "more heads happened in $\\frac{4}{200} = 2\\%$ of "
                "rounds."
                "**Apply the habit.** $2\\% < 5\\%$: results this "
                "extreme are rare for FAIR coins. Wobble is a poor "
                "explanation; a biased coin is a better one."
                "**Say it precisely.** The simulation doesn't prove "
                "bias — it shows the fair-coin model and the data sit "
                "badly together, which is exactly what \"statistically "
                "significant\" means.",
                [
                    "Eq(Rational(4, 200), Rational(1, 50))",
                    "Eq(Rational(1, 50), Rational(2, 100))",
                    "Rational(1, 50) < Rational(1, 20)",
                ],
            ),
            problem(
                "im3-u7-l3-we2",
                "A sweet company claims $40\\%$ of its sweets are red. A "
                "random bag of $25$ has only $5$ red ($20\\%$). Fifty "
                "simulated bags at the claimed rate contained $6$ to "
                "$14$ reds in $47$ of $50$ cases, and $5$-or-fewer reds "
                "in $2$ cases. What should we conclude?",
                "**What the claim predicts.** At $40\\%$, a bag of $25$ "
                "averages $0.4 \\cdot 25 = 10$ reds — but simulation "
                "shows honest bags ranging widely; $6$–$14$ is business "
                "as usual."
                "**Locate the bag.** Five reds ($\\hat{p} = \\frac{5}"
                "{25} = 0.2$) occurred in $\\frac{2}{50} = 4\\%$ of "
                "simulated bags — under the $5\\%$ habit, surprising."
                "**Conclude with care.** The bag casts real doubt on "
                "the $40\\%$ claim. With only $50$ trials the estimate "
                "of \"how rare\" is itself rough — more simulation "
                "rounds would sharpen it.",
                [
                    "Eq(Rational(2, 5)*25, 10)",
                    "Eq(Rational(5, 25), Rational(1, 5))",
                    "Eq(Rational(2, 50), Rational(1, 25))",
                    "Rational(1, 25) < Rational(1, 20)",
                ],
            ),
            problem(
                "im3-u7-l3-we3",
                "A basketball player claims to make $30\\%$ of "
                "three-pointers. Design a random-digit simulation of "
                "$5$ shots, and use it to decide whether making $3$ of "
                "$5$ would contradict the claim, given that $65$ of "
                "$400$ simulated five-shot sets had $3$ or more makes.",
                "**Build the simulator.** Let digits $0, 1, 2$ be a "
                "make and $3$–$9$ a miss: three of ten digits is "
                "exactly $30\\%$. Each block of $5$ random digits is "
                "one five-shot set."
                "**Read the runs.** Three-or-more makes occurred in "
                "$\\frac{65}{400} = 16.25\\%$ of the simulated sets — "
                "common, not rare. (The exact binomial value is "
                "$16.3\\%$; the simulation landed right on it.)"
                "**Verdict.** $3$ of $5$ is entirely consistent with a "
                "$30\\%$ shooter — a hot afternoon proves nothing "
                "either way. Rarity, not success, is what carries "
                "evidence.",
                [
                    "Eq(Rational(65, 400), Rational(13, 80))",
                    "Abs(binomial(5, 3)*Rational(3, 10)**3*Rational(7, 10)**2 + binomial(5, 4)*Rational(3, 10)**4*Rational(7, 10) + Rational(3, 10)**5 - Rational(13, 80)) < Rational(1, 100)",
                    "Rational(13, 80) > Rational(1, 20)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Expecting a sample to match the population exactly.",
                "100 fair flips almost never give exactly 50 heads — "
                "wobble is the normal state of affairs, not a defect. "
                "The question is never \"did it deviate?\" but \"did it "
                "deviate by more than wobble explains?\"",
            ),
            mistake(
                "Judging a result with no reference distribution.",
                "62 heads is not surprising or unsurprising on its own — "
                "only compared against what fair coins actually produce. "
                "Simulate first; the verdict comes from where the result "
                "falls among the trials.",
            ),
            mistake(
                "Assigning digits that don't match the probability.",
                "For 30%, the hit set must be three of the ten digits "
                "(say 0, 1, 2) — not \"the digit 3\". Count the digits "
                "in the hit set and divide by ten; that fraction IS the "
                "probability being simulated.",
            ),
            mistake(
                "Running a handful of trials and calling it a "
                "distribution.",
                "Ten trials cannot reveal what happens 2% of the time. "
                "Rarity judgments need hundreds of repetitions — the "
                "picture of ordinary wobble has to be dense before an "
                "outlier can stand out against it.",
            ),
        ],
        try_it=[
            problem(
                "im3-u7-l3-t1",
                "A die claimed fair shows a six $16$ times in $60$ "
                "rolls (a fair die averages $10$). In $100$ simulated "
                "rounds of $60$ fair rolls, only $3$ rounds reached "
                "$16$ or more sixes. Judge the claim.",
                "Expected sixes: $\\frac{60}{6} = 10$; observed "
                "$\\frac{16}{60} = \\frac{4}{15}$, well above. Among "
                "fair dice, $16$-or-more sixes occurred in $3\\%$ of "
                "rounds — under the $5\\%$ habit, doubt the die: "
                "ordinary wobble rarely reaches that far.",
                [
                    "Eq(Rational(60, 6), 10)",
                    "Eq(Rational(16, 60), Rational(4, 15))",
                    "Rational(3, 100) < Rational(1, 20)",
                ],
            ),
            problem(
                "im3-u7-l3-t2",
                "A spinner claims to land blue $50\\%$ of the time. In "
                "$20$ spins it shows $13$ blues. Simulations of $20$ "
                "fair spins put the middle $95\\%$ of outcomes between "
                "$6$ and $14$ blues. Is the spinner's claim in "
                "trouble?",
                "No. $13$ blues ($\\hat{p} = 0.65$) sits inside the "
                "$6$–$14$ range that fair spinners produce $95\\%$ of "
                "the time — this is ordinary sampling wobble at $n = "
                "20$, not evidence against the claim.",
                [
                    "Eq(Rational(13, 20), Rational(65, 100))",
                    "Rational(6, 20) < Rational(13, 20)",
                    "Rational(13, 20) < Rational(14, 20)",
                ],
            ),
            problem(
                "im3-u7-l3-t3",
                "Design a random-digit simulation for polling one "
                "resident of a town where $45\\%$ support a new park, "
                "and state how many supporters a simulated sample of "
                "$20$ residents would average.",
                "Use PAIRS of digits, $00$–$99$: let $00$–$44$ mean "
                "\"supporter\" — forty-five of the hundred pairs, "
                "exactly $45\\%$ — and $45$–$99$ mean \"not\". Twenty "
                "pairs simulate the sample; it averages $0.45 \\cdot "
                "20 = 9$ supporters.",
                [
                    "Eq(Rational(45, 100), Rational(9, 20))",
                    "Eq(Rational(9, 20)*20, 9)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "Honest samples disagree",
             "body": "Flip a fair coin $100$ times: $47$ heads. Again: $53$. Again: $51$. Same coin, different statistics — SAMPLING VARIABILITY is the dance of $\\hat{p}$ around the true $p$. It is not error; it is what chance looks like. The skill of this lesson is telling ordinary wobble from something that isn't.",
             "beats": ["Same population, different samples, different $\\hat{p}$",
                       "Wobble is normal — the question is how much is normal",
                       "Bigger samples wobble less"]},
            {"kind": "worked", "title": "Sixty-two heads", "problemId": "im3-u7-l3-we1"},
            tap(
                "Is 53 heads suspicious?",
                "You flip a fair coin $100$ times and get $53$ heads "
                "instead of $50$. The right reaction is:",
                ["ordinary — statistics vary from sample to sample",
                 "strong evidence the coin is biased",
                 "impossible for a truly fair coin",
                 "the flips must be redone"],
                0,
                "$53$ is a $3$-point wobble — everyday behaviour for "
                "$100$ fair flips, as any simulation shows. Deviating "
                "from the exact mean is the rule, not the exception.",
                ["Eq(Rational(53, 100) - Rational(1, 2), Rational(3, 100))"],
            ),
            {"kind": "worked", "title": "The bag of sweets", "problemId": "im3-u7-l3-we2"},
            {"kind": "tip", "eyebrow": "The habit", "title": "Five percent is the working line",
             "body": "\"Rare under the claim\" needs a threshold, and the working convention is $5\\%$: if results as extreme as yours occur in fewer than one-twentieth of simulated trials, stop blaming wobble. It is a habit, not a law — near the line, say \"borderline\" and simulate more."},
            tap(
                "Read the simulation",
                "Under a claimed model, $250$ simulated trials were run; "
                "only $5$ were as extreme as the observed result. The "
                "observed result is:",
                ["evidence against the claim — a $2\\%$ event",
                 "consistent with the claim — $5$ trials found it",
                 "proof the simulation is broken",
                 "impossible to interpret without a formula"],
                0,
                "$\\frac{5}{250} = 2\\%$, below the $5\\%$ habit: the "
                "claimed model rarely produces such results, so the "
                "claim — not luck — is what's doubtful.",
                ["Eq(Rational(5, 250), Rational(1, 50))",
                 "Rational(1, 50) < Rational(1, 20)"],
            ),
            {"kind": "worked", "title": "Thirty-percent shooter", "problemId": "im3-u7-l3-we3"},
            {"kind": "teach", "title": "Digits as dice",
             "body": "Random digits simulate any probability: for $30\\%$, call $0,1,2$ a hit and $3$–$9$ a miss — three digits of ten. For $45\\%$, use pairs: $00$–$44$ hit, forty-five pairs of a hundred. Group digits to match the sample size, run hundreds of rounds, and the distribution of ordinary outcomes appears — the backdrop every real result is judged against.",
             "beats": ["Match the probability by COUNT of digits",
                       "$45\\%$ needs pairs: $00$–$44$",
                       "Hundreds of rounds draw the wobble's shape"]},
            {"kind": "tryIt", "title": "Sixteen sixes", "problemId": "im3-u7-l3-t1"},
            {"kind": "tryIt", "title": "The spinner's alibi", "problemId": "im3-u7-l3-t2"},
            {"kind": "tryIt", "title": "Build the simulator", "problemId": "im3-u7-l3-t3"},
            tap(
                "Pick the digits",
                "To simulate an event with probability $70\\%$ using "
                "single random digits, the correct assignment is:",
                ["$0$–$6$ hit, $7$–$9$ miss",
                 "$0$–$7$ hit, $8$–$9$ miss",
                 "the digit $7$ hits, all others miss",
                 "$0$–$6$ miss, $7$–$9$ hit"],
                0,
                "$0$–$6$ is SEVEN digits of the ten — exactly "
                "$70\\%$. Count the digits in the hit set; the digit "
                "labels themselves mean nothing.",
                ["Eq(Rational(7, 10), Rational(70, 100))"],
            ),
            {"kind": "recap", "title": "Simulation — what sticks",
             "points": [
                 "Statistics wobble from sample to sample even when nothing is wrong.",
                 "To test a claim: assume it, simulate many trials, locate the observed result.",
                 "Observed in under about 5% of trials — doubt the claim, not your luck.",
                 "Digit assignments match probabilities by count: 30% is three digits of ten.",
                 "Hundreds of trials, not a handful — rarity needs a dense backdrop.",
             ]},
        ],
    )


# ===========================================================================
# Lesson 4 — margin of error and conclusions
# ===========================================================================

def lesson_margin():
    return lesson(
        slug="margin-of-error-and-conclusions",
        title="Margin of Error & Conclusions",
        concrete=(
            "One poll says $52\\%$, another says $49\\%$ — and neither "
            "is broken. Every poll number wears an invisible $\\pm$: "
            "ask $400$ voters and the wobble is about $5$ points either "
            "way. Headlines print the point; the honest object is the "
            "interval. Learn to read the $\\pm$ and you can tell a real "
            "lead from a coin toss — and tell when an experiment's "
            "result is big enough to mean something."
        ),
        objective=(
            "Attach a margin of error to a sample proportion, read polls "
            "as intervals rather than points, shrink the margin by "
            "growing the sample, and judge whether an experiment's "
            "difference between treatments exceeds what chance "
            "re-assignment produces."
        ),
        concept=[
            "Simulation (Lesson 3) shows the wobble of $\\hat{p}$ has a "
            "predictable size, and for $95\\%$ of random samples it "
            "stays within roughly $\\frac{1}{\\sqrt{n}}$ of the truth. "
            "That number is the MARGIN OF ERROR. A poll of $400$: "
            "$\\frac{1}{\\sqrt{400}} = \\frac{1}{20} = 5$ points. The "
            "poll's honest statement is not \"$52\\%$\" but \"$52 \\pm "
            "5$\" — somewhere between $47\\%$ and $57\\%$.",

            "Conclusions live or die by the interval. \"$52 \\pm 5$\" "
            "straddles $50\\%$, so the poll CANNOT call the race — a "
            "lead smaller than the margin is a coin toss in disguise. "
            "Only when the whole interval sits on one side of the "
            "threshold does the data license a conclusion: $54 \\pm 2$ "
            "clears $50$; $52 \\pm 5$ does not.",

            "Precision is bought with sample size, at ruinous exchange "
            "rates: the $\\sqrt{n}$ downstairs means halving the "
            "margin takes FOUR times the sample. From $\\pm 5$ at "
            "$n = 400$ to $\\pm 2.5$ costs $n = 1600$. The refined "
            "formula $2\\sqrt{\\hat{p}(1 - \\hat{p})/n}$ sharpens the "
            "quick rule when $\\hat{p}$ is far from $\\frac{1}{2}$ — "
            "and equals it exactly at $\\hat{p} = \\frac{1}{2}$, the "
            "worst case.",

            "Experiments get the same treatment. Fertiliser group: "
            "$70\\%$ thrive; control: $40\\%$ — a $30$-point gap. Is "
            "that the fertiliser, or luck of the draw? RE-RANDOMISE: "
            "shuffle the same outcomes into two random groups again "
            "and again and watch what gaps pure chance produces. If "
            "shuffles reach $30$ points in only $1\\%$ of trials, the "
            "gap is SIGNIFICANT — and because the original assignment "
            "was random, the conclusion may use the word \"causes\".",
        ],
        key_idea=(
            "A poll's number is an interval, not a point — about 1/sqrt(n) "
            "wide on each side. And an experiment's gap means something "
            "only when it beats the gaps that random re-shuffling of the "
            "same data routinely makes."
        ),
        facts=[
            fact("Margin of error, quick rule",
                 "\\text{MoE} \\approx \\dfrac{1}{\\sqrt{n}}",
                 "The 95%-confidence wobble of a sample proportion — a "
                 "poll of 400 carries about 5 points."),
            fact("The honest interval",
                 "\\hat{p} - \\text{MoE} \\ \\le\\ p \\ \\le\\ \\hat{p} + \\text{MoE}",
                 "The parameter is somewhere in here (for about 95% of "
                 "samples) — report the interval, not the point."),
            fact("The fourfold rule",
                 "\\text{half the margin} \\Longleftarrow 4 \\times \\text{the sample}",
                 "The square root downstairs makes precision expensive: "
                 "halving the wobble quadruples the bill."),
            fact("Refined margin",
                 "2\\sqrt{\\dfrac{\\hat{p}(1 - \\hat{p})}{n}}",
                 "Sharper when p-hat is far from one half; equal to the "
                 "quick rule at p-hat = 1/2, its worst case."),
            fact("Significant difference",
                 "\\text{observed gap} \\gg \\text{re-randomised gaps} \\Rightarrow \\text{treatment effect}",
                 "If chance shuffles rarely match the gap, the treatment "
                 "— assigned at random — is the credible cause."),
        ],
        worked=[
            problem(
                "im3-u7-l4-we1",
                "A poll of $400$ voters finds $52\\%$ support candidate "
                "A. Attach a margin of error, give the interval, and "
                "say whether the poll shows A ahead.",
                "**Quick rule.** $\\text{MoE} \\approx \\frac{1}"
                "{\\sqrt{400}} = \\frac{1}{20} = 5$ points."
                "**The interval.** $52 \\pm 5$: support is plausibly "
                "anywhere from $47\\%$ to $57\\%$."
                "**Read it.** The interval contains $50\\%$, so the "
                "data cannot rule out a tie or worse — a $2$-point "
                "lead inside a $5$-point margin is not a lead. \"Too "
                "close to call\" is the correct headline.",
                [
                    "Eq(1/sqrt(400), Rational(1, 20))",
                    "Eq(Rational(52, 100) - Rational(1, 20), Rational(47, 100))",
                    "Eq(Rational(52, 100) + Rational(1, 20), Rational(57, 100))",
                    "Rational(47, 100) < Rational(1, 2)",
                ],
            ),
            problem(
                "im3-u7-l4-we2",
                "How many voters must be polled to cut the margin of "
                "error from $5$ points to $2.5$ points? Then check the "
                "quick rule against the refined margin "
                "$2\\sqrt{\\hat{p}(1-\\hat{p})/n}$ at $\\hat{p} = "
                "\\frac{1}{2}$, $n = 400$.",
                "**Invert the rule.** $\\frac{1}{\\sqrt{n}} = "
                "\\frac{1}{40}$ requires $n = 1600$ — QUADRUPLE the "
                "$400$, for half the margin. The square root "
                "downstairs makes every halving cost a factor of "
                "four."
                "**Check the refinement.** At $\\hat{p} = \\frac{1}"
                "{2}$: $2\\sqrt{\\frac{(1/2)(1/2)}{400}} = "
                "2\\sqrt{\\frac{1}{1600}} = \\frac{2}{40} = "
                "\\frac{1}{20}$ — exactly the quick rule. The quick "
                "rule IS the refined formula at its worst case, which "
                "is why it's a safe default.",
                [
                    "Eq(1/sqrt(1600), Rational(1, 40))",
                    "Eq(Rational(1600, 400), 4)",
                    "Eq(2*sqrt(Rational(1, 4)/400), Rational(1, 20))",
                ],
            ),
            problem(
                "im3-u7-l4-we3",
                "Eighty seedlings are randomly split $40$–$40$; the "
                "fertilised group has $28$ thrive, the control $16$. "
                "Re-randomising the same $44$ thrive/$36$ fail labels "
                "into random groups $200$ times produced a gap of "
                "$30$ points or more only $2$ times. What may be "
                "concluded?",
                "**The gap.** Fertilised: $\\frac{28}{40} = 70\\%$; "
                "control: $\\frac{16}{40} = 40\\%$; difference $30$ "
                "points."
                "**Chance's best effort.** Shuffling the same "
                "outcomes into random groups produced $30$-point gaps "
                "in $\\frac{2}{200} = 1\\%$ of trials — chance almost "
                "never does this on its own."
                "**The verdict.** The gap is significant, and because "
                "the ORIGINAL groups were formed by random "
                "assignment, the cause is the fertiliser — this is "
                "the full S-IC.5 argument, end to end.",
                [
                    "Eq(Rational(28, 40), Rational(7, 10))",
                    "Eq(Rational(16, 40), Rational(2, 5))",
                    "Eq(Rational(7, 10) - Rational(2, 5), Rational(3, 10))",
                    "Eq(Rational(2, 200), Rational(1, 100))",
                    "Rational(1, 100) < Rational(1, 20)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reading a poll as an exact number.",
                "\"52%\" from 400 voters means \"somewhere around 47% "
                "to 57%\". The headline prints the point; the "
                "information is the interval. Any conclusion that "
                "ignores the margin is reading noise.",
            ),
            mistake(
                "Doubling the sample to halve the margin.",
                "The n sits under a square root: halving the margin "
                "needs FOUR times the sample. Doubling only shrinks "
                "the margin by a factor of sqrt(2) — about 30% off, "
                "not 50%.",
            ),
            mistake(
                "Declaring a winner inside the margin.",
                "If the interval straddles the threshold (50%, or the "
                "rival's interval), the data cannot call it. A lead "
                "smaller than the margin of error is a coin toss "
                "wearing a suit.",
            ),
            mistake(
                "Using the margin of error to excuse a biased sample.",
                "The MoE prices CHANCE wobble in a random sample — "
                "nothing else. It cannot repair a volunteer poll or a "
                "convenience sample; bias is outside its jurisdiction "
                "entirely.",
            ),
        ],
        try_it=[
            problem(
                "im3-u7-l4-t1",
                "A survey of $100$ students finds $56\\%$ prefer later "
                "lunches. Give the margin of error and the interval. "
                "Can the school conclude a majority prefers the "
                "change?",
                "$\\text{MoE} \\approx \\frac{1}{\\sqrt{100}} = 10$ "
                "points, so the interval is $46\\%$ to $66\\%$. It "
                "contains $50\\%$ — no majority conclusion; a sample "
                "of $100$ is simply too coarse for a $6$-point lead.",
                [
                    "Eq(1/sqrt(100), Rational(1, 10))",
                    "Eq(Rational(56, 100) - Rational(1, 10), Rational(46, 100))",
                    "Eq(Rational(56, 100) + Rational(1, 10), Rational(66, 100))",
                ],
            ),
            problem(
                "im3-u7-l4-t2",
                "A sample of $100$ has $\\hat{p} = 0.8$. Compute the "
                "refined margin $2\\sqrt{\\hat{p}(1 - \\hat{p})/n}$ "
                "and compare it with the quick rule.",
                "$2\\sqrt{\\frac{0.8 \\cdot 0.2}{100}} = "
                "2\\sqrt{\\frac{0.16}{100}} = 2 \\cdot \\frac{0.4}"
                "{10} = 0.08$ — eight points, sharper than the quick "
                "rule's $\\frac{1}{\\sqrt{100}} = 10$. The further "
                "$\\hat{p}$ sits from $\\frac{1}{2}$, the more the "
                "quick rule overstates the wobble.",
                [
                    "Eq(2*sqrt(Rational(16, 100)/100), Rational(2, 25))",
                    "Eq(Rational(2, 25), Rational(8, 100))",
                    "Rational(2, 25) < Rational(1, 10)",
                ],
            ),
            problem(
                "im3-u7-l4-t3",
                "A website's volunteer poll of $5000$ readers reports "
                "$60\\%$ support for a policy; a random sample of "
                "$400$ residents finds $45\\%$. Using margins of "
                "error, decide whether the two results can be "
                "reconciled — and which deserves the headline.",
                "The random sample carries $\\text{MoE} \\approx "
                "\\frac{1}{\\sqrt{400}} = 5$ points: interval "
                "$40\\%$–$50\\%$. Even its top end falls short of "
                "$60\\%$, so wobble cannot reconcile the two — the "
                "volunteer poll is biased, and its $5000$ responses "
                "make it precise about the wrong population. The "
                "random $45 \\pm 5$ deserves the headline.",
                [
                    "Eq(1/sqrt(400), Rational(1, 20))",
                    "Rational(45, 100) + Rational(1, 20) < Rational(60, 100)",
                ],
            ),
        ],
        steps=[
            {"kind": "teach", "title": "The invisible plus-minus",
             "body": "Lesson 3's simulations show the wobble of a sample proportion has a size — and for $95\\%$ of random samples it stays within about $\\frac{1}{\\sqrt{n}}$ of the truth. That is the MARGIN OF ERROR. A poll of $400$ voters: $\\frac{1}{\\sqrt{400}} = 5$ points. \"$52\\%$\" honestly means \"$47\\%$ to $57\\%$\".",
             "beats": ["$\\text{MoE} \\approx \\dfrac{1}{\\sqrt{n}}$",
                       "$n = 400 \\Rightarrow \\pm 5$ points",
                       "The poll's real answer is an interval"]},
            {"kind": "worked", "title": "Too close to call", "problemId": "im3-u7-l4-we1"},
            tap(
                "The quick margin",
                "A poll samples $2500$ people. Its margin of error is "
                "about:",
                ["$2\\%$", "$4\\%$", "$50\\%$", "$0.04\\%$"],
                0,
                "$\\frac{1}{\\sqrt{2500}} = \\frac{1}{50} = 2\\%$ — "
                "twenty-five hundred people buy a two-point margin.",
                ["Eq(1/sqrt(2500), Rational(1, 50))"],
            ),
            {"kind": "worked", "title": "The price of precision", "problemId": "im3-u7-l4-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "The margin cannot fix bias",
             "body": "$\\frac{1}{\\sqrt{n}}$ prices the CHANCE wobble of a random sample — that is all. A volunteer poll of $5000$ has a tiny margin around the wrong answer: precisely wrong beats vaguely right only in headlines. Check the sampling method before trusting any interval."},
            tap(
                "Call it or not?",
                "A poll of $400$ gives candidate A $53\\%$ — margin of "
                "error $5$ points. The honest conclusion is:",
                ["too close to call — the interval contains $50\\%$",
                 "A wins — $53$ is more than $50$",
                 "A loses — polls always overstate",
                 "the poll must be redone with $401$ people"],
                0,
                "$53 \\pm 5$ runs from $48\\%$ to $58\\%$ — both sides "
                "of $50$. A lead smaller than the margin is a coin "
                "toss in a suit.",
                ["Rational(53, 100) - Rational(5, 100) < Rational(1, 2)"],
            ),
            {"kind": "worked", "title": "Does the fertiliser work?", "problemId": "im3-u7-l4-we3"},
            {"kind": "teach", "title": "Shuffling the labels",
             "body": "An experiment's gap gets the simulation treatment: RE-RANDOMISE the same outcomes into two random groups, over and over, and see what gaps chance manufactures. If the observed gap beats nearly all of them — under the $5\\%$ habit — it is significant. And because the real groups were formed by coin flip, the conclusion is causal: the treatment did it.",
             "beats": ["Shuffle outcomes into random groups, many times",
                       "Observed gap rare among shuffles $\\Rightarrow$ significant",
                       "Random assignment upgrades \"significant\" to \"causal\""]},
            {"kind": "tryIt", "title": "Majority or not?", "problemId": "im3-u7-l4-t1"},
            {"kind": "tryIt", "title": "The refined margin", "problemId": "im3-u7-l4-t2"},
            {"kind": "tryIt", "title": "Duelling polls", "problemId": "im3-u7-l4-t3"},
            tap(
                "What shrinks the wobble?",
                "A pollster wants to cut the margin of error from "
                "$4\\%$ to $2\\%$. The sample must be:",
                ["four times as large",
                 "twice as large",
                 "one hundred people larger",
                 "replaced by two polls of the same size"],
                0,
                "The margin runs as $\\frac{1}{\\sqrt{n}}$: from "
                "$n = 625$ ($4\\%$) to $n = 2500$ ($2\\%$) — a factor "
                "of four in sample for a factor of two in margin.",
                ["Eq(1/sqrt(625), Rational(1, 25))",
                 "Eq(Rational(2500, 625), 4)"],
            ),
            {"kind": "recap", "title": "Margin of error — what sticks",
             "points": [
                 "Every sample proportion wears a margin of about 1/sqrt(n) on each side.",
                 "Conclusions need the WHOLE interval on one side of the threshold.",
                 "Halving the margin quadruples the sample — precision is expensive.",
                 "The margin prices chance wobble only; it cannot repair a biased sample.",
                 "Experiment gaps are judged by re-randomisation — rare gap + random assignment = causal conclusion.",
             ]},
        ],
    )


# ===========================================================================
# Practice bank
# ===========================================================================

def practice_bank():
    return [
        problem(
            "im3-u7-p1",
            "A city of $40000$ households wants to know how many "
            "recycle. In a random sample of $200$ households, $68$ "
            "recycle. Name the parameter being estimated, and estimate "
            "it — first as a proportion, then as a count.",
            "The parameter is the true proportion of the $40000$ "
            "households that recycle. The statistic estimating it is "
            "$\\hat{p} = \\frac{68}{200} = \\frac{17}{50} = 0.34$ — so "
            "an estimated $0.34 \\cdot 40000 = 13600$ households "
            "recycle.",
            [
                "Eq(Rational(68, 200), Rational(17, 50))",
                "Eq(Rational(17, 50)*40000, 13600)",
            ],
        ),
        problem(
            "im3-u7-p2",
            "A cafeteria manager surveys students standing in the lunch "
            "line about cafeteria food; $33$ of $44$ are satisfied. "
            "Compute the proportion and name the flaw in generalising "
            "it to all students.",
            "$\\frac{33}{44} = \\frac{3}{4} = 75\\%$ — of students IN "
            "THE LINE. That is a convenience sample biased toward "
            "students who chose to eat there today; students who avoid "
            "the cafeteria (the most dissatisfied group) cannot appear "
            "in it at all. Only a random sample of the whole school "
            "estimates the school-wide proportion.",
            [
                "Eq(Rational(33, 44), Rational(3, 4))",
            ],
        ),
        problem(
            "im3-u7-p3",
            "Classify each study: (a) $500$ commuters are asked how "
            "they travel to work; (b) accident rates are compared "
            "between drivers who already own red cars and drivers who "
            "don't; (c) $90$ patients are randomly assigned, $45$ and "
            "$45$, to a new drug or a placebo. Which can support a "
            "causal conclusion?",
            "(a) asks — a survey. (b) watches self-formed groups — an "
            "observational study. (c) imposes treatment by random "
            "assignment ($\\frac{90}{2} = 45$ each) — an experiment, "
            "and the only one of the three whose result can be read "
            "causally: red-car owners may differ from others in driving "
            "style, age, or mileage, but the randomised halves differ "
            "on average in nothing but the drug.",
            [
                "Eq(Rational(90, 2), 45)",
                "Eq(45 + 45, 90)",
            ],
        ),
        problem(
            "im3-u7-p4",
            "A school has $300$ ninth-graders and $200$ tenth-graders. "
            "A sample of $50$ is to represent both grades in "
            "proportion. How many students should come from each "
            "grade?",
            "Ninth grade is $\\frac{300}{500}$ of the school: $\\frac{300}"
            "{500} \\cdot 50 = 30$ students. Tenth grade: $\\frac{200}"
            "{500} \\cdot 50 = 20$. Sampling each grade separately in "
            "proportion (a stratified sample) guarantees the blend "
            "matches the school instead of leaving it to luck.",
            [
                "Eq(Rational(300, 500)*50, 30)",
                "Eq(Rational(200, 500)*50, 20)",
            ],
        ),
        problem(
            "im3-u7-p5",
            "IQ scores are approximately normal with mean $100$ and "
            "standard deviation $15$. Between which values do the "
            "middle $68\\%$ fall? The middle $95\\%$?",
            "One standard deviation: $100 \\pm 15$ gives $85$ to "
            "$115$ — the middle $68\\%$. Two: $100 \\pm 30$ gives "
            "$70$ to $130$ — the middle $95\\%$.",
            [
                "Eq(100 - 15, 85)",
                "Eq(100 + 15, 115)",
                "Eq(100 - 2*15, 70)",
                "Eq(100 + 2*15, 130)",
            ],
        ),
        problem(
            "im3-u7-p6",
            "Bat scored $130$ on an IQ-style test ($\\mu = 100$, "
            "$\\sigma = 15$) and $620$ on an entrance exam ($\\mu = "
            "500$, $\\sigma = 100$). On which test did he place "
            "relatively higher?",
            "IQ: $z = \\frac{130 - 100}{15} = 2$. Entrance exam: $z = "
            "\\frac{620 - 500}{100} = 1.2$. Two full standard "
            "deviations beats $1.2$ — the IQ score is the rarer, "
            "relatively higher result, even though $620$ is the bigger "
            "number.",
            [
                "Eq(Rational(130 - 100, 15), 2)",
                "Eq(Rational(620 - 500, 100), Rational(6, 5))",
                "2 > Rational(6, 5)",
            ],
        ),
        problem(
            "im3-u7-p7",
            "Quiz scores are approximately normal with mean $75$ and "
            "standard deviation $6$. Of $250$ students, about how many "
            "scored below $69$?",
            "$69 = 75 - 6$ is one standard deviation below the mean; "
            "the tail below it holds $\\frac{100 - 68}{2} = 16\\%$. "
            "Count: $0.16 \\cdot 250 = 40$ students.",
            [
                "Eq(75 - 6, 69)",
                "Eq(Rational(100 - 68, 2), 16)",
                "Eq(Rational(16, 100)*250, 40)",
            ],
        ),
        problem(
            "im3-u7-p8",
            "A machine part's length is normal with mean $40$ mm and "
            "standard deviation $4$ mm. Parts outside $\\mu \\pm "
            "3\\sigma$ are scrapped. State the scrap limits, and "
            "estimate the scrapped count in a run of $1000$ parts.",
            "Limits: $40 - 12 = 28$ mm and $40 + 12 = 52$ mm. The "
            "rule keeps $99.7\\%$ inside three standard deviations, so "
            "$0.3\\%$ is scrapped: about $\\frac{3}{1000} \\cdot 1000 "
            "= 3$ parts per thousand.",
            [
                "Eq(40 - 3*4, 28)",
                "Eq(40 + 3*4, 52)",
                "Eq(Rational(3, 1000)*1000, 3)",
            ],
        ),
        problem(
            "im3-u7-p9",
            "A distribution has mean $70$ and standard deviation $8$. "
            "Find the values whose z-scores are $1.5$ and $-2$.",
            "Forwards from the mean: $x = 70 + 1.5 \\cdot 8 = 82$, "
            "and $x = 70 - 2 \\cdot 8 = 54$. The z-score is a recipe: "
            "start at the mean, walk $z$ standard deviations.",
            [
                "Eq(70 + Rational(3, 2)*8, 82)",
                "Eq(70 - 2*8, 54)",
            ],
        ),
        problem(
            "im3-u7-p10",
            "A cereal brand claims a prize in $1$ of every $4$ boxes. "
            "In $40$ boxes bought, only $4$ had prizes. In $250$ "
            "simulations of $40$ boxes at the claimed rate, $8$ "
            "trials had $4$ or fewer prizes. Judge the claim.",
            "The claim predicts $\\frac{1}{4} \\cdot 40 = 10$ prizes "
            "on average; $4$ is far below. Among simulated honest "
            "runs, $4$-or-fewer occurred in $\\frac{8}{250} = 3.2\\%$ "
            "of trials — under the $5\\%$ habit. The shortfall is too "
            "rare to blame on wobble; doubt the one-in-four claim.",
            [
                "Eq(Rational(1, 4)*40, 10)",
                "Eq(Rational(8, 250), Rational(4, 125))",
                "Rational(4, 125) < Rational(1, 20)",
            ],
        ),
        problem(
            "im3-u7-p11",
            "Design a simulation, using pairs of random digits, for "
            "sampling one voter from a town where $35\\%$ favour a "
            "bond measure — and state the average number of "
            "favourable voters in simulated samples of $20$.",
            "Pairs $00$–$99$: let $00$–$34$ mean \"favours\" — "
            "thirty-five pairs of the hundred, exactly $35\\%$ — and "
            "$35$–$99$ mean \"does not\". Twenty pairs make one "
            "sample; the average count is $0.35 \\cdot 20 = 7$ "
            "favourable voters.",
            [
                "Eq(Rational(35, 100), Rational(7, 20))",
                "Eq(Rational(35, 100)*20, 7)",
            ],
        ),
        problem(
            "im3-u7-p12",
            "Two pollsters sample the same population: one asks $100$ "
            "people, the other $400$. Compare the spreads of their "
            "sample proportions.",
            "Spread scales as $\\frac{1}{\\sqrt{n}}$: "
            "$\\frac{1/\\sqrt{100}}{1/\\sqrt{400}} = \\frac{20}{10} = "
            "2$. The $100$-person poll wobbles twice as much — "
            "quadrupling the sample halves the spread, which is the "
            "square-root law that runs the whole unit.",
            [
                "Eq((1/sqrt(100))/(1/sqrt(400)), 2)",
            ],
        ),
        problem(
            "im3-u7-p13",
            "A poll of $2500$ residents finds $54\\%$ support a new "
            "library. Give the margin of error and interval. May the "
            "town conclude majority support?",
            "$\\text{MoE} \\approx \\frac{1}{\\sqrt{2500}} = "
            "\\frac{1}{50} = 2$ points: interval $52\\%$ to $56\\%$. "
            "The ENTIRE interval sits above $50\\%$, so yes — "
            "majority support is a safe conclusion at this sample "
            "size (contrast $n = 400$, whose $5$-point margin would "
            "have straddled $50$).",
            [
                "Eq(1/sqrt(2500), Rational(1, 50))",
                "Eq(Rational(54, 100) - Rational(1, 50), Rational(52, 100))",
                "Rational(52, 100) > Rational(1, 2)",
            ],
        ),
        problem(
            "im3-u7-p14",
            "A newspaper wants poll results with a margin of error of "
            "$4$ points. About how many people must it sample?",
            "Set $\\frac{1}{\\sqrt{n}} = 0.04 = \\frac{1}{25}$: then "
            "$\\sqrt{n} = 25$, so $n = 625$. Check: $\\frac{1}"
            "{\\sqrt{625}} = \\frac{1}{25} = 4\\%$.",
            [
                "Eq(1/sqrt(625), Rational(1, 25))",
                "Eq(Rational(1, 25), Rational(4, 100))",
            ],
        ),
        problem(
            "im3-u7-p15",
            "Sixty students are randomly assigned, $30$ and $30$, to "
            "a new study method or the usual one. Pass counts: $24$ "
            "of $30$ against $15$ of $30$. Re-randomising the same "
            "outcomes $150$ times produced a gap at least this large "
            "$3$ times. What can be concluded?",
            "New method: $\\frac{24}{30} = 80\\%$; usual: $\\frac{15}"
            "{30} = 50\\%$; gap $30$ points. Chance shuffles matched "
            "it in $\\frac{3}{150} = 2\\%$ of trials — significant "
            "under the $5\\%$ habit. Because assignment was random, "
            "the conclusion is causal: the new method raised the pass "
            "rate.",
            [
                "Eq(Rational(24, 30), Rational(4, 5))",
                "Eq(Rational(15, 30), Rational(1, 2))",
                "Eq(Rational(4, 5) - Rational(1, 2), Rational(3, 10))",
                "Eq(Rational(3, 150), Rational(1, 50))",
                "Rational(1, 50) < Rational(1, 20)",
            ],
        ),
        problem(
            "im3-u7-p16",
            "Two candidates poll at $48\\%$ and $52\\%$, each with a "
            "margin of error of $3$ points. A pundit declares the "
            "second candidate \"clearly ahead\". Evaluate.",
            "The intervals are $45$–$51$ and $49$–$55$ — they "
            "OVERLAP ($51 > 49$), so the data are consistent with "
            "either candidate leading. \"Clearly ahead\" overstates a "
            "$4$-point gap carried by $6$ points of combined wobble; "
            "the honest call is \"too close to call\".",
            [
                "Eq(Rational(48, 100) + Rational(3, 100), Rational(51, 100))",
                "Eq(Rational(52, 100) - Rational(3, 100), Rational(49, 100))",
                "Rational(51, 100) > Rational(49, 100)",
            ],
        ),
    ]


# ===========================================================================
# Test bank
# ===========================================================================

def test_bank():
    return [
        problem(
            "im3-u7-x1",
            "A school of $1400$ students samples $35$ at random; $21$ "
            "ride the bus. Identify the statistic, and estimate the "
            "school-wide number of bus riders.",
            "The statistic is $\\hat{p} = \\frac{21}{35} = \\frac{3}"
            "{5} = 0.6$ — computed from the sample, estimating the "
            "unknown school-wide parameter. Scaled up: $0.6 \\cdot "
            "1400 = 840$ bus riders, give or take the sampling "
            "wobble.",
            [
                "Eq(Rational(21, 35), Rational(3, 5))",
                "Eq(Rational(3, 5)*1400, 840)",
            ],
        ),
        problem(
            "im3-u7-x2",
            "Three studies of a memory-training app: (a) users are "
            "surveyed about whether they feel sharper; (b) test "
            "scores of $56$ existing users are compared with $56$ "
            "non-users; (c) $56$ volunteers are randomly split "
            "$28$–$28$, half assigned the app. Which design permits "
            "the conclusion \"the app improves scores\", and why "
            "only that one?",
            "(a) is a survey, (b) an observational study, (c) an "
            "experiment. Only (c): its random split ($\\frac{56}{2} = "
            "28$ per group) makes the groups alike on average in "
            "motivation, age, and everything hidden, so a score gap "
            "can be pinned on the app. In (b), people who CHOSE the "
            "app likely differ from non-users in ways that also move "
            "test scores.",
            [
                "Eq(Rational(56, 2), 28)",
                "Eq(28 + 28, 56)",
            ],
        ),
        problem(
            "im3-u7-x3",
            "Delivery times are approximately normal with mean $30$ "
            "minutes and standard deviation $5$. What percent of "
            "deliveries take $20$ to $40$ minutes? Of $800$ "
            "deliveries, about how many take longer than $40$ "
            "minutes?",
            "$20 = 30 - 10$ and $40 = 30 + 10$ are $\\mu \\pm "
            "2\\sigma$: about $95\\%$. Beyond $40$ is one tail of "
            "$\\frac{100 - 95}{2} = 2.5\\%$: about $0.025 \\cdot 800 "
            "= 20$ deliveries.",
            [
                "Eq(30 - 2*5, 20)",
                "Eq(30 + 2*5, 40)",
                "Eq(Rational(100 - 95, 2), Rational(5, 2))",
                "Eq(Rational(5, 2)/100*800, 20)",
            ],
        ),
        problem(
            "im3-u7-x4",
            "Tuya scored $88$ on a test with mean $80$ and standard "
            "deviation $5$; Dorj scored $84$ on a test with mean $72$ "
            "and standard deviation $8$. Who placed relatively "
            "higher?",
            "Tuya: $z = \\frac{88 - 80}{5} = 1.6$. Dorj: $z = "
            "\\frac{84 - 72}{8} = 1.5$. Tuya, narrowly — $1.6 > 1.5$ "
            "standard deviations above their respective means. The "
            "raw four-point difference in scores decided nothing; the "
            "z-scores did.",
            [
                "Eq(Rational(88 - 80, 5), Rational(8, 5))",
                "Eq(Rational(84 - 72, 8), Rational(3, 2))",
                "Rational(8, 5) > Rational(3, 2)",
            ],
        ),
        problem(
            "im3-u7-x5",
            "A seed packet claims $50\\%$ germination. Of $40$ seeds "
            "planted, only $12$ sprout. In $200$ simulations at the "
            "claimed rate, $3$ trials had $12$ or fewer sprouts. "
            "Judge the claim.",
            "The claim predicts $0.5 \\cdot 40 = 20$ sprouts on "
            "average; $12$ ($\\hat{p} = 0.3$) is far below. Honest "
            "packets produced $12$-or-fewer in $\\frac{3}{200} = "
            "1.5\\%$ of simulations — well under the $5\\%$ habit. "
            "The germination claim is in serious doubt.",
            [
                "Eq(Rational(1, 2)*40, 20)",
                "Eq(Rational(12, 40), Rational(3, 10))",
                "Rational(3, 200) < Rational(1, 20)",
            ],
        ),
        problem(
            "im3-u7-x6",
            "Design a single-digit simulation for a town where "
            "$60\\%$ support a measure, and give the expected number "
            "of supporters in a simulated sample of $25$.",
            "Digits $0$–$5$ mean \"supports\" — six of the ten "
            "digits, exactly $60\\%$ — and $6$–$9$ mean \"does "
            "not\". Twenty-five digits make one sample, averaging "
            "$0.6 \\cdot 25 = 15$ supporters.",
            [
                "Eq(Rational(6, 10), Rational(60, 100))",
                "Eq(Rational(60, 100)*25, 15)",
            ],
        ),
        problem(
            "im3-u7-x7",
            "A poll of $625$ residents finds $58\\%$ favour a "
            "recycling ordinance. Give the margin of error and "
            "interval, and state what may be concluded.",
            "$\\text{MoE} \\approx \\frac{1}{\\sqrt{625}} = "
            "\\frac{1}{25} = 4$ points: interval $54\\%$ to $62\\%$. "
            "The whole interval clears $50\\%$, so majority support "
            "is a sound conclusion — the lead ($8$ points) is twice "
            "the margin.",
            [
                "Eq(1/sqrt(625), Rational(1, 25))",
                "Eq(Rational(58, 100) - Rational(1, 25), Rational(54, 100))",
                "Rational(54, 100) > Rational(1, 2)",
            ],
        ),
        problem(
            "im3-u7-x8",
            "One hundred plants are randomly assigned $50$–$50$ to a "
            "new grow light or sunlight. Flowering counts: $32$ of "
            "$50$ under the light, $22$ of $50$ in sun. "
            "Re-randomising the outcomes $300$ times matched the "
            "observed gap only $12$ times. Complete the inference.",
            "Gap: $\\frac{32}{50} = 64\\%$ against $\\frac{22}{50} = "
            "44\\%$ — twenty points. Chance shuffles reached it in "
            "$\\frac{12}{300} = 4\\%$ of trials, under the $5\\%$ "
            "line: significant. Random assignment converts that into "
            "a causal verdict — the grow light increased flowering. "
            "(At $4\\%$, only just — a cautious report would call for "
            "replication.)",
            [
                "Eq(Rational(32, 50), Rational(16, 25))",
                "Eq(Rational(22, 50), Rational(11, 25))",
                "Eq(Rational(16, 25) - Rational(11, 25), Rational(1, 5))",
                "Eq(Rational(12, 300), Rational(1, 25))",
                "Rational(1, 25) < Rational(1, 20)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="statistical-inference",
        title="Statistical Inference",
        unit_number=7,
        blurb=(
            "Populations against samples, random sampling and why it "
            "matters, the normal model, simulation, margin of error, and "
            "what an experiment can conclude that an observational study "
            "cannot."
        ),
        builds_on=(
            "Describing data from IM1 Unit 9 — from summarising a sample "
            "to inferring about a population."
        ),
        lessons=[
            lesson_samples(),
            lesson_normal(),
            lesson_simulation(),
            lesson_margin(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
