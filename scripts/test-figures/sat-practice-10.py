#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 10 → public/sat-figures/sat-p10-*.png

Parameter manifest only; all drawing lives in satfigs.py and every value
matches the builder's stems and verify[] blocks.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# M1 Q10 bar chart. The mean (18) and the median (16) must DIFFER — that
# separation is what the question tests, so assert it here.
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
TICKETS = [10, 14, 16, 24, 26]
assert sum(TICKETS) == 90 and sum(TICKETS) / len(TICKETS) == 18
assert sorted(TICKETS)[len(TICKETS) // 2] == 16
F.bar_chart("sat-p10-m1-q10", DAYS, TICKETS,
            "Tickets sold", 5, title="Daily ticket sales")

# M1 Q19 two-way table. The No column totals 65 with 39 seniors in it, so
# the conditional probability is 39/65 = 3/5.
CELLS = [[34, 26], [21, 39]]
assert sum(sum(r) for r in CELLS) == 120
assert CELLS[0][1] + CELLS[1][1] == 65
assert sum(CELLS[1]) == 60
F.two_way_table("sat-p10-m1-q19",
                col_heads=["Yes", "No"],
                row_heads=["Junior", "Senior"],
                cells=CELLS, title="Survey responses by class")

# M2H Q9 right triangle, drawn to scale from the exact legs. theta sits at
# the bottom-left vertex, so the leg of length 8 is adjacent to it and the
# hypotenuse is the 8-15-17 triple's 17.
LEG_ADJ, LEG_OPP = 8, 15
assert LEG_ADJ**2 + LEG_OPP**2 == 17**2
F.right_triangle("sat-p10-m2h-q09", LEG_ADJ, LEG_OPP,
                 base_label=f"${LEG_ADJ}$", height_label=f"${LEG_OPP}$",
                 theta_at="bottom-left")
