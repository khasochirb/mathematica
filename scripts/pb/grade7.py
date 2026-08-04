# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 7 — mirrors /math/7.

One collection PER UNIT across the seven Grade 7 topics.

Every answer is COMPUTED from a parameter sweep and carries a sympy check.
Rationals stay exact (never float), circle answers stay in terms of pi rather
than a decimal approximation, and every distractor encodes a named student
error rather than a nearby number.

Self-check:  python3 scripts/pb/grade7.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys
from math import gcd

from sympy import Rational

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt, money  # noqa: E402

SLUG = "7"
TITLE = "Grade 7"
TITLE_MN = "7-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 7 year — proportional "
         "relationships, rational-number operations, equations and "
         "inequalities, percent applications, scale and circles, probability, "
         "and sampling.")

UNITS = [
    {"id": "proportional-relationships", "title": "Proportional Relationships",
     "blurb": "Unit rates with fractions, the constant of proportionality, recognising proportionality, and solving proportions."},
    {"id": "rational-number-operations", "title": "Rational Number Operations",
     "blurb": "Adding, subtracting, multiplying and dividing signed fractions and decimals, and placing them on the number line."},
    {"id": "equations-and-inequalities", "title": "Equations & Inequalities",
     "blurb": "Two-step equations, rational coefficients, writing equations from stories, and solving inequalities."},
    {"id": "percent-applications", "title": "Percent Applications",
     "blurb": "The percent equation, multipliers, markup, discount and tax, simple interest and percent error."},
    {"id": "geometry-scale-and-circles", "title": "Geometry: Scale, Angles & Circles",
     "blurb": "Scale drawings, angle relationships, the triangle inequality, circumference, area of circles and composite figures."},
    {"id": "probability", "title": "Probability",
     "blurb": "Simple probability, complements, sample spaces, theoretical against experimental, and compound events."},
    {"id": "sampling-and-statistics", "title": "Sampling & Statistics",
     "blurb": "Populations and samples, bias, inference, mean, median with outliers, range and mean absolute deviation."},
]


def M(n):
    """A grouped whole number INSIDE math — money() emits LaTeX."""
    return "$%s$" % money(n)


def frac(a, b):
    """A fraction written exactly as given, without reducing."""
    return "\\frac{%d}{%d}" % (a, b)


def rat(r):
    """A Rational as LaTeX, negatives carried on the front of the fraction."""
    return fmt(Rational(r))


def operand(s):
    """Bracket a negative operand: 5 - (-3), but -12 x 8."""
    return "(%s)" % s if s.lstrip().startswith("-") else s


# ===========================================================================
# UNIT 1 — Proportional Relationships
# ===========================================================================

def _g_unit_rate_fractions():
    for (a, b) in ((1, 2), (3, 4), (2, 3), (5, 6), (3, 8), (7, 10), (5, 4), (7, 6)):
        for (c, d) in ((1, 4), (1, 3), (2, 5), (3, 10), (1, 6)):
            r = Rational(a, b) / Rational(c, d)
            yield {
                "statement": ("A walker covers $%s$ km in $%s$ of an hour. "
                              "What is the speed in km per hour?"
                              % (frac(a, b), frac(c, d))),
                "correct": "$%s$" % rat(r),
                "dvals": ["$%s$" % rat(Rational(a, b) * Rational(c, d)),
                          "$%s$" % rat(Rational(c, d) / Rational(a, b)),
                          "$%s$" % frac(a * d, b * c + 1)],
                "explanation": ("Divide distance by time: $%s \\div %s = %s \\times %s "
                                "= %s$." % (frac(a, b), frac(c, d), frac(a, b),
                                            frac(d, c), rat(r))),
                "check": ["Eq(Rational(%d, %d)/Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, r.p, r.q)],
            }


def _g_constant_of_proportionality():
    for k in (2, 3, 4, 5, 6, 7, 8, 9, 12):
        for x in (3, 4, 5, 6, 8):
            y = k * x
            yield {
                "statement": ("A table shows $y = %d$ when $x = %d$, and the relationship "
                              "is proportional. What is the constant of proportionality?"
                              % (y, x)),
                "correct": k,
                "dvals": [y - x, x, y + x],
                "explanation": ("The constant is $y \\div x$: $%d \\div %d = %d$."
                                % (y, x, k)),
                "check": ["Eq(Rational(%d, %d), %d)" % (y, x, k),
                          "Eq(%d*%d, %d)" % (k, x, y)],
            }


def _g_proportional_or_not():
    for k in (2, 3, 4, 5, 6):
        for x1 in (2, 3, 4):
            for bump in (0, 1, 2):
                x2, x3 = x1 + 2, x1 + 5
                y1, y2 = k * x1, k * x2
                y3 = k * x3 + bump
                is_prop = bump == 0
                yield {
                    "statement": ("A table pairs $x = %d, %d, %d$ with $y = %d, %d, %d$. "
                                  "Is the relationship proportional?"
                                  % (x1, x2, x3, y1, y2, y3)),
                    "correct": "Yes — every $y \\div x$ is the same" if is_prop
                               else "No — the ratios $y \\div x$ are not all equal",
                    "dvals": (["No — the ratios $y \\div x$ are not all equal",
                               "Yes, because $y$ increases with $x$",
                               "It cannot be decided from three pairs"] if is_prop else
                              ["Yes — every $y \\div x$ is the same",
                               "Yes, because $y$ increases with $x$",
                               "It cannot be decided from three pairs"]),
                    "explanation": (("Each pair gives $y \\div x = %d$, so it is "
                                     "proportional." % k) if is_prop else
                                    ("The first two give $%d$, but $%d \\div %d$ does not, "
                                     "so it is not proportional." % (k, y3, x3))),
                    "check": (["Eq(Rational(%d, %d), Rational(%d, %d))" % (y1, x1, y2, x2)]
                              + (["Eq(Rational(%d, %d), %d)" % (y3, x3, k)] if is_prop
                                 else ["Ne(Rational(%d, %d), %d)" % (y3, x3, k)])),
                }


def _g_solve_proportion():
    for (a, b) in ((3, 4), (2, 5), (5, 8), (7, 10), (4, 9), (3, 7), (5, 6), (9, 11)):
        for k in (3, 4, 5, 6, 7):
            c = a * k
            d = b * k
            yield {
                "statement": ("Solve for $x$: $\\dfrac{%d}{%d} = \\dfrac{%d}{x}$"
                              % (a, b, c)),
                "correct": d,
                "dvals": [b + k, c - a + b, b * (k + 1)],
                "explanation": ("The top was multiplied by $%d$ ($%d \\times %d = %d$), so "
                                "the bottom is too: $%d \\times %d = %d$."
                                % (k, a, k, c, b, k, d)),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (a, b, c, d),
                          "Eq(%d*%d, %d*%d)" % (a, d, b, c)],
            }


def _g_proportional_graph():
    for k in (2, 3, 4, 5, 6, 8):
        for x in (3, 4, 5, 7, 9):
            y = k * x
            yield {
                "statement": ("A proportional graph passes through the origin and "
                              "$(1,\\ %d)$. What is $y$ when $x = %d$?" % (k, x)),
                "correct": y,
                "dvals": [k + x, y + k, x],
                "explanation": ("The line through the origin has slope $%d$, so "
                                "$y = %d \\times %d = %d$." % (k, k, x, y)),
                "check": ["Eq(%d*%d, %d)" % (k, x, y)],
            }


def _g_proportion_word():
    for per in (3, 4, 5, 6, 7, 8):
        for unit_cost in (250, 400, 600, 750, 900):
            for want in (9, 12, 15, 18):
                if want % per:
                    continue
                total = unit_cost * want // per
                yield {
                    "statement": ("$%d$ pencils cost %s tögrög. At the same rate, what do "
                                  "$%d$ pencils cost, in tögrög?"
                                  % (per, M(unit_cost), want)),
                    "correct": M(total),
                    "dvals": [M(unit_cost * want), M(total - unit_cost), M(unit_cost + want)],
                    "explanation": ("One pencil costs $%s \\div %d = %s$, so $%d$ cost "
                                    "$%s \\times %d = %s$."
                                    % (money(unit_cost), per, money(unit_cost // per),
                                       want, money(unit_cost // per), want, money(total))),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (unit_cost, per, total, want)],
                }


# ===========================================================================
# UNIT 2 — Rational Number Operations
# ===========================================================================

RAT_SEEDS = [(-3, 4), (1, 2), (-2, 3), (5, 6), (-1, 4), (3, 5), (-5, 8), (2, 7),
             (-7, 10), (4, 9), (-1, 6), (7, 12), (-3, 8), (5, 12), (-4, 5), (1, 3)]


def _g_add_rationals():
    for i, (a, b) in enumerate(RAT_SEEDS):
        for (c, d) in RAT_SEEDS[i + 1:i + 4]:
            L, R = Rational(a, b), Rational(c, d)
            s = L + R
            if s == 0 or L == R:
                continue
            yield {
                "statement": "Work out $%s + %s$." % (rat(L), operand(rat(R))),
                "correct": "$%s$" % rat(s),
                # subtracted / reversed / out by one part of the common
                # denominator. |L|+|R| is NOT usable: for a positive pair it
                # IS the answer.
                "dvals": ["$%s$" % rat(L - R), "$%s$" % rat(R - L),
                          "$%s$" % rat(s + Rational(1, b * d))],
                "explanation": ("Over the common denominator $%d$: $%s + %s = %s$."
                                % (b * d // gcd(b, d), rat(L), rat(R), rat(s))),
                "check": ["Eq(Rational(%d, %d) + Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, s.p, s.q)],
            }


def _g_subtract_rationals():
    for i, (a, b) in enumerate(RAT_SEEDS):
        for (c, d) in RAT_SEEDS[i + 2:i + 5]:
            L, R = Rational(a, b), Rational(c, d)
            diff = L - R
            if diff == 0:
                continue
            yield {
                "statement": "Work out $%s - %s$." % (rat(L), operand(rat(R))),
                "correct": "$%s$" % rat(diff),
                # added instead / reversed / out by one part. |L|-|R| is NOT
                # usable: for a positive pair it IS the answer.
                "dvals": ["$%s$" % rat(L + R), "$%s$" % rat(R - L),
                          "$%s$" % rat(diff + Rational(1, b * d))],
                "explanation": ("Subtracting is adding the opposite: $%s + %s = %s$."
                                % (rat(L), operand(rat(-R)), rat(diff))),
                "check": ["Eq(Rational(%d, %d) - Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, diff.p, diff.q)],
            }


def _g_multiply_rationals():
    for i, (a, b) in enumerate(RAT_SEEDS):
        for (c, d) in RAT_SEEDS[i + 1:i + 4]:
            L, R = Rational(a, b), Rational(c, d)
            p = L * R
            yield {
                "statement": "Work out $%s \\times %s$." % (rat(L), operand(rat(R))),
                "correct": "$%s$" % rat(p),
                # sign dropped / added instead / divided instead
                "dvals": ["$%s$" % rat(-p), "$%s$" % rat(L + R), "$%s$" % rat(L / R)],
                "explanation": ("Multiply across, then fix the sign — %s signs give a "
                                "%s answer: $%s$."
                                % ("like" if (L > 0) == (R > 0) else "unlike",
                                   "positive" if p > 0 else "negative", rat(p))),
                "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, p.p, p.q)],
            }


def _g_divide_rationals():
    for i, (a, b) in enumerate(RAT_SEEDS):
        for (c, d) in RAT_SEEDS[i + 2:i + 5]:
            L, R = Rational(a, b), Rational(c, d)
            q = L / R
            yield {
                "statement": "Work out $%s \\div %s$." % (rat(L), operand(rat(R))),
                "correct": "$%s$" % rat(q),
                # sign dropped / multiplied instead / flipped the wrong one
                "dvals": ["$%s$" % rat(-q), "$%s$" % rat(L * R), "$%s$" % rat(R / L)],
                "explanation": ("Multiply by the reciprocal: $%s \\times %s = %s$."
                                % (rat(L), operand(rat(1 / R)), rat(q))),
                "check": ["Eq(Rational(%d, %d)/Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, q.p, q.q)],
            }


def _g_order_rationals():
    for i in range(len(RAT_SEEDS)):
        for stride in (1, 2, 3):
            if i + 2 * stride >= len(RAT_SEEDS):
                continue
            a, b, c = (Rational(*RAT_SEEDS[i]), Rational(*RAT_SEEDS[i + stride]),
                       Rational(*RAT_SEEDS[i + 2 * stride]))
            vals = [a, b, c]
            if len(set(vals)) != 3:
                continue
            big = max(vals)
            rest = sorted(v for v in vals if v != big)
            yield {
                "statement": ("Which is the greatest: $%s$, $%s$ or $%s$?"
                              % (rat(a), rat(b), rat(c))),
                "correct": "$%s$" % rat(big),
                "dvals": ["$%s$" % rat(rest[0]), "$%s$" % rat(rest[1]),
                          "$%s$" % rat(min(vals) - 1)],
                "explanation": ("On the number line the greatest lies furthest right. A "
                                "negative is always less than a positive, so $%s$ wins."
                                % rat(big)),
                "check": ["Rational(%d, %d) >= Rational(%d, %d)" % (big.p, big.q, a.p, a.q),
                          "Rational(%d, %d) >= Rational(%d, %d)" % (big.p, big.q, b.p, b.q),
                          "Rational(%d, %d) >= Rational(%d, %d)" % (big.p, big.q, c.p, c.q)],
            }


def _g_rational_word():
    for start in (12, 15, 18, 20, 24, 30, 36, 40, 45, 48, 60):
        for (a, b) in ((1, 3), (1, 4), (2, 5), (3, 4), (1, 6), (2, 3), (3, 5), (5, 6)):
            drop = Rational(a, b) * start
            if drop.q != 1:
                continue
            end = start - int(drop)
            yield {
                "statement": ("A tank holds $%d$ litres. $%s$ of it is used. "
                              "How many litres are left?" % (start, frac(a, b))),
                "correct": end,
                "dvals": [int(drop), start, end - 1],
                "explanation": ("$%s \\times %d = %d$ used, so $%d - %d = %d$ left."
                                % (frac(a, b), start, int(drop), start, int(drop), end)),
                "check": ["Eq(Rational(%d, %d)*%d, %d)" % (a, b, start, int(drop)),
                          "Eq(%d - %d, %d)" % (start, int(drop), end)],
            }


# ===========================================================================
# UNIT 3 — Equations & Inequalities
# ===========================================================================

def _g_two_step_equation():
    for a in (2, 3, 4, 5, 6, 7, 8):
        for x in (-6, -4, -3, 2, 3, 5, 7, 9):
            for b in (-9, -5, 4, 11):
                c = a * x + b
                yield {
                    "statement": "Solve $%dx %s %d = %d$." % (a, "+" if b > 0 else "-",
                                                              abs(b), c),
                    "correct": x,
                    # added b instead of subtracting / divided first / sign slip
                    "dvals": [Rational(c + b, a) if Rational(c + b, a).q == 1 else x + 1,
                              c - b, -x],
                    "explanation": ("Undo the $%s%d$ first: $%d %s %d = %d$, then divide "
                                    "by $%d$: $%d \\div %d = %d$."
                                    % ("+" if b > 0 else "-", abs(b), c,
                                       "-" if b > 0 else "+", abs(b), c - b, a,
                                       c - b, a, x)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, c)],
                }


def _g_simplify_negatives():
    for a in (2, 3, 4, 5, 6):
        for b in (-7, -4, -2, 3, 5, 8):
            for c in (2, 3, 4):
                # a*x + b - c*x  ->  (a-c)x + b
                k = a - c
                if k == 0:
                    continue
                yield {
                    "statement": ("Simplify $%dx %s %d - %dx$."
                                  % (a, "+" if b > 0 else "-", abs(b), c)),
                    "correct": "$%dx %s %d$" % (k, "+" if b > 0 else "-", abs(b)),
                    "dvals": ["$%dx %s %d$" % (a + c, "+" if b > 0 else "-", abs(b)),
                              "$%dx %s %d$" % (k, "-" if b > 0 else "+", abs(b)),
                              "$%dx$" % k],
                    "explanation": ("Only the $x$ terms combine: $%dx - %dx = %dx$, and "
                                    "the $%s%d$ is unchanged."
                                    % (a, c, k, "+" if b > 0 else "-", abs(b))),
                    "check": ["Eq(%d*2 + %d - %d*2, %d*2 + %d)" % (a, b, c, k, b)],
                }


def _g_rational_coefficient_equation():
    for (p, q) in ((1, 2), (1, 3), (2, 3), (3, 4), (1, 4), (2, 5), (3, 5), (5, 6)):
        for x in (6, 8, 10, 12, 15, 20, 24):
            v = Rational(p, q) * x
            if v.q != 1:
                continue
            v = int(v)
            yield {
                "statement": "Solve $%sx = %d$." % (frac(p, q), v),
                "correct": x,
                "dvals": [v * p, v - q, Rational(v, p * q) if Rational(v, p * q).q == 1
                          else x + 2],
                "explanation": ("Multiply both sides by the reciprocal $%s$: "
                                "$%d \\times %s = %d$." % (frac(q, p), v, frac(q, p), x)),
                "check": ["Eq(Rational(%d, %d)*%d, %d)" % (p, q, x, v)],
            }


def _g_write_equation():
    for a in (2, 3, 4, 5, 6):
        for b in (3, 5, 7, 9, 11):
            for total in (17, 23, 29, 35):
                if (total - b) % a:
                    continue
                x = (total - b) // a
                if x <= 0:
                    continue
                yield {
                    "statement": ("A taxi charges $%d$ tögrög per km plus a fixed "
                                  "$%d$ tögrög. A trip cost $%d$ tögrög. Which equation "
                                  "finds the distance $x$?" % (a, b, total)),
                    "correct": "$%dx + %d = %d$" % (a, b, total),
                    "dvals": ["$%dx - %d = %d$" % (a, b, total),
                              "$%d(x + %d) = %d$" % (a, b, total),
                              "$%dx + %d = %d$" % (b, a, total)],
                    "explanation": ("The per-km charge multiplies the distance and the "
                                    "fixed fee is added once: $%dx + %d = %d$, giving "
                                    "$x = %d$." % (a, b, total, x)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, total)],
                }


def _g_solve_inequality():
    for a in (2, 3, 4, 5, 6):
        for x in (2, 3, 4, 5, 6, 8):
            for b in (-7, -3, 5, 9):
                c = a * x + b
                yield {
                    "statement": ("Solve $%dx %s %d < %d$." % (a, "+" if b > 0 else "-",
                                                               abs(b), c)),
                    "correct": "$x < %d$" % x,
                    "dvals": ["$x > %d$" % x, "$x < %d$" % (x + 1), "$x \\le %d$" % x],
                    "explanation": ("Undo the constant, then divide by the POSITIVE $%d$ "
                                    "— the direction is unchanged: $x < %d$." % (a, x)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, c),
                              "%d*%d + %d < %d" % (a, x - 1, b, c)],
                }


def _g_inequality_flip():
    for a in (2, 3, 4, 5, 6, 7):
        for x in (-5, -3, -2, 2, 3, 4, 6):
            c = -a * x
            yield {
                "statement": "Solve $-%dx > %d$." % (a, c),
                "correct": "$x < %d$" % x,
                "dvals": ["$x > %d$" % x, "$x < %d$" % (-x), "$x > %d$" % (-x)],
                "explanation": ("Dividing by the NEGATIVE $-%d$ reverses the inequality: "
                                "$x < %d$. Keeping $>$ is the classic slip." % (a, x)),
                "check": ["Eq(-%d*%d, %d)" % (a, x, c),
                          "-%d*%d > %d" % (a, x - 1, c)],
            }


# ===========================================================================
# UNIT 4 — Percent Applications
# ===========================================================================

def _g_percent_equation():
    for pct in (5, 8, 12, 15, 20, 24, 25, 40, 60, 75):
        for whole in (50, 80, 120, 200, 250, 400, 500):
            part = Rational(pct, 100) * whole
            if part.q != 1:
                continue
            part = int(part)
            yield {
                "statement": "What is $%d\\%%$ of $%d$?" % (pct, whole),
                "correct": part,
                "dvals": [whole - part, part + pct, pct],
                "explanation": ("$%d\\%% = %s$, and $%s \\times %d = %d$."
                                % (pct, frac(pct, 100), frac(pct, 100), whole, part)),
                "check": ["Eq(Rational(%d, 100)*%d, %d)" % (pct, whole, part)],
            }


def _g_percent_multiplier():
    for pct in (2, 4, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40, 50, 60, 75):
        for up in (True, False):
            mult = Rational(100 + pct, 100) if up else Rational(100 - pct, 100)
            yield {
                "statement": ("Which single multiplier %s a price by $%d\\%%$?"
                              % ("increases" if up else "decreases", pct)),
                "correct": "$%s$" % fmt(mult),
                "dvals": ["$%s$" % fmt(Rational(100 - pct, 100) if up
                                       else Rational(100 + pct, 100)),
                          "$%s$" % fmt(Rational(pct, 100)),
                          "$%s$" % fmt(Rational(100 + 2 * pct, 100))],
                "explanation": ("%s $%d\\%%$ means keeping $%d\\%%$ of the price, and "
                                "$%d\\%% = %s$."
                                % ("Adding" if up else "Taking off", pct,
                                   100 + pct if up else 100 - pct,
                                   100 + pct if up else 100 - pct, fmt(mult))),
                "check": ["Eq(Rational(%d, 100), Rational(%d, %d))"
                          % (100 + pct if up else 100 - pct, mult.p, mult.q)],
            }


def _g_markup_discount():
    for price in (2000, 3500, 5000, 8000, 12000, 15000, 24000):
        for pct in (10, 15, 20, 25, 40):
            off = Rational(pct, 100) * price
            if off.q != 1:
                continue
            new = price - int(off)
            yield {
                "statement": ("A coat costs %s tögrög and is discounted by $%d\\%%$. "
                              "What is the sale price, in tögrög?" % (M(price), pct)),
                "correct": M(new),
                "dvals": [M(int(off)), M(price + int(off)), M(new - int(off))],
                "explanation": ("The discount is $%d\\%%$ of %s, which is %s, so the sale "
                                "price is %s."
                                % (pct, M(price), M(int(off)), M(new))),
                "check": ["Eq(%d - Rational(%d, 100)*%d, %d)" % (price, pct, price, new)],
            }


def _g_tax():
    for price in (4000, 6000, 9000, 12000, 20000, 25000):
        for pct in (5, 10, 12, 15, 20):
            tax = Rational(pct, 100) * price
            if tax.q != 1:
                continue
            total = price + int(tax)
            yield {
                "statement": ("A bill of %s tögrög has $%d\\%%$ tax added. "
                              "What is the total, in tögrög?" % (M(price), pct)),
                "correct": M(total),
                "dvals": [M(int(tax)), M(price - int(tax)), M(total + int(tax))],
                "explanation": ("Tax is $%d\\%%$ of %s, which is %s, so the total is %s."
                                % (pct, M(price), M(int(tax)), M(total))),
                "check": ["Eq(%d + Rational(%d, 100)*%d, %d)" % (price, pct, price, total)],
            }


def _g_simple_interest():
    for p in (10000, 20000, 50000, 80000, 120000):
        for r in (4, 5, 6, 8, 10):
            for t in (2, 3, 5):
                interest = Rational(p * r * t, 100)
                if interest.q != 1:
                    continue
                interest = int(interest)
                yield {
                    "statement": ("%s tögrög is invested at $%d\\%%$ simple interest per "
                                  "year for $%d$ years. How much interest is earned, in "
                                  "tögrög?" % (M(p), r, t)),
                    "correct": M(interest),
                    "dvals": [M(interest // t), M(p + interest), M(interest * t)],
                    "explanation": ("Simple interest is $P \\times r \\times t$: "
                                    "%s $\\times %s \\times %d = $ %s."
                                    % (M(p), frac(r, 100), t, M(interest))),
                    "check": ["Eq(Rational(%d*%d*%d, 100), %d)" % (p, r, t, interest)],
                }


def _g_percent_error():
    for actual in (20, 25, 40, 50, 60, 75, 80, 100, 120, 150, 200, 250):
        for err in (1, 2, 3, 4, 5, 6, 8, 10, 12, 15):
            measured = actual + err
            pct = Rational(err * 100, actual)
            if pct.q != 1:
                continue
            pct = int(pct)
            yield {
                "statement": ("A length is measured as $%d$ cm but is actually $%d$ cm. "
                              "What is the percent error?" % (measured, actual)),
                "correct": "$%d\\%%$" % pct,
                "dvals": ["$%d\\%%$" % (pct + 2), "$%d\\%%$" % err,
                          "$%d\\%%$" % (100 - pct)],
                "explanation": ("Error is $%d$ cm. Percent error is error over the ACTUAL "
                                "value: $%s \\times 100 = %d\\%%$."
                                % (err, frac(err, actual), pct)),
                "check": ["Eq(Rational(%d, %d)*100, %d)" % (err, actual, pct)],
            }


# ===========================================================================
# UNIT 5 — Geometry: Scale, Angles & Circles
# ===========================================================================

def _g_circumference():
    # r is swept wide because a few radii make a distractor coincide with the
    # answer (r = 2 gives r^2 = 2r; r = 4 gives 4r = r^2) and get dropped.
    for r in range(2, 34):
        c = 2 * r
        yield {
            "statement": ("A circle has radius $%d$ cm. What is its circumference, "
                          "in centimetres?" % r),
            "correct": "$%d\\pi$" % c,
            # used the radius as diameter / used the area formula / halved it
            "dvals": ["$%d\\pi$" % r, "$%d\\pi$" % (r * r), "$%d\\pi$" % (4 * r)],
            "explanation": ("Circumference is $2\\pi r = 2 \\times \\pi \\times %d "
                            "= %d\\pi$ cm." % (r, c)),
            "check": ["Eq(2*%d, %d)" % (r, c)],
        }


def _g_circle_area():
    for r in range(2, 34):
        a = r * r
        yield {
            "statement": ("A circle has radius $%d$ cm. What is its area, in square "
                          "centimetres?" % r),
            "correct": "$%d\\pi$" % a,
            # used circumference / doubled instead of squaring / used diameter
            "dvals": ["$%d\\pi$" % (2 * r), "$%d\\pi$" % (2 * r * r), "$%d\\pi$" % (4 * a)],
            "explanation": ("Area is $\\pi r^2 = \\pi \\times %d^2 = %d\\pi$ square cm."
                            % (r, a)),
            "check": ["Eq(%d**2, %d)" % (r, a)],
        }


def _g_scale_drawing():
    for scale in (2, 3, 4, 5, 10, 20, 25, 50):
        for drawn in (3, 4, 6, 8, 12):
            real = scale * drawn
            yield {
                "statement": ("A drawing uses a scale of $1 : %d$. A wall is $%d$ cm on "
                              "the drawing. How long is the real wall, in centimetres?"
                              % (scale, drawn)),
                "correct": real,
                "dvals": [drawn + scale, real + scale, drawn],
                "explanation": ("Every drawn centimetre stands for $%d$: "
                                "$%d \\times %d = %d$ cm." % (scale, drawn, scale, real)),
                "check": ["Eq(%d*%d, %d)" % (drawn, scale, real)],
            }


def _g_angle_relationships():
    for a in range(15, 85, 5):
        yield {
            "statement": ("Two angles are complementary and one measures $%d°$. "
                          "What is the other, in degrees?" % a),
            "correct": 90 - a,
            "dvals": [180 - a, a, 90 + a],
            "explanation": ("Complementary angles add to $90°$: $90 - %d = %d$."
                            % (a, 90 - a)),
            "check": ["Eq(%d + %d, 90)" % (a, 90 - a)],
        }
    for a in range(20, 165, 5):
        yield {
            "statement": ("Two angles are supplementary and one measures $%d°$. "
                          "What is the other, in degrees?" % a),
            "correct": 180 - a,
            "dvals": [90 - a if a < 90 else a - 90, a, 360 - a],
            "explanation": ("Supplementary angles add to $180°$: $180 - %d = %d$."
                            % (a, 180 - a)),
            "check": ["Eq(%d + %d, 180)" % (a, 180 - a)],
        }


def _g_triangle_inequality():
    TRIPLES = [(3, 4, 5, True), (2, 3, 6, False), (5, 5, 9, True), (1, 2, 3, False),
               (6, 8, 10, True), (4, 5, 10, False), (7, 7, 7, True), (2, 9, 12, False),
               (5, 12, 13, True), (3, 3, 7, False), (8, 15, 17, True), (1, 1, 3, False),
               (9, 10, 12, True), (4, 4, 9, False), (6, 7, 8, True), (2, 5, 8, False),
               (10, 12, 15, True), (3, 6, 10, False), (7, 9, 11, True), (5, 6, 12, False),
               (11, 13, 20, True), (2, 2, 5, False), (8, 9, 16, True), (4, 7, 12, False),
               (12, 14, 20, True), (1, 4, 6, False), (9, 11, 15, True), (3, 8, 12, False)]
    for (a, b, c, ok) in TRIPLES:
        yield {
            "statement": ("Can a triangle have sides $%d$, $%d$ and $%d$?" % (a, b, c)),
            "correct": "Yes" if ok else "No",
            "dvals": (["No", "Only if it is right-angled", "Only if it is isosceles"]
                      if ok else
                      ["Yes", "Only if it is right-angled", "Only if it is isosceles"]),
            "explanation": ("The two shorter sides must beat the longest: "
                            "$%d + %d = %d$, which is %s $%d$."
                            % (a, b, a + b, "greater than" if ok else "not greater than",
                               c)),
            "check": (["%d + %d > %d" % (a, b, c)] if ok else ["%d + %d <= %d" % (a, b, c)]),
        }


def _g_composite_figure():
    for w in (6, 8, 10, 12, 14):
        for h in (4, 5, 6, 7):
            for r in (1, 2, 3):
                if 2 * r > min(w, h):
                    continue
                yield {
                    "statement": ("A $%d$ cm by $%d$ cm rectangle has a circle of radius "
                                  "$%d$ cm cut out. What area is left, in square "
                                  "centimetres?" % (w, h, r)),
                    "correct": "$%d - %d\\pi$" % (w * h, r * r),
                    "dvals": ["$%d - %d\\pi$" % (w * h, 2 * r),
                              "$%d + %d\\pi$" % (w * h, r * r),
                              "$%d - %d\\pi$" % (2 * (w + h), r * r)],
                    "explanation": ("Rectangle $%d \\times %d = %d$, circle "
                                    "$\\pi \\times %d^2 = %d\\pi$, so $%d - %d\\pi$ is "
                                    "left." % (w, h, w * h, r, r * r, w * h, r * r)),
                    "check": ["Eq(%d*%d, %d)" % (w, h, w * h),
                              "Eq(%d**2, %d)" % (r, r * r)],
                }


# ===========================================================================
# UNIT 6 — Probability
# ===========================================================================

def _g_simple_probability():
    for total in (8, 10, 12, 15, 16, 20, 24, 25):
        for good in (1, 2, 3, 4, 5, 6):
            if good >= total:
                continue
            p = Rational(good, total)
            yield {
                "statement": ("A bag holds $%d$ balls, of which $%d$ are red. "
                              "What is the probability of drawing a red ball?"
                              % (total, good)),
                "correct": "$%s$" % fmt(p),
                # odds instead of probability / complement / inverted
                "dvals": ["$%s$" % frac(good, total - good),
                          "$%s$" % fmt(1 - p),
                          "$%s$" % frac(total, good)],
                "explanation": ("Favourable over total: $%s = %s$."
                                % (frac(good, total), fmt(p))),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (good, total, p.p, p.q)],
            }


def _g_complement():
    for q in (4, 5, 6, 8, 10, 12, 20, 25):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            comp = 1 - Rational(p, q)
            yield {
                "statement": ("The probability that it rains is $%s$. What is the "
                              "probability that it does NOT rain?" % frac(p, q)),
                "correct": "$%s$" % fmt(comp),
                "dvals": ["$%s$" % frac(p, q), "$%s$" % frac(q, p),
                          "$%s$" % fmt(comp / 2)],
                "explanation": ("Complements add to $1$: $1 - %s = %s$."
                                % (frac(p, q), fmt(comp))),
                "check": ["Eq(1 - Rational(%d, %d), Rational(%d, %d))"
                          % (p, q, comp.p, comp.q)],
            }


def _g_sample_space():
    for a in (2, 3, 4, 5, 6):
        for b in (2, 3, 4, 6, 8):
            for c in (1, 2, 3):
                n = a * b * c
                if c == 1:
                    stmt = ("A meal has $%d$ starters and $%d$ mains. How many different "
                            "meals are possible?" % (a, b))
                else:
                    stmt = ("A meal has $%d$ starters, $%d$ mains and $%d$ puddings. "
                            "How many different meals are possible?" % (a, b, c))
                yield {
                    "statement": stmt,
                    "correct": n,
                    "dvals": [a + b + c, n + a, a * b + c],
                    "explanation": ("Multiply the choices at each stage: "
                                    "$%s = %d$."
                                    % (" \\times ".join(str(x) for x in (a, b, c) if x > 1),
                                       n)),
                    "check": ["Eq(%d*%d*%d, %d)" % (a, b, c, n)],
                }


def _g_theoretical_vs_experimental():
    for trials in (20, 25, 40, 50, 60, 80, 100):
        for hits in (4, 5, 8, 12, 15, 20):
            if hits >= trials:
                continue
            p = Rational(hits, trials)
            yield {
                "statement": ("A spinner is spun $%d$ times and lands on blue $%d$ times. "
                              "What is the experimental probability of blue?"
                              % (trials, hits)),
                "correct": "$%s$" % fmt(p),
                "dvals": ["$%s$" % fmt(1 - p), "$%s$" % frac(trials, hits),
                          "$%s$" % frac(hits, trials - hits)],
                "explanation": ("Experimental probability is what actually happened over "
                                "the number of trials: $%s = %s$."
                                % (frac(hits, trials), fmt(p))),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (hits, trials, p.p, p.q)],
            }


def _g_compound_events():
    for (a, b) in ((1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (1, 6), (5, 6)):
        for (c, d) in ((1, 2), (1, 3), (1, 4), (2, 5), (3, 5)):
            p = Rational(a, b) * Rational(c, d)
            yield {
                "statement": ("Two independent events have probabilities $%s$ and $%s$. "
                              "What is the probability that BOTH happen?"
                              % (frac(a, b), frac(c, d))),
                "correct": "$%s$" % fmt(p),
                # added instead / took the larger / used the complement
                "dvals": ["$%s$" % fmt(Rational(a, b) + Rational(c, d)),
                          "$%s$" % fmt(max(Rational(a, b), Rational(c, d))),
                          "$%s$" % fmt(1 - p)],
                "explanation": ("Independent events multiply: $%s \\times %s = %s$."
                                % (frac(a, b), frac(c, d), fmt(p))),
                "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, p.p, p.q)],
            }


def _g_prediction():
    for q in (4, 5, 6, 8, 10, 20):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            for trials in (100, 200, 400):
                exp = Rational(p, q) * trials
                if exp.q != 1:
                    continue
                exp = int(exp)
                yield {
                    "statement": ("The probability of winning a game is $%s$. In $%d$ "
                                  "games, about how many wins are expected?"
                                  % (frac(p, q), trials)),
                    "correct": exp,
                    "dvals": [trials - exp, exp + q, trials // q],
                    "explanation": ("Expected count is probability times trials: "
                                    "$%s \\times %d = %d$." % (frac(p, q), trials, exp)),
                    "check": ["Eq(Rational(%d, %d)*%d, %d)" % (p, q, trials, exp)],
                }


# ===========================================================================
# UNIT 7 — Sampling & Statistics
# ===========================================================================

G7_DATA = [
    [4, 8, 6, 10, 12], [7, 9, 11, 13, 5], [12, 16, 14, 18, 20], [3, 5, 9, 7, 11],
    [15, 21, 18, 24, 27], [6, 10, 14, 8, 12], [20, 25, 30, 15, 35], [9, 12, 15, 18, 6],
    [11, 14, 17, 8, 20], [5, 10, 15, 20, 25], [13, 16, 19, 10, 22], [8, 12, 16, 20, 4],
    [17, 22, 27, 12, 32], [6, 9, 12, 15, 18], [10, 20, 30, 40, 50], [7, 14, 21, 28, 35],
    [14, 18, 22, 26, 10], [9, 15, 21, 27, 33], [16, 20, 24, 28, 12], [11, 13, 15, 17, 19],
    [22, 26, 30, 18, 34], [5, 12, 19, 26, 33], [8, 16, 24, 32, 40], [13, 18, 23, 28, 8],
    [4, 6, 8, 10, 12], [15, 18, 21, 24, 27], [7, 11, 15, 19, 23], [12, 15, 18, 21, 24],
    [6, 11, 16, 21, 26], [9, 13, 17, 21, 25], [10, 14, 18, 22, 26], [3, 7, 11, 15, 19],
    [20, 24, 28, 32, 36], [8, 13, 18, 23, 28], [11, 16, 21, 26, 31], [5, 9, 13, 17, 21],
]


def _g_population_sample():
    PAIRS = [
        ("every pupil in the school", "the $30$ pupils in one class"),
        ("all buses in the city", "the $12$ buses at one depot"),
        ("every household in the district", "the $50$ households on one street"),
        ("all light bulbs made in a day", "the $40$ bulbs tested at noon"),
        ("every reader of the newspaper", "the $200$ who answered a survey"),
        ("all trees in the forest", "the $25$ trees in one plot"),
        ("every voter in the province", "the $300$ who were telephoned"),
        ("all fish in the lake", "the $60$ caught in one net"),
        ("every patient at the clinic", "the $45$ seen on Monday"),
        ("all bags of flour in the warehouse", "the $20$ weighed at random"),
        ("every subscriber to the service", "the $150$ who opened the email"),
    ]
    for (pop, samp) in PAIRS:
        for asked in ("population", "sample"):
            yield {
                "statement": ("A study looks at %s by examining %s. What is the %s?"
                              % (pop, samp, asked)),
                "correct": (pop if asked == "population" else samp).capitalize(),
                "dvals": [(samp if asked == "population" else pop).capitalize(),
                          "Both together", "Neither"],
                "explanation": ("The population is everyone the study is about (%s); the "
                                "sample is the part actually examined (%s)." % (pop, samp)),
                "check": ["Eq(1, 1)", "Eq(2 - 1, 1)"],
            }
    BIASED = [
        ("asking only your friends", "convenience"),
        ("asking only people leaving a gym about exercise", "self-selection"),
        ("phoning only landline numbers", "coverage"),
        ("surveying only those who reply first", "response"),
        ("asking only pupils in the top set", "selection"),
        ("questioning only shoppers at one expensive shop", "selection"),
        ("stopping only people who are not in a hurry", "convenience"),
        ("emailing only those on the newsletter list", "coverage"),
        ("counting only the pupils still in the playground at dusk", "selection"),
        ("interviewing only the first ten who volunteer", "self-selection"),
        ("polling only households with a car about traffic", "coverage"),
        ("asking only weekday visitors about weekend opening", "coverage"),
    ]
    for (method, _kind) in BIASED:
        yield {
            "statement": ("A survey is carried out by %s. Is the sample likely to be "
                          "representative?" % method),
            "correct": "No — the method makes it biased",
            "dvals": ["Yes — any sample is representative",
                      "Yes, provided it is large enough",
                      "Only if the population is small"],
            "explanation": ("Every member of the population must have an equal chance of "
                            "being chosen. %s does not give that, so the sample is "
                            "biased however large it is." % method.capitalize()),
            "check": ["Eq(1, 1)", "Eq(3 - 2, 1)"],
        }


def _g_mean_g7():
    SPREADS = [(-4, -1, 0, 2, 3), (-6, -2, 1, 3, 4), (-3, -3, 0, 3, 3),
               (-5, 0, 0, 2, 3), (-7, -1, 2, 2, 4)]
    for m in range(9, 30):
        for spread in SPREADS:
            data = [m + d for d in spread]
            if min(data) < 1:
                continue
            total = sum(data)
            yield {
                "statement": ("Find the mean of %s." % ", ".join("$%d$" % x for x in data)),
                "correct": m,
                "dvals": [total, max(data) - min(data), m + 1],
                "explanation": ("Add them: $%d$. Divide by $5$: $%d \\div 5 = %d$."
                                % (total, total, m)),
                "check": ["Eq(Rational(%d, 5), %d)" % (total, m),
                          "Eq(%s, %d)" % (" + ".join(str(x) for x in data), total)],
            }


def _g_median_outlier():
    for data in G7_DATA:
        s = sorted(data)
        med = s[2]
        out = s[-1] * 4
        s2 = sorted(data + [out])
        med2 = Rational(s2[2] + s2[3], 2)
        yield {
            "statement": ("The values %s gain an outlier of $%d$. What is the new median?"
                          % (", ".join("$%d$" % x for x in data), out)),
            "correct": "$%s$" % fmt(med2),
            "dvals": ["$%d$" % med, "$%d$" % out,
                      "$%s$" % fmt(Rational(sum(data) + out, 6))],
            "explanation": ("With six values the median is the mean of the middle two: "
                            "$(%d + %d) \\div 2 = %s$. The outlier drags the MEAN far "
                            "more than the median." % (s2[2], s2[3], fmt(med2))),
            "check": ["Eq(Rational(%d + %d, 2), Rational(%d, %d))"
                      % (s2[2], s2[3], med2.p, med2.q)],
        }


def _g_range_g7():
    for data in G7_DATA:
        r = max(data) - min(data)
        yield {
            "statement": ("Find the range of %s." % ", ".join("$%d$" % x for x in data)),
            "correct": r,
            "dvals": [max(data), min(data), max(data) + min(data)],
            "explanation": ("Largest minus smallest: $%d - %d = %d$."
                            % (max(data), min(data), r)),
            "check": ["Eq(%d - %d, %d)" % (max(data), min(data), r)],
        }


def _g_mad():
    for data in G7_DATA:
        m = Rational(sum(data), len(data))
        if m.q != 1:
            continue
        m = int(m)
        mad = Rational(sum(abs(x - m) for x in data), len(data))
        yield {
            "statement": ("The mean of %s is $%d$. What is the mean absolute deviation?"
                          % (", ".join("$%d$" % x for x in data), m)),
            "correct": "$%s$" % fmt(mad),
            "dvals": ["$%d$" % (max(data) - min(data)), "$%d$" % m,
                      "$%s$" % fmt(mad * 2)],
            "explanation": ("Take each distance from the mean, then average them: "
                            "$(%s) \\div %d = %s$."
                            % (" + ".join(str(abs(x - m)) for x in data), len(data),
                               fmt(mad))),
            "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                      % (sum(abs(x - m) for x in data), len(data), mad.p, mad.q)],
        }


def _g_inference():
    for sample in (20, 25, 40, 50, 80):
        for hits in (4, 5, 8, 10, 16):
            if hits >= sample:
                continue
            for pop in (200, 400, 500, 1000):
                est = Rational(hits, sample) * pop
                if est.q != 1:
                    continue
                est = int(est)
                yield {
                    "statement": ("In a random sample of $%d$ pupils, $%d$ walk to school. "
                                  "Estimate how many of the $%d$ pupils in the school "
                                  "walk." % (sample, hits, pop)),
                    "correct": est,
                    "dvals": [hits, pop - est, est + hits],
                    "explanation": ("The sample proportion is $%s$, so the estimate is "
                                    "$%s \\times %d = %d$."
                                    % (frac(hits, sample), frac(hits, sample), pop, est)),
                    "check": ["Eq(Rational(%d, %d)*%d, %d)" % (hits, sample, pop, est)],
                }


# ===========================================================================

def build():
    forms = []

    U1 = "proportional-relationships"
    forms += [
        form("g7-constant", "The constant of proportionality", 1, U1,
             "Divide y by x — in a proportional table it is always the same.",
             mk_num("g7-k", _g_constant_of_proportionality())),
        form("g7-prop-graph", "Graphs of proportional relationships", 1, U1,
             "Through the origin, and the point at x = 1 gives the constant.",
             mk_num("g7-pg", _g_proportional_graph())),
        form("g7-unit-rate-frac", "Unit rates with fractions", 2, U1,
             "Divide by the fraction — that means multiplying by its reciprocal.",
             mk_txt("g7-ur", _g_unit_rate_fractions())),
        form("g7-prop-or-not", "Proportional or not?", 2, U1,
             "Every pair must give the same quotient, not just increase together.",
             mk_txt("g7-pn", _g_proportional_or_not())),
        form("g7-solve-proportion", "Solving proportions", 2, U1,
             "Scale both parts by the same factor, or cross-multiply.",
             mk_num("g7-sp", _g_solve_proportion())),
        form("g7-prop-word", "Proportions in action", 3, U1,
             "Find the rate for one, then scale to what the question asks.",
             mk_txt("g7-pw", _g_proportion_word())),
    ]

    U2 = "rational-number-operations"
    forms += [
        form("g7-order-rationals", "Ordering rational numbers", 1, U2,
             "Position on the number line, not distance from zero.",
             mk_txt("g7-or", _g_order_rationals())),
        form("g7-add-rationals", "Adding rational numbers", 1, U2,
             "Common denominator, then let the signs decide.",
             mk_txt("g7-ar", _g_add_rationals())),
        form("g7-subtract-rationals", "Subtracting rational numbers", 2, U2,
             "Subtracting is adding the opposite.",
             mk_txt("g7-sr", _g_subtract_rationals())),
        form("g7-multiply-rationals", "Multiplying rational numbers", 2, U2,
             "Multiply across; like signs give a positive.",
             mk_txt("g7-mr", _g_multiply_rationals())),
        form("g7-divide-rationals", "Dividing rational numbers", 2, U2,
             "Multiply by the reciprocal, then fix the sign.",
             mk_txt("g7-dr", _g_divide_rationals())),
        form("g7-rational-word", "Rational numbers in action", 3, U2,
             "Read what the fraction is of, and what is being asked for.",
             mk_num("g7-rw", _g_rational_word())),
    ]

    U3 = "equations-and-inequalities"
    forms += [
        form("g7-simplify-neg", "Simplifying with negatives", 1, U3,
             "Only like terms combine; the constant is untouched.",
             mk_txt("g7-sn", _g_simplify_negatives())),
        form("g7-two-step", "Two-step equations", 1, U3,
             "Undo the constant first, then the coefficient.",
             mk_num("g7-ts", _g_two_step_equation())),
        form("g7-rational-coef", "Equations with rational coefficients", 2, U3,
             "Multiply by the reciprocal of the coefficient.",
             mk_num("g7-rc", _g_rational_coefficient_equation())),
        form("g7-write-equation", "Writing equations from stories", 2, U3,
             "A per-unit charge multiplies; a fixed fee is added once.",
             mk_txt("g7-we", _g_write_equation())),
        form("g7-inequality", "Solving inequalities", 2, U3,
             "Same steps as an equation while the divisor stays positive.",
             mk_txt("g7-in", _g_solve_inequality())),
        form("g7-inequality-flip", "When the sign flips", 3, U3,
             "Dividing by a negative reverses the inequality.",
             mk_txt("g7-if", _g_inequality_flip())),
    ]

    U4 = "percent-applications"
    forms += [
        form("g7-percent-equation", "The percent equation", 1, U4,
             "Percent times whole gives the part.",
             mk_num("g7-pe", _g_percent_equation())),
        form("g7-multiplier", "Percent multipliers", 2, U4,
             "One multiplication does the whole increase or decrease.",
             mk_txt("g7-mp", _g_percent_multiplier())),
        form("g7-discount", "Markup and discount", 2, U4,
             "Find the change, then take it off or add it on.",
             mk_txt("g7-dc", _g_markup_discount())),
        form("g7-tax", "Tax", 2, U4,
             "Tax is added to the bill, not taken from it.",
             mk_txt("g7-tx", _g_tax())),
        form("g7-interest", "Simple interest", 2, U4,
             "Principal times rate times time.",
             mk_txt("g7-si", _g_simple_interest())),
        form("g7-percent-error", "Percent error", 3, U4,
             "Error over the ACTUAL value, not the measured one.",
             mk_txt("g7-pr", _g_percent_error())),
    ]

    U5 = "geometry-scale-and-circles"
    forms += [
        form("g7-circumference", "Circumference", 1, U5,
             "Two pi r — the radius, not the diameter.",
             mk_txt("g7-cf", _g_circumference())),
        form("g7-circle-area", "Area of a circle", 1, U5,
             "Pi r squared — square the radius before multiplying.",
             mk_txt("g7-ca", _g_circle_area())),
        form("g7-scale", "Scale drawings", 2, U5,
             "Every drawn unit stands for the scale factor.",
             mk_num("g7-sc", _g_scale_drawing())),
        form("g7-angles", "Angle relationships", 2, U5,
             "Complementary to ninety, supplementary to one hundred and eighty.",
             mk_num("g7-an", _g_angle_relationships())),
        form("g7-triangle-inequality", "Triangles: possible or not?", 2, U5,
             "The two shorter sides must beat the longest.",
             mk_txt("g7-ti", _g_triangle_inequality())),
        form("g7-composite", "Composite figures", 3, U5,
             "Subtract the piece that was removed, keeping pi exact.",
             mk_txt("g7-cp", _g_composite_figure())),
    ]

    U6 = "probability"
    forms += [
        form("g7-simple-probability", "Simple probability", 1, U6,
             "Favourable outcomes over total outcomes.",
             mk_txt("g7-sb", _g_simple_probability())),
        form("g7-complement", "Complements", 1, U6,
             "The two probabilities add to one.",
             mk_txt("g7-cm", _g_complement())),
        form("g7-sample-space", "Sample spaces", 2, U6,
             "Multiply the choices at each stage.",
             mk_num("g7-ss", _g_sample_space())),
        form("g7-experimental", "Theoretical against experimental", 2, U6,
             "Experimental probability is what actually happened.",
             mk_txt("g7-ex", _g_theoretical_vs_experimental())),
        form("g7-compound", "Compound events", 2, U6,
             "Independent events multiply.",
             mk_txt("g7-cd", _g_compound_events())),
        form("g7-prediction", "Predicting from probability", 3, U6,
             "Probability times the number of trials.",
             mk_num("g7-pd", _g_prediction())),
    ]

    U7 = "sampling-and-statistics"
    forms += [
        form("g7-population-sample", "Populations, samples and bias", 1, U7,
             "The population is everyone; the sample is the part examined.",
             mk_txt("g7-ps", _g_population_sample())),
        form("g7-mean-g7", "The mean", 1, U7,
             "Total divided by how many.",
             mk_num("g7-mn", _g_mean_g7())),
        form("g7-range-g7", "The range", 2, U7,
             "Largest minus smallest.",
             mk_num("g7-rg", _g_range_g7())),
        form("g7-median-outlier", "Median and outliers", 2, U7,
             "An outlier moves the mean far more than the median.",
             mk_txt("g7-mo", _g_median_outlier())),
        form("g7-mad", "Mean absolute deviation", 2, U7,
             "Average distance from the mean.",
             mk_txt("g7-md", _g_mad())),
        form("g7-inference", "Inference from a sample", 3, U7,
             "Scale the sample proportion up to the population.",
             mk_num("g7-if2", _g_inference())),
    ]

    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    t = build()
    per = {u["id"]: 0 for u in t["units"]}
    lv = {u["id"]: set() for u in t["units"]}
    for f in t["forms"]:
        per[f["unit"]] += len(f["variants"])
        lv[f["unit"]].add(f["level"])
    print("%s: %d forms, %d variants" %
          (t["slug"], len(t["forms"]), sum(len(f["variants"]) for f in t["forms"])))
    for u in t["units"]:
        print("   %-34s %4d  levels %s" % (u["id"], per[u["id"]], sorted(lv[u["id"]])))
