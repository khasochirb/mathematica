# -*- coding: utf-8 -*-
"""Problem-bank subject: Precalculus — mirrors the /math/precalculus course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/precalculus.py` to
self-check.
"""
import math
import re

from fractions import Fraction

import sympy as _sp
from sympy import Rational, sympify

SLUG = "precalculus"
TITLE = "Precalculus"
TITLE_MN = "Прекалькулюс"
BLURB = ("Unit-by-unit practice for the Precalculus course — functions and transformations through conics.")

UNITS = [
    {"id": "functions-and-their-graphs", "title": "Functions & Their Graphs",
     "blurb": "Domain, range, and graph features; composition; inverse functions; even/odd symmetry."},
    {"id": "transformations-of-graphs", "title": "Transformations of Graphs",
     "blurb": "Shifts, stretches, reflections, the combined form a·f(x−h)+k, and piecewise graphs."},
    {"id": "polynomial-functions", "title": "Polynomial Functions",
     "blurb": "End behavior, zeros and the Factor Theorem, multiplicity, division and the Remainder Theorem."},
    {"id": "rational-functions", "title": "Rational Functions",
     "blurb": "Vertical asymptotes, holes, horizontal and slant asymptotes, and complete graphs."},
    {"id": "exponentials-and-logarithms", "title": "Exponentials & Logarithms",
     "blurb": "Growth and decay, compound interest and e, logs as inverses, and exponential/log equations."},
    {"id": "the-unit-circle", "title": "The Unit Circle",
     "blurb": "Radians, sine and cosine as coordinates, special angles, and reference angles in all quadrants."},
    {"id": "trigonometric-graphs-and-equations", "title": "Trig Graphs & Equations",
     "blurb": "The sine wave, amplitude/period/shifts, fundamental identities, and solving trig equations."},
    {"id": "conic-sections", "title": "Conic Sections",
     "blurb": "Circles, ellipses, parabolas with foci, hyperbolas, and classifying second-degree equations."},
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


def _floor12(name, variants):
    """Target is 12 variants per form; two-form units need 12 + 12 >= 24."""
    assert len(variants) == 12, "%s: %d variants (want 12)" % (name, len(variants))
    return variants


def _pm(c):
    """Signed suffix term ' + 5' / ' - 5' (never '+ -5')."""
    return " + %d" % c if c >= 0 else " - %d" % (-c)


def _xpm(c):
    """Render 'x + c' with a clean sign; c == 0 -> 'x'."""
    return "x" if c == 0 else "x%s" % _pm(c)


def _fr_core(fr):
    """Exact rational -> KaTeX body (integer, or \\frac with leading minus)."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return "%d" % fr.numerator
    if fr < 0:
        return "-\\frac{%d}{%d}" % (-fr.numerator, fr.denominator)
    return "\\frac{%d}{%d}" % (fr.numerator, fr.denominator)


def _fr_tex(fr):
    return "$%s$" % _fr_core(fr)


# Exact unit-circle values keyed by (num, den) of sin/cos: latex body + sympy str.
_TRIG_TEX = {
    "0": "0", "1": "1", "-1": "-1",
    "1/2": "\\frac{1}{2}", "-1/2": "-\\frac{1}{2}",
    "sqrt(2)/2": "\\frac{\\sqrt{2}}{2}", "-sqrt(2)/2": "-\\frac{\\sqrt{2}}{2}",
    "sqrt(3)/2": "\\frac{\\sqrt{3}}{2}", "-sqrt(3)/2": "-\\frac{\\sqrt{3}}{2}",
}


def _trig_key(v):
    """Exact sympy value (0, ±1, ±1/2, ±√2/2, ±√3/2) -> key into _TRIG_TEX."""
    for k in _TRIG_TEX:
        if _sp.sympify(k) == v:
            return k
    raise ValueError("not a special value: %r" % v)


def _pi_frac_tex(p, q):
    """KaTeX body for p*pi/q (p >= 1, q >= 2)."""
    num = "\\pi" if p == 1 else "%d\\pi" % p
    return "\\dfrac{%s}{%d}" % (num, q)


# -------------------------------------------------------------------------
# Form 1: evaluate-composite (functions-and-their-graphs, level 1)
# -------------------------------------------------------------------------
def _gen_evaluate_composite():
    cands = [(2, 3, 1, 2), (3, 1, 2, 1), (2, 5, 3, -1), (4, 1, 2, 2),
             (3, 2, 4, -2), (2, 1, 5, 3), (5, 2, 1, 1), (3, 4, 2, -1),
             (2, 7, 3, 2), (4, 3, 1, -2), (5, 1, 4, 1), (2, 2, 6, 3),
             (3, 5, 2, 2), (4, 2, 3, -1), (2, 4, 1, -3), (5, 3, 2, -2)]
    variants, seen = [], []
    i = 0
    for ci_, (a, b, c, k) in enumerate(cands):
        if len(variants) >= 12:
            break
        order = "fg" if len(variants) % 2 == 0 else "gf"
        fk = a * k + b
        gk = k * k + c
        if order == "fg":
            correct, other = a * gk + b, fk * fk + c
            call = "f(g(%d))" % k
        else:
            correct, other = fk * fk + c, a * gk + b
            call = "g(f(%d))" % k
        dvals = [other, fk * gk, fk + gk]
        if not _distinct([correct] + dvals):
            continue
        stmt = ("If $f(x) = %dx%s$ and $g(x) = x^2%s$, find $%s$."
                % (a, _pm(b), _pm(c), call))
        if stmt in seen:
            continue
        seen.append(stmt)
        if order == "fg":
            expl = ("Work inside out: $g(%d) = %d$, then $f(%d) = %d$. "
                    "Composing in the wrong order, $g(f(%d))$, gives $%d$."
                    % (k, gk, gk, correct, k, other))
            checks = ["(%d)*((%d)**2 + (%d)) + (%d) == %d"
                      % (a, k, c, b, correct)]
        else:
            expl = ("Work inside out: $f(%d) = %d$, then $g(%d) = %d$. "
                    "Composing in the wrong order, $f(g(%d))$, gives $%d$."
                    % (k, fk, fk, correct, k, other))
            checks = ["((%d)*(%d) + (%d))**2 + (%d) == %d"
                      % (a, k, b, c, correct)]
        variants.append(_mk(
            "PC-comp-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % correct, ["$%d$" % v for v in dvals], i, expl, checks))
        i += 1
    return _floor12("evaluate-composite", variants)


def _rs_evaluate_composite(s):
    m = re.search(r"f\(x\) = (\d+)x ([+-]) (\d+)", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    m = re.search(r"g\(x\) = x\^2 ([+-]) (\d+)", s)
    c = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
    m = re.search(r"\$(f|g)\((f|g)\((-?\d+)\)\)\$", s)
    outer, k = m.group(1), int(m.group(3))
    f = lambda x: a * x + b          # noqa: E731
    g = lambda x: x * x + c          # noqa: E731
    return ("num", f(g(k)) if outer == "f" else g(f(k)))


# -------------------------------------------------------------------------
# Form 2: domain-combined (functions-and-their-graphs, level 2)
# -------------------------------------------------------------------------
def _gen_domain_combined():
    pairs = [(1, 4), (2, 5), (3, 7), (2, 6), (1, 5), (4, 9),
             (3, 8), (5, 9), (2, 7), (1, 6), (4, 8), (3, 6)]
    variants = []
    for i, (a, b) in enumerate(pairs):
        assert b > a
        stmt = ("What is the domain of "
                "$f(x) = \\dfrac{\\sqrt{x - %d}}{x - %d}$?" % (a, b))
        correct = "$x \\ge %d,\\ x \\neq %d$" % (a, b)
        dis = ["$x \\ge %d$" % a,
               "$x > %d,\\ x \\neq %d$" % (a, b),
               "$x \\neq %d$" % b]
        variants.append(_mk(
            "PC-dom-v%02d" % (i + 1), stmt, correct, dis, i,
            "The square root needs $x - %d \\ge 0$ and the denominator "
            "forbids $x = %d$, so $x \\ge %d$ with $x \\neq %d$. Dropping "
            "the denominator condition — the classic slip — keeps the "
            "forbidden point $x = %d$." % (a, b, a, b, b),
            ["sqrt((%d) - (%d)) == 0" % (a, a),
             "(%d) > (%d)" % (b, a)]))
    return _floor12("domain-combined", variants)


def _rs_domain_combined(s):
    m = re.search(r"\\sqrt\{x - (\d+)\}\}\{x - (\d+)\}", s)
    a, b = int(m.group(1)), int(m.group(2))
    return ("opt", "$x \\ge %d,\\ x \\neq %d$" % (a, b))


# -------------------------------------------------------------------------
# Form 3: average-rate (functions-and-their-graphs, level 2)
# -------------------------------------------------------------------------
def _gen_average_rate():
    cands = [(3, 1, 4), (-2, 2, 5), (5, 1, 3), (1, 2, 6), (-4, 3, 5),
             (2, 1, 5), (-1, 2, 4), (4, 3, 7), (-3, 1, 6), (6, 2, 7),
             (-5, 4, 6), (7, 3, 8)]
    variants = []
    for i, (c, p, q) in enumerate(cands):
        assert p < q
        ans = p + q
        dvals = [q * q - p * p, q - p, p * q]
        assert _distinct([ans] + dvals), (c, p, q)
        stmt = ("For $f(x) = x^2%s$, find the average rate of change of $f$ "
                "from $x = %d$ to $x = %d$." % (_pm(c), p, q))
        variants.append(_mk(
            "PC-avg-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "The average rate is $\\frac{f(%d) - f(%d)}{%d - %d} = "
            "\\frac{%d}{%d} = %d$. Stopping at $f(%d) - f(%d) = %d$ — "
            "forgetting to divide by the run — is the classic slip."
            % (q, p, q, p, (q - p) * ans, q - p, ans, q, p, q * q - p * p),
            ["(((%d)**2 + (%d)) - ((%d)**2 + (%d)))/((%d) - (%d)) == %d"
             % (q, c, p, c, q, p, ans),
             "(%d) + (%d) == %d" % (p, q, ans)]))
    return _floor12("average-rate", variants)


def _rs_average_rate(s):
    m = re.search(r"x\^2 ([+-]) (\d+)\$", s)
    c = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
    m = re.search(r"from \$x = (-?\d+)\$ to \$x = (-?\d+)\$", s)
    p, q = int(m.group(1)), int(m.group(2))
    return ("num", Rational(((q * q + c) - (p * p + c)), (q - p)))


# -------------------------------------------------------------------------
# Form 4: describe-transform (transformations-of-graphs, level 1)
# -------------------------------------------------------------------------
def _gen_describe_transform():
    shifts = [(3, 2), (-4, 5), (2, -6), (-1, -3), (5, 4),
              (-2, 7), (4, -1), (-6, -2), (7, 1), (-5, -4)]
    variants = []
    i = 0
    for (h, k) in shifts:
        hw = "right" if h > 0 else "left"
        kw = "up" if k > 0 else "down"
        ah, ak = abs(h), abs(k)
        word = lambda hw_, kw_: ("Shifted %s $%d$ and %s $%d$"  # noqa: E731
                                 % (hw_, ah, kw_, ak))
        correct = word(hw, kw)
        dis = [word("left" if h > 0 else "right", kw),
               word(hw, "down" if k > 0 else "up"),
               word("left" if h > 0 else "right", "down" if k > 0 else "up")]
        stmt = ("How is the graph of $y = f(%s)%s$ obtained from the graph "
                "of $y = f(x)$?" % (_xpm(-h), _pm(k)))
        variants.append(_mk(
            "PC-desc-v%02d" % (len(variants) + 1), stmt, correct, dis, i,
            "Inside the parentheses, $x %s %d$ moves the graph %s $%d$ "
            "(opposite the visible sign); the $%s %d$ outside moves it "
            "%s $%d$. Reading the inner sign literally — %s $%d$ — is the "
            "classic trap."
            % ("-" if h > 0 else "+", ah, hw, ah,
               "+" if k > 0 else "-", ak, kw, ak,
               "left" if h > 0 else "right", ah),
            ["(%d) %s 0" % (h, ">" if h > 0 else "<"),
             "(%d) %s 0" % (k, ">" if k > 0 else "<")]))
        i += 1
    # Reflection pair
    variants.append(_mk(
        "PC-desc-v%02d" % (len(variants) + 1),
        "How is the graph of $y = -f(x)$ obtained from the graph of "
        "$y = f(x)$?",
        "Reflected across the x-axis",
        ["Reflected across the y-axis", "Rotated $180°$ about the origin",
         "Shifted down $1$"], i,
        "The minus sign acts on the output, flipping every $y$-value: a "
        "reflection across the x-axis. Flipping across the y-axis instead "
        "would be $y = f(-x)$ — the sign acting on the input.",
        ["-(x**2) == -x**2"]))
    i += 1
    variants.append(_mk(
        "PC-desc-v%02d" % (len(variants) + 1),
        "How is the graph of $y = f(-x)$ obtained from the graph of "
        "$y = f(x)$?",
        "Reflected across the y-axis",
        ["Reflected across the x-axis", "Rotated $180°$ about the origin",
         "Shifted left $1$"], i,
        "The minus sign acts on the input, flipping every $x$-value: a "
        "reflection across the y-axis. Flipping across the x-axis instead "
        "would be $y = -f(x)$ — the sign acting on the output.",
        ["(-x)**2 == x**2"]))
    return _floor12("describe-transform", variants)


def _rs_describe_transform(s):
    if "-f(x)" in s:
        return ("opt", "Reflected across the x-axis")
    if "f(-x)" in s:
        return ("opt", "Reflected across the y-axis")
    m = re.search(r"y = f\(x ([+-]) (\d+)\) ([+-]) (\d+)\$", s)
    h = int(m.group(2)) * (-1 if m.group(1) == "+" else 1)
    k = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
    return ("opt", "Shifted %s $%d$ and %s $%d$"
            % ("right" if h > 0 else "left", abs(h),
               "up" if k > 0 else "down", abs(k)))


# -------------------------------------------------------------------------
# Form 5: transformed-point (transformations-of-graphs, level 2)
# -------------------------------------------------------------------------
def _gen_transformed_point():
    cands = [(1, 6, 2, 3), (2, 4, 2, -3), (3, -6, 3, 2), (-2, 8, 4, 1),
             (0, 6, 3, 4), (4, -4, 2, 5), (-1, 9, 3, -2), (2, 10, 5, 2),
             (-3, 6, 2, -4), (5, -8, 4, 3), (1, -10, 5, -1), (-4, 12, 3, 5)]
    variants = []
    for i, (p, q, a, h) in enumerate(cands):
        assert a >= 2 and h != 0 and q % a == 0 and q != 0
        correct = (p + h, a * q)
        dis = [(p - h, a * q), (p + h, q // a), (a * p, q + h)]
        assert _distinct([correct] + dis), (p, q, a, h)
        stmt = ("The point $(%d; %d)$ lies on the graph of $y = f(x)$. "
                "Which point must lie on the graph of $y = %df(%s)$?"
                % (p, q, a, _xpm(-h)))
        variants.append(_mk(
            "PC-tpt-v%02d" % (i + 1), stmt,
            "$(%d; %d)$" % correct, ["$(%d; %d)$" % d for d in dis], i,
            "The inside $%s$ shifts $x$ by $%+d$ and the outside factor "
            "$%d$ stretches $y$, so $(%d; %d) \\to (%d; %d)$. Shifting the "
            "wrong way gives $(%d; %d)$ — the classic inner-sign slip."
            % (_xpm(-h), h, a, p, q, p + h, a * q, p - h, a * q),
            ["(%d) + (%d) == %d" % (p, h, p + h),
             "(%d)*(%d) == %d" % (a, q, a * q)]))
    return _floor12("transformed-point", variants)


def _rs_transformed_point(s):
    m = re.search(r"point \$\((-?\d+); (-?\d+)\)\$", s)
    p, q = int(m.group(1)), int(m.group(2))
    m = re.search(r"y = (\d+)f\(x ([+-]) (\d+)\)\$", s)
    a = int(m.group(1))
    h = int(m.group(3)) * (-1 if m.group(2) == "+" else 1)
    return ("opt", "$(%d; %d)$" % (p + h, a * q))


# -------------------------------------------------------------------------
# Form 6: polynomial-division (polynomial-functions, level 3)
# -------------------------------------------------------------------------
def _ctm(coef, var):
    """Signed term like ' + 3x^2', ' - x', ' + 5' (coef != 0, no '1x')."""
    sign = "+" if coef > 0 else "-"
    m = abs(coef)
    body = str(m) if not var else (var if m == 1 else "%d%s" % (m, var))
    return " %s %s" % (sign, body)


def _gen_polynomial_division():
    # At least one coefficient >= 10 (distinct territory from Algebra 2's form).
    cands = [(2, 12, 15, 2), (-3, 14, -10, 1), (5, -11, 20, -2),
             (1, 10, -12, 3), (-2, 13, 18, -1), (4, -15, 11, 2),
             (6, 12, -14, -3), (-4, 16, 10, 1), (3, -13, 25, -2),
             (2, 11, -16, 4), (-5, 18, 12, -1), (7, -12, 30, 2),
             (3, 15, -20, -4), (-6, 20, 14, 3)]
    variants = []
    i = 0
    for (a, b, c, k) in cands:
        if len(variants) >= 12:
            break
        p = lambda t: t ** 3 + a * t * t + b * t + c   # noqa: E731
        r = p(k)
        qconst = b + k * (a + k)     # constant term of the quotient
        dvals = [p(-k), c, qconst]
        if not _distinct([r] + dvals):
            continue
        cubic = "x^3" + _ctm(a, "x^2") + _ctm(b, "x") + _ctm(c, "")
        div = "(x - %d)" % k if k >= 0 else "(x + %d)" % (-k)
        stmt = ("Divide $%s$ by $%s$. What is the remainder?" % (cubic, div))
        # verify the quotient-constant distractor with sympy division
        x = _sp.Symbol("x")
        quo, rem = _sp.div(x**3 + a * x**2 + b * x + c, x - k, x)
        assert rem == r and quo.coeff(x, 0) == qconst
        variants.append(_mk(
            "PC-div-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % r, ["$%d$" % v for v in dvals], i,
            "By the Remainder Theorem the remainder is $p(%d) = %d$ — no "
            "long division needed. Evaluating at $x = %d$ (misreading the "
            "divisor's sign) gives $%d$." % (k, r, -k, p(-k)),
            ["rem(x**3 + (%d)*x**2 + (%d)*x + (%d), x - (%d), x) == %d"
             % (a, b, c, k, r),
             "(%d)**3 + (%d)*(%d)**2 + (%d)*(%d) + (%d) == %d"
             % (k, a, k, b, k, c, r)]))
        i += 1
    return _floor12("polynomial-division", variants)


def _rs_polynomial_division(s):
    m = re.search(
        r"\$x\^3 ([+-]) (\d*)x\^2 ([+-]) (\d*)x ([+-]) (\d+)\$ by "
        r"\$\(x ([+-]) (\d+)\)\$", s)

    def coef(sign, digits):
        v = int(digits) if digits else 1
        return v if sign == "+" else -v

    a = coef(m.group(1), m.group(2))
    b = coef(m.group(3), m.group(4))
    c = coef(m.group(5), m.group(6))
    k = int(m.group(8)) * (-1 if m.group(7) == "+" else 1)
    return ("num", k ** 3 + a * k * k + b * k + c)


# -------------------------------------------------------------------------
# Form 7: build-from-zeros (polynomial-functions, level 2)
# -------------------------------------------------------------------------
def _gen_build_from_zeros():
    cands = [(3, -5), (2, 7), (-4, 6), (1, -8), (5, 2), (-3, -7),
             (4, 9), (-2, 5), (6, -1), (-5, 8), (7, 3), (-6, -2),
             (2, -9), (8, 5)]
    variants = []
    i = 0
    for (r, s) in cands:
        if len(variants) >= 12:
            break
        prod, msum = r * s, -(r + s)
        if prod == 0 or r + s == 0:
            continue
        if len(variants) % 2 == 0:
            q_txt, correct = "its constant term", prod
            dvals = [msum, -prod, r + s]
            expl = ("$(x - (%d))(x - (%d))$ multiplies out to "
                    "$x^2%sx%s$, so the constant term is $rs = %d$. "
                    "Answering $-(r + s) = %d$ mixes it up with the "
                    "$x$-coefficient."
                    % (r, s, _pm(msum), _pm(prod), prod, msum))
        else:
            q_txt, correct = "the coefficient of $x$", msum
            dvals = [prod, r + s, -prod]
            expl = ("$(x - (%d))(x - (%d))$ multiplies out to "
                    "$x^2%sx%s$, so the $x$-coefficient is $-(r + s) = %d$. "
                    "Forgetting the minus sign gives $%d$."
                    % (r, s, _pm(msum), _pm(prod), msum, r + s))
        if not _distinct([correct] + dvals):
            continue
        stmt = ("A monic quadratic has zeros $%d$ and $%d$. What is %s?"
                % (r, s, q_txt))
        variants.append(_mk(
            "PC-zero-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % correct, ["$%d$" % v for v in dvals], i, expl,
            ["expand((x - (%d))*(x - (%d))) == x**2 + (%d)*x + (%d)"
             % (r, s, msum, prod)]))
        i += 1
    return _floor12("build-from-zeros", variants)


def _rs_build_from_zeros(s):
    m = re.search(r"zeros \$(-?\d+)\$ and \$(-?\d+)\$", s)
    r, z = int(m.group(1)), int(m.group(2))
    if "constant term" in s:
        return ("num", r * z)
    assert "coefficient of $x$" in s
    return ("num", -(r + z))


# -------------------------------------------------------------------------
# Form 8: slant-asymptote (rational-functions, level 3)
# -------------------------------------------------------------------------
def _gen_slant_asymptote():
    cands = [(3, 1, 2), (-2, 4, 3), (1, -5, 4), (5, 2, -2), (-4, 3, 1),
             (2, -1, 5), (-1, 6, 2), (4, -3, -3), (-3, 2, 4), (6, 1, -1),
             (-5, -2, 2), (2, 5, -4), (0, 3, 3), (1, 2, -5)]
    variants = []
    i = 0
    x = _sp.Symbol("x")
    for (a, b, c) in cands:
        if len(variants) >= 12:
            break
        m_ = a + c                     # slope-1 intercept of the slant line
        # verify by actual polynomial division
        quo, rem = _sp.div(x**2 + a * x + b, x - c, x)
        assert quo == x + m_, (a, b, c)
        opts_ints = {m_, a, -c}
        if len(opts_ints) != 3 or c == 0:
            continue
        correct = "$y = %s$" % _xpm(m_)
        dis = ["$y = %s$" % _xpm(a), "$y = %s$" % _xpm(-c), "$x = %d$" % c]
        num = "x^2" + (_ctm(a, "x") if a else "") + (_ctm(b, "") if b else "")
        den = _xpm(-c)
        stmt = ("Find the slant asymptote of "
                "$f(x) = \\dfrac{%s}{%s}$." % (num, den))
        variants.append(_mk(
            "PC-slant-v%02d" % (len(variants) + 1), stmt, correct, dis, i,
            "Long division gives $f(x) = x%s + \\frac{%s}{%s}$, and the "
            "fraction dies as $x \\to \\pm\\infty$, so the slant asymptote "
            "is $y = %s$. Reading the intercept straight off the numerator "
            "as $%d$ skips the division. ($x = %d$ is the vertical "
            "asymptote.)"
            % (_pm(m_), str(rem), den, _xpm(m_), a, c),
            ["quo(x**2 + (%d)*x + (%d), x - (%d), x) == x + (%d)"
             % (a, b, c, m_),
             "rem(x**2 + (%d)*x + (%d), x - (%d), x) == %d"
             % (a, b, c, int(rem))]))
        i += 1
    return _floor12("slant-asymptote", variants)


def _rs_slant_asymptote(s):
    m = re.search(r"\\dfrac\{x\^2((?: [+-] \d*x)?)((?: [+-] \d+)?)\}"
                  r"\{x ([+-]) (\d+)\}", s)
    a = 0
    if m.group(1):
        g = m.group(1).strip()          # like "+ 3x" or "- x"
        sign, digits = g[0], g[2:-1]
        a = (int(digits) if digits else 1) * (1 if sign == "+" else -1)
    b = 0
    if m.group(2):
        g = m.group(2).strip()
        b = int(g[2:]) * (1 if g[0] == "+" else -1)
    c = int(m.group(4)) * (-1 if m.group(3) == "+" else 1)
    x = _sp.Symbol("x")
    quo, _ = _sp.div(x**2 + a * x + b, x - c, x)
    return ("opt", "$y = %s$" % _xpm(int(quo.coeff(x, 0))))


# -------------------------------------------------------------------------
# Form 9: rational-intercepts (rational-functions, level 1)
# -------------------------------------------------------------------------
def _gen_rational_intercepts():
    cands = [(3, 7), (2, 5), (4, 9), (5, 2), (6, 11), (7, 3),
             (2, 9), (8, 3), (3, 10), (9, 4), (5, 8), (10, 3), (4, 7)]
    variants = []
    i = 0
    for (a, b) in cands:
        if len(variants) >= 12:
            break
        assert a != b and a * b != 0 and a * a != b * b
        stmt_head = "For $f(x) = \\dfrac{x - %d}{x - %d}$, " % (a, b)
        if len(variants) % 2 == 0:
            stmt = stmt_head + "what is the x-intercept?"
            correct = "$x = %d$" % a
            dis = ["$x = %d$" % b, "$x = %d$" % (-a), "$x = %d$" % (-b)]
            expl = ("The graph crosses the x-axis where the numerator is "
                    "zero: $x = %d$. The denominator's zero, $x = %d$, is "
                    "the vertical asymptote — the classic mix-up."
                    % (a, b))
            checks = ["(%d) - (%d) == 0" % (a, a),
                      "Abs((%d) - (%d)) > 0" % (a, b)]
        else:
            fr = Fraction(a, b)
            stmt = stmt_head + "what is the y-intercept?"
            correct = "$y = %s$" % _fr_core(fr)
            dvals = [Fraction(b, a), -fr, Fraction(a)]
            assert _distinct([fr] + dvals), (a, b)
            dis = ["$y = %s$" % _fr_core(v) for v in dvals]
            expl = ("Substitute $x = 0$: $f(0) = \\frac{0 - %d}{0 - %d} = "
                    "\\frac{%d}{%d}$ — the two minus signs cancel. Keeping "
                    "one of them gives $%s$."
                    % (a, b, a, b, _fr_core(-fr)))
            checks = ["Rational(0 - (%d), 0 - (%d)) == Rational(%d, %d)"
                      % (a, b, fr.numerator, fr.denominator)]
        variants.append(_mk(
            "PC-rint-v%02d" % (len(variants) + 1), stmt, correct, dis, i,
            expl, checks))
        i += 1
    return _floor12("rational-intercepts", variants)


def _rs_rational_intercepts(s):
    m = re.search(r"\\dfrac\{x - (\d+)\}\{x - (\d+)\}", s)
    a, b = int(m.group(1)), int(m.group(2))
    if "x-intercept" in s:
        return ("opt", "$x = %d$" % a)
    assert "y-intercept" in s
    return ("opt", "$y = %s$" % _fr_core(Fraction(-a, -b)))


# -------------------------------------------------------------------------
# Form 10: exp-growth-value (exponentials-and-logarithms, level 2)
# -------------------------------------------------------------------------
def _gen_exp_growth_value():
    # (A, base, k): half base 3, several negative k -> fraction answers
    cands = [(3, 2, 4), (5, 3, 2), (2, 2, -3), (4, 3, -2), (5, 2, 3),
             (2, 3, 3), (3, 2, -2), (7, 3, -1), (4, 2, 5), (10, 3, 2),
             (7, 2, -4), (5, 3, -3), (3, 2, 6), (2, 3, 4)]
    variants = []
    i = 0
    for (A, base, k) in cands:
        if len(variants) >= 12:
            break
        correct = Fraction(base) ** k * A
        dvals = [Fraction(A * base * k), Fraction(base) ** k,
                 Fraction(A) ** k * base]
        if not _distinct([correct] + dvals):
            continue
        stmt = ("If $f(x) = %d \\cdot %d^x$, find $f(%d)$." % (A, base, k))
        if k > 0:
            expl = ("$f(%d) = %d \\cdot %d^{%d} = %d \\cdot %d = %s$. "
                    "Multiplying instead of exponentiating — "
                    "$%d \\cdot %d \\cdot %d$ — gives $%d$."
                    % (k, A, base, k, A, base ** k, _fr_core(correct),
                       A, base, k, A * base * k))
        else:
            expl = ("The negative exponent means a reciprocal: "
                    "$f(%d) = %d \\cdot \\frac{1}{%d^{%d}} = %s$. "
                    "Multiplying instead of exponentiating gives $%d$."
                    % (k, A, base, -k, _fr_core(correct), A * base * k))
        variants.append(_mk(
            "PC-exp-v%02d" % (len(variants) + 1), stmt,
            _fr_tex(correct), [_fr_tex(v) for v in dvals], i, expl,
            ["(%d) * Rational(%d)**(%d) == Rational(%d, %d)"
             % (A, base, k, correct.numerator, correct.denominator)]))
        i += 1
    return _floor12("exp-growth-value", variants)


def _rs_exp_growth_value(s):
    m = re.search(r"f\(x\) = (\d+) \\cdot (\d+)\^x", s)
    A, base = int(m.group(1)), int(m.group(2))
    k = int(re.search(r"f\((-?\d+)\)\$", s).group(1))
    return ("num", A * Rational(base) ** k)


# -------------------------------------------------------------------------
# Form 11: log-solve-precalc (exponentials-and-logarithms, level 2)
# -------------------------------------------------------------------------
def _gen_log_solve():
    # (b, a, c) with b in {2,3,5}, c in 1..3; avoid b == c collisions
    cands = [(2, 5, 3), (3, -4, 2), (5, 1, 2), (2, -3, 5), (3, 2, 2),
             (5, -2, 2), (2, 7, 5), (3, 1, 4), (5, 4, 3), (2, -1, 6),
             (3, -5, 2), (5, 3, 2), (2, 2, 3), (3, 6, 2)]
    variants = []
    i = 0
    for (b, a, c) in cands:
        if len(variants) >= 12:
            break
        ans = b ** c + a
        dvals = [b * c + a, c ** b + a, b ** c - a]
        if not _distinct([ans] + dvals):
            continue
        stmt = "Solve for $x$: $\\log_%d(%s) = %d$." % (b, _xpm(-a), c)
        variants.append(_mk(
            "PC-log-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "Rewrite in exponential form: $%s = %d^{%d} = %d$, so "
            "$x = %d$. Multiplying base times exponent — "
            "$%d \\cdot %d%s$ — gives $%d$."
            % (_xpm(-a), b, c, b ** c, ans, b, c, _pm(a), b * c + a),
            ["(%d)**(%d) + (%d) == %d" % (b, c, a, ans),
             "((%d) - (%d)) == (%d)**(%d)" % (ans, a, b, c)]))
        i += 1
    return _floor12("log-solve-precalc", variants)


def _rs_log_solve(s):
    m = re.search(r"\\log_(\d)\(x ([+-]) (\d+)\) = (\d+)", s)
    b = int(m.group(1))
    a = int(m.group(3)) * (-1 if m.group(2) == "+" else 1)
    c = int(m.group(4))
    return ("num", b ** c + a)


# -------------------------------------------------------------------------
# Form 12: radian-exact (the-unit-circle, level 1)
# -------------------------------------------------------------------------
_TRIG_POOL = ["0", "1", "-1", "1/2", "-1/2", "sqrt(2)/2", "-sqrt(2)/2",
              "sqrt(3)/2", "-sqrt(3)/2"]


def _gen_radian_exact():
    cases = [("sin", 1, 6), ("sin", 5, 6), ("sin", 7, 6), ("sin", 4, 3),
             ("sin", 11, 6), ("sin", 1, 2), ("cos", 1, 3), ("cos", 3, 4),
             ("cos", 2, 3), ("cos", 5, 4), ("cos", 5, 3), ("cos", 7, 6)]
    variants = []
    for i, (fn, p, q) in enumerate(cases):
        ang = Rational(p, q) * _sp.pi
        val = _sp.sin(ang) if fn == "sin" else _sp.cos(ang)
        co = _sp.cos(ang) if fn == "sin" else _sp.sin(ang)
        key = _trig_key(val)
        # distractors: sign flip, the co-function value, its sign flip —
        # patched from the pool whenever they collide with the answer.
        want = [_sp.Integer(-1) * val, co, _sp.Integer(-1) * co]
        dis_keys, used = [], {key}
        for w in want:
            try:
                k2 = _trig_key(w)
            except ValueError:
                k2 = None
            if k2 is None or k2 in used:
                k2 = next(k for k in _TRIG_POOL if k not in used)
            dis_keys.append(k2)
            used.add(k2)
        stmt = ("Evaluate exactly: $\\%s%s$." % (fn, _pi_frac_tex(p, q)))
        cofn = "cos" if fn == "sin" else "sin"
        variants.append(_mk(
            "PC-rad-v%02d" % (i + 1), stmt,
            "$%s$" % _TRIG_TEX[key], ["$%s$" % _TRIG_TEX[k] for k in dis_keys],
            i,
            "The reference angle and the quadrant's sign give "
            "$\\%s%s = %s$. Quoting the co-function value "
            "$\\%s%s = %s$ is the classic swap."
            % (fn, _pi_frac_tex(p, q), _TRIG_TEX[key],
               cofn, _pi_frac_tex(p, q), _TRIG_TEX[_trig_key(co)]),
            ["%s(%d*pi/%d) == %s" % (fn, p, q, key)]))
    return _floor12("radian-exact", variants)


def _rs_radian_exact(s):
    m = re.search(r"\\(sin|cos)\\dfrac\{(\d*)\\pi\}\{(\d+)\}", s)
    fn = m.group(1)
    p = int(m.group(2)) if m.group(2) else 1
    q = int(m.group(3))
    ang = Rational(p, q) * _sp.pi
    return ("num", _sp.sin(ang) if fn == "sin" else _sp.cos(ang))


# -------------------------------------------------------------------------
# Form 13: point-on-circle (the-unit-circle, level 2)
# -------------------------------------------------------------------------
def _pt_pair(ck, sk):
    return "$(%s; %s)$" % (_TRIG_TEX[ck], _TRIG_TEX[sk])


def _gen_point_on_circle():
    cases = [(1, 6), (5, 6), (7, 6), (11, 6), (1, 3), (2, 3), (4, 3),
             (5, 3), (1, 4), (3, 4), (5, 4), (7, 4)]
    variants = []
    for i, (p, q) in enumerate(cases):
        ang = Rational(p, q) * _sp.pi
        c, s = _sp.cos(ang), _sp.sin(ang)
        ck, sk = _trig_key(c), _trig_key(s)
        nck, nsk = _trig_key(-c), _trig_key(-s)
        correct = _pt_pair(ck, sk)
        if q == 4:
            # |cos| == |sin| here, so a swapped pair may collide — use the
            # three sign-trap pairs instead.
            dis = [_pt_pair(nck, sk), _pt_pair(ck, nsk), _pt_pair(nck, nsk)]
        else:
            dis = [_pt_pair(sk, ck), _pt_pair(nck, sk), _pt_pair(ck, nsk)]
        stmt = ("The terminal point of $t = %s$ on the unit circle is "
                "which of the following?" % _pi_frac_tex(p, q))
        variants.append(_mk(
            "PC-pt-v%02d" % (i + 1), stmt, correct, dis, i,
            "The terminal point is $(\\cos t; \\sin t)$: cosine first, "
            "then sine, with signs set by the quadrant — here "
            "$(%s; %s)$. Writing the pair as $(\\sin t; \\cos t)$ is the "
            "classic swap." % (_TRIG_TEX[ck], _TRIG_TEX[sk]),
            ["cos(%d*pi/%d) == %s" % (p, q, ck),
             "sin(%d*pi/%d) == %s" % (p, q, sk)]))
    return _floor12("point-on-circle", variants)


def _rs_point_on_circle(s):
    m = re.search(r"t = \\dfrac\{(\d*)\\pi\}\{(\d+)\}", s)
    p = int(m.group(1)) if m.group(1) else 1
    q = int(m.group(2))
    ang = Rational(p, q) * _sp.pi
    return ("opt", _pt_pair(_trig_key(_sp.cos(ang)), _trig_key(_sp.sin(ang))))


# -------------------------------------------------------------------------
# Form 14: count-solutions (trigonometric-graphs-and-equations, level 3)
# -------------------------------------------------------------------------
# (fn, c-latex, count, verification checks on [0°, 360°))
_CNT_CASES = [
    ("sin", "0", 2, ["sin(rad(0)) == 0", "sin(rad(180)) == 0"]),
    ("sin", "1", 1, ["sin(rad(90)) == 1"]),
    ("sin", "-1", 1, ["sin(rad(270)) == -1"]),
    ("sin", "\\frac{1}{2}", 2,
     ["sin(rad(30)) == Rational(1,2)", "sin(rad(150)) == Rational(1,2)"]),
    ("sin", "2", 0, ["Abs(2) > 1"]),
    ("sin", "\\frac{\\sqrt{3}}{2}", 2,
     ["sin(rad(60)) == sqrt(3)/2", "sin(rad(120)) == sqrt(3)/2"]),
    ("cos", "0", 2, ["cos(rad(90)) == 0", "cos(rad(270)) == 0"]),
    ("cos", "1", 1, ["cos(rad(0)) == 1"]),
    ("cos", "-1", 1, ["cos(rad(180)) == -1"]),
    ("cos", "-\\frac{1}{2}", 2,
     ["cos(rad(120)) == -Rational(1,2)", "cos(rad(240)) == -Rational(1,2)"]),
    ("cos", "-2", 0, ["Abs(-2) > 1"]),
    ("cos", "\\frac{\\sqrt{2}}{2}", 2,
     ["cos(rad(45)) == sqrt(2)/2", "cos(rad(315)) == sqrt(2)/2"]),
]


def _cnt_reason(fn, n):
    if n == 0:
        return ("the value lies outside $[-1, 1]$, beyond the range of "
                "$\\%s$, so there are no solutions" % fn)
    if n == 1:
        return ("the graph of $\\%s$ touches this extreme value exactly "
                "once per period" % fn)
    return ("the horizontal line cuts one full wave of $\\%s$ twice" % fn)


def _gen_count_solutions():
    variants = []
    for i, (fn, ctex, n, checks) in enumerate(_CNT_CASES):
        dvals = [n + 1, n - 1 if n >= 1 else n + 2, 4]
        assert _distinct([n] + dvals)
        stmt = ("How many solutions does $\\%s x = %s$ have on the "
                "interval $[0°, 360°)$?" % (fn, ctex))
        variants.append(_mk(
            "PC-cnt-v%02d" % (i + 1), stmt, "$%d$" % n,
            ["$%d$" % v for v in dvals], i,
            "On $[0°, 360°)$ %s: the count is $%d$. Counting an endpoint "
            "twice (or forgetting a quadrant) shifts the answer by one."
            % (_cnt_reason(fn, n), n),
            checks))
    return _floor12("count-solutions", variants)


def _rs_count_solutions(s):
    m = re.search(r"\$\\(sin|cos) x = (.+?)\$ have", s)
    fn, ctex = m.group(1), m.group(2)
    t = ctex.replace("\\frac", "frac")
    t = re.sub(r"\\sqrt\{(\d+)\}", r"sqrt(\1)", t)
    t = re.sub(r"frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
    c = _sp.sympify(t)
    if abs(c) > 1:
        n = 0
    elif abs(c) == 1:
        n = 1
    elif fn == "cos" and c == 0:
        n = 2                    # 90° and 270°
    else:
        n = 2                    # sin: two symmetric solutions (0 -> 0°,180°)
    return ("num", n)


# -------------------------------------------------------------------------
# Form 15: general-solution-form (trigonometric-graphs-and-equations, level 2)
# -------------------------------------------------------------------------
# tan value latex -> base angle in degrees on [0°, 180°)
_TAN_CASES = [("\\sqrt{3}", 60), ("1", 45), ("\\frac{\\sqrt{3}}{3}", 30),
              ("-1", 135), ("-\\sqrt{3}", 120),
              ("-\\frac{\\sqrt{3}}{3}", 150), ("0", 0)]
_TAN_SYM = {"\\sqrt{3}": "sqrt(3)", "1": "1",
            "\\frac{\\sqrt{3}}{3}": "sqrt(3)/3", "-1": "-1",
            "-\\sqrt{3}": "-sqrt(3)", "-\\frac{\\sqrt{3}}{3}": "-sqrt(3)/3",
            "0": "0"}


def _gen_family(base):
    if base == 0:
        return "$x = k \\cdot 180°$"
    return "$x = %d° + k \\cdot 180°$" % base


def _gen_general_solution():
    stems = [
        "Which of the following lists ALL solutions of $\\tan x = %s$?",
        "Find all solutions of $\\tan x = %s$ (where $k$ is any integer).",
    ]
    variants = []
    i = 0
    for si, stem in enumerate(stems):
        for (vtex, base) in _TAN_CASES:
            if si == 1 and base in (45, 0):     # 12 total: 7 + 5
                continue
            if base == 0:
                correct = _gen_family(0)
                dis = ["$x = k \\cdot 360°$",
                       "$x = 90° + k \\cdot 180°$", "$x = 0°$"]
                wrongbase = 90
            else:
                wrongbase = (90 - base) % 180
                if wrongbase == base:
                    wrongbase = 30
                correct = _gen_family(base)
                dis = ["$x = %d° + k \\cdot 360°$" % base,
                       _gen_family(wrongbase), "$x = %d°$" % base]
            stmt = stem % vtex
            checks = ["tan(rad(%d)) == %s" % (base, _TAN_SYM[vtex]),
                      "tan(rad(%d)) == %s" % (base + 180, _TAN_SYM[vtex])]
            variants.append(_mk(
                "PC-gen-v%02d" % (len(variants) + 1), stmt, correct, dis, i,
                "Tangent repeats every $180°$, so one family covers every "
                # `correct` already carries its own $...$; stripping them (as
                # this once did) drops raw LaTeX into the prose, where KaTeX
                # never runs and the reader sees "k \cdot 180°".
                "solution: %s. Using the period $360°$ — right for sine "
                "and cosine, wrong for tangent — misses half the answers."
                % correct,
                checks))
            i += 1
    return _floor12("general-solution-form", variants)


def _rs_general_solution(s):
    m = re.search(r"\\tan x = (.+?)\$", s)
    v = _sp.sympify(_TAN_SYM[m.group(1)])
    base = int(_sp.deg(_sp.atan(v))) % 180
    return ("opt", _gen_family(base))


# -------------------------------------------------------------------------
# Form 16: circle-equation (conic-sections, level 1)
# -------------------------------------------------------------------------
def _gen_circle_equation():
    centers = [(2, -3, 16), (-1, 4, 49), (5, 2, 9), (-4, -6, 25),
               (3, 7, 36), (-2, 1, 64)]
    radii = [(1, -2, 7), (-3, 4, 5), (2, 5, 4), (-1, -4, 6),
             (4, 1, 8), (-5, 3, 10)]
    variants = []
    i = 0
    for (h, k, rr) in centers:
        stmt = ("The circle $(x%s)^2 + (y%s)^2 = %d$ has its center at "
                "which point?" % (_pm(-h), _pm(-k), rr))
        dis = ["$(%d; %d)$" % (-h, -k), "$(%d; %d)$" % (-h, k),
               "$(%d; %d)$" % (h, -k)]
        variants.append(_mk(
            "PC-circ-v%02d" % (len(variants) + 1), stmt,
            "$(%d; %d)$" % (h, k), dis, i,
            "The standard form $(x - h)^2 + (y - k)^2 = r^2$ hides the "
            "center behind minus signs: here $(%d; %d)$. Reading the "
            "written signs literally gives $(%d; %d)$ — the classic trap."
            % (h, k, -h, -k),
            ["((%d) - (%d))**2 + ((%d) - (%d))**2 == 0" % (h, h, k, k),
             "(%d) > 0" % rr]))
        i += 1
    for (h, k, r) in radii:
        rr = r * r
        dvals = [rr, 2 * r, rr - r]
        assert _distinct([r] + dvals)
        stmt = ("What is the radius of the circle "
                "$(x%s)^2 + (y%s)^2 = %d$?" % (_pm(-h), _pm(-k), rr))
        variants.append(_mk(
            "PC-circ-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % r, ["$%d$" % v for v in dvals], i,
            "The right side is $r^2$, so $r = \\sqrt{%d} = %d$. Answering "
            "$%d$ forgets to take the square root."
            % (rr, r, rr),
            ["sqrt(%d) == %d" % (rr, r), "(%d)**2 == %d" % (r, rr)]))
        i += 1
    return _floor12("circle-equation", variants)


def _rs_circle_equation(s):
    m = re.search(r"\(x ([+-]) (\d+)\)\^2 \+ \(y ([+-]) (\d+)\)\^2 = (\d+)",
                  s)
    h = int(m.group(2)) * (-1 if m.group(1) == "+" else 1)
    k = int(m.group(4)) * (-1 if m.group(3) == "+" else 1)
    rr = int(m.group(5))
    if "center" in s:
        return ("opt", "$(%d; %d)$" % (h, k))
    assert "radius" in s
    return ("num", _sp.sqrt(rr))


# -------------------------------------------------------------------------
# Form 17: parabola-vertex-conic (conic-sections, level 2)
# -------------------------------------------------------------------------
_DIRS = ["To the right", "To the left", "Upward", "Downward"]


def _gen_parabola_conic():
    variants = []
    i = 0
    for a in [2, -3, 5, -4]:
        correct = _DIRS[0] if a > 0 else _DIRS[1]
        dis = [d for d in _DIRS if d != correct]
        stmt = "The parabola $x = %dy^2$ opens in which direction?" % a
        variants.append(_mk(
            "PC-parv-v%02d" % (len(variants) + 1), stmt, correct, dis, i,
            "With $x$ expressed in terms of $y^2$ the parabola is "
            "horizontal, and the %s coefficient $%d$ points it %s. "
            "\"Upward/downward\" belongs to $y = ax^2$ — the classic "
            "axis mix-up."
            % ("positive" if a > 0 else "negative", a,
               "right" if a > 0 else "left"),
            ["(%d) %s 0" % (a, ">" if a > 0 else "<")]))
        i += 1
    for fourp in [4, 8, 12, 16, 20, -4, -8, -12]:
        p = fourp // 4
        dis = ["$(%d; 0)$" % fourp, "$(0; %d)$" % p, "$(%d; 0)$" % (-p)]
        stmt = ("The parabola $y^2 = %dx$ has its focus at which point?"
                % fourp)
        variants.append(_mk(
            "PC-parv-v%02d" % (len(variants) + 1), stmt,
            "$(%d; 0)$" % p, dis, i,
            "Match $y^2 = 4px$: $4p = %d$ gives $p = %d$, so the focus is "
            "$(%d; 0)$ on the axis of symmetry. Forgetting to divide by 4 "
            "puts it at $(%d; 0)$." % (fourp, p, p, fourp),
            ["4*(%d) == %d" % (p, fourp)]))
        i += 1
    return _floor12("parabola-vertex-conic", variants)


def _rs_parabola_conic(s):
    if "opens in which direction" in s:
        a = int(re.search(r"\$x = (-?\d+)y\^2\$", s).group(1))
        return ("opt", _DIRS[0] if a > 0 else _DIRS[1])
    fourp = int(re.search(r"\$y\^2 = (-?\d+)x\$", s).group(1))
    assert fourp % 4 == 0
    return ("opt", "$(%d; 0)$" % (fourp // 4))


# -------------------------------------------------------------------------
# Form 18: ellipse-foci (conic-sections, level 3)
# -------------------------------------------------------------------------
def _gen_ellipse_foci():
    cands = [(25, 16, 3), (25, 9, 4), (100, 64, 6), (100, 36, 8),
             (169, 144, 5), (169, 25, 12), (225, 144, 9), (225, 81, 12),
             (289, 225, 8), (289, 64, 15), (625, 576, 7), (625, 49, 24)]
    variants = []
    for i, (A, B, c) in enumerate(cands):
        a, b = math.isqrt(A), math.isqrt(B)
        assert a * a == A and b * b == B and c * c == A - B and A > B
        dvals = [a - b, a + b, b]
        assert _distinct([c] + dvals), (A, B)
        stmt = ("For the ellipse $\\dfrac{x^2}{%d} + \\dfrac{y^2}{%d} = 1$, "
                "the foci are at $(\\pm c; 0)$. Find $c$." % (A, B))
        variants.append(_mk(
            "PC-ell-v%02d" % (i + 1), stmt, "$%d$" % c,
            ["$%d$" % v for v in dvals], i,
            "For an ellipse $c^2 = a^2 - b^2 = %d - %d = %d$, so "
            "$c = %d$. Subtracting the radii themselves, $a - b = %d$, is "
            "the classic slip — the subtraction happens on the squares."
            % (A, B, A - B, c, a - b),
            ["sqrt(%d - %d) == %d" % (A, B, c),
             "(%d)**2 + (%d)**2 == (%d)**2" % (c, b, a)]))
    return _floor12("ellipse-foci", variants)


def _rs_ellipse_foci(s):
    m = re.search(r"\\dfrac\{x\^2\}\{(\d+)\} \+ \\dfrac\{y\^2\}\{(\d+)\}", s)
    A, B = int(m.group(1)), int(m.group(2))
    return ("num", _sp.sqrt(A - B))


# =========================================================================
# Assembly
# =========================================================================
def new_forms():
    """Unit-specific forms authored for this subject."""
    return [
        {"id": "evaluate-composite", "title": "Evaluating compositions",
         "level": 1, "unit": "functions-and-their-graphs",
         "skill": "f(g(k)): work inside out — evaluate g first, then feed it to f.",
         "variants": _gen_evaluate_composite()},
        {"id": "domain-combined", "title": "Domains with roots and fractions",
         "level": 2, "unit": "functions-and-their-graphs",
         "skill": "Intersect the conditions: the radicand stays ≥ 0 AND the denominator stays ≠ 0.",
         "variants": _gen_domain_combined()},
        {"id": "average-rate", "title": "Average rate of change",
         "level": 2, "unit": "functions-and-their-graphs",
         "skill": "Slope of the secant: (f(q) − f(p))/(q − p) — for x² + c it collapses to p + q.",
         "variants": _gen_average_rate()},
        {"id": "describe-transform", "title": "Naming the transformation",
         "level": 1, "unit": "transformations-of-graphs",
         "skill": "Inside the parentheses moves opposite its sign; outside moves as written; minus reflects.",
         "variants": _gen_describe_transform()},
        {"id": "transformed-point", "title": "Tracking a point through a transform",
         "level": 2, "unit": "transformations-of-graphs",
         "skill": "y = a·f(x − h): the x-coordinate shifts by h, the y-coordinate stretches by a.",
         "variants": _gen_transformed_point()},
        {"id": "polynomial-division", "title": "Division and the remainder",
         "level": 3, "unit": "polynomial-functions",
         "skill": "Dividing by (x − k) leaves remainder p(k) — substitute instead of long-dividing.",
         "variants": _gen_polynomial_division()},
        {"id": "build-from-zeros", "title": "Building a quadratic from its zeros",
         "level": 2, "unit": "polynomial-functions",
         "skill": "Monic with zeros r, s: x² − (r + s)x + rs — sum with a minus, product as-is.",
         "variants": _gen_build_from_zeros()},
        {"id": "slant-asymptote", "title": "Slant asymptotes",
         "level": 3, "unit": "rational-functions",
         "skill": "Degree over degree-minus-one: divide, keep the linear quotient, drop the remainder.",
         "variants": _gen_slant_asymptote()},
        {"id": "rational-intercepts", "title": "Intercepts of rational functions",
         "level": 1, "unit": "rational-functions",
         "skill": "x-intercept: numerator = 0. y-intercept: plug in x = 0 and watch the signs cancel.",
         "variants": _gen_rational_intercepts()},
        {"id": "exp-growth-value", "title": "Evaluating exponential models",
         "level": 2, "unit": "exponentials-and-logarithms",
         "skill": "A · b^x: exponentiate the base first, then scale by A; negative x means reciprocal.",
         "variants": _gen_exp_growth_value()},
        {"id": "log-solve-precalc", "title": "Solving log equations",
         "level": 2, "unit": "exponentials-and-logarithms",
         "skill": "log_b(inner) = c means inner = b^c — rewrite in exponential form, then isolate x.",
         "variants": _gen_log_solve()},
        {"id": "radian-exact", "title": "Exact values in radians",
         "level": 1, "unit": "the-unit-circle",
         "skill": "Reference angle + quadrant sign: read sin and cos of the special angles exactly.",
         "variants": _gen_radian_exact()},
        {"id": "point-on-circle", "title": "Terminal points on the unit circle",
         "level": 2, "unit": "the-unit-circle",
         "skill": "The terminal point of t is (cos t; sin t) — cosine first, signs from the quadrant.",
         "variants": _gen_point_on_circle()},
        {"id": "count-solutions", "title": "Counting trig solutions",
         "level": 3, "unit": "trigonometric-graphs-and-equations",
         "skill": "On [0°, 360°): |c| < 1 gives two solutions, |c| = 1 gives one, |c| > 1 gives none.",
         "variants": _gen_count_solutions()},
        {"id": "general-solution-form", "title": "General solutions of tan x = c",
         "level": 2, "unit": "trigonometric-graphs-and-equations",
         "skill": "Tangent's period is 180°: one family x = θ + k·180° catches every solution.",
         "variants": _gen_general_solution()},
        {"id": "circle-equation", "title": "Reading circle equations",
         "level": 1, "unit": "conic-sections",
         "skill": "(x − h)² + (y − k)² = r²: center (h; k) against the signs, radius √(right side).",
         "variants": _gen_circle_equation()},
        {"id": "parabola-vertex-conic", "title": "Horizontal parabolas and foci",
         "level": 2, "unit": "conic-sections",
         "skill": "x = ay² opens sideways with the sign of a; y² = 4px puts the focus at (p; 0).",
         "variants": _gen_parabola_conic()},
        {"id": "ellipse-foci", "title": "Foci of an ellipse",
         "level": 3, "unit": "conic-sections",
         "skill": "c² = a² − b² for an ellipse — subtract the squares, then take the root.",
         "variants": _gen_ellipse_foci()},
    ]


RESOLVERS.update({
    "evaluate-composite": _rs_evaluate_composite,
    "domain-combined": _rs_domain_combined,
    "average-rate": _rs_average_rate,
    "describe-transform": _rs_describe_transform,
    "transformed-point": _rs_transformed_point,
    "polynomial-division": _rs_polynomial_division,
    "build-from-zeros": _rs_build_from_zeros,
    "slant-asymptote": _rs_slant_asymptote,
    "rational-intercepts": _rs_rational_intercepts,
    "exp-growth-value": _rs_exp_growth_value,
    "log-solve-precalc": _rs_log_solve,
    "radian-exact": _rs_radian_exact,
    "point-on-circle": _rs_point_on_circle,
    "count-solutions": _rs_count_solutions,
    "general-solution-form": _rs_general_solution,
    "circle-equation": _rs_circle_equation,
    "parabola-vertex-conic": _rs_parabola_conic,
    "ellipse-foci": _rs_ellipse_foci,
})


# =========================================================================
# Batch 2 — the forms that take every Precalculus unit to six collections.
#
# Four units shipped with two forms each and two with three; a student who
# worked through Transformations had 24 problems and then nothing. Each form
# below drills something its unit did not already ask.
# =========================================================================

# --- functions-and-their-graphs ------------------------------------------
def _gen_inverse_linear():
    cands = [(2, 3), (3, -1), (4, 5), (5, 2), (2, -7), (3, 4),
             (6, 1), (4, -3), (7, 2), (5, -4), (8, 3), (3, 7)]
    variants = []
    for i, (a, b) in enumerate(cands):
        # f(x) = ax + b, so f^-1(x) = (x - b)/a
        assert a > 1
        correct = "$\\dfrac{x%s}{%d}$" % (_pm(-b), a)
        dvals = ["$\\dfrac{x%s}{%d}$" % (_pm(b), a),
                 "$%dx%s$" % (a, _pm(-b)),
                 "$\\dfrac{1}{%dx%s}$" % (a, _pm(b))]
        variants.append(_mk(
            "PC-inv-v%02d" % (i + 1),
            "For $f(x) = %dx%s$, find $f^{-1}(x)$." % (a, _pm(b)),
            correct, dvals, i,
            "Swap and solve: from $y = %dx%s$ you get $x = %dy%s$, so "
            "$y = \\dfrac{x%s}{%d}$. The inverse UNDOES the function — it is "
            "not the reciprocal $\\dfrac{1}{f(x)}$, which is what the fraction "
            "with $f$ in the denominator would be."
            % (a, _pm(b), a, _pm(b), _pm(-b), a),
            ["Eq(%d*((x - (%d))/%d) + (%d), x)" % (a, b, a, b)]))
    return _floor12("inverse-linear", variants)


def _rs_inverse_linear(s):
    m = re.search(r"f\(x\) = (\d+)x ([+-]) (\d+)\$", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    return ("opt", "$\\dfrac{x%s}{%d}$" % (_pm(-b), a))


_EVEN_ODD = [
    # (display latex, sympy source, kind, why)
    ("x^2 + 4", "x**2 + 4", "even", "every power of $x$ is even"),
    ("x^3 - x", "x**3 - x", "odd", "every power of $x$ is odd"),
    ("x^2 + x", "x**2 + x", "neither",
     "it mixes an even power with an odd one"),
    ("5x^4 - 2x^2", "5*x**4 - 2*x**2", "even", "both powers are even"),
    ("x^5 + 3x", "x**5 + 3*x", "odd", "both powers are odd"),
    ("x^3 + 1", "x**3 + 1", "neither",
     "the constant is an even term beside an odd one"),
    ("|x| - 7", "Abs(x) - 7", "even",
     "absolute value is symmetric about the $y$-axis"),
    ("\\dfrac{1}{x}", "1/x", "odd", "reciprocating flips the sign with $x$"),
    ("x^4 + x^3", "x**4 + x**3", "neither",
     "an even power sits beside an odd one"),
    ("6 - x^2", "6 - x**2", "even", "a constant is itself an even term"),
    ("2x^7 - x^3", "2*x**7 - x**3", "odd", "both powers are odd"),
    ("x^2 - 2x + 1", "x**2 - 2*x + 1", "neither",
     "the middle term breaks the symmetry"),
]



def _gen_even_odd():
    names = {"even": "even", "odd": "odd", "neither": "neither even nor odd"}
    variants = []
    for i, (expr, src, kind, why) in enumerate(_EVEN_ODD):
        correct = names[kind]
        wrongs = [names[k] for k in ("even", "odd", "neither") if k != kind]
        wrongs.append("both even and odd")
        # Test the definition at a concrete non-zero input rather than
        # asserting the classification by hand.
        at_neg = src.replace("x", "(-3)")
        at_pos = src.replace("x", "(3)")
        if kind == "even":
            chk = ["(%s) - (%s) == 0" % (at_neg, at_pos)]
        elif kind == "odd":
            chk = ["(%s) + (%s) == 0" % (at_neg, at_pos)]
        else:
            chk = ["(%s) - (%s) != 0" % (at_neg, at_pos),
                   "(%s) + (%s) != 0" % (at_neg, at_pos)]
        variants.append(_mk(
            "PC-eo-v%02d" % (i + 1),
            "Is $f(x) = %s$ even, odd, or neither?" % expr,
            correct, wrongs[:3], i,
            "Compare $f(-x)$ with $f(x)$: here %s, so the function is %s. "
            "Even means $f(-x) = f(x)$ — symmetry across the $y$-axis; odd "
            "means $f(-x) = -f(x)$ — symmetry through the origin; a mixture "
            "of even and odd powers is neither." % (why, correct),
            chk))
    return _floor12("even-odd", variants)


def _rs_even_odd(s):
    expr = re.search(r"f\(x\) = (.+?)\$ even", s).group(1)
    for e, _src, kind, _why in _EVEN_ODD:
        if e == expr:
            # The exact option string, not the bare word: "even" is a
            # substring of "neither even nor odd", so a phrase match would
            # confirm the wrong option just as happily.
            return ("opt", {"even": "even", "odd": "odd",
                            "neither": "neither even nor odd"}[kind])
    raise ValueError("even-odd: unknown expression %r" % expr)


# --- transformations-of-graphs -------------------------------------------
def _gen_write_transform():
    cands = [(3, 5), (-2, 4), (4, -3), (-5, 2), (1, 6), (-4, -1),
             (6, 3), (-1, -5), (2, 7), (-6, 1), (5, -2), (-3, 8)]
    variants = []
    for i, (h, k) in enumerate(cands):
        hword = "right $%d$" % h if h > 0 else "left $%d$" % (-h)
        kword = "up $%d$" % k if k > 0 else "down $%d$" % (-k)
        correct = "$y = (x%s)^2%s$" % (_pm(-h), _pm(k))
        wrongs = ["$y = (x%s)^2%s$" % (_pm(h), _pm(k)),
                  "$y = (x%s)^2%s$" % (_pm(-h), _pm(-k)),
                  "$y = (x%s)^2%s$" % (_pm(h), _pm(-k))]
        variants.append(_mk(
            "PC-wt-v%02d" % (i + 1),
            "The graph of $y = x^2$ is moved %s and %s. Write the new rule."
            % (hword, kword),
            correct, wrongs, i,
            "A horizontal move goes INSIDE the square and against its sign, "
            "so moving %s writes $(x%s)^2$. A vertical move goes outside and "
            "reads as written, so moving %s adds $%s$: the rule is %s."
            % (hword, _pm(-h), kword, _pm(k).strip(), correct),
            ["(0 - (%d))**2 + (%d) == %d" % (h, k, h * h + k)]))
    return _floor12("write-transform", variants)


def _rs_write_transform(s):
    m = re.search(r"moved (right|left) \$(\d+)\$ and (up|down) \$(\d+)\$", s)
    h = int(m.group(2)) * (1 if m.group(1) == "right" else -1)
    k = int(m.group(4)) * (1 if m.group(3) == "up" else -1)
    return ("opt", "$y = (x%s)^2%s$" % (_pm(-h), _pm(k)))


def _gen_vertex_form():
    cands = [(2, 3, 5), (-1, -4, 2), (3, 5, -6), (1, -2, -7), (-2, 6, 1),
             (4, -3, 8), (-3, 1, -4), (2, -5, 3), (5, 2, -1), (-4, -6, 7),
             (1, 7, -2), (3, -1, 6)]
    variants = []
    for i, (a, h, k) in enumerate(cands):
        lead = "" if a == 1 else ("-" if a == -1 else "%d" % a)
        correct = "$(%d; %d)$" % (h, k)
        wrongs = ["$(%d; %d)$" % (-h, k), "$(%d; %d)$" % (h, -k),
                  "$(%d; %d)$" % (k, h)]
        variants.append(_mk(
            "PC-vf-v%02d" % (i + 1),
            "Find the vertex of $y = %s(x%s)^2%s$." % (lead, _pm(-h), _pm(k)),
            correct, wrongs, i,
            "In $y = a(x - h)^2 + k$ the vertex is $(h; k)$. The bracket "
            "reads $x%s$, so $h = %d$ — the sign flips coming out of the "
            "bracket — and $k = %d$ is read as written. The $%s$ in front "
            "stretches the parabola but never moves its vertex."
            % (_pm(-h), h, k, lead or "1"),
            ["((%d)*(((%d)+1) - (%d))**2 + (%d)) - "
             "((%d)*((%d) - (%d))**2 + (%d)) == %d"
             % (a, h, h, k, a, h, h, k, a)]))
    return _floor12("vertex-form", variants)


def _rs_vertex_form(s):
    m = re.search(r"\(x ([+-]) (\d+)\)\^2 ([+-]) (\d+)\$", s)
    h = int(m.group(2)) * (1 if m.group(1) == "-" else -1)
    k = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
    return ("opt", "$(%d; %d)$" % (h, k))


def _gen_shifted_domain():
    cands = [(0, 6, 2), (-3, 5, 4), (1, 9, -2), (-8, -1, 3), (2, 10, 5),
             (-5, 0, -4), (4, 12, 1), (-7, -2, 6), (3, 8, -3), (-6, 4, 2),
             (5, 15, -1), (-4, 7, 4)]
    variants = []
    for i, (lo, hi, h) in enumerate(cands):
        assert lo < hi
        nl, nh = lo + h, hi + h
        correct = "$[%d,\\ %d]$" % (nl, nh)
        wrongs = ["$[%d,\\ %d]$" % (lo - h, hi - h),
                  "$[%d,\\ %d]$" % (lo, hi),
                  "$[%d,\\ %d]$" % (nl, hi)]
        hword = "%d" % h if h > 0 else "(%d)" % h
        variants.append(_mk(
            "PC-sd-v%02d" % (i + 1),
            "$f$ has domain $[%d,\\ %d]$. Find the domain of "
            "$g(x) = f(x%s)$." % (lo, hi, _pm(-h)),
            correct, wrongs, i,
            "$g$ can only be evaluated where the INPUT to $f$ is legal: "
            "$%d \\le x%s \\le %d$, so $%d \\le x \\le %d$. Subtracting %s "
            "instead of adding it moves the domain the wrong way — the "
            "graph shifts opposite to the sign inside the bracket, and so "
            "does the domain." % (lo, _pm(-h), hi, nl, nh, hword),
            ["(%d) + (%d) == %d" % (lo, h, nl),
             "(%d) + (%d) == %d" % (hi, h, nh)]))
    return _floor12("shifted-domain", variants)


def _rs_shifted_domain(s):
    lo, hi = [int(x) for x in
              re.search(r"domain \$\[(-?\d+),\\ (-?\d+)\]\$", s).groups()]
    m = re.search(r"f\(x ([+-]) (\d+)\)\$", s)
    h = int(m.group(2)) * (-1 if m.group(1) == "+" else 1)
    return ("opt", "$[%d,\\ %d]$" % (lo + h, hi + h))


_HSTRETCH = [
    (2, "compressed horizontally by a factor of $\\frac{1}{2}$"),
    (3, "compressed horizontally by a factor of $\\frac{1}{3}$"),
    (4, "compressed horizontally by a factor of $\\frac{1}{4}$"),
    (5, "compressed horizontally by a factor of $\\frac{1}{5}$"),
    (6, "compressed horizontally by a factor of $\\frac{1}{6}$"),
    (8, "compressed horizontally by a factor of $\\frac{1}{8}$"),
]


def _gen_horizontal_stretch():
    variants = []
    idx = 0
    for b, desc in _HSTRETCH:
        variants.append(_mk(
            "PC-hs-v%02d" % (idx + 1),
            "How does the graph of $y = f(%dx)$ compare with the graph of "
            "$y = f(x)$?" % b,
            desc,
            ["stretched horizontally by a factor of $%d$" % b,
             "stretched vertically by a factor of $%d$" % b,
             "compressed vertically by a factor of $\\frac{1}{%d}$" % b],
            idx,
            "A number multiplying $x$ INSIDE the function acts horizontally "
            "and does the opposite of what it looks like: $f(%dx)$ reaches "
            "the value $f(t)$ when $x = \\frac{t}{%d}$, so every point slides "
            "$%d$ times closer to the $y$-axis. A factor outside the "
            "function would stretch vertically instead." % (b, b, b),
            ["Rational(1, %d) < 1" % b]))
        idx += 1
    for b, _desc in _HSTRETCH:
        variants.append(_mk(
            "PC-hs-v%02d" % (idx + 1),
            "How does the graph of $y = f\\left(\\dfrac{x}{%d}\\right)$ "
            "compare with the graph of $y = f(x)$?" % b,
            "stretched horizontally by a factor of $%d$" % b,
            ["compressed horizontally by a factor of $\\frac{1}{%d}$" % b,
             "stretched vertically by a factor of $%d$" % b,
             "compressed vertically by a factor of $\\frac{1}{%d}$" % b],
            idx,
            "Dividing the input by $%d$ makes $x$ travel $%d$ times as far "
            "to reach the same value of $f$, so the graph stretches AWAY "
            "from the $y$-axis by a factor of $%d$. Inside the function, "
            "dividing stretches and multiplying compresses — the reverse of "
            "the outside rule." % (b, b, b),
            ["%d > 1" % b]))
        idx += 1
    return _floor12("horizontal-stretch", variants)


def _rs_horizontal_stretch(s):
    m = re.search(r"f\(([2-9])x\)", s)
    if m:
        b = int(m.group(1))
        return ("opt", "compressed horizontally by a factor of "
                       "$\\frac{1}{%d}$" % b)
    b = int(re.search(r"\\dfrac\{x\}\{(\d+)\}", s).group(1))
    return ("opt", "stretched horizontally by a factor of $%d$" % b)

# --- polynomial-functions -------------------------------------------------
_END_BEHAVIOUR = {
    (1, 1): "down on the left, up on the right",
    (1, -1): "up on the left, down on the right",
    (0, 1): "up on both ends",
    (0, -1): "down on both ends",
}


def _gen_end_behaviour():
    cands = [(2, 3), (-1, 4), (5, 5), (-3, 2), (1, 6), (-4, 7),
             (3, 4), (-2, 5), (6, 2), (-5, 3), (4, 8), (-6, 9)]
    variants = []
    for i, (a, n) in enumerate(cands):
        sign = 1 if a > 0 else -1
        correct = _END_BEHAVIOUR[(n % 2, sign)]
        wrongs = [v for k, v in sorted(_END_BEHAVIOUR.items())
                  if v != correct][:3]
        lead = ("" if a == 1 else ("-" if a == -1 else "%d" % a))
        big = 10 ** 4
        variants.append(_mk(
            "PC-eb-v%02d" % (i + 1),
            "Describe the end behaviour of $p(x) = %sx^{%d} + \\ldots$, where "
            "the dots stand for terms of lower degree." % (lead, n),
            correct, wrongs, i,
            "Only the leading term matters far from the origin. The degree "
            "$%d$ is %s, so the two ends %s, and the leading coefficient "
            "$%s$ is %s, which fixes the direction: %s."
            % (n, "odd" if n % 2 else "even",
               "point opposite ways" if n % 2 else "point the same way",
               lead or "1", "positive" if a > 0 else "negative", correct),
            ["(%d)*(%d)**%d %s 0" % (a, big, n, ">" if a > 0 else "<"),
             "(%d)*(%d)**%d %s 0"
             % (a, -big, n, ">" if a * (-1) ** n > 0 else "<")]))
    return _floor12("end-behaviour", variants)


def _rs_end_behaviour(s):
    m = re.search(r"p\(x\) = (-?\d*)x\^\{(\d+)\}", s)
    lead = m.group(1)
    a = 1 if lead == "" else (-1 if lead == "-" else int(lead))
    n = int(m.group(2))
    return ("opt", _END_BEHAVIOUR[(n % 2, 1 if a > 0 else -1)])


def _gen_zeros_factored():
    cands = [(1, 2, 3), (-1, 4, 2), (5, -3, 1), (2, 6, -4), (-5, 1, 7),
             (3, -2, 8), (4, 9, -1), (-6, 2, 5), (7, 3, -5), (1, -8, 6),
             (-3, 5, 9), (2, 7, -6)]
    variants = []
    for i, (r, s_, t) in enumerate(cands):
        assert len({r, s_, t}) == 3
        roots = sorted((r, s_, t))
        correct = "$x = %d,\\ %d,\\ %d$" % tuple(roots)
        neg = sorted((-r, -s_, -t))
        wrongs = ["$x = %d,\\ %d,\\ %d$" % tuple(neg),
                  "$x = %d,\\ %d,\\ %d$" % tuple(sorted((r, s_, -t))),
                  "$x = %d,\\ %d,\\ %d$" % tuple(sorted((-r, s_, t)))]
        variants.append(_mk(
            "PC-zf-v%02d" % (i + 1),
            "Find the zeros of $p(x) = (x%s)(x%s)(x%s)$."
            % (_pm(-r), _pm(-s_), _pm(-t)),
            correct, wrongs, i,
            "A product is zero exactly when one factor is zero, so set each "
            "bracket to $0$ in turn: $x = %d$, $x = %d$, $x = %d$. Each zero "
            "is the value that CANCELS its bracket, so it carries the "
            "opposite sign to the number written inside."
            % (roots[0], roots[1], roots[2]),
            ["((%d) - (%d))*((%d) - (%d))*((%d) - (%d)) == 0"
             % (r, r, r, s_, r, t)]))
    return _floor12("zeros-factored", variants)


def _rs_zeros_factored(s):
    parts = re.findall(r"\(x ([+-]) (\d+)\)", s)
    roots = sorted(int(n) * (1 if sg == "-" else -1) for sg, n in parts)
    return ("opt", "$x = %d,\\ %d,\\ %d$" % tuple(roots))


def _gen_multiplicity():
    cands = [(2, 2, -3, 3), (-1, 3, 4, 2), (5, 4, 1, 1), (3, 1, -2, 2),
             (-4, 2, 6, 5), (7, 3, -5, 4), (2, 5, 8, 2), (-6, 4, 3, 3),
             (9, 2, -1, 6), (4, 6, -7, 1), (-2, 3, 5, 2), (8, 1, -4, 4)]
    variants = []
    for i, (r, m, s_, n) in enumerate(cands):
        assert r != s_
        ask_first = i % 2 == 0
        root, mult = (r, m) if ask_first else (s_, n)
        crosses = mult % 2 == 1
        correct = ("crosses the $x$-axis there" if crosses
                   else "touches the $x$-axis and turns back")
        wrongs = [("touches the $x$-axis and turns back" if crosses
                   else "crosses the $x$-axis there"),
                  "has a vertical asymptote there",
                  "never reaches the $x$-axis"]
        variants.append(_mk(
            "PC-mu-v%02d" % (i + 1),
            "For $p(x) = (x%s)^{%d}(x%s)^{%d}$, what does the graph do at "
            "$x = %d$?" % (_pm(-r), m, _pm(-s_), n, root),
            correct, wrongs, i,
            "The zero at $x = %d$ has multiplicity $%d$. An ODD multiplicity "
            "changes the sign of $p$ as $x$ passes through, so the graph "
            "crosses; an EVEN multiplicity squares the sign away, so the "
            "graph touches and turns back. Here $%d$ is %s, so the graph %s."
            % (root, mult, mult, "odd" if crosses else "even", correct),
            # p just left of the root times p just right of it: negative
            # exactly when the graph crossed. Both roots are at least 3
            # apart, so the other factor keeps its sign across the step.
            ["(((%d) - (%d))**%d * ((%d) - (%d))**%d) * "
             "(((%d) - (%d))**%d * ((%d) - (%d))**%d) %s 0"
             % (root - 1, r, m, root - 1, s_, n,
                root + 1, r, m, root + 1, s_, n,
                "<" if crosses else ">")]))
    return _floor12("multiplicity", variants)


def _rs_multiplicity(s):
    parts = re.findall(r"\(x ([+-]) (\d+)\)\^\{(\d+)\}", s)
    asked = int(re.search(r"at \$x = (-?\d+)\$", s).group(1))
    for sg, n, mult in parts:
        root = int(n) * (1 if sg == "-" else -1)
        if root == asked:
            return ("opt", "crosses the $x$-axis there" if int(mult) % 2
                    else "touches the $x$-axis and turns back")
    raise ValueError("multiplicity: root %d not in %r" % (asked, parts))


def _gen_vieta():
    cands = [(1, -5, 6), (2, 7, 3), (1, 4, -12), (3, -2, -8), (1, -9, 20),
             (4, 5, 1), (2, -11, 5), (1, 8, 15), (5, 3, -2), (1, -7, 10),
             (3, 10, 7), (2, -3, -9)]
    variants = []
    for i, (a, b, c) in enumerate(cands):
        ask_sum = i % 2 == 0
        ans = Fraction(-b, a) if ask_sum else Fraction(c, a)
        wrong_vals = [Fraction(b, a), Fraction(-c, a), Fraction(a, c) if c
                      else Fraction(a, b), Fraction(b, c) if c else
                      Fraction(b, a)]
        seen, wrongs = {ans}, []
        for w in wrong_vals + [ans + 1, ans - 1, ans + 2]:
            if w not in seen:
                seen.add(w)
                wrongs.append(_fr_tex(w))
            if len(wrongs) == 3:
                break
        variants.append(_mk(
            "PC-vi-v%02d" % (i + 1),
            "The equation $%sx^2%s x%s = 0$ has roots $r$ and $s$. Find "
            "$%s$." % ("" if a == 1 else "%d" % a, _pm(b), _pm(c),
                       "r + s" if ask_sum else "rs"),
            _fr_tex(ans), wrongs, i,
            "Expanding $a(x - r)(x - s)$ and matching coefficients gives "
            "$r + s = -\\dfrac{b}{a}$ and $rs = \\dfrac{c}{a}$. Here that is "
            "$%s$. The minus sign belongs to the SUM only — dropping it "
            "there, or borrowing it for the product, is the usual slip."
            % _fr_core(ans),
            ["Rational(%d, %d) == %s"
             % (-b if ask_sum else c, a,
                "Rational(%d, %d)" % (ans.numerator, ans.denominator))]))
    return _floor12("vieta", variants)


def _rs_vieta(s):
    m = re.search(r"\$(\d*)x\^2 ([+-]) (\d+) x ([+-]) (\d+) = 0\$", s)
    a = 1 if m.group(1) == "" else int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    c = int(m.group(5)) * (1 if m.group(4) == "+" else -1)
    return ("num", Rational(-b, a) if "r + s" in s else Rational(c, a))


# --- rational-functions ---------------------------------------------------
def _gen_vertical_asymptotes():
    cands = [(2, 3), (-1, 5), (4, -2), (-6, 1), (7, 2), (-3, -8),
             (5, 9), (-4, 6), (1, -7), (8, 3), (-2, 10), (6, -5)]
    variants = []
    for i, (p, q) in enumerate(cands):
        assert p != q
        roots = sorted((p, q))
        correct = "$x = %d$ and $x = %d$" % tuple(roots)
        wrongs = ["$x = %d$ and $x = %d$" % tuple(sorted((-p, -q))),
                  "$y = %d$ and $y = %d$" % tuple(roots),
                  "$x = %d$ only" % roots[0]]
        variants.append(_mk(
            "PC-va-v%02d" % (i + 1),
            "Find the vertical asymptotes of "
            "$f(x) = \\dfrac{5}{(x%s)(x%s)}$." % (_pm(-p), _pm(-q)),
            correct, wrongs, i,
            "A vertical asymptote sits where the denominator is zero and the "
            "numerator is not. Setting each bracket to zero gives $x = %d$ "
            "and $x = %d$; the numerator $5$ is never zero, so both survive. "
            "Asymptotes found this way are vertical LINES $x = c$, not "
            "horizontal ones." % (roots[0], roots[1]),
            ["((%d) - (%d))*((%d) - (%d)) == 0" % (p, p, p, q),
             "((%d) - (%d))*((%d) - (%d)) == 0" % (q, p, q, q)]))
    return _floor12("vertical-asymptotes", variants)


def _rs_vertical_asymptotes(s):
    parts = re.findall(r"\(x ([+-]) (\d+)\)", s)
    roots = sorted(int(n) * (1 if sg == "-" else -1) for sg, n in parts)
    return ("opt", "$x = %d$ and $x = %d$" % tuple(roots))


def _lead_term(coef, deg):
    """The leading term as KaTeX: 6, 3x, 5x^{2}."""
    if deg == 0:
        return "%d" % coef
    body = "x" if deg == 1 else "x^{%d}" % deg
    return body if coef == 1 else "%d%s" % (coef, body)


def _gen_horizontal_asymptote():
    # (numerator degree, denominator degree, leading coefficients)
    cands = [(1, 1, 3, 2), (1, 2, 5, 4), (2, 2, 4, 7), (0, 1, 6, 3),
             (2, 3, 2, 5), (1, 1, 9, 4), (3, 3, 5, 2), (1, 3, 8, 3),
             (2, 2, 7, 3), (0, 2, 4, 9), (3, 4, 6, 5), (1, 1, 2, 5)]
    variants = []
    for i, (dn, dd, ln, ld) in enumerate(cands):
        assert ln > 1 and ld > 1, "keep both leading coefficients visible"
        ans = Fraction(ln, ld) if dn == dd else Fraction(0)
        correct = "$y = %s$" % _fr_core(ans)
        pool = [Fraction(ln, ld), Fraction(ld, ln), Fraction(0),
                Fraction(dn + 1, dd + 1)]
        seen, wrongs = {ans}, []
        for w in pool + [ans + 1, ans - 1, ans + 2]:
            if w not in seen:
                seen.add(w)
                wrongs.append("$y = %s$" % _fr_core(w))
            if len(wrongs) == 3:
                break
        big = 10 ** 4
        chk = (["Rational(%d * %d**%d, %d * %d**%d) == Rational(%d, %d)"
                % (ln, big, dn, ld, big, dd, ans.numerator, ans.denominator)]
               if dn == dd else
               ["Rational(%d * %d**%d, %d * %d**%d) < Rational(1, 100)"
                % (ln, big, dn, ld, big, dd)])
        variants.append(_mk(
            "PC-ha-v%02d" % (i + 1),
            "Find the horizontal asymptote of "
            "$f(x) = \\dfrac{%s + \\ldots}{%s + \\ldots}$, where the dots "
            "stand for terms of lower degree."
            % (_lead_term(ln, dn), _lead_term(ld, dd)),
            correct, wrongs, i,
            "Compare the degrees. The top has degree $%d$ and the bottom "
            "degree $%d$, so %s Everything below the leading term is swamped "
            "as $x$ grows, which is why only those two terms decide the level."
            % (dn, dd,
               "the bottom wins and the graph flattens onto $y = 0$."
               if dn < dd else
               "the degrees match and the asymptote is the ratio of the "
               "leading coefficients, $y = %s$." % _fr_core(ans)),
            chk))
    return _floor12("horizontal-asymptote", variants)


_LEAD_RE = r"(\d+)(?:x(?:\^\{(\d+)\})?)?"


def _rs_horizontal_asymptote(s):
    m = re.search(r"\\dfrac\{" + _LEAD_RE + r" \+ \\ldots\}\{"
                  + _LEAD_RE + r" \+ \\ldots\}", s)
    ln, ld = int(m.group(1)), int(m.group(3))
    top = m.group(0).split("}{")[0]
    bot = m.group(0).split("}{")[1]
    dn = 0 if "x" not in top else (int(m.group(2)) if m.group(2) else 1)
    dd = 0 if "x" not in bot else (int(m.group(4)) if m.group(4) else 1)
    return ("opt", "$y = %s$" % _fr_core(Fraction(ln, ld) if dn == dd
                                         else Fraction(0)))


def _gen_hole():
    cands = [2, -3, 5, -1, 4, -6, 7, -2, 3, -5, 8, -4]
    variants = []
    for i, a in enumerate(cands):
        b = a + (2 if a > 0 else -2)
        # f(x) = (x-a)(x-b) / (x-a): a hole at x = a, height b removed
        height = a - b
        correct = "a hole at $x = %d$" % a
        wrongs = ["a vertical asymptote at $x = %d$" % a,
                  "a hole at $x = %d$" % b,
                  "a vertical asymptote at $x = %d$" % b]
        variants.append(_mk(
            "PC-ho-v%02d" % (i + 1),
            "What happens to the graph of "
            "$f(x) = \\dfrac{(x%s)(x%s)}{x%s}$ at the value that makes the "
            "denominator zero?" % (_pm(-a), _pm(-b), _pm(-a)),
            correct, wrongs, i,
            "The factor $x%s$ appears on top AND bottom, so it cancels: away "
            "from $x = %d$ the function is just $x%s$. The cancelled factor "
            "leaves a single missing point — a hole at $x = %d$, height "
            "$%d$ — rather than an asymptote, because nothing blows up."
            % (_pm(-a), a, _pm(-b), a, height),
            ["((%d) - (%d))*((%d) - (%d))/((%d) - (%d)) == (%d) - (%d)"
             % (a + 1, a, a + 1, b, a + 1, a, a + 1, b),
             "((%d) - (%d)) == %d" % (a, b, height)]))
    return _floor12("hole", variants)


def _rs_hole(s):
    a = re.findall(r"\(x ([+-]) (\d+)\)", s)[0]
    return ("opt", "a hole at $x = %d$"
            % (int(a[1]) * (1 if a[0] == "-" else -1)))


def _gen_simplify_rational():
    cands = [2, 3, 5, 7, 4, 6, 8, 9, 10, 11, 12, 13]
    variants = []
    for i, a in enumerate(cands):
        # (x^2 - a^2)/(x - a) = x + a, with x != a
        correct = "$x%s$, with $x \\neq %d$" % (_pm(a), a)
        wrongs = ["$x%s$, with $x \\neq %d$" % (_pm(-a), a),
                  "$x%s$, with $x \\neq %d$" % (_pm(a), -a),
                  "$x^2%s$, with $x \\neq %d$" % (_pm(-a), a)]
        variants.append(_mk(
            "PC-sr-v%02d" % (i + 1),
            "Simplify $\\dfrac{x^2 - %d}{x%s}$, and state the restriction."
            % (a * a, _pm(-a)),
            correct, wrongs, i,
            "The top is a difference of two squares: "
            "$x^2 - %d = (x%s)(x%s)$. Cancelling the shared bracket leaves "
            "$x%s$ — but only where the cancelled factor was not zero, so "
            "$x \\neq %d$ has to travel with the answer. Dropping the "
            "restriction quietly changes the function."
            % (a * a, _pm(-a), _pm(a), _pm(a), a),
            ["((%d)**2 - %d)/((%d) - %d) == (%d) + %d"
             % (a + 1, a * a, a + 1, a, a + 1, a)]))
    return _floor12("simplify-rational", variants)


def _rs_simplify_rational(s):
    m = re.search(r"x\^2 - (\d+)\}\{x ([+-]) (\d+)\}", s)
    a = int(m.group(3)) * (1 if m.group(2) == "-" else -1)
    return ("opt", "$x%s$, with $x \\neq %d$" % (_pm(a), a))

# --- exponentials-and-logarithms ------------------------------------------
def _gen_log_condense():
    # Both arguments are powers of the base, so every logarithm in the
    # statement, the answer and the check is an exact integer.
    cands = [(2, 32, 4), (2, 64, 8), (3, 81, 9), (3, 243, 27), (5, 125, 25),
             (5, 625, 5), (10, 1000, 10), (10, 10000, 100), (7, 343, 49),
             (2, 128, 16), (3, 729, 3), (4, 256, 16)]
    variants = []
    for i, (b, p, q) in enumerate(cands):
        assert p > q and p % q == 0
        correct = "$\\log_{%d}\\dfrac{%d}{%d}$" % (b, p, q)
        wrongs = ["$\\log_{%d}\\dfrac{%d}{%d}$" % (b, q, p),
                  "$\\log_{%d}(%d)$" % (b, p * q),
                  "$\\dfrac{\\log_{%d}%d}{\\log_{%d}%d}$" % (b, p, b, q)]
        variants.append(_mk(
            "PC-lc-v%02d" % (i + 1),
            "Write $\\log_{%d}%d - \\log_{%d}%d$ as a single logarithm."
            % (b, p, b, q),
            correct, wrongs, i,
            "Subtracting logarithms of the same base divides their "
            "arguments: $\\log_b M - \\log_b N = \\log_b\\dfrac{M}{N}$, so "
            "this is $\\log_{%d}\\dfrac{%d}{%d}$, which equals $%d$. The "
            "QUOTIENT of two logarithms is a different object altogether — "
            "that one is the change-of-base formula, and it does not belong "
            "here." % (b, p, q, round(math.log(p // q, b))),
            ["log(%d, %d) - log(%d, %d) == log(Rational(%d, %d), %d)"
             % (p, b, q, b, p, q, b)]))
    return _floor12("log-condense", variants)


def _rs_log_condense(s):
    m = re.search(r"\\log_\{(\d+)\}(\d+) - \\log_\{\d+\}(\d+)\$", s)
    b, p, q = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("opt", "$\\log_{%d}\\dfrac{%d}{%d}$" % (b, p, q))


def _gen_half_life():
    cands = [(3, 6), (5, 20), (2, 8), (10, 30), (4, 16), (7, 21),
             (6, 24), (8, 40), (12, 36), (9, 27), (15, 45), (11, 55)]
    variants = []
    for i, (h, t) in enumerate(cands):
        n = t // h
        assert n * h == t and n >= 2
        ans = Fraction(1, 2 ** n)
        pool = [Fraction(1, 2 * n), Fraction(n, 2 ** n), Fraction(1, n),
                Fraction(2 ** n - 1, 2 ** n), Fraction(1, 2 ** (n + 1)),
                Fraction(1, 2 ** n - 1), Fraction(1, 2 ** n + 1)]
        seen, wrongs = {ans}, []
        for w in pool:
            if w not in seen:
                seen.add(w)
                wrongs.append(_fr_tex(w))
            if len(wrongs) == 3:
                break
        variants.append(_mk(
            "PC-hl-v%02d" % (i + 1),
            "A sample halves every $%d$ hours. What fraction of it is left "
            "after $%d$ hours?" % (h, t),
            _fr_tex(ans), wrongs, i,
            "In $%d$ hours the sample halves $\\frac{%d}{%d} = %d$ times, so "
            "what remains is $\\left(\\frac{1}{2}\\right)^{%d} = %s$. Halving "
            "$%d$ times is not the same as dividing by $%d$ — repeated "
            "halving shrinks far faster."
            % (t, t, h, n, n, _fr_core(ans), n, 2 * n),
            ["Rational(1, 2)**%d == Rational(%d, %d)"
             % (n, ans.numerator, ans.denominator)]))
    return _floor12("half-life", variants)


def _rs_half_life(s):
    h = int(re.search(r"halves every \$(\d+)\$ hours", s).group(1))
    t = int(re.search(r"after \$(\d+)\$ hours", s).group(1))
    return ("num", Rational(1, 2) ** (t // h))


# --- the-unit-circle ------------------------------------------------------
_SPECIAL_DEGREES = [30, 45, 60, 90, 120, 135, 150, 210, 225, 240, 300, 315]


def _rad_tex(deg):
    fr = Fraction(deg, 180)
    return "$%s$" % _pi_frac_tex(fr.numerator, fr.denominator)


def _gen_degree_radian():
    variants = []
    for i, deg in enumerate(_SPECIAL_DEGREES):
        fr = Fraction(deg, 180)
        # Distractors are the radian measures of neighbouring special angles,
        # so no option can be spotted by its formatting alone.
        others = [d for d in _SPECIAL_DEGREES if d != deg]
        wrongs = [_rad_tex(others[(i + k) % len(others)]) for k in (1, 4, 7)]
        assert len(set(wrongs)) == 3, deg
        variants.append(_mk(
            "PC-dr-v%02d" % (i + 1),
            "Convert $%d°$ to radians." % deg,
            _rad_tex(deg), wrongs, i,
            "Multiply by $\\dfrac{\\pi}{180}$: "
            "$%d \\cdot \\dfrac{\\pi}{180} = %s$. A half-turn is $180° = "
            "\\pi$, so anything under a full turn has to come out below "
            "$2\\pi$."
            % (deg, _pi_frac_tex(fr.numerator, fr.denominator)),
            ["Rational(%d, 180) == Rational(%d, %d)"
             % (deg, fr.numerator, fr.denominator)]))
    return _floor12("degree-radian", variants)


def _rs_degree_radian(s):
    return ("opt", _rad_tex(int(re.search(r"Convert \$(\d+)°\$",
                                          s).group(1))))


def _gen_coterminal():
    cands = [400, 750, -30, -200, 480, -405, 900, -135, 1000, -60, 620, -315]
    variants = []
    for i, given in enumerate(cands):
        ans = given % 360
        pool = [(ans + 180) % 360, 360 - ans, (ans + 90) % 360, ans + 360,
                (540 - ans) % 360, (ans + 45) % 360, ans + 720]
        seen, wrongs = {ans}, []
        for w in pool:
            if w not in seen:
                seen.add(w)
                wrongs.append("$%d°$" % w)
            if len(wrongs) == 3:
                break
        turns = abs(given - ans) // 360
        variants.append(_mk(
            "PC-co-v%02d" % (i + 1),
            "Find the angle between $0°$ and $360°$ that is coterminal with "
            "$%d°$." % given,
            "$%d°$" % ans, wrongs, i,
            "Add or subtract whole turns of $360°$ until the angle lands in "
            "range: $%d° %s %d \\cdot 360° = %d°$. Coterminal angles share a "
            "terminal ray, so every trigonometric value matches — which is "
            "why this reduction is safe to do before anything else."
            % (given, "-" if given > ans else "+", turns, ans),
            ["(%d - %d) %% 360 == 0" % (given, ans),
             "%d >= 0" % ans, "%d < 360" % ans]))
    return _floor12("coterminal", variants)


def _rs_coterminal(s):
    g = int(re.search(r"coterminal with \$(-?\d+)°\$", s).group(1))
    return ("opt", "$%d°$" % (g % 360))


def _gen_reference_angle():
    cands = [110, 160, 200, 250, 290, 340, 135, 225, 315, 100, 190, 280]
    variants = []
    for i, a in enumerate(cands):
        ref = (a if a < 90 else 180 - a if a < 180 else
               a - 180 if a < 270 else 360 - a)
        pool = [a, 180 - ref, 360 - ref, 180 + ref, ref + 90, a - 90,
                90 - ref, ref + 180]
        seen, wrongs = {ref}, []
        for w in pool:
            if w not in seen:
                seen.add(w)
                wrongs.append("$%d°$" % w)
            if len(wrongs) == 3:
                break
        assert len(wrongs) == 3, a
        quad = 1 if a < 90 else (2 if a < 180 else (3 if a < 270 else 4))
        variants.append(_mk(
            "PC-ra-v%02d" % (i + 1),
            "Find the reference angle for $%d°$." % a,
            "$%d°$" % ref, wrongs, i,
            "The reference angle is the ACUTE angle to the nearer half of "
            "the $x$-axis. $%d°$ lies in quadrant $%d$, so the reference "
            "angle is $%d°$. It is always strictly between $0°$ and $90°$ — "
            "anything outside that range is not a reference angle."
            % (a, quad, ref),
            ["%d > 0" % ref, "%d < 90" % ref]))
    return _floor12("reference-angle", variants)


def _rs_reference_angle(s):
    a = int(re.search(r"reference angle for \$(\d+)°\$", s).group(1)) % 360
    return ("opt", "$%d°$" % (a if a < 90 else 180 - a if a < 180 else
                              a - 180 if a < 270 else 360 - a))


# --- trigonometric-graphs-and-equations -----------------------------------
def _deg_tex(fr):
    return "$%s°$" % _fr_core(fr)


def _gen_amplitude_period():
    cands = [(3, 2), (5, 4), (2, 3), (7, 6), (4, 5), (6, 8),
             (1, 9), (8, 10), (9, 12), (2, 15), (10, 18), (5, 20)]
    variants = []
    for i, (a, b) in enumerate(cands):
        ask_period = i % 2 == 0
        period = Fraction(360, b)
        ans = period if ask_period else Fraction(a)
        wrap = _deg_tex if ask_period else _fr_tex
        pool = [Fraction(a), Fraction(b), period, Fraction(2 * a),
                Fraction(180, b), Fraction(a + b), Fraction(360, b + 1)]
        seen, wrongs = {ans}, []
        for w in pool:
            if w not in seen:
                seen.add(w)
                wrongs.append(wrap(w))
            if len(wrongs) == 3:
                break
        assert len(wrongs) == 3, (a, b)
        variants.append(_mk(
            "PC-ap-v%02d" % (i + 1),
            "For $y = %s\\sin(%dx)$, find the %s."
            % ("" if a == 1 else "%d" % a, b,
               "period, in degrees" if ask_period else "amplitude"),
            wrap(ans), wrongs, i,
            "The number in FRONT sets the amplitude — how far the curve "
            "reaches above and below its midline — so the amplitude here is "
            "$%d$. The number multiplying $x$ squeezes the graph "
            "horizontally, so the period is $\\dfrac{360°}{%d} = %s°$. "
            "Swapping the two roles is the usual slip."
            % (a, b, _fr_core(period)),
            ["Rational(360, %d) == Rational(%d, %d)"
             % (b, period.numerator, period.denominator)]))
    return _floor12("amplitude-period", variants)


def _rs_amplitude_period(s):
    m = re.search(r"y = (\d*)\\sin\((\d+)x\)", s)
    a = 1 if m.group(1) == "" else int(m.group(1))
    b = int(m.group(2))
    if "period" in s:
        return ("opt", _deg_tex(Fraction(360, b)))
    return ("opt", _fr_tex(Fraction(a)))


def _gen_midline_range():
    cands = [(3, 2), (5, -1), (2, 7), (4, -3), (6, 1), (1, 5),
             (7, -2), (8, 4), (2, -6), (9, 3), (5, 5), (3, -4)]
    variants = []
    for i, (a, d) in enumerate(cands):
        lo, hi = d - a, d + a
        correct = "$[%d,\\ %d]$" % (lo, hi)
        wrongs = ["$[%d,\\ %d]$" % (-a, a),
                  "$[%d,\\ %d]$" % (d, d + a),
                  "$[%d,\\ %d]$" % (lo - a, hi + a)]
        variants.append(_mk(
            "PC-mr-v%02d" % (i + 1),
            "Find the range of $y = %s\\sin x%s$."
            % ("" if a == 1 else "%d" % a, _pm(d)),
            correct, wrongs, i,
            "$\\sin x$ runs from $-1$ to $1$; multiplying by $%d$ stretches "
            "that to $-%d$ up to $%d$, and adding $%d$ lifts the whole thing "
            "onto the midline $y = %d$. So the range is $[%d,\\ %d]$ — "
            "centre $\\pm$ amplitude." % (a, a, a, d, d, lo, hi),
            ["(%d) - (%d) == %d" % (d, a, lo),
             "(%d) + (%d) == %d" % (d, a, hi)]))
    return _floor12("midline-range", variants)


def _rs_midline_range(s):
    m = re.search(r"y = (\d*)\\sin x ([+-]) (\d+)\$", s)
    a = 1 if m.group(1) == "" else int(m.group(1))
    d = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    return ("opt", "$[%d,\\ %d]$" % (d - a, d + a))


def _gen_phase_shift():
    cands = [30, -45, 60, -20, 90, -75, 15, -120, 40, -60, 25, -150]
    variants = []
    for i, c in enumerate(cands):
        word = "right $%d°$" % c if c > 0 else "left $%d°$" % (-c)
        wrongs = ["left $%d°$" % abs(c) if c > 0 else "right $%d°$" % abs(c),
                  "up $%d$" % abs(c), "down $%d$" % abs(c)]
        variants.append(_mk(
            "PC-ps-v%02d" % (i + 1),
            "Describe the phase shift of $y = \\sin(x%s°)$ compared with "
            "$y = \\sin x$." % _pm(-c),
            word, wrongs, i,
            "The shift lives inside the function, so the graph moves AGAINST "
            "the written sign: $\\sin(x%s°)$ takes the value $\\sin 0°$ at "
            "$x = %d°$, which is where $\\sin x$ was at $x = 0°$ — the curve "
            "has moved %s. A number added outside the sine would move it "
            "vertically instead." % (_pm(-c), c, word),
            ["Eq(sin((%d - (%d))*pi/180), 0)" % (c, c)]))
    return _floor12("phase-shift", variants)


def _rs_phase_shift(s):
    m = re.search(r"\\sin\(x ([+-]) (\d+)°\)", s)
    c = int(m.group(2)) * (1 if m.group(1) == "-" else -1)
    return ("opt", "right $%d°$" % c if c > 0 else "left $%d°$" % (-c))


# (function, latex value, sympy source, the two solutions on [0°, 360°))
_TRIG_SOLUTIONS = [
    ("sin", "\\frac{1}{2}", "Rational(1,2)", 30, 150),
    ("sin", "\\frac{\\sqrt{2}}{2}", "sqrt(2)/2", 45, 135),
    ("sin", "\\frac{\\sqrt{3}}{2}", "sqrt(3)/2", 60, 120),
    ("sin", "-\\frac{1}{2}", "-Rational(1,2)", 210, 330),
    ("sin", "-\\frac{\\sqrt{2}}{2}", "-sqrt(2)/2", 225, 315),
    ("sin", "-\\frac{\\sqrt{3}}{2}", "-sqrt(3)/2", 240, 300),
    ("cos", "\\frac{1}{2}", "Rational(1,2)", 60, 300),
    ("cos", "\\frac{\\sqrt{2}}{2}", "sqrt(2)/2", 45, 315),
    ("cos", "\\frac{\\sqrt{3}}{2}", "sqrt(3)/2", 30, 330),
    ("cos", "-\\frac{1}{2}", "-Rational(1,2)", 120, 240),
    ("cos", "-\\frac{\\sqrt{2}}{2}", "-sqrt(2)/2", 135, 225),
    ("cos", "-\\frac{\\sqrt{3}}{2}", "-sqrt(3)/2", 150, 210),
]


def _gen_solve_trig():
    variants = []
    for i, (fn, tex, src, p, q) in enumerate(_TRIG_SOLUTIONS):
        correct = "$x = %d°$ and $x = %d°$" % (p, q)
        wrongs = ["$x = %d°$ only" % p,
                  "$x = %d°$ and $x = %d°$" % (p, (p + 180) % 360),
                  "$x = %d°$ and $x = %d°$" % ((p + 90) % 360,
                                               (q + 90) % 360)]
        ref = min(p, 180 - p) if fn == "sin" else min(p, 360 - p)
        ref = ref if ref <= 90 else 180 - ref
        quads = ("the first and second" if fn == "sin" and not
                 tex.startswith("-") else
                 "the third and fourth" if fn == "sin" else
                 "the first and fourth" if not tex.startswith("-") else
                 "the second and third")
        variants.append(_mk(
            "PC-st-v%02d" % (i + 1),
            "Solve $\\%s x = %s$ for $0° \\le x < 360°$." % (fn, tex),
            correct, wrongs, i,
            "The reference angle is $%d°$, and $\\%s$ takes this value in "
            "%s quadrants, so $x = %d°$ and $x = %d°$. Stopping at the first "
            "solution a calculator reports is the standard way to lose half "
            "the answer." % (ref, fn, quads, p, q),
            ["Eq(%s(%d*pi/180), %s)" % (fn, p, src),
             "Eq(%s(%d*pi/180), %s)" % (fn, q, src)]))
    return _floor12("solve-trig", variants)


def _rs_solve_trig(s):
    m = re.search(r"\\(sin|cos) x = (.+?)\$ for", s)
    fn, tex = m.group(1), m.group(2)
    for f, t, _src, p, q in _TRIG_SOLUTIONS:
        if f == fn and t == tex:
            return ("opt", "$x = %d°$ and $x = %d°$" % (p, q))
    raise ValueError("solve-trig: unknown %r %r" % (fn, tex))


# --- conic-sections -------------------------------------------------------
def _gen_hyperbola_asymptotes():
    cands = [(3, 2), (5, 4), (2, 7), (4, 3), (6, 5), (2, 9),
             (7, 2), (9, 4), (3, 10), (8, 3), (5, 12), (11, 6)]
    variants = []
    for i, (a, b) in enumerate(cands):
        assert math.gcd(a, b) == 1 and a > 1 and b > 1
        correct = "$y = \\pm\\dfrac{%d}{%d}x$" % (b, a)
        wrongs = ["$y = \\pm\\dfrac{%d}{%d}x$" % (a, b),
                  "$y = \\pm\\dfrac{%d}{%d}x$" % (b * b, a * a),
                  "$y = \\pm%dx$" % (a * b)]
        variants.append(_mk(
            "PC-hy-v%02d" % (i + 1),
            "Find the asymptotes of "
            "$\\dfrac{x^2}{%d} - \\dfrac{y^2}{%d} = 1$." % (a * a, b * b),
            correct, wrongs, i,
            "The denominators are $a^2 = %d$ and $b^2 = %d$, so $a = %d$ and "
            "$b = %d$. A hyperbola opening left and right has asymptotes "
            "$y = \\pm\\dfrac{b}{a}x = \\pm\\dfrac{%d}{%d}x$. The square "
            "roots matter: using the denominators themselves gives a slope "
            "far too steep." % (a * a, b * b, a, b, b, a),
            ["sqrt(%d) == %d" % (a * a, a), "sqrt(%d) == %d" % (b * b, b)]))
    return _floor12("hyperbola-asymptotes", variants)


def _rs_hyperbola_asymptotes(s):
    m = re.search(r"x\^2\}\{(\d+)\} - \\dfrac\{y\^2\}\{(\d+)\}", s)
    a = int(_sp.sqrt(int(m.group(1))))
    b = int(_sp.sqrt(int(m.group(2))))
    return ("opt", "$y = \\pm\\dfrac{%d}{%d}x$" % (b, a))


def _gen_ellipse_axes():
    cands = [(5, 3), (4, 2), (6, 5), (7, 3), (10, 6), (8, 5),
             (9, 4), (12, 7), (11, 6), (13, 5), (15, 9), (14, 8)]
    variants = []
    for i, (a, b) in enumerate(cands):
        assert a > b
        ask_major = i % 2 == 0
        ans = 2 * a if ask_major else 2 * b
        pool = [a, b, 2 * b if ask_major else 2 * a, a + b, a + 1, 2 * a + 2]
        seen, wrongs = {ans}, []
        for w in pool:
            if w not in seen:
                seen.add(w)
                wrongs.append("$%d$" % w)
            if len(wrongs) == 3:
                break
        assert len(wrongs) == 3, (a, b)
        variants.append(_mk(
            "PC-ea-v%02d" % (i + 1),
            "For the ellipse $\\dfrac{x^2}{%d} + \\dfrac{y^2}{%d} = 1$, find "
            "the length of the %s axis."
            % (a * a, b * b, "major" if ask_major else "minor"),
            "$%d$" % ans, wrongs, i,
            "Take square roots of the denominators: $%d$ and $%d$, the "
            "larger one lying along the major axis. An axis runs the WHOLE "
            "way across, so its length is twice the semi-axis — the major "
            "axis is $%d$ and the minor axis is $%d$."
            % (a, b, 2 * a, 2 * b),
            ["sqrt(%d) == %d" % (a * a, a), "sqrt(%d) == %d" % (b * b, b),
             "2*%d == %d" % (a if ask_major else b, ans)]))
    return _floor12("ellipse-axes", variants)


def _rs_ellipse_axes(s):
    m = re.search(r"x\^2\}\{(\d+)\} \+ \\dfrac\{y\^2\}\{(\d+)\}", s)
    a = int(_sp.sqrt(int(m.group(1))))
    b = int(_sp.sqrt(int(m.group(2))))
    return ("num", 2 * (max(a, b) if "major" in s else min(a, b)))


def _gen_complete_square_circle():
    cands = [(2, 3, 12), (-1, 4, 4), (5, -2, 20), (-3, -6, 16), (4, 1, 8),
             (-5, 2, 5), (6, -3, 11), (-2, 7, 4), (3, 5, 15), (-4, -1, 8),
             (7, 2, 4), (-6, 3, 11)]
    variants = []
    for i, (h, k, r2) in enumerate(cands):
        d, e = -2 * h, -2 * k
        f = h * h + k * k - r2
        assert f != 0 and h != 0 and k != 0
        correct = "$(%d; %d)$" % (h, k)
        wrongs = ["$(%d; %d)$" % (-h, -k), "$(%d; %d)$" % (d, e),
                  "$(%d; %d)$" % (k, h)]
        variants.append(_mk(
            "PC-cs-v%02d" % (i + 1),
            "Find the centre of the circle $x^2 + y^2%s x%s y%s = 0$."
            % (_pm(d), _pm(e), _pm(f)),
            correct, wrongs, i,
            "Complete the square in each variable. Half of $%d$ is $%d$ and "
            "half of $%d$ is $%d$, so the equation rewrites as "
            "$(x%s)^2 + (y%s)^2 = %d$ and the centre is $(%d; %d)$. The "
            "centre is HALF each coefficient with the sign flipped — never "
            "the coefficient itself."
            % (d, d // 2, e, e // 2, _pm(-h), _pm(-k), r2, h, k),
            ["(%d)**2 + (%d)**2 + (%d)*(%d) + (%d)*(%d) + (%d) == -(%d)"
             % (h, k, d, h, e, k, f, r2)]))
    return _floor12("complete-square-circle", variants)


def _rs_complete_square_circle(s):
    m = re.search(r"x\^2 \+ y\^2 ([+-]) (\d+) x ([+-]) (\d+) y", s)
    d = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
    e = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
    return ("opt", "$(%d; %d)$" % (-d // 2, -e // 2))


_BATCH2_META = [
    ("inverse-linear", "Inverting a linear function", 2,
     "functions-and-their-graphs",
     "Swap x and y, then solve: the inverse undoes f, it is not 1/f.",
     _gen_inverse_linear, _rs_inverse_linear),
    ("even-odd", "Even, odd, or neither", 1, "functions-and-their-graphs",
     "Even: f(-x) = f(x). Odd: f(-x) = -f(x). Mixed powers: neither.",
     _gen_even_odd, _rs_even_odd),
    ("write-transform", "Writing a transformed rule", 1,
     "transformations-of-graphs",
     "Horizontal moves go inside and against the sign; vertical moves go "
     "outside and read as written.",
     _gen_write_transform, _rs_write_transform),
    ("vertex-form", "The vertex from vertex form", 1,
     "transformations-of-graphs",
     "y = a(x - h)^2 + k has vertex (h; k) — h flips coming out of the "
     "bracket, k does not.",
     _gen_vertex_form, _rs_vertex_form),
    ("shifted-domain", "The domain after a shift", 2,
     "transformations-of-graphs",
     "The domain moves with the graph: f(x - h) is legal where x - h is.",
     _gen_shifted_domain, _rs_shifted_domain),
    ("horizontal-stretch", "Stretching and squeezing sideways", 2,
     "transformations-of-graphs",
     "Inside the function, multiplying compresses and dividing stretches — "
     "the reverse of the outside rule.",
     _gen_horizontal_stretch, _rs_horizontal_stretch),
    ("end-behaviour", "End behaviour of a polynomial", 1,
     "polynomial-functions",
     "Degree parity decides whether the ends agree; the leading sign decides "
     "which way they point.",
     _gen_end_behaviour, _rs_end_behaviour),
    ("zeros-factored", "Zeros from factored form", 1, "polynomial-functions",
     "Set each bracket to zero — every zero carries the opposite sign to the "
     "number inside.",
     _gen_zeros_factored, _rs_zeros_factored),
    ("multiplicity", "Crossing or touching at a zero", 2,
     "polynomial-functions",
     "Odd multiplicity crosses the axis; even multiplicity touches and turns "
     "back.",
     _gen_multiplicity, _rs_multiplicity),
    ("vieta", "Sum and product of the roots", 2, "polynomial-functions",
     "r + s = -b/a and rs = c/a — the minus belongs to the sum only.",
     _gen_vieta, _rs_vieta),
    ("vertical-asymptotes", "Vertical asymptotes", 1, "rational-functions",
     "Where the denominator is zero and the numerator is not.",
     _gen_vertical_asymptotes, _rs_vertical_asymptotes),
    ("horizontal-asymptote", "Horizontal asymptotes", 2, "rational-functions",
     "Compare degrees: bottom bigger gives y = 0, equal gives the ratio of "
     "leading coefficients.",
     _gen_horizontal_asymptote, _rs_horizontal_asymptote),
    ("hole", "Holes against asymptotes", 3, "rational-functions",
     "A factor that cancels leaves a hole; one that survives on the bottom "
     "leaves an asymptote.",
     _gen_hole, _rs_hole),
    ("simplify-rational", "Simplifying with a restriction", 2,
     "rational-functions",
     "Cancel the shared factor, then carry the restriction it leaves behind.",
     _gen_simplify_rational, _rs_simplify_rational),
    ("log-condense", "Condensing logarithms", 2,
     "exponentials-and-logarithms",
     "log M - log N = log(M/N) — a difference of logs, not a quotient of "
     "them.",
     _gen_log_condense, _rs_log_condense),
    ("half-life", "Half-life", 2, "exponentials-and-logarithms",
     "Count the halvings, then raise 1/2 to that power.",
     _gen_half_life, _rs_half_life),
    ("degree-radian", "Degrees to radians", 1, "the-unit-circle",
     "Multiply by pi/180; a half-turn is exactly pi.",
     _gen_degree_radian, _rs_degree_radian),
    ("coterminal", "Coterminal angles", 1, "the-unit-circle",
     "Add or subtract whole turns of 360 degrees until the angle lands in "
     "range.",
     _gen_coterminal, _rs_coterminal),
    ("reference-angle", "Reference angles", 2, "the-unit-circle",
     "The acute angle to the nearer half of the x-axis — always under 90 "
     "degrees.",
     _gen_reference_angle, _rs_reference_angle),
    ("amplitude-period", "Amplitude and period", 1,
     "trigonometric-graphs-and-equations",
     "The coefficient in front sets the amplitude; the one on x sets the "
     "period, 360/b.",
     _gen_amplitude_period, _rs_amplitude_period),
    ("midline-range", "Range from the midline", 2,
     "trigonometric-graphs-and-equations",
     "Centre plus or minus amplitude.",
     _gen_midline_range, _rs_midline_range),
    ("phase-shift", "Phase shift", 2, "trigonometric-graphs-and-equations",
     "Inside the function the graph moves against the written sign.",
     _gen_phase_shift, _rs_phase_shift),
    ("solve-trig", "Solving sin and cos exactly", 2,
     "trigonometric-graphs-and-equations",
     "Two solutions per turn: reference angle first, then the two quadrants "
     "the sign allows.",
     _gen_solve_trig, _rs_solve_trig),
    ("hyperbola-asymptotes", "Asymptotes of a hyperbola", 3, "conic-sections",
     "y = +/- (b/a)x — take square roots of the denominators first.",
     _gen_hyperbola_asymptotes, _rs_hyperbola_asymptotes),
    ("ellipse-axes", "Axis lengths of an ellipse", 1, "conic-sections",
     "An axis is twice its semi-axis; the larger denominator sits under the "
     "major one.",
     _gen_ellipse_axes, _rs_ellipse_axes),
    ("complete-square-circle", "Completing the square for a circle", 2,
     "conic-sections",
     "The centre is half each coefficient, sign flipped.",
     _gen_complete_square_circle, _rs_complete_square_circle),
]


def _batch2_forms():
    return [{"id": fid, "title": title, "level": level, "unit": unit,
             "skill": skill, "variants": gen()}
            for fid, title, level, unit, skill, gen, _rz in _BATCH2_META]


_BATCH1_FORMS = new_forms


def new_forms():  # noqa: F811 — appends batch 2 to the original list
    """All unit-specific forms: the original set plus batch 2 above."""
    return _BATCH1_FORMS() + _batch2_forms()


RESOLVERS.update({fid: rz for fid, _t, _l, _u, _s, _g, rz in _BATCH2_META})


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
