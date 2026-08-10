# -*- coding: utf-8 -*-
"""SAT bank generators that complete each subtopic's Level 1-2-3 ladder.

Re-cutting the bank onto the College Board's twenty subtopics left every
subtopic with at least three forms, but not every subtopic with all three
DIFFICULTY tiers: seven had no Level 3, six had no Level 1, and conditional
probability jumped from Level 1 straight to Level 3. The unit page offers a
level filter, so a student who picks "Level 3 - Exam" on Circles was told
that tier does not exist for the one subtopic they were revising.

This module supplies the missing tier in each case. Levels follow the house
rule (practice-test-authoring SKILL, §10): difficulty is the number of
distinct ideas chained and how hidden the entry point is, never uglier
arithmetic. A Level 1 item here is one concept in one step; a Level 3 item
chains three, or turns on an insight (a parameter that kills the solution,
completing the square twice, a constraint that binds on the other quantity).

Same contract as scripts/pb/sat.py and sat_extra.py: the answer is COMPUTED
from named parameters, each distractor encodes one named student error, and
check[] is hard-asserted by the gate before anything is written.

100% self-authored (expansion-vision §4.3). English by hub policy.
"""
from sympy import Rational

from imbank import P, ang, closed, figure, fmt, lin, quad, xpm  # noqa: F401


def _term(coef, var):
    """' + 6x' / ' - 6x' / '' — a signed term for an equation built up in place."""
    if coef == 0:
        return ""
    return " %s %s%s" % ("+" if coef > 0 else "-",
                         "" if abs(coef) == 1 else abs(coef), var)


def _const(c):
    if c == 0:
        return ""
    return " %s %d" % ("+" if c > 0 else "-", abs(c))


def _bx(p, var="x"):
    """`x + 3` / `x - 3` / `x` — xpm() without the brackets, for when the
    caller supplies its own (a squared bracket, a fraction's denominator)."""
    return xpm(p, var).strip("()") if p else var


# ===========================================================================
# Algebra
# ===========================================================================

def g_lin1_no_solution():
    """LEVEL 3 — the parameter that makes a linear equation unsolvable.

    Nothing is 'solved' here: the student has to see that matching the x
    coefficients cancels x entirely, leaving a false numeric claim. It is the
    commonest hard Algebra stem on the test and the one place where the right
    move is to stop solving.
    """
    raws = []
    for m in (2, 3, 4, 5, 6, 7):
        for b in (1, 3, 5, 8):
            for d in (2, 6, 9, 12):
                if d == b:
                    continue
                x1 = b - d               # the solution when a = m + 1
                raws.append({
                    "statement": "In the equation $%s = ax%s$, $a$ is a constant. If the "
                                 "equation has NO solution, what is the value of $a$?"
                                 % (lin(m, b), _const(d)),
                    "correct": m,
                    # sign flipped; solved the constants instead; combined both
                    "dvals": [-m, d - b, m + (d - b)],
                    "explanation": "Move every $x$ to one side: $(%d - a)x = %d - %d = %d$. "
                                   "If $a \\ne %d$ you can divide and there is exactly one "
                                   "solution, so the only way to have none is $a = %d$ — then "
                                   "the $x$ terms cancel and the equation says $%d = %d$, "
                                   "which is false. (With $a = %d$ the solution would be "
                                   "$x = %d$, so that value is not it.)"
                                   % (m, d, b, d - b, m, m, b, d, m + 1, x1),
                    "check": ["Ne(%d, %d)" % (b, d),
                              "Eq(%d*(%d) + %d, %d*(%d) + %d)"
                              % (m, x1, b, m + 1, x1, d)],
                })
    return raws


def g_lin2_perpendicular():
    """LEVEL 3 — y-intercept of the perpendicular through a point.

    Three chained ideas: negative reciprocal, substitute the point, solve for
    the intercept. Reusing the given slope is the error the distractors name.
    """
    raws = []
    # c varies SLOWEST: it is the one number in the stem that does not affect
    # the answer, so keeping it outermost stops consecutive variants from
    # differing only in an irrelevant constant.
    for c in (-3, 2, 5):
        for m in (2, 3, 4, 5, -2, -3):
            for k in (-3, -2, -1, 1, 2, 3):
                x0 = m * k
                for y0 in (-2, 1, 4):
                    b = y0 + k          # y0 - (-1/m)*x0 = y0 + x0/m = y0 + k
                    raws.append({
                        "statement": "In the $xy$-plane, line $\\ell$ passes through the "
                                     "point $(%d,\\ %d)$ and is perpendicular to the line "
                                     "$y = %s$. What is the $y$-coordinate of the "
                                     "$y$-intercept of $\\ell$?" % (x0, y0, lin(m, c)),
                        "correct": b,
                        # sign of the reciprocal; reused m; reused -m
                        "dvals": [y0 - k, y0 - m * x0, y0 + m * x0],
                        "explanation": "Perpendicular slopes multiply to $-1$, so $\\ell$ has "
                                       "slope $%s$, the negative reciprocal of $%d$. Putting "
                                       "$(%d,\\ %d)$ into $y = %sx + b$ gives $%d = %d + b$, "
                                       "so $b = %d$. Reusing the slope $%d$ itself gives $%d$."
                                       % (fmt(Rational(-1, m)), m, x0, y0,
                                          fmt(Rational(-1, m)), y0, -k, b, m,
                                          y0 - m * x0),
                        "check": ["Eq(%d * Rational(-1, %d), -1)" % (m, m),
                                  "Eq(Rational(-1, %d)*(%d) + (%d), %d)" % (m, x0, b, y0)],
                    })
    return raws


def g_sys_easy_substitute():
    """LEVEL 1 — one substitution, one division.

    The Systems unit opened at Level 2, so a student meeting simultaneous
    equations for the first time had no entry point in the bank.
    """
    raws = []
    for m in (2, 3, 4, 5, 6, 7):
        for x0 in (2, 3, 4, 5, 6, 7, 8):
            total = (m + 1) * x0
            raws.append({
                "statement": "In the system of equations $y = %dx$ and $x + y = %d$, what "
                             "is the value of $x$?" % (m, total),
                "correct": x0,
                # gave y; gave the total; added instead of multiplying
                "dvals": [m * x0, total, x0 + m],
                "explanation": "The first equation already gives $y$ in terms of $x$, so "
                               "substitute it into the second: $x + %dx = %d$, which is "
                               "$%dx = %d$, so $x = %d$. The other unknown is $y = %d$ — a "
                               "different question."
                               % (m, total, m + 1, total, x0, m * x0),
                "check": ["Eq(%d + %d, %d)" % (x0, m * x0, total),
                          "Eq(%d*%d, %d)" % (m, x0, m * x0)],
            })
    return raws


def g_ineq_easy_solve():
    """LEVEL 1 — one inequality, positive coefficient, no flip.

    Deliberately never flips: the flip has its own Level 2 form. What this
    drills is that an inequality is solved exactly like an equation when the
    coefficient is positive — and the distractor flips anyway.
    """
    rels = [("\\le", "\\ge"), ("<", ">"), ("\\ge", "\\le"), (">", "<")]
    raws = []
    for (rel, flipped) in rels:
        for a in (2, 3, 4, 5):
            for b in (-6, -3, 4, 7):
                for x0 in (-4, -2, 1, 3, 5):
                    c = a * x0 + b
                    raws.append({
                        "statement": "What is the solution to $%s %s %d$?"
                                     % (lin(a, b), rel, c),
                        "correct": "$x %s %d$" % (rel, x0),
                        "dvals": [
                            "$x %s %d$" % (flipped, x0),          # flipped for no reason
                            "$x %s %d$" % (rel, c - b),           # forgot to divide by a
                            "$x %s %s$" % (rel, fmt(Rational(c, a))),  # forgot to move b
                        ],
                        "explanation": "Take the constant across, exactly as you would in an "
                                       "equation: $%dx %s %d$. Then divide by $%d$ — and "
                                       "because $%d$ is POSITIVE the sign does not turn "
                                       "round: $x %s %d$. The sign only flips when you "
                                       "multiply or divide by a NEGATIVE number."
                                       % (a, rel, c - b, a, a, rel, x0),
                        "check": ["Eq(%d*(%d) + (%d), %d)" % (a, x0, b, c),
                                  "%d*(%d) + (%d) > %d" % (a, x0 + 1, b, c)],
                    })
    return raws


def g_ineq_compound_count():
    """LEVEL 3 — how many integers satisfy a compound inequality.

    Chains three ideas: solve both sides at once, read the strict endpoints,
    then count. The commonest wrong answer counts the endpoints themselves.
    """
    raws = []
    for a in (2, 3, 4, 5):
        for b in (-3, 1, 5):
            for lo in (-4, -2, 0, 1, 3):
                for n in (4, 5, 6, 7, 8):
                    hi = lo + n
                    low, up = a * lo + b, a * hi + b
                    raws.append({
                        "statement": "How many integer values of $x$ satisfy "
                                     "$%d < %s < %d$?" % (low, lin(a, b), up),
                        "correct": n - 1,
                        # counted both endpoints; counted one; never divided by a
                        "dvals": [n + 1, n, a * n],
                        "explanation": "Take the $%d$ across all three parts, then divide "
                                       "every part by $%d$: $%d < x < %d$. Both inequalities "
                                       "are STRICT, so $%d$ and $%d$ are themselves excluded "
                                       "and the integers that remain run from $%d$ to $%d$ — "
                                       "that is $%d - (%d) - 1 = %d$ of them. Counting the "
                                       "two endpoints as well gives $%d$."
                                       % (b, a, lo, hi, lo, hi, lo + 1, hi - 1,
                                          hi, lo, n - 1, n + 1),
                        "check": ["Eq(%d*(%d) + (%d), %d)" % (a, lo, b, low),
                                  "Eq(%d*(%d) + (%d), %d)" % (a, hi, b, up),
                                  "Eq(%d - (%d) - 1, %d)" % (hi, lo, n - 1)],
                    })
    return raws


# ===========================================================================
# Advanced Math
# ===========================================================================

def g_eq_rational_cancel():
    """LEVEL 3 — factor the numerator, then cancel.

    The 'which of the following is equivalent' stem in its hard dress: the
    student must factor a quadratic BEFORE anything cancels, and the excluded
    value in the stem is the hint that the denominator is one of the factors.
    """
    raws = []
    for p in (-5, -3, -2, 2, 3, 4, 6):
        for q in (-6, -4, -1, 1, 3, 5, 7):
            if q == p or p == 1 or q == 0:
                continue
            s, pr = p + q, p * q
            raws.append({
                "statement": "For $x \\ne %d$, which expression is equivalent to "
                             "$\\dfrac{%s}{%s}$?" % (-p, quad(1, s, pr), _bx(p)),
                "correct": "$%s$" % _bx(q),
                "dvals": [
                    "$%s$" % _bx(p),          # cancelled the wrong factor
                    "$%s$" % _bx(s),          # cancelled the x's, kept the sum
                    "$%s$" % _bx(pr),         # kept the constant term
                ],
                "explanation": "The numerator factors, because $(%d) + (%d) = %d$ and "
                               "$(%d)(%d) = %d$: $%s = %s%s$. The denominator is one "
                               "of those factors, so it cancels and what is left is $%s$. "
                               "Cancelling the $x$'s term by term is not legal — only whole "
                               "factors cancel."
                               % (p, q, s, p, q, pr, quad(1, s, pr), xpm(p), xpm(q), _bx(q)),
                "check": ["Eq(expand(%s*%s), x**2 + (%d)*x + (%d))"
                          % (xpm(p), xpm(q), s, pr),
                          "Eq(simplify((x**2 + (%d)*x + (%d))/%s - %s), 0)"
                          % (s, pr, xpm(p), xpm(q))],
            })
    return raws


def g_nlsys_easy_intersect():
    """LEVEL 1 — where a parabola meets a horizontal line.

    The nonlinear-systems unit began at Level 2. This is the one-step entry:
    a horizontal line makes the substitution trivial and leaves x^2 = k, so
    the only idea being drilled is that a square root has TWO signs.
    """
    raws = []
    for c in (-5, -3, -1, 2, 4, 6):
        for k in (2, 3, 4, 5, 6, 7, 8):
            d = k * k + c
            raws.append({
                "statement": "In the $xy$-plane, the graph of $y = %s$ and the line "
                             "$y = %d$ intersect at two points. What are the "
                             "$x$-coordinates of those points?" % (quad(1, 0, c), d),
                "correct": "$x = -%d$ and $x = %d$" % (k, k),
                "dvals": [
                    "$x = %d$ only" % k,                              # dropped the negative root
                    "$x = -%d$ and $x = %d$" % (k * k, k * k),        # never took the root
                    "$x = -%d$ and $x = %d$" % (abs(d), abs(d)),      # read off the y-value
                ],
                "explanation": "Set the two expressions equal: $x^2%s = %d$, so "
                               "$x^2 = %d$. Taking the square root of both sides gives TWO "
                               "answers, $x = %d$ and $x = -%d$, because both square to "
                               "$%d$. Reporting only the positive root is the standard slip "
                               "here."
                               % (_const(c), d, k * k, k, k, k * k),
                "check": ["Eq((%d)**2 + (%d), %d)" % (k, c, d),
                          "Eq((-%d)**2 + (%d), %d)" % (k, c, d)],
            })
    return raws


def g_nlf_vertex_form():
    """LEVEL 1 — read the vertex straight off the vertex form.

    Nonlinear Functions started at Level 2. Vertex form is the one place a
    quadratic gives up a feature with no work at all — provided you read the
    sign of h backwards, which is exactly what the first distractor does.
    """
    raws = []
    for a in (1, 2, 3, -1, -2):
        for h in (-5, -3, -2, 2, 3, 4):
            for k in (-6, -1, 3, 5, 8):
                if h == k:
                    continue
                lead = "" if a == 1 else ("-" if a == -1 else "%d" % a)
                raws.append({
                    "statement": "The function $f$ is defined by "
                                 "$f(x) = %s(%s)^2%s$. What are the coordinates of the "
                                 "vertex of the graph of $y = f(x)$ in the $xy$-plane?"
                                 % (lead, _bx(-h), _const(k)),
                    "correct": "$(%d,\\ %d)$" % (h, k),
                    "dvals": [
                        "$(%d,\\ %d)$" % (-h, k),   # took h straight from the bracket
                        "$(%d,\\ %d)$" % (h, -k),   # flipped k as well
                        "$(%d,\\ %d)$" % (k, h),    # swapped the coordinates
                    ],
                    "explanation": "In vertex form $f(x) = a(x - h)^2 + k$ the vertex is "
                                   "$(h,\\ k)$. Here the bracket is $%s$, so $h = %d$ — the "
                                   "sign INSIDE the bracket is the opposite of the "
                                   "$x$-coordinate — and $k = %d$. The vertex is "
                                   "$(%d,\\ %d)$." % (xpm(-h), h, k, h, k),
                    "check": ["Eq(%d*((%d) - (%d))**2 + (%d), %d)" % (a, h, h, k, k),
                              "Ne(%d*((%d) - (%d))**2 + (%d), %d)"
                              % (a, h + 1, h, k, k)],
                })
    return raws


# ===========================================================================
# Problem-Solving and Data Analysis
# ===========================================================================

def g_ratio_constraint():
    """LEVEL 3 — a ratio with two supplies, only one of which binds.

    Three ideas chained: convert the units, test BOTH ingredients against the
    ratio, then scale the whole recipe by the one that runs out first. Adding
    the two supplies together — the first distractor — ignores the ratio and
    is the answer most students give.
    """
    raws = []
    for (a, b) in ((5, 2), (4, 3), (7, 3), (3, 2), (5, 3), (8, 5)):
        for grams in (2000, 2400, 3000, 3600, 4000, 4500):
            for t in (100, 150, 200, 250, 300, 350):
                if grams - a * t < a:      # flour must have real slack, at least one part
                    continue
                sugar = b * t
                swapped = min(grams // b, sugar // a)
                raws.append({
                    "statement": "A dough is mixed from flour and sugar in the ratio "
                                 "$%d : %d$ by mass. A baker has $%s$ kg of flour and $%d$ g "
                                 "of sugar. What is the greatest mass of dough, in grams, "
                                 "that can be mixed?"
                                 % (a, b, ("%g" % (grams / 1000.0)), sugar),
                    "correct": (a + b) * t,
                    "dvals": [
                        grams + sugar,             # used every gram of both, ratio ignored
                        (a + b) * (grams // a),    # assumed the flour ran out first
                        (a + b) * swapped,         # applied the ratio the wrong way round
                    ],
                    "explanation": "Work in grams: $%s$ kg is $%d$ g of flour. One 'part' "
                                   "weighs the same for both, so the flour allows "
                                   "$%d \\div %d = %d$ full parts and the sugar allows "
                                   "$%d \\div %d = %d$. The SMALLER of the two is what you "
                                   "actually get — $%d$ parts — and the dough is "
                                   "$%d + %d = %d$ parts of that size: "
                                   "$%d \\cdot %d = %d$ g. Adding the two supplies gives "
                                   "$%d$ g, which would need a ratio the baker does not have."
                                   % (("%g" % (grams / 1000.0)), grams,
                                      grams, a, grams // a, sugar, b, t, t,
                                      a, b, a + b, a + b, t, (a + b) * t, grams + sugar),
                    "check": ["Eq(%d*%d, %d)" % (b, t, sugar),
                              "%d*%d < %d" % (a, t, grams),
                              "Eq((%d + %d)*%d, %d)" % (a, b, t, (a + b) * t)],
                })
    return raws


def g_1var_median():
    """LEVEL 1 — the median of a short unsorted list.

    One-Variable Data opened at Level 2. The single idea: the median is the
    middle of the SORTED list. The list is deliberately given out of order,
    and one distractor is whatever sits in the middle of it as printed.
    """
    gaps = [(0, 2, 5, 9, 14), (0, 1, 4, 8, 11), (0, 3, 6, 10, 15),
            (0, 2, 7, 11, 16), (0, 4, 5, 9, 13)]
    perms = [(2, 4, 0, 3, 1), (3, 0, 4, 1, 2)]
    raws = []
    for g in gaps:
        for a in range(3, 20):
            vals = [a + x for x in g]
            med = vals[2]
            total = sum(vals)
            mean = Rational(total, 5)
            rng = g[4]
            for perm in perms:
                shown = [vals[i] for i in perm]
                raws.append({
                    "statement": "A data set consists of the five values "
                                 "$%d,\\ %d,\\ %d,\\ %d,\\ %d$. What is the median of the "
                                 "data set?" % tuple(shown),
                    "correct": med,
                    # middle of the list AS PRINTED; the mean; the range
                    "dvals": [shown[2], mean, rng],
                    "explanation": "Put the values in order first: "
                                   "$%d,\\ %d,\\ %d,\\ %d,\\ %d$. With five values the median "
                                   "is the third one, $%d$. Taking the middle of the list as "
                                   "printed gives $%d$, and the mean, "
                                   "$\\dfrac{%d}{5} = %s$, is a different summary altogether."
                                   % (vals[0], vals[1], vals[2], vals[3], vals[4],
                                      med, shown[2], total, fmt(mean)),
                    "check": ["Eq(Rational(%d, 5), Rational(%d, %d))"
                              % (total, mean.p, mean.q),
                              "%d < %d" % (vals[0], vals[1]),
                              "%d < %d" % (vals[1], vals[2]),
                              "%d < %d" % (vals[2], vals[3]),
                              "%d < %d" % (vals[3], vals[4])],
                })
    return raws


def g_2var_overestimate():
    """LEVEL 3 — how many points the model overestimates.

    Not one residual but three, and then a count. The sign convention is the
    whole question: 'overestimates' means predicted ABOVE observed, i.e. a
    NEGATIVE residual, which is the direction students reverse.
    """
    patterns = [(1, 1, 1), (1, 1, 0), (1, 0, 0), (0, 0, 0),
                (0, 1, 1), (1, 0, 1), (0, 1, 0), (0, 0, 1)]
    raws = []
    for m in (2, 3, 4, 5):
        for b in (1, 5, 10):
            for xs in ((1, 3, 6), (2, 4, 7), (1, 4, 8)):
                for pat in patterns:
                    pts, over = [], 0
                    for (x, up) in zip(xs, pat):
                        pred = m * x + b
                        # up == 1: the model sits ABOVE the point (an overestimate)
                        obs = pred - 2 if up else pred + 2
                        pts.append((x, obs))
                        over += up
                    raws.append({
                        "statement": "A line of best fit for a data set is $y = %s$. Three "
                                     "of the data points are $(%d,\\ %d)$, $(%d,\\ %d)$ and "
                                     "$(%d,\\ %d)$. For how many of these three points does "
                                     "the model OVERESTIMATE the observed value?"
                                     % (lin(m, b), pts[0][0], pts[0][1], pts[1][0],
                                        pts[1][1], pts[2][0], pts[2][1]),
                        "correct": over,
                        "dvals": sorted({0, 1, 2, 3} - {over}),
                        "explanation": "Predict at each $x$ and compare with the observed "
                                       "$y$: the model gives $%d$, $%d$ and $%d$ against "
                                       "$%d$, $%d$ and $%d$. The model overestimates wherever "
                                       "the prediction is LARGER than the observation, and "
                                       "that is true at $%d$ of the three points. Counting "
                                       "the other direction — the points sitting ABOVE the "
                                       "line — gives $%d$ instead."
                                       % (m * xs[0] + b, m * xs[1] + b, m * xs[2] + b,
                                          pts[0][1], pts[1][1], pts[2][1], over, 3 - over),
                        "check": ["%d*(%d) + %d %s %d"
                                  % (m, x, b, ">" if up else "<", obs)
                                  for ((x, obs), up) in zip(pts, pat)],
                    })
    return raws


def g_prob_union():
    """LEVEL 2 — 'or' with an overlap.

    The probability unit jumped from Level 1 (read a table) to Level 3
    (condition on a row). This is the middle rung: two groups that overlap,
    so the counts cannot simply be added.
    """
    raws = []
    for n in (40, 50, 60, 80, 100):
        for s_pct in (55, 60, 65, 70):
            for i_pct in (35, 40, 45):
                for b_pct in (15, 20, 25):
                    s, i, both = n * s_pct // 100, n * i_pct // 100, n * b_pct // 100
                    if (n * s_pct) % 100 or (n * i_pct) % 100 or (n * b_pct) % 100:
                        continue
                    if both > min(s, i) or s + i - both > n:
                        continue
                    val = Rational(s + i - both, n)
                    if val == 1:            # certainty is not a question
                        continue
                    raws.append({
                        "statement": "Of the $%d$ students surveyed, $%d$ play a sport, $%d$ "
                                     "play an instrument, and $%d$ do both. If one of the "
                                     "surveyed students is chosen at random, what is the "
                                     "probability that the student plays a sport OR an "
                                     "instrument?" % (n, s, i, both),
                        "correct": val,
                        "dvals": [
                            Rational(s + i, n),          # added, double-counting the overlap
                            Rational(both, n),           # answered 'and' instead of 'or'
                            Rational(s + i - both, s + i),  # divided by the wrong total
                        ],
                        "explanation": "The $%d$ students who do both are inside BOTH counts, "
                                       "so adding $%d + %d = %d$ counts them twice. Subtract "
                                       "the overlap once: $%d - %d = %d$ students do at least "
                                       "one. The probability is "
                                       "$\\dfrac{%d}{%d} = \\dfrac{%d}{%d}$. Adding without "
                                       "subtracting gives $\\dfrac{%d}{%d}$."
                                       % (both, s, i, s + i, s + i, both, s + i - both,
                                          s + i - both, n, val.p, val.q, s + i, n),
                        "check": ["Eq(Rational(%d + %d - %d, %d), Rational(%d, %d))"
                                  % (s, i, both, n, val.p, val.q),
                                  "%d + %d - %d <= %d" % (s, i, both, n),
                                  "%d <= %d" % (both, min(s, i))],
                    })
    return raws


# ===========================================================================
# Geometry and Trigonometry
# ===========================================================================

def _sin_fig(leg_opp, leg_adj, hyp):
    """Right triangle, right angle at C, angle A between AC and AB."""
    s = 6.0 / max(leg_opp, leg_adj)
    pts = [P("C", 0, 0), P("A", leg_adj * s, 0), P("B", 0, leg_opp * s)]
    objs = closed(["C", "A", "B"], labels=[str(leg_adj), str(hyp), str(leg_opp)])
    objs.append(ang("C", "A", "B", None))
    return figure(pts, objs)


def g_rt_easy_ratio():
    """LEVEL 1 — one trig ratio, straight from the definition.

    Right-Triangle Trigonometry started at Level 2. All three sides are given,
    so there is no Pythagoras step: the only idea is which two sides the ratio
    names, and the distractors are the other three ratios of the same triangle.
    """
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
               (20, 21, 29), (9, 40, 41)]
    raws = []
    for (p0, q0, h0) in triples:
        for k in (1, 2, 3):
            p, q, h = p0 * k, q0 * k, h0 * k
            if h > 90:
                continue
            for (name, val, d1, d2) in (
                ("\\sin", Rational(p, h), Rational(q, h), Rational(p, q)),
                ("\\cos", Rational(q, h), Rational(p, h), Rational(q, p)),
            ):
                raws.append({
                    "statement": "In right triangle $ABC$ the right angle is at $C$, "
                                 "$BC = %d$, $AC = %d$, and $AB = %d$. What is the value of "
                                 "$%s A$?" % (p, q, h, name),
                    "correct": val,
                    # the other ratio at A; the tangent; the reciprocal
                    "dvals": [d1, d2, 1 / val],
                    "explanation": "Angle $A$ sits at vertex $A$, so the side OPPOSITE it is "
                                   "$BC = %d$, the side beside it is $AC = %d$, and the "
                                   "hypotenuse is $AB = %d$. %s of an angle is %s over "
                                   "hypotenuse: $%s A = \\dfrac{%d}{%d}$. Reading the ratio "
                                   "from the wrong vertex, or turning it upside down, "
                                   "produces the other three options."
                                   % (p, q, h, "Sine" if name == "\\sin" else "Cosine",
                                      "opposite" if name == "\\sin" else "adjacent",
                                      name, p if name == "\\sin" else q, h),
                    "check": ["Eq((%d)**2 + (%d)**2, (%d)**2)" % (p, q, h),
                              "Eq(Rational(%d, %d)**2 + Rational(%d, %d)**2, 1)"
                              % (p, h, q, h)],
                    "geoFigure": _sin_fig(p, q, h),
                })
    return raws


def g_cir_complete_square():
    """LEVEL 3 — radius from the expanded equation of a circle.

    Completing the square twice, then remembering the right-hand side is r
    SQUARED. Three chained moves and a final square root that most of the
    wrong answers skip.
    """
    raws = []
    for h in (-4, -3, -2, 2, 3, 4):
        for k in (-4, -3, 2, 3, 5):
            for r in (2, 3, 5, 6, 7, 10):
                d, e = -2 * h, -2 * k
                f = h * h + k * k - r * r
                if f == 0:
                    continue
                raws.append({
                    "statement": "In the $xy$-plane, the graph of "
                                 "$x^2 + y^2%s%s%s = 0$ is a circle. What is the radius of "
                                 "the circle?" % (_term(d, "x"), _term(e, "y"), _const(f)),
                    "correct": r,
                    # stopped at r^2; gave the diameter; read the centre instead
                    "dvals": [r * r, 2 * r, abs(h) + abs(k)],
                    "explanation": "Group and complete the square in each variable: "
                                   "$x^2%s$ needs $%d$, and $y^2%s$ needs $%d$. The equation "
                                   "becomes $(%s)^2 + (%s)^2 = %d$, so the centre is "
                                   "$(%d,\\ %d)$ and the RIGHT-HAND SIDE is $r^2$, not $r$. "
                                   "Taking the square root gives $r = %d$; stopping one step "
                                   "early gives $%d$."
                                   % (_term(d, "x"), h * h, _term(e, "y"), k * k,
                                      _bx(-h), _bx(-k, "y"), r * r, h, k, r, r * r),
                    "check": ["Eq(expand((x - (%d))**2 + (y - (%d))**2 - (%d)**2), "
                              "x**2 + y**2 + (%d)*x + (%d)*y + (%d))" % (h, k, r, d, e, f),
                              "Eq((%d)**2 + (%d)**2 - (%d), %d)" % (h, k, f, r * r)],
                })
    return raws
