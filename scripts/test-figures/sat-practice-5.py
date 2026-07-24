#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 5 — nothing but satfigs tool calls with
the SAME parameter values as scripts/test-builders/sat-practice-5.py.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

print("generating SAT practice test 5 figures:")

# ── Module 1 ──────────────────────────────────────────────────────────

# Q2: pages per day table (mean = 24)
F.value_table("sat-p5-m1-q02", "Day", ["Mon", "Tue", "Wed", "Thu", "Fri"],
              "Pages", [18, 30, 22, 27, 23])

# Q10: travel two-way table, walkers 12 + 10 = 22
F.two_way_table("sat-p5-m1-q10",
                col_heads=["Bus", "Walk"],
                row_heads=["Grade 9", "Grade 10"],
                cells=[[18, 12], [20, 10]], title="Travel to school")

# Q12: bacteria growth 500 * 2^(t/3)
F.curve_graph("sat-p5-m1-q12",
              fns=[(lambda t: 500 * 2 ** (t / 3), 0, 9.4)],
              xlim=(-0.6, 10.2), ylim=(-400, 4700),
              xticks=(3, 6, 9), yticks=(1000, 2000, 3000, 4000),
              marks=[(0, 500), (3, 1000), (6, 2000), (9, 4000)])

# Q13: right triangle, adjacent 6, opposite 8, hyp 10, theta at bottom-left
F.right_triangle("sat-p5-m1-q13", base=6, height=8,
                 base_label="$6$", height_label="$8$", hyp_label="$10$",
                 theta_at="bottom-left")

# Q17: box plot (12, 20, 28, 36, 50)
F.box_plot("sat-p5-m1-q17", five=(12, 20, 28, 36, 50), lo=10, hi=50,
           tick_step=10, xlabel="Value")

# ── Module 2 Easy ─────────────────────────────────────────────────────

# Q2: books read bar chart (7, 12, 9, 4)
F.bar_chart("sat-p5-m2e-q02", ["Ana", "Bat", "Chimeg", "Dorj"],
            [7, 12, 9, 4], ylabel="Books", ytick_step=3, title="Books read")

# Q10: scatter with line of best fit y = 4x + 5
F.scatter("sat-p5-m2e-q10",
          pts=[(1, 10), (2, 12), (3, 18), (4, 20), (5, 26), (6, 28)],
          line=(4, 5), xlim=(0, 8), ylim=(0, 36),
          xticks=(2, 4, 6), yticks=(10, 20, 30))

# Q13: right triangle legs 9 and 12 (hypotenuse unknown)
F.right_triangle("sat-p5-m2e-q13", base=9, height=12,
                 base_label="$9$", height_label="$12$", hyp_label="$?$")

# Q17: temperature histogram, starts 50/60/70/80, counts 7/8/6/9
F.histogram("sat-p5-m2e-q17", starts=[50, 60, 70, 80], counts=[7, 8, 6, 9],
            xlabel="High temperature (°F)", ylabel="Days", ytick_step=2)

# ── Module 2 Hard ─────────────────────────────────────────────────────

# Q2: drink preference bar chart (18, 24, 18)
F.bar_chart("sat-p5-m2h-q02", ["Tea", "Coffee", "Water"], [18, 24, 18],
            ylabel="People", ytick_step=6, title="Drink preference")

# Q13: 30-60-90 triangle, hypotenuse 14; long leg = 7*sqrt(3) is adjacent
# to the 30 degree angle, short leg = 7 (opposite 30) is left unlabeled so
# the figure never prints the answer.
F.right_triangle("sat-p5-m2h-q13", base=7 * math.sqrt(3), height=7,
                 hyp_label="$14$", theta_at="bottom-left",
                 theta_label="$30^\\circ$")

# Q17: pass/fail two-way table, adults 15 passed of 25
F.two_way_table("sat-p5-m2h-q17",
                col_heads=["Passed", "Failed"],
                row_heads=["Adult", "Child"],
                cells=[[15, 10], [20, 15]], title="Test results")

print("done.")
