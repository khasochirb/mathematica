#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 3 — nothing but satfigs tool calls with
the SAME parameter values as scripts/test-builders/sat-practice-3.py. If a
figure needs drawing code that isn't a tool yet, add the tool to satfigs.py
rather than forking per-test code.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

print("generating SAT practice test 3 figures:")

# ── Module 1 ──────────────────────────────────────────────────────────

# Q2: library open-hours table (total = 34)
F.value_table("sat-p3-m1-q02", "Day", ["Mon", "Tue", "Wed", "Thu"],
              "Hours", [6, 9, 7, 12])

# Q3: 115° and x° on a straight line (drawn exactly: 115° + 65°)
F.angle_pair("sat-p3-m1-q03", known_deg=115, known_label="$115°$",
             unknown_label="$x°$")

# Q10: exponential growth, doubling every hour from 100
F.curve_graph("sat-p3-m1-q10",
              fns=[(lambda t: 100 * 2 ** t, 0, 3.15)],
              xlim=(-0.4, 3.7), ylim=(-90, 880),
              xticks=(1, 2, 3), yticks=(100, 200, 400, 800),
              marks=[(0, 100), (1, 200), (2, 400), (3, 800)])

# Q11: plant heights with best-fit line y = 2x + 6
F.scatter("sat-p3-m1-q11",
          pts=[(1, 9), (2, 9), (3, 13), (4, 13), (5, 17), (6, 17),
               (7, 19), (8, 23)],
          line=(2, 6), xlim=(-1.2, 12), ylim=(-3, 30),
          xticks=(2, 4, 6, 8, 10), yticks=(10, 20),
          xlabel="Weeks", ylabel="Height (cm)")

# Q17: two-way table, Senior-Tea cell = 18, total = 60
F.two_way_table("sat-p3-m1-q17",
                col_heads=["Coffee", "Tea"], row_heads=["Junior", "Senior"],
                cells=[[12, 10], [20, 18]], title="Drink preference")

# ── Module 2 Easy ─────────────────────────────────────────────────────

# Q2: same-side interior angles 68° and x° (supplementary)
F.transversal("sat-p3-m2e-q02", top_label="$68°$", bottom_label="$x°$")

# Q4: tickets sold by four sellers
F.bar_chart("sat-p3-m2e-q04", ["A", "B", "C", "D"], [50, 35, 42, 28],
            ylabel="Tickets sold", ytick_step=10)

# Q11: quadratic table h(x) = (x − 1)² + 2
F.value_table("sat-p3-m2e-q11", "$x$", [-1, 0, 1, 2, 3],
              "$h(x)$", [6, 3, 2, 3, 6])

# Q13: x > 2 (open dot, ray right)
F.number_line("sat-p3-m2e-q13", point=2, closed=False, direction="right",
              lo=-3, hi=7)

# Q17: right triangle, opposite 3, adjacent 4, hypotenuse 5, θ at bottom-left
F.right_triangle("sat-p3-m2e-q17", base=4, height=3, base_label="4",
                 height_label="3", hyp_label="5", theta_at="bottom-left")

# ── Module 2 Hard ─────────────────────────────────────────────────────

# Q2: same-side interior angles (2x)° and 130° — drawn at the solved
# measures 50° and 130° (x = 25)
F.transversal("sat-p3-m2h-q02", top_label="$(2x)°$",
              bottom_label="$130°$", slope_deg=50)

# Q4: box plot (10, 18, 24, 32, 40)
F.box_plot("sat-p3-m2h-q04", five=(10, 18, 24, 32, 40), lo=10, hi=40,
           tick_step=5, xlabel="Value")

# Q5: parabola y = (x + 2)² − 3, vertex (−2, −3)
F.curve_graph("sat-p3-m2h-q05",
              fns=[(lambda v: (v + 2) ** 2 - 3, -5.0, 1.0)],
              xlim=(-6.2, 2.2), ylim=(-4.4, 6.2),
              xticks=(-2,), yticks=(-3,),
              marks=[(-2, -3)], xnudge={-2: -0.35})

# Q11: quadratic table h(x) = 2(x − 3)² − 4
F.value_table("sat-p3-m2h-q11", "$x$", [1, 2, 3, 4, 5],
              "$h(x)$", [4, -2, -4, -2, 4])

# Q13: x ≤ −1 (closed dot, ray left)
F.number_line("sat-p3-m2h-q13", point=-1, closed=True, direction="left",
              lo=-6, hi=4)

# Q20: central angle 70° at O, inscribed angle at C (unlabeled — the answer)
F.inscribed_circle("sat-p3-m2h-q20", central_deg=70,
                   central_label="$70°$", inscribed_label="")

print("done — re-run the builder to embed true pixel dimensions.")
