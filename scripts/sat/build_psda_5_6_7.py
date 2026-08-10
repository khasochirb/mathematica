#!/usr/bin/env python3
"""SAT Math — Problem-Solving and Data Analysis, Units 5-7.

Builds:
  data/genmath/sat/probability-and-conditional-probability.json
  data/genmath/sat/inference-and-margin-of-error.json
  data/genmath/sat/evaluating-statistical-claims.json

The last of these is a single lesson. The College Board's subtopic is one
idea — what a study design does and does not license you to claim — and
stretching it across three lessons would misrepresent it.

Run: python3 scripts/sat/build_psda_5_6_7.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
PROB_TAG = {"text": "sat-probability", "mono": True}
INF_TAG = {"text": "sat-inference-margin-error", "mono": True}
CLAIM_TAG = {"text": "sat-claims-study-design", "mono": True}


def _b(tag, level):
    return [tag, {"text": level}]


TWO_WAY = (
    "|  | Passed | Failed | Total |\n"
    "| --- | --- | --- | --- |\n"
    "| Studied | $48$ | $12$ | $60$ |\n"
    "| Did not study | $18$ | $22$ | $40$ |\n"
    "| Total | $66$ | $34$ | $100$ |\n\n"
)


# ===========================================================================
# UNIT 5 — Probability and conditional probability
# ===========================================================================

def lesson_probability():
    worked = [
        problem(
            "sat-pr1-w1",
            "The table shows results for $100$ students.\n\n" + TWO_WAY +
            "If a student is selected at random, what is the probability that the student "
            "passed?",
            "**Answer.** $\\dfrac{66}{100} = 0.66$.  \n"
            "A probability is a count of the outcomes you want over a count of all the "
            "outcomes available. 'Selected at random' from the whole group means every one of "
            "the $100$ students is equally likely, so the denominator is the GRAND total:\n"
            "$$P(\\text{passed}) = \\frac{66}{100} = 0.66$$\n"
            "Reading the count is the only real work. The $66$ is the column total for "
            "'Passed' — it combines the $48$ who studied and passed with the $18$ who did not "
            "study and passed.  \n"
            "Using $48$ alone gives $0.48$ and answers a narrower question: the probability of "
            "having both studied AND passed. Both numbers are on the option list, and the "
            "difference between them is exactly what the next lesson is about.",
            [
                "Eq(48 + 18, 66)",
                "Eq(12 + 22, 34)",
                "Eq(66 + 34, 100)",
                "Eq(Rational(66,100), Rational(33,50))",
            ],
        ),
        problem(
            "sat-pr1-w2",
            "Using the same table, what is the probability that a randomly selected student "
            "studied OR passed?",
            "**Answer.** $\\dfrac{78}{100} = 0.78$.  \n"
            "'Or' in probability means at least one of the two, so it includes students who "
            "did both. Adding the two groups directly double-counts them:\n"
            "$$60 + 66 = 126$$\n"
            "which is more than the $100$ students who exist. The $48$ who both studied and "
            "passed have been counted twice, so subtract them once:\n"
            "$$P(\\text{studied or passed}) = \\frac{60 + 66 - 48}{100} = \\frac{78}{100} = 0.78$$\n"
            "Check by counting directly from the table. Everyone qualifies except the students "
            "who neither studied nor passed — that is the $22$ in the bottom-right cell — so "
            "$100 - 22 = 78$ students qualify. Both routes agree.  \n"
            "The subtraction is the whole rule. Skipping it gives $1.26$, a probability greater "
            "than one, which is itself a signal that something has been counted twice.",
            [
                "Eq(60 + 66 - 48, 78)",
                "Eq(100 - 22, 78)",
                "Eq(Rational(78,100), Rational(39,50))",
                "Rational(60 + 66, 100) > 1",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-pr1-t1",
            "Using the table above, what is the probability that a randomly selected student "
            "did not study?",
            "**Answer.** $0.40$. The row total for 'Did not study' is $40$, out of $100$ "
            "students.",
            ["Eq(18 + 22, 40)", "Eq(Rational(40,100), Rational(2,5))"],
        ),
        problem(
            "sat-pr1-t2",
            "Using the table above, what is the probability that a randomly selected student "
            "both studied and failed?",
            "**Answer.** $0.12$. That is a single cell — the intersection of the 'Studied' row "
            "and the 'Failed' column — over the grand total of $100$.",
            ["Eq(Rational(12,100), Rational(3,25))"],
        ),
        problem(
            "sat-pr1-t3",
            "A bag holds $5$ red, $3$ blue and $12$ green counters. What is the probability of "
            "drawing a counter that is NOT green?",
            "**Answer.** $0.4$. There are $20$ counters in total and $8$ are not green, giving "
            "$\\frac{8}{20} = 0.4$. Equivalently, $1 - \\frac{12}{20} = 0.4$ — the complement "
            "rule, which is faster when the unwanted group is the easier one to count.",
            [
                "Eq(5 + 3 + 12, 20)",
                "Eq(Rational(5 + 3, 20), Rational(2,5))",
                "Eq(1 - Rational(12,20), Rational(2,5))",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Probability and conditional probability",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "Usually 1 question, and it nearly always arrives as a two-way table.",
                "Prerequisite: fractions and percentages.",
                "There is no formula to memorise — the work is choosing the right denominator.",
            ],
        },
        {
            "kind": "teach",
            "title": "Wanted over available",
            "body": "A probability is the number of outcomes you want divided by the number "
                    "available. On the SAT the counts are almost always in a two-way table, so "
                    "the arithmetic is trivial and the whole question is which two numbers to "
                    "use. Read the sentence carefully: it tells you the numerator, and — less "
                    "obviously — it tells you the denominator too.",
        },
        {
            "kind": "vennCounts",
            "title": "Why 'or' subtracts the overlap",
            "teach": "Two overlapping groups. Adding their sizes counts the overlap twice, so "
                     "the total for 'in at least one group' is the sum minus the overlap. Drag "
                     "the counts and watch the total refuse to exceed the whole.",
            "config": {
                "mode": "addition",
                "labelA": "Studied",
                "labelB": "Passed",
                "onlyA": 12,
                "both": 48,
                "onlyB": 18,
                "neither": 22,
                "countNoun": "students",
            },
        },
        {"kind": "worked", "title": "Reading a total off the table", "problemId": "sat-pr1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which denominator?",
            "prompt": "From the table of $100$ students, what is the probability that a "
                      "randomly selected student studied?",
            "options": [
                "$\\dfrac{60}{100}$",
                "$\\dfrac{48}{100}$",
                "$\\dfrac{48}{60}$",
                "$\\dfrac{60}{66}$",
            ],
            "correctIndex": 0,
            "explanation": "The selection is from ALL $100$ students, so the denominator is "
                           "$100$, and the number who studied is the row total $60$. Option B "
                           "uses only those who studied and passed; C and D restrict the "
                           "denominator to a subgroup, which answers a conditional question "
                           "instead.",
            "check": ["Eq(48 + 12, 60)", "Eq(Rational(60,100), Rational(3,5))"],
        },
        {
            "kind": "teach",
            "title": "And, or, and not",
            "beats": [
                "'And' is a single cell — the intersection of one row and one column.",
                "'Or' means at least one, so add the two groups and subtract the overlap once.",
                "'Not' is the complement: one minus the probability of the thing.",
                "If an 'or' answer exceeds 1, the overlap was counted twice.",
            ],
        },
        {"kind": "worked", "title": "The overlap, counted once", "problemId": "sat-pr1-w2"},
        {
            "kind": "tip",
            "title": "Count the complement when it is smaller",
            "body": "'What is the probability of NOT green' with twelve green out of twenty is "
                    "faster as $1 - \\frac{12}{20}$ than as $\\frac{5 + 3}{20}$ — and with "
                    "more categories the saving grows. Whenever the unwanted group is easier "
                    "to count than the wanted one, count it and subtract from $1$.",
        },
        {"kind": "tryIt", "title": "Your turn: a row total", "problemId": "sat-pr1-t1"},
        {"kind": "tryIt", "title": "Your turn: a single cell", "problemId": "sat-pr1-t2"},
        {"kind": "tryIt", "title": "Your turn: the complement", "problemId": "sat-pr1-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Probability is wanted over available — the sentence names both.",
                "'And' is one cell; 'or' is the sum of two groups minus their overlap.",
                "'Not' is 1 minus the probability, and is often the faster count.",
                "A probability above 1 means the overlap was double-counted.",
                "Read row totals and column totals off the table rather than re-adding cells.",
            ],
        },
    ]

    return lesson(
        slug="probability-from-tables",
        title="Probability from Two-Way Tables",
        concrete=(
            "A hundred students, sorted by whether they studied and whether they passed. Every "
            "probability question anyone can ask about that group is already sitting in the "
            "table — the only difficulty is deciding which two numbers to divide."
        ),
        objective=(
            "Compute probabilities from a two-way table, including 'and', 'or' and "
            "complement questions, choosing the correct denominator each time."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Probability and conditional "
            "probability*, in the **Problem-Solving and Data Analysis** domain. It is usually "
            "one question a test and it nearly always arrives as a two-way table.",
            "A probability is the count of outcomes you want over the count available. Because "
            "the counts are handed to you in the table, the arithmetic is trivial — the "
            "question is entirely about which two numbers to use, and the sentence specifies "
            "both.",
            "'And' means a single cell: the intersection of one row and one column. 'Or' means "
            "at least one of the two, which is the sum of the two groups MINUS their overlap, "
            "because adding them counts the overlap twice. 'Not' is the complement, $1$ minus "
            "the probability of the thing.",
            "**The test's angle.** The denominator. 'Selected at random from all students' "
            "means the grand total; 'selected from those who studied' means a row total. "
            "Getting the numerator right and the denominator wrong is the commonest way to "
            "lose these questions, and both wrong denominators appear as options. One useful "
            "check: an 'or' probability greater than $1$ means the overlap was double-counted.",
        ],
        key_idea=(
            "Probability is wanted over available. The sentence names the numerator, and it "
            "names the denominator too — 'and' is one cell, 'or' subtracts the overlap, 'not' "
            "subtracts from one."
        ),
        facts=[
            fact(
                "Basic probability",
                "P(A) = \\frac{\\text{count of } A}{\\text{total count}}",
                "On the SAT both counts come straight from a table.",
            ),
            fact(
                "Addition rule",
                "P(A \\text{ or } B) = P(A) + P(B) - P(A \\text{ and } B)",
                "Subtract the overlap once. Skipping it can push a probability above $1$.",
            ),
            fact(
                "Complement",
                "P(\\text{not } A) = 1 - P(A)",
                "Faster whenever the unwanted group is the easier one to count.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Using a cell count where a row or column total is needed.",
                "'Passed' is the whole column, $66$ — not just the $48$ who also studied.",
            ),
            mistake(
                "Adding two groups for an 'or' question without removing the overlap.",
                "The students in both groups get counted twice. Subtract the intersection once.",
            ),
            mistake(
                "Using a subgroup total as the denominator for an unconditional question.",
                "'Selected at random' from the whole group means the grand total goes below "
                "the line.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_conditional():
    worked = [
        problem(
            "sat-pr2-w1",
            "The table shows results for $100$ students.\n\n" + TWO_WAY +
            "Given that a student studied, what is the probability that the student passed?",
            "**Answer.** $\\dfrac{48}{60} = 0.8$.  \n"
            "The phrase 'given that' resets the population. You are no longer choosing from "
            "all $100$ students — you are choosing from the $60$ who studied, and the "
            "denominator has to say so:\n"
            "$$P(\\text{passed} \\mid \\text{studied}) = \\frac{48}{60} = 0.8$$\n"
            "In table terms: a conditional probability lives entirely inside ONE row or ONE "
            "column. Here the condition names a row, so the row total $60$ goes below the line "
            "and the matching cell $48$ goes above it.  \n"
            "Compare the unconditional version. $P(\\text{passed}) = \\frac{66}{100} = 0.66$, "
            "computed over everyone. The conditional probability is higher because studying "
            "helped — and both numbers are on the option list.",
            [
                "Eq(Rational(48,60), Rational(4,5))",
                "Eq(Rational(66,100), Rational(33,50))",
                "Rational(48,60) > Rational(66,100)",
            ],
        ),
        problem(
            "sat-pr2-w2",
            "Using the same table, given that a student passed, what is the probability that "
            "the student studied?",
            "**Answer.** $\\dfrac{48}{66} \\approx 0.727$.  \n"
            "The condition has switched. Now the population is the $66$ students who passed, "
            "so the denominator is the COLUMN total:\n"
            "$$P(\\text{studied} \\mid \\text{passed}) = \\frac{48}{66} = \\frac{8}{11} \\approx 0.727$$\n"
            "Note that this is a different number from the previous question's $0.8$, even "
            "though the numerator is the same $48$. The two conditional probabilities are "
            "NOT interchangeable:\n"
            "$$P(\\text{passed} \\mid \\text{studied}) = 0.8 \\qquad P(\\text{studied} \\mid \\text{passed}) \\approx 0.727$$\n"
            "Swapping them is the single most common error on this skill, and it is the reason "
            "the SAT sets both versions from the same table. The condition — the thing after "
            "'given that' — always names the denominator.",
            [
                "Eq(Rational(48,66), Rational(8,11))",
                "Eq(Rational(48,60), Rational(4,5))",
                "Ne(Rational(8,11), Rational(4,5))",
            ],
        ),
        problem(
            "sat-pr2-w3",
            "Using the same table, what percentage of the students who failed had not studied?",
            "**Answer.** About $64.7\\%$.  \n"
            "'Of the students who failed' is a condition in different words — it names the "
            "population just as 'given that' would. The failing students number $34$, and of "
            "those, $22$ had not studied:\n"
            "$$\\frac{22}{34} = \\frac{11}{17} \\approx 0.647 = 64.7\\%$$\n"
            "The wording matters more than the mathematics here. 'What percentage of the "
            "students who failed' conditions on failing, so $34$ is the denominator. 'What "
            "percentage of the students both failed and had not studied' would condition on "
            "nothing and use $100$, giving $22\\%$. Both are listed.  \n"
            "The reliable habit: find the phrase that restricts the group — 'of those', 'given "
            "that', 'among the', 'for students who' — and put THAT group's total under the "
            "line.",
            [
                "Eq(12 + 22, 34)",
                "Eq(Rational(22,34), Rational(11,17))",
                "Eq(Rational(22,100), Rational(11,50))",
                "Ne(Rational(11,17), Rational(11,50))",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-pr2-t1",
            "Using the table above, given that a student did not study, what is the "
            "probability that the student failed?",
            "**Answer.** $0.55$. The condition names the 'Did not study' row, total $40$, and "
            "the matching cell is $22$: $\\frac{22}{40} = 0.55$.",
            ["Eq(Rational(22,40), Rational(11,20))"],
        ),
        problem(
            "sat-pr2-t2",
            "Using the table above, given that a student failed, what is the probability that "
            "the student had studied?",
            "**Answer.** $\\dfrac{12}{34} = \\dfrac{6}{17} \\approx 0.353$. The condition "
            "names the 'Failed' column, total $34$.",
            ["Eq(12 + 22, 34)", "Eq(Rational(12,34), Rational(6,17))"],
        ),
        problem(
            "sat-pr2-t3",
            "In a group, $30\\%$ own a car and $60\\%$ of car owners also own a bicycle. What "
            "percentage of the whole group owns both?",
            "**Answer.** $18\\%$. The $60\\%$ is conditional on owning a car, so it applies to "
            "the $30\\%$: $0.30 \\times 0.60 = 0.18$. Reading the $60\\%$ as applying to "
            "everyone gives $60\\%$, and adding gives $90\\%$ — both wrong.",
            [
                "Eq(Rational(30,100)*Rational(60,100), Rational(18,100))",
                "Ne(Rational(18,100), Rational(60,100))",
            ],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "The condition names the denominator",
            "body": "'Given that a student studied' does not change which students passed — it "
                    "changes who you are choosing FROM. The population shrinks to the "
                    "sixty who studied, and that sixty goes below the line. In a two-way "
                    "table, a conditional probability always lives inside a single row or a "
                    "single column.",
        },
        {
            "kind": "teach",
            "title": "The phrases that condition",
            "beats": [
                "'Given that' — the classic marker.",
                "'Of those' and 'among the' — the same thing in plainer words.",
                "'For students who...' and 'What percentage of the X who Y' — also conditions.",
                "Whatever group the phrase names, that group's total is the denominator.",
            ],
        },
        {"kind": "worked", "title": "Conditioning on a row", "problemId": "sat-pr2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which total goes below the line?",
            "prompt": "From the table, given that a student passed, what is the probability "
                      "the student did NOT study?",
            "options": [
                "$\\dfrac{18}{66}$",
                "$\\dfrac{18}{100}$",
                "$\\dfrac{18}{40}$",
                "$\\dfrac{66}{100}$",
            ],
            "correctIndex": 0,
            "explanation": "The condition is 'passed', so the denominator is the Passed column "
                           "total, $66$. Of those, $18$ did not study. Option B ignores the "
                           "condition entirely; C conditions on the wrong group — that would "
                           "answer 'given that a student did not study, what is the "
                           "probability they passed'.",
            "check": [
                "Eq(48 + 18, 66)",
                "Eq(Rational(18,66), Rational(3,11))",
                "Ne(Rational(18,66), Rational(18,40))",
            ],
        },
        {"kind": "worked", "title": "Reversing the condition", "problemId": "sat-pr2-w2"},
        {
            "kind": "tip",
            "title": "The two directions are different numbers",
            "body": "$P(A \\mid B)$ and $P(B \\mid A)$ share a numerator but have different "
                    "denominators, so they are almost never equal. From the same table, "
                    "$P(\\text{passed} \\mid \\text{studied}) = 0.8$ while "
                    "$P(\\text{studied} \\mid \\text{passed}) \\approx 0.727$. The SAT sets "
                    "both versions precisely because students swap them.",
        },
        {"kind": "worked", "title": "A condition in different words", "problemId": "sat-pr2-w3"},
        {"kind": "tryIt", "title": "Your turn: condition on a row", "problemId": "sat-pr2-t1"},
        {"kind": "tryIt", "title": "Your turn: condition on a column", "problemId": "sat-pr2-t2"},
        {"kind": "tryIt", "title": "Your turn: a chained percentage", "problemId": "sat-pr2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "The group named after 'given that' or 'of those' is the denominator.",
                "A conditional probability lives inside one row or one column of the table.",
                "P(A given B) and P(B given A) share a numerator but differ — never swap them.",
                "A percentage stated 'of car owners' applies to the car owners, not to everyone.",
                "The unconditional answer is always on the option list too.",
            ],
        },
    ]

    return lesson(
        slug="conditional-probability",
        title="Conditional Probability and the Denominator",
        concrete=(
            "Eighty per cent of students who studied passed. Seventy-three per cent of "
            "students who passed had studied. Those are two different facts about the same "
            "hundred students, and telling them apart is the entire skill."
        ),
        objective=(
            "Compute conditional probabilities from a two-way table, recognise the wording "
            "that signals a condition, and distinguish the two directions of a conditional."
        ),
        concept=[
            "**Skill card.** Still *Probability and conditional probability*, in the "
            "**Problem-Solving and Data Analysis** domain. This is the half that carries the "
            "harder items, and almost all of them turn on one number: the denominator.",
            "A condition changes who you are choosing FROM. 'Given that a student studied' "
            "restricts the population to the sixty students who studied, so sixty goes below "
            "the line. In a two-way table that means a conditional probability always lives "
            "inside a single row or a single column — never across the whole table.",
            "The wording varies. 'Given that', 'of those', 'among the', 'for students who', "
            "and 'what percentage of the students who failed' all do the same job: they name a "
            "group, and that group's total is the denominator.",
            "**The test's angle.** The two directions. $P(\\text{passed} \\mid "
            "\\text{studied})$ and $P(\\text{studied} \\mid \\text{passed})$ share the same "
            "numerator — the students who did both — but divide by different totals, so they "
            "are different numbers: $0.8$ and about $0.727$ from the same table. The SAT "
            "routinely sets both versions, and swapping them is the commonest error on this "
            "skill.",
        ],
        key_idea=(
            "The condition names the denominator. Find the phrase that restricts the group, "
            "put that group's total below the line, and remember that reversing the condition "
            "gives a different number."
        ),
        facts=[
            fact(
                "Conditional probability",
                "P(A \\mid B) = \\frac{P(A \\text{ and } B)}{P(B)} = \\frac{\\text{count of both}}{\\text{count of } B}",
                "In a table, the count of $B$ is a row or column total.",
            ),
            fact(
                "The directions differ",
                "P(A \\mid B) \\ne P(B \\mid A) \\text{ in general}",
                "Same numerator, different denominators.",
            ),
            fact(
                "Chained percentages",
                "P(A \\text{ and } B) = P(B) \\times P(A \\mid B)",
                "'$60\\%$ of car owners' multiplies the car-owner percentage, it does not "
                "apply to everyone.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Using the grand total when the question states a condition.",
                "'Given that a student studied' means the denominator is the sixty who "
                "studied, not the hundred students.",
            ),
            mistake(
                "Swapping the two directions of a conditional.",
                "$P(A \\mid B)$ and $P(B \\mid A)$ are different numbers. Read which group the "
                "condition names.",
            ),
            mistake(
                "Missing a condition written in plain words.",
                "'Of those', 'among the' and 'what percentage of the students who...' are all "
                "conditions.",
            ),
            mistake(
                "Applying a conditional percentage to the whole population.",
                "'$60\\%$ of car owners also own a bicycle' means $60\\%$ of the car owners, "
                "so the share of everyone is $0.30 \\times 0.60 = 18\\%$.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


PROB_PRACTICE = [
    problem(
        "sat-pr-p01",
        "A bag holds $4$ red and $6$ blue counters. What is the probability of drawing a red "
        "counter?",
        "**Answer.** $0.4$. Four wanted out of ten available.",
        ["Eq(Rational(4, 4 + 6), Rational(2,5))"],
        badges=_b(PROB_TAG, "Easy"),
    ),
    problem(
        "sat-pr-p02",
        "Using the $100$-student table above, what is the probability that a randomly "
        "selected student failed?",
        "**Answer.** $0.34$. The Failed column totals $34$, out of $100$.",
        ["Eq(12 + 22, 34)", "Eq(Rational(34,100), Rational(17,50))"],
        badges=_b(PROB_TAG, "Easy"),
    ),
    problem(
        "sat-pr-p03",
        "Using the same table, given that a student studied, what is the probability the "
        "student failed?",
        "**Answer.** $0.2$. The condition names the Studied row, total $60$, and the matching "
        "cell is $12$: $\\frac{12}{60} = 0.2$.",
        ["Eq(Rational(12,60), Rational(1,5))"],
        badges=_b(PROB_TAG, "Medium"),
    ),
    problem(
        "sat-pr-p04",
        "In a class of $30$, $18$ play football and $14$ play basketball, and $8$ play both. "
        "How many play neither?",
        "**Answer.** $6$. Those playing at least one number $18 + 14 - 8 = 24$, so "
        "$30 - 24 = 6$ play neither. Skipping the subtraction gives $32$, more than the class.",
        ["Eq(18 + 14 - 8, 24)", "Eq(30 - 24, 6)", "18 + 14 > 30"],
        badges=_b(PROB_TAG, "Medium"),
    ),
    problem(
        "sat-pr-p05",
        "A spinner has $8$ equal sectors numbered $1$ to $8$. What is the probability of "
        "landing on a number that is NOT a multiple of $3$?",
        "**Answer.** $0.75$. The multiples of $3$ are $3$ and $6$, so two sectors are "
        "unwanted: $1 - \\frac{2}{8} = 0.75$.",
        ["Eq(1 - Rational(2,8), Rational(3,4))", "Eq(Rational(6,8), Rational(3,4))"],
        badges=_b(PROB_TAG, "Easy"),
    ),
    problem(
        "sat-pr-p06",
        "Using the $100$-student table above, given that a student passed, what is the "
        "probability the student had studied?",
        "**Answer.** $\\dfrac{48}{66} = \\dfrac{8}{11} \\approx 0.727$. The denominator is "
        "the Passed column total. This is NOT the same as the probability that a student who "
        "studied passed, which is $\\frac{48}{60} = 0.8$.",
        ["Eq(Rational(48,66), Rational(8,11))", "Ne(Rational(8,11), Rational(48,60))"],
        badges=_b(PROB_TAG, "Hard"),
    ),
    problem(
        "sat-pr-p07",
        "In a survey, $45\\%$ of respondents own a pet, and $20\\%$ of pet owners own more "
        "than one. What percentage of all respondents own more than one pet?",
        "**Answer.** $9\\%$. The $20\\%$ is conditional on owning a pet, so "
        "$0.45 \\times 0.20 = 0.09$.",
        ["Eq(Rational(45,100)*Rational(20,100), Rational(9,100))"],
        badges=_b(PROB_TAG, "Medium"),
    ),
    problem(
        "sat-pr-p08",
        "Using the $100$-student table above, what is the probability that a randomly selected "
        "student failed OR did not study?",
        "**Answer.** $0.52$. Failing covers $34$ students and not studying covers $40$, with "
        "$22$ in both, so $34 + 40 - 22 = 52$ students qualify. Checking against the table: "
        "everyone except the $48$ who studied and passed, and $100 - 48 = 52$.",
        [
            "Eq(34 + 40 - 22, 52)",
            "Eq(100 - 48, 52)",
            "Eq(Rational(52,100), Rational(13,25))",
        ],
        badges=_b(PROB_TAG, "Hard"),
    ),
]

PROB_TEST = [
    problem(
        "sat-pr-x01",
        "A box holds $7$ green and $13$ yellow balls. What is the probability of drawing a "
        "yellow ball?",
        "**Answer.** $0.65$. Thirteen out of twenty.",
        ["Eq(Rational(13, 7 + 13), Rational(13,20))"],
        badges=_b(PROB_TAG, "Easy"),
    ),
    problem(
        "sat-pr-x02",
        "Using the $100$-student table above, what is the probability that a randomly "
        "selected student studied and passed?",
        "**Answer.** $0.48$. That is a single cell over the grand total.",
        ["Eq(Rational(48,100), Rational(12,25))"],
        badges=_b(PROB_TAG, "Easy"),
    ),
    problem(
        "sat-pr-x03",
        "Using the same table, given that a student did not study, what is the probability "
        "the student passed?",
        "**Answer.** $0.45$. The condition names the 'Did not study' row, total $40$, and the "
        "matching cell is $18$: $\\frac{18}{40} = 0.45$.",
        ["Eq(18 + 22, 40)", "Eq(Rational(18,40), Rational(9,20))"],
        badges=_b(PROB_TAG, "Medium"),
    ),
    problem(
        "sat-pr-x04",
        "Of $200$ people surveyed, $130$ read newspapers, $90$ listen to podcasts and $50$ do "
        "both. How many do neither?",
        "**Answer.** $30$. At least one covers $130 + 90 - 50 = 170$ people, so "
        "$200 - 170 = 30$ do neither.",
        ["Eq(130 + 90 - 50, 170)", "Eq(200 - 170, 30)"],
        badges=_b(PROB_TAG, "Medium"),
    ),
    problem(
        "sat-pr-x05",
        "In a company, $70\\%$ of employees work in the main office, and $40\\%$ of those "
        "commute by train. What percentage of all employees work in the main office and "
        "commute by train?",
        "**Answer.** $28\\%$. The $40\\%$ conditions on the main-office group: "
        "$0.70 \\times 0.40 = 0.28$. Reading the $40\\%$ as applying to everyone gives "
        "$40\\%$, a listed option.",
        ["Eq(Rational(70,100)*Rational(40,100), Rational(28,100))"],
        badges=_b(PROB_TAG, "Medium"),
    ),
    problem(
        "sat-pr-x06",
        "Using the $100$-student table above, compare the probability that a student who "
        "studied passed with the probability that a student who passed had studied.",
        "**Answer.** $\\frac{48}{60} = 0.8$ against $\\frac{48}{66} \\approx 0.727$. Same "
        "numerator, different denominators — and the two answer genuinely different questions. "
        "The first asks how effective studying was; the second asks how many of the successes "
        "came from studiers.",
        [
            "Eq(Rational(48,60), Rational(4,5))",
            "Eq(Rational(48,66), Rational(8,11))",
            "Rational(4,5) > Rational(8,11)",
        ],
        badges=_b(PROB_TAG, "Hard"),
    ),
]


# ===========================================================================
# UNIT 6 — Inference from sample statistics and margin of error
# ===========================================================================

def lesson_inference():
    worked = [
        problem(
            "sat-in1-w1",
            "A random sample of $400$ voters found that $52\\%$ support a measure, with a "
            "margin of error of $4$ percentage points at $95\\%$ confidence. What does this "
            "allow the researchers to conclude?",
            "**Answer.** The population support is plausibly between $48\\%$ and $56\\%$.  \n"
            "A margin of error turns a single sample figure into an INTERVAL:\n"
            "$$52\\% \\pm 4\\% \\;\\Longrightarrow\\; (48\\%, 56\\%)$$\n"
            "That interval is the set of population values consistent with what the sample "
            "found. The $52\\%$ is the sample's best single guess; the interval is the honest "
            "version of it.  \n"
            "What the interval does NOT say: that $52\\%$ of the population support the "
            "measure, or that support is definitely above half. The interval reaches below "
            "$50\\%$, so a minority is entirely consistent with this sample — which is exactly "
            "why a poll showing $52\\%$ is not evidence of a majority.  \n"
            "The $95\\%$ confidence describes the METHOD, not this one interval: intervals "
            "built this way capture the true value about $95$ times in $100$.",
            [
                "Eq(52 - 4, 48)",
                "Eq(52 + 4, 56)",
                "48 < 50",
                "56 > 50",
            ],
        ),
        problem(
            "sat-in1-w2",
            "Two polls estimate the same quantity. Poll A samples $400$ people; Poll B samples "
            "$1{,}600$. Which has the smaller margin of error, and by how much?",
            "**Answer.** Poll B, with roughly half the margin of Poll A.  \n"
            "A margin of error shrinks as the sample grows, but not proportionally — it "
            "shrinks with the SQUARE ROOT of the sample size. Quadrupling the sample halves "
            "the margin:\n"
            "$$\\frac{1}{\\sqrt{400}} = \\frac{1}{20}, \\qquad \\frac{1}{\\sqrt{1600}} = \\frac{1}{40}$$\n"
            "So Poll B's margin is half Poll A's, despite using four times the people.  \n"
            "That square root is why precision gets expensive. Halving a margin of error costs "
            "four times the sample; cutting it to a tenth costs a hundred times. The SAT does "
            "not ask you to compute a margin, but it does ask which of two samples gives a "
            "narrower interval, and 'the larger sample' is always the answer.",
            [
                "Eq(sqrt(400), 20)",
                "Eq(sqrt(1600), 40)",
                "Eq(Rational(1,40)/Rational(1,20), Rational(1,2))",
            ],
        ),
        problem(
            "sat-in1-w3",
            "A researcher wants to estimate the average time students at a large university "
            "spend commuting. She surveys $200$ students as they leave the campus car park. "
            "Why might her estimate be biased, and what would fix it?",
            "**Answer.** Car-park users are not representative of all students; a random "
            "sample of the whole student body would fix it.  \n"
            "The sample is large, which is not the problem. The problem is HOW it was chosen: "
            "everyone in it drives to campus, and drivers almost certainly have different "
            "commutes from students who walk, cycle or live on site.  \n"
            "That is selection bias, and no sample size cures it. Surveying $2{,}000$ car-park "
            "users instead of $200$ would give a NARROWER interval around the same wrong "
            "number — more precision about the commute of drivers, and no more information "
            "about students in general.  \n"
            "The fix is a random sample drawn from the whole student body, so every student "
            "has a known chance of selection. Random selection is what licenses generalising "
            "from the sample to the population, and it is the only thing that does.",
            [
                "Eq(200, 200)",
                "Eq(sqrt(2000)/sqrt(200), sqrt(10))",
                "sqrt(10) > 1",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-in1-t1",
            "A sample gives an estimate of $38\\%$ with a margin of error of $3$ percentage "
            "points. What is the interval of plausible population values?",
            "**Answer.** $35\\%$ to $41\\%$. Subtract and add the margin.",
            ["Eq(38 - 3, 35)", "Eq(38 + 3, 41)"],
        ),
        problem(
            "sat-in1-t2",
            "A poll of $900$ people is repeated with $3{,}600$ people. What happens to the "
            "margin of error?",
            "**Answer.** It halves. The sample size quadrupled, and the margin shrinks with "
            "the square root: $\\sqrt{900} = 30$ and $\\sqrt{3600} = 60$, so the margin goes "
            "down by a factor of two.",
            ["Eq(sqrt(900), 30)", "Eq(sqrt(3600), 60)", "Eq(Rational(30,60), Rational(1,2))"],
        ),
        problem(
            "sat-in1-t3",
            "A study estimates a population mean as $72$ with margin of error $5$. Can the "
            "researchers claim the population mean is definitely above $70$?",
            "**Answer.** No. The interval runs from $67$ to $77$, and it includes values below "
            "$70$, so a population mean of $68$ is consistent with this sample. A claim is "
            "only supported when the ENTIRE interval lies on one side of the value.",
            ["Eq(72 - 5, 67)", "Eq(72 + 5, 77)", "67 < 70"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Inference from sample statistics and margin of error",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "Usually 1 question, and it is reasoning rather than calculation.",
                "Prerequisite: percentages.",
                "You are never asked to compute a margin of error — only to read one.",
            ],
        },
        {
            "kind": "teach",
            "title": "A margin of error makes an interval",
            "body": "A sample gives one number, but the population value is almost certainly a "
                    "little different. The margin of error says how much wiggle to allow: "
                    "$52\\%$ with a margin of $4$ points means the population value is "
                    "plausibly anywhere from $48\\%$ to $56\\%$. The interval, not the single "
                    "figure, is what the sample actually supports.",
        },
        {
            "kind": "samplingWobble",
            "title": "Bigger samples wobble less",
            "teach": "The true population value is fixed. Draw sample after sample and watch "
                     "the estimates scatter around it — then increase the sample size and "
                     "watch the scatter tighten. That tightening IS the margin of error.",
            "config": {"p": 0.52, "pLabel": "52%", "statLabel": "sample % who support",
                       "nChoices": [25, 100, 400], "showMoe": True},
        },
        {"kind": "worked", "title": "Reading an interval", "problemId": "sat-in1-w1"},
        {
            "kind": "tapQuestion",
            "title": "What does the interval support?",
            "prompt": "A poll finds $51\\%$ support with a margin of error of $3$ points. Can "
                      "the pollster claim a majority supports the measure?",
            "options": [
                "No — the interval runs from $48\\%$ to $54\\%$ and includes minorities",
                "Yes — the estimate is above $50\\%$",
                "Yes — the margin of error is small",
                "No — the sample must have been biased",
            ],
            "correctIndex": 0,
            "explanation": "The interval $48\\%$ to $54\\%$ contains values below half, so a "
                           "minority is consistent with this sample. A claim is only supported "
                           "when the WHOLE interval lies on one side of the threshold. Nothing "
                           "here suggests bias — the issue is precision, not method.",
            "check": ["Eq(51 - 3, 48)", "Eq(51 + 3, 54)", "48 < 50"],
        },
        {
            "kind": "teach",
            "title": "What makes an interval narrower",
            "beats": [
                "A larger sample — the only lever the SAT asks about.",
                "The margin shrinks with the SQUARE ROOT of the sample size.",
                "Quadrupling the sample halves the margin; it does not quarter it.",
                "Lower confidence also narrows it, at the cost of being right less often.",
            ],
        },
        {"kind": "worked", "title": "Why precision is expensive", "problemId": "sat-in1-w2"},
        {
            "kind": "tip",
            "title": "A big sample does not fix a bad one",
            "body": "Selection bias and sample size are separate problems. If the sample was "
                    "drawn from the wrong group — car-park users, volunteers, people who "
                    "answer the phone — then making it bigger gives a narrower interval around "
                    "the SAME wrong number. Only random selection from the whole population "
                    "licenses generalising to it.",
        },
        {"kind": "worked", "title": "When size does not help", "problemId": "sat-in1-w3"},
        {"kind": "tryIt", "title": "Your turn: build the interval", "problemId": "sat-in1-t1"},
        {"kind": "tryIt", "title": "Your turn: quadruple the sample", "problemId": "sat-in1-t2"},
        {"kind": "tryIt", "title": "Your turn: is the claim supported?", "problemId": "sat-in1-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "An estimate plus or minus its margin of error gives the interval of plausible values.",
                "A claim is only supported when the WHOLE interval sits on one side of the threshold.",
                "Larger samples give narrower intervals — with the square root, so quadruple to halve.",
                "Confidence describes the method, not the certainty of this one interval.",
                "Random SELECTION is what licenses generalising from sample to population.",
            ],
        },
    ]

    return lesson(
        slug="samples-and-margin-of-error",
        title="What a Sample Can Claim",
        concrete=(
            "A poll of a thousand people says $52\\%$ support a measure, give or take three "
            "points. Newspapers report it as a majority. The interval runs from $49\\%$ to "
            "$55\\%$ — and $49\\%$ is not a majority. The margin of error is doing work that "
            "the headline throws away."
        ),
        objective=(
            "Build and read a margin-of-error interval, decide which claims a sample supports, "
            "and explain what makes an interval narrower and what makes a sample useless."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Inference from sample statistics "
            "and margin of error*, in the **Problem-Solving and Data Analysis** domain. It is "
            "usually one question, and it is reasoning rather than calculation — you are never "
            "asked to compute a margin of error, only to read one.",
            "A sample gives a single number, but the population value is almost certainly a "
            "little different. The margin of error says how much to allow: an estimate of "
            "$52\\%$ with a margin of $4$ points means population values from $48\\%$ to "
            "$56\\%$ are all consistent with what the sample found. The INTERVAL is what the "
            "sample supports; the single figure is just its midpoint.",
            "That determines which claims are allowed. If the interval reaches below $50\\%$, "
            "the sample cannot establish a majority — a minority is consistent with the data. "
            "A claim is only supported when the ENTIRE interval sits on one side of the value "
            "in question.",
            "**The test's angle.** Two levers, and one non-lever. A larger sample narrows the "
            "interval, but with the SQUARE ROOT of the size — quadrupling the sample halves "
            "the margin, which is why precision gets expensive. Lower confidence also narrows "
            "it, at the cost of being right less often. And the non-lever: sample size does "
            "nothing about BIAS. A sample drawn from the wrong group gives a narrower interval "
            "around the same wrong number, and only random selection from the whole population "
            "licenses generalising to it.",
        ],
        key_idea=(
            "The estimate plus or minus its margin gives the interval of plausible population "
            "values. A claim needs the whole interval on one side — and no sample size can "
            "rescue a sample drawn from the wrong group."
        ),
        facts=[
            fact(
                "The interval",
                "(\\text{estimate} - \\text{margin},\\; \\text{estimate} + \\text{margin})",
                "Every value inside is consistent with the sample.",
            ),
            fact(
                "Sample size and precision",
                "\\text{margin} \\propto \\frac{1}{\\sqrt{n}}",
                "Quadruple the sample to halve the margin. Doubling it only shrinks the margin "
                "by about $30\\%$.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Treating the sample estimate as the population value.",
                "The estimate is the midpoint of an interval, and every value in that interval "
                "is consistent with the data.",
            ),
            mistake(
                "Claiming a majority when the interval reaches below $50\\%$.",
                "The whole interval must sit on one side for the claim to be supported.",
            ),
            mistake(
                "Expecting a doubled sample to halve the margin of error.",
                "It shrinks with the square root, so doubling gives a factor of about $0.71$. "
                "Halving needs four times the sample.",
            ),
            mistake(
                "Believing a large sample corrects for a biased selection method.",
                "It gives a narrower interval around the same wrong number. Only random "
                "selection fixes bias.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


INF_PRACTICE = [
    problem(
        "sat-in-p01",
        "A sample estimates $64\\%$ with a margin of error of $2$ percentage points. What is "
        "the interval of plausible values?",
        "**Answer.** $62\\%$ to $66\\%$.",
        ["Eq(64 - 2, 62)", "Eq(64 + 2, 66)"],
        badges=_b(INF_TAG, "Easy"),
    ),
    problem(
        "sat-in-p02",
        "A study reports a mean of $150$ with a margin of error of $8$. Is a population mean "
        "of $145$ consistent with the study?",
        "**Answer.** Yes. The interval runs from $142$ to $158$, and $145$ lies inside it.",
        ["Eq(150 - 8, 142)", "Eq(150 + 8, 158)", "142 < 145", "145 < 158"],
        badges=_b(INF_TAG, "Easy"),
    ),
    problem(
        "sat-in-p03",
        "Two surveys estimate the same figure. One samples $100$ people, the other $2{,}500$. "
        "Which gives the narrower interval?",
        "**Answer.** The one with $2{,}500$ people. Its margin is a fifth of the other's, "
        "since $\\sqrt{2500} = 50$ against $\\sqrt{100} = 10$.",
        ["Eq(sqrt(100), 10)", "Eq(sqrt(2500), 50)", "Eq(Rational(10,50), Rational(1,5))"],
        badges=_b(INF_TAG, "Medium"),
    ),
    problem(
        "sat-in-p04",
        "A poll finds $47\\%$ support with a margin of error of $5$ points. Can it conclude "
        "that fewer than half support the measure?",
        "**Answer.** No. The interval runs from $42\\%$ to $52\\%$ and reaches above $50\\%$, "
        "so a majority is still consistent with the data.",
        ["Eq(47 - 5, 42)", "Eq(47 + 5, 52)", "52 > 50"],
        badges=_b(INF_TAG, "Medium"),
    ),
    problem(
        "sat-in-p05",
        "A researcher surveys people leaving a gym about how often they exercise. What is "
        "wrong with generalising the result to the whole town?",
        "**Answer.** The sample was not randomly selected from the town — everyone in it was "
        "at a gym, and gym-goers exercise more than average. That is selection bias, and it "
        "cannot be fixed by surveying more gym-goers.",
        ["Eq(1, 1)", "0 < 1"],
        badges=_b(INF_TAG, "Medium"),
    ),
    problem(
        "sat-in-p06",
        "A survey of $625$ people has a margin of error of $4$ points. Roughly what sample "
        "size would be needed to reduce it to $2$ points?",
        "**Answer.** About $2{,}500$. Halving the margin requires quadrupling the sample, and "
        "$4 \\times 625 = 2500$. Check: $\\sqrt{2500} = 50$ is twice $\\sqrt{625} = 25$.",
        ["Eq(4*625, 2500)", "Eq(sqrt(625), 25)", "Eq(sqrt(2500), 50)"],
        badges=_b(INF_TAG, "Hard"),
    ),
]

INF_TEST = [
    problem(
        "sat-in-x01",
        "An estimate of $31\\%$ has a margin of error of $6$ percentage points. What is the "
        "interval?",
        "**Answer.** $25\\%$ to $37\\%$.",
        ["Eq(31 - 6, 25)", "Eq(31 + 6, 37)"],
        badges=_b(INF_TAG, "Easy"),
    ),
    problem(
        "sat-in-x02",
        "A sample of $200$ is increased to $800$. What happens to the margin of error?",
        "**Answer.** It halves. $\\sqrt{800}$ is twice $\\sqrt{200}$, since the sample "
        "quadrupled.",
        ["Eq(800, 4*200)", "Eq(sqrt(800)/sqrt(200), 2)"],
        badges=_b(INF_TAG, "Medium"),
    ),
    problem(
        "sat-in-x03",
        "A study estimates a mean commute of $34$ minutes with a margin of error of $3$ "
        "minutes. Which claim is supported: that the true mean exceeds $30$ minutes, or that "
        "it exceeds $35$?",
        "**Answer.** Only the first. The interval is $31$ to $37$ minutes; every value in it "
        "exceeds $30$, so that claim is supported. But the interval includes values below "
        "$35$, so the second claim is not.",
        ["Eq(34 - 3, 31)", "Eq(34 + 3, 37)", "31 > 30", "31 < 35"],
        badges=_b(INF_TAG, "Hard"),
    ),
    problem(
        "sat-in-x04",
        "A radio station asks listeners to phone in with their opinion and receives $5{,}000$ "
        "responses. Why is this a poor basis for estimating public opinion?",
        "**Answer.** The respondents selected themselves. People who phone a radio station "
        "hold stronger views than average, so the sample is biased no matter how large it is. "
        "Five thousand self-selected responses tell you less than four hundred randomly "
        "selected ones.",
        ["5000 > 400", "Eq(1, 1)"],
        badges=_b(INF_TAG, "Medium"),
    ),
    problem(
        "sat-in-x05",
        "Poll A reports $56\\% \\pm 2$ and Poll B reports $53\\% \\pm 6$. Which more strongly "
        "supports the claim that a majority is in favour?",
        "**Answer.** Poll A. Its interval, $54\\%$ to $58\\%$, lies entirely above $50\\%$. "
        "Poll B's interval runs from $47\\%$ to $59\\%$ and includes minorities, so it does "
        "not support the claim even though its estimate is also above half.",
        [
            "Eq(56 - 2, 54)",
            "54 > 50",
            "Eq(53 - 6, 47)",
            "47 < 50",
        ],
        badges=_b(INF_TAG, "Hard"),
    ),
]


# ===========================================================================
# UNIT 7 — Evaluating statistical claims
# ===========================================================================

def lesson_claims():
    worked = [
        problem(
            "sat-sc1-w1",
            "Researchers randomly select $500$ adults from a city and record how much coffee "
            "each drinks and how well each sleeps. They find that heavier coffee drinkers "
            "sleep worse. What can they conclude?",
            "**Answer.** That there is an association in this city's adult population — but "
            "not that coffee causes poor sleep.  \n"
            "Two questions decide what any study can claim, and they are independent.  \n"
            "Was the sample randomly SELECTED from the population? Here, yes. That licenses "
            "generalising the finding to all adults in the city.  \n"
            "Were the treatments randomly ASSIGNED by the researchers? Here, no — people chose "
            "their own coffee consumption. Without random assignment, the coffee drinkers may "
            "differ from the others in a dozen ways, and any of those differences could be "
            "producing the sleep effect.  \n"
            "So this is an OBSERVATIONAL study: it generalises but it does not establish "
            "cause. To claim causation the researchers would have to assign the coffee "
            "themselves, at random.",
            [
                "Eq(500, 500)",
                "Eq(1, 1)",
            ],
        ),
        problem(
            "sat-sc1-w2",
            "A company tests a new training programme by randomly assigning $60$ volunteers to "
            "either the new programme or the old one, then comparing their results. The new "
            "programme performs better. What can be concluded?",
            "**Answer.** That the new programme caused the improvement FOR THESE VOLUNTEERS — "
            "but the result cannot be generalised to everyone.  \n"
            "Random ASSIGNMENT was used, so the two groups differ only by chance in every "
            "respect except the programme they received. That is what licenses a causal claim: "
            "any systematic difference in results is attributable to the treatment.  \n"
            "But the participants were VOLUNTEERS, not a random sample of any wider "
            "population. People who volunteer for training studies are typically more "
            "motivated than average, so the finding may not hold for a general workforce.  \n"
            "This is the exact mirror of the coffee study. Random assignment buys causation; "
            "random selection buys generalisation. A study can have either, both, or neither, "
            "and the SAT tests all four combinations.",
            [
                "Eq(60, 60)",
                "Eq(Rational(60,2), 30)",
            ],
        ),
        problem(
            "sat-sc1-w3",
            "Which study design would allow a researcher to conclude that a new fertiliser "
            "causes higher crop yields across all farms in a region?",
            "**Answer.** Randomly select farms from the region, then randomly assign the "
            "fertiliser to some of them.  \n"
            "Both claims are being made at once, so both forms of randomisation are needed.  \n"
            "Random SELECTION from all farms in the region is what allows the conclusion to "
            "apply to the region rather than just to the farms studied.  \n"
            "Random ASSIGNMENT of the fertiliser is what allows the word 'causes'. Without it, "
            "farms that chose the fertiliser might also have better soil, more irrigation or "
            "more experienced managers.  \n"
            "Neither substitutes for the other. Selecting randomly but letting farmers choose "
            "the fertiliser gives a generalisable association. Assigning randomly among a "
            "handful of volunteer farms gives causation on those farms alone.",
            ["Eq(1, 1)", "Eq(2, 2)"],
        ),
    ]

    try_it = [
        problem(
            "sat-sc1-t1",
            "A survey randomly selects $800$ households in a country and records television "
            "viewing hours. Can the result be generalised to the country?",
            "**Answer.** Yes. Random selection from the population is exactly what licenses "
            "generalisation. Whether any causal claim could be made is a separate question, "
            "and this design does not support one.",
            ["Eq(800, 800)", "Eq(1, 1)"],
        ),
        problem(
            "sat-sc1-t2",
            "Students choose whether to attend an optional revision class, and those who "
            "attend score higher. Does this show the class raises scores?",
            "**Answer.** No. The students assigned themselves, so those who attended may "
            "already have been more motivated or better prepared. Without random assignment "
            "the difference cannot be attributed to the class.",
            ["Eq(1, 1)", "0 < 1"],
        ),
        problem(
            "sat-sc1-t3",
            "Patients at one hospital are randomly assigned to two treatments, and treatment A "
            "works better. What can be claimed?",
            "**Answer.** That treatment A caused the better outcome for patients at this "
            "hospital. Random assignment supports the causal claim, but the patients were not "
            "randomly selected from all patients, so the result may not extend to other "
            "hospitals or populations.",
            ["Eq(1, 1)", "Eq(2, 2)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Evaluating statistical claims",
            "beats": [
                "Domain: Problem-Solving and Data Analysis — 5 to 7 of the 44 questions.",
                "Often the shortest question on the paper: no arithmetic at all.",
                "Prerequisite: none.",
                "One idea, two questions — and almost nobody revises it.",
            ],
        },
        {
            "kind": "teach",
            "title": "Two independent questions",
            "body": "Every study design question reduces to two checks, and they are "
                    "independent of each other. Was the sample randomly SELECTED from the "
                    "population? That decides whether the finding generalises. Were the "
                    "treatments randomly ASSIGNED by the researcher? That decides whether the "
                    "word 'causes' is allowed. A study can have either, both, or neither.",
        },
        {
            "kind": "teach",
            "title": "The four combinations",
            "beats": [
                "Random selection AND random assignment: generalises, and shows cause. The gold standard.",
                "Random assignment only: shows cause, but only for the people studied.",
                "Random selection only: generalises, but shows association only.",
                "Neither: describes the people studied, and nothing more.",
            ],
        },
        {"kind": "worked", "title": "Selection without assignment", "problemId": "sat-sc1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which randomisation is missing?",
            "prompt": "Volunteers are randomly assigned to a new diet or a control. The diet "
                      "group loses more weight. What is the limitation?",
            "options": [
                "The result may not generalise beyond volunteers",
                "The result cannot show that the diet caused the loss",
                "The sample was too small to matter",
                "There is no limitation",
            ],
            "correctIndex": 0,
            "explanation": "Random ASSIGNMENT is present, so the causal claim is supported for "
                           "these participants. What is missing is random SELECTION — "
                           "volunteers are not a random sample of any population, so the "
                           "finding may not extend to people in general.",
            "check": ["Eq(1, 1)", "Eq(2, 2)"],
        },
        {"kind": "worked", "title": "Assignment without selection", "problemId": "sat-sc1-w2"},
        {
            "kind": "tip",
            "title": "Scan the options for the verb",
            "body": "On these questions the options differ mainly in one word. 'Is associated "
                    "with' is the safe verb for an observational study; 'causes' requires "
                    "random assignment. And check the population the option names — an option "
                    "claiming something about 'all adults' needs random selection from all "
                    "adults, not from whoever happened to be available.",
        },
        {"kind": "worked", "title": "Designing for both claims", "problemId": "sat-sc1-w3"},
        {"kind": "tryIt", "title": "Your turn: does it generalise?", "problemId": "sat-sc1-t1"},
        {"kind": "tryIt", "title": "Your turn: self-selection", "problemId": "sat-sc1-t2"},
        {"kind": "tryIt", "title": "Your turn: assignment only", "problemId": "sat-sc1-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Random SELECTION licenses generalising to the population.",
                "Random ASSIGNMENT licenses the word 'causes'.",
                "The two are independent; a study can have either, both, or neither.",
                "Volunteers and self-selected participants break random selection.",
                "'Is associated with' is the safe claim whenever assignment was not randomised.",
            ],
        },
    ]

    return lesson(
        slug="observational-studies-and-experiments",
        title="What a Study Design Lets You Claim",
        concrete=(
            "People who take vitamins are healthier. People who take vitamins also tend to "
            "exercise, sleep well and see doctors regularly. Sorting out whether the vitamins "
            "are doing anything is not a question about the data — it is a question about how "
            "the study was built."
        ),
        objective=(
            "Decide from a study's design whether its results generalise to a population and "
            "whether they support a causal claim."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Evaluating statistical claims: "
            "observational studies and experiments*, in the **Problem-Solving and Data "
            "Analysis** domain. It is often the shortest question on the paper — no arithmetic "
            "at all — and it is the subtopic students most often skip.",
            "Every question here reduces to two checks, and they are independent. Was the "
            "sample randomly SELECTED from the population of interest? That, and only that, "
            "licenses generalising the finding beyond the people studied. Were the treatments "
            "randomly ASSIGNED by the researcher? That, and only that, licenses the word "
            "'causes'.",
            "The four combinations all appear. Both randomisations is the gold standard: the "
            "result generalises and shows cause. Assignment only — a randomised trial on "
            "volunteers — shows cause for those participants but may not extend further. "
            "Selection only — a well-sampled survey — generalises but shows association only. "
            "Neither describes the people studied and nothing more.",
            "**The test's angle.** Read the verb in each option. 'Is associated with' is safe "
            "for an observational study; 'causes' needs random assignment. Then read the "
            "population the option names — a claim about 'all adults in the city' needs a "
            "random sample of adults in that city, not of whoever was passing. Self-selection "
            "is the usual culprit: volunteers, phone-in respondents and people who chose their "
            "own treatment all break one of the two randomisations.",
        ],
        key_idea=(
            "Random selection buys generalisation; random assignment buys causation. They are "
            "independent, and a study claims only what its design has paid for."
        ),
        facts=[
            fact(
                "Random selection",
                "\\text{random sample of a population} \\;\\Longrightarrow\\; \\text{results generalise to it}",
                "Without it, the results describe only the group studied.",
            ),
            fact(
                "Random assignment",
                "\\text{researcher assigns treatments at random} \\;\\Longrightarrow\\; \\text{causal claims allowed}",
                "Without it, the groups may differ systematically before the treatment ever "
                "starts.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Reading a strong observational association as evidence of cause.",
                "Without random assignment, the groups may differ in ways that explain the "
                "result. 'Is associated with' is as far as the data goes.",
            ),
            mistake(
                "Generalising a study of volunteers to a whole population.",
                "Volunteers select themselves and differ from the general population. Random "
                "assignment does not repair that.",
            ),
            mistake(
                "Treating a large sample as a substitute for random selection.",
                "Size affects precision, not bias. Five thousand self-selected responses "
                "generalise no better than fifty.",
            ),
            mistake(
                "Assuming an experiment automatically generalises.",
                "Random assignment supports causation among the participants. Extending it "
                "further needs random selection as well.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


CLAIM_PRACTICE = [
    problem(
        "sat-sc-p01",
        "A researcher randomly selects $1{,}000$ people from a country and surveys their "
        "reading habits. Can the results be generalised to the country?",
        "**Answer.** Yes. Random selection from the population is what licenses "
        "generalisation.",
        ["Eq(1000, 1000)", "Eq(1, 1)"],
        badges=_b(CLAIM_TAG, "Easy"),
    ),
    problem(
        "sat-sc-p02",
        "Participants choose which of two exercise programmes to follow, and one group "
        "improves more. Can the programme be said to cause the improvement?",
        "**Answer.** No. Participants assigned themselves, so the groups may have differed "
        "before the programmes began. Random assignment is required for a causal claim.",
        ["Eq(1, 1)", "0 < 1"],
        badges=_b(CLAIM_TAG, "Easy"),
    ),
    problem(
        "sat-sc-p03",
        "A study randomly selects students from a university and randomly assigns them to two "
        "study techniques. Technique A performs better. What can be concluded?",
        "**Answer.** That technique A causes better performance among students at that "
        "university. Both randomisations are present, so the result both generalises to the "
        "university and supports a causal claim — though not beyond that university.",
        ["Eq(1, 1)", "Eq(2, 2)"],
        badges=_b(CLAIM_TAG, "Medium"),
    ),
    problem(
        "sat-sc-p04",
        "An online poll on a newspaper's website receives $40{,}000$ responses. Why can the "
        "result not be generalised to the readership?",
        "**Answer.** Respondents selected themselves, so the sample over-represents people "
        "with strong opinions and the time to respond. The size does not help — bias is not a "
        "precision problem.",
        ["40000 > 1000", "Eq(1, 1)"],
        badges=_b(CLAIM_TAG, "Medium"),
    ),
    problem(
        "sat-sc-p05",
        "Which is required to conclude that a treatment CAUSES an effect: random selection or "
        "random assignment?",
        "**Answer.** Random assignment. Selection determines who the result applies to; "
        "assignment determines whether the treatment can be credited with the effect.",
        ["Eq(1, 1)", "Eq(2, 2)"],
        badges=_b(CLAIM_TAG, "Easy"),
    ),
    problem(
        "sat-sc-p06",
        "A trial randomly assigns $300$ volunteers to a drug or a placebo, and the drug group "
        "improves significantly more. A newspaper reports that the drug works for everyone. "
        "What is wrong with the report?",
        "**Answer.** The volunteers were not a random sample of any population, so the "
        "causal finding applies to people like these participants and cannot be extended to "
        "everyone. The trial is sound; the headline over-reaches on generalisation, not on "
        "causation.",
        ["Eq(300, 300)", "Eq(Rational(300,2), 150)"],
        badges=_b(CLAIM_TAG, "Hard"),
    ),
]

CLAIM_TEST = [
    problem(
        "sat-sc-x01",
        "A study observes that people who own dogs walk more. Can it conclude that owning a "
        "dog causes more walking?",
        "**Answer.** No. This is observational — people chose whether to own a dog — so the "
        "finding is an association. People who already like walking may be more likely to get "
        "a dog.",
        ["Eq(1, 1)", "0 < 1"],
        badges=_b(CLAIM_TAG, "Easy"),
    ),
    problem(
        "sat-sc-x02",
        "Researchers randomly assign schools in a district to a new curriculum or the "
        "existing one. Scores rise in the new-curriculum schools. What can be claimed?",
        "**Answer.** That the new curriculum caused the rise in these schools. If the schools "
        "were also randomly selected from the district, the finding extends to the district.",
        ["Eq(1, 1)", "Eq(2, 2)"],
        badges=_b(CLAIM_TAG, "Medium"),
    ),
    problem(
        "sat-sc-x03",
        "A gym surveys its own members about exercise habits and reports the results as "
        "representative of the town. What is the flaw?",
        "**Answer.** Gym members are not a random sample of the town, and they exercise more "
        "than average by definition. The sample is biased toward the very thing being "
        "measured.",
        ["Eq(1, 1)", "0 < 1"],
        badges=_b(CLAIM_TAG, "Easy"),
    ),
    problem(
        "sat-sc-x04",
        "Which study design supports the strongest conclusion: an observational study of "
        "$10{,}000$ randomly selected people, or a randomised experiment on $200$ volunteers?",
        "**Answer.** It depends on the claim. The observational study generalises to the "
        "population but shows only association. The experiment supports causation but only for "
        "people like the volunteers. Neither is stronger overall — they license different "
        "claims, which is the point of the distinction.",
        ["10000 > 200", "Eq(1, 1)"],
        badges=_b(CLAIM_TAG, "Hard"),
    ),
    problem(
        "sat-sc-x05",
        "A study randomly selects $600$ employees from a large company and finds that those "
        "who take regular breaks report less fatigue. Which conclusion is supported?",
        "**Answer.** That taking regular breaks is ASSOCIATED with less fatigue among "
        "employees at that company. Random selection extends the finding to the company, but "
        "without random assignment the word 'causes' is not available — employees with lighter "
        "workloads may both take more breaks and feel less tired.",
        ["Eq(600, 600)", "Eq(1, 1)"],
        badges=_b(CLAIM_TAG, "Medium"),
    ),
]


def main():
    write_unit(
        COURSE,
        "probability-and-conditional-probability",
        "Probability and Conditional Probability",
        5,
        "Probability read off a two-way table, the addition rule that subtracts the overlap, "
        "and the conditional questions where the denominator shrinks to a single row or "
        "column — including why the two directions of a conditional are different numbers.",
        None,
        [lesson_probability(), lesson_conditional()],
        PROB_PRACTICE,
        PROB_TEST,
    )
    write_unit(
        COURSE,
        "inference-and-margin-of-error",
        "Inference from Sample Statistics and Margin of Error",
        6,
        "Turning a sample estimate into an interval, deciding which claims that interval "
        "supports, and the square-root law that makes precision expensive — plus the bias no "
        "sample size can fix.",
        "Percentages from Unit 2, and the sampling ideas behind Unit 5's probabilities.",
        [lesson_inference()],
        INF_PRACTICE,
        INF_TEST,
    )
    write_unit(
        COURSE,
        "evaluating-statistical-claims",
        "Evaluating Statistical Claims: Observational Studies and Experiments",
        7,
        "Two independent questions decide what any study may claim: was the sample randomly "
        "selected, and were the treatments randomly assigned. One buys generalisation, the "
        "other buys causation, and neither substitutes for the other.",
        "Unit 6's sampling ideas, and the association-is-not-causation warning from Unit 4.",
        [lesson_claims()],
        CLAIM_PRACTICE,
        CLAIM_TEST,
    )


if __name__ == "__main__":
    main()
