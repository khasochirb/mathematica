# -*- coding: utf-8 -*-
"""IB Mathematics problem bank — topic-focused practice for /practice/ib.

Blueprint (memory/resource-blueprint.md): every hub offers topic-focused
practice in ITS OWN taxonomy. For IB that taxonomy is the five official
syllabus topics — Number & Algebra, Functions, Geometry & Trigonometry,
Statistics & Probability, Calculus — split by tier exactly like the live
courses: the ib-sl bank drills the SL syllabus, the ib-hl bank drills the
AHL extension on top of it (HL strictly contains SL, so HL students work
both banks — same rule as the /math/ib-hl course).

All content is 100% self-authored (locked decision, expansion-vision §4.3):
these emulate IB register and difficulty, never actual released questions.
English by hub policy. Every answer and distractor is COMPUTED from named
parameters and sympy-asserted by the gate; every distractor encodes one
specific student error.

Levels: 1 ≈ "write down"/one-step, 2 ≈ standard Paper 1/2 short question,
3 ≈ the last parts of Section A (discriminating 6→7 on a short item).

Unit ids match the COURSE unit slugs (data/genmath/ib-sl, ib-hl) so the
bank's "review the lessons" links land on the right course unit.
"""
import os
import sys
from fractions import Fraction

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from sympy import Rational

from imbank import fmt, lin, mk_num, mk_txt, form, pt


UNITS = [
    {"id": "number-and-algebra", "title": "Number & Algebra",
     "blurb": "Sequences and series, exponents and logarithms, the binomial theorem."},
    {"id": "functions", "title": "Functions",
     "blurb": "Composite and inverse functions, quadratics, rational functions and transformations."},
    {"id": "geometry-and-trigonometry", "title": "Geometry & Trigonometry",
     "blurb": "Radians, the sine and cosine rules, exact values and trigonometric equations."},
    {"id": "statistics-and-probability", "title": "Statistics & Probability",
     "blurb": "Summary statistics, probability laws, conditional probability and the binomial distribution."},
    {"id": "calculus", "title": "Calculus",
     "blurb": "Differentiation, tangents, stationary points, and definite integrals with areas."},
]

HL_UNITS = [
    {"id": "number-and-algebra", "title": "Number & Algebra (AHL)",
     "blurb": "Complex numbers — arithmetic, modulus and argument — and counting principles."},
    {"id": "functions", "title": "Functions (AHL)",
     "blurb": "The remainder and factor theorems, and sums and products of roots."},
    {"id": "geometry-and-trigonometry", "title": "Geometry & Trigonometry (AHL)",
     "blurb": "Vectors in three dimensions, scalar products, angles between vectors, compound angles."},
    {"id": "statistics-and-probability", "title": "Statistics & Probability (AHL)",
     "blurb": "Bayes' theorem, expectation algebra and counting-based probability."},
    {"id": "calculus", "title": "Calculus (AHL)",
     "blurb": "Product, quotient and implicit differentiation, and integration by substitution."},
]


def pi_mult(c):
    """Render c*pi for rational c: 1 -> \\pi, 3/2 -> \\frac{3}{2}\\pi, 2 -> 2\\pi."""
    c = Rational(c)
    if c == 1:
        return "\\pi"
    if c == -1:
        return "-\\pi"
    return "%s\\pi" % fmt(c)


# ===========================================================================
# SL · Topic 1 — Number & Algebra
# ===========================================================================

def _g_sl_arith_nth():
    """u_n = u1 + (n-1)d."""
    raws = []
    for u1 in (2, 3, 5, 7, 8):
        for d in (3, 4, 6, 7, 9, -4, -6):
            if u1 == d:
                continue  # keeps the swapped-roles distractor distinct
            for n in (11, 15, 21):
                un = u1 + (n - 1) * d
                raws.append({
                    "statement": "An arithmetic sequence has first term $u_1 = %d$ and common "
                                 "difference $d = %d$. Find $u_{%d}$." % (u1, d, n),
                    "correct": un,
                    # used n instead of n-1 · swapped u1 and d in the formula ·
                    # added d once instead of (n-1) times
                    "dvals": [u1 + n * d, d + (n - 1) * u1, u1 + (n - 1) + d],
                    "explanation": "Use $u_n = u_1 + (n-1)d$: $u_{%d} = %d + %d \\cdot (%d) "
                                   "= %d$. Multiplying $d$ by $n$ instead of $n-1$ is the "
                                   "classic slip — it gives $%d$."
                                   % (n, u1, n - 1, d, un, u1 + n * d),
                    "check": ["Eq(%d + (%d - 1)*(%d), %d)" % (u1, n, d, un)],
                })
    return raws


def _g_sl_geom_nth():
    """u_n = u1 * r^(n-1), including a fractional ratio."""
    ratios = [Rational(2), Rational(3), Rational(-2), Rational(1, 2)]
    raws = []
    for a in (2, 3, 5, 4):
        for r in ratios:
            for n in (4, 5, 6):
                un = a * r ** (n - 1)
                raws.append({
                    "statement": "A geometric sequence has first term $u_1 = %d$ and common "
                                 "ratio $r = %s$. Find $u_{%d}$." % (a, fmt(r), n),
                    "correct": un,
                    # used r^n · used r^(n-2) · treated it as arithmetic with d = r
                    "dvals": [a * r ** n, a * r ** (n - 2), a + (n - 1) * r],
                    "explanation": "Use $u_n = u_1 r^{\\,n-1}$: $u_{%d} = %d \\cdot "
                                   "\\left(%s\\right)^{%d} = %s$. One factor of $r$ too many "
                                   "gives $%s$."
                                   % (n, a, fmt(r), n - 1, fmt(un), fmt(a * r ** n)),
                    "check": ["Eq(%d * (Rational(%d,%d))**(%d), Rational(%d,%d))"
                              % (a, r.p, r.q, n - 1, un.p, un.q)],
                })
    return raws


def _g_sl_arith_sum():
    """S_n = n/2 (2u1 + (n-1)d)."""
    raws = []
    for u1 in (2, 3, 5, 7, 4):
        for d in (3, 4, 6, 5):
            for n in (10, 12, 20):
                un = u1 + (n - 1) * d
                s = n * (u1 + un) // 2
                raws.append({
                    "statement": "An arithmetic sequence has $u_1 = %d$ and common difference "
                                 "$d = %d$. Find the sum of the first %d terms." % (u1, d, n),
                    "correct": s,
                    # forgot the 1/2 · summed only n-1 terms · used n * u_n
                    "dvals": [2 * s, s - un, n * un],
                    "explanation": "The last term is $u_{%d} = %d$, so $S_{%d} = "
                                   "\\dfrac{%d}{2}(u_1 + u_{%d}) = \\dfrac{%d}{2}(%d + %d) = %d$. "
                                   "Dropping the $\\frac{1}{2}$ doubles it to $%d$."
                                   % (n, un, n, n, n, n, u1, un, s, 2 * s),
                    "check": ["Eq(%d + (%d - 1)*%d, %d)" % (u1, n, d, un),
                              "Eq(Rational(%d,2)*(%d + %d), %d)" % (n, u1, un, s)],
                })
    return raws


def _g_sl_log_laws():
    """log_b(b^i) + log_b(b^j) = i + j."""
    raws = []
    for b in (2, 3, 4, 5, 10):
        for (i, j) in ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (4, 1)):
            x, y = b ** i, b ** j
            raws.append({
                "statement": "Find the value of $\\log_{%d} %d + \\log_{%d} %d$." % (b, x, b, y),
                "correct": i + j,
                # multiplied the logs · multiplied the arguments and stopped ·
                # subtracted the logs
                "dvals": [i * j, x * y, abs(i - j) if i != j else i + j + 1],
                "explanation": "$\\log_{%d} %d = %d$ and $\\log_{%d} %d = %d$, and logs of the "
                               "same base add: $%d + %d = %d$. (Equivalently "
                               "$\\log_{%d}(%d \\cdot %d) = \\log_{%d} %d = %d$.) Multiplying "
                               "the two logs gives $%d$ — addition of logs multiplies the "
                               "ARGUMENTS, not the logs."
                               % (b, x, i, b, y, j, i, j, i + j,
                                  b, x, y, b, x * y, i + j, i * j),
                "check": ["Eq((%d)**(%d), %d)" % (b, i + j, x * y),
                          "Eq(simplify(log(%d,%d) + log(%d,%d)), %d)" % (x, b, y, b, i + j)],
            })
    return raws


def _g_sl_infinite_geom():
    """S_inf = a / (1 - r), |r| < 1."""
    ratios = [Rational(1, 2), Rational(1, 3), Rational(2, 3), Rational(1, 4),
              Rational(3, 4), Rational(-1, 2), Rational(-1, 3)]
    raws = []
    for a in (6, 9, 12, 18, 24, 8):
        for r in ratios:
            s = Rational(a) / (1 - r)
            raws.append({
                "statement": "An infinite geometric series has first term $u_1 = %d$ and "
                             "common ratio $r = %s$. Find the sum of the series." % (a, fmt(r)),
                "correct": s,
                # sign slip in the denominator · divided by r · multiplied by (1-r)
                "dvals": [Rational(a) / (1 + r), Rational(a) / r, a * (1 - r)],
                "explanation": "Since $|r| = %s < 1$ the series converges, and $S_\\infty = "
                               "\\dfrac{u_1}{1 - r} = \\dfrac{%d}{%s} = %s$. Writing $1 + r$ "
                               "in the denominator gives $%s$."
                               % (fmt(abs(r)), a, fmt(1 - r), fmt(s), fmt(Rational(a) / (1 + r))),
                "check": ["Rational(%d,%d) < 1" % (abs(r).p, abs(r).q),
                          "Eq(%d / (1 - Rational(%d,%d)), Rational(%d,%d))"
                          % (a, r.p, r.q, s.p, s.q)],
            })
    return raws


def _g_sl_binomial_coeff():
    """Coefficient of x^k in (x + a)^n."""
    from math import comb
    raws = []
    for n in (4, 5, 6):
        for k in range(1, n):
            if 2 * k == n:
                continue  # keeps the swapped-exponent distractor distinct
            for a in (2, 3, -2, -3):
                c = comb(n, k) * a ** (n - k)
                raws.append({
                    "statement": "Find the coefficient of $x^{%d}$ in the expansion of "
                                 "$%s^{%d}$." % (k, "(x + %d)" % a if a > 0 else "(x - %d)" % -a, n),
                    "correct": c,
                    # swapped which exponent a carries · forgot the binomial
                    # coefficient · forgot the power of a entirely
                    "dvals": [comb(n, k) * a ** k, a ** (n - k), comb(n, k)],
                    "explanation": "The general term is $\\binom{%d}{r} x^{r} \\cdot (%d)^{%d-r}$; "
                                   "for $x^{%d}$ take $r = %d$: $\\binom{%d}{%d}(%d)^{%d} = "
                                   "%d \\cdot %d = %d$. Putting the power of $%d$ on the wrong "
                                   "factor gives $%d$."
                                   % (n, a, n, k, k, n, k, a, n - k,
                                      comb(n, k), a ** (n - k), c, a, comb(n, k) * a ** k),
                    "check": ["Eq(binomial(%d,%d)*(%d)**(%d), %d)" % (n, k, a, n - k, c)],
                })
    return raws


# ===========================================================================
# SL · Topic 2 — Functions
# ===========================================================================

def _g_sl_composite():
    """(f o g)(t) for f(x) = ax + b, g(x) = x^2 + c."""
    raws = []
    for a in (2, 3, -2, 4):
        for b in (1, -3, 5):
            for c in (2, -4, 3):
                for t in (2, -2, 3, 1):
                    fog = a * (t * t + c) + b
                    gof = (a * t + b) ** 2 + c
                    raws.append({
                        "statement": "Let $f(x) = %s$ and $g(x) = %s$. Find $(f \\circ g)(%d)$."
                                     % (lin(a, b), quad_x2c(c), t),
                        "correct": fog,
                        # composed the wrong way round · forgot to multiply c by a ·
                        # added the functions instead of composing
                        "dvals": [gof, a * t * t + c + b, (a * t + b) + (t * t + c)],
                        "explanation": "Inner first: $g(%d) = %d$. Then $f(%d) = %d \\cdot %d "
                                       "%s %d = %d$. Composing in the wrong order gives "
                                       "$(g \\circ f)(%d) = %d$."
                                       % (t, t * t + c, t * t + c, a, t * t + c,
                                          "+" if b >= 0 else "-", abs(b), fog, t, gof),
                        "check": ["Eq(%d*((%d)**2 + (%d)) + (%d), %d)" % (a, t, c, b, fog)],
                    })
    return raws


def quad_x2c(c):
    """Render x^2 + c."""
    if c == 0:
        return "x^2"
    return "x^2 + %d" % c if c > 0 else "x^2 - %d" % -c


def _g_sl_inverse():
    """f(x) = ax + b, find f^{-1}(k)."""
    raws = []
    for a in (2, 3, 4, 5, -2):
        for b in (1, -3, 7, -5):
            for x0 in (2, 3, -1, 4):
                k = a * x0 + b
                raws.append({
                    "statement": "Let $f(x) = %s$. Find $f^{-1}(%d)$." % (lin(a, b), k),
                    "correct": x0,
                    # applied f instead of its inverse · sign slip on b ·
                    # multiplied instead of dividing by a
                    "dvals": [a * k + b, Rational(k + b, a), a * (k - b)],
                    "explanation": "Solve $%s = %d$: $%dx = %d$, so $x = %d$. Applying $f$ "
                                   "itself gives $f(%d) = %d$ — the inverse UNDOES $f$, so "
                                   "check with $f(%d) = %d$."
                                   % (lin(a, b), k, a, k - b, x0, k, a * k + b, x0, k),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, x0, b, k)],
                })
    return raws


def _g_sl_vertex():
    """Vertex of f(x) = x^2 + bx + c, engineered from (h, k)."""
    raws = []
    for h in (1, 2, 3, -1, -2, -3, 4):
        for k in (2, -3, 5, -5, 4, -2):
            if h == k or h == -k:
                continue  # keeps the coordinate-shuffle distractors distinct
            b, c = -2 * h, h * h + k
            raws.append({
                "statement": "The graph of $f(x) = %s$ has its vertex at the point:"
                             % ("x^2 " + ("+ %dx" % b if b > 0 else "- %dx" % -b) +
                                (" + %d" % c if c >= 0 else " - %d" % -c)),
                "correct": "$%s$" % pt(h, k),
                # sign of h flipped · sign of k flipped · coordinates swapped
                "dvals": ["$%s$" % pt(-h, k), "$%s$" % pt(h, -k), "$%s$" % pt(k, h)],
                "explanation": "The $x$-coordinate is $-\\dfrac{b}{2a} = -\\dfrac{%d}{2} = %d$, "
                               "and $f(%d) = %d$. So the vertex is $%s$. Forgetting the minus "
                               "sign in $-b/2a$ gives $x = %d$."
                               % (b, h, h, k, pt(h, k), -h),
                "check": ["Eq(-Rational(%d,2), %d)" % (b, h),
                          "Eq((%d)**2 + (%d)*(%d) + (%d), %d)" % (h, b, h, c, k)],
            })
    return raws


def _g_sl_asymptotes():
    """Asymptotes of f(x) = (ax + b)/(cx + d)."""
    raws = []
    for a in (1, 2, 3, 4):
        for c in (1, 2, 3):
            for b in (1, -3, 5, -1):
                for d in (2, -2, 4, -4, 6):
                    if a * d == b * c:
                        continue  # degenerate (constant function)
                    va, ha = Rational(-d, c), Rational(a, c)
                    if Rational(b, d) == ha or Rational(d, c) == va:
                        continue  # keeps distractors distinct
                    raws.append({
                        "statement": "The function $f(x) = \\dfrac{%s}{%s}$ has asymptotes:"
                                     % (lin(a, b), lin(c, d)),
                        "correct": "$x = %s$ and $y = %s$" % (fmt(va), fmt(ha)),
                        # sign slip on the vertical asymptote · constants ratio for
                        # the horizontal · numerator zero used for the vertical
                        "dvals": ["$x = %s$ and $y = %s$" % (fmt(Rational(d, c)), fmt(ha)),
                                  "$x = %s$ and $y = %s$" % (fmt(va), fmt(Rational(b, d))),
                                  "$x = %s$ and $y = %s$" % (fmt(Rational(-b, a)), fmt(ha))],
                        "explanation": "Vertical asymptote where the denominator is zero: "
                                       "$%s = 0$ gives $x = %s$. Horizontal asymptote from the "
                                       "ratio of leading coefficients: $y = %s$. Setting the "
                                       "NUMERATOR to zero gives the $x$-intercept, not an "
                                       "asymptote."
                                       % (lin(c, d), fmt(va), fmt(ha)),
                        "check": ["Eq(%d*Rational(%d,%d) + %d, 0)" % (c, va.p, va.q, d),
                                  "Eq(Rational(%d,%d), Rational(%d,%d))" % (a, c, ha.p, ha.q)],
                    })
    return raws


def _g_sl_transform_point():
    """Image of (p, q) under y = a f(x - h) + k."""
    raws = []
    for a in (2, 3, -2):
        for h in (1, 2, -1, -2, 3):
            for k in (1, -2, 4, -4):
                for (p, q) in ((2, 3), (-1, 4), (3, -2), (0, 5)):
                    raws.append({
                        "statement": "The point $%s$ lies on the graph of $y = f(x)$. Find the "
                                     "image of this point on the graph of "
                                     "$y = %df(x %s %d) %s %d$."
                                     % (pt(p, q), a, "-" if h > 0 else "+", abs(h),
                                        "+" if k > 0 else "-", abs(k)),
                        "correct": "$%s$" % pt(p + h, a * q + k),
                        # shifted the wrong way · added k before stretching ·
                        # sign slip on k
                        "dvals": ["$%s$" % pt(p - h, a * q + k), "$%s$" % pt(p + h, a * (q + k)),
                                  "$%s$" % pt(p + h, a * q - k)],
                        "explanation": "$x - %d$ shifts the graph $%d$ units %s, and the output "
                                       "is stretched by $%d$ THEN translated by $%d$: the image "
                                       "is $(%d %s %d,\\ %d \\cdot %d %s %d) = %s$. Adding $%d$ "
                                       "before multiplying gives $%s$."
                                       % (h, abs(h), "right" if h > 0 else "left", a, k,
                                          p, "+" if h >= 0 else "-", abs(h), a, q,
                                          "+" if k >= 0 else "-", abs(k),
                                          pt(p + h, a * q + k), k, pt(p + h, a * (q + k))),
                        "check": ["Eq(%d + %d, %d)" % (p, h, p + h),
                                  "Eq(%d*%d + %d, %d)" % (a, q, k, a * q + k)],
                    })
    return raws


# ===========================================================================
# SL · Topic 3 — Geometry & Trigonometry
# ===========================================================================

# (numerator, denominator) of the radian measure as a multiple of pi
_SL_ARCS = [(1, 6), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (5, 6)]


def _g_sl_arc_length():
    """s = r*theta with theta a rational multiple of pi (radians)."""
    raws = []
    for r in (2, 3, 4, 6, 8, 9, 12):
        for (p, q) in _SL_ARCS:
            s = Rational(r * p, q)
            area = Rational(r * r * p, 2 * q)
            deg_val = Rational(r * p * 180, q)
            raws.append({
                "statement": "A circle has radius $%d\\,$cm. Find the length of the arc "
                             "subtended by a central angle of $%s$ radians."
                             % (r, pi_mult(Rational(p, q))),
                "correct": "$%s$ cm" % pi_mult(s),
                # computed the sector area · used the diameter · treated the
                # angle as degrees inside the formula
                "dvals": ["$%s$ cm" % pi_mult(area),
                          "$%s$ cm" % pi_mult(2 * s),
                          "$%s$ cm" % fmt(deg_val)],
                "explanation": "In radians, arc length is $s = r\\theta = %d \\cdot %s = %s$ cm. "
                               "$\\frac{1}{2}r^2\\theta = %s$ is the SECTOR AREA — the other "
                               "half of this formula pair."
                               % (r, pi_mult(Rational(p, q)), pi_mult(s), pi_mult(area)),
                "check": ["Eq(%d * Rational(%d,%d)*pi, Rational(%d,%d)*pi)"
                          % (r, p, q, s.p, s.q)],
            })
    return raws


def _g_sl_cosine_rule():
    """a^2 = b^2 + c^2 - 2bc cos A for A = 60 or 120 degrees."""
    raws = []
    for (deg, cosv) in ((60, Rational(1, 2)), (120, Rational(-1, 2))):
        for b in (3, 4, 5, 6, 7, 8):
            for c in (5, 6, 7, 8, 9, 10, 11):
                if c <= b:
                    continue
                a2 = b * b + c * c - 2 * b * c * cosv
                raws.append({
                    "statement": "In triangle $ABC$, $b = %d$, $c = %d$ and "
                                 "$\\hat{A} = %d^\\circ$. Find $a^2$." % (b, c, deg),
                    "correct": a2,
                    # sign slip on the cosine term · dropped the cosine term
                    # (treated it as a right angle) · forgot the cos factor (used cos A = 1)
                    "dvals": [b * b + c * c + 2 * b * c * cosv,
                              b * b + c * c,
                              b * b + c * c - 2 * b * c],
                    "explanation": "Cosine rule: $a^2 = b^2 + c^2 - 2bc\\cos A = %d + %d - "
                                   "2 \\cdot %d \\cdot %d \\cdot \\left(%s\\right) = %s$. With "
                                   "$\\hat{A} = %d^\\circ$, $\\cos A = %s$ — the sign of the "
                                   "cosine is where this question is won or lost."
                                   % (b * b, c * c, b, c, fmt(cosv), fmt(a2), deg, fmt(cosv)),
                    "check": ["Eq(%d**2 + %d**2 - 2*%d*%d*cos(%d*pi/180), %s)"
                              % (b, c, b, c, deg, a2)],
                })
    return raws


def _g_sl_triangle_area():
    """Area = 1/2 ab sin C with C = 30 or 150 degrees (sin C = 1/2)."""
    raws = []
    for deg in (30, 150):
        for a in (4, 6, 8, 10, 12, 5):
            for b in (6, 8, 10, 12, 14, 9):
                if b <= a or a * b == a + b:
                    continue
                area = Rational(a * b, 4)
                raws.append({
                    "statement": "In triangle $ABC$, $a = %d$, $b = %d$ and "
                                 "$\\hat{C} = %d^\\circ$. Find the area of the triangle."
                                 % (a, b, deg),
                    "correct": area,
                    # forgot sin C (or the 1/2 — same value, one trap) · forgot
                    # both · added the sides instead of multiplying
                    "dvals": [Rational(a * b, 2), a * b, Rational(a + b, 4)],
                    "explanation": "Area $= \\frac{1}{2}ab\\sin C = \\frac{1}{2} \\cdot %d "
                                   "\\cdot %d \\cdot \\sin %d^\\circ = \\frac{1}{2} \\cdot %d "
                                   "\\cdot \\frac{1}{2} = %s$. Since $\\sin %d^\\circ = "
                                   "\\frac{1}{2}$, dropping EITHER the $\\frac{1}{2}$ or the "
                                   "sine leaves $%s$."
                                   % (a, b, deg, a * b, fmt(area), deg, fmt(Rational(a * b, 2))),
                    "check": ["Eq(Rational(1,2)*%d*%d*sin(%d*pi/180), Rational(%d,%d))"
                              % (a, b, deg, area.p, area.q)],
                })
    return raws


# (latex angle, sympy angle) pairs for the exact-value form
_UC = [
    ("\\frac{\\pi}{6}", "pi/6"), ("\\frac{\\pi}{4}", "pi/4"), ("\\frac{\\pi}{3}", "pi/3"),
    ("\\frac{2\\pi}{3}", "2*pi/3"), ("\\frac{3\\pi}{4}", "3*pi/4"), ("\\frac{5\\pi}{6}", "5*pi/6"),
    ("\\frac{7\\pi}{6}", "7*pi/6"), ("\\frac{5\\pi}{4}", "5*pi/4"), ("\\frac{4\\pi}{3}", "4*pi/3"),
    ("\\frac{5\\pi}{3}", "5*pi/3"), ("\\frac{7\\pi}{4}", "7*pi/4"), ("\\frac{11\\pi}{6}", "11*pi/6"),
]

_HALF = "\\frac{1}{2}"
_R2 = "\\frac{\\sqrt{2}}{2}"
_R3 = "\\frac{\\sqrt{3}}{2}"


def _neg(s):
    return "-" + s if not s.startswith("-") else s[1:]


# value tables keyed by the sympy-angle string
_SIN = {"pi/6": _HALF, "pi/4": _R2, "pi/3": _R3, "2*pi/3": _R3, "3*pi/4": _R2,
        "5*pi/6": _HALF, "7*pi/6": _neg(_HALF), "5*pi/4": _neg(_R2),
        "4*pi/3": _neg(_R3), "5*pi/3": _neg(_R3), "7*pi/4": _neg(_R2),
        "11*pi/6": _neg(_HALF)}
_COS = {"pi/6": _R3, "pi/4": _R2, "pi/3": _HALF, "2*pi/3": _neg(_HALF),
        "3*pi/4": _neg(_R2), "5*pi/6": _neg(_R3), "7*pi/6": _neg(_R3),
        "5*pi/4": _neg(_R2), "4*pi/3": _neg(_HALF), "5*pi/3": _HALF,
        "7*pi/4": _R2, "11*pi/6": _R3}

_VAL_SYMPY = {_HALF: "Rational(1,2)", _R2: "sqrt(2)/2", _R3: "sqrt(3)/2",
              _neg(_HALF): "-Rational(1,2)", _neg(_R2): "-sqrt(2)/2", _neg(_R3): "-sqrt(3)/2"}


def _g_sl_exact_values():
    """Exact values of sin / cos at standard angles across all four quadrants."""
    raws = []
    mags = [_HALF, _R2, _R3]
    for (func, table, other) in (("\\sin", _SIN, _COS), ("\\cos", _COS, _SIN)):
        for (ltx, ang) in _UC:
            v = table[ang]
            neg = v.startswith("-")
            mag = v[1:] if neg else v
            wrong_mags = [m for m in mags if m != mag]
            # distractors: sign flipped · right sign but the two WRONG reference
            # magnitudes (the 1/2 vs sqrt2/2 vs sqrt3/2 mix-up)
            dvals = [_neg(v)] + [("-" + m if neg else m) for m in wrong_mags]
            raws.append({
                "statement": "Find the exact value of $%s %s$." % (func, ltx),
                "correct": "$%s$" % v,
                "dvals": ["$%s$" % d for d in dvals],
                "explanation": "The reference angle and the quadrant give "
                               "$%s %s = %s$: fix the reference value first "
                               "($\\frac{1}{2}$, $\\frac{\\sqrt{2}}{2}$ or "
                               "$\\frac{\\sqrt{3}}{2}$), then the sign from the quadrant. "
                               "Half the errors here are the wrong reference value, half "
                               "the wrong sign."
                               % (func, ltx, v),
                "check": ["Eq(simplify(%s(%s) - (%s)), 0)"
                          % ("sin" if func == "\\sin" else "cos", ang, _VAL_SYMPY[v])],
            })
    return raws


def _g_sl_trig_count():
    """Number of solutions of a sin x = b (etc.) on [0, 2pi)."""
    cases = []
    for f in ("sin", "cos"):
        for (a, b) in ((2, 1), (2, -1), (1, 1), (1, -1), (2, 3), (2, -3), (3, 2), (4, 2), (3, -2), (5, 4)):
            r = Fraction(b, a)
            n = 0 if abs(r) > 1 else (1 if abs(r) == 1 else 2)
            cases.append((f, a, b, r, n))
    for c in (1, -1, 3, -2):
        cases.append(("tan", 1, c, Fraction(c), 2))
    raws = []
    for (f, a, b, r, n) in cases:
        eq = "%s%s x = %d" % ("" if a == 1 else str(a), "\\%s" % f, b)
        others = [x for x in (0, 1, 2, 3, 4) if x != n][:3]
        if f == "tan":
            reason = ("$\\tan x = %d$ has exactly one solution in each of two periods of "
                      "$\\tan$ inside $[0, 2\\pi)$ — two solutions in total." % b)
            checks = ["Eq(tan(atan(%d)), %d)" % (b, b)]
        elif n == 2:
            reason = ("$\\%s x = %s$ with $\\left|%s\\right| < 1$ crosses the %s curve twice "
                      "in one full turn." % (f, fmt(Rational(r.numerator, r.denominator)),
                                             fmt(Rational(r.numerator, r.denominator)), f))
            checks = ["Abs(Rational(%d,%d)) < 1" % (r.numerator, r.denominator)]
        elif n == 1:
            reason = ("$\\%s x = %s$ touches the extreme value of %s exactly once per turn."
                      % (f, fmt(Rational(r.numerator, r.denominator)), f))
            checks = ["Eq(Abs(Rational(%d,%d)), 1)" % (r.numerator, r.denominator)]
        else:
            reason = ("$\\left|%s\\right| > 1$ is outside the range of $\\%s$, so there are "
                      "no solutions." % (fmt(Rational(r.numerator, r.denominator)), f))
            checks = ["Abs(Rational(%d,%d)) > 1" % (r.numerator, r.denominator)]
        raws.append({
            "statement": "How many solutions does the equation $%s$ have for "
                         "$0 \\le x < 2\\pi$?" % eq,
            "correct": n,
            "dvals": others,
            "explanation": reason + " Sketch one period before counting — the graph answers "
                           "this faster than algebra.",
            "check": checks,
        })
    return raws


# ===========================================================================
# SL · Topic 4 — Statistics & Probability
# ===========================================================================

def _g_sl_mean_freq():
    """Mean from a frequency list."""
    raws = []
    # Uneven spacing on purpose: for evenly spaced scores the midrange equals
    # the unweighted average and two distractors collapse into one.
    value_sets = [(2, 3, 5, 8), (1, 2, 4, 7), (3, 4, 6, 9), (2, 4, 5, 9), (1, 3, 4, 8)]
    freq_sets = [(3, 5, 8, 4), (2, 6, 7, 5), (4, 4, 6, 6), (1, 7, 9, 3), (5, 3, 2, 6), (2, 8, 6, 4)]
    for vs in value_sets:
        for fs in freq_sets:
            n = sum(fs)
            total = sum(v * f for v, f in zip(vs, fs))
            mean = Rational(total, n)
            raws.append({
                "statement": "In a quiz, the scores $%d, %d, %d, %d$ were obtained by "
                             "$%d, %d, %d, %d$ students respectively. Find the mean score."
                             % (*vs, *fs),
                "correct": mean,
                # ignored the frequencies · divided by the number of distinct
                # scores · midrange instead of mean
                "dvals": [Rational(sum(vs), 4), Rational(total, 4),
                          Rational(vs[0] + vs[3], 2)],
                "explanation": "Total score $= %s = %d$ over $%d$ students, so the mean is "
                               "$\\dfrac{%d}{%d} = %s$. Averaging the four score VALUES "
                               "ignores how many students got each."
                               % (" + ".join("%d \\cdot %d" % (v, f) for v, f in zip(vs, fs)),
                                  total, n, total, n, fmt(mean)),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (total, n, mean.p, mean.q)],
            })
    return raws


def _g_sl_union():
    """P(A u B) = P(A) + P(B) - P(A n B)."""
    raws = []
    for D in (10, 12, 20, 8):
        for pa in range(3, D - 2):
            for pb in range(2, pa + 1):
                for pab in (1, 2):
                    if pab >= pb or pa + pb - pab > D or pa == pb:
                        continue
                    u = Rational(pa + pb - pab, D)
                    raws.append({
                        "statement": "Events $A$ and $B$ satisfy $P(A) = %s$, $P(B) = %s$ and "
                                     "$P(A \\cap B) = %s$. Find $P(A \\cup B)$."
                                     % (fmt(Rational(pa, D)), fmt(Rational(pb, D)),
                                        fmt(Rational(pab, D))),
                        "correct": u,
                        # forgot to subtract the intersection · subtracted it
                        # twice · added the intersection
                        "dvals": [Rational(pa + pb, D), Rational(pa + pb - 2 * pab, D),
                                  Rational(pa + pb + pab, D)],
                        "explanation": "$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = "
                                       "\\dfrac{%d}{%d} + \\dfrac{%d}{%d} - \\dfrac{%d}{%d} = "
                                       "%s$. Adding without subtracting counts the overlap "
                                       "twice."
                                       % (pa, D, pb, D, pab, D, fmt(u)),
                        "check": ["Eq(Rational(%d,%d) + Rational(%d,%d) - Rational(%d,%d), "
                                  "Rational(%d,%d))" % (pa, D, pb, D, pab, D, u.p, u.q)],
                    })
    return raws


def _g_sl_independent():
    """P(A n B) = P(A) P(B) for independent events."""
    pairs = [(Rational(1, 2), Rational(1, 3)), (Rational(1, 4), Rational(2, 3)),
             (Rational(2, 5), Rational(1, 2)), (Rational(1, 3), Rational(1, 4)),
             (Rational(3, 5), Rational(1, 3)), (Rational(2, 3), Rational(1, 5)),
             (Rational(1, 2), Rational(1, 5)), (Rational(3, 4), Rational(1, 3)),
             (Rational(2, 5), Rational(1, 4)), (Rational(1, 6), Rational(1, 2)),
             (Rational(5, 6), Rational(1, 5)), (Rational(1, 4), Rational(1, 3)),
             (Rational(3, 10), Rational(1, 3)), (Rational(2, 3), Rational(3, 10)),
             (Rational(1, 5), Rational(1, 2)), (Rational(4, 5), Rational(1, 4)),
             (Rational(1, 2), Rational(2, 5)), (Rational(5, 8), Rational(1, 5)),
             (Rational(3, 8), Rational(1, 3)), (Rational(7, 10), Rational(1, 7)),
             (Rational(1, 3), Rational(1, 5)), (Rational(2, 7), Rational(1, 2)),
             (Rational(3, 7), Rational(1, 3)), (Rational(5, 9), Rational(1, 5)),
             (Rational(4, 9), Rational(1, 4)), (Rational(1, 8), Rational(2, 3)),
             (Rational(5, 12), Rational(1, 5)), (Rational(7, 12), Rational(1, 7))]
    raws = []
    for (p, q) in pairs:
        both = p * q
        raws.append({
            "statement": "Independent events $A$ and $B$ have $P(A) = %s$ and $P(B) = %s$. "
                         "Find $P(A \\cap B)$." % (fmt(p), fmt(q)),
            "correct": both,
            # added · computed the union · averaged
            "dvals": [p + q, p + q - p * q, (p + q) / 2],
            "explanation": "For independent events the joint probability multiplies: "
                           "$P(A \\cap B) = P(A)\\,P(B) = %s \\cdot %s = %s$. "
                           "$%s$ is $P(A \\cup B)$, not the intersection."
                           % (fmt(p), fmt(q), fmt(both), fmt(p + q - p * q)),
            "check": ["Eq(Rational(%d,%d)*Rational(%d,%d), Rational(%d,%d))"
                      % (p.p, p.q, q.p, q.q, both.p, both.q)],
        })
    return raws


def _g_sl_conditional():
    """P(plays | girl) from a two-way table, stated in words."""
    raws = []
    for a in (6, 8, 10, 12):          # girls who play
        for b in (4, 5, 9, 7):        # girls who don't
            for c in (5, 7, 11):      # boys who play
                for d in (6, 10, 8):  # boys who don't
                    N = a + b + c + d
                    cond = Rational(a, a + b)
                    if cond == Rational(a, a + c) or cond == Rational(a + b, N):
                        continue
                    raws.append({
                        "statement": "In a class, $%d$ girls play an instrument and $%d$ do "
                                     "not; $%d$ boys play and $%d$ do not. A student is chosen "
                                     "at random. Given that the student is a girl, find the "
                                     "probability that she plays an instrument."
                                     % (a, b, c, d),
                        "correct": cond,
                        # conditioned on the wrong margin (players) · the joint
                        # probability · the marginal P(girl)
                        "dvals": [Rational(a, a + c), Rational(a, N), Rational(a + b, N)],
                        "explanation": "Conditioning on \"girl\" restricts the sample space to "
                                       "the $%d$ girls: $P(\\text{plays} \\mid \\text{girl}) = "
                                       "\\dfrac{%d}{%d} = %s$. $\\dfrac{%d}{%d}$ is the JOINT "
                                       "probability — dividing by the whole class is the "
                                       "standard trap."
                                       % (a + b, a, a + b, fmt(cond), a, N),
                        "check": ["Eq(Rational(%d, %d + %d), Rational(%d,%d))"
                                  % (a, a, b, cond.p, cond.q)],
                    })
    return raws


def _g_sl_binomial_dist():
    """P(X = k) for X ~ B(n, p)."""
    from math import comb
    # p = 1/2 makes p and q interchangeable and n = 2k makes the exponents
    # interchangeable — either way the swapped-exponent distractor equals the
    # answer, so both stay out of the grid.
    ps = [Rational(1, 3), Rational(1, 4), Rational(2, 5), Rational(1, 5),
          Rational(2, 3), Rational(3, 5)]
    raws = []
    for n in (4, 5, 6, 7):
        for k in (2, 3):
            for p in ps:
                if 2 * k == n:
                    continue
                q = 1 - p
                prob = comb(n, k) * p ** k * q ** (n - k)
                raws.append({
                    "statement": "A biased coin lands heads with probability $%s$ on each "
                                 "independent toss. It is tossed $%d$ times. Find the "
                                 "probability of exactly $%d$ heads." % (fmt(p), n, k),
                    "correct": prob,
                    # forgot the binomial coefficient · forgot the failures ·
                    # swapped the exponents
                    "dvals": [p ** k * q ** (n - k), comb(n, k) * p ** k,
                              comb(n, k) * p ** (n - k) * q ** k],
                    "explanation": "$X \\sim B(%d, %s)$, so $P(X = %d) = \\binom{%d}{%d} "
                                   "\\left(%s\\right)^{%d}\\left(%s\\right)^{%d} = %s$. "
                                   "Without the $\\binom{%d}{%d} = %d$ factor you count only "
                                   "ONE ordering of the heads."
                                   % (n, fmt(p), k, n, k, fmt(p), k, fmt(q), n - k, fmt(prob),
                                      n, k, comb(n, k)),
                    "check": ["Eq(binomial(%d,%d)*Rational(%d,%d)**%d*Rational(%d,%d)**%d, "
                              "Rational(%d,%d))"
                              % (n, k, p.p, p.q, k, q.p, q.q, n - k, prob.p, prob.q)],
                })
    return raws


# ===========================================================================
# SL · Topic 5 — Calculus
# ===========================================================================

def _g_sl_derivative_value():
    """f(x) = a x^3 + b x + c, find f'(t)."""
    raws = []
    for a in (1, 2, -1, 3):
        for b in (2, -3, 5, -4):
            for c in (1, -2, 4):
                for t in (1, 2, -1, -2):
                    d = 3 * a * t * t + b
                    raws.append({
                        "statement": "Let $f(x) = %s$. Find $f'(%d)$."
                                     % (cubic(a, b, c), t),
                        "correct": d,
                        # evaluated f itself · kept the constant term in f' ·
                        # forgot to multiply by the exponent
                        "dvals": [a * t ** 3 + b * t + c, d + c, a * t * t + b],
                        "explanation": "$f'(x) = %dx^2 %s %d$, so $f'(%d) = %d \\cdot %d %s %d "
                                       "= %d$. The constant term differentiates to zero — "
                                       "carrying the $%d$ into $f'$ is the usual slip."
                                       % (3 * a, "+" if b >= 0 else "-", abs(b), t,
                                          3 * a, t * t, "+" if b >= 0 else "-", abs(b), d, c),
                        "check": ["Eq(%d*3*(%d)**2 + (%d), %d)" % (a, t, b, d)],
                    })
    return raws


def cubic(a, b, c):
    """Render a x^3 + b x + c."""
    s = "x^3" if a == 1 else ("-x^3" if a == -1 else "%dx^3" % a)
    if b != 0:
        xb = "x" if abs(b) == 1 else "%dx" % abs(b)
        s += " %s %s" % ("+" if b > 0 else "-", xb)
    if c != 0:
        s += " %s %d" % ("+" if c > 0 else "-", abs(c))
    return s


def _g_sl_tangent():
    """Tangent to f(x) = x^2 + bx + c at x = p."""
    raws = []
    for b in (2, -2, 4, -4, 6):
        for c in (1, -3, 5, 2):
            for p in (1, 2, -1, 3):
                m = 2 * p + b
                if m == 0 or m == 2 * p:
                    continue
                y0 = p * p + b * p + c
                icpt = y0 - m * p
                raws.append({
                    "statement": "Find the equation of the tangent to the curve "
                                 "$y = %s$ at the point where $x = %d$."
                                 % (quad_full(1, b, c), p),
                    "correct": "$y = %s$" % lin(m, icpt),
                    # used f(p) as the y-intercept · sign slip in the intercept ·
                    # forgot b when differentiating
                    "dvals": ["$y = %s$" % lin(m, y0),
                              "$y = %s$" % lin(m, y0 + m * p),
                              "$y = %s$" % lin(2 * p, y0 - 2 * p * p)],
                    "explanation": "$\\dfrac{dy}{dx} = %s$, so the gradient at $x = %d$ is "
                                   "$m = %d$, and the point is $(%d, %d)$. Then $y - %d = "
                                   "%d(x - %d)$ gives $y = %s$. The $y$-intercept is NOT "
                                   "$f(%d)$ unless the point of tangency is on the $y$-axis."
                                   % (lin(2, b), p, m, p, y0, y0, m, p, lin(m, icpt), p),
                    "check": ["Eq(2*(%d) + (%d), %d)" % (p, b, m),
                              "Eq((%d)**2 + (%d)*(%d) + (%d), %d)" % (p, b, p, c, y0),
                              "Eq(%d*(%d) + (%d), %d)" % (m, p, icpt, y0)],
                })
    return raws


def quad_full(a, b, c):
    """Render ax^2 + bx + c (a = 1 only here)."""
    s = "x^2"
    if b != 0:
        s += " %s %s" % ("+" if b > 0 else "-", "x" if abs(b) == 1 else "%dx" % abs(b))
    if c != 0:
        s += " %s %d" % ("+" if c > 0 else "-", abs(c))
    return s


def _g_sl_at_rest():
    """s(t) = bt - a t^2; the particle is at rest at t = b/(2a)."""
    out = []
    for a in (1, 2, 3, 4, 5):
        for b in (4, 6, 8, 10, 12, 14, 5, 7, 9):
            if b == 2 * a:
                continue  # keeps the inverted distractor distinct
            t0 = Rational(b, 2 * a)
            d_forgot2 = Rational(b, a)     # v = b - at instead of b - 2at; the
            #                                s(t) = 0 root is the SAME value, so
            #                                one distractor covers both errors
            d_invert = Rational(2 * a, b)  # inverted the fraction
            d_v1 = b - 2 * a               # computed v(1) instead of solving v = 0
            out.append({
                "statement": "A particle moves in a straight line with displacement "
                             "$s(t) = %dt - %st^2$ metres after $t$ seconds. Find the time "
                             "at which the particle is instantaneously at rest."
                             % (b, "" if a == 1 else str(a)),
                "correct": t0,
                # forgot the 2 when differentiating (also the s = 0 root) ·
                # inverted the fraction · computed v(1) instead of solving v = 0
                "dvals": [d_forgot2, d_invert, d_v1],
                "explanation": "At rest means $v = \\dfrac{ds}{dt} = 0$: $v(t) = %d - %dt$, so "
                               "$t = \\dfrac{%d}{%d} = %s$ s. Solving $s(t) = 0$ instead gives "
                               "$t = %s$ — that is when the particle RETURNS, not when it "
                               "stops."
                               % (b, 2 * a, b, 2 * a, fmt(t0), fmt(d_forgot2)),
                "check": ["Eq(%d - %d*Rational(%d,%d), 0)" % (b, 2 * a, t0.p, t0.q)],
            })
    return out


def _g_sl_definite_integral():
    """Integral of 3x^2 + c from 0 to b."""
    raws = []
    for b in (1, 2, 3, 4):
        for c in (1, 2, 4, 5, 7, -2, -3, 8):
            v = b ** 3 + c * b
            raws.append({
                "statement": "Evaluate $\\displaystyle\\int_0^{%d} (3x^2 %s %d)\\,dx$."
                             % (b, "+" if c >= 0 else "-", abs(c)),
                "correct": v,
                # differentiated instead of integrating · forgot the +c term ·
                # evaluated the integrand at b and multiplied by b
                "dvals": [6 * b, b ** 3, (3 * b * b + c) * b],
                "explanation": "An antiderivative is $x^3 %s %dx$, so the integral is "
                               "$\\left[x^3 %s %dx\\right]_0^{%d} = %d %s %d = %d$. "
                               "Differentiating instead of integrating gives $6x$ evaluated "
                               "at $%d$, i.e. $%d$."
                               % ("+" if c >= 0 else "-", abs(c),
                                  "+" if c >= 0 else "-", abs(c), b,
                                  b ** 3, "+" if c >= 0 else "-", abs(c * b), v, b, 6 * b),
                "check": ["Eq(integrate(3*x**2 + (%d), (x, 0, %d)), %d)" % (c, b, v)],
            })
    return raws


def _g_sl_area_under():
    """Area between y = kx(b - x) and the x-axis, from 0 to b: k b^3 / 6."""
    raws = []
    for k in (1, 2, 3):
        for b in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12):
            area = Rational(k * b ** 3, 6)
            raws.append({
                "statement": "The curve $y = %sx(%d - x)$ meets the $x$-axis at $x = 0$ and "
                             "$x = %d$. Find the area of the region enclosed by the curve "
                             "and the $x$-axis." % ("" if k == 1 else str(k), b, b),
                "correct": area,
                # kept only the -x^3/3 magnitude · kept only the bx^2/2 term ·
                # halved the correct answer
                "dvals": [Rational(k * b ** 3, 3), Rational(k * b ** 3, 2),
                          Rational(k * b ** 3, 12)],
                "explanation": "Area $= \\displaystyle\\int_0^{%d} %s(%dx - x^2)\\,dx = "
                               "%s\\left[\\frac{%dx^2}{2} - \\frac{x^3}{3}\\right]_0^{%d} = "
                               "%s$. Both terms matter: dropping either one leaves "
                               "$\\frac{%d b^3}{2}$- or $\\frac{%d b^3}{3}$-type values."
                               % (b, "" if k == 1 else str(k), b,
                                  "" if k == 1 else str(k), b, b, fmt(area), k, k),
                "check": ["Eq(integrate(%d*x*(%d - x), (x, 0, %d)), Rational(%d,%d))"
                          % (k, b, b, area.p, area.q)],
            })
    return raws


# ===========================================================================
# HL · Topic 1 — Number & Algebra (complex numbers, counting)
# ===========================================================================

def _cnum(a, b):
    """Render a + bi."""
    if b == 0:
        return str(a)
    im = "i" if abs(b) == 1 else "%di" % abs(b)
    if a == 0:
        return im if b > 0 else "-" + im
    return "%d %s %s" % (a, "+" if b > 0 else "-", im)


def _g_hl_complex_product():
    """Re / Im of (a+bi)(c+di)."""
    raws = []
    for (a, b) in ((2, 3), (1, -2), (3, 1), (-2, 5), (4, -3)):
        for (c, d) in ((1, 2), (3, -1), (2, 5), (-1, 3)):
            rp = a * c - b * d
            ip = a * d + b * c
            for (part, val, wrong_sign) in (("\\mathrm{Re}", rp, a * c + b * d),
                                            ("\\mathrm{Im}", ip, a * d - b * c)):
                raws.append({
                    "statement": "Let $z = (%s)(%s)$. Find $%s(z)$."
                                 % (_cnum(a, b), _cnum(c, d), part),
                    "correct": val,
                    # sign slip on i^2 = -1 · quoted the other part · multiplied
                    # only the matching components
                    "dvals": [wrong_sign, ip if part == "\\mathrm{Re}" else rp,
                              a * c if part == "\\mathrm{Re}" else b * d],
                    "explanation": "Expand: $(%s)(%s) = %s$, using $i^2 = -1$. So "
                                   "$\\mathrm{Re}(z) = %d$ and $\\mathrm{Im}(z) = %d$. "
                                   "Treating $i^2$ as $+1$ flips the sign of the $%d$ term."
                                   % (_cnum(a, b), _cnum(c, d), _cnum(rp, ip), rp, ip, b * d),
                    "check": ["Eq(re((%d + %d*I)*(%d + %d*I)), %d)" % (a, b, c, d, rp),
                              "Eq(im((%d + %d*I)*(%d + %d*I)), %d)" % (a, b, c, d, ip)],
                })
    return raws


def _g_hl_modulus():
    """|a + bi| from scaled Pythagorean pairs."""
    trips = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15),
             (7, 24, 25), (20, 21, 29), (12, 16, 20), (9, 40, 41), (10, 24, 26),
             (15, 20, 25), (18, 24, 30)]
    raws = []
    for (x, y, m) in trips:
        for (a, b) in ((x, y), (x, -y), (-x, y)):
            raws.append({
                "statement": "Find $|z|$ for $z = %s$." % _cnum(a, b),
                "correct": m,
                # forgot the square root · added the components · used the real
                # part's absolute value
                "dvals": [m * m, abs(a) + abs(b), abs(a)],
                "explanation": "$|z| = \\sqrt{a^2 + b^2} = \\sqrt{%d + %d} = \\sqrt{%d} = %d$. "
                               "The modulus needs the square root — $%d$ is $|z|^2$."
                               % (a * a, b * b, m * m, m, m * m),
                "check": ["Eq(Abs(%d + (%d)*I), %d)" % (a, b, m)],
            })
    return raws


# (a, b multiplier of sqrt3 flag, latex of z given scale k) is fiddly; use a
# fixed catalogue of directions with exact principal arguments.
_ARG_DIRS = [
    # (re, im, uses_sqrt3, latex builder args, arg latex, sympy arg)
    ((1, 1), "\\frac{\\pi}{4}", "pi/4"),
    ((-1, 1), "\\frac{3\\pi}{4}", "3*pi/4"),
    ((1, -1), "-\\frac{\\pi}{4}", "-pi/4"),
    ((-1, -1), "-\\frac{3\\pi}{4}", "-3*pi/4"),
]

_ARG_SQRT3 = [
    # (re coef, im coef with sqrt3 on which part) -> z = k(1 + sqrt3 i) etc.
    ("1", "\\sqrt{3}", "pi/3", "1 + sqrt(3)*I"),
    ("-1", "\\sqrt{3}", "2*pi/3", "-1 + sqrt(3)*I"),
    ("1", "-\\sqrt{3}", "-pi/3", "1 - sqrt(3)*I"),
    ("\\sqrt{3}", "1", "pi/6", "sqrt(3) + I"),
    ("-\\sqrt{3}", "1", "5*pi/6", "-sqrt(3) + I"),
    ("\\sqrt{3}", "-1", "-pi/6", "sqrt(3) - I"),
]


def _arg_latex(s):
    """LaTeX for the sympy angle strings used below."""
    table = {"pi/4": "\\frac{\\pi}{4}", "3*pi/4": "\\frac{3\\pi}{4}",
             "-pi/4": "-\\frac{\\pi}{4}", "-3*pi/4": "-\\frac{3\\pi}{4}",
             "pi/3": "\\frac{\\pi}{3}", "2*pi/3": "\\frac{2\\pi}{3}",
             "-pi/3": "-\\frac{\\pi}{3}", "pi/6": "\\frac{\\pi}{6}",
             "5*pi/6": "\\frac{5\\pi}{6}", "-pi/6": "-\\frac{\\pi}{6}"}
    return table[s]


def _g_hl_argument():
    """Principal argument of z on the standard directions."""
    raws = []
    for k in (1, 2, 3):
        for ((x, y), ltx, ang) in _ARG_DIRS:
            a, b = k * x, k * y
            # distractors: reference angle pi/4 with wrong sign/quadrant
            others = [o for o in ("pi/4", "3*pi/4", "-pi/4", "-3*pi/4") if o != ang][:3]
            raws.append({
                "statement": "Find the principal argument of $z = %s$, where "
                             "$-\\pi < \\arg z \\le \\pi$." % _cnum(a, b),
                "correct": "$%s$" % ltx,
                "dvals": ["$%s$" % _arg_latex(o) for o in others],
                "explanation": "$z$ lies in the quadrant with $\\mathrm{Re}(z) %s 0$ and "
                               "$\\mathrm{Im}(z) %s 0$, with reference angle "
                               "$\\frac{\\pi}{4}$ since $|\\mathrm{Re}| = |\\mathrm{Im}|$. "
                               "So $\\arg z = %s$. Plot the point first — the quadrant "
                               "decides everything."
                               % (">" if a > 0 else "<", ">" if b > 0 else "<", ltx),
                "check": ["Eq(arg(%d + (%d)*I), %s)" % (a, b, ang)],
            })
    for k in (1, 2):
        for (reltx, imltx, ang, zexpr) in _ARG_SQRT3:
            kz = "%d" % k if k > 1 else ""
            zltx = "%s%s + %si" % (kz, reltx, imltx) if not imltx.startswith("-") \
                else "%s%s - %si" % (kz, reltx, imltx[1:])
            if k > 1:
                zltx = "%d(%s)" % (k, ("%s + %si" % (reltx, imltx)) if not imltx.startswith("-")
                                   else ("%s - %si" % (reltx, imltx[1:])))
            others = [o for o in ("pi/3", "2*pi/3", "-pi/3", "pi/6", "5*pi/6", "-pi/6")
                      if o != ang][:3]
            raws.append({
                "statement": "Find the principal argument of $z = %s$, where "
                             "$-\\pi < \\arg z \\le \\pi$." % zltx,
                "correct": "$%s$" % _arg_latex(ang),
                "dvals": ["$%s$" % _arg_latex(o) for o in others],
                "explanation": "The point has reference angle $\\frac{\\pi}{6}$ or "
                               "$\\frac{\\pi}{3}$ depending on which component carries the "
                               "$\\sqrt{3}$; here $\\arg z = %s$. Sketch it — sign and "
                               "quadrant first, reference angle second." % _arg_latex(ang),
                "check": ["Eq(arg(%d*(%s)), %s)" % (k, zexpr, ang)],
            })
    return raws


def _g_hl_combinations():
    """nCr counts, including a 'must include one specific person' variant."""
    from math import comb, perm
    raws = []
    for n in (7, 8, 9, 10, 11, 12):
        for k in (2, 3, 4):
            raws.append({
                "statement": "A committee of $%d$ people is to be chosen from a group of "
                             "$%d$. In how many ways can this be done?" % (k, n),
                "correct": comb(n, k),
                # counted ordered selections · chose k-1 · multiplied n by k
                "dvals": [perm(n, k), comb(n, k - 1), n * k],
                "explanation": "Order does not matter, so the count is $\\binom{%d}{%d} = %d$. "
                               "$%d$ is $^{%d}P_{%d}$ — the ORDERED count, larger by the "
                               "$%d!$ orderings of each committee."
                               % (n, k, comb(n, k), perm(n, k), n, k, k),
                "check": ["Eq(binomial(%d,%d), %d)" % (n, k, comb(n, k))],
            })
            raws.append({
                "statement": "A team of $%d$ is chosen from $%d$ players. The captain must "
                             "be in the team. In how many ways can the team be chosen?"
                             % (k, n),
                "correct": comb(n - 1, k - 1),
                # ignored the restriction · excluded the captain but kept k ·
                # subtracted instead of conditioning
                "dvals": [comb(n, k), comb(n - 1, k), comb(n, k) - k],
                "explanation": "The captain's seat is fixed, leaving $\\binom{%d}{%d} = %d$ "
                               "ways to fill the rest. $\\binom{%d}{%d}$ ignores the "
                               "restriction entirely."
                               % (n - 1, k - 1, comb(n - 1, k - 1), n, k),
                "check": ["Eq(binomial(%d,%d), %d)" % (n - 1, k - 1, comb(n - 1, k - 1))],
            })
    return raws


# ===========================================================================
# HL · Topic 2 — Functions (polynomials)
# ===========================================================================

def _g_hl_remainder():
    """Remainder of x^3 + bx^2 + cx + d divided by (x - a)."""
    raws = []
    for a in (1, 2, -1, -2, 3):
        for b in (1, -2, 3):
            for c in (2, -3, 4):
                for d in (1, -4, 5):
                    r = a ** 3 + b * a * a + c * a + d
                    r_wrong = (-a) ** 3 + b * a * a - c * a + d  # evaluated at -a
                    raws.append({
                        "statement": "Find the remainder when $p(x) = %s$ is divided by "
                                     "$(x %s %d)$."
                                     % (poly3(1, b, c, d), "-" if a > 0 else "+", abs(a)),
                        "correct": r,
                        # evaluated p(-a) — THE remainder-theorem sign trap ·
                        # quoted the constant term · dropped the cubic term
                        "dvals": [r_wrong, d, b * a * a + c * a + d],
                        "explanation": "By the remainder theorem the remainder is $p(%d) = %d$. "
                                       "Dividing by $(x %s %d)$ means evaluating at $x = %d$ — "
                                       "evaluating at $%d$ instead gives $%d$."
                                       % (a, r, "-" if a > 0 else "+", abs(a), a, -a, r_wrong),
                        "check": ["Eq((%d)**3 + (%d)*(%d)**2 + (%d)*(%d) + (%d), %d)"
                                  % (a, b, a, c, a, d, r)],
                    })
    return raws


def poly3(a, b, c, d):
    """Render x^3 + bx^2 + cx + d (a = 1 only here)."""
    s = "x^3"
    if b != 0:
        s += " %s %s" % ("+" if b > 0 else "-",
                         "x^2" if abs(b) == 1 else "%dx^2" % abs(b))
    if c != 0:
        s += " %s %s" % ("+" if c > 0 else "-", "x" if abs(c) == 1 else "%dx" % abs(c))
    if d != 0:
        s += " %s %d" % ("+" if d > 0 else "-", abs(d))
    return s


def _g_hl_vieta_cubic():
    """Sum of roots of a x^3 + b x^2 + c x + d = 0."""
    raws = []
    for a in (2, 3, 4):
        for b in (3, -4, 6, -8, 5, -9, 12):
            for (c, d) in ((1, -2), (-3, 5), (2, 7)):
                s = Rational(-b, a)
                raws.append({
                    "statement": "Find the sum of the roots of the equation "
                                 "$%s = 0$." % poly3_lead(a, b, c, d),
                    "correct": s,
                    # sign slip · forgot to divide by a · used -d/a (the
                    # product formula, up to sign)
                    "dvals": [Rational(b, a), -b, Rational(-d, a)],
                    "explanation": "For $ax^3 + bx^2 + cx + d = 0$ the roots sum to "
                                   "$-\\dfrac{b}{a} = -\\dfrac{%d}{%d} = %s$. "
                                   "$-\\dfrac{d}{a}$ is (minus) the PRODUCT of the roots."
                                   % (b, a, fmt(s)),
                    "check": ["Eq(Rational(-(%d), %d), Rational(%d,%d))" % (b, a, s.p, s.q)],
                })
    return raws


def poly3_lead(a, b, c, d):
    """Render ax^3 + bx^2 + cx + d."""
    s = "%dx^3" % a
    if b != 0:
        s += " %s %s" % ("+" if b > 0 else "-",
                         "x^2" if abs(b) == 1 else "%dx^2" % abs(b))
    if c != 0:
        s += " %s %s" % ("+" if c > 0 else "-", "x" if abs(c) == 1 else "%dx" % abs(c))
    if d != 0:
        s += " %s %d" % ("+" if d > 0 else "-", abs(d))
    return s


def _g_hl_factor_k():
    """(x - a) is a factor of x^3 + kx + am  =>  k = -(a^2 + m)."""
    raws = []
    for a in (1, 2, -1, -2, 3, -3):
        for m in (1, 2, 3, -1, -2, 4, 5, -4):
            c = a * m
            k = -(a * a + m)
            if k == 0 or m == 0:
                continue
            raws.append({
                "statement": "Given that $(x %s %d)$ is a factor of "
                             "$p(x) = x^3 + kx %s %d$, find the value of $k$."
                             % ("-" if a > 0 else "+", abs(a), "+" if c >= 0 else "-", abs(c)),
                "correct": k,
                # sign flipped · evaluated at -a · read k as -c/a
                "dvals": [-k, m - a * a, -m],
                "explanation": "A factor means $p(%d) = 0$: $%d + %dk %s %d = 0$, so "
                               "$k = %d$. Substituting $x = %d$ instead gives the trap value "
                               "$%d$."
                               % (a, a ** 3, a, "+" if c >= 0 else "-", abs(c), k, -a, m - a * a),
                "check": ["Eq((%d)**3 + (%d)*(%d) + (%d), 0)" % (a, k, a, c)],
            })
    return raws


def _g_hl_sum_sq_roots():
    """alpha^2 + beta^2 = p^2 - 2q for x^2 + px + q = 0."""
    raws = []
    for p in (1, 2, 3, -1, -2, -3, 4, -4):
        for q in (1, 2, -1, -2, 3, -3, 5):
            v = p * p - 2 * q
            raws.append({
                "statement": "The equation $x^2 %s %sx %s %d = 0$ has roots $\\alpha$ and "
                             "$\\beta$. Find $\\alpha^2 + \\beta^2$."
                             % ("+" if p > 0 else "-", "" if abs(p) == 1 else str(abs(p)),
                                "+" if q > 0 else "-", abs(q)),
                "correct": v,
                # sign slip on the 2q term · subtracted q once · forgot q entirely
                "dvals": [p * p + 2 * q, p * p - q, p * p],
                "explanation": "$\\alpha + \\beta = %d$ and $\\alpha\\beta = %d$, so "
                               "$\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta "
                               "= %d - %d = %d$. The cross term $2\\alpha\\beta$ must be "
                               "subtracted — once, and with its sign."
                               % (-p, q, p * p, 2 * q, v),
                "check": ["Eq((%d)**2 - 2*(%d), %d)" % (p, q, v),
                          # the identity holds for the actual roots
                          "Eq(simplify((-(%d)/2 + sqrt((%d)**2 - 4*(%d))/2)**2 + "
                          "(-(%d)/2 - sqrt((%d)**2 - 4*(%d))/2)**2 - (%d)), 0)"
                          % (p, p, q, p, p, q, v)],
            })
    return raws


# ===========================================================================
# HL · Topic 3 — Geometry & Trigonometry (vectors, compound angles)
# ===========================================================================

_VEC3 = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (4, 4, 7, 9), (2, 6, 9, 11),
         (6, 6, 7, 11), (3, 4, 12, 13), (2, 5, 14, 15), (8, 9, 12, 17),
         (1, 12, 12, 17), (2, 4, 4, 6), (4, 6, 12, 14), (3, 6, 6, 9), (6, 8, 24, 26)]


def _g_hl_vec_magnitude():
    """|v| for 3D vectors with integer magnitude."""
    raws = []
    for (x, y, z, m) in _VEC3:
        for (sx, sy, sz) in ((1, 1, 1), (-1, 1, 1), (1, -1, 1)):
            a, b, c = sx * x, sy * y, sz * z
            raws.append({
                "statement": "Find the magnitude of the vector "
                             "$\\begin{pmatrix} %d \\\\ %d \\\\ %d \\end{pmatrix}$."
                             % (a, b, c),
                "correct": m,
                # forgot the square root · summed the absolute components ·
                # took the largest component
                "dvals": [m * m, abs(a) + abs(b) + abs(c), max(abs(a), abs(b), abs(c))],
                "explanation": "$|\\mathbf{v}| = \\sqrt{%d^2 + %d^2 + %d^2} = \\sqrt{%d} "
                               "= %d$. Signs vanish when squaring; $%d$ is $|\\mathbf{v}|^2$."
                               % (a, b, c, m * m, m, m * m),
                "check": ["Eq(sqrt((%d)**2 + (%d)**2 + (%d)**2), %d)" % (a, b, c, m)],
            })
    return raws


def _g_hl_dot_perp():
    """u . v = 0: find k — pick a,b,d,e freely, then c dividing s = ad + be."""
    out = []
    for (a, b) in ((2, 3), (1, -4), (3, 2), (-2, 5), (4, 1), (2, -5), (5, 2),
                   (3, -1), (1, 6), (4, 3)):
        for (d, e) in ((3, 1), (2, -3), (1, 5), (4, -1), (-2, 3), (2, 5), (3, 4)):
            s = a * d + b * e
            if s == 0:
                continue
            for cc in (2, 3, -2, 4, 6, -3, -4, 5):
                if cc in (1, -1) or s % cc != 0:
                    continue
                m = s // cc
                if m in (0,) or cc * m == -m:  # c = -1 handled above
                    continue
                k = -m
                if k == m or k == s or k == -s or m == -s or s == m:
                    continue
                out.append({
                    "statement": "The vectors $\\begin{pmatrix} %d \\\\ %d \\\\ %d "
                                 "\\end{pmatrix}$ and $\\begin{pmatrix} %d \\\\ %d \\\\ k "
                                 "\\end{pmatrix}$ are perpendicular. Find $k$."
                                 % (a, b, cc, d, e),
                    "correct": k,
                    # sign slip at the last step · stopped at the partial sum ·
                    # forgot to divide by the third component
                    "dvals": [m, s, -s],
                    "explanation": "Perpendicular means the scalar product is zero: "
                                   "$%d \\cdot %d + %d \\cdot %d + %dk = 0$, so "
                                   "$%d + %dk = 0$ and $k = %d$. Losing the minus sign at "
                                   "the last step gives $%d$."
                                   % (a, d, b, e, cc, s, cc, k, m),
                    "check": ["Eq(%d*%d + %d*%d + %d*(%d), 0)" % (a, d, b, e, cc, k)],
                })
    return out


_VEC2 = [(3, 4, 5), (4, 3, 5), (-3, 4, 5), (6, 8, 10), (5, 12, 13), (12, 5, 13),
         (8, 15, 17), (15, 8, 17), (7, 24, 25), (20, 21, 29), (9, 12, 15)]


def _g_hl_vec_angle():
    """cos(theta) between two 2D vectors with integer magnitudes."""
    raws = []
    for i, (x1, y1, m1) in enumerate(_VEC2):
        for (x2, y2, m2) in _VEC2[i + 1:]:
            dot = x1 * x2 + y1 * y2
            cross = abs(x1 * y2 - y1 * x2)
            if dot == 0 or dot == cross:
                continue
            cosv = Rational(dot, m1 * m2)
            raws.append({
                "statement": "Let $\\mathbf{u} = \\begin{pmatrix} %d \\\\ %d \\end{pmatrix}$ "
                             "and $\\mathbf{v} = \\begin{pmatrix} %d \\\\ %d \\end{pmatrix}$, "
                             "and let $\\theta$ be the angle between them. Find "
                             "$\\cos\\theta$." % (x1, y1, x2, y2),
                "correct": cosv,
                # sign flipped · divided by the SUM of magnitudes · computed
                # sin(theta) instead
                "dvals": [-cosv, Rational(dot, m1 + m2), Rational(cross, m1 * m2)],
                "explanation": "$\\cos\\theta = \\dfrac{\\mathbf{u} \\cdot \\mathbf{v}}"
                               "{|\\mathbf{u}||\\mathbf{v}|} = \\dfrac{%d}{%d \\cdot %d} = "
                               "%s$. The magnitudes MULTIPLY in the denominator — adding "
                               "them gives $%s$."
                               % (dot, m1, m2, fmt(cosv), fmt(Rational(dot, m1 + m2))),
                "check": ["Eq(%d*%d + %d*%d, %d)" % (x1, x2, y1, y2, dot),
                          "Eq(Rational(%d, %d*%d), Rational(%d,%d))"
                          % (dot, m1, m2, cosv.p, cosv.q)],
            })
    return raws


_CA_FAMILY = ["\\frac{\\sqrt{6} + \\sqrt{2}}{4}", "\\frac{\\sqrt{6} - \\sqrt{2}}{4}",
              "\\frac{\\sqrt{2} - \\sqrt{6}}{4}", "-\\frac{\\sqrt{6} + \\sqrt{2}}{4}"]
_CA_SYM = {_CA_FAMILY[0]: "(sqrt(6)+sqrt(2))/4", _CA_FAMILY[1]: "(sqrt(6)-sqrt(2))/4",
           _CA_FAMILY[2]: "(sqrt(2)-sqrt(6))/4", _CA_FAMILY[3]: "-(sqrt(6)+sqrt(2))/4"}

_TAN_FAMILY = ["2 + \\sqrt{3}", "2 - \\sqrt{3}", "\\sqrt{3} - 2", "-2 - \\sqrt{3}"]
_TAN_SYM = {_TAN_FAMILY[0]: "2 + sqrt(3)", _TAN_FAMILY[1]: "2 - sqrt(3)",
            _TAN_FAMILY[2]: "sqrt(3) - 2", _TAN_FAMILY[3]: "-2 - sqrt(3)"}

# (function, degree angle, sympy angle, correct member of its family)
_CA_ITEMS = [
    ("\\sin", 15, "pi/12", _CA_FAMILY[1]), ("\\sin", 75, "5*pi/12", _CA_FAMILY[0]),
    ("\\sin", 105, "7*pi/12", _CA_FAMILY[0]), ("\\sin", 165, "11*pi/12", _CA_FAMILY[1]),
    ("\\cos", 15, "pi/12", _CA_FAMILY[0]), ("\\cos", 75, "5*pi/12", _CA_FAMILY[1]),
    ("\\cos", 105, "7*pi/12", _CA_FAMILY[2]), ("\\cos", 165, "11*pi/12", _CA_FAMILY[3]),
]
_TAN_ITEMS = [
    ("\\tan", 15, "pi/12", _TAN_FAMILY[1]), ("\\tan", 75, "5*pi/12", _TAN_FAMILY[0]),
    ("\\tan", 105, "7*pi/12", _TAN_FAMILY[3]), ("\\tan", 165, "11*pi/12", _TAN_FAMILY[2]),
]


def _g_hl_compound_angle():
    """Exact values at 15/75/105/165 degrees via compound-angle formulas."""
    raws = []
    for (fn, deg, ang, correct) in _CA_ITEMS:
        fam = [v for v in _CA_FAMILY if v != correct]
        for notation in ("deg", "rad"):
            shown = "%d^\\circ" % deg if notation == "deg" else _rad_ltx(ang)
            raws.append({
                "statement": "Using a compound-angle identity, find the exact value of "
                             "$%s %s$." % (fn, shown),
                "correct": "$%s$" % correct,
                "dvals": ["$%s$" % v for v in fam],
                "explanation": "Split the angle into $45^\\circ \\pm 30^\\circ$ (or "
                               "$60^\\circ \\pm 45^\\circ$) and expand: the value is "
                               "$%s$. All four options are members of the "
                               "$\\frac{\\sqrt{6} \\pm \\sqrt{2}}{4}$ family — the "
                               "identity's SIGN and the quadrant pick the right one."
                               % correct,
                "check": ["Eq(simplify(%s(%s) - (%s)), 0)"
                          % (fn[1:], ang, _CA_SYM[correct])],
            })
    for (fn, deg, ang, correct) in _TAN_ITEMS:
        fam = [v for v in _TAN_FAMILY if v != correct]
        for notation in ("deg", "rad"):
            shown = "%d^\\circ" % deg if notation == "deg" else _rad_ltx(ang)
            raws.append({
                "statement": "Using a compound-angle identity, find the exact value of "
                             "$%s %s$." % (fn, shown),
                "correct": "$%s$" % correct,
                "dvals": ["$%s$" % v for v in fam],
                "explanation": "Expand $\\tan(45^\\circ \\pm 30^\\circ) = "
                               "\\dfrac{\\tan 45^\\circ \\pm \\tan 30^\\circ}"
                               "{1 \\mp \\tan 45^\\circ \\tan 30^\\circ}$ and rationalise: "
                               "the value is $%s$. Check the quadrant for the sign." % correct,
                "check": ["Eq(simplify(tan(%s) - (%s)), 0)" % (ang, _TAN_SYM[correct])],
            })
    return raws


def _rad_ltx(ang):
    table = {"pi/12": "\\frac{\\pi}{12}", "5*pi/12": "\\frac{5\\pi}{12}",
             "7*pi/12": "\\frac{7\\pi}{12}", "11*pi/12": "\\frac{11\\pi}{12}"}
    return table[ang]


# ===========================================================================
# HL · Topic 4 — Statistics & Probability
# ===========================================================================

def _g_hl_bayes():
    """P(A | defective) for two machines."""
    shares = [(Rational(3, 5), Rational(2, 5)), (Rational(7, 10), Rational(3, 10)),
              (Rational(3, 4), Rational(1, 4)), (Rational(2, 3), Rational(1, 3))]
    rates = [(Rational(1, 20), Rational(1, 10)), (Rational(1, 25), Rational(2, 25)),
             (Rational(3, 50), Rational(1, 50)), (Rational(1, 10), Rational(1, 20)),
             (Rational(2, 25), Rational(3, 25)), (Rational(1, 50), Rational(3, 50)),
             (Rational(3, 100), Rational(7, 100)), (Rational(1, 20), Rational(3, 20)),
             (Rational(3, 25), Rational(1, 25))]
    raws = []
    for (pa, pb) in shares:
        for (da, db) in rates:
            ja, jb = pa * da, pb * db
            post = ja / (ja + jb)
            raws.append({
                "statement": "Machine $A$ produces $%s$ of a factory's output and machine "
                             "$B$ the rest. $%s$ of $A$'s items and $%s$ of $B$'s items are "
                             "defective. An item is chosen at random and found to be "
                             "defective. Find the probability it was made by machine $A$."
                             % (fmt(pa), fmt(da), fmt(db)),
                "correct": post,
                # stopped at the joint probability · quoted the prior · computed
                # the complement
                "dvals": [ja, pa, jb / (ja + jb)],
                "explanation": "Bayes: $P(A \\mid D) = \\dfrac{P(A)P(D \\mid A)}"
                               "{P(A)P(D \\mid A) + P(B)P(D \\mid B)} = "
                               "\\dfrac{%s}{%s + %s} = %s$. The joint probability $%s$ still "
                               "needs dividing by the TOTAL probability of a defect."
                               % (fmt(ja), fmt(ja), fmt(jb), fmt(post), fmt(ja)),
                "check": ["Eq(Rational(%d,%d) / (Rational(%d,%d) + Rational(%d,%d)), "
                          "Rational(%d,%d))"
                          % (ja.p, ja.q, ja.p, ja.q, jb.p, jb.q, post.p, post.q)],
            })
    return raws


def _g_hl_var_transform():
    """Var(aX + b) = a^2 Var(X)."""
    raws = []
    for a in (2, 3, 4, 5, -2, -3):
        for b in (1, 2, 3, 5, 7):
            for s2 in (2, 3, 4, 5, 6):
                v = a * a * s2
                raws.append({
                    "statement": "The random variable $X$ has $\\mathrm{Var}(X) = %d$. Find "
                                 "$\\mathrm{Var}(%dX %s %d)$."
                                 % (s2, a, "+" if b >= 0 else "-", abs(b)),
                    "correct": v,
                    # forgot to square a · added b · both errors at once
                    "dvals": [abs(a) * s2, a * a * s2 + b, abs(a) * s2 + b],
                    "explanation": "Variance scales by $a^2$ and ignores shifts: "
                                   "$\\mathrm{Var}(%dX %s %d) = %d^2 \\cdot %d = %d$. Adding "
                                   "the $%d$ is the E$(aX+b)$ rule leaking into the variance."
                                   % (a, "+" if b >= 0 else "-", abs(b), a, s2, v, b),
                    "check": ["Eq((%d)**2 * %d, %d)" % (a, s2, v)],
                })
    return raws


def _g_hl_expected_value():
    """E(X) from a probability table on {1,2,3,4}."""
    tables = [
        (8, (1, 2, 3, 2)), (8, (1, 3, 2, 2)), (8, (2, 1, 3, 2)), (8, (1, 1, 4, 2)),
        (8, (2, 3, 1, 2)), (8, (1, 4, 2, 1)), (8, (3, 1, 2, 2)), (8, (1, 2, 4, 1)),
        (10, (2, 3, 3, 2)), (10, (1, 3, 4, 2)), (10, (3, 2, 4, 1)), (10, (2, 2, 3, 3)),
        (10, (1, 4, 3, 2)), (10, (2, 4, 3, 1)), (10, (1, 2, 4, 3)), (10, (4, 3, 2, 1)),
        (10, (2, 1, 4, 3)), (10, (1, 5, 3, 1)), (10, (3, 1, 4, 2)), (10, (2, 5, 2, 1)),
        (12, (2, 3, 4, 3)), (12, (1, 3, 3, 5)), (12, (2, 5, 4, 1)), (12, (1, 4, 5, 2)),
        (12, (3, 2, 5, 2)), (12, (2, 6, 3, 1)), (12, (1, 2, 5, 4)), (12, (4, 3, 3, 2)),
        (12, (3, 4, 4, 1)), (12, (1, 6, 4, 1)), (12, (2, 2, 5, 3)), (12, (5, 2, 4, 1)),
    ]
    raws = []
    xs = (1, 2, 3, 4)
    for (D, probs) in tables:
        e = Rational(sum(x * p for x, p in zip(xs, probs)), D)
        rev = Rational(sum(x * p for x, p in zip(xs, reversed(probs))), D)
        mode = xs[probs.index(max(probs))]
        raws.append({
            "statement": "A discrete random variable $X$ takes the values $1, 2, 3, 4$ with "
                         "probabilities $%s, %s, %s, %s$ respectively. Find "
                         "$\\mathrm{E}(X)$."
                         % tuple(fmt(Rational(p, D)) for p in probs),
            "correct": e,
            # averaged the values, ignoring the probabilities · matched the
            # probabilities to the wrong values · quoted the mode
            "dvals": [Rational(5, 2), rev, mode],
            "explanation": "$\\mathrm{E}(X) = \\sum x\\,P(X = x) = %s = %s$. The plain "
                           "average $\\frac{5}{2}$ would only be right if all four values "
                           "were equally likely."
                           % (" + ".join("%d \\cdot %s" % (x, fmt(Rational(p, D)))
                                         for x, p in zip(xs, probs)), fmt(e)),
            "check": ["Eq(%s, Rational(%d,%d))"
                      % (" + ".join("%d*Rational(%d,%d)" % (x, p, D)
                                    for x, p in zip(xs, probs)), e.p, e.q)],
        })
    return raws


def _g_hl_prob_combinatorics():
    """P(both red) drawing two without replacement."""
    raws = []
    for r in (3, 4, 5, 6, 7):
        for b in (2, 3, 4, 5, 6):
            n = r + b
            both = Rational(r * (r - 1), n * (n - 1))
            withrep = Rational(r * r, n * n)
            raws.append({
                "statement": "A bag contains $%d$ red and $%d$ blue counters. Two counters "
                             "are drawn at random without replacement. Find the probability "
                             "that both are red." % (r, b),
                "correct": both,
                # treated the draws as with-replacement · did not update the
                # denominator · quoted the single-draw probability
                "dvals": [withrep, Rational(r * (r - 1), n * n), Rational(r, n)],
                "explanation": "$P(\\text{both red}) = \\dfrac{%d}{%d} \\cdot "
                               "\\dfrac{%d}{%d} = %s$ — after one red leaves the bag, both "
                               "counts drop by one. Keeping the denominator at $%d$ is the "
                               "with-replacement error."
                               % (r, n, r - 1, n - 1, fmt(both), n),
                "check": ["Eq(Rational(%d,%d)*Rational(%d,%d), Rational(%d,%d))"
                          % (r, n, r - 1, n - 1, both.p, both.q)],
            })
    return raws


# ===========================================================================
# HL · Topic 5 — Calculus
# ===========================================================================

def _g_hl_product_rule():
    """f(x) = (x^2 + a)(x^3 + b): f'(t)."""
    raws = []
    for a in (1, 2, -1, 3):
        for b in (1, -2, 2, -3):
            for t in (1, 2, -1, -2):
                d = 2 * t * (t ** 3 + b) + 3 * t * t * (t * t + a)
                raws.append({
                    "statement": "Let $f(x) = (x^2 %s %d)(x^3 %s %d)$. Find $f'(%d)$."
                                 % ("+" if a >= 0 else "-", abs(a),
                                    "+" if b >= 0 else "-", abs(b), t),
                    "correct": d,
                    # multiplied the derivatives · kept only the first product-rule
                    # term · evaluated f instead of f'
                    "dvals": [2 * t * 3 * t * t, 2 * t * (t ** 3 + b),
                              (t * t + a) * (t ** 3 + b)],
                    "explanation": "Product rule: $f' = 2x(x^3 %s %d) + 3x^2(x^2 %s %d)$; at "
                                   "$x = %d$ this is $%d + %d = %d$. The derivative of a "
                                   "product is NOT the product of the derivatives "
                                   "($6x^3$ evaluated at $%d$ gives $%d$)."
                                   % ("+" if b >= 0 else "-", abs(b),
                                      "+" if a >= 0 else "-", abs(a), t,
                                      2 * t * (t ** 3 + b), 3 * t * t * (t * t + a), d,
                                      t, 6 * t ** 3),
                    "check": ["Eq(diff((x**2 + (%d))*(x**3 + (%d)), x).subs(x, %d), %d)"
                              % (a, b, t, d)],
                })
    return raws


def _g_hl_quotient_rule():
    """f(x) = (ax + b)/(x^2 + c): f'(t)."""
    raws = []
    for a in (1, 2, 3):
        for b in (1, -2, 4, -1):
            for c in (1, 2, 3):
                for t in (1, -1, 2, -2):
                    num = a * (t * t + c) - (a * t + b) * 2 * t
                    den = (t * t + c) ** 2
                    if num == 0 or 2 * t == 0:
                        continue
                    v = Rational(num, den)
                    raws.append({
                        "statement": "Let $f(x) = \\dfrac{%s}{x^2 %s %d}$. Find $f'(%d)$."
                                     % (lin(a, b), "+" if c >= 0 else "-", abs(c), t),
                        "correct": v,
                        # numerator terms reversed (sign flip) · forgot to square
                        # the denominator · differentiated top and bottom separately
                        "dvals": [-v, Rational(num, t * t + c), Rational(a, 2 * t)],
                        "explanation": "Quotient rule: $f'(x) = \\dfrac{%d(x^2 %s %d) - "
                                       "(%s) \\cdot 2x}{(x^2 %s %d)^2}$; at $x = %d$ the "
                                       "numerator is $%d$ and the denominator $%d$, so "
                                       "$f'(%d) = %s$. Reversing the numerator's two terms "
                                       "flips the sign — the order $u'v - uv'$ is the whole "
                                       "rule."
                                       % (a, "+" if c >= 0 else "-", abs(c), lin(a, b),
                                          "+" if c >= 0 else "-", abs(c), t, num, den, t,
                                          fmt(v)),
                        "check": ["Eq(diff((%d*x + (%d))/(x**2 + (%d)), x).subs(x, %d), "
                                  "Rational(%d,%d))" % (a, b, c, t, v.p, v.q)],
                    })
    return raws


def _g_hl_implicit():
    """x^2 + y^2 + ax = c: dy/dx at (p, q) is -(2p + a)/(2q)."""
    raws = []
    for p in (1, 2, -1, 3, -2):
        for q in (1, 2, -1, 3, -3):
            for a in (2, 4, -2, 6):
                num = 2 * p + a
                if num == 0:
                    continue
                v = Rational(-num, 2 * q)
                c = p * p + q * q + a * p
                if v == Rational(-p, q):
                    continue  # the ignored-a distractor would coincide
                raws.append({
                    "statement": "The point $(%d, %d)$ lies on the curve "
                                 "$x^2 + y^2 %s %dx = %d$. Use implicit differentiation to "
                                 "find $\\dfrac{dy}{dx}$ at this point."
                                 % (p, q, "+" if a > 0 else "-", abs(a), c),
                    "correct": v,
                    # sign flipped · ignored the ax term · forgot to
                    # differentiate y^2 (left dy/dx = -(2p + a))
                    "dvals": [-v, Rational(-p, q), -num],
                    "explanation": "Differentiate term by term: $2x + 2y\\dfrac{dy}{dx} "
                                   "%s %d = 0$, so $\\dfrac{dy}{dx} = -\\dfrac{2x %s %d}{2y}$. "
                                   "At $(%d, %d)$: $-\\dfrac{%d}{%d} = %s$. The $y^2$ term "
                                   "MUST produce a $\\frac{dy}{dx}$ factor — that is the "
                                   "whole point of implicit differentiation."
                                   % ("+" if a > 0 else "-", abs(a),
                                      "+" if a > 0 else "-", abs(a), p, q, num, 2 * q, fmt(v)),
                    "check": ["Eq((%d)**2 + (%d)**2 + (%d)*(%d), %d)" % (p, q, a, p, c),
                              "Eq(Rational(-(%d), 2*(%d)), Rational(%d,%d))"
                              % (num, q, v.p, v.q)],
                })
    return raws


def _g_hl_substitution():
    """Integral of 2x (x^2 + a)^2 from 0 to b: ((b^2+a)^3 - a^3)/3."""
    raws = []
    for a in (1, 2, 3, -1, -2, 4, 5):
        for b in (1, 2, 3, 4, 5):
            u1 = b * b + a
            v = Rational(u1 ** 3 - a ** 3, 3)
            raws.append({
                "statement": "Using the substitution $u = x^2 %s %d$ or otherwise, evaluate "
                             "$\\displaystyle\\int_0^{%d} 2x\\,(x^2 %s %d)^2\\,dx$."
                             % ("+" if a >= 0 else "-", abs(a), b,
                                "+" if a >= 0 else "-", abs(a)),
                "correct": v,
                # forgot the lower limit's contribution · forgot the 1/3 ·
                # integrated u^2 as u^2/2
                "dvals": [Rational(u1 ** 3, 3), u1 ** 3 - a ** 3,
                          Rational(u1 ** 2 - a ** 2, 2)],
                "explanation": "With $u = x^2 %s %d$, $du = 2x\\,dx$, and the limits become "
                               "$%d$ to $%d$: $\\displaystyle\\int_{%d}^{%d} u^2\\,du = "
                               "\\left[\\frac{u^3}{3}\\right]_{%d}^{%d} = %s$. The lower "
                               "limit maps to $u = %d$, not $0$ — dropping it gives $%s$."
                               % ("+" if a >= 0 else "-", abs(a), a, u1, a, u1, a, u1,
                                  fmt(v), a, fmt(Rational(u1 ** 3, 3))),
                "check": ["Eq(integrate(2*x*(x**2 + (%d))**2, (x, 0, %d)), Rational(%d,%d))"
                          % (a, b, v.p, v.q)],
            })
    return raws


# ===========================================================================
# assembly
# ===========================================================================

def build_sl():
    NA, F, G, S, C = ("number-and-algebra", "functions", "geometry-and-trigonometry",
                      "statistics-and-probability", "calculus")
    forms = [
        form("IBSL-NA1", "Arithmetic sequences: the nth term", 1, NA,
             "Apply u_n = u_1 + (n-1)d without the off-by-one.", mk_num("IBSL-NA1", _g_sl_arith_nth())),
        form("IBSL-NA2", "Geometric sequences: the nth term", 1, NA,
             "Apply u_n = u_1 r^(n-1), including fractional ratios.", mk_num("IBSL-NA2", _g_sl_geom_nth())),
        form("IBSL-NA3", "Arithmetic series", 2, NA,
             "Sum n terms with S_n = n/2 (u_1 + u_n).", mk_num("IBSL-NA3", _g_sl_arith_sum())),
        form("IBSL-NA4", "Laws of logarithms", 2, NA,
             "Add logs of the same base by multiplying arguments.", mk_num("IBSL-NA4", _g_sl_log_laws())),
        form("IBSL-NA5", "Infinite geometric series", 3, NA,
             "Test |r| < 1 and apply S = u_1/(1 - r).", mk_num("IBSL-NA5", _g_sl_infinite_geom())),
        form("IBSL-NA6", "Binomial theorem: a coefficient", 3, NA,
             "Pick the right term of (x + a)^n and its sign.", mk_num("IBSL-NA6", _g_sl_binomial_coeff())),
        form("IBSL-F1", "Composite functions", 1, F,
             "Evaluate (f o g)(a) inner-function-first.", mk_num("IBSL-F1", _g_sl_composite())),
        form("IBSL-F2", "Inverse functions", 2, F,
             "Undo a linear function to evaluate f^{-1}(k).", mk_num("IBSL-F2", _g_sl_inverse())),
        form("IBSL-F3", "Vertex of a quadratic", 2, F,
             "Locate the vertex from x = -b/2a.", mk_txt("IBSL-F3", _g_sl_vertex())),
        form("IBSL-F4", "Asymptotes of a rational function", 3, F,
             "Read both asymptotes of (ax+b)/(cx+d).", mk_txt("IBSL-F4", _g_sl_asymptotes())),
        form("IBSL-F5", "Transformations of graphs", 3, F,
             "Track a point through y = a f(x - h) + k in the right order.",
             mk_txt("IBSL-F5", _g_sl_transform_point())),
        form("IBSL-G1", "Arc length in radians", 1, G,
             "Use s = r·theta (and know when it is the sector area instead).",
             mk_txt("IBSL-G1", _g_sl_arc_length())),
        form("IBSL-G2", "The cosine rule", 2, G,
             "Find a^2 with the sign of cos A under control.", mk_num("IBSL-G2", _g_sl_cosine_rule())),
        form("IBSL-G3", "Area of a triangle", 2, G,
             "Apply Area = (1/2) ab sin C.", mk_num("IBSL-G3", _g_sl_triangle_area())),
        form("IBSL-G4", "Exact values on the unit circle", 2, G,
             "Reference angle + quadrant sign for sin and cos.", mk_txt("IBSL-G4", _g_sl_exact_values())),
        form("IBSL-G5", "Counting trig solutions", 3, G,
             "Count solutions of sin/cos/tan equations on [0, 2pi).",
             mk_num("IBSL-G5", _g_sl_trig_count())),
        form("IBSL-S1", "Mean from a frequency table", 1, S,
             "Weight each value by its frequency.", mk_num("IBSL-S1", _g_sl_mean_freq())),
        form("IBSL-S2", "Probability of a union", 2, S,
             "Apply P(A u B) = P(A) + P(B) - P(A n B).", mk_num("IBSL-S2", _g_sl_union())),
        form("IBSL-S3", "Independent events", 1, S,
             "Multiply probabilities for independent events.", mk_num("IBSL-S3", _g_sl_independent())),
        form("IBSL-S4", "Conditional probability", 2, S,
             "Restrict the sample space before dividing.", mk_num("IBSL-S4", _g_sl_conditional())),
        form("IBSL-S5", "The binomial distribution", 3, S,
             "Assemble P(X = k) with the binomial coefficient.", mk_num("IBSL-S5", _g_sl_binomial_dist())),
        form("IBSL-C1", "Derivative at a point", 1, C,
             "Differentiate a polynomial and evaluate.", mk_num("IBSL-C1", _g_sl_derivative_value())),
        form("IBSL-C2", "Equation of a tangent", 2, C,
             "Gradient from f', line through the point of tangency.", mk_txt("IBSL-C2", _g_sl_tangent())),
        form("IBSL-C3", "Kinematics: at rest", 2, C,
             "Solve v = ds/dt = 0, not s = 0.", mk_num("IBSL-C3", _g_sl_at_rest())),
        form("IBSL-C4", "Definite integrals", 2, C,
             "Antidifferentiate and evaluate between limits.", mk_num("IBSL-C4", _g_sl_definite_integral())),
        form("IBSL-C5", "Area under a curve", 3, C,
             "Integrate between the x-intercepts.", mk_num("IBSL-C5", _g_sl_area_under())),
    ]
    return {
        "slug": "ib-sl",
        "title": "IB Mathematics AA SL",
        "titleMn": "IB Mathematics AA SL",
        "blurb": "Topic-focused practice across the five SL syllabus topics — Number & "
                 "Algebra, Functions, Geometry & Trigonometry, Statistics & Probability "
                 "and Calculus — at Paper 1/2 short-question difficulty.",
        "units": UNITS,
        "forms": forms,
    }


def build_hl():
    NA, F, G, S, C = ("number-and-algebra", "functions", "geometry-and-trigonometry",
                      "statistics-and-probability", "calculus")
    forms = [
        form("IBHL-NA1", "Complex numbers: products", 2, NA,
             "Expand (a+bi)(c+di) with i^2 = -1.", mk_num("IBHL-NA1", _g_hl_complex_product())),
        form("IBHL-NA2", "Modulus of a complex number", 1, NA,
             "Compute |z| = sqrt(a^2 + b^2).", mk_num("IBHL-NA2", _g_hl_modulus())),
        form("IBHL-NA3", "Argument of a complex number", 3, NA,
             "Principal argument from quadrant + reference angle.", mk_txt("IBHL-NA3", _g_hl_argument())),
        form("IBHL-NA4", "Counting: combinations", 3, NA,
             "Choose committees, with and without restrictions.", mk_num("IBHL-NA4", _g_hl_combinations())),
        form("IBHL-F1", "The remainder theorem", 2, F,
             "Remainder on division by (x - a) is p(a).", mk_num("IBHL-F1", _g_hl_remainder())),
        form("IBHL-F2", "Vieta for cubics", 2, F,
             "Sum of roots is -b/a — leading coefficient included.", mk_num("IBHL-F2", _g_hl_vieta_cubic())),
        form("IBHL-F3", "The factor theorem", 3, F,
             "Force p(a) = 0 to find an unknown coefficient.", mk_num("IBHL-F3", _g_hl_factor_k())),
        form("IBHL-F4", "Symmetric functions of roots", 3, F,
             "Compute alpha^2 + beta^2 from sum and product.", mk_num("IBHL-F4", _g_hl_sum_sq_roots())),
        form("IBHL-G1", "Magnitude of a 3D vector", 1, G,
             "Square, sum, square-root — signs vanish.", mk_num("IBHL-G1", _g_hl_vec_magnitude())),
        form("IBHL-G2", "Perpendicular vectors", 2, G,
             "Set the scalar product to zero and solve for k.", mk_num("IBHL-G2", _g_hl_dot_perp())),
        form("IBHL-G3", "Angle between vectors", 3, G,
             "cos(theta) = u.v / (|u||v|).", mk_num("IBHL-G3", _g_hl_vec_angle())),
        form("IBHL-G4", "Compound-angle exact values", 3, G,
             "sin/cos/tan of 15°, 75°, 105°, 165° by expanding identities.",
             mk_txt("IBHL-G4", _g_hl_compound_angle())),
        form("IBHL-S1", "Bayes' theorem", 3, S,
             "Reverse a conditional probability over two sources.", mk_num("IBHL-S1", _g_hl_bayes())),
        form("IBHL-S2", "Expectation algebra", 2, S,
             "Var(aX + b) = a^2 Var(X): square the scale, drop the shift.",
             mk_num("IBHL-S2", _g_hl_var_transform())),
        form("IBHL-S3", "Expected value of a discrete variable", 2, S,
             "E(X) = sum of x P(X = x) from a table.", mk_num("IBHL-S3", _g_hl_expected_value())),
        form("IBHL-S4", "Probability without replacement", 2, S,
             "Update both counts after each draw.", mk_num("IBHL-S4", _g_hl_prob_combinatorics())),
        form("IBHL-C1", "The product rule", 2, C,
             "Differentiate a product and evaluate.", mk_num("IBHL-C1", _g_hl_product_rule())),
        form("IBHL-C2", "The quotient rule", 2, C,
             "u'v - uv' over v^2 — order and square both matter.", mk_num("IBHL-C2", _g_hl_quotient_rule())),
        form("IBHL-C3", "Implicit differentiation", 3, C,
             "Differentiate y-terms with a dy/dx factor.", mk_num("IBHL-C3", _g_hl_implicit())),
        form("IBHL-C4", "Integration by substitution", 3, C,
             "Change variable AND limits, then integrate in u.", mk_num("IBHL-C4", _g_hl_substitution())),
    ]
    return {
        "slug": "ib-hl",
        "title": "IB Mathematics AA HL",
        "titleMn": "IB Mathematics AA HL",
        "blurb": "The AHL extension drilled by topic — complex numbers, polynomial "
                 "theorems, vectors, Bayes and harder calculus — on top of the SL bank, "
                 "which HL students should master too.",
        "units": HL_UNITS,
        "forms": forms,
    }
