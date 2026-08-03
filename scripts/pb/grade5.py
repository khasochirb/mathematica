# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 5 — mirrors /math/5.

One collection PER UNIT: each of the eight Grade 5 topics gets its own set
of forms, its own unit page and its own practice session
(/math/problem-bank/5/<unit>/practice), so a student drilling fractions
never has a place-value question thrown at them.

Every problem is generated from a parameter SWEEP and every answer is
COMPUTED, never typed — the same discipline as the Integrated Math banks.
Values stay exact: sympy checks are built from Integer/Rational, never from
float division, and decimal work is checked as Rational(35,100), never as
0.35 (binary floats are not the numbers a fifth-grader wrote down).

Grade 5 house rules observed here:
  - the tögrög sign is written OUTSIDE math (KaTeX cannot draw it);
  - division always carries its receipt (q*d + r = n AND r < d);
  - rounding is checked by nearness, never by a formatted string;
  - no negative results anywhere — integers are a Grade 6 idea.

Self-check:  python3 scripts/pb/grade5.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys

from sympy import Rational

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt, money  # noqa: E402

SLUG = "5"
TITLE = "Grade 5"
TITLE_MN = "5-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 5 year — place value and "
         "the four operations through fractions, decimals, measurement, "
         "geometry and data, with a separate problem set for every unit.")

UNITS = [
    {"id": "whole-numbers-and-place-value", "title": "Whole Numbers & Place Value",
     "blurb": "Digit values to the millions, comparing and ordering, rounding, expanded form and estimation."},
    {"id": "addition-and-subtraction", "title": "Addition & Subtraction",
     "blurb": "Multi-digit sums and differences, missing parts, two-step stories, estimates and add-back checks."},
    {"id": "multiplication-and-division", "title": "Multiplication & Division",
     "blurb": "Two-digit multiplication, the distributive split, division with and without remainders, and what a remainder means."},
    {"id": "fractions-first-steps", "title": "Fractions — First Steps",
     "blurb": "Equivalent fractions, simplifying, comparing, like-denominator arithmetic, mixed numbers and fractions of amounts."},
    {"id": "decimals-first-steps", "title": "Decimals — First Steps",
     "blurb": "Decimal place value, decimals as fractions, comparing without the length trap, adding on the point, rounding and money."},
    {"id": "measurement-and-units", "title": "Measurement & Units",
     "blurb": "The metric ladders for length, mass and capacity, the base-sixty ladder of time, elapsed time and convert-first problems."},
    {"id": "geometry-shapes-and-area", "title": "Geometry — Shapes & Area",
     "blurb": "Missing angles on lines and at points, triangle angle sums, perimeter, area, and figures built from rectangles."},
    {"id": "data-and-graphs", "title": "Data & Graphs",
     "blurb": "Tallies and tables, pictograph keys, bar-graph scales, change on a line graph, and the mean and range."},
]

PLACE_NAME = {2: "hundreds", 3: "thousands", 4: "ten-thousands",
              5: "hundred-thousands", 6: "millions"}


def M(n):
    """A whole number inside math, with thin-space grouping."""
    return "$%s$" % money(n)


def dec(v):
    """Render an exact Rational as a plain decimal string (no trailing zeros)."""
    v = Rational(v)
    s = "%f" % float(v)
    s = s.rstrip("0").rstrip(".")
    return s


def D(v):
    """A decimal inside math."""
    return "$%s$" % dec(v)


def rat_of(s):
    """sympy source for a decimal literal written as an exact Rational."""
    s = str(s)
    if "." not in s:
        return "Integer(%s)" % s
    whole, frac = s.split(".")
    den = 10 ** len(frac)
    return "Rational(%d, %d)" % (int(whole + frac), den)


# ==========================================================================
# Unit 1 — Whole Numbers & Place Value
# ==========================================================================

def _g_digit_value():
    # The asked digit must appear EXACTLY ONCE in the number, or the question
    # has two answers: build the backdrop from a pool that excludes it.
    for d in range(2, 10):
        for p in (2, 3, 4, 5, 6):
            pool = [x for x in (5, 1, 8, 3, 6, 2, 9, 4, 7) if x != d][:6]
            digits = list(pool)
            digits.insert(6 - p, d)
            assert digits.count(d) == 1 and digits[0] != 0
            n = int("".join(str(x) for x in digits))
            val = d * 10 ** p
            yield {
                "statement": "In %s, what is the digit $%d$ worth?" % (M(n), d),
                "correct": M(val),
                "dvals": [M(d), M(d * 10 ** (p - 1)), M(d * 10 ** (p + 1))],
                "explanation": ("It stands in the %s place, so it is worth "
                                "$%d \\times %s = %s$." % (PLACE_NAME[p], d, money(10 ** p), money(val))),
                "check": ["Eq(%d*%d, %d)" % (d, 10 ** p, val),
                          "Eq(Mod(floor(Rational(%d, %d)), 10), %d)" % (n, 10 ** p, d)],
            }


def _g_largest_number():
    for a in range(1, 10):
        for b in range(0, 10):
            base = 100000 * a + 1000 * b
            nums = [base + 4820, base + 4280, base + 4802, base + 4028]
            if len(set(nums)) != 4:
                continue
            top = max(nums)
            rest = [x for x in nums if x != top]
            yield {
                "statement": ("Four aimags report their populations as %s. Which "
                              "number is the largest?"
                              % ", ".join(M(x) for x in nums)),
                "correct": M(top),
                "dvals": [M(x) for x in rest],
                "explanation": ("Every number here uses the same digits, so compare "
                                "place by place from the left: %s wins at the "
                                "first place where they differ." % M(top)),
                "check": ["%d > %d" % (top, rest[0]), "%d > %d" % (top, rest[1]),
                          "%d > %d" % (top, rest[2])],
            }


def _g_round_place():
    starts = [3417, 8256, 12483, 25791, 46308, 57642, 91375, 138264,
              264913, 507428, 736159, 849027]
    for n in starts:
        for place in (10, 100, 1000, 10000):
            rem = n % place
            if rem == 0 or 2 * rem == place:
                continue
            down = n - rem
            up = down + place
            correct = up if 2 * rem > place else down
            other = down if correct == up else up
            yield {
                "statement": "Round %s to the nearest %s." % (M(n), M(place)),
                "correct": M(correct),
                "dvals": [M(other), M(down - place), M(up + place)],
                "explanation": ("%s sits between %s and %s; it is nearer %s, so that "
                                "is the rounded value." % (M(n), M(down), M(up), M(correct))),
                "check": ["Eq(%d + %d, %d)" % (down, place, up),
                          "Abs(%d - %d) < Abs(%d - %d)" % (n, correct, n, other),
                          "Eq(Mod(%d, %d), 0)" % (correct, place)],
            }


def _g_expanded_form():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in (3, 6, 9):
                n = a * 100000 + b * 1000 + c * 10 + 7
                terms = [a * 100000, b * 1000, c * 10, 7]
                correct = " + ".join(money(t) for t in terms)
                bad_flat = " + ".join(str(x) for x in (a, b, c, 7))
                bad_shift = " + ".join(money(t) for t in [a * 100000, b * 10000, c * 10, 7])
                bad_extra = " + ".join(money(t) for t in [a * 100000, b * 1000, 400, c * 10, 7])
                yield {
                    "statement": "Which is the expanded form of %s?" % M(n),
                    "correct": "$%s$" % correct,
                    "dvals": ["$%s$" % bad_flat, "$%s$" % bad_shift, "$%s$" % bad_extra],
                    "explanation": ("Each digit contributes its PLACE value: "
                                    "$%s = %s$. The zeros in %s contribute nothing, "
                                    "so they bring no term." % (correct, money(n), M(n))),
                    "check": ["Eq(%d + %d + %d + %d, %d)" % (terms[0], terms[1], terms[2], terms[3], n)],
                }


def _g_estimate_sum():
    pairs = [(2380, 4715), (3162, 5849), (4527, 2938), (6194, 1873),
             (7451, 2682), (5308, 3947), (8236, 1594), (2769, 6435),
             (3841, 4276), (5623, 3158), (9147, 728), (4085, 5762),
             (1938, 7264), (6472, 2815), (3506, 4193)]
    for a, b in pairs:
        for place in (100, 1000):
            ra = round(a / place) * place
            rb = round(b / place) * place
            if a % place == place // 2 or b % place == place // 2:
                continue
            est = ra + rb
            if est == a + b:
                continue
            yield {
                "statement": ("Estimate $%s + %s$ by rounding each number to the "
                              "nearest %s." % (money(a), money(b), M(place))),
                "correct": M(est),
                "dvals": [M(a + b), M(est + place), M(est - place)],
                "explanation": ("$%s$ rounds to $%s$ and $%s$ rounds to $%s$, so the "
                                "estimate is $%s$. (The exact answer is $%s$ — an "
                                "estimate is meant to be close, not equal.)"
                                % (money(a), money(ra), money(b), money(rb),
                                   money(est), money(a + b))),
                "check": ["Eq(%d + %d, %d)" % (ra, rb, est),
                          "Abs(%d - %d) <= %d" % (a, ra, place // 2),
                          "Abs(%d - %d) <= %d" % (b, rb, place // 2)],
            }


def _g_build_largest():
    sets = [(3, 8, 1, 6), (2, 9, 4, 7), (5, 1, 8, 3), (6, 2, 7, 9),
            (4, 8, 2, 5), (7, 3, 9, 1), (2, 6, 8, 4), (5, 9, 3, 7),
            (1, 4, 6, 8), (3, 7, 2, 9), (8, 5, 1, 6), (4, 9, 7, 2),
            (6, 3, 5, 8), (2, 7, 4, 9), (9, 1, 6, 3), (5, 8, 2, 4),
            (7, 4, 8, 1), (3, 6, 9, 5), (8, 2, 5, 7), (4, 1, 9, 6),
            (6, 9, 3, 2), (7, 5, 4, 8), (9, 3, 8, 1), (2, 5, 6, 7),
            (1, 8, 4, 3), (5, 6, 9, 2), (3, 4, 7, 6), (8, 9, 2, 1),
            (6, 7, 1, 5), (4, 3, 8, 9)]
    for ds in sets:
        big = int("".join(str(x) for x in sorted(ds, reverse=True)))
        small = int("".join(str(x) for x in sorted(ds)))
        asc = sorted(ds, reverse=True)
        swapped = int("".join(str(x) for x in (asc[:2] + [asc[3], asc[2]])))
        third = int("".join(str(x) for x in ([asc[1], asc[0]] + asc[2:])))
        yield {
            "statement": ("Using the digits $%d$, $%d$, $%d$ and $%d$ once each, "
                          "what is the largest four-digit number you can build?"
                          % ds),
            "correct": M(big),
            "dvals": [M(small), M(swapped), M(third)],
            "explanation": ("Put the biggest digit where it is worth most: "
                            "largest first, then next largest, down to the ones. "
                            "That gives $%d$." % big),
            "check": ["%d > %d" % (big, small), "%d > %d" % (big, swapped),
                      "%d > %d" % (big, third)],
        }


# ==========================================================================
# Unit 2 — Addition & Subtraction
# ==========================================================================

def _g_add_multi():
    pairs = [(2456, 3178), (5827, 1394), (4639, 2785), (7148, 2673),
             (3592, 4826), (6274, 3859), (8135, 1947), (2968, 5473),
             (4317, 3895), (5786, 2648), (1493, 7259), (6852, 2374),
             (3741, 5628), (9126, 843), (2537, 6489), (4908, 3175),
             (7263, 1848), (5471, 3796), (3084, 6927), (8619, 1284),
             (2745, 4936), (6318, 2857), (4172, 5689), (3826, 4795),
             (7509, 2364), (1657, 8243), (5294, 3718), (6837, 2465),
             (2913, 5876), (4586, 3927), (8071, 1638), (3465, 5279),
             (7182, 2749), (5638, 3417), (2094, 6835), (4753, 3268)]
    for a, b in pairs:
        s = a + b
        yield {
            "statement": "$%s + %s =$" % (money(a), money(b)),
            "correct": M(s),
            "dvals": [M(s - 1000), M(s + 10), M(s - 100)],
            "explanation": ("Line the places up and add from the right, carrying "
                            "each time a column passes nine: $%s$. Check by "
                            "subtracting: $%s - %s = %s$."
                            % (money(s), money(s), money(b), money(a))),
            "check": ["Eq(%d + %d, %d)" % (a, b, s), "Eq(%d - %d, %d)" % (s, b, a)],
        }


def _g_sub_multi():
    pairs = [(7214, 2865), (8532, 3697), (6041, 2758), (9375, 4816),
             (5620, 1943), (8107, 2549), (7463, 3875), (6208, 1764),
             (9541, 3687), (4302, 1859), (8756, 2938), (7019, 3486),
             (6483, 2597), (9260, 4738), (5814, 2967), (8395, 1648),
             (7602, 3859), (6137, 2478), (9048, 5163), (4726, 1938),
             (8271, 3594), (7350, 2687), (6904, 1758), (9613, 4826),
             (5187, 2439), (8460, 3795), (7038, 2149), (6572, 3894),
             (9204, 5637), (4815, 1976), (8143, 2568), (7690, 3847),
             (6329, 1785), (9476, 2938), (5061, 2374), (8728, 4859)]
    for a, b in pairs:
        d = a - b
        yield {
            "statement": "$%s - %s =$" % (money(a), money(b)),
            "correct": M(d),
            "dvals": [M(d + 100), M(d - 10), M(a + b)],
            "explanation": ("Subtract place by place, regrouping where the top digit "
                            "is smaller: $%s$. Add back to check: $%s + %s = %s$."
                            % (money(d), money(d), money(b), money(a))),
            "check": ["Eq(%d - %d, %d)" % (a, b, d), "Eq(%d + %d, %d)" % (d, b, a)],
        }


def _g_missing_part():
    pairs = [(2345, 7001), (1876, 5432), (3094, 8215), (4567, 9013),
             (2718, 6305), (3852, 7194), (1469, 5028), (5231, 8607),
             (2984, 6152), (3576, 9048), (1735, 4293), (4820, 9165),
             (2607, 7384), (3149, 8026), (5478, 9231), (1892, 6047),
             (3265, 7810), (4703, 9584), (2158, 6936), (3947, 8253),
             (1524, 5079), (4386, 9142), (2790, 7635), (3018, 8471),
             (5642, 9308), (1963, 6284), (3475, 7096), (4209, 8853),
             (2836, 7541), (3691, 9027), (1408, 5762), (4957, 9384),
             (2273, 6819), (3580, 8146), (1746, 5093), (4128, 9675)]
    for b, c in pairs:
        a = c - b
        yield {
            "statement": "$\\square + %s = %s$. What belongs in the box?" % (money(b), money(c)),
            "correct": M(a),
            "dvals": [M(c + b), M(a + 100), M(a - 10)],
            "explanation": ("A missing part is found by subtracting the known part "
                            "from the whole: $%s - %s = %s$. Check: $%s + %s = %s$."
                            % (money(c), money(b), money(a), money(a), money(b), money(c))),
            "check": ["Eq(%d + %d, %d)" % (a, b, c), "Eq(%d - %d, %d)" % (c, b, a)],
        }


def _g_two_step_word():
    rows = [(4500, 1250, 380), (6200, 2400, 750), (3800, 1150, 460),
            (7300, 2850, 920), (5100, 1740, 630), (8400, 3260, 540),
            (2900, 1080, 350), (6700, 2530, 810), (4200, 1360, 470),
            (9100, 3480, 720), (5600, 2170, 590), (3400, 1290, 680),
            (7800, 2640, 430), (4900, 1830, 760), (6300, 2410, 880),
            (8200, 3150, 520), (3700, 1460, 690), (5300, 2080, 340),
            (7100, 2790, 610), (4600, 1520, 950), (9400, 3670, 480),
            (2800, 1140, 570), (6900, 2350, 830), (5800, 2260, 390),
            (3200, 1070, 640), (8600, 3390, 750), (4400, 1680, 520),
            (7500, 2940, 660), (5900, 2130, 410), (3600, 1250, 870),
            (8900, 3520, 630), (4100, 1490, 780), (6600, 2580, 450),
            (5400, 1970, 690), (7700, 3080, 360), (9200, 3740, 810)]
    for start, sold, bought in rows:
        end = start - sold + bought
        yield {
            "statement": ("A warehouse holds %s bricks. It sends out %s and then "
                          "receives %s more. How many bricks does it hold now?"
                          % (M(start), M(sold), M(bought))),
            "correct": M(end),
            "dvals": [M(start - sold - bought), M(start + sold - bought), M(start - sold)],
            "explanation": ("Two steps, in order: $%s - %s = %s$, then "
                            "$%s + %s = %s$."
                            % (money(start), money(sold), money(start - sold),
                               money(start - sold), money(bought), money(end))),
            "check": ["Eq(%d - %d, %d)" % (start, sold, start - sold),
                      "Eq(%d + %d, %d)" % (start - sold, bought, end)],
        }


def _g_estimate_difference():
    pairs = [(8214, 2865), (7532, 3197), (9041, 4758), (6375, 1816),
             (8620, 2943), (7107, 3549), (9463, 2875), (6208, 1264),
             (8541, 3687), (7302, 2859), (9756, 4938), (6019, 2486),
             (8483, 3597), (7260, 1738), (9814, 5967), (6395, 2648),
             (8602, 3159), (7137, 2478), (9048, 4163), (6726, 1938),
             (8271, 2594), (7350, 3687), (9904, 5758), (6613, 1826),
             (8187, 3439), (7460, 2795), (9038, 4149), (6572, 2894),
             (8204, 3637), (7815, 2976), (9143, 5568), (6690, 1847),
             (8329, 2785), (7476, 3938), (9061, 4374), (6728, 1859)]
    for a, b in pairs:
        ra = round(a / 1000) * 1000
        rb = round(b / 1000) * 1000
        if a % 1000 == 500 or b % 1000 == 500:
            continue
        est = ra - rb
        if est == a - b or est <= 0:
            continue
        yield {
            "statement": ("Estimate $%s - %s$ by rounding each number to the "
                          "nearest thousand." % (money(a), money(b))),
            "correct": M(est),
            "dvals": [M(a - b), M(est + 1000), M(est - 1000)],
            "explanation": ("$%s$ rounds to $%s$ and $%s$ rounds to $%s$: the "
                            "estimate is $%s$. (Exactly, it is $%s$.)"
                            % (money(a), money(ra), money(b), money(rb),
                               money(est), money(a - b))),
            "check": ["Eq(%d - %d, %d)" % (ra, rb, est),
                      "Abs(%d - %d) <= 500" % (a, ra), "Abs(%d - %d) <= 500" % (b, rb)],
        }


def _g_inverse_check():
    pairs = [(7214, 2865), (8532, 3697), (6041, 2758), (9375, 4816),
             (5620, 1943), (8107, 2549), (7463, 3875), (6208, 1764),
             (9541, 3687), (4302, 1859), (8756, 2938), (7019, 3486),
             (6483, 2597), (9260, 4738), (5814, 2967), (8395, 1648),
             (7602, 3859), (6137, 2478), (9048, 5163), (4726, 1938),
             (8271, 3594), (7350, 2687), (6904, 1758), (9613, 4826),
             (5187, 2439), (8460, 3795), (7038, 2149), (6572, 3894),
             (9204, 5637), (4815, 1976), (8143, 2568), (7690, 3847),
             (6329, 1785), (9476, 2938), (5061, 2374), (8728, 4859)]
    for a, b in pairs:
        d = a - b
        yield {
            "statement": ("Which calculation checks that $%s - %s = %s$?"
                          % (money(a), money(b), money(d))),
            "correct": "$%s + %s$" % (money(d), money(b)),
            "dvals": ["$%s + %s$" % (money(a), money(b)),
                      "$%s - %s$" % (money(d), money(b)),
                      "$%s - %s$" % (money(a), money(b))],
            "explanation": ("Subtraction is undone by addition: put the answer back "
                            "with what was taken away. $%s + %s = %s$, the number "
                            "you started from."
                            % (money(d), money(b), money(a))),
            "check": ["Eq(%d + %d, %d)" % (d, b, a)],
        }


# ==========================================================================
# Unit 3 — Multiplication & Division
# ==========================================================================

def _g_mult_2x1():
    for a in range(13, 99, 2):
        for b in (3, 4, 6, 7, 8, 9):
            p = a * b
            wrong_partial = b * ((a // 10) + (a % 10))
            if wrong_partial == p:
                continue
            yield {
                "statement": "$%d \\times %d =$" % (a, b),
                "correct": p,
                "dvals": [p - a, p + b, wrong_partial],
                "explanation": ("Split by place: $%d \\times %d = %d$ and "
                                "$%d \\times %d = %d$, so $%d + %d = %d$."
                                % (a // 10 * 10, b, a // 10 * 10 * b, a % 10, b,
                                   (a % 10) * b, a // 10 * 10 * b, (a % 10) * b, p)),
                "check": ["Eq(%d*%d, %d)" % (a, b, p),
                          "Eq(%d*%d + %d*%d, %d)" % (a // 10 * 10, b, a % 10, b, p)],
            }


def _g_mult_2x2():
    for a in range(12, 60, 4):
        for b in range(13, 45, 3):
            p = a * b
            tens_only = (a // 10 * 10) * (b // 10 * 10) + (a % 10) * (b % 10)
            if tens_only == p:
                continue
            yield {
                "statement": "$%d \\times %d =$" % (a, b),
                "correct": M(p),
                "dvals": [M(tens_only), M(p - 100), M(p + 10)],
                "explanation": ("Break the second factor: $%d \\times %d = %d$ and "
                                "$%d \\times %d = %d$; together $%d$."
                                % (a, b // 10 * 10, a * (b // 10 * 10), a, b % 10,
                                   a * (b % 10), p)),
                "check": ["Eq(%d*%d, %d)" % (a, b, p),
                          "Eq(%d*%d + %d*%d, %d)" % (a, b // 10 * 10, a, b % 10, p)],
            }


def _g_divide_exact():
    for d in (3, 4, 6, 7, 8, 9, 12):
        for q in range(13, 45, 3):
            n = q * d
            if q in (d + 1, d - 1, d):
                continue
            yield {
                "statement": "$%s \\div %d =$" % (money(n), d),
                "correct": q,
                "dvals": [q + 1, q - 1, d],
                "explanation": ("Ask how many $%d$s fit in $%s$: exactly $%d$, "
                                "because $%d \\times %d = %s$."
                                % (d, money(n), q, q, d, money(n))),
                "check": ["Eq(%d*%d, %d)" % (q, d, n), "Eq(Rational(%d, %d), %d)" % (n, d, q)],
            }


def _g_divide_remainder():
    for d in (3, 4, 6, 7, 8, 9):
        for q in range(14, 50, 4):
            for r in (1, 2, 3):
                if r >= d:
                    continue
                n = q * d + r
                bad_r = d + r                      # a remainder too big to be legal
                yield {
                    "statement": "Divide: $%s \\div %d$. Give the quotient and remainder."
                                 % (money(n), d),
                    "correct": "$%d$ remainder $%d$" % (q, r),
                    "dvals": ["$%d$ remainder $%d$" % (q, r + 1),
                              "$%d$ remainder $%d$" % (q - 1, bad_r),
                              "$%d$ remainder $%d$" % (q + 1, r)],
                    "explanation": ("$%d \\times %d = %s$, and $%s - %s = %d$ is left "
                                    "over. The remainder must be smaller than $%d$, "
                                    "which $%d$ is."
                                    % (q, d, money(q * d), money(n), money(q * d), r, d, r)),
                    "check": ["Eq(%d*%d + %d, %d)" % (q, d, r, n), "%d < %d" % (r, d)],
                }


def _g_distributive_split():
    for a in (3, 4, 6, 7, 8, 9):
        for b in range(23, 99, 7):
            tens, ones = b // 10 * 10, b % 10
            if ones == 0:
                continue
            yield {
                "statement": "Which split makes $%d \\times %d$ easier to work out?" % (a, b),
                "correct": "$%d \\times %d + %d \\times %d$" % (a, tens, a, ones),
                "dvals": ["$%d \\times %d + %d$" % (a, tens, ones),
                          "$%d \\times %d + %d \\times %d$" % (a, tens // 10, a, ones),
                          "$%d + %d \\times %d$" % (a, tens, ones)],
                "explanation": ("Split the second factor by place and multiply both "
                                "parts: $%d \\times %d + %d \\times %d = %d + %d = %d$."
                                % (a, tens, a, ones, a * tens, a * ones, a * b)),
                "check": ["Eq(%d*%d + %d*%d, %d*%d)" % (a, tens, a, ones, a, b)],
            }


def _g_interpret_remainder():
    rows = [(100, 8, "children", "bus", "buses"), (125, 6, "boxes", "shelf", "shelves"),
            (94, 7, "guests", "table", "tables"), (150, 9, "books", "crate", "crates"),
            (83, 5, "sheep", "pen", "pens"), (167, 12, "eggs", "carton", "cartons"),
            (119, 8, "chairs", "row", "rows"), (142, 9, "apples", "basket", "baskets"),
            (77, 6, "tents", "truck", "trucks"), (188, 15, "bottles", "case", "cases"),
            (134, 7, "students", "van", "vans"), (96, 9, "cakes", "tray", "trays"),
            (155, 12, "pencils", "pack", "packs"), (108, 7, "visitors", "car", "cars"),
            (173, 10, "bricks", "pallet", "pallets"), (89, 6, "lambs", "trailer", "trailers"),
            (146, 8, "plates", "box", "boxes"), (127, 9, "flags", "bundle", "bundles"),
            (164, 11, "seedlings", "tray", "trays"), (91, 4, "chairs", "stack", "stacks"),
            (138, 6, "melons", "crate", "crates"), (117, 5, "jars", "carton", "cartons"),
            (182, 12, "tiles", "box", "boxes"), (105, 8, "cups", "rack", "racks"),
            (159, 7, "logs", "cart", "carts"), (123, 10, "sacks", "trolley", "trolleys"),
            (176, 9, "posters", "tube", "tubes"), (98, 7, "coats", "rail", "rails"),
            (145, 11, "bowls", "crate", "crates"), (112, 6, "hats", "shelf", "shelves"),
            (168, 13, "candles", "box", "boxes"), (87, 5, "goats", "pen", "pens"),
            (152, 9, "loaves", "basket", "baskets"), (129, 8, "cans", "tray", "trays"),
            (191, 14, "planks", "bundle", "bundles"), (104, 6, "mugs", "crate", "crates")]
    for total, cap, thing, one, many in rows:
        q, r = divmod(total, cap)
        if r == 0:
            continue
        need = q + 1
        yield {
            "statement": ("Each %s holds $%d$ %s. How many %s are needed for $%d$ %s?"
                          % (one, cap, thing, many, total, thing)),
            "correct": need,
            "dvals": [q, cap, need + 1],
            "explanation": ("$%d \\div %d = %d$ remainder $%d$. Those last $%d$ still "
                            "need somewhere to go, so one more is required: $%d$."
                            % (total, cap, q, r, r, need)),
            "check": ["Eq(%d*%d + %d, %d)" % (q, cap, r, total), "%d < %d" % (r, cap),
                      "Eq(%d + 1, %d)" % (q, need), "%d*%d >= %d" % (need, cap, total)],
        }


# ==========================================================================
# Unit 4 — Fractions
# ==========================================================================

def _g_equivalent_numerator():
    base = [(2, 3), (3, 4), (1, 5), (5, 6), (3, 8), (2, 5), (4, 7), (5, 9),
            (1, 6), (7, 10), (3, 5), (2, 9), (5, 8), (4, 9), (1, 4), (7, 12)]
    for n, d in base:
        for k in (2, 3, 4):
            nd, nn = d * k, n * k
            yield {
                "statement": ("Fill the gap: $\\frac{%d}{%d} = \\frac{\\square}{%d}$"
                              % (n, d, nd)),
                "correct": nn,
                "dvals": [n + k, n * (k + 1), nd - n],
                "explanation": ("The denominator was multiplied by $%d$, so the "
                                "numerator must be too: $%d \\times %d = %d$. Both "
                                "fractions name the same amount."
                                % (k, n, k, nn)),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (nn, nd, n, d)],
            }


def _g_simplify():
    base = [(2, 3), (3, 4), (4, 5), (5, 6), (3, 8), (2, 7), (5, 9), (7, 10),
            (3, 5), (4, 9), (5, 8), (1, 6), (7, 12), (2, 9), (5, 12), (3, 10)]
    for p, q in base:
        for k in (2, 3, 4):
            n, d = p * k, q * k
            yield {
                "statement": "Write $\\frac{%d}{%d}$ in its simplest form." % (n, d),
                "correct": Rational(p, q),
                "dvals": [Rational(p + 1, q), Rational(p, q + 1), Rational(n, d - k)],
                "explanation": ("Both parts share the factor $%d$: $%d \\div %d = %d$ "
                                "and $%d \\div %d = %d$, giving $\\frac{%d}{%d}$."
                                % (k, n, k, p, d, k, q, p, q)),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (n, d, p, q),
                          "Eq(gcd(%d, %d), 1)" % (p, q)],
            }


def _g_largest_fraction():
    groups = [
        [(3, 4), (2, 3), (5, 8), (7, 12)], [(4, 5), (3, 4), (7, 10), (5, 8)],
        [(5, 6), (3, 4), (7, 9), (11, 15)], [(2, 3), (5, 9), (7, 12), (1, 2)],
        [(7, 8), (5, 6), (4, 5), (9, 11)], [(3, 5), (5, 9), (7, 15), (1, 2)],
        [(5, 7), (2, 3), (7, 11), (3, 5)], [(9, 10), (7, 8), (5, 6), (11, 13)],
        [(4, 7), (1, 2), (5, 11), (3, 7)], [(7, 10), (2, 3), (5, 8), (3, 5)],
        [(5, 12), (1, 3), (3, 8), (2, 7)], [(8, 9), (5, 6), (7, 9), (4, 5)],
        [(3, 8), (1, 3), (2, 7), (1, 4)], [(6, 7), (5, 6), (7, 9), (9, 11)],
        [(4, 9), (2, 5), (3, 8), (5, 13)], [(7, 12), (1, 2), (5, 9), (4, 9)],
        [(9, 14), (3, 5), (5, 9), (7, 13)], [(11, 12), (7, 8), (9, 11), (5, 6)],
        [(2, 9), (1, 5), (3, 14), (1, 6)], [(5, 11), (2, 5), (3, 8), (4, 11)],
        [(8, 11), (2, 3), (7, 11), (5, 8)], [(3, 7), (2, 5), (5, 13), (1, 3)],
        [(9, 13), (2, 3), (7, 11), (5, 9)], [(7, 16), (2, 5), (3, 8), (5, 14)],
        [(5, 14), (1, 3), (3, 10), (2, 7)], [(11, 15), (7, 10), (2, 3), (5, 8)],
        [(4, 11), (1, 3), (3, 10), (2, 7)], [(13, 15), (5, 6), (7, 9), (9, 11)],
        [(3, 11), (1, 4), (2, 9), (1, 5)], [(9, 16), (1, 2), (4, 9), (5, 12)],
    ]
    for g in groups:
        vals = [Rational(n, d) for n, d in g]
        if len(set(vals)) != 4:
            continue
        top = max(vals)
        rest = [v for v in vals if v != top]
        yield {
            "statement": ("Which of $%s$ is the largest?"
                          % "$, $".join(fmt(v) for v in vals)),
            "correct": top,
            "dvals": rest,
            "explanation": ("Compare against a common size (a common denominator, or "
                            "how far each is from $1$): $%s$ is the biggest of the four."
                            % fmt(top)),
            "check": ["Rational(%d, %d) > Rational(%d, %d)" % (top.p, top.q, v.p, v.q)
                      for v in rest],
        }


def _g_add_like():
    for d in (5, 6, 7, 8, 9, 10, 12):
        for a in range(1, d):
            for b in range(1, d):
                if a + b > d + 3 or a > b:
                    continue
                s = Rational(a + b, d)
                if s == Rational(a * b, d):
                    continue
                yield {
                    "statement": "$\\frac{%d}{%d} + \\frac{%d}{%d} =$" % (a, d, b, d),
                    "correct": s,
                    "dvals": [Rational(a + b, 2 * d), Rational(a * b, d), Rational(a + b + 1, d)],
                    "explanation": ("The pieces are already the same size, so count "
                                    "them: $%d + %d = %d$ of the $%d$-sized pieces, "
                                    "which is $%s$." % (a, b, a + b, d, fmt(s))),
                    "check": ["Eq(Rational(%d, %d) + Rational(%d, %d), Rational(%d, %d))"
                              % (a, d, b, d, a + b, d)],
                }


def _g_improper_to_mixed():
    for d in (3, 4, 5, 6, 7, 8, 9):
        for w in (2, 3, 4):
            for r in range(1, d):
                if r > 3:
                    continue
                n = w * d + r
                yield {
                    "statement": "Write $\\frac{%d}{%d}$ as a mixed number." % (n, d),
                    "correct": "$%d\\frac{%d}{%d}$" % (w, r, d),
                    "dvals": ["$%d\\frac{%d}{%d}$" % (r, w, d),
                              "$%d\\frac{%d}{%d}$" % (w, r + 1, d),
                              "$%d\\frac{%d}{%d}$" % (w + 1, r, d)],
                    "explanation": ("How many whole lots of $\\frac{%d}{%d}$ hide in "
                                    "$\\frac{%d}{%d}$? $%d \\div %d = %d$ remainder "
                                    "$%d$, so $%d$ wholes and $\\frac{%d}{%d}$ left."
                                    % (d, d, n, d, n, d, w, r, w, r, d)),
                    "check": ["Eq(%d + Rational(%d, %d), Rational(%d, %d))" % (w, r, d, n, d),
                              "%d < %d" % (r, d)],
                }


def _g_fraction_of_quantity():
    for d in (3, 4, 5, 6, 8):
        for n in range(1, d):
            for unit in (12, 20, 24, 36, 40, 48, 60, 72):
                if unit % d != 0:
                    continue
                part = unit // d * n
                if part == unit or 2 * n == d:      # halves make two options equal
                    continue
                yield {
                    "statement": ("A crate holds $%d$ apples. How many are "
                                  "$\\frac{%d}{%d}$ of them?" % (unit, n, d)),
                    "correct": part,
                    "dvals": [unit - part, part + unit // d, unit + part],
                    "explanation": ("Split into $%d$ equal groups: $%d \\div %d = %d$ "
                                    "in each. Then take $%d$ of them: "
                                    "$%d \\times %d = %d$."
                                    % (d, unit, d, unit // d, n, n, unit // d, part)),
                    "check": ["Eq(Rational(%d, %d)*%d, %d)" % (n, d, unit, part),
                              "Eq(Rational(%d, %d), %d)" % (unit, d, unit // d)],
                }


# ==========================================================================
# Unit 5 — Decimals
# ==========================================================================

def _g_decimal_digit_value():
    for w in (3, 5, 6, 7, 8):
        for t in (2, 3, 4, 6, 7):
            for h in (1, 4, 5, 8, 9):
                if t == h:
                    continue
                n = "%d.%d%d" % (w, t, h)
                yield {
                    "statement": "In $%s$, what is the digit $%d$ worth?" % (n, h),
                    "correct": D(Rational(h, 100)),
                    "dvals": [D(Rational(h, 10)), "$%d$" % h, D(Rational(h, 1000))],
                    "explanation": ("It sits in the hundredths place — the second "
                                    "column after the point — so it is worth "
                                    "$\\frac{%d}{100} = %s$." % (h, dec(Rational(h, 100)))),
                    "check": ["Eq(%s, %d + Rational(%d, 10) + Rational(%d, 100))"
                              % (rat_of(n), w, t, h)],
                }


def _g_decimal_as_fraction():
    vals = [(35, 100), (6, 10), (75, 100), (4, 10), (25, 100), (8, 10),
            (45, 100), (2, 10), (95, 100), (5, 10), (15, 100), (12, 100),
            (64, 100), (85, 100), (36, 100), (55, 100), (24, 100), (48, 100),
            (7, 10), (9, 10), (18, 100), (32, 100), (65, 100), (44, 100),
            (56, 100), (72, 100), (28, 100), (92, 100), (16, 100), (84, 100)]
    for p, q in vals:
        r = Rational(p, q)
        yield {
            "statement": ("Write $%s$ as a fraction in its simplest form."
                          % dec(r)),
            "correct": "$\\frac{%d}{%d}$" % (r.p, r.q),
            "dvals": ["$\\frac{%d}{%d}$" % (p, q),
                      "$\\frac{%d}{%d}$" % (p, q * 10),
                      "$\\frac{%d}{%d}$" % (r.p + 1, r.q)],
            "explanation": ("Read the place: $%s$ is $\\frac{%d}{%d}$, and dividing "
                            "both parts by their common factor gives "
                            "$\\frac{%d}{%d}$." % (dec(r), p, q, r.p, r.q)),
            "check": ["Eq(Rational(%d, %d), Rational(%d, %d))" % (p, q, r.p, r.q),
                      "Eq(gcd(%d, %d), 1)" % (r.p, r.q)],
        }


def _g_compare_decimals():
    groups = [
        ["0.7", "0.68", "0.075", "0.607"], ["0.5", "0.45", "0.409", "0.049"],
        ["0.9", "0.89", "0.098", "0.809"], ["0.6", "0.58", "0.065", "0.506"],
        ["0.8", "0.78", "0.087", "0.708"], ["0.4", "0.38", "0.045", "0.304"],
        ["0.35", "0.3", "0.309", "0.295"], ["0.62", "0.6", "0.596", "0.206"],
        ["0.74", "0.7", "0.698", "0.407"], ["0.83", "0.8", "0.799", "0.308"],
        ["0.56", "0.5", "0.499", "0.065"], ["0.91", "0.9", "0.889", "0.109"],
        ["0.47", "0.4", "0.399", "0.074"], ["0.28", "0.2", "0.198", "0.082"],
        ["0.65", "0.6", "0.599", "0.056"], ["0.39", "0.3", "0.298", "0.093"],
        ["1.5", "1.45", "1.405", "0.95"], ["2.3", "2.25", "2.075", "1.9"],
        ["3.6", "3.55", "3.09", "2.95"], ["1.8", "1.75", "1.099", "0.98"],
        ["4.2", "4.15", "4.075", "3.9"], ["2.7", "2.65", "2.089", "1.97"],
        ["5.1", "5.05", "5.009", "4.9"], ["3.4", "3.35", "3.049", "2.94"],
        ["0.25", "0.2", "0.199", "0.052"], ["0.72", "0.7", "0.699", "0.27"],
        ["0.53", "0.5", "0.489", "0.35"], ["0.86", "0.8", "0.795", "0.68"],
        ["0.94", "0.9", "0.899", "0.49"], ["0.41", "0.4", "0.395", "0.14"],
    ]
    for g in groups:
        vals = [Rational(rat_of(s).split("(")[1].split(",")[0],
                         rat_of(s).split(",")[1].strip(" )")) if "." in s else Rational(s)
                for s in g]
        if len(set(vals)) != 4:
            continue
        top = max(vals)
        idx = vals.index(top)
        rest = [g[i] for i in range(4) if i != idx]
        yield {
            "statement": ("Which of $%s$ is the largest?" % "$, $".join(g)),
            "correct": "$%s$" % g[idx],
            "dvals": ["$%s$" % s for s in rest],
            "explanation": ("Compare place by place from the left, not by how many "
                            "digits are written: $%s$ is the biggest. A longer "
                            "decimal is not a bigger one." % g[idx]),
            "check": ["%s > %s" % (rat_of(g[idx]), rat_of(s)) for s in rest],
        }


def _g_add_sub_decimals():
    rows = [("4.7", "2.85", "+"), ("6.3", "1.45", "+"), ("5.6", "3.75", "+"),
            ("2.9", "4.35", "+"), ("7.2", "1.85", "+"), ("3.4", "2.95", "+"),
            ("8.1", "0.65", "+"), ("5.3", "3.45", "+"), ("6.7", "2.55", "+"),
            ("4.2", "3.85", "+"), ("9.4", "0.75", "+"), ("3.8", "1.65", "+"),
            ("7.5", "2.25", "+"), ("2.6", "5.45", "+"), ("6.1", "3.35", "+"),
            ("8.3", "0.95", "+"), ("5.2", "1.35", "-"), ("7.4", "2.65", "-"),
            ("6.1", "3.45", "-"), ("9.3", "4.75", "-"), ("8.2", "1.55", "-"),
            ("4.6", "2.85", "-"), ("7.1", "3.25", "-"), ("5.4", "1.95", "-"),
            ("9.2", "5.65", "-"), ("6.3", "2.45", "-"), ("8.5", "3.75", "-"),
            ("7.6", "4.35", "-"), ("5.1", "2.55", "-"), ("9.4", "6.85", "-"),
            ("6.2", "1.75", "-"), ("8.4", "5.95", "-")]
    for a, b, op in rows:
        ra, rb = eval_rat(a), eval_rat(b)
        res = ra + rb if op == "+" else ra - rb
        if res <= 0:
            continue
        yield {
            "statement": "$%s %s %s =$" % (a, op, b),
            "correct": D(res),
            "dvals": [D(res + Rational(1, 2)), D(res - Rational(1, 10)), D(res * 10)],
            "explanation": ("Line up the points (write $%s$ as $%s$ if it helps), then "
                            "work column by column: the answer is $%s$."
                            % (a, dec(ra), dec(res))),
            "check": ["Eq(%s %s %s, %s)" % (rat_of(a), op, rat_of(b), rat_of(dec(res)))],
        }


def eval_rat(s):
    """Exact Rational from a decimal string — never float()."""
    if "." not in s:
        return Rational(int(s))
    whole, frac = s.split(".")
    return Rational(int(whole + frac), 10 ** len(frac))


def _g_round_decimals():
    vals = ["6.348", "2.751", "8.164", "4.926", "3.472", "7.238", "5.681",
            "9.317", "1.845", "6.593", "2.164", "8.729", "4.351", "7.916",
            "3.284", "5.437", "9.652", "1.378", "6.721", "2.593", "8.146",
            "4.867", "7.319", "3.752", "5.284", "9.431", "1.968", "6.235",
            "2.847", "8.514", "4.193", "7.628"]
    for s in vals:
        v = eval_rat(s)
        tenths = int(str(s).split(".")[1][0])
        hundredths = int(str(s).split(".")[1][1])
        whole = int(s.split(".")[0])
        down = whole + Rational(tenths, 10)
        up = down + Rational(1, 10)
        if hundredths == 5:
            continue
        correct = up if hundredths > 5 else down
        other = down if correct == up else up
        yield {
            "statement": "Round $%s$ to one decimal place (the nearest tenth)." % s,
            "correct": D(correct),
            "dvals": [D(other), "$%s$" % s, "$%d$" % whole],
            "explanation": ("$%s$ lies between $%s$ and $%s$; the hundredths digit is "
                            "$%d$, so it is nearer $%s$."
                            % (s, dec(down), dec(up), hundredths, dec(correct))),
            "check": ["Abs(%s - %s) < Abs(%s - %s)"
                      % (rat_of(s), rat_of(dec(correct)), rat_of(s), rat_of(dec(other)))],
        }


def _g_money_total():
    rows = [(3, 2500, 2, 800), (4, 1200, 3, 950), (2, 3500, 5, 400),
            (5, 1800, 2, 1250), (3, 4200, 4, 650), (6, 900, 3, 1400),
            (2, 6500, 4, 750), (4, 2300, 5, 600), (3, 3800, 2, 1150),
            (5, 1600, 3, 850), (2, 4900, 6, 500), (4, 2700, 3, 1050),
            (3, 5400, 2, 950), (6, 1300, 4, 700), (2, 7200, 3, 1100),
            (5, 2100, 4, 550), (3, 3300, 5, 800), (4, 1900, 2, 1350),
            (2, 5800, 5, 450), (6, 1500, 3, 1250), (3, 4600, 4, 600),
            (5, 2400, 2, 1450), (4, 3100, 6, 350), (2, 6800, 4, 900),
            (3, 2900, 3, 1150), (6, 1700, 5, 500), (4, 3600, 3, 750),
            (5, 2800, 2, 1550), (2, 8100, 4, 650), (3, 5100, 6, 400)]
    for qa, pa, qb, pb in rows:
        total = qa * pa + qb * pb
        yield {
            "statement": ("A student buys $%d$ notebooks at %s tögrög each and $%d$ "
                          "pens at %s tögrög each. What is the total cost, in tögrög?"
                          % (qa, M(pa), qb, M(pb))),
            "correct": M(total),
            "dvals": [M(qa * pa), M(total - qb * pb + pb), M((qa + qb) * pa)],
            "explanation": ("Notebooks: $%d \\times %s = %s$. Pens: "
                            "$%d \\times %s = %s$. Together $%s$ tögrög."
                            % (qa, money(pa), money(qa * pa), qb, money(pb),
                               money(qb * pb), money(total))),
            "check": ["Eq(%d*%d + %d*%d, %d)" % (qa, pa, qb, pb, total)],
        }


# ==========================================================================
# Unit 6 — Measurement & Units
# ==========================================================================

LADDER = [("km", "m", 1000), ("m", "cm", 100), ("cm", "mm", 10), ("m", "mm", 1000)]


def _g_convert_length():
    for big, small, k in LADDER:
        for n in (3, 5, 7, 9, 12, 15, 24, 40, 60):
            v = n * k
            yield {
                "statement": "$%d$ %s $=$ how many %s?" % (n, big, small),
                "correct": M(v),
                "dvals": [M(n * k * 10), M(n * k // 10 if k > 10 else n * 100), M(n)],
                "explanation": ("One %s is $%s$ %s, so $%d \\times %s = %s$. Changing "
                                "to a smaller unit always gives a bigger number."
                                % (big, money(k), small, n, money(k), money(v))),
                "check": ["Eq(%d*%d, %d)" % (n, k, v)],
            }


def _g_convert_mass_capacity():
    ladders = [("kg", "g", 1000), ("l", "ml", 1000), ("t", "kg", 1000)]
    for big, small, k in ladders:
        for n in (2, 3, 4, 6, 8, 12, 15, 25, 40, 75):
            v = n * k
            yield {
                "statement": "$%d$ %s $=$ how many %s?" % (n, big, small),
                "correct": M(v),
                "dvals": [M(n * 100), M(n * k * 10), M(n)],
                "explanation": ("The step from %s to %s is $\\times %s$: "
                                "$%d \\times %s = %s$."
                                % (big, small, money(k), n, money(k), money(v))),
                "check": ["Eq(%d*%d, %d)" % (n, k, v)],
            }
    for big, small, k in ladders:
        for n in (2, 3, 5, 7, 9, 14, 20):
            v = n * k
            yield {
                "statement": "$%s$ %s $=$ how many %s?" % (money(v), small, big),
                "correct": M(n),
                "dvals": [M(v), M(n * 10), M(v // 100)],
                "explanation": ("Going up a ladder step divides: $%s \\div %s = %d$ %s."
                                % (money(v), money(k), n, big)),
                "check": ["Eq(Rational(%d, %d), %d)" % (v, k, n)],
            }


def _g_time_convert():
    for h in range(1, 9):
        for m in (5, 15, 20, 25, 35, 40, 50, 55):
            total = h * 60 + m
            yield {
                "statement": "How many minutes are there in $%d$ h $%d$ min?" % (h, m),
                "correct": total,
                "dvals": [h * 100 + m, h * 60, total + 60],
                "explanation": ("An hour is $60$ minutes, not $100$: "
                                "$%d \\times 60 = %d$, and $%d + %d = %d$."
                                % (h, h * 60, h * 60, m, total)),
                "check": ["Eq(%d*60 + %d, %d)" % (h, m, total)],
            }


def _g_elapsed_time():
    starts = [(9, 15), (10, 40), (13, 25), (14, 35), (7, 50), (11, 5),
              (15, 20), (8, 45), (16, 10), (12, 30), (17, 55), (6, 25),
              (18, 40), (9, 35), (13, 50), (10, 15)]
    lasts = [(1, 50), (2, 25), (0, 45)]
    for (sh, sm) in starts:
        for (lh, lm) in lasts:
            total = sh * 60 + sm + lh * 60 + lm
            if total >= 24 * 60:
                continue
            eh, em = divmod(total, 60)
            yield {
                "statement": ("A programme starts at %02d:%02d and lasts %d h %d min. "
                              "When does it end?" % (sh, sm, lh, lm)),
                "correct": "%02d:%02d" % (eh, em),
                "dvals": ["%02d:%02d" % ((eh + 1) % 24, em),
                          "%02d:%02d" % (eh, (em + 15) % 60),
                          "%02d:%02d" % ((sh + lh) % 24, (sm + lm) % 60 if sm + lm < 60 else (sm + lm) - 60)],
                "explanation": ("Add the hours, then the minutes, carrying an hour "
                                "whenever the minutes pass $60$: %02d:%02d plus "
                                "%d h %d min lands on %02d:%02d."
                                % (sh, sm, lh, lm, eh, em)),
                "check": ["Eq(%d*60 + %d + %d*60 + %d, %d*60 + %d)"
                          % (sh, sm, lh, lm, eh, em), "%d < 60" % em],
            }


def _g_compare_measures():
    groups = [
        [(2500, "mm"), (240, "cm"), (2, "m"), (1, "m")],
        [(3, "m"), (250, "cm"), (2800, "mm"), (29, "cm")],
        [(1500, "m"), (2, "km"), (900, "m"), (1, "km")],
        [(4000, "g"), (3, "kg"), (500, "g"), (2, "kg")],
        [(2, "l"), (1500, "ml"), (900, "ml"), (1, "l")],
        [(750, "cm"), (7, "m"), (6900, "mm"), (5, "m")],
        [(3, "kg"), (2500, "g"), (2, "kg"), (900, "g")],
        [(5, "km"), (4500, "m"), (3, "km"), (2900, "m")],
        [(120, "cm"), (1, "m"), (900, "mm"), (80, "cm")],
        [(6, "l"), (5500, "ml"), (4, "l"), (3900, "ml")],
        [(8, "m"), (790, "cm"), (7500, "mm"), (6, "m")],
        [(9, "kg"), (8500, "g"), (7, "kg"), (6900, "g")],
        [(450, "cm"), (4, "m"), (3900, "mm"), (3, "m")],
        [(2, "t"), (1500, "kg"), (900, "kg"), (1, "t")],
        [(650, "ml"), (Rational(1, 2), "l"), (490, "ml"), (400, "ml")],
        [(15, "m"), (1400, "cm"), (13000, "mm"), (12, "m")],
        [(7, "km"), (6500, "m"), (5, "km"), (4900, "m")],
        [(340, "cm"), (3, "m"), (2900, "mm"), (2, "m")],
        [(5, "kg"), (4500, "g"), (3, "kg"), (2900, "g")],
        [(11, "l"), (10500, "ml"), (9, "l"), (8900, "ml")],
        [(280, "cm"), (2, "m"), (1900, "mm"), (1, "m")],
        [(4, "t"), (3500, "kg"), (2, "t"), (1900, "kg")],
        [(18, "m"), (1700, "cm"), (16000, "mm"), (15, "m")],
        [(950, "g"), (Rational(9, 10), "kg"), (890, "g"), (800, "g")],
        [(6, "km"), (5900, "m"), (5, "km"), (4800, "m")],
        [(72, "cm"), (Rational(7, 10), "m"), (690, "mm"), (60, "cm")],
        [(13, "kg"), (12500, "g"), (11, "kg"), (10900, "g")],
        [(3, "l"), (2900, "ml"), (2, "l"), (1900, "ml")],
        [(24, "m"), (2300, "cm"), (22000, "mm"), (21, "m")],
        [(880, "mm"), (87, "cm"), (Rational(8, 10), "m"), (79, "cm")],
    ]
    to_mm = {"mm": 1, "cm": 10, "m": 1000, "km": 1000000,
             "g": 1, "kg": 1000, "t": 1000000, "ml": 1, "l": 1000}
    for g in groups:
        vals = [Rational(v) * to_mm[u] for v, u in g]
        if len(set(vals)) != 4:
            continue
        top = max(vals)
        idx = vals.index(top)
        rest = [i for i in range(4) if i != idx]

        def label(i):
            v, u = g[i]
            return "$%s$ %s" % (fmt(v) if Rational(v).q != 1 else money(int(v)), u)

        yield {
            "statement": ("Which is the largest measurement: %s?"
                          % ", ".join(label(i) for i in range(4))),
            "correct": label(idx),
            "dvals": [label(i) for i in rest],
            "explanation": ("Convert them all to one unit before comparing — bare "
                            "numbers lie, because each is counting a different sized "
                            "step. In the smallest unit here, %s is the biggest of "
                            "the four." % label(idx)),
            "check": ["Rational(%d, %d) > Rational(%d, %d)"
                      % (top.p, top.q, vals[i].p, vals[i].q) for i in rest],
        }


def _g_measurement_word():
    rows = [(5, 40), (6, 45), (8, 50), (4, 30), (9, 60), (7, 55), (10, 80),
            (3, 25), (12, 90), (6, 35), (8, 70), (5, 45), (9, 40), (7, 60),
            (11, 75), (4, 35), (10, 65), (6, 55), (8, 45), (5, 30),
            (12, 70), (7, 40), (9, 85), (3, 20), (11, 60), (4, 45),
            (10, 55), (6, 25), (8, 35), (5, 65)]
    for metres, piece in rows:
        cm = metres * 100
        q, r = divmod(cm, piece)
        if r == 0:
            continue
        yield {
            "statement": ("A rope $%d$ m long is cut into pieces of $%d$ cm. How many "
                          "whole pieces are there?" % (metres, piece)),
            "correct": q,
            "dvals": [q + 1, metres, piece],
            "explanation": ("Convert first: $%d$ m $= %s$ cm. Then "
                            "$%s \\div %d = %d$ remainder $%d$ — the leftover $%d$ cm "
                            "is too short to be another piece."
                            % (metres, money(cm), money(cm), piece, q, r, r)),
            "check": ["Eq(%d*100, %d)" % (metres, cm),
                      "Eq(%d*%d + %d, %d)" % (q, piece, r, cm), "%d < %d" % (r, piece)],
        }


# ==========================================================================
# Unit 7 — Geometry
# ==========================================================================

def _g_missing_angle():
    for a in range(20, 160, 5):
        b = 180 - a
        yield {
            "statement": ("Two angles sit side by side on a straight line. One "
                          "measures $%d^\\circ$. How big is the other?" % a),
            "correct": b,
            "dvals": [360 - a, 90 - a if a < 90 else a - 90, b + 10],
            "explanation": ("Angles on a straight line total $180^\\circ$: "
                            "$180 - %d = %d^\\circ$." % (a, b)),
            "check": ["Eq(180 - %d, %d)" % (a, b), "Eq(%d + %d, 180)" % (a, b)],
        }
    for a in range(40, 200, 10):
        for c in (60, 90, 110):
            b = 360 - a - c
            if b <= 0:
                continue
            yield {
                "statement": ("Three angles meet at a point: $%d^\\circ$, $%d^\\circ$ "
                              "and one more. How big is the third?" % (a, c)),
                "correct": b,
                "dvals": [180 - a - c if 180 - a - c > 0 else b + 90, b + 20, a + c],
                "explanation": ("A full turn is $360^\\circ$: "
                                "$360 - %d - %d = %d^\\circ$." % (a, c, b)),
                "check": ["Eq(360 - %d - %d, %d)" % (a, c, b),
                          "Eq(%d + %d + %d, 360)" % (a, c, b)],
            }


def _g_triangle_angle():
    for a in range(25, 110, 5):
        for b in (35, 45, 55, 65, 75):
            c = 180 - a - b
            if c <= 0 or c == a or c == b:
                continue
            yield {
                "statement": ("A triangle has angles of $%d^\\circ$ and $%d^\\circ$. "
                              "Find the third angle." % (a, b)),
                "correct": c,
                "dvals": [360 - a - b, c + 10, a + b],
                "explanation": ("Every triangle's angles total $180^\\circ$: "
                                "$180 - %d - %d = %d^\\circ$. Check: "
                                "$%d + %d + %d = 180$." % (a, b, c, a, b, c)),
                "check": ["Eq(180 - %d - %d, %d)" % (a, b, c),
                          "Eq(%d + %d + %d, 180)" % (a, b, c)],
            }


def _g_perimeter_rect():
    for l in range(6, 30, 2):
        for w in range(3, 20, 3):
            if w >= l:
                continue
            p = 2 * (l + w)
            yield {
                "statement": ("A rectangle measures $%d$ m by $%d$ m. Find its "
                              "perimeter." % (l, w)),
                "correct": p,
                "dvals": [l * w, l + w, 2 * l + w],
                "explanation": ("The walk passes two lengths and two widths: "
                                "$2 \\times (%d + %d) = %d$ m."
                                % (l, w, p)),
                "check": ["Eq(2*(%d + %d), %d)" % (l, w, p),
                          "Eq(%d + %d + %d + %d, %d)" % (l, w, l, w, p)],
            }


def _g_area_rect():
    for l in range(5, 32, 3):
        for w in range(4, 22, 2):
            if w >= l:
                continue
            a = l * w
            yield {
                "statement": ("A rectangle measures $%d$ m by $%d$ m. Find its area."
                              % (l, w)),
                "correct": a,
                "dvals": [2 * (l + w), l + w, a * 2],
                "explanation": ("Area counts the unit squares inside: "
                                "$%d \\times %d = %d$ square metres."
                                % (l, w, a)),
                "check": ["Eq(%d*%d, %d)" % (l, w, a)],
            }


def _g_perimeter_backwards():
    for w in range(3, 18, 2):
        for l in range(w + 2, w + 22, 4):
            p = 2 * (l + w)
            yield {
                "statement": ("A rectangle has a perimeter of $%d$ cm and a width of "
                              "$%d$ cm. How long is it?" % (p, w)),
                "correct": l,
                "dvals": [p - w, p // 2, p // 4],
                "explanation": ("Halve the perimeter to get one length plus one "
                                "width: $%d \\div 2 = %d$. Then $%d - %d = %d$ cm."
                                % (p, p // 2, p // 2, w, l)),
                "check": ["Eq(Rational(%d, 2) - %d, %d)" % (p, w, l),
                          "Eq(2*(%d + %d), %d)" % (l, w, p)],
            }


def _g_composite_area():
    for L in range(8, 20, 2):
        for W in range(5, 13, 2):
            for bl in (2, 3, 4):
                bw = 2
                if bl >= L or bw >= W:
                    continue
                whole = L * W
                bite = bl * bw
                a = whole - bite
                if a == whole or a <= 0:
                    continue
                yield {
                    "statement": ("A $%d$ m by $%d$ m rectangular yard has a $%d$ m by "
                                  "$%d$ m corner cut out of it. What area is left?"
                                  % (L, W, bl, bw)),
                    "correct": a,
                    "dvals": [whole, whole + bite, whole - 2 * bite],
                    "explanation": ("Fill and subtract: the whole rectangle is "
                                    "$%d \\times %d = %d$ m², the bite is "
                                    "$%d \\times %d = %d$ m², so $%d - %d = %d$ m² "
                                    "remain. Splitting the L-shape into two pieces "
                                    "gives the same $%d$."
                                    % (L, W, whole, bl, bw, bite, whole, bite, a, a)),
                    "check": ["Eq(%d*%d - %d*%d, %d)" % (L, W, bl, bw, a),
                              "Eq(%d*%d + (%d - %d)*%d, %d)" % (L, W - bw, L, bl, bw, a)],
                }


# ==========================================================================
# Unit 8 — Data & Graphs
# ==========================================================================

def _g_tally_read():
    for b in range(3, 15):
        for s in range(0, 5):
            n = 5 * b + s
            if s == 0 and b % 2 == 0:
                continue
            yield {
                "statement": ("A tally chart shows $%d$ full bundles of five and $%d$ "
                              "single marks. What is the count?" % (b, s)),
                "correct": n,
                "dvals": [b + s, 5 * b, n + 5],
                "explanation": ("Each bundle is worth five: $5 \\times %d = %d$, plus "
                                "the $%d$ singles makes $%d$." % (b, 5 * b, s, n)),
                "check": ["Eq(5*%d + %d, %d)" % (b, s, n)],
            }


def _g_table_missing():
    rows = [(60, 27, 19, 9), (80, 34, 26, 12), (50, 21, 15, 8),
            (100, 42, 31, 18), (45, 18, 14, 7), (75, 30, 24, 13),
            (90, 38, 27, 16), (65, 26, 20, 11), (120, 50, 38, 21),
            (55, 22, 17, 9), (85, 35, 28, 14), (70, 29, 22, 12),
            (110, 46, 34, 19), (40, 16, 13, 6), (95, 40, 30, 17),
            (105, 44, 33, 20), (48, 19, 15, 8), (78, 32, 25, 13),
            (88, 36, 28, 15), (68, 28, 21, 11), (115, 48, 36, 22),
            (52, 21, 16, 9), (82, 34, 26, 14), (72, 30, 23, 12),
            (125, 52, 40, 23), (44, 18, 14, 7), (92, 38, 29, 16),
            (98, 41, 31, 18), (58, 24, 18, 10), (108, 45, 34, 20)]
    for total, a, b, c in rows:
        d = total - a - b - c
        if d <= 0:
            continue
        yield {
            "statement": ("A frequency table counts $%d$ animals in four rows. Three "
                          "of the rows show $%d$, $%d$ and $%d$. What does the fourth "
                          "row show?" % (total, a, b, c)),
            "correct": d,
            "dvals": [total - a - b, d + 5, a + b + c],
            "explanation": ("The rows must add to the total: "
                            "$%d - %d - %d - %d = %d$. Check: $%d + %d + %d + %d = %d$."
                            % (total, a, b, c, d, a, b, c, d, total)),
            "check": ["Eq(%d - %d - %d - %d, %d)" % (total, a, b, c, d),
                      "Eq(%d + %d + %d + %d, %d)" % (a, b, c, d, total)],
        }


def _g_pictograph():
    for key in (5, 10, 20, 25, 50):
        for sym in range(2, 9):
            for half in (0, 1):
                if half and key % 2:
                    continue
                v = sym * key + (key // 2 if half else 0)
                label = ("$%d$ and a half symbols" % sym) if half else ("$%d$ symbols" % sym)
                yield {
                    "statement": ("A pictograph uses the key 'one symbol $= %d$'. A row "
                                  "of %s stands for what value?" % (key, label)),
                    "correct": v,
                    "dvals": [sym, sym + key, sym * key * 2],
                    "explanation": ("Reading a pictograph multiplies by the key: "
                                    "$%d \\times %d = %s$.%s"
                                    % (sym, key, money(sym * key),
                                       (" Half a symbol carries half the key, another "
                                        "$%d$, giving %s in all." % (key // 2, M(v)))
                                       if half else "")),
                    "check": ["Eq(%d*%d + %d, %d)" % (sym, key, (key // 2 if half else 0), v)],
                }


def _g_bar_scale():
    for step in (5, 10, 20, 25, 50):
        for lines in range(2, 10):
            v = step * lines
            yield {
                "statement": ("On a bar graph the gridlines are marked every $%d$. A "
                              "bar reaches the %s gridline. What value does it show?"
                              % (step, {2: "second", 3: "third", 4: "fourth", 5: "fifth",
                                        6: "sixth", 7: "seventh", 8: "eighth",
                                        9: "ninth"}[lines])),
                "correct": v,
                "dvals": [lines, v + step, step],
                "explanation": ("Each gridline is worth $%d$, so $%d \\times %d = %s$. "
                                "Counting gridlines as ones is the commonest bar-graph "
                                "mistake." % (step, lines, step, money(v))),
                "check": ["Eq(%d*%d, %d)" % (lines, step, v)],
            }


def _g_mean():
    groups = [
        (12, 15, 9, 16), (8, 10, 6, 16), (14, 9, 17, 12), (20, 25, 15, 20),
        (7, 11, 13, 9), (18, 22, 14, 26), (5, 9, 11, 15), (30, 24, 18, 28),
        (13, 17, 21, 9), (6, 14, 10, 18), (25, 15, 35, 25), (11, 19, 13, 17),
        (22, 16, 28, 14), (9, 13, 7, 11), (16, 24, 20, 12), (10, 20, 30, 20),
        (17, 23, 15, 21), (12, 18, 24, 10), (8, 16, 12, 20), (26, 14, 22, 18),
        (15, 21, 27, 9), (19, 11, 23, 15), (7, 15, 9, 13), (28, 20, 24, 16),
        (13, 9, 19, 15), (24, 18, 30, 12), (6, 10, 14, 18), (21, 13, 17, 25),
        (11, 15, 19, 7), (23, 17, 13, 27),
    ]
    for vals in groups:
        total = sum(vals)
        if total % len(vals):
            continue
        m = total // len(vals)
        yield {
            "statement": ("Find the mean of $%d$, $%d$, $%d$ and $%d$."
                          % vals),
            "correct": m,
            "dvals": [total, max(vals) - min(vals), m + 2],
            "explanation": ("Add everything, then share it out equally: "
                            "$%d + %d + %d + %d = %d$, and $%d \\div 4 = %d$. "
                            "Check by multiplying back: $%d \\times 4 = %d$."
                            % (vals[0], vals[1], vals[2], vals[3], total, total, m, m, total)),
            "check": ["Eq(%d + %d + %d + %d, %d)" % (vals + (total,)),
                      "Eq(Rational(%d, 4), %d)" % (total, m),
                      "Eq(%d*4, %d)" % (m, total)],
        }


def _g_range():
    groups = [
        (34, 19, 28, 41), (50, 22, 37, 22), (12, 45, 30, 27), (63, 18, 44, 51),
        (26, 39, 15, 48), (71, 33, 57, 29), (17, 42, 36, 23), (58, 24, 46, 31),
        (85, 47, 62, 39), (13, 29, 21, 35), (94, 56, 73, 48), (28, 16, 43, 37),
        (67, 32, 51, 25), (19, 38, 27, 44), (76, 41, 59, 33), (22, 49, 31, 18),
        (81, 53, 68, 42), (15, 34, 26, 47), (72, 38, 55, 29), (24, 41, 33, 17),
        (89, 52, 66, 45), (11, 27, 19, 36), (78, 43, 61, 35), (25, 48, 32, 21),
        (93, 57, 71, 49), (14, 31, 23, 40), (69, 36, 54, 27), (20, 45, 34, 16),
        (83, 51, 64, 43), (18, 37, 29, 46),
    ]
    for vals in groups:
        r = max(vals) - min(vals)
        yield {
            "statement": ("Find the range of $%d$, $%d$, $%d$ and $%d$." % vals),
            "correct": r,
            "dvals": [max(vals), sum(vals), min(vals)],
            "explanation": ("Range is the spread from smallest to largest: "
                            "$%d - %d = %d$. Everything in between is ignored."
                            % (max(vals), min(vals), r)),
            "check": ["Eq(%d - %d, %d)" % (max(vals), min(vals), r)],
        }


def _g_mean_missing():
    rows = [(18, 4, 14, 20, 19), (12, 4, 9, 13, 15), (20, 5, 18, 22, 17),
            (15, 4, 11, 16, 18), (25, 4, 20, 27, 24), (10, 5, 7, 12, 9),
            (16, 4, 13, 18, 15), (22, 5, 19, 24, 21), (14, 4, 10, 15, 17),
            (30, 4, 26, 32, 29), (11, 5, 8, 13, 10), (19, 4, 15, 21, 20),
            (24, 5, 21, 26, 23), (13, 4, 9, 14, 16), (28, 4, 24, 30, 27),
            (17, 5, 14, 19, 16), (21, 4, 17, 23, 22), (26, 5, 23, 28, 25),
            (12, 4, 8, 14, 13), (23, 4, 19, 25, 24), (18, 5, 15, 20, 17),
            (27, 4, 23, 29, 28), (15, 5, 12, 17, 14), (20, 4, 16, 22, 21),
            (29, 4, 25, 31, 30), (16, 5, 13, 18, 15), (25, 5, 22, 27, 24),
            (14, 4, 10, 16, 15), (31, 4, 27, 33, 32), (19, 5, 16, 21, 18)]
    for mean, count, a, b, c in rows:
        total = mean * count
        known = [a, b, c] if count == 4 else [a, b, c, mean]
        missing = total - sum(known)
        if missing <= 0:
            continue
        yield {
            "statement": ("%d days of readings have a mean of $%d$. %s of them were "
                          "%s. What was the last reading?"
                          % (count, mean, "Three" if count == 4 else "Four",
                             ", ".join("$%d$" % v for v in known))),
            "correct": missing,
            "dvals": [mean, total, sum(known)],
            "explanation": ("Work backwards from the receipt: the total must be "
                            "$%d \\times %d = %d$. The known readings make $%d$, so "
                            "the last is $%d - %d = %d$."
                            % (mean, count, total, sum(known), total, sum(known), missing)),
            "check": ["Eq(%d*%d, %d)" % (mean, count, total),
                      "Eq(%d - %d, %d)" % (total, sum(known), missing),
                      "Eq(Rational(%d, %d), %d)" % (total, count, mean)],
        }


# ==========================================================================
# assembly — one collection per unit
# ==========================================================================

def build():
    forms = []

    U1 = "whole-numbers-and-place-value"
    forms += [
        form("g5-digit-value", "What a digit is worth", 1, U1,
             "A digit's value is the digit times its place — read the column, not the digit.",
             mk_txt("g5-dv", _g_digit_value())),
        form("g5-largest-number", "Comparing large numbers", 1, U1,
             "Same digits, different order: compare place by place from the left.",
             mk_txt("g5-ln", _g_largest_number())),
        form("g5-round-place", "Rounding to a given place", 2, U1,
             "Find the two neighbours, then choose the nearer one.",
             mk_txt("g5-rp", _g_round_place())),
        form("g5-expanded-form", "Expanded form", 2, U1,
             "Every digit contributes its place value; zeros contribute nothing.",
             mk_txt("g5-ef", _g_expanded_form())),
        form("g5-estimate-sum", "Estimating a sum", 2, U1,
             "Round first, then add — an estimate is close, not equal.",
             mk_txt("g5-es", _g_estimate_sum())),
        form("g5-build-largest", "Building the largest number", 3, U1,
             "Biggest digit into the biggest place, and keep going down.",
             mk_txt("g5-bl", _g_build_largest())),
    ]

    U2 = "addition-and-subtraction"
    forms += [
        form("g5-add-multi", "Multi-digit addition", 1, U2,
             "Line up the places, add from the right, carry past nine.",
             mk_txt("g5-am", _g_add_multi())),
        form("g5-sub-multi", "Multi-digit subtraction", 1, U2,
             "Regroup where the top digit is smaller, then check by adding back.",
             mk_txt("g5-sm", _g_sub_multi())),
        form("g5-missing-part", "Finding a missing part", 2, U2,
             "Whole minus the known part — then add back to check.",
             mk_txt("g5-mp", _g_missing_part())),
        form("g5-two-step-word", "Two-step word problems", 2, U2,
             "Do the steps in the order the story tells them.",
             mk_txt("g5-tsw", _g_two_step_word())),
        form("g5-estimate-difference", "Estimating a difference", 2, U2,
             "Round both numbers to the same place before subtracting.",
             mk_txt("g5-ed", _g_estimate_difference())),
        form("g5-inverse-check", "Checking by the inverse", 3, U2,
             "Addition undoes subtraction: answer plus what was taken away.",
             mk_txt("g5-ic", _g_inverse_check())),
    ]

    U3 = "multiplication-and-division"
    forms += [
        form("g5-mult-2x1", "Two-digit by one-digit", 1, U3,
             "Split by place, multiply each part, then add.",
             mk_num("g5-m21", _g_mult_2x1())),
        form("g5-divide-exact", "Division without a remainder", 1, U3,
             "How many of the divisor fit — checked by multiplying back.",
             mk_num("g5-de", _g_divide_exact())),
        form("g5-mult-2x2", "Two-digit by two-digit", 2, U3,
             "Two partial products, both carrying their place value.",
             mk_txt("g5-m22", _g_mult_2x2())),
        form("g5-divide-remainder", "Quotient and remainder", 2, U3,
             "q x d + r = n, and the remainder must be smaller than the divisor.",
             mk_txt("g5-dr", _g_divide_remainder())),
        form("g5-distributive-split", "Splitting a multiplication", 2, U3,
             "Break the second factor by place — BOTH parts get multiplied.",
             mk_txt("g5-ds", _g_distributive_split())),
        form("g5-interpret-remainder", "What the remainder means", 3, U3,
             "Sometimes the leftovers need one more container, sometimes they don't.",
             mk_num("g5-ir", _g_interpret_remainder())),
    ]

    U4 = "fractions-first-steps"
    forms += [
        form("g5-equivalent-numerator", "Equivalent fractions", 1, U4,
             "Multiply top and bottom by the same number and the amount is unchanged.",
             mk_num("g5-eq", _g_equivalent_numerator())),
        form("g5-add-like", "Adding like fractions", 1, U4,
             "Same-sized pieces: count them, keep the denominator.",
             mk_num("g5-al", _g_add_like())),
        form("g5-simplify", "Simplest form", 2, U4,
             "Divide both parts by their common factor until only 1 is shared.",
             mk_num("g5-si", _g_simplify())),
        form("g5-largest-fraction", "Comparing fractions", 2, U4,
             "Common denominators, or distance from one — never bigger numbers.",
             mk_num("g5-lf", _g_largest_fraction())),
        form("g5-improper-to-mixed", "Improper to mixed numbers", 2, U4,
             "Divide: the quotient is the wholes, the remainder stays on top.",
             mk_txt("g5-im", _g_improper_to_mixed())),
        form("g5-fraction-of-quantity", "A fraction of an amount", 3, U4,
             "Divide by the denominator, multiply by the numerator.",
             mk_num("g5-fq", _g_fraction_of_quantity())),
    ]

    U5 = "decimals-first-steps"
    forms += [
        form("g5-decimal-digit-value", "Decimal place value", 1, U5,
             "Tenths, then hundredths — the columns keep going past the point.",
             mk_txt("g5-ddv", _g_decimal_digit_value())),
        form("g5-decimal-as-fraction", "Decimals as fractions", 1, U5,
             "Read the last column for the denominator, then simplify.",
             mk_txt("g5-daf", _g_decimal_as_fraction())),
        form("g5-compare-decimals", "Comparing decimals", 2, U5,
             "Compare column by column; a longer decimal is not a bigger one.",
             mk_txt("g5-cd", _g_compare_decimals())),
        form("g5-add-sub-decimals", "Adding and subtracting decimals", 2, U5,
             "Line up the points, not the last digits.",
             mk_txt("g5-asd", _g_add_sub_decimals())),
        form("g5-round-decimals", "Rounding decimals", 2, U5,
             "Find the neighbouring tenths and pick the nearer one.",
             mk_txt("g5-rd", _g_round_decimals())),
        form("g5-money-total", "Money problems", 3, U5,
             "Multiply each item out, then add the piles.",
             mk_txt("g5-mt", _g_money_total())),
    ]

    U6 = "measurement-and-units"
    forms += [
        form("g5-convert-length", "Converting lengths", 1, U6,
             "Down the ladder multiplies; the number gets bigger, the amount doesn't.",
             mk_txt("g5-cl", _g_convert_length())),
        form("g5-convert-mass-capacity", "Mass and capacity", 1, U6,
             "Kilograms to grams, litres to millilitres — the same x1000 step.",
             mk_txt("g5-cmc", _g_convert_mass_capacity())),
        form("g5-time-convert", "Hours and minutes", 2, U6,
             "An hour is 60 minutes, never 100.",
             mk_num("g5-tc", _g_time_convert())),
        form("g5-elapsed-time", "Elapsed time", 2, U6,
             "Add hours then minutes, carrying an hour whenever minutes pass 60.",
             mk_txt("g5-et", _g_elapsed_time())),
        form("g5-compare-measures", "Comparing measurements", 2, U6,
             "Convert to one unit before comparing — bare numbers lie.",
             mk_txt("g5-cm", _g_compare_measures())),
        form("g5-measurement-word", "Convert-first problems", 3, U6,
             "Get both quantities into the same unit, then do the arithmetic.",
             mk_num("g5-mw", _g_measurement_word())),
    ]

    U7 = "geometry-shapes-and-area"
    forms += [
        form("g5-missing-angle", "Missing angles", 1, U7,
             "Straight line 180, full turn 360 — say which before subtracting.",
             mk_num("g5-ma", _g_missing_angle())),
        form("g5-perimeter-rect", "Perimeter of a rectangle", 1, U7,
             "The walk around: two lengths and two widths.",
             mk_num("g5-pr", _g_perimeter_rect())),
        form("g5-area-rect", "Area of a rectangle", 1, U7,
             "The tile count inside: length times width, in square units.",
             mk_num("g5-ar", _g_area_rect())),
        form("g5-triangle-angle", "The triangle angle sum", 2, U7,
             "Every triangle spends exactly 180 degrees.",
             mk_num("g5-ta", _g_triangle_angle())),
        form("g5-perimeter-backwards", "Perimeter, run backwards", 2, U7,
             "Halve the perimeter first, then subtract the known side.",
             mk_num("g5-pb", _g_perimeter_backwards())),
        form("g5-composite-area", "Composite areas", 3, U7,
             "Fill and subtract, or split and add — the two roads must agree.",
             mk_num("g5-ca", _g_composite_area())),
    ]

    U8 = "data-and-graphs"
    forms += [
        form("g5-tally-read", "Reading tallies", 1, U8,
             "Bundles are worth five: 5 x bundles + singles.",
             mk_num("g5-tr", _g_tally_read())),
        form("g5-pictograph", "Pictograph keys", 1, U8,
             "Value = symbols x key, and half a symbol carries half the key.",
             mk_num("g5-pg", _g_pictograph())),
        form("g5-range", "The range", 1, U8,
             "Largest minus smallest — the spread, not the centre.",
             mk_num("g5-rg", _g_range())),
        form("g5-table-missing", "Completing a table", 2, U8,
             "The rows must add to the total; a known total finds a missing row.",
             mk_num("g5-tm", _g_table_missing())),
        form("g5-bar-scale", "Reading a bar graph's scale", 2, U8,
             "Gridlines x step — counting gridlines as ones is the classic error.",
             mk_num("g5-bs", _g_bar_scale())),
        form("g5-mean", "Finding the mean", 2, U8,
             "Total divided by how many, checked by multiplying back.",
             mk_num("g5-mn", _g_mean())),
        form("g5-mean-missing", "Working back from a mean", 3, U8,
             "mean x count gives the total; subtract what you know.",
             mk_num("g5-mm", _g_mean_missing())),
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
