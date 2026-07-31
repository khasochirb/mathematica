# -*- coding: utf-8 -*-
"""Grade 9 problem bank — the exit level of the Mid school band.

Resource blueprint: every band carries exams at the bottom (exit), built by
the IM exam selector over a verified MCQ bank. Grade lesson problems carry no
options, so this module IS that bank: three forms per Grade-9 topic, every
answer computed from named parameters, every distractor a named error model,
every check sympy-asserted by the gate. Registered as a course-ladder bank
(the Grade 9 course lives at /math/9), it also gives Grade 9 the same
topic-practice surface as every other course.

Unit ids equal the Grade-9 topic slugs so bank units link into /math/9/<slug>.
Grade 9 is the high-school-entrance transition year — level 3 items sit at
entrance-exam difficulty.
"""
import os
import sys

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from sympy import Rational

from imbank import fmt, lin, mk_num, mk_txt, form, pt

EQ, IN, FN, LM, SI, PW, DD = (
    "equations-and-formulas", "inequalities-and-absolute-value",
    "introduction-to-functions", "linear-models-and-variation",
    "inequalities-in-two-variables", "piecewise-and-absolute-value-graphs",
    "data-distributions",
)

UNITS = [
    {"id": EQ, "title": "Equations & Formulas",
     "blurb": "Variables on both sides, literal equations, and rate problems."},
    {"id": IN, "title": "Inequalities & Absolute Value",
     "blurb": "Multi-step inequalities and absolute-value equations and inequalities."},
    {"id": FN, "title": "Introduction to Functions",
     "blurb": "Function notation, evaluating, inverting, and domains."},
    {"id": LM, "title": "Linear Models & Variation",
     "blurb": "Direct and inverse variation, and linear models from data."},
    {"id": SI, "title": "Systems of Inequalities",
     "blurb": "Testing points against constraints and optimizing over a region."},
    {"id": PW, "title": "Piecewise & Absolute-Value Graphs",
     "blurb": "The V graph, piecewise evaluation, and step-function models."},
    {"id": DD, "title": "Data Distributions",
     "blurb": "Medians, quartiles, the IQR and outlier fences."},
]


# ===========================================================================
# Equations & Formulas
# ===========================================================================

def _g_both_sides():
    """ax + b = cx + d engineered so x = x0."""
    raws = []
    for a in (3, 4, 5, 6, 7):
        for c in (1, 2, -2, -3):
            if a == c:
                continue
            for x0 in (-5, -3, -2, 2, 3, 4, 6):
                b = ((x0 + 7) % 9) - 4
                d = (a - c) * x0 + b
                raws.append({
                    "statement": "Solve $%s = %s$." % (lin(a, b), lin(c, d)),
                    "correct": x0,
                    # sign slip when collecting x-terms · off by the constant
                    # move · negated answer
                    "dvals": [Rational(d - b, a + c) if a + c != 0 else -x0,
                              Rational(d + b, a - c), -x0],
                    "explanation": "Move the $x$-terms to one side: $%dx = %d$, so "
                                   "$x = %d$. Adding $%dx$ instead of subtracting it is "
                                   "the usual slip."
                                   % (a - c, d - b, x0, c),
                    "check": ["Eq(%d*(%d) + (%d), %d*(%d) + (%d))" % (a, x0, b, c, x0, d)],
                })
    return raws


def _g_literal():
    """Solve a formula for one of its letters."""
    # (statement template, correct, distractors...) built per family
    raws = []
    for m in (2, 3, 4, 5):
        for c in (1, 2, 3, 5, 7):
            raws.append({
                "statement": "Solve $y = %dx %s %d$ for $x$." % (m, "+", c),
                "correct": "$x = \\dfrac{y - %d}{%d}$" % (c, m),
                # forgot to move the constant · sign slip · multiplied instead
                "dvals": ["$x = \\dfrac{y}{%d} - %d$" % (m, c),
                          "$x = \\dfrac{y + %d}{%d}$" % (c, m),
                          "$x = %d(y - %d)$" % (m, c)],
                "explanation": "Undo in reverse order: subtract $%d$ first, then divide "
                               "the WHOLE side by $%d$: $x = \\dfrac{y - %d}{%d}$. "
                               "Dividing before subtracting leaves the $%d$ undivided."
                               % (c, m, c, m, c),
                "check": ["Eq((%d*x + %d - %d)/%d, x)" % (m, c, c, m)],
            })
    for b_coef in (2, 3, 4, 6):
        for a_coef in (2, 4, 5, 3):
            if a_coef == b_coef:
                continue
            raws.append({
                "statement": "Solve $P = %da + %db$ for $b$." % (a_coef, b_coef),
                "correct": "$b = \\dfrac{P - %da}{%d}$" % (a_coef, b_coef),
                "dvals": ["$b = \\dfrac{P}{%d} - %da$" % (b_coef, a_coef),
                          "$b = \\dfrac{P + %da}{%d}$" % (a_coef, b_coef),
                          "$b = %d(P - %da)$" % (b_coef, a_coef)],
                "explanation": "Isolate the $b$-term: $P - %da = %db$, then divide by "
                               "$%d$: $b = \\dfrac{P - %da}{%d}$."
                               % (a_coef, b_coef, b_coef, a_coef, b_coef),
                "check": ["Eq((%d*a + %d*b - %d*a)/%d, b)" % (a_coef, b_coef, a_coef, b_coef)],
            })
    return raws


def _g_meeting():
    """Two movers close a gap: t = D / (r1 + r2)."""
    raws = []
    pairs = [(40, 60), (30, 50), (45, 55), (35, 65), (20, 40), (50, 70), (25, 35)]
    for (r1, r2) in pairs:
        s = r1 + r2
        for t in (2, 3, 4, 5):
            D = s * t
            raws.append({
                "statement": "Two cars start $%d$ km apart and drive toward each other, "
                             "one at $%d$ km/h and the other at $%d$ km/h. After how many "
                             "hours do they meet?" % (D, r1, r2),
                "correct": t,
                # subtracted the rates · used one car's rate · used the other's
                "dvals": [Rational(D, r2 - r1) if r2 != r1 else t + 1,
                          Rational(D, r2), Rational(D, r1)],
                "explanation": "Together they close the gap at $%d + %d = %d$ km/h, so "
                               "$t = \\dfrac{%d}{%d} = %d$ hours. Rates ADD when the "
                               "motion is toward each other — subtracting is the "
                               "chasing-problem formula."
                               % (r1, r2, s, D, s, t),
                "check": ["Eq(Rational(%d, %d + %d), %d)" % (D, r1, r2, t)],
            })
    return raws


# ===========================================================================
# Inequalities & Absolute Value
# ===========================================================================

def _g_multistep_ineq():
    """Solve ax + b < c (including negative a, where the sign flips)."""
    raws = []
    for a in (2, 3, 4, -2, -3, -5):
        for x0 in (2, 3, -2, 4, -4, 1):
            for b in (1, -3, 5):
                c = a * x0 + b
                op, flipped = ("<", ">") if a > 0 else (">", "<")
                # statement always uses "<"; solution direction depends on a
                sol_op = "<" if a > 0 else ">"
                raws.append({
                    "statement": "Solve the inequality $%s < %d$." % (lin(a, b), c),
                    "correct": "$x %s %d$" % (sol_op, x0),
                    # forgot to flip (or flipped when they shouldn't) · sign slip
                    # on the constant · answered with the boundary only
                    "dvals": ["$x %s %d$" % (">" if sol_op == "<" else "<", x0),
                              "$x %s %d$" % (sol_op, -x0) if x0 != 0 else "$x %s %d$" % (sol_op, 1),
                              "$x = %d$" % x0],
                    "explanation": "Isolate: $%dx < %d$, so dividing by $%d$ %s: "
                                   "$x %s %d$. %s"
                                   % (a, c - b, a,
                                      "keeps the direction" if a > 0 else "FLIPS the inequality",
                                      sol_op, x0,
                                      "" if a > 0 else "Dividing by a negative number reverses the sign — the classic trap."),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, x0, b, c)],
                })
    return raws


def _g_abs_equation():
    """|x - a| = b: two solutions a ± b."""
    raws = []
    for a in (2, 3, 5, -2, -4, 6, -1):
        for b in (1, 2, 3, 4, 7):
            if a == b or a == 0:
                continue
            hi, lo = a + b, a - b
            raws.append({
                "statement": "Solve $|x %s %d| = %d$." % ("-" if a > 0 else "+", abs(a), b),
                "correct": "$x = %d$ or $x = %d$" % (hi, lo),
                # kept only one branch · sign slip on the center · solved
                # x - a = b and x + a = b
                "dvals": ["$x = %d$" % hi,
                          "$x = %d$ or $x = %d$" % (-a + b, -a - b),
                          "$x = %d$ or $x = %d$" % (b - a, b + a) if (b - a, b + a) not in ((hi, lo), (lo, hi)) else "$x = %d$" % lo],
                "explanation": "The expression inside is $%d$ away from zero, two ways: "
                               "$x %s %d = %d$ gives $x = %d$, and $x %s %d = -%d$ gives "
                               "$x = %d$. An absolute-value equation with a positive "
                               "right side always has BOTH branches."
                               % (b, "-" if a > 0 else "+", abs(a), b, hi,
                                  "-" if a > 0 else "+", abs(a), b, lo),
                "check": ["Eq(Abs(%d - (%d)), %d)" % (hi, a, b),
                          "Eq(Abs(%d - (%d)), %d)" % (lo, a, b)],
            })
    return raws


def _g_abs_inequality():
    """|x - a| <= b: the interval [a-b, a+b]."""
    raws = []
    for a in (1, 2, 4, -3, 5, -1, 3):
        for b in (1, 2, 3, 5):
            if a == 0 or a == -a:
                pass
            lo, hi = a - b, a + b
            if (-a - b, -a + b) == (lo, hi):
                continue
            raws.append({
                "statement": "Solve $|x %s %d| \\le %d$." % ("-" if a > 0 else "+", abs(a), b),
                "correct": "$%d \\le x \\le %d$" % (lo, hi),
                # picked the outside (the OR case) · sign slip on the center ·
                # boundary only
                "dvals": ["$x \\le %d$ or $x \\ge %d$" % (lo, hi),
                          "$%d \\le x \\le %d$" % (-a - b, -a + b),
                          "$x \\le %d$" % hi],
                "explanation": "\"Within $%d$ of $%d$\" is a single interval: "
                               "$%d \\le x \\le %d$. The two-piece answer belongs to "
                               "$|x %s %d| \\ge %d$ — $\\le$ traps you INSIDE, $\\ge$ "
                               "throws you OUTSIDE."
                               % (b, a, lo, hi, "-" if a > 0 else "+", abs(a), b),
                "check": ["Eq(Abs(%d - (%d)), %d)" % (lo, a, b),
                          "Eq(Abs(%d - (%d)), %d)" % (hi, a, b),
                          "Abs(%d - (%d)) < %d" % (a, a, b)],
            })
    return raws


# ===========================================================================
# Introduction to Functions
# ===========================================================================

def _g_evaluate_fn():
    """g(t) for g(x) = a x^2 + c."""
    raws = []
    for a in (2, 3, -2, 4, 5):
        for c in (1, -3, 5, -1, 7):
            for t in (2, -2, 3, -3):
                v = a * t * t + c
                raws.append({
                    "statement": "Let $g(x) = %dx^2 %s %d$. Find $g(%d)$."
                                 % (a, "+" if c >= 0 else "-", abs(c), t),
                    "correct": v,
                    # squared (at) instead of t · sign slip on c · forgot the square
                    "dvals": [a * a * t * t + c, a * t * t - c, a * t + c],
                    "explanation": "Substitute and square FIRST: $g(%d) = %d \\cdot %d "
                                   "%s %d = %d$. Squaring $%d \\cdot %d$ instead of just "
                                   "$%d$ gives $%d$."
                                   % (t, a, t * t, "+" if c >= 0 else "-", abs(c), v,
                                      a, t, t, a * a * t * t + c),
                    "check": ["Eq(%d*(%d)**2 + (%d), %d)" % (a, t, c, v)],
                })
    return raws


def _g_domain():
    """Domain of k/(x-a) and sqrt(x-a)."""
    raws = []
    for a in (2, 3, 5, -2, -4, 1, 7, -1):
        for k in (1, 2, 3):
            raws.append({
                "statement": "What is the domain of $f(x) = \\dfrac{%d}{x %s %d}$?"
                             % (k, "-" if a > 0 else "+", abs(a)),
                "correct": "all real numbers except $x = %d$" % a,
                # sign slip · confused with the square-root rule · no restriction
                "dvals": ["all real numbers except $x = %d$" % -a,
                          "$x \\ge %d$" % a,
                          "all real numbers"],
                "explanation": "Division by zero is the only danger: the denominator is "
                               "zero at $x = %d$, and every other input is fine. "
                               "$x \\ge %d$ is the SQUARE-ROOT rule, not the fraction "
                               "rule." % (a, a),
                "check": ["Eq((%d) %s %d, 0)" % (a, "-" if a > 0 else "+", abs(a))],
            })
            raws.append({
                "statement": "What is the domain of $f(x) = %s\\sqrt{x %s %d}$?"
                             % ("" if k == 1 else str(k), "-" if a > 0 else "+", abs(a)),
                "correct": "$x \\ge %d$" % a,
                # strict inequality · sign slip · the fraction rule
                "dvals": ["$x > %d$" % a,
                          "$x \\ge %d$" % -a,
                          "all real numbers except $x = %d$" % a],
                "explanation": "The expression under the root must be $\\ge 0$: "
                               "$x %s %d \\ge 0$ gives $x \\ge %d$ — and $x = %d$ itself "
                               "IS allowed ($\\sqrt{0} = 0$), so the inequality is not "
                               "strict." % ("-" if a > 0 else "+", abs(a), a, a),
                "check": ["Eq(sqrt((%d) %s %d), 0)" % (a, "-" if a > 0 else "+", abs(a))],
            })
    return raws


def _g_solve_fx():
    """f(x) = v for f(x) = ax + b: invert, don't evaluate."""
    raws = []
    for a in (2, 3, 4, -2, 5):
        for b in (1, -3, 5, -1):
            for x0 in (2, 3, -2, 4):
                v = a * x0 + b
                raws.append({
                    "statement": "Let $f(x) = %s$. Find the value of $x$ for which "
                                 "$f(x) = %d$." % (lin(a, b), v),
                    "correct": x0,
                    # evaluated f(v) instead of solving · sign slip on b ·
                    # forgot to divide
                    "dvals": [a * v + b, Rational(v + b, a), v - b],
                    "explanation": "Set $%s = %d$ and solve: $%dx = %d$, so $x = %d$. "
                                   "Computing $f(%d) = %d$ answers the OPPOSITE "
                                   "question — output for input, not input for output."
                                   % (lin(a, b), v, a, v - b, x0, v, a * v + b),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, x0, b, v)],
                })
    return raws


# ===========================================================================
# Linear Models & Variation
# ===========================================================================

def _g_direct_variation():
    """y = kx: from (x0, y0), find y at x1."""
    raws = []
    for k in (2, 3, 5, Rational(3, 2), Rational(5, 2), 4):
        for x0 in (2, 4, 6, 8):
            y0 = k * x0
            if y0 != int(y0):
                continue
            for x1 in (3, 5, 10, 12):
                if x1 == x0:
                    continue
                y1 = k * x1
                if y1 != int(y1):
                    continue
                raws.append({
                    "statement": "$y$ varies directly with $x$, and $y = %d$ when "
                                 "$x = %d$. Find $y$ when $x = %d$." % (y0, x0, x1),
                    "correct": y1,
                    # inverse-variation answer · added the change in x · quoted k
                    "dvals": [Rational(y0 * x0, x1), y0 + (x1 - x0), k],
                    "explanation": "Direct variation keeps the RATIO constant: "
                                   "$k = \\dfrac{%d}{%d} = %s$, so $y = %s \\cdot %d = "
                                   "%d$. Keeping the PRODUCT constant instead is inverse "
                                   "variation — that gives $%s$."
                                   % (y0, x0, fmt(k), fmt(k), x1, y1,
                                      fmt(Rational(y0 * x0, x1))),
                    "check": ["Eq(Rational(%d, %d) * %d, %d)" % (y0, x0, x1, y1)],
                })
    return raws


def _g_inverse_variation():
    """y = k/x: from (x0, y0), find y at x1."""
    raws = []
    for k in (24, 36, 48, 60, 120):
        for x0 in (2, 3, 4, 6):
            y0 = k // x0
            if k % x0:
                continue
            for x1 in (8, 12, 5, 10):
                if x1 == x0 or k % x1:
                    continue
                y1 = k // x1
                raws.append({
                    "statement": "$y$ varies inversely with $x$, and $y = %d$ when "
                                 "$x = %d$. Find $y$ when $x = %d$." % (y0, x0, x1),
                    "correct": y1,
                    # direct-variation answer · quoted k · subtracted the change
                    "dvals": [Rational(y0 * x1, x0), k, y0 - (x1 - x0)],
                    "explanation": "Inverse variation keeps the PRODUCT constant: "
                                   "$k = %d \\cdot %d = %d$, so $y = \\dfrac{%d}{%d} = %d$. "
                                   "Scaling $y$ up with $x$ is DIRECT variation."
                                   % (y0, x0, k, k, x1, y1),
                    "check": ["Eq(Rational(%d, %d), %d)" % (k, x1, y1),
                              "Eq(%d*%d, %d*%d)" % (y0, x0, y1, x1)],
                })
    return raws


def _g_model_two_points():
    """A linear cost model through two data points."""
    raws = []
    for m in (3, 5, 8, 12, 15):
        for b in (20, 30, 50, 40):
            for (x1, x2) in ((2, 5), (3, 7), (4, 9), (2, 6)):
                c1, c2 = m * x1 + b, m * x2 + b
                raws.append({
                    "statement": "A tutor charges $%d$ dollars for a $%d$-hour booking "
                                 "and $%d$ dollars for a $%d$-hour booking. The charge "
                                 "$C$ is a linear function of the hours $x$. Which model "
                                 "is correct?" % (c1, x1, c2, x2),
                    "correct": "$C = %s$" % lin(m, b),
                    # ratio through the origin · intercept read as the first
                    # price · slope from one point (c1/x1)
                    "dvals": ["$C = %s$" % lin(Rational(c2, x2), 0) if c2 % x2 == 0 else "$C = \\dfrac{%d}{%d}x$" % (c2, x2),
                              "$C = %s$" % lin(m, c1),
                              "$C = %s$" % lin(Rational(c1, x1), 0) if c1 % x1 == 0 else "$C = \\dfrac{%d}{%d}x$" % (c1, x1)],
                    "explanation": "The rate is $\\dfrac{%d - %d}{%d - %d} = %d$ dollars "
                                   "per hour, and the base fee follows: $%d - %d \\cdot %d "
                                   "= %d$. So $C = %s$. A line through the origin would "
                                   "mean no base fee — but the two prices aren't "
                                   "proportional to the hours."
                                   % (c2, c1, x2, x1, m, c1, m, x1, b, lin(m, b)),
                    "check": ["Eq(Rational(%d - %d, %d - %d), %d)" % (c2, c1, x2, x1, m),
                              "Eq(%d*%d + %d, %d)" % (m, x1, b, c1),
                              "Eq(%d*%d + %d, %d)" % (m, x2, b, c2)],
                })
    return raws


# ===========================================================================
# Systems of Inequalities
# ===========================================================================

def _g_point_solution():
    """Which point satisfies ax + by <= c?"""
    raws = []
    for (a, b) in ((1, 1), (2, 1), (1, 2), (3, 2), (2, 3), (1, 3), (3, 1), (4, 1)):
        for c in (5, 6, 8, 10, 12, 14):
            # solution point well inside; distractors clearly outside
            sol = (1, 1)
            outs = [(c, c), (c, 1), (1, c)]
            if a * sol[0] + b * sol[1] >= c:
                continue
            outs = [(px, py) for (px, py) in outs if a * px + b * py > c]
            if len(outs) < 3:
                continue
            raws.append({
                "statement": "Which point is a solution of the inequality "
                             "$%sx + %sy \\le %d$?"
                             % ("" if a == 1 else a, "" if b == 1 else b, c),
                "correct": "$%s$" % pt(*sol),
                "dvals": ["$%s$" % pt(*p) for p in outs[:3]],
                "explanation": "Substitute each point: $%d \\cdot %d + %d \\cdot %d = %d "
                               "\\le %d$ ✓ — the others push the left side past $%d$. "
                               "Testing the point IS the whole method; no graph needed."
                               % (a, sol[0], b, sol[1], a * sol[0] + b * sol[1], c, c),
                "check": ["%d*%d + %d*%d <= %d" % (a, sol[0], b, sol[1], c)] +
                         ["%d*%d + %d*%d > %d" % (a, px, b, py, c) for (px, py) in outs[:3]],
            })
    return raws


def _g_system_point():
    """Which point satisfies BOTH x + y <= c and x - y >= d?"""
    raws = []
    for c in (6, 8, 10, 7, 9):
        for d in (0, 1, 2, -1, 3):
            # correct: on the safe side of both. pick (x, y) = (d + 2, 1)
            sx, sy = d + 2, 1
            if sx + sy > c or sx - sy < d:
                continue
            # each distractor violates exactly one constraint
            bad1 = (c + 1, 0)            # violates x + y <= c
            bad2 = (d - 2, 0)            # violates x - y >= d
            bad3 = (c, c)                # violates both
            if not (bad1[0] + bad1[1] > c and bad2[0] - bad2[1] < d and (bad3[0] + bad3[1] > c)):
                continue
            raws.append({
                "statement": "Which point satisfies BOTH $x + y \\le %d$ and "
                             "$x - y \\ge %d$?" % (c, d),
                "correct": "$%s$" % pt(sx, sy),
                "dvals": ["$%s$" % pt(*bad1), "$%s$" % pt(*bad2), "$%s$" % pt(*bad3)],
                "explanation": "A system needs BOTH checks to pass: $%d + %d = %d \\le %d$ "
                               "✓ and $%d - %d = %d \\ge %d$ ✓. Each wrong option passes "
                               "one test and fails the other — always test every "
                               "constraint."
                               % (sx, sy, sx + sy, c, sx, sy, sx - sy, d),
                "check": ["%d + %d <= %d" % (sx, sy, c),
                          "%d - %d >= %d" % (sx, sy, d),
                          "%d + %d > %d" % (bad1[0], bad1[1], c),
                          "%d - %d < %d" % (bad2[0], bad2[1], d)],
            })
    return raws


def _g_optimize_region():
    """Maximize P = ax + by over listed vertices."""
    raws = []
    for (a, b) in ((3, 2), (2, 5), (4, 3), (5, 2), (2, 3), (3, 4), (5, 3), (4, 5)):
        for (x1, y1, x2, y2) in ((6, 0, 4, 3), (5, 0, 3, 4), (8, 0, 5, 4), (7, 0, 4, 5), (9, 0, 6, 3)):
            verts = [(0, 0), (x1, 0), (0, y1 + 2), (x2, y2)]
            vals = [a * x + b * y for (x, y) in verts]
            best = max(vals)
            if vals.count(best) != 1:
                continue
            others = sorted(set(v for v in vals if v != best), reverse=True)
            if len(others) < 3:
                continue
            raws.append({
                "statement": "A feasible region has vertices $%s$, $%s$, $%s$ and $%s$. "
                             "What is the maximum value of $P = %dx + %dy$ on this "
                             "region?" % (*[pt(x, y) for (x, y) in verts], a, b),
                "correct": best,
                # the other vertices' values — stopping at the wrong corner
                "dvals": others[:3],
                "explanation": "A linear objective is maximized at a VERTEX, so evaluate "
                               "$P$ at all four: $%s$. The largest is $%d$. Checking "
                               "only some corners is how the maximum gets missed."
                               % (", ".join(str(v) for v in vals), best),
                "check": ["Eq(Max(%s), %d)" % (", ".join(str(v) for v in vals), best)],
            })
    return raws


# ===========================================================================
# Piecewise & Absolute-Value Graphs
# ===========================================================================

def _g_v_vertex():
    """Vertex of y = |x - h| + k."""
    raws = []
    for h in (1, 2, 3, -1, -2, -4, 5):
        for k in (2, -3, 4, -1, 5, -5):
            if h == k or h == -k:
                continue
            raws.append({
                "statement": "What is the vertex of the graph of "
                             "$y = |x %s %d| %s %d$?"
                             % ("-" if h > 0 else "+", abs(h), "+" if k > 0 else "-", abs(k)),
                "correct": "$%s$" % pt(h, k),
                # sign of h flipped (the |x - h| trap) · sign of k flipped ·
                # coordinates swapped
                "dvals": ["$%s$" % pt(-h, k), "$%s$" % pt(h, -k), "$%s$" % pt(k, h)],
                "explanation": "The V sits where the inside is zero: $x = %d$, at height "
                               "$y = %d$ — vertex $%s$. Inside the absolute value the "
                               "sign works BACKWARD: $|x - %d|$ moves the vertex to "
                               "$+%d$, not $-%d$."
                               % (h, k, pt(h, k), abs(h), abs(h), abs(h)) if h > 0 else
                               "The V sits where the inside is zero: $x = %d$, at height "
                               "$y = %d$ — vertex $%s$. Inside the absolute value the "
                               "sign works backward — $|x + %d|$ puts the vertex at "
                               "$-%d$." % (h, k, pt(h, k), abs(h), abs(h)),
                "check": ["Eq(Abs(%d - (%d)), 0)" % (h, h),
                          "Eq(Abs(0) + (%d), %d)" % (k, k)],
            })
    return raws


def _g_piecewise_eval():
    """Evaluate a two-branch piecewise function, including at the boundary."""
    raws = []
    for a in (2, 3, 4):          # boundary
        for (m1, b1) in ((2, 1), (3, -2), (1, 4)):
            for (m2, b2) in ((-1, 8), (2, 5), (-2, 12)):
                for t in (a - 2, a, a + 2):
                    branch2 = t >= a
                    v = (m2 * t + b2) if branch2 else (m1 * t + b1)
                    wrong = (m1 * t + b1) if branch2 else (m2 * t + b2)
                    if v == wrong:
                        continue
                    raws.append({
                        "statement": "Let $f(x) = \\begin{cases} %s & x < %d \\\\ %s & "
                                     "x \\ge %d \\end{cases}$. Find $f(%d)$."
                                     % (lin(m1, b1), a, lin(m2, b2), a, t),
                        "correct": v,
                        # used the wrong branch · averaged the branches · used
                        # the boundary value a as the answer
                        "dvals": [wrong, Rational(v + wrong, 2), a if a not in (v, wrong) else a + 10],
                        "explanation": "$x = %d$ %s $%d$, so the %s branch applies: "
                                       "$f(%d) = %d$. At the boundary itself the "
                                       "\"$\\ge$\" branch owns the point — that's what "
                                       "the equals sign decides."
                                       % (t, "is at least" if branch2 else "is less than",
                                          a, "second" if branch2 else "first", t, v),
                        "check": ["Eq(%d*(%d) + (%d), %d)"
                                  % ((m2, t, b2, v) if branch2 else (m1, t, b1, v))],
                    })
    return raws


def _g_step_pricing():
    """A step-function tariff: 'or part of one' rounds up.

    Weights are half-integers on purpose: at a whole-number weight the
    round-down and treat-as-proportional error models coincide with the
    correct charge, and the variant would (rightly) self-destruct.
    """
    raws = []
    tariffs = [(500, 300, 1), (400, 250, 2), (600, 200, 1), (700, 150, 2), (450, 350, 1)]
    for (base, per, cut1) in tariffs:
        for w2 in (3, 5, 7, 9, 11, 13):  # weight = w2/2 kg
            w = Rational(w2, 2)
            extra = w - cut1
            if extra <= 0:
                continue
            started = int(extra) + 1                    # ceil of a half-integer
            cost = base + per * started
            d_floor = base + per * int(extra)           # rounded down instead of up
            d_exact = base + per * extra                # charged proportionally
            d_nobase = per * started                    # forgot the base charge
            raws.append({
                "statement": "A courier charges ₮$%d$ for the first $%d$ kg and ₮$%d$ "
                             "for each ADDITIONAL kilogram or part of one. What does a "
                             "package weighing $%s$ kg cost, in tögrög?"
                             % (base, cut1, per, fmt(w)),
                "correct": cost,
                "dvals": [d_floor, d_exact, d_nobase],
                "explanation": "Beyond the first $%d$ kg there are $%s$ kg extra, and "
                               "\"or part of one\" ROUNDS UP: $%d$ started "
                               "kilogram%s. Cost $= %d + %d \\cdot %d = %d$. A step "
                               "tariff jumps at each cut — it never charges "
                               "proportionally."
                               % (cut1, fmt(extra), started,
                                  "s" if started != 1 else "", base, per, started, cost),
                "check": ["Eq(%d + %d*ceiling(Rational(%d,2) - %d), %d)"
                          % (base, per, w2, cut1, cost)],
            })
    return raws


# ===========================================================================
# Data Distributions
# ===========================================================================

def _g_median():
    """Median of 7 values (odd count: the middle one)."""
    raws = []
    base_sets = [
        (2, 4, 5, 7, 9, 11, 14), (3, 3, 6, 8, 10, 13, 15), (1, 2, 4, 6, 9, 12, 13),
        (5, 6, 8, 9, 12, 15, 19), (2, 5, 7, 10, 11, 14, 18), (4, 4, 5, 8, 11, 12, 16),
    ]
    for vals in base_sets:
        for shift in (0, 1, 2, 3, 5):
            v = tuple(x + shift for x in vals)
            med = v[3]
            mean = Rational(sum(v), 7)
            mid = Rational(v[0] + v[6], 2)
            if med in (mean, mid) or mean == mid:
                continue
            raws.append({
                "statement": "Find the median of the data set $%s$."
                             % ", ".join(str(x) for x in v),
                "correct": med,
                # the mean · the midrange · the 4th value counted from a
                # 1-indexed slip (3rd value)
                "dvals": [mean, mid, v[2]],
                "explanation": "Seven values are already ordered, so the median is the "
                               "4th: $%d$ — three below it, three above. The mean "
                               "($%s$) weighs the VALUES; the median only counts "
                               "positions." % (med, fmt(mean)),
                "check": ["Eq(%d, %d)" % (med, v[3]),
                          "%d < %d" % (v[2], v[3]), "%d <= %d" % (v[3], v[4])],
            })
    return raws


def _g_iqr():
    """IQR of 8 values: Q3 - Q1 (quartiles = medians of the halves)."""
    raws = []
    base_sets = [
        (2, 4, 6, 8, 10, 12, 16, 20), (1, 3, 5, 7, 11, 13, 15, 21),
        (4, 6, 6, 10, 12, 14, 18, 22), (3, 5, 9, 11, 13, 17, 19, 23),
        (2, 2, 4, 8, 10, 14, 16, 18), (5, 7, 9, 13, 15, 17, 21, 27),
    ]
    for vals in base_sets:
        for shift in (0, 2, 4, 6, 10):
            v = tuple(x + shift for x in vals)
            q1 = Rational(v[1] + v[2], 2)
            q3 = Rational(v[5] + v[6], 2)
            iqr = q3 - q1
            rng = v[7] - v[0]
            med = Rational(v[3] + v[4], 2)
            if iqr in (rng, q3, med):
                continue
            raws.append({
                "statement": "For the data set $%s$, find the interquartile range (IQR)."
                             % ", ".join(str(x) for x in v),
                "correct": iqr,
                # the full range · Q3 alone · the median
                "dvals": [rng, q3, med],
                "explanation": "Split the ordered data in half: the lower half's median "
                               "is $Q_1 = %s$ and the upper half's is $Q_3 = %s$, so "
                               "IQR $= %s - %s = %s$. The RANGE ($%d$) uses the extremes "
                               "— exactly the values the IQR is built to ignore."
                               % (fmt(q1), fmt(q3), fmt(q3), fmt(q1), fmt(iqr), rng),
                "check": ["Eq(Rational(%d + %d, 2), Rational(%d,%d))" % (v[1], v[2], q1.p, q1.q),
                          "Eq(Rational(%d + %d, 2), Rational(%d,%d))" % (v[5], v[6], q3.p, q3.q),
                          "Eq(Rational(%d,%d) - Rational(%d,%d), Rational(%d,%d))"
                          % (q3.p, q3.q, q1.p, q1.q, iqr.p, iqr.q)],
            })
    return raws


def _g_fences():
    """Upper outlier fence: Q3 + 1.5 * IQR."""
    raws = []
    for q1 in (10, 12, 14, 20, 8, 16):
        for iqr in (4, 8, 12, 6, 10):
            q3 = q1 + iqr
            fence = q3 + Rational(3, 2) * iqr
            d_forgot = q3 + iqr
            d_wrongq = q1 + Rational(3, 2) * iqr
            d_below = q3 - Rational(3, 2) * iqr
            if len({fence, d_forgot, d_wrongq, d_below}) != 4:
                continue
            raws.append({
                "statement": "A data set has $Q_1 = %d$ and $Q_3 = %d$. Above what value "
                             "is a data point considered an outlier (using the "
                             "$1.5 \\cdot \\text{IQR}$ rule)?" % (q1, q3),
                "correct": fence,
                # forgot the 1.5 · started the fence at Q1 · went the wrong way
                "dvals": [d_forgot, d_wrongq, d_below],
                "explanation": "IQR $= %d - %d = %d$, so the upper fence is "
                               "$Q_3 + 1.5 \\cdot %d = %d + %s = %s$. The fence hangs "
                               "off $Q_3$, not $Q_1$ — and the $1.5$ is the whole "
                               "point of the rule."
                               % (q3, q1, iqr, iqr, q3, fmt(Rational(3, 2) * iqr), fmt(fence)),
                "check": ["Eq(%d + Rational(3,2)*%d, Rational(%d,%d))"
                          % (q3, iqr, fence.p, fence.q)],
            })
    return raws


# ===========================================================================
# assembly
# ===========================================================================

def build():
    forms = [
        form("G9-EQ1", "Variables on both sides", 1, EQ,
             "Collect x-terms on one side without a sign slip.", mk_num("G9-EQ1", _g_both_sides())),
        form("G9-EQ2", "Literal equations", 2, EQ,
             "Rearrange a formula for a chosen letter.", mk_txt("G9-EQ2", _g_literal())),
        form("G9-EQ3", "Rate problems", 3, EQ,
             "Closing-the-gap motion: rates add.", mk_num("G9-EQ3", _g_meeting())),
        form("G9-IN1", "Multi-step inequalities", 1, IN,
             "Solve ax + b < c — flip when dividing by a negative.", mk_txt("G9-IN1", _g_multistep_ineq())),
        form("G9-IN2", "Absolute-value equations", 2, IN,
             "Both branches of |x - a| = b.", mk_txt("G9-IN2", _g_abs_equation())),
        form("G9-IN3", "Absolute-value inequalities", 3, IN,
             "Inside vs outside: ≤ traps, ≥ throws out.", mk_txt("G9-IN3", _g_abs_inequality())),
        form("G9-FN1", "Evaluating functions", 1, FN,
             "Substitute and follow the order of operations.", mk_num("G9-FN1", _g_evaluate_fn())),
        form("G9-FN2", "Domain of a function", 2, FN,
             "Fractions exclude a point; roots need x ≥ a.", mk_txt("G9-FN2", _g_domain())),
        form("G9-FN3", "Solving f(x) = v", 3, FN,
             "Input for a given output — invert, don't evaluate.", mk_num("G9-FN3", _g_solve_fx())),
        form("G9-LM1", "Direct variation", 1, LM,
             "Constant ratio: y = kx.", mk_num("G9-LM1", _g_direct_variation())),
        form("G9-LM2", "Inverse variation", 2, LM,
             "Constant product: y = k/x.", mk_num("G9-LM2", _g_inverse_variation())),
        form("G9-LM3", "Models from two points", 3, LM,
             "Rate from the difference, base fee from a point.", mk_txt("G9-LM3", _g_model_two_points())),
        form("G9-SI1", "Testing a point", 1, SI,
             "Substitute the point into the inequality.", mk_txt("G9-SI1", _g_point_solution())),
        form("G9-SI2", "Systems of inequalities", 2, SI,
             "A solution must pass EVERY constraint.", mk_txt("G9-SI2", _g_system_point())),
        form("G9-SI3", "Optimizing over a region", 3, SI,
             "Evaluate the objective at every vertex.", mk_num("G9-SI3", _g_optimize_region())),
        form("G9-PW1", "Vertex of the V", 1, PW,
             "|x - h| + k puts the vertex at (h, k).", mk_txt("G9-PW1", _g_v_vertex())),
        form("G9-PW2", "Evaluating piecewise functions", 2, PW,
             "Pick the branch the input belongs to — boundaries included.", mk_num("G9-PW2", _g_piecewise_eval())),
        form("G9-PW3", "Step-function models", 3, PW,
             "\"Or part thereof\" rounds up, never proportionally.", mk_num("G9-PW3", _g_step_pricing())),
        form("G9-DD1", "The median", 1, DD,
             "The middle POSITION, not the middle value.", mk_num("G9-DD1", _g_median())),
        form("G9-DD2", "Quartiles & the IQR", 2, DD,
             "Medians of the halves; IQR = Q3 - Q1.", mk_num("G9-DD2", _g_iqr())),
        form("G9-DD3", "Outlier fences", 3, DD,
             "Q3 + 1.5·IQR marks the upper fence.", mk_num("G9-DD3", _g_fences())),
    ]
    return {
        # Slug "9" mirrors the course path /math/9, so every piece of shared
        # machinery (bank chrome, exam routes, ExamList links) lines up free.
        "slug": "9",
        "title": "Grade 9",
        "titleMn": "9-р анги",
        "blurb": "The Mid school band's exit level, drilled by topic — equations and "
                 "inequalities through functions, models, and data. Level 3 sits at "
                 "high-school-entrance difficulty.",
        "units": UNITS,
        "forms": forms,
    }
