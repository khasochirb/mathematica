#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 2 — nothing but satfigs tool calls
with the SAME parameter values as scripts/test-builders/sat-practice-2.py.
This is the intended shape of every future figure script: if a figure
needs drawing code that isn't a tool yet, add the tool to satfigs.py.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

print("generating SAT practice test 2 figures:")

# ── Module 1 ──────────────────────────────────────────────────────────

# Q2: books sold per day
F.bar_chart("sat-p2-m1-q02",
            ["Mon", "Tue", "Wed", "Thu", "Fri"], [30, 25, 40, 55, 45],
            ylabel="Books sold", ytick_step=10)

# Q3: linear function table f(x) = 3x + 5
F.value_table("sat-p2-m1-q03", "$x$", [0, 1, 2, 3],
              "$f(x)$", [5, 8, 11, 14])

# Q5: angles (2x)° and 34° on a straight line (drawn exactly: 146° + 34°)
F.angle_pair("sat-p2-m1-q05", known_deg=34, known_label="$34°$",
             unknown_label="$(2x)°$")

# Q8: rectangle 10 × 6 with right triangle of height 4 on top
F.composite_area("sat-p2-m1-q08", rect_w=10, rect_h=6, tri_h=4)

# Q10: strong negative linear association (no fitted line shown)
F.scatter("sat-p2-m1-q10",
          pts=[(1, 38), (2, 33), (3, 31), (4, 27), (5, 22), (6, 20),
               (7, 15), (8, 13), (9, 8), (10, 5)],
          xlim=(-1.2, 12), ylim=(-5, 45),
          xticks=(2, 4, 6, 8, 10), yticks=(10, 20, 30, 40))

# Q12: exponential decay, halving every 10 days from 320
F.curve_graph("sat-p2-m1-q12",
              fns=[(lambda t: 320 * 0.5 ** (t / 10), 0, 42)],
              xlim=(-4, 46), ylim=(-38, 372),
              xticks=(10, 20, 30, 40), yticks=(40, 80, 160, 320),
              marks=[(0, 320), (10, 160), (20, 80), (30, 40)])

# Q16: central angle 80° at O, inscribed angle x° at C (half, exact)
F.inscribed_circle("sat-p2-m1-q16", central_deg=80,
                   central_label="$80°$", inscribed_label="$x°$")

# Q17: system y = x − 1, y = −x + 5 with solution (3, 2)
F.lines_graph("sat-p2-m1-q17", lines=[(1, -1), (-1, 5)],
              xlim=(-1.6, 6.6), ylim=(-2.6, 6.6), mark=(3, 2))

# ── Module 2 Easy ─────────────────────────────────────────────────────

# Q2: same-side interior angles 110° and x°
F.transversal("sat-p2-m2e-q02", top_label="$110°$", bottom_label="$x°$")

# Q4: club member ages, decade bins
F.histogram("sat-p2-m2e-q04", starts=(10, 20, 30, 40, 50),
            counts=(2, 4, 6, 5, 3), xlabel="Age (years)",
            ylabel="Members", ytick_step=2)

# Q5: y = |x − 3| − 2
F.curve_graph("sat-p2-m2e-q05",
              fns=[(lambda v: abs(v - 3) - 2, -1.4, 7.4)],
              xlim=(-2.6, 8.4), ylim=(-3.4, 5.4),
              xticks=(1, 3, 5), yticks=(-2,),
              marks=[(3, -2)], xnudge={1: -0.3, 5: 0.3})

# Q8: cylinder r = 4, h = 5 (drawn with those proportions)
F.cylinder("sat-p2-m2e-q08", r_label="4", h_label="5", r=4, h=5)

# Q11: quadratic table g(x) = (x − 2)² − 1
F.value_table("sat-p2-m2e-q11", "$x$", [-1, 0, 1, 2, 3],
              "$g(x)$", [8, 3, 0, -1, 0])

# Q13: x ≥ −1 (closed dot, ray right)
F.number_line("sat-p2-m2e-q13", point=-1, closed=True, direction="right",
              lo=-5, hi=5)

# Q17: right triangle legs 12 (adjacent) and 5, hypotenuse 13, θ marked
F.right_triangle("sat-p2-m2e-q17", base=12, height=5, base_label="12",
                 height_label="5", hyp_label="13",
                 theta_at="bottom-left")

# ── Module 2 Hard ─────────────────────────────────────────────────────

# Q2: same-side interior angles (4x)° and (2x + 30)° — drawn at the
# exact solved measures 100° and 80° (x = 25)
F.transversal("sat-p2-m2h-q02", top_label="$(4x)°$",
              bottom_label="$(2x + 30)°$", slope_deg=80)

# Q4: homework minutes box plot (12, 20, 28, 38, 50)
F.box_plot("sat-p2-m2h-q04", five=(12, 20, 28, 38, 50), lo=10, hi=50,
           tick_step=10, xlabel="Minutes")

# Q5: y = 2|x − 1| − 6
F.curve_graph("sat-p2-m2h-q05",
              fns=[(lambda v: 2 * abs(v - 1) - 6, -3.4, 5.4)],
              xlim=(-4.8, 6.8), ylim=(-7.8, 4.6),
              xticks=(-2, 1, 4), yticks=(-6,),
              marks=[(1, -6)], xnudge={-2: -0.35, 4: 0.35})

# Q8: cylinder, height 10, base circumference 12π (no radius segment —
# the radius is what the student must recover)
F.cylinder("sat-p2-m2h-q08", r_label=None, h_label="10", r=3.6, h=10)

# Q11: quadratic table h(x) = ½(x − 4)² − 1
F.value_table("sat-p2-m2h-q11", "$x$", [0, 2, 4, 6, 8],
              "$h(x)$", [7, 1, -1, 1, 7])

# Q13: x < 2 (open dot, ray left)
F.number_line("sat-p2-m2h-q13", point=2, closed=False, direction="left",
              lo=-3, hi=6)

# Q17: right triangle, hyp 25, opposite 15, adjacent 20 unlabeled
F.right_triangle("sat-p2-m2h-q17", base=20, height=15, base_label=None,
                 height_label="15", hyp_label="25",
                 theta_at="bottom-left")

print("done — re-run the builder to embed true pixel dimensions.")
