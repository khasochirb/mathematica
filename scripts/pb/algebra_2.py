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
    ]


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
