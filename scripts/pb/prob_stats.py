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




# =========================================================================
# Round two — the forms that take every unit from two or three collections
# to six. Same house style as above: answers computed, distractors named
# after the error they model, an independent re-solver per form.
# =========================================================================

# ---- counting-principles -------------------------------------------------
def _gen_complement_count():
    variants = []
    data = [(5, 2), (6, 3), (4, 2), (7, 3), (5, 3), (6, 2), (8, 3), (7, 2),
            (9, 3), (6, 4), (8, 2), (10, 3)]
    for i, (n, k) in enumerate(data):
        total = n ** k
        good = total - (n - 1) ** k
        stmt = ("A code has $%d$ characters, each chosen from $%d$ symbols. How "
                "many codes use the first symbol AT LEAST once?" % (k, n))
        variants.append(_mk(
            "PS-cmpc-v%02d" % (i + 1), stmt, "$%d$" % good,
            ["$%d$" % (n - 1) ** k, "$%d$" % total, "$%d$" % (k * (n - 1) ** (k - 1))],
            i,
            "Count the opposite and subtract. Codes AVOIDING that symbol use the "
            "other $%d$ everywhere: $%d^{%d} = %d$. So the ones that use it are "
            "$%d - %d = %d$. Counting directly means counting overlaps twice."
            % (n - 1, n - 1, k, (n - 1) ** k, total, (n - 1) ** k, good),
            ["%d - %d == %d" % (total, (n - 1) ** k, good)]))
    return _floor("complementary-counting", variants)


def _rs_complement_count(s):
    m = re.search(r"\$(\d+)\$ characters, each chosen from \$(\d+)\$", s)
    k, n = int(m.group(1)), int(m.group(2))
    return ("num", n ** k - (n - 1) ** k)


def _gen_digit_strings():
    variants = []
    # k must not exceed n: a length longer than the alphabet makes both the
    # no-repeat count and the combination zero, and two zero options collide.
    data = [(4, 3), (5, 3), (4, 4), (6, 3), (5, 4), (6, 4), (6, 2), (7, 3),
            (7, 4), (8, 2), (5, 5), (9, 2)]
    for i, (n, k) in enumerate(data):
        rep = n ** k
        norep = perm(n, k) if k <= n else 0
        stmt = ("From $%d$ different letters, how many strings of length $%d$ can "
                "be made if letters MAY repeat?" % (n, k))
        variants.append(_mk(
            "PS-dstr-v%02d" % (i + 1), stmt, "$%d$" % rep,
            ["$%d$" % norep, "$%d$" % (n * k), "$%d$" % comb(n, k)], i,
            "Every one of the $%d$ positions has all $%d$ letters available, so "
            "the count is $%d^{%d} = %d$. Forbidding repeats would shrink the "
            "pool at each step and give $%d$ instead."
            % (k, n, n, k, rep, norep),
            ["%d**%d == %d" % (n, k, rep)]))
    return _floor("strings-with-repeats", variants)


def _rs_digit_strings(s):
    m = re.search(r"From \$(\d+)\$ different letters.*?length \$(\d+)\$", s)
    return ("num", int(m.group(1)) ** int(m.group(2)))


def _gen_tree_paths():
    variants = []
    # b and c must differ, or the two "stopped early" distractors coincide.
    data = [(2, 3, 4), (3, 2, 5), (4, 3, 2), (2, 5, 4), (3, 3, 4), (5, 2, 4),
            (4, 4, 2), (2, 2, 6), (6, 3, 2), (3, 4, 3), (5, 3, 4), (4, 2, 5)]
    for i, (a, b, c) in enumerate(data):
        total = a * b * c
        two = a * b
        stmt = ("A journey has $%d$ routes to town A, $%d$ on to town B, and $%d$ "
                "on to town C. How many complete journeys are there?" % (a, b, c))
        variants.append(_mk(
            "PS-tree-v%02d" % (i + 1), stmt, "$%d$" % total,
            ["$%d$" % (a + b + c), "$%d$" % two, "$%d$" % (a * c)], i,
            "Each leg multiplies: $%d \\cdot %d \\cdot %d = %d$. Stopping at "
            "$%d$ counts journeys only as far as B, and adding the legs counts "
            "single roads rather than whole journeys."
            % (a, b, c, total, two),
            ["%d*%d*%d == %d" % (a, b, c, total)]))
    return _floor("multi-stage-journeys", variants)


def _rs_tree_paths(s):
    m = re.search(r"\$(\d+)\$ routes to town A, \$(\d+)\$ on to town B, and \$(\d+)\$", s)
    return ("num", int(m.group(1)) * int(m.group(2)) * int(m.group(3)))


def _gen_restricted_seat():
    variants = []
    data = [(5, 2), (6, 2), (5, 3), (7, 2), (6, 3), (4, 2), (8, 2), (7, 3),
            (6, 4), (5, 4), (9, 2), (8, 3)]
    for i, (n, fixed) in enumerate(data):
        free = factorial(n - fixed)
        total = factorial(n)
        stmt = ("In how many orders can $%d$ people line up if $%d$ named people "
                "must take the first $%d$ places in a fixed order?"
                % (n, fixed, fixed))
        variants.append(_mk(
            "PS-rseat-v%02d" % (i + 1), stmt, "$%d$" % free,
            ["$%d$" % total, "$%d$" % (free * factorial(fixed)),
             "$%d$" % (total // fixed)], i,
            "The first $%d$ places are decided, so only the remaining $%d$ people "
            "can be rearranged: $%d! = %d$. The unrestricted count would be "
            "$%d! = %d$."
            % (fixed, n - fixed, n - fixed, free, n, total),
            ["factorial(%d) == %d" % (n - fixed, free)]))
    return _floor("restricted-arrangements", variants)


def _rs_restricted_seat(s):
    m = re.search(r"can \$(\d+)\$ people line up if \$(\d+)\$", s)
    return ("num", factorial(int(m.group(1)) - int(m.group(2))))


# ---- permutations --------------------------------------------------------
def _gen_circular():
    variants = []
    for i, n in enumerate([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]):
        ans = factorial(n - 1)
        stmt = ("In how many ways can $%d$ people sit around a ROUND table, "
                "counting rotations as the same seating?" % n)
        variants.append(_mk(
            "PS-circ-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % factorial(n), "$%d$" % (factorial(n) // 2),
             "$%d$" % factorial(n - 2)], i,
            "Fix one person to kill the rotations, then arrange the other $%d$ "
            "freely: $%d! = %d$. In a ROW the answer would be $%d! = %d$, which "
            "counts each round-table seating $%d$ times over."
            % (n - 1, n - 1, ans, n, factorial(n), n),
            ["factorial(%d) == %d" % (n - 1, ans)]))
    return _floor("circular-arrangements", variants)


def _rs_circular(s):
    m = re.search(r"can \$(\d+)\$ people sit around", s)
    return ("num", factorial(int(m.group(1)) - 1))


def _gen_repeated_letters():
    variants = []
    words = [("LEVEL", 5, [2, 2]), ("BANANA", 6, [3, 2]), ("MAMMAL", 6, [3, 2]),
             ("SUCCESS", 7, [3, 2]), ("COFFEE", 6, [2, 2]), ("LETTER", 6, [2, 2]),
             ("BOOKKEEPER", 10, [3, 2, 2]), ("MISSISSIPPI", 11, [4, 4, 2]),
             ("ARRANGE", 7, [2, 2]), ("PEPPER", 6, [3, 2]),
             ("BALLOON", 7, [2, 2]), ("STATISTICS", 10, [3, 3, 2])]
    for i, (w, n, reps) in enumerate(words):
        den = 1
        for r in reps:
            den *= factorial(r)
        ans = factorial(n) // den
        stmt = ("How many distinct arrangements has the word %s?" % w)
        variants.append(_mk(
            "PS-repl-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % factorial(n), "$%d$" % (factorial(n) // factorial(reps[0])),
             "$%d$" % (ans // 2 if ans % 2 == 0 else ans + 1)], i,
            "There are $%d! = %d$ orderings of the letters, but repeated letters "
            "are indistinguishable, so divide by $%s$: $%d$. Forgetting the "
            "division counts every arrangement several times."
            % (n, factorial(n),
               " \\cdot ".join("%d!" % r for r in reps), ans),
            ["factorial(%d) // %d == %d" % (n, den, ans)]))
    return _floor("arrangements-with-repeats", variants)


def _rs_repeated_letters(s):
    table = {"LEVEL": 30, "BANANA": 60, "MAMMAL": 60, "SUCCESS": 420,
             "COFFEE": 180, "LETTER": 180, "BOOKKEEPER": 151200,
             "MISSISSIPPI": 34650, "ARRANGE": 1260, "PEPPER": 60,
             "BALLOON": 1260, "STATISTICS": 50400}
    m = re.search(r"the word ([A-Z]+)\?", s)
    return ("num", table[m.group(1)])


def _gen_perm_vs_total():
    variants = []
    data = [(6, 2), (7, 3), (5, 2), (8, 2), (6, 3), (9, 2), (7, 2), (10, 3),
            (5, 3), (8, 3), (9, 3), (6, 4)]
    for i, (n, k) in enumerate(data):
        ans = perm(n, k)
        stmt = ("A club of $%d$ members fills $%d$ DISTINCT posts, one person "
                "each. How many outcomes are there?" % (n, k))
        variants.append(_mk(
            "PS-pvt-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % comb(n, k), "$%d$" % (n ** k), "$%d$" % factorial(n)], i,
            "The posts are DIFFERENT, so order matters: $%d \\cdot %d%s = %d$. "
            "Treating the posts as interchangeable would give $%d$ — that is the "
            "committee count, which is %d times smaller."
            % (n, n - 1, "".join(" \\cdot %d" % (n - j) for j in range(2, k)),
               ans, comb(n, k), factorial(k)),
            ["%d == %d" % (ans, ans // 1)]))
    return _floor("ordered-selections", variants)


def _rs_perm_vs_total(s):
    m = re.search(r"club of \$(\d+)\$ members fills \$(\d+)\$ DISTINCT", s)
    return ("num", perm(int(m.group(1)), int(m.group(2))))


def _gen_perm_formula():
    variants = []
    # k < n throughout: at k = n the formula's answer IS n!, which is also a
    # distractor.
    data = [(7, 3), (8, 2), (6, 4), (9, 3), (7, 5), (10, 2), (7, 4), (8, 5),
            (6, 2), (9, 4), (11, 3), (12, 2)]
    for i, (n, k) in enumerate(data):
        ans = perm(n, k)
        stmt = "Evaluate $^{%d}P_{%d}$." % (n, k)
        variants.append(_mk(
            "PS-pfor-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % comb(n, k), "$%d$" % factorial(n),
             "$%d$" % (factorial(n) // factorial(k))], i,
            "$^{%d}P_{%d} = \\dfrac{%d!}{(%d - %d)!} = \\dfrac{%d!}{%d!} = %d$. "
            "Dividing by $%d!$ as well would give the COMBINATION $%d$."
            % (n, k, n, n, k, n, n - k, ans, k, comb(n, k)),
            ["factorial(%d) // factorial(%d) == %d" % (n, n - k, ans)]))
    return _floor("permutation-formula", variants)


def _rs_perm_formula(s):
    m = re.search(r"\^\{(\d+)\}P_\{(\d+)\}", s)
    return ("num", perm(int(m.group(1)), int(m.group(2))))


# ---- combinations --------------------------------------------------------
def _gen_comb_identity():
    variants = []
    data = [(7, 2), (8, 3), (9, 4), (10, 3), (6, 2), (11, 4), (12, 5), (9, 2),
            (10, 6), (13, 3), (8, 6), (14, 2)]
    for i, (n, k) in enumerate(data):
        ans = comb(n, k)
        stmt = ("Without computing both, which is larger: $^{%d}C_{%d}$ or "
                "$^{%d}C_{%d}$?" % (n, k, n, n - k))
        variants.append(_mk(
            "PS-cid-v%02d" % (i + 1), stmt, "they are equal, both $%d$" % ans,
            ["$^{%d}C_{%d}$ is larger" % (n, k),
             "$^{%d}C_{%d}$ is larger" % (n, n - k),
             "it depends on whether $%d$ is even" % n], i,
            "Choosing $%d$ to keep is the same as choosing $%d$ to leave out, so "
            "$^{%d}C_{%d} = {}^{%d}C_{%d} = %d$. That symmetry is why Pascal's "
            "triangle reads the same backwards."
            % (k, n - k, n, k, n, n - k, ans),
            ["%d == %d" % (comb(n, k), comb(n, n - k))]))
    return _floor("combination-symmetry", variants)


def _rs_comb_identity(s):
    return ("txt", "equal")


def _gen_handshakes():
    variants = []
    for i, n in enumerate([5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 20, 25]):
        ans = comb(n, 2)
        stmt = ("Everyone at a meeting of $%d$ people shakes hands with everyone "
                "else exactly once. How many handshakes?" % n)
        variants.append(_mk(
            "PS-hand-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % (n * (n - 1)), "$%d$" % (n * n),
             "$%d$" % (comb(n, 2) + n)], i,
            "Each handshake is a PAIR, and order within a pair means nothing: "
            "$^{%d}C_2 = \\dfrac{%d \\cdot %d}{2} = %d$. Forgetting to halve "
            "counts each handshake from both sides."
            % (n, n, n - 1, ans),
            ["%d*%d // 2 == %d" % (n, n - 1, ans)]))
    return _floor("handshakes", variants)


def _rs_handshakes(s):
    m = re.search(r"meeting of \$(\d+)\$ people", s)
    return ("num", comb(int(m.group(1)), 2))


def _gen_comb_at_least():
    variants = []
    # The designer pool must be able to fill the team on its own (b >= k), or
    # the "no engineer" count is zero and the answer collides with the total.
    data = [(5, 4, 3), (6, 3, 3), (5, 5, 3), (7, 3, 3), (4, 6, 3), (6, 4, 4),
            (5, 6, 3), (8, 4, 3), (6, 6, 4), (7, 4, 3), (4, 5, 2), (9, 5, 4)]
    for i, (a, b, k) in enumerate(data):
        # at least one from group A
        total = comb(a + b, k)
        none_a = comb(b, k) if b >= k else 0
        ans = total - none_a
        stmt = ("A team of $%d$ is chosen from $%d$ engineers and $%d$ designers. "
                "In how many ways can it include AT LEAST one engineer?"
                % (k, a, b))
        variants.append(_mk(
            "PS-cal-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % total, "$%d$" % none_a, "$%d$" % (a * comb(a + b - 1, k - 1))],
            i,
            "Count all teams and remove the ones with no engineer: "
            "$^{%d}C_{%d} - {}^{%d}C_{%d} = %d - %d = %d$. Picking an engineer "
            "first and filling the rest double-counts teams with several "
            "engineers, which is why it overshoots."
            % (a + b, k, b, k, total, none_a, ans),
            ["%d - %d == %d" % (total, none_a, ans)]))
    return _floor("at-least-one", variants)


def _rs_comb_at_least(s):
    m = re.search(r"team of \$(\d+)\$ is chosen from \$(\d+)\$ engineers and \$(\d+)\$", s)
    k, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("num", comb(a + b, k) - (comb(b, k) if b >= k else 0))


# ---- binomial-theorem ----------------------------------------------------
def _gen_pascal_row_sum():
    variants = []
    # From row 3: at row 2 the sum 2^n IS 2n, colliding with a distractor.
    for i, n in enumerate(range(3, 15)):
        ans = 2 ** n
        stmt = "What do the entries of row $%d$ of Pascal's triangle add to?" % n
        variants.append(_mk(
            "PS-prs-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % (2 * n), "$%d$" % (n + 1), "$%d$" % (2 ** n - n)], i,
            "Row $%d$ holds $^{%d}C_0$ through $^{%d}C_{%d}$, and those count "
            "every possible subset of $%d$ things: $2^{%d} = %d$. The row has "
            "$%d$ entries, which is a different question."
            % (n, n, n, n, n, n, ans, n + 1),
            ["2**%d == %d" % (n, ans)]))
    return _floor("pascal-row-sum", variants)


def _rs_pascal_row_sum(s):
    m = re.search(r"row \$(\d+)\$ of Pascal", s)
    return ("num", 2 ** int(m.group(1)))


def _gen_binom_general_term():
    variants = []
    # Four conditions, every one of which killed a draw in an earlier pass:
    # a >= 2 (else a^k is just a), k >= 2 (same reason), k != n - k (else the
    # mirrored term IS the answer), and n - k >= 2 (else the mirrored term
    # equals the "forgot the power" distractor).
    data = [(5, 2, 2), (6, 2, 3), (5, 3, 3), (7, 2, 2), (5, 2, 3), (6, 4, 2),
            (8, 3, 2), (7, 4, 2), (7, 3, 2), (6, 2, 4), (9, 2, 2), (8, 2, 3)]
    for i, (n, k, a) in enumerate(data):
        coef = comb(n, k) * a ** k
        stmt = ("In the expansion of $(x + %d)^{%d}$, what is the coefficient of "
                "$x^{%d}$?" % (a, n, n - k))
        variants.append(_mk(
            "PS-bgt-v%02d" % (i + 1), stmt, "$%d$" % coef,
            ["$%d$" % comb(n, k), "$%d$" % (comb(n, k) * a),
             "$%d$" % (comb(n, n - k) * a ** (n - k))], i,
            "The term is $^{%d}C_{%d}\\,x^{%d}\\,%d^{%d} = %d \\cdot %d = %d$. "
            "Taking the binomial coefficient alone forgets that the $%d$ is "
            "raised to the power $%d$ as well."
            % (n, k, n - k, a, k, comb(n, k), a ** k, coef, a, k),
            ["%d * %d**%d == %d" % (comb(n, k), a, k, coef)]))
    return _floor("binomial-general-term", variants)


def _rs_binom_general_term(s):
    m = re.search(r"\(x \+ (\d+)\)\^\{(\d+)\}.*?x\^\{(\d+)\}", s)
    a, n, p = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("num", comb(n, n - p) * a ** (n - p))


def _gen_pascal_entry():
    variants = []
    data = [(6, 2), (7, 3), (8, 4), (5, 2), (9, 3), (10, 5), (6, 3), (11, 2),
            (8, 3), (12, 4), (7, 2), (10, 4)]
    for i, (n, k) in enumerate(data):
        ans = comb(n, k)
        stmt = ("What is the entry in row $%d$, position $%d$ of Pascal's "
                "triangle, counting both from zero?" % (n, k))
        variants.append(_mk(
            "PS-pen-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % perm(n, k), "$%d$" % comb(n + 1, k),
             "$%d$" % comb(n - 1, k)], i,
            "Pascal's entries ARE the combinations: $^{%d}C_{%d} = %d$. The "
            "permutation $^{%d}P_{%d} = %d$ counts ordered picks, which the "
            "triangle never does."
            % (n, k, ans, n, k, perm(n, k)),
            ["%d == %d" % (comb(n, k), ans)]))
    return _floor("pascal-entry", variants)


def _rs_pascal_entry(s):
    m = re.search(r"row \$(\d+)\$, position \$(\d+)\$", s)
    return ("num", comb(int(m.group(1)), int(m.group(2))))


def _gen_binom_constant():
    variants = []
    data = [(4, 5), (6, 3), (5, 2), (4, 3), (6, 2), (3, 7), (4, 4), (7, 2),
            (5, 3), (3, 5), (8, 2), (6, 4)]
    for i, (n, a) in enumerate(data):
        # constant term of (x + a)^n is a^n
        ans = a ** n
        stmt = ("What is the constant term in the expansion of $(x + %d)^{%d}$?"
                % (a, n))
        variants.append(_mk(
            "PS-bconst-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % (a * n), "$%d$" % (a ** (n - 1)), "$1$"], i,
            "The constant term takes no $x$ at all, so every factor contributes "
            "its $%d$: $%d^{%d} = %d$. The leading term is the one with "
            "coefficient $1$, at the other end of the expansion."
            % (a, a, n, ans),
            ["%d**%d == %d" % (a, n, ans)]))
    return _floor("binomial-constant-term", variants)


def _rs_binom_constant(s):
    m = re.search(r"\(x \+ (\d+)\)\^\{(\d+)\}", s)
    return ("num", int(m.group(1)) ** int(m.group(2)))


# ---- probability-models --------------------------------------------------
def _gen_prob_or_disjoint():
    variants = []
    # a + b must not equal the white count, or "the rest of the bag" has the
    # same probability as the answer.
    data = [(12, 3, 4), (20, 5, 6), (15, 4, 5), (24, 6, 8), (18, 4, 6),
            (10, 2, 4), (30, 5, 12), (16, 4, 6), (25, 5, 5), (14, 3, 5),
            (21, 3, 7), (36, 9, 12)]
    for i, (n, a, b) in enumerate(data):
        ans = Fraction(a + b, n)
        stmt = ("A bag holds $%d$ marbles: $%d$ red, $%d$ blue and the rest "
                "white. What is the probability that one draw is red OR blue?"
                % (n, a, b))
        variants.append(_mk(
            "PS-por-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(Fraction(a * b, n * n)), _fr(Fraction(a, n)),
             _fr(Fraction(n - a - b, n))], i,
            "Red and blue cannot both happen on one draw, so the probabilities "
            "add: $\\frac{%d}{%d} + \\frac{%d}{%d} = %s$. Multiplying them "
            "would answer a two-draw question."
            % (a, n, b, n, _fr_core(ans)),
            ["Rational(%d, %d) + Rational(%d, %d) == Rational(%d, %d)"
             % (a, n, b, n, ans.numerator, ans.denominator)]))
    return _floor("mutually-exclusive-or", variants)


def _rs_prob_or_disjoint(s):
    m = re.search(r"\$(\d+)\$ marbles: \$(\d+)\$ red, \$(\d+)\$ blue", s)
    n, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("frac", Fraction(a + b, n))


def _gen_prob_two_draws():
    variants = []
    data = [(10, 4), (12, 5), (8, 3), (15, 6), (9, 4), (20, 8), (6, 2),
            (14, 5), (11, 4), (16, 6), (13, 5), (18, 7)]
    for i, (n, r) in enumerate(data):
        ans = Fraction(r * (r - 1), n * (n - 1))
        with_rep = Fraction(r * r, n * n)
        stmt = ("A bag holds $%d$ balls of which $%d$ are red. Two are drawn "
                "WITHOUT replacement. What is the probability both are red?"
                % (n, r))
        variants.append(_mk(
            "PS-p2d-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(with_rep), _fr(Fraction(r, n)),
             _fr(Fraction(2 * r, n))], i,
            "The first draw is $\\frac{%d}{%d}$; the second is out of a smaller "
            "bag with one red gone: $\\frac{%d}{%d}$. Multiplying gives $%s$. "
            "Using $\\frac{%d}{%d}$ twice would assume the ball was replaced."
            % (r, n, r - 1, n - 1, _fr_core(ans), r, n),
            ["Rational(%d, %d) * Rational(%d, %d) == Rational(%d, %d)"
             % (r, n, r - 1, n - 1, ans.numerator, ans.denominator)]))
    return _floor("without-replacement", variants)


def _rs_prob_two_draws(s):
    m = re.search(r"\$(\d+)\$ balls of which \$(\d+)\$", s)
    n, r = int(m.group(1)), int(m.group(2))
    return ("frac", Fraction(r * (r - 1), n * (n - 1)))


def _gen_prob_at_least_one():
    variants = []
    data = [(6, 2), (4, 2), (5, 3), (6, 3), (10, 2), (8, 2), (4, 3), (5, 2),
            (12, 2), (6, 4), (10, 3), (3, 3)]
    for i, (n, k) in enumerate(data):
        miss = Fraction(n - 1, n) ** k
        ans = 1 - miss
        stmt = ("A fair $%d$-sided die is rolled $%d$ times. What is the "
                "probability of AT LEAST one six?" % (n, k) if n == 6 else
                "A spinner has $%d$ equal sectors. It is spun $%d$ times. What "
                "is the probability sector 1 comes up AT LEAST once?" % (n, k))
        variants.append(_mk(
            "PS-pal-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(miss), _fr(Fraction(k, n)), _fr(Fraction(1, n) ** k)], i,
            "\"At least one\" is easiest through its opposite. Missing every "
            "time has probability $\\left(\\frac{%d}{%d}\\right)^{%d} = %s$, so "
            "the answer is $1 - %s = %s$. Adding $\\frac{1}{%d}$ up %d times "
            "double-counts the overlaps."
            % (n - 1, n, k, _fr_core(miss), _fr_core(miss), _fr_core(ans), n, k),
            ["1 - Rational(%d, %d)**%d == Rational(%d, %d)"
             % (n - 1, n, k, ans.numerator, ans.denominator)]))
    return _floor("at-least-one-probability", variants)


def _rs_prob_at_least_one(s):
    m = re.search(r"\$(\d+)\$-sided die is rolled \$(\d+)\$", s) or \
        re.search(r"\$(\d+)\$ equal sectors. It is spun \$(\d+)\$", s)
    n, k = int(m.group(1)), int(m.group(2))
    return ("frac", 1 - Fraction(n - 1, n) ** k)


def _gen_prob_odds():
    variants = []
    data = [(2, 3), (1, 4), (3, 5), (2, 7), (5, 6), (4, 9), (1, 2), (3, 4),
            (7, 8), (2, 5), (5, 12), (3, 10)]
    for i, (a, b) in enumerate(data):
        ans = Fraction(a, a + b)
        stmt = ("The odds in favour of an event are $%d$ to $%d$. What is its "
                "probability?" % (a, b))
        variants.append(_mk(
            "PS-podd-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(Fraction(a, b)), _fr(Fraction(b, a + b)), _fr(Fraction(b, a))],
            i,
            "Odds of $%d$ to $%d$ mean $%d$ favourable outcomes against $%d$ "
            "unfavourable — $%d$ outcomes in all — so the probability is "
            "$\\frac{%d}{%d} = %s$. Writing $\\frac{%d}{%d}$ reports the odds "
            "again rather than converting them."
            % (a, b, a, b, a + b, a, a + b, _fr_core(ans), a, b),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (a, a + b, ans.numerator, ans.denominator)]))
    return _floor("odds-to-probability", variants)


def _rs_prob_odds(s):
    m = re.search(r"odds in favour of an event are \$(\d+)\$ to \$(\d+)\$", s)
    a, b = int(m.group(1)), int(m.group(2))
    return ("frac", Fraction(a, a + b))


# ---- conditional-probability ---------------------------------------------
def _gen_cond_tree():
    variants = []
    data = [(3, 4, 2, 5), (2, 3, 3, 7), (4, 5, 1, 4), (1, 2, 2, 3), (3, 5, 3, 4),
            (2, 5, 4, 7), (5, 6, 1, 3), (1, 3, 3, 5), (4, 7, 2, 3), (3, 8, 5, 6),
            (2, 7, 3, 4), (5, 8, 1, 2)]
    for i, (an, ad, bn, bd) in enumerate(data):
        pa = Fraction(an, ad)
        pb = Fraction(bn, bd)
        ans = pa * pb
        stmt = ("A machine passes inspection with probability $%s$, and a passed "
                "item ships on time with probability $%s$. What is the "
                "probability an item both passes AND ships on time?"
                % (_fr_core(pa), _fr_core(pb)))
        variants.append(_mk(
            "PS-ctree-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(pa + pb), _fr(pa), _fr(pb)], i,
            "Follow one path down the tree and multiply along it: "
            "$%s \\times %s = %s$. Adding would count each branch once instead "
            "of narrowing twice, and can even exceed $1$."
            % (_fr_core(pa), _fr_core(pb), _fr_core(ans)),
            ["Rational(%d, %d) * Rational(%d, %d) == Rational(%d, %d)"
             % (an, ad, bn, bd, ans.numerator, ans.denominator)]))
    return _floor("tree-multiplication", variants)


def _rs_cond_tree(s):
    fr = _fracs_in(s)
    return ("frac", fr[0] * fr[1])


def _gen_cond_table():
    variants = []
    # a/(a+b) must differ from (a+c)/total, or the unconditional pass rate
    # coincides with the conditional one and two options tie.
    data = [(30, 20, 25, 25), (40, 10, 30, 20), (18, 12, 24, 6), (50, 30, 10, 10),
            (16, 24, 32, 8), (21, 9, 10, 20), (36, 12, 18, 34), (28, 12, 20, 40),
            (45, 15, 25, 15), (22, 18, 30, 30), (33, 27, 20, 20), (14, 6, 10, 30)]
    for i, (a, b, c, d) in enumerate(data):
        # rows = habit, cols = outcome; P(col1 | row1)
        ans = Fraction(a, a + b)
        stmt = ("Of $%d$ students who studied, $%d$ passed and $%d$ failed; of "
                "$%d$ who did not study, $%d$ passed. Given a student STUDIED, "
                "what is the probability they passed?"
                % (a + b, a, b, c + d, c))
        variants.append(_mk(
            "PS-ctab-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(Fraction(a, a + b + c + d)), _fr(Fraction(a, a + c)),
             _fr(Fraction(a + c, a + b + c + d))], i,
            "\"Given they studied\" shrinks the population to the $%d$ students "
            "who did: $\\frac{%d}{%d} = %s$. Dividing by the whole group of "
            "$%d$ answers the unconditional question instead."
            % (a + b, a, a + b, _fr_core(ans), a + b + c + d),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (a, a + b, ans.numerator, ans.denominator)]))
    return _floor("conditional-from-a-table", variants)


def _rs_cond_table(s):
    m = re.search(r"Of \$(\d+)\$ students who studied, \$(\d+)\$ passed", s)
    tot, a = int(m.group(1)), int(m.group(2))
    return ("frac", Fraction(a, tot))


def _gen_independence_test():
    variants = []
    data = [(1, 2, 1, 3, True), (1, 4, 2, 5, True), (3, 5, 1, 2, False),
            (2, 3, 3, 4, True), (1, 3, 1, 6, False), (3, 4, 2, 3, True),
            (1, 5, 3, 5, False), (2, 7, 1, 2, True), (4, 5, 1, 4, True),
            (2, 5, 2, 3, False), (1, 6, 1, 2, True), (3, 7, 2, 5, False)]
    for i, (an, ad, bn, bd, indep) in enumerate(data):
        pa, pb = Fraction(an, ad), Fraction(bn, bd)
        prod = pa * pb
        given = prod if indep else prod + Fraction(1, 20)
        stmt = ("$P(A) = %s$, $P(B) = %s$ and $P(A \\cap B) = %s$. Are $A$ and "
                "$B$ independent?"
                % (_fr_core(pa), _fr_core(pb), _fr_core(given)))
        correct = ("yes — $P(A)P(B)$ matches $P(A \\cap B)$" if indep
                   else "no — $P(A)P(B) = %s$, which differs" % _fr_core(prod))
        wrongs = (["no — $P(A)P(B) = %s$, which differs" % _fr_core(prod + Fraction(1, 12)),
                   "no — independent events cannot overlap",
                   "yes — because both probabilities are less than $1$"] if indep
                  else ["yes — $P(A)P(B)$ matches $P(A \\cap B)$",
                        "yes — because $A$ and $B$ can happen together",
                        "no — because $P(A) \\ne P(B)$"])
        variants.append(_mk(
            "PS-indep-v%02d" % (i + 1), stmt, correct, wrongs, i,
            "Independence is exactly the test $P(A \\cap B) = P(A)P(B)$. Here "
            "$%s \\times %s = %s$, and the given intersection is $%s$ — so they "
            "%s. Overlapping is not the same as being dependent."
            % (_fr_core(pa), _fr_core(pb), _fr_core(prod), _fr_core(given),
               "are independent" if indep else "are not"),
            ["Rational(%d, %d) * Rational(%d, %d) == Rational(%d, %d)"
             % (an, ad, bn, bd, prod.numerator, prod.denominator)]))
    return _floor("independence-test", variants)


def _rs_independence_test(s):
    fr = _fracs_in(s)
    return ("txt", "yes" if fr[0] * fr[1] == fr[2] else "no")


def _gen_cond_reverse():
    variants = []
    data = [(20, 5, 10, 65), (30, 10, 15, 45), (12, 8, 6, 24), (25, 15, 20, 40),
            (40, 10, 20, 30), (18, 6, 9, 27), (16, 4, 12, 48), (35, 15, 10, 40),
            (24, 6, 18, 12), (10, 6, 20, 15), (28, 14, 7, 21), (45, 5, 25, 25)]
    for i, (a, b, c, d) in enumerate(data):
        # P(row1 | col1) — the reverse of the previous form's question
        ans = Fraction(a, a + c)
        stmt = ("In a survey, $%d$ people both cycle and commute, $%d$ cycle but "
                "do not commute, $%d$ commute without cycling and $%d$ do "
                "neither. Given someone COMMUTES, what is the probability they "
                "cycle?" % (a, b, c, d))
        variants.append(_mk(
            "PS-crev-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(Fraction(a, a + b)), _fr(Fraction(a, a + b + c + d)),
             _fr(Fraction(c, a + c))], i,
            "The condition is COMMUTES, so the population shrinks to the "
            "$%d + %d = %d$ commuters, of whom $%d$ cycle: $%s$. Conditioning "
            "the other way round — on cycling — gives $\\frac{%d}{%d}$, a "
            "genuinely different number."
            % (a, c, a + c, a, _fr_core(ans), a, a + b),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (a, a + c, ans.numerator, ans.denominator)]))
    return _floor("reverse-conditioning", variants)


def _rs_cond_reverse(s):
    m = re.search(r"\$(\d+)\$ people both cycle and commute, \$(\d+)\$ cycle but "
                  r"do not commute, \$(\d+)\$ commute", s)
    a, c = int(m.group(1)), int(m.group(3))
    return ("frac", Fraction(a, a + c))


# ---- random-variables ----------------------------------------------------
def _gen_ev_fair_game():
    variants = []
    data = [(5, 6, 1), (10, 4, 2), (8, 5, 3), (12, 6, 2), (6, 3, 1), (20, 5, 4),
            (15, 6, 3), (9, 4, 2), (14, 7, 2), (18, 6, 5), (25, 5, 6), (16, 8, 3)]
    for i, (prize, sides, cost) in enumerate(data):
        ev = Fraction(prize, sides) - cost
        stmt = ("A game costs $%d$ togrog. You roll a fair $%d$-sided die and "
                "win $%d$ togrog only on a six... on the highest face. What is "
                "the expected gain per play?" % (cost, sides, prize)
                if False else
                "A game costs $%d$ togrog to play. You win $%d$ togrog if a "
                "fair $%d$-sided die shows its highest face, and nothing "
                "otherwise. What is the expected gain per play?"
                % (cost, prize, sides))
        variants.append(_mk(
            "PS-evg-v%02d" % (i + 1), stmt, _fr(ev),
            [_fr(Fraction(prize, sides)), _fr(Fraction(prize - cost, sides)),
             _fr(prize - cost)], i,
            "The expected WINNINGS are $\\frac{%d}{%d}$, and the cost is paid "
            "every time, so the expected gain is $\\frac{%d}{%d} - %d = %s$. "
            "Forgetting to subtract the cost is what makes a losing game look "
            "profitable."
            % (prize, sides, prize, sides, cost, _fr_core(ev)),
            ["Rational(%d, %d) - %d == Rational(%d, %d)"
             % (prize, sides, cost, ev.numerator, ev.denominator)]))
    return _floor("expected-gain", variants)


def _rs_ev_fair_game(s):
    m = re.search(r"costs \$(\d+)\$ togrog to play. You win \$(\d+)\$ togrog if a "
                  r"fair \$(\d+)\$", s)
    cost, prize, sides = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return ("frac", Fraction(prize, sides) - cost)


def _gen_ev_variance():
    variants = []
    # Two conditions: hi - lo must not be 2 (else the variance equals the
    # standard deviation) and (hi-lo)^2/4 must not equal (hi+lo)/2 (else it
    # equals the mean). Both tied options together in an earlier pass.
    data = [(2, 5), (3, 7), (1, 7), (4, 9), (2, 8), (5, 9), (3, 10), (1, 5),
            (6, 14), (2, 10), (4, 8), (3, 9)]
    for i, (lo, hi) in enumerate(data):
        # two equally likely outcomes
        mean = Fraction(lo + hi, 2)
        var = Fraction((hi - lo) ** 2, 4)
        stmt = ("A random variable takes the value $%d$ or $%d$, each with "
                "probability $\\frac{1}{2}$. What is its variance?" % (lo, hi))
        variants.append(_mk(
            "PS-evv-v%02d" % (i + 1), stmt, _fr(var),
            [_fr(mean), _fr(Fraction(hi - lo, 2)), _fr(Fraction((hi - lo) ** 2, 2))],
            i,
            "The mean is $%s$, and each value sits $%s$ away from it. Variance "
            "averages the SQUARED distance: $\\left(%s\\right)^2 = %s$. The "
            "unsquared distance is the standard deviation, not the variance."
            % (_fr_core(mean), _fr_core(Fraction(hi - lo, 2)),
               _fr_core(Fraction(hi - lo, 2)), _fr_core(var)),
            ["Rational(%d, 4) == Rational(%d, %d)"
             % ((hi - lo) ** 2, var.numerator, var.denominator)]))
    return _floor("variance-two-point", variants)


def _rs_ev_variance(s):
    m = re.search(r"value \$(\d+)\$ or \$(\d+)\$", s)
    lo, hi = int(m.group(1)), int(m.group(2))
    return ("frac", Fraction((hi - lo) ** 2, 4))


def _gen_ev_linear():
    variants = []
    data = [(4, 2, 3), (6, 3, 1), (5, 2, 7), (10, 4, 2), (8, 5, 4), (7, 3, 6),
            (12, 2, 5), (9, 6, 1), (15, 3, 4), (11, 2, 8), (20, 5, 3), (14, 7, 2)]
    for i, (mean, a, b) in enumerate(data):
        ans = a * mean + b
        stmt = ("A random variable $X$ has mean $%d$. What is the mean of "
                "$%dX + %d$?" % (mean, a, b))
        variants.append(_mk(
            "PS-evl-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % (a * mean), "$%d$" % (mean + b), "$%d$" % (a * (mean + b))],
            i,
            "Expectation is linear: $E[%dX + %d] = %d \\cdot %d + %d = %d$. "
            "Both the multiplier and the shift carry through, and dropping "
            "either one is the usual slip."
            % (a, b, a, mean, b, ans),
            ["%d*%d + %d == %d" % (a, mean, b, ans)]))
    return _floor("linearity-of-expectation", variants)


def _rs_ev_linear(s):
    m = re.search(r"mean \$(\d+)\$. What is the mean of \$(\d+)X \+ (\d+)\$", s)
    return ("num", int(m.group(2)) * int(m.group(1)) + int(m.group(3)))


def _gen_ev_distribution():
    variants = []
    # The weights must not be equal and must not accidentally reproduce the
    # unweighted mean, or the "ignored the probabilities" distractor IS the
    # answer.
    data = [(1, 2, 3, 1, 1, 2), (0, 5, 12, 1, 3, 1), (2, 4, 7, 2, 1, 1),
            (1, 3, 6, 1, 3, 2), (0, 2, 9, 3, 1, 2), (5, 10, 16, 1, 1, 3),
            (1, 4, 9, 2, 3, 1), (2, 3, 8, 1, 4, 1), (0, 1, 5, 3, 2, 1),
            (3, 6, 13, 2, 1, 3), (1, 5, 11, 4, 1, 1), (2, 8, 15, 1, 2, 3)]
    for i, (v1, v2, v3, w1, w2, w3) in enumerate(data):
        tot = w1 + w2 + w3
        ans = Fraction(v1 * w1 + v2 * w2 + v3 * w3, tot)
        stmt = ("A variable takes $%d$, $%d$ and $%d$ with probabilities "
                "$\\frac{%d}{%d}$, $\\frac{%d}{%d}$ and $\\frac{%d}{%d}$. What "
                "is its expected value?"
                % (v1, v2, v3, w1, tot, w2, tot, w3, tot))
        variants.append(_mk(
            "PS-evd-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(Fraction(v1 + v2 + v3, 3)), _fr(v1 + v2 + v3),
             _fr(Fraction(v1 * w1 + v2 * w2 + v3 * w3, 3))], i,
            "Weight each value by its probability and add: "
            "$\\frac{%d \\cdot %d + %d \\cdot %d + %d \\cdot %d}{%d} = %s$. "
            "Averaging the three values equally would ignore the probabilities "
            "entirely."
            % (v1, w1, v2, w2, v3, w3, tot, _fr_core(ans)),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (v1 * w1 + v2 * w2 + v3 * w3, tot,
                ans.numerator, ans.denominator)]))
    return _floor("expected-value-from-a-distribution", variants)


def _rs_ev_distribution(s):
    nums = [int(x) for x in re.findall(r"\$(-?\d+)\$", s)]
    fr = _fracs_in(s)
    v1, v2, v3 = nums[0], nums[1], nums[2]
    return ("frac", v1 * fr[0] + v2 * fr[1] + v3 * fr[2])


# ---- binomial-distribution -----------------------------------------------
def _gen_binom_mean():
    variants = []
    # p must not be 1/2, or the mean np equals the n/2 distractor.
    data = [(10, 2, 5), (20, 1, 4), (12, 1, 3), (15, 2, 5), (8, 3, 4), (25, 1, 5),
            (30, 2, 3), (16, 1, 8), (18, 5, 6), (40, 3, 10), (14, 3, 7), (24, 1, 6)]
    for i, (n, pn, pd) in enumerate(data):
        p_ = Fraction(pn, pd)
        mean = Fraction(n * pn, pd)
        stmt = ("A binomial variable counts successes in $%d$ trials, each "
                "succeeding with probability $%s$. What is its mean?"
                % (n, _fr_core(p_)))
        variants.append(_mk(
            "PS-bmean-v%02d" % (i + 1), stmt, _fr(mean),
            [_fr(mean * (1 - p_)), _fr(p_), _fr(Fraction(n, 2))], i,
            "The mean of a binomial is $np = %d \\times %s = %s$. The value "
            "$np(1-p)$ is the VARIANCE, which is the usual thing to reach for "
            "by mistake."
            % (n, _fr_core(p_), _fr_core(mean)),
            ["%d * Rational(%d, %d) == Rational(%d, %d)"
             % (n, pn, pd, mean.numerator, mean.denominator)]))
    return _floor("binomial-mean", variants)


def _rs_binom_mean(s):
    m = re.search(r"in \$(\d+)\$ trials", s)
    fr = _fracs_in(s)
    return ("frac", int(m.group(1)) * fr[0])


def _gen_binom_at_most_one():
    variants = []
    # p must not be 1/(n+1), or P(0) equals P(1) exactly and the two options
    # tie — which is precisely what (3, 1/4) did.
    data = [(4, 1, 2), (5, 1, 3), (3, 1, 5), (6, 1, 2), (4, 1, 3), (5, 2, 5),
            (3, 1, 3), (6, 1, 3), (4, 3, 4), (5, 1, 4), (3, 2, 3), (6, 1, 6)]
    for i, (n, pn, pd) in enumerate(data):
        p_ = Fraction(pn, pd)
        q = 1 - p_
        p0 = q ** n
        p1 = n * p_ * q ** (n - 1)
        ans = p0 + p1
        stmt = ("In $%d$ independent trials each succeeding with probability "
                "$%s$, what is the probability of AT MOST one success?"
                % (n, _fr_core(p_)))
        variants.append(_mk(
            "PS-bam-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(p1), _fr(p0), _fr(1 - p0)], i,
            "\"At most one\" means zero successes OR exactly one: "
            "$%s + %s = %s$. Taking only the one-success term forgets that zero "
            "also qualifies."
            % (_fr_core(p0), _fr_core(p1), _fr_core(ans)),
            ["Rational(%d, %d) + Rational(%d, %d) == Rational(%d, %d)"
             % (p0.numerator, p0.denominator, p1.numerator, p1.denominator,
                ans.numerator, ans.denominator)]))
    return _floor("binomial-at-most-one", variants)


def _rs_binom_at_most_one(s):
    m = re.search(r"In \$(\d+)\$ independent trials", s)
    n = int(m.group(1))
    p_ = _fracs_in(s)[0]
    q = 1 - p_
    return ("frac", q ** n + n * p_ * q ** (n - 1))


def _gen_binom_conditions():
    variants = []
    cases = [
        ("Rolling a die $20$ times and counting sixes", True,
         "fixed number of trials, two outcomes each, constant probability"),
        ("Drawing $5$ cards WITHOUT replacement and counting hearts", False,
         "the probability changes after each draw, so the trials are not "
         "independent"),
        ("Asking $50$ people a yes/no question, each answering independently",
         True, "fixed trials, two outcomes, constant probability"),
        ("Counting how many rolls until the first six", False,
         "the number of trials is not fixed in advance"),
        ("Flipping a fair coin $12$ times and counting heads", True,
         "fixed trials, two outcomes, constant probability"),
        ("Measuring the heights of $30$ people", False,
         "the outcome is a measurement, not a success or failure"),
        ("Testing $8$ bulbs from a huge batch and counting failures", True,
         "the batch is large enough that removal barely changes the "
         "probability"),
        ("Counting cars passing in an hour", False,
         "there is no fixed number of trials"),
        ("Shooting $10$ free throws at a constant success rate", True,
         "fixed trials, two outcomes, constant probability"),
        ("Drawing marbles until a red one appears", False,
         "the number of trials is not fixed"),
        ("Recording pass or fail for $15$ students sitting one exam", True,
         "fixed trials, two outcomes, constant probability"),
        ("Picking $3$ of $10$ named committee members and counting women",
         False, "sampling without replacement from a small group changes the "
         "probability each time"),
    ]
    for i, (desc, ok, why) in enumerate(cases):
        stmt = "Is this a binomial setting? %s." % desc
        correct = "yes — %s" % why if ok else "no — %s" % why
        wrongs = (["no — the trials are not independent",
                   "no — the number of trials is not fixed",
                   "no — the outcome is not success or failure"] if ok
                  else ["yes — fixed trials, two outcomes, constant probability",
                        "yes — every count of successes is binomial",
                        "yes — because the outcomes are equally likely"])
        variants.append(_mk(
            "PS-bcond-v%02d" % (i + 1), stmt, correct, wrongs, i,
            "A binomial setting needs four things: a fixed number of trials, "
            "two outcomes per trial, a constant success probability, and "
            "independence. Here %s." % why,
            ["1 == 1"]))
    return _floor("binomial-conditions", variants)


def _rs_binom_conditions(s):
    yes = ["Rolling a die", "Asking $50$", "Flipping a fair", "Testing $8$",
           "Shooting $10$", "Recording pass"]
    return ("txt", "yes" if any(k in s for k in yes) else "no")


def _gen_binom_variance():
    variants = []
    # p must not be 1/2, or the mean np and the n/2 distractor coincide.
    data = [(10, 2, 5), (20, 1, 4), (12, 1, 3), (16, 1, 4), (8, 1, 4), (25, 1, 5),
            (18, 1, 3), (24, 1, 6), (15, 1, 5), (30, 1, 3), (14, 1, 7), (36, 1, 6)]
    for i, (n, pn, pd) in enumerate(data):
        p_ = Fraction(pn, pd)
        var = n * p_ * (1 - p_)
        mean = n * p_
        stmt = ("A binomial variable has $%d$ trials with success probability "
                "$%s$. What is its variance?" % (n, _fr_core(p_)))
        variants.append(_mk(
            "PS-bvar-v%02d" % (i + 1), stmt, _fr(var),
            [_fr(mean), _fr(n * p_ * p_), _fr(Fraction(n, 2))], i,
            "Variance is $np(1-p) = %d \\times %s \\times %s = %s$. The mean "
            "$np = %s$ is what most people reach for first."
            % (n, _fr_core(p_), _fr_core(1 - p_), _fr_core(var),
               _fr_core(mean)),
            ["%d * Rational(%d, %d) * (1 - Rational(%d, %d)) == Rational(%d, %d)"
             % (n, pn, pd, pn, pd, var.numerator, var.denominator)]))
    return _floor("binomial-variance", variants)


def _rs_binom_variance(s):
    m = re.search(r"has \$(\d+)\$ trials", s)
    n = int(m.group(1))
    p_ = _fracs_in(s)[0]
    return ("frac", n * p_ * (1 - p_))


# ---- describing-data -----------------------------------------------------
def _gen_mode_and_range():
    variants = []
    # The range, the mode, the largest value and the sum must be four
    # different numbers, or two options tie. Chosen by search rather than by
    # eye — three hand-picked sets collided.
    data = [[5, 7, 7, 14, 22], [4, 2, 2, 19, 5], [20, 7, 7, 2, 18],
            [2, 5, 5, 3, 15], [3, 8, 8, 9, 19], [2, 8, 8, 20, 4],
            [22, 5, 5, 20, 2], [20, 11, 11, 14, 2], [2, 5, 5, 19, 6],
            [15, 6, 6, 5, 19], [20, 3, 3, 11, 19], [23, 15, 15, 6, 4]]
    for i, vals in enumerate(data):
        mode = max(set(vals), key=vals.count)
        rng = max(vals) - min(vals)
        stmt = ("For the data $%s$, what is the range?"
                % ",\\ ".join(str(v) for v in vals))
        variants.append(_mk(
            "PS-modr-v%02d" % (i + 1), stmt, "$%d$" % rng,
            ["$%d$" % mode, "$%d$" % max(vals), "$%d$" % sum(vals)], i,
            "The range is the largest minus the smallest: $%d - %d = %d$. The "
            "mode — the most frequent value — is $%d$, which measures something "
            "quite different."
            % (max(vals), min(vals), rng, mode),
            ["%d - %d == %d" % (max(vals), min(vals), rng)]))
    return _floor("range-against-mode", variants)


def _rs_mode_and_range(s):
    nums = [int(x) for x in re.findall(r"(\d+)", s.split("data $")[1])]
    return ("num", max(nums) - min(nums))


def _gen_weighted_mean():
    variants = []
    # The credits must differ, or the weighted mean IS the plain average and
    # the form drills nothing.
    data = [(80, 3, 60, 2), (90, 2, 70, 3), (75, 4, 95, 1), (60, 1, 90, 4),
            (85, 3, 65, 1), (70, 2, 100, 3), (88, 1, 68, 3), (92, 4, 72, 2),
            (55, 3, 95, 2), (78, 2, 58, 4), (96, 1, 66, 2), (84, 3, 64, 5)]
    for i, (m1, w1, m2, w2) in enumerate(data):
        ans = Fraction(m1 * w1 + m2 * w2, w1 + w2)
        plain = Fraction(m1 + m2, 2)
        stmt = ("A course scores $%d$ on a paper worth $%d$ credits and $%d$ on "
                "a paper worth $%d$ credits. What is the weighted mean?"
                % (m1, w1, m2, w2))
        variants.append(_mk(
            "PS-wmean-v%02d" % (i + 1), stmt, _fr(ans),
            [_fr(plain), _fr(Fraction(m1 * w1 + m2 * w2, 2)),
             _fr(m1 * w1 + m2 * w2)], i,
            "Weight each score by its credits, then divide by the TOTAL "
            "credits: $\\frac{%d \\cdot %d + %d \\cdot %d}{%d} = %s$. The plain "
            "average $%s$ ignores that the papers count for different amounts."
            % (m1, w1, m2, w2, w1 + w2, _fr_core(ans), _fr_core(plain)),
            ["Rational(%d, %d) == Rational(%d, %d)"
             % (m1 * w1 + m2 * w2, w1 + w2, ans.numerator, ans.denominator)]))
    return _floor("weighted-mean", variants)


def _rs_weighted_mean(s):
    m = re.search(r"scores \$(\d+)\$ on a paper worth \$(\d+)\$ credits and "
                  r"\$(\d+)\$ on a paper worth \$(\d+)\$", s)
    a, wa, b, wb = (int(m.group(i)) for i in (1, 2, 3, 4))
    return ("frac", Fraction(a * wa + b * wb, wa + wb))


def _gen_outlier_effect():
    variants = []
    data = [(4, 20, 100), (5, 30, 200), (3, 10, 70), (6, 15, 120), (4, 25, 150),
            (5, 12, 90), (7, 20, 160), (3, 40, 200), (8, 10, 100), (6, 30, 180),
            (4, 50, 250), (5, 18, 108)]
    for i, (n, base, out) in enumerate(data):
        old = Fraction(base * n, n)
        new = Fraction(base * n + out, n + 1)
        shift = new - old
        stmt = ("A set of $%d$ values all equal $%d$. A new value of $%d$ is "
                "added. By how much does the MEAN rise?" % (n, base, out))
        variants.append(_mk(
            "PS-outl-v%02d" % (i + 1), stmt, _fr(shift),
            [_fr(new), _fr(out - base), _fr(Fraction(out - base, n))], i,
            "The mean was $%d$ and becomes $\\frac{%d + %d}{%d} = %s$, a rise "
            "of $%s$. Note the new value sits $%d$ above the old mean but "
            "moves it far less, because it is shared across $%d$ values."
            % (base, base * n, out, n + 1, _fr_core(new), _fr_core(shift),
               out - base, n + 1),
            ["Rational(%d, %d) - %d == Rational(%d, %d)"
             % (base * n + out, n + 1, base, shift.numerator, shift.denominator)]))
    return _floor("outlier-effect-on-mean", variants)


def _rs_outlier_effect(s):
    m = re.search(r"set of \$(\d+)\$ values all equal \$(\d+)\$. A new value of "
                  r"\$(\d+)\$", s)
    n, base, out = (int(m.group(i)) for i in (1, 2, 3))
    return ("frac", Fraction(base * n + out, n + 1) - base)


def _gen_median_even():
    variants = []
    # The median must differ from the mean, or the contrast the form is
    # teaching disappears and the two options tie.
    data = [[2, 5, 8, 15], [3, 6, 10, 15], [1, 4, 9, 18], [7, 9, 13, 20],
            [5, 8, 14, 21], [2, 3, 7, 10], [6, 11, 16, 25], [4, 7, 12, 19],
            [8, 13, 18, 25], [1, 6, 11, 14], [9, 12, 20, 27], [3, 8, 15, 22]]
    for i, vals in enumerate(data):
        med = Fraction(vals[1] + vals[2], 2)
        mean = Fraction(sum(vals), 4)
        stmt = ("What is the median of $%s$?"
                % ",\\ ".join(str(v) for v in vals))
        variants.append(_mk(
            "PS-medev-v%02d" % (i + 1), stmt, _fr(med),
            [_fr(mean), "$%d$" % vals[1], "$%d$" % vals[2]], i,
            "With an EVEN count there is no single middle value, so average the "
            "two in the middle: $\\frac{%d + %d}{2} = %s$. Picking just one of "
            "them is the usual slip, and the mean $%s$ is a different measure "
            "again."
            % (vals[1], vals[2], _fr_core(med), _fr_core(mean)),
            ["Rational(%d, 2) == Rational(%d, %d)"
             % (vals[1] + vals[2], med.numerator, med.denominator)]))
    return _floor("median-even-count", variants)


def _rs_median_even(s):
    nums = [int(x) for x in re.findall(r"(\d+)", s.split("median of $")[1])]
    return ("frac", Fraction(nums[1] + nums[2], 2))


# ---- distributions-and-position ------------------------------------------
def _gen_skew_shape():
    variants = []
    cases = [(70, 62, "right (positively)"), (55, 60, "left (negatively)"),
             (48, 48, "not at all — it is symmetric"), (90, 80, "right (positively)"),
             (33, 40, "left (negatively)"), (25, 25, "not at all — it is symmetric"),
             (120, 100, "right (positively)"), (64, 70, "left (negatively)"),
             (18, 18, "not at all — it is symmetric"), (200, 150, "right (positively)"),
             (45, 52, "left (negatively)"), (81, 81, "not at all — it is symmetric")]
    for i, (mean, med, ans) in enumerate(cases):
        wrongs = [w for w in ("right (positively)", "left (negatively)",
                              "not at all — it is symmetric") if w != ans]
        stmt = ("A distribution has mean $%d$ and median $%d$. Which way is it "
                "skewed?" % (mean, med))
        variants.append(_mk(
            "PS-skew-v%02d" % (i + 1), stmt, ans,
            wrongs + ["it cannot be decided from these two numbers"], i,
            "The mean is dragged toward the long tail while the median stays "
            "put, so mean %s median means the tail lies %s. Here $%d$ %s $%d$."
            % ("above" if mean > med else ("below" if mean < med else "equals"),
               "to the right" if mean > med else
               ("to the left" if mean < med else "on neither side"),
               mean, ">" if mean > med else ("<" if mean < med else "="), med),
            ["%d %s %d" % (mean, ">" if mean > med else
                           ("<" if mean < med else "=="), med)]))
    return _floor("skew-from-mean-and-median", variants)


def _rs_skew_shape(s):
    m = re.search(r"mean \$(\d+)\$ and median \$(\d+)\$", s)
    a, b = int(m.group(1)), int(m.group(2))
    return ("txt", "right" if a > b else ("left" if a < b else "symmetric"))


def _gen_percentile():
    variants = []
    # Chosen by search across the whole percentile range: the percentile, the
    # plain fraction, the raw count and the complement must be four different
    # numbers, and two hand-picked pairs were not.
    data = [(200, 18), (150, 24), (80, 20), (300, 96), (120, 47), (500, 245),
            (60, 34), (250, 155), (400, 272), (90, 67), (180, 144), (1000, 860)]
    for i, (n, below) in enumerate(data):
        pct = Fraction(below * 100, n)
        stmt = ("In a group of $%d$ scores, $%d$ are below yours. Roughly what "
                "percentile are you at?" % (n, below))
        variants.append(_mk(
            "PS-pct-v%02d" % (i + 1), stmt, _fr(pct) + "th",
            [_fr(Fraction(below, n)) + "th", "$%d$th" % below,
             _fr(100 - pct) + "th"], i,
            "A percentile is the PERCENTAGE below you: "
            "$\\frac{%d}{%d} \\times 100 = %s$. Reporting the raw count $%d$ "
            "or the plain fraction leaves out the conversion to a percentage."
            % (below, n, _fr_core(pct), below),
            ["Rational(%d * 100, %d) == Rational(%d, %d)"
             % (below, n, pct.numerator, pct.denominator)]))
    return _floor("percentile-from-counts", variants)


def _rs_percentile(s):
    m = re.search(r"group of \$(\d+)\$ scores, \$(\d+)\$ are below", s)
    n, b = int(m.group(1)), int(m.group(2))
    return ("frac", Fraction(b * 100, n))


def _gen_standard_deviation_shift():
    variants = []
    data = [(12, 5), (20, 8), (7, 3), (15, 6), (30, 10), (9, 4), (25, 7),
            (18, 9), (40, 12), (11, 2), (22, 11), (16, 4)]
    for i, (mean, sd) in enumerate(data):
        stmt = ("Every value in a data set with mean $%d$ and standard "
                "deviation $%d$ has $10$ ADDED to it. What is the new standard "
                "deviation?" % (mean, sd))
        variants.append(_mk(
            "PS-sdsh-v%02d" % (i + 1), stmt, "$%d$" % sd,
            ["$%d$" % (sd + 10), "$%d$" % (mean + 10), "$%d$" % (sd * 10)], i,
            "Adding a constant slides every value the same distance, so the "
            "SPREAD is untouched: the standard deviation stays $%d$. The MEAN "
            "does move, from $%d$ to $%d$ — which is the number most people "
            "adjust by mistake."
            % (sd, mean, mean + 10),
            ["%d == %d" % (sd, sd), "%d + 10 == %d" % (mean, mean + 10)]))
    return _floor("shifting-a-distribution", variants)


def _rs_standard_deviation_shift(s):
    m = re.search(r"standard\s+deviation \$(\d+)\$", s)
    return ("num", int(m.group(1)))


# ---- two-variable-data ---------------------------------------------------
def _gen_correlation_sign():
    variants = []
    cases = [("hours revised", "exam mark", "positive"),
             ("hours of television", "exam mark", "negative"),
             ("shoe size", "exam mark", "close to zero"),
             ("age of a car", "its resale price", "negative"),
             ("height", "arm span", "positive"),
             ("distance from a heater", "temperature felt", "negative"),
             ("rainfall", "umbrella sales", "positive"),
             ("day of the month", "shoe size", "close to zero"),
             ("engine size", "fuel used per kilometre", "positive"),
             ("altitude", "air pressure", "negative"),
             ("number of pages", "reading time", "positive"),
             ("house number", "residents' income", "close to zero")]
    for i, (x, y, ans) in enumerate(cases):
        wrongs = [w for w in ("positive", "negative", "close to zero") if w != ans]
        stmt = ("What correlation would you expect between %s and %s?" % (x, y))
        variants.append(_mk(
            "PS-corr-v%02d" % (i + 1), stmt, ans,
            wrongs + ["exactly $1$"], i,
            "As %s rises, %s tends to %s, which is %s correlation. Note that no "
            "real data set reaches exactly $1$ — that would mean the points sit "
            "on a perfect straight line."
            % (x, y,
               "rise too" if ans == "positive" else
               ("fall" if ans == "negative" else "do neither"), ans),
            ["1 == 1"]))
    return _floor("expected-correlation", variants)


def _rs_correlation_sign(s):
    neg = ["television", "age of a car", "distance from a heater", "altitude"]
    zero = ["shoe size and exam", "day of the month", "house number"]
    if any(k in s for k in zero):
        return ("txt", "zero")
    return ("txt", "negative" if any(k in s for k in neg) else "positive")


def _gen_residual():
    variants = []
    data = [(3, 14, 2, 5), (5, 27, 4, 6), (2, 9, 3, 4), (6, 31, 5, 3),
            (4, 20, 3, 7), (7, 38, 5, 4), (1, 6, 4, 1), (8, 45, 5, 6),
            (3, 17, 6, 2), (9, 50, 5, 8), (2, 13, 7, 1), (10, 62, 6, 5)]
    for i, (x, actual, m, b) in enumerate(data):
        pred = m * x + b
        res = actual - pred
        stmt = ("A fitted line is $y = %dx + %d$. At $x = %d$ the observed value "
                "is $%d$. What is the residual?" % (m, b, x, actual))
        variants.append(_mk(
            "PS-resid-v%02d" % (i + 1), stmt, "$%d$" % res,
            ["$%d$" % (-res), "$%d$" % pred, "$%d$" % actual], i,
            "The residual is OBSERVED minus PREDICTED: the line predicts "
            "$%d \\cdot %d + %d = %d$, so the residual is $%d - %d = %d$. "
            "Subtracting the other way round flips the sign and reverses what "
            "it tells you about the fit."
            % (m, x, b, pred, actual, pred, res),
            ["%d - (%d*%d + %d) == %d" % (actual, m, x, b, res)]))
    return _floor("residuals", variants)


def _rs_residual(s):
    m = re.search(r"y = (\d+)x \+ (\d+)\$. At \$x = (\d+)\$ the observed value "
                  r"is \$(\d+)\$", s)
    a, b, x, act = (int(m.group(i)) for i in (1, 2, 3, 4))
    return ("num", act - (a * x + b))


def _gen_causation():
    variants = []
    cases = [
        ("Ice-cream sales and drowning both rise in summer",
         "a lurking variable — hot weather — drives both"),
        ("Towns with more libraries have more crime",
         "both simply track how big the town is"),
        ("Children with bigger shoes read better",
         "age drives both, so the link is not causal"),
        ("Countries eating more chocolate win more prizes",
         "wealth plausibly drives both"),
        ("People who take vitamins report better health",
         "healthier people may be the ones who choose to take vitamins"),
        ("Houses with more bedrooms sell for more",
         "size plausibly causes the price, so here a causal reading is fair"),
        ("Students who attend more lectures score higher",
         "attendance may cause the score, but motivation could drive both"),
        ("Cities with more firefighters have more fire damage",
         "bigger fires call out more firefighters, so the arrow points the "
         "other way"),
        ("Months with more weddings have more sunshine",
         "people CHOOSE sunny months, so the arrow points the other way"),
        ("Areas with more storks have more babies",
         "rural areas have both, so a lurking variable explains it"),
        ("Older children run faster",
         "age plausibly causes the speed, so a causal reading is fair"),
        ("Employees with larger offices earn more",
         "seniority plausibly drives both"),
    ]
    for i, (obs, why) in enumerate(cases):
        stmt = ("%s. What is the safest conclusion?" % obs)
        variants.append(_mk(
            "PS-caus-v%02d" % (i + 1), stmt,
            "correlation is not proof of cause here — %s" % why,
            ["the first definitely causes the second",
             "the second definitely causes the first",
             "the two are unrelated"], i,
            "An observed association can arise from a lurking variable, from "
            "the causal arrow pointing the other way, or from chance. Here, "
            "%s — so a causal claim is not safe on this evidence alone." % why,
            ["1 == 1"]))
    return _floor("correlation-and-causation", variants)


def _rs_causation(s):
    return ("txt", "not causal")


# ---- inference-and-studies -----------------------------------------------
def _gen_sampling_method():
    variants = []
    cases = [
        ("Numbering everyone and picking with a random number table",
         "simple random sampling"),
        ("Taking every $10$th name on an alphabetical list",
         "systematic sampling"),
        ("Splitting by year group and sampling randomly within each",
         "stratified sampling"),
        ("Picking a few whole classes at random and surveying everyone in them",
         "cluster sampling"),
        ("Asking whoever happens to walk past the school gate",
         "convenience sampling"),
        ("Drawing names from a hat", "simple random sampling"),
        ("Choosing every $5$th house along a street", "systematic sampling"),
        ("Sampling separately from urban and rural households in proportion",
         "stratified sampling"),
        ("Selecting three villages at random and surveying every household",
         "cluster sampling"),
        ("Posting an online poll and using whoever replies",
         "convenience sampling"),
        ("Assigning each pupil a number and using a computer's random picks",
         "simple random sampling"),
        ("Dividing by gender and sampling each group in proportion",
         "stratified sampling"),
    ]
    kinds = ["simple random sampling", "systematic sampling",
             "stratified sampling", "cluster sampling", "convenience sampling"]
    for i, (desc, ans) in enumerate(cases):
        wrongs = [k for k in kinds if k != ans][:3]
        variants.append(_mk(
            "PS-samp-v%02d" % (i + 1),
            "Which sampling method is this? %s." % desc, ans, wrongs, i,
            "%s. Stratified sampling splits into groups and samples WITHIN "
            "each; cluster sampling picks whole groups and takes everyone in "
            "them — that is the pair most often confused." % ans.capitalize(),
            ["1 == 1"]))
    return _floor("sampling-methods", variants)


def _rs_sampling_method(s):
    if "every $" in s:
        return ("txt", "systematic")
    if "Splitting by" in s or "separately from" in s or "Dividing by" in s:
        return ("txt", "stratified")
    if "whole classes" in s or "three villages" in s:
        return ("txt", "cluster")
    if "walk past" in s or "whoever replies" in s:
        return ("txt", "convenience")
    return ("txt", "simple random")


def _gen_bias_source():
    variants = []
    cases = [
        ("A survey on library use is conducted inside the library",
         "the sample over-represents people who already use libraries"),
        ("A poll about phone habits is run by text message",
         "people without phones cannot answer at all"),
        ("Only those who feel strongly bother to return the questionnaire",
         "response bias: strong opinions are over-represented"),
        ("Every question begins with the phrase 'Don't you agree that'",
         "the wording leads the respondent toward one answer"),
        ("A health study samples only volunteers from a gym",
         "the sample is fitter than the population it claims to describe"),
        ("A survey on internet speed is conducted online",
         "people with poor connections are least able to respond"),
        ("Interviewers ask about income face to face",
         "respondents may under-report to a stranger"),
        ("A school samples only pupils present on the day",
         "frequent absentees are systematically excluded"),
        ("A shop surveys customers about its own service",
         "dissatisfied people have already stopped coming"),
        ("A study of commuting asks only weekday morning travellers",
         "shift and weekend workers are left out"),
        ("The only answers offered are 'good' and 'excellent'",
         "the scale has no way to record a negative view"),
        ("A charity asks donors whether charity work matters",
         "the group asked is not representative of anyone else"),
    ]
    for i, (desc, why) in enumerate(cases):
        stmt = "What is the main problem with this study? %s." % desc
        variants.append(_mk(
            "PS-bias-v%02d" % (i + 1), stmt, why,
            ["the sample is too small to say anything",
             "the results should be reported as percentages",
             "nothing — the method is sound"], i,
            "The flaw is structural rather than a matter of size: %s. Adding "
            "more people would not fix it, because every extra person is drawn "
            "from the same skewed pool." % why,
            ["1 == 1"]))
    return _floor("sources-of-bias", variants)


def _rs_bias_source(s):
    return ("txt", "biased sample")


def _gen_margin_of_error():
    variants = []
    data = [(50, 4), (52, 3), (46, 5), (61, 2), (38, 6), (55, 4), (43, 3),
            (67, 5), (29, 4), (72, 3), (58, 6), (35, 2)]
    for i, (pct, moe) in enumerate(data):
        lo, hi = pct - moe, pct + moe
        stmt = ("A poll reports $%d\\%%$ support with a margin of error of "
                "$%d$ percentage points. What is the plausible range?"
                % (pct, moe))
        variants.append(_mk(
            "PS-moe-v%02d" % (i + 1), stmt,
            "$%d\\%%$ to $%d\\%%$" % (lo, hi),
            ["$%d\\%%$ to $%d\\%%$" % (pct, hi),
             "$%d\\%%$ to $%d\\%%$" % (lo, pct),
             "$%d\\%%$ to $%d\\%%$" % (pct - 2 * moe, pct + 2 * moe)], i,
            "The margin of error extends BOTH ways from the reported figure: "
            "$%d \\pm %d$ gives $%d\\%%$ to $%d\\%%$. A one-sided range would "
            "claim the poll can only be wrong in one direction."
            % (pct, moe, lo, hi),
            ["%d - %d == %d" % (pct, moe, lo), "%d + %d == %d" % (pct, moe, hi)]))
    return _floor("margin-of-error", variants)


def _rs_margin_of_error(s):
    m = re.search(r"\$(\d+)\\%\$ support with a margin of error of \$(\d+)\$", s)
    p_, e = int(m.group(1)), int(m.group(2))
    return ("txt", "%d to %d" % (p_ - e, p_ + e))

# Round two: the forms that take every unit from two or three collections
# to six.
_FORMS_META += [
    ("complementary-counting", "Complementary counting", 2,
     "counting-principles",
     "Count the opposite and subtract — it beats counting overlaps.",
     _gen_complement_count, _rs_complement_count),
    ("strings-with-repeats", "Strings with repeats", 1,
     "counting-principles",
     "Every position keeps the full alphabet when repeats are allowed.",
     _gen_digit_strings, _rs_digit_strings),
    ("multi-stage-journeys", "Multi-stage journeys", 1,
     "counting-principles",
     "Each leg multiplies; adding counts single roads.",
     _gen_tree_paths, _rs_tree_paths),
    ("restricted-arrangements", "Arrangements with a fixed block", 3,
     "counting-principles",
     "Only the unfixed people can be rearranged.",
     _gen_restricted_seat, _rs_restricted_seat),
    ("circular-arrangements", "Round-table arrangements", 3,
     "permutations",
     "Fix one seat to kill the rotations: (n-1)!.",
     _gen_circular, _rs_circular),
    ("arrangements-with-repeats", "Arranging repeated letters", 3,
     "permutations",
     "Divide by a factorial for each repeated letter.",
     _gen_repeated_letters, _rs_repeated_letters),
    ("ordered-selections", "Distinct posts", 2,
     "permutations",
     "Different posts mean order matters — that is a permutation.",
     _gen_perm_vs_total, _rs_perm_vs_total),
    ("permutation-formula", "The nPr formula", 1,
     "permutations",
     "n! divided by (n-k)! — and no k! as well.",
     _gen_perm_formula, _rs_perm_formula),
    ("combination-symmetry", "The symmetry of nCk", 2,
     "combinations",
     "Choosing what to keep is choosing what to leave out.",
     _gen_comb_identity, _rs_comb_identity),
    ("handshakes", "Counting pairs", 1,
     "combinations",
     "Every handshake is a pair, so halve the ordered count.",
     _gen_handshakes, _rs_handshakes),
    ("at-least-one", "At least one from a group", 3,
     "combinations",
     "Count all, subtract the ones with none — picking first double-counts.",
     _gen_comb_at_least, _rs_comb_at_least),
    ("pascal-row-sum", "Row sums of Pascal's triangle", 2,
     "binomial-theorem",
     "Row n adds to 2^n — every subset of n things.",
     _gen_pascal_row_sum, _rs_pascal_row_sum),
    ("binomial-general-term", "A named term's coefficient", 3,
     "binomial-theorem",
     "The binomial coefficient AND the constant's power.",
     _gen_binom_general_term, _rs_binom_general_term),
    ("pascal-entry", "Entries of Pascal's triangle", 1,
     "binomial-theorem",
     "Pascal's entries are the combinations themselves.",
     _gen_pascal_entry, _rs_pascal_entry),
    ("binomial-constant-term", "The constant term", 2,
     "binomial-theorem",
     "No x at all, so every factor gives its constant.",
     _gen_binom_constant, _rs_binom_constant),
    ("mutually-exclusive-or", "Mutually exclusive OR", 1,
     "probability-models",
     "One draw cannot be both, so the probabilities add.",
     _gen_prob_or_disjoint, _rs_prob_or_disjoint),
    ("without-replacement", "Two draws without replacement", 3,
     "probability-models",
     "The second draw comes from a smaller bag.",
     _gen_prob_two_draws, _rs_prob_two_draws),
    ("at-least-one-probability", "At least one, by the complement", 3,
     "probability-models",
     "1 minus the probability of missing every time.",
     _gen_prob_at_least_one, _rs_prob_at_least_one),
    ("odds-to-probability", "Odds into probability", 2,
     "probability-models",
     "Odds a to b means a out of a + b.",
     _gen_prob_odds, _rs_prob_odds),
    ("tree-multiplication", "Multiplying along a tree", 1,
     "conditional-probability",
     "Follow one path and multiply the branches.",
     _gen_cond_tree, _rs_cond_tree),
    ("conditional-from-a-table", "Conditioning on a row", 2,
     "conditional-probability",
     "The condition shrinks the population you divide by.",
     _gen_cond_table, _rs_cond_table),
    ("independence-test", "Testing independence", 3,
     "conditional-probability",
     "P(A and B) = P(A)P(B), or they are dependent.",
     _gen_independence_test, _rs_independence_test),
    ("reverse-conditioning", "Conditioning the other way", 3,
     "conditional-probability",
     "P(A given B) and P(B given A) are different numbers.",
     _gen_cond_reverse, _rs_cond_reverse),
    ("expected-gain", "Expected gain per play", 2,
     "random-variables",
     "Expected winnings minus the cost that is paid every time.",
     _gen_ev_fair_game, _rs_ev_fair_game),
    ("variance-two-point", "Variance of a two-point variable", 3,
     "random-variables",
     "Variance averages the SQUARED distance from the mean.",
     _gen_ev_variance, _rs_ev_variance),
    ("linearity-of-expectation", "Linearity of expectation", 1,
     "random-variables",
     "Both the multiplier and the shift carry through.",
     _gen_ev_linear, _rs_ev_linear),
    ("expected-value-from-a-distribution", "Expected value from a table", 2,
     "random-variables",
     "Weight each value by its probability.",
     _gen_ev_distribution, _rs_ev_distribution),
    ("binomial-mean", "The binomial mean", 1,
     "binomial-distribution",
     "np — not np(1-p), which is the variance.",
     _gen_binom_mean, _rs_binom_mean),
    ("binomial-at-most-one", "At most one success", 3,
     "binomial-distribution",
     "Zero successes OR exactly one — both qualify.",
     _gen_binom_at_most_one, _rs_binom_at_most_one),
    ("binomial-conditions", "Is it binomial?", 1,
     "binomial-distribution",
     "Fixed trials, two outcomes, constant p, independence.",
     _gen_binom_conditions, _rs_binom_conditions),
    ("binomial-variance", "The binomial variance", 2,
     "binomial-distribution",
     "np(1-p) — the mean is np, a different number.",
     _gen_binom_variance, _rs_binom_variance),
    ("range-against-mode", "Range against mode", 1,
     "describing-data",
     "Range measures spread, mode measures frequency.",
     _gen_mode_and_range, _rs_mode_and_range),
    ("weighted-mean", "Weighted means", 2,
     "describing-data",
     "Divide by the total weight, not by the count.",
     _gen_weighted_mean, _rs_weighted_mean),
    ("outlier-effect-on-mean", "How far one value moves the mean", 3,
     "describing-data",
     "A new value is shared across everyone.",
     _gen_outlier_effect, _rs_outlier_effect),
    ("median-even-count", "Median of an even count", 1,
     "describing-data",
     "Average the middle two — neither one alone.",
     _gen_median_even, _rs_median_even),
    ("skew-from-mean-and-median", "Reading skew", 2,
     "distributions-and-position",
     "The mean is dragged toward the long tail.",
     _gen_skew_shape, _rs_skew_shape),
    ("percentile-from-counts", "Percentiles", 1,
     "distributions-and-position",
     "The PERCENTAGE below you, not the count.",
     _gen_percentile, _rs_percentile),
    ("shifting-a-distribution", "Shifting every value", 3,
     "distributions-and-position",
     "Adding a constant moves the centre and leaves the spread.",
     _gen_standard_deviation_shift, _rs_standard_deviation_shift),
    ("expected-correlation", "Expecting a correlation", 1,
     "two-variable-data",
     "Which way does one variable move as the other rises?",
     _gen_correlation_sign, _rs_correlation_sign),
    ("residuals", "Residuals", 2,
     "two-variable-data",
     "Observed minus predicted — the order fixes the sign.",
     _gen_residual, _rs_residual),
    ("correlation-and-causation", "Correlation against cause", 3,
     "two-variable-data",
     "A lurking variable or a reversed arrow explains most links.",
     _gen_causation, _rs_causation),
    ("sampling-methods", "Naming a sampling method", 1,
     "inference-and-studies",
     "Stratified samples within groups; cluster takes whole groups.",
     _gen_sampling_method, _rs_sampling_method),
    ("sources-of-bias", "Spotting bias", 2,
     "inference-and-studies",
     "A structural flaw does not shrink with a bigger sample.",
     _gen_bias_source, _rs_bias_source),
    ("margin-of-error", "Margin of error", 3,
     "inference-and-studies",
     "The margin extends BOTH ways from the reported figure.",
     _gen_margin_of_error, _rs_margin_of_error),
]



def _gen_interpret_slope():
    variants = []
    data = [("kilometres driven", "litres of fuel used", 7, 3),
            ("years of experience", "salary in thousands", 4, 22),
            ("minutes studied", "marks scored", 2, 15),
            ("kilograms of feed", "kilograms gained", 3, 5),
            ("hours worked", "items produced", 12, 8),
            ("metres of fabric", "cost in thousands", 6, 4),
            ("days of growth", "centimetres tall", 5, 10),
            ("pages written", "hours spent", 1, 2),
            ("bags of fertiliser", "sacks harvested", 9, 14),
            ("kilometres walked", "calories burned", 60, 25),
            ("weeks of training", "seconds off a time", 2, 40),
            ("litres of paint", "square metres covered", 11, 6)]
    for i, (x, y, m, b) in enumerate(data):
        stmt = ("A fitted line is $y = %dx + %d$, where $x$ is %s and $y$ is "
                "%s. What does the $%d$ tell you?" % (m, b, x, y, m))
        variants.append(_mk(
            "PS-slope-v%02d" % (i + 1), stmt,
            "each extra unit of %s adds about $%d$ to %s" % (x, m, y),
            ["the value of %s when %s is zero" % (y, x),
             "the total %s across the whole data set" % y,
             "how well the line fits the points"], i,
            "The slope is a RATE OF CHANGE: one more unit of %s is associated "
            "with about $%d$ more of %s. The intercept $%d$ is the value when "
            "%s is zero, and the fit is measured separately."
            % (x, m, y, b, x),
            ["%d*1 + %d - (%d*0 + %d) == %d" % (m, b, m, b, m)]))
    return _floor("interpreting-slope", variants)


def _rs_interpret_slope(s):
    return ("txt", "rate of change")


def _gen_population_sample():
    """Population, sample, parameter or statistic — which is which.

    Deliberately NOT another "what kind of study is this?": that form already
    exists in this unit, and a second copy would have shipped the same twelve
    questions under a new name."""
    variants = []
    cases = [
        ("all $40\\,000$ voters in a district", "the population",
         "the entire group the conclusion is about"),
        ("the $800$ voters actually telephoned", "the sample",
         "the part of the population that was measured"),
        ("the true percentage of all voters who support the plan",
         "a parameter", "a number describing the whole population"),
        ("the percentage of the $800$ called who supported it", "a statistic",
         "a number computed from the sample"),
        ("every tree in the forest", "the population",
         "the entire group under study"),
        ("the $50$ trees measured", "the sample", "the measured part"),
        ("the mean height of ALL the trees", "a parameter",
         "a summary of the whole population"),
        ("the mean height of the $50$ measured", "a statistic",
         "a summary of the sample"),
        ("all pupils in the country", "the population",
         "the whole group the claim covers"),
        ("the $2\\,000$ pupils surveyed", "the sample",
         "the group actually asked"),
        ("the true national pass rate", "a parameter",
         "a fixed number about the whole population"),
        ("the pass rate among those surveyed", "a statistic",
         "a number that changes from sample to sample"),
    ]
    kinds = ["the population", "the sample", "a parameter", "a statistic"]
    for i, (desc, ans, why) in enumerate(cases):
        wrongs = [k for k in kinds if k != ans]
        variants.append(_mk(
            "PS-popsam-v%02d" % (i + 1),
            "In a study, what is %s?" % desc, ans, wrongs, i,
            "This is %s — %s. The pair worth keeping straight is parameter "
            "against statistic: a parameter is a fixed fact about the whole "
            "population, while a statistic is computed from a sample and "
            "changes if you sample again." % (ans, why),
            ["1 == 1"]))
    return _floor("population-and-sample", variants)


def _rs_population_sample(s):
    if "true " in s or "ALL the" in s:
        return ("txt", "parameter")
    if "all " in s or "every " in s:
        return ("txt", "population")
    if "among those" in s or "of the $" in s and "measured" in s:
        return ("txt", "statistic")
    return ("txt", "sample")


_FORMS_META += [
    ("interpreting-slope", "What the slope means", 3,
     "two-variable-data",
     "The slope is a rate of change; the intercept is the starting value.",
     _gen_interpret_slope, _rs_interpret_slope),
    ("population-and-sample", "Population, sample, parameter, statistic", 3,
     "inference-and-studies",
     "A parameter describes the population; a statistic comes from a sample.",
     _gen_population_sample, _rs_population_sample),
]


# The self-check runs last on purpose: the round-two forms are appended to
# _FORMS_META below the original table, and a check placed above them would
# report the old count and call the module complete.
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
