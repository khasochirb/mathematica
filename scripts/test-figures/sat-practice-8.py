#!/usr/bin/env python3
"""
Figures for SAT Math Practice Test 8 → public/sat-figures/sat-p8-*.png

Every call passes the SAME parameter values the builder script
(scripts/test-builders/sat-practice-8.py) uses in its stems and verify[]
blocks. All drawing lives in scripts/test-figures/satfigs.py.

Run AFTER the builder, then re-run the builder so satbuild.figure() reads
back the true pixel dimensions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import satfigs as F

# Q9 quadratic table. The SECOND differences must be constant (4) — that
# is the property the question is built on, so assert it here too.
XS, YS = [0, 1, 2, 3], [5, 8, 15, 26]
_d1 = [YS[i + 1] - YS[i] for i in range(3)]
assert [_d1[i + 1] - _d1[i] for i in range(2)] == [4, 4]
assert all(2 * x * x + x + 5 == y for x, y in zip(XS, YS))
F.value_table("sat-p8-m1-q09", "$x$", XS, "$g(x)$", YS)

# Q20 cone cross-section: the radius, height, and slant height form a
# right triangle. Drawn to scale from the true legs; the hypotenuse (the
# slant height) is left UNLABELED because it is the answer.
assert 9 ** 2 + 12 ** 2 == 15 ** 2
F.right_triangle("sat-p8-m1-q20", base=9, height=12,
                 base_label="$9$", height_label="$12$")

# Q20 (module 2 easy) exponential table: each output is 3 times the last.
XS2, YS2 = [0, 1, 2, 3], [7, 21, 63, 189]
assert all(b == 3 * a for a, b in zip(YS2, YS2[1:]))
F.value_table("sat-p8-m2e-q20", "$x$", XS2, "$h(x)$", YS2)

print("sat-practice-8 figures done")
