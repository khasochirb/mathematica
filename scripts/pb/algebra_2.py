# -*- coding: utf-8 -*-
"""Problem-bank subject: Algebra 2 — mirrors the /math/algebra-2 course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/algebra_2.py` for the self-check.
"""
import importlib.util
import os

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "algebra-2"
TITLE = "Algebra 2"
TITLE_MN = "Алгебр 2"
BLURB = ("Unit-by-unit practice for the Algebra 2 course — transformations, complex numbers, polynomials, logs, rationals, and sequences.")

UNITS = [
    {"id": "functions-and-transformations", "title": "Functions & Transformations",
     "blurb": "Function notation, domain and range, the four graph moves, absolute value, and piecewise functions."},
    {"id": "quadratics-and-complex-numbers", "title": "Quadratics & Complex Numbers",
     "blurb": "Vertex form and completing the square, the number i, complex roots, and quadratic inequalities."},
    {"id": "systems-and-nonlinear-models", "title": "Systems & Nonlinear Models",
     "blurb": "2×2 systems at speed, three variables, curves meeting lines, and feasible regions with the corner principle."},
    {"id": "polynomial-functions", "title": "Polynomial Functions",
     "blurb": "End behavior, division and the remainder/factor theorems, zeros with multiplicity, and cubic+ equations."},
    {"id": "radicals-and-rational-exponents", "title": "Radicals & Rational Exponents",
     "blurb": "Fractional powers, radical arithmetic, equations with phantom solutions, and inverse functions."},
    {"id": "exponentials-and-logarithms", "title": "Exponentials & Logarithms",
     "blurb": "Growth and decay, logs as the reverse gear, the three log laws, and solving both equation families."},
    {"id": "rational-functions", "title": "Rational Functions",
     "blurb": "Variation, asymptotes and holes, rational-expression arithmetic, and equations with work problems."},
    {"id": "sequences-and-series", "title": "Sequences & Series",
     "blurb": "Arithmetic ladders, geometric rockets, infinite sums, sigma notation, and recursion — the capstone."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "composition": "functions-and-transformations",
    "inverse-value": "functions-and-transformations",
    "log-evaluate": "exponentials-and-logarithms",
    "exp-equation": "exponentials-and-logarithms",
    "log-add-rule": "exponentials-and-logarithms",
    "exp-substitution": "exponentials-and-logarithms",
    "log-equation": "exponentials-and-logarithms",
    "log-chain": "exponentials-and-logarithms",
    "log-inequality": "exponentials-and-logarithms",
    "exp-inequality-flip": "exponentials-and-logarithms",
    "arith-nth": "sequences-and-series",
    "geo-nth": "sequences-and-series",
    "arith-find-d": "sequences-and-series",
    "arith-sum": "sequences-and-series",
    "geo-sum": "sequences-and-series",
    "which-term": "sequences-and-series",
    "infinite-geo": "sequences-and-series",
    "geo-two-terms": "sequences-and-series",
}

SOURCES = ['functions', 'logarithms', 'sequences']

# Independent re-solvers for the NEW forms below: form id -> fn(statement) ->
# ("num", sympy-comparable) | ("opt", exact option string) | ("assert", bool)
RESOLVERS = {}


def _load(name):
    spec = importlib.util.spec_from_file_location(
        "pbsrc_%s" % name, os.path.join(PB, "%s.py" % name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _remapped_forms():
    src = {}
    for name in SOURCES:
        for f in _load(name).build()["forms"]:
            src[f["id"]] = f
    forms = []
    for fid, unit in REMAP.items():
        f = dict(src[fid])
        f["unit"] = unit
        forms.append(f)
    return forms


# =========================================================================
# Authoring helpers for the new unit-specific forms
# =========================================================================
import math
import re as _re
from fractions import Fraction


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


def _pm(c):
    """Signed suffix term ' + 5' / ' - 5' (never '+ -5')."""
    return " + %d" % c if c >= 0 else " - %d" % (-c)


def _xpm(c):
    """Render 'x + c' with a clean sign; c == 0 -> 'x'."""
    return "x" if c == 0 else "x%s" % _pm(c)


def _sf(r):
    """Factor (x - r) with a clean sign."""
    return "(x - %d)" % r if r >= 0 else "(x + %d)" % (-r)


def _ctm(coef, var):
    """Signed term like ' + 3x^2', ' - x', ' + 5' (coef != 0, no '1x')."""
    sign = "+" if coef > 0 else "-"
    m = abs(coef)
    body = str(m) if not var else (var if m == 1 else "%d%s" % (m, var))
    return " %s %s" % (sign, body)


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


def _ctex(a, b):
    """Render a + bi (b != 0), hiding a unit coefficient on i."""
    im = "i" if abs(b) == 1 else "%di" % abs(b)
    return "%d %s %s" % (a, "+" if b > 0 else "-", im)


def _ytex(p, q):
    """Horizontal-asymptote option string 'y = p/q' in lowest terms."""
    return "$y = %s$" % _fr_core(Fraction(p, q))


_I_WORDS = {0: "$1$", 1: "$i$", 2: "$-1$", 3: "$-i$"}
_I_SYM = {0: "1", 1: "I", 2: "-1", 3: "-I"}


# -------------------------------------------------------------------------
# Form: complex-arithmetic (quadratics-and-complex-numbers, level 1)
# -------------------------------------------------------------------------
def _gen_complex_arithmetic():
    variants, seen = [], set()
    i = 0
    quads = []
    for a in [2, 3, -2, 4, -3, 5, 1, -4, -5, 2]:
        for (b, c, d) in [(3, 1, -2), (-2, 2, 1), (4, 3, 2), (1, -3, 5),
                          (-5, 2, 3), (2, -4, -1), (5, 1, 4), (-1, -2, -3)]:
            quads.append((a, b, c, d))

    def add_product(a, b, c, d, part):
        nonlocal i
        real, imag = a * c - b * d, a * d + b * c
        if real == 0 or imag == 0:
            return False
        if part == "REAL":
            correct, dvals = real, [a * c + b * d, imag, a * c]
            wrong = ("Adding $bd$ instead of subtracting it (forgetting "
                     "$i^2 = -1$) gives $%d$." % (a * c + b * d))
        else:
            correct, dvals = imag, [a * d - b * c, real, b * d]
            wrong = "A sign slip on one cross term gives $%d$." % (a * d - b * c)
        if not _distinct([correct] + dvals):
            return False
        stmt = ("Compute $(%s)(%s)$. What is the %s part of the result?"
                % (_ctex(a, b), _ctex(c, d), part))
        if stmt in seen:
            return False
        seen.add(stmt)
        fn = "re" if part == "REAL" else "im"
        variants.append(_mk(
            "A2-cmul-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % correct, ["$%d$" % v for v in dvals], i,
            "FOIL and use $i^2 = -1$: the product is $%s$, so the %s part is "
            "$%d$. %s" % (_ctex(real, imag), part.lower(), correct, wrong),
            ["%s(((%d) + (%d)*I)*((%d) + (%d)*I)) == %d"
             % (fn, a, b, c, d, correct)]))
        i += 1
        return True

    n = 0
    for (a, b, c, d) in quads[0::2]:
        if n >= 12:
            break
        if add_product(a, b, c, d, "REAL"):
            n += 1
    n = 0
    for (a, b, c, d) in quads[1::2]:
        if n >= 12:
            break
        if add_product(a, b, c, d, "IMAGINARY"):
            n += 1
    for n_exp in [5, 6, 7, 8, 10, 13, 15, 18, 21, 26, 31, 36]:
        r = n_exp % 4
        correct = _I_WORDS[r]
        dis = [_I_WORDS[k] for k in range(4) if k != r]
        variants.append(_mk(
            "A2-cmul-v%02d" % (len(variants) + 1),
            "Simplify $i^{%d}$." % n_exp, correct, dis, i,
            "Powers of $i$ cycle with period 4: $i^1 = i$, $i^2 = -1$, "
            "$i^3 = -i$, $i^4 = 1$. Since $%d = 4 \\cdot %d + %d$, "
            "$i^{%d} = i^{%d} = %s$."
            % (n_exp, n_exp // 4, r, n_exp, r, correct.strip("$")),
            ["I**%d == %s" % (n_exp, _I_SYM[r])]))
        i += 1
    assert len(variants) >= 34, "complex-arithmetic: %d" % len(variants)
    return variants


def _parse_ctex(t):
    import sympy as sp
    m = _re.fullmatch(r"(-?\d+) ([+-]) (\d*)i", t.strip())
    a = int(m.group(1))
    b = int(m.group(3)) if m.group(3) else 1
    if m.group(2) == "-":
        b = -b
    return a + b * sp.I


def _rs_complex_arithmetic(s):
    import sympy as sp
    m = _re.search(r"\$i\^\{(\d+)\}\$", s)
    if m:
        v = sp.I ** int(m.group(1))
        for r, sym in ((0, sp.Integer(1)), (1, sp.I),
                       (2, sp.Integer(-1)), (3, -sp.I)):
            if v == sym:
                return ("opt", _I_WORDS[r])
        raise ValueError("unreachable i power")
    m = _re.search(r"\$\(([^()]+)\)\(([^()]+)\)\$", s)
    z = sp.expand(_parse_ctex(m.group(1)) * _parse_ctex(m.group(2)))
    return ("num", sp.re(z) if "REAL part" in s else sp.im(z))


# -------------------------------------------------------------------------
# Form: complex-roots (quadratics-and-complex-numbers, level 3)
# -------------------------------------------------------------------------
def _gen_complex_roots():
    variants, seen = [], set()
    i = 0
    for m in [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]:
        for beta in [1, 2, 3, 4, 5, 6]:
            p, q = 2 * m, m * m + beta * beta
            vals = [beta, 2 * beta, m, q - p]
            if not _distinct(vals):
                continue
            D = p * p - 4 * q      # = -4 beta^2 < 0
            stmt = ("The equation $x^2%sx%s = 0$ has roots "
                    "$x = \\alpha \\pm \\beta i$ with $\\beta > 0$. Find $\\beta$."
                    % (_pm(p), _pm(q)))
            if stmt in seen:
                continue
            seen.add(stmt)
            variants.append(_mk(
                "A2-croots-v%02d" % (len(variants) + 1), stmt,
                "$%d$" % beta, ["$%d$" % v for v in vals[1:]], i,
                "$D = (%d)^2 - 4 \\cdot %d = %d < 0$, so "
                "$x = \\frac{%d \\pm \\sqrt{%d}\\,i}{2}$ and "
                "$\\beta = \\frac{\\sqrt{%d}}{2} = %d$. Forgetting to halve "
                "$\\sqrt{%d}$ gives $%d$."
                % (p, q, D, -p, -D, -D, beta, -D, 2 * beta),
                ["(%d)**2 - 4*(%d) == %d" % (p, q, D),
                 "sqrt(%d)/2 == %d" % (-D, beta),
                 "expand(((%d) + (%d)*I)**2 + (%d)*((%d) + (%d)*I) + (%d)) == 0"
                 % (-m, beta, p, -m, beta, q)]))
            i += 1
            if len(variants) >= 36:
                return variants
    return variants


def _rs_complex_roots(s):
    import sympy as sp
    m = _re.search(r"x\^2 ([+-]) (\d+)x \+ (\d+) = 0", s)
    p = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
    q = int(m.group(3))
    D = p * p - 4 * q
    assert D < 0
    return ("num", sp.sqrt(-D) / 2)


# -------------------------------------------------------------------------
# Form: line-parabola (systems-and-nonlinear-models, level 2)
# -------------------------------------------------------------------------
def _gen_line_parabola():
    tangent, two, zero = [], [], []
    for m in [2, -2, 4, -4, 6, -6]:
        for b in [1, -2, 3, 0]:
            tangent.append((m, b, b + (m * m) // 4))
    for m in [1, -1, 2, 3, -3, 5]:
        for dc in [-2, 0, -5]:
            for b in [0, 2, -1, 4]:
                if m * m - 4 * dc > 0:
                    two.append((m, b, b + dc))
    for m in [1, -1, 2, -2, 3, 4]:
        for up in [1, 2, 4]:
            for b in [0, 1, -3, 2]:
                zero.append((m, b, b + (m * m) // 4 + up))

    variants, seen = [], set()
    i = 0
    pools = [(two, 2), (tangent, 1), (zero, 0)]
    idxs = [0, 0, 0]
    while len(variants) < 36:
        progressed = False
        for pi in range(3):
            pool, count = pools[pi]
            while idxs[pi] < len(pool):
                m, b, c = pool[idxs[pi]]
                idxs[pi] += 1
                D = m * m - 4 * (c - b)
                got = 2 if D > 0 else (1 if D == 0 else 0)
                assert got == count, "line-parabola: engineered pool wrong"
                parab = "x^2" + (_pm(c) if c else "")
                mstr = "" if m == 1 else ("-" if m == -1 else "%d" % m)
                line = mstr + "x" + (_pm(b) if b else "")
                stmt = ("How many points do the graphs of $y = %s$ and "
                        "$y = %s$ share?" % (parab, line))
                if stmt in seen:
                    continue
                seen.add(stmt)
                cb = c - b
                eqtx = "x^2" + _ctm(-m, "x") + (_ctm(cb, "") if cb else "")
                sign = ">" if D > 0 else ("==" if D == 0 else "<")
                tail = {2: "positive, so the graphs meet twice",
                        1: "zero, so the line is tangent — exactly one shared point",
                        0: "negative, so the line misses the parabola"}[count]
                variants.append(_mk(
                    "A2-lp-v%02d" % (len(variants) + 1), stmt,
                    "$%d$" % count,
                    ["$%d$" % v for v in (0, 1, 2, 3) if v != count], i,
                    "Set them equal: $%s = 0$ has discriminant "
                    "$(%d)^2 - 4 \\cdot (%d) = %d$ — %s. Three is impossible: "
                    "a quadratic has at most two roots." % (eqtx, m, cb, D, tail),
                    ["(%d)**2 - 4*((%d) - (%d)) == %d" % (m, c, b, D),
                     "(%d) %s 0" % (D, sign)]))
                i += 1
                progressed = True
                break
            if len(variants) >= 36:
                break
        if not progressed:
            break
    assert len(variants) >= 34, "line-parabola: %d" % len(variants)
    return variants


def _rs_line_parabola(s):
    first, second = s.split(" and ")
    m1 = _re.search(r"\$y = x\^2(?: ([+-]) (\d+))?\$", first)
    c = 0
    if m1.group(1):
        c = int(m1.group(2)) * (1 if m1.group(1) == "+" else -1)
    m2 = _re.search(r"\$y = (-?\d*)x(?: ([+-]) (\d+))?\$", second)
    ms = m2.group(1)
    m = 1 if ms == "" else (-1 if ms == "-" else int(ms))
    b = 0
    if m2.group(2):
        b = int(m2.group(3)) * (1 if m2.group(2) == "+" else -1)
    D = m * m - 4 * (c - b)
    return ("opt", "$%d$" % (2 if D > 0 else (1 if D == 0 else 0)))


# -------------------------------------------------------------------------
# Form: nonlinear-system (systems-and-nonlinear-models, level 3)
# -------------------------------------------------------------------------
def _gen_nonlinear_system():
    variants, seen = [], set()
    i = 0
    slist = [5, -3, 7, 2, -6, 9, -8, 4, -1, 6, -4, 8, 3, -7, 1, -5, -2, 0]
    plist = [1, 2, -3, 4, -5, 6, -2, 3]
    for si, s in enumerate(slist):
        taken = 0
        for p in plist[si % 4:] + plist[:si % 4]:
            ans = s * s - 2 * p
            if ans <= 0:
                continue
            vals = [ans, s * s, s * s + 2 * p, s * s - p]
            if not _distinct(vals):
                continue
            stmt = "If $x + y = %d$ and $xy = %d$, find $x^2 + y^2$." % (s, p)
            if stmt in seen:
                continue
            seen.add(stmt)
            variants.append(_mk(
                "A2-nls-v%02d" % (len(variants) + 1), stmt,
                "$%d$" % ans, ["$%d$" % v for v in vals[1:]], i,
                "Square the sum: $(x + y)^2 = x^2 + 2xy + y^2$, so "
                "$x^2 + y^2 = (%d)^2 - 2 \\cdot (%d) = %d$. Forgetting to "
                "subtract $2xy$ leaves $%d$." % (s, p, ans, s * s),
                ["(%d)**2 - 2*(%d) == %d" % (s, p, ans),
                 "expand((x + y)**2 - 2*x*y) == x**2 + y**2"]))
            i += 1
            taken += 1
            if taken >= 2:
                break
    assert len(variants) >= 34, "nonlinear-system: %d" % len(variants)
    return variants


def _rs_nonlinear_system(s):
    m = _re.search(r"\$x \+ y = (-?\d+)\$ and \$xy = (-?\d+)\$", s)
    S, P = int(m.group(1)), int(m.group(2))
    return ("num", S * S - 2 * P)


# -------------------------------------------------------------------------
# Form: factored-cubic (polynomial-functions, level 1)
# -------------------------------------------------------------------------
def _gen_factored_cubic():
    trips = []
    for r1 in range(-6, 8):
        for r2 in range(r1 + 1, 8):
            for r3 in range(r2 + 1, 8):
                if 0 in (r1, r2, r3):
                    continue
                trips.append((r1, r2, r3))
    trips.sort(key=lambda t: (t[0] * 7 + t[1] * 13 + t[2] * 17) % 29)
    orders = [(0, 1, 2), (2, 0, 1), (1, 2, 0)]

    variants, seen = [], set()
    i = 0
    need = [12, 12, 12]     # sum-of-roots, p(0), largest-root
    for ti, roots in enumerate(trips):
        if len(variants) >= 36:
            break
        a, b, c = roots
        disp = [roots[j] for j in orders[ti % 3]]
        ftex = "".join(_sf(r) for r in disp)
        S = a + b + c
        P2 = a * b + a * c + b * c
        P3 = a * b * c
        for kind in [(ti + k) % 3 for k in range(3)]:
            if not need[kind]:
                continue
            if kind == 0:
                if S == 0:
                    continue
                vals = [S, -S, P2, P3]
                stmt = "For $p(x) = %s$, find the sum of the roots." % ftex
                expl = ("Set each factor to zero: the roots are $%d$, $%d$ and "
                        "$%d$, so their sum is $%d$. Flipping every root's sign "
                        "(reading $(x - r)$ as root $-r$) gives $%d$."
                        % (disp[0], disp[1], disp[2], S, -S))
                checks = ["(%d) + (%d) + (%d) == %d" % (a, b, c, S),
                          "expand((x - (%d))*(x - (%d))*(x - (%d))) == "
                          "x**3 - (%d)*x**2 + (%d)*x - (%d)"
                          % (a, b, c, S, P2, P3)]
                correct, dvals = S, [-S, P2, P3]
            elif kind == 1:
                vals = [-P3, P3, S, 0]
                stmt = "For $p(x) = %s$, find $p(0)$." % ftex
                expl = ("Substitute $x = 0$: each factor becomes minus its root, "
                        "so $p(0) = (%d)(%d)(%d) = %d$. Taking the plain product "
                        "of the roots, $%d$, misses the three sign flips."
                        % (-disp[0], -disp[1], -disp[2], -P3, P3))
                checks = ["(0 - (%d))*(0 - (%d))*(0 - (%d)) == %d"
                          % (a, b, c, -P3)]
                correct, dvals = -P3, [P3, S, 0]
            else:
                mx, mn = max(roots), min(roots)
                md = S - mx - mn
                vals = [mx, mn, md, -mx]
                stmt = "For $p(x) = %s$, what is the largest root?" % ftex
                expl = ("The roots are $%d$, $%d$ and $%d$; the largest is "
                        "$%d$. Careful with negatives: $%d$ is the smallest "
                        "root, not the largest." % (disp[0], disp[1], disp[2], mx, mn))
                checks = ["Max(%d, %d, %d) == %d" % (a, b, c, mx)]
                correct, dvals = mx, [mn, md, -mx]
            if not _distinct(vals):
                continue
            if stmt in seen:
                continue
            seen.add(stmt)
            variants.append(_mk(
                "A2-cubic-v%02d" % (len(variants) + 1), stmt,
                "$%d$" % correct, ["$%d$" % v for v in dvals], i,
                expl, checks))
            i += 1
            need[kind] -= 1
            break
    assert len(variants) >= 34, "factored-cubic: %d" % len(variants)
    return variants


def _rs_factored_cubic(s):
    roots = [int(v) if sg == "-" else -int(v)
             for sg, v in _re.findall(r"\(x ([+-]) (\d+)\)", s)]
    assert len(roots) == 3
    if "sum of the roots" in s:
        return ("num", sum(roots))
    if "p(0)" in s:
        return ("num", (-roots[0]) * (-roots[1]) * (-roots[2]))
    assert "largest root" in s
    return ("num", max(roots))


# -------------------------------------------------------------------------
# Form: remainder-theorem (polynomial-functions, level 2)
# -------------------------------------------------------------------------
def _gen_remainder():
    variants, seen = [], set()
    i = 0
    pairs = [(2, -3), (-3, 1), (1, 4), (-2, -5), (3, 2), (-4, 3), (2, 5), (-1, -2)]
    ks = [1, -1, 2, -2, 3, -3]
    alist = [1, -2, 2, -1, 3, -3]
    for (b, c) in pairs:
        for k in ks:
            for ai in range(len(alist)):
                a = alist[(len(variants) + ai) % len(alist)]
                r = k ** 3 + a * k * k + b * k + c
                d1 = -k ** 3 + a * k * k - b * k + c      # evaluated p(-k)
                d3 = -k ** 3 + a * k * k + b * k + c      # sign slip on x^3
                vals = [r, d1, c, d3]
                if not _distinct(vals):
                    continue
                cubic = "x^3" + _ctm(a, "x^2") + _ctm(b, "x") + _ctm(c, "")
                stmt = ("Find the remainder when $%s$ is divided by $%s$."
                        % (cubic, _sf(k)))
                if stmt in seen:
                    continue
                seen.add(stmt)
                variants.append(_mk(
                    "A2-rem-v%02d" % (len(variants) + 1), stmt,
                    "$%d$" % r, ["$%d$" % d1, "$%d$" % c, "$%d$" % d3], i,
                    "By the Remainder Theorem, dividing by $%s$ leaves "
                    "$p(%d)$; substituting gives $%d$. Evaluating at $x = %d$ "
                    "instead — misreading the divisor's sign — gives $%d$."
                    % (_sf(k), k, r, -k, d1),
                    ["rem(x**3 + (%d)*x**2 + (%d)*x + (%d), x - (%d), x) == %d"
                     % (a, b, c, k, r),
                     "(%d)**3 + (%d)*(%d)**2 + (%d)*(%d) + (%d) == %d"
                     % (k, a, k, b, k, c, r)]))
                i += 1
                break
            if len(variants) >= 36:
                return variants
    assert len(variants) >= 34, "remainder-theorem: %d" % len(variants)
    return variants


def _rs_remainder(s):
    m = _re.search(
        r"\$x\^3 ([+-]) (\d*)x\^2 ([+-]) (\d*)x ([+-]) (\d+)\$ is divided by "
        r"\$\(x ([+-]) (\d+)\)\$", s)

    def coef(sign, digits):
        v = int(digits) if digits else 1
        return v if sign == "+" else -v

    a = coef(m.group(1), m.group(2))
    b = coef(m.group(3), m.group(4))
    c = coef(m.group(5), m.group(6))
    k = int(m.group(8))
    if m.group(7) == "+":
        k = -k
    return ("num", k ** 3 + a * k * k + b * k + c)


# -------------------------------------------------------------------------
# Form: rational-exponents (radicals-and-rational-exponents, level 1)
# -------------------------------------------------------------------------
def _gen_rational_exponents():
    cases = []
    for r in [2, 3, 4, 5, 6, 7, 10]:
        for q in [2, 3, 4, 5]:
            n = r ** q
            if n > 1024:
                continue
            for p in [2, 3, 5, -1, -2, -3]:
                if math.gcd(abs(p), q) != 1:
                    continue
                val = Fraction(r) ** p
                if max(val.numerator, val.denominator) > 4000:
                    continue
                if n ** abs(p) > 100000:
                    continue
                cases.append((n, p, q, r, val))

    variants, seen = [], set()
    i = 0
    for (n, p, q, r, val) in cases:
        d1 = Fraction(n * p, q)        # multiplied n by the exponent
        d2 = Fraction(n) ** p          # forgot the q-th root
        d3 = 1 / val                   # reciprocal slip
        if not _distinct([val, d1, d2, d3]):
            continue
        stmt = "Evaluate $%d^{%d/%d}$." % (n, p, q)
        if stmt in seen:
            continue
        seen.add(stmt)
        root_tex = ("\\sqrt{%d}" % n) if q == 2 else ("\\sqrt[%d]{%d}" % (q, n))
        if p > 0:
            expl = ("Root first, then power: $%d^{%d/%d} = (%s)^{%d} "
                    "= %d^{%d} = %s$. Skipping the root and computing $%d^{%d}$ "
                    "gives %s." % (n, p, q, root_tex, p, r, p, _fr_core(val),
                                   n, p, _fr_tex(d2)))
        else:
            expl = ("The negative exponent flips to a reciprocal: "
                    "$%d^{%d/%d} = \\frac{1}{(%s)^{%d}} = "
                    "\\frac{1}{%d^{%d}} = %s$. Dropping the minus gives %s."
                    % (n, p, q, root_tex, -p, r, -p, _fr_core(val), _fr_tex(d3)))
        variants.append(_mk(
            "A2-rexp-v%02d" % (len(variants) + 1), stmt,
            _fr_tex(val), [_fr_tex(d1), _fr_tex(d2), _fr_tex(d3)], i,
            expl,
            ["Rational(%d)**Rational(%d, %d) == Rational(%d, %d)"
             % (n, p, q, val.numerator, val.denominator),
             "(%d)**(%d) == %d" % (r, q, n)]))
        i += 1
        if len(variants) >= 36:
            return variants
    assert len(variants) >= 34, "rational-exponents: %d" % len(variants)
    return variants


def _rs_rational_exponents(s):
    import sympy as sp
    m = _re.search(r"\$(\d+)\^\{(-?\d+)/(\d+)\}\$", s)
    n, p, q = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("num", sp.Integer(n) ** sp.Rational(p, q))


# -------------------------------------------------------------------------
# Form: simplify-radical (radicals-and-rational-exponents, level 2)
# -------------------------------------------------------------------------
def _gen_simplify_radical():
    variants = []
    i = 0
    for a in range(2, 13):
        for b in [2, 3, 5, 6, 7, 10]:
            if a == b:
                continue
            k = a * a * b
            # all four option values are positive; compare exact squares
            sq = [Fraction(a * a * b), Fraction(b * b * a),
                  Fraction(a * a * b * b), Fraction(k, 2) ** 2]
            if not _distinct(sq):
                continue
            variants.append(_mk(
                "A2-rad-v%02d" % (len(variants) + 1),
                "Simplify $\\sqrt{%d}$." % k,
                "$%d\\sqrt{%d}$" % (a, b),
                ["$%d\\sqrt{%d}$" % (b, a), "$%d$" % (a * b),
                 _fr_tex(Fraction(k, 2))], i,
                "Pull out the largest perfect square: $\\sqrt{%d} = "
                "\\sqrt{%d \\cdot %d} = %d\\sqrt{%d}$. Swapping the pieces to "
                "$%d\\sqrt{%d}$ is the classic slip."
                % (k, a * a, b, a, b, b, a),
                ["sqrt(%d) == %d*sqrt(%d)" % (k, a, b),
                 "(%d)**2 * (%d) == %d" % (a, b, k)]))
            i += 1
            if len(variants) >= 36:
                return variants
    assert len(variants) >= 34, "simplify-radical: %d" % len(variants)
    return variants


def _rs_simplify_radical(s):
    import sympy as sp
    m = _re.search(r"\\sqrt\{(\d+)\}", s)
    return ("num", sp.sqrt(int(m.group(1))))


# -------------------------------------------------------------------------
# Form: rational-function-features (rational-functions, level 2)
# -------------------------------------------------------------------------
def _gen_rational_features():
    variants, seen = [], set()
    i = 0
    # (a) vertical asymptote of (x + a)/(x - b) -> x = b
    n = 0
    for b in [3, -2, 5, -4, 1, -6, 2, -1, 4, -5, 6, -3, 7, -7]:
        if n >= 18:
            break
        for a in [4, -3, 2, 6, -5, 1, -2, 5]:
            if n >= 18:
                break
            if abs(a) == abs(b):
                continue
            stmt = ("Find the vertical asymptote of $f(x) = \\dfrac{%s}{%s}$."
                    % (_xpm(a), _xpm(-b)))
            if stmt in seen:
                continue
            seen.add(stmt)
            variants.append(_mk(
                "A2-rfa-v%02d" % (len(variants) + 1), stmt,
                "$x = %d$" % b,
                ["$x = %d$" % (-b), "$x = %d$" % (-a), "$x = %d$" % a], i,
                "A vertical asymptote sits where the denominator is zero: "
                "$%s = 0$ gives $x = %d$. The numerator's zero, $x = %d$, is "
                "the x-intercept — not an asymptote." % (_xpm(-b), b, -a),
                ["(%d) + (%d) == 0" % (b, -b),
                 "Abs((%d) + (%d)) > 0" % (b, a)]))
            i += 1
            n += 1
    # (b) horizontal asymptote of (ax + b)/(cx + d) -> y = a/c reduced
    n = 0
    for c in [2, 3, 4, 5, 6]:
        if n >= 18:
            break
        for a in [4, 3, 6, 2, 5, 8, 9, 10]:
            if n >= 18:
                break
            for (b, d) in [(1, 3), (-2, 5), (3, -4), (5, 2), (-1, -3), (2, 7)]:
                if n >= 18:
                    break
                fr = Fraction(a, c)
                if len({fr, Fraction(b, d), Fraction(c, a), Fraction(0)}) != 4:
                    continue
                stmt = ("Find the horizontal asymptote of "
                        "$f(x) = \\dfrac{%dx%s}{%dx%s}$."
                        % (a, _pm(b), c, _pm(d)))
                if stmt in seen:
                    continue
                seen.add(stmt)
                core = _fr_core(fr)
                if (fr.numerator, fr.denominator) == (a, c):
                    ratio_tex = core
                else:
                    ratio_tex = "\\frac{%d}{%d} = %s" % (a, c, core)
                variants.append(_mk(
                    "A2-rfa-v%02d" % (len(variants) + 1), stmt,
                    _ytex(a, c),
                    [_ytex(b, d), _ytex(c, a), "$y = 0$"], i,
                    "The degrees match, so the horizontal asymptote is the "
                    "ratio of the leading coefficients: $y = %s$. Taking the "
                    "ratio of the constants, $\\frac{%d}{%d}$, is the classic "
                    "slip." % (ratio_tex, b, d),
                    ["Rational(%d, %d) == Rational(%d, %d)"
                     % (a, c, fr.numerator, fr.denominator),
                     "limit(((%d)*x + (%d))/((%d)*x + (%d)), x, oo) == "
                     "Rational(%d, %d)"
                     % (a, b, c, d, fr.numerator, fr.denominator)]))
                i += 1
                n += 1
    assert len(variants) >= 34, "rational-function-features: %d" % len(variants)
    return variants


def _rs_rational_features(s):
    if "vertical asymptote" in s:
        m = _re.search(r"\\dfrac\{x ([+-]) (\d+)\}\{x ([+-]) (\d+)\}", s)
        v = int(m.group(4))
        b = v if m.group(3) == "-" else -v
        return ("opt", "$x = %d$" % b)
    m = _re.search(r"\\dfrac\{(\d+)x ([+-]) (\d+)\}\{(\d+)x ([+-]) (\d+)\}", s)
    return ("opt", _ytex(int(m.group(1)), int(m.group(4))))


def new_forms():
    """Unit-specific forms authored for this subject (appended by unit)."""
    return [
        {"id": "complex-arithmetic", "title": "Complex number arithmetic",
         "level": 1, "unit": "quadratics-and-complex-numbers",
         "skill": "Multiply with i² = −1; powers of i repeat every four steps.",
         "variants": _gen_complex_arithmetic()},
        {"id": "complex-roots", "title": "Reading β from complex roots",
         "level": 3, "unit": "quadratics-and-complex-numbers",
         "skill": "When D < 0 the roots are −p/2 ± (√|D|/2)i — halve the root of |D|.",
         "variants": _gen_complex_roots()},
        {"id": "line-parabola", "title": "Counting line–parabola intersections",
         "level": 2, "unit": "systems-and-nonlinear-models",
         "skill": "Set the curves equal and count roots with the discriminant.",
         "variants": _gen_line_parabola()},
        {"id": "nonlinear-system", "title": "Symmetric systems: x² + y²",
         "level": 3, "unit": "systems-and-nonlinear-models",
         "skill": "x² + y² = (x + y)² − 2xy — square the sum, subtract twice the product.",
         "variants": _gen_nonlinear_system()},
        {"id": "factored-cubic", "title": "Reading a factored cubic",
         "level": 1, "unit": "polynomial-functions",
         "skill": "Factored form hands you the roots: sum them, evaluate p(0), rank them.",
         "variants": _gen_factored_cubic()},
        {"id": "remainder-theorem", "title": "The remainder theorem",
         "level": 2, "unit": "polynomial-functions",
         "skill": "Dividing by (x − k) leaves remainder p(k) — just substitute.",
         "variants": _gen_remainder()},
        {"id": "rational-exponents", "title": "Evaluating rational exponents",
         "level": 1, "unit": "radicals-and-rational-exponents",
         "skill": "n^(p/q) = (q-th root of n)^p; a negative exponent means reciprocal.",
         "variants": _gen_rational_exponents()},
        {"id": "simplify-radical", "title": "Simplifying square roots",
         "level": 2, "unit": "radicals-and-rational-exponents",
         "skill": "√(a²·b) = a√b — pull the largest perfect square out of the radical.",
         "variants": _gen_simplify_radical()},
        {"id": "rational-function-features", "title": "Asymptotes of rational functions",
         "level": 2, "unit": "rational-functions",
         "skill": "Vertical: where the denominator dies. Horizontal (equal degrees): ratio of leading coefficients.",
         "variants": _gen_rational_features()},
    ] + _batch2_forms()


RESOLVERS.update({
    "complex-arithmetic": _rs_complex_arithmetic,
    "complex-roots": _rs_complex_roots,
    "line-parabola": _rs_line_parabola,
    "nonlinear-system": _rs_nonlinear_system,
    "factored-cubic": _rs_factored_cubic,
    "remainder-theorem": _rs_remainder,
    "rational-exponents": _rs_rational_exponents,
    "simplify-radical": _rs_simplify_radical,
    "rational-function-features": _rs_rational_features,
})


# =========================================================================
# Batch 2 — textbook exercise-set forms (12-variant target, floor >= 10)
# =========================================================================
def _mk12(vid, statement, correct, distractors, i, explanation, check):
    """Assembler for the 12-variant batch; same discipline as _mk."""
    opts = [correct] + list(distractors)
    assert len(set(opts)) == 4, "%s: option collision %r" % (vid, opts)
    options, ci = _place(correct, distractors, i)
    return {"id": vid, "statement": statement, "options": options,
            "correctIndex": ci, "explanation": explanation, "check": check}


def _floor12(name, variants):
    """Batch-2 target is ~12 variants; hard floor is 10 (check_subject)."""
    assert len(variants) >= 10, "%s: only %d variants" % (name, len(variants))
    return variants


# -------------------------------------------------------------------------
# Form: shift-vertex (functions-and-transformations, level 1)
# -------------------------------------------------------------------------
def _gen_shift_vertex():
    variants = []
    for i, (h, k) in enumerate([(2, 5), (-3, 4), (1, -6), (-4, -2), (5, 3),
                                (-1, 7), (3, -5), (-6, 1), (4, 6), (-2, -7),
                                (7, -1), (-5, 2)]):
        stmt = ("The graph of $y = %s^2%s$ has its vertex at which point?"
                % (_sf(h), _pm(k)))
        variants.append(_mk12(
            "A2-shift-v%02d" % (i + 1), stmt,
            "$(%d; %d)$" % (h, k),
            ["$(%d; %d)$" % (-h, k), "$(%d; %d)$" % (h, -k),
             "$(%d; %d)$" % (-h, -k)], i,
            "Vertex form $y = (x - h)^2 + k$ puts the vertex at $(h; k)$ — "
            "here $(%d; %d)$. The sign trap: reading $%s$ as $x = %d$ gives "
            "$(%d; %d)$." % (h, k, _sf(h), -h, -h, k),
            ["((%d) - (%d))**2 + (%d) == %d" % (h, h, k, k),
             "((%d) + 1 - (%d))**2 + (%d) > %d" % (h, h, k, k)]))
    return _floor12("shift-vertex", variants)


def _rs_shift_vertex(s):
    m = _re.search(r"\(x ([+-]) (\d+)\)\^2 ([+-]) (\d+)", s)
    h = int(m.group(2)) * (-1 if m.group(1) == "+" else 1)
    k = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
    return ("opt", "$(%d; %d)$" % (h, k))


# -------------------------------------------------------------------------
# Form: inverse-of-linear (functions-and-transformations, level 2)
# -------------------------------------------------------------------------
def _gen_inverse_linear():
    cands = [(2, 3, 4), (3, -2, 5), (4, 1, -3), (5, 2, 2), (2, -5, 6),
             (-2, 3, 4), (2, 7, -3), (3, 1, 6), (4, -3, 2), (5, 3, -1),
             (2, -1, 8), (3, 5, 3), (6, 1, 2), (3, 4, 7)]
    variants, i = [], 0
    for (a, b, t) in cands:
        if len(variants) >= 12:
            break
        c = a * t + b
        d1 = Fraction(a * c + b)     # applied f again instead of undoing it
        d2 = Fraction(c + b, a)      # sign slip on b
        d3 = Fraction(c - b)         # forgot to divide by a
        if not _distinct([Fraction(t), d1, d2, d3]):
            continue
        stmt = "If $f(x) = %dx%s$, find $f^{-1}(%d)$." % (a, _pm(b), c)
        variants.append(_mk12(
            "A2-invf-v%02d" % (len(variants) + 1), stmt,
            "$%d$" % t, [_fr_tex(d1), _fr_tex(d2), _fr_tex(d3)], i,
            "Undo $f$ in reverse: $f^{-1}(%d) = \\frac{%d - (%d)}{%d} = %d$. "
            "Plugging $%d$ into $f$ itself — the classic inverse slip — "
            "gives $%d$." % (c, c, b, a, t, c, a * c + b),
            ["((%d) - (%d))/(%d) == %d" % (c, b, a, t),
             "(%d)*(%d) + (%d) == %d" % (a, t, b, c)]))
        i += 1
    return _floor12("inverse-of-linear", variants)


def _rs_inverse_linear(s):
    import sympy as sp
    m = _re.search(r"f\(x\) = (-?\d+)x ([+-]) (\d+)", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    c = int(_re.search(r"f\^\{-1\}\((-?\d+)\)", s).group(1))
    return ("num", sp.Rational(c - b, a))


# -------------------------------------------------------------------------
# Form: transform-point-function (functions-and-transformations, level 2)
# -------------------------------------------------------------------------
def _gen_transform_point():
    specs = ([("k",) + t for t in [(3, 7, 4), (-2, 5, -3), (4, -1, 6),
                                   (-5, -3, 2)]]
             + [("h",) + t for t in [(2, 9, 3), (-4, 1, -2), (5, -6, 4),
                                     (1, 2, -5)]]
             + [("neg",) + t for t in [(3, 4, 0), (-2, 7, 0), (5, -3, 0),
                                       (-6, -1, 0)]])
    variants = []
    for i, (mode, p, q, t) in enumerate(specs):
        base = "The point $(%d; %d)$ lies on the graph of $y = f(x)$. " % (p, q)
        if mode == "k":
            stmt = base + ("Which point must lie on the graph of "
                           "$y = f(x)%s$?" % _pm(t))
            correct, dis = (p, q + t), [(p + t, q), (p, q - t), (p + t, q + t)]
            expl = ("Adding $%d$ outside $f$ slides the graph vertically, so "
                    "only the $y$-coordinate moves: $(%d; %d)$. Shifting the "
                    "$x$-coordinate instead gives $(%d; %d)$ — the classic "
                    "mix-up." % (t, p, q + t, p + t, q))
            checks = ["(%d) + (%d) == %d" % (q, t, q + t)]
        elif mode == "h":
            stmt = base + ("Which point must lie on the graph of "
                           "$y = f(%s)$?" % _xpm(-t))
            correct, dis = (p + t, q), [(p - t, q), (p, q + t), (p + t, q + t)]
            expl = ("Replacing $x$ by $%s$ shifts the graph %d unit(s) "
                    "%s, so the point moves to $(%d; %d)$. Sliding it the "
                    "other way to $(%d; %d)$ is the classic backwards slip."
                    % (_xpm(-t), abs(t), "right" if t > 0 else "left",
                       p + t, q, p - t, q))
            checks = ["(%d) + (%d) == %d" % (p, t, p + t)]
        else:
            stmt = base + "Which point must lie on the graph of $y = -f(x)$?"
            correct, dis = (p, -q), [(-p, q), (-p, -q), (p, q)]
            expl = ("The minus in front of $f$ reflects the graph across the "
                    "$x$-axis, flipping only the $y$-coordinate: $(%d; %d)$. "
                    "Reflecting across the $y$-axis instead gives $(%d; %d)$."
                    % (p, -q, -p, q))
            checks = ["-(%d) == %d" % (q, -q)]
        variants.append(_mk12(
            "A2-tpf-v%02d" % (i + 1), stmt, "$(%d; %d)$" % correct,
            ["$(%d; %d)$" % d for d in dis], i, expl, checks))
    return _floor12("transform-point-function", variants)


def _rs_transform_point(s):
    m = _re.search(r"point \$\((-?\d+); (-?\d+)\)\$", s)
    p, q = int(m.group(1)), int(m.group(2))
    if "-f(x)" in s:
        np_, nq = p, -q
    else:
        mk = _re.search(r"y = f\(x\) ([+-]) (\d+)\$", s)
        if mk:
            k = int(mk.group(2)) * (1 if mk.group(1) == "+" else -1)
            np_, nq = p, q + k
        else:
            mh = _re.search(r"y = f\(x ([+-]) (\d+)\)\$", s)
            inner = int(mh.group(2)) * (1 if mh.group(1) == "+" else -1)
            np_, nq = p - inner, q
    return ("opt", "$(%d; %d)$" % (np_, nq))


# -------------------------------------------------------------------------
# Form: conjugate-product (quadratics-and-complex-numbers, level 1)
# -------------------------------------------------------------------------
def _gen_conjugate_product():
    pairs = [(3, 2), (4, 1), (5, 3), (2, 5), (6, 1), (1, 4), (7, 2), (3, 5),
             (4, 3), (5, 2), (6, 5), (2, 3)]
    variants = []
    for i, (a, b) in enumerate(pairs):
        ans = a * a + b * b
        dvals = [a * a - b * b, (a + b) ** 2, a * a]
        assert _distinct([ans] + dvals)
        stmt = "Compute $(%s)(%s)$." % (_ctex(a, b), _ctex(a, -b))
        variants.append(_mk12(
            "A2-conj-v%02d" % (i + 1), stmt, "$%d$" % ans,
            ["$%d$" % v for v in dvals], i,
            "Conjugates multiply to $a^2 + b^2$: the cross terms cancel and "
            "$-(bi)^2 = +b^2$, so $%d + %d = %d$. Treating $i^2$ as $+1$ "
            "gives $a^2 - b^2 = %d$." % (a * a, b * b, ans, a * a - b * b),
            ["expand(((%d) + (%d)*I)*((%d) - (%d)*I)) == %d"
             % (a, b, a, b, ans),
             "(%d)**2 + (%d)**2 == %d" % (a, b, ans)]))
    return _floor12("conjugate-product", variants)


def _rs_conjugate_product(s):
    import sympy as sp
    m = _re.search(r"\$\(([^()]+)\)\(([^()]+)\)\$", s)
    z = sp.expand(_parse_ctex(m.group(1)) * _parse_ctex(m.group(2)))
    assert sp.im(z) == 0
    return ("num", sp.re(z))


# -------------------------------------------------------------------------
# Form: complex-magnitude (quadratics-and-complex-numbers, level 2)
# -------------------------------------------------------------------------
def _gen_complex_magnitude():
    pairs = [(3, 4), (6, 8), (5, 12), (8, 15), (7, 24), (20, 21), (9, 12),
             (12, 16), (-3, 4), (6, -8), (-5, 12), (8, -15)]
    variants = []
    for i, (a, b) in enumerate(pairs):
        c = math.isqrt(a * a + b * b)
        assert c * c == a * a + b * b
        dvals = [abs(a) + abs(b), a * a + b * b, max(abs(a), abs(b))]
        assert _distinct([c] + dvals)
        stmt = "Compute $|%s|$." % _ctex(a, b)
        variants.append(_mk12(
            "A2-cmag-v%02d" % (i + 1), stmt, "$%d$" % c,
            ["$%d$" % v for v in dvals], i,
            "The magnitude is $\\sqrt{a^2 + b^2} = \\sqrt{%d + %d} = %d$ — "
            "a Pythagorean pair. Adding $|a| + |b| = %d$ skips the squares, "
            "and stopping at $%d$ forgets the square root."
            % (a * a, b * b, c, abs(a) + abs(b), a * a + b * b),
            ["sqrt((%d)**2 + (%d)**2) == %d" % (a, b, c),
             "Abs((%d) + (%d)*I) == %d" % (a, b, c)]))
    return _floor12("complex-magnitude", variants)


def _rs_complex_magnitude(s):
    import sympy as sp
    m = _re.search(r"\$\|([^|$]+)\|\$", s)
    return ("num", sp.Abs(_parse_ctex(m.group(1))))


# -------------------------------------------------------------------------
# Form: complex-add-scale (quadratics-and-complex-numbers, level 1)
# -------------------------------------------------------------------------
def _gen_complex_add_scale():
    cands = [(2, 3, 2, 3, 1, -4), (3, 1, 5, 2, 4, -2), (2, -2, 3, 4, 1, 2),
             (3, 2, -1, 2, -3, 5), (4, 1, 2, 3, 2, -3), (2, 5, -3, 3, -1, 4),
             (3, -4, 2, 2, 5, 1), (2, 2, 7, 5, 1, -2), (4, -1, 3, 2, 3, 2),
             (3, 3, -2, 4, -2, 1), (2, 6, 1, 3, 2, 3), (5, 1, -2, 2, -4, 3),
             (2, -3, 4, 3, 5, -1), (3, 4, 3, 2, 1, 6), (4, 2, -5, 3, 3, 1),
             (2, 7, 2, 4, -1, -3)]
    variants, i = [], 0
    for idx, (mm, a, b, nn, c, d) in enumerate(cands):
        if len(variants) >= 12:
            break
        real, imag = mm * a + nn * c, mm * b + nn * d
        part = "imaginary" if idx % 2 == 0 else "real"
        if part == "imaginary":
            correct, dvals = imag, [real, mm * b - nn * d, b + d]
        else:
            correct, dvals = real, [imag, mm * a - nn * c, a + c]
        if not _distinct([correct] + dvals):
            continue
        stmt = ("Compute $%d(%s) + %d(%s)$. What is the %s part of the "
                "result?" % (mm, _ctex(a, b), nn, _ctex(c, d), part))
        fn = "im" if part == "imaginary" else "re"
        variants.append(_mk12(
            "A2-cadd-v%02d" % (len(variants) + 1), stmt, "$%d$" % correct,
            ["$%d$" % v for v in dvals], i,
            "Scale both parts of each number, then add: the result is "
            "$%s$, whose %s part is $%d$. Forgetting to multiply the inner "
            "parts by the scalars gives $%d$."
            % (_ctex(real, imag), part,
               correct, (b + d) if part == "imaginary" else (a + c)),
            ["%s((%d)*((%d) + (%d)*I) + (%d)*((%d) + (%d)*I)) == %d"
             % (fn, mm, a, b, nn, c, d, correct)]))
        i += 1
    return _floor12("complex-add-scale", variants)


def _rs_complex_add_scale(s):
    import sympy as sp
    m = _re.search(r"\$(\d+)\(([^()]+)\) \+ (\d+)\(([^()]+)\)\$", s)
    z = sp.expand(int(m.group(1)) * _parse_ctex(m.group(2))
                  + int(m.group(3)) * _parse_ctex(m.group(4)))
    return ("num", sp.im(z) if "imaginary part" in s else sp.re(z))


# -------------------------------------------------------------------------
# Form: circle-line-intersections (systems-and-nonlinear-models, level 2)
# -------------------------------------------------------------------------
def _gen_circle_line():
    cases = [(5, 3), (5, 5), (5, 7), (4, -2), (4, 4), (4, -6), (6, -5),
             (6, 6), (6, 8), (3, 2), (3, -3), (7, 10)]
    variants = []
    for i, (r, k) in enumerate(cases):
        r2 = r * r
        diff = r2 - k * k
        count = 2 if diff > 0 else (1 if diff == 0 else 0)
        stmt = ("How many points do the circle $x^2 + y^2 = %d$ and the "
                "line $y = %d$ have in common?" % (r2, k))
        if count == 2:
            tail = ("$x = \\pm\\sqrt{%d}$ — two points. Four is impossible: "
                    "a line meets a circle at most twice." % diff)
        elif count == 1:
            tail = ("only $x = 0$ — the line is tangent, one point. "
                    "Counting $\\pm 0$ as two points is the classic slip.")
        else:
            tail = ("no real solutions — the line misses the circle "
                    "entirely, zero points. Forgetting to compare $|%d|$ "
                    "with the radius $%d$ is the classic slip." % (k, r))
        sign = ">" if diff > 0 else ("==" if diff == 0 else "<")
        variants.append(_mk12(
            "A2-circ-v%02d" % (i + 1), stmt, "$%d$" % count,
            ["$%d$" % v for v in (0, 1, 2, 4) if v != count], i,
            "Substitute $y = %d$: $x^2 = %d - %d = %d$, giving %s"
            % (k, r2, k * k, diff, tail),
            ["(%d) - (%d)**2 %s 0" % (r2, k, sign),
             "(%d)**2 == %d" % (r, r2)]))
    return _floor12("circle-line-intersections", variants)


def _rs_circle_line(s):
    m = _re.search(r"x\^2 \+ y\^2 = (\d+)", s)
    r2 = int(m.group(1))
    k = int(_re.search(r"\$y = (-?\d+)\$", s).group(1))
    d = r2 - k * k
    return ("opt", "$%d$" % (2 if d > 0 else (1 if d == 0 else 0)))


# -------------------------------------------------------------------------
# Form: substitution-nonlinear (systems-and-nonlinear-models, level 3)
# -------------------------------------------------------------------------
def _gen_substitution_nonlinear():
    pairs = [(5, -2), (4, -1), (6, -3), (3, -5), (7, -2), (2, -6), (8, -3),
             (4, -7), (6, -1), (9, -4), (5, -8), (7, -4)]
    variants = []
    for i, (r, s2) in enumerate(pairs):
        a, b = r + s2, -r * s2
        dvals = [s2, a, -r]
        assert _distinct([r] + dvals)
        stmt = ("The parabola $y = x^2$ and the line $y = %dx%s$ intersect "
                "at two points. What is the larger $x$-coordinate of an "
                "intersection point?" % (a, _pm(b)))
        quad = "x^2" + _ctm(-a, "x") + _ctm(-b, "")
        variants.append(_mk12(
            "A2-subnl-v%02d" % (i + 1), stmt, "$%d$" % r,
            ["$%d$" % v for v in dvals], i,
            "Set $x^2 = %dx%s$ and factor: $%s = %s%s = 0$, so $x = %d$ or "
            "$x = %d$; the larger is $%d$. Grabbing the smaller root, $%d$, "
            "is the classic slip."
            % (a, _pm(b), quad, _sf(r), _sf(s2), r, s2, r, s2),
            ["(%d)**2 == (%d)*(%d) + (%d)" % (r, a, r, b),
             "expand((x - (%d))*(x - (%d))) == x**2 - (%d)*x - (%d)"
             % (r, s2, a, b),
             "(%d) > (%d)" % (r, s2)]))
    return _floor12("substitution-nonlinear", variants)


def _rs_substitution_nonlinear(s):
    import sympy as sp
    m = _re.search(r"\$y = (-?\d+)x ([+-]) (\d+)\$", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    x = sp.Symbol("x")
    return ("num", max(sp.solve(x**2 - a * x - b, x)))


# -------------------------------------------------------------------------
# Form: end-behavior (polynomial-functions, level 1)
# -------------------------------------------------------------------------
_ENDB = {(1, 0): "Rises to the right and rises to the left",
         (1, 1): "Rises to the right and falls to the left",
         (-1, 1): "Falls to the right and rises to the left",
         (-1, 0): "Falls to the right and falls to the left"}


def _gen_end_behavior():
    cases = [(1, 2, " - 4x + 1", " - 4*x + 1"),
             (2, 4, " - 3x^2 + 2", " - 3*x**2 + 2"),
             (3, 6, " + x - 5", " + x - 5"),
             (1, 3, " - 2x + 7", " - 2*x + 7"),
             (2, 5, " + x^2 - 3", " + x**2 - 3"),
             (4, 3, " - x^2 + 2", " - x**2 + 2"),
             (-1, 2, " + 5x - 2", " + 5*x - 2"),
             (-2, 4, " + x^3 - 1", " + x**3 - 1"),
             (-3, 6, " - 2x + 4", " - 2*x + 4"),
             (-1, 3, " + 4x - 6", " + 4*x - 6"),
             (-2, 5, " - x^2 + 3", " - x**2 + 3"),
             (-5, 3, " + 2x^2 - 1", " + 2*x**2 - 1")]
    variants = []
    for i, (a, n, ttex, tpy) in enumerate(cases):
        lead = ("x^%d" % n if a == 1 else
                "-x^%d" % n if a == -1 else "%dx^%d" % (a, n))
        key = (1 if a > 0 else -1, n % 2)
        correct = _ENDB[key]
        dis = [v for k2, v in sorted(_ENDB.items()) if k2 != key]
        right = "oo" if a > 0 else "-oo"
        left = "oo" if (a > 0) == (n % 2 == 0) else "-oo"
        ppy = "%d*x**%d%s" % (a, n, tpy)
        variants.append(_mk12(
            "A2-endb-v%02d" % (i + 1),
            "Describe the end behavior of the graph of $p(x) = %s%s$."
            % (lead, ttex),
            correct, dis, i,
            "The leading term $%s$ wins for large $|x|$: %s degree with a "
            "%s coefficient means the graph %s. Reading end behavior off "
            "the lower-order terms — which the leading term swamps — is "
            "the classic mistake."
            % (lead, "even" if n % 2 == 0 else "odd",
               "positive" if a > 0 else "negative", correct.lower()),
            ["limit(%s, x, oo) == %s" % (ppy, right),
             "limit(%s, x, -oo) == %s" % (ppy, left)]))
    return _floor12("end-behavior", variants)


def _rs_end_behavior(s):
    m = _re.search(r"p\(x\) = (-?\d*)x\^(\d+)", s)
    g = m.group(1)
    a = -1 if g == "-" else (1 if g == "" else int(g))
    n = int(m.group(2))
    return ("opt", _ENDB[(1 if a > 0 else -1, n % 2)])


# -------------------------------------------------------------------------
# Form: degree-of-product (polynomial-functions, level 1)
# -------------------------------------------------------------------------
def _gen_degree_product():
    dcases = [
        (3, 4, "(x^3 + 2x - 1)(x^4 - x + 5)",
         "(x**3 + 2*x - 1)*(x**4 - x + 5)"),
        (2, 5, "(x^2 - 3x + 2)(x^5 + x - 4)",
         "(x**2 - 3*x + 2)*(x**5 + x - 4)"),
        (4, 4, "(x^4 + x^2 - 3)(x^4 - 2x + 1)",
         "(x**4 + x**2 - 3)*(x**4 - 2*x + 1)"),
        (2, 3, "(x^2 + 5x + 6)(x^3 - x^2 + 2)",
         "(x**2 + 5*x + 6)*(x**3 - x**2 + 2)"),
        (3, 5, "(x^3 - 4x + 7)(x^5 + 2x^2 - 1)",
         "(x**3 - 4*x + 7)*(x**5 + 2*x**2 - 1)"),
        (4, 6, "(x^4 + 3x - 2)(x^6 - x^3 + 4)",
         "(x**4 + 3*x - 2)*(x**6 - x**3 + 4)")]
    lcases = [(3, 4, -2, 5), (5, 2, -3, 4), (-4, 3, 2, 6), (2, 3, -5, 2),
              (-2, 5, 7, 3), (6, 2, -3, 5)]
    variants, i = [], 0
    for idx in range(6):
        mdeg, ndeg, tex, py = dcases[idx]
        ans = mdeg + ndeg
        dvals = [mdeg * ndeg, max(mdeg, ndeg), ans - 1]
        assert _distinct([ans] + dvals)
        variants.append(_mk12(
            "A2-degp-v%02d" % (len(variants) + 1),
            "What is the degree of the product $%s$?" % tex,
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "Degrees add under multiplication: the leading terms multiply "
            "to $x^{%d} \\cdot x^{%d} = x^{%d}$. Multiplying the degrees "
            "to get $%d$ is the classic slip."
            % (mdeg, ndeg, ans, mdeg * ndeg),
            ["degree(expand(%s), x) == %d" % (py, ans),
             "(%d) + (%d) == %d" % (mdeg, ndeg, ans)]))
        i += 1
        a, mdeg2, b, ndeg2 = lcases[idx]
        ans2 = a * b
        dvals2 = [-ans2, a + b, mdeg2 + ndeg2]
        assert _distinct([ans2] + dvals2)
        variants.append(_mk12(
            "A2-degp-v%02d" % (len(variants) + 1),
            "What is the leading coefficient of the product "
            "$(%dx^%d)(%dx^%d)$?" % (a, mdeg2, b, ndeg2),
            "$%d$" % ans2, ["$%d$" % v for v in dvals2], i,
            "Coefficients multiply and exponents add: $(%d)(%d) = %d$ on "
            "$x^{%d}$. Adding the coefficients gives $%d$, and $%d$ is the "
            "degree — not the coefficient."
            % (a, b, ans2, mdeg2 + ndeg2, a + b, mdeg2 + ndeg2),
            ["(%d)*(%d) == %d" % (a, b, ans2),
             "expand(((%d)*x**%d)*((%d)*x**%d)) == (%d)*x**%d"
             % (a, mdeg2, b, ndeg2, ans2, mdeg2 + ndeg2)]))
        i += 1
    return _floor12("degree-of-product", variants)


def _rs_degree_product(s):
    if "leading coefficient" in s:
        m = _re.search(r"\((-?\d+)x\^(\d+)\)\((-?\d+)x\^(\d+)\)", s)
        return ("num", int(m.group(1)) * int(m.group(3)))
    exps = [int(e) for e in _re.findall(r"\(x\^(\d+)", s)]
    assert len(exps) == 2
    return ("num", exps[0] + exps[1])


# -------------------------------------------------------------------------
# Form: zeros-multiplicity (polynomial-functions, level 2)
# -------------------------------------------------------------------------
def _gen_zeros_multiplicity():
    tpairs = [(3, -1), (-2, 5), (4, 1), (-5, 2), (1, -4), (6, -2)]
    spairs = [(2, 3), (-3, 5), (4, -1), (-2, -5), (5, 2), (-4, 3)]
    variants, i = [], 0
    for idx in range(6):
        a, b = tpairs[idx]
        variants.append(_mk12(
            "A2-mult-v%02d" % (len(variants) + 1),
            "The graph of $p(x) = %s^2%s$ touches (without crossing) the "
            "$x$-axis at which zero?" % (_sf(a), _sf(b)),
            "$x = %d$" % a,
            ["$x = %d$" % b, "$x = %d$" % (-a), "$x = 0$"], i,
            "The squared factor makes $x = %d$ a double zero, so the graph "
            "touches and turns there; at $x = %d$ the single factor makes "
            "it cross. Picking the crossing zero is the classic mix-up."
            % (a, b),
            ["rem((x - (%d))**2*(x - (%d)), (x - (%d))**2, x) == 0"
             % (a, b, a),
             "Abs((%d) - (%d)) > 0" % (a, b)]))
        i += 1
        a2, b2 = spairs[idx]
        ans = a2 + b2
        dvals = [2 * a2 + b2, -(a2 + b2), a2 * b2]
        assert _distinct([ans] + dvals)
        variants.append(_mk12(
            "A2-mult-v%02d" % (len(variants) + 1),
            "Find the sum of the distinct zeros of $p(x) = %s^2%s$."
            % (_sf(a2), _sf(b2)),
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "The distinct zeros are $%d$ and $%d$, so the sum is $%d$. "
            "Counting the double zero twice — as if multiplicity added a "
            "root — gives $%d$." % (a2, b2, ans, 2 * a2 + b2),
            ["(%d) + (%d) == %d" % (a2, b2, ans),
             "((%d) - (%d))**2*((%d) - (%d)) == 0" % (a2, a2, a2, b2)]))
        i += 1
    return _floor12("zeros-multiplicity", variants)


def _rs_zeros_multiplicity(s):
    m = _re.search(r"\(x ([+-]) (\d+)\)\^2\(x ([+-]) (\d+)\)", s)
    a = int(m.group(2)) * (1 if m.group(1) == "-" else -1)
    b = int(m.group(4)) * (1 if m.group(3) == "-" else -1)
    if "touches" in s:
        return ("opt", "$x = %d$" % a)
    return ("num", a + b)


# -------------------------------------------------------------------------
# Form: add-radicals (radicals-and-rational-exponents, level 1)
# -------------------------------------------------------------------------
def _gen_add_radicals():
    cases = [(5, 2, 4, 3), (4, 3, 2, 2), (6, 2, 5, 5), (7, 3, 6, 2),
             (2, 6, 3, 7), (8, 2, 7, 6), (3, 5, 4, 10), (9, 4, 6, 3),
             (5, 4, 3, 11), (6, 3, 7, 13), (4, 2, 3, 5), (7, 2, 5, 6)]
    variants = []
    for i, (a, b, c, k) in enumerate(cases):
        m = a + b - c
        assert m >= 2
        variants.append(_mk12(
            "A2-radd-v%02d" % (i + 1),
            "Simplify $%d\\sqrt{%d} + %d\\sqrt{%d} - %d\\sqrt{%d}$."
            % (a, k, b, k, c, k),
            "$%d\\sqrt{%d}$" % (m, k),
            ["$%d\\sqrt{%d}$" % (a + b + c, k), "$%d$" % m,
             "$%d\\sqrt{%d}$" % (m, 2 * k)], i,
            "Like radicals combine through their coefficients: "
            "$(%d + %d - %d)\\sqrt{%d} = %d\\sqrt{%d}$. Ignoring the minus "
            "sign gives $%d\\sqrt{%d}$, and the radical itself never "
            "disappears." % (a, b, c, k, m, k, a + b + c, k),
            ["%d*sqrt(%d) + %d*sqrt(%d) - %d*sqrt(%d) == %d*sqrt(%d)"
             % (a, k, b, k, c, k, m, k)]))
    return _floor12("add-radicals", variants)


def _rs_add_radicals(s):
    m = _re.search(r"\$(\d+)\\sqrt\{(\d+)\} \+ (\d+)\\sqrt\{\d+\} - "
                   r"(\d+)\\sqrt\{\d+\}\$", s)
    a, k, b, c = (int(m.group(1)), int(m.group(2)), int(m.group(3)),
                  int(m.group(4)))
    return ("opt", "$%d\\sqrt{%d}$" % (a + b - c, k))


# -------------------------------------------------------------------------
# Form: multiply-radicals (radicals-and-rational-exponents, level 2)
# -------------------------------------------------------------------------
def _split_sq(n):
    """n -> (m, r) with n = m^2 * r and r square-free."""
    m, d = 1, 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
            m *= d
        d += 1
    return m, n


def _gen_multiply_radicals():
    cases = [(6, 8), (2, 6), (3, 6), (5, 10), (2, 10), (6, 10), (8, 10),
             (3, 15), (2, 8), (3, 12), (2, 18), (6, 24)]
    variants = []
    for i, (a, b) in enumerate(cases):
        prod = a * b
        mm, nn = _split_sq(prod)
        assert mm >= 2
        stmt = "Simplify $\\sqrt{%d} \\cdot \\sqrt{%d}$." % (a, b)
        if nn == 1:
            correct = "$%d$" % mm
            dis = ["$\\sqrt{%d}$" % (a + b), "$%d$" % prod, "$%d$" % (a + b)]
            expl = ("Multiply under one radical: $\\sqrt{%d} \\cdot "
                    "\\sqrt{%d} = \\sqrt{%d} = %d$. Adding the radicands to "
                    "get $\\sqrt{%d}$ is the classic slip, and $%d$ forgets "
                    "the square root." % (a, b, prod, mm, a + b, prod))
            checks = ["sqrt(%d)*sqrt(%d) == %d" % (a, b, mm)]
        else:
            correct = "$%d\\sqrt{%d}$" % (mm, nn)
            assert mm != nn
            dis = ["$\\sqrt{%d}$" % (a + b), "$%d$" % prod,
                   "$%d\\sqrt{%d}$" % (nn, mm)]
            expl = ("Multiply under one radical, then pull out the square: "
                    "$\\sqrt{%d} = \\sqrt{%d \\cdot %d} = %d\\sqrt{%d}$. "
                    "Adding the radicands to get $\\sqrt{%d}$ is the "
                    "classic slip." % (prod, mm * mm, nn, mm, nn, a + b))
            checks = ["sqrt(%d)*sqrt(%d) == %d*sqrt(%d)" % (a, b, mm, nn)]
        variants.append(_mk12("A2-rmul-v%02d" % (i + 1), stmt, correct,
                              dis, i, expl, checks))
    return _floor12("multiply-radicals", variants)


def _rs_multiply_radicals(s):
    m = _re.search(r"\\sqrt\{(\d+)\} \\cdot \\sqrt\{(\d+)\}", s)
    mm, nn = _split_sq(int(m.group(1)) * int(m.group(2)))
    if nn == 1:
        return ("opt", "$%d$" % mm)
    return ("opt", "$%d\\sqrt{%d}$" % (mm, nn))


# -------------------------------------------------------------------------
# Form: solve-radical (radicals-and-rational-exponents, level 2)
# -------------------------------------------------------------------------
def _gen_solve_radical():
    cands = [(5, 4), (-3, 2), (7, 3), (6, 5), (1, 4), (10, 6), (-6, 3),
             (-8, 2), (2, 6), (11, 4), (-4, 5), (9, 2), (3, 5), (12, 4)]
    variants, i = [], 0
    for (a, b) in cands:
        if len(variants) >= 12:
            break
        ans = b * b - a
        dvals = [b - a, a - b * b, (b - a) ** 2]
        if not _distinct([ans] + dvals):
            continue
        variants.append(_mk12(
            "A2-rsolve-v%02d" % (len(variants) + 1),
            "Solve $\\sqrt{%s} = %d$ for $x$." % (_xpm(a), b),
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "Square both sides: $x%s = %d$, so $x = %d - (%d) = %d$. Moving "
            "$%d$ across without squaring first gives $%d$."
            % (_pm(a), b * b, b * b, a, ans, a, b - a),
            ["sqrt((%d) + (%d)) == %d" % (ans, a, b),
             "(%d)**2 - (%d) == %d" % (b, a, ans)]))
        i += 1
    return _floor12("solve-radical", variants)


def _rs_solve_radical(s):
    m = _re.search(r"\\sqrt\{x ([+-]) (\d+)\} = (\d+)", s)
    a = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
    b = int(m.group(3))
    return ("num", b * b - a)


# -------------------------------------------------------------------------
# Form: simplify-rational (rational-functions, level 2)
# -------------------------------------------------------------------------
def _gen_simplify_rational():
    cands = [(3, 5), (2, 7), (4, 6), (5, 2), (3, -2), (6, 3), (2, -5),
             (7, 4), (4, -3), (5, 9), (8, 2), (3, 10), (2, 9), (6, -1)]
    variants, i = [], 0
    for (k, c) in cands:
        if len(variants) >= 12:
            break
        if c == k:
            continue
        ans = c + k
        dvals = [c - k, c, c * k]
        if not _distinct([ans] + dvals):
            continue
        variants.append(_mk12(
            "A2-rsimp-v%02d" % (len(variants) + 1),
            "Simplify $\\dfrac{x^2 - %d}{x - %d}$, then evaluate the result "
            "at $x = %d$." % (k * k, k, c),
            "$%d$" % ans, ["$%d$" % v for v in dvals], i,
            "Factor the difference of squares and cancel: "
            "$\\frac{(x - %d)(x + %d)}{x - %d} = x + %d$, which at "
            "$x = %d$ equals $%d$. Subtracting instead — as if it "
            "simplified to $x - %d$ — gives $%d$."
            % (k, k, k, k, c, ans, k, c - k),
            ["((%d)**2 - %d)/((%d) - %d) == %d" % (c, k * k, c, k, ans),
             "simplify((x**2 - %d)/(x - %d) - (x + %d)) == 0"
             % (k * k, k, k)]))
        i += 1
    return _floor12("simplify-rational", variants)


def _rs_simplify_rational(s):
    m = _re.search(r"\\dfrac\{x\^2 - (\d+)\}\{x - (\d+)\}", s)
    k = int(m.group(2))
    assert k * k == int(m.group(1))
    c = int(_re.search(r"at \$x = (-?\d+)\$", s).group(1))
    return ("num", c + k)


# -------------------------------------------------------------------------
# Form: add-rational-numeric (rational-functions, level 1)
# -------------------------------------------------------------------------
def _gen_add_rational_numeric():
    pairs = [(2, 3), (2, 5), (3, 4), (4, 6), (2, 7), (3, 5), (5, 6),
             (2, 9), (4, 5), (3, 8), (6, 10), (2, 4)]
    variants = []
    for i, (a, b) in enumerate(pairs):
        correct = Fraction(a + b, a * b)
        dvals = [Fraction(2, a + b), Fraction(1, a + b), Fraction(1, a * b)]
        assert _distinct([correct] + dvals)
        variants.append(_mk12(
            "A2-radd2-v%02d" % (i + 1),
            "Compute $\\dfrac{1}{%d} + \\dfrac{1}{%d}$." % (a, b),
            _fr_tex(correct), [_fr_tex(d) for d in dvals], i,
            "Use the common denominator $%d$: $\\frac{%d}{%d} + "
            "\\frac{%d}{%d} = %s$. Adding tops and bottoms separately — "
            "$\\frac{2}{%d}$ — is the classic mistake."
            % (a * b, b, a * b, a, a * b, _fr_core(correct), a + b),
            ["Rational(1, %d) + Rational(1, %d) == Rational(%d, %d)"
             % (a, b, correct.numerator, correct.denominator)]))
    return _floor12("add-rational-numeric", variants)


def _rs_add_rational_numeric(s):
    m = _re.search(r"\\dfrac\{1\}\{(\d+)\} \+ \\dfrac\{1\}\{(\d+)\}", s)
    a, b = int(m.group(1)), int(m.group(2))
    return ("opt", _fr_tex(Fraction(a + b, a * b)))


# -------------------------------------------------------------------------
# Form: hole-or-asymptote (rational-functions, level 3)
# -------------------------------------------------------------------------
_HOLE_OPTS = ["a hole", "a vertical asymptote", "an $x$-intercept",
              "a horizontal asymptote"]


def _gen_hole_or_asymptote():
    holes = [(2, -3), (-1, 4), (3, 5), (-4, -2), (5, -1), (-3, 1)]
    vas = [(1, -2, 3), (2, 4, -1), (-3, 1, 2), (5, -2, -4), (-1, -5, 3),
           (4, 2, 6)]
    variants, i = [], 0
    for idx in range(6):
        a, b = holes[idx]
        variants.append(_mk12(
            "A2-hole-v%02d" % (len(variants) + 1),
            "For $f(x) = \\dfrac{%s%s}{%s}$, what feature does the graph "
            "have at $x = %d$?" % (_sf(a), _sf(b), _xpm(-a), a),
            "a hole", [o for o in _HOLE_OPTS if o != "a hole"], i,
            "The factor $%s$ cancels, so near $x = %d$ the graph is just "
            "$y = %s$ with one point missing — a hole. Calling it a "
            "vertical asymptote is the classic confusion: an asymptote "
            "needs a denominator zero that does NOT cancel."
            % (_sf(a), a, _xpm(-b)),
            ["limit(((x - (%d))*(x - (%d)))/(x - (%d)), x, %d) == %d"
             % (a, b, a, a, a - b),
             "Abs((%d) - (%d)) > 0" % (a, b)]))
        i += 1
        a2, b2, c2 = vas[idx]
        numv = (c2 - a2) * (c2 - b2)
        variants.append(_mk12(
            "A2-hole-v%02d" % (len(variants) + 1),
            "For $f(x) = \\dfrac{%s%s}{%s}$, what feature does the graph "
            "have at $x = %d$?" % (_sf(a2), _sf(b2), _xpm(-c2), c2),
            "a vertical asymptote",
            [o for o in _HOLE_OPTS if o != "a vertical asymptote"], i,
            "At $x = %d$ the denominator vanishes while the numerator "
            "equals $%d \\ne 0$, so $f$ blows up — a vertical asymptote. "
            "A hole would need $%s$ to cancel with the numerator, and it "
            "doesn't." % (c2, numv, _xpm(-c2)),
            ["Abs(((%d) - (%d))*((%d) - (%d))) > 0" % (c2, a2, c2, b2)]))
        i += 1
    return _floor12("hole-or-asymptote", variants)


def _rs_hole_or_asymptote(s):
    m = _re.search(r"\\dfrac\{\(x ([+-]) (\d+)\)\(x ([+-]) (\d+)\)\}"
                   r"\{x ([+-]) (\d+)\}", s)

    def rt(sign, digits):
        v = int(digits)
        return v if sign == "-" else -v

    n1, n2, dr = (rt(m.group(1), m.group(2)), rt(m.group(3), m.group(4)),
                  rt(m.group(5), m.group(6)))
    v = int(_re.search(r"at \$x = (-?\d+)\$", s).group(1))
    assert v == dr
    if dr in (n1, n2):
        return ("opt", "a hole")
    return ("opt", "a vertical asymptote")


def _batch2_forms():
    """Batch-2 unit-specific forms (the textbook exercise-set expansion)."""
    return [
        {"id": "shift-vertex", "title": "Vertex from vertex form",
         "level": 1, "unit": "functions-and-transformations",
         "skill": "y = (x - h)^2 + k has vertex (h; k) — mind the sign on h.",
         "variants": _gen_shift_vertex()},
        {"id": "inverse-of-linear", "title": "Evaluating a linear inverse",
         "level": 2, "unit": "functions-and-transformations",
         "skill": "f^{-1}(c) undoes f: subtract b first, then divide by a.",
         "variants": _gen_inverse_linear()},
        {"id": "transform-point-function", "title": "Tracking a point through a transformation",
         "level": 2, "unit": "functions-and-transformations",
         "skill": "Outside changes move y, inside changes move x (backwards), a leading minus flips y.",
         "variants": _gen_transform_point()},
        {"id": "conjugate-product", "title": "Multiplying complex conjugates",
         "level": 1, "unit": "quadratics-and-complex-numbers",
         "skill": "(a + bi)(a - bi) = a^2 + b^2 — the cross terms cancel.",
         "variants": _gen_conjugate_product()},
        {"id": "complex-magnitude", "title": "Magnitude of a complex number",
         "level": 2, "unit": "quadratics-and-complex-numbers",
         "skill": "|a + bi| = sqrt(a^2 + b^2) — Pythagoras in the complex plane.",
         "variants": _gen_complex_magnitude()},
        {"id": "complex-add-scale", "title": "Scaling and adding complex numbers",
         "level": 1, "unit": "quadratics-and-complex-numbers",
         "skill": "m(a + bi) + n(c + di): scale real and imaginary parts separately, then add.",
         "variants": _gen_complex_add_scale()},
        {"id": "circle-line-intersections", "title": "Circle meets horizontal line",
         "level": 2, "unit": "systems-and-nonlinear-models",
         "skill": "Substitute y = k into x^2 + y^2 = r^2 and count real solutions of x^2 = r^2 - k^2.",
         "variants": _gen_circle_line()},
        {"id": "substitution-nonlinear", "title": "Parabola meets line by substitution",
         "level": 3, "unit": "systems-and-nonlinear-models",
         "skill": "Set x^2 = ax + b, factor, and read off both roots before answering.",
         "variants": _gen_substitution_nonlinear()},
        {"id": "end-behavior", "title": "End behavior of polynomials",
         "level": 1, "unit": "polynomial-functions",
         "skill": "Sign and parity of the leading term decide both ends of the graph.",
         "variants": _gen_end_behavior()},
        {"id": "degree-of-product", "title": "Degree and leading coefficient of a product",
         "level": 1, "unit": "polynomial-functions",
         "skill": "Degrees add, leading coefficients multiply.",
         "variants": _gen_degree_product()},
        {"id": "zeros-multiplicity", "title": "Zeros with multiplicity",
         "level": 2, "unit": "polynomial-functions",
         "skill": "Even multiplicity touches the x-axis; odd multiplicity crosses. Distinct zeros count once.",
         "variants": _gen_zeros_multiplicity()},
        {"id": "add-radicals", "title": "Adding like radicals",
         "level": 1, "unit": "radicals-and-rational-exponents",
         "skill": "a sqrt(k) + b sqrt(k) - c sqrt(k) = (a + b - c) sqrt(k) — combine coefficients only.",
         "variants": _gen_add_radicals()},
        {"id": "multiply-radicals", "title": "Multiplying square roots",
         "level": 2, "unit": "radicals-and-rational-exponents",
         "skill": "sqrt(a) * sqrt(b) = sqrt(ab), then pull out the largest perfect square.",
         "variants": _gen_multiply_radicals()},
        {"id": "solve-radical", "title": "Solving a basic radical equation",
         "level": 2, "unit": "radicals-and-rational-exponents",
         "skill": "sqrt(x + a) = b: square both sides first, then isolate x = b^2 - a.",
         "variants": _gen_solve_radical()},
        {"id": "simplify-rational", "title": "Cancel, then evaluate",
         "level": 2, "unit": "rational-functions",
         "skill": "(x^2 - k^2)/(x - k) = x + k for x != k — factor before substituting.",
         "variants": _gen_simplify_rational()},
        {"id": "add-rational-numeric", "title": "Adding unit fractions",
         "level": 1, "unit": "rational-functions",
         "skill": "1/a + 1/b = (a + b)/(ab) — never add tops and bottoms separately.",
         "variants": _gen_add_rational_numeric()},
        {"id": "hole-or-asymptote", "title": "Hole or vertical asymptote?",
         "level": 3, "unit": "rational-functions",
         "skill": "A cancelled factor leaves a hole; an uncancelled denominator zero is a vertical asymptote.",
         "variants": _gen_hole_or_asymptote()},
    ]


RESOLVERS.update({
    "shift-vertex": _rs_shift_vertex,
    "inverse-of-linear": _rs_inverse_linear,
    "transform-point-function": _rs_transform_point,
    "conjugate-product": _rs_conjugate_product,
    "complex-magnitude": _rs_complex_magnitude,
    "complex-add-scale": _rs_complex_add_scale,
    "circle-line-intersections": _rs_circle_line,
    "substitution-nonlinear": _rs_substitution_nonlinear,
    "end-behavior": _rs_end_behavior,
    "degree-of-product": _rs_degree_product,
    "zeros-multiplicity": _rs_zeros_multiplicity,
    "add-radicals": _rs_add_radicals,
    "multiply-radicals": _rs_multiply_radicals,
    "solve-radical": _rs_solve_radical,
    "simplify-rational": _rs_simplify_rational,
    "add-rational-numeric": _rs_add_rational_numeric,
    "hole-or-asymptote": _rs_hole_or_asymptote,
})


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = _remapped_forms() + new_forms()
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
