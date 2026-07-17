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
                "solution: %s. Using the period $360°$ — right for sine "
                "and cosine, wrong for tangent — misses half the answers."
                % correct.strip("$"),
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
