# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 4 — mirrors /math/4.

One collection PER UNIT: each of the eight Grade 4 topics gets its own set of
forms, its own unit page and its own practice session
(/math/problem-bank/4/<unit>/practice), so a student drilling times tables is
never handed a clock question.

Every problem is generated from a parameter SWEEP and every answer is
COMPUTED, never typed. Values stay exact: sympy checks are built from
Integer/Rational, never from float division.

Grade 4 house rules (the same ones scripts/grade4/check_grade4.py enforces on
the lessons, applied here by hand because the bank has its own gate):
  - nothing above 10 000, because that is the year's number range;
  - no decimals and no negatives — both are later years;
  - division carries its receipt (q*d + r = n AND r < d);
  - the tögrög is written as a WORD, outside math (KaTeX cannot draw ₮);
  - reading level stays at nine years old: short sentences, concrete nouns.

Self-check:  python3 scripts/pb/grade4.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import sys

from sympy import Rational

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, mk_num, mk_txt, money  # noqa: E402

SLUG = "4"
TITLE = "Grade 4"
TITLE_MN = "4-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 4 year — numbers to "
         "10 000, the four operations, first fractions, shapes and symmetry, "
         "measurement and data, with a separate problem set for every unit.")

UNITS = [
    {"id": "numbers-to-10000", "title": "Numbers to 10 000",
     "blurb": "Place value to the thousands, reading and writing numbers, comparing, rounding and number patterns."},
    {"id": "addition-and-subtraction", "title": "Addition & Subtraction",
     "blurb": "Column addition and subtraction with regrouping, mental strategies, missing numbers and word problems."},
    {"id": "times-tables-and-multiplication", "title": "Times Tables & Multiplication",
     "blurb": "Equal groups, the tables to ten, arrays and the turnaround trick, and multiplying bigger numbers."},
    {"id": "division-and-sharing", "title": "Division & Sharing",
     "blurb": "Sharing and grouping, division facts, remainders and what they mean, halving, and choosing the operation."},
    {"id": "fractions-parts-of-a-whole", "title": "Fractions — Parts of a Whole",
     "blurb": "Equal parts, unit and non-unit fractions, comparing fractions, equivalence and a fraction of a set."},
    {"id": "shapes-and-symmetry", "title": "Shapes & Symmetry",
     "blurb": "Naming 2-D shapes, right angles, sorting quadrilaterals, lines of symmetry, 3-D solids and perimeter."},
    {"id": "measurement-time-and-money", "title": "Measurement, Time & Money",
     "blurb": "Centimetres and metres, grams and kilograms, millilitres and litres, the clock, the calendar and tögrög."},
    {"id": "data-and-pictographs", "title": "Data & Pictographs",
     "blurb": "Tally marks, tables and totals, pictograph keys, bar-chart scales and asking questions of data."},
]


def M(n):
    """A grouped whole number INSIDE math: 3 407 -> $3\\,407$."""
    return "$%s$" % money(n)


def frac(a, b):
    """A fraction written EXACTLY as given, without reducing.

    Grade 4 meets fractions as "how many of the equal parts", so shading two
    of four parts must read 2/4. Rendering through Rational would silently
    reduce it to 1/2 and quietly change the question. The sympy checks still
    use Rational, so the maths is exact even though the display is not
    lowest-terms.
    """
    return "\\frac{%d}{%d}" % (a, b)


PLACE_NAME = {0: "ones", 1: "tens", 2: "hundreds", 3: "thousands"}

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}


def words_under_100(n):
    if n < 20:
        return ONES[n]
    t, o = divmod(n, 10)
    return TENS[t] if o == 0 else "%s-%s" % (TENS[t], ONES[o])


def words(n):
    """British-style words for 1..9999: 3406 -> 'three thousand four hundred and six'."""
    assert 1 <= n <= 9999
    th, rest = divmod(n, 1000)
    h, r = divmod(rest, 100)
    parts = []
    if th:
        parts.append("%s thousand" % ONES[th])
    if h:
        parts.append("%s hundred" % ONES[h])
    if r:
        parts.append(("and " if (th or h) else "") + words_under_100(r))
    return " ".join(parts)


# ===========================================================================
# UNIT 1 — Numbers to 10 000
# ===========================================================================

def _g_place_value():
    # The asked digit must appear EXACTLY ONCE, or the question has two
    # answers. Build the other three digits from a pool that excludes it.
    POOLS = [(7, 1, 4), (2, 9, 5), (6, 3, 8), (4, 7, 1)]
    for d in range(2, 10):
        for p in (1, 2, 3):
            for pool in POOLS:
                rest = [x for x in pool if x != d]
                if len(rest) < 3:
                    continue
                digits = list(rest[:3])
                digits.insert(3 - p, d)
                if digits[0] == 0 or digits.count(d) != 1:
                    continue
                n = int("".join(str(x) for x in digits))
                val = d * 10 ** p
                others = [d * 10 ** q for q in (0, 1, 2, 3) if q != p]
                yield {
                    "statement": "In %s, what is the digit $%d$ worth?" % (M(n), d),
                    "correct": M(val),
                    "dvals": [M(o) for o in others],
                    "explanation": ("The $%d$ stands in the %s place, so it is worth "
                                    "$%d \\times %s = %s$."
                                    % (d, PLACE_NAME[p], d, money(10 ** p), money(val))),
                    "check": ["Eq(%d*%d, %d)" % (d, 10 ** p, val),
                              "Eq(Mod(floor(Rational(%d, %d)), 10), %d)" % (n, 10 ** p, d)],
                }


def _g_words_to_numeral():
    SHAPES = [(4, 0, 6), (2, 5, 0), (0, 3, 7), (6, 1, 2), (0, 0, 9), (5, 4, 0)]
    for th in range(1, 10):
        for (h, t, o) in SHAPES:
            n = th * 1000 + h * 100 + t * 10 + o
            # Distractors: the classic misreadings — dropping the hundreds
            # zero, swapping tens and ones, and hearing the thousands digit
            # as hundreds.
            d1 = th * 1000 + h * 100 + o * 10 + t
            d2 = th * 1000 + t * 10 + o + h * 10
            d3 = th * 100 + h * 100 + t * 10 + o
            if len({n, d1, d2, d3}) != 4:
                continue
            yield {
                "statement": "Write %s as a numeral." % words(n),
                "correct": M(n),
                "dvals": [M(d1), M(d2), M(d3)],
                "explanation": ("$%d$ thousands, $%d$ hundreds, $%d$ tens and $%d$ ones: "
                                "$%s + %s + %d + %d = %s$."
                                % (th, h, t, o, money(th * 1000), money(h * 100), t * 10, o,
                                   money(n))),
                "check": ["Eq(%d*1000 + %d*100 + %d*10 + %d, %d)" % (th, h, t, o, n)],
            }


def _g_compare_numbers():
    BASES = [(3241, 3412, 3214), (5060, 5600, 5006), (7418, 7481, 7148),
             (2903, 2930, 2093), (8175, 8157, 8517), (4602, 4620, 4062),
             (6389, 6398, 6839), (1547, 1574, 1457), (9024, 9042, 9204),
             (2768, 2786, 2678), (5391, 5319, 5913), (3480, 3408, 3840)]
    for (a, b, c) in BASES:
        ordered = sorted([a, b, c])
        small, mid, big = ordered
        # The three options besides the answer are the other two numbers plus
        # one near-miss, so a guesser cannot win by elimination.
        yield {
            "statement": "Which of these is the largest: %s, %s or %s?" % (M(a), M(b), M(c)),
            "correct": M(big),
            "dvals": [M(small), M(mid), M(big - 1000)],
            "explanation": ("Compare from the left. The first column where they differ "
                            "decides it, so %s is the largest." % M(big)),
            "check": ["%d > %d" % (big, mid), "%d > %d" % (mid, small)],
        }
        yield {
            "statement": "Which of these is the smallest: %s, %s or %s?" % (M(a), M(b), M(c)),
            "correct": M(small),
            "dvals": [M(mid), M(big), M(small + 1000)],
            "explanation": ("Compare from the left. %s has the smaller digit in the first "
                            "column that differs." % M(small)),
            "check": ["%d < %d" % (small, mid), "%d < %d" % (mid, big)],
        }


def _round_to(n, step):
    """Round half UP, which is the rule Grade 4 is taught."""
    return ((n + step // 2) // step) * step


def _g_rounding():
    NUMS = [1463, 2748, 3529, 4185, 5074, 6836, 7291, 8617, 9352, 2605, 4470, 7938]
    for n in NUMS:
        for step in (10, 100, 1000):
            r = _round_to(n, step)
            below = (n // step) * step
            above = below + step
            d = [x for x in (below, above, below - step, above + step) if x != r][:3]
            if len(set(d + [r])) != 4 or min(d + [r]) < 0:
                continue
            yield {
                "statement": "Round %s to the nearest %s." % (M(n), M(step)),
                "correct": M(r),
                "dvals": [M(x) for x in d],
                "explanation": ("%s sits between %s and %s. It is nearer to %s."
                                % (M(n), M(below), M(above), M(r))),
                "check": ["Eq(%d, %d)" % (r, r),
                          "Abs(%d - %d) <= %d" % (n, r, step // 2),
                          "Eq(Mod(%d, %d), 0)" % (r, step)],
            }


def _g_expanded_form():
    NUMS = [3407, 5162, 2840, 7095, 6318, 4703, 9526, 1274, 8039, 2951,
            6480, 3715, 5208, 7362, 4096, 1583, 2607, 3928, 4260, 5074,
            6135, 7409, 8261, 9037, 1746, 2385, 3054, 4817, 5390, 6702,
            7148, 8523, 9264, 1069, 2478, 3691, 4205, 5836, 6017, 7952]
    for n in NUMS:
        th, rest = divmod(n, 1000)
        h, r = divmod(rest, 100)
        t, o = divmod(r, 10)
        parts = [(th * 1000), (h * 100), (t * 10), o]
        shown = " + ".join(money(p) for p in parts if p)
        wrong1 = " + ".join(money(p) for p in [th, h, t, o] if p)
        wrong2 = " + ".join(money(p) for p in [th * 1000, h * 100, t, o] if p)
        wrong3 = " + ".join(money(p) for p in [th * 100, h * 10, t * 10, o] if p)
        if len({shown, wrong1, wrong2, wrong3}) != 4:
            continue
        yield {
            "statement": "Write %s in expanded form." % M(n),
            "correct": "$%s$" % shown,
            "dvals": ["$%s$" % wrong1, "$%s$" % wrong2, "$%s$" % wrong3],
            "explanation": ("Each digit is worth its digit times its place, and a zero "
                            "contributes nothing: $%s = %s$." % (shown, money(n))),
            "check": ["Eq(%s, %d)" % (" + ".join(str(p) for p in parts if p), n)],
        }


def _g_number_pattern():
    for start in (120, 245, 370, 415, 560, 685, 730, 855, 900):
        for step in (25, 50, 100, 5):
            terms = [start + i * step for i in range(4)]
            nxt = start + 4 * step
            if nxt > 9999:
                continue
            yield {
                "statement": ("A pattern starts %s, %s, %s, %s. What comes next?"
                              % tuple(M(t) for t in terms)),
                "correct": M(nxt),
                "dvals": [M(nxt + step), M(nxt - 1), M(terms[3] + step // 5 + 1)],
                "explanation": ("Each step adds $%d$, so after %s comes $%s + %d = %s$."
                                % (step, M(terms[3]), money(terms[3]), step, money(nxt))),
                "check": ["Eq(%d - %d, %d)" % (terms[1], terms[0], step),
                          "Eq(%d + %d, %d)" % (terms[3], step, nxt)],
            }


# ===========================================================================
# UNIT 2 — Addition & Subtraction
# ===========================================================================

def _addition_pairs():
    """A sweep of four-digit pairs that each need at least one carry — a sum
    with no regrouping is not what this form is drilling."""
    for th in range(1, 5):
        for h in (1, 3, 5, 7, 9):
            for t in (2, 6, 8):
                a = th * 1000 + h * 100 + t * 10 + 7
                b = (5 - th) * 1000 + (9 - h) * 100 + (9 - t) * 10 + 8
                if a + b > 9999 or b < 1000:
                    continue
                # at least one column must carry
                if not (7 + 8 >= 10 or t + (9 - t) >= 10 or h + (9 - h) >= 10):
                    continue
                yield a, b


def _g_column_add():
    for (a, b) in _addition_pairs():
        s = a + b
        if s > 9999:
            continue
        yield {
            "statement": "Work out $%s + %s$." % (money(a), money(b)),
            "correct": M(s),
            "dvals": [M(s - 100), M(s + 10), M(s - 1000)],
            "explanation": ("Line up the places and add from the right, carrying past "
                            "nine: $%s + %s = %s$." % (money(a), money(b), money(s))),
            "check": ["Eq(%d + %d, %d)" % (a, b, s), "Eq(%d - %d, %d)" % (s, a, b)],
        }


def _subtraction_pairs():
    """Four-digit pairs where the ones column forces a regroup, so the form
    actually drills borrowing rather than digit-by-digit subtraction."""
    for th in range(4, 10):
        for h in (0, 2, 4, 6):
            for t in (1, 3, 5):
                a = th * 1000 + h * 100 + t * 10 + 2
                b = (th - 3) * 1000 + (h + 3) * 100 + (t + 4) * 10 + 7
                if b < 1000 or b >= a:
                    continue
                yield a, b


def _g_column_sub():
    for (a, b) in _subtraction_pairs():
        d = a - b
        yield {
            "statement": "Work out $%s - %s$." % (money(a), money(b)),
            "correct": M(d),
            "dvals": [M(d + 100), M(d - 10), M(d + 1000)],
            "explanation": ("Regroup where the top digit is smaller, then subtract: "
                            "$%s - %s = %s$. Check by adding back: $%s + %s = %s$."
                            % (money(a), money(b), money(d), money(d), money(b), money(a))),
            "check": ["Eq(%d - %d, %d)" % (a, b, d), "Eq(%d + %d, %d)" % (d, b, a)],
        }


def _g_missing_number():
    for (a, b) in _addition_pairs():
        s = a + b
        if s > 9999:
            continue
        yield {
            "statement": "What number goes in the box? $%s + \\square = %s$" % (money(a), money(s)),
            "correct": M(b),
            "dvals": [M(s + a), M(b + 10), M(b - 100)],
            "explanation": ("The box is the missing part, so subtract the part you know: "
                            "$%s - %s = %s$." % (money(s), money(a), money(b))),
            "check": ["Eq(%d + %d, %d)" % (a, b, s), "Eq(%d - %d, %d)" % (s, a, b)],
        }


def _g_mental_strategy():
    for a in (146, 238, 375, 427, 519, 663, 728, 854, 942):
        for near in (99, 199, 98, 49):
            s = a + near
            round_up = near + 1
            yield {
                "statement": "Work out $%d + %d$ in your head." % (a, near),
                "correct": M(s),
                "dvals": [M(s + 1), M(s - 1), M(a + round_up + 1)],
                "explanation": ("Add $%d$ and take one back: $%d + %d = %d$, then "
                                "$%d - 1 = %d$." % (round_up, a, round_up, a + round_up,
                                                    a + round_up, s)),
                "check": ["Eq(%d + %d, %d)" % (a, near, s),
                          "Eq(%d + %d - 1, %d)" % (a, round_up, s)],
            }


def _g_word_problem_add():
    # (plural noun, where it lives) — the sentence reads "There were N books in
    # the school library. Then M more books arrived."
    ITEMS = [("books", "in the school library"), ("bricks", "on the site"),
             ("seedlings", "in the nursery"), ("stamps", "in the album"),
             ("sheep", "in the herd"), ("bottles", "at the depot")]
    STARTS = [1240, 2185, 3072, 1836, 2451, 3608, 1974, 2760, 3125]
    ADDS = [365, 478, 592, 246, 813, 157]
    i = 0
    for start in STARTS:
        for add in ADDS:
            i += 1
            noun, where = ITEMS[i % len(ITEMS)]
            total = start + add
            if total > 9999:
                continue
            yield {
                "statement": ("There were %s %s %s. Then %s more %s arrived. "
                              "How many are there now?"
                              % (M(start), noun, where, M(add), noun)),
                "correct": M(total),
                "dvals": [M(start - add), M(total + 100), M(total - 10)],
                "explanation": ("More were added, so add: $%s + %s = %s$."
                                % (money(start), money(add), money(total))),
                "check": ["Eq(%d + %d, %d)" % (start, add, total),
                          "%d > %d" % (total, start)],
            }


def _g_inverse_check():
    for (a, b) in _subtraction_pairs():
        d = a - b
        yield {
            "statement": ("A pupil worked out $%s - %s$ and got %s. Which addition checks it?"
                          % (money(a), money(b), M(d))),
            "correct": "$%s + %s = %s$" % (money(d), money(b), money(a)),
            "dvals": ["$%s + %s = %s$" % (money(d), money(a), money(a + d)),
                      "$%s - %s = %s$" % (money(a), money(d), money(b)),
                      "$%s + %s = %s$" % (money(a), money(b), money(a + b))],
            "explanation": ("Addition undoes subtraction: the answer plus what was taken "
                            "away must give back the start, and $%s + %s = %s$."
                            % (money(d), money(b), money(a))),
            "check": ["Eq(%d + %d, %d)" % (d, b, a), "Eq(%d - %d, %d)" % (a, b, d)],
        }


# ===========================================================================
# UNIT 3 — Times Tables & Multiplication
# ===========================================================================

def _g_tables_2_5_10():
    for t in (2, 5, 10):
        for k in range(2, 13):
            p = t * k
            yield {
                "statement": "What is $%d \\times %d$?" % (t, k),
                "correct": p,
                "dvals": [p + t, p - t, t * (k + 2)],
                "explanation": ("$%d$ groups of $%d$ is $%d$." % (k, t, p)),
                "check": ["Eq(%d*%d, %d)" % (t, k, p), "Eq(%d/%d, %d)" % (p, t, k)],
            }


def _g_tables_6_9():
    for t in (6, 7, 8, 9):
        for k in range(3, 13):
            p = t * k
            yield {
                "statement": "What is $%d \\times %d$?" % (t, k),
                "correct": p,
                "dvals": [p + t, p - t, p + 1],
                "explanation": ("$%d$ groups of $%d$ is $%d$. One group less is $%d$."
                                % (k, t, p, p - t)),
                "check": ["Eq(%d*%d, %d)" % (t, k, p), "Eq(%d/%d, %d)" % (p, k, t)],
            }


def _g_equal_groups():
    THINGS = ["pencils", "sweets", "marbles", "buttons", "coins", "stickers",
              "apples", "beads", "shells"]
    i = 0
    for g in range(3, 10):
        for per in (4, 6, 7, 8, 9):
            i += 1
            p = g * per
            yield {
                "statement": ("There are $%d$ boxes with $%d$ %s in each box. "
                              "How many %s altogether?"
                              % (g, per, THINGS[i % len(THINGS)], THINGS[i % len(THINGS)])),
                "correct": p,
                "dvals": [g + per, p - per, p + g],
                "explanation": ("Equal groups mean multiply: $%d \\times %d = %d$."
                                % (g, per, p)),
                "check": ["Eq(%d*%d, %d)" % (g, per, p), "Eq(%d/%d, %d)" % (p, g, per)],
            }


def _g_arrays_turnaround():
    for r in range(2, 12):
        for c in range(2, 12):
            if r >= c:
                continue
            p = r * c
            yield {
                "statement": ("An array has $%d$ rows of $%d$. Which multiplication gives "
                              "the same total?" % (r, c)),
                "correct": "$%d \\times %d$" % (c, r),
                "dvals": ["$%d \\times %d$" % (c, r + 1),
                          "$%d + %d$" % (r, c),
                          "$%d \\times %d$" % (c, c)],
                "explanation": ("Turn the array a quarter turn and it becomes $%d$ rows of "
                                "$%d$. Both give $%d$." % (c, r, p)),
                "check": ["Eq(%d*%d, %d*%d)" % (r, c, c, r), "Eq(%d*%d, %d)" % (r, c, p)],
            }


def _g_multiply_two_digit():
    for a in (12, 14, 16, 18, 21, 23, 25, 27, 32, 34, 36, 41, 43, 45, 52, 54, 63, 72):
        for k in (3, 4, 5):
            p = a * k
            if p > 9999:
                continue
            tens, ones = divmod(a, 10)
            yield {
                "statement": "Work out $%d \\times %d$." % (a, k),
                "correct": M(p),
                "dvals": [M(p + k), M(p - 10), M(tens * 10 * k + ones)],
                "explanation": ("Split $%d$ into $%d$ and $%d$: $%d \\times %d = %d$ and "
                                "$%d \\times %d = %d$, and $%d + %d = %d$."
                                % (a, tens * 10, ones, tens * 10, k, tens * 10 * k,
                                   ones, k, ones * k, tens * 10 * k, ones * k, p)),
                "check": ["Eq(%d*%d, %d)" % (a, k, p),
                          "Eq(%d*%d + %d*%d, %d)" % (tens * 10, k, ones, k, p)],
            }


def _g_missing_factor():
    for t in (3, 4, 6, 7, 8, 9):
        for k in range(3, 11):
            p = t * k
            yield {
                "statement": "What number goes in the box? $%d \\times \\square = %d$" % (t, p),
                "correct": k,
                "dvals": [k + 1, k - 1, p - t],
                "explanation": ("Ask how many $%d$s make $%d$: $%d \\div %d = %d$."
                                % (t, p, p, t, k)),
                "check": ["Eq(%d*%d, %d)" % (t, k, p), "Eq(%d/%d, %d)" % (p, t, k)],
            }


# ===========================================================================
# UNIT 4 — Division & Sharing
# ===========================================================================

def _g_division_facts():
    for d in (2, 3, 4, 5, 6, 7, 8, 9):
        for q in range(2, 11):
            n = d * q
            yield {
                "statement": "What is $%d \\div %d$?" % (n, d),
                "correct": q,
                "dvals": [q + 1, q - 1, n - d],
                "explanation": ("$%d \\times %d = %d$, so $%d \\div %d = %d$."
                                % (d, q, n, n, d, q)),
                "check": ["Eq(%d*%d, %d)" % (d, q, n), "Eq(%d/%d, %d)" % (n, d, q)],
            }


def _g_sharing():
    WHO = ["children", "friends", "cousins", "classmates", "neighbours", "teammates"]
    WHAT = ["sweets", "marbles", "stickers", "cards", "grapes", "pencils"]
    i = 0
    for people in (3, 4, 5, 6, 7, 8):
        for each in (4, 6, 7, 8, 9, 12):
            i += 1
            total = people * each
            yield {
                "statement": ("$%d$ %s share $%d$ %s equally. How many does each one get?"
                              % (people, WHO[i % len(WHO)], total, WHAT[i % len(WHAT)])),
                "correct": each,
                "dvals": [each + 1, each - 1, total - people],
                "explanation": ("Sharing equally means divide: $%d \\div %d = %d$ each."
                                % (total, people, each)),
                "check": ["Eq(%d*%d, %d)" % (people, each, total),
                          "Eq(%d/%d, %d)" % (total, people, each)],
            }


def _g_remainders():
    for d in (3, 4, 5, 6, 7, 8):
        for q in (4, 6, 7, 9, 11):
            for r in (1, 2):
                if r >= d:
                    continue
                n = d * q + r
                yield {
                    "statement": "Work out $%d \\div %d$ and give the remainder." % (n, d),
                    "correct": "$%d$ remainder $%d$" % (q, r),
                    "dvals": ["$%d$ remainder $%d$" % (q, r + 1),
                              "$%d$ remainder $%d$" % (q + 1, r),
                              "$%d$ remainder $%d$" % (q - 1, r)],
                    "explanation": ("$%d \\times %d = %d$, and $%d - %d = %d$ is left over. "
                                    "The remainder must be smaller than $%d$."
                                    % (d, q, d * q, n, d * q, r, d)),
                    "check": ["Eq(%d*%d + %d, %d)" % (q, d, r, n), "%d < %d" % (r, d)],
                }


def _g_halving():
    for n in (24, 36, 48, 56, 68, 72, 84, 96, 128, 146, 158, 164, 172, 186, 194,
              216, 234, 258, 276, 288, 304, 326, 348, 372, 394, 416, 438, 452,
              476, 498, 524, 546, 568, 582, 614, 636):
        h = n // 2
        yield {
            "statement": "What is half of $%d$?" % n,
            "correct": h,
            "dvals": [h + 1, h - 2, n * 2],
            "explanation": ("Half of $%d$ is $%d$, because $%d + %d = %d$."
                            % (n, h, h, h, n)),
            "check": ["Eq(2*%d, %d)" % (h, n), "Eq(%d/2, %d)" % (n, h)],
        }


def _g_choose_operation():
    i = 0
    for groups in (4, 5, 6, 7, 8, 9):
        for per in (6, 7, 8, 9, 12):
            i += 1
            total = groups * per
            if i % 2 == 0:
                yield {
                    "statement": ("$%d$ baskets hold $%d$ eggs each. Which calculation "
                                  "finds the total number of eggs?" % (groups, per)),
                    "correct": "$%d \\times %d$" % (groups, per),
                    "dvals": ["$%d \\div %d$" % (total, groups),
                              "$%d + %d$" % (groups, per),
                              "$%d - %d$" % (per, groups)],
                    "explanation": ("Equal groups joined together means multiply: "
                                    "$%d \\times %d = %d$." % (groups, per, total)),
                    "check": ["Eq(%d*%d, %d)" % (groups, per, total)],
                }
            else:
                yield {
                    "statement": ("$%d$ eggs are packed into baskets of $%d$. Which "
                                  "calculation finds the number of baskets?" % (total, per)),
                    "correct": "$%d \\div %d$" % (total, per),
                    "dvals": ["$%d \\times %d$" % (total, per),
                              "$%d - %d$" % (total, per),
                              "$%d + %d$" % (total, per)],
                    "explanation": ("A total split into equal groups means divide: "
                                    "$%d \\div %d = %d$ baskets." % (total, per, groups)),
                    "check": ["Eq(%d/%d, %d)" % (total, per, groups),
                              "Eq(%d*%d, %d)" % (groups, per, total)],
                }


def _g_remainder_meaning():
    for d in (4, 5, 6, 8):
        for q in (5, 6, 7, 9, 11, 13):
            for r in (1, 3):
                if r >= d:
                    continue
                n = d * q + r
                yield {
                    "statement": ("$%d$ children go camping. Each tent sleeps $%d$. "
                                  "How many tents are needed so everyone has a place?"
                                  % (n, d)),
                    "correct": q + 1,
                    "dvals": [q, q + 2, d + q],
                    "explanation": ("$%d \\div %d = %d$ remainder $%d$. The $%d$ left over "
                                    "still need a tent, so $%d + 1 = %d$ tents."
                                    % (n, d, q, r, r, q, q + 1)),
                    "check": ["Eq(%d*%d + %d, %d)" % (q, d, r, n), "%d < %d" % (r, d),
                              "%d*%d >= %d" % (q + 1, d, n)],
                }


# ===========================================================================
# UNIT 5 — Fractions — Parts of a Whole
# ===========================================================================

def _g_name_fraction():
    for den in (3, 4, 5, 6, 8, 10):
        for num in range(1, den):
            if den - num == num:
                continue          # the unshaded distractor would equal the answer
            yield {
                "statement": ("A shape is cut into $%d$ equal parts and $%d$ of them are "
                              "shaded. What fraction is shaded?" % (den, num)),
                "correct": "$%s$" % frac(num, den),
                "dvals": ["$%s$" % frac(den, num),
                          "$%s$" % frac(num, den + 1),
                          "$%s$" % frac(den - num, den)],
                "explanation": ("The bottom number counts the equal parts ($%d$) and the "
                                "top counts the shaded ones ($%d$)." % (den, num)),
                "check": ["Eq(Rational(%d, %d) + Rational(%d, %d), 1)" % (num, den, den - num, den),
                          "Rational(%d, %d) < 1" % (num, den)],
            }


def _g_unit_fraction():
    for den in (2, 3, 4, 5, 6, 8, 10, 12):
        for total in (12, 20, 24, 30, 36, 40, 60):
            if total % den:
                continue
            part = total // den
            yield {
                "statement": "What is $%s$ of $%d$?" % (frac(1, den), total),
                "correct": part,
                "dvals": [part + 1, total - part, den * total // 10 + 1],
                "explanation": ("One part out of $%d$ equal parts: $%d \\div %d = %d$."
                                % (den, total, den, part)),
                "check": ["Eq(%d*%d, %d)" % (den, part, total),
                          "Eq(Rational(1, %d)*%d, %d)" % (den, total, part)],
            }


def _g_compare_same_denominator():
    for den in (3, 4, 5, 6, 8, 10, 12):
        for a in range(1, den):
            for b in range(a + 1, den):
                yield {
                    "statement": ("Which is larger, $%s$ or $%s$?"
                                  % (frac(a, den), frac(b, den))),
                    "correct": "$%s$" % frac(b, den),
                    "dvals": ["$%s$" % frac(a, den),
                              "They are equal",
                              "$%s$" % frac(a, den + 1)],
                    "explanation": ("The parts are the same size, so more parts means more: "
                                    "$%d > %d$." % (b, a)),
                    "check": ["Rational(%d, %d) > Rational(%d, %d)" % (b, den, a, den),
                              "%d > %d" % (b, a)],
                }


def _g_compare_same_numerator():
    for num in (1, 2, 3):
        for a in (3, 4, 5, 6, 8, 10, 12):
            for b in (3, 4, 5, 6, 8, 10, 12):
                if b <= a or num >= a:
                    continue
                yield {
                    "statement": ("Which is larger, $%s$ or $%s$?"
                                  % (frac(num, a), frac(num, b))),
                    "correct": "$%s$" % frac(num, a),
                    "dvals": ["$%s$" % frac(num, b),
                              "They are equal",
                              "$%s$" % frac(num + 1, b)],
                    "explanation": ("Same number of parts, but cutting into $%d$ makes each "
                                    "part bigger than cutting into $%d$." % (a, b)),
                    "check": ["Rational(%d, %d) > Rational(%d, %d)" % (num, a, num, b),
                              "%d < %d" % (a, b)],
                }


def _g_fraction_of_set():
    for den in (3, 4, 5, 6, 8):
        for num in range(2, den):
            for total in (24, 30, 36, 40, 48, 60):
                if total % den:
                    continue
                part = num * total // den
                yield {
                    "statement": ("A class has $%d$ pupils and $%s$ of them walk to school. "
                                  "How many walk?" % (total, frac(num, den))),
                    "correct": part,
                    "dvals": [total // den, total - part, part + num],
                    "explanation": ("One part is $%d \\div %d = %d$, and $%d$ parts is "
                                    "$%d \\times %d = %d$."
                                    % (total, den, total // den, num, num, total // den, part)),
                    "check": ["Eq(Rational(%d, %d)*%d, %d)" % (num, den, total, part),
                              "Eq(%d*%d, %d)" % (num, total // den, part)],
                }


def _g_equivalent_fractions():
    for den in (2, 3, 4, 5, 6, 8, 10):
        for num in range(1, den):
            for k in (2, 3, 4, 5):
                if den * k > 40:
                    continue
                # Asking for the missing TOP number keeps every draw a
                # different question. "Which fraction equals 1/2?" would read
                # identically for every multiplier and collapse to one variant.
                yield {
                    "statement": ("Fill the box: $%s = \\frac{\\square}{%d}$"
                                  % (frac(num, den), den * k)),
                    "correct": num * k,
                    # forgot to scale the top / added the multiplier instead of
                    # multiplying / used the wrong multiplier
                    "dvals": [num, num + k, num * (k + 1)],
                    "explanation": ("The bottom was multiplied by $%d$ ($%d \\times %d = %d$), "
                                    "so the top must be too: $%d \\times %d = %d$."
                                    % (k, den, k, den * k, num, k, num * k)),
                    "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (num * k, den * k, num, den),
                              "Eq(%d*%d, %d)" % (num, k, num * k)],
                }


# ===========================================================================
# UNIT 6 — Shapes & Symmetry
# ===========================================================================

POLY = [("triangle", 3), ("quadrilateral", 4), ("pentagon", 5), ("hexagon", 6),
        ("heptagon", 7), ("octagon", 8), ("nonagon", 9), ("decagon", 10)]


def _g_shape_sides():
    for (name, n) in POLY:
        yield {
            "statement": "How many sides does a %s have?" % name,
            "correct": n,
            "dvals": [n + 1, n - 1, n + 2],
            "explanation": ("A %s has $%d$ sides, and the same number of corners."
                            % (name, n)),
            "check": ["Eq(%d, %d)" % (n, n), "Eq(%d - 2, %d)" % (n, n - 2)],
        }
    for (a, na) in POLY:
        for (b, nb) in POLY:
            if nb <= na:
                continue
            yield {
                "statement": ("How many more sides does a %s have than a %s?" % (b, a)),
                "correct": nb - na,
                # off by one / answered with either shape's own side count
                "dvals": [nb - na + 1, na, nb],
                "explanation": ("A %s has $%d$ sides and a %s has $%d$: $%d - %d = %d$."
                                % (b, nb, a, na, nb, na, nb - na)),
                "check": ["Eq(%d - %d, %d)" % (nb, na, nb - na), "%d > %d" % (nb, na)],
            }


def _g_right_angles():
    # (shape, right angles, three plausible wrong counts). The distractors are
    # written out per shape because a shape with 0 or 1 right angles cannot
    # carry the usual off-by-one set without one of them landing on the answer.
    SHAPES = [("rectangle", 4, (2, 3, 0)),
              ("square", 4, (1, 2, 3)),
              ("right-angled trapezium", 2, (0, 1, 4)),
              ("right-angled triangle", 1, (0, 2, 3)),
              ("regular pentagon", 0, (1, 2, 5)),
              ("regular hexagon", 0, (1, 3, 6))]
    for (name, k, wrong) in SHAPES:
        yield {
            "statement": "How many right angles does a %s have?" % name,
            "correct": k,
            "dvals": list(wrong),
            "explanation": ("A %s has $%d$ right angle%s — a right angle is a square "
                            "corner." % (name, k, "" if k == 1 else "s")),
            "check": ["Eq(%d, %d)" % (k, k), "%d <= 4" % k],
        }
    # Only shapes with at least two right angles get the multiplied version:
    # with k = 1 the "added instead of multiplied" distractor equals the answer.
    for (name, k, _w) in SHAPES:
        if k < 2:
            continue
        for extra in range(2, 10):
            total = k * extra
            yield {
                "statement": ("A pattern is made from $%d$ %ss. How many right angles are "
                              "there altogether?" % (extra, name)),
                "correct": total,
                # counted one shape only / used one shape too many / added
                "dvals": [k, (extra + 1) * k, extra + k],
                "explanation": ("One %s has $%d$ right angles, so $%d$ of them have "
                                "$%d \\times %d = %d$." % (name, k, extra, extra, k, total)),
                "check": ["Eq(%d*%d, %d)" % (extra, k, total)],
            }


def _g_quadrilaterals():
    # (shape, defining property, pairs of parallel sides). The naming question
    # is set in a pupil's context so each draw is a different question rather
    # than the same sentence with the options shuffled.
    FACTS = [
        ("square", "four equal sides and four right angles", 2),
        ("rectangle", "two pairs of equal sides and four right angles", 2),
        ("rhombus", "four equal sides but no right angles", 2),
        ("parallelogram", "two pairs of parallel sides but no right angles", 2),
        ("trapezium", "exactly one pair of parallel sides", 1),
    ]
    PUPILS = ["Bat", "Saraa", "Dorj", "Oyuna", "Tuya", "Bold", "Naran", "Enkhee"]
    for (i, (name, desc, _par)) in enumerate(FACTS):
        others = [f[0] for f in FACTS if f[0] != name]
        for (j, pupil) in enumerate(PUPILS):
            yield {
                "statement": ("%s cuts out a tile with %s. What shape is it?"
                              % (pupil, desc)),
                "correct": name.capitalize(),
                "dvals": [others[(j) % len(others)].capitalize(),
                          others[(j + 1) % len(others)].capitalize(),
                          others[(j + 2) % len(others)].capitalize()],
                "explanation": ("A %s is the quadrilateral with %s." % (name, desc)),
                "check": ["Eq(4, 4)"],
            }
    for (name, desc, par) in FACTS:
        yield {
            "statement": "How many pairs of parallel sides does a %s have?" % name,
            "correct": par,
            "dvals": [par + 1, par + 2, 4],
            "explanation": ("A %s has %s, which gives $%d$ pair%s of parallel sides."
                            % (name, desc, par, "" if par == 1 else "s")),
            "check": ["Eq(2*%d, %d)" % (par, 2 * par), "%d <= 2" % par],
        }


def _g_symmetry_lines():
    REG = [("equilateral triangle", 3), ("square", 4), ("regular pentagon", 5),
           ("regular hexagon", 6), ("regular octagon", 8), ("rectangle", 2),
           ("rhombus", 2), ("circle", 0)]
    for (name, k) in REG:
        if name == "circle":
            continue
        for mult in range(2, 7):
            total = k * mult
            yield {
                "statement": ("A poster shows $%d$ separate %ss. How many lines of symmetry "
                              "are drawn in total?" % (mult, name)),
                "correct": total,
                "dvals": [total + mult, total - mult, k + mult],
                "explanation": ("One %s has $%d$ lines of symmetry, so $%d$ of them have "
                                "$%d \\times %d = %d$." % (name, k, mult, mult, k, total)),
                "check": ["Eq(%d*%d, %d)" % (mult, k, total), "%d > 0" % total],
            }


def _g_solids():
    SOLIDS = [("cube", 6, 12, 8), ("cuboid", 6, 12, 8), ("square-based pyramid", 5, 8, 5),
              ("triangular prism", 5, 9, 6), ("tetrahedron", 4, 6, 4)]
    for (name, f, e, v) in SOLIDS:
        yield {
            "statement": "How many faces does a %s have?" % name,
            "correct": f,
            "dvals": [e, v, f + 1] if len({e, v, f + 1, f}) == 4 else [f + 1, f + 2, f + 3],
            "explanation": ("A %s has $%d$ faces, $%d$ edges and $%d$ vertices."
                            % (name, f, e, v)),
            "check": ["Eq(%d - %d + %d, 2)" % (v, e, f)],
        }
        yield {
            "statement": "How many edges does a %s have?" % name,
            "correct": e,
            "dvals": [f, v, e + 1] if len({f, v, e + 1, e}) == 4 else [e + 1, e + 2, e + 3],
            "explanation": ("A %s has $%d$ edges, where two faces meet." % (name, e)),
            "check": ["Eq(%d - %d + %d, 2)" % (v, e, f)],
        }
        yield {
            "statement": "How many vertices (corners) does a %s have?" % name,
            "correct": v,
            "dvals": [f, e, v + 1] if len({f, e, v + 1, v}) == 4 else [v + 1, v + 2, v + 3],
            "explanation": ("A %s has $%d$ vertices, where the edges meet." % (name, v)),
            "check": ["Eq(%d - %d + %d, 2)" % (v, e, f)],
        }
    for (name, f, e, v) in SOLIDS:
        for mult in (2, 3, 4, 5):
            yield {
                "statement": ("A model uses $%d$ %ss. How many faces are there in total?"
                              % (mult, name)),
                "correct": f * mult,
                "dvals": [e * mult, v * mult, f * mult + 1],
                "explanation": ("Each %s has $%d$ faces: $%d \\times %d = %d$."
                                % (name, f, mult, f, f * mult)),
                "check": ["Eq(%d*%d, %d)" % (mult, f, f * mult)],
            }


def _g_perimeter():
    for (name, n) in POLY:
        for side in (3, 5, 6, 7, 8, 9, 12):
            p = n * side
            yield {
                "statement": ("A regular %s has sides of $%d$ cm. What is its perimeter?"
                              % (name, side)),
                "correct": p,
                "dvals": [p + side, p - side, n + side],
                "explanation": ("All $%d$ sides are equal, so the perimeter is "
                                "$%d \\times %d = %d$ cm." % (n, n, side, p)),
                "check": ["Eq(%d*%d, %d)" % (n, side, p)],
            }


# ===========================================================================
# UNIT 7 — Measurement, Time & Money
# ===========================================================================

def _g_length():
    for m in range(1, 10):
        for cm in (0, 5, 20, 45, 60, 85):
            total = m * 100 + cm
            yield {
                "statement": "How many centimetres are there in $%d$ m $%d$ cm?" % (m, cm),
                "correct": M(total),
                "dvals": [M(m * 10 + cm), M(total + 100), M(m * 100 + cm * 10)],
                "explanation": ("One metre is $100$ cm, so $%d$ m is $%s$ cm, and "
                                "$%s + %d = %s$ cm."
                                % (m, money(m * 100), money(m * 100), cm, money(total))),
                "check": ["Eq(%d*100 + %d, %d)" % (m, cm, total)],
            }


def _g_mass_capacity():
    for kg in range(1, 9):
        for g in (0, 50, 250, 400, 750, 900):
            total = kg * 1000 + g
            if total > 9999:
                continue
            yield {
                "statement": "How many grams are there in $%d$ kg $%d$ g?" % (kg, g),
                "correct": M(total),
                "dvals": [M(kg * 100 + g), M(total + 1000), M(kg * 1000 + g * 10)],
                "explanation": ("One kilogram is $1\\,000$ g, so $%d$ kg is $%s$ g, and "
                                "$%s + %d = %s$ g."
                                % (kg, money(kg * 1000), money(kg * 1000), g, money(total))),
                "check": ["Eq(%d*1000 + %d, %d)" % (kg, g, total)],
            }
    for l in range(1, 9):
        for ml in (0, 100, 250, 500, 750):
            total = l * 1000 + ml
            if total > 9999:
                continue
            yield {
                "statement": "How many millilitres are there in $%d$ l $%d$ ml?" % (l, ml),
                "correct": M(total),
                "dvals": [M(l * 100 + ml), M(total + 1000), M(l * 1000 + ml * 10)],
                "explanation": ("One litre is $1\\,000$ ml, so $%d$ l is $%s$ ml, and "
                                "$%s + %d = %s$ ml."
                                % (l, money(l * 1000), money(l * 1000), ml, money(total))),
                "check": ["Eq(%d*1000 + %d, %d)" % (l, ml, total)],
            }


def _clock(h, m):
    return "$%d$:$%02d$" % (h, m)


def _g_clock():
    for h in range(1, 12):
        for m in (0, 15, 30, 45):
            past = m if m <= 30 else 60 - m
            if m == 0:
                phrase = "%d o'clock" % h
            elif m == 15:
                phrase = "quarter past %d" % h
            elif m == 30:
                phrase = "half past %d" % h
            else:
                phrase = "quarter to %d" % (h + 1)
            wrong = ["quarter past %d" % (h + 1), "half past %d" % (h + 1),
                     "quarter to %d" % h, "%d o'clock" % (h + 1)]
            dv = [w for w in wrong if w != phrase][:3]
            yield {
                "statement": "A clock reads %s. How do you say this time?" % _clock(h, m),
                "correct": phrase,
                "dvals": dv,
                "explanation": ("The hour hand is at $%d$ and the minute hand shows $%d$ "
                                "minutes, which we say as %s." % (h, m, phrase)),
                "check": ["Eq(%d*60 + %d, %d)" % (h, m, h * 60 + m), "%d < 60" % m],
            }


def _g_duration():
    for sh in range(1, 11):
        for sm in (0, 15, 30, 45):
            for dur in (45, 90, 120):
                start = sh * 60 + sm
                end = start + dur
                if end >= 12 * 60:
                    continue
                eh, em = divmod(end, 60)
                yield {
                    "statement": ("A lesson starts at %s and lasts $%d$ minutes. "
                                  "When does it end?" % (_clock(sh, sm), dur)),
                    "correct": _clock(eh, em),
                    "dvals": [_clock(eh, (em + 15) % 60), _clock(eh + 1, em),
                              _clock(sh, (sm + dur) % 60)],
                    "explanation": ("$%d$ minutes is $%d$ h $%d$ min. Adding to %s gives %s."
                                    % (dur, dur // 60, dur % 60, _clock(sh, sm),
                                       _clock(eh, em))),
                    "check": ["Eq(%d + %d, %d)" % (start, dur, end),
                              "Eq(%d*60 + %d, %d)" % (eh, em, end)],
                }


def _g_money():
    for a in (150, 250, 320, 480, 560, 720, 850, 940):
        for b in (100, 200, 350, 450, 600):
            total = a + b
            if total > 9999:
                continue
            yield {
                "statement": ("A pen costs %s tögrög and a notebook costs %s tögrög. "
                              "How much do they cost together, in tögrög?"
                              % (money(a), money(b))),
                "correct": M(total),
                "dvals": [M(abs(a - b)), M(total + 100), M(total - 10)],
                "explanation": ("Add the two prices: $%s + %s = %s$ tögrög."
                                % (money(a), money(b), money(total))),
                "check": ["Eq(%d + %d, %d)" % (a, b, total)],
            }
    for paid in (1000, 2000, 5000):
        for cost in (350, 640, 780, 1250, 1830, 2450):
            if cost >= paid:
                continue
            change = paid - cost
            yield {
                "statement": ("A child pays with a %s tögrög note for something costing "
                              "%s tögrög. How much change, in tögrög?"
                              % (money(paid), money(cost))),
                "correct": M(change),
                "dvals": [M(paid + cost), M(change + 100), M(change - 50)],
                "explanation": ("Change is what is left: $%s - %s = %s$ tögrög."
                                % (money(paid), money(cost), money(change))),
                "check": ["Eq(%d - %d, %d)" % (paid, cost, change),
                          "Eq(%d + %d, %d)" % (change, cost, paid)],
            }


def _g_convert_first():
    for m in range(2, 9):
        for cm in (25, 40, 60, 75, 90):
            for take in (30, 55, 80):
                total = m * 100 + cm
                left = total - take
                if left <= 0:
                    continue
                yield {
                    "statement": ("A ribbon is $%d$ m $%d$ cm long. $%d$ cm is cut off. "
                                  "How many centimetres are left?" % (m, cm, take)),
                    "correct": M(left),
                    "dvals": [M(total + take), M(left + 100), M(m * 100 - take)],
                    "explanation": ("Change to one unit first: $%d$ m $%d$ cm is $%s$ cm. "
                                    "Then $%s - %d = %s$ cm."
                                    % (m, cm, money(total), money(total), take, money(left))),
                    "check": ["Eq(%d*100 + %d, %d)" % (m, cm, total),
                              "Eq(%d - %d, %d)" % (total, take, left)],
                }


# ===========================================================================
# UNIT 8 — Data & Pictographs
# ===========================================================================

def _g_tally():
    for n in range(3, 40):
        fives, ones = divmod(n, 5)
        yield {
            "statement": ("A tally chart shows $%d$ full groups of five and $%d$ single "
                          "marks. How many is that?" % (fives, ones)),
            "correct": n,
            "dvals": [fives + ones, n + 5, n - 1],
            "explanation": ("Each full group is five: $%d \\times 5 = %d$, and $%d$ more "
                            "makes $%d$." % (fives, fives * 5, ones, n)),
            "check": ["Eq(%d*5 + %d, %d)" % (fives, ones, n), "%d < 5" % ones],
        }


def _g_pictograph():
    for key in (2, 5, 10):
        for whole in range(2, 10):
            for half in (0, 1):
                total = whole * key + half * key // 2
                if key % 2 and half:
                    continue
                sym = "$%d$ whole symbols" % whole
                if half:
                    sym += " and a half symbol"
                # Built as one plain sentence, not a nested format: an
                # explanation assembled from a conditional fragment that
                # carries its own $...$ is how the Grade 5 bank once shipped a
                # garbled line.
                if half:
                    why = ("$%d \\times %d = %d$, and half a symbol is $%d$ more, "
                           "giving $%d$." % (whole, key, whole * key, key // 2, total))
                else:
                    why = ("$%d$ symbols worth $%d$ each: $%d \\times %d = %d$."
                           % (whole, key, whole, key, total))
                yield {
                    "statement": ("On a pictograph one symbol stands for $%d$ books. "
                                  "A row shows %s. How many books is that?" % (key, sym)),
                    "correct": total,
                    # counted symbols not books / one symbol too many / forgot
                    # that the key multiplies
                    "dvals": [whole + half, total + key, whole * (key + 1)],
                    "explanation": why,
                    "check": ["Eq(%d*%d + %d, %d)" % (whole, key, half * key // 2, total)],
                }


def _g_table_total():
    ROWS = [("Monday", "Tuesday", "Wednesday"), ("red", "blue", "green"),
            ("Grade 3", "Grade 4", "Grade 5")]
    i = 0
    for a in (12, 18, 24, 31, 45, 52):
        for b in (9, 15, 27, 33, 41):
            for c in (7, 14, 22):
                i += 1
                total = a + b + c
                names = ROWS[i % len(ROWS)]
                yield {
                    "statement": ("A table shows %s: $%d$, %s: $%d$, %s: $%d$. "
                                  "What is the total?" % (names[0], a, names[1], b,
                                                          names[2], c)),
                    "correct": total,
                    # forgot the last row / carried wrong / dropped the first row
                    "dvals": [a + b, total + 10, b + c],
                    "explanation": ("Add every row: $%d + %d + %d = %d$." % (a, b, c, total)),
                    "check": ["Eq(%d + %d + %d, %d)" % (a, b, c, total)],
                }


def _g_bar_scale():
    for step in (2, 5, 10, 20):
        for lines in range(2, 10):
            v = step * lines
            yield {
                "statement": ("On a bar chart each gridline is worth $%d$. A bar reaches "
                              "the $%d$th gridline. What value does it show?" % (step, lines)),
                "correct": v,
                "dvals": [lines, v + step, lines + step],
                "explanation": ("Gridlines times the step: $%d \\times %d = %d$. Counting "
                                "gridlines as ones would give $%d$, the classic slip."
                                % (lines, step, v, lines)),
                "check": ["Eq(%d*%d, %d)" % (lines, step, v)],
            }


def _g_compare_categories():
    i = 0
    for a in (14, 22, 35, 48, 56, 63, 71):
        for b in (8, 17, 29, 41, 52):
            i += 1
            if a == b:
                continue
            hi, lo = max(a, b), min(a, b)
            yield {
                "statement": ("A bar chart shows $%d$ for football and $%d$ for basketball. "
                              "How many more chose the more popular sport?" % (a, b)),
                "correct": hi - lo,
                "dvals": [hi + lo, hi - lo + 1, lo],
                "explanation": ("The taller bar is $%d$ and the shorter is $%d$: "
                                "$%d - %d = %d$ more." % (hi, lo, hi, lo, hi - lo)),
                "check": ["Eq(%d - %d, %d)" % (hi, lo, hi - lo), "%d >= %d" % (hi, lo)],
            }


def _g_data_question():
    i = 0
    for a in (12, 20, 28, 36, 44):
        for b in (15, 25, 33, 41):
            for c in (9, 18, 27):
                i += 1
                total = a + b + c
                hi = max(a, b, c)
                yield {
                    "statement": ("Three classes collected $%d$, $%d$ and $%d$ bottles. "
                                  "Which statement is true?" % (a, b, c)),
                    "correct": "Altogether they collected $%d$ bottles." % total,
                    "dvals": ["Altogether they collected $%d$ bottles." % (total + 10),
                              "The largest number collected was $%d$." % (hi + 5),
                              "All three classes collected the same number."],
                    "explanation": ("Add all three: $%d + %d + %d = %d$. The largest single "
                                    "class collected $%d$." % (a, b, c, total, hi)),
                    "check": ["Eq(%d + %d + %d, %d)" % (a, b, c, total),
                              "%d >= %d" % (hi, a), "%d >= %d" % (hi, b), "%d >= %d" % (hi, c)],
                }


# ===========================================================================

def build():
    forms = []

    U1 = "numbers-to-10000"
    forms += [
        form("g4-place-value", "What a digit is worth", 1, U1,
             "A digit's value is the digit times its place — read the column, not the digit.",
             mk_txt("g4-pv", _g_place_value())),
        form("g4-words-numeral", "Words into numerals", 1, U1,
             "Thousands, hundreds, tens and ones, in that order — a missing hundred is a zero.",
             mk_txt("g4-wn", _g_words_to_numeral())),
        form("g4-compare", "Comparing four-digit numbers", 2, U1,
             "Compare from the left; the first column that differs decides it.",
             mk_txt("g4-cmp", _g_compare_numbers())),
        form("g4-rounding", "Rounding", 2, U1,
             "Find the two neighbours, then choose the nearer one.",
             mk_txt("g4-rnd", _g_rounding())),
        form("g4-expanded", "Expanded form", 2, U1,
             "Every digit contributes its place value; a zero contributes nothing.",
             mk_txt("g4-exp", _g_expanded_form())),
        form("g4-pattern", "Number patterns", 3, U1,
             "Find the step by subtracting neighbours, then keep stepping.",
             mk_txt("g4-pat", _g_number_pattern())),
    ]

    U2 = "addition-and-subtraction"
    forms += [
        form("g4-column-add", "Column addition", 1, U2,
             "Line up the places, add from the right, carry past nine.",
             mk_txt("g4-ca", _g_column_add())),
        form("g4-column-sub", "Column subtraction", 1, U2,
             "Regroup where the top digit is smaller, then check by adding back.",
             mk_txt("g4-cs", _g_column_sub())),
        form("g4-missing", "Missing numbers", 2, U2,
             "The box is the missing part: whole minus the part you know.",
             mk_txt("g4-mn", _g_missing_number())),
        form("g4-mental", "Mental strategies", 2, U2,
             "Add the round number, then take back what you added too much.",
             mk_txt("g4-ms", _g_mental_strategy())),
        form("g4-word-add", "Word problems", 2, U2,
             "Decide what the story does to the number before you calculate.",
             mk_txt("g4-wa", _g_word_problem_add())),
        form("g4-inverse", "Checking by the inverse", 3, U2,
             "Addition undoes subtraction — answer plus what was taken away.",
             mk_txt("g4-inv", _g_inverse_check())),
    ]

    U3 = "times-tables-and-multiplication"
    forms += [
        form("g4-tables-easy", "Tables of 2, 5 and 10", 1, U3,
             "The tables that come first, straight from equal groups.",
             mk_num("g4-t1", _g_tables_2_5_10())),
        form("g4-tables-hard", "Tables of 6 to 9", 1, U3,
             "The harder tables — one group more or less is the fastest repair.",
             mk_num("g4-t2", _g_tables_6_9())),
        form("g4-equal-groups", "Equal groups", 2, U3,
             "Equal groups joined together means multiply.",
             mk_num("g4-eg", _g_equal_groups())),
        form("g4-arrays", "Arrays and the turnaround", 2, U3,
             "Rows times columns, and turning the array does not change the total.",
             mk_txt("g4-ar", _g_arrays_turnaround())),
        form("g4-multiply-2d", "Multiplying bigger numbers", 2, U3,
             "Split into tens and ones, multiply each, then add.",
             mk_txt("g4-m2", _g_multiply_two_digit())),
        form("g4-missing-factor", "Missing factors", 3, U3,
             "Ask how many of one number make the other.",
             mk_num("g4-mf", _g_missing_factor())),
    ]

    U4 = "division-and-sharing"
    forms += [
        form("g4-div-facts", "Division facts", 1, U4,
             "Every division fact is a times-table fact read backwards.",
             mk_num("g4-df", _g_division_facts())),
        form("g4-sharing", "Sharing equally", 1, U4,
             "Sharing between people means divide by how many people.",
             mk_num("g4-sh", _g_sharing())),
        form("g4-remainders", "Remainders", 2, U4,
             "The remainder is what will not fill another group, and it is always smaller than the divisor.",
             mk_txt("g4-rm", _g_remainders())),
        form("g4-halving", "Halving", 2, U4,
             "Half is division by two, checked by doubling back.",
             mk_num("g4-hv", _g_halving())),
        form("g4-choose-op", "Multiply or divide?", 2, U4,
             "Groups joined means multiply; a total split into groups means divide.",
             mk_txt("g4-co", _g_choose_operation())),
        form("g4-remainder-meaning", "What the remainder means", 3, U4,
             "Sometimes the leftover needs a whole extra group — read the story, not just the numbers.",
             mk_num("g4-rmm", _g_remainder_meaning())),
    ]

    U5 = "fractions-parts-of-a-whole"
    forms += [
        form("g4-name-fraction", "Naming a fraction", 1, U5,
             "The bottom counts the equal parts, the top counts the ones you have.",
             mk_txt("g4-nf", _g_name_fraction())),
        form("g4-unit-fraction", "Unit fractions of an amount", 1, U5,
             "One part out of the whole: divide by the bottom number.",
             mk_num("g4-uf", _g_unit_fraction())),
        form("g4-compare-denom", "Comparing with the same bottom", 2, U5,
             "Same-size parts, so more parts means more.",
             mk_txt("g4-cd", _g_compare_same_denominator())),
        form("g4-compare-num", "Comparing with the same top", 2, U5,
             "Fewer parts in the whole makes each part bigger.",
             mk_txt("g4-cn", _g_compare_same_numerator())),
        form("g4-fraction-set", "A fraction of a set", 2, U5,
             "Find one part first, then take as many as the top says.",
             mk_num("g4-fs", _g_fraction_of_set())),
        form("g4-equivalent", "Equivalent fractions", 3, U5,
             "Multiply the top and the bottom by the same number and the value is unchanged.",
             mk_txt("g4-eq", _g_equivalent_fractions())),
    ]

    U6 = "shapes-and-symmetry"
    forms += [
        form("g4-shape-sides", "Sides and corners", 1, U6,
             "Naming shapes by how many sides they have.",
             mk_num("g4-ss", _g_shape_sides())),
        form("g4-right-angles", "Right angles", 1, U6,
             "A right angle is a square corner — count them shape by shape.",
             mk_num("g4-ra", _g_right_angles())),
        form("g4-quadrilaterals", "Sorting quadrilaterals", 2, U6,
             "Four-sided shapes sorted by equal sides, parallel sides and right angles.",
             mk_txt("g4-qd", _g_quadrilaterals())),
        form("g4-symmetry", "Lines of symmetry", 2, U6,
             "A line of symmetry folds the shape exactly onto itself.",
             mk_num("g4-sy", _g_symmetry_lines())),
        form("g4-solids", "3-D solids", 2, U6,
             "Faces, edges and vertices — the three things you count on a solid.",
             mk_num("g4-sd", _g_solids())),
        form("g4-perimeter", "Perimeter of a regular shape", 3, U6,
             "Perimeter is the distance all the way round: sides times side length.",
             mk_num("g4-pm", _g_perimeter())),
    ]

    U7 = "measurement-time-and-money"
    forms += [
        form("g4-length", "Metres and centimetres", 1, U7,
             "One metre is one hundred centimetres.",
             mk_txt("g4-ln", _g_length())),
        form("g4-mass-capacity", "Grams, kilograms, millilitres and litres", 1, U7,
             "One kilogram is a thousand grams; one litre is a thousand millilitres.",
             mk_txt("g4-mc", _g_mass_capacity())),
        form("g4-clock", "Reading the clock", 2, U7,
             "Quarter past, half past and quarter to — and which hour they belong to.",
             mk_txt("g4-cl", _g_clock())),
        form("g4-duration", "How long it lasts", 2, U7,
             "Start time plus length gives the end time, counting sixty to the hour.",
             mk_txt("g4-du", _g_duration())),
        form("g4-money", "Tögrög and change", 2, U7,
             "Adding prices, and change as what is left from the note.",
             mk_txt("g4-mo", _g_money())),
        form("g4-convert-first", "Change the units first", 3, U7,
             "Two units in one problem: make them the same before you calculate.",
             mk_txt("g4-cf", _g_convert_first())),
    ]

    U8 = "data-and-pictographs"
    forms += [
        form("g4-tally", "Tally marks", 1, U8,
             "Each full gate is five, and the singles are added on.",
             mk_num("g4-tl", _g_tally())),
        form("g4-pictograph", "Pictograph keys", 1, U8,
             "Value = symbols times the key, and half a symbol is half the key.",
             mk_num("g4-pg", _g_pictograph())),
        form("g4-table-total", "Tables and totals", 2, U8,
             "Every row counts towards the total.",
             mk_num("g4-tt", _g_table_total())),
        form("g4-bar-scale", "Reading a bar chart's scale", 2, U8,
             "Gridlines times the step — counting gridlines as ones is the classic error.",
             mk_num("g4-bs", _g_bar_scale())),
        form("g4-compare-cats", "Comparing two bars", 2, U8,
             "How many more is a subtraction, not a total.",
             mk_num("g4-cc", _g_compare_categories())),
        form("g4-data-question", "Asking questions of data", 3, U8,
             "Check each statement against the numbers before choosing.",
             mk_txt("g4-dq", _g_data_question())),
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
