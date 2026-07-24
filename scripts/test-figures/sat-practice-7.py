#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 7 → public/sat-figures/sat-p7-*.png

Every call passes the SAME parameter values the builder script
(scripts/test-builders/sat-practice-7.py) uses in its stems and verify[]
blocks, so a figure cannot disagree with the question it illustrates.
All drawing lives in scripts/test-figures/satfigs.py.

Run AFTER the builder, then re-run the builder so satbuild.figure() reads
back the true pixel dimensions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# ── Module 1 ──────────────────────────────────────────────────────────

# Q4 linear-function table. x steps by 2 (not 1) — that is the trap the
# question tests, so the table must show it plainly.
XS, YS = [1, 3, 5, 7], [9, 17, 25, 33]
assert all((YS[i + 1] - YS[i]) / (XS[i + 1] - XS[i]) == 4 for i in range(3))
F.value_table("sat-p7-m1-q04", "$x$", XS, "$f(x)$", YS)

# Q10 two-way table for a JOINT probability. Cells sum to 80; the tool
# computes the margins so they cannot drift from these numbers.
CELLS_Q10 = [[21, 14], [18, 27]]
assert sum(sum(r) for r in CELLS_Q10) == 80
assert CELLS_Q10[1][0] == 18 and sum(CELLS_Q10[1]) == 45
assert CELLS_Q10[0][0] + CELLS_Q10[1][0] == 39
F.two_way_table("sat-p7-m1-q10",
                col_heads=["Yes", "No"],
                row_heads=["Tenth grade", "Eleventh grade"],
                cells=CELLS_Q10,
                title="Responses to the schedule survey")

# Q14 box plot: the five-number summary the IQR question reads from.
FIVE = [12, 20, 27, 38, 51]
assert FIVE[3] - FIVE[1] == 18
F.box_plot("sat-p7-m1-q14", FIVE, lo=5, hi=60, tick_step=10,
           xlabel="Value")

# ── Module 2, easier variant ──────────────────────────────────────────

# Q13 system read off a graph: the two lines must actually cross at (2, 4).
# y = 2x and y = -x + 6 both pass through it, exactly.
assert 2 * 2 == 4 and -(2) + 6 == 4
F.lines_graph("sat-p7-m2e-q13", [(2, 0), (-1, 6)], xlim=(-3, 7),
              ylim=(-3, 8), mark=(2, 4))

# Q17 two function tables for the composition f(g(4)).
F_VALS = {1: 4, 2: 6, 3: 1, 4: 5}
G_VALS = {1: 3, 2: 1, 3: 2, 4: 4}
assert F_VALS[G_VALS[4]] == 5
F.value_table("sat-p7-m2e-q17-f", "$x$", list(F_VALS),
              "$f(x)$", list(F_VALS.values()))
F.value_table("sat-p7-m2e-q17-g", "$x$", list(G_VALS),
              "$g(x)$", list(G_VALS.values()))
# The stem shows one image, so stack the two tables into a single figure.
F.stack_images("sat-p7-m2e-q17",
               ["sat-p7-m2e-q17-f", "sat-p7-m2e-q17-g"], gap=26)

# Q18 histogram whose running total first reaches 10 in the second bar.
COUNTS = [4, 7, 6, 3]
assert sum(COUNTS) == 20 and COUNTS[0] < 10 <= COUNTS[0] + COUNTS[1]
F.histogram("sat-p7-m2e-q18", starts=[0, 10, 20, 30], counts=COUNTS,
            xlabel="Commute time (minutes)", ylabel="Number of people",
            ytick_step=2)

# ── Module 2, harder variant ──────────────────────────────────────────

# Q5 two-way table for a conditional stated in the REVERSED direction:
# the condition names the pass COLUMN, not a row.
CELLS_Q5 = [[24, 16], [9, 31]]
assert sum(sum(r) for r in CELLS_Q5) == 80
assert CELLS_Q5[0][0] + CELLS_Q5[1][0] == 33 and sum(CELLS_Q5[0]) == 40
F.two_way_table("sat-p7-m2h-q05",
                col_heads=["Passed", "Failed"],
                row_heads=["Morning", "Evening"],
                cells=CELLS_Q5,
                title="Driving test results by session")

print("sat-practice-7 figures done")
