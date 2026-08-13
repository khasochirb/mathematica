#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Division — Sharing & Grouping.

The two faces of division — sharing a pile between a known number of
people, and grouping a pile into bundles of a known size; division facts
read straight out of the times tables you already own; dividing by 3 and
4; and choosing between multiplication and division from the words of a
story.

Through-line: DIVISION UNDOES MULTIPLICATION. Sharing and grouping ask
different questions but the same fact answers both, every division has a
multiplication receipt, and a story tells you which of the three numbers
is missing.

Grade discipline: EXACT division only — every share comes out even, with
nothing left over. (Remainders are Grade 4's, and introducing them here
would blur the receipt that makes division checkable.) Divisors are 2, 3,
4, 5 and 10; nothing exceeds 1000; no negatives, no decimals, no
fractions of an object. Every check is sympy-asserted BEFORE the JSON is
written.

Run: python3 scripts/grade2/build_division_sharing_and_grouping.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, withprobfig, workedset,
                     write_topic, fig_groups, C_ACCENT, C_WARM, C_GREEN)


def shares(n_people, each, who="child"):
    """The result of SHARING: one labelled group per person, `each` in it.
    Built from the same two numbers as the division fact, so the picture
    and the fact cannot disagree."""
    assert 1 <= n_people <= 8 and 0 <= each <= 12, "shares: out of range"
    return fig_groups(*[(each, "%s %d" % (who, i + 1), C_ACCENT)
                        for i in range(n_people)])


def bundles_of(n_groups, size, noun="bag"):
    """The result of GROUPING: `n_groups` bundles, each holding `size`."""
    assert 1 <= n_groups <= 8 and 1 <= size <= 12, "bundles_of: out of range"
    return fig_groups(*[(size, "%s %d" % (noun, i + 1), C_GREEN)
                        for i in range(n_groups)])


# ==========================================================================
# Lesson 1 — Sharing Equally
# ==========================================================================

def lesson_sharing():
    total, people = 12, 3
    each = total // people
    fig_share = shares(people, each)
    fig_unfair = fig_groups((5, "child 1", C_WARM), (4, "child 2", C_WARM),
                            (3, "child 3", C_WARM))
    fig_share20 = shares(4, 5)
    return {
        "slug": "sharing-equally",
        "title": "Sharing Equally",
        "concreteComparison": (
            "Twelve buuz on a plate and three children round it. Handing "
            "them out one at a time — one for you, one for you, one for "
            "you — until the plate is empty gives each child $4$. That is "
            "division: $12 \\div 3 = 4$."),
        "objective": (
            "Share a total equally between a known number of people, "
            "write the division fact, and check it with a multiplication "
            "receipt."),
        "concept": [
            "**Sharing splits a total into equal parts.** $12$ buuz "
            "shared between $3$ children gives $4$ each: $12 \\div 3 = "
            "4$. The first number is what you started with, the second is "
            "how many are sharing, and the answer is how many EACH one "
            "gets.",
            "**Equal is the whole point.** Giving out $5$, $4$ and $3$ "
            "also empties the plate, but nobody would call it sharing. "
            "Division always means equal parts — if the parts differ, no "
            "division fact describes it.",
            "**Every division has a multiplication receipt.** If each of "
            "$3$ children got $4$, then $3 \\times 4 = 12$ must bring the "
            "buuz back. That receipt is how you check a division without "
            "dividing again.",
        ],
        "keyIdea": (
            "Sharing asks \"how many each?\" — and the answer is right "
            "only if multiplying it back by the number of sharers returns "
            "the total you started with."),
        "facts": [
            {"title": "Sharing",
             "latex": "12 \\div 3 = 4",
             "explanation": "Twelve shared between three gives four each."},
            {"title": "The receipt",
             "latex": "3 \\times 4 = 12",
             "explanation": "Three children with four each brings the twelve back — the check."},
        ],
        "workedExamples": [
            {"id": "g3dv-l1-we1",
             "statement": "Share $%d$ buuz equally between $%d$ children. How many each?" % (total, people),
             "note": "Hand them out one round at a time.",
             "solution": ("Deal them out: after each round every child has one "
                          "more, and the plate empties after four rounds. So "
                          "each child has $4$: $12 \\div 3 = 4$. Receipt: "
                          "$3 \\times 4 = 12$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*4, 12)", "Eq(Rational(12, 3), 4)"]},
            {"id": "g3dv-l1-we2",
             "statement": "Share $20$ sweets equally between $4$ children.",
             "note": "Ask which times fact reaches $20$.",
             "solution": ("You need the number that four children can each hold "
                          "to make $20$: $4 \\times 5 = 20$, so each child gets "
                          "$5$. That is $20 \\div 4 = 5$, and the receipt "
                          "$4 \\times 5 = 20$ ✓ confirms it."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*5, 20)", "Eq(Rational(20, 4), 5)"]},
        ],
        "commonMistakes": [
            {"text": "Answering with the number of sharers instead of the share — saying 12 ÷ 3 = 3.",
             "correction": "The 3 is who is sharing; the answer is what each one GETS. Twelve between three is 4 each, and the receipt 3 × 4 = 12 proves it while 3 × 3 = 9 does not.",
             "authored": True},
            {"text": "Calling an uneven split a division — sharing 12 as 5, 4 and 3.",
             "correction": "That empties the plate but the parts are not equal, so it is not sharing. Division always makes every part the same size: 4, 4 and 4.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3dv-l1-t1",
             "statement": "Share $10$ apples equally between $2$ children, and give the receipt.",
             "solution": ("$2 \\times 5 = 10$, so each child gets $5$: "
                          "$10 \\div 2 = 5$. Receipt: $2 \\times 5 = 10$ ✓."),
             "check": ["Eq(2*5, 10)", "Eq(Rational(10, 2), 5)"]},
            {"id": "g3dv-l1-t2",
             "statement": "Share $15$ stones equally between $5$ children.",
             "solution": ("$5 \\times 3 = 15$, so each gets $3$: "
                          "$15 \\div 5 = 3$. Receipt: $5 \\times 3 = 15$ ✓."),
             "check": ["Eq(5*3, 15)", "Eq(Rational(15, 5), 3)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One for you, one for you", [
                "Twelve buuz, three children. Hand them round one at a time until the plate is empty — the picture below shows how they land.",
                "Each child ends up with $4$, and that is what division records: $12 \\div 3 = 4$. The first number is the pile, the second is how many are sharing, and the answer is what EACH one gets.",
                "Notice what the answer is not. It is not the number of children — they were given to you. Division tells you the size of one share.",
            ]), fig_share),
            workedset("Share it out", "Deal in rounds until the pile is gone.", [
                wex("Share $12$ buuz between $3$ children.",
                    ["Deal one round at a time; the plate empties after four rounds.",
                     "Each child has $4$: $12 \\div 3 = 4$.",
                     "Receipt: $3 \\times 4 = 12$ ✓."],
                    "$4$ each",
                    ["Eq(3*4, 12)", "Eq(Rational(12, 3), 4)"]),
                wex("Share $20$ sweets between $4$ children.",
                    ["Which times fact reaches $20$ with four groups?",
                     "$4 \\times 5 = 20$, so each child gets $5$.",
                     "$20 \\div 4 = 5$; receipt $4 \\times 5 = 20$ ✓."],
                    "$5$ each",
                    ["Eq(4*5, 20)", "Eq(Rational(20, 4), 5)"]),
            ]),
            tryitset("How many each?", "The answer is the size of one share.", [
                withfig(tp("The picture shows $20$ sweets shared between $4$ children. Each child gets:",
                   ["$5$", "$4$", "$16$"],
                   "$4 \\times 5 = 20$, so each share is $5$. Answering $4$ gives the number of children back, and $16$ subtracts instead of sharing.",
                   ["Eq(4*5, 20)", "Eq(Rational(20, 4), 5)",
                    "Eq(20 - 4, 16)"]), fig_share20),
                tp("$18$ stones shared between $3$ children gives each:",
                   ["$6$", "$3$", "$15$"],
                   "$3 \\times 6 = 18$, so each child gets $6$. The receipt confirms it, while $3 \\times 3 = 9$ does not reach $18$.",
                   ["Eq(3*6, 18)", "Eq(Rational(18, 3), 6)", "Eq(3*3, 9)"]),
                tp("$10$ buuz shared between $5$ children gives each:",
                   ["$2$", "$5$", "$50$"],
                   "$5 \\times 2 = 10$, so each gets $2$. Answering $5$ repeats the number of children, and $50$ multiplies instead of sharing.",
                   ["Eq(5*2, 10)", "Eq(Rational(10, 5), 2)", "Eq(5*10, 50)"]),
            ]),
            withfig(tapq("Is this sharing?", "Twelve buuz are given out as $5$, $4$ and $3$. Is that division?",
                 ["no — the parts are not equal",
                  "yes: $12 \\div 3 = 4$",
                  "yes, because the plate is empty",
                  "yes: $12 \\div 5 = 4$"],
                 "The plate does empty — $5 + 4 + 3 = 12$ — but sharing means EQUAL parts, and these differ. Shared properly, each child would get $12 \\div 3 = 4$.",
                 ["Eq(5 + 4 + 3, 12)", "Eq(Rational(12, 3), 4)", "Ne(5, 4)"]),
                 fig_unfair),
            funfact("Why a plate empties evenly or not at all",
                    "Try sharing $13$ buuz between $3$ children and something awkward happens: everyone gets $4$ and one buuz sits there, belonging to nobody. Numbers that share out cleanly are special, and every one of them is hiding in a times table — which is exactly why the next lessons send you back to the tables to find them."),
            withfig(teach("Concept B", "The receipt proves it", [
                "Every division carries a multiplication that undoes it. If $12$ shared between $3$ gives $4$ each, then putting the shares back must return the pile: $3 \\times 4 = 12$.",
                "That is the receipt, and it is how you check a division WITHOUT dividing a second time. Multiplication is the easier operation, so the check is easier than the work.",
                "The picture below shows $4$ children with $5$ each. Reading it as sharing gives $20 \\div 4 = 5$; reading it as a times fact gives $4 \\times 5 = 20$. One picture, both facts.",
            ]), fig_share20),
            workedset("Check with the receipt",
                      "Multiply the share back by the number of sharers.", [
                wex("Is $15 \\div 5 = 3$ correct?",
                    ["Receipt: $5 \\times 3 = 15$.",
                     "It returns the pile we started with, so yes ✓."],
                    "correct",
                    ["Eq(5*3, 15)", "Eq(Rational(15, 5), 3)"]),
                wex("Bat says $16 \\div 4 = 3$. Check it.",
                    ["Receipt: $4 \\times 3 = 12$.",
                     "That is not $16$, so the answer is wrong.",
                     "The true share is $4$, since $4 \\times 4 = 16$."],
                    "wrong — it is $4$",
                    ["Eq(4*3, 12)", "Ne(12, 16)", "Eq(4*4, 16)",
                     "Eq(Rational(16, 4), 4)"]),
            ]),
            tryitset("Receipts", "Multiply back and see whether the pile returns.", [
                tp("Which receipt proves $20 \\div 5 = 4$?",
                   ["$5 \\times 4 = 20$", "$20 \\times 5 = 100$",
                    "$20 - 5 = 15$"],
                   "Putting four back into each of five shares returns the pile: $5 \\times 4 = 20$ ✓. The others do not rebuild the twenty.",
                   ["Eq(5*4, 20)", "Eq(Rational(20, 5), 4)",
                    "Eq(20*5, 100)"]),
                tp("Saruul says $18 \\div 3 = 5$. The receipt says:",
                   ["$3 \\times 5 = 15$, so she is wrong",
                    "$3 \\times 5 = 18$, so she is right",
                    "the receipt cannot check a division"],
                   "$3 \\times 5 = 15$, which is $3$ short of $18$ — so her answer is too small. The true share is $6$, because $3 \\times 6 = 18$.",
                   ["Eq(3*5, 15)", "Eq(18 - 15, 3)", "Eq(3*6, 18)"]),
                tp("$12 \\div 4$ is:",
                   ["$3$", "$4$", "$8$"],
                   "$4 \\times 3 = 12$, so each of four shares holds $3$. Answering $4$ repeats the number of sharers, and $8$ subtracts instead.",
                   ["Eq(4*3, 12)", "Eq(Rational(12, 4), 3)", "Eq(12 - 4, 8)"]),
            ]),
            tapq("What does the answer count?", "In $20 \\div 4 = 5$, what does the $5$ count?",
                 ["how many each sharer gets", "how many sharers there are",
                  "how many are left over", "the total"],
                 "The $20$ is the pile and the $4$ is how many are sharing, so the $5$ is the size of ONE share. The receipt says it plainly: $4$ shares of $5$ rebuild the pile, $4 \\times 5 = 20$.",
                 ["Eq(4*5, 20)", "Eq(Rational(20, 4), 5)"]),
            recap([
                "Sharing splits a total into EQUAL parts and asks how many each.",
                "$12 \\div 3 = 4$: the pile, the number of sharers, the size of one share.",
                "Unequal parts are not division, however neatly the pile empties.",
                "Every division has a multiplication receipt — $3 \\times 4 = 12$ — and it is the check.",
            ]),
            tip("Say the receipt out loud before you write a division answer down: \"three children with four each is twelve\". If the sentence does not come back to the pile you started with, the answer is wrong."),
            tryitset("Chapter practice", "Share, then multiply back.", [
                tp("$16 \\div 2$ is:",
                   ["$8$", "$2$", "$14$"],
                   "$2 \\times 8 = 16$, so each of two shares holds $8$. Answering $14$ subtracts instead of sharing.",
                   ["Eq(2*8, 16)", "Eq(Rational(16, 2), 8)", "Eq(16 - 2, 14)"]),
                tp("$25$ shared between $5$ gives each:",
                   ["$5$", "$20$", "$30$"],
                   "$5 \\times 5 = 25$, so each share is $5$. Here the share and the number of sharers happen to match, which is unusual and worth noticing.",
                   ["Eq(5*5, 25)", "Eq(Rational(25, 5), 5)"]),
                tp("Which division does the receipt $4 \\times 6 = 24$ prove?",
                   ["$24 \\div 4 = 6$", "$24 \\div 6 = 24$",
                    "$4 \\div 24 = 6$"],
                   "Four shares of six rebuild twenty-four, so $24 \\div 4 = 6$. (The same receipt also proves $24 \\div 6 = 4$ — but not the answer $24$.)",
                   ["Eq(4*6, 24)", "Eq(Rational(24, 4), 6)",
                    "Eq(Rational(24, 6), 4)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Sharing Equally\"",
                    "Sharing is only half of division. The next lesson asks a different-looking question — not \"how many each?\" but \"how many groups?\" — and discovers that the very same fact answers both.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Grouping
# ==========================================================================

def lesson_grouping():
    fig_group = bundles_of(4, 3)
    fig_group20 = bundles_of(4, 5)
    fig_both = fig_groups((3, "share: 4 children get 3", C_ACCENT),
                          (4, "group: bags of 3 make 4 bags", C_GREEN))
    return {
        "slug": "grouping",
        "title": "Grouping",
        "concreteComparison": (
            "Twelve buuz again — but now nobody is sharing. They are "
            "being packed into bags of $3$. How many bags? Four. The "
            "question sounds completely different from sharing, and the "
            "answer comes from exactly the same fact: $12 \\div 3 = 4$."),
        "objective": (
            "Group a total into bundles of a known size, write the "
            "division fact, and tell a grouping question apart from a "
            "sharing one."),
        "concept": [
            "**Grouping asks how many bundles fit.** $12$ buuz packed in "
            "bags of $3$ makes $4$ bags: $12 \\div 3 = 4$. The first "
            "number is the pile, the second is the SIZE of each bundle, "
            "and the answer is how many bundles there are.",
            "**Sharing and grouping ask different questions.** Sharing "
            "knows how many parts and wants their size; grouping knows "
            "the size and wants how many parts. \"Between $3$ children\" "
            "is sharing; \"into bags of $3$\" is grouping.",
            "**One fact answers both.** $12 \\div 3 = 4$ serves as \"three "
            "children get four each\" and as \"bags of three make four "
            "bags\". The story differs, the picture differs, the "
            "arithmetic does not — which is why you only ever learn one "
            "set of division facts.",
        ],
        "keyIdea": (
            "Sharing knows the number of parts and finds their size; "
            "grouping knows the size and finds the number of parts — and "
            "the same division fact answers both."),
        "facts": [
            {"title": "Grouping",
             "latex": "12 \\div 3 = 4",
             "explanation": "Twelve packed in bags of three makes four bags."},
            {"title": "Two questions, one fact",
             "latex": "3 \\times 4 = 12",
             "explanation": "The receipt is the same whether the 3 counts children or bag size."},
        ],
        "workedExamples": [
            {"id": "g3dv-l2-we1",
             "statement": "Twelve buuz are packed into bags of $3$. How many bags?",
             "note": "Count how many bundles of three fit.",
             "solution": ("Take three at a time: $3, 6, 9, 12$ — four bundles "
                          "empty the plate. So $12 \\div 3 = 4$ bags, and the "
                          "receipt $4 \\times 3 = 12$ ✓ confirms it."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*3, 12)", "Eq(Rational(12, 3), 4)"]},
            {"id": "g3dv-l2-we2",
             "statement": "Twenty sweets are packed into bags of $5$. How many bags — and how does this differ from sharing $20$ between $5$?",
             "note": "Same fact, different question.",
             "solution": ("Bags of five: $20 \\div 5 = 4$ bags. Sharing $20$ "
                          "between $5$ children also uses $20 \\div 5 = 4$, but "
                          "there the $4$ is what each CHILD gets. Same "
                          "arithmetic, different meaning for the answer."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*4, 20)", "Eq(Rational(20, 5), 4)"]},
        ],
        "commonMistakes": [
            {"text": "Reading \"bags of 3\" as \"3 bags\" and answering 12 ÷ 3 as though there were three bundles of four.",
             "correction": "\"Bags of 3\" fixes the SIZE at three, so the question is how many bags — and the answer is 4 bags of 3, not 3 bags of 4. The fact is the same; be sure which number the answer counts.",
             "authored": True},
            {"text": "Thinking sharing and grouping need different division facts.",
             "correction": "They need the same one. 12 ÷ 3 = 4 answers \"three children get four each\" and \"bags of three make four bags\" — only what the 4 MEANS changes.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3dv-l2-t1",
             "statement": "How many bags of $2$ can be filled from $14$ buuz?",
             "solution": ("Count in twos to $14$: seven bundles. So "
                          "$14 \\div 2 = 7$ bags, receipt $7 \\times 2 = 14$ ✓."),
             "check": ["Eq(7*2, 14)", "Eq(Rational(14, 2), 7)"]},
            {"id": "g3dv-l2-t2",
             "statement": "Is \"$18$ pencils into boxes of $6$\" sharing or grouping? Answer it.",
             "solution": ("It is grouping — the box SIZE is given and the number "
                          "of boxes is wanted. $18 \\div 6 = 3$ boxes, receipt "
                          "$3 \\times 6 = 18$ ✓."),
             "check": ["Eq(3*6, 18)", "Eq(Rational(18, 6), 3)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "How many bundles fit?", [
                "The same twelve buuz, but now they are being packed into bags of $3$ — the picture below shows the bags that result.",
                "Count them: four bags. Or count up in threes — $3, 6, 9, 12$ — and the number of steps is the number of bags.",
                "The division is $12 \\div 3 = 4$. Here the $3$ is the SIZE of a bag and the $4$ counts the bags, which is the reverse of what those numbers meant when you were sharing.",
            ]), fig_group),
            workedset("Count the bundles", "Step up by the bundle size.", [
                wex("How many bags of $3$ fill from $12$ buuz?",
                    ["Count in threes: $3, 6, 9, 12$ — four steps.",
                     "$12 \\div 3 = 4$ bags.",
                     "Receipt: $4 \\times 3 = 12$ ✓."],
                    "$4$ bags",
                    ["Eq(4*3, 12)", "Eq(Rational(12, 3), 4)"]),
                wex("How many bags of $5$ fill from $20$ sweets?",
                    ["Count in fives: $5, 10, 15, 20$ — four steps.",
                     "$20 \\div 5 = 4$ bags.",
                     "Receipt: $4 \\times 5 = 20$ ✓."],
                    "$4$ bags",
                    ["Eq(4*5, 20)", "Eq(Rational(20, 5), 4)"]),
            ]),
            tryitset("How many bundles?", "Step up by the bundle size and count the steps.", [
                withfig(tp("The picture shows $20$ sweets in bags of $5$. The number of bags is:",
                   ["$4$", "$5$", "$15$"],
                   "Counting in fives to $20$ takes four steps, so four bags: $20 \\div 5 = 4$. Answering $5$ repeats the bag size, and $15$ subtracts instead.",
                   ["Eq(4*5, 20)", "Eq(Rational(20, 5), 4)",
                    "Eq(20 - 5, 15)"]), fig_group20),
                tp("How many boxes of $2$ can be filled from $16$ eggs?",
                   ["$8$", "$2$", "$14$"],
                   "$8 \\times 2 = 16$, so eight boxes. Counting in twos to $16$ takes eight steps.",
                   ["Eq(8*2, 16)", "Eq(Rational(16, 2), 8)"]),
                tp("$30$ stones into piles of $10$ makes:",
                   ["$3$ piles", "$10$ piles", "$20$ piles"],
                   "Three whole bundles of ten make $30$, so $30 \\div 10 = 3$ piles. Answering $10$ repeats the pile size.",
                   ["Eq(3*10, 30)", "Eq(Rational(30, 10), 3)"]),
            ]),
            tapq("Which number does the answer count?", "\"$12$ buuz into bags of $3$.\" The answer $4$ counts:",
                 ["the bags", "the buuz in each bag",
                  "the buuz left over", "the buuz altogether"],
                 "The bag SIZE was given as $3$, so the answer must be the number of bags: four bags of three, $4 \\times 3 = 12$ ✓. Had the question said \"between $3$ children\", the same $4$ would have counted buuz per child.",
                 ["Eq(4*3, 12)", "Eq(Rational(12, 3), 4)"]),
            funfact("Shops group, families share",
                    "Almost every packing job in the world is grouping: eggs into trays of ten, tea into boxes of twenty, sheep into pens of fifty. Almost every meal is sharing. The two questions feel so different that many languages use different words for them — and mathematics quietly answers both with one division."),
            withfig(teach("Concept B", "Two questions, one fact", [
                "Put the two pictures side by side. Sharing $12$ between $3$ children gives $4$ each. Grouping $12$ into bags of $3$ gives $4$ bags.",
                "Both are $12 \\div 3 = 4$. The arithmetic is identical; what changes is what the $3$ and the $4$ MEAN — sharers and share size, or bundle size and bundle count.",
                "That is a real economy. You never have to learn \"sharing facts\" and \"grouping facts\" separately — there is one set of division facts, and the story tells you how to read the answer.",
            ]), fig_both),
            workedset("Name the question, then answer it",
                      "\"Between\" shares; \"into groups of\" groups.", [
                wex("Is \"$18$ pencils into boxes of $6$\" sharing or grouping?",
                    ["The box SIZE is given, so it is grouping.",
                     "$18 \\div 6 = 3$ boxes; receipt $3 \\times 6 = 18$ ✓."],
                    "grouping — $3$ boxes",
                    ["Eq(3*6, 18)", "Eq(Rational(18, 6), 3)"]),
                wex("Is \"$18$ pencils between $6$ children\" sharing or grouping?",
                    ["The number of PARTS is given, so it is sharing.",
                     "$18 \\div 6 = 3$ pencils each; same fact, different meaning."],
                    "sharing — $3$ each",
                    ["Eq(6*3, 18)", "Eq(Rational(18, 6), 3)"]),
            ]),
            tryitset("Sharing or grouping?", "What is given — the number of parts, or their size?", [
                tp("\"$24$ chairs arranged in rows of $4$.\" This is:",
                   ["grouping — the row size is given",
                    "sharing — the number of rows is given",
                    "neither — it is a multiplication"],
                   "\"Rows of $4$\" fixes the size, so the question is how many rows: $24 \\div 4 = 6$ rows.",
                   ["Eq(6*4, 24)", "Eq(Rational(24, 4), 6)"]),
                tp("\"$24$ chairs shared equally between $4$ rooms.\" Each room gets:",
                   ["$6$ chairs", "$4$ chairs", "$20$ chairs"],
                   "The number of parts is given, so this is sharing: $24 \\div 4 = 6$ chairs per room. Note it is the same division as the grouping question above.",
                   ["Eq(4*6, 24)", "Eq(Rational(24, 4), 6)"]),
                tp("Which question does $16 \\div 4 = 4$ NOT answer?",
                   ["how many bags of $16$ fit into $4$",
                    "how many bags of $4$ fit into $16$",
                    "how much each of $4$ children gets from $16$"],
                   "The first swaps the pile and the bundle size — you cannot fill a bag of sixteen from a pile of four. The other two are the grouping and sharing readings of the same fact.",
                   ["Eq(4*4, 16)", "Eq(Rational(16, 4), 4)", "16 > 4"]),
            ]),
            tapq("The words that decide", "Which phrase tells you the question is GROUPING?",
                 ["\"into bags of $5$\"", "\"between $5$ children\"",
                  "\"shared equally among $5$\"", "\"split $5$ ways\""],
                 "\"Into bags of $5$\" fixes the bundle SIZE and leaves the number of bags to be found. The other three all name how many parts there are, which makes them sharing.",
                 ["Eq(Rational(20, 5), 4)", "Eq(5*4, 20)"]),
            recap([
                "Grouping asks how many bundles of a given size fit into a total.",
                "Sharing gives the number of parts and asks their size; grouping gives the size and asks the number.",
                "One division fact answers both — only the meaning of the answer changes.",
                "\"Into groups of\" is grouping; \"between\" or \"among\" is sharing.",
            ]),
            tip("When a division question arrives, ask which of the two numbers you were handed: the number of PARTS, or the SIZE of a part. That single question tells you what your answer will mean."),
            tryitset("Chapter practice", "Read the question type before you divide.", [
                tp("$21$ sweets into bags of $3$ makes:",
                   ["$7$ bags", "$3$ bags", "$18$ bags"],
                   "$7 \\times 3 = 21$, so seven bags. Counting in threes to $21$ takes seven steps.",
                   ["Eq(7*3, 21)", "Eq(Rational(21, 3), 7)"]),
                tp("$40$ stones shared between $10$ children gives each:",
                   ["$4$", "$10$", "$30$"],
                   "$10 \\times 4 = 40$, so each child gets $4$. This is sharing — the number of children was given.",
                   ["Eq(10*4, 40)", "Eq(Rational(40, 10), 4)"]),
                tp("A fact that answers BOTH \"$15$ into bags of $5$\" and \"$15$ between $5$ children\" is:",
                   ["$15 \\div 5 = 3$", "$15 \\div 3 = 5$",
                    "$15 \\times 5 = 75$"],
                   "Both questions divide fifteen by five: three bags, or three each. The second fact is true but answers a different pair of questions — bundles of three.",
                   ["Eq(Rational(15, 5), 3)", "Eq(5*3, 15)",
                    "Eq(Rational(15, 3), 5)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Grouping\"",
                    "Two questions, one set of facts — and you already know most of those facts, because they are the times tables read backwards. That is exactly what the next lesson does.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Division Facts from the Tables
# ==========================================================================

def lesson_facts_from_tables():
    fig_family = fig_groups((5, "row 1", C_ACCENT), (5, "row 2", C_ACCENT),
                            (5, "row 3", C_ACCENT), (5, "row 4", C_ACCENT))
    fig_tens = fig_groups((10, "ten 1", C_GREEN), (10, "ten 2", C_GREEN),
                          (10, "ten 3", C_GREEN))
    return {
        "slug": "division-facts-from-the-tables",
        "title": "Division Facts from the Tables",
        "concreteComparison": (
            "There is no such thing as a division table to learn. Every "
            "division fact is a times fact read backwards: because "
            "$4 \\times 5 = 20$, you already know both $20 \\div 4 = 5$ "
            "and $20 \\div 5 = 4$ — two facts you never had to memorise."),
        "objective": (
            "Read division facts out of the tables of $2$, $5$ and $10$, "
            "write the four facts of a multiplication–division family, and "
            "use them to divide quickly."),
        "concept": [
            "**Every times fact gives two division facts.** From "
            "$4 \\times 5 = 20$ come $20 \\div 4 = 5$ and $20 \\div 5 = "
            "4$. Together with the turnaround $5 \\times 4 = 20$, that is "
            "a family of four facts built on three numbers.",
            "**Dividing by 2 is halving.** $16 \\div 2 = 8$ because "
            "$2 \\times 8 = 16$. Only even numbers divide by $2$ exactly "
            "— an odd number always leaves one over.",
            "**Dividing by 10 strips a zero, and dividing by 5 counts "
            "fives.** $30 \\div 10 = 3$ because three whole bundles of "
            "ten make thirty. And $30 \\div 5 = 6$ because six fives do: "
            "halve the bundles and you double their number.",
        ],
        "keyIdea": (
            "Division facts are not new facts. Each one is a times fact "
            "read backwards, so the tables you already know answer every "
            "division you meet."),
        "facts": [
            {"title": "One family, four facts",
             "latex": "4 \\times 5 = 20",
             "explanation": "Also gives 5 × 4 = 20, 20 ÷ 4 = 5 and 20 ÷ 5 = 4."},
            {"title": "Dividing by ten",
             "latex": "30 \\div 10 = 3",
             "explanation": "Three whole bundles of ten make thirty."},
        ],
        "workedExamples": [
            {"id": "g3dv-l3-we1",
             "statement": "Write the four facts of the family for $4$, $5$ and $20$.",
             "note": "Two multiplications, two divisions.",
             "solution": ("$4 \\times 5 = 20$ and $5 \\times 4 = 20$ build the "
                          "twenty; $20 \\div 4 = 5$ and $20 \\div 5 = 4$ take it "
                          "apart. Four facts from three numbers — and learning "
                          "any one of them delivers the rest."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*5, 20)", "Eq(5*4, 20)", "Eq(Rational(20, 4), 5)",
                       "Eq(Rational(20, 5), 4)"]},
            {"id": "g3dv-l3-we2",
             "statement": "Find $30 \\div 5$ and $30 \\div 10$, and say how the two answers are related.",
             "note": "Both come out of tables you know.",
             "solution": ("$5 \\times 6 = 30$, so $30 \\div 5 = 6$. And "
                          "$10 \\times 3 = 30$, so $30 \\div 10 = 3$. Halving "
                          "the bundle size from ten to five doubles the number "
                          "of bundles: $3$ becomes $6$. Smaller bundles, more "
                          "of them — always."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*6, 30)", "Eq(Rational(30, 5), 6)",
                       "Eq(10*3, 30)", "Eq(Rational(30, 10), 3)",
                       "Eq(2*3, 6)"]},
        ],
        "commonMistakes": [
            {"text": "Turning a division round — answering 20 ÷ 5 as 5 ÷ 20 or claiming both are the same.",
             "correction": "Multiplication turns around; division does not. 20 ÷ 5 = 4 shares a pile of twenty, while 5 ÷ 20 tries to share five between twenty — a different and much smaller thing.",
             "authored": True},
            {"text": "Expecting an odd number to halve exactly, e.g. 15 ÷ 2 = 7.",
             "correction": "Only even numbers divide by 2 with nothing over: 7 × 2 = 14, not 15. This year every division is chosen to come out exactly, and 15 ÷ 2 does not.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3dv-l3-t1",
             "statement": "Use the times tables to find $18 \\div 2$ and write its receipt.",
             "solution": ("$2 \\times 9 = 18$, so $18 \\div 2 = 9$. Receipt: "
                          "$2 \\times 9 = 18$ ✓ — and halving $18$ agrees."),
             "check": ["Eq(2*9, 18)", "Eq(Rational(18, 2), 9)"]},
            {"id": "g3dv-l3-t2",
             "statement": "Write the four facts of the family for $2$, $10$ and $20$.",
             "solution": ("$2 \\times 10 = 20$, $10 \\times 2 = 20$, "
                          "$20 \\div 2 = 10$ and $20 \\div 10 = 2$."),
             "check": ["Eq(2*10, 20)", "Eq(Rational(20, 2), 10)",
                       "Eq(Rational(20, 10), 2)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Times tables, read backwards", [
                "The array below is $4$ rows of $5$ — a picture you met when learning the tables. It says $4 \\times 5 = 20$.",
                "But read it as sharing and it says $20 \\div 4 = 5$: twenty stones in four rows, five to a row. Read it as grouping and it says $20 \\div 5 = 4$.",
                "So one array carries four facts: $4 \\times 5 = 20$, $5 \\times 4 = 20$, $20 \\div 4 = 5$, $20 \\div 5 = 4$. There is no division table to learn — only the times tables, read the other way.",
            ]), fig_family),
            workedset("Read the family", "Two multiplications, two divisions.", [
                wex("Write the four facts for $4$, $5$ and $20$.",
                    ["Building: $4 \\times 5 = 20$ and $5 \\times 4 = 20$.",
                     "Taking apart: $20 \\div 4 = 5$ and $20 \\div 5 = 4$."],
                    "four facts",
                    ["Eq(4*5, 20)", "Eq(Rational(20, 4), 5)",
                     "Eq(Rational(20, 5), 4)"]),
                wex("Write the four facts for $2$, $9$ and $18$.",
                    ["Building: $2 \\times 9 = 18$ and $9 \\times 2 = 18$.",
                     "Taking apart: $18 \\div 2 = 9$ and $18 \\div 9 = 2$."],
                    "four facts",
                    ["Eq(2*9, 18)", "Eq(Rational(18, 2), 9)",
                     "Eq(Rational(18, 9), 2)"]),
            ]),
            tryitset("Use the family", "Find the times fact, then read it backwards.", [
                tp("$16 \\div 2$ is:",
                   ["$8$", "$14$", "$32$"],
                   "$2 \\times 8 = 16$, so $16 \\div 2 = 8$ — dividing by two is halving. $14$ subtracts and $32$ doubles.",
                   ["Eq(2*8, 16)", "Eq(Rational(16, 2), 8)", "Eq(16 - 2, 14)"]),
                tp("If $5 \\times 7 = 35$, then $35 \\div 5$ is:",
                   ["$7$", "$5$", "$30$"],
                   "The times fact read backwards: seven fives make thirty-five, so thirty-five holds seven fives.",
                   ["Eq(5*7, 35)", "Eq(Rational(35, 5), 7)"]),
                tp("Which fact does NOT belong to the family of $2$, $8$ and $16$?",
                   ["$16 \\div 32 = 2$", "$16 \\div 8 = 2$",
                    "$8 \\times 2 = 16$"],
                   "$32$ is not one of the three numbers at all. The real family is $2 \\times 8 = 16$, $8 \\times 2 = 16$, $16 \\div 2 = 8$ and $16 \\div 8 = 2$.",
                   ["Eq(8*2, 16)", "Eq(Rational(16, 8), 2)",
                    "Eq(Rational(16, 2), 8)"]),
            ]),
            tapq("Does division turn around?", "You know $20 \\div 5 = 4$. Is $5 \\div 20$ also $4$?",
                 ["no — division does not turn around",
                  "yes, division turns around like multiplication",
                  "yes, but only for the five times table",
                  "yes — both equal $4$"],
                 "Multiplication turns around; division does not. $20 \\div 5 = 4$ shares a pile of twenty, while $5 \\div 20$ would share five between twenty — far less than one each, which is not even a whole number.",
                 ["Eq(Rational(20, 5), 4)", "Eq(5*4, 20)", "20 > 5"]),
            funfact("The oldest division problem we have",
                    "A clay tablet from ancient Mesopotamia, thousands of years old, sets a problem about sharing barley equally among workers — and solves it exactly the way you just did, by finding the multiplication that rebuilds the pile. The notation has changed completely. The method has not."),
            withfig(teach("Concept B", "Dividing by 2, 5 and 10", [
                "Three divisors are worth knowing cold. Dividing by $2$ is halving: $16 \\div 2 = 8$, because $2 \\times 8 = 16$. Only even numbers halve exactly.",
                "Dividing by $10$ counts whole bundles — the picture below shows the three tens inside $30$, so $30 \\div 10 = 3$.",
                "And dividing by $5$ counts fives: $30 \\div 5 = 6$. Compare the two — halving the bundle size from ten to five doubled the number of bundles, from $3$ to $6$. Smaller bundles always means more of them.",
            ]), fig_tens),
            workedset("The three easy divisors",
                      "Halve, count fives, or count whole tens.", [
                wex("Find $30 \\div 10$ and $30 \\div 5$.",
                    ["$10 \\times 3 = 30$, so $30 \\div 10 = 3$.",
                     "$5 \\times 6 = 30$, so $30 \\div 5 = 6$.",
                     "Half the bundle size, double the count: $3 \\to 6$ ✓."],
                    "$3$ and $6$",
                    ["Eq(Rational(30, 10), 3)", "Eq(Rational(30, 5), 6)",
                     "Eq(2*3, 6)"]),
                wex("Find $80 \\div 10$ and $14 \\div 2$.",
                    ["$10 \\times 8 = 80$, so $80 \\div 10 = 8$ — the zero comes off.",
                     "$2 \\times 7 = 14$, so $14 \\div 2 = 7$ — halving."],
                    "$8$ and $7$",
                    ["Eq(10*8, 80)", "Eq(Rational(80, 10), 8)",
                     "Eq(Rational(14, 2), 7)"]),
            ]),
            tryitset("Halve, five, ten", "Which table holds the answer?", [
                tp("$60 \\div 10$ is:",
                   ["$6$", "$50$", "$600$"],
                   "Six whole bundles of ten make sixty, so $60 \\div 10 = 6$ — the zero comes off. $50$ subtracts and $600$ multiplies.",
                   ["Eq(10*6, 60)", "Eq(Rational(60, 10), 6)",
                    "Eq(60 - 10, 50)"]),
                tp("$45 \\div 5$ is:",
                   ["$9$", "$40$", "$5$"],
                   "$5 \\times 9 = 45$, so nine fives make forty-five. Note $45$ ends in $5$, the mark of an odd number of fives.",
                   ["Eq(5*9, 45)", "Eq(Rational(45, 5), 9)",
                    "Eq(Mod(45, 10), 5)"]),
                tp("Which of these does NOT divide by $2$ exactly?",
                   ["$15$", "$14$", "$16$"],
                   "$15$ is odd, so halving it leaves one over. $14 \\div 2 = 7$ and $16 \\div 2 = 8$ both come out exactly.",
                   ["Eq(Mod(15, 2), 1)", "Eq(Rational(14, 2), 7)",
                    "Eq(Rational(16, 2), 8)"]),
            ]),
            tapq("Bundle size against bundle count", "$40 \\div 10 = 4$. Without calculating, is $40 \\div 5$ bigger or smaller?",
                 ["bigger — smaller bundles means more of them",
                  "smaller — dividing by a smaller number gives less",
                  "the same",
                  "you cannot tell without working it out"],
                 "Halving the bundle size doubles how many fit: $40 \\div 5 = 8$, twice the $4$. Smaller bundles always means MORE bundles, which surprises people who expect a smaller divisor to give a smaller answer.",
                 ["Eq(Rational(40, 10), 4)", "Eq(Rational(40, 5), 8)",
                  "Eq(2*4, 8)"]),
            recap([
                "There is no division table — every division fact is a times fact read backwards.",
                "Three numbers make four facts: $4 \\times 5 = 20$, $5 \\times 4 = 20$, $20 \\div 4 = 5$, $20 \\div 5 = 4$.",
                "Division does NOT turn around: $20 \\div 5$ and $5 \\div 20$ are quite different.",
                "Halving divides by $2$; counting whole tens divides by $10$; and smaller bundles always means more of them.",
            ]),
            tip("When a division stalls, ask the times question instead: \"what times $5$ makes $35$?\" is the same problem in a form your memory already answers."),
            tryitset("Chapter practice", "Find the times fact hiding inside.", [
                tp("$24 \\div 2$ is:",
                   ["$12$", "$22$", "$48$"],
                   "$2 \\times 12 = 24$, so halving twenty-four gives twelve. $22$ subtracts and $48$ doubles.",
                   ["Eq(2*12, 24)", "Eq(Rational(24, 2), 12)"]),
                tp("$50 \\div 5$ is:",
                   ["$10$", "$45$", "$5$"],
                   "$5 \\times 10 = 50$, so ten fives make fifty. Equivalently, $50$ is five bundles of ten or ten bundles of five.",
                   ["Eq(5*10, 50)", "Eq(Rational(50, 5), 10)"]),
                tp("From $10 \\times 7 = 70$ you can read off:",
                   ["$70 \\div 10 = 7$", "$70 \\div 7 = 10$ only",
                    "$7 \\div 70 = 10$"],
                   "The family gives BOTH $70 \\div 10 = 7$ and $70 \\div 7 = 10$; the first option is one of them. The third turns the division round, which is never allowed.",
                   ["Eq(10*7, 70)", "Eq(Rational(70, 10), 7)",
                    "Eq(Rational(70, 7), 10)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Division Facts from the Tables\"",
                    "Every division fact you will meet this year is already sitting inside a times table you know. The next lesson reaches for the threes and fours the same way — no new memorising, just reading the same facts from the other end.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Dividing by 3 and 4
# ==========================================================================

def lesson_by_three_four():
    fig_24by3 = bundles_of(8, 3, "bag")
    fig_24by4 = shares(4, 6)
    fig_halve = fig_groups((12, "half of 24", C_ACCENT),
                           (6, "then half of 12", C_WARM))
    return {
        "slug": "dividing-by-3-and-4",
        "title": "Dividing by 3 and 4",
        "concreteComparison": (
            "Twenty-four is a generous number: it shares between $3$ "
            "exactly, and between $4$ exactly. Dividing by $3$ means "
            "counting threes; dividing by $4$ can be done by halving, and "
            "then halving again."),
        "objective": (
            "Divide by $3$ using the three times table, divide by $4$ by "
            "halving twice, and recognise which numbers divide exactly by "
            "each."),
        "concept": [
            "**Dividing by 3 counts threes.** $24 \\div 3 = 8$ because "
            "$3 \\times 8 = 24$ — eight bags of three empty a pile of "
            "twenty-four. If counting in threes never lands exactly on "
            "the number, it does not divide by $3$.",
            "**Dividing by 4 is halving twice.** $24 \\div 4$: half of "
            "$24$ is $12$, and half of $12$ is $6$. So $24 \\div 4 = 6$. "
            "It works because four is two twos — sharing between four is "
            "sharing between two, then splitting each share again.",
            "**Not every number divides exactly.** $24$ divides by both "
            "$3$ and $4$, but $22$ divides by neither: counting in threes "
            "goes $21, 24$ and steps over it, and halving twice gives "
            "$11$ and then a half. This year every problem is chosen so "
            "the division comes out exactly.",
        ],
        "keyIdea": (
            "Divide by $3$ by counting threes, and by $4$ by halving "
            "twice — and check every answer by multiplying it back."),
        "facts": [
            {"title": "Counting threes",
             "latex": "24 \\div 3 = 8",
             "explanation": "Eight bags of three make twenty-four."},
            {"title": "Halve, then halve again",
             "latex": "24 \\div 4 = 6",
             "explanation": "Half of 24 is 12; half of 12 is 6 — because four is two twos."},
        ],
        "workedExamples": [
            {"id": "g3dv-l4-we1",
             "statement": "Find $24 \\div 3$ and prove it with the receipt.",
             "note": "Count in threes, or find the times fact.",
             "solution": ("Counting in threes: $3, 6, 9, 12, 15, 18, 21, 24$ — "
                          "eight steps. So $24 \\div 3 = 8$, and the receipt "
                          "$3 \\times 8 = 24$ ✓ confirms it."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*8, 24)", "Eq(Rational(24, 3), 8)"]},
            {"id": "g3dv-l4-we2",
             "statement": "Find $24 \\div 4$ by halving twice.",
             "note": "Four is two twos.",
             "solution": ("Half of $24$ is $12$; half of $12$ is $6$. So "
                          "$24 \\div 4 = 6$. It works because sharing between "
                          "four is sharing between two and then halving each "
                          "share again. Receipt: $4 \\times 6 = 24$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(24, 2), 12)", "Eq(Rational(12, 2), 6)",
                       "Eq(4*6, 24)", "Eq(Rational(24, 4), 6)"]},
        ],
        "commonMistakes": [
            {"text": "Halving only once when dividing by 4 — answering 24 ÷ 4 = 12.",
             "correction": "Halving once divides by 2, not 4. The second halving is what finishes the job: 12 halved is 6, and 4 × 6 = 24 ✓ while 4 × 12 = 48.",
             "authored": True},
            {"text": "Forcing a division that does not come out, such as 22 ÷ 4 = 5.",
             "correction": "The receipt exposes it: 4 × 5 = 20, not 22. Twenty-two does not divide by four exactly, and every division in this topic is chosen so that it does.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3dv-l4-t1",
             "statement": "Find $27 \\div 3$ and give the receipt.",
             "solution": ("$3 \\times 9 = 27$, so $27 \\div 3 = 9$. Receipt: "
                          "$3 \\times 9 = 27$ ✓."),
             "check": ["Eq(3*9, 27)", "Eq(Rational(27, 3), 9)"]},
            {"id": "g3dv-l4-t2",
             "statement": "Find $32 \\div 4$ by halving twice.",
             "solution": ("Half of $32$ is $16$; half of $16$ is $8$. So "
                          "$32 \\div 4 = 8$, and $4 \\times 8 = 32$ ✓."),
             "check": ["Eq(Rational(32, 2), 16)", "Eq(Rational(16, 2), 8)",
                       "Eq(4*8, 32)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counting threes", [
                "Twenty-four stones packed into bags of three — the picture below shows the bags.",
                "Count them: eight. Or count up in threes and stop at $24$: $3, 6, 9, 12, 15, 18, 21, 24$ — again eight steps.",
                "So $24 \\div 3 = 8$, with receipt $3 \\times 8 = 24$ ✓. Every division by three is this same walk up the three times table.",
            ]), fig_24by3),
            workedset("Divide by three", "Walk up the threes and count the steps.", [
                wex("Find $24 \\div 3$.",
                    ["Count in threes to $24$: eight steps.",
                     "$24 \\div 3 = 8$; receipt $3 \\times 8 = 24$ ✓."],
                    "$8$",
                    ["Eq(3*8, 24)", "Eq(Rational(24, 3), 8)"]),
                wex("Find $21 \\div 3$.",
                    ["$3 \\times 7 = 21$.",
                     "So $21 \\div 3 = 7$; receipt $3 \\times 7 = 21$ ✓."],
                    "$7$",
                    ["Eq(3*7, 21)", "Eq(Rational(21, 3), 7)"]),
            ]),
            tryitset("Threes", "Which three times fact reaches the number?", [
                tp("$18 \\div 3$ is:",
                   ["$6$", "$15$", "$54$"],
                   "$3 \\times 6 = 18$, so six threes make eighteen. $15$ subtracts and $54$ multiplies.",
                   ["Eq(3*6, 18)", "Eq(Rational(18, 3), 6)", "Eq(18 - 3, 15)"]),
                tp("$30 \\div 3$ is:",
                   ["$10$", "$27$", "$3$"],
                   "$3 \\times 10 = 30$, so ten threes make thirty. Receipt ✓.",
                   ["Eq(3*10, 30)", "Eq(Rational(30, 3), 10)"]),
                tp("Which number does NOT divide by $3$ exactly?",
                   ["$20$", "$21$", "$24$"],
                   "Counting in threes goes $18, 21, 24$ and steps straight over $20$ — indeed $20$ leaves $2$ over. The other two land exactly.",
                   ["Eq(Mod(20, 3), 2)", "Eq(Rational(21, 3), 7)",
                    "Eq(Rational(24, 3), 8)"]),
            ]),
            tapq("Counting the steps", "Counting in threes from $3$ reaches $27$. How many steps was that?",
                 ["$9$", "$27$", "$3$", "$8$"],
                 "$3 \\times 9 = 27$, so nine steps of three arrive exactly on twenty-seven — which is another way of saying $27 \\div 3 = 9$.",
                 ["Eq(3*9, 27)", "Eq(Rational(27, 3), 9)"]),
            funfact("Why 24 is such a friendly number",
                    "Twenty-four shares out exactly between $2$, $3$, $4$, $6$, $8$ and $12$ — more ways than any smaller number manages. That is why hours come in $24$s and why old measures counted in dozens: a number that divides many ways makes sharing easy, and traders noticed long before mathematicians explained it."),
            withfig(teach("Concept B", "Halving twice", [
                "Now share those same twenty-four between $4$ children — the picture below shows the result: six each.",
                "There is a neat route to it. Half of $24$ is $12$, and half of $12$ is $6$. So $24 \\div 4 = 6$.",
                "It works because four is two twos: sharing between four is sharing between two, then splitting each of those shares in half again. Halve ONCE and you have only divided by two — that missing second step is the classic slip.",
            ]), fig_24by4),
            workedset("Divide by four", "Halve, then halve again.", [
                wex("Find $24 \\div 4$.",
                    ["Half of $24$ is $12$.",
                     "Half of $12$ is $6$.",
                     "$24 \\div 4 = 6$; receipt $4 \\times 6 = 24$ ✓."],
                    "$6$",
                    ["Eq(Rational(24, 2), 12)", "Eq(Rational(12, 2), 6)",
                     "Eq(4*6, 24)"]),
                wex("Find $40 \\div 4$.",
                    ["Half of $40$ is $20$.",
                     "Half of $20$ is $10$.",
                     "$40 \\div 4 = 10$; receipt $4 \\times 10 = 40$ ✓."],
                    "$10$",
                    ["Eq(Rational(40, 2), 20)", "Eq(Rational(20, 2), 10)",
                     "Eq(4*10, 40)"]),
            ]),
            tryitset("Fours", "Two halvings, not one.", [
                tp("$28 \\div 4$ is:",
                   ["$7$", "$14$", "$24$"],
                   "Half of $28$ is $14$, and half of $14$ is $7$. Stopping at $14$ has only divided by two — the commonest mistake here.",
                   ["Eq(Rational(28, 2), 14)", "Eq(Rational(14, 2), 7)",
                    "Eq(4*7, 28)"]),
                tp("$36 \\div 4$ is:",
                   ["$9$", "$18$", "$32$"],
                   "Half of $36$ is $18$; half of $18$ is $9$. Receipt: $4 \\times 9 = 36$ ✓.",
                   ["Eq(Rational(36, 2), 18)", "Eq(Rational(18, 2), 9)",
                    "Eq(4*9, 36)"]),
                withfig(tp("The picture shows both halvings of $24$. Bat divides $24$ by $4$ and answers $12$. He:",
                   ["halved only once", "halved three times",
                    "subtracted instead"],
                   "Halving once divides by two, giving $12$ — the first group in the picture. The second halving finishes the job at $6$. The receipt catches the slip: $4 \\times 12 = 48$, not $24$.",
                   ["Eq(Rational(24, 2), 12)", "Eq(4*12, 48)",
                    "Eq(Rational(24, 4), 6)"]), fig_halve),
            ]),
            tapq("Why halving twice works", "Dividing by $4$ can be done as two halvings because:",
                 ["four is two twos",
                  "halving always divides by four",
                  "four is one more than three",
                  "it only works for the number $24$"],
                 "Sharing between four is sharing between two and then halving each share again, because $2 \\times 2 = 4$. It works for every number that divides exactly: $40 \\to 20 \\to 10$, and $4 \\times 10 = 40$ ✓.",
                 ["Eq(2*2, 4)", "Eq(Rational(40, 2), 20)",
                  "Eq(Rational(20, 2), 10)"]),
            recap([
                "Divide by $3$ by counting threes — the number of steps is the answer.",
                "Divide by $4$ by halving twice, because four is two twos.",
                "Halving once only divides by $2$; the second halving is not optional.",
                "Not every number divides exactly — the receipt is what tells you.",
            ]),
            tip("For any division by four, say \"half, half\" as you work. Two words, two steps, and you will never hand in the answer to a division by two by mistake."),
            tryitset("Chapter practice", "Count threes, or halve twice.", [
                tp("$15 \\div 3$ is:",
                   ["$5$", "$12$", "$45$"],
                   "$3 \\times 5 = 15$, so five threes make fifteen. Receipt ✓.",
                   ["Eq(3*5, 15)", "Eq(Rational(15, 3), 5)"]),
                tp("$20 \\div 4$ is:",
                   ["$5$", "$10$", "$16$"],
                   "Half of $20$ is $10$; half of $10$ is $5$. Answering $10$ stops after one halving.",
                   ["Eq(Rational(20, 2), 10)", "Eq(Rational(10, 2), 5)",
                    "Eq(4*5, 20)"]),
                tp("Which division does NOT come out exactly?",
                   ["$26 \\div 4$", "$24 \\div 4$", "$28 \\div 4$"],
                   "Halving $26$ gives $13$, and $13$ is odd, so the second halving cannot finish — indeed $4 \\times 6 = 24$ and $4 \\times 7 = 28$ step straight over $26$.",
                   ["Eq(Rational(26, 2), 13)", "Eq(Mod(13, 2), 1)",
                    "Eq(4*6, 24)", "Eq(4*7, 28)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Dividing by 3 and 4\"",
                    "You can now divide by $2$, $3$, $4$, $5$ and $10$ — every divisor this year needs. The last lesson stops asking how to divide and starts asking WHEN: how to tell from a story whether to multiply or to divide.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Choosing the Operation
# ==========================================================================

def lesson_choosing():
    fig_mult = bundles_of(5, 4, "shelf")
    fig_div = shares(4, 5, "friend")
    return {
        "slug": "choosing-the-operation",
        "title": "Choosing the Operation",
        "concreteComparison": (
            "\"Five shelves with $4$ jars on each\" and \"$20$ jars "
            "shared between $5$ shelves\" use the same three numbers — "
            "$5$, $4$ and $20$ — but ask opposite questions. Which number "
            "is MISSING is what decides whether you multiply or divide."),
        "objective": (
            "Decide from a story whether to multiply or divide, by "
            "working out which of the three numbers in the family is "
            "missing."),
        "concept": [
            "**Three numbers, and one of them is missing.** Every times "
            "or sharing story involves a number of groups, a group size, "
            "and a total. If the TOTAL is missing you multiply; if a "
            "group count or group size is missing you divide.",
            "**Missing total means multiply.** \"Five shelves with $4$ "
            "jars each — how many jars?\" gives both group facts and "
            "wants the total: $5 \\times 4 = 20$.",
            "**Missing group means divide.** \"Twenty jars on $5$ "
            "shelves — how many on each?\" gives the total and the number "
            "of groups: $20 \\div 5 = 4$. And \"twenty jars, $4$ to a "
            "shelf — how many shelves?\" gives the total and the size: "
            "$20 \\div 4 = 5$.",
        ],
        "keyIdea": (
            "Find which of the three — groups, group size, total — the "
            "story leaves out. Missing total, multiply; missing group, "
            "divide."),
        "facts": [
            {"title": "Missing total: multiply",
             "latex": "5 \\times 4 = 20",
             "explanation": "Both group facts given, total wanted."},
            {"title": "Missing group: divide",
             "latex": "20 \\div 5 = 4",
             "explanation": "Total given, one group fact given, the other wanted."},
        ],
        "workedExamples": [
            {"id": "g3dv-l5-we1",
             "statement": "Five shelves hold $4$ jars each. How many jars? Say which number was missing.",
             "note": "Groups, size, total — which one is absent?",
             "solution": ("Groups: $5$. Size: $4$. The TOTAL is missing, so "
                          "multiply: $5 \\times 4 = 20$ jars. Sense check — "
                          "$20$ is bigger than either given number, as a total "
                          "should be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*4, 20)", "20 > 5", "20 > 4"]},
            {"id": "g3dv-l5-we2",
             "statement": "Twenty jars are shared equally between $5$ shelves. How many on each?",
             "note": "This time the total is given.",
             "solution": ("Total: $20$. Groups: $5$. The group SIZE is missing, "
                          "so divide: $20 \\div 5 = 4$ jars per shelf. Receipt: "
                          "$5 \\times 4 = 20$ ✓, and $4$ is smaller than the "
                          "total, as a share must be."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(20, 5), 4)", "Eq(5*4, 20)", "4 < 20"]},
        ],
        "commonMistakes": [
            {"text": "Multiplying whenever two numbers appear, so \"20 jars on 5 shelves\" becomes 100.",
             "correction": "The total (20) was already given, so multiplying invents jars that do not exist. The missing number is the group size: 20 ÷ 5 = 4.",
             "authored": True},
            {"text": "Ignoring the size of the answer — giving a share bigger than the total.",
             "correction": "A share is always smaller than the pile it came from, and a total is always bigger than one group. Check the size of your answer against the story before writing it down.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3dv-l5-t1",
             "statement": "Three boxes hold $6$ pencils each. How many pencils? Which number was missing?",
             "solution": ("The total was missing, so multiply: $3 \\times 6 = 18$ "
                          "pencils — bigger than both given numbers ✓."),
             "check": ["Eq(3*6, 18)", "18 > 6"]},
            {"id": "g3dv-l5-t2",
             "statement": "Eighteen pencils are packed $6$ to a box. How many boxes? Which number was missing?",
             "solution": ("The number of GROUPS was missing, so divide: "
                          "$18 \\div 6 = 3$ boxes. Receipt: $3 \\times 6 = 18$ ✓."),
             "check": ["Eq(Rational(18, 6), 3)", "Eq(3*6, 18)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Missing total? Multiply.", [
                "Five shelves, four jars on each — the picture below. Nobody has told you the total, and the total is what is being asked for.",
                "Both group facts are known: how many groups ($5$) and how big each is ($4$). So multiply: $5 \\times 4 = 20$ jars.",
                "Check the size. A total must be bigger than either of the numbers that built it, and $20$ beats both $5$ and $4$ comfortably.",
            ]), fig_mult),
            workedset("Missing total", "Both group facts given — multiply.", [
                wex("Five shelves with $4$ jars each. How many jars?",
                    ["Groups $5$, size $4$, total missing.",
                     "$5 \\times 4 = 20$ jars.",
                     "Bigger than both given numbers ✓."],
                    "$20$ jars",
                    ["Eq(5*4, 20)", "20 > 5"]),
                wex("Six bags with $3$ stones each. How many stones?",
                    ["Groups $6$, size $3$, total missing.",
                     "$6 \\times 3 = 18$ stones ✓."],
                    "$18$ stones",
                    ["Eq(6*3, 18)", "18 > 6"]),
            ]),
            tryitset("Which is missing?", "Name the missing number before you calculate.", [
                tp("Four boxes hold $5$ apples each. The number of apples is:",
                   ["$20$", "$9$", "$1$"],
                   "The total is missing and both group facts are given, so multiply: $4 \\times 5 = 20$. Adding gives $9$ and subtracting gives $1$ — neither counts apples.",
                   ["Eq(4*5, 20)", "Eq(4 + 5, 9)", "Eq(5 - 4, 1)"]),
                tp("A herder ties $2$ horses at each of $7$ posts. The number of horses is:",
                   ["$14$", "$9$", "$5$"],
                   "Seven groups of two: $7 \\times 2 = 14$ horses. The total was the missing number.",
                   ["Eq(7*2, 14)", "Eq(7 + 2, 9)"]),
                tp("In \"$8$ plates with $3$ buuz each\", the missing number is:",
                   ["the total", "the number of plates",
                    "the buuz on one plate"],
                   "Both group facts are given — eight plates, three each — so the total is what is wanted: $8 \\times 3 = 24$ buuz.",
                   ["Eq(8*3, 24)", "24 > 8"]),
            ]),
            tapq("Total already known", "\"Twenty jars on $5$ shelves — how many on each?\" Should you multiply?",
                 ["no — the total is given, so divide",
                  "yes: $20 \\times 5 = 100$",
                  "yes, because there are two numbers",
                  "no — you should subtract"],
                 "The total ($20$) is already known, so multiplying would invent jars: $100$ is five times more than the shop has. The group size is missing, so divide: $20 \\div 5 = 4$.",
                 ["Eq(Rational(20, 5), 4)", "Eq(20*5, 100)", "100 > 20"]),
            funfact("The question hiding in the units",
                    "There is a second clue, and it never lies: look at what the answer should be measured in. \"How many jars\" and \"how many jars per shelf\" are different units, and only one of them can be right. When the words confuse you, ask what the answer is counting."),
            withfig(teach("Concept B", "Missing group? Divide.", [
                "Twenty jars shared between $5$ shelves — the picture below shows four on each.",
                "Here the total is given, so multiplying is out. What is missing is the group SIZE, and a missing group is found by dividing: $20 \\div 5 = 4$ jars per shelf.",
                "The other kind of missing group works the same way. \"Twenty jars, $4$ to a shelf — how many shelves?\" leaves the group COUNT out, so again divide: $20 \\div 4 = 5$ shelves.",
            ]), fig_div),
            workedset("Missing group", "Total given — divide.", [
                wex("Twenty jars between $5$ shelves. How many on each?",
                    ["Total $20$, groups $5$, size missing.",
                     "$20 \\div 5 = 4$ jars per shelf.",
                     "Receipt: $5 \\times 4 = 20$ ✓."],
                    "$4$ each",
                    ["Eq(Rational(20, 5), 4)", "Eq(5*4, 20)"]),
                wex("Twenty jars, $4$ to a shelf. How many shelves?",
                    ["Total $20$, size $4$, group count missing.",
                     "$20 \\div 4 = 5$ shelves.",
                     "Receipt: $5 \\times 4 = 20$ ✓ — the same receipt as above."],
                    "$5$ shelves",
                    ["Eq(Rational(20, 4), 5)", "Eq(5*4, 20)"]),
            ]),
            tryitset("Multiply or divide?", "Which of the three is the story missing?", [
                tp("$24$ pencils are shared between $4$ children. Each gets:",
                   ["$6$", "$96$", "$20$"],
                   "The total is given and the share size is missing, so divide: $24 \\div 4 = 6$. Multiplying gives $96$, four times more pencils than exist.",
                   ["Eq(Rational(24, 4), 6)", "Eq(24*4, 96)", "96 > 24"]),
                tp("$24$ pencils are packed $6$ to a box. The number of boxes is:",
                   ["$4$", "$144$", "$30$"],
                   "The total is given and the number of groups is missing, so divide: $24 \\div 6 = 4$ boxes. Receipt: $4 \\times 6 = 24$ ✓.",
                   ["Eq(Rational(24, 6), 4)", "Eq(4*6, 24)"]),
                tp("Which story should you MULTIPLY?",
                   ["$6$ boxes with $4$ pencils each",
                    "$24$ pencils in boxes of $4$",
                    "$24$ pencils between $6$ children"],
                   "Only the first leaves the total out. The other two hand you the total of $24$ and ask for a group fact, so both divide.",
                   ["Eq(6*4, 24)", "Eq(Rational(24, 4), 6)",
                    "Eq(Rational(24, 6), 4)"]),
            ]),
            tapq("Checking the size", "A story shares $30$ sweets between some children, and the answer comes out as $90$. What went wrong?",
                 ["it multiplied — a share cannot exceed the pile",
                  "nothing — $90$ can be correct",
                  "it divided when it should have multiplied",
                  "the pile must have been bigger than $30$"],
                 "A share is always smaller than the pile it came from, so $90$ from a pile of $30$ is impossible — the numbers were multiplied instead of divided. Between $3$ children, for instance, the answer would be $30 \\div 3 = 10$.",
                 ["Eq(Rational(30, 3), 10)", "Eq(30*3, 90)", "90 > 30"]),
            recap([
                "Every story has three numbers: how many groups, how big each is, and the total.",
                "Missing TOTAL means multiply; missing group count or group size means divide.",
                "A total is bigger than either group number; a share is smaller than the pile.",
                "The receipt checks the answer whichever way you went.",
            ]),
            tip("Write the three words — groups, size, total — and fill in the two the story gives you. The empty one names your operation before you have done any arithmetic at all."),
            tryitset("Chapter practice", "Name the missing number first.", [
                tp("$7$ nests with $3$ eggs each hold:",
                   ["$21$ eggs", "$10$ eggs", "$4$ eggs"],
                   "The total is missing, so multiply: $7 \\times 3 = 21$ eggs — more than either given number ✓.",
                   ["Eq(7*3, 21)", "21 > 7"]),
                tp("$21$ eggs are packed $3$ to a box. The number of boxes is:",
                   ["$7$", "$63$", "$18$"],
                   "The total is given and the group count is missing, so divide: $21 \\div 3 = 7$ boxes. Receipt: $7 \\times 3 = 21$ ✓.",
                   ["Eq(Rational(21, 3), 7)", "Eq(7*3, 21)"]),
                tp("$21$ eggs shared between $7$ children gives each:",
                   ["$3$", "$147$", "$14$"],
                   "Total given, share size missing, so divide: $21 \\div 7 = 3$ eggs each. All three of these questions live in one family — only the missing number moved.",
                   ["Eq(Rational(21, 7), 3)", "Eq(7*3, 21)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Choosing the Operation\" — and the topic",
                    "Sharing, grouping, the tables read backwards, the threes and fours, and choosing between times and divide. Every one of them rested on the same receipt: multiply the answer back and the pile must return. Next comes fractions — what happens when a share does not come out whole.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = shares(3, 4)
    fig_pr5 = bundles_of(6, 5, "bag")
    return [
        withprobfig(prob("g3dv-pr1", "The picture shows a plate of buuz shared between $3$ children. Write the division fact and its receipt.",
             "Each child has $4$, so $12 \\div 3 = 4$. Receipt: $3 \\times 4 = 12$ ✓ — the shares put back together return the plate.",
             ["Eq(Rational(12, 3), 4)", "Eq(3*4, 12)"]), fig_pr1),
        prob("g3dv-pr2", "Twenty-four stones are shared between $4$ children, and also packed into bags of $4$. Give both answers and say what each one counts.",
             "Both are $24 \\div 4 = 6$. In the sharing story the $6$ counts stones per child; in the grouping story it counts bags. Same arithmetic, different meaning — receipt $4 \\times 6 = 24$ ✓ either way.",
             ["Eq(Rational(24, 4), 6)", "Eq(4*6, 24)"]),
        prob("g3dv-pr3", "Write the four facts of the family for $3$, $7$ and $21$.",
             "$3 \\times 7 = 21$, $7 \\times 3 = 21$, $21 \\div 3 = 7$ and $21 \\div 7 = 3$. Three numbers, four facts.",
             ["Eq(3*7, 21)", "Eq(7*3, 21)", "Eq(Rational(21, 3), 7)",
              "Eq(Rational(21, 7), 3)"]),
        prob("g3dv-pr4", "Find $36 \\div 4$ by halving twice, showing both halvings.",
             "Half of $36$ is $18$; half of $18$ is $9$. So $36 \\div 4 = 9$, and the receipt $4 \\times 9 = 36$ ✓ confirms it. Stopping after one halving would answer $18$, which is $36 \\div 2$.",
             ["Eq(Rational(36, 2), 18)", "Eq(Rational(18, 2), 9)",
              "Eq(4*9, 36)", "Eq(Rational(36, 2), 18)"]),
        withprobfig(prob("g3dv-pr5", "The picture shows $30$ sweets in bags. Write the division fact, then say what happens to the number of bags if the bag size is halved.",
             "Six bags of five: $30 \\div 5 = 6$. Halving the bag size to make bags of $\\frac{5}{2}$ is awkward, so compare the other way — bags of ten give $30 \\div 10 = 3$, half as many bags. Bigger bundles always means fewer of them, and smaller bundles more.",
             ["Eq(Rational(30, 5), 6)", "Eq(5*6, 30)",
              "Eq(Rational(30, 10), 3)", "Eq(2*3, 6)"]), fig_pr5),
        prob("g3dv-pr6", "Saruul says $20 \\div 5$ and $5 \\div 20$ are both $4$. Show her the difference.",
             "$20 \\div 5 = 4$ shares a pile of twenty between five, which works out exactly: receipt $5 \\times 4 = 20$ ✓. Turning it round asks five to be shared between twenty, so nobody could get a whole thing. Multiplication turns around; division never does.",
             ["Eq(Rational(20, 5), 4)", "Eq(5*4, 20)", "20 > 5"]),
        prob("g3dv-pr7", "A shop has $40$ eggs. Give the number of boxes if they are packed $5$ to a box, then $10$ to a box. Explain the pattern.",
             "$40 \\div 5 = 8$ boxes and $40 \\div 10 = 4$ boxes. Doubling the box size halves the number of boxes, because the same forty eggs are being wrapped in bundles twice as large.",
             ["Eq(Rational(40, 5), 8)", "Eq(Rational(40, 10), 4)",
              "Eq(2*4, 8)"]),
        prob("g3dv-pr8", "\"Six shelves with $5$ jars each\" and \"$30$ jars on $6$ shelves\". Say which needs multiplying, which needs dividing, and why.",
             "The first leaves the TOTAL out, so multiply: $6 \\times 5 = 30$ jars. The second gives the total and leaves the group SIZE out, so divide: $30 \\div 6 = 5$ jars per shelf. The same three numbers, and which one is missing decides the operation.",
             ["Eq(6*5, 30)", "Eq(Rational(30, 6), 5)"]),
    ]


def test_bank():
    return [
        prob("g3dv-x1", "Share $16$ stones equally between $4$ children, and prove the answer with a receipt.",
             "$4 \\times 4 = 16$, so each child gets $4$: $16 \\div 4 = 4$. Receipt: $4 \\times 4 = 16$ ✓. Here the share and the number of sharers happen to match, which is a coincidence of this particular number.",
             ["Eq(4*4, 16)", "Eq(Rational(16, 4), 4)"]),
        prob("g3dv-x2", "How many bags of $3$ can be filled from $27$ buuz? Say whether this is sharing or grouping.",
             "It is grouping — the bag SIZE is given and the number of bags is wanted. Counting in threes to $27$ takes nine steps, so $27 \\div 3 = 9$ bags, receipt $9 \\times 3 = 27$ ✓.",
             ["Eq(9*3, 27)", "Eq(Rational(27, 3), 9)"]),
        prob("g3dv-x3", "Write the four facts for $5$, $8$ and $40$, then use one of them to find how many fives are in $40$.",
             "$5 \\times 8 = 40$, $8 \\times 5 = 40$, $40 \\div 5 = 8$ and $40 \\div 8 = 5$. The number of fives in forty is the third fact: $8$.",
             ["Eq(5*8, 40)", "Eq(Rational(40, 5), 8)",
              "Eq(Rational(40, 8), 5)"]),
        prob("g3dv-x4", "Find $32 \\div 4$ two ways: by halving twice, and by using a times fact.",
             "Halving twice: $32 \\to 16 \\to 8$. By the tables: $4 \\times 8 = 32$, so $32 \\div 4 = 8$. Both roads reach $8$, which is exactly what you would expect — the halvings are just the times fact taken in two smaller steps.",
             ["Eq(Rational(32, 2), 16)", "Eq(Rational(16, 2), 8)",
              "Eq(4*8, 32)", "Eq(Rational(32, 4), 8)"]),
        prob("g3dv-x5", "Bat answers $28 \\div 4 = 14$. Use the receipt to show he is wrong, and name his mistake.",
             "Receipt: $4 \\times 14 = 56$, which is twice $28$ — so the answer is wrong. He halved only once, and halving once divides by two, not four. The second halving gives $14 \\div 2 = 7$, and $4 \\times 7 = 28$ ✓.",
             ["Eq(4*14, 56)", "Eq(56 - 28, 28)", "Eq(Rational(28, 2), 14)",
              "Eq(Rational(14, 2), 7)", "Eq(4*7, 28)"]),
        prob("g3dv-x6", "A shop has $45$ sweets. Write one story for each of $45 \\div 5$ and $5 \\times 45$, and say which of the two answers could describe the sweets in the shop.",
             "$45 \\div 5 = 9$ is a story about the sweets themselves — nine bags of five, or nine sweets each for five children. $5 \\times 45 = 225$ is a story about five shops like this one, and it counts sweets that are not in this shop at all. Only the division describes what is on the premises, because a share can never exceed its pile.",
             ["Eq(Rational(45, 5), 9)", "Eq(5*9, 45)", "Eq(5*45, 225)",
              "225 > 45"]),
    ]


def main():
    topic = {
        "slug": "division-sharing-and-grouping",
        "title": "Division — Sharing & Grouping",
        "grade": 3,
        "status": "published",
        "blurb": ("Sharing a total into equal parts and grouping it into "
                  "bundles — the two faces of one operation — division facts "
                  "read backwards out of the times tables, dividing by 3 and "
                  "by 4, and choosing between times and divide from a story."),
        "lessons": [
            lesson_sharing(),
            lesson_grouping(),
            lesson_facts_from_tables(),
            lesson_by_three_four(),
            lesson_choosing(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "division-sharing-and-grouping.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
