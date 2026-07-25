#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 12 → public/sat-figures/sat-p12-*.png

Parameter manifest only; all drawing lives in satfigs.py and every value
matches the builder's stems and verify[] blocks.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# M1 Q5 trapezoid, drawn to scale from the exact bases and height. Only
# the three given lengths are labelled — the area is what the student
# must find, so it never appears on the figure.
B1, B2, H = 10, 6, 5
assert (B1 + B2) * H / 2 == 40
F.trapezoid("sat-p12-m1-q05", B1, B2, H,
            bottom_label=f"${B1}$", top_label=f"${B2}$",
            height_label=f"${H}$")

# M1 Q7 table of a linear relationship: y = 4x + 3 at every listed x.
XS, YS = [1, 2, 3, 4], [7, 11, 15, 19]
assert all(yy == 4 * xx + 3 for xx, yy in zip(XS, YS))
F.value_table("sat-p12-m1-q07", "$x$", XS, "$y$", YS)

# M1 Q20 tangent from an external point. The radius-tangent right angle
# makes OPQ a 9-12-15 right triangle. Only OP and OQ are labelled — PQ is
# the answer, and satfigs deliberately leaves it unlabelled.
RADIUS, TANGENT, HYP = 9, 12, 15
assert RADIUS**2 + TANGENT**2 == HYP**2
F.tangent_circle("sat-p12-m1-q20", RADIUS, TANGENT,
                 radius_label=f"${RADIUS}$", hyp_label=f"${HYP}$")
