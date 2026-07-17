# -*- coding: utf-8 -*-
"""Problem-bank subject: Probability & Statistics — mirrors the /math/prob-stats course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/prob_stats.py` to
self-check.
"""
import re
from fractions import Fraction
from math import comb, factorial, perm

from sympy import Rational

SLUG = "prob-stats"
TITLE = "Probability & Statistics"
TITLE_MN = "Магадлал ба статистик"
BLURB = ("Unit-by-unit practice for the Probability & Statistics course — counting to inference, every unit with its own exercise set.")

UNITS = [
    {"id": "counting-principles", "title": "Counting Principles",
     "blurb": "The multiplication and addition principles, complementary counting, and organized lists — how to count without counting."},
    {"id": "permutations", "title": "Permutations & Arrangements",
     "blurb": "Factorials, arrangements of all or some objects, repeated letters, and seating with restrictions."},
    {"id": "combinations", "title": "Combinations",
     "blurb": "Choosing without order: nCr, committees, at-least and at-most counts, and when order matters vs when it doesn't."},
    {"id": "binomial-theorem", "title": "Pascal's Triangle & the Binomial Theorem",
     "blurb": "The triangle that counts everything: binomial coefficients, expanding powers, and finding specific terms."},
    {"id": "probability-models", "title": "Probability Models",
     "blurb": "Sample spaces, events, equally-likely outcomes, complements, and the addition rule with Venn diagrams."},
    {"id": "conditional-probability", "title": "Conditional Probability & Independence",
     "blurb": "How information changes chance: P(A|B), the multiplication rule, independence, weighted trees, and Bayes by table."},
    {"id": "random-variables", "title": "Random Variables & Expected Value",
     "blurb": "Turning outcomes into numbers: probability distributions, expected value, variance, and what makes a game fair."},
    {"id": "binomial-distribution", "title": "The Binomial Distribution",
     "blurb": "Repeated independent trials: binomial probabilities, expected count np, shape, and simulation."},
    {"id": "describing-data", "title": "Describing Data",
     "blurb": "Center and spread done right: mean, median, IQR, standard deviation, boxplots, and the 1.5×IQR outlier fence."},
    {"id": "distributions-and-position", "title": "Distribution Shape & Position",
     "blurb": "Histograms and shape, percentiles, z-scores, and the normal curve with the 68–95–99.7 rule."},
    {"id": "two-variable-data", "title": "Two-Variable Data",
     "blurb": "Scatterplots, the correlation coefficient, the least-squares line, and why correlation is not causation."},
    {"id": "inference-and-studies", "title": "Sampling, Studies & Inference",
     "blurb": "Random sampling, bias, experiments vs observation, simulation-based inference, and margin of error — the capstone."},
]

# No legacy forms: this subject is authored fresh.
REMAP = {}
SOURCES = []

# form id -> fn(statement) -> ("num", sympy value) | ("opt", exact option str)
RESOLVERS = {}


# =========================================================================
# Authoring helpers
# =========================================================================
def _place(correct, distractors, i):
    """Return (options, correctIndex) with the correct answer at slot i % 4."""
    pos = i % 4
    opts = [None] * 4
    opts[pos] = correct
    rest = list(distractors)
    j = 0
    for p in range(4):
        if p == pos:
            continue
        opts[p] = rest[j]
        j += 1
    return opts, pos


def _mk(vid, statement, correct, distractors, i, explanation, check):
    """Assemble a variant; crash if any two options collide."""
    opts = [correct] + list(distractors)
    assert len(set(opts)) == 4, "%s: option collision %r" % (vid, opts)
    options, ci = _place(correct, distractors, i)
    return {"id": vid, "statement": statement, "options": options,
            "correctIndex": ci, "explanation": explanation, "check": check}


def _distinct(vals):
    """True when all (exact) values are pairwise distinct."""
    return len(set(vals)) == len(vals)


def _floor(name, variants, lo=10):
    """Target is ~12 variants per form; the hard floor is 10 (check_subject)."""
    assert len(variants) >= lo, "%s: only %d variants" % (name, len(variants))
    return variants


def _fr_core(fr):
    """Exact rational -> KaTeX body (integer, or \\frac with leading minus)."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return "%d" % fr.numerator
    if fr < 0:
        return "-\\frac{%d}{%d}" % (-fr.numerator, fr.denominator)
    return "\\frac{%d}{%d}" % (fr.numerator, fr.denominator)


def _fr(fr):
    return "$%s$" % _fr_core(fr)


def _rat(fr):
    fr = Fraction(fr)
    return Rational(fr.numerator, fr.denominator)


def _fracs_in(s):
    """All \\frac{p}{q} in a statement, as Fractions (in order)."""
    return [Fraction(int(p), int(q))
            for p, q in re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", s)]


# -------------------------------------------------------------------------
# Form 1: multiplication-principle (counting-principles, level 1)
# -------------------------------------------------------------------------
_MULT = [(3, 4, 2), (2, 5, 3), (4, 3, 5), (3, 5, 4), (2, 6, 3), (5, 4, 3),
         (3, 6, 2), (4, 5, 2), (2, 4, 5), (6, 3, 4), (5, 3, 4), (4, 6, 2)]


def _gen_mult():
    variants = []
    for i, (a, b, c) in enumerate(_MULT):
        ans = a * b * c
        dvals = [a + b + c, a * b + c, a * (b + c)]
        assert _distinct([ans] + dvals)
        stmt = ("A menu offers $%d$ soups, $%d$ main dishes, and $%d$ "
                "desserts. How many different three-course meals — one soup, "
                "one main, one dessert — are possible?" % (a, b, c))
        variants.append(_mk(
            "PS-mult-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "Each soup pairs with every main and every dessert, so multiply: "
            "$%d \\cdot %d \\cdot %d = %d$. Adding $%d + %d + %d = %d$ counts "
            "single dishes, not full meals." % (a, b, c, ans, a, b, c, a + b + c),
            ["%d*%d*%d == %d" % (a, b, c, ans)]))
    return _floor("multiplication-principle", variants)


def _rs_mult(s):
    m = re.search(r"\$(\d+)\$ soups, \$(\d+)\$ main dishes, and \$(\d+)\$ desserts", s)
    return ("num", int(m.group(1)) * int(m.group(2)) * int(m.group(3)))


# -------------------------------------------------------------------------
# Form 2: addition-or-multiplication (counting-principles, level 2)
# -------------------------------------------------------------------------
_AND_PAIRS = [(4, 10), (5, 6), (3, 9), (6, 8), (7, 5), (8, 4)]
_OR_PAIRS = [(7, 5), (9, 4), (6, 8), (12, 5), (8, 7), (10, 6)]


def _gen_aor():
    variants = []
    i = 0
    for (a, b) in _AND_PAIRS:
        ans = a * b
        dvals = [a + b, a * b - 1, a + b + 1]
        assert _distinct([ans] + dvals)
        stmt = ("A locker code consists of one letter chosen from $%d$ "
                "letters followed by one digit chosen from $%d$ digits. "
                "How many different codes are possible?" % (a, b))
        variants.append(_mk(
            "PS-aor-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "The code needs a letter AND a digit, so the choices multiply: "
            "$%d \\cdot %d = %d$. Adding $%d + %d = %d$ is the classic slip — "
            "that counts picking just one symbol." % (a, b, ans, a, b, a + b),
            ["%d*%d == %d" % (a, b, ans)]))
        i += 1
    for (a, b) in _OR_PAIRS:
        ans = a + b
        dvals = [a * b, a + b - 1, a + b + 1]
        assert _distinct([ans] + dvals)
        stmt = ("As a prize, a student may take one book from $%d$ novels or "
                "one book from $%d$ comics — one book in total. How many "
                "different choices are possible?" % (a, b))
        variants.append(_mk(
            "PS-aor-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "One book from either shelf means OR, so the counts add: "
            "$%d + %d = %d$. Multiplying to get $%d$ is the classic slip — "
            "that would count taking one of each." % (a, b, ans, a * b),
            ["%d + %d == %d" % (a, b, ans)]))
        i += 1
    return _floor("addition-or-multiplication", variants)


def _rs_aor(s):
    a, b = [int(x) for x in re.findall(r"from \$(\d+)\$", s)]
    return ("num", a * b if "followed by" in s else a + b)


# -------------------------------------------------------------------------
# Form 3: npr-value (permutations, level 1)
# -------------------------------------------------------------------------
_NPR = [(5, 2), (5, 3), (6, 2), (6, 4), (7, 2), (7, 3), (8, 2), (8, 3),
        (9, 2), (9, 3), (10, 2), (10, 3)]


def _gen_npr():
    variants = []
    for i, (n, r) in enumerate(_NPR):
        ans = perm(n, r)
        dvals = [comb(n, r), n ** r, factorial(n) // factorial(r)]
        assert _distinct([ans] + dvals), (n, r)
        stmt = ("Compute $P(%d, %d)$ — the number of ways to arrange $%d$ of "
                "$%d$ distinct objects in a row." % (n, r, r, n))
        variants.append(_mk(
            "PS-npr-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "$P(%d, %d) = \\frac{%d!}{(%d - %d)!} = %d$. Dividing by $%d!$ as "
            "well gives $\\binom{%d}{%d} = %d$ — that counts unordered "
            "choices, not arrangements." % (n, r, n, n, r, ans, r, n, r, comb(n, r)),
            ["factorial(%d)/factorial(%d) == %d" % (n, n - r, ans),
             "binomial(%d, %d)*factorial(%d) == %d" % (n, r, r, ans)]))
    return _floor("npr-value", variants)


def _rs_npr(s):
    m = re.search(r"\$P\((\d+), (\d+)\)\$", s)
    n, r = int(m.group(1)), int(m.group(2))
    return ("num", perm(n, r))


# -------------------------------------------------------------------------
# Form 4: arrangements (permutations, level 2)
# -------------------------------------------------------------------------
def _gen_arrangements():
    variants = []
    i = 0
    for n in range(3, 9):
        ans = factorial(n)
        d3 = n * n if n * n != 2 ** n else n * (n - 1)
        dvals = [factorial(n - 1), 2 ** n, d3]
        assert _distinct([ans] + dvals), n
        stmt = ("In how many different ways can $%d$ people stand in a row "
                "for a photo?" % n)
        variants.append(_mk(
            "PS-arr-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "All $%d$ people are ordered, so the count is $%d! = %d$. "
            "Using $(%d - 1)! = %d$ is the circular-table formula — a row "
            "has no rotation to cancel." % (n, n, ans, n, factorial(n - 1)),
            ["factorial(%d) == %d" % (n, ans)]))
        i += 1
    for n in range(3, 9):
        ans = factorial(n - 1)
        dvals = [factorial(n), factorial(n - 2), n]
        assert _distinct([ans] + dvals), n
        stmt = ("In how many different ways can $%d$ people stand in a row "
                "for a photo if one particular person must stand first?" % n)
        variants.append(_mk(
            "PS-arr-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "The first spot is forced, so only the other $%d$ people are "
            "arranged: $(%d - 1)! = %d$. Answering $%d! = %d$ ignores the "
            "restriction." % (n - 1, n, ans, n, factorial(n)),
            ["factorial(%d) == %d" % (n - 1, ans)]))
        i += 1
    return _floor("arrangements", variants)


def _rs_arrangements(s):
    n = int(re.search(r"\$(\d+)\$ people", s).group(1))
    return ("num", factorial(n - 1) if "must stand first" in s else factorial(n))


# -------------------------------------------------------------------------
# Form 5: ncr-value (combinations, level 1)
# -------------------------------------------------------------------------
_NCR = [(5, 2), (6, 2), (6, 3), (7, 2), (7, 3), (8, 2), (8, 3), (9, 2),
        (9, 4), (10, 2), (11, 3), (12, 2)]


def _gen_ncr():
    variants = []
    for i, (n, r) in enumerate(_NCR):
        ans = comb(n, r)
        dvals = [perm(n, r), comb(n, r - 1), comb(n + 1, r)]
        assert _distinct([ans] + dvals), (n, r)
        stmt = ("Compute $\\binom{%d}{%d}$ — the number of ways to choose "
                "$%d$ objects from $%d$ when order does not matter." % (n, r, r, n))
        variants.append(_mk(
            "PS-ncr-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "$\\binom{%d}{%d} = \\frac{%d!}{%d!\\,%d!} = %d$. Forgetting to "
            "divide by $%d!$ gives $P(%d, %d) = %d$ — that counts ordered "
            "picks twice-plus over." % (n, r, n, r, n - r, ans, r, n, r, perm(n, r)),
            ["binomial(%d, %d) == %d" % (n, r, ans)]))
    return _floor("ncr-value", variants)


def _rs_ncr(s):
    m = re.search(r"\\binom\{(\d+)\}\{(\d+)\}", s)
    return ("num", comb(int(m.group(1)), int(m.group(2))))


# -------------------------------------------------------------------------
# Form 6: committee (combinations, level 2)
# -------------------------------------------------------------------------
_COMM = [(5, 6, 2, 3), (6, 5, 3, 2), (4, 5, 2, 2), (6, 7, 2, 3), (7, 6, 3, 2),
         (5, 5, 2, 3), (7, 5, 2, 2), (6, 6, 2, 3), (5, 7, 2, 3), (4, 6, 2, 3),
         (6, 4, 3, 2), (7, 7, 3, 2)]


def _gen_committee():
    variants = []
    for i, (m_, g, b, c) in enumerate(_COMM):
        ans = comb(m_, b) * comb(g, c)
        dvals = [comb(m_ + g, b + c), comb(m_, b) + comb(g, c),
                 perm(m_, b) * perm(g, c)]
        assert _distinct([ans] + dvals), (m_, g, b, c)
        stmt = ("A class has $%d$ boys and $%d$ girls. In how many ways can "
                "a committee of exactly $%d$ boys and $%d$ girls be chosen?"
                % (m_, g, b, c))
        variants.append(_mk(
            "PS-comm-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "Choose the boys and the girls separately, then multiply: "
            "$\\binom{%d}{%d}\\binom{%d}{%d} = %d \\cdot %d = %d$. Using "
            "$\\binom{%d}{%d} = %d$ ignores the exactly-$%d$-boys condition."
            % (m_, b, g, c, comb(m_, b), comb(g, c), ans,
               m_ + g, b + c, comb(m_ + g, b + c), b),
            ["binomial(%d, %d)*binomial(%d, %d) == %d" % (m_, b, g, c, ans)]))
    return _floor("committee", variants)


def _rs_committee(s):
    m = re.search(r"has \$(\d+)\$ boys and \$(\d+)\$ girls", s)
    m2 = re.search(r"exactly \$(\d+)\$ boys and \$(\d+)\$ girls", s)
    return ("num", comb(int(m.group(1)), int(m2.group(1)))
            * comb(int(m.group(2)), int(m2.group(2))))


# -------------------------------------------------------------------------
# Form 7: binomial-coefficient (binomial-theorem, level 2)
# -------------------------------------------------------------------------
_BCO = [(4, 2, 1), (4, 2, 2), (4, 3, 1), (4, 3, 2), (5, 2, 1), (5, 3, 2),
        (5, 2, 3), (6, 2, 2), (6, 3, 1), (6, 2, 3), (6, 3, 2), (7, 2, 2),
        (7, 2, 3), (7, 3, 1)]


def _gen_bco():
    variants = []
    i = 0
    for (n, a, k) in _BCO:
        if len(variants) >= 12:
            break
        ans = comb(n, k) * a ** k
        dvals = [comb(n, k), a ** k, comb(n, k - 1) * a ** (k - 1)]
        if not _distinct([ans] + dvals):
            continue
        stmt = ("In the expansion of $(x + %d)^{%d}$, what is the "
                "coefficient of $x^{%d}$?" % (a, n, n - k))
        variants.append(_mk(
            "PS-bco-v%02d" % (len(variants) + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "The $x^{%d}$ term is $\\binom{%d}{%d} x^{%d} \\cdot %d^{%d}$, so "
            "the coefficient is $%d \\cdot %d = %d$. Writing only "
            "$\\binom{%d}{%d} = %d$ forgets the factor $%d^{%d}$."
            % (n - k, n, k, n - k, a, k, comb(n, k), a ** k, ans,
               n, k, comb(n, k), a, k),
            ["binomial(%d, %d)*%d**%d == %d" % (n, k, a, k, ans)]))
        i += 1
    return _floor("binomial-coefficient", variants)


def _rs_bco(s):
    m = re.search(r"\$\(x \+ (\d+)\)\^\{(\d+)\}\$", s)
    a, n = int(m.group(1)), int(m.group(2))
    e = int(re.search(r"coefficient of \$x\^\{(\d+)\}\$", s).group(1))
    k = n - e
    return ("num", comb(n, k) * a ** k)


# -------------------------------------------------------------------------
# Form 8: pascal-row (binomial-theorem, level 1)
# -------------------------------------------------------------------------
_PAS_ENTRY = [(5, 2), (6, 2), (6, 3), (7, 2), (7, 3), (8, 3)]


def _gen_pascal():
    variants = []
    i = 0
    for (n, k) in _PAS_ENTRY:
        ans = comb(n, k)
        dvals = [comb(n, k - 1), comb(n - 1, k), comb(n + 1, k)]
        assert _distinct([ans] + dvals), (n, k)
        stmt = ("What is the entry in position $%d$ (counting from $0$) of "
                "row $%d$ of Pascal's triangle?" % (k, n))
        variants.append(_mk(
            "PS-pas-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "Row $%d$, position $%d$ is $\\binom{%d}{%d} = %d$. Counting "
            "positions from $1$ instead of $0$ lands on $\\binom{%d}{%d} = %d$."
            % (n, k, n, k, ans, n, k - 1, comb(n, k - 1)),
            ["binomial(%d, %d) == %d" % (n, k, ans)]))
        i += 1
    for n in range(5, 11):
        ans = 2 ** n
        dvals = [2 ** (n - 1), n * n, 2 * n]
        assert _distinct([ans] + dvals), n
        stmt = ("What is the sum of all the entries in row $%d$ of Pascal's "
                "triangle?" % n)
        variants.append(_mk(
            "PS-pas-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "Each row's entries sum to a power of two: row $%d$ sums to "
            "$2^{%d} = %d$. Halving to $%d$ comes from using $2^{%d}$ — an "
            "off-by-one on the row number." % (n, n, ans, 2 ** (n - 1), n - 1),
            ["2**%d == %d" % (n, ans)]))
        i += 1
    return _floor("pascal-row", variants)


def _rs_pascal(s):
    if "sum of all the entries" in s:
        n = int(re.search(r"row \$(\d+)\$", s).group(1))
        return ("num", 2 ** n)
    m = re.search(r"position \$(\d+)\$ \(counting from \$0\$\) of row \$(\d+)\$", s)
    return ("num", comb(int(m.group(2)), int(m.group(1))))


# -------------------------------------------------------------------------
# Form 9: single-event (probability-models, level 1)
# -------------------------------------------------------------------------
_SEV = [(3, 5), (2, 7), (4, 5), (3, 7), (5, 7), (2, 5), (5, 3), (7, 3),
        (4, 9), (3, 4), (7, 5), (5, 9)]


def _gen_single_event():
    variants = []
    for i, (r, b) in enumerate(_SEV):
        p = Fraction(r, r + b)
        dvals = [Fraction(r, b), Fraction(b, r + b), Fraction(1, 2)]
        assert _distinct([p] + dvals), (r, b)
        stmt = ("A bag contains $%d$ red and $%d$ blue marbles. One marble "
                "is drawn at random. What is the probability that it is red?"
                % (r, b))
        variants.append(_mk(
            "PS-sev-v%02d" % (i + 1), stmt, _fr(p),
            [_fr(v) for v in dvals], i,
            "Probability is favourable over TOTAL: $\\frac{%d}{%d + %d} = %s$. "
            "Dividing red by blue, $%s$, gives odds — not a probability."
            % (r, r, b, _fr_core(p), _fr_core(Fraction(r, b))),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (r, r + b, p.numerator, p.denominator)]))
    return _floor("single-event", variants)


def _rs_single_event(s):
    m = re.search(r"\$(\d+)\$ red and \$(\d+)\$ blue", s)
    r, b = int(m.group(1)), int(m.group(2))
    return ("num", Rational(r, r + b))


# -------------------------------------------------------------------------
# Form 10: complement (probability-models, level 2)
# -------------------------------------------------------------------------
_RAIN = [(2, 5), (3, 7), (2, 7), (3, 8), (4, 9), (2, 9)]


def _gen_complement():
    variants = []
    i = 0
    for (p, q) in _RAIN:
        ans = Fraction(q - p, q)
        dvals = [Fraction(p, q), Fraction(q, p), Fraction(1, q)]
        assert _distinct([ans] + dvals), (p, q)
        stmt = ("The probability that it rains tomorrow is $\\frac{%d}{%d}$. "
                "What is the probability that it does not rain?" % (p, q))
        variants.append(_mk(
            "PS-comp-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(v) for v in dvals], i,
            "Rain and no-rain are complements, so subtract from one: "
            "$1 - \\frac{%d}{%d} = %s$. Answering $\\frac{%d}{%d}$ again "
            "forgets the complement entirely." % (p, q, _fr_core(ans), p, q),
            ["1 - Rational(%d, %d) == Rational(%d, %d)"
             % (p, q, ans.numerator, ans.denominator)]))
        i += 1
    for k in range(1, 7):
        ans = Fraction(5, 6)
        dvals = [Fraction(1, 6), Fraction(1, 2), Fraction(2, 3)]
        stmt = ("A fair die is rolled once. What is the probability of not "
                "rolling a $%d$?" % k)
        variants.append(_mk(
            "PS-comp-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(v) for v in dvals], i,
            "Five of the six equally likely faces are not $%d$, so the "
            "probability is $1 - \\frac{1}{6} = \\frac{5}{6}$. Answering "
            "$\\frac{1}{2}$ (\"it happens or it doesn't\") ignores the six "
            "equally likely faces." % k,
            ["1 - Rational(1, 6) == Rational(5, 6)"]))
        i += 1
    return _floor("complement", variants)


def _rs_complement(s):
    if "die" in s:
        return ("num", Rational(5, 6))
    p = _fracs_in(s)[0]
    return ("num", 1 - _rat(p))


# -------------------------------------------------------------------------
# Form 11: conditional-from-counts (conditional-probability, level 3)
# -------------------------------------------------------------------------
_COND = [(40, 16, 6), (60, 24, 9), (30, 12, 5), (45, 15, 6), (36, 16, 10),
         (48, 16, 10), (60, 25, 10), (80, 32, 12), (54, 18, 8), (42, 14, 6),
         (64, 24, 9), (72, 27, 12), (56, 21, 9), (90, 36, 15), (66, 22, 8),
         (70, 28, 16)]


def _gen_conditional():
    variants = []
    i = 0
    for (N, A, B) in _COND:
        if len(variants) >= 12:
            break
        ans = Fraction(B, A)
        dvals = [Fraction(B, N), Fraction(A, N), Fraction(A - B, A)]
        if not _distinct([ans] + dvals):
            continue
        stmt = ("A school has $%d$ students; $%d$ of them play chess, and "
                "$%d$ of the chess players are girls. One chess player is "
                "chosen at random. What is the probability that a girl is "
                "chosen?" % (N, A, B))
        variants.append(_mk(
            "PS-cond-v%02d" % (len(variants) + 1), stmt, _fr(ans),
            [_fr(v) for v in dvals], i,
            "The draw is from the $%d$ chess players only, so "
            "$P = \\frac{%d}{%d} = %s$. Dividing by all $%d$ students, "
            "$%s$, uses the wrong total — the condition shrank the sample "
            "space." % (A, B, A, _fr_core(ans), N, _fr_core(Fraction(B, N))),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (B, A, ans.numerator, ans.denominator)]))
        i += 1
    return _floor("conditional-from-counts", variants)


def _rs_conditional(s):
    m = re.search(r"has \$(\d+)\$ students; \$(\d+)\$ of them play chess, "
                  r"and \$(\d+)\$", s)
    return ("num", Rational(int(m.group(3)), int(m.group(2))))


# -------------------------------------------------------------------------
# Form 12: independent-and (conditional-probability, level 2)
# -------------------------------------------------------------------------
_IND = [(Fraction(1, 2), Fraction(2, 3)), (Fraction(1, 3), Fraction(3, 5)),
        (Fraction(1, 4), Fraction(2, 5)), (Fraction(1, 2), Fraction(1, 3)),
        (Fraction(2, 3), Fraction(3, 4)), (Fraction(1, 5), Fraction(1, 2)),
        (Fraction(2, 5), Fraction(2, 3)), (Fraction(1, 6), Fraction(1, 2)),
        (Fraction(3, 4), Fraction(1, 3)), (Fraction(1, 2), Fraction(3, 5)),
        (Fraction(1, 3), Fraction(1, 4)), (Fraction(2, 3), Fraction(1, 5))]


def _gen_independent():
    variants = []
    for i, (p, q) in enumerate(_IND):
        ans = p * q
        dvals = [p + q, p + q - p * q, (p + q) / 2]
        assert _distinct([ans] + dvals), (p, q)
        stmt = ("Events $A$ and $B$ are independent, with "
                "$P(A) = %s$ and $P(B) = %s$. Find $P(A \\cap B)$."
                % (_fr_core(p), _fr_core(q)))
        stmt = stmt.replace("= \\frac", "= \\frac")  # keep fracs bare inside $
        stmt = ("Events $A$ and $B$ are independent, with "
                "$P(A) = %s$ and $P(B) = %s$. Find $P(A \\cap B)$."
                % (_fr_core(p), _fr_core(q)))
        variants.append(_mk(
            "PS-ind-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(v) for v in dvals], i,
            "Independent events multiply: $P(A \\cap B) = %s \\cdot %s = %s$. "
            "The formula $P(A) + P(B) - P(A)P(B) = %s$ computes "
            "$P(A \\cup B)$ — the OR, not the AND."
            % (_fr_core(p), _fr_core(q), _fr_core(ans),
               _fr_core(p + q - p * q)),
            ["Rational(%d, %d)*Rational(%d, %d) == Rational(%d, %d)"
             % (p.numerator, p.denominator, q.numerator, q.denominator,
                ans.numerator, ans.denominator)]))
    return _floor("independent-and", variants)


def _rs_independent(s):
    p, q = _fracs_in(s)[:2]
    return ("num", _rat(p * q))


# -------------------------------------------------------------------------
# Form 13: expected-value (random-variables, level 3) — sole form of its
# unit, so it carries 24 variants to clear the >= 24-per-unit gate.
# -------------------------------------------------------------------------
_EV_VALS = [(1, 2, 3), (0, 2, 5), (1, 3, 6), (2, 4, 7), (1, 5, 10), (0, 3, 8),
            (2, 5, 9), (1, 4, 8), (3, 5, 10), (0, 4, 9), (2, 6, 11), (1, 2, 5)]
_EV_PROBS = [(1, 2, 1, 4), (1, 1, 2, 4), (1, 2, 3, 6), (2, 3, 1, 6),
             (3, 1, 2, 6), (1, 3, 4, 8), (2, 1, 5, 8), (3, 4, 1, 8),
             (1, 4, 5, 10), (2, 3, 5, 10), (1, 1, 3, 5), (2, 1, 2, 5)]


def _gen_expected_value():
    variants = []
    i = 0
    for off in range(len(_EV_PROBS)):
        for vi, (v1, v2, v3) in enumerate(_EV_VALS):
            if len(variants) >= 24:
                return _floor("expected-value", variants)
            a, b, c, n = _EV_PROBS[(vi + off) % len(_EV_PROBS)]
            assert a + b + c == n
            probs = [Fraction(a, n), Fraction(b, n), Fraction(c, n)]
            ev = v1 * probs[0] + v2 * probs[1] + v3 * probs[2]
            dvals = [Fraction(v1 + v2 + v3, 3), Fraction(v3), Fraction(v1 + v2 + v3)]
            if not _distinct([ev] + dvals):
                continue
            stmt = ("A random variable $X$ takes the values $%d$, $%d$, and "
                    "$%d$ with probabilities $%s$, $%s$, and $%s$ "
                    "respectively. Find $E(X)$."
                    % (v1, v2, v3, _fr_core(probs[0]), _fr_core(probs[1]),
                       _fr_core(probs[2])))
            if any(v["statement"] == stmt for v in variants):
                continue
            variants.append(_mk(
                "PS-ev-v%02d" % (len(variants) + 1), stmt, _fr(ev),
                [_fr(v) for v in dvals], i,
                "Weight each value by its probability: $E(X) = "
                "%d \\cdot %s + %d \\cdot %s + %d \\cdot %s = %s$. Averaging "
                "the three values equally, $%s$, ignores the weights."
                % (v1, _fr_core(probs[0]), v2, _fr_core(probs[1]),
                   v3, _fr_core(probs[2]), _fr_core(ev),
                   _fr_core(Fraction(v1 + v2 + v3, 3))),
                ["%d*Rational(%d, %d) + %d*Rational(%d, %d) + "
                 "%d*Rational(%d, %d) == Rational(%d, %d)"
                 % (v1, probs[0].numerator, probs[0].denominator,
                    v2, probs[1].numerator, probs[1].denominator,
                    v3, probs[2].numerator, probs[2].denominator,
                    ev.numerator, ev.denominator),
                 "Rational(%d, %d) + Rational(%d, %d) + Rational(%d, %d) == 1"
                 % (probs[0].numerator, probs[0].denominator,
                    probs[1].numerator, probs[1].denominator,
                    probs[2].numerator, probs[2].denominator)]))
            i += 1
    return _floor("expected-value", variants, lo=24)


def _rs_expected_value(s):
    m = re.search(r"values \$(-?\d+)\$, \$(-?\d+)\$, and \$(-?\d+)\$", s)
    vals = [int(m.group(j)) for j in (1, 2, 3)]
    probs = _fracs_in(s)
    assert len(probs) == 3 and sum(probs) == 1
    return ("num", _rat(sum(v * p for v, p in zip(vals, probs))))


# -------------------------------------------------------------------------
# Form 14: binomial-exact (binomial-distribution, level 3) — sole form of
# its unit, so it carries 24 variants (12 coin + 12 die).
# -------------------------------------------------------------------------
_COIN = [(3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3),
         (5, 4), (6, 2), (6, 3), (6, 4)]
_DIE = [(3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3),
        (5, 4), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)]


def _gen_binomial_exact():
    variants = []
    i = 0
    for (n, k) in _COIN:
        ans = Fraction(comb(n, k), 2 ** n)
        cands = [Fraction(1, 2 ** n), Fraction(k, n), Fraction(comb(n, k), n),
                 Fraction(comb(n, k), 2 ** (n + 1)), Fraction(k + 1, 2 ** n)]
        dvals = []
        for c in cands:
            if c != ans and c not in dvals:
                dvals.append(c)
            if len(dvals) == 3:
                break
        assert _distinct([ans] + dvals) and len(dvals) == 3, (n, k)
        stmt = ("A fair coin is flipped $%d$ times. What is the probability "
                "of getting exactly $%d$ heads?" % (n, k))
        variants.append(_mk(
            "PS-bin-v%02d" % (len(variants) + 1), stmt, _fr(ans),
            [_fr(v) for v in dvals], i,
            "There are $\\binom{%d}{%d} = %d$ orders for the heads among "
            "$2^{%d} = %d$ equally likely outcomes, so $P = %s$. Answering "
            "$%s$ forgets the $\\binom{%d}{%d}$ orderings."
            % (n, k, comb(n, k), n, 2 ** n, _fr_core(ans),
               _fr_core(Fraction(1, 2 ** n)), n, k),
            ["binomial(%d, %d)*Rational(1, 2)**%d == Rational(%d, %d)"
             % (n, k, n, ans.numerator, ans.denominator)]))
        i += 1
    for (n, k) in _DIE:
        if len(variants) >= 24:
            break
        ans = Fraction(comb(n, k) * 2 ** (n - k), 3 ** n)
        cands = [Fraction(2 ** (n - k), 3 ** n),
                 Fraction(comb(n, k) * 2 ** k, 3 ** n), Fraction(k, n),
                 Fraction(comb(n, k), 3 ** n), Fraction(2 ** k, 3 ** n)]
        dvals = []
        for c in cands:
            if c != ans and c not in dvals:
                dvals.append(c)
            if len(dvals) == 3:
                break
        assert _distinct([ans] + dvals) and len(dvals) == 3, (n, k)
        stmt = ("A fair die is rolled $%d$ times. What is the probability "
                "that it shows a five or a six on exactly $%d$ of the rolls?"
                % (n, k))
        variants.append(_mk(
            "PS-bin-v%02d" % (len(variants) + 1), stmt, _fr(ans),
            [_fr(v) for v in dvals], i,
            "Each roll succeeds with $p = \\frac{2}{6} = \\frac{1}{3}$, so "
            "$P = \\binom{%d}{%d}\\left(\\frac{1}{3}\\right)^{%d}"
            "\\left(\\frac{2}{3}\\right)^{%d} = %s$. Swapping the exponents "
            "gives $%s$ — success and failure traded places."
            % (n, k, k, n - k, _fr_core(ans),
               _fr_core(Fraction(comb(n, k) * 2 ** k, 3 ** n))),
            ["binomial(%d, %d)*Rational(1, 3)**%d*Rational(2, 3)**%d == "
             "Rational(%d, %d)"
             % (n, k, k, n - k, ans.numerator, ans.denominator)]))
        i += 1
    return _floor("binomial-exact", variants, lo=24)


def _rs_binomial_exact(s):
    if "coin" in s:
        m = re.search(r"flipped \$(\d+)\$ times.*exactly \$(\d+)\$ heads", s)
        n, k = int(m.group(1)), int(m.group(2))
        return ("num", Rational(comb(n, k), 2 ** n))
    m = re.search(r"rolled \$(\d+)\$ times.*exactly \$(\d+)\$ of the rolls", s)
    n, k = int(m.group(1)), int(m.group(2))
    return ("num", comb(n, k) * Rational(1, 3) ** k * Rational(2, 3) ** (n - k))


# -------------------------------------------------------------------------
# Form 15: mean-median (describing-data, level 1)
# -------------------------------------------------------------------------
_MEAN_LISTS = [[7, 2, 9, 4, 3], [12, 3, 9, 5, 1], [4, 11, 2, 8, 5],
               [10, 1, 7, 3, 4], [6, 13, 2, 9, 5], [8, 1, 12, 5, 4]]
_MEDIAN_LISTS = [[9, 2, 4, 6, 13], [3, 10, 8, 1, 6], [11, 5, 2, 8, 3],
                 [8, 12, 4, 9, 3], [14, 3, 10, 6, 1], [5, 1, 9, 12, 3]]


def _list_tex(vals):
    return ", ".join("$%d$" % v for v in vals)


def _gen_mean_median():
    variants = []
    i = 0
    for vals in _MEAN_LISTS:
        s5 = sorted(vals)
        assert sum(vals) % 5 == 0
        mean = Fraction(sum(vals), 5)
        med, mid, mm = Fraction(s5[2]), Fraction(vals[2]), Fraction(s5[0] + s5[4], 2)
        assert _distinct([mean, med, mid, mm]), vals
        stmt = "Find the mean of the data set: %s." % _list_tex(vals)
        variants.append(_mk(
            "PS-mm-v%02d" % (i + 1), stmt, _fr(mean),
            [_fr(med), _fr(mid), _fr(mm)], i,
            "Add and divide by the count: $\\frac{%s}{5} = %s$. The middle "
            "value of the sorted list, $%d$, is the median — a different "
            "statistic." % (" + ".join(str(v) for v in vals), _fr_core(mean), s5[2]),
            ["Rational(%s, 5) == %s"
             % (" + ".join(str(v) for v in vals), _fr_core_py(mean))]))
        i += 1
    for vals in _MEDIAN_LISTS:
        s5 = sorted(vals)
        mean = Fraction(sum(vals), 5)
        med, mid, mm = Fraction(s5[2]), Fraction(vals[2]), Fraction(s5[0] + s5[4], 2)
        assert _distinct([med, mean, mid, mm]), vals
        stmt = "Find the median of the data set: %s." % _list_tex(vals)
        variants.append(_mk(
            "PS-mm-v%02d" % (i + 1), stmt, _fr(med),
            [_fr(mean), _fr(mid), _fr(mm)], i,
            "Sort first: %s — the middle value is $%d$. Taking the middle "
            "of the UNSORTED list, $%d$, is the classic trap."
            % (", ".join("$%d$" % v for v in s5), s5[2], vals[2]),
            ["Max(%d, %d, %d) == %d" % (s5[0], s5[1], s5[2], s5[2]),
             "Min(%d, %d, %d) == %d" % (s5[2], s5[3], s5[4], s5[2])]))
        i += 1
    return _floor("mean-median", variants)


def _fr_core_py(fr):
    """Exact rational -> sympy-source text (integer or Rational(p, q))."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return "%d" % fr.numerator
    return "Rational(%d, %d)" % (fr.numerator, fr.denominator)


def _rs_mean_median(s):
    vals = [int(x) for x in re.findall(r"\$(-?\d+)\$", s)]
    assert len(vals) == 5
    if "the mean" in s:
        return ("num", Rational(sum(vals), 5))
    return ("num", sorted(vals)[2])


# -------------------------------------------------------------------------
# Form 16: add-a-value (describing-data, level 2)
# -------------------------------------------------------------------------
_ADD = [(4, 10, 12, 20), (5, 8, 9, 14), (3, 6, 8, 14), (6, 12, 11, 5),
        (4, 7, 9, 17), (5, 10, 12, 22), (7, 9, 10, 17), (3, 14, 12, 6),
        (9, 5, 6, 15), (4, 20, 18, 10), (6, 7, 8, 14), (8, 15, 14, 6)]


def _gen_add_value():
    variants = []
    for i, (n, m, M, x) in enumerate(_ADD):
        assert n * m + x == M * (n + 1)
        dvals = [Fraction(m + x, 2), Fraction(m), Fraction(n * m + x)]
        assert _distinct([Fraction(M)] + dvals), (n, m, M, x)
        stmt = ("The mean of $%d$ numbers is $%d$. After one more number, "
                "$%d$, is added to the list, what is the new mean?" % (n, m, x))
        variants.append(_mk(
            "PS-add-v%02d" % (i + 1), stmt, "$%d$" % M,
            [_fr(v) for v in dvals], i,
            "The old numbers total $%d \\cdot %d = %d$, so the new mean is "
            "$\\frac{%d + %d}{%d} = %d$. Averaging just $%d$ and $%d$ "
            "pretends the list held a single number."
            % (n, m, n * m, n * m, x, n + 1, M, m, x),
            ["Rational(%d*%d + %d, %d) == %d" % (n, m, x, n + 1, M)]))
    return _floor("add-a-value", variants)


def _rs_add_value(s):
    m = re.search(r"mean of \$(\d+)\$ numbers is \$(\d+)\$. After one more "
                  r"number, \$(-?\d+)\$", s)
    n, mn, x = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("num", Rational(n * mn + x, n + 1))


# -------------------------------------------------------------------------
# Form 17: frequency-mean (distributions-and-position, level 2)
# -------------------------------------------------------------------------
_FREQ = [(5, 7, 10, 3, 5, 2), (3, 6, 10, 4, 3, 3), (5, 8, 10, 2, 5, 3),
         (2, 6, 11, 5, 3, 2), (4, 7, 12, 5, 2, 3), (3, 8, 12, 2, 3, 5),
         (4, 6, 10, 3, 3, 4), (4, 9, 11, 2, 3, 5), (3, 5, 11, 2, 4, 4),
         (5, 9, 12, 4, 4, 2), (2, 7, 12, 5, 2, 3), (4, 6, 13, 1, 3, 6)]


def _gen_frequency_mean():
    variants = []
    for i, (v1, v2, v3, f1, f2, f3) in enumerate(_FREQ):
        sf = f1 + f2 + f3
        svf = v1 * f1 + v2 * f2 + v3 * f3
        mean = Fraction(svf, sf)
        assert mean.denominator == 1, (v1, v2, v3, f1, f2, f3)
        dvals = [Fraction(v1 + v2 + v3, 3), Fraction(sf, 3), Fraction(svf)]
        assert _distinct([mean] + dvals), (v1, v2, v3, f1, f2, f3)
        stmt = ("On a quiz, $%d$ students scored $%d$ points, $%d$ students "
                "scored $%d$ points, and $%d$ students scored $%d$ points. "
                "Find the mean score." % (f1, v1, f2, v2, f3, v3))
        variants.append(_mk(
            "PS-freq-v%02d" % (i + 1), stmt, _fr(mean),
            [_fr(v) for v in dvals], i,
            "Weight each score by how many students earned it: "
            "$\\frac{%d \\cdot %d + %d \\cdot %d + %d \\cdot %d}{%d} = %s$. "
            "Averaging just the three score values, $%s$, ignores the "
            "frequencies." % (f1, v1, f2, v2, f3, v3, sf, _fr_core(mean),
                              _fr_core(Fraction(v1 + v2 + v3, 3))),
            ["Rational(%d*%d + %d*%d + %d*%d, %d) == %s"
             % (f1, v1, f2, v2, f3, v3, sf, _fr_core_py(mean))]))
    return _floor("frequency-mean", variants)


def _rs_frequency_mean(s):
    pairs = re.findall(r"\$(\d+)\$ students scored \$(\d+)\$ points", s)
    assert len(pairs) == 3
    sf = sum(int(f) for f, _v in pairs)
    svf = sum(int(f) * int(v) for f, v in pairs)
    return ("num", Rational(svf, sf))


# -------------------------------------------------------------------------
# Form 18: range-iqr-position (distributions-and-position, level 1)
# -------------------------------------------------------------------------
_RANGE_LISTS = [[12, 3, 7, 18, 5], [21, 6, 14, 9, 2], [8, 15, 3, 11, 6],
                [17, 4, 9, 13, 6], [25, 10, 16, 7, 13], [5, 19, 11, 2, 8]]
_Q1_LISTS = [[2, 5, 7, 9, 12, 15], [1, 4, 6, 10, 13, 17],
             [3, 6, 8, 11, 14, 20], [2, 4, 9, 13, 16, 21],
             [5, 8, 10, 14, 18, 22], [1, 3, 7, 11, 15, 19]]


def _gen_range_q1():
    variants = []
    i = 0
    for vals in _RANGE_LISTS:
        s5 = sorted(vals)
        rng = s5[4] - s5[0]
        dvals = [Fraction(s5[4]), Fraction(rng + 1), Fraction(s5[2])]
        assert _distinct([Fraction(rng)] + dvals), vals
        stmt = "Find the range of the data set: %s." % _list_tex(vals)
        variants.append(_mk(
            "PS-rng-v%02d" % (i + 1), stmt, "$%d$" % rng,
            [_fr(v) for v in dvals], i,
            "Range is largest minus smallest: $%d - %d = %d$. Reporting the "
            "maximum $%d$ alone confuses the spread with the biggest value."
            % (s5[4], s5[0], rng, s5[4]),
            ["%d - %d == %d" % (s5[4], s5[0], rng),
             "Max(%s) == %d" % (", ".join(str(v) for v in vals), s5[4])]))
        i += 1
    for vals in _Q1_LISTS:
        a, b, c, d = vals[0], vals[1], vals[2], vals[3]
        q1 = Fraction(b)
        dvals = [Fraction(c + d, 2), Fraction(c), Fraction(a)]
        assert _distinct([q1] + dvals), vals
        stmt = ("The data set %s is already sorted. Find $Q_1$, the median "
                "of the lower half." % _list_tex(vals))
        variants.append(_mk(
            "PS-rng-v%02d" % (i + 1), stmt, "$%d$" % b,
            [_fr(v) for v in dvals], i,
            "The lower half is $%d$, $%d$, $%d$, and its middle value is "
            "$%d$. The value $%s$ is the median of the WHOLE set, not $Q_1$."
            % (a, b, c, b, _fr_core(Fraction(c + d, 2))),
            ["Max(%d, %d) == %d" % (a, b, b),
             "Min(%d, %d) == %d" % (b, c, b)]))
        i += 1
    return _floor("range-iqr-position", variants)


def _rs_range_q1(s):
    vals = [int(x) for x in re.findall(r"\$(-?\d+)\$", s)]
    if "the range" in s:
        assert len(vals) == 5
        return ("num", max(vals) - min(vals))
    vals = [v for v in vals if True]
    assert "lower half" in s and len(vals) == 6
    return ("num", sorted(vals)[1])

# -------------------------------------------------------------------------
# Form 19: line-of-fit (two-variable-data, level 2)
# -------------------------------------------------------------------------
_FIT = [(3, 4, 5), (2, 7, 6), (4, -3, 3), (5, 2, 4), (2, 9, 8), (3, -5, 7),
        (6, -1, 4), (4, 5, 6), (2, -4, 9), (5, 8, 2), (3, 7, 5), (7, 2, 4)]


def _gen_fit():
    variants = []
    for i, (a, b, c) in enumerate(_FIT):
        ans = a * c + b
        dvals = [Fraction(a + b * c), Fraction(a * b + c), Fraction(a * (c + b))]
        assert _distinct([Fraction(ans)] + dvals)
        bs = "+ %d" % b if b >= 0 else "- %d" % (-b)
        stmt = ("A line of best fit for a scatterplot is $\\hat{y} = %dx %s$. "
                "Predict $\\hat{y}$ when $x = %d$." % (a, bs, c))
        variants.append(_mk(
            "PS-fit-v%02d" % (i + 1), stmt, "$%d$" % ans,
            [_fr(v) for v in dvals], i,
            "Substitute the $x$-value into the line: $%d \\cdot %d %s = %d$. "
            "The slope multiplies $x$; the intercept is added once, not "
            "multiplied." % (a, c, bs, ans),
            ["%d*%d + (%d) == %d" % (a, c, b, ans)]))
    return _floor("line-of-fit", variants)


def _rs_fit(s):
    m = re.search(r"\\hat\{y\} = (-?\d+)x ([+-]) (\d+)\$", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    c = int(re.search(r"x = (-?\d+)\$", s).group(1))
    return ("num", a * c + b)


# -------------------------------------------------------------------------
# Form 19b: scatterplot-association (two-variable-data, level 1)
# -------------------------------------------------------------------------
_OPT_ASSOC = ["A positive association", "A negative association",
              "No association", "A perfect linear relationship"]
_ASSOC = [
    ("hours a student studies", "the score they earn on the exam",
     "tends to INCREASE", "A positive association"),
    ("a car's age in years", "its resale value",
     "tends to DECREASE", "A negative association"),
    ("a student's shoe size", "their score on a history quiz",
     "shows NO CLEAR PATTERN", "No association"),
    ("daily temperature", "the number of visitors at a swimming pool",
     "tends to INCREASE", "A positive association"),
    ("the altitude of a hiking trail", "the air temperature along it",
     "tends to DECREASE", "A negative association"),
    ("the last digit of a phone number", "the owner's monthly rent",
     "shows NO CLEAR PATTERN", "No association"),
    ("the number of practice free throws taken", "the number made in a game",
     "tends to INCREASE", "A positive association"),
    ("the number of absences a student has", "their course grade",
     "tends to DECREASE", "A negative association"),
    ("a person's house number", "the number of pets they own",
     "shows NO CLEAR PATTERN", "No association"),
    ("the size of an engine", "the fuel it burns per kilometer",
     "tends to INCREASE", "A positive association"),
    ("the price of a concert ticket", "the number of tickets sold",
     "tends to DECREASE", "A negative association"),
    ("the length of a family's surname", "their weekly grocery bill",
     "shows NO CLEAR PATTERN", "No association"),
]


def _gen_assoc():
    variants = []
    for i, (xdesc, ydesc, trend, correct) in enumerate(_ASSOC):
        dopts = [o for o in _OPT_ASSOC if o != correct][:3]
        stmt = ("A scatterplot compares %s ($x$) with %s ($y$). As $x$ "
                "increases, $y$ %s. Which best describes the association?"
                % (xdesc, ydesc, trend))
        if correct == "A positive association":
            why = ("both variables rise together, so the cloud of points "
                   "slopes upward")
        elif correct == "A negative association":
            why = ("$y$ falls as $x$ rises, so the cloud of points slopes "
                   "downward")
        else:
            why = ("knowing $x$ tells you nothing about $y$; the points "
                   "form no sloped cloud")
        variants.append(_mk(
            "PS-assoc-v%02d" % (i + 1), stmt, correct, dopts, i,
            "Here %s. A real scatterplot is rarely a PERFECT line — "
            "association describes the overall trend, not an exact fit."
            % why,
            ["%d == %d" % (i, i)]))
    return _floor("scatterplot-association", variants)


def _rs_assoc(s):
    if "INCREASE" in s:
        return ("opt", "A positive association")
    if "DECREASE" in s:
        return ("opt", "A negative association")
    assert "NO CLEAR PATTERN" in s
    return ("opt", "No association")


# -------------------------------------------------------------------------
# Form 20: study-type (inference-and-studies, level 1)
# -------------------------------------------------------------------------
_OPT_STUDY = ["an experiment", "an observational study", "a census",
              "a sample survey"]
_STUDIES = [
    ("A researcher randomly ASSIGNS half of 60 plants to a new fertilizer "
     "and half to none, then compares growth.", "an experiment"),
    ("A doctor reviews EXISTING hospital records to compare recovery times "
     "of two treatments patients already chose.", "an observational study"),
    ("The school asks EVERY SINGLE student in the building which lunch "
     "option they prefer.", "a census"),
    ("A pollster RANDOMLY SELECTS 400 of a city's voters and asks whom "
     "they support.", "a sample survey"),
    ("A lab randomly ASSIGNS volunteers to sleep 6 or 8 hours, then "
     "measures reaction time.", "an experiment"),
    ("A biologist WATCHES wild birds and records their feeding habits "
     "without interfering.", "an observational study"),
    ("The census bureau contacts EVERY SINGLE household in the district "
     "to count residents.", "a census"),
    ("A store RANDOMLY SELECTS 150 of its customers and asks them to rate "
     "the service.", "a sample survey"),
    ("Students are randomly ASSIGNED to two teaching methods and take the "
     "same test afterward.", "an experiment"),
    ("A nutritionist compares the EXISTING diets that two groups of "
     "runners already follow.", "an observational study"),
    ("The teacher polls EVERY SINGLE member of the class about the trip "
     "date.", "a census"),
    ("A news site RANDOMLY SELECTS 1000 of the country's adults and asks "
     "one question.", "a sample survey"),
]


def _gen_study():
    variants = []
    for i, (scen, correct) in enumerate(_STUDIES):
        dopts = [o for o in _OPT_STUDY if o != correct][:3]
        if correct == "an experiment":
            why = ("the researcher ASSIGNS the treatment — that active "
                   "assignment is exactly what makes it an experiment")
        elif correct == "an observational study":
            why = ("no treatment is assigned; existing behavior is only "
                   "watched or looked up")
        elif correct == "a census":
            why = "EVERY member of the group is measured, not a subset"
        else:
            why = ("a random SUBSET of the population answers — a sample "
                   "standing in for the whole")
        variants.append(_mk(
            "PS-study-v%02d" % (i + 1), scen + " This is best described as…",
            correct, dopts, i,
            "Here %s. Assignment → experiment; watching → observational; "
            "everyone → census; a chosen subset → sample survey." % why,
            ["%d == %d" % (i, i)]))
    return _floor("study-type", variants)


def _rs_study(s):
    if "ASSIGNS" in s or "ASSIGNED" in s:
        return ("opt", "an experiment")
    if "EVERY SINGLE" in s:
        return ("opt", "a census")
    if "RANDOMLY SELECTS" in s:
        return ("opt", "a sample survey")
    assert "EXISTING" in s or "WATCHES" in s
    return ("opt", "an observational study")


# -------------------------------------------------------------------------
# Form 21: sample-vs-population (inference-and-studies, level 2)
# -------------------------------------------------------------------------
_POP = [(12000, 200, 45), (30000, 300, 120), (8000, 100, 35),
        (24000, 400, 150), (15000, 250, 90), (40000, 500, 210),
        (9000, 150, 60), (18000, 300, 75), (20000, 200, 88),
        (36000, 600, 260), (10000, 125, 40), (28000, 350, 140)]


def _gen_pop():
    variants = []
    for i, (N, n, k) in enumerate(_POP):
        assert (N * k) % n == 0, (N, n, k)
        ans = N * k // n
        dvals = [Fraction(k), Fraction(k * n), Fraction(N - k)]
        assert _distinct([Fraction(ans)] + dvals)
        stmt = ("A city has $%d$ residents. In a random sample of $%d$ "
                "residents, $%d$ approve of a new park. What is the best "
                "estimate of the TOTAL number of residents who approve?"
                % (N, n, k))
        variants.append(_mk(
            "PS-pop-v%02d" % (i + 1), stmt, "$%d$" % ans,
            [_fr(v) for v in dvals], i,
            "Scale the sample rate up to the population: "
            "$\\frac{%d}{%d} \\cdot %d = %d$. The raw count $%d$ describes "
            "only the sample, not the whole city." % (k, n, N, ans, k),
            ["Rational(%d, %d)*%d == %d" % (k, n, N, ans)]))
    return _floor("sample-vs-population", variants)


def _rs_pop(s):
    N = int(re.search(r"has \$(\d+)\$ residents", s).group(1))
    n = int(re.search(r"sample of \$(\d+)\$ residents", s).group(1))
    k = int(re.search(r"\$(\d+)\$ approve", s).group(1))
    return ("num", Rational(N * k, n))


# =========================================================================
# Assembly
# =========================================================================

_FORMS_META = [
    ("multiplication-principle", "The multiplication principle", 1,
     "counting-principles",
     "Independent choices multiply: each option pairs with every other.",
     _gen_mult, _rs_mult),
    ("addition-or-multiplication", "Add or multiply?", 2,
     "counting-principles",
     "OR means add the counts; AND (one of each) means multiply.",
     _gen_aor, _rs_aor),
    ("npr-value", "Permutations nPr", 1, "permutations",
     "Order matters: n!/(n−r)! counts arrangements.",
     _gen_npr, _rs_npr),
    ("arrangements", "Arranging people in a row", 2, "permutations",
     "n people in a row: n!. Fixing one position leaves (n−1)!.",
     _gen_arrangements, _rs_arrangements),
    ("ncr-value", "Combinations nCr", 1, "combinations",
     "Order ignored: divide the arrangements by r!.",
     _gen_ncr, _rs_ncr),
    ("committee", "Committees from two groups", 2, "combinations",
     "Choose from each group separately, then multiply the counts.",
     _gen_committee, _rs_committee),
    ("binomial-coefficient", "Coefficients in (x + a)^n", 2,
     "binomial-theorem",
     "The x^(n−k) term carries C(n, k)·a^k — both parts, not just one.",
     _gen_bco, _rs_bco),
    ("pascal-row", "Reading Pascal's triangle", 1, "binomial-theorem",
     "Entry k of row n is C(n, k); the whole row sums to 2^n.",
     _gen_pascal, _rs_pascal),
    ("single-event", "One draw from a bag", 1, "probability-models",
     "Favorable over TOTAL — the denominator counts everything in the bag.",
     _gen_single_event, _rs_single_event),
    ("complement", "The complement rule", 2, "probability-models",
     "P(not A) = 1 − P(A) — the two must add to 1.",
     _gen_complement, _rs_complement),
    ("conditional-from-counts", "Conditional probability from counts", 3,
     "conditional-probability",
     "Given B, the denominator shrinks to B's count — not the whole group.",
     _gen_conditional, _rs_conditional),
    ("independent-and", "Independent AND", 2, "conditional-probability",
     "Independent events: multiply. Adding gives OR (minus the overlap).",
     _gen_independent, _rs_independent),
    ("expected-value", "Expected value", 3, "random-variables",
     "E(X) = Σ value · probability — a weighted average, not a plain one.",
     _gen_expected_value, _rs_expected_value),
    ("binomial-exact", "Exactly k successes", 3, "binomial-distribution",
     "P = C(n,k) p^k (1−p)^(n−k) — the C(n,k) counts the orders.",
     _gen_binomial_exact, _rs_binomial_exact),
    ("mean-median", "Mean and median", 1, "describing-data",
     "Mean: sum ÷ count. Median: middle of the SORTED list.",
     _gen_mean_median, _rs_mean_median),
    ("add-a-value", "How a new value moves the mean", 2, "describing-data",
     "New mean = (old sum + new value) ÷ (n + 1).",
     _gen_add_value, _rs_add_value),
    ("frequency-mean", "Mean from a frequency table", 2,
     "distributions-and-position",
     "Weight each value by its frequency before dividing.",
     _gen_frequency_mean, _rs_frequency_mean),
    ("range-iqr-position", "Range and quartile position", 1,
     "distributions-and-position",
     "Range = max − min; Q1 is the median of the lower half.",
     _gen_range_q1, _rs_range_q1),
    ("line-of-fit", "Predicting with a fitted line", 2, "two-variable-data",
     "Substitute x into ŷ = ax + b — slope times x, plus the intercept once.",
     _gen_fit, _rs_fit),
    ("scatterplot-association", "Reading a scatterplot's trend", 1,
     "two-variable-data",
     "Upward cloud → positive; downward → negative; no slope → none.",
     _gen_assoc, _rs_assoc),
    ("study-type", "What kind of study is this?", 1, "inference-and-studies",
     "Assigning → experiment; watching → observational; everyone → census; "
     "a subset → sample survey.",
     _gen_study, _rs_study),
    ("sample-vs-population", "From sample to population", 2,
     "inference-and-studies",
     "Scale the sample proportion up to the population size.",
     _gen_pop, _rs_pop),
]


def new_forms():
    forms = []
    for fid, title, level, unit, skill, gen, _rz in _FORMS_META:
        forms.append({"id": fid, "title": title, "level": level,
                      "unit": unit, "skill": skill, "variants": gen()})
    return forms


RESOLVERS.update({fid: rz for fid, _t, _l, _u, _s, _g, rz in _FORMS_META})


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = new_forms()
    for f in forms:
        assert f["unit"] in unit_order, "%s: unknown unit %r" % (f["id"], f["unit"])
    forms.sort(key=lambda f: (unit_order[f["unit"]], f["level"], f["id"]))
    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    data = build()
    total = sum(len(f["variants"]) for f in data["forms"])
    per_unit = {u["id"]: 0 for u in UNITS}
    for f in data["forms"]:
        per_unit[f["unit"]] += len(f["variants"])
    ids = [v["id"] for f in data["forms"] for v in f["variants"]]
    assert len(ids) == len(set(ids)), "variant ids not unique"
    empty = [u for u, n in per_unit.items() if n == 0]
    print("SELFCHECK OK  forms=%d  total=%d  units=%d  empty_units=%s"
          % (len(data["forms"]), total, len(UNITS), ",".join(empty) or "none"))
