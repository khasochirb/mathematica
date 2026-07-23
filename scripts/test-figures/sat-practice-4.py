#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 4 — nothing but satfigs tool calls with
the SAME parameter values as scripts/test-builders/sat-practice-4.py.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

print("generating SAT practice test 4 figures:")

# ── Module 1 ──────────────────────────────────────────────────────────

# Q2: laps per day table (mean = 14)
F.value_table("sat-p4-m1-q02", "Day", ["Mon", "Tue", "Wed", "Thu", "Fri"],
              "Laps", [12, 15, 9, 18, 16])

# Q10: travel two-way table, grade 11 walkers 10 of 40
F.two_way_table("sat-p4-m1-q10",
                col_heads=["Bus", "Walk"], row_heads=["Grade 10", "Grade 11"],
                cells=[[24, 16], [30, 10]], title="Travel to school")

# Q12: machine value decay 8000 * 0.75^x
F.curve_graph("sat-p4-m1-q12",
              fns=[(lambda t: 8000 * 0.75 ** t, 0, 4.4)],
              xlim=(-0.5, 5.1), ylim=(-800, 8900),
              xticks=(1, 2, 3, 4), yticks=(2000, 4500, 6000, 8000),
              marks=[(0, 8000), (1, 6000), (2, 4500)])

# Q17: delivery-time box plot (20, 30, 40, 55, 70)
F.box_plot("sat-p4-m1-q17", five=(20, 30, 40, 55, 70), lo=20, hi=70,
           tick_step=10, xlabel="Minutes")

# ── Module 2 Easy ─────────────────────────────────────────────────────

# Q2: books read bar chart (7, 12, 9, 4)
F.bar_chart("sat-p4-m2e-q02", ["Ana", "Bat", "Chimeg", "Dorj"],
            [7, 12, 9, 4], ylabel="Books read", ytick_step=2)

# Q4: single line through (0, -2) and (2, 2) — slope 2
F.lines_graph("sat-p4-m2e-q04", lines=[(2, -2)],
              xlim=(-3.6, 4.6), ylim=(-4.6, 4.6))

# Q10: exponential table h(x) = 5 * 2^x
F.value_table("sat-p4-m2e-q10", "$x$", [0, 1, 2, 3],
              "$h(x)$", [5, 10, 20, 40])

# Q13: x >= 3 (closed dot, ray right)
F.number_line("sat-p4-m2e-q13", point=3, closed=True, direction="right",
              lo=-2, hi=8)

# Q17: cylinder r = 3, h = 5
F.cylinder("sat-p4-m2e-q17", r_label="3", h_label="5", r=3, h=5)

# ── Module 2 Hard ─────────────────────────────────────────────────────

# Q2: angles (3x)° and 48° on a straight line (drawn exactly: 132° + 48°)
F.angle_pair("sat-p4-m2h-q02", known_deg=48, known_label="$48°$",
             unknown_label="$(3x)°$")

# Q4: wait-time histogram (3, 5, 7, 4, 1 across 0-50)
F.histogram("sat-p4-m2h-q04", starts=(0, 10, 20, 30, 40),
            counts=(3, 5, 7, 4, 1), xlabel="Wait time (minutes)",
            ylabel="Customers", ytick_step=2)

# Q11: quadratic table f(x) = 4 - (x - 3)^2
F.value_table("sat-p4-m2h-q11", "$x$", [1, 2, 3, 4, 5],
              "$f(x)$", [0, 3, 4, 3, 0])

# Q12: employees two-way table, remote 12/8
F.two_way_table("sat-p4-m2h-q12",
                col_heads=["Under 5 yr", "5+ yr"],
                row_heads=["Remote", "Office"],
                cells=[[12, 8], [18, 12]], title="Years of service")

print("done — re-run the builder to embed true pixel dimensions.")
