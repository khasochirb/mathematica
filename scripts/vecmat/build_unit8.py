#!/usr/bin/env python3
"""Vectors & Matrices — Unit 8: Systems in Three Unknowns.

Ministry of Education order А/492 (2019), section 11.2 "Тэгшитгэлийн систем":

  11.2г   solve a linear system in THREE unknowns by Gauss's method
  11.2д*  the determinant and the inverse of a 3x3 matrix
  11.2е*  solve a three-unknown system by Cramer's rule

Unit 6 solves 2x2 systems with the inverse matrix and Cramer's rule, and the
course stopped there. The ministry does not: three unknowns and row reduction
are core (заавал судлах) grade-11 content, and a student who has only ever met
ad − bc has no way in. This unit supplies the missing half — and it supplies
it in the order that makes the machinery inevitable rather than magical.

The unit's through-line: ELIMINATION IS BOOKKEEPING, AND THE MATRIX IS THE
BOOK. Every step of the "add a multiple of one equation to another" method
you already use for two unknowns survives verbatim in three; writing the
system as an augmented grid just stops you from re-copying the letters. Once
the grid is triangular, back-substitution reads the answer off. The 3x3
determinant then arrives as the ONE number that predicts whether all this will
work, and Cramer's rule as the shortcut it buys you.

Run: python3 scripts/vecmat/build_unit8.py   (then npm run verify:genmath)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "vectors-matrices"


def M3(rows):
    """Inline LaTeX for a 3x3 matrix (no surrounding dollars)."""
    body = r" \\ ".join(" & ".join(str(x) for x in r) for r in rows)
    return r"\begin{pmatrix} %s \end{pmatrix}" % body


def AUG(rows):
    """An augmented 3x4 grid, the vertical bar drawn with array."""
    body = r" \\ ".join(
        "%s & %s & %s & %s" % tuple(str(x) for x in r) for r in rows
    )
    return r"\left(\begin{array}{ccc|c} %s \end{array}\right)" % body


def SYS(rows):
    """A three-equation system in a cases environment. Each row is a string."""
    return r"\begin{cases} %s \end{cases}" % (r" \\ ".join(rows))


# ===========================================================================
# Lesson 1 — the augmented matrix and row operations
# ===========================================================================

L1_WORKED = [
    problem(
        "vm81-we1",
        r"Write the system $" + SYS([
            "2x + 3y - z = 7",
            "x - y + 4z = -2",
            "3x + 2z = 5",
        ]) + r"$ as an augmented matrix.",
        r"Line the unknowns up in the same order in every equation, and write a $0$ wherever an "
        r"unknown is missing — the third equation has no $y$ term. The coefficients go left of "
        r"the bar, the constants to its right: "
        r"$" + AUG([[2, 3, -1, 7], [1, -1, 4, -2], [3, 0, 2, 5]]) + r"$. Nothing has been solved "
        r"yet; the letters have simply stopped being re-copied.",
        ["2*1 + 3*0 - 1*0 == 2", "3*0 + 0*1 + 2*0 == 0", "1*(-1) == -1"],
    ),
    problem(
        "vm81-we2",
        r"Starting from $" + AUG([[1, 2, -1, 3], [2, 5, 1, 8], [0, 1, 3, 5]]) + r"$, use the "
        r"first row to clear the $x$ from the second row.",
        r"The operation is $R_2 - 2R_1$: subtract twice the first row from the second, entry by "
        r"entry. $2 - 2 \cdot 1 = 0$, $5 - 2 \cdot 2 = 1$, $1 - 2 \cdot (-1) = 3$ and "
        r"$8 - 2 \cdot 3 = 2$. The grid becomes "
        r"$" + AUG([[1, 2, -1, 3], [0, 1, 3, 2], [0, 1, 3, 5]]) + r"$. The solution set is "
        r"untouched: adding a multiple of one equation to another never gains or loses a "
        r"solution.",
        ["2 - 2*1 == 0", "5 - 2*2 == 1", "1 - 2*(-1) == 3", "8 - 2*3 == 2"],
    ),
    problem(
        "vm81-we3",
        r"Two rows of a reduced system read $" + AUG([[0, 1, 3, 2], [0, 1, 3, 5]]) + r"$. What "
        r"does the system say, and what does that mean for its solutions?",
        r"Subtracting the first of these from the second gives the row "
        r"$" + AUG([[0, 0, 0, 3]]) + r"$, which reads $0x + 0y + 0z = 3$, that is $0 = 3$. No "
        r"triple $(x; y; z)$ can satisfy it, so the system has NO solutions — the two equations "
        r"describe parallel planes. Had the last entry been $0$ instead, the row would read "
        r"$0 = 0$: a true but empty statement, meaning one equation was redundant and the "
        r"solutions form a whole line.",
        ["5 - 2 == 3", "1 - 1 == 0", "3 - 3 == 0"],
    ),
]

L1_TRY = [
    problem(
        "vm81-t1",
        r"Write $" + SYS(["x + 5z = 4", "2x - y + z = 0", "y - 3z = 6"]) + r"$ as an augmented "
        r"matrix.",
        r"Missing unknowns become zeros: "
        r"$" + AUG([[1, 0, 5, 4], [2, -1, 1, 0], [0, 1, -3, 6]]) + r"$.",
        ["1*1 + 0*1 + 5*0 == 1", "0*1 + 1*0 - 3*0 == 0", "2 - 1 + 1 == 2"],
    ),
    problem(
        "vm81-t2",
        r"Apply $R_3 - 4R_1$ to $" + AUG([[1, -2, 1, 5], [0, 3, 2, 1], [4, 1, -3, 2]]) + r"$.",
        r"Entry by entry: $4 - 4 = 0$, $1 - 4(-2) = 9$, $-3 - 4 \cdot 1 = -7$, "
        r"$2 - 4 \cdot 5 = -18$. The new grid is "
        r"$" + AUG([[1, -2, 1, 5], [0, 3, 2, 1], [0, 9, -7, -18]]) + r"$.",
        ["4 - 4*1 == 0", "1 - 4*(-2) == 9", "-3 - 4*1 == -7", "2 - 4*5 == -18"],
    ),
]

L1 = lesson(
    "augmented-matrices-and-row-operations",
    "Augmented Matrices & Row Operations",
    "Solving two equations by elimination means adding multiples of one to the other until a "
    "letter disappears. With three unknowns the same method works — but you end up copying x, y "
    "and z dozens of times. The augmented matrix is that method with the letters removed: only "
    "the numbers that actually change get written down.",
    "Write a three-unknown system as an augmented matrix, apply the three elementary row "
    "operations, and read what a row of zeros is telling you.",
    [
        r"**The grid holds the coefficients, the bar holds the constants.** The system "
        r"$" + SYS(["a_1x + b_1y + c_1z = d_1", "a_2x + b_2y + c_2z = d_2", "a_3x + b_3y + c_3z = d_3"])
        + r"$ becomes $" + AUG([["a_1", "b_1", "c_1", "d_1"], ["a_2", "b_2", "c_2", "d_2"],
                                ["a_3", "b_3", "c_3", "d_3"]]) + r"$. Line the unknowns up in "
        r"the same order in every row, and write $0$ for any that is missing.",
        r"**Three operations, and none of them changes the answer.** You may swap two rows; "
        r"multiply a row by a non-zero number; or add a multiple of one row to another. Each is "
        r"reversible, so no solution is created and none is lost — which is exactly the licence "
        r"that lets you keep changing the system until it is easy.",
        r"**A row of zeros is a message.** If elimination produces $0 \; 0 \; 0 \mid k$ with "
        r"$k \ne 0$, the system says $0 = k$ and has no solution at all. If it produces "
        r"$0 \; 0 \; 0 \mid 0$, one equation carried no new information and the solutions form "
        r"a whole line — infinitely many of them.",
    ],
    "A three-unknown system is a 3×4 grid; swap, scale and add rows freely — the solution set "
    "never changes; a zero row reports 'no solution' or 'infinitely many'.",
    [
        fact(
            "Augmented matrix",
            AUG([["a_1", "b_1", "c_1", "d_1"], ["a_2", "b_2", "c_2", "d_2"],
                 ["a_3", "b_3", "c_3", "d_3"]]),
            "Coefficients left of the bar, constants right of it, one row per equation.",
        ),
        fact(
            "The three row operations",
            r"R_i \leftrightarrow R_j, \qquad kR_i \; (k \ne 0), \qquad R_i + kR_j",
            "Swap, scale, combine — all reversible, so the solution set survives.",
        ),
        fact(
            "What a zero row says",
            r"0\;0\;0 \mid k \ne 0 \Rightarrow \varnothing, \qquad 0\;0\;0 \mid 0 \Rightarrow \infty",
            "Contradiction means no solution; a true-but-empty row means infinitely many.",
        ),
    ],
    L1_WORKED,
    [
        mistake(
            "Forgetting the zero for a missing unknown.",
            "An equation like 3x + 2z = 5 has no y, so its row is 3, 0, 2 — writing 3, 2, 5 "
            "shifts every later column and quietly solves a different system.",
        ),
        mistake(
            "Multiplying a row by zero to make an entry vanish.",
            "Scaling by zero destroys the equation — it is the one multiplier the rule forbids. "
            "To clear an entry, ADD a multiple of another row instead.",
        ),
    ],
    L1_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "Elimination, with the letters removed",
            "body": r"You already solve two equations by elimination: multiply one equation, add "
                    r"it to the other, watch a letter vanish. Three unknowns need the same moves "
                    r"but many more of them, and the letters $x$, $y$, $z$ sit in the same "
                    r"columns every single time. So write only the numbers, keep the columns "
                    r"aligned, and draw a bar where the equals signs were.",
        },
        {
            "kind": "systemGraph",
            "eyebrow": "Where you came from",
            "title": "Two unknowns, one crossing point",
            "teach": r"With two unknowns, a solution is where two lines cross, and elimination "
                     r"is the algebra that finds it. With three unknowns each equation is a "
                     r"PLANE in space, and a unique solution is the single point where all three "
                     r"meet. Parallel planes give no solution; planes sharing a whole line give "
                     r"infinitely many — the same three outcomes, one dimension up.",
            "config": {"m1": 1, "b1": -1, "m2": -2, "b2": 5, "interactive": True},
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "The missing unknown",
            "prompt": r"Which row represents the equation $4x - z = 9$?",
            "options": [
                r"$4 \;\; 0 \;\; -1 \mid 9$",
                r"$4 \;\; -1 \;\; 9 \mid 0$",
                r"$4 \;\; -1 \;\; 0 \mid 9$",
                r"$0 \;\; 4 \;\; -1 \mid 9$",
            ],
            "correctIndex": 0,
            "explanation": r"There is no $y$ term, so the middle column is $0$; the coefficient "
                           r"of $z$ is $-1$ and the constant $9$ goes past the bar.",
            "check": ["4*1 + 0*0 + (-1)*0 == 4", "4*0 + 0*1 + (-1)*0 == 0"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "System to grid", "problemId": "vm81-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "One elimination step", "problemId": "vm81-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "A row of zeros",
            "prompt": r"Elimination produces the row $0 \;\; 0 \;\; 0 \mid 6$. The system…",
            "options": [
                "has no solution",
                "has exactly one solution",
                "has infinitely many solutions",
                "needs one more equation",
            ],
            "correctIndex": 0,
            "explanation": r"The row reads $0 = 6$, which nothing can satisfy. Had the last "
                           r"entry been $0$, the row would read $0 = 0$ and the system would "
                           r"have infinitely many solutions.",
            "check": ["0*1 + 0*2 + 0*3 == 0", "Ne(0, 6)"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Reading a contradiction", "problemId": "vm81-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Name every operation as you do it",
            "body": r"Write $R_2 - 2R_1$ beside the row you are changing, before you change it. "
                    r"It costs three characters and it does two jobs: it stops you from applying "
                    r"the operation to the wrong row, and if the final answer fails to check, "
                    r"you can walk back up the page and find the exact step that broke instead "
                    r"of starting over.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Build the grid", "problemId": "vm81-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "One row operation", "problemId": "vm81-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "Two thousand years old",
            "body": "The method in this unit is named after Carl Friedrich Gauss, who used it "
                    "around 1810 — but it appears, worked out on counting rods in exactly this "
                    "rectangular-array form, in the Chinese text 'Nine Chapters on the "
                    "Mathematical Art', compiled roughly 2,000 years earlier. Chapter eight is "
                    "literally called 'Rectangular Arrays'.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"Coefficients left of the bar, constants right; a missing unknown is a $0$.",
                r"Swap, scale by a non-zero number, add a multiple — the solutions survive.",
                r"$0 = k$ means no solution; $0 = 0$ means infinitely many.",
            ],
        },
    ],
)


# ===========================================================================
# Lesson 2 — Gaussian elimination (11.2г)
# ===========================================================================

L2_WORKED = [
    problem(
        "vm82-we1",
        r"Solve $" + SYS(["x + 2y + z = 9", "2x + y - z = 3", "3x - y + 2z = 8"]) + r"$ by "
        r"Gauss's method.",
        r"Start from $" + AUG([[1, 2, 1, 9], [2, 1, -1, 3], [3, -1, 2, 8]]) + r"$. Clear the "
        r"first column with $R_2 - 2R_1$ and $R_3 - 3R_1$: "
        r"$" + AUG([[1, 2, 1, 9], [0, -3, -3, -15], [0, -7, -1, -19]]) + r"$. Simplify the "
        r"second row with $-\tfrac{1}{3}R_2$ to get $0 \;\; 1 \;\; 1 \mid 5$, then clear the "
        r"second column below it with $R_3 + 7R_2$: "
        r"$" + AUG([[1, 2, 1, 9], [0, 1, 1, 5], [0, 0, 6, 16]]) + r"$. "
        r"The grid is now triangular, so back-substitute: the last row gives "
        r"$6z = 16$, that is $z = \tfrac{8}{3}$; the second gives "
        r"$y = 5 - \tfrac{8}{3} = \tfrac{7}{3}$; the first gives "
        r"$x = 9 - 2 \cdot \tfrac{7}{3} - \tfrac{8}{3} = \tfrac{5}{3}$. Check in the third "
        r"original equation: $3 \cdot \tfrac{5}{3} - \tfrac{7}{3} + 2 \cdot \tfrac{8}{3} = 8$.",
        [
            "Eq(-7 + 7*1, 0)",
            "Eq(-1 + 7*1, 6)",
            "Eq(-19 + 7*5, 16)",
            "Eq(6*Rational(8,3), 16)",
            "Eq(5 - Rational(8,3), Rational(7,3))",
            "Eq(9 - 2*Rational(7,3) - Rational(8,3), Rational(5,3))",
            "Eq(3*Rational(5,3) - Rational(7,3) + 2*Rational(8,3), 8)",
        ],
    ),
    problem(
        "vm82-we2",
        r"Solve $" + SYS(["x + y + z = 6", "2x - y + 3z = 9", "x + 4y - z = 3"]) + r"$.",
        r"From $" + AUG([[1, 1, 1, 6], [2, -1, 3, 9], [1, 4, -1, 3]]) + r"$, apply "
        r"$R_2 - 2R_1$ and $R_3 - R_1$: "
        r"$" + AUG([[1, 1, 1, 6], [0, -3, 1, -3], [0, 3, -2, -3]]) + r"$. Now $R_3 + R_2$ "
        r"removes the second column: $0 \;\; 0 \;\; -1 \mid -6$, so $z = 6$. Back-substituting "
        r"into $-3y + z = -3$ gives $-3y = -9$, so $y = 3$; and the first equation gives "
        r"$x = 6 - 3 - 6 = -3$. Check the second original equation: "
        r"$2(-3) - 3 + 3 \cdot 6 = 9$.",
        [
            "Eq(-1 - 2, -3)", "Eq(3 - 9, -6)",
            "Eq(3 + (-3), 0)", "Eq(-2 + 1, -1)", "Eq(-3 + (-3), -6)",
            "Eq(-3*3 + 6, -3)", "Eq(-3 + 3 + 6, 6)",
            "Eq(2*(-3) - 3 + 3*6, 9)",
        ],
    ),
    problem(
        "vm82-we3",
        r"Solve $" + SYS(["x - y + 2z = 3", "2x - 2y + 4z = 7", "x + y - z = 1"]) + r"$, or show "
        r"that no solution exists.",
        r"From $" + AUG([[1, -1, 2, 3], [2, -2, 4, 7], [1, 1, -1, 1]]) + r"$, the operation "
        r"$R_2 - 2R_1$ gives the row $0 \;\; 0 \;\; 0 \mid 1$, because "
        r"$7 - 2 \cdot 3 = 1$ while every coefficient cancels. That row reads $0 = 1$, so the "
        r"system has no solution. Geometrically the first two equations describe parallel "
        r"planes: the left-hand side of the second is exactly twice the first, but the "
        r"right-hand side is not. The third equation never gets a say.",
        ["2 - 2*1 == 0", "-2 - 2*(-1) == 0", "4 - 2*2 == 0", "7 - 2*3 == 1", "Ne(1, 0)"],
    ),
]

L2_TRY = [
    problem(
        "vm82-t1",
        r"Solve $" + SYS(["x + y + z = 2", "y + 2z = 5", "3z = 9"]) + r"$ by back-substitution.",
        r"The grid is already triangular. The last equation gives $z = 3$; the second gives "
        r"$y = 5 - 6 = -1$; the first gives $x = 2 - (-1) - 3 = 0$. The solution is "
        r"$(0; -1; 3)$.",
        ["Eq(9/3, 3)", "Eq(5 - 2*3, -1)", "Eq(2 - (-1) - 3, 0)"],
    ),
    problem(
        "vm82-t2",
        r"Solve $" + SYS(["x + 2y - z = 4", "2x + 3y + z = 11", "x - y + 2z = 1"]) + r"$.",
        r"$R_2 - 2R_1$ gives $0 \;\; -1 \;\; 3 \mid 3$ and $R_3 - R_1$ gives "
        r"$0 \;\; -3 \;\; 3 \mid -3$. Then $R_3 - 3R_2$ gives $0 \;\; 0 \;\; -6 \mid -12$, so "
        r"$z = 2$. Back-substituting: $-y + 6 = 3$ gives $y = 3$, and $x = 4 - 6 + 2 = 0$. The "
        r"solution is $(0; 3; 2)$, which satisfies all three original equations.",
        [
            "Eq(3 - 2*2, -1)", "Eq(1 + 2, 3)", "Eq(11 - 2*4, 3)",
            "Eq(-3 - 3*(-1), 0)", "Eq(3 - 3*3, -6)", "Eq(-3 - 3*3, -12)",
            "Eq(-3 + 6, 3)", "Eq(0 + 2*3 - 2, 4)", "Eq(2*0 + 3*3 + 2, 11)",
            "Eq(0 - 3 + 2*2, 1)",
        ],
    ),
]

L2 = lesson(
    "gaussian-elimination",
    "Gaussian Elimination",
    "There is one method for three unknowns, and it is the one you already use for two, run "
    "twice. Clear the first column, clear the second, and the last row hands you a single "
    "unknown for free. Everything after that is substitution, walking back up the page.",
    "Solve a three-unknown linear system by forward elimination to triangular form and back "
    "substitution, and recognise systems with no solution or infinitely many.",
    [
        r"**Forward: make a staircase of zeros.** Use the first row to clear every entry below "
        r"the leading $1$ in column one, then use the second row to clear what is below it in "
        r"column two. When the grid looks like "
        r"$" + AUG([[r"\ast", r"\ast", r"\ast", r"\ast"], [0, r"\ast", r"\ast", r"\ast"],
                    [0, 0, r"\ast", r"\ast"]]) + r"$ the forward phase is finished. This shape "
        r"is called row echelon form.",
        r"**Backward: read the answer off, bottom to top.** The last row involves only $z$, so "
        r"it gives $z$ immediately. Put that into the second row, which now involves only $y$. "
        r"Put both into the first row for $x$. Substitute the triple back into an equation you "
        r"have NOT used during elimination — that is a genuine check, not a re-run of your own "
        r"arithmetic.",
        r"**Two things can go wrong, and both are informative.** A row $0\;0\;0 \mid k$ with "
        r"$k \ne 0$ means the planes miss each other: no solution. A row $0\;0\;0 \mid 0$ means "
        r"one equation was a combination of the others: a free unknown remains, and the "
        r"solutions form a line, written by setting $z = t$ and expressing $x$ and $y$ in terms "
        r"of $t$.",
    ],
    "Clear column one, then column two, then back-substitute from the bottom row; a zero row "
    "reports no solution or a free unknown.",
    [
        fact(
            "Row echelon form",
            AUG([[r"\ast", r"\ast", r"\ast", r"\ast"], [0, r"\ast", r"\ast", r"\ast"],
                 [0, 0, r"\ast", r"\ast"]]),
            "The target of the forward phase: zeros below the staircase.",
        ),
        fact(
            "The clearing move",
            r"R_i \to R_i - \frac{a_{i1}}{a_{11}} R_1",
            "Subtract the right multiple of the pivot row and the entry below the pivot dies.",
        ),
        fact(
            "Back substitution",
            r"z = \frac{d_3}{c_3}, \quad y = \frac{d_2 - c_2 z}{b_2}, \quad x = \frac{d_1 - b_1 y - c_1 z}{a_1}",
            "Bottom row first; each line has exactly one unknown left in it.",
        ),
    ],
    L2_WORKED,
    [
        mistake(
            "Applying a row operation to the coefficients but not the constant.",
            "The row past the bar is part of the equation. If you subtract 2R1 from R2, subtract "
            "it from all FOUR entries — dropping the last one silently changes the answer.",
        ),
        mistake(
            "Checking the solution in an equation you already used to find it.",
            "Substitute back into an original equation that was not the last one you "
            "manipulated. Checking against your own final row confirms nothing but that you can "
            "copy numbers.",
        ),
    ],
    L2_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "Down the staircase, then back up",
            "body": r"Gauss's method has exactly two phases and they run in opposite directions. "
                    r"Going DOWN, you destroy unknowns: the first column loses its lower "
                    r"entries, then the second, until the bottom row contains a single unknown. "
                    r"Going UP, you recover them one at a time, each row handing over its last "
                    r"unknown because everything else in it is already known.",
        },
        {
            "kind": "stepProof",
            "eyebrow": "One solve, justified",
            "title": "Every step has a reason",
            "config": {
                "given": "x + y + z = 6,  2x - y + 3z = 9,  x + 4y - z = 3",
                "prove": "x = -3, y = 3, z = 6",
                "rows": [
                    {"statement": "Write the augmented matrix (1 1 1 | 6), (2 -1 3 | 9), (1 4 -1 | 3)",
                     "reason": "The system with the letters removed — columns hold x, y, z."},
                    {"statement": "R2 - 2R1 gives (0 -3 1 | -3)",
                     "reason": "Adding a multiple of one equation to another leaves the solution set unchanged."},
                    {"statement": "R3 - R1 gives (0 3 -2 | -3)",
                     "reason": "Same operation, now clearing the last entry of column one."},
                    {"statement": "R3 + R2 gives (0 0 -1 | -6)",
                     "reason": "Column two is cleared; the grid is now triangular."},
                    {"statement": "z = 6",
                     "reason": "The bottom row reads -z = -6, an equation in one unknown."},
                    {"statement": "y = 3",
                     "reason": "Substituting z into -3y + z = -3 gives -3y = -9."},
                    {"statement": "x = -3",
                     "reason": "Substituting y and z into x + y + z = 6."},
                    {"statement": "2(-3) - 3 + 3(6) = 9",
                     "reason": "Checked against the second original equation, which was not used last."},
                ],
            },
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "Which operation clears it?",
            "prompt": r"The grid has $R_1 = 1 \;\; 2 \;\; 1 \mid 4$ and $R_2 = 3 \;\; 1 \;\; 0 \mid 5$. "
                      r"Which operation puts a $0$ in the first entry of $R_2$?",
            "options": [r"$R_2 - 3R_1$", r"$R_2 + 3R_1$", r"$R_2 - R_1$", r"$3R_2 - R_1$"],
            "correctIndex": 0,
            "explanation": r"$3 - 3 \cdot 1 = 0$. The multiplier is the entry you want to kill "
                           r"divided by the pivot above it.",
            "check": ["3 - 3*1 == 0", "1 - 3*2 == -5", "0 - 3*1 == -3", "5 - 3*4 == -7"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "A full solve", "problemId": "vm82-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "Whole-number answers", "problemId": "vm82-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "A free unknown",
            "prompt": r"Elimination ends with $0 \;\; 0 \;\; 0 \mid 0$ as the last row. The "
                      r"system has…",
            "options": [
                "infinitely many solutions",
                "no solution",
                "exactly one solution",
                "exactly two solutions",
            ],
            "correctIndex": 0,
            "explanation": r"The row says $0 = 0$, which is true but empty: one equation "
                           r"repeated information. Two independent equations in three unknowns "
                           r"leave a free unknown, so the solutions form a line.",
            "check": ["0*5 + 0*7 + 0*2 == 0", "Eq(0, 0)"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "When there is no solution", "problemId": "vm82-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Choose the row with the 1 as your pivot",
            "body": r"You are allowed to swap rows, so before eliminating anything, move a row "
                    r"whose leading coefficient is $1$ (or $-1$) to the top. Every multiplier "
                    r"below it then stays a whole number, and an exam solve that never leaves "
                    r"the integers is an exam solve you can finish in time.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Back-substitute only", "problemId": "vm82-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "A full three-unknown solve", "problemId": "vm82-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "The most-run algorithm you have never heard of",
            "body": "Weather forecasts, bridge design, medical scanners and the physics in games "
                    "all end up solving enormous linear systems — millions of unknowns rather "
                    "than three. Almost every one of them is solved by the method on this page, "
                    "reorganised for speed but unchanged in substance. It is plausibly the most "
                    "executed numerical algorithm in history.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                "Forward phase: clear column one, then column two — zeros below the staircase.",
                "Backward phase: bottom row gives one unknown; substitute upward.",
                r"$0 = k$ means no solution; $0 = 0$ means a free unknown and a line of solutions.",
            ],
        },
    ],
)


# ===========================================================================
# Lesson 3 — 3x3 determinants and inverses (11.2д)
# ===========================================================================

L3_WORKED = [
    problem(
        "vm83-we1",
        r"Compute $\det A$ for $A = " + M3([[2, -1, 3], [0, 4, 1], [5, 2, -2]]) + r"$ by "
        r"expanding along the first row.",
        r"Each entry is multiplied by the determinant of what is left when its row and column "
        r"are deleted, with the signs $+, -, +$ across the row. "
        r"$\det A = 2(4 \cdot (-2) - 1 \cdot 2) - (-1)(0 \cdot (-2) - 1 \cdot 5) "
        r"+ 3(0 \cdot 2 - 4 \cdot 5)$. The three brackets are $-10$, $-5$ and $-20$, so "
        r"$\det A = 2(-10) + 1(-5) + 3(-20) = -20 - 5 - 60 = -85$.",
        [
            "4*(-2) - 1*2 == -10", "0*(-2) - 1*5 == -5", "0*2 - 4*5 == -20",
            "2*(-10) - (-1)*(-5) + 3*(-20) == -85",
        ],
    ),
    problem(
        "vm83-we2",
        r"Expand $\det B$ for $B = " + M3([[3, 0, 0], [7, -2, 5], [1, 6, 4]]) + r"$ along the "
        r"row or column that makes the work smallest.",
        r"The first row has two zeros, so expanding along it leaves a single term: "
        r"$\det B = 3\big((-2) \cdot 4 - 5 \cdot 6\big) = 3(-8 - 30) = 3(-38) = -114$. "
        r"Expanding along any other row gives the same $-114$ after three times the work — "
        r"choosing the row with the most zeros is free.",
        ["(-2)*4 - 5*6 == -38", "3*(-38) == -114"],
    ),
    problem(
        "vm83-we3",
        r"Find the inverse of $A = " + M3([[1, 0, 2], [2, -1, 3], [4, 1, 8]]) + r"$ by "
        r"row-reducing $(A \mid I)$.",
        r"Row-reduce the wide grid $" + AUG([[1, 0, 2, r"\;1\;0\;0"], [2, -1, 3, r"\;0\;1\;0"],
                                             [4, 1, 8, r"\;0\;0\;1"]]) + r"$ until the left half "
        r"becomes the identity; whatever the right half turns into is $A^{-1}$. Since "
        r"$\det A = 1(-8 - 3) - 0 + 2(2 + 4) = -11 + 12 = 1$, the inverse has integer entries: "
        r"$A^{-1} = " + M3([[-11, 2, 2], [-4, 0, 1], [6, -1, -1]]) + r"$. Verify one entry — the "
        r"top-left of $AA^{-1}$ is $1 \cdot (-11) + 0 \cdot (-4) + 2 \cdot 6 = 1$, as the "
        r"identity requires.",
        [
            "1*(-1*8 - 3*1) - 0*(2*8 - 3*4) + 2*(2*1 - (-1)*4) == 1",
            "1*(-11) + 0*(-4) + 2*6 == 1",
            "1*2 + 0*0 + 2*(-1) == 0",
            "2*(-11) + (-1)*(-4) + 3*6 == 0",
            "4*(-11) + 1*(-4) + 8*6 == 0",
            "4*2 + 1*0 + 8*(-1) == 0",
            "4*2 + 1*1 + 8*(-1) == 1",
        ],
    ),
]

L3_TRY = [
    problem(
        "vm83-t1",
        r"Compute $\det " + M3([[1, 2, 3], [0, -1, 4], [0, 0, 5]]) + r"$.",
        r"Expand down the first column: only the top entry survives, giving "
        r"$1\big((-1) \cdot 5 - 4 \cdot 0\big) = -5$. For any triangular matrix the "
        r"determinant is just the product of the diagonal entries: $1 \cdot (-1) \cdot 5 = -5$.",
        ["(-1)*5 - 4*0 == -5", "1*(-1)*5 == -5"],
    ),
    problem(
        "vm83-t2",
        r"Show that $C = " + M3([[1, 2, 3], [2, 4, 6], [5, 0, 1]]) + r"$ has no inverse.",
        r"The second row is exactly twice the first, so eliminating with $R_2 - 2R_1$ produces a "
        r"row of zeros and the determinant is $0$: "
        r"$1(4 - 0) - 2(2 - 30) + 3(0 - 20) = 4 + 56 - 60 = 0$. A matrix with determinant $0$ "
        r"has no inverse.",
        ["1*(4*1 - 6*0) - 2*(2*1 - 6*5) + 3*(2*0 - 4*5) == 0", "2*1 - 4 == -2", "Eq(2*1, 2)"],
    ),
]

L3 = lesson(
    "determinants-of-3x3-matrices",
    "3x3 Determinants & Inverses",
    "For a 2x2 matrix, ad − bc answers everything: is there an inverse, does the system have one "
    "solution, how do areas scale. Three unknowns need the same single number, and it is built "
    "by breaking the 3x3 into three 2x2 pieces you already know how to handle.",
    "Compute a 3x3 determinant by expansion along a row or column, and find a 3x3 inverse by "
    "row-reducing the matrix beside the identity.",
    [
        r"**Expand along a row, in three 2x2 pieces.** Delete the row and column of an entry and "
        r"you are left with a $2 \times 2$ determinant, its MINOR. Along the first row: "
        r"$\det A = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}$ — note the alternating sign. Any "
        r"row or column may be used and all give the same number, so choose the one with the "
        r"most zeros.",
        r"**The determinant is still the yes-or-no.** $\det A \ne 0$ means $A$ has an inverse "
        r"and the system $AX = B$ has exactly one solution. $\det A = 0$ means the three planes "
        r"fail to meet in a single point — no solution or infinitely many — and no inverse "
        r"exists. In space, $|\det A|$ is the factor by which volumes are scaled.",
        r"**Invert by row-reducing beside the identity.** Write $(A \mid I)$ as a wide grid and "
        r"run the row operations of Lesson 2 until the left half is $I$. The right half has "
        r"become $A^{-1}$, because every operation that turns $A$ into $I$ turns $I$ into "
        r"$A^{-1}$. If a row of zeros appears on the left, $\det A = 0$ and there is nothing to "
        r"find.",
    ],
    "Expand a 3×3 determinant into three 2×2 minors with signs + − +; det ≠ 0 ⇔ an inverse "
    "exists; find it by row-reducing (A | I).",
    [
        fact(
            "Expansion along the first row",
            r"\det A = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}",
            "Each minor is the 2x2 determinant left after deleting that entry's row and column.",
        ),
        fact(
            "The sign pattern",
            M3([["+", "-", "+"], ["-", "+", "-"], ["+", "-", "+"]]),
            "Alternating from the top-left; it applies to whichever row or column you expand.",
        ),
        fact(
            "Invertibility",
            r"\det A \ne 0 \iff A^{-1} \text{ exists} \iff AX = B \text{ has one solution}",
            "The same statement as in Unit 6, one size up.",
        ),
    ],
    L3_WORKED,
    [
        mistake(
            "Forgetting the minus sign on the middle term.",
            "The signs alternate + − + across the first row. Dropping the minus on the second "
            "term is the single most common 3x3 determinant error, and it is invisible in the "
            "answer — nothing else looks wrong.",
        ),
        mistake(
            "Computing a minor from the wrong four entries.",
            "Delete the whole row AND the whole column of the entry, then take what remains. "
            "For the middle entry of the top row, that leaves the four corners of the bottom "
            "two rows, not the four entries next to it.",
        ),
    ],
    L3_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "One number, three smaller determinants",
            "body": r"A $3 \times 3$ determinant is not a new formula to memorise — it is three "
                    r"copies of $ad - bc$ with signs in front. Take an entry, cross out its row "
                    r"and column, and the four survivors form a $2 \times 2$ determinant. Do "
                    r"that for the three entries of one row, attach the signs $+, -, +$, and "
                    r"add.",
        },
        {
            "kind": "conjectureTest",
            "eyebrow": "Test the claim",
            "title": "Does an inverse exist?",
            "config": {
                "conjecture": "A 3x3 matrix has an inverse exactly when its determinant is not zero.",
                "items": [
                    {"label": "diag(2, 3, 5)", "holds": True,
                     "note": "det = 30, and the inverse is diag(1/2, 1/3, 1/5)."},
                    {"label": "rows (1 2 3), (2 4 6), (5 0 1)", "holds": True,
                     "note": "Row 2 is twice row 1, so det = 0 — and indeed no inverse exists."},
                    {"label": "rows (1 0 2), (2 -1 3), (4 1 8)", "holds": True,
                     "note": "det = 1, so the inverse exists and has integer entries."},
                    {"label": "the 3x3 matrix of all ones", "holds": True,
                     "note": "Every row is identical, det = 0, no inverse."},
                ],
            },
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "The middle sign",
            "prompt": r"Expanding along the first row, the middle term of $\det A$ carries which "
                      r"sign?",
            "options": ["minus", "plus", "it depends on the entry's sign", "no sign is needed"],
            "correctIndex": 0,
            "explanation": r"The pattern is $+, -, +$ across the first row, regardless of "
                           r"whether the entry itself is positive or negative.",
            "check": ["2*(4*(-2) - 1*2) - (-1)*(0*(-2) - 1*5) + 3*(0*2 - 4*5) == -85"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Expanding along a row", "problemId": "vm83-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "Pick the row with zeros", "problemId": "vm83-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "What a zero determinant rules out",
            "prompt": r"For a $3 \times 3$ matrix $A$ with $\det A = 0$, the system $AX = B$…",
            "options": [
                "has no solution or infinitely many, never exactly one",
                "always has exactly one solution",
                "always has no solution",
                "always has infinitely many solutions",
            ],
            "correctIndex": 0,
            "explanation": r"A zero determinant kills uniqueness. Which of the two remaining "
                           r"cases you are in depends on $B$, and elimination is what tells you.",
            "check": ["1*(4*1 - 6*0) - 2*(2*1 - 6*5) + 3*(2*0 - 4*5) == 0"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "An inverse by row reduction", "problemId": "vm83-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Hunt for zeros before you expand",
            "body": r"You may expand along ANY row or column, and every choice gives the same "
                    r"answer. A row containing two zeros collapses the work from three minors to "
                    r"one. If no row has zeros, spend one row operation creating one — that is "
                    r"allowed as long as you only ADD a multiple of another row, which never "
                    r"changes the determinant.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "A triangular determinant", "problemId": "vm83-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "No inverse", "problemId": "vm83-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "Determinants are older than matrices",
            "body": "The determinant was studied for well over a century before anyone thought "
                    "of the matrix as an object in its own right — Seki in Japan and Leibniz in "
                    "Europe both wrote determinants down in the 1680s, while the word 'matrix' "
                    "waits until Sylvester in 1850. The number came first; the grid it belongs "
                    "to was invented afterwards to explain it.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"Expand into three $2 \times 2$ minors with signs $+, -, +$.",
                "Any row or column works — pick the one with the most zeros.",
                r"$\det \ne 0$ means invertible; find the inverse by row-reducing $(A \mid I)$.",
            ],
        },
    ],
)


# ===========================================================================
# Lesson 4 — Cramer's rule in three unknowns (11.2е)
# ===========================================================================

L4_WORKED = [
    problem(
        "vm84-we1",
        r"Solve $" + SYS(["2x + y - z = 5", "x - y + 2z = 3", "3x + 2y + z = 14"]) + r"$ by "
        r"Cramer's rule.",
        r"The coefficient determinant is "
        r"$D = \det " + M3([[2, 1, -1], [1, -1, 2], [3, 2, 1]]) + r" = 2(-1 - 4) - 1(1 - 6) "
        r"- 1(2 + 3) = -10 + 5 - 5 = -10$. Since $D \ne 0$ there is exactly one solution. "
        r"Replacing the first column by the constants gives "
        r"$D_x = \det " + M3([[5, 1, -1], [3, -1, 2], [14, 2, 1]]) + r" = -25 + 25 - 20 = -20$; "
        r"replacing the second column instead gives $D_y = -30$, and the third gives "
        r"$D_z = -20$. Then $x = \tfrac{-20}{-10} = 2$, $y = \tfrac{-30}{-10} = 3$ and "
        r"$z = \tfrac{-20}{-10} = 2$. Check the third equation: "
        r"$3 \cdot 2 + 2 \cdot 3 + 2 = 14$.",
        [
            "2*(-1*1 - 2*2) - 1*(1*1 - 2*3) + (-1)*(1*2 - (-1)*3) == -10",
            "5*(-1*1 - 2*2) - 1*(3*1 - 2*14) + (-1)*(3*2 - (-1)*14) == -20",
            "2*(3*1 - 2*14) - 5*(1*1 - 2*3) + (-1)*(1*14 - 3*3) == -30",
            "2*(-1*14 - 3*2) - 1*(1*14 - 3*3) + 5*(1*2 - (-1)*3) == -20",
            "Eq(Rational(-20, -10), 2)", "Eq(Rational(-30, -10), 3)",
            "Eq(3*2 + 2*3 + 2, 14)",
        ],
    ),
    problem(
        "vm84-we2",
        r"For $" + SYS(["x + 2y + z = 4", "2x - y + 3z = 1", "3x + y + 4z = 5"]) + r"$, compute "
        r"the coefficient determinant and say what Cramer's rule can and cannot tell you.",
        r"$D = \det " + M3([[1, 2, 1], [2, -1, 3], [3, 1, 4]]) + r" = 1(-4 - 3) - 2(8 - 9) "
        r"+ 1(2 + 3) = -7 + 2 + 5 = 0$. With $D = 0$ every quotient in Cramer's rule would "
        r"divide by zero, so the rule says nothing at all — it does not say 'no solution'. "
        r"Elimination settles it: the third equation is the sum of the first two, since "
        r"$4 + 1 = 5$ matches, so the system has infinitely many solutions along a line.",
        [
            "1*(-1*4 - 3*1) - 2*(2*4 - 3*3) + 1*(2*1 - (-1)*3) == 0",
            "Eq(1 + 2, 3)", "Eq(2 + (-1), 1)", "Eq(1 + 3, 4)", "Eq(4 + 1, 5)",
        ],
    ),
    problem(
        "vm84-we3",
        r"Find only $z$ for the system $" + SYS(["x + y + z = 6", "2x - y + z = 3", "x + 2y - z = 2"])
        + r"$.",
        r"Cramer's rule earns its place here: one unknown means two determinants, not a full "
        r"elimination. $D = \det " + M3([[1, 1, 1], [2, -1, 1], [1, 2, -1]]) + r" "
        r"= 1(1 - 2) - 1(-2 - 1) + 1(4 + 1) = -1 + 3 + 5 = 7$, and replacing the THIRD column "
        r"by the constants gives "
        r"$D_z = \det " + M3([[1, 1, 6], [2, -1, 3], [1, 2, 2]]) + r" = 1(-2 - 6) - 1(4 - 3) "
        r"+ 6(4 + 1) = -8 - 1 + 30 = 21$. So $z = \tfrac{21}{7} = 3$, found without ever "
        r"computing $x$ or $y$.",
        [
            "1*(-1*(-1) - 1*2) - 1*(2*(-1) - 1*1) + 1*(2*2 - (-1)*1) == 7",
            "1*(-1*2 - 3*2) - 1*(2*2 - 3*1) + 6*(2*2 - (-1)*1) == 21",
            "Eq(Rational(21, 7), 3)",
        ],
    ),
]

L4_TRY = [
    problem(
        "vm84-t1",
        r"A system has $D = 5$, $D_x = 15$, $D_y = -10$ and $D_z = 20$. Write its solution.",
        r"Divide each by $D$: $x = 3$, $y = -2$, $z = 4$.",
        ["Eq(Rational(15,5), 3)", "Eq(Rational(-10,5), -2)", "Eq(Rational(20,5), 4)"],
    ),
    problem(
        "vm84-t2",
        r"Solve $" + SYS(["x + y = 3", "y + z = 5", "x + z = 4"]) + r"$ by Cramer's rule.",
        r"Written with all three unknowns, the matrix is $" + M3([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
        + r"$, so $D = 1(1 - 0) - 1(0 - 1) + 0 = 2$. Replacing columns by the constants "
        r"$(3; 5; 4)$ gives $D_x = 2$, $D_y = 4$ and $D_z = 6$, hence $x = 1$, $y = 2$, "
        r"$z = 3$. All three original equations check.",
        [
            "1*(1*1 - 1*0) - 1*(0*1 - 1*1) + 0*(0*0 - 1*1) == 2",
            "3*(1*1 - 1*0) - 1*(5*1 - 1*4) + 0*(5*0 - 1*4) == 2",
            "1*(5*1 - 1*4) - 3*(0*1 - 1*1) + 0*(0*4 - 5*1) == 4",
            "1*(1*4 - 5*0) - 1*(0*4 - 5*1) + 3*(0*0 - 1*1) == 6",
            "Eq(1 + 2, 3)", "Eq(2 + 3, 5)", "Eq(1 + 3, 4)",
        ],
    ),
]

L4 = lesson(
    "cramers-rule-in-three-unknowns",
    "Cramer's Rule in Three Unknowns",
    "Unit 6 solved two equations with two determinants. The same trick scales: four determinants "
    "and three divisions solve three equations, with no elimination at all — and if the question "
    "asks for only one of the unknowns, you compute exactly two determinants and stop.",
    "Solve a three-unknown system with Cramer's rule, and know precisely when the rule applies "
    "and when elimination is the only way through.",
    [
        r"**Four determinants, three divisions.** Let $D$ be the determinant of the coefficient "
        r"matrix, and let $D_x$, $D_y$, $D_z$ be what you get by replacing the corresponding "
        r"COLUMN with the column of constants. Then $x = \tfrac{D_x}{D}$, "
        r"$y = \tfrac{D_y}{D}$, $z = \tfrac{D_z}{D}$.",
        r"**The rule needs a non-zero denominator.** If $D = 0$, every quotient is undefined and Cramer's "
        r"rule reports nothing — not 'no solution', simply nothing. Go back to elimination, "
        r"which distinguishes the empty case from the infinite one.",
        r"**Choose the tool the question rewards.** Cramer is unbeatable when only one unknown is "
        r"wanted, or when the coefficients are letters rather than numbers. Elimination wins "
        r"when all three unknowns are wanted, when $D$ might be $0$, and whenever the numbers "
        r"are large — four $3 \times 3$ determinants is a lot of arithmetic to keep clean.",
    ],
    "x = Dx/D, y = Dy/D, z = Dz/D, where Dx replaces the x-column with the constants — and only "
    "when D ≠ 0.",
    [
        fact(
            "Cramer's rule",
            r"x = \frac{D_x}{D}, \qquad y = \frac{D_y}{D}, \qquad z = \frac{D_z}{D}",
            "Valid exactly when D, the coefficient determinant, is non-zero.",
        ),
        fact(
            "Building D_x",
            M3([["d_1", "b_1", "c_1"], ["d_2", "b_2", "c_2"], ["d_3", "b_3", "c_3"]]),
            "The x-column is replaced by the constants; the other two columns are untouched.",
        ),
        fact(
            "When D = 0",
            r"D = 0 \Rightarrow \text{no unique solution; use elimination}",
            "The rule is silent, not negative — elimination decides between none and infinitely many.",
        ),
    ],
    L4_WORKED,
    [
        mistake(
            "Replacing a row instead of a column.",
            "D_x replaces the x-COLUMN with the constants. Swapping a row in instead produces a "
            "different determinant and a wrong answer that still looks plausible.",
        ),
        mistake(
            "Reading D = 0 as 'no solution'.",
            "It means the rule cannot be used. The system may have no solution or infinitely "
            "many — only elimination tells you which.",
        ),
    ],
    L4_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "The same rule, one size up",
            "body": r"In Unit 6 you solved a $2 \times 2$ system as $x = \tfrac{D_x}{D}$, "
                    r"$y = \tfrac{D_y}{D}$. Absolutely nothing changes for three unknowns except "
                    r"that the determinants are $3 \times 3$ and there is a third quotient. The "
                    r"pattern is worth trusting: replace the column belonging to the unknown you "
                    r"want, and divide.",
        },
        {
            "kind": "teach",
            "eyebrow": "Two tools, one decision",
            "title": "Gauss or Cramer?",
            "body": r"Both methods are correct whenever $D \ne 0$, so the choice is about "
                    r"effort. Want all three unknowns with ugly coefficients? Eliminate — you "
                    r"handle each number once. Want $z$ alone, or are the coefficients letters "
                    r"like $a$ and $k$? Cramer — two determinants and a division. Suspect "
                    r"$D = 0$? You have no choice: eliminate.",
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "Which column moves?",
            "prompt": r"To find $y$ by Cramer's rule, you replace…",
            "options": [
                "the second column with the constants",
                "the second row with the constants",
                "the first column with the constants",
                "the whole matrix with the constants",
            ],
            "correctIndex": 0,
            "explanation": r"$y$ owns the second column, so that is the one the constants take "
                           r"over; the other two columns stay exactly as they were.",
            "check": ["2*(3*1 - 2*14) - 5*(1*1 - 2*3) + (-1)*(1*14 - 3*3) == -30"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "A full Cramer solve", "problemId": "vm84-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "When D is zero", "problemId": "vm84-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "D = 0",
            "prompt": r"A three-unknown system has $D = 0$ and $D_x = 7$. What follows?",
            "options": [
                "Cramer's rule does not apply; use elimination",
                r"$x = 0$",
                "the system has exactly one solution",
                "the system has infinitely many solutions",
            ],
            "correctIndex": 0,
            "explanation": r"Dividing by $D = 0$ is undefined, so the rule is silent. Only "
                           r"elimination can decide between no solution and infinitely many.",
            "check": ["1*(-1*4 - 3*1) - 2*(2*4 - 3*3) + 1*(2*1 - (-1)*3) == 0"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "One unknown only", "problemId": "vm84-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Compute D first, always",
            "body": r"Before writing a single other determinant, compute $D$. If it is zero you "
                    r"have saved yourself three pointless $3 \times 3$ expansions and you know "
                    r"to switch to elimination. If it is non-zero you also have the denominator "
                    r"of all three answers already in hand.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "From determinants to answers", "problemId": "vm84-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "A symmetric system", "problemId": "vm84-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "Beautiful, and hopeless at scale",
            "body": "Cramer's rule is a closed formula — the answer written out in one line — "
                    "which makes it perfect for proofs and for systems with letters in them. As "
                    "a computational method it is a disaster: solving 20 equations this way, "
                    "expanding determinants naively, would need more arithmetic than there are "
                    "seconds in the age of the universe, while elimination finishes in a few "
                    "thousand steps.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"$x = D_x/D$, $y = D_y/D$, $z = D_z/D$ — replace that unknown's column.",
                r"$D = 0$ means the rule is silent; elimination decides.",
                "Cramer for one unknown or for letters; elimination for everything else.",
            ],
        },
    ],
)


# ===========================================================================
# Practice & test
# ===========================================================================

PRACTICE = [
    problem(
        "vm8-pr-1",
        r"Write $" + SYS(["3x - y + 2z = 5", "x + 4z = 1", "2x + 5y - z = 0"]) + r"$ as an "
        r"augmented matrix.",
        r"The second equation has no $y$: "
        r"$" + AUG([[3, -1, 2, 5], [1, 0, 4, 1], [2, 5, -1, 0]]) + r"$.",
        ["3*1 - 1*0 + 2*0 == 3", "1*1 + 0*1 + 4*0 == 1", "2 + 5 - 1 == 6"],
    ),
    problem(
        "vm8-pr-2",
        r"Apply $R_2 - 3R_1$ to the rows $R_1 = 1 \;\; -2 \;\; 4 \mid 2$ and "
        r"$R_2 = 3 \;\; 1 \;\; -5 \mid 7$.",
        r"Entry by entry: $3 - 3 = 0$, $1 - 3(-2) = 7$, $-5 - 12 = -17$, $7 - 6 = 1$. The new "
        r"row is $0 \;\; 7 \;\; -17 \mid 1$.",
        ["3 - 3*1 == 0", "1 - 3*(-2) == 7", "-5 - 3*4 == -17", "7 - 3*2 == 1"],
    ),
    problem(
        "vm8-pr-3",
        r"Solve $" + SYS(["x + y + z = 4", "2y - z = 1", "4z = 8"]) + r"$ by back-substitution.",
        r"$z = 2$ from the last equation; then $2y - 2 = 1$ gives $y = \tfrac{3}{2}$; then "
        r"$x = 4 - \tfrac{3}{2} - 2 = \tfrac{1}{2}$.",
        ["Eq(8/4, 2)", "Eq(Rational(1+2, 2), Rational(3,2))",
         "Eq(4 - Rational(3,2) - 2, Rational(1,2))"],
    ),
    problem(
        "vm8-pr-4",
        r"Solve $" + SYS(["x + 2y - z = 3", "2x - y + z = 3", "x - y + 2z = 4"]) + r"$ by "
        r"Gauss's method.",
        r"$R_2 - 2R_1$ gives $0 \;\; -5 \;\; 3 \mid -3$ and $R_3 - R_1$ gives "
        r"$0 \;\; -3 \;\; 3 \mid 1$. Then $5R_3 - 3R_2$ gives $0 \;\; 0 \;\; 6 \mid 14$, so "
        r"$z = \tfrac{7}{3}$. Back-substituting: $-5y + 7 = -3$ gives $y = 2$, and "
        r"$x = 3 - 4 + \tfrac{7}{3} = \tfrac{4}{3}$.",
        ["Eq(-1 - 2*2, -5)", "Eq(1 + 1, 2)", "Eq(3 - 2*3, -3)",
         "Eq(5*(-3) - 3*(-5), 0)", "Eq(5*3 - 3*3, 6)", "Eq(5*1 - 3*(-3), 14)",
         "Eq(Rational(14,6), Rational(7,3))", "Eq(-5*2 + 3*Rational(7,3), -3)",
         "Eq(Rational(4,3) + 2*2 - Rational(7,3), 3)"],
    ),
    problem(
        "vm8-pr-5",
        r"Compute $\det " + M3([[1, 2, 0], [3, -1, 4], [2, 0, 5]]) + r"$.",
        r"Expanding along the first row: $1(-5 - 0) - 2(15 - 8) + 0 = -5 - 14 = -19$.",
        ["-1*5 - 4*0 == -5", "3*5 - 4*2 == 7", "1*(-5) - 2*7 + 0 == -19"],
    ),
    problem(
        "vm8-pr-6",
        r"Show that $" + M3([[2, 4, 6], [1, 2, 3], [5, 1, 0]]) + r"$ has determinant $0$, and say "
        r"what that means for its inverse.",
        r"The first row is twice the second, so the determinant vanishes: "
        r"$2(0 - 3) - 4(0 - 15) + 6(1 - 10) = -6 + 60 - 54 = 0$. A matrix with determinant $0$ "
        r"has no inverse.",
        ["2*(2*0 - 3*1) - 4*(1*0 - 3*5) + 6*(1*1 - 2*5) == 0", "Eq(2*1, 2)", "Eq(2*3, 6)"],
    ),
    problem(
        "vm8-pr-7",
        r"A system has coefficient determinant $D = -4$, and $D_x = 8$, $D_y = -4$, $D_z = 12$. "
        r"Write its solution.",
        r"$x = \tfrac{8}{-4} = -2$, $y = \tfrac{-4}{-4} = 1$, $z = \tfrac{12}{-4} = -3$.",
        ["Eq(Rational(8,-4), -2)", "Eq(Rational(-4,-4), 1)", "Eq(Rational(12,-4), -3)"],
    ),
    problem(
        "vm8-pr-8",
        r"Use Cramer's rule to find $x$ for $" + SYS(["2x + y + z = 7", "x + 2y + z = 8", "x + y + 2z = 9"]) + r"$.",
        r"$D = \det " + M3([[2, 1, 1], [1, 2, 1], [1, 1, 2]]) + r" = 2(4 - 1) - 1(2 - 1) "
        r"+ 1(1 - 2) = 6 - 1 - 1 = 4$. Replacing the first column by $(7; 8; 9)$ gives "
        r"$D_x = 7(4 - 1) - 1(16 - 9) + 1(8 - 18) = 21 - 7 - 10 = 4$, so $x = 1$.",
        ["2*(2*2 - 1*1) - 1*(1*2 - 1*1) + 1*(1*1 - 2*1) == 4",
         "7*(2*2 - 1*1) - 1*(8*2 - 1*9) + 1*(8*1 - 2*9) == 4", "Eq(Rational(4,4), 1)"],
    ),
]

TEST = [
    problem(
        "vm8-ty-1",
        r"Solve $" + SYS(["x + y - z = 2", "2x - y + z = 5", "x + 2y + z = 5"]) + r"$ by "
        r"Gauss's method, and check your answer in the third equation.",
        r"From $" + AUG([[1, 1, -1, 2], [2, -1, 1, 5], [1, 2, 1, 5]]) + r"$, "
        r"$R_2 - 2R_1$ gives $0 \;\; -3 \;\; 3 \mid 1$ and $R_3 - R_1$ gives "
        r"$0 \;\; 1 \;\; 2 \mid 3$. Then $3R_3 + R_2$ gives $0 \;\; 0 \;\; 9 \mid 10$, so "
        r"$z = \tfrac{10}{9}$. Back-substituting: $y = 3 - \tfrac{20}{9} = \tfrac{7}{9}$, and "
        r"$x = 2 - \tfrac{7}{9} + \tfrac{10}{9} = \tfrac{7}{3}$. Check in the third equation: "
        r"$\tfrac{7}{3} + \tfrac{14}{9} + \tfrac{10}{9} = 5$.",
        ["Eq(-1 - 2, -3)", "Eq(1 + 2, 3)", "Eq(5 - 2*2, 1)",
         "Eq(3*1 + (-3), 0)", "Eq(3*2 + 3, 9)", "Eq(3*3 + 1, 10)",
         "Eq(3 - 2*Rational(10,9), Rational(7,9))",
         "Eq(2 - Rational(7,9) + Rational(10,9), Rational(7,3))",
         "Eq(Rational(7,3) + 2*Rational(7,9) + Rational(10,9), 5)"],
    ),
    problem(
        "vm8-ty-2",
        r"Solve $" + SYS(["x + 3y - z = 1", "2x + 6y - 2z = 5", "x - y + z = 0"]) + r"$, or show "
        r"that it has no solution.",
        r"$R_2 - 2R_1$ produces $0 \;\; 0 \;\; 0 \mid 3$, since $5 - 2 = 3$ while every "
        r"coefficient cancels. The row reads $0 = 3$, so the system has no solution: the first "
        r"two equations describe parallel planes, and the third cannot rescue them.",
        ["2 - 2*1 == 0", "6 - 2*3 == 0", "-2 - 2*(-1) == 0", "5 - 2*1 == 3", "Ne(3, 0)"],
    ),
    problem(
        "vm8-ty-3",
        r"Compute $\det " + M3([[4, -2, 1], [3, 0, 5], [-1, 2, 2]]) + r"$, choosing an expansion "
        r"that keeps the work small.",
        r"The second row contains a zero, so expand along it with the signs $-, +, -$: "
        r"$\det = -3\big((-2) \cdot 2 - 1 \cdot 2\big) + 0 - 5\big(4 \cdot 2 - (-2)(-1)\big) "
        r"= -3(-6) - 5(6) = 18 - 30 = -12$. Expanding along the first row gives the same $-12$.",
        ["(-2)*2 - 1*2 == -6", "4*2 - (-2)*(-1) == 6", "-3*(-6) + 0 - 5*6 == -12",
         "4*(0*2 - 5*2) - (-2)*(3*2 - 5*(-1)) + 1*(3*2 - 0*(-1)) == -12"],
    ),
    problem(
        "vm8-ty-4",
        r"For which value of $k$ does $" + M3([[1, 2, 3], [2, "k", 6], [1, 1, 2]]) + r"$ fail to "
        r"have an inverse?",
        r"Expand: $\det = 1(2k - 6) - 2(4 - 6) + 3(2 - k) = 2k - 6 + 4 + 6 - 3k = 4 - k$. The "
        r"inverse fails to exist exactly when the determinant is $0$, that is $k = 4$. "
        r"Substituting back: $1(8 - 6) - 2(4 - 6) + 3(2 - 4) = 2 + 4 - 6 = 0$.",
        ["1*(2*4 - 6*1) - 2*(2*2 - 6*1) + 3*(2*1 - 4*1) == 0",
         "Eq(4 - 4, 0)", "1*(2*5 - 6*1) - 2*(2*2 - 6*1) + 3*(2*1 - 5*1) == -1"],
    ),
    problem(
        "vm8-ty-5",
        r"Solve $" + SYS(["x + y + 2z = 4", "2x - y + z = 2", "x + 2y - z = 2"]) + r"$ by "
        r"Cramer's rule.",
        r"$D = \det " + M3([[1, 1, 2], [2, -1, 1], [1, 2, -1]]) + r" = 1(1 - 2) - 1(-2 - 1) "
        r"+ 2(4 + 1) = -1 + 3 + 10 = 12$. Replacing each column in turn by the constants "
        r"$(4; 2; 2)$ gives $D_x = 12$, $D_y = 12$ and $D_z = 12$, so $x = y = z = 1$. All "
        r"three original equations check: $1 + 1 + 2 = 4$, $2 - 1 + 1 = 2$ and "
        r"$1 + 2 - 1 = 2$.",
        ["1*(-1*(-1) - 1*2) - 1*(2*(-1) - 1*1) + 2*(2*2 - (-1)*1) == 12",
         "4*(-1*(-1) - 1*2) - 1*(2*(-1) - 1*2) + 2*(2*2 - (-1)*2) == 12",
         "1*(2*(-1) - 1*2) - 4*(2*(-1) - 1*1) + 2*(2*2 - 2*1) == 12",
         "1*(-1*2 - 2*2) - 1*(2*2 - 2*1) + 4*(2*2 - (-1)*1) == 12",
         "Eq(1 + 1 + 2, 4)", "Eq(2 - 1 + 1, 2)", "Eq(1 + 2 - 1, 2)"],
    ),
    problem(
        "vm8-ty-6",
        r"A system in three unknowns has coefficient determinant $D = 0$. A student concludes "
        r"that it has no solution. Explain the error, and give a system with $D = 0$ that has "
        r"infinitely many solutions.",
        r"A zero determinant rules out a UNIQUE solution, nothing more: the three planes fail to "
        r"meet at a single point, but they may still share a whole line. Cramer's rule is simply "
        r"undefined, and only elimination decides. An example with infinitely many solutions is "
        r"$" + SYS(["x + y + z = 3", "2x + 2y + 2z = 6", "x - y = 0"]) + r"$, whose second "
        r"equation is twice the first; its determinant is "
        r"$1(0 + 2) - 1(0 - 2) + 1(-2 - 2) = 0$, and the solutions form the line "
        r"$x = y = t$, $z = 3 - 2t$.",
        ["1*(2*0 - 2*(-1)) - 1*(2*0 - 2*1) + 1*(2*(-1) - 2*1) == 0",
         "Eq(2*1, 2)", "Eq(2*3, 6)",
         "Eq(5 + 5 + (3 - 2*5), 3)", "Eq(2*5 + 2*5 + 2*(3 - 2*5), 6)", "Eq(5 - 5, 0)"],
    ),
]


write_unit(
    COURSE,
    "systems-in-three-unknowns",
    "Systems in Three Unknowns",
    8,
    "Elimination with the letters removed: augmented matrices and row operations, Gauss's "
    "method, the 3x3 determinant and inverse, and Cramer's rule for three unknowns.",
    "The 2x2 systems, determinants and inverses of Unit 6.",
    [L1, L2, L3, L4],
    PRACTICE,
    TEST,
)
