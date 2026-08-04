# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 6 — mirrors /math/6.

One collection PER UNIT: each of the ten Grade 6 topics gets its own set of
forms, its own unit page and its own practice session
(/math/problem-bank/6/<unit>/practice).

Every problem is generated from a parameter SWEEP and every answer is
COMPUTED, never typed. Decimals are carried as Rational — 0.35 is
Rational(35, 100), never the binary float — so a check can never pass or fail
on a rounding artefact.

Grade 6 is where the number system opens up: negatives, decimals and percents
are all in scope, unlike Grade 4/5. Division still carries its receipt where
a remainder is meant.

Self-check:  python3 scripts/pb/grade6.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys
from math import gcd

from sympy import Rational, factorint

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt, money  # noqa: E402

SLUG = "6"
TITLE = "Grade 6"
TITLE_MN = "6-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 6 year — ratios and rates, "
         "fractions, decimals, percents, integers, factors, expressions and "
         "equations, the coordinate plane, area and volume, and statistics.")

UNITS = [
    {"id": "ratios-and-rates", "title": "Ratios & Rates",
     "blurb": "Writing and simplifying ratios, equivalent ratios, comparing them, rates and unit rates."},
    {"id": "fractions", "title": "Fractions",
     "blurb": "Equivalence and comparison, the four operations on fractions, and fraction word problems."},
    {"id": "decimals", "title": "Decimals",
     "blurb": "Decimal place value, comparing and rounding, and the four operations on decimals."},
    {"id": "percentages", "title": "Percentages",
     "blurb": "Percent of a number, what percent one number is of another, increase and decrease, and finding the whole."},
    {"id": "integers", "title": "Integers",
     "blurb": "Comparing and ordering, absolute value and opposites, and the four operations on signed numbers."},
    {"id": "factors-and-multiples", "title": "Factors and Multiples",
     "blurb": "Factors and multiples, primes and composites, greatest common factor, least common multiple and prime factorisation."},
    {"id": "expressions-and-equations", "title": "Expressions and Equations",
     "blurb": "Exponents, order of operations, writing and evaluating expressions, equivalence and one-step equations."},
    {"id": "coordinate-plane", "title": "Coordinate Plane",
     "blurb": "Quadrants, plotting and reading points, reflections across the axes, and distance between points."},
    {"id": "geometry-area-volume", "title": "Geometry: Area and Volume",
     "blurb": "Area of rectangles, parallelograms, triangles and trapezoids, composite figures, volume and surface area."},
    {"id": "data-and-statistics", "title": "Data and Statistics",
     "blurb": "Mean, median, mode and range, reading dot plots and histograms, and describing a data set."},
]


def dec(v):
    """Exact decimal string for a Rational: Rational(465,100) -> '4.65'.

    Never goes through float — 0.1 + 0.2 must not become 0.30000000000000004
    in a statement a twelve-year-old is asked to trust.
    """
    r = Rational(v)
    neg = r < 0
    r = abs(r)
    k = 0
    while (Rational(10) ** k * r).q != 1:
        k += 1
        if k > 8:
            raise ValueError("not a terminating decimal: %s" % v)
    n = int(Rational(10) ** k * r)
    s = str(n).rjust(k + 1, "0")
    out = s if k == 0 else s[:-k] + "." + s[-k:]
    return ("-" if neg else "") + out


def M(n):
    """A grouped whole number INSIDE math: 3 000 -> $3\\,000$.

    money() emits a KaTeX thin space, so it MUST sit inside $...$ — outside,
    the reader sees a literal backslash-comma. That defect shipped in the
    Grade 5 bank once already.
    """
    return "$%s$" % money(n)


def frac(a, b):
    """A fraction written exactly as given, without reducing."""
    return "\\frac{%d}{%d}" % (a, b)


def signed(n):
    """A signed integer for display: -4 stays -4, +4 renders as 4."""
    return str(n)


def operand(n):
    """An operand in a signed calculation.

    Negatives get brackets — "5 - (-3)" — because that is how the sign is
    read; positives do not, since "-12 x (8)" is not how anyone writes it.
    """
    return "(%d)" % n if n < 0 else str(n)


# ===========================================================================
# UNIT 1 — Ratios & Rates
# ===========================================================================

def _g_simplify_ratio():
    for k in (2, 3, 4, 5, 6, 7):
        for (a, b) in ((2, 3), (3, 4), (4, 5), (5, 6), (2, 5), (3, 7), (4, 7), (5, 8)):
            A, B = a * k, b * k
            yield {
                "statement": "Write the ratio $%d : %d$ in its simplest form." % (A, B),
                "correct": "$%d : %d$" % (a, b),
                "dvals": ["$%d : %d$" % (b, a), "$%d : %d$" % (A // gcd(A, B) + 1, b),
                          "$%d : %d$" % (a, b + 1)],
                "explanation": ("The greatest common factor of $%d$ and $%d$ is $%d$: "
                                "$%d \\div %d = %d$ and $%d \\div %d = %d$."
                                % (A, B, k, A, k, a, B, k, b)),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (A, B, a, b),
                          "Eq(gcd(%d, %d), 1)" % (a, b)],
            }


def _g_equivalent_ratio():
    for (a, b) in ((2, 3), (3, 5), (4, 7), (5, 2), (7, 4), (3, 8), (6, 5), (9, 4)):
        for k in (2, 3, 4, 5, 6):
            yield {
                "statement": ("$%d : %d = %d : \\square$. What number completes the ratio?"
                              % (a, b, a * k)),
                "correct": b * k,
                "dvals": [b + k, b * (k + 1), a * k],
                "explanation": ("The first part was multiplied by $%d$ ($%d \\times %d = %d$), "
                                "so the second must be too: $%d \\times %d = %d$."
                                % (k, a, k, a * k, b, k, b * k)),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (a, b, a * k, b * k),
                          "Eq(%d*%d, %d)" % (b, k, b * k)],
            }


def _g_compare_ratios():
    PAIRS = [((2, 3), (3, 4)), ((3, 5), (5, 8)), ((4, 7), (5, 9)), ((5, 6), (7, 9)),
             ((2, 5), (3, 8)), ((7, 10), (5, 7)), ((4, 9), (3, 7)), ((5, 12), (4, 9)),
             ((7, 8), (8, 9)), ((3, 4), (5, 7)), ((6, 11), (5, 9)), ((9, 10), (7, 8)),
             ((2, 7), (3, 10)), ((5, 11), (4, 9)), ((7, 12), (5, 9)), ((3, 8), (4, 11)),
             ((8, 15), (5, 9)), ((7, 9), (9, 11)), ((4, 5), (9, 11)), ((5, 13), (3, 8)),
             ((6, 7), (7, 8)), ((2, 9), (3, 13)), ((9, 14), (5, 8)), ((11, 12), (13, 14)),
             ((3, 11), (2, 7)), ((7, 15), (5, 11)), ((4, 13), (3, 10)), ((8, 9), (10, 11)),
             ((5, 14), (4, 11)), ((6, 13), (7, 15))]
    for ((a, b), (c, d)) in PAIRS:
        L, R = Rational(a, b), Rational(c, d)
        if L == R:
            continue
        big = "$%d : %d$" % ((a, b) if L > R else (c, d))
        small = "$%d : %d$" % ((c, d) if L > R else (a, b))
        yield {
            "statement": ("Which ratio is larger, $%d : %d$ or $%d : %d$?" % (a, b, c, d)),
            "correct": big,
            "dvals": [small, "They are equal", "$%d : %d$" % (a + c, b + d)],
            "explanation": ("Write both with the same second part, or compare "
                            "$%s$ against $%s$: %s is larger."
                            % (fmt(L), fmt(R), big.strip("$"))),
            "check": ["Ne(Rational(%d, %d), Rational(%d, %d))" % (a, b, c, d),
                      "Eq(Max(Rational(%d, %d), Rational(%d, %d)), Rational(%d, %d))"
                      % (a, b, c, d, *((a, b) if L > R else (c, d)))],
        }


def _g_rate():
    for total in (120, 150, 180, 210, 240, 270, 300, 360):
        for hours in (2, 3, 4, 5, 6):
            if total % hours:
                continue
            per = total // hours
            yield {
                "statement": ("A van travels $%d$ km in $%d$ hours at a steady speed. "
                              "How far does it travel in one hour?" % (total, hours)),
                "correct": per,
                "dvals": [per + hours, total - hours, per * 2],
                "explanation": ("Divide to find the rate for one hour: "
                                "$%d \\div %d = %d$ km." % (total, hours, per)),
                "check": ["Eq(%d*%d, %d)" % (per, hours, total),
                          "Eq(Rational(%d, %d), %d)" % (total, hours, per)],
            }


def _g_unit_rate():
    for items in (4, 5, 6, 8, 10, 12):
        for unit_price in (150, 240, 320, 450, 600, 750):
            total = items * unit_price
            yield {
                "statement": ("$%d$ identical notebooks cost %s tögrög. "
                              "What is the cost of one notebook, in tögrög?"
                              % (items, M(total))),
                "correct": M(unit_price),
                "dvals": [M(unit_price + items), M(total - items), M(unit_price * 2)],
                "explanation": ("Unit rate is the total divided by how many: "
                                "$%s \\div %d = %s$ tögrög."
                                % (money(total), items, money(unit_price))),
                "check": ["Eq(%d*%d, %d)" % (items, unit_price, total),
                          "Eq(Rational(%d, %d), %d)" % (total, items, unit_price)],
            }


def _g_ratio_word():
    for (a, b) in ((2, 3), (3, 4), (3, 5), (4, 5), (5, 7), (2, 7), (5, 4), (7, 3)):
        for k in (3, 4, 5, 6, 7):
            total = (a + b) * k
            partA = a * k
            yield {
                "statement": ("Red and blue counters are in the ratio $%d : %d$. "
                              "There are $%d$ counters altogether. How many are red?"
                              % (a, b, total)),
                "correct": partA,
                "dvals": [b * k, total - partA + 1, a * (k + 1)],
                "explanation": ("There are $%d + %d = %d$ shares and $%d \\div %d = %d$ "
                                "in each share, so red has $%d \\times %d = %d$."
                                % (a, b, a + b, total, a + b, k, a, k, partA)),
                "check": ["Eq(%d*%d, %d)" % (a + b, k, total),
                          "Eq(%d*%d, %d)" % (a, k, partA),
                          "Eq(Rational(%d, %d), Rational(%d, %d))" % (partA, total - partA, a, b)],
            }


# ===========================================================================
# UNIT 2 — Fractions
# ===========================================================================

def _g_equiv_fraction():
    for den in (3, 4, 5, 6, 8, 9, 10, 12):
        for num in range(1, den):
            if gcd(num, den) != 1:
                continue
            for k in (2, 3, 4):
                yield {
                    "statement": ("Fill the box: $%s = \\frac{\\square}{%d}$"
                                  % (frac(num, den), den * k)),
                    "correct": num * k,
                    "dvals": [num, num + k, num * (k + 1)],
                    "explanation": ("The bottom was multiplied by $%d$, so the top must be "
                                    "too: $%d \\times %d = %d$." % (k, num, k, num * k)),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (num * k, den * k, num, den)],
                }


def _g_compare_fractions():
    # Pairs are swept rather than hand-listed so the form cannot quietly run
    # short as the floor moves.
    SEEDS = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5), (4, 5),
             (1, 6), (5, 6), (2, 7), (3, 7), (4, 7), (5, 7), (3, 8), (5, 8),
             (7, 8), (4, 9), (5, 9), (7, 9), (3, 10), (7, 10), (9, 10),
             (5, 11), (7, 12), (11, 12)]
    PAIRS = [(SEEDS[i], SEEDS[j])
             for i in range(len(SEEDS))
             for j in (i + 1, i + 3, i + 7)
             if j < len(SEEDS)]
    for ((a, b), (c, d)) in PAIRS:
        L, R = Rational(a, b), Rational(c, d)
        if L == R:
            continue
        hi = (a, b) if L > R else (c, d)
        lo = (c, d) if L > R else (a, b)
        yield {
            "statement": "Which is larger, $%s$ or $%s$?" % (frac(a, b), frac(c, d)),
            "correct": "$%s$" % frac(*hi),
            "dvals": ["$%s$" % frac(*lo), "They are equal", "$%s$" % frac(a + c, b + d)],
            "explanation": ("Over the common denominator $%d$: $%s$ against $%s$."
                            % (b * d, frac(a * d, b * d), frac(c * b, b * d))),
            "check": ["Rational(%d, %d) > Rational(%d, %d)" % (hi[0], hi[1], lo[0], lo[1]),
                      "Eq(Rational(%d, %d)*%d, %d)" % (a, b, b, a)],
        }


def _g_add_sub_fractions():
    # Non-unit fractions with unlike denominators — the case the common
    # denominator actually matters for.
    SEEDS = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5), (3, 5),
             (4, 5), (1, 6), (5, 6), (2, 7), (3, 7), (3, 8), (5, 8), (7, 8),
             (3, 10), (7, 10), (5, 12), (7, 12)]
    for i, (a, b) in enumerate(SEEDS):
        for (c, d) in SEEDS[i + 1:i + 4]:
            if b == d:
                continue
            L, R = Rational(a, b), Rational(c, d)
            s = L + R
            diff = abs(L - R)
            lcd = b * d // gcd(b, d)
            if diff == 0:
                continue
            yield {
                "statement": "Work out $%s + %s$." % (frac(a, b), frac(c, d)),
                "correct": "$%s$" % fmt(s),
                # added tops and bottoms / subtracted instead / slipped by one
                # part of the common denominator
                "dvals": ["$%s$" % frac(a + c, b + d),
                          "$%s$" % fmt(diff),
                          "$%s$" % fmt(s + Rational(1, lcd))],
                "explanation": ("The common denominator is $%d$: "
                                "$%s + %s = %s$, which is $%s$."
                                % (lcd, frac(a * lcd // b, lcd), frac(c * lcd // d, lcd),
                                   frac(a * lcd // b + c * lcd // d, lcd), fmt(s))),
                "check": ["Eq(Rational(%d, %d) + Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, s.p, s.q),
                          "Eq(lcm(%d, %d), %d)" % (b, d, lcd)],
            }


def _g_multiply_fractions():
    for (a, b) in ((1, 2), (2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (5, 6), (3, 8), (5, 8)):
        for (c, d) in ((2, 3), (3, 4), (4, 5), (5, 7), (1, 3), (3, 7)):
            p = Rational(a, b) * Rational(c, d)
            yield {
                "statement": "Work out $%s \\times %s$." % (frac(a, b), frac(c, d)),
                "correct": "$%s$" % fmt(p),
                "dvals": ["$%s$" % fmt(Rational(a, b) + Rational(c, d)),
                          "$%s$" % frac(a * d, b * c),
                          "$%s$" % frac(a + c, b * d)],
                "explanation": ("Multiply across: $%d \\times %d = %d$ on top and "
                                "$%d \\times %d = %d$ underneath, which simplifies to $%s$."
                                % (a, c, a * c, b, d, b * d, fmt(p))),
                "check": ["Eq(Rational(%d, %d)*Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, p.p, p.q)],
            }


def _g_divide_fractions():
    for (a, b) in ((1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (5, 6), (5, 8), (7, 10),
                   (2, 7), (3, 8), (7, 12), (5, 9)):
        for (c, d) in ((1, 2), (2, 3), (3, 4), (1, 4), (2, 5), (3, 8), (1, 3), (5, 6)):
            if (a, b) == (c, d):
                continue
            q = Rational(a, b) / Rational(c, d)
            yield {
                "statement": "Work out $%s \\div %s$." % (frac(a, b), frac(c, d)),
                "correct": "$%s$" % fmt(q),
                "dvals": ["$%s$" % fmt(Rational(a, b) * Rational(c, d)),
                          "$%s$" % fmt(Rational(c, d) / Rational(a, b)),
                          "$%s$" % frac(a * c, b * d)],
                "explanation": ("Dividing by a fraction is multiplying by its reciprocal: "
                                "$%s \\times %s = %s$." % (frac(a, b), frac(d, c), fmt(q))),
                "check": ["Eq(Rational(%d, %d)/Rational(%d, %d), Rational(%d, %d))"
                          % (a, b, c, d, q.p, q.q)],
            }


def _g_fraction_word():
    for den in (3, 4, 5, 6, 8):
        for num in range(1, den):
            if gcd(num, den) != 1:
                continue
            for total in (24, 36, 48, 60, 72, 96, 120):
                if total % den:
                    continue
                part = num * total // den
                yield {
                    "statement": ("A shop has $%d$ apples and sells $%s$ of them. "
                                  "How many are left?" % (total, frac(num, den))),
                    "correct": total - part,
                    # answered with the amount SOLD / forgot to subtract /
                    # out by one share
                    "dvals": [part, total, total - part + total // den],
                    "explanation": ("It sold $%s \\times %d = %d$, so $%d - %d = %d$ are "
                                    "left." % (frac(num, den), total, part, total, part,
                                               total - part)),
                    "check": ["Eq(Rational(%d, %d)*%d, %d)" % (num, den, total, part),
                              "Eq(%d - %d, %d)" % (total, part, total - part)],
                }


# ===========================================================================
# UNIT 3 — Decimals
# ===========================================================================

DEC_PLACE = {1: "tenths", 2: "hundredths", 3: "thousandths"}


def _g_decimal_place():
    # The asked digit must appear exactly once after the point, or the
    # question has two answers — so the other digits come from a pool that
    # excludes it, and each pool is tried in turn to keep the sweep wide.
    POOLS = [(7, 2, 9), (1, 5, 3), (8, 6, 4), (2, 8, 5)]
    for d in range(1, 10):
        for p in (1, 2, 3):
            for pool in POOLS:
                rest = [x for x in pool if x != d][:2]
                if len(rest) < 2:
                    continue
                digits = list(rest)
                digits.insert(p - 1, d)
                if digits.count(d) != 1:
                    continue
                whole = 4
                r = Rational(whole * 1000 + digits[0] * 100 + digits[1] * 10 + digits[2],
                             1000)
                val = Rational(d, 10 ** p)
                others = [Rational(d, 10 ** q) for q in (1, 2, 3) if q != p] + [Rational(d)]
                yield {
                    "statement": "In $%s$, what is the digit $%d$ worth?" % (dec(r), d),
                    "correct": "$%s$" % dec(val),
                    "dvals": ["$%s$" % dec(o) for o in others[:3]],
                    "explanation": ("It stands in the %s place, so it is worth $%s$."
                                    % (DEC_PLACE[p], dec(val))),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (d, 10 ** p, val.p, val.q)],
                }


def _g_compare_decimals():
    # Every triple sets the same trap: the SHORTEST string is the largest
    # value. Swept rather than listed so the form stays wide.
    def triples():
        for w in range(0, 5):
            for t in range(2, 10):
                for k in (1, 7):
                    x = dec(Rational(w * 10 + t, 10))
                    y = dec(Rational(w * 100 + (t - 1) * 10 + 5, 100))
                    z = dec(Rational(w * 1000 + (t - 1) * 100 + k, 1000))
                    if len({Rational(x), Rational(y), Rational(z)}) != 3:
                        continue
                    yield x, y, z

    for (x, y, z) in triples():
        vals = {s: Rational(s) for s in (x, y, z)}
        big = max(vals, key=lambda s: vals[s])
        rest = [s for s in (x, y, z) if s != big]
        yield {
            "statement": ("Which is the largest: $%s$, $%s$ or $%s$?" % (x, y, z)),
            "correct": "$%s$" % big,
            "dvals": ["$%s$" % rest[0], "$%s$" % rest[1], "They are equal"],
            "explanation": ("Line up the points and compare place by place — a longer "
                            "decimal is not automatically larger. $%s$ is the largest."
                            % big),
            "check": ["Rational('%s') > Rational('%s')" % (big, rest[0]),
                      "Rational('%s') > Rational('%s')" % (big, rest[1])],
        }


def _g_round_decimal():
    BASES = ["3.472", "1.856", "2.349", "5.617", "4.283", "6.745", "7.128", "8.564",
             "9.037", "2.916", "3.581", "4.209", "1.374", "2.638", "4.951", "5.062",
             "6.487", "7.253", "8.719", "9.146", "1.528", "3.094", "5.736", "6.812"]
    for s in BASES:
        r = Rational(s)
        for p in (1, 2):
            step = Rational(1, 10 ** p)
            below = Rational(int(r / step)) * step
            above = below + step
            near = below if (r - below) < (above - r) else above
            # rounded the wrong way / out by two steps / rounded to one place
            # too many. NOT "below" — when the answer rounds down that IS the
            # answer, and the whole form collapses.
            other = above if near == below else below
            step2 = Rational(1, 10 ** (p + 1))
            b2 = Rational(int(r / step2)) * step2
            near2 = b2 if (r - b2) < (b2 + step2 - r) else b2 + step2
            dv = [other, near + 2 * step, near2]
            if len({near} | set(dv)) != 4:
                continue
            yield {
                "statement": ("Round $%s$ to $%d$ decimal place%s."
                              % (s, p, "" if p == 1 else "s")),
                "correct": "$%s$" % dec(near),
                "dvals": ["$%s$" % dec(o) for o in dv],
                "explanation": ("$%s$ lies between $%s$ and $%s$, and it is nearer to $%s$."
                                % (s, dec(below), dec(above), dec(near))),
                "check": ["Abs(Rational('%s') - Rational(%d, %d)) <= Rational(1, %d)"
                          % (s, near.p, near.q, 2 * 10 ** p)],
            }


def _g_add_sub_decimals():
    A = ["2.4", "3.75", "1.6", "5.28", "4.05", "6.9", "7.35", "8.2"]
    B = ["1.35", "0.8", "2.45", "1.07", "3.6", "0.95"]
    for x in A:
        for y in B:
            X, Y = Rational(x), Rational(y)
            s = X + Y
            yield {
                "statement": "Work out $%s + %s$." % (x, y),
                "correct": "$%s$" % dec(s),
                "dvals": ["$%s$" % dec(X - Y if X > Y else Y - X),
                          "$%s$" % dec(s + Rational(1, 10)),
                          "$%s$" % dec(s - Rational(1, 100))],
                "explanation": ("Line up the decimal points and add: $%s + %s = %s$."
                                % (x, y, dec(s))),
                "check": ["Eq(Rational('%s') + Rational('%s'), Rational(%d, %d))"
                          % (x, y, s.p, s.q)],
            }


def _g_multiply_decimals():
    for x in ("0.4", "0.7", "1.2", "2.5", "3.6", "0.25", "1.5", "4.2"):
        for k in (3, 4, 6, 8, 12):
            X = Rational(x)
            p = X * k
            yield {
                "statement": "Work out $%s \\times %d$." % (x, k),
                "correct": "$%s$" % dec(p),
                "dvals": ["$%s$" % dec(p * 10), "$%s$" % dec(p / 10),
                          "$%s$" % dec(X + k)],
                "explanation": ("Multiply as whole numbers, then put back the same number "
                                "of decimal places: $%s \\times %d = %s$." % (x, k, dec(p))),
                "check": ["Eq(Rational('%s')*%d, Rational(%d, %d))" % (x, k, p.p, p.q)],
            }


def _g_divide_decimals():
    for k in (2, 4, 5, 8):
        for whole in (12, 18, 24, 30, 36, 42, 48, 60):
            q = Rational(whole, 10) / k
            if q.q > 100:
                continue
            x = dec(Rational(whole, 10))
            yield {
                "statement": "Work out $%s \\div %d$." % (x, k),
                "correct": "$%s$" % dec(q),
                "dvals": ["$%s$" % dec(q * 10), "$%s$" % dec(q / 10),
                          "$%s$" % dec(Rational(whole, 10) * k)],
                "explanation": ("$%s \\div %d = %s$ — check it by multiplying back: "
                                "$%s \\times %d = %s$." % (x, k, dec(q), dec(q), k, x)),
                "check": ["Eq(Rational('%s')/%d, Rational(%d, %d))" % (x, k, q.p, q.q),
                          "Eq(Rational(%d, %d)*%d, Rational('%s'))" % (q.p, q.q, k, x)],
            }


# ===========================================================================
# UNIT 4 — Percentages
# ===========================================================================

def _g_percent_of():
    for pct in (5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80):
        for n in (40, 60, 80, 120, 200, 240, 300, 400):
            v = Rational(pct, 100) * n
            if v.q != 1:
                continue
            v = int(v)
            yield {
                "statement": "What is $%d\\%%$ of $%d$?" % (pct, n),
                "correct": v,
                "dvals": [v + pct, n - v, v * 2],
                "explanation": ("$%d\\%%$ means $%s$, and $%s \\times %d = %d$."
                                % (pct, frac(pct, 100), frac(pct, 100), n, v)),
                "check": ["Eq(Rational(%d, 100)*%d, %d)" % (pct, n, v)],
            }


def _g_what_percent():
    for whole in (20, 25, 40, 50, 80, 200):
        for pct in (10, 20, 25, 40, 50, 60, 75, 80):
            part = Rational(pct, 100) * whole
            if part.q != 1:
                continue
            part = int(part)
            yield {
                "statement": "What percent of $%d$ is $%d$?" % (whole, part),
                "correct": "$%d\\%%$" % pct,
                "dvals": ["$%d\\%%$" % (pct + 10), "$%d\\%%$" % (100 - pct),
                          "$%d\\%%$" % (part if part != pct and part <= 100 else pct + 5)],
                "explanation": ("$%s = %s$, which is $%d\\%%$."
                                % (frac(part, whole), fmt(Rational(part, whole)), pct)),
                "check": ["Eq(Rational(%d, %d)*100, %d)" % (part, whole, pct)],
            }


def _g_fraction_percent():
    PAIRS = [((1, 2), 50), ((1, 4), 25), ((3, 4), 75), ((1, 5), 20), ((2, 5), 40),
             ((3, 5), 60), ((4, 5), 80), ((1, 10), 10), ((3, 10), 30), ((7, 10), 70),
             ((9, 10), 90), ((1, 20), 5), ((3, 20), 15), ((7, 20), 35), ((11, 20), 55),
             ((13, 20), 65), ((17, 20), 85), ((19, 20), 95), ((1, 25), 4), ((6, 25), 24),
             ((1, 50), 2), ((7, 50), 14), ((21, 50), 42), ((23, 25), 92),
             ((2, 25), 8), ((9, 20), 45), ((11, 25), 44), ((17, 50), 34),
             ((3, 50), 6), ((13, 25), 52), ((19, 25), 76), ((9, 25), 36)]
    for ((a, b), pct) in PAIRS:
        yield {
            "statement": "Write $%s$ as a percentage." % frac(a, b),
            "correct": "$%d\\%%$" % pct,
            # the complement / a near miss / the numerator read as a percent.
            # NOT (100 - pct) alone: at 50% that IS the answer.
            "dvals": ["$%d\\%%$" % (pct + 5), "$%d\\%%$" % a, "$%d\\%%$" % b],
            "explanation": ("Scale the bottom to $100$: $%s = %s = %d\\%%$."
                            % (frac(a, b), frac(pct, 100), pct)),
            "check": ["Eq(Rational(%d, %d)*100, %d)" % (a, b, pct)],
        }


def _g_percent_change():
    for n in (40, 50, 60, 80, 120, 200, 250, 400):
        for pct in (10, 20, 25, 50):
            up = n + Rational(pct, 100) * n
            down = n - Rational(pct, 100) * n
            if up.q != 1 or down.q != 1:
                continue
            up, down = int(up), int(down)
            yield {
                "statement": ("A price of %s tögrög rises by $%d\\%%$. "
                              "What is the new price, in tögrög?" % (M(n), pct)),
                "correct": M(up),
                # took it off instead of adding / gave only the rise / forgot to
                # apply it. NOT n - pct: that is a NEGATIVE price for a big
                # percentage, which is not a thing a shop can charge.
                "dvals": [M(down), M(up - n), M(n)],
                "explanation": ("The rise is $%d\\%%$ of $%d$, which is $%d$, so the new "
                                "price is $%d + %d = %d$."
                                % (pct, n, up - n, n, up - n, up)),
                "check": ["Eq(%d + Rational(%d, 100)*%d, %d)" % (n, pct, n, up)],
            }
            yield {
                "statement": ("A price of %s tögrög falls by $%d\\%%$. "
                              "What is the new price, in tögrög?" % (M(n), pct)),
                "correct": M(down),
                # added instead of taking off / gave only the fall / forgot to
                # apply it
                "dvals": [M(up), M(n - down), M(n)],
                "explanation": ("The fall is $%d\\%%$ of $%d$, which is $%d$, so the new "
                                "price is $%d - %d = %d$."
                                % (pct, n, n - down, n, n - down, down)),
                "check": ["Eq(%d - Rational(%d, 100)*%d, %d)" % (n, pct, n, down)],
            }


def _g_find_whole():
    for pct in (10, 20, 25, 40, 50, 75, 80):
        for whole in (40, 60, 80, 120, 200, 240, 400):
            part = Rational(pct, 100) * whole
            if part.q != 1:
                continue
            part = int(part)
            yield {
                "statement": ("$%d\\%%$ of a number is $%d$. What is the number?"
                              % (pct, part)),
                "correct": whole,
                "dvals": [part, whole + part, whole // 2],
                "explanation": ("If $%d\\%%$ is $%d$, then $1\\%%$ is $%s$ and $100\\%%$ is "
                                "$%s \\times 100 = %d$."
                                % (pct, part, fmt(Rational(part, pct)),
                                   fmt(Rational(part, pct)), whole)),
                "check": ["Eq(Rational(%d, 100)*%d, %d)" % (pct, whole, part)],
            }


def _g_percent_word():
    for total in (40, 50, 60, 80, 120, 200):
        for pct in (15, 20, 25, 30, 40, 60):
            got = Rational(pct, 100) * total
            if got.q != 1:
                continue
            got = int(got)
            yield {
                "statement": ("A class of $%d$ pupils has $%d\\%%$ who cycle to school. "
                              "How many do NOT cycle?" % (total, pct)),
                "correct": total - got,
                "dvals": [got, total - got + 5, 100 - pct],
                "explanation": ("$%d\\%%$ of $%d$ is $%d$ who cycle, so $%d - %d = %d$ do "
                                "not." % (pct, total, got, total, got, total - got)),
                "check": ["Eq(Rational(%d, 100)*%d, %d)" % (pct, total, got),
                          "Eq(%d - %d, %d)" % (total, got, total - got)],
            }


# ===========================================================================
# UNIT 5 — Integers
# ===========================================================================

def _g_compare_integers():
    PAIRS = [(-3, 5), (-7, -2), (-10, 4), (0, -6), (-1, -9), (8, -8), (-15, -12),
             (-4, 0), (-20, -25), (6, -11), (-13, -3), (-18, 2), (-5, -14), (9, -9),
             (-2, -8), (-30, -21), (-6, 3), (-11, -17), (7, -7), (-24, -19),
             (-16, 5), (-9, -1), (-25, -30), (4, -13), (-8, -12), (-14, 6)]
    for (a, b) in PAIRS:
        hi, lo = max(a, b), min(a, b)
        yield {
            "statement": "Which is greater, $%s$ or $%s$?" % (signed(a), signed(b)),
            "correct": hi,
            # picked the wrong one / off by one / compared sizes instead of
            # positions. NOT abs(lo): for a pair like 8 and -8 that IS the
            # answer.
            "dvals": [lo, lo - 1, abs(hi) + abs(lo) + 1],
            "explanation": ("On the number line $%s$ lies to the right of $%s$, so it is "
                            "greater. Being further from zero does not make a negative "
                            "bigger." % (signed(hi), signed(lo))),
            "check": ["%d > %d" % (hi, lo)],
        }


def _g_absolute_value():
    for n in list(range(-20, 0)) + list(range(1, 15)):
        yield {
            "statement": "What is $|%s|$?" % signed(n),
            "correct": abs(n),
            "dvals": [n if n < 0 else -n, abs(n) + 1, abs(n) * 2],
            "explanation": ("Absolute value is the distance from zero, which is never "
                            "negative: $|%s| = %d$." % (signed(n), abs(n))),
            "check": ["Eq(Abs(%d), %d)" % (n, abs(n))],
        }


def _g_add_integers():
    for a in (-12, -9, -7, -5, -3, 4, 6, 8, 11):
        for b in (-11, -8, -6, -4, 5, 7, 9, 13):
            s = a + b
            if s == 0:
                continue          # -s would equal the answer
            yield {
                "statement": "Work out $%s + %s$." % (signed(a), operand(b)),
                "correct": s,
                # subtracted instead / reversed the order / flipped the sign.
                # |a|+|b| is NOT usable: for a positive pair it is the answer.
                "dvals": [a - b, b - a, -s],
                "explanation": ("Signs differ means take the difference and keep the sign "
                                "of the larger size; signs the same means add and keep the "
                                "sign. $%s + (%s) = %s$." % (signed(a), signed(b), signed(s))),
                "check": ["Eq(%d + %d, %d)" % (a, b, s)],
            }


def _g_subtract_integers():
    for a in (-10, -8, -5, -2, 3, 6, 9, 12):
        for b in (-9, -6, -4, 5, 7, 11):
            d = a - b
            if d == 0:
                continue          # b - a would equal the answer
            yield {
                "statement": "Work out $%s - %s$." % (signed(a), operand(b)),
                "correct": d,
                # added instead / reversed the order / subtracted twice.
                # b - a IS -d, so it cannot also appear as a separate option.
                "dvals": [a + b, b - a, a - 2 * b],
                "explanation": ("Subtracting is adding the opposite: "
                                "$%s - %s = %s + %s = %s$."
                                % (signed(a), operand(b), signed(a), operand(-b), signed(d))),
                "check": ["Eq(%d - %d, %d)" % (a, b, d), "Eq(%d + (%d), %d)" % (a, -b, d)],
            }


def _g_multiply_divide_integers():
    for a in (-12, -9, -8, -6, -4, 3, 5, 7, 11):
        for b in (-7, -5, -3, 4, 6, 8):
            p = a * b
            yield {
                "statement": "Work out $%s \\times %s$." % (signed(a), operand(b)),
                "correct": p,
                "dvals": [-p, a + b, abs(p) + 1],
                "explanation": ("Same signs give a positive, different signs give a "
                                "negative: $%s \\times %s = %s$."
                                % (signed(a), operand(b), signed(p))),
                "check": ["Eq(%d*%d, %d)" % (a, b, p)],
            }


def _g_integer_word():
    for start in (-15, -12, -8, -5, -3, 2, 6, 10):
        for rise in (4, 7, 9, 12, 18, 23):
            end = start + rise
            yield {
                "statement": ("At dawn the temperature was $%s$ °C. By noon it had risen "
                              "by $%d$ °C. What was the temperature at noon, in °C?"
                              % (signed(start), rise)),
                "correct": end,
                "dvals": [start - rise, rise - start, -end],
                "explanation": ("Rising means moving right on the number line: "
                                "$%s + %d = %s$." % (signed(start), rise, signed(end))),
                "check": ["Eq(%d + %d, %d)" % (start, rise, end)],
            }


# ===========================================================================
# UNIT 6 — Factors and Multiples
# ===========================================================================

def _g_factors():
    for n in (12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 42, 45, 48, 50, 54, 56, 60,
              64, 66, 70, 72, 75, 80, 84, 88, 90, 96, 100):
        divs = [d for d in range(1, n + 1) if n % d == 0]
        k = len(divs)
        yield {
            "statement": "How many factors does $%d$ have?" % n,
            "correct": k,
            "dvals": [k + 1, k - 1, k + 2],
            "explanation": ("The factors of $%d$ are %s — that is $%d$ of them."
                            % (n, ", ".join("$%d$" % d for d in divs), k)),
            "check": ["Eq(%d, %d)" % (k, k)] + ["Eq(Mod(%d, %d), 0)" % (n, d) for d in divs[:4]],
        }


def _g_multiples():
    for n in range(3, 16):
        for k in (4, 5, 6, 7):
            m = n * k
            yield {
                "statement": "What is the $%d$th multiple of $%d$?" % (k, n),
                "correct": m,
                "dvals": [n * (k + 1), n + k, n * (k - 1)],
                "explanation": ("Multiples of $%d$ are $%d, %d, %d, \\ldots$ — the $%d$th "
                                "is $%d \\times %d = %d$."
                                % (n, n, 2 * n, 3 * n, k, n, k, m)),
                "check": ["Eq(%d*%d, %d)" % (n, k, m), "Eq(Mod(%d, %d), 0)" % (m, n)],
            }


def _g_prime_composite():
    NUMS = list(range(11, 60))
    for n in NUMS:
        f = factorint(n)
        is_prime = len(f) == 1 and list(f.values())[0] == 1
        yield {
            "statement": "Is $%d$ prime or composite?" % n,
            "correct": "Prime" if is_prime else "Composite",
            "dvals": ["Composite" if is_prime else "Prime", "Neither", "Both"],
            "explanation": (("$%d$ has no factors except $1$ and itself, so it is prime."
                             % n) if is_prime else
                            ("$%d = %s$, so it has a factor other than $1$ and itself and "
                             "is composite."
                             % (n, " \\times ".join("%d" % p * 1 for p in
                                                    sorted(f) for _ in range(f[p]))))),
            "check": (["Eq(len(factorint(%d)), 1)" % n] if is_prime
                      else ["Mod(%d, %d) == 0" % (n, sorted(f)[0])]),
        }


def _g_gcf():
    PAIRS = [(12, 18), (16, 24), (20, 30), (24, 36), (18, 27), (28, 42), (30, 45),
             (32, 48), (36, 60), (40, 56), (45, 75), (48, 72), (50, 80), (54, 81),
             (60, 90), (63, 84), (14, 35), (22, 33), (26, 39), (34, 51), (15, 25),
             (21, 28), (33, 55), (44, 66), (52, 78), (25, 65)]
    for (a, b) in PAIRS:
        g = gcd(a, b)
        yield {
            "statement": "What is the greatest common factor of $%d$ and $%d$?" % (a, b),
            "correct": g,
            "dvals": [a * b // g, g * 2, g + 1],
            "explanation": ("The common factors of $%d$ and $%d$ are the divisors of $%d$; "
                            "the greatest is $%d$." % (a, b, g, g)),
            "check": ["Eq(gcd(%d, %d), %d)" % (a, b, g),
                      "Eq(Mod(%d, %d), 0)" % (a, g), "Eq(Mod(%d, %d), 0)" % (b, g)],
        }


def _g_lcm():
    PAIRS = [(4, 6), (6, 8), (8, 12), (9, 12), (10, 15), (12, 18), (14, 21), (15, 20),
             (16, 24), (18, 24), (20, 25), (21, 28), (24, 36), (5, 7), (6, 9), (8, 10),
             (9, 15), (10, 12), (12, 16), (14, 18), (15, 25), (18, 27), (20, 30),
             (22, 33), (26, 39), (4, 10)]
    for (a, b) in PAIRS:
        l = a * b // gcd(a, b)
        yield {
            "statement": "What is the least common multiple of $%d$ and $%d$?" % (a, b),
            "correct": l,
            "dvals": [a * b, gcd(a, b), l + a],
            "explanation": ("$%d \\times %d \\div %d = %d$, using the greatest common "
                            "factor $%d$." % (a, b, gcd(a, b), l, gcd(a, b))),
            "check": ["Eq(lcm(%d, %d), %d)" % (a, b, l),
                      "Eq(Mod(%d, %d), 0)" % (l, a), "Eq(Mod(%d, %d), 0)" % (l, b)],
        }


def _g_prime_factorisation():
    NUMS = [12, 18, 20, 24, 28, 30, 36, 40, 42, 44, 45, 48, 50, 52, 54, 56, 60,
            63, 66, 70, 72, 75, 80, 84, 88, 90, 98, 100]
    for n in NUMS:
        f = factorint(n)
        parts = []
        for p in sorted(f):
            parts.append("%d" % p if f[p] == 1 else "%d^{%d}" % (p, f[p]))
        shown = " \\times ".join(parts)
        wrong1 = " \\times ".join("%d" % p for p in sorted(f))
        wrong2 = " \\times ".join(["%d" % (sorted(f)[0])] * 2 + ["%d" % n])
        wrong3 = " \\times ".join("%d" % (p + 1) for p in sorted(f))
        if len({shown, wrong1, wrong2, wrong3}) != 4:
            continue
        yield {
            "statement": "Write $%d$ as a product of prime factors." % n,
            "correct": "$%s$" % shown,
            "dvals": ["$%s$" % wrong1, "$%s$" % wrong2, "$%s$" % wrong3],
            "explanation": ("Divide by primes until only primes remain: $%d = %s$."
                            % (n, shown)),
            "check": ["Eq(%s, %d)" % (" * ".join("%d**%d" % (p, f[p]) for p in sorted(f)), n)],
        }


# ===========================================================================
# UNIT 7 — Expressions and Equations
# ===========================================================================

def _g_exponents():
    for b in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        for e in (2, 3, 4):
            v = b ** e
            if v > 10000:
                continue
            yield {
                "statement": "What is $%d^{%d}$?" % (b, e),
                "correct": v,
                # multiplied by the exponent / one too many factors / one too few
                "dvals": [b * e, v + b, v - b],
                "explanation": ("$%d^{%d}$ means $%s = %d$ — an exponent is repeated "
                                "multiplication, not multiplication by the exponent."
                                % (b, e, " \\times ".join([str(b)] * e), v)),
                "check": ["Eq(%d**%d, %d)" % (b, e, v)],
            }


def _g_order_of_operations():
    for a in (2, 3, 4, 5, 6):
        for b in (2, 3, 4, 5):
            for c in (6, 8, 10, 12):
                v = a + b * c
                wrong = (a + b) * c
                if v == wrong:
                    continue
                yield {
                    "statement": "Work out $%d + %d \\times %d$." % (a, b, c),
                    "correct": v,
                    "dvals": [wrong, a * b + c, a + b + c],
                    "explanation": ("Multiplication comes before addition: "
                                    "$%d \\times %d = %d$, then $%d + %d = %d$."
                                    % (b, c, b * c, a, b * c, v)),
                    "check": ["Eq(%d + %d*%d, %d)" % (a, b, c, v),
                              "Ne(%d + %d*%d, (%d + %d)*%d)" % (a, b, c, a, b, c)],
                }


def _g_evaluate_expression():
    for a in (2, 3, 4, 5, 6, 7):
        for b in (1, 2, 3, 4, 5):
            for x in (2, 3, 4, 5, 6):
                v = a * x + b
                yield {
                    "statement": ("Evaluate $%dx + %d$ when $x = %d$." % (a, b, x)),
                    "correct": v,
                    "dvals": [a + x + b, a * (x + b), v + a],
                    "explanation": ("Substitute and follow the order of operations: "
                                    "$%d \\times %d + %d = %d + %d = %d$."
                                    % (a, x, b, a * x, b, v)),
                    "check": ["Eq(%d*%d + %d, %d)" % (a, x, b, v)],
                }


def _g_write_expression():
    for a in (2, 3, 4, 5, 6, 7, 8):
        for b in (1, 3, 5, 7, 9, 11):
            yield {
                "statement": ("Write an expression for: $%d$ more than $%d$ times a "
                              "number $n$." % (b, a)),
                "correct": "$%dn + %d$" % (a, b),
                "dvals": ["$%d(n + %d)$" % (a, b), "$%dn - %d$" % (a, b),
                          "$%dn + %d$" % (b, a)],
                "explanation": ("$%d$ times the number is $%dn$, and $%d$ more than that "
                                "adds $%d$: $%dn + %d$." % (a, a, b, b, a, b)),
                "check": ["Eq((%d*2 + %d), %d)" % (a, b, a * 2 + b),
                          "Ne(%d*(2 + %d), %d*2 + %d)" % (a, b, a, b)],
            }


def _g_equivalent_expression():
    for a in (2, 3, 4, 5, 6):
        for b in (1, 2, 3, 4, 5, 6):
            yield {
                "statement": "Expand $%d(x + %d)$." % (a, b),
                "correct": "$%dx + %d$" % (a, a * b),
                "dvals": ["$%dx + %d$" % (a, b), "$%dx + %d$" % (a * b, a * b),
                          "$%dx$" % (a * b)],
                "explanation": ("Multiply both terms inside by $%d$: "
                                "$%d \\times x = %dx$ and $%d \\times %d = %d$."
                                % (a, a, a, a, b, a * b)),
                "check": ["Eq(%d*(3 + %d), %d*3 + %d)" % (a, b, a, a * b)],
            }


def _g_one_step_equation():
    for a in (2, 3, 4, 5, 6, 7, 8, 9):
        for x in (3, 4, 5, 6, 7, 8, 9, 12):
            v = a * x
            yield {
                "statement": "Solve $%dx = %d$." % (a, v),
                "correct": x,
                "dvals": [v - a, v + a, a + x],
                "explanation": ("Divide both sides by $%d$: $%d \\div %d = %d$."
                                % (a, v, a, x)),
                "check": ["Eq(%d*%d, %d)" % (a, x, v), "Eq(Rational(%d, %d), %d)" % (v, a, x)],
            }


# ===========================================================================
# UNIT 8 — Coordinate Plane
# ===========================================================================

def _quad(x, y):
    if x > 0 and y > 0:
        return "I"
    if x < 0 and y > 0:
        return "II"
    if x < 0 and y < 0:
        return "III"
    return "IV"


def _g_quadrant():
    for x in (-6, -4, -2, 3, 5, 7):
        for y in (-5, -3, 2, 4, 6):
            q = _quad(x, y)
            others = [o for o in ("I", "II", "III", "IV") if o != q]
            yield {
                "statement": "In which quadrant does the point $(%d,\\ %d)$ lie?" % (x, y),
                "correct": "Quadrant %s" % q,
                "dvals": ["Quadrant %s" % o for o in others],
                "explanation": ("$x$ is %s and $y$ is %s, which is quadrant %s."
                                % ("positive" if x > 0 else "negative",
                                   "positive" if y > 0 else "negative", q)),
                "check": ["Eq(sign(%d), %d)" % (x, 1 if x > 0 else -1),
                          "Eq(sign(%d), %d)" % (y, 1 if y > 0 else -1)],
            }


def _g_reflect():
    for x in (-6, -4, -3, 2, 5, 7):
        for y in (-5, -2, 3, 4, 6):
            yield {
                "statement": ("Reflect the point $(%d,\\ %d)$ across the $x$-axis. "
                              "What are its new coordinates?" % (x, y)),
                "correct": "$(%d,\\ %d)$" % (x, -y),
                "dvals": ["$(%d,\\ %d)$" % (-x, y), "$(%d,\\ %d)$" % (-x, -y),
                          "$(%d,\\ %d)$" % (y, x)],
                "explanation": ("Reflecting across the $x$-axis keeps $x$ and flips the "
                                "sign of $y$: $(%d,\\ %d) \\to (%d,\\ %d)$."
                                % (x, y, x, -y)),
                "check": ["Eq(%d, %d)" % (x, x), "Eq(%d, -(%d))" % (-y, y)],
            }


def _g_distance_axis():
    for a in (-8, -6, -4, -2, 1, 3, 5):
        for b in (2, 4, 6, 7, 9):
            if a == b:
                continue
            d = abs(b - a)
            yield {
                "statement": ("Points $(%d,\\ 3)$ and $(%d,\\ 3)$ lie on the same "
                              "horizontal line. How far apart are they?" % (a, b)),
                "correct": d,
                "dvals": [a + b, abs(a) + abs(b) + 1, d + 2],
                "explanation": ("Same $y$, so the distance is the difference of the "
                                "$x$-values: $|%d - %d| = %d$." % (b, a, d)),
                "check": ["Eq(Abs(%d - %d), %d)" % (b, a, d)],
            }


def _g_read_point():
    for x in (-7, -5, -3, 2, 4, 6):
        for y in (-6, -4, 3, 5, 7):
            yield {
                "statement": ("A point is $%d$ units %s of the origin and $%d$ units %s "
                              "it. What are its coordinates?"
                              % (abs(x), "right" if x > 0 else "left",
                                 abs(y), "above" if y > 0 else "below")),
                "correct": "$(%d,\\ %d)$" % (x, y),
                "dvals": ["$(%d,\\ %d)$" % (y, x), "$(%d,\\ %d)$" % (-x, y),
                          "$(%d,\\ %d)$" % (x, -y)],
                "explanation": ("The $x$-coordinate comes first: $%d$ across and $%d$ up "
                                "or down gives $(%d,\\ %d)$." % (x, y, x, y)),
                "check": ["Eq(Abs(%d), %d)" % (x, abs(x)), "Eq(Abs(%d), %d)" % (y, abs(y))],
            }


def _g_rectangle_on_grid():
    for w in (3, 4, 5, 6, 7, 8):
        for h in (2, 3, 5, 6, 9):
            area = w * h
            per = 2 * (w + h)
            yield {
                "statement": ("A rectangle on the grid has corners $(0,\\ 0)$, $(%d,\\ 0)$, "
                              "$(%d,\\ %d)$ and $(0,\\ %d)$. What is its area?"
                              % (w, w, h, h)),
                "correct": area,
                "dvals": [per, w + h, area + w],
                "explanation": ("The sides are $%d$ and $%d$, so the area is "
                                "$%d \\times %d = %d$ square units." % (w, h, w, h, area)),
                "check": ["Eq(%d*%d, %d)" % (w, h, area)],
            }


def _g_perimeter_on_grid():
    for w in (3, 4, 5, 6, 7, 8):
        for h in (2, 3, 5, 6, 9):
            per = 2 * (w + h)
            yield {
                "statement": ("A rectangle on the grid is $%d$ units wide and $%d$ units "
                              "tall. What is its perimeter?" % (w, h)),
                "correct": per,
                "dvals": [w * h, w + h, per + 2],
                "explanation": ("Perimeter is twice the width plus twice the height: "
                                "$2 \\times (%d + %d) = %d$ units." % (w, h, per)),
                "check": ["Eq(2*(%d + %d), %d)" % (w, h, per)],
            }


# ===========================================================================
# UNIT 9 — Geometry: Area and Volume
# ===========================================================================

def _g_area_rectangle():
    for b in (4, 5, 6, 7, 8, 9, 12, 15):
        for h in (3, 4, 6, 8, 10):
            a = b * h
            yield {
                "statement": ("A parallelogram has base $%d$ cm and height $%d$ cm. "
                              "What is its area, in square centimetres?" % (b, h)),
                "correct": a,
                "dvals": [2 * (b + h), b + h, a // 2 if a % 2 == 0 else a + b],
                "explanation": ("Area of a parallelogram is base times height: "
                                "$%d \\times %d = %d$." % (b, h, a)),
                "check": ["Eq(%d*%d, %d)" % (b, h, a)],
            }


def _g_area_triangle():
    for b in (4, 6, 8, 10, 12, 14, 16, 18):
        for h in (3, 5, 7, 9, 11):
            a = Rational(b * h, 2)
            if a.q != 1:
                continue
            a = int(a)
            yield {
                "statement": ("A triangle has base $%d$ cm and height $%d$ cm. "
                              "What is its area, in square centimetres?" % (b, h)),
                "correct": a,
                "dvals": [b * h, b + h, a + b],
                "explanation": ("Area of a triangle is half the base times the height: "
                                "$%d \\times %d \\div 2 = %d$." % (b, h, a)),
                "check": ["Eq(Rational(%d*%d, 2), %d)" % (b, h, a)],
            }


def _g_area_trapezoid():
    for a in (4, 5, 6, 8, 10):
        for b in (7, 9, 12, 14, 16):
            for h in (4, 6, 8):
                area = Rational((a + b) * h, 2)
                if area.q != 1:
                    continue
                area = int(area)
                yield {
                    "statement": ("A trapezoid has parallel sides $%d$ cm and $%d$ cm and "
                                  "height $%d$ cm. What is its area, in square "
                                  "centimetres?" % (a, b, h)),
                    "correct": area,
                    "dvals": [(a + b) * h, a * b, area + h],
                    "explanation": ("Add the parallel sides, halve, then multiply by the "
                                    "height: $(%d + %d) \\div 2 \\times %d = %d$."
                                    % (a, b, h, area)),
                    "check": ["Eq(Rational((%d + %d)*%d, 2), %d)" % (a, b, h, area)],
                }


def _g_composite_area():
    for w in (6, 8, 10, 12):
        for h in (4, 5, 6, 7):
            for c in (2, 3):
                big = w * h
                cut = c * c
                area = big - cut
                yield {
                    "statement": ("A $%d$ cm by $%d$ cm rectangle has a $%d$ cm square cut "
                                  "out of one corner. What area is left, in square "
                                  "centimetres?" % (w, h, c)),
                    "correct": area,
                    "dvals": [big, cut, area - c],
                    "explanation": ("The rectangle is $%d \\times %d = %d$ and the square "
                                    "is $%d \\times %d = %d$, so $%d - %d = %d$ is left."
                                    % (w, h, big, c, c, cut, big, cut, area)),
                    "check": ["Eq(%d*%d - %d*%d, %d)" % (w, h, c, c, area)],
                }


def _g_volume_prism():
    for l in (3, 4, 5, 6, 8):
        for w in (2, 3, 4, 7):
            for h in (2, 5, 6):
                v = l * w * h
                yield {
                    "statement": ("A rectangular prism is $%d$ cm by $%d$ cm by $%d$ cm. "
                                  "What is its volume, in cubic centimetres?" % (l, w, h)),
                    "correct": v,
                    "dvals": [l + w + h, 2 * (l * w + l * h + w * h), l * w],
                    "explanation": ("Volume is length times width times height: "
                                    "$%d \\times %d \\times %d = %d$." % (l, w, h, v)),
                    "check": ["Eq(%d*%d*%d, %d)" % (l, w, h, v)],
                }


def _g_surface_area():
    for l in (2, 3, 4, 5, 6):
        for w in (2, 3, 4, 7):
            for h in (3, 5, 8):
                sa = 2 * (l * w + l * h + w * h)
                yield {
                    "statement": ("A box is $%d$ cm by $%d$ cm by $%d$ cm. What is its "
                                  "surface area, in square centimetres?" % (l, w, h)),
                    "correct": sa,
                    "dvals": [l * w * h, sa // 2, l * w + l * h + w * h + 1],
                    "explanation": ("Three pairs of faces: "
                                    "$2(%d \\times %d + %d \\times %d + %d \\times %d) = %d$."
                                    % (l, w, l, h, w, h, sa)),
                    "check": ["Eq(2*(%d*%d + %d*%d + %d*%d), %d)" % (l, w, l, h, w, h, sa)],
                }


# ===========================================================================
# UNIT 10 — Data and Statistics
# ===========================================================================

DATASETS = [
    [4, 7, 9, 12, 3], [8, 5, 11, 6, 10], [15, 12, 18, 9, 21], [6, 6, 9, 12, 2],
    [20, 14, 17, 11, 23], [7, 13, 5, 9, 11], [16, 10, 22, 8, 14], [3, 8, 5, 12, 7],
    [25, 18, 30, 12, 20], [9, 15, 6, 18, 12], [11, 7, 14, 5, 8], [24, 16, 20, 12, 28],
    [5, 10, 15, 20, 25], [13, 9, 17, 11, 15], [22, 14, 26, 18, 10], [6, 12, 18, 9, 15],
    [8, 8, 14, 20, 5], [17, 13, 21, 9, 25], [4, 11, 7, 14, 9], [19, 15, 23, 11, 27],
    [10, 6, 14, 18, 22], [12, 16, 8, 20, 4], [21, 9, 15, 27, 3], [7, 14, 21, 28, 5],
    [16, 12, 8, 20, 24], [11, 22, 33, 5, 9], [13, 26, 7, 19, 10], [18, 6, 24, 12, 30],
]


def _g_mean():
    # Built around the mean rather than filtered for it: five deviations that
    # sum to zero give an exact mean every time, so the sweep never thins.
    SPREADS = [(-4, -1, 0, 2, 3), (-6, -2, 1, 3, 4), (-3, -3, 0, 3, 3),
               (-5, 0, 0, 2, 3), (-7, -1, 2, 2, 4), (-2, -2, -1, 2, 3)]
    for m in range(8, 30):
        for spread in SPREADS:
            data = [m + d for d in spread]
            if min(data) < 1:
                continue
            total = sum(data)
            n = len(data)
            yield {
                "statement": ("Find the mean of %s."
                              % ", ".join("$%d$" % x for x in data)),
                "correct": m,
                # gave the total / gave the range / off by one
                "dvals": [total, max(data) - min(data), m + 1],
                "explanation": ("Add them: $%d$. Divide by how many: $%d \\div %d = %d$."
                                % (total, total, n, m)),
                "check": ["Eq(Rational(%d, %d), %d)" % (total, n, m),
                          "Eq(%s, %d)" % (" + ".join(str(x) for x in data), total)],
            }


def _g_median():
    for data in DATASETS:
        s = sorted(data)
        med = s[len(s) // 2]
        yield {
            "statement": ("Find the median of %s." % ", ".join("$%d$" % x for x in data)),
            "correct": med,
            # took the middle of the UNSORTED list is the classic error, but it
            # often is the median — so the options are the two ends and their
            # sum, which never coincide with the middle value.
            "dvals": [s[0], s[-1], s[0] + s[-1]],
            "explanation": ("In order they are %s, and the middle value is $%d$."
                            % (", ".join("$%d$" % x for x in s), med)),
            "check": ["Eq(%d, %d)" % (med, med),
                      "%d >= %d" % (med, s[0]), "%d <= %d" % (med, s[-1])],
        }


def _g_mode():
    for data in DATASETS:
        d = data + [data[0]]          # guarantee exactly one repeat
        counts = {x: d.count(x) for x in d}
        top = max(counts, key=lambda x: counts[x])
        if list(counts.values()).count(counts[top]) != 1:
            continue
        yield {
            "statement": ("Find the mode of %s." % ", ".join("$%d$" % x for x in d)),
            "correct": top,
            # near misses plus the two ends added — max(d) alone is unusable
            # because the repeated value is often the largest.
            "dvals": [top + 1, top - 1, max(d) + min(d)],
            "explanation": ("$%d$ appears $%d$ times, more often than any other value."
                            % (top, counts[top])),
            "check": ["Eq(%d, %d)" % (top, top)],
        }


def _g_range():
    for data in DATASETS:
        r = max(data) - min(data)
        yield {
            "statement": ("Find the range of %s." % ", ".join("$%d$" % x for x in data)),
            "correct": r,
            # answered with either end / added them. NOT r + min: that is
            # exactly max, which is already an option.
            "dvals": [max(data), min(data), max(data) + min(data)],
            "explanation": ("Largest minus smallest: $%d - %d = %d$."
                            % (max(data), min(data), r)),
            "check": ["Eq(%d - %d, %d)" % (max(data), min(data), r)],
        }


def _g_frequency_table():
    for a in (3, 5, 7, 9, 11):
        for b in (2, 4, 6, 8):
            for c in (1, 3, 5):
                total = a + b + c
                yield {
                    "statement": ("A frequency table shows $%d$ pupils with one pet, $%d$ "
                                  "with two and $%d$ with three. How many pupils were "
                                  "asked?" % (a, b, c)),
                    "correct": total,
                    "dvals": [a + b, total + c, a * 1 + b * 2 + c * 3],
                    "explanation": ("Add the frequencies: $%d + %d + %d = %d$ pupils."
                                    % (a, b, c, total)),
                    "check": ["Eq(%d + %d + %d, %d)" % (a, b, c, total)],
                }


def _g_histogram_interval():
    for start in (0, 10, 20, 30, 40):
        for width in (5, 10, 20):
            for k in (2, 3, 4):
                lo = start + width * (k - 1)
                hi = lo + width
                yield {
                    "statement": ("A histogram has equal intervals of width $%d$ starting "
                                  "at $%d$. What is the $%d$rd interval?"
                                  % (width, start, k) if k == 3 else
                                  ("A histogram has equal intervals of width $%d$ starting "
                                   "at $%d$. What is interval number $%d$?"
                                   % (width, start, k))),
                    "correct": "$%d$ to $%d$" % (lo, hi),
                    "dvals": ["$%d$ to $%d$" % (lo + width, hi + width),
                              "$%d$ to $%d$" % (start, start + width),
                              "$%d$ to $%d$" % (lo, hi + width)],
                    "explanation": ("Each interval is $%d$ wide, so interval $%d$ runs "
                                    "from $%d + %d \\times %d = %d$ to $%d$."
                                    % (width, k, start, width, k - 1, lo, hi)),
                    "check": ["Eq(%d + %d*%d, %d)" % (start, width, k - 1, lo),
                              "Eq(%d - %d, %d)" % (hi, lo, width)],
                }


# ===========================================================================

def build():
    forms = []

    U1 = "ratios-and-rates"
    forms += [
        form("g6-simplify-ratio", "Simplifying a ratio", 1, U1,
             "Divide both parts by their greatest common factor.",
             mk_txt("g6-sr", _g_simplify_ratio())),
        form("g6-equivalent-ratio", "Equivalent ratios", 1, U1,
             "Whatever you multiply one part by, multiply the other by too.",
             mk_txt("g6-er", _g_equivalent_ratio())),
        form("g6-compare-ratios", "Comparing ratios", 2, U1,
             "Turn both into fractions, or give them a common second part.",
             mk_txt("g6-cr", _g_compare_ratios())),
        form("g6-rate", "Rates", 2, U1,
             "A rate compares two different units — divide to find one of them.",
             mk_num("g6-rt", _g_rate())),
        form("g6-unit-rate", "Unit rate", 2, U1,
             "Cost per one item: divide the total by how many.",
             mk_txt("g6-ur", _g_unit_rate())),
        form("g6-ratio-word", "Ratio word problems", 3, U1,
             "Count the shares first, then find what one share is worth.",
             mk_num("g6-rw", _g_ratio_word())),
    ]

    U2 = "fractions"
    forms += [
        form("g6-equiv-fraction", "Equivalent fractions", 1, U2,
             "Multiply top and bottom by the same number.",
             mk_txt("g6-ef", _g_equiv_fraction())),
        form("g6-compare-fractions", "Comparing fractions", 1, U2,
             "A common denominator settles it.",
             mk_txt("g6-cf", _g_compare_fractions())),
        form("g6-add-fractions", "Adding fractions", 2, U2,
             "Common denominator first — never add the bottoms.",
             mk_txt("g6-af", _g_add_sub_fractions())),
        form("g6-multiply-fractions", "Multiplying fractions", 2, U2,
             "Multiply across the top and across the bottom, then simplify.",
             mk_txt("g6-mf", _g_multiply_fractions())),
        form("g6-divide-fractions", "Dividing fractions", 2, U2,
             "Multiply by the reciprocal of the second fraction.",
             mk_txt("g6-df", _g_divide_fractions())),
        form("g6-fraction-word", "Fraction word problems", 3, U2,
             "Read what the fraction is OF, and what the question asks for.",
             mk_num("g6-fw", _g_fraction_word())),
    ]

    U3 = "decimals"
    forms += [
        form("g6-decimal-place", "Decimal place value", 1, U3,
             "Tenths, hundredths, thousandths — the column names the value.",
             mk_txt("g6-dp", _g_decimal_place())),
        form("g6-compare-decimals", "Comparing decimals", 1, U3,
             "Compare place by place; more digits does not mean larger.",
             mk_txt("g6-cd", _g_compare_decimals())),
        form("g6-round-decimal", "Rounding decimals", 2, U3,
             "Find the two neighbours at that place, then take the nearer.",
             mk_txt("g6-rd", _g_round_decimal())),
        form("g6-add-decimals", "Adding decimals", 2, U3,
             "Line up the points, not the right-hand ends.",
             mk_txt("g6-ad", _g_add_sub_decimals())),
        form("g6-multiply-decimals", "Multiplying decimals", 2, U3,
             "Multiply as whole numbers, then restore the decimal places.",
             mk_txt("g6-md", _g_multiply_decimals())),
        form("g6-divide-decimals", "Dividing decimals", 3, U3,
             "Divide, then check by multiplying back.",
             mk_txt("g6-dd", _g_divide_decimals())),
    ]

    U4 = "percentages"
    forms += [
        form("g6-percent-of", "Percent of a number", 1, U4,
             "A percent is hundredths — multiply.",
             mk_num("g6-po", _g_percent_of())),
        form("g6-fraction-percent", "Fractions as percentages", 1, U4,
             "Scale the denominator to one hundred.",
             mk_txt("g6-fp", _g_fraction_percent())),
        form("g6-what-percent", "What percent is it?", 2, U4,
             "Part over whole, then scale to hundredths.",
             mk_txt("g6-wp", _g_what_percent())),
        form("g6-percent-change", "Increase and decrease", 2, U4,
             "Find the change, then add it on or take it off.",
             mk_txt("g6-pc", _g_percent_change())),
        form("g6-percent-word", "Percent word problems", 2, U4,
             "Decide whether the question wants the part or what is left.",
             mk_num("g6-pw", _g_percent_word())),
        form("g6-find-whole", "Finding the whole", 3, U4,
             "Work back from the part: find one percent, then one hundred.",
             mk_num("g6-fh", _g_find_whole())),
    ]

    U5 = "integers"
    forms += [
        form("g6-compare-integers", "Comparing integers", 1, U5,
             "Further right on the number line means greater.",
             mk_num("g6-ci", _g_compare_integers())),
        form("g6-absolute-value", "Absolute value", 1, U5,
             "Distance from zero, never negative.",
             mk_num("g6-av", _g_absolute_value())),
        form("g6-add-integers", "Adding integers", 2, U5,
             "Same signs add; different signs take the difference.",
             mk_num("g6-ai", _g_add_integers())),
        form("g6-subtract-integers", "Subtracting integers", 2, U5,
             "Subtracting is adding the opposite.",
             mk_num("g6-si", _g_subtract_integers())),
        form("g6-multiply-integers", "Multiplying and dividing integers", 2, U5,
             "Same signs positive, different signs negative.",
             mk_num("g6-mi", _g_multiply_divide_integers())),
        form("g6-integer-word", "Integers in context", 3, U5,
             "Temperature and elevation: decide which way the number line moves.",
             mk_num("g6-iw", _g_integer_word())),
    ]

    U6 = "factors-and-multiples"
    forms += [
        form("g6-factors", "Factors", 1, U6,
             "Every number that divides it exactly, counted in pairs.",
             mk_num("g6-fc", _g_factors())),
        form("g6-multiples", "Multiples", 1, U6,
             "The times table of a number, going on forever.",
             mk_num("g6-mu", _g_multiples())),
        form("g6-prime-composite", "Prime or composite", 2, U6,
             "Exactly two factors makes a prime.",
             mk_txt("g6-pc2", _g_prime_composite())),
        form("g6-gcf", "Greatest common factor", 2, U6,
             "The largest number that divides both.",
             mk_num("g6-gc", _g_gcf())),
        form("g6-lcm", "Least common multiple", 2, U6,
             "The first number that appears in both times tables.",
             mk_num("g6-lc", _g_lcm())),
        form("g6-prime-factorisation", "Prime factorisation", 3, U6,
             "Break it down until every factor is prime.",
             mk_txt("g6-pf", _g_prime_factorisation())),
    ]

    U7 = "expressions-and-equations"
    forms += [
        form("g6-exponents", "Exponents", 1, U7,
             "Repeated multiplication, not multiplication by the exponent.",
             mk_num("g6-ex", _g_exponents())),
        form("g6-order-of-operations", "Order of operations", 1, U7,
             "Multiplication and division before addition and subtraction.",
             mk_num("g6-oo", _g_order_of_operations())),
        form("g6-evaluate", "Evaluating expressions", 2, U7,
             "Substitute the value, then follow the order of operations.",
             mk_num("g6-ev", _g_evaluate_expression())),
        form("g6-write-expression", "Writing expressions", 2, U7,
             "Turn the words into symbols in the order the meaning demands.",
             mk_txt("g6-we", _g_write_expression())),
        form("g6-equivalent-expression", "Equivalent expressions", 2, U7,
             "The distributive law: multiply every term inside the bracket.",
             mk_txt("g6-ee", _g_equivalent_expression())),
        form("g6-one-step", "One-step equations", 3, U7,
             "Undo what was done to the unknown.",
             mk_num("g6-os", _g_one_step_equation())),
    ]

    U8 = "coordinate-plane"
    forms += [
        form("g6-quadrant", "Quadrants", 1, U8,
             "The pair of signs tells you the quadrant.",
             mk_txt("g6-qd", _g_quadrant())),
        form("g6-read-point", "Reading coordinates", 1, U8,
             "Across first, then up or down.",
             mk_txt("g6-rp", _g_read_point())),
        form("g6-reflect", "Reflections across an axis", 2, U8,
             "Reflecting in the x-axis flips the sign of y.",
             mk_txt("g6-rf", _g_reflect())),
        form("g6-distance", "Distance on the plane", 2, U8,
             "On a shared row or column, distance is the difference.",
             mk_num("g6-ds", _g_distance_axis())),
        form("g6-grid-perimeter", "Perimeter on the grid", 2, U8,
             "Twice the width plus twice the height.",
             mk_num("g6-gp", _g_perimeter_on_grid())),
        form("g6-grid-area", "Polygons on the grid", 3, U8,
             "Read the side lengths off the coordinates, then use the formula.",
             mk_num("g6-ga", _g_rectangle_on_grid())),
    ]

    U9 = "geometry-area-volume"
    forms += [
        form("g6-area-parallelogram", "Area of a parallelogram", 1, U9,
             "Base times perpendicular height.",
             mk_num("g6-ap", _g_area_rectangle())),
        form("g6-area-triangle", "Area of a triangle", 1, U9,
             "Half the base times the height.",
             mk_num("g6-at", _g_area_triangle())),
        form("g6-area-trapezoid", "Area of a trapezoid", 2, U9,
             "Average the parallel sides, then multiply by the height.",
             mk_num("g6-az", _g_area_trapezoid())),
        form("g6-volume", "Volume of a rectangular prism", 2, U9,
             "Length times width times height.",
             mk_num("g6-vl", _g_volume_prism())),
        form("g6-surface-area", "Surface area", 2, U9,
             "Three pairs of matching faces.",
             mk_num("g6-sa", _g_surface_area())),
        form("g6-composite-area", "Composite figures", 3, U9,
             "Split the shape, or subtract the missing piece.",
             mk_num("g6-ca", _g_composite_area())),
    ]

    U10 = "data-and-statistics"
    forms += [
        form("g6-range", "The range", 1, U10,
             "Largest minus smallest — the spread, not the centre.",
             mk_num("g6-rg", _g_range())),
        form("g6-frequency-table", "Frequency tables", 1, U10,
             "The frequencies add to how many were asked.",
             mk_num("g6-ft", _g_frequency_table())),
        form("g6-mean", "The mean", 2, U10,
             "Total divided by how many.",
             mk_num("g6-mn", _g_mean())),
        form("g6-median", "The median", 2, U10,
             "Order them first, then take the middle.",
             mk_num("g6-me", _g_median())),
        form("g6-mode", "The mode", 2, U10,
             "The value that appears most often.",
             mk_num("g6-mo", _g_mode())),
        form("g6-histogram", "Histogram intervals", 3, U10,
             "Equal-width intervals, counted from the start.",
             mk_txt("g6-hg", _g_histogram_interval())),
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
