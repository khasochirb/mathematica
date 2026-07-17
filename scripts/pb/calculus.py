# -*- coding: utf-8 -*-
"""Problem-bank subject: Calculus — mirrors the /math/calculus course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/calculus.py` to
self-check.
"""
import re
from fractions import Fraction

import sympy as sp
from sympy import Rational, sympify

SLUG = "calculus"
TITLE = "Calculus"
TITLE_MN = "Калькулюс"
BLURB = ("Unit-by-unit practice for the Calculus course — limits, derivatives, and integrals, exam-style.")

UNITS = [
    {"id": "limits-and-continuity", "title": "Limits & Continuity",
     "blurb": "What a function is heading toward: limits from graphs and algebra, limits at infinity, and the definition of an unbroken graph."},
    {"id": "the-derivative", "title": "The Derivative",
     "blurb": "Secants collapse onto tangents: the difference quotient, the derivative function, the power rule, and the four library derivatives."},
    {"id": "differentiation-techniques", "title": "Differentiation Techniques",
     "blurb": "Product, quotient, and chain rules; combining them, and second derivatives — the whole differentiable world unlocked."},
    {"id": "applications-of-derivatives", "title": "Applications of Derivatives",
     "blurb": "Tangent and normal lines, rise and fall, peaks and valleys certified two ways, concavity — and optimization, the art of the best."},
    {"id": "integrals", "title": "Integrals",
     "blurb": "Differentiation reversed, areas by slicing, and the Fundamental Theorem that collapses infinite sums into one subtraction."},
    {"id": "applications-of-integrals", "title": "Applications of Integrals",
     "blurb": "Areas between curves, motion recovered from velocity, average values — and a capstone running the whole course in one arc."},
]

# No legacy forms: this subject is authored fresh.
REMAP = {}
SOURCES = []

# form id -> fn(statement) -> ("num", sympy value) | ("opt", exact option str)
RESOLVERS = {}

_X = sp.Symbol("x")
_T = sp.Symbol("t")


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
    assert len(variants) >= lo, "%s: only %d variants" % (name, len(variants))
    return variants


def _term_tex(c, e, lead, var="x"):
    """One clean-signed latex term of c*var^e (c != 0)."""
    v = "" if e == 0 else (var if e == 1 else "%s^%d" % (var, e))
    m = abs(c)
    body = str(m) if not v else (v if m == 1 else "%d%s" % (m, v))
    if lead:
        return body if c > 0 else "-" + body
    return (" + " if c > 0 else " - ") + body


def _ptex(terms, var="x"):
    """Latex polynomial from [(coef, exp), ...] — no '+ -3', no '1x'."""
    out, lead = "", True
    for c, e in terms:
        if c == 0:
            continue
        out += _term_tex(c, e, lead, var)
        lead = False
    assert out, "empty polynomial"
    return out


def _py(terms, var="x"):
    """Sympifiable python source for the same polynomial (literal ints)."""
    parts = []
    for c, e in terms:
        if c == 0:
            continue
        if e == 0:
            parts.append("(%d)" % c)
        elif e == 1:
            parts.append("(%d)*%s" % (c, var))
        else:
            parts.append("(%d)*%s**%d" % (c, var, e))
    return " + ".join(parts)


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


def _parse_poly(latex, var="x"):
    """Latex like '-3x + 5', '4x^2 - 7x + 1', 't^3 + 2t' -> sympy expr."""
    t = latex.replace("^", "**").replace("\\,", "").replace(" ", "")
    t = re.sub(r"(\d)" + var, r"\1*" + var, t)
    t = re.sub(r"(?<![*\d])" + var, "1*" + var, t)
    return sympify(t)


# -------------------------------------------------------------------------
# Form 1: limit-substitution (limits-and-continuity, level 1) — CAL-lsub
# -------------------------------------------------------------------------
def _gen_limit_substitution():
    cands = [(2, 3, -5, 2), (3, -2, 4, 1), (1, 4, -3, 3), (2, -5, 3, 2),
             (3, 2, -7, -1), (1, -3, 5, 4), (2, 7, -1, 1), (4, -1, 6, 2),
             (1, 5, -2, -2), (3, -4, 2, 3), (2, 1, -9, 3), (1, 6, 4, -3),
             (5, -2, -3, 1), (2, -3, 6, -2)]
    variants, seen, i = [], set(), 0
    for (a, b, c, k) in cands:
        if len(variants) >= 12:
            break
        ans = a * k * k + b * k + c
        d1 = a * k * k - b * k + c          # substituted -k
        d2 = a * k * k + b * k              # dropped the constant term
        d3 = 2 * a * k + b                  # differentiated by reflex
        if not _distinct([ans, d1, d2, d3]):
            continue
        poly = _ptex([(a, 2), (b, 1), (c, 0)])
        stmt = "Evaluate $\\lim_{x \\to %d}(%s)$." % (k, poly)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-lsub-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "A polynomial is continuous, so the limit is just the value at "
            "$x = %d$: substituting gives $%d$. Plugging in $x = %d$ instead "
            "— a sign slip on the limit point — gives $%d$." % (k, ans, -k, d1),
            ["limit(%s, x, (%d)) == %d" % (_py([(a, 2), (b, 1), (c, 0)]), k, ans)]))
        i += 1
    return _floor("limit-substitution", variants)


def _rs_limit_substitution(s):
    m = re.search(r"\\lim_\{x \\to (-?\d+)\}\((.+?)\)\$", s)
    return ("num", _parse_poly(m.group(2)).subs(_X, int(m.group(1))))


# -------------------------------------------------------------------------
# Form 2: limit-factor-cancel (limits-and-continuity, level 2) — CAL-lfac
# -------------------------------------------------------------------------
def _gen_limit_factor_cancel():
    variants, seen, i = [], set(), 0
    # (a) (x^2 - k^2)/(x - k) -> 2k
    for k in [3, 4, 5, 6, 7, -2, -3, -4]:
        ans, dvals = 2 * k, [0, k, k * k]
        if not _distinct([ans] + dvals):
            continue
        num = _ptex([(1, 2), (-k * k, 0)])
        den = _ptex([(1, 1), (-k, 0)])
        stmt = "Evaluate $\\lim_{x \\to %d}\\frac{%s}{%s}$." % (k, num, den)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-lfac-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "Factor $%s = (%s)(%s)$, cancel the common factor, and "
            "substitute: $x + %d \\to %d$. Reading the $\\frac{0}{0}$ form "
            "as an answer of $0$ is the classic slip."
            % (num, den, _ptex([(1, 1), (k, 0)]), k, ans)
            if k >= 0 else
            "Factor $%s = (%s)(%s)$, cancel the common factor, and "
            "substitute to get $%d$. Reading the $\\frac{0}{0}$ form as an "
            "answer of $0$ is the classic slip."
            % (num, den, _ptex([(1, 1), (k, 0)]), ans),
            ["limit((x**2 - (%d))/(x - (%d)), x, (%d)) == %d"
             % (k * k, k, k, ans)]))
        i += 1
    # (b) (x - r)(x - s)/(x - r) -> r - s
    for (r, s_) in [(5, 2), (3, -1), (2, -4), (-2, 3), (4, 1), (6, 2)]:
        if len(variants) >= 12:
            break
        p, q = -(r + s_), r * s_
        assert p != 0 and q != 0
        ans, dvals = r - s_, [0, r, r + s_]
        if not _distinct([ans] + dvals):
            continue
        num = _ptex([(1, 2), (p, 1), (q, 0)])
        den = _ptex([(1, 1), (-r, 0)])
        stmt = "Evaluate $\\lim_{x \\to %d}\\frac{%s}{%s}$." % (r, num, den)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-lfac-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "The numerator factors as $(%s)(%s)$; cancel $%s$ and substitute "
            "$x = %d$ into the other factor to get $%d$. Answering $0$ from "
            "the $\\frac{0}{0}$ form is the classic slip."
            % (den, _ptex([(1, 1), (-s_, 0)]), den, r, ans),
            ["limit((x**2 + (%d)*x + (%d))/(x - (%d)), x, (%d)) == %d"
             % (p, q, r, r, ans)]))
        i += 1
    return _floor("limit-factor-cancel", variants)


def _rs_limit_factor_cancel(s):
    m = re.search(r"\\lim_\{x \\to (-?\d+)\}\\frac\{(.+?)\}\{(.+?)\}\$", s)
    k = int(m.group(1))
    expr = _parse_poly(m.group(2)) / _parse_poly(m.group(3))
    return ("num", sp.limit(expr, _X, k))


# -------------------------------------------------------------------------
# Form 3: limit-infinity (limits-and-continuity, level 2) — CAL-linf
# -------------------------------------------------------------------------
def _gen_limit_infinity():
    variants, seen, i = [], set(), 0
    same_deg = [(6, -1, 2, 3, 4, 5), (2, 3, 1, 4, -1, 3), (5, 2, -3, 2, 1, 4),
                (3, -4, 2, 6, 1, 5), (8, 1, 3, 2, -5, 6), (4, 5, -2, 3, 2, 7),
                (7, -2, 1, 2, 3, 4), (9, 2, -4, 3, -1, 2)]
    for (a, b, c, d, e, f) in same_deg:
        ans = Fraction(a, d)
        opts = [_fr_tex(ans), _fr_tex(Fraction(c, f)), "$\\infty$",
                _fr_tex(Fraction(d, a))]
        if not _distinct(opts):
            continue
        num = _ptex([(a, 2), (b, 1), (c, 0)])
        den = _ptex([(d, 2), (e, 1), (f, 0)])
        stmt = "Evaluate $\\lim_{x \\to \\infty}\\frac{%s}{%s}$." % (num, den)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-linf-v%02d" % (len(variants) + 1), stmt,
            opts[0], opts[1:], i,
            "The degrees match, so only the leading terms survive as "
            "$x \\to \\infty$: the limit is $\\frac{%d}{%d} = %s$. Taking "
            "the ratio of the constant terms, $%s$, is the classic slip."
            % (a, d, _fr_core(ans), _fr_core(Fraction(c, f))),
            ["limit(%s, x, oo) == Rational(%d, %d)"
             % ("(%s)/(%s)" % (_py([(a, 2), (b, 1), (c, 0)]),
                               _py([(d, 2), (e, 1), (f, 0)])),
                ans.numerator, ans.denominator)]))
        i += 1
    lower_deg = [(3, 2, 4, -1, 5), (2, -3, 5, 1, 4), (5, 1, 2, 3, -4),
                 (4, -1, 3, 2, 6)]
    for (a, b, c, d, e) in lower_deg:
        if len(variants) >= 12:
            break
        opts = ["$0$", _fr_tex(Fraction(a, c)), "$\\infty$",
                _fr_tex(Fraction(b, e))]
        if not _distinct(opts):
            continue
        num = _ptex([(a, 1), (b, 0)])
        den = _ptex([(c, 2), (d, 1), (e, 0)])
        stmt = "Evaluate $\\lim_{x \\to \\infty}\\frac{%s}{%s}$." % (num, den)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-linf-v%02d" % (len(variants) + 1), stmt,
            opts[0], opts[1:], i,
            "The denominator's degree is higher, so it grows faster and the "
            "ratio dies to $0$. Taking the ratio of the leading coefficients, "
            "$%s$, ignores the degree mismatch — that rule only applies when "
            "the degrees are equal." % _fr_core(Fraction(a, c)),
            ["limit(%s, x, oo) == 0"
             % ("(%s)/(%s)" % (_py([(a, 1), (b, 0)]),
                               _py([(c, 2), (d, 1), (e, 0)])))]))
        i += 1
    return _floor("limit-infinity", variants)


def _rs_limit_infinity(s):
    m = re.search(r"\\lim_\{x \\to \\infty\}\\frac\{(.+?)\}\{(.+?)\}\$", s)
    expr = _parse_poly(m.group(1)) / _parse_poly(m.group(2))
    return ("num", sp.limit(expr, _X, sp.oo))


# -------------------------------------------------------------------------
# Form 4: continuity-value (limits-and-continuity, level 3) — CAL-cont
# -------------------------------------------------------------------------
def _gen_continuity_value():
    variants, i = [], 0
    for k in [3, 4, 5, 6, 7, 8, -2, -3, -4, -5, -6, -7]:
        ans, dvals = 2 * k, [0, k, k * k]
        assert _distinct([ans] + dvals)
        num = _ptex([(1, 2), (-k * k, 0)])
        den = _ptex([(1, 1), (-k, 0)])
        stmt = ("For what value of $c$ is $f$ continuous, where "
                "$f(x) = \\frac{%s}{%s}$ for $x \\neq %d$ and $f(%d) = c$?"
                % (num, den, k, k))
        variants.append(_mk(
            "CAL-cont-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "Continuity forces $c = \\lim_{x \\to %d} f(x)$; cancel the "
            "factor $%s$ so the limit is $x + %d \\to %d$. Choosing $c = 0$ "
            "because the raw formula looks like $\\frac{0}{0}$ is the "
            "classic slip." % (k, den, k, ans) if k >= 0 else
            "Continuity forces $c = \\lim_{x \\to %d} f(x)$; cancel the "
            "factor $%s$ and substitute to get $%d$. Choosing $c = 0$ "
            "because the raw formula looks like $\\frac{0}{0}$ is the "
            "classic slip." % (k, den, ans),
            ["limit((x**2 - (%d))/(x - (%d)), x, (%d)) == %d"
             % (k * k, k, k, ans)]))
        i += 1
    return _floor("continuity-value", variants)


def _rs_continuity_value(s):
    m = re.search(r"\\frac\{(.+?)\}\{(.+?)\}", s)
    k = int(re.search(r"f\((-?\d+)\) = c", s).group(1))
    expr = _parse_poly(m.group(1)) / _parse_poly(m.group(2))
    return ("num", sp.limit(expr, _X, k))


# -------------------------------------------------------------------------
# Form 5: power-rule-at-point (the-derivative, level 1) — CAL-pow
# -------------------------------------------------------------------------
def _gen_power_rule_point():
    cands = [(2, 2, 3, 2), (3, 2, -4, 2), (2, 3, 5, 2), (4, 2, -3, 3),
             (2, 2, -5, 3), (3, 3, 2, 2), (5, 2, 4, 2), (2, 3, -1, 3),
             (3, 2, 5, -2), (4, 2, 1, 2), (2, 2, 7, 4), (3, 2, -2, 4),
             (5, 3, 3, 2), (2, 2, -7, -3)]
    variants, seen, i = [], set(), 0
    for (a, n, b, k) in cands:
        if len(variants) >= 12:
            break
        ans = a * n * k ** (n - 1) + b
        d1 = a * k ** n + b * k             # computed f(k) instead
        d2 = a * n * k ** n                 # kept the old exponent
        d3 = a * k ** (n - 1) + b           # dropped the factor n
        if not _distinct([ans, d1, d2, d3]):
            continue
        poly = _ptex([(a, n), (b, 1)])
        stmt = "If $f(x) = %s$, find $f'(%d)$." % (poly, k)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-pow-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "Power rule: $f'(x) = %s$, so $f'(%d) = %d$. Computing the "
            "function value $f(%d) = %d$ instead of the derivative is the "
            "classic mix-up." % (_ptex([(a * n, n - 1), (b, 0)]), k, ans, k, d1),
            ["diff(%s, x).subs(x, (%d)) == %d"
             % (_py([(a, n), (b, 1)]), k, ans)]))
        i += 1
    return _floor("power-rule-at-point", variants)


def _rs_power_rule_point(s):
    m = re.search(r"f\(x\) = (.+?)\$, find \$f'\((-?\d+)\)\$", s)
    return ("num", sp.diff(_parse_poly(m.group(1)), _X).subs(_X, int(m.group(2))))


# -------------------------------------------------------------------------
# Form 6: tangent-slope (the-derivative, level 2) — CAL-tan
# -------------------------------------------------------------------------
def _gen_tangent_slope():
    cands = [(4, 1, 2), (-3, 2, 4), (5, -2, 1), (2, -6, 3), (-4, 3, 2),
             (6, -1, 1), (-2, 5, 3), (3, 2, -2), (7, -3, 1), (4, -7, 2),
             (2, 3, -1), (-6, 2, 4), (5, 1, -2), (1, -4, 3), (3, -5, 2),
             (-5, 4, 3)]
    variants, seen, i = [], set(), 0
    for (b, c, k) in cands:
        if len(variants) >= 12:
            break
        ans = 2 * k + b
        d1 = k * k + b * k + c              # the y-value at k
        d2 = 2 * k                          # dropped b
        d3 = k + b                          # halved the x^2 rule
        if not _distinct([ans, d1, d2, d3]):
            continue
        poly = _ptex([(1, 2), (b, 1), (c, 0)])
        stmt = ("What is the slope of the tangent line to $y = %s$ at "
                "$x = %d$?" % (poly, k))
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-tan-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "The slope of the tangent is the derivative: $y' = %s$, so at "
            "$x = %d$ the slope is $%d$. Reporting the $y$-value $%d$ "
            "instead of the derivative is the classic slip."
            % (_ptex([(2, 1), (b, 0)]), k, ans, d1),
            ["diff(%s, x).subs(x, (%d)) == %d"
             % (_py([(1, 2), (b, 1), (c, 0)]), k, ans)]))
        i += 1
    return _floor("tangent-slope", variants)


def _rs_tangent_slope(s):
    m = re.search(r"y = (.+?)\$ at \$x = (-?\d+)\$", s)
    return ("num", sp.diff(_parse_poly(m.group(1)), _X).subs(_X, int(m.group(2))))


# -------------------------------------------------------------------------
# Form 7: derivative-function (the-derivative, level 1) — CAL-dfn
# -------------------------------------------------------------------------
def _gen_derivative_function():
    cands = [(2, 3, -4, 5), (1, -2, 3, -6), (3, 1, 2, -4), (2, -5, 1, 3),
             (1, 4, -2, 7), (4, -1, 5, 2), (2, 2, -3, -1), (3, -4, -2, 6),
             (1, -3, 4, 2), (5, 2, -1, -3), (2, 1, 6, -2), (3, 3, -5, 4),
             (1, 5, 2, -8)]
    variants, seen, i = [], set(), 0
    for (a, b, c, d) in cands:
        if len(variants) >= 12:
            break
        correct = "$%s$" % _ptex([(3 * a, 2), (2 * b, 1), (c, 0)])
        d1 = "$%s$" % _ptex([(3 * a, 2), (2 * b, 1), (c + d, 0)])   # kept d
        d2 = "$%s$" % _ptex([(3 * a, 3), (2 * b, 2), (c, 1)])       # powers not reduced
        d3 = "$%s$" % _ptex([(a, 2), (b, 1), (c, 0)])               # coefficients not multiplied
        if not _distinct([correct, d1, d2, d3]):
            continue
        poly = _ptex([(a, 3), (b, 2), (c, 1), (d, 0)])
        stmt = "If $f(x) = %s$, what is $f'(x)$?" % poly
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-dfn-v%02d" % (len(variants) + 1), stmt,
            correct, [d1, d2, d3], i,
            "Bring each exponent down as a factor and lower it by one; the "
            "constant $%d$ differentiates to zero. Leaving the coefficients "
            "un-multiplied, as in %s, is the classic slip." % (d, d3),
            ["diff(%s, x) == %s"
             % (_py([(a, 3), (b, 2), (c, 1), (d, 0)]),
                _py([(3 * a, 2), (2 * b, 1), (c, 0)]))]))
        i += 1
    return _floor("derivative-function", variants)


def _rs_derivative_function(s):
    m = re.search(r"f\(x\) = (.+?)\$, what is", s)
    d = sp.diff(_parse_poly(m.group(1)), _X)
    p = sp.Poly(d, _X)
    deg = p.degree()
    terms = [(int(c), deg - j) for j, c in enumerate(p.all_coeffs())]
    return ("opt", "$%s$" % _ptex(terms))


# -------------------------------------------------------------------------
# Form 8: product-rule-value (differentiation-techniques, level 3) — CAL-prod
# -------------------------------------------------------------------------
def _gen_product_rule_value():
    # (k, f(k), f'(k), g(k), g'(k))
    cands = [(1, 2, 3, 4, 5), (2, 3, -1, 2, 4), (3, 4, 2, -3, 1),
             (0, -2, 5, 3, 1), (2, 5, -3, 2, -1), (1, -3, 2, 4, 2),
             (4, 1, 6, 2, -3), (2, -4, 1, 5, 3), (3, 6, -2, 1, 4),
             (1, 7, 3, -2, 1), (2, -1, 4, 3, 5), (5, 2, -3, 4, 1),
             (3, 3, 5, 2, -2), (1, 4, -2, 5, 3)]
    variants, seen, i = [], set(), 0
    for (k, A, B, C, D) in cands:
        if len(variants) >= 12:
            break
        ans = B * C + A * D
        d1 = B * D                          # multiplied the derivatives
        d2 = A * C                          # multiplied the values
        d3 = B * C - A * D                  # minus instead of plus
        if A * D == 0 or not _distinct([ans, d1, d2, d3]):
            continue
        stmt = ("Let $h(x) = f(x)\\,g(x)$. Given $f(%d) = %d$, $f'(%d) = %d$, "
                "$g(%d) = %d$, $g'(%d) = %d$, find $h'(%d)$."
                % (k, A, k, B, k, C, k, D, k))
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-prod-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "Product rule: $h'(%d) = f'(%d)g(%d) + f(%d)g'(%d) = "
            "(%d)(%d) + (%d)(%d) = %d$. Multiplying the two derivatives, "
            "$(%d)(%d) = %d$, is the classic wrong move."
            % (k, k, k, k, k, B, C, A, D, ans, B, D, d1),
            ["(%d)*(%d) + (%d)*(%d) == %d" % (B, C, A, D, ans)]))
        i += 1
    return _floor("product-rule-value", variants)


def _rs_product_rule_value(s):
    A = int(re.search(r"\$f\(-?\d+\) = (-?\d+)\$", s).group(1))
    B = int(re.search(r"\$f'\(-?\d+\) = (-?\d+)\$", s).group(1))
    C = int(re.search(r"\$g\(-?\d+\) = (-?\d+)\$", s).group(1))
    D = int(re.search(r"\$g'\(-?\d+\) = (-?\d+)\$", s).group(1))
    return ("num", B * C + A * D)


# -------------------------------------------------------------------------
# Form 9: chain-rule-power (differentiation-techniques, level 2) — CAL-chn
# -------------------------------------------------------------------------
def _gen_chain_rule_power():
    cands = [(2, 1, 2, 1), (3, -2, 2, 2), (2, 3, 2, 1), (3, 1, 2, 1),
             (2, -5, 2, 4), (4, -3, 2, 2), (3, -4, 3, 2), (2, -1, 3, 3),
             (5, 2, 2, 1), (3, 2, 2, -1), (2, -4, 3, 3), (2, 7, 2, -2),
             (4, 1, 2, 2), (3, -7, 2, 4)]
    variants, seen, i = [], set(), 0
    for (a, b, n, k) in cands:
        if len(variants) >= 12:
            break
        u = a * k + b
        if u == 0:
            continue
        ans = n * a * u ** (n - 1)
        d1 = n * u ** (n - 1)               # forgot the inner derivative a
        d2 = a * n * u ** n                 # kept the outer exponent
        d3 = u ** n                         # just evaluated f(k)
        if not _distinct([ans, d1, d2, d3]):
            continue
        inner = _ptex([(a, 1), (b, 0)])
        stmt = "If $f(x) = (%s)^%d$, find $f'(%d)$." % (inner, n, k)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-chn-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "Chain rule: $f'(x) = %d(%s)^{%d} \\cdot %d$, and the inner value "
            "at $x = %d$ is $%d$, so $f'(%d) = %d \\cdot %d^{%d} \\cdot %d = "
            "%d$. Forgetting the inner derivative $%d$ gives $%d$."
            % (n, inner, n - 1, a, k, u, k, n, u, n - 1, a, ans, a, d1),
            ["diff((%s)**%d, x).subs(x, (%d)) == %d"
             % (_py([(a, 1), (b, 0)]), n, k, ans)]))
        i += 1
    return _floor("chain-rule-power", variants)


def _rs_chain_rule_power(s):
    m = re.search(r"f\(x\) = \((.+?)\)\^(\d)\$, find \$f'\((-?\d+)\)", s)
    inner = _parse_poly(m.group(1))
    n, k = int(m.group(2)), int(m.group(3))
    return ("num", sp.diff(inner ** n, _X).subs(_X, k))


# -------------------------------------------------------------------------
# Form 10: second-derivative (differentiation-techniques, level 2) — CAL-sec
# -------------------------------------------------------------------------
def _gen_second_derivative():
    cands = [(2, -5, 1), (-3, 2, 2), (1, -6, 2), (4, -2, 1), (2, 3, 2),
             (-2, 5, 3), (3, 2, 3), (-4, 1, 3), (5, -3, 1), (2, -7, 3),
             (-1, 6, 2), (-5, 4, 4), (1, 2, 4)]
    variants, seen, i = [], set(), 0
    for (a, b, k) in cands:
        if len(variants) >= 12:
            break
        ans = 6 * k + 2 * a
        d1 = 3 * k * k + 2 * a * k + b      # stopped at the velocity s'(k)
        d2 = k ** 3 + a * k * k + b * k     # the position s(k)
        d3 = 6 * k                          # dropped the 2a term
        if not _distinct([ans, d1, d2, d3]):
            continue
        poly = _ptex([(1, 3), (a, 2), (b, 1)], var="t")
        stmt = ("A particle's position is $s(t) = %s$. Find the acceleration "
                "$s''(%d)$." % (poly, k))
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-sec-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "Differentiate twice: $s''(t) = %s$, so $s''(%d) = %d$. Stopping "
            "after one derivative — the velocity $s'(%d) = %d$ — is the "
            "classic slip." % (_ptex([(6, 1), (2 * a, 0)], var="t"), k, ans,
                               k, d1),
            ["diff(%s, t, 2).subs(t, (%d)) == %d"
             % (_py([(1, 3), (a, 2), (b, 1)], var="t"), k, ans)]))
        i += 1
    return _floor("second-derivative", variants)


def _rs_second_derivative(s):
    m = re.search(r"s\(t\) = (.+?)\$", s)
    k = int(re.search(r"s''\((-?\d+)\)", s).group(1))
    return ("num", sp.diff(_parse_poly(m.group(1), "t"), _T, 2).subs(_T, k))


# -------------------------------------------------------------------------
# Form 11: critical-point (applications-of-derivatives, level 2) — CAL-crit
# -------------------------------------------------------------------------
def _gen_critical_point():
    variants, seen, i = [], set(), 0
    # (a) x^2 - 2ax + b: minimum at x = a
    for (a, b) in [(3, 5), (-2, 7), (4, -3), (-5, 2), (1, -6), (6, -1)]:
        if not _distinct([a, -a, b, 2 * a]):
            continue
        poly = _ptex([(1, 2), (-2 * a, 1), (b, 0)])
        stmt = ("For $f(x) = %s$, at which value of $x$ does $f$ reach its "
                "minimum?" % poly)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-crit-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % a, ["$%d$" % (-a), "$%d$" % b, "$%d$" % (2 * a)], i,
            "Set $f'(x) = %s = 0$ to get $x = %d$; $f''(x) = 2 > 0$ confirms "
            "a minimum. Flipping the sign to $x = %d$ — misreading the "
            "middle coefficient — is the classic slip."
            % (_ptex([(2, 1), (-2 * a, 0)]), a, -a),
            ["diff(%s, x).subs(x, (%d)) == 0"
             % (_py([(1, 2), (-2 * a, 1), (b, 0)]), a),
             "diff(%s, x, 2).subs(x, (%d)) > 0"
             % (_py([(1, 2), (-2 * a, 1), (b, 0)]), a)]))
        i += 1
    # (b) x^3 - 3p^2 x: critical points ±p, ask for the positive one
    for p in [1, 2, 3, 4, 5, 6]:
        M = 3 * p * p
        if not _distinct([p, -p, M, 2 * p]):
            continue
        poly = _ptex([(1, 3), (-M, 1)])
        stmt = ("The function $f(x) = %s$ has two critical points. What is "
                "the positive one?" % poly)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-crit-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % p, ["$%d$" % (-p), "$%d$" % M, "$%d$" % (2 * p)], i,
            "Solve $f'(x) = 3x^2 - %d = 0$: $x^2 = %d$, so $x = \\pm %d$ and "
            "the positive one is $%d$. Answering $%d$ — the other critical "
            "point — misses the word positive." % (M, p * p, p, p, -p),
            ["diff(x**3 - (%d)*x, x).subs(x, (%d)) == 0" % (M, p),
             "diff(x**3 - (%d)*x, x, 2).subs(x, (%d)) > 0" % (M, p)]))
        i += 1
    return _floor("critical-point", variants)


def _rs_critical_point(s):
    if "minimum" in s:
        m = re.search(r"f\(x\) = (.+?)\$", s)
        sols = sp.solve(sp.diff(_parse_poly(m.group(1)), _X), _X)
        assert len(sols) == 1
        return ("num", sols[0])
    m = re.search(r"x\^3 - (\d+)x\$", s)
    return ("num", sp.sqrt(sp.Rational(int(m.group(1)), 3)))


# -------------------------------------------------------------------------
# Form 12: tangent-line-y (applications-of-derivatives, level 3) — CAL-tany
# -------------------------------------------------------------------------
def _gen_tangent_line_y():
    variants, i = [], 0
    for p in [1, 3, 4, 5, 6, 7, -1, -3, -4, -5, -6, -7]:
        ans = -p * p
        dvals = [p * p, 0, 2 * p]
        assert _distinct([ans] + dvals)
        stmt = ("Find the $y$-coordinate of the point where the tangent line "
                "to $y = x^2$ at $x = %d$ crosses the $y$-axis." % p)
        variants.append(_mk(
            "CAL-tany-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "The tangent at $x = %d$ is $y = %d(x - (%d)) + %d$; setting "
            "$x = 0$ gives $y = %d$. Answering $%d$ — the height of the "
            "point of tangency — is the classic slip."
            % (p, 2 * p, p, p * p, ans, p * p),
            ["diff(x**2, x).subs(x, (%d))*(0 - (%d)) + (%d)**2 == (%d)"
             % (p, p, p, ans)]))
        i += 1
    return _floor("tangent-line-y", variants)


def _rs_tangent_line_y(s):
    p = int(re.search(r"at \$x = (-?\d+)\$", s).group(1))
    return ("num", -p * p)


# -------------------------------------------------------------------------
# Form 13: increasing-interval (applications-of-derivatives, level 3) — CAL-incr
# -------------------------------------------------------------------------
def _gen_increasing_interval():
    variants, i = [], 0
    for a in range(2, 14):
        M = 3 * a * a
        correct = "$(-%d;\\ %d)$" % (a, a)
        d1 = "$(-\\infty;\\ -%d)$" % a
        d2 = "$(%d;\\ \\infty)$" % a
        d3 = "$(-%d;\\ %d)$" % (a * a, a * a)
        stmt = ("On which interval is $f(x) = %s$ decreasing?"
                % _ptex([(1, 3), (-M, 1)]))
        variants.append(_mk(
            "CAL-incr-v%02d" % (len(variants) + 1), stmt,
            correct, [d1, d2, d3], i,
            "$f'(x) = 3x^2 - %d = 3(x - %d)(x + %d)$ is negative exactly "
            "between the roots, so $f$ decreases on $(-%d;\\ %d)$. The outer "
            "intervals are where $f'$ is positive — where $f$ increases."
            % (M, a, a, a, a),
            ["diff(x**3 - (%d)*x, x).subs(x, 0) < 0" % M,
             "diff(x**3 - (%d)*x, x).subs(x, (%d)) == 0" % (M, a),
             "diff(x**3 - (%d)*x, x).subs(x, (-%d)) == 0" % (M, a)]))
        i += 1
    return _floor("increasing-interval", variants)


def _rs_increasing_interval(s):
    m = re.search(r"x\^3 - (\d+)x\$", s)
    a = sp.sqrt(sp.Rational(int(m.group(1)), 3))
    assert a.is_integer
    return ("opt", "$(-%d;\\ %d)$" % (a, a))


# -------------------------------------------------------------------------
# Form 14: antiderivative (integrals, level 1) — CAL-anti
# -------------------------------------------------------------------------
def _gen_antiderivative():
    cands = [(6, 2, 5), (3, 2, -4), (9, 2, 2), (12, 2, -1), (4, 3, 3),
             (8, 3, -5), (12, 3, 2), (6, 2, -7), (9, 2, -3), (3, 2, 7),
             (4, 3, -2), (8, 3, 1)]
    variants, seen, i = [], set(), 0
    for (a, n, b) in cands:
        if len(variants) >= 12:
            break
        assert a % (n + 1) == 0 and b != 0
        A = a // (n + 1)
        correct = "$%s$" % _ptex([(A, n + 1), (b, 1)])
        d1 = "$%s$" % _ptex([(n * a, n - 1)])            # differentiated instead
        d2 = "$%s$" % _ptex([(a, n + 1), (b, 1)])        # kept the coefficient
        d3 = "$%s$" % _ptex([(A, n + 1)])                # dropped the bx term
        if not _distinct([correct, d1, d2, d3]):
            continue
        poly = _ptex([(a, n), (b, 0)])
        stmt = "Which of the following is an antiderivative of $f(x) = %s$?" % poly
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-anti-v%02d" % (len(variants) + 1), stmt,
            correct, [d1, d2, d3], i,
            "Raise each exponent by one and divide by the new exponent: "
            "$\\frac{%d}{%d}x^%d%s$ differentiates back to $f(x)$. "
            "Differentiating instead of integrating — the classic reversal — "
            "gives %s." % (a, n + 1, n + 1, _term_tex(b, 1, False), d1),
            ["diff(%s, x) == %s"
             % (_py([(A, n + 1), (b, 1)]), _py([(a, n), (b, 0)]))]))
        i += 1
    return _floor("antiderivative", variants)


def _rs_antiderivative(s):
    m = re.search(r"f\(x\) = (\d+)x\^(\d) ([+-]) (\d+)\$", s)
    a, n = int(m.group(1)), int(m.group(2))
    b = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
    A = Fraction(a, n + 1)
    assert A.denominator == 1
    return ("opt", "$%s$" % _ptex([(int(A), n + 1), (b, 1)]))


# -------------------------------------------------------------------------
# Form 15: definite-integral (integrals, level 2) — CAL-defint
# -------------------------------------------------------------------------
def _gen_definite_integral():
    cands = [(2, 3, 4), (4, -2, 3), (2, 5, 3), (6, -1, 2), (3, 2, 4),
             (2, -3, 5), (4, 1, 2), (2, 7, 2), (5, 4, 2), (3, -2, 2),
             (2, 1, 6), (6, 5, 3), (4, 3, 3)]
    variants, seen, i = [], set(), 0
    for (a, b, k) in cands:
        if len(variants) >= 12:
            break
        assert (a * k * k) % 2 == 0
        ans = (a * k * k) // 2 + b * k
        d1 = a * k + b                      # the integrand's value at k
        d2 = a * k * k + b * k              # forgot the 1/2
        d3 = -ans                           # computed F(0) - F(k)
        if ans == 0 or not _distinct([ans, d1, d2, d3]):
            continue
        integrand = _ptex([(a, 1), (b, 0)])
        stmt = "Evaluate $\\int_0^%d (%s)\\,dx$." % (k, integrand)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-defint-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
            "An antiderivative is $F(x) = %s$, so the integral is "
            "$F(%d) - F(0) = %d$. Forgetting to halve the $x^2$ term gives "
            "$%d$." % (_ptex([(a, 2), (2 * b, 1)]) if a % 2 else
                       _ptex([(a // 2, 2), (b, 1)]), k, ans, d2)
            if a % 2 == 0 else
            "An antiderivative is $F(x) = \\frac{%d}{2}x^2%s$, so the "
            "integral is $F(%d) - F(0) = %d$. Forgetting to halve the $x^2$ "
            "term gives $%d$." % (a, _term_tex(b, 1, False), k, ans, d2),
            ["integrate(%s, (x, 0, (%d))) == %d"
             % (_py([(a, 1), (b, 0)]), k, ans)]))
        i += 1
    return _floor("definite-integral", variants)


def _rs_definite_integral(s):
    m = re.search(r"\\int_0\^(\d+) \((.+?)\)\\,dx", s)
    k = int(m.group(1))
    return ("num", sp.integrate(_parse_poly(m.group(2)), (_X, 0, k)))


# -------------------------------------------------------------------------
# Form 16: area-under-line (applications-of-integrals, level 2) — CAL-area
# -------------------------------------------------------------------------
def _gen_area_under_line():
    variants, seen, i = [], set(), 0
    # (a) triangle under y = mx from 0 to k (16 variants)
    n = 0
    for m in range(2, 9):
        for k in (4, 6, 8):
            if n >= 16:
                break
            if k == 2 * m:
                continue
            ans = (m * k * k) // 2
            d1 = m * k                      # the height at x = k
            d2 = m * k * k                  # forgot the 1/2
            d3 = (k * k) // 2               # dropped the slope m
            if not _distinct([ans, d1, d2, d3]):
                continue
            stmt = ("Find the area under the line $y = %s$ from $x = 0$ to "
                    "$x = %d$." % (_ptex([(m, 1)]), k))
            if stmt in seen:
                continue
            seen.add(stmt)
            variants.append(_mk(
                "CAL-area-v%02d" % (len(variants) + 1), stmt,
                "$%d$" % ans, ["$%d$" % d1, "$%d$" % d2, "$%d$" % d3], i,
                "The region is a triangle with base $%d$ and height $%d \\cdot "
                "%d = %d$, so the area is $\\frac{1}{2} \\cdot %d \\cdot %d = "
                "%d$ — exactly what $\\int_0^%d %sx\\,dx$ gives. Forgetting "
                "the $\\frac{1}{2}$ gives $%d$."
                % (k, m, k, m * k, k, m * k, ans, k, m, d2),
                ["integrate((%d)*x, (x, 0, (%d))) == %d" % (m, k, ans),
                 "Rational(1, 2)*(%d)*((%d)*(%d)) == %d" % (k, m, k, ans)]))
            i += 1
            n += 1
    # (b) area under y = x^2 from 0 to k -> k^3/3 (8 variants)
    for k in [1, 2, 3, 5, 6, 7, 9, 10]:
        ans = Fraction(k ** 3, 3)
        d1 = Fraction(k ** 3)               # forgot the 1/3
        d2 = Fraction(k ** 4, 4)            # integrated to the wrong power
        d3 = Fraction(3 * k ** 3)           # multiplied by 3 instead
        if not _distinct([ans, d1, d2, d3]):
            continue
        stmt = ("Find the area under the parabola $y = x^2$ from $x = 0$ to "
                "$x = %d$." % k)
        if stmt in seen:
            continue
        seen.add(stmt)
        variants.append(_mk(
            "CAL-area-v%02d" % (len(variants) + 1), stmt,
            _fr_tex(ans), [_fr_tex(d1), _fr_tex(d2), _fr_tex(d3)], i,
            "$\\int_0^%d x^2\\,dx = \\frac{x^3}{3}\\Big|_0^%d = %s$. "
            "Forgetting to divide by $3$ gives $%s$."
            % (k, k, _fr_core(ans), _fr_core(d1)),
            ["integrate(x**2, (x, 0, (%d))) == Rational(%d, %d)"
             % (k, ans.numerator, ans.denominator)]))
        i += 1
    # applications-of-integrals is a one-form unit: keep it at >= 24 variants
    return _floor("area-under-line", variants, lo=24)


def _rs_area_under_line(s):
    k = int(re.search(r"to \$x = (\d+)\$", s).group(1))
    if "parabola" in s:
        return ("num", sp.Rational(k ** 3, 3))
    m = int(re.search(r"y = (\d+)x\$", s).group(1))
    return ("num", sp.Rational(m * k * k, 2))


def new_forms():
    """Unit-specific forms authored for this subject (ordered by unit)."""
    return [
        # ---- limits-and-continuity ----
        {"id": "limit-substitution", "title": "Limits by direct substitution",
         "level": 1, "unit": "limits-and-continuity",
         "skill": "Polynomials are continuous — the limit is just the value at the point.",
         "variants": _gen_limit_substitution()},
        {"id": "limit-factor-cancel", "title": "0/0 limits: factor and cancel",
         "level": 2, "unit": "limits-and-continuity",
         "skill": "Factor the numerator, cancel the vanishing factor, then substitute.",
         "variants": _gen_limit_factor_cancel()},
        {"id": "limit-infinity", "title": "Limits at infinity",
         "level": 2, "unit": "limits-and-continuity",
         "skill": "Equal degrees: ratio of leading coefficients. Bigger denominator degree: 0.",
         "variants": _gen_limit_infinity()},
        {"id": "continuity-value", "title": "Choosing c for continuity",
         "level": 3, "unit": "limits-and-continuity",
         "skill": "Continuity at the hole forces f(k) to equal the limit — cancel and substitute.",
         "variants": _gen_continuity_value()},
        # ---- the-derivative ----
        {"id": "power-rule-at-point", "title": "Power rule at a point",
         "level": 1, "unit": "the-derivative",
         "skill": "Bring the exponent down, lower it by one, then substitute the point.",
         "variants": _gen_power_rule_point()},
        {"id": "tangent-slope", "title": "Slope of the tangent line",
         "level": 2, "unit": "the-derivative",
         "skill": "The tangent's slope is the derivative evaluated at the point — not the y-value.",
         "variants": _gen_tangent_slope()},
        {"id": "derivative-function", "title": "The derivative as a function",
         "level": 1, "unit": "the-derivative",
         "skill": "Differentiate term by term: multiply by the exponent, drop it by one, kill constants.",
         "variants": _gen_derivative_function()},
        # ---- differentiation-techniques ----
        {"id": "product-rule-value", "title": "Product rule from a table",
         "level": 3, "unit": "differentiation-techniques",
         "skill": "(fg)' = f'g + fg' — never the product of the derivatives.",
         "variants": _gen_product_rule_value()},
        {"id": "chain-rule-power", "title": "Chain rule on a power",
         "level": 2, "unit": "differentiation-techniques",
         "skill": "Differentiate the outside, then multiply by the inner derivative.",
         "variants": _gen_chain_rule_power()},
        {"id": "second-derivative", "title": "Acceleration: the second derivative",
         "level": 2, "unit": "differentiation-techniques",
         "skill": "Acceleration is s'' — differentiate the position twice, then substitute.",
         "variants": _gen_second_derivative()},
        # ---- applications-of-derivatives ----
        {"id": "critical-point", "title": "Locating critical points",
         "level": 2, "unit": "applications-of-derivatives",
         "skill": "Set f'(x) = 0 and solve; the second derivative certifies a minimum.",
         "variants": _gen_critical_point()},
        {"id": "tangent-line-y", "title": "Where the tangent meets the y-axis",
         "level": 3, "unit": "applications-of-derivatives",
         "skill": "Build the tangent line y = f'(p)(x − p) + f(p), then set x = 0.",
         "variants": _gen_tangent_line_y()},
        {"id": "increasing-interval", "title": "Where the function decreases",
         "level": 3, "unit": "applications-of-derivatives",
         "skill": "f decreases exactly where f' < 0 — between the roots of f'.",
         "variants": _gen_increasing_interval()},
        # ---- integrals ----
        {"id": "antiderivative", "title": "Picking the antiderivative",
         "level": 1, "unit": "integrals",
         "skill": "Raise the exponent by one and divide by it — differentiate to verify.",
         "variants": _gen_antiderivative()},
        {"id": "definite-integral", "title": "Definite integrals of linear functions",
         "level": 2, "unit": "integrals",
         "skill": "Antidifferentiate, then compute F(k) − F(0) — the Fundamental Theorem.",
         "variants": _gen_definite_integral()},
        # ---- applications-of-integrals ----
        {"id": "area-under-line", "title": "Area under a graph",
         "level": 2, "unit": "applications-of-integrals",
         "skill": "Area under y = mx is a triangle (½·k·mk) — the integral agrees; under x² it is k³/3.",
         "variants": _gen_area_under_line()},
    ]


RESOLVERS.update({
    "limit-substitution": _rs_limit_substitution,
    "limit-factor-cancel": _rs_limit_factor_cancel,
    "limit-infinity": _rs_limit_infinity,
    "continuity-value": _rs_continuity_value,
    "power-rule-at-point": _rs_power_rule_point,
    "tangent-slope": _rs_tangent_slope,
    "derivative-function": _rs_derivative_function,
    "product-rule-value": _rs_product_rule_value,
    "chain-rule-power": _rs_chain_rule_power,
    "second-derivative": _rs_second_derivative,
    "critical-point": _rs_critical_point,
    "tangent-line-y": _rs_tangent_line_y,
    "increasing-interval": _rs_increasing_interval,
    "antiderivative": _rs_antiderivative,
    "definite-integral": _rs_definite_integral,
    "area-under-line": _rs_area_under_line,
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
