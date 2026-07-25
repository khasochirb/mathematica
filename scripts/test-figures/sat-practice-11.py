#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 11 → public/sat-figures/sat-p11-*.png

Parameter manifest only; all drawing lives in satfigs.py and every value
matches the builder's stems and verify[] blocks.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# M1 Q10 box plot. The IQR (18), the median (27) and the range (34) must
# be three DIFFERENT numbers — the distractors are exactly those.
FIVE = (12, 20, 27, 38, 46)
assert FIVE[3] - FIVE[1] == 18
assert FIVE[2] == 27 and FIVE[4] - FIVE[0] == 34
assert len({FIVE[3] - FIVE[1], FIVE[2], FIVE[4] - FIVE[0]}) == 3
F.box_plot("sat-p11-m1-q10", FIVE, 10, 50, 5,
           "Daily high temperature (degrees Fahrenheit)")

# M1 Q14 histogram, 10-minute bins. The question asks for the count at or
# above 20 minutes, which is the last three bars.
STARTS, COUNTS = [0, 10, 20, 30, 40], [3, 8, 11, 6, 2]
assert sum(COUNTS) == 30 and sum(COUNTS[2:]) == 19
F.histogram("sat-p11-m1-q14", STARTS, COUNTS,
            "Waiting time (minutes)", "Customers", ytick_step=2)

# M1 Q19 scatterplot with its line of best fit. The point at x = 6 must
# sit exactly 3 above the line y = 2x + 5 — that gap is the answer.
PTS = [(1, 8), (2, 8), (3, 12), (4, 12), (5, 16), (6, 20), (7, 18), (8, 22)]
SLOPE, INTERCEPT = 2, 5
_actual = dict(PTS)[6]
assert _actual - (SLOPE * 6 + INTERCEPT) == 3
F.scatter("sat-p11-m1-q19", PTS, line=(SLOPE, INTERCEPT),
          xlim=(0, 9), ylim=(0, 26), xticks=(2, 4, 6, 8),
          yticks=(5, 10, 15, 20, 25), xlabel="$x$", ylabel="$y$")
