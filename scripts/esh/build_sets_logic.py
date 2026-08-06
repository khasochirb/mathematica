#!/usr/bin/env python3
"""Sets & Logic — the three ЭЕШ-authored units under data/genmath/esh/.

The one ЭЕШ exam topic with no source anywhere in the platform catalog, so
these units are authored here rather than curated. English-first per the
owner decision recorded in memory/expansion-vision.md §4.7 (2026-07-28), and
pitched at a student already scoring ~650/800: notation is introduced
briskly, and the worked problems are exam-shaped (multi-fact chains, survey
counting, interval reasoning) rather than definitional drills.

Every numeric claim is interpolated from named Python variables and asserted
by sympy at build time (imbuild.assert_checks) — the same discipline as the
IM builders. Run from repo root:

    python3 scripts/esh/build_sets_logic.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "im"))
from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402


# ===========================================================================
# Unit 1 — Sets & Operations
# ===========================================================================

def build_sets_and_operations():
    lessons = []

    # --- Lesson 1: The language of sets ------------------------------------
    lessons.append(lesson(
        slug="sets-and-membership",
        title="Sets, Membership & Cardinality",
        concrete=(
            "A set is a guest list: what matters is WHO is on it, not the order "
            "you wrote the names in or how many times a name got scribbled. "
            "{1, 2, 3} and {3, 1, 2, 2} are the same party."
        ),
        objective=(
            "Read and write sets in roster and set-builder notation, decide "
            "membership and subset claims, and count a set's elements."
        ),
        concept=[
            "A **set** is an unordered collection of distinct objects, its **elements**. "
            "$x \\in A$ says $x$ is an element of $A$; $x \\notin A$ says it is not. "
            "Roster notation lists the elements: $A = \\{2, 4, 6, 8\\}$. Set-builder "
            "notation states the rule: $A = \\{x \\in \\mathbb{Z} : -2 \\le x < 4\\}$ "
            "reads 'all integers from $-2$ up to but not including $4$'.",
            "$B \\subseteq A$ ($B$ is a **subset** of $A$) means every element of $B$ is "
            "also in $A$. Watch the two levels: $2 \\in \\{2, 4\\}$ is an element claim, "
            "$\\{2\\} \\subseteq \\{2, 4\\}$ is a subset claim — mixing them up is the "
            "classic exam trap. The **empty set** $\\varnothing$ has no elements and is "
            "a subset of every set.",
            "The **cardinality** $|A|$ (also written $n(A)$) is the number of elements. "
            "For a run of consecutive integers from $a$ to $b$ inclusive, "
            "$|A| = b - a + 1$ — the '+1' is where fast solvers lose a point.",
        ],
        key_idea=(
            "A set is decided by membership alone — no order, no repeats. Element "
            "claims use $\\in$, subset claims use $\\subseteq$, and $|A|$ counts."
        ),
        facts=[
            fact(
                "Membership vs subset",
                "x \\in A, \\qquad B \\subseteq A",
                "An ELEMENT belongs with $\\in$; a whole SET fits inside with $\\subseteq$.",
            ),
            fact(
                "Consecutive-integer count",
                "|\\{a, a+1, \\ldots, b\\}| = b - a + 1",
                "Inclusive runs count both ends — subtract, then add one.",
            ),
        ],
        worked=[
            problem(
                "esh-sets-l1-we1",
                "List the elements of $A = \\{x \\in \\mathbb{Z} : -2 \\le x < 4\\}$ and state $|A|$.",
                "The integers from $-2$ up to $3$: $A = \\{-2, -1, 0, 1, 2, 3\\}$. "
                "Count with the inclusive-run rule from $-2$ to $3$: $3 - (-2) + 1 = 6$, so $|A| = 6$.",
                ["Eq(3 - (-2) + 1, 6)"],
            ),
            problem(
                "esh-sets-l1-we2",
                "How many positive multiples of $3$ are less than $50$? Write the set in set-builder notation first.",
                "$M = \\{x \\in \\mathbb{N} : x < 50,\\ 3 \\mid x\\} = \\{3, 6, \\ldots, 48\\}$. "
                "The largest is $48 = 3 \\cdot 16$, so there are $\\lfloor 49/3 \\rfloor = 16$ elements.",
                ["Eq(floor(Rational(49, 3)), 16)", "Eq(3*16, 48)"],
            ),
        ],
        mistakes=[
            mistake(
                "Writing $\\{2\\} \\in \\{2, 4\\}$ because '2 is in the set'.",
                "$2 \\in \\{2, 4\\}$ (element), but $\\{2\\} \\subseteq \\{2, 4\\}$ (subset). "
                "$\\{2\\} \\in \\{2, 4\\}$ is false — the set $\\{2\\}$ is not one of the listed elements.",
            ),
            mistake(
                "Counting $\\{5, 6, \\ldots, 20\\}$ as $20 - 5 = 15$ elements.",
                "Inclusive runs need the $+1$: $20 - 5 + 1 = 16$ elements.",
            ),
        ],
        try_it=[
            problem(
                "esh-sets-l1-t1",
                "State $|B|$ for $B = \\{x \\in \\mathbb{Z} : -7 < x \\le 5\\}$.",
                "The integers from $-6$ to $5$ inclusive: $5 - (-6) + 1 = 12$, so $|B| = 12$. "
                "Note $-7$ itself is excluded by the strict inequality.",
                ["Eq(5 - (-6) + 1, 12)"],
            ),
            problem(
                "esh-sets-l1-t2",
                "How many two-digit numbers are divisible by $7$?",
                "Two-digit multiples of $7$ run from $14 = 7 \\cdot 2$ to $98 = 7 \\cdot 14$: "
                "that is $14 - 2 + 1 = 13$ numbers.",
                ["Eq(7*2, 14)", "Eq(7*14, 98)", "Eq(14 - 2 + 1, 13)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The language",
                "title": "Guest lists, not queues",
                "body": (
                    "A set cares only about membership. $\\{1, 2, 3\\}$, $\\{3, 2, 1\\}$ and "
                    "$\\{1, 1, 2, 3\\}$ are all the SAME set — order and repeats are ignored. "
                    "Everything in this unit builds on that single convention."
                ),
            },
            {
                "kind": "teach",
                "eyebrow": "Two levels",
                "title": "Element vs subset",
                "body": (
                    "$\\in$ speaks about one element; $\\subseteq$ speaks about a whole set. "
                    "$2 \\in \\{2, 4\\}$ and $\\{2\\} \\subseteq \\{2, 4\\}$ are both true — but "
                    "$\\{2\\} \\in \\{2, 4\\}$ is false, and the exam loves to offer it."
                ),
            },
            tap(
                "Which claims hold?",
                "For $A = \\{1, \\{2\\}, 3\\}$, which statement is TRUE?",
                ["$\\{2\\} \\in A$", "$2 \\in A$", "$\\{1, 2\\} \\subseteq A$", "$|A| = 2$"],
                0,
                "The elements of $A$ are $1$, the SET $\\{2\\}$, and $3$ — so $\\{2\\} \\in A$ is true, "
                "while the number $2$ itself is not an element. $|A| = 3$.",
                ["Eq(3, 3)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Set-builder to roster", "problemId": "esh-sets-l1-we1"},
            {"kind": "worked", "title": "Counting multiples", "problemId": "esh-sets-l1-we2"},
            tap(
                "The +1 reflex",
                "How many integers satisfy $-4 \\le x \\le 9$?",
                ["$13$", "$14$", "$12$", "$9$"],
                1,
                "Inclusive run: $9 - (-4) + 1 = 14$. Forgetting the $+1$ gives the tempting $13$.",
                ["Eq(9 - (-4) + 1, 14)"],
                eyebrow="Quick check",
            ),
            {"kind": "tryIt", "title": "Strict on one side", "problemId": "esh-sets-l1-t1"},
            {"kind": "tryIt", "title": "Two-digit multiples", "problemId": "esh-sets-l1-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "A set = membership only; no order, no repeats",
                    "$\\in$ for elements, $\\subseteq$ for sets; $\\varnothing \\subseteq$ everything",
                    "Consecutive integers $a$ to $b$: count $= b - a + 1$",
                ],
            },
        ],
    ))

    # --- Lesson 2: Union, intersection, difference, complement -------------
    lessons.append(lesson(
        slug="union-intersection-difference",
        title="Union, Intersection, Difference & Complement",
        concrete=(
            "Two clubs at one school: the union is everyone who joined anything, "
            "the intersection is the students running between both rooms, the "
            "difference is one club with the double-bookers removed, and the "
            "complement is everyone still at home."
        ),
        objective=(
            "Compute $A \\cup B$, $A \\cap B$, $A \\setminus B$ and $A'$ for concrete "
            "sets, and read each operation as a plain-language condition."
        ),
        concept=[
            "**Union** $A \\cup B = \\{x : x \\in A \\text{ or } x \\in B\\}$ — in at least one. "
            "**Intersection** $A \\cap B = \\{x : x \\in A \\text{ and } x \\in B\\}$ — in both. "
            "Two sets with $A \\cap B = \\varnothing$ are **disjoint**.",
            "**Difference** $A \\setminus B$ keeps what is in $A$ but not in $B$ — and it is "
            "not symmetric: $A \\setminus B \\ne B \\setminus A$ in general. Within a stated "
            "**universal set** $U$, the **complement** $A' = U \\setminus A$ is everything "
            "$A$ leaves out, so $|A'| = |U| - |A|$.",
            "On the exam these appear as conditions chained in words: 'divisible by 2 or 3' "
            "is a union, 'divisible by 2 and 3' is an intersection, 'even but not a multiple "
            "of 3' is a difference. Translate the sentence into the operation first, then count.",
        ],
        key_idea=(
            "Or $\\to \\cup$, and $\\to \\cap$, but-not $\\to \\setminus$, everything-else "
            "$\\to$ complement. The operation IS the sentence."
        ),
        facts=[
            fact(
                "The four operations",
                "A \\cup B,\\quad A \\cap B,\\quad A \\setminus B,\\quad A' = U \\setminus A",
                "Or, and, but-not, everything-else — each word picks its operation.",
            ),
            fact(
                "Complement count",
                "|A'| = |U| - |A|",
                "Counting what you don't want is often faster than counting what you do.",
            ),
        ],
        worked=[
            problem(
                "esh-sets-l2-we1",
                "Let $A = \\{1, 2, 3, 4, 5, 6\\}$ and $B = \\{4, 5, 6, 7, 8\\}$. Find "
                "$|A \\cup B|$, $|A \\cap B|$ and $|A \\setminus B|$.",
                "$A \\cap B = \\{4, 5, 6\\}$, so $|A \\cap B| = 3$. "
                "$A \\cup B = \\{1, \\ldots, 8\\}$, so $|A \\cup B| = 8$ — note "
                "$6 + 5 - 3 = 8$, the shared elements are counted once. "
                "$A \\setminus B = \\{1, 2, 3\\}$, so $|A \\setminus B| = 6 - 3 = 3$.",
                ["Eq(6 + 5 - 3, 8)", "Eq(6 - 3, 3)"],
            ),
            problem(
                "esh-sets-l2-we2",
                "With universal set $U = \\{1, 2, \\ldots, 30\\}$, let $E$ be the multiples of "
                "$2$ and $T$ the multiples of $3$. How many elements are even but NOT multiples of $3$?",
                "$|E| = 15$ (the evens up to $30$) and $E \\cap T$ is the multiples of $6$: "
                "$|E \\cap T| = 5$. The question asks for $|E \\setminus T| = 15 - 5 = 10$.",
                ["Eq(floor(Rational(30, 2)), 15)", "Eq(floor(Rational(30, 6)), 5)", "Eq(15 - 5, 10)"],
            ),
        ],
        mistakes=[
            mistake(
                "Computing $|A \\cup B|$ as $|A| + |B|$.",
                "Shared elements get counted twice that way. Either list the union, or use "
                "$|A| + |B| - |A \\cap B|$ — the next unit makes this a formula.",
            ),
            mistake(
                "Treating $A \\setminus B$ and $B \\setminus A$ as the same set.",
                "Difference is directional: $\\{1,2,3\\} \\setminus \\{3\\} = \\{1,2\\}$ but "
                "$\\{3\\} \\setminus \\{1,2,3\\} = \\varnothing$.",
            ),
        ],
        try_it=[
            problem(
                "esh-sets-l2-t1",
                "For $A = \\{2, 4, 6, 8, 10, 12\\}$ and $B = \\{3, 6, 9, 12\\}$, find "
                "$|A \\cap B|$ and $|A \\cup B|$.",
                "$A \\cap B = \\{6, 12\\}$: $|A \\cap B| = 2$. Then "
                "$|A \\cup B| = 6 + 4 - 2 = 8$.",
                ["Eq(6 + 4 - 2, 8)"],
            ),
            problem(
                "esh-sets-l2-t2",
                "In $U = \\{1, \\ldots, 40\\}$, how many numbers are NOT multiples of $5$?",
                "Multiples of $5$: $|A| = 8$. Complement: $|A'| = 40 - 8 = 32$.",
                ["Eq(floor(Rational(40, 5)), 8)", "Eq(40 - 8, 32)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "Four verbs",
                "title": "Or, and, but-not, everything-else",
                "body": (
                    "Every set operation is a sentence: union collects anything in EITHER set, "
                    "intersection demands BOTH, difference keeps one side and evicts the overlap, "
                    "complement flips to everything the set is not. Translate first, compute second."
                ),
            },
            tap(
                "Pick the operation",
                "'Students who study physics but not chemistry' is which set?",
                ["$P \\setminus C$", "$P \\cap C$", "$P \\cup C$", "$C \\setminus P$"],
                0,
                "'But not' is a difference, taken FROM physics: $P \\setminus C$. "
                "Direction matters — $C \\setminus P$ is the chemists who avoid physics.",
                ["Eq(1, 1)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "All three counts at once", "problemId": "esh-sets-l2-we1"},
            {"kind": "worked", "title": "Even but not a multiple of 3", "problemId": "esh-sets-l2-we2"},
            tap(
                "Disjoint or not",
                "$A$ = odd numbers, $B$ = multiples of $4$. What is $A \\cap B$?",
                ["$\\varnothing$", "$\\{4\\}$", "the odd multiples of 4", "$A$"],
                0,
                "Every multiple of $4$ is even, so no odd number can be in $B$: the sets are "
                "disjoint and the intersection is empty.",
                ["Eq(Mod(4, 2), 0)"],
                eyebrow="Quick check",
            ),
            {"kind": "tryIt", "title": "Intersection, then union", "problemId": "esh-sets-l2-t1"},
            {"kind": "tryIt", "title": "Count the complement", "problemId": "esh-sets-l2-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$\\cup$ = or, $\\cap$ = and, $\\setminus$ = but-not (directional!), $'$ = everything else",
                    "$|A'| = |U| - |A|$ — complements turn hard counts into easy ones",
                    "Never add $|A| + |B|$ for a union without removing the overlap",
                ],
            },
        ],
    ))

    # --- Lesson 3: Subsets and power sets ----------------------------------
    lessons.append(lesson(
        slug="subsets-and-power-sets",
        title="Counting Subsets",
        concrete=(
            "Packing a bag from 5 items: each item is an independent yes/no. Five "
            "binary switches give $2^5 = 32$ different bags — including the empty "
            "one. Subset counting is switch counting."
        ),
        objective=(
            "Count all subsets, proper subsets, and subsets constrained to contain "
            "or avoid particular elements."
        ),
        concept=[
            "Each element of an $n$-element set is either IN a subset or OUT — $n$ "
            "independent binary choices, so there are $2^n$ subsets in total. The count "
            "includes $\\varnothing$ (all switches off) and $A$ itself (all on).",
            "A **proper subset** excludes $A$ itself, leaving $2^n - 1$. Some texts also "
            "exclude $\\varnothing$; ЭЕШ items say explicitly which is meant — read the stem.",
            "Constraints pin switches: subsets that MUST contain a given element leave "
            "$n-1$ free choices, so $2^{n-1}$ of them; must-contain-two leaves $2^{n-2}$. "
            "Subsets avoiding an element are the subsets of the other $n-1$ elements — "
            "also $2^{n-1}$. Pin the forced switches, count the free ones.",
        ],
        key_idea=(
            "Subsets are binary choices: $2^n$ total, and every constraint just pins "
            "switches — count $2^{\\text{free}}$."
        ),
        facts=[
            fact(
                "Subset count",
                "\\#\\text{subsets of an } n\\text{-set} = 2^n",
                "In-or-out for each element; the empty set and the whole set both count.",
            ),
            fact(
                "Pinned elements",
                "\\#\\{S : a \\in S\\} = 2^{n-1}",
                "Forcing an element in (or out) removes one free choice.",
            ),
        ],
        worked=[
            problem(
                "esh-sets-l3-we1",
                "A set has $6$ elements. How many subsets does it have, and how many are proper?",
                "Total: $2^6 = 64$. Proper subsets exclude the set itself: $64 - 1 = 63$.",
                ["Eq(2**6, 64)", "Eq(2**6 - 1, 63)"],
            ),
            problem(
                "esh-sets-l3-we2",
                "How many subsets of $\\{1, 2, 3, 4, 5, 6, 7\\}$ contain both $1$ and $2$?",
                "Pin $1$ and $2$ in; the other five elements stay free: $2^{7-2} = 2^5 = 32$.",
                ["Eq(2**5, 32)", "Eq(7 - 2, 5)"],
            ),
        ],
        mistakes=[
            mistake(
                "Forgetting that $\\varnothing$ and $A$ itself are subsets.",
                "Both count in $2^n$. Only 'proper' (and, when stated, 'non-empty') removes them.",
            ),
            mistake(
                "Counting subsets that contain $a$ as $2^n - 1$.",
                "Pinning $a$ in leaves $n-1$ free elements: $2^{n-1}$, which is half of $2^n$ — "
                "as symmetry demands, since $a$ is in exactly half of all subsets.",
            ),
        ],
        try_it=[
            problem(
                "esh-sets-l3-t1",
                "$|A| = 8$. How many non-empty proper subsets does $A$ have?",
                "All subsets: $2^8 = 256$. Remove $\\varnothing$ and $A$: $256 - 2 = 254$.",
                ["Eq(2**8, 256)", "Eq(256 - 2, 254)"],
            ),
            problem(
                "esh-sets-l3-t2",
                "How many subsets of a $6$-element set contain a chosen element $a$ but NOT a chosen element $b$?",
                "$a$ pinned in, $b$ pinned out — four elements remain free: $2^4 = 16$.",
                ["Eq(6 - 2, 4)", "Eq(2**4, 16)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The switchboard",
                "title": "n elements, n switches",
                "body": (
                    "Building a subset is walking down the element list flipping in/out switches. "
                    "$n$ independent switches, $2^n$ outcomes. This one picture answers every "
                    "subset-counting question in the topic."
                ),
            },
            {"kind": "worked", "title": "Total and proper", "problemId": "esh-sets-l3-we1"},
            tap(
                "Halving",
                "What fraction of all subsets of an $n$-set contain a fixed element $a$?",
                ["exactly half", "$1/n$", "depends on $n$", "all but one"],
                0,
                "Pair each subset with its version toggling $a$: one of each pair contains $a$. "
                "So exactly half — $2^{n-1}$ of $2^n$.",
                ["Eq(2**5, 2 * 2**4)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Two pinned elements", "problemId": "esh-sets-l3-we2"},
            {"kind": "tryIt", "title": "Non-empty and proper", "problemId": "esh-sets-l3-t1"},
            {"kind": "tryIt", "title": "One in, one out", "problemId": "esh-sets-l3-t2"},
            {
                "kind": "funFact",
                "eyebrow": "Fun fact",
                "title": "Why 2^0 = 1 makes sense here",
                "body": (
                    "The empty set has exactly one subset — itself. The formula $2^n$ handles "
                    "the edge case with no special pleading: $2^0 = 1$. When a formula survives "
                    "its weirdest input, trust it more, not less."
                ),
            },
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$2^n$ subsets; $2^n - 1$ proper; $2^n - 2$ non-empty proper",
                    "Each pinned element halves the count: $2^{\\text{free}}$",
                    "Read the stem: 'proper' and 'non-empty' change the answer by 1 each",
                ],
            },
        ],
    ))

    # --- Lesson 4: Set identities ------------------------------------------
    lessons.append(lesson(
        slug="set-identities",
        title="De Morgan & the Algebra of Sets",
        concrete=(
            "Negating 'cheap AND fast' gives 'expensive OR slow' — the NOT "
            "distributes and flips the connective. De Morgan's laws are that "
            "everyday negation, written in set language."
        ),
        objective=(
            "Apply De Morgan's laws and the distributive laws to rewrite and "
            "count complements of unions and intersections."
        ),
        concept=[
            "**De Morgan's laws**: $(A \\cup B)' = A' \\cap B'$ and "
            "$(A \\cap B)' = A' \\cup B'$. Complement flips union with intersection. "
            "In words: NOT (in either) = outside both; NOT (in both) = missing from at least one.",
            "The **distributive laws** mirror arithmetic: "
            "$A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)$ and "
            "$A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)$ — the second has no "
            "arithmetic analogue, which is why it feels wrong and is tested.",
            "The exam's favorite use is counting: 'how many are in neither club' is "
            "$|(A \\cup B)'| = |U| - |A \\cup B|$ — one De Morgan step turns a fussy "
            "condition into a subtraction.",
        ],
        key_idea=(
            "Complement swaps $\\cup$ and $\\cap$ (De Morgan). 'Neither' means "
            "$|U| - |A \\cup B|$ — always."
        ),
        facts=[
            fact(
                "De Morgan's laws",
                "(A \\cup B)' = A' \\cap B', \\qquad (A \\cap B)' = A' \\cup B'",
                "The complement bar breaks over the operation and flips it.",
            ),
            fact(
                "Neither count",
                "|\\text{neither}| = |U| - |A \\cup B|",
                "One subtraction, once the union is known.",
            ),
        ],
        worked=[
            problem(
                "esh-sets-l4-we1",
                "In $U = \\{1, \\ldots, 20\\}$, $A$ = multiples of $4$, $B$ = multiples of $5$. "
                "Verify De Morgan by counting: $|(A \\cup B)'|$ and $|A' \\cap B'|$.",
                "$|A| = 5$, $|B| = 4$, $A \\cap B$ = multiples of $20$: $|A \\cap B| = 1$. "
                "So $|A \\cup B| = 5 + 4 - 1 = 8$ and $|(A \\cup B)'| = 20 - 8 = 12$. "
                "Directly: $A' \\cap B'$ is the numbers divisible by neither — the same $12$ "
                "elements. Both routes agree, as De Morgan promises.",
                [
                    "Eq(floor(Rational(20, 4)), 5)",
                    "Eq(floor(Rational(20, 5)), 4)",
                    "Eq(floor(Rational(20, 20)), 1)",
                    "Eq(5 + 4 - 1, 8)",
                    "Eq(20 - 8, 12)",
                ],
            ),
            problem(
                "esh-sets-l4-we2",
                "Of $32$ students, $18$ passed algebra and the set of students who failed BOTH "
                "algebra and geometry has $6$ students. How many passed at least one subject?",
                "'Failed both' is $(A \\cup G)'$ by De Morgan. So "
                "$|A \\cup G| = 32 - 6 = 26$ students passed at least one.",
                ["Eq(32 - 6, 26)"],
            ),
        ],
        mistakes=[
            mistake(
                "Distributing the complement without flipping: $(A \\cup B)' = A' \\cup B'$.",
                "The operation flips: $(A \\cup B)' = A' \\cap B'$. Check with a tiny example — "
                "$U = \\{1,2\\}$, $A = \\{1\\}$, $B = \\{2\\}$ breaks the unflipped version.",
            ),
            mistake(
                "Reading 'not both' as 'neither'.",
                "'Not both' is $(A \\cap B)' $ — missing from at least one. 'Neither' is "
                "$(A \\cup B)'$ — missing from both. They differ by everyone in exactly one set.",
            ),
        ],
        try_it=[
            problem(
                "esh-sets-l4-t1",
                "In $U$ with $|U| = 50$: $|A| = 23$, $|B| = 19$, $|A \\cap B| = 8$. "
                "Find $|A' \\cap B'|$.",
                "$|A \\cup B| = 23 + 19 - 8 = 34$; De Morgan turns the target into "
                "$|(A \\cup B)'| = 50 - 34 = 16$.",
                ["Eq(23 + 19 - 8, 34)", "Eq(50 - 34, 16)"],
            ),
            problem(
                "esh-sets-l4-t2",
                "With the same data, how many elements are in $A' \\cup B'$?",
                "De Morgan: $A' \\cup B' = (A \\cap B)'$, so the count is $50 - 8 = 42$.",
                ["Eq(50 - 8, 42)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The flip",
                "title": "NOT breaks the bracket and flips the verb",
                "body": (
                    "Negate 'in $A$ or $B$' and you get 'out of $A$ AND out of $B$'. Negate "
                    "'in both' and you get 'missing from at least one'. That is the whole of "
                    "De Morgan — the symbols just record it."
                ),
            },
            {"kind": "worked", "title": "De Morgan, verified by counting", "problemId": "esh-sets-l4-we1"},
            tap(
                "Neither vs not-both",
                "$|U| = 40$, $|A \\cap B| = 9$. How many elements are NOT in both sets?",
                ["$31$", "$9$", "$40 - |A \\cup B|$", "cannot be determined"],
                0,
                "'Not in both' is the complement of the intersection: $40 - 9 = 31$. "
                "('Neither' would need the union instead — different question.)",
                ["Eq(40 - 9, 31)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Failed both, passed at least one", "problemId": "esh-sets-l4-we2"},
            {"kind": "tryIt", "title": "Neither, via De Morgan", "problemId": "esh-sets-l4-t1"},
            {"kind": "tryIt", "title": "Missing from at least one", "problemId": "esh-sets-l4-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$(A \\cup B)' = A' \\cap B'$ and $(A \\cap B)' = A' \\cup B'$",
                    "'Neither' $= |U| - |A \\cup B|$; 'not both' $= |U| - |A \\cap B|$",
                    "When a complement looks hard, De Morgan it into a subtraction",
                ],
            },
        ],
    ))

    practice = [
        problem(
            "esh-sets-p1",
            "Write the elements of $A = \\{x \\in \\mathbb{Z} : x^2 < 10\\}$ and state $|A|$.",
            "Integers with square below $10$: $\\{-3, -2, -1, 0, 1, 2, 3\\}$, so $|A| = 7$.",
            ["Eq(3**2, 9)", "9 < 10", "Eq(4**2, 16)", "16 > 10", "Eq(3 - (-3) + 1, 7)"],
        ),
        problem(
            "esh-sets-p2",
            "How many integers between $1$ and $100$ inclusive are multiples of $6$?",
            "From $6$ to $96 = 6 \\cdot 16$: $\\lfloor 100/6 \\rfloor = 16$.",
            ["Eq(floor(Rational(100, 6)), 16)", "Eq(6*16, 96)"],
        ),
        problem(
            "esh-sets-p3",
            "$A = \\{1,3,5,7,9,11\\}$, $B = \\{3,6,9,12\\}$. Find $|A \\cup B|$ and $|B \\setminus A|$.",
            "$A \\cap B = \\{3, 9\\}$: $|A \\cup B| = 6 + 4 - 2 = 8$; $|B \\setminus A| = 4 - 2 = 2$.",
            ["Eq(6 + 4 - 2, 8)", "Eq(4 - 2, 2)"],
        ),
        problem(
            "esh-sets-p4",
            "A set has $2^n = 128$ subsets. Find $n$ and the number of its non-empty subsets.",
            "$2^7 = 128$, so $n = 7$. Non-empty: $128 - 1 = 127$.",
            ["Eq(2**7, 128)", "Eq(128 - 1, 127)"],
        ),
        problem(
            "esh-sets-p5",
            "How many subsets of $\\{a, b, c, d, e\\}$ contain $a$ or $b$ (at least one of them)?",
            "Complement count: subsets avoiding BOTH $a$ and $b$ are subsets of the other three "
            "elements — $2^3 = 8$. So $2^5 - 8 = 32 - 8 = 24$.",
            ["Eq(2**5, 32)", "Eq(2**3, 8)", "Eq(32 - 8, 24)"],
        ),
        problem(
            "esh-sets-p6",
            "In $U = \\{1, \\ldots, 60\\}$, how many numbers are multiples of neither $4$ nor $6$?",
            "$|A| = 15$, $|B| = 10$; multiples of $\\mathrm{lcm}(4,6) = 12$: $|A \\cap B| = 5$. "
            "Union: $15 + 10 - 5 = 20$; neither: $60 - 20 = 40$.",
            [
                "Eq(floor(Rational(60, 4)), 15)",
                "Eq(floor(Rational(60, 6)), 10)",
                "Eq(lcm(4, 6), 12)",
                "Eq(floor(Rational(60, 12)), 5)",
                "Eq(15 + 10 - 5, 20)",
                "Eq(60 - 20, 40)",
            ],
        ),
        problem(
            "esh-sets-p7",
            "True or false, for $A = \\{2, \\{3\\}\\}$: (i) $3 \\in A$; (ii) $\\{3\\} \\in A$; "
            "(iii) $\\{\\{3\\}\\} \\subseteq A$. How many are true?",
            "(i) false — the elements are $2$ and the set $\\{3\\}$; (ii) true; (iii) true, since "
            "its only element $\\{3\\}$ is in $A$. Two of the three hold.",
            ["Eq(2, 2)"],
        ),
        problem(
            "esh-sets-p8",
            "$|U| = 45$, $|A| = 21$, $|B| = 17$, $|A' \\cap B'| = 15$. Find $|A \\cap B|$.",
            "De Morgan: $|A \\cup B| = 45 - 15 = 30$. Then "
            "$|A \\cap B| = 21 + 17 - 30 = 8$.",
            ["Eq(45 - 15, 30)", "Eq(21 + 17 - 30, 8)"],
        ),
        problem(
            "esh-sets-p9",
            "How many subsets of an $8$-element set contain a fixed element $a$ and have "
            "$b$ excluded, where $b \\ne a$?",
            "Two switches pinned, six free: $2^6 = 64$.",
            ["Eq(8 - 2, 6)", "Eq(2**6, 64)"],
        ),
        problem(
            "esh-sets-p10",
            "$A \\subseteq B$, $|A| = 5$, $|B| = 9$. Find $|A \\cup B|$, $|A \\cap B|$ and "
            "$|B \\setminus A|$.",
            "With $A$ inside $B$: union is $B$ ($9$), intersection is $A$ ($5$), and "
            "$|B \\setminus A| = 9 - 5 = 4$.",
            ["Eq(9 - 5, 4)"],
        ),
    ]

    test = [
        problem(
            "esh-sets-q1",
            "State $|A|$ for $A = \\{x \\in \\mathbb{Z} : -5 \\le x < 12\\}$.",
            "From $-5$ to $11$ inclusive: $11 - (-5) + 1 = 17$.",
            ["Eq(11 - (-5) + 1, 17)"],
        ),
        problem(
            "esh-sets-q2",
            "$A = \\{1,2,3,4,5\\}$, $B = \\{4,5,6,7\\}$: find $|A \\cup B| + |A \\cap B|$.",
            "$|A \\cap B| = 2$, $|A \\cup B| = 5 + 4 - 2 = 7$; the sum is $7 + 2 = 9$ — "
            "which also equals $|A| + |B|$, no accident.",
            ["Eq(5 + 4 - 2, 7)", "Eq(7 + 2, 9)", "Eq(5 + 4, 9)"],
        ),
        problem(
            "esh-sets-q3",
            "A set has $63$ proper subsets. How many elements does it have?",
            "$2^n - 1 = 63 \\Rightarrow 2^n = 64 = 2^6$, so $n = 6$.",
            ["Eq(63 + 1, 64)", "Eq(2**6, 64)"],
        ),
        problem(
            "esh-sets-q4",
            "How many subsets of $\\{1, \\ldots, 7\\}$ contain the element $7$?",
            "Pin $7$ in; six free choices: $2^6 = 64$.",
            ["Eq(2**6, 64)"],
        ),
        problem(
            "esh-sets-q5",
            "In $U = \\{1, \\ldots, 100\\}$, how many numbers are divisible by neither $2$ nor $5$?",
            "$|A| = 50$, $|B| = 20$, multiples of $10$: $10$. Union $= 50 + 20 - 10 = 60$; "
            "neither $= 100 - 60 = 40$.",
            [
                "Eq(floor(Rational(100, 2)), 50)",
                "Eq(floor(Rational(100, 5)), 20)",
                "Eq(floor(Rational(100, 10)), 10)",
                "Eq(50 + 20 - 10, 60)",
                "Eq(100 - 60, 40)",
            ],
        ),
        problem(
            "esh-sets-q6",
            "$|U| = 36$, $|A \\cap B| = 7$. How many elements are in $A' \\cup B'$?",
            "De Morgan: $A' \\cup B' = (A \\cap B)'$, so $36 - 7 = 29$.",
            ["Eq(36 - 7, 29)"],
        ),
        problem(
            "esh-sets-q7",
            "$B \\subseteq A$, $|A| = 12$, $|A \\setminus B| = 8$. How many subsets does $B$ have?",
            "$|B| = 12 - 8 = 4$, so $B$ has $2^4 = 16$ subsets.",
            ["Eq(12 - 8, 4)", "Eq(2**4, 16)"],
        ),
    ]

    write_unit(
        "esh",
        "sets-and-operations",
        "Sets & Operations",
        1,
        "Sets, membership and subsets, the four operations, subset counting with powers "
        "of two, and De Morgan's laws — the notation the rest of the topic (and half of "
        "probability) is written in.",
        None,
        lessons,
        practice,
        test,
    )


# ===========================================================================
# Unit 2 — Venn Diagrams & Counting
# ===========================================================================

def build_venn_diagrams():
    # Region values for the three-set survey, used by lessons 3-4. Aggregates
    # are DERIVED here so the statements and checks cannot disagree.
    a_only, b_only, c_only = 9, 6, 5
    ab, ac, bc, abc = 4, 3, 2, 1
    neither3 = 10
    A3 = a_only + ab + ac + abc          # 17
    B3 = b_only + ab + bc + abc          # 13
    C3 = c_only + ac + bc + abc          # 11
    AB3, AC3, BC3 = ab + abc, ac + abc, bc + abc   # pairwise totals incl. center
    union3 = a_only + b_only + c_only + ab + ac + bc + abc  # 30
    total3 = union3 + neither3           # 40
    exactly_one = a_only + b_only + c_only          # 20
    exactly_two = ab + ac + bc                      # 9

    lessons = []

    # --- Lesson 1: Reading a two-set Venn ----------------------------------
    lessons.append(lesson(
        slug="reading-a-two-set-venn",
        title="The Four Regions of a Two-Set Venn",
        concrete=(
            "Two overlapping spotlights on a stage: lit by the left only, the "
            "right only, both beams, or standing in the dark. Every person is in "
            "exactly one of those four zones — that's the whole diagram."
        ),
        objective=(
            "Decompose two-set problems into the four disjoint regions (only-A, "
            "both, only-B, neither) and move between region counts and set counts."
        ),
        concept=[
            "A two-set Venn diagram splits the universe into four **disjoint** regions: "
            "only-$A$, the overlap $A \\cap B$, only-$B$, and neither. Disjoint means the "
            "region counts simply ADD — that is the diagram's entire power.",
            "Set totals are region sums: $|A| = \\text{only-}A + \\text{both}$, so "
            "$\\text{only-}A = |A| - |A \\cap B|$. Fill the overlap FIRST, then the "
            "onlies, then whatever is left is 'neither'.",
            "Every exam phrase maps to regions: 'only algebra' (one region), 'both' "
            "(the overlap), 'at least one' (three regions), 'neither' (the outside).",
        ],
        key_idea=(
            "Four disjoint regions, filled from the overlap outward. Region counts "
            "add; set counts are region sums."
        ),
        facts=[
            fact(
                "Region decomposition",
                "|A| = |A \\text{ only}| + |A \\cap B|",
                "A set total is its exclusive region plus the overlap.",
            ),
            fact(
                "Everything accounted",
                "|U| = \\text{only-}A + \\text{both} + \\text{only-}B + \\text{neither}",
                "The four regions tile the universe — their counts must sum to it.",
            ),
        ],
        worked=[
            problem(
                "esh-venn-l1-we1",
                "In a class of $30$, $18$ play basketball, $14$ play volleyball, $8$ play both. "
                "Fill the four regions.",
                "Overlap first: both $= 8$. Only basketball: $18 - 8 = 10$; only volleyball: "
                "$14 - 8 = 6$. Accounted for: $10 + 8 + 6 = 24$; neither: $30 - 24 = 6$.",
                ["Eq(18 - 8, 10)", "Eq(14 - 8, 6)", "Eq(10 + 8 + 6, 24)", "Eq(30 - 24, 6)"],
            ),
            problem(
                "esh-venn-l1-we2",
                "Of $40$ students, $12$ study only French, $9$ study both French and German, and "
                "$11$ study neither. How many study German?",
                "Regions must sum to $40$: only-German $= 40 - 12 - 9 - 11 = 8$. "
                "So $|G| = 8 + 9 = 17$.",
                ["Eq(40 - 12 - 9 - 11, 8)", "Eq(8 + 9, 17)"],
            ),
        ],
        mistakes=[
            mistake(
                "Filling only-$A$ with $|A|$ instead of $|A| - |A \\cap B|$.",
                "The circle's total includes the overlap. Write the overlap first and subtract.",
            ),
            mistake(
                "Forgetting the 'neither' region exists.",
                "The two circles rarely cover the whole universe — always check the leftover "
                "against $|U|$.",
            ),
        ],
        try_it=[
            problem(
                "esh-venn-l1-t1",
                "$|U| = 50$, $|A| = 27$, $|B| = 22$, both $= 13$. How many are in neither set?",
                "Only-$A$: $14$; only-$B$: $9$; total covered $14 + 13 + 9 = 36$; "
                "neither $= 50 - 36 = 14$.",
                ["Eq(27 - 13, 14)", "Eq(22 - 13, 9)", "Eq(14 + 13 + 9, 36)", "Eq(50 - 36, 14)"],
            ),
            problem(
                "esh-venn-l1-t2",
                "In a survey of $45$ people, $16$ liked tea only, $21$ liked coffee only, "
                "and everyone liked at least one of the two. How many liked both?",
                "With nobody outside, the three inner regions tile the whole group: "
                "both $= 45 - 16 - 21 = 8$.",
                ["Eq(45 - 16 - 21, 8)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The picture",
                "title": "Four zones, no double counting",
                "body": (
                    "The four regions are disjoint by construction — every person lands in "
                    "exactly one. That is why region arithmetic is plain addition, and why the "
                    "first move in ANY two-set problem is: write the overlap."
                ),
            },
            {
                "kind": "vennCounts",
                "eyebrow": "Play",
                "title": "Drag the counts, watch the totals",
                "teach": (
                    "Set the four region counts and watch $|A|$, $|B|$, the union and the "
                    "universe recompute. Notice $|A|$ changes when 'both' changes — the circle "
                    "total always includes the overlap."
                ),
                "config": {"mode": "regions", "labelA": "A", "labelB": "B",
                           "onlyA": 10, "both": 8, "onlyB": 6, "neither": 6},
            },
            {"kind": "worked", "title": "Overlap first, then outward", "problemId": "esh-venn-l1-we1"},
            tap(
                "Which region?",
                "'Students who study French only' is which part of the diagram?",
                [
                    "the French circle minus the overlap",
                    "the whole French circle",
                    "the overlap",
                    "everything outside German",
                ],
                0,
                "'Only' excludes the overlap: only-French $= |F| - |F \\cap G|$. The whole "
                "circle would include the double-bookers.",
                ["Eq(1, 1)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Working backwards to a circle", "problemId": "esh-venn-l1-we2"},
            {"kind": "tryIt", "title": "Find the outsiders", "problemId": "esh-venn-l1-t1"},
            {"kind": "tryIt", "title": "Read the stem carefully", "problemId": "esh-venn-l1-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "Four disjoint regions; counts add",
                    "Fill the overlap first; 'only' means circle minus overlap",
                    "Check the total: regions must sum to $|U|$",
                ],
            },
        ],
    ))

    # --- Lesson 2: Inclusion–exclusion, two sets ----------------------------
    lessons.append(lesson(
        slug="inclusion-exclusion",
        title="Inclusion–Exclusion for Two Sets",
        concrete=(
            "Add two guest lists and the people invited by both hosts get counted "
            "twice — so subtract them once. That correction IS the formula."
        ),
        objective=(
            "Use $|A \\cup B| = |A| + |B| - |A \\cap B|$ fluently in both directions, "
            "including solving for the overlap or a set size."
        ),
        concept=[
            "Adding $|A| + |B|$ counts the overlap twice, so "
            "$$|A \\cup B| = |A| + |B| - |A \\cap B|.$$ Four quantities, one equation — "
            "the exam gives any three and asks for the fourth.",
            "With a universal set, chain it with the complement: "
            "$|\\text{neither}| = |U| - |A \\cup B|$. Most word problems are these two "
            "lines run in sequence.",
            "Bounds questions use the same equation: the overlap is largest when one set "
            "sits inside the other ($\\min(|A|, |B|)$) and smallest when the union fills "
            "the whole universe ($|A| + |B| - |U|$, or $0$ if that is negative).",
        ],
        key_idea=(
            "$|A \\cup B| = |A| + |B| - |A \\cap B|$ — one equation, four unknowns, "
            "any three given."
        ),
        facts=[
            fact(
                "Inclusion–exclusion",
                "|A \\cup B| = |A| + |B| - |A \\cap B|",
                "Add both, subtract the double-counted overlap.",
            ),
            fact(
                "Overlap bounds",
                "|A| + |B| - |U| \\;\\le\\; |A \\cap B| \\;\\le\\; \\min(|A|, |B|)",
                "Squeeze the overlap between forced sharing and full nesting.",
            ),
        ],
        worked=[
            problem(
                "esh-venn-l2-we1",
                "In a group of $60$: $38$ have a bicycle, $27$ have a scooter, $12$ have both. "
                "How many have neither?",
                "$|A \\cup B| = 38 + 27 - 12 = 53$; neither $= 60 - 53 = 7$.",
                ["Eq(38 + 27 - 12, 53)", "Eq(60 - 53, 7)"],
            ),
            problem(
                "esh-venn-l2-we2",
                "Every one of $52$ students reads at least one of two magazines; $31$ read the "
                "first and $35$ read the second. How many read both?",
                "'At least one' means $|A \\cup B| = 52$. Solve: "
                "$|A \\cap B| = 31 + 35 - 52 = 14$.",
                ["Eq(31 + 35 - 52, 14)"],
            ),
        ],
        mistakes=[
            mistake(
                "Using $|A| + |B|$ as the union when nothing says the sets are disjoint.",
                "Only disjoint sets add cleanly. If an overlap is possible, the formula "
                "needs $- |A \\cap B|$.",
            ),
            mistake(
                "Answering an overlap larger than the smaller set.",
                "$|A \\cap B| \\le \\min(|A|, |B|)$ always — an overlap of $20$ between sets "
                "of size $15$ and $30$ is impossible. Sanity-check against the bound.",
            ),
        ],
        try_it=[
            problem(
                "esh-venn-l2-t1",
                "$|A| = 45$, $|B| = 30$, $|A \\cup B| = 63$. Find $|A \\cap B|$ and $|A \\setminus B|$.",
                "$|A \\cap B| = 45 + 30 - 63 = 12$; $|A \\setminus B| = 45 - 12 = 33$.",
                ["Eq(45 + 30 - 63, 12)", "Eq(45 - 12, 33)"],
            ),
            problem(
                "esh-venn-l2-t2",
                "In a class of $28$, everyone studies English or Russian: $19$ study English, "
                "$16$ study Russian. How many study only Russian?",
                "Both $= 19 + 16 - 28 = 7$; only Russian $= 16 - 7 = 9$.",
                ["Eq(19 + 16 - 28, 7)", "Eq(16 - 7, 9)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The correction",
                "title": "Counted twice, subtracted once",
                "body": (
                    "$|A| + |B|$ walks both circles and steps on the overlap twice. One "
                    "subtraction repairs it. Everything this lesson does is that equation, "
                    "rearranged."
                ),
            },
            {"kind": "worked", "title": "Union, then neither", "problemId": "esh-venn-l2-we1"},
            {"kind": "worked", "title": "Solving for the overlap", "problemId": "esh-venn-l2-we2"},
            tap(
                "Feasible or not",
                "$|A| = 15$, $|B| = 30$, and someone claims $|A \\cap B| = 20$. Possible?",
                ["No — the overlap cannot exceed 15", "Yes", "Only if $|U| = 45$", "Only if the sets are equal"],
                0,
                "The overlap lives inside BOTH sets, so it is at most $\\min(15, 30) = 15$. "
                "A claimed $20$ fails immediately.",
                ["Eq(Min(15, 30), 15)", "20 > 15"],
                eyebrow="Quick check",
            ),
            {"kind": "tryIt", "title": "Overlap, then difference", "problemId": "esh-venn-l2-t1"},
            {"kind": "tryIt", "title": "Everyone covered", "problemId": "esh-venn-l2-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$|A \\cup B| = |A| + |B| - |A \\cap B|$; solve for whichever is missing",
                    "Chain with $|U| - |A \\cup B|$ for 'neither'",
                    "Overlap sanity bound: never more than the smaller set",
                ],
            },
        ],
    ))

    # --- Lesson 3: Three-set Venn -------------------------------------------
    lessons.append(lesson(
        slug="three-set-venn",
        title="Three Sets, Eight Regions",
        concrete=(
            "Three spotlights make eight zones — down to the triple overlap in "
            "the middle and the darkness outside. Fill the middle first and work "
            "outward, like painting a target from the bullseye."
        ),
        objective=(
            "Fill all eight regions of a three-set diagram from given data, working "
            "from the triple overlap outward."
        ),
        concept=[
            "Three sets cut the universe into $8$ disjoint regions: three 'only' zones, "
            "three 'exactly two' zones, the triple overlap, and the outside. As before, "
            "region counts ADD.",
            "Fill order is everything: start at the **center** $|A \\cap B \\cap C|$, "
            "then peel each pairwise overlap — the 'exactly $A$ and $B$' zone is "
            "$|A \\cap B| - |A \\cap B \\cap C|$ — then the onlies, then the outside.",
            f"Example survey (used through this lesson): only-counts ${a_only}$, ${b_only}$, "
            f"${c_only}$; exactly-two zones ${ab}$, ${ac}$, ${bc}$; center ${abc}$; outside "
            f"${neither3}$. Then $|A| = {a_only} + {ab} + {ac} + {abc} = {A3}$ — a circle "
            "total is its four regions summed.",
        ],
        key_idea=(
            "Eight regions, filled center-outward. A pairwise total always CONTAINS "
            "the center — subtract it to get the 'exactly two' zone."
        ),
        facts=[
            fact(
                "Exactly-two zone",
                "|A \\cap B \\text{ only}| = |A \\cap B| - |A \\cap B \\cap C|",
                "The stated pairwise overlap includes the triple — peel it off.",
            ),
            fact(
                "Circle total",
                "|A| = \\text{only-}A + (AB\\text{ only}) + (AC\\text{ only}) + \\text{center}",
                "Each circle is exactly four regions.",
            ),
        ],
        worked=[
            problem(
                "esh-venn-l3-we1",
                f"In the survey, $|A \\cap B| = {AB3}$, $|A \\cap C| = {AC3}$, "
                f"$|B \\cap C| = {BC3}$ and $|A \\cap B \\cap C| = {abc}$. Find the three "
                "'exactly two sets' region counts.",
                f"Peel the center from each pairwise total: $AB$ only $= {AB3} - {abc} = {ab}$; "
                f"$AC$ only $= {AC3} - {abc} = {ac}$; $BC$ only $= {BC3} - {abc} = {bc}$.",
                [
                    f"Eq({AB3} - {abc}, {ab})",
                    f"Eq({AC3} - {abc}, {ac})",
                    f"Eq({BC3} - {abc}, {bc})",
                ],
            ),
            problem(
                "esh-venn-l3-we2",
                f"Continuing: $|A| = {A3}$ and the $A$-circle's overlap regions hold "
                f"${ab}$, ${ac}$ and ${abc}$ people. How many are in $A$ only, and how many "
                f"people are in the whole survey if ${neither3}$ chose none and the other "
                f"only-zones hold ${b_only}$ and ${c_only}$?",
                f"Only-$A$ $= {A3} - {ab} - {ac} - {abc} = {a_only}$. Summing all eight regions: "
                f"${a_only} + {b_only} + {c_only} + {ab} + {ac} + {bc} + {abc} + {neither3} = {total3}$.",
                [
                    f"Eq({A3} - {ab} - {ac} - {abc}, {a_only})",
                    f"Eq({a_only} + {b_only} + {c_only} + {ab} + {ac} + {bc} + {abc} + {neither3}, {total3})",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Using a stated pairwise overlap as the 'exactly two' region.",
                "$|A \\cap B|$ includes the triple overlap. The exactly-two zone is "
                "$|A \\cap B| - |A \\cap B \\cap C|$.",
            ),
            mistake(
                "Filling the circles before the center.",
                "Everything overlapping is entangled with the center — fill "
                "$|A \\cap B \\cap C|$ first or every later subtraction goes wrong.",
            ),
        ],
        try_it=[
            problem(
                "esh-venn-l3-t1",
                f"$|B| = {B3}$, with center ${abc}$, $AB$-only ${ab}$ and $BC$-only ${bc}$. "
                "How many are in $B$ only?",
                f"Only-$B$ $= {B3} - {ab} - {bc} - {abc} = {b_only}$.",
                [f"Eq({B3} - {ab} - {bc} - {abc}, {b_only})"],
            ),
            problem(
                "esh-venn-l3-t2",
                f"In the survey, how many people are in EXACTLY one set, and exactly two?",
                f"Exactly one: ${a_only} + {b_only} + {c_only} = {exactly_one}$. "
                f"Exactly two: ${ab} + {ac} + {bc} = {exactly_two}$.",
                [
                    f"Eq({a_only} + {b_only} + {c_only}, {exactly_one})",
                    f"Eq({ab} + {ac} + {bc}, {exactly_two})",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The map",
                "title": "Bullseye first",
                "body": (
                    "Eight regions sounds like chaos until you fix the fill order: center, "
                    "then the three exactly-two zones, then the onlies, then the outside. "
                    "Each step is one subtraction from something already known."
                ),
            },
            {"kind": "worked", "title": "Peeling the pairwise totals", "problemId": "esh-venn-l3-we1"},
            tap(
                "Contains the center",
                "$|A \\cap B| = 9$ and $|A \\cap B \\cap C| = 4$. People in $A$ and $B$ but NOT $C$?",
                ["$5$", "$9$", "$13$", "$4$"],
                0,
                "The pairwise total includes the center: $9 - 4 = 5$.",
                ["Eq(9 - 4, 5)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "A circle is four regions", "problemId": "esh-venn-l3-we2"},
            {"kind": "tryIt", "title": "Another circle, same peel", "problemId": "esh-venn-l3-t1"},
            {"kind": "tryIt", "title": "Exactly one, exactly two", "problemId": "esh-venn-l3-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "Fill order: center → exactly-two zones → onlies → outside",
                    "Pairwise totals contain the center; subtract to get 'exactly two'",
                    "All eight regions sum to $|U|$ — use it as the final check",
                ],
            },
        ],
    ))

    # --- Lesson 4: Inclusion–exclusion, three sets ---------------------------
    lessons.append(lesson(
        slug="three-set-inclusion-exclusion",
        title="Inclusion–Exclusion for Three Sets",
        concrete=(
            "Add three lists: pairwise sharers got counted twice, and the "
            "triple-sharers three times — then subtracting all three pairs "
            "erases the triple-sharers entirely. Add them back once. That "
            "over-and-under dance is the formula."
        ),
        objective=(
            "Apply $|A \\cup B \\cup C|$ inclusion–exclusion to survey problems, "
            "including 'at least one' and 'none' questions."
        ),
        concept=[
            "$$|A \\cup B \\cup C| = |A| + |B| + |C| - |A \\cap B| - |A \\cap C| - "
            "|B \\cap C| + |A \\cap B \\cap C|.$$ Singles added, pairs subtracted, "
            "triple added back — each element ends up counted exactly once.",
            f"On the survey data: ${A3} + {B3} + {C3} - {AB3} - {AC3} - {BC3} + {abc} = "
            f"{union3}$, matching the region sum. When the formula and the diagram "
            "disagree, the arithmetic is wrong — they are the same count.",
            "Chained with the complement, 'none of the three' is "
            "$|U| - |A \\cup B \\cup C|$ — the standard closer for survey problems.",
        ],
        key_idea=(
            "Singles $-$ pairs $+$ triple: every element counted once. 'None' is "
            "the universe minus that union."
        ),
        facts=[
            fact(
                "Three-set inclusion–exclusion",
                "|A \\cup B \\cup C| = \\Sigma|A| - \\Sigma|A \\cap B| + |A \\cap B \\cap C|",
                "Add singles, subtract pairs, add the triple back.",
            ),
            fact(
                "None of the three",
                "|\\text{none}| = |U| - |A \\cup B \\cup C|",
                "The survey closer — compute the union, subtract from the total.",
            ),
        ],
        worked=[
            problem(
                "esh-venn-l4-we1",
                f"Verify the formula on the survey: $|A| = {A3}$, $|B| = {B3}$, $|C| = {C3}$, "
                f"$|A \\cap B| = {AB3}$, $|A \\cap C| = {AC3}$, $|B \\cap C| = {BC3}$, "
                f"$|A \\cap B \\cap C| = {abc}$.",
                f"${A3} + {B3} + {C3} - {AB3} - {AC3} - {BC3} + {abc} = {union3}$ — "
                f"exactly the eight-region sum minus the outside (${total3} - {neither3}$).",
                [
                    f"Eq({A3} + {B3} + {C3} - {AB3} - {AC3} - {BC3} + {abc}, {union3})",
                    f"Eq({total3} - {neither3}, {union3})",
                ],
            ),
            problem(
                "esh-venn-l4-we2",
                "Of $100$ students, $55$ like math, $44$ like physics, $35$ like chemistry; "
                "$20$ like math and physics, $15$ math and chemistry, $12$ physics and "
                "chemistry; $5$ like all three. How many like none?",
                "Union $= 55 + 44 + 35 - 20 - 15 - 12 + 5 = 92$; none $= 100 - 92 = 8$.",
                ["Eq(55 + 44 + 35 - 20 - 15 - 12 + 5, 92)", "Eq(100 - 92, 8)"],
            ),
        ],
        mistakes=[
            mistake(
                "Stopping at 'singles minus pairs' and forgetting to add the triple back.",
                "Subtracting the three pairwise overlaps removes triple-sharers three times "
                "after adding them three times — net zero. The $+|A \\cap B \\cap C|$ restores them.",
            ),
            mistake(
                "Feeding 'exactly two' zone counts into the formula's pairwise slots.",
                "The formula wants FULL pairwise overlaps (center included). Region counts "
                "belong to the diagram method — do not mix the two mid-solution.",
            ),
        ],
        try_it=[
            problem(
                "esh-venn-l4-t1",
                "$|A| = 30$, $|B| = 25$, $|C| = 20$, pairwise overlaps $10$, $8$, $6$, triple $3$. "
                "Find $|A \\cup B \\cup C|$.",
                "$30 + 25 + 20 - 10 - 8 - 6 + 3 = 54$.",
                ["Eq(30 + 25 + 20 - 10 - 8 - 6 + 3, 54)"],
            ),
            problem(
                "esh-venn-l4-t2",
                "In the previous problem, $|U| = 60$. How many elements lie outside all three sets?",
                "$60 - 54 = 6$.",
                ["Eq(60 - 54, 6)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The dance",
                "title": "Over-count, under-count, correct",
                "body": (
                    "Track one triple-sharer through the formula: added $3$ times with the "
                    "singles, removed $3$ times with the pairs, restored once at the end — "
                    "counted exactly once. The formula is bookkeeping, not magic."
                ),
            },
            {"kind": "worked", "title": "Formula meets diagram", "problemId": "esh-venn-l4-we1"},
            tap(
                "Track one person",
                "Someone belongs to $A$ and $B$ but not $C$. How many times does the formula count them?",
                ["once", "twice", "zero times", "three times"],
                0,
                "Added twice ($|A|$, $|B|$), subtracted once ($|A \\cap B|$): net $2 - 1 = 1$. "
                "Everyone nets to one — that is the proof.",
                ["Eq(2 - 1, 1)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "The classic survey", "problemId": "esh-venn-l4-we2"},
            {"kind": "tryIt", "title": "Straight application", "problemId": "esh-venn-l4-t1"},
            {"kind": "tryIt", "title": "And the outsiders", "problemId": "esh-venn-l4-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "Singles $-$ pairs $+$ triple — every element counted once",
                    "'None' $= |U| -$ union; 'at least one' $=$ the union itself",
                    "Formula uses FULL overlaps; the diagram uses exclusive regions — don't mix",
                ],
            },
        ],
    ))

    practice = [
        problem(
            "esh-venn-p1",
            "$|U| = 55$, $|A| = 31$, $|B| = 24$, $|A \\cap B| = 12$. Fill all four regions.",
            "Only-$A$: $19$; only-$B$: $12$; both: $12$; neither: $55 - 43 = 12$.",
            ["Eq(31 - 12, 19)", "Eq(24 - 12, 12)", "Eq(19 + 12 + 12, 43)", "Eq(55 - 43, 12)"],
        ),
        problem(
            "esh-venn-p2",
            "Every student passed at least one of two exams: $70\\%$ passed the first, "
            "$60\\%$ passed the second. What percent passed both?",
            "$70 + 60 - 100 = 30$ percent.",
            ["Eq(70 + 60 - 100, 30)"],
        ),
        problem(
            "esh-venn-p3",
            "$|A| = 26$, $|A \\cup B| = 41$, $|A \\cap B| = 9$. Find $|B|$.",
            "$|B| = 41 - 26 + 9 = 24$.",
            ["Eq(41 - 26 + 9, 24)"],
        ),
        problem(
            "esh-venn-p4",
            "Among $80$ people, $45$ drink tea and $38$ drink coffee; $10$ drink neither. "
            "How many drink both?",
            "Union $= 80 - 10 = 70$; both $= 45 + 38 - 70 = 13$.",
            ["Eq(80 - 10, 70)", "Eq(45 + 38 - 70, 13)"],
        ),
        problem(
            "esh-venn-p5",
            "$|A \\cap B| = 11$ with $|A \\cap B \\cap C| = 4$; $|A| = 29$ and $|A \\cap C| = 9$. "
            "How many elements are in $A$ but in neither $B$ nor $C$?",
            "Peel the $A$-circle: only-$A$ $= 29 - (11 - 4) - (9 - 4) - 4 = 29 - 7 - 5 - 4 = 13$.",
            ["Eq(11 - 4, 7)", "Eq(9 - 4, 5)", "Eq(29 - 7 - 5 - 4, 13)"],
        ),
        problem(
            "esh-venn-p6",
            "Sports survey of $90$: football $50$, basketball $40$, chess $30$; football+basketball "
            "$18$, football+chess $14$, basketball+chess $10$; all three $6$. How many play nothing?",
            "Union $= 50 + 40 + 30 - 18 - 14 - 10 + 6 = 84$; none $= 90 - 84 = 6$.",
            ["Eq(50 + 40 + 30 - 18 - 14 - 10 + 6, 84)", "Eq(90 - 84, 6)"],
        ),
        problem(
            "esh-venn-p7",
            "In the survey of the previous problem, how many play EXACTLY two sports?",
            "Each pairwise total loses the triple: $(18-6) + (14-6) + (10-6) = 12 + 8 + 4 = 24$.",
            ["Eq(18 - 6, 12)", "Eq(14 - 6, 8)", "Eq(10 - 6, 4)", "Eq(12 + 8 + 4, 24)"],
        ),
        problem(
            "esh-venn-p8",
            "$|A| = 17$, $|B| = 13$, $|U| = 25$. What are the smallest and largest possible "
            "values of $|A \\cap B|$?",
            "Largest: $\\min(17, 13) = 13$. Smallest: $17 + 13 - 25 = 5$ — the sets cannot "
            "avoid sharing at least $5$ elements inside a $25$-element universe.",
            ["Eq(Min(17, 13), 13)", "Eq(17 + 13 - 25, 5)"],
        ),
        problem(
            "esh-venn-p9",
            "Of $200$ readers, $120$ read news, $90$ read sport, and $40$ read both. "
            "How many read exactly one section?",
            "Only-news $80$, only-sport $50$: exactly one $= 80 + 50 = 130$.",
            ["Eq(120 - 40, 80)", "Eq(90 - 40, 50)", "Eq(80 + 50, 130)"],
        ),
        problem(
            "esh-venn-p10",
            "Three sets have union $71$ inside $|U| = 84$; singles sum to $95$ and the triple "
            "overlap is $7$. What do the pairwise overlaps sum to?",
            "From inclusion–exclusion: $95 - \\Sigma_{\\text{pairs}} + 7 = 71$, so "
            "$\\Sigma_{\\text{pairs}} = 95 + 7 - 71 = 31$.",
            ["Eq(95 + 7 - 71, 31)"],
        ),
    ]

    test = [
        problem(
            "esh-venn-q1",
            "$|A| = 34$, $|B| = 21$, $|A \\cap B| = 8$. Find $|A \\cup B|$.",
            "$34 + 21 - 8 = 47$.",
            ["Eq(34 + 21 - 8, 47)"],
        ),
        problem(
            "esh-venn-q2",
            "In a class of $32$, $20$ like math, $15$ like physics, $4$ like neither. "
            "How many like both?",
            "Union $= 32 - 4 = 28$; both $= 20 + 15 - 28 = 7$.",
            ["Eq(32 - 4, 28)", "Eq(20 + 15 - 28, 7)"],
        ),
        problem(
            "esh-venn-q3",
            "$|A \\cap B| = 14$ and $|A \\cap B \\cap C| = 5$. How many elements are in "
            "$A$ and $B$ but not in $C$?",
            "$14 - 5 = 9$.",
            ["Eq(14 - 5, 9)"],
        ),
        problem(
            "esh-venn-q4",
            "Singles $28, 24, 19$; pairwise overlaps $9, 7, 5$; triple $2$. Find the union.",
            "$28 + 24 + 19 - 9 - 7 - 5 + 2 = 52$.",
            ["Eq(28 + 24 + 19 - 9 - 7 - 5 + 2, 52)"],
        ),
        problem(
            "esh-venn-q5",
            "With the previous data and $|U| = 60$, how many elements are in none of the sets?",
            "$60 - 52 = 8$.",
            ["Eq(60 - 52, 8)"],
        ),
        problem(
            "esh-venn-q6",
            "Of $75$ students, $40$ study English only, and $25$ study both English and German. "
            "Everyone studies at least one language. How many study German?",
            "Only-German $= 75 - 40 - 25 = 10$; $|G| = 10 + 25 = 35$.",
            ["Eq(75 - 40 - 25, 10)", "Eq(10 + 25, 35)"],
        ),
        problem(
            "esh-venn-q7",
            "$|A| = 12$ and $|B| = 20$ inside $|U| = 26$. What is the minimum possible $|A \\cap B|$?",
            "$12 + 20 - 26 = 6$ — the universe is too small for them to share less.",
            ["Eq(12 + 20 - 26, 6)"],
        ),
    ]

    write_unit(
        "esh",
        "venn-diagrams-and-counting",
        "Venn Diagrams & Counting",
        2,
        "The four regions of a two-set diagram, inclusion–exclusion in both directions, "
        "eight-region three-set diagrams filled center-outward, and the three-set formula — "
        "the survey-problem toolkit the exam returns to every year.",
        "Set operations and complements from Unit 1.",
        lessons,
        practice,
        test,
    )


# ===========================================================================
# Unit 3 — Number Sets & Intervals
# ===========================================================================

def build_number_sets_and_intervals():
    lessons = []

    # --- Lesson 1: The family of number sets --------------------------------
    lessons.append(lesson(
        slug="the-family-of-number-sets",
        title="ℕ, ℤ, ℚ, ℝ — the Nested Family",
        concrete=(
            "Russian dolls: the naturals sit inside the integers, the integers "
            "inside the rationals, the rationals inside the reals — and the "
            "irrationals are the gap between the last two dolls."
        ),
        objective=(
            "Classify numbers into $\\mathbb{N} \\subset \\mathbb{Z} \\subset "
            "\\mathbb{Q} \\subset \\mathbb{R}$, recognizing disguised members and "
            "the irrationals in the gap."
        ),
        concept=[
            "$\\mathbb{N} = \\{1, 2, 3, \\ldots\\}$, $\\mathbb{Z}$ adds zero and negatives, "
            "$\\mathbb{Q}$ is all ratios $p/q$ with $q \\ne 0$ — equivalently the decimals "
            "that terminate or repeat — and $\\mathbb{R}$ fills the line. Each is a subset "
            "of the next.",
            "The **irrationals** are $\\mathbb{R} \\setminus \\mathbb{Q}$: decimals that "
            "never terminate or repeat, like $\\sqrt{2}$ and $\\pi$. They are a set "
            "DIFFERENCE, not a fifth doll — a number is rational or irrational, never both.",
            "Exam classification items hide members in disguise: $\\sqrt{49} = 7$ is a "
            "natural number, $\\frac{18}{6} = 3$ is an integer, $0.75 = \\frac{3}{4}$ is "
            "rational. Simplify FIRST, classify second.",
        ],
        key_idea=(
            "$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$; "
            "irrational = real but not rational. Simplify before classifying."
        ),
        facts=[
            fact(
                "The chain",
                "\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}",
                "Every natural is an integer, every integer rational, every rational real.",
            ),
            fact(
                "Rational means",
                "x = \\tfrac{p}{q},\\ q \\ne 0 \\iff \\text{decimal terminates or repeats}",
                "Two equivalent tests — use whichever the number's costume invites.",
            ),
        ],
        worked=[
            problem(
                "esh-int-l1-we1",
                "Classify each: $\\sqrt{49}$, $-\\frac{12}{4}$, $0.\\overline{3}$, $\\sqrt{8}$.",
                "$\\sqrt{49} = 7 \\in \\mathbb{N}$. $-\\frac{12}{4} = -3 \\in \\mathbb{Z}$ "
                "(not $\\mathbb{N}$). $0.\\overline{3} = \\frac{1}{3} \\in \\mathbb{Q}$. "
                "$\\sqrt{8} = 2\\sqrt{2}$ is irrational — $8$ is not a perfect square.",
                ["Eq(sqrt(49), 7)", "Eq(Rational(-12, 4), -3)", "Eq(Rational(1, 3), Rational(1, 3))",
                 "Eq(sqrt(8), 2*sqrt(2))"],
            ),
            problem(
                "esh-int-l1-we2",
                "Is $\\frac{\\sqrt{50}}{\\sqrt{2}}$ rational or irrational?",
                "Simplify before judging: $\\frac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{25} = 5$ — "
                "a natural number. Irrational pieces can combine into rational results.",
                ["Eq(sqrt(50)/sqrt(2), 5)"],
            ),
        ],
        mistakes=[
            mistake(
                "Classifying $\\sqrt{49}$ as irrational because it has a root sign.",
                "Simplify first: $\\sqrt{49} = 7$. The costume is not the number.",
            ),
            mistake(
                "Calling $\\pi$ rational because $\\frac{22}{7}$ is close.",
                "$\\frac{22}{7}$ is an approximation, not an equality — $\\pi$ has no exact "
                "fraction form, which is the definition of irrational.",
            ),
        ],
        try_it=[
            problem(
                "esh-int-l1-t1",
                "Which of $\\sqrt{36}$, $\\sqrt{18}$, $-\\frac{20}{5}$, $0.121212\\ldots$ are rational?",
                "$\\sqrt{36} = 6$ ✓, $-\\frac{20}{5} = -4$ ✓, $0.\\overline{12} = \\frac{12}{99} = "
                "\\frac{4}{33}$ ✓; $\\sqrt{18} = 3\\sqrt{2}$ is irrational. Three of the four.",
                ["Eq(sqrt(36), 6)", "Eq(Rational(-20, 5), -4)",
                 "Eq(Rational(12, 99), Rational(4, 33))", "Eq(sqrt(18), 3*sqrt(2))"],
            ),
            problem(
                "esh-int-l1-t2",
                "Give the value of $\\sqrt{2} \\cdot \\sqrt{32}$ and classify it.",
                "$\\sqrt{2} \\cdot \\sqrt{32} = \\sqrt{64} = 8$ — a natural number, from two "
                "irrational factors.",
                ["Eq(sqrt(2)*sqrt(32), 8)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The dolls",
                "title": "Four nested sets, one gap",
                "body": (
                    "$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$ — "
                    "each doll fits in the next. The irrationals are not a doll: they are the "
                    "space between $\\mathbb{Q}$ and $\\mathbb{R}$, defined by NOT being rational."
                ),
            },
            {"kind": "worked", "title": "Numbers in disguise", "problemId": "esh-int-l1-we1"},
            tap(
                "Costume check",
                "Which number is irrational?",
                ["$\\sqrt{12}$", "$\\sqrt{\\frac{16}{25}}$", "$0.\\overline{7}$", "$-\\frac{35}{7}$"],
                0,
                "$\\sqrt{12} = 2\\sqrt{3}$ — $12$ is not a perfect square. The others simplify "
                "to $\\frac{4}{5}$, $\\frac{7}{9}$ and $-5$: all rational.",
                ["Eq(sqrt(12), 2*sqrt(3))", "Eq(sqrt(Rational(16, 25)), Rational(4, 5))",
                 "Eq(Rational(-35, 7), -5)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Irrational pieces, rational whole", "problemId": "esh-int-l1-we2"},
            {"kind": "tryIt", "title": "Three of four", "problemId": "esh-int-l1-t1"},
            {"kind": "tryIt", "title": "A rational product", "problemId": "esh-int-l1-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$; irrational $= \\mathbb{R} \\setminus \\mathbb{Q}$",
                    "Rational $\\iff$ terminating or repeating decimal $\\iff$ a fraction",
                    "SIMPLIFY first — roots and fractions love disguises",
                ],
            },
        ],
    ))

    # --- Lesson 2: Interval notation ----------------------------------------
    lessons.append(lesson(
        slug="interval-notation",
        title="Intervals & Their Notation",
        concrete=(
            "A bus route with stations: square bracket means the bus stops AT the "
            "station, round bracket means it passes without stopping. The route "
            "between is served either way."
        ),
        objective=(
            "Convert between inequalities, number-line pictures and interval "
            "notation, including rays to infinity."
        ),
        concept=[
            "$[a, b]$ includes both endpoints ($a \\le x \\le b$); $(a, b)$ excludes both "
            "($a < x < b$); $[a, b)$ and $(a, b]$ mix. Square bracket = endpoint in, "
            "round = out. On a number line: filled dot vs open dot.",
            "Rays use $\\infty$: $x > 3$ is $(3, \\infty)$ and $x \\le -1$ is "
            "$(-\\infty, -1]$. Infinity ALWAYS takes a round bracket — it is a direction, "
            "not a reachable endpoint. The whole line is $(-\\infty, \\infty) = \\mathbb{R}$.",
            "The length of a bounded interval is $b - a$ regardless of brackets — "
            "endpoints have zero width. But element COUNTS over the integers do depend "
            "on brackets, which is where interval work reconnects with Unit 1's counting.",
        ],
        key_idea=(
            "Square bracket = endpoint included, round = excluded; $\\infty$ is always "
            "round. Length $= b - a$ either way."
        ),
        facts=[
            fact(
                "The four bounded shapes",
                "[a,b],\\quad (a,b),\\quad [a,b),\\quad (a,b]",
                "Brackets record endpoint membership; the interior is the same.",
            ),
            fact(
                "Rays",
                "x > a \\iff (a, \\infty), \\qquad x \\le a \\iff (-\\infty, a]",
                "Infinity is a direction — never bracketed square.",
            ),
        ],
        worked=[
            problem(
                "esh-int-l2-we1",
                "Write $-3 < x \\le 7$ in interval notation and give the interval's length.",
                "Open at $-3$, closed at $7$: $(-3, 7]$. Length $= 7 - (-3) = 10$.",
                ["Eq(7 - (-3), 10)"],
            ),
            problem(
                "esh-int-l2-we2",
                "How many INTEGERS lie in $(-3, 7]$, and how many in $[-3, 7]$?",
                "$(-3, 7]$ holds $-2, \\ldots, 7$: that is $7 - (-2) + 1 = 10$ integers. "
                "Closing the left end adds $-3$ itself: $11$.",
                ["Eq(7 - (-2) + 1, 10)", "Eq(10 + 1, 11)"],
            ),
        ],
        mistakes=[
            mistake(
                "Writing $[3, \\infty]$ for $x \\ge 3$.",
                "No number equals $\\infty$, so it can never be 'included': $[3, \\infty)$.",
            ),
            mistake(
                "Thinking $(2, 5)$ and $[2, 5]$ have different lengths.",
                "Both have length $3$ — single points carry no width. Only integer COUNTS "
                "change with the brackets.",
            ),
        ],
        try_it=[
            problem(
                "esh-int-l2-t1",
                "Write $\\{x : x \\ge -4\\}$ and $\\{x : x < 6\\}$ in interval notation, and "
                "give the length of their intersection.",
                "$[-4, \\infty)$ and $(-\\infty, 6)$; intersection $[-4, 6)$ has length "
                "$6 - (-4) = 10$.",
                ["Eq(6 - (-4), 10)"],
            ),
            problem(
                "esh-int-l2-t2",
                "How many integers are in the interval $[-5, 5)$?",
                "$-5$ through $4$: $4 - (-5) + 1 = 10$.",
                ["Eq(4 - (-5) + 1, 10)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The brackets",
                "title": "Stops and pass-throughs",
                "body": (
                    "One convention carries the whole lesson: square bracket stops at the "
                    "endpoint, round bracket passes it by. Translate the inequality's $\\le$ "
                    "vs $<$ into brackets and the notation writes itself."
                ),
            },
            {"kind": "worked", "title": "Inequality to interval", "problemId": "esh-int-l2-we1"},
            tap(
                "Direction, not destination",
                "Which is the correct notation for $x \\le 4$?",
                ["$(-\\infty, 4]$", "$[-\\infty, 4]$", "$(4, -\\infty)$", "$(-\\infty, 4)$"],
                0,
                "Ray to the left, endpoint included: $(-\\infty, 4]$. Infinity is always round, "
                "and $4$ takes the square bracket because of $\\le$.",
                ["Eq(1, 1)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Counting integers inside", "problemId": "esh-int-l2-we2"},
            {"kind": "tryIt", "title": "Two rays, one overlap", "problemId": "esh-int-l2-t1"},
            {"kind": "tryIt", "title": "Half-open count", "problemId": "esh-int-l2-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$\\le, \\ge \\to$ square bracket; $<, > \\to$ round; $\\infty$ always round",
                    "Length $= b - a$, brackets irrelevant",
                    "Integer counts DO care about brackets — recount the endpoints",
                ],
            },
        ],
    ))

    # --- Lesson 3: Combining intervals --------------------------------------
    lessons.append(lesson(
        slug="combining-intervals",
        title="Intersections & Unions of Intervals",
        concrete=(
            "Two friends' free time: you can meet only when BOTH are free — the "
            "later start and the earlier end. Availability of at least one of "
            "them is the union, and it may come in two separate pieces."
        ),
        objective=(
            "Intersect and unite intervals on the number line, recognizing when a "
            "union stays in two pieces and when an intersection is empty."
        ),
        concept=[
            "**Intersection**: keep the overlap — the interval from the LARGER left "
            "endpoint to the SMALLER right endpoint: "
            "$[a, b] \\cap [c, d] = [\\max(a,c), \\min(b,d)]$, empty when "
            "$\\max(a,c) > \\min(b,d)$.",
            "**Union**: merge when the intervals touch or overlap; otherwise the union "
            "stays as two disjoint pieces written with $\\cup$. There is no simpler form "
            "of $(-\\infty, 1) \\cup (3, \\infty)$ — leaving it in pieces IS the answer.",
            "Systems of inequalities are interval intersections: $x > -2$ AND $x \\le 5$ "
            "is $(-2, 5]$. 'Or' conditions are unions. Sketching the number line before "
            "writing notation prevents nearly every error in this lesson.",
        ],
        key_idea=(
            "Intersection: $[\\max(a,c), \\min(b,d)]$, possibly empty. Union: merge "
            "if touching, else two pieces with $\\cup$."
        ),
        facts=[
            fact(
                "Interval intersection",
                "[a,b] \\cap [c,d] = [\\max(a,c), \\min(b,d)]",
                "Later start, earlier end — empty if they cross.",
            ),
            fact(
                "And vs or",
                "\\text{and} \\to \\cap, \\qquad \\text{or} \\to \\cup",
                "The same translation as Unit 1, now on the number line.",
            ),
        ],
        worked=[
            problem(
                "esh-int-l3-we1",
                "Find $[-4, 6] \\cap (1, 9]$ and its length.",
                "Later start: $\\max(-4, 1) = 1$ (open, from the round bracket); earlier end: "
                "$\\min(6, 9) = 6$ (closed). Intersection $(1, 6]$, length $6 - 1 = 5$.",
                ["Eq(Max(-4, 1), 1)", "Eq(Min(6, 9), 6)", "Eq(6 - 1, 5)"],
            ),
            problem(
                "esh-int-l3-we2",
                "Solve the system $x \\ge -1$ and $x < 4$ and $x \\ne 2$, in interval notation.",
                "The first two give $[-1, 4)$; removing the single point $2$ splits it: "
                "$[-1, 2) \\cup (2, 4)$. Lengths $2 - (-1) = 3$ and $4 - 2 = 2$ — total $5$, "
                "the original length, since a point has no width.",
                ["Eq(2 - (-1), 3)", "Eq(4 - 2, 2)", "Eq(3 + 2, 4 - (-1))"],
            ),
        ],
        mistakes=[
            mistake(
                "Merging a two-piece union into one interval: $(-\\infty,1) \\cup (3,\\infty) = (3,1)$?",
                "If the pieces do not touch, they stay separate. $(3, 1)$ is not even an "
                "interval — the union keeps its $\\cup$.",
            ),
            mistake(
                "Taking the smaller left endpoint for an intersection.",
                "Intersection starts where BOTH have started: the LARGER left endpoint. "
                "The smaller one belongs to the union.",
            ),
        ],
        try_it=[
            problem(
                "esh-int-l3-t1",
                "Find $(-\\infty, 3] \\cap (-2, \\infty)$ and the number of integers in it.",
                "Overlap: $(-2, 3]$, holding integers $-1, 0, 1, 2, 3$ — that is "
                "$3 - (-1) + 1 = 5$ of them.",
                ["Eq(3 - (-1) + 1, 5)"],
            ),
            problem(
                "esh-int-l3-t2",
                "Is $[5, 8] \\cap [9, 12]$ empty? Justify with the endpoint rule.",
                "$\\max(5, 9) = 9 > \\min(8, 12) = 8$ — the later start comes after the "
                "earlier end, so the intersection is $\\varnothing$.",
                ["Eq(Max(5, 9), 9)", "Eq(Min(8, 12), 8)", "9 > 8"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The overlap rule",
                "title": "Later start, earlier end",
                "body": (
                    "Every interval intersection is the same two comparisons: the overlap "
                    "begins at the larger left endpoint and ends at the smaller right one. "
                    "If those cross, there is no overlap at all."
                ),
            },
            {"kind": "worked", "title": "Max, min, and the brackets", "problemId": "esh-int-l3-we1"},
            tap(
                "Sketch first",
                "$(-\\infty, 2) \\cup [2, \\infty)$ equals…",
                ["$\\mathbb{R}$", "$\\varnothing$", "$(-\\infty, 2)$", "two disjoint pieces"],
                0,
                "The pieces meet exactly at $2$, which the right piece includes — together they "
                "tile the whole line: $\\mathbb{R}$.",
                ["Eq(1, 1)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "A punctured interval", "problemId": "esh-int-l3-we2"},
            {"kind": "tryIt", "title": "Two rays meet", "problemId": "esh-int-l3-t1"},
            {"kind": "tryIt", "title": "When nothing overlaps", "problemId": "esh-int-l3-t2"},
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "Intersection $= [\\max, \\min]$; crossed endpoints mean $\\varnothing$",
                    "Unions merge only when the pieces touch; otherwise keep the $\\cup$",
                    "Sketch the line first — notation second",
                ],
            },
        ],
    ))

    # --- Lesson 4: Absolute value as distance --------------------------------
    lessons.append(lesson(
        slug="absolute-value-as-distance",
        title="Absolute Value as Distance",
        concrete=(
            "A leash staked at point $a$: $|x - a| < r$ is everywhere the dog can "
            "reach — the open interval of radius $r$ around the stake. Cut the "
            "leash ($> r$) and the dog is anywhere OUTSIDE that stretch."
        ),
        objective=(
            "Translate $|x - a| < r$ and $|x - a| > r$ into intervals and unions of "
            "rays, and write a given interval as an absolute-value condition."
        ),
        concept=[
            "$|x - a|$ is the DISTANCE from $x$ to $a$. So $|x - a| < r$ collects the "
            "points within $r$ of $a$: the interval $(a - r, a + r)$. With $\\le$ the "
            "endpoints join: $[a - r, a + r]$.",
            "$|x - a| > r$ is the far side of the leash: $(-\\infty, a - r) \\cup "
            "(a + r, \\infty)$ — always TWO pieces. An absolute-value 'greater than' "
            "never collapses to a single interval.",
            "Backwards is the exam's favorite: the interval $(2, 10)$ has center "
            "$\\frac{2 + 10}{2} = 6$ and radius $\\frac{10 - 2}{2} = 4$, so it is exactly "
            "$|x - 6| < 4$. Center–radius form makes any symmetric condition one line.",
        ],
        key_idea=(
            "$|x - a| < r \\iff a - r < x < a + r$; the $>$ version is the two-ray "
            "outside. Interval $\\to$ condition via center and radius."
        ),
        facts=[
            fact(
                "Within the leash",
                "|x - a| < r \\iff x \\in (a - r,\\ a + r)",
                "Distance below $r$: the open ball around $a$.",
            ),
            fact(
                "Center and radius",
                "a = \\tfrac{p + q}{2}, \\qquad r = \\tfrac{q - p}{2}",
                "Any interval $(p, q)$ is $|x - a| < r$ with these values.",
            ),
        ],
        worked=[
            problem(
                "esh-int-l4-we1",
                "Solve $|x - 3| \\le 5$ and count the integers in the solution set.",
                "Distance from $3$ at most $5$: $[3 - 5, 3 + 5] = [-2, 8]$. "
                "Integers: $8 - (-2) + 1 = 11$.",
                ["Eq(3 - 5, -2)", "Eq(3 + 5, 8)", "Eq(8 - (-2) + 1, 11)"],
            ),
            problem(
                "esh-int-l4-we2",
                "Write the interval $(-1, 9)$ as an absolute-value inequality.",
                "Center $\\frac{-1 + 9}{2} = 4$, radius $\\frac{9 - (-1)}{2} = 5$: "
                "$|x - 4| < 5$.",
                ["Eq(Rational(-1 + 9, 2), 4)", "Eq(Rational(9 - (-1), 2), 5)"],
            ),
        ],
        mistakes=[
            mistake(
                "Solving $|x - 3| > 5$ as a single interval $(-2, 8)$.",
                "'Greater than' is the OUTSIDE: $(-\\infty, -2) \\cup (8, \\infty)$. The "
                "single interval is the $<$ case.",
            ),
            mistake(
                "Reading $|x + 2| < 3$ as centered at $+2$.",
                "$|x + 2| = |x - (-2)|$ — the center is $-2$. Rewrite the inside as "
                "$x - a$ before reading off the center.",
            ),
        ],
        try_it=[
            problem(
                "esh-int-l4-t1",
                "Solve $|x + 2| < 3$ in interval notation.",
                "Center $-2$, radius $3$: $(-2 - 3, -2 + 3) = (-5, 1)$.",
                ["Eq(-2 - 3, -5)", "Eq(-2 + 3, 1)"],
            ),
            problem(
                "esh-int-l4-t2",
                "Write $[1, 13]$ in the form $|x - a| \\le r$.",
                "Center $\\frac{1 + 13}{2} = 7$, radius $\\frac{13 - 1}{2} = 6$: "
                "$|x - 7| \\le 6$.",
                ["Eq(Rational(1 + 13, 2), 7)", "Eq(Rational(13 - 1, 2), 6)"],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "The leash",
                "title": "Distance, pictured",
                "body": (
                    "Read $|x - a|$ as 'how far $x$ is from $a$' and both inequality types "
                    "become geometry: $< r$ is the stretch within reach, $> r$ is everything "
                    "beyond it — two rays, always."
                ),
            },
            {"kind": "worked", "title": "Leash of length 5", "problemId": "esh-int-l4-we1"},
            tap(
                "Inside or outside",
                "The solution set of $|x - 6| > 2$ is…",
                [
                    "$(-\\infty, 4) \\cup (8, \\infty)$",
                    "$(4, 8)$",
                    "$[4, 8]$",
                    "$(8, \\infty)$",
                ],
                0,
                "Distance from $6$ exceeding $2$ puts $x$ beyond $4$ on the left or beyond "
                "$8$ on the right — both rays, not just one.",
                ["Eq(6 - 2, 4)", "Eq(6 + 2, 8)"],
                eyebrow="Quick check",
            ),
            {"kind": "worked", "title": "Interval to condition", "problemId": "esh-int-l4-we2"},
            {"kind": "tryIt", "title": "A shifted center", "problemId": "esh-int-l4-t1"},
            {"kind": "tryIt", "title": "Backwards, with brackets", "problemId": "esh-int-l4-t2"},
            {
                "kind": "funFact",
                "eyebrow": "Fun fact",
                "title": "The ε you will meet again",
                "body": (
                    "University analysis defines limits with exactly this lesson: "
                    "$|x - a| < \\varepsilon$ as 'within $\\varepsilon$ of $a$'. The leash "
                    "picture you built here is the mental model for all of calculus's rigor."
                ),
            },
            {
                "kind": "recap",
                "title": "What sticks",
                "points": [
                    "$|x - a| < r$: interval $(a - r, a + r)$; $\\le$ closes it",
                    "$|x - a| > r$: two rays — never one interval",
                    "Interval $\\to$ condition: center $= \\frac{p+q}{2}$, radius $= \\frac{q-p}{2}$",
                ],
            },
        ],
    ))

    practice = [
        problem(
            "esh-int-p1",
            "Classify $\\sqrt{81}$, $-\\frac{14}{2}$, $\\sqrt{20}$, $0.\\overline{45}$ as "
            "natural, integer, rational or irrational (most specific set).",
            "$\\sqrt{81} = 9 \\in \\mathbb{N}$; $-\\frac{14}{2} = -7 \\in \\mathbb{Z}$; "
            "$\\sqrt{20} = 2\\sqrt{5}$ irrational; $0.\\overline{45} = \\frac{45}{99} = "
            "\\frac{5}{11} \\in \\mathbb{Q}$.",
            ["Eq(sqrt(81), 9)", "Eq(Rational(-14, 2), -7)", "Eq(sqrt(20), 2*sqrt(5))",
             "Eq(Rational(45, 99), Rational(5, 11))"],
        ),
        problem(
            "esh-int-p2",
            "Write $-6 \\le x < 2$ in interval notation; give its length and the number of "
            "integers it contains.",
            "$[-6, 2)$; length $2 - (-6) = 8$; integers $-6$ through $1$: $1 - (-6) + 1 = 8$.",
            ["Eq(2 - (-6), 8)", "Eq(1 - (-6) + 1, 8)"],
        ),
        problem(
            "esh-int-p3",
            "Find $[-2, 5) \\cap [0, 8]$ and $[-2, 5) \\cup [0, 8]$.",
            "Intersection: $[\\max(-2,0), \\min(5,8))$ with the appropriate brackets $= [0, 5)$. "
            "The pieces overlap, so the union merges: $[-2, 8]$.",
            ["Eq(Max(-2, 0), 0)", "Eq(Min(5, 8), 5)"],
        ),
        problem(
            "esh-int-p4",
            "Solve $|x - 5| < 3$ and state how many integers satisfy it.",
            "$(2, 8)$: integers $3$ through $7$ — $7 - 3 + 1 = 5$ of them.",
            ["Eq(5 - 3, 2)", "Eq(5 + 3, 8)", "Eq(7 - 3 + 1, 5)"],
        ),
        problem(
            "esh-int-p5",
            "Solve $|x + 1| \\ge 4$ in interval notation.",
            "Center $-1$, radius $4$: outside means $(-\\infty, -5] \\cup [3, \\infty)$.",
            ["Eq(-1 - 4, -5)", "Eq(-1 + 4, 3)"],
        ),
        problem(
            "esh-int-p6",
            "Write the set $\\{x : 3 < x < 11\\}$ as an absolute-value inequality.",
            "Center $7$, radius $4$: $|x - 7| < 4$.",
            ["Eq(Rational(3 + 11, 2), 7)", "Eq(Rational(11 - 3, 2), 4)"],
        ),
        problem(
            "esh-int-p7",
            "Is $\\frac{\\sqrt{27}}{\\sqrt{3}}$ rational? Compute it.",
            "$\\sqrt{27}/\\sqrt{3} = \\sqrt{9} = 3$ — rational (in fact natural).",
            ["Eq(sqrt(27)/sqrt(3), 3)"],
        ),
        problem(
            "esh-int-p8",
            "Solve the system $x > -3$, $x \\le 6$, $x \\ne 0$ in interval notation.",
            "$(-3, 6]$ minus the point $0$: $(-3, 0) \\cup (0, 6]$.",
            ["Eq(6 - (-3), 9)"],
        ),
        problem(
            "esh-int-p9",
            "For which integer values of $x$ is $|x - 4| \\le 2$ AND $x$ even?",
            "$[2, 6]$ holds integers $2,3,4,5,6$; the even ones are $2, 4, 6$ — three values.",
            ["Eq(4 - 2, 2)", "Eq(4 + 2, 6)", "Eq(floor(Rational(6 - 2, 2)) + 1, 3)"],
        ),
        problem(
            "esh-int-p10",
            "The intervals $[a, 10]$ and $[4, 7]$ intersect in a set of length $3$. "
            "If $a \\le 4$, find the intersection.",
            "With $a \\le 4$ the overlap is $[\\max(a,4), \\min(10,7)] = [4, 7]$ — length "
            "$7 - 4 = 3$ ✓, so the intersection is $[4, 7]$ itself.",
            ["Eq(Min(10, 7), 7)", "Eq(7 - 4, 3)"],
        ),
    ]

    test = [
        problem(
            "esh-int-q1",
            "Which of $\\sqrt{64}$, $\\sqrt{40}$, $\\frac{22}{7}$, $0.1\\overline{6}$ is irrational?",
            "$\\sqrt{40} = 2\\sqrt{10}$ — the only irrational; $\\sqrt{64} = 8$, and the other "
            "two are fractions by form ($0.1\\overline{6} = \\frac{1}{6}$).",
            ["Eq(sqrt(64), 8)", "Eq(sqrt(40), 2*sqrt(10))", "Eq(Rational(1, 6), Rational(1, 6))"],
        ),
        problem(
            "esh-int-q2",
            "How many integers are in $(-4, 9]$?",
            "$-3$ through $9$: $9 - (-3) + 1 = 13$.",
            ["Eq(9 - (-3) + 1, 13)"],
        ),
        problem(
            "esh-int-q3",
            "Find $(-\\infty, 4) \\cap [-1, \\infty)$.",
            "Overlap from the later start $-1$ (closed) to the earlier end $4$ (open): $[-1, 4)$.",
            ["Eq(4 - (-1), 5)"],
        ),
        problem(
            "esh-int-q4",
            "Solve $|x - 2| \\le 7$ in interval notation.",
            "$[2 - 7, 2 + 7] = [-5, 9]$.",
            ["Eq(2 - 7, -5)", "Eq(2 + 7, 9)"],
        ),
        problem(
            "esh-int-q5",
            "Solve $|x + 3| > 1$ in interval notation.",
            "Center $-3$, radius $1$: $(-\\infty, -4) \\cup (-2, \\infty)$.",
            ["Eq(-3 - 1, -4)", "Eq(-3 + 1, -2)"],
        ),
        problem(
            "esh-int-q6",
            "Write $[-9, 1]$ in the form $|x - a| \\le r$.",
            "Center $\\frac{-9 + 1}{2} = -4$, radius $\\frac{1 - (-9)}{2} = 5$: $|x + 4| \\le 5$.",
            ["Eq(Rational(-9 + 1, 2), -4)", "Eq(Rational(1 - (-9), 2), 5)"],
        ),
        problem(
            "esh-int-q7",
            "How many integers satisfy $|x| < 6$ but NOT $|x| < 2$?",
            "$|x| < 6$: eleven integers $-5..5$. Remove $|x| < 2$'s three ($-1, 0, 1$): "
            "$11 - 3 = 8$.",
            ["Eq(5 - (-5) + 1, 11)", "Eq(1 - (-1) + 1, 3)", "Eq(11 - 3, 8)"],
        ),
    ]

    write_unit(
        "esh",
        "number-sets-and-intervals",
        "Number Sets & Intervals",
        3,
        "The nested family ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ with the irrationals in the gap, interval "
        "notation and integer counts, intersections and unions on the number line, and "
        "absolute value read as distance — the language every inequality answer is "
        "written in.",
        "Set operations and counting from Units 1–2.",
        lessons,
        practice,
        test,
    )


if __name__ == "__main__":
    build_sets_and_operations()
    build_venn_diagrams()
    build_number_sets_and_intervals()
