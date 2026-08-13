# -*- coding: utf-8 -*-
"""Problem-bank subject: Grade 2 — mirrors /math/3.

One collection PER UNIT: each of the eight Grade 2 topics gets its own set of
forms, its own unit page and its own practice session
(/math/problem-bank/3/<unit>/practice), so a student drilling times tables is
never handed a clock question.

Every problem is generated from a parameter SWEEP and every answer is
COMPUTED, never typed. Values stay exact: sympy checks are built from
Integer/Rational, never from float division.

Grade 2 house rules (the same ones scripts/primary_check.py enforces on the
lessons at a ceiling of 1000, applied here by hand because the bank has its
own gate):
  - nothing above 1000, because that is the year's number range;
  - no decimals and no negatives — both are later years;
  - division comes out EXACTLY, with no remainder (remainders are Grade 4's),
    and every division carries its multiplication receipt;
  - fraction denominators are 2, 3 and 4 only, written as the picture shows
    them and never silently reduced;
  - the tögrög is written as a WORD, outside math (KaTeX cannot draw the sign);
  - numbers below 1000 need no thousands separator, so none is used — money()
    is deliberately not imported here;
  - reading level stays at eight years old: short sentences, concrete nouns.

Self-check:  python3 scripts/pb/grade3.py
Regenerate:  python3 scripts/build_problembank.py
"""
import os
import re
import sys

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import form, mk_num, mk_txt  # noqa: E402

SLUG = "2"
TITLE = "Grade 2"
TITLE_MN = "2-р анги"
BLURB = ("Unit-by-unit practice for the whole Grade 2 year — numbers to 1000, "
         "the four operations, first fractions, shapes, measuring and data, "
         "with a separate problem set for every unit.")

UNITS = [
    {"id": "numbers-to-1000", "title": "Numbers to 1000",
     "blurb": "Hundreds, tens and ones, words and digits, comparing and ordering, step counting and rounding to the nearest ten."},
    {"id": "addition-and-subtraction-to-1000", "title": "Addition & Subtraction to 1000",
     "blurb": "Mental tens and hundreds, column addition with a carry, column subtraction with a break, fact families and word problems."},
    {"id": "multiplication-first-facts", "title": "Multiplication — First Facts",
     "blurb": "Equal groups, arrays and the turnaround, the tables of 2, 5 and 10, the threes and fours, and times one and times zero."},
    {"id": "division-sharing-and-grouping", "title": "Division — Sharing & Grouping",
     "blurb": "Sharing into equal parts, grouping into bundles, division facts from the tables, dividing by 3 and 4, and choosing the operation."},
    {"id": "fractions-halves-and-quarters", "title": "Fractions — Halves, Thirds & Quarters",
     "blurb": "Naming equal parts, how many make a whole, comparing unit fractions, the leftover part, and a fraction of a set."},
    {"id": "shapes-sides-and-corners", "title": "Shapes, Sides & Corners",
     "blurb": "Naming flat shapes by their sides, square corners, solid shapes and what they do, shape patterns and sorting."},
    {"id": "measuring-time-and-money", "title": "Measuring, Time & Money",
     "blurb": "Reading a ruler, metres and centimetres, comparing mass and capacity, o'clock and half past, and counting tögrög."},
    {"id": "tallies-and-picture-graphs", "title": "Tallies & Picture Graphs",
     "blurb": "Reading and drawing tallies, table totals and missing rows, one-for-one picture graphs and the questions they answer."},
]

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
    """A three-digit number in words, the way it is read aloud."""
    assert 0 < n <= 1000, "words: %r outside the Grade 2 range" % (n,)
    if n == 1000:
        return "one thousand"
    h, rest = divmod(n, 100)
    if h == 0:
        return words_under_100(rest)
    out = "%s hundred" % ONES[h]
    if rest:
        out += " and %s" % words_under_100(rest)
    return out


def frac(a, b):
    """A fraction written EXACTLY as given, never reduced.

    Grade 2 meets fractions as "how many of the equal parts", so two shaded
    pieces of four must read 2/4 — that is what the child can see. The sympy
    checks still use Rational, so the maths is exact even though the display
    is not in lowest terms."""
    return "\\frac{%d}{%d}" % (a, b)



# Objects a fraction can be "of". Varying the object is not decoration: the
# bank keys distinctness on the STATEMENT, so a form that asks about a bar
# eight times ships one question, not eight.
FRAC_OBJECTS = ["bar", "bread", "cake", "ribbon", "rug", "plank",
                "strip of felt", "loaf", "board", "belt", "sheet", "rope"]


def _frac_distractors(num, den, count=3):
    """Three wrong fractions, distinct from the answer AS RENDERED STRINGS.

    Chosen from a fixed pool in order of how plausible the mistake is —
    upside down first, then the complement, then a single part — falling
    through to other legal denominators when an earlier candidate happens to
    render the same as the answer. Picking them by formula instead was what
    silently dropped whole draws: 2/4's complement IS 2/4."""
    right = frac(num, den)
    cands = [(den, num), (den - num, den), (1, den), (den, den)]
    for d2 in (2, 3, 4):
        for n2 in range(1, d2 + 1):
            cands.append((n2, d2))
    out, seen = [], {right}
    for a, b in cands:
        if not (b in (2, 3, 4) and 0 < a <= b):
            continue
        text = frac(a, b)
        if text in seen:
            continue
        seen.add(text)
        out.append("$%s$" % text)
        if len(out) == count:
            break
    return out


# ===========================================================================
# Unit 1 — Numbers to 1000
# ===========================================================================

def _g_place_value():
    """Every draw's three distractors are the SAME digit read in the wrong
    column, plus the whole number — the actual mistakes a child makes. They
    have to be chosen per column: reusing one formula across all three places
    makes a distractor collide with the answer and silently drops the draw."""
    names = {2: "hundreds", 1: "tens", 0: "ones"}
    for h in range(1, 10):
        for t in (2, 4, 6, 8):
            for o in (3, 7):
                n = 100 * h + 10 * t + o
                for place, digit in ((2, h), (1, t), (0, o)):
                    worth = digit * 10 ** place
                    if place == 2:
                        dvals = [digit, digit * 10, n]
                    elif place == 1:
                        dvals = [digit, digit * 100, n]
                    else:
                        dvals = [digit * 10, digit * 100, n]
                    yield {
                        "statement": ("In the number $%d$, what is the digit $%d$ in the "
                                      "%s column worth?" % (n, digit, names[place])),
                        "correct": worth,
                        "dvals": dvals,
                        "explanation": ("The $%d$ stands in the %s column, so it counts "
                                        "$%d$ %s: $%d \\times %d = %d$."
                                        % (digit, names[place], digit, names[place],
                                           digit, 10 ** place, worth)),
                        "check": ["Eq(%d*%d, %d)" % (digit, 10 ** place, worth),
                                  "Eq(%d + %d + %d, %d)" % (h * 100, t * 10, o, n)],
                    }


def _g_words_to_digits():
    for h in range(1, 10):
        for rest in (0, 4, 15, 30, 47, 60, 8, 19):
            n = 100 * h + rest
            swapped = 100 * h + (rest % 10) * 10 + rest // 10 if rest >= 10 else n + 10
            yield {
                "statement": ("Write \"%s\" in digits." % words(n)),
                "correct": n,
                "dvals": [n + 100, swapped if swapped != n else n + 1, n - h * 100 if rest else n + 9],
                "explanation": ("$%d$ hundreds, $%d$ tens and $%d$ ones: "
                                "$%d + %d + %d = %d$."
                                % (h, rest // 10, rest % 10, h * 100,
                                   (rest // 10) * 10, rest % 10, n)),
                "check": ["Eq(%d + %d + %d, %d)"
                          % (h * 100, (rest // 10) * 10, rest % 10, n)],
            }


def _g_compare():
    pairs = []
    for h in range(1, 10):
        for d in (1, 2, 3):
            if h + d <= 9:
                pairs.append((100 * h + 47, 100 * (h + d) + 12))
        pairs.append((100 * h + 30, 100 * h + 70))
        pairs.append((100 * h + 5, 100 * h + 50))
    for a, b in pairs:
        big, small = max(a, b), min(a, b)
        yield {
            "statement": ("Which sign belongs between $%d$ and $%d$?" % (a, b)),
            "correct": "$%d %s %d$" % (a, ">" if a > b else "<", b),
            "dvals": ["$%d %s %d$" % (a, "<" if a > b else ">", b),
                      "$%d = %d$" % (a, b),
                      "$%d %s %d$" % (b, ">" if a > b else "<", a)],
            "explanation": ("Compare from the left. The first column where the "
                            "digits differ decides, and $%d$ is the larger by "
                            "$%d$." % (big, big - small)),
            "check": ["%d > %d" % (big, small),
                      "Eq(%d - %d, %d)" % (big, small, big - small)],
        }


def _g_order():
    for h in range(1, 9):
        for gap in (1, 2, 3):
            if h + gap > 9:
                continue
            for lo_tens in (0, 1):
                a = 100 * h + 9 + lo_tens
                b = 100 * h + 90
                c = 100 * (h + gap) + 5
                yield {
                    "statement": ("Put $%d$, $%d$ and $%d$ in order, smallest "
                                  "first. Which comes FIRST?" % (b, c, a)),
                    "correct": a,
                    "dvals": [b, c, a + 100],
                    "explanation": ("$%d$ and $%d$ share their hundreds digit, so "
                                    "the tens decide and $%d$ is smaller; $%d$ has "
                                    "more hundreds than both." % (a, b, a, c)),
                    "check": ["%d < %d" % (a, b), "%d < %d" % (b, c)],
                }


def _g_step_count():
    for step in (2, 5, 10, 100):
        for start in range(step, 400, 17):
            s = start - start % step if step in (5, 10, 100) else start - start % 2
            if s < step:
                continue
            third = s + 2 * step
            nxt = s + 3 * step
            if nxt > 1000:
                continue
            yield {
                "statement": ("A count in %ds reads $%d$, $%d$, $%d$. What comes "
                              "next?" % (step, s, s + step, third)),
                "correct": nxt,
                "dvals": [third + 1, nxt + step, third],
                "explanation": ("Every gap is $%d$, so the next number is "
                                "$%d + %d = %d$." % (step, third, step, nxt)),
                "check": ["Eq(%d + %d, %d)" % (third, step, nxt),
                          "Eq(%d - %d, %d)" % (s + step, s, step)],
            }


def _g_round_ten():
    for n in range(11, 700, 7):
        low = n - n % 10
        high = low + 10
        up = n % 10 >= 5
        ans = high if up else low
        yield {
            "statement": "Round $%d$ to the nearest ten." % n,
            "correct": ans,
            "dvals": [low if up else high, n, ans + 10],
            "explanation": ("$%d$ sits between $%d$ and $%d$. It is $%d$ above "
                            "$%d$ and $%d$ below $%d$, so %s is nearer."
                            % (n, low, high, n - low, low, high - n, high,
                               "the upper ten" if up else "the lower ten")
                            if n % 10 != 5 else
                            "$%d$ is exactly halfway between $%d$ and $%d$, and "
                            "the agreed rule rounds a half UP to $%d$."
                            % (n, low, high, high)),
            "check": ["Eq(%d - %d, %d)" % (n, low, n - low),
                      "Eq(%d - %d, %d)" % (high, n, high - n)],
        }


# ===========================================================================
# Unit 2 — Addition & Subtraction to 1000
# ===========================================================================

def _g_mental_hundreds():
    for a in range(105, 700, 23):
        for add in (100, 200, 300):
            if a + add > 1000:
                continue
            yield {
                "statement": "Work out $%d + %d$ in your head." % (a, add),
                "correct": a + add,
                "dvals": [a + add // 10, a + add + 100, a + add // 100],
                "explanation": ("$%d$ is $%d$ whole hundreds, so only the "
                                "hundreds digit moves: $%d + %d = %d$, with the "
                                "tens and ones copied down."
                                % (add, add // 100, a, add, a + add)),
                "check": ["Eq(%d + %d, %d)" % (a, add, a + add),
                          "Eq(Mod(%d, 100), Mod(%d, 100))" % (a + add, a)],
            }


def _g_column_add():
    for a in range(126, 700, 31):
        for b in range(117, 300, 29):
            if a + b > 1000:
                continue
            if (a % 10) + (b % 10) < 10:
                continue                      # this form drills the carry
            no_carry = a + b - 10
            yield {
                "statement": "Add $%d + %d$." % (a, b),
                "correct": a + b,
                "dvals": [no_carry, a + b + 90, a + b - 100],
                "explanation": ("Ones: $%d + %d = %d$ — write $%d$ and carry a "
                                "ten. Adding the rest gives $%d$. Forgetting the "
                                "carry costs exactly ten."
                                % (a % 10, b % 10, a % 10 + b % 10,
                                   (a % 10 + b % 10) % 10, a + b)),
                "check": ["Eq(%d + %d, %d)" % (a, b, a + b),
                          "Eq(%d + %d, %d)" % (a % 10, b % 10, a % 10 + b % 10),
                          "%d > 9" % (a % 10 + b % 10)],
            }


def _g_column_sub():
    for a in range(231, 950, 37):
        for b in range(118, 400, 43):
            if b >= a:
                continue
            if (a % 10) >= (b % 10):
                continue                      # this form drills the break
            yield {
                "statement": "Work out $%d - %d$." % (a, b),
                "correct": a - b,
                "dvals": [a - b + 10, a - b + 2 * ((b % 10) - (a % 10)), a - b + 100],
                "explanation": ("The ones column is short, so break a ten: "
                                "$%d - %d = %d$ in the ones. The answer is $%d$, "
                                "and the receipt $%d + %d = %d$ proves it."
                                % (a % 10 + 10, b % 10, a % 10 + 10 - b % 10,
                                   a - b, a - b, b, a)),
                "check": ["Eq(%d - %d, %d)" % (a, b, a - b),
                          "Eq(%d + %d, %d)" % (a - b, b, a),
                          "%d < %d" % (a % 10, b % 10)],
            }


def _g_fact_family():
    for p in range(30, 500, 23):
        for q in range(40, 400, 37):
            if p + q > 1000:
                continue
            whole = p + q
            yield {
                "statement": ("Two parts of $%d$ and $%d$ make a whole. Which "
                              "fact does NOT belong to their family?"
                              % (p, q)),
                "correct": "$%d - %d = %d$" % (p, whole, q),
                "dvals": ["$%d + %d = %d$" % (p, q, whole),
                          "$%d - %d = %d$" % (whole, p, q),
                          "$%d - %d = %d$" % (whole, q, p)],
                "explanation": ("The whole, $%d$, always leads a subtraction — "
                                "you cannot take it away from one of its own "
                                "parts. The other three facts are the family."
                                % whole),
                "check": ["Eq(%d + %d, %d)" % (p, q, whole),
                          "Eq(%d - %d, %d)" % (whole, p, q),
                          "%d > %d" % (whole, p)],
            }


def _g_missing_number():
    for known in range(30, 500, 19):
        for whole in range(520, 1000, 41):
            if known >= whole:
                continue
            miss = whole - known
            yield {
                "statement": ("Find the missing number: $\\square + %d = %d$."
                              % (known, whole)),
                "correct": miss,
                # `whole + known` was the natural "added instead of
                # subtracting" distractor and it ran past 1500 — outside the
                # year's number range, which is a rule the bank keeps by hand.
                "dvals": [known, miss + 10, miss - 10],
                "explanation": ("The whole $%d$ is showing, so the gap is a "
                                "PART: $%d - %d = %d$. Check: $%d + %d = %d$."
                                % (whole, whole, known, miss, miss, known, whole)),
                "check": ["Eq(%d - %d, %d)" % (whole, known, miss),
                          "Eq(%d + %d, %d)" % (miss, known, whole)],
            }


def _g_word_two_step():
    for start in range(300, 900, 47):
        for spend in range(60, 300, 53):
            for gain in (30, 50, 80):
                if spend >= start:
                    continue
                mid = start - spend
                end = mid + gain
                if end > 1000 or mid <= gain:
                    continue      # `mid - gain` is a distractor; keep it positive
                yield {
                    "statement": ("A shop had $%d$ eggs, sold $%d$, then received "
                                  "$%d$ more. How many now?" % (start, spend, gain)),
                    "correct": end,
                    "dvals": [mid, start + spend + gain, mid - gain],
                    "explanation": ("Selling splits: $%d - %d = %d$. The delivery "
                                    "joins: $%d + %d = %d$. The middle number "
                                    "$%d$ is the shop between the two events, "
                                    "not the answer."
                                    % (start, spend, mid, mid, gain, end, mid)),
                    "check": ["Eq(%d - %d, %d)" % (start, spend, mid),
                              "Eq(%d + %d, %d)" % (mid, gain, end)],
                }


# ===========================================================================
# Unit 3 — Multiplication — First Facts
# ===========================================================================

def _g_equal_groups():
    for g in range(2, 9):
        for s in range(2, 11):
            yield {
                "statement": ("There are $%d$ baskets with $%d$ eggs in each. "
                              "How many eggs?" % (g, s)),
                "correct": g * s,
                "dvals": [g + s, g * s + s, g * s - s],
                "explanation": ("%d groups of %d: %s $= %d$, which is "
                                "$%d \\times %d$."
                                % (g, s, " + ".join([str(s)] * min(g, 5))
                                   + (" + ..." if g > 5 else ""), g * s, g, s)),
                "check": ["Eq(%d*%d, %d)" % (g, s, g * s),
                          "Eq(%d + %d, %d)" % (g, s, g + s)],
            }


def _g_turnaround():
    for r in range(2, 9):
        for c in range(2, 11):
            if r == c:
                continue
            yield {
                "statement": ("An array has $%d$ rows of $%d$. Reading it down "
                              "the columns instead gives which fact?" % (r, c)),
                "correct": "$%d \\times %d = %d$" % (c, r, r * c),
                "dvals": ["$%d \\times %d = %d$" % (c, r, r * c + c),
                          "$%d + %d = %d$" % (r, c, r + c),
                          "$%d \\times %d = %d$" % (r, c, r * c + r)],
                "explanation": ("The same stones read the other way: $%d$ "
                                "columns of $%d$, so $%d \\times %d = %d$ — the "
                                "turnaround, and the total cannot change."
                                % (c, r, c, r, r * c)),
                "check": ["Eq(%d*%d, %d)" % (c, r, r * c),
                          "Eq(%d*%d, %d*%d)" % (r, c, c, r)],
            }


def _g_friendly_tables():
    for t in (2, 5, 10):
        for k in range(2, 11):
            p = t * k
            yield {
                "statement": "What is $%d \\times %d$?" % (t, k),
                "correct": p,
                "dvals": [t + k, p + t, p - t],
                "explanation": ("%s: $%d \\times %d = %d$."
                                % ({2: "Double it", 5: "Count the fives",
                                    10: "Whole bundles of ten"}[t], t, k, p)),
                "check": ["Eq(%d*%d, %d)" % (t, k, p),
                          "Eq(Mod(%d, %d), 0)" % (p, t)],
            }


def _g_threes_fours():
    for t in (3, 4):
        for k in range(2, 15):
            p = t * k
            if t == 4:
                why = ("Four groups is two groups counted twice: "
                       "$2 \\times %d = %d$, doubled to $%d$." % (k, 2 * k, p))
                chk = ["Eq(2*%d, %d)" % (k, 2 * k),
                       "Eq(%d + %d, %d)" % (2 * k, 2 * k, p),
                       "Eq(%d*%d, %d)" % (t, k, p)]
            else:
                why = ("Count in threes to the $%d$th stop: "
                       "$3 \\times %d = %d$." % (k, k, p))
                chk = ["Eq(3*%d, %d)" % (k, p),
                       "Eq(%d + 3, %d)" % (p, p + 3)]
            yield {
                "statement": "What is $%d \\times %d$?" % (t, k),
                "correct": p,
                "dvals": [t + k, p + t, p - t],
                "explanation": why,
                "check": chk,
            }


def _g_one_and_zero():
    for n in range(1, 21):
        yield {
            "statement": "What is $%d \\times 1$?" % n,
            "correct": n,
            "dvals": [1, n + 1, 0],
            "explanation": ("$%d$ groups of one hold one thing each, so the "
                            "answer is $%d$ — multiplying by one leaves a "
                            "number alone." % (n, n)),
            "check": ["Eq(%d*1, %d)" % (n, n)],
        }
    for n in range(2, 21):
        yield {
            "statement": "What is $%d \\times 0$?" % n,
            "correct": 0,
            "dvals": [n, 1, n * 10],
            "explanation": ("$%d$ empty groups hold nothing at all: the answer "
                            "is $0$. The $%d$ counts the groups, and there is "
                            "nothing inside any of them." % (n, n)),
            "check": ["Eq(%d*0, 0)" % n, "Eq(0*%d, 0)" % n],
        }


def _g_times_story():
    nouns = [("shelf", "shelves", "jars"), ("bag", "bags", "buuz"),
             ("post", "posts", "horses"), ("box", "boxes", "pencils")]
    for gi, (sing, plur, thing) in enumerate(nouns):
        for g in range(2, 9):
            for s in (3, 4, 5, 6):
                yield {
                    "statement": ("There are $%d$ %s with $%d$ %s on each. How "
                                  "many %s altogether?" % (g, plur, s, thing, thing)),
                    "correct": g * s,
                    "dvals": [g + s, g * s + g, abs(s - g) + g * 2],
                    "explanation": ("Equal groups, so multiply: "
                                    "$%d \\times %d = %d$ %s. Adding would give "
                                    "$%d$, which counts nothing in the story."
                                    % (g, s, g * s, thing, g + s)),
                    "check": ["Eq(%d*%d, %d)" % (g, s, g * s),
                              "Eq(%d + %d, %d)" % (g, s, g + s)],
                }


# ===========================================================================
# Unit 4 — Division — Sharing & Grouping
# ===========================================================================

def _g_sharing():
    for people in (2, 3, 4, 5, 10):
        for each in range(2, 11):
            total = people * each
            yield {
                "statement": ("$%d$ sweets are shared equally between $%d$ "
                              "children. How many does each child get?"
                              % (total, people)),
                "correct": each,
                "dvals": [people, total - people, total + people],
                "explanation": ("$%d \\times %d = %d$, so each share is $%d$. "
                                "The receipt puts the shares back together and "
                                "returns the pile."
                                % (people, each, total, each)),
                "check": ["Eq(%d*%d, %d)" % (people, each, total),
                          "Eq(Rational(%d, %d), %d)" % (total, people, each)],
            }


def _g_grouping():
    for size in (2, 3, 4, 5, 10):
        for bags in range(2, 11):
            total = size * bags
            yield {
                "statement": ("$%d$ buuz are packed into bags of $%d$. How many "
                              "bags?" % (total, size)),
                "correct": bags,
                "dvals": [size, total - size, total],
                "explanation": ("Counting up in %ds reaches $%d$ after $%d$ "
                                "steps, so there are $%d$ bags. Receipt: "
                                "$%d \\times %d = %d$."
                                % (size, total, bags, bags, bags, size, total)),
                "check": ["Eq(%d*%d, %d)" % (bags, size, total),
                          "Eq(Rational(%d, %d), %d)" % (total, size, bags)],
            }


def _g_division_facts():
    for d in (2, 5, 10):
        for q in range(2, 13):
            n = d * q
            yield {
                "statement": "What is $%d \\div %d$?" % (n, d),
                "correct": q,
                "dvals": [d, n - d, n + d],
                "explanation": ("Read the times table backwards: "
                                "$%d \\times %d = %d$, so $%d \\div %d = %d$."
                                % (d, q, n, n, d, q)),
                "check": ["Eq(%d*%d, %d)" % (d, q, n),
                          "Eq(Rational(%d, %d), %d)" % (n, d, q)],
            }


def _g_divide_three_four():
    for d in (3, 4):
        for q in range(2, 16):
            n = d * q
            if d == 4:
                why = ("Halve twice: half of $%d$ is $%d$, and half of that is "
                       "$%d$. Receipt: $4 \\times %d = %d$."
                       % (n, n // 2, q, q, n))
                chk = ["Eq(Rational(%d, 2), %d)" % (n, n // 2),
                       "Eq(Rational(%d, 2), %d)" % (n // 2, q),
                       "Eq(4*%d, %d)" % (q, n)]
            else:
                why = ("Count in threes to $%d$: that takes $%d$ steps. "
                       "Receipt: $3 \\times %d = %d$." % (n, q, q, n))
                chk = ["Eq(3*%d, %d)" % (q, n),
                       "Eq(Rational(%d, 3), %d)" % (n, q)]
            yield {
                "statement": "What is $%d \\div %d$?" % (n, d),
                "correct": q,
                "dvals": [d, n // 2 if d == 4 else n - d, n + d],
                "explanation": why,
                "check": chk,
            }


def _g_receipt_check():
    for d in (2, 3, 4, 5, 10):
        for q in range(3, 12):
            n = d * q
            wrong = q + 1
            yield {
                "statement": ("A pupil answers $%d \\div %d = %d$. What does the "
                              "receipt say?" % (n, d, wrong)),
                "correct": "$%d \\times %d = %d$, so the answer is wrong"
                           % (d, wrong, d * wrong),
                "dvals": ["$%d \\times %d = %d$, so the answer is right"
                          % (d, wrong, n),
                          "$%d + %d = %d$, so the answer is right"
                          % (d, wrong, d + wrong),
                          "the receipt cannot check a division"],
                "explanation": ("Multiplying the answer back gives "
                                "$%d \\times %d = %d$, not $%d$ — so it is "
                                "wrong. The true answer is $%d$, since "
                                "$%d \\times %d = %d$."
                                % (d, wrong, d * wrong, n, q, d, q, n)),
                "check": ["Eq(%d*%d, %d)" % (d, wrong, d * wrong),
                          "Ne(%d, %d)" % (d * wrong, n),
                          "Eq(%d*%d, %d)" % (d, q, n)],
            }


def _g_choose_operation():
    for g in range(2, 9):
        for s in (3, 4, 5, 6):
            total = g * s
            yield {
                "statement": ("$%d$ pencils are packed $%d$ to a box. Which "
                              "operation finds the number of boxes?"
                              % (total, s)),
                "correct": "divide: $%d \\div %d = %d$" % (total, s, g),
                "dvals": ["multiply: $%d \\times %d = %d$" % (total, s, total * s),
                          "add: $%d + %d = %d$" % (total, s, total + s),
                          "subtract: $%d - %d = %d$" % (total, s, total - s)],
                "explanation": ("The total is already given and the number of "
                                "GROUPS is missing, so divide: "
                                "$%d \\div %d = %d$ boxes. Multiplying would "
                                "invent pencils that do not exist."
                                % (total, s, g)),
                "check": ["Eq(Rational(%d, %d), %d)" % (total, s, g),
                          "Eq(%d*%d, %d)" % (g, s, total),
                          "%d > %d" % (total * s, total)],
            }


# ===========================================================================
# Unit 5 — Fractions
# ===========================================================================

def _g_name_fraction():
    for obj in FRAC_OBJECTS:
        for den in (2, 3, 4):
            for num in range(1, den):
                yield {
                    "statement": ("A %s is cut into $%d$ equal parts and $%d$ "
                                  "%s shaded. What fraction is shaded?"
                                  % (obj, den, num, "is" if num == 1 else "are")),
                    "correct": "$%s$" % frac(num, den),
                    "dvals": _frac_distractors(num, den),
                    "explanation": ("The bottom number records the cutting — "
                                    "$%d$ equal parts — and the top counts the "
                                    "pieces shaded, which is $%d$."
                                    % (den, num)),
                    "check": ["Eq(Rational(%d, %d)*%d, %d)" % (num, den, den, num),
                              "%d < %d" % (num, den)],
                }


def _g_make_a_whole():
    for obj in FRAC_OBJECTS:
        for den in (2, 3, 4):
            for taken in range(1, den):
                need = den - taken
                yield {
                    "statement": ("A %s is cut into $%d$ equal parts and $%d$ "
                                  "%s been taken. How many parts are still "
                                  "needed to make a whole %s?"
                                  % (obj, den, taken,
                                     "has" if taken == 1 else "have", obj)),
                    "correct": need,
                    "dvals": [den, den + need, need + 2 * den],
                    "explanation": ("$%d$ parts rebuild the whole and $%d$ %s "
                                    "gone, so $%d - %d = %d$ are still needed."
                                    % (den, taken, "is" if taken == 1 else "are",
                                       den, taken, need)),
                    "check": ["Eq(%d - %d, %d)" % (den, taken, need),
                              "Eq(Rational(%d, %d) + Rational(%d, %d), 1)"
                              % (taken, den, need, den)],
                }


def _g_compare_unit_fractions():
    for obj in FRAC_OBJECTS:
        for a, b in ((2, 3), (2, 4), (3, 4)):
            yield {
                "statement": ("Of the same %s, which is the bigger piece — "
                              "$%s$ or $%s$?" % (obj, frac(1, a), frac(1, b))),
                "correct": "$%s$" % frac(1, a),
                "dvals": ["$%s$" % frac(1, b),
                          "they are equal",
                          "$%s$" % frac(a, b)],
                "explanation": ("Cutting into $%d$ gives bigger pieces than "
                                "cutting the same %s into $%d$ — the bigger "
                                "bottom number always means the smaller piece."
                                % (a, obj, b)),
                "check": ["Rational(1, %d) > Rational(1, %d)" % (a, b),
                          "%d < %d" % (a, b)],
            }


def _g_leftover():
    for obj in FRAC_OBJECTS:
        for den in (2, 3, 4):
            for num in range(1, den):
                left = den - num
                yield {
                    "statement": ("$%s$ of a %s is shaded. What fraction is "
                                  "plain?" % (frac(num, den), obj)),
                    "correct": "$%s$" % frac(left, den),
                    "dvals": _frac_distractors(left, den),
                    "explanation": ("The %s holds $%d$ equal parts and $%d$ "
                                    "%s shaded, so $%d$ remain plain. Shaded and "
                                    "plain always rebuild the whole."
                                    % (obj, den, num,
                                       "is" if num == 1 else "are", left)),
                    "check": ["Eq(Rational(%d, %d) + Rational(%d, %d), 1)"
                              % (num, den, left, den),
                              "Eq(%d - %d, %d)" % (den, num, left)],
                }


def _g_unit_fraction_of_set():
    for den in (2, 3, 4):
        for each in range(2, 13):
            total = den * each
            yield {
                "statement": ("What is $%s$ of $%d$ sweets?" % (frac(1, den), total)),
                "correct": each,
                "dvals": [den, total - den, total],
                "explanation": ("The bottom number makes the groups: share the "
                                "$%d$ into $%d$ equal groups, giving "
                                "$%d \\div %d = %d$ in each."
                                % (total, den, total, den, each)),
                "check": ["Eq(Rational(%d, %d), %d)" % (total, den, each),
                          "Eq(%d*%d, %d)" % (den, each, total)],
            }


def _g_non_unit_of_set():
    for den in (3, 4):
        for num in range(2, den):
            for each in range(2, 11):
                total = den * each
                ans = num * each
                yield {
                    "statement": ("What is $%s$ of $%d$ pencils?"
                                  % (frac(num, den), total)),
                    "correct": ans,
                    "dvals": [each, total, total + each],
                    "explanation": ("Share into $%d$ groups: "
                                    "$%d \\div %d = %d$ in each. Then take $%d$ "
                                    "groups: $%d \\times %d = %d$."
                                    % (den, total, den, each, num, num, each, ans)),
                    "check": ["Eq(Rational(%d, %d), %d)" % (total, den, each),
                              "Eq(%d*%d, %d)" % (num, each, ans),
                              "%d < %d" % (ans, total)],
                }


# ===========================================================================
# Unit 6 — Shapes, Sides & Corners
# ===========================================================================

SHAPES = [("triangle", 3), ("square", 4), ("rectangle", 4)]


SHAPE_CONTEXTS = ["road sign", "tile", "window pane", "biscuit", "patch of felt",
                  "flag", "sticker", "paving stone", "card", "badge",
                  "wooden block", "picture frame"]


def _g_shape_by_sides():
    for ctx in SHAPE_CONTEXTS:
        for name, sides in SHAPES:
            extra = {"square": " and all of them equal",
                     "rectangle": " with two long and two short"}.get(name, "")
            others = [n for n, _ in SHAPES if n != name] + ["circle"]
            yield {
                "statement": ("A %s has $%d$ straight sides%s. What shape is "
                              "it?" % (ctx, sides, extra)),
                "correct": name,
                "dvals": others,
                "explanation": ("$%d$ straight sides%s makes it a %s — and it "
                                "has $%d$ corners to match, so $%d + %d = %d$ "
                                "things to count."
                                % (sides,
                                   " that are all equal" if name == "square" else "",
                                   name, sides, sides, sides, 2 * sides)),
                "check": ["Eq(%d + %d, %d)" % (sides, sides, 2 * sides),
                          "Eq(%d*2, %d)" % (sides, 2 * sides)],
            }


def _g_sides_and_corners():
    for name, sides in SHAPES:
        for count in range(2, 11):
            yield {
                "statement": ("How many sides do $%d$ %ss have altogether?"
                              % (count, name)),
                "correct": count * sides,
                "dvals": [count + sides, sides, count * sides + count],
                "explanation": ("Each %s has $%d$ sides, so $%d$ of them have "
                                "$%d \\times %d = %d$."
                                % (name, sides, count, count, sides, count * sides)),
                "check": ["Eq(%d*%d, %d)" % (count, sides, count * sides)],
            }


def _g_square_corners():
    # Every four-cornered name gives the same arithmetic, so the NAME is what
    # keeps the statements distinct. The triangle used to live here too and
    # silently dropped every draw: it has one square corner, so "how many do
    # N triangles have" answers N — which is also the first distractor.
    for name in ("rectangle", "square", "page"):
        for count in range(1, 10):
            yield {
                "statement": ("How many square corners do $%d$ %ss have "
                              "altogether?" % (count, name)),
                "correct": 4 * count,
                "dvals": [count, count + 4, 5 * count],
                "explanation": ("Each %s has $4$ square corners, so $%d$ of "
                                "them have $%d \\times 4 = %d$."
                                % (name, count, count, 4 * count)),
                "check": ["Eq(%d*4, %d)" % (count, 4 * count)],
            }
    yield {
        "statement": ("At most how many of a triangle's corners can be "
                      "square?"),
        "correct": 1,
        "dvals": [3, 2, 0],
        "explanation": ("Two square corners would send the remaining sides "
                        "alongside each other so they never met, and the "
                        "triangle could not close: $3 - 2 = 1$ is the most "
                        "it can manage."),
        "check": ["Eq(3 - 2, 1)", "Eq(3 + 3, 6)"],
    }


SOLIDS = [("cube", 6), ("cylinder", 2), ("cone", 1), ("sphere", 0)]


def _g_solid_faces():
    # Asking about ONE solid at a time collapsed for the cone (1 face, so the
    # answer equals the number of solids) and the sphere (0 faces, so two
    # distractors tied at zero). Mixing two kinds keeps every draw honest and
    # still drills the same fact: what each solid contributes.
    FACES = {"cube": 6, "cylinder": 2, "cone": 1, "sphere": 0}
    for a_name in ("cube", "cylinder"):
        for b_name in ("cone", "sphere", "cube"):
            if a_name == b_name:
                continue
            for a in range(1, 4):
                for b in range(1, 4):
                    total = a * FACES[a_name] + b * FACES[b_name]
                    yield {
                        "statement": ("How many flat faces do $%d$ %ss and $%d$ "
                                      "%ss have altogether?"
                                      % (a, a_name, b, b_name)),
                        "correct": total,
                        "dvals": [a + b, total + FACES[a_name], total - 1],
                        "explanation": ("A %s has $%d$ flat faces and a %s has "
                                        "$%d$, so $%d \\times %d + %d \\times "
                                        "%d = %d$.%s"
                                        % (a_name, FACES[a_name], b_name,
                                           FACES[b_name], a, FACES[a_name],
                                           b, FACES[b_name], total,
                                           " A sphere is curved all over, so it "
                                           "contributes none." if b_name == "sphere"
                                           else "")),
                        "check": ["Eq(%d*%d + %d*%d, %d)"
                                  % (a, FACES[a_name], b, FACES[b_name], total)],
                    }


def _g_shape_pattern():
    for rep in (2, 3, 4, 5):
        for copies in range(2, 10):
            n = rep * copies
            yield {
                "statement": ("A shape pattern repeats every $%d$ shapes. How "
                              "many shapes are there in $%d$ full repeats?"
                              % (rep, copies)),
                "correct": n,
                "dvals": [rep + copies, n + rep, copies],
                "explanation": ("$%d$ copies of a $%d$-shape repeat: "
                                "$%d \\times %d = %d$ shapes."
                                % (copies, rep, copies, rep, n)),
                "check": ["Eq(%d*%d, %d)" % (copies, rep, n)],
            }


def _g_sorting_rule():
    for ctx in SHAPE_CONTEXTS:
        yield {
            "statement": ("A box of %ss is sorted. Under which rule do a "
                          "square and a rectangle land in DIFFERENT piles?"
                          % ctx),
            "correct": "are all the sides equal?",
            "dvals": ["how many sides does it have?",
                      "does it have square corners?",
                      "is it a flat shape?"],
            "explanation": ("Both have $4$ sides and $4$ square corners, so "
                            "those rules keep them together — $4 + 4 = 8$ "
                            "things to count on each. Only the equal-sides "
                            "rule separates them."),
            "check": ["Eq(4 + 4, 8)", "Eq(4*1, 4)"],
        }
    for ctx in SHAPE_CONTEXTS:
        yield {
            "statement": ("A box of %ss is sorted by number of sides. Which "
                          "shape ends up in a pile of its own, with no sides "
                          "at all?" % ctx),
            "correct": "a circle",
            "dvals": ["a triangle", "a square", "a rectangle"],
            "explanation": ("A corner is where two straight sides meet, and a "
                            "circle has no straight sides — so $0 + 0 = 0$ "
                            "sides and corners."),
            "check": ["Eq(0 + 0, 0)", "Eq(3 + 3, 6)"],
        }
    for name, sides in SHAPES:
        for other, osides in SHAPES:
            if name == other or sides == osides:
                continue
            yield {
                "statement": ("Sorting by number of sides, does a %s share a "
                              "pile with a %s?" % (name, other)),
                "correct": "no — $%d$ sides against $%d$" % (sides, osides),
                "dvals": ["yes — both have $%d$ sides" % sides,
                          "yes — both have $%d$ sides" % osides,
                          "only if their corners match"],
                "explanation": ("A %s has $%d$ straight sides and a %s has "
                                "$%d$, so the rule puts them in different "
                                "piles." % (name, sides, other, osides)),
                "check": ["Ne(%d, %d)" % (sides, osides),
                          "Eq(%d + %d, %d)" % (sides, sides, 2 * sides)],
            }


# ===========================================================================
# Unit 7 — Measuring, Time & Money
# ===========================================================================

def _g_ruler():
    for start in range(0, 8):
        for length in range(2, 10):
            end = start + length
            if end > 15:
                continue
            yield {
                "statement": ("A stick lies along a ruler from the $%d$ cm mark "
                              "to the $%d$ cm mark. How long is it?"
                              % (start, end)),
                "correct": length,
                "dvals": [end, start + end, end + 1],
                "explanation": ("It covers the centimetres from $%d$ to $%d$: "
                                "$%d - %d = %d$ cm. Reading only the far mark "
                                "gives $%d$, which is right only when the "
                                "object starts at zero."
                                % (start, end, end, start, length, end)),
                "check": ["Eq(%d - %d, %d)" % (end, start, length),
                          "Eq(%d + %d, %d)" % (length, start, end)],
            }


def _g_metres():
    for m in range(1, 10):
        yield {
            "statement": "How many centimetres are there in $%d$ metres?" % m,
            "correct": m * 100,
            "dvals": [m * 10, m + 100, m * 100 + 10],
            "explanation": ("Each metre is $100$ centimetres, so "
                            "$%d \\times 100 = %d$ cm." % (m, m * 100)),
            "check": ["Eq(%d*100, %d)" % (m, m * 100)],
        }
    for m in range(1, 10):
        yield {
            "statement": "How many metres is $%d$ cm?" % (m * 100),
            "correct": m,
            "dvals": [m * 100, m * 10, m + 1],
            "explanation": ("Every $100$ centimetres is one metre, and "
                            "$%d$ holds $%d$ of them: $%d \\times 100 = %d$."
                            % (m * 100, m, m, m * 100)),
            "check": ["Eq(%d*100, %d)" % (m, m * 100),
                      "Eq(Rational(%d, 100), %d)" % (m * 100, m)],
        }
    for m in range(1, 10):
        for cm in (m * 100 - 30, m * 100 + 40):
            if cm <= 0 or cm > 1000:
                continue
            longer_m = cm < m * 100
            yield {
                "statement": ("Which is longer, $%d$ m or $%d$ cm? Give the "
                              "longer length in centimetres." % (m, cm)),
                "correct": m * 100 if longer_m else cm,
                "dvals": [cm if longer_m else m * 100, m, abs(m * 100 - cm)],
                "explanation": ("Put both in one unit: $%d$ m is $%d$ cm. "
                                "Then $%d > %d$, so the longer is $%d$ cm — a "
                                "gap of $%d$ cm."
                                % (m, m * 100,
                                   max(m * 100, cm), min(m * 100, cm),
                                   max(m * 100, cm), abs(m * 100 - cm))),
                "check": ["Eq(%d*100, %d)" % (m, m * 100),
                          "%d > %d" % (max(m * 100, cm), min(m * 100, cm))],
            }


def _g_mass_capacity():
    for a in range(3, 20):
        for b in range(1, 15):
            if b >= a:
                continue
            yield {
                "statement": ("One sack weighs $%d$ kg and another weighs $%d$ "
                              "kg. How much heavier is the first?" % (a, b)),
                "correct": a - b,
                "dvals": [a + b, a, b],
                "explanation": ("The heavier pan sinks, and the gap is "
                                "$%d - %d = %d$ kg. Adding $%d$ kg to the light "
                                "side would level the balance."
                                % (a, b, a - b, a - b)),
                "check": ["Eq(%d - %d, %d)" % (a, b, a - b),
                          "Eq(%d + %d, %d)" % (b, a - b, a),
                          "%d > %d" % (a, b)],
            }


def _g_clock():
    for h in range(1, 13):
        for half in (0, 1):
            for _rep in range(2):
                if half:
                    nxt = h % 12 + 1
                    yield {
                        "statement": ("The long hand points straight down and "
                                      "the short hand sits between the $%d$ and "
                                      "the $%d$. What time is it?" % (h, nxt)),
                        "correct": "half past %s" % ONES[h],
                        "dvals": ["half past %s" % ONES[nxt],
                                  "%s o'clock" % ONES[h],
                                  "%s o'clock" % ONES[nxt]],
                        "explanation": ("The long hand straight down means $30$ "
                                        "of the hour's $60$ minutes have gone. "
                                        "The hour is the one the short hand has "
                                        "PASSED, so it is half past %s."
                                        % ONES[h]),
                        "check": ["Eq(2*30, 60)", "Eq(60 - 30, 30)"],
                    }
                else:
                    yield {
                        "statement": ("The long hand points straight up and the "
                                      "short hand points at the $%d$. What time "
                                      "is it?" % h),
                        # The fourth option used to be a hard-coded "twelve
                        # o'clock", which IS the answer when h is 12 — every
                        # twelve-o'clock draw collided and was dropped. Both
                        # neighbours of the hour are safe at any h.
                        "correct": "%s o'clock" % ONES[h],
                        "dvals": ["half past %s" % ONES[h],
                                  "%s o'clock" % ONES[h % 12 + 1],
                                  "%s o'clock" % ONES[12 if h == 1 else h - 1]],
                        "explanation": ("The long hand straight up is zero "
                                        "minutes past, so the hour has just "
                                        "begun — and the short hand names it: "
                                        "%s o'clock." % ONES[h]),
                        "check": ["Eq(60 - 60, 0)", "Eq(2*30, 60)"],
                    }


def _g_money_total():
    for hundreds in range(1, 8):
        for fifties in range(0, 3):
            for twenties in range(0, 4):
                total = 100 * hundreds + 50 * fifties + 20 * twenties
                if total > 1000 or (fifties == 0 and twenties == 0):
                    continue
                notes = hundreds + fifties + twenties
                parts = ["$%d$ notes of $100$" % hundreds]
                if fifties:
                    parts.append("$%d$ of $50$" % fifties)
                if twenties:
                    parts.append("$%d$ of $20$" % twenties)
                yield {
                    "statement": ("A purse holds %s. How many tögrög is that?"
                                  % ", ".join(parts)),
                    "correct": total,
                    "dvals": [notes, total + 100, total - 20],
                    "explanation": ("Count by value, biggest first: "
                                    "$%d \\times 100 = %d$, and the rest adds "
                                    "up to $%d$, giving $%d$ tögrög. The purse "
                                    "holds $%d$ notes, but that is not the "
                                    "amount."
                                    % (hundreds, hundreds * 100,
                                       total - hundreds * 100, total, notes)),
                    "check": ["Eq(%d*100 + %d*50 + %d*20, %d)"
                              % (hundreds, fifties, twenties, total),
                              "Eq(%d*100, %d)" % (hundreds, hundreds * 100)],
                }


def _g_change():
    for paid in (200, 300, 400, 500, 1000):
        for price in range(60, 900, 37):
            if price >= paid:
                continue
            change = paid - price
            if change < 20:
                continue          # change - 10 must stay a sensible amount
            yield {
                "statement": ("An item costs $%d$ tögrög and you pay with $%d$. "
                              "What is the change?" % (price, paid)),
                "correct": change,
                # `paid + price` models "added instead of subtracting", but
                # with a 1000-tögrög note it lands above the year's number
                # range — and so does change + 100. A change that is ten
                # tögrög out shows the same slip and stays inside the year.
                "dvals": [price, change + 10, change - 10],
                "explanation": ("Change is payment minus price: "
                                "$%d - %d = %d$ tögrög. Receipt: "
                                "$%d + %d = %d$, which returns exactly what was "
                                "handed over."
                                % (paid, price, change, change, price, paid)),
                "check": ["Eq(%d - %d, %d)" % (paid, price, change),
                          "Eq(%d + %d, %d)" % (change, price, paid)],
            }


# ===========================================================================
# Unit 8 — Tallies & Picture Graphs
# ===========================================================================

def _g_read_tally():
    for n in range(3, 40):
        bundles, singles = divmod(n, 5)
        yield {
            "statement": ("A tally shows $%d$ closed %s of five and $%d$ single "
                          "%s. What is the count?"
                          % (bundles, "bundle" if bundles == 1 else "bundles",
                             singles, "mark" if singles == 1 else "marks")),
            "correct": n,
            "dvals": [bundles + singles, n + 5, n - 1],
            "explanation": ("Each bundle is worth five: "
                            "$%d \\times 5 = %d$, and $%d$ more makes $%d$."
                            % (bundles, bundles * 5, singles, n)),
            "check": ["Eq(%d*5 + %d, %d)" % (bundles, singles, n),
                      "%d < 5" % singles],
        }


def _g_draw_tally():
    for n in range(6, 45):
        bundles, singles = divmod(n, 5)
        yield {
            "statement": ("Drawn as tally marks, how many SINGLE marks does "
                          "$%d$ leave over?" % n),
            "correct": singles,
            "dvals": [bundles, n - bundles, singles + 5],
            "explanation": ("$%d$ whole bundles use $%d \\times 5 = %d$ marks, "
                            "leaving $%d - %d = %d$ singles — and it is always "
                            "fewer than five, because a fifth would close "
                            "another bundle."
                            % (bundles, bundles, bundles * 5, n, bundles * 5,
                               singles)),
            "check": ["Eq(%d - %d, %d)" % (n, bundles * 5, singles),
                      "%d < 5" % singles],
        }


def _g_table_total():
    for a in range(3, 20):
        for b in range(4, 18, 3):
            for c in (2, 6, 9):
                total = a + b + c
                yield {
                    "statement": ("A table reads sheep $%d$, goats $%d$, horses "
                                  "$%d$. What is the total?" % (a, b, c)),
                    "correct": total,
                    "dvals": [a + b, total - c + 1, total + c],
                    "explanation": ("Add the rows: $%d + %d = %d$, then "
                                    "$%d + %d = %d$ animals."
                                    % (a, b, a + b, a + b, c, total)),
                    "check": ["Eq(%d + %d + %d, %d)" % (a, b, c, total)],
                }


def _g_missing_row():
    for a in range(4, 25):
        for b in range(3, 20, 4):
            for miss in (2, 5, 8):
                total = a + b + miss
                yield {
                    "statement": ("A table has rows of $%d$ and $%d$ and a "
                                  "smudged third row. The total is $%d$. What "
                                  "was the third row?" % (a, b, total)),
                    "correct": miss,
                    "dvals": [a + b, total, total + a],
                    "explanation": ("The readable rows come to $%d + %d = %d$, "
                                    "so the missing one is $%d - %d = %d$. "
                                    "Check: $%d + %d = %d$."
                                    % (a, b, a + b, total, a + b, miss,
                                       a + b, miss, total)),
                    "check": ["Eq(%d + %d, %d)" % (a, b, a + b),
                              "Eq(%d - %d, %d)" % (total, a + b, miss),
                              "Eq(%d + %d, %d)" % (a + b, miss, total)],
                }


def _g_pictograph_compare():
    for a in range(3, 18):
        for b in range(2, 15, 2):
            if b >= a:
                continue
            yield {
                "statement": ("On a picture graph one picture stands for one "
                              "child. One row has $%d$ pictures and another has "
                              "$%d$. How many more children are in the longer "
                              "row?" % (a, b)),
                "correct": a - b,
                "dvals": [a + b, a, b],
                "explanation": ("One picture is one child, so the gap between "
                                "the rows is the answer: $%d - %d = %d$ more. "
                                "Adding the rows gives $%d$, which is how many "
                                "there are altogether."
                                % (a, b, a - b, a + b)),
                "check": ["Eq(%d - %d, %d)" % (a, b, a - b),
                          "Eq(%d + %d, %d)" % (b, a - b, a)],
            }


def _g_data_question():
    for a in range(4, 16):
        for b in range(2, 12, 3):
            for c in (3, 7):
                total = a + b + c
                yield {
                    "statement": ("A block graph shows wrestling $%d$, archery "
                                  "$%d$, racing $%d$, one block per child. How "
                                  "many children were asked altogether?"
                                  % (a, b, c)),
                    "correct": total,
                    "dvals": [max(a, b, c), max(a, b, c) - min(a, b, c), a + b],
                    "explanation": ("Each child appears in exactly one bar, so "
                                    "\"altogether\" adds every bar: "
                                    "$%d + %d + %d = %d$ children. The gap "
                                    "between the tallest and shortest bar is a "
                                    "different question."
                                    % (a, b, c, total)),
                    "check": ["Eq(%d + %d + %d, %d)" % (a, b, c, total),
                              "%d > %d" % (total, max(a, b, c))],
                }


# ===========================================================================
# build
# ===========================================================================

def build():
    forms = []

    U1 = "numbers-to-1000"
    forms += [
        form("g3-place-value", "What a digit is worth", 1, U1,
             "A digit's value is the digit times its place — read the column, not the digit.",
             mk_num("g3-pv", _g_place_value())),
        form("g3-words", "Words into digits", 1, U1,
             "Hundreds, then tens and ones — a column the words skip takes a zero.",
             mk_num("g3-wd", _g_words_to_digits())),
        form("g3-compare", "Comparing three-digit numbers", 2, U1,
             "Compare from the left; the first column that differs decides it.",
             mk_txt("g3-cmp", _g_compare())),
        form("g3-order", "Putting numbers in order", 2, U1,
             "Sort by hundreds, and break any tie with the tens.",
             mk_num("g3-ord", _g_order())),
        form("g3-steps", "Counting in steps", 2, U1,
             "Find the gap between neighbours, then keep stepping by it.",
             mk_num("g3-stp", _g_step_count())),
        form("g3-round", "Rounding to the nearest ten", 3, U1,
             "Name the two neighbouring tens, then choose the nearer — a half goes up.",
             mk_num("g3-rnd", _g_round_ten())),
    ]

    U2 = "addition-and-subtraction-to-1000"
    forms += [
        form("g3-mental-hundreds", "Adding whole hundreds", 1, U2,
             "A whole hundred moves one digit; everything else is copied down.",
             mk_num("g3-mh", _g_mental_hundreds())),
        form("g3-column-add", "Column addition with a carry", 1, U2,
             "When the ones pass nine, ten of them move next door as a carry.",
             mk_num("g3-ca", _g_column_add())),
        form("g3-column-sub", "Column subtraction with a break", 2, U2,
             "Short column? Break a ten, and remember to reduce the one you took it from.",
             mk_num("g3-cs", _g_column_sub())),
        form("g3-fact-family", "Fact families", 2, U2,
             "The whole always leads a subtraction — it can never be taken from a part.",
             mk_txt("g3-ff", _g_fact_family())),
        form("g3-missing", "Missing numbers", 2, U2,
             "Missing part, subtract; missing whole, add.",
             mk_num("g3-mn", _g_missing_number())),
        form("g3-two-step", "Two-step word problems", 3, U2,
             "Do the steps in the order the story tells them; the middle number is not the answer.",
             mk_num("g3-ts", _g_word_two_step())),
    ]

    U3 = "multiplication-first-facts"
    forms += [
        form("g3-equal-groups", "Equal groups", 1, U3,
             "The first number counts the groups, the second counts inside one.",
             mk_num("g3-eg", _g_equal_groups())),
        form("g3-turnaround", "Arrays and the turnaround", 2, U3,
             "One rectangle, two readings — the total cannot change when you tilt your head.",
             mk_txt("g3-ta", _g_turnaround())),
        form("g3-friendly", "Tables of 2, 5 and 10", 1, U3,
             "Double, count the fives, or bundle the tens — and check the ending.",
             mk_num("g3-fr", _g_friendly_tables())),
        form("g3-threes-fours", "Tables of 3 and 4", 2, U3,
             "Threes are a step count; fours are twos doubled.",
             mk_num("g3-tf", _g_threes_fours())),
        form("g3-one-zero", "Times one and times zero", 1, U3,
             "One leaves a number alone; zero empties it, whichever side the zero is on.",
             mk_num("g3-oz", _g_one_and_zero())),
        form("g3-times-story", "Multiplication stories", 3, U3,
             "A story multiplies only when its groups are equal.",
             mk_num("g3-st", _g_times_story())),
    ]

    U4 = "division-sharing-and-grouping"
    forms += [
        form("g3-sharing", "Sharing equally", 1, U4,
             "Sharing asks how many EACH — the answer is the size of one share.",
             mk_num("g3-sh", _g_sharing())),
        form("g3-grouping", "Grouping into bundles", 1, U4,
             "Grouping asks how many BUNDLES — the bundle size was given to you.",
             mk_num("g3-gr", _g_grouping())),
        form("g3-div-facts", "Division facts from the tables", 2, U4,
             "Every division fact is a times fact read backwards.",
             mk_num("g3-df", _g_division_facts())),
        form("g3-div-34", "Dividing by 3 and 4", 2, U4,
             "Count threes, or halve twice — because four is two twos.",
             mk_num("g3-d34", _g_divide_three_four())),
        form("g3-receipt", "Checking with the receipt", 3, U4,
             "Multiply the answer back; if the pile does not return, the answer is wrong.",
             mk_txt("g3-rc", _g_receipt_check())),
        form("g3-choose-op", "Choosing the operation", 3, U4,
             "Missing total, multiply; missing group, divide.",
             mk_txt("g3-co", _g_choose_operation())),
    ]

    U5 = "fractions-halves-and-quarters"
    forms += [
        form("g3-name-fraction", "Naming the shaded part", 1, U5,
             "Bottom number from the cutting, top number from the counting.",
             mk_txt("g3-nf", _g_name_fraction())),
        form("g3-make-whole", "Making a whole", 1, U5,
             "The bottom number is how many parts it takes to rebuild the whole.",
             mk_num("g3-mw", _g_make_a_whole())),
        form("g3-compare-frac", "Comparing unit fractions", 2, U5,
             "Of one whole, a bigger bottom number always means a smaller piece.",
             mk_txt("g3-cf", _g_compare_unit_fractions())),
        form("g3-leftover", "The part that is left", 2, U5,
             "Shaded and plain always rebuild the whole — just count what you did not take.",
             mk_txt("g3-lo", _g_leftover())),
        form("g3-frac-set", "A unit fraction of a set", 2, U5,
             "Divide by the bottom number to make the equal groups.",
             mk_num("g3-fs", _g_unit_fraction_of_set())),
        form("g3-frac-set-2", "More than one part of a set", 3, U5,
             "Share by the bottom number, then take as many groups as the top says.",
             mk_num("g3-fs2", _g_non_unit_of_set())),
    ]

    U6 = "shapes-sides-and-corners"
    forms += [
        form("g3-name-shape", "Naming flat shapes", 1, U6,
             "Count the straight sides — that is what gives a flat shape its name.",
             mk_txt("g3-ns", _g_shape_by_sides())),
        form("g3-count-sides", "Counting sides", 1, U6,
             "Sides and corners always match, so counting one counts the other.",
             mk_num("g3-cs2", _g_sides_and_corners())),
        form("g3-square-corners", "Square corners", 2, U6,
             "A rectangle has four; a triangle can have at most one.",
             mk_num("g3-sc", _g_square_corners())),
        form("g3-solids", "Solid shapes", 2, U6,
             "Flat faces let a solid stack; curved surfaces let it roll.",
             mk_num("g3-so", _g_solid_faces())),
        form("g3-pattern", "Shape patterns", 2, U6,
             "Find the repeating piece and its length, then count ahead.",
             mk_num("g3-pt", _g_shape_pattern())),
        form("g3-sorting", "Sorting by a rule", 3, U6,
             "Different rules put the same shapes into different piles.",
             mk_txt("g3-sr", _g_sorting_rule())),
    ]

    U7 = "measuring-time-and-money"
    forms += [
        form("g3-ruler", "Reading a ruler", 1, U7,
             "Subtract the starting mark — the far mark alone is the length only from zero.",
             mk_num("g3-ru", _g_ruler())),
        form("g3-metres", "Metres and centimetres", 1, U7,
             "A metre is one hundred centimetres.",
             mk_num("g3-me", _g_metres())),
        form("g3-mass", "Comparing mass", 2, U7,
             "The heavier pan sinks; the gap is what would level it.",
             mk_num("g3-ms", _g_mass_capacity())),
        form("g3-clock", "Telling the time", 2, U7,
             "Long hand for minutes, short hand for the hour it has PASSED.",
             mk_txt("g3-cl", _g_clock())),
        form("g3-money", "Counting tögrög", 2, U7,
             "Count by value, biggest note first — the number of notes is not the amount.",
             mk_num("g3-mo", _g_money_total())),
        form("g3-change", "Working out change", 3, U7,
             "Payment minus price, then check by adding the change back.",
             mk_num("g3-ch", _g_change())),
    ]

    U8 = "tallies-and-picture-graphs"
    forms += [
        form("g3-read-tally", "Reading a tally", 1, U8,
             "Each closed bundle is worth five, then add the singles.",
             mk_num("g3-rt", _g_read_tally())),
        form("g3-draw-tally", "Drawing a tally", 1, U8,
             "Fill whole bundles first; the leftovers are always fewer than five.",
             mk_num("g3-dt", _g_draw_tally())),
        form("g3-table-total", "Table totals", 2, U8,
             "Add every row — the total is the table's receipt.",
             mk_num("g3-tt", _g_table_total())),
        form("g3-missing-row", "A missing row", 2, U8,
             "Total minus the rows you can read gives the one you cannot.",
             mk_num("g3-mr", _g_missing_row())),
        form("g3-pictograph", "Comparing picture-graph rows", 2, U8,
             "One picture is one thing, so the gap between rows is the answer.",
             mk_num("g3-pg", _g_pictograph_compare())),
        form("g3-data-question", "Questions from a graph", 3, U8,
             "\"Altogether\" adds every bar; \"how many more\" subtracts two.",
             mk_num("g3-dq", _g_data_question())),
    ]

    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


CEILING = 1000

_NUMBER = re.compile(r"(?<![\d.\\])(\d+)(?![\d.])")
_NEGATIVE = re.compile(r"(?<![\w])-\d")


def _audit(topic):
    """Enforce the Grade 2 house rules on the generated bank.

    verify-problembank.py proves every sympy check is TRUE and every string
    renders, but it is shared by twenty-five subjects and cannot know that
    this one stops at 1000 and never shows a negative. Those two rules were
    comments at the top of this file until three distractors broke them —
    `whole + known` reaching 1470, `paid + price` reaching 1060, and
    `mid - gain` going negative — so they are checked here instead."""
    problems = []
    for f in topic["forms"]:
        for v in f["variants"]:
            for field in ("statement", "explanation"):
                _scan(problems, f["id"], v["id"], v[field])
            for opt in v["options"]:
                _scan(problems, f["id"], v["id"], opt)
    return problems


def _scan(out, form_id, var_id, text):
    for m in _NUMBER.finditer(text):
        if int(m.group(1)) > CEILING:
            out.append("%s/%s: %s exceeds the Grade 2 ceiling of %d — %r"
                       % (form_id, var_id, m.group(1), CEILING, text[:70]))
    if _NEGATIVE.search(text):
        out.append("%s/%s: negative value, which Grade 2 has not met — %r"
                   % (form_id, var_id, text[:70]))


if __name__ == "__main__":
    topic = build()
    n_forms = len(topic["forms"])
    n_vars = sum(len(f["variants"]) for f in topic["forms"])
    per_unit = {u["id"]: 0 for u in topic["units"]}
    for f in topic["forms"]:
        assert f["unit"] in per_unit, "%s: unknown unit %r" % (f["id"], f["unit"])
        per_unit[f["unit"]] += len(f["variants"])
    print("grade3 — %d forms, %d variants" % (n_forms, n_vars))
    for u in topic["units"]:
        print("  %-38s %4d" % (u["id"], per_unit[u["id"]]))
    failures = _audit(topic)
    if failures:
        print("\n%d HOUSE-RULE FAILURES:" % len(failures))
        for f in failures[:30]:
            print("  x %s" % f)
        sys.exit(1)
    print("  ok  nothing above %d, no negatives" % CEILING)
