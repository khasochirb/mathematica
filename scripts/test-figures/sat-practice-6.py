#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 6 → public/sat-figures/sat-p6-*.png

Every call passes the SAME parameter values the builder script
(scripts/test-builders/sat-practice-6.py) uses in its stems and verify[]
blocks, so a figure cannot disagree with the question it illustrates.
All drawing lives in scripts/test-figures/satfigs.py; this file is a
parameter manifest, nothing more.

Run AFTER the builder (so the stems are settled), then re-run the builder
so satbuild.figure() reads back the true pixel dimensions.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# ── Module 1 ──────────────────────────────────────────────────────────

# Q5 trapezoid: parallel sides 8 (top) and 14 (bottom), height 6.
F.trapezoid("sat-p6-m1-q05", b_bottom=14, b_top=8, height=6,
            bottom_label="$14$", top_label="$8$", height_label="$6$")

# Q8 isosceles triangle ABC with AB = AC and apex angle 44 degrees.
# The equal legs are chosen as 10; the base then follows EXACTLY from the
# apex angle, so the drawing is the triangle the stem describes.
_APEX = 44
_LEG = 10.0
_BASE = 2 * _LEG * math.sin(math.radians(_APEX / 2))
# triangle_sss(a = BC opposite A, b = CA opposite B, c = AB opposite C)
F.triangle_sss("sat-p6-m1-q08", a=_BASE, b=_LEG, c=_LEG,
               angle_labels={"A": r"$44^\circ$"},
               ticks={"b": 1, "c": 1})  # CA and AB carry one tick each: AB = AC

# Q13 45-45-90 right triangle with both legs 7 (hypotenuse deliberately
# unlabeled — it is what the student must find).
F.right_triangle("sat-p6-m1-q13", base=7, height=7,
                 base_label="$7$", height_label="$7$",
                 theta_at="bottom-left", theta_label=r"$45^\circ$")

# Q14 frequency table: pets owned against number of families (sums to 20
# families and 73 pets, matching the builder's assertion).
F.value_table("sat-p6-m1-q14", "Pets owned", [2, 3, 4, 5],
              "Number of families", [3, 5, 8, 4])

# Q19 scatterplot with the line of best fit y = 3x + 12. The residuals of
# these ten points sum to zero, so the drawn line really is a plausible
# line of best fit, and the point at x = 8 sits exactly 4 above it.
_PTS = [(1, 15), (2, 17), (3, 22), (4, 23), (5, 28),
        (6, 29), (7, 34), (8, 40), (9, 37), (10, 40)]
assert sum(y - (3 * x + 12) for x, y in _PTS) == 0, "residuals must balance"
assert (8, 40) in _PTS and 40 - (3 * 8 + 12) == 4
F.scatter("sat-p6-m1-q19", _PTS, line=(3, 12), xlim=(0, 11.6), ylim=(0, 48),
          xticks=(2, 4, 6, 8, 10), yticks=(10, 20, 30, 40),
          xlabel="Hours", ylabel="Units assembled")

# Q20 tangent line: radius 9, OQ = 15, so PQ = 12 by the Pythagorean
# theorem. PQ is NOT labeled — it is the answer.
assert 9 ** 2 + 12 ** 2 == 15 ** 2
F.tangent_circle("sat-p6-m1-q20", radius=9, tangent_len=12,
                 radius_label="$9$", hyp_label="$15$")

# ── Module 2, easier variant ──────────────────────────────────────────

# Q5 sphere of radius 3.
F.sphere("sat-p6-m2e-q05", radius_label="$3$")

# Q8 vertical angles: the marked pair really is vertical, drawn at the
# true 68 degrees.
F.vertical_angles("sat-p6-m2e-q08", slope_deg=68,
                  label_right=r"$(4x)^\circ$", label_left=r"$68^\circ$")

# Q20 sector with a 60-degree central angle. The radius is deliberately
# left unlabeled: the stem gives the AREA, and recovering r = 7 from it is
# the first step of the problem.
F.sector("sat-p6-m2e-q20", central_deg=60, angle_label=r"$60^\circ$")

# ── Module 2, harder variant ──────────────────────────────────────────

# Q4 parallelogram. With x = 34 the labeled angles are 3x + 10 = 112 and
# 2x = 68 degrees, so the shape is drawn at its true 112-degree corner.
_X = 34
assert (3 * _X + 10) + 2 * _X == 180
F.parallelogram("sat-p6-m2h-q04", base=6.0, side=4.0, angle_deg=3 * _X + 10,
                left_label=r"$(3x + 10)^\circ$", right_label=r"$(2x)^\circ$")

# Q5 two-way table of commuters by age group and travel method. Totals are
# computed inside the tool, so they cannot drift from these cells.
F.two_way_table("sat-p6-m2h-q05",
                col_heads=["Bus", "Car", "Bicycle"],
                row_heads=["Under 30", "30 or older"],
                cells=[[18, 12, 15], [10, 26, 9]],
                title="Method of travel to work")

# Q18 Thales: AB is a diameter of length 26 and AC = 10, so the angle at C
# is right and BC = 24 — left unlabeled as the answer.
assert 10 ** 2 + 24 ** 2 == 26 ** 2
F.semicircle_triangle("sat-p6-m2h-q18", diameter=26, leg=10,
                      diam_label="$26$", leg_label="$10$")

print("sat-practice-6 figures done")
