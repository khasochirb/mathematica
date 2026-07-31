# -*- coding: utf-8 -*-
"""SAT Math problem bank — topic-focused practice for /practice/sat.

Blueprint (memory/resource-blueprint.md): every hub offers topic-focused
practice in ITS OWN taxonomy. For the Digital SAT that taxonomy is the four
official domains — Algebra, Advanced Math, Problem-Solving & Data Analysis,
Geometry & Trigonometry — with the exam's real weighting reflected in form
counts, not just labels.

All content is 100% self-authored (locked decision, expansion-vision §4.3):
these emulate the SAT's format, register and difficulty tiers, never actual
released questions. English by hub policy. Every answer and distractor is
COMPUTED from named parameters and sympy-asserted by the gate; distractors
encode one specific student error each.

Levels map to the SAT's difficulty tiers: 1 easy, 2 medium, 3 hard.
"""
import math
from sympy import Rational

from imbank import (
    CAP, FLOOR, fmt, lin, quad, xpm,
    mk_num, mk_txt, form,
    P, seg, ang, closed, figure,
)


# ===========================================================================
# Unit 1 — Algebra (linear equations, systems, inequalities, linear models)
# ===========================================================================

def _g_linear_solve():
    """a(x + b) = cx + d, engineered so x = x0 exactly."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for c in (1, 2, 3, 4, 5, 7):
            if c == a:
                continue
            for x0 in (-6, -4, -3, -2, 2, 3, 4, 5):
                b = (x0 % 5) + 1
                d = a * (x0 + b) - c * x0
                raws.append({
                    "statement": "If $%d(x %s %d) = %s$, what is the value of $x$?"
                                 % (a, "+" if b >= 0 else "-", abs(b), lin(c, d)),
                    "correct": x0,
                    "dvals": [x0 + 1, x0 - 1, -x0],
                    "explanation": "Distribute: $%s$. Collect the $x$ terms: $%dx = %d$, so "
                                   "$x = %d$. Forgetting to distribute over $%d$ is the "
                                   "classic slip here."
                                   % (lin(a, a * b), a - c, d - a * b, x0, b),
                    "check": ["Eq(%d*((%d) + %d), %d*(%d) + (%d))" % (a, x0, b, c, x0, d)],
                })
    return raws


def _g_slope_meaning():
    """Interpretation of m in C(x) = mx + b — pure SAT 'meaning' item."""
    jobs = [
        ("plumber", "service call"), ("electrician", "house visit"),
        ("tutor", "enrollment"), ("landscaper", "consultation"),
        ("photographer", "booking"), ("mechanic", "inspection"),
    ]
    raws = []
    for job, visit in jobs:
        for m in (25, 30, 35, 40, 45):
            for b in (20, 50, 60):
                raws.append({
                    "statement": "A %s charges $C(x) = %dx + %d$ dollars for a job that "
                                 "takes $x$ hours. What is the best interpretation of the "
                                 "number $%d$ in this context?" % (job, m, b, m),
                    "correct": "Each additional hour of work adds %d dollars to the total charge." % m,
                    "dvals": [
                        "The one-time fee for the %s is %d dollars." % (visit, m),
                        "The total charge for a one-hour job is %d dollars." % m,
                        "Each additional hour of work adds %d dollars to the total charge." % b,
                    ],
                    "explanation": "In $C(x) = %dx + %d$ the coefficient of $x$ is the rate of "
                                   "change: one more hour raises the charge by $%d$ dollars. "
                                   "The constant $%d$ is the one-time fee, and a one-hour job "
                                   "costs $%d$, not $%d$."
                                   % (m, b, m, b, m + b, m),
                    "check": ["Eq(%d*1 + %d - (%d*0 + %d), %d)" % (m, b, m, b, m)],
                })
    return raws


def _g_system_solve():
    """2x2 system built from its solution; asked for x."""
    raws = []
    for (p, q) in ((2, 3), (3, 2), (2, 5), (3, 4), (4, 3)):
        for x0 in (-4, -3, -2, -1, 1, 2, 3, 4):
            for y0 in (-3, -2, -1, 1, 2, 3):
                c1 = p * x0 + q * y0
                c2 = x0 - y0
                raws.append({
                    "statement": "The system $%dx + %dy = %d$ and $x - y = %d$ has solution "
                                 "$(x,\\ y)$. What is the value of $x$?" % (p, q, c1, c2),
                    "correct": x0,
                    "dvals": [y0, x0 + y0, -x0],
                    "explanation": "From the second equation, $y = x - (%d)$. Substitute: "
                                   "$%dx + %d(x - (%d)) = %d$, so $%dx = %d$ and $x = %d$ "
                                   "(then $y = %d$)."
                                   % (c2, p, q, c2, c1, p + q, c1 + q * c2, x0, y0),
                    "check": ["Eq(%d*(%d) + %d*(%d), %d)" % (p, x0, q, y0, c1),
                              "Eq((%d) - (%d), %d)" % (x0, y0, c2)],
                })
    return raws


def _g_line_two_points():
    """Slope of the line through two given points."""
    raws = []
    for m in (-4, -3, -2, 2, 3, 4, 5):
        for b in (-5, -3, -1, 0, 2, 4):
            for x1 in (-4, -2, -1, 1, 2):
                x2 = x1 + 2 + (abs(b) % 3)
                y1, y2 = m * x1 + b, m * x2 + b
                raws.append({
                    "statement": "A line in the $xy$-plane passes through the points "
                                 "$(%d,\\ %d)$ and $(%d,\\ %d)$. What is the slope of the line?"
                                 % (x1, y1, x2, y2),
                    "correct": m,
                    "dvals": [-m, m + 1, m - 1],
                    "explanation": "Slope $= \\dfrac{%d - (%d)}{%d - (%d)} = \\dfrac{%d}{%d} = %d$. "
                                   "Putting the run over the rise, or mixing the subtraction "
                                   "order in one coordinate only, flips or shifts the answer."
                                   % (y2, y1, x2, x1, y2 - y1, x2 - x1, m),
                    "check": ["Eq((%d) - (%d), %d*((%d) - (%d)))" % (y2, y1, m, x2, x1)],
                })
    return raws


def _g_inequality_greatest():
    """c - ax > b: the greatest integer x satisfying it is x0 - 1."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for x0 in (-4, -2, -1, 1, 2, 3, 5, 6):
            for b in (1, 4, 7, 10):
                c = a * x0 + b
                raws.append({
                    "statement": "If $%d - %dx > %d$, what is the greatest integer value of $x$?"
                                 % (c, a, b),
                    "correct": x0 - 1,
                    "dvals": [x0, x0 + 1, -(x0 - 1)],
                    "explanation": "Subtract $%d$: $-%dx > %d$. Dividing by $-%d$ FLIPS the "
                                   "inequality: $x < %d$. The greatest integer strictly below "
                                   "$%d$ is $%d$. Answering $%d$ means the flip was missed."
                                   % (c, a, b - c, a, x0, x0, x0 - 1, x0),
                    "check": ["%d - %d*(%d) > %d" % (c, a, x0 - 1, b),
                              "%d - %d*(%d) <= %d" % (c, a, x0, b)],
                })
    return raws


def _g_no_solution_k():
    """Value of k making a system inconsistent (parallel, different lines)."""
    raws = []
    for a in (2, 3, 4, 6):
        for e in (2, 3, 5):
            for b in (1, 2):
                if (a * e) % b:
                    continue
                k = (a * e) // b
                for c in (5, 7, 11):
                    f = c * k // a + 3          # guarantees a*f != c*k
                    if a * f == c * k:
                        f += 1
                    raws.append({
                        "statement": "For what value of $k$ does the system $%dx + %dy = %d$ "
                                     "and $kx + %dy = %d$ have no solution?" % (a, b, c, e, f),
                        "correct": k,
                        "dvals": [k + 1, k - 1, -k],
                        "explanation": "No solution means the lines are parallel but distinct: "
                                       "the coefficients must be proportional, "
                                       "$\\dfrac{k}{%d} = \\dfrac{%d}{%d}$, so $k = %d$ — while "
                                       "the constants $%d$ and $%d$ break the proportion, so the "
                                       "lines never meet." % (a, e, b, k, c, f),
                        "check": ["Eq(%d*%d - %d*%d, 0)" % (a, e, b, k),
                                  "Ne(%d*%d, %d*%d)" % (a, f, c, k)],
                    })
    return raws


def _g_linear_function_value():
    """f is linear with two known values; find a third."""
    raws = []
    for m in (-3, -2, 2, 3, 4):
        for p in (-2, -1, 1, 2):
            for gap in (2, 3, 4):
                q = p + gap
                for u0 in (-5, 0, 4, 7):
                    u, v = u0, u0 + m * gap
                    r = q + 2
                    fr = u + m * (r - p)
                    raws.append({
                        "statement": "The function $f$ is linear, $f(%d) = %d$, and "
                                     "$f(%d) = %d$. What is the value of $f(%d)$?"
                                     % (p, u, q, v, r),
                        "correct": fr,
                        "dvals": [fr + m, fr - m, m * r],
                        "explanation": "The slope is $\\dfrac{%d - (%d)}{%d - (%d)} = %d$, so each "
                                       "step of $1$ in the input adds $%d$. From $f(%d) = %d$, "
                                       "stepping to $%d$ gives $f(%d) = %d + %d \\cdot %d = %d$."
                                       % (v, u, q, p, m, m, q, v, r, r, v, m, r - q, fr),
                        "check": ["Eq((%d) + %d*((%d) - (%d)), %d)" % (u, m, q, p, v),
                                  "Eq((%d) + %d*((%d) - (%d)), %d)" % (u, m, r, p, fr)],
                    })
    return raws


# ===========================================================================
# Unit 2 — Advanced Math (quadratics, exponents, functions, exponentials)
# ===========================================================================

def _g_vieta_sum():
    """Sum of the solutions of a factorable quadratic."""
    raws = []
    for r1 in range(-7, 8):
        for r2 in range(r1 + 1, 8):
            if r1 == 0 or r2 == 0:
                continue
            s, pr = r1 + r2, r1 * r2
            raws.append({
                "statement": "What is the sum of the solutions of $%s = 0$?"
                             % quad(1, -s, pr),
                "correct": s,
                "dvals": [-s, pr, -pr],
                "explanation": "The quadratic factors as $%s%s = 0$, so the solutions are "
                               "$%d$ and $%d$ and their sum is $%d$. (Vieta: for "
                               "$x^2 + bx + c$, the sum is $-b$ — here $-(%d) = %d$.)"
                               % (xpm(-r1), xpm(-r2), r1, r2, s, -s, s),
                "check": ["Eq((%d) + (%d), %d)" % (r1, r2, s),
                          "Eq((%d)*(%d), %d)" % (r1, r2, pr),
                          "Eq((%d)**2 - (%d)*(%d) + (%d), 0)" % (r1, s, r1, pr)],
            })
    return raws


def _g_exponent_rules():
    """(x^a * x^b)^c / x^d = x^n — find n."""
    raws = []
    for a in (1, 2, 3, 4, 5):
        for b in (1, 2, 3, 4):
            for c in (2, 3):
                for d in (1, 2, 3, 5):
                    n = (a + b) * c - d
                    raws.append({
                        "statement": "If $\\dfrac{(x^{%d} \\cdot x^{%d})^{%d}}{x^{%d}} = x^{n}$ "
                                     "for all $x \\ne 0$, what is the value of $n$?"
                                     % (a, b, c, d),
                        "correct": n,
                        "dvals": [a * b * c - d, (a + b) * c + d, a + b + c - d],
                        "explanation": "Inside the parentheses the exponents ADD: "
                                       "$x^{%d}$. The power multiplies: $x^{%d}$. Division "
                                       "subtracts: $n = %d - %d = %d$. Multiplying $%d \\cdot %d$ "
                                       "instead of adding is the standard slip."
                                       % (a + b, (a + b) * c, (a + b) * c, d, n, a, b),
                        "check": ["Eq((%d + %d)*%d - %d, %d)" % (a, b, c, d, n)],
                    })
    return raws


def _g_vertex():
    """Vertex of y = ax^2 + bx + c with b = 2at so the vertex is integral."""
    raws = []
    for a in (1, 2, 3):
        for t in (-4, -3, -2, -1, 1, 2, 3, 4):
            b = 2 * a * t
            for c in (-6, -2, 1, 3, 5, 8):
                xv = -t
                mval = c - a * t * t
                raws.append({
                    "statement": "The graph of $y = %s$ in the $xy$-plane is a parabola. "
                                 "What is the $x$-coordinate of its vertex?" % quad(a, b, c),
                    "correct": xv,
                    "dvals": [-xv, b, mval],
                    "explanation": "The vertex sits at $x = -\\dfrac{b}{2a} = -\\dfrac{%d}{%d} "
                                   "= %d$. Dropping the minus sign gives $%d$; the $y$-value "
                                   "there is $%d$, a different quantity."
                                   % (b, 2 * a, xv, -xv, mval),
                    "check": ["Eq(-Rational(%d, %d), %d)" % (b, 2 * a, xv),
                              "Eq(%d - %d*(%d)**2, %d)" % (c, a, t, mval)],
                })
    return raws


def _g_evaluate_f():
    """f(k) for a quadratic — negative k tests the (-k)^2 discipline."""
    raws = []
    for a in (1, 2, 3):
        for b in (-5, -3, -2, 2, 3, 4):
            for c in (-4, -1, 2, 5):
                for k in (-3, -2, 2, 3):
                    fk = a * k * k + b * k + c
                    raws.append({
                        "statement": "If $f(x) = %s$, what is the value of $f(%d)$?"
                                     % (quad(a, b, c), k),
                        "correct": fk,
                        "dvals": [a * k * k - b * k + c, -fk, fk - 2 * c],
                        "explanation": "$f(%d) = %d(%d)^2 %s %d \\cdot %d %s %d = %d %s %d %s %d "
                                       "= %d$. The sign of the middle term is where credit is "
                                       "usually lost."
                                       % (k, a, k, "+" if b >= 0 else "-", abs(b), k,
                                          "+" if c >= 0 else "-", abs(c),
                                          a * k * k, "+" if b * k >= 0 else "-", abs(b * k),
                                          "+" if c >= 0 else "-", abs(c), fk),
                        "check": ["Eq(%d*(%d)**2 + (%d)*(%d) + (%d), %d)" % (a, k, b, k, c, fk)],
                    })
    return raws


def _g_equivalent_factored():
    """Which expression is equivalent — factoring with signed roots."""
    raws = []
    for r1 in (-7, -5, -4, -3, -2, 2, 3, 4):
        for r2 in (-6, -4, -1, 1, 3, 5, 6, 7):
            if abs(r1) == abs(r2):
                continue
            s, pr = -(r1 + r2), r1 * r2
            body = quad(1, s, pr)
            raws.append({
                "statement": "Which of the following is equivalent to $%s$?" % body,
                "correct": "$%s%s$" % (xpm(-r1), xpm(-r2)),
                "dvals": ["$%s%s$" % (xpm(r1), xpm(r2)),
                          "$%s%s$" % (xpm(-r1), xpm(r2)),
                          "$%s%s$" % (xpm(r1), xpm(-r2))],
                "explanation": "Look for two numbers with product $%d$ and sum $%d$: they are "
                               "$%d$ and $%d$, so $%s = %s%s$. Sign errors in the brackets "
                               "produce the other three options — expand to check."
                               % (pr, s, -r1, -r2, body, xpm(-r1), xpm(-r2)),
                "check": ["Eq(expand((x + (%d))*(x + (%d))), x**2 + (%d)*x + (%d))"
                          % (-r1, -r2, s, pr)],
            })
    return raws


def _g_one_solution_k():
    """Positive k for which ax^2 + kx + c = 0 has exactly one solution."""
    raws = []
    for t in range(2, 17):
        for a in (1, 2, 3, 4):
            if (t * t) % a:
                continue
            c = (t * t) // a
            k = 2 * t
            raws.append({
                "statement": "For what positive value of $k$ does the equation "
                             "$%s = 0$ have exactly one solution?"
                             % quad(a, 0, c).replace("x^2", "x^2 + kx"),
                "correct": k,
                "dvals": [t, t * t, 4 * t],
                "explanation": "Exactly one solution means the discriminant is zero: "
                               "$k^2 - 4 \\cdot %d \\cdot %d = 0$, so $k^2 = %d$ and the "
                               "positive root is $k = %d$."
                               % (a, c, 4 * a * c, k),
                "check": ["Eq((%d)**2 - 4*%d*%d, 0)" % (k, a, c)],
            })
    return raws


def _g_exponential_value():
    """f(t) = A * b^t growth — evaluate after k periods."""
    contexts = [
        ("bacteria in a culture", "doubles", 2, "hours"),
        ("subscribers of a channel", "doubles", 2, "months"),
        ("cells in a sample", "triples", 3, "days"),
        ("views of a video", "triples", 3, "weeks"),
    ]
    raws = []
    for noun, verb, bb, unitw in contexts:
        for A in (200, 300, 400, 500, 800):
            # Periods where the error-model distractors stay distinct from the
            # answer (b=2,k=2 makes A*b*k equal A*b^k; b=2,k=4 and b=3,k=3
            # make two distractors coincide) — those combos assemble to
            # duplicate options and get dropped, so don't generate them.
            for k in ((3, 5) if bb == 2 else (2, 4)):
                val = A * bb ** k
                raws.append({
                    "statement": "The number of %s starts at $%d$ and %s every one of the "
                                 "next %d %s. How many are there at the end?"
                                 % (noun, A, verb, k, unitw),
                    "correct": val,
                    "dvals": [A * bb * k, A + bb ** k, A * bb ** (k - 1)],
                    "explanation": "Growth is multiplicative: $%d \\cdot %d^{%d} = %d$. "
                                   "Computing $%d \\cdot %d \\cdot %d$ (linear growth) gives "
                                   "$%d$ — the exponential/linear confusion the SAT tests."
                                   % (A, bb, k, val, A, bb, k, A * bb * k),
                    "check": ["Eq(%d*%d**%d, %d)" % (A, bb, k, val)],
                })
    return raws


# ===========================================================================
# Unit 3 — Problem-Solving & Data Analysis
# ===========================================================================

def _g_percent_of():
    contexts = ["students at a school", "seats in a theater",
                "books in a library", "employees of a company"]
    raws = []
    for ctx in contexts:
        for p in (15, 20, 25, 35, 40, 45, 55, 60, 65, 75, 85):
            for n in (240, 360, 400, 480, 600):
                v = n * p // 100
                if n * p % 100:
                    continue
                raws.append({
                    "statement": "Exactly $%d\\%%$ of the $%d$ %s satisfy a condition. "
                                 "How many is that?" % (p, n, ctx),
                    "correct": v,
                    "dvals": [n - v, v + n // 100, n * p // 10 if n * p // 10 != v else v + 1],
                    "explanation": "$%d\\%%$ of $%d$ is $\\dfrac{%d}{100} \\cdot %d = %d$. "
                                   "The complement, $%d$, answers a different question "
                                   "('how many do NOT')." % (p, n, p, n, v, n - v),
                    "check": ["Eq(Rational(%d, 100)*%d, %d)" % (p, n, v)],
                })
    return raws


def _g_ratio_share():
    raws = []
    for (a, b) in ((2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (5, 7)):
        for u in (4, 6, 8, 10, 12, 15):
            T = (a + b) * u
            mx, mn = max(a, b) * u, min(a, b) * u
            raws.append({
                "statement": "A drawer holds red and blue pens in the ratio $%d : %d$, "
                             "and there are $%d$ pens in total. How many pens are in the "
                             "LARGER group?" % (a, b, T),
                "correct": mx,
                # smaller group · one part too many · found the part size and
                # stopped (mx - u would equal mn for every consecutive ratio)
                "dvals": [mn, mx + u, u],
                "explanation": "The ratio splits the total into $%d + %d = %d$ equal parts of "
                               "$\\dfrac{%d}{%d} = %d$ each. The larger group has $%d$ parts: "
                               "$%d \\cdot %d = %d$."
                               % (a, b, a + b, T, a + b, u, max(a, b), max(a, b), u, mx),
                "check": ["Eq(%d*(%d + %d), %d)" % (u, a, b, T),
                          "Eq(%d + %d, %d)" % (mx, mn, T)],
            })
    return raws


def _g_new_mean():
    raws = []
    for n in (4, 5, 6, 8, 9):
        for m in (10, 12, 15, 18, 20):
            for m2 in (m + 1, m + 2, m + 3):
                v = m2 * (n + 1) - m * n
                raws.append({
                    "statement": "The mean of $%d$ numbers is $%d$. After one more number is "
                                 "included, the mean of all $%d$ numbers is $%d$. What number "
                                 "was included?" % (n, m, n + 1, m2),
                    "correct": v,
                    "dvals": [m2, v - n, m2 + n],
                    "explanation": "Means hide sums: the first $%d$ numbers total $%d \\cdot %d "
                                   "= %d$, and all $%d$ total $%d \\cdot %d = %d$. The new "
                                   "number is the difference: $%d - %d = %d$."
                                   % (n, n, m, n * m, n + 1, n + 1, m2, (n + 1) * m2,
                                      (n + 1) * m2, n * m, v),
                    "check": ["Eq(%d*(%d) - %d*%d, %d)" % (m2, n + 1, m, n, v),
                              "Eq(Rational(%d*%d + %d, %d), %d)" % (m, n, v, n + 1, m2)],
                })
    return raws


def _g_rate_minutes():
    raws = []
    for r in (24, 36, 40, 48, 60, 72):
        for t in (15, 20, 30, 45, 50):
            if (r * t) % 60:
                continue
            d = r * t // 60
            raws.append({
                "statement": "A train travels at a constant $%d$ miles per hour. How many "
                             "miles does it travel in $%d$ minutes?" % (r, t),
                "correct": d,
                "dvals": [r * t, d * 2, r - t if r - t > 0 and r - t != d else d + 5],
                "explanation": "$%d$ minutes is $\\dfrac{%d}{60}$ of an hour, so the distance "
                               "is $%d \\cdot \\dfrac{%d}{60} = %d$ miles. Multiplying "
                               "$%d \\cdot %d$ without converting units gives the giant "
                               "distractor." % (t, t, r, t, d, r, t),
                "check": ["Eq(Rational(%d*%d, 60), %d)" % (r, t, d)],
            })
    return raws


def _g_outlier_effect():
    """Removing a large outlier: mean moves more than the median (mk_txt)."""
    raws = []
    for a in range(2, 16):
        for extra in (24, 30, 36, 44):
            o = a + extra
            vals = [a, a + 1, a + 2, a + 3, o]
            drop_med_num = 1          # median falls from a+2 to a+3/2: drop = 1/2
            mean_with_num = 4 * a + 6 + o
            mean_wo_num = 4 * a + 6
            # mean drop = mean_with/5 - mean_wo/4 must exceed 1/2 for the claim
            if Rational(mean_with_num, 5) - Rational(mean_wo_num, 4) <= Rational(1, 2):
                continue
            raws.append({
                "statement": "A data set consists of the values $%d,\\ %d,\\ %d,\\ %d,\\ %d$. "
                             "If the largest value is removed, which statement is true?"
                             % tuple(vals),
                "correct": "The mean decreases by more than the median decreases.",
                "dvals": [
                    "The median decreases by more than the mean decreases.",
                    "The mean and the median decrease by the same amount.",
                    "Neither the mean nor the median changes.",
                ],
                "explanation": "The outlier $%d$ drags the mean up hard but barely touches the "
                               "middle of the list. Removing it drops the median only from "
                               "$%d$ to $%s$ (half a unit), while the mean falls from "
                               "$%s$ to $%s$ — more than half a unit. Outliers hit the mean, "
                               "not the median."
                               % (o, a + 2, fmt(Rational(2 * a + 3, 2)),
                                  fmt(Rational(mean_with_num, 5)), fmt(Rational(mean_wo_num, 4))),
                "check": ["(Rational(%d, 5) - Rational(%d, 4)) > Rational(1, 2)"
                          % (mean_with_num, mean_wo_num),
                          "Eq((%d) - Rational(%d, 2), Rational(1, 2))" % (a + 2, 2 * a + 3)],
            })
            del drop_med_num
    return raws


def _g_weighted_mean():
    raws = []
    for n1 in (10, 12, 15, 20):
        for n2 in (5, 10, 15, 20):
            for m1 in (60, 70, 80):
                for dm in (5, 10, 15):
                    m2 = m1 + dm
                    tot = n1 * m1 + n2 * m2
                    if tot % (n1 + n2):
                        continue
                    M = tot // (n1 + n2)
                    if 2 * M == m1 + m2:
                        continue          # would collide with the unweighted trap
                    raws.append({
                        "statement": "In one class of $%d$ students the mean score was $%d$; "
                                     "in another class of $%d$ students it was $%d$. What was "
                                     "the mean score of all $%d$ students combined?"
                                     % (n1, m1, n2, m2, n1 + n2),
                        "correct": M,
                        "dvals": [Rational(m1 + m2, 2), m1, m2],
                        "explanation": "Weight by class size: $\\dfrac{%d \\cdot %d + %d \\cdot "
                                       "%d}{%d} = \\dfrac{%d}{%d} = %d$. Averaging the two means "
                                       "as $%s$ ignores that the classes are different sizes."
                                       % (n1, m1, n2, m2, n1 + n2, tot, n1 + n2, M,
                                          fmt(Rational(m1 + m2, 2))),
                        "check": ["Eq(Rational(%d*%d + %d*%d, %d), %d)"
                                  % (n1, m1, n2, m2, n1 + n2, M)],
                    })
    return raws


def _g_conditional_from_survey():
    raws = []
    for a in (12, 15, 18, 21, 24):        # seniors preferring X
        for c in (6, 9, 10, 14, 16):      # juniors preferring X
            for b in (8, 11, 13):         # seniors preferring Y
                d = b + 4                 # juniors preferring Y
                val = Rational(a, a + c)
                raws.append({
                    "statement": "In a survey, $%d$ seniors and $%d$ juniors preferred plan X, "
                                 "while $%d$ seniors and $%d$ juniors preferred plan Y. If a "
                                 "surveyed student who preferred plan X is chosen at random, "
                                 "what is the probability that the student is a senior?"
                                 % (a, c, b, d),
                    "correct": val,
                    "dvals": [Rational(c, a + c),
                              Rational(a, a + b),
                              Rational(a, a + b + c + d)],
                    "explanation": "The condition shrinks the world to the $%d + %d = %d$ "
                                   "students who preferred X. Among them $%d$ are seniors: "
                                   "$\\dfrac{%d}{%d}$. Dividing by all seniors or by everyone "
                                   "surveyed answers different questions."
                                   % (a, c, a + c, a, a, a + c),
                    "check": ["Eq(Rational(%d, %d + %d), Rational(%d, %d))"
                              % (a, a, c, val.p, val.q)],
                })
    return raws


# ===========================================================================
# Unit 4 — Geometry & Trigonometry
# ===========================================================================

def _tri_fig(x_deg, y_deg, labx, laby, labz):
    """Triangle with base angles x°, y° (exact construction), angle marks."""
    xr, yr = math.radians(x_deg), math.radians(y_deg)
    base = 6.0
    cx = base * math.tan(yr) / (math.tan(xr) + math.tan(yr))
    cy = cx * math.tan(xr)
    pts = [P("A", 0, 0), P("B", base, 0), P("C", cx, cy)]
    objs = closed(["A", "B", "C"])
    objs += [ang("A", "B", "C", labx), ang("B", "C", "A", laby), ang("C", "A", "B", labz)]
    return figure(pts, objs)


def _g_triangle_angles():
    raws = []
    for x in range(35, 76, 5):
        for y in range(40, 81, 8):
            z = 180 - x - y
            if z < 25 or z > 110 or z in (x, y):
                continue
            raws.append({
                "statement": "In the triangle shown, two angles measure $%d^\\circ$ and "
                             "$%d^\\circ$. What is the measure of the third angle?" % (x, y),
                "correct": z,
                # forgot the second angle · summed the givens (exterior-angle
                # confusion) · borrow slip: subtracted from 190 instead of 180
                "dvals": [180 - x, x + y, z + 10],
                "explanation": "The angles of a triangle sum to $180^\\circ$: "
                               "$180 - %d - %d = %d$." % (x, y, z),
                "check": ["Eq(%d + %d + %d, 180)" % (x, y, z)],
                "geoFigure": _tri_fig(x, y, "%d°" % x, "%d°" % y, "?"),
            })
    return raws


def _g_area_missing_side():
    raws = []
    for w in (4, 5, 6, 8, 9, 12):
        for l in (7, 10, 11, 13, 15):
            A = w * l
            raws.append({
                "statement": "A rectangle has area $%d$ square centimeters and width $%d$ "
                             "centimeters. What is its length, in centimeters?" % (A, w),
                "correct": l,
                "dvals": [A - w, l + w, 2 * (l + w)],
                "explanation": "Area $=$ width $\\times$ length, so the length is "
                               "$\\dfrac{%d}{%d} = %d$. Subtracting instead of dividing, or "
                               "reaching for the perimeter formula, gives the traps."
                               % (A, w, l),
                "check": ["Eq(%d*%d, %d)" % (w, l, A)],
            })
    for b in (6, 8, 10, 12):
        for h in (5, 7, 9, 11):
            A = b * h // 2
            if (b * h) % 2:
                continue
            raws.append({
                "statement": "A triangle has area $%d$ square inches and base $%d$ inches. "
                             "What is its height, in inches?" % (A, b),
                "correct": h,
                "dvals": [2 * h, A - b, h + 2],
                "explanation": "Area $= \\tfrac{1}{2} \\cdot$ base $\\cdot$ height, so "
                               "$%d = \\tfrac{1}{2} \\cdot %d \\cdot h$ and $h = %d$. "
                               "Forgetting the $\\tfrac{1}{2}$ halves the answer."
                               % (A, b, h),
                "check": ["Eq(Rational(1,2)*%d*%d, %d)" % (b, h, A)],
            })
    return raws


def _rt_fig(a, b, la, lb, lc):
    """Right triangle, legs a (horizontal) and b (vertical), scaled to ~6 wide."""
    s = 6.0 / max(a, b)
    pts = [P("A", 0, 0), P("B", a * s, 0), P("C", 0, b * s)]
    objs = closed(["A", "B", "C"], labels=[la, lc, lb])
    objs.append(ang("A", "B", "C", None))
    return figure(pts, objs)


def _g_pythagorean():
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]
    raws = []
    for (a0, b0, c0) in triples:
        for k in (1, 2, 3, 4):
            a, b, c = a0 * k, b0 * k, c0 * k
            if c > 130:
                continue
            raws.append({
                "statement": "The right triangle shown has legs of length $%d$ and $%d$. "
                             "What is the length of its hypotenuse?" % (a, b),
                "correct": c,
                "dvals": [a + b, c + k, c - k],
                "explanation": "By the Pythagorean theorem, $%d^2 + %d^2 = %d + %d = %d = %d^2$, "
                               "so the hypotenuse is $%d$. Adding the legs is the tempting "
                               "shortcut that never works." % (a, b, a * a, b * b, c * c, c, c),
                "check": ["Eq((%d)**2 + (%d)**2, (%d)**2)" % (a, b, c)],
                "geoFigure": _rt_fig(a, b, str(a), str(b), "?"),
            })
            raws.append({
                "statement": "A right triangle has hypotenuse $%d$ and one leg of length $%d$. "
                             "What is the length of the other leg?" % (c, a),
                "correct": b,
                "dvals": [c - a, b + k, a + c],
                "explanation": "$%d^2 - %d^2 = %d - %d = %d = %d^2$, so the missing leg is "
                               "$%d$. Subtracting the lengths themselves ($%d - %d$) skips the "
                               "squares." % (c, a, c * c, a * a, b * b, b, b, c, a),
                "check": ["Eq((%d)**2 - (%d)**2, (%d)**2)" % (c, a, b)],
            })
    return raws


def _g_circle_equation():
    raws = []
    for h in (-5, -3, -2, 2, 3, 4):
        for k in (-4, -1, 1, 5):
            for r in (3, 4, 5, 6, 7, 9, 10):
                raws.append({
                    "statement": "The graph of $(x %s %d)^2 + (y %s %d)^2 = %d$ in the "
                                 "$xy$-plane is a circle. What is the radius of the circle?"
                                 % ("-" if h > 0 else "+", abs(h),
                                    "-" if k > 0 else "+", abs(k), r * r),
                    "correct": r,
                    "dvals": [r * r, 2 * r, r + 2],
                    "explanation": "The right side of the standard form is $r^2$, not $r$: "
                                   "$r^2 = %d$ gives $r = %d$. Reading $%d$ off as the radius "
                                   "is the classic misread; the center is $(%d,\\ %d)$."
                                   % (r * r, r, r * r, h, k),
                    "check": ["Eq((%d)**2, %d)" % (r, r * r)],
                })
    return raws


def _g_volume_solve():
    raws = []
    for r in (2, 3, 4, 5, 6):
        for h in (3, 5, 7, 8, 10, 12, 15):
            V = r * r * h
            raws.append({
                "statement": "A right circular cylinder has volume $%d\\pi$ cubic centimeters "
                             "and base radius $%d$ centimeters. What is its height, in "
                             "centimeters?" % (V, r),
                "correct": h,
                # divided by r once · read r as the diameter (radius r/2 gives
                # 4h) · subtracted r^2 instead of dividing by it
                "dvals": [r * h, 4 * h, V - r * r],
                "explanation": "$V = \\pi r^2 h$, so $%d\\pi = \\pi \\cdot %d \\cdot h$ and "
                               "$h = \\dfrac{%d}{%d} = %d$. Dividing by $r$ instead of $r^2$ "
                               "leaves a factor of $%d$ behind." % (V, r * r, V, r * r, h, r),
                "check": ["Eq(Rational(%d, (%d)**2), %d)" % (V, r, h)],
            })
    return raws


def _g_cofunction():
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
               (9, 40, 41), (12, 35, 37)]
    raws = []
    for (p, s, q) in triples:
        for swap in (False, True):
            opp, adj = (p, s) if not swap else (s, p)
            sin_a = Rational(opp, q)
            raws.append({
                "statement": "In right triangle $ABC$, the right angle is at $C$ and "
                             "$\\sin A = \\dfrac{%d}{%d}$. What is the value of $\\cos B$?"
                             % (opp, q),
                "correct": sin_a,
                "dvals": [Rational(adj, q), Rational(opp, adj), Rational(q, opp)],
                "explanation": "Angles $A$ and $B$ are complementary ($A + B = 90^\\circ$), and "
                               "the cofunction identity says $\\cos B = \\sin A = "
                               "\\dfrac{%d}{%d}$ — no computation needed. Solving for the third "
                               "side and building $\\cos B$ from scratch lands in the same "
                               "place, slower." % (opp, q),
                "check": ["Eq((%d)**2 + (%d)**2, (%d)**2)" % (opp, adj, q),
                          "Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (opp, q, sin_a.p, sin_a.q)],
            })
            raws.append({
                "statement": "In right triangle $PQR$, the right angle is at $R$, and "
                             "$\\cos P = \\dfrac{%d}{%d}$. What is the value of $\\sin Q$?"
                             % (adj, q),
                "correct": Rational(adj, q),
                "dvals": [Rational(opp, q), Rational(adj, opp), Rational(q, adj)],
                "explanation": "$P$ and $Q$ are complementary, so $\\sin Q = \\cos P = "
                               "\\dfrac{%d}{%d}$ by the cofunction identity." % (adj, q),
                "check": ["Eq((%d)**2 + (%d)**2, (%d)**2)" % (opp, adj, q)],
            })
    return raws


def _sim_fig(a, b, c, k):
    """Two similar triangles side by side, the second scaled by k."""
    s = 3.2 / max(a, b)
    s2 = s * k
    # first triangle at origin, second shifted right
    x0 = a * s + 1.6
    pts = [P("A", 0, 0), P("B", a * s, 0), P("C", 0.3 * a * s, b * s),
           P("D", x0, 0), P("E", x0 + a * s2, 0), P("F", x0 + 0.3 * a * s2, b * s2)]
    objs = closed(["A", "B", "C"], labels=[str(a), None, None])
    objs += closed(["D", "E", "F"], labels=[str(a * k) if float(k) == int(k) else None, None, None])
    return figure(pts, objs)


def _g_similar_triangles():
    raws = []
    for (p, q) in ((3, 2), (2, 1), (5, 2), (4, 3), (5, 3), (7, 4)):
        for m in (4, 6, 8, 10):
            for n_base in (3, 5, 7, 9):
                n = n_base * q
                mk = m * p // q if (m * p) % q == 0 else None
                if mk is None:
                    continue
                ef = n * p // q
                raws.append({
                    "statement": "Triangles $ABC$ and $DEF$ shown are similar, with "
                                 "$AB = %d$, $DE = %d$, and $BC = %d$. What is the length "
                                 "of $EF$?" % (m, mk, n),
                    "correct": ef,
                    "dvals": [n + (mk - m), n, mk],
                    "explanation": "Similar triangles scale by one factor: "
                                   "$\\dfrac{DE}{AB} = \\dfrac{%d}{%d} = %s$, so "
                                   "$EF = %d \\cdot %s = %d$. Adding the same DIFFERENCE "
                                   "($+%d$) instead of multiplying by the same ratio gives "
                                   "$%d$ — the additive trap."
                                   % (mk, m, fmt(Rational(p, q)), n, fmt(Rational(p, q)),
                                      ef, mk - m, n + mk - m),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (mk, m, p, q),
                              "Eq(%d*Rational(%d, %d), %d)" % (n, p, q, ef)],
                    "geoFigure": _sim_fig(3, 2, 4, Rational(p, q)),
                })
    return raws


# ===========================================================================
# Assembly
# ===========================================================================

def build():
    forms = [
        # --- Algebra ------------------------------------------------------
        form("sat-alg-linear-solve", "Solving linear equations", 1, "algebra",
             "Distribute, collect, divide — with the signs intact.",
             mk_num("SAT-ALG1", _g_linear_solve())),
        form("sat-alg-slope-meaning", "Interpreting the slope", 1, "algebra",
             "In C(x) = mx + b, m is the per-unit rate and b the one-time part.",
             mk_txt("SAT-ALG2", _g_slope_meaning())),
        form("sat-alg-systems", "Systems of two equations", 2, "algebra",
             "Substitute or eliminate; the answer is a coordinate, not a guess.",
             mk_num("SAT-ALG3", _g_system_solve())),
        form("sat-alg-two-points", "Slope through two points", 2, "algebra",
             "Rise over run, subtracting in the SAME order top and bottom.",
             mk_num("SAT-ALG4", _g_line_two_points())),
        form("sat-alg-inequality", "Linear inequalities", 2, "algebra",
             "Dividing by a negative flips the inequality — every time.",
             mk_num("SAT-ALG5", _g_inequality_greatest())),
        form("sat-alg-no-solution", "Systems with no solution", 3, "algebra",
             "Parallel slopes, mismatched constants — proportion the coefficients.",
             mk_num("SAT-ALG6", _g_no_solution_k())),
        form("sat-alg-linear-function", "Linear functions from two values", 3, "algebra",
             "Two values fix a linear function; the slope carries you to any third.",
             mk_num("SAT-ALG7", _g_linear_function_value())),

        # --- Advanced Math ------------------------------------------------
        form("sat-adv-vieta", "Sum of the solutions", 1, "advanced-math",
             "Factor, or read the sum straight off the coefficients (Vieta).",
             mk_num("SAT-ADV1", _g_vieta_sum())),
        form("sat-adv-exponents", "Exponent rules", 1, "advanced-math",
             "Multiply inside: add. Power: multiply. Divide: subtract.",
             mk_num("SAT-ADV2", _g_exponent_rules())),
        form("sat-adv-vertex", "Vertex of a parabola", 2, "advanced-math",
             "x = -b/(2a), minus sign included; the y-value is a separate question.",
             mk_num("SAT-ADV3", _g_vertex())),
        form("sat-adv-evaluate", "Evaluating functions", 2, "advanced-math",
             "Substitute with parentheses — (-3)^2 is 9, and the middle term keeps its sign.",
             mk_num("SAT-ADV4", _g_evaluate_f())),
        form("sat-adv-factored-form", "Equivalent factored forms", 2, "advanced-math",
             "Product and sum identify the bracket numbers; expand to verify.",
             mk_txt("SAT-ADV5", _g_equivalent_factored())),
        form("sat-adv-one-solution", "Exactly one solution", 3, "advanced-math",
             "One solution means discriminant zero: k^2 = 4ac.",
             mk_num("SAT-ADV6", _g_one_solution_k())),
        form("sat-adv-exponential", "Exponential growth", 3, "advanced-math",
             "Repeated multiplication, not repeated addition: A·b^t.",
             mk_num("SAT-ADV7", _g_exponential_value())),

        # --- Problem-Solving & Data Analysis ------------------------------
        form("sat-psd-percent", "Percent of a quantity", 1, "problem-solving-data",
             "p% is p/100 — and watch whether the question asks the part or the rest.",
             mk_num("SAT-PSD1", _g_percent_of())),
        form("sat-psd-ratio", "Ratios and totals", 1, "problem-solving-data",
             "A ratio splits the total into equal parts; find the part size first.",
             mk_num("SAT-PSD2", _g_ratio_share())),
        form("sat-psd-new-mean", "Changing the mean", 2, "problem-solving-data",
             "Means hide sums — convert to totals before and after.",
             mk_num("SAT-PSD3", _g_new_mean())),
        form("sat-psd-rate", "Rates with unit conversion", 2, "problem-solving-data",
             "Minutes are not hours: convert before multiplying.",
             mk_num("SAT-PSD4", _g_rate_minutes())),
        form("sat-psd-outlier", "Outliers, mean and median", 2, "problem-solving-data",
             "Outliers drag the mean; the median barely notices them.",
             mk_txt("SAT-PSD5", _g_outlier_effect())),
        form("sat-psd-weighted-mean", "Combined means", 3, "problem-solving-data",
             "Different group sizes mean the combined mean is weighted, not averaged.",
             mk_num("SAT-PSD6", _g_weighted_mean())),
        form("sat-psd-conditional", "Conditional probability", 3, "problem-solving-data",
             "The condition shrinks the world — divide within the given group.",
             mk_num("SAT-PSD7", _g_conditional_from_survey())),

        # --- Geometry & Trigonometry --------------------------------------
        form("sat-geo-angles", "Angles in a triangle", 1, "geometry-trig",
             "The three angles always total 180°.",
             mk_num("SAT-GEO1", _g_triangle_angles())),
        form("sat-geo-area", "Area with a missing side", 1, "geometry-trig",
             "Run the area formula backwards — and keep the triangle's 1/2.",
             mk_num("SAT-GEO2", _g_area_missing_side())),
        form("sat-geo-pythagorean", "The Pythagorean theorem", 2, "geometry-trig",
             "Square, add (or subtract), then root — never add bare lengths.",
             mk_num("SAT-GEO3", _g_pythagorean())),
        form("sat-geo-circle", "Equation of a circle", 2, "geometry-trig",
             "The standard form shows r^2 on the right, not r.",
             mk_num("SAT-GEO4", _g_circle_equation())),
        form("sat-geo-volume", "Volume, solved backwards", 2, "geometry-trig",
             "V = πr²h — divide by r squared, not by r.",
             mk_num("SAT-GEO5", _g_volume_solve())),
        form("sat-geo-cofunction", "Sine and cosine of complements", 3, "geometry-trig",
             "sin A = cos(90° − A): complementary angles trade sine for cosine.",
             mk_num("SAT-GEO6", _g_cofunction())),
        form("sat-geo-similar", "Similar triangles", 3, "geometry-trig",
             "Similarity multiplies every side by the SAME ratio — never adds.",
             mk_num("SAT-GEO7", _g_similar_triangles())),
    ]

    return {
        "slug": "sat",
        "title": "SAT Math",
        "titleMn": "SAT Math",
        "blurb": "Topic-focused practice across the four Digital SAT domains — Algebra, "
                 "Advanced Math, Problem-Solving & Data Analysis, and Geometry & "
                 "Trigonometry — at the exam's three difficulty tiers.",
        "units": [
            {"id": "algebra", "title": "Algebra",
             "blurb": "Linear equations and inequalities, systems, and linear models — "
                      "about a third of every SAT Math section."},
            {"id": "advanced-math", "title": "Advanced Math",
             "blurb": "Quadratics, exponents, function notation and exponential growth — "
                      "the section that separates 600s from 700s."},
            {"id": "problem-solving-data", "title": "Problem-Solving & Data Analysis",
             "blurb": "Percents, ratios, rates, means and probability — every question is "
                      "a real-world sentence hiding one computation."},
            {"id": "geometry-trig", "title": "Geometry & Trigonometry",
             "blurb": "Angles, areas, the Pythagorean theorem, circles and right-triangle "
                      "trig — the domain with the shortest formulas and the most traps."},
        ],
        "forms": forms,
    }
