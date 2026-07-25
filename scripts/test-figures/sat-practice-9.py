#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 9 → public/sat-figures/sat-p9-*.png

Parameter manifest only; all drawing lives in satfigs.py and every value
matches the builder's stems and verify[] blocks.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# Q10 frequency table. The running total must first reach 13 (the median
# position for 25 values) in the SECOND row — that is the question.
VALS, FREQ = [1, 2, 3, 4], [5, 9, 7, 4]
assert sum(FREQ) == 25 and FREQ[0] < 13 <= FREQ[0] + FREQ[1]
F.value_table("sat-p9-m1-q10", "Siblings", VALS, "Students", FREQ)

# Q19 two-way table. The NO column totals 27, the under-40 row totals 40.
CELLS = [[22, 18], [31, 9]]
assert sum(sum(r) for r in CELLS) == 80
assert CELLS[0][1] + CELLS[1][1] == 27 and sum(CELLS[0]) == 40
F.two_way_table("sat-p9-m1-q19",
                col_heads=["Yes", "No"],
                row_heads=["Under 40", "40 or older"],
                cells=CELLS, title="Survey responses by age group")

# Q9 (module 2 hard) same-side interior angles: drawn at the true 118
# degrees so the labeled angle matches the figure.
assert 180 - 118 == 62
F.transversal("sat-p9-m2h-q09", top_label=r"$118^\circ$",
              bottom_label=r"$x^\circ$", slope_deg=62)

print("sat-practice-9 figures done")
