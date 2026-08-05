#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Division & Sharing.

Sharing and grouping as the two faces of one division, division facts
mined from the times tables (fact families and unknown-factor thinking),
first remainders with their two-part receipts, halving and doubling as
an undo pair, and story problems where the child chooses the operation.

Through-line: DIVIDE FORWARD, MULTIPLY BACK. Every division in this
topic signs a multiplication receipt — quotient times divisor (plus the
leftover, once remainders arrive) must rebuild the starting number, and
the remainder must stay smaller than the divisor.

Grade discipline: divisors at most 10, no long division, no negative
numbers, values inside 10 000; remainders are introduced gently and
every remainder check proves r < d. Figures are built from the SAME
variables as the statements they illustrate, so text and picture cannot
disagree.

Run: python3 scripts/grade4/build_division_and_sharing.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic, withfig,
                     fig_groups, fig_numline, fig_geo, P, poly,
                     C_ACCENT, C_WARM, C_GREEN)


def lab(v):
    """A number-line label: plain text with a space separator."""
    return "{:,}".format(v).replace(",", " ")


# ==========================================================================
# Lesson 1 — Sharing & Grouping
# ==========================================================================

def lesson_sharing_grouping():
    n1, d1, q1 = 12, 3, 4
    # Sharing picture: d1 cousins, q1 buuz each.
    fig_share = fig_groups((q1, "cousin 1"), (q1, "cousin 2"), (q1, "cousin 3"))
    # Grouping picture: the same 12 buuz, bags of d1 — q1 bags.
    fig_bags = fig_groups((d1, "bag 1"), (d1, "bag 2"),
                          (d1, "bag 3"), (d1, "bag 4"))
    # Chapter-practice picture: the pile BEFORE anyone shares it. An
    # assessment figure may show the set-up, never the partition — the
    # sharing is the student's job.
    shr_n, shr_d, shr_q = 21, 7, 3
    fig_pile = fig_groups((shr_n, "togrog coins to share"))
    return {
        "slug": "sharing-and-grouping",
        "title": "Sharing & Grouping",
        "concreteComparison": (
            "$12$ buuz and $3$ cousins. Share the buuz out and each "
            "cousin gets $4$. Or pack the same $12$ buuz into bags of "
            "$3$ and you fill $4$ bags. Two different stories — "
            "sharing and grouping — but one and the same division: "
            "$12 \\div 3 = 4$."),
        "objective": (
            "Read a division two ways — share among $3$, or make "
            "groups of $3$ — say what the answer counts, and check "
            "every answer by multiplying back."),
        "concept": [
            "**One division, two stories.** $12 \\div 3$ can mean "
            "SHARE $12$ among $3$ (how many each?) or GROUP $12$ "
            "into threes (how many groups?). Different questions, "
            "same answer: $4$.",
            "**Sharing deals out; grouping peels off.** Sharing: deal "
            "one to each of the $3$ cousins until the plate is empty "
            "— $4$ rounds, so $4$ each. Grouping: peel off $3$ at a "
            "time — $4$ peels, so $4$ bags. The question tells you "
            "what the $4$ counts.",
            "**Division undoes multiplication.** $4 \\times 3 = 12$ "
            "packs four groups of three into one pile; $12 \\div 3 = "
            "4$ unpacks the pile again. So every division carries a "
            "check: multiply the answer by the divisor and the "
            "starting number must rebuild.",
        ],
        "keyIdea": (
            "One division tells two stories — share among $d$, or "
            "make groups of $d$ — and one check guards them both: "
            "divide forward, multiply back."),
        "facts": [
            {"title": "Two stories, one answer",
             "latex": "12 \\div 3 = 4 \\ \\text{each} \\quad \\text{or} \\quad 12 \\div 3 = 4 \\ \\text{groups}",
             "explanation": "Share among 3, or make groups of 3 — the same division answers both questions."},
            {"title": "Multiply back",
             "latex": "12 \\div 3 = 4 \\quad \\text{because} \\quad 4 \\times 3 = 12",
             "explanation": "Division undoes multiplication — the product must rebuild what you divided."},
        ],
        "workedExamples": [
            {"id": "g4dv-l1-we1",
             "statement": "Three cousins share $12$ buuz equally. How many does each get, and which multiplication checks the answer?",
             "note": "A sharing story: the answer counts buuz EACH.",
             "solution": ("Deal them out: $12 \\div 3 = 4$ buuz each. Multiply "
                          "back: $4 \\times 3 = 12$ ✓ — three shares of four "
                          "rebuild the whole plate."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(12,3), 4)", "Eq(4*3, 12)"]},
            {"id": "g4dv-l1-we2",
             "statement": "You have $20$ khuushuur and pack them into boxes of $5$. How many boxes do you fill?",
             "note": "A grouping story: the answer counts BOXES.",
             "solution": ("Peel off fives: $20 \\div 5 = 4$ boxes. Multiply "
                          "back: $4 \\times 5 = 20$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(20,5), 4)", "Eq(4*5, 20)"]},
        ],
        "commonMistakes": [
            {"text": "Mixing up what the answer counts — reading 12 ÷ 3 = 4 as \"4 bags\" in a sharing story.",
             "correction": "Read the question first. Shared among 3 cousins, the 4 counts buuz EACH; packed in bags of 3, the 4 counts BAGS. Same number, different meaning.",
             "authored": True},
            {"text": "Dividing the wrong way around — writing 3 ÷ 12 for \"12 shared among 3\".",
             "correction": "The pile being shared comes first: 12 ÷ 3. Twelve things split three ways is 4 each — and the receipt 4 × 3 = 12 confirms the order was right.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4dv-l1-t1",
             "statement": "Share $18$ sweets among $6$ friends. How many each? Multiply back to check.",
             "solution": "$18 \\div 6 = 3$ sweets each. Check: $3 \\times 6 = 18$ ✓.",
             "check": ["Eq(Rational(18,6), 3)", "Eq(3*6, 18)"]},
            {"id": "g4dv-l1-t2",
             "statement": "A herder ties $24$ horses in lines of $8$. How many lines?",
             "solution": "Groups of $8$: $24 \\div 8 = 3$ lines. Check: $3 \\times 8 = 24$ ✓.",
             "check": ["Eq(Rational(24,8), 3)", "Eq(3*8, 24)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One division, two stories", [
                "SHARE: $%d \\div %d$ can ask '$%d$ buuz shared among $%d$ cousins — how many EACH?' Deal them out one at a time: every cousin ends with $%d$." % (n1, d1, n1, d1, q1),
                "GROUP: the same $%d \\div %d$ can ask '$%d$ buuz packed in bags of $%d$ — how many BAGS?' Peel off $%d$ at a time: $%d$ bags." % (n1, d1, n1, d1, d1, q1),
                "Two hand movements — dealing out, peeling off — but one division and one answer: $%d \\div %d = %d$. The QUESTION tells you what the $%d$ counts." % (n1, d1, q1, q1),
            ]), fig_share),
            workedset("Two stories of one division",
                      "Say which story it is — each, or groups — before dividing.", [
                wex("Three cousins share $12$ buuz. How many each?",
                    ["Sharing story: deal $12$ out among $3$.",
                     "$12 \\div 3 = 4$ buuz each; multiply back: $4 \\times 3 = 12$ ✓."],
                    "$4$ each",
                    ["Eq(Rational(12,3), 4)", "Eq(4*3, 12)"]),
                withfig(wex("The same $12$ buuz are packed in bags of $3$. How many bags?",
                    ["Grouping story: peel off $3$ at a time.",
                     "$12 \\div 3 = 4$ bags — same division, new meaning. Receipt: $4 \\times 3 = 12$ ✓."],
                    "$4$ bags",
                    ["Eq(Rational(12,3), 4)", "Eq(4*3, 12)"]), fig_bags),
            ]),
            tryitset("Each, or groups?", "Read the story; say what the answer counts.", [
                tp("Share $20$ sweets among $4$ children. Each child gets:",
                   ["$5$ sweets", "$4$ sweets", "$16$ sweets"],
                   "Sharing: $20 \\div 4 = 5$ each, and $5 \\times 4 = 20$ rebuilds the bag ✓. $16$ took $4$ away instead of sharing four ways.",
                   ["Eq(Rational(20,4), 5)", "Eq(5*4, 20)"]),
                tp("Pack $18$ khuushuur into boxes of $6$. You fill:",
                   ["$3$ boxes", "$6$ boxes", "$12$ boxes"],
                   "Grouping: $18 \\div 6 = 3$ boxes, and $3 \\times 6 = 18$ ✓. The answer counts boxes, not khuushuur per box.",
                   ["Eq(Rational(18,6), 3)", "Eq(3*6, 18)"]),
                tp("In $15 \\div 5 = 3$ read as a SHARING story with $5$ friends, the $3$ counts:",
                   ["sweets each friend gets", "the number of friends", "sweets left over"],
                   "Shared among $5$, the answer counts how many EACH: $3$, since $3 \\times 5 = 15$ ✓. Nothing is left over — the shares come out even.",
                   ["Eq(Rational(15,5), 3)", "Eq(3*5, 15)"]),
            ]),
            tapq("Same number, two meanings", "$24 \\div 6 = 4$. Which pair of stories BOTH fit this division?",
                 ["$24$ sweets shared among $6$ children ($4$ each), or $24$ sweets in bags of $6$ ($4$ bags)",
                  "$24$ sweets shared among $4$ children, or bags of $4$",
                  "$6$ sweets shared among $24$ children",
                  "$24$ sweets with $6$ eaten"],
                 "Divide by $6$ and the $6$ plays one of two parts: number of sharers (the answer counts each) or size of each group (the answer counts groups). Either way $4 \\times 6 = 24$ rebuilds the pile ✓. Eating $6$ is subtraction — a different question entirely.",
                 ["Eq(Rational(24,6), 4)", "Eq(4*6, 24)"]),
            funfact("Card dealers divide by hand",
                    "Deal a pile of $40$ cards around a table of $4$ players, one card each in turn, and when the pile runs out every player holds exactly $10$: the dealing performed $40 \\div 4 = 10$ without anyone computing it. Sharing division is so natural that card players run it every evening — one round of the table per unit of the answer."),
            teach("Concept B", "Division undoes multiplication", [
                "$4 \\times 3 = 12$ packs four groups of three into a pile; $12 \\div 3 = 4$ unpacks the pile back into groups. Each operation undoes the other.",
                "That gives every division a built-in check: multiply the answer by the divisor and the starting number must rebuild. $12 \\div 3 = 4$, and $4 \\times 3 = 12$ ✓.",
                "This is the through-line of the whole topic: divide forward, multiply back. An answer that cannot rebuild its pile is wrong — no exceptions.",
            ]),
            workedset("Multiply back",
                      "The product must rebuild the pile.", [
                wex("Compute $30 \\div 6$ and check it.",
                    ["Six times WHAT is thirty? $6 \\times 5 = 30$, so $30 \\div 6 = 5$.",
                     "Multiply back: $5 \\times 6 = 30$ ✓."],
                    "$5$",
                    ["Eq(Rational(30,6), 5)", "Eq(5*6, 30)"]),
                wex("Dorj says $28 \\div 4 = 6$. Check his answer.",
                    ["Multiply back: $6 \\times 4 = 24$ — not $28$. The receipt fails.",
                     "The true answer is $7$: $7 \\times 4 = 28$ ✓."],
                    "$7$, not $6$",
                    ["Eq(6*4, 24)", "Ne(24, 28)", "Eq(7*4, 28)"]),
            ]),
            tryitset("Check by rebuilding", "Multiply the answer by the divisor.", [
                tp("$36 \\div 4$ equals:",
                   ["$9$", "$8$", "$32$"],
                   "$9 \\times 4 = 36$ rebuilds the pile ✓. $8 \\times 4 = 32$ falls short — and $32$ itself is what remains after taking one $4$ away, not after sharing.",
                   ["Eq(Rational(36,4), 9)", "Eq(9*4, 36)", "Eq(8*4, 32)"]),
                tp("$45 \\div 5$ equals:",
                   ["$9$", "$8$", "$40$"],
                   "$9 \\times 5 = 45$ ✓. $8 \\times 5 = 40$ misses the pile by one five.",
                   ["Eq(Rational(45,5), 9)", "Eq(9*5, 45)", "Eq(8*5, 40)"]),
                tp("Which multiplication CHECKS $32 \\div 8 = 4$?",
                   ["$4 \\times 8 = 32$", "$32 \\times 8$", "$4 \\times 4 = 16$"],
                   "Answer times divisor must rebuild the start: $4 \\times 8 = 32$ ✓. Multiplying the pile itself, or the answer by itself, rebuilds nothing.",
                   ["Eq(4*8, 32)", "Eq(Rational(32,8), 4)"]),
            ]),
            tapq("The receipt catches it", "Suvdaa computes $54 \\div 6 = 8$. What does multiplying back say?",
                 ["$8 \\times 6 = 48$, not $54$ — the answer is wrong; $54 \\div 6 = 9$",
                  "$8 \\times 6 = 54$ — the answer is right",
                  "multiplying back cannot check a division",
                  "only the teacher can check it"],
                 "Multiply back: $8 \\times 6 = 48$, and $48$ is not $54$ — the receipt fails on the spot. $9$ passes: $9 \\times 6 = 54$ ✓.",
                 ["Eq(8*6, 48)", "Ne(48, 54)", "Eq(9*6, 54)"]),
            recap([
                "One division, two stories: share among d (how many each) or group by d (how many groups).",
                "Sharing deals out one at a time; grouping peels off d at a time.",
                "The question tells you what the answer counts — each, or groups.",
                "Division undoes multiplication: divide forward, multiply back.",
                "An answer that cannot rebuild its pile is wrong.",
            ]),
            tip("Before dividing, say which story it is — 'how many each' or 'how many groups'. After dividing, multiply back and watch the pile rebuild."),
            tryitset("Mixed practice", "Both stories, every answer multiplied back.", [
                withfig(tp("Share $%d$ togrog coins among $%d$ children. Each child gets:" % (shr_n, shr_d),
                   ["$%d$ coins" % shr_q, "$%d$ coins" % shr_d, "$%d$ coins" % (shr_n - shr_d)],
                   "$%d \\div %d = %d$ each, and $%d \\times %d = %d$ ✓. $%d$ took $%d$ coins away — subtraction wearing a division costume." % (
                       shr_n, shr_d, shr_q, shr_q, shr_d, shr_n, shr_n - shr_d, shr_d),
                   ["Eq(Rational(%d,%d), %d)" % (shr_n, shr_d, shr_q),
                    "Eq(%d*%d, %d)" % (shr_q, shr_d, shr_n)]), fig_pile),
                tp("A camp sets out $27$ beds, $3$ to a ger. Gers needed:",
                   ["$9$", "$8$", "$24$"],
                   "Groups of $3$ from a total of $27$: $27 \\div 3 = 9$ gers, and $9 \\times 3 = 27$ ✓.",
                   ["Eq(Rational(27,3), 9)", "Eq(9*3, 27)"]),
                tp("$48 \\div 6$ equals:",
                   ["$8$", "$7$", "$9$"],
                   "$8 \\times 6 = 48$ ✓. The neighbours miss: $7 \\times 6 = 42$ and $9 \\times 6 = 54$.",
                   ["Eq(Rational(48,6), 8)", "Eq(8*6, 48)", "Eq(7*6, 42)", "Eq(9*6, 54)"]),
                tp("Which story fits $35 \\div 7 = 5$ read as a GROUPING story?",
                   ["$35$ sheep penned in groups of $7$ fill $5$ pens",
                    "$35$ sheep shared among $5$ herders",
                    "$35$ sheep with $7$ sold at market"],
                   "Grouping by $7$: the answer counts groups — $5$ pens of $7$, and $5 \\times 7 = 35$ ✓. Sharing among $5$ herders is the OTHER story of a different division; selling $7$ is subtraction.",
                   ["Eq(Rational(35,7), 5)", "Eq(5*7, 35)"]),
                tp("Bolor says $63 \\div 7 = 8$. The multiply-back check shows:",
                   ["$8 \\times 7 = 56$ — wrong; the answer is $9$",
                    "$8 \\times 7 = 63$ — right",
                    "the check cannot decide"],
                   "$8 \\times 7 = 56$, and $56$ is not $63$: the receipt fails. $9 \\times 7 = 63$ ✓ signs cleanly.",
                   ["Eq(8*7, 56)", "Ne(56, 63)", "Eq(9*7, 63)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Sharing & Grouping\"",
                    "Two stories, one division, and the multiply-back check that guards them both. Next: how every times-table fact you already own quietly hands you two division facts for free.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Division Facts
# ==========================================================================

def lesson_division_facts():
    fa, fb, fp = 6, 7, 42
    fig_family = fig_geo(
        [P("T", 5, 8.3, str(fp)),
         P("L", 1.7, 1.7, str(fa)),
         P("R", 8.3, 1.7, str(fb))],
        poly(["T", "L", "R"], color=C_ACCENT),
        height=190)
    # Unknown-factor picture: jumps of fa from 0 land on fp after fb jumps.
    fig_jumps = fig_numline(
        [(fa * i, str(fa * i)) for i in range(fb)] + [(fp, str(fp), C_GREEN)],
        lo=0, hi=fp)
    return {
        "slug": "division-facts",
        "title": "Division Facts",
        "concreteComparison": (
            "Learn one fact, own four: $6 \\times 7 = 42$ brings "
            "$7 \\times 6 = 42$, $42 \\div 6 = 7$ and $42 \\div 7 = "
            "6$ along with it. Picture a family photo — two small "
            "numbers, one big one on top — and four ways of reading "
            "who belongs to whom."),
        "objective": (
            "Turn every times-table fact into its two division facts, "
            "and answer divisions by unknown-factor thinking: $42 "
            "\\div 6$ asks $6 \\times \\square = 42$."),
        "concept": [
            "**Three numbers, one triangle.** $6$, $7$ and $42$ hold "
            "together: $6 \\times 7 = 42$, $7 \\times 6 = 42$, $42 "
            "\\div 6 = 7$, $42 \\div 7 = 6$. Two multiplications, two "
            "divisions — one fact family.",
            "**The product leads every division.** Division unpacks "
            "the pile, so it starts from the big number on top: $42 "
            "\\div 6$ and $42 \\div 7$ belong to the family; $6 \\div "
            "42$ does not.",
            "**Division asks: times what?** $42 \\div 6$ is the "
            "question $6 \\times \\square = 42$. The six times table "
            "answers it — $6 \\times 7 = 42$ — so no division table "
            "ever needs memorising. Divide forward, multiply back.",
        ],
        "keyIdea": (
            "Every times-table fact hides two division facts, and "
            "every division is a times-table question in disguise: "
            "$42 \\div 6$ asks $6 \\times \\square = 42$."),
        "facts": [
            {"title": "One family, four facts",
             "latex": "6 \\times 7 = 42 \\quad 7 \\times 6 = 42 \\quad 42 \\div 6 = 7 \\quad 42 \\div 7 = 6",
             "explanation": "The product sits on top of the triangle; the divisions start from it."},
            {"title": "Unknown-factor thinking",
             "latex": "42 \\div 6 = \\square \\ \\Leftrightarrow \\ 6 \\times \\square = 42",
             "explanation": "A division is answered by the times-table fact hiding inside it."},
        ],
        "workedExamples": [
            {"id": "g4dv-l2-we1",
             "statement": "Write the full fact family of $6$, $7$ and $42$.",
             "note": "Two multiplications, two divisions — the product leads both divisions.",
             "solution": ("$6 \\times 7 = 42$ and $7 \\times 6 = 42$; then $42 "
                          "\\div 6 = 7$ and $42 \\div 7 = 6$. One triangle of "
                          "numbers, four facts."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6*7, 42)", "Eq(7*6, 42)",
                       "Eq(Rational(42,6), 7)", "Eq(Rational(42,7), 6)"]},
            {"id": "g4dv-l2-we2",
             "statement": "Use unknown-factor thinking to find $56 \\div 8$.",
             "note": "Ask the times-table question hiding inside.",
             "solution": ("$56 \\div 8$ asks $8 \\times \\square = 56$. The "
                          "eight times table answers: $8 \\times 7 = 56$. So "
                          "$56 \\div 8 = 7$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*7, 56)", "Eq(Rational(56,8), 7)"]},
        ],
        "commonMistakes": [
            {"text": "Seating the big number wrongly — writing 6 ÷ 42 = 7 as a family fact.",
             "correction": "The product leads every division: 42 ÷ 6 = 7 and 42 ÷ 7 = 6. The big number starts the division; the small ones follow.",
             "authored": True},
            {"text": "Memorising 42 ÷ 6 and 42 ÷ 7 as two separate new facts.",
             "correction": "They are one family: both live inside 6 × 7 = 42. Learn the multiplication once and read it backwards twice — no new memorising.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4dv-l2-t1",
             "statement": "Write the fact family of $4$, $9$ and $36$.",
             "solution": "$4 \\times 9 = 36$, $9 \\times 4 = 36$, $36 \\div 4 = 9$, $36 \\div 9 = 4$.",
             "check": ["Eq(4*9, 36)", "Eq(9*4, 36)",
                       "Eq(Rational(36,4), 9)", "Eq(Rational(36,9), 4)"]},
            {"id": "g4dv-l2-t2",
             "statement": "Find $72 \\div 9$ by asking a times-table question.",
             "solution": "$9 \\times \\square = 72$; the nine times table says $9 \\times 8 = 72$, so $72 \\div 9 = 8$.",
             "check": ["Eq(9*8, 72)", "Eq(Rational(72,9), 8)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "One triangle, four facts", [
                "Put the three numbers on a triangle: the product $%d$ on top, the factors $%d$ and $%d$ below. That one triangle holds FOUR facts." % (fp, fa, fb),
                "Multiplying reads it upward — $%d \\times %d = %d$ and $%d \\times %d = %d$. Dividing reads it downward — $%d \\div %d = %d$ and $%d \\div %d = %d$." % (
                    fa, fb, fp, fb, fa, fp, fp, fa, fb, fp, fb, fa),
                "The product LEADS both divisions: they start from the $%d$ on top. Cover any corner and the other two rebuild it — that is what makes it a family." % (fp,),
            ]), fig_family),
            workedset("Reading the triangle",
                      "The product on top; divisions start from it.", [
                wex("List the family of $6$, $7$ and $42$.",
                    ["$6 \\times 7 = 42$ and $7 \\times 6 = 42$.",
                     "$42 \\div 6 = 7$ and $42 \\div 7 = 6$ — the product leads both."],
                    "four facts",
                    ["Eq(6*7, 42)", "Eq(7*6, 42)",
                     "Eq(Rational(42,6), 7)", "Eq(Rational(42,7), 6)"]),
                wex("How big is the family of $5$, $5$ and $25$?",
                    ["Both factors match, so the readings collapse: $5 \\times 5 = 25$ is its own twin.",
                     "Just two different facts: $5 \\times 5 = 25$ and $25 \\div 5 = 5$ — a square family."],
                    "two facts",
                    ["Eq(5*5, 25)", "Eq(Rational(25,5), 5)"]),
            ]),
            tryitset("Family members only", "The product leads; the factors follow.", [
                tp("Which division fact belongs to the family of $3$, $8$ and $24$?",
                   ["$24 \\div 8 = 3$", "$8 \\div 3 = 24$", "$24 \\div 3 = 6$"],
                   "The product $24$ leads: $24 \\div 8 = 3$, receipted by $3 \\times 8 = 24$ ✓. And $24 \\div 3$ is $8$, not $6$ — the third option smuggles in a stranger.",
                   ["Eq(3*8, 24)", "Eq(Rational(24,8), 3)", "Eq(Rational(24,3), 8)"]),
                tp("The fact family of $7$, $9$ and $63$ contains how many DIFFERENT facts?",
                   ["$4$", "$2$", "$1$"],
                   "Two multiplications and two divisions: $7 \\times 9 = 63$, $9 \\times 7 = 63$, $63 \\div 7 = 9$, $63 \\div 9 = 7$. Only square families like $5, 5, 25$ shrink to two.",
                   ["Eq(7*9, 63)", "Eq(Rational(63,7), 9)", "Eq(Rational(63,9), 7)"]),
                tp("$54 \\div 9$ equals:",
                   ["$6$", "$7$", "$5$"],
                   "It lives in the family of $6 \\times 9 = 54$: so $54 \\div 9 = 6$. One row up, $7 \\times 9 = 63$ overshoots the pile.",
                   ["Eq(6*9, 54)", "Eq(Rational(54,9), 6)", "Eq(7*9, 63)"]),
            ]),
            tapq("Who sits on top?", "In the fact family of $8$, $6$ and $48$, every DIVISION fact starts with:",
                 ["$48$ — the product leads",
                  "$8$ — the bigger factor",
                  "$6$ — the smaller factor",
                  "any of the three numbers"],
                 "Division unpacks the product, so it starts from the top of the triangle: $48 \\div 8 = 6$ and $48 \\div 6 = 8$. A division starting from a factor asks a question this family cannot answer.",
                 ["Eq(8*6, 48)", "Eq(Rational(48,8), 6)", "Eq(Rational(48,6), 8)"]),
            funfact("The times table is half the size it looks",
                    "Because $6 \\times 7$ and $7 \\times 6$ always agree, the ten-by-ten times table mirrors itself across its diagonal — learn one half and the other half comes free. Better still, every fact inside it hides two division facts, so the one table you memorise quietly answers the division questions too."),
            withfig(teach("Concept B", "Division asks: times what?", [
                "$%d \\div %d$ is not a new kind of question. It asks $%d \\times \\square = %d$. Run the six times table until it lands — $%d \\times %d = %d$ — and the answer is $%d$." % (fp, fa, fa, fp, fa, fb, fp, fb),
                "The number line shows the same hunt: jumps of $%d$ starting at $0$ reach $%d$ in exactly $%d$ jumps. Counting the jumps IS the division." % (fa, fp, fb),
                "So there is no division table to memorise. Every division with a divisor up to $10$ is a times-table fact read backwards: divide forward, multiply back.",
            ]), fig_jumps),
            workedset("Times what?",
                      "Ask the times-table question; the answer drops out.", [
                wex("Find $56 \\div 8$.",
                    ["Ask: $8 \\times \\square = 56$. The table says $8 \\times 7 = 56$.",
                     "So $56 \\div 8 = 7$ — and the same fact is the receipt."],
                    "$7$",
                    ["Eq(8*7, 56)", "Eq(Rational(56,8), 7)"]),
                wex("Find $81 \\div 9$.",
                    ["Ask: $9 \\times \\square = 81$; the table says $9 \\times 9 = 81$.",
                     "So $81 \\div 9 = 9$ — a square family, both factors equal."],
                    "$9$",
                    ["Eq(9*9, 81)", "Eq(Rational(81,9), 9)"]),
            ]),
            tryitset("The hidden question", "Say the times-table question out loud first.", [
                tp("$63 \\div 7$ equals:",
                   ["$9$", "$8$", "$7$"],
                   "$7 \\times 9 = 63$ ✓. One row down, $7 \\times 8 = 56$ falls short of the pile.",
                   ["Eq(7*9, 63)", "Eq(Rational(63,7), 9)", "Eq(7*8, 56)"]),
                tp("$40 \\div 5$ asks which times-table question?",
                   ["$5 \\times \\square = 40$", "$40 \\times \\square = 5$", "$5 \\times 40 = \\square$"],
                   "Division hunts the missing factor: $5 \\times \\square = 40$, and $5 \\times 8 = 40$ hands over the $8$.",
                   ["Eq(5*8, 40)", "Eq(Rational(40,5), 8)"]),
                tp("$100 \\div 10$ equals:",
                   ["$10$", "$100$", "$1$"],
                   "$10 \\times 10 = 100$ — the biggest square family in the table. So $100 \\div 10 = 10$.",
                   ["Eq(10*10, 100)", "Eq(Rational(100,10), 10)"]),
            ]),
            tapq("No new table needed", "To find $72 \\div 8$, the fastest honest route is:",
                 ["ask $8 \\times \\square = 72$ and read off $9$",
                  "count down from $72$ by ones",
                  "memorise a separate division table",
                  "measure it with a ruler"],
                 "Unknown-factor thinking: $8 \\times 9 = 72$, so $72 \\div 8 = 9$ — the times table you already own, read backwards. Counting down by ones gets there eventually; the table gets there now.",
                 ["Eq(8*9, 72)", "Eq(Rational(72,8), 9)"]),
            recap([
                "Three numbers, one triangle: two multiplications and two divisions.",
                "The product sits on top and leads every division fact.",
                "Square families like 5, 5, 25 hold just two different facts.",
                "A division is a times-table question: 42 ÷ 6 asks 6 × what = 42.",
                "No division table exists to learn — divide forward, multiply back.",
            ]),
            tip("For every division below, say the hidden multiplication out loud — 'six times WHAT is fifty-four?' — then multiply back to seal the answer."),
            tryitset("Mixed practice", "Families and hidden questions together.", [
                tp("$49 \\div 7$ equals:",
                   ["$7$", "$8$", "$6$"],
                   "$7 \\times 7 = 49$ — a square family, so the quotient repeats the divisor: $7$.",
                   ["Eq(7*7, 49)", "Eq(Rational(49,7), 7)"]),
                tp("Which fact does NOT belong to the family of $4$, $8$ and $32$?",
                   ["$32 \\div 4 = 6$", "$4 \\times 8 = 32$", "$32 \\div 8 = 4$"],
                   "$32 \\div 4 = 8$, not $6$ — the claim fails its multiply-back, since $6 \\times 4 = 24$. The other two are genuine family members.",
                   ["Eq(Rational(32,4), 8)", "Eq(6*4, 24)", "Ne(24, 32)", "Eq(4*8, 32)"]),
                tp("$60 \\div 6$ equals:",
                   ["$10$", "$6$", "$12$"],
                   "$6 \\times 10 = 60$ ✓ — dividing by $6$ undoes multiplying by $6$.",
                   ["Eq(6*10, 60)", "Eq(Rational(60,6), 10)"]),
                tp("A family contains $9 \\times 4 = 36$. Its two division facts are:",
                   ["$36 \\div 9 = 4$ and $36 \\div 4 = 9$",
                    "$9 \\div 4$ and $4 \\div 9$",
                    "$36 \\div 6 = 6$ and $36 \\div 3 = 12$"],
                   "The product $36$ leads both: $36 \\div 9 = 4$ and $36 \\div 4 = 9$. The facts about $6$ and $3$ are true of OTHER families — this triangle holds only $9$, $4$ and $36$.",
                   ["Eq(9*4, 36)", "Eq(Rational(36,9), 4)", "Eq(Rational(36,4), 9)"]),
                tp("Sarnai knows $8 \\times 6 = 48$ but has forgotten $48 \\div 6$. She should:",
                   ["read her known fact backwards: $48 \\div 6 = 8$",
                    "start subtracting sixes from $48$ one by one",
                    "give up until she learns a division table"],
                   "The division lives inside the multiplication she owns: $8 \\times 6 = 48$ means $48 \\div 6 = 8$, no new work. Subtracting sixes also lands on eight rounds — the slow road to the same place.",
                   ["Eq(8*6, 48)", "Eq(Rational(48,6), 8)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Division Facts\"",
                    "One triangle, four facts, and the hidden question 'times what?' — the entire times table, now working double shifts. Next: what happens when the sharing refuses to come out even.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Remainders
# ==========================================================================

def lesson_remainders():
    rn, rd, rq, rr = 23, 5, 4, 3
    # Sharing 23 among 5: five shares of 4, and 3 left over.
    # Colour carries the meaning here: every FULL share is the same blue
    # (equal shares look equal), and the leftover keeps the topic's
    # reserved warm colour, used for no share anywhere in the topic.
    fig_left = fig_groups(
        *([(rq, "friend %d" % (i + 1), C_ACCENT) for i in range(rd)]
          + [(rr, "left over", C_WARM)]))
    # The gap picture: 23 sits between 4 fives and 5 fives.
    fig_gap = fig_numline(
        [(rq * rd, "%d fives" % rq), (rn, str(rn), C_WARM),
         ((rq + 1) * rd, "%d fives" % (rq + 1))],
        lo=0, hi=(rq + 1) * rd)
    return {
        "slug": "remainders",
        "title": "Remainders",
        "concreteComparison": (
            "You share $23$ aaruul among $5$ friends: four each, and "
            "$3$ pieces stay in your palm. The leftover has a name — "
            "the REMAINDER — and a rule: it must be too small to "
            "share another round. The receipt proves both parts: "
            "$4 \\times 5 + 3 = 23$, and $3 < 5$."),
        "objective": (
            "Divide with leftovers, write the answer as quotient and "
            "remainder, and sign the two-part receipt every time: "
            "quotient times divisor plus remainder rebuilds the "
            "start, and the remainder stays smaller than the "
            "divisor."),
        "concept": [
            "**Sometimes the shares refuse to come out even.** $23 "
            "\\div 5$: four each uses $20$, and $3$ are left — too "
            "few for a fifth-for-everyone round. We write $23 \\div 5 "
            "= 4$ r $3$: quotient $4$, remainder $3$.",
            "**The remainder is always smaller than the divisor.** If "
            "$5$ or more were left, every friend could take one more "
            "— the sharing stopped too early. The rule is $r < d$, "
            "checked every single time.",
            "**The receipt grows a new term.** Quotient times divisor "
            "PLUS remainder rebuilds the start: $4 \\times 5 + 3 = "
            "23$. Multiply back and add the leftover — both parts, "
            "every time. Divide forward, multiply back.",
        ],
        "keyIdea": (
            "A remainder is what sharing leaves behind — always "
            "smaller than the divisor — and the receipt has two "
            "parts: $q \\times d + r$ rebuilds the start, and "
            "$r < d$."),
        "facts": [
            {"title": "Quotient and remainder",
             "latex": "23 \\div 5 = 4 \\ \\text{r} \\ 3",
             "explanation": "Four full shares, three left over — too few for another round."},
            {"title": "The two-part receipt",
             "latex": "4 \\times 5 + 3 = 23 \\quad \\text{and} \\quad 3 < 5",
             "explanation": "Rebuild the start, and confirm the leftover is smaller than the divisor."},
        ],
        "workedExamples": [
            {"id": "g4dv-l3-we1",
             "statement": "Share $23$ aaruul among $5$ friends. How many each, how many left over? Sign the receipt.",
             "note": "Find the biggest times-table fact that still fits.",
             "solution": ("$5 \\times 4 = 20$ fits inside $23$; $5 \\times 5 = "
                          "25$ is too much. So $4$ each with $3$ left: $23 \\div "
                          "5 = 4$ r $3$. Receipt: $4 \\times 5 + 3 = 23$ ✓ and "
                          "$3 < 5$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*4, 20)", "Eq(5*5, 25)",
                       "Eq(4*5 + 3, 23)", "3 < 5"]},
            {"id": "g4dv-l3-we2",
             "statement": "$50$ khuushuur are packed in boxes of $8$. How many full boxes, and how many are left?",
             "note": "A grouping story with a leftover.",
             "solution": ("$8 \\times 6 = 48$ fits inside $50$; $8 \\times 7 = "
                          "56$ is too much. So $6$ full boxes and $2$ left: $50 "
                          "\\div 8 = 6$ r $2$. Receipt: $6 \\times 8 + 2 = 50$ "
                          "✓ and $2 < 8$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*6, 48)", "Eq(8*7, 56)",
                       "Eq(6*8 + 2, 50)", "2 < 8"]},
        ],
        "commonMistakes": [
            {"text": "Stopping the sharing too early — answering 23 ÷ 5 = 3 r 8.",
             "correction": "Eight leftovers still hold a full round: one more each makes 4 r 3. Sharing stops only when the leftover is SMALLER than the divisor — always check r < d.",
             "authored": True},
            {"text": "Dropping the remainder from the receipt — checking 23 ÷ 5 = 4 r 3 with 4 × 5 = 20 and stopping.",
             "correction": "20 is not 23. The receipt has two terms now: 4 × 5 + 3 = 23. Multiply back, then add the leftover.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4dv-l3-t1",
             "statement": "Compute $34 \\div 4$ with its remainder, and sign the receipt.",
             "solution": "$4 \\times 8 = 32$ fits; $2$ are left. $34 \\div 4 = 8$ r $2$. Receipt: $8 \\times 4 + 2 = 34$ ✓ and $2 < 4$ ✓.",
             "check": ["Eq(4*8, 32)", "Eq(8*4 + 2, 34)", "2 < 4"]},
            {"id": "g4dv-l3-t2",
             "statement": "$29$ sweets are packed in bags of $9$. How many full bags, and how many sweets are left?",
             "solution": "$3 \\times 9 = 27$ fits: $3$ full bags, $2$ sweets left. Receipt: $3 \\times 9 + 2 = 29$ ✓ and $2 < 9$ ✓.",
             "check": ["Eq(3*9, 27)", "Eq(3*9 + 2, 29)", "2 < 9"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "When shares refuse to come out even", [
                "Share $%d$ aaruul among $%d$ friends: after $%d$ rounds each friend holds $%d$, the pile holds $%d$ — too few for another round for everyone." % (rn, rd, rq, rq, rr),
                "We write $%d \\div %d = %d$ r $%d$: the QUOTIENT $%d$ counts full shares, the REMAINDER $%d$ counts what stayed behind." % (rn, rd, rq, rr, rq, rr),
                "The receipt grows a term: $%d \\times %d + %d = %d$ ✓. Multiply back AND add the leftover — the pile must rebuild exactly." % (rq, rd, rr, rn),
            ]), fig_left),
            workedset("First remainders",
                      "Find the biggest times-table fact that fits; the leftover is the remainder.", [
                wex("Compute $23 \\div 5$.",
                    ["$5 \\times 4 = 20$ fits; $5 \\times 5 = 25$ is too much: quotient $4$, remainder $3$.",
                     "Receipt: $4 \\times 5 + 3 = 23$ ✓ and $3 < 5$ ✓."],
                    "$4$ r $3$",
                    ["Eq(4*5 + 3, 23)", "3 < 5", "Eq(5*5, 25)"]),
                wex("Compute $50 \\div 8$.",
                    ["$8 \\times 6 = 48$ fits; $8 \\times 7 = 56$ is too much: quotient $6$, remainder $2$.",
                     "Receipt: $6 \\times 8 + 2 = 50$ ✓ and $2 < 8$ ✓."],
                    "$6$ r $2$",
                    ["Eq(6*8 + 2, 50)", "2 < 8", "Eq(8*7, 56)"]),
            ]),
            tryitset("Quotient and leftover", "The receipt has two parts — use both.", [
                tp("$17 \\div 3$ equals:",
                   ["$5$ r $2$", "$5$ r $3$", "$6$ r $1$"],
                   "$3 \\times 5 = 15$, leaving $2$: receipt $5 \\times 3 + 2 = 17$ ✓ and $2 < 3$ ✓. A remainder of $3$ would allow another round, and $6 \\times 3 = 18$ overshoots the pile.",
                   ["Eq(5*3 + 2, 17)", "2 < 3", "Eq(6*3, 18)"]),
                tp("$26 \\div 4$ equals:",
                   ["$6$ r $2$", "$5$ r $6$", "$6$ r $4$"],
                   "$4 \\times 6 = 24$, leaving $2$: receipt $6 \\times 4 + 2 = 26$ ✓ and $2 < 4$ ✓. In $5$ r $6$, six leftovers still share a whole round.",
                   ["Eq(6*4 + 2, 26)", "2 < 4", "6 > 4"]),
                tp("$40 \\div 6$ equals:",
                   ["$6$ r $4$", "$7$ r $2$", "$6$ r $6$"],
                   "$6 \\times 6 = 36$, leaving $4$: receipt $6 \\times 6 + 4 = 40$ ✓ and $4 < 6$ ✓. $7 \\times 6 = 42$ overshoots the pile.",
                   ["Eq(6*6 + 4, 40)", "4 < 6", "Eq(7*6, 42)"]),
            ]),
            tapq("Two answers rebuild — one is right", "For $23 \\div 5$, both $4$ r $3$ and $3$ r $8$ rebuild the pile. Which is correct, and why?",
                 ["$4$ r $3$ — a remainder must be smaller than the divisor, and $8 > 5$",
                  "$3$ r $8$ — bigger remainders are safer",
                  "both answers are correct",
                  "neither answer is correct"],
                 "$3 \\times 5 + 8 = 23$ really does rebuild the pile — but $8$ leftovers still hold a full round of sharing. The remainder rule breaks the tie: $r < d$, and only $3 < 5$ obeys it. So $4$ r $3$ is the one honest answer.",
                 ["Eq(3*5 + 8, 23)", "Eq(4*5 + 3, 23)", "8 > 5", "3 < 5"]),
            funfact("The year's leftover day",
                    "An ordinary year has $365$ days, and $365 \\div 7 = 52$ r $1$: fifty-two full weeks and one day left over. That single leftover day is why your birthday lands one weekday later each ordinary year — the remainder does the sliding."),
            withfig(teach("Concept B", "The leftover rule, on a line", [
                "On the number line, jumps of $%d$ reach $%d$ after $%d$ jumps; the next jump lands on $%d$ — past the pile. The pile sits at $%d$, in the gap." % (rd, rq * rd, rq, (rq + 1) * rd, rn),
                "The remainder is the distance past the last full jump: $%d$. It can never reach a full jump — if it did, you would simply jump again. That is the rule $r < d$, drawn." % (rr,),
                "Remainder stories ask about the leftover itself: share $%d$ among $%d$ and the question 'how many stay in the bag?' is answered by the remainder, $%d$." % (rn, rd, rr),
            ]), fig_gap),
            workedset("Remainder stories",
                      "Some questions want the quotient, some want the leftover.", [
                wex("$38$ sweets are shared among $9$ children. How many sweets are LEFT OVER?",
                    ["$9 \\times 4 = 36$ fits inside $38$, and $2$ remain.",
                     "Answer: $2$ left over. Receipt: $4 \\times 9 + 2 = 38$ ✓ and $2 < 9$ ✓."],
                    "$2$ sweets",
                    ["Eq(9*4, 36)", "Eq(4*9 + 2, 38)", "2 < 9"]),
                wex("$52$ horses graze in herds of $10$. How many FULL herds?",
                    ["$10 \\times 5 = 50$ fits, and $2$ horses stay outside the herds.",
                     "Answer: $5$ full herds. Receipt: $5 \\times 10 + 2 = 52$ ✓ and $2 < 10$ ✓."],
                    "$5$ herds",
                    ["Eq(5*10 + 2, 52)", "2 < 10"]),
            ]),
            tryitset("Read the question twice", "Quotient, or remainder — the story decides.", [
                tp("$44$ buuz are steamed on trays of $8$. Full trays:",
                   ["$5$", "$4$", "$6$"],
                   "$8 \\times 5 = 40$ fits, $8 \\times 6 = 48$ is too many: $5$ full trays with $4$ buuz over. Receipt: $5 \\times 8 + 4 = 44$ ✓ and $4 < 8$ ✓.",
                   ["Eq(5*8 + 4, 44)", "4 < 8", "Eq(8*6, 48)"]),
                tp("$31$ togrog coins are shared among $4$ children. Coins LEFT OVER:",
                   ["$3$", "$7$", "$0$"],
                   "$4 \\times 7 = 28$ fits, and $3$ remain with $3 < 4$ — the sharing truly stopped. Receipt: $7 \\times 4 + 3 = 31$ ✓. The $7$ is the quotient; the question asked for the leftover.",
                   ["Eq(4*7, 28)", "Eq(7*4 + 3, 31)", "3 < 4"]),
                tp("Which remainder is IMPOSSIBLE when dividing by $6$?",
                   ["$6$", "$5$", "$0$"],
                   "Remainders when dividing by $6$ run from $0$ up to $5$. A leftover of $6$ is a full group — the sharing owes one more round. And $0$ simply means the shares came out even.",
                   ["Not(6 < 6)", "5 < 6", "0 < 6"]),
            ]),
            tapq("Each, and left over", "$60$ sweets are shared among $7$ children. How many does each child get, and how many are left?",
                 ["$8$ each and $4$ left",
                  "$4$ each and $8$ left",
                  "$8$ each and $8$ left",
                  "$7$ each and $4$ left"],
                 "$7 \\times 8 = 56$ fits inside $60$, leaving $4$: quotient $8$ (each), remainder $4$ (left). Receipt: $8 \\times 7 + 4 = 60$ ✓ and $4 < 7$ ✓.",
                 ["Eq(7*8, 56)", "Eq(8*7 + 4, 60)", "4 < 7"]),
            recap([
                "When shares refuse to come out even, the leftover is the remainder.",
                "The remainder is always smaller than the divisor — otherwise share another round.",
                "The receipt has two terms: quotient × divisor + remainder = start.",
                "Rebuilding alone is not enough — r < d breaks the tie.",
                "Read the question twice: some ask for the shares, some for the leftover.",
            ]),
            tip("Write the receipt for every answer below — quotient times divisor, plus remainder — and say both checks aloud: 'rebuilds the pile' and 'leftover smaller than the divisor'."),
            tryitset("Mixed practice", "Quotients, remainders, and two-part receipts.", [
                tp("$25 \\div 7$ equals:",
                   ["$3$ r $4$", "$3$ r $5$", "$4$ r $3$"],
                   "$7 \\times 3 = 21$, leaving $4$: receipt $3 \\times 7 + 4 = 25$ ✓ and $4 < 7$ ✓. $4 \\times 7 = 28$ overshoots the pile.",
                   ["Eq(3*7 + 4, 25)", "4 < 7", "Eq(4*7, 28)"]),
                tp("$58 \\div 6$ equals:",
                   ["$9$ r $4$", "$8$ r $10$", "$9$ r $6$"],
                   "$6 \\times 9 = 54$, leaving $4$: receipt $9 \\times 6 + 4 = 58$ ✓ and $4 < 6$ ✓. Leftovers of $10$ or $6$ still hold full rounds.",
                   ["Eq(9*6 + 4, 58)", "4 < 6", "10 > 6"]),
                tp("$70$ aaruul dry on racks of $9$. Full racks, and pieces over:",
                   ["$7$ racks, $7$ over", "$7$ racks, $2$ over", "$8$ racks, $2$ over"],
                   "$9 \\times 7 = 63$ fits, $9 \\times 8 = 72$ is too many: $7$ racks and $7$ over. Receipt: $7 \\times 9 + 7 = 70$ ✓ and $7 < 9$ ✓.",
                   ["Eq(7*9 + 7, 70)", "7 < 9", "Eq(9*8, 72)"]),
                tp("A $33$-page story is read $10$ pages at a sitting. After $3$ full sittings, pages left:",
                   ["$3$", "$10$", "$0$"],
                   "$3 \\times 10 = 30$ pages read; the remainder is $3$, and $3 < 10$. Receipt: $3 \\times 10 + 3 = 33$ ✓.",
                   ["Eq(3*10 + 3, 33)", "3 < 10"]),
                tp("Which is a CORRECTLY finished division?",
                   ["$29 \\div 4 = 7$ r $1$", "$29 \\div 4 = 6$ r $5$", "$29 \\div 4 = 7$ r $4$"],
                   "$7 \\times 4 + 1 = 29$ ✓ and $1 < 4$ ✓. The second rebuilds too ($6 \\times 4 + 5 = 29$) but $5 > 4$ — a round of sharing is still owed. The third does not rebuild at all: $7 \\times 4 + 4 = 32$.",
                   ["Eq(7*4 + 1, 29)", "1 < 4", "Eq(6*4 + 5, 29)", "5 > 4",
                    "Eq(7*4 + 4, 32)", "Ne(32, 29)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Remainders\"",
                    "Leftovers named, the rule r < d, and a receipt that grew a second term. Next: the friendliest division of all — splitting into two — and the doubling that undoes it.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Halving & Doubling
# ==========================================================================

def lesson_halving_doubling():
    dbl = 6                      # double 6 = two sixes
    fig_double = fig_groups((dbl, "one six", C_ACCENT),
                            (dbl, "another six", C_WARM))
    hn, hh = 4800, 2400          # halving demo: half of 4800
    fig_halfline = fig_numline(
        [(0, "0"), (hh, lab(hh), C_GREEN), (hn, lab(hn))],
        lo=0, hi=hn)
    return {
        "slug": "halving-and-doubling",
        "title": "Halving & Doubling",
        "concreteComparison": (
            "Fold a rope of $8$ metres in half: each part is $4$ "
            "metres. Unfold it: $8$ again. Halving and doubling are "
            "that fold and unfold — $\\div \\, 2$ and $\\times \\, 2$ "
            "— and each undoes the other, so every half can be "
            "checked by doubling it straight back."),
        "objective": (
            "Halve as dividing by $2$ and double as multiplying by "
            "$2$, use each to check the other, and halve even "
            "numbers up to $10\\,000$ by splitting them into "
            "friendly parts."),
        "concept": [
            "**Doubling multiplies by two; halving divides by two.** "
            "Double $6$ is $6 + 6 = 12$, which is $2 \\times 6$. "
            "Half of $12$ is the sharing division $12 \\div 2 = 6$ "
            "— two equal shares, take one.",
            "**They undo each other.** Double $7$ to get $14$; halve "
            "$14$ and the $7$ walks straight back. So doubling is "
            "the CHECK for every halving, and halving checks every "
            "doubling — divide forward, multiply back, with $2$ in "
            "the divisor's seat.",
            "**Halve big numbers place by place.** $4\\,800 = "
            "4\\,000 + 800$, so half is $2\\,000 + 400 = 2\\,400$. "
            "When a digit is odd, split differently: $76 = 60 + 16$, "
            "so half is $30 + 8 = 38$. The doubling check scales up "
            "with you: $2 \\times 2\\,400 = 4\\,800$ ✓.",
        ],
        "keyIdea": (
            "Halving is dividing by 2 and doubling is multiplying by "
            "2; they undo each other, so the unfold — doubling the "
            "half — must always rebuild the exact start."),
        "facts": [
            {"title": "Fold and unfold",
             "latex": "14 \\div 2 = 7 \\quad \\text{and} \\quad 2 \\times 7 = 14",
             "explanation": "Halving undoes doubling — doubling the half must rebuild the whole."},
            {"title": "Halve place by place",
             "latex": "4\\,800 \\div 2 = 2\\,400",
             "explanation": "Half of 4 thousands is 2 thousands; half of 8 hundreds is 4 hundreds."},
        ],
        "workedExamples": [
            {"id": "g4dv-l4-we1",
             "statement": "Halve $18$, then check by doubling.",
             "note": "Half means two equal shares — take one.",
             "solution": ("$18 \\div 2 = 9$, since $9 + 9 = 18$. Double back: "
                          "$2 \\times 9 = 18$ ✓ — the fold unfolds exactly."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(18,2), 9)", "Eq(9 + 9, 18)", "Eq(2*9, 18)"]},
            {"id": "g4dv-l4-we2",
             "statement": "Halve $4\\,800$ and check by doubling.",
             "note": "Split into thousands and hundreds; halve each part.",
             "solution": ("Place by place: half of $4\\,000$ is $2\\,000$, half "
                          "of $800$ is $400$ — together $2\\,400$. Double back: "
                          "$2 \\times 2\\,400 = 4\\,800$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(4000,2), 2000)", "Eq(Rational(800,2), 400)",
                       "Eq(2*2400, 4800)"]},
        ],
        "commonMistakes": [
            {"text": "Halving digit by digit and jamming on an odd one — trying \"half of 7, half of 6\" for 76.",
             "correction": "Split into friendly EVEN parts first: 76 = 60 + 16, so half is 30 + 8 = 38. Double back: 2 × 38 = 76 ✓.",
             "authored": True},
            {"text": "Doubling to check but never comparing — doubling the half and moving on without looking.",
             "correction": "The doubled half must rebuild the EXACT starting number: halve 4 800 to 2 400, double to 4 800, match confirmed. No match, no answer.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4dv-l4-t1",
             "statement": "Halve $64$ and check by doubling.",
             "solution": "$64 = 60 + 4$: half is $30 + 2 = 32$. Check: $2 \\times 32 = 64$ ✓.",
             "check": ["Eq(Rational(64,2), 32)", "Eq(2*32, 64)"]},
            {"id": "g4dv-l4-t2",
             "statement": "Double $370$, then halve your answer. What comes back?",
             "solution": "$2 \\times 370 = 740$; then $740 \\div 2 = 370$ — the starting number, because halving undoes doubling.",
             "check": ["Eq(2*370, 740)", "Eq(Rational(740,2), 370)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The fold and the unfold", [
                "DOUBLE means two of the same: double $%d$ is $%d + %d = %d$, which is $2 \\times %d$." % (dbl, dbl, dbl, 2 * dbl, dbl),
                "HALVE means split into two equal shares and take one: half of $%d$ is $%d \\div 2 = %d$ — a sharing division with $2$ in the divisor's seat." % (2 * dbl, 2 * dbl, dbl),
                "Each undoes the other: double $7$ to get $14$, halve $14$ and the $7$ walks back. So every half is checked by its double — divide forward, multiply back.",
            ]), fig_double),
            workedset("Halve and prove it",
                      "Every half is checked by its double.", [
                wex("Halve $18$.",
                    ["$18 \\div 2 = 9$, since $9 + 9 = 18$.",
                     "Double back: $2 \\times 9 = 18$ ✓."],
                    "$9$",
                    ["Eq(Rational(18,2), 9)", "Eq(2*9, 18)"]),
                wex("Double $45$, then halve the result.",
                    ["$2 \\times 45 = 90$.",
                     "$90 \\div 2 = 45$ — back where we started, exactly as the undo promises."],
                    "$90$, then $45$ again",
                    ["Eq(2*45, 90)", "Eq(Rational(90,2), 45)"]),
            ]),
            tryitset("Fold, unfold", "Halve with a doubling check; double with a halving check.", [
                tp("Half of $16$ is:",
                   ["$8$", "$6$", "$32$"],
                   "$8 + 8 = 16$, and the unfold agrees: $2 \\times 8 = 16$ ✓. $32$ is the DOUBLE of $16$ — the opposite move.",
                   ["Eq(Rational(16,2), 8)", "Eq(2*8, 16)", "Eq(2*16, 32)"]),
                tp("Double $35$ is:",
                   ["$70$", "$65$", "$75$"],
                   "$2 \\times 35 = 70$, and halving back gives $70 \\div 2 = 35$ ✓.",
                   ["Eq(2*35, 70)", "Eq(Rational(70,2), 35)"]),
                tp("Half of $90$ is:",
                   ["$45$", "$40$", "$180$"],
                   "$90 = 80 + 10$: half is $40 + 5 = 45$, and $2 \\times 45 = 90$ ✓. $180$ doubled instead of halving.",
                   ["Eq(Rational(90,2), 45)", "Eq(2*45, 90)", "Eq(2*90, 180)"]),
            ]),
            tapq("Walk it back", "Naran doubles a number and gets $56$. The number was:",
                 ["$28$ — halve the $56$ to walk back",
                  "$112$ — double it again",
                  "$54$ — take $2$ away",
                  "$58$ — add $2$"],
                 "Doubling forward is undone by halving back: $56 \\div 2 = 28$, and the check runs forward again — $2 \\times 28 = 56$ ✓. Doubling again would give $112$, marching the wrong way.",
                 ["Eq(Rational(56,2), 28)", "Eq(2*28, 56)", "Eq(2*56, 112)"]),
            funfact("Ten doublings pass a thousand",
                    "Start at $1$ and double just ten times: $1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1\\,024$ — past a thousand in ten moves. And halving runs home just as fast: ten halvings bring $1\\,024$ straight back to $1$. Doubling is the fastest-growing move you own."),
            withfig(teach("Concept B", "Halving big numbers, place by place", [
                "Split into friendly parts and halve each: $%s = %s + %s$, so half is $%s + %s = %s$." % (lab(hn).replace(" ", "\\,"), "4\\,000", "800", "2\\,000", "400", lab(hh).replace(" ", "\\,")),
                "When a digit is odd, split differently: $76 = 60 + 16$ (not $70 + 6$), so half is $30 + 8 = 38$ — feed the odd ten to the ones.",
                "The doubling check scales up with you: $2 \\times 2\\,400 = 4\\,800$ ✓ and $2 \\times 38 = 76$ ✓. The unfold must rebuild the exact start, however big the number.",
            ]), fig_halfline),
            workedset("Big halves",
                      "Split into friendly parts; double to prove.", [
                wex("Halve $6\\,400$.",
                    ["$6\\,000 \\to 3\\,000$ and $400 \\to 200$.",
                     "Half: $3\\,200$. Double back: $2 \\times 3\\,200 = 6\\,400$ ✓."],
                    "$3\\,200$",
                    ["Eq(Rational(6400,2), 3200)", "Eq(2*3200, 6400)"]),
                wex("Halve $580$.",
                    ["$580 = 500 + 80$: half of $500$ is $250$, half of $80$ is $40$.",
                     "Half: $290$. Double back: $2 \\times 290 = 580$ ✓."],
                    "$290$",
                    ["Eq(Rational(580,2), 290)", "Eq(250 + 40, 290)", "Eq(2*290, 580)"]),
            ]),
            tryitset("Halve the thousands", "Friendly parts, then the doubling check.", [
                tp("Half of $8\\,400$ is:",
                   ["$4\\,200$", "$4\\,400$", "$2\\,100$"],
                   "$8\\,000 \\to 4\\,000$ and $400 \\to 200$: $4\\,200$, and $2 \\times 4\\,200 = 8\\,400$ ✓. $2\\,100$ halved TWICE — a quarter, not a half.",
                   ["Eq(Rational(8400,2), 4200)", "Eq(2*4200, 8400)", "Eq(Rational(4200,2), 2100)"]),
                tp("Half of $92$ is:",
                   ["$46$", "$41$", "$184$"],
                   "$92 = 80 + 12$: half is $40 + 6 = 46$, and $2 \\times 46 = 92$ ✓.",
                   ["Eq(Rational(92,2), 46)", "Eq(2*46, 92)"]),
                tp("Half of $7\\,000$ is:",
                   ["$3\\,500$", "$3\\,000$", "$350$"],
                   "Split the odd thousand: $7\\,000 = 6\\,000 + 1\\,000$, so half is $3\\,000 + 500 = 3\\,500$, and $2 \\times 3\\,500 = 7\\,000$ ✓.",
                   ["Eq(Rational(7000,2), 3500)", "Eq(2*3500, 7000)"]),
            ]),
            tapq("The unfold exposes it", "Bataa halves $9\\,200$ and gets $4\\,100$. The doubling check says:",
                 ["$2 \\times 4\\,100 = 8\\,200$, not $9\\,200$ — wrong; the half is $4\\,600$",
                  "$2 \\times 4\\,100 = 9\\,200$ — the half is right",
                  "doubling cannot check a halving",
                  "the check needs a remainder"],
                 "Double back: $2 \\times 4\\,100 = 8\\,200$, and the start does not rebuild. Half of $9\\,200$ is $4\\,600$ (split $8\\,000 + 1\\,200$ into $4\\,000 + 600$), and $2 \\times 4\\,600 = 9\\,200$ ✓.",
                 ["Eq(2*4100, 8200)", "Ne(8200, 9200)", "Eq(4000 + 600, 4600)",
                  "Eq(2*4600, 9200)"]),
            recap([
                "Doubling is × 2; halving is ÷ 2 — sharing between two.",
                "They undo each other: doubling the half must rebuild the exact start.",
                "Halve big numbers place by place, splitting into friendly even parts.",
                "76 halves as 60 + 16, not 70 + 6 — feed the odd ten to the ones.",
                "Check every half by doubling, and every double by halving.",
            ]),
            tip("Halve place by place, and finish every answer with its unfold — double the half, or halve the double, and watch the start come back."),
            tryitset("Mixed practice", "Folds and unfolds, small and large.", [
                tp("Half of $48$ is:",
                   ["$24$", "$28$", "$96$"],
                   "$40 + 8 \\to 20 + 4 = 24$, and $2 \\times 24 = 48$ ✓. $96$ is the double.",
                   ["Eq(Rational(48,2), 24)", "Eq(2*24, 48)", "Eq(2*48, 96)"]),
                tp("Double $2\\,750$ is:",
                   ["$5\\,500$", "$4\\,500$", "$5\\,750$"],
                   "$2\\,000 \\to 4\\,000$, $700 \\to 1\\,400$, $50 \\to 100$: together $5\\,500$, and halving back gives $2\\,750$ ✓.",
                   ["Eq(2*2750, 5500)", "Eq(Rational(5500,2), 2750)"]),
                tp("Half of $5\\,600$ is:",
                   ["$2\\,800$", "$2\\,300$", "$2\\,600$"],
                   "$5\\,600 = 4\\,000 + 1\\,600$: half is $2\\,000 + 800 = 2\\,800$, and $2 \\times 2\\,800 = 5\\,600$ ✓.",
                   ["Eq(Rational(5600,2), 2800)", "Eq(2*2800, 5600)"]),
                tp("A rope of $34$ m is folded in half. Each part measures:",
                   ["$17$ m", "$16$ m", "$68$ m"],
                   "$34 = 20 + 14$: half is $10 + 7 = 17$ m, and the unfold $2 \\times 17 = 34$ ✓. $68$ is two ropes, not half of one.",
                   ["Eq(Rational(34,2), 17)", "Eq(2*17, 34)", "Eq(2*34, 68)"]),
                tp("Half of $10\\,000$ is:",
                   ["$5\\,000$", "$1\\,000$", "$4\\,000$"],
                   "Ten thousands share into two fives: $5\\,000$, and $2 \\times 5\\,000 = 10\\,000$ ✓.",
                   ["Eq(Rational(10000,2), 5000)", "Eq(2*5000, 10000)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Halving & Doubling\"",
                    "The friendliest division and its undo — a fold and an unfold that check each other. Last stop: stories that refuse to say which operation they want, and the two words that give them away.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Multiply or Divide?
# ==========================================================================

def lesson_choosing():
    gm_g, gm_s = 4, 5            # 4 gers, 5 guests each -> 20 guests
    fig_mult = fig_groups(*[(gm_s, "ger %d" % (i + 1)) for i in range(gm_g)])
    pn, pd, pq = 18, 6, 3        # 18 goats, pens of 6 -> 3 pens
    fig_pens = fig_groups(*[(pd, "pen %d" % (i + 1)) for i in range(pq)])
    return {
        "slug": "choosing-the-operation",
        "title": "Multiply or Divide?",
        "concreteComparison": (
            "Two questions about one ger camp. '$4$ gers with $5$ "
            "guests EACH — how many guests?' joins equal groups: "
            "multiply, $20$. '$20$ guests sleep $5$ to a ger — how "
            "many gers?' splits a total: divide, $4$. Notice that "
            "'each' sits in BOTH stories, so it cannot decide for you "
            "— the real tell is the total: wanted, or given and being "
            "split?"),
        "objective": (
            "Decide whether a story multiplies or divides by finding "
            "its total — wanted, or given and being split — and "
            "receipt every answer so the story's numbers rebuild "
            "each other."),
        "concept": [
            "**Multiplying joins equal groups.** You KNOW the group "
            "size and the group count; you WANT the total. '$4$ "
            "gers of $5$ guests': $4 \\times 5 = 20$. Flag words: "
            "'altogether', 'in all'. The word 'each' turns up in "
            "dividing stories too, so it never decides on its own.",
            "**Dividing splits a given total.** You KNOW the total; "
            "you want the share or the count of groups. '$20$ "
            "guests, $5$ to a ger': $20 \\div 5 = 4$. Flag words: "
            "'shared among', 'split into', 'groups of'.",
            "**The total is the tell.** Ask one question of every "
            "story: is the total WANTED, or GIVEN and being split? "
            "Wanted: multiply. Given: divide. Then receipt the "
            "answer — the story's numbers must rebuild each other, "
            "whichever operation you chose.",
        ],
        "keyIdea": (
            "Find the total: wanted means multiply, given-and-split "
            "means divide — and either way the receipt closes the "
            "loop, because the story's numbers must rebuild each "
            "other."),
        "facts": [
            {"title": "The tell",
             "latex": "\\text{total wanted} \\to \\times \\qquad \\text{total given} \\to \\div",
             "explanation": "Multiplying builds a total from equal groups; dividing splits a given total."},
            {"title": "One receipt for both",
             "latex": "4 \\times 5 = 20 \\quad \\text{and} \\quad 20 \\div 5 = 4",
             "explanation": "The story's numbers rebuild each other — whichever operation you chose."},
        ],
        "workedExamples": [
            {"id": "g4dv-l5-we1",
             "statement": "A camp pitches $6$ gers with $4$ beds each. How many beds altogether?",
             "note": "Group size and count given; the total is wanted.",
             "solution": ("'Each' with 'altogether' calls for multiplication: "
                          "$6 \\times 4 = 24$ beds. Read the receipt backwards: "
                          "$24 \\div 6 = 4$ beds per ger — the story again ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6*4, 24)", "Eq(Rational(24,6), 4)"]},
            {"id": "g4dv-l5-we2",
             "statement": "$63$ sheep are split equally among $9$ pens. How many sheep per pen?",
             "note": "The total is given and being split.",
             "solution": ("The total $63$ is already in the story: divide. $63 "
                          "\\div 9 = 7$ sheep per pen. Receipt: $7 \\times 9 = "
                          "63$ ✓ — the flock reassembles."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(63,9), 7)", "Eq(7*9, 63)"]},
        ],
        "commonMistakes": [
            {"text": "Grabbing the two numbers and multiplying, whatever the story says.",
             "correction": "Find the total first. If the total is already in the story and being split, the operation is division: 63 sheep into 9 pens is 63 ÷ 9 = 7, not 63 × 9.",
             "authored": True},
            {"text": "Dividing by the answer instead of the given group size — for \"40 sweets, bags of 8\", reaching for 40 ÷ 5.",
             "correction": "Divide by the number the story GIVES: bags of 8 means 40 ÷ 8 = 5 bags. The 5 is the answer, not the divisor — the receipt 5 × 8 = 40 keeps every number in its seat.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4dv-l5-t1",
             "statement": "$7$ shelves hold $8$ books each. Choose the operation and find the total.",
             "solution": "Total wanted from equal groups: multiply. $7 \\times 8 = 56$ books — and $56 \\div 7 = 8$ retells the story ✓.",
             "check": ["Eq(7*8, 56)", "Eq(Rational(56,7), 8)"]},
            {"id": "g4dv-l5-t2",
             "statement": "$54$ chairs are set out in rows of $6$. Choose the operation and find the number of rows.",
             "solution": "Total given, split into groups of $6$: divide. $54 \\div 6 = 9$ rows. Receipt: $9 \\times 6 = 54$ ✓.",
             "check": ["Eq(Rational(54,6), 9)", "Eq(9*6, 54)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Which way does the story point?", [
                "MULTIPLY stories hand you equal groups and ask for the TOTAL: '$%d$ gers with $%d$ guests each — how many guests?' $%d \\times %d = %d$." % (gm_g, gm_s, gm_g, gm_s, gm_g * gm_s),
                "DIVIDE stories hand you the total and split it: '$%d$ guests, $%d$ to a ger — how many gers?' $%d \\div %d = %d$." % (gm_g * gm_s, gm_s, gm_g * gm_s, gm_s, gm_g),
                "The tell is the TOTAL: wanted, multiply; given and being split, divide. 'Altogether' usually flags the first; 'shared among' and 'groups of' flag the second. 'Each' appears in BOTH — '$%d$ gers with $%d$ guests each' multiplies, '$%d$ guests share $%d$ gers, how many in each?' divides — so let the total decide." % (gm_g, gm_s, gm_g * gm_s, gm_g),
            ]), fig_mult),
            workedset("Reading the tell",
                      "Find the total in the story before touching the numbers.", [
                wex("A camp pitches $6$ gers with $4$ beds each. Beds altogether?",
                    ["The total is WANTED, built from equal groups: multiply.",
                     "$6 \\times 4 = 24$ beds; backwards, $24 \\div 6 = 4$ retells the story ✓."],
                    "$24$ beds",
                    ["Eq(6*4, 24)", "Eq(Rational(24,6), 4)"]),
                withfig(wex("$18$ goats are penned in groups of $6$. How many pens?",
                    ["The total $18$ is GIVEN, split into sixes: divide.",
                     "$18 \\div 6 = 3$ pens. Receipt: $3 \\times 6 = 18$ ✓."],
                    "$3$ pens",
                    ["Eq(Rational(18,6), 3)", "Eq(3*6, 18)"]), fig_pens),
            ]),
            tryitset("Spot the tell", "Total wanted, or total given?", [
                tp("$9$ boxes hold $6$ khuushuur each. Altogether that is:",
                   ["$54$ khuushuur", "$15$ khuushuur", "$3$ khuushuur"],
                   "Equal groups, total wanted: $9 \\times 6 = 54$, and $54 \\div 9 = 6$ retells the story ✓. $15$ ADDED the two numbers ($9 + 6$) — boxes and khuushuur cannot be counted together.",
                   ["Eq(9*6, 54)", "Eq(Rational(54,9), 6)", "Eq(9 + 6, 15)"]),
                tp("$48$ students sit at tables of $8$. Tables needed:",
                   ["$6$", "$40$", "$56$"],
                   "The total $48$ is given, split into eights: $48 \\div 8 = 6$ tables, receipt $6 \\times 8 = 48$ ✓. $40$ subtracted and $56$ added — neither splits anything.",
                   ["Eq(Rational(48,8), 6)", "Eq(6*8, 48)"]),
                tp("$30$ litres of airag fill jugs of $5$ litres. Jugs filled:",
                   ["$6$", "$150$", "$25$"],
                   "Total given, split into fives: $30 \\div 5 = 6$ jugs, receipt $6 \\times 5 = 30$ ✓. $150$ multiplied instead — thirty jugs of five litres is a different camp.",
                   ["Eq(Rational(30,5), 6)", "Eq(6*5, 30)", "Eq(30*5, 150)"]),
            ]),
            tapq("Where division lives", "In which story is DIVISION the right move?",
                 ["$36$ sweets shared among $6$ friends",
                  "$6$ bags with $36$ sweets each",
                  "$36$ sweets and $6$ more arrive",
                  "$36$ sweets, and $6$ are eaten"],
                 "Only the first hands you a total ($36$) and splits it: $36 \\div 6 = 6$ each, receipt $6 \\times 6 = 36$ ✓. Bags of $36$ BUILD a bigger total ($6 \\times 36 = 216$); arriving is addition; eating is subtraction.",
                 ["Eq(Rational(36,6), 6)", "Eq(6*6, 36)", "Eq(6*36, 216)"]),
            funfact("Three costumes for one operation",
                    "Division wears three outfits: $12 \\div 3$, $12/3$, and the fraction $\\frac{12}{3}$ — all commanding the same split, all equal to $4$. When you meet fractions properly, you will already know their secret: every fraction is a division in costume."),
            teach("Concept B", "Receipt every story", [
                "Whichever operation you choose, the receipt closes the loop: a division's answer multiplies back to the total, and a multiplication's answer divides back to the group size. The story's numbers must rebuild each other.",
                "A wrong choice fails loudly. Splitting cannot GROW a pile: if '$56$ sheep into $8$ pens' seems to give $448$, the size alone shouts multiplication sneaked in — $56 \\div 8 = 7$ is the split.",
                "Some stories take two steps: '$5$ trays of $8$ buuz, shared among $10$ guests' — first BUILD the total ($5 \\times 8 = 40$), then SPLIT it ($40 \\div 10 = 4$ each). One multiply, one divide, one receipt each.",
            ]),
            workedset("Receipts and two-step stories",
                      "Build the total, or split it — sometimes both.", [
                wex("$40$ students ride in $8$ equal minibuses. How many in each?",
                    ["Total given, shared among $8$: $40 \\div 8 = 5$.",
                     "Receipt: $5 \\times 8 = 40$ ✓ — the group reassembles."],
                    "$5$ students",
                    ["Eq(Rational(40,8), 5)", "Eq(5*8, 40)"]),
                wex("$5$ trays hold $8$ buuz each; $10$ guests share them equally. Buuz per guest?",
                    ["Build the total first: $5 \\times 8 = 40$ buuz.",
                     "Split it: $40 \\div 10 = 4$ each. Receipt: $4 \\times 10 = 40$ ✓."],
                    "$4$ buuz",
                    ["Eq(5*8, 40)", "Eq(Rational(40,10), 4)", "Eq(4*10, 40)"]),
            ]),
            tryitset("Choose, then receipt", "One tell, one operation, one receipt.", [
                tp("$72$ arrows are shared among $8$ archers. Each archer gets:",
                   ["$9$ arrows", "$8$ arrows", "$64$ arrows"],
                   "Total given, shared: $72 \\div 8 = 9$, receipt $9 \\times 8 = 72$ ✓. $64$ took $8$ arrows away instead of sharing.",
                   ["Eq(Rational(72,8), 9)", "Eq(9*8, 72)"]),
                tp("A wrestler trains $3$ hours a day for $7$ days. Total hours:",
                   ["$21$", "$10$", "$18$"],
                   "Equal daily groups, total wanted: $3 \\times 7 = 21$, and $21 \\div 7 = 3$ retells the story ✓. $10$ added the numbers ($3 + 7$); $18$ counted only six days ($3 \\times 6$).",
                   ["Eq(3*7, 21)", "Eq(Rational(21,7), 3)", "Eq(3 + 7, 10)", "Eq(3*6, 18)"]),
                tp("$4$ quivers hold $6$ arrows each; the arrows are then shared among $3$ archers. Each gets:",
                   ["$8$ arrows", "$6$ arrows", "$2$ arrows"],
                   "Two steps: build $4 \\times 6 = 24$, then split $24 \\div 3 = 8$ each, receipt $8 \\times 3 = 24$ ✓.",
                   ["Eq(4*6, 24)", "Eq(Rational(24,3), 8)", "Eq(8*3, 24)"]),
            ]),
            tapq("Splitting cannot grow", "For '$56$ sheep split equally into $8$ pens', Tuya computes $56 \\times 8 = 448$. What gives her away?",
                 ["a split cannot grow the flock — $448 > 56$; the split is $56 \\div 8 = 7$",
                  "nothing — $448$ sheep per pen is correct",
                  "she should have added the numbers",
                  "the story cannot be answered"],
                 "A split hands out what is already there, so each pen must hold FEWER than $56$. $56 \\div 8 = 7$ sheep per pen, receipt $7 \\times 8 = 56$ ✓.",
                 ["Eq(56*8, 448)", "448 > 56", "Eq(Rational(56,8), 7)", "Eq(7*8, 56)"]),
            recap([
                "Multiplying joins equal groups into a total; dividing splits a given total.",
                "The tell: total wanted means multiply; total given means divide.",
                "'Altogether' usually asks for a total (multiply); 'shared among' and 'groups of' split one (divide) — but 'each' shows up in BOTH, so always ask whether the total is wanted or given.",
                "Splitting cannot grow the pile — a giant answer to a sharing story is a wrong turn.",
                "Receipt every story: the numbers must rebuild each other.",
            ]),
            tip("Underline the total in each story — or the words asking for it — before choosing. Then receipt: rebuild the total from your answer."),
            tryitset("Mixed practice", "Multiply, divide, or both — the tell decides.", [
                tp("$8$ rows of $7$ chairs. Chairs altogether:",
                   ["$56$", "$15$", "$63$"],
                   "Total wanted: $8 \\times 7 = 56$, and $56 \\div 8 = 7$ retells ✓. $15$ added the numbers; $63$ slipped a row ($9 \\times 7$).",
                   ["Eq(8*7, 56)", "Eq(Rational(56,8), 7)", "Eq(9*7, 63)"]),
                tp("$45$ kg of aaruul is packed into $9$ equal sacks. Each sack holds:",
                   ["$5$ kg", "$54$ kg", "$36$ kg"],
                   "Total given, split: $45 \\div 9 = 5$ kg, receipt $5 \\times 9 = 45$ ✓. $54$ added; $36$ subtracted — neither splits.",
                   ["Eq(Rational(45,9), 5)", "Eq(5*9, 45)", "Eq(45 + 9, 54)"]),
                tp("$28$ children form teams of $4$ for the Naadam relay. Teams:",
                   ["$7$", "$24$", "$32$"],
                   "Groups of $4$ from a given total: $28 \\div 4 = 7$ teams, receipt $7 \\times 4 = 28$ ✓.",
                   ["Eq(Rational(28,4), 7)", "Eq(7*4, 28)"]),
                tp("Which story matches $6 \\times 9 = 54$?",
                   ["$6$ shelves of $9$ books — how many books altogether",
                    "$54$ books shared onto $6$ shelves — how many per shelf",
                    "$9$ books, and $6$ are given away"],
                   "Equal groups joined into a wanted total: shelves of $9$. The second story is the DIVISION $54 \\div 6 = 9$ — same family, other direction; the third is subtraction.",
                   ["Eq(6*9, 54)", "Eq(Rational(54,6), 9)"]),
                tp("$3$ herders own $8$ horses each; the horses are stabled $6$ to a pen. Pens needed:",
                   ["$4$", "$24$", "$2$"],
                   "Two steps: build the total $3 \\times 8 = 24$ horses, then split into sixes: $24 \\div 6 = 4$ pens, receipt $4 \\times 6 = 24$ ✓.",
                   ["Eq(3*8, 24)", "Eq(Rational(24,6), 4)", "Eq(4*6, 24)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Multiply or Divide?\" — and the topic",
                    "Sharing and grouping, fact families, first remainders, folds and unfolds, and stories that reveal their operation through the total — with a multiply-back receipt on every single answer. Long division, where the same receipts steer much bigger numbers, is Grade 5's story.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    # pr4 figure: the tray BEFORE any plate is filled — the whole pile,
    # un-partitioned. Filling the plates and counting the leftover is the
    # question, so the picture must not do it.
    p4n, p4d, p4q, p4r = 22, 6, 3, 4
    fig_tray = fig_groups((p4n, "buuz on the tray"))
    # pr8 figure: the ladder of eights along 0..40, labelled with plain
    # numbers only. Which two straddle 30 — and the gap to the lower one —
    # is left for the student.
    e_d, e_n, e_hi = 8, 30, 40
    fig_between = fig_numline(
        [(e_d * i, str(e_d * i)) for i in range(1, e_hi // e_d + 1)]
        + [(e_n, str(e_n), C_WARM)],
        lo=0, hi=e_hi)
    return [
        prob("g4dv-pr1", "Share $42$ aaruul equally among $6$ plates. How many on each plate? Multiply back to check.",
             "$42 \\div 6 = 7$ on each plate. Check: $7 \\times 6 = 42$ ✓.",
             ["Eq(Rational(42,6), 7)", "Eq(7*6, 42)"]),
        prob("g4dv-pr2", "How many teams of $9$ can $81$ children make?",
             "Groups of $9$ from a total of $81$: $81 \\div 9 = 9$ teams. Check: $9 \\times 9 = 81$ ✓.",
             ["Eq(Rational(81,9), 9)", "Eq(9*9, 81)"]),
        prob("g4dv-pr3", "Write the full fact family of $8$, $9$ and $72$.",
             "$8 \\times 9 = 72$, $9 \\times 8 = 72$, $72 \\div 8 = 9$, $72 \\div 9 = 8$ — the product $72$ leads both divisions.",
             ["Eq(8*9, 72)", "Eq(9*8, 72)",
              "Eq(Rational(72,8), 9)", "Eq(Rational(72,9), 8)"]),
        withprobfig(
            prob("g4dv-pr4",
                 "$%d$ buuz are set out on plates of $%d$. How many full plates, and how many buuz are left? Sign the receipt." % (p4n, p4d),
                 "$%d \\times %d = %d$ fits inside $%d$: $%d$ full plates and $%d$ buuz left. Receipt: $%d \\times %d + %d = %d$ ✓ and $%d < %d$ ✓." % (
                     p4d, p4q, p4d * p4q, p4n, p4q, p4r, p4q, p4d, p4r, p4n, p4r, p4d),
                 ["Eq(%d*%d, %d)" % (p4d, p4q, p4d * p4q),
                  "Eq(%d*%d + %d, %d)" % (p4q, p4d, p4r, p4n),
                  "%d < %d" % (p4r, p4d)]),
            fig_tray),
        prob("g4dv-pr5", "Compute $47 \\div 5$ with its remainder, and sign the receipt.",
             "$5 \\times 9 = 45$ fits: $47 \\div 5 = 9$ r $2$. Receipt: $9 \\times 5 + 2 = 47$ ✓ and $2 < 5$ ✓.",
             ["Eq(5*9, 45)", "Eq(9*5 + 2, 47)", "2 < 5"]),
        prob("g4dv-pr6", "Halve $6\\,800$, and prove your answer by doubling.",
             "$6\\,000 \\to 3\\,000$ and $800 \\to 400$: half is $3\\,400$. Proof: $2 \\times 3\\,400 = 6\\,800$ ✓.",
             ["Eq(Rational(6800,2), 3400)", "Eq(2*3400, 6800)"]),
        prob("g4dv-pr7", "A camp pitches $7$ gers with $6$ guests each. Choose the operation and find the number of guests.",
             "The total is wanted from equal groups: multiply. $7 \\times 6 = 42$ guests — and $42 \\div 7 = 6$ retells the story ✓.",
             ["Eq(7*6, 42)", "Eq(Rational(42,7), 6)"]),
        withprobfig(
            prob("g4dv-pr8", "Between which two multiples of $8$ does $30$ sit? Use them to write $30 \\div 8$ with its remainder and receipt.",
                 "$3 \\times 8 = 24$ and $4 \\times 8 = 32$: the pile sits between them, so $30 \\div 8 = 3$ r $6$. Receipt: $3 \\times 8 + 6 = 30$ ✓ and $6 < 8$ ✓.",
                 ["Eq(3*8, 24)", "Eq(4*8, 32)", "24 < 30", "30 < 32",
                  "Eq(3*8 + 6, 30)", "6 < 8"]),
            fig_between),
    ]


def test_bank():
    return [
        prob("g4dv-x1", "Compute $64 \\div 8$, and write the multiplication that checks it.",
             "$8 \\times 8 = 64$ — a square family — so $64 \\div 8 = 8$, checked by $8 \\times 8 = 64$ ✓.",
             ["Eq(Rational(64,8), 8)", "Eq(8*8, 64)"]),
        prob("g4dv-x2", "Find $54 \\div 6$ by unknown-factor thinking, naming the times-table fact you used.",
             "$54 \\div 6$ asks $6 \\times \\square = 54$; the fact is $6 \\times 9 = 54$, so $54 \\div 6 = 9$.",
             ["Eq(6*9, 54)", "Eq(Rational(54,6), 9)"]),
        prob("g4dv-x3", "$62$ sweets are packed in bags of $7$. How many full bags, how many sweets left? Sign the receipt.",
             "$7 \\times 8 = 56$ fits inside $62$: $8$ full bags and $6$ sweets left. Receipt: $8 \\times 7 + 6 = 62$ ✓ and $6 < 7$ ✓.",
             ["Eq(7*8, 56)", "Eq(8*7 + 6, 62)", "6 < 7"]),
        prob("g4dv-x4", "Halve $9\\,600$, and check your answer by doubling.",
             "$9\\,600 = 8\\,000 + 1\\,600$: half is $4\\,000 + 800 = 4\\,800$. Check: $2 \\times 4\\,800 = 9\\,600$ ✓.",
             ["Eq(Rational(9600,2), 4800)", "Eq(4000 + 800, 4800)", "Eq(2*4800, 9600)"]),
        prob("g4dv-x5", "$63$ khuushuur are shared equally among $7$ tables. Choose the operation and find how many per table.",
             "The total $63$ is given and being split: divide. $63 \\div 7 = 9$ per table. Receipt: $9 \\times 7 = 63$ ✓.",
             ["Eq(Rational(63,7), 9)", "Eq(9*7, 63)"]),
        prob("g4dv-x6", "$6$ trays hold $8$ buuz each, and the buuz are shared equally among $4$ friends. How many buuz per friend? Receipt both steps.",
             "Build the total: $6 \\times 8 = 48$ buuz. Split it: $48 \\div 4 = 12$ each. Receipts: $48 \\div 6 = 8$ retells the trays ✓ and $12 \\times 4 = 48$ rebuilds the pile ✓.",
             ["Eq(6*8, 48)", "Eq(Rational(48,6), 8)",
              "Eq(Rational(48,4), 12)", "Eq(12*4, 48)"]),
    ]


def main():
    topic = {
        "slug": "division-and-sharing",
        "title": "Division & Sharing",
        "grade": 4,
        "status": "published",
        "blurb": ("Sharing and grouping as the two faces of division, "
                  "division facts from the times tables, first remainders "
                  "with their receipts, and choosing the right operation."),
        "lessons": [
            lesson_sharing_grouping(),
            lesson_division_facts(),
            lesson_remainders(),
            lesson_halving_doubling(),
            lesson_choosing(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "division-and-sharing.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
