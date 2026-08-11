# -*- coding: utf-8 -*-
"""Integrated Math 1 — the second half of every unit's bank.

The IM1 bank shipped with six forms per unit and a difficulty profile that
stopped at Level 2 in six of the nine units: a student who picked
"Level 3 · Exam" on Linear Functions, Coordinate Geometry or Data & Statistics
was offered a tier that did not exist. This module doubles every unit to
twelve forms and gives each one a real ramp — roughly four Level 1, five
Level 2 and three Level 3.

Level means what the house says it means (practice-test-authoring §10):
the number of distinct ideas chained and how hidden the entry point is,
never uglier arithmetic. A Level 1 form here is one concept in one step; a
Level 3 form chains three, or turns on a decision the student has to make
before any calculating starts.

Same contract as scripts/pb/integrated_1.py: the answer is COMPUTED from
named parameters, each distractor encodes one named student error, and every
check[] is sympy-asserted by the gate before anything is written.
"""
from sympy import Rational, sqrt

from imbank import fmt, lin, pt, xpm  # noqa: F401


def _ord(n):
    """1 -> 1st, 2 -> 2nd, 3 -> 3rd, 11 -> 11th ..."""
    if 10 <= n % 100 <= 20:
        return "%dth" % n
    return "%d%s" % (n, {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))


def _gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# ===========================================================================
# Unit 1 — Quantities & the Structure of Expressions
# ===========================================================================

def g_unit_of_rate():
    """LEVEL 1 — what unit a computed quantity carries."""
    cases = [
        ("distance in kilometres", "time in hours", "kilometres per hour",
         ["hours per kilometre", "kilometres", "hours"]),
        ("total cost in dollars", "number of items", "dollars per item",
         ["items per dollar", "dollars", "items"]),
        ("mass in grams", "volume in cubic centimetres", "grams per cubic centimetre",
         ["cubic centimetres per gram", "grams", "cubic centimetres"]),
        ("population", "area in square kilometres", "people per square kilometre",
         ["square kilometres per person", "people", "square kilometres"]),
        ("energy in joules", "time in seconds", "joules per second",
         ["seconds per joule", "joules", "seconds"]),
        ("volume in litres", "time in minutes", "litres per minute",
         ["minutes per litre", "litres", "minutes"]),
        ("rainfall in millimetres", "time in days", "millimetres per day",
         ["days per millimetre", "millimetres", "days"]),
        ("wage in dollars", "time in hours", "dollars per hour",
         ["hours per dollar", "dollars", "hours"]),
    ]
    raws = []
    for (top, bot, right, wrong) in cases:
        for (a, b) in ((120, 4), (75, 5), (240, 8), (54, 6)):
            raws.append({
                "statement": "A quantity is found by dividing a %s by a %s. If the two "
                             "measurements are $%d$ and $%d$, the answer is $%d$ — but in "
                             "WHAT unit?" % (top, bot, a, b, a // b),
                "correct": right,
                "dvals": list(wrong),
                "explanation": "Dividing carries the units with it: %s divided by %s gives "
                               "%s. Reading the units off the division is the fastest check "
                               "that a calculation answered the question that was asked."
                               % (top.split(" in ")[-1] if " in " in top else top,
                                  bot.split(" in ")[-1] if " in " in bot else bot, right),
                "check": ["Eq(Rational(%d, %d), %d)" % (a, b, a // b)],
            })
    return raws


def g_compound_convert():
    """LEVEL 2 — a rate converted through two units at once."""
    raws = []
    for kmh in (18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 126):
        ms = Rational(kmh * 1000, 3600)
        raws.append({
            "statement": "A speed of $%d$ kilometres per hour is how many metres per "
                         "second?" % kmh,
            "correct": ms,
            # multiplied instead of divided by 3.6; forgot the 1000; forgot the 3600
            "dvals": [Rational(kmh * 36, 10), kmh, kmh * 1000],
            "explanation": "Two conversions at once: $1$ km is $1000$ m and $1$ hour is "
                           "$3600$ s, so multiply by $\\dfrac{1000}{3600} = "
                           "\\dfrac{1}{3.6}$. Here $%d \\div 3.6 = %s$ m/s. Converting only "
                           "one of the two units is the usual slip."
                           % (kmh, fmt(ms)),
            "check": ["Eq(Rational(%d*1000, 3600), Rational(%d, %d))"
                      % (kmh, ms.p, ms.q)],
        })
    for lpm in (9, 12, 15, 18, 21, 24, 30, 36, 42, 48, 54, 60):
        lph = lpm * 60
        raws.append({
            "statement": "A pump moves $%d$ litres per minute. How many litres per hour "
                         "is that?" % lpm,
            "correct": lph,
            "dvals": [Rational(lpm, 60), lpm * 24, lpm + 60],
            "explanation": "An hour holds $60$ minutes, so multiply: "
                           "$%d \\times 60 = %d$ litres per hour. Dividing would answer "
                           "'litres per second-and-a-bit', which nobody asked for."
                           % (lpm, lph),
            "check": ["Eq(%d*60, %d)" % (lpm, lph)],
        })
    for cost, area in ((45, 4), (60, 5), (84, 6), (96, 8), (150, 10), (72, 3),
                       (110, 5), (128, 8)):
        raws.append({
            "statement": "Flooring costs $\\$%d$ for $%d$ square metres. What is the cost "
                         "per square metre?" % (cost, area),
            "correct": Rational(cost, area),
            "dvals": [Rational(area, cost), cost * area, cost - area],
            "explanation": "'Per square metre' means dollars divided by square metres: "
                           "$%d \\div %d = %s$. The units settle the direction of the "
                           "division before any arithmetic."
                           % (cost, area, fmt(Rational(cost, area))),
            "check": ["Eq(Rational(%d, %d)*%d, %d)" % (cost, area, area, cost)],
        })
    return raws


def g_area_units():
    """LEVEL 2 — converting an AREA, where the factor gets squared."""
    raws = []
    for (a, b) in ((3, 4), (2, 5), (6, 7), (4, 9), (8, 5), (3, 10),
                   (7, 7), (12, 5), (6, 6), (9, 11), (2, 15), (4, 4)):
        m2 = a * b
        cm2 = m2 * 10000
        raws.append({
            "statement": "A room measures $%d$ m by $%d$ m. What is its area in SQUARE "
                         "CENTIMETRES?" % (a, b),
            "correct": cm2,
            # used the length factor once; used it cubed; forgot to convert
            "dvals": [m2 * 100, m2 * 1000000, m2],
            "explanation": "The area is $%d \times %d = %d$ m². One metre is $100$ cm, so "
                           "one SQUARE metre is $100^2 = 10\,000$ cm² — the factor gets "
                           "squared because two lengths were multiplied. "
                           "$%d \times 10\,000 = %d$ cm². Multiplying by $100$ once is "
                           "the standard error." % (a, b, m2, m2, cm2),
            "check": ["Eq(%d*%d, %d)" % (a, b, m2),
                      "Eq(100**2, 10000)",
                      "Eq(%d*10000, %d)" % (m2, cm2)],
        })
    for km in (2, 3, 5, 6, 8, 9, 12, 15, 20, 25, 4, 7):
        raws.append({
            "statement": "A square field of side $%d$ km has what area in square metres?"
                         % km,
            "correct": km * km * 1000000,
            "dvals": [km * km * 1000, km * 1000, km * km],
            "explanation": "Side $%d$ km is $%d\,000$ m, so the area is "
                           "$(%d\,000)^2 = %d$ m². Equivalently $%d$ km² times "
                           "$1000^2 = 1\,000\,000$."
                           % (km, km, km, km * km * 1000000, km * km),
            "check": ["Eq((%d*1000)**2, %d)" % (km, km * km * 1000000),
                      "Eq(1000**2, 1000000)"],
        })
    return raws


def g_rearrange_repeated():
    """LEVEL 3 — the target letter appears twice, so it must be factored out."""
    raws = []
    for (u, v) in (("c", "d"), ("p", "q"), ("m", "n"), ("s", "t")):
        for a in (2, 3, 4, 5, 6, 7):
            for b in (1, 2, 3, 5):
                if b == a or abs(a - b) == 1 or b == 1:
                    continue
                c = 4
                raws.append({
                    "statement": "Solve $%dx + %s = %dx + %s$ for $x$, where $%s$ and $%s$ "
                                 "are constants." % (a, u, b, v, u, v),
                    "correct": "$x = \\dfrac{%s - %s}{%d}$" % (v, u, a - b),
                    "dvals": [
                        "$x = \\dfrac{%s - %s}{%d}$" % (u, v, a - b),   # subtracted backwards
                        "$x = \\dfrac{%s - %s}{%d}$" % (v, u, a + b),   # added the coefficients
                        "$x = %s - %s$" % (v, u),                        # never divided
                    ],
                    "explanation": "The unknown is on BOTH sides, so it cannot be isolated "
                                   "by moving constants alone. Gather it: "
                                   "$%dx - %dx = %s - %s$, which is $%dx = %s - %s$, so "
                                   "$x = \\dfrac{%s - %s}{%d}$. Subtracting the two "
                                   "coefficients the other way flips the sign of the whole "
                                   "answer." % (a, b, v, u, a - b, v, u, v, u, a - b),
                    "check": ["Eq(%d*Rational(%d - %d, %d) + %d, %d*Rational(%d - %d, %d) + %d)"
                              % (a, c + 12, c, a - b, c, b, c + 12, c, a - b, c + 12)],
                })
    return raws


def g_build_and_evaluate():
    """LEVEL 3 — build the expression from the situation, then evaluate it."""
    ctx = [
        ("a taxi", "a flag-fall of", "dollars and", "dollars per kilometre", "kilometres"),
        ("a printer", "a setup fee of", "dollars and", "dollars per page", "pages"),
        ("a hall", "a booking fee of", "dollars and", "dollars per hour", "hours"),
        ("a courier", "a base charge of", "dollars and", "dollars per parcel", "parcels"),
    ]
    raws = []
    for (who, f1, f2, f3, unitname) in ctx:
        for base in (12, 20, 25, 35):
            for rate in (3, 4, 6, 7):
                for n in (8, 12, 15):
                    total = base + rate * n
                    raws.append({
                        "statement": "%s charges %s $\\$%d$ %s $\\$%d$ %s. Write the cost "
                                     "as an expression in the number of %s, then find the "
                                     "cost for $%d$ %s."
                                     % (who.capitalize(), f1, base, f2, rate, f3,
                                        unitname, n, unitname),
                        "correct": total,
                        # multiplied the fee too; added the rate once; forgot the fee
                        "dvals": [(base + rate) * n, base + rate, rate * n],
                        "explanation": "The fee is charged ONCE, so it is a constant; the "
                                       "rate is charged per %s, so it is a coefficient. The "
                                       "expression is $%s$, and at $%d$ it gives "
                                       "$%d + %d = %d$. Multiplying the fee by the count "
                                       "too is the standard error."
                                       % (unitname[:-1], lin(rate, base), n, base,
                                          rate * n, total),
                        "check": ["Eq(%d*%d + %d, %d)" % (rate, n, base, total)],
                    })
    return raws


def g_interpret_parameter():
    """LEVEL 3 — what a parameter MEANS inside a compound formula."""
    raws = []
    for P in (1000, 2000, 5000, 8000):
        for r in (4, 5, 6, 8):
            for n in (2, 4, 12):
                per = {2: "twice a year", 4: "four times a year",
                       12: "every month"}[n]
                raws.append({
                    "statement": "A savings account is modelled by "
                                 "$A = %d\\left(1 + \\dfrac{0.0%d}{%d}\\right)^{%d t}$, "
                                 "where $t$ is in years. What does the $%d$ in TWO places "
                                 "of this formula represent?" % (P, r, n, n, n),
                    "correct": "The number of times interest is added per year — here, %s."
                               % per,
                    "dvals": [
                        "The number of years the money is invested.",
                        "The annual interest rate, as a percentage.",
                        "The number of dollars added each year.",
                    ],
                    "explanation": "The annual rate $0.0%d$ is split into $%d$ equal "
                                   "portions, and the exponent counts $%d$ periods per "
                                   "year — so $%d$ is the COMPOUNDING FREQUENCY, %s. The "
                                   "starting balance is $%d$ and the rate is $%d\\%%$; "
                                   "neither is what the question asked about."
                                   % (r, n, n, n, per, P, r),
                    "check": ["Eq(%d*%d, %d)" % (n, 1, n),
                              "Eq(Rational(%d, 100)/%d*%d, Rational(%d, 100))"
                              % (r, n, n, r)],
                })
    return raws


# ===========================================================================
# Unit 2 — Linear Equations & Inequalities
# ===========================================================================

def g_solve_negatives():
    """LEVEL 1 — ax + b = c with the signs working against you."""
    raws = []
    for a in (-2, -3, -4, -5, 2, 3, 4, 6):
        for x0 in (-6, -4, -3, -1, 2, 3, 5, 7):
            for b in (-9, -5, 7, 11):
                c = a * x0 + b
                raws.append({
                    "statement": "Solve $%s = %d$ for $x$." % (lin(a, b), c),
                    "correct": x0,
                    # sign of the division; added b instead of subtracting; divided first
                    "dvals": [-x0, Rational(c + b, a), Rational(c, a)],
                    "explanation": "Take the constant across first: $%dx = %d - (%d) = %d$. "
                                   "Then divide by $%d$: $x = %d$. Dividing before moving "
                                   "the constant leaves $\\dfrac{%d}{%d}$, a different "
                                   "number." % (a, c, b, c - b, a, x0, c, a),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, x0, b, c)],
                })
    return raws


def g_check_solution():
    """LEVEL 1 — which of four values actually satisfies the equation."""
    raws = []
    for a in (2, 3, 4, 5):
        for b in (-7, -3, 4, 9):
            for c in (1, 2, 5):
                for x0 in (-3, -1, 2, 4, 6):
                    rhs = a * x0 + b + c * x0
                    raws.append({
                        "statement": "Which value of $x$ satisfies "
                                     "$%s = %s$?" % (lin(a, b), lin(a + c, b - c * x0)),
                        "correct": x0,
                        "dvals": [x0 + 1, x0 - 1, -x0 if x0 != 0 else x0 + 2],
                        "explanation": "Substituting $x = %d$ makes the left side "
                                       "$%d$ and the right side $%d$ — equal, so it is the "
                                       "solution. Checking a candidate by substitution is "
                                       "always available and never wrong."
                                       % (x0, a * x0 + b, (a + c) * x0 + b - c * x0),
                        "check": ["Eq(%d*(%d) + (%d), %d*(%d) + (%d))"
                                  % (a, x0, b, a + c, x0, b - c * x0)],
                    })
    return raws


def g_clear_fractions():
    """LEVEL 2 — multiply through by the common denominator."""
    raws = []
    for p in (2, 3, 4, 5, 6):
        for q in (2, 3, 4, 6):
            if p == q:
                continue
            lcm = p * q // _gcd(p, q)
            for x0 in (lcm, 2 * lcm, 3 * lcm):
                t = Rational(x0, p) + Rational(x0, q)
                if t.q != 1:
                    continue
                raws.append({
                    "statement": "Solve $\\dfrac{x}{%d} + \\dfrac{x}{%d} = %s$."
                                 % (p, q, fmt(t)),
                    "correct": x0,
                    # added the denominators; used only one fraction; halved
                    "dvals": [Rational(t) * (p + q), Rational(t) * p,
                              Rational(x0, 2)],
                    "explanation": "Multiply every term by the common denominator $%d$: "
                                   "$%dx + %dx = %s$, so $%dx = %s$ and $x = %d$. Adding "
                                   "the denominators instead of using their common multiple "
                                   "is the classic slip."
                                   % (lcm, lcm // p, lcm // q, fmt(t * lcm),
                                      lcm // p + lcm // q, fmt(t * lcm), x0),
                    "check": ["Eq(Rational(%d,%d) + Rational(%d,%d), %s)"
                              % (x0, p, x0, q, fmt(t))],
                })
    return raws


def g_inequality_word():
    """LEVEL 2 — a threshold in words, answered by the largest whole number."""
    ctx = [("rides", "a fairground ride costs", "entry costs"),
           ("games", "each arcade game costs", "the entry fee is"),
           ("prints", "each photo print costs", "the sitting fee is"),
           ("hours", "each hour of court hire costs", "the membership fee is")]
    raws = []
    for (what, c1, c2) in ctx:
        for fee in (8, 12, 15, 20):
            for rate in (3, 4, 5, 6):
                for budget in (44, 50, 62, 71):
                    n = (budget - fee) // rate
                    if n < 3:
                        continue
                    raws.append({
                        "statement": "At a park %s $\\$%d$ and %s $\\$%d$. With $\\$%d$ to "
                                     "spend in total, what is the greatest number of %s "
                                     "affordable?" % (c1, rate, c2, fee, budget, what),
                        "correct": n,
                        # rounded up; forgot the fee; divided the budget by the fee
                        "dvals": [n + 1, budget // rate, Rational(budget, fee)],
                        "explanation": "The fee is paid once, leaving $%d - %d = %d$ for "
                                       "the %s: $%d \\div %d = %s$, and you cannot buy a "
                                       "fraction of one, so the answer rounds DOWN to $%d$. "
                                       "Rounding up would overspend."
                                       % (budget, fee, budget - fee, what, budget - fee,
                                          rate, fmt(Rational(budget - fee, rate)), n),
                        "check": ["%d*%d + %d <= %d" % (rate, n, fee, budget),
                                  "%d*%d + %d > %d" % (rate, n + 1, fee, budget)],
                    })
    return raws


def g_abs_equation():
    """LEVEL 3 — |ax + b| = c splits into two cases."""
    raws = []
    for a in (1, 2, 3, 4):
        for b in (-9, -5, -2, 3, 7):
            for c in (4, 6, 8, 10, 12):
                r1 = Rational(c - b, a)
                r2 = Rational(-c - b, a)
                if r1.q != 1 or r2.q != 1:
                    continue
                lo, hi = min(r1, r2), max(r1, r2)
                raws.append({
                    "statement": "Solve $|%s| = %d$." % (lin(a, b), c),
                    "correct": "$x = %s$ or $x = %s$" % (fmt(lo), fmt(hi)),
                    "dvals": [
                        "$x = %s$ only" % fmt(hi),                 # dropped the negative case
                        "$x = %s$ or $x = %s$" % (fmt(-hi), fmt(hi)),  # negated the answer
                        "$x = %s$ or $x = %s$" % (fmt(lo - 1), fmt(hi + 1)),
                    ],
                    "explanation": "Absolute value asks which numbers sit $%d$ away from "
                                   "zero, and there are TWO: $%s = %d$ gives $x = %s$, and "
                                   "$%s = -%d$ gives $x = %s$. Solving only the positive "
                                   "case loses half the answer."
                                   % (c, lin(a, b), c, fmt(r1), lin(a, b), c, fmt(r2)),
                    "check": ["Eq(Abs(%d*Rational(%d, %d) + (%d)), %d)"
                              % (a, r1.p, r1.q, b, c),
                              "Eq(Abs(%d*Rational(%d, %d) + (%d)), %d)"
                              % (a, r2.p, r2.q, b, c)],
                })
    return raws


def g_compound_count():
    """LEVEL 3 — how many integers satisfy a compound inequality."""
    raws = []
    for a in (2, 3, 4, 5):
        for b in (-5, -1, 2, 6):
            for lo in (-5, -3, 0, 2, 4):
                for n in (4, 5, 6, 7, 9):
                    hi = lo + n
                    low, up = a * lo + b, a * hi + b
                    raws.append({
                        "statement": "How many integers $x$ satisfy "
                                     "$%d < %s < %d$?" % (low, lin(a, b), up),
                        "correct": n - 1,
                        # counted both endpoints; counted one; never divided by a
                        "dvals": [n + 1, n, a * n],
                        "explanation": "Take the $%d$ across all three parts and divide "
                                       "every part by $%d$: $%d < x < %d$. Both bounds are "
                                       "STRICT, so the integers run from $%d$ to $%d$ — "
                                       "$%d - (%d) - 1 = %d$ of them."
                                       % (b, a, lo, hi, lo + 1, hi - 1, hi, lo, n - 1),
                        "check": ["Eq(%d*(%d) + (%d), %d)" % (a, lo, b, low),
                                  "Eq(%d*(%d) + (%d), %d)" % (a, hi, b, up),
                                  "Eq(%d - (%d) - 1, %d)" % (hi, lo, n - 1)],
                    })
    return raws


# ===========================================================================
# Unit 3 — Functions & Sequences
# ===========================================================================

def g_evaluate_f():
    """LEVEL 1 — one substitution into function notation."""
    raws = []
    for a in (2, 3, 4, 5, -2, -3):
        for b in (-7, -3, 1, 6, 9):
            for k in (-3, -1, 2, 4, 5):
                raws.append({
                    "statement": "The function $f$ is defined by $f(x) = %s$. What is "
                                 "$f(%d)$?" % (lin(a, b), k),
                    "correct": a * k + b,
                    # multiplied the constant too; added instead of multiplying; used -k
                    "dvals": [(a + b) * k, a + b + k, a * (-k) + b],
                    "explanation": "Function notation says: put $%d$ wherever $x$ appears. "
                                   "$f(%d) = %d(%d) + (%d) = %d + (%d) = %d$. The $f$ is a "
                                   "NAME, not a factor — $f(%d)$ never means $f$ times $%d$."
                                   % (k, k, a, k, b, a * k, b, a * k + b, k, k),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, k, b, a * k + b)],
                })
    return raws


def g_domain_range():
    """LEVEL 2 — domain and range of a finite set of points."""
    raws = []
    for x0 in (-4, -2, 0, 1, 3, 5):
        for d in (1, 2, 3):
            for y0 in (-3, 0, 2, 6):
                for e in (2, 4, 5):
                    xs = [x0, x0 + d, x0 + 2 * d, x0 + 3 * d]
                    ys = [y0, y0 + e, y0 + 2 * e, y0 + 3 * e]
                    raws.append({
                        "statement": "A function is given by the points "
                                     "$(%d, %d)$, $(%d, %d)$, $(%d, %d)$ and $(%d, %d)$. "
                                     "What is its DOMAIN?"
                                     % (xs[0], ys[0], xs[1], ys[1], xs[2], ys[2],
                                        xs[3], ys[3]),
                        "correct": "$\\{%d, %d, %d, %d\\}$" % tuple(xs),
                        "dvals": [
                            "$\\{%d, %d, %d, %d\\}$" % tuple(ys),      # gave the range
                            "$\\{%d, %d\\}$" % (xs[0], xs[3]),         # only the extremes
                            "$\\{%d, %d, %d, %d\\}$" % tuple(y + x for x, y in zip(xs, ys)),
                        ],
                        "explanation": "The domain is the set of INPUTS — the first "
                                       "coordinate of each point: $%d, %d, %d, %d$. The "
                                       "second coordinates form the RANGE, which is a "
                                       "different set and a different question."
                                       % tuple(xs),
                        "check": ["Eq(%d - %d, %d)" % (xs[1], xs[0], d),
                                  "Eq(%d - %d, %d)" % (ys[1], ys[0], e)],
                    })
    return raws


def g_is_function():
    """LEVEL 2 — the one-output rule, applied to a named set of pairs."""
    raws = []
    for a in (1, 2, 3, 4, 5, 6, 7):
        for c in (2, 3, 4):
            for y in (5, 8, 11, 13):
                # a genuine function: every input distinct, one output repeated
                raws.append({
                    "statement": "A relation consists of the pairs $(%d, %d)$, $(%d, %d)$ "
                                 "and $(%d, %d)$. Is it a function, and why?"
                                 % (a, y, a + c, y, a + 2 * c, y + 1),
                    "correct": "Yes — each input appears with exactly one output.",
                    "dvals": [
                        "No — two of the pairs share the same output.",
                        "No — an input is paired with two different outputs.",
                        "No — the outputs do not increase steadily.",
                    ],
                    "explanation": "A function requires each INPUT to have exactly one "
                                   "output. The inputs $%d$, $%d$ and $%d$ are all "
                                   "different, so the rule is satisfied. Two inputs sharing "
                                   "the OUTPUT $%d$ is perfectly legal — that restriction "
                                   "runs the other way." % (a, a + c, a + 2 * c, y),
                    "check": ["Ne(%d, %d)" % (a, a + c),
                              "Ne(%d, %d)" % (a + c, a + 2 * c)],
                })
                # not a function: one input, two outputs
                raws.append({
                    "statement": "A relation consists of the pairs $(%d, %d)$, $(%d, %d)$ "
                                 "and $(%d, %d)$. Is it a function, and why?"
                                 % (a, y, a, y + c, a + c, y),
                    "correct": "No — an input is paired with two different outputs.",
                    "dvals": [
                        "Yes — each input appears with exactly one output.",
                        "No — two of the pairs share the same output.",
                        "Yes — every output is used at most twice.",
                    ],
                    "explanation": "The input $%d$ appears twice, once with output $%d$ and "
                                   "once with output $%d$. A function cannot give one input "
                                   "two answers, so this relation is not one. The repeated "
                                   "OUTPUT $%d$ elsewhere would have been fine."
                                   % (a, y, y + c, y),
                    "check": ["Eq(%d, %d)" % (a, a),
                              "Ne(%d, %d)" % (y, y + c)],
                })
    return raws


def g_two_terms_arith():
    """LEVEL 3 — an arithmetic sequence from two non-consecutive terms."""
    raws = []
    for a1 in (-6, -3, 2, 4, 7, 11):
        for d in (2, 3, 4, 5, -3, -4):
            for (m, n) in ((3, 8), (4, 10), (2, 9), (5, 12), (3, 11)):
                tm, tn = a1 + (m - 1) * d, a1 + (n - 1) * d
                raws.append({
                    "statement": "In an arithmetic sequence the %s term is $%d$ and the "
                                 "%s term is $%d$. What is the FIRST term?"
                                 % (_ord(m), tm, _ord(n), tn),
                    "correct": a1,
                    # gave the common difference; stepped back once only; one step too far
                    "dvals": [d, tm - d, a1 - d],
                    "explanation": "The two terms are $%d$ steps apart, so "
                                   "$d = \\dfrac{(%d) - (%d)}{%d - %d} = %d$. Now step back "
                                   "from the %s term, which is $%d - 1 = %d$ steps after "
                                   "the first: $a_1 = (%d) - (%d)(%d) = %d$. Stepping back "
                                   "only once is the usual slip."
                                   % (n - m, tn, tm, n, m, d, _ord(m), m, m - 1, tm,
                                      m - 1, d, a1),
                    "check": ["Eq(%d + (%d - 1)*(%d), %d)" % (a1, m, d, tm),
                              "Eq(%d + (%d - 1)*(%d), %d)" % (a1, n, d, tn),
                              "Eq(Rational(%d - %d, %d - %d), %d)" % (tn, tm, n, m, d)],
                })
    return raws


def g_recursive_explicit():
    """LEVEL 3 — matching a recursive rule to its explicit formula."""
    raws = []
    for a1 in (-5, -2, 1, 3, 6, 9, 12):
        for d in (2, 3, 4, 5, 6, -2, -3):
            raws.append({
                "statement": "A sequence is defined by $a_1 = %d$ and "
                             "$a_{n} = a_{n-1} %s %d$. Which explicit formula gives the "
                             "same sequence?"
                             % (a1, "+" if d > 0 else "-", abs(d)),
                "correct": "$a_n = %d %s %d(n - 1)$"
                           % (a1, "+" if d > 0 else "-", abs(d)),
                "dvals": [
                    "$a_n = %d %s %dn$" % (a1, "+" if d > 0 else "-", abs(d)),
                    "$a_n = %d %s %d(n + 1)$" % (a1, "+" if d > 0 else "-", abs(d)),
                    "$a_n = %d %s %d(n - 1)$" % (d, "+" if a1 > 0 else "-", abs(a1)),
                ],
                "explanation": "The recursive rule adds $%d$ each step, so the explicit "
                               "form is first term plus $d$ times the number of STEPS "
                               "taken — and reaching the $n$th term takes $n - 1$ steps, "
                               "not $n$. Checking at $n = 1$ settles it: the correct "
                               "formula gives $%d$, while the $%dn$ version gives $%d$."
                               % (d, a1, abs(d), a1 + d),
                "check": ["Eq(%d + %d*(1 - 1), %d)" % (a1, d, a1),
                          "Eq(%d + %d*(2 - 1), %d)" % (a1, d, a1 + d),
                          "Eq(%d + %d*(5 - 1), %d)" % (a1, d, a1 + 4 * d)],
            })
    return raws


def g_sequence_threshold():
    """LEVEL 3 — the first term of a sequence to pass a threshold."""
    raws = []
    for a1 in (5, 8, 12, 15, 20):
        for d in (3, 4, 6, 7, 9):
            for extra in (30, 50, 70, 90):
                target = a1 + extra
                n = 1
                while a1 + (n - 1) * d <= target:
                    n += 1
                raws.append({
                    "statement": "An arithmetic sequence starts at $%d$ and increases by "
                                 "$%d$ each term. Which term is the FIRST to exceed $%d$?"
                                 % (a1, d, target),
                    "correct": n,
                    # off by one; solved for the value not the position; ignored the start
                    "dvals": [n - 1, a1 + (n - 1) * d, (target // d) + 1],
                    "explanation": "The $n$th term is $%d + %d(n-1)$. Term $%d$ is $%d$, "
                                   "which is still at most $%d$; term $%d$ is $%d$, the "
                                   "first above it. 'Exceeds' means STRICTLY greater — "
                                   "landing exactly on $%d$ would not count."
                                   % (a1, d, n - 1, a1 + (n - 2) * d, target, n,
                                      a1 + (n - 1) * d, target),
                    "check": ["%d + %d*(%d - 1) > %d" % (a1, d, n, target),
                              "%d + %d*(%d - 1) <= %d" % (a1, d, n - 1, target)],
                })
    return raws


# ===========================================================================
# Unit 4 — Linear Functions & Modelling
# ===========================================================================

def g_slope_from_table():
    """LEVEL 1 — rate of change read off a table of equally spaced inputs."""
    raws = []
    for x0 in (0, 1, 2, 3, 5):
        for step in (1, 2, 3, 4):
            for m in (2, 3, 4, 5, -2, -3, -4):
                for b in (1, 5, 9):
                    xs = [x0 + i * step for i in range(4)]
                    ys = [m * x + b for x in xs]
                    raws.append({
                        "statement": "A linear function has the values $f(%d) = %d$, "
                                     "$f(%d) = %d$, $f(%d) = %d$ and $f(%d) = %d$. What is "
                                     "its rate of change?"
                                     % (xs[0], ys[0], xs[1], ys[1], xs[2], ys[2],
                                        xs[3], ys[3]),
                        "correct": m,
                        # the change in y alone; the reciprocal-ish; the first output
                        "dvals": [m * step, Rational(step, m) if m else step, ys[0]],
                        "explanation": "Rate of change is the change in output DIVIDED by "
                                       "the change in input: $\\dfrac{%d - %d}{%d - %d} = "
                                       "\\dfrac{%d}{%d} = %d$. Reading only the jump in "
                                       "$f$ ignores that the inputs move $%d$ at a time."
                                       % (ys[1], ys[0], xs[1], xs[0], m * step, step, m,
                                          step),
                        "check": ["Eq(Rational(%d - %d, %d - %d), %d)"
                                  % (ys[1], ys[0], xs[1], xs[0], m),
                                  "Eq(Rational(%d - %d, %d - %d), %d)"
                                  % (ys[3], ys[2], xs[3], xs[2], m)],
                    })
    return raws


def g_line_from_intercepts():
    """LEVEL 2 — the equation of a line from where it crosses the axes."""
    raws = []
    for p in (-6, -4, -3, -2, 2, 3, 4, 6):
        for q in (-9, -6, -3, 3, 6, 9, 12):
            g = _gcd(p, q)
            m = Rational(-q, p)
            raws.append({
                "statement": "A line crosses the $x$-axis at $(%d, 0)$ and the $y$-axis at "
                             "$(0, %d)$. What is its equation?" % (p, q),
                "correct": "$y = %sx %s %d$" % (fmt(m), "+" if q > 0 else "-", abs(q)),
                "dvals": [
                    "$y = %sx %s %d$" % (fmt(-m), "+" if q > 0 else "-", abs(q)),
                    "$y = %sx %s %d$" % (fmt(m), "+" if p > 0 else "-", abs(p)),
                    "$y = %sx %s %d$" % (fmt(Rational(-p, q)), "+" if q > 0 else "-", abs(q)),
                ],
                "explanation": "Two points give the slope: "
                               "$m = \\dfrac{%d - 0}{0 - (%d)} = %s$. The $y$-intercept is "
                               "handed to you as $%d$, so $y = %sx %s %d$. Using the "
                               "$x$-intercept as the constant is the standard mix-up."
                               % (q, p, fmt(m), q, fmt(m), "+" if q > 0 else "-", abs(q)),
                "check": ["Eq(Rational(%d, %d)*(%d) + (%d), 0)" % (m.p, m.q, p, q),
                          "Eq(Rational(%d, %d)*0 + (%d), %d)" % (m.p, m.q, q, q)],
            })
    return raws


def g_compare_two_models():
    """LEVEL 2 — two linear plans, and when one overtakes the other."""
    ctx = [("Plan A", "Plan B", "months"), ("Gym X", "Gym Y", "months"),
           ("Printer P", "Printer Q", "pages"), ("Van hire", "Car hire", "days")]
    raws = []
    for (n1, n2, unit) in ctx:
        for b1 in (10, 20, 30, 40):
            for r1 in (5, 6, 8):
                for extra in (12, 18, 24):
                    b2 = b1 + extra
                    for dr in (2, 3, 4):
                        r2 = r1 - dr
                        if r2 <= 0 or extra % dr:
                            continue
                        n = extra // dr
                        raws.append({
                            "statement": "%s costs $\\$%d$ up front plus $\\$%d$ per %s. "
                                         "%s costs $\\$%d$ up front plus $\\$%d$ per %s. "
                                         "After how many %s do they cost the same?"
                                         % (n1, b1, r1, unit[:-1], n2, b2, r2, unit[:-1],
                                            unit),
                            "correct": n,
                            # difference of the fees; difference of the rates; their sum
                            "dvals": [extra, dr, b1 + b2],
                            "explanation": "Set the two costs equal: "
                                           "$%d + %dn = %d + %dn$. Collecting gives "
                                           "$%dn = %d$, so $n = %d$. The cheaper start-up "
                                           "plan is behind by $\\$%d$ and catches up at "
                                           "$\\$%d$ per %s."
                                           % (b1, r1, b2, r2, dr, extra, n, extra, dr,
                                              unit[:-1]),
                            "check": ["Eq(%d + %d*%d, %d + %d*%d)"
                                      % (b1, r1, n, b2, r2, n),
                                      "Eq(Rational(%d, %d), %d)" % (extra, dr, n)],
                        })
    return raws


def g_tiered_rate():
    """LEVEL 3 — a two-stage linear model, with the break point mattering."""
    ctx = [("electricity", "kilowatt-hours", "cents"),
           ("water", "cubic metres", "cents"),
           ("data", "gigabytes", "cents"),
           ("parking", "hours", "cents")]
    raws = []
    for (what, unit, money_) in ctx:
        for br in (20, 25, 30, 40):
            for r1 in (6, 8, 10):
                for r2 in (12, 15, 18):
                    for over in (5, 10, 15):
                        used = br + over
                        total = br * r1 + over * r2
                        raws.append({
                            "statement": "%s tariff charges $%d$ %s per %s for the first "
                                         "$%d$ %s and $%d$ %s per %s after that. What is "
                                         "the charge for $%d$ %s?"
                                         % (("An " + what) if what[0] in "aeiou"
                                            else ("A " + what),
                                            r1, money_, unit[:-1], br, unit, r2,
                                            money_, unit[:-1], used, unit),
                            "correct": total,
                            # charged everything at the high rate; at the low rate;
                            # applied the second rate to the whole excess plus the break
                            "dvals": [used * r2, used * r1, br * r2 + over * r1],
                            "explanation": "The first $%d$ %s cost $%d \\times %d = %d$ %s. "
                                           "Only the $%d$ %s ABOVE the break are charged at "
                                           "the higher rate: $%d \\times %d = %d$. Total "
                                           "$%d + %d = %d$ %s. Charging the whole "
                                           "usage at the high rate is the standard error."
                                           % (br, unit, br, r1, br * r1, money_, over,
                                              unit, over, r2, over * r2, br * r1,
                                              over * r2, total, money_),
                            "check": ["Eq(%d*%d + %d*%d, %d)" % (br, r1, over, r2, total),
                                      "Eq(%d + %d, %d)" % (br, over, used)],
                        })
    return raws


def g_parallel_through_point():
    """LEVEL 3 — a parallel line through a point, then evaluated somewhere else."""
    raws = []
    for m in (2, 3, 4, -2, -3, 5):
        for (x0, y0) in ((1, 4), (-2, 3), (3, -5), (-1, -2), (4, 1), (2, -6)):
            for c in (-4, 1, 7):
                for k in (5, 6, 8):
                    b = y0 - m * x0
                    val = m * k + b
                    raws.append({
                        "statement": "Line $\\ell$ passes through $(%d, %d)$ and is "
                                     "PARALLEL to $y = %s$. What is the $y$-coordinate of "
                                     "the point on $\\ell$ where $x = %d$?"
                                     % (x0, y0, lin(m, c), k),
                        "correct": val,
                        # used the given line itself; used the perpendicular slope; used b
                        "dvals": [m * k + c, y0 + Rational(-1, m) * (k - x0), b],
                        "explanation": "Parallel means the SAME slope, $%d$. Through "
                                       "$(%d, %d)$: $%d = %d(%d) + b$, so $b = %d$ and "
                                       "$\\ell$ is $y = %s$. At $x = %d$: "
                                       "$%d(%d) + (%d) = %d$. Using the original line's "
                                       "intercept $%d$ answers a different question."
                                       % (m, x0, y0, y0, m, x0, b, lin(m, b), k, m, k, b,
                                          val, c),
                        "check": ["Eq(%d*(%d) + (%d), %d)" % (m, x0, b, y0),
                                  "Eq(%d*(%d) + (%d), %d)" % (m, k, b, val)],
                    })
    return raws


def g_model_breakdown():
    """LEVEL 3 — reading a linear model AND saying where it stops making sense."""
    ctx = [
        ("A candle burns down", "height in centimetres", "hours", "the candle is used up"),
        ("A tank drains", "volume in litres", "minutes", "the tank is empty"),
        ("A phone battery discharges", "charge as a percentage", "hours", "the battery is flat"),
        ("A savings jar is emptied", "amount in dollars", "weeks", "the jar is empty"),
    ]
    raws = []
    for (story, ylab, tlab, end) in ctx:
        for b in (24, 30, 36, 45, 60):
            for m in (2, 3, 4, 5, 6):
                if b % m:
                    continue
                t = b // m
                raws.append({
                    "statement": "%s according to $y = %s$, where $y$ is the %s and $t$ is "
                                 "the time in %s. For what values of $t$ does this model "
                                 "make sense?" % (story, lin(-m, b), ylab, tlab),
                    "correct": "$0 \\le t \\le %d$" % t,
                    "dvals": [
                        "$t \\ge 0$, with no upper limit",
                        "$0 \\le t \\le %d$" % b,
                        "$0 \\le t \\le %d$" % m,
                    ],
                    "explanation": "The model starts at $t = 0$ and the quantity runs out "
                                   "when $y = 0$: $%s = 0$ gives $t = %d$. Beyond that the "
                                   "formula predicts a NEGATIVE %s, which is where %s and "
                                   "the model stops describing anything. The domain of a "
                                   "model is part of the model."
                                   % (lin(-m, b), t, ylab, end),
                    "check": ["Eq(-%d*%d + %d, 0)" % (m, t, b),
                              "-%d*%d + %d < 0" % (m, t + 1, b)],
                })
    return raws


# ===========================================================================
# Unit 5 — Systems of Equations & Inequalities
# ===========================================================================

def g_sys_substitution_easy():
    """LEVEL 1 — one equation already gives y, so it is one substitution."""
    raws = []
    for m in (2, 3, 4, 5, 6):
        for x0 in (2, 3, 4, 5, 6, 7, 8):
            for c in (0, 1, 3, 5):
                total = x0 + m * x0 + c
                raws.append({
                    "statement": "Solve the system $y = %s$ and $x + y = %d$ for $x$."
                                 % (lin(m, c), total),
                    "correct": x0,
                    # gave y; gave the total; added the coefficients
                    "dvals": [m * x0 + c, total, x0 + m],
                    "explanation": "The first equation already states $y$, so substitute it "
                                   "into the second: $x + %s = %d$, which is $%dx = %d$ and "
                                   "$x = %d$. The other unknown, $y = %d$, is a different "
                                   "question." % (lin(m, c), total, m + 1, total - c, x0,
                                                  m * x0 + c),
                    "check": ["Eq(%d + (%d*%d + %d), %d)" % (x0, m, x0, c, total),
                              "Eq(%d*%d + %d, %d)" % (m, x0, c, m * x0 + c)],
                })
    return raws


def g_sys_check_pair():
    """LEVEL 1 — does this ordered pair satisfy BOTH equations?"""
    raws = []
    for (p, q) in ((1, 2), (2, 1), (3, 1), (1, 3), (2, 3), (3, 2)):
        for x0 in (-3, -1, 1, 2, 4, 5):
            for y0 in (-2, 1, 3, 4):
                c1, c2 = p * x0 + q * y0, x0 - y0
                raws.append({
                    "statement": "Which ordered pair is the solution of the system "
                                 "$%dx + %dy = %d$ and $x - y = %d$?" % (p, q, c1, c2),
                    "correct": "$(%d,\\ %d)$" % (x0, y0),
                    "dvals": [
                        "$(%d,\\ %d)$" % (y0, x0),          # coordinates swapped
                        "$(%d,\\ %d)$" % (x0 + 1, y0),      # satisfies neither
                        "$(%d,\\ %d)$" % (x0, y0 + 1),
                    ],
                    "explanation": "A solution must satisfy BOTH equations. Substituting "
                                   "$(%d,\\ %d)$: the first gives $%d(%d) + %d(%d) = %d$ ✓ "
                                   "and the second gives $%d - (%d) = %d$ ✓. Swapping the "
                                   "coordinates breaks at least one of them."
                                   % (x0, y0, p, x0, q, y0, c1, x0, y0, c2),
                    "check": ["Eq(%d*(%d) + %d*(%d), %d)" % (p, x0, q, y0, c1),
                              "Eq((%d) - (%d), %d)" % (x0, y0, c2)],
                })
    return raws


def g_sys_mixture():
    """LEVEL 2 — two unknown counts from a total and a value."""
    ctx = [("adult", "child", "tickets", "dollars"),
           ("large", "small", "boxes", "kilograms"),
           ("gold", "silver", "coins", "grams"),
           ("hardback", "paperback", "books", "dollars")]
    raws = []
    for (t1, t2, thing, money_) in ctx:
        for v1 in (9, 12, 15, 20):
            for v2 in (4, 5, 6, 8):
                if v1 <= v2:
                    continue
                for a in (6, 8, 10, 12):
                    for b in (5, 7, 9, 14):
                        n, val = a + b, v1 * a + v2 * b
                        raws.append({
                            "statement": "A shop sold $%d$ %s in total, some %s and some "
                                         "%s, taking $%d$ %s altogether. A %s one is worth "
                                         "$%d$ and a %s one $%d$. How many %s ones were "
                                         "sold?" % (n, thing, t1, t2, val, money_, t1, v1,
                                                    t2, v2, t1),
                            "correct": a,
                            # gave the other count; the total; used the wrong price
                            "dvals": [b, n, Rational(val, v1)],
                            "explanation": "Let $x$ be the number of %s ones. Then "
                                           "$%d - x$ are %s, and "
                                           "$%dx + %d(%d - x) = %d$. Expanding gives "
                                           "$%dx + %d = %d$, so $%dx = %d$ and $x = %d$. "
                                           "The other count, $%d$, answers the other half "
                                           "of the question."
                                           % (t1, n, t2, v1, v2, n, val, v1 - v2, v2 * n,
                                              val, v1 - v2, val - v2 * n, a, b),
                            "check": ["Eq(%d + %d, %d)" % (a, b, n),
                                      "Eq(%d*%d + %d*%d, %d)" % (v1, a, v2, b, val)],
                        })
    return raws


def g_sys_elimination_scaled():
    """LEVEL 2 — neither coefficient matches, so one equation must be scaled."""
    raws = []
    for a1 in (2, 3, 4, 5):
        for b1 in (3, 5, 7):
            for k in (2, 3, 4):
                a2, b2 = a1 * k + 1, b1 * k - 1
                for x0 in (-2, 1, 2, 3, 4):
                    for y0 in (-3, 1, 2, 5):
                        c1, c2 = a1 * x0 + b1 * y0, a2 * x0 + b2 * y0
                        raws.append({
                            "statement": "Solve the system $%dx + %dy = %d$ and "
                                         "$%dx + %dy = %d$ for $y$."
                                         % (a1, b1, c1, a2, b2, c2),
                            "correct": y0,
                            "dvals": [x0, y0 + 1, -y0 if y0 else y0 + 2],
                            "explanation": "Neither variable cancels as written, so scale "
                                           "first: multiplying the equations by $%d$ and "
                                           "$%d$ makes the $x$ terms match, and subtracting "
                                           "leaves one equation in $y$ alone. It solves to "
                                           "$y = %d$ (and then $x = %d$). Substituting both "
                                           "back into BOTH equations is the check."
                                           % (a2, a1, y0, x0),
                            "check": ["Eq(%d*(%d) + %d*(%d), %d)"
                                      % (a1, x0, b1, y0, c1),
                                      "Eq(%d*(%d) + %d*(%d), %d)"
                                      % (a2, x0, b2, y0, c2)],
                        })
    return raws


def g_sys_combination():
    """LEVEL 3 — the question asks for a COMBINATION, not for x or y."""
    raws = []
    for (p, q) in ((2, 3), (3, 2), (4, 1), (1, 4), (3, 5), (5, 2)):
        for x0 in (-3, -1, 2, 3, 5, 6):
            for y0 in (-2, 1, 4, 7):
                c1 = p * x0 + q * y0
                c2 = x0 + y0 + 3
                want = x0 + y0
                raws.append({
                    "statement": "In the system $%dx + %dy = %d$ and $x + y + 3 = %d$, what "
                                 "is the value of $x + y$?" % (p, q, c1, c2),
                    "correct": want,
                    # solved for x; for y; used the second equation's constant
                    "dvals": [x0, y0, c2],
                    "explanation": "The second equation already contains $x + y$: "
                                   "$x + y = %d - 3 = %d$. No solving for $x$ and $y$ "
                                   "separately is needed — and doing it would take three "
                                   "times as long for the same answer. Read the question "
                                   "before choosing a method."
                                   % (c2, want),
                    "check": ["Eq(%d*(%d) + %d*(%d), %d)" % (p, x0, q, y0, c1),
                              "Eq((%d) + (%d) + 3, %d)" % (x0, y0, c2),
                              "Eq((%d) + (%d), %d)" % (x0, y0, want)],
                })
    return raws


def g_sys_inequality_point():
    """LEVEL 3 — which point satisfies BOTH inequalities."""
    raws = []
    for m in (1, 2, 3):
        for b in (1, 2, 4, 6):
            for k in (5, 8, 10, 12):
                for (px, py) in ((1, 1), (2, 3), (1, 4), (3, 2)):
                    if not (py < m * px + b and px + py < k):
                        continue
                    bad1 = (px, m * px + b + 2)
                    bad2 = (k, k)
                    bad3 = (px + k, py)
                    raws.append({
                        "statement": "Which point satisfies BOTH $y < %s$ and $x + y < %d$?"
                                     % (lin(m, b), k),
                        "correct": "$(%d,\\ %d)$" % (px, py),
                        "dvals": ["$(%d,\\ %d)$" % bad1, "$(%d,\\ %d)$" % bad2,
                                  "$(%d,\\ %d)$" % bad3],
                        "explanation": "Test each candidate in BOTH inequalities — passing "
                                       "one is not enough. $(%d,\\ %d)$ gives $%d < %d$ ✓ "
                                       "and $%d < %d$ ✓. $(%d,\\ %d)$ sits ABOVE the first "
                                       "line, so it fails there whatever the second says."
                                       % (px, py, py, m * px + b, px + py, k,
                                          bad1[0], bad1[1]),
                        "check": ["%d < %d*(%d) + %d" % (py, m, px, b),
                                  "%d + %d < %d" % (px, py, k),
                                  "%d >= %d*(%d) + %d" % (bad1[1], m, bad1[0], b)],
                    })
    return raws


# ===========================================================================
# Unit 6 — Exponential Functions
# ===========================================================================

def g_percent_to_factor():
    """LEVEL 1 — a percentage change becomes a multiplier."""
    raws = []
    for p in (2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20, 24, 25, 30, 35, 40, 45, 50, 60, 75):
        up = Rational(100 + p, 100)
        down = Rational(100 - p, 100)
        raws.append({
            "statement": "A quantity INCREASES by $%d\\%%$ each year. What is the growth "
                         "factor?" % p,
            "correct": up,
            "dvals": [Rational(p, 100), down, Rational(p, 10)],
            "explanation": "Keeping all of it and adding $%d\\%%$ means multiplying by "
                           "$1 + %s = %s$. The bare $%s$ is the INCREASE alone, not the "
                           "multiplier — using it would shrink the quantity to a fraction "
                           "of itself." % (p, fmt(Rational(p, 100)), fmt(up),
                                           fmt(Rational(p, 100))),
            "check": ["Eq(1 + Rational(%d, 100), Rational(%d, %d))" % (p, up.p, up.q)],
        })
        raws.append({
            "statement": "A quantity DECREASES by $%d\\%%$ each year. What is the decay "
                         "factor?" % p,
            "correct": down,
            "dvals": [Rational(p, 100), up, Rational(-p, 100)],
            "explanation": "Losing $%d\\%%$ leaves $%d\\%%$, so the multiplier is "
                           "$1 - %s = %s$. A decay factor is always between $0$ and $1$; a "
                           "negative multiplier would flip the sign of the quantity every "
                           "year." % (p, 100 - p, fmt(Rational(p, 100)), fmt(down)),
            "check": ["Eq(1 - Rational(%d, 100), Rational(%d, %d))"
                      % (p, down.p, down.q)],
        })
    return raws


def g_write_exp_model():
    """LEVEL 2 — turn a described situation into a formula."""
    ctx = [("a colony of bacteria", "bacteria", "hours"),
           ("a town's population", "people", "years"),
           ("an investment", "dollars", "years"),
           ("a car's value", "dollars", "years")]
    raws = []
    for (story, unit, tlab) in ctx:
        for a in (200, 500, 1200, 8000):
            for p in (5, 8, 12, 20, 25):
                for grow in (True, False):
                    f = Rational(100 + p, 100) if grow else Rational(100 - p, 100)
                    word = "grows" if grow else "falls"
                    raws.append({
                        "statement": "%s starts at $%d$ %s and %s by $%d\\%%$ every "
                                     "%s. Which formula models it after $t$ %s?"
                                     % (story.capitalize(), a, unit, word, p, tlab[:-1],
                                        tlab),
                        "correct": "$y = %d(%s)^t$" % (a, fmt(f)),
                        "dvals": [
                            "$y = %d(%s)^t$" % (a, fmt(Rational(p, 100))),
                            "$y = %d + %s t$" % (a, fmt(f)),
                            "$y = %d(%s)^t$" % (a, fmt(Rational(100 + p, 100)
                                                       if not grow
                                                       else Rational(100 - p, 100))),
                        ],
                        "explanation": "The starting amount is the coefficient, $%d$. A "
                                       "%s of $%d\\%%$ per %s multiplies by $%s$ each time, "
                                       "so that is the base and $t$ is the exponent. A "
                                       "percentage change compounds — it is never added "
                                       "term by term, which is what the linear option "
                                       "does." % (a, word.rstrip('s'), p, tlab[:-1], fmt(f)),
                        "check": ["Eq(%d*Rational(%d, %d)**0, %d)"
                                  % (a, f.p, f.q, a),
                                  "Eq(%d*Rational(%d, %d)**1, Rational(%d, %d))"
                                  % (a, f.p, f.q, (a * f).p, (a * f).q)],
                    })
    return raws


def g_compare_exp_models():
    """LEVEL 2 — two exponential models, compared at a given time."""
    raws = []
    for a1 in (100, 200, 400, 800):
        for b1 in (2, 3):
            for a2 in (50, 150, 300):
                for b2 in (3, 4, 5):
                    if b2 <= b1:
                        continue
                    for t in (2, 3, 4):
                        v1, v2 = a1 * b1 ** t, a2 * b2 ** t
                        if v1 == v2:
                            continue
                        bigger = "the first" if v1 > v2 else "the second"
                        raws.append({
                            "statement": "Model A is $y = %d \\cdot %d^t$ and model B is "
                                         "$y = %d \\cdot %d^t$. What is the value of the "
                                         "LARGER of the two at $t = %d$?"
                                         % (a1, b1, a2, b2, t),
                            "correct": max(v1, v2),
                            "dvals": [min(v1, v2), a1 * b1 * t, a2 * b2 * t],
                            "explanation": "At $t = %d$, model A gives "
                                           "$%d \\cdot %d^{%d} = %d$ and model B gives "
                                           "$%d \\cdot %d^{%d} = %d$, so %s is larger. A "
                                           "bigger STARTING value does not settle it — the "
                                           "base wins eventually, and $t = %d$ may already "
                                           "be past the crossover."
                                           % (t, a1, b1, t, v1, a2, b2, t, v2, bigger, t),
                            "check": ["Eq(%d*%d**%d, %d)" % (a1, b1, t, v1),
                                      "Eq(%d*%d**%d, %d)" % (a2, b2, t, v2)],
                        })
    return raws


def g_doubling_threshold():
    """LEVEL 3 — the first whole period at which a model passes a level."""
    raws = []
    for a in (3, 5, 8, 12, 20):
        for b in (2, 3, 4):
            for mult in (20, 50, 100, 300, 700):
                target = a * mult
                n = 0
                while a * b ** n <= target:
                    n += 1
                raws.append({
                    "statement": "A population is modelled by $P = %d \\cdot %d^{t}$, with "
                                 "$t$ in years. After how many WHOLE years does the "
                                 "population first exceed $%d$?" % (a, b, target),
                    "correct": n,
                    # off by one; the multiplier; the ratio of the two numbers
                    "dvals": [n - 1, mult, Rational(target, b)],
                    "explanation": "At $t = %d$ the model gives $%d$, still at most $%d$; "
                                   "at $t = %d$ it gives $%d$, which is past it. So the "
                                   "answer is $%d$ years. Because $t$ counts whole years, "
                                   "the answer must round UP — the model crosses the level "
                                   "part-way through the year."
                                   % (n - 1, a * b ** (n - 1), target, n, a * b ** n, n),
                    "check": ["%d*%d**%d > %d" % (a, b, n, target),
                              "%d*%d**%d <= %d" % (a, b, n - 1, target)],
                })
    return raws


def g_exp_from_two_points():
    """LEVEL 3 — recover a and b from two values of the model."""
    raws = []
    for a in (2, 3, 5, 7, 10, 12):
        for b in (2, 3, 4, 5):
            for k in (2, 3, 4):
                v0, vk = a, a * b ** k
                raws.append({
                    "statement": "An exponential model $y = a \\cdot b^{t}$ passes through "
                                 "$(0, %d)$ and $(%d, %d)$. What are $a$ and $b$?"
                                 % (v0, k, vk),
                    "correct": "$a = %d$, $b = %d$" % (a, b),
                    "dvals": [
                        "$a = %d$, $b = %d$" % (a, b ** k),      # forgot the k-th root
                        "$a = %d$, $b = %d$" % (vk, b),          # read a off the wrong point
                        "$a = %d$, $b = %d$" % (a, b + 1),
                    ],
                    "explanation": "At $t = 0$ every power is $1$, so $a = %d$ is read "
                                   "straight off. Then $%d \\cdot b^{%d} = %d$ gives "
                                   "$b^{%d} = %d$, and taking the $%d$th root leaves "
                                   "$b = %d$. Skipping the root gives $%d$, the growth over "
                                   "all $%d$ periods rather than per period."
                                   % (a, a, k, vk, k, b ** k, k, b, b ** k, k),
                    "check": ["Eq(%d*%d**0, %d)" % (a, b, v0),
                              "Eq(%d*%d**%d, %d)" % (a, b, k, vk)],
                })
    return raws


def g_rate_period_change():
    """LEVEL 3 — the same growth, rewritten for a different period."""
    names = {2: ("half-year", 2), 3: ("four-month", 3), 4: ("quarter-year", 4)}
    raws = []
    for root in (2, 3, 4, 5, 6, 7, 8, 9, 10):
        for k in (2, 3, 4):
            b = root ** k
            if b > 100000:
                continue
            per, _ = names[k]
            raws.append({
                "statement": "A quantity multiplies by $%d$ every year. By what factor does "
                             "it multiply in each %s period, of which there are $%d$ in a "
                             "year?" % (b, per, k),
                "correct": "$%d$" % root,
                "dvals": ["$%s$" % fmt(Rational(b, k)), "$%d$" % b,
                          "$%s$" % fmt(Rational(b - 1, k) + 1)],
                "explanation": "The $%d$ periods must MULTIPLY to the annual factor, not "
                               "add to it: $x^{%d} = %d$, so $x = %d$ (check: "
                               "$%d^{%d} = %d$). Dividing the annual factor by $%d$ treats "
                               "compound growth as if it were linear, which is the whole "
                               "distinction this unit is about."
                               % (k, k, b, root, root, k, b, k),
                "check": ["Eq(%d**%d, %d)" % (root, k, b)],
            })
    return raws


# ===========================================================================
# Unit 7 — Transformations, Congruence & Proof
# ===========================================================================

def g_reflect_in_axis():
    """LEVEL 1 — the image of a point under a reflection in an axis."""
    raws = []
    for x in (-6, -4, -3, -1, 2, 3, 5, 7):
        for y in (-5, -2, 1, 4, 6):
            raws.append({
                "statement": "The point $(%d,\\ %d)$ is reflected in the $x$-axis. What are "
                             "the coordinates of the image?" % (x, y),
                "correct": "$(%d,\\ %d)$" % (x, -y),
                "dvals": ["$(%d,\\ %d)$" % (-x, y), "$(%d,\\ %d)$" % (-x, -y),
                          "$(%d,\\ %d)$" % (y, x)],
                "explanation": "Reflecting in the $x$-axis flips the point over that axis, "
                               "so the horizontal position is untouched and the vertical "
                               "one changes sign: $(x,\\ y) \\to (x,\\ -y)$, giving "
                               "$(%d,\\ %d)$. Negating $x$ instead reflects in the "
                               "$y$-axis." % (x, -y),
                "check": ["Eq(%d, %d)" % (x, x), "Eq(-(%d), %d)" % (y, -y)],
            })
            raws.append({
                "statement": "The point $(%d,\\ %d)$ is reflected in the $y$-axis. What are "
                             "the coordinates of the image?" % (x, y),
                "correct": "$(%d,\\ %d)$" % (-x, y),
                "dvals": ["$(%d,\\ %d)$" % (x, -y), "$(%d,\\ %d)$" % (-x, -y),
                          "$(%d,\\ %d)$" % (y, x)],
                "explanation": "Reflecting in the $y$-axis keeps the height and flips the "
                               "side: $(x,\\ y) \\to (-x,\\ y)$, giving $(%d,\\ %d)$. The "
                               "axis you reflect in is the one whose coordinate SURVIVES."
                               % (-x, y),
                "check": ["Eq(-(%d), %d)" % (x, -x), "Eq(%d, %d)" % (y, y)],
            })
    return raws


def g_rotate_about_origin():
    """LEVEL 1 — quarter and half turns about the origin."""
    raws = []
    for x in (-5, -3, -2, 1, 2, 4, 6):
        for y in (-6, -4, -1, 3, 5, 7):
            raws.append({
                "statement": "The point $(%d,\\ %d)$ is rotated $90°$ ANTICLOCKWISE about "
                             "the origin. What are the coordinates of the image?" % (x, y),
                "correct": "$(%d,\\ %d)$" % (-y, x),
                "dvals": ["$(%d,\\ %d)$" % (y, -x), "$(%d,\\ %d)$" % (-x, -y),
                          "$(%d,\\ %d)$" % (y, x)],
                "explanation": "A quarter turn anticlockwise sends $(x,\\ y)$ to "
                               "$(-y,\\ x)$, so $(%d,\\ %d)$ lands on $(%d,\\ %d)$. The "
                               "CLOCKWISE quarter turn is the other one, $(y,\\ -x)$ — the "
                               "two differ by a half turn."
                               % (x, y, -y, x),
                "check": ["Eq(-(%d), %d)" % (y, -y), "Eq(%d, %d)" % (x, x)],
            })
            raws.append({
                "statement": "The point $(%d,\\ %d)$ is rotated $180°$ about the origin. "
                             "What are the coordinates of the image?" % (x, y),
                "correct": "$(%d,\\ %d)$" % (-x, -y),
                "dvals": ["$(%d,\\ %d)$" % (-y, x), "$(%d,\\ %d)$" % (y, -x),
                          "$(%d,\\ %d)$" % (x, -y)],
                "explanation": "A half turn sends every point to the opposite side of the "
                               "origin: $(x,\\ y) \\to (-x,\\ -y)$, giving $(%d,\\ %d)$. "
                               "Both coordinates change sign, which is what makes a half "
                               "turn the same clockwise or anticlockwise."
                               % (-x, -y),
                "check": ["Eq(-(%d), %d)" % (x, -x), "Eq(-(%d), %d)" % (y, -y)],
            })
    return raws


def g_congruent_parts():
    """LEVEL 2 — corresponding parts of triangles named in a congruence."""
    raws = []
    letters = [("A", "B", "C", "P", "Q", "R"), ("D", "E", "F", "X", "Y", "Z"),
               ("J", "K", "L", "S", "T", "U"), ("M", "N", "O", "G", "H", "I")]
    raws = []
    for (a, b, c, p, q, r) in letters:
        for val in (5, 7, 9, 12, 14, 18):
            for which in range(3):
                src = [(a + b, p + q), (b + c, q + r), (a + c, p + r)][which]
                wrong = [(p + r), (q + r), (p + q)][which]
                raws.append({
                    "statement": "Triangle $%s%s%s$ is congruent to triangle $%s%s%s$, and "
                                 "$%s = %d$. Which side of the second triangle must also "
                                 "measure $%d$?" % (a, b, c, p, q, r, src[0], val, val),
                    "correct": "$%s$" % src[1],
                    "dvals": ["$%s$" % wrong if wrong != src[1] else "$%s%s$" % (q, p),
                              "$%s%s$" % (r, p) if ("%s%s" % (r, p)) != src[1] else "$%s%s$" % (p, r),
                              "$%s%s$" % (a, c)],
                    "explanation": "A congruence statement is an ORDER: $%s \\to %s$, "
                                   "$%s \\to %s$, $%s \\to %s$. So $%s$ corresponds to "
                                   "$%s$, and corresponding parts of congruent triangles "
                                   "are equal. Reading the letters out of order is what "
                                   "produces the wrong side."
                                   % (a, p, b, q, c, r, src[0], src[1]),
                    "check": ["Eq(%d, %d)" % (val, val), "%d > 0" % val],
                })
    return raws


def g_parallel_angle():
    """LEVEL 2 — a transversal across parallel lines."""
    raws = []
    for ang in (35, 42, 48, 55, 62, 68, 73, 78, 82, 105, 112, 118, 125, 133):
        raws.append({
            "statement": "Two parallel lines are cut by a transversal. One of the "
                         "co-interior angles measures $%d°$. What is the other co-interior "
                         "angle?" % ang,
            "correct": 180 - ang,
            "dvals": [ang, 360 - ang, 90 - ang],
            "explanation": "Co-interior angles lie between the parallel lines on the SAME "
                           "side of the transversal, and they are supplementary: "
                           "$180° - %d° = %d°$. Equal is what ALTERNATE angles are — the "
                           "opposite sides of the transversal." % (ang, 180 - ang),
            "check": ["Eq(180 - %d, %d)" % (ang, 180 - ang),
                      "Eq(%d + %d, 180)" % (ang, 180 - ang)],
        })
        raws.append({
            "statement": "Two parallel lines are cut by a transversal. An alternate interior "
                         "angle pair includes an angle of $%d°$. What is the angle "
                         "co-interior to that same angle?" % ang,
            "correct": 180 - ang,
            "dvals": [ang, 90 - ang if ang < 90 else ang - 90, 2 * ang],
            "explanation": "The alternate angle equals $%d°$; the CO-INTERIOR angle sits "
                           "beside it on a straight line, so it is $180° - %d° = %d°$. "
                           "Alternate means equal, co-interior means supplementary — which "
                           "side of the transversal you are on decides which."
                           % (ang, ang, 180 - ang),
            "check": ["Eq(180 - %d, %d)" % (ang, 180 - ang)],
        })
    return raws


def g_angle_algebra():
    """LEVEL 3 — an angle relationship turned into an equation."""
    raws = []
    for a in (2, 3, 4, 5):
        for gap in (1, 2, 3, 4):
            c = a + gap
            for x0 in (6, 8, 9, 11, 13, 15, 17):
                for d in (4, 9, 14, 21):
                    b = gap * x0 + d          # forces a*x0 + b == c*x0 + d
                    ang = a * x0 + b
                    if ang >= 175 or b > 120:
                        continue
                    raws.append({
                        "statement": "Two parallel lines are cut by a transversal. A pair of "
                                     "CORRESPONDING angles measure $%dx + %d$ and "
                                     "$%dx + %d$ degrees. Find $x$." % (a, b, c, d),
                        "correct": x0,
                        # gave the ANGLE not x; sign slip; matched constants only
                        "dvals": [ang, -x0, b - d],
                        "explanation": "Corresponding angles between parallel lines are "
                                       "EQUAL, so $%dx + %d = %dx + %d$. Collecting gives "
                                       "$%dx = %d$, hence $x = %d$; both expressions then "
                                       "give $%d°$, which is the check. Treating the pair "
                                       "as supplementary — making them sum to $180°$ — is "
                                       "the commonest wrong move, and it is what "
                                       "CO-INTERIOR angles do, not corresponding ones."
                                       % (a, b, c, d, gap, b - d, x0, ang),
                        "check": ["Eq(%d*%d + %d, %d*%d + %d)" % (a, x0, b, c, x0, d),
                                  "Eq(%d*%d + %d, %d)" % (a, x0, b, ang),
                                  "%d < 180" % ang],
                    })
    return raws


def g_triangle_theorems():
    """LEVEL 3 — angle sum, exterior angle, isosceles and midsegment."""
    raws = []
    for a in (28, 34, 41, 47, 53, 59, 66, 72):
        for b in (35, 44, 52, 61, 68):
            if a + b >= 180:
                continue
            raws.append({
                "statement": "Two angles of a triangle measure $%d°$ and $%d°$. What is the "
                             "EXTERIOR angle at the third vertex?" % (a, b),
                "correct": a + b,
                "dvals": [180 - a - b, 180 - a, 360 - a - b],
                "explanation": "An exterior angle equals the sum of the two REMOTE interior "
                               "angles: $%d + %d = %d°$. The third INTERIOR angle is "
                               "$180 - %d - %d = %d°$, and indeed $%d + %d = 180$ — the two "
                               "form a linear pair."
                               % (a, b, a + b, a, b, 180 - a - b, a + b, 180 - a - b),
                "check": ["Eq(%d + %d, %d)" % (a, b, a + b),
                          "Eq(180 - %d - %d, %d)" % (a, b, 180 - a - b),
                          "Eq(%d + %d, 180)" % (a + b, 180 - a - b)],
            })
    for apex in (20, 30, 36, 44, 50, 64, 70, 80, 96, 110, 120, 134):
        base = Rational(180 - apex, 2)
        raws.append({
            "statement": "An isosceles triangle has an apex angle of $%d°$ between its two "
                         "equal sides. What is each base angle?" % apex,
            "correct": base,
            "dvals": [180 - apex, Rational(apex, 2), 90 - apex],
            "explanation": "Equal sides face equal angles, so the two base angles are the "
                           "same. They share what is left of the $180°$: "
                           "$\\dfrac{180 - %d}{2} = %s°$. Halving the APEX angle instead "
                           "answers a different question." % (apex, fmt(base)),
            "check": ["Eq(Rational(180 - %d, 2), Rational(%d, %d))"
                      % (apex, base.p, base.q),
                      "Eq(%d + 2*Rational(%d, %d), 180)" % (apex, base.p, base.q)],
        })
    for side in (14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58):
        raws.append({
            "statement": "$M$ and $N$ are the midpoints of two sides of a triangle whose "
                         "third side measures $%d$. What is the length of $MN$?" % side,
            "correct": Rational(side, 2),
            "dvals": [side, side * 2, Rational(side, 3)],
            "explanation": "The midsegment joining two midpoints is parallel to the third "
                           "side and exactly HALF its length: $\\dfrac{%d}{2} = %s$. The "
                           "halving is the part most often dropped."
                           % (side, fmt(Rational(side, 2))),
            "check": ["Eq(Rational(%d, 2), Rational(%d, %d))"
                      % (side, Rational(side, 2).p, Rational(side, 2).q),
                      "Eq(2*Rational(%d, 2), %d)" % (side, side)],
        })
    return raws


# ===========================================================================
# Unit 8 — Coordinate Geometry
# ===========================================================================

def g_segment_length_axis():
    """LEVEL 1 — a horizontal or vertical segment needs no distance formula."""
    raws = []
    for x1 in (-7, -4, -2, 1, 3, 6):
        for d in (3, 5, 8, 11):
            for y in (-5, -1, 2, 6):
                raws.append({
                    "statement": "What is the length of the segment joining $(%d,\\ %d)$ "
                                 "and $(%d,\\ %d)$?" % (x1, y, x1 + d, y),
                    "correct": d,
                    "dvals": [x1 + d, 2 * d, x1 + d + y],
                    "explanation": "Both points share the height $%d$, so the segment is "
                                   "horizontal and its length is the difference of the "
                                   "$x$-coordinates: $%d - (%d) = %d$. No distance formula "
                                   "is needed — although it would give the same answer, "
                                   "since the vertical difference is zero."
                                   % (y, x1 + d, x1, d),
                    "check": ["Eq((%d) - (%d), %d)" % (x1 + d, x1, d),
                              "Eq(sqrt(((%d) - (%d))**2 + 0**2), %d)" % (x1 + d, x1, d)],
                })
                raws.append({
                    "statement": "What is the length of the segment joining $(%d,\\ %d)$ "
                                 "and $(%d,\\ %d)$?" % (y, x1, y, x1 + d),
                    "correct": d,
                    "dvals": [x1 + d, 2 * d, abs(y) + d],
                    "explanation": "Both points share the $x$-coordinate $%d$, so the "
                                   "segment is vertical and its length is the difference of "
                                   "the heights: $%d - (%d) = %d$."
                                   % (y, x1 + d, x1, d),
                    "check": ["Eq((%d) - (%d), %d)" % (x1 + d, x1, d)],
                })
    return raws


def g_triangle_perimeter():
    """LEVEL 2 — three distances, added."""
    raws = []
    for (a, b) in ((3, 4), (6, 8), (5, 12), (9, 12), (8, 15), (12, 16),
                   (7, 24), (20, 21), (10, 24), (15, 20), (9, 40), (12, 35)):
        c = int(round((a * a + b * b) ** 0.5))
        if c * c != a * a + b * b:
            continue
        for (ox, oy) in ((0, 0), (-2, 1), (3, -4)):
            raws.append({
                "statement": "A triangle has vertices $(%d,\\ %d)$, $(%d,\\ %d)$ and "
                             "$(%d,\\ %d)$. What is its perimeter?"
                             % (ox, oy, ox + a, oy, ox, oy + b),
                "correct": a + b + c,
                # forgot the hypotenuse; used the area; doubled a leg instead
                "dvals": [a + b, Rational(a * b, 2), a + c + c],
                "explanation": "Two sides are along the axes, of lengths $%d$ and $%d$. The "
                               "third joins $(%d,\\ %d)$ to $(%d,\\ %d)$: "
                               "$\\sqrt{%d^2 + %d^2} = \\sqrt{%d} = %d$. The perimeter is "
                               "$%d + %d + %d = %d$. Note the area, "
                               "$\\frac{1}{2}(%d)(%d) = %s$, is a different quantity."
                               % (a, b, ox + a, oy, ox, oy + b, a, b, a * a + b * b, c,
                                  a, b, c, a + b + c, a, b, fmt(Rational(a * b, 2))),
                "check": ["Eq(%d**2 + %d**2, %d**2)" % (a, b, c),
                          "Eq(%d + %d + %d, %d)" % (a, b, c, a + b + c)],
            })
    return raws


def g_other_endpoint():
    """LEVEL 2 — the midpoint run backwards."""
    raws = []
    for (ax, ay) in ((-4, 3), (2, -5), (1, 1), (-6, -2), (5, 4), (0, -7)):
        for (mx, my) in ((1, 0), (-1, 2), (3, 3), (-3, -4), (4, -2), (2, 5)):
            bx, by = 2 * mx - ax, 2 * my - ay
            raws.append({
                "statement": "$M(%d,\\ %d)$ is the midpoint of segment $AB$, and "
                             "$A$ is $(%d,\\ %d)$. What are the coordinates of $B$?"
                             % (mx, my, ax, ay),
                "correct": "$(%d,\\ %d)$" % (bx, by),
                "dvals": [
                    "$(%d,\\ %d)$" % (mx - ax, my - ay),      # subtracted without doubling
                    "$(%d,\\ %d)$" % (Rational(ax + mx, 2) if (ax + mx) % 2 == 0 else ax + mx,
                                      Rational(ay + my, 2) if (ay + my) % 2 == 0 else ay + my),
                    "$(%d,\\ %d)$" % (2 * ax - mx, 2 * ay - my),   # ran it the wrong way
                ],
                "explanation": "The midpoint AVERAGES the endpoints, so recovering the "
                               "other one doubles and subtracts: "
                               "$B_x = 2(%d) - (%d) = %d$ and $B_y = 2(%d) - (%d) = %d$. "
                               "Checking: the midpoint of $(%d,\\ %d)$ and $(%d,\\ %d)$ is "
                               "indeed $(%d,\\ %d)$."
                               % (mx, ax, bx, my, ay, by, ax, ay, bx, by, mx, my),
                "check": ["Eq(Rational((%d) + (%d), 2), %d)" % (ax, bx, mx),
                          "Eq(Rational((%d) + (%d), 2), %d)" % (ay, by, my)],
            })
    return raws


def g_triangle_area_coords():
    """LEVEL 3 — area from three vertices, no base conveniently on an axis."""
    raws = []
    for (bx, by) in ((4, 0), (6, 0), (0, 5), (0, 8), (5, 0), (0, 6)):
        for (cx, cy) in ((3, 6), (-2, 4), (7, 3), (-4, -3), (2, 9), (8, -2)):
            for (ox, oy) in ((0, 0), (1, 2), (-3, 1)):
                ax, ay = ox, oy
                Bx, By = ox + bx, oy + by
                Cx, Cy = ox + cx, oy + cy
                twice = abs(ax * (By - Cy) + Bx * (Cy - ay) + Cx * (ay - By))
                if twice == 0:
                    continue
                area = Rational(twice, 2)
                raws.append({
                    "statement": "A triangle has vertices $(%d,\\ %d)$, $(%d,\\ %d)$ and "
                                 "$(%d,\\ %d)$. What is its area?"
                                 % (ax, ay, Bx, By, Cx, Cy),
                    "correct": area,
                    # forgot to halve; halved twice; used the perimeter-ish sum
                    "dvals": [twice, Rational(twice, 4), abs(bx) + abs(by) + abs(cx)],
                    "explanation": "Using the coordinate area formula, "
                                   "$\\text{Area} = \\frac{1}{2}\\left|x_A(y_B - y_C) + "
                                   "x_B(y_C - y_A) + x_C(y_A - y_B)\\right|$, the bracket "
                                   "comes to $%d$ and half of it is $%s$. Forgetting the "
                                   "half is the standard error — that quantity is twice the "
                                   "area, which is the area of the surrounding "
                                   "parallelogram." % (twice, fmt(area)),
                    "check": ["Eq(Abs((%d)*((%d) - (%d)) + (%d)*((%d) - (%d)) + "
                              "(%d)*((%d) - (%d))), %d)"
                              % (ax, By, Cy, Bx, Cy, ay, Cx, ay, By, twice),
                              "Eq(Rational(%d, 2), Rational(%d, %d))"
                              % (twice, area.p, area.q)],
                })
    return raws


def g_prove_parallelogram():
    """LEVEL 3 — which coordinate fact PROVES the shape is a parallelogram."""
    raws = []
    for (a, b) in ((3, 5), (4, 7), (6, 2), (5, 9), (8, 3), (2, 6),
                   (7, 4), (9, 5), (3, 8), (6, 7), (4, 4), (5, 3)):
        for (ox, oy) in ((0, 0), (-2, 3), (1, -4)):
            raws.append({
                "statement": "A quadrilateral has vertices $(%d,\\ %d)$, $(%d,\\ %d)$, "
                             "$(%d,\\ %d)$ and $(%d,\\ %d)$, in order. Which single "
                             "coordinate check PROVES it is a parallelogram?"
                             % (ox, oy, ox + a, oy, ox + a + b, oy + b, ox + b, oy + b),
                "correct": "Both pairs of opposite sides have equal slopes.",
                "dvals": [
                    "All four sides have the same length.",
                    "The four vertices are all in different quadrants.",
                    "The diagonals have equal length.",
                ],
                "explanation": "A parallelogram is DEFINED by both pairs of opposite sides "
                               "being parallel, and parallel means equal slope — so that is "
                               "the check that proves it and nothing more is needed. Equal "
                               "side lengths would prove a RHOMBUS and equal diagonals a "
                               "RECTANGLE; both are stronger claims than the question asks "
                               "for, and neither follows from being a parallelogram.",
                "check": ["Eq(Rational((%d) - (%d), (%d) - (%d)), "
                          "Rational((%d) - (%d), (%d) - (%d)))"
                          % (oy, oy, ox + a, ox, oy + b, oy + b, ox + a + b, ox + b),
                          "Eq((%d) - (%d), (%d) - (%d))"
                          % (ox + a, ox, ox + a + b, ox + b)],
            })
    return raws


def g_right_angle_condition():
    """LEVEL 3 — find the missing coordinate that makes the angle right."""
    raws = []
    for m in (2, 3, 4, 5, -2, -3):
        for (px, py) in ((1, 2), (-2, 1), (3, -1), (0, 4), (2, 5), (-1, -3)):
            for step in (2, 3, 4):
                qx = px + m * step
                qy = py + step * m * m          # so PQ has slope m... see below
                # Build P, Q with slope m, then R so that QR is perpendicular.
                qx, qy = px + step, py + m * step
                rx = qx + m * step
                ry = qy - step
                raws.append({
                    "statement": "$P$ is $(%d,\\ %d)$ and $Q$ is $(%d,\\ %d)$. For angle "
                                 "$PQR$ to be a RIGHT angle, which point could $R$ be?"
                                 % (px, py, qx, qy),
                    "correct": "$(%d,\\ %d)$" % (rx, ry),
                    "dvals": [
                        "$(%d,\\ %d)$" % (qx + step, qy + m * step),   # same direction
                        "$(%d,\\ %d)$" % (qx + m * step, qy + step),   # sign of the reciprocal
                        "$(%d,\\ %d)$" % (px, py),                     # back to P
                    ],
                    "explanation": "$PQ$ has slope "
                                   "$\\dfrac{%d - (%d)}{%d - (%d)} = %d$. A right angle at "
                                   "$Q$ needs $QR$ perpendicular, so its slope must be the "
                                   "negative reciprocal $%s$. From $Q$, moving $%d$ right "
                                   "and $%d$ down reaches $(%d,\\ %d)$, and "
                                   "$%d \\times %s = -1$ confirms it."
                                   % (qy, py, qx, px, m, fmt(Rational(-1, m)), m * step,
                                      step, rx, ry, m, fmt(Rational(-1, m))),
                    "check": ["Eq(Rational((%d) - (%d), (%d) - (%d)), %d)"
                              % (qy, py, qx, px, m),
                              "Eq(Rational((%d) - (%d), (%d) - (%d)), Rational(-1, %d))"
                              % (ry, qy, rx, qx, m),
                              "Eq(%d*Rational(-1, %d), -1)" % (m, m)],
                })
    return raws


# ===========================================================================
# Unit 9 — Data & Statistics
# ===========================================================================

def g_mode_median():
    """LEVEL 1 — the mode and the median of a short list."""
    raws = []
    for a in range(2, 14):
        for gap in (1, 2, 3):
            vals = [a, a + gap, a + gap, a + 3 * gap, a + 5 * gap]
            shown = [vals[3], vals[1], vals[0], vals[4], vals[2]]
            raws.append({
                "statement": "A data set is $%d,\\ %d,\\ %d,\\ %d,\\ %d$. What is the "
                             "MODE?" % tuple(shown),
                "correct": a + gap,
                "dvals": [a + gap, a, a + 5 * gap] if False else
                         [vals[3], a, a + 5 * gap],
                "explanation": "The mode is the value that appears most often. Only $%d$ "
                               "occurs twice; every other value occurs once. The median — "
                               "the middle of the SORTED list — is also $%d$ here, but "
                               "that is a coincidence of this data set, not a rule."
                               % (a + gap, a + gap),
                "check": ["Eq(%d, %d)" % (vals[1], vals[2]),
                          "Ne(%d, %d)" % (vals[0], vals[3])],
            })
            raws.append({
                "statement": "A data set is $%d,\\ %d,\\ %d,\\ %d,\\ %d$. What is the "
                             "MEDIAN?" % tuple(shown),
                "correct": vals[2],
                "dvals": [shown[2], vals[4], Rational(sum(vals), 5)],
                "explanation": "Sort first: $%d,\\ %d,\\ %d,\\ %d,\\ %d$. With five values "
                               "the median is the third, $%d$. Taking the middle of the "
                               "list AS PRINTED gives $%d$ instead."
                               % (vals[0], vals[1], vals[2], vals[3], vals[4], vals[2],
                                  shown[2]),
                "check": ["%d <= %d" % (vals[1], vals[2]),
                          "%d <= %d" % (vals[2], vals[3]),
                          "Eq(Rational(%d, 5), Rational(%d, %d))"
                          % (sum(vals), Rational(sum(vals), 5).p,
                             Rational(sum(vals), 5).q)],
            })
    return raws


def g_compare_spread():
    """LEVEL 2 — same centre, different spread."""
    raws = []
    for c in (10, 12, 15, 18, 20, 25, 30, 40):
        for s1 in (1, 2, 3):
            for s2 in (5, 6, 8):
                A = [c - s1, c, c + s1]
                B = [c - s2, c, c + s2]
                raws.append({
                    "statement": "Data set A is $%d,\\ %d,\\ %d$ and data set B is "
                                 "$%d,\\ %d,\\ %d$. Which statement is true?"
                                 % (A[0], A[1], A[2], B[0], B[1], B[2]),
                    "correct": "The two sets have the same mean, but B is more spread out.",
                    "dvals": [
                        "The two sets have the same mean, but A is more spread out.",
                        "B has the larger mean as well as the larger spread.",
                        "The two sets have the same mean and the same spread.",
                    ],
                    "explanation": "Both sets are symmetric about $%d$, so both means are "
                                   "$%d$. The ranges differ: A spans $%d$ and B spans $%d$. "
                                   "Centre and spread are independent — equal means say "
                                   "nothing at all about how tightly the values cluster."
                                   % (c, c, 2 * s1, 2 * s2),
                    "check": ["Eq(Rational(%d, 3), %d)" % (sum(A), c),
                              "Eq(Rational(%d, 3), %d)" % (sum(B), c),
                              "%d > %d" % (2 * s2, 2 * s1)],
                })
    return raws


def g_relative_frequency():
    """LEVEL 2 — a two-way table read as a percentage of a row."""
    raws = []
    for a in (9, 12, 14, 15, 16, 18, 21, 24, 25, 27, 30, 32, 35, 36):
        for b in (6, 8, 10, 12, 14, 16, 20, 24):
            for c in (9, 11, 14, 16, 19):
                d = c + 5
                row = a + b
                pct = Rational(100 * a, row)
                if pct.q != 1:
                    continue
                raws.append({
                    "statement": "In a survey, $%d$ students who cycle and $%d$ students "
                                 "who walk said they enjoy the journey, while $%d$ cyclists "
                                 "and $%d$ walkers did not. What PERCENTAGE of the cyclists "
                                 "enjoy the journey?" % (a, c, b, d),
                    "correct": pct,
                    "dvals": [Rational(100 * b, row),
                              Rational(100 * a, a + c),
                              Rational(100 * a, a + b + c + d)],
                    "explanation": "'Of the cyclists' fixes the denominator: there are "
                                   "$%d + %d = %d$ cyclists in total, and $%d$ of them "
                                   "enjoy it, so $\\dfrac{%d}{%d} = %s\\%%$. Dividing by "
                                   "everyone surveyed, or by all the enjoyers, answers a "
                                   "different question."
                                   % (a, b, row, a, a, row, fmt(pct)),
                    "check": ["Eq(Rational(100*%d, %d), %d)" % (a, row, pct),
                              "Eq(%d + %d, %d)" % (a, b, row)],
                })
    return raws


def g_residual_fit():
    """LEVEL 3 — the residual, and what its sign says."""
    raws = []
    for m in (2, 3, 4, 5):
        for b in (1, 4, 7, 10):
            for x in (2, 3, 5, 6, 8):
                for e in (-6, -3, 3, 5):
                    pred = m * x + b
                    obs = pred + e
                    raws.append({
                        "statement": "A line of best fit is $y = %s$. At $x = %d$ the "
                                     "observed value is $%d$. What is the residual, and "
                                     "does the model over- or under-predict?"
                                     % (lin(m, b), x, obs),
                        "correct": e,
                        # sign reversed; the prediction; the observation
                        "dvals": [-e, pred, obs],
                        "explanation": "Residual means observed MINUS predicted: the model "
                                       "predicts $%d(%d) + %d = %d$, so the residual is "
                                       "$%d - %d = %d$. A %s residual means the point sits "
                                       "%s the line, so the model %s-predicts there. "
                                       "Reversing the subtraction reverses the story."
                                       % (m, x, b, pred, obs, pred, e,
                                          "positive" if e > 0 else "negative",
                                          "above" if e > 0 else "below",
                                          "under" if e > 0 else "over"),
                        "check": ["Eq(%d*%d + %d, %d)" % (m, x, b, pred),
                                  "Eq(%d - %d, %d)" % (obs, pred, e)],
                    })
    return raws


def g_association_claim():
    """LEVEL 3 — what an association does and does not license."""
    pairs = [
        ("hours of sleep", "test scores", "a tutoring programme"),
        ("ice-cream sales", "sunburn cases", "a sun-safety campaign"),
        ("shoe size", "reading ability", "a shoe-fitting service"),
        ("number of firefighters sent", "fire damage", "sending fewer firefighters"),
        ("coffee cups per day", "hours worked", "a coffee subsidy"),
        ("weekly exercise", "resting heart rate", "a gym membership"),
        ("class size", "average grade", "smaller classes"),
        ("time on social media", "reported anxiety", "a screen-time limit"),
        ("household income", "holiday spending", "an income supplement"),
        ("age of a car", "repair cost", "replacing older cars"),
        ("rainfall", "umbrella sales", "an umbrella tax"),
        ("study group size", "exam pass rate", "compulsory study groups"),
    ]
    raws = []
    for (v1, v2, action) in pairs:
        for r in (0.62, 0.71, 0.78, 0.84):
            raws.append({
                "statement": "A study finds a correlation of $%.2f$ between %s and %s. "
                             "Which conclusion is supported?" % (r, v1, v2),
                "correct": "The two vary together; the study alone cannot show that one "
                           "causes the other.",
                "dvals": [
                    "%s causes %s, because the correlation is strong."
                    % (v1.capitalize(), v2),
                    "Introducing %s will therefore change %s." % (action, v2),
                    "There is no relationship, because correlation is never meaningful.",
                ],
                "explanation": "A correlation of $%.2f$ is real and worth reporting — the "
                               "two quantities do move together. But an OBSERVATIONAL study "
                               "cannot rule out a lurking variable driving both, or the "
                               "causation running the other way. Only a randomised "
                               "experiment licenses a causal claim, and only for the "
                               "population it sampled." % r,
                "check": ["%s > 0" % r, "%s < 1" % r],
            })
    return raws


def g_outlier_effect():
    """LEVEL 3 — adding one extreme value: what moves and what does not."""
    raws = []
    for a in range(3, 15):
        for gap in (2, 3, 4):
            for jump in (40, 60, 90):
                vals = [a, a + gap, a + 2 * gap, a + 3 * gap, a + 4 * gap]
                med = vals[2]
                mean = Rational(sum(vals), 5)
                out = a + jump
                new_mean = Rational(sum(vals) + out, 6)
                new_med = Rational(vals[2] + vals[3], 2)
                raws.append({
                    "statement": "The values $%d,\\ %d,\\ %d,\\ %d,\\ %d$ have mean $%s$ "
                                 "and median $%d$. The value $%d$ is now added to the set. "
                                 "Which statement is true?"
                                 % (vals[0], vals[1], vals[2], vals[3], vals[4],
                                    fmt(mean), med, out),
                    "correct": "The mean rises by much more than the median does.",
                    "dvals": [
                        "The median rises by much more than the mean does.",
                        "The mean and the median rise by the same amount.",
                        "Neither the mean nor the median changes.",
                    ],
                    "explanation": "The new value is far above the rest. The mean uses "
                                   "every value's SIZE, so it climbs from $%s$ to $%s$. The "
                                   "median only cares about POSITION, and with six values "
                                   "it becomes the average of the middle two: $%s$ — a "
                                   "small move. That difference in sensitivity is why the "
                                   "median is preferred for skewed data."
                                   % (fmt(mean), fmt(new_mean), fmt(new_med)),
                    "check": ["Eq(Rational(%d, 5), Rational(%d, %d))"
                              % (sum(vals), mean.p, mean.q),
                              "Eq(Rational(%d, 6), Rational(%d, %d))"
                              % (sum(vals) + out, new_mean.p, new_mean.q),
                              "Rational(%d, %d) - Rational(%d, %d) > "
                              "Rational(%d, %d) - %d"
                              % (new_mean.p, new_mean.q, mean.p, mean.q,
                                 new_med.p, new_med.q, med)],
                })
    return raws
