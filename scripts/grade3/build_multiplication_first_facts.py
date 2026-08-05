#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Multiplication — First Facts.

Equal groups as the thing multiplication counts; arrays and the
turnaround (one rectangle, two facts); the friendly tables of 2, 5 and
10 with the patterns in their endings; the tables of 3 and 4 built from
counting on and from doubling; and the two odd-looking facts — times one
and times zero — followed by multiplication stories.

Through-line: MULTIPLICATION IS COUNTING EQUAL GROUPS. Every lesson
returns to it — the groups give the meaning, the array shows why the two
orders agree, the friendly tables are step-counts you already know, the
harder tables are built from the friendly ones, and a story is only a
times story if its groups are equal.

Grade discipline: tables of 2, 3, 4, 5 and 10 only (Grade 4 owns the
full set to ten and two-digit by one-digit work), nothing above 1000, no
negatives, no decimals. Every check is sympy-asserted with exact
integers BEFORE the JSON is written. Figures are built from the SAME
Python variables as the statements they illustrate.

Run: python3 scripts/grade3/build_multiplication_first_facts.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, workedset, write_topic,
                     fig_groups, fig_numline, C_ACCENT, C_WARM, C_GREEN)


def equal_groups(count, size, noun, color=C_ACCENT):
    """`count` groups of `size`, each labelled. Built from the same two
    numbers the times fact uses, so the picture always shows the fact."""
    assert 1 <= count <= 8 and 0 <= size <= 12, "equal_groups: out of range"
    return fig_groups(*[(size, "%s %d" % (noun, i + 1), color)
                        for i in range(count)])


def array(rows, cols_, color=C_ACCENT):
    """A rectangle drawn as `rows` rows of `cols_` — the picture whose two
    readings are the turnaround."""
    assert 1 <= rows <= 8 and 1 <= cols_ <= 12, "array: out of range"
    return fig_groups(*[(cols_, "row %d" % (i + 1), color) for i in range(rows)])


# ==========================================================================
# Lesson 1 — Equal Groups
# ==========================================================================

def lesson_equal_groups():
    g, s = 4, 3
    fig_gers = equal_groups(g, s, "ger")
    fig_plates = equal_groups(5, 2, "plate", C_WARM)
    fig_draw = equal_groups(3, 5, "circle", C_GREEN)
    return {
        "slug": "equal-groups",
        "title": "Equal Groups",
        "concreteComparison": (
            "Four gers stand by the river with $3$ horses tied at each "
            "one. You could count the horses by adding: $3 + 3 + 3 + 3 = "
            "12$. Multiplication says exactly the same thing in one short "
            "word — $4 \\times 3 = 12$, four groups of three."),
        "objective": (
            "Read a picture of equal groups as a times fact, write a "
            "times fact as repeated addition, and say why unequal groups "
            "have no times fact at all."),
        "concept": [
            "**Multiplication counts equal groups.** $4 \\times 3$ means "
            "$4$ groups with $3$ in each: $3 + 3 + 3 + 3 = 12$. The first "
            "number counts the GROUPS; the second says how many are IN "
            "one group.",
            "**The groups must all be the same size.** Groups of $3$, $3$ "
            "and $4$ have no single times fact, because the whole point "
            "of $\\times$ is that one number can speak for every group. "
            "When the groups differ, you have to add.",
            "**A fact and a picture say the same thing.** See $5$ plates "
            "with $2$ buuz on each and you can write $5 \\times 2 = 10$. "
            "Read $3 \\times 5$ and you can draw it: three circles with "
            "five dots in each, $15$ altogether. If you cannot say what "
            "the groups are, you are not multiplying yet.",
        ],
        "keyIdea": (
            "A times fact is repeated addition wearing a short name: the "
            "first number counts the equal groups, the second counts "
            "inside one group."),
        "facts": [
            {"title": "Groups of",
             "latex": "4 \\times 3 = 3 + 3 + 3 + 3 = 12",
             "explanation": "Four groups of three — the times sign is shorthand for the repeated sum."},
            {"title": "Equal or nothing",
             "latex": "3 + 3 + 4 \\ne 3 \\times 3",
             "explanation": "Unequal groups have no times name; 3 × 3 = 9 but the picture holds 10."},
        ],
        "workedExamples": [
            {"id": "g3mu-l1-we1",
             "statement": "Four gers each have $%d$ horses tied outside. Write the repeated addition and the times fact." % s,
             "note": "Count the groups first, then look inside one group.",
             "solution": ("Four groups of three: $3 + 3 + 3 + 3 = 12$. In one "
                          "word, $4 \\times 3 = 12$ — twelve horses, counted at "
                          "a stroke instead of one at a time."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3 + 3 + 3 + 3, 12)", "Eq(4*3, 12)"]},
            {"id": "g3mu-l1-we2",
             "statement": "A drawing shows groups of $4$, $4$, $4$ and $3$ apples. Can one times fact count them?",
             "note": "Check whether every group is the same size.",
             "solution": ("No — one group is a different size. The total is "
                          "$4 + 4 + 4 + 3 = 15$, but four equal groups of four "
                          "would be $4 \\times 4 = 16$, one apple too many. When "
                          "the groups differ you must add."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4 + 4 + 4 + 3, 15)", "Eq(4*4, 16)", "Ne(15, 16)"]},
        ],
        "commonMistakes": [
            {"text": "Adding the two numbers — reading 4 × 3 as 4 + 3 = 7.",
             "correction": "The times sign counts GROUPS: four groups of three is 3 + 3 + 3 + 3 = 12. Adding counts the number of groups and one group together, which answers nothing.",
             "authored": True},
            {"text": "Writing a times fact for unequal groups, calling 3, 3 and 4 \"3 × 3\".",
             "correction": "3 × 3 = 9, but the picture holds 3 + 3 + 4 = 10. Multiplication needs every group the same size; if one differs, add.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3mu-l1-t1",
             "statement": "Write $5 \\times 2$ as repeated addition and find it.",
             "solution": "Five groups of two: $2 + 2 + 2 + 2 + 2 = 10$, so $5 \\times 2 = 10$.",
             "check": ["Eq(2 + 2 + 2 + 2 + 2, 10)", "Eq(5*2, 10)"]},
            {"id": "g3mu-l1-t2",
             "statement": "A picture shows $3$ nests with $4$ eggs in each. Write the times fact and the total.",
             "solution": "Three groups of four: $4 + 4 + 4 = 12$, so $3 \\times 4 = 12$ eggs.",
             "check": ["Eq(4 + 4 + 4, 12)", "Eq(3*4, 12)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Groups of the same size", [
                "Four gers, three horses tied at each — the picture below. To count them you could add: $3 + 3 + 3 + 3 = 12$.",
                "Multiplication says it in one word: $4 \\times 3 = 12$, read \"four groups of three\". The first number counts the GROUPS; the second counts inside ONE group.",
                "The times sign carries a promise: every group is the same size. That promise is what lets one short fact stand in for a long sum.",
            ]), fig_gers),
            workedset("From picture to fact",
                      "Count the groups, look inside one, write the fact.", [
                wex("Four gers, $3$ horses at each. The sum and the fact?",
                    ["Four groups of three: $3 + 3 + 3 + 3 = 12$.",
                     "In one word: $4 \\times 3 = 12$."],
                    "$4 \\times 3 = 12$",
                    ["Eq(3 + 3 + 3 + 3, 12)", "Eq(4*3, 12)"]),
                wex("Five plates with $2$ buuz on each. The sum and the fact?",
                    ["$2 + 2 + 2 + 2 + 2 = 10$.",
                     "$5 \\times 2 = 10$ — five groups of two."],
                    "$5 \\times 2 = 10$",
                    ["Eq(2 + 2 + 2 + 2 + 2, 10)", "Eq(5*2, 10)"]),
            ]),
            tryitset("Read the groups", "Groups first, then inside one group.", [
                withfig(tp("The picture shows $5$ plates with $2$ buuz on each. The times fact is:",
                   ["$5 \\times 2 = 10$", "$5 + 2 = 7$", "$2 \\times 2 = 4$"],
                   "Five groups of two: $2 + 2 + 2 + 2 + 2 = 10$, so $5 \\times 2 = 10$. Writing $5 + 2 = 7$ adds the group count to one group — the classic mix-up.",
                   ["Eq(2 + 2 + 2 + 2 + 2, 10)", "Eq(5 + 2, 7)"]), fig_plates),
                tp("Three groups of $4$ written as repeated addition is:",
                   ["$4 + 4 + 4 = 12$", "$3 + 3 + 3 = 9$", "$4 + 3 = 7$"],
                   "Three groups, four in each: add the $4$ three times to get $12$, which is $3 \\times 4$. Adding threes counts the wrong thing three times.",
                   ["Eq(4 + 4 + 4, 12)", "Eq(3 + 3 + 3, 9)"]),
                tp("Which story matches $4 \\times 5$?",
                   ["$4$ boxes with $5$ pencils in each",
                    "$4$ pencils and $5$ more pencils",
                    "one box with $9$ pencils"],
                   "Four groups of five: $4 \\times 5 = 20$ pencils. The other two stories are additions — $4 + 5 = 9$ — and an addition is not a times story.",
                   ["Eq(4*5, 20)", "Eq(4 + 5, 9)"]),
            ]),
            tapq("The broken promise", "A drawing shows groups of $4$, $4$, $4$ and $3$ apples. Can one times fact count it?",
                 ["no — one group is a different size",
                  "yes: $4 \\times 4 = 16$",
                  "yes: $4 \\times 3 = 12$",
                  "yes: $3 \\times 4 = 12$"],
                 "The total is $4 + 4 + 4 + 3 = 15$, but $4 \\times 4 = 16$ counts one apple too many. The times sign promises EQUAL groups, and this picture breaks the promise — so add instead.",
                 ["Eq(4 + 4 + 4 + 3, 15)", "Eq(4*4, 16)", "Ne(15, 16)"]),
            funfact("Count the legs, not the horses",
                    "A horse stands on $4$ legs, so a string of $5$ horses stands on $5 \\times 4 = 20$ legs — no need to count leg by leg. Multiplication was invented for exactly this moment: whenever the world hands you equal groups, one fact counts them all at once."),
            withfig(teach("Concept B", "From fact back to picture", [
                "Facts translate back into pictures. To draw $3 \\times 5$, draw $3$ groups with $5$ in each — like the picture below — and the count confirms it: $5 + 5 + 5 = 15$.",
                "Reading order matters for the drawing: $3 \\times 5$ makes $3$ groups of $5$, while $5 \\times 3$ makes $5$ groups of $3$. Two different pictures — and next lesson you will discover their totals secretly agree.",
                "If you can draw the picture, you own the fact. Drawing is not a beginner's crutch; it is the check that you know what the numbers mean.",
            ]), fig_draw),
            workedset("From fact to picture",
                      "Say the groups aloud, then draw and count.", [
                wex("Draw $3 \\times 5$ and find the total.",
                    ["Three circles, five dots in each.",
                     "Count: $5 + 5 + 5 = 15$, so $3 \\times 5 = 15$."],
                    "$15$",
                    ["Eq(5 + 5 + 5, 15)", "Eq(3*5, 15)"]),
                wex("Saruul draws $2$ baskets with $4$ eggs in each. Which fact did she draw?",
                    ["Two groups of four: $4 + 4 = 8$.",
                     "$2 \\times 4 = 8$."],
                    "$2 \\times 4 = 8$",
                    ["Eq(4 + 4, 8)", "Eq(2*4, 8)"]),
            ]),
            tryitset("Draw it in your head",
                     "Groups from the first number, size from the second.", [
                tp("To draw $4 \\times 2$ you draw:",
                   ["$4$ groups with $2$ in each",
                    "$4$ groups with $4$ in each",
                    "$2$ groups with $2$ in each"],
                   "First number counts the groups, second the size: four groups of two, totalling $8$. Four groups of four would be $16$ — a much bigger picture.",
                   ["Eq(4*2, 8)", "Eq(4*4, 16)"]),
                tp("A picture of $2$ baskets with $5$ eggs each shows:",
                   ["$2 \\times 5 = 10$", "$2 + 5 = 7$", "$5 \\times 5 = 25$"],
                   "Two groups of five: $5 + 5 = 10$ eggs. Adding gives $7$, which counts the baskets and one basket's eggs together.",
                   ["Eq(5 + 5, 10)", "Eq(2*5, 10)", "Eq(2 + 5, 7)"]),
                tp("Which drawing does NOT show a times fact?",
                   ["groups of $2$, $3$ and $2$",
                    "groups of $3$, $3$ and $3$",
                    "groups of $2$, $2$, $2$ and $2$"],
                   "The first has unequal groups, so no single times fact fits: it totals $2 + 3 + 2 = 7$. The others are $3 \\times 3 = 9$ and $4 \\times 2 = 8$.",
                   ["Eq(2 + 3 + 2, 7)", "Eq(3*3, 9)", "Eq(4*2, 8)"]),
            ]),
            tapq("Which number counts the groups?", "In $5 \\times 3$, what does the $5$ count?",
                 ["the number of groups", "how many are in each group",
                  "the total", "nothing — the order does not matter"],
                 "The first number counts the GROUPS: five groups of three, $3 + 3 + 3 + 3 + 3 = 15$. (The total does turn out the same as $3 \\times 5$ — but the pictures are different, which is next lesson's discovery.)",
                 ["Eq(3 + 3 + 3 + 3 + 3, 15)", "Eq(5*3, 15)"]),
            recap([
                "$4 \\times 3$ means four groups of three: $3 + 3 + 3 + 3 = 12$.",
                "The first number counts the groups; the second counts inside one group.",
                "Every group must be the SAME size, or there is no times fact — you must add.",
                "A times fact and its picture always say the same thing; if you can draw it, you own it.",
            ]),
            tip("Say every times fact out loud as \"groups of\" — \"four groups of three\" — before you work it out. The words stop $4 \\times 3$ from ever turning into $4 + 3$."),
            tryitset("Chapter practice", "Groups, then size, then total.", [
                tp("$3 \\times 2$ as repeated addition is:",
                   ["$2 + 2 + 2 = 6$", "$3 + 3 = 6$", "$3 + 2 = 5$"],
                   "Three groups of two: add the $2$ three times. Both of the first two answers happen to reach $6$, but only one of them is the picture $3 \\times 2$ describes — three groups, not two.",
                   ["Eq(2 + 2 + 2, 6)", "Eq(3*2, 6)", "Eq(3 + 3, 6)"]),
                tp("A shelf holds $4$ boxes with $5$ books in each. The total is:",
                   ["$20$ books", "$9$ books", "$45$ books"],
                   "Four groups of five: $5 + 5 + 5 + 5 = 20$. Adding gives $9$, and writing the digits side by side gives $45$ — neither counts the books.",
                   ["Eq(5 + 5 + 5 + 5, 20)", "Eq(4*5, 20)", "Eq(4 + 5, 9)"]),
                tp("Which sum could be written as a times fact?",
                   ["$6 + 6 + 6$", "$6 + 5 + 6$", "$6 + 6 + 5$"],
                   "Only the first has all its groups equal: $3 \\times 6 = 18$. The others total $17$ each and need adding, because one group is the wrong size.",
                   ["Eq(6 + 6 + 6, 18)", "Eq(3*6, 18)", "Eq(6 + 5 + 6, 17)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Equal Groups\"",
                    "You now know what multiplication IS, which is worth more than any number of memorised facts. Next you will meet the array — a way of drawing groups that reveals something surprising about the order of the two numbers.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Arrays and the Turnaround
# ==========================================================================

def lesson_arrays():
    r, c = 3, 4
    fig_rows = array(r, c)
    fig_cols = array(c, r, C_WARM)
    fig_25 = array(2, 5, C_GREEN)
    return {
        "slug": "arrays-and-the-turnaround",
        "title": "Arrays & the Turnaround",
        "concreteComparison": (
            "Stones are laid out in a neat rectangle: $3$ rows with $4$ "
            "stones in each. Read it by rows and you see $3 \\times 4$. "
            "Turn your head and read it by columns and you see $4 \\times "
            "3$. Same stones, same total — two facts for the price of "
            "one."),
        "objective": (
            "Read an array as a times fact in two ways, use the "
            "turnaround to get a second fact free, and say why the two "
            "orders must agree."),
        "concept": [
            "**An array is equal groups laid out in a rectangle.** $3$ "
            "rows of $4$ is $3$ groups of $4$: $4 + 4 + 4 = 12$. Rows are "
            "the groups and the row length is the group size.",
            "**The same rectangle read the other way gives the other "
            "fact.** Those same stones form $4$ columns of $3$: "
            "$3 + 3 + 3 + 3 = 12$. So $3 \\times 4 = 4 \\times 3$, and "
            "neither reading is more correct than the other.",
            "**That halves what you have to learn.** Every fact you know "
            "hands you its partner for free: knowing $2 \\times 5 = 10$ "
            "means you already know $5 \\times 2 = 10$. The stones cannot "
            "change in number just because you tilted your head.",
        ],
        "keyIdea": (
            "One rectangle, two readings, one total — so $a \\times b$ "
            "and $b \\times a$ are always equal, and every fact you learn "
            "comes with a partner."),
        "facts": [
            {"title": "Two readings of one array",
             "latex": "3 \\times 4 = 4 \\times 3 = 12",
             "explanation": "Rows give one fact, columns the other; the stones never moved."},
            {"title": "A free partner",
             "latex": "2 \\times 5 = 5 \\times 2 = 10",
             "explanation": "Learn one order and the other arrives without any extra work."},
        ],
        "workedExamples": [
            {"id": "g3mu-l2-we1",
             "statement": "An array has $%d$ rows of $%d$ stones. Write both times facts it proves." % (r, c),
             "note": "Read it by rows, then by columns.",
             "solution": ("By rows: $3$ groups of $4$, so $3 \\times 4 = 12$. By "
                          "columns: $4$ groups of $3$, so $4 \\times 3 = 12$. "
                          "One rectangle, two facts, and the count is $12$ "
                          "either way."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*4, 12)", "Eq(4*3, 12)", "Eq(4 + 4 + 4, 12)"]},
            {"id": "g3mu-l2-we2",
             "statement": "Saruul knows $2 \\times 5 = 10$. What does she also know, without doing any work?",
             "note": "Turn the array round.",
             "solution": ("She also knows $5 \\times 2 = 10$. Two rows of five "
                          "and five rows of two are the same rectangle seen from "
                          "two sides, so the total cannot change: "
                          "$5 + 5 = 10$ and $2 + 2 + 2 + 2 + 2 = 10$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*5, 10)", "Eq(5*2, 10)", "Eq(5 + 5, 10)",
                       "Eq(2 + 2 + 2 + 2 + 2, 10)"]},
        ],
        "commonMistakes": [
            {"text": "Thinking 3 × 4 and 4 × 3 must be different because the pictures look different.",
             "correction": "The pictures ARE different — three rows of four is not four rows of three. But they contain the same stones, so both count 12. Different arrangement, same total.",
             "authored": True},
            {"text": "Counting the rows as the total — answering \"3 rows of 4\" with 3.",
             "correction": "The rows are the groups, not the answer. Three groups of four holds 4 + 4 + 4 = 12 stones altogether.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3mu-l2-t1",
             "statement": "An array has $2$ rows of $4$. Write both facts and the total.",
             "solution": ("By rows: $2 \\times 4 = 8$. By columns: $4 \\times 2 = "
                          "8$. Total $8$ either way, since $4 + 4 = 8$."),
             "check": ["Eq(2*4, 8)", "Eq(4*2, 8)", "Eq(4 + 4, 8)"]},
            {"id": "g3mu-l2-t2",
             "statement": "If $4 \\times 5 = 20$, what is $5 \\times 4$? Explain without calculating.",
             "solution": ("$5 \\times 4 = 20$ too. It is the same rectangle read "
                          "along the other side — no stones were added or taken "
                          "away, so the total cannot have changed."),
             "check": ["Eq(4*5, 20)", "Eq(5*4, 20)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "A rectangle of equal groups", [
                "The stones below are laid out in $3$ rows with $4$ in each — an array.",
                "Reading by rows, that is $3$ groups of $4$: $4 + 4 + 4 = 12$, or $3 \\times 4 = 12$.",
                "An array is just equal groups tidied into straight lines, and the tidiness is what makes the next discovery possible.",
            ]), fig_rows),
            workedset("Read an array by rows",
                      "Rows are the groups; the row length is the group size.", [
                wex("An array has $3$ rows of $4$. What is the total?",
                    ["Three groups of four: $4 + 4 + 4 = 12$.",
                     "So $3 \\times 4 = 12$."],
                    "$12$",
                    ["Eq(4 + 4 + 4, 12)", "Eq(3*4, 12)"]),
                wex("An array has $2$ rows of $5$. What is the total?",
                    ["Two groups of five: $5 + 5 = 10$.",
                     "So $2 \\times 5 = 10$."],
                    "$10$",
                    ["Eq(5 + 5, 10)", "Eq(2*5, 10)"]),
            ]),
            tryitset("Count the array", "Groups down the side, size along the row.", [
                withfig(tp("The array below has $3$ rows of $4$. The total is:",
                   ["$12$", "$7$", "$3$"],
                   "Three groups of four: $4 + 4 + 4 = 12$. Adding the two numbers gives $7$, and answering $3$ counts only the rows.",
                   ["Eq(4 + 4 + 4, 12)", "Eq(3*4, 12)", "Eq(3 + 4, 7)"]), fig_rows),
                tp("An array of $4$ rows of $2$ holds:",
                   ["$8$", "$6$", "$42$"],
                   "Four groups of two: $2 + 2 + 2 + 2 = 8$. Adding gives $6$, and writing the digits together gives $42$ — neither counts anything in the picture.",
                   ["Eq(2 + 2 + 2 + 2, 8)", "Eq(4*2, 8)", "Eq(4 + 2, 6)"]),
                tp("Which array holds the MOST?",
                   ["$4$ rows of $5$", "$3$ rows of $5$", "$4$ rows of $4$"],
                   "$4 \\times 5 = 20$ beats $3 \\times 5 = 15$ and $4 \\times 4 = 16$. Adding a whole row of five gains more than adding one to each row.",
                   ["Eq(4*5, 20)", "Eq(3*5, 15)", "Eq(4*4, 16)", "20 > 16"]),
            ]),
            tapq("Rows or total?", "An array has $3$ rows of $4$ stones. How many stones are there?",
                 ["$12$", "$3$", "$4$", "$7$"],
                 "The rows are the groups, not the answer: $4 + 4 + 4 = 12$ stones. Answering $3$ counts the rows and $4$ counts one row.",
                 ["Eq(4 + 4 + 4, 12)", "Eq(3*4, 12)"]),
            funfact("Why market stalls stack in rectangles",
                    "Eggs come in trays, tiles come in sheets, and soldiers stand in squares — all for the same reason. A rectangle can be counted without counting: two quick numbers along the sides give the total, and anyone can check it from a distance. The array is the oldest counting trick still in daily use."),
            withfig(teach("Concept B", "Turn it round", [
                "Here is the SAME rectangle of stones, read the other way: $4$ columns with $3$ in each.",
                "That reading says $4 \\times 3$, and counting gives $3 + 3 + 3 + 3 = 12$ — exactly what the row reading gave. So $3 \\times 4 = 4 \\times 3$.",
                "This is the turnaround, and it is a genuine bargain: every fact you learn hands you a second one free. Know $2 \\times 5 = 10$ and you already know $5 \\times 2 = 10$ without lifting a pencil.",
            ]), fig_cols),
            workedset("Use the turnaround",
                      "One fact, then its partner, at no extra cost.", [
                wex("An array has $3$ rows of $4$. Write BOTH facts.",
                    ["Rows: $3 \\times 4 = 12$.",
                     "Columns: $4 \\times 3 = 12$.",
                     "Same stones, so the totals must match."],
                    "$3 \\times 4 = 4 \\times 3 = 12$",
                    ["Eq(3*4, 12)", "Eq(4*3, 12)"]),
                wex("You know $2 \\times 5 = 10$. What else do you know?",
                    ["Turn the array: $5 \\times 2$.",
                     "$2 + 2 + 2 + 2 + 2 = 10$, so $5 \\times 2 = 10$ as well."],
                    "$5 \\times 2 = 10$",
                    ["Eq(2*5, 10)", "Eq(5*2, 10)",
                     "Eq(2 + 2 + 2 + 2 + 2, 10)"]),
            ]),
            tryitset("The free fact", "Turn the array; the total cannot change.", [
                withfig(tp("This array shows $2$ rows of $5$. Which pair of facts does it prove?",
                   ["$2 \\times 5 = 10$ and $5 \\times 2 = 10$",
                    "$2 \\times 5 = 10$ and $5 \\times 2 = 7$",
                    "$2 + 5 = 7$ and $5 + 2 = 7$"],
                   "Rows give $2 \\times 5 = 10$ and columns give $5 \\times 2 = 10$. The two orders must agree because they count the same stones.",
                   ["Eq(2*5, 10)", "Eq(5*2, 10)", "Eq(2 + 5, 7)"]), fig_25),
                tp("If $3 \\times 5 = 15$, then $5 \\times 3$ is:",
                   ["$15$", "$8$", "$35$"],
                   "The turnaround: the same rectangle read the other way, so the total is unchanged at $15$. Adding gives $8$ and running the digits together gives $35$.",
                   ["Eq(3*5, 15)", "Eq(5*3, 15)", "Eq(3 + 5, 8)"]),
                tp("Saruul has learned the $5$ times table. Which fact does she NOT yet get free?",
                   ["$3 \\times 4$", "$3 \\times 5$", "$4 \\times 5$"],
                   "$3 \\times 5$ and $4 \\times 5$ are in her table already, and their turnarounds come free. But $3 \\times 4 = 12$ has no five in it at all, so it must be learned separately.",
                   ["Eq(3*4, 12)", "Eq(3*5, 15)", "Eq(4*5, 20)"]),
            ]),
            tapq("Why must they agree?", "Why is $4 \\times 3$ equal to $3 \\times 4$?",
                 ["they count the same array from two sides",
                  "because both answers end in the same digit",
                  "they are not equal — the pictures differ",
                  "it is a rule with no reason"],
                 "The rectangle does not change when you tilt your head, so the count cannot change either: $3 + 3 + 3 + 3 = 12$ and $4 + 4 + 4 = 12$. The pictures genuinely differ, but they hold the same stones.",
                 ["Eq(3 + 3 + 3 + 3, 12)", "Eq(4 + 4 + 4, 12)",
                  "Eq(4*3, 3*4)"]),
            recap([
                "An array is equal groups laid out in a rectangle: rows are the groups.",
                "Read by rows and by columns to get two facts from one picture.",
                "$3 \\times 4 = 4 \\times 3$ — the turnaround — because the stones never moved.",
                "Every fact you learn comes with a free partner, halving what there is to remember.",
            ]),
            tip("Whenever you learn a new times fact, write its turnaround underneath straight away. Two facts learned in the time it takes to learn one is the best bargain in arithmetic."),
            tryitset("Chapter practice", "Two readings, one total.", [
                tp("An array of $5$ rows of $4$ holds:",
                   ["$20$", "$9$", "$54$"],
                   "Five groups of four: $4 + 4 + 4 + 4 + 4 = 20$, which is also $4 \\times 5$ read down the columns.",
                   ["Eq(5*4, 20)", "Eq(4*5, 20)", "Eq(5 + 4, 9)"]),
                tp("Knowing $4 \\times 2 = 8$ also tells you:",
                   ["$2 \\times 4 = 8$", "$4 + 2 = 8$", "$8 \\times 2 = 4$"],
                   "The turnaround gives $2 \\times 4 = 8$ free. Note $4 + 2 = 6$, not $8$ — the middle option is simply false.",
                   ["Eq(4*2, 8)", "Eq(2*4, 8)", "Eq(4 + 2, 6)"]),
                tp("Which two facts come from ONE array?",
                   ["$2 \\times 3$ and $3 \\times 2$",
                    "$2 \\times 3$ and $2 \\times 4$",
                    "$3 \\times 3$ and $3 \\times 4$"],
                   "Only a turnaround pair shares a rectangle: $2 \\times 3 = 6$ and $3 \\times 2 = 6$. The other pairs are different rectangles with different totals.",
                   ["Eq(2*3, 6)", "Eq(3*2, 6)", "Eq(2*4, 8)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Arrays & the Turnaround\"",
                    "You have just halved the size of every times table you will ever learn. From here on, each new fact you meet quietly delivers its partner as well — and the tables in the next two lessons are much shorter than they look.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — The Tables of 2, 5 and 10
# ==========================================================================

def lesson_friendly_tables():
    fig_twos = fig_numline([(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"),
                            (10, "10")], lo=0, hi=10)
    fig_fives = fig_numline([(0, "0"), (5, "5"), (10, "10"), (15, "15"),
                             (20, "20"), (25, "25")], lo=0, hi=25)
    # Six whole bundles of ten — the picture for the 10 x 6 question below.
    fig_tens = fig_groups(*[(10, "ten %d" % (i + 1), C_ACCENT) for i in range(6)])
    return {
        "slug": "tables-of-2-5-and-10",
        "title": "The Tables of 2, 5 and 10",
        "concreteComparison": (
            "You already know these tables — you learned them while "
            "counting in steps. Counting $2, 4, 6, 8$ IS the two times "
            "table; counting $5, 10, 15, 20$ is the five. All that is "
            "left is to notice the patterns that make them impossible to "
            "get wrong."),
        "objective": (
            "Recall the tables of $2$, $5$ and $10$, use the endings of "
            "the answers to check them, and connect each table to a step "
            "count you already know."),
        "concept": [
            "**The two times table is doubling, and every answer is "
            "even.** $2 \\times 1 = 2$, $2 \\times 2 = 4$, up to "
            "$2 \\times 10 = 20$. Every answer ends in $0, 2, 4, 6$ or "
            "$8$ — an odd ending means you have slipped.",
            "**The five times table alternates its endings.** "
            "$5, 10, 15, 20, 25, \\ldots$ — an odd number of fives ends "
            "in $5$, and an even number of fives pairs up into whole "
            "tens and ends in $0$.",
            "**The ten times table is the easiest of all.** $3 \\times "
            "10 = 30$: three whole bundles of ten. Every answer ends in "
            "$0$, and the other digit is simply the number you started "
            "with.",
        ],
        "keyIdea": (
            "The friendly tables are step counts you already know, and "
            "each one leaves a fingerprint in the endings that checks "
            "your answer for free."),
        "facts": [
            {"title": "Twos are doubles",
             "latex": "2 \\times 7 = 14",
             "explanation": "Double seven; every answer in this table is even."},
            {"title": "Fives alternate",
             "latex": "5 \\times 6 = 30",
             "explanation": "An even count of fives pairs into whole tens, so it ends in 0."},
        ],
        "workedExamples": [
            {"id": "g3mu-l3-we1",
             "statement": "Find $2 \\times 7$ and check the answer with the twos pattern.",
             "note": "Doubling is the fastest route.",
             "solution": ("Double seven: $7 + 7 = 14$, so $2 \\times 7 = 14$. "
                          "The check is the ending — $14$ is even, as every "
                          "answer in the two times table must be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(7 + 7, 14)", "Eq(2*7, 14)", "Eq(Mod(14, 2), 0)"]},
            {"id": "g3mu-l3-we2",
             "statement": "Find $5 \\times 6$ and $5 \\times 7$, and explain their different endings.",
             "note": "Count fives, then look at the last digit.",
             "solution": ("$5 \\times 6 = 30$ and $5 \\times 7 = 35$. Six fives "
                          "pair into three whole tens, so the answer ends in "
                          "$0$; seven fives leave one five unpaired, so the "
                          "answer ends in $5$. Even counts of five end in $0$, "
                          "odd counts end in $5$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*6, 30)", "Eq(Mod(30, 10), 0)", "Eq(5*7, 35)",
                       "Eq(Mod(35, 10), 5)"]},
        ],
        "commonMistakes": [
            {"text": "Answering 2 × 7 with 9, adding instead of doubling.",
             "correction": "2 × 7 means two groups of seven: 7 + 7 = 14. Adding gives 9, which is odd — and no answer in the two times table can be odd.",
             "authored": True},
            {"text": "Giving an answer in the five times table that ends in something other than 0 or 5, such as 5 × 6 = 32.",
             "correction": "Every multiple of five ends in 5 or 0. 5 × 6 = 30, and an ending of 2 is a signal to count again.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3mu-l3-t1",
             "statement": "Find $2 \\times 9$ and say how the ending confirms it.",
             "solution": ("Double nine: $9 + 9 = 18$, so $2 \\times 9 = 18$. It "
                          "is even, as every answer in this table must be."),
             "check": ["Eq(9 + 9, 18)", "Eq(2*9, 18)", "Eq(Mod(18, 2), 0)"]},
            {"id": "g3mu-l3-t2",
             "statement": "Find $10 \\times 7$ and explain the pattern in the digits.",
             "solution": ("Seven whole tens: $10 \\times 7 = 70$. The answer is "
                          "the starting number with a $0$ after it, because each "
                          "ten is one full bundle and seven bundles is seven "
                          "tens."),
             "check": ["Eq(10*7, 70)", "Eq(Mod(70, 10), 0)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Twos and fives are step counts", [
                "The line below counts in twos: $0, 2, 4, 6, 8, 10$. You already learned this as step counting — and it IS the two times table.",
                "$2 \\times 4$ is simply the fourth stop: $8$. Doubling gets you there fastest of all: $4 + 4 = 8$.",
                "Every answer is even, because two equal groups can always be paired off with nothing left over. An odd answer in this table is impossible.",
            ]), fig_twos),
            workedset("Twos by doubling", "Double the other number.", [
                wex("Find $2 \\times 7$.",
                    ["Double seven: $7 + 7 = 14$.",
                     "$2 \\times 7 = 14$, and $14$ is even ✓."],
                    "$14$",
                    ["Eq(7 + 7, 14)", "Eq(2*7, 14)", "Eq(Mod(14, 2), 0)"]),
                wex("Find $2 \\times 8$.",
                    ["Double eight: $8 + 8 = 16$.",
                     "$2 \\times 8 = 16$, even as expected ✓."],
                    "$16$",
                    ["Eq(8 + 8, 16)", "Eq(2*8, 16)", "Eq(Mod(16, 2), 0)"]),
            ]),
            tryitset("Twos", "Double it, then check the ending is even.", [
                tp("$2 \\times 6$ is:",
                   ["$12$", "$8$", "$26$"],
                   "Double six: $6 + 6 = 12$. Adding gives $8$, and running the digits together gives $26$ — neither is doubling.",
                   ["Eq(6 + 6, 12)", "Eq(2*6, 12)", "Eq(2 + 6, 8)"]),
                tp("$2 \\times 9$ is:",
                   ["$18$", "$11$", "$19$"],
                   "Double nine: $9 + 9 = 18$. An answer of $11$ adds instead, and $19$ is odd — impossible in the two times table.",
                   ["Eq(9 + 9, 18)", "Eq(2*9, 18)", "Eq(Mod(19, 2), 1)"]),
                tp("Which answer CANNOT belong to the two times table?",
                   ["$15$", "$14$", "$16$"],
                   "$15$ is odd, and two equal groups always pair off exactly. $14 = 2 \\times 7$ and $16 = 2 \\times 8$ are both fine.",
                   ["Eq(Mod(15, 2), 1)", "Eq(2*7, 14)", "Eq(2*8, 16)"]),
            ]),
            tapq("The impossible answer", "A pupil answers $2 \\times 7 = 15$. How do you know it is wrong without recounting?",
                 ["$15$ is odd, and every answer in the twos is even",
                  "$15$ is too small",
                  "$15$ does not end in $5$",
                  "you cannot know without recounting"],
                 "Two equal groups always pair off with nothing left over, so every answer in this table is even. The true answer is $7 + 7 = 14$.",
                 ["Eq(Mod(15, 2), 1)", "Eq(2*7, 14)", "Eq(Mod(14, 2), 0)"]),
            funfact("Why fives feel so easy",
                    "Five is half of ten, so counting in fives is really counting half-bundles — and two of them always click together into a whole ten. That is why the answers alternate $5, 0, 5, 0$: each pair of fives completes a ten and resets the ending. Your hands are the original reason ten matters at all."),
            withfig(teach("Concept B", "Fives and tens", [
                "The line below counts in fives: $0, 5, 10, 15, 20, 25$. Look only at the last digits — $0, 5, 0, 5, 0, 5$, forever.",
                "The reason is that two fives make a ten. An EVEN number of fives pairs up completely and ends in $0$; an ODD number leaves one five over and ends in $5$. So $5 \\times 6 = 30$ but $5 \\times 7 = 35$.",
                "The ten times table is easier still: $3 \\times 10 = 30$ is three whole bundles of ten. Write the number, add a zero, done.",
            ]), fig_fives),
            workedset("Fives and tens", "Count the fives; pair them into tens.", [
                wex("Find $5 \\times 6$.",
                    ["Six fives: $5, 10, 15, 20, 25, 30$.",
                     "Six is even, so they pair into three whole tens.",
                     "$5 \\times 6 = 30$, ending in $0$ ✓."],
                    "$30$",
                    ["Eq(5*6, 30)", "Eq(Mod(30, 10), 0)", "Eq(3*10, 30)"]),
                wex("Find $10 \\times 4$.",
                    ["Four whole bundles of ten.",
                     "$10 + 10 + 10 + 10 = 40$.",
                     "$10 \\times 4 = 40$ — the number with a zero after it."],
                    "$40$",
                    ["Eq(10 + 10 + 10 + 10, 40)", "Eq(10*4, 40)"]),
            ]),
            tryitset("Fives and tens", "Check the ending before you commit.", [
                tp("$5 \\times 8$ is:",
                   ["$40$", "$45$", "$13$"],
                   "Eight fives pair into four whole tens: $40$, ending in $0$ as an even count of fives must. $45$ would need an odd count, and $13$ adds instead.",
                   ["Eq(5*8, 40)", "Eq(Mod(40, 10), 0)", "Eq(5 + 8, 13)"]),
                tp("$5 \\times 9$ is:",
                   ["$45$", "$40$", "$14$"],
                   "Nine fives: eight of them pair into $40$, and one five is left over — $45$. An odd count of fives always ends in $5$.",
                   ["Eq(5*9, 45)", "Eq(Mod(45, 10), 5)", "Eq(40 + 5, 45)"]),
                withfig(tp("The picture shows $6$ bundles of ten. $10 \\times 6$ is:",
                   ["$60$", "$16$", "$610$"],
                   "Six whole bundles of ten: $60$. Adding gives $16$, and writing the digits side by side gives $610$.",
                   ["Eq(10*6, 60)", "Eq(10 + 6, 16)"]), fig_tens),
            ]),
            tapq("Odd or even count of fives?", "Which of these could be an answer in the five times table?",
                 ["$35$", "$32$", "$34$", "$38$"],
                 "Every multiple of five ends in $5$ or $0$, and only $35$ does — it is $5 \\times 7$. The others all end in even digits that fives never produce.",
                 ["Eq(5*7, 35)", "Eq(Mod(35, 5), 0)", "Eq(Mod(32, 5), 2)"]),
            recap([
                "The two times table is doubling, and every answer is even.",
                "The five times table ends in $5$ (odd count) or $0$ (even count), because two fives make a ten.",
                "The ten times table writes the number with a zero after it: $10 \\times 7 = 70$.",
                "Each table's endings are a free check — a wrong ending means a wrong answer.",
            ]),
            tip("When an answer in these tables feels uncertain, check its ENDING first. It takes no time at all and it catches most slips before you have to count anything again."),
            tryitset("Chapter practice", "Double, pair, or bundle.", [
                tp("$2 \\times 10$ is:",
                   ["$20$", "$12$", "$210$"],
                   "Double ten, or one bundle of ten twice: $20$. This fact sits in both the twos and the tens table, which is why it feels so familiar.",
                   ["Eq(2*10, 20)", "Eq(10 + 10, 20)", "Eq(2 + 10, 12)"]),
                tp("$5 \\times 4$ is:",
                   ["$20$", "$25$", "$9$"],
                   "Four fives pair into two whole tens: $20$. And the turnaround gives $4 \\times 5 = 20$ free.",
                   ["Eq(5*4, 20)", "Eq(4*5, 20)", "Eq(Mod(20, 10), 0)"]),
                tp("Which fact is WRONG?",
                   ["$5 \\times 6 = 35$", "$2 \\times 6 = 12$",
                    "$10 \\times 3 = 30$"],
                   "Six fives is an even count, so the answer must end in $0$: $5 \\times 6 = 30$, not $35$. The other two are correct.",
                   ["Eq(5*6, 30)", "Ne(5*6, 35)", "Eq(2*6, 12)",
                    "Eq(10*3, 30)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"The Tables of 2, 5 and 10\"",
                    "Three tables, and you barely had to learn anything — they were step counts you already owned. The next lesson does the same trick again: the threes and fours are built out of the twos you have just confirmed.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — The Tables of 3 and 4
# ==========================================================================

def lesson_threes_fours():
    fig_threes = fig_numline([(0, "0"), (3, "3"), (6, "6"), (9, "9"),
                              (12, "12"), (15, "15")], lo=0, hi=15)
    fig_double = fig_groups((6, "2 x 3 = 6", C_ACCENT),
                            (12, "double it: 4 x 3 = 12", C_WARM))
    fig_4x6 = array(4, 6, C_GREEN)
    return {
        "slug": "tables-of-3-and-4",
        "title": "The Tables of 3 and 4",
        "concreteComparison": (
            "The threes and fours look harder than the friendly tables, "
            "but they are not new work. Counting in threes gives the "
            "whole three times table, and every four times fact is "
            "simply a two times fact doubled."),
        "objective": (
            "Recall the tables of $3$ and $4$, build any four times fact "
            "by doubling a two times fact, and use a known fact to reach "
            "the one beside it."),
        "concept": [
            "**The three times table is counting in threes.** $3, 6, 9, "
            "12, 15, \\ldots$ — the same step count, now with names: "
            "$3 \\times 4 = 12$ is the fourth stop.",
            "**Every four times fact is a doubled two times fact.** "
            "$4 \\times 3$ is twice $2 \\times 3$: $2 \\times 3 = 6$, and "
            "doubling gives $12$. That works because four groups is two "
            "groups counted twice.",
            "**A fact you own reaches the fact beside it.** If "
            "$3 \\times 5 = 15$, then $3 \\times 6$ is one more group of "
            "three: $15 + 3 = 18$. Stepping one group along is always "
            "cheaper than starting the count again.",
        ],
        "keyIdea": (
            "Build the fact you need from a fact you already own — count "
            "on by one group, or double a two times fact to reach a four "
            "times fact."),
        "facts": [
            {"title": "Fours are doubled twos",
             "latex": "4 \\times 3 = 2 \\times (2 \\times 3) = 12",
             "explanation": "Four groups is two groups counted twice, so double the twos answer."},
            {"title": "One more group",
             "latex": "3 \\times 6 = 3 \\times 5 + 3 = 18",
             "explanation": "Stepping to the next fact adds exactly one group."},
        ],
        "workedExamples": [
            {"id": "g3mu-l4-we1",
             "statement": "Find $4 \\times 3$ by doubling a two times fact.",
             "note": "Halve the four, then double the answer.",
             "solution": ("$2 \\times 3 = 6$. Four groups is two groups counted "
                          "twice, so double it: $6 + 6 = 12$. Therefore "
                          "$4 \\times 3 = 12$ — reached without learning "
                          "anything new."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*3, 6)", "Eq(6 + 6, 12)", "Eq(4*3, 12)"]},
            {"id": "g3mu-l4-we2",
             "statement": "You know $3 \\times 5 = 15$. Find $3 \\times 6$ without counting from the start.",
             "note": "How many more groups do you need?",
             "solution": ("$3 \\times 6$ is one more group of three than "
                          "$3 \\times 5$, so add a single three: $15 + 3 = 18$. "
                          "So $3 \\times 6 = 18$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*5, 15)", "Eq(15 + 3, 18)", "Eq(3*6, 18)"]},
        ],
        "commonMistakes": [
            {"text": "Doubling the wrong number — turning 4 × 3 into 4 × 6 = 24.",
             "correction": "Four groups of three is two groups of three counted twice: double the ANSWER 6, not the group size. 4 × 3 = 12.",
             "authored": True},
            {"text": "Adding one instead of one GROUP when stepping along: 3 × 6 = 15 + 1 = 16.",
             "correction": "The step from 3 × 5 to 3 × 6 adds a whole extra group of three: 15 + 3 = 18.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3mu-l4-t1",
             "statement": "Find $4 \\times 5$ by doubling.",
             "solution": ("$2 \\times 5 = 10$, and doubling gives $10 + 10 = 20$. "
                          "So $4 \\times 5 = 20$."),
             "check": ["Eq(2*5, 10)", "Eq(10 + 10, 20)", "Eq(4*5, 20)"]},
            {"id": "g3mu-l4-t2",
             "statement": "You know $4 \\times 6 = 24$. Find $4 \\times 7$.",
             "solution": ("One more group of four: $24 + 4 = 28$, so "
                          "$4 \\times 7 = 28$."),
             "check": ["Eq(4*6, 24)", "Eq(24 + 4, 28)", "Eq(4*7, 28)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Threes are a step count with names", [
                "The line below counts in threes: $0, 3, 6, 9, 12, 15$. Nothing here is new — it is step counting from the first topic.",
                "Giving the stops their names turns the count into a table: $3 \\times 1 = 3$, $3 \\times 2 = 6$, $3 \\times 4 = 12$, and so on.",
                "And once you know one stop, the next is one group away: $3 \\times 5 = 15$, so $3 \\times 6 = 15 + 3 = 18$. Never restart a count you have already begun.",
            ]), fig_threes),
            workedset("Threes by counting on",
                      "Start from a fact you own; add one group.", [
                wex("Find $3 \\times 4$.",
                    ["Count in threes: $3, 6, 9, 12$.",
                     "The fourth stop is $12$, so $3 \\times 4 = 12$."],
                    "$12$",
                    ["Eq(3 + 3 + 3 + 3, 12)", "Eq(3*4, 12)"]),
                wex("You know $3 \\times 5 = 15$. Find $3 \\times 6$.",
                    ["One more group of three is needed.",
                     "$15 + 3 = 18$, so $3 \\times 6 = 18$."],
                    "$18$",
                    ["Eq(3*5, 15)", "Eq(15 + 3, 18)", "Eq(3*6, 18)"]),
            ]),
            tryitset("Threes", "One more group, not one more.", [
                tp("$3 \\times 7$ is:",
                   ["$21$", "$10$", "$18$"],
                   "Count on from $3 \\times 6 = 18$: one more three gives $21$. Adding the numbers gives $10$, and $18$ stops one group short.",
                   ["Eq(3*6, 18)", "Eq(18 + 3, 21)", "Eq(3*7, 21)"]),
                tp("If $3 \\times 8 = 24$, then $3 \\times 9$ is:",
                   ["$27$", "$25$", "$32$"],
                   "One extra group of three: $24 + 3 = 27$. Adding one gives $25$, which forgets that a step is a whole group.",
                   ["Eq(3*8, 24)", "Eq(24 + 3, 27)", "Eq(3*9, 27)"]),
                tp("Which number is NOT in the three times table?",
                   ["$14$", "$12$", "$15$"],
                   "Counting in threes goes $12, 15, 18$ — it steps straight over $14$. Indeed $14$ leaves a remainder of $2$ when shared into threes.",
                   ["Eq(3*4, 12)", "Eq(3*5, 15)", "Eq(Mod(14, 3), 2)"]),
            ]),
            tapq("How big is one step?", "Going from $3 \\times 5$ to $3 \\times 6$, how much does the answer grow?",
                 ["by $3$", "by $1$", "by $6$", "by $5$"],
                 "One more GROUP of three is added, so the answer grows by $3$: $15 + 3 = 18$. Growing by $1$ would give $16$, which is not in the table at all.",
                 ["Eq(3*5, 15)", "Eq(3*6, 18)", "Eq(18 - 15, 3)"]),
            funfact("The three times table hides a trick",
                    "Add up the digits of any answer in the three times table and the total is itself in the three times table: $12 \\to 1 + 2 = 3$, $18 \\to 1 + 8 = 9$, $27 \\to 2 + 7 = 9$. It works for every multiple of three, however large, and it is the fastest way anyone has found to test whether a big number can be shared into threes."),
            withfig(teach("Concept B", "Fours are doubled twos", [
                "The picture below shows $2 \\times 3 = 6$ beside its double, $4 \\times 3 = 12$.",
                "That is the whole four times table: four groups is two groups counted twice, so work out the two times fact and double it. $2 \\times 5 = 10$, so $4 \\times 5 = 20$.",
                "Take care WHAT you double. It is the answer that doubles, not the group size — doubling the $3$ instead would give $4 \\times 6$, a different fact entirely.",
            ]), fig_double),
            workedset("Fours by doubling", "Do the twos fact, then double it.", [
                wex("Find $4 \\times 3$.",
                    ["$2 \\times 3 = 6$.",
                     "Double the answer: $6 + 6 = 12$.",
                     "$4 \\times 3 = 12$."],
                    "$12$",
                    ["Eq(2*3, 6)", "Eq(6 + 6, 12)", "Eq(4*3, 12)"]),
                wex("Find $4 \\times 6$.",
                    ["$2 \\times 6 = 12$.",
                     "Double it: $12 + 12 = 24$.",
                     "$4 \\times 6 = 24$."],
                    "$24$",
                    ["Eq(2*6, 12)", "Eq(12 + 12, 24)", "Eq(4*6, 24)"]),
            ]),
            tryitset("Fours", "Halve the four, do the twos, double back.", [
                tp("$4 \\times 7$ is:",
                   ["$28$", "$14$", "$11$"],
                   "$2 \\times 7 = 14$, and doubling gives $28$. Stopping at $14$ answers the twos fact, and $11$ adds instead of multiplying.",
                   ["Eq(2*7, 14)", "Eq(14 + 14, 28)", "Eq(4*7, 28)"]),
                withfig(tp("The array shows $4$ rows of $6$. $4 \\times 6$ is:",
                   ["$24$", "$12$", "$46$"],
                   "$2 \\times 6 = 12$, doubled to $24$ — and the array shows four rows of six holding exactly that many.",
                   ["Eq(2*6, 12)", "Eq(4*6, 24)", "Eq(12 + 12, 24)"]), fig_4x6),
                tp("Bat works out $4 \\times 3$ by doubling the $3$ and gets $4 \\times 6 = 24$. His mistake was:",
                   ["he doubled the group size instead of the answer",
                    "he should have tripled instead",
                    "nothing — $24$ is correct"],
                   "Doubling must happen to the ANSWER: $2 \\times 3 = 6$, then $6 + 6 = 12$. Doubling the group size answers a different question, and $24$ is twice too big.",
                   ["Eq(2*3, 6)", "Eq(4*3, 12)", "Eq(4*6, 24)",
                    "Eq(24 - 12, 12)"]),
            ]),
            tapq("What gets doubled?", "To find $4 \\times 5$ from the twos table, you should:",
                 ["work out $2 \\times 5 = 10$ and double the $10$",
                  "work out $2 \\times 5 = 10$ and double the $5$",
                  "double the $4$ to get $8 \\times 5$",
                  "add $2 \\times 5$ and $4$"],
                 "Four groups is two groups counted twice, so the ANSWER doubles: $10 + 10 = 20$, giving $4 \\times 5 = 20$. Doubling the group size would give $2 \\times 10$, and doubling the $4$ changes the question altogether.",
                 ["Eq(2*5, 10)", "Eq(10 + 10, 20)", "Eq(4*5, 20)"]),
            recap([
                "The three times table is the step count $3, 6, 9, 12, 15$ with names attached.",
                "Stepping from one fact to the next adds one whole GROUP, not one.",
                "Every four times fact is a two times fact doubled: $2 \\times 6 = 12$, so $4 \\times 6 = 24$.",
                "Double the answer, never the group size.",
            ]),
            tip("When a fact will not come to mind, do not freeze — reach for the nearest fact you DO know and step to it. One group forward, one group back, or a double: every fact in these tables is one small move from a fact you own."),
            tryitset("Chapter practice", "Build it from something you know.", [
                tp("$3 \\times 3$ is:",
                   ["$9$", "$6$", "$33$"],
                   "Three groups of three: $3 + 3 + 3 = 9$. It is also one group on from $3 \\times 2 = 6$.",
                   ["Eq(3 + 3 + 3, 9)", "Eq(3*3, 9)", "Eq(3*2, 6)"]),
                tp("$4 \\times 8$ is:",
                   ["$32$", "$16$", "$12$"],
                   "$2 \\times 8 = 16$, doubled to $32$. Stopping at $16$ answers only the twos fact, and $12$ adds the numbers instead.",
                   ["Eq(2*8, 16)", "Eq(16 + 16, 32)", "Eq(4*8, 32)"]),
                tp("If $4 \\times 9 = 36$, then $4 \\times 10$ is:",
                   ["$40$", "$37$", "$45$"],
                   "One more group of four: $36 + 4 = 40$ — which the ten times table confirms straight away.",
                   ["Eq(4*9, 36)", "Eq(36 + 4, 40)", "Eq(4*10, 40)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"The Tables of 3 and 4\"",
                    "Five tables now, and almost none of them were memorised from cold — they were built from step counts, doubles and single steps sideways. That is how the rest of the tables arrive next year too.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Times One, Times Zero, and Stories
# ==========================================================================

def lesson_one_zero_stories():
    fig_ones = fig_groups((1, "box 1", C_ACCENT), (1, "box 2", C_ACCENT),
                          (1, "box 3", C_ACCENT), (1, "box 4", C_ACCENT))
    fig_zero = fig_groups((0, "box 1: empty", C_WARM),
                          (0, "box 2: empty", C_WARM),
                          (0, "box 3: empty", C_WARM))
    fig_story = equal_groups(5, 4, "bag", C_GREEN)
    return {
        "slug": "times-one-times-zero-and-stories",
        "title": "Times One, Times Zero & Stories",
        "concreteComparison": (
            "Four boxes with one stone in each hold $4$ stones. Three "
            "boxes with nothing in them hold nothing at all. These two "
            "facts look almost too obvious to write down — and they are "
            "exactly the two that get muddled most often."),
        "objective": (
            "Use the times one and times zero rules correctly, and turn a "
            "word story into a times fact when — and only when — its "
            "groups are equal."),
        "concept": [
            "**Times one changes nothing.** $4 \\times 1 = 4$: four boxes "
            "with one stone each hold four stones. And $1 \\times 4 = 4$: "
            "one box with four stones in it. Either way the answer is the "
            "other number, untouched.",
            "**Times zero gives nothing.** $3 \\times 0 = 0$: three empty "
            "boxes hold nothing. And $0 \\times 5 = 0$: no boxes at all, "
            "so nothing to count. Whichever number is the zero, the "
            "answer is zero.",
            "**A story is a times story only when its groups are equal.** "
            "\"Five bags with $4$ apples in each\" is $5 \\times 4 = 20$. "
            "\"Five apples and four more\" is $5 + 4 = 9$ — no groups at "
            "all. Read the story and ask: are there equal groups, and how "
            "many are in one?",
        ],
        "keyIdea": (
            "Multiplying by one leaves a number alone and multiplying by "
            "zero destroys it — and a word problem is a times problem "
            "only if it really has equal groups."),
        "facts": [
            {"title": "Times one",
             "latex": "4 \\times 1 = 4",
             "explanation": "Four groups of one, or one group of four — either way, four."},
            {"title": "Times zero",
             "latex": "3 \\times 0 = 0",
             "explanation": "Three empty groups hold nothing at all."},
        ],
        "workedExamples": [
            {"id": "g3mu-l5-we1",
             "statement": "Work out $4 \\times 1$ and $1 \\times 4$, and say why they agree.",
             "note": "Draw both pictures.",
             "solution": ("$4 \\times 1$ is four boxes with one stone in each: "
                          "$1 + 1 + 1 + 1 = 4$. $1 \\times 4$ is one box with "
                          "four stones: $4$. The pictures look quite different, "
                          "but the turnaround guarantees the same total — and "
                          "both equal $4$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1 + 1 + 1 + 1, 4)", "Eq(4*1, 4)", "Eq(1*4, 4)"]},
            {"id": "g3mu-l5-we2",
             "statement": "A shop packs $5$ bags with $4$ apples in each. How many apples? Would $5 + 4$ answer it?",
             "note": "Are the groups equal?",
             "solution": ("Five equal groups of four: $4 + 4 + 4 + 4 + 4 = 20$, "
                          "so $5 \\times 4 = 20$ apples. $5 + 4 = 9$ would be "
                          "the answer to a different story — five apples and "
                          "four more — which has no groups in it at all."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4 + 4 + 4 + 4 + 4, 20)", "Eq(5*4, 20)",
                       "Eq(5 + 4, 9)", "Ne(20, 9)"]},
        ],
        "commonMistakes": [
            {"text": "Answering 3 × 0 with 3, on the grounds that \"there are still three boxes\".",
             "correction": "The boxes are counted, but what is IN them is what multiplication totals: three empty boxes hold 0 stones. 3 × 0 = 0.",
             "authored": True},
            {"text": "Multiplying whenever two numbers appear — turning \"5 apples and 4 more\" into 5 × 4 = 20.",
             "correction": "That story has no equal groups; it just joins two amounts, so 5 + 4 = 9. Multiplication needs groups, not merely two numbers.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3mu-l5-t1",
             "statement": "Work out $7 \\times 1$ and $0 \\times 7$.",
             "solution": ("$7 \\times 1 = 7$ — seven groups of one leaves seven "
                          "untouched. $0 \\times 7 = 0$ — no groups at all, so "
                          "there is nothing to count."),
             "check": ["Eq(7*1, 7)", "Eq(0*7, 0)"]},
            {"id": "g3mu-l5-t2",
             "statement": "A herder ties $3$ horses at each of $4$ posts. Write the times fact, then say what $3 + 4$ would have answered.",
             "solution": ("Four equal groups of three: $4 \\times 3 = 12$ horses. "
                          "$3 + 4 = 7$ would answer \"three horses and four more "
                          "horses\" — a story with no posts in it."),
             "check": ["Eq(4*3, 12)", "Eq(3 + 4, 7)", "Ne(12, 7)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The two quiet rules", [
                "Four boxes, one stone in each — the picture below. Counting gives $1 + 1 + 1 + 1 = 4$, so $4 \\times 1 = 4$.",
                "Multiplying by one leaves a number exactly as it was. It has to: taking one group of something IS that something.",
                "The turnaround says $1 \\times 4 = 4$ as well — one box with four stones in it. Different picture, same total.",
            ]), fig_ones),
            workedset("Times one", "One group of it, or groups of one.", [
                wex("Work out $4 \\times 1$.",
                    ["Four boxes with one stone each.",
                     "$1 + 1 + 1 + 1 = 4$, so $4 \\times 1 = 4$."],
                    "$4$",
                    ["Eq(1 + 1 + 1 + 1, 4)", "Eq(4*1, 4)"]),
                wex("Work out $1 \\times 9$.",
                    ["One group with nine in it.",
                     "There is nothing to repeat, so the answer is $9$."],
                    "$9$",
                    ["Eq(1*9, 9)", "Eq(9*1, 9)"]),
            ]),
            tryitset("Times one", "The other number comes through unchanged.", [
                tp("$6 \\times 1$ is:",
                   ["$6$", "$1$", "$7$"],
                   "Six groups of one: $6$. Answering $1$ counts one group's contents, and $7$ adds the numbers instead.",
                   ["Eq(6*1, 6)", "Eq(6 + 1, 7)"]),
                tp("$1 \\times 8$ is:",
                   ["$8$", "$1$", "$18$"],
                   "One group with eight in it is just eight. The turnaround agrees: $8 \\times 1 = 8$.",
                   ["Eq(1*8, 8)", "Eq(8*1, 8)"]),
                tp("Which fact leaves the number unchanged?",
                   ["$5 \\times 1$", "$5 \\times 0$", "$5 \\times 2$"],
                   "$5 \\times 1 = 5$ — untouched. $5 \\times 0 = 0$ destroys it, and $5 \\times 2 = 10$ doubles it.",
                   ["Eq(5*1, 5)", "Eq(5*0, 0)", "Eq(5*2, 10)"]),
            ]),
            tapq("One group of nine", "What is $1 \\times 9$?",
                 ["$9$", "$1$", "$10$", "$0$"],
                 "One group with nine things in it holds nine things — there is nothing to repeat. Answering $1$ counts the groups rather than their contents.",
                 ["Eq(1*9, 9)", "Eq(9*1, 9)"]),
            funfact("Zero had to be argued for",
                    "For centuries, mathematicians disagreed about whether zero was a number at all — how can nothing be something you count with? The argument was settled by usefulness: without zero there is no way to write $305$, and no way to say what three empty boxes hold. The rule $3 \\times 0 = 0$ is what makes the whole system hold together."),
            withfig(teach("Concept B", "Times zero, and reading a story", [
                "Three boxes, all empty — drawn below. How many stones? None: $3 \\times 0 = 0$.",
                "It works the other way too. $0 \\times 5$ means no groups at all, so again there is nothing to count: $0$. Whichever number is zero, the answer is zero.",
                "Now the real skill. A story is a TIMES story only when it has equal groups: \"five bags with four apples in each\" gives $5 \\times 4 = 20$. \"Five apples and four more\" gives $5 + 4 = 9$ — two numbers, but no groups.",
            ]), fig_zero),
            workedset("Zero, and stories", "Ask: are there equal groups?", [
                wex("Work out $3 \\times 0$ and $0 \\times 6$.",
                    ["Three empty boxes hold nothing: $3 \\times 0 = 0$.",
                     "No boxes at all also holds nothing: $0 \\times 6 = 0$."],
                    "both $0$",
                    ["Eq(3*0, 0)", "Eq(0*6, 0)"]),
                wex("Five bags with $4$ apples in each. How many apples?",
                    ["Equal groups — this is a times story.",
                     "$4 + 4 + 4 + 4 + 4 = 20$, so $5 \\times 4 = 20$ apples.",
                     "$5 + 4 = 9$ would answer a story with no bags in it."],
                    "$20$ apples",
                    ["Eq(5*4, 20)", "Eq(4 + 4 + 4 + 4 + 4, 20)",
                     "Eq(5 + 4, 9)"]),
            ]),
            tryitset("Zero, and times stories", "Groups or no groups?", [
                tp("$5 \\times 0$ is:",
                   ["$0$", "$5$", "$50$"],
                   "Five empty groups hold nothing at all. Answering $5$ counts the groups instead of their contents.",
                   ["Eq(5*0, 0)", "Eq(0*5, 0)"]),
                withfig(tp("The picture shows $5$ bags with $4$ apples in each. The total is:",
                   ["$20$ apples", "$9$ apples", "$54$ apples"],
                   "Five equal groups of four: $5 \\times 4 = 20$. Adding gives $9$, which would answer \"five apples and four more\".",
                   ["Eq(5*4, 20)", "Eq(5 + 4, 9)"]), fig_story),
                tp("Which story is NOT a times story?",
                   ["Bat has $6$ stones and finds $3$ more",
                    "Bat has $6$ bags with $3$ stones in each",
                    "Bat fills $3$ boxes with $6$ stones each"],
                   "The first simply joins two amounts — $6 + 3 = 9$, with no groups anywhere. The other two have equal groups and give $18$.",
                   ["Eq(6 + 3, 9)", "Eq(6*3, 18)", "Eq(3*6, 18)"]),
            ]),
            tapq("Empty groups", "Three boxes stand on a shelf, all empty. How many stones altogether?",
                 ["$0$", "$3$", "$1$", "you cannot tell"],
                 "Multiplication counts what is INSIDE the groups, and each of these holds nothing: $3 \\times 0 = 0$. The three counts boxes, not stones.",
                 ["Eq(3*0, 0)", "Eq(0 + 0 + 0, 0)"]),
            recap([
                "$n \\times 1 = n$ — one group of something is that something.",
                "$n \\times 0 = 0$ — empty groups, or no groups at all, hold nothing.",
                "A story is a times story only if it has EQUAL groups; two numbers alone are not enough.",
                "Ask \"how many groups, and how many in one?\" before choosing an operation.",
            ]),
            tip("Before multiplying in a word problem, say the sentence \"there are ___ groups with ___ in each\". If you cannot fill both blanks from the story, it is not a times problem."),
            tryitset("Chapter practice", "One leaves it, zero empties it, groups make it.", [
                tp("$9 \\times 0$ is:",
                   ["$0$", "$9$", "$90$"],
                   "Nine empty groups hold nothing: $0$. The nine counts groups, and there is nothing inside any of them.",
                   ["Eq(9*0, 0)", "Eq(0*9, 0)"]),
                tp("$1 \\times 1$ is:",
                   ["$1$", "$2$", "$0$"],
                   "One group with one thing in it: $1$. Adding would give $2$, which is the commonest slip on this smallest of facts.",
                   ["Eq(1*1, 1)", "Eq(1 + 1, 2)"]),
                tp("A herder ties $3$ horses at each of $4$ posts. The number of horses is:",
                   ["$12$", "$7$", "$34$"],
                   "Four equal groups of three: $4 \\times 3 = 12$ horses. Adding gives $7$, which answers a story with no posts in it.",
                   ["Eq(4*3, 12)", "Eq(3 + 4, 7)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Times One, Times Zero & Stories\" — and the topic",
                    "Equal groups, arrays and the turnaround, the friendly tables, the threes and fours, and the two quiet rules. One idea carried all of it: multiplication counts equal groups. Next comes division, which takes those same groups apart again.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr3 = array(3, 6, C_ACCENT)
    return [
        prob("g3mu-pr1", "A camp pitches $4$ gers with $5$ beds in each. Write the repeated addition and the times fact.",
             "Four groups of five: $5 + 5 + 5 + 5 = 20$, so $4 \\times 5 = 20$ beds.",
             ["Eq(5 + 5 + 5 + 5, 20)", "Eq(4*5, 20)"]),
        prob("g3mu-pr2", "Find $2 \\times 8$ and $5 \\times 8$. What must each answer end in, and why?",
             "$2 \\times 8 = 16$: doubling always gives an even answer. $5 \\times 8 = 40$: eight is an even count of fives, so they pair into four whole tens and the answer ends in $0$.",
             ["Eq(2*8, 16)", "Eq(Mod(16, 2), 0)", "Eq(5*8, 40)",
              "Eq(Mod(40, 10), 0)"]),
        withprobfig(prob("g3mu-pr3", "The array shows $3$ rows of $6$. Write both times facts it proves and the total.",
             "Rows: $3 \\times 6 = 18$. Columns: $6 \\times 3 = 18$. One rectangle, two readings, one count of $18$.",
             ["Eq(3*6, 18)", "Eq(6*3, 18)"]), fig_pr3),
        prob("g3mu-pr4", "Build $4 \\times 7$ from the two times table, showing every step.",
             "$2 \\times 7 = 14$. Four groups is two groups counted twice, so double the answer: $14 + 14 = 28$. Therefore $4 \\times 7 = 28$.",
             ["Eq(2*7, 14)", "Eq(14 + 14, 28)", "Eq(4*7, 28)"]),
        prob("g3mu-pr5", "You know $3 \\times 6 = 18$. Find $3 \\times 7$ and $3 \\times 5$ without recounting from zero.",
             "One group forward: $18 + 3 = 21$, so $3 \\times 7 = 21$. One group back: $18 - 3 = 15$, so $3 \\times 5 = 15$. A known fact reaches both of its neighbours.",
             ["Eq(3*6, 18)", "Eq(18 + 3, 21)", "Eq(3*7, 21)",
              "Eq(18 - 3, 15)", "Eq(3*5, 15)"]),
        prob("g3mu-pr6", "Work out $6 \\times 1$ and $6 \\times 0$, and explain the difference in one sentence.",
             "$6 \\times 1 = 6$ and $6 \\times 0 = 0$. Six groups of one hold one thing each, so six altogether; six groups of nothing hold nothing at all.",
             ["Eq(6*1, 6)", "Eq(6*0, 0)"]),
        prob("g3mu-pr7", "A picture shows groups of $5$, $5$ and $3$. Explain why no single times fact counts it, and give the true total.",
             "The groups are not all the same size, and the times sign promises they are. The total is $5 + 5 + 3 = 13$, whereas three equal groups of five would be $3 \\times 5 = 15$ — two too many.",
             ["Eq(5 + 5 + 3, 13)", "Eq(3*5, 15)", "Eq(15 - 13, 2)"]),
        prob("g3mu-pr8", "Saruul knows only the tables of $2$, $5$ and $10$. Show how she can still answer $4 \\times 5$ AND $5 \\times 4$.",
             "$5 \\times 4$ is in her five times table: four fives pair into two whole tens, giving $20$. The turnaround then hands her $4 \\times 5 = 20$ free — the same array read the other way.",
             ["Eq(5*4, 20)", "Eq(4*5, 20)", "Eq(Mod(20, 10), 0)"]),
    ]


def test_bank():
    return [
        prob("g3mu-x1", "Write $4 \\times 3$ as repeated addition and find it. Then explain why groups of $3$, $3$ and $4$ have NO single times fact.",
             "$4 \\times 3 = 3 + 3 + 3 + 3 = 12$. The unequal groups total $3 + 3 + 4 = 10$, while three equal groups of three make only $3 \\times 3 = 9$ — so no times fact fits, and you must add.",
             ["Eq(4*3, 12)", "Eq(3 + 3 + 4, 10)", "Eq(3*3, 9)", "Ne(10, 9)"]),
        prob("g3mu-x2", "Find $2 \\times 9$, $5 \\times 9$ and $10 \\times 9$, giving each answer's ending check.",
             "$2 \\times 9 = 18$: a double, so even. $5 \\times 9 = 45$: nine is an odd count of fives, so one five is left unpaired and the answer ends in $5$. $10 \\times 9 = 90$: nine whole bundles of ten, ending in $0$.",
             ["Eq(2*9, 18)", "Eq(Mod(18, 2), 0)", "Eq(5*9, 45)",
              "Eq(Mod(45, 10), 5)", "Eq(10*9, 90)"]),
        prob("g3mu-x3", "Build $4 \\times 8$ from $2 \\times 8$, and $3 \\times 8$ from $3 \\times 7$.",
             "$2 \\times 8 = 16$, and four groups is two groups twice: $16 + 16 = 32$, so $4 \\times 8 = 32$. And $3 \\times 7 = 21$, so one more group of three gives $21 + 3 = 24 = 3 \\times 8$.",
             ["Eq(2*8, 16)", "Eq(16 + 16, 32)", "Eq(4*8, 32)",
              "Eq(3*7, 21)", "Eq(21 + 3, 24)", "Eq(3*8, 24)"]),
        prob("g3mu-x4", "An array has $5$ rows of $3$ stones. Write both times facts, and say why they must agree.",
             "Rows: $5 \\times 3 = 15$. Columns: $3 \\times 5 = 15$. They must agree because both readings count the SAME stones — tilting your head cannot change how many there are.",
             ["Eq(5*3, 15)", "Eq(3*5, 15)"]),
        prob("g3mu-x5", "Work out $8 \\times 1$, $8 \\times 0$ and $0 \\times 8$, and say what each picture looks like.",
             "$8 \\times 1 = 8$: eight boxes with one stone each. $8 \\times 0 = 0$: eight empty boxes. $0 \\times 8 = 0$: no boxes at all. Multiplying by one leaves the number alone; multiplying by zero empties it, whichever side the zero is on.",
             ["Eq(8*1, 8)", "Eq(8*0, 0)", "Eq(0*8, 0)"]),
        prob("g3mu-x6", "A shop has $4$ shelves with $6$ jars on each. Bat answers $10$ jars. Explain his mistake and give the right answer.",
             "Bat added the two numbers: $4 + 6 = 10$. But the story has equal GROUPS — four groups of six — so it is a times story: $6 + 6 + 6 + 6 = 24$, giving $4 \\times 6 = 24$ jars. His answer is $14$ short.",
             ["Eq(4 + 6, 10)", "Eq(4*6, 24)", "Eq(24 - 10, 14)"]),
    ]


def main():
    topic = {
        "slug": "multiplication-first-facts",
        "title": "Multiplication — First Facts",
        "grade": 3,
        "status": "published",
        "blurb": ("Equal groups and repeated addition, arrays and the "
                  "turnaround, the friendly tables of 2, 5 and 10 with their "
                  "ending patterns, the threes and fours built by doubling, "
                  "and the quiet rules for times one and times zero."),
        "lessons": [
            lesson_equal_groups(),
            lesson_arrays(),
            lesson_friendly_tables(),
            lesson_threes_fours(),
            lesson_one_zero_stories(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "multiplication-first-facts.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
